#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 98 批 · DE 4 户（其中 1 户国别更正 → 奥地利）+ GB 4 户 + PL 4 户（T29-U91，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 98

# ---------------- DE 4（含 AT 1）----------------
put('SB-232', key='de', batch=B, name='AIXONTEC GmbH（aixontec.com；Aachen）— 网络基础设施产品开发 / 组装 / 销售（自有品牌线缆 + 工业以太网；Amazon 卖家）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Imprint（AIXONTEC GmbH；general manager Ashkan Ghaznavi；Freunder Weg 106, 52068 Aachen；VAT DE 301189253；**Amtsgericht Aachen HRB 19851**）+ Northdata（HRB 19851；2015-08-11 登记；MD A. Ghaznavi Monfared；Capital €25,000）+ webvalid（Gesellschaftsvertrag 2015-07-21；Unternehmensgegenstand「Entwicklung, Konfektion und Vertrieb von innovativen Produkten für die Netzwerk-Infrastruktur」；GF Ghaznavi Monfared, Ashkan，单独代表权 + 自我交易豁免）+ XING（Dipl.-Ing. Ashkan Ghaznavi = Partner / Gesellschafter + GF since 2011；此前 Leoni Kerpen 区域销售、Niedax 中东 / 印度区域销售经理）+ Amazon.de 卖家 Impressum',
    url='https://www.northdata.com/AIXONTEC%20GmbH,%20Aachen/HRB%2019851',
    number='Amtsgericht Aachen HRB 19851；USt-IdNr. DE 301189253', status='Active', incorporated='2015-07-21（合同）/ 2015-08-11（登记）；业务自称 2011 起', company_type='GmbH（资本 €25,000；一人 GF = 股东）',
    sic=['网络基础设施产品开发 / 线缆组装 / 销售（Verlegekabel、跳线、RFID 线缆资产管理、工业以太网、家庭光纤）', 'Amazon.de 自有品牌 AIXONTEC 卖家'],
    address='Freunder Weg 106, 52068 Aachen', accounts='—（GmbH 小型，Bundesanzeiger 简式）', accounts_due='—', size_band='微型 / 小型（资本 €25,000；一人 GF）',
    officers=['Dipl.-Ing. Ashkan Ghaznavi Monfared — Geschäftsführer + Gesellschafter（*1974；2011 起）= 研究档 KP ashkan.ghaznavi@ 本人'], psc='Ashkan Ghaznavi Monfared（推定全资）', charges='', prev_names=[],
    lines=['**研究档 KP 坐实 = 老板本人**（GF + 股东，线缆行业销售出身）→ 发信直达决策人；14 次群发无回复 = 读而不回或进垃圾箱，第二次触达换主题不换人',
           '自有品牌 AIXONTEC（Amazon 卖家 + 自家网店）+ 表内「工业 FS 常总的 / 现从国内供应商采购」= **已在华南买工业交换机贴自己标** → 对标现供应商报 STI 工业线贴 AIXONTEC 标（OEM 30%，MOQ 1），卖点 3 年保修 + Marvell 管理型（STI-288DGGPM $137）',
           '规模微型（€25k 资本、一人 GF）→ 单量小但「自有标 + 已进口 + 决策人直达」三项全中 → **贴标试探首选 small**；Simon 表内「可以着重跟一下」与此一致',
           '发信窗口 Thu 12–14 CET；信用：Amazon 卖家 + 2015 起无变更，T/T 前 100% 起步'],
    notes='贴标试探 small（KP = 老板本人）。')
put('SB-1091', key='de', batch=B, name='TRIOTRONIK GmbH（2026-09-16 更名自 TRIOTRONIK Computer und Netzwerktechnik GmbH；triotronik.com；Weiz / Krottendorf, Steiermark, 奥地利）— 网络组件批发「der Netzwerkdistributor」+ 光纤 / 铜缆组件与 WLAN 天线制造（国别更正 DE → AT）', iso='AT', fetched=F,
    source='DE→AT · 1 次检索：akademie.triotronik.com Impressum（TRIOTRONIK Computer und Netzwerktechnik GmbH；Energiestraße 10, 8160 Weiz；UID ATU63017835；**Firmenbuchnr. 287460k LG ZRS Graz**；Geschäftsführung Peter Hofer-Perner, Thomas Thir；Beteiligung TRIOTRONIK Holding GmbH 100%；Unternehmensgegenstand 网络组件批发 + 光纤 / 铜缆网络组件与 WLAN 天线制造）+ firmenatlas（FN 287460K 活跃；**2026-09-16 更名 TRIOTRONIK GmbH**；2007-02-07 设立；2025 年报 Bilanzsumme €12.4M / Eigenkapital €3.7M / Jahresüberschuss €3.6M；GF Thomas Thir-Greiter *1983 + Peter Hofer-Perner *1967（均 2021-10-11 起单独代表）；Prokurist Bernhard Flicker *1986）+ WKO（GISA 20818319 / 20895938；Krottendorf 站点 2012-11-20 起）+ unternehmen24（资本 €35,000）+ Kleine Zeitung 2026-09-30「So will die Firma Triotronik in Weiz weiter wachsen」（三位股东 Thir-Greiter / Flicker 销售总监 / Hofer-Perner）',
    url='https://www.firmenatlas.com/firma/287460k',
    number='FN 287460k（LG ZRS Graz）；UID ATU63017835；GLN 9110017050682', status='Active（2026-09-16 更名；2025 年报已交）', incorporated='2007-02-07', company_type='GmbH（资本 €35,000；TRIOTRONIK Holding GmbH 100% → 三位经营股东）',
    sic=['网络组件批发（MikroTik Master 分销、PLANET 在线销售专页、Ubiquiti 等）', '光纤 / 铜缆网络组件与 WLAN 天线制造（自有品牌）', 'TRIOTRONIK Akademie 培训'],
    address='Energiestraße 10, 8160 Weiz（Krottendorf）, Steiermark, Austria', accounts='2025 年报：资产总额 €12.4M；权益 €3.7M（30.1%）；净利 €3.6M（firmenatlas）', accounts_due='—', size_band='中型（净利 €3.6M；奥地利区域性分销商）',
    officers=['Thomas Thir-Greiter — Geschäftsführer + Gesellschafter（2021-10-11 起；此前 Prokurist）', 'Peter (Hubert) Hofer-Perner — Geschäftsführer + Gesellschafter（2021-10-11 起）', 'Bernhard Flicker — Prokurist + Vertriebsleiter + Gesellschafter', 'Wolfgang Sembacher — 前 GF（已卸任）'], psc='TRIOTRONIK Holding GmbH（100%）→ Thir-Greiter / Hofer-Perner / Flicker', charges='', prev_names=['TRIOTRONIK Computer und Netzwerktechnik GmbH（2007-02-07 → 2026-09-16）'],
    lines=['**国别更正**：用户表归 DE，实为奥地利施蒂利亚 Weiz → country_fix 奥地利；发信窗口与 DE 同（Thu 12–14 CET）',
           '**分销 20%，B BIG**：MikroTik Master 分销 + PLANET 专页 = 正好卖我们对标的两个牌子；2025 净利 €3.6M、2021 管理层收购后三位股东经营、2026-09 更名 + 扩张报道 → 有钱有渠道有决策人',
           '收件人：研究档无 KP → 写 Bernhard Flicker（Vertriebsleiter + 股东，产品线决策）抄 office@；对标 PLANET GS-4210 / MikroTik CRS 报 STC-424XGGPM-280W（$198 list）+ HRUI 入门线，卖点 = PLANET 同规格 -30%、Marvell L2+、3 年保修（STI）',
           '自有制造（光纤 / 铜缆组件 + 天线）= 有贴标习惯 → 第二句带「TRIOTRONIK 标 PoE 交换机 OEM 30%，MOQ 1」；升 A 候选（回信即 A）'],
    notes='国别更正 AT；B BIG；分销 20% + 贴标；升 A 候选。')
put('SB-833', key='de', batch=B, name='comtime GmbH（comtime-com.de；Norderstedt bei Hamburg）— 工业路由器 / M2M 调制解调器制造商「Made in Germany」（DIN 导轨；为他牌 OEM）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（comtime GmbH；Gutenbergring 67b, 22848 Norderstedt；GF Markus Kasten；**HRB Kiel 4574 NO**；USt-ID DE 813138753；WEEE DE 84024192）+ Creditreform（HRB 4574 NO Amtsgericht Kiel；2026-02-04 公告：GF 3. Kasten, Markus *1995 Hamburg 单独代表；2025-03-24 公告：地址迁 Gutenbergring 67b）+ Creditsafe（2000 年登记）+ firmenwissen（Active；1 GF）+ PresseBox / wlw（Josef Dorfer = Marketing und Vertrieb, Vertriebsleiter）+ stellenwerk Bremen 2026-06（「Industrierouter Made in Germany – von der Hardware bis zur Firmware」）',
    url='https://comtime-com.de/impressum/',
    number='Amtsgericht Kiel HRB 4574 NO；USt-IdNr. DE 813138753', status='Active（2026-02 新任 GF）', incorporated='2000（登记）', company_type='GmbH',
    sic=['工业路由器 / M2M 调制解调器（5G / LTE / DSL / LAN、OpenVPN 连接服务器、WebCenter 设备管理）自研自产', '为第三方 OEM（站内 OEM 19 处）'],
    address='Gutenbergring 67b, 22848 Norderstedt（2025-03 迁入；旧址 Gutenbergring 22）；研发招聘地 Bremen', accounts='—', accounts_due='—', size_band='小型',
    officers=['Markus Kasten — Geschäftsführer（*1995；2026-02-04 登记，新任）', 'Josef Dorfer — Vertriebsleiter（Marketing und Vertrieb）= 研究档 KP jd@ 本人（2013 起即是销售负责人）'], psc='未取', charges='', prev_names=[],
    lines=['**准同行（工业路由器厂）**：不买交换机做转售，只可能「配套」→ 缝隙 = 他们的 DIN 导轨路由器旁边缺工业 PoE 交换机 → 贴 comtime 标的 STI-054GP / STI-144GP（4+1 SFP）做「Router + Switch 套件」= **贴标试探 small（OEM 30%）**',
           '2026-02 换了 30 岁的新 GF（Markus Kasten）→ 新管理层常会补产品线 → 第二次触达写给新 GF 抄 Josef Dorfer，主题「DIN-rail PoE switch to pair with your LTE routers」',
           '8 次群发无回复 + 「Made in Germany」品牌叙事 → 贴标要中性包装 + 不提产地争议；低优先，一页纸即止'],
    notes='准同行；贴标试探 small；低概率。')
put('SB-1003', key='de', batch=B, name='aplus Datenkabel und Kommunikationssysteme GmbH & Co. KG（aplusnet.de / kabelprofi.net；Oldenburg）— 线缆组装起家的网络产品专业分销商（商标 a-plus / aplusNet；二代家族企业）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（aplus Datenkabel und Kommunikationssysteme GmbH & Co. KG；Gerhard-Stalling-Straße 34, 26135 Oldenburg；**Amtsgericht Oldenburg HRA 4241**；Komplementärin aplusNET Beteiligungs-GmbH HRB 5681；GF Smilka Geserick, Sonja Geserick；USt-IdNr. DE814202910）+ companyhouse（2005-02-28；Kapital €250,000；Gesellschafter Sonja Geserick；Prokurist Arno Geserick 1994 起）+ kabelprofi.net Über uns / Compliance（1986 Arno Geserick 创办；1996 起扩至 IT 分销；1997 注册商标 a-plus / aplusNet；2005 二代 Smilka + Sonja Geserick 接班）+ Northdata（HRA 4241；文字图形商标 aplusNET）+ ChannelPartner「Spezial-Distributoren」名录（网络产品 + 定制线缆组装）',
    url='https://www.aplusnet.de/Informationen/Impressum/',
    number='Amtsgericht Oldenburg HRA 4241（KG）/ HRB 5681（Komplementär-GmbH）；USt-IdNr. DE814202910', status='Active', incorporated='1986（业务）/ 2005-02-28（现 KG 形式）', company_type='GmbH & Co. KG（资本 €250,000；家族二代）',
    sic=['网络产品专业分销（SFP、工业交换机、MC、PoE；Digitus 等）', '定制线缆 / 线束组装（机械设备、车辆测量、IT / 电信）', '自有商标 a-plus / aplusNet'],
    address='Gerhard-Stalling-Straße 34, 26135 Oldenburg', accounts='—（KG 简式）', accounts_due='—', size_band='小型 / 中型（资本 €250,000；专业分销）',
    officers=['Sonja Geserick — Geschäftsführerin（Komplementär-GmbH）+ Gesellschafterin = 研究档 KP sonja.geserick@ 本人', 'Smilka Geserick — Geschäftsführerin', 'Arno Geserick — 创办人，Prokurist（1994 起）'], psc='Geserick 家族', charges='', prev_names=[],
    lines=['**研究档 KP 坐实 = 老板本人**（二代 GF + 股东）→ 发信直达决策人',
           '表内「Digitus 的产品很多，价格很高」= 现用 Assmann/Digitus 做 MC / 工业 FS / PoE 货源 → **分销 20%**：对标 Digitus 报 STC-110XGE（$65）/ STI-288DGGPM（$137）/ STC-228GP（$33），卖点 = 同规格 -30~40%',
           '自有商标 aplusNet 已注册 29 年 + 自有线缆组装 = 有贴标基因 → 第二句「aplusNet 标 MC / PoE 交换机 OEM 30%，MOQ 1」；收件人 Sonja Geserick；发信窗口 Thu 12–14 CET',
           '官网 unreachable（研究档）但 kabelprofi.net / Impressum 2026 在线 → 地址与邮箱有效；表内「质量一般」= Simon 对其货的评价，不影响发信'],
    notes='KP = 老板本人；分销 20% + 贴标。')


# ---------------- GB 4（含 AE 1）----------------
put('SB-1054', key='gb', batch=B, name='Luxrite Ltd（luxritesecurity.com；Stevenage, Hertfordshire）— Trade-only CCTV / 门禁 / 报警分销商，自有品牌 SPRO / Vectus', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 06801342（Private limited company；Incorporated 2009-01-26；Active；Unit 3 Eastman Way, Pin Green Industrial Estate, Stevenage SG1 4SZ；Officers 3 / 0 resignations：LUO, Chin Ping, Ms.（Director，2009-01-26 起，British，b. 1977-09）；LO, Liu Jung（Director 2013-05-23 起 + Secretary 2009-01-26 起，b. 1975-09））+ Endole（PSC = Chin Ping Luo + Liu Jung Lo；Small）+ companiesintheuk（Capital £1,000；Accounts Total Exemption Full；Charges 0）+ LinkedIn（11–50 人；「home to the SPRO and Vectus brand of CCTV equipment」；Rio Luo = Director）+ 官网（© 2026；Registered in England No 6801342；Ruijie PoE 交换机在售）',
    url='https://find-and-update.company-information.service.gov.uk/company/06801342',
    number='Companies House 06801342；VAT 未取', status='Active（2026 官网在线；Charges 0）', incorporated='2009-01-26', company_type='Private limited company（资本 £1,000；两位董事 = PSC 夫妇式持股）',
    sic=['Trade-only 安防分销：HD / IP CCTV、报警（Ajax / Texecom / Dahua Airshield）、可视门禁、门禁；只供批发商 / 零售商 / 安装商', '自有品牌 SPRO / Vectus（CCTV）'],
    address='Unit 3 Eastman Way, Pin Green Industrial Estate, Stevenage, Hertfordshire SG1 4SZ', accounts='Total Exemption Full（小型；资产负债表 <£7.5M）', accounts_due='未取（CH 页未抓到期日）', size_band='小型（11–50 人）',
    officers=['Chin Ping (Rio) Luo — Director / Sales Director + PSC（2009 起）', 'Liu Jung Lo — Director（2013 起）+ Secretary（2009 起）+ PSC', 'Vinny Lomonaco — Account Manager', 'Peter Cheung — IT Operations Manager'], psc='Chin Ping Luo + Liu Jung Lo', charges='0', prev_names=[],
    lines=['**自有品牌 SPRO / Vectus + 在售 Ruijie PoE** → 两条线：① 对标 Ruijie RG-ES2xx 报 HRUI STC-028GP / STC-228GP / STC-2224GP（分销 20%）；② **SPRO 标 PoE 交换机 OEM 30%**（他们已给摄像机贴自有标，PoE 配套贴标顺理成章）',
           '两位董事 = PSC（Luo / Lo，华人姓氏，2009 起）→ 大概率已有华南 / 台湾直采渠道 → 卖点只能是「Marvell 管理型 + 3 年保修 + MOQ 1 混批」，不是价格；收件人：研究档无 KP → 写 Rio Luo（Sales Director）',
           '**升 A 候选**（回信即 A）：自有标 + 已进口 + 决策人直达 + 英国主战场；发信窗口 Thu 12–14 GMT；不提是否中文沟通（默认不）'],
    notes='自有标 SPRO / Vectus；OEM 30% + 分销 20%；升 A 候选。')
put('SB-1002', key='gb', batch=B, name='Amplicon Liveline Limited（amplicon.com；Brighton）— 工业计算 / 数据通信 / 测控 / 安防自动化分销商（1973；Amplicon Group）', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 01091353（Private limited company；Incorporated 1973-01-18；Active；Unit 11 Centenary Industrial Estate, Hollingdean Road, Brighton BN2 4AW（2024-03-15 自 Hughes Road 地址更正）；Officers 21 / 20 resignations：CITRONI, Gina（Director，2004-07-01 起，Occupation Commercial Director，b. 1958-11）；BUSHBY, Mark / SAUNDERS, Douglas（Operations Director）；Filing：AA 小型公司账目至 2024-06-30（2025-03-20 交）；PSC02 2024-12-13：Amplicon Group Holdings Ltd（14466238）自 2024-11-20 持股 ≥75%，接替 Amplicon Group Limited（06201353））+ Endole（Medium：50–250 人或 £10–50M）',
    url='https://find-and-update.company-information.service.gov.uk/company/01091353',
    number='Companies House 01091353', status='Active（账目至 2024-06-30 已交 2025-03-20）', incorporated='1973-01-18', company_type='Private limited company（Amplicon Group Holdings Ltd 14466238 持股 ≥75%，2024-11 集团重组）',
    sic=['工业计算（工控机 / 嵌入式）、数据通信（工业交换机：Moxa / Hirschmann / Advantech / Cisco）、测控（DAQ）、安防自动化分销（面向系统集成商、OEM、制造商）'],
    address='Unit 11 Centenary Industrial Estate, Hollingdean Road, Brighton BN2 4AW', accounts='小型公司账目至 2024-06-30（2025-03-20 交；Endole 评 Medium）', accounts_due='2025-06-30 期账目应于 2026-03-31 前交（按例推算，未核）', size_band='中型（50–250 人 / £10–50M，Endole）',
    officers=['Gina Citroni — Director + Commercial Director（2004 起；亦为 Amplicon Group Ltd 董事 2007 起）= 研究档 KP gina.c@ 本人', 'Mark Bushby — Director', 'Douglas Saunders — Operations Director（CH 现列 resigned / 名录列现任，待核）'], psc='Amplicon Group Holdings Ltd（14466238；2024-11-20 起）', charges='未取', prev_names=[],
    lines=['**研究档 KP 坐实 = 商务总监兼董事本人**（Gina Citroni，2004 起）→ 发信直达采购决策人',
           '表内「工业 FS 很多牌子的销售平台」= Moxa / Hirschmann / Advantech 工业交换机分销 → **分销 20%（工业线）**：对标 Moxa EDS 系列报 STI-288DGGPM（$137）/ STI-244DGGPM（$121）/ STI-0240GE（$130），卖点 = Moxa 同规格 -50%、3 年保修、-40~75 °C',
           '2024-11 集团重组（新控股公司 14466238）+ 50 余年老牌 → 采购流程正规，先要证书（CE / RoHS / UKCA 齐）与样机（付费样机）；B BIG',
           '发信窗口 Thu 12–14 GMT；不提 UL / 军工'],
    notes='KP = 商务总监本人；B BIG；分销 20% 工业线。')
put('SB-1020', key='gb', batch=B, name='Cratsol Technology LLC（cratsol.ae；Dubai Business Bay）+ 英国壳 CRATSOL LTD（Newcastle upon Tyne）— IT 硬件增值转售商（VAR；国别更正 GB → AE）', iso='AE', fetched=F,
    source='GB→AE · 1 次检索：LinkedIn（Cratsol Technology LLC - UAE；2017；11–50；601 One by Omniyat, Business Bay, Dubai；另列 Chicago IL 地址）+ Crunchbase（Legal Name Cratsol Technology LLC；sales@cratsol.ae）+ 官网 Contact（CRATSOL TECHNOLOGY LLC, Office 605 Silver Tower, Business Bay）+ ZoomInfo（<$5M；Faisal Shahid 2019 起）+ **Companies House 11084123 CRATSOL LTD**（Incorporated 2017-11-27；Active；G18 Amber Court, William Armstrong Drive, Newcastle upon Tyne NE4 7YA = 注册地址服务）',
    url='https://find-and-update.company-information.service.gov.uk/company/11084123',
    number='UAE 营业执照号未取；英国壳 Companies House 11084123', status='Active（UAE 主体 2026-09 仍在；英国壳 Active）', incorporated='2017（UAE）/ 2017-11-27（英国壳）', company_type='LLC（迪拜）+ Private limited company（英国，注册地址服务）',
    sic=['IT 硬件 / 软件增值转售（台式机、工作站、显示器、打印机、网络；多品牌）面向 UAE 与海外'],
    address='601 One by Omniyat / Office 605 Silver Tower, Business Bay, Dubai, UAE；英国壳 G18 Amber Court, William Armstrong Drive, Newcastle upon Tyne NE4 7YA', accounts='英国壳：未取', accounts_due='未取', size_band='小型（11–50 人；<$5M）',
    officers=['Faisal Shahid — Cratsol Technology（ZoomInfo）', 'Issac Grant / Amir Zahirshah — 研究档询盘联系人（Skype）', '英国壳董事未取'], psc='未取', charges='', prev_names=[],
    lines=['**国别更正**：cratsol.co.uk 只是迪拜 VAR 的英国壳（Newcastle 注册地址服务）→ country_fix 阿联酋；不属四大主战场',
           '唯一询盘是「10G DAC 3 m × 300 单价」= Saga 不做的品类 → 只能一页纸回 STC-110XGE（10G 交换机 $65）做关联，**低概率，不加厚**',
           '迪拜 IT VAR 做政府 / 企业标 → 会要 Cisco 级品牌；我们没有位置；若回信按分销 20% 报，T/T 前 100%'],
    notes='国别更正 AE；低概率；下轮不追。')
put('SB-1067', key='gb', batch=B, name='Raytel Security Systems Limited（raytelsecurity.com；South Woodham Ferrers, Essex）— 门禁 / 门口机制造商兼库存商（1979；Vimar Elvox / Soyal 英国授权分销；Raytel Group）', iso='GB', fetched=F,
    source='GB · 1 次检索：官网 About（Raytel Security Systems Limited；Raytel House, 1-5 Cutlers Road, South Woodham Ferrers, Chelmsford CM3 5WA；Established 1979；**Company Registration No 1280393**；VAT GB 394 9607 00；Directors R. Lawrence (Managing), D. G. Brookes）+ Companies House 01280393（Incorporated 1976-10-06；Active；前名 ELEKTROFLO SYSTEMS LIMITED 1976-10-06 → 1979-12-31；Officers：BROOKES, David Gary（Director）；LAWRENCE, Roy（Director））+ Endole（Roy Lawrence b. 1934-04 = PSC，1991-11 起董事，92 岁，活跃于 6 家公司；David Gary Brookes b. 1960-02 Engineer；Secretary Michelle Mead；股东 2）+ raytel.co.uk（Raytel Group 1980 成立 = Rayleigh Instruments 1964 + Raytel Security Systems 1979 母公司）+ LinkedIn（2–10 人）',
    url='https://find-and-update.company-information.service.gov.uk/company/01280393',
    number='Companies House 01280393；VAT GB 394 9607 00', status='Active', incorporated='1976-10-06（业务 1979 起）', company_type='Private limited company（Raytel Group 成员；PSC Roy Lawrence）',
    sic=['门禁 / 门口机（音视频对讲）产品制造 + 库存分销（自有 Raytel / AR- 系列读卡器 + Vimar Elvox + Soyal 英国授权分销）', 'ISO 9001（1991 起）'],
    address='Raytel House, 1-5 Cutlers Road, South Woodham Ferrers, Chelmsford, Essex CM3 5WA', accounts='未取（1 次即停）', accounts_due='未取', size_band='微型（2–10 人）',
    officers=['Roy Lawrence — Managing Director + PSC（b. 1934；1991 起）', 'David Gary Brookes — Director（Engineer，b. 1960）', 'Michelle Mead — Secretary'], psc='Roy Lawrence', charges='未取', prev_names=['Elektroflo Systems Limited（1976–1979）'],
    lines=['微型（2–10 人）+ 92 岁老板 + 门禁为主、CCTV / PoE 只是配套 → **低概率，一页纸即止，不加厚**',
           '自有品牌 Raytel 门禁产品 + Elvox IP 门口机需要 PoE → 一句「Raytel 标 4 / 8 口 PoE（STI-054GP / STC-028GP），MOQ 1」带过；收件人 info@ 点名 David Brookes（工程董事，更可能看技术信）',
           '发信窗口 Thu 12–14 GMT'],
    notes='低概率；下轮不追。')


# ---------------- PL 4 ----------------
put('SB-058', key='pl', batch=B, name='„SABMARTV” Marcin Wypiór（sabmar.tv；Rybnik）— 体育赛事网络直播 / 转播制作个体企业（摩托车速道赛 PPV）= 终端用户', iso='PL', fetched=F,
    source='PL · 1 次检索：GoWork（Nazwa pełna „SABMARTV” MARCIN WYPIOR；ul. Gruntowa 43D, 44-270 Rybnik；**NIP 6421823587；REGON 273230435**；Forma prawna Indywidualna działalność gospodarcza；Data rozpoczęcia 1997-05-14）+ Targeo（PKD 59.11.Z 影视 / 电视节目制作）+ krs-online / pkt.pl（Sabmar Studio foto-video，1996 起）+ WP SportoweFakty 2024-09-16（Marcin Wypiór = 网络电视 SABMARtv 所有人；速道赛转播）+ ppv.stream 规则页（组织者 SABMARtv, Rybnik, NIP 642-182-35-87）',
    url='https://www.gowork.pl/sabmartv-marcin-wypior,25701005/dane-kontaktowe-firmy',
    number='NIP 6421823587；REGON 273230435（CEIDG）', status='Active（2024 转播活跃）', incorporated='1997-05-14（CEIDG）', company_type='Indywidualna działalność gospodarcza（个体）',
    sic=['59.11.Z 体育赛事网络直播 / 转播制作（2 辆转播车、虚拟演播室、PPV 平台）', '27.31.Z 光缆生产（登记副业）'],
    address='ul. Gruntowa 43D, 44-270 Rybnik（旧址 Modrzewiowa 22）', accounts='—（个体）', accounts_due='—', size_band='微型（家庭经营；子 Błażej Wypiór 参与）',
    officers=['Marcin Wypiór — 业主 = 研究档 KP biuro@sabmar.tv'], psc='Marcin Wypiór', charges='', prev_names=['Sabmar Studio foto-video（1996）'],
    lines=['**终端用户（转播制作个体）**：买交换机只为自己转播车 / 演播室的 IP 视频网（SMPTE 2110 需要 PTP / 大缓存，非我们强项）→ **不加厚，一页纸即止**；若回信只报 STC-110XGE（10G）/ STC-424XGGPM-280W 两行',
           '登记副业 27.31.Z 光缆生产 = 他们自己做光缆跳线 → 与我们无交集；复利无'],
    notes='终端用户；低概率；下轮不追。')
put('SB-1009', key='pl', batch=B, name='Batna Sp. z o.o.（batna24.com / anteny24.pl；Częstochowa）— Ubiquiti / MikroTik 欧洲主力分销商（2001 起；Mucha 家族）', iso='PL', fetched=F,
    source='PL · 1 次检索：rejestr.io（BATNA SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ；**KRS 0001003926**；Prezes Zarządu Magdalena Mucha 2022-12-01 起；Kapitał 40,000 zł；Olgi Boznańskiej 3E, 42-202 Częstochowa）+ aleo（股东 Łukasz Jan Mucha 5 份 / Magdalena Marzena Mucha 5 份）+ D&B（REGON 380387214）+ rejestr.io 24 BATNA Sp. z o.o. Sp. k.（KRS 0000908391；NIP 5732927213；REGON 389288258；2021-06-25；komplementariusz = Batna Sp. z o.o.；komandytariusz Łukasz Jan Mucha）+ bizraport（主业 46.52 电子 / 电信设备批发；页面示「392,5 mln zł」规模指标，口径未明 → 仅作区间）+ kadorf / Facebook（2001 起；「main European distributor of Ubiquiti Networks and MikroTik」）+ batna24.com 产品卡（Batna sp. z o. o., ul. 1 Maja 23, 42-217 Częstochowa；+48 34 361 04 48）',
    url='https://rejestr.io/krs/1003926/batna',
    number='KRS 0001003926（Batna Sp. z o.o.）；REGON 380387214；关联 24 BATNA Sp. z o.o. Sp. k. KRS 0000908391 / NIP 5732927213', status='Active（2026-09 产品卡仍以 Batna sp. z o.o. 开票）', incorporated='2022-12-01（现 Sp. z o.o.；业务 2001 起；Sp. k. 2021-06-25）', company_type='Sp. z o.o.（资本 40,000 zł；Mucha 夫妇各半）+ Sp. k. 经营体',
    sic=['46.52 无线 / 网络设备批发：Ubiquiti、MikroTik、Extralink、LigoWave、TP-Link、RF elements、Totolink（switch 301 / camera 231 / poe 92 SKU）', '多语种电商（PL / IT / CS …）'],
    address='ul. Olgi Boznańskiej 3E, 42-202 Częstochowa（注册）；ul. 1 Maja 23, 42-217 Częstochowa（开票 / 门店）', accounts='第三方规模指标：数亿 zł 级（bizraport，口径未明）', accounts_due='—', size_band='大型（欧洲级 Ubiquiti / MikroTik 分销；B BIG）',
    officers=['Magdalena (Marzena) Mucha — Prezes Zarządu + 股东 50%', 'Łukasz Jan Mucha — 股东 50% + Sp. k. komandytariusz（实际经营者，推定）'], psc='Mucha 夫妇', charges='', prev_names=['24 BATNA Sp. z o.o. Sp. k.（经营体）'],
    lines=['**B BIG，分销 20%**：欧洲级 Ubiquiti / MikroTik 分销商 = 正是我们对标的两个牌子的货架 → 对标 MikroTik CRS / Ubiquiti USW 报 STC-424XGGPM-280W（$198 list）+ HRUI 入门线 + STC-110XGE（10G $65），卖点 = 同规格 -30% + Marvell L2+',
           '2022-12 重组为 Sp. z o.o.（原 Sp. k.）= 正常化；研究档 KP 只有 shop@ → 写 zakupy / product manager「switche」抄 shop@；波兰为次级战场，但这家是 PL 名单里最大的渠道',
           '意大利语站点曾被归入意大利名单（研究档）→ 以 PL 主体为准，不重复发；发信窗口 Thu 12–14 CET；**升 A 候选**（回信即 A）'],
    notes='B BIG；分销 20%；升 A 候选。')
put('SB-1017', key='pl', batch=B, name='Cellco Communications Sp. z o.o.（cellco.com.pl；Kobylanka k. Szczecina + Warszawa 分部）— 光纤技术供应商 / 光缆生产（Wieczorek 家族）', iso='PL', fetched=F,
    source='PL · 1 次检索：官网 Kontakt（Cellco Communications Sp. z o.o.；ul. Szczecińska 30E, 73-108 Kobylanka；分部 Plac Konesera 12, 03-736 Warszawa；**NIP 852-18-26-706；KRS 0000213509 Sąd Rejonowy w Szczecinie；Kapitał 52,000 zł**；Tomasz Wieczorek = CEO / Prezes Zarządu tomasz.wieczorek@；Piotr Wieczorek = Zastępca Prezesa；Bartosz Wieczorek = Head of Technology (R&D)）+ rejestr.io（2004-08-03；Prezes Tomasz Piotr Wieczorek 2004 起 = 股东 + 实际受益人；规模指标 24 mln）+ aleo（Tomasz Piotr Wieczorek 416 份 / 41,600 zł = 80%）+ krs-online（PKD 27.31.Z 光缆生产）+ gowork（Piotr Mariusz Wieczorek 副总）',
    url='https://www.cellco.com.pl/kontakt.htm',
    number='KRS 0000213509（Szczecin）；NIP 8521826706', status='Active（2026 官网更新）', incorporated='2004-08-03', company_type='Sp. z o.o.（资本 52,000 zł；Tomasz Wieczorek 80%）',
    sic=['27.31.Z 光缆生产 / 光纤技术供应：光缆、CWDM、GPON、跳线、光纤配线架、10G / FTTH', '少量 MC / 交换机配套'],
    address='ul. Szczecińska 30E, 73-108 Kobylanka（总部）；Plac Konesera 12, 03-736 Warszawa（分部）', accounts='第三方规模指标 ≈24 mln zł（rejestr.io，口径未明）', accounts_due='—', size_band='小型 / 中型（家族企业）',
    officers=['Tomasz Piotr Wieczorek — Prezes Zarządu + 80% 股东 + 实际受益人 = 研究档 KP tomasz.wieczorek@ 本人', 'Piotr Mariusz Wieczorek — Zastępca Prezesa', 'Bartosz Wieczorek — Head of Technology (R&D)'], psc='Tomasz Piotr Wieczorek（80%）', charges='', prev_names=['Cellco S.A.（KRS 0000206576，2005-01 注销的前身）'],
    lines=['**研究档 KP 坐实 = 老板本人**（Prezes + 80% 股东）→ 发信直达决策人',
           '光纤为主、交换机只是配套（表内「MC 较多 没咋看到 switch」）→ **分销 20%，窄品类**：只报带 SFP 上联 / 全光口的型号（STC-228GP 8+2 SFP $33–35、STC-2224GP 24+2+2、STC-110XGE 10G $65、STI-144GP 4+1 SFP 工业）做「光缆 + 光口交换机」配套，不发整本价格表',
           '华沙 Plac Konesera（Koneser 园区）分部 = 面向运营商 / FTTH 项目；发信窗口 Thu 12–14 CET；不加厚'],
    notes='KP = 老板本人；窄品类分销 20%。')
put('SB-1061', key='pl', batch=B, name='FHU „TELSAT” s.c.（obserwuj.pl；Tarnów）— CCTV 网店（民事合伙；Dahua 为主）', iso='PL', fetched=F,
    source='PL · 1 次检索：obserwuj.pl Regulamin / Kontakt（Właścicielem sklepu jest FHU„TELSAT” s.c.；ul. Rolnicza 7, 33-100 Tarnów；**NIP 993-00-03-405**；tel. 14 627 44 11）+ Ceneo 店铺页（NIP 9930003405；卖家为 CEIDG 登记个体经营者）',
    url='https://www.obserwuj.pl/kontakt,p1.html',
    number='NIP 9930003405（s.c.；合伙人 CEIDG 登记）', status='Active（Ceneo 在列；官网 timeout 偶发）', incorporated='未取（1 次即停）', company_type='Spółka cywilna（FHU = Firma Handlowo-Usługowa，民事合伙）',
    sic=['CCTV 网店：AHD / IP 监控套装、录像机、摄像机（Dahua 为主）、配套 FS / VC / MC / SFP'],
    address='ul. Rolnicza 7, 33-100 Tarnów', accounts='—', accounts_due='—', size_band='微型',
    officers=['合伙人姓名未公开（s.c.）'], psc='合伙人', charges='', prev_names=[],
    lines=['微型 CCTV 网店（民事合伙，Dahua 套装为主）→ **低概率，一页纸即止，不加厚**；若回信只报 HRUI STC-028GP $28 / STC-228GP $33',
           '表内「大华产品比较多」= Dahua 自带 PoE 交换机 → 我们只在「非 Dahua 8/16 口价格带」有位置'],
    notes='低概率；下轮不追。')

print('b98 DE 4 + GB 4 + PL 4 written')
