# -*- coding: utf-8 -*-
"""波 3 R13：「邮箱待补」收口批 16 户（爱 2 / 英 1 / 法 6 / 土 4 / 德 3）——含 5 户不再补查的元器件/巨头收口；XB-C0688 于第 92 批并线到 Saga SB-100。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run

J = {}
def j(*a, **k): _j(J, *a, **k)
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_OEM = 'Would a PoE switch line under your own label be of interest, and if so, which port count should we sample first?'

# ---- A 首触 ----
j('XB-C0688', 'C', '并线', typ='Perpa 网络/安防分销 + 自有标签（GelecekBT Bilgi Teknolojileri = Telkolink，Perpa A Blok；老板 Yusuf Ölçer）', reason='来源名仅「Bilgi Teknolojileri」，按 Perpa + PoE 品类判定为 GelecekBT；公司底数第 92 批核实：GelecekBT 与 Telkolink 同一老板 Yusuf Ölçer（LinkedIn「Gelecekbt.com General Manager」+ telkolink.com 联系页 yusuf@telkolink.com），而 Telkolink 已是 Saga 客户 SB-100（+ SB-275 gelecekbt.com）→ 并线到 Saga 侧，不另发首触，避免一人两信',
  ev=[{'claim': 'gelecekbt.com 产品页 GBT-C1400 PoE Extender…İletişim：Perpa Ticaret Merkezi A Blok Kat:13 No:1990 Şişli İstanbul…satis@gelecekbt.com', 'quote': 'GelecekBT Bilgi Teknolojileri · Perpa Ticaret Merkezi A Blok Kat:13 No:1990 Şişli İstanbul · satis@gelecekbt.com', 'url': 'https://gelecekbt.com/GBT-C1400'},
      {'claim': 'LinkedIn Yusuf Ölçer：Gelecekbt.com şirketinde General Manager…GelececekBT.com Telkolink, CLR Networks ve ONET kablolama çözümleri Türkiye Dağıtıcısıdır；Telkolink 联系页 Satış yusuf@telkolink.com', 'quote': 'GelececekBT.com Telkolink, CLR Networks ve ONET kablolama çözümleri Türkiye Dağıtıcısıdır', 'url': 'https://tr.linkedin.com/in/yusuf%C3%B6l%C3%A7er'}])
j('XB-C0889', 'A', '首触', 'W04', '安防进口分销（HEXAPRO Sécurité，Chassieu/Lyon；17 年；2–10 人；Dahua/Ajax/Visonic/Hikvision 分销，面向安装商）', '小型进口分销，里昂区域安装商渠道', 'FR 进口分销、邮箱已补 → 升 A 首触（轻，排 2027-01-28 周四）', kind='dist2', to='contact@hexapro-securite.fr',
  ev=[{'claim': 'LinkedIn：Importateur Distributeur en Matériel de Sécurité…17 ans…2-10 employés；infonet：contact@hexapro-securite.fr', 'quote': 'Importateur Distributeur en Matériel de Sécurité | Fort de ses 17 ans d\'expérience', 'url': 'https://fr.linkedin.com/company/hexaprosecurite'}],
  q=Q_D2)

# ---- B 不动 ----
j('XB-C0480', 'B', '不动', typ='卫星/地面/CCTV 器材商（Satworld，Dublin 12；零售 + 行业账户，面向安装商/集成商/批发）', reason='以卫星电视器材为主、零售门店型 → B 不动；sales@satworld.ie 已记',
  ev=[{'claim': 'Crunchbase：Trade accounts support installers, system integrators, wholesalers, and retail businesses…sales@satworld.ie', 'quote': 'Irelands Premier Satellite, Terrestrial, CCTV Supplier', 'url': 'https://www.satworld.ie/'}])
j('XB-C0476', 'B', '不动', typ='网络设备电商（broadbandbuyer.com / Essanet Ltd，Milton Keynes；2002 起；11,000+ SKU；行业账户；自称英国分销伙伴）', reason='来源库误标 DE，实为英国；品牌货电商、自营选品空间小 → B 不动；公开邮箱为客服 we.care@broadbandbuyer.com（Trustpilot），采购邮箱未见',
  ev=[{'claim': 'About：Since 2002, broadbandbuyer.com has helped trade installers, resellers, and IT professionals…trusted UK distribution partner；Contact 页 Essanet Ltd 21 Kelvin Drive Milton Keynes', 'quote': 'If you\'re a trade installer, reseller, or IT specialist looking for a trusted UK distribution partner, we\'re here to help', 'url': 'https://www.broadbandbuyer.com/about/'}])
j('XB-C0937', 'B', '不动', typ='电子/卫星/安防折扣电商（SATENCO SARL，Plaisance-du-Touch；2011 起；资本 €150k；Metro/Leroy Merlin/Boulanger 平台卖家）', reason='B2C 折扣电商 → B 不动；info@satenco.com 已记',
  ev=[{'claim': 'Metro Marketplace 卖家页：SATENCO SARL…info@satenco.com…Représentants Michael WHARMBY；verif：SARL 2011 资本 150 000 EUR', 'quote': 'Satenco est le spécialiste de la vente en ligne de matériel Satellite et Electronique, à prix discount', 'url': 'https://www.metro.fr/marketplace/seller/56c306cb-539d-4ce9-b711-13d89fda3fef'}])
j('XB-C0939', 'B', '不动', typ='弱电/安防集成商（SAS MYCONNECT，Mudaison 34；2014 起；资本 €100k；1,500 个站点）', reason='集成商 → B 不动；contact@myconnect.fr 已记',
  ev=[{'claim': '官网：Intégrateur national sur le marché des courants faibles et solutions de sécurités…1500 sites；Mentions：SAS MYCONNECT 资本 100.000 €…contact@myconnect.fr', 'quote': 'Intégrateur national sur le marché des courants faibles et solutions de sécurités pour les entreprises', 'url': 'https://myconnect.fr/contact/'}])
j('XB-C0659', 'B', '不动', typ='大型系统集成 + 研发（Proline Bilişim Sistemleri A.Ş.，İstanbul Ataşehir/Ümraniye；生物识别、城市安防、电子身份项目；「infoMet」未定位）', reason='大型集成商/方案商（BIG），非分销渠道 → B 不动；info@pro-line.com.tr 已记',
  ev=[{'claim': '官网：Proline is a Turkish technology company and R&D centre…Secure Documents and Biometric Solutions…info@pro-line.com.tr；AUS Türkiye 会员页 CEO Serdal KARAKAŞ', 'quote': 'Proline is a Turkish technology company and R&D centre that develops software and hardware products', 'url': 'https://pro-line.com.tr/'}])
j('XB-C0159', 'B', '不动', typ='半导体授权分销 + ODM 方案（Atlantik Elektronik GmbH，Planegg/München；1977 起；40+ 年）', reason='元器件渠道，与交换机无关，不再补查 → B 不动；info@atlantikelektronik.com 已记',
  ev=[{'claim': '官网 Contact：Headquarter Munich Fraunhoferstraße 11a 82152 Planegg…info@atlantikelektronik.com；Distribution…40 years of experience', 'quote': 'Atlantik Elektronik has been Germany\'s distributor and ODM solution provider for innovative semiconductor products and technologies for over 40 years', 'url': 'https://www.atlantikelektronik.com/en'}])
j('XB-C1048', 'B', '不动', typ='电子元器件分销（Börsig GmbH Electronic-Distributor，Neckarsulm；40 年；连接器/无源件 + 线缆组件）', reason='元器件渠道，与交换机无关，不再补查 → B 不动；info@boersig.com / export@boersig.com 已记',
  ev=[{'claim': '官网 Contact：Börsig GmbH Electronic-Distributor Siegmund-Loewe-Strasse 5 74172 Neckarsulm…info@boersig.com…Export sales export@boersig.com', 'quote': 'Börsig GmbH Neckarsulm seit 40 Jahren Electronic Distributor für elektromechanische und passive Bauelemente', 'url': 'https://www.boersig.com/en/contact/your-connection-to-us'}])
j('XB-C1115', 'B', '不动', typ='德国 IT 厂商 + 分销（WORTMANN AG，Hüllhorst；1986 起；自有品牌 TERRA；2025 营收 €12 亿；约 800 人；16,000 家经销商）', reason='巨头（BIG）：自有品牌 TERRA 由成熟 ODM 体系供货，小贸易商难切入，不再补查 → B 不动；邮箱未记',
  ev=[{'claim': 'Kurzprofil：über 1 Milliarde € Umsatz in 2025…Hersteller, Distributor und Cloud Service Anbieter…ungefähr 800 Mitarbeitern über 16.000 Fachhändler', 'quote': 'Als Hersteller, Distributor und Cloud Service Anbieter bedienen wir mit ungefähr 800 Mitarbeitern über 16.000 Fachhändler und Systemhäuser in ganz Europa', 'url': 'https://www.wortmann.de/de-de/content/unternehmen-kurzprofil.aspx'}])
j('XB-C0491', 'B', '不动', typ='军工/工业电子元件（Focus Elektronik，来源库备注）', reason='元器件而非网络渠道；R06 网查未得公开邮箱，不再补查 → B 不动',
  ev=[{'claim': '来源库备注「🇹🇷 B类 | 军工+工业电子元件」；R06（2026-10-28）网查无公开邮箱', 'quote': '军工+工业电子元件', 'url': 'data/external_clients/cctv.json#XB-C0491'}])
j('XB-C0493', 'B', '不动', typ='电子元件商（Barbaros Elektronik，1978 起，来源库备注）', reason='元器件而非网络渠道；R06 网查未得公开邮箱，不再补查 → B 不动',
  ev=[{'claim': '来源库备注「🇹🇷 C类 | 1978, 电子元件」；R06（2026-10-28）网查无公开邮箱', 'quote': '1978, 电子元件', 'url': 'data/external_clients/cctv.json#XB-C0493'}])

# ---- C ----
j('XB-C0481', 'C', '不动', typ='手机/平板维修零售店（Cian\'s Tech World，Cavan；2017 起；2–10 人）', reason='消费电子维修零售 → C 不动',
  ev=[{'claim': 'LinkedIn：Industry Retail…2-10 employees…Specialties Tablet Sales & Repairs, Smartphones Sales & Repairs', 'quote': 'Specialties: Tablet Sales & Repairs, Smartphones Sales & Repairs, Laptop Sales & Repairs', 'url': 'https://ie.linkedin.com/company/cianstechworld'}])
j('XB-C0934', 'C', '不动', typ='微型 IT 维修 + 安防分销（DAIR MARKET EURL，Rezé/Nantes；2011 起；官方 0 名员工；dair-secur.fr 目录）', reason='一人公司 → C 不动；dair.market@free.fr 已记',
  ev=[{'claim': 'pappers：Effectif 0 salarié (donnée 2026)…Dirigeant Bouffet Olivier；europages 自述 distributeur spécialisé en équipements de sécurité', 'quote': 'Effectif : 0 salarié (donnée 2026)', 'url': 'https://www.pappers.fr/entreprise/dair-market-533437950'}])
j('XB-C0938', 'C', '不动', typ='微型电气/AV 批发（ELINNOV CONNECT SAS，Le Havre；2022 起；资本 €1,000）', reason='初创微型、资本 €1,000 → C 不动',
  ev=[{'claim': 'societe.com：DATE DE CREATION 17 mars 2022…Commerce de gros de matériel électrique；societeinfo：Capital social 1 000 €', 'quote': 'Capital social 1 000 €', 'url': 'https://societeinfo.com/app/recherche/societe/911466563'}])
j('XB-C0956', 'C', '不动', typ='数字营销 + 电信 + 安防小代理（YOQO SAS，Dijon/Paris；2022 起；资本 €5k）', reason='微型多业务代理 → C 不动',
  ev=[{'claim': 'yoqo.fr：YOQO accompagne les TPE et PME…Digital & acquisition…Télécom…Sécurité；Politique：SAS au capital de 5000€', 'quote': 'YOQO – SAS au capital de 5000€ – RCS Paris', 'url': 'https://yoqo.fr/politique-de-confidentialite/'}])

run(J, 'W3-R13', expect=16)
