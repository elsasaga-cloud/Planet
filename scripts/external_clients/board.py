# -*- coding: utf-8 -*-
"""跟进总台 + 发送包生成器（只读 JSON，勿手改产物）。
产物：
  docs/跟进总台.md            —— 一页：本周要发 / External 已研究 XA 的下一动作 / S 箱群发来信 / Saga 在谈（链到跟进日历）/ 等回·不动统计
  docs/发送包/<ISO 周>.md      —— 本周窗口内的全部英文稿（Simon 复制发送；Agent 不发）
用法：python3 scripts/external_clients/board.py [--date 2026-10-27]
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, ROOT  # noqa: E402
from research_store import all_cards  # noqa: E402

REPOS = {'E': ('Edgecore', 'edgecore.json'), 'M': ('mikrotik-info', 'mikrotik.json'), 'C': ('CCTV-PoE', 'cctv.json')}
WINDOW_BOX = {'US': 'S 箱', 'CA': 'S 箱', 'GB': 'S 箱', 'DE': 'S 箱', 'TR': 'S 箱'}
MACHINE = re.compile(r'auto ?repl|autoreply|réponse automatique|confirmare|\(#\d+\)|\[VH#|MSD-\d+|verification code|unsubscribe|out of office', re.I)


def load_records():
    out = {}
    for letter, (repo, fn) in REPOS.items():
        p = os.path.join(DATA, fn)
        d = json.load(open(p, encoding='utf-8'))
        recs = d['records'] if isinstance(d, dict) and 'records' in d else d
        if isinstance(recs, dict):
            for v in recs.values():
                if isinstance(v, list) and v and isinstance(v[0], dict) and 'code' in v[0]:
                    recs = v
                    break
        for r in recs:
            out[r['code']] = (repo, r)
    return out


def iso_week(d):
    y, w, _ = d.isocalendar()
    return f'{y}-W{w:02d}'


def week_range(d):
    mon = d - dt.timedelta(days=d.weekday())
    return mon, mon + dt.timedelta(days=6)


def parse_when(s):
    s = (s or '').strip()
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.match(r'(\d{4})-(\d{2})$', s)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), 1)
    return None


def weekday_zh(d):
    return '周' + '一二三四五六日'[d.weekday()]


def md_path(repo, code, grade):
    folder = os.path.join(ROOT, 'External Clients', repo, grade)
    if os.path.isdir(folder):
        for fn in os.listdir(folder):
            if fn.startswith(code + '-'):
                return f'External Clients/{repo}/{grade}/{fn}'
    return f'External Clients/{repo}/{grade}/{code}-*.md'


def s_box_replies():
    p = os.path.join(ROOT, 'data', 'gmail_s', '2026-09_10群发名单_未入库.csv')
    if not os.path.exists(p):
        return []
    rows = list(csv.DictReader(open(p, encoding='utf-8-sig')))
    out = []
    for r in rows:
        try:
            n = int(r.get('来信') or 0)
        except ValueError:
            n = 0
        if n > 0:
            subj = r.get('最后主题') or ''
            kind = '机器回执' if MACHINE.search(subj) else '待核（可能真人）'
            if r.get('域名') in ('firstrade.com', 'email.adobe.com', 'smartbyte.com.cn', 'ymhso.com', 'thomasnet.com'):
                kind = '无关（供应商/平台/私务）'
            out.append((r.get('邮箱'), r.get('域名'), r.get('最后'), subj, kind))
    return out


def saga_now_rows():
    """从 docs/跟进日历_2026-11.md 的「现在」段抽表格行（只读，不改口径）。"""
    p = os.path.join(ROOT, 'docs', '跟进日历_2026-11.md')
    if not os.path.exists(p):
        return [], ''
    lines = open(p, encoding='utf-8').read().splitlines()
    rows, in_now = [], False
    head = ''
    for ln in lines:
        if ln.startswith('## 现在'):
            in_now = True
            head = ln.strip('# ').strip()
            continue
        if in_now and ln.startswith('## ') and not ln.startswith('## 现在'):
            break
        if in_now and ln.startswith('| S'):
            cells = [c.strip() for c in ln.strip('|').split('|')]
            if len(cells) >= 7:
                rows.append(cells)
    return rows, head



def write_package(wk, mon, sun, items_wk, rest, now):
    pk = [f'# 发送包 {wk}（{mon}～{sun}）', '',
          f'生成：{now}（自动，勿手改；源 = `data/external_clients/research/*.json`）。**Simon 复制发送；Agent 不发信。** 每封一问；发前把称呼里的人名核一眼；价格快照 2026-10-27、15 天有效，过期先问我更新。',
          '', f'共 **{len(items_wk)}** 封：' + '；'.join(f'{d} {weekday_zh(d)} {n} 封' for d, n in sorted({i["date"]: 0 for i in items_wk}.items()) for n in [sum(1 for x in items_wk if x["date"] == d)]), '']
    by_day = {}
    for i in items_wk:
        by_day.setdefault((i['date'], i['window']), []).append(i)
    for (d, w), lst in sorted(by_day.items()):
        pk.append(f'## {d} {weekday_zh(d)} · {w} · {len(lst)} 封')
        pk.append('')
        pk.append('| # | 户 | 公司 | 国 | 动作 | 收件 | 从哪个箱 | 主题 |')
        pk.append('|---|---|---|---|---|---|---|---|')
        for k, i in enumerate(lst, 1):
            pk.append(f"| {k} | {i['code']} | {i['name']} | {i['iso']} | {i['action']} | `{i['email']}` | {WINDOW_BOX.get(i['iso'], 'S 箱')} | {i['draft']['subject']} |")
        pk.append('')
        for k, i in enumerate(lst, 1):
            pk.append(f"### {k}. {i['code']} · {i['name']} · {i['action']}")
            pk.append('')
            pk.append(f"- 收件：`{i['email']}` ｜ 角度：{i['angle']} ｜ 档案：`{i['md']}`")
            if i['notes']:
                pk.append(f"- 注意：{i['notes']}")
            pk.append('')
            pk.append('```text')
            pk.append('To: ' + i['email'])
            pk.append('Subject: ' + i['draft']['subject'])
            pk.append('')
            pk.append(i['draft']['body'])
            pk.append('```')
            pk.append('')
    if rest:
        pk.append('## 不在本周窗口（已有稿，到期进下一个发送包）')
        pk.append('')
        pk.append('| 户 | 公司 | 国 | 动作 | 时点 | 窗口 |')
        pk.append('|---|---|---|---|---|---|')
        for i in rest:
            pk.append(f"| {i['code']} | {i['name']} | {i['iso']} | {i['action']} | {i['when']} | {i['window']} |")
        pk.append('')
    open(os.path.join(ROOT, 'docs', '发送包', f'{wk}.md'), 'w', encoding='utf-8').write('\n'.join(pk))



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=dt.date.today().isoformat())
    ap.add_argument('--also-weeks', type=int, default=2, help='额外预生成后续几周的发送包')
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.date)
    mon, sun = week_range(today)
    wk = iso_week(today)
    recs = load_records()
    cards = all_cards()
    now = dt.datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')

    items = []
    for code, c in cards.items():
        repo, r = recs.get(code, ('?', {}))
        nm = c.get('next_move') or {}
        d = parse_when(nm.get('when'))
        items.append(dict(code=code, repo=repo, name=c['name'], iso=r.get('iso') or '', grade=c['grade_final'], action=nm.get('action'),
                          angle=nm.get('angle', ''), model=nm.get('model', ''), price=nm.get('price', ''), window=nm.get('window', ''),
                          when=nm.get('when', ''), date=d, email=(c.get('contacts') or {}).get('email', ''), draft=c.get('draft_en'),
                          md=md_path(repo, code, c['grade_final']), reason=c.get('grade_reason_final', ''), notes=c.get('notes', '')))
    send = [i for i in items if i['action'] in ('第二封', '首触') and i['draft']]
    this_week = sorted([i for i in send if i['date'] and mon <= i['date'] <= sun], key=lambda x: (x['date'], x['iso'], x['code']))
    later = sorted([i for i in send if not (i['date'] and mon <= i['date'] <= sun)], key=lambda x: (x['date'] or dt.date(2099, 1, 1), x['code']))
    waiting = [i for i in items if i['action'] == '等回']
    idle = [i for i in items if i['action'] in ('不动', '并线')]

    # ---------- 发送包（本周 + 后续 N 周各一份） ----------
    os.makedirs(os.path.join(ROOT, 'docs', '发送包'), exist_ok=True)
    future = {}
    for k in range(0, a.also_weeks + 1):
        m0 = mon + dt.timedelta(days=7 * k)
        s0 = m0 + dt.timedelta(days=6)
        w0 = iso_week(m0)
        lst0 = sorted([i for i in send if i['date'] and m0 <= i['date'] <= s0], key=lambda x: (x['date'], x['iso'], x['code']))
        write_package(w0, m0, s0, lst0, [i for i in send if not (i['date'] and m0 <= i['date'] <= s0)], now)
        future[w0] = len(lst0)
    # ---------- 跟进总台 ----------
    sb = s_box_replies()
    saga_rows, saga_head = saga_now_rows()
    bd = ['# 跟进总台（一页）', '',
          f'生成：{now}（自动：`python3 scripts/external_clients/board.py`；源 = External research JSON + `data/gmail_s/2026-09_10群发名单_未入库.csv` + `docs/跟进日历_2026-11.md`）。只看这一页就知道本周要发什么、谁在等、谁不动。',
          '']
    bd.append('## 0. 一句话')
    bd.append('')
    bd.append(f"- External Clients 第 2 步：已研究 **{len(cards)}** 户（A {sum(1 for i in items if i['grade']=='A')} / B {sum(1 for i in items if i['grade']=='B')} / C {sum(1 for i in items if i['grade']=='C')}）；有稿待发 **{len(send)}** 封，其中本周 **{len(this_week)}** 封 → `docs/发送包/{wk}.md`；等回 {len(waiting)}；不动/并线 {len(idle)}。")
    bd.append(f"- Saga 老客户：`docs/跟进日历_2026-11.md` 「{saga_head or '现在'}」{len(saga_rows)} 户（下表 §3 摘前列）。")
    bd.append('')
    bd.append(f'## 1. 本周要发（{wk}，{len(this_week)} 封）— 稿全文在 `docs/发送包/{wk}.md`')
    bd.append('')
    bd.append('后续周（稿已备好，到周再发）：' + '；'.join(f'`docs/发送包/{w}.md` {n} 封' for w, n in future.items() if w != wk))
    bd.append('')
    bd.append('| 日期 | 窗口 | 户 | 公司 | 国 | 动作 | 型号 / 价 | 收件 |')
    bd.append('|---|---|---|---|---|---|---|---|')
    for i in this_week:
        bd.append(f"| {i['date']} {weekday_zh(i['date'])} | {i['window']} | {i['code']} | {i['name']} | {i['iso']} | {i['action']} | {i['model']} / {i['price']} | `{i['email']}` |")
    bd.append('')
    bd.append('## 2. External 已研究户 · 下一动作总表（按时点）')
    bd.append('')
    bd.append('| 时点 | 户 | 公司 | 国 | 级 | 动作 | 角度 | 档案 |')
    bd.append('|---|---|---|---|---|---|---|---|')
    for i in sorted(items, key=lambda x: ({'第二封': 0, '首触': 0, '等回': 1, '并线': 2, '不动': 3}[x['action']], x['date'] or dt.date(2099, 1, 1), x['code'])):
        bd.append(f"| {i['when'] or '—'} | {i['code']} | {i['name']} | {i['iso']} | {i['grade']} | {i['action']} | {(i['angle'] or i['reason'])[:70]} | `{i['md']}` |")
    bd.append('')
    bd.append('## 3. Saga 老客户 · 现在就做（摘自跟进日历，口径不改；全表见 `docs/跟进日历_2026-11.md`）')
    bd.append('')
    if saga_rows:
        bd.append('| 户 | 公司 | 国家 | 级 | 时点 | 渠道 | 一句话（开头） |')
        bd.append('|---|---|---|---|---|---|---|')
        for c in saga_rows:
            one = c[-1] if len(c) >= 10 else ''
            bd.append(f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[5]} | {c[6]} | {one[:60]} |")
    else:
        bd.append('（跟进日历未生成）')
    bd.append('')
    bd.append('## 4. S 箱 2026-09/10 群发 · 有来信的 16 个地址（机器回执 ≠ 回复；只有「待核」值得看一眼）')
    bd.append('')
    bd.append('| 地址 | 域 | 最后 | 最后主题 | 判 |')
    bd.append('|---|---|---|---|---|')
    for e, dom, last, subj, kind in sb:
        bd.append(f"| `{e}` | {dom} | {last} | {subj[:60]} | {kind} |")
    bd.append('')
    bd.append('## 5. 等回 / 不动（不用管，到期自动进下一轮）')
    bd.append('')
    bd.append('- 等回：' + ('、'.join(f"{i['code']}（{i['when'] or '—'}）" for i in waiting) or '无'))
    bd.append('- 不动/并线：' + ('、'.join(f"{i['code']}" for i in idle) or '无'))
    bd.append('')
    bd.append('## 6. 规矩（每轮不变）')
    bd.append('')
    bd.append('- 每周 20–30 封；美加 周三 08–10 当地，英/德/欧 周四 12–14，土耳其 周四 10–12；Simon 发，Agent 只备稿。')
    bd.append('- 每封一问、不伪造 Re:、价 = 快照 + 15 天、不提供应商/客户/同行、不写电话。')
    bd.append('- 回了 → 记到该户档案（研究卡 touch_status）并通知我改下一动作；退信 → 换地址或改 LinkedIn。')
    open(os.path.join(ROOT, 'docs', '跟进总台.md'), 'w', encoding='utf-8').write('\n'.join(bd))
    print('board ok', dict(cards=len(cards), send=len(send), this_week=len(this_week), later=len(later), waiting=len(waiting), idle=len(idle), week=wk))


if __name__ == '__main__':
    main()
