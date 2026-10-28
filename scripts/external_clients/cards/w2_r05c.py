# -*- coding: utf-8 -*-
"""波 2 R05 批 c：法国 35 + 西班牙 24 + 葡萄牙 11 = 70。web_search 9 家（Ubitech / AiRiCOM / PEDAB / Ditecom / Noriak / Equipages / Databox / Connect Data / HD Technology）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run, CONS, ATP

J = {}
def j(*a, **k): _j(J, *a, **k)
BIG = '大型广线/集团分销，决策链长 → B 慢慢跟进'

# ===== 法国 35 =====
j('XA-C0004', 'A', '首触', 'W49', '安防电商分销（Ubitech SARL，Plaisir 78；2014 起，Hikvision/Dahua/Ajax/TP-Link VIGI 官方 e-distributeur，Ubitech Business 面向安装商含网络与布线）', '安防分销，PoE 配摄像机', 'FR 安防分销、未触达 → A 首触', kind='dist2',
  notes='本轮 web_search：ubitech.fr/content/4-a-propos「1er e-distributeur européen de produits Hikvision」；ubitech-business.com 面向安装商。',
  q='Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?')
j('XA-C0014', 'B', '不动', typ='视频监控安装服务商（2IIBM Tech）', reason='安装商非渠道 → B')
j('XA-E003', 'B', '不动', typ='SI/VAR（Celeris Informatique）', reason='SI 非渠道；10-19 刚发未回 → B')
j('XA-E014', 'C', '并线', typ='= XA-M169 ALLNET France（同公司，Edgecore 库重复）', reason='同公司并线 → C')
j('XA-M169', 'B', '不动', typ='ALLNET 集团法国分销（ALLNET France SAS，Carcassonne；MikroTik/Edgecore 分销）', reason='自有 ALLNET 品牌同行集团 → B')
j('XA-M032', 'A', '首触', 'W49', '工业网络/IIoT 分销（AiRiCOM，Boufféré 85 + Paris；N-Tron/Advantech/Terz 工业交换机法国备货，Moxa 渠道伙伴）', '工业交换机品类现成', 'FR 工业网络分销、未触达 → A 首触', kind='ind', to='marketing@airicom.fr',
  notes='本轮 web_search：airicom.com「Airicom : votre spécialiste des Switches industriels en France … Advantech, N-Tron et Terz」。仅公开 marketing@，首封请其转采购。',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to the industrial switches you stock?')
j('XA-M168', 'A', '第二封', 'W49', '电信/ISP 渠道增值分销（ACTN，Tournefeuille/Toulouse；MikroTik 官方分销）', '运营商/ISP 渠道，交换机已是品类', 'FR 电信渠道 VAD → 维持 A（优先）', kind='dist2',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
j('XA-M170', 'A', '首触', 'W49', '工业自动化分销（APLUS Systeme Automation；ORing 授权）', '工业交换机品类现成', 'FR 工业分销、未触达 → A 首触（轻卡，名录导入）', kind='ind',
  q='Would a second-source DIN-rail PoE switch be worth a test unit next to your ORing range?')
j('XA-M171', 'A', '首触', 'W49', 'MikroTik 专营 B2B 网店（Azurtem Shop，Nice；CRS 在售）', 'MikroTik 渠道，交换机已是品类', 'FR MikroTik 渠道、未触达 → A 首触', kind='dist',
  q='Would either line be relevant for your business customers, or is switching fully covered today?')
j('XA-M172', 'A', '首触', 'W49', 'MikroTik 官方分销（EDOX SAS，Burnhaupt-le-Haut 68）', 'MikroTik 渠道', 'FR MikroTik 分销、未触达 → A 首触', kind='dist',
  q='Would either line be relevant for your reseller customers, or is switching fully covered today?')
j('XA-M173', 'B', '不动', typ='N-Tron 渠道名录导入（FGET International；仅 gmail 地址）', reason='未核实、地址弱 → B')
j('XA-M174', 'A', '第二封', 'W49', '电信/IT 渠道分销（Convergence Direct / Groupe Convergence SAS，Thouars 79）', '电信渠道分销', 'FR 渠道分销 → 维持 A', kind='dist2',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
j('XA-M175', 'A', '首触', 'W49', 'MES 软件商兼工业硬件分销（HD Technology，Bron/Lyon；30 年，Red Lion/N-Tron 官方分销，store.hdtechnology.com）', '工业交换机品类现成', 'FR 工业分销、未触达 → A 首触（轻卡）', kind='ind',
  notes='本轮 web_search：redlion.net/fr/distributeurs/technologie-hd；store.hdtechnology.com/red-lion。',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to the industrial switches you list?')
j('XA-M176', 'A', '第二封', 'W49', '无线网络专营分销（MHz Wireless / mhzshop.com，Marquixanes 66；MikroTik/Ubiquiti/Netonix）', 'WISP 渠道', 'FR WISP 分销 → 维持 A',
  q='Would a DIN-rail PoE line be relevant for your WISP customers next to the outdoor switches you carry?')
j('XA-M300', 'C', '并线', typ='= XA-M176 MHz Wireless（同站 mhzshop.com，Netonix 名录重复）', reason='同公司并线 → C')
j('XA-M177', 'A', '第二封', 'W49', 'MikroTik 分销（Netcom Group，Pantin 93）', 'MikroTik 渠道', 'FR MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M178', 'B', '不动', typ='企业 WiFi/网络/电话集成商（NFTECH - WiFi France，Metz）', reason='集成商非渠道 → B')
j('XA-M179', 'B', '不动', typ='露营地 WiFi 运营商（Osmozis S.A.，Clapiers）', reason='运营商/终端用户型，非渠道 → B')
j('XA-M180', 'B', '不动', typ='小型 MikroTik 转售商（Redvise，Paris，瑞典系）', reason='小、未核实 → B')
j('XA-M181', 'B', '不动', typ='电信运营商/白标电信批发（Sewan，Paris）', reason='运营商非交换机渠道 → B')
j('XA-M182', 'A', '第二封', 'W49', 'MikroTik 分销（Vodenn SAS，La Farlède 83）', 'MikroTik 渠道', 'FR MikroTik 分销 → 维持 A（轻卡）',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M337', 'B', '不动', typ='MSP（Evelem）', reason=ATP)
for c, n in (('XA-M419', 'BlueBearsIT'), ('XA-M420', 'CFI France'), ('XA-M421', 'Delta Sertec'), ('XA-M422', 'Groupe Networks'), ('XA-M423', 'GTD International'), ('XA-M424', 'ITNI'), ('XA-M425', 'NXO France（大型集成商）'), ('XA-M426', 'Synexie')):
    j(c, 'B', '不动', typ='IT 集成商/VAR（%s）' % n, reason=ATP)
j('XA-M495', 'A', '第二封', 'W49', '进口分销商（Noriak Distribution / Micro Tech Distribution SAS，Cesson-Sévigné 35；2006 起，20–49 人，6 名外勤销售；Noriak Réseau 3,500 个网络/工业网络/监控 SKU）', '进口 + 分销，网络与工业网络品类现成', 'FR 进口分销商、规模对口 → 维持 A（优先）', kind='dist2',
  notes='本轮 web_search：noriak-distri.com「importation et distribution … produits réseaux」；pappers 20–49 人；noriak-reseau.com「réseau industriel … switches」。',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
j('XA-M496', 'A', '首触', 'W49', '电信/网络进口分销（Connect Data – Sintel，Bièvres 91；1981 起，约 20 人，年销约 1,500 万欧，面向运营商/集成商/转售商；Perle/Teltonika/Ruckus 等，含一家台系交换机品牌）', '进口分销，交换机品类现成', 'FR 进口分销商、未触达 → A 首触（优先）', kind='dist2', to='sales@connectdata.fr',
  notes='本轮 web_search：connectdata.fr/societe「importation et distribution de solutions pour les Infrastructures Réseaux」「une vingtaine de personnes … CA d\'environ 15 millions」。',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
j('XA-M497', 'B', '不动', typ='系统集成商/MSP（Equipages，Voisins-le-Bretonneux；20–49 人，三地分支）', reason='集成商非渠道 → B', notes='本轮 web_search：equipages.fr「intégrateur système, réseau et sécurité」。')
j('XA-M498', 'B', '不动', typ='企业 IT 基础设施 VAD（Pedab France，Paris；IBM/ALE/Nokia，瑞典 Pedab 集团）', reason='高接触型企业 VAD，商品交换机不对口 → B', notes='本轮 web_search：pedab.fr；Christine Berthon 为法国负责人（S 箱 9-28 已发未回）。')
j('XA-M499', 'A', '首触', 'W49', '工业网络官方分销（Sphinx France / Sphinx Connect；Moxa 与 Advantech 法国官方分销，25 年，12,000 SKU 备货）', '工业交换机品类现成', 'FR 工业分销、未触达 → A 首触', kind='ind', to='sales@sphinxfrance.fr',
  notes='本轮 web_search：sphinxfrance.com/marques/moxa「distributeur officiel de Moxa en France」。与德/意 Sphinx 同系不同法人。',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to your Moxa range?')
# ===== 西班牙 24 =====
j('XA-C0005', 'B', '不动', typ='全球安防分销西班牙分公司（ADI Global Spain；订单邮箱）', reason=BIG)
for c, t in (('XA-M057', '酒店 WiFi SaaS/顾问（Hotelinking）'), ('XA-M058', '顾问（Hecnys）'), ('XA-M059', '顾问公司（Celenet）'), ('XA-M274', '顾问（adrnet）'), ('XA-M277', '顾问/讲师（Lanpixel）'),
             ('XA-M280', '小集成商（Perpi.tech）'), ('XA-M282', '顾问（IT Consultores）'), ('XA-M283', '顾问（Dualcom）'), ('XA-M284', '顾问（Codisats）'), ('XA-M287', '顾问（Ibersystems）'), ('XA-M288', '顾问/讲师（Strato Networks）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M278', 'C', '不动', typ='个人顾问（仅 gmail，无站点）', reason='个人、无公司 → C')
j('XA-M289', 'C', '不动', typ='个人讲师（cursos-mikrotik.com，仅 hotmail）', reason='个人、无公司 → C')
j('XA-M275', 'A', '首触', 'W49', '无线/网络专营网店 + 分销（CiudadWireless，Madrid）', 'MikroTik 渠道', 'ES MikroTik 渠道、未触达 → A 首触', kind='dist',
  q='Would either line be relevant for your reseller customers, or is switching fully covered today?')
j('XA-M276', 'B', '不动', typ='大型广线 IT 分销（DMI Computer，Madrid）', reason=BIG)
j('XA-M279', 'B', '不动', typ='小型电子仪器设计/分销网店（Ditecom Design SL，Madrid；在售 1 款工业交换机）', reason='小店 → B', notes='本轮 web_search：ditecom.com 工业交换机类目仅 ISW-801。')
j('XA-M281', 'B', '不动', typ='大型广线 IT 分销（Infortisa，Valencia）', reason=BIG)
j('XA-M285', 'A', '首触', 'W49', '无线网络分销（Laufquen Comunicaciones，Alcorcón/Madrid；Ubiquiti/MikroTik）', 'WISP/无线渠道', 'ES 无线分销、未触达、KP 实名 → A 首触', kind='dist', to='fernando.novoa@laufquen.com', lead='Hi Fernando,',
  kp=[{'name': 'Fernando Novoa', 'role': '官网公开商务联系人', 'source': '来源库官网核对'}],
  q='Would either line be relevant for your wireless customers, or is switching outside what Laufquen stocks?')
j('XA-M286', 'B', '不动', typ='电信系统集成商（Leadernet Sistemas，N-Tron 渠道名录导入）', reason='未核实为分销 → B')
j('XA-M326', 'B', '不动', typ='大型电气/安防/自动化分销集团（Berdin Grupo）', reason=BIG)
j('XA-M327', 'B', '不动', typ='VoIP/网络集成商（DeInta，Zaragoza）', reason=ATP)
j('XA-M328', 'C', '不动', typ='秘鲁批发分销（Nexus Technology，nexus.com.pe；误归西班牙）', reason='区域外（南美）→ C；误归属')
j('XA-M468', 'B', '不动', typ='布线/电气集成商（Líneas y Cables S.A.）', reason=ATP)
# ===== 葡萄牙 11 =====
j('XA-M055', 'A', '第二封', 'W49', '工业方案/分销（AGL Industrial Solutions / Guedes Lopes，Porto Salvo；Antaira 官方名录分销）', '工业交换机品类现成', 'PT 工业分销 → 维持 A', kind='ind',
  q='Would a second-source DIN-rail PoE switch be worth a test unit next to your Antaira range?')
for c, t in (('XA-M056', '酒店/多住户网络顾问（MiniMeLabs）'), ('XA-M270', 'ICT 集成商（Sinaltech）'), ('XA-M271', '顾问（Engenheiros.pt）'), ('XA-M334', '培训伙伴（NetHighTech，仅 gmail）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M333', 'C', '并线', typ='= XA-M271（同人同邮箱 camacho@engenheiros.pt）', reason='重复 → C 并线')
j('XA-M272', 'A', '首触', 'W49', 'MikroTik 分销（Officelan，Canas de Senhorim）', 'MikroTik 渠道', 'PT MikroTik 分销、未触达 → A 首触', kind='dist',
  q='Would either line be relevant for your reseller customers, or is switching fully covered today?')
j('XA-M273', 'A', '第二封', 'W49', 'MikroTik 分销（Truenet，Lisboa）', 'MikroTik 渠道', 'PT MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M487', 'B', '不动', typ='布线/光纤集成商（C2F Copper2Fiber）', reason=ATP)
j('XA-M488', 'B', '不动', typ='葡萄牙最大 IT 广线分销之一（Databox Informática S.A.，Massamá；约 140 人、年销约 8,000 万欧，TP-Link/Hikvision/Huawei eKit 分销，100% 渠道）', reason=BIG + '；将来可作 OEM 品类谈，先慢跟', notes='本轮 web_search：intel partner showcase「about 140 people … more than 80 million Euros」。')
j('XA-M504', 'B', '不动', typ='Perle 授权分销/集成（DSSI，Agualva-Cacém）', reason='未核实规模、10-01 已发未回 → B 待核')

run(J, 'W2-R05c', expect=70)
