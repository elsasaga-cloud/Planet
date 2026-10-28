# -*- coding: utf-8 -*-
"""波 3 R09：「邮箱待补」补查第三批 12 户（土 7 / 法 5）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run

J = {}
def j(*a, **k): _j(J, *a, **k)
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_D2S = 'Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?'
Q_OEM = 'Would a PoE switch line under your own label be of interest, and if so, which port count should we sample first?'

# ---- A 首触 ----
j('XB-C0511', 'A', '首触', 'W02', '安防批发（Kasa Elektronik Güvenlik Sistemleri A.Ş.，Ankara Çankaya；官网带 B2B 登录）', '有 B2B 经销体系的安防批发商', 'TR 主战场、B2B 批发、邮箱已补 → 升 A 首触（排 2027-01-14 周四）', kind='dist2', to='info@kasaguvenlik.com',
  ev=[{'claim': '官网：Kasa Elektronik Güvenlik Sistemleri A.Ş.…Email: info@kasaguvenlik.com；页面有 B2B GİRİŞİ', 'quote': 'Kasa Elektronik Güvenlik Sistemleri A.Ş. Aşağı Öveçler Mah. Lizbon Cad. No: 69/B Çankaya Ankara', 'url': 'https://kasaguvenlik.com/'}],
  q=Q_D2S)
j('XB-C0700', 'A', '首触', 'W02', '安防进口分销（Okisan Güvenlik Teknolojileri A.Ş.，Istanbul Okmeydanı；1993 起；Tiandy 独家 + Dahua 土耳其分销；5,000+ 经销商；Ankara/İzmir 分部）', '土耳其头部安防进口商，经销网大，PoE 交换机是其配套品类', 'TR 主战场、进口 + 分销、邮箱已补 → 升 A 首触（排 2027-01-14 周四）', kind='dist2', to='info@okisan.com',
  ev=[{'claim': 'LinkedIn：leading importing company…28 years…network consisted of more than 5,000 distributors；manuzone 列 info@okisan.com', 'quote': 'Okisan Güvenlik Teknolojileri, is a leading importing company in the security industry for 28 years', 'url': 'https://tr.linkedin.com/company/okisan-g%C3%BCvenlik-teknolojileri-a-%C5%9F-'}],
  kp=[{'name': 'Ekrem Özkara', 'role': '负责人（güvenliktedarik 名录）', 'source': 'https://guvenliktedarik.com/brand/okisan-guvenlik-teknolojileri-a-s/'}],
  q=Q_D2)
j('XB-C0516', 'A', '首触', 'W02', '自有品牌安防进口商（Besta Güvenlik İç ve Dış Tic. Ltd.，Istanbul Kadıköy + İzmir 分店；自有 BESTA 摄像机 / PoE 交换机 BST 系列；toptanguvenlik.com 卖 ARNA 品牌 PoE）', '自有标签 PoE 交换机 → OEM 品牌商（目标客户第一序）', 'TR、自有品牌进口商、邮箱已补 → 升 A 首触，用自有标签问句（排 2027-01-14 周四）', kind='dist', to='info@bestaguvenlik.com',
  ev=[{'claim': '官网产品页：BESTA 4 PORT POE SWİTCH BST420 / BST-08；şikayetvar 列 info@bestaguvenlik.com；bestabilisim 联系页：Kadıköy 总部 + İzmir Balçova 分店', 'quote': 'Besta BST420, 4 PoE portuyla küçük ölçekli kamera sistemleri için kompakt ve ekonomik switch çözümü', 'url': 'https://www.bestaguvenlik.com/'}],
  q=Q_OEM)
j('XB-C0921', 'A', '首触', 'W03', 'IT 批发（1foTrade，Sandouville 诺曼底；2003 起；14,000 SKU / 300 品牌；11–50 人；面向 IT 经销商）', '区域 IT 批发商，有网络品类，决策链短', 'FR、IT 批发、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist', to='contact@1fotrade.com',
  ev=[{'claim': '官网 CGV：distribution de pièces détachées, composants et périphériques informatiques depuis 2003…14 000 références…contact@1fotrade.com；LinkedIn 11–50 人', 'quote': '1foTrade fournit aux revendeurs IT, matériels, composants et configurations prêts à vendre', 'url': 'https://www.1fotrade.com/cgv/'}],
  kp=[{'name': 'Philippe Haneuse', 'role': '负责人（Directeur de la publication）', 'source': 'https://www.1fotrade.com/legale/'}],
  q=Q_D2)
j('XB-C0910', 'A', '首触', 'W03', '弱电分销 + 集成（CNM International / Comptoir de Négoce Méridional，La Ciotat；1997 起家族企业；11–50 人；Tiandy 伙伴）', '区域弱电分销商，视频监控 + 门禁配套 PoE', 'FR 区域分销、邮箱已补 → 升 A 首触（轻，排 2027-01-21 周四）', kind='dist2', to='contact@cnm-international.fr',
  ev=[{'claim': 'LinkedIn：société familiale créée en 1997. Distributeur/Intégrateur…Courants Faibles；Tiandy 项目页列 contact@cnm-international.fr', 'quote': 'CNM International, société familiale créée en 1997. Distributeur/Intégrateur spécialisé en Matériels et Solutions Courants Faibles', 'url': 'https://fr.linkedin.com/company/cnm-international'}],
  q=Q_D2S)

# ---- B 不动 ----
j('XB-C0502', 'B', '不动', typ='IP 摄像机批发网店（Güvenlikbayii Ltd. Şti.，Istanbul Küçükçekmece，非 Ankara）', reason='官网邮箱被遮蔽，仅电话/WhatsApp → 仍无公开邮箱 → B 不动',
  ev=[{'claim': '官网：Güvenlikbayii Ltd. Şti. Cumhuriyet Mah. İnönü Cd. No: 29 Küçükçekmece/İstanbul；邮箱显示为 [email protected]', 'quote': 'Güvenlikbayii.com olarak ip güvenlik kamerası toptan satışı yapmaktayız', 'url': 'https://www.guvenlikbayii.com/'}])
j('XB-C0504', 'B', '不动', typ='Perpa 小店（Perpa Elektronik / İnteractive Bilişim Elektronik Ltd.，Perpa B 座；照明 + 电子）', reason='小型零售店铺，非渠道；info@perpaelektronik.com 已记 → B 不动',
  ev=[{'claim': 'Perpa 名录：Perpa Elektronik…AYDINLATMA…info@perpaelektronik.com.tr；官网 info@perpaelektronik.com', 'quote': 'Firma Resmi Adı : İNTERACTİVE BİLİŞİM ELEKTRONİK REKLAM VE BİLGİ TEKNOLOJİLERİ SANAYİ TİCARET LİMITED ŞİRKETİ', 'url': 'https://www.perpaelektronik.com/bize-ulasin/'}])
j('XB-C0889', 'B', '不动', typ='安防分销（Hexapro Sécurité，Chassieu/Lyon；Dahua/Ajax/Visonic/Hikvision 官方分销）', reason='官网仅电话无邮箱 → 仍无公开邮箱 → B 不动（可下轮再试）',
  ev=[{'claim': '官网「Qui sommes-nous」：HEXAPRO, revendeur officiel Dahua France et Ajax systems…Tél: 04.72.51.28.28（无邮箱）', 'quote': 'En tant que distributeur Dahua France mais aussi distributeur Ajax systems , Visonic France et Hikvision France', 'url': 'https://www.hexapro-securite.fr/content/18-qui-sommes-nous-Hexapro-distributeur-Visonic-Dahua-Ajax-Alarmes-Hikvision'}])
j('XB-C0494', 'B', '不动', typ='服务器/网络新机 + 翻新供应商（TRUNK Bilişim Teknolojileri Ltd.，Istanbul Ataşehir；Cisco/Juniper/HPE/Ubiquiti/Ruijie）', reason='二手/翻新 + 企业大牌为主，非我方渠道；info@trunk.tr 已记 → B 不动',
  ev=[{'claim': '官网：Sıfır ve ikinci el network ekipmanları tedariki…info@trunk.tr', 'quote': 'Cisco, Juniper, HPE, Extreme, Ubiquiti ve Ruijie switch, router, access point ve SFP modülleri. Sıfır ve ikinci el network ekipmanları tedariki', 'url': 'https://www.trunk.tr/cozumler/sifir-ikinci-el-network-ekipmanlari/'}])
j('XB-C0906', 'B', '不动', typ='安防制造商（Synchronic，Franqueville-Saint-Pierre；1988 起；76 人；银行安防；Urmet 集团）', reason='制造商 / 集团子公司，非分销渠道 → B 不动',
  ev=[{'claim': 'Urmet 公告：Le Groupe URMET France annonce le rachat de la société SYNCHRONIC；ugap：76 salariés、CA €17.5M', 'quote': 'SYNCHRONIC développe et fabrique des solutions destinées à tous types de sites', 'url': 'https://www.urmet.fr/actualites/synchronic-rejoint-le-groupe-urmet-france-pour-renforcer-le-pole-tertiaire.html'}])
j('XB-C0926', 'B', '不动', typ='企业通信设备电商分销集团（Onedirect，Saint-Estève/Perpignan；1999 起；51–200 人；8 国）', reason='跨国目录电商，采购链长 → B 不动；hello@onedirect.fr 已记',
  ev=[{'claim': '官网「Qui sommes-nous」：LE GROUPE ONEDIRECT EST PRÉSENT DANS 8 PAYS…hello@onedirect.fr；LinkedIn 51–200 人、1999 起', 'quote': 'LE GROUPE ONEDIRECT EST PRÉSENT DANS 8 PAYS', 'url': 'https://www.onedirect.fr/qui-sommes-nous'}])

# ---- C ----
j('XB-C0512', 'C', '不动', typ='安装商（Aydın Elektronik Güvenlik Sistemleri，Ankara Ulus；仅 hotmail 邮箱）', reason='安装商 + 免费邮箱 → C 不动',
  ev=[{'claim': '官网联系页：ayd_guvenlik@hotmail.com；Kale Mahallesi…Ulus Altındağ / Ankara', 'quote': 'Mail Adresimiz ayd_guvenlik@hotmail.com', 'url': 'https://ankarakamerasistemleri.com.tr/iletisim/'}])

run(J, 'W3-R09', expect=12)
