#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-X01 · 交叉检查：External 副档（saga_dup = 与 Saga 同一公司）的等级跟主档走 · T29-U131 2026-10-29。

LT-01 时副档「随主档等级 B」，之后主档在 LT-R01…R05S 被打回 C（如 SC-2728 Blue Helix：Companies House Dormant），副档没跟着动。
规则：主档 C → 副档 C（理由抄主档复核结论）；主档 A/B → 副档保持 B（副档不计数，升降跟主档）。写 overrides.json + 研究卡 grade_final + 复核记录日志。幂等。
"""
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SD = os.path.join(ROOT, 'data', 'saga_clients')
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')
DATE = '2026-10-29'
BATCH = 'LT-X01'


def main():
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in json.load(open(os.path.join(DATA, f'{repo}.json'), encoding='utf-8'))['records']:
            recs[r['code']] = r
    p = os.path.join(DATA, 'overrides.json')
    ov = json.load(open(p, encoding='utf-8'))
    log = list(csv.DictReader(open(LOG, encoding='utf-8-sig')))
    seen = {(r['编号'], r['批次']) for r in log}
    master_reason = {r['编号']: r['结论与理由'] for r in log if r['复核后等级'] == 'C'}
    n = 0
    for code, o in ov.items():
        sd = recs.get(code, {}).get('saga_dup')
        if not isinstance(sd, dict) or o.get('grade') != 'B':
            continue
        m = ents.get(sd.get('code'))
        if not m or m['grade'] != 'C':
            continue
        why = master_reason.get(m['code'], '主档复核打回 C 储备')
        reason = f"{BATCH} {DATE}：副档随主档 —— 主档 Saga {m['code']} 已复核打回 C 储备（{why[:160]}）→ 本档同步 C；主档回 B 本档跟着回"
        o.update({'prev_reason': o.get('reason', ''), 'grade': 'C', 'reason': reason, 'date': DATE, 'batch': BATCH, 'from': 'B',
                  'review': {'status': '打回C', 'prio': 3, 'date': DATE, 'batch': BATCH, 'note': reason, 'cat': 'FOLLOW'}})
        cp = os.path.join(DATA, 'research', f'{code}.json')
        if os.path.exists(cp):
            c = json.load(open(cp, encoding='utf-8'))
            c['grade_final'] = 'C'
            c['grade_reason_final'] = reason[:300]
            json.dump(c, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        if (code, BATCH) not in seen:
            log.append({'编号': code, '公司': recs[code].get('name', ''), '国家': recs[code].get('country_zh', ''), '复核前等级': 'B', '复核后等级': 'C',
                        '批次': BATCH, '日期': DATE, '结论与理由': reason})
            seen.add((code, BATCH))
        n += 1
    json.dump(ov, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(LOG, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['编号', '公司', '国家', '复核前等级', '复核后等级', '批次', '日期', '结论与理由'])
        w.writeheader()
        w.writerows(log)
    print(BATCH, 'followed', n, 'log', len(log))


if __name__ == '__main__':
    main()
