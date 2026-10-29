#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""External XC · X1-02 入池户 reg_pending 补证 批 X1-02R（2026-10-29，T29-U122「继续」）。

对象：X1-02 带 `reg_pending` 的 17 户 P 池 / 观察档（13 ○ + 4 ☆），再加 ○ XC-M132 / M154 / M158 / M168 美国户的州注册号 —— 每户
一次 depth-1 检索（官方登记库 / 公司名录），结果落在 data/external_clients/xc_path_fill_2026-10-29_b2.json['regfix']（只读它，不再外查）。

结果：注册号坐实 11（GB 3 / NO 2 / NL 1 / BG 2 / FR 2 / US SAM 1）→ 去 reg_pending；仍待补 7（IE CRO / GR ΓΕΜΗ / MK ЕМБС / US 州号 ×4，
已补法人名 / 体量者记入判语）。档位变化 1：XC-M072 КОМИКОН ООД ○ → ☆ 观察档（2021 营业额 357k лв、资本 €2,556 → 微型，试单后转正）；
XC-E063 Xentech 名录含「Opgeheven」字样 → 加 status_check；XC-M158 Santa Clara Systems 联邦供应商（SAM UEI / CAGE）→ 加 fed_vendor。
SC-729 Brown Bear（Saga 侧）另见 scripts/saga_clients/sieve_batches/g2r_002_fix.py。

落四处（幂等，按「｜补证 X1-02R」标记）：sieve_x.json（reason 追加 / tags / star / verdict / reg / facts）；研究卡 evidence + notes；
P池_巡检表（档位 / 入池 / 标签 / 备注）；名册小节「External 并池 · 补证 X1-02R」。

用法：python3 sieve_batches_x/x1_002r_regfix.py
"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve_x  # noqa: E402
import research_store  # noqa: E402

BATCH = 'X1-02R'
DATE = '2026-10-29'
ROOT = sieve_x.ROOT
DATA = os.path.join(ROOT, 'data', 'external_clients')
FILL = os.path.join(DATA, f'xc_path_fill_{DATE}_b2.json')
WATCH = os.path.join(ROOT, 'data', 'saga_clients', f'P池_巡检表_{DATE}.csv')
ROSTER = os.path.join(ROOT, 'docs', f'P池_资产池名册_{DATE}.md')
MARK = f'｜补证 {BATCH}（{DATE}）：'

# code → dict(found=bool 注册号坐实, add=[tags], drop=[tags], star=新档位, verdict=新池位, label=一句话)
R = {
    'XC-M177': dict(found=True, label='Companies House 02718521 坐实'),
    'XC-M179': dict(found=True, label='Companies House 01166468 + VAT 坐实（35 人 / $6.9M）'),
    'XC-E068': dict(found=True, label='Companies House 08962068 + VAT 坐实'),
    'XC-M124': dict(found=False, label='法人名修正 D.L.C. DataLink Communications Ltd；CRO 号仍待补'),
    'XC-M100': dict(found=True, label='Org.nr 997 293 851 坐实（22 人；2025 PBT 13.5M NOK）'),
    'XC-M101': dict(found=True, label='Org.nr 968 614 150 坐实（13 人；2025 营收 80M NOK）'),
    'XC-E063': dict(found=True, add=['status_check'], label='KvK 34242736 坐实；名录见「Opgeheven」字样 → 状态待核'),
    'XC-M072': dict(found=True, add=['micro'], star='☆', verdict='pool_watch', label='ЕИК 131340703 坐实但 2021 营业额 357k лв / 资本 €2,556 → 微型 → ○ 转 ☆ 观察档'),
    'XC-M073': dict(found=True, label='ЕИК 130521622 坐实（2020 营业额 €2.62M；21–27 人）'),
    'XC-M087': dict(found=False, label='ΓΕΜΗ 一次检索未中，仍待补'),
    'XC-M116': dict(found=True, label='SIREN 429 607 740 坐实（SARL €120k；3–5 人）'),
    'XC-E059': dict(found=True, label='SIREN 451 371 884 坐实（SARL €9k）'),
    'XC-M083': dict(found=False, label='同名 АСПЕКТ ДОО（软件）排除；ЕМБС 仍待补'),
    'XC-M147': dict(found=False, label='官网法人 International Trade Carrier, LLC + 地址；MD SDAT 号仍待补'),
    'XC-M132': dict(found=False, label='体量 75–80 人 / $5.5M 坐实；TX SOS 号仍待补（补到即 ★）'),
    'XC-M154': dict(found=False, label='体量 15–16 人 / $3M；MD SDAT 号仍待补'),
    'XC-M158': dict(found=True, add=['fed_vendor'], label='SAM.gov UEI KNKRVNQCAEJ7 / CAGE 392W1 坐实（30 人 / $10.6M）'),
    'XC-M168': dict(found=False, label='体量 35 人 / $5–25M；IL SOS 号仍待补'),
}


def main():
    fx = json.load(open(FILL, encoding='utf-8'))['regfix']
    assert set(R) <= set(fx), set(R) - set(fx)
    sieve = sieve_x.load_sieve()
    n = 0
    for code, v in R.items():
        cur = sieve[code]
        if MARK in cur['reason']:
            continue
        assert cur.get('batch') == 'X1-02' and cur['verdict'] in ('pool', 'pool_watch'), (code, cur.get('batch'), cur['verdict'])
        f = fx[code]
        cur['reason'] += MARK + v['label'] + '；' + f['note']
        if f['reg']:
            cur['reg'] = f['reg']
        tags = list(cur.get('tags') or [])
        if v['found']:
            tags = [t for t in tags if t != 'reg_pending']
        for t in v.get('add') or []:
            if t not in tags:
                tags.append(t)
        cur['tags'] = tags
        if v.get('star'):
            cur['star'] = v['star']
        if v.get('verdict'):
            cur['verdict'] = v['verdict']
        cur.setdefault('facts', []).extend({'what': w, 'url': u, 'date': DATE} for w, u in f['facts'])
        cur['recheck'] = BATCH
        # 研究卡：证据 + 备注
        card = research_store.get(code)
        if card:
            urls = {e.get('url') for e in card.get('evidence') or []}
            for w, u in f['facts']:
                if u not in urls:
                    card.setdefault('evidence', []).append({'kind': '登记 / 名录', 'claim': w, 'quote': '', 'url': u, 'date': DATE})
            if f['reg'] and f['reg'] not in (card.get('notes') or ''):
                card['notes'] = ((card.get('notes') or '') + '；' if card.get('notes') else '') + f'{BATCH} 补证：{f["reg"]}'
            research_store.put(card)
        n += 1
    cnt = sieve_x.save_sieve(sieve)

    # 巡检表：档位 / 入池 / 标签 / 备注
    with open(WATCH, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    header, body = rows[0], rows[1:]
    upd = 0
    for r in body:
        code = r[0]
        if code not in R or f'补证 {BATCH}' in r[11]:
            continue
        v = R[code]
        row = sieve[code]
        if v.get('star'):
            r[1] = v['star']
        if v.get('verdict'):
            r[2] = '正式' if v['verdict'] == 'pool' else '观察'
        r[7] = '、'.join(x for x in row['tags'] if x != 'email_found')
        r[11] = r[11] + f'｜补证 {BATCH}：' + (fx[code]['reg'] or v['label'])[:120]
        upd += 1
    with open(WATCH, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(body)

    # 名册小节
    marker = f'## External 并池 · 补证 {BATCH}'
    md = open(ROSTER, encoding='utf-8').read()
    if marker not in md:
        found = [c for c, v in R.items() if v['found']]
        pend = [c for c, v in R.items() if not v['found']]
        lines = ['', marker + f'（{DATE}，坐实 {len(found)} / 仍待补 {len(pend)}）', '',
                 f'> X1-02 入池 / 观察户的 `reg_pending` 各做一次官方登记库 / 名录检索（`data/external_clients/xc_path_fill_{DATE}_b2.json` → regfix）。'
                 f'坐实 {len(found)}（去 reg_pending，注册号写入 sieve_x `reg`）；仍待补 {len(pend)}（已补法人名 / 体量者记入判语）。'
                 '档位变化：XC-M072 КОМИКОН ООД ○ → ☆ 观察档（微型）；XC-E063 加 `status_check`；XC-M158 加 `fed_vendor`。'
                 'Saga 侧 SC-729 Brown Bear ○ → △（ИНН 对应法人为 ООО «Мицар»，与 brownbear.ru 关联未证实）见「Saga C 复查 · 补证 G2R-02」。',
                 '', '| 编号 | 档 | 公司 | 结果 | 注册号 / 说明 |', '|---|---|---|---|---|']
        names = {r[0]: r[3] for r in body}
        for c, v in R.items():
            row = sieve[c]
            lines.append(f'| {c} | {row.get("star", "")} | {names.get(c, c)[:44]} | {"坐实" if v["found"] else "待补"} | {(fx[c]["reg"] or v["label"])[:90].replace("|", "｜")} |')
        lines.append('')
        open(ROSTER, 'a', encoding='utf-8').write('\n'.join(lines))
    print(BATCH, 'sieve_upd', n, 'csv_upd', upd, dict(cnt))


if __name__ == '__main__':
    main()
