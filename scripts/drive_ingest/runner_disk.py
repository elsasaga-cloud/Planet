#!/usr/bin/env python3
"""GitHub 托管运行器的磁盘管理（T29-U19b，2026-10-23）。

背景：《Extra Info.zip》第 5/6 次入库（02:58Z / 03:18Z）都在解包阶段无声死亡，Simon 从 Actions 页拿到的注解是
    System.IO.IOException: No space left on device : '/home/runner/actions-runner/.../_diag/Worker_20261023-031808-utc.log'
即运行器**根盘**写满（托管 ubuntu 运行器根盘只保证 ~14 GB 可用；apt 装 LibreOffice/tesseract 后更少），
4.36 GB 的 zip + 解包（含内层压缩包再解包）+ /tmp 抽取临时文件 就把它填满了；之前的「Actions 停摆 / 配额用尽」判断是错的。

本模块在任务开始时（只在 GITHUB_ACTIONS 下生效，本地/沙箱直接跳过）：
  1. 报告 / 、/mnt 、/tmp 、工作区 的容量（写进 RUNNER_DISK_NOTE 环境变量 → 各任务把它记进 _run_status.md，留证据）；
  2. 删除用不到的预装大件（dotnet / Android SDK / CodeQL / swift / ghcup / PowerShell / chromium / docker 镜像 …，可腾 20–25 GB）；
     不碰 /opt/hostedtoolcache/Python（setup-python 装的解释器就在那里）；
  3. 选剩余容量最大的文件系统作为工作盘：设置 RAW_DIR / ZIP_DIR / TMPDIR（tempfile.mkdtemp、soffice、pdftoppm 的临时文件都跟着走），
     /mnt 若是独立的大盘就用 /mnt，否则用清理后的根盘；
  4. 提供 free_gb() / guard() 给抽取循环做低水位保护。

环境变量：
  RUNNER_DISK_MIN_FREE_GB  根盘剩余低于此值才做清理（默认 40 → 实际上在托管运行器上总会清理）
  RUNNER_DISK_CLEAN=0      关闭清理
  RUNNER_DISK_READY=1      已经处理过（dispatcher 设置，子进程不再重复）
"""
import os
import shutil
import subprocess
import sys
import tempfile
import time

BIG_PREINSTALLED = [
    '/usr/local/lib/android',          # Android SDK ~9–12 GB
    '/opt/hostedtoolcache/CodeQL',     # ~5 GB
    '/usr/share/dotnet',               # ~2 GB
    '/usr/share/swift',                # ~2 GB
    '/usr/local/.ghcup', '/opt/ghc',   # Haskell
    '/usr/local/share/powershell',
    '/usr/local/share/chromium', '/usr/local/share/chromedriver-linux64', '/usr/local/share/edge_driver', '/usr/local/share/gecko_driver',
    '/usr/share/miniconda', '/usr/local/julia1.*', '/usr/lib/google-cloud-sdk', '/usr/local/aws-cli', '/usr/local/aws-sam-cli', '/usr/lib/heroku',
    '/opt/microsoft', '/opt/google/chrome', '/usr/local/share/boost',
]


def log(*a):
    print('[disk]', *a, flush=True)


def free_gb(path):
    try:
        return round(shutil.disk_usage(path).free / 1024 ** 3, 1)
    except Exception:  # noqa
        return -1.0


def total_gb(path):
    try:
        return round(shutil.disk_usage(path).total / 1024 ** 3, 1)
    except Exception:  # noqa
        return -1.0


def _dev(path):
    try:
        return os.stat(path).st_dev
    except Exception:  # noqa
        return None


def df_table(paths):
    seen, rows = set(), []
    for p in paths:
        if not p or not os.path.exists(p):
            continue
        d = _dev(p)
        rows.append(f"{p}: 剩余 {free_gb(p)} / 共 {total_gb(p)} GB" + ('' if d not in seen else '（同一文件系统）'))
        seen.add(d)
    return '；'.join(rows)


def _sudo(cmd, timeout=600):
    full = (['sudo', '-n'] if os.geteuid() != 0 and shutil.which('sudo') else []) + cmd
    try:
        return subprocess.run(full, capture_output=True, text=True, timeout=timeout)
    except Exception as e:  # noqa
        log('cmd failed', cmd[:3], repr(e)[:120])
        return None


def clean_preinstalled():
    """删预装大件，返回腾出的 GB。每条命令独立超时，失败忽略。"""
    before = free_gb('/')
    t0 = time.time()
    import glob
    for pat in BIG_PREINSTALLED:
        for p in glob.glob(pat):
            if os.path.exists(p):
                _sudo(['rm', '-rf', p], timeout=420)
    if shutil.which('docker'):
        _sudo(['docker', 'system', 'prune', '-af', '--volumes'], timeout=240)
    _sudo(['apt-get', 'clean'], timeout=120)
    _sudo(['rm', '-rf', '/var/lib/apt/lists/*'], timeout=60)
    freed = round(free_gb('/') - before, 1)
    log(f'cleaned preinstalled: / {before} → {free_gb("/")} GB (+{freed}) in {time.time() - t0:.0f}s')
    return freed


def _ensure_writable(d):
    try:
        os.makedirs(d, exist_ok=True)
        test = os.path.join(d, '.w')
        open(test, 'w').close()
        os.remove(test)
        return True
    except Exception:  # noqa
        r = _sudo(['mkdir', '-p', d], timeout=30)
        if r is None or r.returncode != 0:
            return False
        _sudo(['chown', '-R', f'{os.getuid()}:{os.getgid()}', d], timeout=120)
        try:
            test = os.path.join(d, '.w')
            open(test, 'w').close()
            os.remove(test)
            return True
        except Exception:  # noqa
            return False


def choose_work_dir(preferred=None):
    """候选：env RAW_DIR 所在目录、/mnt/saga_work、/tmp/saga_work → 取所在文件系统剩余最大的。返回 (work_dir, free_gb)。"""
    cands = []
    if preferred:
        cands.append(os.path.dirname(preferred.rstrip('/')) or '/')
    cands += ['/mnt/saga_work', '/tmp/saga_work', os.path.join(tempfile.gettempdir(), 'saga_work')]
    best, best_free = None, -1
    for c in cands:
        probe = c if os.path.exists(c) else (os.path.dirname(c) or '/')
        f = free_gb(probe)
        if f > best_free + 0.5:          # 容量接近时按候选顺序（优先沿用 env 指定的目录）
            if _ensure_writable(c):
                best, best_free = c, f
    return best, best_free


def prepare(job_label=''):
    """任务入口调用一次。返回说明文字（已放入 os.environ['RUNNER_DISK_NOTE']）。非 Actions 环境返回 ''。"""
    if os.environ.get('RUNNER_DISK_READY') == '1':
        return os.environ.get('RUNNER_DISK_NOTE', '')
    if not os.environ.get('GITHUB_ACTIONS'):
        os.environ['RUNNER_DISK_READY'] = '1'
        return ''
    root = os.environ.get('GITHUB_WORKSPACE') or os.getcwd()
    before = df_table(['/', '/mnt', '/tmp', root])
    log('before:', before)
    freed = 0.0
    min_free = float(os.environ.get('RUNNER_DISK_MIN_FREE_GB', '40'))
    if os.environ.get('RUNNER_DISK_CLEAN', '1') == '1' and free_gb('/') < min_free:
        freed = clean_preinstalled()
    work, wfree = choose_work_dir(os.environ.get('RAW_DIR'))
    note = ''
    if work:
        raw = os.path.join(work, 'raw')
        zipd = os.path.join(work, 'zip')
        tmpd = os.path.join(work, 'tmp')
        for d in (raw, zipd, tmpd):
            os.makedirs(d, exist_ok=True)
        os.environ['RAW_DIR'] = raw
        os.environ['ZIP_DIR'] = zipd
        os.environ['TMPDIR'] = tmpd
        tempfile.tempdir = tmpd
        note = (f'运行器磁盘（{job_label or "job"}）：开始时 {before}；清理预装大件腾出 {freed} GB；'
                f'工作盘 {work}（剩余 {wfree} GB，RAW_DIR/ZIP_DIR/TMPDIR 均指向此处）；清理后 {df_table(["/", "/mnt", root])}')
    else:
        note = f'运行器磁盘（{job_label or "job"}）：开始时 {before}；清理腾出 {freed} GB；未能建立工作目录，沿用 RAW_DIR={os.environ.get("RAW_DIR")}'
    os.environ['RUNNER_DISK_NOTE'] = note
    os.environ['RUNNER_DISK_READY'] = '1'
    log(note)
    return note


class DiskLow(RuntimeError):
    pass


def guard(path, min_gb=1.5, tmp_prefixes=('fx_', 'att_', 'tmp')):
    """低水位保护：剩余 < min_gb 时先清掉 TMPDIR 下 10 分钟没动过的临时目录，再不够就抛 DiskLow（调用方记 skip，不让整个运行器死）。"""
    if free_gb(path) >= min_gb:
        return
    td = tempfile.gettempdir()
    now = time.time()
    try:
        for fn in os.listdir(td):
            p = os.path.join(td, fn)
            if fn.startswith(tmp_prefixes) and os.path.isdir(p) and now - os.path.getmtime(p) > 600:
                shutil.rmtree(p, ignore_errors=True)
    except Exception:  # noqa
        pass
    if free_gb(path) < min_gb:
        raise DiskLow(f'disk low: {path} {free_gb(path)} GB < {min_gb} GB')


if __name__ == '__main__':
    print(df_table(['/', '/mnt', '/tmp', os.getcwd()]))
    print('would clean:', [p for p in BIG_PREINSTALLED if os.path.exists(p)])
    sys.exit(0)
