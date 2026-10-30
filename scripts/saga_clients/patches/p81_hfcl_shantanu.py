#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p81 · SB-243 HFCL：Simon 2026-10-30（T29-U142）「HFCL保留A 前2天那个人还问我产品呢 Shantanu HFCL +91 98211 96123」
→ KP Shantanu 补 WhatsApp 号；研究档事实（dir=Simon，2026-10-28 约：问产品）；next_move 改为 WhatsApp 现在就接；intel KP 一条；A 维持（Simon 裁定：上市中型集团自己是 OEM 采购方 → 不按巨头子公司算）。幂等。"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P = os.path.join(ROOT, 'data', 'saga_clients', 'research', 'SB-243.json')
PHONE = '+91 98211 96123'
DATE = '2026-10-30'


def main():
    rs = json.load(open(P, encoding='utf-8'))
    ch = []
    # KP
    for k in rs.get('kp') or []:
        if 'Shantanu' in (k.get('name') or ''):
            if PHONE not in (k.get('phone') or ''):
                k['phone'] = (k.get('phone') + '；' if k.get('phone') else '') + f'{PHONE}（WhatsApp，Simon 2026-10-30 给）'
                ch.append('kp.phone')
            if '2026-10-28' not in (k.get('title') or ''):
                k['title'] = (k.get('title') or '') + '；**2026-10-28（约）仍在向 Simon 问产品（WhatsApp）**——活跃对话中，Simon 2026-10-30 定「保留 A」'
                ch.append('kp.title')
    mr = rs.setdefault('mail_review', {})
    facts = mr.setdefault('facts', [])
    if not any(f.get('dir') == 'Simon' and 'Shantanu' in str(f.get('quote', '')) and '2026-10-28' in str(f.get('date', '')) for f in facts):
        facts.append({'date': '2026-10-28（约）', 'dir': 'Simon', 'who': 'Simon（WhatsApp 对话，T29-U142 转述）', 'quote': f'「前 2 天那个人还问我产品呢 — Shantanu HFCL {PHONE}」', 'why': 'HFCL 采购/产品线人员 Shantanu 主动问产品 → 对话活跃；Simon 裁定 HFCL 保留 A', 'k': '对话全记录 2026-10-30 T29-U142'})
        ch.append('fact')
    nm = mr.setdefault('next_move', {})
    if nm.get('when') != '现在（WhatsApp 接着 2026-10-28 的问题答）':
        nm['when_prev'] = nm.get('when')
        nm['channel_prev'] = nm.get('channel')
        nm['when'] = '现在（WhatsApp 接着 2026-10-28 的问题答）'
        nm['channel'] = f'WhatsApp {PHONE}（Shantanu）'
        nm['action'] = '接着他 2026-10-28 问的产品：给对应型号规格 + 一口价（OEM 30% 档：CENTEC ≥35% / Marvell L3 ≥25%），只问一个问题（量 / 哪个项目）；' + (nm.get('action') or '')
        ch.append('next_move')
    it = rs.setdefault('intel', {'as_of': DATE, 'items': []})
    key = f'KP Shantanu（HFCL）WhatsApp {PHONE}'
    if not any(key in x.get('quote', '') for x in it['items']):
        it['items'].append({'kind': 'KP', 'date': DATE, 'quote': f'{key}；2026-10-28（约）主动问产品（Simon 口述）', 'url': '', 'note': 'Simon 2026-10-30：HFCL 保留 A；上市中型集团自己是 OEM 采购方，不按「巨头子公司」算（K8）', 'batch': 'INTEL-12', 'found': True, 'added': DATE})
        it['as_of'] = DATE
        ch.append('intel')
    rs['override_reason'] = (rs.get('override_reason') or '') + ('' if 'K8' in (rs.get('override_reason') or '') else '；Simon 2026-10-30 裁定保留 A（K8：上市中型集团自为 OEM 采购方；Shantanu 2026-10-28 仍在问产品）')
    json.dump(rs, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('SB-243', ch or 'no change')


if __name__ == '__main__':
    main()
