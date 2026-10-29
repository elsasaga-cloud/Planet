#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-R09（Planet 侧）· 邮箱域体检异常：PB-029 Microsam（加拿大）· T29-U131 2026-10-29。

DNS 2026-10-29：microsam.ca MX/A/NS = NXDOMAIN（域名已失效）；planet-ca.com 分销商名录仍列 info@microsam.ca + 电话；Facebook 页在；
ZoomInfo 仍写 www.microsam.ca。邮箱路径断、只剩电话 / Facebook（Saga 不打电话、社媒只 James）→ 无路径 → C 储备（可逆：补到邮箱即回 B）。
另：SB-944 Fybera country_fix → 保加利亚（官网电话 +359 2 4214270）。幂等。
"""
import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')
DATE = '2026-10-29'
BATCH = 'LT-R09'
REASON = ('域名 microsam.ca 已失效（DNS 2026-10-29 MX/A/NS NXDOMAIN）；planet-ca.com 分销商名录仍列 info@microsam.ca / +1 (514) 999-9648，'
          'Facebook 页在、ZoomInfo <25 人 <$5M；邮箱路径断、只剩电话 / 社媒 → 无路径 → C 储备（补到邮箱即回 B）')
URLS = 'https://planet-ca.com/distributors/ ; https://www.facebook.com/microsam.ca/ ; https://www.zoominfo.com/c/microsam-inc/459190017'


def main():
    rows = list(csv.DictReader(open(PCSV, encoding='utf-8-sig')))
    fields = list(rows[0].keys())
    n = 0
    for r in rows:
        if r['档案编号'] != 'PB-029' or f'打回C·{BATCH}' in (r['长期群复核'] or ''):
            continue
        r['人工定级'] = 'C'
        r['C级细分'] = '储备·复核打回'
        r['长期群复核'] = (r['长期群复核'] or '') + f'｜打回C·{BATCH} {DATE}（{REASON}；证据 {URLS}）'
        n += 1
    with open(PCSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    log = list(csv.DictReader(open(LOG, encoding='utf-8-sig')))
    if not any(r['编号'] == 'PB-029' and r['批次'] == BATCH for r in log):
        log.append({'编号': 'PB-029', '公司': 'Microsam', '国家': '加拿大', '复核前等级': 'B', '复核后等级': 'C', '批次': BATCH, '日期': DATE, '结论与理由': REASON})
        with open(LOG, 'w', encoding='utf-8-sig', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=['编号', '公司', '国家', '复核前等级', '复核后等级', '批次', '日期', '结论与理由'])
            w.writeheader()
            w.writerows(log)
    # SB-944 country_fix
    p = os.path.join(ROOT, 'data', 'saga_clients', 'research', 'SB-944.json')
    j = json.load(open(p, encoding='utf-8'))
    m = 0
    if j.get('country_fix') != '保加利亚':
        j['country_fix'] = '保加利亚'
        j['notes'] = f'{BATCH} {DATE} country_fix：表内「比利时」有误，官网 fybera.com 联系电话 +359 2 4214270（索非亚）→ 保加利亚。\n' + (j.get('notes') or '')
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        m = 1
    print(BATCH, 'planet', n, 'country_fix', m, 'log', len(log))


if __name__ == '__main__':
    main()
