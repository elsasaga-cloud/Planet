#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 109 批（T29-U102，公司底数第二十七轮 · 欧洲其他国家 B 池第 3 轮 40 户：IT 11 / ES 6 / CZ 4 / SE 3 / FR 3 / FI 2 / HU 2 / GR 2 / LT 1 / BE 1 / DK 1 / RO 1 / BG 1 / CH 1 / NL 1）—— 把 registry（batch=109）已核实的官方登记事实回写研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=109 行）。
结构同 batch108_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 30% 目标 · B BIG · 加厚一次 4（SB-522 GUILERA, S.A. CIF A08851461 1953 / 1981 自有品牌 ADILEC 光传输 / SB-589 BY DEMES SL CIF B60347010 1985 伊比利亚 #1 安防分销 132 人 自有品牌 AIRSPACE / CCTVDIRECT → 回信即 A / SB-288 SECOMP International AG CHE-112.622.278 集团 250 人 自有品牌 ROLINE / VALUE / SB-309 Alternetivo s.r.o. IČO 25098314 1996 VAD 自有品牌 NNET）；
分销 20% · B BIG · 加厚一次 6（SB-1129 REDCORP SA/NV BCE 0448.875.715 1989 €32M 创始人 Ronald / Dino Reich / SB-432 QUBIX S.P.A. 03575150283 €29.7M 净利 €6.6M 几乎全线台系 → 回信即 A / SB-470 ASM = 100MEGA Distribution s.r.o. 60707968 100–149 人 / SB-423 EQUIPEMENTS SCIENTIFIQUES (ES France) 353579634 €101.5M Guez 家族 / SB-1092 Unifibre 分支 → OPTOPLAST S.R.L. 01220320665 €20.7M 2026-10-01 并购 / SB-1022 DANBIT A/S CVR 78788216 自编 ESW 货号 = 现成贴牌买家 small）；
分销 20% + 贴标可谈 加厚 small 1（SB-1052 LAN Kft. 10678994-2-42 20–49 人 自编货号）；
一页纸一次 · 有回声再加厚 24（SB-996 ADJ = IoT Tecnologie s.r.l. 04446661219 贴标可谈 / SB-997 Agmultivision 04302850963 / SB-998 AKIS Technologies UAB 120113138 / SB-1130 CNSTECH 已回信 / SB-431 PROTEKNA 03451940237 Moxa 经销 / SB-816 LORWEN = LAPOTECH S.R.L.S. 05082330654 贴标可谈 / SB-1008 Avstek Oy 2721676-8 / SB-1086 TEAM TELECOM SRL 14306256 €3.2M / SB-1126 KLINGER Finland Oy 0195519-1 CCTV 事业部 / SB-1128 LOSAN s.r.o. 64053580 / SB-461 EMOS spol. s r.o. 19014104 Legrand 100% 低命中 / SB-985 QNV SL B60574779 换切口 / SB-015 Suministros Industriales MP4 SL B63629968 / SB-024 Erstech Technika Kft. 13118145-2-13 / SB-026 Safe-tech CCTV Systems SWEDEN AB 556732-8181 WA / SB-295 WI-COM SOLUTIONS 07628770963 非轨交 / SB-009 SICURMAX S.R.L. 02360600239 守界通过只谈民用 WA / SB-257 VOXPLUS 05516110961 / SB-394 МАКСТЕЛ ООД 130157325 换切口 / SB-524 Armadi-Rack = M.D.W. srl 02766841205 / SB-201 EL.SI. S.R.L. 01536710799 / SB-774 MP2 Netwerkproducten B.V. KvK 62165984 换切口 / SB-025 SIPE SAS 814329462 / SB-057 RFCOM Ξυγκάκης Ο.Ε. WA）；
并线 1（SB-1011 Binär Teknik Scandinavia AB 559181-6201 = Danbit 瑞典壳 → 并线 SB-1022）；
不动 4（SB-1070 SafeGuard Sverige AB 559523-7867 前身 SafeGuard Sweden AB 556848-7226 2025 破产 + 新壳 1 人 / SB-764 IFOTEC SAS 421531708 法国自产工业交换机 = 同行 / SB-046 INTELIWARE SL B86690344 一人网店 + 亏损 + 8 次 0 回复 / SB-014 Intec Seguridad 域名与候选法人 B57518151 未证实 + 20 次 0 回复）；
坐实 36 / 部分坐实 4（SB-1130 ΑΦΜ 未取 / SB-057 ΑΦΜ 未取 ΓΕΜΗ 推定 / SB-014 同一性未证实 / SB-524 成立日未取）/ 未坐实 0；
KP 坐实 = 老板 / 董事 / 总经理本人 19（SB-1129 Ronald + Dino Reich / SB-1130 Panagiotis Lichas / SB-764 Gilles Billet / SB-1008 Jari Haaparanta / SB-1022 Peter Grubb Jensen / SB-1052 Hegedűs József / SB-1128 Jan Stehno / SB-015 Silvia Pascual Fernández / SB-024 János Hőgye / SB-026 Jimmy Johansson / SB-046 Rafael Torrico / SB-309 Lukáš Reif / SB-589 Ricardo Rubi Rio / SB-423 Daniel + Laurent Guez / SB-009 Massimo Marzari / SB-394 Mladen Marinov / SB-432 Filippo Gnocco / SB-470 Petr Bečička / SB-025 Olivier Donadio / SB-057 Konstantinos Xygkakis）；
法定名补全 22（SB-996 / SB-816 / SB-1092 / SB-1129 / SB-1086 / SB-1130 / SB-524 / SB-470 / SB-288 / SB-774 / SB-423 / SB-025 / SB-057 / SB-394 / SB-432 / SB-257 / SB-295 / SB-309 / SB-589 / SB-985 / SB-1011 / SB-1022）；升 A 候选 SB-589 / SB-432（回信即 A）；次候选 SB-1129 / SB-288 / SB-522 / SB-309 / SB-470 / SB-423；国别更正 0（SB-1070 研究档「波兰」有误但 entities iso 已为 SE → 不动）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 109 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- 第 1/3 ----------
    'SB-996': {'facts': {'legal_name': 'ADJ（品牌）— 进口分销主体 IoT Tecnologie s.r.l.（P.IVA / CF 04446661219；adj.it 页脚）', 'founded': '品牌 2006' + TAG,
                         'other': '第 109 批：罗马 San Cesareo 意大利 IT / 电子自有品牌（设计在意大利、中国合作厂生产；100+ ADJ Zone + 比利时 70 经销；11–50 人）→ **贴标 OEM 30% 可谈，B，一页纸一次（OEM 切口 STC-028GP / STC-228GP / STC-2224GP）**' + TAG}},
    'SB-997': {'facts': {'legal_name': 'Agmultivision s.r.l. Unipersonale（P.IVA / CF 04302850963；REA MI-1739481）', 'founded': '2004' + TAG,
                         'other': '第 109 批：米兰 Segrate 专业 AV / 多媒体增值分销商（Peerless-AV 意大利分销；MePA；股本 €30,000；11–50 人）→ **分销 20% small，一页纸一次（AV-over-IP 管理型 PoE）**' + TAG}},
    'SB-998': [{'add_kp': {'name': 'Vilius Ivanauskas', 'role': 'Komercijos direktorius（geltoni.lt / imones.lt）= 收件人（info@ 点名）' + TAG, 'email': '', 'source': 'https://rekvizitai.vz.lt/en/company/tipas/'}},
               {'add_kp': {'name': 'Vladislavas Grod', 'role': 'Direktorius（rekvizitai.vz.lt）= 拍板人' + TAG, 'email': '', 'source': 'https://rekvizitai.vz.lt/en/company/tipas/'}},
               {'facts': {'legal_name': 'AKIS Technologies, UAB（原 UAB TIPAS；įmonės kodas 120113138；PVM LT201131314）', 'founded': '1990-12-14' + TAG,
                          'other': '第 109 批：维尔纽斯排队 / 停车 / 交通管理系统制造商（16–18 人；2025 营收 €861k）→ **采购型 25% small，一页纸一次（STI 配路侧 / 停车场柜）**；不谈轨交' + TAG}}],
    'SB-1070': [{'kp_match': 'sara@safeguard.se', 'role': '研究档 KP（sara@）— 公司为 2025-03 新设壳，前身破产 → 不动' + TAG},
                {'add_kp': {'name': 'Isa Ataseven', 'role': 'Styrelseledamot（allabolag；2004 年生；替补 Eugen Ataseven）— 仅记录' + TAG, 'email': '', 'source': 'https://www.allabolag.se/foretag/safeguard-sverige-ab/norsborg/bevakningsf%C3%B6retag/2KJ9D63I5YCZJ'}},
                {'facts': {'legal_name': 'SafeGuard Sverige AB（org.nr 559523-7867；前身 SafeGuard Sweden AB 556848-7226 已于 2025 破产）', 'founded': '2025-03-18（前身 2011）' + TAG,
                           'other': '第 109 批：Norsborg 安防安装商新壳（1 人；股本 SEK 25k；董事 20 岁）；研究档国别「波兰」有误 → 瑞典（entities 已为 SE）→ **不动（前身破产新壳）**' + TAG}}],
    'SB-1129': [{'kp_match': 'ronald@redcorp.com', 'role': 'Founder（redcorp.com About；pappers.be 口径 Ronald Reich Management and Consulting）= 拍板人 / 收件人' + TAG},
                {'kp_match': 'dino@redcorp.com', 'role': 'Founder（redcorp.com About）= 收件人（抄）' + TAG},
                {'kp_match': 'danny@redcorp.com', 'role': '董事（pappers.be 口径 Daniel Lipski）' + TAG},
                {'facts': {'legal_name': 'REDCORP SA/NV（BCE / TVA BE 0448.875.715，2021-10 起；吸收原 Redcorp 0437.509.887）', 'founded': '1989-05-18（原法人）/ 1992-12-11（现法人）' + TAG,
                           'other': '第 109 批：布鲁塞尔 Saint-Gilles B2B IT 电商（营业额 €31.97M；≈49 人；Reich 家族；目录已有台系工业 IGS 系列）→ **分销 20%，B BIG，加厚一次（STI 1:1 对照 IGS）**；次候选升 A' + TAG}}],
    'SB-1130': [{'kp_name': 'Akis Lichas', 'role': 'Engineer（官网 Team）= 收件人（info@ 直呼 Akis）' + TAG},
                {'add_kp': {'name': 'Panagiotis Lichas', 'role': '负责人 / 业主（ananas.gr 名录 ΛΙΧΑΣ ΠΑΝΑΓΙΩΤΗΣ；2026-05-21 回信署名）= 拍板人（抄）' + TAG, 'email': 'info@cnstech.gr', 'source': 'https://www.cnstech.gr/about-us/'}},
                {'facts': {'legal_name': 'CNSTECH / CNS Tech（Peristeri；ΑΦΜ / ΓΕΜΗ 未取 → 部分坐实）', 'founded': '2013（活动 2007）' + TAG,
                           'other': '第 109 批：雅典小型 IT 托管 / CCTV / 布线安装商 + 小网店（在售国产 PoE；已回信）→ **集成 25% small，一页纸一次（STC-028GP / STC-228GP 对照其在售价位）**' + TAG}}],
    'SB-431': [{'kp_match': 'stefano.turrina@', 'role': '研究档 KP（protekna.it）= 收件人；amministratore 未取' + TAG},
               {'facts': {'legal_name': 'PROTEKNA S.R.L.（P.IVA / CF 03451940237；REA VR-337644）', 'founded': '2005-01-03（成立 2004-11-19）' + TAG,
                          'other': '第 109 批：维罗纳 Dossobuono 工业自动化元件分销商（Mitsubishi / Moxa / Murr / Hilscher / Mean Well 经销；6 人；2024 营收 €2.41M 下滑）→ **分销 20% small，一页纸一次（STI 作 Moxa 第二价位）**' + TAG}}],
    'SB-522': [{'kp_match': 'compras@guilera.com', 'role': '采购部（compras@）= 收件人（点名 ADILEC product manager）' + TAG},
               {'facts': {'legal_name': 'GUILERA, S.A.（CIF A08851461；Registro Mercantil de Barcelona hoja 59776）', 'founded': '1981-07-22（活动 1953）' + TAG,
                          'other': '第 109 批：巴塞罗那 Molins de Rei 汽车 / 工业电子制造商（ISO 9001 / 14001 / TS 16949），自有品牌 ADILEC 光纤传输系统（MC / FS / VC / SFP 全贴自家 logo）→ **贴标 OEM 30% 正中目标，B BIG，加厚一次（「under the ADILEC label」切口）**；汽车主业不碰' + TAG}}],
    'SB-764': [{'kp_match': 'gbillet@', 'name': 'Gilles Billet', 'role': 'Président / 创始人（pappers；1953 年生；DG = Yves-Gaël Billet）— 同行制造商 → 不动' + TAG},
               {'add_kp': {'name': 'Yves-Gaël Billet', 'role': 'Directeur général（pappers；2024 起；家族）— 仅记录' + TAG, 'email': '', 'source': 'https://www.pappers.fr/entreprise/ifotec-421531708'}},
               {'facts': {'legal_name': 'IFOTEC SAS（SIREN 421 531 708；TVA FR25421531708）', 'founded': '1999-01-02' + TAG,
                          'other': '第 109 批：Voiron 光纤传输 / 安全工业交换机制造商（INet 系列「entièrement conçu et fabriqué dans notre usine à Voiron」；20–49 人；股本 €113,335）→ **同行制造商 → 不动**' + TAG}}],
    'SB-816': {'facts': {'legal_name': 'LORWEN（品牌）— 运营主体 LAPOTECH S.R.L.S.（P.IVA 05082330654；Sarno (SA)）', 'founded': '品牌 2013' + TAG,
                         'other': '第 109 批：萨莱诺自有品牌视频监控（LW- 系列 NVR / IPC / 5 口 PoE 交换机；中国代工；意大利经销网）→ **贴标 OEM 30% 可谈 small，B，一页纸一次（STC-028GP / STC-228GP 只报 OEM 档）**' + TAG}},
    'SB-1008': [{'add_kp': {'name': 'Jari Haaparanta', 'role': 'Toimitusjohtaja / 董事（kauppalehti / finder.fi；Tanja Haaparanta 替补）= 拍板人 / 收件人（info@ 点名）' + TAG, 'email': 'info@avstek.fi', 'source': 'https://www.finder.fi/Turvaj%C3%A4rjestelm%C3%A4t/Avstek+Oy/H%C3%A4meenlinna/yhteystiedot/3101598'}},
                {'facts': {'legal_name': 'Avstek Oy（Y-tunnus 2721676-8）', 'founded': '2015-10-30' + TAG,
                           'other': '第 109 批：Hämeenlinna 安防 / 电气安装承包商兼网店（Tukes S3；1–4 人；网店 PoE 类目全为台系）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP / STI-054GP 1:1）**' + TAG}}],
    'SB-1011': {'facts': {'legal_name': 'Binär Teknik Scandinavia AB（org.nr 559181-6201；VAT SE559181620101；前身 Svensk Binär Teknik AB 556517-3753）', 'founded': '2018-11-26（前身 1995）' + TAG,
                          'other': '第 109 批：马尔默销售壳（0 雇员；发货在丹麦 Køge；董事 = Danbit 管理层 Kirsten Anette Hansen Petersen / Peter Grubb Jensen）→ **并线 SB-1022 DANBIT A/S，不单独发**' + TAG}},
    'SB-1022': [{'add_kp': {'name': 'Peter Grubb Jensen', 'role': 'Adm. direktør / 董事（krak.dk / ownr.dk）= 拍板人 / 收件人（salg@danbit.dk 点名）' + TAG, 'email': 'salg@danbit.dk', 'source': 'https://www.proff.dk/firma/danbit-as/solr%C3%B8d-strand/elektronik-og-telekommunikationsudstyr-engros/1AWPDKI10MZ'}},
                {'facts': {'legal_name': 'DANBIT A/S（Dansk Binær Teknik；CVR 78788216）', 'founded': '1985-09-26（活动 1970）' + TAG,
                           'other': '第 109 批：Køge 工业 IT / 网络分销商（7 人；FY2025-06 毛利 DKK 3.94M；把台系工业 PoE 换自家 ESW 货号卖 = 现成贴牌买家；瑞典壳 SB-1011）→ **贴标 OEM 30% 可谈 + 分销 20%，B，加厚一次（small）**' + TAG}}],
    'SB-1052': [{'add_kp': {'name': 'Hegedűs József', 'role': 'Ügyvezető（lan.hu Kapcsolat / companywall.hu；所有人 Fejes András Béláné）= 拍板人 / 收件人（sales@lan.hu 点名）' + TAG, 'email': 'sales@lan.hu', 'source': 'https://www.companywall.hu/v%C3%A1llalat/lan-kft/MMHpGT00'}},
                {'facts': {'legal_name': 'LAN Számítástechnikai Szolgáltató Kft.（adószám 10678994-2-42；cégjegyzékszám 01-09-162407）', 'founded': '1992-05-04（活动 1991）' + TAG,
                           'other': '第 109 批：布达佩斯网络 / 布线 / 机柜 / UPS 分销 + 电商 + 集成 + 施工（20–49 人；自编货号卖台系工业交换机）→ **分销 20% + 贴标可谈，B，加厚一次（small）**' + TAG}}],
    # ---------- 第 2/3 ----------
    'SB-1086': {'facts': {'legal_name': 'TEAM TELECOM SRL（CUI RO14306256；J40/9771/2001）', 'founded': '2001-11-21' + TAG,
                          'other': '第 109 批：布加勒斯特电信设备分销与集成商（8 人；2024 营业额 RON 15.97M ≈ €3.2M、净利 RON 1.52M；台系工业交换机页 + 机架 / DC）→ **分销 20% small，一页纸一次（STI 1:1 + STC-2224GP / STC-424XGGPM-280W）**' + TAG}},
    'SB-1092': {'facts': {'legal_name': 'UNIFIBRE（业务分支）— 2026-10-01 起并入 OPTOPLAST S.R.L.（rebrand Optoconnect；P.IVA 01220320665；CF 05645630632；REA TO-916276；Unifibre S.r.l. 原 P.IVA 未取）', 'founded': '1988（Optoplast；现主体登记 2007-04-23）' + TAG,
                          'other': '第 109 批：都灵光纤连接制造集团（2024 营收 €20.67M；109 人；Star Capital SGR 控股；4 厂）收购 Unifibre 光纤增值分销分支（有源类目全为台系）→ **分销 20%，B BIG，加厚一次（切口 = 并购后供应商重审）**；军工不碰' + TAG}},
    'SB-1126': [{'add_kp': {'name': 'Esa Virtanen', 'role': 'Toimitusjohtaja（proff.fi；集团子公司 CEO）— 不直接发；收件人 = CCTV Systems 事业部（info@ 点名）' + TAG, 'email': '', 'source': 'https://www.proff.fi/yrityksen/klinger-finland-oy/masala/koneet-ja-laitteet/0195519-1I10PO'}},
                {'facts': {'legal_name': 'KLINGER Finland Oy（Y-tunnus 0195519-1；KLINGER 集团）', 'founded': '1940' + TAG,
                           'other': '第 109 批：Kirkkonummi Masala 工业阀门 / 密封 / 仪表批发（2025 营收 €39.0M；115 人）+ CCTV Systems 事业部（工业 PoE 配 IP 摄像机）→ **采购型 25% small（事业部级），一页纸一次（STI 1:1）**' + TAG}}],
    'SB-1128': [{'add_kp': {'name': 'Jan Stehno', 'role': 'Jednatel / 股东（fakturujzdarma；2023-02-02 起；另 Pavel Zwinger）= 拍板人 / 收件人（点名）' + TAG, 'email': '', 'source': 'https://rejstrik.penize.cz/64053580-losan-s-r-o'}},
                {'facts': {'legal_name': 'LOSAN s.r.o.（IČO 64053580；DIČ CZ64053580；KS Ústí nad Labem C 10071）', 'founded': '1995-12-18' + TAG,
                           'other': '第 109 批：Chomutov 三店区域 IT 零售 / 电商 / 学校 IT 供应商（10–19 人；e-shop 备库台系工业交换机）→ **分销 20% small，一页纸一次（STI-288DGGPM / STI-0240GE 对照在库型号）**' + TAG}}],
    'SB-461': [{'add_kp': {'name': 'Franck Lemery', 'role': 'Jednatel（2025-05-12 起；Legrand 派驻；另 Emmanuel Regent / Yriex Dominique Roullac）— 不直接发；收件人 = product manager 网络 / 电脑配件' + TAG, 'email': '', 'source': 'https://rejstrik.penize.cz/19014104-emos-spol-s-r-o'}},
               {'facts': {'legal_name': 'EMOS spol. s r.o.（IČO 19014104；KS Ostrava C 1167；唯一股东 Legrand France S.A. 自 2024-01-01）', 'founded': '1991-07-18' + TAG,
                          'other': '第 109 批：Přerov 自有品牌消费电子 / 电工产品公司（≈400 人；集团营收 CZK 2.3bn；2022 并入 Legrand）→ **贴标 OEM 30% 低命中，B，一页纸一次（非管理 PoE 走网络配件类目）；无回声 → 不动**' + TAG}}],
    'SB-985': [{'kp_match': 'roberto.cordeiro@', 'role': '研究档 KP（qnv.com）= 收件人；administradores solidarios ×3 未具名' + TAG},
               {'facts': {'legal_name': 'QNV SL（品牌 QNV Solutions；CIF B60574779）', 'founded': '1994-05-16' + TAG,
                          'other': '第 109 批：Santa Coloma de Cervelló 工业计算 / 工业通信 / 机器视觉分销（Adlink / Korenix / Cincoze；15 人；分部 Madrid / Bizkaia / Portugal；15 次群发无回）→ **分销 20% small，一页纸一次（换切口：STI 作 Korenix 第二价位 + 交期）；再无回声 → 不动**' + TAG}}],
    'SB-015': [{'kp_match': 'info@suministros-industriales', 'role': '研究档 KP Hugo Hernàndez（曾 1 次回复）= 收件人' + TAG},
               {'add_kp': {'name': 'Silvia Pascual Fernández', 'role': 'Administradora única（BORME 2025-06-19）= 拍板人（抄）' + TAG, 'email': '', 'source': 'https://www.iberinform.es/empresa/1753516/suministros-industriales-mp4'}},
               {'facts': {'legal_name': 'SUMINISTROS INDUSTRIALES MP4 SL（CIF B63629968）', 'founded': '2004-09-28' + TAG,
                          'other': '第 109 批：Sabadell 工业用品供应商（自动化 / 条导；6 人；股本 €3,460；主业无网络类目）→ **采购型 25% small，一页纸一次（STI 配电柜一口价）；再无回声 → 不动**' + TAG}}],
    'SB-024': [{'kp_match': 'jhogye@', 'role': 'Ügyvezető（Hőgye János；ISAF 2025 到访）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'Erstech Technika Kereskedelmi és Szolgáltató Kft.（adószám 13118145-2-13；cégjegyzékszám 13-09-108843）', 'founded': '2003-09-29' + TAG,
                          'other': '第 109 批：Tatárszentgyörgy 电气安装 + 安防维护小承包商（2025 营收 HUF 27.98M ≈ €70k；jegyzett tőke HUF 8M）→ **集成 25% small，一页纸一次（按其点过的 5 口升压 + 2 光 10 电一口价）；再无回声 → 不动**' + TAG}}],
    'SB-026': [{'kp_match': 'jimmy@safe-tech.se', 'role': 'Styrelseledamot / 100% 实益人 / CEO（allabolag / bolagsfakta；1977 年生；WA 已加）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'Safe-tech CCTV Systems SWEDEN AB（org.nr 556732-8181；VAT SE556732818101）', 'founded': '2007-06-28' + TAG,
                          'other': '第 109 批：Markaryd 小型 CCTV 批发商（3 人；2024 营收 SEK 4.63M −24%、亏损；替补 Sara Mikaela Ahl）→ **分销 20% small，一页纸一次（WA 走 Simon 一口价）；再无回声 → 不动**' + TAG}}],
    'SB-046': [{'kp_match': 'info@domoticalia', 'role': 'Administrador único / 唯一雇员（BORME 2013；datoscif）— 一人网店 → 不动' + TAG},
               {'facts': {'legal_name': 'INTELIWARE SL（品牌 Domoticalia；CIF B86690344；RM Madrid H M-554995）', 'founded': '2013-03-15' + TAG,
                          'other': '第 109 批：Torrejón de Ardoz 智能家居 / 网络网店（1 名雇员；股本 €3,006；上年亏损；8 次 0 回复）→ **不动（一人网店）**' + TAG}}],
    'SB-295': [{'kp_match': 'info@wicomsolutions', 'role': '研究档 KP Alessandro Padovani = 收件人；amministratore 未取' + TAG},
               {'facts': {'legal_name': 'WI-COM SOLUTIONS S.R.L.（P.IVA / CF 07628770963；REA MB-1880777）', 'founded': '2011-11-30' + TAG,
                          'other': '第 109 批：Bovisio Masciago RF / 天线 / 连接元器件代理分销（3 人；2024 营收 €3.73M、净利 €1.44M；交换机栏目为 EN 50155 / IEC 60255 轨交 / 电力级）→ **代理型 small，一页纸一次只给非轨交工业线；无回声 → 不动**；军工 / 轨交不提' + TAG}}],
    'SB-309': [{'kp_match': 'reif@alternetivo', 'role': '股东（detail.cz：Valenta / Dolák / Reif）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'kratky@alternetivo', 'role': '研究档 KP（产品 / 采购）= 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'Alternetivo s.r.o.（IČO 25098314；DIČ CZ25098314；MS Praha C 49492）', 'founded': '1996/1997' + TAG,
                          'other': '第 109 批：布拉格网络与电信 VAD（CZ + SK；ChannelWorld 年度 VAD 2017 / 2018 / 2021；jednatelé Ondřej Valenta / Radim Dolák；**自有品牌 NNET 工业非管理 PoE**）→ **贴标 OEM 30% 可谈 + 分销 20%，B BIG，加厚一次（STI 1:1 对照 NNET）**；次候选升 A' + TAG}}],
    'SB-589': [{'kp_match': 'bydemes@bydemes.com', 'role': 'Managing Director / Administrador delegado（electrico.info 口径 Rubi Rio Ricardo；Administrador único = LAST ROUND HOLDING SL）= 拍板人' + TAG},
               {'kp_name': 'Liana Barragan', 'role': '研究档 KP = 收件人（抄）' + TAG},
               {'add_kp': {'name': 'María Gracia Guzzi', 'role': 'Directora de compras / exportaciones（electrico.info）= 收件人（compras 点名）' + TAG, 'email': '', 'source': 'https://www.electrico.info/empresa-demes-en-barcelona-32739'}},
               {'facts': {'legal_name': 'BY DEMES SL（By Demes Group；CIF B60347010）', 'founded': '1985' + TAG,
                          'other': '第 109 批：巴塞罗那 + Coslada 伊比利亚 #1 电子安防分销商（132 人；40+ 品牌 6,500 SKU；自有品牌 AIRSPACE / CCTVDIRECT；Hyundai 独家；在售 Wi-Tek / Cudy）→ **贴标 OEM 30% 正中目标，B BIG，加厚一次；回信即升 A**' + TAG}}],
    # ---------- 第 3/3 ----------
    'SB-423': [{'add_kp': {'name': 'Daniel Guez', 'role': 'Président（pappers；2025-09 起，此前 Président du directoire 2004 起；1966 年生）= 拍板人（不直接发）' + TAG, 'email': '', 'source': 'https://www.pappers.fr/entreprise/equipements-scientifiques-353579634'}},
               {'add_kp': {'name': 'Laurent Guez', 'role': 'Directeur général（pappers；2004 起；1972 年生）— 仅记录；收件人 = chef de produit réseaux via contact@es-france.com' + TAG, 'email': 'contact@es-france.com', 'source': 'https://www.pappers.fr/entreprise/equipements-scientifiques-353579634'}},
               {'facts': {'legal_name': 'EQUIPEMENTS SCIENTIFIQUES（ES France；SIREN 353 579 634；SIRET 35357963400018；SAS 自 2025-09）', 'founded': '1990-01-26（活动 1963）' + TAG,
                          'other': '第 109 批：Garches 四部门增值分销商（2025 营业额 €101.5M；101 人；ISO 9001；站内 ORing 工业线；Guez 家族；2 次群发无回）→ **分销 20%，B BIG，加厚一次（换切口：ORing 第二价位 + 付费借测）**' + TAG}}],
    'SB-009': [{'kp_match': 'info@sicurmax.com', 'role': 'Amministratore / 创始合伙人（PEC massimo.marzari@；WA 已加）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'SICURMAX S.R.L.（原 SICURMAX S.n.c. di Marzari Massimo & C.；P.IVA / CF 02360600239；REA VR-233884）', 'founded': '1992-07-01' + TAG,
                          'other': '第 109 批：Bovolone 民用 / 工业安防集成商（6 人；ISO 9001；SOA；MePA；军方 / NATO 场所资质为附带 → 守界核查通过，稿内只谈民用 / 工地）→ **集成 25% small，一页纸一次（WA 走 Simon）；再无回声 → 不动**' + TAG}}],
    'SB-257': [{'kp_match': 'gianni.scandroglio@', 'role': '研究档 KP（voxplus.it）= 收件人；amministratore 未取' + TAG},
               {'kp_name': 'Fabio Frigerio', 'role': '研究档 KP = 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'VOXPLUS S.R.L.（P.IVA / CF 05516110961；REA MI-1828564）', 'founded': '2007-01-24（成立 2006-12-19）' + TAG,
                          'other': '第 109 批：米兰 / Busto Arsizio 系统集成商（15 人；2024 营收 €1.82M；站内 Maiwe 工业交换机）→ **集成 25% small，一页纸一次（STI-054GP 对 5 口工业 PoE；STC-424XGGPM-280W 对 8×90 W + 4×10G）**' + TAG}}],
    'SB-394': [{'kp_match': 'e.slavev@', 'role': '研究档 KP（推定 Славов 家族；управител Огнян Божидаров Славов）= 收件人' + TAG},
               {'add_kp': {'name': 'Mladen Marinov', 'role': 'Управител（papagal.bg / ksb.bg 口径 Младен Георгиев Маринов；m.marinov@）= 拍板人（抄）' + TAG, 'email': 'm.marinov@maxtel.bg', 'source': 'https://papagal.bg/eik/130157325/773b'}},
               {'facts': {'legal_name': 'МАКСТЕЛ ООД（MAXTEL Ltd.；ЕИК 130157325；ДДС BG130157325）', 'founded': '1999-12-09' + TAG,
                          'other': '第 109 批：索非亚 CCTV / 门禁 / 通信 / LED 进口批发商（全国渠道；市政 CCTV 项目；股本 BGN 5,000；15 次群发无回）→ **分销 20% small，一页纸一次（换切口一口价）；再无回声 → 不动**' + TAG}}],
    'SB-432': [{'kp_match': 'fgnocco@', 'role': 'General Manager（LinkedIn）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'info@qubix.it', 'role': 'Business Developer Manager（研究档）= 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'QUBIX S.P.A.（P.IVA / CF 03575150283；REA PD-321331）', 'founded': '2001-02-01' + TAG,
                          'other': '第 109 批：帕多瓦结构化布线 / 网络 / CCTV 分销商（21 人；2025 营收 €29.72M、净利 €6.62M；股本 €300,000；几乎全线台系；BDM Caroline (Chia Ling) Lee）→ **分销 20%，B BIG，加厚一次；回信即升 A**' + TAG}}],
    'SB-470': [{'kp_match': 'hemzal@asm.cz', 'role': '研究档 KP（ASM 部门产品 / 采购）= 收件人' + TAG},
               {'add_kp': {'name': 'Petr Bečička', 'role': 'Jednatel / 股东（podnikatel.cz；Ing.；1994 起；另一股东 Martin Zavřel）= 拍板人（不直接发）' + TAG, 'email': '', 'source': 'https://rejstrik.penize.cz/60707968-100mega-distribution-s-r-o'}},
               {'facts': {'legal_name': 'ASM = 100MEGA Distribution s.r.o.（IČO 60707968；DIČ CZ60707968；KS Brno C 15317）', 'founded': '1994-05-24' + TAG,
                          'other': '第 109 批：布尔诺大型 IT 分销商（100–149 人；营业额前 0.5%；股本 CZK 12.96M）的安装商 / 集成商 ICT 渠道部门 ASM（布拉格；台系 61 / Dahua 105）→ **分销 20%，B BIG，加厚一次（STI + STC 1:1）**' + TAG}}],
    'SB-524': [{'kp_match': 'info@armadi-rack', 'role': '业主（reteimprese 口径 Luciani Massimiliano）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Alfredo Marmone', 'role': '研究档 KP = 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'Armadi-Rack.it（品牌 / 网店）— 运营主体 M.D.W. srl（P.IVA / CF 02766841205；REA BO-465866）', 'founded': '未取' + TAG,
                          'other': '第 109 批：博洛尼亚 Casalecchio di Reno 19 寸机柜 / 电子外壳制造 + 网店（交换机栏目卖 Digitus / Utepo 贴牌货）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP / STI-054GP 1:1）**' + TAG}}],
    'SB-201': {'facts': {'legal_name': 'EL.SI. S.R.L.（P.IVA / CF 01536710799；REA KR-118653）', 'founded': '1985-10-18' + TAG,
                         'other': '第 109 批：Crotone 南意安防 / 自动化区域分销商（16 人；2025 营收 €3.91M、净利 €25k，2024 亏损；股本 €93,600；Amministratore Unico 未具名）→ **分销 20% small，一页纸一次（STC PoE 配 CCTV 线）**' + TAG}},
    'SB-288': [{'add_kp': {'name': 'Michael Taraba', 'role': 'Präsident des Verwaltungsrats / 集团创始人（moneyhouse / prospex；另 Hans Walbert / Roland Silvestri / Hans Rudolf Merz）= 拍板人（不直接发；收件人 = ROLINE 产品经理 via info@secomp-international.com）' + TAG, 'email': 'info@secomp-international.com', 'source': 'https://www.moneyhouse.ch/en/company/secomp-international-ag-12957629611'}},
               {'facts': {'legal_name': 'SECOMP International AG（UID CHE-112.622.278；CH-170.3.028.825-9；关联 SECOMP AG CHE-211.141.887 / SECOMP Electronic Components GmbH HRB 361374 Ettlingen）', 'founded': '集团 1988（瑞士主体 ≤2013）' + TAG,
                          'other': '第 109 批：Bassersdorf 国际贸易主体（集团 ≈250 人；中央仓 Ettlingen；分支 FR / NL / CZ；自有品牌 ROLINE / VALUE；已从国内多家采购含 HRUI；6 次群发无回）→ **贴标 OEM 30% 正中目标，B BIG，加厚一次（换切口：ROLINE 标 PoE 系列补齐 + 德国仓 DAP）**；次候选升 A' + TAG}}],
    'SB-774': [{'add_kp': {'name': 'Sandra Meijer', 'role': '联系人 / 经营者（qshops；创始人 Marcel Meijer 已故）= 收件人（klantenservice@ 点名）' + TAG, 'email': 'klantenservice@netwerkproducten.com', 'source': 'https://www.netwerkproducten.com/service/over-ons'}},
               {'facts': {'legal_name': 'MP2 Netwerkproducten B.V.（KvK 62165984；BTW NL8546.95.667B01）', 'founded': '2014-12-23（活动 2002 / 1996）' + TAG,
                          'other': '第 109 批：Houten 网络产品网店（2 人；机柜 / 线缆 / 交换机 / 光纤；15 次群发无回）→ **分销 20% small，一页纸一次（换切口一口价 + 荷兰 DAP）；再无回声 → 不动**' + TAG}}],
    'SB-014': [{'kp_match': 'vicente.jimenez@', 'role': '用户表 KP（intecseg.com；WA 已加；20 次 0 回复）— 公司同一性未证实 → 不动' + TAG},
               {'facts': {'legal_name': 'Intec Seguridad（「ITS, S.L. - S.B.T.」）— 候选法人 INTEC SEGURIDAD MENORCA SL（CIF B57518151；Ciutadella de Menorca）；域名 intecseg.com 与该法人同一性未证实 → 部分坐实', 'founded': '2007-08-10（候选法人）' + TAG,
                          'other': '第 109 批：候选法人 = 梅诺卡岛微型安防安装商（警察登记 3451；0–10 人；CNAE 4321 / 8010）→ **不动（未证实 + 20 次 0 回复）**；Vicente 在 WA 主动开口再谈预付款小单' + TAG}}],
    'SB-025': [{'kp_match': 'odonadio@', 'role': 'Président（pappers；2016-07 起；1980 年生）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'SIPE – Société Insulaire de Protection Electronique SAS（SIREN 814 329 462；SIRET 81432946200034；TVA FR39814329462；RCS Ajaccio）', 'founded': '2015-10-01（活动 1985）' + TAG,
                          'other': '第 109 批：阿雅克肖安防安装商（10–19 人；APSAD 三认证；Collectivité de Corse 框架合同；只要 3 个工业 PoE 配件；5 次无实质回复）→ **集成 25% small，一页纸一次（STI-054GP / STI-144GP 一口价 + MOQ 1）；再无回声 → 不动**' + TAG}}],
    'SB-057': [{'kp_match': 'info@rfcom.gr', 'role': 'Διαχειριστής / 业主（findbiz；Ο.Ε. 合伙；WA 在线）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'ΞΥΓΚΑΚΗΣ ΚΩΝΣΤΑΝΤΙΝΟΣ ΗΛ. Ο.Ε.「RFCOM」（ΑΦΜ 未取；ΓΕΜΗ 601010939512 推定 → 部分坐实）', 'founded': '2008' + TAG,
                          'other': '第 109 批：塞萨洛尼基 Σταυρούπολη 安防 / 通信 / 天线 / Z-Wave 进口分销商（NACE 4650；回过 2 次信）→ **分销 20% small，一页纸一次（WA 走 Simon 一口价 + MOQ 1）；成单再加厚**' + TAG}}],
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
