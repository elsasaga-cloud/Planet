#!/usr/bin/env python3
"""T28 · Google Drive《SmartByte》文件夹全量入库（由 GitHub Actions 运行器执行）。

背景：Simon 要删除 Drive 里 5.7 GB 的《SmartByte》文件夹腾空间；删除前必须把里面的信息全部
留在仓库里。Arena 沙箱只能访问 github/pypi，拿不到 Drive 文件字节；Drive 连接器的文本抽取又会
丢掉 Word 表格（规格书的核心）。所以由运行器按 data/smartbyte_drive_index.json 里的 2,385 个
文件 ID 逐个下载（文件夹临时设为「知道链接者可查看」），本地全保真抽取后写回分支：

    data/smartbyte_drive/manifest.json   每个文件一条：路径/类型/字节/sha256/状态/抽取方式/字数/去重指向
    data/smartbyte_drive/manifest.csv    同上（人读）
    data/smartbyte_drive/text/<id>.json  每个文档一份全文：Word 段落+表格（按原顺序）、Excel 逐表逐行、
                                         PDF 逐页（无文字层则 OCR）、PPT 逐页、XMind 大纲、RAR 内文本、DXF 文字…
    data/smartbyte_drive/thumbs/<id>.jpg 图片/视频/PSD 的缩略图（≤360px），图片另做 OCR（有字才存）
    data/smartbyte_drive/_coverage.md    覆盖率报告：按类型/文件夹的成功、仅元数据、重复、失败清单
    GitHub Release <RELEASE_TAG>         原始文件按顶层文件夹打包（≤1.8 GB/包）作为完整备份（不进 Git 历史）

内容去重：同 sha256 只抽取一次，其余文件写 same_as 指向。
断点续跑：已在 manifest 里且所属文件夹备份完成的文件默认跳过（FORCE=1 全部重做）。

用法：python scripts/drive_ingest/ingest.py
环境变量：
  INDEX=data/smartbyte_drive_index.json  OUT_DIR=data/smartbyte_drive  RAW_DIR=/tmp/drive_raw  ZIP_DIR=/tmp/drive_zip
  WORKERS=6  LIMIT=0  ONLY_FOLDERS=工业管理,MC  ONLY_TYPES=Word,Excel  FORCE=0
  COMMIT_EVERY=200  GIT_COMMIT=0  GIT_REF=分支名
  BACKUP=1  RELEASE_TAG=drive-smartbyte-YYYYMMDD  PART_MAX_GB=1.8  RELEASE_TARGET=<sha>
  OCR=1  THUMB_PX=360  OCR_MAX_PAGES=150
  LOCAL_DIR=<目录>  → 测试模式：不下载，直接读 LOCAL_DIR/<Drive 路径>
  SOURCE_RELEASE=<tag> → 备选来源：从本仓库 Release 下载 Simon 手工上传的 Drive 打包 zip，解压后当 LOCAL_DIR 用（不需共享 Drive）
"""
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import traceback
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INDEX = os.environ.get('INDEX') or os.path.join(ROOT, 'data', 'smartbyte_drive_index.json')
OUT = os.environ.get('OUT_DIR') or os.path.join(ROOT, 'data', 'smartbyte_drive')
TEXT_DIR = os.path.join(OUT, 'text')
THUMB_DIR = os.path.join(OUT, 'thumbs')
RAW_DIR = os.environ.get('RAW_DIR') or '/tmp/drive_raw'
ZIP_DIR = os.environ.get('ZIP_DIR') or '/tmp/drive_zip'
LOCAL_DIR = os.environ.get('LOCAL_DIR', '')
SOURCE_RELEASE = os.environ.get('SOURCE_RELEASE', '')  # 备选来源：Simon 手工上传到 Release 的 Drive 下载 zip

WORKERS = int(os.environ.get('WORKERS', '6'))
LIMIT = int(os.environ.get('LIMIT', '0'))
ONLY_FOLDERS = [x.strip() for x in os.environ.get('ONLY_FOLDERS', '').split(',') if x.strip()]
ONLY_TYPES = [x.strip() for x in os.environ.get('ONLY_TYPES', '').split(',') if x.strip()]
FORCE = os.environ.get('FORCE', '0') == '1'
COMMIT_EVERY = int(os.environ.get('COMMIT_EVERY', '200'))
GIT_COMMIT = os.environ.get('GIT_COMMIT', '0') == '1'
GIT_REF = os.environ.get('GIT_REF', '')
BACKUP = os.environ.get('BACKUP', '1') == '1'
RELEASE_TAG = os.environ.get('RELEASE_TAG') or ('drive-smartbyte-' + datetime.now(timezone.utc).strftime('%Y%m%d'))
RELEASE_TARGET = os.environ.get('RELEASE_TARGET', '')
PART_MAX = int(float(os.environ.get('PART_MAX_GB', '1.8')) * 1024 ** 3)
OCR = os.environ.get('OCR', '1') == '1'
THUMB_PX = int(os.environ.get('THUMB_PX', '360'))
OCR_MAX_PAGES = int(os.environ.get('OCR_MAX_PAGES', '150'))
MAX_ROWS = int(os.environ.get('MAX_ROWS', '30000'))
MAX_JSON = 12 * 1024 * 1024

DL_URL = 'https://drive.usercontent.google.com/download?id={id}&export=download&confirm=t'
DL_URL2 = 'https://drive.google.com/uc?export=download&id={id}&confirm=t'

# 顶层文件夹处理顺序（价值高的在前；「暂时不用的」最后）+ Release 包名用的 ASCII 别名
FOLDER_ORDER = ['(root)', '工业管理', '工业非管理', '商业管理', 'MC', 'Managed Industrial Ethernet Switch_最新资料',
                'Bypass', 'User Manual', 'Certification', 'PCB Information', 'Case', '管理界面图', '组合图', '素材',
                'Factory Information', '暂时不用的']
FOLDER_SLUG = {'(root)': 'root', '工业管理': 'industrial_managed', '工业非管理': 'industrial_unmanaged',
               '商业管理': 'commercial_managed', 'MC': 'media_converter',
               'Managed Industrial Ethernet Switch_最新资料': 'managed_industrial_latest', 'Bypass': 'bypass',
               'User Manual': 'user_manual', 'Certification': 'certification', 'PCB Information': 'pcb_information',
               'Case': 'case', '管理界面图': 'ui_screenshots', '组合图': 'combo_images', '素材': 'assets',
               'Factory Information': 'factory_information', '暂时不用的': 'unused_for_now'}

IMG_EXT = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tif', '.tiff', '.heic', '.heif'}
try:  # HEIC（iPhone 照片）：有 pillow-heif 就按普通图片处理
    import pillow_heif  # noqa
    pillow_heif.register_heif_opener()
except Exception:  # noqa
    pass
VID_EXT = {'.mp4', '.mov', '.avi', '.mkv', '.wmv'}

LOCK = threading.Lock()
SOFFICE_LOCK = threading.Lock()
T0 = time.time()


def log(*a):
    print(f'[{time.time() - T0:7.1f}s]', *a, flush=True)


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def have(cmd):
    return shutil.which(cmd) is not None


def run(cmd, timeout=600, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, **kw)


# ---------------------------------------------------------------- 下载
def download(rec, dest):
    """下载到 dest；返回 None 或错误字符串。"""
    if LOCAL_DIR:
        src = os.path.join(LOCAL_DIR, rec['path'])
        if not os.path.exists(src):
            # Drive 打包下载时同名文件会被加 " (1)" 后缀；按「文件夹 + 主名前缀 + 扩展名」兜底匹配
            d = os.path.join(LOCAL_DIR, rec['folder'])
            stem, ext = os.path.splitext(rec['name'])
            cands = []
            if os.path.isdir(d):
                for fn in os.listdir(d):
                    st2, ex2 = os.path.splitext(fn)
                    if ex2.lower() == ext and re.fullmatch(re.escape(stem) + r'( \(\d+\))?', st2):
                        fp = os.path.join(d, fn)
                        if rec.get('bytes') and os.path.getsize(fp) == rec['bytes']:
                            cands.insert(0, fp)
                        else:
                            cands.append(fp)
            if not cands:
                return 'local file not found'
            src = cands[0]
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if os.path.lexists(dest):
            os.remove(dest)
        os.symlink(os.path.abspath(src), dest)
        return None
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    import requests
    last = ''
    for attempt in range(6):
        for url in (DL_URL, DL_URL2):
            try:
                with requests.get(url.format(id=rec['id']), stream=True, timeout=(15, 120),
                                  headers={'User-Agent': 'Mozilla/5.0'}) as r:
                    ctype = r.headers.get('Content-Type', '')
                    if r.status_code != 200:
                        last = f'HTTP {r.status_code}'
                        if r.status_code in (403, 429):
                            time.sleep(8 + attempt * 10)
                        continue
                    if 'text/html' in ctype and rec['ext'] not in ('.html', '.htm'):
                        body = r.content[:6000].decode('utf-8', 'ignore')
                        if ('ServiceLogin' in body or 'accounts.google.com' in body or 'Request access' in body
                                or 'You need access' in body or '需要访问权限' in body):
                            return 'NOT_SHARED: Drive returned a sign-in / request-access page（文件夹未设为「知道链接者可查看」）'
                        if 'confirm' in body or 'virus' in body.lower():
                            m = re.search(r'confirm=([0-9A-Za-z_-]+)', body)
                            if m:
                                url2 = DL_URL.format(id=rec['id']).replace('confirm=t', 'confirm=' + m.group(1))
                                with requests.get(url2, stream=True, timeout=(15, 120)) as r2:
                                    if r2.status_code == 200 and 'text/html' not in r2.headers.get('Content-Type', ''):
                                        with open(dest, 'wb') as f:
                                            for chunk in r2.iter_content(1 << 20):
                                                f.write(chunk)
                                        return None
                        last = 'HTML instead of file (not shared / quota / sign-in page)'
                        continue
                    with open(dest, 'wb') as f:
                        for chunk in r.iter_content(1 << 20):
                            f.write(chunk)
                size = os.path.getsize(dest)
                if rec.get('bytes') and abs(size - rec['bytes']) > max(64, rec['bytes'] * 0.02) and size < rec['bytes']:
                    last = f'size mismatch {size} vs {rec["bytes"]}'
                    continue
                return None
            except Exception as e:  # noqa
                last = f'{type(e).__name__}: {e}'[:200]
        time.sleep(3 + attempt * 5)
    # 最后再试 gdown
    try:
        import gdown
        out = gdown.download(id=rec['id'], output=dest, quiet=True, fuzzy=False)
        if out and os.path.exists(dest) and os.path.getsize(dest) > 0:
            return None
    except Exception as e:  # noqa
        last = f'gdown: {e}'[:200]
    return last or 'download failed'


# ---------------------------------------------------------------- 抽取：Word
W_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def _cell_text(cell):
    parts = [p.text.strip() for p in cell.paragraphs if p.text.strip()]
    for t in getattr(cell, 'tables', []):
        for r in t.rows:
            seen = None
            row = []
            for c in r.cells:
                if c._tc is seen:
                    continue
                seen = c._tc
                row.append(_cell_text(c))
            parts.append(' | '.join(row))
    return ' / '.join(parts)


def extract_docx(path):
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    d = docx.Document(path)
    blocks, texts, warnings = [], [], []
    body = d.element.body
    for child in body.iterchildren():
        tag = child.tag.split('}')[-1]
        if tag == 'p':
            p = Paragraph(child, d)
            t = p.text.strip()
            if not t:
                continue
            try:
                style = p.style.name if p.style is not None else ''
            except Exception:  # noqa
                style = ''
            kind = 'h' if (style or '').lower().startswith(('heading', 'title')) else 'p'
            blocks.append({'t': kind, 's': style, 'text': t})
            texts.append(t)
        elif tag == 'tbl':
            tb = Table(child, d)
            rows = []
            try:
                for r in tb.rows:
                    seen = None
                    row = []
                    for c in r.cells:
                        if c._tc is seen:
                            continue
                        seen = c._tc
                        row.append(_cell_text(c))
                    if any(x.strip() for x in row):
                        rows.append(row)
            except Exception as e:  # noqa
                warnings.append(f'table: {e}')
            if rows:
                blocks.append({'t': 'table', 'rows': rows})
                texts.append('\n'.join('\t'.join(r) for r in rows))
        elif tag == 'sdt':
            t = ''.join(x.text or '' for x in child.iter(W_NS + 't')).strip()
            if t:
                blocks.append({'t': 'p', 's': 'sdt', 'text': t})
                texts.append(t)
    # 文本框 / 形状里的文字（python-docx 段落 API 读不到）
    tb_texts = []
    for txbx in body.iter(W_NS + 'txbxContent'):
        for p in txbx.iter(W_NS + 'p'):
            t = ''.join(x.text or '' for x in p.iter(W_NS + 't')).strip()
            if t:
                tb_texts.append(t)
    tb_texts = list(dict.fromkeys(tb_texts))
    hf = []
    try:
        for s in d.sections:
            for part in (s.header, s.footer):
                for p in part.paragraphs:
                    if p.text.strip():
                        hf.append(p.text.strip())
    except Exception as e:  # noqa
        warnings.append(f'header/footer: {e}')
    hf = list(dict.fromkeys(hf))
    cp = d.core_properties
    meta = {'title': cp.title or '', 'author': cp.author or '', 'last_modified_by': cp.last_modified_by or '',
            'created': cp.created.isoformat() if cp.created else '', 'modified': cp.modified.isoformat() if cp.modified else '',
            'paragraphs': sum(1 for b in blocks if b['t'] != 'table'), 'tables': sum(1 for b in blocks if b['t'] == 'table')}
    media = []
    try:
        with zipfile.ZipFile(path) as z:
            for n in z.namelist():
                if n.startswith('word/media/'):
                    media.append({'name': n.split('/')[-1], 'bytes': z.getinfo(n).file_size})
    except Exception:  # noqa
        pass
    meta['embedded_images'] = len(media)
    text = '\n'.join(texts)
    if tb_texts:
        text += '\n[文本框]\n' + '\n'.join(tb_texts)
    if hf:
        text += '\n[页眉页脚]\n' + '\n'.join(hf)
    return {'method': 'python-docx(段落+表格+文本框+页眉页脚)', 'status': 'ok' if text.strip() else 'meta',
            'meta': meta, 'text': text, 'blocks': blocks, 'textboxes': tb_texts, 'header_footer': hf,
            'embedded_media': media[:400], 'warnings': warnings}


def soffice_convert(path, fmt, outdir):
    if not have('soffice'):
        return None, 'soffice not installed'
    os.makedirs(outdir, exist_ok=True)
    with SOFFICE_LOCK:
        try:
            r = run(['soffice', '--headless', '--norestore', '--convert-to', fmt, '--outdir', outdir, path], timeout=420)
        except subprocess.TimeoutExpired:
            return None, 'soffice timeout'
    base = os.path.splitext(os.path.basename(path))[0] + '.' + fmt.split(':')[0]
    out = os.path.join(outdir, base)
    if os.path.exists(out):
        return out, None
    return None, 'soffice produced nothing: ' + (r.stderr or r.stdout)[-300:]


def extract_doc(path, tmp):
    out, err = soffice_convert(path, 'docx', tmp)
    if not out:
        return {'method': 'soffice→docx', 'status': 'meta', 'meta': {}, 'text': '', 'warnings': [err]}
    ex = extract_docx(out)
    ex['method'] = 'soffice→docx→' + ex['method']
    return ex


# ---------------------------------------------------------------- 抽取：Excel
def _html_table_text(data):
    """把伪装成 xls/xlsx 的 HTML 表格（常见于中文系统导出）转成按行 tab 分隔文本。"""
    from html.parser import HTMLParser

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.rows, self.row, self.cell, self.in_cell = [], [], [], False

        def handle_starttag(self, tag, attrs):
            if tag == 'tr':
                self.row = []
            elif tag in ('td', 'th'):
                self.in_cell, self.cell = True, []
            elif tag == 'br' and self.in_cell:
                self.cell.append(' ')

        def handle_endtag(self, tag):
            if tag in ('td', 'th') and self.in_cell:
                self.row.append(''.join(self.cell).strip())
                self.in_cell = False
            elif tag == 'tr':
                if any(self.row):
                    self.rows.append(self.row)
                self.row = []

        def handle_data(self, d):
            if self.in_cell:
                self.cell.append(d)

    for enc in ('utf-8', 'gb18030', 'latin-1'):
        try:
            html = data.decode(enc)
            break
        except Exception:  # noqa
            continue
    else:
        html = data.decode('utf-8', 'ignore')
    m = re.search(r'charset=["\']?([\w-]+)', html[:4000], re.I)
    if m and m.group(1).lower() not in ('utf-8', 'utf8'):
        try:
            html = data.decode(m.group(1))
        except Exception:  # noqa
            pass
    p = P()
    try:
        p.feed(html)
        p.close()
    except Exception:  # noqa
        pass
    return p.rows


def extract_excel_any(path, tmp):
    """按文件头识别真实格式：zip(xlsx) / OLE2(xls) / HTML 表格 / 其他 → soffice 转换；扩展名不可信。"""
    with open(path, 'rb') as f:
        head = f.read(8)
    errs = []
    if head[:4] == b'PK\x03\x04':
        try:
            return extract_xlsx(path)
        except Exception as e:  # noqa
            errs.append(f'openpyxl: {e}'[:160])
        try:  # 样式表损坏等 openpyxl/soffice 都打不开的 xlsx：直接读 zip 里的 sheet XML + sharedStrings
            r = extract_xlsx_raw(path)
            r.setdefault('warnings', []).extend(errs)
            return r
        except Exception as e:  # noqa
            errs.append(f'raw-xml: {e}'[:160])
    if head[:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1':
        try:
            r = extract_xls(path)
            if not path.lower().endswith('.xls'):
                r.setdefault('warnings', []).append('扩展名为 xlsx 但实际是 OLE2 .xls（按内容识别）')
            return r
        except Exception as e:  # noqa
            errs.append(f'xlrd: {e}'[:160])
    with open(path, 'rb') as f:
        sample = f.read(4_000_000)
    low = sample[:20000].lower()
    if b'<table' in low or b'<html' in low or b'<?xml' in low and b'urn:schemas-microsoft-com:office:spreadsheet' in sample[:200000]:
        if have('soffice'):
            out, err = soffice_convert(path, 'xlsx', tmp)
            if out:
                try:
                    r = extract_xlsx(out)
                    r['method'] = 'soffice→xlsx→' + r['method']
                    r.setdefault('warnings', []).append('扩展名为 Excel 但实际是 HTML/XML 表格（已经 soffice 转换）')
                    return r
                except Exception as e:  # noqa
                    errs.append(f'soffice-xlsx: {e}'[:160])
            else:
                errs.append(err or 'soffice failed')
        rows = _html_table_text(sample)
        if rows:
            text = '\n'.join('\t'.join(r) for r in rows)
            return {'method': 'html-table', 'status': 'ok', 'meta': {'rows_total': len(rows), 'note': 'Excel 扩展名但内容为 HTML 表格'},
                    'text': text, 'sheets': {'html': {'state': 'visible', 'rows': rows}}, 'warnings': errs}
    if have('soffice'):
        out, err = soffice_convert(path, 'xlsx', tmp)
        if out:
            try:
                r = extract_xlsx(out)
                r['method'] = 'soffice→xlsx→' + r['method']
                r.setdefault('warnings', []).append('原文件无法直接解析，已经 soffice 转换（头部 %s）' % head.hex())
                return r
            except Exception as e:  # noqa
                errs.append(f'soffice-xlsx: {e}'[:160])
        else:
            errs.append(err or 'soffice failed')
    raise RuntimeError('; '.join(errs) or f'unknown excel format (head {head.hex()})')


def extract_xlsx_raw(path):
    """不依赖 openpyxl：解析 xl/sharedStrings.xml + xl/worksheets/sheetN.xml（含内联字符串与公式缓存值）。"""
    import xml.etree.ElementTree as ET
    ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
          'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
    zf = zipfile.ZipFile(path)
    names = set(zf.namelist())
    shared = []
    if 'xl/sharedStrings.xml' in names:
        root = ET.fromstring(zf.read('xl/sharedStrings.xml'))
        for si in root.findall('m:si', ns):
            shared.append(''.join(t.text or '' for t in si.iter('{%s}t' % ns['m'])))
    # 表名 ↔ 文件
    sheet_files = {}
    try:
        wb = ET.fromstring(zf.read('xl/workbook.xml'))
        rels = ET.fromstring(zf.read('xl/_rels/workbook.xml.rels'))
        rid2t = {r.get('Id'): r.get('Target') for r in rels}
        for sh in wb.find('m:sheets', ns):
            t = rid2t.get(sh.get('{%s}id' % ns['r']), '').lstrip('/')
            t = t if t.startswith('xl/') else 'xl/' + t
            sheet_files[sh.get('name')] = t
    except Exception:  # noqa
        pass
    if not sheet_files or not any(fn in names for fn in sheet_files.values()):
        sheet_files = {n.rsplit('/', 1)[-1][:-4]: n for n in sorted(names) if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')}

    def col_idx(ref):
        c = 0
        for ch in ref:
            if ch.isalpha():
                c = c * 26 + (ord(ch.upper()) - 64)
            else:
                break
        return c

    sheets, lines, total = {}, [], 0
    for title, fn in sheet_files.items():
        if fn not in names:
            continue
        rows = []
        for row in ET.fromstring(zf.read(fn)).iter('{%s}row' % ns['m']):
            cells = {}
            for c in row.findall('m:c', ns):
                t = c.get('t')
                v = c.find('m:v', ns)
                if t == 's' and v is not None and v.text is not None:
                    val = shared[int(v.text)] if int(v.text) < len(shared) else ''
                elif t == 'inlineStr':
                    val = ''.join(x.text or '' for x in c.iter('{%s}t' % ns['m']))
                else:
                    val = (v.text or '') if v is not None else ''
                if val != '':
                    cells[col_idx(c.get('r', ''))] = val
            if cells:
                w = max(cells)
                rows.append([cells.get(i, '') for i in range(1, w + 1)])
        rows = [r for r in rows if any(x.strip() for x in r)]
        sheets[title] = {'state': 'visible', 'rows': rows}
        total += len(rows)
        lines.append(f'=== 表：{title}（{len(rows)} 行）===')
        lines += ['\t'.join(r) for r in rows]
    text = '\n'.join(lines)
    return {'method': 'xlsx-raw-xml', 'status': 'ok' if total else 'meta', 'meta': {'sheets': list(sheets), 'rows_total': total},
            'text': text, 'sheets': sheets, 'warnings': ['openpyxl 无法打开（样式表损坏等），按 zip 内 XML 直接读取：无格式/合并单元格信息']}


def _fmt(v):
    if v is None:
        return ''
    if isinstance(v, float):
        if v.is_integer():
            return str(int(v))
        return repr(round(v, 6))
    if isinstance(v, datetime):
        return v.isoformat(sep=' ')
    s = str(v)
    return s.strip()


def extract_xlsx(path):
    import openpyxl
    sheets, texts, warnings = {}, [], []
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        for ws in wb.worksheets:
            rows = []
            n = 0
            for row in ws.iter_rows(values_only=True):
                vals = [_fmt(v) for v in row]
                while vals and vals[-1] == '':
                    vals.pop()
                if any(vals):
                    rows.append(vals)
                n += 1
                if len(rows) >= MAX_ROWS:
                    warnings.append(f'{ws.title}: truncated at {MAX_ROWS} rows')
                    break
            sheets[ws.title] = {'state': ws.sheet_state, 'rows': rows}
            texts.append(f'--- Sheet: {ws.title} ---')
            texts.extend('\t'.join(r) for r in rows)
    finally:
        wb.close()
    media = 0
    try:
        with zipfile.ZipFile(path) as z:
            media = sum(1 for n in z.namelist() if n.startswith('xl/media/'))
    except Exception:  # noqa
        pass
    meta = {'sheets': list(sheets.keys()), 'embedded_images': media,
            'rows_total': sum(len(s['rows']) for s in sheets.values())}
    text = '\n'.join(texts)
    return {'method': 'openpyxl(values)', 'status': 'ok' if meta['rows_total'] else 'meta', 'meta': meta,
            'text': text, 'sheets': sheets, 'warnings': warnings}


def extract_xls(path):
    import xlrd
    wb = xlrd.open_workbook(path)
    sheets, texts = {}, []
    for ws in wb.sheets():
        rows = []
        for i in range(ws.nrows):
            vals = []
            for j in range(ws.ncols):
                c = ws.cell(i, j)
                v = c.value
                if c.ctype == xlrd.XL_CELL_DATE:
                    try:
                        v = datetime(*xlrd.xldate_as_tuple(v, wb.datemode)).isoformat(sep=' ')
                    except Exception:  # noqa
                        pass
                vals.append(_fmt(v))
            while vals and vals[-1] == '':
                vals.pop()
            if any(vals):
                rows.append(vals)
        sheets[ws.name] = {'rows': rows}
        texts.append(f'--- Sheet: {ws.name} ---')
        texts.extend('\t'.join(r) for r in rows)
    meta = {'sheets': list(sheets.keys()), 'rows_total': sum(len(s['rows']) for s in sheets.values())}
    return {'method': 'xlrd', 'status': 'ok' if meta['rows_total'] else 'meta', 'meta': meta,
            'text': '\n'.join(texts), 'sheets': sheets, 'warnings': []}


# ---------------------------------------------------------------- 抽取：PDF
_OCR_LANG = None


def ocr_lang():
    global _OCR_LANG
    if _OCR_LANG is None:
        langs = ''
        try:
            langs = run(['tesseract', '--list-langs'], timeout=60).stdout
        except Exception:  # noqa
            pass
        parts = [l for l in ('chi_sim', 'chi_tra', 'eng') if l in langs]
        _OCR_LANG = '+'.join(parts) or 'eng'
        log('tesseract langs:', _OCR_LANG)
    return _OCR_LANG


def ocr_image_file(img_path, lang=None):
    if not have('tesseract'):
        return '', 0.0
    lang = lang or ocr_lang()
    try:
        r = run(['tesseract', img_path, 'stdout', '-l', lang, '--psm', '3', 'tsv'], timeout=180)
    except subprocess.TimeoutExpired:
        return '', 0.0
    words, confs = [], []
    lines = {}
    for ln in r.stdout.splitlines()[1:]:
        parts = ln.split('\t')
        if len(parts) < 12:
            continue
        try:
            conf = float(parts[10])
        except ValueError:
            continue
        txt = parts[11].strip()
        if conf < 0 or not txt:
            continue
        key = (parts[1], parts[2], parts[3], parts[4])  # page, block, par, line
        lines.setdefault(key, []).append(txt)
        confs.append(conf)
        words.append(txt)
    text = '\n'.join(' '.join(v) for v in lines.values())
    conf = sum(confs) / len(confs) if confs else 0.0
    return text.strip(), round(conf, 1)


def extract_pdf(path, tmp, allow_ocr=True):
    pages, warnings, meta = [], [], {}
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            meta = {'pages': len(pdf.pages)}
            md = pdf.metadata or {}
            for k in ('Title', 'Author', 'Creator', 'Producer', 'CreationDate', 'ModDate'):
                if md.get(k):
                    meta[k.lower()] = str(md[k])[:200]
            for i, page in enumerate(pdf.pages):
                try:
                    pages.append((page.extract_text() or '').strip())
                except Exception as e:  # noqa
                    pages.append('')
                    warnings.append(f'p{i + 1}: {e}'[:120])
    except Exception as e:  # noqa
        warnings.append(f'pdfplumber: {e}'[:160])
        try:
            from pypdf import PdfReader
            rd = PdfReader(path)
            meta = {'pages': len(rd.pages)}
            pages = [(p.extract_text() or '').strip() for p in rd.pages]
        except Exception as e2:  # noqa
            warnings.append(f'pypdf: {e2}'[:160])
    method = 'pdfplumber'
    chars = sum(len(p) for p in pages)
    ocr_pages = 0
    if allow_ocr and OCR and pages and chars < 60 * len(pages) and have('pdftoppm') and have('tesseract'):
        # 基本没有文字层 → 逐页 OCR
        n = min(len(pages), OCR_MAX_PAGES)
        od = os.path.join(tmp, 'ocr')
        os.makedirs(od, exist_ok=True)
        try:
            run(['pdftoppm', '-r', '160', '-png', '-l', str(n), path, os.path.join(od, 'p')], timeout=900)
            imgs = sorted(f for f in os.listdir(od) if f.endswith('.png'))
            for i, f in enumerate(imgs):
                if i >= len(pages):
                    break
                t, conf = ocr_image_file(os.path.join(od, f))
                if t and len(t) > len(pages[i]):
                    pages[i] = t
                    ocr_pages += 1
            method = f'pdfplumber+OCR({ocr_pages}p)'
            if len(pages) > n:
                warnings.append(f'OCR capped at {n} pages of {len(pages)}')
        except Exception as e:  # noqa
            warnings.append(f'ocr: {e}'[:160])
        shutil.rmtree(od, ignore_errors=True)
    text = '\n\n'.join(f'[p{i + 1}]\n{p}' for i, p in enumerate(pages) if p)
    meta['ocr_pages'] = ocr_pages
    return {'method': method, 'status': 'ok' if text.strip() else 'meta', 'meta': meta, 'text': text,
            'pages': pages, 'warnings': warnings}


# ---------------------------------------------------------------- 抽取：PPT
def extract_pptx(path):
    from pptx import Presentation
    from pptx.util import Emu  # noqa
    prs = Presentation(path)
    slides, texts, warnings = [], [], []

    def walk(shape, items):
        try:
            if shape.shape_type == 6 and hasattr(shape, 'shapes'):  # group
                for s in shape.shapes:
                    walk(s, items)
                return
            if getattr(shape, 'has_table', False) and shape.has_table:
                rows = []
                for r in shape.table.rows:
                    rows.append([c.text.strip() for c in r.cells])
                items.append({'t': 'table', 'rows': rows})
                return
            if getattr(shape, 'has_text_frame', False) and shape.has_text_frame:
                t = '\n'.join(p.text.strip() for p in shape.text_frame.paragraphs if p.text.strip())
                if t:
                    items.append({'t': 'p', 'text': t})
            if shape.shape_type == 13:
                items.append({'t': 'picture', 'name': getattr(shape, 'name', '')})
        except Exception as e:  # noqa
            warnings.append(f'shape: {e}'[:120])

    for i, slide in enumerate(prs.slides, 1):
        items = []
        for shape in slide.shapes:
            walk(shape, items)
        notes = ''
        try:
            if slide.has_notes_slide and slide.notes_slide.notes_text_frame is not None:
                notes = slide.notes_slide.notes_text_frame.text.strip()
        except Exception:  # noqa
            pass
        slides.append({'n': i, 'items': items, 'notes': notes})
        st = [it['text'] for it in items if it['t'] == 'p']
        st += ['\t'.join(r) for it in items if it['t'] == 'table' for r in it['rows']]
        if notes:
            st.append('[notes] ' + notes)
        texts.append(f'[slide {i}]\n' + '\n'.join(st))
    meta = {'slides': len(slides), 'pictures': sum(1 for s in slides for it in s['items'] if it['t'] == 'picture')}
    text = '\n\n'.join(texts)
    return {'method': 'python-pptx', 'status': 'ok' if re.sub(r'\[slide \d+\]', '', text).strip() else 'meta',
            'meta': meta, 'text': text, 'slides': slides, 'warnings': warnings}


# ---------------------------------------------------------------- 抽取：图片 / 视频 / 其他
def make_thumb(im, dest):
    from PIL import ImageOps
    try:
        im = ImageOps.exif_transpose(im)
    except Exception:  # noqa
        pass
    im = im.convert('RGB')
    im.thumbnail((THUMB_PX, THUMB_PX))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    im.save(dest, 'JPEG', quality=68, optimize=True)
    return os.path.getsize(dest)


def extract_image(path, thumb_path, tmp):
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    warnings = []
    im = Image.open(path)
    meta = {'format': im.format, 'width': im.size[0], 'height': im.size[1], 'mode': im.mode}
    try:
        exif = im.getexif()
        for tag, key in ((306, 'datetime'), (271, 'make'), (272, 'model'), (305, 'software')):
            if exif.get(tag):
                meta[key] = str(exif.get(tag))[:80]
    except Exception:  # noqa
        pass
    try:
        meta['thumb_bytes'] = make_thumb(im, thumb_path)
    except Exception as e:  # noqa
        warnings.append(f'thumb: {e}'[:120])
    ocr = None
    if OCR and have('tesseract'):
        try:
            w, h = im.size
            im2 = im.convert('RGB')
            if max(w, h) > 2200:
                im2.thumbnail((2200, 2200))
            elif max(w, h) < 700:
                im2 = im2.resize((int(w * 2), int(h * 2)))
            op = os.path.join(tmp, 'ocr_src.png')
            im2.save(op)
            t, conf = ocr_image_file(op)
            if t and len(re.sub(r'[\W_]+', '', t)) >= 3 and conf >= 45:
                ocr = {'text': t, 'conf': conf}
        except Exception as e:  # noqa
            warnings.append(f'ocr: {e}'[:120])
    text = ocr['text'] if ocr else ''
    return {'method': 'pillow+tesseract' if OCR else 'pillow', 'status': 'ok' if text else 'meta', 'meta': meta,
            'text': text, 'ocr': ocr, 'warnings': warnings}


def extract_video(path, thumb_path):
    meta, warnings = {}, []
    if have('ffprobe'):
        try:
            r = run(['ffprobe', '-v', 'error', '-print_format', 'json', '-show_format', '-show_streams', path], timeout=120)
            j = json.loads(r.stdout or '{}')
            fmt = j.get('format', {})
            meta['duration_s'] = round(float(fmt.get('duration', 0) or 0), 1)
            for s in j.get('streams', []):
                if s.get('codec_type') == 'video' and 'width' not in meta:
                    meta.update({'width': s.get('width'), 'height': s.get('height'), 'vcodec': s.get('codec_name')})
                if s.get('codec_type') == 'audio' and 'acodec' not in meta:
                    meta['acodec'] = s.get('codec_name')
            tags = fmt.get('tags', {})
            if tags.get('creation_time'):
                meta['creation_time'] = tags['creation_time']
        except Exception as e:  # noqa
            warnings.append(f'ffprobe: {e}'[:120])
    if have('ffmpeg'):
        try:
            os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
            ss = '2' if meta.get('duration_s', 0) > 3 else '0'
            run(['ffmpeg', '-y', '-v', 'error', '-ss', ss, '-i', path, '-frames:v', '1', '-vf', f'scale={THUMB_PX}:-2',
                 thumb_path], timeout=180)
            if os.path.exists(thumb_path):
                meta['thumb_bytes'] = os.path.getsize(thumb_path)
        except Exception as e:  # noqa
            warnings.append(f'ffmpeg: {e}'[:120])
    return {'method': 'ffprobe+ffmpeg', 'status': 'meta', 'meta': meta, 'text': '', 'warnings': warnings}


def extract_xmind(path):
    lines, warnings = [], []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if 'content.json' in names:
            data = json.loads(z.read('content.json').decode('utf-8', 'ignore'))

            def walk(topic, depth):
                if not isinstance(topic, dict):
                    return
                title = str(topic.get('title', '')).strip()
                note = ''
                n = topic.get('notes') or {}
                if isinstance(n, dict):
                    note = ((n.get('plain') or {}).get('content') or '').strip()
                lines.append('  ' * depth + '- ' + title + (f'  ⟦备注: {note}⟧' if note else ''))
                ch = topic.get('children') or {}
                for key in ('attached', 'detached', 'summary', 'callout'):
                    for t in ch.get(key, []) or []:
                        walk(t, depth + 1)

            for sheet in (data if isinstance(data, list) else [data]):
                lines.append(f"# Sheet: {sheet.get('title', '')}")
                walk(sheet.get('rootTopic') or {}, 0)
            method = 'xmind(content.json)'
        elif 'content.xml' in names:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(z.read('content.xml'))

            def lname(t):
                return t.split('}')[-1]

            def walk_xml(topic, depth):
                title = ''
                for c in topic:
                    if lname(c.tag) == 'title':
                        title = (c.text or '').strip()
                lines.append('  ' * depth + '- ' + title)
                for c in topic.iter():
                    pass
                for c in topic:
                    if lname(c.tag) == 'children':
                        for tps in c:
                            for t in tps:
                                if lname(t.tag) == 'topic':
                                    walk_xml(t, depth + 1)

            for sheet in root:
                if lname(sheet.tag) != 'sheet':
                    continue
                st = ''
                for c in sheet:
                    if lname(c.tag) == 'title':
                        st = (c.text or '').strip()
                lines.append(f'# Sheet: {st}')
                for c in sheet:
                    if lname(c.tag) == 'topic':
                        walk_xml(c, 0)
            method = 'xmind(content.xml)'
        else:
            method = 'xmind(unknown layout)'
            warnings.append('no content.json/xml: ' + ','.join(names[:10]))
    text = '\n'.join(lines)
    return {'method': method, 'status': 'ok' if text.strip() else 'meta', 'meta': {'lines': len(lines)}, 'text': text,
            'outline': lines, 'warnings': warnings}


def extract_archive(path, tmp):
    members, texts, warnings = [], [], []
    ext = os.path.splitext(path)[1].lower()
    od = os.path.join(tmp, 'arch')
    os.makedirs(od, exist_ok=True)
    ok = False
    if ext == '.zip':
        try:
            with zipfile.ZipFile(path) as z:
                z.extractall(od)
            ok = True
        except Exception as e:  # noqa
            warnings.append(f'zip: {e}'[:120])
    if not ok:
        for cmd in (['7z', 'x', '-y', f'-o{od}', path], ['unrar', 'x', '-y', path, od + '/']):
            if have(cmd[0]):
                try:
                    r = run(cmd, timeout=300)
                    ok = r.returncode == 0
                    if ok:
                        break
                    warnings.append(f'{cmd[0]}: ' + (r.stderr or r.stdout)[-200:])
                except Exception as e:  # noqa
                    warnings.append(f'{cmd[0]}: {e}'[:120])
    total = 0
    for dp, _, fns in os.walk(od):
        for fn in sorted(fns):
            fp = os.path.join(dp, fn)
            rel = os.path.relpath(fp, od)
            size = os.path.getsize(fp)
            m = {'name': rel, 'bytes': size}
            if size <= 2 * 1024 * 1024 and total < 4 * 1024 * 1024:
                try:
                    raw = open(fp, 'rb').read()
                    if b'\x00' not in raw[:4000]:
                        t = raw.decode('utf-8', 'ignore')
                        m['text'] = t
                        total += len(t)
                        texts.append(f'[{rel}]\n{t}')
                except Exception:  # noqa
                    pass
            members.append(m)
    shutil.rmtree(od, ignore_errors=True)
    text = '\n\n'.join(texts)
    return {'method': 'archive-extract', 'status': 'ok' if text.strip() else 'meta',
            'meta': {'members': len(members), 'extracted': ok}, 'text': text, 'members': members, 'warnings': warnings}


def extract_dxf(path):
    texts, warnings, meta = [], [], {}
    try:
        import ezdxf
        doc = ezdxf.readfile(path)
        msp = doc.modelspace()
        counts = {}
        for e in msp:
            t = e.dxftype()
            counts[t] = counts.get(t, 0) + 1
            try:
                if t == 'TEXT':
                    texts.append(e.dxf.text)
                elif t == 'MTEXT':
                    texts.append(e.plain_text())
                elif t == 'INSERT':
                    for a in e.attribs:
                        texts.append(f'{a.dxf.tag}={a.dxf.text}')
            except Exception:  # noqa
                pass
        meta = {'dxfversion': doc.dxfversion, 'layers': [l.dxf.name for l in doc.layers][:200], 'entities': counts}
        method = 'ezdxf'
    except Exception as e:  # noqa
        warnings.append(f'ezdxf: {e}'[:160])
        method = 'dxf-regex'
        try:
            raw = open(path, 'rb').read().decode('utf-8', 'ignore')
            lines = raw.splitlines()
            for i in range(len(lines) - 1):
                if lines[i].strip() == '1' and lines[i + 1].strip():
                    texts.append(lines[i + 1].strip())
        except Exception as e2:  # noqa
            warnings.append(f'regex: {e2}'[:120])
    texts = [t for t in (x.strip() for x in texts) if t]
    text = '\n'.join(dict.fromkeys(texts))
    return {'method': method, 'status': 'ok' if text.strip() else 'meta', 'meta': meta, 'text': text, 'warnings': warnings}


def extract_via_pdf(path, tmp, thumb_path=None):
    out, err = soffice_convert(path, 'pdf', tmp)
    if not out:
        return {'method': 'soffice→pdf', 'status': 'meta', 'meta': {}, 'text': '', 'warnings': [err]}
    ex = extract_pdf(out, tmp)
    ex['method'] = 'soffice→pdf→' + ex['method']
    if thumb_path and have('pdftoppm'):
        try:
            run(['pdftoppm', '-r', '40', '-png', '-f', '1', '-l', '1', out, os.path.join(tmp, 'pg')], timeout=120)
            pg = [f for f in os.listdir(tmp) if f.startswith('pg') and f.endswith('.png')]
            if pg:
                from PIL import Image
                ex['meta']['thumb_bytes'] = make_thumb(Image.open(os.path.join(tmp, pg[0])), thumb_path)
        except Exception as e:  # noqa
            ex['warnings'].append(f'thumb: {e}'[:120])
    return ex


def extract_psd(path, thumb_path):
    from PIL import Image
    meta, warnings = {}, []
    try:
        im = Image.open(path)
        meta = {'format': im.format, 'width': im.size[0], 'height': im.size[1], 'mode': im.mode}
        meta['thumb_bytes'] = make_thumb(im, thumb_path)
    except Exception as e:  # noqa
        warnings.append(f'psd: {e}'[:160])
    return {'method': 'pillow(psd composite)', 'status': 'meta', 'meta': meta, 'text': '', 'warnings': warnings}


def extract_any(rec, local, tmp):
    ext = rec['ext']
    thumb = os.path.join(THUMB_DIR, rec['id'] + '.jpg')
    if ext == '.docx':
        return extract_docx(local), None
    if ext == '.doc':
        return extract_doc(local, tmp), None
    if ext in ('.xlsx', '.xlsm', '.xls'):
        return extract_excel_any(local, tmp), None
    if ext == '.pdf':
        return extract_pdf(local, tmp), None
    if ext in ('.pptx',):
        return extract_pptx(local), None
    if ext in ('.ppt',):
        return extract_via_pdf(local, tmp), None
    if ext in IMG_EXT:
        return extract_image(local, thumb, tmp), thumb
    if ext in VID_EXT:
        return extract_video(local, thumb), thumb
    if ext == '.xmind':
        return extract_xmind(local), None
    if ext in ('.rar', '.zip', '.7z'):
        return extract_archive(local, tmp), None
    if ext == '.dxf':
        return extract_dxf(local), None
    if ext in ('.ai', '.eps'):
        with open(local, 'rb') as f:
            if f.read(5) == b'%PDF-':      # Illustrator 文件通常内嵌 PDF
                r = extract_pdf(local, tmp)
                r['method'] = 'ai-as-pdf→' + r['method']
                return r, None
        return extract_via_pdf(local, tmp, thumb), thumb
    if ext in ('.pub', '.cdr', '.odt', '.rtf', '.wps', '.vsd', '.vsdx', '.vdx'):
        return extract_via_pdf(local, tmp, thumb), thumb
    if ext == '.psd':
        return extract_psd(local, thumb), thumb
    if ext in ('.txt', '.csv', '.md', '.json', '.xml', '.mib', '.log'):
        t = open(local, 'rb').read().decode('utf-8', 'ignore')
        return {'method': 'text', 'status': 'ok' if t.strip() else 'meta', 'meta': {}, 'text': t, 'warnings': []}, None
    return {'method': 'none', 'status': 'meta', 'meta': {}, 'text': '', 'warnings': [f'no extractor for {ext}']}, None


# ---------------------------------------------------------------- 主流程
def load_index():
    d = json.load(open(INDEX, encoding='utf-8'))
    recs = []
    for f in d['files']:
        folder = f['所在子文件夹路径']
        parts = folder.split('/')
        top = parts[1] if len(parts) > 1 else '(root)'
        name = f['文件名']
        recs.append({'id': f['_drive_id'], 'name': name, 'path': folder + '/' + name, 'folder': folder, 'top': top,
                     'ext': os.path.splitext(name)[1].lower(), 'type': f['文件类型'], 'bytes': f.get('_bytes', 0),
                     'summary_old': f.get('内容摘要', '')})
    return d.get('meta', {}), recs


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    s = json.dumps(obj, ensure_ascii=False, indent=0, separators=(',', ':'))
    if len(s.encode('utf-8')) > MAX_JSON:
        for k in ('blocks', 'sheets', 'pages', 'slides', 'members'):
            obj.pop(k, None)
        obj['text'] = obj.get('text', '')[:MAX_JSON // 2]
        obj.setdefault('warnings', []).append('truncated: json > 12 MB')
        s = json.dumps(obj, ensure_ascii=False, indent=0, separators=(',', ':'))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)


class State:
    def __init__(self):
        self.manifest = {'meta': {}, 'files': {}}
        self.by_sha = {}
        self.recs_by_id = {}
        self.processed = 0
        self.since_commit = 0
        self.not_shared = 0
        if os.path.exists(os.path.join(OUT, 'manifest.json')):
            try:
                self.manifest = json.load(open(os.path.join(OUT, 'manifest.json'), encoding='utf-8'))
                for fid, m in self.manifest['files'].items():
                    if m.get('sha256') and m.get('status') in ('ok', 'meta'):
                        self.by_sha.setdefault(m['sha256'], fid)
            except Exception as e:  # noqa
                log('manifest unreadable, starting fresh:', e)
                self.manifest = {'meta': {}, 'files': {}}
        self.manifest['meta'].setdefault('backup', {})
        self.manifest['meta'].setdefault('runs', [])

    def finalize_dups(self):
        files = self.manifest['files']
        for m in files.values():
            if m.get('status') == 'dup' and m.get('same_as') in files:
                src = files[m['same_as']]
                m['chars'] = src.get('chars', 0)
                m['same_as_path'] = src.get('path', '')
                if not m.get('thumb'):
                    m['thumb'] = src.get('thumb', '')
                if not m.get('text_file'):
                    m['text_file'] = src.get('text_file', '')

    def save(self):
        os.makedirs(OUT, exist_ok=True)
        self.finalize_dups()
        files = self.manifest['files']
        st = {}
        for m in files.values():
            st[m['status']] = st.get(m['status'], 0) + 1
        self.manifest['meta'].update({'updated_at': now(), 'files_total_in_index': self.manifest['meta'].get('files_total_in_index', 0),
                                      'files_in_manifest': len(files), 'status_counts': st, 'release_tag': RELEASE_TAG if BACKUP else ''})
        write_json(os.path.join(OUT, 'manifest.json'), {'meta': self.manifest['meta'],
                                                        'files': dict(sorted(files.items(), key=lambda kv: kv[1]['path']))})
        cols = ['id', 'path', 'type', 'ext', 'bytes', 'sha256', 'status', 'method', 'chars', 'same_as', 'text_file', 'thumb', 'error']
        with open(os.path.join(OUT, 'manifest.csv'), 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(cols)
            for m in sorted(files.values(), key=lambda m: m['path']):
                w.writerow([m.get(c, '') for c in cols])


def git_commit_push(msg):
    if not GIT_COMMIT:
        return
    try:
        rel = os.path.relpath(OUT, ROOT)
        subprocess.run(['git', 'add', rel], cwd=ROOT, check=True)
        r = subprocess.run(['git', 'commit', '-q', '-m', msg], cwd=ROOT)
        if r.returncode != 0:
            log('nothing to commit')
            return
        ref = GIT_REF or subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=ROOT,
                                        capture_output=True, text=True).stdout.strip()
        for attempt in range(6):
            subprocess.run(['git', 'pull', '-q', '--rebase', '-X', 'theirs', 'origin', ref], cwd=ROOT)
            p = subprocess.run(['git', 'push', '-q', 'origin', f'HEAD:{ref}'], cwd=ROOT)
            if p.returncode == 0:
                log(f'pushed: {msg}')
                return
            time.sleep(5 + attempt * 5)
        log('push failed after retries')
    except Exception as e:  # noqa
        log('git error', e)


def process_one(rec, state):
    t0 = time.time()
    local = os.path.join(RAW_DIR, rec['path'])
    tmp = os.path.join(RAW_DIR, '_tmp', rec['id'])
    os.makedirs(tmp, exist_ok=True)
    m = {'id': rec['id'], 'name': rec['name'], 'path': rec['path'], 'folder': rec['folder'], 'top': rec['top'],
         'type': rec['type'], 'ext': rec['ext'], 'bytes': rec['bytes'], 'sha256': '', 'status': 'fail', 'method': '',
         'chars': 0, 'same_as': '', 'text_file': '', 'thumb': '', 'error': '', 'at': now(),
         'index_summary': rec.get('summary_old', '')}
    try:
        err = download(rec, local)
        if err:
            m['error'] = err
            return m, None
        m['bytes_actual'] = os.path.getsize(local)
        m['sha256'] = sha256_file(local)
        with LOCK:
            dup_of = state.by_sha.get(m['sha256'])
            if dup_of and dup_of != rec['id']:
                pass
            else:
                state.by_sha[m['sha256']] = rec['id']
                dup_of = None
        if dup_of:
            src = state.recs_by_id.get(dup_of) or state.manifest['files'].get(dup_of, {})
            m.update({'status': 'dup', 'same_as': dup_of, 'same_as_path': src.get('path', ''), 'method': 'sha256 duplicate'})
            stub = {'id': rec['id'], 'name': rec['name'], 'path': rec['path'], 'bytes': rec['bytes'], 'sha256': m['sha256'],
                    'same_as': dup_of, 'same_as_path': src.get('path', ''), 'same_as_json': f'text/{dup_of}.json',
                    'note': '内容与 same_as 文件完全相同（sha256 一致），全文见该文件的 JSON'}
            if rec['ext'] not in IMG_EXT and rec['ext'] not in VID_EXT:
                write_json(os.path.join(TEXT_DIR, rec['id'] + '.json'), stub)
                m['text_file'] = f'text/{rec["id"]}.json'
            return m, None
        ex, thumb = extract_any(rec, local, tmp)
        text = ex.get('text') or ''
        m['status'] = ex.get('status', 'meta')
        m['method'] = ex.get('method', '')
        m['chars'] = len(text)
        if ex.get('warnings'):
            m['warnings'] = ex['warnings'][:8]
        if thumb and os.path.exists(thumb):
            m['thumb'] = f'thumbs/{rec["id"]}.jpg'
        if rec['ext'] in IMG_EXT or rec['ext'] in VID_EXT:
            # 图片/视频：只在 manifest 里记元数据 + OCR 文字（不单独写 JSON，除非 OCR 有字）
            m['meta'] = ex.get('meta', {})
            if text:
                m['ocr_text'] = text[:1500]
                m['ocr_conf'] = (ex.get('ocr') or {}).get('conf')
                write_json(os.path.join(TEXT_DIR, rec['id'] + '.json'),
                           {'id': rec['id'], 'name': rec['name'], 'path': rec['path'], 'type': rec['type'], 'bytes': rec['bytes'],
                            'sha256': m['sha256'], 'extracted_at': now(), 'method': m['method'], 'meta': m['meta'],
                            'ocr': ex.get('ocr'), 'text': text})
                m['text_file'] = f'text/{rec["id"]}.json'
        else:
            rec_out = {'id': rec['id'], 'name': rec['name'], 'path': rec['path'], 'type': rec['type'], 'ext': rec['ext'],
                       'bytes': rec['bytes'], 'sha256': m['sha256'], 'extracted_at': now(), 'method': m['method'],
                       'status': m['status'], 'chars': m['chars'], 'meta': ex.get('meta', {}),
                       'warnings': ex.get('warnings', []), 'text': text}
            for k in ('blocks', 'textboxes', 'header_footer', 'embedded_media', 'sheets', 'pages', 'slides',
                      'outline', 'members', 'ocr'):
                if ex.get(k):
                    rec_out[k] = ex[k]
            write_json(os.path.join(TEXT_DIR, rec['id'] + '.json'), rec_out)
            m['text_file'] = f'text/{rec["id"]}.json'
        return m, None
    except Exception as e:  # noqa
        m['error'] = f'{type(e).__name__}: {e}'[:300]
        m['trace'] = traceback.format_exc()[-800:]
        return m, None
    finally:
        m['secs'] = round(time.time() - t0, 1)
        shutil.rmtree(tmp, ignore_errors=True)


def gh_release_ensure():
    r = run(['gh', 'release', 'view', RELEASE_TAG], timeout=120)
    if r.returncode == 0:
        return True
    cmd = ['gh', 'release', 'create', RELEASE_TAG, '--latest=false', '--title',
           f'Drive《SmartByte》原始文件备份 {RELEASE_TAG[-8:]}',
           '--notes', 'T28：Google Drive《SmartByte》文件夹（5.7 GB，2,385 文件）删除前的完整原件备份，按顶层文件夹打包。'
                      '抽取出的全文/缩略图/清单见分支 arena/3f35b9b3-planet 的 data/smartbyte_drive/。']
    if RELEASE_TARGET:
        cmd += ['--target', RELEASE_TARGET]
    r = run(cmd, timeout=180)
    if r.returncode != 0:
        log('release create failed:', (r.stderr or r.stdout)[-300:])
        return False
    return True


def backup_folder(top, recs, state):
    """把该顶层文件夹已下载的原件打成 ≤PART_MAX 的 zip 分卷并上传到 Release。
    若该文件夹此前已备份完成（补漏 / 重试运行），新文件打成独立的 retry 分卷追加，绝不覆盖已有分卷。"""
    files = []
    for r in recs:
        p = os.path.join(RAW_DIR, r['path'])
        if os.path.exists(p):
            files.append((r, p, os.path.getsize(p)))
    if not files:
        return []
    prev = state.manifest['meta']['backup'].get(top) or {}
    supplement = bool(prev.get('done')) and bool(prev.get('parts')) and not FORCE
    os.makedirs(ZIP_DIR, exist_ok=True)
    slug = FOLDER_SLUG.get(top) or re.sub(r'[^A-Za-z0-9._-]+', '_', top).strip('_') or 'folder'
    if supplement:
        slug += '_retry' + datetime.now(timezone.utc).strftime('%Y%m%d%H%M')
    parts, cur, cur_size, idx = [], [], 0, 1

    def flush():
        nonlocal cur, cur_size, idx
        if not cur:
            return
        name = f'smartbyte_drive_{slug}_part{idx:02d}.zip'
        zp = os.path.join(ZIP_DIR, name)
        with zipfile.ZipFile(zp, 'w', zipfile.ZIP_STORED, allowZip64=True) as z:
            for r, p, _ in cur:
                z.write(p, r['path'])
        parts.append({'asset': name, 'bytes': os.path.getsize(zp), 'sha256': sha256_file(zp), 'files': [r['id'] for r, _, _ in cur],
                      'paths': [r['path'] for r, _, _ in cur]})
        cur, cur_size, idx = [], 0, idx + 1

    for r, p, s in files:
        if cur and cur_size + s > PART_MAX:
            flush()
        cur.append((r, p, s))
        cur_size += s
    flush()
    ok_all = True
    if have('gh') and gh_release_ensure():
        for part in parts:
            zp = os.path.join(ZIP_DIR, part['asset'])
            done = False
            for attempt in range(4):
                r = run(['gh', 'release', 'upload', RELEASE_TAG, zp, '--clobber'], timeout=3600)
                if r.returncode == 0:
                    done = True
                    break
                log('upload retry', part['asset'], (r.stderr or r.stdout)[-200:])
                time.sleep(10 + attempt * 20)
            part['uploaded'] = done
            ok_all = ok_all and done
            if done:
                os.remove(zp)
    else:
        for part in parts:
            part['uploaded'] = False
        ok_all = False
        log('gh not available / release failed; zips kept in', ZIP_DIR)
    if supplement:
        merged = dict(prev)
        merged.update({'done': bool(prev.get('done')) and ok_all, 'at': now(), 'files': prev.get('files', 0) + len(files),
                       'bytes': prev.get('bytes', 0) + sum(s for _, _, s in files), 'parts': list(prev.get('parts', [])) + parts,
                       'retries': prev.get('retries', 0) + 1})
        state.manifest['meta']['backup'][top] = merged
    else:
        state.manifest['meta']['backup'][top] = {'done': ok_all, 'at': now(), 'files': len(files),
                                                  'bytes': sum(s for _, _, s in files), 'parts': parts}
    if ok_all:
        for _, p, _ in files:
            try:
                os.remove(p)
            except OSError:
                pass
    return parts


def coverage_md(state, index_meta, recs):
    files = state.manifest['files']
    by_type, by_top = {}, {}
    for r in recs:
        m = files.get(r['id'])
        st = m['status'] if m else 'pending'
        by_type.setdefault(r['type'], {}).setdefault(st, 0)
        by_type[r['type']][st] += 1
        by_top.setdefault(r['top'], {}).setdefault(st, 0)
        by_top[r['top']][st] += 1
    sts = ['ok', 'meta', 'dup', 'fail', 'pending']
    L = ['# Drive《SmartByte》全量入库 · 覆盖率报告', '',
         f'- 生成时间：{now()}；索引：{len(recs)} 个文件（{index_meta.get("总大小", "")}），manifest：{len(files)} 条',
         '- 状态含义：**ok** = 抽到正文（Word 段落+表格 / Excel 逐行 / PDF 逐页(或 OCR) / PPT 逐页 / 图片 OCR 有字）；'
         '**meta** = 只有元数据+缩略图（无文字的图片/视频/设计源文件，或空文档）；**dup** = 与另一文件 sha256 完全相同，指向 same_as；'
         '**fail** = 下载或解析失败（见下表）；**pending** = 本次未处理',
         f'- 原件备份：GitHub Release `{RELEASE_TAG}`（私有仓库，按顶层文件夹分卷 zip）' if BACKUP else '- 原件备份：本次未开启',
         '', '## 按类型', '', '| 类型 | ' + ' | '.join(sts) + ' | 合计 |', '|---|' + '---|' * (len(sts) + 1)]
    for t, d in sorted(by_type.items(), key=lambda kv: -sum(kv[1].values())):
        L.append(f'| {t} | ' + ' | '.join(str(d.get(s, 0)) for s in sts) + f' | {sum(d.values())} |')
    L += ['', '## 按顶层文件夹', '', '| 文件夹 | ' + ' | '.join(sts) + ' | 合计 | 备份 |', '|---|' + '---|' * (len(sts) + 2)]
    for t in FOLDER_ORDER + [x for x in by_top if x not in FOLDER_ORDER]:
        d = by_top.get(t)
        if not d:
            continue
        b = state.manifest['meta']['backup'].get(t)
        bs = ('✅ ' + ', '.join(p['asset'] for p in b['parts'])) if b and b.get('done') else ('⚠️ 未完成' if b else '—')
        L.append(f'| {t} | ' + ' | '.join(str(d.get(s, 0)) for s in sts) + f' | {sum(d.values())} | {bs} |')
    fails = [m for m in files.values() if m['status'] == 'fail']
    L += ['', f'## 失败清单（{len(fails)}）', '']
    if fails:
        L += ['| 路径 | 类型 | 大小 | 错误 |', '|---|---|---|---|']
        for m in sorted(fails, key=lambda m: m['path']):
            L.append(f"| {m['path'].replace('|', '/')} | {m['type']} | {m['bytes']} | {m.get('error', '').replace('|', '/')} |")
    else:
        L.append('无。')
    metas = [m for m in files.values() if m['status'] == 'meta' and m['type'] not in ('图片', '视频')]
    L += ['', f'## 仅元数据的非图片文件（{len(metas)}）', '']
    if metas:
        L += ['| 路径 | 类型 | 抽取方式 | 说明 |', '|---|---|---|---|']
        for m in sorted(metas, key=lambda m: m['path']):
            L.append(f"| {m['path'].replace('|', '/')} | {m['type']} | {m.get('method', '')} | {'; '.join(m.get('warnings', []))[:160].replace('|', '/')} |")
    else:
        L.append('无。')
    chars = sum(m.get('chars', 0) for m in files.values() if m['status'] == 'ok')
    ocr_imgs = sum(1 for m in files.values() if m['type'] == '图片' and m['status'] == 'ok')
    L += ['', '## 体量', '', f'- 抽取正文合计 {chars:,} 字符；图片 OCR 有字 {ocr_imgs} 张；缩略图 '
          f'{sum(1 for m in files.values() if m.get("thumb") and m["status"] != "dup")} 张',
          f'- 运行记录：{json.dumps(state.manifest["meta"].get("runs", [])[-3:], ensure_ascii=False)}']
    with open(os.path.join(OUT, '_coverage.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')


def fetch_source_release():
    """备选来源：从 Release 下载 Simon 手工上传的 Drive 打包 zip，解压成目录树后当作 LOCAL_DIR。"""
    global LOCAL_DIR
    base = os.path.join(os.path.dirname(RAW_DIR.rstrip('/')) or '/tmp', 'drive_src')
    zdir, tree = os.path.join(base, 'zips'), os.path.join(base, 'tree')
    os.makedirs(zdir, exist_ok=True)
    os.makedirs(tree, exist_ok=True)
    r = run(['gh', 'release', 'download', SOURCE_RELEASE, '-D', zdir, '--pattern', '*.zip', '--clobber'], timeout=7200)
    if r.returncode != 0:
        log('release download failed:', (r.stderr or r.stdout)[-300:])
        sys.exit(3)
    for fn in sorted(os.listdir(zdir)):
        if not fn.lower().endswith('.zip'):
            continue
        log('unzip', fn)
        try:
            with zipfile.ZipFile(os.path.join(zdir, fn)) as z:
                for info in z.infolist():
                    # Drive 打包：成员名是 cp437 误码的 UTF-8 时修正
                    name = info.filename
                    if info.flag_bits & 0x800 == 0:
                        try:
                            name = name.encode('cp437').decode('utf-8')
                        except Exception:  # noqa
                            pass
                    if name.endswith('/'):
                        continue
                    out = os.path.join(tree, name)
                    os.makedirs(os.path.dirname(out), exist_ok=True)
                    with z.open(info) as src, open(out, 'wb') as dst:
                        shutil.copyfileobj(src, dst, 1 << 20)
        except zipfile.BadZipFile:
            run(['7z', 'x', '-y', f'-o{tree}', os.path.join(zdir, fn)], timeout=3600)
        os.remove(os.path.join(zdir, fn))
    # 顶层若不是 SmartByte/ 而是直接子目录，则补一层
    if not os.path.isdir(os.path.join(tree, 'SmartByte')):
        inner = os.path.join(tree, 'SmartByte')
        os.makedirs(inner, exist_ok=True)
        for fn in os.listdir(tree):
            if fn != 'SmartByte':
                shutil.move(os.path.join(tree, fn), os.path.join(inner, fn))
    LOCAL_DIR = tree
    log('source release ready at', tree)


def main():
    global LOCAL_DIR, RELEASE_TAG
    if SOURCE_RELEASE and not LOCAL_DIR:
        fetch_source_release()
    index_meta, recs = load_index()
    state = State()
    # 续跑 / 补漏时沿用第一次备份用的 Release，避免按日期散落到多个 Release
    prev_tag = state.manifest['meta'].get('release_tag')
    if prev_tag and not os.environ.get('RELEASE_TAG') and not FORCE:
        RELEASE_TAG = prev_tag
    state.recs_by_id = {r['id']: r for r in recs}
    state.manifest['meta']['files_total_in_index'] = len(recs)
    state.manifest['meta']['index_source'] = index_meta.get('来源', '')
    log(f'index: {len(recs)} files; manifest has {len(state.manifest["files"])}; tools: '
        + ' '.join(f'{c}={"y" if have(c) else "n"}' for c in ('tesseract', 'soffice', 'pdftoppm', 'ffmpeg', '7z', 'unrar', 'gh')))
    todo = recs
    if ONLY_FOLDERS:
        todo = [r for r in todo if r['top'] in ONLY_FOLDERS]
    if ONLY_TYPES:
        todo = [r for r in todo if r['type'] in ONLY_TYPES]
    if not FORCE:
        def done(r):
            m = state.manifest['files'].get(r['id'])
            if not m or m['status'] == 'fail':
                return False
            if BACKUP and not (state.manifest['meta']['backup'].get(r['top']) or {}).get('done'):
                return False
            return True
        todo = [r for r in todo if not done(r)]
    if LIMIT:
        todo = todo[:LIMIT]
    log(f'to process: {len(todo)}')
    run_rec = {'started': now(), 'todo': len(todo), 'workers': WORKERS, 'backup': BACKUP, 'ocr': OCR}
    state.manifest['meta']['runs'].append(run_rec)
    order = {t: i for i, t in enumerate(FOLDER_ORDER)}
    tops = sorted({r['top'] for r in todo}, key=lambda t: order.get(t, 99))
    os.makedirs(TEXT_DIR, exist_ok=True)
    os.makedirs(THUMB_DIR, exist_ok=True)
    total_done = 0
    for top in tops:
        group = [r for r in todo if r['top'] == top]
        # 大文件夹：先处理文档再处理图片，便于尽早提交有价值内容
        group.sort(key=lambda r: (r['ext'] in IMG_EXT or r['ext'] in VID_EXT, r['path']))
        log(f'== folder {top}: {len(group)} files')
        n_ok = 0
        abort = False
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            futs = {ex.submit(process_one, r, state): r for r in group}
            for fut in as_completed(futs):
                m, _ = fut.result()
                with LOCK:
                    state.manifest['files'][m['id']] = m
                    state.processed += 1
                    state.since_commit += 1
                    total_done += 1
                    n_ok += m['status'] in ('ok', 'meta', 'dup')
                    if m['status'] == 'fail' and str(m.get('error', '')).startswith('NOT_SHARED'):
                        state.not_shared += 1
                        if state.not_shared >= 5 and state.processed <= 40:
                            abort = True
                    elif m['status'] != 'fail':
                        state.not_shared = 0
                    if state.processed % 50 == 0:
                        log(f'{state.processed}/{len(todo)} done; last: {m["status"]} {m["path"][-60:]} ({m.get("secs")}s)')
                    if state.since_commit >= COMMIT_EVERY:
                        state.save()
                        git_commit_push(f'T28: Drive《SmartByte》入库 +{state.since_commit}（累计 {state.processed}/{len(todo)}，{top}）')
                        state.since_commit = 0
                if abort:
                    log('ABORT: Drive 连续返回登录/申请权限页 —— 《SmartByte》文件夹还没有设为「知道链接的任何人可查看」。'
                        '请先设置共享再重跑。')
                    ex.shutdown(wait=False, cancel_futures=True)
                    break
        if abort:
            state.save()
            coverage_md(state, index_meta, recs)
            sys.exit(2)
        if BACKUP and not LOCAL_DIR:
            parts = backup_folder(top, group, state)
            log(f'backup {top}: {len(parts)} parts, done={state.manifest["meta"]["backup"].get(top, {}).get("done")}')
        elif BACKUP and LOCAL_DIR:
            state.manifest['meta']['backup'][top] = {'done': True, 'at': now(), 'files': len(group), 'parts': [],
                                                      'note': f'原件来源 Release {SOURCE_RELEASE}（Simon 手工上传的 Drive 打包）' if SOURCE_RELEASE else 'LOCAL_DIR test'}
        state.save()
        coverage_md(state, index_meta, recs)
        git_commit_push(f'T28: Drive《SmartByte》入库 · {top} 完成（{n_ok}/{len(group)}，累计 {state.processed}/{len(todo)}）')
        state.since_commit = 0
    run_rec.update({'finished': now(), 'processed': state.processed})
    state.save()
    coverage_md(state, index_meta, recs)
    git_commit_push(f'T28: Drive《SmartByte》入库收口（本次 {state.processed}，manifest {len(state.manifest["files"])}/{len(recs)}）')
    st = state.manifest['meta'].get('status_counts', {})
    log('DONE', json.dumps(st, ensure_ascii=False))


def maybe_dispatch_run_file():
    """RUN 文件里若有 `JOB=gmail` / `JOB=files`（KEY=VALUE 行），把本次运行转交给 scripts/gmail_ingest/ingest.py /
    scripts/drive_ingest/files_job.py（复用同一 workflow，无需再另存新的 workflow 文件）。RUN 里的 KEY=VALUE 覆盖 workflow 传入的环境变量；Drive 专用变量不下传。"""
    run_file = os.environ.get('RUN_FILE') or os.path.join(ROOT, 'scripts', 'drive_ingest', 'RUN')
    try:
        lines = open(run_file, encoding='utf-8').read().splitlines()
    except Exception:  # noqa
        return
    kv = {}
    for ln in lines:
        ln = ln.strip()
        if not ln or ln.startswith('#') or '=' not in ln:
            continue
        k, v = ln.split('=', 1)
        kv[k.strip().upper()] = v.strip().strip('"').strip("'")
    job = kv.pop('JOB', '').lower()
    scripts = {'gmail': os.path.join(ROOT, 'scripts', 'gmail_ingest', 'ingest.py'),
               'files': os.path.join(ROOT, 'scripts', 'drive_ingest', 'files_job.py')}
    if job not in scripts:
        return
    env = dict(os.environ)
    for k in ('COMMIT_EVERY', 'ONLY_FOLDERS', 'ONLY_TYPES', 'WORKERS', 'INDEX', 'OUT_DIR', 'LOCAL_DIR', 'SOURCE_RELEASE', 'OCR', 'LIMIT', 'FORCE'):
        env.pop(k, None)
    env.update(kv)
    script = scripts[job]
    log(f'RUN says JOB={job} → dispatch to', script, json.dumps({k: (v if k != 'SOURCE_IDS' else v[:60]) for k, v in kv.items()}))
    sys.stdout.flush()
    os.execve(sys.executable, [sys.executable, script], env)


if __name__ == '__main__':
    maybe_dispatch_run_file()
    main()
