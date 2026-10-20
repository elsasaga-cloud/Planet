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
  - 连续两张截图的重叠：若后一张开头 K 条消息与前一张结尾 K 条消息文本相同（K>=2），去掉后一张的这 K 条；
  - 95 张截图实际来自 4 个会话（窗口标题行 y<60）：A 群「Peter hu、Anna (3)」/ B 群「Peter hu、扫地僧(3)」/
    C 群「STSC20250117007 (6)」（含土耳其客户 Levent KILIC）/ D 与 Peter hu 的单聊；标题缺失或乱码（'X'）的截图沿用前一张的会话；
  - 时间戳格式：「YYYY-M-D HH:MM」（往年）、「M/D HH:MM」（截图当年 = --year，默认 2026）、「Yesterday/星期/Friday HH:MM」
    （相对 --shot-date，默认 2026-10-20）；裸「HH:MM」不作为时间戳（易与 OCR 断行混淆）。
输出：docs/smartbyte/微信沟通记录_SmartByte_OCR重建.md（纯 OCR 重建稿；人工复核前不作事实引用），按会话分节、按日分段
用法：python3 scripts/wechat_transcript.py [--in data/wechat_smartbyte_ocr] [--out docs/smartbyte/微信沟通记录_SmartByte_OCR重建.md]
"""
import argparse, json, re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MEMBERS = {"Peter hu": "Peter hu", "Peterhu": "Peter hu", "Pctcr hu": "Peter hu", "Peler hu": "Peter hu",
           "Anna": "Anna", "Rot": "Rot", "Simon": "Simon", "酒歌": "酒歌", "Dora": "Dora", "扫地僧": "扫地僧",
           "Levent KILIC": "Levent KILIC", "sushen": "sushen"}
CHAT_TITLES = {"A": "群「Peter hu、Anna (3)」（Saga × SmartByte 主群：Peter hu / Anna / Rot / 酒歌 / Dora）",
               "B": "群「Peter hu、扫地僧(3)」（与 SmartByte 研发「扫地僧」的技术群）",
               "C": "群「STSC20250117007 (6)」（178 台 LT-IS6318GP-2GX16GT 大货项目群，含土耳其客户 Levent KILIC）",
               "D": "与 Peter hu 的单聊"}
import datetime as _dt
WEEKDAYS = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6,
            "星期一": 0, "星期二": 1, "星期三": 2, "星期四": 3, "星期五": 4, "星期六": 5, "星期日": 6, "星期天": 6}
TS3_RE = re.compile(r"^(\d{1,2})/(\d{1,2}) ?(\d{1,2}):(\d{2})$")                 # 1/22 14:09（截图当年，微信不显示年份）
TS4_RE = re.compile(r"^(Yesterday|昨天|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|星期[一二三四五六日天]) ?(\d{1,2}):(\d{2})$", re.I)
SHOT_DATE = _dt.date(2026, 10, 20)
SHOT_YEAR = 2026
DECOR = {"微信电脑版", "Chat History", "W", "X", "P", "Not Downloaded", "Downloaded"}
TS_RE = re.compile(r"^(\d{4})-(\d{1,2})-(\d{1,2}) (\d{1,2}):(\d{2})$")        # 2024-3-4 10:11（微信月日不补零）
TS_NOSP_RE = re.compile(r"^(\d{4})-(\d{1,2})-(\d{1,2}?)(\d{1,2}):(\d{2})$")    # OCR 丢空格：2024-10-716:14 → 日取最短
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
        m = TS_RE.match(t) or TS_NOSP_RE.match(t)
        if m and 450 <= r["x"] <= 950:
            y_, mo, d, hh, mm = m.groups()
            if 1 <= int(mo) <= 12 and 1 <= int(d) <= 31 and int(hh) <= 23:
                ts = f"{y_}-{int(mo):02d}-{int(d):02d} {int(hh):02d}:{mm}"; cur = None; continue
        if TS2_RE.match(t) and 450 <= r["x"] <= 950:
            ts = t; cur = None; continue
        m3 = TS3_RE.match(t)
        if m3 and 450 <= r["x"] <= 950:
            mo, d, hh, mm = m3.groups()
            if 1 <= int(mo) <= 12 and 1 <= int(d) <= 31 and int(hh) <= 23:
                ts = f"{SHOT_YEAR}-{int(mo):02d}-{int(d):02d} {int(hh):02d}:{mm}"; cur = None; continue
        m4 = TS4_RE.match(t)
        if m4 and 450 <= r["x"] <= 950:
            w, hh, mm = m4.groups(); wl = w.lower()
            if wl in ("yesterday", "昨天"):
                day = SHOT_DATE - _dt.timedelta(days=1)
            else:
                back = (SHOT_DATE.weekday() - WEEKDAYS[wl]) % 7 or 7
                day = SHOT_DATE - _dt.timedelta(days=back)
            ts = f"{day.isoformat()} {int(hh):02d}:{mm}"; cur = None; continue
        if r["y"] < 60 and (("(" in t and ")" in t) or t.strip() in ("Peter hu", "X")):  # 窗口标题行
            continue
        side = "L" if r["x"] < LEFT_MAX_X else "R"  # 左侧气泡文字左缘恒在 x≈100；右侧气泡右对齐、宽窄不一，左缘 600–1450
        if side == "L" and t in MEMBERS and r["w"] < 200:
            speaker = MEMBERS[t]; cur = None; continue
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


def chat_of(meta, prev_chat):
    """按窗口标题行（y<60）判断会话；缺失/乱码则沿用前一张"""
    for r in sorted(meta["lines"], key=lambda r: r["y"]):
        if r["y"] >= 60:
            break
        t = r["text"].strip()
        if "Anna" in t:
            return "A"
        if "扫地僧" in t:
            return "B"
        if t.startswith("STSC"):
            return "C"
        if t == "Peter hu":
            return "D"
    return prev_chat or "A"


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
    ap.add_argument("--year", type=int, default=2026, help="「M/D HH:MM」格式时间戳所属年份（截图当年）")
    ap.add_argument("--shot-date", default="2026-10-20", help="截图日期（解释 Yesterday / 星期 / 裸时间）")
    a = ap.parse_args()
    global SHOT_YEAR, SHOT_DATE
    SHOT_YEAR = a.year; SHOT_DATE = _dt.date.fromisoformat(a.shot_date)
    imgs = load(REPO / a.inp)
    chats = {k: [] for k in CHAT_TITLES}      # chat -> msgs
    prev_by_chat = {k: [] for k in CHAT_TITLES}
    stats, prev_chat = [], None
    for name, meta in imgs:
        chat = chat_of(meta, prev_chat); prev_chat = chat
        msgs = parse_image(name, meta)
        prev = prev_by_chat[chat]
        msgs, dropped = dedup_overlap(prev, msgs) if prev else (msgs, 0)
        stats.append((name, chat, len(meta["lines"]), len(msgs), dropped))
        chats[chat].extend(msgs); prev_by_chat[chat] = msgs or prev
    # 向后填充时间戳（截图开头尚未出现时间戳的消息沿用同一会话上一张的最后时间）
    total = 0
    for chat, all_msgs in chats.items():
        last_ts = None
        for m in all_msgs:
            if m["ts"]:
                last_ts = m["ts"]
            else:
                m["ts"] = last_ts or "（时间未识别）"
        total += len(all_msgs)
    out = [f"# SmartByte 微信沟通记录 OCR 重建稿（4 个会话）\n",
           f"> 来源：Simon 2026-10-20 上传到 main 的 {len(imgs)} 张长截图（见 `scripts/wechat_ocr.py` 头注）；本稿由 OCR 自动重建，"
           f"**未经人工复核，不得直接作为事实引用**；引用前回看原图（文件名见每段末尾的 ⟨img⟩）。\n",
           f"> 消息总数 {total}；每个会话内按截图顺序排列，时间戳为聊天内原时间（+0800）；"
           f"「M/D HH:MM」格式按 {SHOT_YEAR} 年、相对日期按截图日 {SHOT_DATE} 换算。\n"]
    for chat in CHAT_TITLES:
        all_msgs = chats[chat]
        if not all_msgs:
            continue
        n_img = sum(1 for s_ in stats if s_[1] == chat)
        out.append(f"\n## 会话 {chat}：{CHAT_TITLES[chat]} — {n_img} 张截图，{len(all_msgs)} 条\n")
        cur_day = None
        for m in all_msgs:
            day = m["ts"][:10]
            if day != cur_day:
                out.append(f"\n### {day}\n"); cur_day = day
            tag = " 📎" if m.get("attach") else ""
            out.append(f"- **{m['ts'][11:] if len(m['ts']) > 10 else m['ts']} {m['speaker']}**：{m['text']}{tag} ⟨{m['img'][-10:-4]}⟩")
    out.append("\n\n## 重建统计（每张截图：会话，OCR 行数 → 消息数，去重叠条数）\n")
    for name, chat, nl, nm, dr in stats:
        out.append(f"- {name}: 会话 {chat}，{nl} 行 → {nm} 条（去重叠 {dr}）")
    all_msgs = [m for k in CHAT_TITLES for m in chats[k]]
    Path(REPO / a.out).parent.mkdir(parents=True, exist_ok=True)
    (REPO / a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"images {len(imgs)}  messages {len(all_msgs)}  -> {a.out}")


if __name__ == "__main__":
    main()
