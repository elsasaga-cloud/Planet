#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A / B 档并入 P 池 · 批 AB-01（T29-U125，2026-10-29；Q-71 默认方案，`docs/AB并池方案_草案_2026-10-29.md` §5 / §7）。

只加「池位」，不改等级：A 还是 A、B 还是 B。
输入：data/saga_clients/AB并池_预演_2026-10-29.csv（`ab_pool_dryrun.py` 的只读预演，1,229 行）
  P 核心（A 90）        → pool      ★  tags + core（A 复核 19 另加 a_review）
  P 核心候选（B 64）    → pool      ★  tags + core（gg 8 户加 gg：首触只问候 + 新品，不推单）
  P 正式候选（B 38）    → pool      ○
  P 观察候选（B 181）   → pool_watch ☆（真回弱 / 四主区冷户：试单 / 回信即转正，两轮无动静退回原档）
  留 B / 留 B·复核 / 留 B·守界 → 不动
落点：
  data/saga_clients/sieve.json      新增 SA-/SB- 行（rule AB1、batch AB-01、origin Saga-A / Saga-B、gate 3）
  data/saga_clients/P池_巡检表_2026-10-29.csv  追加（编号守卫，幂等）
  docs/P池_资产池名册_2026-10-29.md   追加「## Saga A/B 并池 · 批 AB-01」小节（标记守卫）
之后重跑：p_roster.py / web_watch/checklist.py / web_watch/discover.py / Saga render。
撤销：python3 ab_pool_001.py --undo（删 batch AB-01 的 sieve 行 + 巡检表行；名册小节留痕加注）。
"""
import argparse
import collections
import csv
import importlib.util
import json
import os
import re
import subprocess
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
SAGA = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SAGA))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
SIEVE = os.path.join(DATA, 'sieve.json')
DRY = os.path.join(DATA, 'AB并池_预演_2026-10-29.csv')
WATCH = os.path.join(DATA, 'P池_巡检表_2026-10-29.csv')
ROSTER = os.path.join(ROOT, 'docs', 'P池_资产池名册_2026-10-29.md')
BATCH = 'AB-01'
DATE = '2026-10-29'
NEXT_CHECK = '2026-12-28'
MARK = '## Saga A/B 并池 · 批 AB-01'
CONC = {'P 核心': ('pool', '★'), 'P 核心候选': ('pool', '★'), 'P 正式候选': ('pool', '○'), 'P 观察候选': ('pool_watch', '☆')}
GROUP_ORDER = ['四主区 + 波兰', '欧洲其他', '俄语区', '印度 / 南亚', '东亚 / 东南亚 / 大洋洲', '中东 / 非洲', '拉美', '其他']


def _mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def short(s, n):
    s = re.sub(r'\s+', ' ', s or '')
    return s if len(s) <= n else s[:n - 1] + '…'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--undo', action='store_true')
    a = ap.parse_args()
    now = subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()
    sieve = _mod('saga_sieve', os.path.join(SAGA, 'sieve.py'))
    s = sieve.load_sieve()
    ents = {e['code']: e for e in json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))}
    wrows = list(csv.DictReader(open(WATCH, encoding='utf-8-sig')))
    fields = list(wrows[0].keys())

    if a.undo:
        codes = [k for k, v in s.items() if k != '_meta' and v.get('batch') == BATCH]
        for k in codes:
            s.pop(k)
        cnt = sieve.save_sieve(s)
        keep = [r for r in wrows if r['编号'] not in set(codes)]
        with open(WATCH, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(keep)
        t = open(ROSTER, encoding='utf-8').read().rstrip('\n')
        t += f'\n\n> {now} {DATE} **AB-01 已撤销**（`ab_pool_001.py --undo`）：上节 {len(codes)} 户池位移除，等级本来就没动。\n'
        open(ROSTER, 'w', encoding='utf-8').write(t)
        print('undo', len(codes), 'sieve', dict(cnt), 'csv', len(keep))
        return

    dry = list(csv.DictReader(open(DRY, encoding='utf-8-sig')))
    have_csv = {r['编号'] for r in wrows}
    added, new_csv, roster_rows = 0, [], []
    c_v, c_g, c_grp = collections.Counter(), collections.Counter(), collections.Counter()
    for r in dry:
        conc = r['预演结论']
        if conc not in CONC:
            continue
        code = r['编号']
        e = ents.get(code)
        assert e and e['grade'] in ('A', 'B'), code
        verdict, g = CONC[conc]
        tags = [t for t in (r['标签'] or '').split('、') if t]
        if conc in ('P 核心', 'P 核心候选'):
            tags.append('core')
        if conc == 'P 核心' and 'A 复核' in (r['理由'] or ''):
            tags.append('a_review')
        if 'gg' in (r['红旗'] or ''):
            tags.append('gg')
        if '巨头' in (r['红旗'] or '') and 'giant' not in tags:
            tags.append('giant')
        tags = sorted(OrderedDict.fromkeys(tags))
        why = r['理由'].replace('**', '')
        reason = (f"{g} P 池{'正式' if verdict == 'pool' else '观察'}（{conc}，{e['grade']} 档并池 · 等级不动）：{why}"
                  f"；命中 {r['命中/6']}/6（成单/样品 {r['成单/样品'] or '—'} · 真回 {r['真回'] or '—'} · WA {r['WA'] or '—'} · 对位 {r['对位'] or '—'} · 登记 {r['登记'] or '—'} · 体量 {short(r['体量'], 30) or '—'}）")
        if 'gg' in tags:
            reason += '；Simon: gg（难复购）→ 首触只一句问候 + 新品，不推单'
        if 'a_review' in tags:
            reason += '；A 复核：等 A 新标准一起看（池位先给，不降级）'
        row = s.get(code)
        if row and row.get('batch') != BATCH:
            raise SystemExit(f'{code} 已有非 AB-01 的 sieve 行：{row}')
        s[code] = {'verdict': verdict, 'gate': 3, 'rule': 'AB1', 'reason': reason, 'date': DATE, 'manual': False, 'batch': BATCH,
                   'origin': f"Saga-{e['grade']}", 'ab_conc': conc, 'grade': g, 'next_check': NEXT_CHECK, 'tags': tags}
        added += 1
        c_v[verdict] += 1
        c_g[g] += 1
        c_grp[(r['区域组'], verdict)] += 1
        links = list(OrderedDict.fromkeys((e.get('domains') or []) + [u for u in (e.get('platform_links') or []) if 'google.com/search' not in u and 'yandex.com/search' not in u]))
        roster_rows.append((r['区域组'], verdict, g, code, e, r, tags))
        if code not in have_csv:
            new_csv.append({'编号': code, '档位': g, '入池': '正式' if verdict == 'pool' else '观察', '公司': r['公司（登记名优先）'] or e.get('name'), '国家': e.get('country') or r['国家'] or '未填',
                            '区域组': r['区域组'], '域名 / 平台链接': ' | '.join(links), '标签': '、'.join(tags), '上次巡检': DATE, '下次巡检': NEXT_CHECK,
                            '巡检项': '官网改版 / 新品 / 招聘 / 社媒（LinkedIn / FB / IG）/ GitHub / 展会出席 / 新闻稿 / 域名 MX 存活',
                            '备注': short(f"{e['grade']} 档并池（{conc}）：{why}", 160) + ('；Simon: gg（难复购）首触只问候' if 'gg' in tags else '')})
    cnt = sieve.save_sieve(s)
    if new_csv:
        order = {'★★': 0, '★': 1, '○': 2, '△': 3, '☆': 4}
        new_csv.sort(key=lambda x: (GROUP_ORDER.index(x['区域组']) if x['区域组'] in GROUP_ORDER else 9, x['入池'] != '正式', order.get(x['档位'], 9), x['编号']))
        with open(WATCH, 'a', encoding='utf-8-sig', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writerows(new_csv)
    t = open(ROSTER, encoding='utf-8').read()
    if MARK not in t:
        L = ['', f'{MARK}（T29-U125，{DATE} {now}；Q-71 默认方案执行，`sieve_batches/ab_pool_001.py`，可 `--undo`）', '',
             f"> 只加池位、等级不动。A 90 全部 → 正式 ★（19 户 `a_review` 等 A 新标准）；B 核心候选 64 → 正式 ★（gg 8 户带 `gg`）；B 正式候选 38 → 正式 ○；B 观察候选 181 → 观察 ☆。"
             f" 本批 {added} 户：正式 {c_v['pool']} / 观察 {c_v['pool_watch']}（★ {c_g['★']} / ○ {c_g['○']} / ☆ {c_g['☆']}）。留 B 847 / 复核 8 / 守界 1 不动（继续走发送包）。"
             f" 并池后 P 池 = 正式 {cnt['pool']} / 观察 {cnt['pool_watch']}（含 C 池 243 / 59）。", '',
             '| 区域组 | 正式 | 观察 |', '|---|---|---|']
        for grp in GROUP_ORDER:
            if c_grp[(grp, 'pool')] or c_grp[(grp, 'pool_watch')]:
                L.append(f"| {grp} | {c_grp[(grp, 'pool')]} | {c_grp[(grp, 'pool_watch')]} |")
        L += ['', '| 档 | 编号 | 等级 | 公司 | 国家 | 区域组 | 预演结论 | 标签 | 理由（摘） |', '|---|---|---|---|---|---|---|---|---|']
        order = {'★': 0, '○': 1, '☆': 2}
        for grp, v, g, code, e, r, tags in sorted(roster_rows, key=lambda x: (x[1] != 'pool', order[x[2]], GROUP_ORDER.index(x[0]) if x[0] in GROUP_ORDER else 9, x[3])):
            L.append(f"| {g} | `{code}` | {e['grade']} | {short(r['公司（登记名优先）'] or e.get('name'), 40).replace('|', '｜')} | {e.get('country') or '未填'} | {grp} | {r['预演结论']} | {'、'.join(tags)} | {short(r['理由'].replace('**', ''), 110).replace('|', '｜')} |")
        L.append('')
        open(ROSTER, 'w', encoding='utf-8').write(t.rstrip('\n') + '\n' + '\n'.join(L))
    print(BATCH, 'added', added, dict(c_v), dict(c_g), 'csv +', len(new_csv), 'sieve', dict(cnt))


if __name__ == '__main__':
    main()
