# -*- coding: utf-8 -*-
"""第 107 批（T29-U100，2026-10-28）欧洲其他国家 B 池第 1 轮 · 第 2/3（8 户）—— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 107
F = '2026-10-28'

put('SB-198', key='lt', batch=B, name='Katalita, UAB（katalita.lt；考纳斯区 Neveronys Tvenkinio g. 10；įmonės kodas 134637695；PVM LT346376917）— 1995-12-18 登记的 ICT / 网络设备批发商（EVRK 465000；MikroTik / Ubiquiti（官方 reseller 名录）/ Teltonika / TP-Link / LigoWave / Mimosa / Extralink 分销 —「Extralink 是他们的品牌」存疑，Extralink 属 Batna24，Katalita 只是转售）；股本 €8,690；6–8 人；2025 营收 €6.86M、利润 €132k（人均极高 = 纯批发）；负责人 Donatas Zubenas；CFO Robertas Zubenas（研究档 KP，同姓 → 家族）；群发 4 次 6 次打开', iso='LT', fetched=F,
    source='LT · 1 次检索：rekvizitai.vz.lt（Katalita, UAB；code 134637695；founded 1995；VAT LT346376917；Share capital 8 690 €；Tvenkinio g. 10 Pabiržio k. LT-54477 Kauno r.；Sodra 2026-10-17 6 darbuotojai）+ 官网 Kontaktai（KATALITA UAB；Tvenkinio g. 10 Neveronių k.；kodas 134637695；PVM LT346376917；+370 603 03213；品牌 Mikrotik / Ubiquiti / Ligowave / TP-LINK / Mimosa / Teltonika / Xiaomi / Extralink）+ tax.lt（įregistruota 1995-12-18；2025 pajamos 6,86 mln. €；pelnas 132 tūkst. €；6 darbuotojai；465000 IRT įrangos didmeninė prekyba）+ imoniubaze / kaina24（Vadovas Donatas Zubenas；8 darbuotojai）+ ui.com Distributors（Katalita Resellers Lithuania）',
    url='https://rekvizitai.vz.lt/en/company/katalita/',
    number='įmonės kodas 134637695；PVM LT346376917', status='Veikiantis / Active', incorporated='1995-12-18', company_type='UAB（Zubenas 家族私有；股本 €8,690）',
    sic=['ICT / 网络设备批发（EVRK 46.50；MikroTik / Ubiquiti / Teltonika 渠道；面向立陶宛 + 出口）'],
    address='Tvenkinio g. 10, Neveronių k., LT-54478 Kauno r. sav.', accounts='2025 营收 €6.86M；利润 €132k', accounts_due='—', size_band='小微（6–8 人；人均营收 ≈€1M）',
    officers=['Donatas Zubenas — Vadovas（负责人）= 拍板人', 'Robertas Zubenas — CFO（研究档 KP，robertas@katalita.lt）= 收件人'], psc='Zubenas 家族（推定）', charges='', prev_names=[],
    lines=['**MikroTik / Ubiquiti 渠道的纯批发商（6 人做 €6.9M）→ 分销 20%，B BIG，加厚一次**：STC-028GP / STC-228GP / STC-2224GP / STC-424XGGPM-280W 一页纸 + 与其在售 TP-Link / MikroTik 价位 1:1；**不接 Extralink 话题**（非其品牌）；稿内不点名 MikroTik / Ubiquiti',
           '收件人 robertas@ 直呼 Robertas，抄 Donatas Zubenas；6 次打开无回复 → 二次触达换切口「a PoE line at wholesale margin beside your MikroTik shelf」；发信窗口 Thu 12–14 EET'],
    notes='分销 20%；B BIG；加厚一次；坐实（įmonės kodas + 营收）。')
put('SB-095', key='it', batch=B, name='Mtechnology（「Mtechnology Divisione Italiana — marchio registrato」；mtechnology.it；P.IVA 02451810960（站脚；蒙扎-布里安扎 / 米兰区号段）；法人全名未取 → 部分坐实；installer 渠道价表由 Gamma Commerciale 承载，是否同一法人待补证）— 面向工业 / 极端环境（钢厂、铸造、船舶）的 AI 视频监控品牌商，**自有型号工业 PoE 交换机 MT-TP7-16GT240BT（20 口管理 16×Hi-PoE 90W / 240W）、MT-TP7308POE、MT-TP7324GE-POE、MT-TP7224E-POE**（表内「工业 FS（Utepo 式外壳）是他们自己贴标」）；只经认证安装商销售；群发 6 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：mtechnology.it 全站页脚（Mtechnology Divisione Italiana - Mtechnology è un marchio registrato - P.IVA 02451810960）+ Chi siamo / Contatti（distribuisce esclusivamente tramite rete di installatori certificati；R&D 可改 firmware / hardware）+ gammacommerciale.it（Mtechnology 安装商价表：telecamere IP、NVR、extender、switch long distance、convertitori IP）；ufficiocamerale 的 M - TECHNOLOGY S.R.L. 00892280942（Vinchiaturo CB，1 人）= 同名异主，不取',
    url='https://www.mtechnology.it/chi-siamo.1.96.uw',
    number='P.IVA 02451810960（站脚；法人名未取）', status='Active（站点 2026 更新）', incorporated='未取', company_type='注册商标 / 意大利分部（法人待补证）',
    sic=['工业级 AI 视频监控品牌商（自有型号摄像机 / NVR / 工业 PoE 交换机 / 长距 PoE 扩展）— 安装商渠道'],
    address='未取（P.IVA 段位 = 蒙扎-布里安扎 / 米兰）', accounts='—', accounts_due='—', size_band='小型（推定）',
    officers=['（未具名）— 收件人 info@mtechnology.it（点名 ufficio acquisti / product manager）'], psc='未取', charges='', prev_names=[],
    lines=['**已经自贴标工业 PoE 交换机（MT-TP7 系列，Utepo 式）的品牌商 = 贴标 OEM 30% 正中目标，B BIG，加厚一次；升 A 次候选**：STI-288DGGPM / STI-244DGGPM / STI-488DGGPM / STI-154GP 一页纸 + 1:1 对照 MT-TP7-16GT240BT（90 W Hi-PoE 口 / 240 W 预算）；稿内不点名 Utepo',
           '收件人 info@ 点名 ufficio acquisti；6 次打开无回复 → 二次触达换切口「second source for your MT-TP7 industrial PoE family」；发信窗口 Thu 12–14 CET；意语一句引子；法人名 / 所在地待补证（下次核：Gamma Commerciale 是否同主）'],
    notes='贴标 30% 目标；B BIG；加厚一次；升 A 次候选；部分坐实（P.IVA 站脚、法人名未取）。')
put('SB-244', key='it', batch=B, name='Innowatt = GRUPPO COSOLA S.R.L. 的自有品牌网店（innowatt.it；P.IVA 01218230777（站脚；马泰拉段位）；LinkedIn「Gruppo Cosola Impianti Tecnologici」= 技术安装集团）— 电气 / 技术 / 安防材料电商（视频监控 772 件、网络 295 件；Hikvision / Uniview / Ruijie / Safire / X-Security 系配件贴 INNOWATT 标）；REA / 注册地未取 → 部分坐实；表内「工业 FS，中科德能的」「可以尝试多跟进一下」；群发 12 次无回复 6 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：innowatt.it 页脚（© 2026, Innowatt GRUPPO COSOLA S.R.L - P.IVA: 01218230777；shop@innowatt.it；linkedin gruppo-cosola-impianti-tecnologici）+ About（Innowatt is an Italian brand of electrical, technological and safety equipment）+ Collections（Networking 295 / Videosorveglianza 772 / Videoregistratori 126；INNOWATT 标配件）；atoka 的 Innowatt Srl Semplificata 05403310757（Sannicola LE，电力分销）= 同名异主，不取',
    url='https://www.innowatt.it/en/pages/about',
    number='P.IVA 01218230777（GRUPPO COSOLA S.R.L.；REA 未取）', status='Active（站点 2026）', incorporated='未取', company_type='S.r.l.（安装集团 + 自有品牌电商）',
    sic=['电气 / 安防 / 网络材料电商（自有 Innowatt 标）+ 技术系统安装（Gruppo Cosola）'],
    address='未取（P.IVA 段位 = 马泰拉省，巴西利卡塔）', accounts='—', accounts_due='—', size_band='小型（推定）',
    officers=['（未具名）— 收件人 commerciale@ / shop@innowatt.it（点名 ufficio acquisti）'], psc='Cosola 家族（推定）', charges='', prev_names=[],
    lines=['**自有标配件电商 + 安装集团 → 贴标 OEM 30% 可谈（Innowatt 标 PoE 交换机，小批量）+ 分销 20%，B，加厚一次（small）**：STC-028GP / STC-228GP / STC-2224GP + STI-154GP 一页纸；稿内不点名 Hikvision / Ruijie',
           '12 次群发无回复但 6 次打开 → 二次触达必须换切口「your own label on the PoE switch, not ours」；收件人 commerciale@ 点名 ufficio acquisti；发信窗口 Thu 12–14 CET；意语一句引子；注册地 / REA 待补证'],
    notes='贴标 30% 可谈 + 分销 20%；B；加厚一次（small）；部分坐实。')
put('SB-492', key='it', batch=B, name='SISTEL S.R.L.（Sistel Networking 事业部；sistel-networking.it / sistelsrl.it；诺瓦拉省 Suno Via Novara 21；P.IVA 01164230037；REA NO-153233）— 1986 年登记的电子元件制造商（ATECO 26.11.09）兼网络方案部（铜缆 / 光纤布线、机柜、UPS、工业交换机；官网 Industrial Ethernet Solution 专页 = 某台系品牌工业交换机 IGS-620TF 等）；2024 营收 €1.70M、净利 €206k；研究档「资本 €10k」；面向安装商 / IT 经理；群发 6 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：ufficiocamerale（SISTEL S.R.L.；P.IVA 01164230037；Via Novara 21 28019 Suno (NO)；Rea 153233；Data Iscrizione 28/05/1986；ATECO 261109；Utile € 206.464 2024）+ companyreports（Fatturato € 1.699.479 2024；Fondazione 11/07/1986）+ sistel-networking.it Chi siamo（Sistel Networking è la divisione specializzata di SISTEL srl … Da oltre 30 anni；P. IVA 01164230037；info@sistel-networking.it；0322 858077）',
    url='https://www.ufficiocamerale.it/1662/sistel-srl',
    number='P.IVA / CF 01164230037；REA NO-153233', status='Active', incorporated='1986-05-28（登记）/ 1986-07-11', company_type='S.r.l.（私有）',
    sic=['电子元件制造（ATECO 26.11）+ 网络方案事业部（布线 / 机柜 / UPS / 工业交换机，面向安装商）'],
    address='Via Novara 21, 28019 Suno (NO)', accounts='2024 营收 €1,699,479；净利 €206,464', accounts_due='—', size_band='小型（推定 10–20 人）',
    officers=['（未具名）— 收件人 info@sistel-networking.it（点名 responsabile divisione Networking）'], psc='未取', charges='', prev_names=[],
    lines=['**给安装商做「布线 + 机柜 + 工业交换机」整包的小方案商（现用台系工业交换机）→ 集成 25%，B，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM 1:1 对照 IGS-620TF 类）；有回声再加厚**；稿内不点名台系品牌',
           '收件人 info@ 点名 divisione Networking；6 次打开无回复 → 二次触达换切口「a second industrial switch line for your cabinet bundles」；发信窗口 Thu 12–14 CET；意语一句引子'],
    notes='集成 25% small；一页纸；坐实（P.IVA + REA + 营收）。')
put('SB-908', key='it', batch=B, name='CT Service di Cerino Gianluca（Techlu 网店 techlu.it / ctservicestore.it；坎波巴索 Viale Duca d’Aosta 43, 86100 Campobasso（莫利塞）；P.IVA 01771320700；CF CRNGLC67L29L483I）— 个体工商户（impresa individuale；ATECO 46.47.3；3–10 年）：安防 / 监控 / 自动化 / 智能家居 / 网络 门店 + 安装商网店（Ajax 目录；在售 PoE 交换机 SW8FE2FE-100W、SW4GE1GE-65W、Safire DIN PoE —「商业 PoE，ONV 的」）；联系邮箱 Gmail；群发 6 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：informazione-aziende（Ct Service Di Cerino Gianluca；VIALE DUCA D’AOSTA 43 86100 Campobasso；CF CRNGLC67L29L483I；P.IVA 01771320700；IMPRESA INDIVIDUALE；ATECO 46.47.3；Età 3–10 anni）+ reportaziende（同）+ ctservicestore.it Contattaci（Via Duca D’Aosta 43；340 7562053；ctservicemolise@gmail.com；P.IVA 01771320700）+ robarts.it（Techlu.it è lo store online di CT Service di Cerino Gianluca … punto vendita fisico a Campobasso）',
    url='https://www.informazione-aziende.it/Azienda_CT-SERVICE-DI-CERINO-GIANLUCA',
    number='P.IVA 01771320700；CF CRNGLC67L29L483I', status='Active', incorporated='未取（3–10 年）', company_type='Impresa individuale（个体）',
    sic=['安防 / 监控 / 自动化 / 网络 零售门店 + 安装商网店（Techlu）'],
    address='Viale Duca d’Aosta 43, 86100 Campobasso (CB)', accounts='—', accounts_due='—', size_band='个体（1–3 人）',
    officers=['Gianluca Cerino — 业主（titolare）= 唯一收件人（info@techlu.it / ctservicemolise@gmail.com）'], psc='Gianluca Cerino', charges='', prev_names=[],
    lines=['**1 人安防门店 + 网店（已卖 ONV 式商用 PoE）→ 分销 20% small，一页纸一次（STC-028GP / STC-228GP 对照其 SW8FE2FE-100W 价位）；无回声 → 不动**',
           '收件人直呼 Gianluca；6 次打开无回复 → 二次触达换切口；发信窗口 Thu 12–14 CET；意语一句引子；MOQ 1 + T/T 对个体友好可提'],
    notes='分销 20% small；一页纸一次 → 不动；坐实（P.IVA 个体）。')
put('SB-326', key='other', batch=B, name='PROXEET LIMITED（proxeet.com / portablepoe.com / chiprian.com；帕福斯 Neofytou Nikolaidi 61, Yiannis Court, Floor 2, Office 201, 8011 Pafos；ΗΕ 437925，2022-08-31 注册）— 面向 ISP 的网络设备品牌商（**自有 Chiprian 系列 L3 管理交换机 + iBlock 便携 PoE 注入器**；LinkedIn 11–50、2020 起）；董事 Aleksei Kizriakov + Andrei Tikhonov（Tikhonov 兼秘书，且为多家塞浦路斯公司秘书 = 公司服务商）→ 俄籍创始团队的塞浦路斯法人；研究档 KP Marina Shkarpetina（marketplace@，用户表 RFQ）；群发 5 次打开', iso='CY', fetched=F,
    source='CY · 1 次检索：i-cyprus（PROXEET LIMITED；ΗΕ 437925；Private Limited；Registration 31/08/2022；Active；Neofytou Nikolaidi 61 Yiannis Court Floor 2 Office 201 8011 Pafos）+ companiesregistry.cy（Directors ANTREI TYCHONOV + ALEKSEI KIZRIAKOV；Secretary Antrei Tychonov，related to ANDREY ST. TIKHONOV & CO LLC）+ proxeet.shop Support（Proxeet Ltd, Neofytou Nikolaidi 61 Paphos；+357 25100999；info@proxeet.com）+ LinkedIn（11–50；Founded 2020；Telecommunications）+ D&B 目录（Computer and Electronic Product Manufacturing, Paphos）',
    url='https://i-cyprus.com/company/611007',
    number='ΗΕ 437925', status='Active（Registrar of Companies）', incorporated='2022-08-31', company_type='Private Limited（俄籍创始团队；秘书为公司服务商）',
    sic=['ISP 网络设备品牌商（自有 Chiprian L3 交换机 / iBlock PoE 注入器；网店 + marketplace）'],
    address='Neofytou Nikolaidi 61, Yiannis Court, Floor 2, Office 201, 8011 Pafos', accounts='—', accounts_due='—', size_band='小型（11–50 口径）',
    officers=['Aleksei Kizriakov — Director = 拍板人', 'Andrei Tikhonov — Director + Secretary（公司服务商，非业务人）', 'Marina Shkarpetina — Marketplace（研究档 KP，marketplace@proxeet.com；用户表 RFQ）= 收件人'], psc='未取（俄籍创始团队推定）', charges='', prev_names=[],
    lines=['**自有标 L3 交换机（Chiprian）的 ISP 设备品牌商 = 贴标 OEM 30% 目标，B BIG，加厚一次；升 A 次候选**：STC-424XGGPM-280W / STC-448XGGPM / STC-110XGE + STI 线一页纸 + 1:1 对照 Chiprian 在售机型；只报 OEM 档',
           '收件人 marketplace@ 直呼 Marina（她发过 RFQ），抄 Aleksei Kizriakov；5 次打开无回复 → 二次触达接其 RFQ 旧题；发信窗口 Thu 12–14 EET；**塞浦路斯 EU 法人，收款走正常 T/T；不碰俄方背景话题**'],
    notes='贴标 30% 目标；B BIG；加厚一次；升 A 次候选；坐实（ΗΕ）。')
put('SB-036', key='cz', batch=B, name='Inthouse Systems s.r.o.（inthouse.eu；布拉格 Grafická 769/9, Smíchov, 150 00 Praha 5；IČO 05405947；C 263202 MSPH）— 2016-09-19 登记（品牌 2013 起）的楼宇自动化软件 / 云网关小公司（Inthouse App / Studio / Cloud + Inthouse Hub，接 Siemens 等楼控）；注册资本 2,000 Kč；jednatelé 兼实益所有人 Andrej Hraško（2016）+ Matej Snoha（2017，创始人），均为斯洛伐克人；约 4 人；群发 5 次打开', iso='CZ', fetched=F,
    source='CZ · 1 次检索：or.justice.cz（Inthouse Systems s.r.o.；IČO 054 05 947；C 263202 Městský soud v Praze；Den zápisu 19. září 2016；Grafická 769/9 Smíchov）+ rejstrik.penize.cz（Jednatel Andrej Hraško Bratislava od 19.9.2016；Jednatel Matej Snoha Banská Bystrica od 5.1.2017；每位 jednatel 单独代表）+ kurzy.cz（Z. kapitál 2 000 Kč）+ hlidacstatu（Skuteční majitelé Hraško + Snoha 2022-09-30）+ inthouse.eu Privacy（Inthouse Systems s.r.o. Grafická 769/9 … IČO 05405947）',
    url='https://rejstrik.penize.cz/05405947-inthouse-systems-s-r-o',
    number='IČO 05405947；C 263202 MSPH', status='Active（1 aktivní živnost）', incorporated='2016-09-19', company_type='s.r.o.（两名斯洛伐克创始人持有；注册资本 2,000 Kč）',
    sic=['楼宇自动化软件 / 云网关（Inthouse Hub）'],
    address='Grafická 769/9, Smíchov, 150 00 Praha 5', accounts='—', accounts_due='—', size_band='小微（≈4 人）',
    officers=['Matej Snoha — jednatel / 创始人 = 拍板人 / 收件人', 'Andrej Hraško — jednatel / 实益所有人'], psc='Hraško / Snoha', charges='', prev_names=[],
    lines=['**软件 / 网关公司，硬件采购量极小 → 采购型 25% 一页纸一次（STC-028GP 配 Hub 机柜）；无回声 → 不动**',
           '收件人点名 Matej Snoha；5 次打开无回复 → 二次触达换切口；发信窗口 Thu 12–14 CET'],
    notes='采购型 25% tiny；一页纸一次 → 不动；坐实（IČO）。')
put('SB-261', key='cz', batch=B, name='RecTec servis, s.r.o.（rectec.cz；布尔诺郊 Židlochovice Nádražní 92, 667 01；IČO 17957036；DIČ CZ17957036；C 132302 KS Brno）— 2023-01-23 登记的回收生产线（破碎 / 热解 / 精炼 / 清洗）与工业自动化供应商；注册资本 200,000 Kč；jednatel Viktor Fojt（研究档 KP；布尔诺）；100% 股东 CVFT s.r.o.；2023 阿里巴巴 RFQ「BIDI 千兆光模块」（Saga 不做光模块）；表内 6 次跟进无回复；群发 5 次打开', iso='CZ', fetched=F,
    source='CZ · 1 次检索：fakturujzdarma（RecTec servis, s.r.o.；IČO 17957036；DIČ CZ17957036；Spolehlivý plátce DPH；Nádražní 92 667 01 Židlochovice；Datum vzniku 23. ledna 2023；Základní kapitál 200 000 Kč；C 132302 Krajský soud v Brně；jednatel Viktor Fojt Absolonova 637/16 Brno；společník CVFT s.r.o. 100 %；ARES 2025-08-19）+ kurzy.cz / podnikatel.cz / finmag（同）',
    url='https://rejstrik-firem.kurzy.cz/17957036/rectec-servis-sro/',
    number='IČO 17957036；DIČ CZ17957036；C 132302 KS Brno', status='Active（可靠增值税纳税人）', incorporated='2023-01-23', company_type='s.r.o.（CVFT s.r.o. 100%；注册资本 200,000 Kč）',
    sic=['回收生产线与工业自动化设备供应 / 服务'],
    address='Nádražní 92, 667 01 Židlochovice（Brno-venkov）', accounts='—', accounts_due='—', size_band='小微（2023 新设）',
    officers=['Viktor Fojt — jednatel（研究档 KP，fojt@rectec.cz）= 拍板人 / 收件人'], psc='CVFT s.r.o.（100%）', charges='', prev_names=[],
    lines=['**回收产线集成商，网络件只是配套（其 RFQ 是光模块，Saga 不做）→ 项目 25% 一页纸一次（STI-054GP / STI-144GP 产线控制柜用）；无回声 → 不动**',
           '收件人直呼 Viktor；6 次跟进 + 5 次打开无回复 → 二次触达换切口「DIN-rail switches for your recycling line cabinets」；发信窗口 Thu 12–14 CET'],
    notes='项目 25% small；一页纸一次 → 不动；坐实（IČO）。')
print('b107 第 2/3 8 written')
