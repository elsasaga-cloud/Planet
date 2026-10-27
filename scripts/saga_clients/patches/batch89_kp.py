#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 89 批（T29-U71，公司底数第七轮 · B 档按互动强度续挖，加大批量：28 户 / 13 国）：把官方 / 准官方登记核出来的「老板 / 董事 / 股权 / 规模 / 财务 / 同行与守界判定」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=89 行；SB-745 为 88 行补核）。
结构同 batch88_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 89 批 官方登记核实 2026-10-27）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
ABR = 'https://abr.business.gov.au/Search/ResultsActive?SearchText='
UPD = {
    # ---------- GB ----------
    'SB-679': [{'add_kp': {'name': 'Michael Charles White', 'role': 'Director（2005-04-14 创立至今；1954 生 = 72 岁）+ 配偶 June White 任 Secretary = **夫妻店老板 = 联系人 Mike**；研究档原无具名 KP' + TAG, 'email': '', 'phone': '', 'source': CH + '05424607/officers'},
                'facts': {'legal_name': 'SARATOTA LIMITED（Companies House 05424607；2005-04-14；Welwyn Garden City, Hertfordshire；SIC 82990；账目下期 2027-01-31）', 'founded': '2005-04-14（Companies House）' + TAG, 'staff': '微型（夫妻两人；micro-entity 账目）' + TAG, 'size': '微型（夫妻店）' + TAG}}],
    'SB-745': {'facts': {'other': '补核（2026-10-27）：SIC 46510 计算机 / 外设 / 软件批发；账目至 2025-06-30 已报、下期 2027-03-31；CS 2025-10-20；PSC = Port Group Limited（11393630）≥75%（2020-02-03 起；此前 Elvidge / Jones / Law 各 25–50%，2016–2020）；Port Group Limited 本身 2018-06-01 成立于 Hove（168 Church Road），SIC 41100 建筑开发，曾用名 NLW HOLDINGS LIMITED（至 2019-02-20）→ 实控 = Law 家族控股壳，Tim Jones 为经营董事' + TAG}},
    # ---------- AU ----------
    'SB-546': [{'kp_match': 'sales@ness.com.au', 'role': '销售信箱联系人（Ness 是**制造商**不是经销商 → sales@ 不会买交换机）' + TAG},
               {'kp_match': 'grmace@ness.com.au', 'role': '员工（职务未核；ABR 无董事信息）—— 若为产品经理则是对的人' + TAG},
               {'facts': {'legal_name': 'NESS CORPORATION PTY LIMITED（ABN 28 069 984 372；ABN 生效 2000-04-13、GST 2000-07-01；NSW 2147 Seven Hills；商号 Ness Security Products / Nesstronics / Valet / Protect Direct）', 'founded': '≈1995（ACN 069 984 372 段）；ABN 2000-04-13' + TAG, 'staff': '澳洲报警 / 对讲 / 智能家居**制造商**（自有品牌，百人级）' + TAG, 'size': '中型（制造商）' + TAG, 'hq': 'Seven Hills NSW 2147（悉尼西）' + TAG}}],
    'SB-348': [{'kp_match': 'rnathan@cloudtronics.com.au', 'role': '推定董事 / 业主（公司上有 CLOUDTRONICS HOLDINGS PTY LTD 控股壳 = 老板双层结构；ASIC 董事付费未取）' + TAG},
               {'facts': {'legal_name': 'CLOUDTRONICS PTY LTD（ABN 46 603 072 000；控股 CLOUDTRONICS HOLDINGS PTY LTD ABN 89 692 459 537；NSW 2100 Brookvale；另有印尼 .co.id 支持信箱）', 'founded': '≈2014–2015（ACN 603xxx 段）' + TAG, 'size': '小型（IT / 网络集成 + 印尼分部）' + TAG, 'hq': 'Brookvale NSW 2100（悉尼北滩）' + TAG}}],
    'SB-398': [{'kp_match': 'nickf@osd.com.au', 'role': '员工（职务未核）—— 公司 = 1985 年起的光纤 / 工业以太网设备**制造商**（同行 + 轨交 / 国防客户 = 守界）→ 不追' + TAG},
               {'facts': {'legal_name': 'OPTICAL SYSTEMS DESIGN PTY LTD（ABN 83 003 020 504；NSW 2102 Warriewood）', 'founded': '≈1985（ACN 003 020 504 段；官网自述）' + TAG, 'size': '小型 / 中型制造商（同行）' + TAG, 'hq': 'Warriewood NSW 2102' + TAG}}],
    'SB-943': [{'kp_name': 'Pete Monaghan', 'role': '职务未核；Dorani 为墨尔本自有品牌对讲 / 门禁进口商（ABR 以 Trading Name 登记 → 老板用信托 / 旧壳经营）→ 下一封写他本人' + TAG},
               {'facts': {'legal_name': 'DORANI PTY LTD（ABR 名称类型 Trading Name，ABN 57 909 759 767；VIC 3121 Richmond；实体名待 View 页）', 'size': '小型（自有品牌进口商）' + TAG, 'hq': 'Richmond VIC 3121（墨尔本）' + TAG}}],
    'SB-345': [{'kp_match': 'sales@andcorp.com.au', 'role': '推定创办人 / 董事（公司名 And-corp 取自姓氏；自有品牌 Yamasaki IoT）= **老板 = 联系人**（ASIC 付费未取）' + TAG, 'name': 'Philip Anderson'},
               {'facts': {'legal_name': 'ANDCORP ENTERPRISES PTY. LTD.（ABN 93 610 329 934；NSW 2176 Wetherill Park；品牌 Yamasaki IoT）', 'founded': '≈2016（ACN 610xxx 段）' + TAG, 'size': '小型（进口分销 + 自有品牌）' + TAG, 'hq': 'Wetherill Park NSW 2176（悉尼西）' + TAG}}],
    'SB-503': [{'kp_match': 'harry.courtice@elpro.com.au', 'role': '职务未核；公司 = 布里斯班工业无线制造商 ELPRO（2019 新法人）→ 问「网络配套是否本地选型」' + TAG},
               {'facts': {'legal_name': 'ELPRO TECHNOLOGIES PTY LTD（ABN 98 634 237 933；QLD 4014 Nundah）', 'founded': '≈2019（ACN 634xxx 段；ELPRO 品牌 1990 年代起，2019 实体 = 重组后新设，待核）' + TAG, 'size': '小型 / 中型（工业无线制造商）' + TAG, 'hq': 'Nundah QLD 4014（布里斯班）' + TAG}}],
    # ---------- IL ----------
    'SB-696': [{'kp_match': 'yair@aironix.co.il', 'role': 'Manager / 经营者（ח.פ. 515461101 公司 2016-05-30 成立；ORing 以色列授权分销；ISO 9001 + 国防部供应商证 11005959）= **老板 = 联系人**；**守界：军工项目 PASS，只报商用 24 口**' + TAG},
               {'kp_match': 'info@aironix.co.il', 'role': '总信箱联系人（Eytan Birenzwige；职务未核）' + TAG},
               {'facts': {'legal_name': 'Aironix Systems Ltd（ח.פ. 515461101；2016-05-30；Kadima；私人有限公司；最近年报 2019）', 'founded': '2016-05-30（以色列公司登记处镜像）' + TAG, 'staff': '微型（经营者 Yair + 销售 Shiri Amzaleg；工业网络分销）' + TAG, 'size': '微型' + TAG, 'hq': 'Kadima-Zoran（特拉维夫北）' + TAG}}],
    # ---------- CA ----------
    'SB-144': [{'kp_match': 'robert@bsdnetworks.com', 'role': 'Owner / President（1982 创立至今，44 年；≈19 人；自有品牌光纤转换器 / 交换机 / SFP 经 Graybar Canada 分销）= **老板 = 联系人**；他问「自产还是 OEM」→ 答 SmartByte 自有工厂 + Saga 渠道，OEM 30% 贴 BSD 标' + TAG, 'name': 'Robert Lichtenstein'},
               {'facts': {'legal_name': 'BSD International Marketing（商号 BSD Networks；Concord / Woodbridge, Ontario；安省登记号未取 —— Ontario 登记处 JS）', 'founded': '1982（ZoomInfo / 官网）' + TAG, 'staff': '≈19 人（ZoomInfo）' + TAG, 'size': '小型（自有品牌进口商）' + TAG, 'hq': 'Concord (Vaughan), Ontario（多伦多北）' + TAG}}],
    'SB-970': [{'kp_name': 'Kalai Kalaichelvan（Dr.）', 'role': 'Founder, President & CEO（联邦公司 3921174，2001-07-16；母公司 PomeGran Inc. 含 3 家 ISP）—— 不直接写，抄送' + TAG},
               {'add_kp': {'name': 'Saf Assadi', 'role': 'CTO = 无线基站 / 工业 PoE 选型人 → 写他（STI 工业系列 -40℃）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.federalcorporation.ca/corporation/3921174'},
                'facts': {'legal_name': 'EION Inc.（Corporations Canada 3921174；BN 870048014；2001-07-16；260 Terence Matthews Cres, Ottawa ON；母公司 PomeGran Inc.，旗下 ISP CochraneTel / Canquest / Digicom）', 'founded': '2001-07-16（Corporations Canada）' + TAG, 'staff': '≈40 人（2009）；LinkedIn 51–200；高管 CEO Kalaichelvan / CTO Assadi / VP Eng Sumit Kumar / VP Sales Mistry' + TAG, 'size': '小型 / 中型（无线设备商 + ISP 集团）' + TAG}},
               {'add_kp': {'name': 'Manny Mistry', 'role': 'VP Sales = ISP 接入侧 24 口管理型选型人 → 写他；研究档原收件 harshul@ 非决策人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.federalcorporation.ca/corporation/3921174'}}],
    # ---------- TR ----------
    'SB-149': [{'kp_match': 'mustafa@klasnet.com.tr', 'role': '用户表联系人（Bursa Nilüfer；公司 2021 起营业、团队 14 年经验；法定类型 / 股东未取 —— 1 次检索仅命中官网）' + TAG},
               {'facts': {'staff': '10+ 人（自述）；2021 新店' + TAG, 'size': '微型 / 小型（2021 新集成商）' + TAG}}],
    'SB-186': [{'kp_match': 'info@basaranelektronik.net', 'role': 'Boss / 业主 + 技师（LinkedIn：25 年电子行业；Gömeç / Balıkesir 一人安防安装店；推定 şahıs）= **老板 = 联系人**' + TAG},
               {'facts': {'staff': '微型（1–3 人安装店）；注意同名干扰（Başaran Group 建筑集团 / basaranelektronik.com 2024 新店均非本户）' + TAG, 'hq': 'Mithatpaşa Mh. Hasan Şen Sk. 23/30, Gömeç / Balıkesir（爱琴海 Edremit 湾）' + TAG}}],
    'SB-301': [{'kp_match': 'scbalkis@ebatek.com', 'role': '推定创办人 / 业主（foursquare 本店 10+ 次签到「Coşkun B.」；公司 2005 Gaziantep 成立，软件 + IT + 网络 / 光纤工程）—— 未证实' + TAG},
               {'facts': {'hq': 'İncilipınar Mh. 36001 Nolu Sk. Emir İş Merkezi No:8/B, Şehitkamil / Gaziantep（东南部）' + TAG, 'size': '微型 / 小型（估 5–15 人）' + TAG}}],
    'SB-457': [{'kp_match': 'info@pavotek.com.tr', 'role': 'Project Manager（2022 起；前 CTech）—— 公司 = 400 人国防电子制造商，自研军民两用交换机 / 路由器（守界 + 同行）→ **不追**' + TAG, 'name': 'Serkan Ertürk'},
               {'kp_match': 'hilal.kirlioglu@pavotek.com.tr', 'role': '职能未核（国防电子厂员工）—— 不追' + TAG},
               {'facts': {'legal_name': 'PAVO TASARIM ÜRETİM ELEKTRONİK TİC. A.Ş.（Pavotek；Teknopark İstanbul Pendik + Orhanlı 工厂；董事长 Dr. Alper Özbilen）', 'founded': '2003（Teknopark İstanbul）' + TAG, 'staff': '300（2021）→ 400+（官网）；LinkedIn 201–500' + TAG, 'size': '中型 / 大型（国防电子制造商 = 守界 + 同行）' + TAG, 'hq': 'Pendik / İstanbul（Teknopark）' + TAG}}],
    'SB-861': {'facts': {'founded': '1984-01-27（EMIS）；原 Ltd. Şti. 后转 A.Ş.' + TAG, 'staff': '76–80 人（2026）/ Kompass 100–249；19 省分支；品牌 Assmann / ATEN / Digitus / Lindy / PLANET / Teltonika / Tumtec / Huawei eKit；DMO 目录供应商；进口自台湾 / 德国 / 波兰' + TAG, 'size': '中型（全国 IT 分销商）' + TAG, 'other': '登记：Ankara Ticaret Sicili（Çankaya）1750038872（Kompass）；信里不提 PLANET / 台湾' + TAG}},
    # ---------- DE ----------
    'SB-429': {'facts': {'legal_name': 'Murrelektronik GmbH（Amtsgericht Stuttgart HRB 270279；LEI 529900J3OOQZY4CQNQ96；Grabenstr. 29, 71570 Oppenweiler）', 'founded': '1975-09-24（Handelsregister）' + TAG, 'staff': '大型自动化元件制造商（Hafner 家族控股；GF Jürgen Erkert + Ulrich Viethen；≥10 国子公司；自有工业交换机线；Stammkapital €5M）' + TAG, 'size': '大型（同行上游 → 不追；收件 shop@ 为网店客服箱）' + TAG, 'hq': 'Oppenweiler（斯图加特北）' + TAG}},
    'SB-543': [{'add_kp': {'name': 'Dimitrios Koutrouvis', 'role': 'Geschäftsführer（2024-10-08 起；与 Amphenol 高管 D\'Amico / Lampo 同日任命 = 公司 2024-10 起属美国 Amphenol 集团）= 研究档收件人 dimitrios.koutrouvis@luetze.com 本人 → **联系人 = 德国总经理**，但采购已集团化 → 只写一封问「网络 / 连接线是否仍本地选型」' + TAG, 'email': 'dimitrios.koutrouvis@luetze.com', 'phone': '', 'source': 'https://www.northdata.de/Friedrich%20L%C3%BCtze%20GmbH,%20Weinstadt'},
                'facts': {'legal_name': 'Friedrich Lütze GmbH（Amtsgericht Stuttgart HRB 740258；LEI 529900QY4FK0M7B3P846；Bruckwiesenstr. 17-19, 71384 Weinstadt；与 Luetze International GmbH 利润转移协议；2024-10 起 Amphenol 集团）', 'founded': '2012-02-07（现法人；创业 1958）' + TAG, 'staff': '2024：Umsatz €74.8M、Bilanzsumme €38.4M；GF 3 人 + Prokura 3 人；商标 LÜTZE CABLEFIX / LIMO-Box / PANELCON / LUNA / LUCI RAIL' + TAG, 'size': '中型（€75M；Amphenol 子公司）' + TAG, 'hq': 'Weinstadt（斯图加特东）' + TAG}}],
    # ---------- CZ ----------
    'SB-605': [{'add_kp': {'name': 'Michal Vodička', 'role': 'Předseda představenstva（董事长；创始人 Karel Vodička 之子；所有人 MV elektro 100%）—— 不直接写；下一封写采购部「datové sítě」品类经理，不发 nabidky@' + TAG, 'email': '', 'phone': '', 'source': 'https://or.justice.cz/ias/ui/rejstrik-$firma?ico=26279690'},
                'facts': {'legal_name': 'ELKOV elektro a.s.（IČO 26279690；DIČ CZ26279690；KS Brno B 3718；LEI 31570010000000108638；基本资本 33,000,000 Kč）', 'founded': '2002-03-04（Obchodní rejstřík）' + TAG, 'staff': '500–999（RES）/ ≈700（2025）；集团营收 55 亿 Kč（≈ €2.2 亿）；33 家分店；董事会 6 人（Vodička / Mareš / Škrhák / Havlíček / Kobylková / Sedláčková）' + TAG}}],
    'SB-680': [{'kp_match': 'p.simek@schrack.cz', 'role': '产品 / 销售经办（12 封 3 次打开 0 回）—— 不再写经办' + TAG},
               {'add_kp': {'name': 'Ing. Marek Zacios', 'role': 'Jednatel + ředitel（1998-09-22 起；**2005 起集团 Schrack Technik GmbH 共同所有人**）= 拍板人 → 下一封写他：Schrack 贴牌 PoE 第二货源（选型在维也纳产品管理，他能转样）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.podnikatel.cz/rejstrik/schrack-technik-spol-s-r-o-15039137/'},
                'facts': {'legal_name': 'Schrack Technik spol. s r.o.（IČO 15039137；DIČ CZ15039137；MS Praha C 5437；基本资本 16,000,000 Kč；母公司 Schrack Technik GmbH 维也纳）', 'founded': '1991-08-27（Obchodní rejstřík）' + TAG, 'staff': '中型（捷克子公司；jednatelé Zacios / Chroust / Gletthofer；自有品牌网络产品）' + TAG, 'size': '中型（集团大型）' + TAG, 'hq': 'Dolnoměcholupská 1339/2, Praha 10 – Hostivař' + TAG}}],
    # ---------- US ----------
    'SB-352': [{'kp_name': 'Ken Misterka', 'role': 'VP Purchasing（2001 起）/ VP Logistics（2008 起）= **采购拍板人本人** —— 制造商采购要的是配套 / 贴牌，不是价表' + TAG},
               {'kp_name': 'Peter Polus', 'role': 'Founder / Chairman（1992 创立；Polus 家族所有；CEO 为 A. Peter Polus III）' + TAG},
               {'facts': {'legal_name': 'Fiberdyne Labs, Inc.（NY S-Corp；SAM UEI L689L2J632M7，登记 2001-10-04、有效至 2026-10-31；127 Business Park Dr, Frankfort NY 13340）', 'founded': '1992（Herkimer NY；SAM 开业日 1994-08-23）' + TAG, 'staff': '51–200 人（LinkedIn / ZoomInfo）；光纤产品制造商（CATV / 电信）；SAM 登记 = 政府项目（TAA 限制 → 只走商业线）' + TAG, 'size': '中型（家族制造商）' + TAG, 'hq': 'Frankfort, New York（Utica 东）' + TAG}}],
    'SB-365': [{'kp_match': 'sales@robofiber.com', 'role': '销售信箱（29 封 4 次打开 0 回）—— 改写老板本人' + TAG},
               {'add_kp': {'name': 'Radu Matei', 'role': 'Co-Founder / CEO / Director / 注册代理人（CA SoS 3540849，2013-01-25）= **一人公司老板 = 该写的人**；自有品牌 ROBOFIBER（USPTO 4854935 含以太网交换机）→ OEM 30%' + TAG, 'email': '', 'phone': '', 'source': 'https://www.bizprofile.net/ca/alamo/robofiber-inc'},
                'facts': {'founded': '2013-01-25（California SoS）' + TAG, 'staff': '≤10 人（6，Datanyze）；营收估 $1.3–6M 区间（第三方，不采信）' + TAG, 'size': '微型（一人公司 + 贴牌电商）' + TAG, 'hq': 'Alamo, California（PMB 信箱地址）' + TAG}}],
    'SB-094': [{'kp_match': 'steve.bradley@maxcomcorp.com', 'role': 'CEO（2008 起；兼 Sonlight Communications 总裁；前 Comcast 工程总监）= **老板 = 联系人**；**公司在加州 Fair Oaks（美国），用户表国别 CA 实为加州缩写误判 → 按 US 处理（FCC，无 ISED）**' + TAG},
               {'kp_name': 'Tom Maguire', 'role': 'Sales Executive（Hickory NC）' + TAG},
               {'facts': {'legal_name': 'Maxcom, Inc.（California；7996 California Ave Ste E, Fair Oaks CA 95628；州登记号未取）', 'founded': '2000-01（官网）' + TAG, 'staff': '2 人（RocketReach；外包生产）' + TAG, 'size': '微型（光纤传输设备小厂）' + TAG, 'hq': 'Fair Oaks, California, USA（非加拿大）' + TAG}}],
    'SB-759': [{'kp_match': 'eric@futurereadysolutions.com', 'role': 'Founder & President（2014 创立、2015 启动；前 PPC / Belden / Perfect Path 代理人）= **老板 = 联系人**；公司 = AV 集成渠道「代理 + 分销」平台，服务 1,500+ 集成商' + TAG},
               {'facts': {'legal_name': 'Future Ready Solutions（Bonita Springs, Florida；法定后缀未取 —— Sunbiz ✗）', 'founded': '2014（CB Insights）/ 2015 初启动（官网）' + TAG, 'staff': '小型（估 5–15 人）；CEDIA / InfoComm / ProSource / Azione 会员' + TAG, 'size': '小型（渠道代理 + 分销）' + TAG, 'hq': '24551 Production Circle Ste 3, Bonita Springs FL 34135' + TAG}}],
    # ---------- LT ----------
    'SB-789': [{'add_kp': {'name': 'Valdemaras Narkovičius', 'role': 'Direktorius / Generalinis direktorius（2019-06-21 起）= 拍板人；研究档原无具名 KP（24 封全寄 info@）→ 下一封写他：viSar 贴牌 PoE（OEM 30%）+ 分销 20% 并列' + TAG, 'email': '', 'phone': '', 'source': 'https://rekvizitai.vz.lt/en/company/sareme/manager/'},
                'facts': {'legal_name': 'UAB „SAREME“（įmonės kodas 110629811；PVM LT106298113；1994-06-16；股本 €630,000；Vytenio g. 46, LT-03229 Vilnius + Kaunas 分部；品牌 viSar）', 'founded': '1994-06-16（Registrų centras 镜像）' + TAG, 'staff': '22–23 人（SODRA 2026-10）；**2025 营收 €9.22M；2023 营收 €10.82M / 净利 €349k**；平均工资 €3,778' + TAG, 'size': '小型（€9–11M 安防分销商，立陶宛民营市场领先）' + TAG, 'hq': 'Vilnius（Vytenio g. 46）' + TAG}}],
    # ---------- ES ----------
    'SB-424': [{'add_kp': {'name': 'Fiammetta Cometto', 'role': 'Presidenta del Consejo de Administración（董事会 7 人；意大利姓 → 推定意资控股）—— 不直接写；2026-10-21 BORME 合并吸收 → 2027-01 后写产品管理 / compras' + TAG, 'email': '', 'phone': '', 'source': 'https://www.einforma.com/informacion-empresa/golmar-sistemas-comunicacion'},
                'facts': {'legal_name': 'GOLMAR SISTEMAS DE COMUNICACIÓN, S.A.（CIF A08370314；RM Barcelona tomo 24.484 folio 192；资本 €1,239,400.23；曾用名 Sistemas de Comunicación Golmar SA）', 'founded': '1975-04-09（Registro Mercantil 镜像）' + TAG, 'staff': '100–112 人（2022–2026）；销售 €6–30M 区间；CNAE 2640；审计 Gabinete Audiwork；**BORME 2026-10-21 Fusión y absorción**' + TAG, 'size': '中型（对讲 / 视频门禁制造商）' + TAG, 'hq': 'C/ Silici 13-25, Pol. Ind. Famades, 08940 Cornellà de Llobregat (Barcelona)' + TAG}}],
    # ---------- RU ----------
    'SB-899': [{'kp_match': 'zakupki@dozor23.ru', 'role': 'Руководитель отдела продаж（销售部主管，兼采购信箱 zakupki@）= 经办；老板 = Директор Завгородний（dir@）→ 俄语信写他、抄 dir@' + TAG, 'name': 'Алифанов Сергей Игоревич'},
               {'add_kp': {'name': 'Завгородний Василий Васильевич', 'role': 'Директор + ИП（零售网主体 ИП Завгородний В. В.；集团另含 ООО «ПожЮг-Сервис» / ООО «БСК Дозор»）= 老板' + TAG, 'email': 'dir@dozor23.ru', 'phone': '', 'source': 'https://anapa.dozor23.ru/company/staff/'},
                'facts': {'legal_name': 'ГК «Дозор23» = ИП Завгородний Василий Васильевич（零售网）+ ООО «ПожЮг-Сервис» + ООО «БСК Дозор»（ИНН 未取 —— 首张形式发票时问 реквизиты）', 'staff': '小型（Краснодар / Анапа / Славянск-на-Кубани / Темрюк 4 城门店 + 安装队；估 15–30 人）' + TAG, 'hq': '350000 Краснодар, ул. Кропоткина 50, оф. 303А（总部）；Анапа ул. Чехова 81' + TAG}}],
    # ---------- PT ----------
    'SB-1023': [{'kp_match': 'office@dipol.pt', 'role': '办公室信箱（不再发）' + TAG},
                {'add_kp': {'name': 'Ricardo Manuel da Silva Vieira', 'role': '推定 sócio-gerente（一人有限公司 = 老板；民防局 SCIE 设备实体登记负责人，证书至 2027-09）→ 下一封写他' + TAG, 'email': 'ricardo.vieira@skuatechnology.com', 'phone': '', 'source': 'https://prociv.gov.pt/media/evnd50kk/listagem_773_24-01-2025.pdf'},
                 'facts': {'legal_name': 'SKUA TECHNOLOGY, UNIPESSOAL LDA（NIPC 508525934；CRC Braga；资本 €25,000；CAE 46502；商号 SKUA Tech；DIPOL Ibéria 葡西代理）', 'founded': '2008-03-28（Registo Comercial 镜像 + 官网）' + TAG, 'staff': '小型（一人公司；估 5–15 人；2023–2025 资产负债表已存，付费未取）' + TAG, 'size': '小型（安防分销 + B2B 网店）' + TAG, 'hq': 'Rua da Quintã, Pavilhão 21, Frossos, 4700-023 Braga' + TAG}}],
    # ---------- CY ----------
    'SB-992': {'facts': {'founded': '1983-03-15（HE 19231；塞浦路斯登记处 JS 不可抓，批 82 已关闭 → 本批仅建档）' + TAG, 'other': '底数止于 HE 号 + D&B 主事人 Charalampous；分销 20%；写 p.christos 抄 Charalampous' + TAG}},
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
