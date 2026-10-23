#!/usr/bin/env python3
"""GitHub 监控：freddy36（Frederik Kriewitz，NYNEX / fiberONE，SA-013）及 SmartByte 相关上游文件。

宪法条款（T29-U16，2026-10-22）：此人/此仓库的任何更新都极为敏感，必须每轮开工先跑一次本脚本，
把变化带时间戳入库（append-only）。不改历史快照，只追加。

用法（仓库根目录）：
    python3 scripts/github_watch/watch.py            # 抓取 → 与上次比对 → 写快照/变化日志/当前状态 → 归档上游文件
    python3 scripts/github_watch/watch.py --no-files # 不下载上游文件（只比对元数据）

依赖：`gh` 已登录（GITHUB_TOKEN 亦可），python3 标准库。网络只需 api.github.com。
输出（均在 data/github_watch/）：
    snapshots/<UTC>.json   本轮原始快照（append-only）
    latest.json            最新快照（供下次比对）
    变化日志.md             每轮一节：与上一快照的差异（无差异也记一行，证明查过）
    当前状态.md             人读摘要（每轮重写）
    upstream_files/        上游仓库里 SmartByte 相关文件的本地副本（按 blob sha 变更才重写）
    own_repos/<repo>/README.md  他本人（非 fork）仓库的 README 副本
"""
import base64
import json
import os
import re
import subprocess
import sys
import time
import datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'data', 'github_watch')
CFG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'targets.json')
TS = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
NO_FILES = '--no-files' in sys.argv


def _gh_once(path, headers=None):
    cmd = ['gh', 'api', path]
    for h in headers or []:
        cmd += ['-H', h]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return {'_error': (r.stderr or r.stdout).strip()[:300]}
    txt = r.stdout.strip()
    if not txt:
        return {}
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        return {'_raw': txt[:2000]}


def gh_search(path, prev_value=None, errors=None):
    """搜索类端点：GitHub 限 30 次/分钟，调用间隔 2.2 s；失败时沿用上一快照的值并登记错误，
    避免把「限流导致的空结果」误判成「消失/新增」。"""
    time.sleep(2.2)
    r = _gh_once(path)
    if isinstance(r, dict) and '_error' in r:
        if errors is not None:
            errors.append({'path': path, 'error': r['_error'][:160]})
        return prev_value if prev_value is not None else r
    return r


def gh(path, paginate=False, headers=None, max_pages=20):
    """GET 一个 REST 端点。paginate=True 时自行按 page=1..N 翻页（旧版 gh 无 --slurp），
    把 list 页或 search 的 {items:[...]} 页拍平成一个 list。"""
    if not paginate:
        return _gh_once(path, headers)
    flat = []
    sep = '&' if '?' in path else '?'
    for page in range(1, max_pages + 1):
        data = _gh_once(f'{path}{sep}page={page}', headers)
        if isinstance(data, dict) and '_error' in data:
            return data if page == 1 else flat
        items = data['items'] if isinstance(data, dict) and 'items' in data else data
        if not isinstance(items, list):
            return flat if flat else data
        flat.extend(items)
        if len(items) < 100 or (isinstance(data, dict) and 'items' in data and len(flat) >= data.get('total_count', 0)):
            break
    return flat


def load_cfg():
    with open(CFG, encoding='utf-8') as f:
        return json.load(f)


def snapshot(cfg, prev=None):
    user = cfg['user']
    prev = prev or {}
    snap = {'ts': TS, 'user_login': user, '_errors': []}
    # 1 档案
    p = gh(f'users/{user}')
    snap['profile'] = {k: p.get(k) for k in ('login', 'id', 'name', 'company', 'blog', 'location', 'email', 'bio',
                                             'public_repos', 'public_gists', 'followers', 'following',
                                             'created_at', 'updated_at')} if '_error' not in p else p
    # 2 仓库
    repos = gh(f'users/{user}/repos?per_page=100&type=owner&sort=pushed', paginate=True)
    snap['repos'] = {}
    for r in repos if isinstance(repos, list) else []:
        snap['repos'][r['name']] = {
            'fork': r.get('fork'), 'pushed_at': r.get('pushed_at'), 'updated_at': r.get('updated_at'),
            'stars': r.get('stargazers_count'), 'default_branch': r.get('default_branch'),
            'description': r.get('description'), 'homepage': r.get('homepage'),
        }
    # 3 关注的 fork：分支 + 领先上游的提交
    snap['fork_branches'] = {}
    for fk in cfg.get('forks', []):
        repo, upstream, base = fk['repo'], fk['upstream'], fk.get('base', 'master')
        branches = gh(f'repos/{user}/{repo}/branches?per_page=100', paginate=True)
        d = {}
        for b in branches if isinstance(branches, list) else []:
            name = b['name']
            cmp_ = gh(f'repos/{upstream}/compare/{base}...{user}:{name}')
            entry = {'sha': b['commit']['sha'][:12]}
            if '_error' in cmp_:
                entry['compare_error'] = cmp_['_error']
            else:
                entry['ahead'] = cmp_.get('ahead_by')
                entry['behind'] = cmp_.get('behind_by')
                entry['commits'] = [
                    {'date': c['commit']['committer']['date'], 'sha': c['sha'][:12],
                     'msg': c['commit']['message'].split('\n')[0][:160],
                     'files_url': c.get('html_url')}
                    for c in cmp_.get('commits', [])
                ]
            d[name] = entry
        snap['fork_branches'][repo] = {'upstream': upstream, 'branches': d}
    # 4 他发起的 PR / issue（全 GitHub）
    snap['authored'] = {}
    for kind in ('pull-request', 'issue'):
        time.sleep(2.2)
        items = gh(f'search/issues?q=author:{user}+is:{kind}&sort=updated&order=desc&per_page=100', paginate=True)
        if isinstance(items, dict) and '_error' in items:
            snap['_errors'].append({'path': f'authored:{kind}', 'error': items['_error'][:160]})
            snap['authored'][kind] = (prev.get('authored') or {}).get(kind, [])
            continue
        lst = []
        for it in items if isinstance(items, list) else []:
            lst.append({'repo': it['repository_url'].rsplit('/repos/', 1)[-1], 'number': it['number'],
                        'title': it['title'], 'state': it['state'], 'created': it['created_at'],
                        'updated': it['updated_at'], 'closed': it.get('closed_at'),
                        'merged': (it.get('pull_request') or {}).get('merged_at'), 'url': it['html_url']})
        snap['authored'][kind] = lst
    # 5 他参与（评论/被 @/审阅）的最近 issue/PR
    snap['involves_recent'] = []
    for kind in ('pull-request', 'issue'):
        prev_inv = [x for x in prev.get('involves_recent', []) if x.get('kind') == kind]
        inv = gh_search(f'search/issues?q=involves:{user}+-author:{user}+is:{kind}&sort=updated&order=desc&per_page=50',
                        prev_value={'items': None}, errors=snap['_errors'])
        if inv.get('items') is None:
            snap['involves_recent'] += prev_inv
            continue
        snap['involves_recent'] += [
            {'repo': it['repository_url'].rsplit('/repos/', 1)[-1], 'number': it['number'], 'title': it['title'],
             'kind': kind, 'author': it['user']['login'], 'updated': it['updated_at'], 'url': it['html_url']}
            for it in (inv.get('items', []) if isinstance(inv, dict) else [])]
    # 6 公开事件（GitHub 只保留 90 天 / 300 条）
    ev = gh(f'users/{user}/events/public?per_page=100', paginate=True)
    snap['events'] = []
    for e in ev if isinstance(ev, list) else []:
        pl = e.get('payload') or {}
        snap['events'].append({
            'id': e['id'], 'at': e['created_at'], 'type': e['type'], 'repo': e['repo']['name'],
            'action': pl.get('action'), 'ref': pl.get('ref'),
            'title': ((pl.get('pull_request') or {}).get('title') or (pl.get('issue') or {}).get('title')
                      or ((pl.get('comment') or {}).get('body') or '')[:120]),
            'commits': [c['message'].split('\n')[0][:120] for c in pl.get('commits', [])][:10],
        })
    # 7 star / following / gists
    st = gh(f'users/{user}/starred?per_page=100', paginate=True,
            headers=['Accept: application/vnd.github.star+json'])
    snap['starred'] = [{'repo': s['repo']['full_name'], 'starred_at': s.get('starred_at')}
                       for s in st if isinstance(s, dict) and 'repo' in s] if isinstance(st, list) else st
    fo = gh(f'users/{user}/following?per_page=100', paginate=True)
    snap['following'] = [f['login'] for f in fo] if isinstance(fo, list) else fo
    gi = gh(f'users/{user}/gists?per_page=100', paginate=True)
    snap['gists'] = [{'id': g['id'], 'desc': g.get('description'), 'updated': g['updated_at'],
                      'files': list((g.get('files') or {}).keys())} for g in gi] if isinstance(gi, list) else gi
    # 8 上游仓库中的 SmartByte 相关文件（任何人改动都算信号）
    snap['upstream'] = {}
    for up in cfg.get('upstream_repos', []):
        repo, branch, pat = up['repo'], up.get('branch', 'master'), up.get('pattern', 'smartbyte')
        tree = gh(f'repos/{repo}/git/trees/{branch}?recursive=1')
        files = {}
        rx = re.compile(pat, re.I)
        for t in (tree.get('tree', []) if isinstance(tree, dict) else []):
            if t['type'] == 'blob' and rx.search(t['path']):
                last = gh(f'repos/{repo}/commits?path={t["path"]}&sha={branch}&per_page=1')
                lc = {}
                if isinstance(last, list) and last:
                    c = last[0]
                    lc = {'sha': c['sha'][:12], 'date': c['commit']['committer']['date'],
                          'author': (c.get('author') or {}).get('login') or c['commit']['author']['name'],
                          'msg': c['commit']['message'].split('\n')[0][:140]}
                files[t['path']] = {'blob': t['sha'][:12], 'size': t.get('size'), 'last_commit': lc}
        # 该仓库里提到 smartbyte 的 issue/PR（任何作者）
        mentions = []
        prev_m = (prev.get('upstream', {}).get(repo) or {}).get('smartbyte_mentions', [])
        for kind in ('pull-request', 'issue'):
            iss = gh_search(f'search/issues?q=smartbyte+repo:{repo}+is:{kind}&sort=updated&order=desc&per_page=50',
                            prev_value={'items': None}, errors=snap['_errors'])
            if iss.get('items') is None:
                mentions += [m for m in prev_m if m.get('is_pr') == (kind == 'pull-request')]
                continue
            mentions += [{'number': it['number'], 'title': it['title'], 'author': it['user']['login'],
                          'state': it['state'], 'created': it['created_at'], 'updated': it['updated_at'],
                          'is_pr': kind == 'pull-request', 'url': it['html_url']}
                         for it in (iss.get('items', []) if isinstance(iss, dict) else [])]
        snap['upstream'][repo] = {'branch': branch, 'files': files, 'smartbyte_mentions': mentions,
                                  'tree_truncated': tree.get('truncated') if isinstance(tree, dict) else None}
    # 9 全站搜索（SmartByte / Saga 的型号与名字；新命中 = 新的 OEM 客户或新的集成）
    snap['searches'] = {}
    for q in cfg.get('code_searches', []):
        r = gh_search(f'search/code?q={q}&per_page=50', prev_value=prev.get('searches', {}).get('code:' + q), errors=snap['_errors'])
        if isinstance(r, dict) and 'hits' in r:   # 沿用了上一快照
            snap['searches']['code:' + q] = r
            continue
        if isinstance(r, dict) and 'items' in r:
            snap['searches']['code:' + q] = {
                'total': r.get('total_count'),
                'hits': sorted({it['repository']['full_name'] + ':' + it['path'] for it in r['items']})}
        else:
            snap['searches']['code:' + q] = r
    for q in cfg.get('repo_searches', []):
        r = gh_search(f'search/repositories?q={q}&per_page=50', prev_value=prev.get('searches', {}).get('repo:' + q), errors=snap['_errors'])
        if isinstance(r, dict) and 'hits' in r:
            snap['searches']['repo:' + q] = r
            continue
        if isinstance(r, dict) and 'items' in r:
            snap['searches']['repo:' + q] = {
                'total': r.get('total_count'),
                'hits': sorted(it['full_name'] + ' (' + (it.get('pushed_at') or '')[:10] + ')' for it in r['items'])}
        else:
            snap['searches']['repo:' + q] = r
    return snap


SEEN_PATH = os.path.join(OUT, 'seen.json')


def load_seen():
    if os.path.exists(SEEN_PATH):
        return {k: set(v) for k, v in json.load(open(SEEN_PATH, encoding='utf-8')).items()}
    return {}


def save_seen(seen):
    with open(SEEN_PATH, 'w', encoding='utf-8') as f:
        json.dump({k: sorted(v) for k, v in seen.items()}, f, ensure_ascii=False, indent=0)


def diff(prev, cur, seen=None):
    """返回变化条目列表（中文、可直接写入日志）。
    seen = 历史累计已见键集合（跨所有快照）：GitHub 搜索索引偶尔漏返回旧条目，若只与上一快照比会反复误报「新」；
    因此 PR/issue/参与/提及/搜索命中/事件 只有在**从未见过**时才算新。"""
    out = []
    seen = seen if seen is not None else {}
    def first_time(bucket, key):
        b = seen.setdefault(bucket, set())
        if key in b:
            return False
        b.add(key)
        return True
    if not prev:
        out.append('首轮基线建立（无上一快照可比）')
        # 仍要把当前所有键登记为已见
        for kind in ('pull-request', 'issue'):
            for x in cur.get('authored', {}).get(kind, []):
                first_time('authored', f'{x["repo"]}#{x["number"]}')
        for x in cur.get('involves_recent', []):
            first_time('involves', f'{x["repo"]}#{x["number"]}')
        for e in cur.get('events', []):
            first_time('events', e['id'])
        for repo, d in cur.get('upstream', {}).items():
            for m in d.get('smartbyte_mentions', []):
                first_time('mentions', f'{repo}#{m["number"]}')
        for q, r in cur.get('searches', {}).items():
            if isinstance(r, dict) and 'hits' in r:
                for h in r['hits']:
                    first_time('search:' + q, h)
        return out
    # 档案
    for k in ('name', 'company', 'blog', 'location', 'bio', 'public_repos', 'followers', 'following'):
        a, b = (prev.get('profile') or {}).get(k), (cur.get('profile') or {}).get(k)
        if a != b:
            out.append(f'档案字段 {k}：{a!r} → {b!r}')
    # 仓库
    pr, cr = prev.get('repos', {}), cur.get('repos', {})
    for n in sorted(set(cr) - set(pr)):
        out.append(f'新仓库 {n}（fork={cr[n]["fork"]}，pushed {cr[n]["pushed_at"]}）：{cr[n].get("description")}')
    for n in sorted(set(pr) - set(cr)):
        out.append(f'仓库消失/改名/转私有：{n}')
    for n in sorted(set(cr) & set(pr)):
        if cr[n]['pushed_at'] != pr[n]['pushed_at']:
            out.append(f'仓库 {n} 有新推送：{pr[n]["pushed_at"]} → {cr[n]["pushed_at"]}')
        if cr[n].get('description') != pr[n].get('description'):
            out.append(f'仓库 {n} 描述变更：{pr[n].get("description")!r} → {cr[n].get("description")!r}')
    # fork 分支
    for repo, d in cur.get('fork_branches', {}).items():
        pb = (prev.get('fork_branches', {}).get(repo) or {}).get('branches', {})
        cb = d.get('branches', {})
        for b in sorted(set(cb) - set(pb)):
            cms = cb[b].get('commits') or []
            out.append(f'fork {repo} 新分支 {b}（领先上游 {cb[b].get("ahead")}）：' +
                       ' ‖ '.join(f'{c["date"][:10]} {c["msg"]}' for c in cms[:5]))
        for b in sorted(set(pb) - set(cb)):
            out.append(f'fork {repo} 分支删除：{b}')
        for b in sorted(set(pb) & set(cb)):
            if pb[b].get('sha') != cb[b].get('sha'):
                cms = cb[b].get('commits') or []
                out.append(f'fork {repo} 分支 {b} 有新提交 {pb[b].get("sha")} → {cb[b].get("sha")}：' +
                           ' ‖ '.join(f'{c["date"][:10]} {c["msg"]}' for c in cms[-5:]))
    # PR / issue
    for kind in ('pull-request', 'issue'):
        pk = {(x['repo'], x['number']): x for x in prev.get('authored', {}).get(kind, [])}
        ck = {(x['repo'], x['number']): x for x in cur.get('authored', {}).get(kind, [])}
        for key in sorted(set(ck) - set(pk)):
            x = ck[key]
            if first_time('authored', f'{x["repo"]}#{x["number"]}'):
                out.append(f'新 {kind} {x["repo"]}#{x["number"]}「{x["title"]}」{x["created"][:10]} {x["url"]}')
        for key in sorted(set(ck) & set(pk)):
            a, b = pk[key], ck[key]
            if (a['state'], a.get('merged'), a['updated']) != (b['state'], b.get('merged'), b['updated']):
                out.append(f'{kind} {b["repo"]}#{b["number"]}「{b["title"]}」状态/更新：'
                           f'{a["state"]}/{(a.get("merged") or "")[:10]}/{a["updated"][:10]} → '
                           f'{b["state"]}/{(b.get("merged") or "")[:10]}/{b["updated"][:10]}')
    # 参与
    pi = {(x['repo'], x['number']) for x in prev.get('involves_recent', [])}
    for x in cur.get('involves_recent', []):
        if (x['repo'], x['number']) not in pi and first_time('involves', f'{x["repo"]}#{x["number"]}'):
            out.append(f'新参与（评论/被提及/审阅）{x.get("kind")} {x["repo"]}#{x["number"]}「{x["title"]}」by {x.get("author")} 更新 {x["updated"][:10]} {x["url"]}')
    # 事件
    pe = {e['id'] for e in prev.get('events', [])}
    for e in cur.get('events', []):
        if e['id'] not in pe and first_time('events', e['id']):
            out.append(f'新公开事件 {e["at"]} {e["type"]} {e["repo"]} {e.get("action") or ""} {e.get("ref") or ""} {e.get("title") or ""}'.strip())
    # star / following / gists
    ps = {s['repo'] for s in prev.get('starred', []) if isinstance(s, dict)}
    for s in cur.get('starred', []) if isinstance(cur.get('starred'), list) else []:
        if s['repo'] not in ps:
            out.append(f'新 star：{s["repo"]}（{(s.get("starred_at") or "")[:10]}）')
    pf = set(prev.get('following', []) if isinstance(prev.get('following'), list) else [])
    for f in cur.get('following', []) if isinstance(cur.get('following'), list) else []:
        if f not in pf:
            out.append(f'新 following：{f}')
    pg = {g['id'] for g in prev.get('gists', []) if isinstance(g, dict)}
    for g in cur.get('gists', []) if isinstance(cur.get('gists'), list) else []:
        if g['id'] not in pg:
            out.append(f'新 gist：{g["id"]} {g.get("desc")} {g.get("files")}')
    # 上游文件
    for repo, d in cur.get('upstream', {}).items():
        pfiles = (prev.get('upstream', {}).get(repo) or {}).get('files', {})
        cfiles = d.get('files', {})
        for p in sorted(set(cfiles) - set(pfiles)):
            lc = cfiles[p].get('last_commit', {})
            out.append(f'上游 {repo} 新文件 {p}（{lc.get("date", "")[:10]} by {lc.get("author")}：{lc.get("msg")}）')
        for p in sorted(set(pfiles) - set(cfiles)):
            out.append(f'上游 {repo} 文件消失：{p}')
        for p in sorted(set(pfiles) & set(cfiles)):
            if pfiles[p]['blob'] != cfiles[p]['blob']:
                lc = cfiles[p].get('last_commit', {})
                out.append(f'上游 {repo} 文件变更 {p}（{lc.get("date", "")[:10]} by {lc.get("author")}：{lc.get("msg")}）')
        pm = {m['number'] for m in (prev.get('upstream', {}).get(repo) or {}).get('smartbyte_mentions', [])}
        for m in d.get('smartbyte_mentions', []):
            if m['number'] not in pm and first_time('mentions', f'{repo}#{m["number"]}'):
                out.append(f'上游 {repo} 新的 SmartByte 相关 {"PR" if m["is_pr"] else "issue"} #{m["number"]}「{m["title"]}」by {m["author"]} {m["created"][:10]} {m["url"]}')
    # 搜索
    for q, r in cur.get('searches', {}).items():
        if not isinstance(r, dict) or 'hits' not in r:
            continue
        pr_ = prev.get('searches', {}).get(q) or {}
        ph = set(pr_.get('hits', [])) if isinstance(pr_, dict) else set()
        for h in r['hits']:
            if h not in ph and first_time('search:' + q, h):
                out.append(f'搜索 {q} 新命中：{h}')
        if isinstance(pr_, dict) and pr_.get('total') != r.get('total'):
            out.append(f'搜索 {q} 总数：{pr_.get("total")} → {r.get("total")}')
    return out


def archive_files(cfg, cur, prev):
    """把上游 SmartByte 相关文件与他本人仓库 README 拉到本地（blob 变了才重写）。"""
    saved = []
    for repo, d in cur.get('upstream', {}).items():
        pfiles = (prev.get('upstream', {}).get(repo) or {}).get('files', {}) if prev else {}
        for path, meta in d.get('files', {}).items():
            dest = os.path.join(OUT, 'upstream_files', repo.replace('/', '__'), path)
            if os.path.exists(dest) and pfiles.get(path, {}).get('blob') == meta['blob']:
                continue
            c = gh(f'repos/{repo}/contents/{path}?ref={d.get("branch", "master")}')
            if isinstance(c, dict) and c.get('encoding') == 'base64':
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, 'wb') as f:
                    f.write(base64.b64decode(c['content']))
                saved.append(path)
            elif isinstance(c, dict) and c.get('download_url'):
                r = subprocess.run(['curl', '-sL', c['download_url']], capture_output=True)
                if r.returncode == 0:
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    open(dest, 'wb').write(r.stdout)
                    saved.append(path)
    user = cfg['user']
    for name, meta in cur.get('repos', {}).items():
        if meta.get('fork'):
            continue
        dest = os.path.join(OUT, 'own_repos', name, 'README.md')
        if os.path.exists(dest) and prev and (prev.get('repos', {}).get(name) or {}).get('pushed_at') == meta['pushed_at']:
            continue
        c = gh(f'repos/{user}/{name}/readme')
        if isinstance(c, dict) and c.get('encoding') == 'base64':
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f:
                f.write(base64.b64decode(c['content']))
            saved.append(f'{name}/README')
    return saved


def write_status(cfg, cur, changes):
    u = cfg['user']
    p = cur.get('profile', {})
    lines = [f'# GitHub 监控 · 当前状态（{u} = Frederik Kriewitz，NYNEX / fiberONE，SA-013）', '',
             f'> 本轮抓取 {cur["ts"]}。每轮开工先跑 `python3 scripts/github_watch/watch.py`；变化见 `变化日志.md`，原始快照见 `snapshots/`。', '',
             '## 档案', f'- {p.get("name")}（@{p.get("login")}，id {p.get("id")}）· 注册 {str(p.get("created_at"))[:10]} · 公开仓库 {p.get("public_repos")} · followers {p.get("followers")} · 档案更新 {p.get("updated_at")}', '',
             '## 与 SmartByte / Saga 直接相关']
    for repo, d in cur.get('upstream', {}).items():
        lines.append(f'### 上游 {repo}（{d.get("branch")}）')
        for path, m in sorted(d.get('files', {}).items()):
            lc = m.get('last_commit', {})
            lines.append(f'- `{path}`（{m.get("size")} B，最后提交 {str(lc.get("date"))[:10]} by {lc.get("author")}：{lc.get("msg")}）')
        if d.get('smartbyte_mentions'):
            lines.append(f'- 该仓库提到 SmartByte 的 issue/PR（{len(d["smartbyte_mentions"])}）：' +
                         '；'.join(f'#{m["number"]} {m["title"]}（{m["author"]}，{m["created"][:10]}，{m["state"]}）' for m in d['smartbyte_mentions']))
        lines.append('')
    lines.append('## 他的 fork 上领先上游的分支（= 未合并/进行中的工作）')
    for repo, d in cur.get('fork_branches', {}).items():
        for b, m in sorted(d.get('branches', {}).items()):
            if m.get('ahead'):
                cms = m.get('commits') or []
                lines.append(f'- {repo}:{b} 领先 {m["ahead"]}：' + ' ‖ '.join(f'{c["date"][:10]} {c["msg"]}' for c in cms[-4:]))
    lines.append('')
    lines.append('## 近期 PR（按更新时间，前 15）')
    for x in cur.get('authored', {}).get('pull-request', [])[:15]:
        lines.append(f'- {x["created"][:10]} → {x["updated"][:10]} {x["state"]}{" merged" if x.get("merged") else ""} {x["repo"]}#{x["number"]} {x["title"]}')
    lines.append('')
    lines.append('## 近 90 天公开事件')
    for e in cur.get('events', [])[:30]:
        lines.append(f'- {e["at"]} {e["type"]} {e["repo"]} {e.get("action") or ""} {e.get("title") or ""}'.rstrip())
    if not cur.get('events'):
        lines.append('- （无）')
    lines.append('')
    lines.append('## 全站搜索')
    for q, r in cur.get('searches', {}).items():
        if isinstance(r, dict) and 'hits' in r:
            lines.append(f'- {q}：{r.get("total")} 命中 → ' + '；'.join(r['hits'][:25]))
        else:
            lines.append(f'- {q}：{r}')
    lines.append('')
    lines.append('## 本轮变化')
    lines += [f'- {c}' for c in changes] or ['- 无']
    with open(os.path.join(OUT, '当前状态.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def main():
    cfg = load_cfg()
    os.makedirs(os.path.join(OUT, 'snapshots'), exist_ok=True)
    latest = os.path.join(OUT, 'latest.json')
    prev = json.load(open(latest, encoding='utf-8')) if os.path.exists(latest) else None
    seen = load_seen()
    if not seen:
        # 首次：用历史全部快照播种已见集合，避免把旧条目当新
        import glob
        for sp in sorted(glob.glob(os.path.join(OUT, 'snapshots', '*.json'))):
            try:
                diff(None, json.load(open(sp, encoding='utf-8')), seen)
            except Exception:
                pass
    cur = snapshot(cfg, prev)
    changes = diff(prev, cur, seen)
    save_seen(seen)
    saved = [] if NO_FILES else archive_files(cfg, cur, prev)
    with open(os.path.join(OUT, 'snapshots', TS.replace(':', '') + '.json'), 'w', encoding='utf-8') as f:
        json.dump(cur, f, ensure_ascii=False, indent=1)
    with open(latest, 'w', encoding='utf-8') as f:
        json.dump(cur, f, ensure_ascii=False, indent=1)
    log = os.path.join(OUT, '变化日志.md')
    new = not os.path.exists(log)
    with open(log, 'a', encoding='utf-8') as f:
        if new:
            f.write('# GitHub 监控 · 变化日志（append-only；每轮一节，无变化也记）\n')
        f.write(f'\n## {TS}\n')
        for c in changes:
            f.write(f'- {c}\n')
        if not changes:
            f.write('- 无变化\n')
        if saved:
            f.write(f'- 本轮归档/更新文件 {len(saved)}：' + '；'.join(saved[:30]) + '\n')
        if cur.get('_errors'):
            f.write(f'- 本轮 API 失败 {len(cur["_errors"])}（已沿用上一快照对应数据）：' + '；'.join(e['path'][:80] for e in cur['_errors'][:10]) + '\n')
    write_status(cfg, cur, changes)
    print(f'{TS} changes={len(changes)} saved_files={len(saved)}')
    for c in changes:
        print(' -', c[:200])


if __name__ == '__main__':
    main()
