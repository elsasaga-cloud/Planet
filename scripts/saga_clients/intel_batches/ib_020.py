#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-20（T29-U144 2026-10-30）· 登记库镜像：把 data/saga_clients/registry/*.json 里 A 户（及挖过的 B 户）的官方登记行镜像进 intel（kind 登记，带来源 URL）。幂等。"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

SD = os.path.join(IS.ROOT, 'data', 'saga_clients')
D = '2026-10-30'
B = 'INTEL-20'


def main():
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    reg = {}
    for f in glob.glob(os.path.join(SD, 'registry', '*.json')):
        for c, v in (json.load(open(f, encoding='utf-8')) or {}).get('rows', {}).items():
            reg.setdefault(c, v)
    n = 0
    for c, v in reg.items():
        e = ents.get(c)
        if not e or e.get('grade') not in ('A', 'B'):
            continue
        src = str(v.get('source') or '')
        num = str(v.get('number') or '')
        if '0 查' in src or '未查' in num or not v.get('name'):
            continue
        q = f"{src[:60]}：{str(v.get('name', ''))[:90]}" + (f" · {num[:40]}" if num and num not in ('—', '') else '') + (f" · {str(v.get('status', ''))[:30]}" if v.get('status') else '') + (f" · 成立 {str(v.get('incorporated', ''))[:10]}" if v.get('incorporated') else '') + (f" · {str(v.get('address', ''))[:80]}" if v.get('address') else '')
        n += IS.add(c, '登记', q, str(v.get('url') or ''), D, '登记库镜像（公司底数 2026-10-27 批次）', B, True)
    print(B, 'registry mirrored +', n)


if __name__ == '__main__':
    main()
