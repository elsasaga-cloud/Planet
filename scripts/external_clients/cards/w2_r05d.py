# -*- coding: utf-8 -*-
"""波 2 R05 批 d：希腊 19 + 保加利亚 8 + 罗马尼亚 6 + 塞尔维亚 6 + 克罗地亚 2 + 斯洛文尼亚 2 + 斯洛伐克 3 + 立陶宛 3 + 拉脱维亚 3 + 爱沙尼亚 2 + 爱尔兰 3 + 塞浦路斯 3 + 马耳他 2 + 摩尔多瓦 2 + 波黑 1 + 北马其顿 2 + 阿尔巴尼亚 1 + 黑山 3 + 科索沃 2 + 冰岛 1 = 74。
小市场以轻卡为主；S 箱邮件核对：TELESYSTEM 来信为「Confirmare de primire」自动回执。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run, CONS, ATP

J = {}
def j(*a, **k): _j(J, *a, **k)
BIG = '大型广线/集团分销，决策链长 → B 慢慢跟进'
SMALL = '小市场小店、未核实 → B 慢慢跟进'
Q_DIST = 'Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?'
Q_IND = 'Would a second-source DIN-rail PoE switch be worth a test unit next to the industrial brands you carry?'
Q_FIRST = 'Would either line be relevant for your reseller customers, or is switching fully covered today?'

# ===== 希腊 19 =====
for c, t in (('XA-M011', '集成商/顾问（Systemcon）'), ('XA-M012', '培训机构（mikrotiktraining.gr）'), ('XA-M013', '顾问（GTA）'), ('XA-M015', '顾问（IME）'), ('XA-M115', '顾问（Exasolutions）'), ('XA-M116', '顾问（DSlab）'), ('XA-M118', '顾问（Alfa-tech）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M120', 'C', '不动', typ='个人顾问（仅 gmail）', reason='个人、无公司邮箱 → C')
j('XA-M014', 'A', '首触', 'W50', '希腊首家 MikroTik 分销（HellasCom Ltd.）', 'MikroTik 渠道源头', 'GR MikroTik 分销、未触达 → A 首触', kind='dist', q=Q_FIRST)
j('XA-M110', 'B', '不动', typ='ALLNET 集团希腊分公司（Allnet.Greece，邮箱在 allnet-italia.it）', reason='自有 ALLNET 品牌同行集团 → B')
j('XA-M111', 'A', '第二封', 'W50', '工业自动化分销（Alpha Motion S.A.，Athens；HMS/N-Tron 渠道）', '工业交换机品类现成', 'GR 工业分销 → 维持 A（轻卡，名录导入）', kind='ind', q=Q_IND)
j('XA-M112', 'A', '第二封', 'W50', '工业自动化代理（Automation Experts，Athens；Antaira 授权，覆盖希腊+塞浦路斯）', '工业交换机品类现成', 'GR 工业分销 → 维持 A', kind='ind', q=Q_IND)
j('XA-M113', 'A', '第二封', 'W50', '有线/无线网络专营网店（Cableworks，Argyroupoli；MikroTik 分类在售）', 'MikroTik 渠道', 'GR 网络渠道 → 维持 A', q=Q_DIST)
j('XA-M114', 'C', '并线', typ='= XA-M113 Cableworks（同集团同电话 e-Wireless）', reason='同集团并线 → C')
j('XA-M117', 'A', '第二封', 'W50', '网络设备网店（Hellas Digital，Glyfada）', 'MikroTik 渠道', 'GR 网络网店 → 维持 A（轻卡）', q=Q_DIST)
j('XA-M119', 'A', '第二封', 'W50', '电子/通信集团（MARAC Electronics S.A.，Perama；MikroTik 官方分销）', 'MikroTik 渠道，具名收件人', 'GR MikroTik 分销 → 维持 A',
  kp=[{'name': 'C. Pipitsoulis', 'role': '来源库具名邮箱（S 箱 10-08 收件人）', 'source': '来源库'}], q=Q_DIST)
j('XA-M121', 'A', '第二封', 'W50', 'MikroTik 官方分销（XPATIT S.A.，Attika）', 'MikroTik 渠道', 'GR MikroTik 分销 → 维持 A', q=Q_DIST)
j('XA-M489', 'B', '不动', typ='IT 集成商（Digital Sima S.A.）', reason=ATP)
j('XA-M490', 'B', '不动', typ='IT 集成商（LEXIS S.A.）', reason=ATP)
# ===== 保加利亚 8 =====
j('XA-M068', 'A', '第二封', 'W50', 'IT 分销（ASAP，Sofia；MikroTik 官方分销）', 'IT/网络分销', 'BG 分销 → 维持 A', kind='dist2',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
j('XA-M069', 'B', '不动', typ='IT 零售/网店（Computer Market，Burgas）', reason=SMALL)
j('XA-M070', 'A', '第二封', 'W50', 'MikroTik 专营网店（MTBG OOD / mikrotikbg.shop，Burgas）', 'MikroTik 渠道', 'BG MikroTik 专营 → 维持 A（轻卡）', q=Q_DIST)
j('XA-M071', 'B', '不动', typ='顾问（Digit Consult）', reason=CONS)
j('XA-M072', 'B', '不动', typ='IT 零售（PCLife，Plovdiv；订单邮箱）', reason=SMALL)
j('XA-M073', 'B', '不动', typ='网络公司（Riva Ltd，Burgas）', reason=SMALL)
j('XA-M074', 'B', '不动', typ='通信工程公司（Rootelsat / Vesuvius Streamline，Shumen）', reason='工程商非渠道 → B')
j('XA-M075', 'B', '不动', typ='顾问（Nebo Systems）', reason=CONS)
# ===== 罗马尼亚 6 =====
j('XA-E015', 'B', '不动', typ='大型系统集成商（Datanet Systems，București）', reason='大型 SI 非渠道；10-20 刚发未回 → B')
j('XA-M208', 'A', '第二封', 'W50', '安防/网络分销（Dipol Connect SRL，București；波兰 DIPOL 集团罗马尼亚公司）', '安防 + 网络分销', 'RO 分销 → 维持 A', kind='dist2',
  q='Which of the three would be worth a sample for your product team first - the 24-port entry PoE, the 24-port L2+, or the DIN-rail unit?')
j('XA-M209', 'A', '第二封', 'W50', 'MikroTik 分销（Netter System SRL / mikrotik.ro，Cristuru Secuiesc）', 'MikroTik 渠道', 'RO MikroTik 分销 → 维持 A', q=Q_DIST)
j('XA-M210', 'B', '不动', typ='顾问（New Vision）', reason=CONS)
j('XA-M211', 'A', '第二封', 'W50', 'MikroTik 分销（TELESYSTEM，Bacău / București / Iași）', 'MikroTik 渠道，三地门店', 'RO MikroTik 分销 → 维持 A',
  touch='S 箱 2026-10-09 群发「24 Port PoE Managed Switch」→ 来信为自动回执「Confirmare de primire」→ 视同已发未回', notes='来信核对：threads 显示 2 分钟后回「Confirmare de primire」，机器回执。', q=Q_DIST)
j('XA-M212', 'A', '第二封', 'W50', 'Ubiquiti/MikroTik 授权网店（Wifimag.ro，Tulcea；2007 起）', 'WISP 渠道', 'RO WISP 网店 → 维持 A（轻卡）', q=Q_DIST)
# ===== 塞尔维亚 6 =====
j('XA-M008', 'B', '不动', typ='讲师/网络架构师（Netis）', reason=CONS)
j('XA-M009', 'C', '不动', typ='个人（仅 gmail，无站点）', reason='个人 → C')
j('XA-M101', 'A', '第二封', 'W50', '网络设备商店（3NET，Vranje）', 'MikroTik 渠道', 'RS 网络渠道 → 维持 A（轻卡）', q=Q_DIST)
j('XA-M102', 'B', '不动', typ='顾问（routerboard.rs）', reason=CONS)
j('XA-M103', 'A', '第二封', 'W50', '监控 + 网络设备商（Pixel Network LLC，Novi Sad）', '安防 + 网络渠道', 'RS 渠道 → 维持 A（轻卡）', kind='dist2',
  q='Which would be worth a sample for your installer customers first - the 24-port entry PoE switch or the DIN-rail unit?')
j('XA-M336', 'B', '不动', typ='培训机构（MikroTik Trening Srbija）', reason=CONS)
# ===== 克罗地亚 / 斯洛文尼亚 / 斯洛伐克 =====
j('XA-M076', 'A', '第二封', 'W50', 'MikroTik 分销（LOST d.o.o.，Zagreb）', 'MikroTik 渠道', 'HR MikroTik 分销 → 维持 A', q=Q_DIST)
j('XA-M294', 'B', '不动', typ='顾问（Kerberos）', reason=CONS)
j('XA-M162', 'A', '第二封', 'W50', 'MikroTik 分销（PC H.AND d.o.o.，Trzin）', 'MikroTik 渠道', 'SI MikroTik 分销 → 维持 A', q=Q_DIST)
j('XA-M163', 'A', '第二封', 'W50', 'MikroTik 分销（PEC Sistemi / tehnox.si，Maribor）', 'MikroTik 渠道', 'SI MikroTik 分销 → 维持 A', q=Q_DIST)
j('XA-M160', 'B', '不动', typ='顾问（Alfac）', reason=CONS)
j('XA-M161', 'A', '首触', 'W50', 'MikroTik 分销（WESTech spol. s r.o.，Bratislava）', 'MikroTik 渠道', 'SK MikroTik 分销、未触达 → A 首触', kind='dist', q=Q_FIRST)
j('XA-M492', 'A', '第二封', 'W50', '电子元器件/工业分销（SOS electronic，Košice；Hirschmann 授权，中东欧覆盖）', '工业网络品类现成', 'SK 工业分销 → 维持 A', kind='ind', q=Q_IND)
# ===== 立陶宛 / 拉脱维亚 / 爱沙尼亚 =====
j('XA-M041', 'B', '不动', typ='培训机构（mikrotik-training.lt）', reason=CONS)
j('XA-M042', 'B', '不动', typ='顾问/小集成商（Magit）', reason=CONS)
j('XA-M207', 'B', '不动', typ='波罗的海最大 IT 广线分销（ACC Distribution UAB，Kaunas）', reason=BIG)
j('XA-M144', 'B', '不动', typ='零售网店（GoodStore，Daugavpils）', reason=SMALL)
j('XA-M145', 'A', '第二封', 'W50', '网络设备网店 + 顾问（NetPro SIA / nasstore.eu，Riga；全欧配送）', 'MikroTik 渠道，拉脱维亚唯一认证顾问在此', 'LV 网络渠道 → 维持 A', to='oleg@netpro.lv', hits_domain='netpro.lv', lead='Hi Oleg,',
  kp=[{'name': 'Oļegs Žakovs', 'role': 'MikroTik 认证顾问 / NetPro（S 箱 10-04 收件人）', 'source': 'MikroTik 顾问名录'}], q=Q_DIST)
j('XA-M146', 'C', '并线', typ='= XA-M145 NetPro SIA（同人）', reason='同公司并线 → C')
j('XA-M192', 'A', '第二封', 'W50', '无线链路/MikroTik/ISP 公司（Kernel AS，Tartu）', 'MikroTik 渠道', 'EE 渠道 → 维持 A（轻卡）', q=Q_DIST)
j('XA-M193', 'A', '第二封', 'W50', '专业 WiFi/光纤网络公司（Sonictest OÜ，Tartu）', 'MikroTik 渠道', 'EE 渠道 → 维持 A（轻卡）', lead='Hi Imre,',
  kp=[{'name': 'Imre', 'role': '来源库具名邮箱（S 箱 10-06 收件人）', 'source': '来源库'}], q=Q_DIST)
# ===== 爱尔兰 / 塞浦路斯 / 马耳他 =====
j('XA-M190', 'A', '第二封', 'W50', 'WISP 设备供应商（Irish Wireless，Co. Clare）', 'WISP 渠道', 'IE WISP 渠道 → 维持 A', q=Q_DIST)
j('XA-M191', 'A', '第二封', 'W50', 'MikroTik 分销（gCnTech Limited，Dublin）', 'MikroTik 渠道', 'IE MikroTik 分销 → 维持 A（轻卡）', lead='Hi Greg,',
  kp=[{'name': 'Greg', 'role': '来源库具名邮箱（S 箱 10-09 收件人）', 'source': '来源库'}], q=Q_DIST)
j('XA-M505', 'B', '不动', typ='Perle 授权分销/集成（Infinite Technology）', reason='未核实规模、10-01 已发未回 → B 待核')
j('XA-E016', 'B', '不动', typ='IT 分销（MCS IT Distribution Ltd.，Cyprus；Edgecore 分销）', reason='仅有 reorganization@ 异常地址，未触达 → B 待补地址')
j('XA-M104', 'A', '首触', 'W50', 'MikroTik 分销（Cy-Wireless / art2soft）', 'MikroTik 渠道', 'CY MikroTik 分销、未触达 → A 首触', kind='dist', q=Q_FIRST)
j('XA-M105', 'A', '第二封', 'W50', 'MikroTik 分销（MS Electronics Ltd，Limassol）', 'MikroTik 渠道', 'CY MikroTik 分销 → 维持 A（轻卡）',
  kp=[{'name': 'Pieris', 'role': '来源库具名邮箱（S 箱 10-08 收件人）', 'source': '来源库'}], q=Q_DIST)
j('XA-M061', 'A', '第二封', 'W50', 'MikroTik 分销 + 马耳他唯一认证顾问（Nexus Networks）', 'MikroTik 渠道', 'MT MikroTik 分销 → 维持 A（轻卡）', to='johann@nexus.com.mt', lead='Hi Johann,',
  kp=[{'name': 'Johann', 'role': 'MikroTik 认证顾问（S 箱 10-04 收件人）', 'source': 'MikroTik 顾问名录'}], q=Q_DIST)
j('XA-M290', 'B', '不动', typ='MikroTik 转售（WST Systems Ltd，Birkirkara）', reason=SMALL)
# ===== 摩尔多瓦 / 波黑 / 北马其顿 / 阿尔巴尼亚 / 黑山 / 科索沃 / 冰岛 =====
j('XA-M158', 'C', '不动', typ='个人顾问（mail.ru）', reason='个人、非公司邮箱 → C')
j('XA-M159', 'C', '不动', typ='个人软件开发者（mail.ru，无站点）', reason='个人 → C')
j('XA-M189', 'B', '不动', typ='顾问（Wirac，波黑）', reason=CONS)
j('XA-M092', 'B', '不动', typ='网络设备商（ALL4NET DOOEL，Skopje；邮箱域不一致）', reason='地址不一致、未触达 → B 待补')
j('XA-M093', 'B', '不动', typ='监控 + 网络设备商（Treco，Skopje）', reason='区域外围、小 → B')
j('XA-M060', 'C', '不动', typ='个人顾问（router.al，gmail）', reason='个人 → C')
j('XA-M291', 'B', '不动', typ='顾问（Core-Bridge，黑山）', reason=CONS)
j('XA-M292', 'B', '不动', typ='网络设备商（Netmont DOO，Bar；邮箱域不一致）', reason='地址不一致、未触达 → B 待补')
j('XA-M293', 'B', '不动', typ='网络设备网店 + B2B 门户（RIDMONT，Podgorica）', reason='区域外围、小 → B')
j('XA-M205', 'B', '不动', typ='网络设备商（H2 Holding / fortshpejt.com，Prishtina）', reason='区域外围、小 → B')
j('XA-M206', 'B', '不动', typ='技术产品商店（KosProd，Fushë Kosovë）', reason='区域外围、小 → B')
j('XA-M077', 'A', '第二封', 'W50', 'MikroTik 分销（Öruggt Net ehf / Secure Net，Reykjavik）', 'MikroTik 渠道', 'IS MikroTik 分销 → 维持 A（轻卡）', q=Q_DIST)

run(J, 'W2-R05d', expect=74)
