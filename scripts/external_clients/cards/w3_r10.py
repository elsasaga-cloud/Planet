# -*- coding: utf-8 -*-
"""波 3 R10：「邮箱待补」补查第四批 12 户（德 6 / 英 2 / 美 3 / 波 1）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run

J = {}
def j(*a, **k): _j(J, *a, **k)
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_D2S = 'Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?'
Q_OEM = 'Would a PoE switch line under your own label be of interest, and if so, which port count should we sample first?'

# ---- A 首触 ----
j('XB-C0363', 'A', '首触', 'W03', '视频安防分销（erdkreis CCTV/IP-VIDEO GmbH，Bergkirchen-Günding 慕尼黑近郊；咨询-规划-销售-培训；Avigilon/Hikvision/Barox/Videotec/Hanwha/Pelco）', '德国视频安防专业分销，PoE 交换机为配套品类', 'DE 主战场、专业分销、邮箱已补 → 升 A 首触（排 2027-01-21 周四；XB-C1096 同公司并线）', kind='dist2', to='vertrieb@erdkreisvideo.de',
  ev=[{'claim': '官网 Kontakt：Zentrale…Mail: vertrieb@erdkreisvideo.de；首页：Videoüberwachungstechnik Beratung-Planung-Verkauf-Schulung |Ava|Avigilon|Hikvision|Barox|Videotec|Hanwha|Pelco', 'quote': 'erdkreis CCTV/IP-VIDEO GmbH Dieselstraße 16 D-85232 Bergkirchen-Günding', 'url': 'https://www.erdkreisvideo.de/kontakt/'}],
  kp=[{'name': 'Stefan Palme', 'role': 'Geschäftsführer（Impressum）', 'source': 'http://www.erdkreisvideo.de/impressum/'}],
  q=Q_D2)
j('XB-C1062', 'A', '首触', 'W03', '视频/安防技术经销 + B2B 门户（ModiTech Service GmbH，Chemnitz；b2b.moditech.de；2N 等门禁/视频品牌；品牌 Digital Key World）', '面向安装商的 B2B 经销，小公司决策快', 'DE、B2B 经销、邮箱已补 → 升 A 首触（轻，排 2027-01-21 周四）', kind='dist2', to='shop@moditech.de',
  ev=[{'claim': 'shop.moditech.de 联系页：ModiTech Video- und Sicherheitstechnik…E-Mail: shop@moditech.de；b2b.moditech.de 为 B2B 订购门户；Impressum GF André Dietze', 'quote': 'ModiTech Video- und Sicherheitstechnik André Dietze Bernsdorfer Straße 291 09125 Chemnitz', 'url': 'https://shop.moditech.de/Ueber-uns/Kontakt'}],
  kp=[{'name': 'André Dietze', 'role': 'Geschäftsführer', 'source': 'https://www.moditech.de/impressum/'}],
  q=Q_D2S)
j('XB-C0685', 'A', '首触', 'W03', '安防系统直供商（CCTV Camera Pros LLC，Lantana/Boynton Beach FL；退伍军人企业；自有 Viewtron 线；在售 PoE 交换机）', '美国线上直供 + 自有品牌，PoE 交换机已在卖', 'US 主战场、自有品牌线、邮箱已补 → 升 A 首触，用自有标签问句（排 2027-01-20 周三）', kind='dist', to='info@cctvcamerapros.net',
  ev=[{'claim': 'About 页：veteran owned business…reached via email at info@cctvcamerapros.net；产品页 16 Port Network PoE Switch', 'quote': 'We can also be reached via email at info@cctvcamerapros.net', 'url': 'https://videos.cctvcamerapros.com/app-content/about.html'}],
  kp=[{'name': 'Mike Haldas', 'role': 'managing partner', 'source': 'https://www.cctvcamerapros.com/Contact-Us-s/1084.htm'}, {'name': 'Greg Bond', 'role': 'managing partner', 'source': 'https://www.cctvcamerapros.com/Contact-Us-s/1084.htm'}],
  q=Q_OEM)
j('XB-C0686', 'A', '首触', 'W03', '安防经销商平台（Nelly\'s Security，Broken Arrow/Tulsa OK；免费 Dealer Program + 空白产品贴牌 Branding Program；品类含 PoE switches）', '给经销商做贴牌 → 自身是白牌采购方（OEM 品牌商序列）', 'US 主战场、白牌采购、邮箱已补 → 升 A 首触，用自有标签问句（排 2027-01-20 周三）', kind='dist', to='customerservice@nellyssecurity.com',
  ev=[{'claim': 'Dealer Program 页：access to the Branding Program for free branding on the blank products you purchase from us；联系页 customerservice@nellyssecurity.com；leadiq：products including…PoE switches, networking tools', 'quote': 'As a Dealer, you get perks like competitive pricing, access to the Branding Program for free branding on the blank products you purchase from us', 'url': 'https://nellyssecurity.com/blogs/articles/nellys-dealer-program-faq-branding-shipping-and-more'}],
  kp=[{'name': 'Sean Nelson', 'role': 'Founder / Owner', 'source': 'https://www.linkedin.com/in/sean-nelson-63305619/'}],
  q=Q_OEM)
j('XB-C0585', 'A', '首触', 'W03', '安防进口分销（Eltrox Sp. z o.o.，Częstochowa；2003 起；零售品牌 Eltrox 30 家门店 + 批发品牌 Hurton；PZP Ochrona 会员）', '波兰头部安防进口商，批发平台 Hurton 面向安装商', 'PL 次重点、进口 + 批发、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist2', to='bok@hurton.pl',
  ev=[{'claim': 'PZP Ochrona：wiodący dystrybutor i importer systemów bezpieczeństwa w Polsce…rynku hurtowym pod marką Hurton…od 2003 r.；hurton.pl：wysłać e-maila na adres: bok@hurton.pl', 'quote': 'wiodący dystrybutor i importer systemów bezpieczeństwa w Polsce. Obecny na rynku detalicznym pod marką handlową Eltrox oraz na rynku hurtowym pod marką Hurton', 'url': 'https://pzpochrona.pl/firmy_zrzeszone/eltrox-sp-z-o-o/'}],
  kp=[{'name': 'Dariusz Kędzierski', 'role': 'Hurton 合作计划联系人（d.kedzierski@eltrox.pl）', 'source': 'https://hurton.pl/program-partnerski'}],
  q=Q_D2)

# ---- B 不动 ----
j('XB-C1077', 'B', '不动', typ='「IT made in Germany」网店（Brauns IT，Berlin 个体；Teltonika/Ubiquiti）', reason='「德国制造」定位与我方相悖 + 个体网店；info@it-made-in-germany.de 已记 → B 不动',
  ev=[{'claim': 'Impressum：IT made in Germany | Brauns IT Inh. Torsten Brauns…info@it-made-in-germany.de；Unternehmen 页：deutsche Hard- und Software…bündeln', 'quote': 'Wir haben es uns zur Aufgabe gemacht, deutsche Hard- und Software auf it-made-in-germany.de zu bündeln', 'url': 'https://it-made-in-germany.de/impressum/'}])
j('XB-C1079', 'B', '不动', typ='厂商自有 VAD（Dallmeier Components GmbH，Hamburg；Dallmeier 集团；18 人）', reason='制造商自营分销（只走 Dallmeier 全线）→ B 不动；info@d-components.com 已记',
  ev=[{'claim': 'Dallmeier 新闻稿：specialist installers in Germany…purchase components from…Dallmeier directly from the company\'s own distributor Dallmeier Components；Impressum info@d-components.com', 'quote': 'Dallmeier establishes own distribution in Germany', 'url': 'https://www.dallmeier.com/about-us/press-center/distribution-dallmeier-components'}])
j('XB-C1125', 'B', '不动', typ='IT 系统集成商 + 网店（MR Datentechnik Vertriebs- und Service GmbH，Nürnberg；1994 起；250–499 人）', reason='大型系统集成商，采购链长 → B 不动；info@mr-daten.de / shop@mr-daten.de 已记',
  ev=[{'claim': 'unternehmen24：Gründung 08.12.1994…Mitarbeiter 250-499；官网 Kontakt info@mr-daten.de；网店 Impressum shop@mr-daten.de', 'quote': 'MR Datentechnik Vertriebs- und Service GmbH Emmericher Strasse 13 90411 Nürnberg', 'url': 'https://www.mr-daten-shop.de/de/impressum'}],
  kp=[{'name': 'Helge Schön', 'role': 'Leitung Vertrieb', 'source': 'https://www.nik-nbg.de/netzwerk/mitglieder/mr-datentechnik-vertriebs-und-service-gmbh/'}])
j('XB-C1151', 'B', '不动', typ='消防报警分销（HON Security and Fire Distribution GmbH，Leverkusen；Esser/Notifier/Morley 授权分销）', reason='主营火灾报警，非网络渠道 → B 不动；info@fire-distribution.de 已记',
  ev=[{'claim': 'Facebook：einer der größten autorisierten Distributoren für Esser Brandmeldetechnik in Deutschland；Impressum info@fire-distribution.de，GF Sven Kniesche', 'quote': 'Wir sind einer der größten autorisierten Distributoren für Esser Brandmeldetechnik in Deutschland', 'url': 'https://fire-distribution.de/impressum/'}])
j('XB-C0805', 'B', '不动', typ='Cisco Premier Partner / 托管服务商（Re-solution Data Ltd，London；2–10 人；住房协会、智能楼宇）', reason='Cisco 系集成商，非分销 → B 不动；hello@re-solution.co.uk 已记',
  ev=[{'claim': '官网：Re-solution is a Cisco-certified partner…hello@re-solution.co.uk；LinkedIn 2–10 人、2015 起', 'quote': 'Security first Cisco Experts. Specialising in Cisco Networks, Security, Datacentre & Cloud', 'url': 'https://re-solution.co.uk/contact/'}])

# ---- C ----
j('XB-C0812', 'C', '不动', typ='非公司（「Premier Partners」= International Security Expo 的赞助商计划名，名下为 Smiths Detection/Abloy/Hirsch 等展商）', reason='来源库误把展会赞助计划当公司 → C 不动',
  ev=[{'claim': 'ISE 官网：Our Premier Partners Programme is for companies with stands over 48sqm', 'quote': 'Our Premier Partners Programme is for companies with stands over 48sqm', 'url': 'https://www.internationalsecurityexpo.com/premier-partners'}])
j('XB-C0657', 'C', '不动', typ='无法定位（「Advanced Tech Solutions」同名公司多家：加州 IT 采购 Adtecsol、南达科他 MSP、洛杉矶 Advanced Tech Supply 等）', reason='来源库条目无域名、无法唯一定位 → C 不动',
  ev=[{'claim': 'web_search 2026-10-28：同名至少 5 家，无一与 PoE/CCTV 渠道明确对应', 'quote': '', 'url': 'https://adtecsol.com/contact-us'}])

run(J, 'W3-R10', expect=12)
