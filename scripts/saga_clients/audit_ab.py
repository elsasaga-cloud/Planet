#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saga Clients · A/B 加厚审计（T29-U54「确保信息又多又对又好」）

三个维度，逐户机械核对，结果进库：
  多（证据量）：每户事实条数 / 有无来信事实 / 有无成交 / 有无 Elsa 触达口径 / 绑定行与下一步是否齐全；
  对（正确性）：信稿里的「型号 - $价」是否落在允许集合（SmartByte 档位价（㉕ 封顶）/ 列表价 / 群发现价 / 最近实报 / HRUI 三档 / CENTEC 锚价）、
               型号是否存在于价格表、开头句引用的「"主题" on 日期」是否能在事实里找到同日去信、Elsa 已见价与信稿价是否冲突、
               证书与国别是否配套、日期是否在未来、档位是否 20/25/30、P1 是否在描述表；
  好（可发性）：一封一问、英文稿不混其他语言、红线词（ERPS/CLI/watchdog/in stock/free sample/list price/Elsa …）、
               称呼名字在档案里能找到、渲染 MD 与 JSON 同步。

输出：
  docs/requirements/AB加厚审计_<日期>.md     —— 人读报告（汇总 + 逐条问题）
  data/saga_clients/audit_ab_<日期>.json      —— 机器读明细（供补丁脚本定位）
退出码 0 = 硬错误为 0；1 = 有硬错误。
"""
import datetime as dt
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, OUT_DIR, ROOT, RESEARCH_DIR  # noqa: E402
import render  # noqa: E402  (PRICES / HRUI_TIERS / ALT_PRICES / ELSA_LIVE_NOW / P1_EN / tier_price)

TODAY = dt.date.today().isoformat()
REPORT = os.path.join(ROOT, 'docs', 'requirements', f'AB加厚审计_{TODAY}.md')
DETAIL = os.path.join(DATA, f'audit_ab_{TODAY}.json')

MONTHS = {m: i for i, m in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 1)}

# 最近实报 / 活动价 / 列表外锚价（docs/reference/群发价台账 + 方法与进度 第 72–75 批口径）
REAL = {
    'STI-050GE': [17.0, 17.8, 18.5, 24.0, 25.0, 26.0], 'STI-080GE': [31.4, 32.5, 32.7, 34.0], 'STI-110GE': [26.5, 22.4, 23.4, 24.3],
    'STI-110FE': [19.7, 20.6, 21.4], 'STI-111GP': [27.8, 29.0, 30.1], 'STI-244GP': [35.0, 35.2, 36.6, 38.1], 'STI-280GE': [46.0, 46.6, 48.6, 50.5],
    'STI-288GP': [60.0, 57.4, 59.8, 62.2], 'STI-21616GP': [185.0, 170.4, 177.5, 184.6], 'STI-054GP': [32.5, 33.0, 31.2, 33.8],
    'STI-154GP': [36.0, 37.0, 38.0, 37.7, 39.2, 40.8], 'STI-288DGGPM': [137.5, 125.0], 'STI-288DGGPM-2BT': [154.0], 'STI-288GPM': [72.0, 78.9, 82.2, 85.5],
    'STC-424XGGPM-280W': [180.0, 170.0], 'STC-448XGGPM': [335.0, 300.0], 'STC-4168XGGCM': [280.0, 300.0, 392.4, 376.5],
    'STC-114XGDGP': [44.0], 'STC-18XGDGE': [50.1], 'STC-2016GP': [88.0], 'STC-2024GP': [93.5], 'STC-024GP': [22.3], 'STC-028GFP': [17.9, 17.6],
    'STC-05GE': [5.9, 6.2, 6.4], 'STC-08GE': [10.5], 'STC-624XGDGPM': [466.4], 'STC-028GP': [25.1, 26.2, 27.2, 24.2], 'STC-228GP': [33.2, 34.6, 35.9, 30.8],
    'STC-114GP': [17.0, 17.8, 18.5], 'STC-204GP': [24.2, 25.2, 26.2, 20.4], 'STC-2216GPM': [141.7, 147.6, 153.5, 137.5], 'STC-28GM': [56.5, 58.9, 61.2],
    'STC-28GPM': [71.0, 74.0, 77.0], 'STC-128GFP': [25.0],
    'STH-2C24XF-HSI': [1500.0], 'STH-32C-HSI': [6000.0], 'STH-8C48DX-HSI': [4800.0], 'STH-2C6QX-HSI': [1200.0], 'STH-32QC-HSI': [16000.0],
    'STH-2C24XF-SFI': [], 'STI-21616XGGPM': [322.6, 297.8, 310.2], 'STI-488XGGPM': [165.0, 171.9, 178.8, 178.7], 'STI-448DGGGM': [205.5],
    'STC-424XGGM': [127.4, 132.7, 138.0, 130.0], 'STI-488XGGBPM': [215.0], 'STI-21616GPM': [], 'STI-21616GPM-2BT': [], 'STC-110XGE': [65.0], 'STI-0160GE': [100.0, 105.0], 'STI-222GP': [33.0, 34.0], 'STC-424DGGPM-280W': [134.5, 140.1, 145.7, 150.0, 135.0], 'STC-28DGGPM': [80.7, 84.1, 87.4, 81.0],
}
BYPASS = {186.5, 194.3, 202.1}  # LT-IS6312GP-4GX8GT-FBP（无 Saga 型号）
TOL = 0.11

FORBIDDEN = re.compile(r'\bERPS\b|\bCLI\b|watchdog|in stock|free sample|list price|EXW list|\bElsa\b|UL compliant|trading company|NDAA[- ]compliant|'
                       r'E-mark report|LACP|SNMP ?v[23]|wall-mount|alarm relay|250 ?m\b', re.I)
# 已人工核过、允许保留的（档号 → 词）：客户自己的项目名 / 真实线程 / 客户要求的原厂名 / 固件 7.5 实证
ALLOW_FORBIDDEN = {
    'SB-093': {'watchdog'}, 'SA-013': set(), 'SB-473': {'CLI'}, 'SB-1336': {'CLI', 'SNMP v2', 'SNMP v3'}, 'SB-761': {'SNMP v3'}, 'SB-040': {'CLI'},
    'SA-091': {'CLI'}, 'SB-679': {'CLI'}, 'SB-1088': {'NDAA-compliant'}, 'SA-052': {'watchdog'},
    'SA-024': {'SNMPv3'},            # 复述客户 2025-01-16 标书原话（LACP/IPv6/Voice VLAN/SNMPv3/SSHv2）
    'SB-093': {'watchdog', '250 m'},  # 复述我方 2026-05-05 对 17 问的答复 + 2026-09-14 Alan 原话「PoE watchdog and 250-meter PoE」
    'SC-2186': {'CLI', 'SNMP v3'},    # CENTEC 核心机（Hohunet）CLI/SNMPv3 属实，红线只针对 Marvell/非管理线
}
MODEL_RE = re.compile(r'\b(ST[CIH]-[0-9A-Z]+(?:-[0-9A-Z]+)*)\b')
PRICE_RE = re.compile(r'(?:\$|USD)\s?([\d,]+(?:\.\d+)?)|([\d,]+(?:\.\d+)?)\s?USD')
OPENER_RE = re.compile(r'"([^"\n]{3,90})" on (\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})')
GREET_RE = re.compile(r'^\s*(?:Hi|Hello|Dear|Hola|Bonjour|Buongiorno|Merhaba|Hallo|Guten Tag|Здравствуйте|Sayın|Olá)\s*,?\s*(?:Mr\.?|Ms\.?|Mrs\.?|Herr|Frau)?\s*([^,，\n:—–-]{1,40})[,，:—–-]', re.M)
CERT_EXPECT = {  # iso → (必须出现之一, 不该出现)
    'US': ({'FCC'}, {'UKCA', 'EAC', 'KC', 'RCM', 'BIS'}), 'CA': ({'FCC'}, {'UKCA', 'EAC', 'KC', 'RCM', 'BIS'}),
    'GB': ({'UKCA'}, {'FCC', 'EAC', 'KC', 'RCM', 'BIS'}), 'UK': ({'UKCA'}, {'FCC', 'EAC', 'KC', 'RCM', 'BIS'}),
    'RU': ({'EAC'}, {'UKCA', 'KC', 'RCM', 'BIS'}), 'BY': ({'EAC'}, {'UKCA', 'KC', 'RCM', 'BIS'}), 'KZ': ({'EAC'}, {'UKCA', 'KC', 'RCM', 'BIS'}),
    'KR': ({'KC'}, {'UKCA', 'EAC', 'RCM', 'BIS'}), 'AU': ({'RCM'}, {'UKCA', 'EAC', 'KC', 'BIS'}), 'IN': ({'BIS'}, {'UKCA', 'EAC', 'KC', 'RCM'}),
}
EU_LIKE = {'DE', 'IT', 'FR', 'ES', 'PL', 'NL', 'BE', 'CZ', 'AT', 'SE', 'DK', 'FI', 'NO', 'CH', 'PT', 'IE', 'HU', 'RO', 'BG', 'GR', 'SK', 'SI', 'HR', 'LT', 'LV', 'EE', 'CY', 'LU', 'MT', 'IS', 'RS', 'TR'}
NONASCII_OK = set('’“”–—é·°×−…')
PRIVATE_SUBJ = ('WhatsApp', '私信', '模板', '触发', 'LinkedIn', 'Türkçe', '整段', '微信', 'WeChat')
EN_WORDS = {'the', 'and', 'you', 'for', 'we', 'a', 'to', 'of', 'in', 'is', 'on', 'with', 'your', 'our', 'one', 'question', 'this', 'that', 'it', 'at', 'from', 'which', 'are', 'or', 'an', 'as', 'be', 'if', 'not', 'have', 'has', 'was', 'will', 'can', 'do', 'but', 'by', 'us', 'so', 'no', 'what', 'would', 'there', 'still', 'just', 'only', 'same', 'last', 'most', 'mail', 'mails', 'price', 'switch', 'switches', 'port', 'ports', 'per', 'unit', 'units', 'days', 'day', 'working', 'regards', 'best', 'hello', 'hi', 'dear', 'thank', 'thanks', 'please', 'any', 'all', 'more', 'than', 'when', 'who', 'how', 'since', 'about', 'into', 'over', 'under', 'after', 'before', 'both', 'each', 'then', 'here', 'they', 'them', 'their', 'its', 'also', 'very', 'much', 'many', 'some', 'sent', 'send', 'answer', 'reply', 'write', 'wrote', 'asked', 'ask', 'need', 'use', 'model', 'models'}
SIGN_RE = re.compile(r'\n(?:Best regards|Regards|Kind regards|Thank you)[,.]?\s*\n+\s*([^\n]{1,40})\n')
CERT_LIST_OK = {'SA-067'}  # 供应商档案：列出我方持有的 FCC/UKCA 报告，不是对瑞典客户主张


QUOTE_CSV = os.path.join(ROOT, 'data', 'S邮箱_报价史_2026-10-22.csv')
RT_IND_MD = os.path.join(ROOT, 'docs', 'reference', '价格表_Realtek工业线_Saga对外_2025.md')
HOHUNET_CSV = os.path.join(ROOT, 'data', 'hohunet_STH对照表.csv')


def load_own_quotes():
    """收件域 → {型号 → {价}}（S 邮箱报价史 2023→2026，规则 ㉕ ①「自己报过的价优先」）。"""
    import csv
    out = defaultdict(lambda: defaultdict(set))
    if not os.path.exists(QUOTE_CSV):
        return out
    for r in csv.DictReader(open(QUOTE_CSV, encoding='utf-8-sig')):
        try:
            out[r['收件域'].strip().lower()][r['附近型号'].strip()].add(float(r['USD']))
        except (ValueError, KeyError):
            pass
    return out


def load_rt_ind():
    """Realtek 工业线 2025-04 Saga 对外列表价（文档表格 | 型号 | … | $价 |）。"""
    out = {}
    if not os.path.exists(RT_IND_MD):
        return out
    for line in open(RT_IND_MD, encoding='utf-8'):
        m = re.match(r'\|\s*(ST[CI]-[0-9A-Z-]+)\s*\|.*\$([\d.]+)\s*\|\s*$', line.strip())
        if m:
            out.setdefault(m.group(1), set()).add(float(m.group(2)))
    return out


def load_sth_models():
    """CENTEC（Hohunet）型号全集：对照表 + CENTEC 锚价文档 + 入库的 STH 规格书文本（gmail 附件 / Extra Info / suppliers_drive）。"""
    out = set()
    if os.path.exists(HOHUNET_CSV):
        import csv
        for r in csv.DictReader(open(HOHUNET_CSV, encoding='utf-8-sig')):
            k = (r.get('Saga型号') or '').strip()
            if k:
                out.add(k)
    srcs = [os.path.join(ROOT, 'docs', 'reference', 'CENTEC_产品表与报价锚_2026-10-24.md')]
    srcs += glob.glob(os.path.join(ROOT, 'data', 'extra_info_2026-10', 'text', '*STH*.json'))
    srcs += glob.glob(os.path.join(ROOT, 'data', 'gmail_a', 'attachments', 'text', '*.json'))
    srcs += glob.glob(os.path.join(ROOT, 'data', 'suppliers_drive', 'text', '*.json'))
    for fp in srcs:
        try:
            out |= set(re.findall(r'STH-[0-9A-Z]+(?:-[0-9A-Z]+)*', open(fp, encoding='utf-8', errors='ignore').read()))
        except OSError:
            pass
    return out


def load_out_index():
    """code → {(date, subject_lower)}：S/A 邮箱去信（gmail jsonl，client 标签）+ Elsa 群发命中（bcc_match_latest）。"""
    idx = defaultdict(set)
    for acct in ('gmail_s', 'gmail_a'):
        for fp in glob.glob(os.path.join(ROOT, 'data', acct, 'messages', '*', '*.jsonl')):
            for line in open(fp, encoding='utf-8'):
                try:
                    m = json.loads(line)
                except ValueError:
                    continue
                if m.get('dir') != 'out':
                    continue
                d_ = (m.get('date') or '')[:10]
                s_ = (m.get('subj') or '').strip().lower()
                for c in m.get('client') or []:
                    idx[c].add((d_, s_))
    fp = os.path.join(ROOT, 'data', 'gmail_e', 'bcc_match_latest.json')
    if os.path.exists(fp):
        for c, v in json.load(open(fp, encoding='utf-8')).items():
            for h in v.get('hits') or []:
                idx[c].add(((h.get('date') or '')[:10], (h.get('subject') or '').strip().lower()))
    return idx


OWN = load_own_quotes()
RT_IND = load_rt_ind()
STH_MODELS = load_sth_models()
OUT_IDX = load_out_index()


def allowed_prices(model, domains=()):
    out = set()
    r = render.PRICES.get(model)
    if r:
        for t in (20, 25, 30):
            v, _ = render.tier_price(r, t)
            try:
                out.add(float(v))
            except ValueError:
                pass
        try:
            if r.get('Saga列表价USD'):
                out.add(float(r['Saga列表价USD']))
        except ValueError:
            pass
    h = render.HRUI_TIERS.get(model)
    if h:
        out |= {h[20], h[25], h[30]}
        if h.get('list'):
            out.add(h['list'])
    a = render.ALT_PRICES.get(model)
    if a:
        try:
            out.add(float(a[0]))
        except ValueError:
            pass
    if model in render.ELSA_LIVE_NOW:
        out.add(float(render.ELSA_LIVE_NOW[model]))
    out |= set(REAL.get(model, []))
    out |= RT_IND.get(model, set())
    r3 = render.PRICES.get(model + '(L3)')
    if r3:
        for t in (20, 25, 30):
            v, _ = render.tier_price(r3, t)
            try:
                out.add(float(v))
            except ValueError:
                pass
    for dom in domains:
        out |= OWN.get(dom, {}).get(model, set())
    return out


def known_model(model):
    return bool(render.PRICES.get(model) or render.PRICES.get(model + '(L3)') or render.HRUI_TIERS.get(model) or render.ALT_PRICES.get(model) or model in REAL
                or model in render.P1_EN or model in RT_IND or model in STH_MODELS)


def pairs_in(text):
    """[(model, price_float, context)] —— 型号后 70 字符内的第一个 $ 数字（到下一个型号为止）。"""
    ms = list(MODEL_RE.finditer(text))
    out = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        seg = text[m.end():end]
        pm = PRICE_RE.search(seg)
        if pm and pm.start() <= 70:
            try:
                out.append((m.group(1), float((pm.group(1) or pm.group(2)).replace(',', '')), text[max(0, m.start() - 30):m.end() + 40].replace('\n', ' ')))
            except ValueError:
                pass
    return out


def md_path(code, grade):
    g = glob.glob(os.path.join(OUT_DIR, grade, f'{code}-*.md'))
    return g[0] if g else None


def main():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    E = {e['code']: e for e in ents}
    ab = [e for e in ents if e.get('grade') in ('A', 'B')]
    hard = []    # (code, kind, detail) 必须修
    soft = []    # (code, kind, detail) 人工眼核
    depth = {}   # code → metrics
    stats = Counter()
    for e in sorted(ab, key=lambda x: x['code']):
        c, g, iso = e['code'], e['grade'], (e.get('iso') or '').upper()
        fp = os.path.join(RESEARCH_DIR, f'{c}.json')
        if not os.path.exists(fp):
            hard.append((c, '无研究档', g)); continue
        d = json.load(open(fp, encoding='utf-8'))
        jtxt = json.dumps(d, ensure_ascii=False)
        mr = d.get('mail_review') or {}
        if not mr:
            hard.append((c, '无 mail_review', g)); continue
        nm = mr.get('next_move') or {}
        sn = mr.get('saga_now') or {}
        facts = mr.get('facts') or []
        b = mr.get('binding')
        btxt = b.get('level') if isinstance(b, dict) else (' / '.join(b) if isinstance(b, list) else (b or ''))
        # ---- 多 ----
        dirs = Counter((f.get('dir') or '?') for f in facts)
        m = {'grade': g, 'iso': iso, 'country': e.get('country'), 'facts': len(facts), 'in': dirs.get('来', 0), 'out': dirs.get('去', 0) + dirs.get('out', 0),
             'pi': dirs.get('PI', 0) + dirs.get('内', 0), 'elsa': sum(1 for f in facts if 'elsa' in str(f.get('k', '')).lower() or 'Elsa' in str(f.get('quote', ''))),
             'binding': bool(btxt), 'need': bool(mr.get('need')), 'situation': bool(mr.get('situation')), 'when': nm.get('when') or '',
             'channel': bool(nm.get('channel')), 'action': bool(nm.get('action')), 'draft': bool(mr.get('draft_en')), 'p1': sn.get('p1') or '', 'tier': sn.get('tier'),
             'signals': len(d.get('signals') or []), 'kp': len(d.get('kp') or []), 'summary': bool(d.get('summary'))}
        depth[c] = m
        for k in ('binding', 'need', 'situation', 'channel', 'action'):
            if not m[k]:
                hard.append((c, f'缺 {k}', g))
        if not m['when']:
            hard.append((c, '缺 when', g))
        if not facts:
            soft.append((c, '0 事实', f'{g} {e.get("country")} when={m["when"][:20]}'))
        if not m['summary']:
            soft.append((c, '无 summary', g))
        # ---- 对：结构 ----
        if m['tier'] not in (20, 25, 30, None):
            hard.append((c, '档位非 20/25/30', str(m['tier'])))
        for tok in MODEL_RE.findall(str(m['p1'])):
            if not known_model(tok):
                soft.append((c, 'P1 含未知型号', tok))
        for f in facts:
            dte = str(f.get('date') or '')
            if re.match(r'\d{4}-\d{2}-\d{2}', dte) and dte[:10] > TODAY:
                hard.append((c, '事实日期在未来', dte))
        de = mr.get('draft_en')
        if de is not None and not (isinstance(de, dict) and de.get('subject') and de.get('body')):
            hard.append((c, 'draft_en 结构错', str(de)[:60]))
        # ---- 对 / 好：信稿 ----
        if isinstance(de, dict) and de.get('body'):
            subj, body = de['subject'], de['body']
            txt = subj + '\n' + body
            private = any(k in subj for k in PRIVATE_SUBJ)
            # 价
            for model, price, ctx in pairs_in(body):
                if not known_model(model):
                    hard.append((c, '信稿型号不在任何价格表', f'{model} ${price} ← {ctx}'))
                    continue
                doms = tuple(x.lower() for x in (e.get('domains') or []))
                allowed = allowed_prices(model, doms)
                if model.startswith('STH-') and not any(abs(price - a) <= TOL for a in allowed):
                    soft.append((c, 'CENTEC 报价需眼核（按项目锚价）', f'{model} ${price} ← {ctx}'))
                    continue
                if model == 'STC-4168XGGCM':
                    soft.append((c, '4168XGGCM 报价需眼核（$280 活动已停）', f'${price} ← {ctx}'))
                    continue
                if not any(abs(price - a) <= TOL for a in allowed):
                    hard.append((c, '信稿价不在允许集合', f'{model} ${price}（允许 {sorted(allowed)[:8]}…）← {ctx}'))
            for price_only in re.findall(r'\$(\d{3}\.\d)\b', body):
                if abs(float(price_only) - 202.1) <= TOL or abs(float(price_only) - 194.3) <= TOL or abs(float(price_only) - 186.5) <= TOL:
                    pass  # bypass 无型号
            # Elsa 已见价冲突
            sp = str(sn.get('price') or '')
            if '$170（24 Port PoE' in sp and 'STC-424XGGPM-280W' in body and '$180' in body and '170' not in body:
                hard.append((c, '见过 $170 却直接报 $180 未说明', ''))
            if '$300（48 Port PoE' in sp and 'STC-448XGGPM' in body and '$335' in body and '300' not in body:
                hard.append((c, '见过 $300 却直接报 $335 未说明', ''))
            if '$280（10G Enterprise' in sp and re.search(r'STC-4168XGGCM[^$\n]{0,60}\$\d', body) and '280' not in body:
                hard.append((c, '见过 $280 却对 4168XGGCM 报了新价', ''))
            # 开头句引用的群发主题 + 日期
            fact_dates = {str(f.get('date') or '')[:10] for f in facts}
            outs = OUT_IDX.get(c, set())
            for s_, dd, mon, yy in OPENER_RE.findall(body):
                iso_d = f'{yy}-{MONTHS[mon]:02d}-{int(dd):02d}'
                same_day = {s for d_, s in outs if d_ == iso_d}
                if s_.strip().lower() in same_day:
                    stats['opener_ok'] += 1
                    if iso_d not in fact_dates:
                        soft.append((c, '开头句去信不在事实列表（邮箱索引有）', f'"{s_}" {iso_d}'))
                elif same_day:
                    hard.append((c, '开头句主题与当日去信不符', f'稿「{s_}」{iso_d} ≠ 邮箱「{" / ".join(sorted(same_day))}」'))
                elif iso_d in fact_dates:
                    soft.append((c, '开头句日期只在事实里、邮箱索引无（Elsa 1:1 等）', f'"{s_}" {iso_d}'))
                else:
                    hard.append((c, '开头句日期无去信记录', f'"{s_}" {iso_d}'))
            # 证书 × 国别
            exp = CERT_EXPECT.get(iso)
            if exp and re.search(r'\b(CE|FCC|UKCA|EAC|KC|RCM|BIS)\b', body):
                need, bad = exp
                if not any(re.search(rf'\b{t}\b', body) for t in need):
                    soft.append((c, f'{iso} 稿缺 {"/".join(need)}', subj[:50]))
                hit = [t for t in bad if re.search(rf'\b{t}\b', body)]
                if hit:
                    hard.append((c, f'{iso} 稿出现不相干证书 {hit}', subj[:50]))
            if iso in EU_LIKE and c not in CERT_LIST_OK and re.search(r'\bUKCA\b|\bFCC\b', body) and not re.search(r'no UL|FCC/CE/RoHS reports', body):
                soft.append((c, f'{iso}（欧盟/土）稿出现 UKCA/FCC', subj[:50]))
            # 英文稿语言判定（功能词占比）
            if not private:
                ws = re.findall(r"[^\W\d_]+", body.lower())
                if len(ws) >= 15 and sum(1 for w in ws if w in EN_WORDS) / len(ws) < 0.16:
                    hard.append((c, '信稿非英文（功能词占比低）', subj[:50]))
            # 署名
            sm = SIGN_RE.search(body + '\n')
            if sm and sm.group(1).strip() not in ('Simon', 'Alan', 'Elsa', 'Simon Ling', 'Alan Yang'):
                soft.append((c, '署名非 Simon/Alan/Elsa', sm.group(1).strip()))
            if 'Alan Yan' in body or 'Simon Yan' in body:
                hard.append((c, '署名杜撰姓氏', subj[:40]))
            # 一问（只数正文）
            nq = body.count('One question')
            if not private and nq == 0 and '?' not in body:
                soft.append((c, '无问句', subj[:50]))
            if nq > 1:
                soft.append((c, '多个 One question', subj[:50]))
            # 非英文混入
            if not private:
                na = {ch for ch in txt if ord(ch) > 127 and ch not in NONASCII_OK}
                if na:
                    soft.append((c, '英文稿含非 ASCII', ''.join(sorted(na))[:16] + ' | ' + subj[:40]))
            # 红线词
            for mm in FORBIDDEN.finditer(txt):
                w = mm.group(0)
                if any(w.lower().startswith(a.lower()) for a in ALLOW_FORBIDDEN.get(c, set())):
                    continue
                if w.lower() == 'elsa' and ('Elsa' in str(nm.get('channel')) or 'Elsa' in sp or '欠答' in str(nm.get('action'))):
                    continue  # Elsa 箱回复稿署名 Elsa
                hard.append((c, '红线词', f'{w} | {subj[:40]}'))
            if re.match(r'^\s*Re:', subj) and not any(f.get('dir') == '来' for f in facts):
                soft.append((c, '主题 Re: 但事实里无来信', subj[:50]))
            # 称呼名字能否在档案里找到
            gm = GREET_RE.search(body)
            if gm:
                name = gm.group(1).strip()
                first = re.split(r'[\s\-]', name)[0].strip(".'")
                if first and not name.lower().endswith('team') and first.lower() not in ('there', 'all', 'sir', 'madam') and len(first) > 1:
                    hay = (jtxt + json.dumps(e, ensure_ascii=False)).lower()
                    if first.lower() not in hay:
                        soft.append((c, '称呼名字在档案里找不到', name))
            # 渲染同步
            mp = md_path(c, g)
            if not mp:
                hard.append((c, '无渲染 MD', g))
            else:
                md = open(mp, encoding='utf-8').read()
                if subj[:40] not in md:
                    hard.append((c, 'MD 未含信稿主题（未重渲染）', subj[:40]))
                if btxt and btxt[:25] not in md:
                    soft.append((c, 'MD 未含绑定行开头', btxt[:25]))
        else:
            mp = md_path(c, g)
            if not mp:
                hard.append((c, '无渲染 MD', g))
        stats[f'{g}_total'] += 1
        stats[f'{g}_draft'] += 1 if m['draft'] else 0
        stats[f'{g}_facts'] += len(facts)
        stats[f'{g}_zero_facts'] += 1 if not facts else 0
    # ---------- 汇总 ----------
    def whenkey(w):
        return '群发节奏' if '群发' in w else ('不动' if '不动' in w else ('2027' if w.startswith('2027') else ('11 月队列' if (w.startswith('现在') or w.startswith('2026-1')) else '其他')))
    nodraft = Counter((m['grade'], whenkey(m['when'])) for m in depth.values() if not m['draft'])
    fdist = {g: Counter(min(m['facts'], 6) for m in depth.values() if m['grade'] == g) for g in ('A', 'B')}
    thin_a = sorted([(m['facts'], c) for c, m in depth.items() if m['grade'] == 'A'])[:15]
    thin_b = sorted([(m['facts'], c, m['country'], whenkey(m['when'])) for c, m in depth.items() if m['grade'] == 'B' and m['facts'] <= 1 and whenkey(m['when']) not in ('不动',)])
    hk = Counter(k for _, k, _ in hard)
    sk = Counter(k for _, k, _ in soft)
    L = [f'# A/B 加厚审计（{TODAY}，`scripts/saga_clients/audit_ab.py`）', '',
         f'> 口径：A/B 以 `entities.json` 的 grade 为准（A {stats["A_total"]} / B {stats["B_total"]}）。硬错误 = 必须修（价/型号/日期/红线/结构）；软项 = 人工眼核。',
         '', '## 一、多（证据量）', '',
         f'- 事实条数：A 共 {stats["A_facts"]} 条（户均 {stats["A_facts"] / max(1, stats["A_total"]):.1f}，0 事实 {stats["A_zero_facts"]} 户）；B 共 {stats["B_facts"]} 条（户均 {stats["B_facts"] / max(1, stats["B_total"]):.1f}，0 事实 {stats["B_zero_facts"]} 户）。',
         f'- 事实条数分布（≥6 并为 6）：A {dict(sorted(fdist["A"].items()))}；B {dict(sorted(fdist["B"].items()))}。',
         f'- 手写信稿：A {stats["A_draft"]}/{stats["A_total"]}；B {stats["B_draft"]}/{stats["B_total"]}。无手写稿按 when 分：' + '；'.join(f'{g} {k} {n}' for (g, k), n in sorted(nodraft.items())) + '。',
         f'- A 级事实最少的 15 户：' + '、'.join(f'{c}（{n}）' for n, c in thin_a) + '。',
         f'- B 级 ≤1 条事实且非「不动」的户：{len(thin_b)} 户（见明细 JSON `thin_b`）。',
         '', '## 二、对（正确性）硬错误', '', f'- 硬错误合计 **{len(hard)}**：' + ('；'.join(f'{k} {n}' for k, n in hk.most_common()) if hk else '0') + '。', '']
    for c, k, dtl in hard:
        L.append(f'- `{c}` {k}：{dtl}')
    L += ['', '## 三、好（可发性）软项（人工眼核）', '', f'- 软项合计 {len(soft)}：' + ('；'.join(f'{k} {n}' for k, n in sk.most_common()) if sk else '0') + '。', '']
    by = defaultdict(list)
    for c, k, dtl in soft:
        by[k].append(f'`{c}`' + (f'（{dtl}）' if dtl else ''))
    for k, items in sorted(by.items(), key=lambda x: -len(x[1])):
        L.append(f'- **{k}**（{len(items)}）：' + '；'.join(items[:60]) + ('；…' if len(items) > 60 else ''))
    L += ['', f'- 开头句「"主题" on 日期」与事实同日核对通过：{stats["opener_ok"]} 处。', '']
    open(REPORT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    json.dump({'date': TODAY, 'hard': hard, 'soft': soft, 'depth': depth, 'thin_b': thin_b, 'stats': dict(stats)}, open(DETAIL, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'A {stats["A_total"]} B {stats["B_total"]} | hard {len(hard)} soft {len(soft)} | report {os.path.relpath(REPORT, ROOT)}')
    for k, n in hk.most_common():
        print('  HARD', k, n)
    for k, n in sk.most_common():
        print('  soft', k, n)
    return 1 if hard else 0


if __name__ == '__main__':
    sys.exit(main())
