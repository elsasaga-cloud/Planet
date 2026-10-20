#!/usr/bin/env python3
"""SmartByte 官网整站归档器（T15）。

在 GitHub Actions 运行器上执行（Arena 沙箱对 smartbyte-switch.com 无出网权限）。
职责只有一个：把站点上**所有**可达页面、附件（规格书等）、图片原样抓下来并写清单；
解析/整理在仓库内另做（scripts/smartbyte_crawl/build.py）。

用法：python crawl.py <OUT_dir(入 git)> <BIN_dir(二进制，不入 git)>
环境变量：MAX_PAGES(默认 1500) DELAY(默认 0.8s) MAX_IMAGE_MB(默认 600) PDF_COMMIT_MB(默认 60)
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import deque
from datetime import datetime, timezone
from urllib.parse import parse_qsl, unquote, urlencode, urljoin, urlparse, urlunparse

import requests

HOST = "www.smartbyte-switch.com"
BASE = f"https://{HOST}/"
OUT = sys.argv[1] if len(sys.argv) > 1 else "data/smartbyte_site_raw"
BIN = sys.argv[2] if len(sys.argv) > 2 else "crawl_bin"
MAX_PAGES = int(os.environ.get("MAX_PAGES", "1500"))
DELAY = float(os.environ.get("DELAY", "0.8"))
MAX_IMAGE_MB = float(os.environ.get("MAX_IMAGE_MB", "600"))
PDF_COMMIT_MB = float(os.environ.get("PDF_COMMIT_MB", "60"))
UA = "Mozilla/5.0 (compatible; SagaTelecom-site-archiver/1.0; +https://sagatele.com)"

ASSET_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp", ".css", ".js", ".woff", ".woff2",
             ".ttf", ".eot", ".otf", ".mp4", ".webm", ".mp3", ".map", ".json")
FILE_EXT = (".pdf", ".zip", ".rar", ".7z", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".bin", ".img", ".exe")
IMG_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico")

S = requests.Session()
S.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.5"})
T0 = time.time()
LOG = []


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    LOG.append(line)


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def norm(u, base=BASE):
    try:
        u = urljoin(base, u.strip())
        p = urlparse(u)
    except Exception:
        return None
    if p.scheme not in ("http", "https"):
        return None
    if p.netloc.lower() not in (HOST, "smartbyte-switch.com"):
        return None
    path = p.path or "/"
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not k.lower().startswith("utm")]
    return urlunparse(("https", HOST, path, "", urlencode(q), ""))


def kind(u):
    """page / download / image / asset"""
    p = urlparse(u)
    path = p.path.lower()
    q = p.query.lower()
    if "downdetail" in path.lower() or "downdetail" in q or "a=download" in q:
        return "download"
    if path.endswith(IMG_EXT):
        return "image"
    if path.endswith(FILE_EXT):
        return "download"
    if path.endswith(ASSET_EXT):
        return "asset"
    return "page"


def fname(u, ext=""):
    p = urlparse(u)
    s = unquote(p.path).strip("/") or "index"
    if p.query:
        s += "__" + unquote(p.query)
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_")
    if len(s) > 140:
        s = s[:110] + "_" + hashlib.md5(u.encode()).hexdigest()[:10]
    return s + ext


def get(u, stream=False, timeout=60):
    last = None
    for i in range(4):
        try:
            r = S.get(u, timeout=timeout, stream=stream, allow_redirects=True)
            if r.status_code in (403, 429, 500, 502, 503, 504):
                last = f"HTTP {r.status_code}"
                time.sleep(4 * (i + 1))
                continue
            return r, None
        except requests.RequestException as e:
            last = repr(e)
            time.sleep(4 * (i + 1))
    return None, last


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main():
    for d in ("html", "datasheet_text", "datasheets"):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
    for d in ("downloads", "images"):
        os.makedirs(os.path.join(BIN, d), exist_ok=True)

    # ---------- seeds ----------
    seeds = [BASE]
    r, err = get(BASE + "sitemap.xml")
    if r is not None and r.status_code == 200:
        with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(r.text)
        locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", r.text, flags=re.I | re.S)
        for l in locs:
            n = norm(l)
            if n and n not in seeds:
                seeds.append(n)
        log(f"sitemap: {len(locs)} loc, {len(seeds)} seeds")
    else:
        log(f"sitemap fetch failed: {err}")
    r, err = get(BASE + "robots.txt")
    if r is not None and r.status_code == 200:
        with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
            f.write(r.text)

    # ---------- BFS over pages ----------
    queue = deque(seeds)
    seen = set(seeds)
    pages = []
    downloads = {}  # url -> {found_on: [...]}
    images = {}  # url -> {found_on: [...], alt: ...}
    external = {}
    while queue and len(pages) < MAX_PAGES:
        u = queue.popleft()
        r, err = get(u)
        time.sleep(DELAY)
        rec = {"url": u, "fetched_at": now(), "status": None, "final_url": None, "content_type": None,
               "file": None, "bytes": None, "sha256": None, "title": None, "error": err}
        if r is None:
            log(f"FAIL {u}: {err}")
            pages.append(rec)
            continue
        rec.update(status=r.status_code, final_url=r.url, content_type=r.headers.get("content-type"))
        if r.status_code != 200:
            log(f"HTTP {r.status_code} {u}")
            pages.append(rec)
            continue
        ct = (rec["content_type"] or "").lower()
        if "html" not in ct and "xml" not in ct and "text" not in ct:
            # binary served at a page URL → treat as download
            downloads.setdefault(u, {"found_on": []})["found_on"].append("(direct)")
            rec["error"] = "binary-at-page-url → downloads"
            pages.append(rec)
            continue
        if r.encoding is None or r.encoding.lower() in ("iso-8859-1", "latin-1"):
            r.encoding = r.apparent_encoding or "utf-8"
        html = r.text
        name = fname(u, ".html")
        with open(os.path.join(OUT, "html", name), "w", encoding="utf-8") as f:
            f.write(html)
        m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
        rec.update(file=f"html/{name}", bytes=len(html.encode("utf-8")), sha256=sha256(html.encode("utf-8")),
                   title=re.sub(r"\s+", " ", m.group(1)).strip() if m else None)
        pages.append(rec)
        # links
        for href in re.findall(r"""href\s*=\s*["']([^"'#]+)""", html, flags=re.I):
            if href.lower().startswith(("javascript:", "mailto:", "tel:", "whatsapp:", "data:")):
                continue
            n = norm(href, r.url)
            if n is None:
                try:
                    h = urlparse(urljoin(r.url, href)).netloc
                    if h:
                        external.setdefault(h, set()).add(u)
                except Exception:
                    pass
                continue
            k = kind(n)
            if k == "page":
                if n not in seen:
                    seen.add(n)
                    queue.append(n)
            elif k == "download":
                downloads.setdefault(n, {"found_on": []})["found_on"].append(u)
            elif k == "image":
                images.setdefault(n, {"found_on": [], "alt": ""})["found_on"].append(u)
        for m2 in re.finditer(r"""<img[^>]+?(?:src|data-src|data-original)\s*=\s*["']([^"']+)["'][^>]*>""", html, flags=re.I):
            n = norm(m2.group(1), r.url)
            if n is None:
                continue
            alt = re.search(r"""alt\s*=\s*["']([^"']*)""", m2.group(0), flags=re.I)
            d = images.setdefault(n, {"found_on": [], "alt": ""})
            d["found_on"].append(u)
            if alt and alt.group(1) and not d["alt"]:
                d["alt"] = alt.group(1)
        for m3 in re.finditer(r"""url\(\s*["']?([^"')]+?)["']?\s*\)""", html, flags=re.I):
            n = norm(m3.group(1), r.url)
            if n and kind(n) == "image":
                images.setdefault(n, {"found_on": [], "alt": ""})["found_on"].append(u)
        if len(pages) % 25 == 0:
            log(f"pages {len(pages)} queue {len(queue)} downloads {len(downloads)} images {len(images)}")
    log(f"BFS done: pages={len(pages)} queue_left={len(queue)} downloads={len(downloads)} images={len(images)}")
    write_jsonl(os.path.join(OUT, "pages_manifest.jsonl"), pages)

    # ---------- downloads (datasheets etc.) ----------
    dl_rows = []
    used = {}
    for i, (u, meta) in enumerate(sorted(downloads.items())):
        r, err = get(u, stream=True, timeout=120)
        rec = {"url": u, "found_on": sorted(set(meta["found_on"])), "fetched_at": now(), "status": None,
               "content_type": None, "filename": None, "file": None, "bytes": None, "sha256": None, "error": err}
        if r is None:
            dl_rows.append(rec)
            log(f"DL FAIL {u}: {err}")
            continue
        rec.update(status=r.status_code, content_type=r.headers.get("content-type"))
        if r.status_code != 200:
            dl_rows.append(rec)
            continue
        cd = r.headers.get("content-disposition", "")
        fn = None
        m = re.search(r"filename\*\s*=\s*(?:UTF-8|utf-8)''([^;]+)", cd)
        if m:
            fn = unquote(m.group(1).strip().strip('"'))
        else:
            m = re.search(r'filename\s*=\s*"?([^";]+)"?', cd)
            if m:
                fn = m.group(1).strip()
                try:
                    fn = fn.encode("latin-1").decode("utf-8")
                except Exception:
                    pass
        if not fn:
            fn = unquote(os.path.basename(urlparse(r.url).path)) or "download"
            if "." not in fn:
                ct = (rec["content_type"] or "").lower()
                fn += ".pdf" if "pdf" in ct else (".bin")
        fn = re.sub(r"[\\/:*?\"<>|]+", "_", fn).strip() or "download.bin"
        data = r.content
        h = sha256(data)
        base_fn = fn
        if fn in used and used[fn] != h:
            stem, ext = os.path.splitext(base_fn)
            fn = f"{stem}_{h[:8]}{ext}"
        used[fn] = h
        with open(os.path.join(BIN, "downloads", fn), "wb") as f:
            f.write(data)
        rec.update(filename=fn, file=f"downloads/{fn}", bytes=len(data), sha256=h)
        dl_rows.append(rec)
        time.sleep(DELAY)
        if (i + 1) % 20 == 0:
            log(f"downloads {i + 1}/{len(downloads)}")
    write_jsonl(os.path.join(OUT, "downloads_manifest.jsonl"), dl_rows)
    log(f"downloads done: {sum(1 for d in dl_rows if d['file'])}/{len(dl_rows)} ok, "
        f"{sum(d['bytes'] or 0 for d in dl_rows) / 1e6:.1f} MB")

    # ---------- text extraction (pdftotext) ----------
    n_txt = 0
    for d in dl_rows:
        if not d["file"] or not d["filename"].lower().endswith(".pdf"):
            continue
        src = os.path.join(BIN, d["file"])
        dst = os.path.join(OUT, "datasheet_text", os.path.splitext(d["filename"])[0] + ".txt")
        try:
            subprocess.run(["pdftotext", "-layout", src, dst], check=True, timeout=120,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            d["text_file"] = os.path.relpath(dst, OUT)
            n_txt += 1
        except Exception as e:
            d["text_error"] = repr(e)
    write_jsonl(os.path.join(OUT, "downloads_manifest.jsonl"), dl_rows)
    log(f"pdftotext: {n_txt}")

    # ---------- commit PDFs into git only if small enough ----------
    pdf_bytes = sum(d["bytes"] or 0 for d in dl_rows if d["file"])
    pdfs_committed = pdf_bytes <= PDF_COMMIT_MB * 1e6
    if pdfs_committed:
        for d in dl_rows:
            if d["file"]:
                shutil.copy2(os.path.join(BIN, d["file"]), os.path.join(OUT, "datasheets", d["filename"]))
    log(f"downloads total {pdf_bytes / 1e6:.1f} MB → committed to git: {pdfs_committed}")

    # ---------- images (binary dir only) ----------
    img_rows = []
    total = 0
    for i, (u, meta) in enumerate(sorted(images.items())):
        rec = {"url": u, "alt": meta["alt"], "found_on": sorted(set(meta["found_on"]))[:20],
               "found_on_count": len(set(meta["found_on"])), "status": None, "file": None, "bytes": None, "sha256": None}
        if total > MAX_IMAGE_MB * 1e6:
            rec["error"] = "skipped: image budget exceeded"
            img_rows.append(rec)
            continue
        r, err = get(u, stream=True, timeout=120)
        if r is None:
            rec["error"] = err
            img_rows.append(rec)
            continue
        rec["status"] = r.status_code
        if r.status_code == 200:
            data = r.content
            fn = fname(u)
            with open(os.path.join(BIN, "images", fn), "wb") as f:
                f.write(data)
            rec.update(file=f"images/{fn}", bytes=len(data), sha256=sha256(data))
            total += len(data)
        img_rows.append(rec)
        time.sleep(min(DELAY, 0.3))
        if (i + 1) % 100 == 0:
            log(f"images {i + 1}/{len(images)} {total / 1e6:.0f} MB")
    write_jsonl(os.path.join(OUT, "images_manifest.jsonl"), img_rows)
    log(f"images done: {sum(1 for d in img_rows if d['file'])}/{len(img_rows)} ok, {total / 1e6:.1f} MB")

    summary = {
        "crawled_at": now(), "host": HOST, "pages_total": len(pages),
        "pages_ok": sum(1 for p in pages if p["file"]), "pages_failed": [p["url"] for p in pages if not p["file"]],
        "queue_left": len(queue), "downloads_total": len(dl_rows), "downloads_ok": sum(1 for d in dl_rows if d["file"]),
        "downloads_bytes": pdf_bytes, "pdfs_committed": pdfs_committed, "pdf_text_files": n_txt,
        "images_total": len(img_rows), "images_ok": sum(1 for d in img_rows if d["file"]), "images_bytes": total,
        "external_hosts": {k: len(v) for k, v in sorted(external.items())},
        "elapsed_s": round(time.time() - T0), "user_agent": UA, "delay_s": DELAY,
    }
    with open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT, "crawl_log.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    with open(os.path.join(BIN, "pdfs_committed.flag"), "w") as f:
        f.write("1" if pdfs_committed else "0")
    log(json.dumps({k: v for k, v in summary.items() if k not in ("pages_failed", "external_hosts")}))


if __name__ == "__main__":
    main()
