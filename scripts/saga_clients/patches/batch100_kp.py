#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 100 批（T29-U93，公司底数第十八轮 · B 档「自有 logo + 打开」五国 24 户）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=100 行）。
结构同 batch99_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：OEM 30% 首选 2（SB-475 CCTVDEPO 自有品牌 SECUZI / TİRENZO；SB-478 Eurocam 自有网络品牌 Eurolink）；贴标 OEM 30% 目标 2（SB-743 Cleerline；SB-488 OctoGate）；
分销 / 自有标两可 1（SB-547 Netinet）；分销 20% 首选 GB 1（SB-1123 Connectec = PLANET 授权分销）；分销 20% 7（SB-687 Telkotim / SB-489 Portel / SB-1133 Netram / SB-1053 ServiceNet / SB-1124 Fonex / SB-454 Leoptics / SB-521 ACE）；
集成商 25% 5（SB-490 Radio Teknoloji / SB-260 HK / SB-379 TRK / SB-1047 Kamsys / SB-521 Oxford Aerials 另线）；贴标 small 4（SB-741 Canary / SB-754 FasterCable / SB-783 S.I. Tech / SB-559 VIPA / SB-061 Megatel）；WhatsApp 直报 1（SB-496 Bora）；
未坐实 1（SB-531 Dynamode）；部分坐实 3（SB-754 / SB-521 / SB-454）；KP 坐实 = 老板 / GF / Prezes / President 本人 9（SB-743 / SB-783 / SB-061 / SB-687 / SB-478 / SB-1133 / SB-488 / SB-379 / SB-547）；KP 误归属 1（SB-521 Shaun Guard = Oxford Aerials）；
拼写更正 1（SB-379 Karwat → Karwar）；国别更正 0；升 A 候选 5（SB-475 / SB-478 / SB-488 / SB-1123 / SB-547，回信即 A）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 100 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US 6 ----------
    'SB-741': [{'kp_match': 'cmckee@', 'role': '研究档联系人（职务未核；非登记高管）= 收件人' + TAG},
               {'add_kp': {'name': 'Vinh Quang Tran', 'role': 'Chief Executive Officer（CA SoS 1418771 Statement of Information）= 拍板人（抄送 / 点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'Canary Communications, Inc.（California General Corporation；CA SoS 1418771；SAM UEI WVRYXAA7DEK9）', 'founded': '1987-09-25' + TAG, 'staff': '1–10 人；<$5M', 'hq': '6040 Hellyer Avenue, Suite 150, San Jose, CA 95138',
                          'other': '第 100 批：自有品牌媒体转换器 / 数据二极管商（表内从 VOLKTEK 买 MC）→ 自有标 PoE / 光口交换机贴标 small（STI-144GP / STC-228GP）；军方 / 政府客户不提；加厚一次' + TAG}}],
    'SB-743': {'kp_match': 'ryan@cleerline.com', 'role': 'President / Partner（Cleerline Technology Group, LLC；D’Addario & Co 关联）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Cleerline Technology Group, LLC（蒙大拿；SoS 号未取；SSF 光纤专利品牌）', 'founded': '2012' + TAG, 'staff': '11–50 人（15）', 'hq': '8404 Elway Drive, Suite 2B, Missoula, MT 59808',
                         'other': '第 100 批：自有品牌（SSF 光纤 + 网络配件）+ 总裁本人收件 → **贴标 OEM 30% 目标**：Cleerline 标 STC-228GP / STC-2224GP / STI-144GP 配其光纤；B BIG；加厚' + TAG}},
    'SB-754': [{'kp_match': 'richard@fastercable.com', 'role': 'Sales Manager（FasterCable, Las Vegas）= 收件人' + TAG},
               {'kp_name': 'Juliette O', 'role': 'Director, Operations（研究档写 V. President；姓 Ozols）= 抄送' + TAG},
               {'facts': {'legal_name': 'FasterCable（fastercable.com；内华达实体名 / SoS 号未取 → 部分坐实；宾州 Faster Cables LLC 为同名他户）', 'staff': '5 人' + TAG, 'hq': '3325 W Ali Baba Ln, Ste 619, Las Vegas, NV 89118',
                          'other': '第 100 批：线缆配件经销 + 自有标工业交换机型号（EISW8-100T 等）→ 贴标 small（STI-054GP / STI-144GP）；一页纸' + TAG}}],
    'SB-783': {'kp_match': 'sales@sitech-bitdriver.com', 'name': 'Ramesh Sheth', 'role': 'President / Owner（S.I. Tech, Inc.；研究档「Ramesh S」）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'S.I. Tech, Inc.（Illinois Corporation 1983-09-22；IL SoS 文件号未取）', 'founded': '1983-09-22（开业 1984-03-01）' + TAG, 'staff': '2–10 人；<$5M', 'hq': '1101 N. Raddant Road, Batavia, IL 60510',
                         'other': '第 100 批：光纤调制解调器 / 复用器老牌小厂（军方 / 工业客户，不提军用）→ 自有标光口交换机贴标 small（STI-144GP / STI-288DGGPM）；一页纸' + TAG}},
    'SB-559': {'add_kp': {'name': 'Thomas Kosse', 'role': 'President & CEO（VIPA ControlsAmerica；研究档无 KP）= 收件人' + TAG, 'email': ''},
               'facts': {'legal_name': 'VIPA ControlsAmerica（GA 实体名 / SoS 号未取；德国 VIPA GmbH / YASKAWA 旗下北美销售服务公司）', 'founded': '1998' + TAG, 'staff': '8 人', 'hq': '980 Birmingham Rd. Ste 721, Alpharetta, GA 30004（非威斯康星）',
                         'other': '第 100 批：PLC / HMI 北美销售公司 → 工业导轨交换机配套（STI-054GP / STI-144GP / STI-0240GE）贴标 small；一页纸' + TAG}},
    'SB-061': {'kp_match': 'zack@megatelindustries.com', 'role': 'President / Sales Manager（Megatel Industries Corporation 业主；D&B / Buzzfile）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Megatel Industries Corporation（PA Corporation；PA DOS 号未取；CAGE IRRG5）', 'founded': '1991（D&B）/ 1994（自述）' + TAG, 'staff': '3 人；$0.4–2M', 'hq': '664 Wagner Court, North Wales, PA 19454',
                         'other': '第 100 批：数据通信 / 光纤批发出口商兼 OEM 品牌商（3 人）→ 贴标 small（STC-228GP / STI-144GP）；政府 CAGE 客户不提；一页纸' + TAG}},
    # ---------- TR 6 ----------
    'SB-687': {'kp_match': 'veli@telkotim.com', 'name': 'Veli Uysal', 'role': 'Genel Müdür（总经理；Anadolu Ajansı 2022-04-19 采访署名）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Telkotim Bilişim Teknolojileri Tic. Ltd. Şti.（Ankara；MERSİS 号未取）', 'founded': '2008' + TAG, 'hq': 'Çamlıca Mah. Anadolu Bulvarı Timko İşyerleri No 20 c-4, Yenimahalle / Ankara（非 İstanbul）',
                         'other': '第 100 批：光纤 / 网络基础设施分销（TTAF / HCS 光缆，D-Link / Ruijie 交换机）→ 分销 20%：STC-228GP / STC-2224GP + STI-144GP / STI-288DGGPM 配其光缆项目；加厚一次' + TAG}},
    'SB-475': [{'kp_name': 'Asuman Ozuedogru', 'name': 'Asuman Özüdoğru', 'role': 'Müşteri Temsilcisi（客户代表；官网 Hakkımızda；真实邮箱应为 asuman@，研究档误配 can@）= 抄送' + TAG},
               {'kp_name': 'Can Gurcan', 'role': '研究档联系人 can@（职务未核）= 主收件人，点名「satın alma / ürün müdürü」' + TAG},
               {'facts': {'legal_name': 'CCTVDEPO Güvenlik Teknolojileri A.Ş.（MERSİS 0203034849100015；Ticaret Sicil 70431-5 İstanbul；VKN 2030348491）', 'founded': '2004' + TAG, 'staff': '51–200 人；$1–10M', 'hq': 'Hürriyet Mh Güngören Sk 4b, Bahçelievler 34188 İstanbul（注册 Remzi Özkaya Cad. No 18 Yenibosna；门店 Perpa B Blok K8 No 836）',
                          'other': '第 100 批：**自有品牌 SECUZI / TİRENZO 的生产商兼进口商 + 站内自有标 PoE 交换机（SZNT-*）+ 全国 bayi 批发 → OEM 30% 首选 TR**：SECUZI 标 STC-028GP / STC-228GP / STC-2216GP / STC-2224GP；B BIG；加厚；升 A 候选（回信即 A）' + TAG}}],
    'SB-478': {'kp_match': 'gokhandemir@', 'role': 'CEO – Founding Manager（创办人；官网 EN About 署名 ext 14）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Eurocam GD Güvenlik Elektronik ve Bilişim Sistemleri San. Dış Tic. Ltd. Şti.（前 GD Güvenlik Sistemleri San. Dış Tic. Ltd. Şti.；MERSİS 号未取；Bursa 的 Eurocam Yapı 为他户）', 'founded': '2017' + TAG, 'staff': '11–50 人；500+ bayi', 'hq': 'Perpa Ticaret Merkezi A Blok 8. Kat No 918, 34384 Şişli / İstanbul',
                         'other': '第 100 批：**自有网络品牌 Eurolink（网络 / 连接设备进口）+ 自有安防品牌 Eurocam（2020 起自产摄像机）+ 直接进口 + 500 bayi → OEM 30% 首选 TR**：Eurolink 标 STC-028GP / STC-228GP / STC-2216GP / STC-2224GP；其官网承诺 2 年保修 → STI 3 年可对齐；B BIG；加厚；升 A 候选（回信即 A）' + TAG}},
    'SB-489': {'kp_match': 'okay.yucedag@', 'role': '研究档联系人（Sales；职务未核）= 收件人' + TAG,
               'facts': {'legal_name': 'PORTEL TEKNOLOJİ SAN. VE TİC. A.Ş.（VKN 7320767976；Ticaret Sicil 1075179 İstanbul；NACE 46.52.01）', 'founded': '2017-05-23' + TAG, 'hq': 'Yalı Mah. Kadir Sk. No 14, Helis More Residence K7 D82, 34873 Kartal / İstanbul',
                         'other': '第 100 批：工业网络 + 半导体供应小型 A.Ş.，已直采三旺（表内）→ 分销 20%：切「Marvell 管理型 L2+ 工业 PoE」STI-288DGGPM / STI-488DGGPM + 3 年保修 + MOQ 1；铁路客户守界；一页纸（不点名三旺）' + TAG}},
    'SB-490': [{'kp_match': 'salih.yildirim@', 'role': 'Project Manager（研究档；选型人）= 收件人' + TAG},
               {'facts': {'legal_name': 'Radio Teknoloji Hizmetleri A.Ş.（İstanbul Bakırköy；MERSİS 号未取）', 'founded': '2015' + TAG, 'staff': '11–50 人', 'hq': 'Ataköy 7-8-9-10. Kısım Mah. Çobançeşme E-5 Yan Yol Cad. Avrupa Residence No 8/1 A Blok D10, Bakırköy / İstanbul',
                          'other': '第 100 批：户外宽带无线（PtP / PtMP / LTE）分销 + 集成（KGYS / 港口 / 机场 / 市政；客户含 TSK → 信里不提军用）→ 集成商 25%：STI-054GP / STI-144GP / STI-288DGGPM 杆位 PoE；一页纸 + 杆位配置图' + TAG}}],
    'SB-496': {'kp_match': 'boraerim@', 'role': '业主（Facebook 主页「By Bora Teknoloji Dünyası」Ağrı；WhatsApp 已加）= 收件人' + TAG,
               'facts': {'legal_name': 'By Bora Teknoloji Dünyası（Ağrı 个体门店；无 VKN / 域名 → 部分坐实；Trabzon 的 Bora Teknoloji 为他户）', 'hq': 'Ağrı' + TAG, 'staff': '1–5 人（推定）',
                         'other': '第 100 批：弱电 / 电脑 / 安防微型门店，询盘 2 SFP + 8 PoE ×10 → WhatsApp 直报 STC-228GP（$33 ×10）+ DAP 运费；不加厚、不进群发' + TAG}},
    # ---------- DE 4 ----------
    'SB-1133': {'kp_name': 'Jürgen Hübner', 'role': 'Geschäftsführer（*1968，自 2005；HRB 19078 Wuppertal）= **拍板人本人 = 收件人**' + TAG,
                'facts': {'legal_name': 'Netram Memory GmbH（HRB 19078 Amtsgericht Wuppertal；EUID DER1608.HRB19078；资本 €25,000）', 'founded': '2005-03-08（登记 2005-04-14）' + TAG, 'staff': '2–10 人', 'hq': 'Dohlenweg 6, 42115 Wuppertal',
                          'other': '第 100 批：内存 / 光模块 / 网络配件微型电商 → 只切「配光模块一起卖的交换机」STC-110XGE（8×2.5G + 2×10G）+ STC-228GP → 分销 20%，小户，一页纸' + TAG}},
    'SB-1053': {'add_kp': {'name': 'Andreas Bude', 'role': 'CEO / Geschäftsführer（wlw 企业档；研究档无 KP）= 收件人' + TAG, 'email': ''},
                'facts': {'legal_name': 'ServiceNet EDV-Vertrieb GmbH（店名 lichtleiterkabel.com；HRB 号未取；域名方 Traffictime Handels- & Marketing GmbH）', 'founded': '1996' + TAG, 'hq': 'Provinzialstraße 40, 53859 Niederkassel',
                          'other': '第 100 批：LWL 光缆定制 / 布线 B2B 电商 → 有源件为配角 → 分销 20%，小户，一页纸：STI-144GP / STI-288DGGPM + STC-228GP' + TAG}},
    'SB-260': [{'kp_match': 'lg@hk-systeme.de', 'role': '研究档联系人（Impressum 域下；职务未核）= 收件人' + TAG},
               {'add_kp': {'name': 'Johannes Brüls', 'role': 'Geschäftsführer（Dipl.-Ing.；Impressum；HRB 105842 Düsseldorf）= 拍板人（点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'HK GmbH（HRB 105842 Amtsgericht Düsseldorf；USt-ID DE236356997；Paderborn 的 HKS Systeme GmbH 为他户）', 'founded': '未取（经营 25 年以上）' + TAG, 'hq': 'Albert-Einstein-Str. 5, 40764 Langenfeld',
                          'other': '第 100 批：消防报警 / 语音疏散 / 电声报警集成商 → IP 音频网络 PoE（STC-228GP / STC-2224GP）→ 集成商 25%，小户，一页纸' + TAG}}],
    'SB-488': {'kp_match': 'frank.menne@', 'role': 'Geschäftsführer（vertretungsberechtigt；Impressum + HRB 9944 Paderborn；创办人系，源自 HSM-Menne GmbH）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'OctoGate IT Security Systems GmbH（HRB 9944 Amtsgericht Paderborn；USt-ID DE275066387；资本 €25,000）', 'founded': '2010-10-07（登记 2010-11-19）' + TAG, 'staff': '11–50 人', 'hq': 'Friedrich-List-Str. 87, 33100 Paderborn',
                         'other': '第 100 批：**自有硬件品牌（OctoGate 防火墙 / Schulfirewall 学校整包）+ 已直采 FS.com 交换机 + GF 本人收件 → 贴标 OEM 30% 目标**：OctoGate 标 STC-228GP / STC-2224GP / STC-4424GCPM + STC-110XGE 上联；B BIG；加厚；升 A 候选（回信即 A）' + TAG}},
    # ---------- GB 4 ----------
    'SB-1123': [{'add_kp': {'name': 'Paul Jarvis', 'role': 'Managing Director（LinkedIn / Business Wales；非登记董事）= 收件人（sales@ 主送 + 点名）' + TAG, 'email': 'sales@connectec.uk'},},
                {'add_kp': {'name': 'Tao Wei', 'role': 'Director / PSC（Companies House 10933159，2025-11-25 起；母公司 Dynamic Technology Solutions Ltd 100%）= 拍板人（华人姓名 → 可选中文直联，Simon 定，默认英文）' + TAG, 'email': ''},
                 'facts': {'legal_name': 'CONNECTEC LIMITED（Companies House 10933159；VAT GB277433186；D-U-N-S 223187960；SIC 47910）', 'founded': '2017-08-25' + TAG, 'staff': '11 人（2024 账）', 'hq': 'Unit 4 Wrexham Midpoint, Dolydd Road, Wrexham LL13 7AJ（2026-07-30 起）',
                           'other': '第 100 批：**PLANET 授权分销商 + Ruijie 在售 + 2025 下半年董事全换（换货源窗口）→ 分销 20% 首选 GB**：STC-228GP / STC-2216GP / STC-2224GP 对标其 PLANET 在售价 + STI-144GP；B BIG；加厚；升 A 候选（回信即 A）' + TAG}}],
    'SB-531': {'facts': {'legal_name': 'Dynamode（dynamode.co.uk；Companies House 1 次关键词检索未命中 → 未坐实；下轮补：站点 Terms 法人名）' + TAG,
                         'other': '第 100 批：自有品牌网络 / 电脑配件商 = 贴标 OEM 30% 目标但主体未坐实 → 坐实前只发一页纸（STC-028GP / STC-228GP / STC-2224GP 贴标）；收件 sales@' + TAG}},
    'SB-379': {'kp_match': 'info@trksolutions.co.uk', 'name': 'Sahil Karwar', 'role': 'Director / PSC 75–100%（Companies House 12948953；研究档拼写 Karwat → 更正 Karwar）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'TRK SOLUTIONS LTD（Companies House 12948953；VAT 437821090；SIC 43210 + 61100；同名 07147856 为他户）', 'founded': '2020-10-14' + TAG, 'staff': '<10 人；Micro', 'hq': 'Premier Business Centre, 47-49 Park Royal Road, London NW10 7LQ（商务中心）',
                         'other': '第 100 批：CCTV / 门禁 / 报警微型安装商 → 集成商 25%，小户，一页纸：STC-028GP / STC-228GP / STC-2224GP；MOQ 1' + TAG}},
    'SB-521': [{'kp_match': 'shaun@oxfordaerials.co.uk', 'role': 'Owner / original installer, **Oxford Aerials Ltd（Wallingford 安装商）= ACE 的客户，非 ACE 人员 → 误归属**；另线集成商 25% 可直发' + TAG},
               {'add_kp': {'name': '（ACE 采购）', 'role': 'Aerials & Cable Equipment Ltd 采购 / CCTV & networking buyer（公司号与董事未取 → 下轮补）= 本户主收件人' + TAG, 'email': 'sales@aceonline.co.uk'},
                'facts': {'legal_name': 'Aerials & Cable Equipment Ltd（商号 ACE Distributors；Cheltenham；Companies House 号未取 → 部分坐实；研究档「Oxford, UK / 约 1990」有误）', 'founded': '1983' + TAG, 'staff': '11–50 人', 'hq': 'Cheltenham, Gloucestershire（01242 511511）',
                          'other': '第 100 批：天线 / 卫星 / CCTV / UniFi 全国安装商分销 → 分销 20%（sales@ 首信一页纸：STC-028GP / STC-228GP / STC-2224GP）；Shaun Guard = Oxford Aerials 另线' + TAG}}],
    # ---------- PL 4 ----------
    'SB-1047': {'add_kp': {'name': 'Piotr Błoński', 'role': '业主（CEIDG；NIP 8231551721；研究档无 KP）= 收件人' + TAG, 'email': ''},
                'facts': {'legal_name': 'KAMSYS Piotr Błoński（CEIDG 个体；NIP 8231551721；REGON 142179316；MSWiA 安防许可）', 'founded': '2010-01-14' + TAG, 'hq': 'ul. Wileńska 27, 05-120 Legionowo',
                          'other': '第 100 批：监控 / 报警 / 门禁网店 + 安装 → 集成商 25%，小户，一页纸：STC-028GP / STC-228GP' + TAG}},
    'SB-1124': {'add_kp': {'name': '（Borowscy 合伙人）', 'role': 'wspólnicy（KRS 0000317918 普通合伙；姓名未取）= 收件人 sklep@ 点名 właściciel / zakupy' + TAG, 'email': 'sklep@fonex.pl'},
                'facts': {'legal_name': 'FONEX K.T.M. Borowscy Sp. j.（KRS 0000317918；NIP 9492100567；REGON 241058180；BDO 000427576；PKD 46.52.Z）', 'founded': '2008-11-18' + TAG, 'hq': 'ul. Wręczycka 13/15, 42-202 Częstochowa',
                          'other': '第 100 批：区域安防批发 + 网店 + 安装 → 分销 20%，小户，一页纸：STC-028GP / STC-228GP / STC-2216GP' + TAG}},
    'SB-547': {'kp_match': 'marek.niewczas@', 'role': 'Prezes Zarządu（自 2002-03-07；KRS 0000096977；股东 10%，配偶 Agnieszka Niewczas 65%）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'NETINET Sp. z o.o.（KRS 0000096977；NIP 1181481416；REGON 016121659；资本 50,000 zł；前 IC Intracom Polska 项目）', 'founded': '2002-03-07（经营自 1999）' + TAG, 'hq': 'ul. Arkuszowa 18, 01-934 Warszawa',
                         'other': '第 100 批：Intellinet / Manhattan 品牌波兰运营型分销（测试 / 上市 / 营销 / 保修全包）+ 老板本人收件 → 分销 20% 或 Netinet 自有标 OEM 30%（STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W）；B BIG；加厚；升 A 候选（回信即 A）' + TAG}},
    'SB-454': {'facts': {'legal_name': 'Leoptics（leoptics.pl；CEIDG 同名命中「Leoptics Maja Matyjewicz」Łódź NIP 7251850432 / REGON 364507458，经营者对应待核 → 部分坐实；Warszawa TELEOPTICS Sp. z o.o. 为他户）', 'founded': '2018-10-07（CEIDG）' + TAG, 'hq': 'ul. Rewolucji 1905 r. 18/63, 90-207 Łódź（CEIDG）',
                         'other': '第 100 批：光模块 / CWDM 网店（Saga 不做光模块）→ 只切 10G 上联 STC-110XGE + STC-228GP → 分销 20%，微型，一页纸；表内「German brand link」无证据不采' + TAG}},
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
