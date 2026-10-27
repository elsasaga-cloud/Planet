#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q-65 国别机检（T29-U72，2026-10-27）：用电话国家码 / 北美区号 / 域名 ccTLD 反推国别，与 entities.json 的 iso 比对，列出疑似填错的户。
只读 entities.json，不改任何数据；结果写 docs/国别机检_Q-65_<日期>.md + data/saga_clients/country_check_<日期>.json。
规则（保守，宁漏勿错）：
  - 电话：纯数字串。10 位（或 11 位以 1 开头）→ NANP，按区号分 US / CA / 加勒比；≥11 位且不以 0 开头 → 按国家码前缀表（最长匹配）判国；以 0 开头 = 本国格式，跳过。
  - 域名：ccTLD（.de .ca .tr …）≠ iso 记一票；通用 TLD 不计；.co/.io/.me/.tv/.ai/.cc/.eu/.us 不计。
  - 只有「电话国 ≠ iso」或「ccTLD ≠ iso」才列出；电话多数票决定建议国；A/B 列前，C 只计数 + 附表。
用法：python3 scripts/saga_clients/country_check.py
"""
import json, os, re, sys, datetime
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT  # noqa

TODAY = datetime.date.today().isoformat()
ENT = os.path.join(ROOT, 'data', 'saga_clients', 'entities.json')

CA_AREA = set('204 226 236 249 250 263 289 306 343 354 365 367 368 382 403 416 418 428 431 437 438 450 468 474 506 514 519 548 579 581 584 587 604 613 639 647 672 683 705 709 742 753 778 780 782 807 819 825 867 873 879 902 905'.split())
CARIB = {'242': 'BS', '246': 'BB', '264': 'AI', '268': 'AG', '284': 'VG', '340': 'VI', '345': 'KY', '441': 'BM', '473': 'GD', '649': 'TC', '658': 'JM', '664': 'MS', '670': 'MP', '671': 'GU', '684': 'AS', '721': 'SX', '758': 'LC', '767': 'DM', '784': 'VC', '787': 'PR', '809': 'DO', '829': 'DO', '849': 'DO', '868': 'TT', '869': 'KN', '876': 'JM', '939': 'PR'}
CC = {  # 国家码 → ISO（最长匹配）；7 = RU/KZ 不判
    '20': 'EG', '27': 'ZA', '30': 'GR', '31': 'NL', '32': 'BE', '33': 'FR', '34': 'ES', '36': 'HU', '39': 'IT', '40': 'RO', '41': 'CH', '43': 'AT', '44': 'GB', '45': 'DK', '46': 'SE', '47': 'NO', '48': 'PL', '49': 'DE',
    '51': 'PE', '52': 'MX', '53': 'CU', '54': 'AR', '55': 'BR', '56': 'CL', '57': 'CO', '58': 'VE', '60': 'MY', '61': 'AU', '62': 'ID', '63': 'PH', '64': 'NZ', '65': 'SG', '66': 'TH', '81': 'JP', '82': 'KR', '84': 'VN', '86': 'CN', '90': 'TR', '91': 'IN', '92': 'PK', '93': 'AF', '94': 'LK', '95': 'MM', '98': 'IR',
    '212': 'MA', '213': 'DZ', '216': 'TN', '218': 'LY', '220': 'GM', '221': 'SN', '223': 'ML', '225': 'CI', '233': 'GH', '234': 'NG', '237': 'CM', '243': 'CD', '244': 'AO', '249': 'SD', '251': 'ET', '254': 'KE', '255': 'TZ', '256': 'UG', '260': 'ZM', '263': 'ZW', '264': 'NA',
    '351': 'PT', '352': 'LU', '353': 'IE', '354': 'IS', '355': 'AL', '356': 'MT', '357': 'CY', '358': 'FI', '359': 'BG', '370': 'LT', '371': 'LV', '372': 'EE', '373': 'MD', '374': 'AM', '375': 'BY', '376': 'AD', '380': 'UA', '381': 'RS', '382': 'ME', '383': 'XK', '385': 'HR', '386': 'SI', '387': 'BA', '389': 'MK',
    '420': 'CZ', '421': 'SK', '423': 'LI', '502': 'GT', '503': 'SV', '504': 'HN', '505': 'NI', '506': 'CR', '507': 'PA', '509': 'HT', '591': 'BO', '593': 'EC', '595': 'PY', '598': 'UY', '852': 'HK', '853': 'MO', '855': 'KH', '856': 'LA', '880': 'BD', '886': 'TW',
    '960': 'MV', '961': 'LB', '962': 'JO', '963': 'SY', '964': 'IQ', '965': 'KW', '966': 'SA', '967': 'YE', '968': 'OM', '970': 'PS', '971': 'AE', '972': 'IL', '973': 'BH', '974': 'QA', '975': 'BT', '976': 'MN', '977': 'NP', '992': 'TJ', '993': 'TM', '994': 'AZ', '995': 'GE', '996': 'KG', '998': 'UZ',
}
CCTLD = {'de': 'DE', 'ca': 'CA', 'tr': 'TR', 'uk': 'GB', 'fr': 'FR', 'pl': 'PL', 'ru': 'RU', 'in': 'IN', 'au': 'AU', 'it': 'IT', 'es': 'ES', 'nl': 'NL', 'se': 'SE', 'no': 'NO', 'dk': 'DK', 'fi': 'FI', 'be': 'BE', 'ch': 'CH', 'at': 'AT', 'cz': 'CZ', 'sk': 'SK', 'hu': 'HU', 'ro': 'RO', 'bg': 'BG', 'gr': 'GR', 'pt': 'PT', 'ie': 'IE', 'lt': 'LT', 'lv': 'LV', 'ee': 'EE', 'ua': 'UA', 'by': 'BY', 'kz': 'KZ', 'rs': 'RS', 'hr': 'HR', 'si': 'SI', 'ba': 'BA', 'mk': 'MK', 'al': 'AL', 'cy': 'CY', 'il': 'IL', 'ae': 'AE', 'sa': 'SA', 'qa': 'QA', 'kw': 'KW', 'om': 'OM', 'bh': 'BH', 'jo': 'JO', 'lb': 'LB', 'eg': 'EG', 'ma': 'MA', 'tn': 'TN', 'dz': 'DZ', 'ng': 'NG', 'ke': 'KE', 'za': 'ZA', 'gh': 'GH', 'pk': 'PK', 'bd': 'BD', 'lk': 'LK', 'np': 'NP', 'th': 'TH', 'vn': 'VN', 'my': 'MY', 'sg': 'SG', 'id': 'ID', 'ph': 'PH', 'kr': 'KR', 'jp': 'JP', 'tw': 'TW', 'hk': 'HK', 'cn': 'CN', 'nz': 'NZ', 'mx': 'MX', 'br': 'BR', 'ar': 'AR', 'cl': 'CL', 'co': None, 'pe': 'PE', 'uy': 'UY', 'py': 'PY', 'bo': 'BO', 'ec': 'EC', 've': 'VE', 'uz': 'UZ', 'az': 'AZ', 'ge': 'GE', 'am': 'AM', 'md': 'MD', 'mt': 'MT', 'is': 'IS', 'lu': 'LU', 'ir': 'IR', 'iq': 'IQ', 'bt': 'BT', 'mn': 'MN', 'kh': 'KH', 'mm': 'MM', 'us': None, 'eu': None, 'io': None, 'me': None, 'tv': None, 'ai': None, 'cc': None}
NAMES = {'US': '美国', 'CA': '加拿大', 'GB': '英国', 'DE': '德国', 'TR': '土耳其', 'IN': '印度', 'IL': '以色列', 'AU': '澳大利亚', 'FR': '法国', 'IT': '意大利', 'ES': '西班牙', 'PL': '波兰', 'NL': '荷兰', 'MX': '墨西哥', 'PR': '波多黎各', 'DO': '多米尼加', 'JM': '牙买加', 'TT': '特立尼达和多巴哥', 'BS': '巴哈马', 'BB': '巴巴多斯', 'KY': '开曼群岛', 'BM': '百慕大'}


NSN = {  # 国家码后的号码位数（E.164 国家有效号码长度，粗表）；长度不符 → 不判
    'TR': (10,), 'DE': (10, 11), 'GB': (10,), 'FR': (9,), 'IT': (9, 10), 'ES': (9,), 'PL': (9,), 'NL': (9,), 'RU': (10,), 'IN': (10,), 'IL': (9,), 'AU': (9,), 'AE': (9,), 'SA': (9,), 'SG': (8,), 'TH': (9,), 'ID': (9, 10, 11), 'VN': (9,), 'PK': (10,), 'MY': (9, 10), 'CZ': (9,), 'SK': (9,), 'HU': (9,), 'RO': (9,), 'BG': (8, 9), 'GR': (10,), 'PT': (9,), 'LT': (8,), 'CY': (8,), 'UA': (9,), 'BY': (9,), 'KZ': (10,), 'RS': (8, 9), 'BR': (10, 11), 'MX': (10,), 'AR': (10,), 'CL': (9,), 'CO': (10,), 'ZA': (9,), 'NG': (10,), 'EG': (10,), 'KR': (9, 10), 'JP': (10,), 'TW': (9,), 'CN': (11,), 'HK': (8,), 'NZ': (8, 9, 10), 'SE': (9,), 'NO': (8,), 'DK': (8,), 'FI': (9, 10), 'BE': (9,), 'CH': (9,), 'AT': (10, 11), 'IE': (9,), 'LB': (7, 8), 'JO': (9,), 'IQ': (10,), 'KW': (8,), 'QA': (8,), 'OM': (8,), 'BH': (8,), 'MA': (9,), 'TN': (8,), 'DZ': (9,), 'KE': (9,), 'GH': (9,), 'LK': (9,), 'BD': (10,), 'NP': (10,), 'PH': (10,), 'PE': (9,), 'EC': (9,), 'UY': (8,), 'PY': (9,), 'BO': (8,), 'VE': (10,), 'UZ': (9,), 'AZ': (9,), 'GE': (9,), 'AM': (8,), 'MD': (8,), 'MT': (8,), 'IS': (7,), 'LU': (9,), 'IR': (10,), 'HR': (8, 9), 'SI': (8,), 'BA': (8,), 'MK': (8,), 'AL': (9,), 'EE': (7, 8), 'LV': (8,), 'KH': (8, 9), 'MM': (8, 9, 10), 'MN': (8,), 'BT': (8,), 'ET': (9,), 'TZ': (9,), 'UG': (9,), 'ZM': (9,), 'ZW': (9,), 'CM': (9,), 'CI': (10,), 'SN': (9,), 'SD': (9,), 'LY': (9,), 'TM': (8,), 'TJ': (9,), 'KG': (9,), 'AF': (9,), 'SY': (9,), 'YE': (9,), 'PS': (9,), 'MV': (7,), 'GT': (8,), 'SV': (8,), 'HN': (8,), 'NI': (8,), 'CR': (8,), 'PA': (8,), 'HT': (8,), 'CU': (8,), 'MO': (8,), 'LA': (8, 9), 'AD': (6,), 'LI': (7,), 'AO': (9,), 'CD': (9,), 'NA': (9,), 'GM': (7,), 'ML': (8,), 'XK': (8,), 'ME': (8,),
}
NANP_ISO = {'US', 'CA', '??'} | set(CARIB.values())


def phone_country(p, iso=''):
    d = re.sub(r'\D', '', p or '')
    if not d or d.startswith('0'):
        return None
    explicit_1 = False
    if len(d) == 11 and d.startswith('1'):
        d = d[1:]; explicit_1 = True
    if len(d) == 10 and d[0] in '23456789' and (explicit_1 or iso in NANP_ISO):
        a = d[:3]
        if a in CA_AREA:
            return 'CA'
        if a in CARIB:
            return CARIB[a]
        return 'US'
    if len(d) >= 11:
        for n in (3, 2):
            cc = d[:n]
            if cc in CC:
                c = CC[cc]
                if len(d) - n in NSN.get(c, ()):
                    return c
                return None
        if d[0] == '7' and len(d) == 11:
            return 'RU/KZ'
    return None


def tld_country(dom):
    t = (dom or '').lower().rsplit('.', 1)[-1]
    return CCTLD.get(t)


def main():
    ents = json.load(open(ENT, encoding='utf-8'))
    out = []
    for e in ents:
        iso = e.get('iso') or '??'
        phones = e.get('phones') or []
        if isinstance(phones, str):
            try:
                phones = eval(phones)
            except Exception:
                phones = []
        votes = Counter(c for c in (phone_country(p, iso) for p in phones) if c)
        doms = e.get('domains') or []
        if isinstance(doms, str):
            try:
                doms = eval(doms)
            except Exception:
                doms = []
        tlds = Counter(c for c in (tld_country(d) for d in doms) if c)
        ph_best = votes.most_common(1)[0][0] if votes else None
        tl_best = tlds.most_common(1)[0][0] if tlds else None
        ph_bad = bool(ph_best) and ph_best not in (iso, 'RU/KZ') and not (ph_best == 'RU/KZ' and iso in ('RU', 'KZ'))
        tl_bad = bool(tl_best) and tl_best != iso
        if not (ph_bad or tl_bad):
            continue
        # 建议国：电话优先（有实号），其次 ccTLD；两者矛盾时标「待看官网」
        sug = ph_best if ph_bad else tl_best
        conf = '高' if (ph_bad and tl_bad and ph_best == tl_best) else ('中' if ph_bad and len(votes) == 1 and votes[ph_best] >= 1 else '低')
        if ph_bad and tl_best and tl_best == iso:
            conf = '低（域名支持原国别，电话可能是海外联系人）'
        out.append({'code': e['code'], 'grade': e.get('grade'), 'name': e.get('name'), 'iso': iso, 'country': e.get('country'),
                    'phone_votes': dict(votes), 'tld_votes': dict(tlds), 'suggest': sug, 'confidence': conf,
                    'phones': phones[:3], 'domains': doms[:3]})
    out.sort(key=lambda r: ({'A': 0, 'B': 1, 'C': 2}.get(r['grade'], 3), r['code']))
    jp = os.path.join(ROOT, 'data', 'saga_clients', f'country_check_{TODAY}.json')
    json.dump(out, open(jp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    by_grade = Counter(r['grade'] for r in out)
    pairs = Counter(f"{r['iso']}→{r['suggest']}" for r in out)
    L = [f'# 国别机检（Q-65）— {TODAY}', '',
         f'来源：`scripts/saga_clients/country_check.py` 只读 `entities.json`（{len(ents)} 户），用电话国家码 / 北美区号 / 域名 ccTLD 反推国别并与表内 iso 比对。**不改任何数据**；确认后用 research JSON 的 `country_fix` 纠正（build.py 已支持，原值留 `country_table`）。',
         '', f'疑似户：**{len(out)}**（A {by_grade.get("A", 0)} / B {by_grade.get("B", 0)} / C {by_grade.get("C", 0)}）。最多的方向：' + '、'.join(f'{k} {v}' for k, v in pairs.most_common(8)) + '。',
         '', '置信度：高 = 电话与域名同指一国；中 = 只有电话（单一国家码）；低 = 只有域名 ccTLD，或域名支持原国别（电话可能是海外联系人 / 代理）。',
         '', '## A / B 档（逐户看官网后再 country_fix）', '', '| 编号 | 档 | 名称 | 表内 | 建议 | 置信 | 电话票 | 域名票 | 电话样本 |', '|---|---|---|---|---|---|---|---|---|']
    for r in out:
        if r['grade'] in ('A', 'B'):
            L.append(f"| {r['code']} | {r['grade']} | {str(r['name'])[:40]} | {r['iso']} {r['country']} | {r['suggest']} {NAMES.get(r['suggest'], '')} | {r['confidence']} | {r['phone_votes']} | {r['tld_votes']} | {' / '.join(r['phones'])} |")
    L += ['', '## C 档（只列，不处理）', '', '| 编号 | 名称 | 表内 | 建议 | 置信 |', '|---|---|---|---|---|']
    for r in out:
        if r['grade'] == 'C':
            L.append(f"| {r['code']} | {str(r['name'])[:40]} | {r['iso']} | {r['suggest']} | {r['confidence']} |")
    mp = os.path.join(ROOT, 'docs', f'国别机检_Q-65_{TODAY}.md')
    open(mp, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(mp, len(out), dict(by_grade), pairs.most_common(10))


if __name__ == '__main__':
    main()
