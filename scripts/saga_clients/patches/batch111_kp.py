#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 111 批（T29-U104，公司底数第二十九轮 · 欧洲其他国家 B 池第 5 轮 40 户：IT 13 / CZ 4 / BY 3 / LT 2 / RS 2 / FR 2 / HR 1 / NO 1 / RO 1 / NL 1 / CY 1 / BG 1 / PT 1 / GE 1 / CH 1 / EE 1 / XK 1 / BE 1 / ES 1 / IE 1）—— 把 registry 核实结果回写研究档 KP 角色 / 法定名 / 事实。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=111 行）。
结构同 batch110_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：B BIG · 加厚一次 6（SB-479 EZY Infotech d.o.o. OIB 79541484681 ≈€6.7M 两城 Direktor Branko Novosel / SB-483 MELBYE AS 941 009 697 NOK 342M 自有品牌 贴标配套 30% Daglig leder Hege Nordahl / SB-313 Intellcom Group LLC 202441189 格鲁吉亚 Ubiquiti 官方分销 / SB-638 ПТЧ УП «Опатов» УНП 190207304 自有品牌 OPL 管理型交换机 贴标 30% Director Igor Dashchinski / SB-768 KBV DATACOM d.o.o. PIB 106983968 190 人 电信基建 仅非轨交线 / SB-807 ООО «Датастрим ДЕП» УНП 100917214 51–200 人 白俄头部分销 → 回信即次候选升 A）；
加厚 small 一次 3（SB-235 BOS ITALY S.R.L. 03576140242 自有品牌 BOS 贴标 30% / SB-333 YLI ETERNIT ACCES S.R.L. CUI 19284558 RO+HU 门禁分销 / SB-462 ETER BIOMETRIC TECHNOLOGIES SRL 02089510354 €3.95M CEO 唯一所有人 Andrea Giacobazzi 曾索 bypass 资料）；
一页纸一次 · 有回声再加厚 20（贴标 / 配套 30% 4：SB-594 KM SOLTEC S.R.L. 04466860238 Kimera 工业 PC / SB-778 UAB Enzas 303005607 自有品牌 Pyramid 摄像机 Direktorius Arūnas Ramonas / SB-146 EXSYS ITALIA S.R.L. 02375220130 自有品牌 1 人 / SB-558 UNIFORMATIC SAS 333 998 623 自有品牌配件 + 台系工业交换机；分销 20% 10：SB-514 ELECTRO PNEUMATIC SOLUTIONS DOO PIB 108600536 研究档域名误判 / SB-520 ABCtech s.r.o. 27546624 jednatel Jan Hofman / SB-838 GMI DATABOX SAS 320 290 190 Président Robert Bugnet / SB-977 eltrox.cz 经营者 E-commerce Group s.r.o. SK 47589175 / SB-245 IOTECH-ITALIA DI L. DONATO 13362610969 个体 / SB-254 SICURTECNICA S.R.L. 01400990634 / SB-726 ELETTRONICA E SICUREZZA SRL 03518240241 €1.35M +32% / SB-134 КАССАБА СИСТЕМС ООД 131403477 展会见过 CEO / SB-535 ESCAD Trade s.r.o. 60487283 30 年 CCTV 批发 / SB-752 ENIKA.CZ s.r.o. 28218167 新总经理 Lukáš Majkuth；集成 25% 6：SB-980 IP Voice Group Services B.V. KvK 61046655 / SB-554 SYSNET S.R.L. 12548250153 €5.2M / SB-972 K.N. ELECTROLOGIC SERVICES LIMITED HE 251241 Director Nikolas Konomou / SB-030 MEDIAS-COM'S SA CHE-394.326.893 2020 样品单回访 / SB-121 STORM ICT L.L.C. 科索沃 CEO Alban Beqiri 会面回访 / SB-263 Tecside BV 0795.233.912 回 RFQ 2.5G+10G）；
不动 11（SB-748 dnaelektro.cz OSVČ Lukáš Wagner 74378945 综合网店 / SB-234 Benzotronic di Benzoni Mauro 01414660397 个体门店 / SB-237 Dales srl 04273690752 暖通光伏非目标 / SB-247 jpg.lt 未坐实无 KP / SB-526 automationstore.it 未坐实验证墙 / SB-700 cctvcamara.pt 中国厂家 Vividview 葡萄牙分支 Gmail / SB-747 Digitclik di Princic Iztok 一人建设中 / SB-056 NETWORK BUSINESS SOLUTIONS OÜ 11338038 休眠 VAT 注销 2023-05 / SB-1111 查无实体 / SB-241 Tomasz Głuszek 个人 Gmail WA 维系 / SB-814 ЧСУП «Айстрим Плюс» 191523533 微型无 KP）；
坐实 33 / 部分坐实 3（SB-700 NIPC 未取 / SB-747 P.IVA 未取全 / SB-121 ARBK 编号未取）/ 未坐实 4（SB-247 / SB-526 / SB-1111 / SB-241）；
KP 坐实 = 老板 / 董事 / 总经理本人 13（SB-520 Jan Hofman / SB-594 Matteo Pinato / SB-838 Robert Bugnet / SB-479 Branko Novosel / SB-483 Hege Nordahl / SB-778 Arūnas Ramonas / SB-972 Nikolas Konomou / SB-462 Andrea Giacobazzi / SB-030 Christophe Cordonier / SB-121 Alban Beqiri / SB-263 Giovanni Desramault / SB-638 Igor Dashchinski / SB-752 Lukáš Majkuth + jednatelé Vávra / Geisler）；
法定名补全 / 更正 29；country_fix 0（SB-247 / SB-807 / SB-814 研究档国别有误但 entities iso 正确，不改；SB-977 SK 法人运营 CZ 站，iso 保持 CZ）。
旁线索（≠ 目标，另立户评估）：EXSYS 德国 / 瑞士总部（SB-146 母牌）；Storm Group（克罗地亚，SB-121 母集团）；Melbye Group AS（SB-483 母公司）；AT Networks（IE，SB-241 疑似雇主，待证）；Security Planet（BOS 意大利分销商）；DNA Group s.r.o. 24282197（SB-748 同址）；Eltrox s.r.o. Ostrava 29382289 ≠ eltrox.cz；KommaGo B.V. / voipshop.nl ≠ SB-980；EP Solution d.o.o. HR ≠ SB-514；INTELCOM GROUP 406099546 ≠ SB-313；D'ALESSANDRIS S.R.L. Supino 02452850601 ≠ SB-237；DIGITKLIK d.o.o. Trzin ≠ SB-747。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 111 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- 第 1/3 ----------
    'SB-514': {'facts': {'legal_name': 'ELECTRO PNEUMATIC SOLUTIONS DOO（商号 EP Solutions；ep-solutions.rs；PIB 108600536；MB 21032018）— 研究档域名 257.cz 为误判', 'founded': '2014-07-17' + TAG,
                         'other': '第 111 批：贝尔格莱德工业自动化分销商（PROFINET 线 + 机器人；3 办事处）→ **分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM 作现场网络第二价位 + RS 非欧盟 DAP；塞语引子）**；收件人 office@ep-solutions.rs' + TAG}},
    'SB-520': [{'add_kp': {'name': 'Jan Hofman', 'role': 'jednatel（abctech.cz 法律信息）= 拍板人（info@ / obchod@ 点名）' + TAG, 'email': '', 'source': 'https://www.abctech.cz/'}},
               {'facts': {'legal_name': 'ABCtech s.r.o.（IČO 27546624；DIČ CZ27546624；C 25333 KS Hradec Králové）', 'founded': '2008-08-28' + TAG,
                          'other': '第 111 批：Česká Skalice / Hradec Králové 网络渠道网店（提供批发合作）→ **分销 20% small，一页纸一次（换切口：主流品牌价位带之间的第二 PoE 货源 STC-028GP / STC-228GP / STC-2224GP + CZ DAP 小起订；捷语引子，点名 Jan Hofman）；再无回声 → 不动**' + TAG}}],
    'SB-594': [{'add_kp': {'name': 'Matteo Pinato', 'role': 'Fondatore / Amministratore（kmsoltec.com About）= 拍板人 / 收件人' + TAG, 'email': '', 'source': 'https://www.kmsoltec.com/'}},
               {'facts': {'legal_name': 'KM SOLTEC S.R.L.（自有工业 PC 品牌 Kimera Computers；P.IVA / CF 04466860238；REA VR-463733）', 'founded': '2017-03-20' + TAG,
                          'other': '第 111 批：Pressana (VR) 工业 PC 组装 + 工厂硬件网店（10 人；2024 营收 €2.01M）→ **贴标 / 配套 30% small，一页纸一次（STI-054GP / STI-144GP / STI-154GP 作工业 PC 整机配套，可贴 Kimera 标 + 3 年保 + MOQ 1；意语引子，Matteo 直呼）**' + TAG}}],
    'SB-748': {'facts': {'legal_name': 'dnaelektro.cz — 经营者 Lukáš Wagner（OSVČ；IČO 74378945；DIČ CZ8509045446）；同址 DNA Group s.r.o. 24282197', 'founded': '—（个体）' + TAG,
                         'other': '第 111 批：Praha 5 / Červený Újezd 个体工商户综合网店（45,000 SKU，网络仅一类）→ **不动（一人网店规则；主动询盘零售价 / 预付款）**' + TAG}},
    'SB-838': [{'add_kp': {'name': 'Robert Bugnet', 'role': 'Président（pappers / verif；全名 Robert Gérard José Bugnet）= 拍板人 / 收件人（ventes@ 点名）' + TAG, 'email': '', 'source': 'https://www.pappers.fr/entreprise/gmi-databox-320290190'}},
               {'facts': {'legal_name': 'GMI DATABOX SAS（原 SARL；SIREN 320 290 190；RCS Évry；TVA FR28320290190）', 'founded': '1980-11-18' + TAG,
                          'other': '第 111 批：Mennecy (91) 老牌工业通信 / 数据中心增值分销商（6–9 人；CA 2025 €1.59M）→ **分销 20% small，一页纸一次（换切口：STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM 作第二价位 + 3 年保 + FR DAP；法语引子）；有回声再加厚**' + TAG}}],
    'SB-977': [{'add_kp': {'name': 'Martin Kundrik', 'role': 'eltrox.cz 站点联系人（schema；职务未取）= 收件人' + TAG, 'email': '', 'source': 'https://www.eltrox.cz/'}},
               {'facts': {'legal_name': 'eltrox.cz — 经营者 E-commerce Group, s.r.o.（斯洛伐克 Bardejov；IČO 47589175；IČ DPH SK2024000066；OR Okresný súd Prešov）≠ Eltrox s.r.o. Ostrava 29382289', 'founded': '未取' + TAG,
                          'other': '第 111 批：SK 法人运营的 CZ / SK 安防网店（已上架白牌 PoE）→ **分销 20% small，一页纸一次（换切口：STC-028GP / STC-228GP / STC-2224GP 作摄像机套件 PoE SKU + 比价 + SK DAP；捷 / 斯语引子）；有回声再加厚**；iso 保持 CZ' + TAG}}],
    'SB-980': {'facts': {'legal_name': 'IP Voice Group Services B.V.（网店 ipvoiceshop.nl；Zeewolde；KvK 61046655）≠ KommaGo B.V. / voipshop.nl', 'founded': '≈2014（业务 2011）' + TAG,
                         'other': '第 111 批：微型 VoIP 服务商（网店维护中；15 次无打开）→ **集成 25% small，一页纸一次（IP 话机部署的 PoE 配套 STC-028GP / STC-228GP + MOQ 1；荷语引子）；再无回声 → 不动**' + TAG}},
    'SB-235': [{'kp_match': 'info@bositaly.it', 'role': '公司公开信箱（KP 未取；Borinato 家族推定）= 收件人，一问产品负责人' + TAG},
               {'facts': {'legal_name': 'BOS ITALY S.R.L.（原 Borinato Security S.r.l.；P.IVA / CF 03576140242；REA VI-336327；socio unico）', 'founded': '2009-11-02' + TAG,
                          'other': '第 111 批：Val Liona (VI) 自有品牌 BOS 摄像机（ONVIF 会员）+ 自有 poe / switch 类目、走分销商渠道（8 人；2024 营收 €2.54M）→ **贴标 OEM 30% 目标，B，加厚 small 一次（BOS 标 PoE 整线 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP / STI-144GP；中性包装 + 自编货号 + 3 年保）；回信 → 次候选升 A**' + TAG}}],
    'SB-245': [{'kp_name': 'L. Donato', 'role': 'Titolare（ditta individuale；Lorenzo）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'IOTECH-ITALIA DI L. DONATO（ditta individuale；P.IVA 13362610969；REA MI-2718540；域名持有人 RCC ITALY srl）', 'founded': '2024-01-25（业务 2019）' + TAG,
                          'other': '第 111 批：San Donato Milanese 一人工业 IoT 技术代表（顾问式代理小众品牌）→ **分销 20% small，一页纸一次（代理一条中性品牌工业 PoE 线 STI-054GP / STI-144GP / STI-154GP，MOQ 1 + 3 年保；意语引子）；再无回声 → 不动**' + TAG}}],
    'SB-254': [{'kp_name': 'Arena Enzo', 'role': 'Tecnico（研究档）= 收件人（info@ 点名）' + TAG},
               {'add_kp': {'name': 'Francesco De Gennaro', 'role': '创始人 / 负责人（paginemail 名录；职务未取，待证）= 拍板人（抄）' + TAG, 'email': '', 'source': 'https://www.ufficiocamerale.it/'}},
               {'facts': {'legal_name': 'SICURTECNICA S.R.L.（P.IVA / CF 01400990634；REA NA-307645）', 'founded': '1988-07-05（创立 1980）' + TAG,
                          'other': '第 111 批：那不勒斯微型安防经销（3 人；2025 营收 €769k 微亏）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP 配 IP 摄像机套件一口价 + MOQ 1 + 预付款；意语引子）；再无回声 → 不动**' + TAG}}],
    'SB-333': [{'kp_match': 'andreea.toderici@', 'role': 'Security System Engineer（研究档）= 收件人（ofertare@ 抄）' + TAG},
               {'facts': {'legal_name': 'YLI ETERNIT ACCES S.R.L.（商号 YLI Control Acces；CUI 19284558；Cluj-Napoca）', 'founded': '2006' + TAG,
                          'other': '第 111 批：RO + HU 门禁 / 安防进口分销商（11–50 人；3 办事处；已上架 UTEPO PoE）→ **分销 20%，B，加厚 small 一次（门禁 / 对讲 PoE 配套 STC-028GP / STC-228GP / STC-2224GP + 工业 STI-054GP；两国 DAP 小起订；罗语引子）；回信 → 次候选**' + TAG}}],
    'SB-479': [{'kp_match': 'petra@ezy.hr', 'role': 'Managing Director（研究档）= 收件人' + TAG},
               {'kp_name': 'David Dolenec', 'role': 'Product Manager（研究档）= 收件人（抄）' + TAG},
               {'add_kp': {'name': 'Branko Novosel', 'role': 'Direktor i član uprave（ezy.hr 法律信息 / companywall）= 拍板人' + TAG, 'email': '', 'source': 'https://www.ezy.hr/kontakti'}},
               {'facts': {'legal_name': 'EZY Infotech d.o.o.（全称 … za trgovinu；OIB 79541484681；MBS 070061024；Čakovec + Zagreb）', 'founded': '2002-05-16' + TAG,
                          'other': '第 111 批：克罗地亚两城 IT 分销商（收入 ≈€6.68M；在售台系 PoE；做 MikroTik / Ubiquiti 培训）→ **分销 20%，B BIG，加厚一次（台系 / MikroTik 价位带之间的第二 PoE 货源 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP / STI-144GP；HR DAP 小起订）；回信 → 次候选升 A**' + TAG}}],
    'SB-483': [{'kp_match': 'amm@melbye.com', 'role': 'Customer and Logistics Coordinator（研究档；非决策）= 请转产品 / 采购负责人' + TAG},
               {'add_kp': {'name': 'Hege Nordahl', 'role': 'Daglig leder / Styrets leder（proff / 1881）= 拍板人' + TAG, 'email': '', 'source': 'https://www.proff.no/'}},
               {'facts': {'legal_name': 'MELBYE AS（商号 Melbye Skandinavia Norge AS；org.nr 941 009 697；Melbye Group AS 100%；Skedsmokorset）', 'founded': '1986-05-26（集团 1907）' + TAG,
                          'other': '第 111 批：自有品牌光纤 / 基础设施产品商（48–74 人；营业额 NOK 342M；2025 税前 NOK 30.5M；te@ 已退信）→ **贴标 / 配套 30% 目标，B BIG，加厚一次（光纤到边缘的配套 PoE / 工业交换机 STC-028GP / STC-228GP / STI-054GP / STI-144GP / STI-288DGGPM，可贴 Melbye 标；NO 非欧盟 DAP 买方清关）；收件人改产品 / 采购负责人；回信 → 次候选升 A**' + TAG}}],
    'SB-554': [{'kp_match': 'stefano.cornelli@', 'role': 'Deputy CTO（研究档）= 收件人' + TAG},
               {'kp_name': 'Christian Tufariello', 'role': 'Chief Operating Officer（研究档）= 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'SYSNET S.R.L.（原 Sysnet Telematica S.r.l.；P.IVA / CF 12548250153；REA MI-1565510；Milano + Torino 等分部）', 'founded': '1998-07-30' + TAG,
                          'other': '第 111 批：三年营收 ×3.5 的 ICT 集成商（32 人；2025 营收 €5.23M；已用台系工业交换机）→ **集成 25% small，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM + STC-2224GP 作项目第二价位 + 3 年保；意语引子，Stefano 直呼 + Christian 抄）；有回声再加厚**' + TAG}}],
    # ---------- 第 2/3 ----------
    'SB-726': [{'kp_name': 'Fortunato Riccardo', 'role': '研究档 KP（info@；表内「会说中文」）= 收件人' + TAG},
               {'facts': {'legal_name': 'ELETTRONICA E SICUREZZA SRL（原 … snc di D. Ferrari & C.；P.IVA / CF 03518240241；REA VI-331657；Thiene (VI)）', 'founded': '2009-02-12' + TAG,
                          'other': '第 111 批：安防设备批发分销商（4 人；2024 营收 €1.35M +32%）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP / STC-2224GP 配摄像机 + 对讲套件一口价 + MOQ 1；意语引子，点名 Riccardo）；有回声再加厚**；中文直联由 Simon 定（默认否）' + TAG}}],
    'SB-778': [{'kp_match': 'arunas@pyramid.lt', 'role': 'Direktorius（info.lt / rekvizitai）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Mattheos Dimitras', 'role': 'Business Manager（研究档）= 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'UAB „Enzas“（商号 Pyramid.lt / Pyramid Electronics；įmonės kodas 303005607；PVM LT100009310917；Vilnius）', 'founded': '2013-02-21' + TAG,
                          'other': '第 111 批：监控 / 安防网店 + 门店（9–10 人；**自有品牌 Pyramid 摄像机 PYR-SH200X**；EN / RU / LT）→ **贴标 30% small，一页纸一次（Pyramid 标 PoE 交换机 STC-028GP / STC-228GP / STC-2224GP 配自家摄像机套件，中性包装 + 自编货号；英 / 俄文引子，Arūnas 直呼）；有回声再加厚**' + TAG}}],
    'SB-972': [{'kp_name': 'Nikolas Konomou', 'role': 'Director（LinkedIn 2009-06 起；Electrical Engineer）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'K.N. ELECTROLOGIC SERVICES LIMITED（HE 251241；VAT 10251241W；Strovolos, Nicosia）', 'founded': '≈2009' + TAG,
                          'other': '第 111 批：电气工程 / 光伏承包商（Plumettaz CY + GR 分销；网络非主业；21 次无打开）→ **集成 25% small，一页纸一次（楼宇 / 光伏场站监控的 PoE 配套 STC-028GP / STI-054GP + MOQ 1 + CY DAP；英文，Nikolas 直呼）；再无回声 → 不动**' + TAG}}],
    'SB-134': [{'add_kp': {'name': 'K. Kassabow', 'role': 'CEO / 业主（研究档展会记录；kkassabow@kassabasystems.com）= 拍板人 / 收件人' + TAG, 'email': 'kkassabow@kassabasystems.com', 'source': 'https://papagal.bg/eik/131403477/a657'}},
               {'facts': {'legal_name': 'КАССАБА СИСТЕМС ООД（Kassaba Systems Ltd.；原 ЕООД；ЕИК 131403477；ДДС BG131403477 自 2006-09-15；София 1309）', 'founded': '2005-03-25' + TAG,
                          'other': '第 111 批：微型 CCTV 直接进口商 + 安装商（6 人；2020 营业额 €627k；展会见过 CEO）→ **分销 20% small，一页纸一次（提展会会面 + STC-028GP / STC-228GP 配套件一口价 + MOQ 1 + BG DAP；保语引子）；再无回声 → 不动**' + TAG}}],
    'SB-146': {'facts': {'legal_name': 'EXSYS ITALIA - S.R.L.（P.IVA / CF 02375220130；REA CO-257326；Como）— EXSYS 品牌德国 / 瑞士总部另立户', 'founded': '1998-04-15' + TAG,
                         'other': '第 111 批：自有品牌 EXSYS 接口卡 / 工业 HUB / PoE 交换机（台湾代工）的意大利公司（1 人；2025 营收 €233k）→ **贴标 30% small，一页纸一次（EXSYS 标 STC-028GP / STC-228GP / STI-054GP 作台系代工的第二价位 + 小 MOQ；意语引子）；再无回声 → 不动**；收件人 exsys@exsys.it' + TAG}},
    'SB-234': {'facts': {'legal_name': 'Benzotronic di Benzoni Mauro（impresa individuale；P.IVA 01414660397；CF BNZMRA64R13H199Y；Ravenna）', 'founded': '1998（个体）' + TAG,
                         'other': '第 111 批：个体电子 / 安防门店 + 网店（3 人；本地零售为主；13 次无打开）→ **不动（一人网店规则）**；业主 Mauro Benzoni' + TAG}},
    'SB-237': {'facts': {'legal_name': 'Dales srl（D\'ales S.r.l.；站点 dalessandris.it「D\'Alessandris Group」；P.IVA 04273690752；Presicce-Acquarica (LE)）≠ D\'ALESSANDRIS S.R.L. Supino 02452850601', 'founded': '2010（集团 1970）' + TAG,
                         'other': '第 111 批：暖通 / 锅炉 / 光伏 / 电气材料 / 五金批发零售商（18 人；网络仅附带类目）→ **非目标行业 → 不动**' + TAG}},
    'SB-247': {'facts': {'legal_name': 'jpg.lt（经营主体未坐实；1 查即停）', 'founded': '未取' + TAG,
                         'other': '第 111 批：立陶宛语监控 / 安防网店（LAN / PoE 类目、Ajax、车牌识别；仅 info@）；法人未命中 → **未坐实 + 无 KP + 21 次无打开 → 不动（B 保留）**；研究档国别应为 LT（entities 已为 LT）' + TAG}},
    'SB-526': {'facts': {'legal_name': 'automationstore.it（经营主体未坐实；1 查即停；同名 A.I. AUTOMAZIONE INDUSTRIALE S.R.L. 03059890966 / AUTOMAZIONI INDUSTRIALI S.R.L. 02053790248 均无关联证据）', 'founded': '未取' + TAG,
                         'other': '第 111 批：自动化产品网店（站点验证墙；仅 info@；23 次无打开）→ **未坐实 → 不动（B 保留）**' + TAG}},
    'SB-535': {'facts': {'legal_name': 'ESCAD Trade s.r.o.（IČO 60487283；DIČ CZ60487283；C 27175 Městský soud v Praze；Praha 10 – Hostivař）', 'founded': '1994-03-29（业务 1993）' + TAG,
                         'other': '第 111 批：30 年 CCTV 进口批发商 + 网店（Milesight 授权；已售台系 PoE）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP / STC-2224GP 作摄像机配套的第二价位 PoE + CZ DAP 小起订；捷语引子）；有回声再加厚**；收件人 obchod@（jednatel 未取）' + TAG}},
    'SB-700': {'facts': {'legal_name': 'cctvcamara.pt（CCTVCÂMARA；Lisboa；自称 Vividview Interconnected Technology Co., Ltd. 葡萄牙分支；NIPC 未取；仅 Gmail + WhatsApp）', 'founded': '未取' + TAG,
                         'other': '第 111 批：中国 CCTV 厂家的葡萄牙门店（同行分支；24 次无打开）→ **不动**' + TAG}},
    'SB-747': {'facts': {'legal_name': 'Digitclik di Princic Iztok（impresa individuale；34170 Gorizia；P.IVA 未取全）≠ DIGITKLIK d.o.o. Trzin（SI）', 'founded': '未取' + TAG,
                         'other': '第 111 批：一人网络产品网店（站点「Stran v izdelavi」建设中；23 次无打开）→ **不动**' + TAG}},
    'SB-313': [{'kp_match': 'ekvtime@intellcom.net', 'role': 'Head of Product Management（研究档）= 收件人' + TAG},
               {'kp_match': 'soso@intellcom.net', 'role': 'Head of Procurement（研究档）= 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'შპს ინტელკომ ჯგუფი / Intellcom Group LLC（识别码 202441189；NAPR 2008-02-22；42 Tereverko St., Tbilisi）≠ INTELCOM GROUP 406099546', 'founded': '2008-02-22' + TAG,
                          'other': '第 111 批：格鲁吉亚 IT / 安防 / 供电分销商（**Ubiquiti 官方分销、Uniview 合作伙伴**；11–50 人；2025-06 工单一次）→ **分销 20%，B BIG，加厚一次（主流品牌价位带之间的第二 PoE 货源 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP；GE DAP 买方清关 + 预付款；英 / 俄文）；回信 → 次候选升 A**' + TAG}}],
    # ---------- 第 3/3 ----------
    'SB-462': [{'kp_match': 'a.giacobazzi@', 'role': 'CEO & founder；2024-08 起唯一所有人（secsolution：Marcello Canali 售股）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'ETER BIOMETRIC TECHNOLOGIES SRL（P.IVA / CF 02089510354；REA RE-250476；Rubiera (RE)；单一股东）', 'founded': '2004-02-11（登记 2004-07-15）' + TAG,
                          'other': '第 111 批：门禁 / 考勤 / 消防探测分销 + 集成商（12 人；2024 营收 €3.95M，2019 起连年增长）；CEO 本人曾索 bypass + 接线图资料 → **集成 25% small，加厚一次（门禁 / 消防网络的 PoE 供电 STC-028GP / STI-054GP / STI-144GP + 旁路需求回访，直发 Andrea 一问；意语引子）；回信 → 次候选**' + TAG}}],
    'SB-558': [{'kp_match': 'virginie@uniformatic.fr', 'role': '研究档 KP（职务待核）= 收件人；2025-12 总部迁里昂后先确认邮箱仍有效' + TAG},
               {'facts': {'legal_name': 'UNIFORMATIC SAS（SIREN 333 998 623；TVA FR43333998623；RCS Lyon（原 Bobigny）；资本 €200,000；associée unique）', 'founded': '1985-11-18' + TAG,
                          'other': '第 111 批：IT / 网络配件批发商（10–19 人；自有品牌 Uniformatic 线缆 / 电源 + 代理台系工业交换机；2025-12-01 总部自 Neuilly-sur-Marne 迁 Rillieux-la-Pape）→ **贴标 30% small，一页纸一次（Uniformatic 标 DIN 导轨 PoE STI-054GP / STI-144GP / STI-154GP 作现有工业线的第二价位 + 自编货号 + 小 MOQ；法语引子）；有回声再加厚**' + TAG}}],
    'SB-752': [{'kp_match': 'i.horackova@', 'role': '研究档收件人（职务待核）' + TAG},
               {'kp_match': 'p.gottwald@', 'role': '研究档收件人（姓名 / 职务待核）' + TAG},
               {'add_kp': {'name': 'Lukáš Majkuth', 'role': 'generální ředitel + prokurista（enika.eu 公告，2025-04-15 起）= 拍板人（邮箱未取，抄请转）' + TAG, 'email': '', 'source': 'https://www.enika.eu/'}},
               {'add_kp': {'name': 'Jiří Vávra', 'role': 'Ing.；jednatel（OR，2007-12-20 起）' + TAG, 'email': '', 'source': 'https://rejstrik.penize.cz/28218167-enika-cz-s-r-o'}},
               {'facts': {'legal_name': 'ENIKA.CZ s.r.o.（IČO 28218167；DIČ CZ28218167；C 49375 KS Hradec Králové；Nová Paka；前身 ENIKA spol. s r.o. 15055761）', 'founded': '2007-12-20（前身 1994）' + TAG,
                          'other': '第 111 批：无线控制技术制造商 + 电气元件 / 照明分销商（20,000+ 品项；网络为边缘品类；8 次无打开）→ **分销 20% small，一页纸一次（照明控制 / 楼宇项目的 PoE 供电 STC-028GP / STI-054GP 一口价 + MOQ 1；捷语引子）；再无回声 → 不动**' + TAG}}],
    'SB-030': [{'add_kp': {'name': 'Christophe Denis Cordonier', 'role': '董事 / 签字权（moneyhouse）= 拍板人（推定 Clients 表「Director Manager」）' + TAG, 'email': '', 'source': 'https://www.moneyhouse.ch/en/company/medias-coms-sa-21311210971'}},
               {'add_kp': {'name': 'Philippe Bonvin', 'role': '董事 / 签字权（moneyhouse）' + TAG, 'email': '', 'source': 'https://www.moneyhouse.ch/en/company/medias-coms-sa-21311210971'}},
               {'facts': {'legal_name': 'MEDIAS-COM\'S SA（UID CHE-394.326.893；CH-626.3.019.073-4；HR Valais；Place du Village 18, 1978 Lens）', 'founded': '2018-11-02' + TAG,
                          'other': '第 111 批：媒体 / 传播 + 电信转售微型公司（2020 样品单 IM-MC110FE ×2 / IM-FP144FE ×2 后无跟进）→ **集成 25% small，一页纸一次（回访 2020 样品 + 工业 MC / STI-054GP 现价一口价 + CH DAP 买方清关；法语引子，Cordonier 直呼）；再无回声 → 不动**' + TAG}}],
    'SB-056': [{'add_kp': {'name': 'Dmitri Simonov', 'role': '受益人（inforegister，2018-09-20 起）= WA 联系人（推定）' + TAG, 'email': '', 'source': 'https://www.inforegister.ee/11338038-NETWORK-BUSINESS-SOLUTIONS-OU'}},
               {'facts': {'legal_name': 'NETWORK BUSINESS SOLUTIONS OÜ（registrikood 11338038；原 Osaühing Angelmont；Vesse tn 9a, Tallinn）', 'founded': '2007-01-09' + TAG,
                          'other': '第 111 批：**法人休眠（VAT EE101131030 已于 2023-05-15 注销；2024 Q1 0 雇员 / 0 国税；2024 预测营业额 ≈ €0；资产 €46k；2 条法院记录）→ 不动（WA 闲聊不转商机；主动询盘预付款）**' + TAG}}],
    'SB-121': [{'kp_match': 'alban.beqiri@', 'role': 'CEO（LinkedIn / D&B；2013-09 起）= 拍板人 / 收件人；研究档邮箱域名 storm.ict.com 有误 → storm-ict.com（具体地址待核，先发 info@storm-ict.com 抄）' + TAG},
               {'kp_name': 'Vegim Zhitija', 'role': 'CTO（名录）' + TAG},
               {'add_kp': {'name': 'Elion Rexhepi', 'role': 'Sales Manager（RocketReach）' + TAG, 'email': '', 'source': 'https://rocketreach.co/storm-ict-llc-profile_b556e312f9d4c813'}},
               {'facts': {'legal_name': 'STORM ICT L.L.C.（Prishtinë；Storm Group（HR）成员；ARBK 商业编号未取；NCAGE A08RH）', 'founded': '2013-09' + TAG,
                          'other': '第 111 批：科索沃 + 北马其顿 ICT 集成商（ISO 9001 / 27001；Cisco 系项目；6–50 人）；现场说用工业管理型 PoE、拿了彩页、未发过信 → **集成 25% small，一页纸一次（会面回访 + STI-288DGGPM / STI-488DGGPM / STI-054GP 作第二价位 + XK 非欧盟 DAP 买方清关 + 预付款；英文）；回信 → 加厚**' + TAG}}],
    'SB-263': [{'kp_name': 'Giovanni Desramault', 'role': 'founder / sales（tecsideshop.be；giovanni@tecside.be 优于 orders@）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'Tecside BV（BE 0795.233.912；Kolonel Begaultlaan 11, 3012 Leuven；前身 TECside Comm.V 0567.983.696 2014–2023）', 'founded': '2022-12-22（前身 2014-11-20）' + TAG,
                          'other': '第 111 批：定制 LED 照明 + 视听安装微型公司（2.2 FTE；阿里 RFQ 8× 2.5G + 4× 10G SFP+）→ **集成 25% small，一页纸一次（直接回应 RFQ：主表若有 2.5G 多千兆型号则报之，否则 STC-2224GP / STC-4424GCPM + 10G 上联说明 + MOQ 1；荷语引子）；回信 → 加厚**；发信前核主表 2.5G 型号' + TAG}}],
    'SB-638': [{'kp_match': 'dia@opatov.ru', 'role': 'Director（研究档）= 拍板人 / 收件人（info@opatov.by 抄）' + TAG},
               {'facts': {'legal_name': 'ПТЧ УП «Опатов»（Производственно-торговое частное унитарное предприятие；УНП 190207304；ОКПО 37546484；Минск, ул. Франциска Скорины 52）', 'founded': '2001' + TAG,
                          'other': '第 111 批：电信 / 工业自动化材料设备供应商 + 系统集成商（Sumitomo 授权服务；**自有商标 OPL / OPL-SFP：光模块按总协议代工、OPL 管理型交换机 5–26 口**；阿里询盘 bypass）→ **贴标 30% 目标，B BIG，加厚一次（OPL 标 PoE 交换机 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP / STI-288DGGPM 作第二代工源 + 旁路回访 + 中性包装 / 自编货号 + 预付款；俄文）；回信 → 次候选升 A**；BY 收款 / 物流路径同 RU 议题' + TAG}}],
    'SB-768': [{'kp_match': 'dponjavic@gmail.com', 'role': '研究档 KP（Gmail；职务待核）= 收件人（office@kbvdatacom.rs 抄，一问职务 / 公司邮箱）' + TAG},
               {'facts': {'legal_name': 'Društvo za informacione tehnologije i telekomunikacije KBV DATACOM d.o.o. Beograd（PIB 106983968；MB 20718749；Zorana Žunkovića 17, Beograd）', 'founded': '2011-03-11' + TAG,
                          'other': '第 111 批：电信 / 能源 / 交通基建设计与建设工程商（APR「大型」；190 人；持铁路电信施工许可 I141E3 → **守界：只谈电信 / 能源 / 安防线，绝不提铁路**；阿里 RTS 旁路模块小单）→ **集成 25%，B BIG，加厚一次（光纤接入 / 安防 / 电力站点的工业 PoE STI-054GP / STI-144GP / STI-288DGGPM + 旁路回访 + RS 非欧盟 DAP；英文 / 塞语）；回信 → 次候选升 A**' + TAG}}],
    'SB-1111': {'facts': {'legal_name': '（未具名；无名称 / 域名 / 邮箱 / 电话可查；0 次检索）', 'founded': '未取' + TAG,
                          'other': '第 111 批：仅 12 条 WhatsApp 历史（2023-12 → 2024-11）、身份全空 → **查无实体 → 不动；Simon 若能从 WA 对出号码 / 公司名再立户**' + TAG}},
    'SB-241': {'facts': {'legal_name': 'Tomasz Głuszek（个人；Gmail；爱尔兰 +353 83；无 CRO 法人；LinkedIn 同名「AT Networks, Ireland」待证）', 'founded': '—' + TAG,
                         'other': '第 111 批：个人安装商、2 个工业 90W PoE 注入器样品已成交、WA 活跃 → **不进发送包（个人 / Gmail）；Simon 在 WA 顺手维系（STI-054GP 整机一口价）；registry 不动**' + TAG}},
    'SB-807': {'facts': {'legal_name': 'ООО «Датастрим ДЕП»（Datastream DEP；УНП 100917214（登记证 2001-06-20，Мингорисполком）；ОКПО 373712285000；Минск, ул. Мележа 1, комн. 1309）', 'founded': '2001-06-20（业务 1993 起）' + TAG,
                         'other': '第 111 批：白俄电信 / 网络 / 监控设备综合分销商（**ZyXEL / ORing / VIVOTEK / QNAP 等官方分销；51–200 人；面向集成商**；仅 info@）→ **分销 20%，B BIG，加厚一次（工业 PoE STI-054GP / STI-144GP / STI-288DGGPM 作现有台系线的第二价位 + 商用 STC-028GP / STC-2224GP + 预付款；俄文，一问采购负责人）；回信 → 次候选升 A**；研究档国别应为 BY（entities 已为 BY）；BY 收款 / 物流路径同 RU 议题' + TAG}},
    'SB-814': {'facts': {'legal_name': 'ЧСУП «Айстрим Плюс»（Частное сервисное унитарное предприятие；УНП 191523533；ОКПО 379687595000；Минск, ул. Пономаренко 35）', 'founded': '2011-02-15' + TAG,
                         'other': '第 111 批：微型家庭 / 办公 CCTV + 报警 + 门禁销售安装商（Partizan 官方经销；仅 info@）→ **不动（微型无 KP；BY 收款路径未定）**；研究档国别应为 BY（entities 已为 BY）' + TAG}},
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
