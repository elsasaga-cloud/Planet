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
WD = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
_DC = os.path.join(DATA, 'dims_country.json')
DIMS_COUNTRY = json.load(open(_DC, encoding='utf-8')) if os.path.exists(_DC) else {}
_HOL = os.path.join(DATA, 'holidays_2026-11_2027-03.json')   # 第 82 批 holidays_cal.py 产物；缺失则该列为 —
HOLIDAYS = (json.load(open(_HOL, encoding='utf-8')).get('countries') or {}) if os.path.exists(_HOL) else {}


def holiday_note(iso, start, end):
    """该国在 [start, end] 内的法定假日 + 惯例停摆（第 82 批）；用于日历「该窗口假日」列。"""
    hc = HOLIDAYS.get((iso or '').upper())
    if not hc:
        return ''
    parts = []
    for d, n in hc.get('legal') or []:
        dd = dt.date.fromisoformat(d)
        if start <= dd <= end:
            parts.append(f'{d[5:]} {n[:18]}')
    for ps, pe, lab, kind in hc.get('practice') or []:
        if dt.date.fromisoformat(ps) <= end and dt.date.fromisoformat(pe) >= start and kind != '供应侧':
            parts.append(f'{ps[5:]}→{pe[5:]} {lab.split("：")[0][:14]}' if ps != pe else f'{ps[5:]} {lab.split("：")[0][:14]}')
    return '；'.join(parts)


def send_hint(iso):
    """该国群发打开率最高的时段（dims.py 统计），换算成北京时间给 Simon 排发信；没有统计的国家返回空。"""
    cw = (DIMS_COUNTRY.get('send_window') or {}).get((iso or '').upper())
    tz = (DIMS_COUNTRY.get('tz') or {}).get((iso or '').upper())
    if not cw or not cw.get('best') or tz is None:
        return ''
    b = cw['best'][0]
    h_bj = b['h'] - tz + 8
    wd = b['wd']
    if h_bj >= 24:
        h_bj -= 24
        wd = (wd + 1) % 7
    elif h_bj < 0:
        h_bj += 24
        wd = (wd - 1) % 7
    return f"{WD[wd]} 北京 {h_bj:02d}–{(h_bj + 2) % 24:02d}（对方 {WD[b['wd']]} {b['h']:02d}–{b['h'] + 2:02d}，{b['rate']}%）"


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
            'hint': send_hint(e.get('iso')),
            'iso': (e.get('iso') or '').upper(),
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

    y, m = int(month[:4]), int(month[5:7])
    m_start, m_end = dt.date(y, m, 1), dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1)
    today = dt.date.today()

    def table(rows, title):
        if not rows:
            return
        if title == '现在':
            ws, we = today, today + dt.timedelta(days=14)
        else:
            ws, we = m_start, m_end
        L.append(f'## {title}（{len(rows)}）'); L.append('')
        groups = defaultdict(list)
        for r in rows:
            groups[kind(r)].append(r)
        for k in ['个别跟进（按证据写）', '补答 / 回原线程', '首触一句话（可一天批量发）']:
            rs = groups.get(k) or []
            if not rs:
                continue
            L.append(f'### {k}（{len(rs)}）'); L.append('')
            L.append('| 户 | 公司 | 国家 | 级 | 绑定 | 时点 | 渠道 | 发信时段（该国打开率最高格） | 该窗口假日（别发的日子） | 一句话 |'); L.append('|---|---|---|---|---|---|---|---|---|---|')
            rs.sort(key=lambda r: (REGION_ORDER.index(r['region']), r['rank'], -r['facts']))
            for r in rs:
                q = (r['q'] or r['action']).replace('|', '／').replace('\n', ' ')
                L.append(f"| {r['code']} | {r['name']} | {r['country']} | {r['grade']} | {r['level']} | {r['when'][:16]} | {r['channel']} | {r['hint'] or '—'} | {holiday_note(r['iso'], ws, we) or '—'} | {q[:160]} |")
            L.append('')

    table(now, '现在')
    table(mon, month)
    L.append('## 用法'); L.append('')
    L.append('- 「个别跟进」每户打开档案看 `facts` 最后三条再发；「首触一句话」可以同一天用 A 邮箱批量发（每封只改公司名/型号）；「补答」回原线程，不开新线程。')
    L.append('- 发完把结果写回档案（`next_move.when` 改成下一时点），重跑 `calendar.py` 即可刷新本页。')
    L.append('- 「发信时段」= 该国全库群发按对方本地时间统计的打开率最高的 2 小时格（`dims.py` → `dims_country.json`，像素口径、只看相对高低），已换算成北京时间；WhatsApp / 微信不受此限。')
    L.append('- 「该窗口假日」= 第 82 批 `holidays_cal.py`（法定 + 惯例停摆）落在本月 / 两周内的日子；假日前一个工作日下午、当天、长假后第一个上午都别发。我方春节停摆（2027-01-25 锁单 → 02-17 复工）对所有国家通用，不在此列重复。总表见 `docs/各国假日避让_2026-11_2027-03.md`。')
    out = os.path.join(ROOT, 'docs', f'跟进日历_{month}.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(out, len(now), len(mon))


if __name__ == '__main__':
    main()
