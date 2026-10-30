#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A 类挖底进度板：data/saga_clients/A挖底_进度_<date>.csv + docs/A挖底_进度.md（每户 × 维度 的条数；缺口；按区域排队）。"""
import csv
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intel_store as IS  # noqa: E402

ROOT = IS.ROOT
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-30'
PRI = {'土耳其': 0, '北美': 1, '欧洲': 2, '俄语区': 3, '南亚': 4, '亚太': 5, '中东': 6, '非洲': 7, '拉美': 8}


def main():
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    A = sorted([e for e in ents.values() if e['grade'] == 'A'], key=lambda e: (PRI.get(e['region'], 9), e['code']))
    rows = []
    for e in A:
        rs = e.get('research') or {}
        st = IS.stats(rs)
        g = IS.gaps(rs)
        items = (rs.get('intel') or {}).get('items') or []
        rows.append({'编号': e['code'], '公司': e['name'], '国家': e['country'], '区域': e['region'], '档': (rs.get('a_deep') or {}).get('tier') or ('A1' if e.get('pi') else ''),
                     **{k: (f"{st[k][0]}" + (f"/未得{st[k][1]}" if st[k][1] else '')) if k in st else '' for k in IS.KINDS},
                     '条数': len(items), '缺口': '、'.join(g), '最近批次': max([x.get('batch', '') for x in items] + ['']), '状态': '未开挖' if not items else ('已过一遍' if not g else '挖掘中')})
    p = os.path.join(SD, f'A挖底_进度_{DATE}.csv')
    with open(p, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    c = Counter(r['状态'] for r in rows)
    kc = Counter()
    for r in rows:
        for k in IS.KINDS:
            if r[k]:
                kc[k] += 1
    L = [f'# A 类「挖个底掉」进度板（{DATE}）\n',
         '> Simon（T29-U138）：A 类要挖个底掉——年报、领英、KP、人事变动、参加的展会、论坛、GitHub……商业世界里挂得上的都挖进仓库。一轮一轮搞。本板由 `scripts/saga_clients/intel/progress.py` 生成；明细在每户研究档 `intel` 与 MD「商业情报·挖底」一节。\n',
         f'- A 户 {len(rows)}：已过一遍（核心 7 维度都碰过）{c["已过一遍"]} / 挖掘中 {c["挖掘中"]} / 未开挖 {c["未开挖"]}',
         '- 各维度有记录的户数：' + '、'.join(f'{k} {kc[k]}' for k in IS.KINDS),
         '- 排队顺序：土耳其 → 北美 → 欧洲 → 俄语区 → 南亚 → 亚太 → 中东 → 非洲 → 拉美（每轮按此顺序取未开挖/有缺口的户）',
         '- 维度口径：年报/财务（上市年报、注册处账目、第三方营收估计）· 登记 · 领英公司页（规模/总部/成立）· KP（人名 + 职务 + 链接）· 人事变动（任免/招聘）· 展会/活动 · 新闻/招标 · GitHub/技术足迹（匿名 API）· 社媒 · 供应商/品牌关系 · 论坛/社区 · 官网变化\n',
         '| 编号 | 公司 | 国家 | 档 | 条数 | 状态 | 缺口 | 年报 | 领英 | KP | 人事 | 展会 | 新闻 | GitHub | 品牌关系 |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        L.append(f"| {r['编号']} | {str(r['公司'])[:24].replace('|', '／')} | {str(r['国家'])[:6]} | {r['档']} | {r['条数']} | {r['状态']} | {r['缺口'].replace('、', ' ')} | {r['年报/财务']} | {r['领英公司页']} | {r['KP']} | {r['人事变动']} | {r['展会/活动']} | {r['新闻/招标']} | {r['GitHub/技术足迹']} | {r['供应商/品牌关系']} |")
    open(os.path.join(ROOT, 'docs', 'A挖底_进度.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('rows', len(rows), dict(c), 'kinds', dict(kc))


if __name__ == '__main__':
    main()
