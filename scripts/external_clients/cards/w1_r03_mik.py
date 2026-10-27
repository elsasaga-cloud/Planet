# -*- coding: utf-8 -*-
"""波 1 第 3 轮（收官）：mikrotik-info XA 德国 73 家研究卡（数据驱动：公司事实取自来源库记录 + S 箱群发名单；
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
R = 'W1-R03'
SIG = "\n\nSimon\nSaga Telecom - sagatele.com"
SNAP = 'USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
SNAP24 = 'USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
CERT = {'US': 'FCC/CE', 'GB': 'UKCA/CE', 'DE': 'CE'}
WHEN = {('DE', 'W46'): '2026-11-12', ('DE', 'W47'): '2026-11-19'}
WINDOW = {'DE': 'DE 周四 12–14'}
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


# ---- 人工判断表 J（德国 73）----
J = {}


def j(code, g, act, slot=None, typ='', fit='', reason='', lead='Hi,', q='', to=None, kp=None, notes='', kind=None, angle=''):
    J[code] = dict(g=g, act=act, slot=slot, typ=typ, fit=fit, reason=reason, lead=lead, q=q, to=to, kp=kp or [], notes=notes, kind=kind, angle=angle)


CONS = '小项目集成商/系统之家（Allied Telesis 伙伴名录批量导入），非渠道；9–10 月已发未回 → B 慢慢跟进（不进第二封）'
# 唯一 A：ATEG（本轮 web_search 复核）
j('XA-M123', 'A', '第二封', 'W46', '工业自动化组件分销（Remscheid，1995 起，>1000 客户；HMS Networks Strategic Partner 2026-03；2–10 人）', '工业网络技术在其产品线内，STI 做第二供应商',
  'DE 主攻区工业自动化分销、HMS 战略伙伴 → 维持 A', q='Would a DIN-rail PoE switch at this price be worth a test unit for your panel-builder and machine-builder customers?',
  notes='本轮 web_search 复核：ateg.de/ueber-uns「1995 als Vertriebsgesellschaft für Komponenten der Automatisierungstechnik… über 1000 Kunden」；ateg.de/news 2026-03-04 HMS Networks Strategic Partner；implisense：industrielle Netzwerktechnik 在产品线内。')
# MikroTik 认证顾问 / ISP / 运营商 → B
j('XA-M016', 'B', '不动', typ='IT 安全/网络公司内的 MikroTik 认证顾问（Bremen）', reason='顾问/IT 安全公司，非渠道 → B')
j('XA-M017', 'B', '不动', typ='光纤接入 ISP（Westhofen）', reason='ISP 终端买家、小 → B')
j('XA-M018', 'B', '不动', typ='WISP/运营商（Karlsbad，自建骨干）', reason='运营商终端买家 → B（若回信可直接报 STI）')
j('XA-M019', 'B', '不动', typ='个人顾问（München）', reason='个人顾问 → B')
j('XA-M020', 'B', '不动', typ='RouterOS 咨询/培训（Oberhausen）', reason='顾问/培训 → B')
j('XA-M126', 'B', '不动', typ='个人顾问（Marburg）', reason='个人顾问 → B')
j('XA-M129', 'C', '并线', typ='= XA-M124 FMS Internetservice GmbH（同公司顾问，已研究、10-29 第二封）', reason='同公司并线 → C')
j('XA-M296', 'C', '并线', typ='= XA-M124 FMS Internetservice GmbH（已研究、10-29 第二封）', reason='同公司重复 → C 并线')
j('XA-M297', 'B', '不动', typ='MikroTik 支持/咨询/实施（Hamburg）', reason='咨询实施商 → B')
j('XA-M299', 'C', '不动', typ='原 WISP 器材分销（meconet e.K.）— 官网公告退出电子市场，只清库存、专做天线/射频配件/电源', reason='已退出交换机业务 → C',
  notes='本轮 web_search 复核：meconet.de/mikrotik.html「meconet e.K. is withdrawing from the electronics market! Currently, we are only selling our inventory」。')
j('XA-M301', 'C', '并线', typ='= XA-M021 VARIA System GmbH（已研究、10-29 第二封）', reason='同集团重复 → C 并线')
j('XA-M329', 'B', '不动', typ='元器件/嵌入式分销（Lantronix 授权，design-in；atestore.de）', reason='元器件 design-in 分销，非交换机渠道 → B')
j('XA-M339', 'B', '不动', typ='MSP（Allied Telesis 伙伴）', reason=CONS)
# Allied Telesis 伙伴名录 → B（小系统之家/集成商）
for c, t in (('XA-M361', 'IT 服务（Reken/Velen）'), ('XA-M364', '安防技术（Schwerin）'), ('XA-M365', 'IT 系统集成（Idstein）'), ('XA-M366', 'IT 系统之家（Apfelstädt）'),
             ('XA-M367', 'IT 系统之家（Weißenburg）'), ('XA-M368', '船用电子/集成（Wilhelmshaven，Sperry Marine 伙伴）'), ('XA-M369', 'IT 系统之家（Wetzlar）'), ('XA-M370', 'IT 系统之家（Böhl-Iggelheim）'),
             ('XA-M371', '中小企业网络/布线（Chemnitz）'), ('XA-M372', 'IT 系统之家（Stadtlohn，dataVISIONgroup）'), ('XA-M373', 'IT 系统之家（Albstadt）'), ('XA-M376', '区域运营商（Dessau）'),
             ('XA-M377', 'IT 系统之家（Köln）'), ('XA-M378', 'IT 系统之家（Dresden）'), ('XA-M379', '特种电缆分销（Quickborn）'), ('XA-M380', 'IT 系统之家（Bergneustadt）'),
             ('XA-M385', 'IT 系统之家（Bonn）'), ('XA-M386', '电子/IT（Dillingen）'), ('XA-M387', '报警/消防技术（Hamburg）'), ('XA-M388', 'IT 系统之家（Berlin，Integrate Elite）'),
             ('XA-M389', 'IT 系统之家（Traunstein）'), ('XA-M390', 'IT 系统之家（Burgwedel）'), ('XA-M392', 'IT 咨询（Köln）'), ('XA-M393', 'IT 系统之家（Frankenberg）'),
             ('XA-M394', 'IT 系统之家（Mühldorf）'), ('XA-M395', 'IT 系统之家（Tübingen）'), ('XA-M396', 'IT 系统之家（Boppard，Integrate Elite）'), ('XA-M397', 'IT 系统之家（Bayern）'),
             ('XA-M398', 'IT 系统之家（Spardorf）'), ('XA-M399', 'IT 服务（Wiehl）'), ('XA-M400', 'IT 系统之家（Meerane）'), ('XA-M401', 'IT 系统之家（Augsburg，accompio 集团）'),
             ('XA-M402', 'IT 系统之家（Berlin；einkauf@ 已停用 2026-10-04）'), ('XA-M403', 'IT 系统之家（Ampfing）'), ('XA-M404', 'IT 服务（Bremen，OAS AG）'), ('XA-M405', 'IT 系统之家（Brackenheim）'),
             ('XA-M406', '安防集成（PKE 集团 Berlin 分部）'), ('XA-M408', '电气技术（Frankfurt）'), ('XA-M409', 'IT 系统之家（München）'), ('XA-M410', 'IT 系统之家（Wilhelmshaven）'),
             ('XA-M411', '公共广播/数据通信/IP 照明（Frankfurt）'), ('XA-M413', 'IT 系统之家（Bochum）'), ('XA-M414', 'IT 系统之家（Hochdorf-Assenheim）'), ('XA-M416', 'IT 系统之家（Neuss）'),
             ('XA-M417', 'IT 系统之家（Stuttgart）'), ('XA-M418', '电气技术（Korntal-Münchingen）')):
    j(c, 'B', '不动', typ=t, reason=CONS)
j('XA-M402', 'B', '不动', typ='IT 系统之家（Berlin）', reason=CONS, notes='einkauf@nitoit.de 已停用（2026-10-04），再触达改 vertrieb@/kontakt@。')
# 大 / 守界 / 同行 / 集团重复 → C
j('XA-M362', 'C', '不动', typ='大型 IT 集团分支（ACP，Halle）', reason='大集团 → C')
j('XA-M363', 'C', '不动', typ='物流软件商（Acteos 德国子公司）', reason='不对口 → C')
j('XA-M374', 'C', '不动', typ='军事通信方向 IT（dainox）', reason='军用守界 → C')
j('XA-M375', 'C', '不动', typ='视频安防厂商（Dallmeier，自有品牌）', reason='同行厂商 → C', notes='9-29 来信与发信同分钟、单条入站 → 按自动回执处理，非真人回复。')
j('XA-M381', 'C', '不动', typ='TEMPEST/防务 IT（Diepholz）', reason='防务守界 → C')
j('XA-M382', 'C', '不动', typ='建筑五金集团总部（Gretsch-Unitas，Ditzingen）', reason='终端/大集团 → C')
j('XA-M383', 'C', '并线', typ='= XA-M382 Gretsch-Unitas（Berlin 分支）', reason='同集团并线 → C')
j('XA-M384', 'C', '并线', typ='= XA-M382 Gretsch-Unitas（GU BKS Service）', reason='同集团并线 → C')
j('XA-M391', 'C', '不动', typ='全球 IT 巨头德国法人（Insight）', reason='大 → C')
j('XA-M407', 'C', '不动', typ='大型 IT 服务商（prego services）', reason='大 → C')
j('XA-M412', 'C', '不动', typ='大型系统集成集团（TELCAT MULTICOM）', reason='大 → C')
j('XA-M415', 'C', '不动', typ='电子制造/方案集团（TQ-Systems）', reason='EMS 集团、非买家 → C')
j('XA-M509', 'B', '不动', typ='自有品牌配件商（goobay，Braunschweig；来源库未建档、无邮箱）', reason='OEM 潜在但无邮箱、未核 → B 待补', notes='若做 OEM 线，先补 Einkauf 邮箱再首触。')

assert len(J) == 73, len(J)


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
print('mik R03 cards', len(cards), Counter(c['grade_final'] for c in cards), Counter(c['next_move']['action'] for c in cards),
      Counter(c['next_move']['when'] for c in cards if c['next_move']['action'] in ('第二封', '首触')))
