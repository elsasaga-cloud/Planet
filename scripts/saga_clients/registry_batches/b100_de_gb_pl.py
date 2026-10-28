# -*- coding: utf-8 -*-
"""第 100 批（T29-U93，2026-10-28）DE 4 + GB 4 + PL 4 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 100
F = '2026-10-28'

# ---------------- DE 4 ----------------
put('SB-1133', key='de', batch=B, name='Netram Memory GmbH（netram.de；Wuppertal）— 2005 年起的内存 / 光模块 / 网络配件小型分销商（HRB 19078 Wuppertal；GF Jürgen Hübner；2–10 人）', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata（Netram Memory GmbH；Amtsgericht Wuppertal HRB 19078；EUID DER1608.HRB19078；Dohlenweg 6, 42115 Wuppertal；2005-04-14 登记；Geschäftsführer Jürgen Hübner；资本 €25,000；经营范围 Vertrieb elektronischer Bauelemente）+ registercheck（Aktiv；成立 2005-03-08；GF Jürgen Hübner *1968，自 2005-04-13）+ Kompass（NACE 4651 批发；CEO Jürgen Hübner）+ Implisense（+49 202 758050；info@netram.de）+ LinkedIn（Netram GmbH；2–10 人）',
    url='https://www.northdata.com/Netram%20Memory%20GmbH,%20Wuppertal/HRB%2019078',
    number='HRB 19078（Amtsgericht Wuppertal）· EUID DER1608.HRB19078', status='Aktiv', incorporated='2005-03-08（登记 2005-04-14）', company_type='GmbH（资本 €25,000；私有）',
    sic=['NACE 46.51 — 电脑 / 外设批发（兼容内存模块、光模块 / DAC、网络配件电商）'],
    address='Dohlenweg 6, 42115 Wuppertal', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Jürgen Hübner — Geschäftsführer（*1968，自 2005）= 研究档 KP 本人'], psc='Jürgen Hübner（推定）', charges='', prev_names=[],
    lines=['**研究档 KP 坐实 = GF 本人**；光模块 / 内存配件电商，Saga 不做光模块 → 只能切「配光模块一起卖的交换机」：STC-110XGE（$65，8×2.5G + 2×10G SFP+）+ STC-228GP → **分销 20%，小户，一页纸**',
           '表内 1 次跟进无回复 → 第二次触达换主题「a 10G uplink switch for your transceiver customers」；发信窗口 Thu 12–14 CET'],
    notes='KP = GF 本人；分销 20%；小户；一页纸。')
put('SB-1053', key='de', batch=B, name='ServiceNet EDV-Vertrieb GmbH（店名 lichtleiterkabel.com；Niederkassel）— 1996 年起的 LWL 光缆定制 / 网络布线 B2B 电商（CEO Andreas Bude；域名持有方 Traffictime Handels- & Marketing GmbH / Holger Sockel）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网首页（「Seit 1996 … Netzwerkverkabelung, Glasfaserkabel, Komponenten (aktive und passive)」）+ wlw（lichtleiterkabel.com by ServiceNet EDV-Vertrieb GmbH；Provinzialstraße 40, 53859 Niederkassel；Distributor / Wholesaler；CEO Andreas Bude；1996）+ connektar 2018-12-13（Lichtleiterkabel.de 域名由 Traffictime Handels- & Marketing GmbH（Grafschaft；GF Holger Sockel）取得；「Betrieben wird der Shop durch die ServiceNet EDV Vertriebs GmbH」）；HRB 号未取（1 次检索）',
    url='https://www.wlw.com/en/company/lichtleiterkabelcom-by-servicenet-edv-vertrieb-gmbh-1805537',
    number='GmbH（Niederkassel；HRB 号未取）', status='Active（站点 2026-01 更新）', incorporated='1996', company_type='GmbH（私有；CEO Andreas Bude）',
    sic=['LWL 光缆定制 / 网络布线（跳线 / 安装线）/ 有源无源组件 B2B 电商'],
    address='Provinzialstraße 40, 53859 Niederkassel', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['Andreas Bude — CEO / Geschäftsführer（wlw）', 'Holger Sockel — 域名方 Traffictime GmbH GF（非本户经营者）'], psc='未取', charges='', prev_names=[],
    lines=['**光缆电商顺带卖有源件** → 交换机只是配角 → **分销 20%，小户，一页纸**：STI-144GP / STI-288DGGPM（光口工业，配其 LWL 定制线）+ STC-228GP',
           '研究档无 KP；收件人 Andreas Bude（CEO）；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 12–14 CET'],
    notes='分销 20%；小户；一页纸；研究档补 KP Andreas Bude。')
put('SB-260', key='de', batch=B, name='HK GmbH（hk-systeme.de；Langenfeld）— 25 年以上的消防报警 / 语音疏散 / 电声报警系统集成商（HRB 105842 Düsseldorf；GF Dipl.-Ing. Johannes Brüls）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（HK GmbH；Albert-Einstein-Str. 5, 40764 Langenfeld；Tel 02173-39959310；Handelsregister Amtsgericht Düsseldorf HRB 105842；USt-ID DE236 356 997；Geschäftsführer Dipl. Ing. Johannes Brüls；dispo@ / buero@hk-systeme.de；「Seit über 25 Jahren … Brandmeldeanlagen, Sprachalarmierung oder Elektroakustische Alarmanlagen」）+ registercheck（HK GmbH, Langenfeld；同址同邮）；Paderborn 的 HKS Systeme GmbH（HRB 571828）与 HK.SYSTEMS AG 为同名他户，不采',
    url='https://hk-systeme.de/de/pages/impressum',
    number='HRB 105842（Amtsgericht Düsseldorf）· USt-ID DE236356997', status='Aktiv', incorporated='未取（经营 25 年以上）', company_type='GmbH（私有）',
    sic=['消防报警（BMA）、语音报警（SAA）、电声报警系统（ENS）设计安装维保 —— 弱电集成商'],
    address='Albert-Einstein-Str. 5, 40764 Langenfeld', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['Johannes Brüls（Dipl.-Ing.）— Geschäftsführer', 'Lukas Gierlirg — 研究档 KP lg@（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**消防 / 语音疏散集成商** → IP 广播 / 语音报警网络要 PoE 交换机，但量小、认证重（EN 54 体系外设备仅作传输）→ **集成商 25%，小户，一页纸**：STC-228GP / STC-2224GP（给 IP 音频终端供电）',
           '研究档站点 http_error → 收件人 Lukas Gierlirg lg@（在 Impressum 域下，可信）；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 12–14 CET'],
    notes='集成商 25%；小户；一页纸。')
put('SB-488', key='de', batch=B, name='OctoGate IT Security Systems GmbH（octogate.de / schulfirewall.de / kitawall.de；Paderborn）— 2010 年起的防火墙 / 校园网络安全设备厂商（HRB 9944 Paderborn；GF Frank Menne；11–50 人；源自 2001 年 HSM-Menne 的 OctoGate 防火墙；表内「FS.com 买家，着重跟」）', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（OctoGate IT Security Systems GmbH；Friedrich-List-Str. 87（旧 42）, 33100 Paderborn；+49 5251 18040-0；Vertretungsberechtigter Geschäftsführer Frank Menne；Amtsgericht Paderborn HRB 9944；USt-ID DE 275 066 387）+ Northdata（HRB 9944；EUID DER2809.HRB9944；MD Frank Menne, Jürgen Weiß；资本 €25,000；2010-11-23 登记；商标 OctoGate）+ Implisense（成立 2010-10-07；€25,000）+ LinkedIn（11–50 人；2010；IT Security / Firewall / IT Infrastruktur / WLAN / Digitalisierung）+ Regio Manager（源自 HSM-Menne GmbH / HSM IT-Services；2001 首台 OctoGate 防火墙；面向 KMU 与学校）+ 官网 Über uns（2010 从 HSM 拆分成立）',
    url='https://www.northdata.com/OctoGate%20IT%20Security%20Systems%20GmbH,%20Paderborn/HRB%209944',
    number='HRB 9944（Amtsgericht Paderborn）· USt-ID DE275066387', status='Aktiv（2026-08 站点更新）', incorporated='2010-10-07（登记 2010-11-19）', company_type='GmbH（资本 €25,000；私有；GF Frank Menne）',
    sic=['IT 安全设备制造 / 软件开发：OctoGate 防火墙、Schulfirewall（学校）、Kitawall（幼儿园）、WLAN、云管理；通过系统集成商与教育机构交付'],
    address='Friedrich-List-Str. 87, 33100 Paderborn', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Frank Menne — Geschäftsführer（创办人系；= 研究档 KP 本人）', 'Jürgen Weiß — 曾任 MD（Northdata）'], psc='Frank Menne（推定）', charges='', prev_names=[],
    lines=['**自有硬件品牌（OctoGate 防火墙 / 学校整包）+ 已从华南（FS.com）直采交换机 + GF 本人在收件 → 贴标 OEM 30% 目标**：OctoGate 标 STC-228GP / STC-2224GP / STC-4424GCPM（学校 PoE 接入，配其防火墙整包）+ STC-110XGE（10G 上联）；B BIG，**加厚**（贴标流程 + 三档价 + 学校场景一页纸）',
           '表内「着重跟」且 1 次跟进无回复 → 第二次触达换主题「PoE access switches to ship with Schulfirewall — your label」；发信窗口 Thu 12–14 CET；升 A 候选（回信即 A）'],
    notes='贴标 OEM 30% 目标；KP = GF 本人；B BIG；加厚；升 A 候选。')

# ---------------- GB 4 ----------------
put('SB-1123', key='gb', batch=B, name='CONNECTEC LIMITED（connectec.uk；Wrexham）— 2017 年起的消防 / 安防 / 网络 / 电气全国分销商；**PLANET 授权分销商** + Ruijie + Ajax；11 人；母公司 Dynamic Technology Solutions Ltd（100%）；董事 Tao Wei', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 10933159（CONNECTEC LIMITED；Active；Private limited；2017-08-25 成立；注册地 2026-07-30 起 Unit 4 Wrexham Midpoint, Dolydd Road, Wrexham LL13 7AJ（前 Unit B Wrexham Technology Park, Croesnewydd Road LL13 7YP）；AP01 Tao Wei 董事 2025-11-25；TM01 Ning Yu 2025-11-28 离任、Nathanael Tristan Owen 2025-06-12 离任；CS01 2026-02-17）+ companiesintheuk（11 名员工 2024 账；资本 £100；Total Exemption Full）+ Pomanda（SIC 47910；最大股东 Dynamic Technology Solutions Ltd 100%）+ 官网 brands/planet（「authorised Planet distributor」；公司号 10933159；VAT GB277433186；D-U-N-S 223187960；trade accounts）+ Business Wales / LinkedIn（Paul Jarvis — Managing Director）',
    url='https://find-and-update.company-information.service.gov.uk/company/10933159',
    number='Companies House 10933159 · VAT GB277433186 · D-U-N-S 223187960', status='Active（CS01 2026-02-17；AD01 2026-07-30）', incorporated='2017-08-25', company_type='Private limited company（资本 £100；100% Dynamic Technology Solutions Ltd）',
    sic=['47910 — 邮购 / 互联网零售（实为消防、安防、网络、电气、TV & 卫星安装件的全国 B2B 分销）'],
    address='Unit 4 Wrexham Midpoint, Dolydd Road, Wrexham LL13 7AJ', accounts='Total Exemption Full（小型；2024 账 11 人）', accounts_due='—', size_band='小型（11 人）',
    officers=['Tao Wei — Director（2025-11-25 起；36 岁；PSC）', 'Paul Jarvis — Managing Director（LinkedIn / Business Wales；非登记董事）', 'Ning Yu — 董事 2025-06 → 2025-11（已离任）', 'Nathanael Tristan Owen — 董事（2025-06 离任）'], psc='Tao Wei（Endole）；股东 Dynamic Technology Solutions Ltd 100%', charges='', prev_names=[],
    lines=['**PLANET 授权分销商 + Ruijie 在售 + 2025 下半年董事全换（Tao Wei / Ning Yu）→ 正是「换货源窗口」→ 分销 20% 首选 GB**：STC-228GP / STC-2216GP / STC-2224GP（对标其 PLANET 非网管 / 网管 PoE 在售价）+ STI-144GP（工业）；B BIG，**加厚**（对标价表 + 库存 / 交期说明），升 A 候选（回信即 A）',
           '收件人：研究档无 KP → sales@ 主送 + 点名 Paul Jarvis（MD）；董事为华人姓名 → **可选中文直联（默认仍英文，与 Vidos 同规则，Simon 定）**；表内无跟进 → 首信即一页纸；发信窗口 Thu 12–14 GMT'],
    notes='分销 20% 首选 GB；B BIG；加厚；升 A 候选；可选中文直联（Simon 定）。')
put('SB-531', key='gb', batch=B, name='Dynamode（dynamode.co.uk；英国）— 自有品牌网络 / 电脑配件品牌商（研究档：own brand；Elsa 已 1:1 去信 sales@）；**本轮 1 次检索未命中登记主体 → 未坐实**', iso='GB', fetched=F,
    source='GB · 1 次检索（Companies House 关键词「Dynamode UK Ltd」）→ 仅返回 DYNOMAP UK LTD 12733659 等无关同音户，**未命中**；按「1 次未中即停」规则不再追；站点事实沿用研究档（dynamode.co.uk，自有品牌，sales@）',
    url='https://www.dynamode.co.uk/',
    number='未坐实（登记主体 / 公司号未取）', status='站点在线（研究档快照 ok）', incorporated='未取', company_type='未取（自有品牌商，推定 Ltd）',
    sic=['自有品牌网络 / 电脑配件（交换机、网卡、机箱电源等）—— 经英国 IT 分销渠道出货'],
    address='英国（门牌未取）', accounts='—', accounts_due='—', size_band='未取',
    officers=['无（研究档无 KP；Elsa 1:1 去信 sales@）'], psc='未取', charges='', prev_names=[],
    lines=['**自有品牌 = 天然贴标对象（OEM 30% 目标）但主体未坐实** → 下轮补项：Companies House 关键词「Dynamode」/「Dynamode Ltd」+ 站点 Terms 页法人名；坐实前只发一页纸（STC-028GP / STC-228GP / STC-2224GP 贴标）不加厚',
           '收件人 sales@（研究档）；表内 Elsa 1 次去信无回复 → 第二次触达换主题「your-label PoE switches, MOQ 1」；发信窗口 Thu 12–14 GMT'],
    notes='未坐实（1 次未中）；OEM 30% 目标待坐实；下轮补项。')
put('SB-379', key='gb', batch=B, name='TRK SOLUTIONS LTD（trksolutions.co.uk；London Park Royal）— 2020 年成立的 CCTV / 门禁 / 报警安装微型公司（Companies House 12948953；唯一董事 + PSC Sahil Karwar；<10 人）', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 12948953（TRK SOLUTIONS LTD；Active；2020-10-14 成立；Premier Business Centre, 47-49 Park Royal Road, London NW10 7LQ；SIC 43210 电气安装 + 61100 有线电信）+ Endole（<10 人；资产负债表 <£500k；唯一董事 / 股东 / PSC Sahil Karwar，42 岁，2020-10 任；「High debt ratio」）+ bizstats（PSC 75–100%）+ companieslist（SAHIL KARWAR 董事）+ 官网（公司号 12948953；VAT 437821090；info@；0208 146 1234）+ LinkedIn（Sahil Karwar — TRK SOLUTIONS LTD）；TRK SOLUTIONS LIMITED 07147856（Knight 夫妇）为同名他户，不采',
    url='https://find-and-update.company-information.service.gov.uk/company/12948953',
    number='Companies House 12948953 · VAT 437821090', status='Active（最近账 2023-10-31）', incorporated='2020-10-14', company_type='Private limited company（单董事；注册地为商务中心）',
    sic=['43210 — 电气安装', '61100 — 有线电信（CCTV / 门禁 / 报警 / 网络安装）'],
    address='Premier Business Centre, 47-49 Park Royal Road, London NW10 7LQ（商务中心）', accounts='Micro（<£500k）', accounts_due='—', size_band='微型（<10 人）',
    officers=['Sahil Karwar — Director / PSC 75–100%（研究档写 Karwat → 更正为 Karwar）'], psc='Sahil Karwar', charges='', prev_names=[],
    lines=['**微型安装商，老板本人收件** → **集成商 25%，小户，一页纸**：STC-028GP / STC-228GP（CCTV 4–8 路）+ STC-2224GP（门禁 + 摄像机项目）；MOQ 1 + 伦敦 DAP 运费说明',
           '表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 12–14 GMT；研究档 KP 拼写更正 Karwat → Karwar'],
    notes='集成商 25%；小户；一页纸；KP 拼写更正。')
put('SB-521', key='gb', batch=B, name='Aerials & Cable Equipment Ltd（商号 ACE Distributors；aceonline.co.uk；Cheltenham）— 1983 年起天线 / 卫星 / CCTV / 光纤 / UniFi / 音响全国分销商（11–50 人；自有车队）；**研究档 KP Shaun Guard 实为客户 Oxford Aerials Ltd（Wallingford 安装商）业主 → 误归属**', iso='GB', fetched=F,
    source='GB · 1 次检索：官网（ACE Distributors Ltd；「Aerials & Cable Equipment Ltd have been supplying the UK Aerial & Satellite industries with quality components since 1983」；Surveillance / Audio / Cables / CCTV / Installation Equipment；trade pricing login）+ LinkedIn（Aerials & Cable Equipment Ltd；Cheltenham；11–50 人；1983；01242 511511；sales@aceonline.co.uk；CCTV / Solar PV / HDMI / AV 分部；自有车队全国配送）+ X（Unifi / Sky / Sonos / Fibre）+ oxfordaerials.co.uk（「Shaun Guard is the owner and original installer of Oxford Aerials … Wallingford」；Oxford Aerials Ltd, Wyndham House, Lester Way, Wallingford OX10 9TD）；**Companies House 号未取**（1 次检索；同名 ACE LTD 06137240 / ACE TV & AERIAL INSTALLATIONS LTD 08500547 不采）',
    url='https://www.linkedin.com/company/aerials-&-cable-equipment-ltd',
    number='部分坐实（法人名 Aerials & Cable Equipment Ltd；公司号未取）', status='Active（站点 + LinkedIn 在线）', incorporated='1983', company_type='Private limited company（私有）',
    sic=['天线 / 卫星 / IRS 分配、CCTV、光纤、UniFi 网络、HDMI 分配、音响、专用线缆 —— 面向安装商的全国 B2B 分销'],
    address='Cheltenham, Gloucestershire（门牌未取）', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['无登记董事信息（公司号未取）', 'Shaun Guard — Oxford Aerials Ltd 业主（研究档 KP shaun@oxfordaerials.co.uk）= **误归属，非 ACE 人员**'], psc='未取', charges='', prev_names=[],
    lines=['**两户混在一行**：域名 = ACE（全国安装商分销，卖 UniFi / CCTV → PoE 交换机正对口）→ **分销 20%**，收件人 sales@aceonline.co.uk（点名 purchasing / CCTV & networking buyer）；Shaun Guard = Oxford Aerials（微型安装商）→ 另线 **集成商 25% 一页纸**（shaun@ 可直发）',
           '下轮补项：Companies House 关键词「Aerials & Cable Equipment」取公司号 + 董事；表内 1 次跟进（发给 Shaun）无回复 → ACE 一线为首信；发信窗口 Thu 12–14 GMT'],
    notes='分销 20%（ACE）+ 集成商 25%（Oxford Aerials 另线）；KP 误归属已标；公司号下轮补。')

# ---------------- PL 4 ----------------
put('SB-1047', key='pl', batch=B, name='KAMSYS Piotr Błoński（kamsys.pl；Legionowo）— 2010 年起的监控 / 报警 / 门禁 / 对讲网店兼安装商（CEIDG 个体；持 MSWiA 安防许可；零售 + 批发）', iso='PL', fetched=F,
    source='PL · 1 次检索：GoWork / krs-online（KAMSYS PIOTR BŁOŃSKI；NIP 8231551721；REGON 142179316；Indywidualna działalność gospodarcza；开业 2010-01-14；ul. Wileńska 27, 05-120 Legionowo）+ 官网 Kontakt / O firmie（同 NIP / REGON；+48 22 774 07 86；CCTV / SSWiN / SKD / RCP / 对讲 / 自动门；「Sprzedaż detaliczna i hurtowa」；MSWiA 许可）+ Marketplanet（Network infrastructure devices / Telecommunications equipment 品类）',
    url='https://www.gowork.pl/kamsys-piotr-blonski,22633776/dane-kontaktowe-firmy',
    number='NIP 8231551721 · REGON 142179316（CEIDG）', status='Active（站点在线；VAT 在册）', incorporated='2010-01-14', company_type='Jednoosobowa działalność gospodarcza（个体）',
    sic=['安防系统（CCTV / 报警 / 门禁 / 考勤 / 对讲）网店 + 设计安装 + 批发；蓄电池 / 电工配件'],
    address='ul. Wileńska 27, 05-120 Legionowo（mazowieckie）', accounts='—', accounts_due='—', size_band='微型（个体）',
    officers=['Piotr Błoński — 业主（CEIDG）= 收件人（研究档无 KP）'], psc='Piotr Błoński', charges='', prev_names=[],
    lines=['**个体安防网店 + 安装** → **集成商 25%，小户，一页纸**：STC-028GP / STC-228GP（IP 监控 4–8 路）；MOQ 1 + DAP 华沙运费',
           '收件人 Piotr Błoński（业主）；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 12–14 CET'],
    notes='集成商 25%；小户；一页纸；研究档补 KP Piotr Błoński。')
put('SB-1124', key='pl', batch=B, name='FONEX K.T.M. Borowscy Sp. j.（fonex.pl / fonex.com.pl；Częstochowa）— 2008 年起的报警 / 监控 / 安防批发商 + 网店 + 安装（KRS 0000317918；Borowski 家族普通合伙；PKD 46.52 电子电信设备批发）', iso='PL', fetched=F,
    source='PL · 1 次检索：官网 Kontakt（FONEX K.T.M. Borowscy SP.J.；ul. Wręczycka 13/15, 42-202 Częstochowa；NIP 9492100567；KRS 0000317918；REGON 241058180；BDO 000427576；34 3 525 111；sklep@fonex.pl）+ krs-pobierz（Spółka jawna；aktywna；登记 2008-11-18；最近 KRS 变更 2026-04-17；主营 Sprzedaż hurtowa sprzętu elektronicznego i telekomunikacyjnego）+ rejestr.io / aleo（同号）+ fonex.com.pl（安装业务；info@fonex.pl）+ 规程 Regulamin（Sąd Rejonowy w Częstochowie XVII Wydział KRS）',
    url='https://rejestr.io/krs/317918',
    number='KRS 0000317918 · NIP 9492100567 · REGON 241058180 · BDO 000427576', status='Aktywna（KRS 变更 2026-04-17）', incorporated='2008-11-18', company_type='Spółka jawna（普通合伙；Borowscy）',
    sic=['PKD 46.52.Z — 电子 / 电信设备批发（报警 SATEL、CCTV、门禁、对讲；网店 + 安装）'],
    address='ul. Wręczycka 13/15, 42-202 Częstochowa（śląskie）', accounts='—', accounts_due='—', size_band='小型（人数未取；区域批发）',
    officers=['Borowscy（合伙人；姓名未取）= 收件人 sklep@ / info@（研究档无 KP）'], psc='Borowski 家族', charges='', prev_names=[],
    lines=['**区域安防批发 + 网店** → **分销 20%，小户，一页纸**：STC-028GP / STC-228GP / STC-2216GP（对标其在售 PoE 交换机价）',
           '收件人 sklep@fonex.pl（点名 właściciel / zakupy）；表内无跟进 → 首信即一页纸；发信窗口 Thu 12–14 CET'],
    notes='分销 20%；小户；一页纸。')
put('SB-547', key='pl', batch=B, name='NETINET Sp. z o.o.（netinet.pl；Warszawa）— 1999 年起（KRS 2002）的波兰 IT 分销商，Intellinet / Manhattan 品牌波兰运营方（前 IC Intracom Polska）；Prezes Marek Niewczas（= 研究档 KP「着重跟」）；资本 50,000 zł', iso='PL', fetched=F,
    source='PL · 1 次检索：rejestr.io（NETINET SPÓŁKA Z O.O.；KRS 0000096977；NIP 1181481416；Prezes Zarządu Marek Rafał Niewczas 自 2002-03-07；Członek Zarządu Agnieszka Maria Niewczas 自 2007-04-11；资本 50 tys. zł）+ krs-pobierz（REGON 016121659；ul. Arkuszowa 18, 01-934 Warszawa；登记 2002-03-07；最近变更 2026-07-16；主营电脑 / 外设 / 软件批发）+ bizraport（股东 Agnieszka Niewczas 65% 自 2017-01-20；Marek Niewczas 10%；prokurent Kamil Niewczas / Kazimierz Sojka；wspólnik Stefan Radzimiński）+ aleo（Marek Niewczas 54 岁）+ 官网 O firmie（「polskim dystrybutorem produktów IT działającym od ponad 30 lat」；IC Intracom Polska 项目结束后转为独立 Netinet，仍经波兰 IT 分销龙头承接 Intellinet / Manhattan 合同；全程包办测试 / 上市 / 营销 / 分销 / 保修）',
    url='https://rejestr.io/krs/96977/netinet',
    number='KRS 0000096977 · NIP 1181481416 · REGON 016121659', status='Aktywna（KRS 变更 2026-07-16）', incorporated='2002-03-07（经营自 1999）', company_type='Spółka z o.o.（资本 50,000 zł；Niewczas 家族控股）',
    sic=['PKD 46.51.Z — 电脑 / 外设 / 软件批发（Intellinet 网络 / Manhattan 配件品牌的波兰运营：测试、上市、营销、分销、保修）'],
    address='ul. Arkuszowa 18, 01-934 Warszawa', accounts='—', accounts_due='—', size_band='小型（人数未取；品牌运营型分销）',
    officers=['Marek Rafał Niewczas — Prezes Zarządu（自 2002；= 研究档 KP 本人）', 'Agnieszka Maria Niewczas — Członek Zarządu / 股东 65%', 'Kamil Niewczas / Kazimierz Sojka — prokurent'], psc='Agnieszka Niewczas 65% / Marek Niewczas 10%', charges='', prev_names=['（前身 IC Intracom Polska 项目）'],
    lines=['**品牌运营型分销（替品牌方做全套上市 / 保修）+ 老板本人收件** → 既可 **分销 20%**（Intellinet 之外补 Marvell 网管 PoE 线），也可谈 **自有标 OEM 30%**（Netinet 标 STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W）；B BIG，**加厚**，升 A 候选（回信即 A）',
           '表内「着重跟」1 次跟进无回复 → 第二次触达换主题「a managed PoE line beside Intellinet — your label or ours」；发信窗口 Thu 12–14 CET'],
    notes='分销 20% / 自有标 OEM 30%；KP = Prezes 本人；B BIG；加厚；升 A 候选。')
put('SB-454', key='pl', batch=B, name='Leoptics（leoptics.pl；Łódź）— 光模块 / CWDM / 网络交换机波兰网店（WordPress；SPEED-CWDM 系列资料 2017）；**CEIDG 命中「Leoptics Maja Matyjewicz」（Łódź，NIP 7251850432，2018 起）但与站点经营者的对应未另核 → 部分坐实**', iso='PL', fetched=F,
    source='PL · 1 次检索：OWG / CEIDG（Leoptics Maja Matyjewicz；NIP 7251850432；REGON 364507458；AKTYWNY；VAT czynny；自 2018-10-07；ul. Rewolucji 1905 r. 18/63, 90-207 Łódź）—— 同名命中但站点 Impressum 未取；Warszawa 的 TELEOPTICS Sp. z o.o.（KRS 0000165777，Fujikura 熔接机）为他户，不采；站点事实沿用研究档（leoptics.pl 「przełączniki sieciowe」品类、SPEED-CWDM 资料）',
    url='https://www.owg.pl/ceidg/leoptics_maja_matyjewicz_9,74,725185,7251850432',
    number='部分坐实（CEIDG NIP 7251850432 · REGON 364507458；经营者对应待核）', status='Active（CEIDG 在册；站点快照 ok）', incorporated='2018-10-07（CEIDG）', company_type='Jednoosobowa działalność gospodarcza（个体，推定）',
    sic=['光模块 / CWDM / DAC、网络交换机等光通信配件网店'],
    address='ul. Rewolucji 1905 r. 18/63, 90-207 Łódź（CEIDG）', accounts='—', accounts_due='—', size_band='微型（个体）',
    officers=['Maja Matyjewicz — 业主（CEIDG；对应待核）；研究档无 KP'], psc='Maja Matyjewicz（推定）', charges='', prev_names=[],
    lines=['**光模块网店（Saga 不做光模块）** → 只能切 10G 上联交换机 → **分销 20%，微型，一页纸**：STC-110XGE（$65）+ STC-228GP；表内「German brand link」未见证据 → 不采',
           '收件人：站点联系邮箱（研究档）；表内 1 次跟进无回复 → 第二次触达换主题；发信窗口 Thu 12–14 CET；下轮补项：站点 Regulamin 法人名'],
    notes='分销 20%；微型；一页纸；部分坐实（经营者待核）。')

print('b100 DE 4 + GB 4 + PL 4 written')
