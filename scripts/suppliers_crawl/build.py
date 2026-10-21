#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HRUI / Hohunet 官网归档 → 整理层（T25 / PR-02-18）。

输入（原始层，由 Actions 上的 crawl.py v3.0 写入，不手改）：
  data/<site>_site_raw/pages_manifest.jsonl / html/*.html / downloads_manifest.jsonl / datasheet_text/*.txt / images_manifest.jsonl / summary.json
输出（整理层，全部由本脚本生成，不手改）：
  data/<site>_site/pages.json                 每个 HTML 页一条：url / 类型 / 标题 / h1 / 面包屑 / 描述 / 标题层级 / 表格 / 正文摘录 / PDF / 图片数
  data/<site>_site/products.json              产品页结构化（型号、规格表逐行、图片、下载）
  data/<site>_官网页面索引.csv                 页面索引（按类型 / URL）
  data/<site>_官网型号索引.csv                 产品索引（型号 / 标题 / 类目 / 端口要点 / URL）
  docs/suppliers/<Name>/01-官网页面索引.md     按类型分组的页面清单（带抓取日期）
  docs/suppliers/<Name>/02-官网产品清单.md     产品清单（英文原文照录要点 + 规格要点）
  docs/suppliers/<Name>/products/<slug>.md     每产品一页（原文照录：标题 / 描述 / 规格表 / 图片 / 下载）

用法：python3 scripts/suppliers_crawl/build.py [hrui|hohunet]   （缺省两站都跑；需要 beautifulsoup4 + lxml）
规则：只整理不改原文；英文原文照录，中文只出现在栏目名；所有事实带官网 URL + 抓取日期；未抓到的如实写「未抓到」。
"""
import csv
import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from urllib.parse import urljoin, urlparse, unquote

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover
    sys.exit("pip install --break-system-packages beautifulsoup4 lxml")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SITES = {
    'hrui': dict(name='HRUI', host='www.hruitech.com', raw='data/hrui_site_raw', out='data/hrui_site',
                 csv_pages='data/hrui_官网页面索引.csv', csv_products='data/hrui_官网型号索引.csv',
                 docs='docs/suppliers/HRUI'),
    'hohunet': dict(name='Hohunet', host='hohunet.com', raw='data/hohunet_site_raw', out='data/hohunet_site',
                    csv_pages='data/hohunet_官网页面索引.csv', csv_products='data/hohunet_官网型号索引.csv',
                    docs='docs/suppliers/Hohunet'),
}

JUNK_TAGS = ('script', 'style', 'noscript', 'svg', 'iframe', 'form', 'nav', 'footer', 'header')


def rp(p):
    return os.path.join(ROOT, p)


def read_jsonl(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return rows


def clean(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()


def classify(site, url):
    p = urlparse(url).path.lower()
    if site == 'hohunet':
        if p.startswith('/product/') and len(p) > 9:
            return 'product'
        if p.startswith('/product-category/') or p.startswith('/product-tag/'):
            return 'category'
        if re.match(r'^/\d{4}/\d{2}/', p) or p.startswith('/blog') or p.startswith('/news') or p.startswith('/category/') or p.startswith('/tag/') or p.startswith('/author/'):
            return 'post'
        if p.startswith('/service'):
            return 'service'
        if p in ('', '/'):
            return 'home'
        return 'page'
    # hrui
    if p in ('', '/', '/index.html'):
        return 'home'
    if re.search(r'/(poe-switch|managed-switch|industrial-poe-switch|industrial-ethernet-switch|optical-fiber-converter|poe-accessory|wireless-bridge|web-managed|l2-managed|l3-managed|poe-injector|poe-extender|poe-splitter|hi-poe|products?)(/|\.html|$)', p):
        # 类目或筛选页：路径较短且无数字编号
        if re.search(r'[-_/]\d{2,}', p) or p.count('/') >= 3:
            return 'product'
        return 'category'
    if re.search(r'/(product-news|exhibition-news|company-news|industry-news|news|technology-sharing)', p):
        return 'post'
    if re.search(r'/(about|company-profile|founding-story|development-history|qualifications|product-certification|odmoem|oem|channel|after-sales|service|web-manual|data-download|firmware-download|digital-management|solution|contact)', p):
        return 'page'
    if p.endswith('.html') and re.search(r'\d', p):
        return 'product'
    return 'page'


def extract_tables(soup):
    tables = []
    for t in soup.find_all('table'):
        rows = []
        for tr in t.find_all('tr'):
            cells = [clean(c.get_text(' ')) for c in tr.find_all(['th', 'td'])]
            cells = [c for c in cells]
            if any(cells):
                rows.append(cells)
        if rows:
            tables.append(rows)
    return tables


def main_text(soup):
    body = soup.find('main') or soup.find('article') or soup.find(id=re.compile('content|main', re.I)) or soup.body or soup
    txt = body.get_text('\n')
    lines = [clean(l) for l in txt.split('\n')]
    lines = [l for l in lines if l and len(l) > 1]
    # 去重连续重复行
    out, prev = [], None
    for l in lines:
        if l != prev:
            out.append(l)
        prev = l
    return out


def parse_page(site, cfg, rec, html_path):
    with open(html_path, encoding='utf-8', errors='ignore') as f:
        raw = f.read()
    soup = BeautifulSoup(raw, 'lxml')
    title = clean(soup.title.get_text()) if soup.title else ''
    desc = ''
    m = soup.find('meta', attrs={'name': 'description'})
    if m and m.get('content'):
        desc = clean(m['content'])
    canonical = ''
    l = soup.find('link', rel='canonical')
    if l and l.get('href'):
        canonical = l['href']
    h1 = [clean(h.get_text(' ')) for h in soup.find_all('h1')]
    crumbs = []
    bc = soup.find(class_=re.compile('breadcrumb', re.I)) or soup.find(id=re.compile('breadcrumb', re.I))
    if bc:
        crumbs = [clean(a.get_text()) for a in bc.find_all(['a', 'span', 'li']) if clean(a.get_text())]
        crumbs = list(OrderedDict.fromkeys(crumbs))
    pdfs = []
    for a in soup.find_all('a', href=True):
        href = urljoin(rec.get('final_url') or rec['url'], a['href'])
        if re.search(r'\.(pdf|docx?|xlsx?|zip|rar|bin|img)(\?|$)', href, re.I):
            pdfs.append(dict(url=href, text=clean(a.get_text())))
    imgs = []
    for im in soup.find_all('img'):
        src = im.get('data-src') or im.get('data-lazy-src') or im.get('data-original') or im.get('src') or ''
        if src and not src.startswith('data:'):
            imgs.append(urljoin(rec.get('final_url') or rec['url'], src))
    imgs = list(OrderedDict.fromkeys(imgs))
    for tag in soup.find_all(JUNK_TAGS):
        tag.decompose()
    heads = [(h.name, clean(h.get_text(' '))) for h in soup.find_all(['h1', 'h2', 'h3']) if clean(h.get_text(' '))]
    tables = extract_tables(soup)
    lines = main_text(soup)
    text = '\n'.join(lines)
    return OrderedDict([
        ('url', rec['url']), ('final_url', rec.get('final_url')), ('fetched_at', rec.get('fetched_at')),
        ('status', rec.get('status')), ('file', rec.get('file')), ('type', classify(site, rec.get('final_url') or rec['url'])),
        ('title', title), ('h1', h1), ('description', desc), ('canonical', canonical), ('breadcrumb', crumbs),
        ('headings', heads[:80]), ('tables', tables[:40]), ('downloads', pdfs[:60]), ('images', imgs[:120]),
        ('text_lines', len(lines)), ('text_excerpt', text[:6000]),
    ])


PORT_RE = re.compile(r'(\d+)\s*[x×\*]\s*(10/100/1000M?|10/100M?|100M|1000M|1G|2\.5G|5G|10G|25G|40G|100G|400G|800G|Gigabit|Fast Ethernet)[^,;|\n]{0,40}', re.I)


def port_summary(text):
    hits = PORT_RE.findall(text or '')
    seen, out = set(), []
    for n, speed in hits:
        k = (n, speed.upper())
        if k in seen:
            continue
        seen.add(k)
        out.append(f'{n}×{speed}')
        if len(out) >= 6:
            break
    return ' + '.join(out)


MODEL_RE = {
    'hohunet': re.compile(r'\b(S\d{4}[A-Z]*(?:-[0-9A-Z]+)*(?:-(?:EI|SI|PLUS))?)\b'),
    'hrui': re.compile(r'\b(HR\d{3,}[A-Z0-9\-]*|[A-Z]{2,4}-?\d{2,}[A-Z0-9\-]*)\b'),
}


def product_record(site, page):
    text = page['title'] + '\n' + '\n'.join(page['h1']) + '\n' + page['text_excerpt']
    models = []
    for m in MODEL_RE.get(site, MODEL_RE['hrui']).findall(text):
        if m not in models:
            models.append(m)
    model = models[0] if models else ''
    spec_rows = []
    for t in page['tables']:
        for row in t:
            if 1 <= len(row) <= 4 and len(' '.join(row)) < 400:
                spec_rows.append(row)
    cat = ''
    if page['breadcrumb']:
        bc = [c for c in page['breadcrumb'] if c.lower() not in ('home', 'products', 'product')]
        cat = ' > '.join(bc[:-1]) if len(bc) > 1 else (bc[0] if bc else '')
    return OrderedDict([
        ('model', model), ('models_in_page', models[:8]), ('title', page['title']), ('h1', page['h1'][:1]),
        ('category', cat), ('url', page['url']), ('fetched_at', page['fetched_at']),
        ('ports', port_summary(text)), ('description', page['description']),
        ('spec_rows', spec_rows[:120]), ('downloads', page['downloads']), ('images', page['images'][:40]),
        ('excerpt', page['text_excerpt'][:2500]),
    ])


def slug_of(url):
    p = unquote(urlparse(url).path).strip('/').replace('/', '_')
    p = re.sub(r'[^A-Za-z0-9._-]+', '_', p).strip('_') or 'index'
    return p[:120]


def md_escape(s):
    return (s or '').replace('|', '\\|')


def write_product_md(cfg, prod, pages_dir):
    os.makedirs(pages_dir, exist_ok=True)
    fn = os.path.join(pages_dir, slug_of(prod['url']) + '.md')
    L = []
    title = prod['h1'][0] if prod['h1'] else prod['title']
    L.append(f"# {title}")
    L.append('')
    L.append(f"> 来源：<{prod['url']}>（抓取 {prod['fetched_at']}，原文照录；中文仅为栏目名）  ")
    if prod['model']:
        L.append(f"> 官网型号：**{prod['model']}**" + (f"；页内其他型号：{', '.join(prod['models_in_page'][1:])}" if len(prod['models_in_page']) > 1 else ''))
    if prod['category']:
        L.append(f"> 类目：{prod['category']}")
    if prod['ports']:
        L.append(f"> 端口要点（正则抽取）：{prod['ports']}")
    L.append('')
    if prod['description']:
        L.append('## Description (meta)')
        L.append(prod['description'])
        L.append('')
    if prod['spec_rows']:
        L.append('## Specification（表格逐行）')
        L.append('| 项 | 值 |')
        L.append('|---|---|')
        for row in prod['spec_rows']:
            if len(row) == 1:
                L.append(f"| **{md_escape(row[0])}** | |")
            else:
                L.append(f"| {md_escape(row[0])} | {md_escape(' / '.join(row[1:]))} |")
        L.append('')
    if prod['excerpt']:
        L.append('## 页面正文摘录')
        L.append('```')
        L.append(prod['excerpt'])
        L.append('```')
        L.append('')
    if prod['downloads']:
        L.append('## 下载')
        for d in prod['downloads']:
            L.append(f"- [{d['text'] or d['url'].rsplit('/', 1)[-1]}]({d['url']})")
        L.append('')
    if prod['images']:
        L.append('## 图片（官网 URL；本地副本见 data/<site>_site_raw/images/）')
        for u in prod['images'][:20]:
            L.append(f"- {u}")
        L.append('')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    return os.path.relpath(fn, ROOT)


def build(site):
    cfg = SITES[site]
    raw = rp(cfg['raw'])
    if not os.path.isdir(raw):
        print(f'[{site}] 原始层不存在：{cfg["raw"]}（Actions 尚未落地）')
        return
    summary = {}
    if os.path.exists(os.path.join(raw, 'summary.json')):
        summary = json.load(open(os.path.join(raw, 'summary.json'), encoding='utf-8'))
    manifest = read_jsonl(os.path.join(raw, 'pages_manifest.jsonl'))
    pages = []
    for rec in manifest:
        if rec.get('status') != 200 or not rec.get('file'):
            continue
        hp = os.path.join(raw, rec['file'])
        if not os.path.exists(hp):
            continue
        try:
            pages.append(parse_page(site, cfg, rec, hp))
        except Exception as e:  # noqa
            print(f'[{site}] 解析失败 {rec["url"]}: {e}')
    # 去重（同一 final_url 多次）
    uniq = OrderedDict()
    for p in pages:
        key = (p['final_url'] or p['url']).rstrip('/')
        if key not in uniq:
            uniq[key] = p
    pages = list(uniq.values())
    pages.sort(key=lambda p: (p['type'], p['url']))
    os.makedirs(rp(cfg['out']), exist_ok=True)
    with open(rp(cfg['out']) + '/pages.json', 'w', encoding='utf-8') as f:
        json.dump(OrderedDict([('site', cfg['host']), ('summary', summary), ('pages', pages)]), f, ensure_ascii=False, indent=1)
    products = [product_record(site, p) for p in pages if p['type'] == 'product']
    with open(rp(cfg['out']) + '/products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=1)
    # CSV 页面索引
    with open(rp(cfg['csv_pages']), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['类型', 'URL', '标题', 'H1', '描述', '表格数', '下载数', '图片数', '正文行数', '抓取时间', '本地文件'])
        for p in pages:
            w.writerow([p['type'], p['url'], p['title'], ' | '.join(p['h1']), p['description'], len(p['tables']), len(p['downloads']), len(p['images']), p['text_lines'], p['fetched_at'], p['file']])
    # CSV 产品索引
    with open(rp(cfg['csv_products']), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['官网型号', '标题', '类目', '端口要点', '规格行数', '下载数', 'URL', '抓取时间'])
        for pr in products:
            w.writerow([pr['model'], pr['h1'][0] if pr['h1'] else pr['title'], pr['category'], pr['ports'], len(pr['spec_rows']), len(pr['downloads']), pr['url'], pr['fetched_at']])
    # docs
    docs = rp(cfg['docs'])
    os.makedirs(docs, exist_ok=True)
    by_type = defaultdict(list)
    for p in pages:
        by_type[p['type']].append(p)
    L = [f"# {cfg['name']} 官网页面索引（{cfg['host']}）", '',
         f"> 由 `scripts/suppliers_crawl/build.py` 从 `{cfg['raw']}/` 生成；页面 {len(pages)}，产品页 {len(products)}。"
         f" 抓取状态：complete={summary.get('complete')}，pages_ok={summary.get('pages_ok')}/{summary.get('pages_total')}，"
         f"downloads_ok={summary.get('downloads_ok')}/{summary.get('downloads_total')}，images_ok={summary.get('images_ok')}/{summary.get('images_total')}，"
         f"crawled_at={summary.get('crawled_at')}。", '']
    order = ['home', 'page', 'service', 'category', 'product', 'post']
    for t in order + [t for t in by_type if t not in order]:
        if t not in by_type:
            continue
        L.append(f"## {t}（{len(by_type[t])}）")
        L.append('| 标题 | URL | 抓取 | 表格/下载/图 |')
        L.append('|---|---|---|---|')
        for p in by_type[t]:
            L.append(f"| {md_escape(p['title'])[:90]} | <{p['url']}> | {(p['fetched_at'] or '')[:10]} | {len(p['tables'])}/{len(p['downloads'])}/{len(p['images'])} |")
        L.append('')
    with open(os.path.join(docs, '01-官网页面索引.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    # 产品清单 + 单页
    pdir = os.path.join(docs, 'products')
    paths = []
    for pr in products:
        paths.append(write_product_md(cfg, pr, pdir))
    L = [f"# {cfg['name']} 官网产品清单", '',
         f"> {len(products)} 个产品页（原文照录见 `products/`）。端口要点为正则抽取，以单页规格表为准。", '',
         '| 官网型号 | 标题 | 类目 | 端口要点 | 单页 |', '|---|---|---|---|---|']
    for pr, pth in zip(products, paths):
        L.append(f"| {md_escape(pr['model'])} | {md_escape((pr['h1'][0] if pr['h1'] else pr['title'])[:80])} | {md_escape(pr['category'])[:40]} | {md_escape(pr['ports'])} | [{os.path.basename(pth)}](products/{os.path.basename(pth)}) |")
    with open(os.path.join(docs, '02-官网产品清单.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    tc = Counter(p['type'] for p in pages)
    print(f"[{site}] pages={len(pages)} {dict(tc)} products={len(products)} models={sum(1 for p in products if p['model'])} complete={summary.get('complete')}")


if __name__ == '__main__':
    targets = sys.argv[1:] or list(SITES)
    for s in targets:
        build(s)
