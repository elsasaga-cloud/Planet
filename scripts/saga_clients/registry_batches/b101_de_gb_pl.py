# -*- coding: utf-8 -*-
"""第 101 批（T29-U94，2026-10-28）DE 4 + GB 4 + PL 4 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 101
F = '2026-10-28'

# ---------------- DE 4 ----------------
put('SB-556', key='de', batch=B, name='UBF EDV Handel und Beratung Jürgen Fischer GmbH（ubf.de；Castrop-Rauxel，注册地 2015 迁 Mühldorf a. Inn）— 1981 年起的工业网络配件 B2B 电商 / 分销商（Industrial Ethernet、PoE、交换机、SFP、媒体转换器、串口 / 现场总线、LWL；ISO 9001:2015；GF 兼唯一股东 Jürgen Fischer）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（UBF EDV Handel und Beratung Jürgen Fischer GmbH；Römerstr. 37, 44579 Castrop-Rauxel；+49 2305 9634 0；vertrieb@ubf.de；Handelsregister HRB Dortmund Nr. 32518；W-IdNr DE421854265；USt-ID DE 125 414 228；WEEE DE 77813798；DIN EN ISO 9001:2015）+ firmendatenbanken（GmbH；HRB 32518 Dortmund；Geschäftsführung Jürgen Fischer；Gesellschafter Jürgen Fischer）+ Northdata（Dortmund HRB 32518 / Traunstein HRB 24719 / Dortmund HRB 18432；MD Jürgen Fischer；Capital 50,000 DEM；Change of headquarters）+ vivid 登记公告（Gesellschaftsvertrag 1981-06-25；2004 由 Herne 迁 Castrop-Rauxel；2015-10-20 Sitz 迁 Mühldorf a. Inn（Amtsgericht Traunstein HRB 24719））+ branchen-info（B2B Hersteller / Distributor / Großhandel mit Netzwerkkomponenten）',
    url='https://www.northdata.com/UBF%20EDV%20Handel%20und%20Beratung%20J%C3%BCrgen%20Fischer%20GmbH,%20Castrop-Rauxel/Amtsgericht%20Dortmund%20HRB%2032518',
    number='HRB 32518（Amtsgericht Dortmund；2015 起注册地 Mühldorf a. Inn = Amtsgericht Traunstein HRB 24719）· USt-ID DE125414228', status='Aktiv（站点在线）', incorporated='1981-06-25（公司合同）', company_type='GmbH（资本 50,000 DEM；GF 兼唯一股东 Jürgen Fischer）',
    sic=['工业网络组件 B2B 电商 / 分销（Industrial Ethernet 交换机、PoE 供电器 / 交换机、SFP、媒体转换器、串口 RS-232/422/485 与现场总线、LWL 光缆 / 跳线、POF）'],
    address='Römerstr. 37, 44579 Castrop-Rauxel（经营地；注册地 Mühldorf a. Inn）', accounts='—', accounts_due='—', size_band='微型 / 小型（人数未取；一人公司推定）',
    officers=['Jürgen Fischer — Geschäftsführer / Alleingesellschafter = 拍板人（研究档无具名 KP，仅 vertrieb@）'], psc='Jürgen Fischer', charges='', prev_names=['UBF EDV Handel und Beratung Jürgen Firscher GmbH（登记笔误，2004 更正）'],
    lines=['**老牌工业网络电商 + 老板一人拍板** → **分销 20%，小户，一页纸**：STI-054GP / STI-144GP / STI-288DGGPM（导轨 PoE / 光口）+ STC-228GP；强调 MOQ 1 + 3 年 STI 保修 + 德国 DAP 运费',
           '收件人 vertrieb@ 点名 Herrn Fischer；表内 1 次跟进无回复 → 第二次触达换主题「DIN-rail PoE switches for your industrial shop — 3-year warranty」；发信窗口 Thu 12–14 CET'],
    notes='分销 20%；小户；一页纸；研究档补 KP Jürgen Fischer。')
put('SB-472', key='de', batch=B, name='BMAnetworks GmbH（bma-networks.com；Schwentinental bei Kiel + Hamburg-Bahrenfeld）— 2007 年起的企业 IT 系统集成商（网络 / 安全 / ADC 项目；DIERCK GROUP 成员，集团 260 人）；Amtsgericht Kiel HRB 4103；GF Alisa Ehrk / Wolfgang Ehrk；18 人，总资产 €4.5M（2024 账）；研究档 KP Mats Hansen = Head of Information Security（非采购）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（BMAnetworks GmbH；Albert-Einstein-Ring 5, 22761 Hamburg-Bahrenfeld；Vertretungsberechtigte Geschäftsführer Alisa Ehrk, Wolfgang Ehrk；Registergericht Amtsgericht Kiel HRB 4103；USt-IdNr DE167682158；DIERCK GROUP (Holding) Preetzer Chaussee 55, 24222 Schwentinental）+ Validatis（Sitz Schwentinental；HRB 4103；EUID DEX1517R.HRB4103；Jahresabschluss 2024（2026-02-18）：Bilanzsumme €4.5M +36 %，18 Mitarbeiter，Eigenkapital €1.7M）+ Northdata（HRB 4103 KI；LEI 529900FOV9RXV8MQPE96；2007-10-09 as Dierck Sicherheitstechnik GmbH）+ LinkedIn（2007；11–50；Systemintegrator IT-Networking / Security / ADC）+ Datanyze（Mats Hansen — Head of Information Security）+ Empack（DIERCK GROUP 260 人，140 年历史）',
    url='https://bma-networks.com/impressum',
    number='HRB 4103 KI（Amtsgericht Kiel）· LEI 529900FOV9RXV8MQPE96 · USt-ID DE167682158', status='Aktiv（2024 账已公示 2026-02-18）', incorporated='2007-10-09（原名 Dierck Sicherheitstechnik GmbH）', company_type='GmbH（DIERCK GROUP 集团成员）',
    sic=['IT 系统集成：企业网络、IT 安全、应用交付（ADC）、咨询与实施（厂商认证工程师；全德客户）'],
    address='Preetzer Chaussee 55, 24222 Schwentinental（总部）；Albert-Einstein-Ring 5, 22761 Hamburg（分部）', accounts='2024 账：总资产 €4.5M，权益 €1.7M，18 人', accounts_due='—', size_band='小型（18 人；集团 260 人）',
    officers=['Alisa Ehrk — Geschäftsführerin', 'Wolfgang Ehrk — Geschäftsführer / 内容责任人', 'Mats Hansen — Head of Information Security = 研究档 KP mats.hansen@（**非采购 / 非网络选型人**）'], psc='DIERCK GROUP (Holding)', charges='', prev_names=['Dierck Sicherheitstechnik GmbH（2007）'],
    lines=['**企业级 SI（Cisco / F5 一类项目）+ 研究档 KP 是信息安全负责人** → Saga 产品对口度低 → **集成商 25% 低概率，一页纸即止**：STC-4424GCPM / STC-424XGGPM-280W（楼宇接入 PoE 替代款）+ STC-110XGE；不加厚',
           '收件人改 info@ 点名「Einkauf / Netzwerk-Projektleitung」，Mats Hansen 抄送；表内 1 次跟进无回复 → 第二次触达一次后 `when=不动`；发信窗口 Thu 12–14 CET'],
    notes='集成商 25% 低概率；一页纸；KP 非采购。')
put('SB-493', key='de', batch=B, name='Syserso Networks GmbH（syserso.com；Hannover）— ITTC Group 旗下电信网络 / VoIP 安全 / KRITIS 方案增值分销与集成商（Ribbon「Best Channel Performer 2026」；ISO 9001 / 45001 / 27001）；Amtsgericht Hannover HRB 217735；2019-01-29 成立为 Corning Services GmbH，2021-12 更名；资本 €260,000；**GF Naif Kiy = 研究档 KP 本人**（+ GF Michael Clever 2024-11 起）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（Syserso Networks GmbH – an ITTC Group Company；Ahrensburger Straße 8, 30659 Hannover；Geschäftsführer Naif Kiy, Michael Clever；Amtsgericht Hannover HRB 217735；USt-ID DE 216719491；+49 511 740192-0）+ registercheck（Aktiv；资本 €260,000；GF Michael Clever *1965 / Naif Kiy *1969，登记 2024-11-22）+ online-handelsregister（成立 2019-01-29；最后变更 2021-12-20）+ OpenCorporates（2021-11/12 由 Corning Services GmbH 更名 Syserso Networks GmbH；Naif Kiy / Timothy Leonard GF 2019 起；Prokurist Detlef Böse）+ companyhouse（Naif Kiy GF seit Jan 2019）+ Xing 新闻（Ribbon INSIGHTS EMEA 2026 Best Channel Performer；GF Naif Kiy、销售总监 Holger Kausch）+ ContactOut（VoIP 安全、KRITIS 运营商方案；ISO 9001 / 45001 / 27001）',
    url='https://www.syserso.com/impressum/',
    number='HRB 217735（Amtsgericht Hannover）· USt-ID DE216719491', status='Aktiv（Creditreform 最后变更 2024-11-22）', incorporated='2019-01-29（原 Corning Services GmbH；2021-12 更名）', company_type='GmbH（资本 €260,000；ITTC Group 成员）',
    sic=['电信运营商 / 关键基础设施网络方案增值分销与集成（Ribbon 会话边界控制 / VoIP 安全、传输、接入）；全德区域销售处'],
    address='Ahrensburger Straße 8, 30659 Hannover', accounts='—', accounts_due='—', size_band='小型 / 中型（人数未取；4 名登记管理人）',
    officers=['Naif Kiy — Geschäftsführer（*1969，2019 起）= **研究档 KP naif.kiy@ 本人**', 'Michael Clever — Geschäftsführer（*1965，2024-11 起）', 'Holger Kausch — Vertriebsleiter', 'Detlef Böse — Prokurist（2019）'], psc='ITTC Group', charges='', prev_names=['Corning Services GmbH（2019–2021）'],
    lines=['**运营商 / KRITIS 增值分销（Ribbon 线）+ GF 本人收件** → 可切「接入 / 汇聚以太网交换机作为其方案配套」→ **分销 20% 低中概率**：STC-424XGGPM-280W / STC-448XGGPM（机房汇聚）+ STC-110XGE + STH-2C24XF-HSI（25G ToR）；一页纸 + DC 线规格，不加厚',
           '表内 1 次跟进无回复 → 第二次触达换主题「Ethernet access/ToR switches to complement your Ribbon deployments」；发信窗口 Thu 12–14 CET'],
    notes='分销 20% 低中概率；KP = GF 本人；一页纸。')
put('SB-617', key='de', batch=B, name='Industrial Personal Computer 2U GmbH（2024-11-15 前名 IPC2U GmbH；ipc2u.de / ipc2u.com；Langenhagen bei Hannover）— 25 年以上的工业电脑 / 嵌入式 / 面板 PC / 工业网络方案分销商兼系统集成商（EMEA；台湾采购口 +886；RuggON 等品牌分销）；Amtsgericht Hannover HRB 201075；**GF Arthur Barasch = 研究档 KP 本人**', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（Industrial Personal Computer 2U GmbH；Frankenring 6, D-30855 Langenhagen；+49 511 807 259-0；sales@ipc2u.de；USt-IdNr DE250846309；WEEE DE 353 065 04；台湾电话 +886 (2) 2930 1196）+ evsedo.de Impressum（Register AG Hannover HRB B201075；Geschäftsführer Arthur Barasch）+ Northdata（HRB 201075；LEI 5299004NVERIA0XMW716；2024-11-15 Name: Industrial Personal Computer 2U GmbH，此前 IPC2U GmbH；MD Arthur Barasch）+ companyhouse（Arthur Barasch, Berlin；alleinvertretungsberechtigt；另任 inektra GmbH / invara UG）+ 官网首页（「internationaler Anbieter und Systemintegrator für industrielle Computing-Lösungen mit mehr als 25 Jahren Erfahrung」；工业 PC / 嵌入式 / 面板 PC / 边缘服务器 / 19 英寸机架 / **industrielle Netzwerklösungen**；定制平台）+ openPR（IPC2U 成为 RuggON 德国分销商）',
    url='https://www.northdata.com/Industrial%20Personal%20Computer%202U%20GmbH,%20Langenhagen/Amtsgericht%20Hannover%20HRB%20201075',
    number='HRB 201075（Amtsgericht Hannover）· LEI 5299004NVERIA0XMW716 · USt-ID DE250846309', status='Aktiv（Embedded World 2026 参展）', incorporated='未取（经营 25 年以上；公司号 2010 年代）', company_type='GmbH（GF Arthur Barasch，单独代表权）',
    sic=['工业电脑 / 嵌入式 / 面板 PC / 工业边缘服务器 / 19 英寸机架电脑分销与系统集成（整机装配、OS 预装、测试）', '工业网络方案（交换机 / 网关 / IoT 网关）配套分销'],
    address='Frankenring 6, 30855 Langenhagen', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['Arthur Barasch — Geschäftsführer（Berlin；单独代表）= **研究档 KP barasch@ 本人**'], psc='Arthur Barasch（推定）', charges='', prev_names=['IPC2U GmbH（— 2024-11）'],
    lines=['**工业 PC 分销 + 自带「工业网络方案」品类 + 台湾采购口 + GF 本人收件 → 分销 20%（可谈 IPC2U 标工业交换机 OEM 30%）**：STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM / STI-0240GE（导轨宽温，配其工业 PC 方案）；B BIG，**加厚**（对标台系工业交换机价 + 3 年保修 + MOQ 1）',
           '表内 1 次跟进无回复 → 第二次触达换主题「DIN-rail managed switches as a second source beside your Taiwan line — your label possible」；发信窗口 Thu 12–14 CET；升 A 候选（回信即 A）'],
    notes='分销 20% / 可谈贴标；KP = GF 本人；B BIG；加厚；升 A 候选。')

# ---------------- GB 4 ----------------
put('SB-385', key='gb', batch=B, name='DTS Digital（dtsdigitalcctv.co.uk；Scarborough, North Yorkshire）— 2009 年起的在线 CCTV 设备分销商（Genie / ZIP / SPRO / Vectus / NiteDevil / Alien / IRLAB / Dahua / Hanwha 授权分销；2–10 人；Owner Derek Stephenson）；**Companies House 同名 DTS DIGITAL LIMITED 06949184（Sheffield，2024-05 注销，董事 Southwell / Atherton）疑非本户 → 未坐实（法人主体未定）**', iso='GB', fetched=F,
    source='GB · 1 次检索：官网 company_info（DTS Digital；95–99 Dean Road, Scarborough YO12 7QS；contact@）+ RocketReach（2009；4 人；Owner Derek Stephenson）+ LinkedIn（2009；2–10；Self-Owned；Scarborough）+ Trustpilot / Professional Security（2009 起；Genie / ZIP / SPRO / Vectus / NiteDevil / Alien / IRLABS / Dahua / Hanwha 授权分销；联系人 D Stephenson；43 Newby Farm Road YO12 6UJ）+ Companies House 06949184（DTS DIGITAL LIMITED；Dinnington, Sheffield；2009-07-01 成立；**Dissolved 2024-05-07**；董事 Martin Raymond Southwell / Michael Albert Atherton / Melanie Southwell）—— 地址与人员均不符，疑同名他户；Scarborough 主体（Ltd 或个体）未取',
    url='https://www.dtsdigitalcctv.co.uk/company_info.asp',
    number='未坐实（Scarborough 主体未取；CH 06949184 疑他户且已注销）', status='站点在线（2024-05 更新）', incorporated='2009（自述）', company_type='未取（Self-Owned；疑个体 / 小 Ltd）',
    sic=['CCTV 设备在线分销（HD IP / HD 模拟 / 套件）面向行业与零售客户，欧洲发货'],
    address='95–99 Dean Road, Scarborough, North Yorkshire YO12 7QS', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Derek Stephenson — Owner（RocketReach / Professional Security「D Stephenson」）= 收件人', 'Pavel Tsenov — 研究档 KP contact@（职务未核）'], psc='Derek Stephenson（推定）', charges='', prev_names=[],
    lines=['**微型在线 CCTV 分销** → **分销 20% small，一页纸**：STC-028GP / STC-228GP / STC-2216GP（配其 IP 套件；3 年保修对齐其「up to 3 years warranty」口径 → 用 STI 或写明延保）',
           '收件人 contact@ 点名 Derek Stephenson；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 12–14 GMT；下轮补项：站点 Terms 法人名'],
    notes='分销 20% small；一页纸；未坐实（主体待定）。')
put('SB-386', key='gb', batch=B, name='DVS LTD（dvs.co.uk；Cardiff，Unit 3 Neptune Point）— 2003 年成立的 Hikvision 英国主要分销商（CCTV / 门禁 / 报警 / 智能家居）；2016 管理层收购，**2022-01 Midwich plc 取得多数股权**（母公司 Cooper Projects Limited 10121998 = PSC）；MD Tim Goodson；Companies House 04963144；注册地 c/o Midwich, Diss', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 04963144（DVS LTD；Active；2003-11-13 成立；注册地 C/O Midwich Limited, Vinces Road, Diss IP22 4YT（2022-01-20 由 Cardiff 迁入）；PSC Cooper Projects Limited 10121998（2016-06-20 起）；董事 Timothy Goodson 2016 / Gavin Francis Dunleavy 2013 / Stephen Barry Fenby 2022 / Mark Daniel Lowe 2022 / Adam Thomas Councell 2026-03-02）+ Endole（Hikvision CCTV 分销；Gavin Dunleavy — Commercial Director）+ theorg（Tim Goodson MD；David Davies 技术总监；Lynsey Morgan 财务总监；Josh Whitehead Head of Sales）+ SecurityInformed 2016（MBO，HSBC 融资）+ ChannelWeb 2022-01（Midwich 收购多数股权；Hikvision / Toshiba 分销）+ RocketReach（157 人；$6.6M —— 第三方，仅作区间）',
    url='https://find-and-update.company-information.service.gov.uk/company/04963144',
    number='Companies House 04963144', status='Active（新董事 2026-03-02）', incorporated='2003-11-13', company_type='Private limited company（Midwich plc 旗下，经 Cooper Projects Limited 控股）',
    sic=['安防产品分销（Hikvision 英国主分销；CCTV / 视频火灾探测 / 门禁 / 报警 / 智能家居），面向行业安装商'],
    address='Unit 3, Neptune Point, Vanguard Way, Cardiff CF24 5PG（经营地；注册地 c/o Midwich, Diss）', accounts='—（Midwich 集团并表）', accounts_due='—', size_band='中型（第三方 100+ 人；集团上市公司）',
    officers=['Timothy Goodson — Managing Director / Director（2016 起）', 'Gavin Francis Dunleavy — Commercial Director / Director（2013 起）', 'Stephen Barry Fenby / Mark Daniel Lowe — Director（Midwich 方，2022）', 'Adam Thomas Councell — Director（2026-03）', 'Josh Whitehead — Head of Sales', 'Scott Abraham — 研究档 KP scott.abraham@（职务未核）'], psc='Cooper Projects Limited（10121998）→ Midwich plc', charges='', prev_names=[],
    lines=['**上市集团旗下 Hikvision 主分销 → 供应商准入正式、绑定 Hikvision 生态 → 分销 20% 低概率但体量大**：切口 = 「非 Hikvision 的网络侧」STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W 作为其 PoE 交换机第二货源；一页纸即止，不加厚',
           '收件人：Scott Abraham（研究档，已在收）+ 点名 Commercial Director Gavin Dunleavy / Head of Sales Josh Whitehead；研究档站点 http_error → 用 CH / theorg 信息；表内 1 次跟进无回复 → 第二次触达一次；发信窗口 Thu 12–14 GMT'],
    notes='分销 20% 低概率（Midwich 集团）；一页纸。')
put('SB-390', key='gb', batch=B, name='SSED Ltd（T/A Hunters Wholesalers；hunters-wholesalers.co.uk；Maidenhead，前址 Slough / Langley）— 2003 年起的多品牌电子安防批发商（CCTV / 门禁 / 对讲 / 入侵 / 消防；Hikvision / Videx / Fike / Bosch；2–10 人）；Companies House **04864055**（Terms 页）；联系人 Harjinder Narula；（HUNTERS WHOLESALERS LIMITED 06486469 = 2011 注销旧壳）', iso='GB', fetched=F,
    source='GB · 1 次检索：官网 Terms（「Hunters Wholesalers, a trading name of SSED Ltd, company registration number 04864055 and registered office at Trade City, Unit 3 Martin Road, Clivemont Park, Maidenhead SL6 7DZ」）+ 官网 About（SSED T/A Hunters Wholesalers；2003 起；独立多品牌分销）+ LinkedIn（2003；2–10；Slough；Hikvision / Videx / Fike / Bosch）+ Kompass（SIC 80200；0–9 人；注册号误列 06486469）+ Companies House 06486469（HUNTERS WHOLESALERS LIMITED；2008-01-28 成立；**Dissolved 2011-02-22**；242 Trelawney Avenue, Langley = 旧壳）+ construction.co.uk（Mr Harjinder Narula）+ securitysuppliesdirect.co.uk（sales@hunters-wholesalers.co.uk；01628 669 124；同址）',
    url='https://www.hunters-wholesalers.co.uk/information/terms?language=en-gb',
    number='Companies House 04864055（SSED Ltd）；旧壳 HUNTERS WHOLESALERS LIMITED 06486469 已注销 2011', status='Active（站点在线；多址运营）', incorporated='2003（自述；SSED Ltd 号段 2003）', company_type='Private limited company（SSED Ltd 以 Hunters Wholesalers 商号经营）',
    sic=['80200 — 安防系统服务（实为电子安防设备多品牌批发：CCTV / 门禁 / 对讲 / 报警 / 消防 / 卫星电视 / 配钥匙）'],
    address='Trade City, Unit 3 Martin Road, Clivemont Park, Maidenhead SL6 7DZ（另址 Unit 4A Kelpatrick Road, Slough SL1 6BW）', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Harjinder Narula — 联系人 / 负责人（construction.co.uk；董事身份未核）= 收件人（研究档无 KP）'], psc='未取', charges='', prev_names=['HUNTERS WHOLESALERS LIMITED（06486469，2008–2011 旧壳）'],
    lines=['**微型多品牌安防批发** → **分销 20% small，一页纸**：STC-028GP / STC-228GP / STC-2216GP（对标其 Hikvision PoE 交换机在售价）',
           '收件人 sales@ 点名 Harjinder Narula；表内无跟进（研究档站点 timeout）→ 首信即一页纸；发信窗口 Thu 12–14 GMT；下轮补项：CH 04864055 董事 / 账目'],
    notes='分销 20% small；一页纸；CH 04864055 待补董事。')
put('SB-770', key='gb', batch=B, name='LANODE LIMITED（lanode.com / lanode.co.uk；Camberley, Surrey）— 1992 年成立的网络 / 传输 / 数据通信专业分销商（媒体转换器、工业以太网、交换机、PoE、SFP、CWDM / DWDM、串口服务器、E1 / G.SHDSL；KBC Networks 合作伙伴）；Companies House 02702078；**Managing Director Donal McDonnell（80% 股东）= 研究档 KP 本人**；2–10 人', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 02702078（LANODE LIMITED；Active；1992-03-31 成立；注册地 White Lodge, Saville Gardens, Camberley GU15 1DF；董事 Donal McDonnell *1958-03，1992 起）+ Pomanda（SIC 61100；最大股东 Donal McDonnell 80%）+ Endole（Company Secretary Raquel McDonnell；2 名股东、1 名 PSC）+ GlobalDatabase（Ian Philip — Technical Manager；Nige Howarth — Marketing；Mia Steward-Storey — Internal Sales）+ D&B（Managing Director Donal McDonnell；+44 1276 677220）+ prospeo（经营地 Unit 1 Phase 4, Albany Park, Camberley GU16 7PL；1–10 人）+ 官网 Products（Industrial Ethernet Managed & Unmanaged、PoE、Ethernet Switches、Media Converters、CWDM/DWDM）+ Light Reading 2023-11（Lanode 扩大与 KBC Networks 合作）',
    url='https://find-and-update.company-information.service.gov.uk/company/02702078',
    number='Companies House 02702078', status='Active', incorporated='1992-03-31', company_type='Private limited company（Donal McDonnell 80%）',
    sic=['61100 — 有线电信活动（实为网络 / 传输 / 数据通信设备专业分销：媒体转换器、工业以太网、交换机、PoE、光模块、复用器、串口服务器）'],
    address='White Lodge, Saville Gardens, Camberley GU15 1DF（注册）；Unit 1 Phase 4, Albany Park, Camberley GU16 7PL（经营）', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Donal McDonnell — Director / Managing Director（*1958；80%）= **研究档 KP donal@ 本人**', 'Raquel McDonnell — Company Secretary（股东）', 'Ian Philip — Technical Manager', 'Mia Steward-Storey — Internal Sales'], psc='Donal McDonnell（80%）', charges='', prev_names=[],
    lines=['**产品线与 Saga 完全同向（工业以太网 / PoE / 媒体转换）+ 老板本人收件 + 已代理 KBC（美系工业交换机）→ 分销 20%**：STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM（对标 KBC 工业线价，3 年保修）+ STC-228GP / STC-2224GP；加厚一次（工业线对标价表）',
           '表内 1 次跟进无回复 → 第二次触达换主题「a value industrial Ethernet line beside KBC — managed L2+, 3-year warranty, MOQ 1」（不点名 KBC）；发信窗口 Thu 12–14 GMT；升 A 候选（回信即 A）'],
    notes='分销 20%；KP = MD / 80% 股东本人；加厚一次；升 A 候选。')

# ---------------- PL 4 ----------------
put('SB-199', key='pl', batch=B, name='Kore Konect Sp. z o.o.（korekonect.com；Warszawa Bartycka 22B/21A）— 2021-05-05 注册的结构化布线 / 机柜 / 交换机 / UPS「品牌制造商」（自称 manufacturer；产品线含 PoE / 工业 PoE 交换机、媒体转换器、SFP）；资本仅 5,000 zł、注册地为住宅楼；中东经销页（gabs-me.com）→ 疑为外资贸易型自有品牌公司', iso='PL', fetched=F,
    source='PL · 1 次检索：krs-pobierz（KORE KONECT SPÓŁKA Z O.O.；KRS 0000898338；NIP 5213927829；REGON 388906180；aktywna；资本 5,000 zł；ul. Bartycka 22B/21A, 00-716 Warszawa；登记 2021-05-05；最近变更 2024-08-13；主营 PKD 32.99 其他制造）+ 官网（Kore Konect；结构化布线铜缆 / 光纤、服务器机柜 7U–47U、Ethernet / PoE / Industrial PoE Switches、Media Converter、SFP、UPS、控制电缆；BARTYCKA 22B M21A；info@korekonect.com）+ gabs-me.com（中东经销页：「Polish based manufacturer of … Network Switches and UPS」）；Warszawa 的 KORE Sp. z o.o.（广告公司，KRS 0000206537）与 Szczecin 的 Kore Poland 为同名他户，不采',
    url='https://krs-pobierz.pl/kore-konect-spolka-z-ograniczona-odpowiedzialnoscia-i7120353',
    number='KRS 0000898338 · NIP 5213927829 · REGON 388906180', status='Aktywna（KRS 变更 2024-08-13）', incorporated='2021-05-05', company_type='Spółka z o.o.（资本 5,000 zł —— 法定最低；董事会代表）',
    sic=['PKD 32.99.Z — 其他制造（实为自有品牌 Kore Konect：布线 / 机柜 / 交换机 / UPS，外采贴牌出口至中东等地）'],
    address='ul. Bartycka 22B/21A, 00-716 Warszawa（住宅楼）', accounts='—', accounts_due='—', size_band='微型（资本 5,000 zł；人数未取）',
    officers=['董事会成员姓名未取（研究档无 KP；info@）'], psc='未取', charges='', prev_names=[],
    lines=['**自有品牌但壳型公司（5,000 zł 资本、住宅地址、面向中东经销）** → 贴标需求真实但付款与量存疑 → **贴标 small：一页纸 + 预付款条款**（Kore Konect 标 STC-028GP / STC-228GP / STI-054GP），T/T 100% 预付、MOQ 1、不赊',
           '收件人 info@；表内「已售 E-wind」→ 已有华南货源 → 第二次触达换主题「managed L2+ PoE under your label — 3-year STI warranty」；发信窗口 Thu 12–14 CET；不加厚'],
    notes='贴标 small；壳型公司预付；一页纸。')
put('SB-415', key='pl', batch=B, name='A2S（a2s.pl；波兰）— 研究档 KP Maciej Łuczyński ml@a2s.pl；**本轮 1 次检索未命中登记主体（仅见 MAJOA Sp. z o.o. 董事 Maciej Piotr Łuczyński，未证同人）→ 未坐实**', iso='PL', fetched=F,
    source='PL · 1 次检索（关键词 A2S a2s.pl Maciej Łuczyński KRS）→ 返回 Polskie Sieci Teleinformatyczne S.A.、Łuczyński i Partnerzy、MAJOA Sp. z o.o.（KRS 0001014967；Maciej Piotr Łuczyński 董事 2023 起，150 udziałów）、A2Systems（NIP 6331740751）、A2 Sp. z o.o. 等 —— 均无法与 a2s.pl 对应；按「1 次未中即停」规则不再追；站点事实沿用研究档（a2s.pl，角色判定来源：官网文案）',
    url='https://a2s.pl/',
    number='未坐实（登记主体未取）', status='站点在线（研究档快照 ok）', incorporated='未取', company_type='未取',
    sic=['网络 / 弱电产品分销或集成（研究档官网文案判定；细分未核）'],
    address='波兰（门牌未取）', accounts='—', accounts_due='—', size_band='未取',
    officers=['Maciej Łuczyński — 研究档 KP ml@a2s.pl（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**未坐实** → 坐实前只发一页纸（STC-228GP / STC-2224GP / STI-144GP）；下轮补项：站点 Regulamin / Kontakt 页法人名 + NIP 再查 KRS / CEIDG',
           '收件人 ml@；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 12–14 CET'],
    notes='未坐实（1 次未中）；一页纸；下轮补项。')
put('SB-418', key='pl', batch=B, name='ATEL ELECTRONICS Sp. z o.o.（atel.com.pl；Opole）— 光纤技术 / 工业与无线通信元件进口分销商，**ORing Industrial Networking 波兰授权分销**（工业交换机 / 媒体转换器 / 串口服务器、热成像、测量仪器、售后件）；KRS 0001010225（2023-01-02 登记，前身个体推定）；资本 50,000 zł；第三方营收区间 3.5–9.7 mln zł', iso='PL', fetched=F,
    source='PL · 1 次检索：官网页脚 / Zasady sprzedaży（Atel Electronics Sp. z o.o.；ul. Oleska 121, 45-231 Opole；Kapitał zakładowy 50.000,00；KRS 0001010225；Sąd Rejonowy w Opolu VIII Wydział KRS；REGON 524050890；NIP 7543356130）+ 官网 ORing 页（「Atel Electronics jest autoryzowanym dystrybutorem produktów firmy ORing Industrial Networking w Polsce」；ITS / 能源 / EN 50155 产品）+ krs-pobierz（登记 2023-01-02；最近变更 2026-06-30；主营电子 / 电信设备批发）+ bizraport（营收 3.5 / 9.7 mln zł 两档；光纤技术、工业 / 无线通信、工业交换机、热成像、售后件）+ Facebook（进口与分销网络元件、测量设备）+ Marketplanet 供应商库',
    url='https://krs-pobierz.pl/atel-electronics-spolka-z-ograniczona-odpowiedzialnoscia-i0001010225',
    number='KRS 0001010225 · NIP 7543356130 · REGON 524050890', status='Aktywna（KRS 变更 2026-06-30）', incorporated='2023-01-02（Sp. z o.o. 登记；业务更早，前身推定个体）', company_type='Spółka z o.o.（资本 50,000 zł）',
    sic=['PKD 46.52.Z — 电子 / 电信设备批发（光纤技术、工业通信 ORing、无线、热成像、测量仪器、售后件进口分销）'],
    address='ul. Oleska 121, 45-231 Opole', accounts='第三方营收区间 3.5–9.7 mln zł（仅作区间）', accounts_due='—', size_band='小型（人数未取）',
    officers=['董事会姓名未取（研究档无 KP；cust@）'], psc='未取', charges='', prev_names=[],
    lines=['**ORing 授权分销（台系高价工业线）→ Saga STI 正好做其「价值线」第二货源 → 分销 20%**：STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM 对标 ORing IPS / IGS 系列价（表内「ORing 工业线在售（高价）」）+ STI-0240GE；ITS 道路 / 能源场景谈，**轨交 EN 50155 不谈（守界）**；加厚一次（对标价表）',
           '收件人 cust@ 点名「dział handlowy / właściciel」；表内 1 次跟进无回复 → 第二次触达换主题「a value industrial line beside ORing — managed L2+, -40~75 °C, 3-year warranty」（不点名 ORing）；发信窗口 Thu 12–14 CET；下轮补项：KRS 董事会'],
    notes='分销 20%；加厚一次；轨交守界；董事会下轮补。')
put('SB-674', key='pl', batch=B, name='Noxel Sp. z o.o.（noxel.pl；Chorzów，前址 Katowice）— 2019 年成立的电子 / 安防网店（摄像机、NVR、网络、路由器、报警、视频对讲）；KRS 0000799308；资本 5,000 zł；PKD 47.91.Z 邮购 / 网络零售', iso='PL', fetched=F,
    source='PL · 1 次检索：官网 Kontakt / Regulamin（Noxel Sp. z o.o.；ul. Katowicka 16B, 41-500 Chorzów；KRS 0000799308；NIP 6762569629；REGON 384126338；资本 5,000 zł；kontakt@noxel.pl；32 708 55 36）+ GoWork / imsig / infoveriti（同号；aktywna）+ pkt / biznesfinder（2019 成立；PKD 47.91.Z；旧址 Józefowska 76, 40-145 Katowice）+ Facebook（「Sklep z elektroniką i zabezpieczeniami. Kamery, rejestratory, sieci, routery, alarmy, wideodomofony」）',
    url='https://noxel.pl/regulamin/',
    number='KRS 0000799308 · NIP 6762569629 · REGON 384126338', status='Aktywna（站点 2026-08 更新）', incorporated='2019', company_type='Spółka z o.o.（资本 5,000 zł）',
    sic=['PKD 47.91.Z — 邮购 / 网络零售（电子与安防：摄像机 / NVR / 网络 / 路由器 / 报警 / 视频对讲）'],
    address='ul. Katowicka 16B, 41-500 Chorzów（旧址 ul. Józefowska 76, 40-145 Katowice）', accounts='—', accounts_due='—', size_band='微型（资本 5,000 zł）',
    officers=['董事会姓名未取（研究档无 KP；kontakt@）'], psc='未取', charges='', prev_names=[],
    lines=['**微型安防网店** → **分销 20% small，一页纸**：STC-028GP / STC-228GP（零售款 4–8 口 PoE）；MOQ 1 + DAP 华沙',
           '收件人 kontakt@ 点名 właściciel；表内无跟进（用户表来源）→ 首信即一页纸；发信窗口 Thu 12–14 CET'],
    notes='分销 20% small；一页纸。')

print('b101 DE 4 + GB 4 + PL 4 written')
