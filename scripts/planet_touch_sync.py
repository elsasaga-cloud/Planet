#!/usr/bin/env python3
"""把 S 邮箱导出（data/gmail_s/messages/*.jsonl）与 Elsa 已触达清单（data/gmail_已触达清单.csv）
同步进 Planet 渠道客户主表（data/客户名单_Planet渠道_2026-10.csv）的 状态 / 首次触达日 / 最后互动日 / 备注。

规则（PR-02-31 复盘 2026-10-22）：
- 匹配：客户「网站」域名 == 联系人邮箱域名，或「入口/联系方式」里出现的邮箱域名 == 联系人邮箱域名；
- 有实质来信（bulk=False 的 in 件；自动回复/退信不算）→ 状态 `20-有回复(S邮箱 去N/来M)`；只有去信 → `10-已触达(S邮箱 去N·0回复)`；
  只在 Elsa 群发清单 → `10-已触达(E邮箱群发 N封·0回复)`；两者都有时以 S 邮箱为主、E 另注；
- 首次触达日 = 最早一封，最后互动日 = 最晚一封；备注前置一段「【触达同步 yyyy-mm-dd】…」，幂等（已有同标记段则替换）。
- 不改评级、不改编号；改完请跑 `python3 scripts/render.py && python3 scripts/audit.py`。
"""
import csv
import datetime as dt
import glob
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
S_MSGS = os.path.join(ROOT, 'data', 'gmail_s', 'messages')
E_LIST = os.path.join(ROOT, 'data', 'gmail_已触达清单.csv')
TODAY = dt.date.today().isoformat()
MARK = '【触达同步'
OWN = {'gmail.com', 'googlemail.com', 'sagatelecom.com', 'sagatele.com', 'outlook.com', 'hotmail.com', 'yahoo.com'}


def dom_of_url(u):
    u = (u or '').strip().lower()
    u = re.sub(r'^https?://', '', u)
    u = re.sub(r'^www\.', '', u)
    return u.split('/')[0].split('?')[0]


def doms_of_text(t):
    return {m.lower() for m in re.findall(r'[\w.+-]+@([\w-]+(?:\.[\w-]+)+)', t or '')}


def main():
    rows = list(csv.DictReader(open(MASTER, encoding='utf-8-sig')))
    fields = list(rows[0].keys())
    # 按域名统计 S 邮箱往来：直接扫消息体（contacts.csv 不区分自动回复；消息里 bulk=True 的来信 = 自动回复/退信）
    s_stat = {}
    for fp in sorted(glob.glob(os.path.join(S_MSGS, '*', '*.jsonl'))):
        for line in open(fp, encoding='utf-8'):
            m = json.loads(line)
            people = ([m['from']] if m.get('dir') == 'in' else (m.get('to') or []) + (m.get('cc') or []))
            seen = set()
            for pp in people:
                em = (pp.get('e') or '').lower()
                d = em.split('@')[-1]
                if not d or d in OWN or d in seen:
                    continue
                seen.add(d)
                st = s_stat.setdefault(d, {'out': 0, 'in': 0, 'auto': 0, 'first': '', 'last': '', 'emails': set(), 'last_in': None})
                day = (m.get('date') or '')[:10]
                st['first'] = min(st['first'] or day, day)
                st['last'] = max(st['last'], day)
                st['emails'].add(em)
                if m.get('dir') == 'in':
                    if m.get('bulk'):
                        st['auto'] += 1
                    else:
                        st['in'] += 1
                        if not st['last_in'] or day >= st['last_in'][0]:
                            st['last_in'] = (day, em, m.get('subj') or '')
                else:
                    st['out'] += 1
    e_by_dom = defaultdict(list)
    if os.path.exists(E_LIST):
        for c in csv.DictReader(open(E_LIST, encoding='utf-8-sig')):
            d = (c.get('收件域名') or '').lower()
            if d:
                e_by_dom[d].append(c)
    changed = []
    for r in rows:
        doms = {dom_of_url(r.get('网站'))} | doms_of_text(r.get('入口/联系方式'))
        doms = {d for d in doms if d and d not in OWN}
        s = [s_stat[d] for d in doms if d in s_stat]
        e = [c for d in doms for c in e_by_dom.get(d, [])]
        if not s and not e:
            continue
        out = sum(x['out'] for x in s)
        inn = sum(x['in'] for x in s)
        auto = sum(x['auto'] for x in s)
        dates = [x['first'] for x in s] + [x['last'] for x in s]
        dates += [c['发送日期'][:10] for c in e if c.get('发送日期')]
        first, last = min(dates), max(dates)
        s_addr = '、'.join(sorted(set().union(*[x['emails'] for x in s]))[:4]) if s else ''
        if s and inn > 0:
            status = f'20-有回复(S邮箱 去{out}/来{inn})'
        elif s and out == 0:
            status = f'10-已触达(S邮箱 去信未入导出·仅见自动回复{auto}封)'
        elif s:
            status = f'10-已触达(S邮箱 去{out}·0回复)'
        else:
            status = f'10-已触达(E邮箱群发 {len(e)}封·0回复)'
        last_in = ''
        if inn > 0:
            lc = max((x['last_in'] for x in s if x['last_in']), key=lambda t: t[0])
            last_in = f'；最后实质来信 {lc[0]} {lc[1]}「{lc[2][:50]}」'
        if auto:
            last_in += f'；另有自动回复/退信 {auto} 封（不算回复）'
        note = (f'{MARK} {TODAY}】' +
                (f'S 邮箱（s.sagatelecom）去 {out} / 实质来信 {inn}，{first} → {last}，地址 {s_addr}{last_in}' if s else '') +
                ('；' if s and e else '') +
                (f'Elsa 账号群发 {len(e)} 封（{min(c["发送日期"] for c in e)[:10]} → {max(c["发送日期"] for c in e)[:10]}）0 回复' if e else '') +
                '。首触邮件不再是「冷启动」，改为续谈口径。')
        old_note = r.get('备注') or ''
        if MARK in old_note:
            old_note = re.sub(r'【触达同步[^】]*】[^|]*?。首触邮件不再是「冷启动」，改为续谈口径。\s*\|?\s*', '', old_note)
        r['备注'] = (note + (' | ' + old_note if old_note else '')).strip()
        r['状态'] = status
        r['首次触达日'] = first
        r['最后互动日'] = last
        changed.append((r['档案编号'], r['公司名'], status, first, last))
    with open(MASTER, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)
    for c in changed:
        print(*c, sep=' | ')
    print(f'updated {len(changed)} / {len(rows)} rows → {MASTER}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
