#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p79 · A-DEEP-01 应用（T29-U137 2026-10-30）：把 ab_final/a_deep.py 的核验卡写进研究档，并执行「下放 B」。
  · 每个 A 候选 research['a_deep'] = {batch, date, verdict, ident, role, fit, need, path, size, veto, gaps, story, timeline(末 12 条), web_facts}
  · 网查事实 → mail_review.facts（dir=查，who=Agent 网查 A-DEEP-01，含 URL），以 URL 去重
  · verdict 下放B → grade_override='B' + override_reason + override_history（batch A-DEEP-01）；留A 不改 override（p78 已置 A）
  · extra.country_fix → research['country_fix']
幂等；之后 build.py → render.py。日志追加 data/长期客户群_复核记录.csv。
"""
import csv
import json
import os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
RESEARCH = os.path.join(SD, 'research')
DATE = '2026-10-30'
BATCH = 'A-DEEP-01'
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')


def main():
    deep = json.load(open(os.path.join(SD, f'A深挖_核验_{DATE}.json'), encoding='utf-8'))
    manual = set()
    if os.path.exists(os.path.join(SD, '人工定级.csv')):
        for r in csv.DictReader(open(os.path.join(SD, '人工定级.csv'), encoding='utf-8-sig')):
            manual.add((r.get('键或编号') or r.get('档案编号') or list(r.values())[0] or '').strip())
    cnt = Counter()
    log_rows = []
    for c, o in deep.items():
        p = os.path.join(RESEARCH, c + '.json')
        if not os.path.exists(p):
            cnt['no_research'] += 1
            continue
        rs = json.load(open(p, encoding='utf-8'))
        rs['a_deep'] = {'batch': BATCH, 'date': DATE, 'verdict': o['verdict'], 'tier': o['tier'], 'ident': o['ident'], 'role': o['role'], 'fit_words': o['fit_words'], 'p1': o['p1'], 'need': o['need'], 'asks': o['asks'],
                        'path': o['path'], 'size': o['size'], 'size_lv': o['size_lv'], 'veto': o['veto'], 'gaps': o['gaps'], 'story': o['story'], 'n_out': o['n_out'], 'n_in': o['n_in'], 'last_in': o['last_in'], 'last_out': o['last_out'],
                        'prices_out': o['prices_out'], 'timeline': o['timeline'][-12:], 'web_facts': o['web_facts'], 'manual': o['manual']}
        mr = rs.setdefault('mail_review', {})
        fl = mr.setdefault('facts', [])
        for wf in o['web_facts']:
            if not any(f.get('url') == wf['url'] for f in fl):
                fl.append({'date': DATE, 'dir': '查', 'who': f'Agent 网查 {BATCH}', 'quote': wf['quote'][:300], 'why': 'A 落池核验：身份/角色/规模（网页公开信息）', 'url': wf['url']})
        if (o.get('extra') or {}).get('country_fix') and not rs.get('country_fix'):
            rs['country_fix'] = o['extra']['country_fix']
        if c in manual:
            cnt['manual_skip'] += 1
            json.dump(rs, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            continue
        if o['verdict'] == '下放B':
            reason = f"{BATCH} {DATE} A 落池核验未过 → 下放 B：" + '；'.join(o['gaps'][-1:] or o['veto'] or o['gaps'])
            hist = rs.setdefault('override_history', [])
            if not any(h.get('batch') == BATCH for h in hist):
                hist.append({'batch': BATCH, 'date': DATE, 'from_override': rs.get('grade_override'), 'to': 'B', 'prev_reason': rs.get('override_reason') or '', 'reason': reason})
            rs['grade_override'] = 'B'
            rs['override_reason'] = reason[:600]
            cnt['下放B'] += 1
            log_rows.append([c, o['name'], o['country'], o['grade_now'], 'B', BATCH, DATE, reason[:200]])
        else:
            cnt['留A'] += 1
        json.dump(rs, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    have = set()
    if os.path.exists(LOG):
        have = {(x['编号'], x['批次']) for x in csv.DictReader(open(LOG, encoding='utf-8-sig'))}
    new = [x for x in log_rows if (x[0], x[5]) not in have]
    with open(LOG, 'a', encoding='utf-8-sig', newline='') as f:
        csv.writer(f).writerows(new)
    print(BATCH, dict(cnt), 'log +', len(new))


if __name__ == '__main__':
    main()
