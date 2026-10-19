#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pricing.py — 从用户上传的 SmartByte 人民币价格表（xlsx）与 Saga 美元价格表（pdf）生成：
  1) data/价格主表.csv                      机器可读（SmartByte 型号 / CNY / 三档 USD / Saga 对应型号 / Saga 列表价）
  2) docs/reference/价格表_三档加价_USD.md   人读版（含汇率快照、规则、Saga 无对应说明）

规则（用户 2026-10-19，见 docs/rules/报价与型号规则.md）：
  报价 USD = SmartByte 未税 CNY × (1 + 档位) ÷ USD/CNY 汇率，EXW。
  档位：0.20 / 0.25 / 0.30。
依赖：openpyxl、pdfplumber（沙箱 .venv_planet 已装；重置后 pip install openpyxl pdfplumber）。
用法：python scripts/pricing.py [--rate 6.69] [--rate-date 2026-10-17]
"""
import argparse, csv, glob, os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------- SmartByte → Saga 规格对照（人工维护；依据 Saga 三份 PDF 的规格行与 Mikrotik 仓库 2026-09-28 对照表） ----------
# 值：(Saga 型号 或 None, 说明)。None 表示 Saga 暂无对应 → MD 中沿用 SmartByte 型号并显式注明。
SAGA_MAP = {
    # ---- 商用管理型（LT-S8xxx）----
    "LT-S8310G-2GX8GT":      ("STC-28DGGM",          "8×GE + 2×1G/2.5G SFP，L2+；SmartByte 备注：成本回落前暂停出货"),
    "LT-S8310GP-2GX8GT":     ("STC-28DGGPM",         "8×GE PoE + 2×1G/2.5G SFP，L2+；Saga 标 240W 预算，SmartByte 标 120W 电源——报价前核对电源规格"),
    "LT-S8328G-4GX24GT-S":   ("STC-424DGGM",         "24×GE + 4×1G/2.5G SFP，L2+（AC5 爆款）"),
    "LT-S8328GP-4GX24GT-S":  ("STC-424DGGPM-280W",   "24×GE PoE + 4×1G/2.5G SFP，280W，L2+"),
    "LT-S8328GP-4GX24GT":    ("STC-424DGGPM-440W",   "24×GE PoE + 4×1G/2.5G SFP，440W，L2+"),
    "LT-S8328XG-4XS24GT-S":  ("STC-424XGGM",         "24×GE + 4×10G SFP+，L2+ 档（Saga 同型号另有 L3 档 $295）"),
    "LT-S8328XGP-4XS24GT-S": ("STC-424XGGPM-280W",   "24×GE PoE + 4×10G SFP+，280W，L2+（用户 R61 口径：对外 $180/台）"),
    "LT-S8352G-4GX48GT":     ("STC-448DGGM",         "48×GE + 4×1G/2.5G SFP，L2+"),
    "LT-S8352GP-4GX48GT":    ("STC-448DGGPM",        "48×GE PoE + 4×1G/2.5G SFP，440W，L2+"),
    "LT-S8352XG-4XS48GT":    ("STC-448XGGM",         "48×GE + 4×10G SFP+，L2+ 档（Saga 同型号另有 L3 档 $512）"),
    "LT-S8352XGP-4XS48GT":   ("STC-448XGGPM",        "48×GE PoE + 4×10G SFP+，440W，L2+ 档（L3 档 $583）"),
    "LT-S8528XG-4XS24GT":    ("STC-424XGGM(L3)",     "24×GE + 4×10G SFP+，L3；Saga PDF 中 L3 档与 L2+ 档同型号名、不同价"),
    "LT-S8528XGP-4XS24GT":   ("STC-424XGGPM(L3)",    "24×GE PoE + 4×10G SFP+，440W，L3"),
    "LT-IS8528XG-4XS16GT8GC":  ("STC-4816XGCGM",     "16×GE + 8×Combo + 4×10G，L3（SmartByte 备注 AC5 停产，可用原价出 AC3）"),
    "LT-IS8528XGP-4XS16GT8GC": ("STC-4816XGCGPM",    "16×GE PoE + 8×Combo + 4×10G，L3，440W"),
    "LT-S8528XG-4XS16GX8GC": ("STC-4168XGGCM",       "16×1G SFP + 8×Combo + 4×10G，L3"),
    "LT-S8552XG-4XS48GT":    ("STC-448XGGM(L3)",     "48×GE + 4×10G SFP+，L3"),
    "LT-S8552XGP-4XS48GT":   ("STC-448XGGPM(L3)",    "48×GE PoE + 4×10G SFP+，L3，440W"),
    "LT-S8552XG-4XS48GX":    ("STC-448XGGMO",        "48×1G SFP + 4×10G SFP+，L3（全光）"),
    # ---- 工业管理型（LT-IS3xxx L2 / LT-IS6xxx L2+ / LT-IS65xx L3）----
    "LT-IS3206F-2FX4TX":     ("STI-240FM",           "4×FE + 2×100M SFP，L2 管理"),
    "LT-IS3206FP-2FX4TX":    ("STI-244FPM",          "4×FE PoE + 2×100M SFP，L2 管理，120W"),
    "LT-IS3206G-2GX4GT":     ("STI-240GM",           "4×GE + 2×1G SFP，L2 管理"),
    "LT-IS3206GP-2GX4GT":    ("STI-244GPM",          "4×GE PoE + 2×1G SFP，L2 管理，120W"),
    "LT-IS3210G-2GX8GT":     ("STI-280GM",           "8×GE + 2×SFP，L2 管理（SmartByte 标 2.5G SFP，Saga 标 1G SFP——核对）"),
    "LT-IS3210GP-2GX8T":     ("STI-288GPM",          "8×GE PoE + 2×SFP，L2 管理，240W"),
    "LT-IS6306G-2GX4GT":     ("STI-240DGGM",         "4×GE + 2×1G/2.5G SFP，L2+"),
    "LT-IS6306GP-2GX4GT":    ("STI-244DGGPM",        "4×GE PoE + 2×1G/2.5G SFP，L2+，120W"),
    "LT-IS6306GP-2GX4GT-2BT":("STI-244DGGPM-2BT",    "4×GE PoE（2 口 bt）+ 2×2.5G SFP，L2+，240W"),
    "LT-IS6310G-2GX8GT":     ("STI-280DGGM",         "8×GE + 2×1G/2.5G SFP，L2+"),
    "LT-IS6310GP-2GX8GT":    ("STI-288DGGPM",        "8×GE PoE + 2×1G/2.5G SFP，L2+，240W"),
    "LT-IS6310GP-2GX8GT-2BT":("STI-288DGGPM-2BT",    "8×GE PoE（2 口 bt）+ 2×2.5G SFP，L2+，240W"),
    "LT-IS6312G-4GX8GT":     ("STI-480DGGM",         "8×GE + 4×1G/2.5G SFP，L2+"),
    "LT-IS6312GP-4GX8GT":    ("STI-488DGGPM",        "8×GE PoE + 4×1G/2.5G SFP，L2+，240W"),
    "LT-IS6312GP-4GX8GT-2BT":("STI-488DGGPM-2BT",    "8×GE PoE（2 口 bt）+ 4×2.5G SFP，L2+，240W"),
    "LT-IS6316G-8GX8GT":     ("STI-448DGGGM",        "8×GE + 4×1G SFP + 4×2.5G SFP，L2+（SmartByte 备注 AC5 停产可出 AC3）"),
    "LT-IS6316GP-8GX8GT":    ("STI-448DGGGPM",       "8×GE PoE + 4×1G SFP + 4×2.5G SFP，L2+，240W"),
    "LT-IS6318G-2GX16GT":    ("STI-2160DGGM",        "16×GE + 2×1G/2.5G SFP，L2+"),
    "LT-IS6318GP-2GX16GT":   ("STI-21616DGGPM",      "16×GE PoE + 2×1G/2.5G SFP，L2+，240W"),
    "LT-IS6320G-4GX16GT-D":  (None,                  "16×GE + 4×2.5G SFP + DI/DO/RS485：Saga 无 4×2.5G 上联的 16 口型（就近 STI-2160DGGM 为 2×SFP）——沿用 SmartByte 型号并注明"),
    "LT-IS6320GP-4GX16GT-D": (None,                  "16×GE PoE + 4×2.5G SFP + DI/DO：Saga 暂无对应——沿用 SmartByte 型号并注明"),
    "LT-IS6320GP-4GX16GT-D-4BT":(None,               "16×GE PoE（4 口 bt）+ 4×2.5G SFP + DI/DO：Saga 暂无对应——沿用 SmartByte 型号并注明"),
    "LT-IS6228GP-4GX24GT-4BT":("STI-42424DGGPM-4BT", "24×GE PoE（4 口 bt）+ 4×2.5G SFP，L2+，DIN（SmartByte 表内型号疑为 LT-IS6328GP-4GX24GT-4BT 之笔误——报价前核对）"),
    "LT-IS6328GP-4GX24GT-U-2BT":("STI-42424DGGPM-U-2BT","24×GE PoE（2 口 bt）+ 4×2.5G SFP，L2+，1U 机架 370W"),
    "LT-IS6328G-4GX24GT-D":  ("STI-4240DGGM",        "24×GE + 4×1G/2.5G SFP，L2+，DIN"),
    "LT-IS6328GP-4GX24GT":   ("STI-42424DGGPM",      "24×GE PoE + 4×1G/2.5G SFP，L2+，DIN"),
    "LT-IS6328G-4GX24GT-U-D":("STI-4240DGGM-U",      "24×GE + 4×1G/2.5G SFP，L2+，1U 机架 AC"),
    "LT-IS6328GP-4GX24GT-U": ("STI-42424DGGPM-U",    "24×GE PoE + 4×1G/2.5G SFP，L2+，1U 机架，370W"),
    "LT-IS6328G-20GX8GC-D":  ("STI-4168DGGCM-U",     "16×SFP + 8×Combo + 4×2.5G SFP，L2+（Saga 为机架 AC 型，SmartByte 为 -D 型——核对形态）"),
    "LT-IS6312XG-4XS8GT":    ("STI-480XGGM",         "8×GE + 4×10G SFP+，L2+"),
    "LT-IS6312XGP-4XS8GT":   ("STI-488XGGPM",        "8×GE PoE + 4×10G SFP+，L2+，240W"),
    "LT-IS6312XGP-4XS8GT-2BT":(None,                 "8×GE PoE（2 口 bt）+ 4×10G：Saga 无 bt + 4×10G 组合（就近 STI-288DGGPM-2BT 为 2×2.5G 上联）——沿用 SmartByte 型号并注明"),
    "LT-IS6316XG-4XS4GX8GT": ("STI-448XGGGM",        "8×GE + 4×1G SFP + 4×10G SFP+，L2+ 档（L3 档 $363）"),
    "LT-IS6316XGP-4XS4GX8GT":("STI-448XGGGPM",       "8×GE PoE + 4×1G SFP + 4×10G，L2+，240W（L3 档 $385）"),
    "LT-IS6318XG-2XS16GT":   ("STI-2160XGGM",        "16×GE + 2×10G SFP+，L2+ 档（L3 档 $385）"),
    "LT-IS6318XGP-2XS16GT":  ("STI-21616XGGPM",      "16×GE PoE + 2×10G SFP+，L2+，240W（L3 档 $412.5）"),
    "LT-IS6320XG-4XS8GX8GT-D":("STI-488DGGGM",       "8×GE + 8×SFP + 4×上联：Saga STI-488DGGGM 上联为 2.5G 非 10G——10G 上联刚需时沿用 SmartByte 并注明"),
    "LT-IS6328XG-4XS24GT-D": ("STI-4240XGGM",        "24×GE + 4×10G SFP+，L2+ 档（L3 档 $478.5），DIN"),
    "LT-IS6328XGP-4XS24GT":  ("STI-42424XGGPM",      "24×GE PoE + 4×10G SFP+，L2+ 档（L3 档 $517），DIN"),
    "LT-IS6328XGP-4XS24GT-4BT":("STI-42424XGGPM-4BT","24×GE PoE（4 口 bt）+ 4×10G，L2+ 档（L3 档 $550）"),
    "LT-IS6328XG-4XS24GT-U-D":("STI-4240XGGM-U",     "24×GE + 4×10G SFP+，L2+ 档（L3 档 $506），1U 机架"),
    "LT-IS6328XGP-4XS24GT-U":("STI-42424XGGPM-U",    "24×GE PoE + 4×10G SFP+，L2+ 档（L3 档 $550），1U 机架 370W"),
    "LT-IS6328XGP-4XS24GT-U-2BT":("STI-42424XGGPM-U-2BT","24×GE PoE（2 口 bt）+ 4×10G，1U 机架，L2+ 档（L3 档 $583）"),
    "LT-IS6328XG-4XS16GX8GC-D":("STI-4168XGGCM-U",   "16×SFP + 8×Combo + 4×10G，L2+ 档（L3 档 $605）；Saga 为机架型"),
    "LT-IS6516XG-4XS4GX8GT": ("STI-448XGGGM(L3)",    "工业 L3：8×GE + 4×1G SFP + 4×10G"),
    "LT-IS6516XGP-4XS4GX8GT":("STI-448XGGGPM(L3)",   "工业 L3 PoE：8×GE PoE + 4×1G SFP + 4×10G"),
    "LT-IS6518XG-2XS16GT":   ("STI-2160XGGM(L3)",    "工业 L3：16×GE + 2×10G"),
    "LT-IS6518XGP-2XS16GT":  ("STI-21616XGGPM(L3)",  "工业 L3 PoE：16×GE PoE + 2×10G"),
    "LT-IS6520XG-4XS8GX8GT": (None,                  "工业 L3：8×GE + 8×SFP + 4×10G——Saga L3 档无此端口组合，沿用 SmartByte 并注明"),
    "LT-IS6520XG-4XS16GT":   ("STI-4160XGGM",        "工业 L3：16×GE + 4×10G"),
    "LT-IS6520XGP-4XS16GT":  ("STI-41616XGGPM",      "工业 L3 PoE：16×GE PoE + 4×10G"),
    "LT-IS6520XGP-4XS16GT-4BT":("STI-41616XGGPM-4BT","工业 L3 PoE（4 口 bt）：16×GE + 4×10G（Saga 该型为 1U 机架 AC——核对形态）"),
    "LT-IS6528XG-4XS24GT":   ("STI-4240XGGM(L3)",    "工业 L3：24×GE + 4×10G，DIN"),
    "LT-IS6528XGP-4XS24GT":  ("STI-42424XGGPM(L3)",  "工业 L3 PoE：24×GE PoE + 4×10G，DIN"),
    "LT-IS6528XGP-4XS24GT-4BT":("STI-42424XGGPM-4BT(L3)","工业 L3 PoE（4 口 bt）：24×GE + 4×10G"),
    "LT-IS6528XG-4XS24GT-U": ("STI-4240XGGM-U(L3)",  "工业 L3：24×GE + 4×10G，1U 机架"),
    "LT-IS6528XGP-4XS24GT-U":("STI-42424XGGPM-U(L3)","工业 L3 PoE：24×GE PoE + 4×10G，1U 机架"),
    "LT-IS6528XGP-4XS24GT-U-2BT":("STI-42424XGGPM-U-2BT(L3)","工业 L3 PoE（2 口 bt）：24×GE + 4×10G，1U 机架"),
    "LT-IS6528XG-4XS16GT8GC-U":("STI-4816XGCGM-U",   "工业 L3：16×GE + 8×Combo + 4×10G，1U 机架"),
    "LT-IS6528XGP-4XS16GT8GC-U":("STI-4816XGCGPM-U", "工业 L3 PoE：16×GE PoE + 8×Combo + 4×10G，1U 机架"),
    "LT-IS6528XGP-4XS16GT8GC-U-2BT":("STI-4816XGCGPM-U-2BT","工业 L3 PoE（2 口 bt）：16×GE + 8×Combo + 4×10G"),
    "LT-IS6528XG-4XS16GX8GC-U":("STI-4168XGGCM-U(L3)","工业 L3：16×SFP + 8×Combo + 4×10G，1U 机架"),
    "LT-IS6552XG-4XS48GT-U": ("STI-4480XGGM-U",      "工业 L3：48×GE + 4×10G，1U 机架（SmartByte 标已停产——报价前确认）"),
    # ---- 工业非管理型（LT-IS30xx / LT-IS60xx）----
    "LT-IS3005F-1FX4TX":  ("STI-140FE",  "4×FE + 1×100M SFP"),
    "LT-IS3005F-5TX-M":   ("STI-050FE",  "5×FE（Saga 为 DC12-58V；SmartByte -M 为 12-36V——核对）"),
    "LT-IS3005F-5TX-E":   ("STI-050FE",  "5×FE"),
    "LT-IS3006F-2FX4TX":  ("STI-240FE",  "4×FE + 2×100M SFP"),
    "LT-IS3008F-8TX":     ("STI-080FE",  "8×FE"),
    "LT-IS3009F-1FX8TX":  ("STI-180FE",  "8×FE + 1×100M SFP"),
    "LT-IS3005G-5GT-M":   ("STI-050GE",  "5×GE（电压范围核对）"),
    "LT-IS3005G-5GT":     ("STI-050GE",  "5×GE"),
    "LT-IS3005G-1GX4GT":  ("STI-140GE",  "4×GE + 1×1G SFP"),
    "LT-IS3006G-1GT1GX4GT":("STI-150GE", "5×GE + 1×1G SFP"),
    "LT-IS3006G-2GX4GT":  ("STI-240GE",  "4×GE + 2×1G SFP"),
    "LT-IS3008G-8GT":     ("STI-080GE",  "8×GE"),
    "LT-IS3010G-2GX8GT":  ("STI-280GE",  "8×GE + 2×1G SFP"),
    "LT-IS6016G-16GT":    ("STI-0160GE", "16×GE"),
    "LT-IS6018G-2GX16GT": ("STI-2160GE", "16×GE + 2×1G SFP"),
    "LT-IS3005FP-1FX4TX": ("STI-144FP",  "4×FE PoE + 1×100M SFP"),
    "LT-IS3005FP-5TX":    ("STI-054FP",  "4×FE PoE + 1×FE 上联"),
    "LT-IS3006FP-2FX4TX": ("STI-244FP",  "4×FE PoE + 2×100M SFP"),
    "LT-IS3008FP-8TX":    ("STI-088FP",  "8×FE PoE"),
    "LT-IS3009FP-1FX8TX": ("STI-188FP",  "8×FE PoE + 1×100M SFP"),
    "LT-IS3005GP-5GT":    ("STI-054GP",  "4×GE PoE + 1×GE 上联"),
    "LT-IS3005GP-1GX4GT": ("STI-144GP",  "4×GE PoE + 1×1G SFP"),
    "LT-IS3006GP-1GT1GX4GT":("STI-154GP","4×GE PoE + 1×GE + 1×1G SFP"),
    "LT-IS3006GP-2GX4GT": ("STI-244GP",  "4×GE PoE + 2×1G SFP"),
    "LT-IS3008GP-8GT":    ("STI-088GP",  "8×GE PoE"),
    "LT-IS3010GP-2GX8GT": ("STI-288GP",  "8×GE PoE + 2×1G SFP"),
    "LT-IS6012GP-4GX8GT": ("STI-488GP",  "8×GE PoE + 4×1G SFP（Saga PDF 规格行写 2 port Fiber，型号名为 488——报价前核对）"),
    "LT-IS6016GP-16GT":   ("STI-01616GP","16×GE PoE"),
    "LT-IS6018GP-2GX16GT":("STI-21616GP","16×GE PoE + 2×1G SFP"),
    # ---- 工业介质转换器 ----
    "LT-IMC30F-E":        ("STI-110FE",  "1×FE + 1×100M SFP"),
    "LT-IMC30FP-E":       ("STI-111FP",  "1×FE PoE + 1×100M SFP"),
    "LT-IMC30F-1FX2TX-E": ("STI-120FE",  "2×FE + 1×100M SFP"),
    "LT-IMC30FP-1FX2TX-E":("STI-122FP",  "2×FE PoE + 1×100M SFP"),
    "LT-IMC30F-2FX2TX-E": ("STI-220FE",  "2×FE + 2×100M SFP"),
    "LT-IMC30FP-2FX2TX-E":("STI-222FP",  "2×FE PoE + 2×100M SFP"),
    "LT-IMC30G-E":        ("STI-110GE",  "1×GE + 1×1G SFP"),
    "LT-IMC30GP-E":       ("STI-111GP",  "1×GE PoE + 1×1G SFP"),
    "LT-IMC30G-1GX2GT-E": ("STI-120GE",  "2×GE + 1×1G SFP"),
    "LT-IMC30GP-1GX2GT-E":("STI-122GP",  "2×GE PoE + 1×1G SFP"),
    "LT-IMC30G-2GX2GT-E": ("STI-220GE",  "2×GE + 2×1G SFP"),
    "LT-IMC30GP-2GX2GT-E":("STI-222GP",  "2×GE PoE + 2×1G SFP"),
}
# Bypass 系列：Saga 三份 PDF 均无 Bypass 型号 → 全部"无对应"
BYPASS_NOTE = "光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明"

TIERS = (0.20, 0.25, 0.30)


def load_smartbyte():
    import openpyxl
    rows = []
    files = sorted(glob.glob(os.path.join(ROOT, "*.xlsx")))
    for f in files:
        wb = openpyxl.load_workbook(f, data_only=True)
        src = os.path.basename(f)
        for ws in wb.worksheets:
            section = ""
            for r in ws.iter_rows(values_only=True):
                cells = ["" if v is None else str(v).strip() for v in r]
                if not any(cells):
                    continue
                nonempty = [c for c in cells if c]
                # 节标题行：只有一个非空且不像型号
                if len(nonempty) == 1 and not nonempty[0].startswith("LT-"):
                    section = nonempty[0].replace("\n", " ")[:80]
                    continue
                model = next((c for c in cells if c.startswith("LT-")), None)
                if not model:
                    continue
                # 基础价：第一个纯数字单元格
                nums = [c for c in cells if re.fullmatch(r"\d+(\.\d+)?", c)]
                base = float(nums[0]) if nums else None
                desc = ""
                for c in cells:
                    if c and not c.startswith("LT-") and not re.fullmatch(r"\d+(\.\d+)?", c) and len(c) > 20:
                        desc = c.replace("\n", " / ")
                        break
                if base is not None:
                    rows.append(dict(model=model, cny=base, desc=desc[:160], section=section, source=src))
                # 同行 PoE 衍生型号：模式 "LT-xxxP-… | 价格"
                for i, c in enumerate(cells):
                    if c.startswith("LT-") and c != model:
                        # 价格在下一个非空单元
                        nxt = next((x for x in cells[i + 1:] if x), "")
                        m = re.fullmatch(r"\d+(\.\d+)?", nxt)
                        if m:
                            rows.append(dict(model=c, cny=float(nxt), desc="PoE 衍生型（同主型规格 + PoE）", section=section, source=src))
                # 单元格内嵌："LT-…-2BT(…), the unit price is 820 RMB未税" / "LT-…-4BT, 1960"
                for c in cells:
                    for mm in re.finditer(r"(LT-[A-Z0-9\-]+?)(?:\([^)]*\))?[, ]+(?:the unit price is\s*)?(\d{3,5})\s*RMB", c):
                        rows.append(dict(model=mm.group(1), cny=float(mm.group(2)), desc="PoE++ 衍生型（1–2/1–4 口 bt 60–90W）", section=section, source=src))
                    for mm in re.finditer(r"(LT-[A-Z0-9\-]+?-\dBT),\s*(\d{3,5})\s*$", c):
                        rows.append(dict(model=mm.group(1), cny=float(mm.group(2)), desc="PoE++ 衍生型", section=section, source=src))
    # 去重（同型号取首个）
    seen, out = set(), []
    for r in rows:
        if r["model"] in seen:
            continue
        seen.add(r["model"])
        out.append(r)
    return out


def load_saga_list():
    """从 3 份 Saga PDF 抽取 型号 → [(价格, 规格摘要)]（同型号可能 L2+/L3 两档）。"""
    import pdfplumber
    saga = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "Price List_*.pdf"))):
        with pdfplumber.open(f) as pdf:
            for page in pdf.pages:
                for t in page.extract_tables():
                    for row in t:
                        if not row or not row[0]:
                            continue
                        m = str(row[0]).strip()
                        if not re.match(r"^ST[CI]-", m):
                            continue
                        price = None
                        for c in row[1:]:
                            if c and re.search(r"\$\s*\d", str(c)):
                                price = float(re.search(r"\$\s*([\d.]+)", str(c)).group(1))
                        spec = (str(row[1]) if len(row) > 1 and row[1] else "").replace("\n", " ")
                        layer = "L3" if "L3" in spec else ("L2+" if "L2+" in spec else ("L2" if "L2 " in spec else ""))
                        if price is not None:
                            saga.setdefault(m, []).append((price, layer, spec[:90]))
    return saga


def saga_price_for(saga, name):
    """name 形如 'STC-424XGGM' 或 'STC-424XGGM(L3)'。返回 (价格或None, 备注)。"""
    if not name:
        return None, ""
    base, want = name, None
    mm = re.match(r"^(.*?)\((L3|L2\+)\)$", name)
    if mm:
        base, want = mm.group(1), mm.group(2)
    cands = saga.get(base)
    if not cands:
        return None, "Saga PDF 未见该型号（人工核对）"
    if want:
        for p, layer, _ in cands:
            if layer == want:
                return p, want
        return None, f"Saga PDF 无 {want} 档"
    if len(cands) == 1:
        return cands[0][0], cands[0][1]
    # 多档：默认取最低（L2+）
    p, layer, _ = sorted(cands)[0]
    return p, f"{layer}（另有 {'/'.join(l for _, l, _ in sorted(cands)[1:])} 档）"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rate", type=float, default=6.69, help="USD/CNY 汇率快照")
    ap.add_argument("--rate-date", default="2026-10-17", help="汇率快照日期")
    ap.add_argument("--rate-src", default="macrotrends.net / exchange-rates.org（2026-10-17 收盘 6.6912/6.6908）；Bloomberg 2026-10-16 6.6865")
    a = ap.parse_args()
    today = datetime.date.today().isoformat()

    sb = load_smartbyte()
    saga = load_saga_list()

    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "docs", "reference"), exist_ok=True)
    csv_path = os.path.join(ROOT, "data", "价格主表.csv")
    md_path = os.path.join(ROOT, "docs", "reference", "价格表_三档加价_USD.md")

    hdr = ["SmartByte型号", "系列/节", "规格摘要", "CNY未税", f"USD@+20%", f"USD@+25%", f"USD@+30%",
           "Saga对应型号", "Saga列表价USD", "Saga档位/备注", "对照说明", "汇率", "汇率日期", "来源文件"]
    out_rows = []
    n_map = n_nomap = n_over = 0
    for r in sb:
        m = r["model"]
        if m in SAGA_MAP:
            saga_name, note = SAGA_MAP[m]
        elif m.endswith("FBP"):
            saga_name, note = None, BYPASS_NOTE
        else:
            saga_name, note = None, "未在对照表中（人工补）"
        sp, sl = saga_price_for(saga, saga_name) if saga_name else (None, "")
        usd = [round(r["cny"] * (1 + t) / a.rate, 1) for t in TIERS]
        if saga_name:
            n_map += 1
        else:
            n_nomap += 1
        if sp and usd[0] > sp:
            n_over += 1
        out_rows.append([m, r["section"], r["desc"], f"{r['cny']:.0f}", *[f"{u:.1f}" for u in usd],
                         saga_name or "（Saga 暂无对应，沿用 SmartByte 型号）", f"{sp:.1f}" if sp else "", sl, note,
                         f"{a.rate}", a.rate_date, r["source"]])

    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        w.writerows(out_rows)

    # ---------- Markdown ----------
    L = []
    L.append(f"# 价格表 · SmartByte 人民币 → 三档加价 → 美元 EXW（生成日 {today}）\n")
    L.append("> 由 `scripts/pricing.py` 从用户上传的 4 份 SmartByte xlsx 与 3 份 Saga PDF 自动生成；**不要手改本文件**，改规则请改脚本或对照表后重跑。\n")
    L.append("## 规则与快照\n")
    L.append(f"- **公式**：报价 USD = SmartByte 未税 CNY × (1 + 档位) ÷ 汇率；档位 20% / 25% / 30%（用户 2026-10-19）。")
    L.append(f"- **汇率快照**：1 USD = **{a.rate} CNY**（{a.rate_date}；来源：{a.rate_src}）。报价当日须重新核汇率。")
    L.append("- **价格有效期**：SmartByte 管理型两表 2026-09-01 → 2026-12-30；非管理型表 2024-01-11 更新；Bypass 表 2025-03-12。**报价前核价**。")
    L.append("- **条款**：EXW；商用线（STC-）保 1 年、含电源适配器；工业线（STI-）保 3 年、**不含**工业电源与光模块；PoE 均为 af/at（bt 仅 SmartByte -BT 衍生型，Saga 工业线部分型号有 -2BT/-4BT）。")
    L.append("- **档位默认**：分销/走量/比价 → 20%；集成商/项目 → 25%；OEM/ODM 深度定制或小批量技术型 → 30%。档案里写明所选档位与理由。")
    L.append("- **型号书写**：MD/邮件写 Saga 型号；下表「Saga对应型号」为空或标「暂无对应」者，写 SmartByte 型号并注明「Saga 暂无对应型号，沿用 SmartByte 型号」。")
    L.append(f"- **统计**：SmartByte 型号 {len(sb)} 个；有 Saga 对应 {n_map} 个；无对应 {n_nomap} 个；**按今日汇率 +20% 已高于 Saga PDF 列表价的型号 {n_over} 个**（Saga PDF 列表价似按旧汇率/旧成本计算，建议用户刷新 Saga PDF）。\n")
    L.append("## 速查（最常用 P1 候选）\n")
    quick = ["LT-S8310GP-2GX8GT", "LT-S8328GP-4GX24GT-S", "LT-S8328XGP-4XS24GT-S", "LT-S8328XG-4XS24GT-S", "LT-S8328G-4GX24GT-S",
             "LT-IS3010GP-2GX8GT", "LT-IS6310GP-2GX8GT", "LT-IS6312XGP-4XS8GT", "LT-IS6318GP-2GX16GT", "LT-IS6328XGP-4XS24GT"]
    L.append("| SmartByte | Saga 型号 | CNY | +20% | +25% | +30% | Saga PDF 列表价 |")
    L.append("|---|---|---:|---:|---:|---:|---:|")
    idx = {r[0]: r for r in out_rows}
    for q in quick:
        if q in idx:
            r = idx[q]
            L.append(f"| {r[0]} | {r[7]} | {r[3]} | ${r[4]} | ${r[5]} | ${r[6]} | {('$' + r[8]) if r[8] else '—'} |")
    L.append("")
    cur = None
    L.append("## 全表\n")
    L.append("| SmartByte 型号 | 规格摘要 | CNY | +20% | +25% | +30% | Saga 对应型号 | Saga 列表价 | 档位/备注 | 对照说明 |")
    L.append("|---|---|---:|---:|---:|---:|---|---:|---|---|")
    for r in out_rows:
        if r[1] != cur:
            cur = r[1]
            L.append(f"| **{cur or '—'}** |  |  |  |  |  |  |  |  |  |")
        L.append(f"| {r[0]} | {r[2][:70]} | {r[3]} | ${r[4]} | ${r[5]} | ${r[6]} | {r[7]} | {('$' + r[8]) if r[8] else '—'} | {r[9]} | {r[10]} |")
    L.append("")
    L.append("## Saga PDF 原始列表价（USD EXW，抽取自 3 份 PDF，供对照）\n")
    L.append("| Saga 型号 | 档 | 列表价 | 规格摘要 |")
    L.append("|---|---|---:|---|")
    for m in sorted(saga):
        for p, layer, spec in saga[m]:
            L.append(f"| {m} | {layer or '—'} | ${p} | {spec} |")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"smartbyte models: {len(sb)}  saga models: {len(saga)}  mapped: {n_map}  unmapped: {n_nomap}  over_list: {n_over}")
    print("wrote", csv_path, md_path)


if __name__ == "__main__":
    main()
