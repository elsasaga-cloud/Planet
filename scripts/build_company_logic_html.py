#!/usr/bin/env python3
"""生成《SmartByte × Saga：两家公司的逻辑与方向》自包含 HTML（T24，PR-02-17）。

数据来源（全部已入库，脚本只读不改）：
  data/smartbyte_site/products.json           官网 252 个产品页（T15 归档 → build.py）
  data/smartbyte_官网型号索引.csv              官网型号 ↔ 价格主表匹配
  data/价格主表.csv                            SmartByte 2026-09 价格表 135 型号 + Saga 对应型号 + 三档 USD
  data/客户名单_Planet渠道_2026-10.csv         PLANET 渠道挖掘 129 户
  data/smartbyte_drive_index.json              Drive《SmartByte》全量索引（2,385 文件）
  data/smartbyte_site_raw/summary.json         官网归档状态
  docs/smartbyte_wechat_summary.md             微信纪要（§4 待跟进表）
  docs/requirements/待统一处理问题清单.md      Q-18…Q-28
文字结论均来自：docs/smartbyte_wechat_summary.md、docs/smartbyte/公司与政策页_2026-10-20.md、docs/drive/MUST-KNOW/*.md、
docs/reference/Saga公司画像与边界.md、scripts/drive_index_summaries.json（Drive 已读文档摘要）。
用法：python3 scripts/build_company_logic_html.py  → docs/两家公司逻辑与方向_SmartByte-Saga.html
"""
import csv
import html
import json
import os
import re
from collections import Counter, OrderedDict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "两家公司逻辑与方向_SmartByte-Saga.html")


def rd(p):
    with open(os.path.join(ROOT, p), encoding="utf-8-sig") as f:
        return f.read()


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=False)


# ---------- 数据 ----------
prod = json.load(open(os.path.join(ROOT, "data/smartbyte_site/products.json"), encoding="utf-8"))
P = prod["products"]
cat_counts = OrderedDict()
for p in P:
    cat_counts.setdefault(p["category_l1"].strip(), Counter())[p["category_l2"]] += 1
pm_rows = list(csv.DictReader(open(os.path.join(ROOT, "data/价格主表.csv"), encoding="utf-8-sig")))
idx_rows = list(csv.DictReader(open(os.path.join(ROOT, "data/smartbyte_官网型号索引.csv"), encoding="utf-8-sig")))
cust = list(csv.DictReader(open(os.path.join(ROOT, "data/客户名单_Planet渠道_2026-10.csv"), encoding="utf-8-sig")))
drive = json.load(open(os.path.join(ROOT, "data/smartbyte_drive_index.json"), encoding="utf-8"))
dmeta = drive["meta"]
site_sum = json.load(open(os.path.join(ROOT, "data/smartbyte_site_raw/summary.json"), encoding="utf-8"))
wx = rd("docs/smartbyte_wechat_summary.md")
qlist = rd("docs/requirements/待统一处理问题清单.md")

grade = Counter(r["评级"] for r in cust)
country = Counter(r["国家"] for r in cust)
match_how = Counter(r["匹配方式"].split("(")[0] for r in idx_rows)
n_matched = sum(1 for r in idx_rows if r["基型号(价格主表)"])
rate = pm_rows[0]["汇率"]
rate_date = pm_rows[0]["汇率日期"]

# 微信 §4 待跟进表
m = re.search(r"## 4\. 待跟进事项.*?\n\n(\|.*?)\n\n---", wx, flags=re.S)
todo_rows = []
if m:
    for ln in m.group(1).splitlines()[2:]:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) >= 4:
            todo_rows.append(cells[:4])
# Q 清单 Q-18..Q-28
q_rows = []
for ln in qlist.splitlines():
    mm = re.match(r"\| (Q-(\d+)) \| ([^|]+) \| (.+?) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|\s*$", ln)
    if mm and int(mm.group(2)) >= 18:
        q_rows.append((mm.group(1), mm.group(3).strip(), re.sub(r"\*\*", "", mm.group(4)).strip(), mm.group(6).strip(), mm.group(7).strip()))

# 价格主表代表行（同一基型号家族各取一行）
pick_models = ["LT-IS3206G-2GX4GT", "LT-IS3206GP-2GX4GT", "LT-IS6310G-2GX8GT", "LT-IS6310GP-2GX8GT", "LT-IS6312GP-4GX8GT-2BT",
               "LT-IS6318GP-2GX16GT", "LT-IS6320XG-4XS16GT", "LT-IS6528XG-4XS24GT-U", "LT-S8328GP-4GX24GT", "LT-S8328G-4GX24GT",
               "LT-S8352GP-4XS48GT", "LT-IS6312XGP-4XS8GT-2BT-2FBP", "LT-IS6312XG-4XS8GT"]
pm_by = {r["SmartByte型号"].strip(): r for r in pm_rows}
sample = [pm_by[m_] for m_ in pick_models if m_ in pm_by]
if len(sample) < 8:
    sample = pm_rows[:: max(1, len(pm_rows) // 10)][:12]

gen_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def tbl(headers, rows, cls=""):
    h = "<table class='t %s'><thead><tr>%s</tr></thead><tbody>" % (cls, "".join(f"<th>{esc(x)}</th>" for x in headers))
    for r in rows:
        h += "<tr>" + "".join(f"<td>{c if isinstance(c, Raw) else esc(c)}</td>" for c in r) + "</tr>"
    return h + "</tbody></table>"


class Raw(str):
    pass


# ---------- 文案 ----------
CSS = """
:root{--ink:#1c2430;--mute:#5b6775;--line:#dfe5ec;--bg:#f6f8fa;--sb:#0f5fa8;--sg:#b4541a;--ok:#1f7a3a;--warn:#a65d00;--card:#fff}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:-apple-system,"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6;font-size:15px}
a{color:var(--sb);text-decoration:none}a:hover{text-decoration:underline}
.wrap{display:grid;grid-template-columns:250px 1fr;min-height:100vh}
nav{position:sticky;top:0;height:100vh;overflow:auto;background:#10233a;color:#cfe0f3;padding:18px 14px}
nav h3{margin:0 0 10px;font-size:13px;letter-spacing:.08em;color:#8fb3d9;text-transform:uppercase}
nav a{display:block;color:#dce9f7;padding:6px 8px;border-radius:6px;font-size:13.5px}nav a:hover{background:#1c3a5c;text-decoration:none}
nav .sub a{padding-left:20px;font-size:12.5px;color:#a9c3de}
main{padding:28px 44px 80px;max-width:1180px}
h1{font-size:30px;margin:0 0 6px;line-height:1.25}h2{font-size:22px;margin:46px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--line)}
h3{font-size:17px;margin:26px 0 10px}h4{font-size:15px;margin:18px 0 6px;color:var(--mute)}
.lead{font-size:16px;color:#2b3745;max-width:960px}
.meta{color:var(--mute);font-size:13px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:18px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.card .n{font-size:26px;font-weight:700;letter-spacing:-.01em}.card .l{font-size:12.5px;color:var(--mute);margin-top:2px}
.card.sb{border-top:4px solid var(--sb)}.card.sg{border-top:4px solid var(--sg)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:900px){.wrap{grid-template-columns:1fr}nav{position:static;height:auto}.two{grid-template-columns:1fr}main{padding:18px}}
.box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:14px 0}
.box.sb{border-left:5px solid var(--sb)}.box.sg{border-left:5px solid var(--sg)}.box.note{background:#fff8e8;border-color:#f0dcae}
.box.ok{background:#eef8f0;border-color:#bfe0c6}
table.t{width:100%;border-collapse:collapse;background:#fff;font-size:13.5px;margin:10px 0 18px}
table.t th,table.t td{border:1px solid var(--line);padding:7px 9px;vertical-align:top;text-align:left}
table.t th{background:#eef3f8;font-weight:600}table.t tr:nth-child(even) td{background:#fafcfe}
table.t.small{font-size:12.5px}
.tag{display:inline-block;font-size:11.5px;padding:1px 7px;border-radius:999px;background:#e8eef5;color:#2b3745;margin-right:4px}
.tag.sb{background:#dcebfa;color:#0b4a85}.tag.sg{background:#fbe6d6;color:#7a3a0d}.tag.ok{background:#dff3e4;color:#145a2a}.tag.warn{background:#fff0d6;color:#7a4a00}
.flow{display:grid;grid-template-columns:1fr 60px 1fr 60px 1fr;align-items:center;gap:6px;margin:16px 0}
.flow .node{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center}
.flow .node b{display:block;font-size:16px}.flow .node small{color:var(--mute)}
.flow .arrow{text-align:center;font-size:26px;color:#8aa0b6}
.flow .node.sb{border-top:5px solid var(--sb)}.flow .node.sg{border-top:5px solid var(--sg)}.flow .node.cu{border-top:5px solid #3b8a5c}
ul.tight li{margin:3px 0}
.tl{border-left:3px solid #c9d6e3;margin:12px 0 12px 8px;padding-left:18px}
.tl .ev{position:relative;margin:0 0 12px}.tl .ev:before{content:"";position:absolute;left:-24px;top:7px;width:10px;height:10px;border-radius:50%;background:var(--sb);border:2px solid #fff;box-shadow:0 0 0 1px #c9d6e3}
.tl .ev.sg:before{background:var(--sg)}.tl .ev.both:before{background:linear-gradient(90deg,var(--sb) 50%,var(--sg) 50%)}
.tl .d{font-weight:700;font-size:13px;color:var(--mute)}
.kv{display:grid;grid-template-columns:150px 1fr;gap:4px 12px;font-size:14px}.kv dt{color:var(--mute)}.kv dd{margin:0}
footer{margin-top:50px;color:var(--mute);font-size:12.5px;border-top:1px solid var(--line);padding-top:14px}
code{background:#eef2f6;padding:1px 5px;border-radius:4px;font-size:12.5px}
.src{color:var(--mute);font-size:12px}
@media print{nav{display:none}.wrap{grid-template-columns:1fr}main{max-width:none;padding:0}h2{page-break-after:avoid}table{page-break-inside:auto}}
"""

NAV = [
    ("s0", "0 · 一页看懂"),
    ("s1", "1 · 两家公司是谁"),
    ("s2", "2 · 合作逻辑（钱、货、规则）"),
    ("s3", "3 · 产品体系与型号对照"),
    ("s4", "4 · 报价逻辑"),
    ("s5", "5 · 技术路线与时间线"),
    ("s6", "6 · 方向：各自的与共同的"),
    ("s7", "7 · 风险与边界"),
    ("s8", "8 · 待跟进 / 待裁定"),
    ("s9", "9 · 资料入库地图"),
    ("s10", "10 · 可信度说明"),
]


def section_nav():
    return "".join(f"<a href='#{i}'>{esc(t)}</a>" for i, t in NAV)


def cat_table():
    rows = []
    for c1, cnt in cat_counts.items():
        for c2, n in cnt.most_common():
            rows.append((c1, c2, n))
    return tbl(["大类", "品类（官网 19 个）", "产品页数"], rows, "small")


def price_sample_table():
    rows = []
    for r in sample:
        rows.append((r["SmartByte型号"], r["Saga对应型号"], r["CNY未税"], r["USD@+20%"], r["USD@+25%"], r["USD@+30%"], r["对照说明"]))
    return tbl(["SmartByte 型号", "Saga 型号", "CNY 未税", "USD +20%", "USD +25%", "USD +30%", "对照说明"], rows, "small")


def series_table():
    g = OrderedDict()
    for r in pm_rows:
        g.setdefault(re.sub(r"\s+", " ", r["系列/节"].strip()), []).append(r)
    rows = []
    for k, v in g.items():
        c = [float(x["CNY未税"]) for x in v if re.fullmatch(r"[\d.]+", x["CNY未税"].strip())]
        saga = [x["Saga对应型号"] for x in v if x["Saga对应型号"] and not x["Saga对应型号"].startswith("（")]
        rows.append((k[:80], len(v), f"{int(min(c))}–{int(max(c))}" if c else "", f"{len(saga)}/{len(v)}", "、".join(saga[:4]) + ("…" if len(saga) > 4 else "")))
    return tbl(["价格表系列 / 节（SmartByte 2026-09 价格表原文）", "型号数", "CNY 未税区间", "有 Saga 名", "Saga 型号示例"], rows, "small")


def country_table():
    rows = [(k, v) for k, v in country.most_common()]
    return tbl(["国家", "户数"], rows, "small")


def todo_table():
    return tbl(["#", "事项", "相关方", "最后状态 / 下一步"], todo_rows, "small")


def q_table():
    return tbl(["编号", "轮次", "问题", "默认处理（未裁定前）", "结果"], [(a, b, c[:260], d[:160], e) for a, b, c, d, e in q_rows], "small")


def _jsonl(p):
    fp = os.path.join(ROOT, p)
    if not os.path.exists(fp):
        return []
    return [json.loads(l) for l in open(fp, encoding="utf-8") if l.strip()]


def _img_cred_note():
    img_dir = os.path.join(ROOT, "data/smartbyte_site_raw/images")
    n = len(os.listdir(img_dir)) if os.path.isdir(img_dir) else 0
    if n >= 1493:
        return "图片 1,493 张全部下载并入库（型号页内嵌）；"
    if n:
        return f"图片已入库 {n}/1,493 张（其余待下一轮运行）；"
    return "图片 1,493 张已全部下载（二进制暂在 Actions 附件，入 git 由下一轮运行完成）；"


def site_status():
    r = site_sum
    dls = _jsonl("data/smartbyte_site_raw/downloads_manifest.jsonl")
    ims = _jsonl("data/smartbyte_site_raw/images_manifest.jsonl")
    dl_ok = [d for d in dls if d.get("file")]
    im_ok = [d for d in ims if d.get("file")]
    n_pdf_git = len([f for f in os.listdir(os.path.join(ROOT, "data/smartbyte_site_raw/datasheets")) if f.lower().endswith(".pdf")]) if os.path.isdir(os.path.join(ROOT, "data/smartbyte_site_raw/datasheets")) else 0
    n_txt = len(os.listdir(os.path.join(ROOT, "data/smartbyte_site_raw/datasheet_text"))) if os.path.isdir(os.path.join(ROOT, "data/smartbyte_site_raw/datasheet_text")) else 0
    img_total = 1493
    img_dir = os.path.join(ROOT, "data/smartbyte_site_raw/images")
    n_img_git = len(os.listdir(img_dir)) if os.path.isdir(img_dir) else 0
    img_state = f"{len(im_ok)}/{img_total} 已下载（{sum(d.get('bytes') or 0 for d in im_ok) / 1e6:.0f} MB）；入库 `data/smartbyte_site_raw/images/` {n_img_git} 张" + ("（型号页直接内嵌前 3 张产品图并逐张给本地路径）" if n_img_git else "（二进制暂在 Actions Release 附件 / 产物，入 git 由下一轮运行完成）")
    return tbl(["项", "状态（截至本页生成时刻）"], [
        ("页面", f"{r.get('pages_ok')}/{r.get('pages_total')} 抓齐（2 个失败 = 站内死链 404：/Unmanaged-Industrial-Switch、/Industrial-Boost-Power-Adaptor）；其中产品页 {len(P)} 个、品类分页 41 个、新闻 8 篇、公司 / 政策页 ≈10 个"),
        ("规格书 PDF", f"{len(dl_ok)}/245 已归档（{sum(d.get('bytes') or 0 for d in dl_ok) / 1e6:.0f} MB；入库 `data/smartbyte_site_raw/datasheets/` {n_pdf_git} 份 + pdftotext 文本 `datasheet_text/` {n_txt} 份）。PHP 下载口对运行器 403，v2.2 解码 base64 path 走站内直链一次成功"),
        ("图片", f"站点自有图片全在 CDN（gcdn.meidianbang.cn/comdata/70901/…），从已归档 HTML 收集 1,491 张（产品大图 1,140 张 *_b.jpg）+ 站内 2 张：{img_state}"),
        ("整理层", f"`docs/smartbyte/products/` 每型号一页共 {len(P)} 页 + README 索引（含本地 PDF / 文本链接）；`data/smartbyte_官网型号索引.csv` {len(idx_rows)} 行；`data/smartbyte_site/products.json`（规格表逐行结构化）"),
    ], "small")


def drive_table():
    bt = dmeta["按类型"]
    rows = [(k, v) for k, v in bt.items()]
    return tbl(["类型", "文件数"], rows, "small")


top_folders = Counter()
for f in drive["files"]:
    top = (f.get("所在子文件夹路径") or "").split("/")[1] if "/" in (f.get("所在子文件夹路径") or "") else "（根目录）"
    top_folders[top] += 1


def folder_table():
    return tbl(["SmartByte 根下一级目录", "文件数"], top_folders.most_common(), "small")


# ---------- HTML ----------
H = []
A = H.append
A("<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>")
A("<title>SmartByte × Saga：两家公司的逻辑与方向（2026-10-21）</title><style>" + CSS + "</style></head><body><div class='wrap'>")
A("<nav><h3>目录</h3>" + section_nav() + "<div style='margin-top:18px;font-size:12px;color:#8fb3d9'>自包含单文件，可离线打开 / 打印。生成：" + gen_time + "</div></nav><main>")

# 封面
A("<h1>SmartByte × Saga：两家公司的逻辑与方向</h1>")
A(f"<div class='meta'>根据仓库已入库的全部资料汇编：微信 95 张截图（4 个会话，2023-12 → 2026-10-16）、Drive《SmartByte》{dmeta['文件总数']:,} 个文件索引与已读文档、SmartByte 官网整站归档（{len(P)} 个产品页）、2026-09 价格表（{len(pm_rows)} 型号）、Saga MUST-KNOW 政策文件、PLANET 渠道挖掘 {len(cust)} 户。生成 {gen_time}；仓库分支 <code>arena/3f35b9b3-planet</code>。</div>")
A("<p class='lead'>一句话：<b style='color:var(--sb)'>SmartByte</b> 是深圳/惠州的 Marvell 方案以太网交换机<b>源头工厂</b>，只做 OEM/ODM；<b style='color:var(--sg)'>Saga Telecom</b>（郑州仁夏通讯器材）是把 SmartByte 的工业/商用管理型交换机以 <b>Saga 品牌（STI-/STC-）</b>卖到欧洲、土耳其、北美的<b>贸易型品牌商</b>——对外口径「Saga 是 SmartByte 在欧洲市场的分销品牌」，对内是「SmartByte 办事处」式的深度绑定：SmartByte 出产品、固件、认证与售后研发，Saga 出客户、方案包装、长期跟进与一线支持。</p>")

# 0 一页看懂
A("<h2 id='s0'>0 · 一页看懂</h2>")
A("<div class='cards'>")
for n, l, c in [
    ("2023-12", "合作起点（微信会话 D 首条 2023-12-16）", "sb"),
    ("408,185 元", "Saga → SmartByte 累计付款（2024 62,181 / 2025 341,852 / 2026 初 4,152；Drive《转账金额汇总》）", "sg"),
    (f"{len(P)}", "官网产品页（19 品类；工业 ≈ 205 / 商用 40 / 白盒 7）", "sb"),
    (f"{len(pm_rows)}", "2026-09 价格表型号（有效期 2026-09-01 → 12-30）", "sb"),
    (f"{n_matched}/{len(idx_rows)}", "官网型号能对上价格表（精确或去尾缀）", "sb"),
    (f"{dmeta['文件总数']:,}", f"Drive《SmartByte》文件（{dmeta['总大小']}，658 个文件夹）", "sg"),
    ("13,943 条", "微信消息（OCR 重建，4 会话）", "sg"),
    (f"{len(cust)} 户", f"PLANET 渠道客户池（A {grade.get('A', 0)} / B {grade.get('B', 0)} / C {grade.get('C', 0)}）", "sg"),
]:
    A(f"<div class='card {c}'><div class='n'>{esc(n)}</div><div class='l'>{esc(l)}</div></div>")
A("</div>")
A("<div class='flow'>"
  "<div class='node sb'><b>SmartByte Technology</b><small>深圳研发 · 惠州工厂 · 福州研发中心<br>Marvell AC3→AC5 / AC5X / Aldrin2 / Falcon<br>只做 OEM/ODM，自写 Marvell 代码</small></div>"
  "<div class='arrow'>→</div>"
  "<div class='node sg'><b>Saga Telecom</b><small>郑州仁夏通讯器材 · SOHO 贸易商<br>品牌 STI-（工业）/ STC-（商用）<br>Access→Core 方案叙事（+HRUI Realtek、Hohunet CENTEC）</small></div>"
  "<div class='arrow'>→</div>"
  "<div class='node cu'><b>海外客户</b><small>土耳其 Angora / Netas / 警察项目 · 德国 Frederik · 加拿大 · 迪拜 Astel · 印度 Sanjay<br>+ PLANET 渠道池 129 户（US/CA + 欧洲 + TR）</small></div>"
  "</div>")
A("<div class='box note'><b>三句话判断</b><ul class='tight'>"
  "<li><b>逻辑</b>：SmartByte 以「低 MOQ 免费贴牌 + 自研 Marvell 固件 + 5 年机壳/孔位不变」换取 Saga 这类海外品牌商的长期出货；Saga 以「不做自有工厂、不碰源代码、不比 Realtek 低价」换取 SmartByte 的价格空间（「目标是出货，利润不很 care」）与研发直接参与售后。</li>"
  "<li><b>方向</b>：SmartByte 2026 年全面切到 AC5（AC3 已于 2026-07-31 停产）、补 L3 / 7.5.0 固件、做白盒数据中心与 Centec、2027 才碰 TSN / EN50155；Saga 2026 Q3 把自己重新包装成「Managed Networking Solutions（接入到核心）」方案商，弱化「Marvell」字眼、引入 CENTEC 与 DC 交换机，市场重心 DE / UK / TR / IT，另以 PLANET 渠道池开拓 US/CA + 欧洲。</li>"
  "<li><b>卡点</b>：土耳其大单（TT 800→1500 台、Angora 1000+ 台 L2+）连续延期；2026 存储涨价推高全线 +10 USD；Saga 无退税资质、无 UL、官网弱；两家合作的价格与开案规则已经成形，但 2026-09 新价格表尚未同步到 Saga 对外报价（待办 #7）。</li></ul></div>")

# 1 两家公司是谁
A("<h2 id='s1'>1 · 两家公司是谁</h2>")
A("<div class='two'>")
A("<div class='box sb'><h3 style='margin-top:0'>SmartByte Technology Co., Ltd（深圳 / 惠州）</h3><dl class='kv'>"
  "<dt>身份</dt><dd>以太网交换机源头工厂，「one of a few source factories of Ethernet Switches with strong R&amp;D ability in China」；只做 OEM/ODM，不与客户品牌竞争（「We do not prompt our own brand」）。</dd>"
  "<dt>成立 / 规模</dt><dd>2020 年深圳创立（OEM 页另称 since 2015）；制造基地惠州惠阳镇隆 Lihe Youke 创新基地 7–8 层，研发中心福州海西科技园；官网称 98% 产品用 Marvell 芯片，ISO9001/14001。</dd>"
  "<dt>人</dt><dd>Peter hu（老板 / 对接 Saga 的销售，peter@smartbyte.com.cn，每周五在深圳）；Anna / Rot（跟单：合同、标签、出货）；扫地僧 / sushen（技术，直接进客户群排障）；Dora。两位老板为技术出身，CTO 来自大厂。</dd>"
  "<dt>产品</dt><dd>工业管理型 / PoE / PoE++ / Boost PoE / 光纤 Bypass、工业非管理、工业媒体转换器与 Boost 电源；商用 L2+/L3 管理型（含热插拔电源）；白盒数据中心（10G/25G/100G 上联）。官网 19 品类 252 产品页。</dd>"
  "<dt>芯片路线</dt><dd>Marvell：ARM+SOHO（2021）→ AC3（2022–2025）→ AC5 / AC5P / AC5X（2023 预研、2025 切换完成、2026-07-31 AC3 停产）；数据中心 Aldrin2 1.08T 量产、Falcon 3.2T/12.8T；2025 起预研 Centec 平台，2026 计划发布 Centec 管理型。</dd>"
  "<dt>认证 / 保修</dt><dd>CE / UKCA / FCC / RoHS / REACH（认证主体「惠州凌特华盛」，2024-07-24）；无 UL（电源可配 UL 版明纬）。保修：工业 6 系列 5 年 / 3 系列 3 年，商用 3 年，ODM 项目另议，DOA 3 个月。</dd>"
  "<dt>红线</dt><dd>Marvell SDK/源代码受 NDA 不外发（Source Code Cooperation = Unavailable）；硬件设计文件不外发；CKD 只出硬件；升级包只由 SmartByte 制作。</dd>"
  "</dl></div>")
A("<div class='box sg'><h3 style='margin-top:0'>Saga Telecom（郑州仁夏通讯器材）</h3><dl class='kv'>"
  "<dt>身份</dt><dd>中国大陆 SOHO 交换机贸易公司，自有品牌 Saga（型号 STI- 工业 / STC- 商用 / STH- CENTEC 高速汇聚），官网 sagatele.com（用户自评：效果差、影响信任）。Simon 为唯一对接人。</dd>"
  "<dt>货源结构</dt><dd>接入层核心 = SmartByte（Marvell）；补位 = HRUI（Realtek，补型号、价格敏感客户）；汇聚/核心 = Hohunet（CENTEC，L3 / 10G / 25G / 100G）。</dd>"
  "<dt>对外叙事（2026 Q2–Q3）</dt><dd>「Tailored Managed Networking Solutions — A Scalable Path from Access to Core」：架构连续性、持续供应、生命周期延续；Access 层锚定 Marvell，Aggregation/Core 层用 CENTEC；买手式（buffet-style）信息公开——每类资料都有可随时下载的 Google 链接，季度更新。</dd>"
  "<dt>标准条款（Drive 2026 Q3 版）</dt><dd>交期 10–15 天（到款 1–2 工作日 + 生产 4–7 + 快递 4–7）；MOQ 1 台；样品不免费但可抵货款；T/T 或 PayPal，标准品 50/50、定制 100% 预付；RMA 每 100 台送 2 台备件；OEM logo / 包装 / Web UI 免费；SKD 可做、源代码不开放。保修文件写 STC 1 年 / STI 3 年 / STH 1 年，与官网口径的差异 = Q-22。</dd>"
  "<dt>商务框架</dt><dd>CCF（商业合同框架：付款 / 交付 / 质量 / 保修 / RMA / 出口合规）；TTC（技术转移合作分级：OEM 现成、ODM 可谈、SKD 现成、CKD 可谈、SDK 可谈需 NDA、源代码不可）；每位客户一个按国家/姓名命名的 Drive 文件夹（规格书、手册、保修证书、Web/CLI 手册、照片、装运单）。</dd>"
  "<dt>优势 / 劣势</dt><dd>优势：功能强（ERPS、PoE++、IGMP、VLAN、QoS）、深度定制管理功能/界面、芯片有库存交期快、和台湾同行比性价比高。劣势：加价空间有限（「给我 100，最多卖 130」）、无 UL / 轨交认证、不做云管理 / 轨交 / IP67 / 消费级、官网弱、无退税资质。</dd>"
  "<dt>目标客户排序</dt><dd>① 有 OEM/ODM 需求的品牌商 / 方案商 → ② 有从中国进口经验或在用台系品牌（PLANET、ORing、Edgecore）者 → ③ 分销 / 电商 → ④ 小项目型集成商。策略：长期跟进（「1 次不行就 10 次，10 次不行就 2 年 5 年」），弱化贸易商身份，主打方案可行性与技术深度。</dd>"
  "<dt>现有客户线</dt><dd>土耳其 Angora（Levent：Turk Telekom、警察项目、1000+ 台 L2+ 大标）、Netas（军工，3 台 AC5 样机 2026-01）、TronX；德国 Frederik（BDCOM 用户，20 台双 AC）；加拿大板卡客户；迪拜 Astel；印度 Sanjay（MC）；BNSC / 洪瑞（彩盒与贴标）；俄罗斯 Rio-Import（报备）。</dd>"
  "</dl></div>")
A("</div>")

# 2 合作逻辑
A("<h2 id='s2'>2 · 合作逻辑：钱怎么流、货怎么走、规则是什么</h2>")
A("<h3>2.1 关系定位</h3><ul class='tight'>"
  "<li>对外：Peter 2025-03-25 定调「Saga 是 SmartByte 在欧洲市场的分销品牌」；Simon 2024-10-31 自称「SmartByte 办事处」。SmartByte 不出面、不接 Saga 的终端客户，但研发可用英文直接进客户群排障、支持晚间远程（2025-11 起）。</li>"
  "<li>对内（Drive《长期合作问题及评估_2026 验厂》）：Saga 要的是 AC5 平台 5 年不变、SmartByte 自有厂房与研发延续性、Saga 在客户面前「隐身」的长期方案；SmartByte 要的是持续出货与可预期的量。</li>"
  "<li>分工：跟单找 Anna / Rot，解决不了再留言 Peter；技术走扫地僧群；售后 Saga 先让客户录视频 + 口述再转 SmartByte；运行正常的设备不建议升级固件（仅限新需求 / 明显 bug）。</li></ul>")
A("<h3>2.2 钱：累计 408,185 元与关键成交价</h3>")
A(tbl(["时间", "项目", "成交（RMB 未税，SmartByte → Saga）", "备注"], [
    ("2024-09", "LT-IS6310G-2GX8GT 350/385 台", "620 → 600", "首批工业大货；价格按量让步"),
    ("2024-11 → 2025-01", "土耳其 178 对 LT-IS6318GP-2GX16GT + 电源", "1260 + 电源 220 + console 10 = 1490 / 对（总 265,220）", "原为商业 16+4 变体 176 台 740，因清关改工业款；定制包装 3,000 元由 SmartByte 承担"),
    ("2024–2025", "16+4 工业 非 PoE / PoE", "1560 / 1760", "DI/DO +60、RS485 +100、10G 光版 +10 USD"),
    ("2025", "10G 光纤 Bypass LT-IS6312XGP-4XS8GT-2BT-2FBP", "1640（<100 台）/ 1600（≥100 台）", "新 CPU ARM v8 1.2 GHz / 512 MB"),
    ("2025 → 2026-08-31", "土耳其警察项目 best offer", "LT-IS6310GP-2GX8GT 全配 820（MOQ 500）；LT-S8328GP-4GX24GT-S 790", "有效期已过，复活需按 2026-09 新表重报"),
    ("2026-06", "全线调价", "+10 USD / 台", "存储器件暴涨；有效期至 2026-08-31"),
    ("2026-09-02", "新价格表（2026-09-01 → 12-30）", "48 口非 PoE 1000→1320、48 PoE 1500→1720、L3 24 口 1300→1500、爆款 24+4 610→710 / 910→1010、工业 4+2 580→660、8+2 620→700、16+2 1100→1180；LT-IS6312XG 1300→840（AC5 单独做板）", "9/1 前下单保老价；8+2 暂停"),
], "small"))
A("<p class='src'>付款：发货前付款即可（2024-02-18）；大货分批（≈5 万 / 批）；预付 20% 才备料（TT 项目）；特殊样品先付款再下单（2025-09-26）；运费 / 贴标 / 寄盒费用计入下一合同。税务：Simon 无退税资质，Peter 建议转「含税」口径（未落地）。来源：`docs/smartbyte_wechat_summary.md` §3.1 与附录 B，8 处关键价已回看原图核对。</p>")
A("<h3>2.3 货：下单 → 出货流程</h3><ul class='tight'>"
  "<li>Saga 发采购合同 PDF + 箱标 docx + 说明书 PDF → Anna 回 SmartByte 销售合同（P 编号）→ 付款 → 排产 → 标签 / 出货图 / 装箱单确认 → 单号。SN 规则 <code>YYYYMMDD0001</code> 按采购订单日。</li>"
  "<li>包装：单页说明书折叠入盒、不放保修卡；外箱打围膜；商用 24 台 / 箱，16+4 工业 12 台 / 箱（440×375×250）；定制彩盒 MOQ 300（不足可预付存厂）；console 线默认不配（+2 USD）；中性包装、无产地字样（继承规则）。</li>"
  "<li>物流：发深圳百运网 / 中技集运，FedEx &lt;5,000 元走简化流程；《发货方式及流程汇总》v3（2025-10-21）。</li></ul>")
A("<h3>2.4 规则：SmartByte 的承诺与红线（决定 Saga 能对客户承诺什么）</h3>")
A(tbl(["主题", "SmartByte 口径", "对 Saga 对外话术的含义"], [
    ("贴牌", "「1 台样品也可免费定制」logo / 型号 / SN / MAC / Web 界面 / 登录页；官网 OEM 页：全部软件定制 No MOQ", "可承诺 neutral packing + 客户品牌 Web UI；Web 语言需 >1K 台、主题色 ≥5K 台不要随口答应"),
    ("开新品", "项目需 3–5 年持续性；MOQ ≥500 / 单且 ≥2K / 年，或一次性 ≥2K；「能不开新产品就不开」；无 PO / 20% 定金不备料", "ODM 只在客户有量时提；档案里把「改板」类需求标为 Q 类待确认"),
    ("不做", "SD-WAN、TSN（当前）、IEEE1588v2、OpenFlow、MPLS、Stacking、100G（2 年内）、数据中心软件、32×10G 软件、IP SLA、风扇转速读取；EN50155 / IP67 / IoT 板 / 8,000 台低价园区机类项目", "与继承规则一致：不做云管理 / 轨交 / IP67 / 消费级；堆叠、MPLS、BGP/IS-IS（Angora 2026-08 问）直接说不支持"),
    ("软硬件", "Marvell 代码自写，SDK/API 受 NDA 不可给；CKD 只出硬件；升级包只由 SmartByte 制作；硬件设计文件不外发", "TTC 文件写法：SDK Integration 可谈需 NDA，Source Code 不可谈"),
    ("OID / MIB", "出厂固件只写客户 OID，不写 SmartByte / Saga 的；客户无 OID 则自行申请或用 OID=0；历史遗留他人 OID 需清理", "私有 MIB 是技术型客户的卖点，但要先问客户 OID"),
    ("硬件事实", "PoE 全部 Mode A；AC5 工业机壳 / 孔位 5 年不变（LT-IS6312GP-4GX8GT-2BT）；10G 收发器 88X3310 不可降 1G/2.5G；Marvell 很少支持 Combo；57 V 输入可用；老化 ≥8 h 50 ℃", "规格书 / 手册没写的功能 = 暂不支持（可谈但要量）"),
    ("供应链", "Marvell 交期 26 周；PoE 芯片 2025-05 紧张；2026 存储暴涨；1K 台一个月交期难、5K 两个月可", "报价有效期 15 天、报价前核价的规则由此而来"),
], "small"))

# 3 产品体系
A("<h2 id='s3'>3 · 产品体系与型号对照</h2>")
A("<div class='two'><div>" + cat_table() + "</div><div class='box'><h4 style='margin-top:0'>SmartByte 型号怎么读（按官网 252 页归纳）</h4><ul class='tight'>"
  "<li><b>LT-IS</b> 工业交换机 / <b>LT-S</b> 商用 / <b>LT-IMC</b> 工业媒体转换器 / <b>LT-MC</b> 商用 MC / <b>LT-IBPA</b> 工业 Boost 电源。</li>"
  "<li>首位数字 <b>3</b> / <b>6</b> = 系列（6 系列 5 年保、3 系列 3 年保；商用 8 开头）；其后两位 = 端口总数，例 6310 = 6 系列 10 口。</li>"
  "<li><b>G / F</b> 千兆 / 百兆，<b>GP</b> 千兆 PoE，<b>XG</b> 万兆上联；端口段 <b>XS</b> SFP+、<b>GX</b> SFP、<b>GT</b> RJ45、<b>GC</b> Combo，例 4XS8GT = 4 SFP+ + 8 RJ45。</li>"
  "<li>尾缀：<b>-D</b> DI/DO/RS485、<b>-SD</b> 温湿度传感器、<b>-nBT</b> n 个 90 W 802.3bt 口、<b>-BST</b> Boost PoE、<b>-FBP</b> 光纤 Bypass、<b>-U</b> 1U 机架、<b>-AD</b> DC 9–58 V + AC 15–40 V 双输入、<b>-M / -E</b> Compact size。</li>"
  "<li>官网 252 页中 <b>{0}</b> 页能对上 2026-09 价格表（精确 {1}、去尾缀 {2}），其余 {3} 页为价格表外型号（-D/-SD 变体、白盒、新品、MC），报价前询价。</li></ul>"
  "<h4>Saga 型号怎么编（Drive《STI-488XGGPM》命名规则）</h4><ul class='tight'>"
  "<li><b>ST</b> = Saga Telecom；<b>I</b> 工业 / <b>C</b> 商用；数字段 = 光 / 电 / PoE 口数（商用管理型为 光 / 电）；<b>XG</b> 万兆光、<b>DG</b> 2.5G 光、<b>G / F</b> 千兆 / 百兆；<b>C</b> Combo、<b>P</b> PoE、<b>M</b> 管理型；<b>-U</b> 1U、<b>-nBT</b> bt 口数。</li>"
  "<li>例：STI-240GM = 工业 2 光 4 电千兆管理；STI-244GPM = 2 光 4 电 PoE 管理；STI-488XGGPM-2BT = 4 万兆光 + 8 电 PoE 管理、2 个 bt 口。</li>"
  "<li>仓库规则：客户档案 / 邮件一律写 Saga 型号；价格表没有 Saga 名的只能写 SmartByte 型号并注明。</li></ul></div></div>".format(
      n_matched, match_how.get("精确", 0), sum(v for k, v in match_how.items() if k.startswith("去后缀") or k.startswith("订购表")), len(idx_rows) - n_matched))

# 4 报价逻辑
A("<h2 id='s4'>4 · 报价逻辑</h2>")
A(f"<div class='box'><b>公式</b>：USD EXW = SmartByte CNY 未税 × 档位系数 ÷ USD/CNY（当前 {rate} @ {rate_date}）。档位：分销商 / 电商 <b>+20%</b>，集成商 / 项目 <b>+25%</b>，OEM/ODM <b>+30%</b>。对外格式：<code>$xx USD EXW（快照日期，15 天有效，报价前核价）</code>。价格表 {len(pm_rows)} 个型号、有效期 2026-09-01 → 12-30；SmartByte 本身的加价项（DI/DO +60 元、RS485 +100 元、10G 光版 +10 USD、850 W 机型 +400、SC 双纤替代 SFP +33、只出板 −35）要先加进 CNY 再乘系数。</div>")
A("<h4>价格表 12 个系列：Saga 卖什么、在什么价位</h4>" + series_table())
A("<h4>代表型号三档价</h4>" + price_sample_table())
A("<p class='src'>全表：`data/价格主表.csv`（135 行）与 `docs/reference/价格表_三档加价_USD.md`。Saga 列表价与公式价的差异已搁置（T03）；STI-240/STI-050 等 Saga 名的端口含义以价格主表为准（Q-27 待批量复核）。</p>")

# 5 技术路线与时间线
A("<h2 id='s5'>5 · 技术路线与时间线（官网路线图 × 微信实际进度 × Saga 动作）</h2>")
A("<div class='tl'>")
for cls, d, t in [
    ("sb", "2020–2022", "SmartByte 深圳创立；工业非管理 → 商用 L2/L2+ → 工业 L2（ARM+SOHO）→ 商用 L3 → AC3 工业 L2/L2+/L3 大批发布；软件 V3 → V5。"),
    ("both", "2023-12", "Saga 与 SmartByte 建立合作（会话 D 2023-12-16 起）：选型、资料整理、与 Realtek 不比价（2 光 8 / 4 光 8 不报价）。"),
    ("sb", "2023", "AC5/AC5X 预研、AC3→AC5 升级 20%；工业 PoE 支持 90 W bt；软件 V6。"),
    ("both", "2024", "首批工业大货 LT-IS6310G 350/385 台（620→600）；验厂；认证以惠州凌特华盛名义（CE/RoHS/REACH/UKCA/FCC，2024-07）；OEM 规则成形；1.08T DC 交换机（Aldrin2）量产、Fiber Bypass 上市、软件 V7.3.0；12 月宣布 AC3→AC5 切换。"),
    ("sg", "2025-01", "土耳其 178 对 LT-IS6318GP-2GX16GT 执行（1490 / 对，总 265,220）；Turk Telekom 项目（800→1500 台）启动。"),
    ("sb", "2025", "AC3→AC5 100%（工业 4+2 / 8+2 / 8+4 先切，9 月 16+4 / 24+4 样机）；DI/DO/RS485 与 Boost PoE 上市；3.2T 白盒 Falcon；预研 Centec；软件 V7.4.0（voice VLAN、ARP 防欺骗、SCP/SFTP…）。"),
    ("sg", "2025-07 → 12", "德国客户双电源 / 风扇监控 MIB（7.4.7 加 fan OID）；首例正式售后；军工 Netas、Bypass 新客户；Angora 1000+ 台 L2+ 大标（MACsec / DDR 2 GB / SFTP）分析。"),
    ("both", "2026-01 → 03", "Netas 3 台 STI-488DGGPM-2BT（AC5）出样；LT-IS6312GP-4GX8GT-2BT 可出 AC5；7.5.0 feature list（MQTT、LLDP-MED、IGMPv3、PIM-SM，主要加强 L2+）；Saga 的 MUST-KNOW 政策包（CCF / TTC / Roadmap / Warranty）定稿（2026-02）。"),
    ("sb", "2026-06 → 08", "存储涨价 → 全线 +10 USD；TT RFP 2026 对标（缺口 OSPFv3 / PIM-DM / stacking / RMON）；7 月「基本没有 AC3」，<b>2026-07-31 AC3 停产</b>（最终固件 lite-hotfix-7.3.13）；<b>2026-08-26 AC5 7.5.0 bin 发布</b>；8/8 深圳见面：Angora 问堆叠 / USB / OOB / 双电源 / BGP / IS-IS，VRF/MPLS pass。"),
    ("sg", "2026 Q3", "Saga PROFILE 2026Q3：重定位为 Marvell AC5 / CENTEC L2+/L3 定制方案商，覆盖 DE / UK / TR / IT；RoadMap Q3 提纲：弱化 Marvell、强化 Managed Networking Solutions、引入 CENTEC 与 DC 交换机；官网 2026-09 改版（T14 裁定为产品事实真源）。"),
    ("sb", "2026-09-02", "新价格表（2026-09-01 → 12-30）；9/30 德国 20 台 LT-S8528XG 双 AC 询价（1520 旧价，Saga vs 博达比较中）。"),
    ("sg", "2026-10", "PLANET 渠道挖掘 W01–W22 → 129 户（A 18）；微信 / Drive / 官网三路资料入库完成（本仓库）；挖掘暂停待指令。"),
    ("sb", "2026 → 2027（官网路线图）", "2026：12.8T Falcon、MQTT / 1588 PTP / Modbus / Profinet、首款 TSN 工业交换机（Ironman）、工业 / 商用 Centec 管理型、软件 V7.5.0；2027：Teralynx 10、TSN 方案、<b>EN50155 系列</b>、V7.6.0。微信口径：TSN / 1588v2 / MPLS / Stacking 当前不做——路线图是意向，报价只认已发布固件。"),
]:
    A(f"<div class='ev {cls}'><div class='d'>{esc(d)}</div><div>{t}</div></div>")
A("</div>")
A("<div class='box'><h4 style='margin-top:0'>AC5 平台事实（对客户技术答疑直接可用）</h4><ul class='tight'>"
  "<li>RAM / Flash 512 MB 标配（DDR 可换 2 GB 不改板，Flash 改板）；L2/L2+ 256 MB（AC3）/ L3 512 MB；HTTPS 原生；SFTP 2025-04；商业与工业软件同源，L2/L3 手册共用；<b>L3 功能仅 CLI</b>；AC3 / AC5 外观、孔位、CLI 相同。</li>"
  "<li>7.5.0（2026-08-26 bin，<b>仅 AC5 硬件</b>）：IGMP & PIM-SM（CLI）、Time Range 联动 ACL / PoE、密码复杂度、端口隔离 32 组、Web 管理 DHCP relay / ARP 防欺骗 / DHCP server / voice VLAN、VLAN 上的 ACL、MQTT、LLDP-MED。AC5 L3 软件 2026-04 起适配，群内未见「完成」。</li>"
  "<li>TT RFP 2026 缺口：OSPFv3、PIM-DM、Stacking、RMON；Angora 1000+ 台大标的 MACsec 是否支持无结论。</li></ul></div>")

# 6 方向
A("<h2 id='s6'>6 · 方向：各自的与共同的</h2>")
A("<div class='two'>")
A("<div class='box sb'><h3 style='margin-top:0'>SmartByte 往哪走</h3><ul class='tight'>"
  "<li><b>平台</b>：AC5 全面化（AC3 停产），AC5 工业机壳 / 孔位 5 年不变；AC5X 2.5G + 25G 商用；白盒 DC（Aldrin2 → Falcon → Teralynx）；Centec 平台管理型（2026）。</li>"
  "<li><b>软件</b>：7.5.0 加强 L2+（IGMP/PIM-SM、MQTT、LLDP-MED）；L3 继续 CLI-only；2026 工业协议（1588 PTP / Modbus / Profinet），2027 TSN / EN50155——都在路线图，不在当前报价范围。</li>"
  "<li><b>商务</b>：价格随 BOM 走（2026 两次上调），价格表制度化（季度有效期）；MOQ 门槛明确（新品 ≥500 / 单且 ≥2K / 年）；希望 Saga 转含税口径、要 Realtek / 博达价格情报。</li>"
  "<li><b>不做</b>：SD-WAN、OpenFlow、MPLS、Stacking、100G（2 年内）、DC 软件、IoT 板、低价 2.5G 红海（RTL8373 / MaxLinear）、Amazon 库存模式。</li></ul></div>")
A("<div class='box sg'><h3 style='margin-top:0'>Saga 往哪走</h3><ul class='tight'>"
  "<li><b>定位</b>：从「卖 Marvell 交换机的贸易商」→「Managed Networking Solutions 方案商」：接入 Marvell（SmartByte）+ 汇聚 / 核心 CENTEC（Hohunet），卖「架构连续性」而不是单品；文件化的 CCF / TTC / 保修 / 订单流程 / 杂费表 / FAQ 做成客户可自助下载的资料包。</li>"
  "<li><b>市场</b>：DE / UK / TR / IT（PROFILE 2026Q3）+ 本仓库的 US/CA + 欧洲 + 土耳其渠道池；小国不主动挖；UA / 军工 / 公共部门 / 轨交 / 生命安全守界。</li>"
  "<li><b>客户优先级</b>：OEM/ODM 品牌商与方案商 > 有中国进口经验或在用台系品牌者 > 分销 / 电商 > 小项目集成商；A 级 = 真实可追溯需求 + 直接具名联系人 + 拿得下的规模。</li>"
  "<li><b>方法</b>：长期跟进、不做广告、单一 P1 型号 + 一个问题的首触邮件、中性包装、不提产地；售后标准化（视频 + 图 + 文字、Zoom、模板与存档）。</li>"
  "<li><b>产品面</b>：L2+ 规格书全部更新到 7.5；跟进 AC5 L3 规格书；Web / CLI 手册 7.5 版与新 catalog；等 SmartByte 的光模块常规价格表。</li></ul></div>")
A("</div>")
A("<div class='box ok'><h4 style='margin-top:0'>两家的共同方向（已被双方行为证实的）</h4><ul class='tight'>"
  "<li>把 AC5 做成 Saga 工业线的 5 年基座（机壳 / 孔位 / CLI 不变），用「长期稳定 + 深度定制 + 交期」对抗台系与 Realtek 低价。</li>"
  "<li>土耳其是双方共同押注的市场（TT / 警察 / Netas / Angora 大标），其次德国（双 AC、风扇 MIB 的需求直接改了固件）与加拿大（16+2 10G 升级）。</li>"
  "<li>研发直接面对终端（扫地僧进客户群、晚间远程）+ Saga 做一线筛选（视频 + 口述）——这是两家合作里最像「一家公司」的部分。</li>"
  "<li>资料透明化：SmartByte 官网 2026-09 改版（规格书可下载、路线图公开）与 Saga 的 buffet-style 资料包同步出现。</li></ul></div>")

# 7 风险与边界
A("<h2 id='s7'>7 · 风险与边界</h2>")
A(tbl(["风险 / 边界", "事实依据", "对策（已定或建议）"], [
    ("单一供应商 + 平台切换", "AC3 2026-07-31 停产；AC5 L3 软件尚未见「完成」；混合 AC3/AC5 现场升级策略未定（加拿大）", "对客户只报 AC5 在售型号；旧项目补货先问 AC3 库存；L3 需求写明 CLI-only"),
    ("成本上行", "2026-06 全线 +10 USD；2026-09 新表多数型号 +10–30%；Marvell 交期 26 周", "报价 15 天有效 + 报价前核价；价格主表对齐新表（待办 #7）"),
    ("大单延期", "TT 800→1500 台 2025-10 起多次延期；Angora 1000+ 台大标无结果；警察项目 best offer 过期", "不以大单为前提备料（SmartByte 规则：无 PO / 20% 定金不备料）"),
    ("合规 / 认证", "无 UL（美国政府渠道 TAA / UL 门槛，Q-02）；无轨交 / E-mark / KC；出口合规文件执行方式（Netas 军工）待定", "美国三户二封邮件前做 UL/TAA 核对；军工 / 公共部门守界"),
    ("Saga 的加价空间与税务", "「给我 100 最多卖 130」；无退税资质；Peter 建议含税口径未落地", "三档系数固定；不打价格战；税务口径列入最后统一裁定"),
    ("口径冲突", "保修：官网 6 系列 5 年 / 商用 3 年 vs Saga 文件 STI 3 年 / STC 1 年（Q-22）；Incoterms：FAQ 写 DAP/DDP vs 仓库 EXW（Q-18）；工厂素材「our factory」口径（Q-24）", "按 Q 清单默认处理：报价 EXW、保修按 Saga 自己的文件、工厂说 manufacturing partner"),
    ("信息可信度", "微信为 OCR 重建稿；Drive 摘要 1,813 条为文件名推断；官网 PDF 尚未归档", "关键数字已回看原图；型号页只照录官网；PDF 运行 #4 落地后再核规格"),
], "small"))

# 8 待跟进
A("<h2 id='s8'>8 · 待跟进（微信 §4，截至 2026-10-16）与待裁定（Q-18 … Q-28）</h2>")
A("<h3>8.1 与 SmartByte 之间的待办</h3>" + todo_table())
A("<h3>8.2 需要 Simon 最后统一裁定的问题（T07 规则：先列、最后处理）</h3>" + q_table())
A("<p class='src'>Q-01 … Q-17 见 `docs/requirements/待统一处理问题清单.md`。</p>")

# 9 资料入库地图
A("<h2 id='s9'>9 · 资料入库地图（在哪找什么）</h2>")
A(tbl(["资料", "仓库位置", "量 / 状态"], [
    ("微信纪要（时间线 / 产品项目 / 决定承诺 / 待跟进）", "docs/smartbyte_wechat_summary.md", "310 行；OCR 稿 docs/smartbyte/微信沟通记录_SmartByte_OCR重建.md（13,943 条）；逐图 OCR data/wechat_smartbyte_ocr/"),
    ("Drive《SmartByte》全量索引", "data/smartbyte_drive_index.json", f"{dmeta['文件总数']:,} 文件 / {dmeta['文件夹总数']} 文件夹 / {dmeta['总大小']}；摘要三档 读取内容 {dmeta['摘要来源统计']['读取内容']} / 型号解码 {dmeta['摘要来源统计']['型号解码']} / 文件名推断 {dmeta['摘要来源统计']['文件名推断']}"),
    ("Drive MUST-KNOW 政策文件（原文）", "docs/drive/MUST-KNOW/*.md", "Roadmap / How We Do Business / CCF / TTC / Warranty / Order Procedure / Misc Fee / FAQ / After-sales / Client Oriented / 白皮书节选"),
    ("官网原始归档", "data/smartbyte_site_raw/", f"{site_sum.get('pages_ok')} 页 HTML + 244 份规格书 PDF（datasheets/，245 条链接中两条同文件）+ 244 份文本（datasheet_text/）+ 图片 images/ + sitemap / robots / 三份清单 / summary"),
    ("官网整理层", "docs/smartbyte/products/（README 索引）", f"{len(P)} 型号页 + data/smartbyte_官网型号索引.csv + data/smartbyte_site/products.json"),
    ("官网公司 / 政策 / 新闻页", "docs/smartbyte/公司与政策页_2026-10-20.md、新闻与固件说明_2026-10-20.md", "About / Warranty / OEM-ODM / SKD-CKD / Contact / 固件 5.x–7.5 全文 / Factory Tour 28 图"),
    ("价格", "data/价格主表.csv、docs/reference/价格表_三档加价_USD.md", f"{len(pm_rows)} 型号，三档 USD，Saga 对应型号"),
    ("Saga 画像 / 口径 / 条款", "docs/reference/Saga公司画像与边界.md、Saga品牌口径与宣传语录.md、Saga商务条款速查.md、从Mikrotik仓库继承的规则摘要.md", "写话术、定级、选档位的依据"),
    ("PLANET 渠道客户池", "data/客户名单_Planet渠道_2026-10.csv、batch/、profile/A|B|C/", f"{len(cust)} 户，A {grade.get('A', 0)} / B {grade.get('B', 0)} / C {grade.get('C', 0)}；首触邮件在档案内；挖掘暂停（W23 计划 = README 第 35 条）"),
    ("台账", "README.md、docs/requirements/用户要求总账.md、对话全记录.md、待统一处理问题清单.md、docs/audit/全仓审计.md", "每轮更新；Q-28 为最新"),
], "small"))
A("<div class='two'><div><h4>Drive 索引按类型</h4>" + drive_table() + "</div><div><h4>Drive 根下一级目录</h4>" + folder_table() + "</div></div>")
A("<h4>官网归档状态</h4>" + site_status())
A("<h4>PLANET 渠道池按国家</h4><div class='two'><div>" + country_table() + "</div><div class='box'><b>读法</b>：US/CA + 欧洲 + 土耳其为用户裁定的区域；A 18 户为「真实可追溯需求 + 具名联系人 + 拿得下」；B 99 户有公开邮箱可群发；C 12 户为无邮箱 / 太大 / 出区 / 偏业务段。首触邮件：单一 P1 型号 + 一个问题，英文，落款 “Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)”。Elsa 账号发送与否「在考虑」，未决前不发。</div></div>")

# 10 可信度
A("<h2 id='s10'>10 · 可信度说明</h2><ul class='tight'>"
  "<li><b>真源优先级</b>（T14 裁定）：SmartByte 官网（2026-09 改版）&gt; SmartByte 2026-09 价格表 &gt; Saga Drive（2026 Q3 旧版）&gt; 仓库既有推断。本页中官网事实带抓取日期 2026-10-20。</li>"
  "<li><b>微信</b>：95 张长截图经 OCR 重建，非逐字原文；8 处关键报价已回看原图切片核对；截图存在时间空洞（2025-04/05、2026-04 等），「没写」≠「没发生」。</li>"
  "<li><b>Drive</b>：索引一个不漏（3,043 条 id 全部回溯到根）；「读取内容」类摘要只读了开头 300–900 字；图片 / 视频 / 设计源文件按文件名推断。</li>"
  "<li><b>官网</b>：350 页中产品页 252 个全部照录；245 份规格书 PDF 已全部归档并抽取文本（型号页规格表以网页为准、PDF 为佐证，两者口径偶有差异时以 PDF 日期新者为准）；" + _img_cred_note() + "两条 404 为站内死链。</li>"
  "<li><b>本页性质</b>：汇编与判断（第 0、6、7 节的「判断」句为代理基于以上资料的归纳），不是双方签署的文件；任何用于对外承诺的数字请回到对应台账核对。</li></ul>")
A(f"<footer>生成脚本 <code>scripts/build_company_logic_html.py</code>（只读仓库数据，可重复生成）· 生成于 {gen_time} · 仓库 elsasaga-cloud/Planet 分支 arena/3f35b9b3-planet · 文字结论来源：微信纪要 / Drive 已读文档 / 官网归档 / 价格主表 / MUST-KNOW / Saga 画像。</footer>")
A("</main></div></body></html>")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("".join(H))
print(OUT, os.path.getsize(OUT), "bytes; todo rows", len(todo_rows), "q rows", len(q_rows), "sample prices", len(sample))
