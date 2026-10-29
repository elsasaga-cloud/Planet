#!/usr/bin/env python3
"""客户动态监控（T29-U18 成单客户精选层 + T29-U19 A/B 级面监控层，2026-10-23）。只读，不发任何消息。

两层清单合并执行：
  精选层 scripts/web_watch/targets.json       20 家成单客户，人工挑的源（RSS / 整页 / JSON API / sitemap / GitHub / YouTube）
  面层   scripts/web_watch/targets_auto.json  discover.py 离线从 entities.json + T27 官网快照生成的 A/B 级 1,100+ 家：首页 / sitemap / 新闻栏目 / YouTube / GitHub / Telegram / VK
运行时还会从首页 HTML 的 <link rel=alternate type=rss/atom> 自动发现站点 feed（记在 state 的 _meta 里，下一轮起作为 feed_auto 源抓）。

用法（GitHub Actions 运行器；Arena 沙箱无外网，只能跑 --selftest）：
    python scripts/web_watch/watch.py              # 抓全部源，写 data/customer_watch/，在 Actions 内自动提交推送
    python scripts/web_watch/watch.py --only SA-077 SB-001
    python scripts/web_watch/watch.py --no-commit
    python scripts/web_watch/watch.py --selftest   # 用内置样本测试各解析器（不联网）

逻辑：targets.json 每个源 → 抓取 → 规范化（rss/sitemap/github 抽成条目表；html 抽正文文本；json 抽字段）
     → 与 data/customer_watch/state.json 上一轮比较 → 新条目 / 文本行级 diff / 字段变化
     → 追加 变化日志.md（append-only，无变化也记一节）、重写 当前状态.md、latest 文本放 snapshots/<code>/<id>.txt
     （文本快照进 git，历史 diff 用 git log -p 看）。
"""
import argparse
import datetime as _dt
import difflib
import glob
import hashlib
import html as _html
import json
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CFG = os.path.join(HERE, 'targets.json')
CFG_AUTO = os.path.join(HERE, 'targets_auto.json')
OUT = os.path.join(ROOT, 'data', 'customer_watch')
STATE = os.path.join(OUT, 'state.json')
SNAP = os.path.join(OUT, 'snapshots')
WORKERS = int(os.environ.get('WATCH_WORKERS', '12'))
TS = _dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 SagaWatch/1.0'
BROWSER_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
TIMEOUT = 35
MAX_TEXT = 60_000          # 抓取时文本上限
SNAP_TEXT = {'成单': 40_000, 'A': 16_000, 'B': 12_000, 'P': 16_000}   # 落盘快照上限（面层小一点，控制仓库体积）
MAX_ITEMS = 300
STATE_ITEMS = 80           # state.json 里每个源最多保留的条目数（rss / sitemap / github）

try:
    import requests  # noqa: E402
except Exception:  # pragma: no cover
    requests = None


# ----------------------------------------------------------------------------- fetch
import threading as _th
_YT_LOCK = _th.Lock()
_YT_LAST = [0.0]


def _yt_throttle():
    """YouTube 全局串行 + ≥2 s 间隔：全层基线（04:20Z）227 个 YouTube 源 221 个 404（含肯定存在的频道 RSS），
    而零星几个成功 → 疑似 12 线程并发触发了 YouTube 对该 IP 的拦截（以 404 形式）。"""
    with _YT_LOCK:
        wait = 2.0 - (time.time() - _YT_LAST[0])
        if wait > 0:
            time.sleep(wait)
        _YT_LAST[0] = time.time()


def fetch(url, accept=None, attempts=3, timeout=None):
    """返回 (status_code, text, final_url)。失败抛异常。面层（A/B）用 attempts=2、timeout 20 s，控制总时长。
    特例：youtube.com 一开始就用浏览器 UA + 同意 cookie、全局限速，404 也重试一次；https 证书错误时降级 http 再试一次。"""
    if requests is None:
        raise RuntimeError('requests not installed')
    h = {'User-Agent': UA, 'Accept-Language': 'en,tr;q=0.8,ru;q=0.7,th;q=0.6,zh;q=0.5'}
    if accept:
        h['Accept'] = accept
    is_yt = 'youtube.com' in url.lower()
    if is_yt:
        h['User-Agent'] = BROWSER_UA
        h['Accept-Language'] = 'en-US,en;q=0.9'
        h['Cookie'] = 'CONSENT=YES+cb.20210328-17-p0.en+FX+417; SOCS=CAI'
        attempts = max(attempts, 2)
    last = None
    timeout = timeout or TIMEOUT
    ssl_fallback_done = False
    for attempt in range(attempts):
        try:
            if attempt and not is_yt:   # 第 2 次起换成普通浏览器 UA（首轮基线：vilinknet.com 403 / sundartechno feed 429 / govtribe 403 都是反爬 UA 过滤）
                h['User-Agent'] = BROWSER_UA
                h['Accept'] = h.get('Accept') or 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            if is_yt:
                _yt_throttle()
            r = requests.get(url, headers=h, timeout=timeout, allow_redirects=True)
            retry_codes = (403, 429, 404) if is_yt else (403, 429)
            if (r.status_code >= 500 or r.status_code in retry_codes) and attempt < attempts - 1:
                last = RuntimeError(f'HTTP {r.status_code}')
                time.sleep(4 * (attempt + 1) if r.status_code != 429 else 15 * (attempt + 1))
                continue
            enc = r.encoding or 'utf-8'
            if enc.lower() in ('iso-8859-1', 'latin-1') and r.apparent_encoding:
                enc = r.apparent_encoding
            try:
                text = r.content.decode(enc, errors='replace')
            except Exception:
                text = r.text
            return r.status_code, text, r.url
        except Exception as e:  # noqa: BLE001
            last = e
            if 'SSLError' in type(e).__name__ or 'SSL' in str(e)[:200]:
                if url.lower().startswith('https://') and not ssl_fallback_done:
                    ssl_fallback_done = True
                    url = 'http://' + url[8:]          # 证书坏了的小站：http 往往还活着
                    continue
            time.sleep(3 * (attempt + 1))
    raise last or RuntimeError('fetch failed')


def gh_api(path):
    if requests is None:
        raise RuntimeError('requests not installed')
    h = {'User-Agent': UA, 'Accept': 'application/vnd.github+json'}
    tok = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if tok:
        h['Authorization'] = f'Bearer {tok}'
    r = requests.get('https://api.github.com/' + path.lstrip('/'), headers=h, timeout=TIMEOUT)
    if r.status_code != 200:
        raise RuntimeError(f'GitHub API {r.status_code}: {r.text[:120]}')
    return r.json()


# ----------------------------------------------------------------------------- normalize
_TAG_BLOCK = re.compile(r'(?is)<(script|style|noscript|svg|template|iframe)\b.*?</\1\s*>')
_COMMENT = re.compile(r'(?s)<!--.*?-->')
_BR = re.compile(r'(?i)<\s*(br|/p|/div|/li|/h[1-6]|/tr|/section|/article|/header|/footer|/td|/th|/dd|/dt|/blockquote|/pre|/option)\b[^>]*>')
_TAGS = re.compile(r'<[^>]+>')
_WS = re.compile(r'[ \t\r\f\v\u00a0]+')
_VOLATILE = [
    re.compile(r'(?i)\b(nonce|csrf[-_]?token|_wpnonce|wpnonce|sessionid|jsessionid|phpsessid|cf-ray|ray id)\b.{0,80}'),
    re.compile(r'(?i)\b\d{1,2}:\d{2}(:\d{2})?\s*(am|pm)?\b'),  # 时刻（页面自带时钟）
    re.compile(r'(?i)cart\s*\(?\s*\d+\s*\)?|корзина\s*(пуста)?\s*\d*'),
    re.compile(r'(?i)your ip:?\s*\S+'),
]


def html_to_text(src, include=None, exclude=None):
    s = src
    if include:
        for pat in ([include] if isinstance(include, str) else include):
            m = re.search(pat, s)
            if m:
                s = m.group(0)
                break
    for pat in (exclude or []):
        s = re.sub(pat, ' ', s)
    s = _COMMENT.sub(' ', s)
    s = _TAG_BLOCK.sub(' ', s)
    s = _BR.sub('\n', s)
    s = _TAGS.sub(' ', s)
    s = _html.unescape(s)
    lines = []
    for ln in s.split('\n'):
        ln = _WS.sub(' ', ln).strip()
        if not ln:
            continue
        for v in _VOLATILE:
            ln = v.sub('', ln).strip()
        if ln:
            lines.append(ln)
    # 去掉连续重复行（导航重复渲染）
    out = []
    for ln in lines:
        if not out or out[-1] != ln:
            out.append(ln)
    text = '\n'.join(out)
    return text[:MAX_TEXT]


def _strip_ns(tag):
    return tag.split('}', 1)[1] if '}' in tag else tag


def parse_feed(src):
    """RSS 2.0 / Atom / YouTube Atom → [{'id','title','date','link'}]（按文档顺序）。"""
    src = src.lstrip('\ufeff \r\n\t')
    try:
        root = ET.fromstring(src.encode('utf-8', errors='replace'))
    except ET.ParseError:
        # 容错：去掉非法控制字符再试
        cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', src)
        root = ET.fromstring(cleaned.encode('utf-8', errors='replace'))
    items = []
    for el in root.iter():
        t = _strip_ns(el.tag)
        if t not in ('item', 'entry'):
            continue
        d = {'title': '', 'link': '', 'date': '', 'id': ''}
        for c in el:
            ct = _strip_ns(c.tag)
            txt = (c.text or '').strip()
            if ct == 'title':
                d['title'] = re.sub(r'\s+', ' ', _html.unescape(txt))[:200]
            elif ct == 'link':
                d['link'] = txt or c.attrib.get('href', '')
            elif ct in ('pubDate', 'published', 'updated', 'date') and not d['date']:
                d['date'] = txt[:40]
            elif ct in ('guid', 'id') and not d['id']:
                d['id'] = txt
        d['id'] = d['id'] or d['link'] or d['title']
        if d['id']:
            items.append(d)
        if len(items) >= MAX_ITEMS:
            break
    return items


def parse_sitemap(src):
    items = []
    try:
        root = ET.fromstring(src.encode('utf-8', errors='replace'))
    except ET.ParseError:
        return items
    for el in root.iter():
        if _strip_ns(el.tag) != 'url':
            continue
        loc = lastmod = ''
        for c in el:
            ct = _strip_ns(c.tag)
            if ct == 'loc':
                loc = (c.text or '').strip()
            elif ct == 'lastmod':
                lastmod = (c.text or '').strip()
        if loc:
            items.append({'id': loc, 'title': loc.rstrip('/').rsplit('/', 1)[-1], 'date': lastmod, 'link': loc})
        if len(items) >= MAX_ITEMS * 3:
            break
    return items


def dotted(obj, path):
    cur = obj
    for part in path.split('.'):
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except Exception:
                return None
        elif isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
        if cur is None:
            return None
    return cur


def pick_fields(obj, fields):
    if not fields:
        return obj
    return {f: dotted(obj, f) for f in fields}


def github_account(login):
    prof = gh_api(f'users/{login}')
    repos = gh_api(f'users/{login}/repos?per_page=100&sort=pushed&type=all')
    try:
        events = gh_api(f'users/{login}/events/public?per_page=30')
    except Exception:  # noqa: BLE001
        events = []
    items = []
    for r in repos if isinstance(repos, list) else []:
        items.append({'id': 'repo:' + r['full_name'], 'title': f"{r['name']}（{(r.get('description') or '')[:80]}）",
                      'date': r.get('pushed_at') or '', 'link': r.get('html_url', ''), 'pushed_at': r.get('pushed_at')})
    for e in events if isinstance(events, list) else []:
        repo = (e.get('repo') or {}).get('name', '')
        payload = e.get('payload') or {}
        extra = ''
        if e.get('type') == 'PushEvent':
            cms = payload.get('commits') or []
            extra = f"push {len(cms)} commit(s): " + ' ‖ '.join((c.get('message') or '').split('\n')[0][:80] for c in cms[:3])
        elif e.get('type') == 'CreateEvent':
            extra = f"create {payload.get('ref_type')} {payload.get('ref') or ''}"
        elif e.get('type') in ('IssuesEvent', 'PullRequestEvent', 'IssueCommentEvent'):
            obj = payload.get('issue') or payload.get('pull_request') or {}
            extra = f"{payload.get('action')} #{obj.get('number')} {obj.get('title', '')[:80]}"
        items.append({'id': 'event:' + str(e.get('id')), 'title': f"{e.get('type')} {repo} {extra}".strip(),
                      'date': e.get('created_at', ''), 'link': f'https://github.com/{repo}'})
    profile = {k: prof.get(k) for k in ('login', 'type', 'name', 'company', 'blog', 'location', 'email', 'bio',
                                        'public_repos', 'followers', 'created_at', 'updated_at')}
    return profile, items


def youtube_channel_id(page):
    m = re.search(r'"channelId":"(UC[0-9A-Za-z_-]{20,})"', page) or \
        re.search(r'<meta itemprop="identifier" content="(UC[0-9A-Za-z_-]{20,})"', page) or \
        re.search(r'youtube\.com/channel/(UC[0-9A-Za-z_-]{20,})', page)
    return m.group(1) if m else None


YT_API_KEY = os.environ.get('YT_API_KEY', '').strip()


def yt_api(path, **params):
    """YouTube Data API v3（需要 YT_API_KEY；channels.list / playlistItems.list 各 1 配额单位，227 个频道一天 <500 单位，免费额度 10,000）。"""
    params['key'] = YT_API_KEY
    r = requests.get('https://www.googleapis.com/youtube/v3/' + path, params=params, headers={'User-Agent': UA}, timeout=TIMEOUT)
    if r.status_code != 200:
        raise RuntimeError(f'YouTube API {r.status_code}: {r.text[:140]}')
    return r.json()


def yt_api_items(url):
    """用 API 取频道最近上传：返回 (channel_id, items)。url 可以是 feeds/videos.xml?channel_id=、/channel/UC…、/@handle、/user/x；/c/x 不支持（抛异常→走旧路径）。"""
    u = url.strip()
    cid = handle = user = None
    m = re.search(r'channel_id=(UC[0-9A-Za-z_-]{20,})', u) or re.search(r'/channel/(UC[0-9A-Za-z_-]{20,})', u)
    if m:
        cid = m.group(1)
    elif re.search(r'youtube\.com/@([^/?#]+)', u):
        handle = re.search(r'youtube\.com/@([^/?#]+)', u).group(1)
    elif re.search(r'youtube\.com/user/([^/?#]+)', u):
        user = re.search(r'youtube\.com/user/([^/?#]+)', u).group(1)
    else:
        raise RuntimeError('unsupported YouTube URL for API')
    if not cid:
        q = {'part': 'id', 'forHandle': handle} if handle else {'part': 'id', 'forUsername': user}
        data = yt_api('channels', **q)
        items = data.get('items') or []
        if not items:
            raise RuntimeError('YouTube API: channel not found')
        cid = items[0]['id']
    data = yt_api('playlistItems', part='snippet', playlistId='UU' + cid[2:], maxResults=15)
    out = []
    for it in data.get('items') or []:
        sn = it.get('snippet') or {}
        vid = (sn.get('resourceId') or {}).get('videoId') or it.get('id')
        out.append({'id': f'https://www.youtube.com/watch?v={vid}', 'title': sn.get('title', ''), 'date': sn.get('publishedAt', ''), 'link': f'https://www.youtube.com/watch?v={vid}'})
    return cid, out


# ----------------------------------------------------------------------------- per-source
_FEED_LINK = re.compile(r'(?is)<link\b[^>]*>')
_ATTR = re.compile(r"(?is)([a-z:-]+)\s*=\s*(\"([^\"]*)\"|'([^']*)'|([^\s>]+))")


def find_feeds(body, base_url):
    """首页 HTML 里的 <link rel="alternate" type="application/rss+xml|atom+xml" href=…>，返回绝对 URL 列表（去重、排除评论 feed）。"""
    out = []
    for tag in _FEED_LINK.findall(body[:400_000]):
        attrs = {m.group(1).lower(): (m.group(3) or m.group(4) or m.group(5) or '') for m in _ATTR.finditer(tag)}
        if 'alternate' not in (attrs.get('rel') or '').lower():
            continue
        typ = (attrs.get('type') or '').lower()
        if 'rss' not in typ and 'atom' not in typ:
            continue
        href = _html.unescape(attrs.get('href') or '').strip()
        if not href or 'comments' in href.lower():
            continue
        if href.startswith('//'):
            href = 'https:' + href
        elif href.startswith('/'):
            m = re.match(r'(https?://[^/]+)', base_url or '')
            href = (m.group(1) if m else '') + href
        elif not href.startswith('http'):
            href = (base_url or '').rstrip('/') + '/' + href
        if href not in out:
            out.append(href)
    return out


def run_source(src):
    """返回 dict：status, hash, items(dict id→{title,date}), text(可选), fields(可选), error(可选), profile(可选)。"""
    kind = src['kind']
    res = {'kind': kind, 'fetched_at': TS}
    lite = src.get('_lite')           # 面层：少重试、短超时
    fo = {'attempts': 2, 'timeout': 20} if lite else {}
    try:
        if kind == 'github':
            profile, items = github_account(src['login'])
            res['profile'] = profile
            res['items'] = {i['id']: {'title': i['title'], 'date': i.get('date', '')} for i in items}
            res['hash'] = hashlib.sha1(json.dumps([(i['id'], i.get('date')) for i in items], sort_keys=True).encode()).hexdigest()
            res['status'] = 200
            res['summary'] = f"{profile.get('type')} {profile.get('login')} · 仓库 {profile.get('public_repos')} · 最近推送 " + \
                             (max([i.get('date') or '' for i in items if i['id'].startswith('repo:')] or ['-']))
            return res
        url = src['url']
        if 'youtube.com' in (url or '').lower() and kind in ('youtube_handle', 'rss'):
            if YT_API_KEY:
                try:
                    cid, items = yt_api_items(url if not src.get('_cached_channel_id') else f"https://www.youtube.com/channel/{src['_cached_channel_id']}")
                    res['channel_id'] = cid
                    res['status'] = 200
                    res['items'] = {i['id']: {'title': i['title'], 'date': i['date']} for i in items}
                    res['hash'] = hashlib.sha1(json.dumps(sorted(res['items']), ensure_ascii=False).encode()).hexdigest()
                    res['text'] = '\n'.join(f"{i['date']}\t{i['title']}\t{i['link']}" for i in items)
                    res['summary'] = (f"API · {len(items)} 条；最新：{items[0]['date'][:19]} {items[0]['title'][:80]}" if items else 'API · 0 条')
                    return res
                except Exception as e:  # noqa: BLE001
                    if 'unsupported' not in str(e):
                        raise
        if kind == 'youtube_handle':
            cid = src.get('_cached_channel_id')
            if not cid:
                code, page, _ = fetch(url, accept='text/html', **fo)
                cid = youtube_channel_id(page)
                if not cid:
                    raise RuntimeError(f'channelId not found (HTTP {code})' + ('；YouTube 对运行器 IP 常以 404 拦截，设 YT_API_KEY 可绕过' if code == 404 else ''))
            res['channel_id'] = cid
            url = f'https://www.youtube.com/feeds/videos.xml?channel_id={cid}'
            kind = 'rss'
        acc = ('application/rss+xml, application/atom+xml, application/xml, application/json, text/html;q=0.8, */*;q=0.5'
               if kind in ('rss', 'sitemap', 'json') else 'text/html,application/xhtml+xml,*/*;q=0.8')
        try:
            code, body, final = fetch(url, accept=acc, **fo)
        except Exception:
            if not src.get('url_fallback'):
                raise
            code = 599
        if code >= 400 and src.get('url_fallback'):
            code, body, final = fetch(src['url_fallback'], accept=acc, **fo)
        res['status'] = code
        res['final_url'] = final
        if code >= 400:
            # 仍记录错误页文本（例如 522/404 也是状态）
            res['text'] = html_to_text(body)[:4000]
            res['hash'] = hashlib.sha1(f'HTTP {code}'.encode()).hexdigest()
            res['items'] = {}
            res['error'] = f'HTTP {code}'
            if code == 404 and 'youtube.com' in (url or '').lower():
                # 2026-10-23 实测：同一频道 RSS 对运行器一会 200 一会 404，fetch_page 也 404 → 是 YouTube 对数据中心 IP 的拦截，不是频道不存在
                res['error'] = 'YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）'
            return res
        if kind == 'rss':
            items = parse_feed(body)
            if not items and '<html' in body[:2000].lower():
                raise RuntimeError('feed URL returned HTML (no items)')
            res['items'] = {i['id']: {'title': i['title'], 'date': i['date']} for i in items}
            res['hash'] = hashlib.sha1(json.dumps(sorted(res['items']), ensure_ascii=False).encode()).hexdigest()
            res['text'] = '\n'.join(f"{i['date']}\t{i['title']}\t{i['link']}" for i in items)
            res['summary'] = f"{len(items)} 条；最新：{items[0]['date'][:25]} {items[0]['title'][:80]}" if items else '0 条'
        elif kind == 'sitemap':
            items = parse_sitemap(body)
            res['items'] = {i['id']: {'title': i['title'], 'date': i['date']} for i in items}
            res['hash'] = hashlib.sha1(json.dumps([(i['id'], i['date']) for i in items]).encode()).hexdigest()
            res['text'] = '\n'.join(f"{i['date']}\t{i['id']}" for i in items)
            newest = max((i['date'] for i in items if i['date']), default='-')
            res['summary'] = f"{len(items)} 个 URL；最新 lastmod {newest[:19]}"
        elif kind == 'json':
            try:
                obj = json.loads(body)
            except Exception:
                # 有些 RDAP/JSON 服务对 Accept 挑剔；清掉前后噪声再试
                obj = json.loads(body[body.find('{'):body.rfind('}') + 1])
            picked = pick_fields(obj, src.get('fields'))
            res['fields'] = picked
            res['text'] = json.dumps(picked, ensure_ascii=False, indent=1, sort_keys=True)[:MAX_TEXT]
            res['hash'] = hashlib.sha1(res['text'].encode()).hexdigest()
            res['items'] = {}
            res['summary'] = '; '.join(f'{k}={json.dumps(v, ensure_ascii=False)[:60]}' for k, v in (picked.items() if isinstance(picked, dict) else []))[:300]
        else:  # html
            text = html_to_text(body, src.get('include'), src.get('exclude'))
            res['text'] = text
            res['hash'] = hashlib.sha1(text.encode()).hexdigest()
            res['items'] = {}
            first = text.split('\n')[0] if text else ''
            res['summary'] = f'{len(text)} 字符；首行：{first[:80]}'
            if src.get('id') == 'home':
                feeds = find_feeds(body, final or url)
                if feeds:
                    res['feeds_found'] = feeds[:3]
        return res
    except Exception as e:  # noqa: BLE001
        res['error'] = f'{type(e).__name__}: {str(e)[:200]}'
        res['status'] = res.get('status') or 0
        res['items'] = {}
        res['hash'] = None
        return res


# ----------------------------------------------------------------------------- compare
def compare(prev, cur, kind):
    """返回 (变化描述列表, 是否有实质变化)。"""
    notes = []
    if cur.get('error') and not cur.get('hash'):
        if not prev or not prev.get('error'):
            notes.append(f"抓取失败：{cur['error']}")
        return notes, False
    if not prev or prev.get('hash') is None:
        return ['首轮基线'], True
    if prev.get('error') and not cur.get('error'):
        notes.append(f"恢复可达（上轮 {prev['error']}）")
    if cur.get('error') and cur['error'] != prev.get('error'):
        notes.append(f"状态变化：{prev.get('error') or 'OK'} → {cur['error']}")
    pi, ci = prev.get('items') or {}, cur.get('items') or {}
    changed = False
    if pi or ci:
        new = [k for k in ci if k not in pi]
        gone = [k for k in pi if k not in ci]
        upd = [k for k in ci if k in pi and (ci[k].get('date') or '') != (pi[k].get('date') or '')]
        if new:
            changed = True
            shown = '；'.join(f"{ci[k].get('date', '')[:19]} {ci[k].get('title', '')[:90]}" for k in new[:8])
            notes.append(f"新增 {len(new)} 条：{shown}" + ('…' if len(new) > 8 else ''))
        if upd:
            changed = True
            shown = '；'.join(f"{ci[k].get('title', '')[:60]}（{(pi[k].get('date') or '')[:19]} → {(ci[k].get('date') or '')[:19]}）" for k in upd[:8])
            notes.append(f"更新 {len(upd)} 条：{shown}")
        if gone and kind != 'github':
            notes.append(f"消失 {len(gone)} 条（RSS 窗口滚动属正常）：{'；'.join(pi[k].get('title', '')[:50] for k in gone[:5])}")
        if kind == 'github' and gone:
            changed = True
            notes.append(f"仓库/事件消失 {len(gone)}：{'；'.join(k for k in gone[:5])}")
    if kind == 'github':
        pp, cp = prev.get('profile') or {}, cur.get('profile') or {}
        for k in ('name', 'company', 'blog', 'location', 'bio', 'public_repos', 'followers'):
            if pp.get(k) != cp.get(k):
                changed = True
                notes.append(f'档案 {k}：{pp.get(k)!r} → {cp.get(k)!r}')
    if kind in ('html', 'json') and prev.get('hash') != cur.get('hash') and cur.get('hash') \
            and not cur.get('error') and not prev.get('error'):
        # 只在「上轮 OK → 本轮 OK」之间比内容；进入/离开错误态的那一轮只记状态变化（第二轮 indiamart 429 曾被记成 −109 行）
        a = (prev.get('text') or '').split('\n')
        b = (cur.get('text') or '').split('\n')
        d = [ln for ln in difflib.unified_diff(a, b, lineterm='', n=0) if ln[:1] in '+-' and ln[:3] not in ('+++', '---')]
        adds_l = sorted(x[1:] for x in d if x.startswith('+'))
        dels_l = sorted(x[1:] for x in d if x.startswith('-'))
        if adds_l == dels_l:
            # 纯重排（轮播 / 随机推荐顺序）：不算变化，不写日志（第二轮 Astel 首页 HOT 轮播 +3 −3 同内容）
            return notes, changed
        changed = True
        adds, dels = len(adds_l), len(dels_l)
        notes.append(f'内容变化：+{adds} −{dels} 行')
        for ln in d[:14]:
            notes.append('    ' + ln[:160])
        if len(d) > 14:
            notes.append(f'    …（共 {len(d)} 行差异，全文见 snapshots/ 的 git diff）')
    return notes, changed


# ----------------------------------------------------------------------------- io
def load_json(p, default):
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    return default


def save_json(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def load_config(layers):
    """合并精选层 + 面层。返回 customers 列表，每个带 layer（成单 / A / B）与 label。"""
    cur = load_json(CFG, {'customers': []})
    auto = load_json(CFG_AUTO, {'customers': []})
    out, by = [], {}
    for c in cur.get('customers', []):
        c = dict(c)
        c['sources'] = [dict(x) for x in c['sources']]
        c['manual'] = list(c.get('manual', []))
        c['layer'] = '成单'
        c.setdefault('label', '')
        out.append(c)
        by[c['code']] = c
    for c in auto.get('customers', []):
        if c['code'] in by:          # 精选客户：面层只补充源 / 人工链接
            tgt = by[c['code']]
            have = {s.get('url') or s.get('login') for s in tgt['sources']}
            for sx in c['sources']:
                if (sx.get('url') or sx.get('login')) not in have:
                    sx = dict(sx)
                    sx['id'] = 'auto_' + sx['id']
                    tgt['sources'].append(sx)
            for m in c.get('manual', []):
                txt = f"{m.get('label')}: {m.get('url')}" if isinstance(m, dict) else m
                if txt not in tgt['manual']:
                    tgt['manual'].append(txt)
            continue
        c = dict(c)
        if c.get('layer') == 'P':          # P 级 / 资产池层（discover.py 从 P池_巡检表 生成；2026-10-29 起）
            pm = c.get('pool') or {}
            c['label'] = f"P 池 {pm.get('入池', '')} {pm.get('档位', '')}（{pm.get('来源', '')}）".strip()
        else:
            c['layer'] = c.get('grade') or 'B'
            c['label'] = f"{c['layer']} 级"
        out.append(c)
    return [c for c in out if c['layer'] in layers]


def feed_auto_src(url):
    return {'id': 'feed_auto', 'kind': 'rss', 'url': url, 'note': '首页 <link rel=alternate> 自动发现的 feed'}


def process_customer(c, state):
    """抓一个客户的全部源（同一客户内顺序、礼貌间隔）。返回 (code, [(src, prev, cur)])。"""
    results = []
    meta = (state.get('_meta') or {}).get(c['code']) or {}
    srcs = list(c['sources'])
    if meta.get('feed_auto') and not any(s['id'] == 'feed_auto' for s in srcs):
        srcs.append(feed_auto_src(meta['feed_auto']))
    has_feed = any(s['id'] == 'feed_auto' for s in srcs)
    lite = c.get('layer') in ('A', 'B', 'P')
    for s in list(srcs):
        key = f"{c['code']}/{s['id']}"
        prev = state.get(key)
        s = dict(s)
        if lite:
            s['_lite'] = True
        if s['kind'] == 'youtube_handle' and prev and prev.get('channel_id'):
            s['_cached_channel_id'] = prev['channel_id']
        cur = run_source(s)
        results.append((s, prev, cur))
        # 当轮就把新发现的 feed 抓一遍（只在还没有 feed_auto 时；首抓失败或 0 条则不采用）
        if cur.get('feeds_found') and not has_feed:
            has_feed = True
            fsrc = feed_auto_src(cur['feeds_found'][0])
            if lite:
                fsrc['_lite'] = True
            fcur = run_source(fsrc)
            if not fcur.get('error') and fcur.get('items'):
                results.append((fsrc, state.get(f"{c['code']}/feed_auto"), fcur))
            else:
                cur.pop('feeds_found', None)
        time.sleep(0.6)
    return c['code'], results


def prev_text(code, sid):
    p = os.path.join(SNAP, code, f'{sid}.txt')
    if not os.path.exists(p):
        return ''
    with open(p, encoding='utf-8') as f:
        lines = f.read().split('\n')
    return '\n'.join(lines[1:]).rstrip('\n') if lines and lines[0].startswith('# ') else '\n'.join(lines)


def trim_items(items):
    if not items or len(items) <= STATE_ITEMS:
        return items
    ks = sorted(items, key=lambda k: (items[k].get('date') or ''), reverse=True)[:STATE_ITEMS]
    return {k: items[k] for k in ks}


def _meta_of(state, code):
    return (state.get('_meta') or {}).get(code) or {}


def write_status(customers, state, changes_by_layer):
    # 精选层：逐源全表
    deal = [c for c in customers if c['layer'] == '成单']
    lines = ['# 成单客户 · 活跃平台监控 · 当前状态（T29-U18）', '',
             f'> 本轮 {TS}。监控清单 `scripts/web_watch/targets.json`（精选）+ `targets_auto.json`（面层，A/B 级见 `当前状态_AB.md`）；变化 append-only 见 `变化日志.md` / `变化日志_AB.md`；'
             f'每个源的最新规范化文本在 `snapshots/<客户码>/<源 id>.txt`（历史用 `git log -p` 看）。LinkedIn / Facebook / X / Instagram 有登录墙不抓，链接列在 manual 字段，由人工定期看。', '',
             '| 客户 | 标签 | 源 | 类型 | HTTP/状态 | 最近变化 | 摘要 |', '|---|---|---|---|---|---|---|']
    for c in deal:
        srcs = c['sources'] + ([feed_auto_src(_meta_of(state, c['code'])['feed_auto'])] if _meta_of(state, c['code']).get('feed_auto') else [])
        for s in srcs:
            key = f"{c['code']}/{s['id']}"
            st = state.get(key) or {}
            status = st.get('error') or (f"HTTP {st.get('status')}" if st.get('status') else '未抓')
            lines.append(f"| {c['code']} {c['name'].split('（')[0]} | {c.get('label', '')} | [{s['id']}]({s.get('url') or 'https://github.com/' + s.get('login', '')}) | {s['kind']} | {status} | {st.get('last_change_at', '-')} | {(st.get('summary') or '').replace('|', '／')[:120]} |")
    lines += ['', '## 人工查看链接（登录墙）']
    for c in deal:
        for m in c.get('manual', []):
            lines.append(f"- {c['code']}：{m}")
    lines += ['', '## 本轮变化（成单层）']
    lines += [(f'  - `{x.strip()}`' if x.startswith('    ') else f'- {x}') for x in changes_by_layer.get('成单', [])] or ['- 无']
    with open(os.path.join(OUT, '当前状态.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    # 面层：每客户一行
    ab = [c for c in customers if c['layer'] in ('A', 'B')]
    if ab:
        n_src = sum(len(c['sources']) for c in ab)
        cats = {}
        for c in ab:
            for s_ in c['sources']:
                e = (state.get(f"{c['code']}/{s_['id']}") or {}).get('error')
                if e:
                    k = re.sub(r'\(.*', '', e).strip()[:36]
                    cats[k] = cats.get(k, 0) + 1
        cat_line = '；'.join(f'{k} ×{v}' for k, v in sorted(cats.items(), key=lambda x: -x[1])[:10]) or '无'
        L = ['# A/B 级客户 · 动态监控 · 当前状态（T29-U19）', '',
             f'> 失败分类（最近一次状态）：{cat_line}。403 = 站点反爬（运行器 IP 被拦，人工看）；YouTube 404 = YouTube 对数据中心 IP 的拦截（设仓库 secret YT_API_KEY 后走官方 API）；其它 404 = 页面不存在；SSL/连接/DNS 错误 = 站点本身问题，连续多轮失败再从清单摘掉。', '',
             f'> 本轮 {TS}。客户 {len(ab)} 家 / 源 {n_src} 个。清单 `scripts/web_watch/targets_auto.json`（discover.py 离线生成：首页 / sitemap / 新闻栏目 / YouTube / GitHub / Telegram / VK + 运行时自动发现的 feed）。'
             f'变化见 `变化日志_AB.md`；每客户文本快照在 `snapshots/<客户码>/`。「最近变化」= 任一源最近一次内容变化的时间（首轮 = 基线时间）；「人工看」= 有登录墙的社媒，链接在 targets_auto.json 的 manual 字段。', '',
             '| 客户 | 级 | 源数 | 本轮可达/失败 | 最近变化 | 最近变化摘要 | 人工看 |', '|---|---|---|---|---|---|---|']
        for c in sorted(ab, key=lambda x: (x['layer'], x['code'])):
            srcs = c['sources'] + ([{'id': 'feed_auto'}] if _meta_of(state, c['code']).get('feed_auto') else [])
            sts = [state.get(f"{c['code']}/{s['id']}") or {} for s in srcs]
            ok = sum(1 for st in sts if st.get('status') and not st.get('error'))
            bad = sum(1 for st in sts if st.get('error'))
            lc = max((st.get('last_change_at') or '-' for st in sts), default='-')
            summ = _meta_of(state, c['code']).get('last_change_note') or ''
            man = '、'.join((m.get('label', '') if isinstance(m, dict) else str(m)) for m in c.get('manual', [])[:5])
            L.append(f"| {c['code']} {c['name'][:28].replace('|', '／')} | {c['layer']} | {len(srcs)} | {ok}/{bad} | {lc} | {summ.replace('|', '／')[:100]} | {man} |")
        with open(os.path.join(OUT, '当前状态_AB.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(L) + '\n')
    # P 池层：每户一行（T29-U117 资产池；两个月一巡，日常自动抓首页 / feed，人工巡检时看本表 + 变化日志_P.md）
    pool = [c for c in customers if c['layer'] == 'P']
    if pool:
        n_src = sum(len(c['sources']) for c in pool)
        L = ['# P 级 / 资产池 · 动态监控 · 当前状态（T29-U117/U120）', '',
             f'> 本轮 {TS}。P 池 {len(pool)} 户 / 源 {n_src} 个（清单 `scripts/web_watch/targets_auto.json` layer=P，discover.py 从 `data/saga_clients/P池_巡检表_*.csv` 生成：首页（多域名户再看第 2 域名）+ 运行时自动发现的 feed；SC 码沿用 entities / 快照里的社媒与 GitHub）。'
             f'变化 append-only 见 `变化日志_P.md`；快照 `snapshots/<客户码>/`。人工巡检（两个月一次，下次见巡检表「下次巡检」列）时按本表「最近变化」+ 巡检表「巡检项」逐户看；「人工看」= 登录墙社媒链接。', '',
             '| 客户 | 入池 | 档 | 来源 | 区域组 | 源数 | 可达/失败 | 最近变化 | 最近变化摘要 | 人工看 |', '|---|---|---|---|---|---|---|---|---|---|']
        for c in sorted(pool, key=lambda x: ((x.get('pool') or {}).get('入池', ''), {'★★': 0, '★': 1, '○': 2, '△': 3, '☆': 4}.get((x.get('pool') or {}).get('档位', ''), 9), x['code'])):
            pm = c.get('pool') or {}
            srcs = c['sources'] + ([{'id': 'feed_auto'}] if _meta_of(state, c['code']).get('feed_auto') else [])
            sts = [state.get(f"{c['code']}/{s['id']}") or {} for s in srcs]
            ok = sum(1 for st in sts if st.get('status') and not st.get('error'))
            bad = sum(1 for st in sts if st.get('error'))
            lc = max((st.get('last_change_at') or '-' for st in sts), default='-')
            summ = _meta_of(state, c['code']).get('last_change_note') or ''
            man = '、'.join((m.get('label', '') if isinstance(m, dict) else str(m)) for m in c.get('manual', [])[:5])
            L.append(f"| {c['code']} {c['name'][:28].replace('|', '／')} | {pm.get('入池', '')} | {pm.get('档位', '')} | {pm.get('来源', '')} | {pm.get('区域组', '')} | {len(srcs)} | {ok}/{bad} | {lc} | {summ.replace('|', '／')[:100]} | {man} |")
        with open(os.path.join(OUT, '当前状态_P.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(L) + '\n')


def append_log(path, title, changes, errors, n_sources):
    new = not os.path.exists(path)
    if not new and os.path.getsize(path) > 3_000_000:      # 超 3 MB 归档一份，保持 append-only
        os.replace(path, path.replace('.md', f'_至{TS[:10]}.md'))
        new = True
    with open(path, 'a', encoding='utf-8') as f:
        if new:
            f.write(f'# {title}（append-only；每轮一节，无变化也记）\n')
        f.write(f'\n## {TS}（源 {n_sources}）\n')
        for x in changes:
            if x.startswith('### '):
                f.write(f'\n{x}\n')
            elif x.startswith('    '):
                f.write(f'  - `{x.strip()}`\n')
            else:
                f.write(f'- {x}\n')
        if not changes:
            f.write('- 无变化\n')
        if errors:
            f.write(f'- 本轮抓取失败 {len(errors)}：' + '；'.join(errors[:40]) + ('…' if len(errors) > 40 else '') + '\n')


def snapshot_missing(elapsed):
    """T29-U131：巡检后顺手补抓长期客户群（Saga + External + Planet 仓 A/B）缺失 / 失败的官网快照。
    沙箱访问不了客户网站，只有 Actions 运行器能抓；清单 = Saga entities A/B（site_snapshot.py 原生）+ data/长期客户群_补快照清单_*.json
    （External / Planet 仓）。时间预算 = 60 分钟 − 巡检已用时间（工作流上限 90 分钟），跑不完下次接着跑（已成功的不重抓）。"""
    budget = int(60 * 60 - elapsed)
    if budget < 300:
        print(f'snapshot_missing: 预算不足（{budget}s）→ 跳过')
        return
    lists = sorted(glob.glob(os.path.join(ROOT, 'data', '长期客户群_补快照清单_*.json')))
    env = dict(os.environ, GRADES='A,B', FORCE='0', GIT_COMMIT='0', WORKERS='12', COMMIT_EVERY='0', TIME_BUDGET=str(budget),
               EXTRA_SITES=lists[-1] if lists else '')
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'beautifulsoup4', 'lxml'], cwd=ROOT, check=False, timeout=300)
    except Exception as e:
        print('pip bs4 failed (fallback to regex parser):', e)
    print(f'snapshot_missing: budget {budget}s, extra list {os.path.basename(env["EXTRA_SITES"]) if env["EXTRA_SITES"] else "—"}', flush=True)
    try:
        subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'saga_clients', 'site_snapshot.py')], cwd=ROOT, env=env, check=False, timeout=budget + 600)
    except Exception as e:
        print('snapshot_missing failed:', e)


def snapshot_thicken():
    """T29-U131：快照一到就消费（LT-T03）：Saga 研究档 / External 卡 / Planet 仓备注 的在线态、在卖品牌、页面公开联系方式、型号对位校正，
    产出 data/长期客户群_快照加厚_<日>.csv + 快照打回候选表；只改 JSON / CSV（MD 由下次会话的渲染链刷新）；失败不阻断巡检提交。"""
    try:
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'saga_clients', 'lt_snapshot_thicken.py')], cwd=ROOT, check=False, timeout=900,
                           capture_output=True, text=True)
        print('snapshot_thicken:', (r.stdout or '').strip().splitlines()[-1:] or r.returncode, (r.stderr or '')[-300:])
    except Exception as e:
        print('snapshot_thicken failed:', e)


def git_commit(msg):
    if not os.environ.get('GITHUB_ACTIONS'):
        print('not in GitHub Actions → skip commit')
        return
    # 推送目标 = 实际检出的分支，而不是触发工作流的分支：customer-watch.yml 存在默认分支 main 上时
    # GITHUB_REF_NAME == 'main'，但 checkout 的是 arena/3f35b9b3-planet；若按 GITHUB_REF_NAME 推，会把本分支 rebase 到 main 上并推过去（2026-10-23 06:20Z 修）。
    ref = os.environ.get('WATCH_PUSH_REF') or ''
    if not ref:
        try:
            cur = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=ROOT, check=False,
                                 capture_output=True, text=True, timeout=60).stdout.strip()
        except Exception:
            cur = ''
        ref = cur if cur and cur != 'HEAD' else 'arena/3f35b9b3-planet'
    if ref in ('main', 'master'):
        print(f'refuse to push to {ref}; using arena/3f35b9b3-planet')
        ref = 'arena/3f35b9b3-planet'
    sh = lambda *a: subprocess.run(a, cwd=ROOT, check=False, timeout=600)  # noqa: E731
    sh('git', 'config', 'user.name', 'smartbyte-archiver[bot]')
    sh('git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    sh('git', 'add', '-A', os.path.relpath(OUT, ROOT))
    sh('git', 'add', '-A', 'data/saga_clients/site_snapshots')  # T29-U131：巡检后补抓的官网快照一起提交
    for extra in ('data/saga_clients/research', 'data/external_clients/research', 'data/客户名单_Planet渠道_2026-10.csv'):  # LT-T03 快照加厚落点
        sh('git', 'add', '-A', extra)
    for f in glob.glob(os.path.join(ROOT, 'data', '长期客户群_快照*.csv')):
        sh('git', 'add', '-A', os.path.relpath(f, ROOT))
    r = subprocess.run(['git', 'commit', '-q', '-m', msg], cwd=ROOT, check=False)
    if r.returncode != 0:
        print('nothing to commit')
        return
    for attempt in range(3):
        sh('git', 'pull', '-q', '--rebase', 'origin', ref)
        p = subprocess.run(['git', 'push', '-q', 'origin', f'HEAD:{ref}'], cwd=ROOT, check=False)
        if p.returncode == 0:
            print('pushed')
            return
        time.sleep(10)
    print('push failed')


# ----------------------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*', help='只跑这些客户码')
    ap.add_argument('--layer', default='all', help='all | 成单 | A | B | P（逗号分隔可多选；deal = 成单；P = P 级 / 资产池）')
    ap.add_argument('--limit', type=int, default=0, help='最多跑多少个客户（测试用）')
    ap.add_argument('--workers', type=int, default=WORKERS)
    ap.add_argument('--no-commit', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--no-snapshot', action='store_true', help='不补抓 A/B 官网快照（默认在 Actions 里巡检后顺手补抓）')
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    layers = {'成单', 'A', 'B', 'P'} if args.layer.strip().lower() == 'all' else {x.strip() for x in args.layer.replace('deal', '成单').split(',')}  # 2026-10-29：手动 Run 填 ALL 也认
    customers = load_config(layers)
    if args.only:
        customers = [c for c in customers if c['code'] in args.only]
    if args.limit:
        customers = customers[:args.limit]
    state = load_json(STATE, {})
    state.setdefault('_meta', {})
    os.makedirs(SNAP, exist_ok=True)
    changes_by_layer = {'成单': [], 'A': [], 'B': [], 'P': []}
    errors_by_layer = {'成单': [], 'A': [], 'B': [], 'P': []}
    n_sources = {'成单': 0, 'A': 0, 'B': 0, 'P': 0}
    t0 = time.time()
    by_code = {c['code']: c for c in customers}
    done = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        for code, results in ex.map(lambda c: process_customer(c, state), customers):
            c = by_code[code]
            layer = c['layer']
            meta = state['_meta'].setdefault(code, {})
            for s, prev, cur in results:
                key = f"{code}/{s['id']}"
                n_sources[layer] += 1
                if s['kind'] in ('html', 'json') and prev is not None and 'text' not in prev:
                    prev = dict(prev)
                    prev['text'] = prev_text(code, s['id'])
                notes, changed = compare(prev, cur, s['kind'])
                if cur.get('error'):
                    errors_by_layer[layer].append(f"{key}：{cur['error']}")
                entry = {k: cur.get(k) for k in ('kind', 'fetched_at', 'status', 'hash', 'summary', 'error', 'profile', 'fields', 'channel_id', 'final_url')}
                entry['items'] = trim_items(cur.get('items') or {})
                entry['last_change_at'] = TS if changed else (prev or {}).get('last_change_at', '-' if (prev or cur.get('error')) else TS)
                entry['first_seen'] = (prev or {}).get('first_seen') or TS
                entry['url'] = s.get('url') or s.get('login')
                state[key] = {k: v for k, v in entry.items() if v is not None}
                if cur.get('feeds_found'):
                    meta['feeds_found'] = cur['feeds_found']
                    if s['id'] == 'home' and not meta.get('feed_auto'):
                        meta['feed_auto'] = cur['feeds_found'][0]
                if s['id'] == 'feed_auto' and cur.get('error') and prev is None:
                    meta.pop('feed_auto', None)      # 自动 feed 首抓就失败 → 不采用
                if cur.get('text') is not None:
                    d = os.path.join(SNAP, code)
                    os.makedirs(d, exist_ok=True)
                    with open(os.path.join(d, f"{s['id']}.txt"), 'w', encoding='utf-8') as f:
                        f.write(f"# {code} {c['name']} · {s['id']} · {s.get('url') or s.get('login')} · fetched {TS} · HTTP {cur.get('status')}\n")
                        f.write((cur.get('text') or '')[:SNAP_TEXT.get(layer, 12_000)] + '\n')
                label = f"{code} {c['name'].split('（')[0][:30]} · {s['id']}（{s['kind']}）"
                if notes and (changed or any(n.startswith(('抓取失败', '恢复可达', '状态变化')) for n in notes)):
                    changes_by_layer[layer].append(f'{label}：' + notes[0])
                    if layer == '成单':
                        changes_by_layer[layer] += list(notes[1:])
                    else:
                        changes_by_layer[layer] += [n for n in notes[1:] if not n.startswith('    ')][:2] + [n for n in notes[1:] if n.startswith('    ')][:6]
                    if changed and notes[0] != '首轮基线':
                        meta['last_change_note'] = f"{TS[:10]} {s['id']}：{notes[0][:90]}"
                    elif notes[0] == '首轮基线' and not meta.get('last_change_note'):
                        meta['last_change_note'] = f'{TS[:10]} 首轮基线'
            done += 1
            if done % 50 == 0:
                print(f'… {done}/{len(customers)} customers, {time.time() - t0:.0f}s', flush=True)
    save_json(STATE, state)
    tot_changes = sum(len(v) for v in changes_by_layer.values())
    tot_err = sum(len(v) for v in errors_by_layer.values())
    if '成单' in layers:
        append_log(os.path.join(OUT, '变化日志.md'), '成单客户 · 活跃平台监控 · 变化日志', changes_by_layer['成单'], errors_by_layer['成单'], n_sources['成单'])
    if layers & {'A', 'B'}:
        ab_changes = (['### A 级'] + changes_by_layer['A'] if changes_by_layer['A'] else []) + (['### B 级'] + changes_by_layer['B'] if changes_by_layer['B'] else [])
        append_log(os.path.join(OUT, '变化日志_AB.md'), 'A/B 级客户 · 动态监控 · 变化日志', ab_changes, errors_by_layer['A'] + errors_by_layer['B'], n_sources['A'] + n_sources['B'])
    if 'P' in layers:
        append_log(os.path.join(OUT, '变化日志_P.md'), 'P 级 / 资产池 · 动态监控 · 变化日志', changes_by_layer['P'], errors_by_layer['P'], n_sources['P'])
    write_status(load_config({'成单', 'A', 'B', 'P'}), state, changes_by_layer)
    print(f'{TS} customers={len(customers)} sources={sum(n_sources.values())} changed_or_flagged={tot_changes} errors={tot_err} elapsed={time.time() - t0:.0f}s')
    if os.environ.get('GITHUB_ACTIONS') and not args.no_snapshot:
        snapshot_missing(time.time() - t0)
        snapshot_thicken()
    if not args.no_commit:
        # 提交信息里按「源」计数（只数顶层条目，不数缩进的 diff 明细行；2026-10-23 07:03Z 修：此前把明细行也算进去，06:51Z 轮显示 55 实为 11 个源）
        n_top = {k: sum(1 for x in v if not x.startswith((' ', '###'))) for k, v in changes_by_layer.items()}
        git_commit(f"监控：客户动态 {TS}（成单 {n_top['成单']} / A {n_top['A']} / B {n_top['B']} / P 池 {n_top['P']} 个源有变化；抓取失败 {tot_err}；源 {sum(n_sources.values())}）")
    return 0


# ----------------------------------------------------------------------------- selftest（不联网）
def selftest():
    rss = '<?xml version="1.0"?><rss><channel><title>t</title><item><title>A &amp; B</title><link>https://x/a</link><pubDate>Mon, 06 Jul 2026 10:00:00 +0000</pubDate></item><item><title>C</title><guid>g2</guid></item></channel></rss>'
    atom = '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:yt="http://www.youtube.com/xml/schemas/2015"><entry><id>yt:video:1</id><title>V1</title><link rel="alternate" href="https://youtu.be/1"/><published>2026-10-01T00:00:00+00:00</published></entry></feed>'
    sm = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://vilink.us/product/im28/</loc><lastmod>2024-09-20T00:00:00+00:00</lastmod></url></urlset>'
    page = '<html><head><script>var a=1</script><style>.x{}</style></head><body><!-- c --><div id="n">Nav</div><h1>Бит.Блог</h1><p>6 июля 2026</p><p>Оборудование под Вашим брендом</p><div>Корзина пуста 0</div><p>Cloudflare Ray ID: abc</p></body></html>'
    f = parse_feed(rss)
    assert [i['title'] for i in f] == ['A & B', 'C'] and f[0]['id'] == 'https://x/a' and f[1]['id'] == 'g2', f
    a = parse_feed(atom)
    assert a[0]['id'] == 'yt:video:1' and a[0]['link'] == 'https://youtu.be/1' and a[0]['date'].startswith('2026-10-01'), a
    s = parse_sitemap(sm)
    assert s[0]['id'].endswith('/im28/') and s[0]['date'].startswith('2024-09-20'), s
    t = html_to_text(page, include='(?is)<h1[^>]*>.*')
    assert t.startswith('Бит.Блог') and 'Nav' not in t and 'var a' not in t and 'Корзина' not in t, t
    t2 = html_to_text(page)
    assert t2.split('\n')[0] == 'Nav', t2
    assert youtube_channel_id('x "channelId":"UCCAG46dVy-wxXtO-_b7fTPA" y') == 'UCCAG46dVy-wxXtO-_b7fTPA'
    prev = {'hash': 'h1', 'items': {'g2': {'title': 'C', 'date': ''}}, 'text': 'l1\nl2'}
    cur = {'hash': 'h2', 'items': {'g2': {'title': 'C', 'date': ''}, 'https://x/a': {'title': 'A & B', 'date': 'Mon, 06 Jul 2026'}}, 'text': 'l1\nl3'}
    n, ch = compare(prev, cur, 'rss')
    assert ch and n[0].startswith('新增 1 条'), n
    n, ch = compare(prev, cur, 'html')
    assert ch and any(x.startswith('内容变化：+1 −1') for x in n), n
    n, ch = compare(None, cur, 'html')
    assert n == ['首轮基线'] and ch
    n, ch = compare(prev, {'error': 'HTTP 522', 'hash': None, 'items': {}}, 'html')
    assert not ch and n[0].startswith('抓取失败')
    assert dotted({'a': [{'b': 1}]}, 'a.0.b') == 1
    ff = find_feeds('<html><head><link rel="alternate" type="application/rss+xml" title="x" href="/feed/"><link rel="alternate" type="application/rss+xml" href="https://a.b/comments/feed/"></head></html>', 'https://a.b/')
    assert ff == ['https://a.b/feed/'], ff
    cfg = load_json(CFG, None)
    assert cfg and len(cfg['customers']) == 20, len(cfg['customers'])
    merged = load_config({'成单', 'A', 'B', 'P'})
    ids = set()
    layers = {}
    for c in merged:
        layers[c['layer']] = layers.get(c['layer'], 0) + 1
        for s in c['sources']:
            assert s['kind'] in ('rss', 'html', 'json', 'sitemap', 'github', 'youtube_handle'), s
            assert (s.get('url') or s.get('login')), s
            k = f"{c['code']}/{s['id']}"
            assert k not in ids, k
            ids.add(k)
    print(f'selftest OK · customers={len(merged)} layers={layers} sources={len(ids)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
