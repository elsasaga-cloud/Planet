#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""peek.py SB-004 SA-009  → 打印编号区间内实体的关键信号（供调研时快速判断）。"""
import json, os, sys
from common import DATA
E={e['code']:e for e in json.load(open(os.path.join(DATA,'entities.json'),encoding='utf-8'))}
a,b=sys.argv[1],sys.argv[2]
pre=a[:3]
for code in sorted(E):
    if code.startswith(pre) and a<=code<=b:
        e=E[code]
        print(f"{code} | {e['name'][:28]} | {e['country']} | score {e['score']} | deal {e.get('deal')} | repl {e.get('reply_sub')} | wa {e.get('wa')} | fu {len(e['followups'])} | last {e.get('last_year')} | tags {','.join(e['tags'])[:70]}")
        print('   interests:', ' / '.join(e.get('interests',[]))[:160].replace('\n',' '))
        print('   remarks  :', ' / '.join(e.get('remarks',[]))[:160].replace('\n',' '))
