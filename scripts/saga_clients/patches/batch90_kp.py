#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 90 批（T29-U72，公司底数第八轮 · B 档四主攻国 TR / US-CA / DE 为主 + 其它 13 国，37 户 / 14 国 + 2 户未命中）：把官方 / 准官方登记核出来的「老板 / 董事 / 股权 / 规模 / 财务 / 同行与守界判定」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=90 行）。
结构同 batch89_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts。
本批附带 Q-65 国别更正（country_fix 已写入研究档，见 docs/国别机检_Q-65_2026-10-27.md）：SB-538 加拿大 / SB-771 哥斯达黎加 / SB-1136 美国。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 90 批 官方登记核实 2026-10-27）'
ND = 'https://www.northdata.de/'
ABR = 'https://abr.business.gov.au/ABN/View?abn='
UPD = {
    # ---------- TR ----------
    'SB-294': [{'kp_name': 'İsmet Yavuz', 'role': '业主（LinkedIn「Viva Bilgisayar」；Defne / Hatay 一人电脑 + 安防店，推定 şahıs 个体）= **老板 = 联系人**；**同名陷阱：İstanbul 的 Viva Bilgisayar 非本户**' + TAG},
               {'facts': {'founded': '未取（LinkedIn 2016 起有活动；Ticaret Sicil 未命中 = 推定个体户）' + TAG, 'size': '微型（业主 + 数人）' + TAG, 'hq': 'Sümerler Mah. 16. Sk. No:16/3, Defne / Hatay（2023 地震区）' + TAG}}],
    'SB-389': [{'kp_match': 'eskisehir@hiperonline.com', 'role': 'Eskişehir 分部信箱（.com 已死 → **公司活着，官网 / 邮箱在 hiperonline.com.tr**；Q-64 死域名单移出）—— 下一封写 info@ / teknik@ @hiperonline.com.tr 问 Teknik Müdür' + TAG},
               {'facts': {'legal_name': 'HİPERONLİNE İLETİŞİM HİZMETLERİ SANAYİ TİCARET LİMİTED ŞİRKETİ（Vergi No 3330751186，Gaziemir / İzmir；AS216192，自有 IP 1,536 个）', 'founded': '2014（官网）' + TAG, 'staff': '小型 ISP（估 10–30 人；数千用户级）' + TAG, 'size': '小型 ISP' + TAG, 'hq': 'İzmir（总部）+ Eskişehir 分部' + TAG}}],
    'SB-467': [{'kp_name': 'Bayram Tatlı', 'role': '推定业主 / 经理（职务未核；Antalya Muratpaşa 酒店 / 住宅 弱电集成商，法定类型未取）—— 24 口 PoE 酒店场景写他' + TAG},
               {'facts': {'hq': 'Varlık Mah. Piri Reis Cad. No:19/B, Muratpaşa / Antalya' + TAG, 'size': '小型（估 5–15 人）' + TAG}}],
    'SB-686': [{'kp_match': 'info@teknoktadestek.com', 'name': 'Rıfat Yıldız', 'role': '业主（官网 sameAs 指向其个人 X 账号；研究档原记「Rıfat Bende」为误读）= **老板 = 联系人**；İnegöl / Bursa 两店 + 安装队' + TAG},
               {'facts': {'hq': 'Fatih Mh. Kıvırcık Sk. No:9/1, İnegöl / Bursa' + TAG, 'size': '微型 / 小型（两店 + 安装队；估 5–10 人；推定 şahıs）' + TAG}}],
    'SB-280': {'facts': {'legal_name': 'METCOM GÜVENLİK TEKNOLOJİLERİ A.Ş.（VKN 6190579359，Şişli；Perpa Ticaret Merkezi A Blok Kat:7-8 No:703-707）', 'founded': '2017-01-04（vknsorgula；品牌可能更早）' + TAG, 'staff': '车牌识别 / 停车场系统集成 + 自有软件；İstanbul 总部 + Ankara / İzmir 网点' + TAG, 'size': '小型（估 10–30 人）' + TAG, 'hq': 'Şişli / İstanbul（Perpa）' + TAG, 'other': '每个停车出入口 = 摄像机 + 道闸 + 户外机柜工业 PoE → 集成 25%，STI-054GP / STI-154GP' + TAG}},
    'SB-283': [{'kp_match': 'ibrahim@oncuguvenlik.com.tr', 'role': '姓氏 / 职务待核 —— 公司 = **伊斯坦布尔 1,500+ 经销商的安防总批发（100–200 人，$10–50M 级，与 Bimel 同量级）** → 请他转 ağ ürünleri ürün müdürü；分销 20% + 自有标签 OEM 30% 可选' + TAG},
               {'facts': {'legal_name': 'ÖNCÜ GÜVENLİK SİSTEMLERİ A.Ş.（VKN 6560323830，Beykoz；现 A.Ş. 主体 2014-12-04）', 'founded': '2002（业务）/ 2014-12-04（现 A.Ş.）' + TAG, 'staff': '51–200（LinkedIn）/ 100–200（signalhire）；1,500+ bayi；营收估 $10–50M（量级）' + TAG, 'size': '中型（全国安防批发）' + TAG, 'hq': 'Kavacık Mah. FSM Cad. Yayabeyi Sk. No:8, 34810 Beykoz / İstanbul（整栋）' + TAG}}],
    'SB-688': [{'add_kp': {'name': 'Murat Köksal', 'role': 'Network and Security Solutions Director（Ankara；LinkedIn）= 技术决策人 → 写他：数据中心 10G/25G/100G（STH CENTEC）配其 Packet Broker / TAP 卖，分销 20% / OEM 30%；**守界：不做 bypass 交换机**' + TAG, 'email': '', 'phone': '', 'source': 'https://www.teslakom.com/kurumsal'},
                'facts': {'legal_name': 'TESLAKOM BİLİŞİM VE TELEKOMÜNİKASYON A.Ş.（İstanbul Bağcılar Demirkol Plaza + Ankara Bilkent Cyberpark）', 'founded': '2013（官网）' + TAG, 'staff': '12 人（contactout）/ 11–50；Niagara Networks（Packet Broker / Bypass / TAP）+ Celerway SD-WAN + Viprinet 土耳其分销 + 托管服务' + TAG, 'size': '小型增值分销商' + TAG, 'hq': 'Koçman Cd. 54 Demirkol Plaza C Blok Kat:2, Bağcılar / İstanbul' + TAG}}],
    # ---------- CA ----------
    'SB-344': [{'kp_name': 'Wai Lee', 'role': 'CEO / 创始人（1997；Crunchbase）—— **自有品牌 Amer Networks（交换机 / PoE / 光模块）= OEM 品牌商 = 首选目标 → OEM 30% Amer 标**' + TAG},
               {'kp_name': 'Toron Lee', 'role': 'VP Product Management（ex D-Link Canada；RocketReach）= 产品选型人 = **写他**（Lee 家族二代）' + TAG},
               {'facts': {'legal_name': 'Amer Networks（Amer.com；Mississauga ON + Clearwater FL；安省登记 JS-only、FL Sunbiz 未命中）', 'founded': '1997（LinkedIn / 新闻稿）' + TAG, 'staff': '11–50（LinkedIn）；第三方估数百万美元（量级）' + TAG, 'size': '小型（自有品牌网络设备商）' + TAG, 'hq': '3620B Laird Road Unit 4, Mississauga, ON L5L 6A9（+ Clearwater FL 美国仓）' + TAG}}],
    'SB-384': {'facts': {'legal_name': 'Canacctv（网店；法人名未取 —— BC Registry 付费 / JS）', 'size': '微型（估 1–5 人）' + TAG, 'hq': 'Unit B135-6286 203 Street, Langley, BC V2Y 3S1（运营 Surrey）' + TAG, 'other': '微型 CCTV 网店 → 分销 20% 一封 admin@，无回即停' + TAG}},
    'SB-841': [{'add_kp': {'name': 'Brent Koziol', 'role': '业主 / 经营者（1998 加入，父 Joe 退休后接班；与妻 Nonette 共同持有；Red Deer 1977 老店）= **老板 = 联系人**（sales@kohen.ca 转）→ STI 工业 DIN PoE 分销 20%' + TAG, 'email': '', 'phone': '', 'source': 'https://www.kohen.ca/'},
                'facts': {'legal_name': 'Ko-Hen Electronics Supply Ltd.（Alberta 公司登记付费未取）', 'founded': '1977（官网）' + TAG, 'staff': '估 10–20 人；3,840 sq ft 店面 + 库房' + TAG, 'size': '小型（电子元件 / 工业物料零售批发）' + TAG, 'hq': '6022 67A Street, Red Deer, AB T4P 3E8' + TAG}}],
    'SB-847': {'facts': {'legal_name': 'Rollan Tech Inc.（RollanTech Corporation；Québec REQ 未查）', 'size': '微型（名录 ~1 人）→ 不追' + TAG, 'hq': '1288 Rue Saint-Antoine O #1502, Montréal, QC H3C 0X6' + TAG}},
    'SB-399': [{'kp_name': 'Stephane Lavigueur', 'role': 'VP Product & Engineering（2022–）—— **LinkedIn 现挂 Genetec → 可能已离职**；下一封写 sales@ 问「current product lead」，不再指名' + TAG},
               {'add_kp': {'name': 'Dexter Liu', 'role': 'VP Operation（LinkedIn）—— Petawise = **Uniview 加拿大独家**（整线成品）→ 只打其空档：工业 DIN / 2.5G–10G PoE++，分销 20%' + TAG, 'email': '', 'phone': '', 'source': 'https://www.petawise.com/'},
                'facts': {'legal_name': 'Petawise Inc.（Petawise Technologies；安省登记 JS-only）', 'founded': '2014/2015' + TAG, 'staff': '11–50（LinkedIn）/ 8（RocketReach）；ZoomInfo 估 $5.3M（量级）' + TAG, 'size': '小型（Uniview 加拿大独家分销）' + TAG, 'hq': '1040 Martin Grove Rd Unit 9, Toronto (Etobicoke), ON M9W 4W4' + TAG}}],
    'SB-538': [{'kp_match': 'sales@infinitecables.com', 'role': '采购 / 销售口（职务待核）—— **公司在安省 Markham（加拿大），用户表国别 US 误 → country_fix 加拿大；DBA Phantom Cables = 自有品牌 → OEM 30%「Phantom」PoE，FCC + ISED**' + TAG},
               {'add_kp': {'name': 'George Arvanitopoulos', 'role': '董事 / 主要负责人（Corporations Canada 6482929 + D&B）= 老板；联名董事 Chris Michael Frangos —— 抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://opengovca.com/corporation/6482929'},
                'facts': {'legal_name': 'Infinite Cables Inc.（Corporations Canada 6482929；BN 813852142RC0001；DBA Phantom Cables）', 'founded': '2006-01-01（联邦；业务始于 2003）' + TAG, 'staff': '11–50（LinkedIn；RocketReach 32）；62,000 sq ft 办公 + 仓 = 千万加元级' + TAG, 'size': '小型 / 中型（线缆 + 网络配件自有品牌分销）' + TAG, 'hq': '3993 14th Avenue, Markham, ON L3R 4Z6（多伦多东北）' + TAG}}],
    # ---------- US ----------
    'SB-363': [{'kp_match': 'dshay@meridian-tech.com', 'role': '销售口（职务待核）—— 公司 = **纽约长岛 1990 年起的光纤传输设备制造商（同名陷阱：Jacksonville 的 Meridian Technologies 人力公司无关）** → OEM 30% 配套交换机 / 20% 分销' + TAG},
               {'facts': {'legal_name': 'Meridian Technologies, Inc.（NY DOS 检索 JS-only）', 'founded': '1990（LinkedIn）' + TAG, 'staff': '11–50（LinkedIn）' + TAG, 'size': '小型制造商（光纤视频 / 数据传输）' + TAG, 'hq': 'Elmont, NY 11003（长岛）' + TAG}}],
    'SB-773': {'facts': {'legal_name': 'Microseven Systems, LLC（CA SoS 未查）', 'founded': '2001（官网）/ 2003（LinkedIn）' + TAG, 'staff': '微型（1–9 人；创始人 James Cao）；Thomasnet 估 <$1M' + TAG, 'size': '微型（IP 摄像机 + 流媒体）→ 不追' + TAG, 'hq': '404 S Lemon Ave Ste 9, Walnut, CA 91789' + TAG}},
    'SB-913': [{'kp_match': 'asktolanpro@gmail.com', 'role': '官网公开 DM 地址（非私人邮箱）的接待人 —— 公司 = **LanPro® 自有品牌网络设备商（1997 品牌，Doral FL 2003 法人，拉美出口）= OEM 品牌商 → OEM 30% LanPro 标**' + TAG},
               {'facts': {'legal_name': 'LanPro Networks Inc.（原 LanPro of Miami, Inc.；FL Document P03000135286；FEI 20-3029519）', 'founded': '2003-11-19（FL Sunbiz；品牌 LanPro® 自 1997）' + TAG, 'staff': '5–10（Cortera）/ 11–50（LinkedIn）；Cortera 估销售 $5–10M' + TAG, 'size': '小型（自有品牌出口商）' + TAG, 'hq': '1880 NW 93rd Ave, Doral, FL 33172（迈阿密机场工业区）' + TAG, 'other': '与哥斯达黎加 Lanprosa（SB-771）同名但未证实关联，不合并' + TAG}}],
    'SB-994': {'facts': {'legal_name': 'Accurate Technologies Inc.（ATI；MI LARA 未查）', 'founded': '1992-02-04（Bloomberg）' + TAG, 'staff': '51–200（LinkedIn）；7 国子公司' + TAG, 'size': '中型（汽车测试 / 标定工具制造商；客户含国防）→ **守界 + 非目标 → 不追**' + TAG, 'hq': '26999 Meadowbrook Rd, Novi, MI 48377' + TAG}},
    'SB-1136': [{'kp_match': 'sales@fo4sale.com', 'role': 'Fosco Sales 接待（Grace）—— **公司在加州 Pleasanton，用户表「CA」= California 非加拿大 → country_fix 美国（FCC，无 ISED）**' + TAG},
                {'add_kp': {'name': 'Colin Yao', 'role': '创始人 / 业主（官网 + BBB「Sales Manager」= 老板亲自管销售）= **老板 = 联系人** → 光口交换机分销 20%（STI-154GP / STC-110XGE / STI-288DGGPM），FOB 深圳' + TAG, 'email': '', 'phone': '', 'source': 'https://www.fiberoptics4sale.com/'},
                 'facts': {'legal_name': 'Fiber Optics For Sale Co.（FOSCO Connect；CA SoS 未查）', 'founded': '2003-08-04（BBB；业务始于 2001）' + TAG, 'staff': '11–50（LinkedIn）/ 12（BBB）；自述「multi-million dollar annual sales」' + TAG, 'size': '小型（光纤产品网售 + 分销）' + TAG, 'hq': '269 Mavis Drive, Pleasanton, CA 94566（仓 Livermore）' + TAG}}],
    # ---------- CR / KZ ----------
    'SB-771': [{'kp_match': 'mercadeo@lanprosa.com', 'role': '市场口（职务待核）—— **公司在哥斯达黎加 San José（Ruijie 等品牌经销商），用户表国别 US 误 → country_fix 哥斯达黎加**；与迈阿密 LanPro（SB-913）同名未证实关联' + TAG},
               {'facts': {'legal_name': 'Lanprosa S.A.（Registro Nacional 付费未取）', 'founded': '2003（contactout；自述 20 年经验）' + TAG, 'staff': '11–50（LinkedIn）/ 22（RocketReach）' + TAG, 'size': '小型（网络 / 安防分销 + 集成）' + TAG, 'hq': 'Calle Blancos, San Francisco de Goicoechea, San José 11502, Costa Rica' + TAG}}],
    'SB-406': {'facts': {'legal_name': 'ТОО «Альянс»（Торгово-производственная компания «АЛЬЯНС»；volokno.kz；БИН 未取 —— **同名陷阱：ТОО «Volokno KZ» БИН 230240037181（2023 安装商）非本户**）', 'founded': '1999-03-10（官网）' + TAG, 'staff': '估 10–30 人' + TAG, 'size': '小型（光缆 / 光纤配件贸易 1999）' + TAG, 'hq': '050027, г. Алматы, Наурызбайский район, мкр. Калкаман-2' + TAG, 'other': '俄语信：光口交换机分销 20%，EAC 他们；Almaty 北京 13–15 发' + TAG}},
    'SB-616': {'facts': {'legal_name': 'ТОО «Торговый Дом INTANT»（БИН 未取）', 'founded': '2005（官网）' + TAG, 'staff': '6 城分部；估 50–150 人；**安防总分销（HiLook 全国）**' + TAG, 'size': '中型（哈萨克斯坦安防主分销商）' + TAG, 'hq': 'г. Алматы, ул. Байзакова, 60（旧址 ул. Муратбаева 61）' + TAG, 'other': '俄语信：Marvell 管理型 / 工业 / 10G 空档分销 20%；**信里不提 HiLook / Tenda**' + TAG}},
    # ---------- CZ / PL / RU / IT ----------
    'SB-596': [{'kp_match': 'pytlak@optokon.com', 'role': '研究档收件人（波兰分部 / 采购口；职务待核）—— 公司 = **OPTOKON a.s. 捷克 Jihlava 光纤制造商（Štefl 家族；军用线 = PASS），optokon.pl = 波兰分部** → 商用 / 工业 OEM 30%，**明说不做 MIL-STD**，抄 George Štefl' + TAG},
               {'add_kp': {'name': 'George Štefl', 'role': 'Group Manager & Head of Marketing（二代；兼 OptoNet Communication jednatel）；实控人 = 父 Ing. Jiří Štefl（1993 起 jednatel，2021 správní rada）' + TAG, 'email': '', 'phone': '', 'source': 'https://or.justice.cz/ias/ui/rejstrik-$firma?ico=13692283'},
                'facts': {'legal_name': 'OPTOKON, a.s.（IČO 13692283；DIČ CZ13692283；Červený Kříž 250, 586 01 Jihlava；波兰分部 OPTOKON Zakład Światłowodowy —— 用户表国别 PL 保留 = 收件人所在分部）', 'founded': '1991-01-16（s.r.o.；2014-08-30 起 a.s.）' + TAG, 'staff': '估 100–250 人；多国子公司 + 13 个在招岗位' + TAG, 'size': '中型制造商（光纤连接 / 军用加固）' + TAG, 'hq': 'Jihlava, Czech Republic（波兰：Świebodzice 一带分部）' + TAG}}],
    'SB-317': [{'add_kp': {'name': 'Tomáš Pavlíček', 'role': 'Ing.；jednatel（2012-01-02 起，独立代表；ex UTC Fire & Security 捷克）= 推定业主 = **联系人** → CCTV PoE 分销 20%' + TAG, 'email': '', 'phone': '', 'source': 'https://or.justice.cz/ias/ui/rejstrik-$firma?ico=24202908'},
                'facts': {'legal_name': 'Techfors CZ s.r.o.（IČO 24202908；DIČ CZ24202908；OR Praha C 188256）', 'founded': '2012-01-02（Obchodní rejstřík）' + TAG, 'staff': '估 5–15 人' + TAG, 'size': '小型（安防 / 弱电分销 + 集成）' + TAG, 'hq': 'Na staré vinici 395/7, Krč, 140 00 Praha 4' + TAG}}],
    'SB-256': [{'add_kp': {'name': 'Karol Nowak', 'role': 'Prezes zarządu（UNIFORCE sp. z o.o. = 普通合伙人）/ 创始人（2007-09-24 个体起）= **老板 = 联系人**；prokurent Jerzy Zdzisław Nowak（家族）→ 分销 20% + 自有标签 OEM 30% 可选' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/817374'},
                'facts': {'legal_name': 'UNIFORCE TVPRZEMYSLOWA NOWAK SP.K.（原 TVprzemyslowa sp. z o.o. sp.k.；KRS 0000817374 · NIP 7822874326 · REGON 385013197）', 'founded': '2019-12-05（KRS；业务自 2007-09-24）' + TAG, 'staff': '估 5–15 人' + TAG, 'size': '小型（CCTV 批发 / 网店 Poznań）' + TAG, 'hq': 'ul. Kórnicka 30, 61-141 Poznań' + TAG}}],
    'SB-537': {'facts': {'legal_name': 'ООО «АгатСБ.ру»（品牌 HTV / Hi-Tech Vision；ИНН 7204152580 · ОГРН 1107232010808）', 'founded': '2010（ОГРН 110…；秋明注册）' + TAG, 'staff': '估 10–30 人（下轮 rusprofile 按 ИНН 取）' + TAG, 'size': '小型（**自有品牌 HTV 含 PoE 交换机 = OEM 品牌商**）' + TAG, 'hq': 'г. Москва, Сигнальный проезд, 16с2（注册地 Тюмень；分部 Братск）' + TAG, 'other': '俄语信 OEM 30% HTV 标，CNY 预付，EAC 他们' + TAG}},
    'SB-271': [{'kp_name': 'Simone D’Andrea', 'role': 'Direttore Generale / Key Principal（ufficiocamerale）= **决策人 = 联系人** → PoE 4/8/16/24 分销 20%；营收 €4.16M 但利润 €31.8k = 薄利 → 不做第二次让价' + TAG},
               {'kp_name': 'Ivan Stazio', 'role': '市场口（marketing@dodic.it；职务待核）—— 抄送' + TAG},
               {'facts': {'legal_name': 'DODIC ELETTRONICA S.R.L.（Dodic Group；P.IVA / C.F. 01809930603 · REA FR-102942）', 'founded': '1992-04-09（S.r.l.；业务自 1975）' + TAG, 'staff': '7–8 人正式员工 + 6 网点；营收 €4.16M（2025）· 利润 €31.8k' + TAG, 'size': '小型分销（中意安防 / 电子 6 分店）' + TAG, 'hq': 'Via del Casale 13, 03100 Frosinone（总部 + 中央仓 1,500 m²）' + TAG}}],
    # ---------- IL ----------
    'SB-359': [{'kp_match': 'alexander@larch-networks.com', 'role': '联合创始人 / CEO（市场 + 销售；前身 Niram Systems 2008/09）= **老板 = 联系人**；公司 = **Marvell ROS / SONiC 交换机 NOS 软件商** → 卖 Marvell L2+/L3 + CENTEC 做硬件平台，OEM 30% / CENTEC ≥35%，商用 / DC / 工业 only' + TAG},
               {'kp_match': 'azarudniy@larch-networks.com', 'role': '研究档 KP（职务待核；工程口）' + TAG},
               {'add_kp': {'name': 'Eddie Preskovsky', 'role': '联合创始人（Tracxn 记为 co-CEO）—— 抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://www.larch-networks.com/'},
                'facts': {'legal_name': 'Larch Networks Ltd.（原 Niram Systems；ח.פ. 未取 —— 下轮 israeli-companies 按名查）', 'founded': '2008/2009（前身 Niram Systems）' + TAG, 'staff': '11–50（LinkedIn）；开发办公室 Kyiv' + TAG, 'size': '小型（交换机 NOS / 嵌入式网络软件）' + TAG, 'hq': 'Rosh HaAyin, Central District, Israel' + TAG}}],
    'SB-711': [{'kp_match': 'daniel@madalix.co.il', 'name': 'Daniel Zaichik', 'role': 'CEO / 创始人（2016；RocketReach）= **老板 = 联系人** → 工业 DIN PoE 分销 20%；**守界：国防项目 PASS**' + TAG},
               {'facts': {'legal_name': 'MADALIX（ח.פ. 未取）', 'founded': '2016（RocketReach）' + TAG, 'staff': '微型（≈3 人）' + TAG, 'size': '微型 VAR（工业 / 加固计算）' + TAG, 'hq': 'Tel Aviv District, Israel' + TAG}}],
    # ---------- DE ----------
    'SB-240': {'add_kp': {'name': 'Tobias Hübner', 'role': 'Geschäftsführer（2022-10 起；ex ESRA GmbH Prokurist；3 名股东之一 = 推定）= **老板 = 联系人** → **经营范围白纸黑字「摄像机 / NVR / UI 白标」= 在建自有安防品牌 → OEM 30%「frogfish」PoE 4/8/16/24 配 NVR**' + TAG, 'email': '', 'phone': '', 'source': ND + 'frogfish%20surveillance%20GmbH,%20Reichenbach'},
               'facts': {'legal_name': 'frogfish surveillance GmbH（Amtsgericht Chemnitz HRB 35309；EUID DEU1206.HRB35309；Friedensstraße 62, 08468 Reichenbach im Vogtland；登记笔误初名「froqfish」2022-10-25 更正）', 'founded': '2022-10-14（Handelsregister）' + TAG, 'staff': '微型（估 3–10 人）；Stammkapital €25,000；3 股东（Northdata 网络：ESRA GmbH Reichenbach / Friedrich Strobel / Simon Strobel）' + TAG, 'size': '微型（安防白标进口商）' + TAG, 'hq': 'Reichenbach im Vogtland, Sachsen' + TAG, 'other': '**同名陷阱：Kleinmachnow 的 Frogfish&41 GmbH（HRB 34275 Potsdam）无关**' + TAG}},
    # ---------- AU ----------
    'SB-716': [{'kp_match': 'info@radioparts.com.au', 'role': '总信箱接待（Daniel H；职务待核）—— 公司 = 墨尔本 1936 年老牌电子分销（两实体同址 = 家族集团）→ 请转 networking category buyer，分销 20%' + TAG},
               {'facts': {'legal_name': 'RADIO PARTS PTY. LTD.（ABN 95 006 098 719；Trading Name RADIO PARTS GROUP；关联 RADIO PARTS SALES (AUST) PTY LTD ABN 55 004 623 401 同址）', 'founded': '≈1982–83（ACN 006 098 719 段）；集团自述 1936' + TAG, 'staff': '估 50–100 人' + TAG, 'size': '中型（电子 / 安防 / 网络分销，门店 + 网店）' + TAG, 'hq': 'West Melbourne, VIC 3003' + TAG}}],
    'SB-216': [{'kp_match': 'george@ltsecurityinc.com.au', 'role': '推定业主 / 经理（LT SECURITY PTY LTD 2015–16；同邮编 Business Name「LTS Security Australia」）—— LTS = 美国 LT Security Inc. 白标安防品牌的澳洲分销，PoE 已在其品牌线 → 低优先，只打工业 DIN + 2.5G 空档' + TAG},
               {'facts': {'legal_name': 'LT SECURITY PTY LTD（ABN 18 609 932 309；Business Name LTS Security Australia ABN 33 845 781 939）', 'founded': '≈2015–16（ACN 609 932 309 段）' + TAG, 'size': '小型（估 5–15 人；LTS 品牌澳洲分销）' + TAG, 'hq': 'Peakhurst / Riverwood, NSW 2210（悉尼南）' + TAG}}],
    'SB-540': {'facts': {'legal_name': 'JDK TECHNOLOGIES PTY. LTD.（ABN 47 601 677 329）', 'founded': '≈2014（ACN 601 677 329 段）' + TAG, 'size': '微型 / 小型（IT / 安防贸易）' + TAG, 'hq': 'Regents Park / Birrong, NSW 2143（悉尼西）' + TAG}},
    'SB-507': [{'kp_match': 'sales@fibreoptic.com.au', 'role': 'General Manager（2013–；管销售与运营；CEO = 父 A.P. Singh Arneja）= **本地决策人 = 联系人**；**公司 2021 起属瑞典 Hexatronic Group，但仍由 Arneja 父子经营 → 采购权在墨尔本**；信里不提并购' + TAG},
               {'add_kp': {'name': 'A.P. Singh Arneja', 'role': 'CEO / 创始人（2000）—— 抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://www.fibreoptic.com.au/career'},
                'facts': {'legal_name': 'Fibre Optic Systems Pty Ltd（FOS；ABN 未取；2021 起 Hexatronic Group AB 子公司）', 'founded': '2000' + TAG, 'staff': '11–50（23）；第三方估 $24M（量级）；内销经理 Jaideep Singh' + TAG, 'size': '小型 / 中型（光纤 / 铜缆产品制造 + 分销）' + TAG, 'hq': '25 Gilbert Park Drive, Knoxfield, VIC 3180（墨尔本东南）' + TAG}}],
    'SB-699': [{'kp_match': 'mk@ccdact.com', 'role': 'Assistant Manager（2012–；MD Stuart Malcolm King 之子 = 二代）= **联系人**；公司 = **堪培拉自有品牌网络配件商（CCD 牌媒体转换器 / SFP / 交换机，客户含联邦政府供应链）= 现成 OEM 买家 → OEM 30% CCD 标** PoE / 光口；新域 ccd.au' + TAG},
               {'add_kp': {'name': 'Stuart Malcolm King', 'role': 'Managing Director / 业主（2003–；D&B Key Principal）—— 抄送' + TAG, 'email': '', 'phone': '', 'source': ABR + '22134085644'},
                'facts': {'legal_name': 'CCD NETWORKING PTY. LTD.（ABN 22 134 085 644；DBA OMEO CANBERRA）', 'founded': '2008（自述；ACN 134 085 644 段相符）' + TAG, 'staff': '3–10 人；第三方估 $4.4M（量级）' + TAG, 'size': '微型（自有品牌网络配件进口 + 制造 + 分销）' + TAG, 'hq': 'Unit 4, 10 Maryborough Street, Fyshwick, ACT 2609' + TAG}}],
    # ---------- IS / PL / AL ----------
    'SB-1038': [{'add_kp': {'name': 'Johann Sigurthorsson', 'role': '联合创始人 / 业主（1997 与 David Askelsson 共创）= **老板 = 联系人**（icecom@）→ 集成 25%，工业 DIN PoE（-40℃）+ 微波站 PoE++' + TAG, 'email': '', 'phone': '', 'source': 'https://keldan.is/Fyrirtaeki/Yfirlit/5401022440'},
                 'facts': {'legal_name': 'IceCom ehf.（kennitala 540102-2440，ehf 2002-01-14；旧 kt 570197-2239 = 1997 原主体）', 'founded': '1997（原主体）/ 2002-01-14（ehf）' + TAG, 'staff': '估 5–15 人；keldan 最新年报 2020（之后未见 → 发信前看官网 / Facebook 是否仍活跃）' + TAG, 'size': '微型 / 小型集成商（微波 / 网络 / 电视 / CCTV / 楼宇 / 消防）' + TAG, 'hq': 'Lyngás 10, 210 Garðabær, Iceland（EEA，CE 即可）' + TAG}},
                {'add_kp': {'name': 'David Askelsson', 'role': '联合创始人 / 业主 —— 抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://www.icecom.is/index.php/english/'}}],
    'SB-1041': {'facts': {'legal_name': 'INTALL SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ（品牌 noning / 网店 intshop.pl；NIP 6312679269 · REGON 380028515）', 'founded': '2019（自述）' + TAG, 'size': '微型（2–5 人；靠欧洲分销仓转卖）→ 低优先' + TAG, 'hq': 'ul. Bojkowska 22, 44-100 Gliwice' + TAG}},
    'SB-258': [{'kp_match': 'f.luniku@arfanet.al', 'role': 'Administrator & 股东（2013–；另 Lex Travel、ARFA shpk 2005–2020）—— **合规标注（内部）：2024-01 因 IPTV 盗版 + 逃税案被捕，2025-12 报道已获释** → 留档不主动追；来询则 100% 预付、FOB 深圳；信里绝不提案件' + TAG},
               {'facts': {'legal_name': 'ARFANET SH.P.K.（NIPT L31626002T；股东 Artan Sota / Fatjon Luniku / Eduard Koka / Lorenc Sota）', 'founded': '2013-04-23（companywall.al）' + TAG, 'staff': '估 5–10 人；收入 73.5M ALL（≈ €0.73M）· 净利 0.58M ALL' + TAG, 'size': '微型 / 小型（酒店 SMATV / IPTV + 安防批发安装）' + TAG, 'hq': 'Rruga Muhedin Llagani, Ndërtesa 2, Nr.6, Tiranë' + TAG}}],
    # ---------- 未命中 ----------
    'SB-863': {'facts': {'other': '第 90 批检索未命中（cmd-sec.ru：1 次检索仅泛化结果，无法定名 / ИНН）→ 留待 ИНН 线索' + TAG}},
    'SB-095': {'facts': {'other': '第 90 批检索同名多户（「M Technology srl」Olbia / Vinchiaturo 两家一人公司，均无法与 mtechnology.it 对上）→ 未能锁定，不写回登记' + TAG}},
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
