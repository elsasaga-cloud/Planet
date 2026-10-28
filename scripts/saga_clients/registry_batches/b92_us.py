#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 92 批 · US 6 户（T29-U88，2026-10-28）：web_search depth 1 各一次。SB-303 实为加拿大（安省 Markham）→ 入 us 文件但 iso=CA，并在 batch92_kp.py 做 country_fix。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 92
put('SB-108', key='us', batch=B, name='GW Security（gwsecurityusa.com；South El Monte, CA）', iso='US', fetched=F,
    source='US · 1 次检索：BBB（LA & Silicon Valley）档案 —— 1230 Santa Anita Ave Ste A, South El Monte CA 91733；Business Started 2016-12-08；BBB File 2018-07-18；未认证；有消费者投诉（2022 发货拖延）+ Reddit r/SecurityCamera 技术支持差评（2024-07）。加州 SoS 页 JS 不可取，法定名未核',
    url='https://www.bbb.org/us/ca/south-el-monte/profile/security-equipment/gw-security-1216-892747',
    number='CA SoS 实体号未取（bizfile JS）', status='Active（BBB 档在用、官网在售）', incorporated='2016-12-08（BBB Business Started）', company_type='推定 Corporation / LLC（加州）',
    sic=['安防摄像 / NVR 自有品牌零售 + 批发（Amazon + 官网直销；4K IP 相机套装）'],
    address='1230 Santa Anita Ave Ste A, South El Monte, CA 91733-3861（洛杉矶东）', accounts='—', accounts_due='—', size_band='小型（估 5–20 人）',
    officers=['高管 / 股东姓名未取（BBB 不列；加州 SoS 需 JS）'], psc='', charges='BBB 消费者投诉（发货 / 售后）；Reddit 差评 —— 非法律负债，仅说明售后薄弱', prev_names=[],
    lines=['**典型「华人在洛杉矶做自有品牌安防套装」卖家（2016 起，Amazon + 官网）→ 研究档 out 49 封 + 打开 1 次 = 读过不回** → 下一步不是再群发，而是 **OEM 30% 一页：8/16 口 PoE 贴 GW 标配他们的 NVR 套装**，样机付费 1 台',
           '售后口碑差 = 他们缺技术支持 → 可以把「3 年保修 + 英文固件 + 远程配置支持」写成卖点（STI 3 年 / STC 1 年如实写）',
           '法定名 / 高管未核 → 信抬头写 Purchasing；若回信即补 SoS 查档'],
    notes='研究档记「洪瑞 商业 PoE」= 现货源为洪瑞同类 → 报价对标 HRUI 档（STC-028GP $28 / STC-228GP $33）。')
put('SB-303', key='us', batch=B, name='WatchNET Inc.（watchnetinc.com；Markham, Ontario —— 实为加拿大）', iso='CA', fetched=F,
    source='US(→CA) · 1 次检索：LinkedIn 公司页（2000 成立；11–50；总部 Markham ON；产品含 Network Switches）+ ZoomInfo / datanyze / RocketReach（351 Ferrier St Unit 5, Markham ON L3R 5Z2；33–50 人；第三方营收 $10.9–13.6M 仅作区间）+ contactout / signalhire 员工名录（Harish Babu Vettukuzhiyil VP Sales & Marketing；Karthikeyan R 采购物流经理；Milly Prince Executive Director；Roman Dabrowski VP；Matthew Durkee Director Sales USA）',
    url='https://www.linkedin.com/company/watchnet-inc-',
    number='Ontario 公司号未取（Ontario Business Registry 需登录）', status='Active（LinkedIn 2026 更新、Intersec 参展）', incorporated='2000', company_type='Inc.（安大略 / 联邦公司，待核）',
    sic=['视频监控 / 门禁 / IoT 设备自有品牌供应商（相机、录像机、网络交换机、无线 IoT）；北美 + 中东（迪拜号）'],
    address='351 Ferrier St Unit 5, Markham, Ontario L3R 5Z2, Canada', accounts='—', accounts_due='—', size_band='中小型（33–50 人；第三方营收区间 $10–14M）',
    officers=['Milly Prince — Executive Director（datanyze）', 'Roman Dabrowski — Vice President', 'Harish Babu Vettukuzhiyil — VP Sales & Marketing（2022–；研究档 KP harish@）', 'Karthikeyan R — Procurement & Logistics Manager（= 采购口）', 'Matthew Durkee — Director Sales USA', 'Joe Saju — Financial Controller'], psc='', charges='', prev_names=[],
    lines=['**国别更正：WatchNET 总部在加拿大安省 Markham，不是美国** → 研究档加 country_fix 加拿大（证书写 ISED/FCC + CE 皆可；发信窗口按美东 Wed 08–10）',
           '**自有品牌含「Network Switches」= 现成 OEM 品牌商（目标序列第一位）**：37 封群发打开 1 次无回 → 换对象：**采购物流经理 Karthikeyan R**（名字已知、邮箱格式待推 first@watchnetinc.com）+ 抄 Harish；内容只给 OEM 30% 两款（8 口 PoE $xx / 24 口 PoE+2SFP $xx，贴 WatchNET 标）',
           '33–50 人 + 中东分部（+971 号）= 有进口经验、能走 T/T 50/50；单笔 $5–20k 量级',
           '复盘：加拿大无公开年报；每季看 LinkedIn 新品（若出新交换机 = 已另有 OEM 厂）'],
    notes='研究档「Utepo」= 现有 PoE 交换机货源为优特普同类 → 价格对标 HRUI 档再让 5%。')
put('SB-347', key='us', batch=B, name='AVCOMM Technologies Inc.（avcomm.us；Houston, TX）', iso='US', fetched=F,
    source='US · 1 次检索：avcomm.us/about-us（2018 休斯顿成立；核心团队 20 年工业自动化 / 电信经验，含产品设计 / 制造）+ LinkedIn（2019；11–50）+ signalhire / RocketReach / ZoomInfo（Kang Yu CEO / COO；333 West Loop N, Houston 77024；6–50 人）+ myvisajobs H-1B 记录（Xiao Luo CEO；Kang Yu Director）+ scamadviser WHOIS（注册人 Kang Yu，13907 Round Oak Ct Houston 77059）+ RocketReach 管理层含北京产品工程师 Brenda Guan + IANA PEN 57842（AVCOMM Technologies Inc，联系人 Kang Yu）',
    url='https://www.avcomm.us/about-us',
    number='TX SoS 档号未取（需付费 SOSDirect）', status='Active（H-1B 雇主、IANA PEN、官网在售）', incorporated='2018（官网；LinkedIn 2019；inc.avcomm.us 自述 2015）', company_type='Inc.（德州公司）',
    sic=['工业以太网交换机 / IIoT / 边缘计算 自有品牌（6000 系列 PoE 工业交换机）+ 工业 IT 方案'],
    address='333 West Loop N, Houston, TX 77024（WHOIS 住址 13907 Round Oak Ct, Houston 77059）', accounts='—', accounts_due='—', size_band='小型（6–50 人；H-1B 雇主）',
    officers=['Kang Yu — CEO / COO / Director（多源；研究档 KP kang.yu@avcomm.us）= 老板 = 联系人', 'Xiao Luo — CEO（H-1B 申报口径）', 'Yukon Yu — VP Operations', 'Brenda Guan — Product Engineer（北京）'], psc='', charges='', prev_names=[],
    lines=['**这是同行：华人团队在休斯顿运营的工业交换机自有品牌（自有 6000 系列 PoE 工业机、北京产品工程师、IANA 企业号）= 自己有设计 + 中国供应链** → 我们的 STI 工业 DIN 对他们只是「又一个深圳货源」→ **降为 B 不再加厚**；仅当他们缺某口型（如 2.5G / 12 口 L2+ 管理）时可报一款',
           '若要写：写 Kang Yu（老板）一句话问「缺哪一款工业口型」，不发价格表；31 封群发无回已说明问题',
           '法定名 AVCOMM Technologies Inc.（H-1B 记录 Avcomm Technologies）；TX SoS 不再查'],
    notes='守界：不是渠道客户，是品牌同行；留 B 作「潜在 OEM 补缺」。')
put('SB-349', key='us', batch=B, name='Dualcomm Technology, Inc.（dualcomm.com；San Ramon / Danville, CA）', iso='US', fetched=F,
    source='US · 1 次检索：bizprofile.net 加州 SoS 镜像（General Corporation；档号 2772255；2005-09-12 登记；Active，SoS / FTB / Agent 均 Good Standing；CEO / Secretary / CFO / Director / 注册代理人 全为 Ziqiang He，435 Glasgow Cir, Danville CA 94526；业务「R&D of networking devices」）+ dualcomm.com/pages/about-us（创始人 John He；2005 小企业；网络 TAP 发明人；PoE-over-Coax 专利；邮寄地址 2415 San Ramon Valley Blvd #4182 San Ramon 94583）+ ZoomInfo（1–10 人，<$5M）',
    url='https://www.bizprofile.net/ca/danville/dualcomm-technology-inc',
    number='CA SoS 2772255', status='Active · Good Standing（SoS / FTB / Agent / VCFCF 四项 Good，2025-07）', incorporated='2005-09-12', company_type='General Corporation（California）',
    sic=['网络 TAP / Ethernet-over-Coax 自研自销（小众网络监测设备）；网店直销 15,000+ 客户'],
    address='注册 435 Glasgow Cir, Danville, CA 94526；邮寄 2415 San Ramon Valley Blvd #4182, San Ramon, CA 94583', accounts='—', accounts_due='—', size_band='微型（1–10 人；一人公司）',
    officers=['Ziqiang He（John He）— CEO / Secretary / CFO / Director / Registered Agent（五职一人）= 老板 = 唯一联系人'], psc='Ziqiang He（推定 100%）', charges='', prev_names=[],
    lines=['**一人工程师公司（John He 五职一肩），主业是网络 TAP 和同轴传以太网，PoE 交换机只是配套 SKU** → 研究档「自己的牌子」成立，但量极小 → **B 不加厚**；若写只写 John 一句：Dualcomm 标 8 口 PoE 的 OEM 30% 单价 + MOQ 1 箱',
           '20 年 Good Standing、无负面 = 付款安全；100% 预付小单即可',
           '邮寄地址是 UPS 信箱（#4182）= 无仓，发货走小包'],
    notes='')
put('SB-350', key='us', batch=B, name='Edge Networks LLC / Edge Networks USA（edge-networks.us；Charleston, SC）', iso='US', fetched=F,
    source='US · 1 次检索：edge-networks.us/about-us（2019 创立；President & CTO Chris Costa，1996 起做安防产品，曾领导 Fiber Options / GE Security / Radiant Communications / Comnet 工程团队；「USA based」坚固通信设备）+ LinkedIn Christopher Costa（President, Edge Networks USA 2020-07–今；此前 Communication Networks VP Eng 2011–2020）+ ZoomInfo（412 Brandam Ln Ste 103, Charleston SC 29492；1–10 人；<$5M；VP Sales Steven Carrozzo）+ Tracxn（2019；工业以太网交换机 / 媒体转换器 / 延长器 / 光纤 modem 制造商；员工 2，2026-01）。SC SoS 页 JS 未取',
    url='https://edge-networks.us/index.php/about-us',
    number='SC SoS 实体号未取', status='Active（官网 / LinkedIn 2026）', incorporated='2019（LinkedIn 2020-07 任职起算）', company_type='LLC（南卡）',
    sic=['工业以太网交换机 / 媒体转换器 / 以太网延长器 / 光纤 modem 自有品牌（安防 / ITS / 工业 / 政府网络边缘）'],
    address='412 Brandam Ln Ste 103, Charleston, SC 29492（(843) 654-9266）', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Christopher (Chris) Costa — President & CTO / 创始人（研究档 KP ccosta@）= 老板 = 技术拍板 = 联系人', 'Steven Carrozzo — VP Sales'], psc='Chris Costa（推定）', charges='', prev_names=[],
    lines=['**这就是目标序列第一位「OEM 品牌商」的标准像：前 Comnet / GE Security 工程总监自己开的 2–10 人品牌，产品线 = MC + 工业交换机 + 延长器，全部外采贴标** → **OEM 30% 全线**：STI-154GP / STI-288DGGPM 工业 DIN + MC 系列 + 8/16 口 PoE，贴 Edge Networks 标，提供英文固件 / 定制 logo / 3 年保',
           '老板是工程师（1996 起设计安防产品）→ 信写技术参数不写话术：芯片、温宽、MTBF、认证（CE/FCC/RoHS，**不写 UL / NDAA**）；30 封群发无回 = 群发内容不对路，第二封换成「spec sheet + 一款样机价」',
           '「USA based」是他的卖点 = 贴标后他不会提中国来源，正合我们「中性包装」；单笔 $3–10k，T/T 50/50',
           '复盘：每季看他官网新品型号（出现与我们口型重合的新品 = 已找到别家 OEM）'],
    notes='建议升 A 候选（证据：自有品牌 + 全外采 + 老板即 KP）；Simon 定级优先，先留 B 标「OEM 首选」。')
put('SB-362', key='us', batch=B, name='Main Tech Connect（maintechconnect.com；州未取）', iso='US', fetched=F,
    source='US · 1 次检索：ZoomInfo（Main Tech Connect；2001；11–50；<$5M；CTO Jeramie Cavanaugh；电脑 / 网络配件 + PoE 产品网店，美国本土 $50 包邮）+ maintechconnect.com 首页（在售「Industrial 8-Port Gigabit PoE+ L2+ Web-Managed Switch with 2 SFP」）。**同名陷阱：Maintech, Incorporated（新泽西 Cranford，1973，500+ 人，IT 运维服务商）非本户**',
    url='https://www.zoominfo.com/c/main-tech-connect/1275453111',
    number='未取（州未定，SoS 不可查）', status='Active（网店在售）', incorporated='2001（ZoomInfo）', company_type='推定 LLC',
    sic=['电脑 / 网络配件 + AV + PoE 产品 电商（自有型号命名）'],
    address='未取（美国本土发货）', accounts='—', accounts_due='—', size_band='小型（11–50 ZoomInfo，存疑；更像 2–10 人电商）',
    officers=['Jeramie Cavanaugh — CTO（ZoomInfo）= 推定合伙人 / 选品人'], psc='', charges='', prev_names=[],
    lines=['**网店型自有型号卖家（PoE 产品是主类目之一，首页就挂工业 8 口 PoE+ L2+ 管理型）** → 研究档「自己的 logo / 型号」成立 → **OEM 30%：按他现有型号一对一给替代报价**（工业 8 口 PoE+ 2SFP 管理 = STI-288DGGPM $137 档），MOQ 1 箱',
           '州 / 法定名 / 老板未核 → 信写 Jeramie（CTO，选品人）；回信后再查 SoS',
           '29 封群发无回 → 第二封只放一张「他家型号 vs 我们型号 + 价差」对照表'],
    notes='第三方 11–50 人数疑虚高；按微型处理（100% 预付）。')
print('US 6 ok')
