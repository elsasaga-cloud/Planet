#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 110 批（T29-U103，公司底数第二十八轮 · 欧洲其他国家 B 池第 4 轮 40 户：IT 14 / ES 8 / LT 3 / CZ 2 / CH 2 / RO 2 / BE 2 / FR 2（1 户实为 TW）/ HU 1 / MD 1 / SE 1 / SK 1 / PT 1 / CY 1 / GE 1 / GR 1）—— 把 registry 核实结果回写研究档 KP 角色 / 法定名 / 事实。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=110 行）。
结构同 batch109_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：分销 20% · B BIG · 加厚一次 7（SB-1005 ASIT S.p.A. 06221270017 €41.8M 42 人 5 分公司 AD Jacopo Ganz / SB-195 BK grupė UAB 210599550 €41.9M 95 人 波罗的海四国 / SB-277 INSTANT BYTE SL B83680082 36 人 >€20M CEO Juan Prieto / SB-287 S. & A. S.R.L. 01887850129 5 网点 CEO Mauro Brunazzo / SB-437 TPOLE S.R.L. 02978370183（前身 02545250967）€8.8M 15 人 Pietro Milani / SB-576 MATRIX ELECTRONICA SL B79611794 60 人 Flexitron 集团 Webdyn / SB-593 SMART TECH IBD GLOBAL SOLUTIONS S.L.U. B63904445 IBD Global 100+ 人 Administrador Jordi Bassa → 回信即 A）；
贴标 / 配套 30% small · 一页纸一次 2（SB-436 Steplock access AB 559105-9992 自有门禁品牌 Steab 集团 / SB-444 Tritonsystems spol. s r.o. 48060658 ParkIS 停车系统制造商 Lupták 家族）；
一页纸一次 · 有回声再加厚 17（SB-1087 TEHNO ELECTRIC SRL 16179086 / SB-078 SITIS Sàrl CHE-150.026.203 / SB-126 CABLEWINDOW SL B83027185 原 HAI NUO / SB-127 IZUX INGENIERIA Y SEGURIDAD SL B98126444 / SB-130 BONMAG INTERNATIONAL S.R.L. 37299107 / SB-230 ADVANCED INNOVATIONS S.R.L. 04994260968 UTEPO 意大利独家 营收腰斩 / SB-265 Videotronic AG CHE-107.888.942 2026 起 VIDEOR 控股 / SB-269 Contradata Milano S.r.l. 04099800155 / SB-289 SISTEMI AVANZATI ELETTRONICI S.R.L. 01925460022 仅工业线 / SB-290 SOLPAKUTEC INDUSTRY DP 03085880213 个体户 / SB-292 Tesla Networks BV BE 0830.294.165 非车载 / SB-417 ALIDEX NETWORKS S.R.L. 10924650962 / SB-434 S CONNECT S.L. B64872484 SPHINX 子公司 / SB-439 E.V. EXXELL VISION SAS 493 179 089 / SB-573 INTEGRA NETWORK AND EMBEDDED SYSTEMS SL B84961267 仅工业线 / SB-601 OPTIVISUS, LDA 502 752 980 / SB-644 A.K. ART 2 SOFT LIMITED HE 147954 / SB-259 Dourte SRL BE 0684.917.295）；
并线 1（SB-832 Alidex Iberia = SB-417 西班牙站，无独立法人）；
不动 13（SB-1079 SPESA ELETTRICA S.C.A.R.L. 08699710961 0 雇员电气网店联合体 / SB-1084 Frekvent Forklift Kft. 12678859-2-03 叉车配件 / SB-469 Novy Telecom s.r.o. 28481968 采购代理 / SB-266 Axilogi s.r.o. 10964703 代表人注销 + 法院 opatrovník / SB-272 ELECTRONIK HOUSE S.r.l.s. 03568370369 €900 股本小店 / SB-297 Gorgos Cristian Gmail 查无实体 / SB-950 Linenet LLC 404486757 WA 20 次 0 回 / SB-481 Itegra, MB 微型无 KP / SB-491 Rass-security systems 305706724 微型网店 / SB-021 星通資訊 Loop Telecom 22099863 台湾上市同行 / SB-155 JguyTech Gmail 查无实体 / SB-075 ΓΕΜΚΑ Καρύδη Αφοί Ο.Ε. 锁具 / SB-832 并线计入上行）；
坐实 33 / 部分坐实 5（SB-266 卷号不一致 / SB-832 无独立法人 / SB-481 代码未取 / SB-491 法人形式未取 / SB-075 ΑΦΜ 待证）/ 未坐实 2（SB-297 / SB-155）；
KP 坐实 = 老板 / 董事 / 总经理本人 15（SB-078 Arno Freudenreich / SB-1005 Jacopo Ganz / SB-127 Igor Vidal Guimerá / SB-265 Christos Sgouros / SB-269 Alessandro Damian / SB-277 Juan Prieto / SB-287 Mauro Brunazzo / SB-290 Dominik Prieth / SB-292 Bart Pen / SB-437 Pietro Milani / SB-439 Jean-Edmond Rozowykwiat / SB-444 Stanislav Lupták / SB-593 Jordi Bassa / SB-644 Thomas Thoma / SB-230 Fabio Cavalleri VP）；
法定名补全 / 更正 24；country_fix 0（SB-021 实为 TW 制造商，仅注明不改；SB-481 / SB-491 研究档「意大利」有误但 entities iso LT 正确，不改）。
旁线索（≠ 目标，另立户评估）：VIDEOR E. Hartig GmbH（Rödermark，自有品牌 eneo，2026 起控股 SB-265）；SPHINX Computer Vertriebs GmbH（法兰克福，SB-434 母公司）；Flexitron Group（SB-576 母公司）；Steab Förvaltning AB（SB-436 集团）；Garma Electrónica, S.L. B20178372（研究档误入，与 SB-832 无关）。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 110 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- 第 1/3 ----------
    'SB-1079': {'facts': {'legal_name': 'SPESA ELETTRICA S.C.A.R.L.（società consortile；P.IVA / CF 08699710961；REA MI-2042985）', 'founded': '2014-07-28' + TAG,
                          'other': '第 110 批：Assago (MI) 电气材料网店联合体（多家电气批发商共有；0 雇员；2025 营收 €774k；仅意大利境内发货；「switch」= 电气开关）→ **不动（平台 / 非目标）**' + TAG}},
    'SB-1084': {'facts': {'legal_name': 'Frekvent Forklift Kft.（原 PHOENIX FORKLIFT Kft.；adószám 12678859-2-03；cégjegyzékszám 03-09-109129）', 'founded': '2001-06-19' + TAG,
                          'other': '第 110 批：Jánoshalma 叉车 / 建筑机械配件批发 + 网店（2025 净营收 HUF 1.08bn ≈ €2.7M）；表内「工业 FS」为误判 → **非目标行业 → 不动**' + TAG}},
    'SB-1087': {'facts': {'legal_name': 'TEHNO ELECTRIC SRL（CUI RO16179086；J05/330/2004）≠ 同名 TEHNOELECTRIC SRL 16855137', 'founded': '2004-02-25' + TAG,
                          'other': '第 110 批：Oradea 电子元器件 / 电气 / 自动化直接进口网店（11 人；2024 下滑）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP 一口价 + MOQ 1；罗语引子）**；收件人 office@' + TAG}},
    'SB-469': [{'kp_match': 'procurement@novytel.cz', 'role': '研究档 KP（procurement@）— 公司为中国货源采购代理 / 转口商' + TAG},
               {'facts': {'legal_name': 'Novy Telecom s.r.o.（IČO 28481968）', 'founded': '2008-10-30' + TAG,
                          'other': '第 110 批：布拉格 2 亚洲 / 中国货源采购代理与进出口商（主营农机；2024 出口 ≈US$770k，1,004 票主要发乌克兰）→ **采购代理 → 不动（询价只做预付款、不给渠道价）**' + TAG}}],
    'SB-078': [{'kp_match': 'afcn@sitis.ch', 'role': 'Associé-gérant / 100% 所有人（moneyhouse：200 份 CHF 100，单独签字）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'SITIS Sàrl（UID CHE-150.026.203；CH-660.0.018.012-4）', 'founded': '2012-01-04' + TAG,
                          'other': '第 110 批：日内瓦 Rue Rousseau 15 一人 IT / 电信 / 安防服务商（股本 CHF 20k；打开 5 次）→ **集成 25% small，一页纸一次（STC-028GP / STC-228GP / STI-054GP + MOQ 1 + DAP 瑞士买方清关；法语引子）**' + TAG}}],
    'SB-1005': [{'kp_match': 'jacopo.ganz@', 'role': 'Amministratore Delegato（asit.it 2024-06 任命公告）= 拍板人 / 收件人' + TAG},
                {'kp_match': 'marco.gabriele@', 'role': 'Vice President Sales（techcompany360 / rocketreach）= 收件人（抄）' + TAG},
                {'add_kp': {'name': 'Joris Ganz', 'role': 'Presidente e Amministratore Delegato（asit.it 2024-06）' + TAG, 'email': '', 'source': 'https://www.asit.it/nuove-nomine-asit-s-p-a/'}},
                {'facts': {'legal_name': 'ASIT S.p.A.（P.IVA / CF 06221270017；Registro AEE IT22010000013576）', 'founded': '1992-05-12（活动 1984）' + TAG,
                           'other': '第 110 批：都灵 Mappano 专业 ICT 分销商（布线 / 网络 / 安全 / UCC / AV / CCTV；35+ 品牌；1,500 活跃客户；5 分公司 + 2 代理；42 人；2025 营收 €41.8M；股本 €250k）→ **分销 20%，B BIG，加厚一次（换切口：安装商渠道第二价位 + 意大利 DAP 小起订；STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI-054GP / STI-144GP）；次候选升 A**' + TAG}}],
    'SB-126': {'facts': {'legal_name': 'CABLEWINDOW SL（原名 HAI NUO SRL；商号 CABLE WINDOW；CIF B83027185）', 'founded': '2001-06-15' + TAG,
                         'other': '第 110 批：马德里 Pol. Ind. 网络 / 安防线缆设备进口网店（股本 €3,065；2–6 人；年销 ≈€0.5M；原名提示华人背景）→ **分销 20% small，一页纸一次（英文稿；中文直联 Simon 定，默认否）；再无回声 → 不动**；稿内不点名 Utepo' + TAG}},
    'SB-127': [{'kp_name': 'Igor Guimerá', 'role': 'Administrador único / Gerente（infonif：VIDAL GIMERA IGOR；LinkedIn Igor Vidal Guimerá）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'IZUX INGENIERIA Y SEGURIDAD SL（CIF B98126444；RM Valencia H V-133381）', 'founded': '2009-02-25' + TAG,
                          'other': '第 110 批：瓦伦西亚微型 CCTV / 门禁 / 酒店锁批发网店（1–10 人；销售 ≤€250k）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP 配 Hikvision / Dahua 套件一口价 + MOQ 1；西语引子）；再无回声 → 不动**' + TAG}}],
    'SB-130': [{'kp_match': 'bogdan@', 'role': '业主（推定；1 人公司）= 收件人' + TAG},
               {'facts': {'legal_name': 'BONMAG INTERNATIONAL S.R.L.（品牌 OmniSecurity；CUI 37299107；J15/334/2017）', 'founded': '2017-03-29' + TAG,
                          'other': '第 110 批：Dâmbovița Voinești 一人安防 / 自动化安装商（2025 销售 €100.8k；SICAP 小额公采）→ **集成 25% small，一页纸一次（STC-028GP / STC-228GP 一口价 + MOQ 1 + 预付款；罗语引子）；再无回声 → 不动**' + TAG}}],
    'SB-195': [{'kp_match': 'andrius.d@', 'role': 'Padalinio prekybos vadovas / 分部销售负责人（bkgrupe.lt Kontaktai）= 收件人' + TAG},
               {'add_kp': {'name': 'Andrius Dapkevičius', 'role': 'Vadovas / 总经理（rekvizitai.vz.lt）= 拍板人（抄）' + TAG, 'email': '', 'source': 'https://rekvizitai.vz.lt/en/company/bk_grupe/'}},
               {'add_kp': {'name': 'Justas Kudirka', 'role': 'Elektroninės prekybos vadovas / 电商负责人（bkgrupe.lt）' + TAG, 'email': 'justas@bkgrupe.lt', 'source': 'https://bkgrupe.lt/kontaktai'}},
               {'facts': {'legal_name': 'BK grupė, UAB（Uždaroji akcinė bendrovė Baltijos kontaktų grupė；įmonės kodas 210599550；PVM LT105995515）', 'founded': '1994-03-07' + TAG,
                          'other': '第 110 批：考纳斯 波罗的海三国 + 波兰安防系统分销商（管理中心塔林；95 人；销售收入 €41.9M；股本 €67,320；电商部）→ **分销 20%，B BIG，加厚一次（换切口：四国渠道第二 PoE 货源 + 电商 SKU；STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI-054GP）；次候选升 A**；稿内不点名 Utepo' + TAG}}],
    'SB-230': [{'kp_match': 'fabio@ad-in.net', 'role': 'Vice President（研究档；LinkedIn）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'ADVANCED INNOVATIONS S.R.L.（P.IVA / CF 04994260968；REA MB-1789621）', 'founded': '2005-10-26' + TAG,
                          'other': '第 110 批：Usmate Velate (MB) IP 监控进口分销商（1979 安防制造集团旗下；2016 起 UTEPO 意大利独家、2017 起 Uniview；6 人；2024 营收 €1.13M 自 2021 €2.04M 腰斩、亏损 −€66k）→ **分销 20% small，一页纸一次（1:1 对照其独家品牌在售型号，只给毛利切口：STC-028GP / STC-228GP / STC-2224GP / STI-054GP）；有回声再加厚**；稿内绝不点名 UTEPO / Uniview' + TAG}}],
    'SB-265': [{'kp_match': 'c.sgouros@', 'role': 'Verwaltungsratspräsident / Geschäftsführer（business-monitor.ch）= 拍板人 / 收件人' + TAG},
               {'add_kp': {'name': 'Dominik Mizdrak', 'role': 'Verwaltungsrat（VIDEOR E. Hartig GmbH Geschäftsführer；2026 起控股方）— 仅记录' + TAG, 'email': '', 'source': 'https://business-monitor.ch/en/companies/197640-videotronic-ag'}},
               {'facts': {'legal_name': 'Videotronic AG（UID CHE-107.888.942；CH-020.3.927.830-8）≠ Videotronic (Schweiz) AG CHE-106.761.351', 'founded': '1976-08-03' + TAG,
                          'other': '第 110 批：Regensdorf (ZH) 视频安防 / 门禁分销集成商（股本 CHF 316k；1–10 人；**2026 起德国 VIDEOR E. Hartig GmbH（自有品牌 eneo）多数控股**；6 次无回）→ **分销 20% small，一页纸一次（换切口：并入 Videor 后供应商重审；STC-028GP / STC-228GP / STI-054GP；DAP 瑞士）；再无回声 → 不动**；旁线索 VIDEOR / eneo → DE 池另立户' + TAG}}],
    'SB-266': [{'kp_match': 'milan@', 'role': 'CEO（研究档）— 2026-01-19 起不再是登记代表人；2026-03-10 法院登记 opatrovník → 法人状态异常' + TAG},
               {'facts': {'legal_name': 'Axilogi s.r.o.（IČO 10964703；DIČ CZ10964703；C 123877 KS Plzeň；网站自称 C 47636 → 不一致）', 'founded': '2021-06-23' + TAG,
                          'other': '第 110 批：比尔森 IT / 安防网店（股本 CZK 2M；jednatel = DC Europe system a.s.；代表人 Harmáček 2026-01 注销、2026-03 法院指定监护人 Mgr. Martin Svoboda）→ **法人状态异常 → 不动（B 保留，不进发送包；主动询盘只做全额预付）**' + TAG}}],
    'SB-269': [{'kp_match': 'adamian@', 'role': 'General Manager（研究档）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Tiziano Cerato', 'role': 'Sales Engineer（研究档）= 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'Contradata Milano S.r.l.（P.IVA / CF 04099800155；REA MI-987346）', 'founded': '1978' + TAG,
                          'other': '第 110 批：Monza 工业 PC / 嵌入式 / 工业以太网分销商（股本 €78k；10–15 人；2024 营收 €3.69M −22.5%）→ **分销 20% small，一页纸一次（换切口：STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM 作台系第二价位 + 交期）；有回声再加厚**' + TAG}}],
    # ---------- 第 2/3 ----------
    'SB-272': {'facts': {'legal_name': 'ELECTRONIK HOUSE S.r.l.s.（P.IVA / CF 03568370369；REA MO-399124）', 'founded': '2014-05-02' + TAG,
                         'other': '第 110 批：摩德纳电子小店（股本 €900；3 人；2024 营收 €216.5k；仅 info@）→ **按「一人网店」规则 不动**' + TAG}},
    'SB-277': [{'kp_match': 'ejprieto@', 'role': 'CEO（研究档）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'comercial@instantbyte.com', 'role': 'Comercial（研究档 Eduardo Valle）= 收件人（抄）' + TAG},
               {'facts': {'legal_name': 'INSTANT BYTE SL（CIF B83680082；RM Madrid）', 'founded': '2003-07-15' + TAG,
                          'other': '第 110 批：Leganés (Madrid) 无线 / VoIP / CCTV / GPON 增值批发商（36 人；自述年营业额 >€20–22M；1.2 万 SKU）→ **分销 20%，B BIG，加厚一次（换切口：MikroTik / TP-Link 价位带之间的第二 PoE 货源 + 伊比利亚 DAP；STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI-054GP）；次候选升 A**' + TAG}}],
    'SB-287': [{'kp_match': 'mauro.brunazzo@', 'role': 'CEO（研究档）= 拍板人 / 收件人' + TAG},
               {'add_kp': {'name': 'Marcello Gariboldi', 'role': 'Responsabile Commerciale Milano（sea-srl.it Sedi）= 收件人（抄）' + TAG, 'email': 'milano@sea-srl.it', 'source': 'https://www.sea-srl.it/contatti/sedi'}},
               {'facts': {'legal_name': 'S. & A. S.R.L.（商号 S&A；P.IVA / CF 01887850129；REA VA-214291；股本 €100,000）', 'founded': '—（未取）' + TAG,
                          'other': '第 110 批：Gallarate (VA) 安防电子批发分销商（Legnano / Milano / Bologna / Asti 5 网点；TVT / Ajax / Bentel / Bosch / Hochiki）→ **分销 20%，B BIG，加厚一次（换切口：安装商柜台配套 PoE SKU：STC-028GP / STC-228GP / STC-2224GP + 意大利 DAP 小起订）**；营收未取' + TAG}}],
    'SB-289': [{'kp_match': 'c.beriachetto@', 'role': '研究档 KP = 收件人（工业线）' + TAG},
               {'facts': {'legal_name': 'SISTEMI AVANZATI ELETTRONICI S.R.L.（商号 SisAv；P.IVA / CF 01925460022；REA BI-174039）', 'founded': '1998' + TAG,
                          'other': '第 110 批：Cossato (BI) 工业 / 国防 / 医疗电子硬件分销 + 集成（11–50 人；2024 营收 €4.33M）→ **守界：只做工业自动化线 → 分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM 作数据采集现场网络第二价位）；绝不提国防 / 医疗**' + TAG}}],
    'SB-290': [{'kp_match': 'd.prieth@', 'role': 'Titolare / Inhaber（impresa individuale；CF PRTDNK95S07I729O）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'SOLPAKUTEC INDUSTRY DP（Dominik Prieth 个体户；P.IVA 03085880213；REA BZ-230913）', 'founded': '—（≈2019；未取）' + TAG,
                          'other': '第 110 批：南蒂罗尔 Schlanders 一人工业 PC / 工业通信分销（打开 4 次）→ **分销 20% small，一页纸一次（德语引子；STI-054GP / STI-144GP / STI-154GP 作台系第二价位 + MOQ 1 + 预付款）；再无回声 → 不动**；稿内不点名 ICP DAS' + TAG}}],
    'SB-292': [{'kp_match': 'bart@teslanetworks.com', 'role': 'CEO（LinkedIn）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'info@teslanetworks.be', 'role': '研究档 KP Ashwin Taeye（info@）' + TAG},
               {'add_kp': {'name': 'Joris Laeremans', 'role': 'Sales & Marketing Manager（LinkedIn）' + TAG, 'email': '', 'source': 'https://be.linkedin.com/company/tesla-networks'}},
               {'facts': {'legal_name': 'Tesla Networks BV（原 BVBA；BE 0830.294.165；RPR Antwerpen afd. Mechelen）', 'founded': '2010-10-06（业务 1999）' + TAG,
                          'other': '第 110 批：Heist-op-den-Berg 无线 + 工业网络集成 / 咨询商（1–5 人；公交 / 有轨电车车载 ITxPT / 5G 项目为主 = 台系品牌渠道）→ **守界：绝不提轨交 / 车载；只做能源 / 工业 / 智慧城市固定场景 → 集成 25% small，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM + MOQ 1；荷语引子）；再无回声 → 不动**；稿内不点名 ORing' + TAG}}],
    'SB-297': {'facts': {'legal_name': '（未坐实）Gorgos Cristian — Gmail 个人联系人，1 次检索查无摩尔多瓦法人', 'founded': '—' + TAG,
                         'other': '第 110 批：同姓 Gorgos Dorin / Gorgos Simion 的无关 SRL ≠ 目标 → **不动（不进发送包；主动询盘全额预付）**' + TAG}},
    'SB-417': {'facts': {'legal_name': 'ALIDEX NETWORKS S.R.L.（商号 ALIDEX Italia / Alidex Iberia；P.IVA / CF 10924650962；研究档「ALIDEX S.r.l.」更正）', 'founded': '≈2019（「6 anni」）' + TAG,
                         'other': '第 110 批：Codogno (LO) 南欧工业网络分销商（ORing 等；近 8,000 货号；**1 名雇员、股本 €2,000、营收 €388k**；意 + 西两地 = alidex.es → SB-832 并线于此）→ **分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM 第二价位 + MOQ 1）**；稿内不点名 ORing；收件人 info@alidex.it' + TAG}},
    'SB-434': [{'kp_match': 'nicolas@s-connect.es', 'role': 'Inside Sales / Industrial IoT Solutions Specialist（LinkedIn / blog）= 收件人' + TAG},
               {'add_kp': {'name': 'Pablo Kessler de la Maza', 'role': 'Sales and Technical Support Industrial IoT Solutions（LinkedIn）' + TAG, 'email': '', 'source': 'https://www.linkedin.com/company/s-connect-s.l./'}},
               {'facts': {'legal_name': 'S CONNECT S.L.（S-Connect；S.L.U.；CIF B64872484；RM Barcelona；SPHINX Computer Vertriebs GmbH 全资子公司）', 'founded': '2008-05-07（办事处 2003）' + TAG,
                          'other': '第 110 批：巴塞罗那 + 马德里 工业通信 / 工业 IoT 增值分销（德国 SPHINX 集团 7 国；Moxa 等；2–10 人；本地库存）→ **分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM 第二价位 + 短交期；西语引子）；有回声再加厚**；旁线索 SPHINX Computer Vertriebs GmbH（法兰克福）→ DE 池另立户；稿内不点名 Moxa' + TAG}}],
    'SB-436': [{'kp_match': 'peter@steplockaccess.se', 'role': '研究档 KP（姓未取）= 收件人' + TAG},
               {'add_kp': {'name': 'Fredrik Skoog', 'role': 'VD（extern；allabolag / hitta：Carl Fredrik Valter Skoog）= 拍板人（抄）' + TAG, 'email': '', 'source': 'https://www.allabolag.se/foretag/steplock-access-ab/falun/elektronik-och-telekommunikationsutrustning/2KGRTI0I63IFR'}},
               {'facts': {'legal_name': 'Steplock access AB（org.nr 559105-9992；VAT SE559105999201；Steab Förvaltning AB 集团）', 'founded': '2017-03-23' + TAG,
                          'other': '第 110 批：Falun 门禁 / 通行系统自有品牌商（5 人；FY2025-06 营业额 SEK 18.2M ≈ €1.6M，+469% 自 2021；EBIT −SEK 7.2M 投入期；集团 6 公司 84 人 SEK 448M）→ **贴标 / 配套 30% small，一页纸一次（STC-028GP / STI-054GP / STI-144GP 作门禁控制器 PoE 配套，可贴 StepLock 标）；有回声再加厚**；瑞典语引子' + TAG}}],
    'SB-437': [{'kp_match': 'pietro.milani@', 'role': 'Fondatore / CEO（affaritaliani 2025-11；rocketreach）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'info@tpole.it', 'role': '研究档 KP Lorenzo Bruno（info@）' + TAG},
               {'facts': {'legal_name': 'TPOLE S.R.L.（现行 P.IVA / CF 02978370183，REA PV-330560，2025-01-10 登记，股本 €50,000；前身同名 P.IVA 02545250967 / REA 218088，2005-05-02）', 'founded': '2025-01-10（前身 2005-05-02；业务 1995）' + TAG,
                          'other': '第 110 批：Portalbera (PV) 工业 / 嵌入式 PC 增值分销商（15 人；2025 营收 €8.76M、净利 €665k；前身 2022 €9.47M；工业交换机台系）→ **分销 20%，B BIG，加厚一次（换切口：STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM 第二价位 + 3 年保；只提自动机械 / 工业，不提轨交 / 医疗）；次候选升 A**；稿内不点名 Volktek' + TAG}}],
    'SB-439': [{'kp_name': 'Jeannie Rozowykwiat (Levy)', 'role': '原 Présidente（2024-10 → 2025-12；pappers：2025-12-04 起 Président 为 Jean-Edmond）；收件人 commercial@exxell.fr' + TAG},
               {'kp_name': 'Jean-Edmond Rozowykwiat', 'role': 'Président（2025-12-04 起；pappers / societe.com）= 拍板人' + TAG},
               {'facts': {'legal_name': 'E.V. EXXELL VISION SAS（商号 EXXELL VISION；SIREN 493 179 089；RCS Nanterre；TVA FR62493179089；原 SARL，SAS 公告 2025-01-06）', 'founded': '2006-11-20（登记 2008-10-08）' + TAG,
                          'other': '第 110 批：Boulogne-Billancourt 安防设备进口 / 分销 / 安装外包商（资本 €15k；6–9 人；最后公开营收 €727k 2011）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP 配监控套件 + MOQ 1；法语引子）；再无回声 → 不动**' + TAG}}],
    'SB-444': [{'kp_match': 'michal.chvala@', 'role': '研究档 KP = 收件人' + TAG},
               {'kp_name': 'Stanislav Lupták', 'role': 'Konateľ / 所有人（foaf.sk / orsr.sk；Ing.）= 拍板人（抄）' + TAG},
               {'add_kp': {'name': 'Boris Lupták', 'role': 'Konateľ / 所有人（foaf.sk；Mgr.）' + TAG, 'email': '', 'source': 'https://foaf.sk/firmy/436789'}},
               {'facts': {'legal_name': 'Tritonsystems spol. s r.o.（IČO 48060658；DIČ 2120052044；IČ DPH SK2120052044；OR OS Bratislava I Sro 102834/B；关联老公司 T R I T O N spol. s r.o. IČO 31323642 同址）', 'founded': '2015-03-10（集团 1992）' + TAG,
                          'other': '第 110 批：布拉迪斯拉发 停车 / 票务 / 门禁系统制造商 + 运营商（自有品牌 ParkIS / Arena；「斯洛伐克最大停车系统制造商之一」；Lupták 家族）→ **贴标 / 配套 30% small，一页纸一次（换切口：STI-054GP / STI-144GP / STI-154GP 作停车终端 + 车牌相机户外机柜 PoE 配套，可贴 ParkIS 标 + 3 年保）；有回声再加厚**；斯洛伐克语引子' + TAG}}],
    # ---------- 第 3/3 ----------
    'SB-573': [{'kp_match': 'lola.lucena@', 'role': '研究档 KP = 收件人（工业线）' + TAG},
               {'facts': {'legal_name': 'INTEGRA NETWORK AND EMBEDDED SYSTEMS SL（S.L.U.；商号 Integra Network；CIF B84961267；RM Madrid hoja 425407）', 'founded': '2007-01-22' + TAG,
                          'other': '第 110 批：Rivas-Vaciamadrid 工业计算 / 嵌入式 / 工业网络方案商（工业 / 轨交 / 交通 / 电信 / AV / 国防）→ **守界：只做工业 / 能源 / 交通固定机柜线 → 分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM 第二价位；西语引子）**；不提 IEC 61850 / EN 50155；稿内不点名 Lantech' + TAG}}],
    'SB-576': [{'kp_match': 'info@matrix.es', 'role': '研究档 KP Daniel Cortes（info@）= 收件人' + TAG},
               {'facts': {'legal_name': 'MATRIX ELECTRONICA SL（S.L.U.；CIF B79611794；RM Madrid；Administrador único / 所有人 FLEXITRON SL = Flexitron Group；自有 IoT 品牌 Webdyn）', 'founded': '1990-10-18（活动 1991）' + TAG,
                          'other': '第 110 批：马德里 工业电子 / IoT 元器件与模块分销商（60 人；销售额 €6–30M 区间；Madrid / Barcelona / Durango / Valencia / Sevilla + Lisboa / 法国 / 印度 办事处）→ **分销 20%，B BIG，加厚一次（换切口：面向其集成商 / 制造商客户的工业 PoE 配套 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM + Webdyn 网关项目；西语引子）；次候选升 A**' + TAG}}],
    'SB-593': [{'kp_match': 'jordi@iptecno.com', 'role': 'Administrador（BORME-C-2021-3504：Jordi Bassa Jansana）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Joan Balaguer', 'role': '研究档 KP（职务未取）' + TAG},
               {'add_kp': {'name': 'Joan Ojeda Flores', 'role': 'Administrador solidario（BORME 2021）' + TAG, 'email': '', 'source': 'https://www.boe.es/diario_borme/txt.php?id=BORME-C-2021-3504'}},
               {'facts': {'legal_name': 'SMART TECH IBD GLOBAL SOLUTIONS S.L.U.（原名 IPTECNO VIDEOVIGILANCIA SL；商号 IBD Global / IPTecno；CIF B63904445；RM Barcelona）', 'founded': '—（2020-04 BC Diid + IPTecno 合并；2021-05 吸收合并）' + TAG,
                          'other': '第 110 批：Montornès del Vallès 伊比利亚安防分销集团（100+ 人；西 / 葡多地物流基地；IndigoVision / IntelexVision）→ **分销 20%，B BIG，加厚一次（换切口：项目型安防分销的工程配套 PoE：STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI-054GP；西 / 葡两国 DAP）；回信即 A 候选**；稿内不点名 IndigoVision' + TAG}}],
    'SB-601': [{'kp_match': 'rjorge@visus.pt', 'role': '研究档 KP = 收件人' + TAG},
               {'facts': {'legal_name': 'OPTIVISUS, LDA（商号 Visus；原名 CENTRO DE OPTOMETRIA OPTIVISUS, LDA；NIPC 502 752 980）', 'founded': '1991-01（业务 1989）' + TAG,
                          'other': '第 110 批：里斯本 CCTV-IP / 网络 / 电信设备进口分销商（只走经销伙伴网络；Vivotek / DrayTek）→ **分销 20% small，一页纸一次（换切口：STC-028GP / STC-228GP / STC-2224GP 配 IP 摄像机套件 + 葡语引子 + 葡萄牙 DAP）；有回声再加厚**；稿内不点名 Vivotek / DrayTek' + TAG}}],
    'SB-644': [{'kp_match': 'thomas.thoma@', 'role': 'Director / Managing Director（cyprusregistry：ΘΩΜΑΣ ΘΩΜΑ；rocketreach）= 拍板人 / 收件人' + TAG},
               {'add_kp': {'name': 'Janet Bergeman Thomas', 'role': 'Director / Secretary（cyprusregistry）' + TAG, 'email': '', 'source': 'https://cyprusregistry.com/companies/HE/147954'}},
               {'facts': {'legal_name': 'A.K. ART 2 SOFT LIMITED（商号 ART2SOFT / cy-wireless.com；HE 147954）', 'founded': '2004-04-30（业务 2006）' + TAG,
                          'other': '第 110 批：尼科西亚 Lakatameia 网络 / 无线 / VoIP 分销商（Ubiquiti / MikroTik / Ruijie / TP-Link Business / Yeastar 官方分销；500+ 经销商；登记状态 Reminder letter sent，年报 2020 后待补）→ **分销 20% small，一页纸一次（换切口：MikroTik / TP-Link 价位带之间的第二 PoE 货源 STC-028GP / STC-228GP / STC-2224GP + 塞浦路斯 DAP）；有回声再加厚**；希腊语引子' + TAG}}],
    'SB-832': {'facts': {'legal_name': 'Alidex Iberia（alidex.es）= SB-417 ALIDEX NETWORKS S.R.L.（P.IVA 10924650962）的西班牙站；无独立西班牙法人（研究档 garmasl.com = Garma Electrónica, S.L. B20178372 无关）', 'founded': '—（见 SB-417）' + TAG,
                         'other': '第 110 批：**并线 SB-417，不另发**' + TAG}},
    'SB-950': [{'kp_match': 'giorgi@line-net.ge', 'role': '研究档 KP；WhatsApp 20 次未回' + TAG},
               {'facts': {'legal_name': 'Linenet LLC（შპს；识别码 / VAT 404486757；NAPR）', 'founded': '2015-02-05' + TAG,
                          'other': '第 110 批：第比利斯 网络 / 安防 / 消防系统设计与安装商（bia.ge）→ **已触达、20 次 0 回复 → 不动（B 保留；主动询盘预付款）**' + TAG}}],
    'SB-259': [{'add_kp': {'name': 'Sébastien Dourte', 'role': '创办人 / Gérant（LinkedIn Dourte；companyweb 10.2 FTE）= 拍板人（收件人 info@dourte.be 待核）' + TAG, 'email': '', 'source': 'https://www.companyweb.be/en/0684917295/dourte'}},
               {'facts': {'legal_name': 'Dourte SRL / BV（商号 Dourte Elektriciteit；BE 0684.917.295）', 'founded': '2017-11-16（业务 2010）' + TAG,
                          'other': '第 110 批：Ruisbroek (Sint-Pieters-Leeuw) 电气 + 安防安装商（10.2 FTE 2025；毛利 €598k；净利 €8.5k）→ **集成 25% small，一页纸一次（STC-028GP / STC-228GP / STI-054GP 配 CCTV / 门禁 + MOQ 1；法 / 荷引子）；再无回声 → 不动**' + TAG}}],
    'SB-481': {'facts': {'legal_name': 'Itegra, MB（mažoji bendrija；Partizanų g. 21B-11, LT-49478 Kaunas；įmonės kodas 未取）', 'founded': '—（未取）' + TAG,
                         'other': '第 110 批：考纳斯微型电气 / 安防 / 监控安装合伙（rekvizitai 目录条目；无 KP；研究档国别「意大利」有误，entities iso LT 正确，不改）→ **不动**' + TAG}},
    'SB-491': {'facts': {'legal_name': 'Rass-security systems（raskpreke.lt 网店；įmonės kodas 305706724；PVM LT100013849613；法人形式未取）', 'founded': '≈2021（代码段推定）' + TAG,
                         'other': '第 110 批：维尔纽斯 Panerių g. 64 微型安防网店（无 KP；研究档国别「意大利」有误，entities iso LT 正确，不改）→ **按「一人网店」规则 不动**' + TAG}},
    'SB-021': [{'kp_match': 'eric-piaget@', 'role': '外部顾问 / 欧洲销售（LinkedIn：CEO EPA-Technologies SAS，Consultant chez Loop Telecom；法国 Vaucresson）— 公司为台湾上市同行制造商' + TAG},
               {'facts': {'legal_name': '星通資訊股份有限公司 Loop Telecommunication International, Inc.（統一編號 22099863；TWSE 3025；新竹科学园区新安路 8 号）', 'founded': '1991-12-03' + TAG,
                          'other': '第 110 批：台湾上市电信 / 工业以太网设备制造商（董事长兼总经理葉茂林；实收资本 NT$567M；表内 FR 仅为其欧洲顾问所在地，不 country_fix）→ **同行 → 不动（不进任何发送包）**' + TAG}}],
    'SB-155': [{'kp_match': 'jyguibreteau@gmail.com', 'role': '研究档推断 J.-Y. Guibreteau（Gmail）；可能 = Jean-Yves Guibreteau，CG SYSTEMES SAS（SIREN 939 650 495）DG 2025-02 起 — 待证' + TAG},
               {'facts': {'legal_name': '（未坐实）JguyTech — 1 次检索查无法人；可能线索 CG SYSTEMES SAS 939 650 495 待证', 'founded': '—' + TAG,
                          'other': '第 110 批：Gmail 个人、曾买 1 件样品（OM4301）；研究档出现 faiveleytransport.com（轨交供应商）域名 → 若属实为轨交背景（守界）→ **不动（B 保留；再询盘走零售价 / 预付款）**' + TAG}}],
    'SB-075': [{'kp_match': 'info@gmka.gr', 'role': '合伙人（Karydis 家族 Ο.Ε.）' + TAG},
               {'facts': {'legal_name': 'ΓΕΜΚΑ – Καρύδη Αφοί Ο.Ε.（GEMKA – Karydis Bros O.E.；Ομόρρυθμη Εταιρεία；ΑΦΜ 094019245 / ΓΕΜΗ 001037501000 据 11888.gr 但地址不符 → 待证）', 'founded': '1928（Ο.Ε. 登记日期未取）' + TAG,
                          'other': '第 110 批：Αιγάλεω 百年钥匙 / 锁具 / 电子锁 / 保险柜进口批发商（2–10 人；门禁仅副线）→ **非目标行业 → 不动**' + TAG}}],
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
