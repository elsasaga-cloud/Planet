#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A-DEEP-01 · A 级候选「落池核验」深挖（T29-U137 2026-10-30，Simon：有实质回复的要深挖，比之前更广更深，确保真能落入 A pool，否则下放 B；究极深）。

对每个 A 候选（A类终评 target=A）把仓里所有线索合成一份核验卡 research['a_deep']：
  ① 身份（登记 / 官网 / 研究档法定名）② 角色与对位（类型、业务线、在售品牌/型号、是否自牌、是否卖交换机/PoE/工业/光纤）③ 需求证据（对方问过什么、型号/数量/项目）
  ④ 路径（邮箱 MX / WhatsApp / 最近一次真人来信距今）⑤ 规模 ⑥ 否决项（婉拒在后 / 守界 / 巨头 / 同行卖家 / Q-33 / 台湾 / 中国大陆）
  + 全程往来时间线（A/S/E 三箱去信与来信、表内跟进、研究档抄录）+ 我们报过的价（去信里的 $ 数字）+ 一段中文「故事线」。
自动结论：留A（六项全过）/ 下放B（有否决或路径断或角色不对位或身份与需求都薄）/ 待核（有缺口 → 网查补齐后再定）。
输出：data/saga_clients/A深挖_核验_2026-10-30.json/.csv；不改等级（应用由 p79 完成）。幂等。
"""
import csv
import glob
import json
import os
import re
from collections import defaultdict, Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-30'
BATCH = 'A-DEEP-01'
OUT_JSON = os.path.join(SD, f'A深挖_核验_{DATE}.json')
OUT_CSV = os.path.join(SD, f'A深挖_核验_{DATE}.csv')

PRICE_RE = re.compile(r'(?:US\$|USD|\$)\s?(\d{2,4}(?:\.\d+)?)|(\d{2,4}(?:\.\d+)?)\s?(?:USD|usd|US\$)')
MODEL_RE = re.compile(r'\b(ST[CIH]-[0-9A-Z-]{4,}|SG-[0-9A-Z-]{3,}|[0-9]{1,2}\s*[Pp]ort[s]?\s+[A-Za-z0-9 /+-]{3,30}?(?:Switch|PoE|MC|Converter))')
ROLE_WORDS = [
    ('OEM 品牌商', re.compile(r'自有品牌|自牌|own brand|OEM|ODM|贴牌|private label|white ?label|品牌商|manufacturer|制造商', re.I)),
    ('分销商', re.compile(r'分销|经销|distribut|wholesale|批发|reseller|dealer|供应商|trading|贸易', re.I)),
    ('集成商/安装商', re.compile(r'集成|integrat|install|安装|工程|contractor|solution|方案|弱电|security system|CCTV|安防', re.I)),
    ('ISP/运营商', re.compile(r'\bISP\b|运营商|operator|telecom operator|wisp|fiber network|宽带|broadband|AS\d{4,}', re.I)),
    ('终端用户', re.compile(r'终端|end ?user|自用|学校|school|hospital|医院|政府|ministry|inland revenue|church|gospel', re.I)),
]
FIT_RE = re.compile(r'switch|交换机|poe|industrial|工业|fiber|光纤|sfp|media converter|光电转换|network|网络|ethernet|din', re.I)
SELLER_RE = re.compile(r'卖家反推销|把 Saga 当(?:买家|客户)|only sell our own|we manufacture|工单|ticket|Farnell|Patton 卖家', re.I)
GUARD = {'UA', 'IR', 'SY', 'KP', 'CU'}
FREE = re.compile(r'@(gmail|hotmail|yahoo|outlook|live|icloud|mail|yandex|protonmail|aol|gmx|web|list|bk|inbox|rambler|163|qq|126)\.', re.I)


# ---- 人工终判（网查 2026-10-30，web_search；每条带 URL）：verdict, reason, facts[(url, quote)], extra{country_fix}
MANUAL_VERDICT = {
    'SB-1139': ('留A', '危地马拉 Smart Cities 方案设计顾问 Walter Arnoldo Beltetón Mohr：2026-03 带客户需求来（Cisco C9300L-48P-4X 等价、48×1G PoE+ + 4×10G、要堆叠），CENTEC 对位；项目型但需求具体、2026 年活跃',
                [('https://gt.linkedin.com/in/jorge-mondal-chew-86329256', 'Walter Arnoldo Belteton Mohr — Consultor de diseño de soluciones en Smart Cities de Centroamérica · Guatemala（LinkedIn「其他人还看过」侧栏，2026-10-30）')], {'country_fix': '危地马拉'}),
    'SC-1904': ('留A', 'Optimal Systems Distribution, Inc.（菲律宾 Pasig；打印机/条码/UPS/无线网络分销商；ZoomInfo 201–500 人、营收 $19.3M）：2025-12 来信要转 Viber/WhatsApp 谈需求——分销商坐实 + 主动要谈',
                [('https://www.facebook.com/optimalsystemsph/', 'Optimal Systems Distribution, Inc. — Printers, Barcode Scanners, UPS, Wireless Network · 13 Banner St. Pasig City · marketing@optimal.com.ph · +63 286315578'), ('https://www.zoominfo.com/c/optimal-systems-distribution-inc/457685843', 'Optimal Systems Distribution · Philippines · 201-500 Employees · Revenue $19.3 Million')], {}),
    'SC-1200': ('留A', 'Future Point Technologies（拉合尔；2015 年成立 IT 系统集成商，51–200 人，Cisco / Palo Alto 渠道伙伴）：2024-10 来信要 300 台 CLI 管理 L2 工业无风扇（ERPS）——标书型大单，有需求再接',
                [('https://www.zoominfo.com/c/future-point-technologies/460620478', 'Future Point is a prominent IT System Integrator based in Pakistan, established in 2015 … certified channel partner for Cisco and PaloAlto · 51-200 Employees · 60-D III Model Town, Lahore'), ('https://pk.linkedin.com/company/future-point-technologies', 'Future Point Technologies · IT Services and IT Consulting · Lahore · 51-200 employees · Founder and CTO Javed Hashmi')], {}),
    'SC-1399': ('留A', 'Team5 Technologies Pvt Ltd（班加罗尔；CIN U51909KA2016PTC096739；FY2025 营收 $3.56M；数据中心自动化 / 5G 测试 / 串口控制台 / iPDU，政企投标）：2024-11 按政府标书规格要型号 + 价格 + 授权书——DC/投标型，印度名单',
                [('https://tracxn.com/d/companies/team5technologies/__aS7cUwVKzhQ3tmBMip3dZUf234SJFESf71EGtkKK3XE', 'TEAM5 TECHNOLOGIES PRIVATE LIMITED CIN: U51909KA2016PTC096739, Active · Sep 26, 2016 · $3.56M (As on Mar 31, 2025) · 63 OVH Road, Basavanagudi, Bangalore'), ('https://www.zoominfo.com/c/team5-technologies-pvt-ltd/371376403', 'data center automation, 5G testing and measurement, and cloud security … Traffic Generators, Serial Console, iPDU, IoT, and PTP')], {}),
    'SC-1056': ('留A', 'Cloud Infotech Private Limited（诺伊达；CIN U74999UP2018PTC100481；电信/网络分销商，51–100 人，年营业额 25–100 千万卢比；服务 ISP / SMB / 安防）：回信人 Rajiv Goyal 就是 CEO/董事，2024-11 要全系工业交换机 + 最优价',
                [('https://www.cloud-infotech.co.in/profile.html', 'Cloud InfoTech … telecom and networking solutions … Trader - Wholesaler/Distributor · Company CEO Rajiv Goyal · 51 to 100 People · Annual Turnover 25 - 100 Cr · GST 09AAHCC3784F1ZG'), ('https://www.zaubacorp.com/CLOUD-INFOTECH-PRIVATE-LIMITED-U74999UP2018PTC100481', 'CIN U74999UP2018PTC100481 · Directors Parul Garg, Rajiv Kumar Goyal (2018-01-18) · D-92, Sector-63, Noida · Active')], {}),
    'SC-190': ('留A', 'Cronte Technology S.A.（基多；进口商 + 分销商，基多/昆卡/瓜亚基尔三地；法定代表 Luis Alberto Moreta Flores）：Elsa 报价后 2025-06「会看报价」、2025-11 主动转 WhatsApp 续谈——分销商坐实 + 仍在谈',
                [('https://www.dnb.com/business-directory/company-profiles/cronte-technology-sa.c6417fdaa4e01fc9532a13c4f67bbbfe', 'Cronte Technology S.A. · Quito, Pichincha · Key Principal Moreta Flores Luis Alberto · +593-22828917'), ('https://findglocal.com/EC/Quito/784843661896603/Cronte-Technology', 'Importadores y distribuidores · UIO - CUE - GYE · WhatsApp 098 427 3456 · www.cronte.net')], {}),
    'SC-584': ('留A', 'Namba Software（巴西；网络安全 / 云 / 混合基础设施方案商）：采购部 compras@ 2026-08「quero testar 1 pc」要测 1 台——样品级需求、2026 年活跃；拉美非主攻，薄 A',
                [('https://www.nambasoftware.com.br/', 'Namba Software — Especialistas em cibersegurança, cloud computing, infraestrutura híbrida e soluções inteligentes')], {}),
    'SC-1623': ('留A', 'Southern Elements（南非；光纤产品供应商，自营网店 shopfiber.co.za，含有源设备，全非洲发货）：2024-10 问 10 台价格——光纤渠道对位（SFP / MC / 光口交换机），非主攻区薄 A',
                [('https://southernelements.co.za/', 'Southern Elements … trusted supplier of hardware, tools and equipment for the fiber optic industry across Africa … active equipment · webstore shopfiber.co.za'), ('https://za.linkedin.com/company/southernelements', 'Southern Elements · 249 followers · fiber optic networks in Southern Africa')], {}),
    'SC-2904': ('留A', 'First Technology（南非 Midrand；1983 年起的 IT 集成集团，1,001–5,000 人，营收 $413M；网络/存储/云）：2024-08 三封来信确认我方角色与 24 口 Passive PoE 规格——大型集成商渠道，需走正式采购；非主攻区',
                [('https://www.zoominfo.com/c/first-technology-ltd/353641354', 'First Technology, established in 1983 … IT integration group within South Africa · 1K - 5K Employees · Revenue $413.2 Million · CEO Johan de Villiers'), ('https://za.linkedin.com/company/first-technology', 'First Technology · 1,001-5,000 employees · Headquarters Midrand · Storage & Networking, Networking Services')], {}),
    'SB-018': ('留A', 'Walker Security Systems UG（德国 Nettetal 微型安防安装商，Dahua/Jablotron/Ajax 认证）：2025-05 想要测试样机「need to replace a lot of switches」、2025-06 问是否可管理——主攻区 + 真需求', [], {}),
    'SB-1122': ('留A', 'Comtinu（俄罗斯；25G/100G 数据中心项目商）：2024-05 问 48×25G+8×100G / 32×100G，2025-12 三封往来（有 100/25G 项目，问公司网站）——DC 交换机优先客群', [], {}),
    'SB-487': ('留A', 'НПО Телеком（俄罗斯电信设备企业；KP Mikhail Afonin）：2024-06 问芯片、2026-05 问工厂所在城市 / 是否做 Microchip、CENTEC 方案——持续两年有问必答', [], {}),
    'SA-064': ('留A', 'ООО «ОПТА»（莫斯科招投标集中供货商）：20 次跟进 18 次回复，执行总裁亲自对接（Simon 标「比较重要」）——俄区最活跃回信户', [], {}),
    'SA-005': ('留A', 'Taurus Vision（比勒陀利亚 CCTV 视频管理集成商，1–10 人）：3 次实质回复 + WhatsApp 已加，2024-08 要工业 4/8 口 FS 价目——非主攻区但路径活', [], {}),
    'SB-477': ('下放B', 'eminnovate.com 身份不可核（同名印度 IT 公司 eminnovate.co 与网络设备无关；1 查未得即停），仅 2025-06 一句「Any rear facing port switches?」', [('https://eminnovate.co/about-us/', 'Eminnovate — IT services, Data Engineering, BI … Headquartered in India（与 eminnovate.com 是否同一主体未确认）')], {}),
    'SB-118': ('下放B', 'Genrov Ltd（英国一人 ROV 技术服务公司）：交换机需求是 ROV 项目一次性配套，2024-06 要过 DS 后无回；无复购土壤', [], {}),
    'SC-007': ('下放B', 'Born Electronics Limited（英国 2019 年注册，Companies House 最新账目「休眠」；官网挂 BI 系列白牌工业交换机）：疑为国产工业交换机品牌的英国前台 → 同行/卖家，不进 A', [], {}),
    'SC-001': ('下放B', 'SSL（以色列无线/战术通信集成商，代理 SILVUS 等，案例含军方通信、safe city）：军工/战术守界，只问过 8 口 130W——不进 A', [], {}),
    'SB-070': ('下放B', 'Neowine（韩国 fabless 芯片公司，想做代理但不懂网络产品）：行业外，2025-01 索样后无下文', [], {}),
    'SB-227': ('下放B', 'NKF Wireless（菲律宾小型 WISP，兴趣 PON——Saga 无）：2025-01 一句「sample?」；非主攻区 + 品类不对位', [], {}),
    'SC-1715': ('下放B', 'onsite.pk：与 SC-1200 Future Point 同日同文（300 台 CLI 工业 L2 标书）转来，主体未坐实（网查只见 onsite.com.pk 网络安全公司，未必同一家）——并入 SC-1200 跟进，本户 B', [('https://www.onsite.com.pk/contact.html', 'ONSITE Cyber Security Solutions provider in Pakistan · Lahore（onsite.com.pk，与 onsite.pk 关系未确认）')], {}),
    'SC-324': ('下放B', 'enercore.co.in：2024-05 两句（4 口价格 / 印度有无现货）后无回，身份与规模未坐实；印度名单留 B', [], {}),
    'SB-179': ('下放B', '印尼 yahoo 个人「CRISPY CREPES」（公司名疑为微信名，0 查）：2024-04 要过 DS；非主攻区个人', [], {}),
    'SB-510': ('下放B', '泰国 hotmail 个人 Pongpanot（项目型，2024-07 给过 2+4/2+8 工业 PoE 需求）：无公司主体，非主攻区', [], {}),
    'SB-297': ('下放B', '摩尔多瓦 Chisinau 联系人：无域名/公司主体，表内 1 次问 4+2 百兆千兆 100 个价格；不可核', [], {}),
    'SB-565': ('下放B', 'Marmaris Bilişim（土耳其，不会英文，拿别家产品册问 PoE splitter / PON）：品类不对位、无域名', [], {}),
    'SC-2150': ('下放B', '加拿大 telus.net 个人 milo64：2025-05 一句要 specs & pricing；无公司主体', [], {}),
    'SC-3133': ('下放B', 'federalcable.net = Actelis 销售 Casey Hurley 的另一地址，2024-09 回「Maybe….」；本户并入 SB-831 Actelis（A），不单独立 A', [], {}),
    'SB-872': ('下放B', '巴基斯坦 hotmail 个人 Ahmad Awan：2021–2023 问 E1 光 MC / 进口证；非 Saga 品类 + 个人', [], {}),
    'SB-116': ('下放B', 'Pyramid Enterprises（津巴布韦，无域名）：2025 主动问 100 对千兆 WDM MC 项目——WDM 非 Saga 线；非主攻区', [], {}),
    'SB-340': ('下放B', 'ROCKBIOS Limited（加纳，无域名）：2024 两次要价目；不可核、非主攻区', [], {}),
    'SB-865': ('下放B', '赞比亚 hotmail 个人 dbjcontrad：2025-10 Elsa 群发回「price info」；个人 + 非主攻区', [], {}),
    'SB-224': ('下放B', 'Arsenal TV（罗马尼亚 Gmail，电视/视频机构）：2 次回复后 14 次无果，无网站可核', [], {}),
    'SB-701': ('下放B', '美国 outlook 个人 chk999：2024-10 一句问 https；无公司主体', [], {}),
    'SC-012': ('下放B', 'LDZ Apsardze（拉脱维亚国铁安保子公司，国有）：轨交 + 国有守界 → 维持 C（资料保留）', [], {}),
    'SB-241': ('下放B', '爱尔兰 Gmail 个体 Tomasz Głuszek（2010 起用阿里国际站的小安装商/个体）：表内 2024 问 PoE / 要户外 48V PoE 交换机，WhatsApp 已加；注入器样品是本职公司时期的单；个人主体 → B', [], {}),
    'SC-1853': ('下放B', 'itezan：公司名查不到（表内原注「没查到东西」），只 WhatsApp 已加 + 要价格册；不可核', [], {}),
    'SC-665': ('下放B', 'Civitas Systems Srl（罗马尼亚）：2023 备注一句问价后 24 封去信 0 回；身份/角色未坐实', [], {}),
    'SC-3203': ('下放B', 'J Teem Solutions（斯里兰卡 Kurunegala 小型电信/安防/光纤安装商，Hikvision/Dahua）：2024-12/2025-01 两封（要 spec+price、「I am interested」）后无下文；非主攻区小安装商 → B',
                [('https://www.jteem.lk/fiber-solutions/', 'J Teem Solutions … provider of fiber optic network solutions in Sri Lanka … Kurunegala'), ('https://www.jteem.lk/security-alarm-systems/', 'security alarm systems … Hikvision and Dahua … Kurunegala, Sri Lanka')], {}),
}


def load_json(p, default=None):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return default


def own_text(m):
    text = m.get('text') or ''
    qa = m.get('quote_at')
    own = text[:qa] if isinstance(qa, int) and qa > 0 else text
    own = re.sub(r'(?m)^>.*$', '', own)
    own = re.split(r'\n(?:On .{5,80}wrote:|From: |Von: |De : |-----Original Message-----|Am .{5,60}schrieb|Le .{5,60}a écrit)', own)[0]
    return re.sub(r'\s+', ' ', own).strip()


def months_between(d1, d2):
    try:
        y1, m1 = int(d1[:4]), int(d1[5:7])
        y2, m2 = int(d2[:4]), int(d2[5:7])
        return (y2 - y1) * 12 + (m2 - m1)
    except Exception:
        return None


def main():
    ents = {e['code']: e for e in load_json(os.path.join(SD, 'entities.json'))}
    rows = load_json(os.path.join(SD, f'A类终评_{DATE}.json'))
    cands = [r for r in rows if r['target'] == 'A']
    dossier = load_json(os.path.join(SD, f'回信档案_{DATE}.json'), {})
    digest = load_json(os.path.join(SD, 'site_digest.json'), {})
    mx = (load_json(os.path.join(SD, 'mx_check_2026-10-29.json'), {}) or {}).get('domains', {})
    registry = {}
    for f in glob.glob(os.path.join(SD, 'registry', '*.json')):
        for c, v in (load_json(f, {}) or {}).get('rows', {}).items():
            registry.setdefault(c, v)
    quotes = defaultdict(list)
    qp = os.path.join(ROOT, 'data', 'S邮箱_报价史_2026-10-22.csv')
    if os.path.exists(qp):
        for q in csv.DictReader(open(qp, encoding='utf-8-sig')):
            quotes[q['收件域'].lower()].append((q['日期'], q['附近型号'], q['USD'], q['主题'][:40]))
    codes = {r['code'] for r in cands}
    # 三箱往来时间线
    tl = defaultdict(list)
    for box in ['gmail_a', 'gmail_s']:
        for f in sorted(glob.glob(os.path.join(ROOT, 'data', box, 'messages', '*', '*.jsonl'))):
            for line in open(f, encoding='utf-8'):
                m = json.loads(line)
                cl = [c for c in (m.get('client') or []) if c in codes]
                if not cl:
                    continue
                fr = (m.get('from') or {}).get('e', '')
                if m.get('dir') == 'in':
                    own = own_text(m)
                    gist = own[:160]
                    prices = []
                else:
                    body = re.sub(r'\s+', ' ', (m.get('text') or '')[:1500])
                    gist = (m.get('subj') or '')[:80]
                    prices = sorted({a or b for a, b in PRICE_RE.findall(body)})[:4]
                for c in cl:
                    tl[c].append({'date': m['date'][:10], 'dir': m.get('dir'), 'box': box[-1].upper(), 'from': fr, 'subj': (m.get('subj') or '')[:80], 'gist': gist, 'prices': prices, 'bulk': bool(m.get('bulk')), 'k': m['k']})
    out = {}
    for r in cands:
        c = r['code']
        e = ents[c]
        rs = (e.get('research') or {})
        d = dossier.get(c) or {}
        T = sorted(tl.get(c, []), key=lambda x: x['date'])
        for t in d.get('tbl_replies') or []:
            T.append({'date': t['date'], 'dir': 'tbl', 'box': '表', 'from': '', 'subj': t['content'], 'gist': t['reply'], 'prices': [], 'bulk': False, 'k': ''})
        for f in (rs.get('mail_review') or {}).get('facts') or []:
            q0 = re.sub(r'\s+', ' ', str(f.get('quote', '')))[:30].lower()
            dup = any(x['k'] == f.get('k') for x in T if f.get('k')) or any(str(f.get('date', ''))[:10] == x['date'] and q0 and (q0 in x['gist'].lower() or x['gist'][:30].lower() in str(f.get('quote', '')).lower()) for x in T)
            if f.get('dir') in ('来', '去') and f.get('k') and not dup:
                T.append({'date': str(f.get('date', ''))[:10], 'dir': 'in' if f['dir'] == '来' else 'out', 'box': 'R', 'from': str(f.get('who', ''))[:40], 'subj': '', 'gist': str(f.get('quote', ''))[:160], 'prices': [], 'bulk': False, 'k': f.get('k')})
        T.sort(key=lambda x: x['date'])
        ins = [x for x in T if x['dir'] == 'in' and x['box'] != 'R']
        human_in = [m for m in (d.get('msgs') or []) if m['cls'] != 'auto']
        outs = [x for x in T if x['dir'] == 'out']
        # ① 身份
        reg = registry.get(c)
        cf = rs.get('company_facts') or {}
        legal = cf.get('legal_name') or rs.get('name_official') or ''
        sdg = digest.get(c) or {}
        regnum = str((reg or {}).get('number') or '')
        reg_ok = bool(reg) and bool(regnum) and not re.search(r'0 查|未查|未取|未得|—|^$', regnum) and not re.search(r'0 查|未查', str(reg.get('source', '')))
        reg_name_ok = bool(reg) and not reg_ok and bool(reg.get('name')) and not re.search(r'0 查|个人|免费邮箱|主体不明', str(reg.get('name', '')) + str(reg.get('source', ''))) and bool(re.search(r'1 次检索|登记|register|registry|官方', str(reg.get('source', ''))))
        if reg_ok:
            ident = ('登记坐实', f"{reg.get('source', '')[:60]}: {str(reg.get('name', ''))[:60]} · {regnum[:40]} · {str(reg.get('status', ''))[:30]} · {str(reg.get('incorporated', ''))[:10]}")
        elif reg_name_ok:
            ident = ('登记线索', f"{reg.get('source', '')[:60]}: {str(reg.get('name', ''))[:80]} · {str(reg.get('status', ''))[:30]}")
        elif legal and '待补' not in legal and '未' not in legal[:2] and not re.match(r'^[\w.-]+\.[a-z]{2,}$', legal.strip(), re.I) and '@' not in legal and '（未具名）' not in legal and not re.search(r'建档|0 查|个人', legal):
            ident = ('研究档法定名', legal[:120])
        elif sdg.get('status') == 'ok' and sdg.get('title'):
            ident = ('官网坐实', f"{sdg.get('final_url', '')} · {str(sdg.get('title', ''))[:60]}")
        else:
            ident = ('未坐实', str(rs.get('website_status', '') or e.get('domains') or '')[:80])
        # ② 角色与对位
        role_txt = ' '.join([str(rs.get('type', '')), ' '.join(rs.get('business_lines') or []), str(rs.get('summary', ''))[:400], ' '.join(str(x) for x in (e.get('categories') or []))])
        role = '未知'
        for probe in (str(rs.get('type', '')), ' '.join(rs.get('business_lines') or []), str(rs.get('summary', ''))[:400]):
            if not probe.strip():
                continue
            for name, rx in ROLE_WORDS:
                if rx.search(probe):
                    role = name
                    break
            if role != '未知':
                break
        if (e.get('flags') or {}).get('own_brand') and role != 'OEM 品牌商':
            role = 'OEM 品牌商/' + role
        site_txt = ' '.join([str(sdg.get('title', '')), str(sdg.get('desc', '')), ' '.join(sdg.get('kw') or []) if isinstance(sdg.get('kw'), list) else str(sdg.get('kw', '')), ' '.join(sdg.get('headings') or [])[:400]])
        fit_words = sorted({w.lower() for w in FIT_RE.findall(role_txt + ' ' + site_txt)})[:8]
        fit_ok = bool(fit_words) or bool((e.get('fit') or {}).get('switch')) or bool((e.get('fit') or {}).get('mc_sfp'))
        p1 = (rs.get('saga_fit') or {}).get('p1') or ''
        # ③ 需求
        asks = []
        for m in human_in:
            if m['cls'] in ('pos', 'weak'):
                asks.append((m['date'], m['box'], m['excerpt'][:140]))
        for t in d.get('tbl_replies') or []:
            if t['kind'] in ('pos', 'weak'):
                asks.append((t['date'], '表', (t['content'] + '→' + t['reply'])[:140]))
        for f in (rs.get('mail_review') or {}).get('facts') or []:
            if f.get('dir') == '来' and not any(f.get('k') == m['k'] for m in human_in):
                q = str(f.get('quote', ''))
                if re.search(r'price|quot|sample|spec|pcs|units|project|oem|datasheet|catalog|interested|require', q, re.I):
                    asks.append((str(f.get('date', ''))[:10], 'R', q[:140]))
        asks.sort()
        ask_txt = ' ‖ '.join(f'{a} {b}: {t}' for a, b, t in asks[-4:])
        specific = bool(re.search(r'\d+\s*(?:pcs|units|pieces|sets|台|个|套)|project|tender|bid|oem|odm|skd|sample|样|型号|model|spec|datasheet|规格|moq', ask_txt, re.I))
        need = ('具体（型号/数量/项目/样品）' if specific else ('泛（问价/要目录）' if asks else '无'))
        # ④ 路径
        emails = e.get('emails') or []
        corp = [m for m in emails if not FREE.search(m)]
        mx_ok = any((mx.get(m.split('@')[-1].lower()) or {}).get('status') == 'ok' for m in emails)
        wa = bool((e.get('flags') or {}).get('wa_added') or e.get('wa_in_fu'))
        last_in = max([m['date'] for m in human_in] + [str(f.get('date', ''))[:10] for f in (rs.get('mail_review') or {}).get('facts') or [] if f.get('dir') == '来'] + [''])
        last_out = max([x['date'] for x in outs] + [''])
        gap = months_between(last_in, DATE) if last_in else None
        if (mx_ok or wa) and gap is not None and gap <= 24:
            path = ('活', f"{'企业邮箱' if corp else '免费邮箱'} MX {'ok' if mx_ok else '?'}{' + WA' if wa else ''}；最近来信 {last_in}（{gap} 月前）")
        elif (mx_ok or wa) and (gap is None or gap > 24):
            path = ('弱', f"{'企业邮箱' if corp else ('免费邮箱' if emails else '无邮箱')}{' + WA' if wa else ''}；最近来信 {last_in or '无'}" + (f"（{gap} 月前）" if gap is not None else '（仅表内/当面）'))
        elif not emails and not wa:
            path = ('断', '无邮箱无 WA')
        else:
            path = ('弱', f"MX 未确认{' + WA' if wa else ''}；最近来信 {last_in or '无'}")
        # ⑤ 规模
        size = (cf.get('staff') or rs.get('size') or '').strip()
        if not size and reg:
            size = str(reg.get('size', '') or '')
        size_lv = '未知' if not size else ('个人/微型' if re.search(r'个人|微型|1–5|1-5|1–10|sole|个体|自雇|一人', size) else '≥小型')
        # ⑥ 否决
        veto = []
        if e.get('iso') in GUARD or e.get('region') == '乌克兰':
            veto.append('守界国')
        if (e.get('flags') or {}).get('giant'):
            veto.append('巨头')
        if e.get('iso') == 'TW':
            veto.append('台湾品牌商（INH 最高 B）')
        if e.get('iso') == 'CN' or e.get('region') == '中国大陆' or any(str(x).endswith('.cn') for x in (e.get('domains') or [])):
            veto.append('中国大陆')
        if rs.get('q33_hold'):
            veto.append('Q-33 代理商客户')
        if r.get('reply_class') in ('R±', 'R-'):
            veto.append('最后一句婉拒')
        ab = rs.get('ab_final') or {}
        if SELLER_RE.search(str(ab.get('why_not', '')) + ' ' + str(rs.get('summary', ''))[:200]):
            veto.append('疑似同行/卖家')
        # 结论
        gaps = []
        if ident[0] == '未坐实':
            gaps.append('身份未坐实')
        if role == '未知':
            gaps.append('角色未知')
        if not fit_ok:
            gaps.append('对位不明')
        if need == '无':
            gaps.append('无需求证据')
        if path[0] == '弱':
            gaps.append('路径弱')
        if size_lv == '未知':
            gaps.append('规模未知')
        strong = (len(human_in) >= 2) or wa or specific or (bool(corp) and ident[0] != '未坐实' and fit_ok and role != '未知')
        if r['tier'] == 'A1':
            verdict = '留A'  # Saga 成单户：无条件 A
        elif r['tier'] == 'A3':
            verdict = '下放B' if veto else ('留A' if (ident[0] != '未坐实' and role != '未知' and fit_ok) else '待核')
        elif veto:
            verdict = '下放B'
        elif path[0] == '断':
            verdict = '下放B'
        elif role == '终端用户' and not specific:
            verdict = '下放B'
        elif ident[0] == '未坐实' and size_lv in ('个人/微型', '未知') and need != '具体（型号/数量/项目/样品）':
            verdict = '下放B'
        elif set(gaps) <= {'路径弱', '规模未知'} and '路径弱' in gaps and not strong:
            verdict = '下放B'  # 2 年以上只回过一句泛问价、无 WA、身份/角色也薄 → 冷，下放 B
        elif set(gaps) <= {'路径弱', '规模未知'}:
            verdict = '留A'
        else:
            verdict = '待核'
        web_facts = []
        extra = {}
        if c in MANUAL_VERDICT:
            verdict, mreason, wf, extra = MANUAL_VERDICT[c]
            gaps = gaps + ['人工终判：' + mreason]
            web_facts = [{'url': u, 'quote': q, 'date': DATE} for u, q in wf]
        # 故事线
        first = T[0]['date'] if T else ''
        n_out = len(outs)
        pr = sorted({p for x in outs for p in x['prices']}, key=lambda v: float(v))[:6]
        qh = quotes.get((e.get('domains') or [''])[0].lower(), [])[-3:]
        story = (f"{e.get('country')}{'·' + role if role != '未知' else ''}；{ident[0]}：{ident[1][:80]}。"
                 f"往来 {first or '—'}→{max(last_in, last_out) or '—'}：我方去信 {n_out} 封（A {sum(1 for x in outs if x['box'] == 'A')} / S {sum(1 for x in outs if x['box'] == 'S')}），"
                 f"对方真人来信 {len(human_in)} 封 + 表内/备注 {len(d.get('tbl_replies') or [])} 条；对方问过：{ask_txt[:200] or '—'}。"
                 f"我方报过：{('$' + ' / $'.join(pr)) if pr else ('；'.join(f'{a} {b} ${u}' for a, b, u, _ in qh) if qh else '未见报价数字')}。"
                 f"对位：{p1 or '待定'}；路径：{path[1]}。")
        out[c] = {'code': c, 'name': e.get('name'), 'country': e.get('country'), 'iso': e.get('iso'), 'region': e.get('region'), 'tier': r['tier'], 'grade_now': e.get('grade'),
                  'ident': ident, 'role': role, 'fit_words': fit_words, 'fit_ok': fit_ok, 'p1': p1, 'need': need, 'asks': asks[-6:], 'path': path, 'size': size, 'size_lv': size_lv,
                  'veto': veto, 'gaps': gaps, 'verdict': verdict, 'story': story, 'web_facts': web_facts, 'extra': extra, 'manual': c in MANUAL_VERDICT, 'timeline': T[-40:], 'n_out': n_out, 'n_in': len(human_in), 'last_in': last_in, 'last_out': last_out, 'prices_out': pr}
    json.dump(out, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    with open(OUT_CSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['编号', '公司', '国家', '区域', '档', '现等级', '身份', '身份依据', '角色', '对位词', 'P1', '需求', '最近问话', '路径', '路径依据', '规模', '否决', '缺口', '结论', '去信', '来信', '最近来信', '故事线'])
        for c, o in out.items():
            w.writerow([c, o['name'], o['country'], o['region'], o['tier'], o['grade_now'], o['ident'][0], o['ident'][1], o['role'], ' '.join(o['fit_words']), o['p1'], o['need'], ' ‖ '.join(f'{a} {b}: {t}' for a, b, t in o['asks'][-2:]), o['path'][0], o['path'][1], o['size'], '、'.join(o['veto']), '、'.join(o['gaps']), o['verdict'], o['n_out'], o['n_in'], o['last_in'], o['story']])
    print('cands', len(out), Counter(o['verdict'] for o in out.values()))
    print('by tier', Counter((o['tier'], o['verdict']) for o in out.values()))
    print('gaps', Counter(g for o in out.values() for g in o['gaps']))
    print('veto', Counter(v for o in out.values() for v in o['veto']))


if __name__ == '__main__':
    main()
