#!/usr/bin/env python3
"""成单客户「活跃平台」监控（T29-U18，2026-10-23）。只读，不发任何消息。

用法（GitHub Actions 运行器；Arena 沙箱无外网，只能跑 --selftest）：
    python scripts/web_watch/watch.py              # 抓全部源，写 data/customer_watch/，在 Actions 内自动提交推送
    python scripts/web_watch/watch.py --only SA-168 SA-006
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
import hashlib
import html as _html
import json
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CFG = os.path.join(HERE, 'targets.json')
OUT = os.path.join(ROOT, 'data', 'customer_watch')
STATE = os.path.join(OUT, 'state.json')
SNAP = os.path.join(OUT, 'snapshots')
TS = _dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 SagaWatch/1.0'
BROWSER_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
TIMEOUT = 35
MAX_TEXT = 60_000
MAX_ITEMS = 300

try:
    import requests  # noqa: E402
except Exception:  # pragma: no cover
    requests = None


# ----------------------------------------------------------------------------- fetch
def fetch(url, accept=None):
    """返回 (status_code, text, final_url)。失败抛异常。"""
    if requests is None:
        raise RuntimeError('requests not installed')
    h = {'User-Agent': UA, 'Accept-Language': 'en,tr;q=0.8,ru;q=0.7,th;q=0.6,zh;q=0.5'}
    if accept:
        h['Accept'] = accept
    last = None
    for attempt in range(3):
        try:
            if attempt:   # 第 2 次起换成普通浏览器 UA（首轮基线：vilinknet.com 403 / sundartechno feed 429 / govtribe 403 都是反爬 UA 过滤）
                h['User-Agent'] = BROWSER_UA
                h['Accept'] = h.get('Accept') or 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            r = requests.get(url, headers=h, timeout=TIMEOUT, allow_redirects=True)
            if (r.status_code >= 500 or r.status_code in (403, 429)) and attempt < 2:
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


# ----------------------------------------------------------------------------- per-source
def run_source(src):
    """返回 dict：status, hash, items(dict id→{title,date}), text(可选), fields(可选), error(可选), profile(可选)。"""
    kind = src['kind']
    res = {'kind': kind, 'fetched_at': TS}
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
        if kind == 'youtube_handle':
            code, page, _ = fetch(url, accept='text/html')
            cid = youtube_channel_id(page)
            if not cid:
                raise RuntimeError(f'channelId not found (HTTP {code})')
            res['channel_id'] = cid
            url = f'https://www.youtube.com/feeds/videos.xml?channel_id={cid}'
            kind = 'rss'
        acc = ('application/rss+xml, application/atom+xml, application/xml, application/json, text/html;q=0.8, */*;q=0.5'
               if kind in ('rss', 'sitemap', 'json') else 'text/html,application/xhtml+xml,*/*;q=0.8')
        try:
            code, body, final = fetch(url, accept=acc)
        except Exception:
            if not src.get('url_fallback'):
                raise
            code = 599
        if code >= 400 and src.get('url_fallback'):
            code, body, final = fetch(src['url_fallback'], accept=acc)
        res['status'] = code
        res['final_url'] = final
        if code >= 400:
            # 仍记录错误页文本（例如 522/404 也是状态）
            res['text'] = html_to_text(body)[:4000]
            res['hash'] = hashlib.sha1(f'HTTP {code}'.encode()).hexdigest()
            res['items'] = {}
            res['error'] = f'HTTP {code}'
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
    if kind in ('html', 'json') and prev.get('hash') != cur.get('hash') and cur.get('hash'):
        changed = True
        a = (prev.get('text') or '').split('\n')
        b = (cur.get('text') or '').split('\n')
        d = [ln for ln in difflib.unified_diff(a, b, lineterm='', n=0) if ln[:1] in '+-' and ln[:3] not in ('+++', '---')]
        adds = sum(1 for x in d if x.startswith('+'))
        dels = sum(1 for x in d if x.startswith('-'))
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


def write_status(cfg, state, run_changes):
    lines = ['# 成单客户 · 活跃平台监控 · 当前状态（T29-U18）', '',
             f'> 本轮 {TS}。监控清单 `scripts/web_watch/targets.json`；变化 append-only 见 `变化日志.md`；每个源的最新规范化文本在 `snapshots/<客户码>/<源 id>.txt`（历史用 `git log -p` 看）。'
             f'LinkedIn / Facebook / X / Instagram 有登录墙不抓，链接列在各客户 manual 字段，由人工定期看。', '',
             '| 客户 | 标签 | 源 | 类型 | HTTP/状态 | 最近变化 | 摘要 |', '|---|---|---|---|---|---|---|']
    for c in cfg['customers']:
        for s in c['sources']:
            key = f"{c['code']}/{s['id']}"
            st = state.get(key) or {}
            status = st.get('error') or (f"HTTP {st.get('status')}" if st.get('status') else '未抓')
            lines.append(f"| {c['code']} {c['name'].split('（')[0]} | {c['label']} | [{s['id']}]({s.get('url') or 'https://github.com/' + s.get('login', '')}) | {s['kind']} | {status} | {st.get('last_change_at', '-')} | {(st.get('summary') or '').replace('|', '／')[:120]} |")
    lines += ['', '## 人工查看链接（登录墙）']
    for c in cfg['customers']:
        for m in c.get('manual', []):
            lines.append(f"- {c['code']}：{m}")
    lines += ['', '## 本轮变化']
    lines += [f'- {x}' for x in run_changes] or ['- 无']
    with open(os.path.join(OUT, '当前状态.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def git_commit(n_changes, n_err):
    if not os.environ.get('GITHUB_ACTIONS'):
        print('not in GitHub Actions → skip commit')
        return
    ref = os.environ.get('GITHUB_REF_NAME') or 'arena/3f35b9b3-planet'
    sh = lambda *a: subprocess.run(a, cwd=ROOT, check=False, timeout=600)  # noqa: E731
    sh('git', 'config', 'user.name', 'smartbyte-archiver[bot]')
    sh('git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    sh('git', 'add', '-A', os.path.relpath(OUT, ROOT))
    r = subprocess.run(['git', 'commit', '-q', '-m', f'监控：成单客户活跃平台 {TS}（变化 {n_changes} / 抓取失败 {n_err}）'], cwd=ROOT, check=False)
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
    ap.add_argument('--no-commit', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    cfg = load_json(CFG, {'customers': []})
    state = load_json(STATE, {})
    os.makedirs(SNAP, exist_ok=True)
    run_changes, errors = [], []
    for c in cfg['customers']:
        if args.only and c['code'] not in args.only:
            continue
        for s in c['sources']:
            key = f"{c['code']}/{s['id']}"
            prev = state.get(key)
            cur = run_source(s)
            notes, changed = compare(prev, cur, s['kind'])
            if cur.get('error'):
                errors.append(f"{key}：{cur['error']}")
            entry = {k: cur.get(k) for k in ('kind', 'fetched_at', 'status', 'hash', 'items', 'summary', 'error', 'profile', 'fields', 'channel_id', 'final_url')}
            entry['text'] = (cur.get('text') or '')[:MAX_TEXT]
            entry['last_change_at'] = TS if changed else (prev or {}).get('last_change_at', TS if not prev else '-')
            entry['first_seen'] = (prev or {}).get('first_seen') or TS
            state[key] = entry
            if cur.get('text') is not None:
                d = os.path.join(SNAP, c['code'])
                os.makedirs(d, exist_ok=True)
                with open(os.path.join(d, f"{s['id']}.txt"), 'w', encoding='utf-8') as f:
                    f.write(f"# {c['code']} {c['name']} · {s['id']} · {s.get('url') or s.get('login')} · fetched {TS} · HTTP {cur.get('status')}\n")
                    f.write(entry['text'] + '\n')
            label = f"{c['code']} {c['name'].split('（')[0]} · {s['id']}（{s['kind']}）"
            if notes and (changed or any(n.startswith(('抓取失败', '恢复可达', '状态变化')) for n in notes)):
                run_changes.append(f'{label}：' + notes[0])
                run_changes += [n for n in notes[1:]]
            print(f"{key}: {cur.get('status')} {'CHANGED' if changed else 'same'} {cur.get('error') or ''} {(cur.get('summary') or '')[:100]}")
            time.sleep(1.0)
    save_json(STATE, state)
    logp = os.path.join(OUT, '变化日志.md')
    new = not os.path.exists(logp)
    with open(logp, 'a', encoding='utf-8') as f:
        if new:
            f.write('# 成单客户 · 活跃平台监控 · 变化日志（append-only；每轮一节，无变化也记）\n')
        f.write(f'\n## {TS}\n')
        for x in run_changes:
            f.write(f'- {x}\n' if not x.startswith('    ') else f'  - `{x.strip()}`\n')
        if not run_changes:
            f.write('- 无变化\n')
        if errors:
            f.write(f'- 本轮抓取失败 {len(errors)}：' + '；'.join(errors[:20]) + '\n')
    write_status(cfg, state, run_changes)
    print(f'{TS} sources_changed_or_flagged={len(run_changes)} errors={len(errors)}')
    if not args.no_commit:
        git_commit(len(run_changes), len(errors))
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
    cfg = load_json(CFG, None)
    assert cfg and len(cfg['customers']) == 20, len(cfg['customers'])
    ids = set()
    for c in cfg['customers']:
        for s in c['sources']:
            assert s['kind'] in ('rss', 'html', 'json', 'sitemap', 'github', 'youtube_handle'), s
            assert (s.get('url') or s.get('login')), s
            k = f"{c['code']}/{s['id']}"
            assert k not in ids, k
            ids.add(k)
    print(f'selftest OK · customers={len(cfg["customers"])} sources={len(ids)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
