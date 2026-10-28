#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 97 批（T29-U90 同轮续做，公司底数第十五轮 · B 档「自有 logo + 打开」五国 24 户）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=97 行）。
结构同 batch96_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：OEM 30% 首选 5（SB-712 Maple Systems KP = 总裁 + 销售总监 / SB-806 General Data KP = 运营 VP、自有 DG 标交换机 / SB-890 Technopc KP = 董事长兼产品、已买 Ewind / SB-784 BCS 品牌所有人 / SB-683 Spectra KP = 股东 GF）；
同行 / 非品类不动 3（SB-278 Lanmus 贴牌壳 / SB-744 COMMANDO 印度品牌商 → country_fix 印度 / SB-171 Comtek 翻新二手）；准同行低概率 2（SB-794 W&T / SB-592 Fotech）；未坐实 1（SB-268）；终端用户 1（SB-441）；升 A 候选 +2（SB-890 Technopc / SB-784 BCS）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 97 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US / IN ----------
    'SB-1048': {'add_kp': {'name': 'Christy Fagan', 'role': 'Manager, Operations（ZoomInfo / CT Northwest 团队页）= 收件人（info@kargor.com 点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.ct-northwest.com/about/'},
                'facts': {'legal_name': 'Kar-Gor, Inc.（俄勒冈；现以 CT Northwest 品牌经营；OR 登记号未取）', 'founded': '1986-02-14' + TAG, 'staff': '11–50 人；<$5M', 'hq': '3540 Brooks Avenue NE, Building 2, Salem, OR 97301',
                          'other': '第 97 批：kargor.com 重定向之谜 = 改以 CT Northwest 做交通 ITS；交通机柜要 NEMA TS2 → Saga 证书不对口 → 一页纸即止、不加厚' + TAG}},
    'SB-853': {'add_kp': {'name': 'Kenneth G (Ken) Rivera', 'role': 'President / CEO（BBB / SAM / AZ UTRACS 联系人）= 老板 = 收件人（邮箱未公开 → 官网表单 / info@）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.bbb.org/us/ca/chino/profile/low-voltage-contractors/jm-fiber-optics-inc-1126-89069206'},
               'facts': {'legal_name': 'JM Fiber Optics, Inc.（加州 Corporation；MBE / SBA 8(a)；SAM 在册）', 'founded': '1992（业务）/ 1993-02-16（公司）' + TAG, 'staff': '4–9 人；$1–3M', 'hq': '13941 Ramona Ave, Suite A, Chino, CA 91710',
                         'other': '第 97 批：微型政府 / 交通类光纤集成商 → 只谈商业项目一条线，小项目集成商 25%，一页纸写老板；会问 TAA（禁词，不配合）' + TAG}},
    'SB-278': {'kp_match': 'sales@lanmus.com', 'role': '公域 —— **同行（深圳代工贴牌品牌壳，渠道在 UAE / 非洲）：不发**' + TAG,
               'facts': {'legal_name': 'Lanmus Networks（美国实体未坐实；TX 地址为共享办公；OUI 登记名 Lanmus Networks Ltd 2024-10-14）', 'founded': '≈2024' + TAG, 'staff': '微型', 'hq': '6725 S Fry Rd, Ste 700 #108, Katy, TX 77494（虚拟地址）',
                         'other': '第 97 批：自称「independently developed by LANMUS」、由 SPOLLEX 分销至 UAE / GCC / 非洲 = 同货源贴牌同行 → 不发价格表、B 不动' + TAG}},
    'SB-712': [{'kp_match': 'alexm@maplesystems.com', 'name': 'Alex Moskos', 'role': 'President（theorg；前 VP Operations）= **拍板人 = 研究档 KP「Alex M」大概率本人**' + TAG},
               {'kp_match': 'dianec@maplesystems.com', 'name': 'Diane Callahan', 'role': 'Director of Sales & GTM Operations（theorg / ZoomInfo）= 研究档 KP「Diane C」本人 = 抄送' + TAG},
               {'facts': {'legal_name': 'Maple Systems, Inc.（Washington UBI 600490742；WA Profit Corporation；2014 起员工持股）', 'founded': '1983-05-25' + TAG, 'staff': '44–60 人；$7–10M（第三方）', 'hq': '808 134th St SW, Suite 120, Everett, WA 98204',
                          'other': '第 97 批：HMI / PLC 制造商、官网已设工业网络交换机品类（外采转售）→ 工业 PoE 贴 Maple 标 = OEM 30% 首选（STI-054GP / STI-144GP / STI-288DGGPM）；CEO Larry St Peter / Governor Daunne O’Farrell 仅记档' + TAG}}],
    'SB-744': [{'kp_match': 'info@commandonetworks.com', 'role': '公域 —— **同行（印度品牌商，自设深圳 / 香港 / 迪拜办公室直接采购贴牌）：不发**' + TAG},
               {'facts': {'legal_name': 'COMMANDO Networks Private Limited（印度 CIN U74999MH2015PTC261514；美国 COMMANDO Networks Inc. 仅注册代理地址 1007 N Orange St, Wilmington DE）', 'founded': '2015-12-30' + TAG, 'staff': '51–100 人', 'hq': 'Office 212-213, Building No. 2(A-3), Millennium Business Park, MIDC, Mahape, Navi Mumbai 400710, India',
                          'other': '第 97 批：国别更正美国 → 印度；董事 Vazir Ahmed Akhtar Siddiqui + Umair Ahmed Siddiqui；自有品牌 170+ 国商标、深圳华强北办公室 → 同行不动' + TAG},
                'country_fix': '印度'}],
    'SB-806': {'kp_match': 'psanborn@general-data.com', 'role': 'Vice President Operations（explorium）= **运营 / 采购口 = 研究档 KP 本人**' + TAG,
               'facts': {'legal_name': 'General Data Company, Inc.（俄亥俄；SoS 号未取；Tracxn 记法人 1999-12-31）', 'founded': '1981（Pete Wenzel）' + TAG, 'staff': '231–275 人；$37–104M（第三方区间）', 'hq': '4354 Ferguson Drive, Cincinnati, OH 45245',
                         'other': '第 97 批：标签 / 条码 / 网络集成商，已有自有 DG 标 PoE 交换机（DG-S1930K 系列 = 华南贴牌）→ OEM 30% 首选、B BIG，写 VP Operations 价格直接给到位' + TAG}},
    # ---------- TR ----------
    'SB-275': {'add_kp': {'name': 'Yusuf Ölçer', 'role': '联系人 / 疑似业主（haber15 企业名录；satis@gelecekbt.com）= 收件人' + TAG, 'email': 'satis@gelecekbt.com', 'phone': '', 'source': 'https://www.haber15.com.tr/firmalar/gelecekbt-bilgi-teknolojileri.html'},
               'facts': {'legal_name': 'GelecekBT Bilgi Teknolojileri（法律形式 / MERSİS 未取；Perpa 店铺型）', 'founded': '2004-10-13' + TAG, 'staff': '2–10 人', 'hq': 'Perpa Ticaret Merkezi A Blok Kat:13 No:1990, Okmeydanı, 34384 Şişli / İstanbul',
                         'other': '第 97 批：自有品牌 Telkolink（「Telkolink, GelecekBT’ye aittir」）+ CLR Networks 独家 + 分销 3Onedata / TG-NET 华南货 → 贴标 OEM 30% 一句试探 + 分销 20% 为底，价格敏感' + TAG}},
    'SB-268': {'kp_match': 'info@bulutlarbilisim.com', 'role': 'CEO（研究档）—— 法人一次未坐实、官网失效 → 先不发；若试只发 STH 一页纸，无回即 C' + TAG,
               'facts': {'legal_name': 'Bulutlar Bilişim（未坐实；1 次检索无同名命中）', 'founded': '未取' + TAG, 'staff': '微型（推定）', 'hq': '土耳其（城市未取）',
                         'other': '第 97 批：检索结果均为 Bulutistan / Bulut Bilişim 他司 → 未坐实；询盘为 100G/25G 核心（CENTEC 线）；表内「质量可能一般」不逆' + TAG}},
    'SB-442': [{'kp_match': 'furkan@optima.tc', 'role': '研究档 KP（用户表；职务未取）= 收件人，抄 optima@ 点名「satın alma / proje」' + TAG},
               {'add_kp': {'name': 'İ. Tamer Ülgen', 'role': '创始人 / CEO（机械工程师；2000-12 Ostim 创业）= 拍板人（仅记档）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.optima-engineering.com/en/corporate/about-optima'},
                'facts': {'legal_name': 'Optima Mühendislik A.Ş.（原 Ltd. Şti.；MERSİS 未取）', 'founded': '2000-12-05' + TAG, 'staff': '100 人（EMIS 2026）', 'hq': 'Başkent Organize Sanayi Bölgesi 19. Cadde No:62, Malıköy, 06909 Sincan / Ankara',
                          'other': '第 97 批：路障 / 升降柱 / 闸机 / 车牌识别制造商、出口中东 → PoE 交换机为系统配套（外采）→ 工业小口数 + 商用 PoE 贴 Optima 标 = OEM 30% 小' + TAG}}],
    'SB-592': {'kp_match': 'ssahin@fotech.com.tr', 'role': '研究档 KP（全名 / 职务未取）= 收件人，抄 info@' + TAG,
               'facts': {'legal_name': 'Fotech Fiber Optik Teknolojik Hizmetler San. ve Tic. Ltd. Şti.（EMIS；MERSİS 未取）', 'founded': '1989-06-23（Final Elektrik → 1994 Fotech）' + TAG, 'staff': '29 人（EMIS 2026）', 'hq': 'Ataşehir Bulvarı 38. Ada Ata 3/3 Plaza Kat:5 No:51-52, 34758 Ataşehir / İstanbul',
                         'other': '第 97 批：欧美高端品牌独家分销 + 集成（Fluke Networks / Black Box / EXFO）→ 对华南货兴趣低 → 集成商 25% 一页纸即止、不加厚' + TAG}},
    'SB-676': [{'kp_match': 'info@pctedarik.com', 'role': '公域 = 收件人，点名 İslam Çalık' + TAG},
               {'add_kp': {'name': 'İslam Çalık', 'role': 'Key Principal（D&B）= 负责人；n11 店铺登记人 Ali Çalık（şahıs MERSİS 2250094824）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.dnb.com/business-directory/company-profiles.pc_tedarik_ithalat_ihracat_yazilim_ticaret_limited_sirketi.6bf2c05e296f4bae217c29a0a17f5285.html'},
                'facts': {'legal_name': 'PC Tedarik İthalat İhracat Yazılım Ticaret Ltd. Şti.（MERSİS 未取；关联 şahıs 登记 Ali Çalık）', 'founded': '未取' + TAG, 'staff': '1–50 人', 'hq': 'Çınardere Mah. Ankara Cad. No:43A, 34892 Pendik / İstanbul',
                          'other': '第 97 批：硬盘 / 安防 / 电脑批发网店 + 注册商标 UNİMAX → 贴标 OEM 30% 一句试探 + 分销 20% 为底，价格直接给到位' + TAG}}],
    'SB-890': [{'kp_match': 'mithat.yucel@technopc.com.tr', 'role': 'Yönetim Kurulu Başkanı / 分管产品管理（官网组织架构页；1998 Yücel Elektronik 联合创始人）= **拍板人 = 研究档 KP 本人**' + TAG},
               {'kp_name': 'Murat Yücel', 'role': '创始合伙人 / 销售市场执行合伙人（Coşkun Murat Yücel；D&B Key Principal）= 抄送' + TAG},
               {'facts': {'legal_name': 'Technopc Teknoloji San. ve Tic. A.Ş.（ETBİS 登记 A.Ş.；MERSİS 未取）', 'founded': '1998（Yücel Elektronik）/ 2006（Technopc 品牌）' + TAG, 'staff': '51–200 人', 'hq': 'Ataşehir / İstanbul（详细地址未取）',
                          'other': '第 97 批：本土 PC / 工业 PC / NVR 品牌，表内「工业 PoE 买的 Ewind 的」= 已在深圳买工业 PoE 贴标 → OEM 30% 首选，对标 Ewind 报价；升 A 候选（回信即 A）' + TAG}}],
    # ---------- DE ----------
    'SB-188': [{'kp_match': 'bohne@saf-slk.de', 'role': 'Geschäftsführer（HRB 19446 Stendal；由 ppa. 升任）= **拍板人 = 研究档 KP 本人**' + TAG},
               {'kp_match': 'duschka@saf-slk.de', 'role': 'ppa.（Impressum 授权代表）= 研究档 KP = 抄送' + TAG},
               {'facts': {'legal_name': 'Schaltanlagenbau Förderstedt GmbH（Amtsgericht Stendal HRB 19446；资本 €25,000）', 'founded': '2013-04-17（登记 2013-06-03）' + TAG, 'staff': '10–24 人；≤€10M', 'hq': 'Ascherslebener Straße 18d, 06467 Seeland OT Hoym（旧址 Güsten）',
                          'other': '第 97 批：低压开关柜 / 控制柜制造商，柜内 DIN 导轨工业交换机外采配套 → 工业 PoE 小口数一条线，集成商 25%，直接写 GF' + TAG}}],
    'SB-683': {'kp_match': 'juergen.rauscher@spectra.de', 'role': 'Geschäftsführer / 股东（Komplementärin Spectra Verwaltungs-GmbH HRB 738432；Inhaber Lang / Rauscher / Rottmayr）= **三位老板之一 = 研究档 KP 本人**' + TAG,
               'facts': {'legal_name': 'Spectra GmbH & Co. KG（Amtsgericht Stuttgart HRA 726688；Komplementärin HRB 738432；资本 €500,000）', 'founded': '1982（创立）/ 2011-08-16（KG 登记）' + TAG, 'staff': '90–100 人；€10–50M', 'hq': 'Mahdenstr. 3, 72768 Reutlingen（分部 Winterthur / Linz）',
                         'other': '第 97 批：工业 PC 制造商 + ORing 工业交换机分销，2025 连并 Compmall / ICP Deutschland（扩品类期）→ 工业 PoE 自有标 Spectra = OEM 30% 目标 / 分销 20% 为底，B BIG' + TAG}},
    'SB-171': {'add_kp': {'name': 'Askar Sheibani', 'role': 'Geschäftsführer / 集团 CEO（1989 Deeside 创立 Comtek）—— 非品类（翻新 / 二手）：不发' + TAG, 'email': '', 'phone': '', 'source': 'https://www.northdata.com/COMTEK+NETWORK+SYSTEMS+GmbH,+M%C3%B6rfelden-Walldorf/Amtsgericht+Darmstadt+HRB+100142'},
               'facts': {'legal_name': 'COMTEK NETWORK SYSTEMS GmbH（Amtsgericht Darmstadt HRB 100142，原 Offenbach HRB 40700；母公司 Comtek Network Systems (UK) Ltd 05929974）', 'founded': '2003-11-11' + TAG, 'staff': '小型（德国分部）', 'hq': 'Nordendstraße 2, 64546 Mörfelden-Walldorf',
                         'other': '第 97 批：网络设备翻新 / 维修 / 二手商 = 不买新品白牌 → 非品类，B 不动、不发' + TAG}},
    'SB-794': {'add_kp': {'name': 'Jan Gerdes', 'role': 'Produktmanager（Single Pair Ethernet / logic.hub / PC-Karten；wut.de 联系人 PDF 公开 j.gerdes@wut.de）= 收件人（准同行，一页纸即止）' + TAG, 'email': 'j.gerdes@wut.de', 'phone': '', 'source': 'https://www.wut.de/e-wwwww-co-inde-000.pdf?p=1'},
               'facts': {'legal_name': 'Wiesemann & Theis GmbH（Amtsgericht Wuppertal HRB 6377；资本 €250,001）', 'founded': '1979（Reinhard Wiesemann + Rüdiger Theis）' + TAG, 'staff': '50–53 人；€10–50M', 'hq': 'Porschestr. 12, 42279 Wuppertal',
                         'other': '第 97 批：Web-IO / Com-Server 自研自产「made in Wuppertal」= 准同行，目录交换机为补位转售 → 只给产品经理一页纸、不加厚、不投第 2 封；GF Tobias Theis（2024-01 二代接班）仅记档' + TAG}},
    # ---------- GB ----------
    'SB-1031': {'kp_match': 'dgupta@ralakde.co.uk', 'role': 'Director / PSC 75%+（Companies House 09757591；1992-06 生）= **老板 = 研究档 KP 本人**' + TAG,
                'facts': {'legal_name': 'RALAKDE LTD（Companies House 09757591；关联 Ralakde Automation Ltd 11435782 / Ralakde Holdings Limited 16830812（2025-11-04 新设））', 'founded': '2015-09-02' + TAG, 'staff': '微型（1 名股东）', 'hq': 'Unit 5a Victoria Road, Stoke-On-Trent ST4 2HS',
                          'other': '第 97 批：工业自动化备件贸易 + 维修（SIC 33120 / 33140 / 33200 / 47421），2025-11 新设控股 = 重组中 → 分销 20% 一页纸即止（工业 STI 系列），不加厚' + TAG}},
    'SB-975': {'kp_match': 'imcneil@cctv-global.co.uk', 'role': 'Co-founder / Director / PSC（Companies House 08411023；1972-04 生）= **老板之一 = 研究档 KP 本人**；另一董事 / PSC Gonçalo Filipe Dos Santos Silva（1983-10 生）' + TAG,
               'facts': {'legal_name': 'CCTV GLOBAL LONDON LTD（Companies House 08411023）', 'founded': '2013-02-20' + TAG, 'staff': '小型', 'hq': 'Alpha 319, Building K, Chobham Business Centre, Chertsey Road, Chobham, Woking, Surrey GU24 8JB',
                         'other': '第 97 批：Hikvision / HiLook / Ajax 授权分销，现卖 Ruijie 交换机 → 分销 20%：商用 PoE 对标 Ruijie 价格直接给到位，一页纸写联合创始人' + TAG}},
    'SB-154': [{'kp_match': 'nathan@wire.tech', 'role': 'Managing Director / 创始人 / Director（Companies House 11576417；1981-04 生；前 RAF / 皇家海军陆战队）= **拍板人 = 研究档 KP 本人**' + TAG},
               {'kp_match': 'james@wire.tech', 'name': 'James Edward Brooks', 'role': 'Director（2021-12-21 起；1993-04 生）= 研究档 KP「James」本人 = 抄送' + TAG},
               {'facts': {'legal_name': 'WIRE TECHNOLOGIES LIMITED（Companies House 11576417；PSC 2026-01-26 起 Granity Point Group Ltd）', 'founded': '2018-09-19' + TAG, 'staff': '6–11 人；营业额 <£1M（微型）', 'hq': 'Unit 5 Cirencester Business Estate, Esland Place, Love Lane, Cirencester GL7 1YG',
                          'other': '第 97 批：数据中心互连自有品牌（光模块 / DAC / 线缆，Saga 不供）+ Nuvias 独家渠道 → 只做 MC / 光口小交换机贴 Wire 标 OEM 30% 一条线；2026-01 控股变更（刚被收编）→ 不加厚' + TAG}}],
    'SB-255': [{'kp_name': 'Jeremy Lester', 'role': 'Managing Director / Director（Companies House 01613368；2003-11-07 起；1977-03 生；创始人 Alan Lester 之子）= **拍板人**（sales@ 公域）' + TAG},
               {'add_kp': {'name': 'Nick Neil Morgan', 'role': 'Sales Director / Director（2024-06-14 起；1979-03 生）= 抄送（邮箱未公开 → sales@ 点名）' + TAG, 'email': '', 'phone': '', 'source': CH + '01613368/officers'},
                'facts': {'legal_name': 'SWITCHTEC LIMITED（Companies House 01613368；关联 Switchtec Components Ltd 02612994 / Switchtec Electronics Ltd 05541783）', 'founded': '1982-02-12' + TAG, 'staff': '11–50 人', 'hq': 'Brooms Road, Stone Business Park, Stone, Staffordshire ST15 0SH',
                          'other': '第 97 批：Lester 家族工业元器件目录商（7,000+ SKU，无 MOQ），2026-05 申请扩建 = 扩品类窗口 → 工业 DIN 导轨 PoE 一条线，分销 20%；研究档 Mark Stevens（Southern Area Sales Manager）非董事、官方记录自然无 → 仅作抄送' + TAG}}],
    # ---------- PL ----------
    'SB-1004': {'add_kp': {'name': 'Artur Łykowski', 'role': 'Członek Zarządu / 股东（KRS 0000854041；1976 生）= 收件人（arpeo@arpeo.pl 点名）；另一董事 Radosław Herman，股东 Paweł Mierzwa' + TAG, 'email': 'arpeo@arpeo.pl', 'phone': '', 'source': 'https://www.imsig.pl/krs/0000854041'},
                'facts': {'legal_name': 'Arpeo Sp. z o.o.（KRS 0000854041；NIP 5472220160；REGON 386724612；资本 5,000 zł）', 'founded': '2020-08-07' + TAG, 'staff': '微型', 'hq': 'ul. prof. dr. Mieczysława Michałowicza 12, 43-300 Bielsko-Biała',
                          'other': '第 97 批：电工配件微型网店（站内工业交换机页）→ 工业非管理 STI 小口数一条线，分销 20% 一页纸即止' + TAG}},
    'SB-441': {'facts': {'legal_name': '„METAL UNION” Sp. z o.o.（KRS 0000138529；NIP 5731021083；REGON 150090573；资本 1,000,500 zł）', 'founded': '1995-04-26（KRS 2002-11-15）' + TAG, 'staff': '中型制造业（人数未取）；净利 91 tys zł（bizraport）', 'hq': 'ul. Żyzna 11F, 42-200 Częstochowa',
                         'other': '第 97 批：谜底 = 冷弯钢型材厂的 IT 部门买了 €50 光模块 + MC → 终端用户非渠道 → B 保留不加厚；若发只写一页纸「厂区监控 / 车间网络」' + TAG}},
    'SB-942': {'add_kp': {'name': 'Mikołaj Tomaszewski', 'role': '业主（CEIDG；sklep@dmtrade.pl）= 收件人' + TAG, 'email': 'sklep@dmtrade.pl', 'phone': '', 'source': 'https://www.dmtrade.pl/pl/contact.html'},
               'facts': {'legal_name': 'DMTrade Mikołaj Tomaszewski（CEIDG；NIP 6981681757；REGON 300138031）', 'founded': '2005' + TAG, 'staff': '小型（网店 + B2B 批发）', 'hq': 'ul. Wiśniowa 36, 64-000 Kościan',
                         'other': '第 97 批：Cudy 波兰官方分销 + 卖 Spacetronik（SB-092）→ 分销 20% 对标 Cudy 价格直接给到位；若 Spacetronik 成线则作其下游、不单独加厚' + TAG}},
    'SB-784': [{'kp_match': 'm.sobecki@bcs.pl', 'role': 'Project Manager（@bcs.pl = 品牌所有人 BCS Sp. z o.o. 本尊，非 sklep-bcs.pl 经销店）= 产品口 = 收件人' + TAG},
               {'add_kp': {'name': 'Artur Stępowski', 'role': 'Prezes Zarządu（rejestr.io KRS 0000092488）= 拍板人（点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/92488/bcs'},
                'facts': {'legal_name': 'BCS Sp. z o.o.（原 NSS Sp. z o.o.，2024-10-14 更名；KRS 0000092488；NIP 5213124674；REGON 017161046；LEI 259400J1GBGK8VAOD039）', 'founded': '2002-02-21（业务 1998；BCS 品牌 2008）' + TAG, 'staff': '中型（波兰 CCTV 知名品牌；人数未取）', 'hq': 'ul. Modularna 11, 02-238 Warszawa',
                          'other': '第 97 批：BCS 自有标 PoE 交换机（站内 106 处）= 华南贴牌 → OEM 30% 首选（PL）、B BIG；升 A 候选（回信即 A）' + TAG}}],
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
