#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B 级 T4/T5 规则加厚（T27-R6）：对尚无加厚块的 B 级客户，用「官网快照摘要 + 用户表兴趣/备注」按固定规则生成
deepen.py 可直接吞的加厚块（角色 / 业务线 / P1 对位与档位 / 风险 / 近况信号 / 英文切入句 / 证据），级别固定标
「B 级加厚 v1-auto（规则生成：官网快照 + 用户表；未逐家人工调研）」——与人工逐家调研块（v1 / v2）明确区分；
人工复核时用 deepen.py 覆盖同名字段并改 level 即可。

用法：
  python3 autodeep.py --tiers T4,T5 [--limit N] [--codes SB-083,SB-084] > /tmp/auto.json
  python3 deepen.py < /tmp/auto.json
规则（只写可从快照 / 表内直接推出的内容，不编造事实）：
  角色：用户表类型（infer_type）优先 → 官网文案关键词（分销 / 网店 / ISP / 集成安装 / 制造）→ 「待核」；
  档位：OEM/自有品牌 30，分销/网店 20，其余 25；
  P1：用户表兴趣（infer_p1）> 快照自动对位（auto_p1）> 角色默认；P1 为 None 的（SFP / VC / DWDM 需求）保持待核型；
  风险：快照失败/停放、群发无回复、站内出现供应商品牌（Q-33 口径）、企业级品牌为主、疑似同行厂商、非主攻区。
"""
import argparse
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, RESEARCH_DIR  # noqa: E402
from render import SITE, TYPE_RULES, greeting_name, infer_p1, infer_tier, price_line  # noqa: E402

TODAY = '2026-10-21'
LEVEL = 'B 级加厚 v1-auto（规则生成：官网快照 + 用户表；未逐家人工调研）'
FOCUS = ('北美', '欧洲', '土耳其')
SUPPLIER_BRANDS = ('SmartByte（！）', 'HRUI（！）', 'Hohunet（！）', 'Saga（！）')
ENTERPRISE = ('Cisco', 'Juniper', 'Aruba', 'Fortinet', 'Extreme', 'Huawei', 'H3C', 'Allied Telesis')
SURV = ('Hikvision', 'Dahua', 'Uniview', 'Axis', 'Hanwha', 'Bosch', 'Vivotek', 'Milesight', 'Ajax', 'Paradox', 'ZKTeco', 'Pulsar')
PEER_SWITCH = ('Ubiquiti', 'TP-Link', 'MikroTik', 'Netgear', 'D-Link', 'Zyxel', 'Tenda', 'Ruijie', 'Grandstream', 'Cambium', 'PLANET',
               'Edimax', 'LevelOne', 'TRENDnet', 'Intellinet', 'Extralink', 'ONV', 'UniPoE', 'Teltonika')
IND = ('Moxa', 'Hirschmann', 'Phoenix Contact', 'Westermo', 'Advantech', 'Lantech', 'ORing', 'Antaira', 'ComNet', 'barox', 'Korenix',
       'EtherWAN', 'Maiwe', 'Siemens', 'Schneider')

# 官网文案角色判定（小写匹配；顺序 = 优先级）
ROLE_PATS = [
    ('制造商（同行或 OEM 客户待核）', 30, re.compile(r'\b(we (design|manufacture|produce)|manufacturer of|our own brand|private label|own brand|oem|odm)\b|производитель|üretici|hersteller von|produttore di|fabricante de')),
    ('分销商/批发商', 20, re.compile(r'(distribut|wholesal|großhandel|grosshandel|grossist|toptan|hurtown|dystrybu|ingrosso|mayorista|distribuidor|grossiste|velkoobchod|vertrieb|fachhandel|rivenditor|revendeur|дистрибут|поставщик|оптов|ספקית|bayi|tedarik|groothandel|leverancier|importer|importador|importateur)')),
    ('电商/网店', 20, re.compile(r'\b(shop|store|e-?shop|webshop|sklep|tienda|boutique|negozio|loja|магазин|mağaza|online store|add to cart|checkout|cart|eshop)\b')),
    ('电信/ISP/网络运营', 25, re.compile(r'\b(isp|internet service provider|internet provider|broadband|fiber internet|fibre internet|wisp|telecom operator|internet access|hosting)\b')),
    ('IT / 网络安全服务商（交换机为附带）', 25, re.compile(r'(cyber ?security|cybersecurity|it security|information security|penetration|siem|soc as a service|managed security)')),
    ('安防集成/经销', 25, re.compile(r'(cctv|surveillance|alarm|security|güvenlik|guvenlik|sicurezza|seguridad|segurança|sécurité|sicherheit|video ?surveillance|intrusion|videoüberwachung|videosorveglianza|videovigilancia|vidéosurveillance|видеонаблюд|охран|monitoring wizyjny|kamerov|zabezpeč|beveiliging)')),
    ('工业自动化/IoT 方案商', 25, re.compile(r'(automation|scada|industrial|automazione|automatisierung|otomasyon|automatyka|plc|iot|автоматизац|промышлен|automatisering|průmysl)')),
    ('系统集成/工程商', 25, re.compile(r'(install|integrat|solution|systems|engineering|services|smart home|audio.?visual|\bav\b|low voltage|structured cabling|network services|it services|it-service|consult|lösungen|systemhaus|netzwerktechnik|elektrotechnik|soluzioni|impianti|sistemi|çözüm|sistemleri|bilişim|teknoloji|rozwiązania|systemy|instalacje|soluciones|sistemas|intégrateur|решения|системы|интегратор|монтаж|řešení|systémy|lösningar|systemen|datacommunicatie|telecomunica|telekomünikasyon|network|netzwerk|réseau|сет)')),
]
EMAIL_OK = re.compile(r'^[A-Za-z0-9][\w.+-]*@[\w-]+(\.[\w-]+)+$')
SUPPLIER_IN_TABLE = re.compile(r'洪瑞|HRUI|Hongrui|SmartByte|Smartbyte|smartbyte|迈威|Hohunet|hohunet', re.I)
SEG_RULES = [  # (标签, 判定函数)
    ('安防监控（CCTV / 门禁）', lambda kw, t: kw.get('camera', 0) + kw.get('cctv', 0) + kw.get('nvr', 0) + kw.get('surveillance', 0) + kw.get('access control', 0) >= 4),
    ('工业自动化 / OT 网络', lambda kw, t: kw.get('industrial', 0) + kw.get('scada', 0) + min(kw.get('automation', 0), 5) >= 4),
    ('电信 / FTTH / ISP 设备', lambda kw, t: kw.get('ftth', 0) + kw.get('telecom', 0) >= 3),
    ('无线 / WiFi', lambda kw, t: kw.get('wireless', 0) + kw.get('wifi', 0) >= 3),
    ('数据中心 / 企业 IT', lambda kw, t: kw.get('datacenter', 0) + kw.get('data center', 0) >= 2),
    ('布线 / 线缆', lambda kw, t: kw.get('cable', 0) >= 3),
    ('光纤 / 媒体转换', lambda kw, t: kw.get('fiber', 0) + kw.get('fibre', 0) + kw.get('media converter', 0) + kw.get('sfp', 0) >= 3),
    ('网络交换 / PoE', lambda kw, t: kw.get('switch', 0) + kw.get('poe', 0) >= 1 or bool(re.search(r'\b(poe|switch|switches|przełącznik|przelacznik|switche)\b', t))),
]
P1_DESC = {
    'STC-424DGGPM-280W': ('24-port PoE+ L2+ managed switch with 4 SFP uplinks (280 W)', 'access'),
    'STC-424XGGPM-280W': ('24-port PoE+ L2+ managed switch with 4×10G SFP+ uplinks (280 W)', 'access'),
    'STC-28DGGPM': ('8-port PoE+ L2+ managed switch with 2 SFP uplinks', 'access'),
    'STC-424XGGM': ('24-port gigabit L2+ switch with 4×10G SFP+ uplinks', 'agg'),
    'STC-424XGGM(L3)': ('24-port gigabit L3 switch with 4×10G SFP+ uplinks', 'agg'),
    'STC-448DGGPM': ('48-port PoE+ L2+ managed switch', 'access'),
    'STC-448XGGM(L3)': ('48-port L3 switch with 4×10G SFP+ uplinks', 'agg'),
    'STC-448XGGPM': ('48-port PoE+ L2+ switch with 4×10G SFP+ uplinks', 'access'),
    'STI-288GP': ('DIN-rail 8-port gigabit PoE+ industrial switch with 2 SFP (−40~75 °C)', 'ind'),
    'STI-288GPM': ('DIN-rail managed 8-port PoE+ industrial switch with 2 SFP', 'ind'),
    'STI-288DGGPM': ('DIN-rail L2+ managed 8-port PoE+ industrial switch with 2×2.5G SFP', 'ind'),
    'STI-280GE': ('DIN-rail 8-port gigabit industrial switch with 2 SFP (−40~75 °C)', 'ind'),
    'STI-144GP': ('compact DIN-rail 4-port PoE+ industrial switch with 1 SFP uplink', 'ind'),
    'STI-21616GP': ('DIN-rail 16-port PoE+ industrial switch with 2 SFP', 'ind'),
    'STI-110GE': ('DIN-rail gigabit industrial media converter (1 SFP + 1 RJ45)', 'mc'),
    'STI-111GP': ('DIN-rail gigabit PoE industrial media converter', 'mc'),
    'STI-050GE': ('compact 5-port gigabit DIN-rail industrial switch', 'ind'),
}
QUESTION = {
    ('分销', 'access'): 'which port count moves most for you — 8 or 24?',
    ('电商', 'access'): 'which port count moves most for you — 8 or 24?',
    ('分销', 'ind'): 'is DIN-rail PoE or non-PoE the bigger volume for you?',
    ('电商', 'ind'): 'is DIN-rail PoE or non-PoE the bigger volume for you?',
    ('OEM', 'any'): 'which model would you want to see first under your own label?',
    ('制造', 'any'): 'which model would you want to see first under your own label?',
    ('电信', 'agg'): 'is your current need more on the 24G + 4×10G aggregation side or on PoE access?',
    ('any', 'agg'): 'is your current need more on the 24G + 4×10G aggregation side or on PoE access?',
    ('any', 'ind'): 'is DIN-rail PoE or non-PoE the bigger volume for your projects?',
    ('any', 'mc'): 'which fiber side do you need most — SFP-based or fixed single-mode SC?',
    ('any', 'access'): 'which port count do your typical sites need most — 8 or 24?',
}


def site_text(d, with_excerpt=False):
    """角色判定不吞正文摘录（nav 里的 Shop/Cart 会把集成商误判成网店）；品类判定可带摘录。"""
    parts = [d.get('title') or '', d.get('desc') or '', ' '.join(d.get('headings') or []),
             ' '.join((sp.get('title') or '') for sp in (d.get('subpages') or [])),
             ' '.join(re.sub(r'[/\-_.?=&]+', ' ', re.sub(r'^https?://[^/]+', '', sp.get('url') or '')) for sp in (d.get('subpages') or [])),
             ' '.join(re.sub(r'[/\-_.?=&]+', ' ', re.sub(r'^https?://[^/]+', '', u or '')) for u in (d.get('product_pages') or [])),
             (d.get('excerpt') or '')[:1500] if with_excerpt else '']
    return ' '.join(parts).lower()


def page_slugs(d):
    out = []
    for u in (d.get('product_pages') or [])[:4]:
        seg = [x for x in re.sub(r'^https?://[^/]+', '', u or '').split('/') if x]
        if seg:
            out.append(seg[-1][:40])
    return out


def clean_title(t):
    t = (t or '').strip()
    t = re.sub(r'\s*[\|\-–—:·»]\s*(home|homepage|start|startseite|accueil|inicio|anasayfa|ana sayfa|strona główna|главная|home page)\s*$', '', t, flags=re.I)
    t = re.sub(r'^(home|homepage|startseite|accueil|inicio|anasayfa|ana sayfa|strona główna|главная|welcome|welcome to)\s*[\|\-–—:·»]\s*', '', t, flags=re.I)
    return t.strip()[:90]


def user_interest(ent):
    """表内兴趣 + 人工备注（剔除「早期ai:」评估长文，另由 ai_desc() 取其公司描述行）。"""
    xs = []
    for s in (ent.get('interests') or []) + [r for r in (ent.get('remarks') or []) if not (r or '').startswith('早期ai')]:
        s = re.sub(r'\s+', ' ', (s or '')).strip()
        if s and s not in xs:
            xs.append(s)
    return xs


def ai_desc(ent):
    """表内「早期ai: NN% X\\n<公司描述>…」的公司描述行（用户团队早期 AI 评估，仅作角色参考，标明来源）。"""
    for r in ent.get('remarks') or []:
        if (r or '').startswith('早期ai'):
            lines = [x.strip() for x in r.split('\n') if x.strip()]
            if len(lines) > 1:
                return lines[1][:120]
    return ''


def user_type(ent):
    core = ' '.join(user_interest(ent) + (ent.get('names') or []) + (ent.get('froms') or []) + (ent.get('positions') or []))
    for pat, t in TYPE_RULES:
        if re.search(pat, core):
            return t, '用户表'
    ad = ai_desc(ent)
    if ad:
        for pat, t in TYPE_RULES[1:]:  # OEM 规则不采信 AI 描述（其「强调 OEM 贴牌」是建议而非事实）
            if re.search(pat, ad):
                return t, '表内早期 AI 描述'
    return '', ''


def role_of(ent, d):
    typ, src = user_type(ent)  # 用户表类型（兴趣/备注正则；AI 描述仅作次级参考）
    if typ:
        return typ, infer_tier(ent, typ), src
    t = site_text(d) if d else ''
    for name, tier, pat in ROLE_PATS:
        if t and pat.search(t):
            return name, tier, '官网文案'
    if t:
        return '网络/安防经销或集成（官网未见角色词，待核）', 25, '待核'
    return '经销/集成（类型待核，无官网快照）', 25, '待核'


def segments(d):
    if not d or d.get('status') != 'ok':
        return []
    kw = d.get('kw') or {}
    t = site_text(d, with_excerpt=True)
    return [lbl for lbl, fn in SEG_RULES if fn(kw, t)]


def pick_p1(ent, d, role, segs):
    p1, why = infer_p1(ent)
    src = '用户表兴趣'
    if why.startswith('无明确兴趣记录'):
        if d and d.get('auto_p1'):
            p1, why, src = d['auto_p1'], d.get('auto_p1_why') or '官网快照对位', '官网快照'
        else:
            src = '角色默认'
            if '工业' in role or '工业自动化 / OT 网络' in segs:
                p1, why = 'STI-288GP', '角色/品类为工业 → DIN 8 PoE+ 2 SFP 起手'
            elif '电信' in role:
                p1, why = 'STC-424XGGM', '电信/ISP → 24 GE + 4×10G 汇聚起手'
            elif any(k in role for k in ('集成', '安防', '工程')):
                p1, why = 'STC-28DGGPM', '集成/安防 → 8 口 PoE+ 2 SFP L2+ 起手（项目小口数多）'
            else:
                p1, why = 'STC-424DGGPM-280W', '分销/网店 → 24 口 PoE L2+ 走量款'
    alt = ''
    if p1 and p1.startswith('STC') and ('工业自动化 / OT 网络' in segs or '工业' in role):
        alt = '；官网工业词频高 → 备选 STI-288GP / STI-280GE（DIN 导轨）'
    elif p1 and p1.startswith('STI') and '安防监控（CCTV / 门禁）' in segs:
        alt = '；官网监控词频高 → 备选 STC-424DGGPM-280W（24 口 PoE 走量）'
    return p1, why, src, alt


def hook(ent, d, role, p1, brands):
    greet = greeting_name(ent)
    greet = f'{greet}, ' if greet else ''
    carried = [b for b in brands if b not in SUPPLIER_BRANDS][:2]
    opener = f"alongside the {' / '.join(carried)} lines you carry, " if carried else ''
    if p1 is None:
        body = ('we are an OEM/ODM source for Marvell-based PoE and DIN-rail industrial switches (neutral packing, CE/RoHS/FCC); '
                'for the accessory item you asked about we would quote a matching switch instead — ')
        q = 'which port count would that application need, 8 or 24?'
    else:
        desc, fam = P1_DESC.get(p1, (p1, 'access'))
        body = f'we supply the Marvell-based {desc} as an OEM/ODM source with neutral packing (CE/RoHS/FCC, small lots OK) — '
        key = 'any'
        for k in ('OEM', '制造', '分销', '电商', '电信'):
            if k in role:
                key = k
                break
        q = QUESTION.get((key, fam)) or QUESTION.get((key, 'any')) or QUESTION.get(('any', fam)) or QUESTION[('any', 'access')]
    s = (greet + opener + body + q).strip()
    return s[0].upper() + s[1:]


def build_item(ent, d, tier_tag, regen=False):
    code = ent['code']
    d = d if d and d.get('status') else None
    status = d.get('status') if d else ''
    ok = status == 'ok'
    kw = (d.get('kw') or {}) if ok else {}
    brands = list((d.get('brands') or [])) if ok else []
    role, tier, role_src = role_of(ent, d if ok else None)
    segs = segments(d)
    p1, why, p1_src, alt = pick_p1(ent, d if ok else None, role, segs)
    interests = user_interest(ent)
    fu = ent.get('fu_count') or len(ent.get('followups') or [])
    replied = bool(ent.get('reply_sub') or ent.get('reply_other') or ent.get('reply_read'))
    title = clean_title(d.get('title')) if ok else ''
    domain = (ent.get('domains') or [''])[0]
    # —— 摘要（中文，模板）
    bits = []
    if ok:
        bits.append(f"官网「{title or domain}」" + (f"（{d.get('lang')}）" if d.get('lang') else ''))
        if segs:
            bits.append('品类词：' + ' / '.join(segs[:4]))
        if brands:
            bits.append('站内品牌：' + '、'.join(brands[:6]))
        if d.get('models'):
            bits.append('站内型号：' + '、'.join(d['models'][:4]))
        elif page_slugs(d):
            bits.append('产品页：' + '、'.join(page_slugs(d)))
    elif status:
        bits.append(f'官网快照失败（{status}）')
    else:
        bits.append('无域名/未快照')
    if interests:
        bits.append('表内「' + '；'.join(interests)[:80] + '」')
    bits.append(f'群发 {fu} 次' + ('、有回复' if replied else '、无回复') if fu else '表内未见跟进记录')
    summary = f"{ent.get('country', '')}{role}：" + '；'.join(bits) + '。'
    # —— 风险
    risks = []
    if status == 'parked_or_empty':
        risks.append('官网停放/空站（快照 2026-10-21）：疑似停业或换域名，发前核实')
    elif status and not ok:
        risks.append(f'官网快照失败（{status}）：域名/证书待核，邮件可能退回')
    elif not status:
        risks.append('无域名或未快照：仅表内信息，身份待核')
    if fu >= 10 and not replied:
        risks.append(f'群发 {fu} 次无回复：换角度首触（不再发产品图，只问一个问题）')
    if any(b in SUPPLIER_BRANDS for b in brands):
        risks.append('站内出现 Saga 供应商/自家品牌 → Q-33 口径：发前核对渠道冲突（SmartByte 经销名单内者一律不碰）')
    if any(SUPPLIER_IN_TABLE.search(x) for x in interests):
        risks.append('表内提到在用/在卖 HRUI 或 SmartByte 等供应商品牌 → Q-33 口径：只推 SmartByte/Marvell 管理型与工业线，不报 HRUI 同款；若在 SmartByte 经销名单内则不碰')
    if role.startswith('IT / 网络安全'):
        risks.append('主业为 IT/网络安全服务：交换机只是附带采购，低预期')
    ent_b = [b for b in brands if b in ENTERPRISE]
    if len(ent_b) >= 2:
        risks.append('企业级品牌为主（' + '/'.join(ent_b[:3]) + '）：Saga 白牌只作价格补充线')
    if role.startswith('制造商'):
        risks.append('官网自称制造/自有品牌：先确认是同行厂商还是 OEM 买家')
    if tier_tag == 'T5' or (ent.get('region') or '') not in FOCUS:
        risks.append('非主攻区（T5）：低频跟进，不单独做本地化')
    # —— 近况信号
    signals = []
    if ok:
        signals.append(f"官网在线（快照 {(d.get('fetched_at') or '')[:10]}，{d.get('final_url') or domain}）")
        peer = [b for b in brands if b in PEER_SWITCH]
        if peer:
            signals.append('在售同口型交换品牌：' + '、'.join(peer[:5]) + ' → 直接对位替换')
        ind_b = [b for b in brands if b in IND]
        if ind_b:
            signals.append('在售工业网络品牌：' + '、'.join(ind_b[:4]) + ' → 工业线对位')
        sv = [b for b in brands if b in SURV]
        if sv:
            signals.append('安防品牌：' + '、'.join(sv[:4]) + ' → PoE 配套切入')
        mails = [m for m in (d.get('emails') or []) if EMAIL_OK.match(m)]
        if mails:
            signals.append('官网公开邮箱：' + '、'.join(mails[:3]))
    if interests:
        signals.append('用户表兴趣/备注：' + '；'.join(interests)[:120])
    ad = ai_desc(ent)
    if ad:
        signals.append('表内早期 AI 描述（未核实）：' + ad)
    # —— 证据
    ev = []
    if ok:
        quote = (d.get('desc') or '') or '；'.join((d.get('headings') or [])[:6])
        ev.append({'kind': '官网快照', 'claim': f'官网标题：{title or domain}' + (f'；品类词 {" / ".join(segs)}' if segs else ''),
                   'quote': quote[:240], 'url': d.get('final_url') or f'https://{domain}/', 'date': (d.get('fetched_at') or TODAY)[:10]})
    if interests:
        ev.append({'kind': '用户表', 'claim': '表内兴趣/备注', 'quote': '；'.join(interests)[:200], 'url': '（本地 Clients/ 表格，无公开 URL）', 'date': TODAY})
    pl = price_line(p1, tier) if p1 else ''
    saga_fit = {'p1': p1, 'tier': tier, 'why': f'{why}（来源：{p1_src}；档位：{role}→{tier}%）' + alt + (f'；{pl}' if pl else '')}
    item = {
        'code': code, 'merge': not regen,  # 重生成时整块替换（列表/字典不追加）
        'deep': {'done_at': TODAY, 'level': LEVEL},
        'summary': summary,
        'website_status': (f"在线（{domain}，快照 {(d.get('fetched_at') or TODAY)[:10]}）" if ok else (f'快照失败（{status}）' if status else '无域名')),
        'type': role,
        'company_facts': {'hq': ent.get('country', ''), 'other': (f"官网 {domain}，语言 {d.get('lang') or '?'}，快照状态 {status}" if status else '无官网快照') + f'；角色判定来源：{role_src}'},
        'business_lines': segs or (['（官网无品类词 / 无快照：按表内兴趣）'] if interests else ['（待核）']),
        'channels': {'role': role, 'region': ent.get('country', ''),
                     'contact': '、'.join((ent.get('emails') or [])[:2]) or '（表内无邮箱）'},
        'signals': signals, 'risks': risks, 'saga_fit': saga_fit,
        'email_hook': hook(ent, d if ok else None, role, p1, brands),
        'evidence_add': ev,
        'brands_add': [b for b in brands if b not in SUPPLIER_BRANDS],
    }
    if not regen:
        item['notes_add'] = f'规则加厚 {TODAY}（autodeep.py；T 档 {tier_tag}）'
    return item


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tiers', default='T4,T5')
    ap.add_argument('--codes', default='')
    ap.add_argument('--limit', type=int, default=0)
    a = ap.parse_args()
    ents = {e['code']: e for e in json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))}
    tiers = set(a.tiers.split(','))
    codes = []
    if a.codes:
        codes = [(c, '?') for c in a.codes.split(',')]
    else:
        for r in csv.DictReader(open(os.path.join(DATA, 'B级加厚分批.csv'), encoding='utf-8-sig')):
            if r['分批'] in tiers and r['等级'] == 'B' and (r['已加厚'] == '0' or r.get('加厚方式') == '自动'):
                codes.append((r['编号'], r['分批']))
    out = []
    for code, tt in codes:
        e = ents.get(code)
        if not e or e.get('grade') != 'B':
            continue
        p = os.path.join(RESEARCH_DIR, code + '.json')
        regen = False
        if os.path.exists(p):
            dp = json.load(open(p, encoding='utf-8')).get('deep') or {}
            if dp and 'auto' not in (dp.get('level') or ''):
                continue  # 已有人工加厚块，绝不覆盖
            regen = bool(dp)  # 已有自动块 → 整块重生成
        out.append(build_item(e, SITE.get(code), tt, regen))
        if a.limit and len(out) >= a.limit:
            break
    json.dump(out, sys.stdout, ensure_ascii=False, indent=0)
    print(f'autodeep items: {len(out)}', file=sys.stderr)


if __name__ == '__main__':
    main()
