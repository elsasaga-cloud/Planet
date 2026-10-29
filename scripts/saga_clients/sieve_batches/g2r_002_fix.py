#!/usr/bin/env python3
"""Saga C · 复查补证 G2R-02（2026-10-29，T29-U122「继续」）—— 只改 1 户：SC-729 Brown Bear（brownbear.ru）。

G2R-01 依据 tapki.com 聚合页把 ИНН 9728025085 / ОГРН 1217700015807 记为 brownbear.ru 的法人并入池 ○（reg_pending 复核）。
本轮按 ИНН 查官方登记镜像（rusprofile / zachestnyibiznes）：该号对应 ООО «Мицар»（Москва Научный проезд 19 оф. 398；2021-01-22；
оптовая торговля электронным и телекоммуникационным оборудованием；ГД Немецков П.С.；УК 50 000 ₽）—— 经营类目吻合，
但官网 / 官方页都没有把 Brown Bear 与 «Мицар» 绑在一起 → 法人名待核，不能算坐实 → ○ 正式 转 △ 观察（legal_pending），试单 / 回信拿到
合同主体后再转正。事实 + URL 落在 data/external_clients/xc_path_fill_2026-10-29_b2.json['regfix']['SC-729']（只读它，不再外查）。

副作用（幂等，按「｜补证 G2R-02」标记）：data/saga_clients/sieve.json；P池_巡检表 该行档位 / 入池 / 标签 / 备注；名册小节「Saga C 复查 · 补证 G2R-02」。
用法：python3 scripts/saga_clients/sieve_batches/g2r_002_fix.py
"""
import collections
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SIEVE = os.path.join(ROOT, 'data', 'saga_clients', 'sieve.json')
FILL = os.path.join(ROOT, 'data', 'external_clients', 'xc_path_fill_2026-10-29_b2.json')
WATCH = os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_2026-10-29.csv')
ROSTER = os.path.join(ROOT, 'docs', 'P池_资产池名册_2026-10-29.md')
BATCH = 'G2R-02'
DATE = '2026-10-29'
CODE = 'SC-729'
MARK = f'｜补证 {BATCH}（{DATE}）：'
LABEL = ('ИНН 9728025085 官方登记对应 ООО «Мицар»（ОГРН 1217700015807，Москва，2021-01-22，电子 / 电信设备批发，ГД Немецков П.С.，УК 50 000 ₽）'
         '—— 类目吻合但与 brownbear.ru 的关联只有聚合页一处，官方页未证实 → 法人名待核，○ 正式转 △ 观察；试单 / 回信拿到合同主体即转正')


def main():
    fx = json.load(open(FILL, encoding='utf-8'))['regfix'][CODE]
    s = json.load(open(SIEVE, encoding='utf-8'))
    cur = s[CODE]
    changed = False
    if MARK not in cur['reason']:
        assert cur['verdict'] == 'pool' and cur.get('batch') == 'G2R-01' and cur.get('grade') == '○', (cur['verdict'], cur.get('batch'), cur.get('grade'))
        cur['verdict'] = 'pool_watch'
        cur['grade'] = '△'
        cur['reason'] = cur['reason'].replace('○ P 池正式入池（档位 ○，复查批 G2R-01）', f'△ P 池观察档（档位 △，复查批 G2R-01 → 补证 {BATCH}）', 1) + MARK + LABEL
        tags = [t for t in cur.get('tags') or [] if t != 'reg_pending'] + ['legal_pending']
        cur['tags'] = tags
        cur['reg'] = fx['reg']
        cur.setdefault('facts', []).extend({'what': w, 'url': u, 'date': DATE} for w, u in fx['facts'])
        cur['recheck'] = BATCH
        rows = {k: v for k, v in s.items() if k != '_meta'}
        cnt = collections.Counter(v['verdict'] for v in rows.values())
        s['_meta'] = {'updated': DATE, 'rules': 'docs/C池三闸筛选_方案_2026-10-29.md §2', 'counts': dict(cnt), 'n': len(rows)}
        out = {'_meta': s['_meta']}
        out.update(sorted(rows.items()))
        json.dump(out, open(SIEVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        changed = True

    with open(WATCH, encoding='utf-8-sig', newline='') as f:
        rws = list(csv.reader(f))
    header, body = rws[0], rws[1:]
    upd = 0
    for r in body:
        if r[0] == CODE and f'补证 {BATCH}' not in r[11]:
            r[1], r[2] = '△', '观察'
            r[7] = '、'.join(s[CODE]['tags'])
            r[11] = r[11] + f'｜补证 {BATCH}：' + LABEL[:150]
            upd += 1
    if upd:
        with open(WATCH, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(body)

    marker = f'## Saga C 复查 · 补证 {BATCH}'
    md = open(ROSTER, encoding='utf-8').read()
    if marker not in md:
        lines = ['', marker + f'（{DATE}，○ → △ 1）', '',
                 f'> G2R-01 入池的 SC-729 Brown Bear（brownbear.ru）按 ИНН 复核官方登记：{LABEL}。事实见 `data/external_clients/xc_path_fill_{DATE}_b2.json` → regfix → SC-729。',
                 '', '| 编号 | 档 | 公司 | 国家 | 区域组 | 判语（摘） |', '|---|---|---|---|---|---|',
                 f'| {CODE} | △ | Brown Bear（brownbear.ru）· 法人待核（ИНН 9728025085 = ООО «Мицар»） | 俄罗斯 | 俄语区 | {LABEL[:150]}… |', '']
        open(ROSTER, 'a', encoding='utf-8').write('\n'.join(lines))
    print(BATCH, 'sieve_changed', changed, 'csv_upd', upd, s['_meta']['counts'])


if __name__ == '__main__':
    main()
