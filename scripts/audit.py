#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit.py — 仓库一致性审计。目标 errors: 0。写 docs/audit/全仓审计.md。"""
import datetime, json, os, re, sys
from collections import Counter
from common import read_csv, load_batches, PROFILE_DIR, ROOT, dedup_key, COLUMNS

errors, warns = [], []
rows = read_csv()
codes = [r["档案编号"] for r in rows]
# 1 编号唯一与格式
for c, n in Counter(codes).items():
    if n > 1:
        errors.append(f"编号重复 {c} ×{n}")
for r in rows:
    if not re.match(r"^P[ABC]-\d{3}$", r["档案编号"]):
        errors.append(f"编号格式错误 {r['档案编号']} ({r['公司名']})")
    if r["评级"] not in ("A", "B", "C"):
        errors.append(f"{r['档案编号']} 评级为空/非法")
    if r["评级"] != {"PA": "A", "PB": "B", "PC": "C"}[r["档案编号"][:2]] and not r.get("人工定级"):
        warns.append(f"{r['档案编号']} 评级 {r['评级']} 与编号前缀不一致（允许：升降级不改号）")
    if not r["PLANET关联证据URL"]:
        errors.append(f"{r['档案编号']} 缺 PLANET 关联证据 URL")
    for u in re.split(r"\s*;\s*", r["PLANET关联证据URL"]):
        if u and not re.match(r"^https?://", u):
            errors.append(f"{r['档案编号']} 证据 URL 格式错误: {u}")
    if r["评级"] == "C" and not r["C级细分"]:
        errors.append(f"{r['档案编号']} C 类缺细分")
    if not r["评级依据"]:
        errors.append(f"{r['档案编号']} 缺评级依据")
    if r["评级"] in ("A", "B") and "@" not in r["入口/联系方式"]:
        warns.append(f"{r['档案编号']} {r['评级']} 类但入口无邮箱（B 需邮箱；A 需直达人）")
    if r["国家"] in ("中国", "China"):
        errors.append(f"{r['档案编号']} 中国大陆公司不应入库")
# 2 去重键
keys = Counter(dedup_key(r["公司名"], r["国家"]) for r in rows)
for k, n in keys.items():
    if n > 1:
        errors.append(f"去重键重复 {k} ×{n}")
# 3 CSV ↔ profile 对账
prof = {}
for g in "ABC":
    d = os.path.join(PROFILE_DIR, g)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            m = re.match(r"^(P[ABC]-\d{3})-", fn)
            if m:
                prof.setdefault(m.group(1), []).append(f"{g}/{fn}")
for r in rows:
    if r["状态"].startswith("并入"):
        continue
    c = r["档案编号"]
    if c not in prof:
        errors.append(f"{c} 无档案文件")
    elif len(prof[c]) > 1:
        errors.append(f"{c} 档案文件重复 {prof[c]}")
    else:
        g = (r.get("人工定级") or r["评级"])[:1]
        if not prof[c][0].startswith(g + "/"):
            errors.append(f"{c} 档案目录 {prof[c][0][:1]} 与评级 {g} 不符")
for c in prof:
    if c not in codes:
        errors.append(f"档案 {c} 在 CSV 中不存在")
# 4 批次 JSON 结构
for p, b in load_batches():
    for k in ("batch", "date", "customers", "skipped", "queries"):
        if k not in b:
            errors.append(f"{os.path.basename(p)} 缺字段 {k}")
    for cst in b.get("customers", []):
        if not cst.get("evidence"):
            errors.append(f"{os.path.basename(p)} {cst.get('name')} 无 evidence")
        for e in cst.get("evidence", []):
            if not e.get("url") or not e.get("quote"):
                errors.append(f"{os.path.basename(p)} {cst.get('name')} 证据缺 url/quote")
        for k in cst.get("contacts", []):
            if k.get("email") and k.get("status", "").startswith("猜"):
                errors.append(f"{os.path.basename(p)} {cst.get('name')} 含猜测邮箱 {k['email']}（禁止）")
    for s in b.get("skipped", []):
        if not s.get("reason"):
            errors.append(f"{os.path.basename(p)} skipped {s.get('name')} 无原因")
# 5 汇总
grade = Counter(r["评级"] for r in rows)
country = Counter(r["国家"] for r in rows)
typ = Counter(r["类型"] for r in rows)
md = [f"# 全仓审计（自动生成 {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}）\n",
      f"- 客户总数：{len(rows)}（A {grade.get('A',0)} / B {grade.get('B',0)} / C {grade.get('C',0)}）",
      f"- 国家分布：{', '.join(f'{k} {v}' for k, v in country.most_common())}",
      f"- 类型分布：{', '.join(f'{k} {v}' for k, v in typ.most_common())}",
      f"- **errors: {len(errors)}**　warnings: {len(warns)}\n"]
if errors:
    md.append("## Errors\n" + "\n".join(f"- {e}" for e in errors) + "\n")
if warns:
    md.append("## Warnings\n" + "\n".join(f"- {w}" for w in warns) + "\n")
os.makedirs(os.path.join(ROOT, "docs", "audit"), exist_ok=True)
with open(os.path.join(ROOT, "docs", "audit", "全仓审计.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md))
print("\n".join(md))
sys.exit(1 if errors else 0)
