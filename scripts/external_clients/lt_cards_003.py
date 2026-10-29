#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-X01b · 7 张 External 卡随记录域名修正同步（T29-U131 2026-10-29）。
导入时 domain 字段进了邮箱用户名 / 注释（sales.kenya / hk.kim / fletcher.prendergast / sales.tw / camelisat.it与0564）或旧域已死（smart-network.ge /
humanart-kyocera.de）；记录已改 domain（domain_prev + domain_fix_note），卡上的 alive / 证据 URL 也要跟着改。DNS 2026-10-29 复查新域 MX+A 全部正常。幂等。
"""
import ast
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
XDATA = os.path.join(ROOT, 'data', 'external_clients')
DATE = '2026-10-29'
FIX = {'XB-E002': 'mart-networks.com', 'XB-E016': 'aitech24.co.kr', 'XB-E055': 'cdl.co.nz', 'XB-E057': 'commverge.com',
       'XB-M078': 'takopi.ge', 'XA-M388': 'human-art.de', 'XA-M431': 'camelisat.it'}


def main():
    spec = importlib.util.spec_from_file_location('research_store', os.path.join(HERE, 'research_store.py'))
    store = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(store)
    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in json.load(open(os.path.join(XDATA, repo + '.json'), encoding='utf-8'))['records']:
            if r.get('code') in FIX:
                recs[r['code']] = r
    n = 0
    for code, dom in FIX.items():
        card = store.get(code)
        r = recs[code]
        prev = r.get('domain_prev') or ''
        if card.get('domain_fix') == dom:
            continue
        ev = card.get('evidence')
        if isinstance(ev, str):
            ev = ast.literal_eval(ev)
        for e in ev:
            if prev and prev in (e.get('url') or ''):
                e['url'] = (e['url'] or '').replace(prev, dom)
        ev.append({'kind': '域名修正', 'claim': f'记录域名 {prev or "—"} → {dom}（{r.get("domain_fix_note") or "LT-X01"}）；DNS {DATE} MX + A 正常',
                   'quote': f'domain_prev={prev}', 'url': f'https://{dom}/', 'date': DATE})
        card['evidence'] = ev
        card['alive'] = f'域名修正为 {dom}（原 {prev or "—"} 是邮箱用户名 / 注释 / 旧域）；DNS {DATE} MX + A 正常；官网快照待 Actions 补抓'
        card['domain_fix'] = dom
        card['notes'] = f'LT-X01b 域名修正同步（{DATE}）：{prev or "—"} → {dom}。\n' + (card.get('notes') or '')
        store.put(card)
        n += 1
    print('LT-X01b cards fixed', n)


if __name__ == '__main__':
    main()
