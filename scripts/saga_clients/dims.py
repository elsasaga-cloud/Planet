#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A/B 客户多维画像（第 79 批 · T29-U61「各个维度 发挥想象力」· 2026-10-27）。

只用仓库里已有的证据（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 足迹扫描），按客户推导出此前档案里没有的维度：
  1. 时机与节律：他们来信的本地时段 / 星期 / 月份；他们回信中位时长；我方回信中位时长；本国群发打开率最高的发信窗口（全库统计）
  2. 打开偏好：我们群发里他们打开过哪些主题、从未打开哪些（Opened 标签 = 像素，退信同日的剔除；仅作参考）
  3. 报价轨迹：1:1 报过的型号 / 价 / 日期 → 今天按其档位应报的价（价格主表 2026-10-17 汇率）→ 涨跌与解释口径
  4. 品类覆盖与缺口：官网词频 / 站内型号显示的兴趣品类 vs 我们报过 / 卖过 / 他们打开过的品类 → 还没碰过的一类
  5. 规模与贴牌线索：官网站点地图规模、多品牌数、自有型号串（已在贴牌 → OEM 30% 档话术）、语言、社媒
  6. 关联户：同一封邮件里同时出现的其他编号 / 同人名 / 同电话
  7. 写信的人：来信签名里的姓名 + 职务（只认有职务关键词的）
  8. GitHub 足迹：github_presence.py 的硬匹配结果
  9. 日历窗口：对方国家近 120 天的大假 + 我方春节停产提醒
产物：data/saga_clients/dims.json（code → dims）、dims_country.json（各国窗口 / 季节）、docs/AB_热度榜_<日期>.md、docs/各国发信窗口与来询季节_<日期>.md。
render.py 读 dims.json → A/B 档案「多维画像」节。只做机械推导，每行带数字 / 日期 / 消息 key；没有信号的维度不写。
用法：python3 scripts/saga_clients/dims.py [--codes SA-001,SB-002] [--no-docs]
"""
import csv
import glob
import json
import os
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if os.path.abspath(p or '.') != _HERE]   # 本目录有 calendar.py，会遮蔽标准库 calendar（strptime 要用）
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location('saga_common', os.path.join(_HERE, 'common.py'))
_common = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_common)
DATA, ROOT = _common.DATA, _common.ROOT

TODAY = date.today()
TODAY_S = TODAY.isoformat()
OUT = os.path.join(DATA, 'dims.json')
OUT_COUNTRY = os.path.join(DATA, 'dims_country.json')

MODEL_RE = re.compile(r'\b(ST[CIH]-\d{2,5}[A-Z0-9]*(?:-[0-9A-Z]+)*)\b')
PRICE_RE = re.compile(r'(?:(?:US\$|USD|usd|Usd|\$)\s?(\d{2,5}(?:\.\d{1,2})?))|(?:(\d{2,5}(?:\.\d{1,2})?)\s?(?:usd|USD|Usd|US\$|\$|dollars?))')
SUBJ_PREFIX = re.compile(r'^\s*((re|fw|fwd|aw|wg|sv|vs|tr|r|回复|转发)\s*:\s*)+', re.I)
BOUNCE_FROM = re.compile(r'mailer-daemon|postmaster|mail delivery|maildelivery', re.I)
BOUNCE_SUBJ = re.compile(r'delivery status|undeliver|failure notice|returned mail|delivery failure|mail delivery failed|could not be delivered|não entregue|nicht zugestellt', re.I)
AUTO_SUBJ = re.compile(r'automatic reply|auto.?reply|out of office|autoreply|abwesenheit|absence|自动回复|ooo:|away from|on vacation|annual leave|automatische antwort|réponse automatique|respuesta automática|otomatik yanıt|автоответ', re.I)
TITLE_RE = re.compile(r'\b(ceo|cto|coo|cfo|cio|founder|co-founder|owner|president|vice president|vp|director|managing director|general manager|manager|head of|lead|engineer|engineering|sales|purchas\w*|procurement|buyer|sourcing|account|business development|bdm|product|technical|technician|consultant|architect|specialist|coordinator|executive|supervisor|administrator|partner|proprietor|gerente|director comercial|ingeniero|responsable|geschäftsführer|einkauf|vertrieb|leiter|müdür|satın alma|satış|mühendis|директор|менеджер|руководитель|инженер|закуп\w*)\b', re.I)
REGARDS_RE = re.compile(r'(?im)^\s*(?:(?:(?:many |best )?thanks?(?: you)?(?:,? and| &)?\s+)?(?:with\s+)?(?:very\s+)?(?:best|kind|warm|my best)?\s*(?:regards|wishes|rgds)\b[^\n]{0,24}'
                        r'|(?:thank you|thanks|many thanks|cheers|sincerely|yours sincerely|yours faithfully|br|saludos|un saludo|cordialement|bien à vous|mit freundlichen grüßen|mit freundlichen grüssen|freundliche grüße|viele grüße|beste grüße|saygılarımla|saygılar|iyi çalışmalar|с уважением|cordiali saluti|distinti saluti|met vriendelijke groet|met vriendelijke groeten|pozdrawiam|z poważaniem|s pozdravem|üdvözlettel|atenciosamente|cumprimentos|med vänliga hälsningar|med vennlig hilsen|venlig hilsen|ystävällisin terveisin)[,.!]?)\s*$')
SUPPLIER_DOM = ('smartbyte', 'hrui', 'hohunet', 'sagatele', 'sagatelecom')
OUR_DOMAINS = ('sagatelecom', 'sagatele.com')
WEEKDAY_CN = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

# 国家 → 标准时区偏移（小时，不算夏令时；美国/加拿大按东部，俄罗斯按莫斯科，澳大利亚按悉尼）
TZ = {'US': -5, 'CA': -5, 'MX': -6, 'BR': -3, 'AR': -3, 'CL': -4, 'CO': -5, 'PE': -5, 'EC': -5, 'UY': -3, 'PA': -5, 'CR': -6, 'GT': -6, 'DO': -4, 'PR': -4,
      'GB': 0, 'IE': 0, 'PT': 0, 'IS': 0, 'ES': 1, 'FR': 1, 'DE': 1, 'NL': 1, 'BE': 1, 'LU': 1, 'IT': 1, 'CH': 1, 'AT': 1, 'PL': 1, 'CZ': 1, 'SK': 1,
      'HU': 1, 'SE': 1, 'NO': 1, 'DK': 1, 'HR': 1, 'SI': 1, 'RS': 1, 'BA': 1, 'MK': 1, 'AL': 1, 'ME': 1, 'MT': 1, 'RO': 2, 'BG': 2, 'GR': 2, 'FI': 2,
      'EE': 2, 'LV': 2, 'LT': 2, 'UA': 2, 'MD': 2, 'CY': 2, 'TR': 3, 'RU': 3, 'BY': 3, 'IL': 2, 'SA': 3, 'AE': 4, 'QA': 3, 'KW': 3, 'OM': 4, 'BH': 3,
      'IR': 3.5, 'IQ': 3, 'JO': 3, 'LB': 2, 'SY': 3, 'YE': 3, 'EG': 2, 'ZA': 2, 'NG': 1, 'KE': 3, 'TZ': 3, 'UG': 3, 'ET': 3, 'GH': 0, 'MA': 1, 'DZ': 1,
      'TN': 1, 'LY': 2, 'SD': 2, 'SN': 0, 'CI': 0, 'CM': 1, 'AO': 1, 'MZ': 2, 'ZW': 2, 'ZM': 2, 'BW': 2, 'NA': 2, 'MU': 4, 'IN': 5.5, 'PK': 5, 'BD': 6,
      'LK': 5.5, 'NP': 5.75, 'TH': 7, 'VN': 7, 'MY': 8, 'SG': 8, 'ID': 7, 'PH': 8, 'HK': 8, 'TW': 8, 'CN': 8, 'MO': 8, 'KR': 9, 'JP': 9, 'AU': 10,
      'NZ': 12, 'KZ': 5, 'UZ': 5, 'KG': 6, 'TJ': 5, 'TM': 5, 'GE': 4, 'AM': 4, 'AZ': 4, 'MN': 8, 'KH': 7, 'LA': 7, 'MM': 6.5, 'BN': 8, 'MV': 5, 'AF': 4.5}

# 近 120 天大假（对方国家）——只放日期确定或可标「约」的；用于「日历窗口」
HOLIDAYS = {
    'US': [('2026-11-26', '感恩节（周四–周日四天基本停摆）'), ('2026-12-24', '圣诞–元旦（12-24 → 01-04 多数公司半停）')],
    'CA': [('2026-12-24', '圣诞–元旦（12-24 → 01-04）')],
    'GB': [('2026-12-24', '圣诞–元旦（12-24 → 01-04；Boxing Day 12-28 补休）')],
    'IE': [('2026-12-24', '圣诞–元旦')], 'AU': [('2026-12-24', '圣诞–元旦 + 南半球暑假（多到 1 月中）')], 'NZ': [('2026-12-24', '圣诞–元旦 + 暑假到 1 月中')],
    'DE': [('2026-12-24', '圣诞–元旦（12-24 → 01-06，德国多数工厂整周停）')], 'AT': [('2026-12-24', '圣诞–元旦（到 01-06）')], 'CH': [('2026-12-24', '圣诞–元旦')],
    'NL': [('2026-12-24', '圣诞–元旦')], 'BE': [('2026-12-24', '圣诞–元旦')], 'FR': [('2026-12-24', '圣诞–元旦')], 'IT': [('2026-12-08', '圣母无染原罪瞻礼（长周末）'), ('2026-12-24', '圣诞–主显节（到 01-06）')],
    'ES': [('2026-12-08', '宪法日 + 圣母节长周末（12-06/12-08）'), ('2026-12-24', '圣诞–三王节（到 01-06）')], 'PT': [('2026-12-01', '独立日'), ('2026-12-24', '圣诞–元旦')],
    'PL': [('2026-11-11', '独立日'), ('2026-12-24', '圣诞–元旦')], 'CZ': [('2026-11-17', '自由民主日'), ('2026-12-24', '圣诞–元旦')], 'SK': [('2026-11-17', '自由民主日'), ('2026-12-24', '圣诞–元旦')],
    'HU': [('2026-12-24', '圣诞–元旦')], 'RO': [('2026-12-01', '国庆日'), ('2026-12-24', '圣诞–元旦')], 'BG': [('2026-12-24', '圣诞–元旦')], 'GR': [('2026-12-24', '圣诞–元旦')],
    'SE': [('2026-12-24', '圣诞–元旦')], 'NO': [('2026-12-24', '圣诞–元旦')], 'DK': [('2026-12-24', '圣诞–元旦')], 'FI': [('2026-12-06', '独立日'), ('2026-12-24', '圣诞–元旦')],
    'EE': [('2026-12-24', '圣诞–元旦')], 'LV': [('2026-11-18', '独立日'), ('2026-12-24', '圣诞–元旦')], 'LT': [('2026-12-24', '圣诞–元旦')], 'HR': [('2026-12-24', '圣诞–元旦')],
    'SI': [('2026-12-24', '圣诞–元旦')], 'RS': [('2027-01-01', '元旦 + 东正教圣诞 01-07（1 月上旬基本停）')], 'BA': [('2027-01-01', '元旦 + 东正教圣诞 01-07')],
    'UA': [('2026-12-24', '圣诞–元旦')], 'MD': [('2026-12-24', '圣诞–元旦')], 'CY': [('2026-12-24', '圣诞–元旦')], 'MT': [('2026-12-24', '圣诞–元旦')],
    'TR': [('2026-10-29', '共和国日（10-28 下午起放）'), ('2027-01-01', '元旦（1 天）')],
    'RU': [('2026-11-04', '民族统一日'), ('2027-01-01', '新年长假（01-01 → 01-10 整体停摆）')], 'BY': [('2027-01-01', '新年 + 东正教圣诞 01-07')],
    'KZ': [('2026-12-16', '独立日（12-16/17）'), ('2027-01-01', '新年')], 'GE': [('2027-01-01', '新年 + 东正教圣诞 01-07')], 'AM': [('2027-01-01', '新年 + 圣诞 01-06')],
    'IL': [('2026-12-04', '光明节（12-04 → 12-12，非全休）')],
    'SA': [('2027-02-08', '斋月（约 02-08 → 03-09）：工时缩短；开斋节约 03-10')], 'AE': [('2026-12-02', '国庆日（12-02/03）'), ('2027-02-08', '斋月（约 02-08 → 03-09）')],
    'QA': [('2026-12-18', '国庆日'), ('2027-02-08', '斋月（约 02-08 → 03-09）')], 'KW': [('2027-02-08', '斋月（约 02-08 → 03-09）；国庆 02-25/26')], 'OM': [('2026-11-18', '国庆日（11-18/19）'), ('2027-02-08', '斋月（约）')],
    'BH': [('2026-12-16', '国庆日'), ('2027-02-08', '斋月（约）')], 'JO': [('2027-02-08', '斋月（约）')], 'EG': [('2027-02-08', '斋月（约 02-08 → 03-09）')], 'IQ': [('2027-02-08', '斋月（约）')],
    'IR': [('2027-02-08', '斋月（约）'), ('2027-03-20', '诺鲁孜新年（03-20 → 04-02 全国停）')], 'PK': [('2027-02-08', '斋月（约）')], 'BD': [('2026-12-16', '胜利日'), ('2027-02-08', '斋月（约）')],
    'MA': [('2026-11-18', '独立日'), ('2027-02-08', '斋月（约）')], 'DZ': [('2027-02-08', '斋月（约）')], 'TN': [('2027-02-08', '斋月（约）')],
    'MY': [('2026-12-25', '圣诞'), ('2027-02-06', '农历新年（02-06/07）'), ('2027-02-08', '斋月（约）')], 'ID': [('2026-12-25', '圣诞–元旦'), ('2027-02-08', '斋月（约）')],
    'SG': [('2026-12-25', '圣诞'), ('2027-02-06', '农历新年（02-06/07）')], 'HK': [('2026-12-25', '圣诞'), ('2027-02-06', '农历新年（02-06 → 02-09）')], 'TW': [('2027-02-05', '农历新年（02-05 → 02-11）')],
    'VN': [('2027-02-06', '春节 Tết（约 02-05 → 02-11）')], 'KR': [('2026-12-25', '圣诞'), ('2027-02-06', '설날（02-06 → 02-08）')], 'JP': [('2026-12-29', '年末年始（12-29 → 01-04）')],
    'TH': [('2026-12-05', '国王诞辰'), ('2026-12-31', '新年（12-31 → 01-02）')], 'PH': [('2026-12-24', '圣诞–元旦（12-24 → 01-02）')],
    'IN': [('2026-11-08', '排灯节 Diwali（11-08 前后一周生意半停）'), ('2026-12-25', '圣诞')], 'LK': [('2026-12-25', '圣诞')], 'NP': [('2026-11-08', 'Tihar（约 11-07 → 11-11）')],
    'ZA': [('2026-12-16', '和解日 + 圣诞–元旦（12-16 → 01-10 很多公司停）')], 'NG': [('2026-12-25', '圣诞–元旦')], 'KE': [('2026-12-12', 'Jamhuri Day'), ('2026-12-25', '圣诞–元旦')],
    'GH': [('2026-12-25', '圣诞–元旦')], 'ET': [('2027-01-07', '埃塞俄比亚圣诞')],
    'MX': [('2026-11-02', '亡灵节'), ('2026-12-12', '瓜达卢佩圣母节 → 圣诞–元旦（12-12 → 01-06 Guadalupe-Reyes）')], 'BR': [('2026-11-15', '共和国日'), ('2026-12-24', '圣诞–元旦')],
    'AR': [('2026-12-24', '圣诞–元旦 + 南半球暑假')], 'CL': [('2026-12-24', '圣诞–元旦 + 暑假')], 'CO': [('2026-12-08', '圣母节 → 圣诞–元旦')], 'PE': [('2026-12-08', '圣母节 → 圣诞–元旦')],
}
CNY_NOTE = '我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。'

# 型号 → 品类
def model_cat(m):
    m = m.upper()
    if m.startswith('STH'):
        return 'CENTEC 数据中心'
    if 'XG' in m or '10G' in m:
        core = '10G'
    elif 'DG' in m:
        core = '2.5G'
    else:
        core = None
    if m.startswith('STI'):
        base = '工业'
    elif m.startswith('STC'):
        base = '商用'
    else:
        return None
    body = m.split('-', 1)[1] if '-' in m else ''
    managed = body.endswith('M') or body.endswith('M-2BT') or 'PM' in body or 'GM' in body or 'CM' in body
    poe = 'P' in body.replace('PM', 'P') or 'BT' in body
    parts = [base]
    if core:
        parts.append(core)
    parts.append('PoE' if poe else '非PoE')
    parts.append('管理型' if managed else '非管理')
    return ' '.join(parts)


CAT_SUGGEST = {  # 缺口品类 → 一款可报的型号（价格主表 / HRUI 里都有）
    '工业 PoE': ('STI-288GP', '8 口千兆 PoE+ 2 SFP 工业非管理'),
    '工业管理型': ('STI-288DGGPM', '8 口千兆 PoE+ 2 × 2.5G SFP 工业 L2+ 管理'),
    '10G 汇聚': ('STC-448XGGPM', '48 口千兆 PoE + 4 × 10G SFP+ L2+ 管理'),
    '商用 PoE 管理型': ('STC-424XGGPM-280W', '24 口千兆 PoE + 4 × 10G SFP+ L2+ 管理 280W'),
    '商用 PoE 非管理': ('STC-028GP', '8 口千兆 PoE + 2 上联非管理'),
    '光纤接入 / 媒体转换': ('STI-140GE', '1 光 4 电工业非管理'),
    '2.5G': ('STC-114XGDGP', '2.5G PoE（HRUI 线）'),
}


def norm_subj(s):
    return SUBJ_PREFIX.sub('', (s or '').strip()).strip().lower()


def is_reply_subj(s):
    return bool(SUBJ_PREFIX.match(s or ''))


def parse_dt(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)


def offset_min(date_raw):
    m = re.search(r'([+-])(\d{2})(\d{2})\s*(?:\([A-Z]+\))?\s*$', date_raw or '')
    if not m:
        return None
    v = int(m.group(2)) * 60 + int(m.group(3))
    return v if m.group(1) == '+' else -v


def load_prices():
    """Saga 型号 → {'p20','p25','p30','list'}（价格主表 + HRUI 表）。"""
    tbl = {}
    for fn, mcol, lcol in (('价格主表.csv', 'Saga对应型号', 'Saga列表价USD'), ('价格主表_HRUI.csv', 'Saga对应型号', 'Saga列表价USD')):
        p = os.path.join(ROOT, 'data', fn)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p, encoding='utf-8-sig')):
            m = (r.get(mcol) or '').strip().upper()
            if not m or not m.startswith('ST'):
                continue
            def f(k):
                try:
                    return float(r.get(k) or '')
                except ValueError:
                    return None
            rec = {'p20': f('USD@+20%'), 'p25': f('USD@+25%'), 'p30': f('USD@+30%'), 'list': f(lcol)}
            if m not in tbl or (rec['p25'] and (tbl[m].get('p25') or 0) > rec['p25']):
                tbl[m] = rec   # 同型号多行取低价（主表 ㉕：不高于 2026-06 列表价）
    return tbl


def today_price(tbl, model, tier):
    rec = tbl.get(model.upper())
    if not rec:
        return None
    p = rec.get(f'p{tier}') if tier in (20, 25, 30) else rec.get('p25')
    if p is None:
        return None
    if rec.get('list') and rec['list'] < p:
        p = rec['list']
    return round(p, 1)


def main():
    args = sys.argv[1:]
    only = set(args[args.index('--codes') + 1].split(',')) if '--codes' in args else None
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    AB = {e['code']: e for e in ents if e['grade'] in 'AB'}
    research = {}
    for p in glob.glob(os.path.join(DATA, 'research', '*.json')):
        try:
            j = json.load(open(p, encoding='utf-8'))
            research[j['code']] = j
        except Exception:
            pass
    digest = json.load(open(os.path.join(DATA, 'site_digest.json'), encoding='utf-8')) if os.path.exists(os.path.join(DATA, 'site_digest.json')) else {}
    ghp = json.load(open(os.path.join(DATA, 'github_presence.json'), encoding='utf-8')) if os.path.exists(os.path.join(DATA, 'github_presence.json')) else {}
    prices = load_prices()
    qh_by_code = defaultdict(list)                              # S 箱报价史（含个性化群发里的价）
    qh_csv = os.path.join(ROOT, 'data', 'gmail_s', '报价史.csv')
    if os.path.exists(qh_csv):
        qh_rows = list(csv.DictReader(open(qh_csv, encoding='utf-8-sig')))
        sent_cnt = Counter(r.get('价格所在句') or '' for r in qh_rows)
        for r in qh_rows:
            code0 = (r.get('客户编号') or '').strip()
            if not code0:
                continue
            try:
                price = float(r.get('价格USD') or '')
            except ValueError:
                continue
            if not (8 <= price <= 20000):
                continue
            sentence = (r.get('价格所在句') or '').strip()
            mdls = [x.upper() for x in (r.get('型号(正文出现)') or '').split() if MODEL_RE.match(x)]
            qh_by_code[code0].append({'date': r.get('日期') or '', 'models': mdls, 'price': price, 'k': r.get('消息key') or '', 'subj': (r.get('主题') or '')[:50],
                                      'desc': re.sub(r'\s+', ' ', sentence)[:70], 'kind': '群发价' if sent_cnt[sentence] >= 5 else '1:1', 'mb': 'S'})
    bought_by_code = {}
    pcsv = os.path.join(ROOT, 'data', 'pi_orders', '成单客户汇总.csv')
    if os.path.exists(pcsv):
        for r in csv.DictReader(open(pcsv, encoding='utf-8-sig')):
            c = (r.get('客户名单编号') or '').strip()
            if c:
                bought_by_code.setdefault(c, []).extend([m.strip().upper() for m in re.split(r'[、,;/ ]+', r.get('Saga型号集合') or '') if m.strip()])
    excl = set()
    for p in glob.glob(os.path.join(DATA, '群发剔除名单_*.csv')):
        for r in csv.DictReader(open(p, encoding='utf-8-sig')):
            c = (r.get('客户编号') or r.get('编号') or '').strip()
            if c:
                excl.add(c)

    # ---------- 邮箱索引 ----------
    per = defaultdict(list)           # code → msgs
    tmpl_recips = {'S': defaultdict(set), 'A': defaultdict(set)}
    raw = {'S': [], 'A': []}
    for mb in ('S', 'A'):
        base = os.path.join(ROOT, 'data', 'gmail_s' if mb == 'S' else 'gmail_a', 'messages')
        for f in sorted(glob.glob(os.path.join(base, '*', '*.jsonl'))):
            for line in open(f, encoding='utf-8'):
                d = json.loads(line)
                if d.get('dir') == 'out':
                    for t in d.get('to') or []:
                        tmpl_recips[mb][norm_subj(d.get('subj'))].add((t.get('e') or '').lower())
                cl = [c for c in (d.get('client') or []) if c in AB]
                if not cl:
                    continue
                raw[mb].append((d, cl))
    tmpl = {mb: {s for s, r in v.items() if len(r) >= 20} for mb, v in tmpl_recips.items()}
    for mb in ('S', 'A'):
        for d, cl in raw[mb]:
            subj = d.get('subj') or ''
            ns = norm_subj(subj)
            fe = ((d.get('from') or {}).get('e') or '').lower()
            fn = ((d.get('from') or {}).get('n') or '').strip()
            bounce = d['dir'] == 'in' and (bool(BOUNCE_FROM.search(fe)) or bool(BOUNCE_SUBJ.search(subj)))
            auto = d['dir'] == 'in' and bool(AUTO_SUBJ.search(subj))
            mass = d['dir'] == 'out' and ns in tmpl[mb] and not is_reply_subj(subj)
            rec = {'mb': mb, 'dir': d['dir'], 'dt': parse_dt(d['date']), 'off': offset_min(d.get('date_raw')), 'fe': fe, 'fn': fn,
                   'subj': subj, 'ns': ns, 'labels': d.get('labels') or [], 'bulk': bool(d.get('bulk')), 'bounce': bounce, 'auto': auto,
                   'mass': mass, 'thr': d.get('thr'), 'k': d.get('k'), 'text': (d.get('text') or '') if (d['dir'] == 'in' or not mass) else '',
                   'to': [(t.get('e') or '').lower() for t in (d.get('to') or [])], 'cc': [(t.get('e') or '').lower() for t in (d.get('cc') or [])],
                   'clients': cl}
            rec['human_in'] = d['dir'] == 'in' and not rec['bulk'] and not bounce and not auto and not any(x in fe for x in OUR_DOMAINS)
            for c in cl:
                per[c].append(rec)
    raw = None

    # ---------- 国家级统计：群发打开窗口 / 来询季节 ----------
    win = defaultdict(lambda: defaultdict(lambda: [0, 0]))   # iso → (wd, block) → [sent, opened]
    season = defaultdict(Counter)                              # iso → month → human inbound
    season_n = Counter()
    season_seen = set()
    bounce_days = defaultdict(set)
    for c, ms in per.items():
        for m in ms:
            if m['bounce']:
                bounce_days[c].add(m['dt'].date())
    for c, ms in per.items():
        iso = AB[c].get('iso') or '??'
        off = TZ.get(iso)
        for m in ms:
            if m['dir'] == 'out' and m['mass'] and off is not None:
                if any(abs((m['dt'].date() - bd).days) <= 1 for bd in bounce_days.get(c, ())):
                    continue
                loc = m['dt'] + timedelta(hours=off)
                key = (loc.weekday(), (loc.hour // 2) * 2)
                win[iso][key][0] += 1
                if 'Opened' in m['labels']:
                    win[iso][key][1] += 1
            if m['human_in']:
                sk = (iso, c, m['dt'].year, m['dt'].month)
                if sk not in season_seen:                       # 同一户同一个月只算一次，免得一个话痨客户把全国曲线带歪
                    season_seen.add(sk)
                    season[iso][m['dt'].month] += 1
                    season_n[iso] += 1
    country = {}
    for iso, cells in win.items():
        sent = sum(v[0] for v in cells.values())
        opened = sum(v[1] for v in cells.values())
        if sent < 300:
            continue
        avg = opened / sent
        best = sorted(((v[1] / v[0], v[0], k) for k, v in cells.items() if v[0] >= 40 and k[0] < 5), reverse=True)[:3]
        bestk = {k for _, _, k in best}
        worst = sorted(((v[1] / v[0], v[0], k) for k, v in cells.items() if v[0] >= 40 and k[0] < 5 and k not in bestk))[:2]
        country[iso] = {'sent': sent, 'opened': opened, 'avg': round(avg * 100, 1),
                        'best': [{'wd': k[0], 'h': k[1], 'rate': round(r * 100, 1), 'n': n} for r, n, k in best],
                        'worst': [{'wd': k[0], 'h': k[1], 'rate': round(r * 100, 1), 'n': n} for r, n, k in worst]}
    seasons = {}
    for iso, cnt in season.items():
        if season_n[iso] >= 15:                                 # 按「户·月」去重后的样本；<30 的在文档里标「样本小」
            top = cnt.most_common(3)
            seasons[iso] = {'n': season_n[iso], 'top': [{'m': m, 'n': n, 'pct': round(n * 100 / season_n[iso], 1)} for m, n in top],
                            'by_month': {str(m): cnt.get(m, 0) for m in range(1, 13)}}
    json.dump({'generated_at': TODAY_S, 'send_window': country, 'season': seasons, 'tz': TZ}, open(OUT_COUNTRY, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # ---------- 关联：人名 / 电话 ----------
    by_person = defaultdict(set)
    by_phone = defaultdict(set)
    for c, e in AB.items():
        for p in e.get('persons') or []:
            nm = re.split(r'[/（(,|;]', p)[0].strip().lower()
            nm = re.sub(r'\s+', ' ', nm)
            if len(nm) >= 6 and ' ' in nm and not any(w in nm for w in ('info', 'sales', 'team', 'office', 'support')):
                by_person[nm].add(c)
        for k in e.get('merge_keys') or []:
            if k.startswith('p:') and len(k) >= 9:
                by_phone[k].add(c)

    # ---------- 逐户 ----------
    dims = {}
    codes = [c for c in AB if (not only or c in only)]
    for c in codes:
        e = AB[c]
        ms = sorted(per.get(c, []), key=lambda m: m['dt'])
        rs = research.get(c) or {}
        mr = rs.get('mail_review') or {}
        tier = None
        for src in ((mr.get('saga_now') or {}), (rs.get('saga_fit') or {})):
            t = src.get('tier')
            if isinstance(t, int) and t in (20, 25, 30):
                tier = t
                break
        d = {'code': c, 'generated_at': TODAY_S}
        iso = e.get('iso') or '??'
        # 1. 时机与节律
        hin = [m for m in ms if m['human_in']]
        if hin:
            loc_hours, wds, months = [], Counter(), Counter()
            for m in hin:
                months[m['dt'].month] += 1
                # 邮件头的时区常被 M365 归一成 +0000，不可信；优先按国家标准时，只有国家不在表里才退回邮件头
                off = (TZ[iso] * 60) if iso in TZ else (m['off'] if m['off'] else 0)
                loc = m['dt'] + timedelta(minutes=off)
                loc_hours.append(loc.hour + loc.minute / 60)
                wds[loc.weekday()] += 1
            t = {'n': len(hin), 'first': hin[0]['dt'].date().isoformat(), 'last': hin[-1]['dt'].date().isoformat(),
                 'months_top': [(m, n) for m, n in months.most_common(3) if n >= 2],
                 'weekdays': [(WEEKDAY_CN[w], n) for w, n in wds.most_common(3)],
                 'weekend_share': round(100 * sum(n for w, n in wds.items() if w >= 5) / len(hin)),
                 'local_hour_median': round(statistics.median(loc_hours), 1) if loc_hours else None,
                 'local_hour_iqr': (round(sorted(loc_hours)[len(loc_hours) // 4], 1), round(sorted(loc_hours)[(3 * len(loc_hours)) // 4], 1)) if len(loc_hours) >= 4 else None,
                 'off_seen': sorted({m['off'] for m in hin if m['off'] is not None})}
            # 回信时延（同线程，上一封是我方）
            their, ours, unanswered = [], [], 0
            by_thr = defaultdict(list)
            for m in ms:
                by_thr[(m['mb'], m['thr'])].append(m)
            for thr_ms in by_thr.values():
                thr_ms.sort(key=lambda m: m['dt'])
                for i, m in enumerate(thr_ms):
                    if m['human_in']:
                        prev_out = next((p for p in reversed(thr_ms[:i]) if p['dir'] == 'out'), None)
                        if prev_out:
                            their.append((m['dt'] - prev_out['dt']).total_seconds() / 3600)
                        nxt_out = next((p for p in thr_ms[i + 1:] if p['dir'] == 'out' and not p['mass']), None)
                        if nxt_out:
                            ours.append((nxt_out['dt'] - m['dt']).total_seconds() / 3600)
                        elif not any(p['dir'] == 'out' for p in thr_ms[i + 1:]):
                            unanswered += 1
            if their:
                t['their_reply_h_median'] = round(statistics.median(their), 1)
                t['their_reply_n'] = len(their)
                t['their_reply_fast_share'] = round(100 * sum(1 for h in their if h <= 24) / len(their))
            if ours:
                t['our_reply_h_median'] = round(statistics.median(ours), 1)
                t['our_reply_n'] = len(ours)
                t['our_reply_slow'] = sum(1 for h in ours if h > 72)
            t['unanswered_in'] = unanswered
            d['timing'] = t
        cw = country.get(iso)
        if cw:
            d['country_window'] = {'iso': iso, 'sent': cw['sent'], 'avg': cw['avg'], 'best': cw['best'][:2]}
        if iso in seasons and len(hin) < 3:
            d['country_season'] = {'iso': iso, 'n': seasons[iso]['n'], 'top': seasons[iso]['top']}
        # 2. 打开偏好
        mass_out = [m for m in ms if m['dir'] == 'out' and m['mass']]
        if mass_out:
            bd = bounce_days.get(c, set())
            valid = [m for m in mass_out if not any(abs((m['dt'].date() - x).days) <= 1 for x in bd)]
            opened = [m for m in valid if 'Opened' in m['labels']]
            op_subj = Counter(m['subj'] for m in opened)
            all_subj = Counter(m['subj'] for m in valid)
            never = [s for s, n in all_subj.most_common() if s not in op_subj][:4]
            o = {'sent': len(mass_out), 'valid': len(valid), 'opened': len(opened), 'opened_12m': sum(1 for m in opened if (datetime.now(timezone.utc) - m['dt']).days <= 365),
                 'opened_subjects': [(s, n, max(m['dt'] for m in opened if m['subj'] == s).date().isoformat()) for s, n in op_subj.most_common(4)],
                 'never_opened': never, 'last_opened': max((m['dt'] for m in opened), default=None),
                 'first_sent': valid[0]['dt'].date().isoformat() if valid else None, 'last_sent': valid[-1]['dt'].date().isoformat() if valid else None,
                 'bounce_days': len(bd)}
            if o['last_opened']:
                o['last_opened'] = o['last_opened'].date().isoformat()
            d['opens'] = o
        # 3. 报价轨迹（1:1 去信里型号 + 价同句）
        quotes = []
        for m in ms:
            if m['dir'] != 'out' or m['mass'] or not m['text']:
                continue
            txt = m['text'].split('\nOn ')[0]
            for line in re.split(r'[\n;。]', txt):
                models = list(dict.fromkeys(MODEL_RE.findall(line)))
                pr = [float(a or b) for a, b in PRICE_RE.findall(line)]
                pr = [p for p in pr if 8 <= p <= 20000]
                if models and pr:
                    pairs = list(zip(models, pr)) if len(models) == len(pr) else [(models[0], pr[0])]
                    for mdl, price in pairs:
                        quotes.append({'date': m['dt'].date().isoformat(), 'model': mdl.upper(), 'price': price, 'mb': m['mb'], 'k': m['k'], 'subj': m['subj'][:50]})
        for q in quotes:
            q['kind'] = '1:1'
            q['desc'] = ''
        # 报价史（S 箱）：型号列可能列了正文里所有型号，按「与今日档价最接近且在 ±40% 内」挑一个，挑不到就只留描述
        for r in qh_by_code.get(c, []):
            mdl = None
            cands = []
            for x in r['models']:
                ref = today_price(prices, x, 25)
                if ref:
                    cands.append((abs(ref - r['price']) / ref, x))
            if cands:
                ratio, x = min(cands)
                if ratio <= 0.4:
                    mdl = x
            quotes.append({'date': r['date'], 'model': mdl or '', 'desc': r['desc'], 'price': r['price'], 'mb': 'S', 'k': r['k'], 'subj': r['subj'], 'kind': r['kind']})
        # 去重：同日同型号/描述同价
        seen = set()
        q2 = []
        for q in quotes:
            key = (q['date'], q['model'] or q['desc'][:40], q['price'])
            if key not in seen:
                seen.add(key)
                q2.append(q)
        if q2:
            latest = {}
            for q in sorted(q2, key=lambda x: x['date']):
                latest[q['model'] or q['desc'][:40]] = q
            rows = []
            for _, q in sorted(latest.items(), key=lambda x: x[1]['date'], reverse=True)[:8]:
                row = dict(q)
                row['today'] = today_price(prices, q['model'], tier or 25) if q['model'] else None
                row['tier_used'] = tier or 25
                if row['today']:
                    row['delta_pct'] = round((row['today'] - q['price']) * 100 / q['price'])
                rows.append(row)
            n11 = sum(1 for q in q2 if q['kind'] == '1:1')
            d['quotes'] = {'n': len(q2), 'n_1to1': n11, 'n_mass': len(q2) - n11, 'first': min(q['date'] for q in q2), 'last': max(q['date'] for q in q2),
                           'last_1to1': max((q['date'] for q in q2 if q['kind'] == '1:1'), default=None), 'rows': rows, 'tier_known': tier is not None}
        # 4. 品类覆盖与缺口
        shown = Counter()
        for q in q2:
            cat = model_cat(q['model']) if q['model'] else None
            if cat:
                shown[cat] += 1
        bought = [m for m in dict.fromkeys(bought_by_code.get(c, [])) if MODEL_RE.match(m)]
        for mdl in bought:
            cat = model_cat(mdl)
            if cat:
                shown[cat] += 1
        opened_cats = set()
        for s, n, _dt in (d.get('opens') or {}).get('opened_subjects') or []:
            sl = s.lower()
            if 'industrial' in sl:
                opened_cats.add('工业')
            if 'poe' in sl:
                opened_cats.add('PoE')
            if '10g' in sl or 'sfp' in sl or 'fiber' in sl or 'aggregation' in sl:
                opened_cats.add('10G 汇聚')
            if 'l3' in sl or 'layer 3' in sl:
                opened_cats.add('L3')
            if '2.5g' in sl:
                opened_cats.add('2.5G')
        dg = digest.get(c) or {}
        kw = dg.get('kw') or {}
        interest = []
        if (kw.get('industrial', 0) + kw.get('automation', 0)) >= 10:
            interest.append(('工业', f"industrial {kw.get('industrial', 0)} / automation {kw.get('automation', 0)}"))
        if (kw.get('cctv', 0) + kw.get('camera', 0)) >= 10 and kw.get('poe', 0) >= 5:
            interest.append(('安防 PoE', f"cctv {kw.get('cctv', 0)} / camera {kw.get('camera', 0)} / poe {kw.get('poe', 0)}"))
        if kw.get('10g', 0) >= 5:
            interest.append(('10G 汇聚', f"10g {kw.get('10g', 0)} / sfp {kw.get('sfp', 0)}"))
        if kw.get('media converter', 0) >= 10:
            interest.append(('光纤接入 / 媒体转换', f"media converter {kw.get('media converter', 0)} / fiber {kw.get('fiber', 0) + kw.get('fibre', 0)}"))
        hold_now = (mr.get('next_move') or {}).get('when') in ('不动', '仅被动', '被动') or c in excl
        if interest and not hold_now:
            shown_txt = ' '.join(shown)
            gaps = []
            for cat, ev in interest:
                covered = False
                if cat == '工业' and ('工业' in shown_txt or '工业' in opened_cats):
                    covered = True
                if cat == '安防 PoE' and ('PoE 管理型' in shown_txt or 'PoE 非管理' in shown_txt or 'PoE' in opened_cats):
                    covered = True
                if cat == '10G 汇聚' and ('10G' in shown_txt or '10G 汇聚' in opened_cats):
                    covered = True
                if cat == '光纤接入 / 媒体转换' and ('非PoE 非管理' in shown_txt and '工业' in shown_txt):
                    covered = True
                if not covered:
                    key = {'工业': '工业 PoE', '安防 PoE': '商用 PoE 管理型', '10G 汇聚': '10G 汇聚', '光纤接入 / 媒体转换': '光纤接入 / 媒体转换'}[cat]
                    mdl, desc = CAT_SUGGEST[key]
                    gaps.append({'cat': cat, 'evidence': ev, 'model': mdl, 'desc': desc, 'price': today_price(prices, mdl, tier or 25)})
            d['coverage'] = {'interest': interest, 'shown': dict(shown), 'bought': bought, 'opened_cats': sorted(opened_cats), 'gaps': gaps[:2]}
        # 5. 规模与贴牌线索
        if dg and dg.get('status') == 'ok':
            models = dg.get('models') or []
            sld = ((e.get('domains') or [''])[0] or '').split('.')[0].lower()
            words = [w for w in re.split(r'[^A-Za-z]+', e.get('name') or '') if w]
            initials = ''.join(w[0] for w in words[:3]).lower() if len(words) >= 2 else ''
            own = []
            for m in models:
                pre = re.match(r'([A-Za-z]{2,6})', m)
                if not pre:
                    continue
                p = pre.group(1).lower()
                if (len(sld) >= 4 and sld.startswith(p) and len(p) >= 3) or (initials and p == initials) or (len(p) >= 4 and p in sld):
                    own.append(m)
            social = [s for s in (dg.get('social') or []) if isinstance(s, str)]
            s5 = {'sitemap': dg.get('sitemap_count'), 'brands': (dg.get('brands') or [])[:6] if isinstance(dg.get('brands'), list) else list(dg.get('brands') or {})[:6],
                  'brands_n': len(dg.get('brands') or []), 'lang': dg.get('lang'), 'models_n': len(models), 'own_label': own[:5], 'social': social[:4],
                  'fetched': (dg.get('fetched_at') or '')[:10]}
            if s5['sitemap'] or s5['brands_n'] or own or social:
                d['scale'] = s5
        # 6. 关联户
        rel = Counter()
        why = defaultdict(set)
        for m in ms:
            for oc in m['clients']:
                if oc != c:
                    rel[oc] += 1
                    why[oc].add('同一封邮件')
        for p, cs in by_person.items():
            if c in cs:
                for oc in cs:
                    if oc != c:
                        rel[oc] += 1
                        why[oc].add(f'同人名「{p}」')
        for p, cs in by_phone.items():
            if c in cs:
                for oc in cs:
                    if oc != c:
                        rel[oc] += 1
                        why[oc].add('同电话')
        if rel:
            d['related'] = [{'code': oc, 'name': AB[oc]['name'] if oc in AB else oc, 'grade': AB[oc]['grade'] if oc in AB else '?', 'why': sorted(why[oc]), 'n': n}
                            for oc, n in rel.most_common(5)]
        # 7. 写信的人（签名）
        people = {}
        for m in hin:
            if not m['fe'] or not m['text'] or any(x in m['fe'] for x in SUPPLIER_DOM):
                continue
            rec = people.setdefault(m['fe'], {'email': m['fe'], 'names': Counter(), 'titles': Counter(), 'n': 0, 'first': m['dt'].date().isoformat(), 'last': m['dt'].date().isoformat(), 'mb': set()})
            rec['n'] += 1
            rec['last'] = m['dt'].date().isoformat()
            rec['mb'].add(m['mb'])
            fn0 = re.split(r'\s*[|｜]\s*', m['fn'] or '')[0].strip()[:40]   # 「Au Wai Choon | R ~Nets」只留人名
            if fn0 and '@' not in fn0:
                rec['names'][fn0] += 1
            txt = m['text'][:6000]
            for rm in REGARDS_RE.finditer(txt):
                tail = [ln.strip(' \t*_-|>') for ln in txt[rm.end():].split('\n')]
                tail = [ln for ln in tail if ln and not REGARDS_RE.match(ln + '\n') and not re.fullmatch(r'(?i)(best regards|kind regards|regards|thanks|thank you|br|cheers),?', ln)][:6]
                if not tail:
                    continue
                cand_name = tail[0]
                if re.search(r'(?i)regards|thanks|thank you|wishes|cheers|sincerely|salut|grü|gruss|saygı|cordial|pozdraw|uважением|уважением|best$', cand_name):
                    continue
                if 2 <= len(cand_name.split()) <= 4 and len(cand_name) <= 40 and not re.search(r'\d|@|http|www\.', cand_name) and not TITLE_RE.search(cand_name):
                    rec['names'][cand_name] += 2
                    for ln in tail[1:4]:
                        if TITLE_RE.search(ln) and len(ln) <= 70 and '@' not in ln and 'http' not in ln and not re.search(r'\+?\d[\d\s().-]{6,}', ln):
                            rec['titles'][ln] += 1
                            break
                elif TITLE_RE.search(cand_name) and len(cand_name) <= 70 and ' | ' in cand_name:
                    nm, _, tt = cand_name.partition(' | ')
                    rec['names'][nm.strip()] += 1
                    rec['titles'][tt.strip()] += 1
                break
        if people:
            d['people'] = [{'email': p['email'], 'name': (p['names'].most_common(1) or [('', 0)])[0][0], 'title': re.sub(r'[*|\xa0]+', ' ', (p['titles'].most_common(1) or [('', 0)])[0][0]).strip(' .'),
                            'n': p['n'], 'first': p['first'], 'last': p['last'], 'mb': ''.join(sorted(p['mb']))}
                           for p in sorted(people.values(), key=lambda x: (-x['n'], x['last']))[:5]]
        # 8. GitHub
        g = ghp.get(c)
        if g and g.get('accounts'):                             # 只用账号命中；repos_mentioning 多为同名词噪音，留在 github_presence.json 里不上 MD
            d['github'] = {'accounts': g.get('accounts') or [], 'repos_mentioning_n': len(g.get('repos_mentioning') or []), 'checked_at': g.get('checked_at')}
        # 9. 日历窗口
        hol = [(dd, nm) for dd, nm in HOLIDAYS.get(iso, []) if 0 <= (date.fromisoformat(dd) - TODAY).days <= 120]
        d['calendar'] = {'holidays': hol, 'cny': CNY_NOTE, 'tz': TZ.get(iso)}
        # 热度
        last_in = date.fromisoformat(d['timing']['last']) if d.get('timing') else None
        rec_days = (TODAY - last_in).days if last_in else None
        heat = 0
        why_heat = []
        if rec_days is not None:
            f = 1 if rec_days <= 90 else 0.6 if rec_days <= 365 else 0.3 if rec_days <= 730 else 0.1
            heat += 40 * f
            why_heat.append(f'最近真人来信 {last_in}（{rec_days} 天前）')
        n_rep = (d.get('timing') or {}).get('their_reply_n', 0)
        if n_rep:
            heat += 15 * min(n_rep, 4) / 4
            why_heat.append(f'回过我方 {n_rep} 次')
        op12 = (d.get('opens') or {}).get('opened_12m', 0)
        if op12:
            heat += 15 * min(op12, 5) / 5
            why_heat.append(f'近 12 个月打开群发 {op12} 次')
        if e.get('pi'):
            heat += 20
            why_heat.append('成交过（PI）')
        if d.get('quotes') and d['quotes'].get('n_1to1'):
            heat += 10
            why_heat.append(f"1:1 报过价 {d['quotes']['n_1to1']} 次（最近 {d['quotes']['last_1to1']}）")
        d['heat'] = {'score': round(heat), 'why': why_heat, 'excluded': c in excl, 'hold': (mr.get('next_move') or {}).get('when') in ('不动', '仅被动', '被动')}
        dims[c] = d
    if only and os.path.exists(OUT):
        old = json.load(open(OUT, encoding='utf-8'))
        old.update(dims)
        dims_all = old
    else:
        dims_all = dims
    json.dump(dims_all, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'dims: {len(dims)} 户（文件共 {len(dims_all)}）→ {OUT}')
    if '--no-docs' not in args:
        write_docs(dims_all, AB, country, seasons)


def fmt_h(h):
    return f'{int(h):02d}:{int(round((h - int(h)) * 60)):02d}'


def write_docs(dims, AB, country, seasons):
    # 热度榜
    rows = sorted(dims.values(), key=lambda d: -d['heat']['score'])
    L = [f'# A/B 热度榜（数据推导 · {TODAY_S}）', '',
         '> 分数 = 最近真人来信（≤90 天 40 分 / ≤1 年 24 / ≤2 年 12 / 更早 4）+ 回过我方（每次 3.75，封顶 15）+ 近 12 个月打开群发（每次 3，封顶 15）+ 成交过 20 + 1:1 报过价 10。',
         '> 只是把邮箱里的行为排个序，供「这个月先碰谁」；绑定行 / 下一步仍以各户档案为准。剔除名单内或绑定行「不动 / 仅被动」的户单独标出。', '',
         '| # | 编号 | 客户 | 国家 | 级 | 分 | 依据 | 状态 |', '|---|---|---|---|---|---|---|---|']
    n = 0
    for d in rows:
        if d['heat']['score'] <= 0:
            continue
        c = d['code']
        e = AB[c]
        n += 1
        st = '剔除名单' if d['heat']['excluded'] else ('绑定行：不动/被动' if d['heat']['hold'] else '')
        L.append(f"| {n} | {c} | {e['name'][:36]} | {e['country']} | {e['grade']} | {d['heat']['score']} | {'；'.join(d['heat']['why'])} | {st} |")
        if n >= 120:
            break
    L += ['', f'共 {sum(1 for d in rows if d["heat"]["score"] > 0)} 户有行为分；0 分（从未有真人来信、未打开、未成交、未 1:1 报价）{sum(1 for d in rows if d["heat"]["score"] <= 0)} 户。']
    open(os.path.join(ROOT, 'docs', f'AB_热度榜_{TODAY_S}.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    # 各国窗口与季节
    cn = {}
    for e in AB.values():
        cn[e.get('iso') or '??'] = e.get('country')
    L = [f'# 各国发信窗口与来询季节（全库 S/A 邮箱统计 · {TODAY_S}）', '',
         '> **发信窗口**：把我们每封群发按收件人国家换算成对方本地时间（标准时，不含夏令时；美加按东部、俄罗斯按莫斯科），统计「Opened」标签比例（像素打开，退信前后一天的剔除；代理/安全网关会误触发，只看相对高低）。只列群发 ≥300 封的国家，单元格 ≥40 封。',
         '> **来询季节**：客户真人来信（去群发、退信、自动回复）按「户·月」去重后的月份分布（一个话痨客户只算一次），只列 ≥15 个户·月的国家；<30 的标「样本小」。', '',
         '## 发信窗口（对方本地时间）', '', '| 国家 | 群发封数 | 平均打开率 | 最高的两个时段 | 最低的两个时段 |', '|---|---|---|---|---|']
    for iso, cw in sorted(country.items(), key=lambda x: -x[1]['sent']):
        best = '；'.join(f"{WEEKDAY_CN[b['wd']]} {b['h']:02d}–{b['h'] + 2:02d} 点 {b['rate']}%（{b['n']} 封）" for b in cw['best'])
        worst = '；'.join(f"{WEEKDAY_CN[b['wd']]} {b['h']:02d}–{b['h'] + 2:02d} 点 {b['rate']}%（{b['n']} 封）" for b in cw['worst'])
        L.append(f"| {cn.get(iso, iso)}（{iso}） | {cw['sent']} | {cw['avg']}% | {best} | {worst} |")
    L += ['', '## 来询季节（真人来信按月）', '', '| 国家 | 来信封数 | 前三个月份 | 1–12 月分布 |', '|---|---|---|---|']
    for iso, s in sorted(seasons.items(), key=lambda x: -x[1]['n']):
        top = '；'.join(f"{t['m']} 月 {t['pct']}%（{t['n']}）" for t in s['top'])
        dist = ' '.join(f"{m}:{s['by_month'][str(m)]}" for m in range(1, 13))
        L.append(f"| {cn.get(iso, iso)}（{iso}） | {s['n']}{'（样本小）' if s['n'] < 30 else ''} | {top} | {dist} |")
    L += ['', '> 用法：给某国客户排发信日时，优先落在该国最高的时段；来询季节高的月份前两周，把该国 B 级的「下一步」往前挪。数据文件 `data/saga_clients/dims_country.json`。']
    open(os.path.join(ROOT, 'docs', f'各国发信窗口与来询季节_{TODAY_S}.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('docs written')


if __name__ == '__main__':
    main()
