# -*- coding: utf-8 -*-
"""波 1 第 1 轮：mikrotik-info XA 土耳其 7 + 德国 8 = 15 家研究卡（轻卡：沿用来源库 2026-09-28 R53 / 10-06 R63 官网核对，本轮未外查）。
全部已于 9-28~10-10 群发过 24 口 PoE L2+（STC-424XGGPM-280W），未回 → 第二封换角度：STI 工业 L2+ PoE（MikroTik 没有的品类）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research_store import put

D = '2026-10-27'
R = 'W1-R01'
SIG = "\n\nSimon\nSaga Telecom - sagatele.com"
OPEN = "I wrote in late September about our 24-port PoE L2+ switch; this is a different product line, so a fresh note rather than a reply."
IND = "STI-288DGGPM: DIN-rail industrial L2+ switch, 8 x GE PoE+ (240 W budget) + 2 x SFP (1G/2.5G), -40 to +75 C, dual DC input, ERPS ring, SNMPv3, USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days), CE/RoHS, 3-year warranty. Also 4-port (USD 121) and 8 + 4 SFP (USD 147) versions, and PoE++ 90 W variants."
LIGHT = '轻卡：本轮未外查，沿用来源库官网核对（R53 2026-09-28 / R63 2026-10-06）。'

def ev(kind, claim, url, quote='', date='2026-09-28'):
    return {'kind': kind, 'claim': claim, 'quote': quote, 'url': url, 'date': date}

def mk(code, name, iso, city, site, email, summary, typ, brands, fit, ev_claim, ev_url, kp=None, grade='A', reason='', when=None, window='', angle='', body_lead='', q='', action='第二封', ev_date='2026-09-28', subject=None, extra_notes=''):
    if when is None:
        when = '2026-11-05' if iso == 'TR' else '2026-10-29'   # 2026-10-29 = 土耳其共和国日，TR 顺延一周
    card = dict(code=code, name=name, round=R, researched_at=D,
        alive='来源库 %s 官网核对在线；本轮未复查' % ev_date, summary=summary, type_final=typ, size='小型（未查）', brands_seen=brands,
        saga_line='SmartByte 商用 L2+（已发）→ 第二封换 STI 工业 L2+ PoE 补位', fit=fit,
        evidence=[ev('来源库官网核对', ev_claim, ev_url, '', ev_date), ev('来源库群发记录', 'R71：本户一轮跟进已完成（用户报告），逐户日期/收件地址未记录', 'External Clients/mikrotik-info/A/' + code, '', '2026-10-12')],
        contacts={'email': email, 'email_status': '来源库首选（official-company/channel）', 'kp': kp or []},
        touch_status='9-28~10-10 群发 24 口 PoE L2+ → 已发未回', saga_overlap='无',
        grade_final=grade, grade_reason_final=reason,
        next_move={'action': action, 'angle': angle or 'STI 工业 L2+ PoE（MikroTik 无此品类）', 'model': 'STI-288DGGPM', 'price': 'USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)', 'window': window or ('TR 周四 10–12' if iso == 'TR' else 'DE 周四 12–14'), 'when': when},
        notes=LIGHT + (' ' + extra_notes if extra_notes else ''))
    if action in ('第二封', '首触'):
        card['draft_en'] = {'subject': subject or 'Industrial DIN-rail PoE switches - the category MikroTik does not cover',
                            'body': body_lead + "\n\n" + OPEN + "\n\n" + IND + "\n\n" + q + SIG}
    return card

cards = []
# ---- 土耳其 7 ----
cards.append(mk('XA-M094', 'Internetten Ltd. / Wi (wi.com.tr)', 'TR', 'Gebze/Kocaeli', 'wi.com.tr', 'satis@wi.com.tr',
    'Gebze 的 MikroTik 授权分销商，光纤/电信器材专营，在售 Ruijie Reyee PoE+ 交换机、SFP、GPON，有 B2B 经销商计划。',
    'MikroTik 授权分销（光纤/电信）', ['MikroTik', 'Ruijie Reyee', 'GPON'], '已卖中国品牌 PoE，经销商计划现成；工业 PoE 是其空白',
    'Wi / WINET 为 MikroTik Authorized Distributor，在售 Ruijie Reyee RG-ES206GS-P 千兆 PoE+ 交换机、SFP、GPON、B2B 经销商计划', 'https://www.wi.com.tr/en',
    reason='TR 主攻区 MikroTik 分销 + 已卖中国 PoE 品牌 → 维持 A', body_lead='Hi,',
    q='Do your ISP and plant customers ask you for DIN-rail PoE switches, or is that still handled by other suppliers?'))
cards.append(mk('XA-M095', 'Merpa Bilişim (merpazar.com)', 'TR', 'Istanbul', 'merpazar.com', 'alinail@merpazar.com',
    '伊斯坦布尔 1990 年起的 IT 分销商（merpazar 网店），MikroTik 官方 reseller；总经理/创始人 Ali Nail Koçyiğit 实名邮箱公开。',
    'IT 分销 + 网店（MikroTik reseller）', ['MikroTik'], '通用分销，但有创始人直达邮箱',
    '官网 kimdir 页：Ali Nail Koçyiğit Genel Müdür（1990 创始人）', 'https://www.merpazar.com/merpazar-com-kimdir',
    kp=[{'name': 'Ali Nail Koçyiğit', 'role': 'Genel Müdür / 创始人', 'source': '官网 kimdir 页'}],
    reason='TR 主攻区、创始人实名直达 → 维持 A（来源库原 B，因 KP 直达升）', body_lead='Dear Mr. Koçyiğit,',
    q='Would a DIN-rail PoE line be of interest for your industrial and campus customers, or is your focus purely on the commercial range?'))
cards.append(mk('XA-M096', 'Nodenet Global', 'TR', 'Istanbul', 'nodenetglobal.com', 'sales@nodenetglobal.com',
    '伊斯坦布尔 10+ 年的网络管理/安全/云服务商，自宣布成为 MikroTik 土耳其分销商，有自有网店。',
    'MikroTik 土耳其分销（网络/安全/云背景）', ['MikroTik'], '分销 + 工程背景，工业 PoE 可卖进项目',
    '官网公告「Nodenet Global, MikroTik Türkiye Distribütörü Oldu!」', 'https://nodenetglobal.com/',
    reason='TR 主攻区 MikroTik 分销 → 维持 A', body_lead='Hi,',
    q='Is industrial PoE something your project team specifies today, or would a datasheet set be the right first step?'))
cards.append(mk('XA-M097', 'Net Vizyon (4mimo.com)', 'TR', 'Istanbul', '4mimo.com', 'satis@netvizyon.net',
    '伊斯坦布尔无线/网络分销商（4mimo 指向 Net Vizyon 网店），代理 Ubiquiti/Mimosa/Jirous/Ruijie/Siklu/Cudy，在售 UniFi PoE 交换机全系。',
    '无线/网络分销（Ubiquiti 等多牌）', ['Ubiquiti', 'Mimosa', 'Jirous', 'Ruijie', 'Siklu', 'Cudy', 'MikroTik'], '多牌分销，PoE 交换机已是品类；工业 PoE 给户外/塔站场景',
    '4mimo.com 指向 shop.netvizyon.net，在售 Ubiquiti UniFi PoE 交换机全系，代理 Ubiquiti/Mimosa/Jirous/Ruijie/Siklu/Cudy', 'https://4mimo.com/',
    reason='TR 主攻区多牌分销、PoE 品类现成 → 维持 A', body_lead='Hi,',
    q='For your wireless-backhaul and tower customers, would a hardened PoE switch at this price point be worth a sample?'))
cards.append(mk('XA-M098', 'Poyraz Network', 'TR', 'Kocaeli', 'poyraznetwork.com', 'sales@poyraznetwork.com',
    'Kocaeli 的 MikroTik Master Distributor（另 Ubiquiti 授权分销、Mimosa/Cudy/V-Sol），5000+ 产品、B2B 经销商价、培训项目，10 年经验。',
    'MikroTik Master Distributor + 多牌（B2B）', ['MikroTik', 'Ubiquiti', 'Mimosa', 'Cudy', 'V-Sol'], 'TR 头部 MikroTik 分销，交换机专类，经销商网络大',
    'Poyraz Network 为 MikroTik Master Distributor（另 Ubiquiti Authorized Distributor），导航含 Switches 与 Training Programs，5000+ 产品', 'https://poyraznetwork.com/us',
    reason='TR 主攻区 Master Distributor、交换机专类 → 维持 A（TR 优先级最高之一）', body_lead='Hi,',
    q='Would you like a sample unit for your lab, or first the full industrial price list for your reseller tiers?'))
cards.append(mk('XA-M099', 'Sekuritim Bilişim', 'TR', 'Istanbul', 'sekuritim.com', 'info@sekuritim.com',
    '伊斯坦布尔 2015 起的 MikroTik Türkiye Master Distributor + 认证培训中心（MTCNA…全系课程），独立网店 shop.sekuritim.com，安全/监控方向。',
    'MikroTik Master Distributor + 培训中心', ['MikroTik'], '培训中心触达大量集成商；安防方向用 PoE 多',
    'Sekuritim 自述 MikroTik Türkiye Master Distributor + MikroTik Certified Training Center（2015 起），shop.sekuritim.com', 'https://sekuritim.com/',
    kp=[{'name': 'Osman Kazdal', 'role': '培训联络（training@，leads-only 不直发）', 'source': 'etkinlik.io'}],
    reason='TR 主攻区 Master Distributor + 培训触达 → 维持 A', body_lead='Hi,',
    q='Since many of your trainees are integrators, would an industrial PoE line be useful to offer alongside the routing portfolio?'))
cards.append(mk('XA-M100', 'Sis Bil Tek (wifianten.com)', 'TR', 'Çorlu/Tekirdağ', 'wifianten.com', 'bilgi@wifianten.com',
    'Çorlu 的 MikroTik Master Distributor & 授权经销，在售 CRS326-24S+2Q+RM 与 UniFi 汇聚交换机，另代理 UBNT/RF-Elements。',
    'MikroTik Master Distributor（无线/WISP 方向）', ['MikroTik', 'Ubiquiti', 'RF Elements'], 'WISP 方向，户外/塔站需要工业 PoE',
    'wifianten.com 自述 Türkiye Mikrotik Master Distributor & Yetkili Satıcı，在售 CRS326-24S+2Q+RM 与 USW-Pro-Aggregation', 'https://wifianten.com/',
    reason='TR 主攻区 Master Distributor、WISP 场景 → 维持 A', body_lead='Hi,',
    q='Do your WISP customers currently buy hardened PoE switches for tower sites from you, or from elsewhere?'))

# ---- 德国 8 ----
cards.append(mk('XA-M021', 'VARIA System GmbH', 'DE', 'Chemnitz', 'varia-store.com', 'shop@varia-store.com',
    '开姆尼茨的 MikroTik Master Distributor/VAD（varia-store 网店），工业/IoT 方向明确，股东总经理 Sven Grimpe 实名。',
    'MikroTik Master Distributor + 工业/IoT 方向', ['MikroTik'], '工业/IoT 方向最贴 STI 线；KP 实名',
    'varia-store.com Impressum：Sven Grimpe Gesellschafter Geschäftsführer', 'https://www.varia-store.com/impressum/',
    kp=[{'name': 'Sven Grimpe', 'role': 'Gesellschafter-Geschäftsführer', 'source': 'Impressum'}],
    reason='DE 主攻区 Master Distributor + 工业/IoT 方向 → 维持 A', body_lead='Hello Mr. Grimpe,',
    q='Would a DIN-rail PoE line fit the industrial/IoT side of varia-store, and if so, would you prefer a sample or the full price list first?'))
cards.append(mk('XA-M122', '4Networks IT-Distribution GmbH (OMG.de)', 'DE', 'Aurich/Bremen', 'omg.de', 'info@4networks.de',
    '4Networks IT-Distribution（Teltonika/MikroTik/Cambium 分销）及其零售网店 OMG.de（MikroTik CRS 现货、UniFi、Teltonika），设 Enterprise 伙伴与安装商计划；CEO Thilko Cullmann、销售负责人 Bernd Eisenhauer。CCTV 库 XA-C0002 并入本号。',
    'IT 分销（MikroTik/Teltonika/Cambium）+ 网店', ['MikroTik', 'Teltonika', 'Cambium', 'Ubiquiti'], '多牌分销 + 安装商计划，工业 PoE 可与 Teltonika 工业路由配套',
    'OMG.DE 为 WLAN/定向无线专业零售商，MikroTik 品牌专区含 CRS520 现货，另 Ubiquiti/Teltonika/Cambium，设 Enterprise 伙伴与安装商计划', 'https://www.omg.de/',
    kp=[{'name': 'Thilko Cullmann', 'role': 'CEO', 'source': '4networks.de 官网/Impressum'}, {'name': 'Bernd Eisenhauer', 'role': 'Head of Sales', 'source': 'LinkedIn 谱'}],
    reason='DE 主攻区多牌分销、KP 实名、跨库并线后信息最全 → 维持 A', body_lead='Hello Mr. Eisenhauer,',
    q='Would an industrial PoE switch line next to your industrial-router brands be worth a look for 4Networks, or is that segment already covered?',
    extra_notes='并线自 XA-C0002（omg.de）。'))
cards.append(mk('XA-M124', 'FMS Internetservice GmbH (mikrotik-shop.de)', 'DE', 'Freiburg', 'mikrotik-shop.de', 'sales@fmsweb.de',
    '弗赖堡 FMS Internetservice 的 MikroTik 专营网店（域名即 mikrotik-shop），面向 ISP/企业/热点运营商，有独立「Switche」分类；GF Patrick Schaub。',
    'MikroTik 专营网店（单品牌依赖）', ['MikroTik'], '单品牌依赖最需要第二品牌；工业 PoE 不与 MikroTik 冲突',
    'mikrotik-shop.de 产品导航含「Switche」独立分类，首页在售 CRS520/CRS320-8P-8B-4S-RM，面向 ISP/企业/热点运营商', 'https://www.mikrotik-shop.de/',
    kp=[{'name': 'Patrick Schaub', 'role': 'Geschäftsführer', 'source': 'companyhouse.de'}],
    reason='DE 主攻区、交换机专类、GF 实名 → 维持 A', body_lead='Hello Mr. Schaub,',
    q='Would a non-competing industrial PoE line make sense for mikrotik-shop.de customers who run outdoor and plant installations?'))
cards.append(mk('XA-M125', 'I-NetPartner GmbH (mikrotik-store.eu)', 'DE', 'Göppingen', 'mikrotik-store.eu', 'sales@mikrotik-store.eu',
    '格平根 I-NetPartner 的 mikrotik-store.eu，自述 2008 起 MikroTik Master Distributor，面向 WISP/无线运营商/集成商，在售 CRS 400G 等高端交换机，设 B2B 账期流程。',
    'MikroTik Master Distributor（WISP/集成商）', ['MikroTik'], 'Master 分销、WISP 方向、B2B 流程成熟；工业 PoE 补位',
    'mikrotik-store.eu 自述「Offizieller MikroTik Master Distributor seit 2008」，在售 CRS418/CRS812（400G）/CSS606，设 B2B 经销账期', 'https://www.mikrotik-store.eu/',
    reason='DE 主攻区 Master Distributor（2008 起） → 维持 A', body_lead='Hello,',
    q='Do your WISP and integrator customers ask for DIN-rail PoE, and would you evaluate a sample for the store?'))
cards.append(mk('XA-M127', 'NSR One GmbH (nsr-tik.com)', 'DE', 'Hilden', 'nsr-tik.com', 'info@nsr-sy.com',
    'Hilden 的小型 MikroTik 经销（保护系统与通信），自述提供路由/交换/无线及批发价给企业与转售商；联系口为手机号 + 另一域名邮箱，规模很小。',
    '小型 MikroTik 经销/集成', ['MikroTik'], '规模很小，批发是口号多于体量',
    'nsr-tik.com 自述「Ihr offizieller Vertriebspartner für MikroTik-Produkte」，Router/Switches/Wireless，Großhandelsangebote für Wiederverkäufer', 'https://nsr-tik.com/',
    grade='B', reason='手机号 + 异域名邮箱的微型经销 → 降 B，不追第二封', action='等回', when='2027-01', body_lead='', q=''))
cards.append(mk('XA-M128', 'Neunetia GmbH', 'DE', 'Köln', 'neunetia.de', 'sales@neunetia.de',
    '科隆网络技术网店，「Switches」为首位热门类目，在售 MikroTik 配件、Cisco C1000/C1200 PoE+ 交换机、Fortinet、Aruba AP。',
    '网络设备网店（多牌，交换机为主类）', ['MikroTik', 'Cisco', 'Fortinet', 'HPE Aruba'], '交换机主类、多牌，接受新牌上架',
    'Neunetia Hot Categories 首位即「Switches」，在售 Cisco C1200-48P-4X / C1200-24FP-4G PoE+、Fortinet、Aruba AP', 'https://neunetia.de/',
    reason='DE 主攻区、交换机为主类的多牌网店 → 维持 A', body_lead='Hello,',
    q='Would an industrial PoE category be worth adding to the Neunetia shop, and may I send the datasheet set for listing?'))
cards.append(mk('XA-M130', 'etree GmbH', 'DE', 'Köln', 'shop.etree.de', 'sales@etree.de',
    '科隆总部的官方分销商（MikroTik/Teltonika 等 50+ 牌，40,000 SKU，11–50 人，波兰/乌克兰分部），创始人 CEO Grazian Dominik Twonski、GF Sebastian Rinne。',
    '多牌官方分销（50+ 牌，PL/UA 分部）', ['MikroTik', 'Teltonika', '50+ 牌'], '多牌分销 + 东欧分部，工业 PoE 可与 Teltonika 配套',
    'R63 web_search 核实：科隆总部官方分销 MikroTik/Teltonika 50+ 牌，11–50 员，波兰/乌克兰分部，40,000 SKU', 'https://etree.de/Services/Informationen/UEber-uns/',
    kp=[{'name': 'Grazian Dominik Twonski', 'role': 'Gründer & CEO', 'source': 'etree.de Über uns'}, {'name': 'Sebastian Rinne', 'role': 'Geschäftsführer', 'source': 'etree.de'}],
    reason='DE 主攻区多牌分销、50+ 牌、KP 实名 → 维持 A', ev_date='2026-10-06', body_lead='Hello Mr. Rinne,',
    q='Would etree consider an industrial PoE line from a new vendor for the DE/PL/UA shops, and what does your listing process look like?'))
cards.append(mk('XA-M131', 'hsc solutions', 'DE', 'Chemnitz', 'hsc-solutions.de', 'office@hsc-solutions.de',
    '开姆尼茨的小型系统集成商/MikroTik 经销（业主 Tom Zschockelt，Dipl.-Inf.），分销信号通用、无差异化切入点。',
    '小型 SI / MikroTik 经销', ['MikroTik'], '小 SI，项目配套为主',
    'Impressum + XING 双源实名：Tom Zschockelt Inhaber', 'https://hsc-solutions.de/impressum-hsc-solutions/',
    kp=[{'name': 'Tom Zschockelt', 'role': 'Inhaber', 'source': 'Impressum + XING'}],
    grade='B', reason='小型集成商（目标序列第 4 位），一轮未回 → 降 B，不追', action='等回', when='2027-01', body_lead='', q=''))

for c in cards:
    put(c)
print('mik cards', len(cards))
