#!/usr/bin/env python3
"""A/B 客户 GitHub 足迹扫描（第 79 批 · 多维加厚 · 2026-10-27）。

只认两种「硬匹配」，宁缺毋滥：
1. 组织：候选 slug（域名主体 / 公司名压缩）→ GET /orgs/{slug}，且该组织的 blog 或 email 含客户域名；
2. 用户：GET /search/users?q=<域名> in:email → 逐个 GET /users/{login} 核对公开邮箱确实在该域名下。
命中写入 data/saga_clients/github_presence.json（code → {domain, orgs[], users[], checked_at}），render.py 读入「多维画像 → GitHub 足迹」。
限速：search 30 次/分钟（每次后 sleep 2.2 s），core 5,000/小时；全程只读公开数据。
用法：python3 scripts/saga_clients/github_presence.py [--grades AB] [--limit N] [--resume]
"""
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATA = os.path.join(ROOT, 'data', 'saga_clients')
OUT = os.path.join(DATA, 'github_presence.json')
FREEMAIL = {'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'live.com', 'icloud.com', 'aol.com', 'msn.com', 'yandex.ru', 'mail.ru',
            'bk.ru', 'list.ru', 'inbox.ru', 'rambler.ru', 'ya.ru', 'naver.com', 'qq.com', '163.com', '126.com', 'protonmail.com', 'proton.me',
            'gmx.de', 'gmx.net', 'web.de', 't-online.de', 'wp.pl', 'o2.pl', 'onet.pl', 'interia.pl', 'seznam.cz', 'abv.bg', 'ukr.net', 'me.com',
            'mac.com', 'ymail.com', 'zoho.com', 'mail.com', 'email.com', 'libero.it', 'orange.fr', 'free.fr', 'wanadoo.fr', 'btinternet.com',
            'eim.ae', 'emirates.net.ae', 'rediffmail.com', 'sbcglobal.net', 'comcast.net', 'verizon.net', 'att.net', 'bigpond.com', 'optusnet.com.au',
            'telenet.be', 'skynet.be', 'ziggo.nl', 'bluewin.ch', 'sapo.pt', 'walla.co.il', 'yahoo.co.uk', 'yahoo.fr', 'yahoo.de', 'yahoo.es',
            'yahoo.it', 'yahoo.in', 'yahoo.co.in', 'hotmail.co.uk', 'hotmail.fr', 'hotmail.it', 'hotmail.es', 'hotmail.de', 'live.co.uk',
            'outlook.es', 'outlook.de', 'outlook.fr', 'googlemail.com', 'tutanota.com', 'pm.me', 'hanmail.net', 'daum.net', 'nate.com'}


def api(path, ok404=True):
    """gh api 封装：返回 (status, json)。404 → (404, None)；限速 → 等待后重试。"""
    for attempt in range(6):
        p = subprocess.run(['gh', 'api', '-i', path], capture_output=True, text=True)
        out = p.stdout
        head, _, body = out.partition('\n\n') if '\n\n' in out else (out, '', '')
        if '\r\n\r\n' in out:
            head, _, body = out.partition('\r\n\r\n')
        m = re.match(r'HTTP/\S+ (\d+)', head or '')
        status = int(m.group(1)) if m else (p.returncode and 599)
        if status == 404:
            return 404, None
        if status in (403, 429) or 'rate limit' in (p.stderr or '').lower():
            reset = re.search(r'X-Ratelimit-Reset: (\d+)', head, re.I)
            wait = max(5, int(reset.group(1)) - int(time.time()) + 2) if reset else 70
            print(f'  限速，等待 {min(wait, 300)} s', flush=True)
            time.sleep(min(wait, 300))
            continue
        if status >= 500 or status == 599:
            time.sleep(10)
            continue
        try:
            return status, json.loads(body) if body.strip() else None
        except Exception:
            return status, None
    return 599, None


def slugs_for(ent, domain):
    cands = []
    sld = domain.split('.')[0]
    if len(sld) >= 4:
        cands.append(sld)
        if '-' in sld:
            cands.append(sld.replace('-', ''))
    name = re.sub(r'[（(].*?[）)]', ' ', ent.get('name') or '')
    words = [w for w in re.split(r'[^A-Za-z0-9]+', name) if w]
    stop = {'ltd', 'llc', 'inc', 'gmbh', 'sa', 'srl', 'sro', 'bv', 'ag', 'co', 'kg', 'spzoo', 'sp', 'zoo', 'limited', 'company', 'corp',
            'corporation', 'the', 'and', 'of', 'plc', 'pty', 'sdn', 'bhd', 'as', 'oy', 'ab', 'aps', 'doo', 'd', 'o', 'tic', 'ltd.', 'san',
            've', 'ticaret', 'sanayi', 'elektronik', 'technologies', 'technology', 'systems', 'solutions', 'group', 'networks', 'network'}
    core = [w.lower() for w in words if w.lower() not in stop and not w.isdigit()]
    if core:
        s1 = ''.join(core[:2])
        if len(s1) >= 4 and s1 not in cands:
            cands.append(s1)
        if len(core[0]) >= 5 and core[0] not in cands:
            cands.append(core[0])
    return cands[:3]


def norm(s):
    s = re.sub(r'[（(].*?[）)]', ' ', s or '').lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    stop = {'ltd', 'llc', 'inc', 'gmbh', 'sa', 'srl', 'sro', 'bv', 'ag', 'co', 'kg', 'limited', 'company', 'corp', 'corporation', 'the', 'plc', 'pty',
            'sdn', 'bhd', 'oy', 'ab', 'aps', 'doo', 'tic', 'san', 've', 'ticaret', 'sanayi', 'a', 's', 'spol', 'sp', 'z', 'o'}
    return ' '.join(w for w in s.split() if w not in stop)


def reg_domain(host):
    host = (host or '').lower().strip()
    host = re.sub(r'^https?://', '', host).split('/')[0].split('@')[-1]
    if host.startswith('www.'):
        host = host[4:]
    return host


def conflicting(u, ent, domain):
    """非强匹配时：账号公开的 blog / email 若落在客户域名之外的域（含同名不同后缀），判为别家。"""
    mine = {reg_domain(x) for x in (ent.get('domains') or [])} | {domain}
    for field in ('blog', 'email'):
        v = u.get(field) or ''
        if not v:
            continue
        host = reg_domain(v)
        if not host:
            continue
        if any(host == m or host.endswith('.' + m) for m in mine):
            continue
        return True
    return False


def verify(login, ent, domain):
    """取账号详情，判断是否属于该客户：strong = blog/email 含域名；name = 组织名与公司名一致；company = 用户 company 字段含公司名/域名。"""
    st, u = api(f'users/{login}')
    if st != 200 or not u:
        return None
    blog = (u.get('blog') or '').lower()
    mail = (u.get('email') or '').lower()
    comp = (u.get('company') or '').lower()
    cname = norm(ent.get('name'))
    tname = norm(ent.get('_title') or '')
    how = None
    if domain in blog or mail.endswith('@' + domain):
        how = 'strong'
    elif u.get('type') == 'Organization' and cname and len(cname) >= 6 and norm(u.get('name')) == cname:
        how = 'name'
    elif u.get('type') == 'Organization' and len(domain.split('.')[0]) >= 6 and norm(u.get('name')).replace(' ', '') == domain.split('.')[0]:
        how = 'name'
    elif u.get('type') == 'Organization' and tname and len(tname) >= 8 and norm(u.get('name')) and (norm(u.get('name')) == tname or tname.startswith(norm(u.get('name')) + ' ')):
        how = 'name'
    elif u.get('type') == 'User' and comp and (domain.split('.')[0] in comp or (cname and len(cname) >= 6 and cname in norm(comp))):
        how = 'company'
    if not how:
        return None
    if how != 'strong' and conflicting(u, ent, domain):
        return None                                   # 名称像但 blog / email 指向别的域名（snexus.com vs snexus.com.tr 之类）→ 不是同一家
    return {'login': u['login'], 'type': u.get('type'), 'url': u['html_url'], 'name': u.get('name'), 'blog': u.get('blog'), 'email': u.get('email'),
            'company': u.get('company'), 'public_repos': u.get('public_repos'), 'created_at': u.get('created_at'), 'updated_at': u.get('updated_at'),
            'bio': (u.get('bio') or u.get('description') or '')[:160], 'match': how}


def main():
    args = sys.argv[1:]
    grades = 'AB'
    limit = None
    if '--grades' in args:
        grades = args[args.index('--grades') + 1]
    if '--limit' in args:
        limit = int(args[args.index('--limit') + 1])
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    ents = [e for e in ents if e['grade'] in grades]
    if '--codes' in args:
        want = set(args[args.index('--codes') + 1].split(','))
        ents = [e for e in ents if e['code'] in want]
        args.append('--redo')
    res = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    digest_path = os.path.join(DATA, 'site_digest.json')
    digest = json.load(open(digest_path, encoding='utf-8')) if os.path.exists(digest_path) else {}
    todo = []
    for e in ents:
        doms = [d for d in (e.get('domains') or []) if d and d.lower() not in FREEMAIL]
        if not doms:
            continue
        if e['code'] in res and '--redo' not in args:
            continue
        todo.append((e, doms[0].lower()))
    if limit:
        todo = todo[:limit]
    print(f'待查 {len(todo)} 户（已有 {len(res)}）', flush=True)
    n_hit = 0
    for i, (e, domain) in enumerate(todo, 1):
        rec = {'domain': domain, 'accounts': [], 'repos_mentioning': [], 'checked_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
        e['_title'] = re.split(r'[|–—\-:]', (digest.get(e['code']) or {}).get('title') or '')[0]
        seen = set()
        cands = []
        # a. 组织 slug 直查
        for slug in slugs_for(e, domain):
            st, j = api(f'orgs/{slug}')
            if st == 200 and j:
                cands.append(j['login'])
        # b. 名称搜组织 / 域名主体搜账号 / 公开邮箱域名
        queries = []
        cname = norm(e.get('name'))
        if cname and (len(cname.split()) >= 2 or len(cname) >= 6) and cname != domain.split('.')[0]:
            queries.append(f'"{cname}" type:org')
        sld = domain.split('.')[0]
        if len(sld) >= 5:
            queries.append(sld)
        title = norm(re.split(r'[|–—\-:]', (digest.get(e['code']) or {}).get('title') or '')[0])
        tw = [w for w in title.split() if w not in {'home', 'homepage', 'welcome', 'official', 'site', 'website', 'to'}][:3]
        if len(tw) >= 2 and ' '.join(tw) != cname:
            queries.append('"' + ' '.join(tw) + '" type:org')
        queries.append(f'{domain} in:email')
        for q in queries:
            st, j = api('search/users?q=' + q.replace(' ', '+').replace('"', '%22') + '&per_page=5')
            time.sleep(2.2)
            if st == 200 and j and j.get('items'):
                cands += [it['login'] for it in j['items'][:5]]
        for login in cands:
            if login.lower() in seen:
                continue
            seen.add(login.lower())
            v = verify(login, e, domain)
            if v:
                rec['accounts'].append(v)
        # c. 提及域名的仓库（README / 描述 / 名称）
        st, j = api(f'search/repositories?q=%22{domain}%22+in:readme,description,name&per_page=5')
        time.sleep(2.2)
        if st == 200 and j and j.get('items'):
            for r in j['items'][:5]:
                rec['repos_mentioning'].append({'full_name': r['full_name'], 'url': r['html_url'], 'desc': (r.get('description') or '')[:120],
                                                'stars': r.get('stargazers_count'), 'pushed_at': r.get('pushed_at'), 'owner_type': r['owner'].get('type')})
        # d. 命中账号的最近仓库
        for a in rec['accounts']:
            st, repos = api(f"users/{a['login']}/repos?sort=pushed&per_page=6")
            if st == 200 and repos:
                a['repos'] = [{'name': r['name'], 'pushed_at': r.get('pushed_at'), 'lang': r.get('language'), 'desc': (r.get('description') or '')[:120],
                               'fork': r.get('fork')} for r in repos]
        res[e['code']] = rec
        if rec['accounts'] or rec['repos_mentioning']:
            n_hit += 1
            print(f"  ✓ {e['code']} {domain}: {[(a['login'], a['match']) for a in rec['accounts']]} repos {[r['full_name'] for r in rec['repos_mentioning']]}", flush=True)
        if i % 10 == 0 or i == len(todo):
            json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            print(f'{i}/{len(todo)} 已存（命中 {n_hit}）', flush=True)
    json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'完成：{len(res)} 户，命中 {sum(1 for v in res.values() if v.get("accounts") or v.get("repos_mentioning"))}')


if __name__ == '__main__':
    main()
