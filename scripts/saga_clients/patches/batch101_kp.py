#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 101 批（T29-U94，公司底数第十九轮 · B 档「自有 logo + 打开」五国 24 户）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=101 行）。
结构同 batch100_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 OEM 30% 目标 3（SB-532 Eclipse CCTV 自有品牌；SB-223 2M Technology 自有标 + 集成；SB-793 WorldStar 自有标 + 分销）；
分销 20% 首选 US 1（SB-621 LANshack / Atcom Services）；分销 20% 首选 TR 1（SB-494 Teleone）；分销 20% 8（SB-566 PCG（DC 线）/ SB-650 Beast（可谈贴标）/ SB-617 IPC2U（可谈贴标）/ SB-770 Lanode / SB-418 Atel / SB-556 UBF / SB-386 DVS（低概率）/ SB-493 Syserso（低中））；
分销 small 4（SB-403 Surveillance-Video / SB-385 DTS Digital / SB-390 Hunters / SB-674 Noxel）；集成商 25% 4（SB-647 Art Telekom（+分销）/ SB-871 İntenet / SB-649 Başarı（轨交守界）/ SB-472 BMAnetworks（低））；贴标 small 1（SB-199 Kore Konect 壳型预付）；采购型 small 1（SB-081 DABOS）；
未坐实 2（SB-385 DTS Digital 主体未定；SB-415 A2S）；部分坐实 5（SB-081 / SB-403 / SB-793 / SB-494 / SB-223 SoS 号）；KP 坐实 = 老板 / GF / GM / President / MD 本人 7（SB-621 / SB-871 / SB-650 / SB-647 外贸经理 / SB-493 / SB-617 / SB-770）；KP 非采购 1（SB-472 信息安全负责人）；
法定名更正 1（SB-621 Tecra Tools → Atcom Services, Inc. dba LANshack.com）；更名登记 1（SB-617 IPC2U GmbH → Industrial Personal Computer 2U GmbH 2024-11-15）；国别更正 0；升 A 候选 5（SB-621 / SB-532 / SB-566 / SB-647 / SB-650，回信即 A；SB-617 / SB-770 次候选）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 101 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US 6 ----------
    'SB-081': {'kp_match': 'zohaib@', 'role': '询盘联系人（职务未核；DABOS, Inc. 科研 / 实验室用品采购供应商）= 收件人' + TAG,
               'facts': {'legal_name': 'DABOS, Inc.（州登记号未取 → 部分坐实；DABS Inc 为同名他户）', 'staff': '小型（人数未取）' + TAG, 'hq': '美国（Bethesda, MD 一带推定；门牌未取）',
                         'other': '第 101 批：采购型供应商（替科研机构代购）→ 一页纸 small（STC-028GP / STC-228GP 按单报价）；不加厚' + TAG}},
    'SB-223': [{'kp_match': 'mohamed@2mtechnology.net', 'role': '研究档 KP（职务未核；疑为业主 / 负责人）= 收件人' + TAG},
               {'kp_name': 'Jarga Jallow', 'role': '研究档 KP（职务未核）= 抄送' + TAG},
               {'facts': {'legal_name': '2M Technology Inc.（2M Solutions Inc. 并存；TX SoS 文件号未取；Texas Security License B15309）', 'founded': '2004（自述）/ 2012（LinkedIn）' + TAG, 'staff': '11–50 人（20）', 'hq': '802 Greenview Dr, Grand Prairie, TX 75050',
                          'other': '第 101 批：自有标安防 / 热成像 + 德州安防持证集成 → **贴标 OEM 30% 目标 + 集成商 25%**（2M 标 STC-228GP / STC-2224GP / STC-4424GCPM）；加厚一次；SoS 文件号下轮补' + TAG}}],
    'SB-403': {'facts': {'legal_name': 'Surveillance-Video.com（NY 实体法定名 / DOS 号未取 → 部分坐实）', 'hq': '387 Canal Street, New York, NY 10013' + TAG,
                         'other': '第 101 批：BBB A+ 安防摄像机在线零售批发 → 分销 20% small（STC-028GP / STC-228GP / STC-2216GP）；一页纸；收件人 info@ 点名 purchasing' + TAG}},
    'SB-532': [{'kp_match': 'tony@eclipsecctv.com', 'role': 'Sales Executive（Eclipse CCTV Inc.）= 收件人' + TAG},
               {'kp_match': 'sales@eclipsecctv.com', 'role': '研究档 KP sales@（职务未核）= 抄送' + TAG},
               {'add_kp': {'name': 'Moises Faroy', 'role': 'President（FL Sunbiz P20000058672；D&B / Buzzfile）= 拍板人（点名 / 抄送）' + TAG, 'email': ''},
                'facts': {'legal_name': 'Eclipse CCTV Inc.（DBA Eclipse Security；Florida Profit Corporation；Sunbiz P20000058672，前身 P03000006534 2003 注销）', 'founded': '1998（自述；现实体 2020 重新登记）' + TAG, 'staff': '10–19 人；$1–5M', 'hq': '3900 N 29th Ave, Hollywood, FL 33020',
                          'other': '第 101 批：自有品牌 Eclipse 安防整线（含 PoE 交换机）+ 总裁可点名 → **贴标 OEM 30% 目标**（Eclipse 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM）；B BIG；加厚；升 A 候选' + TAG}}],
    'SB-621': {'kp_match': 'andrea@lanshack.com', 'role': 'President / Director of Sales（Atcom Services, Inc. dba LANshack.com）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Atcom Services, Inc. dba LANshack.com（研究档原写 Tecra Tools, Inc. = 误，Tecra Tools 为同业他户；NJ 登记号未取）', 'founded': '1993（Atcom）/ 1997（LANshack.com）' + TAG, 'staff': '11–50 人（22）；$4.4M', 'hq': '155 Meadow Rd, Suite 100, Clark, NJ 07066',
                         'other': '第 101 批：结构化布线 / 光纤跳线制造 + 数据网络配件电商 + 总裁本人收件 → **分销 20% 首选 US**（STC-228GP / STC-2224GP / STC-4424GCPM / STI-144GP 配其光纤跳线）；B BIG；加厚；升 A 候选；法定名更正' + TAG}},
    'SB-793': {'kp_match': 'rv@worldstarcctv.com', 'role': 'Business Development（WorldStar Security Cameras）= 收件人' + TAG,
               'facts': {'legal_name': 'WorldStar Security Cameras（WSSC；FL 法定名 / Sunbiz 号未取 → 部分坐实）', 'founded': '2010' + TAG, 'staff': '2–50 人；<$5M', 'hq': '500 S Dixie Hwy W, Pompano Beach, FL 33060',
                         'other': '第 101 批：自有标安防摄像机 + 分销 → **贴标 OEM 30% 目标 + 分销 20%**（WSSC 标 STC-028GP / STC-228GP / STC-2224GP）；加厚一次；部分坐实' + TAG}},
    # ---------- TR 6 ----------
    'SB-871': {'kp_match': 'ercan.ozturk@intenet.com.tr', 'name': 'Ercan Öztürk', 'role': 'General Manager（İntenet İletişim Teknolojileri Ltd. Şti.；LinkedIn）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'İntenet İletişim Teknolojileri Ltd. Şti.（İstanbul；MERSİS 号未取）', 'founded': '1993' + TAG, 'staff': '11–50 人', 'hq': 'Oruç Reis Mah. Giyimkent Sitesi, Giyimkent 2. Sokak No 56, 34237 Esenler / İstanbul',
                         'other': '第 101 批：电信 / 网络系统集成商 + GM 本人收件 → **集成商 25%**（STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W / STC-110XGE）；加厚一次' + TAG}},
    'SB-494': {'facts': {'legal_name': 'Teleone Bilgi ve İletişim Hizmetleri（İzmir；法律形式 / MERSİS 号未取 → 部分坐实；TELEON 为同名他户）', 'founded': '1999' + TAG, 'staff': '小型（<$5M）', 'hq': 'Mithatpaşa Cad. Zafer Apt. No 146 Kat 1 D 2-3, Konak / İzmir（Ankara 区域办）',
                         'other': '第 101 批：电子安防整体方案 + 品牌分销 → **分销 20% 首选 TR**（STC-228GP / STC-2224GP / STC-4424GCPM / STI-144GP）；加厚一次；收件人 info@ 点名 satın alma' + TAG}},
    'SB-566': {'kp_match': 'nalan@', 'role': '研究档 KP（姓待核；职务未核）= 收件人' + TAG,
               'facts': {'legal_name': 'PCG Bilgisayar Sistemleri Pazarlama San. ve Tic. Ltd. Şti.（İstanbul Kartal；EMIS 在册；MERSİS 号未取）', 'founded': '1998（自述）/ 2004-06-04（EMIS 登记）' + TAG, 'staff': '5–50 人', 'hq': 'Baltacı Mehmet Paşa Sok. No 4, Moment İstanbul B Blok D 77, Soğanlık, Kartal / İstanbul 34880',
                         'other': '第 101 批：服务器 / 存储 / 网络 IT 分销 → **分销 20%（DC 线 STH 为主）**：STH-2C24XF-HSI / STH-8C48DX-HSI / STH-32C-HSI + STC-448XGGPM；B BIG；加厚；升 A 候选' + TAG}},
    'SB-647': {'kp_match': 'mujde.balikcioglu@arttelekom.com.tr', 'role': 'Dış Ticaret Müdürü（外贸 / 进口经理；Art Telekom 家族企业成员）= **进口决策人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Art Telekom San. Tic. Ltd. Şti.（LinkedIn / EMIS 写 ART TELEKOM A.Ş.；Ankara Çankaya；MERSİS 号未取；关联 TECOM Mühendislik）', 'founded': '1980（自述）/ 2002-06-26（EMIS 现主体）' + TAG, 'staff': '11–50 人', 'hq': 'Mutlukent Mah. Angora Bulvarı Fesleğen Sok. No 7, Beysukent / Çankaya, Ankara 06800',
                         'other': '第 101 批：电信 / 网络系统集成 + 进口分销（管理层 Hasan / Murat Balıkçıoğlu，销售总监 Tarkan Erdoğan）→ **集成商 25% + 分销 20%**（STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W / STI-288DGGPM）；B BIG；加厚；升 A 候选' + TAG}},
    'SB-649': {'kp_match': 'hakan.ozturk@', 'role': '研究档 KP（职务未核；LinkedIn 同名 ERC Sistem 者为他人，不采）= 收件人' + TAG,
               'facts': {'legal_name': 'Başarı Mühendislik Otomasyon Elektrik Ltd. Şti.（İstanbul Ataşehir；EMIS 在册；MERSİS 号未取；联合创始人 Murat Tunçer）', 'founded': '2007-10-09' + TAG, 'staff': '28–35 人；$4–5M', 'hq': 'İnönü Mah. Kayışdağı Cad. No 128 Kat 1 D 2, 34755 Ataşehir / İstanbul',
                         'other': '第 101 批：能源自动化 / 电气工程集成 → **集成商 25%**（STI-054GP / STI-144GP / STI-288DGGPM 工业导轨）；轨交 EN 50155 守界不谈；一页纸' + TAG}},
    'SB-650': {'kp_match': 'basak.hatem@beastteknoloji.com', 'role': 'Genel Müdür / Kurucu Ortak（总经理 / 创始合伙人；BEAST GÜVENLİK TEKNOLOJİLERİ A.Ş.）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'BEAST GÜVENLİK TEKNOLOJİLERİ A.Ş.（BİGİS 名录 BEAST GÜVENLİK TEKNOLOJİ SAN. DIŞ TİCARET A.Ş.；会员号 34SND561-34077；MERSİS 号未取）', 'founded': '2021' + TAG, 'staff': '4–10 人', 'hq': 'Merdivenköy Mah. Günaydın Sok. No 4, Göztepe / Kadıköy, İstanbul',
                         'other': '第 101 批：安防技术外贸型 A.Ş. + GM / 创始合伙人本人收件 → **分销 20%（可谈贴标 OEM 30%）**（STC-028GP / STC-228GP / STC-2224GP）；加厚一次；升 A 候选' + TAG}},
    # ---------- DE 4 ----------
    'SB-556': {'add_kp': {'name': 'Jürgen Fischer', 'role': 'Geschäftsführer / Alleingesellschafter（HRB Dortmund 32518；2015 起注册地 Mühldorf a. Inn = AG Traunstein HRB 24719）= 拍板人（vertrieb@ 点名）' + TAG, 'email': ''},
               'facts': {'legal_name': 'UBF EDV Handel und Beratung Jürgen Fischer GmbH（HRB 32518 Dortmund；USt-ID DE125414228；ISO 9001:2015）', 'founded': '1981-06-25（公司合同）' + TAG, 'staff': '微型 / 小型（人数未取）', 'hq': 'Römerstr. 37, 44579 Castrop-Rauxel（注册地 Mühldorf a. Inn）',
                         'other': '第 101 批：1981 年起的工业网络配件 B2B 电商 / 分销（Industrial Ethernet / PoE / SFP / 媒体转换器 / 串口）→ **分销 20% small**（STI-054GP / STI-144GP / STI-288DGGPM + STC-228GP）；一页纸' + TAG}},
    'SB-472': {'kp_match': 'mats.hansen@bma-networks.com', 'role': 'Head of Information Security（BMAnetworks GmbH；**非采购 / 非网络选型人**）= 抄送，收件改 info@ 点名 Einkauf / Netzwerk-Projektleitung' + TAG,
               'facts': {'legal_name': 'BMAnetworks GmbH（Amtsgericht Kiel HRB 4103；LEI 529900FOV9RXV8MQPE96；原名 Dierck Sicherheitstechnik GmbH；DIERCK GROUP 成员；GF Alisa Ehrk / Wolfgang Ehrk）', 'founded': '2007-10-09' + TAG, 'staff': '18 人（2024 账；总资产 €4.5M；集团 260 人）', 'hq': 'Preetzer Chaussee 55, 24222 Schwentinental（分部 Albert-Einstein-Ring 5, 22761 Hamburg）',
                         'other': '第 101 批：企业级 IT 系统集成（网络 / 安全 / ADC）→ **集成商 25% 低概率**（STC-4424GCPM / STC-424XGGPM-280W / STC-110XGE）；一页纸即止；第二次触达一次后不动' + TAG}},
    'SB-493': {'kp_match': 'naif.kiy@syserso.com', 'role': 'Geschäftsführer（*1969；2019 起；Amtsgericht Hannover HRB 217735）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Syserso Networks GmbH（HRB 217735 Hannover；资本 €260,000；ITTC Group；原名 Corning Services GmbH 2019–2021；GF Naif Kiy / Michael Clever；Vertriebsleiter Holger Kausch）', 'founded': '2019-01-29（2021-12 更名）' + TAG, 'staff': '小型 / 中型（人数未取）', 'hq': 'Ahrensburger Straße 8, 30659 Hannover',
                         'other': '第 101 批：运营商 / KRITIS 网络方案增值分销（Ribbon 线，ISO 9001 / 45001 / 27001）+ GF 本人收件 → **分销 20% 低中概率**（STC-424XGGPM-280W / STC-448XGGPM / STC-110XGE / STH-2C24XF-HSI 作其方案配套）；一页纸 + DC 规格；不加厚' + TAG}},
    'SB-617': {'kp_match': 'barasch@ipc2u.de', 'role': 'Geschäftsführer（单独代表权；Berlin；Amtsgericht Hannover HRB 201075）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Industrial Personal Computer 2U GmbH（2024-11-15 前名 IPC2U GmbH；HRB 201075 Hannover；LEI 5299004NVERIA0XMW716；USt-ID DE250846309）', 'founded': '未取（经营 25 年以上）' + TAG, 'staff': '小型（人数未取）', 'hq': 'Frankenring 6, 30855 Langenhagen',
                         'other': '第 101 批：工业电脑 / 嵌入式分销 + 系统集成 + 自带工业网络方案品类 + 台湾采购口 + GF 本人收件 → **分销 20%（可谈 IPC2U 标 OEM 30%）**（STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM / STI-0240GE 配其工业 PC）；B BIG；加厚；升 A 候选' + TAG}},
    # ---------- GB 4 ----------
    'SB-385': {'kp_match': 'contact@dtsdigitalcctv.co.uk', 'role': '研究档 KP（职务未核）= 收件人；点名 Owner Derek Stephenson' + TAG,
               'facts': {'legal_name': 'DTS Digital（Scarborough；法人主体未取 → 未坐实；CH 06949184 DTS DIGITAL LIMITED Sheffield 2024-05 注销、董事 Southwell / Atherton 疑同名他户，不采）', 'founded': '2009（自述）' + TAG, 'staff': '2–10 人（Owner Derek Stephenson）', 'hq': '95–99 Dean Road, Scarborough, North Yorkshire YO12 7QS',
                         'other': '第 101 批：微型在线 CCTV 分销（Genie / ZIP / SPRO / Dahua 授权）→ **分销 20% small**（STC-028GP / STC-228GP / STC-2216GP）；一页纸；下轮补项：站点 Terms 法人名' + TAG}},
    'SB-386': {'kp_match': 'scott.abraham@', 'role': '研究档 KP（职务未核；DVS LTD）= 收件人；点名 Commercial Director Gavin Dunleavy / Head of Sales Josh Whitehead' + TAG,
               'facts': {'legal_name': 'DVS LTD（Companies House 04963144；注册地 c/o Midwich Limited, Diss；PSC Cooper Projects Limited 10121998 → Midwich plc 2022-01 多数股权；MD Tim Goodson；董事 Dunleavy / Fenby / Lowe / Councell）', 'founded': '2003-11-13' + TAG, 'staff': '中型（第三方 100+ 人；集团并表）', 'hq': 'Unit 3, Neptune Point, Vanguard Way, Cardiff CF24 5PG',
                         'other': '第 101 批：Hikvision 英国主分销（上市集团旗下，供应商准入正式）→ **分销 20% 低概率但体量大**（非 Hikvision 网络侧：STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W 作 PoE 交换机第二货源）；一页纸即止；不加厚' + TAG}},
    'SB-390': {'add_kp': {'name': 'Harjinder Narula', 'role': '联系人 / 负责人（construction.co.uk；董事身份未核；SSED Ltd T/A Hunters Wholesalers）= 收件人（sales@ 点名）' + TAG, 'email': 'sales@hunters-wholesalers.co.uk'},
               'facts': {'legal_name': 'SSED Ltd T/A Hunters Wholesalers（Companies House 04864055，官网 Terms；旧壳 HUNTERS WHOLESALERS LIMITED 06486469 已于 2011 注销）', 'founded': '2003（自述）' + TAG, 'staff': '2–10 人', 'hq': 'Trade City, Unit 3 Martin Road, Clivemont Park, Maidenhead SL6 7DZ（另址 Slough）',
                         'other': '第 101 批：微型多品牌电子安防批发（Hikvision / Videx / Fike / Bosch）→ **分销 20% small**（STC-028GP / STC-228GP / STC-2216GP）；一页纸；下轮补项：CH 04864055 董事 / 账目' + TAG}},
    'SB-770': {'kp_match': 'donal@lanode.com', 'role': 'Managing Director / Director（*1958；1992 起；80% 股东；Companies House 02702078）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'LANODE LIMITED（Companies House 02702078；SIC 61100；Co Sec Raquel McDonnell；Technical Manager Ian Philip）', 'founded': '1992-03-31' + TAG, 'staff': '2–10 人', 'hq': 'Unit 1 Phase 4, Albany Park, Camberley GU16 7PL（注册地 White Lodge, Saville Gardens, Camberley GU15 1DF）',
                         'other': '第 101 批：网络 / 传输 / 数据通信专业分销（媒体转换器 / 工业以太网 / PoE / SFP；KBC Networks 合作伙伴）+ 老板本人收件 → **分销 20%**（STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM + STC-228GP / STC-2224GP 对标其工业线）；加厚一次；升 A 候选' + TAG}},
    # ---------- PL 4 ----------
    'SB-199': {'facts': {'legal_name': 'Kore Konect Sp. z o.o.（KRS 0000898338；NIP 5213927829；REGON 388906180；资本 5,000 zł；PKD 32.99.Z；Warszawa 的 KORE Sp. z o.o. 为同名他户）', 'founded': '2021-05-05' + TAG, 'staff': '微型（资本 5,000 zł；人数未取）', 'hq': 'ul. Bartycka 22B/21A, 00-716 Warszawa（住宅楼）',
                         'other': '第 101 批：自有品牌布线 / 机柜 / 交换机 / UPS「制造商」实为壳型外采贴牌（面向中东经销）→ **贴标 small + 预付条款**（Kore Konect 标 STC-028GP / STC-228GP / STI-054GP，T/T 100% 预付、MOQ 1、不赊）；一页纸；不加厚' + TAG}},
    'SB-415': {'kp_match': 'ml@a2s.pl', 'role': '研究档 KP（职务未核；1 次检索未命中登记主体 → 未坐实）= 收件人' + TAG,
               'facts': {'legal_name': 'A2S（a2s.pl；登记主体 / NIP 未取 → 未坐实；MAJOA Sp. z o.o. 董事 Maciej Piotr Łuczyński 未证同人，不采）',
                         'other': '第 101 批：**未坐实**（1 次未中即停）→ 坐实前只发一页纸（STC-228GP / STC-2224GP / STI-144GP）；下轮补项：站点 Regulamin / Kontakt 页法人名 + NIP 再查 KRS / CEIDG' + TAG}},
    'SB-418': {'facts': {'legal_name': 'ATEL ELECTRONICS Sp. z o.o.（KRS 0001010225；NIP 7543356130；REGON 524050890；资本 50,000 zł；Sąd Rejonowy w Opolu）', 'founded': '2023-01-02（Sp. z o.o. 登记；业务更早，前身推定个体）' + TAG, 'staff': '小型（人数未取；第三方营收区间 3.5–9.7 mln zł）', 'hq': 'ul. Oleska 121, 45-231 Opole',
                         'other': '第 101 批：光纤 / 工业与无线通信元件进口分销，**ORing 波兰授权分销**（ITS / 能源 / EN 50155）→ Saga STI 作其「价值线」第二货源 → **分销 20%**（STI-054GP / STI-144GP / STI-288DGGPM / STI-488DGGPM / STI-0240GE 对标 ORing IPS / IGS 价）；轨交 EN 50155 守界不谈；加厚一次；董事会下轮补' + TAG}},
    'SB-674': {'facts': {'legal_name': 'Noxel Sp. z o.o.（KRS 0000799308；NIP 6762569629；REGON 384126338；资本 5,000 zł；PKD 47.91.Z）', 'founded': '2019' + TAG, 'staff': '微型（资本 5,000 zł）', 'hq': 'ul. Katowicka 16B, 41-500 Chorzów（旧址 ul. Józefowska 76, Katowice）',
                         'other': '第 101 批：微型电子 / 安防网店（摄像机 / NVR / 网络 / 路由器 / 报警）→ **分销 20% small**（STC-028GP / STC-228GP）；一页纸；收件人 kontakt@ 点名 właściciel' + TAG}},
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
