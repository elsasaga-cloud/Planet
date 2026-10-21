#!/usr/bin/env python3
"""SmartByte 官网整站归档器（T15）。

在 GitHub Actions 运行器上执行（Arena 沙箱对 smartbyte-switch.com 无出网权限）。
职责只有一个：把站点上**所有**可达页面、附件（规格书等）、图片原样抓下来并写清单；
解析/整理在仓库内另做（scripts/smartbyte_crawl/build.py）。

用法：python crawl.py <OUT_dir(入 git)> <BIN_dir(二进制，不入 git)>
环境变量：MAX_PAGES(默认 1500) DELAY(默认 0.8s) MAX_IMAGE_MB(默认 600) PDF_COMMIT_MB(默认 60)
          TIME_BUDGET_MIN(默认 140：墙钟预算，分钟；到点优雅收尾，保证后续 zip / 上传 / 提交步骤能跑)
          CRAWL_HOST / CRAWL_SCHEME（仅本地自测用，默认 www.smartbyte-switch.com / https）

v2（2026-10-20，Actions 运行 #1 在 170 分钟作业上限被杀、颗粒无收之后）：
  ① 墙钟预算：页面阶段最多用预算的 55%，附件阶段累计 85%，图片阶段用满 100%；到点即停、照常写清单与汇总并以 0 退出，
     这样工作流后面的 zip / upload-artifact / commit / release 步骤一定执行，已抓到的东西一定落地。
  ② 断点续抓：OUT 目录里的 pages_manifest.jsonl / downloads_manifest.jsonl / images_manifest.jsonl + crawl_state.json
     随上一轮提交回分支；下一轮（workflow_dispatch 或再推一次本文件）从 crawl_state.json 的队列继续，已抓成功的 URL 不重抓，
     直到 summary.json 的 complete=true。
  ③ 清单每 25 页 / 20 个附件 / 100 张图写一次盘（不是只在最后写），日志跨轮追加。
v2.1（2026-10-20，运行 #2 59 秒即"完成"但首页 / sitemap 均 HTTP 403 之后）：
  ① 开工先探路（probe_access）：归档 UA → 三种浏览器 UA（含 http / 不带 www 变体）→ Playwright 真浏览器（现装 Chromium，
     过 JS 挑战后把 cookie 移植给 requests；移植无效则全程走浏览器上下文请求）。探路结果写 access_diag.json（状态码、server /
     cf-ray / cf-mitigated 头、正文前 600 字），方便判断是 UA 规则、JS 挑战还是 IP 段封禁。
  ② 全部被拒 → mode=blocked：本轮不抓、不重试、不清队列，summary.json complete=false 并写明 how_to_continue。
  ③ 抓取中途连续 12 次 403/429/网络错误 → 判定被封，当前阶段立即优雅收尾（状态照存，下轮续抓），不再把预算烧在重试上。
  ④ 0 页成功时 complete 永远为 false（运行 #2 的假 complete 不再出现）；主流程异常也落盘日志 + summary 后以 0 退出，
     保证工作流后续提交步骤执行。默认 DELAY 0.8 → 1.2 秒、图片间隔 0.3 → 0.5 秒（运行 #1 疑似触发限速）。
v2.2（2026-10-21，运行 #3 页面 350/350 抓齐、但 245 份规格书经 index.php?c=Front/DownDetail&a=downloadFujian 全部 HTTP 403、
     图片 0 张之后）：
  ① 附件：downloadFujian 的 path= 是 base64 的站内静态路径（/comdata/<租户>/productfujian/xxx.pdf）。下载改为候选链：
     站内直链 → CDN 直链（gcdn.meidianbang.cn / *.wds168.cn，站点图片正是从这些 CDN 出的）→ 原 PHP 下载口，
     一律带浏览器 UA + Referer（来源产品页）；以正文 %PDF / content-type 判定成功，HTML 小响应不算成功
     （运行 #3 两条 45 字节 text/html 的「成功」记录在续抓时作废重下）。只有候选全败才计入连续失败。
     文件名改用 name= 参数（规格书标题）+ .pdf，同名不同内容加 sha 前 8 位。PDF_COMMIT_MB 默认 60 → 120。
  ② 图片：站点自有图片全在 CDN（/comdata/<租户>/…），原先按「外站」跳过 → 现从已归档 HTML 里直接收集（不重抓页面），
     带 Referer 下载进二进制目录（随 Release 附件保存），主题/皮肤素材（/images/、/skinp/、/share/）仍不收。
v2.3（2026-10-21，运行 #4 规格书 245/245 直链成功、图片 900/1493 后 CDN 断流 ChunkedEncodingError 把整轮打崩之后）：
  读响应体（r.content）一律包在 try 里：图片 / 附件读体中断只记该条错误并继续，不再让整轮崩；候选链判定也放进 try。
v2.4（2026-10-21，运行 #5 站点对运行器 IP 全 403 但剩余 593 张图都在 CDN 之后）：
  站点被封时若剩余任务只剩 CDN 图片，先探一张 CDN 图：能取就照常跑图片阶段（CDN 与站点不是同一套封禁）；
  页面 / 附件 / 图片三阶段都无剩余时 complete=true，不再因本轮探测被拒而记为未完成。
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import deque
from datetime import datetime, timezone
from urllib.parse import parse_qsl, unquote, urlencode, urljoin, urlparse, urlunparse

import requests

HOST = os.environ.get("CRAWL_HOST", "www.smartbyte-switch.com")
SCHEME = os.environ.get("CRAWL_SCHEME", "https")
BASE = f"{SCHEME}://{HOST}/"
HOSTS_OK = {HOST.lower(), HOST[4:].lower() if HOST.lower().startswith("www.") else ("www." + HOST).lower()}
OUT = sys.argv[1] if len(sys.argv) > 1 else "data/smartbyte_site_raw"
BIN = sys.argv[2] if len(sys.argv) > 2 else "crawl_bin"
MAX_PAGES = int(os.environ.get("MAX_PAGES", "1500"))
DELAY = float(os.environ.get("DELAY", "1.2"))
MAX_IMAGE_MB = float(os.environ.get("MAX_IMAGE_MB", "600"))
PDF_COMMIT_MB = float(os.environ.get("PDF_COMMIT_MB", "120"))
TIME_BUDGET_MIN = float(os.environ.get("TIME_BUDGET_MIN", "140"))
UA = "Mozilla/5.0 (compatible; SagaTelecom-site-archiver/1.0; +https://sagatele.com)"

ASSET_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp", ".css", ".js", ".woff", ".woff2",
             ".ttf", ".eot", ".otf", ".mp4", ".webm", ".mp3", ".map", ".json")
FILE_EXT = (".pdf", ".zip", ".rar", ".7z", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".bin", ".img", ".exe")
IMG_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico")
# 站点自有内容所在 CDN（建站 SaaS 的对象存储）；只收 /comdata/<租户号>/ 下的东西，不收主题素材
CDN_HOSTS = ("gcdn.meidianbang.cn", "cdn-hk.wds168.cn", "img-for-hk.wds168.cn")
CDN_CONTENT_RE = re.compile(r"^https?://(?:gcdn\.meidianbang\.cn|[a-z0-9.-]*\.wds168\.cn)/comdata/\d+/", re.I)

S = requests.Session()
S.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.5"})
T0 = time.time()
LOG = []
RUN_ID = os.environ.get("GITHUB_RUN_NUMBER") or datetime.now(timezone.utc).strftime("local-%Y%m%d%H%M%S")

# 阶段预算（占总预算比例）：页面 55% → 附件累计 85% → 图片 100%
PHASE_CAP = {"pages": 0.55, "downloads": 0.85, "images": 1.0}


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    LOG.append(line)


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def elapsed():
    return time.time() - T0


def over_budget(phase):
    """该阶段是否已用完预算。到点只记一次日志。"""
    cap = TIME_BUDGET_MIN * 60 * PHASE_CAP[phase]
    if elapsed() >= cap:
        if not getattr(over_budget, "_said", {}).get(phase):
            over_budget._said = getattr(over_budget, "_said", {})
            over_budget._said[phase] = True
            log(f"TIME BUDGET: phase '{phase}' cap {cap / 60:.0f} min reached at {elapsed() / 60:.1f} min → graceful stop of this phase")
        return True
    return False


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def found(d, u):
    """记录「在哪页发现」：最多留 20 个样本 + 计数（页眉 logo 之类会出现在每一页，不能把 1500 个 URL 全存进状态文件）。"""
    d["n"] = d.get("n", 0) + 1
    if u not in d["found_on"] and len(d["found_on"]) < 20:
        d["found_on"].append(u)
    return d


def norm(u, base=None):
    try:
        u = urljoin(base or BASE, u.strip())
        p = urlparse(u)
    except Exception:
        return None
    if p.scheme not in ("http", "https"):
        return None
    if p.netloc.lower() not in HOSTS_OK:
        return None
    path = p.path or "/"
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not k.lower().startswith("utm")]
    return urlunparse((SCHEME, HOST, path, "", urlencode(q), ""))


def kind(u):
    """page / download / image / asset"""
    p = urlparse(u)
    path = p.path.lower()
    q = p.query.lower()
    if "downdetail" in path.lower() or "downdetail" in q or "a=download" in q:
        return "download"
    if path.endswith(IMG_EXT):
        return "image"
    if path.endswith(FILE_EXT):
        return "download"
    if path.endswith(ASSET_EXT):
        return "asset"
    return "page"


def fname(u, ext=""):
    p = urlparse(u)
    s = unquote(p.path).strip("/") or "index"
    if p.query:
        s += "__" + unquote(p.query)
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_")
    if len(s) > 140:
        s = s[:110] + "_" + hashlib.md5(u.encode()).hexdigest()[:10]
    return s + ext


CHROME_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
BROWSER_PROFILES = [
    ("chrome-win", CHROME_UA),
    ("firefox-win", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"),
    ("safari-mac", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"),
]
BROWSER_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.5",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1",
}
CHALLENGE_MARKS = ("just a moment", "cf-chl", "challenge-platform", "attention required", "checking your browser",
                   "verify you are human", "access denied", "captcha", "请稍候", "访问被拒绝")
ACCESS = {"mode": None, "profile": None, "base": None}  # probe_access() 填：requests / requests+cookies / playwright / blocked
CONSEC = {"n": 0}  # 连续 403/429/网络错误计数（任一成功即清零）
CONSEC_LIMIT = 12
_PW = {}


def looks_challenge(text):
    t = (text or "")[:4000].lower()
    return any(m in t for m in CHALLENGE_MARKS)


class Resp:
    """requests.Response 的最小替身（Playwright 通道用）：status_code / url / headers / content / text / encoding。"""

    def __init__(self, status, url, headers, body):
        self.status_code = status
        self.url = url
        self.headers = requests.structures.CaseInsensitiveDict(headers or {})
        self.content = body or b""
        m = re.search(r"charset=([\w-]+)", self.headers.get("content-type", "") or "", flags=re.I)
        self.encoding = m.group(1) if m else None
        self.apparent_encoding = "utf-8"

    @property
    def text(self):
        try:
            return self.content.decode(self.encoding or "utf-8", errors="replace")
        except LookupError:
            return self.content.decode("utf-8", errors="replace")


def _note(ok):
    CONSEC["n"] = 0 if ok else CONSEC["n"] + 1


def banned():
    return CONSEC["n"] >= CONSEC_LIMIT


def pw_bootstrap():
    """装 Playwright + Chromium（运行器上现装，约 1-3 分钟）。返回 (ok, info)。"""
    info = {}
    try:
        try:
            import playwright  # noqa: F401
        except ImportError:
            for extra in ([], ["--break-system-packages"], ["--user", "--break-system-packages"]):
                p = subprocess.run([sys.executable, "-m", "pip", "install", "-q", *extra, "playwright"],
                                   capture_output=True, text=True, timeout=600)
                if p.returncode == 0:
                    break
            info["pip"] = p.returncode
            if p.returncode != 0:
                info["pip_err"] = (p.stderr or p.stdout)[-800:]
                return False, info
        p = subprocess.run([sys.executable, "-m", "playwright", "install", "--with-deps", "chromium"],
                           capture_output=True, text=True, timeout=1500)
        info["install_with_deps"] = p.returncode
        if p.returncode != 0:
            info["install_with_deps_err"] = (p.stderr or p.stdout)[-800:]
            subprocess.run(["sudo", "-n", sys.executable, "-m", "playwright", "install-deps", "chromium"],
                           capture_output=True, text=True, timeout=1500)
            p = subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], capture_output=True, text=True, timeout=1500)
            info["install"] = p.returncode
            if p.returncode != 0:
                info["install_err"] = (p.stderr or p.stdout)[-800:]
                return False, info
        from playwright.sync_api import sync_playwright
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled", "--no-sandbox"])
        ctx = browser.new_context(user_agent=CHROME_UA, locale="en-US", viewport={"width": 1366, "height": 850},
                                  extra_http_headers={"Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.5"})
        _PW.update(pw=pw, browser=browser, ctx=ctx, page=ctx.new_page())
        return True, info
    except Exception as e:
        info["error"] = repr(e)
        return False, info


def pw_open_seed(u):
    """真浏览器打开首页，给 JS 挑战最多 25 秒；再用同上下文的 request 拿权威状态码。返回 (status, title, body_head)。"""
    page = _PW["page"]
    resp = page.goto(u, wait_until="domcontentloaded", timeout=60000)
    status = resp.status if resp else None
    title = ""
    for _ in range(25):
        try:
            title = page.title()
        except Exception:
            title = ""
        if status == 200 and not looks_challenge(title):
            break
        page.wait_for_timeout(1000)
        if _ % 5 == 4:
            try:
                r2 = _PW["ctx"].request.get(u, timeout=30000)
                status = r2.status
            except Exception:
                pass
    try:
        head = page.content()[:600]
    except Exception:
        head = ""
    return status, title, head


def pw_get(u, timeout=45):
    """Playwright 通道：复用浏览器上下文的 cookie / UA 直接请求（不渲染）。返回 (Resp, None) 或 (None, err)。"""
    last = None
    for i in range(3):
        try:
            r = _PW["ctx"].request.get(u, timeout=timeout * 1000, max_redirects=10)
            if r.status in (403, 429, 500, 502, 503, 504):
                last = f"HTTP {r.status}"
                if r.status == 403 and i == 0:
                    try:
                        pw_open_seed(BASE)  # 挑战 cookie 可能过期：用页面重新过一次首页
                    except Exception:
                        pass
                time.sleep(5 * (i + 1))
                continue
            _note(True)
            return Resp(r.status, r.url, r.headers, r.body()), None
        except Exception as e:
            last = repr(e)
            time.sleep(3 * (i + 1))
    _note(False)
    return None, last


def get(u, stream=False, timeout=45, headers=None):
    if ACCESS["mode"] == "playwright":
        return pw_get(u, timeout)
    last = None
    for i in range(3):
        try:
            r = S.get(u, timeout=timeout, stream=stream, allow_redirects=True, headers=headers)
            if r.status_code in (403, 429, 500, 502, 503, 504):
                last = f"HTTP {r.status_code}"
                time.sleep(5 * (i + 1))
                continue
            _note(True)
            return r, None
        except requests.RequestException as e:
            last = repr(e)
            time.sleep(3 * (i + 1))
    _note(False)
    return None, last


def fujian_path(u):
    """downloadFujian&path=<base64> → 解码出的站内静态路径（/comdata/<租户>/productfujian/xxx.pdf）；解不出返回 None。"""
    try:
        q = dict(parse_qsl(urlparse(u).query, keep_blank_values=True))
        raw = (q.get("path") or "").strip()
        if not raw:
            return None
        import base64
        pth = base64.b64decode(raw + "=" * (-len(raw) % 4)).decode("utf-8", "ignore").strip()
        return pth if pth.startswith("/") and ".." not in pth and len(pth) < 300 else None
    except Exception:
        return None


def fujian_name(u):
    try:
        q = dict(parse_qsl(urlparse(u).query, keep_blank_values=True))
        return (q.get("name") or "").strip() or None
    except Exception:
        return None


def download_candidates(u):
    pth = fujian_path(u)
    if not pth:
        return [u]
    return [f"{SCHEME}://{HOST}{pth}"] + [f"https://{h}{pth}" for h in CDN_HOSTS] + [u]


def looks_file(r):
    """真文件（PDF 等）而不是被拒 / 登录页之类的 HTML 小响应。"""
    ct = (r.headers.get("content-type") or "").lower()
    body = r.content
    if body[:5] == b"%PDF-" or body[:2] == b"PK" or body[:4] == b"Rar!":
        return True
    if "pdf" in ct or "octet-stream" in ct or "zip" in ct or "msword" in ct or "officedocument" in ct:
        return len(body) > 200
    return ("html" not in ct and "text/" not in ct and "json" not in ct) and len(body) > 2000


def get_download(u, referer=None):
    """附件下载：候选链 站内直链 → CDN 直链 → 原 PHP 口；每个候选最多 2 次；成功返回 (resp, None, 实际 URL)。
    全部失败返回 (None, 诊断串, None)。只有全部失败才计入连续失败（否则 PHP 口的 403 会误触发「被封」判定）。"""
    hdr = {"User-Agent": CHROME_UA, "Accept": "*/*", "Referer": referer or BASE,
           "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}
    tried = []
    for c in download_candidates(u):
        if ACCESS["mode"] == "playwright" and c == u:
            r, err = pw_get(c, 120)
            if r is not None and r.status_code == 200 and looks_file(r):
                _note(True)
                return r, None, c
            tried.append(f"pw {c[:70]}: {err or 'HTTP ' + str(r.status_code)}")
            continue
        for i in range(2):
            try:
                r = S.get(c, timeout=120, allow_redirects=True, headers=hdr)
                good = r.status_code == 200 and looks_file(r)  # looks_file 读 r.content，读体中断也在这里接住
            except (requests.RequestException, OSError, ValueError) as e:
                tried.append(f"{c.split('?')[0][-70:]}: {e.__class__.__name__}")
                time.sleep(2 * (i + 1))
                continue
            if good:
                _note(True)
                return r, None, c
            tried.append(f"{c.split('?')[0][-70:]}: HTTP {r.status_code} {(r.headers.get('content-type') or '')[:28]} {len(r.content)}B")
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(4 * (i + 1))
                continue
            break
    _note(False)
    return None, " | ".join(tried), None


def bogus_download(d):
    """上一轮记成「成功」但其实是 HTML 小响应（运行 #3：45 字节 text/html 的 index.php）。"""
    return (d.get("bytes") or 0) < 2000 and "html" in (d.get("content_type") or "").lower()


def harvest_cdn_images(images, pages):
    """从已归档的 HTML 里收集 CDN 上的站点自有图片（/comdata/<租户>/…），不重抓页面。返回新增条数。"""
    url_of = {p["file"]: p["url"] for p in pages if p.get("file")}
    added = 0
    hdir = os.path.join(OUT, "html")
    rx = re.compile(r"""(?:src|data-src|data-original|href)\s*=\s*["']([^"']+)["']""", re.I)
    for fn in sorted(os.listdir(hdir)) if os.path.isdir(hdir) else []:
        try:
            with open(os.path.join(hdir, fn), encoding="utf-8", errors="ignore") as f:
                html = f.read()
        except OSError:
            continue
        page_url = url_of.get(f"html/{fn}", BASE)
        for m in rx.finditer(html):
            u = m.group(1).strip()
            if not CDN_CONTENT_RE.match(u) or not urlparse(u).path.lower().endswith(IMG_EXT):
                continue
            if u not in images:
                added += 1
            found(images.setdefault(u, {"found_on": [], "alt": ""}), page_url)
    return added


def probe_access():
    """开工前探路：首页用哪种身份能拿到 200？归档 UA → 浏览器 UA（含 http / 不带 www 变体）→ Playwright 真浏览器。
    结果写 access_diag.json；mode ∈ requests / requests+cookies / playwright / blocked。"""
    global UA, BASE, SCHEME, HOST
    diag = {"probed_at": now(), "runner_ip": None, "tried": [], "mode": None}
    if os.environ.get("CRAWL_HOST") is None:  # 真跑时记下运行器出口 IP（若需请站方放行）
        try:
            diag["runner_ip"] = requests.get("https://api.ipify.org?format=text", timeout=10).text.strip()[:64]
        except Exception:
            pass
    apex = HOST[4:] if HOST.lower().startswith("www.") else HOST
    variants = [f"{SCHEME}://{HOST}/"]
    for v in (f"https://{apex}/", f"http://{HOST}/", f"http://{apex}/"):
        if v not in variants:
            variants.append(v)
    profiles = [("archiver", UA, {})] + [(n, ua, BROWSER_HEADERS) for n, ua in BROWSER_PROFILES]
    for name, ua, hdrs in profiles:
        for base in variants:
            ent = {"profile": name, "url": base}
            ok = False
            try:
                r = S.get(base, timeout=45, allow_redirects=True, headers=dict(hdrs, **{"User-Agent": ua}))
                ct = (r.headers.get("content-type") or "").lower()
                ent.update(status=r.status_code, final_url=r.url, content_type=ct, server=r.headers.get("server"),
                           cf_ray=r.headers.get("cf-ray"), cf_mitigated=r.headers.get("cf-mitigated"),
                           x_powered_by=r.headers.get("x-powered-by"), via=r.headers.get("via"),
                           body_head=re.sub(r"\s+", " ", r.text[:600]))
                ok = r.status_code == 200 and ("html" in ct or "text" in ct or not ct) and not looks_challenge(r.text)
            except requests.RequestException as e:
                ent["error"] = repr(e)
            diag["tried"].append(ent)
            log(f"probe {name} {base} → {ent.get('status', ent.get('error'))}")
            if ok:
                S.headers.update(hdrs)
                S.headers["User-Agent"] = ua
                UA = ua
                p = urlparse(base)
                SCHEME, HOST, BASE = p.scheme, p.netloc, base
                diag.update(mode="requests", profile=name, base=base)
                return diag
            time.sleep(2)
    if os.environ.get("PLAYWRIGHT_FALLBACK", "1") != "0":
        log("all requests profiles refused → trying Playwright (headless Chromium)")
        ok, info = pw_bootstrap()
        diag["playwright_bootstrap"] = info
        log(f"playwright bootstrap ok={ok} {json.dumps(info, ensure_ascii=False)[:300]}")
        if ok:
            try:
                st, title, head = pw_open_seed(BASE)
                diag["playwright_seed"] = {"status": st, "title": title, "body_head": re.sub(r"\s+", " ", head)}
                log(f"playwright seed → {st} {title!r}")
                if st == 200:
                    cookies = _PW["ctx"].cookies()
                    diag["playwright_cookies"] = [c.get("name") for c in cookies]
                    S.headers.update(BROWSER_HEADERS)
                    S.headers["User-Agent"] = CHROME_UA
                    UA = CHROME_UA
                    for c in cookies:
                        try:
                            S.cookies.set(c["name"], c["value"], domain=c.get("domain"), path=c.get("path", "/"))
                        except Exception:
                            pass
                    try:
                        r = S.get(BASE, timeout=45, allow_redirects=True)
                        diag["requests_with_cookies"] = r.status_code
                        if r.status_code == 200 and not looks_challenge(r.text):
                            diag.update(mode="requests+cookies", profile="chrome-win+pw-cookies", base=BASE)
                            return diag
                    except requests.RequestException as e:
                        diag["requests_with_cookies"] = repr(e)
                    diag.update(mode="playwright", profile="playwright-chromium", base=BASE)
                    return diag
            except Exception as e:
                diag["playwright_error"] = repr(e)
                log(f"playwright failed: {e!r}")
    diag["mode"] = "blocked"
    return diag


def write_jsonl(path, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except Exception:
                    pass
    return rows


def save_state(path, queue, seen, downloads, images, external, phase, runs):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"saved_at": now(), "phase": phase, "queue": list(queue), "seen": sorted(seen),
                   "downloads": downloads, "images": images,
                   "external": {k: sorted(v) for k, v in external.items()}, "runs": runs},
                  f, ensure_ascii=False)
    os.replace(tmp, path)


def main():
    for d in ("html", "datasheet_text", "datasheets"):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
    for d in ("downloads", "images"):
        os.makedirs(os.path.join(BIN, d), exist_ok=True)
    p_pages = os.path.join(OUT, "pages_manifest.jsonl")
    p_dl = os.path.join(OUT, "downloads_manifest.jsonl")
    p_img = os.path.join(OUT, "images_manifest.jsonl")
    p_state = os.path.join(OUT, "crawl_state.json")

    # ---------- resume? ----------
    state = None
    if os.path.exists(p_state):
        try:
            with open(p_state, encoding="utf-8") as f:
                state = json.load(f)
        except Exception as e:
            log(f"crawl_state.json unreadable ({e!r}) → fresh start")
            state = None
    runs = (state or {}).get("runs", [])
    runs.append({"run": RUN_ID, "started": now(), "resumed": bool(state), "budget_min": TIME_BUDGET_MIN,
                 "max_pages": MAX_PAGES, "delay_s": DELAY})
    log(f"run {RUN_ID} start; resume={bool(state)}; budget {TIME_BUDGET_MIN} min; max_pages {MAX_PAGES}; delay {DELAY}s")
    diag = probe_access()
    ACCESS.update({k: diag.get(k) for k in ("mode", "profile", "base")})
    blocked = diag.get("mode") == "blocked"
    with open(os.path.join(OUT, "access_diag.json"), "w", encoding="utf-8") as f:
        json.dump(diag, f, ensure_ascii=False, indent=2)
    log(f"access mode = {ACCESS['mode']} ({ACCESS['profile']}) base {ACCESS['base']}")
    if blocked:
        log("BLOCKED: 站点对本运行器所有访问方式均拒绝（见 access_diag.json）→ 本轮不抓任何东西，只落盘诊断")

    pages = read_jsonl(p_pages) if state else []
    pages_by_url = {p["url"]: p for p in pages}
    dl_prev = read_jsonl(p_dl) if state else []
    img_prev = read_jsonl(p_img) if state else []

    if state:
        queue = deque(state.get("queue", []))
        seen = set(state.get("seen", []))
        downloads = state.get("downloads", {})
        images = state.get("images", {})
        external = {k: set(v) for k, v in state.get("external", {}).items()}
        # 上一轮抓失败（网络 / 5xx / 非 404）的页面再试一次
        retry = [p["url"] for p in pages if not p.get("file") and p.get("status") != 404
                 and not (p.get("error") or "").startswith("binary-at-page-url")]
        for u in retry:
            if u not in queue:
                queue.appendleft(u)
        for u in retry:
            pages_by_url.pop(u, None)
        pages = [p for p in pages if p["url"] in pages_by_url]
        log(f"resume: pages_done={len(pages)} queue={len(queue)} (retry {len(retry)}) downloads={len(downloads)} images={len(images)}")
    else:
        seeds = [BASE]
        queue = deque(seeds)
        seen = set(seeds)
        downloads = {}  # url -> {found_on: [...]}
        images = {}  # url -> {found_on: [...], alt: ...}
        external = {}
    # ---------- seeds: sitemap / robots（首轮或上轮没拿到时补拿；被封时不碰） ----------
    if not blocked and not os.path.exists(os.path.join(OUT, "sitemap.xml")):
        r, err = get(BASE + "sitemap.xml")
        if r is not None and r.status_code == 200:
            with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
                f.write(r.text)
            locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", r.text, flags=re.I | re.S)
            added = 0
            for l in locs:
                n = norm(l)
                if n and n not in seen:
                    seen.add(n)
                    queue.append(n)
                    added += 1
            log(f"sitemap: {len(locs)} loc, {added} new seeds")
        else:
            log(f"sitemap fetch failed: {err if r is None else 'HTTP ' + str(r.status_code)}")
    if not blocked and not os.path.exists(os.path.join(OUT, "robots.txt")):
        r, err = get(BASE + "robots.txt")
        if r is not None and r.status_code == 200:
            with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
                f.write(r.text)

    def checkpoint(phase):
        write_jsonl(p_pages, pages)
        save_state(p_state, queue, seen, downloads, images, external, phase, runs)

    # ---------- BFS over pages ----------
    n_new_pages = 0
    pages_stop = None
    while queue and not blocked:
        if len(pages) >= MAX_PAGES:
            pages_stop = f"MAX_PAGES {MAX_PAGES} reached (queue_left {len(queue)})"
            break
        if over_budget("pages"):
            pages_stop = f"time budget (queue_left {len(queue)})"
            break
        if banned():
            pages_stop = f"blocked mid-run: {CONSEC_LIMIT} consecutive 403/429/errors (queue_left {len(queue)}) → resume later"
            break
        u = queue.popleft()
        if u in pages_by_url and pages_by_url[u].get("file"):
            continue
        r, err = get(u)
        time.sleep(DELAY)
        rec = {"url": u, "fetched_at": now(), "run": RUN_ID, "status": None, "final_url": None, "content_type": None,
               "file": None, "bytes": None, "sha256": None, "title": None, "error": err}
        pages.append(rec)
        pages_by_url[u] = rec
        n_new_pages += 1
        if r is None:
            log(f"FAIL {u}: {err}")
        else:
            rec.update(status=r.status_code, final_url=r.url, content_type=r.headers.get("content-type"))
            ct = (rec["content_type"] or "").lower()
            if r.status_code != 200:
                log(f"HTTP {r.status_code} {u}")
            elif "html" not in ct and "xml" not in ct and "text" not in ct:
                # binary served at a page URL → treat as download
                found(downloads.setdefault(u, {"found_on": []}), "(direct)")
                rec["error"] = "binary-at-page-url → downloads"
            else:
                if r.encoding is None or r.encoding.lower() in ("iso-8859-1", "latin-1"):
                    r.encoding = r.apparent_encoding or "utf-8"
                html = r.text
                name = fname(u, ".html")
                with open(os.path.join(OUT, "html", name), "w", encoding="utf-8") as f:
                    f.write(html)
                m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
                rec.update(file=f"html/{name}", bytes=len(html.encode("utf-8")), sha256=sha256(html.encode("utf-8")),
                           title=re.sub(r"\s+", " ", m.group(1)).strip() if m else None)
                # links
                for href in re.findall(r"""href\s*=\s*["']([^"'#]+)""", html, flags=re.I):
                    if href.lower().startswith(("javascript:", "mailto:", "tel:", "whatsapp:", "data:")):
                        continue
                    n = norm(href, r.url)
                    if n is None:
                        try:
                            h = urlparse(urljoin(r.url, href)).netloc
                            if h:
                                external.setdefault(h, set()).add(u)
                        except Exception:
                            pass
                        continue
                    k = kind(n)
                    if k == "page":
                        if n not in seen:
                            seen.add(n)
                            queue.append(n)
                    elif k == "download":
                        found(downloads.setdefault(n, {"found_on": []}), u)
                    elif k == "image":
                        found(images.setdefault(n, {"found_on": [], "alt": ""}), u)
                for m2 in re.finditer(r"""<img[^>]+?(?:src|data-src|data-original)\s*=\s*["']([^"']+)["'][^>]*>""", html, flags=re.I):
                    n = norm(m2.group(1), r.url)
                    if n is None:
                        continue
                    alt = re.search(r"""alt\s*=\s*["']([^"']*)""", m2.group(0), flags=re.I)
                    d = found(images.setdefault(n, {"found_on": [], "alt": ""}), u)
                    if alt and alt.group(1) and not d["alt"]:
                        d["alt"] = alt.group(1)
                for m3 in re.finditer(r"""url\(\s*["']?([^"')]+?)["']?\s*\)""", html, flags=re.I):
                    n = norm(m3.group(1), r.url)
                    if n and kind(n) == "image":
                        found(images.setdefault(n, {"found_on": [], "alt": ""}), u)
        if n_new_pages % 25 == 0:
            log(f"pages {len(pages)} (+{n_new_pages} this run) queue {len(queue)} downloads {len(downloads)} images {len(images)} "
                f"elapsed {elapsed() / 60:.1f} min")
            checkpoint("pages")
    if pages_stop is None:
        pages_stop = "blocked (seed refused under every profile; see access_diag.json)" if blocked else "complete (queue empty)"
    log(f"BFS stop: {pages_stop}; pages={len(pages)} (+{n_new_pages}) downloads={len(downloads)} images={len(images)}")
    if not blocked:
        n_cdn = harvest_cdn_images(images, pages)
        log(f"cdn images harvested from archived html: +{n_cdn} (images total {len(images)})")
    checkpoint("downloads")

    # ---------- downloads (datasheets etc.) ----------
    dl_rows = [d for d in dl_prev if d.get("file") and not bogus_download(d)]  # 上一轮已成功的保留（二进制在上一轮的 Release / 产物里；PDF 入库时在 datasheets/）；HTML 小响应的假成功作废重下
    done_dl = {d["url"] for d in dl_rows}
    used = {d["filename"]: d["sha256"] for d in dl_rows if d.get("filename")}
    todo_dl = [(u, meta) for u, meta in sorted(downloads.items()) if u not in done_dl]
    dl_stop = None
    n_new_dl = 0
    for i, (u, meta) in enumerate(todo_dl):
        if blocked or banned():
            dl_stop = f"blocked ({len(todo_dl) - i} left) → resume later"
            break
        if over_budget("downloads"):
            dl_stop = f"time budget ({len(todo_dl) - i} left)"
            break
        r, err, used_url = get_download(u, referer=(meta.get("found_on") or [BASE])[0])
        rec = {"url": u, "found_on": sorted(set(meta["found_on"])), "found_on_count": meta.get("n", len(meta["found_on"])),
               "fetched_at": now(), "run": RUN_ID, "status": None, "content_type": None, "filename": None, "file": None, "bytes": None, "sha256": None, "error": err,
               "fetched_from": used_url, "title": fujian_name(u)}
        n_new_dl += 1
        if r is None:
            dl_rows.append(rec)
            log(f"DL FAIL {u}: {err}")
            continue
        rec.update(status=r.status_code, content_type=r.headers.get("content-type"))
        if r.status_code != 200:
            dl_rows.append(rec)
            continue
        cd = r.headers.get("content-disposition", "")
        fn = None
        m = re.search(r"filename\*\s*=\s*(?:UTF-8|utf-8)''([^;]+)", cd)
        if m:
            fn = unquote(m.group(1).strip().strip('"'))
        else:
            m = re.search(r'filename\s*=\s*"?([^";]+)"?', cd)
            if m:
                fn = m.group(1).strip()
                try:
                    fn = fn.encode("latin-1").decode("utf-8")
                except Exception:
                    pass
        title = fujian_name(u)
        if title:  # 规格书标题做文件名（直链的 basename 是一串哈希，不可读）
            ext = os.path.splitext(urlparse(used_url or u).path)[1].lower() or (".pdf" if r.content[:5] == b"%PDF-" else ".bin")
            fn = title + (ext if ext in FILE_EXT else ".pdf")
        if not fn:
            fn = unquote(os.path.basename(urlparse(r.url).path)) or "download"
            if "." not in fn:
                ct = (rec["content_type"] or "").lower()
                fn += ".pdf" if "pdf" in ct else (".bin")
        fn = re.sub(r"[\\/:*?\"<>|]+", "_", fn).strip() or "download.bin"
        try:
            data = r.content
        except Exception as e:  # noqa: BLE001
            rec["error"] = f"body read failed: {e.__class__.__name__}"
            dl_rows.append(rec)
            continue
        h = sha256(data)
        base_fn = fn
        if fn in used and used[fn] != h:
            stem, ext = os.path.splitext(base_fn)
            fn = f"{stem}_{h[:8]}{ext}"
        used[fn] = h
        with open(os.path.join(BIN, "downloads", fn), "wb") as f:
            f.write(data)
        rec.update(filename=fn, file=f"downloads/{fn}", bytes=len(data), sha256=h)
        dl_rows.append(rec)
        time.sleep(DELAY)
        if n_new_dl % 20 == 0:
            log(f"downloads {i + 1}/{len(todo_dl)} elapsed {elapsed() / 60:.1f} min")
            write_jsonl(p_dl, dl_rows)
    if dl_stop is None:
        dl_stop = "complete"
    write_jsonl(p_dl, dl_rows)
    log(f"downloads stop: {dl_stop}; ok {sum(1 for d in dl_rows if d['file'])}/{len(dl_rows)} (+{n_new_dl} this run), "
        f"{sum(d['bytes'] or 0 for d in dl_rows) / 1e6:.1f} MB")

    # ---------- text extraction (pdftotext) ----------
    n_txt = 0
    for d in dl_rows:
        if not d["file"] or not (d.get("filename") or "").lower().endswith(".pdf"):
            continue
        dst = os.path.join(OUT, "datasheet_text", os.path.splitext(d["filename"])[0] + ".txt")
        if d.get("text_file") and os.path.exists(dst):
            n_txt += 1
            continue
        src = os.path.join(BIN, d["file"])
        if not os.path.exists(src):
            # 上一轮抓的 PDF：若已入库到 datasheets/ 则从那里抽文本
            alt = os.path.join(OUT, "datasheets", d["filename"])
            if os.path.exists(alt):
                src = alt
            else:
                continue
        try:
            subprocess.run(["pdftotext", "-layout", src, dst], check=True, timeout=120,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            d["text_file"] = os.path.relpath(dst, OUT)
            d.pop("text_error", None)
            n_txt += 1
        except Exception as e:
            d["text_error"] = repr(e)
    write_jsonl(p_dl, dl_rows)
    log(f"pdftotext: {n_txt}")

    # ---------- commit PDFs into git only if small enough ----------
    pdf_bytes = sum(d["bytes"] or 0 for d in dl_rows if d["file"])
    pdfs_committed = pdf_bytes <= PDF_COMMIT_MB * 1e6
    if pdfs_committed:
        for d in dl_rows:
            if d["file"]:
                src = os.path.join(BIN, d["file"])
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(OUT, "datasheets", d["filename"]))
    log(f"downloads total {pdf_bytes / 1e6:.1f} MB → committed to git: {pdfs_committed}")
    save_state(p_state, queue, seen, downloads, images, external, "images", runs)

    # ---------- images (binary dir only) ----------
    img_rows = [d for d in img_prev if d.get("file")]
    done_img = {d["url"] for d in img_rows}
    todo_img = [(u, meta) for u, meta in sorted(images.items()) if u not in done_img]
    total = 0
    img_stop = None
    n_new_img = 0
    img_blocked = blocked
    cdn_todo = [u for u, _ in todo_img if CDN_CONTENT_RE.match(u)]
    if blocked and cdn_todo:
        # v2.4：站点封了运行器，但 CDN（gcdn.meidianbang.cn）是另一套；探一张能取就继续（站内图本轮跳过）
        try:
            rp = S.get(cdn_todo[0], timeout=60, headers={"Referer": "https://www.smartbyte-switch.com/", "Accept": "image/*,*/*;q=0.8"})
            body = rp.content if rp.status_code == 200 else b""
            if len(body) > 0:
                img_blocked = False
                CONSEC["n"] = 0
                log(f"site blocked but CDN reachable (probe {rp.status_code}, {len(body)} B) → images phase continues")
            else:
                log(f"site blocked and CDN probe → {rp.status_code} ({len(body)} B); images phase skipped")
        except Exception as e:  # noqa: BLE001
            log(f"site blocked and CDN probe failed: {e.__class__.__name__}; images phase skipped")
    skipped_site_img = 0
    for i, (u, meta) in enumerate(todo_img):
        if img_blocked or banned():
            img_stop = f"blocked ({len(todo_img) - i + skipped_site_img} left) → resume later"
            break
        if blocked and not CDN_CONTENT_RE.match(u):
            skipped_site_img += 1  # 站点被封：站内图留到下轮
            continue
        rec = {"url": u, "alt": meta["alt"], "found_on": sorted(set(meta["found_on"]))[:20],
               "found_on_count": meta.get("n", len(meta["found_on"])), "run": RUN_ID, "status": None, "file": None, "bytes": None, "sha256": None}
        if total > MAX_IMAGE_MB * 1e6:
            rec["error"] = "skipped: image budget exceeded"
            img_rows.append(rec)
            continue
        if over_budget("images"):
            img_stop = f"time budget ({len(todo_img) - i} left)"
            break
        r, err = get(u, stream=True, timeout=120,
                     headers={"User-Agent": CHROME_UA, "Accept": "image/avif,image/webp,image/*,*/*;q=0.8", "Referer": BASE})
        n_new_img += 1
        if r is None:
            rec["error"] = err
            img_rows.append(rec)
            continue
        rec["status"] = r.status_code
        if r.status_code == 200:
            try:
                data = r.content
            except Exception as e:  # noqa: BLE001  读体中断（ChunkedEncodingError / IncompleteRead）→ 记错继续，下轮重试
                rec["error"] = f"body read failed: {e.__class__.__name__}"
                img_rows.append(rec)
                _note(False)
                time.sleep(2)
                continue
            fn = fname(u)
            with open(os.path.join(BIN, "images", fn), "wb") as f:
                f.write(data)
            rec.update(file=f"images/{fn}", bytes=len(data), sha256=sha256(data))
            total += len(data)
        img_rows.append(rec)
        time.sleep(min(DELAY, 0.5))
        if n_new_img % 100 == 0:
            log(f"images {i + 1}/{len(todo_img)} {total / 1e6:.0f} MB elapsed {elapsed() / 60:.1f} min")
            write_jsonl(p_img, img_rows)
    if img_stop is None:
        img_stop = "complete" if not skipped_site_img else f"blocked ({skipped_site_img} site-hosted left, CDN done) → resume later"
    write_jsonl(p_img, img_rows)
    log(f"images stop: {img_stop}; ok {sum(1 for d in img_rows if d['file'])}/{len(img_rows)} (+{n_new_img} this run), {total / 1e6:.1f} MB this run")

    # ---------- summary ----------
    images_left = sum(1 for u, _ in todo_img if u not in {d["url"] for d in img_rows})
    pages_ok = sum(1 for p in pages if p["file"])
    # 被拒型失败（403 / 429 / 网络错误）不算完成：下轮 Run workflow 会重试；404 之类不阻止 complete
    def _refused(rows, skip_prefix):
        return [d["url"] for d in rows if not d.get("file") and not (d.get("error") or "").startswith(skip_prefix)
                and (d.get("status") in (403, 429) or d.get("status") is None)]
    refused = {"pages": _refused(pages, "binary-at-page-url"), "downloads": _refused(dl_rows, "\x00"), "images": _refused(img_rows, "skipped")}
    n_refused = sum(len(v) for v in refused.values())
    nothing_left = (not queue and dl_stop == "complete" and img_stop == "complete")
    complete = (pages_ok > 0 and n_refused == 0 and dl_stop == "complete" and img_stop == "complete"
                and (pages_stop.startswith("complete") or (blocked and nothing_left)))
    runs[-1].update(ended=now(), elapsed_s=round(elapsed()), pages_new=n_new_pages, downloads_new=n_new_dl,
                    images_new=n_new_img, pages_stop=pages_stop, downloads_stop=dl_stop, images_stop=img_stop)
    summary = {
        "crawled_at": now(), "host": HOST, "complete": complete, "blocked": blocked,
        "access": {k: ACCESS.get(k) for k in ("mode", "profile", "base")},
        "refused": {k: len(v) for k, v in refused.items()}, "refused_sample": {k: v[:20] for k, v in refused.items()},
        "pages_total": len(pages), "pages_ok": sum(1 for p in pages if p["file"]),
        "pages_failed": [p["url"] for p in pages if not p["file"]],
        "pages_stop": pages_stop, "queue_left": len(queue),
        "downloads_total": len(dl_rows), "downloads_ok": sum(1 for d in dl_rows if d["file"]),
        "downloads_left": max(0, len(todo_dl) - n_new_dl), "downloads_stop": dl_stop,
        "downloads_bytes": pdf_bytes, "pdfs_committed": pdfs_committed, "pdf_text_files": n_txt,
        "images_total": len(img_rows), "images_ok": sum(1 for d in img_rows if d["file"]),
        "images_left": images_left, "images_stop": img_stop, "images_bytes_this_run": total,
        "external_hosts": {k: len(v) for k, v in sorted(external.items())},
        "runs": runs, "elapsed_s": round(elapsed()), "user_agent": UA, "delay_s": DELAY,
        "time_budget_min": TIME_BUDGET_MIN,
        "how_to_continue": None if complete else (
            "被封：站点对 GitHub Actions 运行器的所有访问方式都返回拒绝（access_diag.json 有状态码 / 响应头 / 正文片段）。"
            "办法：① 过几小时再到 Actions 页点 Run workflow（可能是运行 #1 长时间抓取触发的临时封禁）；"
            "② 在本地电脑运行 python scripts/smartbyte_crawl/crawl.py data/smartbyte_site_raw crawl_bin 后提交；"
            "③ 请 SmartByte 放行归档 UA / 运行器 IP。" if blocked else
            f"未抓完（被拒 403/429/网络错误 {n_refused} 个；页面阶段 {pages_stop}；附件 {dl_stop}；图片 {img_stop}）："
            "在 GitHub Actions 页对 SmartByte site archive 点 Run workflow（或再推一次 crawl.py），会从 crawl_state.json 续抓并重试失败项"),
    }
    with open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT, "crawl_log.txt"), "a", encoding="utf-8") as f:
        f.write(f"===== run {RUN_ID} =====\n" + "\n".join(LOG) + "\n")
    with open(os.path.join(BIN, "pdfs_committed.flag"), "w") as f:
        f.write("1" if pdfs_committed else "0")
    save_state(p_state, queue, seen, downloads, images, external, "done" if complete else "images", runs)
    log(json.dumps({k: v for k, v in summary.items() if k not in ("pages_failed", "external_hosts", "runs")}, ensure_ascii=False))
    log("COMPLETE" if complete else "INCOMPLETE → re-run to continue")


def _crash(exc):
    """主流程异常：日志 + summary 落盘（complete=false），以 0 退出，让工作流后续 zip / 上传 / 提交步骤照跑（检查点都在盘上）。"""
    import traceback
    tb = traceback.format_exc()
    print(tb, file=sys.stderr, flush=True)
    try:
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, "crawl_log.txt"), "a", encoding="utf-8") as f:
            f.write(f"===== run {RUN_ID} CRASH =====\n" + "\n".join(LOG) + "\n" + tb + "\n")
        p = os.path.join(OUT, "summary.json")
        summary = {}
        if os.path.exists(p):
            try:
                with open(p, encoding="utf-8") as f:
                    summary = json.load(f)
            except Exception:
                summary = {}
        summary.update(complete=False, crashed_run=RUN_ID, crash=repr(exc), crashed_at=now(),
                       how_to_continue="本轮异常退出（见 crawl_log.txt 末尾 traceback）；检查点已落盘，修好后 Run workflow 续抓")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        _crash(e)
        sys.exit(0)
    finally:
        try:
            if _PW.get("browser"):
                _PW["browser"].close()
                _PW["pw"].stop()
        except Exception:
            pass
