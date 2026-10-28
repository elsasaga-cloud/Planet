# -*- coding: utf-8 -*-
"""波 3 R07：R06「邮箱待补」补查第一批 12 户（美 4 / 加 1 / 英 2 / 波 2 / 法 2 / 土 1）。查到公开销售邮箱且渠道对口 → A 首触；仍无邮箱或定位不符 → B 不动（邮箱已记）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run

J = {}
def j(*a, **k): _j(J, *a, **k)
Q_IND = 'Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to the industrial brands you carry?'
Q_D2 = 'Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?'
Q_D2S = 'Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?'

# 美国 / 加拿大（周三 2027-01-13）
j('XB-C0128', 'A', '首触', 'W02', '安防摄像机制造 + 分销（Rugged Cams / Rugged CCTV，Kemp TX；1993 起；11–50 人；自有品牌 RuggedCams；也卖高功率 PoE 交换机；店主 Allen Spears）', '自有品牌商，PoE 交换机是其配套品类 → 自有标签对口', 'US 自有品牌 + 分销、邮箱已补 → 升 A 首触（排 2027-01-13 周三）', kind='dist2', to='sales@rugged-cctv.com',
  kp=[{'name': 'Allen Spears', 'role': 'Owner（BBB）', 'source': 'https://www.bbb.org/us/tx/kemp/profile/security-cameras/rugged-cctv-1075-23000633'}],
  ev=[{'claim': '官网：Rugged Cams is a Manufacturer and Distributor of digital security equipment…since 1993；sales@rugged-cctv.com；有 Long Distance High Power PoE Switches 页', 'quote': 'Rugged Cams is a Manufacturer and Distributor of digital security equipment located near Dallas, Texas', 'url': 'https://www.rugged-cctv.com/about-us/'}],
  q='Would a PoE switch line under your RuggedCams label be worth a sample, and who on your product team should see the spec sheets?')
j('XB-C0561', 'A', '首触', 'W02', '工业自动化服务 + 分销（Complete Control Solutions LLC，Lebanon PA；2010 起；约 8 人；2026 起 Antaira 授权分销、Invertek 分销；服务宾州/中大西洋工业客户；合伙人 Dan Kaiser）', '刚开始做工业以太网分销 → 第二来源切入窗口', 'US 小型工业分销、邮箱已补 → 升 A 首触（轻，排 2027-01-13 周三）', kind='ind', to='info@ccs-automation.com',
  kp=[{'name': 'Dan Kaiser', 'role': 'Managing Member（buzzfile / LinkedIn）', 'source': 'https://www.linkedin.com/in/dan-kaiser-b4356651/'}],
  ev=[{'claim': '官网：CCS is an Antaira Authorized Distributor serving Pennsylvania and the Mid-Atlantic with industrial Ethernet switches；info@ccs-automation.com', 'quote': 'Complete Control Solutions is an Antaira Authorized Distributor serving manufacturers and industrial operators throughout Pennsylvania and the surrounding Mid-Atlantic region', 'url': 'https://ccs-automation.com/complete-control-solutions-is-now-an-antaira-authorized-distributor'}],
  q=Q_IND)
j('XB-C0757', 'A', '首触', 'W02', '无线/网络增值分销（Streakwave Wireless, Inc.，San Jose CA；2005 起；圣何塞/盐湖城/辛辛那提 + 澳新；MikroTik/Ubiquiti/Cambium；服务 ISP/集成商/企业；总裁 Carl Moberg）', 'MikroTik/Ubiquiti 渠道 → SmartByte 商用 L2+ 对口', 'US 网络 VAD、邮箱已补 → 升 A 首触（排 2027-01-13 周三）', kind='dist', to='contact@streakwave.com',
  kp=[{'name': 'Carl Moberg', 'role': 'President（buzzfile / OpenCorporates agent）', 'source': 'https://www.buzzfile.com/business/Streakwave-Wireless,-Inc.-408-294-8415'}],
  ev=[{'claim': '招聘页：Since 2005…go-to distributor for ISPs, integrators, and enterprises…MikroTik, Ubiquiti, Cambium；Crunchbase contact@streakwave.com', 'quote': 'We carry the industry’s top brands — MikroTik, Ubiquiti, Cambium, and many more — with deep technical expertise and real inventory', 'url': 'https://employment.streakwave.com/'}],
  q=Q_D2)
j('XB-C0566', 'A', '首触', 'W02', '工业自动化/网络分销（Manufacturers Automation Inc. / ManuAuto，St. Jacobs + Concord ON；40 年+；Moxa 加拿大最大备货分销、Robustel/Weidmüller/Proxim；MTSC 认证工程师）', 'Moxa 加拿大主分销 → 工业线低价第二来源', 'CA 工业分销、邮箱已补 → 升 A 首触（排 2027-01-13 周三）', kind='ind', to='sales@manuauto.com',
  ev=[{'claim': '官网 Line Card：As Moxa’s authorized partner and the largest stocking distributor in Canada；sales@manuauto.com', 'quote': 'ManuAuto is a leading Distributor of Industrial Automation, Networking, and Data Communication Products specializing in Industrial Ethernet Switches', 'url': 'https://www.manuauto.com/index.php?route=information/contact'}],
  q=Q_IND)
j('XB-C0129', 'B', '不动', typ='IT 服务 + GSA 联邦经销（ZDAAS LLC，Glen Burnie MD；女性所有小企业；软件/人力 + 线缆/摄像机/交换机转售）', reason='联邦采购渠道（需 TAA 等资质）与 Saga 条件不符；info@zd-techsolutions.com 已记 → B 不动',
  ev=[{'claim': 'GSA eLibrary 列 ZDAAS LLC 合同 47QTCA18D008G；Thomasnet：distributor of cables, amplifiers, cameras…switches, routers', 'quote': 'Permanent and temporary industrial staffing, software…Also distributor of cables, amplifiers, cameras, computers', 'url': 'https://www.thomasnet.com/company/zdaas-llc-30917176/profile'}])
# 英国（周四 2027-01-21）
j('XB-C0534', 'A', '首触', 'W03', '消防安防批发（ISET UK Fire & Security Distribution Ltd，Nottingham；Hikvision 授权批发；仅对贸易客户）', 'Hikvision 批发，PoE 配套', 'GB 安防批发、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist2', to='sales@iset-uk.co.uk',
  ev=[{'claim': '官网：ISET UK are an Authorised Hikvision Wholesaler…email sales@iset-uk.co.uk；TRADE-ONLY SUPPLIER', 'quote': 'ISET UK are an Authorised Hikvision Wholesaler and are leaders in the UKs security industry', 'url': 'https://www.iset-uk.co.uk/blog/a-guide-to-hikvision-cctv-cameras/'}],
  q=Q_D2S)
j('XB-C0538', 'B', '不动', typ='企业电信/IT 服务商（Birmingham Telecommunications Ltd，Coleshill；2006 起；11–50 人；3CX/托管话音/宽带/Ubiquiti 安装）', reason='MSP/电信服务商，不是分销；info@birminghamtelecom.co.uk 已记 → B 不动',
  ev=[{'claim': 'LinkedIn：Hosted Telephony Specialists - 3CX Platinum Partner…Ubiquiti WiFI Installation；11–50 人', 'quote': 'Hosted Telephony Specialists - 3CX Platinum Partner - SIP Trunking Integrator', 'url': 'https://uk.linkedin.com/company/birmingham-telecommunications-limited'}])
# 波兰（周四 2027-01-21）
j('XB-C0589', 'A', '首触', 'W03', '安防分销（Vidicon Sp. z o.o.，Warsaw + Wrocław；CROW/INIM/ELECTRA 波兰独家分销；报警 + CCTV + 空调）', '独家分销多个欧洲品牌，PoE 配套', 'PL 安防分销、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist2', to='handlowy@vidicon.pl',
  ev=[{'claim': '官网联系页 dział handlowy: elektronika: handlowy@vidicon.pl；自述 Wyłączny dystrybutor produktów firm CROW, INIM, ELECTRA na Polskę', 'quote': 'Dostawca systemów alarmowych i telewizji przemysłowej. Wyłączony dystrybutor produktów firm CROW, INIM, ELECTRA na Polskę.', 'url': 'https://www.vidicon.pl/en/contact'}],
  q=Q_D2S)
j('XB-C0144', 'A', '首触', 'W03', '安防进口分销（Janex International Sp. z o.o.，Warsaw；1992 起；CCTV/报警/消防/门禁进口商 + 分销；B2B 平台；培训/设计支持）', '进口商 + 全国分销 → 对直接从厂家采购有经验', 'PL 进口分销、邮箱已补 → 升 A 首触（排 2027-01-21 周四）', kind='dist2', to='janex@janexint.com.pl',
  ev=[{'claim': '目录页：Janex International jest importerem i dystrybutorem urządzeń technicznej ochrony mienia m.in. telewizji dozorowej CCTV；官网 janex@janexint.com.pl', 'quote': 'Janex International jest importerem i dystrybutorem urządzeń technicznej ochrony mienia m.in. telewizji dozorowej CCTV, systemów alarmowych', 'url': 'http://www.katalog.ochrona-mienia.pl/firma-36.html'}],
  q=Q_D2S)
# 法国
j('XB-C0892', 'B', '不动', typ='安防设备分销/网店（Eclats Antivols，Toulouse centre de gros；1989 起；自述产品均为法国/欧洲制造）', reason='定位「法国/欧洲制造」与中国货源相悖；contact@eclats-antivols.fr 已记 → B 不动',
  ev=[{'claim': 'rfqmatch 简介：All equipment offered is manufactured in France and Europe；infonet 列 contact@eclats-antivols.fr', 'quote': 'All equipment offered is manufactured in France and Europe, ensuring superior quality', 'url': 'https://www.rfqmatch.com/listing/b1e7300e-d3c5-41e1-8e49-7fb6aa43af77'}])
j('XB-C0903', 'B', '不动', typ='安防电子批发 + 集成（SSI Systèmes，Oissel/Rouen；Groupe GTC France；Hikvision/EATON 伙伴；仅电话/表单）', reason='对口但无公开邮箱（官网仅表单与电话）→ B 不动，下一轮 LinkedIn 补',
  ev=[{'claim': '官网：Grossiste Distributeur Concepteur Intégrateur de systèmes électroniques de Sécurité；联系方式仅 02 35 03 04 50 + 表单', 'quote': 'Grossiste Distributeur de systèmes électroniques de Sécurité - Sûreté, nous accompagnons les installateurs sur leurs projets courant faible', 'url': 'https://www.ssi-systemes.fr/'}])
# 土耳其（周四 2027-01-14）
j('XB-C0508', 'A', '首触', 'W02', '网络增值分销（Simet Bilişim Teknolojileri A.Ş.，Ankara；1997 起；约 9 人；BDCOM 土耳其分销、Linksys 分销；网络安全/通信产品 VAD）', '已代理中国交换机品牌 BDCOM → 可加第二条', 'TR 主战场、网络 VAD、邮箱已补 → 升 A 首触（排 2027-01-14 周四）', kind='dist', to='satis@simet.com.tr',
  ev=[{'claim': '官网：SIMET BDCOM DISTRIBUTOR OF TURKEY；Facebook 页 satis@simet.com.tr；contactout 1–10 人', 'quote': 'Simet combines its paths with BDCOM that is supplier of a networking technologies and communications solutions', 'url': 'https://simet.com.tr/index.cfm?cid=5965&fuseaction=objects2.detail_content'}],
  q=Q_D2)

run(J, 'W3-R07', expect=12)
