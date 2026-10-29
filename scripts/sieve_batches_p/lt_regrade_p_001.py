#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Planet 仓 · 长期客户群 批 LT-01（T29-U128，2026-10-29）：三库同一把尺子（Q-76；Simon U128 ③）。

尺子：A = 核心（真人往来 / 成单）；B = 普通跟（对位 + 活着 + 有路径）；C = 储备。
Planet 仓 129 户全是 PLANET 渠道名录挖出的分销 / 集成商：触达记录全是「S 邮箱 去 N · 0 回复」→ 无真人往来 → 没有 A。
规则：随主档（sieve_planet rule DUP-AB / dup_of）→ 主档等级；pass_final / keep_C → C；pool / pool_watch / keep → 有邮箱 B（待过：pool 优先级 1，keep 优先级 3），无邮箱 → C 储备·无路径。
落点：data/客户名单_Planet渠道_2026-10.csv 列「人工定级」+ 新列「长期群复核」；data/长期客户群_LT-01_变更_Planet_2026-10-29.csv。
之后：cd scripts && python3 render.py（129）。幂等。
"""
import csv
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
BATCH = 'LT-01'
DATE = '2026-10-29'
TAG = f'Q-76 {BATCH} {DATE}'


def main():
    now = subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()
    rows = list(csv.DictReader(open(CSV, encoding='utf-8-sig')))
    fields = list(rows[0].keys())
    if '长期群复核' not in fields:
        fields.append('长期群复核')
    sp = json.load(open(os.path.join(ROOT, 'data', 'sieve_planet.json'), encoding='utf-8'))
    saga = {e['code']: e['grade'] for e in json.load(open(os.path.join(ROOT, 'data', 'saga_clients', 'entities.json'), encoding='utf-8'))}
    xov = json.load(open(os.path.join(ROOT, 'data', 'external_clients', 'overrides.json'), encoding='utf-8'))
    out, cnt = [], {}

    def tick(k):
        cnt[k] = cnt.get(k, 0) + 1

    for r in rows:
        code = r['档案编号']
        v = sp.get(code) or {}
        cur = (r.get('人工定级') or r['评级']).strip()[:1]
        has_mail = '@' in (r.get('入口/联系方式') or '')
        verdict, dup = v.get('verdict'), v.get('dup_of')
        new, why, review = None, '', ''
        if dup and (dup in saga or dup in xov):
            new = saga.get(dup) or xov[dup]['grade']
            why = f'随主档 {dup}（{new}）'
        elif verdict == 'pass_final':
            new, why = 'C', '永久 pass（三闸）'
        elif verdict == 'keep_C':
            new, why = 'C', 'C 储备（三闸留 C）'
        elif not has_mail:
            new, why = 'C', 'C 储备·无路径（无邮箱，群发触达不到）'
        else:
            new = 'B'
            why = ('三闸捞出 → B（Simon U128「直接定为 B」）' if verdict in ('pool', 'pool_watch') else
                   ('B 留（对位 + 活着 + 有路径）' if cur == 'B' else 'A → B 普通跟（仅 S 邮箱群发 0 回复，无真人往来）'))
            review = f'待过·优先级 {1 if verdict in ("pool", "pool_watch") else 3}（{DATE}）'
        if r['状态'].startswith('并入'):
            tick('并入 skip')
            continue
        r['人工定级'] = new
        r['长期群复核'] = (f'{TAG}：{why}' + (f'；{review}' if review else ''))
        tick(f'{cur}->{new}')
        out.append([code, r['公司名'], r['国家'], cur, new, why, review])
    with open(CSV, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(ROOT, 'data', '长期客户群_LT-01_变更_Planet_2026-10-29.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '公司', '国家', '原等级', '新等级', '理由', '复核'])
        w.writerows(out)
    print(BATCH, now, cnt, 'rows', len(out))


if __name__ == '__main__':
    main()
