# -*- coding: utf-8 -*-
"""波 2 R05 批 a：荷兰 27 + 比利时 6 + 瑞典 13 + 丹麦 6 + 芬兰 6 + 挪威 4 = 62。web_search 5 家（FiberUnlimited / Kappa Data / JPK / Lextron / Foxconcept）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run, CONS, ATP

J = {}
def j(*a, **k): _j(J, *a, **k)

# ===== 荷兰 27 =====
j('XA-C0001', 'A', '首触', 'W48', '欧洲 B2B 安防批发（JBN Security Systems B.V.）', '安防批发，PoE 配摄像机', 'NL 安防批发、未触达 → A 首触', kind='dist2',
  q='Which of the three would be worth a sample for your product team first - the 24-port entry PoE, the 24-port L2+, or the DIN-rail unit?')
j('XA-E002', 'B', '不动', typ='开放硬件/OCP 方案商（Circle B，Taurus Group）', reason='数据中心方案商非渠道；10-19 刚发未回 → B（将来可谈 CENTEC）')
j('XA-E027', 'B', '不动', typ='塑料光纤（POF）楼宇网络方案商/厂商（FiberUnlimited，Amersfoort，11–50 人；Edgecore 转售伙伴）', reason='自有 POF 产品的方案商，非分销 → B', notes='本轮 web_search 复核：fiberunlimited.com「Halonex® network… reseller partner of EdgeCore」。')
for c, t in (('XA-M053', 'MikroTik 讲师（MyNetworkTraining）'), ('XA-M062', '顾问（GPE Networks）'), ('XA-M063', '顾问（IP Techniek）'), ('XA-M255', 'DAEL 内 MikroTik 顾问'), ('XA-M258', '顾问（Qtopia）'),
             ('XA-M259', '顾问（Dside）'), ('XA-M262', '讲师/WISP（Libernet）'), ('XA-M263', '顾问（Connection Services，占位站）'), ('XA-M264', '培训机构（MikroTrain，Zwolle）'), ('XA-M265', '顾问（RvdB ICT）'), ('XA-M268', '顾问（MNW）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M261', 'C', '并线', typ='= XA-M062 GPE Networks（同人同邮箱）', reason='重复 → C 并线')
j('XA-M254', 'C', '并线', typ='= XA-M267 SDC Group（Aris Vink 为其售前顾问/讲师，记为 KP）', reason='同公司并线 → C')
j('XA-M335', 'C', '并线', typ='= XA-M267 SDC Group（SDC B.V. 同公司）', reason='同公司并线 → C')
j('XA-M267', 'A', '第二封', 'W47', 'MikroTik Value Added Master Distributor（SDC Group / SDC B.V.，Doetinchem；培训伙伴）', 'NL 的 MikroTik 主分销，售前顾问实名', 'NL MikroTik Master Distributor → 维持 A（优先）', lead='Hi Aris,', to='aris@sdc.nl', hits_domain='sdc.nl',
  kp=[{'name': 'Aris Vink', 'role': '售前顾问 / MikroTik 认证讲师（S 箱 10-05 收件人）', 'source': 'MikroTik 顾问名录 / 来源库'}],
  q='Would a DIN-rail PoE line be something your dealers ask for next to the MikroTik range, or is that segment already covered?')
j('XA-M054', 'A', '第二封', 'W47', '工业数据通信分销（Modelec Data-Industrie；Westermo 官方名录 reseller，全套技术支持）', '工业交换机品类现成', 'NL 工业数据通信分销 → 维持 A',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to your Westermo range?')
j('XA-M256', 'A', '第二封', 'W47', 'MikroTik 分销（Interstroom，Hengelo）', 'MikroTik 渠道', 'NL MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M257', 'B', '不动', typ='一人公司（JPK Consulting，Zwolle；休闲园区 WiFi/网络，MikroTik reseller）', reason='一人公司、小 → B', notes='本轮 web_search 复核：KvK 74263684 eenmanszaak。')
j('XA-M260', 'A', '第二封', 'W47', '工业计算机与通信供应商（Lextron B.V.，Dongen，1–10 人；ORing 官方 dealer NL/BE）', '已卖 ORing 工业交换机，STI 第二供应商', 'NL 工业网络渠道 → 维持 A',
  notes='本轮 web_search 复核：lextron.nl「officiële ORing dealer in Nederland en België」；KvK 50778471。',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to your ORing range?')
j('XA-M266', 'A', '第二封', 'W47', '路由器/交换机专业网店（Routershop.nl，Utrecht，20+ 年）', '交换机专类电商', 'NL 交换机专业电商 → 维持 A',
  q='Would a DIN-rail PoE range be worth listing for your business customers, or is Routershop focused on indoor gear?')
j('XA-M269', 'A', '首触', 'W48', '无线数据通信网店（Wimood，Goedereede；Ubiquiti/MikroTik）', 'WISP 渠道', 'NL WISP 渠道、未触达 → A 首触（网店，权重中）', kind='dist',
  q='Would either line be relevant for your wireless customers, or is switching outside what Wimood stocks?')
j('XA-M469', 'B', '不动', typ='IT 集成商（Avelution）', reason=ATP)
j('XA-M470', 'C', '并线', typ='= XA-M472 Kappa Data（集团荷兰分公司，Utrecht）', reason='集团并线 → C')
j('XA-M471', 'B', '不动', typ='IT 集成商（Pijl Solutions）', reason=ATP)
# ===== 比利时 6 =====
j('XA-E001', 'B', '不动', typ='技术型 SI/网络咨询（Deca Consulting；Edgecore/STORDIS 合作）', reason='SI 非渠道；10-19 刚发未回 → B（将来可谈 CENTEC）')
j('XA-M164', 'B', '不动', typ='小型 IT 服务商（Foxconcept，Tongrinne，4 人；MikroTik reseller + KomShine 光纤工具独家分销）', reason='小 IT 服务商 → B', notes='本轮 web_search 复核：companyweb 4.1 FTE。')
j('XA-M165', 'C', '并线', typ='= XA-M166 SmartEye BV（同公司顾问 Jonathan De Graeve）', reason='同公司并线 → C')
j('XA-M166', 'A', '第二封', 'W47', 'MikroTik 专营网店（SmartEye BV / wifistock.be，Wilrijk；Switches 系列在售）', 'MikroTik 渠道，交换机已是品类', 'BE MikroTik 专营 → 维持 A', to='sales@smarteye.eu', hits_domain='smarteye.eu', lead='Hi Jonathan,',
  kp=[{'name': 'Jonathan De Graeve', 'role': '创始人 / 比利时唯一 MikroTik 认证顾问（S 箱 10-05 收件人）', 'source': 'MikroTik 顾问名录'}],
  q='Would a DIN-rail PoE switch be a useful addition to the WifiStock switch range, or is that outside your customers\' needs?')
j('XA-M167', 'A', '首触', 'W48', '工业网络分销（Alfa Systems，Hombeek；Antaira 授权，覆盖卢森堡）', '工业交换机品类现成', 'BE 工业分销、未触达 → A 首触', kind='ind',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to the industrial brands you carry?')
j('XA-M472', 'A', '第二封', 'W47', '泛欧增值分销 VAD（Kappa Data，De Pinte 总部；1998 起，约 100 人，比/荷/法/波四国；网络连接、安全、IoT）', 'VAD，网络 + IoT 事业部对口', 'BE/NL VAD、规模对口 → 维持 A（优先）', kind='dist2', to='sales@kappadata.be',
  notes='本轮 web_search 复核：kappadata.be/en/about-us「value-added distributor… network connectivity, security and IoT since 1998」；kappadata.eu「5 countries… 75 employees」。S 箱 10-04 发 info@，本封改 sales@。',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
# ===== 瑞典 13 =====
j('XA-C0011', 'A', '首触', 'W48', 'Moxa 官方分销（SCN AB / switches.shop）', '工业交换机专类', 'SE 工业分销、未触达 → A 首触', kind='ind',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to your Moxa range?')
j('XA-E004', 'C', '不动', typ='大型技术咨询公司（Vinnergi AB）', reason='大、不对口 → C')
j('XA-M038', 'C', '并线', typ='= XA-M194 AxByte（Leo 为其官方讲师）', reason='同公司并线 → C')
j('XA-M194', 'A', '第二封', 'W47', 'MikroTik 分销 + 官方培训（AxByte / netdist.se，Farsta）', 'MikroTik 渠道 + 讲师影响力', 'SE MikroTik 分销 → 维持 A', to='leo@axbyte.se', hits_domain='axbyte.se', lead='Hi Leo,',
  kp=[{'name': 'Leo', 'role': '瑞典 MikroTik RouterOS 官方讲师，21 年 MikroTik（S 箱 9-28 收件人）', 'source': '来源库'}],
  notes='support@/contact@ 的 2 条来信为自动回执（工单），非真人回复。',
  q='Would a DIN-rail PoE line be relevant for the ISPs you train and supply, or is that segment already covered?')
for c, t in (('XA-M039', '顾问（Straznet）'), ('XA-M196', '安全顾问（XPD）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M195', 'A', '第二封', 'W48', '工业电子/通信分销（EG Electronics AB；N-Tron/Red Lion/Anybus 渠道）', '工业通信品类现成', 'SE 工业分销 → 维持 A（轻卡）',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source for your industrial customers?')
j('XA-M197', 'A', '第二封', 'W48', '工业分销（HighTech Nordic AB，ORing 授权）', '工业交换机品类现成', 'SE 工业分销 → 维持 A',
  q='Would a second-source DIN-rail PoE switch be worth a test unit in your lab?')
j('XA-M198', 'B', '不动', typ='OEM Automatic 集团总部（瑞典上市集团）', reason='集团型技术分销，统一从华沙入口 → B')
j('XA-M199', 'A', '第二封', 'W48', 'MikroTik 分销（Sanuk Systems AB，Älvsjö）', 'MikroTik 渠道', 'SE MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M200', 'A', '首触', 'W48', 'MikroTik 分销（Satellithuset i Limmared / routerboard.se / mikrotik.se）', 'MikroTik 渠道', 'SE MikroTik 分销、未触达 → A 首触', kind='dist',
  q='Would either line be relevant for your reseller customers, or is switching fully covered today?')
j('XA-M325', 'B', '不动', typ='光纤网络方案商（BRS Networks，SE/DK/DE）', reason='方案商非渠道 → B')
j('XA-M500', 'A', '第二封', 'W48', 'Perle 授权分销（Profcon AB，本地备货）', '工业/串口网络分销', 'SE 工业网络分销 → 维持 A',
  q='Would a DIN-rail PoE switch be a sensible addition next to your industrial connectivity range?')
# ===== 丹麦 6 =====
j('XA-M001', 'A', '首触', 'W48', 'MikroTik 分销 + 认证顾问（Puma Solutions ApS，ISP 网络 1998 起）', 'MikroTik 渠道 + 工程', 'DK MikroTik 分销、未触达、KP 实名 → A 首触', kind='dist', to='stefan@pumait.dk', lead='Hi Stefan,',
  kp=[{'name': 'Stefan Andersen', 'role': 'MikroTik 认证顾问（MTCNA+MTCRE）', 'source': '来源库'}],
  q='Would either line be relevant for the ISPs you supply, or is switching outside what Puma stocks?')
j('XA-M002', 'B', '不动', typ='网络公司创始人/顾问（UNIFOSS）', reason=CONS)
j('XA-M064', 'B', '不动', typ='ALLNET 集团北欧分销（自有 ALLNET 品牌交换机）', reason='自有品牌同行集团 → B')
j('XA-M065', 'B', '不动', typ='小网店（Dvisor IT，Rønde）', reason='小店 → B')
j('XA-M066', 'A', '第二封', 'W48', 'MikroTik 分销（Nextron AS，Copenhagen）', 'MikroTik 渠道', 'DK MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M067', 'B', '不动', typ='顾问（CloudPilot）', reason=CONS)
# ===== 芬兰 6 =====
j('XA-M048', 'B', '不动', typ='顾问（Netrotik）', reason=CONS)
j('XA-M049', 'A', '第二封', 'W48', '工业技术贸易集团（Sarlin Oy Ab，1932 起家族企业；压缩空气/能源/自动化；N-Tron/Red Lion 渠道）', '工业自动化分销', 'FI 工业分销 → 维持 A（轻卡，规模偏大）', to='mikko.ylilammi@sarlin.com', lead='Hi Mikko,',
  kp=[{'name': 'Mikko Ylilammi', 'role': '来源库实名邮箱（S 箱 9-28 收件人）', 'source': '官网员工目录'}],
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source for your automation customers?')
j('XA-M236', 'A', '第二封', 'W48', '工业分销（Data Monitor，ORing 授权）', '工业交换机品类现成', 'FI 工业分销 → 维持 A',
  q='Would a second-source DIN-rail PoE switch be worth a test unit in your lab?')
j('XA-M237', 'A', '第二封', 'W48', '工业分销（Fiseg Oy，Tampere，Antaira 授权）', '工业交换机品类现成', 'FI 工业分销 → 维持 A',
  q='Would a second-source DIN-rail PoE switch be worth a test unit in your lab?')
j('XA-M238', 'A', '第二封', 'W48', 'MikroTik 分销（LocalNet Finland，Espoo）', 'MikroTik 渠道', 'FI MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M503', 'A', '第二封', 'W48', 'Perle 授权分销（Timeless Technology，Pori）', '工业/串口网络分销', 'FI 工业网络分销 → 维持 A',
  q='Would a DIN-rail PoE switch be a sensible addition next to your industrial connectivity range?')
# ===== 挪威 4 =====
j('XA-M147', 'A', '第二封', 'W49', '工业无线/网络分销（SATEL NORGE AS，ORing 授权）', '工业交换机品类现成', 'NO 工业分销 → 维持 A',
  q='Would a second-source DIN-rail PoE switch be worth a test unit in your lab?')
j('XA-M485', 'B', '不动', typ='IT 基础设施 VAR（nLogic）', reason=ATP)
j('XA-M486', 'B', '不动', typ='远程访问方案商（Specto Remote）', reason=ATP)
j('XA-M501', 'A', '第二封', 'W49', 'Perle 授权分销（The Junction AS，Drammen）', '工业/串口网络分销', 'NO 工业网络分销 → 维持 A',
  q='Would a DIN-rail PoE switch be a sensible addition next to your industrial connectivity range?')

run(J, 'W2-R05a', expect=62)
