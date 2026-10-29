#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-T01 · 长期客户群骨架档桌面加厚（Saga 201 户：C 池捞出的 SC 196 + 邮件证据 SB 5）· T29-U131 2026-10-29。

Simon U131：「A / B 都深挖过了吗？加厚 审核 交叉检查等等 把没有的都再搞一下」。
骨架档 = LT-01 并池时只有三闸结论的研究档（type / evidence / kp / company_facts / saga_fit 全空）。
本批**不新增网查**：把已经查过、散落在 sieve.json（闸 1 对位 / 闸 2 坐实）、registry/*.json（登记底数：法定名 / 登记号 / 状态 /
地址 / 董事 / 来源 URL）、lt_review（复核结论）、entities.json（表内邮箱 / 兴趣）里的事实整合进研究档的标准字段，
型号对位按「类型 + 档位」给默认值并标明「默认 · 官网快照后校正」。官网快照由每日 Actions 补抓（见 lt_gap_audit.py）。
幂等：deep.batch == 'LT-T01' 跳过。不改等级。
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA  # noqa: E402

R = os.path.join(DATA, 'research')
DATE = '2026-10-29'
BATCH = 'LT-T01'
BRANDS = ['Utepo', 'Hikvision', 'Dahua', 'TP-Link', 'Ubiquiti', 'MikroTik', 'PLANET', 'Planet', 'Cisco', 'Netgear', 'D-Link', 'Zyxel', 'Moxa',
          'Hirschmann', 'Phoenix Contact', 'Westermo', 'Teltonika', 'Aruba', 'Huawei', 'ONV', 'ORing', 'Korenix', 'EtherWAN', 'Antaira',
          'Allied Telesis', 'Edgecore', 'Ruijie', 'Reyee', 'Grandstream', 'Uniview', 'Axis', 'Hanwha', 'Bosch', 'H3C', 'Juniper', 'Extreme',
          'Fortinet', 'Tenda', 'Mercusys', 'Cudy', 'Netis', 'Ruckus', 'Cambium', 'LigoWave', 'Mimosa', 'Perle', 'Black Box', 'Lantech',
          'Advantech', 'Red Lion', 'Siemens', 'Weidmüller', 'Beckhoff', 'Schneider', 'Belden', 'Panduit', 'CommScope', 'Legrand', 'Digitus',
          'Intellinet', 'TRENDnet', 'LevelOne', 'Netonix', 'Wi-Tek', 'Totolink', 'IP-COM', 'Vivotek', 'Provision-ISR', 'Milesight', 'Reolink',
          'Tiandy', 'HRUI', 'Microsens', 'Corning', 'Fiberhome', 'ZTE', 'Yeastar', 'Ubiquiti', 'Mikrotik', 'Avigilon', 'Pelco', 'Honeywell']
TYPE_PAT = re.compile(r'(?:^|[·：:\s）)])([^·：:（()\s][^·：:（()]{1,18}?)\s*(20|25|30)%')


def load(p):
    return json.load(open(p, encoding='utf-8'))


def registry():
    reg = {}
    for f in glob.glob(os.path.join(DATA, 'registry', '*.json')):
        reg.update(load(f)['rows'])
    return reg


def brands_in(*texts):
    t = ' '.join(x for x in texts if x)
    low = t.lower()
    out = []
    for b in BRANDS:
        if b.lower() in low and b not in out and b.lower() != 'planet' or (b == 'PLANET' and 'planet' in low and 'PLANET' not in out):
            out.append(b)
    return [b for b in out if b != 'Mikrotik' or 'MikroTik' not in out][:8]


def default_p1(label, tier):
    lab = label or ''
    if tier == 30:
        return 'STC-424XGGPM-280W', '贴牌 / 自有品牌线起手：24 GE PoE + 4×10G SFP+ L2+ 管理型（30% 档）'
    if tier == 25:
        if re.search(r'工业|自动化|电力|EPC|矿|轨|能源|石油|ISP|WISP|运营', lab):
            return 'STI-288GPM', '工业 / 项目集成起手：DIN 导轨 8 GE PoE + 2 SFP 管理型（25% 档）'
        return 'STC-2216GP', '项目集成起手：16 GE PoE + 2 SFP 管理型（25% 档）'
    return 'STC-228GP', '分销走量起手：8 GE PoE + 2 SFP（20% 档）'


def parse_type(g2, g1, note):
    for txt in (g2, note, g1):
        m = TYPE_PAT.search(txt or '')
        if m:
            label = m.group(1).strip(' ·')
            label = re.sub(r'^[★○△☆\s]+', '', re.sub(r'^(?:观察档|长线|冷户)\s*', '', label)).strip()
            return label, int(m.group(2))
    for txt in (g2, g1, note):
        t = txt or ''
        for kw, tier in (('品牌商', 30), ('OEM', 30), ('自有品牌', 30), ('分销', 20), ('批发', 20), ('进口', 20), ('经销', 20), ('集成', 25), ('安装', 25),
                         ('ISP', 25), ('WISP', 25), ('运营商', 25), ('终端', 25), ('自用', 25), ('直客', 25)):
            if kw in t:
                return kw, tier
    return '', 0


def thicken(code, j, sv, reg, ent):
    g1 = sv.get('g1_reason') or ''
    g2 = sv.get('g2_reason') or sv.get('reason') or ''
    lt = j.get('lt_review') or {}
    note = lt.get('note') or ''
    rg = reg.get(code) or {}
    doms = ent.get('domains') or []
    emails = ent.get('corp_emails') or ent.get('emails') or []
    label, tier = parse_type(g2, g1, note)
    changed = []
    if not j.get('type'):
        j['type'] = f'{label}（闸 2 判定 · {tier}% 档）' if label else '待定（闸 2 未分型；官网快照后定）'
        changed.append('type')
    if not j.get('size') and rg.get('size_band'):
        j['size'] = rg['size_band']
        changed.append('size')
    if not j.get('website_status'):
        st = rg.get('status') or ''
        j['website_status'] = (st if any(k in st for k in ('营业', 'Active', 'active', '在线', '存续')) else '') or (
            f'域名 {doms[0]}（官网快照待 Actions 补抓）' if doms else '无域名（仅表内信息）')
        changed.append('website_status')
    if rg.get('name') and (not j.get('name_official') or j['name_official'] == ent.get('name') or '.' in j.get('name_official', '')):
        j['name_official'] = rg['name'].split('（')[0].split('；')[0][:120]
        changed.append('name_official')
    bs = brands_in(g1, g2, note, ' '.join(ent.get('interests') or []), rg.get('name', ''))
    if not j.get('brands_seen') and bs:
        j['brands_seen'] = bs
        changed.append('brands_seen')
    if not j.get('evidence'):
        ev = []
        if rg:
            ev.append({'kind': '登记底数 / 官网（闸 2 坐实）', 'claim': (rg.get('name') or '')[:240], 'quote': (rg.get('source') or '')[:400],
                       'url': rg.get('url') or '', 'date': rg.get('fetched') or DATE})
        if g1:
            ev.append({'kind': '闸 1 对位', 'claim': g1[:300], 'quote': '', 'url': '', 'date': sv.get('date') or DATE})
        if note:
            ev.append({'kind': f"长期群复核 {lt.get('batch', '')}", 'claim': note[:300], 'quote': '', 'url': '', 'date': lt.get('verdict_date') or DATE})
        j['evidence'] = ev
        changed.append('evidence')
    if not j.get('kp') and emails:
        j['kp'] = [{'name': '—', 'role': '表内邮箱（公开 / 总机）', 'email': e, 'phone': ''} for e in emails[:3]]
        changed.append('kp')
    if not j.get('company_facts') and rg:
        j['company_facts'] = {k: rg.get(k2) for k, k2 in (('legal_name', 'name'), ('reg_no', 'number'), ('status', 'status'), ('incorporated', 'incorporated'),
                                                           ('company_type', 'company_type'), ('address', 'address'), ('size_band', 'size_band'),
                                                           ('officers', 'officers'), ('psc', 'psc'), ('source', 'source'), ('url', 'url'), ('fetched', 'fetched'))}
        j['company_facts']['legal_name'] = (rg.get('name') or '').split('（')[0].split('；')[0][:120]
        changed.append('company_facts')
    if not j.get('business_lines') and rg.get('sic'):
        j['business_lines'] = list(rg['sic'])[:6]
        changed.append('business_lines')
    if not j.get('channels'):
        ch = {}
        if doms:
            ch['网站'] = 'https://' + doms[0]
        if emails:
            ch['直邮'] = '，'.join(emails[:3]) + '（表内）'
        if ch:
            j['channels'] = ch
            changed.append('channels')
    if not j.get('signals'):
        sig = [x for x in [g1[:200], ('表内兴趣：' + '；'.join(ent.get('interests') or [])) if ent.get('interests') else ''] if x]
        if sig:
            j['signals'] = sig
            changed.append('signals')
    if not j.get('risks'):
        rk = [ln[:200] for ln in (rg.get('lines') or []) if re.search(r'退信|无 MX|风险|制裁|收款|KC|未坐实|部分坐实|dormant|停|注销|清算', ln)]
        if '未取' in str(rg.get('number')) or not rg:
            rk.append('登记号未取 → 部分坐实；开 PI 前核对法定名 / 税号')
        if rk:
            j['risks'] = rk[:5]
            changed.append('risks')
    if not j.get('saga_fit'):
        p1, why = default_p1(label, tier or 25)
        j['saga_fit'] = {'p1': p1, 'tier': tier or 25, 'why': f'默认对位（{label or "类型待定"} · {tier or 25}% 档）：{why}', 'basis': '默认 · 官网快照后按业务线校正'}
        changed.append('saga_fit')
    mr = j.setdefault('mail_review', {})
    sn = mr.get('saga_now') or {}
    if not sn.get('p1'):
        mr['saga_now'] = {'p1': j['saga_fit']['p1'], 'why': j['saga_fit']['why']}
        changed.append('mail_review.saga_now')
    facts = mr.setdefault('facts', [])
    if rg and not any('登记' in str(f.get('who', '')) or '登记' in str(f.get('kind', '')) for f in facts):
        facts.append({'date': rg.get('fetched') or DATE, 'dir': '查', 'who': 'Agent 登记底数（registry）', 'quote': (rg.get('source') or rg.get('name') or '')[:300],
                      'why': '闸 2 坐实来源（URL 见 company_facts.url）', 'url': rg.get('url') or ''})
        changed.append('mail_review.facts')
    j['deep'] = {'done_at': DATE, 'level': '桌面加厚 v1（LT-T01：登记底数 + 三闸 + 复核整合，未新增网查；官网快照待 Actions 补抓）', 'batch': BATCH}
    j['notes'] = (f'LT-T01 桌面加厚（{DATE}）：填 {"/".join(changed) or "无新增字段"}；来源 = registry / sieve / lt_review / 表内。' + ('\n' + j['notes'] if j.get('notes') else ''))
    return changed


def main():
    sieve = load(os.path.join(DATA, 'sieve.json'))
    reg = registry()
    ents = {e['code']: e for e in load(os.path.join(DATA, 'entities.json'))}
    import csv
    rows = list(csv.DictReader(open(os.path.join(DATA, '客户主表.csv'), encoding='utf-8-sig')))
    n = {'skeleton': 0, 'mail_only': 0, 'skip': 0}
    for r in rows:
        if r['评级'] not in ('A', 'B'):
            continue
        code = r['档案编号']
        p = os.path.join(R, f'{code}.json')
        j = load(p)
        d = j.get('deep')
        if d:
            if isinstance(d, dict) and d.get('batch') == BATCH:
                n['skip'] += 1
            continue
        if j.get('type') and j.get('summary') and j.get('evidence'):
            j['deep'] = {'done_at': DATE, 'level': '邮件证据 v1（S/A 箱往来整理；官网快照待 Actions 补抓）', 'batch': BATCH}
            n['mail_only'] += 1
        else:
            thicken(code, j, sieve.get(code) or {}, reg, ents.get(code) or {})
            n['skeleton'] += 1
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(BATCH, n)


if __name__ == '__main__':
    main()
