#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""加厚挖掘写入器（T27）：把深挖字段并入已有 research/<code>.json（不覆盖原有引文，只追加/设置）。

用法：python3 deepen.py <<'EOF'
[{"code":"SA-003","deep":{"done_at":"2026-10-21","level":"深挖 v1"},
  "company_facts":{...},"business_lines":[...],"products_seen":[...],"channels":{...},
  "signals":[...],"risks":[...],"saga_fit":{"p1":"STC-424DGGPM-280W","tier":25,"why":"..."},
  "email_hook":"...","evidence_add":[{...}],"kp_add":[{...}],"brands_add":[...],"notes_add":"..."}]
EOF
"""
import json
import os
import sys

from common import RESEARCH_DIR

SET_FIELDS = ['deep', 'company_facts', 'business_lines', 'products_seen', 'channels', 'signals', 'risks', 'saga_fit', 'email_hook',
              'website_status', 'type', 'size', 'summary', 'name_official', 'grade_override', 'override_reason']


def main():
    items = json.load(sys.stdin)
    n = 0
    for it in items:
        code = it['code']
        p = os.path.join(RESEARCH_DIR, code + '.json')
        if not os.path.exists(p):
            print('no research json for', code, '— run add_research.py first')
            continue
        j = json.load(open(p, encoding='utf-8'))
        merge = bool(it.get('merge'))  # v2 增量：列表追加去重、字典更新、标量替换
        for k in SET_FIELDS:
            if k not in it:
                continue
            if merge and isinstance(it[k], list) and isinstance(j.get(k), list):
                if k == 'products_seen':
                    seen = {(x.get('brand'), x.get('model')) for x in j[k]}
                    j[k] += [x for x in it[k] if (x.get('brand'), x.get('model')) not in seen]
                else:
                    j[k] += [x for x in it[k] if x not in j[k]]
            elif merge and isinstance(it[k], dict) and isinstance(j.get(k), dict):
                j[k].update(it[k])
            else:
                j[k] = it[k]
        if it.get('evidence_add'):
            seen = {(e.get('url'), e.get('claim')) for e in j.get('evidence', [])}
            for e in it['evidence_add']:
                if (e.get('url'), e.get('claim')) not in seen:
                    j.setdefault('evidence', []).append(e)
        if it.get('kp_add'):
            seen = {(k.get('name'), k.get('email')) for k in j.get('kp', [])}
            for k in it['kp_add']:
                if (k.get('name'), k.get('email')) not in seen:
                    j.setdefault('kp', []).append(k)
        if it.get('brands_add'):
            for b in it['brands_add']:
                if b not in j.setdefault('brands_seen', []):
                    j['brands_seen'].append(b)
        if it.get('notes_add'):
            j['notes'] = ((j.get('notes') or '') + ' ｜ ' + it['notes_add']).strip(' ｜')
        if 'deep' not in j:
            j['deep'] = {'done_at': it.get('deep', {}).get('done_at', ''), 'level': '深挖 v1'}
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        n += 1
    total = sum(1 for f in os.listdir(RESEARCH_DIR) if f.endswith('.json') and json.load(open(os.path.join(RESEARCH_DIR, f), encoding='utf-8')).get('deep'))
    print(f'deepened {n}; total deep {total}')


if __name__ == '__main__':
    main()
