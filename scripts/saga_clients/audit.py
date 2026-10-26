#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saga Clients · 完整性与去重审计（T27 问 1：「所有客户都录入了吗？重复的都处理了吗？」）

输出：
  data/saga_clients/完整性审计.md      —— 原始行 → 实体 → MD 三级对账（每一行都能找到自己的档案）
  data/saga_clients/疑似重复待确认.md  —— 归并键没连上、但名字 / 域名根 / 电话 / 邮箱本地部分高度相似的实体对（供人工确认 → 人工归并.csv）
退出码 0 = 对账全平；1 = 有漏（看 md）。
"""
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher

from common import DATA, OUT_DIR, ROOT, md_files

GENERIC_LOCAL = {'info', 'sales', 'admin', 'contact', 'office', 'support', 'hello', 'mail', 'export', 'import', 'purchase', 'purchasing',
                 'marketing', 'enquiry', 'enquiries', 'inquiry', 'service', 'hi', 'team', 'order', 'orders', 'ventas', 'vendas', 'kontakt',
                 'biuro', 'satis', 'bilgi', 'commerciale', 'vertrieb', 'achat', 'compras', 'general', 'accounts', 'ceo', 'director', 'manager'}
LEGAL = r'\b(ltd|limited|llc|inc|corp|corporation|co|company|gmbh|srl|s\.r\.l|sl|s\.l|sa|s\.a|bv|b\.v|nv|oy|ab|as|a\.s|sp|z\.o\.o|zoo|sro|s\.r\.o|kft|doo|d\.o\.o|pvt|private|pty|plc|lda|sarl|sas|ооо|оао|зао|ltd\.|şti|sti|tic|san|ve|ltda|eirl|fze|fzc|fzco|llp|pte|sdn|bhd|cv|pt|pl|kg|mbh|ag|ug)\b'


def nname(s):
    s = (s or '').lower()
    s = re.sub(r'https?://|www\.', ' ', s)
    s = re.sub(LEGAL, ' ', s)
    s = re.sub(r'[^a-z0-9\u0400-\u04ff\u4e00-\u9fff ]+', ' ', s)
    return ' '.join(s.split())


def main():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    rows = [json.loads(l) for l in open(os.path.join(DATA, 'rows_raw.jsonl'), encoding='utf-8')]
    out = []
    problems = 0

    # ---------- 1) 原始行 → 实体 ----------
    xlsx_rows = [r for r in rows if 'docx_paragraphs' not in r]
    docx_rows = [r for r in rows if 'docx_paragraphs' in r]
    loc = lambda r: (r['file'], r.get('sheet', ''), int(r.get('row', 0) or 0))
    assigned = Counter()
    for e in ents:
        for s in e['sources']:
            assigned[(s['file'], s.get('sheet', ''), int(s.get('row', 0) or 0))] += 1
    raw_locs = Counter(loc(r) for r in xlsx_rows)
    missing = [l for l in raw_locs if l not in assigned]
    dup_assigned = [l for l, n in assigned.items() if n > 1 and not l[0].endswith('.docx')]
    ghost = [l for l in assigned if l not in raw_locs and not l[0].endswith('.docx') and l[0] != '补录客户.jsonl']  # 补录客户不在 Clients/ 原始行里
    out.append('# Saga Clients · 完整性审计')
    out.append('')
    out.append(f'- 生成：{__import__("datetime").date.today().isoformat()}　脚本：`scripts/saga_clients/audit.py`')
    out.append('')
    out.append('## 1. 原始行 → 客户实体（一行不漏）')
    out.append('')
    out.append(f'- `rows_raw.jsonl` xlsx 行：**{len(xlsx_rows)}**；docx 段落记录：{len(docx_rows)}（其中邮箱不在任何 xlsx 行里的才独立成行）')
    out.append(f'- 已落到实体「来源与归并」里的 xlsx 行：**{sum(1 for l in raw_locs if l in assigned)}**')
    out.append(f'- **未落到任何实体的 xlsx 行：{len(missing)}**' + ('' if not missing else '  ← 有漏，见下表'))
    out.append(f'- 被两个实体同时引用的行：{len(dup_assigned)}；实体引用了不存在的行：{len(ghost)}')
    if missing:
        problems += 1
        out.append('')
        out.append('| 文件 | 表 | 行 | 公司（原值） |')
        out.append('|---|---|---|---|')
        byloc = {loc(r): r for r in xlsx_rows}
        for l in missing[:200]:
            r = byloc[l]
            out.append(f"| {l[0].replace('Clients/', '')} | {l[1]} | {l[2]} | {(r.get('company') or '')[:60]} |")
    if dup_assigned or ghost:
        problems += 1
    # 按文件对账
    out.append('')
    out.append('### 1.1 逐文件对账（抽取行 = 入档行）')
    out.append('')
    out.append('| 文件 | 抽取行 | 入档行 | 差 |')
    out.append('|---|---|---|---|')
    byfile_raw = Counter(l[0] for l in raw_locs)
    byfile_ass = Counter(l[0] for l in raw_locs if l in assigned)
    for f in sorted(byfile_raw):
        d = byfile_raw[f] - byfile_ass[f]
        out.append(f"| {f.replace('Clients/', '')} | {byfile_raw[f]} | {byfile_ass[f]} | {d if d else ''} |")

    # ---------- 2) 实体 → MD ----------
    out.append('')
    out.append('## 2. 客户实体 → MD 档案（一户一档、只在一个等级文件夹）')
    out.append('')
    codes = Counter(e['code'] for e in ents)
    dupcodes = [c for c, n in codes.items() if n > 1]
    md = defaultdict(dict)
    for g in 'ABC':
        for fn, _p in md_files(g):
            m = re.match(r"(S[ABC]-\d+)-", fn)
            if m:
                md[m.group(1)][g] = fn
    ent_by = {e['code']: e for e in ents}
    no_md = [c for c in ent_by if c not in md]
    wrong_dir = [c for c, gs in md.items() if c in ent_by and ent_by[c]['grade'] not in gs]
    multi_dir = [c for c, gs in md.items() if len(gs) > 1]
    orphan = [c for c in md if c not in ent_by]
    byg = Counter(e['grade'] for e in ents)
    out.append(f'- 实体数 **{len(ents)}**：A {byg["A"]} / B {byg["B"]} / C {byg["C"]}；编号重复：{len(dupcodes)}')
    out.append(f'- MD 文件（不含索引）：A {sum(1 for c, gs in md.items() if "A" in gs)} / B {sum(1 for c, gs in md.items() if "B" in gs)} / C {sum(1 for c, gs in md.items() if "C" in gs)}')
    out.append(f'- 无 MD 的实体：{len(no_md)}；MD 在错误文件夹：{len(wrong_dir)}；同一编号出现在多个文件夹：{len(multi_dir)}；无实体的孤儿 MD：{len(orphan)}')
    if dupcodes or no_md or wrong_dir or multi_dir or orphan:
        problems += 1
        for lbl, lst in [('编号重复', dupcodes), ('无 MD', no_md), ('错误文件夹', wrong_dir), ('多文件夹', multi_dir), ('孤儿 MD', orphan)]:
            if lst:
                out.append(f'  - {lbl}：{", ".join(lst[:50])}')

    # ---------- 3) 归并统计 ----------
    out.append('')
    out.append('## 3. 重复客户归并统计')
    out.append('')
    multi = [e for e in ents if len(e['sources']) > 1]
    out.append(f'- 多行合并实体：**{len(multi)}**（合并原始行 {sum(len(e["sources"]) for e in multi)}，消重 {sum(len(e["sources"]) for e in multi) - len(multi)} 行）；明细见 `重复客户归并记录.md`')
    kinds = Counter()
    for e in multi:
        for k in e.get('merge_keys', []):
            kinds[k.split(':')[0]] += 1
    out.append(f'- 归并键分布（多行实体内）：域名 d {kinds["d"]} / 邮箱 e {kinds["e"]} / 电话 p {kinds["p"]} / 公司名+国家 n {kinds["n"]} / 人工 m {kinds["m"]}')
    out.append(f'- 曾用编号（被并掉的编号）合计：{sum(len(e.get("code_aliases") or []) for e in ents)}')

    # ---------- 4) 疑似重复（键没连上） ----------
    cand = []
    seen_pairs = set()

    def add(a, b, why, conf):
        k = tuple(sorted([a['code'], b['code']]))
        if k in seen_pairs:
            return
        seen_pairs.add(k)
        cand.append((conf, a, b, why))

    # 4a 同国 + 规范名高度相似
    by_iso = defaultdict(list)
    for e in ents:
        by_iso[e['iso']].append(e)
    for iso, lst in by_iso.items():
        names = [(nname(e['name']), e) for e in lst]
        names = [(n, e) for n, e in names if len(n) >= 5 and not n.startswith('未具名') and '未具名' not in n]
        # 分桶：首 3 字符
        bucket = defaultdict(list)
        for n, e in names:
            bucket[n[:3]].append((n, e))
        for b, items in bucket.items():
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    n1, e1 = items[i]
                    n2, e2 = items[j]
                    if n1 == n2:
                        add(e1, e2, f'同国同名（规范化后）：{n1}', 'high')
                    elif min(len(n1), len(n2)) >= 6 and SequenceMatcher(None, n1, n2).ratio() >= 0.9:
                        add(e1, e2, f'同国名字相似 ≥0.9：{n1} ~ {n2}', 'mid')
    # 4b 同国 + 域名根相同（acme.com vs acme.co.uk / acme.de）
    root_map = defaultdict(list)
    for e in ents:
        for d in e['domains']:
            root = d.split('.')[0]
            if len(root) >= 5:
                root_map[(e['iso'], root)].append(e)
    for (iso, root), lst in root_map.items():
        uniq = {e['code']: e for e in lst}
        if len(uniq) > 1:
            lst = list(uniq.values())
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    add(lst[i], lst[j], f'同国域名根相同：{root}（{", ".join(lst[i]["domains"][:2])} vs {", ".join(lst[j]["domains"][:2])}）', 'high')
    # 4c 电话后 7 位相同
    ph_map = defaultdict(list)
    for e in ents:
        for p in e['phones']:
            if len(p) >= 9:
                ph_map[p[-7:]].append(e)
    for tail, lst in ph_map.items():
        uniq = {e['code']: e for e in lst}
        if len(uniq) > 1 and len(uniq) <= 4:
            lst = list(uniq.values())
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    add(lst[i], lst[j], f'电话后 7 位相同：…{tail}', 'mid')
    # 4d 同国 + 非通用邮箱本地部分相同
    lp_map = defaultdict(list)
    for e in ents:
        for em in e['emails']:
            lp = em.split('@')[0].lower()
            if lp not in GENERIC_LOCAL and len(lp) >= 5 and not lp.isdigit():
                lp_map[(e['iso'], lp)].append(e)
    for (iso, lp), lst in lp_map.items():
        uniq = {e['code']: e for e in lst}
        if len(uniq) > 1 and len(uniq) <= 3:
            lst = list(uniq.values())
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    add(lst[i], lst[j], f'同国邮箱本地部分相同：{lp}@…', 'low')
    cand.sort(key=lambda x: ({'high': 0, 'mid': 1, 'low': 2}[x[0]], x[1]['code']))
    out.append('')
    out.append('## 4. 疑似重复（归并键没连上，待确认）')
    out.append('')
    cc = Counter(c[0] for c in cand)
    out.append(f'- 候选对：**{len(cand)}**（high {cc["high"]} / mid {cc["mid"]} / low {cc["low"]}）→ 明细 `疑似重复待确认.md`；确认为同一客户的写进 `人工归并.csv`（`编号A,编号B,理由,日期`）后重跑 build.py。')
    out.append('- 不自动合并的原因：同名不同邮箱/域名的两行，可能是同集团不同国家公司、或同名不同企业；合并是不可逆的业务判断，留给人工一键确认。')

    # 写文件
    with open(os.path.join(DATA, '完整性审计.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    L = ['# 疑似重复待确认（归并键没连上的高相似实体对）', '',
         '- 生成：`scripts/saga_clients/audit.py`；确认同一客户 → 在 `data/saga_clients/人工归并.csv` 加一行 `编号A,编号B,理由,日期` → 重跑 `build.py && render.py`（小编号保留，大编号进「曾用编号」）。',
         f'- 候选 {len(cand)} 对：high = 同国同名 / 同国域名根相同；mid = 名字相似 ≥0.9 / 电话后 7 位相同；low = 邮箱本地部分相同。', '',
         '| 置信 | 编号 A | 公司 A | 等级 | 编号 B | 公司 B | 等级 | 国家 | 依据 |', '|---|---|---|---|---|---|---|---|---|']
    for conf, a, b, why in cand:
        L.append(f"| {conf} | {a['code']} | {a['name'][:40]} | {a['grade']} | {b['code']} | {b['name'][:40]} | {b['grade']} | {a['country']}{'' if a['country'] == b['country'] else '/' + b['country']} | {why} |")
    with open(os.path.join(DATA, '疑似重复待确认.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    print(f'rows {len(xlsx_rows)} missing {len(missing)} dup_assigned {len(dup_assigned)} ghost {len(ghost)} | ents {len(ents)} no_md {len(no_md)} wrong_dir {len(wrong_dir)} orphan {len(orphan)} | cand {len(cand)} {dict(cc)}')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
