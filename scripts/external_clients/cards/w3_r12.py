# -*- coding: utf-8 -*-
"""波 3 R12：「邮箱待补」补查第六批 12 户（保 3 / 罗 4 / 西 1 / 意 1 / 丹 1 / 荷 1 / 波 1）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run

J = {}
def j(*a, **k): _j(J, *a, **k)
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_D2S = 'Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?'
Q_OEM = 'Would a PoE switch line under your own label be of interest, and if so, which port count should we sample first?'

# ---- A 首触 ----
j('XB-C0409', 'A', '首触', 'W03', 'IT 批发分销（Lancom Bulgaria Ltd.，Sofia；2004 起；11–50 人；ZTE/Ubiquiti/MikroTik/TP-Link/Zyxel 分销 + 自有品牌 SeaMAX 线缆/配件；IDG 2014 保加利亚前 5 分销）', '网络分销 + 自有品牌 → 可加一条自有标签 PoE 线', 'BG（欧洲）、网络分销 + 自有品牌、邮箱已补 → 升 A 首触，用自有标签问句（排 2027-01-21 周四）', kind='dist', to='sales@lancombg.com',
  ev=[{'claim': '官网：частна компания за доставка на едро…ZTE, Ubiquiti, MikroTik, TP-LINK…собствената си марка SeaMAX；About：one of the 5 largest distributors, according to the IDG ranking for 2014；联系页 sales@lancombg.com', 'quote': 'one of the 5 largest distributors, according to the IDG ranking for 2014', 'url': 'https://www.lancombg.com/en/about-us'}],
  q=Q_OEM)
j('XB-C0434', 'A', '首触', 'W03', '安防专业批发（Soluciones Tecnológicas SEVITEC S.L.，Mairena del Aljarafe/Sevilla；2017 起；21–50 人；Ajax 官方分销；仅对专业客户）', '面向安装商的安防批发，视频 + 门禁配套 PoE', 'ES（欧洲）、专业批发、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist2', to='contacto@sevitec.es',
  ev=[{'claim': '官网：Distribución mayorista de Alarmas Ajax, videovigilancia, control de accesos y domótica exclusiva para profesionales y empresas…contacto@sevitec.es；prospeo 21–50 人、2017 起', 'quote': 'Distribución mayorista de Alarmas Ajax, videovigilancia, control de accesos y domótica exclusiva para profesionales y empresas', 'url': 'https://www.sevitec.es/'}],
  q=Q_D2S)
j('XB-C0073', 'A', '首触', 'W04', '安防进口分销（Telesystem s.r.l.，Bacău；2007 起；Bacău/București/Cluj/Iași 四点；B2B 平台；仅面向安装商；PoE 交换机品类在售）', '罗马尼亚进口 + 分销，有 PoE 交换机品类', 'RO（欧洲）、进口分销、邮箱已补 → 升 A 首触（排 2027-01-28 周四）', kind='dist2', to='office@telesystem.ro',
  ev=[{'claim': '官网：TELESYSTEM este importator si distribuitor oficial…adresate companiilor de profil；品类页 Switch-uri PoE…Distribuitor autorizat in Romania；Uniview 伙伴页 office@telesystem.ro', 'quote': 'Founded in 2007, TELESYSTEM is one of the more dynamic distribution companies in Romania, offering professional solutions and equipment addressed exclusively to installers', 'url': 'https://global.uniview.com/Partner/Find_our_partners/Partners/Europe/'}],
  kp=[{'name': 'David Marian', 'role': '联系人（protectiesipaza 名录）', 'source': 'https://www.protectiesipaza.ro/firme-de-paza/telesystem-s-r-l-protectie-si-paza/'}],
  q=Q_D2)
j('XB-C0345', 'A', '首触', 'W04', '安防进口 + 网店 + 安装（Atu Tech SRL，Sibiu；2011 起；București 代表处；自称全线直接进口）', '直接进口商，兼做安装与零售', 'RO（欧洲）、直接进口、邮箱已补 → 升 A 首触（轻，排 2027-01-28 周四）', kind='dist', to='office@a2t.ro',
  ev=[{'claim': 'Trustpilot 公司自述：Importator direct pentru toata gama de produse din domeniul sistemelor de securitate；ghidul.ro：office@a2t.ro / bucuresti@a2t.ro', 'quote': 'Importator direct pentru toata gama de produse din domeniul sistemelor de securitate', 'url': 'https://www.trustpilot.com/review/a2t.ro'}],
  q=Q_D2)
j('XB-C0347', 'A', '首触', 'W04', '安防分销（SC General Security SRL，Cluj-Napoca；1998 起；Cluj/București/Brașov/Timișoara 分部；自称罗马尼亚最大 Hikvision 供应商；GS Distributie 经销 App）', '罗马尼亚头部安防分销，经销网成熟', 'RO（欧洲）、头部分销、公开管理层邮箱 → 升 A 首触（排 2027-01-28 周四）', kind='dist2', to='bogos@generalsecurity.ro',
  ev=[{'claim': 'Distributie 页：suntem cel mai mare furnizor de produse Hikvision…aplicatia GS Distributie；Contact 页公开 Top Management: Dan Bogos / bogos@generalsecurity.ro', 'quote': 'suntem cel mai mare furnizor de produse Hikvision, care este liderul mondial in solutii de supraveghere video', 'url': 'https://generalsecurity.ro/distributie/'}],
  kp=[{'name': 'Dan Bogos', 'role': 'Top Management（Cluj）', 'source': 'https://generalsecurity.ro/contact/'}, {'name': 'Horațiu Căpîlnean', 'role': 'Top Management（Cluj）', 'source': 'https://generalsecurity.ro/contact/'}],
  q=Q_D2)
j('XB-C0690', 'A', '首触', 'W04', '安防进口分销 + 自有品牌（SC Cristal SRL / Rovision，Bacău；1992 起；Dahua/Hikvision 授权分销；自有品牌 Rovision；B2B App）', '自有品牌 Rovision → 自有标签 PoE 线的 OEM 候选', 'RO（欧洲）、进口 + 自有品牌、邮箱已补 → 升 A 首触，用自有标签问句（排 2027-01-28 周四）', kind='dist', to='vanzari@rovision.ro',
  ev=[{'claim': '官网「Despre noi」：importator de 7 ani…Distribuitor autorizat…Dahua și Hikvision；品牌页：Rovision…importul si distributia…instalatorilor sau revanzatorilor；联系页 vanzari@rovision.ro', 'quote': 'Cristal SRL Bacau infiintata in anul 1992 are ca obiect principal de activitate importul si distributia de camere supraveghere video', 'url': 'https://rovision.ro/brand/rovision/'}],
  q=Q_OEM)

# ---- B 不动 ----
j('XB-C0099', 'B', '不动', typ='跨欧线上安防供应商（MEGATEH.eu / Expresstime OÜ，Tallinn 爱沙尼亚；2008 起；30,000+ 订单；经销商折扣）', reason='实为爱沙尼亚公司（来源库误标 BG）；品牌货线上供应，非选品型分销 → B 不动；sales@megateh.eu 已记', iso='EE',
  ev=[{'claim': 'About：MEGATEH.eu is an Estonian company…Operating under Expresstime OÜ since 2008…over 30,000 orders…sales@megateh.eu', 'quote': 'MEGATEH.eu is an Estonian company specialising in the supply of video surveillance (CCTV) and modern security equipment across Europe and worldwide', 'url': 'https://www.megateh.eu/about-us'}])
j('XB-C0307', 'B', '不动', typ='线上 CCTV 进口零售（MB Vision Ltd.，Plovdiv；2012 起；Hikvision/Dahua 授权；cctvspot.co.uk 面向英国）', reason='线上零售为主，官方邮箱为 gmail + sales@uk.mbvision.net → B 不动',
  ev=[{'claim': 'cctvspot.co.uk Terms：MB Vision Ltd. with VAT reg BG202150972…contact us at cctv.mbvision @ gmail.com…sales @ uk.mbvision.net', 'quote': 'Since our inception in 2012, MB Vision Ltd. has been a leading importer and distributor of high-quality CCTV equipment', 'url': 'https://cctvspot.co.uk/terms'}])
j('XB-C0007', 'B', '不动', typ='自有品牌小厂商（DSE s.r.l.，San Mauro Torinese；1998 起；2 名员工、2024 营收 €689k；ONVIF 会员）', reason='同行自有品牌、规模极小 → B 不动；info@dsecctv.com 已记',
  ev=[{'claim': 'ufficiocamerale：Fatturato € 688.745,00 (2024)…Dipendenti 2；dsecctv.com 联系页 Product information info@dsecctv.com', 'quote': 'DSE è un costruttore di prodotti per la videosorveglianza', 'url': 'https://www.dsecctv.com/contattarci.htm'}])
j('XB-C0789', 'B', '不动', typ='电气元器件独立分销（Electrical Components Holland B.V.，Papendrecht；2018 起；5–9 人）', reason='元器件渠道，与交换机无关 → B 不动；sales@echolland.com 已记',
  ev=[{'claim': '官网：ECH is an independent distributor of electrical components…；联系页 sales@echolland.com；europages 5–9 人', 'quote': 'ECH is an independent distributor of electrical components with a global network of reliable suppliers', 'url': 'https://echolland.com/'}])

# ---- C ----
j('XB-C0461', 'C', '不动', typ='PTZ 云台制造商（2B Security Systems ApS，Roskilde；1997 起；2 名员工）', reason='制造商且仅 2 人 → C 不动',
  ev=[{'claim': 'About：European manufacturer and worldwide distributor of surveillance equipment like PTZ systems…；proff.dk：Antal ansatte 2', 'quote': '2B Security Systems ApS is establised in 1997…The company is a European manufacturer and worldwide distributor', 'url': 'https://www.2bsecurity.com/about-us/'}])
j('XB-C0072', 'C', '不动', typ='中国 GPU 服务器/交换机厂商的波兰 SEO 页（Quantix Intelligent Computing Co., Ltd.，Shenzhen；2017 起）', reason='非波兰公司、同行厂商 → C 不动',
  ev=[{'claim': '官网：Quantix Intelligent Computing Co., Ltd.…based in China…our main engineering team is based in Shenzhen', 'quote': 'While our main engineering team is based in Shenzhen, we partner with several system integrators in Warsaw and Krakow', 'url': 'https://www.quantixgpu.com/local/network-switch-manufacturers-supplier-in-the-poland-market/'}])

run(J, 'W3-R12', expect=12)
