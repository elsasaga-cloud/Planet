#!/usr/bin/env python3
"""把 data/suppliers_drive/（CENTEC + Realtek 两个 Drive 文件夹的全量入库结果）整理成供应商档案里的资料地图：

  docs/suppliers/Hohunet/05-Drive资料_2026-10.md   ← 「CENTEC Based High-Speed Network」(STH 线)
  docs/suppliers/HRUI/05-Drive资料_2026-10.md      ← 「Realtek Based Commercial Switch」(STC Realtek 线)

每份：文件夹树 + 文档清单（可读正文的 Word/PPT/PDF → 指向 text/*.json）+ 每个型号子文件夹的内容（规格书 / 图片数 / 去重）+
价格表 Must-Know 段落原文。只读 manifest.csv 与 text/*.json，不改任何源数据。
"""
import csv
import json
import os
import re
from collections import OrderedDict, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'data', 'suppliers_drive')
MANIFEST = os.path.join(SRC, 'manifest.csv')
TARGETS = {
    'CENTEC Based High-Speed Network': ('Hohunet', 'Hohunet（CENTEC 方案，STH 线）', 'STH'),
    'Realtek Based Commercial Switch': ('HRUI', 'HRUI（Realtek 方案，STC Realtek 线）', 'STC'),
}


def human(n):
    n = int(n or 0)
    for u in ('B', 'KB', 'MB', 'GB'):
        if n < 1024:
            return f'{n:.0f} {u}' if u == 'B' else f'{n:.1f} {u}'
        n /= 1024
    return f'{n:.1f} TB'


def read_text(r):
    if not r.get('text_file'):
        return ''
    p = os.path.join(SRC, r['text_file'])
    if not os.path.exists(p):
        return ''
    d = json.load(open(p, encoding='utf-8'))
    if isinstance(d, dict):
        return d.get('text') or d.get('content') or ''
    return str(d)


def main():
    rows = list(csv.DictReader(open(MANIFEST, encoding='utf-8-sig')))
    for top, (folder, title, prefix) in TARGETS.items():
        rs = [r for r in rows if r['path'].split('/')[0] == top]
        out = os.path.join(ROOT, 'docs', 'suppliers', folder, '05-Drive资料_2026-10.md')
        tree = defaultdict(list)
        for r in rs:
            parts = r['path'].split('/')
            tree['/'.join(parts[1:-1])].append(r)
        n_ok = sum(1 for r in rs if r['status'] == 'ok')
        n_dup = sum(1 for r in rs if r['status'] == 'dup')
        n_meta = sum(1 for r in rs if r['status'] == 'meta')
        total_bytes = sum(int(r['bytes'] or 0) for r in rs)
        L = []
        L.append(f'# {title} · Drive 文件夹「{top}」全量资料地图（2026-10）\n')
        L.append(f'> 来源：Elsa Drive 文件夹「{top}」，2026-10-22 由 Actions `files/drive` 任务全量入库（PR-02-27 第二轮）。'
                 f'文件 **{len(rs)}** 个 / {human(total_bytes)}；抽到正文 {n_ok}、仅元数据（无字图片等）{n_meta}、与他文件完全重复 {n_dup}。  ')
        L.append('> 正文：`data/suppliers_drive/text/<id>.json`；缩略图：`data/suppliers_drive/thumbs/`；清单：`data/suppliers_drive/manifest.csv`；'
                 '原件备份：GitHub Release `drive-suppliers-20261022`（私有）。**该 Drive 文件夹内容为 2026 Q3 口径，型号事实以官网归档（`02-官网产品清单.md` / `products/`）为准，这里是补充与交叉核对源。**\n')
        # key documents
        docs = [r for r in rs if r['type'] != '图片' and r['status'] == 'ok' and not re.search(r'/' + prefix + r'-[^/]+\.docx$', r['path'])]
        L.append('## 1. 总体性文档（手册 / 价格表 / 功能表 / 平台性能）\n')
        L.append('| 文档 | 类型 | 大小 | 正文字数 | 正文文件 |')
        L.append('|---|---|---|---|---|')
        for r in sorted(docs, key=lambda r: r['path']):
            L.append(f"| {'/'.join(r['path'].split('/')[1:])} | {r['type']} | {human(r['bytes'])} | {int(r['chars'] or 0):,} | `{r['text_file']}` |")
        L.append('')
        # price list must-know
        for r in rs:
            if r['path'].lower().endswith('.pdf') and 'price list' in r['path'].lower() and r['status'] == 'ok':
                t = read_text(r)
                head = t[:1800]
                L.append(f"### 价格表首页原文（{r['path'].split('/')[-1]}，截前 1,800 字）\n")
                L.append('```text')
                L.append(head.strip())
                L.append('```\n')
        # model folders
        L.append('## 2. 型号子文件夹（每个型号 = 规格书 docx + 产品图）\n')
        L.append('| 子文件夹 | 文件数 | 规格书（正文字数） | 图片（有字 / 无字 / 重复） | 备注 |')
        L.append('|---|---|---|---|---|')
        for sub in sorted(tree):
            if not sub:
                continue
            fs = tree[sub]
            specs = [r for r in fs if r['type'] in ('Word', 'PDF', 'PPT') and r['status'] == 'ok']
            imgs = [r for r in fs if r['type'] == '图片']
            ok_i = sum(1 for r in imgs if r['status'] == 'ok')
            meta_i = sum(1 for r in imgs if r['status'] == 'meta')
            dup_i = sum(1 for r in imgs if r['status'] == 'dup')
            spec_s = '、'.join(f"{r['path'].split('/')[-1]}（{int(r['chars'] or 0):,}）" for r in specs) or '—'
            other = [r for r in fs if r not in specs and r not in imgs]
            note = '、'.join(r['path'].split('/')[-1] for r in other) if other else ''
            L.append(f'| {sub} | {len(fs)} | {spec_s} | {ok_i} / {meta_i} / {dup_i} | {note} |')
        L.append('')
        # root files
        roots = tree.get('', [])
        if roots:
            L.append('## 3. 文件夹根目录文件\n')
            L.append('| 文件 | 类型 | 状态 | 大小 | 正文文件 |')
            L.append('|---|---|---|---|---|')
            for r in sorted(roots, key=lambda r: r['path']):
                L.append(f"| {r['path'].split('/')[-1]} | {r['type']} | {r['status']} | {human(r['bytes'])} | {('`' + r['text_file'] + '`') if r.get('text_file') else '—'} |")
            L.append('')
        # how-to
        L.append('## 4. 怎么用\n')
        L.append(f'- 查某型号的规格书全文：`python3 -c "import json;print(json.load(open(\'data/suppliers_drive/text/<id>.json\'))[\'text\'])"`（id 见 `manifest.csv` 同名行）。')
        L.append(f'- 与官网对照：`docs/suppliers/{folder}/products/<型号>.md`（官网为准）；差异写入该型号页的「待补证」。')
        L.append('- 图片只做缩略图（`thumbs/`），OCR 有字的图片正文同样在 `text/`。')
        L.append(f'\n*生成：`scripts/suppliers_crawl/drive_docs.py`；源数据只读；生成日期 2026-10-22。*')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
        print(out, len(rs), 'files;', len(docs), 'docs;', sum(1 for s in tree if s), 'subfolders')


if __name__ == '__main__':
    main()
