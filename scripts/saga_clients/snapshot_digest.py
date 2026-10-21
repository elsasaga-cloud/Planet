#!/usr/bin/env python3
"""
T27 · 官网快照摘要器（第 4 步，可选）：
  data/saga_clients/site_snapshots/<编号>.json（GitHub Actions 批量抓取的官网原始摘要）
    → data/saga_clients/site_digest.json（每家一条紧凑摘要：状态 / 标题 / 语言 / 关键词画像 / 站内型号 / 公开邮箱电话 /
       产品页 / 站内出现的品牌 / 自动对位建议）
  render.py 读取 site_digest.json，在每份 MD「客户调研」下渲染「官网快照（自动摘要）」小节；
  对尚无 saga_fit 的实体，用快照关键词给出自动 P1（标注「官网快照对位」）。
  b_tiers.py 读取同一文件补「快照状态」列。
用法：python3 snapshot_digest.py   （无参数；幂等；不改 research/*.json）
"""
import glob
import json
import os
import re
from collections import Counter
from urllib.parse import unquote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
SNAP = os.path.join(DATA, 'site_snapshots')
OUT = os.path.join(DATA, 'site_digest.json')

# 站内出现即记录的品牌（同行 / 可替代 / 渠道信号）；键 = 正则（小写匹配），值 = 展示名
BRANDS = {
    r'\bplanet\b': 'PLANET', r'tp-?link': 'TP-Link', r'ubiquiti|unifi': 'Ubiquiti', r'mikrotik': 'MikroTik',
    r'\bcisco\b': 'Cisco', r'hikvision': 'Hikvision', r'\bdahua\b': 'Dahua', r'\bmoxa\b': 'Moxa',
    r'hirschmann': 'Hirschmann', r'phoenix contact': 'Phoenix Contact', r'\bnetgear\b': 'Netgear',
    r'd-?link': 'D-Link', r'\bzyxel\b': 'Zyxel', r'\baruba\b': 'Aruba', r'\bhuawei\b': 'Huawei',
    r'\bh3c\b': 'H3C', r'\bruijie\b|reyee': 'Ruijie', r'\btenda\b': 'Tenda', r'\bgrandstream\b': 'Grandstream',
    r'\bcambium\b': 'Cambium', r'\baxis\b': 'Axis', r'\buniview\b|\bunv\b': 'Uniview', r'\bonv\b': 'ONV',
    r'\bunipoe\b': 'UniPoE', r'\bmaiwe\b': 'Maiwe', r'\bkorenix\b': 'Korenix', r'\betherwan\b': 'EtherWAN',
    r'\bwestermo\b': 'Westermo', r'\badvantech\b': 'Advantech', r'\blantech\b': 'Lantech', r'\boring\b': 'ORing',
    r'\bantaira\b': 'Antaira', r'\bcomnet\b': 'ComNet', r'\bbarox\b': 'barox', r'\bteltonika\b': 'Teltonika',
    r'\bfs\.com\b|\bfiberstore\b': 'FS.com', r'\bsiemens\b': 'Siemens', r'\bschneider\b': 'Schneider',
    r'\bubnt\b': 'Ubiquiti', r'\bedimax\b': 'Edimax', r'\blevelone\b': 'LevelOne', r'\btrendnet\b': 'TRENDnet',
    r'\bintellinet\b': 'Intellinet', r'\bextralink\b': 'Extralink', r'\bpulsar\b': 'Pulsar', r'\bvivotek\b': 'Vivotek',
    r'\bhanwha\b|\bwisenet\b': 'Hanwha', r'\bbosch\b': 'Bosch', r'\bmilesight\b': 'Milesight', r'\bajax\b': 'Ajax',
    r'\bparadox\b': 'Paradox', r'\bzkteco\b': 'ZKTeco', r'\bfortinet\b': 'Fortinet', r'\bjuniper\b': 'Juniper',
    r'\ballied telesis\b': 'Allied Telesis', r'\bsmartbyte\b': 'SmartByte（！）',
    r'\bhrui\b|\bhongrui\b': 'HRUI（！）', r'\bhohunet\b': 'Hohunet（！）', r'\bsaga ?tele': 'Saga（！）',
}
# 常用词同名品牌：改为大小写敏感 / 带限定词，避免 extreme conditions / ajax 脚本 / the planet / x-axis / paradox 污染
for _k in [r'\bplanet\b', r'\baxis\b', r'\bajax\b', r'\bparadox\b']:
    BRANDS.pop(_k, None)
BRANDS_CS = {
    r'\bPLANET\b|[Pp]lanet [Tt]echnolog|planet\.com\.tw|planetechusa': 'PLANET',
    r'\bAXIS\b|[Aa]xis [Cc]ommunications|[Aa]xis [Cc]amera': 'Axis',
    r'\bAJAX\b|[Aa]jax [Ss]ystems|[Aa]jax [Hh]ub|[Aa]jax [Aa]larm|[Aa]jax [Ss]ecurity': 'Ajax',
    r'\bPARADOX\b|[Pp]aradox [Ss]ecurity|[Pp]aradox [Aa]larm': 'Paradox',
    r'[Ee]xtreme [Nn]etworks|\bEXTREME\b': 'Extreme',
}
BRAND_RE = [(re.compile(k, re.I), v) for k, v in BRANDS.items()] + [(re.compile(k), v) for k, v in BRANDS_CS.items()]
# 监控/建站平台产生的伪邮箱（sentry/wix 哈希、example、图片名等）
JUNK_EMAIL = re.compile(r'(sentry|wixpress|example\.|@.*\.(png|jpg|jpeg|gif|svg|webp)$|^[0-9a-f]{24,}@|noreply|no-reply|schema\.org)', re.I)

# 只保留子串计数可靠的词（site_snapshot.py 用 str.count 子串计数：'din'/'olt'/'ups'/'isp'/'rack'/'onu' 等会被
# coding/voltage/groups/display/track/bonus 污染，弃用）
KW_ORDER = ['switch', 'poe', 'industrial', 'automation', 'scada', 'sfp', 'media converter', 'fiber', 'fibre', 'ethernet',
            'gigabit', '10g', '2.5g', 'camera', 'cctv', 'nvr', 'surveillance', 'access control', 'wireless', 'wifi',
            'telecom', 'ftth', 'datacenter', 'data center', 'cable', 'oem', 'odm', 'distributor', 'wholesale',
            'integrator', 'installer', 'planet', 'mikrotik', 'ubiquiti', 'tp-link', 'cisco', 'moxa', 'hikvision',
            'dahua', 'uniview', 'axis']


def pages(snap):
    """所有已抓页面（首页 + 子页），过滤空值。"""
    out = []
    h = snap.get('home')
    if isinstance(h, dict) and (h.get('title') or h.get('text')):
        out.append(('home', h))
    for sp in snap.get('subpages') or []:
        if isinstance(sp, dict) and (sp.get('title') or sp.get('text')):
            out.append(('sub', sp))
    return out


def auto_p1(kw, text_low):
    """据官网关键词给出自动对位建议（仅在无人工 saga_fit 时使用）。返回 (型号, 理由) 或 (None, None)。"""
    ind = kw.get('industrial', 0) + kw.get('scada', 0) + min(kw.get('automation', 0), 5)
    poe = kw.get('poe', 0)
    sw = kw.get('switch', 0)
    tg = kw.get('10g', 0) + kw.get('2.5g', 0)
    cam = kw.get('camera', 0) + kw.get('cctv', 0) + kw.get('nvr', 0) + kw.get('surveillance', 0)
    ftth = kw.get('ftth', 0) + kw.get('telecom', 0)
    if sw + poe + ind == 0:
        return None, None
    if ind >= 4 and poe >= 1:
        return 'STI-288GP', f'官网快照对位：工业/自动化词频 {ind}、PoE {poe} → DIN 8 PoE+ 2 SFP 起手'
    if ind >= 4:
        return 'STI-280GE', f'官网快照对位：工业/自动化词频 {ind}、无 PoE 侧重 → DIN 8 GE + 2 SFP 非 PoE 起手'
    if tg >= 3 and sw >= 3:
        return 'STC-424XGGM', f'官网快照对位：10G/2.5G 词频 {tg}、交换机 {sw} → 24 GE + 4×10G L2+ 起手'
    if poe >= 6 or (cam >= 4 and poe >= 1):
        return 'STC-424DGGPM-280W', f'官网快照对位：PoE 词频 {poe}、监控 {cam} → 24 口 PoE L2+ 走量款'
    if poe >= 1:
        return 'STC-28DGGPM', f'官网快照对位：PoE 词频 {poe} → 8 口 PoE+ 2 SFP L2+ 起手'
    if ftth >= 4 and sw >= 2:
        return 'STC-424XGGM', f'官网快照对位：电信/FTTH 词频 {ftth} → 汇聚 24 GE + 4×10G'
    if sw >= 1:
        return 'STC-28DGGPM', f'官网快照对位：交换机词频 {sw}、无 PoE/工业侧重 → 8 口 L2+ 起手'
    return None, None


def digest_one(snap):
    code = snap['code']
    d = {'code': code, 'status': snap.get('status', ''), 'fetched_at': snap.get('fetched_at', ''),
         'domains': snap.get('domains') or [], 'errors': (snap.get('errors') or [])[:3]}
    pg = pages(snap)
    home = snap.get('home') if isinstance(snap.get('home'), dict) else {}
    d['final_url'] = home.get('final_url') or home.get('url') or ''
    d['http'] = home.get('http')
    d['title'] = (home.get('title') or '')[:160]
    d['desc'] = (home.get('desc') or '')[:300]
    d['lang'] = home.get('lang') or ''
    d['headings'] = [x for x in (home.get('h') or []) if x and len(x) < 80][:8]
    kw = Counter()
    models = Counter()
    emails, phones, social = set(), set(), set()
    brands = Counter()
    sub_titles = []
    text_all = []
    for kind, p in pg:
        for k, v in (p.get('kw') or {}).items():
            kw[k] += int(v)
        for m in (p.get('models') or []):
            if isinstance(m, (list, tuple)) and len(m) == 2:
                models[str(m[0])] += int(m[1])
        emails.update(e for e in (p.get('emails') or []) if '@' in e and not JUNK_EMAIL.search(e))
        phones.update(p.get('phones') or [])
        social.update(p.get('social') or [])
        t = ' '.join([p.get('title') or '', p.get('desc') or '', ' '.join(p.get('h') or []), p.get('text') or ''])
        text_all.append(t)
        if kind == 'sub':
            sub_titles.append({'title': (p.get('title') or p.get('nav_text') or '')[:120],
                               'url': unquote(p.get('final_url') or p.get('url') or '')})
    text_raw = ' '.join(text_all)
    text_low = text_raw.lower()
    for rx, name in BRAND_RE:
        n = len(rx.findall(text_low if (rx.flags & re.I) else text_raw))
        if n:
            brands[name] += n
    d['kw'] = {k: kw[k] for k in KW_ORDER if kw.get(k)}
    d['models'] = [m for m, _ in models.most_common(12)]
    d['emails'] = sorted(emails)[:6]
    d['phones'] = sorted(phones)[:6]
    d['social'] = sorted(social)[:6]
    d['brands'] = [b for b, _ in brands.most_common(12)]
    d['subpages'] = sub_titles[:8]
    sm = snap.get('sitemap') if isinstance(snap.get('sitemap'), dict) else {}
    d['sitemap_count'] = sm.get('count', 0)
    pl = [unquote(u) for u in (sm.get('product_like') or []) if isinstance(u, str)]
    # 优先目录页（category/catalog/shop/products/switch/poe/industrial），其次短 URL；单品长 URL 靠后
    def prio(u):
        lu = u.lower()
        sc = 0
        for k, w in (('switch', -6), ('poe', -6), ('industrial', -6), ('category', -4), ('catalog', -4), ('katalog', -4),
                     ('products', -3), ('product', -1), ('shop', -2), ('sklep', -2), ('urun', -2), ('ürün', -2)):
            if k in lu:
                sc += w
        return (sc, len(u))
    pl = sorted(dict.fromkeys(pl), key=prio)
    d['product_pages'] = [u[:110] + ('…' if len(u) > 110 else '') for u in pl[:8]]
    txt = re.sub(r'\s+', ' ', home.get('text') or '').strip()
    d['excerpt'] = txt[:420]
    if d['status'] == 'ok':
        d['auto_p1'], d['auto_p1_why'] = auto_p1(d['kw'], text_low)
    else:
        d['auto_p1'], d['auto_p1_why'] = None, None
    # 状态标签（供 MD 与分批表）
    d['status_cn'] = {'ok': '在线', 'parked_or_empty': '停放/空站（疑停业或仅占位）', 'timeout': '超时（站慢或封锁）',
                      'http_error': 'HTTP 错误', 'unreachable': '域名不可达（DNS/连接失败）'}.get(d['status'], d['status'])
    return d


def main():
    files = sorted(glob.glob(os.path.join(SNAP, 'S[ABC]-*.json')))
    out = {}
    st = Counter()
    for f in files:
        try:
            snap = json.load(open(f, encoding='utf-8'))
        except Exception as e:  # 损坏文件不阻断
            print('skip', f, e)
            continue
        dg = digest_one(snap)
        rp = os.path.join(DATA, 'research', dg['code'] + '.json')
        if os.path.exists(rp):
            try:
                mm = json.load(open(rp, encoding='utf-8')).get('site_mismatch')
            except Exception:
                mm = None
            if mm:  # 人工判定：抓到的网站不是本客户（表内域名误配）→ 整条摘要作废，只留说明
                dg = {'code': dg['code'], 'status': 'mismatch', 'status_cn': '域名误配（快照到的网站不是本客户）',
                      'fetched_at': dg.get('fetched_at', ''), 'domains': dg.get('domains') or [], 'errors': [str(mm)],
                      'auto_p1': None, 'auto_p1_why': None, 'brands': [], 'models': [], 'emails': [], 'phones': []}
        out[dg['code']] = dg
        st[dg['status']] += 1
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'digest {len(out)} → {OUT}', dict(st))
    auto = sum(1 for v in out.values() if v.get('auto_p1'))
    br = Counter(b for v in out.values() for b in v['brands'])
    print('auto_p1', auto, '| top brands on sites:', br.most_common(12))


if __name__ == '__main__':
    main()
