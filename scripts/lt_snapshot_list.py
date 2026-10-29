#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群 · 补快照清单生成（External + Planet 仓 A/B；Saga 由 site_snapshot.py 原生按 entities A/B 处理）· T29-U131 2026-10-29。
输出 data/长期客户群_补快照清单_<日期>.json = [{code, name, grade, country, domains[]}]，watch.py 的 snapshot_missing() 取最新一份喂给
site_snapshot.py（EXTRA_SITES）。已有 ok 快照的编号不再列；域名用记录里修正后的 domain / 网站主机名。幂等（同日覆盖）。
用法：python3 scripts/lt_snapshot_list.py
"""
import csv
import importlib.util
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XD = os.path.join(ROOT, 'data', 'external_clients')
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
SNAP = os.path.join(ROOT, 'data', 'saga_clients', 'site_snapshots')


def main():
    spec = importlib.util.spec_from_file_location('lt_gap_audit', os.path.join(ROOT, 'scripts', 'lt_gap_audit.py'))
    ga = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ga)
    date = subprocess.check_output(['date', '-u', '+%Y-%m-%d']).decode().strip()
    out = []

    def has_ok(code):
        return ga.snap_file_status(code) == 'ok'

    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in json.load(open(os.path.join(XD, repo + '.json'), encoding='utf-8'))['records']:
            recs[r['code']] = r
    ov = json.load(open(os.path.join(XD, 'overrides.json'), encoding='utf-8'))
    for c, o in ov.items():
        if o.get('grade') == 'C' or not (o.get('grade') == 'B' or (o.get('review') or {}).get('status') == '留B'):
            continue
        r = recs.get(c)
        if not r or has_ok(c):
            continue
        h = ga.host_of(r.get('domain') or r.get('website') or '')
        if h and '.' in h:
            out.append({'code': c, 'name': (r.get('name') or '')[:80], 'grade': o.get('grade') or 'B', 'country': r.get('country_zh') or '', 'domains': [h]})
    for r in csv.DictReader(open(PCSV, encoding='utf-8-sig')):
        g = r['人工定级'] or r['评级']
        if g not in ('A', 'B') or has_ok(r['档案编号']):
            continue
        h = ga.host_of(r['网站'] or '')
        if h and '.' in h:
            out.append({'code': r['档案编号'], 'name': r['公司名'][:80], 'grade': g, 'country': r['国家'], 'domains': [h]})
    p = os.path.join(ROOT, 'data', f'长期客户群_补快照清单_{date}.json')
    json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('snapshot list', len(out), '→', p, {k: sum(1 for x in out if x['code'].startswith(k)) for k in ('X', 'P')})


if __name__ == '__main__':
    main()
