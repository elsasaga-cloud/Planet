#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 108 批（T29-U101，公司底数第二十六轮 · 欧洲其他国家 B 池第 2 轮 **扩容 40 户**：IT 9 / NL 5 / SE 4 / RO 3 / CZ 3 / FR 3 / ES 3 / LT 2 / IE 2 / SI 1 / RS 1 / GE 1 / BG 1 / SK 1 / CH 1 / BE 1；其中 SB-1072 实为西班牙）：把官方 / 准官方登记核出来的「老板 / 法定名 / 成立日」回写研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=108 行）。
结构同 batch107_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 30% 目标 · B BIG · 加厚一次 5（SB-1016 ADALTRA（原 CAE Groupe）SIREN 320921364 自有品牌 MMC / S2CEB / Axindus / Casanova → 升 A 候选 / SB-569 CABLEMATIC DOS MIL, S.L.U. CIF B62231261 2000 49 人 自有品牌 BeMatik → 升 A 候选 / SB-455 MaxLink 自贴标 PoE 交换机 + 注入器 + SFP 的 ISP 配件品牌（法人未取）→ 升 A 候选 / SB-397 NETIKS DOO BEOGRAD МБ 17326163 2001 44 人 自有 NT 光模块标 / SB-765 INV-TECHNOLOGIE SAS SIREN 808965941 Dynavision 已中韩代工 small）；
分销 20% · B BIG · 加厚一次 6（SB-1088 TIPTEH d.o.o. 5935652000 1996 东南欧 5 国 140+ 人 Hirschmann 第二价位 → 升 A 候选 / SB-1018 COEL DISTRIBUTION SRL 11989650152 €9.4M Planet 分销 / SB-721 Wood Communications Limited CRO 226087 1924 MD Keith Mahony / SB-1049 KENNEDY O’DONOVAN ELECTRONICS LIMITED = KD Electronics Dahua 爱尔兰主分销（CRO 号未取）/ SB-1057 SC MONDO PLAST SRL RO12755240 2000 4 仓 RO+HU / SB-1055 MARCOM S.r.l. 03718740230 2001 Moxa 分销 + 自编 ISE SKU small）；
分销 20% 加厚 small 4（SB-654 DAVANTEL S.L. CIF B63615553 2004 已分销 Fiberroad / Kyland / SB-709 АйСи ИНТРАКОМ ООД ЕИК 200758666 2009 老板 Hristo Chankov 公开 QQ / WeChat / SB-1097 YATUN, s.r.o. IČO 28176791 2007 Control4 独家 / SB-1071 SIELCO SISTEMI S.r.l. 02854460132 2004 IOlog 自有硬件 贴标可谈 small）；
一页纸一次 · 有回声再加厚 17（SB-1063 HARDWARE SOLUTIONS S.R.L. €8.09M 研华 IPC / SB-318 Verdelon 自有品牌贴 Elink（未坐实）/ SB-907 B.E.S.D. Benelux B.V. KvK 50025619 / SB-107 GLM GROUP LTD 第比利斯 ONV 自编号（部分坐实）/ SB-534 ELFCAM SARL 华人业主 Xia Liu / SB-779 Shop4power.nl KvK 63967588 个体 Planet 专营 / SB-1014 BLUENOTE COMMUNICATIONS SA RO15146404 2003 SCADA 集成 / SB-1040 CHT DATA SRL RO 32791574 ICP DAS 网店 / SB-1069 REWEB S.R.L. 02026760351 €2.61M IoT VAD / SB-1072 SECURAME, S.L. CIF B62808498 2002 **实为西班牙 → country_fix** / SB-1074 SETIK S.R.L. 09729650961 €3.89M 安防电商 / SB-571 UAB ENERGUS GROUP 304419130 130 人能源承包 集成 25% / SB-1007 AV Nordic Hemsat AB 556594-9863 / SB-1036 Grin s.r.l. 02710060738 配电柜承包 集成 25%（部分坐实）/ SB-1042 MCV Systems s.r.o. IČO 47378352 USR IoT 网店 / SB-1044 IP CCTV GmbH CHE-112.152.195 2004 Andy Tautschnig / SB-1060 UAB Enzas = Norteh 303005607 / SB-1082 Standard Audio Systems AB 556203-9726 SEK 61M AV 分销 / SB-1093 Vercoma Communicatie Systemen B.V. KvK 34219252 Golmar 子公司）；
不动 6（SB-525 Atlantis-Land 未坐实 + 官网不可达 + 13 次无回复 / SB-855 NEXTLAN s. r. o. IČO 25924826 19 次无回复 + 域名曾易主 / SB-1029 Fibersystem AB 556605-4325 Addtech 集团国防保密通信制造商 守界 / SB-1037 High’Trade International 驻港寻源中间商 未坐实 / SB-1043 Zeevalk IT KvK 60651792 一人兼营 / SB-944 Fybera 未坐实 + 12 次无回复）。
坐实 32 / 部分坐实 4（SB-107 ს/კ 未取 / SB-1049 CRO 号未取 / SB-1036 REA 未取 / SB-455 法人未取）/ 未坐实 4（SB-318 / SB-525 / SB-1037 / SB-944）；
KP 坐实 = 老板 / 董事 / 总经理本人 14（SB-1088 Damijan Jager / SB-397 Pavle Pulek / SB-534 Xia Liu / SB-765 Alexandre Noireaux / SB-721 Keith Mahony + Derek Finlay + Pat Kennedy / SB-1097 Martin Wokoun / SB-1029 Oscar Lindberg / SB-571 Povilas Šidlauskas / SB-709 Hristo Chankov / SB-1007 Martin Carlzon / SB-1016 Bruno Poisson / SB-1044 Andy Tautschnig / SB-1049 Sean Kennedy + Stephen Carroll / SB-1082 Michael Kahlau / SB-1093 Gian Zandonà + Chris Standaar）；国别更正 1（SB-1072 意大利 → 西班牙）；
法定名补全 14（SB-1018 / SB-721 / SB-779 / SB-855 / SB-654 / SB-1097 / SB-1014 / SB-1040 / SB-1072 / SB-1074 / SB-709 / SB-1007 / SB-1042 / SB-1043 / SB-1049 / SB-1057 / SB-1060 / SB-1093 / SB-569）；升 A 候选 4（SB-1016 / SB-569 / SB-455 / SB-1088，回信即 A；次候选 SB-397 / SB-1018 / SB-721 / SB-1057 / SB-1049）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 108 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- 第 1/3 ----------
    'SB-1055': {'facts': {'legal_name': 'MARCOM S.r.l.（P.IVA / CF 03718740230；Registro Imprese di Verona）', 'founded': '2001' + TAG,
                          'other': '第 108 批：维罗纳工业自动化通信分销商（Moxa 工业交换机、工业路由器、LoRaWAN），网店自编 ISE 系列工业交换机 SKU；股本 €20,000；11–50 人 → **分销 20% + 贴标可谈，B，加厚一次（small）**；收件人 info@ 点名 ufficio acquisti' + TAG}},
    'SB-1063': {'facts': {'legal_name': 'HARDWARE SOLUTIONS S.R.L.（P.IVA 02974270361；REA MO-347206）', 'founded': '2005-02-22' + TAG,
                          'other': '第 108 批：Fiorano Modenese 工业 PC / HMI 集成分销商（Advantech Integrator Partner、APLEX 分销）；2024 营收 €8.09M / 净利 €1.40M / 10 人 → **采购型 25% + 分销 20%，B，一页纸一次（STI 配 IPC 机柜）**' + TAG}},
    'SB-1088': [{'add_kp': {'name': 'Damijan Jager', 'role': 'Direktor（bizi.si / ebonitete / companywall.si）= 拍板人 / 收件人（info@tipteh.si 点名）' + TAG, 'email': 'info@tipteh.si', 'source': 'https://www.bizi.si/TIPTEH-D-O-O/'}},
                {'facts': {'legal_name': 'TIPTEH d.o.o., zastopanje in distribucija（matična 5935652000；DŠ SI53509382）', 'founded': '1996-03-15' + TAG,
                           'other': '第 108 批：卢布尔雅那工业自动化分销集团（30+ 品牌含 Hirschmann 工业交换机；子公司 SI / HR / BA / RS / MK，集团 140+ 人；SI 本体 30 人、营收 €9.42M、权益 €7.76M）→ **分销 20%，B BIG，加厚一次（STI 作 Hirschmann 第二价位）；升 A 候选（回信即 A）**' + TAG}}],
    'SB-318': {'facts': {'legal_name': 'Verdelon（品牌；瑞典法人未取 → 未坐实）', 'founded': '未取' + TAG,
                         'other': '第 108 批：1 次检索（allabolag / bolagsverket 口径）未命中任何 Verdelon 法人（仅 Verdion AB 同名异主）→ 未坐实；自有品牌工业 PoE 交换机（贴 Elink）= **贴标 OEM 30% 目标，先一页纸一次，回声后补核法人再加厚**' + TAG}},
    'SB-397': [{'add_kp': {'name': 'Pavle Pulek', 'role': 'Direktor / 法定代表（companywall.rs / netiks.ls.rs）= 拍板人 / 收件人（info@netiks.rs 点名）' + TAG, 'email': 'info@netiks.rs', 'source': 'https://www.companywall.rs/firma/netiks-doo-beograd/MMouX76q'}},
               {'facts': {'legal_name': 'NETIKS DOO BEOGRAD（PRIVREDNO DRUŠTVO NETIKS DOO BEOGRAD (ZVEZDARA)；МБ 17326163；ПИБ 101720299）', 'founded': '2001-07-24' + TAG,
                          'other': '第 108 批：贝尔格莱德网络设备 B2B 商店 + 工程，44 人（2025），**自有「NT」光模块品牌** → **贴标 OEM 30% 可谈（NT 标 PoE / L2 交换机）+ 分销 20%，B BIG，加厚一次；次候选升 A**' + TAG}}],
    'SB-907': {'facts': {'legal_name': 'B.E.S.D. Benelux B.V.（KvK 50025619）', 'founded': '1989' + TAG,
                         'other': '第 108 批：Weert 工业嵌入式 + 数据通信进口分销商（2–10 人；PI Nederland 会员；姊妹站 EKS 光纤）→ **分销 20% small，一页纸一次**；收件人 sales@besd.nl' + TAG}},
    'SB-107': {'facts': {'legal_name': 'GLM GROUP LTD（第比利斯 Didube；ს/კ 未取 → 部分坐实）', 'founded': '未取' + TAG,
                         'other': '第 108 批：安防 / 电信方案商 + 电商（CCTV、门禁、PoE），在售 ONV 交换机并自编号 GLMH1064PL → **贴标 30% 可谈 + 分销 20%，B，一页纸一次**；发信窗口 Thu 12–14 GET' + TAG}},
    'SB-525': [{'kp_match': 'mdl@atlantis-land.com', 'role': 'Buyer（研究档）；法人 / 官网均未核出' + TAG},
               {'kp_match': 'info@atlantis-land.com', 'role': 'Director（研究档）；法人 / 官网均未核出' + TAG},
               {'facts': {'legal_name': 'Atlantis-Land（品牌；法人 / P.IVA 未取 → 未坐实）', 'founded': '未取' + TAG,
                          'other': '第 108 批：官网不可达 + 1 次检索仅命中 Atlantis S.r.l. 罗马 / 布雷西亚同名异主 + 13 次群发无回复 → **不动**（Simon 曾说可多跟进：若官网恢复再补核法人并发一页纸）' + TAG}}],
    'SB-534': [{'kp_match': 'contact@elfcams.com', 'role': '研究档联系人（contact@）= 收件人；拍板人 = gérant Xia Liu' + TAG},
               {'add_kp': {'name': 'Xia Liu', 'role': 'Gérant / 业主（2018 起；1988 年生；华人）= 拍板人（抄送）；中文直联 Simon 定（默认否）' + TAG, 'email': '', 'source': 'https://www.pappers.fr/entreprise/elfcam-844111856'}},
               {'facts': {'legal_name': 'ELFCAM SARL（SIREN 844 111 856；TVA FR36844111856；RCS Créteil）', 'founded': '2018-11-20' + TAG,
                          'other': '第 108 批：Thiais 光纤 / 网络设备电商（自称工厂直销；3–5 人；股本 €20,000）→ **分销 20% small，一页纸一次**；华人业主' + TAG}}],
    'SB-765': [{'kp_match': 'maxence@inv-technology.com', 'role': 'Technical Manager（研究档；Noireaux 家族）= 收件人' + TAG},
               {'add_kp': {'name': 'Alexandre Noireaux', 'role': 'Président / 创始人（2015 起；1966 年生；manageo / societe.com）= 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://www.societe.com/societe/import-network-video-technology-inv-technologie-808965941.html'}},
               {'facts': {'legal_name': 'IMPORT NETWORK VIDEO TECHNOLOGY – INV-TECHNOLOGIE SAS（Dynavision；SIREN 808 965 941；TVA FR30808965941）', 'founded': '2015-01-22' + TAG,
                          'other': '第 108 批：科西嘉 Borgo 视频监控 / 门禁进口批发商，**自有品牌 DYNAVISION 已由中国 / 韩国合作厂代工近 10 年**；3–5 人；2025 营收 €760k → **贴标 OEM 30% 正中目标（Dynavision 标 PoE 交换机），B，加厚一次（small）**' + TAG}}],
    'SB-1018': [{'add_kp': {'name': 'A. Fallerini（姓名待核）', 'role': '研究档联系人 a.fallerini@coeldistribution.it = 收件人（抄 info@ 点名 ufficio acquisti）' + TAG, 'email': 'a.fallerini@coeldistribution.it', 'source': 'https://www.coeldistribution.it/contattaci/'}},
                {'facts': {'legal_name': 'COEL DISTRIBUTION SRL（P.IVA / CF 11989650152；REA MB-2629252，旧 MI-1521836）', 'founded': '1994（活动）/ 1997（登记）' + TAG,
                           'other': '第 108 批：Muggiò (MB) 布线 / 网络 / 电信分销商（Planet Networking / Prysmian / R&M / Rosenberger；目录含 IGS-801T / IGS-1020PTF 工业交换机）；11–50 人；研究档 2023 营收 €9.4M → **分销 20%，B BIG，加厚一次（STI 1:1 对照台系工业机型；不点名 Planet）；次候选升 A**' + TAG}}],
    'SB-721': [{'add_kp': {'name': 'Derek Finlay', 'role': 'Sales Director（2007 MBO 核心；electric.ie）= 收件人（sales@woodcomm.ie 点名）' + TAG, 'email': 'sales@woodcomm.ie', 'source': 'https://electric.ie/wood-communications-celebrate-100-years-of-leadership-in-data-and-telecoms-infrastructure-solutions/'}},
               {'add_kp': {'name': 'Keith Mahony', 'role': 'Managing Director（2005 起董事；vision-net / irishtrade）= 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://www.vision-net.ie/Company-Info/Wood-Communications-Limited-226087'}},
               {'facts': {'legal_name': 'Wood Communications Limited（CRO 226087；PRL IE01544W）', 'founded': '1924（活动）；公司号 226087' + TAG,
                          'other': '第 108 批：都柏林 Ballymount 老牌网络 / 布线 / 数据中心 / IP CCTV 分销商（Planet Technology 为其交换机品牌之一；2007-11 MBO 后管理层持有；11–50 人）→ **分销 20%，B BIG，加厚一次；次候选升 A**；UKCA 不适用（IE = CE）' + TAG}}],
    'SB-779': {'facts': {'legal_name': 'Shop4power.nl（eenmanszaak；h.o.d.n. Shop4networks.nl；KvK 63967588；BTW NL001646847B50）', 'founded': '≈2015（KvK 639…）' + TAG,
                         'other': '第 108 批：Wijhe 一人 UPS / 电池 / 网络网店，「Planet-specialist」自备库存并兼卖 E-Link → **分销 20% small，一页纸一次**；MOQ 1 友好' + TAG}},
    'SB-855': {'facts': {'legal_name': 'NEXTLAN s. r. o.（IČO 25924826；DIČ CZ25924826；C 14968 KS Hradec Králové）', 'founded': '1999-08-03' + TAG,
                         'other': '第 108 批：Chrudim 网络 / 电信 VAD（Axis、Fluke、IMC、Lantech；6–25 人）仍在册，但 19 次群发无回复 + 研究档域名曾易主 → **不动**' + TAG}},
    'SB-654': [{'kp_match': 'jrsalvador@davantel.com', 'name': 'Jose Salvador Collado', 'role': 'CTO（研究档）= 收件人 / 技术拍板' + TAG},
               {'facts': {'legal_name': 'DESARROLLOS AVANZADOS EN TELECOMUNICACIONES, S.L.（DAVANTEL；CIF B63615553）', 'founded': '2004-10-15' + TAG,
                          'other': '第 108 批：巴塞罗那电信接入 / 传输方案分销商（2–10 人；分销 Teltonika、**Fiberroad、Kyland**、Gigalight、Raisecom、Loop Telecom）→ **分销 20%，B，加厚一次（small；STI 1:1 对照其在售中国工业管理型 FS；不点名）**' + TAG}}],
    'SB-1097': [{'add_kp': {'name': 'Martin Wokoun', 'role': 'Jednatel（2007-10-31 起；finmag / zivefirmy）= 拍板人 / 收件人（obchod@yatun.cz 点名）' + TAG, 'email': 'obchod@yatun.cz', 'source': 'https://www.finmag.cz/obchodni-rejstrik/28176791-yatun-s-r-o'}},
                {'facts': {'legal_name': 'YATUN, s.r.o.（IČO 28176791；DIČ CZ28176791）', 'founded': '2007-10-30' + TAG,
                           'other': '第 108 批：布拉格智能家居 / 楼宇自动化 / AV 专业分销商（Control4 / Fibaro / Ekinex CZ+SK 独家；安装商渠道）→ **分销 20%，B，加厚一次（small；STC 配智能家居机柜）**' + TAG}}],
    # ---------- 第 2/3 ----------
    'SB-1014': {'facts': {'legal_name': 'BLUENOTE COMMUNICATIONS SA（CUI RO15146404；J22/101/2003）', 'founded': '2003-01-22' + TAG,
                          'other': '第 108 批：雅西 SCADA / IoT / IIoT 集成商 + 通话录音系统开发商（实缴股本 105,000 RON；EEE 生产者登记）→ **集成 25%，B，一页纸一次（STI 配 SCADA 柜）**；收件人 office@bluenote.ro' + TAG}},
    'SB-1029': [{'add_kp': {'name': 'John Oscar Lindberg', 'role': 'VD（allabolag；Addtech 体系）— 仅记录，不发' + TAG, 'email': '', 'source': 'https://www.allabolag.se/foretag/fibersystem-ab/bromma/datorer-och-kringutrustningar-tillverkning/2K1VV05I63ILT'}},
                {'facts': {'legal_name': 'Fibersystem AB（org.nr 556605-4325；Addtech Nordic AB 子公司）', 'founded': '2001-01-22' + TAG,
                           'other': '第 108 批：Bromma 保密通信设备制造商（SNI 26200；数据二极管 / TEMPEST 级产品；13 人；2025 营收 SEK 266.9M；客户国防 / 政府）→ **守界不动（军工 / 政府主业；自研产品非我方品类）**' + TAG}}],
    'SB-1037': {'facts': {'legal_name': 'High’Trade International（网站署 High Trade International Ltd；总部香港 Sheung Wan；法人 / 注册号未取 → 未坐实）', 'founded': '未取' + TAG,
                          'other': '第 108 批：实为驻港电子元器件 / 家电配件寻源中间商（华南 200 家工厂为欧美大客户寻源；+86 电话；Gmail 联系人）→ **不动**；国别存疑（研究档法国 ← 网站香港）暂不改 iso' + TAG}},
    'SB-1040': {'facts': {'legal_name': 'CHT DATA SRL（CUI RO 32791574；J40/8808/2020；关联 Instruments CHT SRL Ploiești = ICP DAS 官方列名经销商）', 'founded': '≈2014；J40 2020 迁册' + TAG,
                          'other': '第 108 批：布加勒斯特 ICP DAS 网店 + Axiomtek 工控（office@icpdas.ro）→ **分销 20% small，一页纸一次（STI 作第二价位；不点名 ICP DAS）**' + TAG}},
    'SB-1069': {'facts': {'legal_name': 'REWEB S.R.L.（P.IVA 02026760351；REA RE-244931）', 'founded': '2002-12-07（活动 1983 起）' + TAG,
                          'other': '第 108 批：雷焦艾米利亚 IT / IoT 增值分销商（M2M SIM、蜂窝路由 + 天线 + 交换机打包、Advantech、Opengear）；2024 营收 €2.61M / 净利 €399k / 10 人 → **分销 20%，B，一页纸一次（STI 配蜂窝路由柜）**' + TAG}},
    'SB-1072': [{'kp_match': 'contacto@securame.com', 'role': '通用箱（administradores solidarios 未具名）= 收件人' + TAG},
                {'country_fix': '西班牙'},
                {'facts': {'legal_name': 'SECURAME, S.L.（原 TWISTED REALITY S.L.；CIF B62808498；Registro Mercantil de Barcelona）', 'founded': '2002-03-01' + TAG,
                           'other': '第 108 批：**巴塞罗那（研究档误记意大利 → country_fix 西班牙）** 视频监控 / 安防批发网店（Safire 经销；2–10 人；销售 ≈€0.5M）→ **分销 20% small，一页纸一次**；发信窗口 Thu 12–14 CET；西语引子' + TAG}}],
    'SB-1074': {'facts': {'legal_name': 'SETIK S.R.L.（P.IVA 09729650961；REA MB-1910472）', 'founded': '2017-01-09' + TAG,
                          'other': '第 108 批：Cesano Maderno / Lissone 安防套件电商（Dahua / Hikvision / TP-Link；2025 营收 €3.89M、净利 €9k、10 人；法国分支 2025-11 注销）→ **分销 20% small，一页纸一次（PoE 交换机配摄像机套件）**' + TAG}},
    'SB-571': [{'kp_match': 'info@energus.eu', 'role': 'Projektų vadovas（LinkedIn；可能已离职）→ 改点名 direktorius' + TAG},
               {'add_kp': {'name': 'Povilas Šidlauskas', 'role': 'Direktorius（rekvizitai / okredo）= 拍板人 / 收件人（info@energus.eu 点名）' + TAG, 'email': 'info@energus.eu', 'source': 'https://rekvizitai.vz.lt/en/company/energus_group/'}},
               {'facts': {'legal_name': 'UAB „ENERGUS GROUP“（įmonės kodas 304419130；PVM LT100011259419）', 'founded': '2016-11-02（Energus 品牌 2010）' + TAG,
                          'other': '第 108 批：维尔纽斯电气 / 能源工程承包商（光伏、变电、充电桩；117–133 人；2025 营收 €12.95M / 净利 €289k；股本 €27,000）→ **集成 25%，B，一页纸一次（STI 配 PV 监控柜 / 变电站；不谈 IEC 61850）**' + TAG}}],
    'SB-709': [{'kp_match': 'hristo.chankov@ic-intracom.bg', 'name': 'Hristo Chankov', 'role': 'Управител + 55% 股东 + Търговски директор（papagal.bg / 官网 За нас；公开 QQ / WeChat = 直采中国）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'АйСи ИНТРАКОМ ООД（IC INTRACOM Ltd.；ЕИК 200758666；ДДС BG200758666）', 'founded': '2009-06-19' + TAG,
                          'other': '第 108 批：索非亚光纤网络有源 / 无源 + 布线 + 数据中心产品分销商（电信与 DC 客户；7 人；营业额 2.045M лв. 2020；股东 Чанков 55% / Желева 45%）→ **分销 20%，B，加厚一次（small；老板已直采中国，切口「factory-direct with EU-side invoicing」）**；WeChat 不用' + TAG}}],
    'SB-1007': [{'add_kp': {'name': 'Fredrik Kärrander', 'role': 'Marknadsföring（官网 Kontakta oss；fredrik@avnordic.se）= 收件人' + TAG, 'email': 'fredrik@avnordic.se', 'source': 'https://avnordic.se/om-av-nordic/kontakta-oss/'}},
                {'add_kp': {'name': 'Martin Carlzon', 'role': 'VD / ägare（官网；Bolagsverket 登记 VD Hans Martin Karlsson，同一人待核）= 拍板人（抄 info@ 点名）' + TAG, 'email': 'info@avnordic.se', 'source': 'https://www.allabolag.se/foretag/av-nordic-hemsat-ab/bor%C3%A5s/elektronik-och-telekommunikationsutrustning/2K1TMEFI63IFR'}},
                {'facts': {'legal_name': 'AV Nordic Hemsat AB（org.nr 556594-9863；Hemfast Holding AB 子公司）', 'founded': '2000-07-11' + TAG,
                           'other': '第 108 批：Borås 安防 / 网络 / 音响 B2B 批发商（Uniview / Milesight；登记 1 名雇员；2025 营收 SEK 8.4M −36%）→ **分销 20% small，一页纸一次**' + TAG}}],
    # ---------- 第 3/3 ----------
    'SB-1016': [{'add_kp': {'name': 'Bruno Poisson', 'role': 'Président du groupe ADALTRA（CCI Essonne 2025-09）= 拍板层（不直发；收件人 = direction achats via contact@adaltra.fr）' + TAG, 'email': 'contact@adaltra.fr', 'source': 'https://www.essonne.cci.fr/actualites/adaltra-un-nouveau-nom-pour-cae-groupe-et-de-fortes-ambitions-linternational'}},
                {'facts': {'legal_name': 'ADALTRA（原 CAE GROUPE / CAE - DATA；SIREN 320 921 364 RCS Évry；TVA FR13320921364；Président = ADALTRA GROUP 498 664 010）', 'founded': '1989-12-28' + TAG,
                           'other': '第 108 批：Massy（2025-12 起）线缆与连接方案设计分销集团（自有品牌 MMC / S2CEB / Axindus / Casanova；4,500 SKU；Villabé 23,000 m² 仓；SAS 股本 €2,727,360；2025-09 更名）→ **贴标 OEM 30% 正中目标 + 分销 20%，B BIG，加厚一次；升 A 候选（回信即 A）**；旧域名 cae-groupe.fr 邮箱或失效 → 用 adaltra.fr' + TAG}}],
    'SB-1036': {'facts': {'legal_name': 'Grin s.r.l.（P.IVA 02710060738；REA 未取 → 部分坐实）', 'founded': '未取' + TAG,
                          'other': '第 108 批：Torricella (TA) 电气 / 仪表工程承包 + 配电柜制造（客户 Terna / Heineken / Sidel / Siemens 等）→ **集成 25% small，一页纸一次（STI 配 PLC 柜）**' + TAG}},
    'SB-1042': {'facts': {'legal_name': 'MCV Systems s.r.o.（经营 iotkomponenty.sk；IČO 47 378 352；IČ DPH SK2023841930）', 'founded': '≈2013（IČO 4737…）' + TAG,
                          'other': '第 108 批：布拉迪斯拉发工业物联网元件网店（USR IoT / Mean Well / Teltonika；配送全欧盟）→ **分销 20% small，一页纸一次（STI 配串口服务器）**' + TAG}},
    'SB-1043': [{'add_kp': {'name': 'Laurens Marnix Zeevalk', 'role': 'Eigenaar（drimble；个体）— 仅记录' + TAG, 'email': '', 'source': 'https://drimble.nl/bedrijf/heerjansdam/29829178/zeevalk-it.html'}},
                {'facts': {'legal_name': 'Zeevalk IT（h.o.d.n. Ipcamerawebwinkel；eenmanszaak；KvK 60651792；BTW NL199719214B01）', 'founded': '≈2014' + TAG,
                           'other': '第 108 批：Heerjansdam 一人兼营（主业网页设计 + IP 摄像机网店）→ **不动**' + TAG}}],
    'SB-1044': [{'add_kp': {'name': 'Andreas (Andy) Tautschnig', 'role': 'Gesellschafter / Geschäftsführer（UID 公示 / kompass / dachsen.ch）= 拍板人 / 收件人（andy.tautschnig@ipcctv.ch）' + TAG, 'email': 'andy.tautschnig@ipcctv.ch', 'source': 'https://www.ipcctv.ch/info_ip_cctv.htm'}},
                {'facts': {'legal_name': 'IP CCTV GmbH（UID CHE-112.152.195；CH-020.4.030.130-0）', 'founded': '2004' + TAG,
                           'other': '第 108 批：Dachsen (ZH) 视频监控 / 门禁 / 对讲贸易 + 服务（1–4 人；股本 CHF 20,000）→ **分销 20% small，一页纸一次**；瑞士非欧盟 → DAP 注明清关由买方' + TAG}}],
    'SB-1049': [{'add_kp': {'name': 'Stephen Carroll', 'role': 'Commercial Director（LinkedIn；前 Dahua UK & Ireland）= 收件人（sales@kdelectronics.ie 点名）' + TAG, 'email': 'sales@kdelectronics.ie', 'source': 'https://ie.linkedin.com/company/kd-electronics-ireland'}},
                {'add_kp': {'name': 'Sean Kennedy', 'role': 'Director / 业主（D&B Key Principal SEAN ANTHONY KENNEDY；Sean Jr 亦任 Director）= 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://www.kdelectronics.ie/meet-the-team.html'}},
                {'add_kp': {'name': 'Jiawei Sun', 'role': 'Head of Sales / BDM（LinkedIn；华人）— 中文直联 Simon 定（默认否）' + TAG, 'email': '', 'source': 'https://ie.linkedin.com/company/kd-electronics-ireland'}},
                {'facts': {'legal_name': 'KENNEDY O’DONOVAN ELECTRONICS LIMITED（t/a KD Electronics / KD ELECTRONICS LTD；CRO 号未取 → 部分坐实）', 'founded': '1994（活动）' + TAG,
                           'other': '第 108 批：科克 + 都柏林两地仓的安防 / 消防 / 网络 / AV 贸易批发商（「Ireland’s premier Dahua distributor」+ i-PRO / Ajax / TP-Link；21–50 人）→ **分销 20%，B BIG，加厚一次；次候选升 A**；UKCA 不适用（IE = CE）' + TAG}}],
    'SB-1057': [{'add_kp': {'name': 'Ovidiu Pătru', 'role': '商务联系人（gmdu 口径 Mr. Patru Ovidiu）= 收件人（timisoara@mondoplast.net 点名）' + TAG, 'email': 'timisoara@mondoplast.net', 'source': 'https://www.gmdu.net/corp-738086.html'}},
                {'facts': {'legal_name': 'SC MONDO PLAST SRL（CUI RO12755240；J2000000053116；注册地 Bocșa）', 'founded': '2000-02-22' + TAG,
                           'other': '第 108 批：蒂米什瓦拉电信设备进口分销商（CATV / CCTV / 光缆 / 卫星 / 电台 / UPS / 交换机 / MC；Hirschmann + Hikvision；供 Hornbach；仓 București / Timișoara / Brașov / Gyál (HU)；股本 7.4M lei；县 CAEN 4652 第 2）→ **分销 20%，B BIG，加厚一次；次候选升 A**' + TAG}}],
    'SB-1060': {'facts': {'legal_name': 'UAB Enzas（经营 norteh.com「NORTEH」；įmonės kodas 303005607；PVM LT100009310917）', 'founded': '≈2013（kodas 3030…）' + TAG,
                          'other': '第 108 批：维尔纽斯多语言 CCTV 网店（Hikvision / Dahua / Longse / Reolink / Ajax）→ **分销 20% small，一页纸一次**' + TAG}},
    'SB-1071': {'facts': {'legal_name': 'SIELCO SISTEMI S.r.l.（P.IVA 02854460132；REA CO-282515）', 'founded': '2004-12-07' + TAG,
                          'other': '第 108 批：科莫 Guanzate 工业自动化软硬件厂商（Winlog SCADA、IOlog Modbus I/O、PClog 面板 PC；网店兼售工业交换机；2–10 人）→ **贴标可谈 small（Sielco 标 DIN 交换机）+ 分销 20%，B，一页纸一次**' + TAG}},
    'SB-1082': [{'add_kp': {'name': 'Karl Gustaf Michael Kahlau', 'role': 'VD（allabolag；1963 年生）= 拍板人 / 收件人（info@standardaudio.se 点名 Michael Kahlau）' + TAG, 'email': 'info@standardaudio.se', 'source': 'https://www.allabolag.se/foretag/standard-audio-systems-ab/arlandastad/radio-tv-programbolag/2JZHTBII5YH40'}},
                {'facts': {'legal_name': 'Standard Audio Systems AB（org.nr 556203-9726；VAT SE556203972601）', 'founded': '1980-02-25（活动 1979）' + TAG,
                           'other': '第 108 批：Arlandastad 专业音频 / 语音疏散 / AV 控制分销商（EV / Dynacord；15 人；2025 营收 SEK 61.2M；股本 SEK 1M；子公司 Public Audio Systems）→ **分销 20%，B，一页纸一次（管理型 PoE 配 AV 机柜）**' + TAG}}],
    'SB-1093': [{'add_kp': {'name': 'Chris Standaar', 'role': 'Technisch Tekenaar – Inkoop Coördinator（官网 Team）= 收件人' + TAG, 'email': '', 'source': 'https://www.vercoma.nl/over-vercoma/team-vercoma'}},
                {'add_kp': {'name': 'Gian Zandonà', 'role': 'Algemeen directeur（2024 起；官网 / companyinfo）= 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://www.vercoma.nl/nieuws/een-warm-welkom-voor-gian-zandona-nieuwe-directeur-vercoma'}},
                {'facts': {'legal_name': 'Vercoma Communicatie Systemen B.V.（KvK 34219252；BTW NL814413146B01；Golmar Sistemas de Comunicación S.A. 子公司）', 'founded': '1978（活动）；B.V. ≈2005' + TAG,
                           'other': '第 108 批：Wormerveer 门禁 / 对讲 / CCTV 进口分销（Golmar 荷兰独家；11–50 人；安装商渠道）→ **分销 20% small，一页纸一次（PoE 配 IP 对讲项目）**；回声后考虑并线 Golmar 总部' + TAG}}],
    'SB-455': {'facts': {'legal_name': 'MaxLink（品牌 2006 起；总部 Plzeň–Lobzy Cvokařská 1216/8；运营法人 / IČO 未取 → 部分坐实）', 'founded': '品牌 2006' + TAG,
                         'other': '第 108 批：面向 ISP 的网络配件自有品牌（天线、SFP/SFP+/DAC、无源 / 有源 PoE 注入器含 10G bt、PoE 面板、**PoE 交换机**、安装箱）→ **贴标 OEM 30% 正中目标，B BIG，加厚一次（只报 OEM 档）；升 A 候选（回信即 A）；法人回声后补核**' + TAG}},
    'SB-569': {'facts': {'legal_name': 'CABLEMATIC DOS MIL, S.L.U.（CIF B62231261；Registro Mercantil de Barcelona）', 'founded': '2000-04-01' + TAG,
                         'other': '第 108 批：巴塞罗那电脑周边 / 网络 / 线缆进出口分销 + 多平台电商（自有品牌 BeMatik / Cablemarkt；股本 €2,547,000；≈49 人）→ **贴标 OEM 30% 正中目标（BeMatik 标 PoE 交换机 / MC）+ 分销 20%，B BIG，加厚一次；升 A 候选（回信即 A）**；收件人 comercial@ 点名 compras' + TAG}},
    'SB-944': {'facts': {'legal_name': 'Fybera（品牌；比利时法人未取 → 未坐实）', 'founded': '2010（brandfetch 口径）' + TAG,
                         'other': '第 108 批：官网不可达 + 1 次检索（KBO / companyweb 口径）未命中法人 + 12 次群发无回复 → **不动**（自贴标 MC 本是贴标目标，待官网 / 法人恢复可查再议）' + TAG}},
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
