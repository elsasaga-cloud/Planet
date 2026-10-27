# -*- coding: utf-8 -*-
"""External Clients 公共件：国别映射、邮箱/URL 抽取、Saga 重叠、S 箱群发对账、机械初判（XA/XB/XC）。
用法见 README（scripts/external_clients/操作步骤.md）。只读外部仓库克隆 /home/user/.cache/ext/{edge,mik,cctv}。"""
import csv
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
EXT = '/home/user/.cache/ext'
DATA = os.path.join(ROOT, 'data', 'external_clients')

EM = re.compile(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+')
URL = re.compile(r'https?://[^\s)\]>|」』,;，；]+')
PHONE = re.compile(r'\+\d[\d\s().-]{6,}\d')

GENERIC = {
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'yahoo.co.uk', 'live.com', 'icloud.com', 'mail.ru', 'yandex.ru',
    '163.com', 'qq.com', 'protonmail.com', 'aol.com', 'pec.it', 'legalmail.it', 'rediffmail.com', 'vnn.vn', 'googlemail.com',
    'me.com', 'msn.com', 'web.de', 'gmx.de', 'gmx.net', 't-online.de', 'orange.fr', 'wanadoo.fr', 'free.fr', 'libero.it',
    'virgilio.it', 'tin.it', 'ukr.net', 'i.ua', 'seznam.cz', 'wp.pl', 'o2.pl', 'onet.pl', 'interia.pl', 'bk.ru', 'list.ru',
    'inbox.ru', 'rambler.ru', 'sapo.pt', 'telenet.be', 'skynet.be', 'bluewin.ch', 'hispeed.ch', 'btinternet.com', 'btconnect.com',
    'sky.com', 'mac.com', 'ymail.com', 'rocketmail.com', 'email.cz', 'centrum.cz', 'volny.cz', 'abv.bg', 'mail.bg',
    'hotmail.co.uk', 'hotmail.fr', 'hotmail.it', 'yahoo.fr', 'yahoo.it', 'yahoo.de', 'yahoo.es', 'yahoo.ca', 'yahoo.gr',
    'otenet.gr', 'pec.cloud', 'arubapec.it', 'legalmail.com', 'postecert.it', 'pec.impresa.it', 'example.com', 'domain.com',
}

# 中文国名 → ISO2
COUNTRY = {
    '美国': 'US', '加拿大': 'CA', '土耳其': 'TR', '英国': 'GB', '爱尔兰': 'IE', '法国': 'FR', '德国': 'DE', '荷兰': 'NL', '比利时': 'BE',
    '卢森堡': 'LU', '奥地利': 'AT', '瑞士': 'CH', '列支敦士登': 'LI', '意大利': 'IT', '西班牙': 'ES', '葡萄牙': 'PT', '丹麦': 'DK',
    '瑞典': 'SE', '挪威': 'NO', '芬兰': 'FI', '冰岛': 'IS', '波兰': 'PL', '捷克': 'CZ', '斯洛伐克': 'SK', '匈牙利': 'HU',
    '斯洛文尼亚': 'SI', '克罗地亚': 'HR', '塞尔维亚': 'RS', '波黑': 'BA', '波斯尼亚和黑塞哥维那': 'BA', '黑山': 'ME', '北马其顿': 'MK',
    '马其顿': 'MK', '阿尔巴尼亚': 'AL', '希腊': 'GR', '塞浦路斯': 'CY', '马耳他': 'MT', '罗马尼亚': 'RO', '保加利亚': 'BG',
    '科索沃': 'XK', '爱沙尼亚': 'EE', '拉脱维亚': 'LV', '立陶宛': 'LT', '摩尔多瓦': 'MD', '乌克兰': 'UA', '白俄罗斯': 'BY', '俄罗斯': 'RU',
    '格鲁吉亚': 'GE', '亚美尼亚': 'AM', '阿塞拜疆': 'AZ', '哈萨克斯坦': 'KZ', '乌兹别克斯坦': 'UZ', '吉尔吉斯斯坦': 'KG',
    '塔吉克斯坦': 'TJ', '土库曼斯坦': 'TM', '蒙古': 'MN', '以色列': 'IL', '阿联酋': 'AE', '沙特': 'SA', '沙特阿拉伯': 'SA', '卡塔尔': 'QA',
    '科威特': 'KW', '巴林': 'BH', '阿曼': 'OM', '约旦': 'JO', '黎巴嫩': 'LB', '伊拉克': 'IQ', '伊朗': 'IR', '埃及': 'EG', '摩洛哥': 'MA',
    '突尼斯': 'TN', '阿尔及利亚': 'DZ', '利比亚': 'LY', '南非': 'ZA', '尼日利亚': 'NG', '肯尼亚': 'KE', '坦桑尼亚': 'TZ', '乌干达': 'UG',
    '卢旺达': 'RW', '埃塞俄比亚': 'ET', '加纳': 'GH', '科特迪瓦': 'CI', '塞内加尔': 'SN', '喀麦隆': 'CM', '赞比亚': 'ZM', '津巴布韦': 'ZW',
    '莫桑比克': 'MZ', '安哥拉': 'AO', '纳米比亚': 'NA', '博茨瓦纳': 'BW', '毛里求斯': 'MU', '印度': 'IN', '巴基斯坦': 'PK', '孟加拉': 'BD',
    '孟加拉国': 'BD', '斯里兰卡': 'LK', '尼泊尔': 'NP', '不丹': 'BT', '马尔代夫': 'MV', '韩国': 'KR', '日本': 'JP', '中国台湾': 'TW',
    '台湾': 'TW', '中国台北': 'TW', '中国香港': 'HK', '香港': 'HK', '澳门': 'MO', '中国澳门': 'MO', '中国': 'CN', '中国大陆': 'CN',
    '越南': 'VN', '泰国': 'TH', '马来西亚': 'MY', '新加坡': 'SG', '印尼': 'ID', '印度尼西亚': 'ID', '菲律宾': 'PH', '柬埔寨': 'KH',
    '缅甸': 'MM', '老挝': 'LA', '文莱': 'BN', '澳大利亚': 'AU', '新西兰': 'NZ', '巴布亚新几内亚': 'PG', '斐济': 'FJ', '墨西哥': 'MX',
    '巴西': 'BR', '阿根廷': 'AR', '智利': 'CL', '哥伦比亚': 'CO', '秘鲁': 'PE', '厄瓜多尔': 'EC', '委内瑞拉': 'VE', '玻利维亚': 'BO',
    '巴拉圭': 'PY', '乌拉圭': 'UY', '哥斯达黎加': 'CR', '巴拿马': 'PA', '危地马拉': 'GT', '洪都拉斯': 'HN', '萨尔瓦多': 'SV',
    '尼加拉瓜': 'NI', '多米尼加': 'DO', '牙买加': 'JM', '特立尼达和多巴哥': 'TT', '波多黎各': 'PR', '古巴': 'CU',
}
EUROPE = {
    'GB', 'IE', 'FR', 'DE', 'NL', 'BE', 'LU', 'AT', 'CH', 'LI', 'IT', 'ES', 'PT', 'DK', 'SE', 'NO', 'FI', 'IS', 'PL', 'CZ', 'SK', 'HU',
    'SI', 'HR', 'RS', 'BA', 'ME', 'MK', 'AL', 'GR', 'CY', 'MT', 'RO', 'BG', 'EE', 'LV', 'LT', 'MD', 'XK',
}
MAIN = EUROPE | {'US', 'CA', 'TR'}
SECOND = {'RU', 'IN', 'KR'}          # Simon 2026-08-02：「一些俄罗斯 印度 韩国客户」
RISK = {'UA', 'BY', 'RU'}            # 战争/结算风险 → 先 XB

BIG_GROUP = re.compile(
    r'\b(Ingram|TD ?SYNNEX|Tech Data|ALSO\b|Bechtle|Arrow\b|Westcon|Exclusive Networks|ADN\b[^|]{0,40}Distribution|Computacenter|Atea\b|Softcat|'
    r'Insight Enterprises|CDW\b|Dustin|KOMSA|Esprinet|Infinigate|Nuvias|Anixter|WESCO|Graybar|Rexel|Sonepar|Conrad\b|RS Components|'
    r'Farnell|Mouser|Digi-?Key|Avnet|Elko\b|ASBIS|Siemens|Schneider|ABB\b|Honeywell|Johnson Controls|Bosch|Securitas|Redington|'
    r'Mitie|Vodafone|Orange\b|Telef[oó]nica|Deutsche Telekom|AT&T|Verizon|NTT\b|Fujitsu|Hitachi|Toshiba|Samsung|LG\b|Accenture|'
    r'Capgemini|Atos\b|IBM\b|HPE\b|Hewlett|Dell\b|Lenovo|Cisco\b)\b', re.I)
VENDOR = re.compile(r'\b(APRESIA|Edgecore|Edge-core|Accton|MikroTik\s*(SIA|Latvia)?$|Allied Telesis|PLANET Technology|Ubiquiti|'
                    r'Moxa|ORing|Westermo|Perle|Antaira|Netonix|ComNet|Advantech|HMS Networks|Red Lion|N-Tron|TP-Link|Zyxel|'
                    r'Hikvision|Dahua|Uniview|Axis Communications|Altronix|Lantronix|Microchip|Marvell|Realtek|Broadcom)\b', re.I)
GUARD = re.compile(r'(轨交|铁路|railway|rolling stock|军|defen[cs]e|military|船舶|海事|marine|IP67|云管|cloud[- ]managed|核电|nuclear)', re.I)
PERSON = re.compile(r"^[A-ZÀ-Ž][a-zà-ž'’.-]+(\s+[A-ZÀ-Ž]\.)?(\s+[A-ZÀ-Žde][a-zà-ž'’.-]+){1,2}$")
COMPANY_TOKEN = re.compile(r'\b(ApS|A/S|AB|AS|Oy|GmbH|AG|KG|Ltd|Limited|LLC|Inc|Corp|BV|B\.V\.|NV|SIA|UAB|OÜ|Srl|S\.r\.l|SpA|S\.p\.A|SL|S\.L|SA|S\.A|'
                           r'Kft|Zrt|d\.o\.o|s\.r\.o|Sp\.? ?z ?o\.? ?o|PSA|sarl|SARL|SAS|EURL|Lda|Pty|Sdn|Bhd|Co\.|Company|Group|Networks?|Systems?|'
                           r'Solutions?|Technolog|Telecom|Communications?|Informati|Elektro|Electr|Distribut|Service|Consult|Studio|Agency|IT\b|ICT)', re.I)


def iso_of(country_zh):
    c = (country_zh or '').strip()
    c = re.sub(r'[（(].*?[)）]', '', c).strip()
    if c in COUNTRY:
        return COUNTRY[c]
    for k, v in COUNTRY.items():          # 「德国/英国」「美国 (TX)」
        if c.startswith(k):
            return v
    return ''


def emails_in(text):
    out = []
    for e in EM.findall(text or ''):
        e = e.lower().strip('.')
        if e.endswith(('.png', '.jpg', '.jpeg', '.svg', '.md')):
            continue
        if 'firstname' in e or 'lastname' in e or 'example' in e or 'xxx@' in e or e.startswith(('f.lastname', 'first.')):
            continue
        if e not in out:
            out.append(e)
    return out


def domain_of(website):
    w = (website or '').strip().lower()
    w = re.sub(r'^\**', '', w)
    w = re.sub(r'^(https?://)?(www\.)?', '', w)
    w = w.split('/')[0].split(' ')[0].split('（')[0].split('(')[0].strip('*`,;')
    return w if '.' in w else ''


_saga = None


def saga_domains():
    """Saga Clients 全部实体：域名 → (code, grade)；公共域排除。"""
    global _saga
    if _saga is not None:
        return _saga
    ents = json.load(open(os.path.join(ROOT, 'data', 'saga_clients', 'entities.json'), encoding='utf-8'))
    m = {}
    for e in ents:
        code, grade = e.get('code'), e.get('grade')
        blob = json.dumps(e, ensure_ascii=False)
        for em in set(x.lower() for x in EM.findall(blob)):
            d = em.split('@')[1]
            if d not in GENERIC:
                m.setdefault(d, (code, grade))
        for d in re.findall(r'(?:https?://)?(?:www\.)?([a-z0-9-]+(?:\.[a-z0-9-]+)+)', (e.get('domain') or e.get('website') or '').lower()):
            m.setdefault(d, (code, grade))
    _saga = m
    return m


_mass = None


def mass_list():
    """S 箱 2026-09/10「24 Port PoE Managed Switch」群发名单（745 地址）：邮箱 → 行。"""
    global _mass
    if _mass is not None:
        return _mass
    p = os.path.join(ROOT, 'data', 'gmail_s', '2026-09_10群发名单_未入库.csv')
    _mass = {}
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding='utf-8-sig')):
            _mass[r['邮箱'].strip().lower()] = r
    return _mass


def touch_of(emails):
    ml = mass_list()
    hits = [ml[e] for e in emails if e in ml]
    if not hits:
        return None
    h = sorted(hits, key=lambda r: r.get('最后', ''))[-1]
    return {'箱': 'S', '邮箱': h['邮箱'], '首次': h['首次'], '最后': h['最后'], '去信': h['去信'], '来信': h['来信'], '主题': h['最后主题']}


def pregrade(rec):
    """机械初判。返回 (grade, reason, flags)。rec 需有 name/iso/type/emails_live/kp_named/stage/saga_dup/repo。"""
    flags = list(rec.get('flags') or [])
    name = rec.get('name') or ''
    iso = rec.get('iso') or ''
    typ = rec.get('type') or ''
    live = rec.get('emails_live') or []
    stage = (rec.get('stage') or '')
    if iso == 'CN':
        return 'DELETE', '大陆公司（Simon：一律删除）', flags + ['大陆']
    if rec.get('saga_dup'):
        d = rec['saga_dup']
        return 'C', f"与 Saga Clients 重叠（{d['code']}，经 {d['via']}）→ 以 Saga 档为准，本条不单独跟", flags + ['重复=Saga']
    if BIG_GROUP.search(name) or '太难·规模过大' in (rec.get('c_sub') or ''):
        return 'C', '超大集团 / 决策链太长（Saga 守界：大集团搞不定）', flags + ['大集团']
    if VENDOR.search(name):
        return 'C', '品牌原厂 / 供应商 / 同行，不是买家', flags + ['原厂或同行']
    if 'PLANET' in typ.upper() and iso == 'US':
        return 'C', 'Planet 美国渠道（Saga 规则：Versa/Planet USA = C）', flags + ['PlanetUSA']
    if GUARD.search(typ) and not re.search(r'分销|集成|VAR|SI', typ):
        flags.append('守界行业')
    if stage.startswith('02') or stage == 'replied':
        return 'A', '已回信（外部库记录）+ 渠道型买家', flags + ['已回信']
    is_person = bool(PERSON.match(name)) and not COMPANY_TOKEN.search(name)
    if is_person and ('顾问' in typ or '培训' in typ or 'MikroTik 认证' in typ):
        return 'B', '个人顾问 / 培训师（无公司实体）：慢慢跟，不当主力', flags + ['个人顾问']
    if iso in RISK:
        return 'B', f'{iso}：战争 / 结算风险，先 XB', flags + ['风险国']
    if not iso:
        return 'B', '国别未识别，待核后再定', flags + ['国别待核']
    if iso in MAIN:
        if live:
            return 'A', '主攻区（美加/欧/土）+ 渠道型买家 + 有可用商务邮箱' + ('（含实名 KP）' if rec.get('kp_named') else ''), flags
        return 'B', '主攻区但没有可用邮箱（只有表单或地址失效）→ 先 XB，补到邮箱再升', flags + ['缺联系']
    if iso in SECOND:
        return 'B', f'{iso}：Simon 口径「一些俄/印/韩」→ XB 慢慢跟', flags
    return 'B', '对口但不在主攻区（美加/欧/土以外）→ XB', flags


def phones_in(text):
    out = []
    for p in PHONE.findall(text or ''):
        p = re.sub(r'\s+', ' ', p).strip()
        if 7 <= len(re.sub(r'\D', '', p)) <= 15 and p not in out:
            out.append(p)
    return out


def urls_in(text, cap=40):
    out = []
    for u in URL.findall(text or ''):
        u = u.rstrip('.。）)*`')
        if u not in out:
            out.append(u)
        if len(out) >= cap:
            break
    return out


def section(text, title_regex):
    """返回所有标题匹配的 '## ' 小节正文（到下一个 '## ' 为止），拼接。"""
    parts = []
    for m in re.finditer(r'^##+ .*$', text, flags=re.M):
        if re.search(title_regex, m.group(0)):
            start = m.end()
            n = re.search(r'^## ', text[start:], flags=re.M)
            end = start + n.start() if n else len(text)
            parts.append(text[start:end].strip())
    return '\n\n'.join(parts)


def table_rows(block):
    rows = []
    for l in (block or '').split('\n'):
        if l.startswith('|') and not re.match(r'^\|\s*-', l):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            rows.append(cells)
    return rows
