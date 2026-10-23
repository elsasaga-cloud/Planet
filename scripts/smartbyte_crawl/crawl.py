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
v2.5（2026-10-21，运行 #7 成果丢失之后）：Actions 的 checkout 停在触发提交而非分支最新；两轮排队时后一轮的提交步骤
  与前一轮的提交冲突（工作流里 pull --rebase 失败被 || true 吞掉 → push 成空操作，本轮只剩 Release 附件）。
  开抓前先把工作区同步到分支最新（拿最新检查点、让提交步骤干净落地）；本地运行不受影响。
v2.6（2026-10-21，运行 #8 图片 1493/1493 收齐但 Release 附件被逐轮 --clobber 覆盖、前 900 张二进制只剩 90 天期限的 Actions 产物之后）：
  图片二进制也入 git（OUT/images/，总量 ≤ IMG_COMMIT_MB=400 才拷；型号页可直接内嵌显示）；
  清单里"已完成"的图片若二进制既不在 BIN 也不在 OUT/images，则视为未完成重新下载，保证入库齐全。
v2.6.1（2026-10-21，运行 #9 图片 1487/1493 入 git、6 张 CDN 读体中断之后）：图片读体失败就地重试一次（隔 3 s）再记错。
v3.0（2026-10-21，T25：Saga 另两家供应商 HRUI / Hohunet 官网也要入库，而工作流 yml 不可改）：
  ① 通用化：站点由 CRAWL_HOST 决定；sitemap 索引（<loc> 指向子 sitemap / 产品 / 图片）当页面抓到后展开；
     <img> 多收 data-lazy-src / data-large_image；WordPress / 建站 CMS 的垃圾链接（feed / wp-json / ?replytocom / ?p= / 购物车等）不入队。
  ② 入库规则改为按文件：文档类（pdf/doc/xls/ppt…）单文件 ≤60 MB、固件压缩包 ≤15 MB、任何文件 ≤95 MB（GitHub 单文件上限）且累计 ≤PDF_COMMIT_MB
     才拷进 OUT/datasheets；图片累计 ≤IMG_COMMIT_MB 才拷进 OUT/images；图片按「出现页数少的先抓」排序（产品图优先于页眉 logo）。
  ③ 编排：在 GitHub Actions 里以工作流固定命令（SmartByte）启动且 SmartByte 已 complete 时跳过重抓，
     然后顺序以子进程抓 EXTRA_SITES（HRUI → Hohunet，各自 OUT / BIN / 预算），结束后 git add 它们的 OUT 目录，
     由工作流原有的提交步骤一并提交。CRAWL_RECRAWL=1 可强制重抓 SmartByte；CRAWL_EXTRA_SITES=0 可关闭编排。
v3.1（2026-10-21，运行 #11 之后：HRUI 411 页 / 83 附件 / 919 图落地，但产品只到手 56/182）：
  ① HRUI 类目页的产品列表由前端 AJAX 拉取（/web/api.php?act=getdata&p=&limit=8&sortid=&tj=&lanstr=en，8 个类目 sortid 固定），
     静态 HTML 里没有产品链接 → 站点钩子：逐类目翻页调 API，原样存 OUT/api/*.json，产品页 /<类目>/<id>.html 入队；
  ② <img src> 指向目录（以 / 结尾，如 HRUI 的 /web/userfiles/banner/）不算图片，也不计入「被拒」——运行 #11 就卡在这 1 个 403 上 complete=false。
v3.2（2026-10-22，T29-U13：Simon 要求把 SmartByte / HRUI / Hohunet 官网再抓一遍找新信息，且结果全部入库）：
  ① 复抓轮次：CRAWL_BASE=<上一轮整站目录> 时，本轮写到新的 OUT（html 全量照存），逐 URL 与基线比对并写 diff.json / diff.md
     （页面：新增 / 正文有变 / 仅标记变 / 未变 / 消失 / 未抓到；附件 & 图片：新增 / 变化 / 未变 / 消失）；
     二进制内容与基线相同（sha256 一致）的附件 / 图片不再拷入 git（记 same_as_base），只有新增 / 变化的才入库，避免重复体积。
  ② 编排：scripts/smartbyte_crawl/RECRAWL 里 ROUND=YYYYMMDD（可选 SITES=smartbyte,hrui,hohunet）→ 工作流固定命令跑完原逻辑后，
     三站各起一子进程写到 data/site_recrawl/<ROUND>/<site>/；未完成的站再推一次 crawl.py 即从该目录的 crawl_state.json 续抓；
     已 complete 的站跳过。预算按 45/35/20 分配剩余时间。
  ③ 新增整站：hrgdkj.com（HRUI 中文站）、hohunet.cn（Hohunet 中文站）、smartbyte.com.cn（SmartByte 第二域名，可能已停用）进 EXTRA_SITES；
     hrui_cn 有通用 CMS 列表 API 钩子（类目 id 从首页收集）。
v3.3（2026-10-23，T29-U18：成单客户活跃平台监控）：
  scripts/web_watch/RUN_ON_CRAWL 含 WATCH_ONLY=1 时，本工作流的这次运行只执行 scripts/web_watch/watch.py（19 家成单客户 + NYNEX 的
  RSS / 网页 / sitemap / GitHub / JSON 源抓取 + 比对 + 提交 data/customer_watch/），不爬站、不动 data/smartbyte_site_raw。
  改回 WATCH_ONLY=0 即恢复 v3.2 行为。监控触发序号 #1：2026-10-23 首轮基线（02:54Z，63 源 / 15 失败）；#2：2026-10-23T03:04:49Z 修正 15 个失败源后的第二轮；
  #3：2026-10-23 U19 v3.4 —— watch.py 合并 A/B 面层（targets_auto.json，1,100+ 家 / 2,700 源，12 线程），RUN_ON_CRAWL 新增 LAYER=，首次全层运行 = A/B 基线。
  #4：2026-10-23 ≈05:00Z 只跑成单层（LAYER=成单）验证 YouTube 修正（浏览器 UA + 同意 cookie + 全局 2 s 限速 + 404 重试；https 证书错降级 http）。
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
SITE = os.environ.get("CRAWL_SITE") or ("smartbyte" if HOST.lower().endswith("smartbyte-switch.com") else HOST.lower())
# v3.0：工作流命令固定抓 SmartByte；其后顺序抓这些站（T25：Saga 的另两家供应商）
EXTRA_SITES = [
    {"site": "hrui", "host": "www.hruitech.com", "out": "data/hrui_site_raw", "bin": "crawl_bin_hrui"},
    {"site": "hohunet", "host": "hohunet.com", "out": "data/hohunet_site_raw", "bin": "crawl_bin_hohunet"},
    # v3.2（T29-U13）：三家的中文站 / 第二域名也整站入库（smartbyte.com.cn 2026-10-22 沙箱外抓取失败，可能已停用 → 交运行器探路，blocked 就只落诊断）
    {"site": "hrui_cn", "host": "www.hrgdkj.com", "out": "data/hrui_cn_site_raw", "bin": "crawl_bin_hrui_cn"},
    {"site": "hohunet_cn", "host": "hohunet.cn", "out": "data/hohunet_cn_site_raw", "bin": "crawl_bin_hohunet_cn"},
    {"site": "smartbyte_cn", "host": "www.smartbyte.com.cn", "out": "data/smartbyte_cn_site_raw", "bin": "crawl_bin_smartbyte_cn"},
]
# 不入队的垃圾 / 无限组合链接（WordPress、WooCommerce、建站 CMS 常见）
JUNK_RE = re.compile(r"(/feed/?$|/feed/|/wp-json|xmlrpc\.php|wp-login|wp-admin|/wp-includes/|[?&](?:replytocom|p|share|add-to-cart|orderby|"
                     r"attachment_id|s|min_price|max_price|filter_[a-z_]+|product-page|preview|customize_changeset_uuid)=|"
                     r"/cart/?$|/checkout/?$|/my-account|/comments/|/trackback|/print/?$|/amp/?$)", re.I)
MAX_PAGES = int(os.environ.get("MAX_PAGES", "1500"))
DELAY = float(os.environ.get("DELAY", "1.2"))
MAX_IMAGE_MB = float(os.environ.get("MAX_IMAGE_MB", "600"))
PDF_COMMIT_MB = float(os.environ.get("PDF_COMMIT_MB", "120"))
IMG_COMMIT_MB = float(os.environ.get("IMG_COMMIT_MB", "400"))  # 图片总量不超过它就拷进 OUT/images 入 git
TIME_BUDGET_MIN = float(os.environ.get("TIME_BUDGET_MIN", "140"))
# v3.2 复抓：CRAWL_BASE=上一轮整站归档目录（基线）；RECRAWL 文件驱动编排
BASE_OUT = os.environ.get("CRAWL_BASE") or None
RECRAWL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RECRAWL")
RECRAWL_ROOT = "data/site_recrawl"
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
    if path.endswith(IMG_EXT) or path.endswith(FILE_EXT):
        pass  # 图片 / 附件不受垃圾链接规则影响
    elif JUNK_RE.search(u):
        return "skip"
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


def _sync_to_branch_tip():
    """仅在 GitHub Actions 里：把检出同步到分支最新提交（见 v2.5 说明）。"""
    if not os.environ.get("GITHUB_ACTIONS"):
        return
    ref = os.environ.get("GITHUB_REF_NAME") or ""
    if not ref:
        return
    try:
        subprocess.run(["git", "fetch", "-q", "origin", ref], check=True, timeout=180)
        head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, timeout=30).stdout.strip()
        tip = subprocess.run(["git", "rev-parse", "FETCH_HEAD"], capture_output=True, text=True, timeout=30).stdout.strip()
        if head and tip and head != tip:
            subprocess.run(["git", "checkout", "-q", "--detach", tip], check=True, timeout=120)
            log(f"synced checkout {head[:7]} → branch tip {tip[:7]} ({ref})")
        else:
            log(f"checkout already at branch tip {head[:7]}")
    except Exception as e:  # noqa: BLE001
        log(f"sync to branch tip skipped: {e.__class__.__name__}: {e}")


# v3.1：HRUI 官网 8 个产品类目（类目页 JS：init(count) + $.get('/web/api.php?act=getdata',{p,limit:8,sortid,tj,lanstr:'en'})）
HRUI_CATS = {64: "poe-switch", 76: "ethernet-switch", 182: "managed-switch", 184: "industrial-poe-switch",
             186: "industrial-ethernet-switch", 188: "optical-fiber-converter", 190: "poe-accessory", 192: "wireless-bridge"}


def hrui_api_seeds(queue, seen):
    """逐类目翻页调 HRUI 的产品列表 API，原样存 OUT/api/，并把产品详情页 /<类目>/<id>.html 入队。每轮都跑（≈30 次请求），幂等。"""
    os.makedirs(os.path.join(OUT, "api"), exist_ok=True)
    items_all, added, calls = [], 0, 0
    for sid, cat in HRUI_CATS.items():
        p = 1
        while p <= 60:
            u = f"{BASE}web/api.php?act=getdata&p={p}&limit=8&sortid={sid}&tj=&lanstr=en"
            r, err = get(u)
            calls += 1
            time.sleep(DELAY)
            if r is None or r.status_code != 200:
                log(f"hrui api sortid={sid} p={p}: {err if r is None else 'HTTP ' + str(r.status_code)}")
                break
            try:
                items = json.loads(r.text)
            except Exception as e:  # noqa: BLE001
                log(f"hrui api sortid={sid} p={p}: not json ({e!r}): {r.text[:120]!r}")
                break
            if not isinstance(items, list) or not items:
                break
            with open(os.path.join(OUT, "api", f"getdata_sort{sid}_p{p}.json"), "w", encoding="utf-8") as f:
                f.write(r.text)
            for it in items:
                if not isinstance(it, dict):
                    continue
                iid = str(it.get("id") or "").strip()
                if not iid.isdigit():
                    continue
                items_all.append({"id": iid, "sortid": sid, "classid": it.get("classid"), "category": cat,
                                  "title": it.get("title"), "title2": it.get("title2"), "product_sn": it.get("product_sn"),
                                  "url": f"{BASE}{cat}/{iid}.html"})
                n = norm(f"{BASE}{cat}/{iid}.html")
                if n and n not in seen:
                    seen.add(n)
                    queue.append(n)
                    added += 1
            if len(items) < 8:
                break
            p += 1
    with open(os.path.join(OUT, "api", "products_index.json"), "w", encoding="utf-8") as f:
        json.dump(items_all, f, ensure_ascii=False, indent=1)
    log(f"hrui api: {calls} calls, {len(items_all)} products listed, {added} new product pages queued")
    return added


def hrui_cn_api_seeds(queue, seen):
    """v3.2：中文站 hrgdkj.com 与英文站同一套建站 CMS（/web/index.php?topclassid=&classid=&id=、/web/api.php?act=getdata）。
    类目 id 未知 → 从首页 HTML 里收集 classid / sortid / topclassid 数字，逐个当 sortid 调列表 API（lanstr 试 cn / en / 空），
    返回非空 JSON 列表的原样存 OUT/api/，条目里像 URL 的字段入队，否则按 CMS 详情页格式 web/index.php?topclassid=0&classid=<sortid>&id=<id> 入队。
    全部失败也无妨（BFS 照常）。"""
    os.makedirs(os.path.join(OUT, "api"), exist_ok=True)
    r, err = get(BASE)
    if r is None or r.status_code != 200:
        log(f"hrui_cn api seeds: homepage {err if r is None else 'HTTP ' + str(r.status_code)} → skip")
        return 0
    ids = sorted({int(x) for x in re.findall(r"(?:classid|sortid|topclassid)=(\d{1,5})", r.text)} - {0})
    log(f"hrui_cn api seeds: {len(ids)} candidate ids from homepage")
    added, calls, items_all = 0, 0, []
    for sid in ids[:80]:
        for lan in ("cn", "en", ""):
            p = 1
            got = False
            while p <= 40:
                u = f"{BASE}web/api.php?act=getdata&p={p}&limit=8&sortid={sid}&tj=&lanstr={lan}"
                rr, err = get(u)
                calls += 1
                time.sleep(min(DELAY, 0.6))
                if rr is None or rr.status_code != 200:
                    break
                try:
                    items = json.loads(rr.text)
                except Exception:
                    break
                if not isinstance(items, list) or not items:
                    break
                got = True
                with open(os.path.join(OUT, "api", f"getdata_sort{sid}_{lan or 'nolan'}_p{p}.json"), "w", encoding="utf-8") as f:
                    f.write(rr.text)
                for it in items:
                    if not isinstance(it, dict):
                        continue
                    iid = str(it.get("id") or "").strip()
                    link = next((str(it[k]) for k in ("url", "linkurl", "link", "href", "seourl") if it.get(k)), None)
                    cand = link if link else (f"{BASE}web/index.php?topclassid=0&classid={sid}&id={iid}" if iid.isdigit() else None)
                    items_all.append({"id": iid, "sortid": sid, "lanstr": lan, "title": it.get("title"), "product_sn": it.get("product_sn"), "url": cand})
                    n = norm(cand, BASE) if cand else None
                    if n and n not in seen:
                        seen.add(n)
                        queue.append(n)
                        added += 1
                if len(items) < 8:
                    break
                p += 1
            if got:
                break
    with open(os.path.join(OUT, "api", "products_index.json"), "w", encoding="utf-8") as f:
        json.dump(items_all, f, ensure_ascii=False, indent=1)
    log(f"hrui_cn api: {calls} calls, {len(items_all)} items, {added} new pages queued")
    return added


def _load_baseline(out):
    """v3.2 基线：三张清单 url → 记录；外加全部 sha256 集合（同内容换了 URL 也算未变）。"""
    b = {"pages": {}, "downloads": {}, "images": {}, "sha": set()}
    if not out:
        return b
    for key, fn in (("pages", "pages_manifest.jsonl"), ("downloads", "downloads_manifest.jsonl"), ("images", "images_manifest.jsonl")):
        for d in read_jsonl(os.path.join(out, fn)):
            if d.get("url"):
                b[key][d["url"]] = d
                if d.get("sha256"):
                    b["sha"].add(d["sha256"])
    return b


BASELINE = _load_baseline(BASE_OUT)
_TEXT_BLOCK_RE = re.compile(r"<(script|style|noscript)[^>]*>.*?</\1>", re.I | re.S)
_TAG_RE = re.compile(r"<[^>]+>")


def page_text_sig(html):
    """正文签名：去脚本 / 样式 / 标签 / 空白后的 sha256（token、时间戳变了但文字没变 → 不算内容变化）。"""
    t = _TEXT_BLOCK_RE.sub(" ", html or "")
    t = _TAG_RE.sub(" ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return sha256(t.encode("utf-8"))


def _read_text(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""


def build_diff(base, pages, dl_rows, img_rows):
    """v3.2：本轮 vs 基线。返回 {pages:{new,text_changed,markup_only,same,gone,not_reached}, downloads:{…}, images:{…}}。"""
    def ent(d, old=None, extra=None):
        e = {"url": d.get("url"), "title": d.get("title") or (old or {}).get("title"), "file": d.get("file"),
             "old_sha8": ((old or {}).get("sha256") or "")[:8] or None, "new_sha8": (d.get("sha256") or "")[:8] or None,
             "old_bytes": (old or {}).get("bytes"), "new_bytes": d.get("bytes")}
        if extra:
            e.update(extra)
        return e
    out = {}
    # pages
    bp = base["pages"]
    res = {"new": [], "text_changed": [], "markup_only": [], "same": 0, "gone": [], "not_reached": []}
    cur = {p["url"]: p for p in pages}
    for u, p in cur.items():
        old = bp.get(u)
        if old is None:
            if p.get("file"):
                res["new"].append(ent(p))
            continue
        if not p.get("file"):
            if old.get("file"):
                res["gone"].append(ent(p, old, {"status": p.get("status"), "error": p.get("error")}))
            continue
        if not old.get("file"):
            res["new"].append(ent(p, old, {"note": "基线那轮没抓到"}))
            continue
        if p.get("sha256") == old.get("sha256"):
            res["same"] += 1
            continue
        new_html = _read_text(os.path.join(OUT, p["file"]))
        old_html = _read_text(os.path.join(BASE_OUT, old["file"]))
        if page_text_sig(new_html) == page_text_sig(old_html):
            res["markup_only"].append(ent(p, old))
        else:
            res["text_changed"].append(ent(p, old, {"old_file": os.path.join(BASE_OUT, old["file"])}))
    for u, old in bp.items():
        if u not in cur and old.get("file"):
            res["not_reached"].append(ent({"url": u}, old))
    out["pages"] = res
    # downloads / images
    for key, rows in (("downloads", dl_rows), ("images", img_rows)):
        bb = base[key]
        r = {"new": [], "changed": [], "same": 0, "gone": [], "not_reached": []}
        cur = {d["url"]: d for d in rows}
        for u, d in cur.items():
            old = bb.get(u)
            if not d.get("file"):
                if old and old.get("file"):
                    r["gone"].append(ent(d, old, {"status": d.get("status"), "error": d.get("error")}))
                continue
            if d.get("same_as_base") or (old and old.get("sha256") == d.get("sha256")):
                r["same"] += 1
            elif old is None or not old.get("file"):
                r["new"].append(ent(d, old))
            else:
                r["changed"].append(ent(d, old))
        for u, old in bb.items():
            if u not in cur and old.get("file"):
                r["not_reached"].append(ent({"url": u}, old))
        out[key] = r
    return out


def write_diff(diff):
    with open(os.path.join(OUT, "diff.json"), "w", encoding="utf-8") as f:
        json.dump(diff, f, ensure_ascii=False, indent=1)
    L = [f"# 复抓对比：{HOST}（本轮 {now()}；基线 {BASE_OUT}）", ""]
    L.append("| 对象 | 新增 | 正文有变 / 内容变化 | 仅标记变 | 未变 | 消失（本轮取不到） | 本轮未抓到 |")
    L.append("|---|---|---|---|---|---|---|")
    pg = diff["pages"]
    L.append(f"| 页面 | {len(pg['new'])} | {len(pg['text_changed'])} | {len(pg['markup_only'])} | {pg['same']} | {len(pg['gone'])} | {len(pg['not_reached'])} |")
    for key, name in (("downloads", "附件"), ("images", "图片")):
        r = diff[key]
        L.append(f"| {name} | {len(r['new'])} | {len(r['changed'])} | – | {r['same']} | {len(r['gone'])} | {len(r['not_reached'])} |")
    L.append("")
    L.append("说明：「仅标记变」= HTML 字节变了但去标签后的正文一字未变（token / 时间戳 / 计数器之类）；「消失」= 基线抓到过、本轮 404 / 拒绝 / 出错；"
             "「本轮未抓到」= 本轮没有到达该 URL（预算 / 被封 / 站内不再链到）。附件与图片若内容 sha256 与基线一致则不再入 git（见 same_as_base）。")
    def sec(title, rows, cols):
        if not rows:
            return
        L.append("")
        L.append(f"## {title}（{len(rows)}）")
        L.append("")
        L.append("| " + " | ".join(cols) + " |")
        L.append("|" + "---|" * len(cols))
        for e in rows[:400]:
            L.append("| " + " | ".join(str(e.get(c) if e.get(c) is not None else "").replace("|", "\\|").replace("\n", " ") for c in cols) + " |")
        if len(rows) > 400:
            L.append(f"| …… 其余 {len(rows) - 400} 条见 diff.json | | | |")
    sec("页面：新增", pg["new"], ["url", "title", "file"])
    sec("页面：正文有变", pg["text_changed"], ["url", "title", "old_sha8", "new_sha8", "file", "old_file"])
    sec("页面：消失", pg["gone"], ["url", "title", "status", "error"])
    sec("页面：本轮未抓到", pg["not_reached"], ["url", "title"])
    sec("页面：仅标记变", pg["markup_only"], ["url", "title", "old_sha8", "new_sha8"])
    for key, name in (("downloads", "附件"), ("images", "图片")):
        r = diff[key]
        sec(f"{name}：新增", r["new"], ["url", "title", "file", "new_bytes"])
        sec(f"{name}：内容变化", r["changed"], ["url", "title", "old_sha8", "new_sha8", "old_bytes", "new_bytes", "file"])
        sec(f"{name}：消失", r["gone"], ["url", "title", "status", "error"])
        sec(f"{name}：本轮未抓到", r["not_reached"], ["url", "title"])
    with open(os.path.join(OUT, "diff.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def main():
    _sync_to_branch_tip()
    if BASE_OUT:
        log(f"v3.2 recrawl round: baseline {BASE_OUT} (pages {len(BASELINE['pages'])}, downloads {len(BASELINE['downloads'])}, "
            f"images {len(BASELINE['images'])}, sha {len(BASELINE['sha'])}) → OUT {OUT}")
    for d in ("html", "datasheet_text", "datasheets", "images"):
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
    # ---------- v3.1 站点钩子：HRUI 产品列表走 AJAX，静态页没有产品链接 ----------
    if not blocked and SITE == "hrui":
        try:
            hrui_api_seeds(queue, seen)
        except Exception as e:  # noqa: BLE001
            log(f"hrui api seeds failed: {e!r}")
    if not blocked and SITE == "hrui_cn":
        try:
            hrui_cn_api_seeds(queue, seen)
        except Exception as e:  # noqa: BLE001
            log(f"hrui_cn api seeds failed: {e!r}")

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
                # links（v3.0：sitemap / sitemap 索引 XML 的 <loc> / <image:loc> 一并当链接展开）
                hrefs = re.findall(r"""href\s*=\s*["']([^"'#]+)""", html, flags=re.I)
                if "xml" in ct or html.lstrip()[:60].lower().startswith("<?xml") or "<urlset" in html[:2000] or "<sitemapindex" in html[:2000]:
                    hrefs += re.findall(r"<(?:image:|video:)?loc>\s*(.*?)\s*</(?:image:|video:)?loc>", html, flags=re.I | re.S)
                for href in hrefs:
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
                for m2 in re.finditer(r"""<img[^>]+?(?:src|data-src|data-original|data-lazy-src|data-large_image)\s*=\s*["']([^"']+)["'][^>]*>""", html, flags=re.I):
                    n = norm(m2.group(1), r.url)
                    if n is None or kind(n) == "skip" or urlparse(n).path.endswith("/"):
                        continue  # v3.1：src 指向目录的坏 <img> 不算图片
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
        if BASE_OUT and h in BASELINE["sha"]:
            rec["same_as_base"] = True  # v3.2：内容与基线一致 → 不抽文本、不入 git（基线目录里已有）
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
        if not d["file"] or not (d.get("filename") or "").lower().endswith(".pdf") or d.get("same_as_base"):
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

    # ---------- commit downloads into git（v3.0：按文件规则 + 累计上限；此前是全有或全无） ----------
    pdf_bytes = sum(d["bytes"] or 0 for d in dl_rows if d["file"])
    cum = 0
    n_commit = 0
    n_ok_dl = 0
    for d in sorted((d for d in dl_rows if d["file"]), key=lambda d: d.get("bytes") or 0):
        if d.get("same_as_base"):
            d["committed"] = False
            continue
        n_ok_dl += 1
        size = d.get("bytes") or 0
        dst = os.path.join(OUT, "datasheets", d["filename"])
        if not commit_ok(d["filename"], size) or cum + size > PDF_COMMIT_MB * 1e6:
            d["committed"] = False
            continue
        src = os.path.join(BIN, d["file"])
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
        if os.path.exists(dst):
            d["committed"] = True
            cum += size
            n_commit += 1
    pdfs_committed = n_commit == n_ok_dl
    write_jsonl(p_dl, dl_rows)
    log(f"downloads total {pdf_bytes / 1e6:.1f} MB → committed to git: {n_commit}/{n_ok_dl} files ({cum / 1e6:.1f} MB; all={pdfs_committed})")
    save_state(p_state, queue, seen, downloads, images, external, "images", runs)

    # ---------- images (binary dir only) ----------
    def _img_bin_present(d):
        f = d.get("file") or ""
        return os.path.exists(os.path.join(BIN, f)) or os.path.exists(os.path.join(OUT, "images", os.path.basename(f)))

    img_prev_ok = [d for d in img_prev if d.get("file")]
    img_rows = [d for d in img_prev_ok if _img_bin_present(d)]
    if len(img_rows) < len(img_prev_ok):
        log(f"images: {len(img_prev_ok) - len(img_rows)} previously fetched but binary absent (Release clobbered) → re-download for git")
    done_img = {d["url"] for d in img_rows}
    # v3.0：出现页数少的先抓（产品图只在 1-2 页出现；logo / 皮肤图每页都有，排最后，预算不够时先放弃它们）
    todo_img = [(u, meta) for u, meta in sorted(images.items(), key=lambda kv: (len(kv[1].get("found_on") or []), kv[0])) if u not in done_img]
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
            data = None
            for attempt in range(2):  # v2.6.1：读体中断就地重试一次
                try:
                    data = r.content
                    break
                except Exception as e:  # noqa: BLE001  ChunkedEncodingError / IncompleteRead / ConnectionError
                    rec["error"] = f"body read failed: {e.__class__.__name__}"
                    time.sleep(3)
                    if attempt == 0:
                        try:
                            r = S.get(u, timeout=120, stream=True, allow_redirects=True,
                                      headers={"User-Agent": CHROME_UA, "Accept": "image/avif,image/webp,image/*,*/*;q=0.8", "Referer": BASE or "https://www.smartbyte-switch.com/"})
                            rec["status"] = r.status_code
                            if r.status_code != 200:
                                break
                        except Exception as e2:  # noqa: BLE001
                            rec["error"] = f"retry failed: {e2.__class__.__name__}"
                            break
            if data is None:
                img_rows.append(rec)
                _note(False)
                continue
            rec.pop("error", None)
            fn = fname(u)
            with open(os.path.join(BIN, "images", fn), "wb") as f:
                f.write(data)
            rec.update(file=f"images/{fn}", bytes=len(data), sha256=sha256(data))
            if BASE_OUT and rec["sha256"] in BASELINE["sha"]:
                rec["same_as_base"] = True  # v3.2：与基线同内容 → 不入 git
            total += len(data)
        img_rows.append(rec)
        time.sleep(min(DELAY, 0.5))
        if n_new_img % 100 == 0:
            log(f"images {i + 1}/{len(todo_img)} {total / 1e6:.0f} MB elapsed {elapsed() / 60:.1f} min")
            write_jsonl(p_img, img_rows)
    if img_stop is None:
        img_stop = "complete" if not skipped_site_img else f"blocked ({skipped_site_img} site-hosted left, CDN done) → resume later"
    # v2.6：图片入 git
    img_bytes = sum(d.get("bytes") or 0 for d in img_rows if d.get("file") and not d.get("same_as_base"))
    imgs_committed = img_bytes <= IMG_COMMIT_MB * 1e6
    n_copied = 0
    if imgs_committed:
        for d in img_rows:
            if d.get("file") and (d.get("bytes") or 0) <= 95e6 and not d.get("same_as_base"):
                src = os.path.join(BIN, d["file"])
                dst = os.path.join(OUT, "images", os.path.basename(d["file"]))
                if os.path.exists(src) and not os.path.exists(dst):
                    shutil.copy2(src, dst)
                    n_copied += 1
    log(f"images total {img_bytes / 1e6:.1f} MB → committed to git: {imgs_committed} (+{n_copied} copied into {OUT}/images)")
    write_jsonl(p_img, img_rows)
    log(f"images stop: {img_stop}; ok {sum(1 for d in img_rows if d['file'])}/{len(img_rows)} (+{n_new_img} this run), {total / 1e6:.1f} MB this run")

    # ---------- summary ----------
    images_left = sum(1 for u, _ in todo_img if u not in {d["url"] for d in img_rows})
    pages_ok = sum(1 for p in pages if p["file"])
    # 被拒型失败（403 / 429 / 网络错误）不算完成：下轮 Run workflow 会重试；404 之类不阻止 complete
    def _refused(rows, skip_prefix):
        return [d["url"] for d in rows if not d.get("file") and not (d.get("error") or "").startswith(skip_prefix)
                and (d.get("status") in (403, 429) or d.get("status") is None)
                and not urlparse(d["url"]).path.endswith("/")]  # v3.1：目录 URL（坏 <img src>）不算被拒
    refused = {"pages": _refused(pages, "binary-at-page-url"), "downloads": _refused(dl_rows, "\x00"), "images": _refused(img_rows, "skipped")}
    n_refused = sum(len(v) for v in refused.values())
    nothing_left = (not queue and dl_stop == "complete" and img_stop == "complete")
    complete = (pages_ok > 0 and n_refused == 0 and dl_stop == "complete" and img_stop == "complete"
                and (pages_stop.startswith("complete") or (blocked and nothing_left)))
    runs[-1].update(ended=now(), elapsed_s=round(elapsed()), pages_new=n_new_pages, downloads_new=n_new_dl,
                    images_new=n_new_img, pages_stop=pages_stop, downloads_stop=dl_stop, images_stop=img_stop)
    diff = None
    if BASE_OUT:
        try:
            diff = build_diff(BASELINE, pages, dl_rows, img_rows)
            write_diff(diff)
            log("diff: " + json.dumps({k: {kk: (len(vv) if isinstance(vv, list) else vv) for kk, vv in v.items()} for k, v in diff.items()}, ensure_ascii=False))
        except Exception as e:  # noqa: BLE001
            log(f"diff failed: {e!r}")
    summary = {
        "crawled_at": now(), "host": HOST, "complete": complete, "blocked": blocked,
        "recrawl_base": BASE_OUT,
        "diff": ({k: {kk: (len(vv) if isinstance(vv, list) else vv) for kk, vv in v.items()} for k, v in diff.items()} if diff else None),
        "same_as_base": {"downloads": sum(1 for d in dl_rows if d.get("same_as_base")), "images": sum(1 for d in img_rows if d.get("same_as_base"))},
        "access": {k: ACCESS.get(k) for k in ("mode", "profile", "base")},
        "refused": {k: len(v) for k, v in refused.items()}, "refused_sample": {k: v[:20] for k, v in refused.items()},
        "pages_total": len(pages), "pages_ok": sum(1 for p in pages if p["file"]),
        "pages_failed": [p["url"] for p in pages if not p["file"]],
        "pages_stop": pages_stop, "queue_left": len(queue),
        "downloads_total": len(dl_rows), "downloads_ok": sum(1 for d in dl_rows if d["file"]),
        "downloads_left": max(0, len(todo_dl) - n_new_dl), "downloads_stop": dl_stop,
        "downloads_bytes": pdf_bytes, "pdfs_committed": pdfs_committed, "pdf_text_files": n_txt,
        "images_bytes": img_bytes, "images_committed": imgs_committed,
        "images_total": len(img_rows), "images_ok": sum(1 for d in img_rows if d["file"]),
        "images_left": images_left, "images_stop": img_stop, "images_bytes_this_run": total,
        "external_hosts": {k: len(v) for k, v in sorted(external.items())},
        "runs": runs, "elapsed_s": round(elapsed()), "user_agent": UA, "delay_s": DELAY,
        "time_budget_min": TIME_BUDGET_MIN,
        "how_to_continue": None if complete else (
            "被封：站点对 GitHub Actions 运行器的所有访问方式都返回拒绝（access_diag.json 有状态码 / 响应头 / 正文片段）。"
            "办法：① 过几小时再到 Actions 页点 Run workflow（可能是长时间抓取触发的临时封禁）；"
            f"② 在本地电脑运行 CRAWL_HOST={HOST} python scripts/smartbyte_crawl/crawl.py {OUT} {BIN} 后提交；"
            "③ 请站方放行归档 UA / 运行器 IP。" if blocked else
            f"未抓完（被拒 403/429/网络错误 {n_refused} 个；页面阶段 {pages_stop}；附件 {dl_stop}；图片 {img_stop}）："
            "在 GitHub Actions 页对 SmartByte site archive 点 Run workflow（或再推一次 crawl.py），会从 crawl_state.json 续抓并重试失败项"),
        "site": SITE,
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


DOC_EXT = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv")


def commit_ok(fn, size):
    """单个附件是否入 git：任何文件 ≤95 MB（GitHub 单文件 100 MB 硬限）；文档 ≤60 MB；固件 / 压缩包 ≤15 MB。"""
    ext = os.path.splitext(fn or "")[1].lower()
    if size > 95e6:
        return False
    if ext in DOC_EXT:
        return size <= 60e6
    return size <= 15e6


def _already_complete(out):
    try:
        with open(os.path.join(out, "summary.json"), encoding="utf-8") as f:
            return bool(json.load(f).get("complete"))
    except Exception:
        return False


def run_extra_sites():
    """v3.0 编排（仅 GitHub Actions、仅工作流固定命令那次调用）：顺序以子进程抓 EXTRA_SITES，再 git add 它们的 OUT 目录。
    预算：作业上限 170 分钟，给 zip / 提交留 20 分钟；余下在各站之间平分（每站最多 55 分钟）。"""
    if os.environ.get("CRAWL_HOST") or os.environ.get("CRAWL_EXTRA_SITES", "1") == "0" or not os.environ.get("GITHUB_ACTIONS"):
        return
    outs = []
    for site in EXTRA_SITES:
        left = 150 - elapsed() / 60
        n_left = len(EXTRA_SITES) - EXTRA_SITES.index(site)
        budget = max(8, min(55, left / n_left))
        if left < 10:
            log(f"[extra] {site['site']}: no time left ({left:.0f} min) → next run")
            continue
        env = dict(os.environ, CRAWL_HOST=site["host"], CRAWL_SCHEME=site.get("scheme", "https"), CRAWL_SITE=site["site"],
                   TIME_BUDGET_MIN=f"{budget:.0f}", MAX_IMAGE_MB=os.environ.get("EXTRA_MAX_IMAGE_MB", "250"),
                   IMG_COMMIT_MB=os.environ.get("EXTRA_IMG_COMMIT_MB", "250"), PDF_COMMIT_MB=os.environ.get("EXTRA_PDF_COMMIT_MB", "250"))
        log(f"[extra] ===== {site['site']} ({site['host']}) → {site['out']}; budget {budget:.0f} min =====")
        try:
            subprocess.run([sys.executable, os.path.abspath(__file__), site["out"], site["bin"]], env=env, check=False,
                           timeout=(budget + 12) * 60)
        except subprocess.TimeoutExpired:
            log(f"[extra] {site['site']}: child timed out (budget {budget:.0f} min + 12) → checkpoints on disk, resume next run")
        except Exception as e:  # noqa: BLE001
            log(f"[extra] {site['site']}: child failed to run: {e!r}")
        if os.path.isdir(site["out"]):
            outs.append(site["out"])
            try:
                with open(os.path.join(site["out"], "summary.json"), encoding="utf-8") as f:
                    sm = json.load(f)
                log(f"[extra] {site['site']}: complete={sm.get('complete')} pages {sm.get('pages_ok')}/{sm.get('pages_total')} "
                    f"downloads {sm.get('downloads_ok')}/{sm.get('downloads_total')} images {sm.get('images_ok')}/{sm.get('images_total')}")
            except Exception:
                log(f"[extra] {site['site']}: no summary.json")
    if outs:
        try:
            subprocess.run(["git", "add", "-A", *outs], check=True, timeout=600)
            log(f"[extra] git add -A {' '.join(outs)} → staged for the workflow's commit step")
        except Exception as e:  # noqa: BLE001
            log(f"[extra] git add failed: {e!r}")


def _read_kv(path):
    kv = {}
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                kv[k.strip()] = v.strip()
    except Exception:
        pass
    return kv


def run_recrawl_round():
    """v3.2 复抓编排（仅 GitHub Actions、仅工作流固定命令那次调用）：RECRAWL 文件 ROUND=YYYYMMDD → 三站各起一子进程，
    CRAWL_BASE=原整站目录做基线，写到 data/site_recrawl/<ROUND>/<site>/（html 全量 + 仅新增 / 变化的二进制 + diff.md）。
    已 complete 的站跳过；未完成的站下次再推 crawl.py 从该目录的 crawl_state.json 续抓。"""
    if os.environ.get("CRAWL_HOST") or not os.environ.get("GITHUB_ACTIONS"):
        return
    kv = _read_kv(RECRAWL_FILE)
    rnd = (kv.get("ROUND") or "").strip()
    if not rnd:
        return
    want = [x.strip() for x in (kv.get("SITES") or "smartbyte,hrui,hohunet").split(",") if x.strip()]
    sites = [{"site": "smartbyte", "host": HOST, "scheme": SCHEME, "out": OUT}] + EXTRA_SITES
    weights = {"smartbyte": 0.45, "hrui": 0.35, "hohunet": 0.20}
    todo = [s for s in sites if s["site"] in want and not _already_complete(os.path.join(RECRAWL_ROOT, rnd, s["site"]))]
    log(f"[recrawl] round {rnd}: todo {[s['site'] for s in todo]} (skipped complete: {[s['site'] for s in sites if s['site'] in want and s not in todo]})")
    outs = []
    for i, s in enumerate(todo):
        left = 150 - elapsed() / 60
        wsum = sum(weights.get(x["site"], 0.3) for x in todo[i:]) or 1
        budget = max(8, left * weights.get(s["site"], 0.3) / wsum)
        if left < 10:
            log(f"[recrawl] {s['site']}: no time left ({left:.0f} min) → next run")
            continue
        out_r = os.path.join(RECRAWL_ROOT, rnd, s["site"])
        bin_r = f"crawl_bin_r{rnd}_{s['site']}"
        env = dict(os.environ, CRAWL_HOST=s["host"], CRAWL_SCHEME=s.get("scheme", "https"), CRAWL_SITE=s["site"], CRAWL_BASE=s["out"],
                   TIME_BUDGET_MIN=f"{budget:.0f}", MAX_IMAGE_MB=os.environ.get("RECRAWL_MAX_IMAGE_MB", "600"),
                   IMG_COMMIT_MB=os.environ.get("RECRAWL_IMG_COMMIT_MB", "250"), PDF_COMMIT_MB=os.environ.get("RECRAWL_PDF_COMMIT_MB", "250"))
        log(f"[recrawl] ===== {s['site']} ({s['host']}) base {s['out']} → {out_r}; budget {budget:.0f} min =====")
        try:
            subprocess.run([sys.executable, os.path.abspath(__file__), out_r, bin_r], env=env, check=False, timeout=(budget + 12) * 60)
        except subprocess.TimeoutExpired:
            log(f"[recrawl] {s['site']}: child timed out (budget {budget:.0f} min + 12) → checkpoints on disk, resume next run")
        except Exception as e:  # noqa: BLE001
            log(f"[recrawl] {s['site']}: child failed to run: {e!r}")
        if os.path.isdir(out_r):
            outs.append(out_r)
            try:
                with open(os.path.join(out_r, "summary.json"), encoding="utf-8") as f:
                    sm = json.load(f)
                log(f"[recrawl] {s['site']}: complete={sm.get('complete')} pages {sm.get('pages_ok')}/{sm.get('pages_total')} "
                    f"downloads {sm.get('downloads_ok')}/{sm.get('downloads_total')} images {sm.get('images_ok')}/{sm.get('images_total')} "
                    f"diff {json.dumps(sm.get('diff'), ensure_ascii=False)}")
            except Exception:
                log(f"[recrawl] {s['site']}: no summary.json")
    try:
        os.makedirs(RECRAWL_ROOT, exist_ok=True)
        with open(os.path.join(RECRAWL_ROOT, f"round_{rnd}_orchestrator_log.txt"), "a", encoding="utf-8") as f:
            f.write(f"===== run {RUN_ID} {now()} =====\n" + "\n".join(x for x in LOG if "[recrawl]" in x) + "\n")
        subprocess.run(["git", "add", "-A", RECRAWL_ROOT], check=True, timeout=600)
        log(f"[recrawl] git add -A {RECRAWL_ROOT} → staged for the workflow's commit step")
    except Exception as e:  # noqa: BLE001
        log(f"[recrawl] git add failed: {e!r}")


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


def _watch_only_flag():
    """v3.3（T29-U18）：scripts/web_watch/RUN_ON_CRAWL 含 WATCH_ONLY=1 时，本工作流这次运行只跑成单客户活跃平台监控，不爬站。
    原因：沙箱无外网，监控必须在运行器上跑；本工作流由「推送触及 crawl.py」触发且与 drive-smartbyte-ingest 互不占并发组。"""
    flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "web_watch", "RUN_ON_CRAWL")
    try:
        with open(flag, encoding="utf-8") as f:
            return any(ln.strip() == "WATCH_ONLY=1" for ln in f)
    except OSError:
        return False


def _watch_layer():
    """RUN_ON_CRAWL 里的 LAYER=…（缺省 all）。v3.4（T29-U19）：面层 A/B 加入后用它控制本次跑哪几层。"""
    flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "web_watch", "RUN_ON_CRAWL")
    try:
        with open(flag, encoding="utf-8") as f:
            for ln in f:
                if ln.strip().startswith("LAYER="):
                    return ln.strip().split("=", 1)[1].strip() or "all"
    except OSError:
        pass
    return "all"


def _run_customer_watch():
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "web_watch", "watch.py")
    layer = _watch_layer()
    log(f"[watch] WATCH_ONLY=1 → python scripts/web_watch/watch.py --layer {layer}（客户动态监控：成单精选层 + A/B 面层），不爬站")
    try:
        r = subprocess.run([sys.executable, os.path.abspath(script), "--layer", layer], check=False, timeout=5400)
        log(f"[watch] exit {r.returncode}")
    except Exception as e:  # noqa: BLE001
        log(f"[watch] failed: {e!r}")
    # 只建 BIN 本身、不建 downloads/images 子目录：工作流的 zip 步骤 `cd crawl_bin` 能过、`zip -qr … downloads || true` 产不出 zip，
    # Release 步骤就按「no zips」跳过 —— 首轮（02:53Z）因建了空子目录而生成了只有 170/164 字节空 zip 的 smartbyte-site-20261023 发布，已删。
    os.makedirs(BIN, exist_ok=True)


if __name__ == "__main__":
    if os.environ.get("GITHUB_ACTIONS") and not os.environ.get("CRAWL_HOST") and _watch_only_flag():
        _run_customer_watch()
        sys.exit(0)
    try:
        if _already_complete(OUT) and not os.environ.get("CRAWL_RECRAWL"):
            # v3.0：该站已整站抓齐（summary.json complete=true）→ 不重抓（CRAWL_RECRAWL=1 强制）
            for d in ("downloads", "images"):
                os.makedirs(os.path.join(BIN, d), exist_ok=True)  # 工作流的 zip 步骤要 cd 进 BIN
            log(f"{SITE}: {OUT}/summary.json complete=true → skip recrawl (set CRAWL_RECRAWL=1 to force)")
        else:
            main()
    except Exception as e:  # noqa: BLE001
        _crash(e)
    finally:
        try:
            if _PW.get("browser"):
                _PW["browser"].close()
                _PW["pw"].stop()
        except Exception:
            pass
    try:
        run_extra_sites()
    except Exception as e:  # noqa: BLE001
        log(f"[extra] orchestrator failed: {e!r}")
    try:
        run_recrawl_round()
    except Exception as e:  # noqa: BLE001
        log(f"[recrawl] orchestrator failed: {e!r}")
    sys.exit(0)
