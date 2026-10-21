#!/usr/bin/env python3
"""SmartByte 官网归档 → 整理层（T15 第二步）。

输入（原始层，由 Actions 归档器写入，不手改）：
  data/smartbyte_site_raw/pages_manifest.jsonl / html/*.html / downloads_manifest.jsonl / datasheet_text/*.txt
输出（整理层，全部由本脚本生成，不手改）：
  data/smartbyte_site/products.json          全部产品页结构化数据（含规格表逐行、订购表、图片、规格书链接/本地文件）
  data/smartbyte_官网型号索引.csv              每产品页一行：型号 / 标题 / 品类 / URL / 基型号(价格主表) / Saga 对应型号 / CNY
  docs/smartbyte/products/<型号>.md           每型号一页：原文照录（Overview / Features / 规格表 / 订购信息）+ 价格主表对照
  docs/smartbyte/products/README.md          按品类分组的索引

用法：python3 scripts/smartbyte_crawl/build.py   （在仓库根目录；需要 beautifulsoup4 + lxml）
规则：
  - 只整理，不改原文；英文原文照录，中文只出现在栏目名/说明；所有事实带官网 URL + 抓取日期（pages_manifest 的 fetched_at）。
  - 价格主表（data/价格主表.csv，SmartByte 2026-09 价格表，有效期 2026-09-01～12-30）匹配：先精确，再逐段去尾缀
    （-D / -SD / -2BT / -U / -AD / -E / -M / " Series" 等），再用订购表里的具体型号；匹配方式写进索引，未匹配如实写「未匹配」。
  - Saga 对应型号来自价格主表的「Saga对应型号」列；没有就空着（档案里写 SmartByte 型号时须注明——见 AGENT-README 规则）。
"""
import csv
import json
import os
import re
import sys
from collections import OrderedDict, defaultdict
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover
    sys.exit("pip install --break-system-packages beautifulsoup4 lxml")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "data", "smartbyte_site_raw")
OUT_JSON = os.path.join(ROOT, "data", "smartbyte_site", "products.json")
OUT_CSV = os.path.join(ROOT, "data", "smartbyte_官网型号索引.csv")
OUT_MD_DIR = os.path.join(ROOT, "docs", "smartbyte", "products")
PRICE_CSV = os.path.join(ROOT, "data", "价格主表.csv")
HOST = "www.smartbyte-switch.com"
BASE = f"https://{HOST}/"
CDN_IMG_RE = re.compile(r"https?://[a-z0-9.-]+/comdata/\d+/[^\"' )]+?\.(?:jpg|jpeg|png|gif|webp)", re.I)


def norm_url(u, base=BASE):
    """与 crawl.py 的 norm() 同口径，保证能和 downloads_manifest 的 url 对上。"""
    u = urljoin(base, u.strip())
    p = urlparse(u)
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not k.lower().startswith("utm")]
    return urlunparse(("https", HOST, p.path or "/", "", urlencode(q), ""))


def clean(s):
    s = (s or "").replace("\xa0", " ").replace("\u200b", "")
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\s*\n\s*", "\n", s)
    return s.strip()


def cell_text(td):
    # <br> / <p> 当换行，其余拼接
    for br in td.find_all("br"):
        br.replace_with("\n")
    txt = td.get_text("\n")
    return clean(re.sub(r"\n{2,}", "\n", txt))


def parse_table(table):
    """Word 粘贴的规格表 → [(section, key, value)]；1 格 = 小节标题，2 格 = 键/值，≥3 格 = 键 + 其余用 ' | ' 连接；处理 rowspan 的键。"""
    rows = []
    section = ""
    pending = None  # (key, remaining_rows)
    for tr in table.find_all("tr"):
        cells = [c for c in tr.find_all(["td", "th"], recursive=False)]
        if not cells:
            cells = tr.find_all(["td", "th"])
        texts = [cell_text(c) for c in cells]
        nonempty = [(c, t) for c, t in zip(cells, texts) if t]
        if not nonempty:
            continue
        if pending and pending[1] > 0 and len(nonempty) == 1:
            rows.append((section, pending[0], nonempty[0][1]))
            pending = (pending[0], pending[1] - 1)
            continue
        if pending and pending[1] > 0 and len(nonempty) >= 2:
            first = nonempty[0][1]
            if len(first) <= 3 or re.fullmatch(r"[\d.,/*+\-\s]+", first):
                # rowspan 键下的 多列数值（如 Interface: Fiber ports | Copper ports → 2 | 8）
                rows.append((section, pending[0], " | ".join(t for _, t in nonempty)))
            else:
                # rowspan 键下的 子键/值
                rows.append((section, f"{pending[0]} / {first}", " | ".join(t for _, t in nonempty[1:])))
            pending = (pending[0], pending[1] - 1)
            continue
        pending = None
        if len(nonempty) == 1:
            c, t = nonempty[0]
            span = int(c.get("colspan", "1") or 1)
            if span > 1 or len(cells) == 1 or c.find("strong") is not None:
                section = t.replace("\n", " ")
            else:
                rows.append((section, t.replace("\n", " "), ""))
            continue
        key = nonempty[0][1].replace("\n", " ")
        val = " | ".join(t for _, t in nonempty[1:])
        rs = int(nonempty[0][0].get("rowspan", "1") or 1)
        if rs > 1:
            pending = (key, rs - 1)
        rows.append((section, key, val))
    return rows


def parse_order_table(table):
    out = []
    for tr in table.find_all("tr"):
        texts = [cell_text(c) for c in tr.find_all(["td", "th"])]
        texts = [t for t in texts if t]
        if len(texts) < 2:
            continue
        if texts[0].strip().lower() in ("model", "model no.", "model number", "part number", "p/n"):
            continue
        out.append({"model": texts[0].replace("\n", " "), "description": " | ".join(texts[1:])})
    return out


def bullets(container):
    """Features 栏：按 <p>/<li>/<br> 拆行，去掉 ➢ ● ■ ◆ • 等项目符号。"""
    for br in container.find_all("br"):
        br.replace_with("\n")
    lines = []
    for blk in container.find_all(["p", "li", "div", "span"]):
        if blk.find(["p", "li", "div"]):
            continue
        lines.extend(clean(blk.get_text("\n")).split("\n"))
    if not lines:
        lines = clean(container.get_text("\n")).split("\n")
    out = []
    for ln in lines:
        ln = re.sub(r"^[\s➢●■◆•·\-\u2022\u25cf\u25b6>]+", "", ln).strip()
        if ln and ln not in out:
            out.append(ln)
    return out


def load_jsonl(p):
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def load_price_master():
    pm = OrderedDict()
    if not os.path.exists(PRICE_CSV):
        return pm
    with open(PRICE_CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            m = (r.get("SmartByte型号") or "").strip()
            if m:
                pm[m] = r
    return pm


SUFFIX_RE = re.compile(r"\s+Series$", re.I)


def match_price(models, pm):
    """返回 (基型号, 匹配方式, 价格行) 或 (None, '未匹配', None)。"""
    tried = []
    for m in models:
        m0 = SUFFIX_RE.sub("", (m or "").strip())
        if not m0:
            continue
        if m0 in pm:
            return m0, ("精确" if m == models[0] else "订购表型号精确"), pm[m0]
        parts = m0.split("-")
        # 逐段去尾缀（最多去 3 段，且保留至少 LT-xxxx-端口段 两段）
        for k in range(1, min(3, len(parts) - 2) + 1):
            cand = "-".join(parts[:-k])
            tried.append(cand)
            if cand in pm:
                how = "去后缀(" + "-".join(parts[-k:]) + ")"
                if m != models[0]:
                    how = "订购表型号" + how
                return cand, how, pm[cand]
    return None, "未匹配", None


def product_from_html(path, page):
    with open(path, encoding="utf-8", errors="ignore") as f:
        html = f.read()
    m = re.search(r'name="ProductID"\s+value="(\d+)"', html)
    if not m:
        return None
    pid = m.group(1)
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.select_one("h1.pro-name")
    title = clean(h1.get_text()) if h1 else clean((page.get("title") or "").replace("-SmartByte", ""))
    ms = soup.select_one("span.mobile-model")
    model = clean(ms.get_text()).replace("\n", " ") if ms else ""
    crumbs = []
    ol = soup.select_one("ol.breadcrumb")
    if ol:
        crumbs = [clean(a.get_text()) for a in ol.select("li a")]
        last = ol.select_one("li.lastMenu")
        if last:
            crumbs.append(clean(last.get_text()))
    cat1 = crumbs[1] if len(crumbs) > 1 else ""
    cat2 = crumbs[2] if len(crumbs) > 2 else ""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_desc = clean(meta_desc.get("content")) if meta_desc else ""
    if not model and meta_desc:  # 白盒页没有型号栏，型号只在 meta description：「标题, 型号, SmartByte」
        mm = re.sub(r"\s*,\s*SmartByte\s*$", "", meta_desc, flags=re.I)
        if mm.lower().startswith(title.lower()):
            mm = mm[len(title):]
        mm = mm.strip(" ,")
        if 3 <= len(mm) <= 60 and "," not in mm:
            model = mm

    # 标签页：Overview / Features / Technical specification / Order information / ...
    sections = OrderedDict()
    nav = soup.select_one("ul#myTab")
    content = soup.select_one("div.particularsMain.tab-content")
    if nav and content:
        names = [clean(a.get_text()) for a in nav.select("li a")]
        panes = content.find_all("div", class_="tab-pane", recursive=False)
        for name, pane in zip(names, panes):
            sections[name] = pane
    else:  # 移动版布局：h2.particularsNav + div.particularsMain 交替
        for h2 in soup.select("h2.particularsNav"):
            pane = h2.find_parent().find_next_sibling("div", class_="particularsMain")
            if pane is not None:
                sections[clean(h2.get_text())] = pane

    overview, features, specs, order, extra = "", [], [], [], OrderedDict()
    pane_images = []
    for name, pane in sections.items():
        key = name.lower()
        for img in pane.find_all("img"):
            src = img.get("src") or img.get("data-src") or ""
            if src and src not in pane_images:
                pane_images.append(src)
        if key.startswith("overview") or key.startswith("product overview") or key.startswith("description"):
            overview = clean(pane.get_text("\n"))
            overview = re.sub(r"\n{2,}", "\n", overview)
        elif key.startswith("feature"):
            features = bullets(pane)
        elif "specification" in key or key.startswith("spec"):
            for t in pane.find_all("table"):
                specs.extend(parse_table(t))
            if not specs:
                extra[name] = clean(pane.get_text("\n"))
        elif key.startswith("order"):
            for t in pane.find_all("table"):
                order.extend(parse_order_table(t))
            if not order:
                extra[name] = clean(pane.get_text("\n"))
        else:
            txt = clean(pane.get_text("\n"))
            if txt:
                extra[name] = re.sub(r"\n{2,}", "\n", txt)

    # 规格书（Download Annex）
    ds = OrderedDict()
    for a in soup.select("a.downloadonc, a[href*='downloadFujian']"):
        href = a.get("href") or ""
        if "downloadFujian" not in href:
            continue
        u = norm_url(href)
        q = dict(parse_qsl(urlparse(u).query, keep_blank_values=True))
        ds[u] = {"title": clean(q.get("name", "")), "url": u, "path": None}
        try:
            import base64
            raw = q.get("path", "")
            ds[u]["path"] = base64.b64decode(raw + "=" * (-len(raw) % 4)).decode("utf-8", "ignore")
        except Exception:
            pass

    # 图片：产品大图（CDN *_b.*）+ 栏目内图（结构图等）
    imgs = []
    for u in CDN_IMG_RE.findall(html):
        if "/product/" in u and re.search(r"_b\.(jpg|jpeg|png)$", u, re.I) and u not in imgs:
            imgs.append(u)
    diagrams = [u for u in pane_images if u not in imgs]

    return {
        "product_id": pid,
        "url": page["url"],
        "fetched_at": page.get("fetched_at"),
        "page_file": page.get("file"),
        "title": title,
        "model": model,
        "meta_description": meta_desc,
        "category_l1": cat1,
        "category_l2": cat2,
        "breadcrumb": crumbs,
        "overview": overview,
        "features": features,
        "specs": [{"section": s, "key": k, "value": v} for s, k, v in specs],
        "order_info": order,
        "extra_sections": extra,
        "datasheets": list(ds.values()),
        "images": imgs,
        "diagram_images": diagrams,
    }


def safe_name(s):
    s = re.sub(r"\s+Series$", "_Series", s.strip(), flags=re.I)
    s = re.sub(r"[\\/:*?\"<>|\s]+", "_", s).strip("_")
    return s or "unnamed"


def md_escape(s):
    return (s or "").replace("|", "\\|").replace("\n", "<br>")


def render_md(p, pmatch, dl_by_url):
    base, how, prow = pmatch
    lines = [f"# {p['model'] or ('产品页 ' + p['product_id'])} — {p['title']}", ""]
    lines.append(f"- 官网页面：{p['url']}（抓取 {(p.get('fetched_at') or '')[:10]}，原始 HTML：`data/smartbyte_site_raw/{p['page_file']}`）")
    lines.append(f"- 官网品类：{p['category_l1']} / {p['category_l2']}")
    if p["meta_description"]:
        lines.append(f"- 页面描述（meta）：{p['meta_description']}")
    if p["datasheets"]:
        for d in p["datasheets"]:
            rec = dl_by_url.get(d["url"])
            if rec and rec.get("file"):
                if os.path.exists(os.path.join(RAW, "datasheets", rec.get("filename") or "")):
                    loc = f"已归档 PDF `data/smartbyte_site_raw/datasheets/{rec['filename']}`"
                else:
                    loc = f"已归档（二进制在 Actions Release 附件 `{rec.get('file')}`）"
                if rec.get("text_file"):
                    loc += f"，文本 `data/smartbyte_site_raw/{rec['text_file']}`"
            elif rec:
                loc = f"官网下载口拒绝（{rec.get('error') or ('HTTP ' + str(rec.get('status')))}），待归档器重试"
            else:
                loc = "归档器尚未处理"
            lines.append(f"- 规格书（Download Annex）：{d['title'] or '规格书'} — {d['url']}（{loc}）")
    else:
        lines.append("- 规格书：页面未提供下载")
    lines.append("")
    lines.append("## 价格主表对照（SmartByte 2026-09 价格表，有效期 2026-09-01～12-30；USD 按 6.69 @2026-10-17）")
    if prow:
        lines.append(f"- 基型号：**{base}**（匹配方式：{how}）")
        lines.append(f"- CNY 未税：{prow.get('CNY未税','')}；USD@+20% {prow.get('USD@+20%','')} / +25% {prow.get('USD@+25%','')} / +30% {prow.get('USD@+30%','')}")
        lines.append(f"- Saga 对应型号：**{prow.get('Saga对应型号','') or '（价格主表未给，档案中写 SmartByte 型号须注明）'}**；Saga 列表价 USD：{prow.get('Saga列表价USD','')}；档位/备注：{prow.get('Saga档位/备注','')}；对照说明：{prow.get('对照说明','')}")
        if base != SUFFIX_RE.sub("", p["model"]):
            lines.append(f"- 注意：官网型号 `{p['model']}` 与基型号不同（尾缀 = 传感器 -D/-SD、PoE++ -nBT、机架 -U、-AD/-E/-M 等变体），报价前按微信纪要的加价规则核价（DI/DO +60、RS485 +100、10G 光版 +10 USD 等见 `docs/smartbyte_wechat_summary.md` §3）。")
    else:
        lines.append(f"- 价格主表**未匹配**（{how}）：该型号不在 2026-09 价格表的 135 个型号里 → 报价前向 SmartByte 询价；档案中只能写 SmartByte 型号并注明。")
    lines.append("")
    if p["overview"]:
        lines += ["## Overview（原文）", "", p["overview"], ""]
    if p["features"]:
        lines += ["## Features（原文）", ""] + [f"- {f}" for f in p["features"]] + [""]
    if p["specs"]:
        lines += ["## Technical specification（原文，表格逐行照录）", "", "| 小节 | 项目 | 规格 |", "|---|---|---|"]
        for s in p["specs"]:
            lines.append(f"| {md_escape(s['section'])} | {md_escape(s['key'])} | {md_escape(s['value'])} |")
        lines.append("")
    if p["order_info"]:
        lines += ["## Order information（原文）", "", "| Model | Description |", "|---|---|"]
        for o in p["order_info"]:
            lines.append(f"| {md_escape(o['model'])} | {md_escape(o['description'])} |")
        lines.append("")
    for name, txt in p["extra_sections"].items():
        lines += [f"## {name}（原文）", "", txt, ""]
    if p["images"] or p["diagram_images"]:
        lines += ["## 图片（CDN 链接；二进制随归档 Release 保存，不入 git）", ""]
        lines += [f"- {u}" for u in p["images"]]
        lines += [f"- （栏目内图）{u}" for u in p["diagram_images"]]
        lines.append("")
    lines.append("---")
    lines.append("来源：SmartByte 官网（T15 Actions 归档，原文照录，未做改写）；本文件由 `scripts/smartbyte_crawl/build.py` 生成，勿手改。")
    return "\n".join(lines) + "\n"


def main():
    pages = load_jsonl(os.path.join(RAW, "pages_manifest.jsonl"))
    dls = load_jsonl(os.path.join(RAW, "downloads_manifest.jsonl"))
    dl_by_url = {}
    for d in dls:
        prev = dl_by_url.get(d["url"])
        if prev is None or (d.get("file") and not prev.get("file")):
            dl_by_url[d["url"]] = d
    pm = load_price_master()
    products = []
    for pg in pages:
        if not pg.get("file"):
            continue
        path = os.path.join(RAW, pg["file"])
        if not os.path.exists(path):
            continue
        p = product_from_html(path, pg)
        if p:
            products.append(p)
    # 去重：同一 ProductID 可能有 /ProductDetail/<id>.html 与 slug 两个 URL → 留 slug 版，另一个记为别名
    by_pid = OrderedDict()
    for p in products:
        q = by_pid.get(p["product_id"])
        if q is None:
            by_pid[p["product_id"]] = p
            p["alias_urls"] = []
        else:
            keep, drop = (p, q) if ("ProductDetail" in q["url"] and "ProductDetail" not in p["url"]) else (q, p)
            keep["alias_urls"] = sorted(set(keep.get("alias_urls", []) + [drop["url"]] + drop.get("alias_urls", [])))
            by_pid[p["product_id"]] = keep
    products = list(by_pid.values())
    products.sort(key=lambda p: (p["category_l1"], p["category_l2"], p["model"] or "~", p["title"]))

    # 价格匹配 + MD 文件名
    used = {}
    index_rows = []
    os.makedirs(OUT_MD_DIR, exist_ok=True)
    for fn in os.listdir(OUT_MD_DIR):
        if fn.endswith(".md") and fn != "README.md":
            os.remove(os.path.join(OUT_MD_DIR, fn))
    for p in products:
        cands = [p["model"]] + [o["model"] for o in p["order_info"] if o.get("model")]
        base, how, prow = match_price([c for c in cands if c], pm)
        p["price_master"] = {"base_model": base, "how": how,
                             "cny": prow.get("CNY未税") if prow else None,
                             "saga_model": prow.get("Saga对应型号") if prow else None,
                             "saga_list_usd": prow.get("Saga列表价USD") if prow else None,
                             "tier_note": prow.get("Saga档位/备注") if prow else None}
        stem = safe_name(p["model"]) if p["model"] else f"PID{p['product_id']}"
        if stem in used:
            stem = f"{stem}_{p['product_id']}"
        used[stem] = p["product_id"]
        p["md_file"] = f"docs/smartbyte/products/{stem}.md"
        for d in p["datasheets"]:
            rec = dl_by_url.get(d["url"])
            d["archived_file"] = rec.get("file") if rec else None
            d["text_file"] = rec.get("text_file") if rec else None
            d["status"] = ("ok" if rec and rec.get("file") else (rec.get("error") or f"HTTP {rec.get('status')}") if rec else "pending")
        with open(os.path.join(ROOT, p["md_file"]), "w", encoding="utf-8") as f:
            f.write(render_md(p, (base, how, prow), dl_by_url))
        ds0 = p["datasheets"][0] if p["datasheets"] else {}
        index_rows.append(OrderedDict([
            ("SmartByte型号", p["model"]), ("官网标题", p["title"]), ("官网品类", p["category_l2"]), ("官网大类", p["category_l1"]),
            ("官网URL", p["url"]), ("抓取日期", (p.get("fetched_at") or "")[:10]),
            ("基型号(价格主表)", base or ""), ("匹配方式", how),
            ("Saga对应型号", (prow or {}).get("Saga对应型号", "")), ("CNY未税(2026-09价格表)", (prow or {}).get("CNY未税", "")),
            ("规格书URL", ds0.get("url", "")), ("规格书归档", ds0.get("status", "")),
            ("订购表型号", " ; ".join(o["model"] for o in p["order_info"])),
            ("型号页MD", p["md_file"]), ("ProductID", p["product_id"]),
            ("备注", ("别名 URL: " + " ; ".join(p["alias_urls"])) if p.get("alias_urls") else ""),
        ]))

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump({"meta": {"source": "SmartByte 官网 Actions 归档（data/smartbyte_site_raw）", "generated_by": "scripts/smartbyte_crawl/build.py",
                            "products": len(products), "with_model": sum(1 for p in products if p["model"]),
                            "price_matched": sum(1 for p in products if p["price_master"]["base_model"]),
                            "datasheet_links": sum(len(p["datasheets"]) for p in products),
                            "datasheets_archived": sum(1 for p in products for d in p["datasheets"] if d["status"] == "ok")},
                   "products": products}, f, ensure_ascii=False, indent=1)
    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(index_rows[0].keys()), lineterminator="\r\n")
        w.writeheader()
        w.writerows(index_rows)

    # README 索引
    groups = defaultdict(list)
    for p in products:
        groups[(p["category_l1"], p["category_l2"])].append(p)
    n_match = sum(1 for p in products if p["price_master"]["base_model"])
    n_ds_ok = sum(1 for p in products for d in p["datasheets"] if d["status"] == "ok")
    n_ds = sum(len(p["datasheets"]) for p in products)
    L = ["# SmartByte 官网产品库（整理层索引）", "",
         f"- 来源：`data/smartbyte_site_raw/`（T15 GitHub Actions 整站归档；产品页 {len(products)} 个，抓取 2026-10-20）；本目录每型号一页，由 `scripts/smartbyte_crawl/build.py` 生成，**勿手改**。",
         f"- 价格主表匹配：{n_match}/{len(products)} 个产品页能对上 2026-09 价格表（精确或去尾缀）；其余为价格表外型号（新品 / 变体 / 白盒），报价前询价。",
         f"- 规格书：页面给出 {n_ds} 个下载链接，已归档 {n_ds_ok} 个（官网 PHP 下载口对运行器返回 403；v2.2 归档器改走直链重试中，落地后重跑本脚本即自动补齐本地文件与文本链接）。",
         "- 型号命名（SmartByte，按官网页面归纳）：LT-IS = 工业，LT-S = 商用，LT-IMC = 工业媒体转换器，LT-MC = 商用媒体转换器，LT-IBPA = 工业 Boost 电源；首位数字 3/6 = 系列（官网保修页：工业 6 系列 5 年 / 3 系列 3 年），其后两位 = 端口总数；G/F = 千兆/百兆，GP = 千兆 PoE，XG = 万兆上联，XS = SFP+，GX = SFP，GT = RJ45，GC = Combo；尾缀 -D = DI/DO/RS485，-SD = 温湿度传感器，-nBT = n 个 90W 802.3bt 口，-BST = Boost PoE，-U = 1U 机架式，-AD = 直流 9–58V + 交流 15–40V 双输入，-M = Compact size 紧凑型，-E（媒体转换器）= Compact size 紧凑型。Saga 对应名见各页「价格主表对照」。",
         "", "| 大类 | 品类 | 型号数 |", "|---|---|---|"]
    for (c1, c2), ps in groups.items():
        L.append(f"| {c1} | {c2} | {len(ps)} |")
    L.append("")
    for (c1, c2), ps in groups.items():
        L += [f"## {c1} / {c2}（{len(ps)}）", "", "| 型号 | 标题 | 基型号(价格主表) | Saga 对应 | CNY | 规格书 | 页面 |", "|---|---|---|---|---|---|---|"]
        for p in ps:
            pmx = p["price_master"]
            ds = p["datasheets"][0] if p["datasheets"] else None
            ds_s = ("✅" if ds and ds["status"] == "ok" else ("⏳" if ds else "—"))
            L.append(f"| [{md_escape(p['model']) or 'PID' + p['product_id']}]({os.path.basename(p['md_file'])}) | {md_escape(p['title'])} | {pmx['base_model'] or '未匹配'} | {pmx['saga_model'] or ''} | {pmx['cny'] or ''} | {ds_s} | [官网]({p['url']}) |")
        L.append("")
    with open(os.path.join(OUT_MD_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"products {len(products)} (with model {sum(1 for p in products if p['model'])}); price matched {n_match}; "
          f"datasheet links {n_ds}, archived {n_ds_ok}; md files {len(used)}; csv rows {len(index_rows)}")


if __name__ == "__main__":
    main()
