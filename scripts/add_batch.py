#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_batch.py — 把 batch/*.json 的客户合并进主表 CSV（去重、编号冻结、只追加、合并不覆盖）。

用法：python scripts/add_batch.py [batch/xxx.json ...]   （不带参数 = 处理 batch/ 下全部，按文件名顺序）
规则：
  - 去重键 = 国家 + 规范化公司名（去法律后缀）；命中已有行 → 只填补空字段，不覆盖已有值，并在备注追加批次号。
  - 新客户 → 按 rating 分配编号 PA-/PB-/PC-xxx（各级内递增，取现有最大号 +1；永不复用）。
  - 人工定级、状态、跟进日期等运营列永不被批次覆盖。
"""
import datetime, json, os, re, sys
from common import COLUMNS, read_csv, write_csv, dedup_key, load_batches, BATCH_DIR

MERGE_PHRASE = "首触以 Mikrotik 仓库为准"  # 并档规则短语（与 render.py 判定一致）

PROTECTED = {"人工定级", "状态", "首次触达日", "最后互动日", "下次跟进日", "档案编号", "入库批次", "入库日期"}


def next_code(rows, grade):
    pre = {"A": "PA", "B": "PB", "C": "PC"}[grade]
    mx = 0
    for r in rows:
        m = re.match(rf"^{pre}-(\d+)$", r.get("档案编号", ""))
        if m:
            mx = max(mx, int(m.group(1)))
    return f"{pre}-{mx+1:03d}"


def cust_to_row(c, batch_name, date):
    contacts = c.get("contacts") or []
    entry = c.get("contact") or " / ".join(x for x in [
        "；".join(f"{k.get('name','')}{('（'+k['role']+'）') if k.get('role') else ''} {k.get('email','')} {k.get('phone','')}".strip() for k in contacts)
    ] if x)
    urls = [e.get("url", "") for e in (c.get("evidence") or []) if e.get("url")]
    # W17 双保险：并档户的规则短语只要写在 mikrotik_ref 里，就自动补进「备注」，
    # 使 render.py 的并档判定（备注 ∪ Mikrotik仓库对照编号）不依赖人工在两处重复书写。
    notes = c.get("notes", "") or ""
    mref = c.get("mikrotik_ref", "") or ""
    if MERGE_PHRASE in mref and MERGE_PHRASE not in notes:
        notes = (notes + "｜" if notes else "") + "并档：" + MERGE_PHRASE
    return {
        "公司名": c["name"], "国家": c["country"], "城市": c.get("city", ""), "网站": c.get("website", ""),
        "类型": c.get("type", ""), "信号（在卖什么品牌）": c.get("signal", ""), "是否自有品牌": c.get("own_brand", "否"),
        "切入点": c.get("angle", ""), "首推Saga型号": c.get("p1", ""), "入口/联系方式": entry,
        "优先级": c.get("priority", ""), "状态": "00-未触达", "来源": c.get("source", ""),
        "首次触达日": "", "最后互动日": "", "下次跟进日": "", "备注": notes,
        "评级": c.get("rating", ""), "评级依据": c.get("rating_basis", ""), "档案编号": "",
        "C级细分": c.get("c_sub", ""), "人工定级": "", "PLANET关联证据URL": " ; ".join(dict.fromkeys(urls)),
        "Mikrotik仓库对照编号": c.get("mikrotik_ref", ""), "入库批次": batch_name, "入库日期": date,
    }


def main():
    files = sys.argv[1:]
    batches = load_batches()
    if files:
        want = {os.path.abspath(f) for f in files}
        batches = [(p, b) for p, b in batches if os.path.abspath(p) in want]
    rows = read_csv()
    index = {dedup_key(r["公司名"], r["国家"]): r for r in rows}
    added = merged = 0
    for path, b in batches:
        bname = b.get("batch") or os.path.splitext(os.path.basename(path))[0]
        bdate = b.get("date") or datetime.date.today().isoformat()
        for c in b.get("customers", []):
            if not c.get("rating") in ("A", "B", "C"):
                raise SystemExit(f"[{bname}] {c.get('name')} 缺 rating(A/B/C)")
            key = dedup_key(c["name"], c["country"])
            new = cust_to_row(c, bname, bdate)
            if key in index:
                r = index[key]
                if bname in (r.get("备注") or "") or bname in (r.get("入库批次") or ""):
                    continue  # 已合并过
                for k, v in new.items():
                    if k in PROTECTED or not v:
                        continue
                    if not r.get(k):
                        r[k] = v
                    elif k == "PLANET关联证据URL" and v not in r[k]:
                        r[k] = r[k] + " ; " + v
                r["备注"] = (r.get("备注", "") + f"｜{bname} 再次命中，证据已并入").strip("｜")
                merged += 1
            else:
                new["档案编号"] = next_code(rows, c["rating"])
                rows.append(new)
                index[key] = new
                added += 1
    write_csv(rows)
    print(f"added={added} merged={merged} total={len(rows)}")


if __name__ == "__main__":
    main()
