# -*- coding: utf-8 -*-
"""第 102 批（T29-U95，2026-10-28）DE 4 + GB 4 + PL 1 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 102
F = '2026-10-28'

# ---------------- DE 4 ----------------
put('SB-791', key='de', batch=B, name='Wachendorff Prozesstechnik GmbH & Co. KG（wachendorff-prozesstechnik.de；Geisenheim / Rheingau）— 1978-11-17 由 Rolf Wachendorff 创办的工业电子进口 / 分销商（面板 PC、远程维护、数据记录、协议转换、工业网络组件；「Alles aus einer Hand」、原机测试）；Amtsgericht Wiesbaden HRA 7403（普通合伙人 Wachendorff GmbH HRB 20054）；GF 兼所有人 Dipl.-Wirtsch.-Ing. Robert Wachendorff；集团 >110 人、>€25M（2022）；研究档联系 kontakt@segno.de（关联域）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（Wachendorff Prozesstechnik GmbH & Co. KG；Industriestraße 7, 65366 Geisenheim；+49 6722 996520；Amtsgericht Wiesbaden HRA 7403；USt-ID DE113657232；Komplementär Wachendorff GmbH, Amtsgericht Wiesbaden HRB 20054；Geschäftsführer Robert Wachendorff；WEEE DE 79288157）+ wer-zu-wem（Robert Wachendorff — Geschäftsführer & Inhaber）+ Wachendorff Group 历史（1978-11-17 Rolf Wachendorff 创办，进口工业电子；1985 两子 Dr. Peter 与 Robert 加入）+ 集团简介 PDF 2021（>110 人；2022 营收 >€25M；家族经营）+ industrial-production（160 人；€28M；GF Robert / Dr. Peter Wachendorff）+ LinkedIn（1978；51–200；Geisenheim）+ 关联 Wachendorff Automation GmbH & Co. KG（HRA 8377，编码器）',
    url='https://www.wachendorff.com/legal-notice/',
    number='HRA 7403（Amtsgericht Wiesbaden）· Komplementär Wachendorff GmbH HRB 20054 · USt-ID DE113657232', status='Aktiv', incorporated='1978-11-17', company_type='GmbH & Co. KG（家族企业；GF / Inhaber Robert Wachendorff）',
    sic=['工业电子进口与分销（面板 PC、HMI、远程维护、数据记录、协议 / 信号转换器、工业网络组件；原机测试、一站式）', '集团：Wachendorff Automation（编码器制造）'],
    address='Industriestraße 7, 65366 Geisenheim', accounts='集团 >€25M（2022，自报）', accounts_due='—', size_band='中型（集团 >110 人）',
    officers=['Robert Wachendorff — Geschäftsführer & Inhaber（Dipl.-Wirtsch.-Ing.）= 拍板人', 'Dr. Peter Wachendorff — 集团管理层', 'kontakt@segno.de — 研究档联系（关联域；无具名 KP）'], psc='Wachendorff 家族', charges='', prev_names=[],
    lines=['**老牌工业电子进口分销（目标客户序列「有进口经验者」）+ 表内「电口」「可以着重跟一下」→ 分销 20%，可谈 Wachendorff 标 OEM 30%**：STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM / STI-0240GE（导轨宽温，配其面板 PC / 网关线）；B BIG，**加厚**（工业线对标价表 + 原机测试样机付费）',
           '收件人改官方 wp@ / vertrieb@ 点名 Herrn Robert Wachendorff + Produktmanagement Industrielle Kommunikation；群发 8 次已打开 → 第二次触达换主题「DIN-rail managed switches for your industrial portfolio — tested samples, 3-year warranty」；发信窗口 Thu 12–14 CET；升 A 候选（回信即 A）'],
    notes='分销 20% / 可谈贴标；B BIG；加厚；升 A 候选。')
put('SB-411', key='de', batch=B, name='Flöter SDT | Sicherheit, Detektei und Technik GmbH（floeter-sicherheit.de / floeter-sdt.de；Taucha bei Leipzig）— 2021-04-28 登记的保安服务 / 侦探 / 安防技术公司（报警、门禁；区域经理制）；Amtsgericht Leipzig HRB 38796；资本 €25,000；**GF 兼唯一股东 Daniel Flöter = 研究档 KP d@ 本人**；另设 SignalTech GmbH（2025-01-02，GF Daniel Flöter）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（Dewitzer Straße 77H, 04425 Taucha；buero@floeter-sdt.de；Geschäftsführer Daniel Flöter；Amtsgericht Leipzig HRB 38796）+ Creditreform（GmbH；HRB 38796 Leipzig；wirtschaftsaktiv；1 GF；1 Gesellschafter；最后变更 2021-09-15）+ companyhouse（Gesellschaftsvertrag 2021-04-22；Stammkapital €25,000；Zweck：Detektivbüro、Sicherheitsdienst、Bewachung；Daniel Flöter alleinvertretungsberechtigt 2021-04-28 起，Gesellschafter 2024-02 起）+ Northdata（2021-04-28 登记；Daniel Flöter 另任 SignalTech GmbH GF，2025-01-02 登记）+ cylex（团队：Melanie Zimmermann 助理、Sebastian Saupe / Ronny Dietze 区域经理、Lukas Diwisch 招聘 / 销售）',
    url='https://www.companyhouse.de/Floeter-SDT-Sicherheit-Detektei-und-Technik-GmbH-Taucha',
    number='HRB 38796（Amtsgericht Leipzig）', status='Aktiv（2026-01 年报已公示）', incorporated='2021-04-22（公司合同；登记 2021-04-28）', company_type='GmbH（资本 €25,000；Daniel Flöter 唯一股东）',
    sic=['保安服务 / 侦探 / 安防技术安装（报警、门禁、Doorman）'],
    address='Dewitzer Straße 77h, 04425 Taucha', accounts='—', accounts_due='—', size_band='微型 / 小型（人数未取）',
    officers=['Daniel Flöter — Geschäftsführer / Alleingesellschafter = **研究档 KP d@ 本人**（另任 SignalTech GmbH GF）'], psc='Daniel Flöter', charges='', prev_names=[],
    lines=['**保安服务为主、安防技术为辅 + 表内 7 次跟进无回复** → **集成商 25% 低优先，一页纸最后一次后 `when=不动`**：STC-028GP / STC-228GP（报警 / 门禁小项目 PoE）',
           '老板本人收件但长期不回 → 最后一次换主题「one-page: PoE switches for alarm & access installs — MOQ 1」；发信窗口 Thu 12–14 CET；若 SignalTech GmbH 为其技术线可另开一线'],
    notes='集成商 25% 低优先；KP = GF 本人；一页纸一次后不动。')
put('SB-611', key='de', batch=B, name='Avanis GmbH（avanis.de；Bielefeld，Technologiepark Meisenstraße）— 2003 年成立的有源网络设备销售与 WLAN 规划专业商（「Netzwerk-Architekten」：交换机到 RTLS，Ekahau 测量，医院场景；站内 Edgecore / Fortinet）；Amtsgericht Bielefeld HRB 37834；资本 €70,000；LEI 529900I6QC9S0TFPUY37；**GF 兼股东 Thomas Passlack = 研究档 KP tpasslack@ 本人**（+ GF 兼股东 Paul Peter Kaiser）；8–19 人', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（Avanis GmbH；Meisenstraße 79a, 33607 Bielefeld；+49 521 26012 0；GF Thomas Passlack, Paul Peter Kaiser；Amtsgericht Bielefeld HRB 37834；USt-ID DE813687094）+ 官网 Über uns / Team（2003 成立；「Spezialisten im Vertrieb von aktiver Netzwerktechnik」；新楼 Technologiepark；Paul Kaiser / Thomas Passlack Geschäftsführung）+ implisense（Founded 2003-04-22；Share capital €70,000；LEI 529900I6QC9S0TFPUY37；Small enterprise）+ companyhouse（两 GF 自 2003-05-15 单独代表；地址变更 Am Fichtenbrink 38 → Meisenstraße 97a → 79a）+ firmendatenbanken（Gesellschafter Paul Peter Kaiser、Thomas Passlack）+ wlw（10–19 人）+ RocketReach（8 人）',
    url='https://avanis.de/impressum',
    number='HRB 37834（Amtsgericht Bielefeld）· LEI 529900I6QC9S0TFPUY37 · USt-ID DE813687094', status='Aktiv', incorporated='2003-04-22（公司合同；登记 2003-05-15）', company_type='GmbH（资本 €70,000；两 GF 即两股东）',
    sic=['有源网络设备销售（交换机 / WLAN / 安全）+ WLAN 规划测量（Ekahau）+ RTLS；医院等项目'],
    address='Meisenstraße 79a, 33607 Bielefeld', accounts='—', accounts_due='—', size_band='微型 / 小型（8–19 人）',
    officers=['Thomas Passlack — Geschäftsführer / Gesellschafter = **研究档 KP tpasslack@ 本人**', 'Paul Peter Kaiser — Geschäftsführer / Gesellschafter（pkaiser@）', 'Valentin Kaiser — 研究档 KP（职务未核）'], psc='Passlack / Kaiser', charges='', prev_names=[],
    lines=['**网络设备经销 + 已用 Edgecore（OEM 低价定位）+ 老板本人收件 → 分销 20%（项目集成商 25% 两可）**：STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM（楼宇 / 医院 PoE 接入，对标 Edgecore ECS-4650 价）+ STC-110XGE；B BIG，**加厚**（对标价表）',
           '表内 1 次跟进无回复 → 第二次触达换主题「an alternative access-switch line beside your current OEM brand — Marvell L2+, 15-day quote」（不点名 Edgecore）；发信窗口 Thu 12–14 CET；升 A 候选（回信即 A）'],
    notes='分销 20% / 集成商 25%；KP = GF 本人；B BIG；加厚；升 A 候选。')
put('SB-626', key='de', batch=B, name='Vision Dynamics ElectronX（visiondynamics.de；德国）— 研究档 KP Joseph（joseph.nb@）、enquiries@；表内「之前谈过」；**本轮 1 次检索仅命中 Vision Dynamics GmbH（vision-dynamics.de，Oberhaching bei München，Amtsgericht München HRB 235057，工业自动化工程咨询，GF Christian Zimmermann）—— 域名与业务均不符，疑同名他户，不采 → 未坐实**', iso='DE', fetched=F,
    source='DE · 1 次检索（关键词 Vision Dynamics ElectronX visiondynamics.de Impressum）→ 返回 vision-dynamics.de Impressum（Vision Dynamics GmbH；Grünwalder Weg 32, 82041 Oberhaching；GF Christian P. Zimmermann；Amtsgericht München HRB 235057；USt-ID DE313379909）+ implisense / Northdata（2017-07-24 成立；资本 €25,000；经营范围：工业自动化项目管理 / 系统设计 / 软件集成）—— 电子贸易「ElectronX」与 enquiries@ 英式用语均对不上；按「1 次未中即停」规则不再追',
    url='https://visiondynamics.de/',
    number='未坐实（visiondynamics.de 主体未取；HRB 235057 为同名他户，不采）', status='站点快照仅标题（研究档）', incorporated='未取', company_type='未取',
    sic=['电子 / 网络产品贸易（研究档待核）'],
    address='德国（门牌未取）', accounts='—', accounts_due='—', size_band='未取',
    officers=['Joseph（姓未取）— 研究档 KP joseph.nb@（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**未坐实** → 表内「之前谈过」仍值一封：一页纸（STC-228GP / STC-2224GP / STI-144GP）点回旧话题；不加厚；下轮补项：站点 Impressum / whois 法人名',
           '收件人 joseph.nb@ 抄 enquiries@；发信窗口 Thu 12–14 CET'],
    notes='未坐实（1 次未中，同名他户不采）；一页纸。')

# ---------------- GB 4 ----------------
put('SB-040', key='gb', batch=B, name='4DEMAND LTD（4demand.co.uk；London N3）— 2022-12-30 注册的微型 IT / 贸易公司（SIC 46900 非专业批发 + 62012/62020/62090 软件 / IT 咨询；自述由波斯湾地区多家企业合并而来：IT 服务、CCTV / 报警、设备供应与进出口）；Companies House 14564199；资本 £1；**唯一董事 / PSC Mohsen Tavakoli Zaniani（*1992-02）**；英国 Skilled Worker 担保资质；研究档采购联系 Mr. Ari（procurement@）', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 14564199（4DEMAND LTD；Active；Private limited company；Incorporated 2022-12-30；注册地 227 Nether Street, London N3 1NT（2024-10-23 由 80 Golders Green Road NW11 8LN 迁入）；SIC 46900 / 62012 / 62020 / 62090；董事 TAVAKOLI ZANIANI, Mohsen（2022-12-30 起，British，*1992-02）；PSC 同人 75–100%；NEWINC 股本 £1；CS01 2025-01-03）+ Endole（1 董事 / 1 股东 / 1 PSC；020 3576 1986）+ sponsorlicensechecker（UK 担保人名册 Skilled Worker，SIC 46900）',
    url='https://find-and-update.company-information.service.gov.uk/company/14564199',
    number='Companies House 14564199', status='Active（CS01 2025-01-03）', incorporated='2022-12-30', company_type='Private limited company（资本 £1；单一董事 / PSC）',
    sic=['46900 — 非专业批发', '62012 / 62020 / 62090 — 软件开发 / IT 咨询 / 其他 IT 服务'],
    address='227 Nether Street, London N3 1NT（住宅 / 小办公；前址 80 Golders Green Road NW11 8LN）', accounts='—（微型豁免）', accounts_due='—', size_band='微型（<10 人；营业额 <£1M）',
    officers=['Mohsen Tavakoli Zaniani — Director / PSC（*1992-02；British）= 拍板人', 'Mr. Ari — 采购（表内 procurement@）= 收件人'], psc='Mohsen Tavakoli Zaniani（75–100%）', charges='', prev_names=[],
    lines=['**£1 资本微型贸易 / 转口公司（面向海湾）→ 采购型 small：一页纸 + 100% 预付、不赊、不备货**：STC-028GP / STC-228GP / STC-2224GP 按单报价；**目的地与最终用户按出口合规核对（海湾转口）**',
           '收件人 procurement@ 点名 Mr. Ari 抄 Director；表内已有采购联系 → 首信一页纸即止；发信窗口 Thu 12–14 GMT'],
    notes='采购型 small；100% 预付；一页纸；转口合规核对。')
put('SB-590', key='gb', batch=B, name='CARRITECH LTD（carritech.com / optics.carritech.com；London 注册，运营 UK + Madrid）— 2010-05-20 成立的运营商级电信设备备件供应 / 资产管理 / 翻新维修 / WEEE 回收商（延长旧网络寿命；光模块 / SFP 为主，MC 为副线）；Companies House 07260202；SIC 61900；资本 £200；11 人（2025 账）；董事 Bruce Iain Sutherland（创始人，2010）+ Miguel Asín Barcos（2011；PSC；Sales Director，Madrid）', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 07260202（CARRITECH LTD；Active；Private limited company；Incorporated 2010-05-20；注册地 124 City Road, London EC1V 2NX（虚拟办公地址）；CH01 / PSC04 2025–2026 Miguel Asin Barcos 变更）+ companiesintheuk（SIC 61900；资本 £200；11 人 2025 账（2024 为 8）；董事 Miguel ASIN BARCOS 2011-04-12、Bruce Iain SUTHERLAND 2010-06-16；Total Exemption Full）+ Endole（微型；2 董事 / 2 股东 / 2 PSC；Sutherland 58 岁）+ 官网 Company（2010 由 Miguel Asín 与 Bruce Sutherland 创办；备件供应、资产管理、远程支持、硬件支持、WEEE 回收；UK + Spain）+ LinkedIn（11–50；光模块 / SFP、翻新维修、legacy telecoms）+ prospeo（营收约 $1.45M；Miguel Asin Barcos — Sales Director）',
    url='https://find-and-update.company-information.service.gov.uk/company/07260202',
    number='Companies House 07260202', status='Active（2025 账已报）', incorporated='2010-05-20', company_type='Private limited company（资本 £200；两创始董事即 PSC）',
    sic=['61900 — 其他电信活动（运营商旧设备备件供应、资产管理、翻新维修、WEEE 回收；光模块 / SFP 销售）'],
    address='124 City Road, London EC1V 2NX（注册 / 虚拟）；运营 UK + Madrid', accounts='第三方营收约 $1.45M（仅作区间）', accounts_due='—', size_band='微型 / 小型（11 人）',
    officers=['Bruce Iain Sutherland — Director / 创始人（2010）', 'Miguel Asín Barcos — Director / PSC / Sales Director（2011；Madrid）', 'Yura Saskevych — Global Account Director（Madrid）'], psc='Sutherland / Asín Barcos', charges='', prev_names=[],
    lines=['**翻新备件商（同行·翻新类）+ 表内 2 次跟进无回复** → **一页纸一次后 `when=不动`**：仅 MC / 光口小件（STI-144GP / STC-228GP）配其光模块业务；不加厚',
           '收件人 contact@ 点名 Sales Director；发信窗口 Thu 12–14 GMT（马德里团队 CET）'],
    notes='翻新商 → 一页纸一次后不动。')
put('SB-264', key='gb', batch=B, name='TIER1 DATA SYSTEMS LIMITED（tier1ds.com；London W1W 商务中心）— 2018-10-31 注册的 IT 硬件 / 备件经销微型公司（SIC 46520 电子电信设备批发 + 47910 网络零售；Cisco / Juniper / Fortinet / Huawei 品牌货、刀片服务器、配置服务；阿里巴巴 RFQ「Cisco Switch」）；Companies House 11652776；VAT GB311899586；1 人；**董事 / 创始人 Mohammad Samir Jamjam（印度籍，*1990-05）= 研究档 KP「Sameer JamJam」sales@ 本人**；历任多名印度籍董事进出', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 11652776（TIER1 DATA SYSTEMS LIMITED；Active；Private limited company；Incorporated 2018-10-31；注册地 167-169 Great Portland Street, 5th Floor, London W1W 5PF（前址 85 Great Portland Street, First Floor W1W 7LT）；SIC 46520 / 47910；9 名董事 / 7 名已辞；现任 JAMJAM, Mohammad Samir（2018-10-31 起）、KHATRI, Kajal（2026-07-07 起）；已辞 Antelawala / Katara（2025-10-04）/ Kothari 等）+ Endole（VAT GB311899586；2 股东 / 2 PSC；Jamjam 创始人，Indian，36 岁；Khatri 33 岁 首任董事）+ GlobalDatabase（1 人；CS01 2023-10-31）',
    url='https://find-and-update.company-information.service.gov.uk/company/11652776',
    number='Companies House 11652776 · VAT GB311899586', status='Active（新董事 2026-07-07）', incorporated='2018-10-31', company_type='Private limited company（微型；印度籍董事；商务中心注册地）',
    sic=['46520 — 电子与电信设备及零件批发（品牌 IT 硬件 / 备件经纪）', '47910 — 邮购 / 网络零售'],
    address='167-169 Great Portland Street, 5th Floor, London W1W 5PF（商务中心；非实体仓）', accounts='—（微型）', accounts_due='—', size_band='微型（1 人）',
    officers=['Mohammad Samir Jamjam — Director / 创始人 / PSC（*1990-05；Indian）= **研究档 KP sales@ 本人**', 'Kajal Khatri — Director（2026-07 起）'], psc='Jamjam + 1', charges='', prev_names=[],
    lines=['**品牌货经纪（Cisco 为主）+ 商务中心壳 + 1 人** → **采购型 small：一页纸 + 100% 预付、不赊**：STC-2224GP / STC-4424GCPM / STC-110XGE 按单报价；不加厚',
           '收件人 sales@（= 老板本人）；表内无跟进 → 首信一页纸即止；发信窗口 Thu 12–14 GMT'],
    notes='采购型 small；100% 预付；一页纸；KP = 董事本人。')
put('SB-805', key='gb', batch=B, name='CCTVSpot.co.uk = **MB Vision Ltd.（保加利亚 Plovdiv）**— 2012 年起的 CCTV 设备进口 / 在线分销商（Hikvision / Dahua 授权经销、Ajax、Wi-Tek；欧洲发货）；英国站仅为销售前台（UK VAT GB411290538），总部 20 Sredets str., 4003 Plovdiv，BG VAT 202150972；无官方邮箱（Gmail 联系）→ **国别更正：保加利亚**', iso='GB', fetched=F,
    source='GB · 1 次检索：cctvspot.co.uk About Us（「MB Vision Ltd.；Headquarters for Europe: 20 Sredetc str., 4003 Plovdiv, Bulgaria；BG VAT N: BG 202150972；UK VAT N: GB 411290538」；品牌 Hikvision / Dahua / Ajax / Wi-Tek）+ 首页（「Since our inception in 2012, MB Vision Ltd. has been a leading importer and distributor of high-quality CCTV equipment … one of the most trusted online suppliers in Bulgaria … across Europe」）+ DVR kits 页（联系 cctv.mbvision@gmail.com；「imported directly for the EU market」）；保加利亚商业登记（ЕИК 202150972）未另查',
    url='https://cctvspot.co.uk/about-us',
    number='BG ЕИК / VAT 202150972 · UK VAT GB411290538', status='Active（站点在线）', incorporated='2012（自述）', company_type='Ltd.（保加利亚 ООД 推定；英国无实体登记）',
    sic=['CCTV 设备进口与在线分销（Hikvision / Dahua 授权经销；套件、IP、HD-CVI、LPR）'],
    address='ul. Sredets 20, 4003 Plovdiv, Bulgaria（英国站无实体地址）', accounts='—', accounts_due='—', size_band='微型（人数未取）',
    officers=['无具名（研究档无 KP；Gmail 联系 cctv.mbvision@）'], psc='未取', charges='', prev_names=[],
    lines=['**保加利亚在线 CCTV 零售商（英国前台）+ 无官方邮箱 + 表内用 UTEPO PoE** → **分销 20% small，一页纸**：STC-028GP / STC-228GP / STC-2216GP（对标其在售 UTEPO / Wi-Tek 价）；DAP Plovdiv；不加厚',
           '收件：站点联系表 / Gmail（公开邮箱规则：Gmail 为站点公示，可用）；发信窗口 Thu 12–14 EET；国别更正保加利亚（渲染 country_fix）'],
    notes='分销 20% small；一页纸；国别更正 BG。')

# ---------------- PL 1 ----------------
put('SB-172', key='pl', batch=B, name='CONSTEEL Electronics Sp. z o.o. Sp. k.（consteel-electronics.com；Sopot）— 2017-08-22 登记的工业自动化 / 工业电子分销商（面向 CCTV / BMS / 汽车 / 智能电网 / 轨道 / 数字标牌集成商与安装商；**3onedata 工业交换机 PoE+ / EN 50155 / IEC 61850、ADFweb 协议转换、Caimore 无线**）；KRS 0000691687，NIP 5862321609，REGON 368059985；营收 7.9 mln zł（bizraport）、8 人（2022）；普通合伙人 CONSTEEL ELECTRONICS Sp. z o.o.（KRS 0000681591）**Prezes Zarządu Bartosz Marciszewski = 研究档 KP sklep@ 本人**', iso='PL', fetched=F,
    source='PL · 1 次检索：官网 Regulamin / Dział sprzedaży（CONSTEEL Electronics sp. z o.o. sp. k.；ul. Rzemieślnicza 17/19, 81-855 Sopot；NIP 5862321609；REGON 368059985；KRS 0000691687）+ krs-pobierz（Spółka komandytowa；登记 2017-08-22；Sąd Rejonowy Gdańsk-Północ VIII Wydział KRS）+ bizraport（KRS 0000691687；资产 3.1 mln、营收 7.9 mln、利润 849 tys. zł）+ EMIS（2017-08-22；8 人 2022；2024 营收 -21.98%）+ rejestr.io（普通合伙人 CONSTEEL ELECTRONICS Sp. z o.o.；KRS 0000681591；NIP 5862319104；资本 50 tys. zł；Prezes Zarządu Bartosz Marciszewski（2020-02-20 起；500 udziałów）；Marta Ewa Borkowska（2023-01-05 起；500 udziałów））+ 官网 O firmie（3onedata：switche przemysłowe PoE+, EN50155, IEC61850, media konwertery, serwery portów；ADFweb；Caimore）+ automatyka.pl（客户群：集成商 / 分销商 / 制造商 / 安装商）+ LinkedIn（2017；11–50；Gdynia）',
    url='https://krs-pobierz.pl/consteel-electronics-spolka-z-ograniczona-odpowiedzialnoscia-spolka-komandytowa-i6711118',
    number='KRS 0000691687 · NIP 5862321609 · REGON 368059985（普通合伙人 KRS 0000681591）', status='Aktywna（KRS 档案 2026-05 确认）', incorporated='2017-08-22', company_type='Spółka komandytowa（普通合伙人 CONSTEEL ELECTRONICS Sp. z o.o.，资本 50,000 zł）',
    sic=['PKD 46.90.Z — 非专业批发（实为工业自动化 / 工业通信 / 工业电子分销：3onedata 工业交换机、ADFweb 转换器、Caimore 路由、工业 PC、显示器）'],
    address='ul. Rzemieślnicza 17-19, 81-855 Sopot', accounts='营收 7.9 mln zł、利润 849 tys. zł（bizraport；2024 营收 -22%）', accounts_due='—', size_band='小型（8–11 人）',
    officers=['Bartosz Marciszewski — Prezes Zarządu（普通合伙人）/ 股东 50% = **研究档 KP sklep@ 本人**', 'Marta Ewa Borkowska — 股东 50%（2023 起）'], psc='Marciszewski / Borkowska', charges='', prev_names=[],
    lines=['**3onedata 波兰分销（表内「质量一般」）+ 老板本人收件 → Saga STI 作其第二工业线 → 分销 20%**：STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM / STI-0240GE（对标 3onedata IES 系列价；-40~75 °C；3 年保修）；**轨道 EN 50155 / IEC 61850 不谈（守界）**；B BIG，**加厚**（对标价表）',
           '表内「3onedata 的工业 FS 比较多；串口 / 工业 FS / MC」→ 第二次触达换主题「a second industrial Ethernet line beside your current Chinese brand — managed L2+, 3-year warranty, MOQ 1」（不点名 3onedata）；发信窗口 Thu 12–14 CET；升 A 候选（回信即 A）'],
    notes='分销 20%；KP = Prezes 本人；B BIG；加厚；升 A 候选；轨道守界。')
print('b102 DE 4 + GB 4 + PL 1 written')
