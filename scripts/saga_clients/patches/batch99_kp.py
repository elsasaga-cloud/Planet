#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 99 批（T29-U92，公司底数第十七轮 · B 档「自有 logo + 打开」五国 24 户）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=99 行）。
结构同 batch98_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：OEM 30% 首选 3（SB-1051 Klemsan / SB-1019 Connectix / SB-541 KBC Networks）；自有标 OEM 30% 目标 2（SB-427 Longline / SB-777 TMB ProPlex-北京办事处）；
分销 20% 首选 1（SB-1039 ICO）；分销 20% 5（SB-1065 Delta-Opti / SB-1015 BR Network+贴标 / SB-465 Koza / SB-527 AvaLAN→Volume Inc / SB-1058 Multiproject-PLANET 替代）；
贴标 small 3（SB-1056 Mikrodev / SB-1025 ELFON / SB-1013 Lysora-未坐实）；集成商 25% 1（SB-281 multiGuide）；低概率 2（SB-253 Provision-ISR TVT 贴牌 / SB-1080 Sphinx MOXA 分销）；
一页纸 small 5（SB-435 Saucon 车载守界 / SB-1010 Bayiden / SB-1094 VideoBits / SB-1099 ZXTech 消费级 / SB-1045 ITM）；未坐实 3（SB-1013 / SB-737 / SB-1095）；
国别更正 1（SB-253 以色列）；KP 坐实 = 老板 / 董事 / Prokurist 本人 4（SB-435 CEO 创办人 / SB-1080 Prokurist / SB-281 Prokurist+产品经理 / SB-541 President）；升 A 候选 6（SB-1051 / SB-1019 / SB-541 / SB-427 / SB-1039 / SB-1065）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 99 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US / IL ----------
    'SB-777': {'add_kp': {'name': 'Colin Waters', 'role': 'Co-founder / CEO（1983 创办，前巡演技术员；PLASA 2025 仍为 Chief Executive）= 拍板人；收件走 sales@tmb.com 点名 ProPlex 产品经理' + TAG, 'email': '', 'phone': '', 'source': 'https://tmb.com/about/company-profile/'},
               'facts': {'legal_name': 'TMB（TMB Production Supplies & Services；品牌 ProPlex / ProCable / ProPin / ProFibre / ProPower；加州法定名 / SoS 号未取）', 'founded': '1983（LinkedIn 1984）' + TAG, 'staff': '51–200 人', 'hq': '527 Park Avenue, San Fernando, CA 91340（+ Carlstadt NJ / Southall UB2 / Meaford ON / 北京 / Marupe LV）',
                         'other': '第 99 批：自有标 ProPlex GBS PoE 交换机（导轨 5 口 / 便携 6 口）= OEM 30% 目标，但北京办事处 = 已直采 → 一页纸，卖 Marvell 管理型 + IGMP（Art-Net / sACN 多播）+ 3 年保修 + MOQ 1；B BIG；不加厚' + TAG}},
    'SB-253': {'country_fix': '以色列',
               'kp_match': 'sales@provisionisr.com', 'role': 'Technical & Presale Manager（选型人）= 收件人' + TAG,
               'facts': {'legal_name': 'Provision-ISR（以色列 Kfar Saba 私有公司；美国销售子公司 Provision-ISR USA, Dallas TX；公司号未取）', 'founded': '2007' + TAG, 'staff': '51–200 人；USA 11 人 ≈$22M', 'hq': '11 Atir Yeda St, Kfar Saba 4442510, Israel（+ 2472 Southwell Rd, Dallas TX 75229；Medley FL 物流；深圳宝安办公室）',
                         'other': '第 99 批：**国别更正 US → 以色列**；CCTV 品牌商，摄像机由深圳 TVT 贴牌 + 宝安办公室 → 自有标 PoE 交换机已同源直采 → OEM 30% 低概率；Simon「可以尝试多跟进一下」→ 一页纸 Marvell 管理型 L2+ PoE（STC-424XGGPM-280W）差异化，写 Leonardo Severi 抄 sales@；发信窗口 Sun–Thu 10–12 IST；不提 TVT' + TAG}},
    'SB-1013': {'kp_match': 'barros', 'role': '研究档联系人（职务未核；官方登记 1 次未命中 → 未坐实）= 收件人' + TAG,
                'facts': {'legal_name': 'Business Systems Consulting（bizsyscon.com；密苏里；法律形式未核 —— 同名企业多，1 次检索未命中）', 'founded': '1997（自述）' + TAG, 'staff': '2–10 人', 'hq': '圣路易斯郊区（门牌未核）',
                          'other': '第 99 批：**未坐实**；研究档「自有品牌 Lysora + 在售 PLANET GS-4210-24P4C / IGS」仍成立 → 贴标试探 small：Lysora 标 STI-288DGGPM 对标 PLANET IGS；一页纸；下轮不追' + TAG}},
    'SB-435': {'kp_match': 'bfrench@', 'role': 'CEO & Founder / President（1997 创办；Cummins 2023 新闻稿、Buzzfile、D&B 一致）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Saucon Technologies, Inc.（宾夕法尼亚；SAM 在册 Small Business / SDB）', 'founded': '1997' + TAG, 'staff': '28–42 人；$10–15M', 'hq': 'Bethlehem, PA 18020',
                         'other': '第 99 批：客运巴士车载 telematics（车载视频 / 乘客 Wi-Fi）→ 车规 / E-mark 守界 → 只谈车场 / 调度中心侧商业 PoE（STC-228GP / STC-2224GP）；一页纸；CFO William Bouffard' + TAG}},
    'SB-527': [{'kp_match': 'cindy.powers@', 'role': 'Director（AvaLAN，Dover Fueling Solutions 业务单元）= 抄送' + TAG},
               {'kp_match': 'sales@volumeinc.com', 'role': 'Product Manager, Volume Inc.（燃油中心托管网络 + 网络设备批发；AvaLAN 2020 起合作商）= **主收件人（分销 20% 线）**' + TAG},
               {'add_kp': {'name': 'Matt Nelson', 'role': 'Managing Director & GM（原 CEO / President 2008 起；2021-04 Dover 收购后任 Sr. Director & GM；2024-02 起兼管 Bulloch Technologies）= 拍板人（集团流程）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.cbinsights.com/company/avalan-wireless'},
                'facts': {'legal_name': 'AvaLAN Wireless Systems Incorporated（AvaLAN Networks；2021-04-19 起 Dover Fueling Solutions / Dover Corporation NYSE: DOV 全资）', 'founded': '2004（硅谷）→ 2008 迁 Alabama' + TAG, 'staff': '11–50 人', 'hq': '127 Jetplex Circle, Madison, AL 35758 / Huntsville, AL',
                          'other': '第 99 批：Dover 子公司 → 自有标 AW24PTPOE 等 PoE 已有代工 + 集团供应商准入 → OEM 30% 低概率；现实线 = Volume Inc. 分销 20%（STC-028GP / STC-2216GP + 工业 STI-054GP 给加油机 / 前庭）；一页纸' + TAG}}],
    'SB-541': [{'kp_match': 'skuntz@', 'role': 'President = **拍板人 = 主收件人**' + TAG},
               {'kp_match': 'info@kbcnetworks.com', 'role': 'VP Business Development（2010-09 起，LinkedIn）= 抄送' + TAG},
               {'facts': {'legal_name': 'KBC Networks（美国 San Juan Capistrano CA 实体 + 英国 KBC Networks Ltd, Dartford；CEO Jonathan Crockett；Founder & Managing Partner Ramesh Koya；CCO Luis Angulo）', 'founded': '2008（美国口径）/ 2010（英国口径）' + TAG, 'staff': '51–200 人（67–102）；≈$30M', 'hq': '32409 Calle Perfecto, San Juan Capistrano, CA 92675（旧址 25691 Atlantic Ocean Dr, Lake Forest）；Dartford, Kent UK',
                          'other': '第 99 批：**定性 = 品牌商而非同行**：KBC 标加固工业交换机（2–24 口 PoE / 全 SFP / IP40 / -40~75 °C）卖给安防 / ITS 集成商 = 华南工业公模规格 → **OEM 30% 目标（B BIG），升 A 候选**；对口 STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM；首信只谈「第二供应商 / 管理型升级」；美英双总部可各发一次' + TAG}}],
    # ---------- TR ----------
    'SB-1010': {'facts': {'legal_name': 'Bayiden Bilgi Teknolojileri ve E-Ticaret（bayiden.com.tr；法律后缀 / MERSİS 未取；母体 12 Volt Elektronik；ETBİS 命中的 BAYDEN TEKNOLOJİ LTD. ŞTİ. İstanbul 为同名他户）', 'founded': '未取（站点新）' + TAG, 'staff': '微型（未取）', 'hq': 'Gevhernesibe Mah. Anıt Cad. No 5, Kocasinan / Kayseri 38280',
                          'other': '第 99 批：Kayseri 微型电子 / 安防电商 → 一页纸即止（STC-028GP $28 / STC-228GP $33）；收件 info@；不加厚' + TAG}},
    'SB-1051': {'add_kp': {'name': 'Kadir Ferahlı', 'role': 'Yönetim Kurulu Başkanı（董事长；2024-09 50 周年致辞）= 拍板人；收件走 IoT / 电子产品线产品经理（technicalsupport@klemsan.com.tr 为唯一公开邮箱起点）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.iyigunler.net/klemsan-sektordeki-50nci-yasini-kutladi/355283/'},
                'facts': {'legal_name': 'KLEMSAN Elektrik Elektronik Sanayi ve Ticaret A.Ş.（İzmir；Bloomberg 0996344D:TI；SASAD / ENOSAD 会员）', 'founded': '1974-07-20' + TAG, 'staff': '201–500 人（450 人晚宴）', 'hq': 'Kızılüzüm Mah. Kemalpaşa Kızılüzüm Cad. No 15, 35730 Kemalpaşa / İzmir（+ Pınarbaşı 第二工厂）',
                          'other': '第 99 批：**第 99 批 TR 最大户**：50 年接线端子 / 电气连接件制造商，自有 IoT / 电子线，表内「从 VOLKTEK 买工业交换机」= 现成 OEM 30% 需求（Klemsan 标导轨工业交换机）→ **OEM 30% 首选，B BIG，升 A 候选，加厚**（STI-054GP / STI-144GP / STI-288DGGPM 对标 VOLKTEK 同规格 + 3 年保修 + MOQ 1；不点名 VOLKTEK）；工厂总经理 A. Savaş Yalçın' + TAG}},
    'SB-1056': {'add_kp': {'name': 'Habil Sekibağ', 'role': 'Managing Director（创办人；ContactOut / Apollo）= 收件人；Deputy MD Erdem Öztürk' + TAG, 'email': '', 'phone': '', 'source': 'https://www.mikrodev.com/about/'},
                'facts': {'legal_name': 'Mikrodev Bilişim Yazılım Elektronik San. ve Tic. Ltd. Şti.（İstanbul 注册；Gebze TÜBİTAK 自贸区生产；UK 分支 Mikrodev Ltd 自称总部；南非分支）', 'founded': '2006（2011 起商业化生产；MİKRODEV 商标 2011）' + TAG, 'staff': '16–36 人（20 工程师 + 16 技术员）', 'hq': 'TÜBİTAK MAM Teknoloji Serbest Bölgesi, Gebze / Kocaeli',
                          'other': '第 99 批：本土 PLC / RTU / 网关 / 工业路由器自产（准同行）但不做交换机 → 贴标 small：MIKRODEV 标 STI-054GP / STI-144GP 补齐柜内组网，走其 14 家土耳其经销商；一页纸' + TAG}},
    'SB-737': {'kp_name': 'Uğur İmre', 'role': 'ISAF 名录联系人本人（无公司主体；官方登记 1 次未命中 → 未坐实）' + TAG,
               'facts': {'legal_name': '未坐实（无公司名 / 无域名；ISAF 展会名录个人）', 'founded': '未取' + TAG, 'staff': '未取', 'hq': '未取',
                         'other': '第 99 批：**未坐实**；保留 B（有打开）；只随群发带 HRUI 价目，不单独写信、不加厚' + TAG}},
    'SB-427': {'kp_match': 'info@longlinenetwork.com', 'role': '公域（Longline 集团；收件人点名「ürün müdürü / satın alma」；2020-10 迁入自有 Longline Plaza）' + TAG,
               'facts': {'legal_name': 'Longline Bilişim Teknolojileri Ltd. Şti.（İstanbul Bayrampaşa；注册资本 50M–500M TL 档；自有品牌 Longline）', 'founded': '2000' + TAG, 'staff': '11–50 人（22）', 'hq': 'Kartaltepe Mah. Hakan Sok. Longline Plaza No 18, 34040 Bayrampaşa / İstanbul（+ 罗马尼亚 / 中国 / 迪拜 / 美国办事处）',
                         'other': '第 99 批：自有品牌（SFP / 内存 / SSD / 网卡 / MC / 跳线）+ 800 经销伙伴 + 中国办事处 → **贴标 OEM 30% 目标：Longline 标 L2+ 管理型 / PoE 交换机补齐产品线；B BIG，升 A 候选，加厚**（STC-228GP / STC-2224GP / STI-0240GE / STH-2C24XF-HSI；与其自有标 SFP 配套）；不提其中国办事处' + TAG}},
    'SB-465': {'kp_match': 'deniz@kozaguvenlik.com.tr', 'role': '研究档联系人（职务未核）= 收件人，抄 info@ 点名「satın alma」' + TAG,
               'facts': {'legal_name': 'Koza Güvenlik Elektronik Sistemleri San. Tic. Ltd. Şti.（İstanbul；Greentech Güvenlik 集团成员；Teletek 土耳其官方分销商）', 'founded': '2005' + TAG, 'staff': '11–50 人', 'hq': 'Perpa Ticaret Merkezi A Blok Kat 8 No 808-810-940, 34384 Şişli / İstanbul（+ Koza Plaza, Arel Aralığı No 8, Okmeydanı）',
                         'other': '第 99 批：Teletek（BG）报警 / 消防独家 + Kodicom + Dahua 二级分销 + 自有注册品牌 + 全国经销网 → 分销 20% 为主、贴标 small 为辅（STC-028GP / STC-228GP / STC-2216GP）；一页纸' + TAG}},
    # ---------- DE ----------
    'SB-1015': {'kp_match': 'info@br-network.de', 'role': '公域（点名 GF Barthel Robitzsch —— 网站内容负责人；另一 GF Wilfried van den Beek；2024 新任 Prokura Gerome Ramakers / Kyra Kubina）' + TAG,
                'facts': {'legal_name': 'BR Network Solutions GmbH（Amtsgericht Kleve HRB 3402；USt-ID DE 813 479 263；股东 van den Beek 50% / Robitzsch 50%）', 'founded': '2002-05-28（2004-02 迁址登记）' + TAG, 'staff': '10–19 人；股本 330k €', 'hq': 'Emmericher Straße 261, 47533 Kleve',
                          'other': '第 99 批：老板直营专业批发（WZ 46520）+ 自有标「BR Network」+ 3M Volition 主分销 + 已卖 KTI / MICROSENS 交换机 → 分销 20% 为主、贴标 small 为辅（STC-028GP / STC-228GP / STC-2224GP 对标 KTI）；一页纸' + TAG}},
    'SB-1039': {'kp_match': 'vertrieb@ico.de', 'role': '公域（点名「Produktmanagement Netzwerk / Einkauf」，抄 GF Oliver Schröder；另一 GF Alexander Solzer）' + TAG,
                'facts': {'legal_name': 'ICO Innovative Computer GmbH（Amtsgericht Montabaur HRB 20217；资本 €500,000；USt-ID DE 246038247；曾用壳名 DRJ GmbH）', 'founded': '1982（Klaus Jeschke 个体）→ 1991 GmbH → 2005/2006 现登记' + TAG, 'staff': '120 人；≈€20M（2022/23）；2023 资产 €5.03M', 'hq': 'Zuckmayerstraße 15, 65582 Diez',
                          'other': '第 99 批：**第 99 批 DE 最大户**：自称「Distributor und Importeur」+ 20,000 客户（60% 经销商 / 40% 工业）+ 自有工业 PC / 服务器装配 + ISO 9001 → **分销 20% 首选，B BIG，升 A 候选，加厚**（工业线 STI-054GP / STI-288DGGPM；Systemhaus 线 STC-228GP / STC-2224GP / STI-0240GE）' + TAG}},
    'SB-1080': {'kp_match': 'markus.brenner@', 'role': 'Einzelprokura（2005-11-18 起单独代理权 Prokurist；openregister）= **坐实 = 收件人**；GF Hubert Engelhardt（70 岁，单一股东）；Prokura Stefanie Engelhardt（2012）' + TAG,
                'facts': {'legal_name': 'SPHINX Computer Vertriebs-GmbH（Amtsgericht Mannheim HRB 431843；股本 €155,000；USt-ID DE 113585714）', 'founded': '1989-04-25' + TAG, 'staff': '小型（股本 €155k；人数未取）', 'hq': 'Heinrich-Lanz-Straße 14, 69514 Laudenbach',
                          'other': '第 99 批：MOXA / Advantech / Perle 等工业通信正规分销商 → 品牌忠诚高 → 分销 20% 低概率，一页纸「预算线 / 第二来源」（STI-054GP / STI-144GP / STI-288DGGPM；不点名 MOXA）；GF 70 岁传承期' + TAG}},
    'SB-281': {'kp_match': 'javier.ferre@', 'name': 'Javier Ferre Torres', 'role': 'Prokura + Produkt Manager Parkleitsystem（companyhouse.de / LinkedIn）= **坐实 = 选型人 = 收件人**；GF 兼股东 Dr. Roland Kraus（前 Siemens 全球停车业务负责人）' + TAG,
               'facts': {'legal_name': 'multiGuide GmbH（Amtsgericht München HRB 194714；资本 €26,596；USt-ID DE279778200）', 'founded': '2011-10-17' + TAG, 'staff': '11–50 人', 'hq': 'Linienstraße 1, 82041 Oberhaching',
                         'other': '第 99 批：停车引导系统开发 / 制造 / 安装商 → 集成商 25%（地下车库传感器 / 摄像机 / 显示屏 PoE：STI-054GP / STI-144GP 导轨 + STC-2224GP 机房）；一页纸' + TAG}},
    # ---------- GB ----------
    'SB-1094': {'facts': {'legal_name': 'Leading Light Technologies Ltd（Reg No. 06496207；品牌 L2tek；网店 VideoBits）', 'founded': '2008（号段推定；CH 未开）' + TAG, 'staff': '<25 人；<$5M', 'hq': 'Tower House, Lucy Tower Street, Lincoln LN1 1XW（注册处）',
                          'other': '第 99 批：广播 / ProAV 光模块 / 线缆小批量电商（Saga 不做光模块）→ 只剩 AV-over-IP PoE 交换机（IGMP）切口：STC-2224GP / STC-424XGGPM-280W → 分销 20% small，一页纸' + TAG}},
    'SB-1099': {'add_kp': {'name': 'Timothy Mak', 'role': 'Director / PSC（75–100%；1980-01 生）= 唯一决策人' + TAG, 'email': '', 'phone': '', 'source': CH + '12495813'},
                'facts': {'legal_name': 'ZXTECH LTD（Companies House 12495813；Micro；资本 £1；FCA 940104）', 'founded': '2020-03-03' + TAG, 'staff': '微型（1 董事；营业额 <£1M）', 'hq': 'Berkeley Square House, Berkeley Square, Mayfair, London W1J 6BD（虚拟办公室）',
                          'other': '第 99 批：**定性 = 不是同行**，消费级 CCTV 自有标卖家（PoE NVR 套装，配套 PoE 小交换机随套装华南采购）→ 守界（消费级）+ 微型 → 一页纸即止（STC-028GP 贴标 MOQ）；不加厚' + TAG}},
    'SB-1019': [{'kp_match': 'matt.craig@', 'role': '研究档联系人（职务未核；CH 无此人）= 保留抄送' + TAG},
                {'add_kp': {'name': 'Tim Dickens', 'role': 'Director of Brands（ContactOut）= **主收件人**（自有品牌 Connectix 的产品线负责人）' + TAG, 'email': '', 'phone': '', 'source': 'https://contactout.com/company/connectix-cabling-systems-1071899'}},
                {'add_kp': {'name': 'Timothy Roland Brown', 'role': 'Marketing & Development Director（董事，1998-12-01 起）= 抄送；MD / PSC Kevin Arthur Hancock（创办人）' + TAG, 'email': '', 'phone': '', 'source': CH + '02814569/officers'},
                 'facts': {'legal_name': 'Connectix Limited（Companies House 02814569；品牌 Connectix Cabling Systems；Hancock 家族控股）', 'founded': '1993-05-04' + TAG, 'staff': '137 人；营业额 £46.32M', 'hq': '500 Avenue West, Skyline 120, Great Notley, Braintree, Essex CM77 7AA',
                           'other': '第 99 批：**第 99 批 GB 最大户、OEM 30% 首选**：自有品牌含 Networking Equipment；2026-03-16 MD 公开宣布关闭 4 家英国工厂、生产外移印度 / 中国 = 正在找亚洲供应商 → Connectix 标 PoE / 管理型交换机（STC-228GP / STC-2224GP / STI-0240GE / STC-424XGGPM-280W + STI 恶劣环境线）；**B BIG，升 A 候选，加厚**；信中不提关厂新闻' + TAG}}],
    'SB-1045': {'kp_name': 'Neil Stratford / Philip Savill', 'role': '研究档销售联系人（CH 无此二人）= 收件人；Director / PSC Michael John Cook（85 岁，2024-10 起唯一股东）' + TAG,
                'facts': {'legal_name': 'ITM Components Limited（Companies House 03129914；小型豁免账目）', 'founded': '1995-11-23（1991 起营业）' + TAG, 'staff': '7 人；营业额 <£6.5M；现金 £672K（−46%）', 'hq': '10 Whittle Road, Ferndown Industrial Estate, Wimborne, Dorset BH21 7RU',
                          'other': '第 99 批：L-Com / NTI / Extron / Aten 小众分销；合伙人 Ian Flemming 2024-10 退出 → 复利低 → 分销 20% small，一页纸（STC-028GP / STC-228GP）；下轮不追' + TAG}},
    # ---------- PL ----------
    'SB-1065': {'add_kp': {'name': 'Arkadiusz Jerzy Matysiak', 'role': 'Prezes Zarządu（兼 P.W. DELTA 业主）= **拍板人 = 收件人**（delta-opti@delta.poznan.pl）；Wiceprezes Monika Małgorzata Matysiak；Członek Zarządu Arkadiusz Tomasz Topolski' + TAG, 'email': 'delta-opti@delta.poznan.pl', 'phone': '', 'source': 'https://rejestr.io/krs/1225221/delta-opti-monika-matysiak'},
                'facts': {'legal_name': 'DELTA-OPTI Monika Matysiak sp. z o.o.（KRS 0001225221；NIP 7792602869；REGON 544106600；原 DELTA-OPTI MATYSIAK sp. k.；关联 P.W. DELTA Arkadiusz Matysiak NIP 779-000-84-58）', 'founded': 'sp. k. 期未取；2026-03-02 改制 sp. z o.o.' + TAG, 'staff': '小型（未取）；资本 100k zł', 'hq': 'ul. Graniczna 10, 60-713 Poznań',
                          'other': '第 99 批：家族 CCTV / 天线 / WLAN 批发 + 自产桅杆支架 + 多语种出口网店 shopdelta.eu → **分销 20%，B BIG 候选，加厚一次**（STC-028GP / STC-228GP / STC-2216GP + STI-054GP 户外）；2026-03 改制 = 扩张节点' + TAG}},
    'SB-1095': {'facts': {'legal_name': '未坐实（vidom.pl 运营主体未取；检索命中的 VIDOM Systemy Zabezpieczeń sp. z o.o. KRS 0001021691 Mińsk Mazowiecki = vidom.com.pl 同名他户，不采）', 'founded': '未取' + TAG, 'staff': '未取（疑微型网店）', 'hq': '未取',
                          'other': '第 99 批：**未坐实 + 同名陷阱**；LED / Grenton 智能家居网店，PoE 只是配套且表内「质量一般」→ 一页纸即止（STC-028GP）；不加厚' + TAG}},
    'SB-1058': [{'kp_match': 'damian.lis@', 'role': '具名销售（商品页侧栏）= 主收件人' + TAG},
                {'kp_match': 'slawek.janusch@', 'role': '具名销售 = 抄送' + TAG,
                 'facts': {'legal_name': 'PHU Multiproject（Multiproject Hurtownia Teletechniczna；NIP 5842509422；法律形式未核，推定个体 PHU；同名 Multiprojekt sp. z o.o. 多家为他户）', 'founded': '未取' + TAG, 'staff': '微型 / 小型（两位具名销售）', 'hq': 'Gdańsk（门牌未取）',
                           'other': '第 99 批：部分坐实（NIP 已核）；PLANET IGS-624HPT / GSW-4800 在售但缺货 = 替代切口 → 分销 20% small：STI-288DGGPM $137 对标 IGS-624HPT（1 350 zł 净）；一页纸' + TAG}}],
    'SB-1025': {'add_kp': {'name': 'Marek Andrzej Miękina', 'role': 'Prezes Zarządu（普通合伙人 ELFON BIS Sp. z o.o.，2015-10-29 起）= 实控人 = 收件人（抄 biuro@elfon.com.pl）' + TAG, 'email': 'biuro@elfon.com.pl', 'phone': '', 'source': 'https://rejestr.io/krs/700362/elfon-miekina'},
                'facts': {'legal_name': 'ELFON Miękina Sp. K.（原 ELFON BIS Sp. z o.o. Sp. K.；KRS 0000700362；NIP 6792955142；REGON 120559355；GP ELFON BIS Sp. z o.o. KRS 0000583435）', 'founded': '2007-10-12（开业）/ 2017-10-23（现登记）' + TAG, 'staff': '小型（未取；自有生产 + 区域销售）', 'hq': 'ul. Półłanki 27A, 30-740 Kraków（2026-02-01 起；旧址 Ruciana 3）',
                          'other': '第 99 批：波兰楼宇对讲 / IP-SIP 可视对讲制造商 → IP 对讲必配 PoE → 贴标 small（OEM 30%）/ 配套 25%：ELFON 标 STC-028GP / STI-054GP 随其 IP 系统成套；一页纸 + 配套图' + TAG}},
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
