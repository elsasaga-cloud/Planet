#!/usr/bin/env python3
"""
通用「Drive 文件 / 压缩包 → 全保真抽取入库」任务（RUN 里写 JOB=files 即转交到这里；复用 Drive SmartByte ingest workflow）。

用途：Simon 临时上传到 Drive 的单个文件或压缩包（例如供应商最新规格书 zip），连接器下不动（>100 MB）或抽不全（Word 表格丢失），
由 Actions 运行器下载 → 解包（zip/rar/7z，递归；修正 Windows GBK 文件名）→ 每个成员按类型抽取（Word 段落+表格 / Excel 逐行 /
PDF 逐页+OCR / PPT / 图片缩略图+OCR …，复用 drive_ingest/ingest.py 的抽取器）→ data/<OUT_NAME>/{manifest.json,text/*.json,thumbs/,_coverage.md}
→ 提交回分支；原件可选上传 Release。

RUN 里的 KEY=VALUE（经 maybe_dispatch_run_file 传入环境）：
  JOB=files
  SOURCE_IDS     Drive 文件 ID（逗号分隔；需「知道链接的任何人可查看」）
  SOURCE_MD5     可选，与 SOURCE_IDS 对齐的 md5Checksum，下载后校验
  OUT_NAME       输出目录名 → data/<OUT_NAME>/（必填，例如 hrui_specs_2026-10）
  TITLE          覆盖率报告标题（可选）
  OCR            1 = 图片/无文字层 PDF 送 tesseract（默认 1）
  OCR_MIN_KB     图片送 OCR 的最小大小（默认 8）
  WORKERS        抽取并发（默认 4）
  BACKUP         1 = 原件上传 Release files-<OUT_NAME>（默认 1）
  LOCAL_FILES    本地测试：逗号分隔的本地路径（代替 SOURCE_IDS）
  SOURCE_RELEASE 备选来源：从本仓库 Release <tag> 下载原件（上次运行已备份到 files-<OUT_NAME> 时用，分卷 .partNN 自动合并；
                 不再碰 Drive，不占 Drive 下载配额；仍按 SOURCE_MD5 校验）
  CHECKPOINT_MIN 抽取阶段每隔多少分钟提交一次进度（默认 10；2026-10-23 Extra Info 第 5 次运行在抽取阶段无声死亡、无任何提交后加）

崩溃处理（2026-10-23）：main() 外层捕获一切异常 → _run_status.md 写 CRASH + traceback 并提交；抽取阶段每 CHECKPOINT_MIN 分钟
把已完成的 manifest / 进度提交一次（即便之后被 OOM 杀掉，也能看到走到哪）。
"""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT_NAME = (os.environ.get('OUT_NAME') or '').strip()
OUT = os.path.join(ROOT, 'data', OUT_NAME) if OUT_NAME else ''
RAW_DIR = os.environ.get('RAW_DIR') or '/tmp/files_raw'
SOURCE_IDS = [x.strip() for x in os.environ.get('SOURCE_IDS', '').split(',') if x.strip()]
SOURCE_MD5 = [x.strip().lower() for x in os.environ.get('SOURCE_MD5', '').split(',')]
LOCAL_FILES = [x.strip() for x in os.environ.get('LOCAL_FILES', '').split(',') if x.strip()]
SOURCE_RELEASE = (os.environ.get('SOURCE_RELEASE') or '').strip()
CHECKPOINT_MIN = float(os.environ.get('CHECKPOINT_MIN', '10'))
TITLE = os.environ.get('TITLE') or f'Drive 文件入库：{OUT_NAME}'
OCR = os.environ.get('OCR', '1') == '1'
OCR_MIN_KB = float(os.environ.get('OCR_MIN_KB', '8'))
WORKERS = int(os.environ.get('WORKERS', '4'))
BACKUP = os.environ.get('BACKUP', '1') == '1'
GIT_COMMIT = os.environ.get('GIT_COMMIT', '1') == '1'
GIT_REF = os.environ.get('GIT_REF', '')
RELEASE_TARGET = os.environ.get('RELEASE_TARGET', '')
RELEASE_TAG = os.environ.get('RELEASE_TAG') or f'files-{OUT_NAME}'
ARCHIVE_EXT = {'.zip', '.rar', '.7z', '.tgz', '.tar', '.gz'}
SKIP_NAMES = {'thumbs.db', 'desktop.ini', '.ds_store'}
T0 = time.time()
_DRIVE = None


def log(*a):
    print(f'[{time.time() - T0:7.1f}s]', *a, flush=True)


def _free_gb(path):
    try:
        return round(shutil.disk_usage(path).free / 1024 ** 3, 1)
    except Exception:  # noqa
        return '?'


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def have(cmd):
    return shutil.which(cmd) is not None


def run(cmd, timeout=600, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, **kw)


def drive_mod():
    global _DRIVE
    if _DRIVE is None:
        p = os.path.join(ROOT, 'scripts', 'drive_ingest', 'ingest.py')
        spec = importlib.util.spec_from_file_location('drive_ingest_mod', p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        m.THUMB_DIR = os.path.join(OUT, 'thumbs')
        m.OCR = OCR and have('tesseract')
        _DRIVE = m
    return _DRIVE


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=0, separators=(',', ':')))


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
        ref = GIT_REF or subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
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


def abort(code, why):
    log('ABORT:', why)
    try:
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, '_run_status.md'), 'w', encoding='utf-8') as f:
            f.write(f'# {TITLE} · 运行状态\n\n- {now()} **ABORT（exit {code}）**：{why}\n')
        git_commit_push(f'files({OUT_NAME}) 入库中止：{why[:80]}')
    except Exception as e:  # noqa
        log('abort note failed', e)
    sys.exit(code)


# ---------------------------------------------------------------- 来源
def resolve_sources():
    os.makedirs(RAW_DIR, exist_ok=True)
    if LOCAL_FILES:
        return [(os.path.basename(p), p) for p in LOCAL_FILES]
    if SOURCE_RELEASE:
        d = os.path.join(RAW_DIR, 'release')
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d, exist_ok=True)
        log('source: Release', SOURCE_RELEASE)
        r = run(['gh', 'release', 'download', SOURCE_RELEASE, '-D', d, '--clobber'], timeout=7200)
        if r.returncode != 0:
            abort(3, f'release download failed ({SOURCE_RELEASE}): ' + (r.stderr or r.stdout)[-300:])
        parts = defaultdict(list)
        for fn in sorted(os.listdir(d)):
            m = re.fullmatch(r'(.+)\.part(\d+)', fn)
            if m:
                parts[m.group(1)].append(fn)
        for base, fns in parts.items():
            with open(os.path.join(d, base), 'wb') as w:
                for fn in sorted(fns):
                    with open(os.path.join(d, fn), 'rb') as rf:
                        shutil.copyfileobj(rf, w, 1 << 20)
                    os.remove(os.path.join(d, fn))
        paths = [(fn, os.path.join(d, fn)) for fn in sorted(os.listdir(d)) if not fn.endswith('.json')]
        if not paths:
            abort(3, f'Release {SOURCE_RELEASE} has no usable assets')
        want = [x for x in SOURCE_MD5 if re.fullmatch(r'[0-9a-f]{32}', x or '')]
        if want and len(paths) == 1:
            h = hashlib.md5()
            with open(paths[0][1], 'rb') as f:
                for chunk in iter(lambda: f.read(1 << 22), b''):
                    h.update(chunk)
            log(f'md5 {paths[0][0]}: {h.hexdigest()} {"==" if h.hexdigest() == want[0] else "!="} {want[0]}')
            if h.hexdigest() != want[0]:
                abort(3, f'Release copy md5 mismatch: {h.hexdigest()} != {want[0]}（Release {SOURCE_RELEASE} 的分卷不完整？）')
        for name, p in paths:
            log('source', name, os.path.getsize(p), 'bytes (from Release)')
        return paths
    if not SOURCE_IDS:
        abort(1, 'no source: set SOURCE_IDS (or LOCAL_FILES / SOURCE_RELEASE)')
    dm = drive_mod()
    import requests
    paths = []
    for i, fid in enumerate(SOURCE_IDS):
        name, expect = fid, 0
        want_md5 = SOURCE_MD5[i] if i < len(SOURCE_MD5) and re.fullmatch(r'[0-9a-f]{32}', SOURCE_MD5[i] or '') else ''
        try:
            with requests.get(dm.DL_URL.format(id=fid), stream=True, timeout=(15, 60), headers={'User-Agent': 'Mozilla/5.0'}) as r:
                cd = r.headers.get('Content-Disposition', '')
                m = re.search(r"filename\*=UTF-8''([^;]+)", cd) or re.search(r'filename="?([^";]+)"?', cd)
                if m:
                    from urllib.parse import unquote
                    name = unquote(m.group(1))
                    # requests 把 header 当 latin-1 解码：Google 对中文名只给 filename="..."（UTF-8 字节）→ 会变成 æ´ªç 式乱码，这里还原
                    try:
                        fixed = name.encode('latin-1').decode('utf-8')
                        if fixed != name:
                            name = fixed
                    except (UnicodeEncodeError, UnicodeDecodeError):
                        pass
                ctype = r.headers.get('Content-Type', '')
                if 'text/html' in ctype:
                    body = r.content[:6000].decode('utf-8', 'ignore')
                    if 'ServiceLogin' in body or 'accounts.google.com' in body or 'Request access' in body:
                        abort(2, f'{fid} 未共享（返回登录页）；请设为「知道链接的任何人可查看」后重跑')
                else:
                    expect = int(r.headers.get('Content-Length') or 0)
        except SystemExit:
            raise
        except Exception as e:  # noqa
            log('probe failed', fid, e)
        ext = os.path.splitext(name)[1].lower() or '.bin'
        dest = os.path.join(RAW_DIR, re.sub(r'[^\w.\-]+', '_', name) if name != fid else f'{fid}{ext}')
        ptag = dm.partial_tag(f'files-{OUT_NAME}')      # 跨次运行续传暂存（2026-10-23）
        resumed = 0
        for attempt in (1, 2):
            if not (os.path.exists(dest) and os.path.getsize(dest) > 0 and (not expect or os.path.getsize(dest) == expect)):
                if attempt == 1:
                    err, expect, resumed, note = dm.fetch_with_resume(dm.download, fid, dest, expect, name, ext, ptag, log_fn=log)
                else:
                    if os.path.exists(dest):
                        os.remove(dest)
                    log('download (fresh)', fid, '→', dest, f'(expect {expect} bytes)' if expect else '')
                    err, note = dm.download({'id': fid, 'ext': ext, 'path': '', 'folder': '', 'name': name, 'bytes': expect}, dest), ''
                if err:
                    abort(2 if err.startswith('NOT_SHARED') else 3, f'download failed {fid}: {err[:160]}' + (f' ｜ {note}' if note else ''))
            got = os.path.getsize(dest)
            ok = (not expect or got == expect)
            if ok and want_md5:
                h = hashlib.md5()
                with open(dest, 'rb') as f:
                    for chunk in iter(lambda: f.read(1 << 22), b''):
                        h.update(chunk)
                ok = h.hexdigest() == want_md5
                log(f'md5 {dest}: {h.hexdigest()} {"==" if ok else "!="} {want_md5}')
            if ok:
                if resumed:
                    dm.partial_cleanup(fid, ptag)
                break
            if attempt == 2:
                abort(3, f'download verify failed twice: {dest} size {got} expect {expect} md5 {want_md5 or "-"}')
            if resumed:
                dm.partial_cleanup(fid, ptag)
            os.remove(dest)
        log('source', name, os.path.getsize(dest), 'bytes')
        paths.append((name, dest))
    return paths


# ---------------------------------------------------------------- 解包
def _fix_zip_name(zi):
    """Windows 打包的 zip 中文名多为 GBK，Python 按 cp437 解码成乱码；没有 UTF-8 标志位时尝试还原。"""
    if zi.flag_bits & 0x800:
        return zi.filename
    try:
        return zi.filename.encode('cp437').decode('gbk')
    except Exception:  # noqa
        return zi.filename


def unpack(path, dest, depth=0):
    """解包到 dest；返回 (ok, warnings)。嵌套压缩包继续解（最多 3 层）。"""
    os.makedirs(dest, exist_ok=True)
    ext = os.path.splitext(path)[1].lower()
    warnings, ok = [], False
    if ext == '.zip':
        try:
            with zipfile.ZipFile(path) as z:
                for zi in z.infolist():
                    name = _fix_zip_name(zi)
                    if zi.is_dir() or name.endswith('/'):
                        continue
                    target = os.path.normpath(os.path.join(dest, *[p for p in name.replace('\\', '/').split('/') if p not in ('', '.', '..')]))
                    os.makedirs(os.path.dirname(target), exist_ok=True)
                    with z.open(zi) as src, open(target, 'wb') as w:
                        shutil.copyfileobj(src, w, 1 << 20)
            ok = True
        except Exception as e:  # noqa
            warnings.append(f'zip: {e}'[:160])
    elif ext in ('.tgz', '.tar', '.gz'):
        try:
            with tarfile.open(path, 'r:*') as tf:
                tf.extractall(dest)
            ok = True
        except Exception as e:  # noqa
            warnings.append(f'tar: {e}'[:160])
    if not ok:
        for cmd in (['7z', 'x', '-y', f'-o{dest}', path], ['unrar', 'x', '-y', path, dest + '/']):
            if have(cmd[0]):
                r = run(cmd, timeout=1800)
                if r.returncode == 0:
                    ok = True
                    break
                warnings.append(f'{cmd[0]}: ' + (r.stderr or r.stdout)[-200:])
    if ok and depth < 3:
        for dp, _, fns in os.walk(dest):
            for fn in fns:
                if os.path.splitext(fn)[1].lower() in ARCHIVE_EXT and not fn.lower().endswith('.tar.gz'):
                    inner = os.path.join(dp, fn)
                    sub = inner + '.unpacked'
                    if not os.path.exists(sub):
                        ok2, w2 = unpack(inner, sub, depth + 1)
                        warnings += [f'{fn}: {x}' for x in w2]
    return ok, warnings


# ---------------------------------------------------------------- 抽取
def slug(rel, sha):
    base = re.sub(r'[^\w.\-]+', '_', rel.replace('/', '__'))[:120].strip('_')
    return f'{base}__{sha[:8]}'


def extract_one(item, dm):
    rel, local, ext, size, sha = item['path'], item['local'], item['ext'], item['bytes'], item['sha256']
    tmp = tempfile.mkdtemp(prefix='fx_')
    try:
        if ext in dm.IMG_EXT and (not dm.OCR or size < OCR_MIN_KB * 1024):
            # 小图：只做缩略图 + 元数据，不送 OCR
            saved, dm.OCR = dm.OCR, False
            try:
                res, thumb = dm.extract_any({'id': item['id'], 'ext': ext, 'name': os.path.basename(rel)}, local, tmp)
            finally:
                dm.OCR = saved
        else:
            res, thumb = dm.extract_any({'id': item['id'], 'ext': ext, 'name': os.path.basename(rel)}, local, tmp)
        res = res or {}
        text = res.get('text', '') or ''
        out = {'id': item['id'], 'path': rel, 'name': os.path.basename(rel), 'ext': ext, 'bytes': size, 'sha256': sha,
               'source': item['source'], 'method': res.get('method'), 'status': res.get('status', 'meta'),
               'meta': res.get('meta', {}), 'warnings': res.get('warnings', []), 'chars': len(text), 'text': text,
               'blocks': res.get('blocks'), 'pages': res.get('pages'), 'sheets': res.get('sheets'), 'slides': res.get('slides'),
               'members': res.get('members'), 'extracted_at': now()}
        out = {k: v for k, v in out.items() if v is not None}
        if thumb and os.path.exists(thumb):
            out['thumb'] = os.path.relpath(thumb, OUT)
        write_json(os.path.join(OUT, 'text', item['id'] + '.json'), out)
        return {'status': out['status'], 'method': out.get('method'), 'chars': len(text), 'warnings': out['warnings'][:3]}
    except Exception as e:  # noqa
        return {'status': 'fail', 'err': f'{type(e).__name__}: {e}'[:300]}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def coverage(manifest):
    files = manifest['files']
    st = Counter(f['status'] for f in files)
    L = [f'# {TITLE} · 覆盖率报告', '',
         f'- 生成时间：{now()}；来源：' + '；'.join(f'`{s["name"]}` {s["bytes"] / 1e6:.1f} MB（md5 {s.get("md5", "-")}）' for s in manifest['sources']),
         f'- 成员文件 {len(files)} 个（去重前 {manifest.get("members_total", len(files))}）：'
         f'**正文 ok {st.get("ok", 0)} / 仅元数据 meta {st.get("meta", 0)} / 失败 fail {st.get("fail", 0)} / 跳过 skip {st.get("skip", 0)}**',
         f'- 原件备份：' + ('；'.join(f'`{k}` → Release `{v["release"]}` {"✅" if v.get("ok") else "❌"}' for k, v in manifest.get('backup', {}).items()) or '—'),
         '', '## 按类型', '', '| 扩展名 | 个数 | ok | meta | fail | skip | 正文字符 |', '|---|---|---|---|---|---|---|']
    by = defaultdict(Counter)
    ch = Counter()
    for f in files:
        by[f['ext'] or '(无)'][f['status']] += 1
        ch[f['ext'] or '(无)'] += f.get('chars', 0)
    for ext, c in sorted(by.items(), key=lambda x: -sum(x[1].values())):
        L.append(f'| {ext} | {sum(c.values())} | {c.get("ok", 0)} | {c.get("meta", 0)} | {c.get("fail", 0)} | {c.get("skip", 0)} | {ch[ext]:,} |')
    L += ['', '## 文件清单', '', '| 路径 | 大小 | 状态 | 方法 | 字符 | JSON |', '|---|---|---|---|---|---|']
    for f in sorted(files, key=lambda x: x['path']):
        L.append(f'| {f["path"].replace("|", "/")} | {f["bytes"] / 1024:.0f} KB | {f["status"]} | {f.get("method") or ""} | {f.get("chars", 0):,} | `text/{f["id"]}.json` |')
    fails = [f for f in files if f['status'] == 'fail']
    L += ['', f'## 失败（{len(fails)}）', '']
    L += [f'- `{f["path"]}`：{f.get("err", "")}' for f in fails] or ['无。']
    if manifest.get('unpack_warnings'):
        L += ['', '## 解包警告', ''] + [f'- {w}' for w in manifest['unpack_warnings']]
    with open(os.path.join(OUT, '_coverage.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')


def backup(paths, manifest):
    if SOURCE_RELEASE and SOURCE_RELEASE == RELEASE_TAG:
        manifest['backup'] = {name: {'release': RELEASE_TAG, 'ok': True, 'note': '原件本就来自该 Release（上次运行已备份），本次不再上传', 'at': now()} for name, _ in paths}
        log('backup skipped: source is the backup release itself')
        return
    if not BACKUP or not have('gh'):
        return
    r = run(['gh', 'release', 'view', RELEASE_TAG], timeout=120)
    if r.returncode != 0:
        cmd = ['gh', 'release', 'create', RELEASE_TAG, '--latest=false', '--title', f'{TITLE} · 原件', '--notes',
               f'Simon 上传到 Drive 的原始文件备份（{OUT_NAME}）。抽取结果见分支 arena/3f35b9b3-planet 的 data/{OUT_NAME}/。']
        if RELEASE_TARGET:
            cmd += ['--target', RELEASE_TARGET]
        r = run(cmd, timeout=180)
        if r.returncode != 0:
            log('release create failed:', (r.stderr or r.stdout)[-300:])
            return
    bk = manifest.setdefault('backup', {})
    part_max = int(float(os.environ.get('PART_MAX_GB', '1.8')) * 1024 ** 3)  # GitHub 单个 Release 资产上限 2 GiB → 超过就分卷 .partNN（cat 还原）
    for name, p in paths:
        asset = re.sub(r'[^\w.\-]+', '_', name)
        size = os.path.getsize(p)
        if size <= part_max:
            parts = [(asset, p, 0, size)]
        else:
            n = (size + part_max - 1) // part_max
            parts = [(f'{asset}.part{i + 1:02d}', p, i * part_max, min(part_max, size - i * part_max)) for i in range(n)]
        done = []
        for a, src, off, ln in parts:
            if off == 0 and ln == size:
                part_path = src
            else:
                part_path = os.path.join(RAW_DIR, a)
                with open(src, 'rb') as rf, open(part_path, 'wb') as wf:
                    rf.seek(off)
                    left = ln
                    while left > 0:
                        chunk = rf.read(min(1 << 20, left))
                        if not chunk:
                            break
                        wf.write(chunk)
                        left -= len(chunk)
            ok = False
            for attempt in range(3):
                r = run(['gh', 'release', 'upload', RELEASE_TAG, f'{part_path}#{a}', '--clobber'], timeout=7200)
                if r.returncode == 0:
                    ok = True
                    break
                log('upload retry', a, (r.stderr or r.stdout)[-200:])
                time.sleep(10 + attempt * 20)
            done.append({'asset': a, 'bytes': ln, 'sha256': sha256_file(part_path), 'ok': ok})
            if part_path != src:
                os.remove(part_path)
        bk[name] = {'asset': asset, 'bytes': size, 'sha256': sha256_file(p), 'release': RELEASE_TAG, 'ok': all(x['ok'] for x in done), 'parts': done, 'at': now()}
        log('backup', name, bk[name]['ok'], len(done), 'parts')


def main():
    if not OUT_NAME:
        abort(1, 'OUT_NAME is required (→ data/<OUT_NAME>/)')
    log(f'files job: out={OUT} ocr={OCR} workers={WORKERS} tools: ' + ' '.join(f'{c}={"y" if have(c) else "n"}' for c in ('tesseract', 'soffice', 'pdftoppm', '7z', 'gh')))
    os.makedirs(os.path.join(OUT, 'text'), exist_ok=True)
    dm = drive_mod()
    paths = resolve_sources()
    manifest = {'meta': {'out_name': OUT_NAME, 'title': TITLE, 'created': now(), 'ocr': dm.OCR}, 'sources': [], 'files': [], 'unpack_warnings': []}
    # 续跑（2026-10-23）：上次运行的 manifest 里已抽取成功（ok/meta，且 text/<id>.json 还在）的成员直接沿用，不再重抽；FORCE=1 则全部重来。
    prev_done = {}
    mp_prev = os.path.join(OUT, 'manifest.json')
    if os.path.exists(mp_prev) and os.environ.get('FORCE', '0') != '1':
        try:
            prev = json.load(open(mp_prev, encoding='utf-8'))
            for f0 in prev.get('files', []):
                if f0.get('status') in ('ok', 'meta') and os.path.exists(os.path.join(OUT, 'text', f0['id'] + '.json')):
                    prev_done[f0['id']] = f0
            manifest['meta']['resumed_from'] = prev.get('meta', {}).get('checkpoint') or prev.get('meta', {}).get('finished') or '?'
            log(f'resume: {len(prev_done)} members already extracted in previous run')
        except Exception as e:  # noqa
            log('previous manifest unreadable, full run', e)
    for name, p in paths:
        h = hashlib.md5()
        with open(p, 'rb') as f:
            for chunk in iter(lambda: f.read(1 << 22), b''):
                h.update(chunk)
        manifest['sources'].append({'name': name, 'bytes': os.path.getsize(p), 'md5': h.hexdigest(), 'sha256': sha256_file(p)})
    backup(paths, manifest)

    # 解包 / 收集成员
    items, seen = [], {}
    work = os.path.join(RAW_DIR, 'unpacked')
    shutil.rmtree(work, ignore_errors=True)
    for name, p in paths:
        ext = os.path.splitext(name)[1].lower()
        base = re.sub(r'[^\w.\-]+', '_', os.path.splitext(name)[0])
        if ext in ARCHIVE_EXT:
            d = os.path.join(work, base)
            ok, warns = unpack(p, d)
            manifest['unpack_warnings'] += [f'{name}: {w}' for w in warns]
            if not ok:
                abort(3, f'cannot unpack {name}: {warns[-1] if warns else "?"}')
            if not LOCAL_FILES and (SOURCE_RELEASE or (manifest.get('backup') or {}).get(name, {}).get('ok')):
                # 原件已在 Release（本就来自 Release，或刚备份成功）→ 解包后立即删掉本地 zip，省出磁盘（4.36 GB 的 Extra Info 若落在根盘很容易撑满）
                try:
                    os.remove(p)
                    log('freed source archive after unpack:', name, 'free', _free_gb(RAW_DIR), 'GB')
                except Exception as e:  # noqa
                    log('could not remove source archive', e)
            for dp, _, fns in os.walk(d):
                for fn in sorted(fns):
                    fp = os.path.join(dp, fn)
                    rel = os.path.relpath(fp, d).replace('\\', '/')
                    if fn.lower() in SKIP_NAMES or os.path.splitext(fn)[1].lower() in ARCHIVE_EXT and os.path.exists(fp + '.unpacked'):
                        continue
                    items.append({'source': name, 'path': f'{os.path.splitext(name)[0]}/{rel}', 'local': fp})
        else:
            items.append({'source': name, 'path': name, 'local': p})
    manifest['members_total'] = len(items)
    uniq = []
    for it in items:
        it['bytes'] = os.path.getsize(it['local'])
        it['ext'] = os.path.splitext(it['local'])[1].lower()
        it['sha256'] = sha256_file(it['local'])
        it['id'] = slug(it['path'], it['sha256'])
        if it['sha256'] in seen:
            it['dup_of'] = seen[it['sha256']]
            manifest['files'].append({'id': it['id'], 'path': it['path'], 'ext': it['ext'], 'bytes': it['bytes'], 'sha256': it['sha256'],
                                      'status': 'dup', 'same_as': it['dup_of']})
            continue
        seen[it['sha256']] = it['id']
        if it['id'] in prev_done:
            manifest['files'].append(prev_done[it['id']])
            continue
        uniq.append(it)
    log(f'members: {len(items)} ({len(uniq)} unique to extract, {len(prev_done)} reused)')

    # 抽取（每 CHECKPOINT_MIN 分钟提交一次进度：manifest 现状 + _run_status.md 一行，防止无声死亡后一无所有）
    def checkpoint(done_n, final=False):
        manifest['meta']['checkpoint'] = now()
        write_json(os.path.join(OUT, 'manifest.json'), manifest)
        st = Counter(f['status'] for f in manifest['files'])
        line = (f'- {now()} 进度：抽取 {done_n}/{len(uniq)}（ok {st.get("ok", 0)} / meta {st.get("meta", 0)} / fail {st.get("fail", 0)} / dup {st.get("dup", 0)}），'
                f'用时 {(time.time() - T0) / 60:.1f} min，磁盘剩余 RAW {_free_gb(RAW_DIR)} GB / OUT {_free_gb(OUT)} GB\n')
        sp = os.path.join(OUT, '_run_status.md')
        head = f'# {TITLE} · 运行状态\n\n'
        prev = open(sp, encoding='utf-8').read() if os.path.exists(sp) else ''
        if not prev.startswith(head) or '**ABORT' in prev or '**CRASH' in prev or '✅' in prev:
            prev = head + f'- {now()} 本次运行开始（成员 {len(items)}，唯一 {len(uniq)}，来源 {"Release " + SOURCE_RELEASE if SOURCE_RELEASE else "Drive"}，WORKERS={WORKERS}）\n'
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(prev + line)
        if not final:
            git_commit_push(f'files({OUT_NAME}) 进度 {done_n}/{len(uniq)}')

    checkpoint(0)
    last_ck = time.time()
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futs = {pool.submit(extract_one, it, dm): it for it in uniq}
        done = 0
        for fut in futs:
            it = futs[fut]
            r = fut.result()
            rec = {'id': it['id'], 'path': it['path'], 'ext': it['ext'], 'bytes': it['bytes'], 'sha256': it['sha256'], 'source': it['source']}
            rec.update(r)
            manifest['files'].append(rec)
            done += 1
            if done % 25 == 0:
                log(f'extracted {done}/{len(uniq)}')
            if time.time() - last_ck >= CHECKPOINT_MIN * 60:
                checkpoint(done)
                last_ck = time.time()
    manifest['files'].sort(key=lambda x: x['path'])
    manifest['meta']['finished'] = now()
    write_json(os.path.join(OUT, 'manifest.json'), manifest)
    coverage(manifest)
    st = Counter(f['status'] for f in manifest['files'])
    with open(os.path.join(OUT, '_run_status.md'), 'w', encoding='utf-8') as f:
        f.write(f'# {TITLE} · 运行状态\n\n- {now()} ✅ 完成：成员 {len(manifest["files"])}，ok {st.get("ok", 0)} / meta {st.get("meta", 0)} / fail {st.get("fail", 0)} / dup {st.get("dup", 0)}，用时 {(time.time() - T0) / 60:.1f} min\n')
    log('DONE', dict(st))
    git_commit_push(f'files({OUT_NAME}) 入库完成：{len(manifest["files"])} 个成员，正文 {st.get("ok", 0)} / 元数据 {st.get("meta", 0)} / 失败 {st.get("fail", 0)} / 重复 {st.get("dup", 0)}')


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        raise
    except BaseException as e:  # noqa
        import traceback
        tb = traceback.format_exc()[-1500:]
        log('CRASH', tb)
        try:
            os.makedirs(OUT or os.path.join(ROOT, 'data', '_files_job'), exist_ok=True)
            sp = os.path.join(OUT or os.path.join(ROOT, 'data', '_files_job'), '_run_status.md')
            prev = open(sp, encoding='utf-8').read() if os.path.exists(sp) else f'# {TITLE} · 运行状态\n\n'
            with open(sp, 'w', encoding='utf-8') as f:
                f.write(prev + f'- {now()} **CRASH**：{type(e).__name__}: {str(e)[:300]}\n\n```\n{tb}\n```\n')
            git_commit_push(f'files({OUT_NAME}) 崩溃：{type(e).__name__}: {str(e)[:60]}')
        except Exception as e2:  # noqa
            log('crash note failed', e2)
        sys.exit(9)
