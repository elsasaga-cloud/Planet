#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GitHub 技术足迹扫描（api.github.com 匿名；每户：① 邮箱域 in:email 用户 ② 公司名 type:org ③ 域名出现在仓库描述/README）。
结果写 data/saga_clients/intel_github_<date>.json；由 intel_batches 脚本或本脚本 --apply 写入研究档（kind GitHub/技术足迹；未得也记）。
速率：匿名搜索 10 次/分钟 → 自动 sleep。用法：python3 github_scan.py [--apply] [--limit N]
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-30'
OUT = os.path.join(SD, f'intel_github_{DATE}.json')
FREE = re.compile(r'^(gmail|hotmail|yahoo|outlook|live|icloud|mail|yandex|protonmail|aol|gmx|web|list|bk|inbox|rambler|163|qq|126|telus|yahoo\.com)\.', re.I)


def gh(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'saga-intel', 'Accept': 'application/vnd.github+json'})
    for attempt in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=20)
            rem = int(r.headers.get('X-RateLimit-Remaining') or 1)
            d = json.loads(r.read())
            if rem <= 1:
                time.sleep(62)
            return d
        except urllib.error.HTTPError as ex:
            if ex.code in (403, 429):
                time.sleep(65)
                continue
            if ex.code == 422:
                return {'items': [], 'total_count': 0, 'err': 422}
            return {'items': [], 'total_count': 0, 'err': ex.code}
        except Exception as ex:  # noqa
            time.sleep(5)
    return {'items': [], 'total_count': 0, 'err': 'retry'}


def main():
    apply = '--apply' in sys.argv
    limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else 10 ** 6
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    A = [c for c, e in ents.items() if e['grade'] == 'A']
    res = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    done = 0
    for c in A:
        if c in res or done >= limit:
            continue
        e = ents[c]
        doms = [d for d in (e.get('domains') or []) if re.match(r'^[\w.-]+\.[a-z]{2,}$', str(d), re.I) and not FREE.match(d)]
        name = re.sub(r'[^\w .&-]', ' ', str(e.get('name') or '')).strip()
        rec = {'code': c, 'name': e.get('name'), 'domains': doms, 'users': [], 'orgs': [], 'repos': [], 'queries': []}
        if doms:
            d0 = doms[0]
            q = f'{d0} in:email'
            rec['queries'].append(q)
            u = gh('https://api.github.com/search/users?q=' + urllib.parse.quote(q) + '&per_page=10')
            rec['users'] = [{'login': x['login'], 'url': x['html_url'], 'type': x.get('type')} for x in u.get('items', [])][:10]
            q2 = f'"{d0}" in:readme in:description'
            rec['queries'].append(q2)
            rp = gh('https://api.github.com/search/repositories?q=' + urllib.parse.quote(q2) + '&per_page=10')
            rec['repos'] = [{'full_name': x['full_name'], 'url': x['html_url'], 'desc': (x.get('description') or '')[:120], 'stars': x.get('stargazers_count'), 'pushed': (x.get('pushed_at') or '')[:10]} for x in rp.get('items', [])][:10]
        if name and len(name) >= 4 and not re.search(r'@|未具名|公司名', name):
            q3 = f'{name[:40]} type:org'
            rec['queries'].append(q3)
            o = gh('https://api.github.com/search/users?q=' + urllib.parse.quote(q3) + '&per_page=5')
            rec['orgs'] = [{'login': x['login'], 'url': x['html_url']} for x in o.get('items', [])][:5]
        res[c] = rec
        done += 1
        json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        time.sleep(6.5)  # 10 次/分钟（每户最多 3 次）
        print(c, len(rec['users']), len(rec['orgs']), len(rec['repos']), flush=True)
    if apply:
        sys.path.insert(0, os.path.dirname(__file__))
        import intel_store as IS
        n = 0
        for c, rec in res.items():
            rs = IS.load(c)
            if rs is None:
                continue
            toks = [t.lower() for t in re.findall(r'[A-Za-z]{7,}', str(rec.get('name') or '')) if t.lower() not in ('security', 'systems', 'technology', 'technologies', 'solutions', 'solution', 'networks', 'network', 'international', 'limited', 'company', 'services', 'service', 'sistemleri', 'teknoloji', 'elektronik', 'guvenlik', 'bilisim', 'communications', 'engineering', 'electronics', 'computer', 'wireless', 'industries')]
            root = (rec['domains'][0].split('.')[0].lower() if rec['domains'] else '')
            def plausible(txt):
                t = (txt or '').lower().replace('-', '').replace('_', '')
                return any(k in t for k in toks) or (len(root) >= 6 and root.replace('-', '') in t)
            # 重新生成：先清掉旧的 INTEL-GH-01 条目
            it = rs.get('intel')
            if it:
                it['items'] = [x for x in it['items'] if x.get('batch') != 'INTEL-GH-01']
            # 人工判噪（看过 URL 确认与本户无关）
            NOISE = {'SA-063': 'repos', 'SB-018': 'orgs', 'SA-070': 'orgs', 'SA-010': 'repos', 'SA-020': 'repos', 'SA-086': 'repos', 'SB-022': 'orgs',
                     'SB-103': 'orgs', 'SB-1113': 'both', 'SB-360': 'orgs', 'SB-375': 'orgs', 'SB-461': 'repos', 'SC-002': 'orgs', 'SC-371': 'orgs'}
            NOISE_LOGIN = {'liveyet', 'grundig41', 'Grundigt', 'grundigegryndere', 'grundig-akademie'}
            if NOISE.get(c) in ('repos', 'both'):
                rec = dict(rec, repos=[])
            if NOISE.get(c) in ('orgs', 'both'):
                rec = dict(rec, orgs=[])
            rec = dict(rec, orgs=[o for o in rec['orgs'] if o['login'] not in NOISE_LOGIN])
            hits = [(f"GitHub 用户（邮箱域 {rec['domains'][0] if rec['domains'] else ''}）：{u['login']}", u['url']) for u in rec['users']] + \
                   [(f"GitHub 组织（按公司名，疑似）：{o['login']}", o['url']) for o in rec['orgs'] if plausible(o['login'])] + \
                   [(f"GitHub 仓库提及域名：{r['full_name']} — {r['desc']}（★{r['stars']}，最近推送 {r['pushed']}）", r['url']) for r in rec['repos'] if plausible(r['full_name'] + ' ' + r['desc']) or (root and root in (r['desc'] or '').lower())]
            if hits:
                for q, u in hits[:8]:
                    n += IS.add(c, 'GitHub/技术足迹', q, u, DATE, '匿名 API 检索；组织名同名有误配可能，看 URL 再用', 'INTEL-GH-01', True, rs=rs, persist=False)
            else:
                n += IS.add(c, 'GitHub/技术足迹', '未得：' + '；'.join(rec['queries'])[:200] + ('（同名无关组织/仓库已剔除）' if (rec['orgs'] or rec['repos']) else ''), '', DATE, '', 'INTEL-GH-01', False, rs=rs, persist=False)
            IS.save(c, rs)
        print('applied items', n)
    print('scanned', len(res), 'of', len(A))


if __name__ == '__main__':
    main()
