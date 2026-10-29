#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P 池修正 002（T29-U124 全量核验，2026-10-29）：SC-2730 RVi Group 档位符号统一。

发现：P-01 冻结时 RVi 判 `pool_watch`（制裁名单待核、只巡检不发），但 `grade` 仍写 ★，巡检表 / 总名册随之把它算进 ★ 正式档位，
成了全池唯一「观察 + ★」的孤例（观察 59 = ☆ 20 + △ 38 + ★ 1）。Saga 观察档口径 = △（疑点待清）。
修正：sieve.json 与巡检表 CSV 的档位 ★ → △，reason 前缀 ☆ → △ 并加注；制裁核清后再恢复 ★ 转正。幂等。
之后重跑：p_roster.py / web_watch/checklist.py / web_watch/discover.py（targets_auto 的 pool.档位）。
"""
import csv
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SIEVE = os.path.join(ROOT, 'data', 'saga_clients', 'sieve.json')
CSV = os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_2026-10-29.csv')
CODE = 'SC-2730'
NOTE = '（U124 核验：观察档符号 ★→△ 统一口径，制裁核清后恢复 ★ 转正）'


def main():
    now = subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()
    s = json.load(open(SIEVE, encoding='utf-8'))
    row = s[CODE]
    assert row['verdict'] == 'pool_watch', row['verdict']
    changed = 0
    if row.get('grade') != '△':
        row['grade'] = '△'
        changed += 1
    if NOTE not in row['reason']:
        r = row['reason']
        if r.startswith('☆ P 池观察档'):
            r = '△' + r[1:]
        row['reason'] = r + NOTE
        changed += 1
    if changed:
        row['fix_batch'] = f'P-FIX-02 {now}'
        s['_meta']['time'] = now
        json.dump(s, open(SIEVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # 巡检表
    rows = list(csv.DictReader(open(CSV, encoding='utf-8-sig')))
    fields = list(rows[0].keys())
    cchanged = 0
    for r in rows:
        if r['编号'] == CODE and r['档位'] != '△':
            r['档位'] = '△'
            if NOTE not in r['备注']:
                r['备注'] = r['备注'] + NOTE
            cchanged += 1
    if cchanged:
        with open(CSV, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
    print('sieve changed', changed, 'csv changed', cchanged, 'grade now', s[CODE]['grade'])


if __name__ == '__main__':
    main()
