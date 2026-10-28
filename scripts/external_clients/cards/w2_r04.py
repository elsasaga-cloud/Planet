# -*- coding: utf-8 -*-
"""波 2 第 1 轮（R04）：其余 XA 里的 波兰 18 + 加拿大 13 + 捷克 13 + 匈牙利 11 + 奥地利 9 + 瑞士 8 = 72 家研究卡（三库通用的数据驱动机制）。
轻卡为主；本轮 web_search 3 家（Stovaris / DDS NetCom / Nine-One-One）。第二封：MikroTik/工业渠道给 STI 工业线；Edgecore/CCTV 分销给三件套（dist2）。"""
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import DATA, ROOT  # noqa: E402
from research_store import put  # noqa: E402

D = '2026-10-27'
R = 'W2-R04'
SIG = "\n\nSimon\nSaga Telecom - sagatele.com"
SNAP = 'USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
SNAP24 = 'USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
CERT = {'CA': 'FCC/ISED', 'PL': 'CE', 'CZ': 'CE', 'HU': 'CE', 'AT': 'CE', 'CH': 'CE'}
WHEN_EU = {'W46': '2026-11-12', 'W47': '2026-11-19'}
WHEN_CA = {'W46': '2026-11-11', 'W47': '2026-11-18'}
SNAP86 = 'USD 86'
def window(iso):
    return 'CA 周三 08–10 当地' if iso == 'CA' else iso + ' 周四 12–14'


def when(iso, slot):
    return (WHEN_CA if iso == 'CA' else WHEN_EU).get(slot, '')
LIGHT = '轻卡：本轮未外查，沿用来源库官网/名录核对。'
REPO_FILE = {'E': 'edgecore.json', 'M': 'mikrotik.json', 'C': 'cctv.json'}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def ind_block(iso):
    return ("STI-288DGGPM: DIN-rail industrial L2+ switch, 8 x GE PoE+ (240 W budget) + 2 x SFP (1G/2.5G), -40 to +75 C, dual DC input, "
            "ERPS ring, SNMPv3, %s, %s/RoHS, 3-year warranty. Same family: STI-244DGGPM (4 x PoE+ + 2 x SFP, 120 W) at USD 121 and "
            "STI-488DGGPM (8 x PoE+ + 4 x SFP, 240 W) at USD 147." % (SNAP, CERT[iso]))


def dist_intro(iso):
    return ("Saga Telecom supplies network distributors with Marvell-based L2+ PoE switches and Centec-based L3 10G/25G/100G switches, "
            "under our label or the distributor's own, %s. Two lines that usually interest MikroTik and WISP channels:\n\n"
            "- STC-424XGGPM-280W: 24 x GE PoE+ (280 W) + 4 x 10G SFP+, L2+ managed, %s.\n"
            "- %s" % (CERT[iso], SNAP24, ind_block(iso)))


def ind_intro(iso):
    return ("Saga Telecom builds DIN-rail industrial Ethernet switches for distributors who already carry automation and industrial "
            "communication brands and want a second source at a lower price point, %s.\n\n%s" % (CERT[iso], ind_block(iso)))


def date_en(iso_date):
    y, m, d = iso_date.split('-')
    return '%d %s' % (int(d), MONTHS[int(m) - 1])


def dist2_block(iso):
    return ("Three PoE switches our distributor partners move most, all EXW Shenzhen (snapshot 2026-10-27, valid 15 days), %s, under our label or yours:\n\n"
            "- STC-2224GP: 24 x GE PoE+ (300 W) + 2 x GE + 2 x SFP, USD 86.\n"
            "- STC-424XGGPM-280W: 24 x GE PoE+ (280 W) + 4 x 10G SFP+, Marvell-based L2+ managed, USD 170.\n"
            "- STI-288DGGPM: DIN-rail industrial L2+, 8 x GE PoE+ (240 W) + 2 x SFP, -40 to +75 C, USD 137, 3-year warranty (12 months on the commercial units)." % CERT[iso])


# ---- 来源数据（三库）----
recs = {}
for letter, fn in REPO_FILE.items():
    for r in json.load(open(os.path.join(DATA, fn), encoding='utf-8'))['records']:
        recs[r['code']] = r
SB = {}
for row in csv.DictReader(open(os.path.join(ROOT, 'data', 'gmail_s', '2026-09_10群发名单_未入库.csv'), encoding='utf-8-sig')):
    SB.setdefault(row['域名'].lower(), []).append(row)


def src_email(r):
    m = re.search(r'\*\*邮箱\*\*：([^\s\n（]+)', r.get('contact_text') or '')
    e = m.group(1) if m else ''
    if '@' not in e:
        em = r.get('emails')
        if isinstance(em, list) and em and isinstance(em[0], dict):
            e = em[0].get('addr', '')
        elif isinstance(r.get('email'), str):
            e = r['email'].split('（')[0]
    return e if '@' in e else ''


def src_date(r):
    m = re.search(r'【(2026-\d\d-\d\d)', (r.get('src_note') or '') + (r.get('evidence_text') or ''))
    return m.group(1) if m else '2026-09-28'


def clean(s, n=220):
    s = re.sub(r'\*\*', '', s or '').replace('\n', ' ')
    return s[:n]


J = {}


def j(code, g, act, slot=None, typ='', fit='', reason='', lead='Hi,', q='', to=None, kp=None, notes='', kind=None, angle='', force_first=False):
    J[code] = dict(g=g, act=act, slot=slot, typ=typ, fit=fit, reason=reason, lead=lead, q=q, to=to, kp=kp or [], notes=notes, kind=kind, angle=angle, force_first=force_first)


CONS = '顾问/培训/小集成商，非渠道 → B（不进第二封）'
ATP = '小项目集成商（Allied Telesis 伙伴名录批量导入），非渠道 → B 慢慢跟进'
# ===== 波兰 18 =====
j('XA-C0012', 'A', '第二封', 'W46', '网络设备进口分销商（Gliwice，Inter Projekt S.A.）', '进口分销，PoE 全线可供', 'PL 次重点区网络进口分销 → 维持 A（优先）', kind='dist2',
  q='Which of the three would be worth a sample for your product team first - the 24-port L2+, the 24-port entry PoE, or the DIN-rail unit?')
j('XA-E026', 'B', '不动', typ='IT 集成商/VAR（Warsaw，公共部门向）', reason='集成商非渠道；10-21 刚发未回 → B 慢慢跟进')
for c, t in (('XA-M033', 'MikroTik 讲师（Kraków，mtik.pl）'), ('XA-M034', '顾问（C3NET）'), ('XA-M035', '顾问（SAFES，Kraków）'), ('XA-M037', '顾问（Mikrotikon）'), ('XA-M187', '顾问（Innored）'), ('XA-M298', '华沙 MikroTik 官方培训中心')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M036', 'B', '不动', typ='BMS/工业/楼宇自动化网络顾问（SINUX，Warszawa）', reason='顾问型；若回信直接给 STI 工业线 → B')
j('XA-M183', 'A', '第二封', 'W46', '电信专业批发（Alfa Extranet / Aenet.pl，Częstochowa；MikroTik 官方）', '专业批发，MikroTik 渠道', 'PL 次重点区专业批发 → 维持 A', lead='Hi,',
  q='Do your ISP customers ask you for DIN-rail PoE switches for cabinets and towers, or is that still sourced elsewhere?')
j('XA-M184', 'A', '第二封', 'W46', '电信/光纤基础设施 + LAN 分销（FIBERM，Kłobuck，B2B）', '光纤基础设施分销，PoE/工业 PoE 配套', 'PL 次重点区电信基础设施分销 → 维持 A',
  q='Would a DIN-rail PoE switch be a useful addition to your LAN range for FTTH and cabinet installs?')
j('XA-M185', 'A', '首触', 'W47', 'MikroTik 分销（FYR-SYSTEMS，Warszawa）', 'MikroTik 渠道', 'PL 次重点区 MikroTik 分销；S 箱当时地址打错（ikrotik@）= 实际未触达 → A 首触', kind='dist', to='mikrotik@fyr-systems.pl', force_first=True,
  notes='S 箱 10-09 发到 ikrotik@fyr-systems.pl（少了 m），按未触达处理，正确地址 mikrotik@fyr-systems.pl。',
  q='Would either line be relevant for your MikroTik customers, or is switching outside what FYR stocks?')
j('XA-M186', 'A', '第二封', 'W46', '无线网络中心网店（wirelesslan.pl / Konsorcjum ATS，Radom）', 'WISP 渠道', 'PL 次重点区 WISP 渠道 → 维持 A',
  q='Would your WISP customers take a hardened PoE switch for tower sites at this price, or do they stay with their current brand?')
j('XA-M188', 'A', '首触', 'W47', 'MikroTik 进口商/分销商（WiFi24，Przemyśl）', '「Importer – Dystrybutor MikroTik」', 'PL 次重点区 MikroTik 进口分销、未触达 → A 首触', kind='dist',
  q='What is the usual route for a new switch brand onto your line card - a sample first, or a price sheet for your product team?')
j('XA-M479', 'B', '不动', typ='IT 集成商（KNT, Olsztyn）', reason=ATP)
j('XA-M480', 'C', '不动', typ='大型网络集成集团波兰公司（Nomios）', reason='大集团 SI → C')
j('XA-M481', 'A', '第二封', 'W46', '增值分销 VAD（Stovaris，Warszawa，1987 起，原 Alstor SDS；有 IT 网络与工业/IoT 事业部）', 'VAD，网络 + 工业 IoT 两个事业部都对口', 'PL 次重点区 VAD → 维持 A（优先）', kind='dist2', to='biuro@stovaris.pl',
  notes='本轮 web_search 复核：stovaris.pl/en/specjalizacje「value-added distributor (VAD)… IT networks… Industrial and IoT systems」；KRS 0000758346。S 箱 10-01 发的是 esklep@，本封改总信箱 biuro@。',
  q='Which of your divisions would be the right home for this - IT networks or Industrial & IoT - and who should I send the datasheets to?')
j('XA-M502', 'A', '第二封', 'W46', 'Perle 授权分销（Microstar sp. z o.o.，Warsaw；与克罗地亚同名公司无关）', '工业/串口网络分销', 'PL 次重点区工业网络分销 → 维持 A', lead='Hi Piotr,',
  kp=[{'name': 'Piotr Pieczerak', 'role': '销售（S 箱 9-28 收件人）', 'source': '来源库 / S 箱'}],
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to your industrial connectivity range?')
# ===== 加拿大 13 =====
j('XA-E006', 'A', '第二封', 'W47', '电信硬件批发分销（Calgary，1989 起，Ericsson-LG 加拿大独家分销，11–50 人；经销商网络全国）', '全国经销商网络，PoE 配 IP 话机/酒店部署', 'CA 主攻区电信分销、KP 实名 → 维持 A', kind='dist2', lead='Hi Jesse,', to='jesse.foster@nine-one-one.ca',
  kp=[{'name': 'Jesse Foster', 'role': 'V.P. Sales & Marketing', 'source': 'BusinessWire 2024-05 伙伴稿 / S 箱收件人'}],
  notes='本轮 web_search 复核：nine-one-one.ca「wholesale distributor servicing all of Canada… network switches」；Boom Collaboration 稿 Jesse Foster V.P. Sales & Marketing。',
  q='For your interconnect dealers, is PoE for phone and camera deployments something you would rather carry under your own label or ours?')
j('XA-E018', 'A', '第二封', 'W47', '电信/数据网络设备分销（FONEX Data Systems，Montréal）', '分销', 'CA 主攻区分销 → 维持 A', kind='dist2', to='pdipierro@fonex.com',
  q='Which of the three would fit your catalogue first, and is there a product manager I should send the datasheets to?')
j('XA-E019', 'B', '不动', typ='结构化布线/网络安装商（Laval QC）', reason='安装商终端买家；10-21 刚发未回 → B')
for c, t in (('XA-M003', '顾问（Magenta Networks）'), ('XA-M005', '顾问（Commander IT）'), ('XA-M078', '一人公司（ProRéseau，Québec）'), ('XA-M082', '顾问（JMR）'), ('XA-M083', '讲师（Arawi，Winnipeg）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M004', 'A', '首触', 'W47', '工业自动化分销（Industrial Solutions Inc，Alberta，9 人；Moxa/Red Lion/N-Tron/Sixnet/eWon）', '工业交换机品类现成', 'CA 主攻区工业分销、未触达 → A 首触', kind='ind',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source for your panel-builder customers?')
j('XA-M006', 'A', '首触', 'W47', 'MikroTik 分销 + 认证顾问团队（Wireless Netware，Ontario）', 'MikroTik 渠道 + 工程能力', 'CA 主攻区 MikroTik 分销、未触达 → A 首触', kind='dist',
  q='Would either line be relevant for your reseller customers, or is your switching demand fully covered today?')
j('XA-M079', 'A', '第二封', 'W47', 'WISP 无线设备分销（MBSI WAV，Medicine Hat，Alberta）', 'WISP 渠道', 'CA 主攻区 WISP 分销 → 维持 A（优先）',
  q='Would a hardened PoE switch at this price be worth listing next to your tower-site gear?')
j('XA-M080', 'A', '首触', 'W47', 'MikroTik 专营网店（Mahkesis Group，Winnipeg；有 Switches 分类）', 'MikroTik 专营，PoE 交换机已是品类', 'CA 主攻区 MikroTik 专营、未触达 → A 首触（网店，权重中）', kind='dist',
  q='Do your MikroTik customers ask for DIN-rail PoE switches, or is the demand mostly indoor?')
j('XA-M081', 'A', '第二封', 'W47', '网络设备分销（Optitera Global Networks，Ontario；已有工业交换机线）', '已有工业交换机线，STI 做第二供应商', 'CA 主攻区分销 → 维持 A',
  q='Since you already carry an industrial switch line, would a managed DIN-rail unit at this price be worth comparing?')
# ===== 捷克 13 =====
j('XA-E017', 'C', '并线', typ='= XA-M154 Proficomms（同公司，mik 库条目有邮箱）', reason='跨库重复 → C 并线')
j('XA-M031', 'A', '首触', 'W47', '工业网络分销（Westercom，Westermo Silver + Advantech EKI + B+B SmartWorx）', '工业交换机专类', 'CZ 工业网络分销、未触达 → A 首触', kind='ind',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to the industrial brands you carry?')
j('XA-M148', 'A', '第二封', 'W46', '无线/网络设备网店（AIRCOM Praha，wifihw.cz；V-SOL GPON、Meanwell）', 'ISP/WISP 渠道', 'CZ ISP 渠道网店 → 维持 A',
  q='Would a DIN-rail PoE switch be a useful second option for your ISP customers, or do they stay with one brand?')
j('XA-M149', 'B', '不动', typ='大型 IT 广线分销（AT Computers a.s.）', reason='大广线分销 → B')
j('XA-M150', 'A', '第二封', 'W46', '工业分销（ATEsystem，Ostrava，Antaira 授权）', '工业交换机品类现成', 'CZ 工业分销 → 维持 A',
  q='Would a second-source DIN-rail PoE switch be worth a test unit in your lab?')
j('XA-M151', 'B', '不动', typ='顾问（MapNet，Brno）', reason=CONS)
j('XA-M152', 'B', '不动', typ='OEM Automatic 集团捷克公司（瑞典上市集团，Antaira 渠道）', reason='集团型技术分销，邮箱为波兰分公司 → B（将来从华沙一次打集团）')
j('XA-M153', 'A', '首触', 'W47', 'MikroTik 分销（PCV Computers，České Budějovice）', 'MikroTik 渠道', 'CZ MikroTik 分销、未触达 → A 首触', kind='dist',
  q='Would either line be relevant for your MikroTik customers, or is switching outside what PCV stocks?')
j('XA-M154', 'A', '首触', 'W47', '专业网络分销（Proficomms，Brno；ComNet/Microsens/AMG/PLANET/TRENDnet/Cisco IE）', '已卖多牌工业/专业交换机', 'CZ 专业分销、品类现成、未触达 → A 首触（优先）', kind='dist',
  q='Would a second-source industrial PoE line next to the brands you carry be worth a sample, or a price sheet first?')
j('XA-M155', 'A', '第二封', 'W46', '工业分销（TECON，ORing 授权）', '工业交换机品类现成', 'CZ 工业分销 → 维持 A',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source?')
j('XA-M156', 'B', '不动', typ='MikroTik 网店（WIFIPROFI.CZ；klima@ 已停用 2026-10-04）', reason='地址失效、小店 → B', notes='邮箱已停用，再触达需补地址。')
j('XA-M157', 'B', '不动', typ='大型 IT 分销（eD system Czech）', reason='大广线分销 → B')
j('XA-M484', 'B', '不动', typ='IT 集成商（4service）', reason=ATP)
# ===== 匈牙利 11 =====
j('XA-M007', 'B', '不动', typ='MikroTik 专营安装商/顾问（Miskolc）', reason=CONS)
j('XA-M084', 'A', '第二封', 'W46', '工业分销（AXTEK line，Pécel，Antaira 授权）', '工业交换机品类现成', 'HU 工业分销 → 维持 A',
  q='Would a second-source DIN-rail PoE switch be worth a test unit in your lab?')
j('XA-M085', 'A', '第二封', 'W46', '仅面向经销商/集成商的批发网店（AbsolCom，Budapest；在售 D-Link PoE+ 交换机）', 'B2B 批发，PoE 已是品类', 'HU B2B 批发 → 维持 A',
  q='Would a DIN-rail PoE switch be a useful addition for your installer customers, or is your demand mostly indoor PoE?')
j('XA-M086', 'A', '首触', 'W47', 'B2B 批发/官方分销（AccessPoint Kft，Budapest；明列 switch / PoE switch）', 'B2B 批发，PoE 交换机已是品类', 'HU B2B 分销、未触达 → A 首触', kind='dist',
  q='Which of the two would be more relevant for your installer customers - the 24-port PoE or the DIN-rail line?')
j('XA-M087', 'B', '不动', typ='顾问（LazyBear，Pécs）', reason=CONS)
j('XA-M088', 'A', '首触', 'W47', 'IT 分销（Compmarket Hungary Zrt，Budapest；实名邮箱）', '分销、实名直达', 'HU 分销、未触达、KP 实名 → A 首触', kind='dist', lead='Dear Mr. Rákos,',
  kp=[{'name': 'Rákos Zoltán', 'role': '来源库实名邮箱（职务未记）', 'source': '来源库'}],
  q='Would either line fit your networking portfolio, and if so, would you prefer a sample or the full price list first?')
j('XA-M089', 'A', '第二封', 'W47', '工业自动化/控制分销（Controsys，Budapest；N-Tron/Red Lion 渠道）', '工业交换机品类现成', 'HU 工业分销 → 维持 A（轻卡，待核）',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source for your automation customers?')
j('XA-M090', 'A', '第二封', 'W46', 'MikroTik 分销（Expert Zrt，Budapest）', 'MikroTik 渠道', 'HU MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M091', 'A', '第二封', 'W46', '无线/网络专营网店（Wireless-Bolt，Albertirsa；MikroTik Switches 分类）', 'WISP 渠道', 'HU WISP 渠道 → 维持 A',
  q='Would your WISP customers take a hardened PoE switch for tower sites at this price?')
j('XA-M491', 'B', '不动', typ='IT 集成商（Young B.T.S.）', reason=ATP)
j('XA-M493', 'A', '第二封', 'W47', 'Westermo 转售 + 控制工程（ATYS Co，Budapest；与罗马尼亚 ATYS-co 同家）', '工业交换机转售', 'HU 工业渠道 → 维持 A（轻卡）',
  q='Would a second-source DIN-rail PoE switch be worth a test unit next to your industrial range?')
# ===== 奥地利 9 =====
j('XA-M010', 'B', '不动', typ='顾问（Aulaf）', reason=CONS)
j('XA-M106', 'B', '不动', typ='小型系统之家（Formatik，Ehrwald）', reason=CONS)
j('XA-M107', 'A', '第二封', 'W47', 'MikroTik 分销（NETZWARE，Wien）', 'MikroTik 渠道', 'AT MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M108', 'B', '不动', typ='IT 网店（QEDV，Tirol）', reason='小网店 → B')
j('XA-M109', 'B', '不动', typ='中小企业/酒店网络集成商（evoNET，Tirol，约 10 人）', reason=CONS)
for c, t in (('XA-M473', 'IT 集成商（IT-TRUST）'), ('XA-M474', 'IT 集成商（quattroSEC）'), ('XA-M475', 'IT 贸易/集成（S.A.B.E.L. Handels GmbH，Vienna）'), ('XA-M476', 'IT 集成商（Salzgeber）')):
    j(c, 'B', '不动', typ=t, reason=ATP)
# ===== 瑞士 8 =====
j('XA-M040', 'B', '不动', typ='MikroTik 网络设计/自动化工具顾问（Narrowin，Lugano）', reason=CONS)
j('XA-M201', 'A', '第二封', 'W46', 'MikroTik 分销（ENGITECH S.A.，Genève）', 'MikroTik 渠道', 'CH MikroTik 分销 → 维持 A（S 箱已发 2 次，本封是第三触，换品类）',
  q='Would a DIN-rail PoE line be relevant for your integrator customers in Romandie, or is that segment already covered?')
j('XA-M202', 'A', '首触', 'W47', '工业自动化/IIoT 产品分销（INOVIS Live Automation AG，Rüti ZH）', '工业分销', 'CH 工业分销、未触达 → A 首触', kind='ind',
  q='Would a DIN-rail PoE switch line sit alongside your IIoT hardware, or is switching outside your scope?')
j('XA-M203', 'B', '不动', typ='顾问（Portup，Zürich）', reason=CONS)
j('XA-M204', 'B', '不动', typ='LoRaWAN 网关厂商自营 MikroTik 小店（Wifx SA）', reason='厂商 + 小店 → B')
j('XA-M332', 'C', '并线', typ='= XA-M201 ENGITECH S.A.（同公司顾问 Philippe Robert）', reason='同公司并线 → C')
j('XA-M477', 'A', '首触', 'W47', 'OT/工业网络专业商 + 网店（DDS NetCom AG，Fehraltorf，1992 起，2–10 人；2023 起为美国 McNaughton-McKay 全资子公司）', '工业/楼宇自动化网络，DIN 轨 PoE 对位', 'CH 工业网络渠道、未触达 → A 首触（小，权重中）', kind='ind',
  notes='本轮 web_search 复核：LinkedIn「seit Mai 2023 eine 100%ige Tochter der McNaughton-McKay… kritische IT-Netzwerke in Industrie, Produktion und Gebäudeautomation」；os.dds.ch「Industrial Networking Solutions… Switching」。',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit for your OT network projects?')
j('XA-M478', 'B', '不动', typ='IT 集成商（FIVE Informatik）', reason=ATP)

assert len(J) == 72, len(J)

cards = []
for code, jj in J.items():
    r = recs[code]
    iso = r['iso']
    dom = (r.get('domain') or r.get('website') or '').split(' ')[0].lower()
    hits = [] if jj['force_first'] else SB.get(dom, [])
    email = jj['to'] or src_email(r) or (hits[0]['邮箱'] if hits else '')
    sdate = src_date(r)
    note_src = r.get('src_note') or r.get('evidence_text') or r.get('type') or ''
    evidence = [{'kind': '来源库官网/名录核对', 'claim': clean(note_src), 'quote': '', 'url': 'https://' + dom + '/' if dom else '', 'date': sdate}]
    opener = ''
    if hits:
        h = hits[0]
        subj = re.sub(r'^(MSD-\d+\s*)', '', h['最后主题']).strip() or '24 Port PoE Managed Switch'
        evidence.append({'kind': 'S 箱群发记录', 'claim': 'S 箱 %s 发 %s「%s」，去 %s 来 %s' % (h['首次'], h['邮箱'], h['最后主题'], h['去信'], h['来信']),
                         'quote': '', 'url': 'data/gmail_s/2026-09_10群发名单_未入库.csv', 'date': h['最后']})
        touch = 'S 箱 %s 群发「%s」→ 已发未回' % (h['首次'], subj) if h['来信'] == '0' else 'S 箱 %s 群发「%s」→ 来信（%s），待核' % (h['首次'], subj, h['最后主题'])
        opener = ("I wrote on %s about our 24-port PoE L2+ switch ('%s'); this is a different angle, so a fresh note rather than a reply." % (date_en(h['首次']), subj))
    else:
        touch = 'S 箱 9–10 月群发名单未见本域 → 未触达' if not jj['force_first'] else '未触达（S 箱发错地址）'
    act = jj['act']
    if act == '第二封' and not hits:
        act = '首触'
        jj['kind'] = jj['kind'] if jj['kind'] in ('ind', 'dist') else 'dist'
    is_ind = (act == '第二封' and jj['kind'] != 'dist2') or jj['kind'] == 'ind'
    if act in ('第二封', '首触'):
        model = 'STI-288DGGPM' if is_ind else ('STC-2224GP / STC-424XGGPM-280W / STI-288DGGPM' if jj['kind'] == 'dist2' else 'STC-424XGGPM-280W / STI-288DGGPM')
        price = SNAP if is_ind else ('USD 86 / USD 170 / USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)' if jj['kind'] == 'dist2' else SNAP24 + ' / ' + SNAP)
        angle = jj['angle'] or ('STI 工业 L2+ PoE（MikroTik 无此品类）' if (act == '第二封' and is_ind) else ('工业 DIN 轨 PoE 首触' if is_ind else ('分销三件套：HRUI 24 口 + SmartByte 24 口 L2+ + STI' if jj['kind'] == 'dist2' else '分销首触：24 口 PoE + STI 工业线')))
        nm = {'action': act, 'angle': angle, 'model': model, 'price': price, 'window': window(iso), 'when': when(iso, jj['slot'])}
    else:
        nm = {'action': act, 'angle': '', 'model': '', 'price': '', 'window': '', 'when': '不动' if act == '不动' else ''}
    card = dict(code=code, name=r['name'], round=R, researched_at=D,
                alive='本轮 web_search 复核在线（2026-10-27）' if '复核' in jj['notes'] else '来源库 %s 核对在线；本轮未复查' % sdate,
                summary=jj['typ'] + ('；' + clean(r.get('entry_point'), 160) if r.get('entry_point') else ''),
                type_final=jj['typ'], size='未量化' if '人' not in jj['typ'] else jj['typ'],
                brands_seen=[b.strip() for b in re.split(r'[+/,，、]', r.get('signals') or '') if b.strip()][:8],
                saga_line='SmartByte 商用 L2+ + HRUI 入门 PoE + Saga STI 工业 L2+ PoE' if jj['g'] == 'A' else '—',
                fit=jj['fit'], evidence=evidence,
                contacts={'email': email, 'email_status': '来源库公开邮箱' if email else '缺', 'kp': jj['kp']},
                touch_status=touch, saga_overlap='无', grade_final=jj['g'], grade_reason_final=jj['reason'], next_move=nm,
                notes=(jj['notes'] + ' ' if jj['notes'] else '') + ('' if '复核' in jj['notes'] else LIGHT))
    if act in ('第二封', '首触'):
        assert email, code
        if act == '第二封':
            block = dist2_block(iso) if jj['kind'] == 'dist2' else ind_block(iso)
            if jj['kind'] == 'dist2':
                subject = 'PoE switch line for your reseller channel - distributor pricing'
            elif 'MikroTik' in jj['typ'] or 'WISP' in jj['typ'] or 'ISP' in jj['typ']:
                subject = 'Industrial DIN-rail PoE switches - the category MikroTik does not cover'
            else:
                subject = 'A second-source DIN-rail PoE switch for your industrial customers'
            body = jj['lead'] + "\n\n" + opener + "\n\n" + block + "\n\n" + jj['q'] + SIG
        else:
            body = jj['lead'] + "\n\n" + (ind_intro(iso) if is_ind else dist_intro(iso)) + "\n\n" + jj['q'] + SIG
            subject = 'DIN-rail industrial PoE switches - second source for your line card' if is_ind else 'L2+ PoE and industrial switches for your reseller channel'
        card['draft_en'] = {'subject': subject, 'body': body}
    cards.append(card)

for c in cards:
    put(c)
from collections import Counter
print('R04 cards', len(cards), Counter(c['grade_final'] for c in cards), Counter(c['next_move']['action'] for c in cards),
      Counter(c['next_move']['when'] for c in cards if c['next_move']['action'] in ('第二封', '首触')))
