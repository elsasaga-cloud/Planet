#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信长截图 OCR（Simon 与 SmartByte 的微信群聊「Peter hu、Anna (3)」）。

来源：Simon 于 2026-10-20 16:40–16:49 (+0800) 通过 GitHub 网页上传到 main 的 95 张 PNG
      （`WeChat talk with smartbyte/Weixin Image_2026-10-20_*.png` 87 张 + 仓库根目录 8 张），
      单张 1530×14 000～21 000 px 的纵向长截图（深色主题微信电脑版）。
做法：不把 ≈200 MB 的 PNG 合并进工作分支，直接从本地 .git 里 `git show origin/main:<path>` 读取字节；
      按 1500 px 高、1400 px 步长切片（100 px 重叠，重叠区只保留首次出现的行），
      RapidOCR（onnxruntime，中英混排）逐片识别，输出：
        data/wechat_smartbyte_ocr/<文件名>.json   —— 每行 {y, x, w, h, conf, text}（绝对像素坐标）
        data/wechat_smartbyte_ocr/<文件名>.txt    —— 按 y 排序的纯文本（右侧 x≥1000 的行前缀「[Simon]」）
        data/wechat_smartbyte_ocr/_progress.log   —— 进度 / 耗时 / 异常
依赖：pip install --break-system-packages pillow rapidocr-onnxruntime opencv-python-headless
用法：python3 scripts/wechat_ocr.py [--ref origin/main] [--out data/wechat_smartbyte_ocr] [--limit N]
幂等：已有同名 .json 的图片跳过（可随时中断、重跑续做）。
"""
import argparse, io, json, os, subprocess, sys, time, re
from pathlib import Path

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
REPO = Path(__file__).resolve().parent.parent
TILE_H, STEP = 1500, 1400          # 100 px 重叠
RIGHT_X = 1000                      # 右侧气泡（Simon 自己发的消息）起始 x 阈值


def list_images(ref: str):
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref], cwd=REPO,
                         capture_output=True, text=True, check=True).stdout.splitlines()
    imgs = [p for p in out if re.search(r"Weixin Image_\d{4}-\d{2}-\d{2}_\d{6}_\d{3}\.png$", p)]
    # 按截图时间排序（文件名里的 HHMMSS_mmm）——与 Simon 滚动截图的先后一致
    imgs.sort(key=lambda p: re.search(r"_(\d{6}_\d{3})\.png$", p).group(1))
    return imgs


def read_blob(ref: str, path: str) -> bytes:
    return subprocess.run(["git", "show", f"{ref}:{path}"], cwd=REPO,
                          capture_output=True, check=True).stdout


def ocr_image(ocr, img: Image.Image):
    W, H = img.size
    lines = []
    y0 = 0
    while True:
        y1 = min(y0 + TILE_H, H)
        tile = img.crop((0, y0, W, y1)).convert("RGB")
        res, _ = ocr(np.array(tile))
        keep_below = TILE_H - (TILE_H - STEP)  # 1400：重叠区（1400–1500）留给下一片
        last = y1 >= H
        for box, txt, conf in (res or []):
            xs = [p[0] for p in box]; ys = [p[1] for p in box]
            ty = min(ys)
            if not last and ty >= keep_below:
                continue
            lines.append({"y": int(ty + y0), "x": int(min(xs)), "w": int(max(xs) - min(xs)),
                          "h": int(max(ys) - min(ys)), "conf": round(float(conf), 3), "text": txt})
        if last:
            break
        y0 += STEP
    lines.sort(key=lambda r: (r["y"], r["x"]))
    return lines


def to_text(lines):
    out = []
    for r in lines:
        prefix = "[Simon] " if r["x"] >= RIGHT_X else ""
        out.append(f"{r['y']:6d} {prefix}{r['text']}")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/main")
    ap.add_argument("--out", default="data/wechat_smartbyte_ocr")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    out_dir = REPO / a.out
    out_dir.mkdir(parents=True, exist_ok=True)
    log = open(out_dir / "_progress.log", "a", encoding="utf-8")

    def L(msg):
        s = f"{time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}  {msg}"
        print(s, flush=True); log.write(s + "\n"); log.flush()

    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    imgs = list_images(a.ref)
    L(f"start: {len(imgs)} images in {a.ref}; out={out_dir}")
    done = 0
    for i, p in enumerate(imgs, 1):
        if a.limit and done >= a.limit:
            break
        base = Path(p).name[:-4]
        folder = "folder" if "/" in p else "root"
        jpath = out_dir / f"{base}.json"
        if jpath.exists():
            continue
        t0 = time.time()
        try:
            img = Image.open(io.BytesIO(read_blob(a.ref, p)))
            W, H = img.size
            lines = ocr_image(ocr, img)
            meta = {"source_path": p, "location": folder, "ref": a.ref, "width": W, "height": H,
                    "tiles": (H + STEP - 1) // STEP, "lines": lines,
                    "ocr": "rapidocr_onnxruntime", "ocr_time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            (out_dir / f"{base}.txt").write_text(to_text(lines), encoding="utf-8")
            tmp = out_dir / f"{base}.json.tmp"   # 先写临时文件再改名：中断不会留下半截 JSON（幂等跳过依赖 .json 存在）
            tmp.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
            os.replace(tmp, jpath)
            done += 1
            L(f"[{i}/{len(imgs)}] {base} {W}x{H} lines={len(lines)} {time.time()-t0:.1f}s")
        except Exception as e:  # 单张失败不影响其余
            L(f"[{i}/{len(imgs)}] {base} FAILED: {e!r}")
    L(f"finished: newly processed {done}")


if __name__ == "__main__":
    main()
