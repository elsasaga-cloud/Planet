# -*- coding: utf-8 -*-
"""第 107 批（T29-U100，2026-10-28）欧洲其他国家 B 池第 1 轮 · 第 1/3（8 户）—— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 107
F = '2026-10-28'

put('SB-073', key='other', batch=B, name='A.N.B. RIMEX SA（AnB-Rimex；anb-rimex.be；比利时列日 Herstal Parc Industriel des Hauts-Sarts；BCE 0424.592.259）— 1983-07-26 成立的安防 / 楼宇自动化设备制造商 + 分销商（NACE 2630 通信设备制造 + 4652 电子 / 电信设备批发；自有 TriCom 报警主机、TriCare AI；分销 CCTV / 门禁 / 火灾探测；2018 首家 INCERT 认证 CCTV）；股本 €75,000；12.7 FTE；董事兼日常管理 Philippe Stas（2022 起）+ Aida Consult（常任代表）；研究档 KP Ibrahim Tiryaki（it@）；群发 8 次打开', iso='BE', fetched=F,
    source='BE · 1 次检索：companyweb（BE 0424.592.259；Rue de l’Abbaye 89 4040 Herstal；Established 26-07-1983；12.7 FTE；SA）+ b2bhint（Capital 75.000 EUR；NACE 2630 / 4652 / 4669；Dirigeants Stas Philippe Administrateur + Personne chargée de la gestion journalière depuis 2022；Aida Consult Administrateur / Représentant permanent）+ pappers.be（NV；BTW BE0424592259；75 000 €）+ INCERT 证书页（ANB Rimex；BE0424592259；info@anb-rimex.be；04 229 37 97）+ LinkedIn（12 员工）',
    url='https://www.companyweb.be/en/0424592259/a-n-b-rimex',
    number='BCE / TVA BE 0424.592.259（établissement 2.023.133.651）', status='Active（situation normale）', incorporated='1983-07-26', company_type='SA / NV（私有；股本 €75,000）',
    sic=['安防 / 楼宇自动化设备制造（报警主机）+ 安防设备批发（CCTV / 门禁 / 火灾探测）'],
    address='Rue de l’Abbaye 89, 4040 Herstal（Liège）', accounts='2025 年报已交', accounts_due='—', size_band='小型（12.7 FTE）',
    officers=['Philippe Stas — Administrateur + 日常管理负责人（2022 起）= 拍板人', 'Aida Consult（常任代表）— Administrateur', 'Ibrahim Tiryaki — 研究档 KP（it@anb-rimex.be）= 收件人'], psc='未取', charges='', prev_names=[],
    lines=['**自产报警主机 + 分销 CCTV 的比利时小厂 → 贴标 OEM 30% 可谈（AnB 标 PoE 交换机进其 CCTV 套装）+ 分销 20%，B，加厚一次（small）**：STC-028GP / STC-228GP / STC-2224GP 一页纸 + 1:1 对照',
           '收件人 it@ 直呼 Ibrahim，抄 info@ 点名 Philippe Stas；8 次打开无回复 → 二次触达换切口；发信窗口 Thu 12–14 CET；法语一句引子 + 英文正文'],
    notes='贴标 30% 可谈 + 分销 20%；B；加厚一次（small）；坐实（BCE）。')
put('SB-1033', key='other', batch=B, name='Garma Electrónica S.L.（garmasl.com；西班牙圣塞巴斯蒂安 Calle Oyarzun 1 Bajo, 20013 Donostia）— 20+ 年工业仪表与过程控制分销商（Red Lion / N-Tron 工业交换机 NT5000、FEMA 面板表、Scaime 称重、Helmholz 网络、Finetek 液位）；CIF 未取 → 部分坐实；表内「Red Lion Switch、I/O module」；无跟进；群发 8 次打开', iso='ES', fetched=F,
    source='ES · 1 次检索：官网 Home / Contact（Garma Electrónica S.L.；Calle Oyarzun 1 Bajo 20013 Donostia-San Sebastián；info@garmasl.com；943 29 11 02；With over 20 years；Download Red Lion Ntron Networking / N-Tron Series NT5000 / Red Lion FlexEdge / Scaime / Helmholz）+ FEMA 分销页 + Finetek 项目页（Zamakona 船厂）；CIF / Registro Mercantil 未取',
    url='https://www.garmasl.com/en/',
    number='CIF 未取（S.L.）', status='Active', incorporated='未取（自述 20+ 年）', company_type='S.L.（私有；小型）',
    sic=['工业仪表 / 过程控制 / 工业网络分销（Red Lion / N-Tron 代理）'],
    address='Calle Oyarzun 1 Bajo, 20013 Donostia-San Sebastián（Gipuzkoa）', accounts='—', accounts_due='—', size_band='小微（推定 <10 人）',
    officers=['（未具名）— 收件人 info@garmasl.com（点名 compras / responsable de redes industriales）'], psc='未取', charges='', prev_names=[],
    lines=['**卖 N-Tron（高价美系工业交换机）的仪表分销商 → STI 工业线是「第二价位」：分销 20% small，一页纸（STI-054GP / STI-144GP / STI-288DGGPM 1:1 对照 NT5000 价位）一次；有回声再加厚**；稿内不点名 Red Lion / N-Tron',
           '8 次打开无回复 → 二次触达换切口；发信窗口 Thu 12–14 CET；西语一句引子'],
    notes='分销 20% small；一页纸；部分坐实。')
put('SB-101', key='other', batch=B, name='АВИКАМ ЕООД / Avicam Ltd.（avicam-bg.com；索菲亚 ул. Братя Миладинови 60 门店，注册地 №57 ет.5 ап.16；ЕИК 175335234；ДДС BG175335234 2007-09-12）— 品牌 2001 起、法人 2007 年登记的视频监控 / 安防设备进口分销 + 设计安装商（RaySharp 保加利亚官方代表；自有 AVICAM 品牌线缆配件；Viber 销售）；管理者 Георги Атанасов Колев（与 Атанас Георгиев Колев 各 50%，父子推定）；2 名员工（2021）、营业额 €160k（2020）→ 小微；群发 8 次打开', iso='BG', fetched=F,
    source='BG · 1 次检索：papagal.bg（Авикам ЕООД；ЕИК 175335234；Активен；ДДС BG175335234 от 12.09.2007；Дата на регистрация 2007；Седалище София р-н Възраждане, Братя Миладинови 57, ет. 5, ап. 16；Управител Георги Атанасов Колев；Съдружници Атанас Георгиев Колев 50% / Георги Атанасов Колев 50%；Оборот 160 546 € 2020；2 служители 2021）+ 官网（АВИКАМ ООД … над 15 годишен опит；Братя Миладинови 60；sales@avicam-bg.com；+359 2 8327084）+ 品牌页（AVICAM е бранд на АВИКАМ ООД, основана през 2001）+ econ.bg / jobs.bg（ЕИК 175335234）',
    url='https://papagal.bg/eik/175335234/8e85',
    number='ЕИК 175335234；ДДС BG175335234', status='Активен', incorporated='2007（法人）；品牌 2001', company_type='ЕООД / ООД（家族；注册资本 ≈€2,556）',
    sic=['视频监控 / 安防设备进口分销 + 设计安装（自有 AVICAM 配件品牌）'],
    address='ул. Братя Миладинови 60, 1202 София（注册地 №57, ет. 5, ап. 16）', accounts='2020 营业额 €160,546', accounts_due='—', size_band='小微（2 人）',
    officers=['Георги Атанасов Колев（Georgi Kolev）— Управител / 50% 股东 = 拍板人 / 收件人（sales@）', 'Атанас Георгиев Колев — 50% 股东'], psc='Колев 家族', charges='', prev_names=[],
    lines=['**2 人家族安防分销（自有 AVICAM 配件标）→ 分销 20% small；一页纸（STC-028GP / STC-228GP 配其 RaySharp 套装）一次；小批量贴标可一句带过**',
           '收件人 sales@ 点名 Georgi Kolev；8 次打开无回复 → 二次触达换切口；发信窗口 Thu 12–14 EET'],
    notes='分销 20% small；一页纸；坐实（ЕИК）。')
put('SB-1000', key='it', batch=B, name='Alpha Elettronica S.r.l.（alphaelettronica.com；帕尔马 Collecchio Strada Antolini 2/A；P.IVA 01511860346；REA PR-159233）— 1975 年由 Mauro Salsi 创立的电源 / 变压器设计制造商 + 电子电气配件分销商（自有 Alpha Elettronica 品牌；品类含 networking / switch、工业适配器、安防网络交换机；2015 新总部）；股本 €46,500；11–50 人（≈21）；表内「商业 PoE 为主，质量一般」；无跟进；群发 8 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：官网页脚（Alpha Elettronica S.r.l.；Strada Antolini 2/A 43044 Collecchio (PR)；P.IVA/CF IT01511860346；R.E.A. PR-159233；Reg.Impr PR-15711）+ 条款页（Registro Imprese di Parma REA 159233；P.IVA 01511860346）+ visurissima（ATECO 279009 其他电气设备制造；Capitale € 46.500 i.v.；SDI KRRH6B9）+ Storia（1975 创始人 Mauro Salsi；2015 新总部）+ LinkedIn（11–50；1975）+ Contatti（commerciale@ / ordini@ / info@；0521 804427）',
    url='https://www.alphaelettronica.com/en/',
    number='P.IVA / CF 01511860346；REA PR-159233', status='Active', incorporated='1975', company_type='S.r.l.（家族私有；股本 €46,500）',
    sic=['电源 / 变压器制造（ATECO 27.90）+ 电子电气配件分销（自有品牌；含网络 / PoE 交换机品类）'],
    address='Strada Antolini 2/A, 43044 Collecchio (PR)', accounts='—', accounts_due='—', size_band='小型（≈21 人）',
    officers=['Mauro Salsi — 创始人（1975）= 拍板层', '（未具名）— 收件人 commerciale@alphaelettronica.com（点名 ufficio acquisti）'], psc='Salsi 家族（推定）', charges='', prev_names=[],
    lines=['**自有品牌电源厂 + 配件分销（已卖商用 PoE）→ 贴标 OEM 30% 可谈（Alpha 标 PoE 交换机，与其电源线同渠道）+ 分销 20%，B BIG，加厚一次**：STC-028GP / STC-228GP / STC-2224GP + 工业 STI 线一页纸',
           '收件人 commerciale@ 点名 ufficio acquisti；8 次打开无回复 → 二次触达换切口「PoE switch under your own label, same channel as your adapters」；发信窗口 Thu 12–14 CET；意语一句引子'],
    notes='贴标 30% 可谈 + 分销 20%；B BIG；加厚一次；坐实（P.IVA + REA）。')
put('SB-1066', key='lt', batch=B, name='UAB „Elseta“（原 UAB „PRAMONINIS RYŠYS“ 2013–2018；elseta.com；pramoninisrysys.lt 为其工业通信网店；维尔纽斯 L. Zamenhofo g. 5；įmonės kodas 300564737；PVM LT100003358919）— 2006-05-02 登记、Aedilis 研发部拆分而来的工业 / 变电站自动化制造商（Mini RTU、数据集中器、WCCLite、The-Vinci 云；面向配电网 / 新能源 / 产线）；股本 €173,760；≈22 人；负责人 Matas Doviltis；表内「Beijer 工业 FS，质量一般」；群发 8 次打开', iso='LT', fetched=F,
    source='LT · 1 次检索：rekvizitai.vz.lt（Elseta, UAB；code 300564737；founded 2006-05-02；VAT LT100003358919；Share capital 173 760 €；Manager Matas Doviltis；L. Zamenhofo g. 5 LT-06332 Vilnius；4 shareholders；2018-03-16 更名自 UAB PRAMONINIS RYŠYS；2013-01-18 由 UAB ELSETA 改为 PRAMONINIS RYŠYS）+ info.lt（22 darbuotojai；www.pramoninisrysys.lt）+ elseta.com Contacts（Company Code 300564737）+ 公司自述（First established as Aedilis R&D department in 2011, separate company 2017；RTU for secondary substations）',
    url='https://rekvizitai.vz.lt/en/company/elseta/',
    number='įmonės kodas 300564737；PVM LT100003358919', status='Active', incorporated='2006-05-02', company_type='UAB（4 名股东；股本 €173,760）',
    sic=['工业 / 变电站自动化设备制造（RTU、数据集中器）+ 工业通信设备网店（pramoninisrysys.lt）'],
    address='Liudviko Zamenhofo g. 5, LT-06332 Vilnius', accounts='—', accounts_due='—', size_band='小型（≈22 人）',
    officers=['Matas Doviltis — 负责人（vadovas）= 拍板人', '（未具名）— 收件人 info@elseta.com / 网店邮箱（点名 pirkimai / 采购）'], psc='4 名股东（未取）', charges='', prev_names=['UAB „PRAMONINIS RYŠYS“（2013–2018）', 'UAB „ELSETA“（2006–2013）'],
    lines=['**自产 RTU 的工业自动化厂 + 工业通信网店 → 采购型 25%（RTU 柜内 / 变电站二次侧配工业交换机）+ 网店分销 20%，B，加厚一次（small）**：STI-054GP / STI-144GP / STI-288DGGPM / STI-0240GE 一页纸；**守界：不提 IEC 61850 认证，只讲宽温 / 导轨 / 冗余供电**',
           '收件人 info@ 点名 Matas Doviltis；8 次打开无回复 → 二次触达换切口「DIN-rail switches sized for RTU cabinets」；发信窗口 Thu 12–14 EET'],
    notes='采购型 25% + 分销 20%；B；加厚一次（small）；坐实（įmonės kodas）。')
put('SB-358', key='fr', batch=B, name='KYOLIS SAS（kyolis.com；总部 2 rue de la Renaissance 92160 Antony，研发 / 工厂 / 售后 1 rue de la Banque 73000 Chambéry（2023 起投产）；SIREN 519 722 698 RCS Nanterre；TVA FR00519722698）— 2010-01 由 Stéphane Manuse 与 Thomas Eleaume 创立的法国光纤 / 同轴以太网传输设备与工业交换机品牌商（自有 logo；「法国制造」）；股本 €100,000；6–9 人（2022）；Président Thomas Eleaume（2011 起）、DG Stéphane Manuse（2024-06 起）；pappers 标注 1 项登记程序（性质未查）；群发 6 次打开', iso='FR', fetched=F,
    source='FR · 1 次检索：societe.com（KYOLIS；SIREN 519 722 698；SIRET 519 722 698 00023；TVA FR00519722698；création 22/01/2010；NAF 4669B；SAS；2 rue de la Renaissance 92160 Antony；Président Thomas ELEAUME depuis 2011-08-06；DG Stéphane MANUSE depuis 2024-06-28）+ pappers（Effectif 6–9 salariés 2022；Capital 100 000；1 procédure enregistrée）+ infonet（RCS Nanterre；Active）+ 官网 Notre histoire（Créée en 2010 … fabrication française；atelier Chambéry fin 2022，production 2023；siège Antony）+ lefigaro 公告（capital 100.000 €；AG 2024-05-16 任命 DG）',
    url='https://www.societe.com/societe/kyolis-519722698.html',
    number='SIREN 519 722 698（RCS Nanterre）；TVA FR00519722698', status='Active', incorporated='2010-01-22（RCS）', company_type='SAS（私有；股本 €100,000）',
    sic=['光纤 / 同轴以太网传输设备、工业交换机 品牌商（自有 logo；部分法国组装）'],
    address='2 rue de la Renaissance, 92160 Antony（工厂 1 rue de la Banque, 73000 Chambéry）', accounts='—', accounts_due='—', size_band='小微（6–9 人）',
    officers=['Thomas Eleaume — Président（2011 起）= 拍板人（研究档 KP）', 'Stéphane Manuse — Directeur général / 技术（2024-06 起）= 收件人（stephane.manuse@）'], psc='Eleaume / Manuse（创始人）', charges='pappers：1 项登记程序（性质未查）', prev_names=[],
    lines=['**自有 logo 的法国小品牌商（工业 MC / FS / SFP / EoC）→ 贴标 OEM 30% 目标（Kyolis 标导轨工业 PoE / 光口机，补其自产线以外的 SKU）+ 分销 20%，B BIG，加厚一次；升 A 次候选**：STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM 一页纸 + 1:1 规格对照；稿内不说「made in France 替代」',
           '收件人 stephane.manuse@ 直呼 Stéphane，抄 Thomas Eleaume；6 次打开无回复 → 二次触达换切口「fill your catalogue gaps under your own label」；发信窗口 Thu 12–14 CET；法语一句引子'],
    notes='贴标 30% 目标 + 分销 20%；B BIG；加厚一次；升 A 次候选；坐实（SIREN）。')
put('SB-448', key='it', batch=B, name='BETTINI S.R.L.（bettinivideo.com；注册地 Via Marco Ulpio Traiano 16 Milano，运营 / 研发 / 生产 Via E. H. Grieg 23 Saronno (VA)；P.IVA / CF 11883080159；REA MI-1506925）— 1996-09-23 由 Walter 与 Massimo Bettini 兄弟创立的意大利视频监控方案商 / 制造商（2004 收购 GAMS 品牌、2007 并入 Initel 生产分支；GAMS 录像 / 视频分析「意大利设计制造」；分部 Firenze / Roma / Bologna；在售 ComNet 交换机 + 据表内「用 ONV 的直接带标卖」）；股本 €119,000；营收 €8.94M（2025）；42 人（2026）；AD Walter Bettini；Simon「可以尝试多跟进一下」；群发 6 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：官网页脚（Bettini S.r.l.；Milan Register of Companies no. 11883080159；R.E.A. MI-1506925；Capital 119,000.00 Euro；AEE IT15090000009003；Via E. H. Grieg 23 Saronno；info@；+39 0289651000）+ ufficiocamerale（BETTINI S.R.L.；P.IVA 11883080159；Via Marco Ulpio Traiano 16 Milano；Data Iscrizione 23/09/1996；Fatturato € 8.944.233 2025；Dipendenti 42 2026；Utile € 44.374；ATECO 26）+ 官网访谈（Walter Bettini AD；1996 与兄弟 Massimo 创立；2004 GAMS；2007 Initel）+ secsolution（25 周年；Rho 起家；分部 Roma / Firenze / Bologna）+ LinkedIn（51–200 口径）',
    url='https://www.ufficiocamerale.it/9537/bettini-srl',
    number='P.IVA / CF 11883080159；REA MI-1506925', status='Active', incorporated='1996-09-23', company_type='S.r.l.（Bettini 家族私有；股本 €119,000）',
    sic=['视频监控系统制造 / 分销（自有 GAMS 品牌 NVR / 视频分析；ATECO 26；面向安装商；3 分部）'],
    address='运营 Via E. H. Grieg 23, 21047 Saronno (VA)；注册 Via Marco Ulpio Traiano 16, 20149 Milano', accounts='2025 营收 €8,944,233；净利 €44,374', accounts_due='—', size_band='中小（42 人）',
    officers=['Walter Bettini — Amministratore Delegato / 联合创始人 = 拍板人', 'Massimo Bettini — 联合创始人', 'Marco Contu — 研究档 KP（info@）= 收件人', 'Giuseppe Costantini — 研究档 KP'], psc='Bettini 家族', charges='', prev_names=[],
    lines=['**已经把中国 PoE 交换机贴 GAMS 标卖的意大利方案商（营收 €8.9M、42 人、3 分部）→ 贴标 OEM 30% 目标，B BIG，加厚一次；升 A 候选（回信即 A）**：STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI 工业线一页纸 + 1:1 对照其现贴标机型；稿内不点名 ONV / ComNet',
           '收件人 info@ 点名 Marco Contu，抄 Walter Bettini（AD）；6 次打开无回复 → 二次触达换切口「a second OEM source for your GAMS-branded switches」；发信窗口 Thu 12–14 CET；意语一句引子'],
    notes='贴标 30% 目标；B BIG；加厚一次；升 A 候选；坐实（P.IVA + REA + 营收）。')
put('SB-449', key='us', batch=B, name='BV Security = BV USA LLC（bvsecurity.com；**美国伊利诺伊 Elk Grove Village 1951 Landmeier Rd**，研究档误记意大利）— 2009 年起的 PoE 交换机 / 注入器 / 摄像机 / 监控硬盘批发商，自称 OEM/ODM manufacturer，**自有品牌 BV-Tech**（POE-SW802G、SW802-DIN 等 Amazon 热销 264+ 评价）；GeoVision 授权经销；Managing Member Chien Chang Lu，Co-Managing Director / Owner Lisa Tsai；7–11 人；$5.3M 口径；IL LLC 号未取 → 部分坐实；研究档 KP Zehua W（support@）；群发 6 次打开', iso='US', fetched=F,
    source='IT→US · 1 次检索：官网产品页 schema（BV USA LLC alternateName BV Security；1951 Landmeier Road Elk Grove Village IL 60007；sales@bvsecurity.com；+1 877-985-5888）+ About Us（BV Security is an OEM/ODM manufacturer located in the Northwest Suburbs of Chicago … authorized re-seller of GeoVision）+ LinkedIn（BV USA LLC；Founded 2009；11–50；POE Switch and IP Camera）+ buzzfile（BV USA LLC；Chien Chang Lu Managing Member；(847) 619-2288）+ ZoomInfo（Lisa Tsai Co-Managing Director and Owner；$5.3M）+ RocketReach（7 人；Founded 2009）；IL SoS 文件号未取',
    url='https://bvsecurity.com/pages/about-us',
    number='IL LLC（文件号未取）', status='Active', incorporated='2009', company_type='LLC（华裔家族私有）',
    sic=['PoE 交换机 / 注入器 / 摄像机 / 监控硬盘 批发 + 自有品牌 BV-Tech（亚马逊 + 自营店）+ 安装服务'],
    address='1951 Landmeier Rd, Elk Grove Village, IL 60007', accounts='—', accounts_due='—', size_band='小微（7–11 人）',
    officers=['Chien Chang Lu — Managing Member = 拍板人', 'Lisa Tsai — Co-Managing Director / Owner = 拍板人', 'Zehua W — 研究档 KP（support@）= 技术 / 客服，改投 sales@ 点名 Lisa Tsai'], psc='Lu / Tsai', charges='', prev_names=[],
    lines=['**国别更正：美国伊利诺伊（研究档误记意大利 → country_fix 美国）**；**自有 BV-Tech 标 PoE 交换机批发商 = 贴标 OEM 30% 目标（它的 SW802G 类机型正是 STC-028GP / STC-228GP 的贴标对象）+ 工业 DIN 线（STI-054GP / STI-144GP），B BIG，加厚一次；升 A 候选（回信即 A）**；亚马逊渠道 → 价格敏感，报 OEM 30% 档不报分销档',
           '收件人改 sales@ 点名 Lisa Tsai / Chien Chang Lu；华裔业主 → 中文直联 Simon 定（默认否）；6 次打开无回复 → 二次触达换切口「second OEM source for your BV-Tech line」；发信窗口 Wed 08–10 CT；其 NDAA 博客口径我方不碰'],
    notes='贴标 30% 目标；B BIG；加厚一次；升 A 候选；country_fix 美国；部分坐实。')
print('b107 第 1/3 8 written')
