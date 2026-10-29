#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""External 记录邮箱清洗 001（T29-U124 全量核验发现，2026-10-29）。

问题：导入时从中文备注里切出来的邮箱带了前缀 / 后缀碎字（「邮件发exports@…」「邮箱sales@…」「官网联系页给info@…」
「与b452存camacho@…及相同」），共 199 条散在 cctv / edgecore / mikrotik 三库 `records[].emails[].addr` 与 `emails_live`，
研究卡 `contacts.email` 另有 9 条（**加粗**、停用标注粘连）。群发 / MX 核查 / 档案显示都会被这些脏串拖累。

做法（幂等）：对每个不合法的 addr 用正则抠出第一个合法邮箱 → 替换 addr，原串记到 status 尾巴「｜原文「…」」；抠不出的整条删除并记日志；
与同户已有邮箱重复的合并（保留先出现者，status 合并）；`emails_live` 同步清洗 + 去重。研究卡 `contacts.email` 同法，原串记 `contacts.email_note`。
清洗日志：docs/requirements/External_邮箱清洗_2026-10-29.md。之后重跑 `scripts/external_clients/render.py`。

用法：python3 scripts/external_clients/fix_emails_001.py
"""
import collections
import glob
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data', 'external_clients')
LOG = os.path.join(ROOT, 'docs', 'requirements', 'External_邮箱清洗_2026-10-29.md')
EM = re.compile(r'^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$')
FIND = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)+')
# 「first.last@…」这类是邮箱格式模板不是真实地址：保留为线索但标「模板·勿发」，并从 emails_live 剔除
PATTERN = re.compile(r'^(first|last|firstname|lastname|name|vorname|nachname|prenom|nom|xxx+|initial)([._-](first|last|firstname|lastname|name|vorname|nachname|prenom|nom|initial))?$', re.I)


def extract(s):
    m = FIND.search(s or '')
    if not m:
        return None
    a = m.group(0).rstrip('.')
    # 常见粘连：地址后紧跟「及 / 与 / 或 / 【 / （」已被字符类挡住；尾部「.com.my」等多级域名保留
    return a if EM.match(a) else None


def main():
    fixed = collections.Counter()
    examples = []
    dropped = []
    for fn in ('cctv.json', 'edgecore.json', 'mikrotik.json'):
        p = os.path.join(DATA, fn)
        d = json.load(open(p, encoding='utf-8'))
        changed = False
        for r in d['records']:
            emails = r.get('emails') or []
            if not emails and not r.get('emails_live'):
                continue
            seen = {}
            new = []
            for e in emails:
                a = e.get('addr') or ''
                if EM.match(a):
                    clean = a
                else:
                    clean = extract(a)
                    if not clean:
                        dropped.append((r.get('code') or r.get('name'), a))
                        fixed['dropped'] += 1
                        changed = True
                        continue
                    e = dict(e)
                    e['addr'] = clean
                    e['status'] = (e.get('status') or '') + f'｜原文「{a}」'
                    fixed['fixed'] += 1
                    changed = True
                    if len(examples) < 25:
                        examples.append((r.get('code') or r.get('name'), a, clean))
                if PATTERN.match(clean.split('@')[0]) and '模板·勿发' not in (e.get('status') or ''):
                    e = dict(e)
                    e['status'] = '模板·勿发｜' + (e.get('status') or '')
                    fixed['pattern'] += 1
                    changed = True
                k = clean.lower()
                if k in seen:
                    # 合并：保留先出现者，status 并入
                    st = e.get('status') or ''
                    if st and st not in (seen[k].get('status') or ''):
                        seen[k]['status'] = (seen[k].get('status') or '') + '｜' + st
                    fixed['merged_dup'] += 1
                    changed = True
                    continue
                seen[k] = e
                new.append(e)
            if new != emails:
                r['emails'] = new
            live = r.get('emails_live')
            if live is not None:
                nl = []
                for a in live:
                    c = a if EM.match(a) else extract(a)
                    if c and PATTERN.match(c.split('@')[0]):
                        fixed['live_pattern_dropped'] += 1
                        changed = True
                        continue
                    if not c:
                        fixed['live_dropped'] += 1
                        changed = True
                        continue
                    if c != a:
                        fixed['live_fixed'] += 1
                        changed = True
                    if c.lower() not in {x.lower() for x in nl}:
                        nl.append(c)
                    else:
                        fixed['live_dedup'] += 1
                        changed = True
                if nl != live:
                    r['emails_live'] = nl
        if changed:
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            fixed['files'] += 1
    # 研究卡
    card_fixed = []
    for p in glob.glob(os.path.join(DATA, 'research', '*.json')):
        c = json.load(open(p, encoding='utf-8'))
        ct = c.get('contacts') or {}
        em = ct.get('email') or ''
        if em and not EM.match(em):
            clean = extract(em.replace('*', ''))
            if clean:
                ct['email'] = clean
                ct['email_note'] = ((ct.get('email_note') or '') + '；' if ct.get('email_note') else '') + f'原文「{em}」（{os.path.basename(LOG)[:-3]} 清洗）'
                c['contacts'] = ct
                json.dump(c, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
                card_fixed.append((c['code'], em, clean))
    now = subprocess.check_output(['date', '-u', '+%Y-%m-%d %H:%MZ']).decode().strip()
    if fixed or card_fixed:
        lines = [f'# External 记录邮箱清洗 001（{now}，T29-U124 全量核验）', '',
                 f'> 脚本 `scripts/external_clients/fix_emails_001.py`（幂等）。记录层：修正 {fixed["fixed"]} 条、删除抠不出邮箱的 {fixed["dropped"]} 条、合并重复 {fixed["merged_dup"]} 条；'
                 f'`emails_live` 修正 {fixed["live_fixed"]} / 删除 {fixed["live_dropped"]} / 去重 {fixed["live_dedup"]} / 剔除格式模板 {fixed["live_pattern_dropped"]}（如 first.last@…，记录层标「模板·勿发」{fixed["pattern"]} 条）；文件 {fixed["files"]} 个。研究卡 `contacts.email` 修正 {len(card_fixed)} 张。'
                 ' 原串都保留在 status / email_note 里，可回溯。根因：导入脚本从中文备注切邮箱时未用正则截断前后缀；今后新导入一律过 `EM` 正则。', '',
                 '## 记录层示例（前 25）', '', '| 编号 | 原串 | 清洗后 |', '|---|---|---|']
        lines += [f'| {c} | {a.replace("|", "｜")} | {b} |' for c, a, b in examples]
        if dropped:
            lines += ['', '## 删除（抠不出合法邮箱）', ''] + [f'- {c}：`{a}`' for c, a in dropped]
        if card_fixed:
            lines += ['', '## 研究卡', '', '| 编号 | 原串 | 清洗后 |', '|---|---|---|'] + [f'| {c} | {a.replace("|", "｜")} | {b} |' for c, a, b in card_fixed]
        lines.append('')
        if os.path.exists(LOG):
            lines = open(LOG, encoding='utf-8').read().rstrip('\n').split('\n') + ['', f'## 重跑 {now}', '', f'- 记录层 {dict(fixed)}；研究卡 {len(card_fixed)}（幂等：应为 0）', '']
        open(LOG, 'w', encoding='utf-8').write('\n'.join(lines))
    print(dict(fixed), 'cards', len(card_fixed), 'dropped', dropped[:5])


if __name__ == '__main__':
    main()
