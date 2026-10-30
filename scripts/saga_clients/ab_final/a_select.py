#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AB-FINAL-01 · A 级终评选择器（T29-U136 2026-10-30）。

Simon 规则（2026-10-30 原话要旨）：A = 成单客户 + 有过回信沟通的客户（主力军），Alan 邮箱跟进记录最重、S 邮箱极重、Elsa 次之；
                                   再加大池里极贴合 Saga 产品线 / 想法 / 相关跟进的户。先把 A 筛出来，B 之后再说。
实现：
  证据 = 回信档案（A/S Takeout 全量来信 + Elsa index_replied）+ Simon 表内「客户回复」日志 + 研究档 mail_review.facts（dir=来，U130/U131 人工复核时抄录的来信）。
  T1 成单   = PI 包 20 户（含 gg 8 户，Simon 可一键否）+ 人工核定 Saga 时代成单/样品单（DEAL_CURATED）。
  T2 回信   = 户级结论 R+（有实质回复：问价/要样/规格/数量/项目/约谈/OEM），且不在排除项。
  T3 贴合   = 无回信但极贴合（ISAF 当面 + 明确需求 / 自有品牌 OEM 对位 + 深挖坐实），人工名单 FIT_CURATED。
  排除（→ 最高 B，列表给 Simon 看）：守界国（UA/IR/SY/KP/CU）、巨头、Q-33 代理商客户、台湾品牌商（INH 最高 B）、中国大陆（国内只走私账）、
       永久 pass（sieve pass_final）、最后一句硬性婉拒（R±/R-）、仅自动回复、非主攻区域 + 免费邮箱个人 + 仅 1 次薄回复（旋钮 K1）。
  现 A 而无任何上述证据 → 默认降 B（旋钮 K3：Simon 可指名留 A）。
输出：data/saga_clients/A类终评_2026-10-30.csv / .json（决定 + 理由 + 证据摘要），不改研究档；应用由 patches/p78_a_final.py 完成。
"""
import csv
import importlib.util
import json
import os
import re
from collections import Counter

_spec = importlib.util.spec_from_file_location('reply_dossier', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reply_dossier.py'))
_rd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_rd)
classify_msg = _rd.classify_msg

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-30'
OUT_CSV = os.path.join(SD, f'A类终评_{DATE}.csv')
OUT_JSON = os.path.join(SD, f'A类终评_{DATE}.json')

# ---- 2026-10-30 Simon 澄清：Saga 成交客户只有 PI 包 20 户；下面这些「备注成单/样品单」是 Simon 本职公司时期的单，不算 Saga 成交（保留作历史互动线索，不进 A1）
DEAL_NOT_SAGA = {
    'SA-004': '5 电口样品（Boecek，埃森展后，WhatsApp 在联）', 'SA-018': 'PoE 电源常下单（Sewell，复购型）', 'SA-022': '6 台 MC 样品（Addon）',
    'SB-005': '工业 PoE FS 样品单（Rovez）', 'SB-009': '成单（Sicurmax，用户表）', 'SB-011': '成单客户（greentechme，用户表）', 'SB-013': '样品单 MC 25km + 8 口网管 PCB（Synchcom）',
    'SB-241': '2 个 90W PoE 注入器样品（Głuszek）', 'SB-320': '成单客户（Kryukov，用户再筛选表）', 'SB-441': '€50 光模块 + 转换器（Metal Union，微单）',
    'SB-976': '成交 2 次（Boltaev，俄语区名单）', 'SB-1115': '2026-10-17 已开 2 台样品 PI（Milliseconds，主动提出做英国经销）', 'SC-259': 'ISAF 2025 现场购 1 台（CEUIK）',
}
# 老成单但品类/年代不符（光猫 / 延长器 / SFP 2019–2020 等）→ 不入 A，单列
DEAL_OLD = {'SB-030': '2020 MC 样品（瑞士，之后 0 跟进）', 'SB-125': '2019 8 口样品（安哥拉）', 'SB-155': 'OM4301 延长器 1 对（法国）', 'SB-463': '2019 SFP 样品（塞内加尔）',
            'SB-728': '2020 光猫 8 个（新加坡）', 'SB-058': 'HDMI 光端机样品（波兰）', 'SB-069': '早年百兆/非管理（巴基斯坦，无互动）'}
# 用户表「成单客户」但 Simon 亲判「不行」→ 尊重 Simon
DEAL_SIMON_NO = {'SB-1135', 'SC-1173'}

# ---- 贴合名单（无回信/薄回信但极贴合；逐户理由）
FIT_CURATED = {
    'SB-074': 'ISAF 2025 当面：要 PoE 交换机，拿了彩页，WA 已加（土耳其主战场）',
    'SB-167': 'ISAF 2025 当面谈到样品；安卡拉安防承包商（土耳其主战场）',
    'SB-737': 'ISAF 2025 当面报价 2 光 8 电 Realtek PoE 网管 $70；分销商（土耳其）',
    'SB-388': 'ISAF 2025 当面：伊斯坦布尔弱电/安防工程，需求 PoE（土耳其）',
    'SB-392': 'ISAF 2025 当面（Evelyn）：i-PRO 土耳其 Premium 分销商（土耳其）',
    'SA-055': 'ISAF 2025 参展商：安卡拉弱电安防进口批发商 27–35 人（土耳其）',
    'SA-085': 'ISAF 2025：HES 旗下结构化布线品牌 HCS（土耳其，自有品牌 OEM 对位）',
    'SB-132': 'ISAF 2025：伊斯坦布尔工厂自动化分销商（Meanwell/PLC），工业 PoE 对位（土耳其）',
    'SB-274': 'Simon 表内亲记：加济安泰普光纤 ISP（AS205768），全光汇聚对位（土耳其）',
    'SB-389': 'LT-R10 留A：埃斯基谢希尔 ISP HiperFiber，自建光纤网（土耳其）',
    'SA-012': 'CommunicAsia 展会当面问了交换机/HDMI 光端机；FS/MC/VC 自有 logo（泰国，OEM 对位）',
    'SA-030': '伊斯坦布尔自有品牌交换机商 SN-ES/GS/XGS 全线白牌采购（OEM 30% 对位，土耳其）',
    'SA-009': 'DCN 土耳其分销商（2010 起，万台在网）：同类国产交换机渠道（土耳其）',
    'SB-173': '加拿大安防品牌商，交换机由 HRUI 代工贴标 → 直接对位 Saga OEM（Q-33 标记：按不碰同行客户规则仅观察）',
    'SB-529': '美国 DMSI：自有 logo MC 周边（OEM 对位）',
    'SB-599': '俄罗斯 SYMANITRON：工业网络自有品牌 + 合同制造（OEM 对位，俄语区）',
    'SB-970': '加拿大 EION：无线宽带系统商，165+ 渠道，配套交换机需求',
    'SB-143': '美国 BroadStar：AON 社区光纤 ISP，48×SFP 全光汇聚对位 STC-448XGGMO',
    'SB-103': '德国 GRUNDIG Security 品牌独家被许可人 Abetechs（自有品牌 OEM 对位）',
    'SB-077': '德国 Liveye：移动视频监控塔制造商（工业 PoE 整机对位）',
    'SA-082': '德国 ISIMKO：家族制中型系统集成商（1990 起，Cottbus）',
    'SB-256': '波兰 tvprzemyslowa：CCTV 网店/分销，在售 Hik/Dahua PoE（同类替代对位）',
    'SB-248': '美国 Nelly\'s Security：安防电商 switch 75 SKU（同类替代对位）',
    'SB-542': '德国 lanopia：光纤/铜缆增值分销，poe 247 / industrial 126 词频（对位）',
    'SB-988': '美国 Infinity Hardware：IT 硬件转售（新品 + 翻新），北卡',
    'SB-949': '澳大利亚 KSM：工业网络经销，国内货源在供（同类替代对位）',
    'SB-343': '印度 Zekko：电信 IT 与自动化方案商（工业 PoE 对位，印度名单）',
    'SB-1031': '英国 Ralakde：工业自动化备件贸易（工业交换机配套）',
    'SB-1114': '美国 Fikes Media：2026-10-03 来信问 OEM 定制层级（研究档 facts，属回信）',
}
Q33_NOTE = {'SB-173'}

ISO_FOCUS = {'US', 'CA', 'TR', 'GB', 'DE', 'IT', 'PL', 'ES', 'FR', 'CZ', 'NL', 'BG', 'SE', 'RO', 'LT', 'NO', 'CH', 'BE', 'FI', 'GR', 'HU', 'PT', 'DK', 'LV', 'CY', 'EE', 'SK', 'RS', 'SI', 'HR', 'IE', 'AT', 'AL', 'EU', 'MT', 'MK', 'IS', 'XK', 'LU', 'MD', 'BA', 'ME'}
ISO_GUARD = {'UA', 'IR', 'SY', 'KP', 'CU'}
FREE = re.compile(r'@(gmail|hotmail|yahoo|outlook|live|icloud|mail|yandex|protonmail|aol|gmx|web|list|bk|inbox|rambler)\.')

# ---- 人工判读修正（回信档案分类器误判）：not_reply = 非买家回复（卖家反推销 / 工单 / 通知 / 内部转发 / 把 Saga 当客户）；neg = 实为婉拒；pos = 实为实质回复
MANUAL = {
    'not_reply': {'SC-005': 'Intronics 自动确认', 'SC-1267': '对方营销邮件', 'SC-1468': 'BBC 通知', 'SC-164': 'SonicWall 工单确认', 'SC-1224': '工单确认', 'SC-591': 'R.STAHL 自动确认', 'SC-701': '自动确认（俄）', 'SC-740': '自动确认（俄）',
                  'SC-968': 'Triple-S 工单确认（挪）', 'SC-1726': '错发地址（RSL）', 'SC-2992': '把 Saga 当客户', 'SC-004': '卖家反推销', 'SC-1005': '卖家反推销', 'SC-194': 'Farnell 卖家回复', 'SB-775': 'Patton 卖家回复', 'SC-622': '卖家报 Planet 型号',
                  'SC-1332': '卖家报价', 'SC-1795': '卖家发 datasheet', 'SB-758': 'GDPR 通知', 'SB-438': '内部转发', 'SB-357': '休假自动回复', 'SC-1226': '休假自动回复', 'SB-1117': '把 Saga 当买家（贴合名单另议）', 'SC-204': '国内 OEM 供应商（神州数码）',
                  'SB-1109': '表内：一直对勾没看', 'SB-361': '自动回复（给代理人邮箱）', 'SB-530': '休假自动回复', 'SB-624': '地址作废通知', 'SB-925': '对方展会邀请（非回信）', 'SB-497': 'Gmail 表情反应', 'SB-949': '工单选择提示', 'SB-827': '工单登记提示',
                  'SB-462': '转发通知（意）', 'SB-062': '退信', 'SB-1103': '表内仅 thanks', 'SB-033': '表内仅 hi/OK', 'SB-117': '表内仅 useful', 'SB-443': '表内：有 154 了', 'SB-568': '表内：Simon 自己发的', 'SB-115': '表内：Simon 自己发的', 'SB-382': '表内：Simon 自己发的', 'SB-610': '表内：Simon 自己发的', 'SC-1428': '表内：拉黑', 'SC-1798': '表内：拉黑', 'SC-2423': '表内：NO BIZ/拉黑', 'SC-2446': '表内：做不了', 'SB-456': '表内：回复没内容'},
    'neg': {'SC-003': 'take us off your list', 'SC-067': 'only sell own equipment / don\'t waste time', 'SC-258': '国内（IC Intracom 采购）not interested', 'SB-196': '不要中国产', 'SB-694': 'No thanks（只要 SFP+ 前后风道）', 'SC-2255': 'already make / not interested',
            'SA-044': 'not our market', 'SB-936': 'not at this time', 'SA-037': '主要用 RTL 国内成熟产品', 'SA-073': '在和 benchu 合作', 'SB-1101': 'no need sample（想做代理推广）', 'SC-040': '只要 100G 以上 + 嫌价高', 'SB-120': '有需求会说', 'SB-299': '暂时没需求', 'SB-191': '有需求会说/暂时无需求', 'SB-044': '暂时没需求', 'SA-017': 'pass（Cisco $124）', 'SA-019': 'has own SFP solution', 'SB-366': 'no need', 'SC-151': '不做 CCTV 了，本地买', 'SB-021': 'No need now（信息而已）', 'SB-008': '买了别家', 'SA-046': '要 TAA/UL（Saga 无）', 'SC-2401': '伊朗（守界）'},
    'pos': {'SA-003': '用户备注：要了工业品价格表，特别问了 4 光 24 电 / 2 光 24 商业级价格（Simon 亲记）', 'SB-053': 'Onnet 2025：给出其只用的 4 种配置（规格要求，非婉拒）', 'SB-1114': '2026-10-03 来信问 OEM 定制层级（研究档）', 'SB-982': 'MCSS 2026-01 来信要产品清单（研究档）', 'SB-1116': 'Litech 2024-03 来信附技术规格（研究档）', 'SC-1904': '要求转 Viber/WhatsApp 谈需求'},
}


def load():
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    dossier = json.load(open(os.path.join(SD, f'回信档案_{DATE}.json'), encoding='utf-8'))
    sieve = json.load(open(os.path.join(SD, 'sieve.json'), encoding='utf-8'))
    research = {}
    for c in ents:
        p = os.path.join(SD, 'research', f'{c}.json')
        if os.path.exists(p):
            research[c] = json.load(open(p, encoding='utf-8'))
    return ents, dossier, sieve, research


def research_inbound(rs, seen_keys=(), seen_texts=()):
    """研究档 mail_review.facts 中 dir=来 的来信（U130/U131 人工抄录）→ (date, who, quote, cls)；与回信档案同一封（k 相同或正文重合）的去重。"""
    out = []
    ROBOT = re.compile(r'机器人|自动|postmaster|mailer|noreply|no-reply|用户表|Simon 跟进', re.I)
    AUTOQ = re.compile(r'^(?:automatic reply|thank you for contacting|thank you for your email, please select|we have received|your message|the email address .* is obsolete|（gmail emoji|.*couldn.t be delivered)', re.I)
    for f in ((rs or {}).get('mail_review') or {}).get('facts') or []:
        if f.get('dir') == '来' and f.get('quote'):
            who, q = str(f.get('who', '')), str(f.get('quote', ''))
            if ROBOT.search(who) or AUTOQ.search(q.strip()):
                continue
            if f.get('k') and f.get('k') in seen_keys:
                continue
            subj, _, txt = q.partition('｜')
            body = (txt or q).strip()
            if any(t and (t[:40] in body or body[:40] in t) for t in seen_texts):
                continue
            cls = classify_msg(subj if _ else '', body, who, who)
            if cls not in ('pos', 'weak', 'neg'):
                continue
            out.append((str(f.get('date', '')), who, q[:200], cls))
    return out


def main():
    ents, dossier, sieve, research = load()
    pi_map = json.load(open(os.path.join(ROOT, 'data', 'pi_orders', '客户编号映射.json'), encoding='utf-8'))['map']
    pi_codes = {}
    for k, v in pi_map.items():
        code = v.get('code') if isinstance(v, dict) else v
        if code == '旧B-1335':
            code = 'SB-003'  # rio-import 并入 SB-003（2026-10-24 归并）
        if code in ents:
            pi_codes[code] = (ents[code].get('pi') or {}).get('simon', '') or '成单'
    tbl = {r['档案编号']: r for r in csv.DictReader(open(os.path.join(SD, '客户主表.csv'), encoding='utf-8-sig'))}
    rows = []
    for c, e in ents.items():
        rs = research.get(c) or {}
        d = dossier.get(c)
        rc = d['reply_class'] if d else 'none'
        rin = research_inbound(rs, {m['k'] for m in (d['msgs'] if d else [])}, [m['excerpt'] for m in (d['msgs'] if d else []) if m['cls'] != 'auto'])
        if c in MANUAL['not_reply'] and rc not in ('none',):
            rc = 'auto'
            rin = []
        if c in MANUAL['neg']:
            rc = 'R±' if rc in ('R+', 'Rw') else 'R-'
        rin_pos = [x for x in rin if x[3] == 'pos']
        rin_neg = [x for x in rin if x[3] == 'neg']
        if c in MANUAL['pos'] or (rin_pos and rc in ('none', 'auto', 'R0', 'Rw') and c not in MANUAL['neg'] and not (rin_neg and rin_neg[-1][0] > (rin_pos[-1][0] if rin_pos else ''))):
            rc = 'R+'
        elif rin_neg and rc in ('none', 'auto', 'R0') and c not in MANUAL['pos']:
            rc = 'R-'
        deal = ''
        if c in pi_codes:
            deal = f'PI包·{pi_codes[c] or "成单"}'
        elif c in DEAL_NOT_SAGA:
            deal = '备注成单（非 Saga，本职公司时期）·' + DEAL_NOT_SAGA[c]
        elif c in DEAL_OLD:
            deal = '老成单·品类/年代不符·' + DEAL_OLD[c]
        elif c in DEAL_SIMON_NO:
            deal = '表内成单但 Simon 判不行'
        iso = e.get('iso') or '??'
        excl = []
        if iso in ISO_GUARD or e.get('region') == '乌克兰':
            excl.append('守界国')
        if (e.get('flags') or {}).get('giant'):
            excl.append('巨头')
        if iso == 'TW':
            excl.append('台湾品牌商 INH 最高 B')
        if iso == 'CN' or e.get('region') == '中国大陆':
            excl.append('中国大陆')
        if rs.get('q33_hold') or '代理商客户' in ' '.join(e.get('tags') or []):
            excl.append('Q-33 代理商客户')
        if re.search(r'国铁|铁路|轨交|railway|dzelzceļš|军工|tactical|军方|战术', str(rs.get('type', '')) + ' ' + str(e.get('name', ''))) and c not in pi_codes:
            excl.append('守界行业（轨交/军工）')  # 只看主业（type / 名称），summary 里提到军工项目的不算（如 SA-049 只谈自动化/商用）
        if not (e.get('emails') or []) and not (e.get('flags') or {}).get('wa_added') and c not in pi_codes:
            excl.append('无联系路径（无邮箱无 WA）')
        sv = (sieve.get(c) or {}).get('verdict')
        if sv == 'pass_final':
            excl.append('永久 pass')
        # 非主攻区（美加/欧洲/土之外；俄/印/韩也要有来有往）：要「有来有往」才算沟通（K1）——≥2 条实质信号，或 1 封 ≥40 字且含 样品/数量/项目/OEM/约谈 的来信；
        # 单句 price / catalog（尤其免费邮箱个人）→ B1 回信薄
        thin_far = False
        if rc == 'R+' and iso not in ISO_FOCUS and c not in MANUAL['pos']:
            hm = [m for m in (d['msgs'] if d else []) if m['cls'] in ('pos', 'weak')]
            tb = [t for t in (d['tbl_replies'] if d else []) if t['kind'] in ('pos', 'weak')]
            n_sig = len(hm) + len(tb) + len(rin_pos)
            strong_one = any(len(m['excerpt']) >= 40 and re.search(r'sample|\d+\s*(?:pcs|units|pieces|sets)|qty|quantity|project|tender|bid|oem|odm|skd|meeting|visit|whatsapp|viber|wechat|distribut|dealer|reseller|partner', m['excerpt'], re.I) for m in hm)
            if n_sig < 2 and not strong_one:
                thin_far = True
        grade_now = e.get('grade')
        tier, reason = '', ''
        if deal.startswith('PI包'):
            tier = 'A1'
            reason = deal
            if '永久 pass' in excl:
                excl.remove('永久 pass')
        elif rc == 'R+' and not excl and not thin_far:
            tier = 'A2'
            reason = f"真回信 {d['n_in_human'] if d else 0} 封 / 表内 {d['n_tbl_reply'] if d else 0} 条 / 研究档 {len(rin_pos)} 条（{d['boxes'] if d else 'R'}；{d['first'][:7] if d and d['first'] else ''}→{d['last'][:7] if d and d['last'] else ''}）"
        elif c in FIT_CURATED and not (set(excl) - {'Q-33 代理商客户'}):
            tier = 'A3'
            reason = '贴合·' + FIT_CURATED[c]
        else:
            tier = ''
        # 目标等级
        if tier:
            target = 'A'
        elif grade_now == 'A':
            target = 'B'
        else:
            target = grade_now  # B/C 不动（B 的事之后再说）
        hard_excl = {x for x in excl if x.startswith(('守界国', '巨头', '中国大陆', '永久 pass', '无联系路径'))}
        if rc == 'R+' and not tier and grade_now == 'C' and not hard_excl:
            target = 'B'  # 有实质回复的 C 户（薄回复 / 台湾 / Q-33 标记）按 U128 ② 捞到 B；守界/巨头/国内/永久 pass/无路径 留 C
        why_not = ''
        if not tier:
            if rc in ('R±', 'R-'):
                why_not = '最后一句婉拒：' + (MANUAL['neg'].get(c) or (d['msgs'][-1]['excerpt'][:80] if d and d['msgs'] else ''))
            elif excl:
                why_not = '排除：' + '、'.join(excl)
            elif thin_far:
                why_not = '非主攻区 + 免费邮箱 + 仅 1 次薄回复（K1）'
            elif rc == 'Rw':
                why_not = '只有薄回复（K3）'
            elif rc == 'auto':
                why_not = '只有自动回复/非买家回复：' + MANUAL['not_reply'].get(c, '')
            elif deal.startswith('老成单'):
                why_not = deal
            elif deal:
                why_not = deal + '（Simon 2026-10-30：非 Saga 成交）'
            elif grade_now == 'A':
                why_not = '无成单 / 无回信 / 未入贴合名单（K2 可指名留 A）'
        ev = ''
        if d:
            hm = [r for r in d['msgs'] if r['cls'] != 'auto'][-2:]
            ev = ' ‖ '.join(f"[{r['box']} {r['date']}] {r['excerpt'][:110]}" for r in hm)
            if d['tbl_replies']:
                t = d['tbl_replies'][-1]
                ev += f" ‖ 表 {t['date']}: {t['content'][:10]}→{t['reply'][:50]}"
        if rin:
            ev += ' ‖ 研 ' + ' / '.join(f"{a} {b}: {q[:80]}" for a, b, q, _k in rin[-2:])
        rows.append({'code': c, 'name': e.get('name'), 'country': e.get('country'), 'iso': iso, 'grade_now': grade_now, 'target': target, 'tier': tier, 'reason': reason, 'why_not': why_not,
                     'reply_class': rc, 'deal': deal, 'excl': '、'.join(excl), 'evidence': ev[:600], 'manual_grade': (e.get('manual') or {}).get('等级', '')})
    rows.sort(key=lambda r: (r['target'] != 'A', r['tier'] or 'Z', r['code']))
    json.dump(rows, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    with open(OUT_CSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['code', 'name', 'country', 'iso', 'grade_now', 'target', 'tier', 'reason', 'why_not', 'reply_class', 'deal', 'excl', 'evidence', 'manual_grade'])
        w.writeheader()
        for r in rows:
            if r['target'] != r['grade_now'] or r['tier'] or r['why_not']:
                w.writerow(r)
    A = [r for r in rows if r['target'] == 'A']
    print('A total', len(A), Counter(r['tier'] for r in A))
    print('moves', Counter((r['grade_now'], r['target']) for r in rows if r['target'] != r['grade_now']))
    print('A by region', Counter(ents[r['code']]['region'] for r in A).most_common())
    print('A1 by deal', Counter(r['deal'].split('·')[0] for r in A if r['tier'] == 'A1'))


if __name__ == '__main__':
    main()
