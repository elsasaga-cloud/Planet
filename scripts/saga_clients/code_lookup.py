#!/usr/bin/env python3
"""查编号（2026-10-25 重排前后对照）。

用法：python3 scripts/saga_clients/code_lookup.py SA-046 SB-1118 ...
对每个输入同时按「旧编号」和「新编号」两列查 data/saga_clients/编号映射_2026-10-25.csv，并给出现在的档案路径。
对话全记录 / 变更日志 / V0 答卷里出现的编号都是旧编号；README / docs / data / Saga Clients 里的都是新编号。
"""
import csv
import glob
import os
import subprocess
import sys

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MAP = glob.glob(os.path.join(ROOT, 'data', 'saga_clients', '编号映射_*.csv'))


def main(args):
    rows = []
    for p in sorted(MAP):
        rows += list(csv.DictReader(open(p, encoding='utf-8-sig')))
    if not args:
        print(__doc__)
        return
    for q in args:
        q = q.strip().upper()
        hit = False
        for r in rows:
            if r['旧编号'].upper() == q:
                hit = True
                print(f"{q} 是旧编号 → 现为 {r['新编号']}（{r['等级']}）{r['名称']}" + (f" · {r['国家']}" if r['国家'] else ''))
                show(r['新编号'])
        for r in rows:
            if r['新编号'].upper() == q:
                hit = True
                print(f"{q} 是新编号 ← 旧为 {r['旧编号']}（{r['等级']}）{r['名称']}" + (f" · {r['国家']}" if r['国家'] else ''))
                show(r['新编号'])
        if not hit:
            print(f'{q}：映射表里没有（可能是重排后新增的编号，直接到 Saga Clients/ 找）')
            show(q)


def show(code):
    if code.startswith('旧'):
        return
    for p in glob.glob(os.path.join(ROOT, 'Saga Clients', '*', '**', code + '-*.md'), recursive=True):
        print('   档案：' + os.path.relpath(p, ROOT))


if __name__ == '__main__':
    main(sys.argv[1:])
