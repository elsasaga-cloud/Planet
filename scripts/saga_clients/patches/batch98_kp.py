#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 98 批（T29-U91，公司底数第十六轮 · B 档「自有 logo + 打开」五国 24 户）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=98 行）。
结构同 batch97_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：OEM 30% 首选 3（SB-1119 Nokta upTech / SB-1006 Audio Elektronik / SB-419 AVPro MXnet）；自有标 + 分销双线 2（SB-1054 Luxrite SPRO / SB-1091 Triotronik）；
贴标试探 small 4（SB-232 AIXONTEC / SB-402 SFPTURKEY / SB-833 comtime / SB-713 Netronics）；分销 20% 5（SB-602 Anıl / SB-1002 Amplicon / SB-1003 aplus / SB-1009 Batna / SB-1017 Cellco）；
集成商 25% 2（SB-823 SynchroNet / SB-286 Rima）；同行不动 1（SB-751 EnGenius）；准同行低概率 1（SB-600 T1 Nexus）；一页纸 5（SB-988 / SB-572 / SB-1020 / SB-1067 / SB-1061）；终端用户 1（SB-058）；
国别更正 3（SB-713 加拿大 / SB-1091 奥地利 / SB-1020 阿联酋）；KP 坐实 = 老板 / 董事本人 7（SB-823 VP / SB-402 / SB-232 / SB-1003 / SB-1002 / SB-1017 / SB-833 销售总监）；升 A 候选 5（SB-1119 / SB-1006 / SB-1054 / SB-1091 / SB-1009）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 98 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US / CA ----------
    'SB-823': [{'kp_match': 'tanner@synchronet.net', 'role': 'Vice President（Sales / Business Development，2019 起；官网 About 列第二号人物）= **拍板人之一 = 收件人**' + TAG},
               {'kp_match': 'gbrandt@synchronet.net', 'role': 'Engineer（技术选型）= 抄送' + TAG},
               {'facts': {'legal_name': 'SynchroNet Industries, Inc.（NY DOS ID 2345709；1999-02-12 成立；Active）', 'founded': '1999-02-12（业务 1998）' + TAG, 'staff': '10–49 人；≈$7M', 'hq': '1800 N America Dr, Suite A, West Seneca, NY 14224',
                          'other': '第 98 批：MSP（托管 IT）→ 小项目集成商 25%；CEO Jerry Sheehan（创办人）；表内「Stacking」只有 STH 能做，MSP 客户更可能用 STC-4424GCPM / STC-424XGGPM-280W' + TAG}}],
    'SB-988': {'kp_match': 'sales@infinityhardware.us', 'role': '公域 —— 家庭式微型转售 + BPO 混业（Go Get International LLC dba）：一页纸即止' + TAG,
               'facts': {'legal_name': 'Go Get International LLC（dba Infinity Hardware；EIN 85-3229984；DUNS 011668947；北卡 LLC）', 'founded': '2020' + TAG, 'staff': '2–10 人', 'hq': '3975 Netherstone Ln, High Point, NC 27265（住宅区注册地）/ 812 Parliament St',
                         'other': '第 98 批：SAM 未完成注册；少数族裔所有；兼营 BPO / 线索生成 → 低概率，不加厚' + TAG}},
    'SB-419': {'add_kp': {'name': 'Andy Herron', 'role': 'MXnet Systems Group（商业系统，2024-10 起；BusinessWire）= 收件人（研究档无 KP；邮箱未公开 → 官网表单 / sales@）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.businesswire.com/news/home/20241010489206/en/AVPro-Global-Expands-MXnet-Systems-Group'},
               'facts': {'legal_name': 'AVPro Global Holdings, LLC（南达科他；Inc. 5000 2026 No. 4,514）', 'founded': '2013' + TAG, 'staff': '51–200 人', 'hq': 'Sioux Falls, SD（卫星：St. Petersburg / Seattle / Minneapolis / Bratislava / 深圳）',
                         'other': '第 98 批：2026-01-14 CTO Matt Murray 升 CEO，创办人 Jeff Murray 任 Chairman；自有标 MXnet 交换机 AC-MXNET-SW24E / SW48E / 10G-SW24C → OEM 30% 目标；但有深圳办公室 = 已直采 → 卖点只能是 Marvell L2+ / IGMP 调优 / 3 年保修 / MOQ 1；B BIG' + TAG}},
    'SB-600': {'facts': {'legal_name': 'T1 Nexus（T1Nexus；台湾 / 亚洲光模块厂美国合资；CA 实体名未取；英国子公司 T1Nexus UK Limited）', 'founded': '2018' + TAG, 'staff': '11–50 人；≈$4M', 'hq': '47257 Fremont Blvd, Fremont, CA 94538（旧址 Santa Clara）；Swindon SN5 7EX',
                         'other': '第 98 批：准同行（光模块品牌 + 白盒交换机 JV；姊妹公司 US OPTO）→ 低概率；唯一缝隙 = 其 MC / T1-DS2024G 小交换机凑品类 → 一页纸 STC / STI OEM 贴 T1 标 30%' + TAG}},
    'SB-713': {'country_fix': '加拿大',
               'facts': {'legal_name': 'Netronics Communications Inc.（安大略；母公司 / 品牌 Netronics Technologies；Ontario 公司号未取）', 'founded': '1996' + TAG, 'staff': '11–50 人；≈$3M', 'hq': '600-15 Allstate Parkway, Markham, Ontario L3R 5B4, Canada（+ 迪拜 Oud Metha 办公室）',
                         'other': '第 98 批：**国别更正 US → 加拿大**（美国无地址）；无线电台品牌商、MENA 为主市场 → 贴标试探 small：Netronics 标工业 PoE 4+1 / 4+1 SFP（STI-054GP / STI-144GP）配基站；收件人 info@；不加厚' + TAG}},
    'SB-751': {'facts': {'legal_name': 'EnGenius Technologies, Inc.（加州；Senao Networks, Inc. 台湾 3558 100% 子公司）', 'founded': '1999' + TAG, 'staff': '201–500 人（母公司 2,500）', 'hq': '1580 Scenic Ave, Costa Mesa, CA 92626',
                         'other': '第 98 批：**同行（台湾原厂自有品牌交换机的美国销售公司）→ 不发、剔出群发**；表内「商业 FS 大口、SFP、PoE 配件」是其产品线而非需求' + TAG}},
    # ---------- TR ----------
    'SB-1119': {'facts': {'legal_name': 'Nokta Elektronik ve Bilişim Sistemleri Sanayi ve Ticaret A.Ş.（MERSİS 0631-0730-5210-0020；İstanbul Tic. Sicil 555138-0；原 Ltd. Şti.）', 'founded': '2005-05-26（A.Ş.；业务 2000 / 25 年以上）' + TAG, 'staff': '51–200 人', 'hq': 'Perpa Ticaret Merkezi B Blok Kat 8 No. 906, 34384 Şişli / İstanbul；工厂 Arnavutköy',
                          'other': '第 98 批：**自有注册商标 upTech（TPTO 2008/13951，保护至 2028）下卖 PoE 交换机 / SFP / MC + 自有工厂 + bayi 渠道 + 中东 / 突厥 / 巴尔干出口 → OEM 30% 首选（TR），升 A 候选**；Dahua 分销伙伴；首页主推 PLANET GS-5220 → 对标报 STC-424XGGPM-280W；收件人 nokta@ 点名 upTech ürün müdürü / satın alma' + TAG}},
    'SB-286': {'add_kp': {'name': 'Aycan Türkay', 'role': 'Key Principal（D&B；推定 müdür / 股东）= 收件人（bilgi@rimaelektronik.com 点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.dnb.com/business-directory/company-profiles.rima_elektronik_bilisim_ve_guvenlik_sistemleri_sanayi_dis_ticaret_limited_sirketi.d597b24a4b8d4b314b57e7a2b00e6fc1.html'},
               'facts': {'legal_name': 'Rima Elektronik Bilişim ve Güvenlik Sistemleri San. ve Dış Tic. Ltd. Şti.（MERSİS 0735068165000012；VKN 7350681650；资本 123,456 TL；注册商标 newstream）', 'founded': '2010-07-15（现名；业务 1997 / 2000 起）' + TAG, 'staff': '11–50 人', 'hq': 'İstanbul',
                         'other': '第 98 批：安防集成商为主（校园 / 企业监控设计安装）→ 集成商 25%；网店在售 PLANET PoE → 对标 GS-4210-8P2S 报 STC-228GP、IGS 报 STI-288DGGPM；商标 newstream → 贴标试探 small 一句带过' + TAG}},
    'SB-402': {'kp_match': 'ufuk.goren@sfpturkey.com.tr', 'role': 'Managing Partner（RocketReach / ZoomInfo；前 Cinch Connectivity 土耳其国家经理、Vestel）= **老板本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'SFPTURKEY Elektronik İthalat İhracat Ticaret Ltd. Şti.（MERSİS 未取）', 'founded': '2012（Kreasis 起）' + TAG, 'staff': '微型 / 小型', 'hq': 'Koşuyolu Mah., Kadıköy / İstanbul',
                         'other': '第 98 批：三个「自有品牌」Gigacom / SFPTürkiye / geMaxx 实为进口贴牌 → 贴标试探（OEM 30%）：geMaxx 标 MC / 小 PoE（STI-054GP / STC-028GP）MOQ 1；电商为主 → HRUI 线 + DAP 伊斯坦布尔；光模块不提' + TAG}},
    'SB-572': {'kp_match': 'info@fourline.com.tr', 'role': '业主（Özel Elektronik；姓名未公开）= 收件人 —— 微型卫星 / 天线批发，一页纸即止' + TAG,
               'facts': {'legal_name': 'Özel Elektronik（FOURLINE 品牌 2007；VKN 2360002288 Setbaşı VD；未见公司后缀 → 推定 şahıs işletmesi）', 'founded': '2007（品牌）' + TAG, 'staff': '微型（经销商 = 布尔萨本地 5 家电工铺）', 'hq': 'Şükraniye Mah. Ankara Cad. No 242, Yıldırım / Bursa',
                         'other': '第 98 批：PoE 只是 CCTV 配套 → 低概率，不加厚；若回信只报 HRUI STC-028GP / STC-228GP；有贴标习惯（Fourline 接收机 / 适配器）→ 一句「Fourline 标 4 口 PoE MOQ 1」' + TAG}},
    'SB-602': {'kp_match': 'cumhur@aniltelekom.com', 'role': 'Pazarlama ve Satış Yöneticisi（市场与销售经理；ZoomInfo / ContactOut）= 收件人（销售负责人，非采购 → 信里只问一个渠道问题）' + TAG,
               'facts': {'legal_name': 'Anıl Telekomünikasyon Güvenlik ve Bilişim Sistemleri San. Tic. Ltd. Şti.（官网 © 2025；Perpa 旧名录 Anıl Telekomünikasyon Elektrik Malz. Kablo Paz. San. ve Tic. Ltd. Şti.；2025-02-26 新登记 Merkez Şubesi；MERSİS 未取）', 'founded': '2002' + TAG, 'staff': '11–50 人（Perpa A Blok 三层五铺）', 'hq': 'Perpa Ticaret Merkezi A Blok No 1440-1442-1575-1577-1579, Kat 10-11-12, Şişli / İstanbul',
                         'other': '第 98 批：Dahua / Karel / Yealink / TP-Link / Ruijie / Lande 「Ana Dağıtıcı」总分销 → 分销 20%：对标 TP-Link / Ruijie 入门 PoE 报 HRUI 线（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86）；Dahua 自带 PoE → 只打「非 Dahua 8/16/24 口价格带」' + TAG}},
    'SB-1006': {'facts': {'legal_name': 'Audio Elektronik İthalat İhracat Sanayi ve Ticaret A.Ş.（VKN 1030049698 Anadolu Kurumlar VD；EMIS 1988-09-20 设立；Kompass 旧档 Ltd. Şti.；MERSİS 未取）', 'founded': '1988-09-20（A.Ş.；业务 1977 / 1979 起）' + TAG, 'staff': '100–249 人；≈$67M（第三方）', 'hq': 'Esenkent Mah. Barajyolu Cad. No 26, 34776 Dudullu-Ümraniye / İstanbul（6,000 m² 工厂 = 总部）',
                          'other': '第 98 批：**土耳其首家对讲 / 智能家居制造商，IP 对讲系统需配套 PoE，表内「买的 Hisource 的 PoE」= 已在华南采购贴牌 → 对标 Hisource 报 Audio 标 STC-028GP / STC-228GP / STC-2224GP，MOQ 1，OEM 30% 首选（TR），升 A 候选；B BIG**；董事会未取；收件人 info@ 点名 IP Sistemler ürün müdürü / satın alma müdürü' + TAG}},
    # ---------- DE / AT ----------
    'SB-232': {'kp_match': 'ashkan.ghaznavi@aixontec.com', 'role': 'Geschäftsführer + Gesellschafter（HRB 19851 Aachen；Dipl.-Ing.，*1974；前 Leoni Kerpen / Niedax 销售）= **老板本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'AIXONTEC GmbH（Amtsgericht Aachen HRB 19851；USt-IdNr. DE 301189253；资本 €25,000）', 'founded': '2015-07-21（合同）/ 2015-08-11（登记）；自称 2011 起' + TAG, 'staff': '微型 / 小型（一人 GF）', 'hq': 'Freunder Weg 106, 52068 Aachen',
                         'other': '第 98 批：自有品牌 AIXONTEC（Amazon 卖家）+ 表内「工业 FS 现从国内供应商采购」= 已在华南买工业交换机贴标 → **贴标试探首选 small（OEM 30%）**：STI 工业线贴 AIXONTEC 标，MOQ 1，3 年保修；14 次群发无回复 → 第二次触达换主题不换人' + TAG}},
    'SB-1091': {'country_fix': '奥地利',
                'add_kp': {'name': 'Bernhard Flicker', 'role': 'Prokurist + Vertriebsleiter + Gesellschafter（firmenatlas / Kleine Zeitung 2026-09-30）= 收件人（office@triotronik.com 点名；研究档无 KP）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.firmenatlas.com/firma/287460k'},
                'facts': {'legal_name': 'TRIOTRONIK GmbH（2026-09-16 更名自 TRIOTRONIK Computer und Netzwerktechnik GmbH；FN 287460k LG ZRS Graz；UID ATU63017835；资本 €35,000；TRIOTRONIK Holding GmbH 100%）', 'founded': '2007-02-07' + TAG, 'staff': '中型（2025 年报：资产 €12.4M / 权益 €3.7M / 净利 €3.6M）', 'hq': 'Energiestraße 10, 8160 Weiz（Krottendorf）, Steiermark, Austria',
                          'other': '第 98 批：**国别更正 DE → 奥地利**；MikroTik Master 分销 + PLANET 在线专页 + 自有光纤 / 铜缆组件与天线制造 → 分销 20% + 贴标（TRIOTRONIK 标 PoE OEM 30%）；GF Thomas Thir-Greiter + Peter Hofer-Perner（2021-10 起，三位经营股东）；**B BIG，升 A 候选**' + TAG}},
    'SB-833': {'kp_match': 'jd@comtime-com.de', 'role': 'Vertriebsleiter（Marketing und Vertrieb；PresseBox / wlw，2013 起）= 销售总监本人 = 抄送；主收件人改写新 GF' + TAG,
               'add_kp': {'name': 'Markus Kasten', 'role': 'Geschäftsführer（*1995；HRB 4574 NO Kiel，2026-02-04 登记新任）= 第二次触达主收件人（info@ 点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://comtime-com.de/impressum/'},
               'facts': {'legal_name': 'comtime GmbH（Amtsgericht Kiel HRB 4574 NO；USt-IdNr. DE 813138753；WEEE DE 84024192）', 'founded': '2000（登记）' + TAG, 'staff': '小型', 'hq': 'Gutenbergring 67b, 22848 Norderstedt（2025-03 迁入）；研发招聘 Bremen',
                         'other': '第 98 批：工业路由器厂「Made in Germany」= 准同行 → 缝隙 = DIN 导轨路由器旁缺工业 PoE 交换机 → 贴 comtime 标 STI-054GP / STI-144GP「Router + Switch 套件」贴标试探 small；2026-02 新 GF → 新管理层补产品线的窗口；低优先' + TAG}},
    'SB-1003': {'kp_match': 'sonja.geserick@aplusnet.de', 'role': 'Geschäftsführerin（Komplementär-GmbH aplusNET Beteiligungs-GmbH HRB 5681）+ Gesellschafterin；二代（2005 接班）= **老板本人 = 收件人**' + TAG,
                'facts': {'legal_name': 'aplus Datenkabel und Kommunikationssysteme GmbH & Co. KG（Amtsgericht Oldenburg HRA 4241；USt-IdNr. DE814202910；资本 €250,000；商标 a-plus / aplusNet 1997）', 'founded': '1986（业务）/ 2005-02-28（现 KG）' + TAG, 'staff': '小型 / 中型（专业分销）', 'hq': 'Gerhard-Stalling-Straße 34, 26135 Oldenburg',
                          'other': '第 98 批：线缆组装起家的网络产品专业分销商（ChannelPartner Spezial-Distributor）；表内「Digitus 的产品很多，价格很高」→ 对标 Digitus 报 STC-110XGE / STI-288DGGPM / STC-228GP，分销 20%；自有商标 aplusNet → 贴标第二句；GF 另一位 Smilka Geserick，创办人 Arno Geserick Prokurist' + TAG}},
    # ---------- GB / AE ----------
    'SB-1054': {'add_kp': {'name': 'Chin Ping (Rio) Luo', 'role': 'Director / Sales Director + PSC（CH 06801342，2009 起）= 收件人（sales@luxritesecurity.com 点名）' + TAG, 'email': '', 'phone': '', 'source': CH + '06801342/officers'},
                'facts': {'legal_name': 'Luxrite Ltd（Companies House 06801342；资本 £1,000；Total Exemption Full；Charges 0）', 'founded': '2009-01-26' + TAG, 'staff': '11–50 人', 'hq': 'Unit 3 Eastman Way, Pin Green Industrial Estate, Stevenage, Hertfordshire SG1 4SZ',
                          'other': '第 98 批：**Trade-only CCTV 分销 + 自有品牌 SPRO / Vectus + 在售 Ruijie PoE → ① 对标 Ruijie 报 HRUI 线分销 20%；② SPRO 标 PoE 交换机 OEM 30%；升 A 候选**；另一董事 / PSC Liu Jung Lo（Secretary）；两位董事华人姓氏 → 大概率已有直采渠道，卖点 = Marvell 管理型 + 3 年保修 + MOQ 1 混批' + TAG}},
    'SB-1002': {'kp_match': 'gina.c@amplicon.com', 'name': 'Gina Citroni', 'role': 'Director + Commercial Director（CH 01091353，2004-07-01 起；亦任 Amplicon Group Ltd 董事）= **商务总监兼董事本人 = 收件人**' + TAG,
                'facts': {'legal_name': 'Amplicon Liveline Limited（Companies House 01091353；PSC Amplicon Group Holdings Ltd 14466238 自 2024-11-20）', 'founded': '1973-01-18' + TAG, 'staff': '50–250 人 / £10–50M（Endole Medium；CH 账目类别 Small）', 'hq': 'Unit 11 Centenary Industrial Estate, Hollingdean Road, Brighton BN2 4AW',
                          'other': '第 98 批：工业计算 / 数据通信分销（Moxa / Hirschmann / Advantech / Cisco）→ 分销 20% 工业线：对标 Moxa EDS 报 STI-288DGGPM / STI-244DGGPM / STI-0240GE，卖点 -50% + 3 年保修 + 宽温；2024-11 集团重组；B BIG；账目至 2024-06-30 已交 2025-03-20' + TAG}},
    'SB-1020': {'country_fix': '阿联酋',
                'facts': {'legal_name': 'Cratsol Technology LLC（迪拜 Business Bay；英国壳 CRATSOL LTD Companies House 11084123，Newcastle upon Tyne 注册地址服务）', 'founded': '2017（UAE）/ 2017-11-27（英国壳）' + TAG, 'staff': '11–50 人；<$5M', 'hq': '601 One by Omniyat / Office 605 Silver Tower, Business Bay, Dubai, UAE',
                          'other': '第 98 批：**国别更正 GB → 阿联酋**（cratsol.co.uk 仅为壳）；IT 硬件 VAR；唯一询盘 10G DAC（非品类）→ 一页纸 STC-110XGE 关联即止；低概率，不加厚' + TAG}},
    'SB-1067': {'add_kp': {'name': 'David Gary Brookes', 'role': 'Director（Engineer，b. 1960；CH 01280393）= 收件人（info@raytelsecurity.com 点名；MD Roy Lawrence 92 岁 = PSC）' + TAG, 'email': '', 'phone': '', 'source': CH + '01280393/officers'},
                'facts': {'legal_name': 'Raytel Security Systems Limited（Companies House 01280393；VAT GB 394 9607 00；前名 Elektroflo Systems Limited 1976–1979；Raytel Group 成员）', 'founded': '1976-10-06（业务 1979 起）' + TAG, 'staff': '2–10 人', 'hq': 'Raytel House, 1-5 Cutlers Road, South Woodham Ferrers, Chelmsford, Essex CM3 5WA',
                          'other': '第 98 批：门禁 / 门口机制造 + Vimar Elvox / Soyal 英国授权分销；微型 + 92 岁老板 → 低概率，一页纸：Raytel 标 4 / 8 口 PoE（STI-054GP / STC-028GP）MOQ 1 一句带过' + TAG}},
    # ---------- PL ----------
    'SB-058': {'kp_match': 'biuro@sabmar.tv', 'role': '业主（CEIDG „SABMARTV” Marcin Wypiór；NIP 6421823587；REGON 273230435）= 终端用户，不加厚' + TAG,
               'facts': {'legal_name': '„SABMARTV” Marcin Wypiór（Indywidualna działalność gospodarcza；NIP 6421823587；REGON 273230435）', 'founded': '1997-05-14（CEIDG）' + TAG, 'staff': '微型（家庭经营）', 'hq': 'ul. Gruntowa 43D, 44-270 Rybnik',
                         'other': '第 98 批：体育赛事网络直播制作个体（速道赛 PPV）= 终端用户，交换机只为转播车 / 演播室 → 一页纸即止（STC-110XGE / STC-424XGGPM-280W 两行）' + TAG}},
    'SB-1009': {'kp_match': 'shop@batna24.com', 'role': '公域 —— 写 zakupy / product manager「switche」抄 shop@（研究档无人名）' + TAG,
                'add_kp': {'name': 'Łukasz Jan Mucha', 'role': '股东 50% + 24 BATNA Sp. k. komandytariusz（rejestr.io / aleo；实际经营者，推定）= 收件人点名；Prezes = Magdalena Mucha（配偶，2022-12 起）' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/1003926/batna'},
                'facts': {'legal_name': 'Batna Sp. z o.o.（KRS 0001003926；REGON 380387214；资本 40,000 zł；关联经营体 24 BATNA Sp. z o.o. Sp. k. KRS 0000908391 / NIP 5732927213）', 'founded': '2022-12-01（现 Sp. z o.o.；业务 2001 起）' + TAG, 'staff': '大型（欧洲级 Ubiquiti / MikroTik 分销；第三方规模指标数亿 zł 级，口径未明）', 'hq': 'ul. Olgi Boznańskiej 3E, 42-202 Częstochowa（注册）/ ul. 1 Maja 23, 42-217 Częstochowa（开票）',
                          'other': '第 98 批：**「main European distributor of Ubiquiti Networks and MikroTik」→ 对标 MikroTik CRS / Ubiquiti USW 报 STC-424XGGPM-280W + HRUI 入门线 + STC-110XGE，分销 20%，B BIG，升 A 候选**；意大利语站点同主体，不重复发' + TAG}},
    'SB-1017': {'kp_match': 'tomasz.wieczorek@cellco.com.pl', 'role': 'Prezes Zarządu + 80% 股东 + 实际受益人（KRS 0000213509，2004 起）= **老板本人 = 收件人**' + TAG,
                'facts': {'legal_name': 'Cellco Communications Sp. z o.o.（KRS 0000213509 Szczecin；NIP 8521826706；资本 52,000 zł；PKD 27.31.Z 光缆生产）', 'founded': '2004-08-03' + TAG, 'staff': '小型 / 中型（第三方规模指标 ≈24 mln zł，口径未明）', 'hq': 'ul. Szczecińska 30E, 73-108 Kobylanka（总部）；Plac Konesera 12, 03-736 Warszawa（分部）',
                          'other': '第 98 批：光纤为主、交换机配套 → 窄品类分销 20%：只报 SFP 上联 / 全光口型号（STC-228GP / STC-2224GP / STC-110XGE / STI-144GP）做「光缆 + 光口交换机」配套；副总 Piotr Wieczorek、R&D Bartosz Wieczorek（家族）' + TAG}},
    'SB-1061': {'facts': {'legal_name': 'FHU „TELSAT” s.c.（民事合伙；NIP 9930003405；合伙人 CEIDG 登记）', 'founded': '未取' + TAG, 'staff': '微型', 'hq': 'ul. Rolnicza 7, 33-100 Tarnów',
                          'other': '第 98 批：微型 CCTV 网店（Dahua 套装为主）→ 低概率，一页纸：HRUI STC-028GP / STC-228GP 两行；Dahua 自带 PoE → 只在非 Dahua 价格带有位置' + TAG}},
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
