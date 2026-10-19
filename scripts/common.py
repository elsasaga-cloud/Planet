# -*- coding: utf-8 -*-
"""共用：路径、CSV 列、去重键、价格查询。"""
import csv, glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data", "客户名单_Planet渠道_2026-10.csv")
PRICE_CSV = os.path.join(ROOT, "data", "价格主表.csv")
BATCH_DIR = os.path.join(ROOT, "batch")
PROFILE_DIR = os.path.join(ROOT, "profile")

COLUMNS = ["公司名", "国家", "城市", "网站", "类型", "信号（在卖什么品牌）", "是否自有品牌", "切入点", "首推Saga型号",
           "入口/联系方式", "优先级", "状态", "来源", "首次触达日", "最后互动日", "下次跟进日", "备注", "评级", "评级依据",
           "档案编号", "C级细分", "人工定级", "PLANET关联证据URL", "Mikrotik仓库对照编号", "入库批次", "入库日期"]

LEGAL_SUFFIX = r"\b(gmbh|ag|kg|co\.?|ltd\.?|limited|plc|s\.?r\.?l\.?|s\.?p\.?a\.?|s\.?l\.?|s\.?a\.?|s\.?a\.?s\.?|sarl|sas|b\.?v\.?|n\.?v\.?|aps|a/s|ab|as|oy|oü|sp\.? z o\.?o\.?|sp\.? j\.?|s\.?r\.?o\.?|inc\.?|llc|corp\.?|corporation|company|srl|spa|bvba|eurl|kft|d\.?o\.?o\.?)\b"


def norm_name(name: str) -> str:
    n = name.lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(LEGAL_SUFFIX, " ", n)
    n = re.sub(r"[^a-z0-9\u00c0-\u024f\u4e00-\u9fff]+", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def dedup_key(name: str, country: str) -> str:
    return f"{country.strip()}|{norm_name(name)}"


def read_csv():
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(rows):
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    with open(CSV_PATH, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLUMNS})


def load_batches():
    """按文件名（日期前缀）顺序加载，返回 [(path, json)]。"""
    out = []
    for p in sorted(glob.glob(os.path.join(BATCH_DIR, "*.json"))):
        with open(p, encoding="utf-8") as f:
            out.append((p, json.load(f)))
    return out


def load_prices():
    """返回 {Saga型号(去档位括号): row} 与 {SmartByte型号: row}。"""
    by_saga, by_sb = {}, {}
    if not os.path.exists(PRICE_CSV):
        return by_saga, by_sb
    with open(PRICE_CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            by_sb[r["SmartByte型号"]] = r
            s = r["Saga对应型号"]
            if s and not s.startswith("（"):
                by_saga.setdefault(s, r)
                base = re.sub(r"\(.*?\)$", "", s)
                by_saga.setdefault(base, r)
    return by_saga, by_sb


def price_line(model: str, tier: float, by_saga, by_sb, snap="2026-10-17"):
    """生成 `$xx USD EXW（快照…）` 行；model 可为 Saga 或 SmartByte 型号。"""
    col = {0.20: "USD@+20%", 0.25: "USD@+25%", 0.30: "USD@+30%"}[tier]
    r = by_saga.get(model) or by_sb.get(model)
    if not r:
        return f"（价格表中无 {model}，报价前向 SmartByte 核价）", None
    usd = r[col]
    sb = r["SmartByte型号"]
    saga = r["Saga对应型号"]
    tag = f"{int(tier*100)}% 档"
    note = ""
    if saga.startswith("（"):
        note = f"；Saga 暂无对应型号，沿用 SmartByte 型号 {sb}"
    return f"${usd} USD EXW（{tag}，SmartByte {sb} {r['CNY未税']} CNY × {1+tier:.2f} ÷ {r['汇率']}，汇率快照 {r['汇率日期']}，15 天有效，报价前核价{note}）", r
