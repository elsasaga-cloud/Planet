#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 Google Drive《SmartByte》文件夹的分页清单（data/drive_smartbyte_mirror/manifest_pages/pNN.tsv，
由代理经 google_drive.list_files 逐页抄录）汇总成 data/smartbyte_drive_index.json。

每个文件 5 个必填字段（用户 T23 指定）：文件名 / 文件类型 / 文件大小 / 所在子文件夹路径 / 内容摘要（≤50 字）。
另附 _ 前缀辅助字段：Drive id、字节数、摘要来源。

摘要来源三档：
  读取内容   —— 代理用 google_drive.read_file_text 读过正文（节选）的文件，摘要写在 scripts/drive_index_summaries.json
  型号解码   —— 规格书类文件：从 SmartByte / Saga 型号命名规则解码出端口与等级（规则本身来自已读取的 STI-488XGGPM.docx 与多份规格书抽样）
  文件名推断 —— 图片 / 视频 / 设计源文件等不可读内容，按目录与文件名推断

不复制任何原始文件（T23 规则）。
"""
import glob, json, os, re, datetime, sys

ROOT_ID = "1jI4rZhiG16A8ztB2LK-2YYlolxMbPLzQ"
ROOT_NAME = "SmartByte"
PAGES = "data/drive_smartbyte_mirror/manifest_pages/p*.tsv"
OVERRIDES = "scripts/drive_index_summaries.json"
OUT = "data/smartbyte_drive_index.json"

# ---------- 1. 读清单 ----------
items = {}
for f in sorted(glob.glob(PAGES)):
    for ln in open(f, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln:
            continue
        parts = ln.split("\t")
        assert len(parts) == 6, (f, parts[:2])
        i, kind, size, meta, parent, name = parts
        items[i] = dict(kind=kind, size=int(size) if size else 0, meta=meta, parent=parent, name=name)

def path_parts(i):
    chain = []
    cur = i
    while cur != ROOT_ID:
        it = items[cur]
        chain.append(it["name"])
        cur = it["parent"]
    return list(reversed(chain))

# ---------- 2. 类型 ----------
EXT_TYPE = {
    ".png": "图片", ".jpg": "图片", ".jpeg": "图片", ".gif": "图片", ".bmp": "图片", ".webp": "图片",
    ".mp4": "视频", ".mov": "视频", ".avi": "视频",
    ".docx": "Word", ".doc": "Word",
    ".xlsx": "Excel", ".xls": "Excel", ".csv": "Excel",
    ".pptx": "PPT", ".ppt": "PPT",
    ".pdf": "PDF",
    ".pub": "Publisher 排版源文件", ".xmind": "XMind 思维导图", ".rar": "压缩包", ".zip": "压缩包",
    ".cdr": "CorelDRAW 设计稿", ".dxf": "DXF 工程图", ".psd": "Photoshop 源文件", ".txt": "文本",
}

def ftype(name):
    ext = os.path.splitext(name)[1].lower()
    return EXT_TYPE.get(ext, ext.lstrip(".").upper() or "未知")

def human(n):
    if n < 1024:
        return f"{n} B"
    if n < 1024 ** 2:
        return f"{n/1024:.1f} KB"
    if n < 1024 ** 3:
        return f"{n/1024**2:.1f} MB"
    return f"{n/1024**3:.2f} GB"

# ---------- 3. 型号解码 ----------
PORT_TOKENS = [("XGT", "万兆电"), ("XS", "万兆SFP"), ("GX", "千兆SFP"), ("GC", "千兆Combo"), ("GT", "千兆电"),
               ("FX", "百兆光"), ("TX", "百兆电"), ("ST", "2.5G SFP")]
TOKEN_RE = re.compile(r"(\d+)(XGT|XS|GX|GC|GT|FX|TX|ST)")

def decode_lt(model):
    """LT-IS6312GP-4GX8GT-2BT -> 工业6系L2+管理 PoE 4千兆SFP+8千兆电 2口BT"""
    m = re.match(r"LT-(IS|IMC|S|MC|IBPA)(\d)(\d)(\d{2,3})?([A-Z]*)-?(.*)$", model)
    if not m:
        return None
    fam, d1, d2, _, flags, rest = m.groups()
    out = []
    if fam == "IS":
        out.append({"3": "工业3系", "6": "工业6系"}.get(d1, "工业"))
        out.append({"0": "非管理", "2": "L2管理", "3": "L2+管理", "5": "L3管理"}.get(d2, ""))
    elif fam == "S":
        out.append("商业")
        out.append({"2": "L2管理", "3": "L2+管理", "5": "L3管理", "0": "非管理"}.get(d2, ""))
    elif fam == "IMC":
        out.append("工业收发器")
    elif fam == "MC":
        out.append("商业收发器")
    elif fam == "IBPA":
        out.append("PoE 升压器")
    if "P" in flags:
        out.append("PoE")
    ports = [f"{n}{PORT_TOKENS and dict(PORT_TOKENS)[t]}" for n, t in TOKEN_RE.findall(rest.split("-")[0])]
    if ports:
        out.append("+".join(ports))
    suf = rest.split("-")[1:] if "-" in rest else []
    tags = []
    for s in suf:
        if s == "D": tags.append("DI/DO/RS485")
        elif s == "SD": tags.append("温湿度传感器")
        elif s == "BST": tags.append("PoE升压")
        elif s in ("FBP", "2FBP"): tags.append("光口Bypass" + ("×2" if s == "2FBP" else ""))
        elif re.fullmatch(r"\d?BT", s): tags.append(s.replace("BT", "口BT(90W)") if s[0].isdigit() else "BT")
        elif s == "U": tags.append("1U机架")
        elif s == "E": tags.append("E经济版")
        elif s == "S": tags.append("S爆款版")
        elif s.startswith("AC"): tags.append("内置" + s)
        elif s.startswith("2AC"): tags.append("双AC")
        elif s == "SC20": tags.append("SC 20km")
        else: tags.append(s)
    if suf and suf[0].startswith("2AC"):
        tags = ["双AC电源" + suf[0][3:] + "W" if suf[0][3:].isdigit() else "双AC电源"] + tags[1:]
    if tags:
        out.append("/".join(tags))
    return " ".join(x for x in out if x)

SAGA_LETTERS = {"XG": "万兆光", "DG": "2.5G光", "GG": "千兆光+千兆电", "FE": "百兆电", "GE": "千兆电",
                "FP": "百兆PoE", "GP": "千兆PoE", "FM": "百兆管理", "GM": "千兆管理", "FPM": "百兆PoE管理",
                "GPM": "千兆PoE管理", "XGGPM": "万兆光+千兆电PoE管理", "DGGPM": "2.5G光+千兆电PoE管理",
                "XGGM": "万兆光+千兆电管理", "DGGM": "2.5G光+千兆电管理", "XGGCM": "万兆光+千兆Combo管理",
                "DGGCM": "2.5G光+千兆Combo管理", "XGCGPM": "万兆光+Combo+千兆PoE管理", "DGCGPM": "2.5G光+Combo+千兆PoE管理",
                "XGCGM": "万兆光+Combo管理", "DGCGM": "2.5G光+Combo管理", "XGGGPM": "万兆光+千兆电PoE管理(全口)",
                "DGGGPM": "2.5G光+千兆电PoE管理", "XGGGM": "万兆光+千兆电管理", "DGGGM": "2.5G光+千兆电管理",
                "XGE": "万兆收发器", "UMES": "非管理"}

def decode_saga(model):
    """Saga 型号解码。规则来自 STI-488XGGPM.docx：ST=Saga Telecom，I=工业 / C=商业，
    数字 = 光口 / 电口 / PoE 口（工业），商业型号 PoE 口数与电口相同故省略；XG=万兆光，DG=2.5G 光，
    G=千兆，F=百兆，C=Combo，P=PoE，M=管理。"""
    m = re.match(r"ST([ICS])-(\d+)([A-Z]+)(?:-(.*))?$", model)
    if not m:
        return None
    grade, n, letters, suf = m.groups()
    g = {"I": "工业级", "C": "商业级", "S": "特殊"}[grade]
    poe = "P" in letters
    opt = "万兆光" if letters.startswith("X") else ("2.5G光" if letters.startswith("D") else ("百兆光" if letters.startswith("F") else "光"))
    cu = "百兆电" if letters.startswith("F") else "千兆电"
    port = None
    if letters.startswith("UM"):
        port = f"{n}口非管理"
    elif letters[:4] in ("XGGC", "DGGC"):            # 4168: 4 万兆光 + 16 千兆光 + 8 Combo
        port = f"{n[0]}×{opt}+{n[1:-1]}×千兆光+{n[-1]}×Combo"
    elif letters[:4] in ("XGCG", "DGCG"):            # 4816: 4 万兆光 + 8 Combo + 16 电
        port = f"{n[0]}×{opt}+{n[1]}×Combo+{n[2:]}×{cu}" + ("PoE" if poe else "")
    elif letters[:4] in ("XGGG", "DGGG"):            # 448: 4 万兆光 + 4 千兆光 + 8 电
        port = f"{n[0]}×{opt}+{n[1]}×千兆光+{n[2:]}×{cu}" + ("PoE" if poe else "")
    elif grade == "C" and "M" in letters:             # 商业管理型：光 / 电（PoE 口数 = 电口数）
        a, b = (n[0], n[1:]) if len(n) >= 2 else ("0", n)
        port = (f"{a}×{opt}+" if a != "0" else "") + f"{b}×{cu}" + ("PoE" if poe else "")
    else:                                             # 工业：光 / 电 / PoE
        if len(n) == 3:
            a, b, c = n[0], n[1], n[2]
        elif len(n) == 4:
            a, b, c = n[0], n[1:3], n[3]
        elif len(n) == 5:
            a, b, c = n[0], n[1:3], n[3:5]
        else:
            a, b, c = n, "", ""
        port = (f"{a}×{opt}+" if a not in ("0", "") else "") + (f"{b}×{cu}" if b else "") + (f"({c}口PoE)" if c and c != "0" else "")
    s = f"{g}：{port}"
    if "M" in letters.split("E")[0] or letters.endswith("M"):
        s += " 管理型"
    if suf:
        s += " " + suf.replace("2BT", "2口BT").replace("4BT", "4口BT").replace("-U", "-1U").replace("U", "1U", 1) if suf.startswith("U") else " " + suf.replace("2BT", "2口BT").replace("4BT", "4口BT").replace("-U", "-1U")
    return s

# ---------- 4. 规则摘要 ----------
CERT_STD = [("CE-EMC", "CE-EMC"), ("CE-LVD", "CE-LVD"), ("EN 62368-1", "EN 62368-1 LVD"), ("UKCA-EMC", "UKCA-EMC"), ("UKCA -EMC", "UKCA-EMC"),
            ("UKCA-LVD", "UKCA-LVD"), ("UKCA -LVD", "UKCA-LVD"), ("FCC", "FCC"), ("RoHS", "RoHS"), ("REACH", "REACH"), ("EN 55032", "EN 55032")]

def rule_summary(name, parts):
    base, ext = os.path.splitext(name)
    ext = ext.lower()
    pdir = "/".join(parts[:-1])
    up = name.upper()

    # 认证 / 测试报告
    if ("certification" in name.lower() or "certificate" in name.lower() or "test report" in name.lower()
            or "testing report" in name.lower()) and ext == ".pdf":
        kind = "测试报告" if "report" in name.lower() else "认证证书"
        subj = "Saga Telecom 名义" if "Saga Telecom" in name else ("SmartByte 名义" if "SmartByte" in name else "")
        std = next((v for k, v in CERT_STD if k in name), "")
        prod = "收发器" if "Media converter" in name else "以太网交换机"
        return clip(f"{prod}{std}{kind}（{subj}）".replace("（）", "")), "文件名推断"

    # 规格书
    mm = re.search(r"(LT-[A-Z0-9-]+)", base)
    if ("datasheet" in base.lower() or "neutral" in base.lower()) and mm:
        d = decode_lt(mm.group(1)) or mm.group(1)
        if not TOKEN_RE.search(mm.group(1)):
            extra = re.sub(r"(?i)neutral|datasheet|series|--|\.docx", " ", base.replace(mm.group(1), "")).strip()
            d = f"{mm.group(1)} {d}" + (f"（{extra}）" if extra else "")
        return clip(f"SmartByte 中性英文规格书：{d}"), "型号解码"
    ms = re.match(r"(ST[ICS]-[A-Z0-9-]+)", base)
    if ms and ext in (".docx", ".doc"):
        d = decode_saga(ms.group(1)) or ms.group(1)
        return clip(f"Saga 版规格书：{d}"), "型号解码"
    mj = re.match(r"(JW-[A-Z0-9-]+)", base)
    if mj and ext in (".docx", ".doc"):
        return clip(f"进为(JW)低价系列中性规格书：{mj.group(1)}"), "型号解码"

    # 价格表
    if "pricelist" in base.lower() or "price list" in base.lower() or "价格表" in base or "报价" in base:
        tag = "RMB 未税" if ("CNY" in base or "Simon" in base) else ""
        return clip(f"SmartByte 价格表 {tag}：{base}"), "文件名推断"
    if "manual" in base.lower():
        return clip(f"用户手册/操作手册：{base}"), "文件名推断"
    if "QIG" in base or "Quick Installation" in base:
        return clip(f"快速安装指南（中性）：{base}"), "文件名推断"
    if "Feature" in base or "Function List" in base:
        return clip(f"软件功能清单（版本见文件名）：{base}"), "文件名推断"
    if "MIB" in up:
        return clip(f"SNMP MIB 文件/说明：{base}"), "文件名推断"
    if "Packing" in base or "包装" in base:
        return clip(f"包装/装箱信息表：{base}"), "文件名推断"
    if "Catalog" in base:
        return "SmartByte 2025 年产品目录（全系列）", "文件名推断"
    if "DIP" in base:
        return "工业非管理交换机 DIP 拨码定义", "文件名推断"
    if "LED" in base:
        return "工业非管理交换机 LED 指示灯定义", "文件名推断"
    if "Ordering Information" in base:
        return "工业管理型订购信息（型号选配说明）", "文件名推断"

    # 图片 / 视频 / 设计源文件：按目录推断
    ctx = " / ".join([p for p in parts[:-1] if p != ROOT_NAME][-2:])
    if ext in (".png", ".jpg", ".jpeg"):
        if re.match(r"IMG_2022\d{4}_\d{6}", base):
            return clip(f"产品实拍图(2022-05-18)：{ctx}"), "文件名推断"
        if "Mechanical" in base or "结构图" in base or "尺寸图" in base or "dimension" in base.lower():
            return clip(f"机械结构/尺寸图：{ctx}"), "文件名推断"
        if "serial port" in base.lower():
            return clip(f"渲染图({'带' if base.lower().startswith('with') else '无'}串口)：{ctx}"), "文件名推断"
        if base.lower() in ("front", "back", "din-rail", "power supply", "power supply and dip switch", "sc fiber", "sfp fiber",
                            "sfp fiber front", "sfp fiber back", "sc fiber front", "sc fiber back", "sc front", "sfp front", "main"):
            return clip(f"产品渲染图({base})：{ctx}"), "文件名推断"
        if re.fullmatch(r"\d+", base):
            return clip(f"产品图第{base}张：{ctx}"), "文件名推断"
        return clip(f"图片：{base}｜{ctx}"), "文件名推断"
    if ext in (".mp4", ".mov"):
        return clip(f"视频：{base}｜{ctx}"), "文件名推断"
    if ext == ".cdr":
        return clip(f"CorelDRAW 设计稿：{base}"), "文件名推断"
    if ext == ".dxf":
        return clip(f"PCB/机壳 DXF 工程图：{base}"), "文件名推断"
    if ext == ".psd":
        return clip(f"Photoshop 源文件：{base}｜{ctx}"), "文件名推断"
    if ext == ".pub":
        return clip(f"Publisher 排版源文件：{base}"), "文件名推断"
    if ext == ".xmind":
        return clip(f"思维导图：{base}"), "文件名推断"
    if ext == ".pptx":
        return clip(f"演示文稿：{base}"), "文件名推断"
    return clip(f"{base}｜{ctx}"), "文件名推断"

def clip(s, n=50):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"

# ---------- 5. 汇总 ----------
overrides = json.load(open(OVERRIDES, encoding="utf-8")) if os.path.exists(OVERRIDES) else {}
files, folders = [], []
for i, it in items.items():
    parts = path_parts(i)
    if it["kind"] == "D":
        folders.append("/".join([ROOT_NAME] + parts))
        continue
    sub = "/".join([ROOT_NAME] + parts[:-1])
    if i in overrides:
        summ, src = clip(overrides[i]), "读取内容"
    else:
        summ, src = rule_summary(it["name"], [ROOT_NAME] + parts)
    files.append({
        "文件名": it["name"],
        "文件类型": ftype(it["name"]),
        "文件大小": human(it["size"]),
        "所在子文件夹路径": sub,
        "内容摘要": summ,
        "_drive_id": i,
        "_bytes": it["size"],
        "_摘要来源": src,
    })

files.sort(key=lambda r: (r["所在子文件夹路径"], r["文件名"]))
folders.sort()
assert all(len(r["内容摘要"]) <= 50 for r in files)
by_type = {}
for r in files:
    by_type[r["文件类型"]] = by_type.get(r["文件类型"], 0) + 1
by_src = {}
for r in files:
    by_src[r["_摘要来源"]] = by_src.get(r["_摘要来源"], 0) + 1

doc = {
    "meta": {
        "来源": f"Google Drive 文件夹《{ROOT_NAME}》(id {ROOT_ID})，Simon 于 2026-10-20 上传",
        "生成时间UTC": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "生成方式": "google_drive.list_files 逐页抄录（39 页，createdTime 升序）→ scripts/drive_smartbyte_index.py 汇总；未复制任何原始文件",
        "文件总数": len(files),
        "文件夹总数": len(folders),
        "总大小": human(sum(r["_bytes"] for r in files)),
        "总字节": sum(r["_bytes"] for r in files),
        "按类型": dict(sorted(by_type.items(), key=lambda kv: -kv[1])),
        "摘要来源统计": by_src,
        "字段说明": {
            "文件名": "Drive 中的文件名",
            "文件类型": "按扩展名归类：图片/视频/Word/Excel/PDF/PPT 等",
            "文件大小": "人类可读（源字节数见 _bytes）",
            "所在子文件夹路径": "从 SmartByte 根起的完整路径",
            "内容摘要": "≤50 字；_摘要来源 = 读取内容（代理读过正文节选）/ 型号解码（规格书按型号命名规则解码）/ 文件名推断（图片视频等不可读）",
        },
        "注意": "读取内容的文件仅读了开头节选（300–900 字），摘要概括其主题；图片/视频/设计源文件未打开，摘要由目录和文件名推断，可能与实际内容有出入。",
    },
    "文件夹清单": folders,
    "files": files,
}
json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("files", len(files), "folders", len(folders), "bytes", doc["meta"]["总字节"], "by_src", by_src)
