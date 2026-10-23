#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pricing_hrui.py — 从洪瑞（HRUI）给 Saga 的人民币报价单生成 Realtek 线进价主表与人读版：
  1) data/价格主表_HRUI.csv                         机器可读（ZX 型号 / CNY / 三档 USD / Saga 对应型号 / Saga 列表价 / 隐含加价 / 最近采购价）
  2) docs/reference/价格表_HRUI_三档加价_USD.md     人读版（含报价条款、涨价对照、Saga 列表价隐含加价预警）

输入：
  - 根目录《洪瑞报价-天龙2026930.xls》（Simon 2026-10-23 上传至 main@480b89eb，复制到本分支根目录；4 个表页 / 55 款）
  - data/hrui_STC对照表.csv（Saga Realtek 线 61 款 ↔ HRUI 官网 / ZX 中性码，T25 建、T29-U6 增 ZX 列）
  - data/pi_orders/采购合同明细.csv（PI 包里的洪瑞采购合同 = 实际成交进价）
规则：
  - 洪瑞报价 = 不含税、含运费（到 Saga 指定收货点）、有效期 7 天、半年包换两年保修（报价单备注原文）。
  - 三档 USD = CNY × (1 + 档位) ÷ 汇率，仅作参考——Realtek 线对外价以 Saga Drive 价格表（固定 USD）为准；
    「列表价隐含加价」= Saga 列表价 ÷ (CNY ÷ 汇率) − 1，用来发现已低于 20% 底线的型号。
用法：python scripts/pricing_hrui.py [--rate 6.69] [--rate-date 2026-10-17]
"""
import argparse, csv, datetime, hashlib, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLS = os.path.join(ROOT, "洪瑞报价-天龙2026930.xls")
MAP = os.path.join(ROOT, "data", "hrui_STC对照表.csv")
PO = os.path.join(ROOT, "data", "pi_orders", "采购合同明细.csv")
TIERS = (0.20, 0.25, 0.30)
QUOTE_DATE = "2026-09-30"

# 人工对照（报价单 ZX 码 → Saga 型号列表, 说明）。对照表里已有完全一致 ZX 码的不用写在这里。
MANUAL = {
    "ZX-SWG1050":              (["STC-05GE"],  "待核：对照表记 ZX-SWG0050+/0050-M，报价单为新码 1050（5×GE 桌面）"),
    "ZX-SWG1080":              (["STC-08GE"],  "待核：对照表记 ZX-SWG0080/0080+，报价单为新码 1080；规格栏仍写「5个千兆网口」疑为笔误"),
    "ZX-SWG10160D":            (["STC-016GE"], "对照表记 ZX-SWG10160D-M，报价单无 -M 后缀"),
    "ZX-SWG10240D":            (["STC-024GE-D"], "D = 桌面式（1U 挂耳）"),
    "ZX-SWG10240":             (["STC-024GE-U"], "标准 1U 机架式"),
    "ZX900-AFG-411NS":         (["STC-114GP"], "对照表记 -65 后缀（65W），报价单无后缀、规格同为 65W"),
    "ZX900-AFG-42NS":          (["STC-204GP"], "对照表记 -65 后缀，报价单无后缀、规格同为 65W"),
    "ZX900-AFG-82N":           (["STC-028GP", "STC-208GP"], "待核：对照表把两款 Saga 都对到 902 系列 ZX902-AFG-82N（¥140）；900 系列同配置 ¥170"),
    "ZX900-AFG-1622S-200":     (["STC-2216GP"], "待核：对照表 ZX 列空、官网 HR200-AFG-1622S-200；端口 2GE+2SFP+16PoE 一致，200W"),
    "ZX900-AFG-1622S-300":     (["STC-2216GP"], "同上，300W 档"),
    "ZX900-AFG-2422S-300D":    (["STC-2224GP"], "对照表记 -400；此为 300W 桌面（D）档"),
    "ZX900-AFG-2422S-300":     (["STC-2224GP"], "对照表记 -400；此为 300W 档"),
    "ZX900-AF-1621GS-200":     (["STC-1216GFP"], "待核：对照表为「近似」且 ZX 列空；端口 1SFP+2GE+16×百兆 PoE 一致，200W"),
    "ZX900-AF-1621GS-300":     (["STC-1216GFP"], "同上，300W 档"),
    "ZX-SWTG3C12F":            (["STC-120XGM"], "对照表 ZX 列空、官网 HR-SWTG3C12F 对上"),
    "ZX-AFGM-1622S-300":       (["STC-2216GPM"], "对照表官网名为 HR-AFGM-1622S-300(M)、ZX 列却写 -200；300W 档"),
    "ZX-AFGM-2444S-400":       (["STC-4424GCPM"], "对照表官网名为 HR-AFGM-2444S-400(M)、ZX 列写 -300；400W 档"),
    "ZX-AXGM-SWTG3448S-400":   (["STC-448XGGPM"], "待核：对照表记 -650（650W），报价单为 400W 档"),
}
# 对照表里把 STC-2024GP 对到 ZX900-AFG-242S-300，报价单无 242S；不强配。


def read_quote():
    import xlrd
    wb = xlrd.open_workbook(XLS, formatting_info=False)
    rows, terms = [], {}
    for s in wb.sheets():
        section = ""
        for r in range(s.nrows):
            v = [str(s.cell_value(r, c)).strip() for c in range(s.ncols)]
            if r <= 5:
                t = v[0]
                if t.startswith("联系人员"):
                    terms["contact"] = t
                elif t.startswith("备注说明"):
                    terms["remark"] = t
                elif t.startswith("官网"):
                    terms["tel"] = t
                elif t.startswith("公司地址"):
                    terms["addr"] = t
                elif r == 1:
                    terms["company"] = t
                continue
            if r == 6:
                continue
            model, name, spec, pack, unit, carton, price = v[1], v[2], v[4], v[5], v[6], v[7], v[8]
            if not model and not price:
                if v[0]:
                    section = v[0]
                continue
            if not model:
                continue
            try:
                cny = float(price)
            except ValueError:
                continue
            rows.append(dict(sheet=s.name, section=section, model=model, name=name,
                             spec=re.sub(r"\s+", " ", spec), pack=re.sub(r"\s+", " ", pack),
                             carton=re.sub(r"\s+", " ", carton), cny=cny))
    return rows, terms


def read_map():
    m = []
    with open(MAP, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            zx = [z.strip() for z in r.get("规格书2026-10(ZX型号)", "").split("/") if z.strip()]
            m.append(dict(saga=r["Saga型号"], ports=r["端口解码"], level=r["管理级"],
                          usd=float(r["Saga对外价USD_EXW"] or 0), hr=r["HRUI官网同配置"], zx=zx))
    return m


def read_po():
    po = {}
    with open(PO, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r.get("卖方") != "HRUI" or not r.get("单价RMB") or not r.get("卖方型号"):
                continue
            m = r["卖方型号"].strip()
            po.setdefault(m, []).append((r["订单日期"], float(r["单价RMB"]), r["采购订单编号"], r["数量"]))
    for m in po:
        po[m].sort()
    return po


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rate", type=float, default=6.69)
    ap.add_argument("--rate-date", default="2026-10-17")
    a = ap.parse_args()
    today = datetime.date.today().isoformat()
    sha = hashlib.sha256(open(XLS, "rb").read()).hexdigest()[:16]

    quote, terms = read_quote()
    mp = read_map()
    po = read_po()
    by_zx = {}
    for r in mp:
        for z in r["zx"]:
            by_zx.setdefault(z, []).append(r)
    by_saga = {r["saga"]: r for r in mp}

    hdr = ["ZX型号", "报价单表页", "节", "品名", "规格摘要", "CNY不含税含运费", "USD成本", "USD@+20%", "USD@+25%", "USD@+30%",
           "Saga对应型号", "对应方式", "Saga列表价USD", "列表价隐含加价%", "最近采购价RMB", "采购日期", "采购订单", "较最近采购价%",
           "汇率", "汇率日期", "来源文件"]
    out = []
    n_exact = n_manual = n_none = n_low = 0
    for q in quote:
        m = q["model"]
        sagas, how, note = [], "", ""
        if m in by_zx:
            sagas = [r["saga"] for r in by_zx[m]]
            how = "对照表 ZX 码一致"
            n_exact += 1
        elif m in MANUAL:
            sagas, note = MANUAL[m]
            how = "人工对照：" + note
            n_manual += 1
        else:
            how = "Saga 价格表暂无对应（沿用 ZX 码，不对外写供应商名）"
            n_none += 1
        cost = q["cny"] / a.rate
        usd = [round(q["cny"] * (1 + t) / a.rate, 1) for t in TIERS]
        list_prices = [by_saga[s]["usd"] for s in sagas if s in by_saga and by_saga[s]["usd"]]
        lp = min(list_prices) if list_prices else None
        markup = (lp / cost - 1) * 100 if lp else None
        if markup is not None and markup < 20:
            n_low += 1
        last = po.get(m)
        last_price = last_date = last_po = ""
        delta = ""
        if last:
            d, p, pid, qty = last[-1]
            last_price, last_date, last_po = f"{p:.1f}", d, pid
            delta = f"{(q['cny'] / p - 1) * 100:+.1f}"
        out.append([m, q["sheet"], q["section"], q["name"], q["spec"][:160], f"{q['cny']:.1f}", f"{cost:.1f}",
                    *[f"{u:.1f}" for u in usd], " / ".join(sagas), how,
                    f"{lp:.1f}" if lp else "", f"{markup:+.0f}" if markup is not None else "",
                    last_price, last_date, last_po, delta, f"{a.rate}", a.rate_date,
                    f"洪瑞报价-天龙2026930.xls（{QUOTE_DATE}；sha256 {sha}…）"])

    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    csv_path = os.path.join(ROOT, "data", "价格主表_HRUI.csv")
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        w.writerows(out)

    # ---------- Markdown ----------
    L = []
    L.append(f"# 价格表 · 洪瑞（HRUI，Realtek 线）人民币报价 → 美元成本 / 三档参考 / Saga 列表价隐含加价（生成日 {today}）\n")
    L.append("> 由 `scripts/pricing_hrui.py` 从《洪瑞报价-天龙2026930.xls》+ `data/hrui_STC对照表.csv` + `data/pi_orders/采购合同明细.csv` 自动生成；**不要手改本文件**，改对照请改脚本 `MANUAL` 或对照表后重跑。\n")
    L.append("## 报价单本体\n")
    L.append(f"- **文件**：`洪瑞报价-天龙2026930.xls`（Simon 2026-10-23 上传至 `main@480b89eb`，本分支根目录同件；sha256 `{sha}…`；5.5 MB，含产品图）。报价日期按文件名 = **{QUOTE_DATE}**。")
    L.append(f"- **出具方**：{terms.get('company','深圳洪瑞光祥电子技术有限公司')}；{terms.get('addr','')}；{terms.get('tel','')}。")
    L.append(f"- **对接人**：{terms.get('contact','')}。")
    L.append(f"- **条款（原文）**：{terms.get('remark','')}")
    L.append("- **覆盖**：4 个表页 = 商业级交换机（百兆/千兆非管理、千兆 L2 管理、万兆 L3 管理）、商业级 902 系列 PoE、PoE 供电器、商业级 900 系列 PoE，共 **%d 款**；**不含工业级**（ZX-SWTGW/AFGW…）与 2.5G/10G 非管理新命名机型（HR300S/HR510S…）。" % len(quote))
    L.append(f"- **汇率快照**：1 USD = {a.rate} CNY（{a.rate_date}）。**报价当日须重新核汇率；洪瑞报价有效期仅 7 天、历史上「1 个月能变 4-5 次价格」（微信 2026-07-08），下单前再确认。**")
    L.append(f"- **对照统计**：ZX 码与对照表一致 {n_exact} 款；人工对照（含待核）{n_manual} 款；Saga 价格表暂无对应 {n_none} 款。**按今日汇率 Saga 现行列表价隐含加价 < 20% 的型号 {n_low} 款**（见下节）。\n")

    L.append("## 预警：Saga 现行 Realtek 线列表价（Drive 2026 Q3 版）对新进价的隐含加价\n")
    L.append("> 隐含加价 = Saga 列表价 ÷ (洪瑞 CNY ÷ 汇率) − 1。低于 20% = 已跌破三档底线；为负 = 列表价低于进价。Saga 对 Realtek 线一直是固定美元价目表（非 CNY×档位公式），本表只给事实，调价是 Simon 的决定。\n")
    L.append("| ZX 型号 | Saga 型号 | 洪瑞 CNY | USD 成本 | Saga 列表价 | 隐含加价 | +20% 应为 |")
    L.append("|---|---|---:|---:|---:|---:|---:|")
    flagged = [r for r in out if r[13] and float(r[13]) < 20]
    flagged.sort(key=lambda r: float(r[13]))
    for r in flagged:
        L.append(f"| {r[0]} | {r[10]} | {r[5]} | ${r[6]} | ${r[12]} | **{r[13]}%** | ${r[7]} |")
    ok = [r for r in out if r[13] and float(r[13]) >= 20]
    L.append("")
    L.append(f"仍 ≥ 20% 的有 {len(ok)} 款：" + "；".join(f"{r[0]}→{r[10]}（{r[13]}%）" for r in sorted(ok, key=lambda r: float(r[13]))) + "。其中 +35% 以上的几款（STC-2216GP / STC-2224GP 对 900 系列 1622S / 2422S）属人工对照待核，可能 Saga 列表价对应的是更高配版本。\n")

    L.append("## 涨价对照：报价 vs PI 包里的实际成交进价\n")
    L.append("| ZX 型号 | Saga 型号 | 历次采购（日期 / 单价 RMB / 订单） | 2026-09-30 报价 | 较最近一次 |")
    L.append("|---|---|---|---:|---:|")
    for r in out:
        if r[14]:
            hist = "；".join(f"{d} ¥{p:.0f}（{pid}）" for d, p, pid, qty in po[r[0]])
            L.append(f"| {r[0]} | {r[10]} | {hist} | ¥{r[5]} | **{r[17]}%** |")
    L.append("")
    L.append("PI 包里其余洪瑞成交型号（ZX-SWTG015AS/018AS/1216AS/1224AS/1C8F、ZX-SWTGW2C80N/2216AS/2224AS、ZX-AFGW-SWTG218ANS-100）属 2.5G/10G 与工业线，本报价单未覆盖。\n")

    L.append("## 全表\n")
    L.append("| ZX 型号 | 品名 | 规格摘要 | CNY | USD 成本 | +20% | +25% | +30% | Saga 型号 | Saga 列表价 | 隐含加价 | 对应方式 |")
    L.append("|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|")
    cur = None
    for r in out:
        key = f"{r[1]} › {r[2]}"
        if key != cur:
            cur = key
            L.append(f"| **{cur}** |  |  |  |  |  |  |  |  |  |  |  |")
        L.append(f"| {r[0]} | {r[3]} | {r[4][:60]} | {r[5]} | ${r[6]} | ${r[7]} | ${r[8]} | ${r[9]} | {r[10] or '—'} | {('$' + r[12]) if r[12] else '—'} | {(r[13] + '%') if r[13] else '—'} | {r[11]} |")
    L.append("")
    L.append("## 对照表待回写（`data/hrui_STC对照表.csv` 的 ZX 列与本报价单不一致处）\n")
    for m, (sagas, note) in MANUAL.items():
        if any(q["model"] == m for q in quote):
            L.append(f"- {m} → {' / '.join(sagas)}：{note}")
    L.append("")
    L.append("## Saga Realtek 线 61 款中本报价单未覆盖的型号\n")
    covered = set(s for r in out for s in r[10].split(" / ") if s)
    missing = [r for r in mp if r["saga"] not in covered]
    L.append("、".join(f"{r['saga']}（{r['ports']}，{r['level']}）" for r in missing) + f"（共 {len(missing)} 款：2.5G/10G 非管理、Web 管理 W 系列、工业线、全光款——需洪瑞另出报价）。")
    md_path = os.path.join(ROOT, "docs", "reference", "价格表_HRUI_三档加价_USD.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"quote rows {len(quote)}  exact {n_exact}  manual {n_manual}  none {n_none}  low_markup {n_low}  missing_saga {len(missing)}")
    print("wrote", csv_path, md_path)


if __name__ == "__main__":
    main()
