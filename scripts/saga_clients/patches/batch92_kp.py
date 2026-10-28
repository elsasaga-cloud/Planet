#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 92 批（T29-U88，公司底数第十轮 · B 档「筛=1」主战场五国 25 户 + 补项 2 处）：把官方 / 准官方登记核出来的「老板 / 董事 / 股权 / 规模 / 集团归属 / 同行与守界判定」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=92 行）+ scripts/saga_clients/registry_batches/b92_*.py。
结构同 batch91_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix（研究档顶层字段，build.py 读取）。
本批附带 1 处国别更正：SB-303 WatchNET 实为加拿大安省 Markham（用户表 US 误）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 92 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- TR ----------
    'SB-097': {'facts': {'legal_name': 'LANSAN TEKNOLOJİ ANONİM ŞİRKETİ（tabela：Lansan Network Bağlantı Ekipmanları；find.com.tr）', 'founded': '2019-12-04（Şişli / İstanbul）' + TAG, 'staff': '小型（估 5–20 人）' + TAG, 'size': '小型（多股东 A.Ş.；自有标签 + 自产光纤配线架）' + TAG, 'hq': 'Şişli / İstanbul' + TAG, 'other': '**供货链警示：深圳联迅 Shenzhen Lianxun High-Tech 以「LANSAN INTL LIMITED」+ Lansan 品牌出口（2003 起，200–300 人）→ 土耳其 Lansan 极可能是该深圳品牌的土方公司 / 总代 = 已有中国货源** → 只给一页价 + 一款样机价，不加厚；OEM 30% 口径' + TAG}},
    'SB-100': [{'kp_match': 'info@telkolink.com', 'name': 'Yusuf Ölçer', 'role': 'Yetkili / General Manager（katalogrehberi 法定联系人；LinkedIn 兼 Gelecekbt.com GM）= **老板 = 联系人 = 拍板人**（直邮 yusuf@telkolink.com）—— **Telkolink（自有标签）与 GelecekBT（gelecekbt.com = SB-275；外部库 XB-C0688）是同一老板的两块牌子 → 三处并一线，只写这一封**；OEM 30% 走 Telkolink 标（PoE 8/16 口 + MC），MOQ 1 箱、100% 预付' + TAG},
               {'facts': {'legal_name': 'Telkolink Gelecek Yönetim Merkezi Eğitim Dan. San. Tic. Ltd. Şti.（perpahaber 名录；创立方 GYM Bilgi Teknolojileri）', 'founded': '2004' + TAG, 'staff': '1–10（Lusha / RocketReach 6）' + TAG, 'size': '微型（Perpa A Blok 老商户）' + TAG, 'hq': 'Perpa Ticaret Merkezi A Blok K.5 No:295-297, Okmeydanı Şişli / İstanbul' + TAG, 'other': '技术支持 sait@telkolink.com；与 SB-275 gelecekbt.com 同一公司 → 并线' + TAG}}],
    'SB-275': {'facts': {'other': '**第 92 批核实：gelecekbt.com 与 Telkolink（SB-100）同一老板 Yusuf Ölçer（LinkedIn「Gelecekbt.com General Manager」+ telkolink.com 联系页）→ 本户并线到 SB-100，不单独发信**；外部库 XB-C0688 同样并线' + TAG}},
    'SB-105': {'facts': {'legal_name': 'CENOVA BİLİŞİM TEKNOLOJİLERİ İTH. İHR. ve TİC. LTD. ŞTİ.（Şişli VD 2060665571）', 'founded': '2002（LinkedIn 2004）' + TAG, 'staff': '16–49（LinkedIn 18；kariyer 25–49）' + TAG, 'size': '小型（Perpa 安防分销；自有品牌 Cenova + TIANDY / Wisetech 土耳其总代，bayi 导向）' + TAG, 'hq': 'Perpa Ticaret Merkezi B Blok K:8 No:902-904, Şişli / İstanbul' + TAG, 'other': 'OEM 30%：PoE 交换机贴 Cenova 标配自家相机；TIANDY 自带 PoE 交换机 = 现有基线，报价落在其下；关联店 Syscom Güvenlik（A Blok K:7）同一客服号；无公开老板姓名 → 写 satın alma' + TAG}},
    'SB-174': [{'kp_match': 'info@karerguvenlik.com', 'name': 'Nurbaki Karataş', 'role': 'CEO / 创始人（2006–今；PESİAD 会员代表；ZoomInfo / RocketReach）= **老板 = 联系人 = 拍板人** —— 公司 = Pendik 1000 m² 批零兼营安防店（11–50 人）→ 分销 20%：STC-028GP / STC-228GP 配相机套装，样机 1 台付费' + TAG},
               {'kp_name': 'Samet Sahin', 'role': 'Director of Technical Services（RocketReach）= 技术口，抄送' + TAG},
               {'facts': {'legal_name': 'Karer Güvenlik Sistemleri Sanayi ve Ticaret Ltd. Şti.', 'founded': '2006' + TAG, 'staff': '11–50（datanyze 13）' + TAG, 'size': '小型（报警 + CCTV 批发 & 零售）' + TAG, 'hq': 'Yayalar Mah. Atasever Cd. No:44, Pendik / İstanbul（0216 397 33 88）' + TAG}}],
    'SB-867': [{'kp_match': 'murat.soyak@erete.com.tr', 'role': 'Kurucu Ortak（三位创始合伙人之一，2001-12 起；ZoomInfo）= **拍板层 = 联系人** —— 公司 = 24 年网络基础设施分销 + 自办「Erete Network Okulu」培训；**已是 XP-Networks（研究档记 Etherwan）工业交换机分销商 = 有工业 PoE 品牌线** → STI 只做第二货源，报价对标同口数 6–7 折，不推 CENTEC；分销 20%' + TAG},
               {'facts': {'legal_name': 'Erete Bilgi Sistemleri Dış Tic. ve San. Ltd. Şti.', 'founded': '2001-12（创始合伙人 Pınar Kabil / Murat Soyak / Timur Yıldız）' + TAG, 'staff': '11–50（ZoomInfo）' + TAG, 'size': '小型（网络产品分销 + 培训）' + TAG, 'hq': 'Güven Sok. 4/2, Şişli / İstanbul（+90 212 212 81 03）' + TAG}}],
    'SB-866': [{'kp_name': 'Levent Pişman', 'role': 'Co-Owner（LinkedIn，10 年以上）= **老板之一 = 联系人**（satis@ 公用箱，抬头写 Levent Bey）—— 公司 = Ümraniye 自有楼「Egemen Plaza」的 10 人安防批发 + B2B 商城 egemendepo.com → 分销 20%：8/16 口 PoE + 4 口 DIN 先上商城；单笔 ≤ $3k，100% 预付或 50/50' + TAG},
               {'facts': {'legal_name': 'Egemen Elektronik Güvenlik Bilgisayar Sistemleri San. ve Tic. Ltd. Şti.', 'founded': '2013-07-25（EMIS）' + TAG, 'staff': '7–19（EMIS 2025：10 人；LinkedIn 11–50）' + TAG, 'size': '微型 / 小型（安防批发）' + TAG, 'hq': 'Ihlamurkuyu Mh. Malazgirt Cd. Şendal Sk. No:1 Egemen Plaza, 34771 Ümraniye / İstanbul（0216 611 61 00）' + TAG}}],
    # ---------- US / CA ----------
    'SB-108': {'facts': {'legal_name': 'GW Security（BBB 档；加州法定名未核）', 'founded': '2016-12-08（BBB Business Started）' + TAG, 'staff': '小型（估 5–20 人）' + TAG, 'size': '小型（自有品牌安防套装：Amazon + 官网直销）' + TAG, 'hq': '1230 Santa Anita Ave Ste A, South El Monte, CA 91733（洛杉矶东）' + TAG, 'other': 'BBB 未认证、有发货 / 售后投诉 + Reddit 技术支持差评 = 售后薄弱 → 把 3 年保 / 英文固件 / 远程配置支持写成卖点；**OEM 30%：8/16 口 PoE 贴 GW 标配 NVR 套装**，样机 1 台付费；高管未核 → 抬头 Purchasing' + TAG}},
    'SB-303': [{'kp_match': 'harish@watchnetinc.com', 'name': 'Harish Babu Vettukuzhiyil', 'role': 'Vice President, Sales & Marketing（2022–；ZoomInfo / contactout）= 销售副总（抄送）—— **公司在加拿大安省 Markham，用户表国别 US 误 → country_fix 加拿大**；自有品牌产品线含「Network Switches」= **现成 OEM 品牌商** → 换写采购物流经理 Karthikeyan R（抄 Harish），只给 OEM 30% 两款（8 口 PoE / 24 口 PoE+2SFP 贴 WatchNET 标）' + TAG},
               {'add_kp': {'name': 'Karthikeyan R', 'role': 'Procurement & Logistics Manager（contactout / signalhire）= **采购口 = 本轮首选收件人**（邮箱格式待推，first@watchnetinc.com）' + TAG, 'email': '', 'phone': '', 'source': 'https://contactout.com/company/watchnet-inc-5690'},
                'facts': {'legal_name': 'WatchNET Inc.（Markham, Ontario, Canada；Ontario 公司号未取）', 'founded': '2000' + TAG, 'staff': '33–50（RocketReach 33 / datanyze 50；LinkedIn 11–50）；第三方营收区间 $10–14M' + TAG, 'size': '中小型（视频监控 / 门禁 / IoT 自有品牌供应商，北美 + 中东）' + TAG, 'hq': '351 Ferrier St Unit 5, Markham, Ontario L3R 5Z2, Canada' + TAG, 'other': '管理层：Milly Prince Executive Director / Roman Dabrowski VP / Matthew Durkee Director Sales USA / Joe Saju Financial Controller；研究档「Utepo」= 现 PoE 货源同类 → 价格对标 HRUI 档再让 5%；发信窗口按美东 Wed 08–10；证书 ISED/FCC + CE' + TAG},
                'country_fix': '加拿大'}],
    'SB-347': [{'kp_match': 'kang.yu@avcomm.us', 'role': 'CEO / COO / Director（多源；H-1B 申报 Director；WHOIS 注册人；IANA PEN 57842 联系人）= 老板 —— **守界：这是同行 —— 华人团队在休斯顿运营的工业交换机自有品牌（自有 6000 系列 PoE 工业机 + 北京产品工程师 = 自己有设计 + 中国供应链）→ B 不再加厚**；若写只问一句「缺哪一款工业口型」，不发价格表' + TAG},
               {'facts': {'legal_name': 'AVCOMM Technologies Inc.（Houston, TX；TX SoS 档号未取）', 'founded': '2018（官网；LinkedIn 2019）' + TAG, 'staff': '6–50（H-1B 雇主）' + TAG, 'size': '小型（工业以太网 / IIoT / 边缘计算 自有品牌）' + TAG, 'hq': '333 West Loop N, Houston, TX 77024' + TAG, 'other': 'H-1B 记录 CEO Xiao Luo；VP Ops Yukon Yu；Product Engineer Brenda Guan（北京）' + TAG}}],
    'SB-349': {'add_kp': {'name': 'Ziqiang (John) He', 'role': 'CEO / Secretary / CFO / Director / Registered Agent（加州 SoS 2772255 五职一人；官网「创始人 John He」，网络 TAP 发明人）= **老板 = 唯一联系人** —— 一人工程师公司，主业网络 TAP / 同轴传以太网，PoE 交换机只是配套 SKU → B 不加厚；若写只写一句 Dualcomm 标 8 口 PoE OEM 30% 单价 + MOQ 1 箱' + TAG, 'email': '', 'phone': '', 'source': 'https://www.bizprofile.net/ca/danville/dualcomm-technology-inc'},
               'facts': {'legal_name': 'Dualcomm Technology, Inc.（California General Corporation；SoS 2772255；Good Standing 四项）', 'founded': '2005-09-12' + TAG, 'staff': '1–10（一人公司）' + TAG, 'size': '微型（自研网络 TAP / EoC，网店直销 15,000+ 客户）' + TAG, 'hq': '注册 435 Glasgow Cir, Danville, CA 94526；邮寄 UPS 信箱 2415 San Ramon Valley Blvd #4182, San Ramon, CA 94583' + TAG}},
    'SB-350': [{'kp_match': 'ccosta@edge-networks.us', 'name': 'Christopher (Chris) Costa', 'role': 'President & CTO / 创始人（2019；前 Comnet VP Eng 2011–2020、Radiant Communications 工程总监、GE Security 工程总监，1996 起设计安防产品）= **老板 = 技术拍板 = 联系人** —— **目标序列第一位「OEM 品牌商」标准像：2–10 人自有品牌，产品线 = MC + 工业交换机 + 延长器 + 光纤 modem，全部外采贴标 → OEM 30% 全线**（STI-154GP / STI-288DGGPM 工业 DIN + MC + 8/16 口 PoE 贴 Edge Networks 标）；信写参数（芯片 / 温宽 / MTBF / CE-FCC-RoHS，**不写 UL / NDAA**），第二封 = spec sheet + 一款样机价；建议升 A 候选' + TAG},
               {'add_kp': {'name': 'Steven Carrozzo', 'role': 'Vice President, Sales（ZoomInfo）= 商务口，抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://www.zoominfo.com/pic/edge-networks/482033602'},
                'facts': {'legal_name': 'Edge Networks LLC / Edge Networks USA（Charleston, SC；SC SoS 号未取）', 'founded': '2019' + TAG, 'staff': '2–10（Tracxn 2 / ZoomInfo 1–10）' + TAG, 'size': '微型（自有品牌工业以太网 / MC 制造商 —— 实为外采贴标）' + TAG, 'hq': '412 Brandam Ln Ste 103, Charleston, SC 29492（(843) 654-9266）' + TAG, 'other': '「USA based」是其卖点 = 贴标后不提来源，正合中性包装；单笔 $3–10k，T/T 50/50；复盘：每季看官网新品型号' + TAG}}],
    'SB-362': {'add_kp': {'name': 'Jeramie Cavanaugh', 'role': 'Chief Technology Officer（ZoomInfo）= 推定合伙人 / 选品人 = 联系人 —— 网店型自有型号卖家（PoE 是主类目，首页挂工业 8 口 PoE+ L2+ 管理 2SFP）→ **OEM 30%：按他现有型号一对一替代报价**（工业 8 口 PoE+2SFP 管理 = STI-288DGGPM 档），MOQ 1 箱；第二封只放「他家型号 vs 我们型号 + 价差」对照表' + TAG, 'email': '', 'phone': '', 'source': 'https://www.zoominfo.com/c/main-tech-connect/1275453111'},
               'facts': {'legal_name': 'Main Tech Connect（州 / 法定名未核；**同名陷阱：Maintech, Incorporated 新泽西 1973 年 500+ 人 IT 运维商非本户**）', 'founded': '2001（ZoomInfo）' + TAG, 'staff': '11–50（ZoomInfo，疑虚高；按 2–10 人电商处理）' + TAG, 'size': '微型 / 小型（电脑 / 网络配件 + PoE 电商）' + TAG, 'hq': '美国（州未取）' + TAG}},
    # ---------- GB ----------
    'SB-147': [{'kp_match': 'tek@genieproducts.co.uk', 'role': 'Technical Director（LeadIQ「T.O.」；2008 起在 Genie，非登记董事）= 技术口 / 样机测试人 —— **法定主体 BIOACCESS SALES LIMITED（12058650，2019-06 新设）；2023-03-21 两位创始董事同日辞任、Sharon Gorf 独任董事 = 公司换手，新东家两年内重审供应链 = 进门时机**；「Designed in Britain」Trade Only 安防自有品牌，全部外采贴标 → **OEM 30%：PoE 交换机贴 Genie 标配 IP 相机 / NVR**，第二封一页（单价 + 定制 logo / 包装 + UKCA）' + TAG},
               {'add_kp': {'name': 'Sharon Gorf', 'role': 'Director（唯一在任，2023-03-21 起；Companies House 12058650；身份已核验）= **现老板 / 签单人**' + TAG, 'email': '', 'phone': '', 'source': CH + '12058650/officers'},
                'facts': {'legal_name': 'BIOACCESS SALES LIMITED t/a Genie Products（Companies House 12058650；VAT GB 325 6941 88；**同名陷阱：Genie Products Ltd 16201440 Newquay / Genie Products Limited 09877102 Uttoxeter 均非本户**）', 'founded': '2019-06-19（品牌 Genie 早于此）' + TAG, 'staff': '11–50（LeadIQ ≈13）；SIC 26309' + TAG, 'size': '小型（英国安防自有品牌，Trade Only）' + TAG, 'hq': '营业 Caxton Point Business Centre, Caxton Way, Stevenage SG1 2XU；注册 c/o Becktech Limited, Terminus Road, Chichester PO19 8DW' + TAG, 'other': '账目至 2025-11-30 已报，下期 2027-08-31 到期；PSC 待补；微型账目 → T/T 50/50、MOQ 1 箱' + TAG}}],
    'SB-129': {'add_kp': {'name': 'Wen-Cheng Lee', 'role': 'Director（2006-07-31 起）兼 Secretary（2001-10-27 起；英籍，1965 生；身份已核验；Companies House 04256748）= **老板 = 唯一在任高管 = 采购本人** —— 台裔一人公司，2001 起做网络 / 电脑配件分销 24 年；打开 1 次 = 他看过 → 写 Mr Lee 本人；**分销 20%**：STC-028GP / STC-228GP / STC-2224GP 含税到仓价，MOQ 1 箱，100% 预付' + TAG, 'email': '', 'phone': '', 'source': CH + '04256748/officers'},
               'facts': {'legal_name': 'ADDON TECHNOLOGY LTD（Companies House 04256748）', 'founded': '2001-07-23' + TAG, 'staff': '微型（估 2–10 人）；SIC 62090' + TAG, 'size': '微型（华人小分销，有进口经验）' + TAG, 'hq': 'Ground Floor, Building 3, Oakleigh Road South, North London Business Centre, London N11 1GN' + TAG, 'other': '账目至 2025-03-31 已报，下期 2026-12-31 到期；前董事 Tsuen Her Ling（同住址）2015-08 辞任；PSC 待补（推定 Lee 100%）' + TAG}},
    'SB-206': [{'kp_match': 'luke.walsh@brainboxes.com', 'role': 'Managing Director 兼登记 Director（2015-04-20 起；Walsh 家族二代；Companies House 03245094）= 拍板人 —— **守界：利物浦家族制造商（1984 起，自产串口 / 以太网 IO 模块 + 工业交换机，「Made in Britain + 终身保修」）= 我们 STI 对其是竞品而非货源 → B 不加厚**；唯一缝隙：PoE / 千兆管理型口数少，可问采购经理 Kevin Whittaker 是否补一款 OEM（与「Made in Britain」冲突，概率低）；21 封无回 = 没需求' + TAG},
               {'kp_match': 'stephen.greer@brainboxes.com', 'role': 'Sales Director 兼登记 Director（2023-07-11 起）= 销售口（同行，不发价格表）' + TAG},
               {'add_kp': {'name': 'Kevin Whittaker', 'role': 'Purchasing Manager（RocketReach）= 采购口（唯一可能的 OEM 补缺对话人）' + TAG, 'email': '', 'phone': '', 'source': 'https://rocketreach.co/brainboxes-ltd-profile_b5c74e47f42e0d1b'},
                'facts': {'legal_name': 'BRAINBOXES LIMITED（Companies House 03245094；VAT GB 414 5683 52；DUNS 525564092；曾用名 Brain Boxes Limited 1996–2006）', 'founded': '1996-09-03（业务 1984 起）' + TAG, 'staff': '中小型（估 30–60 人；第三方营收 $7.8M 仅区间）；SIC 26512' + TAG, 'size': '中小型（家族制造商）' + TAG, 'hq': '18 Hurricane Court, Hurricane Drive, Speke, Liverpool L24 8RL（0151 220 2500）' + TAG, 'other': '董事：Eamonn Thomas Walsh（创始人，兼 Secretary）/ Patricia Anne Walsh / Luke James Walsh / Joanne Walsh（2023-07）/ Stephen John Greer（2023-07）；PSC 3 名（Walsh 家族）；账目至 2025-10-31 已报，下期 2027-07-31' + TAG}}],
    'SB-740': {'add_kp': {'name': 'Wadii Kherfani', 'role': 'Director（2020-02-12 起；1978 生；Companies House 12459641）= **老板 = 采购 = 联系人**（配偶 Anna Kherfani 2021-05 起亦为董事）—— 夫妻店自有品牌「BCP」结构化布线 + 机柜（自称 British manufacturer，实为 ISO 9000 工厂代工贴标）+ 关联 Teltronix Holdings Ltd（12455268）→ 产品线缺有源设备 → **OEM 30%：BCP 标 PoE 交换机 / 工业 DIN 补「end-to-end」方案**；MOQ 1 箱、T/T 50/50 或 100% 预付' + TAG, 'email': '', 'phone': '', 'source': CH + '12459641/officers'},
               'facts': {'legal_name': 'BRITANIC CABLING PRODUCTION LIMITED（Companies House 12459641；曾用名 TELTRONIX INTERNATIONAL LIMITED 2020-02 → 2021-02）', 'founded': '2020-02-12（官网自述 2004 起）' + TAG, 'staff': '微型 / 小型（估 3–15 人）；SIC 26309 / 27310 / 27320 / 46520' + TAG, 'size': '微型（自有品牌布线 + 机柜）' + TAG, 'hq': '注册 7 Premier Court, Boarden Close, Moulton Park Industrial Estate, Northampton NN3 6LF；营业 Unit 7 Cirrus Park, Lower Farm Road, Northampton NN3 6UR（+44 1604 434188）' + TAG, 'other': '账目至 2025-03-31 已报，下期 2026-12-31 到期；若回信来自 Teltronix 不算新客户' + TAG}},
    # ---------- DE ----------
    'SB-170': [{'add_kp': {'name': 'Eduard Mushkatin', 'role': 'Geschäftsführer / 创始股东（2006 起；AG Düsseldorf HRB 60247；XING 对外联系人）= **老板 = 联系人**（抄 Igor Balter）—— 自有品牌 BALTER（视频监控 / 门禁 / 报警全系贴标，研究档记 Utepo / 洪瑞 PoE）= OEM 品牌商序列第一位，现 PoE 货源是深圳同类 → **OEM 30% 一对一替代**（按 balter.de 在售 PoE 型号列对照：4/8/16 口 + 工业 DIN，贴 BALTER 标、德语包装）；品牌已外延到厨电 = 精力分散 → 一封讲清价差即可' + TAG, 'email': '', 'phone': '', 'source': 'https://www.balter.de/impressum'},
                'facts': {'legal_name': 'Balter GmbH（原 Balter Security GmbH；AG Düsseldorf HRB 60247；USt DE263994622；LEI 9845005D0A88DC60F633）', 'founded': '2006（业务）/ 2008-12-23 登记' + TAG, 'staff': '小型（估 10–30 人）' + TAG, 'size': '小型（安防自有品牌 + 网店 redshop.de；Stammkapital €25,000）' + TAG, 'hq': 'Elisabeth-Selbert-Str. 19, 40764 Langenfeld (Rheinland)（+49 211 22975914）' + TAG, 'other': '两位 GF / 创始股东 Igor Balter + Eduard Mushkatin；单笔 $3–10k，T/T 50/50；复盘 2027-03' + TAG}},
               {'add_kp': {'name': 'Igor Balter', 'role': 'Geschäftsführer / 创始股东（公司冠名人）= 老板，抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://www.northdata.com/Balter%20GmbH,%20Langenfeld%20(Rheinland)/Amtsgericht%20D%C3%BCsseldorf%20HRB%2060247'}}],
    'SB-145': {'facts': {'legal_name': 'DigiComm Gesellschaft für Kommunikationssysteme mbH（AG Neuss HRB 5172）→ 2024-09 并入 AddSecure DigiComm GmbH', 'founded': '1987' + TAG, 'staff': '11–50；母公司 AddSecure 1,000+' + TAG, 'size': '集团子公司（Bechtle → 2023-11 AddSecure（瑞典）→ 2024-09 吸收合并）' + TAG, 'hq': 'Breite Str. 10, 40670 Meerbusch（02159 69375-0）' + TAG, 'other': '**守界：研究档「自有 logo 工业交换机」成立，但采购 / OEM 决策已上收 AddSecure 集团 → B「不再补查」，不再发**；GF Andreas Kluß（2024-05 起，集团任命）' + TAG}},
    'SB-213': [{'kp_match': 'pkaiser@kti.de', 'name': 'Paul Kaiser', 'role': 'Management（kti.de 团队页；Kaiser 家族二代；GF 为 Peter Kaiser，AG Bielefeld HRB 35444）= 联系人 —— **守界：KTI Distribution = 台湾 Katron Technologies（KTI Networks，1983）在 DACH 的独家进口 + 品牌代理（captive 分销，25 年单一货源）→ 研究档「自己的牌子」实为 Katron 的牌子 → B 不动**；唯一缝隙：Katron 缺的口型（2.5G PoE / 高瓦 BT）可一句话问' + TAG},
               {'facts': {'legal_name': 'KTI Distribution GmbH Netzwerkkomponentenhandel（AG Bielefeld HRB 35444；LEI 5299004AYCZJWJVHYO42）', 'founded': '≈1998–2001（Stammkapital 50,000 DEM）' + TAG, 'staff': '微型 / 小型（家族，估 3–10 人）' + TAG, 'size': '微型（单一品牌 DACH 总代）' + TAG, 'hq': 'Meisenstraße 79a, 33607 Bielefeld（+49 521 966800）' + TAG, 'other': 'GF Peter Kaiser；团队 Thomas Passlack / Danuta Kaiser；复盘：每年 3 月看 kti.de 是否出现非 Katron 型号' + TAG}}],
    'SB-368': [{'kp_match': 'j.zenner@welotec.com', 'role': 'Geschäftsführer / CTO（2018-03 起 GF；AG Steinfurt HRB 3363）—— **守界：Welotec 2025-04 起属 Westermo（Ependion AB，全球头部工业交换机制造商）集团，Westermo 派驻 Dr. Reinhard Lülff 2025-07 起单独代表 GF → 交换机货源 = 母公司 → B「不再补查」，不再发**' + TAG},
               {'facts': {'legal_name': 'Welotec GmbH — a Westermo Company（AG Steinfurt HRB 3363；USt DE121631449；Stammkapital €67,000）', 'founded': '1979-05-15（业务 1969）' + TAG, 'staff': '≈70 人；2024 营收 ≈ €24M（经营利润率 13.4%）' + TAG, 'size': '中型（集团子公司）' + TAG, 'hq': 'Zum Hagenbach 7, 48366 Laer（+49 2554 9130-00）' + TAG, 'other': '2023 年报：总资产 €8.34M / 负债 €6.68M；前 GF Daniel Maurice 2025-07 退出；此前控股 WELOTEC Holding GmbH（HRB 9320 Steinfurt）' + TAG}}],
    'SB-698': [{'kp_match': 'info@cbo-it.de', 'role': 'Project Manager（用户表）= 项目口 —— **本轮改写 GF Michael Abel**（光模块自有品牌商，交换机只是副线；Saga 不供光模块 Q-32 → 唯一一条线 = **CBO 标工业 / 商用交换机 OEM 30%** 配他们自家光模块卖套装）；第二封只给「CBO 标 8 口 PoE+2SFP 工业机 / 24 口 +4 SFP 管理型」两行价' + TAG},
               {'add_kp': {'name': 'Michael Abel', 'role': 'Geschäftsführer（Northdata：cbo GmbH, Schliersee, AG München HRB 93986 —— **推定匹配**，回信后以 Impressum 核 HRB）= 老板之一 = 本轮收件人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.northdata.com/cbo%20GmbH,%20Schliersee/Amtsgericht%20M%C3%BCnchen%20HRB%2093986'},
                'facts': {'legal_name': 'cbo GmbH（原 cbo Computer- und Bürotechnikvertrieb Oberland GmbH；AG München HRB 93986；股东 BTW-IT GmbH —— 推定匹配）', 'founded': '≈1990 年代（Stammkapital 80,000 DEM）' + TAG, 'staff': '小型（估 10–30 人）' + TAG, 'size': '小型（光模块 / AOC 自有品牌 CBO + 网络设备）' + TAG, 'hq': 'Miesbacher Str. 16, 83727 Schliersee（上巴伐利亚）' + TAG, 'other': 'GF Michael Abel / Thomas Seebauer；控股 BTW-IT GmbH；T/T 50/50 可谈；复盘 2027-03' + TAG}}],
    # ---------- PL ----------
    'SB-092': {'add_kp': {'name': 'Mikołaj Adam Tomaszewski', 'role': 'Prezes Zarządu 兼唯一股东（1,000 股 / 50,000 zł；KRS 0000993625；个体户 NIP 6981681757 ≈2005 起）= **老板 = 签单人 = 联系人** —— **一人持股、年营收 ≈29.7 mln zł（≈$7.4M）的自有品牌电商（Spacetronik 标，研究档记「洪瑞 工商 switch 自己 logo」）= OEM 品牌商序列第一位，现货源是深圳同类 → OEM 30% 一对一替代**（按 spacetronik.pl 在售 PoE / 工商交换机型号列对照，贴 Spacetronik 标 + 波兰语包装），MOQ 1 箱起、量大按柜谈；资产 22.3 mln zł = 扩张期 → T/T 30/70 可谈；建议升 A 候选' + TAG, 'email': '', 'phone': '', 'source': 'https://www.bizraport.pl/krs/0000993625/spacetronik-spolka-z-ograniczona-odpowiedzialnoscia'},
               'facts': {'legal_name': 'Spacetronik Sp. z o.o.（KRS 0000993625 · NIP 6981862105 · REGON 523197029）', 'founded': '2022-09-23（sp. z o.o.；个体户 ≈2005 起）' + TAG, 'staff': '中小型（估 30–80 人）；营收 ≈29.7 mln zł / 资产 22.3 mln zł（KRS 财报）' + TAG, 'size': '中小型（消费 / 安装电子自有品牌电商 + 批发）' + TAG, 'hq': 'ul. Wiśniowa 36, 64-000 Kościan（波兹南以南）' + TAG, 'other': '登记主 PKD 46.65.Z（办公家具批发）与实际品类不符；VAT 活跃；KRZ 无记录；复盘 2027-07' + TAG}},
    'SB-156': [{'kp_match': 't.b.nowak@cyberteam.pl', 'role': 'Prezes Zarządu / 股东（2007-07-24 起；1975 生；KRS 0000285290）= **老板 = 拍板人 = 联系人** —— 自有品牌 MC / 光纤产品 + 营收 ≈23.5 mln zł（≈$5.9M）+ 经济特区厂址（有组装 / 制造）→ **OEM 30%：Cyberteam 标 MC + 8/16 口 PoE + 工业 DIN**（只给整机贴标，不做裸板）；第二封 = 一句话 + 对照表' + TAG},
               {'facts': {'legal_name': 'Cyberteam Sp. z o.o.（KRS 0000285290 · NIP 9222908443 · REGON 060265810）', 'founded': '2007-07-24' + TAG, 'staff': '中小型（估 20–50 人）；营收 ≈23.5 mln zł / 资产 8.2 mln zł' + TAG, 'size': '中小型（网络 / 光纤自有品牌 + 元件批发制造；股本 200,000 zł）' + TAG, 'hq': 'ul. Strefowa 8, 22-400 Zamość' + TAG, 'other': 'Wiceprezes Radosław Marcin Skwarek；Prokurent Mirosława Ziemian；关联 Nowak Technologie（同一线）；复盘 2027-07' + TAG}}],
    'SB-177': [{'kp_match': 'esklep@ecsystem.pl', 'name': 'Daniel Ochman', 'role': '电商 / 英文客服（ecsystem.pl 联系页「Customer service in English」）= 网店口 —— **改写 handel@ecsystem.pl（批发口）抬头 Daniel，抄 Prezes Mirosław Gabzdyl**；公司 = 克拉克夫安防集成商 + 自营网店（卖 Hasivo 等深圳 PoE）= 渠道不是品牌商 → **分销 20%**：STC-028GP / STC-228GP / STC-2224GP 对标 Hasivo 同口数，MOQ 1 箱，100% 预付' + TAG},
               {'add_kp': {'name': 'Mirosław Gabzdyl', 'role': 'Prezes Zarządu（rejestr.io；KRS 0000181283）= 老板，抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/181283/eltcrac-system'},
                'facts': {'legal_name': 'Eltcrac System Sp. z o.o.（EC System；KRS 0000181283 · NIP 6792784999 · REGON 356766841）', 'founded': '≈2003' + TAG, 'staff': '小型（估 10–25 人）' + TAG, 'size': '小型（安防集成 + 电商；股本 50,000 zł；同主体兼营刀具 / 园艺网店 knivesfamilia / gards）' + TAG, 'hq': 'ul. Ruciana 3, 30-803 Kraków（+48 12 292 48 61）' + TAG, 'other': '信箱：handel@ / biuro@ / inwestycje@ / esklep@；复盘 2027-07' + TAG}}],
    'SB-250': [{'kp_match': 'dariusz.piwowar@pf-electronic.', 'role': 'Wiceprezes Zarządu（2005-09-06 起；KRS 0000046753；可单独代表）= **合伙人 = 拍板层 = 联系人** —— 西里西亚工业自动化分销 + 服务商（PLC / 变频 / 工业网络，25 年，营收 ≈9.3 mln zł）→ **工业 DIN 线分销 20%**：STI-054GP / STI-154GP / STI-288DGGPM 配 PLC 柜，样机 1 台付费；第二封只写工业场景（温宽 / DIN / 冗余供电 / ERPS），不写 CCTV' + TAG},
               {'add_kp': {'name': 'Jacek Andrzej Nędza', 'role': 'Prezes Zarządu（2005-09-06 起）= 老板之一，抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/46753/pf-electronic'},
                'facts': {'legal_name': 'PF Electronic Sp. z o.o.（KRS 0000046753 · NIP 6342396659 · REGON 276904785）', 'founded': '2001-10-15（业务 2000 起）' + TAG, 'staff': '小型（估 10–25 人）；营收 ≈9.3 mln zł（≈$2.3M）' + TAG, 'size': '小型（工业自动化分销 + 维修安装 + 网店；股本 127,500 zł）' + TAG, 'hq': 'ul. Stanisława Konarskiego 18C, 44-100 Gliwice（+48 32 256 25 33；旧址 Katowice Bednorza 2a-6）' + TAG, 'other': '复盘 2027-07' + TAG}}],
    # ---------- 补项（第 91 批遗留） ----------
    'SB-231': {'facts': {'other': '第 92 批补 PSC：Nathan James Parys ≥75%（2025-04-02 起）；前控制人 Mrs Jie Kennett（中国籍）≥75% 2017-09 → 2025-04-02 终止 → **换手坐实：新东家 100% 控股、一人决策，供应商重建中**' + TAG}},
    'SB-574': {'facts': {'other': '第 92 批补 zarząd：**2025-07-01 换届** —— Prezes Marcin Chojnacki、Członek Łukasz Wardak 新任，Wiceprezes Tadeusz Alankiewicz（2015 起）留任，创始人 Robert Żurek 夫妇退居监事会；Prezes / Wiceprezes 可单独签 → 新管理层一年内重审品类 = Lanberg 交换机 OEM 进门窗口；RDF 2023–2025 年报已报；KRZ 无记录' + TAG}},
}


def apply(d, u):
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if u.get('name') and not k.get('name'):
                    k['name'] = u['name']
                if u.get('name') and k.get('name') and k.get('name') != u['name'] and TAG not in (k.get('role') or ''):
                    k['name'] = u['name']
                if u.get('role') and TAG not in (k.get('role') or ''):
                    k['role'] = u['role']
    if u.get('kp_name'):
        for k in kps:
            if (k.get('name') or '') == u['kp_name'] and TAG not in (k.get('role') or ''):
                k['role'] = u['role']
    if u.get('add_kp') and not any(u['add_kp']['name'] == (k.get('name') or '') for k in kps):
        kps.append(u['add_kp'])
    seen, dedup = set(), []
    for k in kps:
        key = (k.get('name'), k.get('email'), k.get('role') or k.get('title'))
        if key in seen:
            continue
        seen.add(key); dedup.append(k)
    d['kp'] = dedup
    cf = d.get('company_facts') or {}
    for fk, fv in (u.get('facts') or {}).items():
        if TAG not in str(cf.get(fk, '')) and fv:
            cf[fk] = fv if fk != 'other' or not cf.get('other') else (cf['other'] + '；' + fv)
    d['company_facts'] = cf
    if u.get('country_fix'):
        d['country_fix'] = u['country_fix']


if __name__ == '__main__':
    for code, u in UPD.items():
        p = os.path.join(RESEARCH_DIR, f'{code}.json')
        d = json.load(open(p, encoding='utf-8'))
        for one in (u if isinstance(u, list) else [u]):
            apply(d, one)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(code, 'ok')
