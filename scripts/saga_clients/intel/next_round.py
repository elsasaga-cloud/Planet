#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二遍滚动 · 下一轮工单（T29-U145 2026-10-31）。对每个 A 户按维度算「新鲜度」，过期或缺失 → 进下一轮人工网查清单（含建议查询词）。
阈值（天）：年报/财务 365 · 登记 365 · 领英公司页 180 · KP 180 · 人事变动 90 · 展会/活动 365 · 新闻/招标（日跑自动，不排人工）· GitHub 180（重跑 github_scan）· 供应商/品牌关系 365。
输出：data/saga_clients/A挖底_下一轮_<date>.csv + docs/A挖底_下一轮.md（按区域优先级 土耳其→北美→欧洲→俄→印→其余，每户最多 3 个维度）。"""
import csv
import datetime as _dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intel_store as IS  # noqa: E402

ROOT = IS.ROOT
SD = os.path.join(ROOT, 'data', 'saga_clients')
TODAY = _dt.date.today()
TTL = {'年报/财务': 365, '登记': 365, '领英公司页': 180, 'KP': 180, '人事变动': 90, '展会/活动': 365, 'GitHub/技术足迹': 180, '供应商/品牌关系': 365}
PRI = {'土耳其': 0, '北美': 1, '欧洲': 2, '俄语区': 3, '南亚': 4, '亚太': 5, '中东': 6, '非洲': 7, '拉美': 8}
QUERY = {
    '年报/财务': '{name} annual report OR revenue OR Jahresabschluss OR bilancio OR faaliyet raporu OR выручка',
    '登记': '{name} company registration number address',
    '领英公司页': '{name} linkedin company size headquarters',
    'KP': '{name} CEO OR "managing director" OR "purchasing manager" OR "product manager"',
    '人事变动': '{name} appoints OR joins OR hiring OR new CEO 2026',
    '展会/活动': '{name} exhibitor 2026 OR fuar OR Messe OR exhibition booth',
    'GitHub/技术足迹': 'python3 scripts/saga_clients/intel/github_scan.py（重扫）',
    '供应商/品牌关系': '{name} distributor OF OR authorized partner OR "own brand" OR OEM',
}


def age_days(items, kind):
    ds = []
    for x in items:
        if x.get('kind') != kind:
            continue
        d = str(x.get('added') or x.get('date') or '')[:10]
        try:
            ds.append((TODAY - _dt.date.fromisoformat(d)).days)
        except Exception:
            pass
    return min(ds) if ds else None


def main():
    scope = sys.argv[sys.argv.index('--scope') + 1] if '--scope' in sys.argv else 'A'
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    rows = []
    for c, e in ents.items():
        if scope == 'A' and e.get('grade') != 'A':
            continue
        if scope != 'A' and not (e.get('grade') == 'B' and ((e.get('research') or {}).get('b_tier') or {}).get('tier') == scope):
            continue
        rs = e.get('research') or {}
        items = (rs.get('intel') or {}).get('items') or []
        name = str(rs.get('name_official') or e.get('name') or '').split('（')[0][:50]
        due = []
        for kind, ttl in TTL.items():
            a = age_days(items, kind)
            if a is None:
                due.append((kind, '缺', 0))
            elif a > ttl:
                due.append((kind, f'{a} 天前', a))
        # 缺失优先、其次最旧；每户最多 3 项
        due.sort(key=lambda x: (x[1] != '缺', -x[2]))
        for kind, why, a in due[:3]:
            rows.append({'优先级': PRI.get(e.get('region'), 9), '区域': e.get('region'), '编号': c, '公司': name, '国家': e.get('country'), '维度': kind, '原因': why, '建议查询': QUERY[kind].format(name=name)})
    rows.sort(key=lambda r: (r['优先级'], r['编号'], r['维度']))
    p = os.path.join(SD, f'{scope}挖底_下一轮_{TODAY.isoformat()}.csv')
    with open(p, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ['编号'])
        w.writeheader()
        w.writerows(rows)
    by = {}
    for r in rows:
        by.setdefault(r['维度'], 0)
        by[r['维度']] += 1
    L = [f'# {scope} 类挖底 · 下一轮工单（{TODAY.isoformat()}）\n',
         '> 第二遍滚动规则：日跑自动进新闻/申报/年报全文/展会名录 → 每轮会话先 `ingest_watch.py` 并入，再按本工单逐户补过期维度（阈值：年报 365 天、登记 365、领英 180、KP 180、人事 90、展会 365、GitHub 180、品牌关系 365）。本页由 `scripts/saga_clients/intel/next_round.py` 生成。\n',
         f"- 待办 {len(rows)} 项（{', '.join(f'{k} {v}' for k, v in sorted(by.items(), key=lambda kv: -kv[1]))}）；顺序：土耳其 → 北美 → 欧洲 → 俄语区 → 南亚 → 亚太 → 中东 → 非洲 → 拉美\n",
         '| 区域 | 编号 | 公司 | 维度 | 原因 | 建议查询 |', '|---|---|---|---|---|---|']
    for r in rows:
        L.append(f"| {r['区域']} | {r['编号']} | {str(r['公司']).replace('|', '／')} | {r['维度']} | {r['原因']} | {str(r['建议查询']).replace('|', '／')} |")
    open(os.path.join(ROOT, 'docs', f'{scope}挖底_下一轮.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('next_round:', len(rows), 'items', by)


if __name__ == '__main__':
    main()
