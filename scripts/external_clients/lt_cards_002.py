#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-T01 · External 长期客户群「无研究卡」B 户建桌面卡（203 户）· T29-U131 2026-10-29。

Simon U131：「A / B 都深挖过了吗？…把没有的都再搞一下」。External 648 户 B 里 203 户没有第 2 步研究卡（XB-E 82 Edgecore 名录 /
XB-C 64 CCTV / XC 52 捞出户 / XB-M 5）。本批**不新增网查**：把来源库 9 月官网 / 名录核对字段（type / kv / facts / kp /
signals / notes / 邮箱）+ 长期群复核结论（overrides.review）+ 本日 DNS 体检（mx_check）整合成标准研究卡，deep=False，
round='LT-T01'，等官网快照（每日 Actions 补抓）后再加厚。幂等：已有卡跳过。不改等级。
"""
import ast
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA  # noqa: E402
import research_store  # noqa: E402

DATE = '2026-10-29'
BATCH = 'LT-T01'
BRANDS = ['Utepo', 'Hikvision', 'Dahua', 'TP-Link', 'Ubiquiti', 'MikroTik', 'PLANET', 'Cisco', 'Netgear', 'D-Link', 'Zyxel', 'Moxa', 'Hirschmann',
          'Phoenix Contact', 'Westermo', 'Teltonika', 'Aruba', 'Huawei', 'ONV', 'ORing', 'Korenix', 'EtherWAN', 'Antaira', 'Allied Telesis',
          'Edgecore', 'Edge-core', 'Ruijie', 'Reyee', 'Grandstream', 'Uniview', 'Axis', 'Hanwha', 'Bosch', 'H3C', 'Juniper', 'Extreme', 'Fortinet',
          'Tenda', 'Cudy', 'Ruckus', 'Cambium', 'LigoWave', 'Mimosa', 'Perle', 'ComNet', 'Lantech', 'Advantech', 'Red Lion', 'Siemens', 'Belden',
          'Panduit', 'CommScope', 'Legrand', 'Digitus', 'Intellinet', 'TRENDnet', 'LevelOne', 'Netonix', 'Wi-Tek', 'Totolink', 'IP-COM', 'Vivotek',
          'Provision-ISR', 'Milesight', 'Reolink', 'Tiandy', 'HRUI', 'Nettek', 'ZINCOM', 'Avigilon', 'Pelco', 'Honeywell', 'Ubiquiti', 'Mikrotik']


def lit(x):
    if isinstance(x, str) and x[:1] in '[{(':
        try:
            return ast.literal_eval(x)
        except Exception:
            return x
    return x


def brands_in(*texts):
    low = ' '.join(str(t) for t in texts if t).lower()
    out = []
    for b in BRANDS:
        if b.lower() in low and b not in out:
            out.append(b)
    if 'Mikrotik' in out and 'MikroTik' in out:
        out.remove('Mikrotik')
    if 'Edge-core' in out and 'Edgecore' in out:
        out.remove('Edge-core')
    return out[:8]


def saga_line(t):
    t = t or ''
    if re.search(r'OEM|品牌|own', t, re.I):
        return 'STC 贴牌 / 自有品牌线（30% 档）'
    if re.search(r'分销|批发|进口|经销|Distribut|Reseller|授权', t, re.I):
        return 'STC 企业 PoE 走量款（20% 档：STC-228GP / STC-2224GP）'
    if re.search(r'ISP|WISP|运营|电信', t, re.I):
        return 'STC 汇聚 + STI 工业（25% 档）'
    if re.search(r'工业|自动化|Industrial', t, re.I):
        return 'STI 工业 PoE（25% 档：STI-288GPM）'
    return 'STC 项目集成款（25% 档：STC-2216GP / STC-228GP）'


def build(code, r, ov, mx):
    kv = lit(r.get('kv')) if r.get('kv') else {}
    kv = kv if isinstance(kv, dict) else {}
    rv = ov.get('review') or {}
    d = r.get('domain') or ''
    st = (mx.get(d) or {}).get('status') if d else None
    alive = {'ok': f'域名 {d} MX 正常（DNS 体检 {DATE}）；官网快照待 Actions 补抓',
             'no_mx': f'域名 {d} 有 A 记录、无 MX（邮箱可能托管在别的域；DNS {DATE}）',
             'null_mx': f'域名 {d} 声明不收邮件（Null MX；DNS {DATE}）→ 邮箱路径待核',
             'nxdomain': f'域名 {d} 不存在（NXDOMAIN；DNS {DATE}）→ 路径待核 / 可能换域',
             'dead': f'域名 {d} 无解析（DNS {DATE}）→ 路径待核'}.get(st or '', (f'域名 {d}（DNS 查询出错，待重查）' if d else '无域名（仅来源库信息）'))
    typ = (r.get('type') or r.get('their_class') or kv.get('类型') or '').strip() or '类型待定（来源库未分型）'
    typ = re.sub(r'^[ABC]类\s*[—-]+\s*', '', typ)
    kvs = '；'.join(f'{k}={str(v)[:60]}' for k, v in kv.items() if k in ('公司全称', '业务', '公司类型', '总部', '地址', '开发策略', '客户优先级', '置信度') and v)[:400]
    sig = r.get('signals') or r.get('src_note') or ''
    summary = f"{r.get('name', '')}（{r.get('country_zh', '')}{(' · ' + r['city']) if r.get('city') else ''}）：{typ}" + (f'；{sig[:160]}' if sig else '') + (f'；{kvs}' if kvs else '')
    ev = [{'kind': '来源库官网/名录核对', 'claim': (typ + ('；' + kvs if kvs else ''))[:300], 'quote': (r.get('notes') or '')[:300],
           'url': ('https://' + d) if d else (r.get('src_repo_ref') or ''), 'date': r.get('src_updated') or '2026-09'}]
    for u in (lit(r.get('evidence_urls')) or [])[:3]:
        if isinstance(u, str) and u.startswith('http'):
            ev.append({'kind': '来源库证据链接', 'claim': '来源库调研时引用', 'quote': '', 'url': u.split('（')[0], 'date': r.get('src_updated') or '2026-09'})
    if rv.get('note'):
        ev.append({'kind': f"长期群复核 {rv.get('batch', '')}", 'claim': rv['note'][:300], 'quote': '', 'url': '', 'date': rv.get('date') or DATE})
    emails = lit(r.get('emails_live')) or []
    kp = []
    for k in (lit(r.get('kp')) or []):
        if isinstance(k, dict) and k.get('name'):
            kp.append({'name': k['name'], 'role': (k.get('role') or '')[:80], 'source': (k.get('status') or '来源库')[:80]})
    kpt = r.get('kp_text') or ''
    if not kp and kpt:
        m = re.search(r'\*\*([^*—\-]{2,40})\s*[—-]+\s*([^*]{2,60})\*\*', kpt)
        if m:
            kp.append({'name': m.group(1).strip(), 'role': m.group(2).strip()[:80], 'source': '来源库 KP 段'})
    contacts = {'email': emails[0] if emails else '', 'email_status': '活（来源库 9 月核对）' if emails else '缺', 'kp': kp}
    t = lit(r.get('touch')) if r.get('touch') else None
    touch = (f"S 箱 {t.get('首次', '')} 去信 {t.get('去信', '')} / 来信 {t.get('来信', '')}（{t.get('主题', '')}）" if isinstance(t, dict) else
             ('S 箱 9–10 月群发名单未见本域 → 未触达' if 'S箱已群发' not in str(r.get('flags')) else 'S 箱已群发 0 回'))
    sd = lit(r.get('saga_dup')) if r.get('saga_dup') not in (None, 'None', '') else None
    overlap = f"Saga {sd['code']}（{sd.get('via', '')}）随主档" if isinstance(sd, dict) else '无'
    card = {'code': code, 'name': r.get('name', ''), 'round': BATCH, 'researched_at': DATE, 'alive': alive, 'summary': summary[:600],
            'type_final': typ[:160], 'size': '', 'brands_seen': brands_in(typ, sig, kvs, r.get('notes'), r.get('heading_path')),
            'saga_line': saga_line(typ + ' ' + sig), 'fit': '', 'evidence': ev, 'contacts': contacts, 'touch_status': touch,
            'saga_overlap': overlap, 'grade_final': 'B', 'grade_reason_final': (rv.get('note') or ov.get('reason') or '留 B')[:300],
            'next_move': {'action': '不动', 'angle': '', 'model': '', 'price': '', 'window': '', 'when': '官网快照 + 加厚后进群发分组（Q-77）'},
            'draft_en': None, 'deep': False,
            'notes': f'{BATCH} 桌面卡（{DATE}）：来源库字段 + 长期群复核 + DNS 体检整合，未新增网查；官网快照到后加厚。'}
    return card


def main():
    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in json.load(open(os.path.join(DATA, f'{repo}.json'), encoding='utf-8'))['records']:
            recs[r['code']] = r
    ov = json.load(open(os.path.join(DATA, 'overrides.json'), encoding='utf-8'))
    mxp = os.path.join(DATA, f'mx_check_{DATE}.json')
    mx = json.load(open(mxp, encoding='utf-8'))['domains'] if os.path.exists(mxp) else {}
    n = {'new': 0, 'skip': 0}
    for code, o in ov.items():
        if o.get('grade') == 'C' or not (o.get('grade') == 'B' or (o.get('review') or {}).get('status') == '留B'):
            continue
        if research_store.get(code):
            n['skip'] += 1
            continue
        research_store.put(build(code, recs[code], o, mx))
        n['new'] += 1
    print(BATCH, n)


if __name__ == '__main__':
    main()
