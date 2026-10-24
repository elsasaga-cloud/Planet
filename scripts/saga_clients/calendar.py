#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saga Clients · 跟进日历：从 research/<code>.json 的 next_move 渲染「现在 / 下月」清单。

只读 JSON，不改任何档案。输出 docs/跟进日历_<YYYY-MM>.md。
用法：python3 calendar.py [YYYY-MM]   （默认 = 下个月）
"""
import ast
import datetime as dt
import json
import os
import sys
from collections import defaultdict

from common import DATA, ROOT

ENT = os.path.join(DATA, 'entities.json')
RES = os.path.join(DATA, 'research')

REGION_ORDER = ['北美', '欧洲', '土耳其', '其他']
REGION_MAP = {'US': '北美', 'CA': '北美', 'TR': '土耳其'}
EU = set('AT BE BG HR CY CZ DK EE FI FR DE GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE GB CH NO IS UA RS BA ME MK AL MD BY GE AM AZ'.split())

BIND_RANK = ['深', '较深', '中度', '轻度绑定', '轻度', '读而不回', '轻度触达', '未绑定', '未发信', '未触达']


def region(e):
    iso = (e.get('iso') or '').upper()
    if iso in REGION_MAP:
        return REGION_MAP[iso]
    if iso in EU:
        return '欧洲'
    return '其他'


def bind_rank(level):
    for i, k in enumerate(BIND_RANK):
        if level.startswith(k):
            return i
    return len(BIND_RANK)


def lst(v):
    if isinstance(v, list):
        return v
    try:
        return ast.literal_eval(v) if v else []
    except Exception:
        return []


def main():
    month = sys.argv[1] if len(sys.argv) > 1 else (dt.date.today().replace(day=1) + dt.timedelta(days=32)).strftime('%Y-%m')
    ents = json.load(open(ENT, encoding='utf-8'))
    ents = ents if isinstance(ents, list) else list(ents.values())
    now, mon = [], []
    for e in ents:
        if e.get('grade') not in ('A', 'B'):
            continue
        p = os.path.join(RES, f"{e['code']}.json")
        if not os.path.exists(p):
            continue
        mr = json.load(open(p, encoding='utf-8')).get('mail_review') or {}
        nm = mr.get('next_move') or {}
        when = str(nm.get('when', ''))
        if not when:
            continue
        b = mr.get('binding') or {}
        row = {
            'code': e['code'], 'name': (e.get('name') or '')[:28], 'country': e.get('country') or '', 'grade': e.get('grade'),
            'region': region(e), 'level': str(b.get('level', ''))[:14], 'rank': bind_rank(str(b.get('level', ''))),
            'when': when, 'channel': str(nm.get('channel', ''))[:26], 'action': str(nm.get('action', '')),
            'q': str(nm.get('one_question', '')), 'subj': str((mr.get('draft_en') or {}).get('subject', ''))[:60],
            'facts': len(mr.get('facts') or []),
        }
        if '现在' in when or '本周' in when:
            now.append(row)
        elif month in when:
            mon.append(row)

    def kind(r):
        a = r['action'] + r['channel']
        if any(k in a for k in ['首封', 'email_hook', '短信一问', '一句话']) and r['rank'] >= bind_rank('轻度触达'):
            return '首触一句话（可一天批量发）'
        if any(k in a for k in ['补答', '回原线程', '回复']):
            return '补答 / 回原线程'
        return '个别跟进（按证据写）'

    L = [f'# 跟进日历 {month}（自动生成，勿手改；来源 research/*.json → next_move）', '',
         f'生成：{dt.datetime.utcnow().strftime("%Y-%m-%d %H:%MZ")}。只列 A/B；每行 = 一句话问题（已在各户档案 `next_move.one_question` / `draft_en`）。排序：绑定深 → 浅；地区：北美 → 欧洲 → 土耳其 → 其他。',
         '', f'**现在就做：{len(now)} 户 · {month}：{len(mon)} 户**', '']

    def table(rows, title):
        if not rows:
            return
        L.append(f'## {title}（{len(rows)}）'); L.append('')
        groups = defaultdict(list)
        for r in rows:
            groups[kind(r)].append(r)
        for k in ['个别跟进（按证据写）', '补答 / 回原线程', '首触一句话（可一天批量发）']:
            rs = groups.get(k) or []
            if not rs:
                continue
            L.append(f'### {k}（{len(rs)}）'); L.append('')
            L.append('| 户 | 公司 | 国家 | 级 | 绑定 | 时点 | 渠道 | 一句话 |'); L.append('|---|---|---|---|---|---|---|---|')
            rs.sort(key=lambda r: (REGION_ORDER.index(r['region']), r['rank'], -r['facts']))
            for r in rs:
                q = (r['q'] or r['action']).replace('|', '／').replace('\n', ' ')
                L.append(f"| {r['code']} | {r['name']} | {r['country']} | {r['grade']} | {r['level']} | {r['when'][:16]} | {r['channel']} | {q[:160]} |")
            L.append('')

    table(now, '现在')
    table(mon, month)
    L.append('## 用法'); L.append('')
    L.append('- 「个别跟进」每户打开档案看 `facts` 最后三条再发；「首触一句话」可以同一天用 A 邮箱批量发（每封只改公司名/型号）；「补答」回原线程，不开新线程。')
    L.append('- 发完把结果写回档案（`next_move.when` 改成下一时点），重跑 `calendar.py` 即可刷新本页。')
    out = os.path.join(ROOT, 'docs', f'跟进日历_{month}.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(out, len(now), len(mon))


if __name__ == '__main__':
    main()
