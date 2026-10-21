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


PORT_RE = re.compile(r'(\d+)\s*[x×\*]\s*(10/100/1000M?|10/100M?|100M|1000M|1G|2\.5G|5G|10G|25G|40G|50G|100G|200G|400G|800G|Gigabit|Fast Ethernet)[^,;|\n]{0,40}', re.I)


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
    'hohunet': re.compile(r'\b(I?S\d{4}[A-Z0-9]*(?:-[0-9A-Z]+)*)'),
    'hrui': re.compile(r'\b(HR[0-9A-Z]*(?:-[0-9A-Za-z+]+)+)'),
}

HRUI_CAT_NAMES = {'poe-switch': 'PoE Switch', 'ethernet-switch': 'Ethernet Switch', 'managed-switch': 'Managed Switch',
                  'industrial-poe-switch': 'Industrial PoE Switch', 'industrial-ethernet-switch': 'Industrial Ethernet Switch',
                  'optical-fiber-converter': 'Optical Fiber Converter', 'poe-accessory': 'PoE Accessory', 'wireless-bridge': 'Wireless Solutions'}


def table_rows(t):
    """rowspan/colspan 感知：返回 [(kind, cells)]，kind='§' 为整行跨列的节标题，否则 'r'；rowspan 的首列标签会补到续行。"""
    out, carry = [], {}  # carry: col -> [text, remaining]
    for tr in t.find_all('tr'):
        tds = tr.find_all(['th', 'td'])
        if not tds:
            continue
        row, col = [], 0
        # 先填入上方 rowspan 延续下来的单元格
        def fill_carry():
            nonlocal col
            while col in carry and carry[col][1] > 0:
                row.append(carry[col][0])
                carry[col][1] -= 1
                col += 1
        fill_carry()
        if len(tds) == 1 and int(tds[0].get('colspan') or 1) > 1 and not row:
            out.append(('§', [clean(tds[0].get_text(' '))]))
            continue
        for td in tds:
            txt = clean(td.get_text(' '))
            rs = int(td.get('rowspan') or 1)
            cs = int(td.get('colspan') or 1)
            row.append(txt)
            if rs > 1:
                carry[col] = [txt, rs - 1]
            col += cs
            fill_carry()
        if any(row):
            out.append(('r', row))
    return out


def flatten_spec(rows):
    """[(kind, cells)] → [(label, value)]；节标题 → ('§', title)。"""
    out = []
    for kind, cells in rows:
        if kind == '§':
            out.append(('§', cells[0]))
            continue
        cells = [c for c in cells if c != '']
        if not cells:
            continue
        if len(cells) == 1:
            out.append((out[-1][0] if out and out[-1][0] != '§' else '', cells[0]))
        else:
            out.append((cells[0], ' / '.join(cells[1:])))
    return out


def spec_dict(spec):
    """[(label, value)] → {label: 'v1 / v2'}（同名多行合并）。"""
    d = OrderedDict()
    for k, v in spec:
        if k == '§' or not k:
            continue
        d[k] = (d[k] + ' / ' + v) if k in d else v
    return d


def plain_rows(rows):
    """软件功能表等：丢掉 kind，保留单元格列表（节标题行保留为单格行）。"""
    return [cells for _, cells in rows]


def local_file_map(raw):
    """下载 / 图片 manifest：url → 本地文件（已归档的）。"""
    def fix(f):
        # 工作流把 crawl_bin/downloads 落到 data/<site>_site_raw/datasheets/，manifest 里仍写 downloads/…
        if f and not os.path.exists(os.path.join(raw, f)):
            alt = 'datasheets/' + os.path.basename(f)
            if os.path.exists(os.path.join(raw, alt)):
                return alt
            return None
        return f
    dl = {r['url']: fix(r.get('file')) for r in read_jsonl(os.path.join(raw, 'downloads_manifest.jsonl')) if r.get('file')}
    im = {r['url']: fix(r.get('file')) for r in read_jsonl(os.path.join(raw, 'images_manifest.jsonl')) if r.get('file')}
    return {k: v for k, v in dl.items() if v}, {k: v for k, v in im.items() if v}


def product_hohunet(page, soup, base, dlmap, immap):
    title = page['h1'][0] if page['h1'] else page['title'].split(' - ')[0]
    m = MODEL_RE['hohunet'].search(title or '')
    model = m.group(1) if m else ''
    sd = soup.select_one('.woocommerce-product-details__short-description')
    short = [clean(x.get_text(' ')) for x in sd.find_all(['li', 'p', 'strong'])] if sd else []
    short = [x for x in short if x]
    cats = [clean(a.get_text()) for a in soup.select('span.posted_in a')]
    tabs = {}
    for d in soup.select('div.woocommerce-Tabs-panel'):
        tid = (d.get('id') or '').replace('tab-', '')
        tabs[tid] = d
    desc = tabs.get('description')
    desc_text = '\n'.join(l for l in main_text(desc) if l) if desc else ''
    desc_imgs = [urljoin(base, (i.get('data-src') or i.get('src') or '')) for i in desc.find_all('img')] if desc else []
    hw = []
    if tabs.get('hardware-specification'):
        for t in tabs['hardware-specification'].find_all('table'):
            hw += flatten_spec(table_rows(t))
    sw = []
    if tabs.get('software-specification'):
        for t in tabs['software-specification'].find_all('table'):
            sw += plain_rows(table_rows(t))
    if not hw and tabs.get('datasheet'):  # 旧版产品页（S2xxx/S35xx）：Datasheet 页签 = 硬件表 + 软件表
        ts = tabs['datasheet'].find_all('table')
        if ts:
            hw = flatten_spec(table_rows(ts[0]))
        if len(ts) > 1:
            sw = [[k, v] for k, v in flatten_spec(table_rows(ts[1]))]
    lic = []
    if tabs.get('license'):
        for t in tabs['license'].find_all('table'):
            lic += plain_rows(table_rows(t))
    dls = []
    if tabs.get('download'):
        for a in tabs['download'].find_all('a', href=True):
            u = urljoin(base, a['href'])
            dls.append(dict(text=clean(a.get_text()), url=u, local=dlmap.get(u)))
    gallery = [urljoin(base, a['href']) for a in soup.select('.woocommerce-product-gallery__image a[href]')]
    hwd = spec_dict(hw)
    hm = MODEL_RE['hohunet'].search(hwd.get('Model', '') or '')
    if hm and (not model or hm.group(1).startswith(model)):
        model = hm.group(1)
    # 短描述去重（主题会把标题重复两遍）
    short2 = []
    for x in short:
        if x != title and x not in short2:
            short2.append(x)
    short = short2
    return OrderedDict([
        ('model', model), ('title', title), ('categories', cats), ('url', page['url']), ('fetched_at', page['fetched_at']),
        ('short', short), ('service_ports', hwd.get('Service Ports', hwd.get('Ethernet Port', ''))), ('switch_capacity', hwd.get('Packet Switch capacity', hwd.get('Switching capacity', hwd.get('Bandwidth', '')))),
        ('throughput', hwd.get('Layer 2/Layer 3 Throughput', hwd.get('Throughput', ''))), ('power_supply', hwd.get('Power supply', '')),
        ('cpu', hwd.get('CPU', '')), ('chipset_platform', hwd.get('Chipset Platform', '')), ('dimensions', hwd.get('Dimensions', '')),
        ('ports', port_summary(hwd.get('Service Ports', '') or title)),
        ('hardware', hw), ('software', sw[:400]), ('license', lic), ('downloads', dls), ('description', desc_text[:8000]),
        ('description_images', [u for u in desc_imgs if u]), ('gallery', gallery), ('gallery_local', [immap.get(u) for u in gallery]),
    ])


def product_hrui(page, soup, base, dlmap, immap, api_idx):
    t = soup.select_one('h3.detail-product-title') or soup.select_one('.detail-mdel')
    model = clean(t.get_text()) if t else ''
    brief = soup.select_one('.detail-product-brief')
    brief = clean(brief.get_text(' ')) if brief else ''
    cat_slug = urlparse(page['url']).path.strip('/').split('/')[0]
    pid = re.sub(r'\D', '', urlparse(page['url']).path.rsplit('/', 1)[-1])
    api = api_idx.get(pid, {})
    # API 的 title / product_sn 通常最干净（页面标题有时带 " - 描述" 或整句描述；个别条目后台把两字段填反）
    for cand in (api.get('product_sn'), api.get('title'), model):
        cand = (cand or '').strip()
        if re.match(r'^HR[0-9A-Z]*-?[0-9A-Z+/-]*$', cand.split(' ')[0]) and ' - ' not in cand and len(cand) <= 40:
            model = cand.split(' ')[0] if ' ' in cand else cand
            break
    else:
        model = model.split(' - ')[0].strip()
    if api.get('category'):
        cat_slug = api['category']
    pdfs = [urljoin(base, a['href']) for a in soup.select('ul.detail-product-btm a[href]') if a['href'].lower().endswith('.pdf')]
    dls = [dict(text='Datasheet', url=u, local=dlmap.get(u)) for u in pdfs]
    contents = soup.select('div.detail-product-content')
    overview, features, spec, imgs_struct = '', [], [], []
    if contents:
        c0 = contents[0]
        lines = main_text(c0)
        overview = '\n'.join(lines)
        features = [l for l in lines if l.startswith('■') or l.startswith('●') or l.startswith('•')]
        for t in c0.find_all('table'):
            spec += flatten_spec(table_rows(t))
    if len(contents) > 1:
        for t in contents[1].find_all('table'):
            spec += flatten_spec(table_rows(t))
    for c in contents[2:]:
        imgs_struct += [urljoin(base, i.get('src') or '') for i in c.find_all('img') if i.get('src')]
    gallery = []
    for i in soup.find_all('img'):
        src = i.get('src') or ''
        if '/userfiles/product/' in src and '/big/' in src:
            gallery.append(urljoin(base, src))
    gallery = list(OrderedDict.fromkeys(gallery))
    sd = spec_dict(spec)
    iface = sd.get('Interface', '') or sd.get('Port Definition', '') or sd.get('Port Configure', '') or sd.get('Device interface', '') or sd.get('Port', '')
    if not iface and api.get('title2'):
        iface = api['title2']  # API 的 title2 本身就是端口描述（如 "16-Port 10/100/1000T 802.3af/at PoE + 2-Port 2.5G SFP ..."）
    return OrderedDict([
        ('model', model or api.get('product_sn') or ''), ('title', api.get('title2') or re.sub(r'\s*(?:-\s*PoE Switch and Industrial Switch Manufacturer)?\s*\|?\s*HRUI\s*$', '', page['title']).strip()),
        ('category', HRUI_CAT_NAMES.get(cat_slug, cat_slug)), ('category_slug', cat_slug), ('site_id', pid), ('url', page['url']), ('fetched_at', page['fetched_at']),
        ('brief', brief), ('interface', iface), ('poe_budget', sd.get('PoE Power Budget', '')), ('switching_bandwidth', sd.get('Switching Bandwidth', '')),
        ('power_supply', sd.get('Power Supply', '')), ('dimensions', sd.get('Structure Information', '')), ('packing', sd.get('Package Information', '')),
        ('ports', port_summary(iface or brief or overview)),
        ('overview', overview[:6000]), ('features', features), ('spec', spec), ('downloads', dls), ('gallery', gallery),
        ('gallery_local', [immap.get(u) for u in gallery]), ('structure_images', imgs_struct),
    ])


def product_record(site, page):
    """通用兜底（非 hrui / hohunet）。"""
    text = page['title'] + '\n' + '\n'.join(page['h1']) + '\n' + page['text_excerpt']
    models = []
    for m in MODEL_RE.get(site, MODEL_RE['hrui']).findall(text):
        if m not in models:
            models.append(m)
    return OrderedDict([('model', models[0] if models else ''), ('title', page['title']), ('url', page['url']), ('fetched_at', page['fetched_at']),
                        ('ports', port_summary(text)), ('spec', []), ('downloads', page['downloads']), ('gallery', page['images'][:20])])


def slug_of(url):
    p = unquote(urlparse(url).path).strip('/').replace('/', '_')
    p = re.sub(r'[^A-Za-z0-9._-]+', '_', p).strip('_') or 'index'
    return p[:120]


def md_escape(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ')


def rel_from_docs(docs_dir, repo_rel):
    """docs/suppliers/<Name>/products/x.md → 仓库相对路径的相对链接。"""
    depth = len(docs_dir.strip('/').split('/'))
    return '../' * depth + repo_rel


def hohunet_fname(pr):
    return (re.sub(r'[^A-Za-z0-9+._-]+', '_', pr['model']) or slug_of(pr['url'])) + '.md'


def hohunet_series(pr):
    for c in pr['categories']:
        if re.match(r'^I?S\d{4}', c):
            return c
    return pr['categories'][0] if pr['categories'] else '（无类目）'


def write_hohunet_md(cfg, pr, pdir, sw_dir, sw_hashes):
    os.makedirs(pdir, exist_ok=True)
    fn = os.path.join(pdir, hohunet_fname(pr))
    raw = cfg['raw']
    L = [f"# {pr['model'] or pr['title']}", '', f"> 来源：<{pr['url']}>（抓取 {pr['fetched_at']}；英文原文照录，中文仅为栏目名）  ",
         f"> 官网标题：{pr['title']}  ", f"> 类目：{' / '.join(pr['categories']) or '—'}  ",
         f"> 端口：{pr['service_ports'] or pr['ports'] or '—'}；交换容量 {pr['switch_capacity'] or '—'}；转发 {pr['throughput'] or '—'}；电源 {pr['power_supply'] or '—'}；芯片平台 {pr['chipset_platform'] or '—'}", '']
    if pr['gallery']:
        L.append('## 产品图')
        for u, loc in zip(pr['gallery'][:6], pr['gallery_local'][:6]):
            if loc:
                L.append(f"![]({rel_from_docs(cfg['docs'] + '/products', raw + '/' + loc)})")
            else:
                L.append(f"- {u}")
        L.append('')
    if pr['short']:
        L.append('## Highlights（官网短描述）')
        for x in pr['short']:
            L.append(f"- {x}")
        L.append('')
    if pr['hardware']:
        L.append('## HARDWARE SPECIFICATION')
        L.append('| 项 | 值 |')
        L.append('|---|---|')
        for k, v in pr['hardware']:
            if k == '§':
                L.append(f"| **{md_escape(v)}** | |")
            else:
                L.append(f"| {md_escape(k)} | {md_escape(v)} |")
        L.append('')
    if pr['license']:
        L.append('## License')
        L.append('| ' + ' | '.join(md_escape(c) for c in pr['license'][0]) + ' |')
        L.append('|' + '---|' * len(pr['license'][0]))
        for row in pr['license'][1:]:
            L.append('| ' + ' | '.join(md_escape(c) for c in row) + ' |')
        L.append('')
    if pr['software']:
        h = __import__('hashlib').md5(json.dumps(pr['software'], ensure_ascii=False).encode()).hexdigest()[:10]
        swf = os.path.join(sw_dir, f'software-spec-{h}.md')
        if h not in sw_hashes:
            os.makedirs(sw_dir, exist_ok=True)
            S = [f"# Software Specification（HOS 功能表，{len(pr['software'])} 行）", '',
                 f"> 首见于 <{pr['url']}>（抓取 {pr['fetched_at']}）；同一张表的型号在各产品页链接到此。列 EB / MS / MA = license 档（○ = 支持）。", '']
            width = max(len(r) for r in pr['software'])
            S.append('| ' + ' | '.join(md_escape(c) for c in (pr['software'][0] + [''] * (width - len(pr['software'][0])))) + ' |')
            S.append('|' + '---|' * width)
            for row in pr['software'][1:]:
                row = row + [''] * (width - len(row))
                S.append('| ' + ' | '.join(md_escape(c) for c in row) + ' |')
            with open(swf, 'w', encoding='utf-8') as f:
                f.write('\n'.join(S))
            sw_hashes[h] = []
        sw_hashes[h].append(pr['model'] or pr['title'])
        L.append(f"## Software Specification\n见 [software/software-spec-{h}.md](../software/software-spec-{h}.md)（{len(pr['software'])} 行，EB / MS / MA 三档）\n")
    if pr['downloads']:
        L.append('## Download')
        for d in pr['downloads']:
            loc = f"（本地：`{raw}/{d['local']}`）" if d.get('local') else '（未归档）'
            L.append(f"- [{d['text'] or d['url'].rsplit('/', 1)[-1]}]({d['url']}) {loc}")
        L.append('')
    if pr['description']:
        L.append('## Description（原文）')
        L.append('```')
        L.append(pr['description'])
        L.append('```')
        L.append('')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    return os.path.relpath(fn, ROOT)


def hrui_fname(pr, dup_models=()):
    base = re.sub(r'[^A-Za-z0-9+._-]+', '_', pr['model']) or slug_of(pr['url'])
    if pr['model'] in dup_models:
        base += f"_{pr['site_id']}"
    return base + '.md'


def write_hrui_md(cfg, pr, pdir, dup_models=()):
    os.makedirs(pdir, exist_ok=True)
    fn = os.path.join(pdir, hrui_fname(pr, dup_models))
    raw = cfg['raw']
    L = [f"# {pr['model'] or pr['title']}", '', f"> 来源：<{pr['url']}>（抓取 {pr['fetched_at']}；英文原文照录，中文仅为栏目名）  ",
         f"> 官网描述：{pr['title'] or '—'}  ", f"> 类目：{pr['category']}（site id {pr['site_id']}）  ",
         f"> 接口：{pr['interface'] or pr['ports'] or '—'}；PoE 预算 {pr['poe_budget'] or '—'}；交换带宽 {pr['switching_bandwidth'] or '—'}；电源 {pr['power_supply'] or '—'}", '']
    if pr['brief']:
        L.append(f"**Brief:** {pr['brief']}")
        L.append('')
    if pr['gallery']:
        L.append('## 产品图')
        for u, loc in zip(pr['gallery'][:6], pr['gallery_local'][:6]):
            if loc:
                L.append(f"![]({rel_from_docs(cfg['docs'] + '/products', raw + '/' + loc)})")
            else:
                L.append(f"- {u}")
        L.append('')
    if pr['downloads']:
        L.append('## Datasheet')
        for d in pr['downloads']:
            loc = f"（本地：`{raw}/{d['local']}`" + (f"；文本：`{raw}/datasheet_text/{os.path.splitext(os.path.basename(d['local']))[0]}.txt`" if d.get('local') else '') + '）' if d.get('local') else '（未归档）'
            L.append(f"- [{d['url'].rsplit('/', 1)[-1]}]({d['url']}) {loc}")
        L.append('')
    if pr['overview']:
        L.append('## Feature and Benefits（原文）')
        L.append('```')
        L.append(pr['overview'])
        L.append('```')
        L.append('')
    if pr['spec']:
        L.append('## Parameter（规格表逐行）')
        L.append('| 项 | 值 |')
        L.append('|---|---|')
        for k, v in pr['spec']:
            if k == '§':
                L.append(f"| **{md_escape(v)}** | |")
            else:
                L.append(f"| {md_escape(k)} | {md_escape(v)} |")
        L.append('')
    if pr['structure_images']:
        L.append('## Product structure / Application topology（图）')
        for u in pr['structure_images'][:10]:
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
    dlmap, immap = local_file_map(raw)
    api_idx = {}
    api_file = os.path.join(raw, 'api', 'products_index.json')
    if os.path.exists(api_file):
        for it in json.load(open(api_file, encoding='utf-8')):
            api_idx[str(it.get('id'))] = it
    pages, soups = [], {}
    for rec in manifest:
        if rec.get('status') != 200 or not rec.get('file'):
            continue
        hp = os.path.join(raw, rec['file'])
        if not os.path.exists(hp):
            continue
        try:
            pg = parse_page(site, cfg, rec, hp)
            pages.append(pg)
        except Exception as e:  # noqa
            print(f'[{site}] 解析失败 {rec["url"]}: {e}')
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
    # ---- 产品页：按站点专用解析（重开 HTML）----
    products = []
    for p in pages:
        if p['type'] != 'product':
            continue
        with open(os.path.join(raw, p['file']), encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
        base = p['final_url'] or p['url']
        try:
            if site == 'hohunet':
                pr = product_hohunet(p, soup, base, dlmap, immap)
                if not pr['hardware'] and not pr['model']:
                    continue  # 非交换机的「产品」页（云平台 / SONiC 文章）仍留在 pages.json
            elif site == 'hrui':
                pr = product_hrui(p, soup, base, dlmap, immap, api_idx)
                if not pr['model']:
                    continue
            else:
                pr = product_record(site, p)
        except Exception as e:  # noqa
            print(f'[{site}] 产品解析失败 {p["url"]}: {e}')
            continue
        products.append(pr)
    # 同型号去重（HRUI 同一产品可能挂在多个类目 / 方案 URL 下：按 site_id 归并，保留内容最全的一条）
    if site == 'hrui':
        products.sort(key=lambda x: -(len(x['spec']) + len(x['downloads']) + len(x['gallery'])))
    seen_m, dedup = set(), []
    for pr in products:
        k = (pr.get('site_id') or pr['model'] or pr['url']).upper() if site == 'hrui' else (pr['model'] or pr['url']).upper()
        if k in seen_m:
            continue
        seen_m.add(k)
        dedup.append(pr)
    products = sorted(dedup, key=lambda x: (x.get('category', '') if site == 'hrui' else hohunet_series(x), x['model']))
    with open(rp(cfg['out']) + '/products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=1)
    # ---- CSV 页面索引 ----
    with open(rp(cfg['csv_pages']), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['类型', 'URL', '标题', 'H1', '描述', '表格数', '下载数', '图片数', '正文行数', '抓取时间', '本地文件'])
        for p in pages:
            w.writerow([p['type'], p['url'], p['title'], ' | '.join(p['h1']), p['description'], len(p['tables']), len(p['downloads']), len(p['images']), p['text_lines'], p['fetched_at'], p['file']])
    # ---- CSV 产品索引 + docs ----
    docs = rp(cfg['docs'])
    os.makedirs(docs, exist_ok=True)
    pdir = os.path.join(docs, 'products')
    for gen in (pdir, os.path.join(docs, 'software')):  # 生成目录整体重建，避免旧文件残留
        if os.path.isdir(gen):
            __import__('shutil').rmtree(gen)
    paths = []
    with open(rp(cfg['csv_products']), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        if site == 'hohunet':
            w.writerow(['官网型号', '官网标题', '类目', 'Service Ports', '交换容量', '转发率', '电源', 'CPU', '芯片平台', '尺寸', '规格书(本地)', 'URL', '抓取时间'])
            sw_hashes = {}
            for pr in products:
                ds = next((d['local'] for d in pr['downloads'] if d.get('local') and 'datasheet' in (d['text'] or '').lower()), '')
                w.writerow([pr['model'], pr['title'], ' / '.join(pr['categories']), pr['service_ports'], pr['switch_capacity'], pr['throughput'], pr['power_supply'], pr['cpu'], pr['chipset_platform'], pr['dimensions'], ds, pr['url'], pr['fetched_at']])
                paths.append(write_hohunet_md(cfg, pr, pdir, os.path.join(docs, 'software'), sw_hashes))
        else:
            w.writerow(['官网型号', '官网描述', '类目', 'Interface', 'PoE 预算', '交换带宽', '电源', '尺寸/重量', '装箱', '规格书(本地)', 'URL', '抓取时间'])
            dup_models = {m for m, n in Counter(p['model'] for p in products).items() if n > 1}
            for pr in products:
                ds = next((d['local'] for d in pr['downloads'] if d.get('local')), '')
                w.writerow([pr['model'], pr['title'], pr['category'], pr['interface'], pr['poe_budget'], pr['switching_bandwidth'], pr['power_supply'], pr['dimensions'], pr['packing'], ds, pr['url'], pr['fetched_at']])
                paths.append(write_hrui_md(cfg, pr, pdir, dup_models))
    # ---- 页面索引 MD ----
    by_type = defaultdict(list)
    for p in pages:
        by_type[p['type']].append(p)
    L = [f"# {cfg['name']} 官网页面索引（{cfg['host']}）", '',
         f"> 由 `scripts/suppliers_crawl/build.py` 从 `{cfg['raw']}/` 生成；HTML 页面 {len(pages)}（去重后），产品 {len(products)}。"
         f" 抓取状态：complete={summary.get('complete')}，pages_ok={summary.get('pages_ok')}/{summary.get('pages_total')}（失败多为 sitemap 里的旧 URL 404），"
         f"downloads_ok={summary.get('downloads_ok')}/{summary.get('downloads_total')}，images_ok={summary.get('images_ok')}/{summary.get('images_total')}，"
         f"crawled_at={summary.get('crawled_at')}。原始 HTML / PDF / PDF 文本 / 图片均在 `{cfg['raw']}/`。", '']
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
    # ---- 产品清单 MD ----
    L = [f"# {cfg['name']} 官网产品清单（{len(products)} 款）", '',
         f"> 由 `scripts/suppliers_crawl/build.py` 生成；每款一页见 `products/`，CSV 见 `{cfg['csv_products']}`。英文原文照录；「—」= 页面无此项。", '']
    if site == 'hohunet':
        groups = defaultdict(list)
        for pr in products:
            groups[hohunet_series(pr)].append(pr)
        for g in sorted(groups):
            L.append(f"## {g}（{len(groups[g])}）")
            L.append('| 官网型号 | 其它类目 | Service Ports | 交换容量 | 电源 | 芯片平台 | 单页 |')
            L.append('|---|---|---|---|---|---|---|')
            for pr in groups[g]:
                pth = hohunet_fname(pr)
                others = ' / '.join(c for c in pr['categories'] if c != g) or '—'
                L.append(f"| {md_escape(pr['model'])} | {md_escape(others)} | {md_escape(pr['service_ports'] or pr['ports'] or '—')[:120]} | {md_escape(pr['switch_capacity'] or '—')} | {md_escape(pr['power_supply'] or '—')} | {md_escape(pr['chipset_platform'] or '—')} | [{pth}](products/{pth}) |")
            L.append('')
    else:
        groups = defaultdict(list)
        for pr in products:
            groups[pr['category']].append(pr)
        for g in sorted(groups):
            L.append(f"## {g}（{len(groups[g])}）")
            L.append('| 官网型号 | 官网描述 | Interface | PoE 预算 | 规格书 | 单页 |')
            L.append('|---|---|---|---|---|---|')
            dup_models = {m for m, n in Counter(p['model'] for p in products).items() if n > 1}
            for pr in groups[g]:
                pth = hrui_fname(pr, dup_models)
                ds = '✓' if any(d.get('local') for d in pr['downloads']) else '—'
                L.append(f"| {md_escape(pr['model'])} | {md_escape(pr['title'] or '—')[:110]} | {md_escape(pr['interface'] or pr['ports'] or '—')} | {md_escape(pr['poe_budget'] or '—')} | {ds} | [{pth}](products/{pth}) |")
            L.append('')
    with open(os.path.join(docs, '02-官网产品清单.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    tc = Counter(p['type'] for p in pages)
    print(f"[{site}] pages={len(pages)} {dict(tc)} products={len(products)} with_datasheet={sum(1 for p in products if any(d.get('local') for d in p['downloads']))} complete={summary.get('complete')}")


if __name__ == '__main__':
    targets = sys.argv[1:] or list(SITES)
    for s in targets:
        build(s)
