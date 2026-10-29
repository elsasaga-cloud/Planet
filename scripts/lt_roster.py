#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群（Q-76）总名册 + 复核队列生成器（T29-U128 起；每次等级 / 复核状态变动后重跑）。

三库只从数据读（render-from-JSON）：
  Saga    data/saga_clients/entities.json（grade / research.lt_review / sieve 池行）
  External data/external_clients/{cctv,edgecore,mikrotik}.json + overrides.json + research/*.json（final_grade 同 render.py）
  Planet  data/客户名单_Planet渠道_2026-10.csv（人工定级 / 长期群复核）
输出：docs/长期客户群_名册_2026-10-29.md、data/长期客户群_复核队列_2026-10-29.csv
"""
import csv
import json
import os
import re
import subprocess
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(ROOT, 'data')
OUT_MD = os.path.join(ROOT, 'docs', '长期客户群_名册_2026-10-29.md')
OUT_Q = os.path.join(D, '长期客户群_复核队列_2026-10-29.csv')
DATE = '2026-10-29'
MAIN = {'US', 'CA', 'TR', 'GB', 'DE', 'PL'}
EUROPE = {'GB', 'IE', 'FR', 'DE', 'NL', 'BE', 'LU', 'AT', 'CH', 'LI', 'IT', 'ES', 'PT', 'DK', 'SE', 'NO', 'FI', 'IS', 'PL', 'CZ', 'SK', 'HU',
          'SI', 'HR', 'RS', 'BA', 'ME', 'MK', 'AL', 'GR', 'CY', 'MT', 'RO', 'BG', 'EE', 'LV', 'LT', 'MD', 'XK'}
RU_ZONE = {'RU', 'BY', 'KZ', 'UZ', 'KG', 'TJ', 'TM', 'AM', 'AZ', 'GE', 'MD'}


def grp(iso):
    if iso in MAIN:
        return '四主区 + 波兰'
    if iso in EUROPE:
        return '欧洲其他'
    if iso in RU_ZONE:
        return '俄语区'
    if iso in {'IN', 'PK', 'BD', 'LK', 'NP'}:
        return '印度 / 南亚'
    if iso in {'KR', 'JP', 'TW', 'HK', 'SG', 'MY', 'TH', 'VN', 'ID', 'PH', 'AU', 'NZ', 'MM', 'KH'}:
        return '东亚 / 东南亚 / 大洋洲'
    if iso in {'AE', 'SA', 'QA', 'KW', 'BH', 'OM', 'IL', 'JO', 'LB', 'IQ', 'EG', 'MA', 'TN', 'DZ', 'ZA', 'NG', 'KE', 'TZ', 'GH', 'ET', 'UG', 'ZM', 'ZW', 'MU', 'CI', 'SN', 'CM', 'AO', 'MZ', 'NA', 'BW', 'RW', 'LY'}:
        return '中东 / 非洲'
    if iso in {'MX', 'BR', 'AR', 'CL', 'CO', 'PE', 'EC', 'VE', 'BO', 'PY', 'UY', 'CR', 'PA', 'GT', 'HN', 'SV', 'NI', 'DO', 'JM', 'TT', 'PR', 'CU'}:
        return '拉美'
    return '其他'


GROUP_ORDER = ['四主区 + 波兰', '欧洲其他', '俄语区', '印度 / 南亚', '东亚 / 东南亚 / 大洋洲', '中东 / 非洲', '拉美', '其他']


def short(s, n):
    s = re.sub(r'\s+', ' ', str(s or ''))
    return s if len(s) <= n else s[:n - 1] + '…'


def main():
    now = subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()
    rows = []   # dict: origin, code, name, country, iso, grade, review(status), prio, why, evidence, domain
    # Saga
    E = json.load(open(os.path.join(D, 'saga_clients', 'entities.json'), encoding='utf-8'))
    sieve = json.load(open(os.path.join(D, 'saga_clients', 'sieve.json'), encoding='utf-8'))
    for e in E:
        if e['grade'] not in 'AB':
            continue
        rs = e.get('research') or {}
        rv = rs.get('lt_review') or {}
        sv = sieve.get(e['code']) or {}
        f = e.get('flags') or {}
        ev = []
        if f.get('deal'):
            ev.append('成单')
        if f.get('sample'):
            ev.append('样品')
        if e.get('pi'):
            ev.append('PI')
        if e.get('reply_sub'):
            ev.append(f"真回 {e['reply_sub']}")
        if f.get('wa_added'):
            ev.append('WA')
        if f.get('own_brand'):
            ev.append('自牌')
        if sv.get('grade'):
            ev.append(f"池位 {sv['grade']}")
        rows.append({'origin': 'Saga', 'code': e['code'], 'name': e.get('name') or '', 'country': e.get('country') or '未填', 'iso': e.get('iso') or '',
                     'grade': e['grade'], 'review': rv.get('status') or ('已过·登记 + 加厚' if e['code'][:2] in ('SA', 'SB') else '—'),
                     'prio': rv.get('prio') or 0, 'why': rv.get('why') or '', 'evidence': ' · '.join(ev) or '—',
                     'domain': (e.get('domains') or [''])[0], 'tags': '、'.join(sv.get('tags') or [])})
    # External
    xov = json.load(open(os.path.join(D, 'external_clients', 'overrides.json'), encoding='utf-8'))
    cards = {}
    rdir = os.path.join(D, 'external_clients', 'research')
    for fn in os.listdir(rdir):
        if fn.endswith('.json'):
            c = json.load(open(os.path.join(rdir, fn), encoding='utf-8'))
            cards[c['code']] = c
    for fn, repo in [('cctv.json', 'CCTV-PoE'), ('edgecore.json', 'Edgecore'), ('mikrotik.json', 'mikrotik-info')]:
        for r in json.load(open(os.path.join(D, 'external_clients', fn), encoding='utf-8'))['records']:
            if r.get('grade') == 'DELETE':
                continue
            o = xov.get(r['code'])
            c = cards.get(r['code'])
            g = o['grade'] if o else (c['grade_final'] if c else r['grade'])
            if g not in 'AB':
                continue
            rv = (o or {}).get('review') or {}
            ev = []
            if (o or {}).get('x_prio'):
                ev.append('原 XA')
            if c:
                ev.append('研究卡 ' + short(c.get('fit') or c.get('type_final') or '', 40))
            if 'S箱有来信' in (r.get('flags') or []):
                ev.append('S 箱有来信')
            if r.get('touch'):
                ev.append('发送包已触达')
            rows.append({'origin': f'External·{repo}', 'code': r['code'], 'name': r.get('name') or '', 'country': r.get('country_zh') or '未填', 'iso': r.get('iso') or '',
                         'grade': g, 'review': rv.get('status') or '—', 'prio': rv.get('prio') or 0, 'why': (o or {}).get('reason', ''),
                         'evidence': ' · '.join(ev) or short(r.get('type') or '', 40), 'domain': r.get('domain') or '', 'tags': ''})
    # Planet
    for r in csv.DictReader(open(os.path.join(D, '客户名单_Planet渠道_2026-10.csv'), encoding='utf-8-sig')):
        g = (r.get('人工定级') or r['评级']).strip()[:1]
        if g not in 'AB' or r['状态'].startswith('并入'):
            continue
        note = r.get('长期群复核') or ''
        m = re.search(r'待过·优先级 (\d)', note)
        rows.append({'origin': 'Planet 仓', 'code': r['档案编号'], 'name': r['公司名'], 'country': r['国家'], 'iso': '',
                     'grade': g, 'review': '待过' if m else ('随主档' if '随主档' in note else ('留B' if '留B·' in note else '—')), 'prio': int(m.group(1)) if m else 0,
                     'why': note, 'evidence': short(r['信号（在卖什么品牌）'], 50), 'domain': r['网站'], 'tags': ''})
    for x in rows:
        x['grp'] = grp(x['iso']) if x['iso'] else '其他'

    # 复核队列 CSV
    q = [x for x in rows if x['review'] == '待过']
    q.sort(key=lambda x: (x['prio'], GROUP_ORDER.index(x['grp']) if x['grp'] in GROUP_ORDER else 9, x['origin'], x['code']))
    with open(OUT_Q, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['优先级', '来源', '编号', '公司', '国家', '区域组', '现等级', '域名', '现有证据', '为什么要过', '复核批次', '复核结论', '复核日期'])
        for x in q:
            w.writerow([x['prio'], x['origin'], x['code'], x['name'], x['country'], x['grp'], x['grade'], x['domain'], x['evidence'], short(x['why'], 160), '', '', ''])

    # 名册 MD
    by_o = Counter((x['origin'].split('·')[0], x['grade']) for x in rows)
    by_r = Counter((x['origin'].split('·')[0], x['review'] if x['review'] in ('待过',) else '已过 / 不需过') for x in rows)
    by_p = Counter(x['prio'] for x in q)
    L = [f'# 长期客户群 · 总名册（Q-76 单一体系）', '', f'生成：{DATE} {now}（`scripts/lt_roster.py`，只从三库数据读；等级一变就重跑）', '',
         '## 0. 这是什么', '',
         '- **长期客户群 = 等级 A + B（三库同一把尺子）。A = 核心 · 精华跟（有真人往来 / 成单 / 样品 / PI 的对位户）；B = 普通跟（对位 + 活着 + 有路径）。**',
         '- 群外：C = 储备（活着但没路径 / 不对位 / 个人 / 守界；不跟不发，冒头再捞）；永久 pass = 走（硬标准，三闸已定）。',
         '- 原「P 池」概念并入本名册（P 池 = 长期客户群；旧名册 / 巡检表 / 巡检清单保留为 2026-12-28 巡检的输入）。',
         '- 升降只三条：回信 / 询价 → 升一档；两轮跟进没动静 → 降一档；弹回 / 明确停发 → pass。',
         '- **复核（Simon U128 第 5 条）**：没咋调研过的户要「过一遍」（官网 / 进口数据 / 项目 → 行业内 + 对位 + 有成单可能），不明朗直接打回 C。队列见 §2 与 `data/长期客户群_复核队列_2026-10-29.csv`。', '',
         '## 1. 数字', '', '| 库 | A 核心 | B 普通跟 | 小计 | 其中 待过 |', '|---|---|---|---|---|']
    tot = Counter()
    for o in ['Saga', 'External', 'Planet 仓']:
        a, b = by_o[(o, 'A')], by_o[(o, 'B')]
        L.append(f"| {o} | {a} | {b} | {a + b} | {by_r[(o, '待过')]} |")
        tot['A'] += a
        tot['B'] += b
        tot['q'] += by_r[(o, '待过')]
    L.append(f"| **合计** | **{tot['A']}** | **{tot['B']}** | **{tot['A'] + tot['B']}** | **{tot['q']}** |")
    L += ['', f"复核队列 {len(q)}：优先级 1（C 捞上来的、从未深挖）{by_p[1]} / 优先级 2（Saga 冷 B「对位未知」）{by_p[2]} / 优先级 3（外部库 / Planet 仓的 B，只有名录级信息）{by_p[3]}。", '',
          '| 区域组 | A | B | 待过 |', '|---|---|---|---|']
    bg = Counter((x['grp'], x['grade']) for x in rows)
    bq = Counter(x['grp'] for x in q)
    for g in GROUP_ORDER:
        if bg[(g, 'A')] or bg[(g, 'B')]:
            L.append(f"| {g} | {bg[(g, 'A')]} | {bg[(g, 'B')]} | {bq[g]} |")
    L += ['', '## 2. 复核队列（怎么过 / 结论怎么落）', '',
          '- 过法：官网业务线（卖什么、给谁装）→ 进口 / 海关线索（Volza / ImportYeti / Panjiva 摘要、海关编码）→ 项目 / 案例 / 招聘 → 登记底数（已坐实的不重查）。每户 1–2 次检索，查不到就按「不明朗」处理。',
          '- 结论三选一：**留 B**（行业内 + 对位 + 有成单可能，证据写进档案）/ **打回 C**（不明朗 / 不对位 / 纯零售 / 个人）/ **升 A**（极少：发现真人往来或成单证据）。',
          '- 落点：Saga → 研究档 `lt_review.status` + 事实；External → `overrides.json`；Planet → CSV「长期群复核」；队列 CSV「复核批次 / 结论 / 日期」。每批 30–60 户，批文件 `scripts/saga_clients/lt_review_batches/lt_r_0NN.py`。', '',
          '## 3. A 核心（精华跟）', '', '| 编号 | 公司 | 国家 | 区域组 | 证据 | 池标签 |', '|---|---|---|---|---|---|']
    for x in sorted([x for x in rows if x['grade'] == 'A'], key=lambda x: (GROUP_ORDER.index(x['grp']) if x['grp'] in GROUP_ORDER else 9, x['code'])):
        L.append(f"| `{x['code']}` | {short(x['name'], 40).replace('|', '｜')} | {x['country']} | {x['grp']} | {x['evidence']} | {x['tags']} |")
    L += ['', '## 4. B 普通跟（按库 · 区域；「复核」列 = 待过 / 已过）', '']
    for o in ['Saga', 'External', 'Planet 仓']:
        sub = [x for x in rows if x['grade'] == 'B' and x['origin'].split('·')[0] == o]
        L += [f'### 4.{["Saga", "External", "Planet 仓"].index(o) + 1} {o}（{len(sub)}）', '', '| 编号 | 公司 | 国家 | 区域组 | 复核 | 证据 / 来源 |', '|---|---|---|---|---|---|']
        for x in sorted(sub, key=lambda x: (x['review'] != '待过', x['prio'], GROUP_ORDER.index(x['grp']) if x['grp'] in GROUP_ORDER else 9, x['code'])):
            rv = x['review'] + (f"·P{x['prio']}" if x['review'] == '待过' else '')
            L.append(f"| `{x['code']}` | {short(x['name'], 40).replace('|', '｜')} | {x['country']} | {x['grp']} | {rv} | {short(x['evidence'], 60).replace('|', '｜')} |")
        L.append('')
    open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('roster', len(rows), dict(tot), 'queue', len(q), dict(by_p))


if __name__ == '__main__':
    main()
