# -*- coding: utf-8 -*-
"""第 107 批（T29-U100，2026-10-28）欧洲其他国家 B 池第 1 轮 · 第 3/3（8 户）—— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 107
F = '2026-10-28'

put('SB-311', key='cz', batch=B, name='DIPOL 捷克站 = TOMI CZECH, s.r.o.（dipolnet.cz；dipolnet@t-cz.com；总部 Skopalova 2991/22, 750 02 Přerov；IČO 26830370；DIČ CZ26830370；门店 Praha-Modřany / Brno-Černovice / Lipník nad Bečvou）— 波兰 DIPOL（Kraków；2026-06-10 由 Sp. j. 改制为 DIPOL sp. z o.o.，1990 起的 CCTV / WLAN / TV-SAT 欧洲分销商 + 天线制造商）在捷克的销售公司（2000+ SKU；Hikvision / Dahua / TP-Link / Ultimode）；表内「switch 展示页很多；可多跟进」；与 SB-1023 DIPOL 葡萄牙同集团 → **采购在 Kraków 总部**；群发 8 次无回复 5 次打开', iso='CZ', fetched=F,
    source='CZ · 1 次检索：dipolnet.cz 首页 / Firma DIPOL（Centrála Skopalova 2991/22 750 02 Přerov；dipolnet@t-cz.com；+420 734 310 460；Společnost DIPOL založena 1990 … evropský distributor CCTV, WLAN, TV-SAT a výrobce antén）+ dipolnet.cz „DIPOL- TOMI CZECH s.r.o.“ 页（Fakturační adresa a sídlo TOMI CZECH, s.r.o. Skopalova 2991/22 Přerov；IČ 26830370；DIČ CZ26830370）+ firmy.cz / info-praha（IČO 26830370；门店 Praha-Modřany；Brno；Lipník）+ dipolnet.cz Aktuality 2026-06-10（DIPOL sp. z o.o.，ul. Ciepłownicza 40 31-574 Kraków，原 DIPOL Gołaszewski Waśniowski Sp. j.）',
    url='https://www.dipolnet.cz/dipol-_tomi_czech_s_r_o_m120.htm',
    number='IČO 26830370；DIČ CZ26830370', status='Active', incorporated='未取（捷克站运营 20+ 年）', company_type='s.r.o.（波兰 DIPOL 集团捷克销售公司）',
    sic=['CCTV / WLAN / TV-SAT / 线缆 批发 + 零售（DIPOL 目录；3 门店）'],
    address='Skopalova 2991/22, 750 02 Přerov（门店 Praha / Brno / Lipník nad Bečvou）', accounts='—', accounts_due='—', size_band='小型（集团子公司）',
    officers=['（未具名）— 收件人 dipolnet@t-cz.com；**真正的选品 / 采购在 Kraków 总部（orders@dipolnet.com）**'], psc='DIPOL sp. z o.o.（Kraków）', charges='', prev_names=[],
    lines=['**集团目录制分销的捷克销售站 → 分销 20%，但选品权在波兰总部：一页纸一次（STC-028GP / STC-228GP / STC-2224GP 对照其在售 TP-Link 价位）并请转给 Kraków 采购；与 SB-1023 并线记一笔；无回声 → 不动**',
           '8 次无回复 5 次打开 → 二次触达换切口「one PoE line for all DIPOL country sites」；发信窗口 Thu 12–14 CET；捷克语一句引子'],
    notes='分销 20%（选品在波兰总部）；一页纸一次 → 不动；与 SB-1023 同集团；坐实（IČO）。')
put('SB-128', key='other', batch=B, name='Órbita Digital = CONEXIÓN B2B 2005, S.L.（orbitadigital.com；奥维耶多 Dr. Francisco Grande Covián 3, Bajo, 33011 Oviedo（阿斯图里亚斯）；CIF B74173303）— 2004 年成立（公司）、2009 年起网店的电信 / 网络 / 光纤 / 多媒体 / 安防 分销与进口商（Triax / Televes / Ikusi / Kathrein / Hikvision / Dahua / Ubiquiti / ZKTeco；自称发货 184 国；马德里 / 巴塞罗那电话）；表内「安防为主，之前有 UTEPO 的交换机」；群发 5 次打开', iso='ES', fetched=F,
    source='ES · 1 次检索：orbitadigital.com Legal warning（CONEXIÓN B2B 2005 S.L. con CIF B74173303 … owner of www.orbitadigital.com；info@orbitadigital.com）+ Company（Founded in Oviedo in 2004 under Conexión B2B 2005, S.L.；2009 online store Órbita Digital；over 184 countries；VAT ESB74173303；Dr. Francisco Grande Covián 3 33011 Oviedo）+ Confianza Online（Razón social CONEXION B2B 2005, S.L.；CIF ESB74173303；985 288 282）+ Location（Madrid +34 910 052 331；WhatsApp 644 40 90 03）',
    url='https://www.orbitadigital.com/en/content/4-company',
    number='CIF B74173303', status='Active', incorporated='2004（网店 2009）', company_type='S.L.（私有；Grupo Conexión）',
    sic=['电信 / 网络 / 光纤 / 多媒体 / 安防 产品分销 + 跨境网店'],
    address='Dr. Francisco Grande Covián 3, Bajo, 33011 Oviedo（Asturias）', accounts='—', accounts_due='—', size_band='小型（推定 10–20 人）',
    officers=['（未具名）— 收件人 info@orbitadigital.com（点名 compras / responsable de networking）'], psc='未取', charges='', prev_names=[],
    lines=['**跨境网店型分销商（曾上架 Utepo 类交换机）→ 分销 20%，B，加厚一次（small）**：STC-028GP / STC-228GP / STC-2224GP / STC-424XGGPM-280W 一页纸 + 1:1 对照其在售同类；MOQ 1 + 15 天有效价对网店友好',
           '收件人 info@ 点名 compras；5 次打开无回复 → 二次触达换切口「a PoE switch line you can list this month」；发信窗口 Thu 12–14 CET；西语一句引子；稿内不点名 Utepo / Hikvision'],
    notes='分销 20%；B；加厚一次（small）；坐实（CIF）。')
put('SB-159', key='it', batch=B, name='EL.MO. S.p.A.（a socio unico；elmospa.com；帕多瓦 Campodarsego Via Pontarola 70, 35011；P.IVA / CF 00605640283；REA PD-126325）— 1976 年登记（REA 1976-02-06）的意大利专业安防系统制造商（入侵报警 EN 50131、门禁、CCTV、无线；经销商 / 安装商网络）；股本 €3,000,000；2025 营收 €30.57M、净利 €1.49M；79 人；表内「CCTV 帧田交换机」「可以尝试多跟进一下」；研究档 KP Agostino Avolio（Technical / Commercial Agent）、Mauro Felice；群发 5 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：ufficiocamerale（EL.MO. S.P.A.；P.IVA 00605640283；VIA PONTAROLA 70 35011 CAMPODARSEGO (PD)；Rea 126325；Data Iscrizione 01/01/1976；Fatturato € 30.569.956 2025；Dipendenti 79 2026；Utile € 1.491.081；Capitale € 3.000.000；ATECO 261）+ abbrevia（REA PD126325 registrazione 06/02/1976；S.p.A.）+ aziende.it（2024 € 30.66M；2022 € 24.18M）+ elmospa.com 页脚（Capitale Sociale € 3.000.000 i.v.；Registro Imprese di Padova 00605640283；+39 049 9203333）+ 隐私页（S.P.A. a socio unico）',
    url='https://www.ufficiocamerale.it/2756/elmo-spa',
    number='P.IVA / CF 00605640283；REA PD-126325', status='Active', incorporated='1976', company_type='S.p.A. a socio unico（股本 €3,000,000）',
    sic=['专业安防系统制造（入侵 / 门禁 / CCTV / 无线；ATECO 26.1）— 经销商 / 安装商渠道'],
    address='Via Pontarola 70, 35011 Campodarsego (PD)', accounts='2025 营收 €30,569,956；净利 €1,491,081', accounts_due='—', size_band='中型（79 人）',
    officers=['（未具名）— 拍板层：Direzione Acquisti / Product Management（S.p.A. a socio unico，单一股东）', 'Agostino Avolio — Technical / Commercial Agent（研究档 KP，agostino.avolio@）= 收件人（代理，非采购）', 'Mauro Felice — 研究档 KP'], psc='单一股东（未取）', charges='', prev_names=[],
    lines=['**€30M / 79 人的安防制造商，CCTV 线已配中国交换机 → 贴标 OEM 30% 目标（EL.MO. 标 PoE 交换机进其 CCTV 目录），B BIG，加厚一次；升 A 候选（回信即 A）**：STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI-154GP 一页纸 + 1:1 对照其目录在售机型',
           '研究档 KP Avolio 是技术 / 商务代理，非采购 → 投 Avolio 的同时抄 info@ 点名 Ufficio Acquisti / Product Manager CCTV；5 次打开无回复 → 二次触达换切口「a second OEM source for the switches in your CCTV catalogue」；发信窗口 Thu 12–14 CET；意语一句引子'],
    notes='贴标 30% 目标；B BIG；加厚一次；升 A 候选；坐实（P.IVA + REA + 营收）。')
put('SB-197', key='it', batch=B, name='Intellisystem Technologies S.r.l.（intellisystem.it；锡拉库萨 Via Augusto Murri 1, 96100 Siracusa；P.IVA / CF 01424300893）— 2000 年起（S.r.l. 2003）由 Cristian Randieri 博士创立的工业网络 / 监控 / 自动化 / 远程控制方案商（在售 3onedata 工业交换机；ATECO 26.20）；2–5 人、营收 <€0.25M 口径（impresaitalia）；President & CEO Cristian Randieri；研究档 KP「Walter Randieri Engineer」「Clelia Randieri Sales Manager」疑为误归属（官网：Clelia Rizza 创始董事）；群发 6 次 5 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：intellisystem.it Contacts（Intellisystem Technologies S.r.l.；P.IVA e C.F. IT01424300893；Via Augusto Murri N°1 96100 Siracusa；+39 0931-1756256）+ reportaziende（Sede legale Via Augusto Murri 1 Siracusa；ATECO 26.20.00）+ impresaitalia（Classe di fatturato 0–0,25 Ml；dipendenti 2–5；P.IVA 01424300893）+ About Us（President & CEO Cristian Randieri PhD；Clelia Rizza Founding Board Member；Roberta Cassarino Communication Manager）+ Crunchbase（established 2000 as engineering office；CEO & Founder since 2003-03-22）；REA 未取',
    url='https://www.intellisystem.it/en/intellisystem-contact/',
    number='P.IVA / CF 01424300893（REA 未取）', status='Active', incorporated='2000（事务所）/ 2003（S.r.l.）', company_type='S.r.l.（创始人持有）',
    sic=['工业网络 / 监控 / 自动化方案 + 研发（在售 3onedata 工业交换机；ATECO 26.20）'],
    address='Via Augusto Murri 1, 96100 Siracusa', accounts='营收 <€0.25M（口径）', accounts_due='—', size_band='小微（2–5 人）',
    officers=['Cristian Randieri — President & CEO / 创始人 = 拍板人 / 收件人（randieri@intellisystem.it；研究档写作 Walter Randieri 疑为误归属 → 同一邮箱）', 'Clelia Rizza — Founding Board Member（研究档写作 Clelia Randieri）'], psc='Randieri', charges='', prev_names=[],
    lines=['**2–5 人工业方案商（卖 3onedata）→ 分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-288DGGPM 1:1 对照 3onedata 同口数）；无回声 → 不动**；稿内不点名 3onedata',
           '收件人 randieri@ 直呼 Cristian（CEO）；5 次打开无回复 → 二次触达换切口；发信窗口 Thu 12–14 CET；意语一句引子'],
    notes='分销 20% small；一页纸一次 → 不动；坐实（P.IVA + 官网）；KP 名修正 Cristian Randieri。')
put('SB-425', key='it', batch=B, name='GSG INTERNATIONAL S.R.L.（gsginternational.com；米兰 Trezzano sul Naviglio Piazza San Lorenzo 48（运营 Via C. Colombo 23）；P.IVA 12178170150；REA MI-1537545）— 1997-06-12 登记的安防市场增值分销商（视频监控 / 门禁 / 网络；品牌 barox / ComNet / Lantech / Nedap；姊妹制造商 Euklis srl（2017，创始人同为 Antonmarco Catania）的 NVR / 人脸识别；Nettosecurity 奥特莱斯）；股本 €53,700；2024 营收 €2.37M、净利 €308（极薄）；7 人；Chairman Antonmarco Catania（1997 创始）、CEO Ludovico Paveri Fontana（2017 起，前 CTO；研究档 KP）；群发 5 次打开', iso='IT', fetched=F,
    source='IT · 1 次检索：ufficiocamerale（GSG INTERNATIONAL S.R.L.；Rea 1537545；Data Iscrizione 12/06/1997；Fatturato € 2.374.984 2024；Dipendenti 7 2026；Utile € 308；ATECO 46502）+ fatturatoitalia（P.IVA 12178170150；REA MI 1537545；Piazza San Lorenzo 48 Trezzano sul Naviglio）+ gsginternational.com 页脚（P.IVA 12178170150；Cap. Sociale € 53.700,00；REA 1537545）+ Team（Antonmarco Catania Chairman，1997 创 GSG、2017 创 Euklis srl；Ludovico Paveri Fontana）+ 2017 新闻稿（Paveri Fontana 任 AD）+ Nedap 合作稿（CEO）',
    url='https://www.ufficiocamerale.it/1127/gsg-international-srl',
    number='P.IVA / CF 12178170150；REA MI-1537545', status='Active', incorporated='1997-06-12', company_type='S.r.l.（私有；股本 €53,700）',
    sic=['安防市场增值分销（视频监控 / 门禁 / 网络；ATECO 46.52）+ 控制室服务'],
    address='Piazza San Lorenzo 48, 20090 Trezzano sul Naviglio (MI)', accounts='2024 营收 €2,374,984；净利 €308', accounts_due='—', size_band='小型（7 人）',
    officers=['Ludovico Paveri Fontana — Amministratore Delegato / CEO（2017 起；研究档 KP，ludovico.paveri@）= 拍板人 / 收件人', 'Antonmarco Catania — Chairman / 创始人（兼 Euklis srl）'], psc='Catania（推定）', charges='', prev_names=[],
    lines=['**卖 barox / ComNet / Lantech 的增值分销商（CEO 直达）→ 分销 20%，B，加厚一次（small）；姊妹厂 Euklis 的贴标 30% 一句带过**：STC-2224GP / STC-4424GCPM / STI-288DGGPM / STI-488DGGPM 一页纸 + 1:1 对照其在售工业机型；净利极薄 → 强调毛利空间',
           '收件人 ludovico.paveri@ 直呼 Ludovico；5 次打开无回复 → 二次触达换切口「a margin line beside your premium switch brands」；发信窗口 Thu 12–14 CET；稿内不点名 barox / ComNet / Lantech'],
    notes='分销 20%；B；加厚一次（small）；坐实（P.IVA + REA + 营收）。')
put('SB-625', key='other', batch=B, name='VIRTWARE – Soluções Integradas de Telecomunicações, Lda.（virtware.pt；波尔图 Vila Nova de Gaia Canidelo Rua dos Canastreiros 394, 4400-404；NIPC 506612813）— 2003-05-19 成立的网络 / 布线增值分销商（结构化布线 Cat.6a、TP-Link L2 交换机、兼容光模块、机柜、VoIP、WLAN、光纤 MTP/MPO、ATEN KVM、UPS）；股本 €5,000；CAE 46900；2–10 人；Owner Augusto Oliveira（研究档 KP）；表内无跟进记录；群发 5 次打开', iso='PT', fetched=F,
    source='PT · 1 次检索：Iberinform（VIRTWARE - SOLUÇÕES INTEGRADAS DE TELECOMUNICAÇÕES, LDA.；NIF/NIPC 506612813；Soc. Por Quotas；Rua Canastreiros Nr. 394 4400-404 Vila Nova de Gaia；CAE 46900；Data de constituição 2003/05/19；Conservatória do Porto）+ racius（Capital Social € 5.000,00）+ virtware.pt 首页（Switches TP-Link Layer 2；MiniGBIC compatíveis；Bastidores；VoIP；MTP/MPO）+ LinkedIn（Value-added distributor；2–10 employees；Canidelo VNG）+ 3ptest（+351 22781 0460；info@virtware.pt）',
    url='https://www.iberinform.pt/empresa/24049432/virtware-solucoes-integradas-de-telecomunicacoes-lda',
    number='NIPC 506612813', status='Active', incorporated='2003-05-19', company_type='Lda.（Sociedade por Quotas；股本 €5,000）',
    sic=['网络 / 结构化布线 / 光纤 增值分销（CAE 46900）'],
    address='Rua dos Canastreiros 394, Canidelo, 4400-404 Vila Nova de Gaia（Porto）', accounts='—', accounts_due='—', size_band='小微（2–10 人）',
    officers=['Augusto Oliveira — Owner / sócio-gerente（研究档 KP，augusto@virtware.pt）= 拍板人 / 收件人'], psc='Augusto Oliveira', charges='', prev_names=[],
    lines=['**卖 TP-Link L2 + 布线的小型增值分销商（老板直达）→ 分销 20% small，一页纸一次（STC-2224GP / STC-424XGGPM-280W / STC-110XGE 对照 TL-SG5428 类价位）；有回声再加厚**；稿内不点名 TP-Link',
           '收件人 augusto@ 直呼 Augusto；表内从未跟进 → 首封按一次触达写（不伪造 Re:）；发信窗口 Thu 12–14 WET；葡语一句引子'],
    notes='分销 20% small；一页纸一次；坐实（NIPC）。')
put('SB-048', key='other', batch=B, name='ALMAKS DOO BEOGRAD（Almaks Security Systems；almaks.rs；贝尔格莱德 Vračar Gospodara Vučića 129, 11118；матични број 06698182；ПИБ 100571552）— 1992-06-15 登记（品牌 1991 起）的塞尔维亚安防系统集成商（火灾 / 入侵报警、视频安防、气溶胶灭火、门禁考勤、周界、对讲；шифра 8020）；所有人兼董事 Slobodan Maksimović（100%）、董事 Uroš Maksimović（二代）、代表 Predrag Đorđević；51–100 人；子公司 ALMAKS GPS d.o.o.（2017）；**2012-03 成交 20 对 1V1D 视频光端机，此后无跟进**；群发 5 次打开', iso='RS', fetched=F,
    source='RS · 1 次检索：companywall.rs（ALMAKS DOO BEOGRAD；Gospodara Vučića 129 11118 Beograd (Vračar)；Aktivan；PIB 100571552；MB 06698182；Datum osnivanja 15.6.1992；Vlasnik Slobodan Maksimović 100%；Direktor Slobodan Maksimović；Direktor Uroš Maksimović；Zastupnik Predrag Đorđević；šifra 8020）+ infostud（51–100 zaposlenih）+ PKS 协会名录（ALMAKS Security Systems d.o.o.；Slobodan Maksimović vlasnik i direktor；almaks@almaks.rs / smaksimovic@almaks.rs；06698182）+ almaks.rs（Since 1991；Founder Slobodan Maksimović）+ companywall ALMAKS GPS d.o.o.（MB 21315931，2017）',
    url='https://www.companywall.rs/firma/almaks-doo-beograd/MMfjjXsD',
    number='Матични број 06698182；ПИБ 100571552', status='Aktivan', incorporated='1992-06-15', company_type='d.o.o.（Maksimović 家族 100%）',
    sic=['安防系统集成（报警 / 视频 / 灭火 / 门禁 / 周界；шифра 8020）'],
    address='Gospodara Vučića 129, 11118 Beograd (Vračar)', accounts='—', accounts_due='—', size_band='中小（51–100 人）',
    officers=['Slobodan Maksimović — Vlasnik i direktor（100%）= 拍板人 / 收件人（smaksimovic@almaks.rs，PKS 公开名录）', 'Uroš Maksimović — Direktor（二代）= 抄送', 'Predrag Đorđević — Zastupnik'], psc='Slobodan Maksimović（100%）', charges='', prev_names=[],
    lines=['**51–100 人的老成单集成商（2012 买过 20 对光端机）→ 集成 25%，B BIG，加厚一次；升 A 次候选（回信即 A）**：STC-028GP / STC-228GP / STC-2224GP + STI-154GP / STI-288DGGPM 一页纸；开头可引 2012 那单（S-box 有记录才引）',
           '收件人 smaksimovic@ 直呼 Slobodan，抄 Uroš；5 次打开无回复 → 二次触达换切口「14 years on, a PoE line for your CCTV projects」；发信窗口 Thu 12–14 CET；塞语一句引子'],
    notes='集成 25%；B BIG；加厚一次；升 A 次候选；坐实（МБ + ПИБ）。')
put('SB-012', key='cz', batch=B, name='XCAM CZech s.r.o.（xcam.cz；俄斯特拉发 Gen. Píky 3038/1a, 702 00 Ostrava – Moravská Ostrava；IČO 29397839；DIČ CZ29397839）— 2012-02-29 登记的小型安防集成 / 安装商（摄像系统安装维护、报警 / 门禁、车牌识别道闸、工地延时、光伏电站摄像；Jablotron / AXIS；官网提 LAN 元件）；jednatel Alexandr Grepl（唯一，2012 起）；表内「已在用 E-link 产品，9 次推送无回复」；群发 5 次打开', iso='CZ', fetched=F,
    source='CZ · 1 次检索：rejstrik.penize.cz（XCAM CZech s.r.o.；IČO 29397839；Datum vzniku a zápisu 29. 2. 2012；Jednatel Alexandr Grepl Ostrava od 29.2.2012；Počet členů 1）+ zivefirmy（IČ 29397839；DIČ CZ29397839；DS y2rah2u）+ xcam.cz（Gen Piky 1A Ostrava；IČO 29397839 / DIČ CZ29397839；kamery pro solární elektrárny a LAN prvky）+ firmy.cz（Gen. Píky 3038/1a；30 years of experience；Jablotron）',
    url='https://rejstrik.penize.cz/29397839-xcam-czech-s-r-o',
    number='IČO 29397839；DIČ CZ29397839', status='Active', incorporated='2012-02-29', company_type='s.r.o.（一人公司）',
    sic=['安防系统集成 / 安装（CCTV / 报警 / 门禁 / 车牌识别 / 光伏电站监控）'],
    address='Gen. Píky 3038/1a, 702 00 Ostrava – Moravská Ostrava', accounts='—', accounts_due='—', size_band='小微（1–5 人）',
    officers=['Alexandr Grepl — jednatel（唯一）= 拍板人 / 收件人'], psc='Alexandr Grepl（推定）', charges='', prev_names=[],
    lines=['**小型安装商（已用国产 E-link 类 PoE）→ 集成 25% small，一页纸一次（STC-028GP / STI-054GP 对光伏电站 / 道闸场景）；9 次无回复 + 无回声 → 不动**',
           '收件人直呼 Alexandr；5 次打开无回复 → 二次触达换切口「outdoor-cabinet PoE for solar-plant cameras」；发信窗口 Thu 12–14 CET；捷克语一句引子'],
    notes='集成 25% small；一页纸一次 → 不动；坐实（IČO）。')
print('b107 第 3/3 8 written')
