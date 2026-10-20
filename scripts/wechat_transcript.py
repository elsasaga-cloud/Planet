#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 scripts/wechat_ocr.py 的逐行 OCR 结果（data/wechat_smartbyte_ocr/*.json）重建为按时间排列的聊天记录。

规则（基于微信电脑版深色主题长截图的版式）：
  - 居中的「YYYY-MM-DD HH:MM」行（x 在 500–900）= 时间戳分隔；
  - 左侧 x<1000 且文本为已知成员名（Peter hu / Anna / Rot …）的短行 = 发言人标签，其后的左侧行归该发言人；
  - 左缘 x>=300 的行 = 右侧气泡 = Simon 自己发的消息（左侧气泡文字左缘恒在 x≈100；居中时间戳 / 系统提示先剔除）；
  - 行间距 <= 34 px 且同侧的连续行合并为一条消息（同一气泡内多行）；
  - 「微信电脑版」「Not Downloaded」「Chat History」「W」等 = 附件 / 转发卡片的装饰字样，保留为 [附件] 标记；
  - 连续两张截图的重叠：若后一张开头 K 条消息与前一张结尾 K 条消息文本相同（K>=2），去掉后一张的这 K 条。
输出：docs/smartbyte/微信沟通记录_SmartByte_OCR重建.md（纯 OCR 重建稿；人工复核前不作事实引用）
用法：python3 scripts/wechat_transcript.py [--in data/wechat_smartbyte_ocr] [--out docs/smartbyte/微信沟通记录_SmartByte_OCR重建.md]
"""
import argparse, json, re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MEMBERS = {"Peter hu", "Peterhu", "Anna", "Rot", "Simon"}
DECOR = {"微信电脑版", "Chat History", "W", "X", "P", "Not Downloaded", "Downloaded"}
TS_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\d{1,2}:\d{2})$")
TS2_RE = re.compile(r"^(昨天|今天|星期[一二三四五六日]|\d{1,2}月\d{1,2}日) ?(\d{1,2}:\d{2})$")
RIGHT_X = 1000
LEFT_MAX_X = 300                    # 左侧气泡（头像 25–70 px，文字 ≈100 px）；居中的时间戳 / 系统提示先行剔除
GAP = 34


def load(in_dir: Path):
    files = sorted(in_dir.glob("Weixin Image_*.json"),
                   key=lambda p: re.search(r"_(\d{6}_\d{3})\.json$", p.name).group(1))
    return [(p.name[:-5], json.loads(p.read_text(encoding="utf-8"))) for p in files]


def parse_image(name, meta):
    """返回 [{'ts','speaker','side','text','y','img'}]（ts 只在遇到时间戳行后更新）"""
    msgs, ts, speaker = [], None, None
    cur = None
    for r in sorted(meta["lines"], key=lambda r: (r["y"], r["x"])):
        t = r["text"].strip()
        if not t:
            continue
        m = TS_RE.match(t) or TS2_RE.match(t)
        if m and 450 <= r["x"] <= 950:
            ts = t; cur = None; continue
        if r["y"] < 60 and ("(" in t and ")" in t):  # 窗口标题「Peter hu、Anna (3)」
            continue
        side = "L" if r["x"] < LEFT_MAX_X else "R"  # 左侧气泡文字左缘恒在 x≈100；右侧气泡右对齐、宽窄不一，左缘 600–1450
        if side == "L" and t in MEMBERS and r["w"] < 200:
            speaker = t; cur = None; continue
        if "invited you" in t or ("邀请" in t and "加入" in t) or "recalled a message" in t or "撤回了一条消息" in t:
            msgs.append({"ts": ts, "speaker": "系统", "side": "C", "text": t, "y": r["y"], "img": name}); cur = None; continue
        if t in DECOR:
            if cur is not None and side == cur["side"]:
                cur["attach"] = True
            continue
        # 同一气泡内的后续行：左缘对齐（±15 px）且行距 <= GAP —— 不论该行自身宽窄，沿用气泡的一侧
        same_bubble = cur is not None and r["y"] - cur["y_end"] <= GAP and abs(r["x"] - cur["x0"]) <= 15
        if same_bubble:
            side = cur["side"]
        who = "Simon" if side == "R" else (speaker or "？")
        if cur is not None and cur["side"] == side and cur["speaker"] == who and r["y"] - cur["y_end"] <= GAP:
            cur["text"] += ("" if re.search(r"[\u4e00-\u9fff，。、；：]$", cur["text"]) else " ") + t
            cur["y_end"] = r["y"] + r["h"]
        else:
            cur = {"ts": ts, "speaker": who, "side": side, "text": t, "y": r["y"], "x0": r["x"],
                   "y_end": r["y"] + r["h"], "img": name}
            msgs.append(cur)
    return msgs


def norm(s):
    return re.sub(r"\s+", "", s)


def dedup_overlap(prev, nxt):
    """去掉 nxt 开头与 prev 结尾重复的消息（按归一化文本比对，最长匹配，至少 2 条）"""
    a = [norm(m["text"]) for m in prev]; b = [norm(m["text"]) for m in nxt]
    best = 0
    for k in range(min(len(a), len(b), 40), 1, -1):
        if a[-k:] == b[:k]:
            best = k; break
    return nxt[best:], best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default="data/wechat_smartbyte_ocr")
    ap.add_argument("--out", default="docs/smartbyte/微信沟通记录_SmartByte_OCR重建.md")
    a = ap.parse_args()
    imgs = load(REPO / a.inp)
    all_msgs, prev, stats = [], [], []
    for name, meta in imgs:
        msgs = parse_image(name, meta)
        msgs, dropped = dedup_overlap(prev, msgs) if prev else (msgs, 0)
        stats.append((name, len(meta["lines"]), len(msgs), dropped))
        all_msgs.extend(msgs); prev = msgs or prev
    # 向后填充时间戳（截图开头尚未出现时间戳的消息沿用上一张的最后时间）
    last_ts = None
    for m in all_msgs:
        if m["ts"]:
            last_ts = m["ts"]
        else:
            m["ts"] = last_ts or "（时间未识别）"
    out = [f"# SmartByte 微信群聊「Peter hu、Anna (3)」OCR 重建稿\n",
           f"> 来源：Simon 2026-10-20 上传到 main 的 {len(imgs)} 张长截图（见 `scripts/wechat_ocr.py` 头注）；本稿由 OCR 自动重建，"
           f"**未经人工复核，不得直接作为事实引用**；引用前回看原图（文件名见每段末尾的 ⟨img⟩）。\n",
           f"> 消息总数 {len(all_msgs)}；按截图顺序排列，时间戳为聊天内原时间（+0800）。\n"]
    cur_day = None
    for m in all_msgs:
        day = m["ts"][:10]
        if day != cur_day:
            out.append(f"\n## {day}\n"); cur_day = day
        tag = " 📎" if m.get("attach") else ""
        out.append(f"- **{m['ts'][11:] if len(m['ts']) > 10 else m['ts']} {m['speaker']}**：{m['text']}{tag} ⟨{m['img'][-10:-4]}⟩")
    out.append("\n\n## 重建统计（每张截图：OCR 行数 → 消息数，去重叠条数）\n")
    for name, nl, nm, dr in stats:
        out.append(f"- {name}: {nl} 行 → {nm} 条（去重叠 {dr}）")
    Path(REPO / a.out).parent.mkdir(parents=True, exist_ok=True)
    (REPO / a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"images {len(imgs)}  messages {len(all_msgs)}  -> {a.out}")


if __name__ == "__main__":
    main()
