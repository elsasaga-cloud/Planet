#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 99 批 · US 6 户 + TR 6 户（T29-U92，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。
选户 = 规程 §3「第 99 批」名单（B 档未建底数，按「自有 logo」+「打开次数」排序）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 99

# ---------------- US 6（其中 1 户国别更正 → 以色列；1 户未坐实）----------------
put('SB-777', key='us', batch=B, name='TMB（ProPlex 品牌；tmb.com / proplex.com；San Fernando, CA 总部 + Carlstadt NJ / London / Toronto / Beijing / Riga）— 演出 / 舞台技术增值分销商兼自有品牌（ProPlex GBS 交换机、ProCable 等）', iso='US', fetched=F,
    source='US · 1 次检索：tmb.com Company Profile（1983 年成立，演出制作一站式供应；办公室 Los Angeles / London / New York / Toronto / Beijing）+ LinkedIn（TMB；1984；51–200 人；HQ San Fernando CA；65 Commerce Rd Carlstadt NJ；Marupe LV）+ proplex.com Contact（527 Park Avenue, San Fernando CA 91340；21 Armstrong Way Southall UB2 4SD；Meaford Ontario；Beijing）+ LSi / PLSN 2020-05（Colin Waters = 创办人 / CEO，前巡演技术员）+ PLASA 2025-06（Colin Waters, Chief Executive；ProPlex CodeClock）+ MapQuest（TMB Production Supplies & Services；品牌 ProCable / ProPlex / ProPin / ProFibre / ProPower）',
    url='https://tmb.com/about/company-profile/',
    number='CA 实体法定名 / SoS 号未取（公开名 TMB / TMB Production Supplies & Services；1 次即停）', status='Active（2025 PLASA 活跃）', incorporated='1983', company_type='私有（创办人 Colin Waters 持有；加州）',
    sic=['演出 / 舞台 / 建筑照明技术增值分销（租赁公司、经销商、制造商）', '自有品牌：ProPlex（Ethernet / DMX 数据分发、GBS 网络交换机）、ProCable / ProPin / ProFibre / ProPower（线缆与连接器）'],
    address='527 Park Avenue, San Fernando, CA 91340（总部）；65 Commerce Road, Carlstadt, NJ 07072；21 Armstrong Way, Southall UB2 4SD（英国）；Meaford, Ontario；北京办事处；Marupe（拉脱维亚）', accounts='—', accounts_due='—', size_band='中型（51–200 人）',
    officers=['Colin Waters — Co-founder / CEO（Chief Executive）', 'Tim Obermann — European Sales Manager（2018 起）'], psc='Colin Waters（推定）', charges='', prev_names=['TMB Production Supplies & Services'],
    lines=['**自有标交换机品牌商（ProPlex GBS：5 口 PoE 导轨、6 口便携 PoE、5 口千兆 PoE）= OEM 30% 目标**，但表内已注明「北京有办事处」= 自己在中国采购 → 卖点不是价格而是「Marvell 管理型 + 工业温宽 + 3 年保修 + MOQ 1 试产」',
           '对口型号：导轨 5 口 PoE → STI-054GP（4 PoE + 1 GE）/ STI-144GP（4+1 SFP）；便携 / 机柜 → STC-028GP（8+2）；演出行业要 IGMP / RSTP 快速收敛（Art-Net / sACN 多播）→ 信里点 IGMP snooping',
           '10 次群发无回复 → 第二次触达换主题「DIN-rail PoE for touring racks」写 sales@tmb.com 点名产品经理（研究档无 KP）；发信窗口 Wed 08–10 PT；一页纸即止，不加厚（细分行业，复利有限）'],
    notes='自有标 OEM 30% 目标；北京办事处 = 已直采；一页纸。')
put('SB-253', key='us', batch=B, name='Provision-ISR（provision-isr.com / provisionisr.com；以色列 Kfar Saba 总部 + Provision-ISR USA Dallas TX + Medley FL 物流）— 以色列 CCTV 品牌商（TVT 贴牌；深圳宝安办公室）（国别更正 US → IL）', iso='IL', fetched=F,
    source='US→IL · 1 次检索：官网 Contact / Privacy（11 Atir Yeda Street, Kfar Sava 4464310, Israel；+972 9 741 7511；America = ILS Cargo, 11459 NW 122nd Street, Medley FL 33178 物流）+ Tracxn / Crunchbase（2007 年成立；Kfar Saba；51–100 / 51–200 人；AI 视频监控制造商）+ LinkedIn Provision-ISR USA（Dallas, Texas；specialties 含 switches）+ RocketReach（Provision-ISR USA；2472 Southwell Rd, Dallas TX 75229；≈$22M；11 人）+ protectfind 2024-06（摄像机由深圳 TVT 贴牌生产，软件以色列开发）',
    url='https://provision-isr.com/about-us/',
    number='以色列公司号 / 美国实体名未取（1 次即停）', status='Active（官网 2026-10 更新；40+ 国）', incorporated='2007', company_type='以色列私有公司 + 美国销售子公司（Dallas）',
    sic=['CCTV 品牌（IP / AHD 摄像机、NVR / DVR、AI 分析、自有标 PoE 交换机）面向安装商；中档市场；40+ 国分销'],
    address='11 Atir Yeda St, Kfar Saba 4442510, Israel（研发 / 市场总部）；2472 Southwell Rd, Dallas, TX 75229（USA）；Medley, FL（物流）；深圳宝安办公室（表内）', accounts='—', accounts_due='—', size_band='中型（51–200 人；≈$22M 美国口径）',
    officers=['Leonardo Severi — Technical & Presale Manager = 研究档 KP（sales@provisionisr.com）', '创办人 / 董事未取'], psc='未取', charges='', prev_names=[],
    lines=['**国别更正**：用户表归 US，实为以色列品牌（美国只是 Dallas 销售公司 + 佛州物流）→ country_fix 以色列；发信窗口按以色列 Sun–Thu 10–12 IST（或美国分部 Wed 08–10 CT）',
           '品牌商 + 深圳宝安办公室 + 摄像机由 TVT 贴牌 → 交换机大概率也从 TVT / 华南同源 → **OEM 30% 低概率**：唯一缝隙是「Marvell 管理型 L2+ PoE（STC-424XGGPM-280W）替代其现有非管理公模」+ 3 年保修；Simon 表内「可以尝试多跟进一下」→ 加厚一次但不抱期望',
           '收件人 Leonardo Severi（技术 / 售前经理 = 选型人）抄 sales@；10 次群发无回复 → 换主题「managed PoE for NVR backbones」；不提 TVT / 不提竞品'],
    notes='国别更正 IL；品牌商已直采；OEM 30% 低概率。')
put('SB-1013', key='us', batch=B, name='Business Systems Consulting（bizsyscon.com；圣路易斯郊区）— 微型 WISP / 网络分销商，自有品牌 Lysora（官方登记 1 次未命中 → 未坐实）', iso='US', fetched=F,
    source='US · 1 次检索未命中（返回 Plymouth MA 的 bizsysconsulting.com、SE 美国 BSC Solutions、Business Systems Consulting LLC 会计所三家同名他户）→ 按规程停；以下仅研究档自述：1997 年起；2–10 人；Ubiquiti / MikroTik / Cambium / PLANET 分销；在售 PLANET GS-4210-24P4C（$522）、IGS 系列；自有品牌 Lysora；联系人 Joseph Barros',
    url='',
    number='未坐实（MO SoS 未查；域名 bizsyscon.com 搜索引擎无直接命中）', status='未核', incorporated='1997（自述）', company_type='未核（推定 LLC / Inc.，密苏里）',
    sic=['WISP / 网络设备分销（Ubiquiti / MikroTik / Cambium / PLANET）', '自有品牌 Lysora'],
    address='圣路易斯郊区（研究档；门牌未核）', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Joseph Barros — 研究档 KP（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**未坐实**：同名企业太多、域名无直接命中 → 不再花检索；研究档「自有品牌 Lysora + 在售 PLANET 工业 PoE」仍成立 → **贴标试探 small（OEM 30%）**：Lysora 标 STI-288DGGPM 对标 PLANET IGS 系列（-40%）',
           '微型 2–10 人 → 单量小；一页纸写 Joseph Barros；下轮不追'],
    notes='未坐实；贴标试探 small；一页纸。')
put('SB-435', key='us', batch=B, name='Saucon Technologies, Inc.（saucontech.com / saucontds.com；Bethlehem, PA）— 客运巴士车载远程信息处理（telematics）方案商（1997；SAM 在册）', iso='US', fetched=F,
    source='US · 1 次检索：Buzzfile（Saucon Technologies, Inc.；Year Founded 1997；State of Inc Pennsylvania；Manufacturing / Importing / Exporting；≈$9.9M；42 人；CEO Bill French）+ Govcb / SAM（SAUCON TECHNOLOGIES INC；1997；Small Business / Small Disadvantaged Business）+ Cummins 2023-10（Bill French = CEO and Founder）+ ZoomInfo（$15.4M 口径；CFO William Bouffard；Owner Satish Balu 列名）+ PRNewswire 2019-01（500+ 客户、10,000+ 辆巴士，北美 + 英国）',
    url='https://www.buzzfile.com/business/Saucon-Technologies,-Inc.-484-241-2500',
    number='宾州公司（PA DOS 号未取；SAM 在册）', status='Active（2026-07 新产品发布）', incorporated='1997', company_type='Inc.（宾夕法尼亚；私有；创办人 CEO）',
    sic=['客运 / 长途巴士车载 telematics：GPS 车队、车载视频监控、电子驾驶日志、乘客 Wi-Fi、Cummins 远程诊断（硬件 + SaaS）'],
    address='Bethlehem, PA 18020（7,100 sq ft 设施）', accounts='—', accounts_due='—', size_band='小型（28–42 人；$10–15M）',
    officers=['Bill (William) French — CEO & Founder / President = 研究档 KP bfrench@ 本人', 'William (Bill) Bouffard — CFO / Managing Director', 'Satish Balu — Owner（ZoomInfo 列名，待核）'], psc='Bill French（推定）', charges='', prev_names=[],
    lines=['**研究档 KP 坐实 = 创办人 CEO 本人**（展会联系人）→ 直达拍板人',
           '但产品是**车载**（巴士上的视频 / Wi-Fi 网关）→ 需要 E-mark / 车规宽压 → Saga 无 E-mark、不做车载 → **守界边缘，一页纸即止**：只提「车场 / 调度中心侧」的商业 PoE（STC-228GP / STC-2224GP 给车库摄像与 Wi-Fi 回传），不提车上',
           '发信窗口 Wed 08–10 ET；不加厚'],
    notes='KP = 创办人 CEO；车载守界 → 一页纸。')
put('SB-527', key='us', batch=B, name='AvaLAN Wireless Systems Incorporated（AvaLAN Networks；avalan.com；Madison / Huntsville, AL）— 加油站 / EMV 工业无线与以太网方案（2021-04 起为 Dover Fueling Solutions 子公司）+ 合作商 Volume Inc.（燃油中心托管网络批发）', iso='US', fetched=F,
    source='US · 1 次检索：CB Insights（AvaLAN Networks；2004；2021-04-19 被 Dover Fueling Solutions 收购；融资 $2.03M）+ LeadIQ（Dover (NYSE: DOV) 2021-04-20 完成收购 AvaLAN Wireless Systems Incorporated）+ LinkedIn（11–50 人；127 Jetplex Circle, Madison AL 35758；2004）+ ContactOut（Matt Nelson = CEO and President 2008 起 → Sr. Director & GM (Dover Fueling Solutions) 2021 起 → MD & GM AvaLAN + Bulloch Technologies 2024-02 起）+ NIST MEP 2026-01（总部 Huntsville AL，远程办公室 AZ / CO / 加拿大）+ PRWeb 2020-05（AvaLAN 与 Volume Inc. 合作托管网络服务；Volume Inc. = 燃油中心托管网络 + 批发网络设备）',
    url='https://www.cbinsights.com/company/avalan-wireless',
    number='Alabama / 原加州公司号未取；母公司 Dover Corporation NYSE: DOV', status='Active（Dover Fueling Solutions 业务单元）', incorporated='2004（硅谷起家；2008 迁 Alabama）', company_type='Incorporated（Dover 全资子公司，2021-04 起）',
    sic=['加油站前庭 / EMV 安全工业无线与以太网（自有 AW24PTPOE 等 PoE / 无线桥接产品；FIPS 140-2）', '数字标牌 / 零售 POS 网络边缘'],
    address='127 Jetplex Circle, Madison, AL 35758 / Huntsville, AL；远程办公室 AZ / CO / 加拿大', accounts='—（并入 Dover）', accounts_due='—', size_band='小型（11–50 人；Dover 子公司）',
    officers=['Matt (Matthew S.) Nelson — Managing Director & GM（原 CEO / President，2008 起）', 'Steve Merrick — CFO（收购前）', 'Cindy Powers — Director = 研究档 KP cindy.powers@', 'John W — Product Manager, Volume Inc. = 研究档 KP sales@volumeinc.com'], psc='Dover Fueling Solutions（Dover Corporation）', charges='', prev_names=['AvaLAN Wireless Systems, Inc.（硅谷，2004）'],
    lines=['**已是 Dover（NYSE: DOV）子公司** → 采购走集团供应商准入（PCI / 质量体系文件多），自有标 AW24PTPOE 等 PoE 产品有现成代工 → **OEM 30% 低概率、周期长**；B 不升',
           '更现实的一条线 = **Volume Inc.（KP John W，Product Manager）= 燃油中心网络设备批发商 → 分销 20%**：对标其在售的 8 / 16 口 PoE 报 HRUI STC-028GP / STC-2216GP + 工业 STI-054GP（加油机内「为什么需要以太网交换机」博客 = 刚需场景）',
           '收件人：Volume Inc. sales@ 点名 John W 为主，AvaLAN Cindy Powers 抄；发信窗口 Wed 08–10 CT；一页纸'],
    notes='Dover 子公司；OEM 低概率；Volume Inc. 分销 20% 一页纸。')
put('SB-541', key='us', batch=B, name='KBC Networks（kbcnetworks.com；San Juan Capistrano / Lake Forest, CA + KBC Networks Ltd, Dartford, UK）— 加固工业传输 / 电源方案品牌商（自有标工业 PoE 交换机 2–24 口；≈$30M）', iso='US', fetched=F,
    source='US · 1 次检索：官网（KBC Networks 32409 Calle Perfecto, San Juan Capistrano CA 92675；Rugged Industrial Network Switches：managed / unmanaged / PoE / PoE+ / PoE++，2–24 口，全 SFP，IP40，-40~+75 °C，无风扇）+ ZoomInfo / Datanyze（KBC Networks Ltd；2008；51–200 / 102 人；$30.2M；CEO Jonathan Crockett）+ Crunchbase（Dartford, Kent 总部；Founder & Managing Partner Ramesh Koya；CCO Luis Angulo）+ MapQuest / ProcessRegister（旧址 25691 Atlantic Ocean Dr Ste B3, Lake Forest CA；Jon Epperson 销售经理）+ LinkedIn David Schulman（VP Business Development 2010-09 起）+ Security Sales 旧闻（Lake Forest 时期发布 ESUL8 / PoE 工业交换机）',
    url='https://www.kbcnetworks.com/products/column-1/network-switches',
    number='CA 实体 / 英国 KBC Networks Ltd 的 CH 号未取（1 次即停）', status='Active（官网 2026-10 更新）', incorporated='2008（美国口径）/ 2010（英国口径）', company_type='私有品牌商（美英双总部）',
    sic=['加固工业网络交换机（自有标，2–24 口 PoE / SFP，IP40）、无线以太网、ThruLink 硬件 VPN、eCopper 同轴 / UTP IP 传输、太阳能 / UPS 电源（安防、ITS、工业控制）'],
    address='32409 Calle Perfecto, San Juan Capistrano, CA 92675（美国）；Dartford, Kent（英国 KBC Networks Ltd）；旧址 Lake Forest CA', accounts='—', accounts_due='—', size_band='中型（51–200 人；≈$30M）',
    officers=['Jonathan Crockett — CEO', 'Ramesh Koya — Founder & Managing Partner', 'Luis Angulo — CCO', 'David Schulman — VP Business Development（2010 起）= 研究档 KP（info@）', 'Steve Kuntz — President（研究档 KP skuntz@）', 'Craig Kennedy — 研究档 KP'], psc='Ramesh Koya（推定）', charges='', prev_names=[],
    lines=['**定性：品牌商而非同行** —— KBC 卖给安防 / ITS 集成商的是贴 KBC 标的加固交换机（规格 2–24 口 PoE / 全 SFP / IP40 / -40~75 °C = 华南工业公模同款）→ 他们是 **OEM 30% 目标（B BIG）**，Simon 表内「优质公司」一致',
           '对口型号：STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM（Marvell 管理型工业 PoE）；卖点 = Marvell L2+ + 3 年保修 + MOQ 1 + 已有 ITS 客户也不要 TS2（不提）',
           '收件人：Steve Kuntz（President）主送、David Schulman（VP BD）抄；美英双总部 → 英国 Dartford 也可 Thu 12–14 GMT 再发一次；**升 A 候选**（回信即 A）',
           '风险：已有稳定亚洲代工 → 首信只谈「第二供应商 / 管理型升级」，不谈替换'],
    notes='B BIG；OEM 30% 目标；升 A 候选。')


# ---------------- TR 6（其中 1 户 ISAF 联系人无公司 → 未坐实）----------------
put('SB-1010', key='tr', batch=B, name='Bayiden Bilgi Teknolojileri ve E-Ticaret（bayiden.com.tr「Teknolojinin Bayisi」；Kayseri）— 微型电子 / 安防 B2B 电商平台（背后 12 Volt Elektronik 技术实验室）', iso='TR', fetched=F,
    source='TR · 1 次检索：bayiden.com.tr 首页 / Hakkımızda（Gevhernesibe Mah. Anıt Cad. No 5, Kocasinan / Kayseri 38280；0850 441 1 352；info@bayiden.com.tr；「Arkamızda 12 Volt Elektronik’in teknik laboratuvar gücü」）+ bayiden.tr 预告页（「Bayiden Bilgi Teknolojileri ve E-Ticaret’in bir iştiraki」；Merkez Kayseri）；ETBİS 命中的 BAYDEN TEKNOLOJİ SAN. VE TİC. LTD. ŞTİ.（İstanbul Başakşehir）为同名他户，不采',
    url='https://www.bayiden.com.tr/ic/hakkimizda',
    number='MERSİS / 法律后缀未取（公开名 Bayiden Bilgi Teknolojileri ve E-Ticaret；1 次即停）', status='Active（站点在线，2026）', incorporated='未取（站点新；12 Volt Elektronik 为母体）', company_type='推定 Ltd. Şti.（Kayseri）',
    sic=['电子元件 / 安防摄像机 / 网络配件 B2B-B2C 电商（Kayseri）'],
    address='Gevhernesibe Mah. Anıt Caddesi No 5, Kocasinan / Kayseri 38280', accounts='—', accounts_due='—', size_band='微型（电商平台；人数未取）',
    officers=['未取（研究档无 KP）'], psc='12 Volt Elektronik（推定母体）', charges='', prev_names=[],
    lines=['**微型 Kayseri 电商平台**（内陆二线城市，非 İstanbul 渠道）→ 单量小、无复利 → **一页纸即止**：HRUI STC-028GP $28 / STC-228GP $33 对标其在售 PoE 交换机价位；收件 info@',
           '发信窗口 Thu 10–12 TRT；不加厚、下轮不追'],
    notes='微型电商；一页纸。')
put('SB-1051', key='tr', batch=B, name='KLEMSAN Elektrik Elektronik Sanayi ve Ticaret A.Ş.（klemsan.com.tr；İzmir Kemalpaşa）— 1974 年成立的接线端子 / 电气连接件制造商（201–500 人；100% 本土资本；IoT / 电子产品线；表内「从 VOLKTEK 买工业交换机」）', iso='TR', fetched=F,
    source='TR · 1 次检索：EMIS（Klemsan Elektrik Elektronik A.S.；成立 1974-07-20；Kızılüzüm Mah. Kemalpaşa Kızılüzüm Cad. No 15, 35730 Kemalpaşa / İzmir）+ Bloomberg（0996344D:TI；1974；noncurrent-carrying wiring devices）+ LinkedIn（201–500 人；1974；Özel Şirket）+ ENOSAD / SASAD 会员页（KLEMSAN Elektrik Elektronik San. ve Tic. A.Ş.；Yetkili İlke Kider）+ 2024-09 50 周年报道（Yönetim Kurulu Başkanı Kadir Ferahlı；450 人晚宴）+ 官网 History（1974 年 100% 国内资本创立；Pınarbaşı 第二工厂）+ D&B（Key Principal Dilek Geçer）',
    url='https://www.emis.com/php/company-profile/TR/Klemsan_Elektrik_Elektronik_AS_en_3358804.html',
    number='A.Ş.（İzmir 商会；MERSİS 号未取）', status='Active（2024 50 周年；2026 官网更新）', incorporated='1974-07-20', company_type='Anonim Şirket（私有；100% 本土资本）',
    sic=['接线端子（klemens）、线槽、电子产品（电源 / 继电器）、标识、IoT、连接器、工具 —— 自产 + 出口'],
    address='Kızılüzüm Mah. Kemalpaşa Kızılüzüm Cad. No 15, 35730 Kemalpaşa / İzmir（总部工厂）；İzmir Pınarbaşı 第二工厂', accounts='—', accounts_due='—', size_band='大型（201–500 人；SASAD 国防工业协会会员）',
    officers=['Kadir Ferahlı — Yönetim Kurulu Başkanı（董事长）', 'A. Savaş Yalçın — Kemalpaşa 工厂总经理（EMO 刊物）', 'Dilek Geçer — Key Principal（D&B）', 'İlke Kider — ENOSAD 联络人'], psc='Ferahlı 家族（推定）', charges='', prev_names=[],
    lines=['**第 99 批 TR 最大户**：50 年老牌电气连接件制造商，自有 IoT / 电子产品线，表内「从 VOLKTEK（台湾工业交换机 ODM）买工业交换机」= **现成的 OEM 30% 需求（Klemsan 标导轨工业交换机）→ OEM 30% 首选，B BIG，升 A 候选**',
           '对口：STI-054GP / STI-144GP / STI-288DGGPM（导轨、宽温、Marvell 管理型）对标 VOLKTEK 同规格 → 价格差 + 3 年保修 + MOQ 1 是切口；不提 VOLKTEK 名字',
           '收件人：研究档无 KP → 写 IoT / 电子产品线产品经理（technicalsupport@klemsan.com.tr 为官网唯一公开邮箱，可作起点）；发信窗口 Thu 10–12 TRT；**加厚**（规格 + 对比价一页）'],
    notes='OEM 30% 首选；B BIG；升 A 候选；加厚。')
put('SB-1056', key='tr', batch=B, name='Mikrodev Bilişim Yazılım Elektronik San. ve Tic. Ltd. Şti.（mikrodev.com；İstanbul 注册，Gebze TÜBİTAK 自贸区生产；英国 / 南非分支）— 本土 PLC / RTU / 网关 / 工业路由器制造商（自有品牌 MIKRODEV，2011 注册商标）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网（2006 年 İstanbul 成立，2011 起商业化生产；PLC / RTU / 网关 / HMI / SCADA；「headquarters in UK, manufacturing in Turkey, branch in South Africa」）+ Kariyer.net（Mikrodev Bilişim Yazılım Elektronik San. ve Tic. Ltd. Şti.；2011 起在 Gebze 高等技术大学校园生产；首家本土 RTU 制造商）+ IoT Tech Expo（20 工程师 + 16 技术员；TÜBİTAK 自贸区；163 型号；土耳其 14 家经销商 + 海外 3 家）+ turkishexporter（2011 注册 MİKRODEV 商标）+ ContactOut / Apollo（Habil Sekibağ = Managing Director；Erdem Öztürk = Deputy MD；Kocaeli；16 人口径）+ EtherCAT 会员页',
    url='https://www.mikrodev.com/about/',
    number='Ltd. Şti.（İstanbul / Kocaeli；MERSİS 号未取）', status='Active（官网 2025-09 更新）', incorporated='2006', company_type='Limited Şirket（私有；UK 分支 Mikrodev Ltd 自称总部）',
    sic=['工业自动化硬件：PLC、RTU、协议转换器、网关、工业路由器（2G/LTE/Wi-Fi）、HMI、SCADA 软件 —— 自研自产（TÜBİTAK 支持）'],
    address='TÜBİTAK MAM Teknoloji Serbest Bölgesi, Gebze / Kocaeli（生产）；İstanbul（注册）；英国 / 南非分支', accounts='—', accounts_due='—', size_band='小型（16–36 人）',
    officers=['Habil Sekibağ — Managing Director（创办人）', 'Erdem Öztürk — Deputy Managing Director'], psc='Habil Sekibağ（推定）', charges='', prev_names=[],
    lines=['**准同行（工业路由器 / 网关自产）但不做交换机** → 与 comtime（SB-833）同型：**贴标 small（OEM 30%）**：MIKRODEV 标导轨工业交换机（STI-054GP / STI-144GP）补齐其 PLC / RTU 柜内组网，走其土耳其 14 家经销商',
           '收件人 Habil Sekibağ（MD 本人）；发信窗口 Thu 10–12 TRT；一页纸即止；英国 / 南非分支可作第二落点（不另发）'],
    notes='准同行；贴标 small；一页纸。')
put('SB-737', key='tr', batch=B, name='Uğur İmre（ISAF 展会联系人；无公司名 / 无域名）— 未坐实', iso='TR', fetched=F,
    source='TR · 1 次检索「Uğur İmre güvenlik kamera network distribütör」未命中任何同名企业或个人主页（仅返回 İzmir / İstanbul 安防经销商泛结果）→ 按规程停；研究档：ISAF 展会名录联系人，仅有姓名 + 个人邮箱 + 历史群发记录',
    url='',
    number='未坐实（无公司主体可核）', status='未核', incorporated='未取', company_type='未取（疑个人 / 微型经销）',
    sic=['安防 / 网络经销（ISAF 展会观众名录推定）'],
    address='未取', accounts='—', accounts_due='—', size_band='未取（疑微型）',
    officers=['Uğur İmre — 本人（ISAF 名录）'], psc='未取', charges='', prev_names=[],
    lines=['**未坐实且无公司主体** → 不再花检索；保留 B 不降（有打开记录）；下一次群发顺带一封 HRUI STC-028GP / STC-228GP 价目即可，**不单独写信、不加厚**'],
    notes='未坐实；仅群发带过。')
put('SB-427', key='tr', batch=B, name='Longline Bilişim Teknolojileri Ltd. Şti.（longline.com.tr / longlinenetwork.com；İstanbul Bayrampaşa「Longline Plaza」）— 自有品牌 Longline（SFP 光模块 / 内存 / SSD / 网卡 / 光纤跳线 / 媒体转换器）+ 网络 / 服务器配件分销（800+ 经销伙伴；罗马尼亚 / 中国 / 迪拜 / 美国办事处）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 Hakkımızda / İletişim（Longline Bilişim Teknolojileri Ltd Şti；Kartaltepe Mah. Hakan Sok. Longline Plaza No 18, 34040 Bayrampaşa / İstanbul；info@longline.com.tr；2020-10-26 迁入自有大楼，与集团公司同楼）+ LinkedIn（11–50 人；2000 年成立）+ Crunchbase（Legal Name Longline Bilişim Teknolojileri Ltd. Şti.；Longline SFP Transceiver）+ makinaturkiye（Limited Şirketi；2000；注册资本 50,000,001–500,000,000 TL 档；合作伙伴 Romania / China / Dubai / USA）+ ZoomInfo（22 人）+ longlinenetwork.com İletişim（同址；0212 321 75 14）',
    url='https://longline.com.tr/en/products/',
    number='Ltd. Şti.（İstanbul；MERSİS 号未取）', status='Active（官网 2025 更新）', incorporated='2000', company_type='Limited Şirket（私有集团；自有大楼）',
    sic=['自有品牌 Longline：SFP / 光模块、内存、SSD、网卡、媒体转换器、光纤跳线（自称生产 = 贴标 / 组装）', '网络 / 服务器配件分销（800+ 土耳其经销伙伴；电信 / 公共部门客户）'],
    address='Kartaltepe Mah. Hakan Sok. Longline Plaza No 18, 34040 Bayrampaşa / İstanbul；旧址 Yeniköy Park Sok. No 29', accounts='—', accounts_due='—', size_band='小型（11–50 人；注册资本 ≥50M TL）',
    officers=['未取（研究档无 KP；info@）'], psc='未取', charges='', prev_names=[],
    lines=['**自有品牌 + 800 经销伙伴 + 中国办事处** → 已在华直采光模块 / 配件；交换机 329 页在售（研究档）但未见 Longline 标交换机 → **贴标 OEM 30% 目标（Longline 标 L2+ 管理型 / PoE 交换机补齐产品线）**，B BIG，升 A 候选（回信即 A）',
           '对口：STC-228GP / STC-2224GP（PoE）+ STI-0240GE / STH-2C24XF-HSI（电信 / 公共部门投标用 Marvell L2+/L3）；卖点 = 与其 SFP 自有标配套 + 3 年保修；不提其中国办事处',
           '收件人 info@longline.com.tr 点名「ürün müdürü / purchasing」；发信窗口 Thu 10–12 TRT；**加厚**（一页规格 + 贴标流程）'],
    notes='自有标 OEM 30% 目标；B BIG；升 A 候选；加厚。')
put('SB-465', key='tr', batch=B, name='Koza Güvenlik Elektronik Sistemleri San. Tic. Ltd. Şti.（kozaguvenlik.com.tr；İstanbul Perpa A Blok + Koza Plaza Okmeydanı）— Teletek（保加利亚）报警 / 消防、Kodicom、Dahua 分销商 + 自有注册品牌（Greentech Güvenlik 集团成员）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 İletişim / Hakkımızda（Koza Güvenlik Elektronik Sistemleri San. Tic. Ltd. Şti.；Perpa Ticaret Merkezi A Blok No 808-810-940 Şişli；Koza Plaza Arel Aralığı No 8 Okmeydanı；2005 年成立；「kendi tescilli markaları + distribütörlük」）+ kobitek 会员页（2005）+ LinkedIn（11–50 人；2005）+ Teletek Electronics 官方 Distributors 页（KOZA GÜVENLİK … LTD. ŞTİ. = 土耳其分销商）+ greentechguvenlik.com.tr Grup Şirketlerimiz（Koza = 集团公司；2010 起全国经销网）+ ISAF Exclusive 2019（Kodicom IP / HD 摄像机、Teletek 报警 / 消防）+ 官网页题「Teletek Electronics Distribütörü & Dahua Türkiye Dağıtıcısı」',
    url='https://www.kozaguvenlik.com.tr/hakkimizda',
    number='Ltd. Şti.（İstanbul；MERSİS 号未取）', status='Active（官网 © 2005–2025；Teletek 2026-03 分销商名单在列）', incorporated='2005', company_type='Limited Şirket（Greentech Güvenlik 集团成员）',
    sic=['电子安防分销：Teletek 报警 / 消防（独家）、Kodicom IP 摄像机、Dahua 二级分销、智能家居；自有注册品牌（摄像机 / 配件）；全国经销网'],
    address='Halil Rıfat Paşa Mah. Yüzer Havuz Sok. Perpa Ticaret Merkezi A Blok Kat 8 No 808-810-940, 34384 Şişli / İstanbul；Koza Plaza, Arel Aralığı No 8, Okmeydanı', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['未取（研究档无 KP；info@）'], psc='Greentech Güvenlik 集团（推定）', charges='', prev_names=[],
    lines=['**Perpa 安防分销商 + 自有注册品牌 + 全国经销网 → 分销 20% 为主、贴标 small 为辅**：Teletek / Kodicom 系统配套的 PoE 交换机（HRUI STC-028GP $28 / STC-228GP $33 / STC-2216GP）',
           '收件人 info@kozaguvenlik.com.tr 点名「satın alma」；发信窗口 Thu 10–12 TRT；一页纸即止'],
    notes='分销 20% + 贴标 small；一页纸。')

print('b99 US 6 + TR 6 written')
