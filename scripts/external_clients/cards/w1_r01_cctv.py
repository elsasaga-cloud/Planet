# -*- coding: utf-8 -*-
"""波 1 第 1 轮：CCTV-PoE XA（DE/TR/US）22 家研究卡。来源库只有 名称/类型/邮箱，本轮 2026-10-27 web_search 逐家复核（14 家外查，8 家轻卡）。
CCTV 库自带的「报价(FOB) $26/$42/$68」是原代理臆造价，一律不用；价格锚取 HRUI/SmartByte 价台账。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research_store import put

D = '2026-10-27'
R = 'W1-R01'
SIG = "\n\nSimon\nSaga Telecom - sagatele.com"
P24U = 'STC-2224GP (24 x GE PoE+ + 2 x GE + 2 x SFP, 300 W, unmanaged) USD 86'
P8U = '8-port PoE+ units from USD 28'
P24M = 'STC-4424GCPM (24 x GE PoE+ + 4 x GE + 4 x SFP, L2 managed, 300 W) USD 165'
PL2 = 'STC-424XGGPM-280W (24 x GE PoE+ 280 W + 4 x 10G SFP+, Marvell L2+) USD 170'
TAIL = ', all EXW Shenzhen, snapshot 2026-10-27, valid 15 days, CE/RoHS/REACH, 12-month warranty.'
INTRO_DE = "Saga Telecom supplies PoE and L2+ switches to security and network distributors in Europe - under our label or the distributor's own."

def ev(kind, claim, url, quote='', date=D):
    return {'kind': kind, 'claim': claim, 'quote': quote, 'url': url, 'date': date}

cards = []

# ---------- 并线 / 守界 / 大体量：不发 ----------
cards.append(dict(code='XA-C0002', name='OMG (omg.de) = 4Networks IT-Distribution', round=R, researched_at=D,
    alive='活（见 XA-M122）', summary='omg.de 是 4Networks IT-Distribution GmbH 的零售网店（同一公司，mikrotik 库已有 XA-M122 全档）。跨库重复，并线到 XA-M122，本号不再单独跟。',
    type_final='跨库重复（并线 XA-M122）', size='见 XA-M122', brands_seen=['Ubiquiti', 'MikroTik', 'Teltonika', 'Cambium'],
    saga_line='见 XA-M122', fit='—',
    evidence=[ev('来源库交叉', 'mikrotik 库 XA-M122「4Networks IT-Distribution（OMG.de）」域名 omg.de 与本条相同', 'External Clients/mikrotik-info/A/XA-M122')],
    contacts={'email': 'shop@omg.de', 'email_status': '公开；不用，走 XA-M122 的 info@4networks.de'},
    touch_status='未发信（CCTV 库从未发信）；XA-M122 已于 9-28~10-10 群发', saga_overlap='跨库重复 XA-M122',
    grade_final='C', grade_reason_final='跨库重复 → C（并线），研究与跟进记在 XA-M122',
    next_move={'action': '并线', 'angle': '→ XA-M122', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='并线目标 XA-M122。'))

cards.append(dict(code='XA-C0010', name='EtherWAN Systems', round=R, researched_at=D,
    alive='活', summary='台湾工业交换机厂商（1996 起，2017 被 Phoenix Contact 收购），美国 Anaheim 分部。是同行/厂商，不是客户。',
    type_final='同行厂商（工业交换机 OEM）', size='Phoenix Contact 子公司', brands_seen=['EtherWAN'],
    saga_line='—', fit='同行，不碰',
    evidence=[ev('来源库', 'OEM工业以太网/PoE/千兆交换机，台湾制造；2017 年被 Phoenix Contact 收购', 'External Clients/CCTV-PoE/A/XA-C0010')],
    contacts={'email': 'marketing@etherwan.com', 'email_status': '公开；不用'},
    touch_status='未发信', saga_overlap='无',
    grade_final='C', grade_reason_final='厂商/同行 → C 不动（原库自己也标「竞品/情报」）',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes=''))

cards.append(dict(code='XA-C0009', name='ADN Distribution GmbH', round=R, researched_at=D,
    alive='活（2023 营收 7.8 亿欧元）', summary='波鸿的 DACH 头部增值分销商（1994 起，约 260 人，7,000+ 伙伴，2023 年营收 ≈7.8 亿欧元），主线云/安全/存储/UCC/现代办公，Edgecore 在其网络线内。对 Saga 这个体量的供应商而言是「大的搞不定」。',
    type_final='大型 VAD（DACH 头部）', size='≈260 人；€780M（2023）', brands_seen=['Citrix', 'Dell', 'Microsoft', 'Nvidia', 'Sonicwall', 'Watchguard', 'Edgecore'],
    saga_line='—', fit='体量与厂商准入门槛都不匹配',
    evidence=[ev('IT-Business「Wer ist ADN?」', 'rund 260 Mitarbeiter … über 7.000 Partnern', 'https://www.it-business.de/wer-ist-adn-a-88250c399eb07a093ee34a396c50de71/', '', '2025-05-26'),
              ev('ADN 官网新闻', 'Umsatz 2023 auf rund 780 Millionen Euro', 'https://www.adn.de/de/aktuelles/news/newsdetail/adn-group-steigert-jahresumsatz-auf-780-millionen-euro', '', '2024-09-01')],
    contacts={'email': 'info@adn.de', 'email_status': '公开；不用'},
    touch_status='未发信', saga_overlap='无',
    grade_final='C', grade_reason_final='7.8 亿欧元的头部 VAD，守界「大的搞不定」→ C 不动',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes=''))

cards.append(dict(code='XA-C0027', name='ELBEX (Deutschland) GmbH', round=R, researched_at=D,
    alive='存疑：2025-02-03 雷根斯堡法院裁定临时破产管理（登记摘录）', summary='雷根斯堡 1979 年起的视频监控厂商/分销商（Uniview、Avigilon 德国分销，20–49 人）。登记记录显示 2025-02 进入临时破产管理，2025-03 变更管理人；现状未明。内部备注，不对外提。',
    type_final='安防分销商（破产程序中）', size='20–49 人（历史）', brands_seen=['Uniview', 'Avigilon', '自有 ELBEX'],
    saga_line='HRUI PoE（若恢复经营）', fit='类型对口，但主体状态不明',
    evidence=[ev('Uniview 欧洲伙伴页', 'distributor of Uniview (UNV), Avigilon … national clients are installers, integrators and resellers', 'https://global.uniview.com/it/Partner/Find_our_partners/Partners/Europe/', '', '2024-07-11'),
              ev('webvalid 登记摘录', 'durch Beschluss des Amtsgerichts Regensburg vom 03.02.2025 … vorläufige Insolvenzverwaltung angeordnet', 'https://www.webvalid.de/company/ELBEX+(Deutschland)+GmbH,+Regensburg/HRB+2545', '', '2025-03-12')],
    contacts={'email': 'cctv@elbex.de', 'email_status': '公开；主体状态未明，暂不发'},
    touch_status='未发信', saga_overlap='无',
    grade_final='C', grade_reason_final='破产程序中、主体状态不明 → C 不动；若 2027 年仍在经营可复核',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='⚠ 内部信息，任何对外文字不得提及破产。'))

cards.append(dict(code='XA-C0020', name='Lieske Elektronik / Industry-Electronics', round=R, researched_at=D,
    alive='活（轻卡：未外查，沿用来源库）', summary='Vörstetten 的工业网络设备 B2B 分销商（Moxa/Hirschmann/Siemens/Weidmüller/Antaira/barox）。纯工业自动化渠道，与 Saga 的商用 PoE/L2+ 主线不交叉；STI 工业线只能当补位，且对手是 Moxa/Hirschmann 级别。',
    type_final='工业网络设备分销商', size='未查', brands_seen=['Moxa', 'Hirschmann', 'Siemens', 'Weidmüller', 'Antaira', 'barox'],
    saga_line='（STI 工业线补位，暂不推）', fit='工业自动化渠道，非主线',
    evidence=[ev('来源库', 'B2B工业网络设备专业分销(Moxa/Hirschmann/Siemens/barox)；vertrieb@industry-electronics.de', 'External Clients/CCTV-PoE/A/XA-C0020')],
    contacts={'email': 'vertrieb@industry-electronics.de', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='德国渠道型但纯工业自动化，主线不交叉 → B；等 STI 工业线有欧洲案例后再碰',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='轻卡。'))

cards.append(dict(code='XA-C0023', name='KOSATEC Computer GmbH', round=R, researched_at=D,
    alive='活（轻卡：未外查）', summary='布伦瑞克的全品类 IT 分销商（德国 Top-5 Vollsortimenter，营收数亿欧元级——据公开常识，待补证）。广线分销商上新要走厂商准入与 listing 流程，小供应商直邮进不去。',
    type_final='全品类 IT 分销商（大）', size='待补证（公开常识：数亿欧元级）', brands_seen=[],
    saga_line='—', fit='体量门槛高',
    evidence=[ev('来源库', 'Vollsortiment IT分销商；德国Top 5；info@kosatec.de', 'External Clients/CCTV-PoE/A/XA-C0023')],
    contacts={'email': 'info@kosatec.de', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='大型广线分销，info@ 直邮无效 → B 不动；若将来有德国经销商案例再经 listing 渠道申请',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='轻卡。'))

cards.append(dict(code='XA-C0024', name='Bluechip Computer AG', round=R, researched_at=D,
    alive='活（轻卡：未外查）', summary='Meuselwitz 的全品类 IT 分销商 + 自有品牌 PC/服务器厂（德国 Top-10——据公开常识，待补证）。同 KOSATEC：大广线，不走直邮。',
    type_final='全品类 IT 分销商 + 自有品牌（大）', size='待补证', brands_seen=['bluechip（自有 PC/服务器）'],
    saga_line='—', fit='体量门槛高',
    evidence=[ev('来源库', 'Vollsortiment IT分销商；德国Top 10；info@bluechip.de', 'External Clients/CCTV-PoE/A/XA-C0024')],
    contacts={'email': 'info@bluechip.de', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='大型广线分销 → B 不动',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='轻卡。'))

cards.append(dict(code='XA-C0025', name='TAROX AG', round=R, researched_at=D,
    alive='活（轻卡：未外查）', summary='Lünen 的 IT 制造商（自有品牌 PC/服务器/工作站「Made in Germany」）兼分销。网络交换机非其品牌主线。',
    type_final='IT 制造商 + 分销（自有 PC 品牌）', size='待补证', brands_seen=['TAROX（自有）'],
    saga_line='（若其自有品牌要加交换机 → OEM）', fit='弱',
    evidence=[ev('来源库', 'IT制造（服务器/工作站/PC）+ 分销；info@tarox.de', 'External Clients/CCTV-PoE/A/XA-C0025')],
    contacts={'email': 'info@tarox.de', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='交换机非主线、体量大 → B 不动',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='轻卡。'))

cards.append(dict(code='XA-C0028', name='BYTEC Bodry Technology GmbH', round=R, researched_at=D,
    alive='活', summary='腓特烈港的 IT 专业分销商（1989 起，92 人，2023 营收 ≈2.64 亿欧元），Fujitsu/Lenovo 主力分销，2020 起加 D-Link 全线。体量大、网络线刚起步且已绑 D-Link。',
    type_final='IT 专业分销商（大，Fujitsu/Lenovo/D-Link）', size='92 人；€264M（2023）', brands_seen=['Fujitsu', 'Lenovo', 'D-Link', 'Datacore', 'IBM'],
    saga_line='—', fit='大分销 + 网络线已绑台系品牌',
    evidence=[ev('implisense', 'Large enterprise · 92 employees (2023) · €263,593,751 revenue', 'https://app.implisense.com/en/companies/bytec-bodry-technology-gmbh-friedrichshafen--DEOXF195OE22', '', '2025-06-19'),
              ev('IT-Business', 'Bytec vertreibt das Netzwerkportfolio von D-Link … Schwerpunkt Business-Produkte', 'https://www.it-business.de/bytec-vertreibt-das-netzwerkportfolio-von-d-link-a-980896/', '', '2020-11-20')],
    contacts={'email': 'info@bytec.de', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='2.6 亿欧元分销商、网络线绑 D-Link → B 不动',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes=''))

cards.append(dict(code='XA-C0018', name='Almas Industries AG', round=R, researched_at=D,
    alive='活', summary='曼海姆的安防方案商（2004 起，生物识别门禁/视频/报警/除颤器，集团 300 人 8 国，德国公司 2024 营收 2,170 万欧元、123 人，母公司 Almas Industries Ltd 伦敦）。自装自卖的终端方案商，不是分销商（原库「Hikvision DACH Distributor」有误）。',
    type_final='安防方案商/集成商（自有安装队伍）', size='123 人；€21.7M（2024，德国公司）', brands_seen=['自有生物识别', '视频监控（品牌未列）'],
    saga_line='HRUI PoE / SmartByte PoE（项目配套）', fit='项目用 PoE，量可观，但采购偏厂商直供或大分销',
    evidence=[ev('官网 Über uns', 'über 300 Mitarbeiter und 30.000 Kunden in acht Ländern … Unternehmen von Butler Industries', 'https://almas-industries.de/ueber-almas-industries/', '', '2025-12-11'),
              ev('handelsregister.ai', 'Revenue 2024 21,70 Mio. €；Employees 2024 123；Konzernabschluss … ALMAS INDUSTRIES Limited in London', 'https://handelsregister.ai/en/organizations/mannheim/activities-of-holding-companies/almas-industries-ag-7c813be78ba568775f946c8ea2d1d63b')],
    contacts={'email': 'info@almas-industries.de', 'email_status': '公开；无采购口'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='终端方案商而非渠道，info@ 无采购口 → B；第 2 波若找到采购/技术负责人再首触',
    next_move={'action': '等回', 'angle': '找采购/技术负责人实名后再首触', 'model': '', 'price': '', 'window': 'DE 周四 12–14', 'when': '2026-12'}, notes=''))

cards.append(dict(code='XA-C0021', name='uniVorx GmbH (DrayTek D-A-CH)', round=R, researched_at=D,
    alive='活', summary='柏林近郊 Schönefeld 的 DrayTek DACH 独家总代（2014 年底接手，11–50 人），只卖 DrayTek 一牌（含 VigorSwitch PoE 全线），下面再分给 Comline/TwoCom/TKR 等分销。品牌独家总代不会上第二家交换机。',
    type_final='单品牌独家总代（DrayTek）', size='11–50 人', brands_seen=['DrayTek'],
    saga_line='—', fit='品牌独家，不会上第二牌',
    evidence=[ev('DrayTek.de Wir über uns', 'Die uniVorx GmbH als exklusiver DrayTek Partner für die DACH Region', 'https://www.draytek.de/wir-ueber-uns.html'),
              ev('heise', 'Neuer Generaldistributor ist dann das eigens gegründete Berliner Unternehmen Univorx', 'https://www.heise.de/newsticker/meldung/Neuer-Distributionsweg-fuer-DrayTek-Router-2499623.html', '', '2014-12-18')],
    contacts={'email': 'contact@draytek.de', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='DrayTek 独家总代，结构上不会引入第二牌交换机 → B 不动',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes=''))

cards.append(dict(code='XA-C0026', name='m2m Germany GmbH', round=R, researched_at=D,
    alive='活（官网 2026-05 更新）', summary='Wehrheim 的 M2M/IoT 方案商 + 分销（2007 起，11–50 人），LoRaWAN 全服务、Milesight 欧洲大分销之一、自研无线硬件。PoE 交换机只是 IoT 网关配套，非其品类重点。',
    type_final='IoT 方案商/分销（Milesight 渠道）', size='11–50 人', brands_seen=['Milesight', '自有 m2m Germany 硬件'],
    saga_line='HRUI PoE 入门款（网关配套）', fit='弱—中',
    evidence=[ev('官网 Manufacturer', 'As a LoRaWAN full service provider … also develops its own wireless hardware；Milesight 在列', 'https://www.m2mgermany.de/en/manufacturer/', '', '2026-05-29'),
              ev('LinkedIn', '11–50 人；Wehrheim；2007', 'https://www.linkedin.com/company/m2m-germany-gmbh')],
    contacts={'email': 'sales@m2mgermany.de', 'email_status': 'Milesight 伙伴页公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='IoT 方案商，交换机非品类重点 → B 不动',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes=''))

cards.append(dict(code='XA-C0029', name='wilkon Systems GmbH & Co. KG', round=R, researched_at=D,
    alive='活（轻卡：未外查）', summary='纽伦堡的 VdS 认证视频监控集成商（规划/安装/运营，含光纤/无线桥接/PoE 交换），自建 PoE 网络。项目型终端买家。',
    type_final='视频监控集成商（VdS Errichter）', size='未查', brands_seen=[],
    saga_line='HRUI PoE / SmartByte PoE（项目配套）', fit='项目用量小而散',
    evidence=[ev('来源库', '视频监控系统集成商（VdS认证Errichter）；网络基础设施含 PoE-Switching', 'External Clients/CCTV-PoE/A/XA-C0029')],
    contacts={'email': 'info@wilkon-sicherheitstechnik.de', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='B', grade_reason_final='集成商/安装商（目标序列第 4 位），不在渠道优先级内 → B，第 3 波后再看',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='轻卡。'))

cards.append(dict(code='XA-C0030', name='Camerawelt (Düsseldorf)', round=R, researched_at=D,
    alive='活（轻卡：未外查）', summary='杜塞尔多夫地区安防安装商，小批量终端需求。',
    type_final='安防安装商（小）', size='小', brands_seen=[],
    saga_line='—', fit='终端触点',
    evidence=[ev('来源库', '安防系统专业安装商；原库自评 C类（区域安装商，小批量）', 'External Clients/CCTV-PoE/A/XA-C0030')],
    contacts={'email': 'info@camerawelt.com', 'email_status': '公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='C', grade_reason_final='小安装商 = 终端触点 → C',
    next_move={'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': ''}, notes='轻卡。'))

# ---------- 确认 XA：首触 ----------
cards.append(dict(code='XA-C0008', name='Xortec GmbH', round=R, researched_at=D,
    alive='活（官网 2026；2026-09 媒体仍报其并购）', summary='法兰克福的 B2B 安防/网络增值分销商（2007 起，11–50 人，PE Beyond Capital 支持，2021–2022 连并柏林/慕尼黑/汉堡三家同行，全国多点），客户是 Facherrichter/经销商/电工企业；网店已卖 barox/Veracity/Hikvision 等网络与 PoE 产品，首页给出销售负责人 Michael Kahl 与 sales.fra@。',
    type_final='安防/网络增值分销商（全国多点）', size='11–50 人（LinkedIn，并购后或更多）', brands_seen=['Hikvision', 'barox', 'Veracity', 'eks'],
    saga_line='HRUI PoE 主打 + SmartByte L2+ PoE', fit='安防 VAD 正是 HRUI PoE 的主渠道；已卖多牌 PoE，加一条中性低价线阻力小；有具名销售负责人',
    evidence=[ev('官网首页', 'Lösungsanbieter für professionelle Sicherheitstechnik, Videoüberwachung und Netzwerktechnik；Hauptsitz Frankfurt；sales.fra@xortec.de；Ansprechpartner: Michael Kahl', 'https://xortec.de/'),
              ev('LinkedIn', 'Distributor von professionellen Videoüberwachungs- u. Datenkommunikationslösungen für den B2B Bereich；11–50；2007', 'https://de.linkedin.com/company/xortec-gmbh'),
              ev('Beyond Capital Partners 新闻稿', 'acquiring videotronic infosystems nord GmbH … Following … Burgenkönig Video GmbH', 'https://beyondcapital-partners.com/en/press-releasesxortec-gmbh-continues-its-market-expansion-through-next-add-on-acquisition-strengthening-its-nationwide-presence/', '', '2022-02'),
              ev('官网网络技术页', 'IP-Extender/PoE-Extender 等网络产品在售（barox、Veracity）', 'https://xortec.de/Produkte/Netzwerktechnik/IP-Extender/')],
    contacts={'email': 'sales.fra@xortec.de', 'email_status': '官网首页公开（法兰克福销售口）', 'kp': [{'name': 'Michael Kahl', 'role': '法兰克福销售联系人', 'source': '官网首页'}]},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='德国安防 VAD、多点、已卖多牌 PoE、具名销售口 → A 首触',
    next_move={'action': '首触', 'angle': '给 Facherrichter 渠道一条中性 PoE 线（非管理 24 口 300 W + 8 口 + L2+ 10G 上联）；分销 20% 档', 'model': 'STC-2224GP / STC-424XGGPM-280W', 'price': 'USD 86 / USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)', 'window': 'DE 周四 12–14', 'when': '2026-10-29'},
    draft_en={'subject': 'Neutral PoE switch line for your installer channel',
              'body': "Hello Mr. Kahl,\n\n" + INTRO_DE + " For a distributor serving Facherrichter, the line that usually moves is the one priced for the camera project rather than for the IT department.\n\nThree reference points at distributor level: " + P24U + "; " + P8U + "; and for the 10G-uplink tier " + PL2 + TAIL + " Your logo on the unit and carton is possible without MOQ.\n\nWould a PDF price sheet of the PoE range be useful for your product team, or do you prefer to start with a paid sample of the 24-port?" + SIG},
    notes='不提 Hikvision 对比。'))

cards.append(dict(code='XA-C0015', name='TURM GmbH', round=R, researched_at=D,
    alive='活（Ajax Roadshow 2026 在办）', summary='杜塞尔多夫的安防分销商/厂商（11–50 人），2018 起 Ajax 报警系统 DACH 官方分销，自有 TURM 视频/门禁品牌，姐妹公司 NSC Videotechnik（同址）出 NSC 牌摄像机/录像机/PoE 交换机（NA-P26360 = 24 口 PoE + 2 上联 + 2 SFP）。即：他们已经在用自有品牌卖进口 PoE 交换机——OEM 对象。',
    type_final='安防分销商 + 自有品牌（Ajax DACH 分销 / NSC 品牌主）', size='11–50 人', brands_seen=['Ajax', 'NSC Videotechnik（自有/姐妹）', 'UR Fog', 'TURM（自有）'],
    saga_line='HRUI PoE（贴 NSC/TURM 标，OEM 30%）', fit='已有自有品牌 PoE 交换机在售 = 现成的 OEM 需求；小公司决策链短',
    evidence=[ev('官网首页', 'Als offizieller Sicherheitstechnik-Distributor von Ajax Systems … NSC-Videotechnik und UR Fog', 'https://turm.tech/'),
              ev('官网 NSC 产品页', 'NSC Videotechnik PoE Switch, 24x PoE, 2x Uplink, 2x SFP, Bestell-Nr. NA-P26360', 'https://www.turm.tech/produkte/nsc-videotechnik'),
              ev('NSC 官网 Kontakt', 'Distributor für Fachhändler und Errichter: TURM GmbH Kappeler Straße 145 40599 Düsseldorf', 'https://nsc-videotechnik.de/Kontakt/'),
              ev('LinkedIn', 'Hersteller und Distributor für Sicherheitstechnik … 11–50', 'https://de.linkedin.com/company/turm-gmbh')],
    contacts={'email': 'info@turm.tech', 'email_status': '官网公开（Fachhändler 口）'},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='自有品牌（NSC）PoE 交换机在售的德国安防分销商 = OEM 品牌商序列第一位 → A 首触（OEM 角度）',
    next_move={'action': '首触', 'angle': 'OEM：为 NSC/TURM 品牌供 24 口 PoE（可配 2 SFP）与 8 口 PoE，含 UI/丝印/彩盒；一问：谁管 NSC 硬件采购', 'model': 'STC-2224GP（OEM）', 'price': 'OEM 档 — 首封不报价，先问采购口', 'window': 'DE 周四 12–14', 'when': '2026-10-29'},
    draft_en={'subject': 'OEM supply for the NSC PoE switch range',
              'body': "Hello,\n\nTURM sells PoE switches under the NSC Videotechnik label - the 24-port with 2 uplinks and 2 SFP, for example. That is exactly the kind of product we build for security brands in Europe: PoE switches with the brand's logo, web UI and carton, CE/RoHS/REACH, no MOQ, 8 to 48 ports, unmanaged or L2 managed, with 10G-uplink options on the managed side.\n\nIf the NSC range is sourced externally, I would be glad to send a spec-by-spec proposal against your current 24-port and 8-port models with pricing.\n\nWho on your side looks after NSC hardware sourcing - may I write to them directly?" + SIG},
    notes='不猜他们现在的供应商。'))

cards.append(dict(code='XA-C0016', name='EPS Vertriebs GmbH', round=R, researched_at=D,
    alive='活（Security Essen 2026 参展页）', summary='Havixbeck 的安防技术批发商（1980 起，11–50 人，EPS 集团），只供 Fachhandel/电工/Errichter；Dahua DACH 官方分销（2020 最佳分销商奖）、Milesight 视频、Ajax/Jablotron 报警，产品表里已有「Switche」一类。家族经营（Hövelmann 父子 + Haas 任 GF）。',
    type_final='安防技术批发商（Dahua/Milesight/Ajax/Jablotron 官方分销）', size='11–50 人', brands_seen=['Dahua', 'Milesight', 'Ajax', 'Jablotron', 'FireAngel', 'UR Fog'],
    saga_line='HRUI PoE 主打（Dahua 项目配套）+ SmartByte L2+', fit='Dahua 官方分销必配 PoE 交换机；目前只能卖 Dahua 自家 PoE，缺一条中性便宜线给 Errichter',
    evidence=[ev('官网 Dahua 页', 'offizieller Distributor für Dahua Videotechnik in Deutschland, Österreich und der Schweiz … als bester Distributor ausgezeichnet', 'https://www.eps-vertrieb.de/dahua/'),
              ev('wlw.at 产品表', 'Videotechnik | DAHUA, Milesight | Kameras … NVR/XVR, Monitore, Switche', 'https://www.wlw.at/de/firma/eps-elektronische-sicherungsanlagen-und-systeme-vertriebs-gmbh-1215232'),
              ev('LinkedIn', 'Großhandel；11–50；Havixbeck；1980', 'https://de.linkedin.com/company/eps-vertriebs-gmbh'),
              ev('handelsregister.ai', 'GF: Jürgen Hövelmann (2008), Maik Hövelmann (2023), Wilfried Haas (2003)', 'https://handelsregister.ai/de/organizations/havixbeck/grosshandel-mit-geraeten-der-unterhaltungselektronik/eps-vertriebs-gmbh-b8f9f21763acdb35268d625fd44cd07b')],
    contacts={'email': 'info@eps-vertrieb.de', 'email_status': 'Dahua 伙伴页 + 官网公开', 'kp': [{'name': 'Maik Hövelmann', 'role': 'Geschäftsführer（2023 起，二代）', 'source': 'handelsregister.ai'}]},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='德国安防批发商、官方分销多牌、已有 Switche 品类、家族小公司 → A 首触',
    next_move={'action': '首触', 'angle': '给 Errichter 的中性 PoE 线：24 口 300 W 非管理 + 8 口 + 24 口 L2 管理；分销 20%', 'model': 'STC-2224GP / STC-4424GCPM', 'price': 'USD 86 / USD 165 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)', 'window': 'DE 周四 12–14', 'when': '2026-10-29'},
    draft_en={'subject': 'PoE switches for your Errichter partners - neutral line, distributor pricing',
              'body': "Hello Mr. Hövelmann,\n\n" + INTRO_DE + " For a video-surveillance wholesaler the useful addition is usually a neutral PoE line that the installer can put under any camera brand without a price discussion.\n\nReference points at distributor level: " + P24U + "; " + P8U + "; " + P24M + TAIL + " Watchdog/PoE-reset and 250 m extend mode on the unmanaged units, VLAN/QoS/ERPS on the managed.\n\nWould you like the PoE price sheet, or shall I start with a paid sample of the 24-port for your technicians?" + SIG},
    notes='不点名 Dahua PoE 比价。'))

cards.append(dict(code='XA-C0017', name='i-Alarmsysteme GmbH', round=R, researched_at=D,
    alive='活（2025-10 搬新址 Alte Gießerei 12, Erkrath）', summary='奥地利 Weikersdorf 总部、DACH 5 个点、50+ 人的报警/视频/门禁批发商（1980 起），德国分部在 Erkrath；Dahua 官方分销（Excellent Distributor 2020），并把中国品牌 Wi-Tek 的 PoE 交换机/AP 作为自家「网络与传输技术」线在卖——说明已接受中国 PoE 品牌直供。',
    type_final='安防批发商（DACH，Dahua 分销 + 自选中国 PoE 品牌）', size='>50 人，5 个点', brands_seen=['Dahua', 'Wi-Tek', 'Ajax', '其他报警/门禁'],
    saga_line='HRUI PoE（对标其 Wi-Tek 线）+ SmartByte L2+', fit='已在卖中国 PoE 品牌，采购路径现成；DE 分部有 vertrieb@ 口',
    evidence=[ev('官网首页', 'Wi-Tek Netzwerk- & Übertragungstechnik — PoE-Switches, Wireless Access Points & mehr', 'https://www.i-alarmsysteme.de/', '', '2025-11-04'),
              ev('官网 Unternehmen', '5 Standorte in Österreich, Deutschland & Schweiz；> 50 MitarbeiterInnen', 'https://www.i-alarmsysteme.de/ueber-uns/unternehmen/'),
              ev('Dahua 分销伙伴页', 'i-Alarmsysteme GmbH … Dahua Execllent Distributor 2020；vertrieb@i-alarmsysteme.de', 'https://www.dahuasecurity.com/de/partners/DistributionPartner?id=all'),
              ev('官网博客', 'i-Alarmsysteme Deutschland ist umgezogen! … Alte Gießerei 12, 40699 Erkrath', 'https://www.i-alarmsysteme.de/blog/i-Alarmsysteme-Deutschland-ist-umgezogen', '', '2025-10-31')],
    contacts={'email': 'vertrieb@i-alarmsysteme.de', 'email_status': 'Dahua 伙伴页 + 官网公开（德国分部销售口）'},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='DACH 安防批发商，已自选中国 PoE 品牌在卖 → 采购路径现成 → A 首触',
    next_move={'action': '首触', 'angle': '第二条 PoE 线：24 口 300 W 非管理 + 8 口 + L2+ 10G 上联，可贴自家标；分销 20%', 'model': 'STC-2224GP / STC-424XGGPM-280W', 'price': 'USD 86 / USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)', 'window': 'DE 周四 12–14', 'when': '2026-10-29'},
    draft_en={'subject': 'A second PoE switch line for your Facherrichter, own label possible',
              'body': "Hello,\n\n" + INTRO_DE + " You already carry a dedicated network and transmission line for installers, so I will keep this to numbers.\n\nAt distributor level: " + P24U + "; " + P8U + "; " + PL2 + TAIL + " Units can carry the i-Alarmsysteme logo and your article numbers from the first order.\n\nIs a second PoE source of interest for your 2027 line card, or is the current one exclusive?" + SIG},
    notes='不提 Wi-Tek 名字。'))

cards.append(dict(code='XA-C0019', name='MICHAEL AG (MichaelTelecom)', round=R, researched_at=D,
    alive='活（2026-05-01 二代 Magnus Michael 任董事长）', summary='下萨克森 Bohmte 的 ITK 分销商（1984 起，家族企业，2024 更名 Michael AG），Hikvision「第一代」分销商、2025-08 升为德国战略分销商；产品线含网络组件（工业/车载/标准交换机、路由器、PoE 注入器、UPS）、TK 设备与网络业务，面向经销商/系统商。',
    type_final='ITK 分销商（Hikvision 战略分销 + 网络组件）', size='中型家族企业（员工数待补证）', brands_seen=['Hikvision', 'HiWatch', 'EZVIZ', '多牌 TK/网络'],
    saga_line='SmartByte L2+ PoE + HRUI PoE（视频项目配套 + 通用网络组件线）', fit='Hikvision 战略分销每个视频项目都要 PoE；网络组件线已含多种交换机，加一条中性 PoE/L2+ 顺手；家族企业链短',
    evidence=[ev('Hikvision 官方分销名录', 'MICHAEL AG Die MICHAEL AG ist HIKVISION-Distributor der ersten Stunde；info@michael-ag.de', 'https://www.hikvision.com/en/Partners/channel-partners/find-a-distributor/', '', '2026-04-01'),
              ev('官网新闻稿', 'MICHAEL AG zum strategischen Distributor für den deutschen Markt ernannt', 'https://www.michael-ag.de/pressemitteilung-michael-ag-und-hikvision-vertiefen-partnerschaft', '', '2025-08-05'),
              ev('官网视频监控页', 'Netzwerkkomponenten wie Industrie-, Fahrzeug- und Standardswitche und Router, Netzwerkkabel, PoE-Injektoren', 'https://www.michael-ag.de/videoueberwachung'),
              ev('ChannelPartner', 'Magnus Michael übernimmt zum 1. Mai 2026 den Vorstandsvorsitz', 'https://www.channelpartner.de/article/4160956/die-michael-ag-bekommt-einen-neuen-chef.html', '', '2026-04-20')],
    contacts={'email': 'info@michael-ag.de', 'email_status': 'Hikvision 名录 + 官网公开', 'kp': [{'name': 'Magnus Michael', 'role': 'Vorstandsvorsitzender（2026-05-01 起）', 'source': 'ChannelPartner/CRN'}, {'name': 'Helmuth Stegemann', 'role': 'Produktmanager Videoüberwachung（2018 报道）', 'source': '官网 2018 奖项稿'}]},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='德国 ITK 分销商 + 视频监控战略分销 + 已有交换机品类 → A 首触（写给视频产品经理）',
    next_move={'action': '首触', 'angle': '视频监控项目配套的 PoE：24 口 L2+ 10G 上联 + 24 口非管理 300 W + 8 口；分销 20%', 'model': 'STC-424XGGPM-280W / STC-2224GP', 'price': 'USD 170 / USD 86 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)', 'window': 'DE 周四 12–14', 'when': '2026-10-29'},
    draft_en={'subject': 'PoE switches for your video-surveillance resellers',
              'body': "Hello,\n\n" + INTRO_DE + " Your network-components line already lists several switch types; what we add is a PoE line priced for camera projects and sold at distributor level.\n\nReference points: " + PL2 + "; " + P24U + "; " + P8U + TAIL + " Voice/camera VLAN, PoE watchdog and 250 m extend mode included where relevant.\n\nCould you forward this to the product manager for video surveillance, or tell me who that is so I can send the full price sheet directly?" + SIG},
    notes='不提 Hikvision 自家交换机。'))

cards.append(dict(code='XA-C0022', name='ASSMANN Electronic GmbH (DIGITUS)', round=R, researched_at=D,
    alive='活（网店 2026 在售多款 PoE 交换机）', summary='Lüdenscheid 1969 年起的 IT 基础设施品牌商（ASSMANN 集团，201–500 人，11 国分公司），自有品牌 DIGITUS 覆盖机柜/布线/网络，网店在售 DIGITUS 牌 PoE 交换机全线（8 口 10" 非管理 DN-95317、8 口 L2+ 管理 PoE DN-95331、工业 16+2 L2 PoE DN-651159 等）。这些有源产品是外采贴牌——典型 OEM 品牌商。',
    type_final='IT 基础设施品牌商（DIGITUS，OEM 外采）', size='201–500 人；11 国子公司', brands_seen=['DIGITUS（自有）'],
    saga_line='SmartByte / HRUI OEM（30% 档）', fit='目标序列第一位「OEM 品牌商」，且已在卖同类 PoE 交换机；难点是找到有源产品的产品经理/采购',
    evidence=[ev('DIGITUS 网店', 'DIGITUS 10" Gigabit 8-Port L2+ Managed PoE+ Switch, DN-95331', 'https://de.assmann.shop/en/Data-Network-Technology/Active-Network-Components/Network-Switches/10-Network-Switches/10-Gigabit-8-Port-L2-Managed-PoE-Switch.html'),
              ev('DIGITUS 网店', 'DIGITUS Industrial 16+2-Port L2 Managed Gigabit Ethernet PoE Switch, DN-651159', 'https://de.assmann.shop/en/Data-Network-Technology/Active-Network-Components/Network-Switches/Industrial-Network-Switches/Industrial-16-2-port-L2-managed-Gigabit-Ethernet-PoE-switch.html'),
              ev('XING 公司页', 'ASSMANN Electronic GmbH … 1969 … Eigenmarke DIGITUS mit Niederlassungen in elf verschiedenen Ländern', 'https://www.xing.com/pages/assmann', '', '2023-05-12'),
              ev('来源库', '201-500 员工；info@assmann.com；LinkedIn ASSMANN GROUP', 'External Clients/CCTV-PoE/A/XA-C0022')],
    contacts={'email': 'info@assmann.com', 'email_status': '公开总口；有源产品的产品经理待找（LinkedIn）'},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='自有品牌在卖外采 PoE 交换机的德国品牌商 = OEM 序列第一位 → A 首触（先问对口人）',
    next_move={'action': '首触', 'angle': 'OEM：对 DIGITUS 现有 8/16/24 口 PoE 与 L2+ 管理款逐项对标供货，一问：有源产品采购/PM 是谁', 'model': 'STC-424XGGPM-280W（OEM）/ HRUI 8–24 口', 'price': 'OEM 档 — 首封不报价', 'window': 'DE 周四 12–14', 'when': '2026-10-29'},
    draft_en={'subject': 'OEM supply for DIGITUS PoE switches - 8 to 48 ports, L2+ and 10G uplinks',
              'body': "Hello,\n\nWe supply PoE and L2+ switches to European infrastructure brands under the brand's own label: 8- to 48-port PoE+/PoE++, unmanaged and L2/L2+ managed (Marvell on the L2+ line), 1G/2.5G/10G uplinks, 10-inch and 19-inch, plus DIN-rail industrial models. CE/RoHS/REACH documentation, custom UI, firmware branding and carton artwork are standard; no MOQ on first orders.\n\nSince DIGITUS already carries a full PoE switch range, a model-by-model proposal against your current 8-, 16- and 24-port items would be the quickest way to compare.\n\nWho is the right person for active network components - product management or purchasing - so I can send the proposal directly?" + SIG},
    notes='KP 待找：LinkedIn「ASSMANN Produktmanager aktive Netzwerkkomponenten」。'))

cards.append(dict(code='XA-C0013', name='WAV, LLC', round=R, researched_at=D,
    alive='活（2026-09 AFL 战略分销稿）', summary='伊利诺伊 Aurora 的北美 WISP/ISP 设备分销商（1990 起，51–200 人，$40.9M，4 个美国仓 + 加拿大 MBSI WAV），卖 Cambium/Ubiquiti/TP-Link/MikroTik 与光纤设备，2024-11 收购 ISP Supplies。营销 EVP Zach Hubeck 实名邮箱已公开。',
    type_final='WISP/ISP 设备分销商（北美）', size='51–200 人；$40.9M', brands_seen=['Cambium', 'Ubiquiti', 'TP-Link', 'MikroTik', 'AFL', 'Clearfield', 'Altowav'],
    saga_line='SmartByte L2+ PoE + CENTEC 10G/25G 汇聚（WISP 塔站/机房）', fit='WISP 渠道的管理型 PoE 与 10G 汇聚是刚需；分销商有仓有渠道；有实名 EVP',
    evidence=[ev('LinkedIn', 'WAV, LLC；51–200；Aurora IL；1990', 'https://www.linkedin.com/company/wav-inc'),
              ev('RocketReach', 'Revenue $40.9M；72 人', 'https://rocketreach.co/wav-llc-profile_b5c70e67f42e0d32'),
              ev('官网新闻', 'WAV … completed an agreement to acquire ISP Supplies', 'https://www.wavonline.com/wav-announces-acquisition-of-isp-supplies-to-expand-distribution-footprint', '', '2024-11-11'),
              ev('PRWeb', 'said Zach Hubeck, Executive Vice President of Marketing at WAV', 'https://www.prweb.com/releases/wav-and-mbsi-wav-named-among-afls-strategic-distribution-partners-in-the-us-and-canada-302882264.html', '', '2026-09-17')],
    contacts={'email': 'zachh@wavonline.com', 'email_status': '来源库记为公开（营销 EVP）；备用 info@wavonline.com', 'kp': [{'name': 'Zach Hubeck', 'role': 'EVP Marketing', 'source': 'PRWeb 2026-09 + 来源库'}, {'name': 'Norm Dumbroff', 'role': 'CEO/Owner', 'source': 'D&B'}]},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='美国 WISP 渠道分销商、多仓、实名 EVP → A 首触',
    next_move={'action': '首触', 'angle': 'WISP 渠道的 L2+ PoE 接入 + Centec 10G 汇聚，分销 20%；一问：新品牌准入流程', 'model': 'STC-424XGGPM-280W / STH-2C24XF-HSI', 'price': 'USD 170 / USD 1,500 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)', 'window': 'US 周三 08–10 当地', 'when': '2026-10-28'},
    draft_en={'subject': 'L2+ PoE and 10G aggregation switches for WAV\'s WISP partners',
              'body': "Hi Zach,\n\nSaga Telecom supplies switches to ISP and WISP distributors - Marvell-based L2+ PoE access switches and Centec-based L3 10G/25G/100G aggregation - under our label or the distributor's own, FCC/CE.\n\nTwo reference points at distributor level: STC-424XGGPM-280W, 24 x GE PoE+ (280 W) + 4 x 10G SFP+, L2+ with ERPS ring and SNMPv3, USD 170; STH-2C24XF-HSI, 24 x 10G SFP+ + 2 x 100G, full L3 (OSPF/BGP, VXLAN), dual PSU, USD 1,500. Both EXW Shenzhen, snapshot 2026-10-27, valid 15 days, 12-month warranty.\n\nWhat is WAV's process for evaluating a new switch vendor - a line review with your product team, or samples first?" + SIG},
    notes=''))

cards.append(dict(code='XA-C0003', name='CCTVburada (Istanbul)', round=R, researched_at=D,
    alive='活（网店 2025-12 博客）', summary='伊斯坦布尔 Kartal 的安防经销/安装商 + 网店，Hikvision 授权经销商，网店有「24 Port Switchler」类目在卖 Ruijie Reyee 管理型交换机（5,500 TL），另做全市摄像头安装服务。小型经销 + 安装，土耳其主攻区。',
    type_final='安防经销商/安装商 + 网店（TR）', size='小', brands_seen=['Hikvision', 'Ruijie Reyee', 'Dahua', 'UNV', 'TP-Link'],
    saga_line='HRUI PoE 入门款（网店上架）', fit='网店已上架中国品牌交换机，加 HRUI 8/16/24 口 PoE 顺手；但体量小、偏安装',
    evidence=[ev('网店博客', 'We serve as an authorized reseller and dealer for Hikvision solutions … Network switch, PoE switch models', 'https://www.cctvburada.com/en/blogs/markalar/hikvision-turkiye-distributoru-yetkili-bayi-ve-servisi', '', '2025-12-04'),
              ev('网店类目', '24 Port Switchler：Ruijie Reyee RG-ES224GC … 5,500.00TL', 'https://www.cctvburada.com/collections/24-port-switchler')],
    contacts={'email': 'info@cctvburada.com', 'email_status': '官网公开'},
    touch_status='未发信', saga_overlap='无',
    grade_final='A', grade_reason_final='土耳其主攻区、网店在卖中国品牌交换机 → A，但体量小，首触排下周 TR 窗口',
    next_move={'action': '首触', 'angle': '网店加 HRUI PoE 8/16/24 口（非管理）与 24 口 L2+；一问：是否进口自采', 'model': 'STC-2224GP / STC-028GP', 'price': 'USD 86 / from USD 28 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)', 'window': 'TR 周四 10–12', 'when': '2026-11-05'},
    draft_en={'subject': 'PoE switches for your web shop - 8/16/24 ports, CE',
              'body': "Hello,\n\nSaga Telecom supplies PoE switches to security dealers and distributors in Türkiye and Europe, under our label or yours. Your shop already lists 24-port switches, so a PoE line for camera installations may fit next to them.\n\nReference points: " + P24U + "; " + P8U + "; 16-port PoE+ USD 63" + TAIL + " Extend mode to 250 m and PoE watchdog on all unmanaged units.\n\nDo you import directly, or do you buy switches through a local distributor? Either way I can send the full PoE price list." + SIG},
    notes=''))

for c in cards:
    put(c)
print('cctv cards', len(cards))
