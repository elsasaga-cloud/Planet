#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 stdin 的 JSON 数组（每项含 code）写成 data/saga_clients/research/<code>.json（覆盖同编号）。"""
import json, os, sys
from common import RESEARCH_DIR
os.makedirs(RESEARCH_DIR, exist_ok=True)
items = json.load(sys.stdin)
for it in items:
    assert it.get('code'), it
    it.setdefault('researched_at', '2026-10-21')
    with open(os.path.join(RESEARCH_DIR, it['code'] + '.json'), 'w', encoding='utf-8') as f:
        json.dump(it, f, ensure_ascii=False, indent=1)
print('written', len(items), 'total', len(os.listdir(RESEARCH_DIR)))
