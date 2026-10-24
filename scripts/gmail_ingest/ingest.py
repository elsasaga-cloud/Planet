#!/usr/bin/env python3
"""T29：Gmail 邮箱（Google Takeout 导出的 .mbox）全量入库。

背景：S / A 两个 Gmail 邮箱接不进 Arena 的 Gmail 连接器，Drive 只有 15 GB 且不可扩容，因此流程固定为
「Takeout 导出 → 上传 Drive（临时「知道链接者可查看」）→ 本脚本在 GitHub Actions 运行器里下载并解析 → 入库 → 删除 Drive 上的导出件」。
本脚本复用 T28 的 workflow（`.github/workflows/drive-smartbyte-ingest.yml`）：在 `scripts/drive_ingest/RUN` 里写
`JOB=gmail` + 参数行并推送，drive_ingest/ingest.py 会把运行转交到这里，不需要再另存新的 workflow。

输入（环境变量，可由 RUN 文件的 KEY=VALUE 行覆盖）：
  ACCOUNT          s | a | e（决定输出目录 data/gmail_<ACCOUNT>/ 与 Release tag gmail-<ACCOUNT>-日期）
  SOURCE_IDS       Drive 文件 ID（逗号分隔）：Takeout 的 .zip / .tgz，或直接是 .mbox
  SOURCE_MD5       可选，与 SOURCE_IDS 一一对应的 Drive md5Checksum（连接器 get_file 可见）；下载后校验，不符则重下一次，再不符即中止
  SOURCE_RELEASE   备选来源：Release tag（Simon 手工把导出件上传到 Release 时用；下载其全部资产）
  LOCAL_FILES      本地测试用：逗号分隔的 zip/mbox 路径
  OWN_EMAILS       本邮箱自己的地址（逗号分隔；默认 <ACCOUNT>.sagatelecom@gmail.com，另会自动从 Sent 标签学习）
  BULK_MODE        headers | full（默认 headers：群发/通知类邮件只留头部 + 600 字摘要；与客户往来或本邮箱回过的线程一律全文）
  ATTACH / ATTACH_MAX_MB / ATTACH_WORKERS / OCR    附件正文抽取（复用 scripts/drive_ingest/ingest.py 的抽取器；默认 1 / 25 / 4 / 0）
  MORE_BATCHES     1 = 本批之后还有后续批次（导出件因 Drive 空间分几次上传时用）：批尾可能被切断的半封邮件存入 state/carry.bin，下一批自动接上
  OCR_MIN_KB       图片附件送 OCR 的最小大小（默认 80；S 邮箱实跑用 8，只跳过图标级小图）
  FORCE            1 = 全部重做（messages/ attachments/ state/ 清空重建；原件备份记录、Release 标签、settings/ 保留，不重传 Release）
  SHARD_MAX_MB     每个 JSONL 分片上限（默认 40，GitHub 单文件 100 MB 硬限）
  COMMIT_EVERY / CHECKPOINT_MIN / MAX_MINUTES      每 N 封 / 每 N 分钟检查点提交（默认 20000 / 15）；总时长上限（默认 330，超时优雅停止，下次续跑）
  GIT_COMMIT / GIT_REF / BACKUP / RELEASE_TAG / RELEASE_TARGET / PART_MAX_GB / RAW_DIR / LIMIT / FORCE   同 drive_ingest

输出 data/gmail_<ACCOUNT>/：
  manifest.json                 进度与状态（来源文件、已处理字节偏移、分片长度、备份、统计）→ 可续跑
  messages/<YYYY>/<YYYY-MM>[_NN].jsonl   每行一封：k, src, off, msgid, thr(X-GM-THRID), date, from/to/cc/bcc, subj, labels, irt, refs,
                                dir(in/out), bulk, keep(full/snippet), body_src, chars, text, quote_at, att[{n,m,b,s,x}], client[SA-…]
                                （att.x 是提交抽取时的状态；附件抽取结果以 attachments/index.json 为准）
  attachments/text/<sha16>.json  附件正文（按 sha256 去重）；attachments/index.json 附件总索引
  threads.json                  线程索引：主题、起止时间、封数、参与者、对方域名、关联客户编号
  contacts.csv                  对方地址索引：姓名、域名、收/发封数、首末日期、最近主题、客户编号
  clients_link.json             按 Saga Clients 编号汇总：封数、最近往来、线程列表（供后续回填档案）
  _coverage.md                  覆盖率报告：按年 / 方向 / 群发 / 标签 / 附件 / 失败 / 备份
原件（Takeout zip 本身）按 ≤1.8 GB 分卷上传到本仓库 Release（私有仓库，不进 Git 历史）。
"""
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import traceback
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from email import policy
from email.parser import BytesParser, BytesHeaderParser
from email.utils import getaddresses, parsedate_to_datetime
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ACCOUNT = (os.environ.get('ACCOUNT') or 's').strip().lower()
OUT = os.environ.get('OUT_DIR') or os.path.join(ROOT, 'data', f'gmail_{ACCOUNT}')
MSG_DIR = os.path.join(OUT, 'messages')
ATT_DIR = os.path.join(OUT, 'attachments')
ATT_TEXT_DIR = os.path.join(ATT_DIR, 'text')
ATT_THUMB_DIR = os.path.join(ATT_DIR, 'thumbs')
sys.path.insert(0, os.path.join(ROOT, 'scripts', 'drive_ingest'))
try:
    import runner_disk  # noqa: E402  T29-U19b：运行器根盘只有 ~14 GB；A 邮箱 mbox 13.4 GB 必须先清理/选大盘
    runner_disk.prepare('gmail_job')
except Exception as _e:  # noqa
    print('[disk] runner_disk skipped:', repr(_e)[:200], flush=True)
DISK_NOTE = os.environ.get('RUNNER_DISK_NOTE', '')
RAW_DIR = os.environ.get('RAW_DIR') or '/tmp/gmail_raw'
SOURCE_IDS = [x.strip() for x in os.environ.get('SOURCE_IDS', '').split(',') if x.strip()]
SOURCE_MD5 = [x.strip().lower() for x in os.environ.get('SOURCE_MD5', '').split(',')]   # 可选：与 SOURCE_IDS 对齐的 Drive md5Checksum，下载后校验
SOURCE_RELEASE = os.environ.get('SOURCE_RELEASE', '').strip()
LOCAL_FILES = [x.strip() for x in os.environ.get('LOCAL_FILES', '').split(',') if x.strip()]
OWN_EMAILS = {x.strip().lower() for x in (os.environ.get('OWN_EMAILS') or f'{ACCOUNT}.sagatelecom@gmail.com').split(',') if x.strip()}
BULK_MODE = os.environ.get('BULK_MODE', 'headers').strip().lower()
SNIPPET = int(os.environ.get('SNIPPET_CHARS', '600'))
ATTACH = os.environ.get('ATTACH', '1') == '1'
ATTACH_MAX = int(float(os.environ.get('ATTACH_MAX_MB', '25')) * 1024 * 1024)
ATTACH_WORKERS = int(os.environ.get('ATTACH_WORKERS', '4'))
OCR = os.environ.get('OCR', '0') == '1'
SHARD_MAX = int(float(os.environ.get('SHARD_MAX_MB', '40')) * 1024 * 1024)
COMMIT_EVERY = int(os.environ.get('COMMIT_EVERY', '20000'))
CHECKPOINT_MIN = float(os.environ.get('CHECKPOINT_MIN', '15'))
MAX_MINUTES = float(os.environ.get('MAX_MINUTES', '330'))
GIT_COMMIT = os.environ.get('GIT_COMMIT', '0') == '1'
GIT_REF = os.environ.get('GIT_REF', '')
BACKUP = os.environ.get('BACKUP', '1') == '1'
RELEASE_TAG = os.environ.get('RELEASE_TAG') or (f'gmail-{ACCOUNT}-' + datetime.now(timezone.utc).strftime('%Y%m%d'))
RELEASE_TARGET = os.environ.get('RELEASE_TARGET', '')
PART_MAX = int(float(os.environ.get('PART_MAX_GB', '1.8')) * 1024 ** 3)
LIMIT = int(os.environ.get('LIMIT', '0'))
FORCE = os.environ.get('FORCE', '0') == '1'
MORE_BATCHES = os.environ.get('MORE_BATCHES', '0') == '1'   # 1 = 导出件分几批上传（Drive 放不下）：本批最后一封可能被切断，先存为 carry，下一批接上
STATE_DIR_NAME = 'state'
MAX_TEXT = int(os.environ.get('MAX_TEXT_CHARS', '400000'))  # 单封正文上限（超长的通常是嵌入 HTML 垃圾）
BLOCK = 8 << 20

T0 = time.time()
T0_ISO = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(T0))
LOCK = threading.Lock()
ENTITIES_PATH = os.path.join(ROOT, 'data', 'saga_clients', 'entities.json')

# Gmail Takeout 的分隔行：From 1234567890@xxx Thu Oct 22 01:55:11 +0000 2026 ；标准 mboxo：From a@b Thu Oct 22 01:55:11 2026
SEP_LINE = re.compile(rb'^From [^\r\n]*\r?\n', re.M)
SEP_RE = re.compile(rb'^From \S+ (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),? (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) '
                    rb'[ 0-3]?\d \d\d:\d\d:\d\d(?: [+-]\d{4})? \d{4}(?: [+-]\d{4})?\r?\n$')
FREEMAIL = {'gmail.com', 'googlemail.com', 'yahoo.com', 'yahoo.co.uk', 'yahoo.fr', 'yahoo.de', 'yahoo.es', 'yahoo.it', 'yahoo.ca',
            'yahoo.com.au', 'yahoo.co.in', 'yahoo.com.br', 'yahoo.com.mx', 'ymail.com', 'rocketmail.com', 'hotmail.com', 'hotmail.co.uk',
            'hotmail.fr', 'hotmail.de', 'hotmail.es', 'hotmail.it', 'outlook.com', 'outlook.es', 'outlook.fr', 'outlook.de', 'live.com',
            'live.co.uk', 'live.fr', 'msn.com', 'aol.com', 'icloud.com', 'me.com', 'mac.com', 'protonmail.com', 'proton.me', 'pm.me',
            'gmx.com', 'gmx.de', 'gmx.net', 'gmx.at', 'web.de', 'mail.com', 'mail.ru', 'yandex.ru', 'yandex.com', 'bk.ru', 'list.ru',
            'inbox.ru', 'rambler.ru', 'ukr.net', '163.com', '126.com', 'qq.com', 'foxmail.com', 'sina.com', 'sohu.com', '139.com',
            'yeah.net', 'aliyun.com', 'naver.com', 'daum.net', 'hanmail.net', 'rediffmail.com', 'zoho.com', 'zohomail.com', 'seznam.cz',
            'wp.pl', 'o2.pl', 'onet.pl', 'interia.pl', 'libero.it', 'virgilio.it', 'orange.fr', 'wanadoo.fr', 'free.fr', 'laposte.net',
            'sfr.fr', 'bluewin.ch', 't-online.de', 'freenet.de', 'telenet.be', 'skynet.be', 'ziggo.nl', 'kpnmail.nl', 'btinternet.com',
            'sky.com', 'bigpond.com', 'optusnet.com.au', 'xtra.co.nz', 'shaw.ca', 'rogers.com', 'sympatico.ca', 'bellsouth.net',
            'comcast.net', 'verizon.net', 'att.net', 'sbcglobal.net', 'cox.net', 'charter.net', 'earthlink.net', 'terra.com.br',
            'uol.com.br', 'bol.com.br', 'hotmail.com.br', 'prodigy.net.mx', 'abv.bg', 'mail.bg', 'walla.co.il', 'yahoo.co.jp',
            'mail.ee', 'inbox.lv', 'centrum.cz', 'email.cz', 'azet.sk', 'citromail.hu', 'freemail.hu', 'eim.ae', 'emirates.net.ae'}
DOC_EXT = {'.docx', '.doc', '.xlsx', '.xlsm', '.xls', '.csv', '.pdf', '.pptx', '.ppt', '.txt', '.rtf', '.odt', '.md', '.xml', '.json',
           '.zip', '.rar', '.7z', '.dxf', '.xmind', '.pub', '.log', '.mib', '.wps',
           '.vsd', '.vsdx', '.vdx', '.cdr', '.ai', '.eps', '.psd',            # 图形/排版源文件：soffice→pdf / PDF 内核 / PSD 合成图
           '.mp4', '.mov', '.avi', '.mkv', '.wmv'}                           # 视频：ffprobe 元数据 + 抽帧缩略图
IMG_EXT = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tif', '.tiff', '.heic', '.heif'}
OCR_MIN_KB = float(os.environ.get('OCR_MIN_KB', '80'))   # 小于此大小的图片附件不送 OCR（邮件里多是签名 logo / 图标）
BULK_LABELS = {'Category Promotions', 'Category Social', 'Category Forums', 'Category Updates', 'Spam'}
BULK_LOCAL = re.compile(r'^(no-?reply|do-?not-?reply|notifications?|notify|newsletter|news|mailer-daemon|postmaster|bounce|alerts?|'
                        r'info-?noreply|support-?noreply|marketing|promo|updates?|digest|hello|team|billing|invoice|receipts?|'
                        r'account|security|feedback|survey|system|robot|bot|auto)(?:[-_.+]|$)', re.I)
QUOTE_MARKERS = [re.compile(p, re.I | re.M) for p in (
    r'^On .{5,200}? wrote:\s*$', r'^-{2,}\s*Original Message\s*-{2,}', r'^-{2,}\s*Forwarded message\s*-{2,}',
    r'^From:\s.+\n(?:Sent|Date):\s.+', r'^发件人[:：]', r'^在 .{4,60}? 写道[:：]', r'^Le .{5,120}? a écrit\s*:', r'^Am .{5,120}? schrieb .{0,60}:',
    r'^El .{5,120}? escribió:', r'^Il .{5,120}? ha scritto:', r'^Em .{5,120}? escreveu:', r'^\d{1,2}\.\d{1,2}\.\d{4} .{0,60} написал', r'^_{10,}\s*$')]


def log(*a):
    print(f'[{time.time() - T0:7.1f}s]', *a, flush=True)


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def have(cmd):
    from shutil import which
    return which(cmd) is not None


def run(cmd, timeout=600, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, **kw)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


# ---------------------------------------------------------------- 复用 drive_ingest 的抽取器
_DRIVE = None


def drive_mod():
    global _DRIVE
    if _DRIVE is None:
        p = os.path.join(ROOT, 'scripts', 'drive_ingest', 'ingest.py')
        spec = importlib.util.spec_from_file_location('drive_ingest_mod', p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        m.THUMB_DIR = ATT_THUMB_DIR          # 图片附件缩略图落到 gmail 目录
        m.OCR = have('tesseract')            # 无文字层 PDF 一律 OCR；图片是否送 OCR 由本脚本自己把关
        _DRIVE = m
    return _DRIVE


# ---------------------------------------------------------------- HTML → 文本
class _H2T(HTMLParser):
    BLOCK = {'p', 'div', 'br', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'ul', 'ol', 'blockquote', 'pre', 'hr',
             'section', 'article', 'header', 'footer', 'title', 'option', 'dd', 'dt'}
    SKIP = {'script', 'style', 'head', 'noscript', 'template'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
        self.href = None

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in self.BLOCK:
            self.out.append('\n')
        elif tag in ('td', 'th'):
            self.out.append('\t')
        elif tag == 'a':
            d = dict(attrs)
            h = d.get('href') or ''
            self.href = h if h.startswith(('http://', 'https://')) and not h.startswith('https://www.google.com/url') else None
        elif tag == 'img':
            d = dict(attrs)
            alt = (d.get('alt') or '').strip()
            if alt:
                self.out.append(f'[图:{alt}]')

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag in self.BLOCK:
            self.out.append('\n')
        elif tag == 'a' and self.href:
            txt = ''.join(self.out[-3:])
            if self.href not in txt:
                self.out.append(f' <{self.href}>')
            self.href = None

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)

    def text(self):
        t = ''.join(self.out)
        t = re.sub(r'[ \t\xa0]+', ' ', t)
        t = re.sub(r' *\n *', '\n', t)
        t = re.sub(r'\n{3,}', '\n\n', t)
        return t.strip()


def html_to_text(html):
    p = _H2T()
    try:
        p.feed(html)
        p.close()
    except Exception:  # noqa
        return re.sub(r'<[^>]+>', ' ', html)
    return p.text()


# ---------------------------------------------------------------- 字节流链（多个 zip / mbox 拼成一条流）
class Chain:
    """把多个来源（zip 内 .mbox 条目 / 裸 .mbox / tgz 解出的 .mbox）按顺序接成一条可 read(n) 的字节流。"""

    def __init__(self, openers):
        self.openers = openers  # [(label, callable→binary stream)]
        self.i = -1
        self.cur = None
        self.pos = 0  # 绝对偏移

    def _next(self):
        if self.cur is not None:
            try:
                self.cur.close()
            except Exception:  # noqa
                pass
        self.i += 1
        if self.i >= len(self.openers):
            self.cur = None
            return False
        self.cur = self.openers[self.i][1]()
        return True

    def read(self, n):
        out = b''
        while len(out) < n:
            if self.cur is None and not self._next():
                break
            b = self.cur.read(n - len(out))
            if not b:
                if not self._next():
                    break
                continue
            out += b
        self.pos += len(out)
        return out

    def skip_to(self, offset):
        while self.pos < offset:
            b = self.read(min(BLOCK, offset - self.pos))
            if not b:
                break

    def label(self):
        return self.openers[self.i][0] if 0 <= self.i < len(self.openers) else ''


def iter_messages(chain, start_offset=0, tail_sink=None):
    """按 mbox 分隔行切分，产出 (分隔行偏移, 正文起始偏移, 消息字节)。分隔行本身不计入消息；
    正文起始偏移 + len(消息字节) == 下一条分隔行的偏移（用于续跑）。
    tail_sink 不为 None 时，流末尾的最后一封（可能被分批切断）不产出，而是以 (sep_line, bytes) 放进 tail_sink。"""
    if start_offset:
        chain.skip_to(start_offset)
    carry = b''
    base = chain.pos          # proc[0] 的绝对偏移
    parts = []
    sep_off = None            # 当前消息分隔行偏移
    body_off = None           # 当前消息正文起始偏移
    sep_line = b''
    while True:
        data = chain.read(BLOCK)
        if not data:
            break
        data = carry + data
        cut = data.rfind(b'\n')
        if cut == -1:
            carry = data
            continue
        proc, carry = data[:cut + 1], data[cut + 1:]
        last = 0
        for m in SEP_LINE.finditer(proc):
            if not SEP_RE.match(m.group(0)):
                continue
            if sep_off is not None:
                parts.append(proc[last:m.start()])
                yield sep_off, body_off, b''.join(parts)
                parts = []
            sep_off = base + m.start()
            body_off = base + m.end()
            sep_line = m.group(0)
            last = m.end()
        if sep_off is None:
            # 流不是从分隔行开始（分卷切断 / 续跑偏移落在消息中间）：残片作为「无头消息」累积
            if proc[last:].strip() or parts:
                if not parts:
                    sep_off = body_off = base + last
                    parts.append(proc[last:])
                else:
                    parts.append(proc[last:])
        else:
            parts.append(proc[last:])
        base += len(proc)
    tail = b''.join(parts) + carry
    if tail.strip():
        if sep_off is None:
            sep_off = body_off = base
            sep_line = b''
        if tail_sink is not None:
            tail_sink.append((sep_line, tail, sep_off))
        else:
            yield sep_off, body_off, tail


# ---------------------------------------------------------------- 来源：下载 / 展开
def abort(code, why):
    """中止前把原因写进 OUT/_run_status.md 并提交（代理读不到 Actions 日志，只能看分支提交）。"""
    log('ABORT:', why)
    try:
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, '_run_status.md'), 'w', encoding='utf-8') as f:
            f.write(f'# Gmail({ACCOUNT}) 入库运行状态\n\n- {now()} **ABORT（exit {code}）**：{why}\n' + (f'- {DISK_NOTE}\n' if DISK_NOTE else ''))
        git_commit_push(f'T29: Gmail({ACCOUNT}) 入库中止：{why[:80]}')
    except Exception as e:  # noqa
        log('abort note failed', e)
    sys.exit(code)


def resolve_sources():
    """返回 [(label, path)]：本地 zip/tgz/mbox 文件列表（已下载）。"""
    os.makedirs(RAW_DIR, exist_ok=True)
    paths = []
    if LOCAL_FILES:
        paths = [(os.path.basename(p), p) for p in LOCAL_FILES]
    elif SOURCE_RELEASE:
        d = os.path.join(RAW_DIR, 'release')
        os.makedirs(d, exist_ok=True)
        r = run(['gh', 'release', 'download', SOURCE_RELEASE, '-D', d, '--clobber'], timeout=7200)
        if r.returncode != 0:
            abort(3, 'release download failed: ' + (r.stderr or r.stdout)[-300:])
        # 分卷 .partNN 不再合并（合并要双倍磁盘）：分卷是原件的裸字节切片，按名字顺序交给 Chain 接成一条流即可，
        # 与原件逐字节相同；zip/tgz 原件若被分卷则仍需合并（zipfile 要随机读）。
        parts = defaultdict(list)
        for fn in sorted(os.listdir(d)):
            m = re.fullmatch(r'(.+)\.part(\d+)', fn)
            if m:
                parts[m.group(1)].append(fn)
        for base, fns in parts.items():
            if base.lower().endswith('.mbox'):
                continue
            with open(os.path.join(d, base), 'wb') as w:
                for fn in sorted(fns, key=natural_key):
                    with open(os.path.join(d, fn), 'rb') as rf:
                        for chunk in iter(lambda: rf.read(1 << 20), b''):
                            w.write(chunk)
                    os.remove(os.path.join(d, fn))
        paths = [(fn, os.path.join(d, fn)) for fn in sorted(os.listdir(d), key=natural_key)]
    elif SOURCE_IDS:
        dm = drive_mod()
        import requests
        for i, fid in enumerate(SOURCE_IDS):
            name = fid
            expect = 0
            want_md5 = SOURCE_MD5[i] if i < len(SOURCE_MD5) and re.fullmatch(r'[0-9a-f]{32}', SOURCE_MD5[i] or '') else ''
            try:  # 先探一下文件名（Content-Disposition）和大小（Content-Length）
                with requests.get(dm.DL_URL.format(id=fid), stream=True, timeout=(15, 60), headers={'User-Agent': 'Mozilla/5.0'}) as r:
                    cd = r.headers.get('Content-Disposition', '')
                    m = re.search(r"filename\*=UTF-8''([^;]+)", cd) or re.search(r'filename="?([^";]+)"?', cd)
                    if m:
                        from urllib.parse import unquote
                        name = unquote(m.group(1))
                    if 'text/html' not in r.headers.get('Content-Type', ''):
                        expect = int(r.headers.get('Content-Length') or 0)
                    if 'text/html' in r.headers.get('Content-Type', ''):
                        body = r.content[:6000].decode('utf-8', 'ignore')
                        if 'ServiceLogin' in body or 'accounts.google.com' in body or 'Request access' in body:
                            abort(2, f'{fid} 未共享（返回登录页）；请把导出件设为「知道链接的任何人可查看」后重跑')
            except SystemExit:
                raise
            except Exception as e:  # noqa
                log('probe failed', fid, e)
            ext = os.path.splitext(name)[1].lower() or '.zip'
            dest = os.path.join(RAW_DIR, re.sub(r'[^\w.\-]+', '_', name) if name != fid else f'{fid}{ext}')
            ptag = dm.partial_tag(f'gmail-{ACCOUNT}')      # 跨次运行续传暂存（2026-10-23：12 GB mbox 被配额锁打断后不再整段白下）
            resumed = 0
            for attempt in (1, 2):
                if os.path.exists(dest) and os.path.getsize(dest) > 0 and (not expect or os.path.getsize(dest) == expect):
                    log('reuse downloaded' if attempt == 1 else 'downloaded', dest, os.path.getsize(dest), 'bytes')
                else:
                    if attempt == 1:
                        err, expect, resumed, note = dm.fetch_with_resume(dm.download, fid, dest, expect, name, ext, ptag, log_fn=log)
                    else:   # 第二次：校验失败后从零重下
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
                    log(f'md5 {dest}: {h.hexdigest()} {"== " if ok else "!= "}{want_md5}')
                if ok:
                    if resumed:
                        dm.partial_cleanup(fid, ptag)
                    break
                log(f'VERIFY FAILED (attempt {attempt}): {dest} size {got} expect {expect}')
                if attempt == 2:
                    abort(3, f'download verify failed twice: {dest} size {got} expect {expect} md5 {want_md5 or "-"}')
                if resumed:          # 拼回的部分可能已坏：丢掉暂存，第二次从零下
                    dm.partial_cleanup(fid, ptag)
                os.remove(dest)
            paths.append((os.path.basename(dest), dest))
    else:
        log('no source: set SOURCE_IDS / SOURCE_RELEASE / LOCAL_FILES')
        sys.exit(1)
    for label, p in paths:
        log(f'source {label}: {os.path.getsize(p) / 1e6:.1f} MB')
    return paths


def mbox_openers(paths):
    """展开来源为 mbox 条目 openers（按文件名排序以保证分卷顺序）。"""
    openers = []
    for label, p in paths:
        low = p.lower()
        if low.endswith('.zip'):
            zf = zipfile.ZipFile(p)
            names = sorted(n for n in zf.namelist() if n.lower().endswith('.mbox'))
            if not names:
                log('WARN: no .mbox in', p, '→ entries:', zf.namelist()[:10])
            for n in names:
                openers.append((f'{label}!{n}', (lambda zf=zf, n=n: zf.open(n)), zf.getinfo(n).file_size))
            keep_side_files(label, [(zi.filename, zi.file_size, (lambda zi=zi: zf.open(zi))) for zi in zf.infolist() if not zi.is_dir()])
        elif low.endswith(('.tgz', '.tar.gz', '.tar')):
            d = os.path.join(RAW_DIR, 'untar_' + re.sub(r'\W+', '_', label))
            os.makedirs(d, exist_ok=True)
            with tarfile.open(p, 'r:*') as tf:
                for ti in tf:
                    if ti.isfile() and not ti.name.lower().endswith('.mbox') and ti.size <= 4 << 20:
                        keep_side_files(label, [(ti.name, ti.size, (lambda tf=tf, ti=ti: tf.extractfile(ti)))])
                    if ti.isfile() and ti.name.lower().endswith('.mbox'):
                        out = os.path.join(d, os.path.basename(ti.name))
                        if not os.path.exists(out) or os.path.getsize(out) != ti.size:
                            with tf.extractfile(ti) as src, open(out, 'wb') as w:
                                for chunk in iter(lambda: src.read(1 << 20), b''):
                                    w.write(chunk)
                        openers.append((f'{label}!{ti.name}', (lambda out=out: open(out, 'rb')), ti.size))
        else:  # 裸 mbox
            openers.append((label, (lambda p=p: open(p, 'rb')), os.path.getsize(p)))
    # 同一导出的多卷 zip 按名字排序后，其中的 mbox 条目也按名字排好；跨卷切断由 Chain 自然接上
    openers.sort(key=lambda x: natural_key(x[0]))
    return openers


def natural_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]


def keep_side_files(label, entries):
    """Takeout 里 .mbox 之外的小文件（User Settings/*.json：签名、自动回复、屏蔽地址、过滤器；archive_browser.html 除外）
    原样存到 OUT/settings/ ——「只要是信息都入库」。"""
    d = os.path.join(OUT, 'settings')
    for name, size, opener in entries:
        low = name.lower()
        if low.endswith('.mbox') or size > 4 << 20 or os.path.basename(low) in ('archive_browser.html',):
            continue
        rel = re.sub(r'^takeout/', '', name, flags=re.I)
        dest = os.path.join(d, re.sub(r'[^\w.\-/ ]+', '_', rel))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        try:
            with opener() as src, open(dest, 'wb') as w:
                w.write(src.read())
            log(f'side file kept: {label}!{name} → {os.path.relpath(dest, OUT)} ({size} B)')
        except Exception as e:  # noqa
            log('side file failed', name, e)


# ---------------------------------------------------------------- 客户关联
class Clients:
    def __init__(self):
        self.by_email = {}
        self.by_domain = {}
        self.grade = {}
        self.name = {}
        if not os.path.exists(ENTITIES_PATH):
            return
        try:
            ents = json.load(open(ENTITIES_PATH, encoding='utf-8'))
        except Exception as e:  # noqa
            log('entities load failed', e)
            return
        for e in ents:
            code = e.get('code')
            if not code:
                continue
            self.grade[code] = e.get('grade', '')
            self.name[code] = e.get('name', '')
            for em in e.get('emails', []) or []:
                em = (em or '').strip().lower()
                if em and '@' in em:
                    self.by_email.setdefault(em, code)
            for d in e.get('domains', []) or []:
                d = (d or '').strip().lower().lstrip('@')
                if d and d not in FREEMAIL and '.' in d:
                    self.by_domain.setdefault(d, code)
        log(f'clients: {len(self.by_email)} emails / {len(self.by_domain)} domains from entities.json')

    def match(self, email):
        email = (email or '').lower()
        if not email or '@' not in email:
            return None
        c = self.by_email.get(email)
        if c:
            return c
        dom = email.rsplit('@', 1)[1]
        if dom in FREEMAIL:
            return None
        c = self.by_domain.get(dom)
        if c:
            return c
        # 子域名 → 主域
        parts = dom.split('.')
        for i in range(1, len(parts) - 1):
            c = self.by_domain.get('.'.join(parts[i:]))
            if c:
                return c
        return None


# ---------------------------------------------------------------- 邮件解析
def addr_list(msg, *names):
    vals = []
    for n in names:
        try:
            vals.extend(msg.get_all(n, []) or [])
        except Exception:  # noqa
            pass
    out = []
    try:
        pairs = getaddresses([str(v) for v in vals])
    except Exception:  # noqa
        pairs = []
    for n, e in pairs:
        e = (e or '').strip().lower()
        if not e or '@' not in e:
            continue
        out.append({'n': (n or '').strip().strip('"')[:120], 'e': e[:200]})
    return out


def hdr(msg, name, default=''):
    try:
        v = msg.get(name)
        return str(v) if v is not None else default
    except Exception:  # noqa
        try:
            raw = msg.get_all(name)
            return str(raw[0]) if raw else default
        except Exception:  # noqa
            return default


def parse_date(msg, sep_line=b''):
    for cand in (hdr(msg, 'Date'),):
        if cand:
            try:
                d = parsedate_to_datetime(cand)
                if d.tzinfo is None:
                    d = d.replace(tzinfo=timezone.utc)
                return d.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), cand
            except Exception:  # noqa
                pass
    for cand in (hdr(msg, 'Received').split(';')[-1].strip() if hdr(msg, 'Received') else '',):
        if cand:
            try:
                d = parsedate_to_datetime(cand)
                if d.tzinfo is None:
                    d = d.replace(tzinfo=timezone.utc)
                return d.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), cand
            except Exception:  # noqa
                pass
    return '', hdr(msg, 'Date')


def decode_part_text(part):
    """text/* part → str（字符集容错）。"""
    payload = part.get_payload(decode=True)
    if payload is None:
        try:
            return str(part.get_content())
        except Exception:  # noqa
            return ''
    cs = (part.get_content_charset() or '').lower().replace('_', '-')
    tried = []
    for enc in (cs, 'utf-8', 'gb18030', 'cp1252', 'latin-1'):
        if not enc or enc in tried:
            continue
        tried.append(enc)
        try:
            return payload.decode(enc)
        except Exception:  # noqa
            continue
    return payload.decode('utf-8', 'replace')


def quote_index(text):
    best = None
    for rx in QUOTE_MARKERS:
        m = rx.search(text)
        if m and (best is None or m.start() < best):
            best = m.start()
    if best is None:
        m = re.search(r'^>', text, re.M)
        if m:
            best = m.start()
    return best


def filename_of(part):
    try:
        fn = part.get_filename()
    except Exception:  # noqa
        fn = None
    if not fn:
        try:
            fn = part.get_param('name')
        except Exception:  # noqa
            fn = None
    return (fn or '').strip()[:200]


def walk_body(msg, texts, htmls, atts, depth=0):
    """收集正文（plain/html）与附件 part。"""
    if depth > 12:
        return
    try:
        ctype = msg.get_content_type()
    except Exception:  # noqa
        ctype = 'application/octet-stream'
    if msg.is_multipart():
        subtype = ctype.split('/')[-1]
        parts = msg.get_payload() or []
        if subtype == 'alternative':
            # 分别收集；最终 plain 优先、html 兜底
            for p in parts:
                walk_body(p, texts, htmls, atts, depth + 1)
        else:
            for p in parts:
                walk_body(p, texts, htmls, atts, depth + 1)
        return
    fn = filename_of(msg)
    try:
        disp = (msg.get_content_disposition() or '').lower()
    except Exception:  # noqa
        disp = ''
    if ctype == 'message/rfc822':
        inner = msg.get_payload()
        if isinstance(inner, list) and inner:
            texts.append('\n[转发/附带邮件]\n')
            walk_body(inner[0], texts, htmls, atts, depth + 1)
        return
    if ctype.startswith('text/') and not fn and disp != 'attachment':
        if ctype == 'text/plain':
            texts.append(decode_part_text(msg))
        elif ctype == 'text/html':
            htmls.append(decode_part_text(msg))
        elif ctype == 'text/calendar':
            texts.append('[日历邀请]\n' + decode_part_text(msg)[:2000])
        return
    atts.append((fn or f'(unnamed {ctype})', ctype, msg))


# ---------------------------------------------------------------- 附件抽取（线程池）
class AttachStore:
    def __init__(self, manifest):
        self.index = {}
        p = os.path.join(ATT_DIR, 'index.json')
        if os.path.exists(p):
            try:
                self.index = json.load(open(p, encoding='utf-8'))
            except Exception:  # noqa
                self.index = {}
        self.pool = ThreadPoolExecutor(max_workers=ATTACH_WORKERS) if ATTACH else None
        self.futures = []
        self.lock = threading.Lock()
        self.manifest = manifest

    def submit(self, sha16, name, ctype, data, mkey, extract=True):
        with self.lock:
            rec = self.index.get(sha16)
            if rec:
                rec['n'] = rec.get('n', 0) + 1
                if name and name not in rec.get('names', []) and len(rec.get('names', [])) < 8:
                    rec.setdefault('names', []).append(name)
                if rec.get('x', '').startswith('skip:snippet') and extract:
                    pass  # 之前只在摘要邮件里见过，这次在全文邮件里出现 → 补抽
                else:
                    return rec.get('x', 'pending')
            else:
                rec = {'name': name, 'names': [name], 'mime': ctype, 'bytes': len(data), 'n': 1, 'first_msg': mkey, 'x': 'skip'}
                self.index[sha16] = rec
            ext = os.path.splitext(name)[1].lower()
        if not extract:
            rec['x'] = 'skip:snippet'
            return rec['x']
        if not ATTACH:
            rec['x'] = 'skip:off'
            return rec['x']
        if len(data) > ATTACH_MAX:
            rec['x'] = 'skip:too_big'
            return rec['x']
        if ext in IMG_EXT:
            if not OCR or len(data) < OCR_MIN_KB * 1024:
                rec['x'] = 'skip:image'
                return rec['x']
        elif ext not in DOC_EXT:
            rec['x'] = 'skip:type'
            return rec['x']
        rec['x'] = 'pending'
        self.futures.append(self.pool.submit(self._extract, sha16, name, ext, data))
        return 'pending'

    def _extract(self, sha16, name, ext, data):
        rec = self.index[sha16]
        tmpd = tempfile.mkdtemp(prefix='att_')
        try:
            local = os.path.join(tmpd, re.sub(r'[^\w.\-]+', '_', name) or ('att' + ext))
            with open(local, 'wb') as f:
                f.write(data)
            dm = drive_mod()
            thumb = os.path.join(ATT_THUMB_DIR, sha16 + '.jpg')
            os.makedirs(ATT_THUMB_DIR, exist_ok=True)
            res, thumb_path = dm.extract_any({'id': sha16, 'ext': ext, 'name': name}, local, tmpd)
            if ext in IMG_EXT and os.path.exists(thumb) and (res or {}).get('status') != 'ok':
                try:
                    os.remove(thumb)  # 没文字的图片不留缩略图（邮件里多是 logo/签名）
                except Exception:  # noqa
                    pass
            text = (res or {}).get('text', '') or ''
            if len(text) > MAX_TEXT:
                text = text[:MAX_TEXT] + f'\n…[截断，共 {len(text)} 字]'
            out = {'sha256_16': sha16, 'name': name, 'ext': ext, 'bytes': len(data), 'method': (res or {}).get('method'),
                   'status': (res or {}).get('status', 'meta'), 'meta': (res or {}).get('meta', {}),
                   'warnings': (res or {}).get('warnings', []), 'chars': len(text), 'text': text,
                   'blocks': (res or {}).get('blocks'), 'pages': (res or {}).get('pages'), 'sheets': (res or {}).get('sheets'),
                   'extracted_at': now()}
            out = {k: v for k, v in out.items() if v is not None}
            write_json(os.path.join(ATT_TEXT_DIR, sha16 + '.json'), out)
            with self.lock:
                rec['x'] = out['status']
                rec['chars'] = len(text)
                rec['method'] = out.get('method')
        except Exception as e:  # noqa
            with self.lock:
                rec['x'] = 'fail'
                rec['err'] = f'{type(e).__name__}: {e}'[:300]
        finally:
            try:
                import shutil
                shutil.rmtree(tmpd, ignore_errors=True)
            except Exception:  # noqa
                pass

    def drain(self, max_pending=400):
        """避免积压占内存：待处理超过阈值时等一等。"""
        if len(self.futures) > max_pending:
            for f in self.futures[:len(self.futures) - max_pending // 2]:
                f.result()
            self.futures = [f for f in self.futures if not f.done()]

    def wait_all(self):
        for f in self.futures:
            try:
                f.result()
            except Exception:  # noqa
                pass
        self.futures = []

    def finish(self):
        self.wait_all()
        if self.pool:
            self.pool.shutdown(wait=True)
            self.pool = None

    def save(self):
        with self.lock:
            write_json(os.path.join(ATT_DIR, 'index.json'), self.index)


# ---------------------------------------------------------------- 分片写入
class Shards:
    def __init__(self, manifest):
        self.manifest = manifest
        self.manifest.setdefault('shards', {})  # rel → bytes（检查点时的长度；续跑按此截断）
        self.handles = {}
        self.sizes = {}
        os.makedirs(MSG_DIR, exist_ok=True)
        # 续跑：把分片截断到上次检查点记录的长度；未登记的分片文件删除
        known = set(self.manifest['shards'])
        for dp, _, fns in os.walk(MSG_DIR):
            for fn in fns:
                rel = os.path.relpath(os.path.join(dp, fn), OUT)
                if rel not in known:
                    os.remove(os.path.join(dp, fn))
        for rel, n in list(self.manifest['shards'].items()):
            p = os.path.join(OUT, rel)
            if not os.path.exists(p):
                del self.manifest['shards'][rel]
                continue
            if os.path.getsize(p) > n:
                with open(p, 'r+b') as f:
                    f.truncate(n)
            self.sizes[rel] = n

    def _pick(self, ym):
        year = ym[:4]
        i = 1
        while True:
            rel = os.path.join('messages', year, f'{ym}.jsonl' if i == 1 else f'{ym}_{i:02d}.jsonl')
            if self.sizes.get(rel, 0) < SHARD_MAX:
                return rel
            i += 1

    def write(self, rec):
        ym = (rec.get('date') or '')[:7] or 'unknown'
        if ym == 'unknown':
            ym = '0000-00'
        rel = self._pick(ym)
        h = self.handles.get(rel)
        if h is None:
            p = os.path.join(OUT, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            h = self.handles[rel] = open(p, 'ab')
        line = (json.dumps(rec, ensure_ascii=False, separators=(',', ':')) + '\n').encode('utf-8')
        h.write(line)
        self.sizes[rel] = self.sizes.get(rel, 0) + len(line)

    def checkpoint(self):
        for h in self.handles.values():
            h.flush()
        self.manifest['shards'] = dict(self.sizes)

    def verify(self, when=''):
        """磁盘分片长度必须等于已记录长度；短了 = 被 git 重写过且句柄失效（10-24 事故），立即报错中止而不是静默丢数据。"""
        bad = []
        for rel, n in self.sizes.items():
            p = os.path.join(OUT, rel)
            d = os.path.getsize(p) if os.path.exists(p) else -1
            if d != n:
                bad.append((rel, n, d))
        if bad:
            log('SHARD MISMATCH', when, bad[:10])
            abort(6, f'shard size mismatch {when}: {bad[:3]}')

    def close(self):
        for h in self.handles.values():
            h.close()
        self.handles = {}


# ---------------------------------------------------------------- Git / Release
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


def gh_release_ensure():
    r = run(['gh', 'release', 'view', RELEASE_TAG], timeout=120)
    if r.returncode == 0:
        return True
    cmd = ['gh', 'release', 'create', RELEASE_TAG, '--latest=false', '--title', f'Gmail（{ACCOUNT} 邮箱）Takeout 原件备份 {RELEASE_TAG[-8:]}',
           '--notes', f'T29：{ACCOUNT}.sagatelecom Gmail 的 Google Takeout 导出原件（.mbox 压缩包，≤1.8 GB 分卷 .partNN，按名字顺序 cat 即可还原）。'
                      f'解析出的邮件 JSONL / 附件正文 / 线程与联系人索引见分支 arena/3f35b9b3-planet 的 data/gmail_{ACCOUNT}/。']
    if RELEASE_TARGET:
        cmd += ['--target', RELEASE_TARGET]
    r = run(cmd, timeout=180)
    if r.returncode != 0:
        log('release create failed:', (r.stderr or r.stdout)[-300:])
        return False
    return True


def backup_sources(paths, manifest):
    """把导出原件（zip/tgz/mbox）按 ≤PART_MAX 分卷上传到 Release；已完成的跳过。"""
    if not BACKUP:
        return
    if LOCAL_FILES and not os.environ.get('FORCE_BACKUP'):
        log('backup skipped (LOCAL_FILES)')
        return
    if SOURCE_RELEASE and not os.environ.get('FORCE_BACKUP'):
        log('backup skipped (source is the Release itself)')
        return
    if not have('gh') or not gh_release_ensure():
        log('backup unavailable (no gh / release)')
        return
    bk = manifest.setdefault('backup', {})
    for label, p in paths:
        key = os.path.basename(p)
        if bk.get(key, {}).get('done') and not os.environ.get('FORCE_BACKUP'):
            continue
        size = os.path.getsize(p)
        whole = sha256_file(p)
        parts = []
        if size <= PART_MAX:
            parts.append((key, p, 0, size))
        else:
            n = (size + PART_MAX - 1) // PART_MAX
            for i in range(n):
                parts.append((f'{key}.part{i + 1:02d}', p, i * PART_MAX, min(PART_MAX, size - i * PART_MAX)))
        done_parts = []
        for asset, src, off, ln in parts:
            if off == 0 and ln == size:
                part_path = src
            else:
                part_path = os.path.join(RAW_DIR, asset)
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
            for attempt in range(4):
                r = run(['gh', 'release', 'upload', RELEASE_TAG, f'{part_path}#{asset}', '--clobber'], timeout=7200)
                if r.returncode == 0:
                    ok = True
                    break
                log('upload retry', asset, (r.stderr or r.stdout)[-200:])
                time.sleep(10 + attempt * 20)
            done_parts.append({'asset': asset, 'bytes': ln, 'sha256': sha256_file(part_path), 'ok': ok})
            if part_path != src:
                os.remove(part_path)
        bk[key] = {'done': all(x['ok'] for x in done_parts), 'at': now(), 'bytes': size, 'sha256': whole, 'release': RELEASE_TAG, 'parts': done_parts}
        log('backup', key, bk[key]['done'], len(done_parts), 'parts')


# ---------------------------------------------------------------- 主流程
def load_manifest():
    p = os.path.join(OUT, 'manifest.json')
    old = None
    if os.path.exists(p):
        try:
            old = json.load(open(p, encoding='utf-8'))
        except Exception:  # noqa
            old = None
    if old is not None and not FORCE:
        return old
    fresh = {'meta': {'account': ACCOUNT, 'own_emails': sorted(OWN_EMAILS), 'created': now()}, 'sources': [], 'progress': {},
             'shards': {}, 'backup': {}, 'runs': [], 'status': 'new'}
    if FORCE and os.path.isdir(OUT):
        import shutil
        for sub in ('messages', 'attachments', 'state'):       # 解析产物重建；settings/ 与备份记录保留
            shutil.rmtree(os.path.join(OUT, sub), ignore_errors=True)
        for fn in ('threads.json', 'contacts.csv', 'clients_link.json', '_coverage.md'):
            try:
                os.remove(os.path.join(OUT, fn))
            except FileNotFoundError:
                pass
        if old is not None:
            fresh['backup'] = old.get('backup', {})
            fresh['sources'] = old.get('sources', [])
            fresh['runs'] = old.get('runs', [])
            fresh['meta']['release_tag'] = old.get('meta', {}).get('release_tag')
            fresh['meta']['own_emails'] = sorted(set(fresh['meta']['own_emails']) | set(old.get('meta', {}).get('own_emails', [])))
            fresh['meta']['force_rebuilt_at'] = now()
    return fresh


def classify_bulk(msg, labels, from_e):
    if 'Spam' in labels:
        return True
    if hdr(msg, 'List-Unsubscribe') or hdr(msg, 'List-Id'):
        return True
    if hdr(msg, 'Precedence').lower() in ('bulk', 'list', 'junk'):
        return True
    a = hdr(msg, 'Auto-Submitted').lower()
    if a and a != 'no':
        return True
    if labels & BULK_LABELS:
        return True
    local = from_e.split('@', 1)[0] if '@' in from_e else from_e
    if BULK_LOCAL.match(local):
        return True
    return False


def labels_of(msg):
    raw = hdr(msg, 'X-Gmail-Labels')
    return {x.strip() for x in raw.split(',') if x.strip()} if raw else set()


def pass1(chain, start_offset, own, clients, limit):
    """只读头部：学习本邮箱地址（Sent）、找出「回过 / 与客户有关」的线程。"""
    hp = BytesHeaderParser(policy=policy.default)
    thr_keep = set()
    sent_from = Counter()
    n = 0
    for off, body_off, raw in iter_messages(chain, start_offset):
        n += 1
        if limit and n > limit:
            break
        try:
            m = hp.parsebytes(raw[:262144])
        except Exception:  # noqa
            continue
        labels = labels_of(m)
        thr = hdr(m, 'X-GM-THRID').strip() or hdr(m, 'Message-ID').strip() or str(off)
        froms = addr_list(m, 'From')
        fe = froms[0]['e'] if froms else ''
        if 'Sent' in labels and fe:
            sent_from[fe] += 1
        if fe in own or 'Sent' in labels:
            thr_keep.add(thr)
            continue
        for a in froms + addr_list(m, 'To', 'Cc'):
            if clients.match(a['e']):
                thr_keep.add(thr)
                break
    learned = {e for e, c in sent_from.most_common(5) if c >= 3}
    return thr_keep, learned, n


def process_message(off, raw, src_i, ctx):
    """src_i = 批次号（manifest.batches[].id），off = 该批次字节流里的分隔行偏移。"""
    own, clients, thr_keep, atts_store = ctx['own'], ctx['clients'], ctx['thr_keep'], ctx['atts']
    rec = {'k': None, 'src': src_i, 'off': off, 'bytes': len(raw)}
    try:
        msg = BytesParser(policy=policy.default).parsebytes(raw)
    except Exception as e:  # noqa
        try:
            msg = BytesParser(policy=policy.compat32).parsebytes(raw)
        except Exception as e2:  # noqa
            rec.update({'k': hashlib.sha1(raw[:4000]).hexdigest()[:16], 'err': f'parse: {e2}'[:200], 'text': raw[:2000].decode('utf-8', 'ignore')})
            return rec
    msgid = hdr(msg, 'Message-ID').strip()
    rec['msgid'] = msgid[:300]
    rec['k'] = hashlib.sha1((msgid or f'{src_i}:{off}').encode()).hexdigest()[:16]
    rec['thr'] = hdr(msg, 'X-GM-THRID').strip()
    rec['date'], rec['date_raw'] = parse_date(msg)
    froms = addr_list(msg, 'From')
    rec['from'] = froms[0] if froms else {'n': '', 'e': ''}
    rec['to'] = addr_list(msg, 'To')
    rec['cc'] = addr_list(msg, 'Cc')
    bcc = addr_list(msg, 'Bcc')
    if bcc:
        rec['bcc'] = bcc
    rt = addr_list(msg, 'Reply-To')
    if rt and rt[0]['e'] != rec['from']['e']:
        rec['reply_to'] = rt[0]
    rec['subj'] = hdr(msg, 'Subject').strip()[:500]
    labels = labels_of(msg)
    rec['labels'] = sorted(labels)
    irt = hdr(msg, 'In-Reply-To').strip()
    if irt:
        rec['irt'] = irt[:300]
    refs = hdr(msg, 'References').split()
    if refs:
        rec['refs'] = [r[:300] for r in refs[:30]]
    fe = rec['from']['e']
    rec['dir'] = 'out' if (fe in own or 'Sent' in labels) else 'in'
    bulk = classify_bulk(msg, labels, fe)
    thr_key = rec['thr'] or msgid or str(off)
    counterparts = [a['e'] for a in ([rec['from']] + rec['to'] + rec['cc']) if a['e'] and a['e'] not in own]
    codes = []
    for e in counterparts:
        c = clients.match(e)
        if c and c not in codes:
            codes.append(c)
    if codes:
        rec['client'] = codes
    keep_full = (BULK_MODE == 'full') or (not bulk) or (thr_key in thr_keep) or bool(codes) or rec['dir'] == 'out' \
        or bool(labels & {'Starred', 'Important'})
    rec['bulk'] = bulk
    rec['keep'] = 'full' if keep_full else 'snippet'
    texts, htmls, atts = [], [], []
    try:
        walk_body(msg, texts, htmls, atts)
    except Exception as e:  # noqa
        rec['err'] = f'body: {e}'[:200]
    plain = '\n'.join(t for t in texts if t and t.strip()).strip()
    if len(plain) >= 20 or not htmls:
        text, src = plain, 'plain'
    else:
        text, src = html_to_text('\n'.join(htmls)), 'html'
        if plain:
            text = plain + '\n' + text
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    rec['body_src'] = src
    rec['chars'] = len(text)
    qi = quote_index(text)
    if qi is not None and qi > 0:
        rec['quote_at'] = qi
    if not keep_full:
        text = text[:SNIPPET]
    elif len(text) > MAX_TEXT:
        text = text[:MAX_TEXT] + f'\n…[截断，共 {rec["chars"]} 字]'
    rec['text'] = text
    att_recs = []
    for name, ctype, part in atts:
        try:
            data = part.get_payload(decode=True) or b''
        except Exception:  # noqa
            data = b''
        sha16 = sha256_bytes(data)[:16] if data else ''
        a = {'n': name, 'm': ctype, 'b': len(data), 's': sha16}
        if data:
            a['x'] = atts_store.submit(sha16, name, ctype, data, rec['k'], extract=keep_full)
        att_recs.append(a)
    if att_recs:
        rec['att'] = att_recs
    return rec


def coverage_md(manifest, stats, clients):
    L = []
    L.append(f'# Gmail（{ACCOUNT} 邮箱）Takeout 全量入库 · 覆盖率报告\n')
    L.append(f'- 生成时间：{now()}；状态：**{manifest.get("status")}**；本邮箱地址：{", ".join(manifest["meta"].get("own_emails", []))}')
    srcs = manifest.get('sources', [])
    L.append(f'- 来源：{len(srcs)} 个文件，合计 {sum(s.get("bytes", 0) for s in srcs) / 1e9:.2f} GB：' + '；'.join(f'`{s["file"]}` {s.get("bytes", 0) / 1e9:.2f} GB' for s in srcs))
    for b in manifest.get('batches', []):
        L.append(f'- 批次 {b.get("id")}：{len(b.get("files", []))} 个文件 / mbox 条目 {b.get("entries", "?")} 个 / 流总长 {b.get("total_bytes", 0) / 1e9:.2f} GB，'
                 f'已处理到偏移 {b.get("offset", 0) / 1e9:.2f} GB，{b.get("messages", 0):,} 封，{"✅ 完成" if b.get("done") else "⏳ 未完"}'
                 + (f'，批尾 carry {b.get("carry_bytes")} B 交下一批' if b.get('carry_bytes') else '')
                 + ('' if b.get('starts_with_separator', True) else '，**⚠️ 流开头不是 `From ` 分隔行——前面可能缺一卷**'))
    exp = sum(int(b.get('messages', 0) or 0) for b in manifest.get('batches', []))
    got = int(stats.get('messages', 0) or 0)
    sh_bad = []
    for rel, n in (manifest.get('shards') or {}).items():
        p = os.path.join(OUT, rel)
        d = os.path.getsize(p) if os.path.exists(p) else -1
        if d != n:
            sh_bad.append(rel)
    if exp == got and not sh_bad:
        L.append(f'- 一致性自检：流中读到 {exp:,} 封 = 分片里 {got:,} 封；{len(manifest.get("shards") or {})} 个分片长度与记录一致 ✅')
    else:
        L.append(f'- **⚠️ 一致性自检失败**：流中读到 {exp:,} 封，分片里只有 {got:,} 封（差 {exp - got:,}）；长度不符的分片 {len(sh_bad)} 个 {sh_bad[:8]} —— 需 FORCE=1 从 Release 原件重跑')
    L.append(f'- 规则：**full** = 全文（非群发 / 本邮箱发出 / 本邮箱回过的线程 / 对方是 Saga Clients 里的客户 / 加星 / 重要）；'
             f'**snippet** = 群发与通知类只留头部 + 前 {SNIPPET} 字；附件按 sha256 去重抽正文（≤{ATTACH_MAX // 1024 // 1024} MB，文档类；图片 OCR={"开" if OCR else "关"}）')
    bk = manifest.get('backup', {})
    if bk:
        L.append('- 原件备份：' + '；'.join(f'`{k}` → Release `{v.get("release")}` {len(v.get("parts", []))} 卷 {"✅" if v.get("done") else "❌"}' for k, v in bk.items()))
    else:
        L.append('- 原件备份：—')
    L.append('')
    L.append('## 总量\n')
    L.append('| 指标 | 数 |\n|---|---|')
    for k in ('messages', 'full', 'snippet', 'out', 'in', 'bulk', 'with_client', 'parse_err', 'attachments', 'att_unique', 'att_ok', 'att_meta',
              'att_fail', 'att_skip', 'text_chars', 'att_chars'):
        L.append(f'| {k} | {stats.get(k, 0):,} |')
    L.append('')
    L.append('## 按年\n')
    L.append('| 年 | 封数 | 发出 | 收到 | 全文 | 群发 |\n|---|---|---|---|---|---|')
    for y in sorted(stats['by_year']):
        d = stats['by_year'][y]
        L.append(f'| {y} | {d["n"]:,} | {d["out"]:,} | {d["in"]:,} | {d["full"]:,} | {d["bulk"]:,} |')
    L.append('')
    L.append('## 标签（前 30）\n')
    L.append('| 标签 | 封数 |\n|---|---|')
    for lab, n in stats['labels'].most_common(30):
        L.append(f'| {lab} | {n:,} |')
    L.append('')
    L.append('## 对方域名（前 40，排除本邮箱与免费邮箱）\n')
    L.append('| 域名 | 封数 | 客户编号 |\n|---|---|---|')
    for dom, n in stats['domains'].most_common(40):
        code = clients.by_domain.get(dom, '')
        L.append(f'| {dom} | {n:,} | {code} |')
    L.append('')
    L.append('## 关联到 Saga Clients 的往来\n')
    L.append(f'- 命中客户编号 {len(stats["clients"])} 个：A {sum(1 for c in stats["clients"] if clients.grade.get(c) == "A")} / '
             f'B {sum(1 for c in stats["clients"] if clients.grade.get(c) == "B")} / C {sum(1 for c in stats["clients"] if clients.grade.get(c) == "C")}；'
             f'明细见 `clients_link.json`、`contacts.csv`')
    L.append('')
    L.append('## 附件类型\n')
    L.append('| 扩展名 | 个数（去重后） | 抽到正文 | 仅元数据 | 失败 | 跳过 |\n|---|---|---|---|---|---|')
    for ext, d in sorted(stats['att_ext'].items(), key=lambda x: -x[1]['n'])[:40]:
        L.append(f'| {ext or "(无)"} | {d["n"]:,} | {d["ok"]:,} | {d["meta"]:,} | {d["fail"]:,} | {d["skip"]:,} |')
    L.append('')
    L.append(f'## 解析失败（{len(stats["errors"])}）\n')
    if stats['errors']:
        L.append('| k | 偏移 | 错误 |\n|---|---|---|')
        for k, off, err in stats['errors'][:200]:
            L.append(f'| {k} | {off} | {err.replace("|", "/")} |')
        if len(stats['errors']) > 200:
            L.append(f'\n…另有 {len(stats["errors"]) - 200} 条，见 manifest.json')
    else:
        L.append('无。')
    L.append('')
    L.append(f'## 附件抽取失败（{len(stats["att_errors"])}）\n')
    if stats['att_errors']:
        L.append('| sha16 | 文件名 | 错误 |\n|---|---|---|')
        for s, nme, err in stats['att_errors'][:200]:
            L.append(f'| {s} | {nme.replace("|", "/")} | {err.replace("|", "/")} |')
    else:
        L.append('无。')
    L.append('')
    L.append('## 运行记录\n')
    for r in manifest.get('runs', []):
        L.append(f'- {json.dumps(r, ensure_ascii=False)}')
    with open(os.path.join(OUT, '_coverage.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')


def build_indexes(manifest, clients):
    """读全部分片 → threads.json / contacts.csv / clients_link.json / 统计（续跑安全：总是从分片重建）。"""
    stats = {'messages': 0, 'full': 0, 'snippet': 0, 'out': 0, 'in': 0, 'bulk': 0, 'with_client': 0, 'parse_err': 0, 'attachments': 0,
             'text_chars': 0, 'by_year': defaultdict(lambda: {'n': 0, 'out': 0, 'in': 0, 'full': 0, 'bulk': 0}), 'labels': Counter(),
             'domains': Counter(), 'clients': set(), 'errors': [], 'att_ext': defaultdict(lambda: {'n': 0, 'ok': 0, 'fail': 0, 'skip': 0}),
             'att_errors': [], 'att_unique': 0, 'att_ok': 0, 'att_meta': 0, 'att_fail': 0, 'att_skip': 0, 'att_chars': 0}
    stats['att_ext'] = defaultdict(lambda: {'n': 0, 'ok': 0, 'meta': 0, 'fail': 0, 'skip': 0})
    threads = {}
    contacts = {}
    clinks = defaultdict(lambda: {'messages': 0, 'out': 0, 'in': 0, 'first': '', 'last': '', 'last_subject': '', 'threads': set(), 'emails': set()})
    own = set(manifest['meta'].get('own_emails', []))
    for dp, _, fns in os.walk(MSG_DIR):
        for fn in sorted(fns):
            if not fn.endswith('.jsonl'):
                continue
            with open(os.path.join(dp, fn), encoding='utf-8') as f:
                for line in f:
                    try:
                        r = json.loads(line)
                    except Exception:  # noqa
                        continue
                    stats['messages'] += 1
                    if r.get('err'):
                        stats['parse_err'] += 1
                        stats['errors'].append((r.get('k'), r.get('off'), r['err']))
                        if not r.get('from'):
                            continue
                    y = (r.get('date') or '0000')[:4]
                    by = stats['by_year'][y]
                    by['n'] += 1
                    d = r.get('dir', 'in')
                    by[d] += 1
                    stats[d] += 1
                    stats[r.get('keep', 'full')] += 1
                    by['full'] += r.get('keep') == 'full'
                    if r.get('bulk'):
                        stats['bulk'] += 1
                        by['bulk'] += 1
                    stats['text_chars'] += len(r.get('text', ''))
                    for lab in r.get('labels', []):
                        stats['labels'][lab] += 1
                    atts = r.get('att', [])
                    stats['attachments'] += len(atts)
                    codes = r.get('client', [])
                    if codes:
                        stats['with_client'] += 1
                        stats['clients'].update(codes)
                    parties = [r.get('from', {})] + r.get('to', []) + r.get('cc', [])
                    for a in parties:
                        e = a.get('e', '')
                        if not e or e in own:
                            continue
                        dom = e.rsplit('@', 1)[-1]
                        if dom not in FREEMAIL:
                            stats['domains'][dom] += 1
                        c = contacts.setdefault(e, {'email': e, 'names': Counter(), 'domain': dom, 'in': 0, 'out': 0, 'n': 0, 'first': '', 'last': '',
                                                   'last_subject': '', 'client': clients.match(e) or ''})
                        c['n'] += 1
                        if a.get('n'):
                            c['names'][a['n']] += 1
                        if a is r.get('from'):
                            c['in'] += 1
                        elif d == 'out':
                            c['out'] += 1
                        dt = r.get('date') or ''
                        if dt and (not c['first'] or dt < c['first']):
                            c['first'] = dt
                        if dt and dt >= c['last']:
                            c['last'] = dt
                            c['last_subject'] = r.get('subj', '')[:120]
                    tk = r.get('thr') or r.get('msgid') or r.get('k')
                    t = threads.setdefault(tk, {'subject': r.get('subj', '')[:200], 'first': '', 'last': '', 'n': 0, 'out': 0, 'in': 0,
                                                'participants': Counter(), 'domains': Counter(), 'client': set(), 'labels': Counter(), 'atts': 0, 'keys': []})
                    t['n'] += 1
                    t[d] += 1
                    t['atts'] += len(atts)
                    dt = r.get('date') or ''
                    if dt and (not t['first'] or dt < t['first']):
                        t['first'] = dt
                        t['subject'] = r.get('subj', '')[:200] or t['subject']
                    if dt and dt >= t['last']:
                        t['last'] = dt
                    for a in parties:
                        if a.get('e') and a['e'] not in own:
                            t['participants'][a['e']] += 1
                            dom = a['e'].rsplit('@', 1)[-1]
                            if dom not in FREEMAIL:
                                t['domains'][dom] += 1
                    t['client'].update(codes)
                    for lab in r.get('labels', []):
                        t['labels'][lab] += 1
                    if len(t['keys']) < 500:
                        t['keys'].append(r.get('k'))
                    for code in codes:
                        cl = clinks[code]
                        cl['messages'] += 1
                        cl[d] += 1
                        if dt and (not cl['first'] or dt < cl['first']):
                            cl['first'] = dt
                        if dt and dt >= cl['last']:
                            cl['last'] = dt
                            cl['last_subject'] = r.get('subj', '')[:120]
                        cl['threads'].add(tk)
                        for a in parties:
                            if a.get('e') and clients.match(a['e']) == code:
                                cl['emails'].add(a['e'])
    # 附件统计
    idx_p = os.path.join(ATT_DIR, 'index.json')
    if os.path.exists(idx_p):
        idx = json.load(open(idx_p, encoding='utf-8'))
        stats['att_unique'] = len(idx)
        for s, a in idx.items():
            ext = os.path.splitext(a.get('name', ''))[1].lower()
            d = stats['att_ext'][ext]
            d['n'] += 1
            x = a.get('x', 'skip')
            if x == 'ok':
                d['ok'] += 1
                stats['att_ok'] += 1
                stats['att_chars'] += a.get('chars', 0)
            elif x == 'fail':
                d['fail'] += 1
                stats['att_fail'] += 1
                stats['att_errors'].append((s, a.get('name', ''), a.get('err', '')))
            elif x == 'meta':
                d['meta'] += 1
                stats['att_meta'] += 1
            else:
                d['skip'] += 1
                stats['att_skip'] += 1
    # 写索引
    th_out = {}
    for k, t in threads.items():
        th_out[k] = {'subject': t['subject'], 'first': t['first'], 'last': t['last'], 'n': t['n'], 'out': t['out'], 'in': t['in'],
                     'participants': [e for e, _ in t['participants'].most_common(12)], 'domains': [d for d, _ in t['domains'].most_common(6)],
                     'client': sorted(t['client']), 'labels': [l for l, _ in t['labels'].most_common(6)], 'atts': t['atts'], 'keys': t['keys']}
    write_json(os.path.join(OUT, 'threads.json'), {'meta': {'generated': now(), 'threads': len(th_out)}, 'threads': th_out})
    with open(os.path.join(OUT, 'contacts.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['email', 'name', 'domain', 'received_from', 'sent_to', 'appearances', 'first', 'last', 'last_subject', 'client_code', 'client_grade', 'client_name'])
        for e, c in sorted(contacts.items(), key=lambda x: -(x[1]['n'])):
            w.writerow([e, c['names'].most_common(1)[0][0] if c['names'] else '', c['domain'], c['in'], c['out'], c['n'], c['first'][:10], c['last'][:10],
                        c['last_subject'], c['client'], clients.grade.get(c['client'], '') if c['client'] else '', clients.name.get(c['client'], '') if c['client'] else ''])
    cl_out = {}
    for code, cl in clinks.items():
        cl_out[code] = {'grade': clients.grade.get(code, ''), 'name': clients.name.get(code, ''), 'messages': cl['messages'], 'out': cl['out'], 'in': cl['in'],
                        'first': cl['first'], 'last': cl['last'], 'last_subject': cl['last_subject'], 'emails': sorted(cl['emails']),
                        'threads': sorted(cl['threads'])[:300]}
    write_json(os.path.join(OUT, 'clients_link.json'), {'meta': {'generated': now(), 'account': ACCOUNT, 'clients': len(cl_out)}, 'clients': cl_out})
    stats['by_year'] = dict(stats['by_year'])
    stats['att_ext'] = dict(stats['att_ext'])
    return stats


def main():
    global RELEASE_TAG
    log(f'gmail ingest: account={ACCOUNT} out={OUT} bulk_mode={BULK_MODE} attach={ATTACH} ocr={OCR} more_batches={MORE_BATCHES} tools: '
        + ' '.join(f'{c}={"y" if have(c) else "n"}' for c in ('tesseract', 'soffice', 'pdftoppm', 'gh')))
    os.makedirs(OUT, exist_ok=True)
    state_dir = os.path.join(OUT, STATE_DIR_NAME)
    manifest = load_manifest()          # FORCE 时会清掉 messages/ attachments/ state/
    os.makedirs(state_dir, exist_ok=True)
    if manifest['meta'].get('release_tag') and not os.environ.get('RELEASE_TAG'):
        RELEASE_TAG = manifest['meta']['release_tag']       # 多批 / 续跑 / FORCE 重建都沿用同一个 Release
    manifest['meta']['release_tag'] = RELEASE_TAG
    manifest['runs'].append({'started': now(), 'limit': LIMIT, 'bulk_mode': BULK_MODE, 'attach': ATTACH, 'ocr': OCR, 'more_batches': MORE_BATCHES})
    paths = resolve_sources()
    old_src = {s.get('file'): s for s in manifest.get('sources', [])}
    cur_sources = [{'label': l, 'file': os.path.basename(p), 'bytes': os.path.getsize(p),
                    'sha256': (old_src.get(os.path.basename(p)) or {}).get('sha256') or sha256_file(p)} for l, p in paths]
    # 批次：来源文件集合相同 → 同一批（续跑）；不同 → 新批次（分几次上传的后续批）
    batches = manifest.setdefault('batches', [])
    key = sorted(x['file'] for x in cur_sources)
    batch = next((b for b in batches if sorted(b.get('files', [])) == key), None)
    if batch is None:
        batch = {'id': len(batches) + 1, 'files': key, 'started': now(), 'offset': 0, 'messages': 0, 'done': False}
        batches.append(batch)
    bid = batch['id']
    known = {x['file'] for x in manifest.get('sources', [])}
    manifest['sources'] = manifest.get('sources', []) + [x for x in cur_sources if x['file'] not in known]
    backup_sources(paths, manifest)
    write_json(os.path.join(OUT, 'manifest.json'), manifest)

    openers = mbox_openers(paths)
    carry_path = os.path.join(state_dir, 'carry.bin')
    if bid > 1 and os.path.exists(carry_path) and os.path.getsize(carry_path) > 0 and not batch.get('done'):
        # 上一批被切断的尾巴接到本批最前面
        log(f'prepend carry from previous batch: {os.path.getsize(carry_path)} bytes')
        openers.insert(0, ('carry(previous batch tail)', (lambda cp=carry_path: open(cp, 'rb')), os.path.getsize(carry_path)))
    total = sum(o[2] for o in openers)
    prog = manifest['progress'] = batch          # 兼容旧字段：progress 指向当前批
    prog.update({'entries': len(openers), 'entry_names': [o[0] for o in openers][:50], 'total_bytes': total})
    start = 0 if FORCE else int(prog.get('offset', 0) or 0)
    if start == 0 and total:
        head = Chain([(o[0], o[1]) for o in openers]).read(5)
        prog['starts_with_separator'] = (head == b'From ')
        if head != b'From ':
            log(f'WARN: stream does not start with a "From " separator (first bytes {head!r}) → 可能缺前一卷 / 前一批')
    if prog.get('done') and not FORCE:
        log(f'batch {bid} already done; rebuilding indexes only')
        start = total
    clients = Clients()
    own = set(OWN_EMAILS) | set(manifest['meta'].get('own_emails', []))

    # pass 1：头部扫描（学习本邮箱地址 + 要全文保留的线程）；线程集合跨批次累积（state/thr_keep.txt）
    thr_path = os.path.join(state_dir, 'thr_keep.txt')
    thr_prev = set(open(thr_path, encoding='utf-8').read().split()) if os.path.exists(thr_path) else set()
    chain = Chain([(o[0], o[1]) for o in openers])
    thr_keep, learned, n1 = pass1(chain, 0, own, clients, LIMIT)
    thr_keep |= thr_prev
    if learned - own:
        log('learned own addresses from Sent:', sorted(learned - own))
    own |= learned
    manifest['meta']['own_emails'] = sorted(own)
    os.makedirs(state_dir, exist_ok=True)
    with open(thr_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(thr_keep)))
    log(f'pass1: {n1} messages scanned, threads to keep full: {len(thr_keep)} (incl. {len(thr_prev)} from previous batches)')

    # pass 2：全量解析
    shards = Shards(manifest)
    atts = AttachStore(manifest)
    ctx = {'own': own, 'clients': clients, 'thr_keep': thr_keep, 'atts': atts}
    chain = Chain([(o[0], o[1]) for o in openers])
    tail_sink = [] if MORE_BATCHES else None
    n = done_since = 0
    last_ckpt = time.time()
    deadline = T0 + MAX_MINUTES * 60
    stopped_early = False
    last_off = start

    n_before = int(prog.get('messages', 0) or 0) if start else 0

    def checkpoint(final=False):
        shards.checkpoint()
        atts.save()
        prog['offset'] = last_off
        prog['messages'] = n_before + n
        manifest['status'] = 'done' if final else 'partial'
        write_json(os.path.join(OUT, 'manifest.json'), manifest)
        with open(os.path.join(OUT, '_run_status.md'), 'w', encoding='utf-8') as f:   # 运行状态（代理读不到 Actions 日志，只看这里）
            f.write(f'# Gmail({ACCOUNT}) 入库运行状态\n\n- {now()} 批次 {bid}：{"✅ 完成" if final else "⏳ 运行中/阶段提交"}，'
                    f'偏移 {last_off:,}/{total:,}（{(last_off / total * 100) if total else 0:.1f}%），本批 {n_before + n:,} 封，'
                    f'开跑 {T0_ISO}，已用 {(time.time() - T0) / 60:.0f} min\n' + (f'- {DISK_NOTE}\n' if DISK_NOTE else ''))

    for off, body_off, raw in iter_messages(chain, start, tail_sink):
        if LIMIT and n >= LIMIT:
            break
        if time.time() > deadline:
            stopped_early = True
            log('MAX_MINUTES reached → graceful stop at offset', off)
            break
        try:
            rec = process_message(off, raw, bid, ctx)
        except Exception as e:  # noqa
            rec = {'k': hashlib.sha1(raw[:4000]).hexdigest()[:16], 'src': bid, 'off': off, 'bytes': len(raw), 'err': f'process: {type(e).__name__}: {e}'[:200],
                   'text': raw[:2000].decode('utf-8', 'ignore'), 'from': {'n': '', 'e': ''}, 'to': [], 'cc': [], 'labels': [], 'dir': 'in', 'keep': 'full'}
        shards.write(rec)
        n += 1
        done_since += 1
        last_off = body_off + len(raw)
        atts.drain()
        if n % 2000 == 0:
            log(f'{n} messages, offset {last_off / 1e9:.2f}/{total / 1e9:.2f} GB, att pending {len(atts.futures)}')
        if done_since >= COMMIT_EVERY or (time.time() - last_ckpt) > CHECKPOINT_MIN * 60:
            atts.wait_all()
            checkpoint()
            shards.close()      # 10-24 修复：git pull --rebase 会用新 inode 重写分片文件，若句柄仍开着，之后的追加全部写进孤儿 inode（A 邮箱首跑丢 5,674 封）
            git_commit_push(f'T29: Gmail({ACCOUNT}) 入库 · 检查点 {prog["messages"]} 封 / {last_off / 1e9:.2f} GB')
            shards.verify('after checkpoint push')
            done_since = 0
            last_ckpt = time.time()
    atts.finish()
    shards.close()
    complete = not stopped_early and not (LIMIT and n >= LIMIT)
    if complete:
        last_off = total if total else last_off
        prog['done'] = True
        prog['ended'] = now()
        if tail_sink:   # MORE_BATCHES：批尾半封存为 carry，下一批接上
            sep_line, tail, _ = tail_sink[-1]
            with open(carry_path, 'wb') as f:
                f.write(sep_line + tail)
            batch['carry_bytes'] = len(sep_line) + len(tail)
            log(f'batch {bid} tail kept as carry: {len(tail)} bytes (will be completed by next batch)')
        elif os.path.exists(carry_path) and bid > 1:
            os.remove(carry_path)
    all_done = complete and not MORE_BATCHES
    checkpoint(final=all_done)
    if complete and MORE_BATCHES:
        manifest['status'] = 'awaiting_next_batch'
        write_json(os.path.join(OUT, 'manifest.json'), manifest)
    stats = build_indexes(manifest, clients)
    manifest['stats'] = {k: v for k, v in stats.items() if k in ('messages', 'full', 'snippet', 'out', 'in', 'bulk', 'with_client', 'parse_err',
                                                                 'attachments', 'att_unique', 'att_ok', 'att_fail', 'att_skip', 'text_chars', 'att_chars')}
    manifest['stats']['clients'] = len(stats['clients'])
    manifest['runs'][-1].update({'ended': now(), 'messages_this_run': n, 'stopped_early': stopped_early})
    write_json(os.path.join(OUT, 'manifest.json'), manifest)
    coverage_md(manifest, stats, clients)
    label = '完成' if all_done else (f'第 {bid} 批完成，等下一批' if complete else '阶段提交')
    git_commit_push(f'T29: Gmail({ACCOUNT}) 入库 {label}：{stats["messages"]} 封（全文 {stats["full"]} / 摘要 {stats["snippet"]}），'
                    f'附件 {stats["att_unique"]} 个去重、正文 {stats["att_ok"]}，关联客户 {len(stats["clients"])} 家')
    log('DONE', json.dumps(manifest['stats'], ensure_ascii=False), 'stopped_early' if stopped_early else '')


if __name__ == '__main__':
    main()
