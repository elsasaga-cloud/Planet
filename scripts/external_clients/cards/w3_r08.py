# -*- coding: utf-8 -*-
"""波 3 R08：「邮箱待补」补查第二批 6 户（土 3 / 法 3）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run

J = {}
def j(*a, **k): _j(J, *a, **k)
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_D2S = 'Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?'

j('XB-C0510', 'A', '首触', 'W02', '安防纯分销（Y3K Güvenlik Teknolojileri A.Ş.，Istanbul Beykoz；2005 起；2011 起 Securitas 集团；35 个国际品牌土耳其分销；进口 + 备货 + 分销 CCTV/门禁）', '纯分销进口商，35 品牌 → 可纳入新 PoE 线', 'TR 主战场、纯分销、邮箱已补 → 升 A 首触（排 2027-01-14 周四）', kind='dist2', to='y3k@y3k.com.tr',
  ev=[{'claim': 'güvenlikonline 企业档案：Y3K bir Securitas grup şirketidir…35 uluslararası markanın Türkiye distribütörüdür；y3k@y3k.com.tr', 'quote': 'Y3K, elektronik güvenlik sistemlerinde kalitesi kanıtlanmış 35 uluslararası markanın Türkiye distribütörüdür', 'url': 'https://guvenlikonline.com/tr/firmalar/y3k-guvenlik-teknolojileri'}],
  q=Q_D2)
j('XB-C0977', 'A', '首触', 'W03', '弱电技术分销 + 集成（VDM Ouest，Bonchamp-lès-Laval；2007 起；11–50 人；面向安装商的批发：消防/视频/门禁/广播）', '面向安装商的区域批发，PoE 配套', 'FR 区域批发、邮箱已补 → 升 A 首触（轻，排 2027-01-21 周四）', kind='dist2', to='info@vdmouest.com',
  ev=[{'claim': 'europages：« intégrateur et distributeur technique » dans le domaine du courant faible, est le partenaire des installateurs；infonet info@vdmouest.com；LinkedIn 11–50 人、2007 起', 'quote': 'VDM Ouest est votre distributeur spécialiste de systèmes de sécurité électronique depuis 2007', 'url': 'https://fr.linkedin.com/company/vdm-ouest'}],
  q=Q_D2S)
j('XB-C0514', 'C', '不动', typ='CLR Networks（深圳网络设备品牌；土耳其分销为 GelecekBT，satis@gelecekbt.com）', reason='同行品牌（中国厂商）→ C；其土耳其分销 GelecekBT 可作为新线索（下一轮考虑新增）',
  ev=[{'claim': '官网联系页：Headquarters…Baoan District, Shenzhen；EMEA 联系 yusuf@clrnetworks.com；gelecekbt.com 为土耳其分销', 'quote': 'CLR Networks Türkiye Dağıtıcısı / Distribütörü GelecekBT\u2019dir', 'url': 'http://www.clrnetworks.com/contact.html'}])
j('XB-C0509', 'B', '不动', typ='IT/安防集成 + Digifort 分销（Rima Elektronik，Istanbul Florya；2000 起；销售 Erhan Türkay）', reason='以集成/项目为主；bilgi@rimaelektronik.com 已记 → B 不动',
  ev=[{'claim': '官网：uçtan uca entegre bilişim hizmetleri…2000 yılında kurulmuştur；bilgi@rimaelektronik.com', 'quote': 'Rima Elektronik Bilişim ve Güvenlik Sistemleri…2000 yılında kurulmuştur', 'url': 'https://www.rimaelektronik.com/iletisim'}])
j('XB-C0894', 'B', '不动', typ='安防安装/维保（France Alarme，Saint-Étienne）', reason='安装商而非分销；contact@francealarme.net 已记 → B 不动',
  ev=[{'claim': 'Facebook：Nous installons et maintenons les systèmes…contact@francealarme.net', 'quote': 'Nous sommes experts en systèmes de sécurité électronique. Nous installons et maintenons', 'url': 'https://www.facebook.com/francealarmeRhoneAlpesAuvergne/'}])
j('XB-C0922', 'B', '不动', typ='消防/合规设备 B2B 网店批发（Normequip，Canéjan/Bordeaux；1998 起；3–9 人；进口商）', reason='主营消防/城市设施，视频监控只是一个品类；contact@normequip.com 已记 → B 不动',
  ev=[{'claim': 'europages：Créée en 1998，Salariés 5-9，Distributeur；官网 contact@normequip.com', 'quote': 'leader de la distribution de produits de sécurité incendie sur internet', 'url': 'https://www.normequip.com/'}])

run(J, 'W3-R08', expect=6)
