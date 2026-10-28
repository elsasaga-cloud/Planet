# -*- coding: utf-8 -*-
"""波 2 通用机制（R05 起）：三库记录 + S 箱群发名单 → 研究卡；人工判断由各批次脚本的 J 表提供。
用法：from w2lib import j, run；定义 J 后 run(J, R)。"""
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import DATA, ROOT  # noqa: E402
from research_store import put  # noqa: E402

D = '2026-10-27'
R = 'W2'
SIG = "\n\nSimon\nSaga Telecom - sagatele.com"
SNAP = 'USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
SNAP24 = 'USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)'
CERT_DEFAULT = 'CE'
CERT = {'CA': 'FCC/ISED', 'US': 'FCC/CE', 'GB': 'UKCA/CE', 'TR': 'CE'}


def cert(iso):
    return CERT.get(iso, CERT_DEFAULT)
WHEN_EU = {'W46': '2026-11-12', 'W47': '2026-11-19', 'W48': '2026-11-26', 'W49': '2026-12-03', 'W50': '2026-12-10', 'W51': '2026-12-17'}
WHEN_CA = {'W46': '2026-11-11', 'W47': '2026-11-18', 'W48': '2026-11-25', 'W49': '2026-12-02', 'W50': '2026-12-09'}
SNAP86 = 'USD 86'
def window(iso):
    return 'CA 周三 08–10 当地' if iso in ('CA', 'US') else iso + ' 周四 12–14'


def when(iso, slot):
    return (WHEN_CA if iso in ('CA', 'US') else WHEN_EU).get(slot, '')
LIGHT = '轻卡：本轮未外查，沿用来源库官网/名录核对。'
REPO_FILE = {'E': 'edgecore.json', 'M': 'mikrotik.json', 'C': 'cctv.json'}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def ind_block(iso):
    return ("STI-288DGGPM: DIN-rail industrial L2+ switch, 8 x GE PoE+ (240 W budget) + 2 x SFP (1G/2.5G), -40 to +75 C, dual DC input, "
            "ERPS ring, SNMPv3, %s, %s/RoHS, 3-year warranty. Same family: STI-244DGGPM (4 x PoE+ + 2 x SFP, 120 W) at USD 121 and "
            "STI-488DGGPM (8 x PoE+ + 4 x SFP, 240 W) at USD 147." % (SNAP, cert(iso)))


def dist_intro(iso):
    return ("Saga Telecom supplies network distributors with Marvell-based L2+ PoE switches and Centec-based L3 10G/25G/100G switches, "
            "under our label or the distributor's own, %s. Two lines that usually interest MikroTik and WISP channels:\n\n"
            "- STC-424XGGPM-280W: 24 x GE PoE+ (280 W) + 4 x 10G SFP+, L2+ managed, %s.\n"
            "- %s" % (cert(iso), SNAP24, ind_block(iso)))


def ind_intro(iso):
    return ("Saga Telecom builds DIN-rail industrial Ethernet switches for distributors who already carry automation and industrial "
            "communication brands and want a second source at a lower price point, %s.\n\n%s" % (cert(iso), ind_block(iso)))


def date_en(iso_date):
    y, m, d = iso_date.split('-')
    return '%d %s' % (int(d), MONTHS[int(m) - 1])


def dist2_block(iso):
    return ("Three PoE switches our distributor partners move most, all EXW Shenzhen (snapshot 2026-10-27, valid 15 days), %s, under our label or yours:\n\n"
            "- STC-2224GP: 24 x GE PoE+ (300 W) + 2 x GE + 2 x SFP, USD 86.\n"
            "- STC-424XGGPM-280W: 24 x GE PoE+ (280 W) + 4 x 10G SFP+, Marvell-based L2+ managed, USD 170.\n"
            "- STI-288DGGPM: DIN-rail industrial L2+, 8 x GE PoE+ (240 W) + 2 x SFP, -40 to +75 C, USD 137, 3-year warranty (12 months on the commercial units)." % cert(iso))


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



def dist2_intro(iso):
    return ("Saga Telecom supplies network and security distributors with PoE and industrial switches, under our label or the distributor's own, %s.\n\n%s"
            % (cert(iso), dist2_block(iso)))


def j(J, code, g, act, slot=None, typ='', fit='', reason='', lead='Hi,', q='', to=None, kp=None, notes='', kind=None, angle='', force_first=False, hits_domain=None):
    J[code] = dict(g=g, act=act, slot=slot, typ=typ, fit=fit, reason=reason, lead=lead, q=q, to=to, kp=kp or [], notes=notes, kind=kind, angle=angle,
                   force_first=force_first, hits_domain=hits_domain)


CONS = '顾问/培训/小集成商，非渠道 → B（不进第二封）'
ATP = '小项目集成商（Allied Telesis 伙伴名录批量导入），非渠道 → B 慢慢跟进'


def run(J, R, expect=None):
    if expect is not None:
        assert len(J) == expect, len(J)

    cards = []
    for code, jj in J.items():
        r = recs[code]
        iso = r['iso']
        dom = (r.get('domain') or r.get('website') or '').split(' ')[0].lower()
        hits = [] if jj['force_first'] else SB.get(jj['hits_domain'] or dom, [])
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
                intro = ind_intro(iso) if is_ind else (dist2_intro(iso) if jj['kind'] == 'dist2' else dist_intro(iso))
                body = jj['lead'] + "\n\n" + intro + "\n\n" + jj['q'] + SIG
                subject = 'DIN-rail industrial PoE switches - second source for your line card' if is_ind else ('PoE switch line for your reseller channel - distributor pricing' if jj['kind'] == 'dist2' else 'L2+ PoE and industrial switches for your reseller channel')
            card['draft_en'] = {'subject': subject, 'body': body}
        cards.append(card)

    for c in cards:
        put(c)
    from collections import Counter
    print(R, 'cards', len(cards), Counter(c['grade_final'] for c in cards), Counter(c['next_move']['action'] for c in cards),
          Counter(c['next_move']['when'] for c in cards if c['next_move']['action'] in ('第二封', '首触')))
