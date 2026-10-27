# -*- coding: utf-8 -*-
"""波 1 第 2 轮：mikrotik-info XA 美国 58 + 英国 40 = 98 家研究卡（数据驱动：公司事实取自来源库记录 + S 箱群发名单；
人工判断在 J 表）。轻卡为主；5 家本轮 web_search 复核（Ivory Egg / MAC Solutions / Telasys / Morgan Ingland / Pymatek）。
第二封角度：STI 工业 DIN 轨 L2+ PoE（MikroTik 没有的品类）；首触：分销型给 STC-424XGGPM-280W + STI，工业型给 STI。"""
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import DATA, ROOT  # noqa: E402
from research_store import put  # noqa: E402

D = '2026-10-27'
R = 'W1-R02'
SIG = "\n\nSimon\nSaga Telecom - sagatele.com"
SNAP = 'USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
SNAP24 = 'USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
CERT = {'US': 'FCC/CE', 'GB': 'UKCA/CE'}
WHEN = {('US', 'W45'): '2026-11-04', ('US', 'W46'): '2026-11-11', ('GB', 'W45'): '2026-11-05', ('GB', 'W46'): '2026-11-12'}
WINDOW = {'US': 'US 周三 08–10 当地', 'GB': 'GB 周四 12–14 当地'}
LIGHT = '轻卡：本轮未外查，沿用来源库官网/名录核对。'
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


# ---- 来源数据 ----
recs = {r['code']: r for r in json.load(open(os.path.join(DATA, 'mikrotik.json'), encoding='utf-8'))['records']}
SB = {}
for row in csv.DictReader(open(os.path.join(ROOT, 'data', 'gmail_s', '2026-09_10群发名单_未入库.csv'), encoding='utf-8-sig')):
    SB.setdefault(row['域名'].lower(), []).append(row)


def src_email(r):
    m = re.search(r'\*\*邮箱\*\*：([^\s\n]+)', r.get('contact_text') or '')
    e = m.group(1) if m else ''
    return e if '@' in e else ''


def src_date(r):
    m = re.search(r'【(2026-\d\d-\d\d)', r.get('src_note') or '')
    return m.group(1) if m else '2026-09-28'


def clean(s, n=220):
    s = re.sub(r'\*\*', '', s or '').replace('\n', ' ')
    return s[:n]


# ---- 人工判断表 J：code -> (grade, action, slot, type_final, fit, reason, lead, question, to, kp, notes, kind) ----
# kind: 'dist' 分销首触 / 'ind' 工业首触 / None（第二封或不发）
J = {}


def j(code, g, act, slot=None, typ='', fit='', reason='', lead='Hi,', q='', to=None, kp=None, notes='', kind=None, angle=''):
    J[code] = dict(g=g, act=act, slot=slot, typ=typ, fit=fit, reason=reason, lead=lead, q=q, to=to, kp=kp or [], notes=notes, kind=kind, angle=angle)


# ===== 美国 58 =====
j('XA-M043', 'A', '第二封', 'W45', '工业分销（N-Tron/Red Lion/HMS 渠道；克利夫兰 1–10 人、60 年）', '工业交换机品类现成，STI 做第二供应商', 'US 主攻区工业分销、品类完全对口 → 维持 A',
  q='For your commercial panel-builder and plant customers, would a DIN-rail PoE switch at this price point be worth a sample unit?', notes='口径：中国产地不谈政府/电力项目，只谈商业渠道。')
j('XA-M044', 'B', '不动', typ='个人顾问/讲师（西语市场，gmail）', reason='个人顾问非采购方、未群发 → B 不动')
j('XA-M045', 'C', '不动', typ='终端用户内部工程师（赛事方 IndyCar）', reason='终端触点，非渠道 → C')
j('XA-M046', 'B', '不动', typ='小型 MSP/顾问（MikroTik 10 证）', reason='小 MSP、support@ 入口、未群发 → B 不动')
j('XA-M047', 'B', '不动', typ='个人顾问/讲师（gmail）', reason='个人讲师非采购方 → B 不动')
j('XA-M213', 'A', '第二封', 'W46', '网络设备分销（迈阿密 25 年，拉美出口向）', '分销 25 年；经销商网络在拉美', 'US 主攻区分销 → 维持 A（拉美出口向，权重中）',
  q='Do your reseller customers ask for hardened PoE switches for outdoor cabinets, or is the demand mostly indoor commercial?')
j('XA-M214', 'B', '不动', typ='MikroTik/Tenda 网店（Walmart 平台卖家）', reason='小网店/平台卖家，难复购 → B')
j('XA-M215', 'B', '不动', typ='网店（Centreville；来源库无核对信息）', reason='信息不足、未群发 → B 待补')
j('XA-M216', 'A', '第二封', 'W45', '网络设备分销（FL，自述 leading distributor）', '分销身份明确', 'US 主攻区分销 → 维持 A',
  q='Would an industrial PoE line be a useful addition for your integrator customers, or is your focus purely indoor commercial switching?')
j('XA-M217', 'A', '第二封', 'W45', '工业自动化分销（Moxa 官方渠道名录）', '已卖工业交换机，STI 同类补位', 'US 主攻区工业分销（Moxa 渠道）→ 维持 A（优先）', lead='Hi Scott,',
  q='Would a second-source DIN-rail PoE switch be worth a test unit in your lab?', to='scott@controllerservice.com', kp=[{'name': 'Scott', 'role': '销售（S 箱 10-09 收件人）', 'source': 'S 箱群发名单'}])
j('XA-M218', 'A', '第二封', 'W45', 'FTTx / 固定无线 / HFC 宽带设备分销（CO）', '宽带运营商渠道，塔站/机柜需要宽温 PoE', 'US 主攻区宽带设备专业分销 → 维持 A（优先）',
  q='Do your fixed-wireless customers buy hardened PoE switches for tower and cabinet sites through you today?')
j('XA-M219', 'A', '第二封', 'W46', '网络设备分销（北迈阿密，拉美向）', '分销', 'US 主攻区分销 → 维持 A（拉美出口向）',
  q='Is there demand from your reseller base for DIN-rail PoE switches, or would the commercial 24-port line be the better fit for a first order?')
j('XA-M220', 'A', '第二封', 'W45', 'WISP 方案分销（NC，shopdoubleradius.com）', 'WISP 渠道，户外/塔站 PoE', 'US 主攻区 WISP 分销 → 维持 A（优先）',
  q='Would a hardened PoE switch at this price be worth listing next to your tower-site gear, or do your customers already have a go-to brand?')
j('XA-M221', 'A', '第二封', 'W46', 'MikroTik 专营网店（Dallas）', 'MikroTik 专营，缺工业 PoE 品类', 'US 主攻区 MikroTik 专营 → 维持 A（网店，权重中）',
  q='Do your MikroTik customers ask you for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M222', 'A', '首触', 'W46', '网络/安防/VoIP 分销（迈阿密）', '分销、未触达', 'US 主攻区分销、未触达 → A 首触', kind='dist',
  q='Which of the two would be more relevant for your reseller customers - the 24-port PoE for offices and camera sites, or the DIN-rail line?')
j('XA-M223', 'B', '不动', typ='MikroTik 自动化集成商/MSP', reason='集成商非渠道 → B')
j('XA-M224', 'B', '不动', typ='ISP 培训机构（The ISP Academy）', reason='培训机构非采购方 → B（关系线，不进发送包）')
j('XA-M225', 'B', '不动', typ='电商品牌代运营/平台卖家（Bellevue）', reason='平台卖家 → B')
j('XA-M226', 'A', '第二封', 'W46', 'WISP 渠道网店（在售 CRS418-8P-8G-2S+RM）', 'WISP 渠道，PoE 交换机已是品类', 'US 主攻区 WISP 渠道 → 维持 A',
  q='Would your WISP customers take a hardened PoE switch for tower sites at this price, or do they stay with their current brand?')
j('XA-M227', 'C', '并线', typ='= XA-E022 Microcom Technologies（Edgecore 库已研究，10-28 首触）', reason='跨库重复，并入 XA-E022 → C', notes='同一家公司；以 XA-E022 为准。')
j('XA-M228', 'A', '首触', 'W45', '宽带/线缆设备分销（PA，自述 MikroTik Master Distributor）', 'Master Distributor、未触达', 'US 主攻区 Master Distributor、未触达 → A 首触（优先）', kind='dist',
  q='What is the usual route for a new switch brand to get onto your line card - a sample for your lab, or a pricing sheet for your product team first?')
j('XA-M229', 'A', '第二封', 'W46', '卫星/宽带设备分销（Rochester）', '宽带设备分销', 'US 主攻区分销 → 维持 A',
  q='Is there a place for a DIN-rail PoE switch in your broadband catalogue, or is your demand mostly head-end and indoor?')
j('XA-M230', 'B', '不动', typ='ISP/WISP 小型直营网店（IL）', reason='小网店 → B')
j('XA-M231', 'C', '不动', typ='加固计算机 / 军用方向', reason='军用守界 → C')
j('XA-M232', 'B', '不动', typ='MikroTik 顾问/讲师个人（gmail）', reason='个人讲师非采购方 → B')
j('XA-M233', 'A', '第二封', 'W46', 'IT 分销（Doral，拉美向）', '分销', 'US 主攻区分销 → 维持 A（拉美向）',
  q='Would a DIN-rail PoE line be relevant for your reseller base, or should we keep to the commercial 24-port switch?')
j('XA-M234', 'A', '第二封', 'W46', '网络设备分销（NJ；来源库 R63 升 A）', '分销', 'US 主攻区分销 → 维持 A', to='info@vodanetsystems.com',
  q='Do your customers ask for industrial PoE switches, or would the commercial line be the better first step?')
j('XA-M235', 'C', '并线', typ='= XA-C0013 WAV, LLC（CCTV 库已研究，10-28 首触 zachh@）', reason='跨库重复 → C 并线', notes='同一家公司；以 XA-C0013 为准。')
j('XA-M295', 'B', '不动', typ='MikroTik 认证培训机构（NC）', reason='培训机构 → B')
j('XA-M303', 'A', '第二封', 'W45', 'WISP 分销/集成（Netonix 代理）', 'WISP 渠道，已卖户外交换机', 'US 主攻区 WISP 渠道 → 维持 A', notes='Netonix 用 Vitesse 芯片，对其不讲 Marvell 话术。',
  q='Would a DIN-rail PoE switch be a useful second option for your tower-site builds, or is your current line fully covering that?')
j('XA-M304', 'A', '第二封', 'W45', 'WISP 分销/集成（Netonix 代理）', 'WISP 渠道', 'US 主攻区 WISP 渠道 → 维持 A', notes='Netonix 用 Vitesse 芯片，对其不讲 Marvell 话术。',
  q='Do your WISP customers currently buy hardened PoE switches from you, or from elsewhere?')
j('XA-M305', 'B', '不动', typ='综合 IT 电商（neobits.com）', reason='综合电商平台 → B')
j('XA-M306', 'A', '首触', 'W45', 'Teltonika 北美战略分销（备货/预配置/培训）', '工业路由分销，工业 PoE 配套', 'US 主攻区工业路由分销、未触达 → A 首触', kind='ind',
  q='Would a DIN-rail PoE switch next to your industrial-router range be worth a sample, or would you rather see the full industrial price list first?')
j('XA-M307', 'A', '第二封', 'W45', 'Teltonika 授权分销（工业蜂窝路由/IoT；在售 TSW212 工业 PoE+ 交换机）', '已卖工业 PoE 交换机，STI 直接对位', 'US 主攻区、工业 PoE 品类现成 → 维持 A（优先）',
  q='Since you already list industrial PoE switches, would a managed DIN-rail unit with ERPS ring at this price be worth comparing?')
for c, t in (('XA-M308', '安防集成商（Cook & Boardman 事业部）'), ('XA-M309', '企业 IT/AV/安防集成商（WI）'), ('XA-M310', '集成商（OH）'), ('XA-M311', '安防/网络集成商'),
             ('XA-M312', '安防集成商（ME）'), ('XA-M314', '集成商（NE）'), ('XA-M315', 'IT 集成商（AZ，仅 support@）'), ('XA-M316', '安防集成商（PA）'),
             ('XA-M317', 'IT 方案商（SD）'), ('XA-M318', '全国安防集成连锁（CT 分部）'), ('XA-M320', '电气承包商（WI）'), ('XA-M321', '消防/安防集成商（OH）'),
             ('XA-M322', '网络集成/运维'), ('XA-M323', '教育 IT 服务（OH）'), ('XA-M324', '布线/集成（WI，未触达）'), ('XA-M340', '托管 IT 服务商（IL，235 客户）'),
             ('XA-M341', 'K12/中小企业 IT 服务（GA）'), ('XA-M482', '安防/消防集成商（Marksman Titan，Resell 级）'), ('XA-M483', '安防/消防集成商')):
    j(c, 'B', '不动', typ=t, reason='小项目集成商/服务商，非渠道；9–10 月已发未回 → B 慢慢跟进（不进第二封）')
j('XA-M313', 'C', '不动', typ='大型 MSP/VAR（Heartland Business Systems）', reason='大 VAR → C')
j('XA-M319', 'C', '并线', typ='= XA-M318 Security 101（同品牌 Rochester 分部）', reason='同品牌连锁，并入 XA-M318 → C')
j('XA-M342', 'A', '第二封', 'W45', 'Hirschmann 授权分销 + 自动化/网络服务（NY）', '工业网络分销', 'US 主攻区工业网络分销 → 维持 A',
  q='Would a lower-priced DIN-rail PoE switch be useful as a second source for your automation customers, or do they insist on one brand?')
j('XA-M507', 'A', '第二封', 'W45', '网络硬件分销/转售（TX，10,000+ 客户 50+ 国，在售 MikroTik CRS518）', '规模与品类对口', 'US 主攻区、规模与品类对口 → 维持 A（优先）',
  q='Would an industrial PoE line be worth adding for your 50-country customer base, or is your demand mostly data-centre and office?')
j('XA-M508', 'B', '不动', typ='翻新 IT 硬件商（IL）', reason='翻新为主 → B')

# ===== 英国 40 =====
j('XA-M050', 'A', '第二封', 'W45', '工业电气批发（Hull，3 万+ 库存项，N-Tron/Red Lion 渠道）', '工业交换机品类现成', 'GB 主攻区工业电气分销 → 维持 A',
  q='Would a DIN-rail PoE switch at this price be worth a trial order for your panel-builder customers?')
j('XA-M051', 'B', '不动', typ='ISP/MSP（SimRush 总代）', reason='ISP 为主 → B')
j('XA-M052', 'A', '第二封', 'W45', '工业网络分销（Runcorn，Antaira 官方名录）', '工业交换机专类', 'GB 主攻区工业网络分销 → 维持 A（优先）',
  q='Would a second-source DIN-rail PoE switch be worth a test unit, or do your customers specify one brand only?')
j('XA-M239', 'B', '不动', typ='个人顾问', reason='个人顾问 → B')
j('XA-M240', 'B', '不动', typ='MikroTik 官方讲师（无直达邮箱）', reason='讲师、无邮箱 → B 不动')
j('XA-M241', 'A', '第二封', 'W46', 'KNX/楼宇自动化技术分销（Nottingham/West Sussex，11–50 人，KNX 培训中心）', 'KNX 机柜就是 DIN 轨，DIN 轨 PoE 交换机天然对位', 'GB 主攻区楼宇自动化分销、品类对位 → 维持 A',
  q='Do your KNX installers ask you for DIN-rail PoE switches for the cabinet, or do they source those elsewhere?',
  notes='本轮 web_search 复核：ivoryegg.co.uk/about「technical distributor of the world\'s best building technologies… supply to trade installers」。', angle='KNX 机柜用 DIN 轨 PoE 交换机')
j('XA-M242', 'A', '首触', 'W46', 'UK 网络运营商 + 自营硬件商店（Guildford）', '运营商 + 渠道', 'GB 主攻区、渠道+运营商、未触达 → A 首触（权重中）', kind='dist',
  q='Would either line fit your hardware store, or is it built around a fixed set of brands?')
j('XA-M243', 'A', '首触', 'W46', '工业 IT/OT 技术分销（Redditch，45 人，Kepware/Ewon/OPC；交通/监控/基础设施/自动化）', '工业通信分销，硬件线可加交换机', 'GB 主攻区工业技术分销、未触达 → A 首触', kind='ind',
  to='sales@mac-solutions.co.uk', q='Would a DIN-rail PoE switch line sit alongside your machine-communications hardware, or is switching outside your scope?',
  notes='本轮 web_search 复核：mac-solutions.net「Technical Distributor for hardware and software products… transportation, surveillance, infrastructure and automation」；Companies House 03762835，45 人（2025）。')
j('XA-M244', 'A', '第二封', 'W46', '网络分销（Oxfordshire；Netonix WISP 交换机代理）', '已卖 WISP 工业交换机', 'GB 主攻区分销、已卖 WISP 工业交换机 → 维持 A',
  q='Would a DIN-rail PoE switch be a useful second option next to your WISP switch range?', notes='10-04 来信为工单自动回执 MSD-13577，非真人回复。')
j('XA-M245', 'A', '第二封', 'W46', 'IoT/物联网分销（Teltonika Diamond 级）', '工业路由分销，工业 PoE 配套', 'GB 主攻区 IoT 分销 → 维持 A',
  q='Would an industrial PoE switch next to your industrial-router range be worth a look, or is that segment already covered?')
j('XA-M246', 'B', '不动', typ='综合 IT 转售（Birmingham；Companies House 微型 <10 人）', reason='综合 IT 经纪型转售，难复购 → B', notes='本轮 web_search 复核：Endole 10146519 微型、<10 人；LinkedIn 自称 201–500 不可信。')
j('XA-M247', 'A', '第二封', 'W45', '网络技术分销（Guildford，Disruptive Technology Distribution）', '分销', 'GB 主攻区分销 → 维持 A（优先）',
  q='Is industrial PoE a category your resellers ask for, or would the commercial 24-port line be the better first conversation?')
j('XA-M248', 'A', '首触', 'W46', '工业自动化分销（Hednesford，2014 起；100+ 品牌含 EtherWAN/Hirschmann；西班牙/拉美办事处）', '工业交换机品类现成', 'GB 主攻区工业分销、未触达 → A 首触', kind='ind',
  q='Would a lower-priced DIN-rail PoE switch be worth adding as a second source next to the industrial Ethernet brands you carry?',
  notes='本轮 web_search 复核：pymatek.co.uk「import and distribution of industrial automation products」，Etherwan/Hirschmann 品牌页在线。')
j('XA-M249', 'B', '不动', typ='MikroTik 培训讲师（无直达邮箱）', reason='讲师、无邮箱 → B 不动')
j('XA-M250', 'A', '首触', 'W46', '光模块/交换机专业供应商（Antaira 授权）', '交换机 + 光模块专类', 'GB 主攻区专业供应商、未触达 → A 首触', kind='ind',
  q='Would a DIN-rail PoE switch fit next to your industrial switch range, or is your demand mostly optics?')
j('XA-M251', 'B', '不动', typ='电信设备顾问/转售（Cardiff，1–10 人，新品+翻新）', reason='翻新/经纪型、微型 → B', notes='本轮 web_search 复核：Companies House 09975808，1–10 人，新品+翻新转售。')
j('XA-M252', 'B', '不动', typ='托管 PBX/VoIP 服务商 + 硬件商城（Norwich，工单制）', reason='VoIP 服务商为主、工单回执 → B')
j('XA-M253', 'A', '第二封', 'W45', '网络设备专业电商/分销（Milton Keynes）', '网络专业电商', 'GB 主攻区网络专业电商 → 维持 A',
  q='Would a DIN-rail PoE range be worth listing for your trade customers, or is that outside what broadbandbuyer stocks?')
j('XA-M330', 'B', '不动', typ='小型 ISP/集成（Jellyfish Broadband）', reason='小集成/ISP → B')
j('XA-M331', 'B', '不动', typ='MikroTik 咨询商（Harrogate）', reason='咨询商 → B')
j('XA-M343', 'A', '第二封', 'W45', 'Allied Telesis Premier Partner 转售/集成 + 独立工业以太网线', '工业以太网线现成', 'GB 主攻区、有工业以太网产品线 → 维持 A',
  q='Would a DIN-rail PoE switch at this price be worth a place in your industrial Ethernet range as a second source?')
for c, t in (('XA-M344', 'MSP（Burnley，Platinum Partner）'), ('XA-M345', '安防+网络融合集成商（UK/NL）'), ('XA-M346', '集成商（Platinum Partner）'),
             ('XA-M347', '控制系统 + 网络集成商'), ('XA-M348', '网络集成商'), ('XA-M349', '集成商（仅 social@）'), ('XA-M350', 'IT 转售/VAR（Woking）'),
             ('XA-M351', '安防系统集成商（KP Michelle Hollinshead, Sales & Marketing）'), ('XA-M353', '集成商（无邮箱）'), ('XA-M354', '集成商（Electracom/Trusol）'),
             ('XA-M355', '集成商'), ('XA-M356', '公共部门 IT 转售（Oxford）'), ('XA-M358', 'IT 转售（Hertfordshire）'), ('XA-M360', '安防系统集成商')):
    j(c, 'B', '不动', typ=t, reason='小项目集成商/服务商，非渠道；9–10 月已发未回 → B 慢慢跟进（不进第二封）')
j('XA-M352', 'C', '不动', typ='大型公共部门 IT 服务商（Centerprise）', reason='大 IT 服务商、公共部门为主 → C')
j('XA-M357', 'C', '不动', typ='防务背景 IT（PH15 Ventures）', reason='防务守界 → C')
j('XA-M359', 'B', '不动', typ='数据布线集成（都柏林）', reason='实为爱尔兰（误归属 GB）、集成商 → B 不动', notes='国家应为 IE；下次重建数据时修 iso。')
j('XA-M494', 'A', '第二封', 'W45', 'Perle 授权分销（Newbury）', '工业/串口网络分销', 'GB 主攻区工业网络分销 → 维持 A',
  q='Would a DIN-rail PoE switch be a sensible addition next to your industrial connectivity range?')
j('XA-M506', 'A', '第二封', 'W45', '独立 VAD（£38–45M，58–66 人；wireless/cloud）', 'VAD 规模对口，WISP/户外无线伙伴需要宽温 PoE', 'GB 主攻区 VAD、规模对口 → 维持 A（优先）', to='info@purdicom.com',
  q='Would a hardened PoE line for your WISP and outdoor-wireless partners be worth a conversation with your product team?')

assert len(J) == 98, len(J)

cards = []
for code, jj in J.items():
    r = recs[code]
    iso = r['iso']
    dom = (r.get('domain') or '').lower()
    hits = SB.get(dom, [])
    email = jj['to'] or src_email(r) or (hits[0]['邮箱'] if hits else '')
    sdate = src_date(r)
    evidence = [{'kind': '来源库官网/名录核对', 'claim': clean(r.get('src_note')) or clean(r.get('type')), 'quote': '', 'url': 'https://' + dom + '/' if dom else '', 'date': sdate}]
    if hits:
        h = hits[0]
        subj = re.sub(r'^(MSD-\d+\s*)', '', h['最后主题']).strip() or '24 Port PoE Managed Switch'
        evidence.append({'kind': 'S 箱群发记录', 'claim': 'S 箱 %s 发 %s「%s」，去 %s 来 %s' % (h['首次'], h['邮箱'], h['最后主题'], h['去信'], h['来信']),
                         'quote': '', 'url': 'data/gmail_s/2026-09_10群发名单_未入库.csv', 'date': h['最后']})
        if h['来信'] != '0':
            touch = 'S 箱 %s 群发「%s」→ 机器回执（%s），无真人回复' % (h['首次'], subj, h['最后主题'])
        else:
            touch = 'S 箱 %s 群发「%s」→ 已发未回' % (h['首次'], subj)
        opener = ("I wrote on %s about our 24-port PoE L2+ switch ('%s'); this is a different product line, so a fresh note rather than a reply."
                  % (date_en(h['首次']), subj))
        if h['来信'] != '0':
            opener = ("My note on %s about our 24-port PoE L2+ switch landed in your ticket system (%s), so I am sending this once more to the sales side; "
                      "it is a different product line anyway." % (date_en(h['首次']), h['最后主题'].split(' ')[0]))
    else:
        touch = 'S 箱 9–10 月群发名单未见本域 → 未触达'
        opener = ''
    act = jj['act']
    if act == '第二封' and not hits:
        act = '首触'  # 没发过就不叫第二封
        jj['kind'] = jj['kind'] or 'dist'
    nm = {'action': act, 'angle': jj['angle'] or ('STI 工业 L2+ PoE（MikroTik 无此品类）' if act == '第二封' else ('工业 DIN 轨 PoE 首触' if jj['kind'] == 'ind' else '分销首触：24 口 PoE + STI 工业线')),
          'model': 'STI-288DGGPM' if (act == '第二封' or jj['kind'] == 'ind') else 'STC-424XGGPM-280W / STI-288DGGPM',
          'price': SNAP if (act == '第二封' or jj['kind'] == 'ind') else SNAP24 + ' / ' + SNAP,
          'window': WINDOW[iso] if act in ('第二封', '首触') else '', 'when': WHEN.get((iso, jj['slot']), '') if act in ('第二封', '首触') else ('不动' if act == '不动' else '')}
    card = dict(code=code, name=r['name'], round=R, researched_at=D,
                alive='来源库 %s 核对在线；本轮未复查' % sdate if '复核' not in jj['notes'] else '本轮 web_search 复核在线（2026-10-27）',
                summary=jj['typ'] + ('；' + clean(r.get('entry_point'), 160) if r.get('entry_point') else ''),
                type_final=jj['typ'], size='未量化' if '人' not in jj['typ'] else jj['typ'], brands_seen=[b.strip() for b in re.split(r'[+/,，、]', r.get('signals') or '') if b.strip()][:8],
                saga_line='SmartByte 商用 L2+（已发/首触）+ Saga STI 工业 L2+ PoE 补位' if jj['g'] == 'A' else '—',
                fit=jj['fit'], evidence=evidence,
                contacts={'email': email, 'email_status': '来源库公开邮箱' if email else '缺', 'kp': jj['kp']},
                touch_status=touch, saga_overlap='无', grade_final=jj['g'], grade_reason_final=jj['reason'], next_move=nm,
                notes=(jj['notes'] + ' ' if jj['notes'] else '') + ('' if '复核' in jj['notes'] else LIGHT))
    if act in ('第二封', '首触'):
        if act == '第二封':
            body = jj['lead'] + "\n\n" + opener + "\n\n" + ind_block(iso) + "\n\n" + jj['q'] + SIG
            subject = 'Industrial DIN-rail PoE switches - the category MikroTik does not cover' if 'MikroTik' in (r.get('type') or '') or 'WISP' in jj['typ'] \
                else 'A second-source DIN-rail PoE switch for your industrial customers'
        else:
            body = jj['lead'] + "\n\n" + (ind_intro(iso) if jj['kind'] == 'ind' else dist_intro(iso)) + "\n\n" + jj['q'] + SIG
            subject = 'DIN-rail industrial PoE switches - second source for your line card' if jj['kind'] == 'ind' else 'L2+ PoE and industrial switches for your reseller channel'
        card['draft_en'] = {'subject': subject, 'body': body}
        assert email, code
    cards.append(card)

for c in cards:
    put(c)
from collections import Counter
print('mik R02 cards', len(cards), Counter(c['grade_final'] for c in cards), Counter(c['next_move']['action'] for c in cards),
      Counter(c['next_move']['when'] for c in cards if c['next_move']['action'] in ('第二封', '首触')))
