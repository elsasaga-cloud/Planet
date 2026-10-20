#!/usr/bin/env python3
"""SmartByte 官网整站归档器（T15）。

在 GitHub Actions 运行器上执行（Arena 沙箱对 smartbyte-switch.com 无出网权限）。
职责只有一个：把站点上**所有**可达页面、附件（规格书等）、图片原样抓下来并写清单；
解析/整理在仓库内另做（scripts/smartbyte_crawl/build.py）。

用法：python crawl.py <OUT_dir(入 git)> <BIN_dir(二进制，不入 git)>
环境变量：MAX_PAGES(默认 1500) DELAY(默认 0.8s) MAX_IMAGE_MB(默认 600) PDF_COMMIT_MB(默认 60)
          TIME_BUDGET_MIN(默认 140：墙钟预算，分钟；到点优雅收尾，保证后续 zip / 上传 / 提交步骤能跑)
          CRAWL_HOST / CRAWL_SCHEME（仅本地自测用，默认 www.smartbyte-switch.com / https）

v2（2026-10-20，Actions 运行 #1 在 170 分钟作业上限被杀、颗粒无收之后）：
  ① 墙钟预算：页面阶段最多用预算的 55%，附件阶段累计 85%，图片阶段用满 100%；到点即停、照常写清单与汇总并以 0 退出，
     这样工作流后面的 zip / upload-artifact / commit / release 步骤一定执行，已抓到的东西一定落地。
  ② 断点续抓：OUT 目录里的 pages_manifest.jsonl / downloads_manifest.jsonl / images_manifest.jsonl + crawl_state.json
     随上一轮提交回分支；下一轮（workflow_dispatch 或再推一次本文件）从 crawl_state.json 的队列继续，已抓成功的 URL 不重抓，
     直到 summary.json 的 complete=true。
  ③ 清单每 25 页 / 20 个附件 / 100 张图写一次盘（不是只在最后写），日志跨轮追加。
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

HOST = os.environ.get("CRAWL_HOST", "www.smartbyte-switch.com")
SCHEME = os.environ.get("CRAWL_SCHEME", "https")
BASE = f"{SCHEME}://{HOST}/"
HOSTS_OK = {HOST.lower(), HOST[4:].lower() if HOST.lower().startswith("www.") else ("www." + HOST).lower()}
OUT = sys.argv[1] if len(sys.argv) > 1 else "data/smartbyte_site_raw"
BIN = sys.argv[2] if len(sys.argv) > 2 else "crawl_bin"
MAX_PAGES = int(os.environ.get("MAX_PAGES", "1500"))
DELAY = float(os.environ.get("DELAY", "0.8"))
MAX_IMAGE_MB = float(os.environ.get("MAX_IMAGE_MB", "600"))
PDF_COMMIT_MB = float(os.environ.get("PDF_COMMIT_MB", "60"))
TIME_BUDGET_MIN = float(os.environ.get("TIME_BUDGET_MIN", "140"))
UA = "Mozilla/5.0 (compatible; SagaTelecom-site-archiver/1.0; +https://sagatele.com)"

ASSET_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp", ".css", ".js", ".woff", ".woff2",
             ".ttf", ".eot", ".otf", ".mp4", ".webm", ".mp3", ".map", ".json")
FILE_EXT = (".pdf", ".zip", ".rar", ".7z", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".bin", ".img", ".exe")
IMG_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico")

S = requests.Session()
S.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.5"})
T0 = time.time()
LOG = []
RUN_ID = os.environ.get("GITHUB_RUN_NUMBER") or datetime.now(timezone.utc).strftime("local-%Y%m%d%H%M%S")

# 阶段预算（占总预算比例）：页面 55% → 附件累计 85% → 图片 100%
PHASE_CAP = {"pages": 0.55, "downloads": 0.85, "images": 1.0}


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    LOG.append(line)


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def elapsed():
    return time.time() - T0


def over_budget(phase):
    """该阶段是否已用完预算。到点只记一次日志。"""
    cap = TIME_BUDGET_MIN * 60 * PHASE_CAP[phase]
    if elapsed() >= cap:
        if not getattr(over_budget, "_said", {}).get(phase):
            over_budget._said = getattr(over_budget, "_said", {})
            over_budget._said[phase] = True
            log(f"TIME BUDGET: phase '{phase}' cap {cap / 60:.0f} min reached at {elapsed() / 60:.1f} min → graceful stop of this phase")
        return True
    return False


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def found(d, u):
    """记录「在哪页发现」：最多留 20 个样本 + 计数（页眉 logo 之类会出现在每一页，不能把 1500 个 URL 全存进状态文件）。"""
    d["n"] = d.get("n", 0) + 1
    if u not in d["found_on"] and len(d["found_on"]) < 20:
        d["found_on"].append(u)
    return d


def norm(u, base=BASE):
    try:
        u = urljoin(base, u.strip())
        p = urlparse(u)
    except Exception:
        return None
    if p.scheme not in ("http", "https"):
        return None
    if p.netloc.lower() not in HOSTS_OK:
        return None
    path = p.path or "/"
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not k.lower().startswith("utm")]
    return urlunparse((SCHEME, HOST, path, "", urlencode(q), ""))


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


def get(u, stream=False, timeout=45):
    last = None
    for i in range(3):
        try:
            r = S.get(u, timeout=timeout, stream=stream, allow_redirects=True)
            if r.status_code in (403, 429, 500, 502, 503, 504):
                last = f"HTTP {r.status_code}"
                time.sleep(3 * (i + 1))
                continue
            return r, None
        except requests.RequestException as e:
            last = repr(e)
            time.sleep(3 * (i + 1))
    return None, last


def write_jsonl(path, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except Exception:
                    pass
    return rows


def save_state(path, queue, seen, downloads, images, external, phase, runs):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"saved_at": now(), "phase": phase, "queue": list(queue), "seen": sorted(seen),
                   "downloads": downloads, "images": images,
                   "external": {k: sorted(v) for k, v in external.items()}, "runs": runs},
                  f, ensure_ascii=False)
    os.replace(tmp, path)


def main():
    for d in ("html", "datasheet_text", "datasheets"):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
    for d in ("downloads", "images"):
        os.makedirs(os.path.join(BIN, d), exist_ok=True)
    p_pages = os.path.join(OUT, "pages_manifest.jsonl")
    p_dl = os.path.join(OUT, "downloads_manifest.jsonl")
    p_img = os.path.join(OUT, "images_manifest.jsonl")
    p_state = os.path.join(OUT, "crawl_state.json")

    # ---------- resume? ----------
    state = None
    if os.path.exists(p_state):
        try:
            with open(p_state, encoding="utf-8") as f:
                state = json.load(f)
        except Exception as e:
            log(f"crawl_state.json unreadable ({e!r}) → fresh start")
            state = None
    runs = (state or {}).get("runs", [])
    runs.append({"run": RUN_ID, "started": now(), "resumed": bool(state), "budget_min": TIME_BUDGET_MIN,
                 "max_pages": MAX_PAGES, "delay_s": DELAY})
    log(f"run {RUN_ID} start; resume={bool(state)}; budget {TIME_BUDGET_MIN} min; max_pages {MAX_PAGES}; delay {DELAY}s")

    pages = read_jsonl(p_pages) if state else []
    pages_by_url = {p["url"]: p for p in pages}
    dl_prev = read_jsonl(p_dl) if state else []
    img_prev = read_jsonl(p_img) if state else []

    if state:
        queue = deque(state.get("queue", []))
        seen = set(state.get("seen", []))
        downloads = state.get("downloads", {})
        images = state.get("images", {})
        external = {k: set(v) for k, v in state.get("external", {}).items()}
        # 上一轮抓失败（网络 / 5xx / 非 404）的页面再试一次
        retry = [p["url"] for p in pages if not p.get("file") and p.get("status") != 404
                 and not (p.get("error") or "").startswith("binary-at-page-url")]
        for u in retry:
            if u not in queue:
                queue.appendleft(u)
        for u in retry:
            pages_by_url.pop(u, None)
        pages = [p for p in pages if p["url"] in pages_by_url]
        log(f"resume: pages_done={len(pages)} queue={len(queue)} (retry {len(retry)}) downloads={len(downloads)} images={len(images)}")
    else:
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
        queue = deque(seeds)
        seen = set(seeds)
        downloads = {}  # url -> {found_on: [...]}
        images = {}  # url -> {found_on: [...], alt: ...}
        external = {}

    def checkpoint(phase):
        write_jsonl(p_pages, pages)
        save_state(p_state, queue, seen, downloads, images, external, phase, runs)

    # ---------- BFS over pages ----------
    n_new_pages = 0
    pages_stop = None
    while queue:
        if len(pages) >= MAX_PAGES:
            pages_stop = f"MAX_PAGES {MAX_PAGES} reached (queue_left {len(queue)})"
            break
        if over_budget("pages"):
            pages_stop = f"time budget (queue_left {len(queue)})"
            break
        u = queue.popleft()
        if u in pages_by_url and pages_by_url[u].get("file"):
            continue
        r, err = get(u)
        time.sleep(DELAY)
        rec = {"url": u, "fetched_at": now(), "run": RUN_ID, "status": None, "final_url": None, "content_type": None,
               "file": None, "bytes": None, "sha256": None, "title": None, "error": err}
        pages.append(rec)
        pages_by_url[u] = rec
        n_new_pages += 1
        if r is None:
            log(f"FAIL {u}: {err}")
        else:
            rec.update(status=r.status_code, final_url=r.url, content_type=r.headers.get("content-type"))
            ct = (rec["content_type"] or "").lower()
            if r.status_code != 200:
                log(f"HTTP {r.status_code} {u}")
            elif "html" not in ct and "xml" not in ct and "text" not in ct:
                # binary served at a page URL → treat as download
                found(downloads.setdefault(u, {"found_on": []}), "(direct)")
                rec["error"] = "binary-at-page-url → downloads"
            else:
                if r.encoding is None or r.encoding.lower() in ("iso-8859-1", "latin-1"):
                    r.encoding = r.apparent_encoding or "utf-8"
                html = r.text
                name = fname(u, ".html")
                with open(os.path.join(OUT, "html", name), "w", encoding="utf-8") as f:
                    f.write(html)
                m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
                rec.update(file=f"html/{name}", bytes=len(html.encode("utf-8")), sha256=sha256(html.encode("utf-8")),
                           title=re.sub(r"\s+", " ", m.group(1)).strip() if m else None)
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
                        found(downloads.setdefault(n, {"found_on": []}), u)
                    elif k == "image":
                        found(images.setdefault(n, {"found_on": [], "alt": ""}), u)
                for m2 in re.finditer(r"""<img[^>]+?(?:src|data-src|data-original)\s*=\s*["']([^"']+)["'][^>]*>""", html, flags=re.I):
                    n = norm(m2.group(1), r.url)
                    if n is None:
                        continue
                    alt = re.search(r"""alt\s*=\s*["']([^"']*)""", m2.group(0), flags=re.I)
                    d = found(images.setdefault(n, {"found_on": [], "alt": ""}), u)
                    if alt and alt.group(1) and not d["alt"]:
                        d["alt"] = alt.group(1)
                for m3 in re.finditer(r"""url\(\s*["']?([^"')]+?)["']?\s*\)""", html, flags=re.I):
                    n = norm(m3.group(1), r.url)
                    if n and kind(n) == "image":
                        found(images.setdefault(n, {"found_on": [], "alt": ""}), u)
        if n_new_pages % 25 == 0:
            log(f"pages {len(pages)} (+{n_new_pages} this run) queue {len(queue)} downloads {len(downloads)} images {len(images)} "
                f"elapsed {elapsed() / 60:.1f} min")
            checkpoint("pages")
    if pages_stop is None:
        pages_stop = "complete (queue empty)"
    log(f"BFS stop: {pages_stop}; pages={len(pages)} (+{n_new_pages}) downloads={len(downloads)} images={len(images)}")
    checkpoint("downloads")

    # ---------- downloads (datasheets etc.) ----------
    dl_rows = [d for d in dl_prev if d.get("file")]  # 上一轮已成功的保留（二进制在上一轮的 Release / 产物里；PDF 入库时在 datasheets/）
    done_dl = {d["url"] for d in dl_rows}
    used = {d["filename"]: d["sha256"] for d in dl_rows if d.get("filename")}
    todo_dl = [(u, meta) for u, meta in sorted(downloads.items()) if u not in done_dl]
    dl_stop = None
    n_new_dl = 0
    for i, (u, meta) in enumerate(todo_dl):
        if over_budget("downloads"):
            dl_stop = f"time budget ({len(todo_dl) - i} left)"
            break
        r, err = get(u, stream=True, timeout=120)
        rec = {"url": u, "found_on": sorted(set(meta["found_on"])), "found_on_count": meta.get("n", len(meta["found_on"])),
               "fetched_at": now(), "run": RUN_ID, "status": None, "content_type": None, "filename": None, "file": None, "bytes": None, "sha256": None, "error": err}
        n_new_dl += 1
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
        if n_new_dl % 20 == 0:
            log(f"downloads {i + 1}/{len(todo_dl)} elapsed {elapsed() / 60:.1f} min")
            write_jsonl(p_dl, dl_rows)
    if dl_stop is None:
        dl_stop = "complete"
    write_jsonl(p_dl, dl_rows)
    log(f"downloads stop: {dl_stop}; ok {sum(1 for d in dl_rows if d['file'])}/{len(dl_rows)} (+{n_new_dl} this run), "
        f"{sum(d['bytes'] or 0 for d in dl_rows) / 1e6:.1f} MB")

    # ---------- text extraction (pdftotext) ----------
    n_txt = 0
    for d in dl_rows:
        if not d["file"] or not (d.get("filename") or "").lower().endswith(".pdf"):
            continue
        dst = os.path.join(OUT, "datasheet_text", os.path.splitext(d["filename"])[0] + ".txt")
        if d.get("text_file") and os.path.exists(dst):
            n_txt += 1
            continue
        src = os.path.join(BIN, d["file"])
        if not os.path.exists(src):
            # 上一轮抓的 PDF：若已入库到 datasheets/ 则从那里抽文本
            alt = os.path.join(OUT, "datasheets", d["filename"])
            if os.path.exists(alt):
                src = alt
            else:
                continue
        try:
            subprocess.run(["pdftotext", "-layout", src, dst], check=True, timeout=120,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            d["text_file"] = os.path.relpath(dst, OUT)
            d.pop("text_error", None)
            n_txt += 1
        except Exception as e:
            d["text_error"] = repr(e)
    write_jsonl(p_dl, dl_rows)
    log(f"pdftotext: {n_txt}")

    # ---------- commit PDFs into git only if small enough ----------
    pdf_bytes = sum(d["bytes"] or 0 for d in dl_rows if d["file"])
    pdfs_committed = pdf_bytes <= PDF_COMMIT_MB * 1e6
    if pdfs_committed:
        for d in dl_rows:
            if d["file"]:
                src = os.path.join(BIN, d["file"])
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(OUT, "datasheets", d["filename"]))
    log(f"downloads total {pdf_bytes / 1e6:.1f} MB → committed to git: {pdfs_committed}")
    save_state(p_state, queue, seen, downloads, images, external, "images", runs)

    # ---------- images (binary dir only) ----------
    img_rows = [d for d in img_prev if d.get("file")]
    done_img = {d["url"] for d in img_rows}
    todo_img = [(u, meta) for u, meta in sorted(images.items()) if u not in done_img]
    total = 0
    img_stop = None
    n_new_img = 0
    for i, (u, meta) in enumerate(todo_img):
        rec = {"url": u, "alt": meta["alt"], "found_on": sorted(set(meta["found_on"]))[:20],
               "found_on_count": meta.get("n", len(meta["found_on"])), "run": RUN_ID, "status": None, "file": None, "bytes": None, "sha256": None}
        if total > MAX_IMAGE_MB * 1e6:
            rec["error"] = "skipped: image budget exceeded"
            img_rows.append(rec)
            continue
        if over_budget("images"):
            img_stop = f"time budget ({len(todo_img) - i} left)"
            break
        r, err = get(u, stream=True, timeout=120)
        n_new_img += 1
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
        if n_new_img % 100 == 0:
            log(f"images {i + 1}/{len(todo_img)} {total / 1e6:.0f} MB elapsed {elapsed() / 60:.1f} min")
            write_jsonl(p_img, img_rows)
    if img_stop is None:
        img_stop = "complete"
    write_jsonl(p_img, img_rows)
    log(f"images stop: {img_stop}; ok {sum(1 for d in img_rows if d['file'])}/{len(img_rows)} (+{n_new_img} this run), {total / 1e6:.1f} MB this run")

    # ---------- summary ----------
    images_left = sum(1 for u, _ in todo_img if u not in {d["url"] for d in img_rows})
    complete = (pages_stop.startswith("complete") and dl_stop == "complete" and img_stop == "complete")
    runs[-1].update(ended=now(), elapsed_s=round(elapsed()), pages_new=n_new_pages, downloads_new=n_new_dl,
                    images_new=n_new_img, pages_stop=pages_stop, downloads_stop=dl_stop, images_stop=img_stop)
    summary = {
        "crawled_at": now(), "host": HOST, "complete": complete,
        "pages_total": len(pages), "pages_ok": sum(1 for p in pages if p["file"]),
        "pages_failed": [p["url"] for p in pages if not p["file"]],
        "pages_stop": pages_stop, "queue_left": len(queue),
        "downloads_total": len(dl_rows), "downloads_ok": sum(1 for d in dl_rows if d["file"]),
        "downloads_left": max(0, len(todo_dl) - n_new_dl), "downloads_stop": dl_stop,
        "downloads_bytes": pdf_bytes, "pdfs_committed": pdfs_committed, "pdf_text_files": n_txt,
        "images_total": len(img_rows), "images_ok": sum(1 for d in img_rows if d["file"]),
        "images_left": images_left, "images_stop": img_stop, "images_bytes_this_run": total,
        "external_hosts": {k: len(v) for k, v in sorted(external.items())},
        "runs": runs, "elapsed_s": round(elapsed()), "user_agent": UA, "delay_s": DELAY,
        "time_budget_min": TIME_BUDGET_MIN,
        "how_to_continue": None if complete else "未抓完：在 GitHub Actions 页对 SmartByte site archive 点 Run workflow（或再推一次 crawl.py），会从 crawl_state.json 续抓",
    }
    with open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT, "crawl_log.txt"), "a", encoding="utf-8") as f:
        f.write(f"===== run {RUN_ID} =====\n" + "\n".join(LOG) + "\n")
    with open(os.path.join(BIN, "pdfs_committed.flag"), "w") as f:
        f.write("1" if pdfs_committed else "0")
    save_state(p_state, queue, seen, downloads, images, external, "done" if complete else "images", runs)
    log(json.dumps({k: v for k, v in summary.items() if k not in ("pages_failed", "external_hosts", "runs")}, ensure_ascii=False))
    log("COMPLETE" if complete else "INCOMPLETE → re-run to continue")


if __name__ == "__main__":
    main()
