#!/usr/bin/env python3
"""T27 · 客户官网快照（供 A/B 级加厚挖掘）。

Arena 沙箱不能访问客户网站，本脚本由 GitHub Actions 运行器执行：
  对 entities.json 中 A/B 级（可配）且有域名的客户，抓首页 + sitemap 概况 + 最多 N 个
  产品/关于/联系子页，抽取紧凑文本摘要（标题 / 描述 / 标题层级 / 导航链接 / 邮箱 / 电话 /
  型号样式 token / 关键词命中 / 社媒 / 正文片段），写入
      data/saga_clients/site_snapshots/<编号>.json   （每站 ≤ ~14 KB）
      data/saga_clients/site_snapshots/_report.json  （汇总：成功 / DNS / 超时 / HTTP 错误）
      data/saga_clients/site_snapshots/_index.csv
  每处理 COMMIT_EVERY 个站点提交一次回分支（GIT_COMMIT=1 时），避免中途失败全丢。

用法：python scripts/saga_clients/site_snapshot.py
环境变量：GRADES=A,B  MAX_SUB=6  FORCE=0  WORKERS=12  LIMIT=0  COMMIT_EVERY=150  GIT_COMMIT=0  GIT_REF=分支名
"""
import csv
import json
import os
import re
import subprocess
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.parse import urljoin, urlparse

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    from bs4 import BeautifulSoup  # noqa
    HAVE_BS4 = True
except Exception:  # pragma: no cover
    HAVE_BS4 = False

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
OUT = os.path.join(DATA, 'site_snapshots')
ENTITIES = os.path.join(DATA, 'entities.json')

GRADES = [g.strip().upper() for g in os.environ.get('GRADES', 'A,B').split(',') if g.strip()]
MAX_SUB = int(os.environ.get('MAX_SUB', '6'))
FORCE = os.environ.get('FORCE', '0') == '1'
WORKERS = int(os.environ.get('WORKERS', '12'))
LIMIT = int(os.environ.get('LIMIT', '0'))
COMMIT_EVERY = int(os.environ.get('COMMIT_EVERY', '150'))
GIT_COMMIT = os.environ.get('GIT_COMMIT', '0') == '1'
GIT_REF = os.environ.get('GIT_REF', '')
FRESH_DAYS = int(os.environ.get('FRESH_DAYS', '30'))
TIMEOUT = (10, 20)
MAX_BODY = 1_500_000
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/124.0.0.0 Safari/537.36')
HEADERS = {'User-Agent': UA, 'Accept': 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.8,de;q=0.5,tr;q=0.5,pl;q=0.5,ru;q=0.5'}

EMAIL_RE = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
PHONE_RE = re.compile(r'(?:\+|00)\d[\d\s().-]{7,}\d')
MODEL_RE = re.compile(r'\b(?=[A-Z0-9-]{5,24}\b)(?=[A-Z0-9-]*\d)(?=[A-Z0-9-]*[A-Z]{2})[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b|'
                      r'\b(?=[A-Z0-9]{5,16}\b)(?=[A-Z0-9]*\d)[A-Z]{2,}[0-9]{2,}[A-Z0-9]*\b')
KEYWORDS = ['switch', 'poe', 'industrial', 'din', 'sfp', 'media converter', 'fiber', 'fibre', 'ethernet',
            'gigabit', '10g', '2.5g', 'cctv', 'camera', 'nvr', 'surveillance', 'access control', 'wifi',
            'wireless', 'router', 'oem', 'odm', 'brand', 'distributor', 'wholesale', 'integrator',
            'installer', 'solution', 'automation', 'scada', 'plc', 'telecom', 'isp', 'ftth', 'olt', 'onu',
            'cable', 'rack', 'ups', 'datacenter', 'data center', 'planet', 'mikrotik', 'ubiquiti',
            'tp-link', 'cisco', 'moxa', 'hikvision', 'dahua', 'uniview', 'axis']
SUB_PRIORITY = [
    ('product', 5), ('produkt', 5), ('produit', 5), ('prodott', 5), ('producto', 5), ('ürün', 5), ('urun', 5),
    ('продук', 5), ('katalog', 4), ('catalog', 4), ('shop', 3), ('sklep', 3), ('store', 3),
    ('switch', 6), ('poe', 6), ('industrial', 6), ('endüstriyel', 6), ('przemysł', 6), ('network', 4),
    ('netzwerk', 4), ('sieci', 4), ('ağ', 2), ('brand', 4), ('marke', 4), ('marka', 4), ('partner', 3),
    ('hersteller', 3), ('manufactur', 3), ('about', 4), ('über', 4), ('hakkımızda', 4), ('hakkimizda', 4),
    ('o-nas', 4), ('o nas', 4), ('о-нас', 4), ('company', 3), ('firma', 3), ('contact', 4), ('kontakt', 4),
    ('iletişim', 4), ('iletisim', 4), ('контакт', 4), ('solution', 2), ('service', 1), ('cctv', 4),
    ('camera', 3), ('kamera', 3), ('fiber', 3), ('ethernet', 3),
]
SKIP_HREF = ('javascript:', 'mailto:', 'tel:', '#', 'whatsapp', '.pdf', '.jpg', '.png', '.zip', '.mp4',
             'login', 'cart', 'account', 'wp-json', 'feed', '/tag/', 'privacy', 'cookie', 'terms', 'agb',
             'impressum', 'datenschutz')
SOCIAL = ('linkedin.com', 'facebook.com', 'instagram.com', 'youtube.com', 'twitter.com', 'x.com', 't.me',
          'wa.me', 'vk.com')

_print_lock = threading.Lock()


def log(*a):
    with _print_lock:
        print(*a, flush=True)


def now_iso():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def clean(s, n=None):
    s = re.sub(r'\s+', ' ', (s or '')).strip()
    return s[:n] if n else s


def get(url, sess):
    r = sess.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True, verify=False, stream=True)
    ctype = (r.headers.get('content-type') or '').lower()
    if 'html' not in ctype and 'xml' not in ctype and 'text' not in ctype:
        r.close()
        return r.status_code, r.url, '', ctype
    buf = b''
    for chunk in r.iter_content(65536):
        buf += chunk
        if len(buf) > MAX_BODY:
            break
    r.close()
    enc = r.encoding or 'utf-8'
    try:
        txt = buf.decode(enc, errors='replace')
    except Exception:
        txt = buf.decode('utf-8', errors='replace')
    return r.status_code, r.url, txt, ctype


def parse_html(html, base):
    """返回紧凑结构：title / desc / lang / h / links / text / emails / phones / models / social / kw."""
    d = {'title': '', 'desc': '', 'lang': '', 'h': [], 'links': [], 'text': '', 'emails': [], 'phones': [],
         'models': [], 'social': [], 'kw': {}}
    if not html:
        return d
    if HAVE_BS4:
        try:
            soup = BeautifulSoup(html, 'lxml')
        except Exception:
            soup = BeautifulSoup(html, 'html.parser')
        for t in soup(['script', 'style', 'noscript', 'svg', 'iframe']):
            t.decompose()
        d['title'] = clean(soup.title.get_text() if soup.title else '', 200)
        m = soup.find('meta', attrs={'name': re.compile('^description$', re.I)}) or \
            soup.find('meta', attrs={'property': 'og:description'})
        d['desc'] = clean(m.get('content') if m else '', 400)
        d['lang'] = clean((soup.html.get('lang') if soup.html else '') or '', 10)
        for tag in soup.find_all(['h1', 'h2', 'h3']):
            t = clean(tag.get_text(' '), 120)
            if t and t not in d['h']:
                d['h'].append(t)
            if len(d['h']) >= 30:
                break
        seen = set()
        for a in soup.find_all('a', href=True):
            href = a['href'].strip()
            if any(k in href.lower() for k in SKIP_HREF[:4]):
                continue
            absu = urljoin(base, href)
            pu = urlparse(absu)
            if pu.scheme not in ('http', 'https'):
                continue
            txt = clean(a.get_text(' '), 80)
            if any(s in pu.netloc for s in SOCIAL):
                if absu not in d['social'] and len(d['social']) < 10:
                    d['social'].append(absu)
                continue
            if pu.netloc.replace('www.', '') != urlparse(base).netloc.replace('www.', ''):
                continue
            key = (pu.path.rstrip('/'), pu.query)
            if key in seen:
                continue
            seen.add(key)
            d['links'].append([txt, absu])
            if len(d['links']) >= 160:
                break
        body = soup.body or soup
        text = clean(body.get_text(' '))
    else:  # pragma: no cover
        text = clean(re.sub(r'<[^>]+>', ' ', html))
        d['title'] = clean((re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S) or [None, ''])[1], 200)
    d['text'] = text[:2500]
    low = text.lower()
    d['emails'] = sorted(set(e.lower() for e in EMAIL_RE.findall(text + ' ' + html)
                             if not e.lower().endswith(('.png', '.jpg', '.gif', '.svg', '.webp'))))[:12]
    d['phones'] = sorted(set(clean(p) for p in PHONE_RE.findall(text)))[:8]
    models = {}
    for mm in MODEL_RE.findall(text):
        if mm.lower() in ('covid-19', 'iso-9001', 'utf-8', 'en-us', 'rohs-2'):
            continue
        models[mm] = models.get(mm, 0) + 1
    d['models'] = sorted(models.items(), key=lambda x: -x[1])[:60]
    d['kw'] = {k: low.count(k) for k in KEYWORDS if k in low}
    return d


def pick_subpages(links, home_url):
    scored = []
    for txt, u in links:
        if any(k in u.lower() for k in SKIP_HREF):
            continue
        hay = (txt + ' ' + urlparse(u).path).lower()
        sc = sum(w for k, w in SUB_PRIORITY if k in hay)
        if u.rstrip('/') == home_url.rstrip('/'):
            continue
        if sc > 0:
            scored.append((sc, len(u), u, txt))
    scored.sort(key=lambda x: (-x[0], x[1]))
    out, seen = [], set()
    for sc, _, u, txt in scored:
        p = urlparse(u).path.rstrip('/')
        if p in seen:
            continue
        seen.add(p)
        out.append((u, txt, sc))
        if len(out) >= MAX_SUB:
            break
    return out


def sitemap_probe(home_url, sess):
    info = {'url': '', 'count': 0, 'product_like': []}
    base = f"{urlparse(home_url).scheme}://{urlparse(home_url).netloc}"
    for cand in ('/sitemap.xml', '/sitemap_index.xml', '/sitemap-index.xml', '/wp-sitemap.xml'):
        try:
            st, fu, body, ct = get(base + cand, sess)
        except Exception:
            continue
        if st != 200 or '<loc>' not in body:
            continue
        locs = re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', body)
        info['url'] = fu
        # 若为索引，再取前 3 个子 sitemap
        subs = [l for l in locs if l.lower().endswith('.xml')][:3]
        urls = [l for l in locs if not l.lower().endswith('.xml')]
        for s in subs:
            try:
                st2, _, b2, _ = get(s, sess)
                if st2 == 200:
                    urls += re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', b2)
            except Exception:
                pass
            if len(urls) > 5000:
                break
        info['count'] = len(urls)
        pl = [u for u in urls if re.search(r'switch|poe|industrial|produ|prod|urun|ürün|katalog|catalog|shop|sklep',
                                           u, re.I)]
        info['product_like'] = pl[:40]
        break
    return info


def snapshot_one(ent):
    code = ent['code']
    doms = [d for d in (ent.get('domains') or []) if d and '.' in d]
    rec = {'code': code, 'name': ent.get('name'), 'country': ent.get('country'), 'grade': ent.get('grade'),
           'fetched_at': now_iso(), 'domains': doms, 'status': 'no_domain', 'home': None, 'sitemap': None,
           'subpages': [], 'errors': []}
    if not doms:
        return rec
    sess = requests.Session()
    home = None
    for dom in doms[:2]:
        for scheme in ('https://', 'http://'):
            for host in (dom, 'www.' + dom) if not dom.startswith('www.') else (dom,):
                url = scheme + host + '/'
                try:
                    st, fu, body, ct = get(url, sess)
                except requests.exceptions.ConnectionError as e:
                    msg = str(e)
                    rec['errors'].append(f'{url} conn: {msg[:120]}')
                    continue
                except requests.exceptions.Timeout:
                    rec['errors'].append(f'{url} timeout')
                    continue
                except Exception as e:
                    rec['errors'].append(f'{url} {type(e).__name__}: {str(e)[:100]}')
                    continue
                if st >= 400 or not body:
                    rec['errors'].append(f'{url} http {st} ct={ct[:30]}')
                    continue
                home = (url, st, fu, body)
                break
            if home:
                break
        if home:
            break
    if not home:
        errs = ' | '.join(rec['errors']).lower()
        if 'name or service not known' in errs or 'nodename' in errs or 'getaddrinfo' in errs or 'no address' in errs:
            rec['status'] = 'dns_fail'
        elif 'timeout' in errs:
            rec['status'] = 'timeout'
        elif 'http 4' in errs or 'http 5' in errs:
            rec['status'] = 'http_error'
        else:
            rec['status'] = 'unreachable'
        return rec
    url, st, fu, body = home
    hp = parse_html(body, fu)
    hp.update({'url': url, 'final_url': fu, 'http': st, 'bytes': len(body)})
    rec['home'] = hp
    rec['status'] = 'ok'
    # 停放页 / 空站检测
    low = (hp['title'] + ' ' + hp['desc'] + ' ' + hp['text'][:800]).lower()
    if any(k in low for k in ('domain is for sale', 'buy this domain', 'parked', 'sedo', 'godaddy', 'hugedomains',
                              'domain expired', 'this domain', 'coming soon', 'under construction')) and len(hp['links']) < 8:
        rec['status'] = 'parked_or_empty'
    try:
        rec['sitemap'] = sitemap_probe(fu, sess)
    except Exception as e:
        rec['errors'].append(f'sitemap {type(e).__name__}')
    for su, stxt, sc in pick_subpages(hp['links'], fu):
        time.sleep(0.4)
        try:
            st2, fu2, body2, ct2 = get(su, sess)
        except Exception as e:
            rec['errors'].append(f'{su} {type(e).__name__}')
            continue
        if st2 >= 400 or not body2:
            rec['errors'].append(f'{su} http {st2}')
            continue
        sp = parse_html(body2, fu2)
        sp['links'] = [l for l in sp['links'] if any(k in (l[0] + l[1]).lower()
                                                   for k in ('switch', 'poe', 'industrial', 'product', 'produkt',
                                                             'ürün', 'urun', 'katalog', 'catalog'))][:40]
        sp['text'] = sp['text'][:1800]
        sp.update({'url': su, 'final_url': fu2, 'http': st2, 'nav_text': stxt, 'score': sc})
        rec['subpages'].append(sp)
    rec['home']['links'] = rec['home']['links'][:120]
    return rec


def git_commit_push(msg):
    if not GIT_COMMIT:
        return
    try:
        subprocess.run(['git', 'add', 'data/saga_clients/site_snapshots'], cwd=ROOT, check=True)
        r = subprocess.run(['git', 'commit', '-q', '-m', msg], cwd=ROOT)
        if r.returncode != 0:
            log('nothing to commit')
            return
        ref = GIT_REF or subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=ROOT,
                                        capture_output=True, text=True).stdout.strip()
        for attempt in range(5):
            subprocess.run(['git', 'pull', '-q', '--rebase', '-X', 'theirs', 'origin', ref], cwd=ROOT)
            p = subprocess.run(['git', 'push', '-q', 'origin', f'HEAD:{ref}'], cwd=ROOT)
            if p.returncode == 0:
                log(f'pushed: {msg}')
                return
            time.sleep(5 + attempt * 5)
        log('push failed after retries')
    except Exception as e:  # pragma: no cover
        log('git error', e)


def main():
    os.makedirs(OUT, exist_ok=True)
    ents = json.load(open(ENTITIES, encoding='utf-8'))
    todo = []
    cutoff = time.time() - FRESH_DAYS * 86400
    for e in sorted(ents, key=lambda x: ('ABC'.index(x['grade']), x['code'])):
        if e['grade'] not in GRADES or not e.get('domains'):
            continue
        fp = os.path.join(OUT, f"{e['code']}.json")
        if not FORCE and os.path.exists(fp) and os.path.getmtime(fp) > cutoff:
            try:
                old = json.load(open(fp, encoding='utf-8'))
                if old.get('status') == 'ok':
                    continue
            except Exception:
                pass
        todo.append(e)
    if LIMIT:
        todo = todo[:LIMIT]
    log(f'sites to snapshot: {len(todo)} (grades={GRADES}, max_sub={MAX_SUB}, workers={WORKERS})')
    done = 0
    stats = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(snapshot_one, e): e for e in todo}
        for fut in as_completed(futs):
            e = futs[fut]
            try:
                rec = fut.result()
            except Exception as ex_:
                rec = {'code': e['code'], 'name': e.get('name'), 'grade': e.get('grade'), 'country': e.get('country'),
                       'fetched_at': now_iso(), 'domains': e.get('domains'), 'status': 'crash',
                       'errors': [f'{type(ex_).__name__}: {str(ex_)[:200]}'], 'home': None, 'subpages': []}
            with open(os.path.join(OUT, f"{rec['code']}.json"), 'w', encoding='utf-8') as f:
                json.dump(rec, f, ensure_ascii=False, separators=(',', ':'))
            stats[rec['status']] = stats.get(rec['status'], 0) + 1
            done += 1
            if done % 25 == 0:
                log(f'{done}/{len(todo)} {stats} {int(time.time() - t0)}s')
            if COMMIT_EVERY and done % COMMIT_EVERY == 0:
                write_report()
                git_commit_push(f'T27: 客户官网快照 +{COMMIT_EVERY}（累计 {done}/{len(todo)}，{now_iso()}）')
    write_report()
    git_commit_push(f'T27: 客户官网快照完成本轮（{done} 站，{now_iso()}）')
    log('done', stats)


def write_report():
    rows, stats, by_grade = [], {}, {}
    for fn in sorted(os.listdir(OUT)):
        if not fn.endswith('.json') or fn.startswith('_'):
            continue
        try:
            r = json.load(open(os.path.join(OUT, fn), encoding='utf-8'))
        except Exception:
            continue
        st = r.get('status')
        stats[st] = stats.get(st, 0) + 1
        by_grade.setdefault(r.get('grade'), {}).setdefault(st, 0)
        by_grade[r.get('grade')][st] += 1
        h = r.get('home') or {}
        rows.append([r['code'], r.get('grade'), r.get('name'), r.get('country'), ','.join(r.get('domains') or []),
                     st, h.get('final_url', ''), h.get('title', ''), len(r.get('subpages') or []),
                     (r.get('sitemap') or {}).get('count', 0), ';'.join(h.get('emails') or [])[:200],
                     r.get('fetched_at')])
    with open(os.path.join(OUT, '_index.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '等级', '公司', '国家', '域名', '状态', '最终URL', '标题', '子页数', 'sitemap条数',
                    '页面邮箱', '抓取时间'])
        w.writerows(rows)
    with open(os.path.join(OUT, '_report.json'), 'w', encoding='utf-8') as f:
        json.dump({'generated_at': now_iso(), 'total': len(rows), 'by_status': stats, 'by_grade': by_grade},
                  f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
