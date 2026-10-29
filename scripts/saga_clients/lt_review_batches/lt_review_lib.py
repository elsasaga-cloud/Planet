#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群 · 复核批共用件（T29-U128 起）。批文件 lt_r_0NN.py 只写 V = {code: (verdict, reason, [(quote, url), ...])}，然后 run(BATCH, V)。

verdict ∈ {'留B', '打回C', '升A'}
落点（Saga 库）：
  research/<code>.json  lt_review{status, batch, verdict_date, note}；mail_review.facts 追加 dir=查 的证据（去重）；
                        打回C → grade_override=C + override_reason（含 c_sub=储备·复核打回）+ override_history；升A → grade_override=A
  sieve.json            打回C → verdict keep_C（batch=本批，lt_prev_verdict 留痕；原 reason 前缀「复核打回」）
  P池_巡检表_2026-10-29.csv  打回C 的行移除（12-28 巡检输入保持干净）
  data/长期客户群_复核记录.csv  追加（编号守卫：同编号同批不重复）
之后：build.py → render → audits → scripts/lt_roster.py。幂等。
"""
import csv
import importlib.util
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SAGA = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SAGA))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
RESEARCH = os.path.join(DATA, 'research')
WATCH = os.path.join(DATA, 'P池_巡检表_2026-10-29.csv')
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')
DATE = '2026-10-29'


def _mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def run(batch, V, date=DATE):
    now = subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()
    sieve_mod = _mod('saga_sieve', os.path.join(SAGA, 'sieve.py'))
    s = sieve_mod.load_sieve()
    ents = {e['code']: e for e in json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))}
    cnt, log_rows, drop = {}, [], set()
    for code, (verdict, reason, facts) in V.items():
        assert verdict in ('留B', '打回C', '升A'), (code, verdict)
        e = ents[code]
        p = os.path.join(RESEARCH, code + '.json')
        rs = json.load(open(p, encoding='utf-8'))
        rv = rs.get('lt_review') or {}
        rs['lt_review'] = {'status': {'留B': '留 B', '打回C': '打回 C', '升A': '升 A'}[verdict], 'batch': batch, 'prio': rv.get('prio'),
                           'queued': rv.get('batch'), 'verdict_date': date, 'note': reason, 'why': rv.get('why', '')}
        mr = rs.setdefault('mail_review', {})
        fl = mr.setdefault('facts', [])
        for quote, url in facts or []:
            if not any(f.get('quote') == quote for f in fl):
                fl.append({'date': date, 'dir': '查', 'who': f'Agent 复核 {batch}', 'quote': quote, 'why': '长期客户群复核证据（非邮件事实，不计真回）', 'url': url})
        hist = rs.setdefault('override_history', [])
        if verdict == '打回C':
            if not any(h.get('batch') == batch for h in hist):
                hist.append({'batch': batch, 'date': date, 'from_override': rs.get('grade_override'), 'to': 'C', 'prev_reason': rs.get('override_reason') or '', 'reason': reason})
            rs['grade_override'] = 'C'
            rs['override_reason'] = f'Q-76 {batch} {date} 复核打回 C 储备：{reason}；c_sub=储备·复核打回 ；回信 / 询价即回 B'
            row = s.get(code)
            if row and row.get('verdict') != 'keep_C':
                row['lt_prev_verdict'] = row.get('verdict')
                row['lt_prev_batch'] = row.get('batch')
                row['verdict'] = 'keep_C'
                row['batch'] = batch
                row['reason'] = f'复核打回（{batch}）：{reason}｜原：' + (row.get('reason') or '')
                row['date'] = date
            drop.add(code)
        elif verdict == '升A':
            if not any(h.get('batch') == batch for h in hist):
                hist.append({'batch': batch, 'date': date, 'from_override': rs.get('grade_override'), 'to': 'A', 'prev_reason': rs.get('override_reason') or '', 'reason': reason})
            rs['grade_override'] = 'A'
            rs['override_reason'] = f'Q-76 {batch} {date} 复核升 A 核心：{reason}'
        json.dump(rs, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        cnt[verdict] = cnt.get(verdict, 0) + 1
        log_rows.append([code, e.get('name'), e.get('country'), e['grade'], {'留B': 'B', '打回C': 'C', '升A': 'A'}[verdict], batch, date, reason])
    sieve_mod.save_sieve(s)
    if drop and os.path.exists(WATCH):
        wrows = list(csv.DictReader(open(WATCH, encoding='utf-8-sig')))
        fields = list(wrows[0].keys())
        keep = [r for r in wrows if r['编号'] not in drop]
        if len(keep) != len(wrows):
            with open(WATCH, 'w', encoding='utf-8-sig', newline='') as f:
                w = csv.DictWriter(f, fieldnames=fields)
                w.writeheader()
                w.writerows(keep)
    have = set()
    if os.path.exists(LOG):
        have = {(r['编号'], r['批次']) for r in csv.DictReader(open(LOG, encoding='utf-8-sig'))}
    new = [r for r in log_rows if (r[0], r[5]) not in have]
    with open(LOG, 'a', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        if not have and f.tell() == 0:
            w.writerow(['编号', '公司', '国家', '复核前等级', '复核后等级', '批次', '日期', '结论与理由'])
        w.writerows(new)
    print(batch, now, cnt, 'log +', len(new), 'sieve 打回', len(drop))
    return cnt
