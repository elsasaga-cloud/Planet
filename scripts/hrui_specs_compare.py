#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HRUI 最新规格书（Drive《洪瑞产品参数.zip》→ data/hrui_specs_2026-10/）vs 官网归档（data/hrui_site/products.json）对比。

产出：
  data/hrui_specs_2026-10/specs_extracted.json   每份规格书抽出的结构化字段 + 官网匹配 + 差异
  data/hrui_specs_2026-10/compare.json           对比结果（给 03 文档用）
用法：cd 仓库根目录 && python3 scripts/hrui_specs_compare.py
"""
import json, re, glob, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_DIR = os.path.join(ROOT, 'data/hrui_specs_2026-10')
SITE = json.load(open(os.path.join(ROOT, 'data/hrui_site/products.json'), encoding='utf-8'))
SITE_BY_MODEL = {p['model'].strip().upper(): p for p in SITE}

# 人工核对过的 ZX → 官网型号映射（自动匹配不到 / 模糊的）。None = 官网确实没有
MANUAL_MAP = {
    'ZX-AFGM-1622S-200': 'HR-AFGM-1622S-300',      # 官网只挂 300W 版（同机型，PoE 预算档不同）
    'ZX-AFGM-2444S-300': 'HR-AFGM-2444S-400',      # 官网只挂 400W 版
    'ZX900-AFG-2422S-400': 'HR900-AFG-2422S-300',  # 官网只挂 300W 版
    'ZX-SW0050+': None, 'ZX-SW0050': None, 'ZX-SW0080': None, 'ZX-SW0080+': None,  # 百兆非网管，官网无
    'ZX-SWG00160': None,
    'ZX-SWTG015AS': 'HR903-SWTG015AS', 'ZX-SWTG018AS': 'HR903-SWTG018AS', 'ZX-SWTG024AS': 'HR903-SWTG024AS',
    'ZX-SWTGW218AS': 'HR902-SWTGW218AS',
    'ZX-SWTG0C80N': None,  # 官网为 Web 网管版 HR902-SWTGW2C80N（不同型号），非网管版官网无
    'ZX-SWTG3448S': None,  # 官网无页面，但 datasheet_text 有 HR-SWTG3448S_WebManual
    'ZX-AXGM-SWTG3448S-650': None,
    'ZX900-AFG-SWTG015ANS': None,
    'ZX901-AF-821GNS': None,
    'ZX902-AF-162G': None, 'ZX902-AF-242G': None, 'ZX902-AF-42N': None, 'ZX902-AF-82GN': None, 'ZX902-AF-82N': None,
    'ZX902-AFG-411NS-65': None, 'ZX902-AFG-42N-65': None, 'ZX902-AFG-42N': None, 'ZX902-AFG-42NS': None, 'ZX902-AFG-42NS-65': None, 'ZX902-AFG-822NS': None, 'ZX902-AFG-82N': None,
}
# 902 系列 ↔ 官网 900 系列「同配置近亲」（仅用于规格参照，不算同型号）
NEAR_MAP = {
    'ZX902-AF-42N': 'HR900-AF-42N', 'ZX902-AF-82N': 'HR900-AF-82N', 'ZX902-AF-82GN': 'HR900-AF-82GN',
    'ZX902-AFG-42N-65': 'HR900-AFG-42N', 'ZX902-AFG-42N': 'HR900-AFG-42N', 'ZX902-AFG-42NS': 'HR900-AFG-42NS-65', 'ZX902-AFG-42NS-65': 'HR900-AFG-42NS-65', 'ZX902-AFG-411NS-65': 'HR900-AFG-411NS-65',
    'ZX902-AFG-822NS': 'HR900-AFG-822NS', 'ZX902-AFG-82N': 'HR900-AFG-82N',
    'ZX902-AF-162G': 'HR900-AF-1621GS-300', 'ZX902-AF-242G': 'HR900-AF-2421GS-300',
    'ZX-SWTG0C80N': 'HR902-SWTGW2C80N', 'ZX-SW0050+': 'HR-SWG0050+', 'ZX-SW0080': 'HR-SWG0080', 'ZX-SW0080+': 'HR-SWG0080+',
    'ZX-AXGM-SWTG3448S-650': 'HR-AXGM-SWTG3624AS',
}


def norm_txt(s):
    s = (s or '').replace('×', '*').replace('x', '*').replace('X', '*').replace('＊', '*')
    s = s.replace('～', '~').replace('℃', '°C').replace('˚C', '°C').replace('ºC', '°C')
    s = re.sub(r'\s+', '', s)
    return s.strip().upper()


def grab(pattern, text, flags=re.I | re.M, group=1, all_=False):
    if all_:
        return [m.group(group).strip() for m in re.finditer(pattern, text, flags)]
    m = re.search(pattern, text, flags)
    return m.group(group).strip() if m else ''


def parse_spec(text, zx_model):
    t = text.replace('\u3000', ' ').replace('\u00a0', ' ').replace('：', ':').replace('（', '(').replace('）', ')').replace('，', ', ')
    lines = [l.strip() for l in t.split('\n')]
    nonempty = [l for l in lines if l and not l.startswith('[p')]
    f = {}
    title = nonempty[0] if nonempty else ''
    if '[p1]' in t:  # PDF：标题可能折成两行，取到 Product Highlights 之前
        head = []
        for l in nonempty:
            if l.lower().startswith('product highlights') or l.startswith('【'): break
            head.append(l)
            if len(head) >= 3: break
        title = ' '.join(head)
    f['title'] = re.sub(r'\s+', ' ', title).strip()
    # 端口
    ports = grab(r'^(?:Ethernet(?: Port)?|Interface|Port)\t(.+)$', t)
    if not ports:
        # PDF 版：Interface 之后若干行到 Port Standard / IEEE
        m = re.search(r'Model\s+\S+\s*\n((?:.*\n){1,6}?)(?=.*(?:Port Standard|IEEE802\.3 \(Ethernet\)))', t)
        if m:
            cand = [l.strip() for l in m.group(1).split('\n') if re.search(r'\d+\s*\*\s*\d+', l)]
            ports = ' / '.join(cand)
    if not ports:
        m = re.search(r'^(\d+\s*[*x×]\s*10/100.*?(?:Ports?|ports?).*)$', t, re.M)
        ports = m.group(1) if m else ''
    ports = re.sub(r'\s*/\s*Interface\s+', ' / ', ports).replace('Interface ', '').strip()
    f['ports'] = ports
    if re.match(r'^Ports?\b', f['title']) and re.match(r'^\s*(\d+)', ports):  # 标题丢了口数（ZX-SWG00160）
        f['title'] = re.match(r'^\s*(\d+)', ports).group(1) + '-' + f['title']
    f['bandwidth'] = grab(r'(?:Switching )?Bandwidth\s*\t?\s*([\d.]+\s*Gbps)', t) or grab(r'Switching Capacity\s*\t?\s*([\d.]+\s*Gbps)', t)
    f['pps'] = grab(r'([\d.]+\s*Mpps)', t)
    f['mac'] = grab(r'MAC Address(?: Table)?\s*\t?\s*(\d+\s*K)', t)
    f['buffer'] = grab(r'(?:Packet Buffer(?: Memory)?|Memory cache|Buffer)\s*\t?\s*([\d.]+\s*[MK]bit)', t)
    f['poe_budget'] = grab(r'PoE Power Budget\s*\n?\s*(\d+\s*W)', t) or grab(r'^(\d+W)\s*\n\s*PoE Power Budget', t) \
        or grab(r'PO?E (?:Total )?power\s*:\s*((?:maximum\s*)?[\d.]+\s*W(?:\s*/\s*maximum\s*[\d.]+\s*W)*)', t)
    f['poe_budget'] = re.sub(r'\s+', ' ', f['poe_budget'].replace('maximum', '')).strip(' /')
    f['hipoe'] = grab(r'(Port\s*1[^\n]*?Hi-?PoE\s*\d+\s*W|Hi-?PoE\s*\d+\s*W)', t)
    psu = re.findall(r'\b(\d{2}V\s*/?\s*\d+(?:\.\d+)?A)\b', t)
    f['power_supply'] = ' / '.join(dict.fromkeys(re.sub(r'[\s/]', '', p) for p in psu))
    f['power_input'] = grab(r'(AC\s*100-240V)', t) or grab(r'(DC\s*\d+V)', t)
    f['max_power'] = grab(r'(?:Product power|Non POE board power|Mainboard power consumption|Power Consumption|Total Power)[:\t\s]*(?:\(Max\))?[:\t\s]*(?:maximum)?\s*([\d.]+\s*W)', t)
    f['temp'] = grab(r'(?:Operating|Working)\s*Temperature:?\s*(-?\d+\s*~\s*\+?\d+\s*°?C)', t)
    f['dims'] = grab(r'Product Dimensions?\s*:?\s*([\d.]+\s*\*\s*[\d.]+\s*\*\s*[\d.]+\s*mm)', t)
    f['nw'] = grab(r'(?:Product N\.W|Product Net Weight|Net Weight|N\.W)\s*:?\s*([\d.]+\s*KG)', t)
    f['pack_qty'] = grab(r'Packing Q[au]antity:?\s*(\d+)', t)
    f['chipset'] = grab(r'Chipset\t(.+)$', t) or grab(r'Chipset:?\s*([A-Z0-9*/ +-]+RTL[0-9A-Z*/ +-]*)', t)
    f['certs'] = grab(r'(?:Safety Certificat(?:e|ion))\t(.+)$', t)
    f['fan'] = grab(r'Fan Quantity\s*(\d+)', t)
    f['install'] = grab(r'Installation\s*\t?\s*([A-Za-z0-9 /,+-]+)$', t)
    f['order_model'] = grab(r'Order Info(?:rmation)?\s*\n\s*(\S+)', t)
    low = t.lower()
    feat = []
    if re.search(r'\bL3 Function\b|Static Routes?\b', t): feat.append('L3静态路由')
    if 'snmp' in low: feat.append('SNMP')
    if re.search(r'\bweb\b', low) and ('managed' in low or 'management' in low): feat.append('Web网管')
    if 'cloud' in low: feat.append('Cloud')
    if 'vlan mode' in low or re.search(r'VLAN[:：]\s*VLAN mode', t): feat.append('VLAN拨码隔离')
    if 'extend' in low: feat.append('Extend 250m')
    if 'watchdog' in low or 'watch dog' in low: feat.append('PoE看门狗')
    if re.search(r'\bbt\b|802\.3bt', low): feat.append('802.3bt')
    if '2500' in t or '2.5G' in t: feat.append('2.5G')
    if '10G' in t or '10000' in t: feat.append('10G')
    if 'console' in low: feat.append('Console')
    if 'fanless' in low: feat.append('无风扇')
    f['features'] = feat
    return f


def site_fields(p):
    """官网产品 → 同口径字段"""
    kv = collections.OrderedDict()
    for sec, line in p.get('spec') or []:
        if ' / ' in line:
            k, v = line.split(' / ', 1)
            kv.setdefault(k.strip(), []).append(v.strip())
        else:
            kv.setdefault(line.strip(), [])
    g = lambda *ks: ' / '.join(sum((kv.get(k, []) for k in ks), []))
    f = {}
    f['title'] = (p.get('title') or '').strip()
    f['ports'] = (p.get('interface') or g('Interface')).strip()
    f['bandwidth'] = (p.get('switching_bandwidth') or g('Switching Capacity', 'Switching Bandwidth', 'Bandwidth')).strip()
    f['pps'] = g('Packet Forwarding Rate', 'Forwarding Rate')
    f['mac'] = g('MAC Address Table', 'MAC Address')
    f['buffer'] = g('Packet Buffer', 'Packet Buffer Memory')
    f['poe_budget'] = (p.get('poe_budget') or g('PoE Power Budget')).strip()
    f['hipoe'] = ' / '.join(v for v in kv.get('PoE Ports', []) if re.search(r'hi-?poe|60W|90W', v, re.I))
    f['power_supply'] = ' / '.join(dict.fromkeys(x.replace(' ', '') for x in re.findall(r'\b(\d{2}V\s?\d+(?:\.\d+)?A)\b', (p.get('power_supply') or '') + ' ' + g('Power Supply'))))
    f['power_input'] = grab(r'(AC\s*100-240V)', (p.get('power_supply') or '') + ' ' + g('Power Supply'))
    f['max_power'] = g('Mainboard Power Consumption', 'Power Consumption')
    f['temp'] = grab(r'(-?\d+\s*~\s*\+?\d+\s*°?C)', g('Operating Temperature', 'Working Temperature') + ' ' + g('Working Environment'))
    f['dims'] = grab(r'Product Dimensions?\s*:?\s*([\d.]+\s*[*x×]\s*[\d.]+\s*[*x×]\s*[\d.]+\s*mm)', (p.get('dimensions') or '') + ' ' + g('Structure Information', 'Product Information'))
    f['nw'] = grab(r'Net Weight:?\s*([\d.]+\s*KG)', (p.get('dimensions') or '') + ' ' + g('Structure Information'), re.I)
    f['pack_qty'] = grab(r'Packing Quantity:?\s*(\d+)', (p.get('packing') or '') + ' ' + g('Packing Information'), re.I)
    f['chipset'] = g('Chipset')
    f['fan'] = g('Fan Quantity', 'Fan')
    f['install'] = g('Installation')
    f['url'] = p['url']
    f['category'] = p['category']
    f['spec_kv_count'] = len(kv)
    return f


COMPARE_FIELDS = [('ports', '端口'), ('bandwidth', '交换容量'), ('pps', '包转发率'), ('mac', 'MAC表'), ('buffer', '缓存'),
                  ('poe_budget', 'PoE预算'), ('hipoe', 'HiPoE'), ('power_supply', '电源适配'), ('max_power', '整机功耗'),
                  ('temp', '工作温度'), ('dims', '尺寸'), ('nw', '净重'), ('pack_qty', '装箱数'), ('chipset', '芯片'), ('fan', '风扇')]


def port_tokens(s):
    """端口描述 → 规范 token 列表 [(数量, 速率, 类型)]，忽略措辞差异。"""
    s = (s or '').replace('×', '*').replace('＊', '*')
    s = re.sub(r'\((?:Ports?\s*)?1-\d[^)]*\)', '', s)  # 去掉 (Ports 1-4 support BT) 之类括注
    s = s.replace('SFP+', 'SFPPLUS')
    s = re.sub(r'(\d)\s*/\s*(\d)', r'\1|\2', s)  # 保护 10/100/1000
    s = re.sub(r'\b(af|at)\s*/\s*(at|bt)\b', r'\1-\2', s, flags=re.I)  # 保护 af/at/bt
    s = re.sub(r'(\d)\s*-\s*Ports?', r'\1 Port', s)  # 24-Port → 24 Port
    segs = re.split(r'\s*(?:/|\+|,|;|、)\s*', s)
    toks = []
    for seg in segs:
        m = re.search(r'(\d+)\s*(?:\*|x|X|-?\s*Ports?\b)', seg)
        if not m:
            continue
        n = int(m.group(1)); u = seg.upper().replace('|', '/')
        if 'CONSOLE' in u:
            toks.append((n, '-', 'Console')); continue
        if 'USB' in u:
            toks.append((n, '-', 'USB')); continue
        if '2500' in u or '2.5G' in u: spd = '2.5G'
        elif 'SFPPLUS' in u or '10G' in u or '10000' in u: spd = '10G'
        elif '1000' in u or '1G' in u or 'GIGABIT' in u: spd = '1G'
        elif '100M' in u or '10/100' in u or '100BASE' in u or re.search(r'\b100\s*M', u): spd = '100M'
        else: spd = '?'
        if 'COMBO' in u: typ = 'Combo'
        elif 'SFP' in u: typ = 'SFP+' if spd == '10G' else 'SFP'
        else: typ = 'RJ45'
        poe = 'PoE' if re.search(r'PO\s?E', u) else ''
        toks.append((n, spd, (poe + ' ' + typ).strip()))
    # Combo 口在新规格书里可能拆成 RJ45(Combo)+SFP(Combo) 两条 → 合并成一条
    combos = [t for t in toks if t[2].endswith('Combo')]
    if len(combos) == 2 and combos[0][0] == combos[1][0]:
        toks = [t for t in toks if not t[2].endswith('Combo')] + [combos[0]]
    return sorted(toks)


def diff_fields(new, old):
    out = []
    for k, label in COMPARE_FIELDS:
        a, b = new.get(k, ''), old.get(k, '')
        if not a or not b:
            continue
        na, nb = norm_txt(a), norm_txt(b)
        if k == 'ports':
            ta, tb = port_tokens(a), port_tokens(b)
            same = (na == nb) or (ta == tb and ta)
            if not same:
                out.append({'field': k, 'label': label, 'new': a, 'site': b, 'new_tokens': ta, 'site_tokens': tb})
            continue
        elif k in ('poe_budget', 'bandwidth', 'pps', 'mac', 'buffer', 'max_power', 'nw', 'pack_qty', 'fan'):
            same = re.findall(r'[\d.]+', na) == re.findall(r'[\d.]+', nb)
        elif k == 'power_supply':
            same = set(na.split('/')) == set(nb.split('/')) or na in nb or nb in na
        elif k == 'temp':
            same = re.findall(r'-?\d+', na) == re.findall(r'-?\d+', nb)
        elif k == 'dims':
            same = re.findall(r'[\d.]+', na) == re.findall(r'[\d.]+', nb)
        else:
            same = na == nb or na in nb or nb in na
        if not same:
            out.append({'field': k, 'label': label, 'new': a, 'site': b})
    return out


def main():
    man = json.load(open(os.path.join(SPEC_DIR, 'manifest.json'), encoding='utf-8'))
    docs = [f for f in man['files'] if f['ext'] in ('.doc', '.docx', '.pdf') and f['status'] == 'ok']
    results = []
    for d in docs:
        j = json.load(open(os.path.join(SPEC_DIR, 'text', d['id'] + '.json'), encoding='utf-8'))
        parts = d['path'].split('/')
        cat, folder = parts[2], parts[3]
        fname = re.sub(r'\.(docx?|pdf)$', '', parts[-1])
        fname = re.sub(r'\s*[（(]\s*(?:英文|EN)\s*[)）]?\s*$', '', fname).replace(' 英文', '').strip()
        if not fname.upper().startswith('ZX') or folder.upper().startswith(fname.upper()):
            model_name = folder  # 文件名只是省略了功率档后缀 → 以文件夹名为准
        else:
            model_name = fname   # 同一文件夹放了两个型号（42N / 42NS）或带 -M 后缀
        fields = parse_spec(j['text'], model_name)
        # 匹配
        zx = model_name.upper()
        hr = re.sub(r'^ZX', 'HR', zx)
        base = re.sub(r'-(\d{2,3})$', '', hr)
        match, how = None, ''
        key = model_name if model_name in MANUAL_MAP else folder
        if key in MANUAL_MAP:
            match, how = MANUAL_MAP[key], 'manual' if MANUAL_MAP[key] else 'none'
        elif hr in SITE_BY_MODEL:
            match, how = hr, 'exact'
        elif base in SITE_BY_MODEL:
            match, how = base, 'base'
        near = NEAR_MAP.get(model_name) or NEAR_MAP.get(folder)
        rec = {'zx_model': model_name, 'folder': folder, 'category_in_zip': cat, 'doc': '/'.join(parts[1:]), 'doc_id': d['id'], 'doc_chars': d['chars'],
               'photos': [], 'fields': fields, 'site_model': match, 'match': how, 'near_model': near}
        if match:
            sf = site_fields(SITE_BY_MODEL[match.upper()])
            rec['site_fields'] = sf
            rec['diffs'] = diff_fields(fields, sf)
        elif near:
            sf = site_fields(SITE_BY_MODEL[near.upper()])
            rec['near_fields'] = sf
            rec['near_diffs'] = diff_fields(fields, sf)
        results.append(rec)
    # 照片
    for f in man['files']:
        if f['ext'] in ('.jpg', '.png'):
            parts = f['path'].split('/')
            for r in results:
                if len(parts) > 3 and parts[3] == r['folder']:
                    r['photos'].append({'name': parts[-1], 'status': f['status'], 'thumb': f.get('thumb'), 'ocr_chars': f.get('chars', 0)})
    results.sort(key=lambda r: (r['category_in_zip'], r['zx_model']))
    json.dump(results, open(os.path.join(SPEC_DIR, 'specs_extracted.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # 官网有、规格书无
    covered = {r['site_model'].upper() for r in results if r['site_model']}
    missing = collections.defaultdict(list)
    for p in SITE:
        if p['model'].strip().upper() not in covered:
            missing[p['category']].append(p['model'].strip())
    summary = {
        'docs': len(results), 'matched': sum(1 for r in results if r['site_model']),
        'not_on_site': [r['zx_model'] for r in results if not r['site_model']],
        'with_diffs': sum(1 for r in results if r.get('diffs')),
        'site_missing_by_category': {k: sorted(v) for k, v in missing.items()},
    }
    json.dump(summary, open(os.path.join(SPEC_DIR, 'compare.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    md_report(results, summary, os.path.join(ROOT, 'docs/suppliers/HRUI/03-最新规格书vs官网_2026-10.md'))
    print(json.dumps(summary, ensure_ascii=False, indent=1)[:3000])
    for r in results:
        print('\n==', r['zx_model'], '->', r['site_model'], r['match'], '| near', r['near_model'])
        fl = r['fields']
        print('  ', fl['title'][:70], '| ports:', fl['ports'][:90])
        print('   bw', fl['bandwidth'], '| pps', fl['pps'], '| mac', fl['mac'], '| buf', fl['buffer'], '| poe', fl['poe_budget'], '| hipoe', fl['hipoe'][:40], '| psu', fl['power_supply'], '| maxP', fl['max_power'], '| temp', fl['temp'], '| dims', fl['dims'], '| nw', fl['nw'], '| qty', fl['pack_qty'], '| chip', fl['chipset'][:40], '| fan', fl['fan'], '| order', fl['order_model'], '|', ','.join(fl['features']))
        for dd in r.get('diffs') or r.get('near_diffs') or []:
            print('   DIFF', dd['label'], '| 新:', dd['new'][:80], '| 官网:', dd['site'][:80])


# ───────────────────────── Markdown 报告 ─────────────────────────
SAGA_MAP = {  # ZX 型号 → (Saga 对应型号, 说明)；依据 data/hrui_STC对照表.csv 的端口解码
    'ZX902-AF-162G': ('STC-0216GFP', '对照表原记「官网无同配置机型」→ 新规格书补齐'),
    'ZX902-AF-242G': ('STC-0224GFP', '对照表原记「官网无同配置机型」→ 新规格书补齐'),
    'ZX901-AF-821GNS': ('STC-128GFP', '对照表原记「官网无同配置机型」→ 新规格书补齐'),
    'ZX900-AFG-SWTG015ANS': ('STC-114XGDGP', '对照表原记「官网无同配置机型」→ 新规格书补齐'),
    'ZX-SWTG3448S': ('STC-448XGGM', '对照表原记「官网无同配置机型」→ 新规格书补齐'),
    'ZX-AXGM-SWTG3448S-650': ('STC-448XGGPM', '对照表原记「官网无同配置机型」→ 新规格书补齐；型号标 650，规格书写 PoE 总功率 600W、电源 54V14.8A+12V6A、主板 57.2W、0~40°C、2 台/箱'),
    'ZX902-AF-42N': ('STC-024FP', '902 新一代（小机箱、口 1 HiPoE 60W）'),
    'ZX902-AF-82N': ('STC-028FP', '902 新一代'),
    'ZX902-AF-82GN': ('STC-028GFP', '902 新一代'),
    'ZX902-AFG-42N-65': ('STC-024GP', '902 新一代'),
    'ZX902-AFG-42NS': ('STC-204GP', '902 新一代'),
    'ZX902-AFG-411NS-65': ('STC-114GP', '902 新一代'),
    'ZX902-AFG-822NS': ('STC-228GP', '902 新一代'),
    'ZX902-AFG-82N': ('STC-028GP / STC-208GP', '902 新一代'),
    'ZX-SWTG0C80N': ('STC-08XGE', '另一款 8×10G-T 非网管（12V8A，机架）；对照表原对 HR500S-8T'),
    'ZX-SW0050': ('—', '百兆非网管，价格主表没有对应 STC 型号（只有千兆 STC-05GE）'),
    'ZX-SW0050+': ('—', '百兆非网管塑壳，价格主表无'),
    'ZX-SW0080': ('—', '百兆非网管，价格主表无'),
    'ZX-SW0080+': ('—', '百兆非网管塑壳，价格主表无'),
    'ZX-SWG00160': ('STC-016GE（近似）', '16 口千兆桌面 12V1A、0~40°C，无 VLAN/Extend 拨码；对照表 STC-016GE 对的是 HR-SWG10160D/-M'),
}
DIFF_NOTES = {  # 同型号差异的人工判读
    'ZX-AFGM-1622S-200': '同一机型两个功率档（200W=52V3.84A／300W=52V5.76A，规格书并列写 180W/280W），官网只挂 300W 档并写 285W；净重差 = 档位差。非冲突。',
    'ZX-AFGM-2444S-300': '规格书给的是 300W 档（52V5.76A→PoE 280W），官网只挂 400W 档（52V7.69A→370W）。同机型不同功率档，非冲突。',
    'ZX-AFGM-82NS': '**PoE 预算 110W（新）vs 100W（官网）**，电源同为 52V2.3A（≈120W）。以新规格书为准，待 HRUI 确认。',
    'ZX-AXGM-SWTG3624AS-450': '电源 54V7.69A（新）vs 56V7.15A（官网）→ 都≈400W，电源模块规格微调。',
    'ZX200-AFGM-SWTG3424S-400': '辅助电源 12V5A（新）vs 12V4A（官网），主电源一致。',
    'ZX900-AF-82GN': '**疑似规格书笔误**：新规格书写「POE power maximum 60W」但电源仍是 52V2.3A（=120W），官网为 115W；同系列 82N 为 110W。按 110~115W 理解，待 HRUI 确认。',
    'ZX900-AF-82N': 'PoE 110W（新）vs 115W（官网），电源同 52V2.3A，口径差异。',
    'ZX900-AFG-2422S-400': '**新功率档**：规格书是 400W 版（PoE 380W、440×280×44、3.565kg、EN8850DH+RTL8238B），官网只有 300W 版（285W、440×204×44）和 300D。可视为新 SKU。',
    'ZX900-AFG-82N': '新规格书仍是 220×161×44 老文档（-10~50°C、448Kbit、整机 10W），官网页面写 0~40°C、1Mbit、6.5W；PoE 预算都 110W。同型号两套文档口径不一，待 HRUI 确认哪套现行。',
    'ZX900-AFG-SWTG018ANS': 'PoE 90W（新）vs 85W（官网），电源同 52V1.92A（100W）；净重 0.91 vs 0.916kg 四舍五入。口径差。',
    'ZX900-AF-1621GS-300': 'PoE 270W（新）vs 290W（官网），电源同 52V5.76A（300W）。口径差，报价按 270W 保守写。',
    'ZX900-AF-2421GS-300': 'PoE 270W（新）vs 290W（官网），电源同 52V5.76A（300W）。口径差，报价按 270W 保守写。',
    'ZX900-AFG-162S-200': 'PoE 180W（新）vs 185W（官网），电源同 52V3.84A（200W）。口径差。',
    'ZX900-AFG-242S-300': 'PoE 286.46W（新，按电源 300W 减整机 18.4W 算）vs 280W（官网）。口径差。',
    'ZX900-AFG-411NS-65': '高度 44.5 vs 44mm、净重 0.63 vs 0.65kg，取整差。',
    'ZX900-AFG-42NS-65': '高度 44.5 vs 44mm，取整差。',
    'ZX-SWG10482S': '**MAC 32K（新）vs 16K（官网）；电源 12V4A（新）vs 12V2A（官网）；工作温度 -10~50°C（新）vs 0~40°C（官网）**；整机 38W vs 33.99W。方案可能已换代，待 HRUI 确认。',
    'ZX-SWTG342408F': '端口写法差：新规格书「24×SFP + 8×Combo」= 把 8 个 Combo 的 SFP 侧也算进 SFP 总数；官网「16×SFP + 8×Combo」。实际硬件一致（16 SFP + 8 Combo + 4×10G SFP+）。',
    'ZX-SWTG3424S': '尺寸 440×205 vs 440×204，取整差。',
    'ZX-SWTG3624AS': '**电源 12V5A（新，整机 52W）vs 12V8A（官网）**。待 HRUI 确认。',
}


def md_report(results, summary, out_path):
    L = []
    A = L.append
    new_models = [r for r in results if not r['site_model']]
    matched = [r for r in results if r['site_model']]
    A('# HRUI 最新规格书（2026-10）vs 官网归档 · 差异报告\n')
    A('> 来源：Simon 2026-10-22 上传 Drive 根目录《洪瑞产品参数.zip》（231.9 MB，md5 `4eb45804e03c1e4934c5b9164aced7cb`），HRUI 刚发来的最新规格书包。'
      '全量抽取结果在 `data/hrui_specs_2026-10/`（`manifest.json`、`text/*.json` 逐文件全文、`thumbs/` 产品照缩略图、`_coverage.md`），原件备份在私有 Release `files-hrui_specs_2026-10`。'
      '官网基线 = 2026-10-21 抓取的 `data/hrui_site/products.json`（182 款）+ `docs/suppliers/HRUI/02-官网产品清单.md`。'
      '结构化抽取与比对脚本：`scripts/hrui_specs_compare.py` → `data/hrui_specs_2026-10/specs_extracted.json`、`compare.json`。\n')
    A('## 0. 一句话结论\n')
    A(f'- 压缩包 = **62 款商用交换机的英文规格书（45 .doc / 5 .docx / 12 .pdf）+ 251 张产品照片**，按三个文件夹分：「交换机」30 款（非网管 + 非 PoE 网管）、「900及管理型POE交换机」22 款、「902POE交换机」10 款。**没有价格**，没有工业级、没有 PoE 配件 / 光纤收发器 / 无线。')
    A('- 型号前缀全部是 **ZX-**（中性/贴牌命名），与官网 **HR-** 一一对应（`ZX900-AFG-82NS` = `HR900-AFG-82NS`，产品照文件名仍叫 `HR-AFGM-1622GS…`）。这是 HRUI 给贴牌客户用的「去品牌」版本，Saga 可直接改成 STC- 对外使用。')
    A(f'- 62 款中 **{len(matched)} 款能对上官网型号**（含 3 款只是功率档不同、1 款 -M 后缀），**{len(new_models)} 款官网没有**：'
      '① **全新「902」PoE 系列 10 款 + 901 系列 1 款**（小机箱 200×118×44、口 1 HiPoE 60W、0~40°C、VLAN/Extend 按键、20 台/箱）；'
      '② 百兆非网管 4 款（5/8 口，铁壳/塑壳）+ 16 口千兆桌面 1 款；'
      '③ 48 口 L3 机型 2 款（`ZX-SWTG3448S` 48GE+4×10G、`ZX-AXGM-SWTG3448S-650` 48GE PoE+4×10G，口 1-4 支持 bt 90W）；'
      '④ 4×2.5G PoE + 2.5G + 10G SFP+ 的 `ZX900-AFG-SWTG015ANS`；⑤ 8×10G-T 非网管 `ZX-SWTG0C80N`。')
    A(f'- 同型号参数对比：**{sum(1 for r in matched if r.get("diffs"))} 款有差异**，其中值得向 HRUI 核实的 5 处：'
      '`HR-AFGM-82NS` PoE 100→110W；`HR-SWG10482S` MAC 16K→32K / 电源 12V2A→12V4A / 温度 0~40→-10~50°C；`HR-SWTG3624AS` 电源 12V8A→12V5A；'
      '`HR900-AF-82GN` 规格书写 PoE 60W（疑笔误，电源 52V2.3A）；`HR900-AFG-82N` 两套文档口径不一。其余是功率档/四舍五入/写法差异。')
    A('- 对 Saga 的直接价值：**对照表里 6 个「官网无同配置机型」的 STC 型号现在有了 HRUI 规格书**（STC-0216GFP、STC-0224GFP、STC-128GFP、STC-114XGDGP、STC-448XGGM、STC-448XGGPM），'
      '另外 STC-248GE 其实对应官网已有的 HR-SWG10482S（对照表原记为无，已更正）。百兆 PoE 三款（STC-024FP/028FP/028GFP）和千兆小 PoE 五款在 902 系列里都有新一代版本。\n')

    A('## 1. 官网没有的型号（20 款）\n')
    A('| ZX 型号 | 规格书标题 | 端口 | PoE 预算 / 电源 | 其他 | 官网最接近 | Saga 对应 | 备注 |')
    A('|---|---|---|---|---|---|---|---|')
    for r in new_models:
        f = r['fields']
        poe = f['poe_budget'] or '—'
        if f['hipoe']: poe += '；' + f['hipoe']
        extra = ' / '.join(x for x in [f['bandwidth'] and ('交换 ' + f['bandwidth']), f['mac'] and ('MAC ' + f['mac']), f['temp'], f['dims'], f['nw'], f['pack_qty'] and (f['pack_qty'] + ' 台/箱'), ('风扇 ' + f['fan']) if f['fan'] else ''] if x)
        saga, note = SAGA_MAP.get(r['zx_model'], ('—', ''))
        A(f"| `{r['zx_model']}` | {f['title'].replace('Datasheet ', '')} | {f['ports']} | {poe} / {f['power_supply'] or f['power_input'] or '—'} | {extra} | {r['near_model'] or '—'} | {saga} | {note} |")
    A('')
    A('### 1.1 「902」系列 vs 官网「900」系列（同端口近亲对比）\n')
    A('902 系列是 HRUI 新一代非网管 PoE（官网完全没有）。相对 900 系列的共同变化：机箱 220×161×44 → **200×118×44**（24 口以下）；'
      '**口 1 支持 HiPoE 60W**（42N/82N/82GN/42N-65/411NS/822NS）；工作温度 -10~50°C → **0~40°C**；按键三模式 **VLAN / Normal / Extend**（Extend 口 1-8 强制 10M、250 m、自动开 PoE 看门狗）；'
      '缓存 448Kbit → 768Kbit~1Mbit；百兆款 PoE 预算略降（82N/82GN 115W → 90W，42N 60W → 50W，电源 52V2.3A → 52V1.85A、52V1.25A → 52V1.05A）；装箱 10 → 20 台；挂耳可选。\n')
    A('| 902 新型号 | 对应 900 官网型号 | 差异（新 vs 官网） |')
    A('|---|---|---|')
    for r in new_models:
        if r.get('near_diffs') is not None and r['near_model'] and r['zx_model'].startswith('ZX90'):
            dd = '；'.join(f"{d['label']} {d['new']} vs {d['site']}" for d in r['near_diffs']) or '仅机箱/文档口径差'
            A(f"| `{r['zx_model']}` | {r['near_model']} | {dd} |")
    A('')

    A('## 2. 能对上官网的型号（42 款）与参数差异\n')
    A('对比字段：端口、交换容量、包转发率、MAC 表、缓存、PoE 预算、HiPoE、电源适配器、整机功耗、工作温度、尺寸、净重、装箱数、芯片、风扇（两边都有值才比；措辞差异已归一化）。\n')
    A('| ZX 型号 | 官网型号 | 匹配 | 差异字段（新 vs 官网） | 判读 |')
    A('|---|---|---|---|---|')
    for r in matched:
        dd = r.get('diffs') or []
        how = {'exact': '同名', 'base': '同名（去功率档后缀）', 'manual': '人工核对', }.get(r['match'], r['match'])
        if dd:
            cell = '；'.join(f"**{d['label']}** {d['new'][:60]} vs {d['site'][:60]}" for d in dd)
        else:
            cell = '一致'
        A(f"| `{r['zx_model']}` | {r['site_model']} | {how} | {cell} | {DIFF_NOTES.get(r['zx_model'], '') if dd else ''} |")
    A('')

    A('## 3. 官网有、这包规格书里没有的型号\n')
    A('这包只覆盖**商用交换机**三类，所以工业级（46 款）、PoE 配件（20）、光纤收发器（6）、无线（6）整类缺席是正常的，不代表停产。商用三类里缺的：\n')
    cat_note = {
        'Ethernet Switch': '非网管：官网的 HR300S 2.5G 系列（新命名体系）、HR500S-8T、HR-SWG10160D（规格书给的是 -M 版）没在包里。',
        'PoE Switch': '非网管 PoE：官网 HR200 系列（200 系）、HR903-AF-xxY 系列、HR200P/HR200-AXG 系列、以及若干功率档（-300/-400/-120/300D）没在包里；'
                      '`HR900-AFG-822NS` 官网有但包里只有 902 版 `ZX902-AFG-822NS`。',
        'Managed Switch': '网管：官网 HR210P/HR310S/HR510P/HR510S/HR530S/HR230S（新命名体系）、Web 网管 HR-AFGW/HR-SWGW/HR-SWTGW 系列、HR-SWTG3C12F、HR902-SWTGW2C80N、HR200-AFGM 系列没在包里。',
    }
    for cat in ('Ethernet Switch', 'PoE Switch', 'Managed Switch'):
        ms = summary['site_missing_by_category'].get(cat, [])
        A(f'- **{cat}**（缺 {len(ms)} 款）：' + '、'.join(f'`{m}`' for m in ms))
        A(f'  - {cat_note[cat]}')
    others = {k: len(v) for k, v in summary['site_missing_by_category'].items() if k not in ('Ethernet Switch', 'PoE Switch', 'Managed Switch')}
    A('- 整类缺席：' + '、'.join(f'{k} {n} 款' for k, n in others.items()) + '（详见 `02-官网产品清单.md`）。')
    A('- 注意官网同时存在两套命名（`HR-SWTG…/HR900-…` 老体系 与 `HR300S/HR510S/HR210P…` 新体系），这包规格书**全部用老体系**改前缀 ZX；对照表 `data/hrui_STC对照表.csv` 里对到新体系型号的 Saga 机型（STC-15XGDGE↔HR300S-5T1XS 等）在本包里对应的是老体系同配置款（ZX-SWTG015AS 等）。\n')

    A('## 4. 需要向 HRUI 确认的问题（建议一封邮件一次问完）\n')
    A('1. `HR-AFGM-82NS` 管理型 8 口 PoE：PoE 预算到底 100W 还是 110W（电源 52V2.3A）？')
    A('2. `HR-SWG10482S` 48+2 口非网管：新规格书 MAC 32K / 12V4A / -10~50°C，官网 16K / 12V2A / 0~40°C —— 是否换了方案？现货是哪一版？')
    A('3. `HR-SWTG3624AS` 24×2.5G+6×10G L3：电源 12V5A（整机 52W）还是 12V8A？')
    A('4. `HR900-AF-82GN`：规格书写 PoE 最大 60W，但电源 52V2.3A、官网 115W，是否笔误？')
    A('5. `HR900-AFG-82N`：规格书（220×161、-10~50°C、448Kbit）与官网页面（0~40°C、1Mbit、6.5W）哪套是现行版本？是否已被 `ZX902-AFG-82N`（200×118）取代？')
    A('6. 902 系列（10 款）是否已量产、与 900 系列价格关系（替代还是并行）？`ZX900-AFG-2422S-400` 400W 版是否新 SKU、价格？')
    A('7. 包里没有工业级和 2.5G 新体系（HR300S/HR510S…），是否另有规格书包？是否有最新价格表（手头的是 2026Q3 Drive 版）？\n')

    A('## 5. 对仓库其他文件的影响\n')
    A('- `data/hrui_STC对照表.csv`：新增列 `规格书2026-10(ZX型号)`，把 62 款 ZX 型号按端口解码挂到对应 STC 行；原「官网无同配置机型」的 7 行（STC-248GE、STC-0216GFP、STC-0224GFP、STC-128GFP、STC-114XGDGP、STC-448XGGM、STC-448XGGPM）结论改为「规格书有」。')
    A('- `data/价格主表.csv`：**不变**（这包没有价格）。百兆非网管 4 款、`ZX-SWG00160`、`ZX-SWTG0C80N`、902 系列、400W/650W 档如需报价要先向 HRUI 问价。')
    A('- `docs/suppliers/HRUI/00-画像与资料地图.md`：补一条「2026-10 ZX 规格书包」资料入口。')
    A('- 产品照片（251 张，含正/背/左/右面）缩略图在 `data/hrui_specs_2026-10/thumbs/`，原图在 Release；做 Saga 产品页时可用（中性外观，无 HRUI logo 需逐张核对——部分文件名含 ZX 字样即为去标版）。\n')
    A('## 6. 抽取覆盖率\n')
    A('313 个成员文件：正文 ok 160 / 仅元数据 112（无文字的产品照）/ 失败 0 / 重复 4；62 份规格书全部成功（.doc 经 LibreOffice 转 docx 后按段落+表格抽取，.pdf 按页抽取），字符数 2.5k~9.4k/份。细目见 `data/hrui_specs_2026-10/_coverage.md`。')
    open(out_path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('md →', out_path, len(L), 'lines')


if __name__ == '__main__':
    main()
