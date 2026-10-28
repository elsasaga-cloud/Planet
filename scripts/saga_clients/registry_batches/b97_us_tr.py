#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 97 批 · US 6 户 + TR 6 户（T29-U90 同轮续做，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。
选户 = 规程 §3「第 97 批」名单（B 档未建底数，按「自有 logo」+「打开次数」排序）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 97

# ---------------- US 6（其中 1 户国别更正 → 印度）----------------
put('SB-1048', key='us', batch=B, name='Kar-Gor, Inc.（kargor.com → 现以 CT Northwest 名义经营；Salem, Oregon）— 智能交通（ITS）产品与服务商', iso='US', fetched=F,
    source='US · 1 次检索：Bloomberg（KAR-Gor Inc；3540 Brooks Avenue NE Building 2, Salem OR 97301；foundingDate 1986-02-14）+ ZoomInfo（Kar-Gor；1986；11–50 人；<$5M；Christy Fagan = Manager, Operations）+ ct-northwest.com/about（CT Northwest：交通行业先进产品与服务，「building on more than 20 years of experience as Kar-Gor Inc」；团队 Christy Fagan / Tim Hoferer；PO Box 54 Tillamook OR；info@kargor.com）+ Concrete Bid Network（Kimberly Weltz 联系人）',
    url='https://www.ct-northwest.com/about/',
    number='Oregon 登记号未取（OR SoS 可查，本次 1 次即停）', status='Active（kargor.com 重定向至 CT Northwest）', incorporated='1986-02-14', company_type='Inc.（俄勒冈；私有）',
    sic=['智能交通系统（ITS）/ 交通信号机柜配套产品与服务（Kar-Gor → CT Northwest 品牌）'],
    address='3540 Brooks Avenue NE, Building 2, Salem, OR 97301（通信 PO Box 54, Tillamook OR 97141）', accounts='—', accounts_due='—', size_band='小型（11–50 人；<$5M）',
    officers=['Christy Fagan — Manager, Operations（ZoomInfo / 官网团队页）', 'Tim Hoferer — 团队（职务未取）', 'Kimberly Weltz — 投标联系人'], psc='未取', charges='', prev_names=['Kar-Gor Inc.（现用 CT Northwest 品牌）'],
    lines=['研究档「kargor.com 快照为重定向页」解谜：公司改以 CT Northwest 品牌做交通 ITS → 交通机柜用工业交换机要 NEMA TS2 / 温宽 → **Saga 工业线证书不对口（守界边缘）→ 一页纸即止、不加厚**',
           '表内「工业 FS」= 他们问过工业光纤交换机；若发只写 STI 系列 + 明确不做 TS2 认证，收件人 info@kargor.com 点名 Operations Manager'],
    notes='低概率；下轮不追。')
put('SB-853', key='us', batch=B, name='JM Fiber Optics, Inc.（jmfiberoptics.com；Chino, CA）— 光纤 / 无线网络工程与集成商（MBE / GSA）', iso='US', fetched=F,
    source='US · 1 次检索：BBB（JM Fiber Optics, Inc.；Corporation；本地开业 1999-12-14；管理人 Kenneth G Rivera, President；BBB 档案 2014-06-03）+ Bloomberg（foundingDate 1993-02-16；13941 Ramona Ave Suite A, Chino CA 91710）+ GovCB / SAM 镜像（联系人 KENNETH G RIVERA, PRESIDENT/CEO）+ LinkedIn（1992 成立；11–50 人；Ken R. = President & CEO；2026 为 Transitvue 做公交站 LED 显示试点）+ RocketReach（4 人；$1M）+ Blue Book（5–9 人；MWBE）+ AZ UTRACS（亚利桑那交通局供应商；主要联系人 Kenneth Rivera）',
    url='https://www.bbb.org/us/ca/chino/profile/low-voltage-contractors/jm-fiber-optics-inc-1126-89069206',
    number='CA 公司（SoS 号未取；SAM 在册）', status='Active', incorporated='1992（业务）/ 1993-02-16（公司）', company_type='Corporation（加州；少数族裔企业 MBE / SBA 8(a)）',
    sic=['238210 光纤 / 无线通信网络工程、安装、测试、认证培训（商业 + 政府 / 交通）'],
    address='13941 Ramona Ave, Suite A, Chino, CA 91710', accounts='—', accounts_due='—', size_band='微型（4–9 人；$1–3M）',
    officers=['Kenneth G (Ken) Rivera — President / CEO（老板；邮箱未公开）'], psc='Kenneth G Rivera（推定）', charges='', prev_names=[],
    lines=['微型政府 / 交通类集成商（GSA、交通局供应商）→ 会问 TAA / NDAA（禁词）→ **只谈商业项目一条线，小项目集成商 25%**，一页纸写老板 Ken Rivera（官网表单 / info@）',
           '发信窗口 Wed 08–10 PT；不加厚'],
    notes='')
put('SB-278', key='us', batch=B, name='Lanmus Networks（lanmus.com；Katy, TX 虚拟办公地址）— 自有品牌交换机壳公司（中东 / 非洲渠道，MAC OUI 2024-10）= 同行', iso='US', fetched=F,
    source='US · 1 次检索：lanmus.com（6725 S Fry Rd, Ste 700 #108, Katy TX 77494 = 共享办公；+1 281 / +1 315 两个电话；「manufactured by LANMUS and distributed by SPOLLEX … throughout the UAE, GCC, Africa, Kenya, and Nepal」；LM-4804XFMGP-L3「independently developed by LANMUS」；LM-2404XMGP-IL3「Availability in UAE」）+ maclookup（Lanmus Networks Ltd 于 2024-10-14 登记 MA-M OUI B0:47:5E）；德州 SoS 未见同名实体（1 次即停）',
    url='https://lanmus.com/about-lanmus-networks/',
    number='美国实体未坐实（TX SoS 无同名；OUI 登记名「Lanmus Networks Ltd」）', status='官网在线（2026-09 更新）', incorporated='≈2024（OUI 2024-10-14）', company_type='品牌壳（美国地址为共享办公；渠道在 UAE / 非洲）',
    sic=['自有品牌管理 / 非管理 / 工业 PoE 交换机（深圳代工贴牌）面向中东 / 非洲分销'],
    address='6725 S Fry Rd, Ste 700 #108, Katy, TX 77494（虚拟地址）', accounts='—', accounts_due='—', size_band='微型',
    officers=['未取（官网无人名）'], psc='未取', charges='', prev_names=[],
    lines=['**同行**：这就是一个 2024 年新起的深圳代工贴牌交换机品牌（美国地址做门面、货卖 UAE / 非洲）→ 不发价格表、B 不动',
           '记档价值：型号命名 LM-2404XSMGP-L2 / LM-4804XFMGP-L3 与华南公模一致 → 同货源，没有我们的位置'],
    notes='不再查。')
put('SB-712', key='us', batch=B, name='Maple Systems, Inc.（maplesystems.com；Everett, WA）— 1983 年起的 HMI / PLC 制造商，2014 起员工持股', iso='US', fetched=F,
    source='US · 1 次检索：opengovwa（MAPLE SYSTEMS, INC.；WA UBI 600490742；Wa Profit Corporation；1983-05-25 注册；Active；808 134th St SW Ste 120, Everett WA 98204；Governors Daunne O’Farrell / Larry St Peter）+ BBB（1983-05-01 开业；President Larry St Peter；EVP Sarah Davis）+ theorg（President Alex Moskos；Director of Sales & GTM Diane Callahan；Director of Engineering Mena Youssef）+ ZoomInfo（CEO Larry St.Peter；VP Manufacturing Andre Zins）+ maplesystems.com/faq（1983 创始人经营 → **2014 起员工持股**）+ RocketReach（60 人；$7.4M）+ LinkedIn（11–50 人；Inc. 5000 六次）',
    url='https://opengovwa.com/corporation/600490742',
    number='Washington UBI 600490742', status='Active', incorporated='1983-05-25', company_type='WA Profit Corporation（员工持股 ESOP，2014 起）',
    sic=['334513 HMI / HMI+PLC / 工业面板 PC / IIoT 网关设计制造 + 工业网络交换机品类转售（面向 OEM / SI / 分销）'],
    address='808 134th St SW, Suite 120, Everett, WA 98204', accounts='—', accounts_due='—', size_band='小型（44–60 人；$7–10M 第三方估）',
    officers=['Alex Moskos — President（theorg）= **研究档 KP「Alex M」alexm@ 大概率本人**', 'Diane Callahan — Director of Sales & GTM Operations = **研究档 KP「Diane C」dianec@ 本人**', 'Larry St Peter — CEO / Governor（创始人一代）', 'Daunne O’Farrell — VP Finance / Governor', 'Andre Zins — VP Manufacturing'], psc='员工持股（ESOP）', charges='', prev_names=[],
    lines=['**研究档两位 KP = 总裁 + 销售总监本人**；官网已设「Industrial Network Switches」品类（外采转售）→ **工业 PoE 贴 Maple 标 = OEM 30% 正解**（STI-054GP / STI-144GP / STI-288DGGPM 配其 HMI 套装），分销 20% 为底',
           '员工持股公司决策偏稳 → 一页纸写 Alex Moskos、抄 Diane Callahan，一个问题：现有工业交换机品类的来源 / 年量？',
           '发信窗口 Wed 08–10 PT'],
    notes='OEM 首选。')
put('SB-744', key='in', batch=B, name='COMMANDO Networks Private Limited（commandonetworks.com；Navi Mumbai，印度）— 自有品牌网络硬件（深圳 / 香港 / 迪拜办公室）= 同行；美国地址为注册代理', iso='IN', fetched=F,
    source='IN · 1 次检索：zaubacorp（COMMANDO NETWORKS PRIVATE LIMITED；CIN U74999MH2015PTC261514；2015-12-30 注册；Registrar Mumbai；实收资本 Rs 100,000；董事 Vazir Ahmed Akhtar Siddiqui + Umair Ahmed Siddiqui）+ commandonetworks.com/about_us（「Indian manufacturer headquartered in Navi Mumbai」）+ /contact（印度 Office 212-213, Bldg 2(A-3), Millennium Business Park, Mahape, Navi Mumbai 400710；美国 COMMANDO Networks Inc. 1007 N Orange St Fl 4, Wilmington DE 19801 = 注册代理地址；迪拜 LLC；深圳华强北 Limited；香港 Limited）+ D&B（Key Principal Vazir Ahmed Akhtar Siddiqui）+ IndiaMART（51–100 人）',
    url='https://www.zaubacorp.com/COMMANDO-NETWORKS-PRIVATE-LIMITED-U74999MH2015PTC261514',
    number='印度 CIN U74999MH2015PTC261514（美国 Inc. 仅注册代理地址）', status='Active', incorporated='2015-12-30', company_type='Private Limited（印度；Siddiqui 家族）',
    sic=['自有品牌交换机 / 路由 / 无线 / MC / SFP / PoE 注入器（深圳采购贴牌，170+ 国商标）'],
    address='Office 212-213, Building No. 2(A-3), Millennium Business Park, MIDC, Mahape, Navi Mumbai 400710, India', accounts='—', accounts_due='—', size_band='小型（51–100 人）',
    officers=['Vazir Ahmed Akhtar Siddiqui — Director / 老板', 'Umair Ahmed Siddiqui — Director'], psc='Siddiqui 家族', charges='', prev_names=[],
    lines=['**国别更正：美国 → 印度（Navi Mumbai）**；自设深圳华强北办公室直接采购贴牌 = **同行品牌商、没有中间位置 → B 不动、不发**',
           '记档价值：威尔明顿 1007 N Orange St 是注册代理楼（见过多次），遇到即查母国'],
    notes='country_fix 印度；不再查。')
put('SB-806', key='us', batch=B, name='General Data Company, Inc.（general-data.com / datageneral.co；Cincinnati, OH）— 标签 / 条码 / 网络集成商，自有 DG 标交换机，201–500 人', iso='US', fetched=F,
    source='US · 1 次检索：general-data.com/about（总部 4354 Ferguson Drive, Cincinnati OH 45245；三处园区：标签制造 / 软件 / 服务维修）+ LinkedIn（1981；201–500 人；私有；标签制造 + 条码数据采集 + 系统集成（现场勘测 / 网络安装）+ 打印机服务）+ Label & Narrow Web 2020（1981 Pete Wenzel 车库创业；1993 三方合并至 Clermont County）+ Tracxn（法人 GENERAL DATA COMPANY INC.，2024-12-31 275 人）+ D&B（营收 $36.8M 模型值）+ RocketReach / ZoomInfo（$104M 第三方估，取范围）+ explorium（Paul Sanborn = Vice President Operations）',
    url='https://www.general-data.com/about',
    number='Ohio 公司（SoS 号未取）', status='Active', incorporated='1981（Tracxn 记法人 1999-12-31）', company_type='Inc.（私有；创始人 / 合伙人）',
    sic=['322220 标签制造 + 423430 条码 / 数据采集设备分销集成 + 网络安装（自有品牌 DG 交换机 DG-S1930K 系列 = 贴牌）'],
    address='4354 Ferguson Drive, Cincinnati, OH 45245', accounts='—', accounts_due='—', size_band='中型（231–275 人；$37–104M 第三方区间）',
    officers=['Paul Sanborn — Vice President Operations（= 研究档 KP psanborn@ 本人 = 运营 / 采购口）', 'Kathy Muczynski — CIO（ZoomInfo）', 'Pete Wenzel — 创始人（1981）'], psc='创始人 / 合伙人（未取）', charges='', prev_names=[],
    lines=['**研究档 KP = 运营副总裁本人**，且已有自有 DG 标 PoE 交换机（DG-S1930K-8GP2S-120W 等 = 华南贴牌）→ **OEM 30% 首选，B BIG**：商用 PoE 全系贴 DG 标（STC-028GP / STC-228GP / STC-2224GP），价格直接给到位',
           '一个问题：DG 标交换机现供应商交期 / 年量？发信窗口 Wed 08–10 ET'],
    notes='OEM 首选。')

# ---------------- TR 6 ----------------
put('SB-275', key='tr', batch=B, name='GelecekBT Bilgi Teknolojileri（gelecekbt.com；Perpa / İstanbul）— 2004 起的网络 / 工业通信分销，自有品牌 Telkolink + CLR Networks 独家', iso='TR', fetched=F,
    source='TR · 1 次检索：gelecekbt.com/hakkimizda（2004-10-13 伊斯坦布尔创立；Perpa Ticaret Merkezi A Blok Kat:13 No:1990 Şişli；satis@gelecekbt.com；CLR Networks 土耳其独家分销；以太网交换机 / SFP / 工业通信 / SDH-PDH / CCTV / 布线）+ perpa.com.tr 名录（CLR Networks / ONET / Telkolink / Netkablo 分销；bayi@）+ telkolink.com（「Telkolink, GelecekBT’ye aittir」= 自有品牌）+ LinkedIn（2–10 人；2004）+ haber15 名录（联系人 Yusuf Ölçer）+ perpahaber（品牌矩阵含 Advantech / 3Onedata / TG-NET / Dahua / Netgear）',
    url='https://gelecekbt.com/hakkimizda',
    number='MERSİS / 法律形式未取（Perpa 名录无 Ltd. 后缀 → 可能为 şahıs 企业）', status='Active（官网 2026 更新）', incorporated='2004-10-13', company_type='未取（şahıs / Ltd. Şti. 待核）',
    sic=['46.52 网络 / 工业通信 / CCTV / 布线分销（Perpa 商贸中心店铺 + B2B）'],
    address='Perpa Ticaret Merkezi A Blok Kat:13 No:1990, Okmeydanı, 34384 Şişli / İstanbul', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Yusuf Ölçer — 联系人 / 疑似业主（haber15 名录）', '销售公域 satis@gelecekbt.com'], psc='未取', charges='', prev_names=[],
    lines=['表内「卖 PLANET 工业件」+ 自有品牌 Telkolink + 分销 3Onedata / TG-NET（都是华南货）→ **贴标 OEM 30% 一句试探（Telkolink 标工业 / 商用 PoE）+ 分销 20% 为底**，Perpa 店铺型微商、价格敏感',
           '发信窗口 Thu 10–12 TRT；写 satis@ 点名 Yusuf Ölçer，一页纸'],
    notes='法律形式待核（一次）。')
put('SB-268', key='tr', batch=B, name='Bulutlar Bilişim（bulutlarbilisim.com；土耳其）— 1 次检索未命中（结果均为 Bulutistan / Bulut Bilişim 他司）', iso='TR', fetched=F,
    source='TR · 1 次检索：无同名命中（EMIS「Bulut Bilisim Teknolojileri Ltd. Sti.」Kartal 2010 / ICT Bulut Bilişim A.Ş. Bulutistan 2015 / Bizim Bulut 均非本户）；研究档：官网 http_error、阿里巴巴询盘「核心交换机 100G/25G」、KP Ammar Alsawadi（CEO）→ 1 次即停',
    url='https://www.emis.com/php/company-profile/TR/Bulut_Bilisim_Teknolojileri_Ltd_Sti_en_3729792.html',
    number='未坐实', status='官网 http_error（研究档）', incorporated='未取', company_type='未取',
    sic=['IT 贸易（阿里巴巴询盘型）'], address='土耳其（城市未取）', accounts='—', accounts_due='—', size_band='微型（推定）',
    officers=['Ammar Alsawadi — CEO（研究档 KP；info@ 公域）'], psc='未取', charges='', prev_names=[],
    lines=['官网失效 + 法人一次未坐实 + 询盘是 100G/25G 核心（CENTEC 线）→ **先不发；若要试只发 STH 一页纸到 info@，无回即 C**',
           '表内「质量可能一般」= Simon 早有判断，不逆'],
    notes='未坐实；下轮不追。')
put('SB-442', key='tr', batch=B, name='Optima Mühendislik A.Ş.（optima-engineering.com / optima.tc；Başkent OSB, Sincan / Ankara）— 路障 / 升降柱 / 闸机制造商，100 人', iso='TR', fetched=F,
    source='TR · 1 次检索：optima-engineering.com/en/corporate/about-optima（2000-12 Ostim Ankara 创立；foundingDate 2000-12；founder / CEO İ. Tamer Ülgen；NACE 28.99.90；路障 / 升降柱 / 破胎器 / 闸机 / 道闸 / 滑动门驱动；2014 投资激励购 9,000 m² 地块、2015 夏建成 Başkent OSB 工厂）+ EMIS（Optima Muhendislik A.S.；2000-12-05 注册；员工 100（2026））+ TİM（2000 年机械工程师 Tamer Ülgen 在 Ostim 100 m² 创业；2017 起 18,000 m² 工厂；OAİB 会员）+ D&B（OPTIMA MUHENDISLIK ANONIM SIRKETI；No:62 Malıköy Başkent OSB 19. Cad.）+ 官网新闻（安卡拉增长最快企业奖）',
    url='https://www.optima-engineering.com/en/corporate/about-optima',
    number='MERSİS 未取（Ltd. Şti. → A.Ş.）', status='Active', incorporated='2000-12-05', company_type='Anonim Şirketi（创始人 Tamer Ülgen）',
    sic=['28.99 物理安防机械（路障 / 升降柱 / 闸机 / 道闸 / 车牌识别停车系统）设计制造 + 出口中东'],
    address='Başkent Organize Sanayi Bölgesi 19. Cadde No:62, Malıköy, 06909 Sincan / Ankara', accounts='—', accounts_due='—', size_band='中型（100 人；EMIS 2026）',
    officers=['İ. Tamer Ülgen — 创始人 / CEO（机械工程师）', 'Furkan Kalkan — 研究档 KP（用户表 furkan@optima.tc；职务未取）'], psc='Tamer Ülgen（推定）', charges='', prev_names=['Optima Mühendislik Ltd. Şti.'],
    lines=['车牌识别 / 停车道闸系统里要配 PoE 交换机（外采）→ **配套一条线：工业小口数 STI-054GP / STI-144GP（户外机柜）+ 商用 STC-028GP，贴 Optima 标随系统出口 = OEM 30% 小**',
           '研究档 KP 职务未取 → 写 furkan@ 抄 optima@ 点名「satın alma / proje」；发信窗口 Thu 10–12 TRT'],
    notes='')
put('SB-592', key='tr', batch=B, name='Fotech Fiber Optik Teknolojik Hizmetler San. ve Tic. Ltd. Şti.（fotech.com.tr；Ataşehir / İstanbul）— 1989 起的系统集成 + 测试测量分销（Fluke Networks / Black Box / EXFO）', iso='TR', fetched=F,
    source='TR · 1 次检索：EMIS（Fotech Fiber Optik Teknolojik Hizmetler San. Ve Tic. Ltd. Sti.；1989-06-23 注册；员工 29（2026）；Ataşehir Bulvarı 38. Ada Ata 3/3 Plaza Kat 5 No.51-52, 34758 Ataşehir）+ fotech.com.tr/en/history（1989 「Final Elektrik」创立 → 1994 更名 Fotech 进入光纤 / 电信）+ /en/contact（info@fotech.com.tr；eticaret@；技术中心 Yedpa Ticaret Merkezi）+ LinkedIn（11–50 人）+ 官网新闻（2021-05 Fluke Networks 分销商；Black Box 土耳其授权分销；Tallysman 分销商页）',
    url='https://www.emis.com/php/company-profile/TR/Fotech_Fiber_Optik_Teknolojik_Hizmetler_San_Ve_Tic_Ltd_Sti_en_3313643.html',
    number='MERSİS 未取', status='Active', incorporated='1989-06-23', company_type='Ltd. Şti.',
    sic=['62.09 / 46.52 网络系统集成 + 数据中心 + 弱电 + 测试测量 / 同步设备独家分销（欧美日加品牌）'],
    address='Ataşehir Bulvarı 38. Ada Ata 3/3 Plaza Kat:5 No:51-52, 34758 Ataşehir / İstanbul', accounts='—', accounts_due='—', size_band='小型（29 人）',
    officers=['「ssahin」— 研究档 KP（ssahin@fotech.com.tr；全名 / 职务未取）', '管理层未取'], psc='未取', charges='', prev_names=['Final Elektrik（1989–1994）'],
    lines=['定位 = 欧美高端品牌独家分销 + 集成（Black Box 本身卖交换机）→ 对华南货兴趣低 → **集成商 25% 一页纸即止（商用 PoE 配项目），不加厚**',
           '发信窗口 Thu 10–12 TRT；写 ssahin@ 抄 info@'],
    notes='低概率。')
put('SB-676', key='tr', batch=B, name='PC Tedarik İthalat İhracat Yazılım Ticaret Ltd. Şti.（pctedarik.com；Pendik / İstanbul）— IT / 安防批发网店，自有品牌 UNİMAX', iso='TR', fetched=F,
    source='TR · 1 次检索：pctedarik.com 页脚（PC TEDARİK İTHALAT İHRACAT YAZILIM TİCARET LTD.ŞTİ.；Çınardere Mh. Ankara Cd. No:43A 34892 Pendik；info@pctedarik.com）+ D&B（Key Principal Islam Calik；Çınardere Mah. Akseki Sok. No:1/1 Pendik）+ n11 店铺（Şirket Ünvanı ali çalık；İşletme Adı PCTEDARİK；**Tescilli Marka UNİMAX**；MERSİS 2250094824（şahıs 登记）；Vergi No 16820709238）+ Glassdoor（1–50 人）+ X（Pendik；硬盘批发起家）',
    url='https://pctedarik.com/11/KVKK',
    number='Ltd. Şti.（MERSİS 未取；n11 登记的 şahıs MERSİS 2250094824 为关联个体户 ali çalık）', status='Active（网店 2026）', incorporated='未取', company_type='Ltd. Şti.（Çalık 家族；另有 şahıs 登记）',
    sic=['46.51 / 47.91 硬盘 / 安防摄像机 / 电脑批发网店（Ruijie / TP-Link / Hikvision / Dahua）+ 自有品牌 UNİMAX'],
    address='Çınardere Mah. Ankara Cad. No:43A, 34892 Pendik / İstanbul', accounts='—', accounts_due='—', size_band='微型（1–50 人）',
    officers=['İslam Çalık — Key Principal（D&B）', 'Ali Çalık — n11 店铺登记人（şahıs）'], psc='Çalık 家族（推定）', charges='', prev_names=[],
    lines=['已有注册商标 UNİMAX（站内 oem 25 处）→ **贴标 OEM 30% 一句试探（商用 PoE 贴 UNİMAX 标）+ 分销 20% 为底**；走量网店价格敏感 → 价格直接给到位',
           '发信窗口 Thu 10–12 TRT；写 info@ 点名 İslam Çalık'],
    notes='')
put('SB-890', key='tr', batch=B, name='Technopc Teknoloji San. ve Tic. A.Ş.（technopc.com.tr；Ataşehir / İstanbul）— 土耳其本土 PC / 工业 PC / NVR 品牌（1998 Yücel Elektronik 起家）', iso='TR', fetched=F,
    source='TR · 1 次检索：technopc.com.tr/organizasyon-yapisi（**Mithat Yücel = Yönetim Kurulu Başkanı**，1970 生，1998 Yücel Elektronik 联合创始人，2005 主导创建 Technopc 品牌，分管行政 / 财务 / **产品管理**；Murat Yücel = 创始合伙人 / 销售市场执行合伙人，1974 生）+ SAHA İstanbul（TECHNOPC TEKNOLOJİ SAN. VE TİC. A.Ş.；品牌 2006 由 Yücel Electronics 创立；迷你 PC / 工业 PC / AIO）+ LinkedIn（51–200 人；1998；Ataşehir）+ D&B（Key Principal Coşkun Murat Yücel）+ Crunchbase（51–100 人）+ ETBİS（Anonim Şirket；KEP technopc@hs01.kep.tr）+ AA 2021（公共部门国产硬件方案）',
    url='https://technopc.com.tr/organizasyon-yapisi',
    number='MERSİS 未取（ETBİS 登记 A.Ş.）', status='Active', incorporated='1998（Yücel Elektronik）/ 2006（Technopc 品牌）', company_type='Anonim Şirketi（Yücel 兄弟）',
    sic=['26.20 迷你 PC / 工业 PC / 面板 PC / NVR-NAS / 加固终端自有品牌制造（本土生产商证书）'],
    address='Ataşehir / İstanbul（İstanbul Genel Müdürlüğü；详细地址未取）', accounts='—', accounts_due='—', size_band='中型（51–200 人）',
    officers=['Mithat Yücel — Yönetim Kurulu Başkanı / 产品管理（= 研究档 KP mithat.yucel@ 本人 = 拍板人）', 'Coşkun Murat Yücel — 创始合伙人 / 销售市场（研究档 KP Murat Yücel）'], psc='Yücel 兄弟', charges='', prev_names=['Yücel Elektronik（1998）'],
    lines=['**表内「工业 PoE，买的 Ewind 的」+ KP = 董事长兼管产品 → 他们已经在深圳买工业 PoE 贴 Technopc 标，只是没买我们的 → OEM 30% 首选**：工业 PoE（STI-054GP / STI-144GP / STI-288DGGPM）+ 商用 PoE 配其 NVR，对标 Ewind 报价直接给到位',
           '一个问题：现用工业 PoE 的型号 / 年量 / 交期痛点？发信窗口 Thu 10–12 TRT；**升 A 候选（回信即 A）**'],
    notes='OEM 首选；A 候选。')

print('b97_us_tr ok')
