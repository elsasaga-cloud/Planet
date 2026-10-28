# -*- coding: utf-8 -*-
"""波 3 R11：「邮箱待补」补查第五批 12 户（法 6 / 波 3 / 土 3）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run

J = {}
def j(*a, **k): _j(J, *a, **k)
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_D2S = 'Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?'

# ---- A 首触 ----
j('XB-C0909', 'A', '首触', 'W03', '安防专业分销（Intégral Système，Collégien 77；2001 起；51–200 人；14–17 家分公司、150 名专家；Axis / Provision-ISR 授权分销）', '法国全国性安防分销网络，视频 + 门禁配套 PoE', 'FR 全国分销、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist2', to='info@integral-systeme.fr',
  ev=[{'claim': 'Distributique 2025-06：Axis…signer un accord de distribution avec Intégral Système…17 agences et 150 experts；官网联系页 info@integral-systeme.fr；LinkedIn 51–200 人、2001 起', 'quote': 'le distributeur dispose de 17 agences et 150 experts en sécurité repartis dans toute la France', 'url': 'https://www.distributique.com/actualites/lire-les-solutions-d-axis-communications-desormais-distribuees-par-integral-systeme-36276.html'}],
  kp=[{'name': 'Stéphane Melinand Jegou', 'role': 'PDG', 'source': 'https://www.distributique.com/actualites/lire-les-solutions-d-axis-communications-desormais-distribuees-par-integral-systeme-36276.html'}],
  q=Q_D2)
j('XB-C0584', 'A', '首触', 'W03', '安防分销（MKJ Systemy Zabezpieczeń Sp. z o.o.，总部 Gdańsk，Szczecin 等多分部；11–50 人；B2B 平台 b2b.mkj.net.pl；Hanwha / Elmes 分销）', '波兰多分部安防分销 + B2B 平台', 'PL 次重点、分销 + B2B、邮箱已补 → 升 A 首触（排 2027-01-21 周四；XB-C0822 同公司已并线）', kind='dist2', to='centrala@mkj.net.pl',
  ev=[{'claim': '官网 Kontakt：MKJ Systemy zabezpieczeń Sp. z o.o. ul. Kielnieńska 187 Gdańsk…centrala@mkj.net.pl；Szczecin 分部 szczecin@mkj.net.pl；b2b.mkj.net.pl 为 B2B 商店', 'quote': 'MKJ Systemy zabezpieczeń Sp. z o.o. ul. Kielnieńska 187 (58)770 19 00 centrala@mkj.net.pl', 'url': 'https://www.mkj.net.pl/kontakt'}],
  q=Q_D2S)
j('XB-C0587', 'A', '首触', 'W03', '安防进口分销（Promitel Sp. z o.o. Sp. k.，Chorzów；B2B 平台 b2b.promitel.pl；品类含 LAN/PoE/WiFi、机柜；Satel 分销）', '进口 + 分销，网络品类已在卖，B2B 平台直接上架', 'PL 次重点、进口分销、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist2', to='info@promitel.pl',
  ev=[{'claim': '官网「Nasza misja」：Od lat zajmujemy się importem i dystrybucją urządzeń…；首页品类 LAN, PoE, WiFi networks…PoE switches；联系页 info@promitel.pl / b2b@promitel.pl', 'quote': 'A wide range of structural network devices, PoE switches, routers and WiFi wireless devices', 'url': 'https://promitel.pl/'}],
  q=Q_D2)

# ---- B 不动 ----
j('XB-C0923', 'B', '不动', typ='IT 电商批发（Topbiz.fr / Actuelburo 集团，Narrosse 朗德省；2005 起；28,000 SKU；B2B + B2C）', reason='目录电商、面向经销商和个人，非专业渠道 → B 不动；serviceclient@topbiz.fr 已记',
  ev=[{'claim': '官网：Grossiste informatique depuis près de 20 ans…28 370 références…serviceclient@topbiz.fr', 'quote': 'Topbiz.fr fournit les revendeurs, les entreprises et les particuliers depuis les Landes', 'url': 'https://www.topbiz.fr/'}])
j('XB-C0924', 'B', '不动', typ='零售商 B2B 分部（GrosBill Pro，Paris；GrosBill 连锁的企业客户部门）', reason='零售集团的 B2B 窗口，不做进口选品 → B 不动；contact@grosbill-pro.com 已记',
  ev=[{'claim': 'pro.grosbill.com：Par e-mail contact@grosbill-pro.com；grosbill-pro.com 多家门店', 'quote': 'GrosBill Pro : matériel informatique pour les entreprises', 'url': 'https://pro.grosbill.com/'}])
j('XB-C0949', 'B', '不动', typ='品牌自营分销（GT Distribution France，Villeneuve-d\'Ascq；GT Alarme 官方分销）', reason='单一品牌的自营分销 → B 不动；contact@gtfrance.fr 已记',
  ev=[{'claim': '官网：Gt France Distribution le Distributeur Officiel des Alarmes et Produits GT ALARME…contact@gtfrance.fr', 'quote': 'Gt France Distribution le Distributeur Officiel des Alarmes et Produits GT ALARME', 'url': 'https://www.gtfrance.fr/'}])
j('XB-C0503', 'B', '不动', typ='Perpa 安防批发店（最接近匹配：Güvenlik Toptancım，Perpa A 座 5 层 419；或 İzmir Balçova 的 Toptan Güvenlik Sistemleri = Besta 分店）', reason='来源名「Toptan Güvenlik」为通用词，身份不唯一；info@guvenliktoptancim.com 已记待确认 → B 不动',
  ev=[{'claim': 'perpahaber：Güvenlik Toptancım Perpa İletişim…A Blok Kat: 5 No: 419…info@guvenliktoptancim.com；toptanguvenlik.com 地址与 Besta İzmir 分店一致', 'quote': 'Halil Rıfat Paşa Mahallesi Perpa Ticaret Merkezi A Blok Kat: 5 No: 419 Şişli İstanbul', 'url': 'https://www.perpahaber.com/guvenlik-toptancim/'}])
j('XB-C0513', 'B', '不动', typ='安防经销/安装（Güler Güvenlik Teknoloji，İzmir Karşıyaka；Ruijie Reyee 经销）', reason='区域经销兼安装，规模小 → B 不动；info@gulerguvenlik.com.tr 已记',
  ev=[{'claim': '官网 İletişim：info@gulerguvenlik.com.tr；guvenlikonline：Cevdet Bilsay Cad. No:92/E Karşıyaka/İZMİR', 'quote': 'Güler Güvenlik Teknoloji ® Profesyonel Çözümler', 'url': 'https://www.gulerguvenlik.com/iletisim'}])

# ---- C ----
j('XB-C0935', 'C', '不动', typ='小型网店（GRANTEK / camerasurveillance.net，Paris；2008 起；1–2 人；面向个人与小商户）', reason='1–2 人的 B2C 网店 → C 不动',
  ev=[{'claim': 'pappers：Vente à distance sur catalogue général；Effectif Entre 1 et 2 salariés；Dirigeant Granovskiy Oleg', 'quote': 'Effectif : Entre 1 et 2 salariés (donnée 2022)', 'url': 'https://www.pappers.fr/entreprise/grantek-504203332'}])
j('XB-C0974', 'C', '不动', typ='安装商（SOLUCAM SARL，Roncq 59；2012 起；1–2 人）', reason='1–2 人安装商 → C 不动',
  ev=[{'claim': 'societe.com：Active 1 à 2 salariés…Travaux d\'installation électrique…Julien VERCAMER；官网 contact@solucam.fr', 'quote': 'ACTIVITÉ (NAF / APE): Travaux d\'installation électrique dans tous locaux - 4321A', 'url': 'https://www.societe.com/societe/solucam-750773186.html'}])
j('XB-C0708', 'C', '不动', typ='无法定位（「CTS Katowice」：同名 CTS Technology Tychy 为工业机械，c-t-s.pl 为汽车改装）', reason='来源库条目无域名、无法唯一定位 → C 不动',
  ev=[{'claim': 'web_search 2026-10-28：Katowice 周边无 CTS 安防/网络分销命中', 'quote': '', 'url': 'https://ctstechnology.pl/kontakt/'}])
j('XB-C0505', 'C', '不动', typ='聚合条目（Perpa Güvenlik / VENAS / ÖZTEK / POSCAM / ONQAM 多店合并）', reason='来源库把 Perpa 多家店铺并成一条，非单一公司 → C 不动（各店如需另立条目再补）')

run(J, 'W3-R11', expect=12)
