#!/usr/bin/env python3
"""
云盘大文件（zip / rar / 7z / 单个文档）→ GitHub Actions 运行器下载 → 解包 → 逐件抽全文 → 小体积文本入 Git，原件进 Release。
可移植精简版（约 400 行）。完整版见同仓库 scripts/drive_ingest/{ingest.py,files_job.py,runner_disk.py}。

输入（环境变量，由 workflow 从 ingest/RUN 读入）：
  SOURCE_IDS / SOURCE_RELEASE / LOCAL_FILES   来源三选一（见 RUN.example）
  SOURCE_MD5   可选，与 SOURCE_IDS 对齐的 md5，下载后校验
  OUT_NAME     必填，输出目录 data/<OUT_NAME>/
  TITLE, BACKUP=1, OCR=1, OCR_MIN_KB=8, WORKERS=4, CHECKPOINT_MIN=10, MAX_CHARS=2000000
  GIT_REF（分支名，workflow 注入）, GH_TOKEN（gh CLI 用）, WORK_DIR（大盘工作目录，默认 /mnt/work 或 /tmp/work）

输出（全部是小文本，可直接 git 提交）：
  data/<OUT_NAME>/manifest.json   每个成员：rel 路径 / ext / bytes / sha256 / status(ok|meta|dup|fail) / method / chars / same_as / error
  data/<OUT_NAME>/text/<slug>.json {"rel","text"}   抽出的全文（Word 段落+表格按原顺序；Excel 逐表逐行；PDF 逐页；PPT 逐页+备注；图片 OCR）
  data/<OUT_NAME>/_coverage.md    按类型统计 + 失败清单（代理只看这个就能判断是否「全保真」）
  data/<OUT_NAME>/_run_status.md  运行/中止原因（代理读不到 Actions 日志，只能看分支提交）
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
import traceback
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))      # 仓库根（脚本放在 <repo>/ingest/ 下）
OUT_NAME = (os.environ.get('OUT_NAME') or '').strip()
OUT = os.path.join(ROOT, 'data', OUT_NAME)
TITLE = os.environ.get('TITLE') or f'入库：{OUT_NAME}'
SOURCE_IDS = [x.strip() for x in os.environ.get('SOURCE_IDS', '').split(',') if x.strip()]
SOURCE_MD5 = [x.strip().lower() for x in os.environ.get('SOURCE_MD5', '').split(',')]
SOURCE_RELEASE = (os.environ.get('SOURCE_RELEASE') or '').strip()
LOCAL_FILES = [x.strip() for x in os.environ.get('LOCAL_FILES', '').split(',') if x.strip()]
BACKUP = os.environ.get('BACKUP', '1') == '1'
OCR = os.environ.get('OCR', '1') == '1'
OCR_MIN_KB = float(os.environ.get('OCR_MIN_KB', '8'))
WORKERS = int(os.environ.get('WORKERS', '4'))
CHECKPOINT_MIN = float(os.environ.get('CHECKPOINT_MIN', '10'))
MAX_CHARS = int(os.environ.get('MAX_CHARS', '2000000'))
GIT_REF = os.environ.get('GIT_REF', '')
IN_ACTIONS = bool(os.environ.get('GITHUB_ACTIONS'))
RELEASE_TAG = os.environ.get('RELEASE_TAG') or f'files-{OUT_NAME}'
DL_URL = 'https://drive.usercontent.google.com/download?id={id}&export=download&confirm=t'
DL_URL2 = 'https://drive.google.com/uc?export=download&id={id}&confirm=t'
ARCHIVE_EXT = {'.zip', '.rar', '.7z', '.tar', '.tgz', '.gz', '.bz2', '.xz'}
TEXT_EXT = {'.txt', '.md', '.csv', '.tsv', '.json', '.py', '.js', '.ts', '.html', '.htm', '.xml', '.yaml', '.yml', '.ini',
            '.cfg', '.conf', '.log', '.sql', '.sh', '.bat', '.r', '.ipynb', '.toml', '.env', '.rst', '.tex', '.m', '.c', '.h',
            '.cpp', '.java', '.go', '.rs', '.css', '.svg', '.mib', '.srt'}
IMG_EXT = {'.png', '.jpg', '.jpeg', '.webp', '.tif', '.tiff', '.bmp', '.gif'}
SKIP_NAMES = {'thumbs.db', 'desktop.ini', '.ds_store'}
T0 = time.time()


def log(*a):
    print(datetime.now(timezone.utc).strftime('%H:%M:%S'), *a, flush=True)


def run(cmd, timeout=600, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, **kw)


def have(cmd):
    return shutil.which(cmd) is not None


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 22), b''):
            h.update(chunk)
    return h.hexdigest()


def md5_file(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 22), b''):
            h.update(chunk)
    return h.hexdigest()


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=0)
    os.replace(tmp, path)


def status_note(text):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, '_run_status.md'), 'a', encoding='utf-8') as f:
        f.write(f"- {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} {text}\n")


def git_commit_push(msg):
    """把 data/<OUT_NAME> 提交回触发分支；运行器之外（本地调试）不提交。"""
    if not IN_ACTIONS or not GIT_REF:
        return
    run(['git', 'add', os.path.relpath(OUT, ROOT)], cwd=ROOT)
    r = run(['git', 'commit', '-q', '-m', msg], cwd=ROOT)
    if r.returncode != 0:
        return                                   # nothing to commit
    for attempt in range(4):
        run(['git', 'pull', '-q', '--rebase', '-X', 'theirs', 'origin', GIT_REF], cwd=ROOT, timeout=300)
        if run(['git', 'push', '-q', 'origin', f'HEAD:{GIT_REF}'], cwd=ROOT, timeout=300).returncode == 0:
            log('pushed:', msg)
            return
        time.sleep(10 + attempt * 10)
    log('push failed (will retry at next checkpoint)')


def abort(code, why):
    log('ABORT:', why)
    status_note(f'**ABORT（exit {code}）**：{why}')
    git_commit_push(f'ingest {OUT_NAME}: ABORT — {why[:80]}')
    sys.exit(code)


# ---------------------------------------------------------------- 1. 工作目录（运行器根盘只有 ~14 GB）
def work_dir():
    for d in (os.environ.get('WORK_DIR') or '', '/mnt/work', '/tmp/work'):
        if not d:
            continue
        try:
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, '.w'), 'w') as f:
                f.write('1')
            return d
        except OSError:
            continue
    return '/tmp'


WORK = work_dir()
RAW = os.path.join(WORK, 'raw')
UNPACK = os.path.join(WORK, 'unpacked')
os.environ['TMPDIR'] = os.path.join(WORK, 'tmp')
os.makedirs(os.environ['TMPDIR'], exist_ok=True)


# ---------------------------------------------------------------- 2. 下载（匿名链接；处理「无法扫描病毒」确认页 / 未共享 / 配额锁 / 断点续传）
def _confirm_url(body, fid):
    from html.parser import HTMLParser
    from urllib.parse import urlencode

    class P(HTMLParser):
        def __init__(self):
            super().__init__()
            self.forms, self.cur = [], None

        def handle_starttag(self, tag, attrs):
            a = dict(attrs)
            if tag == 'form':
                self.cur = {'action': a.get('action') or '', 'fields': {}}
                self.forms.append(self.cur)
            elif tag == 'input' and self.cur is not None and a.get('name'):
                self.cur['fields'][a['name']] = a.get('value') or ''

    p = P()
    try:
        p.feed(body)
    except Exception:  # noqa
        return None
    for f in p.forms:
        if 'download' in f['action'] or 'uc?' in f['action']:
            fields = dict(f['fields'])
            fields.setdefault('id', fid)
            fields.setdefault('export', 'download')
            fields.setdefault('confirm', 't')
            return f['action'] + ('&' if '?' in f['action'] else '?') + urlencode(fields)
    return None


def drive_download(fid, dest):
    """返回 (name, None) 或 (name, 错误串)。错误串以 NOT_SHARED / QUOTA_LOCKED 开头时重试无意义。"""
    import requests
    sess = requests.Session()
    ua = {'User-Agent': 'Mozilla/5.0'}
    name, expect, errs = fid, 0, []
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    for attempt in range(6):
        for url in (DL_URL, DL_URL2):
            url = url.format(id=fid)
            for hop in range(2):                              # hop 1 = 确认页之后的真正下载地址
                got = os.path.getsize(dest) if os.path.exists(dest) else 0
                h = dict(ua)
                if got and (not expect or got < expect):
                    h['Range'] = f'bytes={got}-'                 # Drive 支持 Range 续传
                try:
                    with sess.get(url, stream=True, timeout=(15, 120), headers=h) as r:
                        if r.status_code == 416 and expect and got >= expect:
                            return name, None
                        if r.status_code not in (200, 206):
                            errs.append(f'HTTP {r.status_code}')
                            time.sleep(5 + attempt * 10)
                            break
                        cd = r.headers.get('Content-Disposition', '')
                        m = re.search(r"filename\*=UTF-8''([^;]+)", cd) or re.search(r'filename="?([^";]+)"?', cd)
                        if m:
                            from urllib.parse import unquote
                            name = unquote(m.group(1))
                            try:
                                name = name.encode('latin-1').decode('utf-8')   # 中文文件名还原
                            except (UnicodeEncodeError, UnicodeDecodeError):
                                pass
                        if 'text/html' in r.headers.get('Content-Type', ''):
                            body = r.content[:300000].decode('utf-8', 'ignore')
                            if 'ServiceLogin' in body or 'accounts.google.com' in body or 'Request access' in body:
                                return name, 'NOT_SHARED: Drive 返回登录/申请权限页 —— 文件未设为「知道链接的任何人可查看」'
                            low = body.lower()
                            if 'quota' in low or 'too many users' in low:
                                return name, ('QUOTA_LOCKED: 「Too many users have viewed or downloaded this file recently」'
                                              '—— 该文件 ID 的匿名下载配额已锁（约 24 h）；别反复重试：等一天、或复制成新文件 ID、或改走 Release 来源')
                            nxt = _confirm_url(body, fid)
                            if nxt and hop == 0 and nxt != url:
                                url = nxt
                                continue
                            errs.append('HTML instead of file')
                            break
                        mode = 'ab' if r.status_code == 206 else 'wb'
                        if mode == 'wb':
                            got = 0
                        total = int(r.headers.get('Content-Length') or 0) + got
                        if not expect and total:
                            expect = total
                        with open(dest, mode) as f:
                            for chunk in r.iter_content(1 << 20):
                                f.write(chunk)
                    size = os.path.getsize(dest)
                    if expect and size < expect:
                        errs.append(f'partial {size}/{expect}, resuming')
                        continue
                    return name, None
                except Exception as e:  # noqa
                    errs.append(f'{type(e).__name__}: {str(e)[:100]}')
                    break
        time.sleep(3 + attempt * 5)
    try:                                                      # 最后兜底：gdown
        import gdown
        if os.path.exists(dest):
            os.remove(dest)
        if gdown.download(id=fid, output=dest, quiet=True) and os.path.getsize(dest) > 0:
            return name, None
    except Exception as e:  # noqa
        errs.append(f'gdown: {e}'[:120])
    return name, ' | '.join(dict.fromkeys(errs)) or 'download failed'


def resolve_sources():
    os.makedirs(RAW, exist_ok=True)
    if LOCAL_FILES:
        return [(os.path.basename(p), p) for p in LOCAL_FILES]
    if SOURCE_RELEASE:                                        # 来源 = 本仓库 Release（人工上传；不碰 Drive）
        d = os.path.join(RAW, 'release')
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
        r = run(['gh', 'release', 'download', SOURCE_RELEASE, '-D', d, '--clobber'], timeout=7200, cwd=ROOT)
        if r.returncode != 0:
            abort(3, f'release download failed ({SOURCE_RELEASE}): {(r.stderr or r.stdout)[-200:]}')
        parts = defaultdict(list)
        for fn in sorted(os.listdir(d)):                      # 合并 split 分卷 name.part00 / name.part01 …
            m = re.fullmatch(r'(.+)\.part(\d+)', fn)
            if m:
                parts[m.group(1)].append(fn)
        for base, fns in parts.items():
            with open(os.path.join(d, base), 'wb') as w:
                for fn in sorted(fns):
                    with open(os.path.join(d, fn), 'rb') as rf:
                        shutil.copyfileobj(rf, w, 1 << 20)
                    os.remove(os.path.join(d, fn))
        return [(fn, os.path.join(d, fn)) for fn in sorted(os.listdir(d))]
    if not SOURCE_IDS:
        abort(1, 'no source: set SOURCE_IDS / SOURCE_RELEASE / LOCAL_FILES')
    out = []
    for i, fid in enumerate(SOURCE_IDS):
        dest = os.path.join(RAW, fid + '.bin')
        log('download', fid)
        name, err = drive_download(fid, dest)
        if err:
            abort(2 if err.startswith('NOT_SHARED') else 3, f'download failed {fid}: {err}')
        want = SOURCE_MD5[i] if i < len(SOURCE_MD5) else ''
        if re.fullmatch(r'[0-9a-f]{32}', want or ''):
            got = md5_file(dest)
            log(f'md5 {got} {"==" if got == want else "!="} {want}')
            if got != want:
                abort(3, f'md5 mismatch for {fid}: {got} != {want}')
        final = os.path.join(RAW, re.sub(r'[^\w.\-]+', '_', name) if name != fid else dest)
        if final != dest:
            os.replace(dest, final)
        log('source', name, os.path.getsize(final), 'bytes')
        out.append((name, final))
    return out


# ---------------------------------------------------------------- 3. 原件备份到 Release（≤2 GiB/资产，超过就 split）
def backup(paths):
    if not (BACKUP and IN_ACTIONS and have('gh')):
        return
    if run(['gh', 'release', 'view', RELEASE_TAG], cwd=ROOT).returncode != 0:
        run(['gh', 'release', 'create', RELEASE_TAG, '--title', f'{OUT_NAME} 原件备份', '--notes', TITLE], cwd=ROOT)
    for name, p in paths:
        ups = [p]
        if os.path.getsize(p) > int(1.9 * 1024 ** 3):
            d = os.path.join(WORK, 'split')
            shutil.rmtree(d, ignore_errors=True)
            os.makedirs(d)
            run(['split', '-b', '1800m', '-d', '-a', '2', p, os.path.join(d, os.path.basename(p) + '.part')], timeout=3600)
            ups = [os.path.join(d, x) for x in sorted(os.listdir(d))]
        r = run(['gh', 'release', 'upload', RELEASE_TAG, *ups, '--clobber'], timeout=7200, cwd=ROOT)
        log('release upload', name, 'ok' if r.returncode == 0 else r.stderr[-200:])


# ---------------------------------------------------------------- 4. 解包（递归；修正 Windows GBK 文件名；解完删内层压缩包省盘）
def _fix_name(zi):
    if zi.flag_bits & 0x800:
        return zi.filename                                     # 已是 UTF-8
    raw = zi.filename.encode('cp437', 'replace')
    for enc in ('gb18030', 'utf-8', 'big5', 'shift_jis'):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return zi.filename


def unpack(path, dest, depth=0):
    ext = os.path.splitext(path)[1].lower()
    os.makedirs(dest, exist_ok=True)
    if ext == '.zip':
        with zipfile.ZipFile(path) as z:
            for zi in z.infolist():
                name = _fix_name(zi).replace('\\', '/')
                if zi.is_dir() or name.startswith('__MACOSX/') or os.path.basename(name).startswith('._'):
                    continue
                target = os.path.normpath(os.path.join(dest, name))
                if not target.startswith(os.path.abspath(dest)):
                    continue                                   # zip-slip 防护
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with z.open(zi) as src, open(target, 'wb') as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
    elif ext in ('.tar', '.tgz', '.gz', '.bz2', '.xz') and tarfile.is_tarfile(path):
        with tarfile.open(path) as t:
            t.extractall(dest, filter='data') if hasattr(tarfile, 'data_filter') else t.extractall(dest)
    elif have('7z'):
        r = run(['7z', 'x', '-y', f'-o{dest}', path], timeout=7200)
        if r.returncode not in (0, 1):
            raise RuntimeError('7z failed: ' + (r.stderr or r.stdout)[-200:])
    else:
        raise RuntimeError('no extractor for ' + ext)
    if depth < 3:                                              # 内层压缩包继续解
        for dp, _, fns in os.walk(dest):
            for fn in fns:
                p = os.path.join(dp, fn)
                if os.path.splitext(fn)[1].lower() in ARCHIVE_EXT and (zipfile.is_zipfile(p) or tarfile.is_tarfile(p) or fn.lower().endswith(('.rar', '.7z'))):
                    try:
                        unpack(p, p + '__unpacked', depth + 1)
                        os.remove(p)
                    except Exception as e:  # noqa
                        log('inner archive failed', p, e)


# ---------------------------------------------------------------- 5. 抽取器（够用版；完整版见 ingest.py）
def read_text(p):
    b = open(p, 'rb').read(MAX_CHARS * 4)
    for enc in ('utf-8-sig', 'gb18030', 'latin-1'):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            continue
    return b.decode('utf-8', 'ignore')


def extract_docx(p):
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    d = docx.Document(p)
    out = []
    for el in d.element.body.iterchildren():                   # 段落与表格按原顺序
        tag = el.tag.rsplit('}', 1)[-1]
        if tag == 'p':
            t = Paragraph(el, d).text.strip()
            if t:
                out.append(t)
        elif tag == 'tbl':
            for row in Table(el, d).rows:
                cells = []
                for c in row.cells:
                    ct = ' '.join(c.text.split())
                    if not cells or cells[-1] != ct:           # 合并单元格去重
                        cells.append(ct)
                out.append(' | '.join(cells))
    for s in d.sections:                                       # 页眉页脚
        for part in (s.header, s.footer):
            for para in part.paragraphs:
                if para.text.strip():
                    out.append('[hf] ' + para.text.strip())
    return '\n'.join(out), 'python-docx'


def extract_xlsx(p):
    import openpyxl
    wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f'## sheet: {ws.title}' + (' (hidden)' if ws.sheet_state != 'visible' else ''))
        for row in ws.iter_rows(values_only=True):
            vals = ['' if v is None else str(v).strip() for v in row]
            if any(vals):
                out.append('\t'.join(vals).rstrip())
            if sum(len(x) for x in out) > MAX_CHARS:
                break
    return '\n'.join(out), 'openpyxl'


def extract_xls(p):
    import xlrd
    wb = xlrd.open_workbook(p, formatting_info=False)
    out = []
    for sh in wb.sheets():
        out.append(f'## sheet: {sh.name}')
        for r in range(sh.nrows):
            vals = [str(v).strip() for v in sh.row_values(r)]
            if any(vals):
                out.append('\t'.join(vals).rstrip())
    return '\n'.join(out), 'xlrd'


def ocr_image(p):
    if not have('tesseract'):
        return ''
    r = run(['tesseract', p, 'stdout', '-l', 'chi_sim+eng', '--psm', '6'], timeout=300)
    return r.stdout.strip() if r.returncode == 0 else ''


def extract_pdf(p, tmp):
    import pdfplumber
    pages, n = [], 0
    with pdfplumber.open(p) as pdf:
        n = len(pdf.pages)
        for i, pg in enumerate(pdf.pages, 1):
            t = pg.extract_text() or ''
            for tb in pg.extract_tables() or []:
                t += '\n' + '\n'.join(' | '.join('' if c is None else str(c).strip() for c in row) for row in tb)
            pages.append(f'--- page {i} ---\n{t.strip()}')
    txt = '\n'.join(pages)
    if OCR and have('pdftoppm') and n and len(re.sub(r'\W', '', txt)) < 30 * n:   # 没文字层 → 渲染 + OCR
        os.makedirs(tmp, exist_ok=True)
        run(['pdftoppm', '-r', '200', '-png', '-l', '60', p, os.path.join(tmp, 'pg')], timeout=1200)
        ocr = []
        for fn in sorted(os.listdir(tmp)):
            if fn.endswith('.png'):
                ocr.append(f'--- page {fn} (ocr) ---\n' + ocr_image(os.path.join(tmp, fn)))
        if ocr:
            return '\n'.join(ocr), 'pdfplumber+ocr'
    return txt, 'pdfplumber'


def extract_pptx(p):
    from pptx import Presentation
    prs = Presentation(p)
    out = []
    for i, slide in enumerate(prs.slides, 1):
        out.append(f'--- slide {i} ---')
        for sh in slide.shapes:
            if sh.has_text_frame and sh.text_frame.text.strip():
                out.append(sh.text_frame.text.strip())
            if getattr(sh, 'has_table', False) and sh.has_table:
                for row in sh.table.rows:
                    out.append(' | '.join(c.text.strip() for c in row.cells))
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip():
            out.append('[notes] ' + slide.notes_slide.notes_text_frame.text.strip())
    return '\n'.join(out), 'python-pptx'


def soffice_convert(p, fmt, tmp):
    os.makedirs(tmp, exist_ok=True)
    r = run(['soffice', '--headless', '--convert-to', fmt, '--outdir', tmp, p], timeout=600)
    outs = [os.path.join(tmp, x) for x in os.listdir(tmp) if x.endswith('.' + fmt)]
    if r.returncode != 0 or not outs:
        raise RuntimeError('soffice convert failed')
    return outs[0]


def extract_any(p, ext, tmp):
    """返回 (text, method)。抛异常 = fail；返回 ('', 'meta') = 只记元数据。"""
    if ext in TEXT_EXT:
        return read_text(p), 'text'
    if ext == '.docx':
        return extract_docx(p)
    if ext in ('.xlsx', '.xlsm'):
        return extract_xlsx(p)
    if ext == '.xls':
        try:
            return extract_xls(p)
        except Exception:  # noqa
            return extract_xlsx(soffice_convert(p, 'xlsx', tmp))
    if ext == '.pdf':
        return extract_pdf(p, tmp)
    if ext == '.pptx':
        return extract_pptx(p)
    if ext in ('.doc', '.rtf', '.odt', '.wps'):
        return extract_docx(soffice_convert(p, 'docx', tmp))
    if ext in ('.ppt', '.odp'):
        return extract_pptx(soffice_convert(p, 'pptx', tmp))
    if ext == '.ods':
        return extract_xlsx(soffice_convert(p, 'xlsx', tmp))
    if ext in IMG_EXT:
        if OCR and os.path.getsize(p) >= OCR_MIN_KB * 1024:
            return ocr_image(p), 'ocr'
        return '', 'meta'
    return '', 'meta'


# ---------------------------------------------------------------- 6. 主流程：清点 → 去重 → 抽取（并发）→ 定时提交 → 覆盖率报告
def slug(rel, sha):
    base = re.sub(r'[^\w.\-]+', '_', rel.replace('/', '__'))[-120:]
    return f'{base}__{sha[:8]}'


def coverage(manifest):
    by_ext = defaultdict(Counter)
    for m in manifest:
        by_ext[m['ext'] or '(none)'][m['status']] += 1
    tot = Counter(m['status'] for m in manifest)
    lines = [f'# {TITLE} · 覆盖率', '',
             f"- 生成时间：{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}；成员 {len(manifest)}："
             f"正文 ok {tot['ok']} / 仅元数据 meta {tot['meta']} / 重复 dup {tot['dup']} / 失败 fail {tot['fail']}",
             f"- 原件：{'Release ' + RELEASE_TAG if BACKUP else '未备份'}；来源：{SOURCE_IDS or SOURCE_RELEASE or LOCAL_FILES}", '',
             '| 类型 | ok | meta | dup | fail |', '|---|---|---|---|---|']
    for ext, c in sorted(by_ext.items(), key=lambda kv: -sum(kv[1].values())):
        lines.append(f"| {ext} | {c['ok']} | {c['meta']} | {c['dup']} | {c['fail']} |")
    fails = [m for m in manifest if m['status'] == 'fail']
    if fails:
        lines += ['', '## 失败清单', ''] + [f"- `{m['rel']}` — {m.get('error', '')[:160]}" for m in fails]
    metas = [m for m in manifest if m['status'] == 'meta']
    if metas:
        lines += ['', f'## 仅元数据（{len(metas)}，无文字层或无抽取器）', ''] + [f"- `{m['rel']}` ({m['bytes']} B)" for m in metas[:300]]
    with open(os.path.join(OUT, '_coverage.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def main():
    if not OUT_NAME:
        abort(1, 'OUT_NAME is required')
    os.makedirs(os.path.join(OUT, 'text'), exist_ok=True)
    status_note(f'START {TITLE}；work={WORK}；tools: tesseract={have("tesseract")} soffice={have("soffice")} 7z={have("7z")}')
    sources = resolve_sources()
    backup(sources)
    # 解包 / 单文件直接纳入
    shutil.rmtree(UNPACK, ignore_errors=True)
    os.makedirs(UNPACK)
    for name, p in sources:
        ext = os.path.splitext(name)[1].lower()
        if ext in ARCHIVE_EXT and (zipfile.is_zipfile(p) or tarfile.is_tarfile(p) or ext in ('.rar', '.7z')):
            log('unpack', name)
            unpack(p, os.path.join(UNPACK, os.path.splitext(name)[0]))
            if not LOCAL_FILES:
                os.remove(p)                                   # 原件已在 Release，删掉省盘
        else:
            shutil.copy2(p, os.path.join(UNPACK, name))
    # 清点
    items = []
    for dp, _, fns in os.walk(UNPACK):
        for fn in fns:
            if fn.lower() in SKIP_NAMES or fn.startswith('._'):
                continue
            p = os.path.join(dp, fn)
            items.append({'rel': os.path.relpath(p, UNPACK), 'ext': os.path.splitext(fn)[1].lower(), 'bytes': os.path.getsize(p), 'path': p})
    items.sort(key=lambda x: x['rel'])
    log('members', len(items), 'total bytes', sum(x['bytes'] for x in items))
    # 续跑：上次 manifest 里 ok/meta/dup 的成员直接复用
    prev = {}
    mp = os.path.join(OUT, 'manifest.json')
    if os.path.exists(mp):
        try:
            prev = {m['rel']: m for m in json.load(open(mp, encoding='utf-8'))['members'] if m['status'] != 'fail'}
        except Exception:  # noqa
            prev = {}
    seen = {}
    manifest, lock, last_commit = [], __import__('threading').Lock(), time.time()

    def work(it):
        sha = sha256_file(it['path'])
        rec = {'rel': it['rel'], 'ext': it['ext'], 'bytes': it['bytes'], 'sha256': sha}
        with lock:
            if sha in seen:
                rec.update(status='dup', same_as=seen[sha])
                return rec
            seen[sha] = it['rel']
        old = prev.get(it['rel'])
        if old and old.get('sha256') == sha:
            return old
        tmp = os.path.join(os.environ['TMPDIR'], 'x_' + sha[:12])
        try:
            text, method = extract_any(it['path'], it['ext'], tmp)
            text = (text or '').strip()
            if len(text) > MAX_CHARS:
                text = text[:MAX_CHARS] + f'\n…[truncated at {MAX_CHARS} chars]'
            rec.update(method=method, chars=len(text))
            if text:
                sl = slug(it['rel'], sha)
                write_json(os.path.join(OUT, 'text', sl + '.json'), {'rel': it['rel'], 'text': text})
                rec.update(status='ok', text_file=f'text/{sl}.json')
            else:
                rec['status'] = 'meta'
        except Exception as e:  # noqa
            rec.update(status='fail', error=f'{type(e).__name__}: {str(e)[:200]}')
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        return rec

    def flush(msg):
        write_json(mp, {'title': TITLE, 'generated': datetime.now(timezone.utc).isoformat(), 'members': manifest})
        coverage(manifest)
        git_commit_push(msg)

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for i, rec in enumerate(ex.map(work, items), 1):
            rec.pop('path', None)
            manifest.append(rec)
            if i % 50 == 0:
                log(f'{i}/{len(items)}', Counter(m['status'] for m in manifest))
            if time.time() - last_commit > CHECKPOINT_MIN * 60:
                flush(f'ingest {OUT_NAME}: 进度 {i}/{len(items)}')
                last_commit = time.time()
    tot = Counter(m['status'] for m in manifest)
    status_note(f"DONE 成员 {len(items)}：ok {tot['ok']} / meta {tot['meta']} / dup {tot['dup']} / fail {tot['fail']}；用时 {int(time.time() - T0)} s")
    flush(f"ingest {OUT_NAME}: 完成 {len(items)} 成员（ok {tot['ok']} / meta {tot['meta']} / dup {tot['dup']} / fail {tot['fail']}）")
    log('done', dict(tot))


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        raise
    except Exception:  # noqa
        tb = traceback.format_exc()
        log(tb)
        status_note('**CRASH**\n```\n' + tb[-3000:] + '\n```')
        git_commit_push(f'ingest {OUT_NAME}: CRASH')
        sys.exit(4)
