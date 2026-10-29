#!/usr/bin/env python3
"""
客户动态监控 · 面监控清单生成器（T29-U19，2026-10-23）

Simon：「成单客户的动态都要监控起来……同样的 A 类客户也要监控，如果可能 B 类客户也要监控，系统性地都爬都监控起来，结果都要入库。」

本脚本**离线**运行（沙箱里就能跑，不联网）：读 data/saga_clients/entities.json（A/B 级）+ T27 的官网快照
data/saga_clients/site_snapshots/<code>.json（首页导航链接 / sitemap / 社媒链接），为每个 A/B 客户生成监控源：

  home      html     官网首页（快照里的 final_url；无快照则 https://<域名>/）
  sitemap   sitemap  站点地图（快照里有且条目>0；新增 URL = 新产品/新页面）
  news_N    html     导航里的 新闻/博客/案例/项目/活动 页（最多 2 个）
  youtube   rss / youtube_handle   YouTube 频道（/channel/UC… 直接出 RSS；@句柄 / c / user 由运行器解析一次 channelId）
  github    github   GitHub 组织/用户（API）
  telegram  html     公开频道预览页 https://t.me/s/<name>
  vk        html     VK 公开社区页
  社媒（LinkedIn / Facebook / Instagram / X / WhatsApp）抓不了（登录墙）→ 写进 manual，档案里列链接人工看。

输出 scripts/web_watch/targets_auto.json（watch.py 与手工精选的 targets.json 合并使用；精选里已有的 URL 不重复）。
重新生成是幂等的：同一输入同一输出；手工修正请改 targets.json（精选层）而不是本文件产物。

2026-10-29（T29-U120）起追加 **P 池层**（layer=P）：读 data/saga_clients/P池_巡检表_*.csv（Saga C / External XC / Planet 仓三库并池的正式 + 观察户），
每户监控「域名 / 平台链接」列前 2 个域名的首页（SC 码能在 entities.json / 快照里找到的沿用 A/B 同法），GitHub / YouTube / Telegram / VK 同上，
社媒链接进 manual。P 池层不与 A/B 层重码（P 池只收 C 级与外库户；随 A/B 主档的并档户不单列）。--no-pool 关闭。

用法：python3 scripts/web_watch/discover.py [--grades A,B] [--stats] [--no-pool]
"""
import argparse
import csv
import glob
import json
import os
import re
import sys
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ENT = os.path.join(ROOT, 'data', 'saga_clients', 'entities.json')
SNAPS = os.path.join(ROOT, 'data', 'saga_clients', 'site_snapshots')
CURATED = os.path.join(HERE, 'targets.json')
OUT = os.path.join(HERE, 'targets_auto.json')
POOL_GLOB = os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_*.csv')   # P 级 / 资产池 巡检表（T29-U117 起；取文件名最新一份）

NEWS_PAT = re.compile(r'(?i)(?<![a-z])(news|blog|press|media[- ]?(center|centre|room)|aktuell|neuigkeiten|nouvelles|actualit[eé]s?|noticias|novedades|novosti|'
                      r'новост|блог|пресс|haberler|haber|duyurular|案例|新闻|動態|动态|events?|projects?|referenzen|references?|realizacje|case[- ]?stud(y|ies)|'
                      r'portfolio|updates?|announcements?|whats?-?new|insights?|articles?|knowledge|資訊|资讯)(?![a-z])')
NEWS_BAD = re.compile(r'(?i)(privacy|cookie|terms|login|cart|checkout|account|wp-content|\.(pdf|jpg|png|zip)$|mailto:|tel:|#)')
SOCIAL_HOSTS = {
    'linkedin.com': 'LinkedIn', 'facebook.com': 'Facebook', 'instagram.com': 'Instagram', 'twitter.com': 'X/Twitter', 'x.com': 'X/Twitter',
    'wa.me': 'WhatsApp', 'api.whatsapp.com': 'WhatsApp', 'tiktok.com': 'TikTok', 'pinterest.com': 'Pinterest', 'threads.net': 'Threads',
}


def host_of(u):
    try:
        h = urlparse(u).netloc.lower()
    except Exception:  # noqa
        return ''
    return h[4:] if h.startswith('www.') else h


def norm_url(u):
    return (u or '').strip().rstrip('/').lower()


def youtube_source(u):
    m = re.search(r'youtube\.com/channel/(UC[\w-]{20,})', u)
    if m:
        return {'id': 'youtube', 'kind': 'rss', 'url': f'https://www.youtube.com/feeds/videos.xml?channel_id={m.group(1)}', 'note': f'YouTube 频道 {u}'}
    m = re.search(r'youtube\.com/(@[\w.-]+|c/[\w.-]+|user/[\w.-]+)', u)
    if m:
        return {'id': 'youtube', 'kind': 'youtube_handle', 'url': 'https://www.youtube.com/' + m.group(1), 'note': 'YouTube（运行器解析 channelId 后转 RSS）'}
    return None


def pool_subjects(ents_by_code):
    """巡检表 → 与 entities 同形的 subject 列表（layer=P）。SC 码优先用 entities 的 domains / platform_links；其余用表里的域名列。"""
    files = sorted(glob.glob(POOL_GLOB))
    if not files:
        return [], None
    path = files[-1]
    out = []
    for r in csv.DictReader(open(path, encoding='utf-8-sig')):
        code = (r.get('编号') or '').strip()
        if not code:
            continue
        toks = [t.strip() for t in (r.get('域名 / 平台链接') or '').split('|') if t.strip()]
        domains = [t.lower() for t in toks if re.fullmatch(r'(?i)[a-z0-9.-]+\.[a-z]{2,}', t)]
        links = [t for t in toks if t.startswith('http')]
        e = ents_by_code.get(code) or {}
        if e.get('domains'):
            domains = [d for d in e['domains'] if d] + [d for d in domains if d not in (e.get('domains') or [])]
        origin = 'Saga' if code.startswith('S') else ('External' if code.startswith('X') else 'Planet')
        out.append({'code': code, 'name': r.get('公司') or e.get('name') or code, 'grade': e.get('grade') or 'C', 'country': r.get('国家') or e.get('country') or '',
                    'domains': domains, 'platform_links': list(e.get('platform_links') or []) + links, 'layer': 'P',
                    'pool': {'档位': r.get('档位') or '', '入池': r.get('入池') or '', '来源': origin, '区域组': r.get('区域组') or '', '标签': r.get('标签') or '',
                             '下次巡检': r.get('下次巡检') or ''}})
    return out, os.path.relpath(path, ROOT)


def build(grades, pool=True):
    ents = json.load(open(ENT, encoding='utf-8'))
    subjects = [e for e in ents if e.get('grade') in grades]
    pool_file = None
    if pool:
        ps, pool_file = pool_subjects({e['code']: e for e in ents})
        have = {e['code']: e for e in subjects}
        for x in ps:
            if x['code'] in have:
                have[x['code']]['pool'] = x['pool']      # A / B 并池户（AB-01 起）：层仍是 A / B，只挂池位信息
            else:
                subjects.append(x)
    curated = json.load(open(CURATED, encoding='utf-8')) if os.path.exists(CURATED) else {'customers': []}
    cur_by = {c['code']: c for c in curated.get('customers', [])}
    cur_urls = {norm_url(s.get('url')) for c in curated.get('customers', []) for s in c['sources'] if s.get('url')}
    cur_logins = {(s.get('login') or '').lower() for c in curated.get('customers', []) for s in c['sources'] if s.get('login')}
    customers, stats = [], {'customers': 0, 'no_domain': 0, 'sources': 0, 'kinds': {}, 'social_manual': 0, 'snapshot_missing': 0, 'site_dead': 0, 'pool_customers': 0, 'pool_sources': 0}
    for e in subjects:
        code = e['code']
        is_pool = e.get('layer') == 'P'
        if is_pool:
            stats['pool_customers'] += 1
        stats['customers'] += 1
        domains = [d for d in (e.get('domains') or []) if d]
        snap = None
        sp = os.path.join(SNAPS, f'{code}.json')
        if os.path.exists(sp):
            try:
                snap = json.load(open(sp, encoding='utf-8'))
            except Exception:  # noqa
                snap = None
        else:
            stats['snapshot_missing'] += 1
        home = (snap or {}).get('home') or {}
        home_url = home.get('final_url') or home.get('url') or (f'https://{domains[0]}/' if domains else '')
        if not home_url:
            stats['no_domain'] += 1
            continue
        site_status = (snap or {}).get('status') or 'unknown'
        if site_status in ('unreachable', 'parked_or_empty'):
            stats['site_dead'] += 1
        sources, manual, seen = [], [], set()

        def add(src):
            u = norm_url(src.get('url'))
            lg = (src.get('login') or '').lower()
            if (u and (u in seen or u in cur_urls)) or (lg and (lg in seen or lg in cur_logins)):
                return
            seen.add(u or lg)
            sources.append(src)
            stats['sources'] += 1
            stats['kinds'][src['kind']] = stats['kinds'].get(src['kind'], 0) + 1

        add({'id': 'home', 'kind': 'html', 'url': home_url, 'note': f'官网首页（T27 快照状态 {site_status}）' if snap else '官网首页'})
        hh = host_of(home_url)
        if is_pool:
            # P 池：多域名户（同一法人两个店 / 两国站）再看第 2 个域名首页
            for d in domains[1:2]:
                if host_of(f'https://{d}/') != hh:
                    add({'id': 'home_2', 'kind': 'html', 'url': f'https://{d}/', 'note': '第二域名首页（P 池巡检表）'})
        sm = (snap or {}).get('sitemap') or {}
        if sm.get('url') and (sm.get('count') or 0) > 0:
            add({'id': 'sitemap', 'kind': 'sitemap', 'url': sm['url'], 'note': f'站点地图（2026-10-21 时 {sm["count"]} 条）'})
        # 新闻/博客/案例页：导航链接里按关键词挑，最多 2 个，优先同域
        cands = []
        for t, u in (home.get('links') or []):
            if not u or NEWS_BAD.search(u):
                continue
            if host_of(u) != hh:
                continue
            path = urlparse(u).path or '/'
            segs = [x for x in path.split('/') if x]
            if len(segs) > 3 or (segs and len(segs[-1]) > 40) or len(t or '') > 40:
                continue          # 单篇文章的深链接 / 长 slug 不要，要的是栏目索引页
            if NEWS_PAT.search(t or '') or NEWS_PAT.search(path):
                score = 2 if NEWS_PAT.search(t or '') else 1
                if re.search(r'(?i)news|blog|новост|haber|新闻|nouvelles|noticias|aktuell', (t or '') + path):
                    score += 2
                score -= max(0, len(segs) - 1)      # 越浅越像栏目页
                cands.append((score, t, u))
        cands.sort(key=lambda x: -x[0])
        picked = []
        for score, t, u in cands:
            if norm_url(u) == norm_url(home_url) or any(norm_url(u) == norm_url(p) for p in picked):
                continue
            picked.append(u)
            add({'id': f'news_{len(picked)}', 'kind': 'html', 'url': u, 'note': f'导航「{(t or "")[:40]}」'})
            if len(picked) >= 2:
                break
        # 社媒 / 平台
        socials = list(home.get('social') or []) + list(e.get('platform_links') or [])
        for s in socials:
            if not s or not s.startswith('http'):
                continue
            h = host_of(s)
            if 'youtube.com' in h or h == 'youtu.be':
                ys = youtube_source(s)
                if ys and not any(x['id'] == 'youtube' for x in sources):
                    add(ys)
                continue
            if h == 'github.com':
                m = re.match(r'https?://(?:www\.)?github\.com/([\w.-]+)/?$', s)
                if m and m.group(1).lower() not in ('features', 'about', 'pricing'):
                    add({'id': 'github', 'kind': 'github', 'login': m.group(1), 'note': f'GitHub {s}'})
                continue
            if h in ('t.me', 'telegram.me'):
                m = re.match(r'https?://(?:www\.)?(?:t|telegram)\.me/(?:s/)?([\w]+)', s)
                if m and m.group(1).lower() not in ('share', 'joinchat'):
                    add({'id': 'telegram', 'kind': 'html', 'url': f'https://t.me/s/{m.group(1)}', 'note': 'Telegram 公开频道预览页'})
                continue
            if h == 'vk.com':
                m = re.match(r'https?://(?:www\.)?vk\.com/([\w.]+)/?$', s)
                if m and m.group(1).lower() not in ('share.php', 'login'):
                    add({'id': 'vk', 'kind': 'html', 'url': f'https://vk.com/{m.group(1)}', 'note': 'VK 公开社区页'})
                continue
            for sh, label in SOCIAL_HOSTS.items():
                if h == sh or h.endswith('.' + sh):
                    if not any(m0['url'] == s for m0 in manual):
                        manual.append({'label': label, 'url': s, 'note': '登录墙，人工看'})
                        stats['social_manual'] += 1
                    break
        c = {'code': code, 'name': e.get('name') or code, 'grade': e.get('grade'), 'country': e.get('country') or '', 'layer': e.get('layer') or e.get('grade'),
             'site_status_2026_10_21': site_status, 'sources': sources, 'manual': manual}
        if is_pool:
            c['pool'] = e['pool']
            stats['pool_sources'] += len(sources)
        elif e.get('pool'):
            c['pool'] = e['pool']
            stats['pool_ab'] = stats.get('pool_ab', 0) + 1
        if code in cur_by:
            c['note'] = '精选层（targets.json）已有本客户；此处只补精选里没有的源'
        customers.append(c)
    return {'meta': {'generated_by': 'scripts/web_watch/discover.py', 'inputs': ['data/saga_clients/entities.json', 'data/saga_clients/site_snapshots/ (T27 2026-10-21)'] + ([pool_file + ' (P 池层)'] if pool_file else []),
                     'grades': sorted(grades), 'layers': sorted({c['layer'] for c in customers}), 'stats': stats,
                     'note': '离线生成（幂等）。精选源请改 targets.json；本文件由 discover.py 重新生成时会被覆盖。'},
            'customers': customers}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--grades', default='A,B')
    ap.add_argument('--stats', action='store_true')
    ap.add_argument('--out', default=OUT)
    ap.add_argument('--no-pool', action='store_true', help='不生成 P 池层')
    args = ap.parse_args(argv)
    grades = {g.strip().upper() for g in args.grades.split(',') if g.strip()}
    cfg = build(grades, pool=not args.no_pool)
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=1)
    st = cfg['meta']['stats']
    print(f"targets_auto: customers={len(cfg['customers'])} sources={st['sources']} kinds={st['kinds']} social_manual={st['social_manual']} "
          f"snapshot_missing={st['snapshot_missing']} site_dead={st['site_dead']} no_domain={st['no_domain']} pool={st['pool_customers']}/{st['pool_sources']} → {args.out}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
