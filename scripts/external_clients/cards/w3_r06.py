# -*- coding: utf-8 -*-
"""波 3 R06：XB 渠道型（主攻区：美/加/欧/土）168 户 —— 来源库多数没邮箱，本轮逐家网查补邮箱 + 核实身份，查到且对口的升 A 首触；巨头/不对口/重复/战区 → 不动或并线。
评估依据与来源写在 ev / notes。R06 第一批：德国工业/网络分销。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run, CONS, ATP

J = {}
def j(*a, **k): _j(J, *a, **k)
BIG = '大型广线/集团分销，决策链长 → B 慢慢跟进'
Q_IND = 'Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to the industrial brands you carry?'
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_D2S = 'Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?'

# ===== 德国：工业 / 网络分销（网查补邮箱）=====
j('XB-C1100', 'A', '首触', 'W51', '计算机/通信部件进口分销（ICO Innovative Computer GmbH，Diez；1991 起，约 120 人；2020 起 Antaira 分销，工业以太网交换机品类）', '进口商 + 工业交换机品类现成', 'DE 进口分销、工业线对口、邮箱已补 → 升 A 首触', kind='ind', to='vertrieb@ico.de',
  ev=[{'claim': '官网联系页 Vertrieb 邮箱 vertrieb@ico.de；1991 起分销与进口商；2020 起 Antaira 分销', 'quote': 'ICO übernimmt die Distribution der Antaira Technologies-Produkte', 'url': 'https://wileyindustrynews.com/de/news/ico-vertreibt-ab-sofort-produkte-von-antaira'}],
  q=Q_IND)
j('XB-C1068', 'A', '首触', 'W51', '网络/IT/TK 部件批发进口商（U.T.E. Electronic GmbH & Co. KG，Witten；1989 起，自有仓库；KVM/USV/PDU/PoE 交换机）', '进口批发，网络品类', 'DE 进口批发、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='info@ute.de',
  ev=[{'claim': '官网自述 1989 起 Großhändler, Distributor und Importeur von Netzwerkprodukten；info@ute.de', 'quote': 'seit 1989 tätiger Großhändler, Distributor und Importeur von hochwertigen und ausgewählten Netzwerkprodukten', 'url': 'https://www.ute.de/'}],
  q=Q_D2)
j('XB-C1119', 'B', '不动', typ='无线/IoT/天线分销（EBDS Wireless & Antennas，Montbonnot/Grenoble，法国；2013 起，10–19 人）', reason='主营无线路由/LoRaWAN/天线，交换机非其品类；国别修正 DE→FR；邮箱已补（info@ebds.eu），留 B 备用', iso='FR',
  ev=[{'claim': '官网页脚 info@ebds.eu；Grenoble；10–19 人', 'quote': 'EBDS distribue des solutions sans-fil et est expert des antennes', 'url': 'https://www.ebds.eu/'}])
j('XB-C0448', 'A', '首触', 'W51', '增值分销 VAD（Vitel GmbH，Unterschleißheim/München；2016 起；Peplink/Genetec DACH + Moxa 德国分销）', 'Moxa 分销 → 工业线第二供应商', 'DE VAD、Moxa 渠道、邮箱已补 → 升 A 首触', kind='ind', to='info@vitel.de',
  ev=[{'claim': '官网：Value-Added-Distributor für Peplink, Genetec und Moxa；info@vitel.de', 'quote': 'distributor and partner of Moxa in Germany', 'url': 'https://vitel.de/unternehmen/'}],
  q=Q_IND)
j('XB-C1046', 'A', '首触', 'W51', '工业自动化/工业以太网分销（HOPF Vertriebsgesellschaft mbH，Schwalbach am Taunus；1938 起；1997 起 Hirschmann 分销伙伴；B2B 网店）', '工业以太网品类现成', 'DE 工业分销、邮箱已补 → 升 A 首触', kind='ind', to='info@hopf-online.de',
  ev=[{'claim': 'wlw：1997 起 Hirschmann 分销伙伴；官网 info@hopf-online.de', 'quote': 'seit 1997 Distributionspartner von Hirschmann im Bereich Stecker und Industrial Ethernet', 'url': 'https://www.wlw.de/de/firma/hopf-vertriebsgesellschaft-1018642'}],
  q=Q_IND)
j('XB-C0565', 'A', '首触', 'W51', '商用 + 工业网络 VAD（YELLO Netcom GmbH，Rheine；Moxa 与 Hirschmann 分销，10,000+ SKU；工业销售总监 Marco Syma）', '工业网络 VAD，品类现成，KP 实名', 'DE 工业网络 VAD、KP 实名 → 升 A 首触（优先）', kind='ind', to='vertrieb.industrie@yello-net.de', lead='Hi Marco,',
  kp=[{'name': 'Marco Syma', 'role': 'Sales Director Industrie（vertrieb.industrie@yello-net.de）', 'source': 'https://www.yello-net.de/Unternehmen/Ueber%20uns/Standorte%20-%20Ansprechpartner'},
      {'name': 'Andreas Bartels', 'role': 'Senior Key Account Manager（andreas.bartels@yello-net.de）', 'source': 'https://www.yello-net.de/HirschmannBXPManagedSwitche'}],
  ev=[{'claim': '官网：Moxa und Hirschmann Distributor，Value Added Distributor für kommerzielle und industrielle Netzwerktechnik', 'quote': 'Wir sind Ihr führender Systemanbieter und Value Added Distributor für kommerzielle und industrielle Netzwerktechnik', 'url': 'https://www.yello-net.de/'}],
  q=Q_IND)

# ===== 德国：安防 / 网络分销 第二批（网查补邮箱）=====
j('XB-C0450', 'A', '首触', 'W51', '安防技术批发（SECPLAN Technik GmbH，Reichelsheim；1997 起；13–16 万件库存；DACH 配送；Ajax DACH 领先分销 + Teltonika 批发）', '安防批发，PoE 配套', 'DE 安防批发、邮箱已补 → 升 A 首触', kind='dist2', to='verkauf@secplan.de',
  ev=[{'claim': '官网联系页 Vertrieb 邮箱 verkauf@secplan.de；1997 起安防批发，130,000+ 件库存', 'quote': 'SECPLAN beliefert Errichter und Fachbetriebe seit 1997 mit professioneller Sicherheitstechnik', 'url': 'https://www.secplan.de/Service/Kontakt/'}],
  q=Q_D2S)
j('XB-C1038', 'C', '并线', typ='SECPLAN Teltonika 批发条目', reason='与 XB-C0450 SECPLAN 同一公司 → 并线，不单独跟')
j('XB-C1121', 'A', '首触', 'W51', '数据通信/工业通信分销（SPHINX Computer Vertriebs-GmbH，Laudenbach；Moxa/Advantech/Perle/ADDER 分销；总经理 Hubert Engelhardt）', 'Moxa 德国分销 → 工业线第二供应商', 'DE 工业通信分销、邮箱已补 → 升 A 首触；XC-C1461 为同一公司重复条目', kind='ind', to='mail@sphinxcomputer.de',
  kp=[{'name': 'Hubert Engelhardt', 'role': 'Geschäftsführer（hubert.engelhardt@sphinxcomputer.de，见 Gewerbeverein Laudenbach）', 'source': 'https://www.gv-l.de/mitglieder/'}],
  ev=[{'claim': 'Impressum 自述 Distributor für MOXA, Advantech, ADDER, Multitech, PERLE…；mail@sphinxcomputer.de', 'quote': 'Distributor für MOXA, Advantech, ADDER,Multitech, BARIX,Opengear,PERLE', 'url': 'https://www.sphinxcomputer.de/impressum.php'}],
  q=Q_IND)
j('XB-C0123', 'B', '不动', typ='电子元器件厂商代表（Axellence GmbH，Olching；2000 起；2–10 人；代理 Centec 芯片/白盒方案等）', reason='是厂商销售代表而非交换机分销商，不是采购方；记录 Centec 欧洲代表身份供内部参考；info@axellence.eu',
  ev=[{'claim': '官网产品页列 Centec 芯片与白盒；LinkedIn：manufacturer\u2019s representative，2–10 人', 'quote': 'Pan-European Manufacturer\u2019s Representation connecting innovative Suppliers to innovative Users', 'url': 'https://www.linkedin.com/company/axellence-gmbh'}])
j('XB-C0114', 'A', '首触', 'W02', 'PoE 专营分销（PoE Partner = viveroo GmbH 业务部，Salzkotten；2021 起；PoE Texas 欧洲官方分销；PoE 交换机/注入器网店 B2B）', 'PoE 专营，已有一条美系 PoE 线，可加第二条', 'DE PoE 专营分销、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='info@poe-partner.com',
  ev=[{'claim': '官网：offizieller PoE Texas Distributor für Europa；info@poe-partner.com', 'quote': 'PoE Partner ist Ihr Spezialist für Power over Ethernet und offizieller PoE Texas Distributor für Europa', 'url': 'https://www.poe-partner.com/de/ueber-uns/'}],
  q=Q_D2)
j('XB-C0221', 'C', '并线', typ='PoE Partner 教育方案条目', reason='与 XB-C0114 PoE Partner 同一公司 → 并线')
j('XB-C0375', 'C', '并线', typ='PoE Partner Texas Switch 条目', reason='与 XB-C0114 PoE Partner 同一公司 → 并线')
j('XB-C1051', 'A', '首触', 'W51', '安防批发分销（GRAEF Distribution GmbH，Berlin；Ajax/Paxton/Teltonika/Carrier/TP-Link 网络品类；B2B 网店）', '安防批发 + 已卖网络品类', 'DE 安防批发、邮箱已补 → 升 A 首触', kind='dist2', to='distribution@graef-gruppe.de',
  ev=[{'claim': '网店页眉 distribution@graef-gruppe.de；集团页自述 wholesaler and distributor for security technology', 'quote': 'GRAEF Distribution GmbH is a wholesaler and distributor for security technology', 'url': 'https://www.graef-gruppe.de/en/'}],
  q=Q_D2S)
j('XB-C0485', 'A', '首触', 'W51', '网络产品进口分销（KTI Distribution GmbH，Bielefeld；1996 起；台湾 KTI Networks 介质转换器/交换机/光模块德语区进口商；也做 OEM/ODM；总经理 Paul Peter Kaiser）', '直接从厂商进口交换机 → 对自有标签/第二来源有经验', 'DE 进口分销、邮箱已补 → 升 A 首触', kind='dist2', to='sales@kti.de',
  kp=[{'name': 'Paul Peter Kaiser', 'role': 'Geschäftsführer（PKaiser@kti.de，见官网 Datenschutz）', 'source': 'https://www.kti.de/datenschutz'}],
  ev=[{'claim': '官网：Wir importieren … direkt vom Hersteller Katron Technologies Inc. aus Taiwan；sales@kti.de', 'quote': 'Wir importieren qualitativ hochwertigen Ethernet-Produkte direkt vom Hersteller Katron Technologies Inc. aus Taiwan', 'url': 'https://kti.de/ueber-uns'}],
  q=Q_D2)
j('XB-C1049', 'A', '首触', 'W51', '视频安防分销（VIDEOR E. Hartig GmbH，Rödermark；1975 起；51–200 人；DACH 领先视频安防分销；自有品牌 eneo；Hanwha 分销；销售总监 Michael Schwamborn）', '有自有品牌 eneo → 自有标签 PoE 交换机正对口', 'DE 中大型安防分销、自有品牌、邮箱已补 → 升 A 首触（优先）', kind='dist2', to='sales@videor.com',
  kp=[{'name': 'Michael Schwamborn', 'role': 'Vertriebsleiter / Sales Director（官网联系页）', 'source': 'https://www.videor.com/de/kontakt'}],
  ev=[{'claim': 'Hanwha 分销商名录列 sales@videor.com；LinkedIn 51–200 人，1975 起；eneo 为其注册商标', 'quote': 'eneo ist eine eingetragene Marke der VIDEOR E. Hartig GmbH', 'url': 'https://eneo-security.com/de/impressum'}],
  q='Would a private-label PoE switch line be of interest alongside your own camera brand, and who on your product team should see samples?')
j('XB-C1036', 'A', '首触', 'W51', '安防经销/次级分销（ESA GmbH German Protect，Speyer；2023 起 Hikvision DACH Sub-Distributor；网店 + 安装）', 'Hikvision 次级分销，PoE 配套', 'DE 安防次级分销、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='info@germanprotect.com',
  ev=[{'claim': 'Hikvision 官方线上经销商名录列 info@germanprotect.com；自 2023-01-01 起 DACH Sub-Distributor', 'quote': 'Ab dem 01.01.2023 fungiert die ESA GmbH German Protect als Sub-Distributor innerhalb der DACH Länder für den Hersteller Hikvision', 'url': 'https://www.germanprotect.com/blog/hikvision-news-2023-german-protect-wird-sub-distributor'}],
  q=Q_D2S)
j('XB-C1071', 'B', '不动', typ='电子元器件专业批发（WERNER ELECTRONIC / Werner GmbH，Kreischa bei Dresden；1991 起；HARTING/Phoenix Contact/LAPP 分销）', reason='主营元器件/连接技术，交换机非其主线；邮箱 info@werner-electronic.de 已记，留 B',
  ev=[{'claim': 'Impressum：info@werner-electronic.de；Silicon Saxony 会员页自述元器件专业批发', 'quote': 'Spezial-Fachgroßhandel für elektronische Bauelemente', 'url': 'https://silicon-saxony.de/mitglieder/werner-gmbh/'}])
j('XB-C1057', 'A', '首触', 'W51', '安防分销（BKH Sicherheitstechnik GmbH & Co. KG，Ludwigshafen；AVS/CARDIN/SAFIRE SMART/Provision-ISR 分销；B2B 网店；总经理 Patrick Kane）', '视频安防分销，KP 实名公开', 'DE 安防分销、KP 实名 → 升 A 首触', kind='dist2', to='p.kane@bkh-security.de', lead='Hi Patrick,',
  kp=[{'name': 'Patrick Kane', 'role': 'Geschäftsführer（p.kane@bkh-security.de，官网联系页公开）', 'source': 'https://bkh-security.de/kontakt/'}],
  ev=[{'claim': '官网自述 Fachpartner und Großhändler；SAFIRE SMART 视频分销', 'quote': 'Distributor von SAFIRE SMART Videoüberwachung', 'url': 'https://safiresmart.de/'}],
  q=Q_D2S)
j('XB-C1083', 'B', '不动', typ='专业音视频分销（VIDELCO Europe GmbH，Ratingen；NETGEAR 分销；AV-over-IP）', reason='AV 分销，其交换机需求绑定 NETGEAR AV 系列；邮箱 info@videlco.eu 已记，留 B',
  ev=[{'claim': '官网：VIDELCO Europe ist Distributor für NETGEAR；info@videlco.eu', 'quote': 'VIDELCO Europe ist Distributor für NETGEAR', 'url': 'https://videlco.eu/netgear'}])
j('XB-C1122', 'A', '首触', 'W51', '工业 IoT 硬件分销（EasyNet Technologies UAB，维尔纽斯/伦敦；Milesight VAD 法德英；Queclink/Four-Faith/Wi-Tek；EU+UK 仓）', '已代理中国 PoE 交换机品牌（Wi-Tek），可加第二条', '国别修正 DE→LT；欧洲 IoT 分销、邮箱已补 → 升 A 首触', kind='dist2', to='info@easynt.com', iso='LT',
  ev=[{'claim': '官网：Milesight VAD for France, Germany, UK；名录自述 310+ devices from Milesight, Queclink, Four-Faith, Wi-Tek；info@easynt.com', 'quote': 'EasyNet Technologies is a European and UK industrial IoT hardware distributor, delivering 310+ certified devices from Milesight, Queclink, Four-Faith, Wi-Tek', 'url': 'https://easynt.com/about-us/contact-us/'}],
  q=Q_D2)
j('XB-C1050', 'A', '首触', 'W02', '视频安防增值分销（INKOVIDEO GmbH & Co. KG，Hilden；Foscam 德国官方分销；面向经销商/安装商）', '视频分销，PoE 配套', 'DE 视频分销、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='info@inkovideo.de',
  ev=[{'claim': '官网联系页 info@inkovideo.de；自述 Added-Value-Distribution für Fachhändler, Installateure', 'quote': 'Bei INKOVIDEO steht Added-Value-Distribution im Mittelpunkt', 'url': 'https://inkovideo.de/contact'}],
  q=Q_D2S)
j('XB-C1056', 'A', '首触', 'W02', '安防批发/网店（Gmyrek Elektronik GmbH / topsicherheit.de，Braunsbedra；1997 起；分销+进口+批发）', '安防批发，PoE 配套', 'DE 安防批发、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='info@topsicherheit.de',
  ev=[{'claim': 'Impressum info@topsicherheit.de；europages：Founded 1997, Distributor / Wholesaler', 'quote': 'Versandhandel … info@topsicherheit.de', 'url': 'https://www.topsicherheit.de/impressum.html'}],
  q=Q_D2S)
j('XB-C1070', 'B', '不动', typ='电子元器件分销（LGV Electronic Distribution und Vertriebs GmbH，Flörsheim；1952 起；连接器/焊接/ESD/标识）', reason='元器件线，无交换机品类；邮箱 info@lorenzgroup.com 已记，留 B',
  ev=[{'claim': '官网 info@lorenzgroup.com；wlw：Bauteile-Distributor', 'quote': 'ist Bauteile-Distributor und Beschaffungs- und Logistik-Dienstleister', 'url': 'https://www.wlw.de/de/firma/lgv-electronic-distribution-und-ver-576147'}])
j('XB-C1061', 'A', '首触', 'W51', '对讲/安防分销（Keil Telecom Vertriebs GmbH & Co KG，Leipzig；2006 起 2N 德国分销；2024 起 AXIS、SIEZA；供货批发/集成商；总经理 Thomas Beer）', '2N IP 对讲 + Axis 摄像机 → PoE 交换机配套', 'DE 专业分销、邮箱已补 → 升 A 首触', kind='dist2', to='info@keil-telecom.de',
  kp=[{'name': 'Thomas Beer', 'role': 'Geschäftsführer（XING）', 'source': 'https://www.xing.com/pages/keiltelecomvertriebsgmbh-co-kg'}],
  ev=[{'claim': '官网：Seit 2006 offizieller 2N Distributor…Mit AXIS und SIEZA seit 2024；info@keil-telecom.de', 'quote': 'liefert 2N Produkte in Deutschland an den Großhandel, Systemintegratoren und Vertriebspartner', 'url': 'https://www.keil-telecom.de/'}],
  q=Q_D2S)
j('XB-C1118', 'A', '首触', 'W51', '视频安防分销（ARGUS Sicherheitssysteme GmbH，Gröbenzell/München；Milestone/Milesight/BAROX 分销；2–10 人）', '已卖视频专用 PoE 交换机品牌 → 可加低价第二线', 'DE 视频分销、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='info@argus.eu',
  ev=[{'claim': '官网：Distributor für Milestone, Milesight und BAROX；Distribution: info@argus.eu', 'quote': 'offizieller Milestone, Milesight und BAROX Distributor', 'url': 'https://www.argus.eu/en/about-us'}],
  q=Q_D2S)
j('XB-C1054', 'A', '首触', 'W51', '安防服务商 + 分销（Hörmann Berlin-Brandenburg GmbH，Blankenfelde；2020 起 Crow/Tiandy/PIMA 德语区独家分销；网店）', 'Tiandy 视频独家分销，PoE 配套', 'DE 安防分销、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='info@hoermannberlin.de',
  ev=[{'claim': '官网：Seit 2020 exklusiver Distributor der Markenhersteller Crow, Tiandy und PIMA；info@hoermannberlin.de', 'quote': 'exklusiver Distributor der Qualitätsmarken Crow, Tiandy und PIMA im deutschsprachigen Raum', 'url': 'https://www.hoermannberlin.de/'}],
  q=Q_D2S)
# 德国：未补到邮箱 / 巨头 / 重复 / 不对口
for c, t, why in [
    ('XB-C0159', '电子元器件分销（Atlantik Elektronik，Lantronix PoE 分销）', '大型元器件分销，决策链长，邮箱待补 → B 不动'),
    ('XB-C0181', 'Cambium VAD（4Networks，S 箱 10-06 已去信 info@ 未回）', '已去一信未回，先不加第二封；下一轮再评'),
    ('XB-C0363', 'erdkreis VIDEO GmbH（40 年，Hikvision 伙伴）', '邮箱待补（下一轮网查）→ B 不动；XB-C1096 为同一公司'),
    ('XB-C1048', 'Börsig GmbH（1969 起电子分销，Phoenix）', '元器件线，邮箱待补 → B 不动'),
    ('XB-C1062', 'ModiTech Service GmbH / Digital Key World（2N/SimonsVoss/SALTO）', '门禁服务商为主，邮箱待补 → B 不动'),
    ('XB-C1077', 'IT made in Germany / Brauns IT（Teltonika/Ubiquiti）', '小型 IT 商，邮箱待补 → B 不动'),
    ('XB-C1078', 'macle-shop / LANCOM Distributor', '同行品牌专营网店 → B 不动'),
    ('XB-C1079', 'Dallmeier Components GmbH（DACH 视频安防分销）', '邮箱待补（下一轮网查）→ B 不动'),
    ('XB-C1103', 'SCALCOM GmbH（HPE Aruba/Cisco/Meraki 分销）', '大牌企业网 VAD，与 Saga 定位不符 → B 不动'),
    ('XB-C1110', 'H&D Automatisierung GmbH（Siemens SCALANCE）', '西门子体系集成/分销 → B 不动'),
    ('XB-C1115', 'Wortmann AG（全线 IT 分销，331 款交换机在售）', BIG + '；邮箱待补'),
    ('XB-C1116', 'Siewert & Kau（全线 IT 分销）', BIG),
    ('XB-C1117', 'Systeam AG（专业 IT 分销）', BIG),
    ('XB-C1125', 'MR Datentechnik（IT 零售/分销，多品牌 PoE）', '零售为主，邮箱待补 → B 不动'),
    ('XB-C1126', 'API Computerhandels GmbH（全线 IT 分销）', BIG),
    ('XB-C1130', 'Inter-Tech Elektronik Handels GmbH（机箱/配件分销+制造）', 'PC 配件线，交换机非主营 → B 不动'),
    ('XB-C1150', 'ADI Global Germany', BIG + '（ADI 全球体系）'),
    ('XB-C1151', 'HON Security and Fire Distribution GmbH', '安防/消防分销，邮箱待补（XC-C1467 为同一公司）→ B 不动'),
]:
    j(c, 'B', '不动', typ=t, reason=why)
for c, t, why in [
    ('XB-C1096', 'erdkreis CCTV/IP-VIDEO GmbH', '与 XB-C0363 同一公司 → 并线'),
    ('XB-C1124', '「Wortmann（#502）是最佳目标」分析行', '非客户记录，与 XB-C1115 并线'),
    ('XB-C1145', 'ELBEX Deutschland (#516)', '与 XA-C0027 ELBEX 同一公司（已研究，破产整理中 → 不动）→ 并线'),
    ('XB-C1146', 'Bytec (#530)', '与 XA-C0028 Bytec 同一公司 → 并线'),
    ('XB-C1047', 'Teltonika Germany GmbH（厂商子公司）', '厂商自身，不是采购方 → C'),
    ('XB-C1084', 'FS Deutschland (FS.com)', '同行自有品牌厂商直销 → C'),
]:
    j(c, 'C', '并线' if '并线' in why else '不动', typ=t, reason=why)

# ===== 法国：网络 / 安防分销（网查补邮箱）=====
j('XB-C0900', 'A', '首触', 'W51', '增值分销（ES France – Equipements Scientifiques，Garches；1963 起；ISO 9001；元器件/仪器/工业计算/通信网络四大块；Connect Tech 等工业以太网交换机品类）', '工业网络品类现成', 'FR 工业 VAD、邮箱已补 → 升 A 首触', kind='ind', to='contact@es-france.com',
  ev=[{'claim': '官网自述 distributeur à forte valeur ajoutée depuis 1963，四大领域含 réseaux de communication；contact@es-france.com（Réseau Mesure 会员页）', 'quote': 'spécialisé dans la distribution dans quatre grands domaines : composants, instrumentation, informatique et réseaux', 'url': 'https://www.es-france.com/'}],
  q=Q_IND)
j('XB-C0919', 'A', '首触', 'W51', '电子/工业计算分销集团（Syscom-Prorep，Lisses；1983 起；85 人、约 €60M；法/意/比/荷；工业 PC、无线模块、视频流传输方案）', '工业客户群 + 视频传输品类，DIN 导轨 PoE 可补位', 'FR 工业分销、邮箱已补 → 升 A 首触（轻）', kind='ind', to='contact@syscom-prorep.com',
  ev=[{'claim': '官网联系页 contact@syscom-prorep.com；Siparex：85 collaborateurs，CA proforma ≈ 60 M€', 'quote': 'le groupe compte 85 collaborateurs, un portefeuille de plus de 1 000 clients et réalise un chiffre d\u2019affaires proforma d\u2019environ 60 M€', 'url': 'https://www.siparex.com/syscom-prorep-poursuit-sa-strategie-de-croissance-externe/'}],
  q=Q_IND)
j('XB-C0898', 'A', '首触', 'W51', 'B2B 网络设备分销（Matériel Réseau / ASC Computeur，Caudry；8,851 SKU、100+ 品牌；交换机/PoE/视频监控 IP/UPS）', '品类直接对口（交换机 + PoE）', 'FR 网络分销、邮箱已补 → 升 A 首触', kind='dist2', to='contact@asccomputer.fr',
  ev=[{'claim': '官网页脚 contact@asccomputer.fr；8 851 références actives，100+ marques', 'quote': 'Distributeur B2B de matériel réseau pour les pros et collectivités, partout en France. Opéré par ASC Computeur.', 'url': 'https://materiel-reseau.fr/'}],
  q=Q_D2)
j('XB-C0920', 'A', '首触', 'W02', 'IT B2B 批发（Picata，Bordeaux；2011 起；7,000+ SKU；10,000 m² 仓）', 'IT 批发，面向经销商', 'FR IT 批发、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='commercial@picata.fr',
  ev=[{'claim': '官网首页 Service commercial commercial@picata.fr', 'quote': 'Grossiste & fournisseur informatique B2B pour revendeurs', 'url': 'https://www.picata.fr/'}],
  q=Q_D2)
j('XB-C0882', 'A', '首触', 'W51', 'IP 视频安防专业分销（Noemis，Clermont-Ferrand；2005 起；49 人（35 法 + 14 迪拜）；法国 IP 视频分销第一；Milestone/Hanwha/Eagle Eye）', 'IP 视频分销龙头，PoE 配套量大', 'FR IP 视频分销、邮箱已补 → 升 A 首触（优先）', kind='dist2', to='commercial@noemis.fr',
  kp=[{'name': 'Guillaume Poughon', 'role': 'Fondateur / co-dirigeant', 'source': 'https://www.lecourrierdesentreprises.fr/noemis-le-groupe-clermontois-de-la-videosurveillance-ip-veut-setendre-a-linternational/'}],
  ev=[{'claim': 'Hanwha 落地页页脚 commercial@noemis.fr；EEN 公告：49 employees，national leader in distribution of IP video', 'quote': 'Noemis is the national leader in the distribution of IP video surveillance solutions', 'url': 'https://www.een.com/blog/eagle-eye-networks-announces-distribution-partnership-with-noemis-in-france/'}],
  q=Q_D2S)
j('XB-C0886', 'A', '首触', 'W51', 'IP 安防分销/经销（W3CAM SAS，Lorient；20 年+；Axis/Hikvision/Dahua/Ajax/Hanwha/Bosch/Milestone/2N）', '多品牌视频分销，PoE 配套', 'FR 视频分销、邮箱已补 → 升 A 首触（轻）', kind='dist2', to='contact@w3cam.fr',
  ev=[{'claim': '官网联系页 contact@w3cam.fr；自述 distributeur français spécialisé…depuis plus de 20 ans', 'quote': 'Distributeur français spécialisé en systèmes de vidéosurveillance IP, alarmes anti-intrusion et contrôle d\u2019accès depuis plus de 20 ans', 'url': 'https://www.w3cam.fr/content/6-formulaire-de-contact'}],
  q=Q_D2S)
j('XB-C0880', 'A', '首触', 'W51', '安防进口分销（Tevah Systèmes，Gennevilliers；2004 起；125 人；进口商+分销+集成；Dahua/Hikvision 为主；销售总监 Romain Mallay）', '自己做进口 → 对直接从中国采购交换机有经验', 'FR 进口分销、KP 实名 → 升 A 首触（优先）', kind='dist2', to='romain.m@tevah.fr', lead='Hi Romain,',
  kp=[{'name': 'Romain Mallay', 'role': 'Directeur Commercial（romain.m@tevah.fr，GPMSE 合作伙伴页公开）', 'source': 'https://www.gpmse.com/partenaires-assemblee-generale/'}],
  ev=[{'claim': '官网：Depuis 2004…importation, intégration et distribution；équipe de plus de 125 personnes；adv@tevah.fr', 'quote': 'spécialisé dans l\u2019importation, l\u2019intégration et la distribution de solutions de sécurité innovantes', 'url': 'https://www.tevah.fr/qui-sommes-nous'}],
  q=Q_D2S)
j('XB-C0884', 'A', '首触', 'W51', '安防电子全国分销（Accédia Distribution，Nanterre；10–15 家分部；Ajax 法国官方分销；Groupe Accédia）', '全国分销网，PoE 配套', 'FR 安防分销、邮箱已补 → 升 A 首触', kind='dist2', to='contact@accedia.net',
  ev=[{'claim': '集团法务页 contact@accedia.net；Ajax 公告：leading security solutions distributor in France，10 agencies', 'quote': 'ACCÉDIA DISTRIBUTION was born from the merger of the SEPTAM, TSF, GCAS, AVDM and ESDAS SERIÉ brands to form a network of 10 agencies in France', 'url': 'https://ajax.systems/blog/accedia-new-official-distributor-france/'}],
  q=Q_D2S)
j('XB-C0888', 'A', '首触', 'W02', '安防分销/网店（TSA Distribution，Schiltigheim；Hikvision/Ajax/Dahua/UTEPO；小型）', '小型安防分销，已卖 UTEPO PoE 交换机', 'FR 小型安防分销、邮箱已补 → 升 A 首触（轻，排 2027-W02）', kind='dist2', to='contact@tsa-distribution.com',
  ev=[{'claim': '官网各页 contact@tsa-distribution.com', 'quote': 'TSA Distribution 52 route de Bischwiller 67300 SCHILTIGHEIM', 'url': 'https://tsa-distribution.com/en/products/ajax-3'}],
  q=Q_D2S)
j('XB-C0914', 'A', '首触', 'W51', '工业 IT 增值分销（ADM21，Colombes；1998 起；19 人；Moxa 分销 1998 起；Trendnet 法国独家；3onedata/WoMaster/ACTi；工业以太网专组邮箱）', '已代理两家中国工业交换机品牌 → 对中国工业线采购熟悉', 'FR 工业网络 VAD、邮箱已补 → 升 A 首触（优先）', kind='ind', to='industrialnetworking@adm21.fr',
  ev=[{'claim': '官网「Où nous trouver」列 Ethernet Industriel et Plateforme IIOT : industrialnetworking@adm21.fr；品牌页列 3ONEDATA/WOMASTER/MOXA/TRENDNET', 'quote': 'Ethernet Industriel et Plateforme IIOT : industrialnetworking@adm21.fr', 'url': 'https://www.adm21.fr/ou-nous-trouver'}],
  q=Q_IND)
j('XB-C0917', 'A', '首触', 'W51', '网络连接件制造/进口/批发（Neklan，Lisses；2008 起；Telenco 集团；3,000 客户含批发商/经销商/安装商；有「équipements actifs」品类）', '进口商 + 自有品牌 → 自有标签交换机对口', 'FR 进口批发、邮箱已补 → 升 A 首触', kind='dist2', to='contact@neklan.fr',
  ev=[{'claim': '官网：Fabricant, Importateur, Grosseiste；contact@neklan.fr；LinkedIn 3000 clients', 'quote': 'Fabricant, Importateur, Grossiste Spécialisé en connectique & accessoires informatiques', 'url': 'https://www.neklan.fr/'}],
  q=Q_D2)
j('XB-C0885', 'A', '首触', 'W51', '弱电/安防分销（GDV，Croissy-Beaubourg；1981 起；10–15 家分部，50–155 人；Dahua + Ajax 法国官方分销；业务发展负责人 Gilbert Ecunha）', '全国弱电分销，PoE 配套', 'FR 弱电分销、KP 实名 → 升 A 首触', kind='dist2', to='g.ecunha@gdv.fr', lead='Hi Gilbert,',
  kp=[{'name': 'Gilbert Ecunha', 'role': 'Responsable développement（g.ecunha@gdv.fr，GPMSE 合作伙伴页公开）', 'source': 'https://www.gpmse.com/partenaires-assemblee-generale/'}],
  ev=[{'claim': 'Dahua 法国分销商页列 contact@gdv.fr；LinkedIn 51–200 人', 'quote': 'Depuis 1981, GDV s\u2019est imposé comme un acteur majeur dans la distribution courant faible', 'url': 'https://france.dahuatech.com/ReseauxDistributeurs'}],
  q=Q_D2S)
j('XB-C0877', 'A', '首触', 'W51', '安防电子独立分销第一（ITESA-VEDITEC，Marseille；1978 起；155 人、15 家分部；175 家供应商、6,000 SKU；仅售专业客户）', '品类广、供应商多 → 可纳入新 PoE 线', 'FR 安防分销龙头（中大型）、邮箱已补 → 升 A 首触', kind='dist2', to='contact@itesa.eu',
  ev=[{'claim': '官网首页 contact@itesa.eu；175 fournisseurs et fabricants，6000 références', 'quote': '175 fournisseurs et fabricants … Un stock de 6000 références produits', 'url': 'https://www.itesa-veditec.com/'}],
  q=Q_D2S)
j('XB-C0901', 'A', '首触', 'W02', '安防/通信系统分销（S2ES，Mérignac；1988 起；20–49 人；法国西南第一专业分销）', '区域安防分销，PoE 配套', 'FR 区域分销、邮箱已补 → 升 A 首触（轻，排 2027-W02）', kind='dist2', to='bienvenue@s2es.fr',
  ev=[{'claim': '官网页脚 bienvenue@s2es.fr；1988 起 distribution spécialisée', 'quote': 'Créée en 1988, S2ES est une société de distribution spécialisée en systèmes électroniques de sécurité et de communication', 'url': 'https://www.s2es.fr/'}],
  q=Q_D2S)
j('XB-C0890', 'A', '首触', 'W02', 'Dahua 官方分销（Onyx Vision；adv@onyx-vision.fr）', 'Dahua 分销，PoE 配套', 'FR 视频分销、邮箱（Dahua 分销名录）已补 → 升 A 首触（轻，排 2027-W02）', kind='dist2', to='adv@onyx-vision.fr',
  ev=[{'claim': 'Dahua 法国分销商页列 Onyx Vision adv@onyx-vision.fr', 'quote': 'Onyx Vision Tél:09 70 64 00 00 E-mail:adv@onyx-vision.fr', 'url': 'https://france.dahuatech.com/ReseauxDistributeurs'}],
  q=Q_D2S)
# 法国：巨头 / 并线 / 邮箱待补
for c, t, why in [
    ('XB-C0457', 'Azenn Connect（Azenn + Exertis Connect 2026 合并；300 人、30,000 SKU；Nexora 集团）', BIG + '；邮箱为表单/混淆'),
    ('XB-C0878', 'AASSET Security（TKH 集团）', BIG),
    ('XB-C0879', 'By Demes France（欧洲安防分销龙头；france@bydemes.com）', BIG + '；邮箱已记'),
    ('XB-C0896', 'Alliance-Com（法国电信/网络分销龙头）', BIG),
    ('XB-C0897', 'SQP（Lyon；1986 起；€30M+ VAD；仅表单，公开邮箱只有 software@/support@）', '对口但无销售邮箱 → B 不动，LinkedIn 补'),
    ('XB-C0892', 'ECLATS ANTIVOLS（自称法国第一安防分销）', '邮箱待补（下一轮网查）→ B 不动'),
    ('XB-C0894', 'France Alarme', '邮箱待补 → B 不动'),
    ('XB-C0902', 'Surexpert.pro（SSI Systèmes 的网店，2018 起，2–10 人）', '小型网店，与 XB-C0903 同一集团 → B 不动'),
    ('XB-C0903', 'SSI Systèmes（Rouen）', '邮箱待补 → B 不动'),
    ('XB-C0904', 'Vision Distrib（Drancy；仅公开 compta@ 财务邮箱）', '无销售邮箱 → B 不动'),
    ('XB-C0906', 'Synchronic（1988 起制造/集成/分销）', '制造商属性强，邮箱待补 → B 不动'),
    ('XB-C0909', 'Integral Système', '邮箱待补 → B 不动'),
    ('XB-C0910', 'CNM International', '邮箱待补 → B 不动'),
    ('XB-C0915', 'EET France（EET 集团）', BIG + '（北欧 EET 集团）'),
    ('XB-C0921', 'foTrade（IT 批发 14,000 SKU）', '邮箱待补 → B 不动'),
    ('XB-C0922', 'Normequip（波尔多安防批发）', '邮箱待补 → B 不动'),
    ('XB-C0923', 'Topbiz.fr（IT 批发）', '邮箱待补 → B 不动'),
    ('XB-C0924', 'GrosBill Pro（B2B IT 分销）', '零售集团旗下，邮箱待补 → B 不动'),
    ('XB-C0926', 'OneDirect（企业通信设备分销，D-Link/Zyxel）', '目录型分销，邮箱待补 → B 不动'),
    ('XB-C0933', 'Neoview（法国 CCTV 品牌）', '品牌商自营 → B 不动'),
    ('XB-C0934', 'Dair Market', '邮箱待补 → B 不动'),
    ('XB-C0935', 'GRANTEK', '邮箱待补 → B 不动'),
    ('XB-C0937', 'Satenco', '卫星/安防批发，邮箱待补 → B 不动'),
    ('XB-C0938', 'Elinnov Connect', '邮箱待补 → B 不动'),
    ('XB-C0939', 'Myconnect', '邮箱待补 → B 不动'),
    ('XB-C0949', 'GT Distribution', '邮箱待补 → B 不动'),
    ('XB-C0956', 'YOQO', '邮箱待补 → B 不动'),
    ('XB-C0958', 'E2I Solutions（IP 摄像机制造/分销）', '制造商属性 → B 不动'),
    ('XB-C0974', 'SOLUCAM（分销+安装）', '邮箱待补 → B 不动'),
    ('XB-C0977', 'VDM Ouest（弱电集成+技术分销）', '邮箱待补 → B 不动'),
    ('XB-C0887', 'Tracor Europe → SmartSD', '已并入 SmartSD（NL）→ B 不动，随 SmartSD 条目处理'),
]:
    j(c, 'B', '不动', typ=t, reason=why)
for c, t, why in [
    ('XB-C0192', 'ADI Global Distribution（美国/波多黎各条目，误标 FR）', 'ADI 全球体系 → C 并线到 ADI 条目'),
    ('XB-C0362', 'ADI Global Distribution France', 'ADI 全球体系（巨头）→ C 不动'),
    ('XB-C0883', 'Ubitech Business', '与 XA-C0004 Ubitech 同一公司 → 并线'),
    ('XB-C0891', 'BeIP（2017 被 ALSO 收购，法人 2022 注销）', '已并入 ALSO 集团 → C'),
    ('XB-C0895', 'ACTN（图卢兹 IT 分销）', '与 XA-M168 ACTN 同一公司 → 并线'),
    ('XB-C0899', 'Sphinx France', '与 XA-M499 Sphinx France 同一公司 → 并线'),
    ('XB-C0916', 'EDOX（1993 起 IT/电信/视频分销）', '与 XA-M172 EDOX 同一公司 → 并线'),
    ('XB-C0918', 'Exertis Connect', '2026 并入 Azenn Connect（XB-C0457）→ 并线'),
]:
    j(c, 'C', '并线' if '并线' in why else '不动', typ=t, reason=why)

run(J, 'W3-R06')
