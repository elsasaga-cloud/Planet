# -*- coding: utf-8 -*-
"""波 2 R05 批 b：意大利 66。web_search 5 家（ABES / Aikom / Fiore / SICE / EFA Automazione）。Allied Telesis 伙伴名录批量导入 41 家一律 B。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2lib import j as _j, run, CONS, ATP

J = {}
def j(*a, **k): _j(J, *a, **k)

# --- 分销 / 渠道 ---
j('XA-C0006', 'A', '首触', 'W48', '安防专业分销（ABES S.r.l.，Torino；1985 起，Hikvision 皮埃蒙特/利古里亚/奥斯塔分销，防火/防盗/TVCC，三处门市，5–9 人）', '安防批发，PoE 配摄像机', 'IT 区域安防分销、未触达 → A 首触', kind='dist2', to='info@abes.it',
  notes='本轮 web_search：abes.it/azienda「2012 … distribuzione per Piemonte Liguria e Val D\'Aosta con Hikvision」；europages 5–9 人。',
  q='Which would be worth a sample for your installers first - the 24-port entry PoE switch or the DIN-rail unit?')
j('XA-C0007', 'B', '不动', typ='全国性 IT 广线分销（Computer Gross S.p.A.，Sesa 集团）', reason='大型广线分销，决策链长 → B')
j('XA-M022', 'A', '首触', 'W48', '增值分销 VAD（Aikom Technology S.r.l.，Riccione + Milano；2006 起，Teltonika Gold，另代理一家台系交换机品牌含工业线，B2B 电商 go.aikomtech.com）', '交换机/工业交换机品类现成，VAD 规模对口', 'IT VAD、交换机品类现成、未触达 → A 首触（优先）', kind='dist2',
  notes='本轮 web_search：aikomtech.com 「value-added distributor」「GOLD Teltonika Networks distributor for Italy」；品牌页含 LAN Switch 与 Industrial Switch（台系同行品牌，文案不点名）。',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
j('XA-M028', 'A', '首触', 'W48', '工业通信分销（EFA Automazione S.p.A.，Cernusco sul Naviglio；1988 起，约 34 人，HMS/N-Tron/eWON 意大利分销，Relatech 集团）', '工业交换机品类现成（N-Tron）', 'IT 工业通信分销、未触达 → A 首触', kind='ind', to='vendite@efa.it',
  notes='本轮 web_search：efa.it/marchio/n-tron；contactout 34 人；集团归属不入文案。',
  q='Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to the industrial switches you carry?')
j('XA-M132', 'B', '不动', typ='ALLNET 集团意大利分销（Allnet.Italia S.p.A.，Bologna；MikroTik 官方分销）', reason='自有 ALLNET 品牌同行集团 → B')
j('XA-M134', 'A', '第二封', 'W48', '托管商 + MikroTik 官方分销（C1V Hosting，Roma/Pomezia，自营 AS）', 'MikroTik 渠道', 'IT MikroTik 分销 → 维持 A（轻卡，主业托管）',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M136', 'A', '第二封', 'W48', 'MikroTik 官方分销（Dnet-Distribution，Lainate MI）', 'MikroTik 渠道', 'IT MikroTik 分销 → 维持 A',
  q='Do your reseller customers ask for DIN-rail PoE switches, or is that a category you have not needed to stock?')
j('XA-M139', 'A', '首触', 'W48', '无线网络网店 + 经销商价（SELIT s.r.l. / wirmax.net，Bastia Umbra；MikroTik CRS 在售）', 'MikroTik 渠道，交换机已是品类', 'IT MikroTik 渠道、未触达 → A 首触', kind='dist', to='info@selit.it',
  q='Would either line be relevant for your dealer customers, or is switching fully covered today?')
j('XA-M140', 'A', '第二封', 'W48', '通信设备制造商 + 增值分销（SICE Telecomunicazioni，Lucca；1980 起，51–200 人；自产无线/WiFi/CCTV/VoIP 设备，意大利分销 Ubiquiti/MikroTik/Cambium/Hikvision）', '品牌商 + 分销双重身份：可谈贴牌（OEM 30%）亦可谈分销', 'IT 品牌商兼分销 → 维持 A（优先；品牌商为首选客户类型）', kind='dist2',
  notes='本轮 web_search：sicetelecom.it/azienda/profilo-aziendale「Oltre alla produzione della propria linea di prodotti, SICE è distributore per l\'Italia…」；LinkedIn 51–200 人。',
  q='Would a PoE switch under the SICE label be of interest, or is distribution of our label the more natural fit for your catalogue?')
j('XA-M142', 'A', '第二封', 'W48', 'WISP 网店（WISP STORE SRLS，Fisciano SA；Ubiquiti/MikroTik/TP-Link 经销）', 'WISP 渠道', 'IT WISP 渠道 → 维持 A（轻卡，小）',
  q='Would a DIN-rail PoE switch be worth listing for your WISP customers, or is that outside what they ask for?')
j('XA-M143', 'A', '第二封', 'W48', 'WISP 渠道分销（WispMax，Cagli PU；MikroTik 官方分销，站内已推工业 PoE 交换机）', 'WISP 渠道，工业 PoE 已是品类', 'IT WISP 分销、品类契合 → 维持 A',
  q='Would a second-source DIN-rail PoE switch be worth a test unit next to the industrial PoE models you list today?')
j('XA-M302', 'A', '第二封', 'W48', '网络/无线分销（ELMAT S.p.A.；Netonix 授权，WISP 渠道）', 'WISP 交换机品类现成', 'IT 网络分销 → 维持 A',
  q='Would a DIN-rail PoE line be relevant for your WISP customers next to the outdoor switches you carry?')
j('XA-M338', 'B', '不动', typ='MSP（Nabacom，Allied Telesis 伙伴）', reason=ATP)
j('XA-M440', 'A', '第二封', 'W48', '全国性 ICT 分销（Fiore S.r.l.，Paderno Dugnano MI；1983 起，11–50 人，综合布线/网络/UCC，米兰/维琴察/罗马/巴里，自产 19 英寸机柜）', '网络分销，服务 VAR/SI', 'IT 网络分销、规模对口 → 升 A（原 Allied 名录导入）', kind='dist2',
  notes='本轮 web_search：fioresrl.com「Dal 1983 Fiore si occupa della distribuzione di Cablaggio strutturato, Networking e Telefonia IP」；公司简介 PDF 2025-11。',
  q='Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?')
# --- MikroTik 顾问/讲师 12 ---
for c, t in (('XA-M023', '顾问（mikrotik-training.it）'), ('XA-M024', '顾问/讲师（1off）'), ('XA-M025', '顾问（Bitmagic）'), ('XA-M026', '顾问/讲师（TikTrain）'), ('XA-M027', '顾问（Netify）'),
             ('XA-M029', '讲师（Grifonline）'), ('XA-M030', '顾问公司（PF Tech）'), ('XA-M133', '顾问（Matrix Computers）'), ('XA-M135', '培训机构（CorsiMikrotik）'), ('XA-M137', '顾问/小 ISP（Spadhausen，常驻摩尔多瓦）'),
             ('XA-M138', '顾问（Fastnet）'), ('XA-M141', '小集成商（Byte Solutions）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
# --- Allied Telesis 伙伴名录批量导入 40（Fiore 已升 A 单列）---
ATL = {'XA-M427': 'A.G.informatica', 'XA-M428': 'Adrianet', 'XA-M429': 'Agomir', 'XA-M430': 'C.G.T. Elettronica', 'XA-M432': 'Computer Time', 'XA-M433': 'Connect ICS', 'XA-M434': 'CTC Systems',
       'XA-M435': 'Dps Informatica', 'XA-M436': 'Emilia Informatica', 'XA-M437': 'Eulogic NT', 'XA-M438': 'Evergreen1', 'XA-M439': 'Farpoint', 'XA-M441': 'Gecopra', 'XA-M442': 'General Computer Italia',
       'XA-M443': 'GIS（Hu.Tech Group）', 'XA-M444': 'Goretti Technological Systems', 'XA-M445': 'I&SI', 'XA-M446': 'IFI Consulting', 'XA-M447': 'Irene', 'XA-M448': 'JM Consulting', 'XA-M449': 'Localnet Firenze',
       'XA-M450': 'ML Software', 'XA-M451': 'N&C Telecomunicazioni', 'XA-M452': 'NA.EL', 'XA-M453': 'Net Engineering', 'XA-M454': 'Net System Innovazione', 'XA-M455': 'Newsoft Technology', 'XA-M456': 'Omniconnect',
       'XA-M457': 'PAM Ufficio', 'XA-M458': 'Securcrea', 'XA-M459': 'Sfera Informatica', 'XA-M460': 'SI.EL.CO.', 'XA-M461': 'SIM NT', 'XA-M462': 'Sotech', 'XA-M463': 'SSC', 'XA-M464': 'Storelink',
       'XA-M465': 'T.net', 'XA-M466': 'Techno Center', 'XA-M467': 'World Technology（无官网，tiscali 邮箱）'}
for c, n in ATL.items():
    j(c, 'B', '不动', typ='IT 集成商/VAR（%s）' % n, reason=ATP)
j('XA-M431', 'B', '不动', typ='卫星/安防安装商（CAMELI SAT）', reason=ATP + '；且无可用邮箱')

run(J, 'W2-R05b', expect=66)
