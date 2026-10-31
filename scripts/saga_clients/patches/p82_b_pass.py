#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p82 · B-PASS-01 应用（T29-U146 2026-10-31）：b_select 结果 → 研究档 b_tier（B1/B2/C + 原因）；C → grade_override='C' + override_history + 复核记录。人工定级不动。幂等。"""
import csv
import json
import os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-31'
BATCH = 'B-PASS-01'
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')


def main():
    sel = json.load(open(os.path.join(SD, f'B类分层_{DATE}.json'), encoding='utf-8'))
    manual = set()
    pm = os.path.join(SD, '人工定级.csv')
    if os.path.exists(pm):
        for r in csv.DictReader(open(pm, encoding='utf-8-sig')):
            manual.add((r.get('键或编号') or '').strip())
    cnt = Counter()
    rows = []
    for c, o in sel.items():
        p = os.path.join(SD, 'research', c + '.json')
        if not os.path.exists(p):
            cnt['no_research'] += 1
            continue
        rs = json.load(open(p, encoding='utf-8'))
        rs['b_tier'] = {'tier': o['tier'], 'why': o['why'], 'batch': BATCH, 'date': DATE, 'ident': o['ident'], 'path': o['path'], 'reply': o['rc'], 'focus': o['focus']}
        if o['tier'] == 'C' and c not in manual:
            reason = f"{BATCH} {DATE} B 池分层「不 OK 的下放 C 储备」：{o['why']}"
            hist = rs.setdefault('override_history', [])
            if not any(h.get('batch') == BATCH for h in hist):
                hist.append({'batch': BATCH, 'date': DATE, 'from_override': rs.get('grade_override'), 'to': 'C', 'prev_reason': rs.get('override_reason') or '', 'reason': reason})
                rows.append([c, o['name'], o['country'], 'B', 'C', BATCH, DATE, reason[:200]])
            rs['grade_override'] = 'C'
            rs['override_reason'] = reason[:600]
            cnt['→C'] += 1
        else:
            cnt[o['tier']] += 1
        json.dump(rs, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    have = set()
    if os.path.exists(LOG):
        have = {(x['编号'], x['批次']) for x in csv.DictReader(open(LOG, encoding='utf-8-sig'))}
    new = [x for x in rows if (x[0], x[5]) not in have]
    with open(LOG, 'a', encoding='utf-8-sig', newline='') as f:
        csv.writer(f).writerows(new)
    print(BATCH, dict(cnt), 'log +', len(new))


if __name__ == '__main__':
    main()
