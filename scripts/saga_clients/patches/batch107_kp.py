#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 107 批（T29-U100，公司底数第二十五轮 · 欧洲其他国家 B 池第 1 轮 24 户：IT 10 / CZ 4 / ES 2 / LT 2 / FR 1 / BE 1 / BG 1 / CY 1 / PT 1 / RS 1；其中 SB-449 实为美国）：把官方 / 准官方登记核出来的「老板 / 法定名 / 成立日」回写研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=107 行）。
结构同 batch106_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 30% 目标 · B BIG · 加厚一次 6（SB-448 BETTINI S.R.L. 1996 €8.94M / 42 人 GAMS 标已贴中国交换机 → 升 A 候选 / SB-449 BV USA LLC **美国伊利诺伊**（研究档误记意大利 → country_fix 美国）自有 BV-Tech 标 PoE 交换机 → 升 A 候选 / SB-159 EL.MO. S.p.A. 1976 €30.57M / 79 人 CCTV 线配中国交换机 → 升 A 候选 /
SB-358 KYOLIS SAS 2010 自有 logo 法国品牌商 次候选 / SB-095 Mtechnology 自贴标 MT-TP7 工业 PoE 次候选（法人名未取）/ SB-326 PROXEET LIMITED ΗΕ 437925 自有 Chiprian L3 标 次候选）；
贴标可谈 + 分销 20% 加厚 3（SB-073 A.N.B. RIMEX SA 1983 自产报警主机 small / SB-1000 Alpha Elettronica S.r.l. 1975 自有品牌电源厂 B BIG / SB-244 Innowatt = GRUPPO COSOLA S.R.L. 自有标网店 small）；
分销 20% 加厚 3（SB-198 Katalita UAB 1995 6 人做 €6.86M 的 MikroTik / Ubiquiti 批发 B BIG / SB-128 Órbita Digital = CONEXIÓN B2B 2005 S.L. 跨境网店 small / SB-425 GSG INTERNATIONAL S.R.L. 1997 VAD CEO 直达 small）；
集成 25% 加厚 1（SB-048 ALMAKS DOO BEOGRAD 1992 51–100 人 2012 老成单 → B BIG 次候选）；采购型加厚 small 1（SB-1066 UAB Elseta 2006 RTU 厂，原 PRAMONINIS RYŠYS）；
一页纸一次 · 有回声再加厚 4（SB-1033 Garma Electrónica S.L. N-Tron 代理 / SB-101 АВИКАМ ЕООД 2 人家族 / SB-492 SISTEL S.R.L. 1986 布线整包 / SB-625 Virtware Lda. 2003 老板直达）；
一页纸一次 → 不动 6（SB-908 CT Service di Cerino Gianluca 个体 / SB-036 Inthouse Systems s.r.o. 软件公司 / SB-261 RecTec servis s.r.o. 回收产线 / SB-311 DIPOL 捷克站 = TOMI CZECH s.r.o. 选品在 Kraków、与 SB-1023 同集团 / SB-197 Intellisystem Technologies S.r.l. 2–5 人 / SB-012 XCAM CZech s.r.o. 一人公司）。
坐实 20 / 部分坐实 4（SB-1033 无 CIF / SB-449 IL 文件号未取 / SB-095 法人名未取 / SB-244 REA 未取）/ 未坐实 0；
KP 坐实 = 老板 / CEO / 创始人本人 8（SB-358 Eleaume + Manuse / SB-448 Walter Bettini / SB-425 Paveri Fontana / SB-625 Augusto Oliveira / SB-048 Maksimović 父子 / SB-197 Cristian Randieri（研究档误作 Walter）/ SB-261 Viktor Fojt jednatel / SB-198 Zubenas 家族）；国别更正 1（SB-449 意大利 → 美国）；
法定名补全 9（SB-449 / SB-128 / SB-244 / SB-311 / SB-492 / SB-908 / SB-012 / SB-1066 / SB-101）；升 A 候选 3（SB-448 / SB-449 / SB-159，回信即 A；次候选 SB-358 / SB-095 / SB-326 / SB-048）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 107 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- 第 1/3 ----------
    'SB-073': [{'kp_match': 'it@anb-rimex.be', 'name': 'Ibrahim Tiryaki', 'role': 'Product Manager CCTV（用户表）= 收件人' + TAG},
               {'add_kp': {'name': 'Philippe Stas', 'role': 'Administrateur + 日常管理负责人（2022 起；BCE）= 拍板人（抄 info@ 点名）' + TAG, 'email': '', 'source': 'https://www.companyweb.be/en/0424592259/a-n-b-rimex'}},
               {'facts': {'legal_name': 'A.N.B. RIMEX SA / NV（BCE / TVA BE 0424.592.259；Herstal）', 'founded': '1983-07-26' + TAG,
                          'other': '第 107 批：列日 Herstal 安防 / 楼宇自动化设备制造商（自有 TriCom 报警主机；NACE 2630 + 4652）+ CCTV / 门禁分销；股本 €75,000；12.7 FTE；INCERT 认证 → **贴标 OEM 30% 可谈（AnB 标 PoE 交换机进其 CCTV 套装）+ 分销 20%，B，加厚一次（small）**' + TAG}}],
    'SB-1033': {'facts': {'legal_name': 'Garma Electrónica S.L.（圣塞巴斯蒂安 Calle Oyarzun 1 Bajo；CIF 未取 → 部分坐实）', 'founded': '未取（自述 20+ 年）' + TAG,
                          'other': '第 107 批：工业仪表 / 过程控制分销商（Red Lion / N-Tron NT5000 工业交换机代理、FEMA、Scaime、Helmholz、Finetek）→ **STI 工业线作「第二价位」：分销 20% small，一页纸（1:1 对照 NT5000 价位）一次，有回声再加厚**；稿内不点名 Red Lion / N-Tron' + TAG}},
    'SB-101': [{'add_kp': {'name': 'Georgi Kolev（Георги Атанасов Колев）', 'role': 'Управител / 50% 股东（papagal.bg）= 拍板人 / 收件人（sales@avicam-bg.com）' + TAG, 'email': 'sales@avicam-bg.com', 'source': 'https://papagal.bg/eik/175335234/8e85'}},
               {'facts': {'legal_name': 'АВИКАМ ЕООД / Avicam Ltd.（ЕИК 175335234；ДДС BG175335234；София）', 'founded': '2007（法人）；品牌 2001' + TAG,
                          'other': '第 107 批：索菲亚 2 人家族安防进口分销 + 安装（RaySharp 保加利亚代表；自有 AVICAM 配件标；2020 营业额 €160k；Колев 父子各 50%）→ **分销 20% small，一页纸（STC-028GP / STC-228GP 配其套装）一次；小批量贴标一句带过**' + TAG}}],
    'SB-1000': [{'add_kp': {'name': 'Mauro Salsi', 'role': '创始人（1975；官网 Storia）= 拍板层（收件人 commerciale@ 点名 ufficio acquisti）' + TAG, 'email': 'commerciale@alphaelettronica.com', 'source': 'https://test.alphaelettronica.com/storia'}},
                {'facts': {'legal_name': 'Alpha Elettronica S.r.l.（P.IVA / CF 01511860346；REA PR-159233；Collecchio PR）', 'founded': '1975' + TAG,
                           'other': '第 107 批：帕尔马电源 / 变压器制造商 + 自有品牌电子电气配件分销（品类含网络 / PoE 交换机；股本 €46,500；≈21 人；2015 新总部）→ **贴标 OEM 30% 可谈（Alpha 标 PoE 交换机走其电源同渠道）+ 分销 20%，B BIG，加厚一次**' + TAG}}],
    'SB-1066': [{'add_kp': {'name': 'Matas Doviltis', 'role': 'Vadovas / 负责人（rekvizitai.lt）= 拍板人（收件人 info@ 点名）' + TAG, 'email': '', 'source': 'https://rekvizitai.vz.lt/en/company/elseta/'}},
                {'facts': {'legal_name': 'UAB „Elseta“（原 UAB „PRAMONINIS RYŠYS“ 2013–2018；įmonės kodas 300564737；PVM LT100003358919；Vilnius）', 'founded': '2006-05-02' + TAG,
                           'other': '第 107 批：维尔纽斯工业 / 变电站自动化制造商（Mini RTU、数据集中器；Aedilis 研发部拆分；股本 €173,760；≈22 人）+ 工业通信网店 pramoninisrysys.lt → **采购型 25%（RTU 柜配工业交换机）+ 网店分销 20%，B，加厚一次（small）；守界不提 IEC 61850**；国别 立陶宛（已 country_fix）' + TAG}}],
    'SB-358': [{'kp_match': 'stephane.manuse@kyolis.com', 'name': 'Stéphane Manuse', 'role': 'Directeur général（2024-06 起；联合创始人 / 技术）= 收件人' + TAG},
               {'kp_name': 'Thomas Eleaume', 'role': 'Président（2011 起；联合创始人；societe.com）= 拍板人（抄送）' + TAG},
               {'facts': {'legal_name': 'KYOLIS SAS（SIREN 519 722 698 RCS Nanterre；TVA FR00519722698；Antony，工厂 Chambéry）', 'founded': '2010-01-22' + TAG,
                          'other': '第 107 批：法国光纤 / 同轴以太网传输设备与工业交换机品牌商（自有 logo；Chambéry 2023 投产；股本 €100,000；6–9 人；pappers 标注 1 项登记程序，性质未查）→ **贴标 OEM 30% 目标（Kyolis 标导轨工业 PoE / 光口机补其 SKU）+ 分销 20%，B BIG，加厚一次；升 A 次候选**' + TAG}}],
    'SB-448': [{'kp_match': 'walter.bettini@bettinivideo.com', 'name': 'Walter Bettini', 'role': 'Amministratore Delegato / 联合创始人（1996，与兄弟 Massimo）= 拍板人（抄送）' + TAG},
               {'kp_match': 'info@bettinivideo.com', 'name': 'Marco Contu', 'role': 'Product Manager（研究档）= 收件人' + TAG},
               {'kp_name': 'Giuseppe Costantini', 'role': 'Purchasing Manager（研究档）= 抄送' + TAG},
               {'facts': {'legal_name': 'BETTINI S.R.L.（P.IVA / CF 11883080159；REA MI-1506925；注册 Milano，运营 Saronno VA）', 'founded': '1996-09-23' + TAG,
                          'other': '第 107 批：意大利视频监控方案商 / 制造商（自有 GAMS 品牌；2025 营收 €8.94M；42 人；分部 Firenze / Roma / Bologna；表内「用 ONV 的直接带标卖」）→ **贴标 OEM 30% 目标，B BIG，加厚一次；升 A 候选（回信即 A）**；稿内不点名 ONV / ComNet' + TAG}}],
    'SB-449': [{'kp_match': 'support@bvsecurity.com', 'name': 'Zehua W', 'role': 'Product Manager / 技术客服（研究档）→ 改投 sales@ 点名业主' + TAG},
               {'add_kp': {'name': 'Lisa Tsai', 'role': 'Co-Managing Director / Owner（ZoomInfo）= 拍板人 / 收件人（sales@bvsecurity.com）' + TAG, 'email': 'sales@bvsecurity.com', 'source': 'https://www.zoominfo.com/c/bv-security/22367373'}},
               {'add_kp': {'name': 'Chien Chang Lu', 'role': 'Managing Member（buzzfile；BV USA LLC）= 拍板人' + TAG, 'email': '', 'source': 'https://www.buzzfile.com/business/BV-Security-847-619-2288'}},
               {'country_fix': '美国'},
               {'facts': {'legal_name': 'BV USA LLC（d/b/a BV Security；伊利诺伊 Elk Grove Village；IL 文件号未取 → 部分坐实）', 'founded': '2009' + TAG,
                          'other': '第 107 批：**美国伊利诺伊（研究档误记意大利 → country_fix 美国）**；PoE 交换机 / 注入器 / 摄像机批发商，自称 OEM/ODM，自有品牌 BV-Tech（POE-SW802G 等亚马逊热销）；GeoVision 经销；7–11 人；华裔业主 → **贴标 OEM 30% 目标（其 SW802G 类机型正是 STC-028GP / STC-228GP 的贴标对象），B BIG，加厚一次；升 A 候选（回信即 A）**；中文直联 Simon 定（默认否）；发信窗口 Wed 08–10 CT' + TAG}}],
    # ---------- 第 2/3 ----------
    'SB-198': [{'kp_match': 'robertas@katalita.lt', 'name': 'Robertas Zubenas', 'role': 'CFO（用户表；与负责人同姓 → 家族）= 收件人' + TAG},
               {'add_kp': {'name': 'Donatas Zubenas', 'role': 'Vadovas / 负责人（rekvizitai / imoniubaze）= 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://rekvizitai.vz.lt/en/company/katalita/'}},
               {'facts': {'legal_name': 'Katalita, UAB（įmonės kodas 134637695；PVM LT346376917；Kauno r. Neveronys）', 'founded': '1995-12-18' + TAG,
                          'other': '第 107 批：ICT / 网络设备纯批发商（MikroTik / Ubiquiti 官方 reseller / Teltonika / TP-Link；6–8 人做 2025 营收 €6.86M；Extralink 非其品牌）→ **分销 20%，B BIG，加厚一次**；稿内不点名 MikroTik / Ubiquiti' + TAG}}],
    'SB-095': {'facts': {'legal_name': 'Mtechnology（注册商标 / Divisione Italiana；P.IVA 02451810960 站脚；法人全名未取 → 部分坐实）', 'founded': '未取' + TAG,
                         'other': '第 107 批：面向工业 / 极端环境的 AI 视频监控品牌商，**自有型号工业 PoE 交换机 MT-TP7-16GT240BT / MT-TP7308POE / MT-TP7324GE-POE / MT-TP7224E-POE（Utepo 式）**，只经认证安装商销售（Gamma Commerciale 载其价表）→ **贴标 OEM 30% 正中目标，B BIG，加厚一次；升 A 次候选**；法人名 / 所在地待补证' + TAG}},
    'SB-244': {'facts': {'legal_name': 'GRUPPO COSOLA S.R.L.（Innowatt 为其自有品牌网店；P.IVA 01218230777 站脚；REA 未取 → 部分坐实）', 'founded': '未取' + TAG,
                         'other': '第 107 批：电气 / 安防 / 网络材料电商（视频监控 772 件、网络 295 件；配件贴 INNOWATT 标）+ 技术安装集团 → **贴标 OEM 30% 可谈（小批量）+ 分销 20%，B，加厚一次（small）**；12 次群发无回复 → 二次触达必须换切口' + TAG}},
    'SB-492': {'facts': {'legal_name': 'SISTEL S.R.L.（Sistel Networking 事业部；P.IVA / CF 01164230037；REA NO-153233；Suno NO）', 'founded': '1986-05-28' + TAG,
                         'other': '第 107 批：诺瓦拉电子元件制造商兼网络方案部（布线 / 机柜 / UPS / 台系工业交换机整包；2024 营收 €1.70M、净利 €206k）→ **集成 25%，B，一页纸一次（STI 1:1 对照 IGS-620TF 类）；有回声再加厚**' + TAG}},
    'SB-908': [{'add_kp': {'name': 'Gianluca Cerino', 'role': 'Titolare（个体工商户业主）= 唯一收件人（info@techlu.it）' + TAG, 'email': 'info@techlu.it', 'source': 'https://www.informazione-aziende.it/Azienda_CT-SERVICE-DI-CERINO-GIANLUCA'}},
               {'facts': {'legal_name': 'CT Service di Cerino Gianluca（impresa individuale；P.IVA 01771320700；CF CRNGLC67L29L483I；Campobasso）', 'founded': '未取（3–10 年）' + TAG,
                          'other': '第 107 批：坎波巴索 1 人安防门店 + Techlu 安装商网店（已卖 ONV 式商用 PoE）→ **分销 20% small，一页纸一次；无回声 → 不动**' + TAG}}],
    'SB-326': [{'kp_match': 'marketplace@proxeet.com', 'name': 'Marina Shkarpetina', 'role': 'Marketplace（用户表 RFQ）= 收件人' + TAG},
               {'add_kp': {'name': 'Aleksei Kizriakov', 'role': 'Director（Registrar of Companies）= 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://companiesregistry.cy/company-details/proxeet-limited-437925/'}},
               {'facts': {'legal_name': 'PROXEET LIMITED（ΗΕ 437925；Pafos）', 'founded': '2022-08-31' + TAG,
                          'other': '第 107 批：帕福斯 ISP 网络设备品牌商（**自有 Chiprian L3 管理交换机 + iBlock 便携 PoE 注入器**；俄籍创始团队，董事 Kizriakov + Tikhonov（后者为公司服务商兼秘书）；11–50 口径）→ **贴标 OEM 30% 目标，B BIG，加厚一次；升 A 次候选**；塞浦路斯 EU 法人，正常 T/T；不碰俄方背景话题' + TAG}}],
    'SB-036': [{'add_kp': {'name': 'Matej Snoha', 'role': 'Jednatel / 创始人 / 实益所有人（2017 起；or.justice.cz）= 拍板人 / 收件人' + TAG, 'email': '', 'source': 'https://rejstrik.penize.cz/05405947-inthouse-systems-s-r-o'}},
               {'add_kp': {'name': 'Andrej Hraško', 'role': 'Jednatel / 实益所有人（2016 起）' + TAG, 'email': '', 'source': 'https://rejstrik.penize.cz/05405947-inthouse-systems-s-r-o'}},
               {'facts': {'legal_name': 'Inthouse Systems s.r.o.（IČO 05405947；C 263202 MSPH；Praha 5）', 'founded': '2016-09-19' + TAG,
                          'other': '第 107 批：布拉格楼宇自动化软件 / 云网关公司（≈4 人；注册资本 2,000 Kč；两名斯洛伐克创始人）→ **采购型 25% tiny，一页纸一次；无回声 → 不动**' + TAG}}],
    'SB-261': [{'kp_match': 'fojt@rectec.cz', 'name': 'Viktor Fojt', 'role': 'Jednatel（2023 起；KS Brno C 132302）= 拍板人 / 收件人本人' + TAG},
               {'facts': {'legal_name': 'RecTec servis, s.r.o.（IČO 17957036；DIČ CZ17957036；Židlochovice；100% CVFT s.r.o.）', 'founded': '2023-01-23' + TAG,
                          'other': '第 107 批：回收生产线 / 工业自动化供应商（注册资本 200,000 Kč；2023 阿里巴巴 RFQ 为光模块，Saga 不做）→ **项目 25% small，一页纸一次（STI 导轨机进产线柜）；无回声 → 不动**' + TAG}}],
    # ---------- 第 3/3 ----------
    'SB-311': {'facts': {'legal_name': 'TOMI CZECH, s.r.o.（DIPOL 捷克站；IČO 26830370；DIČ CZ26830370；Přerov）', 'founded': '未取' + TAG,
                         'other': '第 107 批：波兰 DIPOL（Kraków；2026-06-10 改制 DIPOL sp. z o.o.）集团的捷克销售公司（3 门店；Hikvision / Dahua / TP-Link 目录）→ **分销 20% 但选品在 Kraków 总部：一页纸一次并请转 orders@dipolnet.com；与 SB-1023 DIPOL 葡萄牙并线记一笔；无回声 → 不动**' + TAG}},
    'SB-128': {'facts': {'legal_name': 'CONEXIÓN B2B 2005, S.L.（Órbita Digital；CIF B74173303；Oviedo）', 'founded': '2004（网店 2009）' + TAG,
                         'other': '第 107 批：阿斯图里亚斯电信 / 网络 / 安防分销 + 跨境网店（Triax / Televes / Ikusi / Hikvision / Ubiquiti；曾上架 Utepo 类交换机；自称发货 184 国）→ **分销 20%，B，加厚一次（small）；MOQ 1 + 15 天有效价对网店友好**' + TAG}},
    'SB-159': [{'kp_match': 'agostino.avolio@elmospa.com', 'name': 'Agostino Avolio', 'role': 'Technical / Commercial Agent（研究档）= 收件人（代理，非采购 → 抄 info@ 点名 Ufficio Acquisti）' + TAG},
               {'facts': {'legal_name': 'EL.MO. S.p.A. a socio unico（P.IVA / CF 00605640283；REA PD-126325；Campodarsego PD）', 'founded': '1976' + TAG,
                          'other': '第 107 批：帕多瓦专业安防系统制造商（入侵 EN 50131 / 门禁 / CCTV / 无线；经销商 / 安装商渠道；股本 €3M；2025 营收 €30.57M、净利 €1.49M；79 人；表内「CCTV 帧田交换机」）→ **贴标 OEM 30% 目标（EL.MO. 标 PoE 交换机进其 CCTV 目录），B BIG，加厚一次；升 A 候选（回信即 A）**' + TAG}}],
    'SB-197': [{'kp_match': 'randieri@intellisystem.it', 'name': 'Cristian Randieri', 'role': 'President & CEO / 创始人（官网 About Us；研究档误作 Walter Randieri）= 拍板人 / 收件人本人' + TAG},
               {'kp_match': 'info@intellisystem.it', 'name': 'Clelia Rizza', 'role': 'Founding Board Member（官网 About Us；研究档误作 Clelia Randieri）= 抄送' + TAG},
               {'facts': {'legal_name': 'Intellisystem Technologies S.r.l.（P.IVA / CF 01424300893；Siracusa；REA 未取）', 'founded': '2000（事务所）/ 2003（S.r.l.）' + TAG,
                          'other': '第 107 批：锡拉库萨 2–5 人工业网络 / 监控 / 自动化方案商（在售 3onedata 工业交换机；营收 <€0.25M 口径）→ **分销 20% small，一页纸一次（STI 1:1 对照 3onedata 同口数）；无回声 → 不动**' + TAG}}],
    'SB-425': [{'kp_match': 'ludovico.paveri@gsginternational.com', 'name': 'Ludovico Paveri Fontana', 'role': 'Amministratore Delegato / CEO（2017 起，前 CTO）= 拍板人 / 收件人本人' + TAG},
               {'add_kp': {'name': 'Antonmarco Catania', 'role': 'Chairman / 创始人（1997；兼 Euklis srl 2017）' + TAG, 'email': '', 'source': 'https://www.gsginternational.com/it/team.html'}},
               {'facts': {'legal_name': 'GSG INTERNATIONAL S.R.L.（P.IVA / CF 12178170150；REA MI-1537545；Trezzano sul Naviglio MI）', 'founded': '1997-06-12' + TAG,
                          'other': '第 107 批：米兰安防增值分销商（barox / ComNet / Lantech / Nedap；姊妹制造商 Euklis；股本 €53,700；2024 营收 €2.37M、净利 €308；7 人）→ **分销 20%，B，加厚一次（small）；Euklis 贴标 30% 一句带过；强调毛利空间**' + TAG}}],
    'SB-625': [{'kp_match': 'augusto@virtware.pt', 'name': 'Augusto Oliveira', 'role': 'Owner / sócio-gerente（用户表 + LinkedIn）= 拍板人 / 收件人本人' + TAG},
               {'facts': {'legal_name': 'VIRTWARE – Soluções Integradas de Telecomunicações, Lda.（NIPC 506612813；Vila Nova de Gaia）', 'founded': '2003-05-19' + TAG,
                          'other': '第 107 批：波尔图网络 / 布线增值分销商（Cat.6a 布线、TP-Link L2、兼容光模块、机柜、VoIP；股本 €5,000；2–10 人）→ **分销 20% small，一页纸一次（对照 TL-SG5428 类价位）；有回声再加厚**；表内从未跟进 → 首封不伪造 Re:' + TAG}}],
    'SB-048': [{'kp_match': 'smaksimovic@almaks.rs', 'name': 'Slobodan Maksimović', 'role': 'Vlasnik i direktor（100%；1992 创始）= 拍板人 / 收件人本人' + TAG},
               {'add_kp': {'name': 'Uroš Maksimović', 'role': 'Direktor（二代；companywall）= 抄送' + TAG, 'email': '', 'source': 'https://www.companywall.rs/firma/almaks-doo-beograd/MMfjjXsD'}},
               {'facts': {'legal_name': 'ALMAKS DOO BEOGRAD（Almaks Security Systems；МБ 06698182；ПИБ 100571552；Beograd-Vračar）', 'founded': '1992-06-15' + TAG,
                          'other': '第 107 批：贝尔格莱德安防系统集成商（报警 / 视频 / 灭火 / 门禁 / 周界；51–100 人；子公司 ALMAKS GPS 2017；**2012-03 成交 20 对 1V1D 光端机，老成单**）→ **集成 25%，B BIG，加厚一次；升 A 次候选（回信即 A）**；开头引 2012 那单须 S-box 有记录' + TAG}}],
    'SB-012': [{'add_kp': {'name': 'Alexandr Grepl', 'role': 'Jednatel（唯一；2012 起；obchodní rejstřík）= 拍板人 / 收件人' + TAG, 'email': '', 'source': 'https://rejstrik.penize.cz/29397839-xcam-czech-s-r-o'}},
               {'facts': {'legal_name': 'XCAM CZech s.r.o.（IČO 29397839；DIČ CZ29397839；Ostrava）', 'founded': '2012-02-29' + TAG,
                          'other': '第 107 批：俄斯特拉发一人安防集成 / 安装商（CCTV / 报警 / 车牌识别 / 光伏电站监控；Jablotron / AXIS；已用 E-link 类 PoE）→ **集成 25% small，一页纸一次（STI-054GP 对光伏 / 道闸场景）；9 次无回复 → 不动**' + TAG}}],
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
