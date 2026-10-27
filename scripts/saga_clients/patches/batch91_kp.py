#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 91 批（T29-U73，公司底数第九轮 · B 档「筛≥2」尾盘 20 户 / 11 国 + 6 户未命中）：把官方 / 准官方登记核出来的「老板 / 董事 / 股权 / 规模 / 财务 / 同行与守界判定」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=91 行）。
结构同 batch90_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 91 批 官方登记核实 2026-10-27）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- GB / PL / AU ----------
    'SB-231': {'add_kp': {'name': 'Nathan James Parys', 'role': 'Director（唯一在任，2025-04-02 起；Companies House 10953609）= **老板 = 联系人**；**公司 2025-04 换手**：中国籍创始董事 Jie Kennett 同日辞任 → 供应链重建期 = 进门时机；分销 20% / OEM 30% 二选一，UKCA + CE' + TAG, 'email': '', 'phone': '', 'source': CH + '10953609/officers'},
               'facts': {'legal_name': 'ADVANCE TECHNOLOGY SOLUTIONS LTD（Companies House 10953609；VAT GB281168595；**同名陷阱：Advance Technology Limited 03391710 Liverpool 非本户**）', 'founded': '2017-09-08' + TAG, 'staff': '微型 / 小型（估 2–10 人）；SIC 26110 电子元件制造' + TAG, 'size': '微型 / 小型' + TAG, 'hq': 'Felton House, Gemig Street, St Asaph LL17 0RY（注册地 Unit 32 Llys Edmund Prys, St Asaph Business Park LL17 0JA，威尔士）' + TAG, 'other': '账目至 2025-09-30 已报，下期 2027-06-30 到期；PSC 页下轮补' + TAG}},
    'SB-574': {'facts': {'legal_name': 'IMPAKT S.A.（Lanberg 品牌权人；KRS 0000585900，NIP 7831720485，REGON 360441981，**股本 60,761,002 zł**）', 'founded': '品牌 Lanberg 2015；Impakt S.A. 2015-10 登记（集团更早）' + TAG, 'staff': 'Lanberg 品牌页 51–200；Impakt 集团数百人' + TAG, 'size': '大型（波兰 IT 配件自有品牌集团：Lanberg / Natec / Genesis）' + TAG, 'hq': 'ul. Stanisława Lema 16, 62-050 Mosina（波兹南南）' + TAG, 'other': '**lanberg.pl 不是小店 —— Lanberg 产品线本就含交换机 = OEM 品牌商首选 → 写 Lanberg product manager（Impakt 采购）OEM 30%**；zarząd 待 rejestr.io 补' + TAG}},
    'SB-714': {'add_kp': {'name': 'Daniel Peter Willgoose', 'role': '业主 / 主事人（D&B Key Principal；同邮编自管养老金 NET SECURITY WHOLESALERS SUPER FUND ABN 27 140 358 544 = 业主自营）= **老板 = 联系人** → 分销 20% CCTV 配套 PoE + 工业 DIN，RCM 他们' + TAG, 'email': '', 'phone': '', 'source': 'https://abr.business.gov.au/ABN/View?abn=94083730250'},
               'facts': {'legal_name': 'NET SECURITY WHOLESALERS PTY LTD（ABN 94 083 730 250；DBA NetDigital Surveillance）', 'founded': '≈1998（ACN 083 段）' + TAG, 'staff': '小型（估 5–15 人）' + TAG, 'size': '小型（安防 / CCTV 批发）' + TAG, 'hq': '4 Commercial Street, Marleston, SA 5033（阿德莱德）' + TAG}},
    # ---------- TR ----------
    'SB-738': {'kp_name': 'Uğur Şimşek', 'role': 'Manager / 业主（D&B Key Principal；TRNOG 成员）= **老板 = 联系人**（WhatsApp 已加）—— 公司 = **Çerkezköy 工业区 ISP（2016 起，11–50 人）→ 要的是接入交换机 + 给无线 CPE 供电的 PoE，不是 CCTV 套装**：STI-0240GE $130 / STC-110XGE $65 / STI-154GP，分销 20%' + TAG,
               'facts': {'legal_name': 'NETMAX TELEKOMÜNİKASYON İLETİŞİM HİZMETLERİ TİCARET LİMİTED ŞİRKETİ（Mersis 未命中）', 'founded': '2016（LinkedIn）' + TAG, 'staff': '11–50（LinkedIn）' + TAG, 'size': '小型 ISP' + TAG, 'hq': 'Gazi Mustafa Kemal Paşa Mah. Öztırak Cad. No:141, 59500 Çerkezköy / Tekirdağ' + TAG}},
    'SB-723': {'kp_name': 'İbrahim（姓氏待核）', 'role': '推定业主（ISAF 名片；仅 WhatsApp）—— 公司法定名含「电气 / 机械」= **Gebze 工业区安防 + 电气小集成商（工厂弱电承包）** → 工业 DIN PoE + 8/16 口 PoE，分销 20%，100% 预付' + TAG,
               'facts': {'legal_name': 'BİLGEN ELEKTRONİK GÜVENLİK SİSTEMLERİ TEKNOLOJİLERİ YAZILIM ELEKTRİK MAKİNA SAN. VE TİC. LTD. ŞTİ.', 'staff': '微型 / 小型（估 3–10 人）' + TAG, 'size': '微型 / 小型' + TAG, 'hq': 'Osman Yılmaz Mah. 607/1 Sok. No:21, 41400 Gebze / Kocaeli（+90 262 643 61 18）' + TAG}},
    'SB-565': {'facts': {'legal_name': 'Marmaris Bilişim（Marmaris Wifi；推定 şahıs 个体，VKN 未取）', 'staff': '微型（1–5 人）' + TAG, 'size': '微型（电脑 / 网络零售 + 本地 Wi-Fi 接入服务）' + TAG, 'hq': 'Sarıana Mah. Mustafa Kemal Paşa Cad. No:19, Marmaris / Muğla（info@marmarisbilisim.com.tr）' + TAG, 'other': '度假区酒店 / 商铺 Wi-Fi 场景 → 土耳其语 WhatsApp 一页价，一封无回即停；更划算是让他从 TR 分销户拿货' + TAG}},
    # ---------- GE ----------
    'SB-375': {'kp_name': 'George Jaliashvili', 'role': 'CEO / Partner（US SAM 镜像 E-Business / Government POC 同名 = 核实）= **老板 = 联系人**；公司 2020-07 → 2022-07 曾注册美国 SAM（UEI J9LKEG5JR7D6 / CAGE SJFH4；NAICS 541512 + 423690 电子设备批发）= 做过美援 / 国际招标项目，之后未续' + TAG,
               'facts': {'legal_name': 'DELTA CONSULTING LLC（შპს；Tbilisi；SAM UEI J9LKEG5JR7D6 / CAGE SJFH4，Expired 2022-07-14；**同名陷阱：Delta Consulting LLC Oxford MS 无关**）', 'founded': '2014-01-08（SAM business start）' + TAG, 'staff': '小型（估 10–30 人）' + TAG, 'size': '小型 IT 集成商' + TAG, 'hq': '72 O. Oniashvili Str., Tbilisi 0160, Georgia' + TAG, 'other': '集成 25%，管理型 24 口 + 10G 上联（招标要 L2+/L3 规格书 → Marvell 线英文规格）；**信里不提 SAM / 美援**' + TAG}},
    # ---------- AE ----------
    'SB-011': {'kp_match': 'shaji@greentechme.net', 'role': 'WhatsApp 下单人（已成交 2 单；推定业主 / 采购主管）—— 公司法定名 **Green Technical LLC**（Ajman + Dubai 信箱），官网自有型号 PoE 配件（NEPX101/201 延长器、NEPR-111 中继、PoE 媒转）= **已在贴牌卖配件 → 交换机也可贴：OEM 30% + 按 ㉕ 用上次成交价续**' + TAG,
               'facts': {'legal_name': 'Green Technical LLC（greentechme.net；Ajman DED 执照不公开；**同名陷阱：greentech.ae / greentech-ae.com / Greentech Middle East 巴林 均非本户**）', 'staff': '微型 / 小型（估 3–10 人）' + TAG, 'size': '微型 / 小型（网络 + 安防安装供货 + 自有型号 PoE 配件）' + TAG, 'hq': 'P.O. Box 22511, Ajman；P.O. Box 238376, Dubai' + TAG}},
    'SB-053': [{'kp_match': 'saurabh@onnettechnologies.com', 'name': 'Saurabh Pachchigar', 'role': '设计 / 制造负责人（LinkedIn；Pachchigar 家族 = 推定业主之一）= **技术拍板 = 写他**：OEM 30% OTAI 标工业 PoE（STI-054GP / STI-154GP / 288DGGPM-2BT 配其高功率杆件）' + TAG},
               {'kp_match': 'piyush@onnettechnologies.com', 'role': 'Director – Business Development（LinkedIn 2026；研究档原记 Founder / MD 应为误读；PMP，31 年经验）= 商务联系人（抄送）' + TAG},
               {'add_kp': {'name': 'Dipali Pachchigar', 'role': 'Director（contactout / RocketReach）= 法定代表 / 家族' + TAG, 'email': '', 'phone': '', 'source': 'https://ae.linkedin.com/company/otaillc'},
                'facts': {'legal_name': 'ONNET TECHNOLOGIES & INNOVATIONS LLC（OTAI；Ajman 执照号未取）', 'founded': '2012' + TAG, 'staff': '6–50（contactout 6 / LinkedIn 11–50）；营收估 $1–10M（量级）' + TAG, 'size': '小型制造商（高功率 PoE 供电 / 无线 / 智慧杆 / 机箱；TDRA 核准 + FCC ID）= OEM 品牌商' + TAG, 'hq': 'Shed 1 & 2, Street 80-81 Junction, Ajman Industrial Area 1（PO Box 23170；+971 6 748 0204）' + TAG}}],
    # ---------- IN ----------
    'SB-006': [{'add_kp': {'name': 'Pramendra Singh Chaudhary', 'role': 'Director / CEO（DIN 02074072，2019-04-18 起；注册邮箱 chaudhary@unitedcontrolengg.com）= **老板 = 联系人** → 工业 DIN 交换机（STI-054GP / STI-154GP / STI-110GE 宽压）集成 25%，BIS 他们' + TAG, 'email': 'chaudhary@unitedcontrolengg.com', 'phone': '', 'source': 'https://www.zaubacorp.com/UNITED-CONTROL-ENGINEERS-INDIA-PRIVATE-LIMITED-U17302UP2019PTC115938'},
                'facts': {'legal_name': 'UNITED CONTROL ENGINEERS INDIA PRIVATE LIMITED（CIN U17302UP2019PTC115938；GST 09AACCU4195M1ZP）', 'founded': '2019-04-18（业务 2001 起，先为合伙）' + TAG, 'staff': '26–50 人；自报营业额 ₹25–100 cr（≈$3–12M）' + TAG, 'size': '中小型（工业自动化 / 低压电器分销 + 控制柜装配厂；Delta / ABB / Schneider 渠道）' + TAG, 'hq': 'Plot No. 98, Toy City, Ecotech-III, Greater Noida 201306（注册地 218 Udyog Kendra Extn-1）' + TAG}},
               {'add_kp': {'name': 'Sumit Agrawal', 'role': 'Director（DIN 02074121，2019-04-18 起）= 合伙人（抄送）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.tofler.in/united-control-engineers-india-private-limited/company/U17302UP2019PTC115938'}}],
    'SB-243': [{'kp_match': 'shantanu.kumar@hfcl.com', 'role': '有回复（采购 / 产品线人员，职务待核）—— 公司 = **HFCL Ltd 上市光缆 + 电信设备商（FY26 营收 ₹4,949 cr；自有 IO 品牌交换机 / AP = 同行；国防 + 铁路 = 守界）→ 判定不追；仅在其问 ODM / 白牌时报 CENTEC ≥35% / Marvell L3 ≥25%，否则 when=不动**' + TAG},
               {'add_kp': {'name': 'Mahendra Nahata', 'role': '发起人 / Managing Director（上市公司；不直接联系）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.thecompanycheck.com/company/hfcl-limited/L64200HP1987PLC007466'},
                'facts': {'legal_name': 'HFCL LIMITED（原 Himachal Futuristic Communications Ltd；CIN L64200HP1987PLC007466；NSE/BSE: HFCL）', 'founded': '1987' + TAG, 'staff': '2,336 人；FY25 合并营收 ₹4,065 cr、EBITDA ₹507 cr；FY26 ₹4,949 cr；Q2 FY27 单季 ₹2,542 cr / 净利 ₹394 cr 创纪录' + TAG, 'size': '大型上市（电信 96% / 国防 2% / 铁路 2%）' + TAG, 'hq': '8 Commercial Complex, Masjid Moth, Greater Kailash-II, New Delhi 110048（运营 Gurugram）' + TAG}}],
    'SB-827': [{'kp_match': 'pankaj.sodhi@goip.in', 'role': 'CEO（2026-04 起；职业经理人 —— **拍板在 Mittal 家族：Anil / Manav Mittal 董事**）= 写他并请转采购决策人：OEM 30% GoIP 标 PoE 8/16/24 + 2.5G，BIS 他们，SKD / 整机两档' + TAG},
               {'add_kp': {'name': 'Anil Mittal', 'role': 'Director（DIN 00117877，2004-09-20 起）= 实控家族长；姊妹公司 GOIP GLOBAL SOLUTIONS PVT LTD（CIN U72900DL2008PTC173861）同董事' + TAG, 'email': '', 'phone': '', 'source': 'https://www.zaubacorp.com/company/GO-IP-GLOBAL-SERVICES-PRIVATE-LIMITED/U74899DL1994PTC061633'}},
               {'add_kp': {'name': 'Manav Mittal', 'role': 'Director（DIN 08586626，2023-05-02 起）= 二代（抄送候选）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.zaubacorp.com/company/GO-IP-GLOBAL-SERVICES-PRIVATE-LIMITED/U74899DL1994PTC061633'},
                'facts': {'legal_name': 'GO IP GLOBAL SERVICES PRIVATE LIMITED（CIN U74899DL1994PTC061633；实缴 ₹51 lakh）', 'founded': '1994-09-20' + TAG, 'staff': '中小型（估 50–150 人）' + TAG, 'size': '中小型（IP 电话 / 网络产品自有品牌 GoIP + 印度组装 + 分销）= OEM 品牌商' + TAG, 'hq': 'Noida Sector 63, UP（ROC Delhi）' + TAG}}],
    'SB-692': [{'kp_match': 'harish@andatelecom.com', 'role': 'Director（DIN 01054370，2004-12-13 起；与 Neelam Gupta 夫妻档）= **老板 = 联系人** → OEM 30% Anda 标 PoE 8/16/24（我方不供媒转 / ONU），MOQ 20 台 / 型号；**信里不提 ONV / AOA**' + TAG},
               {'add_kp': {'name': 'Neelam Gupta', 'role': 'Director（DIN 02122908，2004-12-13 起）= 配偶合伙' + TAG, 'email': '', 'phone': '', 'source': 'https://www.zaubacorp.com/company/ANDA-TELECOM-PRIVATE-LIMITED/U64202DL2004PTC131212'},
                'facts': {'legal_name': 'ANDA TELECOM PRIVATE LIMITED（CIN U64202DL2004PTC131212；实缴 ₹1 lakh）', 'founded': '2004-12-13' + TAG, 'staff': '1–10 人（EMIS）；FY2024 营收 ₹12.81 cr（≈$1.5M，−23%）、FY2025 +22%' + TAG, 'size': '小型（电信 / 光纤产品自有品牌 + Noida 组装）= OEM 品牌商' + TAG, 'hq': 'E-36 Amar Colony, Lajpat Nagar-IV, New Delhi 110024（制造 E-38 Sector 6, Noida 201301）' + TAG}}],
    'SB-189': [{'kp_match': 'varun@vintronsmartvision.com', 'role': 'Director & CEO（Vintron Smartvision Pvt Ltd = CCTV 运营体；曾任上市体 Vintron Informatics Ltd WTD & CEO 2015-06 → 2019-06）= **二代老板 = 联系人** → OEM 30% Vintron 标 PoE 4/8/16/24 配其 NVR 套装，BIS 他们；先 2 台付费样机' + TAG},
               {'add_kp': {'name': 'Raj Kumar Gupta', 'role': '上市关联体董事长（家族长；上市体 2025-12 更名 Reganto Enterprises Ltd 并转向建筑 / 航空 = 安防业务已沉到私营体）—— 不联系' + TAG, 'email': '', 'phone': '', 'source': 'https://www.marketscreener.com/quote/stock/VINTRON-INFORMATICS-LIMIT-20704747/'},
                'facts': {'legal_name': 'VINTRON SMARTVISION PVT. LTD.（CIN 未取；关联上市体 Vintron Informatics Ltd → Reganto Enterprises Ltd，BSE 517393）', 'founded': '未取（上市体 1991）' + TAG, 'staff': 'CCTV 运营体估 50–200 人；上市关联体 FY25 营收 ₹623 cr（+258%）、净利 ₹47.9 cr（含贸易 / 新业务）' + TAG, 'size': '中型（CCTV / DVR 自有品牌制造）= OEM 品牌商' + TAG, 'hq': 'New Delhi' + TAG, 'other': '**信里不提上市壳更名 / 董事辞任**' + TAG}}],
    # ---------- PK ----------
    'SB-013': [{'kp_match': 'asif@synchcom.com.pk', 'role': '销售负责人（Facebook 公开）= 联系人；拍板 = Senior MD Muhammad Babar —— 公司 **自己替 LigoWave / Dinstar 办过 PTA 型号核准（2016、2017）= 有进口 + 认证经验** → 分销 20% 24 口管理型 + 室外 PoE，PTA 他们，100% 预付或 LC' + TAG},
               {'add_kp': {'name': 'Muhammad Babar', 'role': 'Senior Managing Director（RocketReach）= 拍板人（抄送）' + TAG, 'email': '', 'phone': '', 'source': 'https://synchcom.com.pk/about-us/'}},
               {'add_kp': {'name': 'Muhammad Mehmood', 'role': 'Director（2001 起；兼 Sina Institute of Networks 创始人）' + TAG, 'email': '', 'phone': '', 'source': 'https://synchcom.com.pk/about-us/'},
                'facts': {'legal_name': 'SYNCHCOM (PVT.) LIMITED（SECP 注册号未取）', 'founded': '2005-02（官网；RocketReach 称 2000）' + TAG, 'staff': '小型（估 10–30 人）' + TAG, 'size': '小型（IT / 电信集成 + 分销：LigoWave 巴基斯坦分销、Dinstar、MSAN / GEPON）' + TAG, 'hq': '693 Rehman Baba Road, Sector I-8/4, Islamabad 44000（+92 51 486 4925）' + TAG}}],
    'SB-450': [{'add_kp': {'name': 'Muhammad Farooq Zaheer', 'role': 'CEO = 老板 —— 公司 = **Cisco 巴基斯坦「Partner of the Year 2026」+ Fortinet 伙伴（50–100 人）→ 判定：只在银行 / 政府标里要「非 Cisco 接入层」时有机会；一封抄 Rehan Shaikh，无回即停**' + TAG, 'email': '', 'phone': '', 'source': 'https://comtech.net.pk/'},
                'facts': {'legal_name': 'COMTECH ASSOCIATES (PVT.) LTD（SECP 注册号未取）', 'founded': '2010（LinkedIn）/ 2017（Clutch）' + TAG, 'staff': '50–100 人（LinkedIn 11–50 / Clutch 50–249）' + TAG, 'size': '中小型（企业网络 / 网络安全 / 数据中心集成；24/7 SOC；客户含海湾）' + TAG, 'hq': 'The Hive 3rd Floor, NASTP, Shahrah-e-Faisal, Karachi（+92 21 3440 4440）' + TAG}},
               {'add_kp': {'name': 'Rehan Shaikh', 'role': 'Co-Founder / Director of Sales = 销售拍板（抄送）；COO Abdul Rehman Zaheer（家族）；Head of Solutions Muhammad Irfan Ghauri（2026-01）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.issuewire.com/comtech-associates-joins-cisco-partner-summit-2026-as-a-cisco-partner-1879935322008449'}}],
    # ---------- SG（既有事实建档，仅补判定） ----------
    'SB-728': {'facts': {'other': '第 91 批：按既有 ACRA 事实建档（UEN 200002876C）；一人工程顾问 + 弱电供货，样品单为 ONU（我方不供 GPON）→ 只回交换机线 8/16 口 PoE + 24 口管理型，集成 25%，100% 预付，一封无回即停' + TAG}},
    'SB-001': {'facts': {'other': '第 91 批：按既有 ACRA 事实建档（UEN 202005761Z）；**老板 = 联系人（Au Wai Choon 本人 30 封来信）；DC / 海缆光网络工程商正做 AI-Ready 数据中心 = CENTEC 敲门砖正主** → STH-2C24XF-HSI $1,500 起 + STC-110XGE $65，集成 25% / CENTEC ≥35% 底线' + TAG}},
    # ---------- GR / AE（Intracom） ----------
    'SB-924': [{'kp_match': 'rgrassi@intracom-telecom.com', 'role': 'Procurement Manager（Intracom Telecom 希腊总部）= **正式采购口 = 写他**：集成 25%，24/48 口管理型 + 10G 上联英文规格 + CE/RoHS，随附供应商注册资料（VAT / 银行 / ISO 9001 厂证）；不主动追' + TAG},
               {'kp_match': 'mohammad.yaacoub@intracom-telecom.com', 'role': 'Projects Manager（中东项目；2024-08 / 2024-10 来信）= 抄送' + TAG},
               {'facts': {'legal_name': 'INTRACOM TELECOM（Paiania, Greece）；唯一股东 INTRACOM MIDDLE EAST FZE（Dubai，2015-01 起；瑞士投资人全资）', 'founded': '1977（Intracom Telecom）；FZE 控股 2014–2015' + TAG, 'staff': '1,071（tracxn 2026-05）← 约 1,600（2024-07 官方）= 收缩期' + TAG, 'size': '大型电信系统厂商（无线回传 / FTTx / 智慧城市 / 系统集成）= 同行 + 项目集成双重身份' + TAG, 'hq': '19.7 km Markopoulou Ave., Paiania 19002, Greece（FZE: Dubai）' + TAG, 'other': '**信里不提瑞士投资人 / 裁员**；国别保持 GR' + TAG}}],
    # ---------- ZA ----------
    'SB-987': [{'kp_match': 'anton@throughput.co.za', 'role': 'Technical Support & Sales Manager（IBG 买家指南）= 联系人；老板 = 创始人 Bob Petrie —— 公司 = **Westermo 南部非洲独家分销（2–10 人顾问行）→ 不会替掉独家品牌；仅作交通 / 矿业客户的「非独家配套」价格副线：STI-054GP / STI-154GP 集成 25%，一封无回即停**' + TAG},
               {'add_kp': {'name': 'Bob Petrie', 'role': '创始人（1997）= 老板（Petrie 家族：Brenda Petrie HR）；Gillian Andersson 经理、Mashudu Mudau 分销经理' + TAG, 'email': '', 'phone': '', 'source': 'https://www.throughput.co.za/about-us/profile.html'},
                'facts': {'legal_name': 'THROUGHPUT TECHNOLOGIES (PTY) LTD（CIPC 登记号未取）', 'founded': '1997' + TAG, 'staff': '2–10（LinkedIn）' + TAG, 'size': '微型（工业数据通信分销 + 顾问；Westermo / ProSoft / Secomea / Welotec）' + TAG, 'hq': '42 Thembi Place Office Park, Calderwood Road, Lonehill, Johannesburg' + TAG, 'other': '**信里不提 Westermo / Welotec 收购**' + TAG}}],
    # ---------- 未命中 ----------
    'SB-575': {'facts': {'other': '第 91 批检索未命中（marbim.com.tr：1 次检索仅 Merbim / Narbim / Marmara Bilişim 等近名，无法定名 / VKN）→ 不写回登记；仅 WhatsApp 线' + TAG}},
    'SB-718': {'facts': {'other': '第 91 批检索未命中（teksarf.com / Düzgün Toptan：1 次检索仅泛化「toptan kamera」结果）→ 不写回登记；Gmail 个体户，WhatsApp 线' + TAG}},
    'SB-323': {'facts': {'other': '第 91 批检索未命中（「D&N Elektrik Mühendislik」Doğan Tanrıkulu：1 次检索仅同名无关）→ Gmail 个体户，不再检索' + TAG}},
    'SB-224': {'facts': {'other': '第 91 批检索未命中（「Arsenal TV」罗马尼亚：1 次检索无命中，无 CUI 线索）→ 不再检索' + TAG}},
    'SB-731': {'facts': {'other': '第 91 批检索未命中（「JTS Telecom」加拿大：1 次检索仅 JTS Consulting 温哥华 / JTS Services 蒙特利尔 POS 等同名，均无法与 joejts@hotmail.com 对上）→ 不写回' + TAG}},
    'SB-880': {'facts': {'other': '第 91 批检索未命中（netsolutionstore.com.au：1 次检索仅无关 Net Solutions / Netsol；ABR 常用词检索易截断）→ 下轮试 ABR「net solution store」' + TAG}},
}


def apply(d, u):
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if TAG not in (k.get('role') or '') and TAG not in (k.get('title') or ''):
                    key = 'role' if 'role' in k or 'title' not in k else 'title'
                    k[key] = u['role']
                if u.get('name'):
                    k['name'] = u['name']
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


for code, u in UPD.items():
    p = os.path.join(RESEARCH_DIR, f'{code}.json')
    d = json.load(open(p, encoding='utf-8'))
    for one in (u if isinstance(u, list) else [u]):
        apply(d, one)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(code, 'ok')
