#!/usr/bin/env python3
"""B 级加厚分批表：把 entities.json 中 B 级客户按「互动强度 × 主攻区」分成 T1–T5，写 data/saga_clients/B级加厚分批.csv。
T1 = 有互动（成交/回复/WA/ISAF）且主攻区（北美/欧洲/土耳其）；T2 = 有互动其他地区；T3 = 主攻区无互动但有首轮调研；
T4 = 主攻区无互动未调研；T5 = 其余。表内含是否已有 research JSON / deep 块，便于逐批推进。"""
import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
FOCUS = ('北美', '欧洲', '土耳其')


def engaged(e):
    f = e.get('flags') or {}
    cats = ' '.join(e.get('categories') or []) + ' ' + ' '.join(e.get('tags') or [])
    return bool(e.get('deal_in_fu') or e.get('reply_sub') or e.get('wa_in_fu') or f.get('deal') or f.get('wa_added')
                or f.get('engaged_note') or f.get('sample') or 'ISAF' in cats or 'S重点' in cats)


def main():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    rows = []
    for e in ents:
        if e.get('grade') != 'B':
            continue
        rs = e.get('research') or {}
        rpath = os.path.join(DATA, 'research', e['code'] + '.json')
        has_rs = os.path.exists(rpath)
        deep = bool(rs.get('deep')) if rs else False
        if not deep and has_rs:
            try:
                deep = bool(json.load(open(rpath, encoding='utf-8')).get('deep'))
            except Exception:
                pass
        focus = (e.get('region') or '') in FOCUS
        eng = engaged(e)
        if eng and focus:
            tier = 'T1'
        elif eng:
            tier = 'T2'
        elif focus and has_rs:
            tier = 'T3'
        elif focus:
            tier = 'T4'
        else:
            tier = 'T5'
        f = e.get('flags') or {}
        cats = ' '.join(e.get('categories') or []) + ' ' + ' '.join(e.get('tags') or [])
        rows.append({'编号': e['code'], '等级': 'B', '分批': tier, '公司': e.get('name'), '国家': e.get('country'), '区域': e.get('region'),
                     '成交': int(bool(e.get('deal_in_fu') or f.get('deal'))), '实质回复': int(bool(e.get('reply_sub'))),
                     'WA': int(bool(e.get('wa_in_fu') or f.get('wa_added'))), 'ISAF': int('ISAF' in cats), 'S重点': int('S重点' in cats),
                     '样品': int(bool(f.get('sample'))), '互动备注': int(bool(f.get('engaged_note'))), '自有品牌': int(bool(f.get('own_brand'))),
                     '跟进次数': e.get('fu_count', len(e.get('followups') or [])),
                     '域名': ';'.join(e.get('domains') or []), '邮箱数': len(e.get('emails') or []),
                     '已有调研': int(has_rs), '已加厚': int(deep)})
    order = {'T1': 0, 'T2': 1, 'T3': 2, 'T4': 3, 'T5': 4}
    rows.sort(key=lambda r: (order[r['分批']], -r['成交'], -r['实质回复'], -r['WA'], -r['跟进次数'], r['编号']))
    out = os.path.join(DATA, 'B级加厚分批.csv')
    with open(out, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    stats = {}
    for r in rows:
        stats.setdefault(r['分批'], [0, 0])
        stats[r['分批']][0] += 1
        stats[r['分批']][1] += r['已加厚']
    print(out, {k: f'{v[0]} (加厚 {v[1]})' for k, v in sorted(stats.items())})


if __name__ == '__main__':
    main()
