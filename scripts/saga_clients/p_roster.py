#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P 池总名册（一页、可重生成）—— 从最新 `data/saga_clients/P池_巡检表_*.csv` 生成 `docs/P池_总名册.md`。

批次名册 `docs/P池_资产池名册_2026-10-29.md` 是按批追加的历史；这份是**当前快照**：按区域组 → 档位 → 编号列全部入池户，
带来源库 / 标签 / 判语摘要，供 Simon 一页看完「资产池里到底有谁」。数据以巡检表为准，不手改本文件。

用法：python3 scripts/saga_clients/p_roster.py [--csv 路径] [--out 路径]
"""
import argparse
import collections
import csv
import glob
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
GROUP_ORDER = ['四主区 + 波兰', '欧洲其他', '俄语区', '印度 / 南亚', '东亚 / 东南亚 / 大洋洲', '中东 / 非洲', '拉美', '其他']
STAR_ORDER = {'★★': 0, '★': 1, '○': 2, '☆': 3, '△': 4}
STAR_LABEL = {'★★': '核心（成单 / 深绑定）', '★': '重点（体量 + 对位 + 登记齐 / 自有品牌）', '○': '正式（对位 + 登记坐实或部分坐实）', '☆': '观察（微型 / 对位一般，试单后转正）', '△': '观察（疑点待核）'}


def origin_of(code):
    return {'SC': 'Saga C', 'SB': 'Saga B', 'SA': 'Saga A', 'XC': 'External', 'PA': 'Planet 仓', 'PB': 'Planet 仓', 'PC': 'Planet 仓'}.get(code[:2], code[:2])


def gist(note, n=110):
    s = note
    s = re.sub(r'^来源：[^；]*；', '', s)
    s = re.sub(r'^[★○☆△]+\s*', '', s)
    s = s.replace('|', '｜')
    return s[:n] + ('…' if len(s) > n else '')


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', default=None)
    ap.add_argument('--out', default=os.path.join(ROOT, 'docs', 'P池_总名册.md'))
    a = ap.parse_args(argv)
    path = a.csv or sorted(glob.glob(os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_*.csv')))[-1]
    with open(path, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    now = subprocess.check_output(['date', '-u', '+%Y-%m-%d %H:%MZ']).decode().strip()
    by_g = collections.defaultdict(list)
    for r in rows:
        by_g[r['区域组']].append(r)
    n_f = sum(1 for r in rows if r['入池'] == '正式')
    stars = collections.Counter(r['档位'] for r in rows)
    origins = collections.Counter(origin_of(r['编号']) for r in rows)
    tags = collections.Counter(t for r in rows for t in r['标签'].split('、') if t)
    nxt = collections.Counter(r['下次巡检'] for r in rows).most_common(1)[0][0]
    L = [f'# P 池总名册（当前快照 · 生成 {now}）', '',
         f'> 源：`{os.path.relpath(path, ROOT)}`（{len(rows)} 户 = 正式 {n_f} / 观察 {len(rows) - n_f}）。档位 ' + ' · '.join(f'{s} {stars[s]}' for s in STAR_ORDER if stars.get(s)) +
         '；来源 ' + ' · '.join(f'{k} {v}' for k, v in origins.most_common()) + f'；下次人工巡检 {nxt}（清单 `docs/P池_巡检清单_{nxt}.md`）。'
         ' 批次历史与评估口径见 `docs/P池_资产池名册_2026-10-29.md`；筛选方法见 `docs/C池三闸筛选_方案_2026-10-29.md`。A / B 档并池见 `docs/AB并池方案_草案_2026-10-29.md`（预演，未执行）。',
         '', '## 0. 一眼', '', '| 区域组 | 正式 | 观察 | 合计 |', '|---|---|---|---|']
    for g in GROUP_ORDER:
        rs = by_g.get(g) or []
        if rs:
            L.append(f'| {g} | {sum(1 for r in rs if r["入池"] == "正式")} | {sum(1 for r in rs if r["入池"] != "正式")} | {len(rs)} |')
    L += [f'| **合计** | **{n_f}** | **{len(rows) - n_f}** | **{len(rows)}** |', '',
          '档位：' + '；'.join(f'{s} = {STAR_LABEL[s]}' for s in STAR_ORDER) + '。',
          '标签：' + '、'.join(f'`{k}` {v}' for k, v in tags.most_common()) + '。',
          '（`q33_hold` 只巡检不主动发；`civil_only` 只谈民用项目；`ru_payment` 先问收款；`prepay` 预付 100%；`reg_pending` 注册号待补；`dayjob_fit` 需求在光端机 / DWDM / 光模块，Simon 日职线可用；`oem_target` 自有品牌 → OEM 30% 线）', '']
    for g in GROUP_ORDER:
        rs = by_g.get(g)
        if not rs:
            continue
        rs.sort(key=lambda r: (r['入池'] != '正式', STAR_ORDER.get(r['档位'], 9), r['编号']))
        L += [f'## {g}（{len(rs)} 户）', '', '| 编号 | 档 | 入池 | 公司 | 国家 | 来源 | 标签 | 判语（摘） |', '|---|---|---|---|---|---|---|---|']
        for r in rs:
            L.append(f"| {r['编号']} | {r['档位']} | {r['入池']} | {r['公司'][:44].replace('|', '｜')} | {r['国家']} | {origin_of(r['编号'])} | {r['标签']} | {gist(r['备注'])} |")
        L.append('')
    open(a.out, 'w', encoding='utf-8').write('\n'.join(L))
    print(a.out, len(rows), dict(stars), dict(origins))


if __name__ == '__main__':
    main()
