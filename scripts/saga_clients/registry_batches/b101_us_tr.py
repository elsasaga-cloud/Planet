#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 101 批 · US 6 户 + TR 6 户（T29-U94，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。
选户 = 规程 §3「第 101 批」名单（B 档未建底数，按「自有 logo」+「打开次数」排序）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 101

# ---------------- US 6 ----------------
put('SB-081', key='us', batch=B, name='DABOS, Inc.（dabos.com / blog.dabos.com；美国，马里兰 Bethesda 一带推定）— 科研 / 实验室用品与设备采购供应商（「we support scientists and manufacturers of scientific supplies」；研究档 KP M. Zohaib Razzaq zohaib@）；**1 次检索未命中州登记 → 部分坐实（域名主体确认，州 / 法律形式未取）**', iso='US', fetched=F,
    source='US · 1 次检索：blog.dabos.com（DABOS, Inc.；「At DABOS we support, encourage and equip innovation by supporting scientists and manufacturers of scientific supplies」；2026-02 博文）+ LinkedIn 个人页（Anastasia Khobta — Controller, Dabos, Inc.；Bethesda）；加州 DABS, Inc.（心理健康机构）为同名他户，不采；州 SoS / 法律形式 / 成立日未取',
    url='https://blog.dabos.com/',
    number='部分坐实（Inc.；州登记号未取）', status='Active（博客 2026-02 更新；站点在线）', incorporated='未取', company_type='Corporation（推定；私有）',
    sic=['科研 / 实验室用品、仪器与 IT 设备采购供应（面向科研机构 / 政府实验室的集采型供应商，推定）'],
    address='美国（Bethesda, MD 一带推定；门牌未取）', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['M. Zohaib Razzaq — 研究档 KP zohaib@（询盘联系人；职务未核）', 'Anastasia Khobta — Controller（LinkedIn）'], psc='未取', charges='', prev_names=[],
    lines=['**采购型供应商（替科研 / 政府客户配货）而非渠道** → 有单就报、无单不追 → **一页纸 small**：按其询盘型号直接报价（STC-228GP / STC-2224GP / STI-144GP），MOQ 1、DAP 报价、15 天有效',
           '研究档「见 Clients 表询盘联系人」→ 回复走原询盘线程（不伪造 Re:）；发信窗口 Wed 08–10 ET；不加厚'],
    notes='采购型供应商；一页纸 small；部分坐实。')
put('SB-223', key='us', batch=B, name='2M Technology（2M Technology Inc. / 2M Solutions Inc.；2mtechnology.net；Grand Prairie, TX）— 2004 年起（LinkedIn 2012 / 行业名录 2009）的商业与工业安防集成商兼自有品牌摄像机 / NVR 组装商（防爆摄像机、太阳能监控拖车、X 光机、UniFi 网络；Texas Security License B15309；11–50 人 / 20 人；2017 迪拜办事处）', iso='US', fetched=F,
    source='US · 1 次检索：官网 About（「founded in 2004 at our current base of Grand Prairie, Texas」；2004 首个组装厂出 600 TVL 模拟摄像机；2017 「extended 1000ft PoE 4MP IP camera … all extended PoE built-in switch NVR」+ 迪拜办事处；licensed commercial security integrator B15309）+ 官网首页（Grand Prairie HQ；DFW 全域）+ SDM Buyers Guide（Year Founded 2009；20 名员工；Texas Security License B15309；防爆摄像机 / X 光机 / 集装箱转闸 / 移动监控拖车）+ LeadIQ（NAICS 56162；2009；11–50；(214) 988-4302）+ ContactOut（法律名 2M Solutions Inc.；802 Greenview Dr, Grand Prairie, TX 75050）+ Thomasnet（2M Technology Inc.；Manufacturer；2004）+ LinkedIn（11–50；2012）；TX SoS 文件号未取',
    url='https://www.2mtechnology.net/about-us/',
    number='TX 实体（2M Technology Inc. / 2M Solutions Inc. 并存；SoS 文件号未取）· Texas Security License B15309', status='Active（官网 2026-10 更新；SDM 2026-08）', incorporated='2004（自述）/ 2009（行业名录）/ 2012（LinkedIn）', company_type='Corporation（私有）',
    sic=['NAICS 561621 — 安防系统集成（监控 / 门禁 / 报警 / 消防 / X 光 / 车牌识别 / UniFi 网络）', '自有品牌摄像机 / NVR 组装（防爆机壳定制；「extended PoE built-in switch NVR」）'],
    address='802 Greenview Dr, Grand Prairie, TX 75050', accounts='—', accounts_due='—', size_band='小型（11–50 人；20）',
    officers=['Mohamed Malek — 研究档 KP mohamed@（职务未核；疑为业主 / 负责人）', 'Jarga Jallow — 研究档 KP（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**自有标摄像机 / NVR + 集成商身份 + 已在卖「内置 PoE 交换的 NVR」** → 自有标 PoE 交换机是顺手的补位 → **贴标 OEM 30% 目标（2M 标 STC-228GP / STC-2224GP / STC-4424GCPM）兼集成商 25%**；石油 / 化工防爆现场只谈控制室侧商业 PoE（不碰 IP67 / 防爆）；政府客户不提 NDAA',
           '收件人 Mohamed Malek 主送 + Jarga Jallow 抄；研究档「角色判定来源：用户表」→ 表内 1 次跟进无回复 → 第二次触达换主题「PoE switches under your 2M label to ship with your NVR kits」；发信窗口 Wed 08–10 CT；加厚一次'],
    notes='贴标 OEM 30% 目标 + 集成商 25%；加厚一次；SoS 文件号下轮补。')
put('SB-403', key='us', batch=B, name='Surveillance-Video.com（surveillance-video.com；New York, NY 387 Canal Street）— BBB A+ 认证的安防摄像机 / 监控设备在线零售批发商（表内「已售 E-link PoE 配件」）；**法定名未取 → 部分坐实**', iso='US', fetched=F,
    source='US · 1 次检索：BBB 类目页（Surveillance-Video.com；Accredited Business；BBB Rating A+；Surveillance Equipment / Security Cameras / Security System Monitors；(800) 955-5201；387 Canal Street, New York, NY 10013；Service Area USA）×4 页一致；法定名 / NY DOS 号未取（BBB 详情页未入结果）',
    url='https://www.bbb.org/us/ny/manhattan/category/security-equipment',
    number='部分坐实（NY 实体；法定名 / DOS 号未取）', status='Active（BBB 认证在册）', incorporated='未取', company_type='未取（私有零售批发商）',
    sic=['安防摄像机 / NVR / 监视器 / PoE 配件在线零售与批发（全美发货）'],
    address='387 Canal Street, New York, NY 10013', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['无具名（研究档 info@）'], psc='未取', charges='', prev_names=[],
    lines=['**在线安防零售 + 已卖 PoE 配件** → **分销 20% small，一页纸**：STC-028GP / STC-228GP（4–8 口 PoE 零售款）+ STC-2216GP；MOQ 1、DAP 纽约',
           '收件人 info@ 点名 purchasing；表内无具名 KP；发信窗口 Wed 08–10 ET；下轮补项：BBB 详情页法定名'],
    notes='分销 20% small；一页纸；部分坐实。')
put('SB-532', key='us', batch=B, name='Eclipse CCTV Inc.（DBA Eclipse Security；eclipsecctv.com / eclipsesurveillance.com；Hollywood, FL）— 1998 年起的自有品牌 CCTV / NVR / 门禁品牌商（Eclipse 标，3 年保修；「只经 Ft Lauderdale 的 CCTV Outlet, Inc 分销」）；Sunbiz P20000058672 Active；President Moises Faroy；10–19 人；$1–5M', iso='US', fetched=F,
    source='US · 1 次检索：Sunbiz 实体名列表（ECLIPSE CCTV INC. P20000058672 Active；旧实体 P03000006534 INACT、L20000138773 InActive）+ D&B（Eclipse CCTV Inc.；DBA Eclipse Security；Key Principal Moises Faroy；3900 N 29th Ave, Hollywood, FL 33020-1010）+ Buzzfile（Eclipse Cctv Inc.；Moises Faroy — President；(954) 929-3646）+ Explorium / Thomasnet（1998 成立；11–50 人；$500K–1M；员工 Tony Forbes — Sales executive；Manuel Alvarez；Ernesto Vazquez — Project manager）+ ZoomInfo（10–19 人；$1–5M）+ 官网博文（「Eclipse offers a 3-year manufacturers warranty … Eclipse products are only sold and distributed by CCTV Outlet, Inc in Ft Lauderdale」）+ Facebook（ECLIPSE CCTV INC.；sales@eclipsecctv.com）',
    url='https://search.sunbiz.org/Inquiry/corporationsearch/SearchResults?inquiryType=EntityName&searchTerm=ECLIPSE+CCTV+INC.',
    number='FL Sunbiz P20000058672（Active；前身 P03000006534 2003 已注销）', status='Active', incorporated='1998（自述；现实体 2020 重新登记）', company_type='Florida Profit Corporation（私有；President Moises Faroy）',
    sic=['自有品牌安防产品（摄像机 / DVR / NVR / 门禁 / 对讲）设计与进口，经关联分销商 CCTV Outlet, Inc. 出货；安防工程（SIC 7381）'],
    address='3900 N 29th Ave, Hollywood, FL 33020', accounts='—', accounts_due='—', size_band='小型（10–19 人；$1–5M）',
    officers=['Moises Faroy — President（D&B / Buzzfile）= 拍板人（研究档无）', 'Tony Forbes — Sales Executive = 研究档 KP tony@', 'Manuel Alvarez — 研究档 KP sales@', 'Ernesto Vazquez — Project Manager'], psc='Moises Faroy（推定）', charges='', prev_names=['ECLIPSE CCTV INC.（P03000006534，2003–）'],
    lines=['**自有品牌 + 3 年保修承诺 + 已有进口 / 分销闭环（CCTV Outlet）→ 贴标 OEM 30% 目标**：Eclipse 标 STC-028GP / STC-228GP / STC-2216GP / STC-2224GP（HRUI 1 年保修 vs 其 3 年承诺 → 需写明可延保或改 STI 3 年线）；B BIG，**加厚**',
           '收件人：Tony Forbes 主送（已在收）+ 点名 President Moises Faroy；研究档站点 http_error → 用 Facebook / BBB 信息；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Wed 08–10 ET；升 A 候选（回信即 A）'],
    notes='贴标 OEM 30% 目标；B BIG；加厚；升 A 候选。')
put('SB-621', key='us', batch=B, name='LANshack.com（Atcom Services, Inc. 旗下事业部；lanshack.com；Clark / Toms River, NJ）— 1993/1997 年起的结构化布线 / 光纤跳线制造 + 数据通信产品电商（在售 E-wind 媒体转换器 / 交换机；11–50 人 / 22 人；$4.4M）；**President Andrea Damiano = 研究档 KP 本人**；研究档「Tecra Tools, Inc.」为误配（Tecra Tools 是丹佛工具商）', iso='US', fetched=F,
    source='US · 1 次检索：LinkedIn 公司页（LANshack；1995 进入分销与制造；1996 行业首家全电商；1999 购得 LANshack.com；「LANshack.com is a division of Atcom Services, Inc.」；11–50 人；Toms River NJ；President Andrea Damiano、VP Tom Damiano、CFO Toni Casazza）+ ZoomInfo 个人页（Andrea Damiano — President of LANshack，2007 起；155 Meadow Rd Ste 100, Clark, NJ 07066；(732) 396-3600）+ 官网 linecard PDF（Director of Sales Andrea Damiano 888-568-1230 x1001 andrea@；NAICS 335921 / 334417 / 332212）+ 官网 About（「Made in the USA Since 1993」；制造商兼分销商）+ Datanyze（CEO Anthony Casazza；$4.4M；22 人；1991）+ PRWeb 2023（Founded in 1997 online distributor）；Buyers Guide 的 Tecra Tools Inc（Denver CO）= 他户不采；NJ 实体号未取',
    url='https://www.linkedin.com/company/lanshack',
    number='NJ 实体（Atcom Services, Inc. dba LANshack.com；NJ 登记号未取）', status='Active（Trustpilot 2026-09；站点 2025 更新）', incorporated='1993（自述）/ 1997（LANshack.com）', company_type='Corporation（私有；Damiano / Casazza 家族）',
    sic=['NAICS 335921 光纤线缆制造 / 334417 连接器制造 — 定制光纤 / 铜缆跳线制造', '数据通信产品电商分销（布线硬件、媒体转换器、交换机、工具测试仪）'],
    address='155 Meadow Rd, Suite 100, Clark, NJ 07066（LinkedIn 列 Toms River, NJ）', accounts='—', accounts_due='—', size_band='小型（11–50 人；22；$4.4M）',
    officers=['Andrea Damiano — President / Director of Sales = **研究档 KP andrea@ 本人**', 'Tom (Thomas) Damiano — Vice President', 'Anthony Casazza — CEO（Datanyze）', 'Toni Casazza — CFO'], psc='Damiano / Casazza 家族（推定）', charges='', prev_names=['Atcom Services, Inc.（母公司名）'],
    lines=['**总裁本人在收件 + 已卖华南 E-wind 交换机 / MC + 自产光纤跳线 → 分销 20% 首选 US**（LANshack 标也可谈 OEM 30%）：STC-228GP / STC-2216GP / STC-2224GP 对标其 E-wind 在售价 + STI-144GP / STI-288DGGPM 配其光纤产品 + STC-110XGE（10G 上联）；B BIG，**加厚**',
           '研究档法定名更正：Tecra Tools, Inc. → Atcom Services, Inc.（dba LANshack.com）；表内 1 次跟进无回复 → 第二次触达换主题「a managed PoE line beside E-wind — same source region, 3-year STI warranty」（不点名 E-wind）；发信窗口 Wed 08–10 ET；升 A 候选（回信即 A）'],
    notes='分销 20% 首选 US；KP = President 本人；B BIG；加厚；升 A 候选；法定名更正。')
put('SB-793', key='us', batch=B, name='WorldStar Security Cameras（WSSC；worldstarsecuritycameras.com / worldstarcctv.com；Pompano Beach, FL，前址 Hallandale Beach）— 2010 年起的安防摄像机 / NVR / 门禁 / 网络设备批发 + 安装商（dealer 计划 + **「Custom Branding」自有标服务**；Partnership；11–50 人 / <$5M）；**FL 法定名未取 → 部分坐实**', iso='US', fetched=F,
    source='US · 1 次检索：官网首页（WorldStar Security Cameras；500 S Dixie Hwy W, Pompano Beach, FL 33060；(954) 534-9485；sales@worldstarcctv.com；「wholesale distributor and installer of security cameras, NVRs, access control, and network equipment for dealers, installers, integrators」；菜单含 Dealer Registration / **Custom Branding**；自称 NDAA 设备）+ ZoomInfo（2010；11–50；<$5M；3121 W Hallandale Beach Blvd Ste 110；Rolf Vilaire — Business Development）+ RocketReach（2010；2 人；$1M）+ LinkedIn（Partnership；2010；11–50）+ Yelp（两址）；Sunbiz 法定名未取',
    url='https://worldstarsecuritycameras.com/',
    number='部分坐实（FL；法定名 / Sunbiz 号未取）', status='Active（官网 2026-09 更新）', incorporated='2010', company_type='Partnership（LinkedIn；私有）',
    sic=['安防摄像机 / NVR / 门禁 / 网络设备批发（dealer 计划）+ 本地安装 + 自有标（Custom Branding）服务'],
    address='500 S Dixie Hwy W, Pompano Beach, FL 33060（前址 3121 W Hallandale Beach Blvd Ste 108/110, Hallandale Beach, FL 33009）', accounts='—', accounts_due='—', size_band='小型（2–50 人；<$5M）',
    officers=['Rolf Vilaire — Business Development = 研究档 KP rv@worldstarcctv.com', '合伙人姓名未取'], psc='未取', charges='', prev_names=[],
    lines=['**自己给 dealer 做「Custom Branding」= 已有贴牌需求 → 贴标 OEM 30% 目标（WorldStar 标 STC-028GP / STC-228GP / STC-2216GP）兼分销 20%**；其 NDAA 口径 = 我们不承诺 NDAA（规则），信里只谈规格 / 价格 / 保修；加厚一次',
           '收件人 Rolf Vilaire（BD）；表内 1 次跟进无回复 → 第二次触达换主题「white-label PoE switches for your Custom Branding program」；发信窗口 Wed 08–10 ET；下轮补项：Sunbiz 法定名'],
    notes='贴标 OEM 30% 目标 + 分销 20%；加厚一次；部分坐实。')

# ---------------- TR 6 ----------------
put('SB-871', key='tr', batch=B, name='İntenet İletişim Teknolojileri Ltd. Şti.（intenet.com.tr；İstanbul Esenler Giyimkent）— 1993 年起的电信 / 网络系统集成商（1996 把 TDM 带入土耳其、银行广域网 70%；2000 起 Cisco 系统集成；2007 起能源板块：TEİAŞ 变电站自动化与通信、风 / 水 / 火电厂；AT&T 土耳其方案商；11–50 人）；**General Manager Ercan Öztürk = 研究档 KP 本人**', iso='TR', fetched=F,
    source='TR · 1 次检索：LinkedIn 公司页（İntenet İletişim Teknolojileri LTD.；1993；11–50；Oruçreis İstanbul；员工 Ercan Ozturk — General Manager）+ list.istanbul（Oruç Reis Mah. Giyimkent Sitesi Giyimkent 2. Sokak No 56, Esenler 34237；info@intenet.com.tr）+ 官网 About Us（1993 成立；1996 TDM；1997–2000 TDM 分销；2000 后 Cisco 系统集成（VEDOP 税务局自动化、Sütaş WAN、财政部）；AT&T 方案商；2007 能源板块；TEİAŞ 变电站通信专长）+ 官网 İletişim（同址）；MERSİS 号未取',
    url='https://tr.linkedin.com/company/intenet',
    number='Ltd. Şti.（İstanbul；MERSİS 号未取）', status='Active（站点 2021 内容；LinkedIn 在线）', incorporated='1993', company_type='Limited Şirket（私有）',
    sic=['电信 / 网络系统集成（广域网 / 局域网、Cisco）', '能源行业变电站自动化与通信（TEİAŞ 输电变电站、HES / RES / 火电厂）交钥匙工程'],
    address='Oruç Reis Mah. Giyimkent Sitesi, Giyimkent 2. Sokak No 56, 34237 Esenler / İstanbul', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Ercan Öztürk — General Manager（LinkedIn）= **研究档 KP ercan.ozturk@ 本人**', 'Adnan Bakar — 员工（LinkedIn）'], psc='未取', charges='', prev_names=[],
    lines=['**变电站 / 电厂通信集成商 + GM 本人收件 → 集成商 25%**：STI-288DGGPM / STI-488DGGPM（导轨宽温，变电站 SCADA 环网，IEC 61850 认证未取 → 只说「industrial-grade, -40~75 °C」不说合规）+ STI-0240GE（机房汇聚）；一页纸 + 工业线规格',
           '表内 1 次跟进无回复 → 第二次触达换主题「DIN-rail managed switches for substation LAN — 3-year warranty」；发信窗口 Thu 10–12 TRT；加厚一次'],
    notes='集成商 25%；KP = GM 本人；加厚一次；MERSİS 下轮补。')
put('SB-494', key='tr', batch=B, name='Teleone（Teleone Bilgi ve İletişim Hizmetleri；teleone.com.tr；İzmir Konak，Ankara 区域办）— 1999 年起的电子安防整体方案商兼品牌分销商（Brickcom / Nuuo / Digital Watchdog / Sunell 土耳其分销；2014 起 DMO 国家采购平台供应商前三；TSE-HYB / ISO 2008 起；Bilişim 500 两次；<$5M）；**法律形式 / MERSİS 未取 → 部分坐实**', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 Hakkımızda（İzmir 总部 800 m²；Ankara 区域经理处；Brickcom / Nuuo / Digital Watchdog 土耳其分销；2014 起 DMO 供应商、同领域前三；2008 起 TSE-HYB / ISO / OHSAS；Bilişim 500 两次；2016 全球最佳 Brickcom 分销商）+ ZoomInfo（1999 起；Mithatpaşa Cd. No 146 D 2-3, Konak, İzmir 35260；<$5M）+ 官网 İletişim（Mithatpaşa Cad. Zafer Apt. No 146 Kat 1 D 2-3 Konak / İzmir；0850 221 95 95）+ Facebook（info@teleone.com.tr）+ 官网首页（Sunell 热成像测温方案）；İstanbul 的 TELEON İletişim Hizmetleri（VKN 7350780251，2014）为同名他户，不采',
    url='https://www.teleone.com.tr/hakkimizda/',
    number='部分坐实（İzmir；法律形式 / MERSİS 号未取）', status='Active（站点在线；DMO 供应商）', incorporated='1999', company_type='未取（私有；自述 Bilgi ve İletişim Hizmetleri）',
    sic=['电子安防整体方案（视频监控 / 视频分析 / 网络 / 指挥中心）+ 外国品牌土耳其分销 + 公共采购（DMO）供货'],
    address='Mithatpaşa Cad. Zafer Apt. No 146 Kat 1 D 2-3, Konak / İzmir（Ankara 区域办）', accounts='—', accounts_due='—', size_band='小型（人数未取；<$5M）',
    officers=['无具名（研究档无 KP；info@）'], psc='未取', charges='', prev_names=[],
    lines=['**替外国品牌做土耳其分销 + DMO 公采通道 → 分销 20% 首选 TR（可把 Saga 列为其网络硬件品牌）**：STC-228GP / STC-2224GP / STC-4424GCPM（配其 NVR / 摄像机项目）+ STI-288DGGPM（市政 / 地铁杆位 —— 地铁站只谈站厅商业场景）；加厚一次',
           '收件人 info@ 点名「satın alma / ürün müdürü」；表内无跟进 → 首信即一页纸 + DMO 适配说明（CE / RoHS 文件齐）；发信窗口 Thu 10–12 TRT；下轮补项：法律形式 / MERSİS'],
    notes='分销 20% 首选 TR；加厚一次；部分坐实。')
put('SB-566', key='tr', batch=B, name='PCG Bilgisayar Sistemleri Pazarlama San. ve Tic. Ltd. Şti.（pcgbilgisayar.com；İstanbul Kartal Soğanlık）— 1998 年起（EMIS 登记 2004-06-04）的服务器 / 工作站 / AI 算力分销商：**Gigabyte Enterprise 土耳其独家分销（2016 起）+ NVIDIA Compute Partner + E-View 自有工作站 / 服务器 + Rejitek 工业 PC 独家分销**；11–50 人', iso='TR', fetched=F,
    source='TR · 1 次检索：EMIS（Pcg Bilgisayar Sistemleri Pazarlama Sanayi Ve Ticaret Limited Sirketi；incorporated 2004-06-04；AC Moment Yapı No 4b/77 Soğanlık Yeni Mah. Baltacı Mehmetpaşa Sok. Kartal İstanbul 34880；Electronics Stores）+ 官网首页 / Markalar（1998 起；「Türkiye Resmi Gigabyte Enterprise Distribütörü」2016 起独家；NVIDIA Compute Partner；HPC / 数据中心 / 服务器方案）+ LinkedIn（1998；11–50；E-View İş İstasyonu ve Sunucu Çözümleri）+ RocketReach（5 人；1998）；MERSİS 号未取',
    url='https://www.emis.com/php/company-profile/TR/Pcg_Bilgisayar_Sistemleri_Pazarlama_San_Ve_Tic_Ltd_Sti_en_3340875.html',
    number='Ltd. Şti.（İstanbul；EMIS 在册；MERSİS 号未取）', status='Active（官网 2026-07 更新）', incorporated='1998（自述）/ 2004-06-04（EMIS 登记）', company_type='Limited Şirket（私有）',
    sic=['服务器 / 工作站 / GPU 算力 / 数据中心基础设施分销与集成（Gigabyte Enterprise 独家、NVIDIA、Rejitek 工业 PC）', '自有品牌 E-View 工作站 / 服务器'],
    address='Baltacı Mehmet Paşa Sok. No 4, Moment İstanbul B Blok D 77, Soğanlık, Kartal / İstanbul 34880', accounts='—', accounts_due='—', size_band='小型（5–50 人）',
    officers=['Nalan（姓待核）— 研究档 KP nalan@（职务未核）', '管理层姓名未取'], psc='未取', charges='', prev_names=[],
    lines=['**卖服务器 / AI 算力的分销商 = 数据中心交换机客户（优先级规则）** → **分销 20%，DC 线为主**：STH-2C24XF-HSI（$1,500，24×25G + 100G 上联 ToR）/ STH-8C48DX-HSI（$4,800）/ STH-32C-HSI（$6,000，32×100G）配 Gigabyte 服务器机柜 + STC-110XGE（管理网）；B BIG，**加厚**（DC 方案一页纸 + 三档价 + 与白牌 ToR 对比）',
           '收件人 nalan@（点名「sunucu / veri merkezi ürün müdürü」）；表内 1 次跟进无回复 → 第二次触达换主题「25G/100G ToR switches to ship with your Gigabyte racks」；发信窗口 Thu 10–12 TRT；升 A 候选（回信即 A）'],
    notes='分销 20%（DC 线 STH 为主）；B BIG；加厚；升 A 候选。')
put('SB-647', key='tr', batch=B, name='Art Telekom San. Tic. Ltd. Şti.（LinkedIn / EMIS 写 ART TELEKOM A.Ş.；arttelekom.com.tr；Ankara Çankaya Beysukent，İstanbul Kartal 办）— 1980 年起（EMIS 现主体 2002-06-26）的语音 / 视频 / 数据通信集成商（Mitel / Aastra PBX、IP 电话、视频会议、CCTV、KGYS、结构化布线、光纤、无线；公共机构客户）；**Dış Ticaret Müdürü（外贸经理）Müjde Balıkçıoğlu = 研究档 KP 本人（家族企业：GM Hasan Balıkçıoğlu、副 GM Murat Balıkçıoğlu）**；11–50 人', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 İletişim（Art Telekom San.Tic.Ltd.Şti.；Mutlukent Mah. Angora Bulvarı Fesleğen Sok. No 7, Beysukent-Ankara；+90 312 472 47 47；Genel Müdür Hasan BALIKÇIOĞLU；Genel Müdür Yardımcısı Murat BALIKÇIOĞLU；**Dış Ticaret Müdürü Müjde BALIKÇIOĞLU**；Satış ve Proje Direktörü Tarkan ERDOĞAN）+ arttelekom.com Contact（Genel Müdürlük Ankara + İstanbul Ofis Kartal Uprise Elit Residence；方案：公共广播 / 同传 / AV / 结构化布线与网络 / 卫星电视 / 无线 / 光纤 / KGYS）+ LinkedIn（ART TELEKOM A.Ş.；1980 Ankara；11–50；Müjde Balıkçıoğlu 另任 TECOM Mühendislik A.Ş. Director Distribution Channel）+ EMIS（Art Telekom A.S.；incorporated 2002-06-26；Çankaya Ankara 06800）+ RocketReach（11 人；1980；Müjde — International Trade Manager）；MERSİS 号未取',
    url='https://www.arttelekom.com.tr/iletisim/art-telekom-iletisim',
    number='Ltd. Şti.（官网）/ A.Ş.（LinkedIn / EMIS）并存 — Ankara；MERSİS 号未取', status='Active（官网在线；两地办公）', incorporated='1980（自述）/ 2002-06-26（EMIS 现主体）', company_type='Limited Şirket / Anonim Şirket（家族企业 Balıkçıoğlu；关联 TECOM Mühendislik A.Ş.）',
    sic=['语音 / 视频 / 数据通信系统集成：PBX / IP 电话（Mitel / Aastra）、视频会议、CCTV / KGYS、公共广播与紧急广播、结构化布线与网络、光纤、无线、卫星电视 —— 公共机构与企业客户'],
    address='Mutlukent Mah. Angora Bulvarı Fesleğen Sok. No 7, Beysukent / Çankaya, Ankara 06800（İstanbul 办：Balıkesir Cad. Uprise Elit Residence K 20 D 176, Kartal）', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Hasan Balıkçıoğlu — Genel Müdür（总经理）', 'Murat Balıkçıoğlu — Genel Müdür Yardımcısı（副总；2002 起）', 'Müjde Balıkçıoğlu — Dış Ticaret Müdürü（外贸 / 进口经理）= **研究档 KP mujde.balikcioglu@ 本人 = 进口决策人**', 'Tarkan Erdoğan — Satış ve Proje Direktörü'], psc='Balıkçıoğlu 家族', charges='', prev_names=[],
    lines=['**收件人就是外贸经理（管进口）+ 家族企业 + 公共项目集成 → 集成商 25%（兼分销 20%，TECOM 渠道）**：STC-2224GP / STC-4424GCPM（IP 电话 / 会议 / CCTV 项目 PoE）+ STI-288DGGPM（KGYS 杆位）+ STC-424XGGPM-280W（汇聚）；B BIG，**加厚**（进口流程 + 三档价 + 项目规格页）',
           '表内 1 次跟进无回复 → 第二次触达换主题「direct import of managed PoE switches for your public-sector projects — EXW/DAP both quoted」；发信窗口 Thu 10–12 TRT；升 A 候选（回信即 A）'],
    notes='集成商 25% + 分销 20%；KP = 外贸经理本人；B BIG；加厚；升 A 候选。')
put('SB-649', key='tr', batch=B, name='Başarı Mühendislik Otomasyon Elektrik Ltd. Şti.（basarimuhendislik.com；İstanbul Ataşehir）— 2007-10-09 成立的能源自动化 / SCADA-RTU / 电信系统 / 工业网络 / LoRaWAN IoT 交钥匙工程商（变电站、电厂、OSB、机场、炼油厂、**轨道交通（守界）**、医院；28–35 人；$4–5M；联合创始人 Murat Tunçer）', iso='TR', fetched=F,
    source='TR · 1 次检索：EMIS（Basari Muhendislik Otomasyon Elektrik Ltd. Sti.；incorporated 2007-10-09；Herford Plaza No 128-2 İnönü Mah. Kayışdağı Cad. Ataşehir İstanbul 34755）+ 官网 İletişim / 首页（İnönü Mh. Kayışdağı Cd. Kandiş İş Merkezi No 128 Kat 1 Ataşehir；satis@；+90 216 469 7450；2007 起；SCADA & RTU、能源自动化、电信系统、工业 IoT、工业网络）+ LinkedIn（2007；11–50；Ataşehir）+ ContactOut（28 人；$4.2M）+ RocketReach（35 人；$5M；Co-Founder Murat Tunçer；LoRaWAN IoT）+ Kariyer（电厂、变电站、轨道系统、OSB、机场）；MERSİS 号未取',
    url='https://www.emis.com/php/company-profile/TR/Basari_Muhendislik_Otomasyon_Elektrik_Ltd_Sti_en_3949953.html',
    number='Ltd. Şti.（İstanbul；EMIS 在册；MERSİS 号未取）', status='Active（官网 2025 更新）', incorporated='2007-10-09', company_type='Limited Şirket（私有；联合创始人 Murat Tunçer）',
    sic=['能源自动化 / SCADA-RTU / 电能质量与抄表 / 电信系统 / 工业网络 / LoRaWAN IoT 交钥匙工程（输配电、电厂、OSB、机场、炼油、轨交、医院）'],
    address='İnönü Mah. Kayışdağı Cad. No 128 Kat 1 D 2（Kandiş / Herford Plaza）, 34755 Ataşehir / İstanbul', accounts='—', accounts_due='—', size_band='小型（28–35 人；$4–5M）',
    officers=['Murat Tunçer — Co-Founder（RocketReach）', 'Hakan Öztürk — 研究档 KP hakan.ozturk@（职务未核；LinkedIn 同名 ERC Sistem 者为他人，不采）'], psc='未取', charges='', prev_names=[],
    lines=['**工业自动化工程商 → 集成商 25%**：STI-288DGGPM / STI-488DGGPM（变电站 / 电厂 SCADA 环网，导轨宽温）+ STI-0240GE；**轨道交通项目不碰（守界：无 EN 50155）**，信里只谈能源 / OSB / 机场场景；一页纸 + 工业线规格',
           '收件人 Hakan Öztürk 主送 + satis@ 抄；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 10–12 TRT；不加厚'],
    notes='集成商 25%；轨交守界；一页纸。')
put('SB-650', key='tr', batch=B, name='BEAST GÜVENLİK TEKNOLOJİLERİ A.Ş.（BİGİS 名录写 BEAST GÜVENLİK TEKNOLOJİ SAN. DIŞ TİCARET A.Ş.；beastteknoloji.com；İstanbul Kadıköy Göztepe）— 2021 年成立的电子安防分销商（Tiandy 主分销、Hikvision / Reolink / Ajax / Teknim「最佳分销商」奖；ISAF 参展；4–10 人）；**G.M. / 创始合伙人 Başak (Erdur) Hatem = 研究档 KP 本人**', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 İletişim（Beast Güvenlik Teknolojileri；Merdivenköy Mah. Günaydın Sok. No 4, Göztepe / İstanbul；+90 216 602 26 14；info@；Başak HATEM basak.hatem@ 0539 389 23 69 Dahili 104）+ RocketReach（BEAST GÜVENLİK TEKNOLOJİLERİ A.Ş.；2021；4 人；Başak Hatem — G.M. 2021 起，前 Eslife 产品经理 / ENTES 企业销售经理）+ LinkedIn 帖（BAŞAK ERDUR HATEM — Beast Güvenlik Teknolojileri A.Ş de Kurucu Ortak；Tiandy ana dağıtıcı）+ BİGİS 会员名录（BEAST GÜVENLİK TEKNOLOJİ SAN. DIŞ TİCARET A.Ş.；Başak HATEM；34SND561-34077）+ 官网 2025（BEAST & HIKVISION 会谈、Reolink 来访、ISAF 24 展台、AJAX 奖牌、TEKNİM 最佳分销商奖）；MERSİS 号未取',
    url='https://www.beastteknoloji.com/iletisim/',
    number='A.Ş.（İstanbul；BİGİS 会员号 34SND561-34077；MERSİS 号未取）', status='Active（官网 2025-10 更新）', incorporated='2021', company_type='Anonim Şirket（私有；创始合伙人 Başak Hatem）',
    sic=['电子安防设备分销（Tiandy 主分销；Hikvision / Reolink / Ajax / Teknim；摄像机 / NVR / 报警 / 门禁 / 安装耗材）面向安装商与工程商'],
    address='Merdivenköy Mah. Günaydın Sok. No 4, Göztepe / Kadıköy, İstanbul', accounts='—', accounts_due='—', size_band='微型 / 小型（4–10 人）',
    officers=['Başak (Erdur) Hatem — Genel Müdür / Kurucu Ortak（创始合伙人）= **研究档 KP basak.hatem@ 本人**'], psc='Başak Hatem（合伙人之一）', charges='', prev_names=[],
    lines=['**年轻安防分销商 + 老板本人收件 + 已代理多个外国品牌 → 分销 20%**：STC-028GP / STC-228GP / STC-2216GP / STC-2224GP（配 Tiandy / Hikvision 摄像机套件）；也可谈 Beast 标贴牌（OEM 30%）；加厚一次',
           '表内 1 次跟进无回复 → 第二次触达换主题「a PoE switch line for your Tiandy kits — MOQ 1, 15-day quote」；发信窗口 Thu 10–12 TRT；升 A 候选（回信即 A）'],
    notes='分销 20%（可谈贴标）；KP = GM / 创始合伙人本人；加厚一次；升 A 候选。')

print('b101 US 6 + TR 6 written')
