#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p77 · SA-004 Boecek Sec（德国，A，成交过）：Simon 2026-10-30 06:3xZ 确认「49 172 5368536 有他的WhatsApp」
（与客户主表「电话」列 491725368536 同号）→ 研究档记事实 + 路径改 WhatsApp（邮件 boecek@ 15 封 0 开只作附件通道）。幂等。"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P = os.path.join(ROOT, 'data', 'saga_clients', 'research', 'SA-004.json')
MARK = 'Simon 2026-10-30 确认 WhatsApp'


def main():
    j = json.load(open(P, encoding='utf-8'))
    mr = j.setdefault('mail_review', {})
    fl = mr.setdefault('facts', [])
    if not any(MARK in (f.get('why') or '') for f in fl):
        fl.append({'date': '2026-10-30', 'dir': 'Simon', 'who': 'Simon', 'quote': '49 172 5368536 有他的WhatsApp',
                   'why': MARK + '：路径 = WhatsApp（+49 172 5368536，客户主表「电话」同号；Simon 手机已加）；官网 boecek.de 为 STRATO 占位、邮件 15 封 0 开 → 邮件只作附件通道', 'url': ''})
    nm = mr.get('next_move')
    if isinstance(nm, dict) and 'WhatsApp' not in str(nm.get('channel', '')):
        nm['channel_prev'] = nm.get('channel')
        nm['channel'] = 'WhatsApp（Simon 手机已加 +49 172 5368536；Simon 本人发）→ 要规格书 / 报价时再用邮件 boecek@ 作附件通道（该址 15 封 0 开，先在 WhatsApp 里确认收件地址）'
        nm['when_prev'] = nm.get('when')
        nm['when'] = '随时（WhatsApp 一句真人问候，Simon 本人；不必等 2027-Q1 换人）'
        nm['action'] = '一问（WhatsApp：埃森展买的 5 口样机用得怎样 + 8 口管理 DIN / 4+1 PoE 要不要样价）；' + str(nm.get('action') or '')
    if 'WhatsApp' not in str(mr.get('situation', '')):
        mr['situation'] = str(mr.get('situation') or '') + ' 2026-10-30 Simon 确认有其 WhatsApp（+49 172 5368536）→ 触达路径不缺，缺的是一次真人问候；成交过（埃森展 2024 现场买 5 电口样机）故等级 A 不变。'
    bd = mr.get('binding')
    if isinstance(bd, dict) and 'WhatsApp' not in str(bd.get('level', '')):
        bd['note_2026_10_30'] = 'Simon 手机 WhatsApp 已加（+49 172 5368536）；展会成交过 → 实际绑定高于「邮件 0 回」口径'
    json.dump(j, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('SA-004 WhatsApp patched')


if __name__ == '__main__':
    main()
