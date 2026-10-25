#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 76 批(a)：信稿开头句「most recently "<主题>" on <日期>」与邮箱索引逐封核对，主题错的按当日真实去信主题改写，并把该封去信补成事实。

背景：audit_ab.py 发现 158 封稿的开头句主题取自 gmail_digest 的线程主题列表（首个线程），不是该日期那封邮件的真实主题
（例：SB-183 稿写「Industrial PoE Switch」on 16 September 2026，邮箱里 2026-09-16 那封是「16 Port Industrial PoE Switch」）。
客户收到信时对得上自己收件箱才可信，所以逐封改。

默认 DRY（只打印），`--apply` 落盘。索引来源：data/gmail_s|gmail_a/messages/*/*.jsonl（dir=out，client 标签）+ data/gmail_e/bcc_match_latest.json。
"""
import glob
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from common import DATA, ROOT, RESEARCH_DIR  # noqa: E402

APPLY = '--apply' in sys.argv
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MON = {m: i + 1 for i, m in enumerate(MONTHS)}
OPENER_RE = re.compile(r'"([^"\n]{3,90})" on (\d{1,2}) (' + '|'.join(MONTHS) + r') (\d{4})')
NOTE = '（第 76 批(a) 2026-10-25：开头句主题按邮箱索引核对改写，同日去信补入事实）'


def load_out_index():
    idx = defaultdict(lambda: defaultdict(list))  # code → date → [(ts, subject, who, k)]
    for acct, who in (('gmail_s', 'S 箱（Simon）'), ('gmail_a', 'A 箱（Alan）')):
        for fp in glob.glob(os.path.join(ROOT, 'data', acct, 'messages', '*', '*.jsonl')):
            for line in open(fp, encoding='utf-8'):
                try:
                    m = json.loads(line)
                except ValueError:
                    continue
                if m.get('dir') != 'out':
                    continue
                d_ = (m.get('date') or '')[:10]
                for c in m.get('client') or []:
                    idx[c][d_].append((m.get('date') or '', (m.get('subj') or '').strip(), who, m.get('k') or ''))
    fp = os.path.join(ROOT, 'data', 'gmail_e', 'bcc_match_latest.json')
    if os.path.exists(fp):
        for c, v in json.load(open(fp, encoding='utf-8')).items():
            for h in v.get('hits') or []:
                idx[c][(h.get('date') or '')[:10]].append((h.get('date') or '', (h.get('subject') or '').strip(), 'Elsa 箱群发 Bcc', h.get('msg_id') or ''))
    return idx


def main():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    ab = sorted(e['code'] for e in ents if e.get('grade') in ('A', 'B'))
    idx = load_out_index()
    changed = 0
    unresolved = []
    for c in ab:
        fp = os.path.join(RESEARCH_DIR, f'{c}.json')
        if not os.path.exists(fp):
            continue
        raw = open(fp, encoding='utf-8').read()
        m2 = re.match(r'\{\n(\s+)"', raw)
        ind = len(m2.group(1)) if m2 else 1
        d = json.loads(raw)
        mr = d.get('mail_review') or {}
        de = mr.get('draft_en')
        if not (isinstance(de, dict) and de.get('body')):
            continue
        body, subj = de['body'], de['subject']
        edits = []
        for s_, dd, mon, yy in OPENER_RE.findall(body):
            iso_d = f'{yy}-{MON[mon]:02d}-{int(dd):02d}'
            same = idx.get(c, {}).get(iso_d, [])
            if not same:
                unresolved.append((c, s_, iso_d, 'no mail that day'))
                continue
            subjects = {x[1].lower() for x in same}
            if s_.strip().lower() in subjects:
                continue
            latest = sorted(same)[-1]
            edits.append((s_, iso_d, latest))
        if not edits:
            continue
        facts = mr.setdefault('facts', [])
        for s_, iso_d, (ts, real, who, k) in edits:
            body = body.replace(f'"{s_}" on', f'"{real}" on', 1)
            subj = subj.replace(s_, real) if s_ in subj else subj
            if not any(str(f.get('date')) == iso_d and real.lower() in str(f.get('quote', '')).lower() for f in facts):
                facts.append({'date': iso_d, 'dir': '去', 'who': who, 'quote': real,
                              'why': f'本日去信真实主题（邮箱索引 {k}；信稿开头句引用此封；此前稿内写的「{s_}」是线程列表首题，不是本封）', 'k': k or 'mail_index'})
            print(f'{c} {iso_d}: 「{s_}」→「{real}」({who})')
        de['body'], de['subject'] = body, subj
        nm = mr.setdefault('next_move', {})
        if nm is not None and NOTE not in str(nm.get('action', '')):
            nm['action'] = (nm.get('action') or '') + NOTE
        changed += 1
        if APPLY:
            json.dump(d, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=ind)
            open(fp, 'a', encoding='utf-8').write('\n')
    print(f'{"APPLIED" if APPLY else "DRY"} changed={changed} unresolved={len(unresolved)}')
    for u in unresolved:
        print('  UNRESOLVED', u)


if __name__ == '__main__':
    main()
