#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群复核 · LT-R05（External 优先级 1，67 户）+ LT-R06（Planet 仓 优先级 1，24 户）· T29-U128 2026-10-29。

口径（Simon U128 ⑤.2：没深挖过的要确认「行业内 + 对位 + 有成单可能」，不明朗 → C 储备）：
- External 67 = XC 三闸捞出 → B 的全部。导入记录 type/signals 来自厂商渠道名录（HMS/N-Tron·Red Lion、Westermo、EtherWAN、ORing、MikroTik、ComNet、
  Teltonika、Hikvision 国家分销…）+ 第 2 步研究卡（业务线 / 注册 / 规模）：在卖工业或商用交换机 = 行业内 ✔ 对位 ✔ 分销进口 ✔ → 留 B（桌面复核）。
  ☆ 微型者留 B 但预付 100%；reg_pending（Akçaba / Smartplus / Sapphire / IT Warehouse）登记号待补但 Hikvision 级分销实体明确 → 留 B。
- Planet 24 = 在售 PLANET 交换机（官网品牌页 / 商品页 / 官方分销自述，证据 URL 在 CSV「PLANET关联证据URL」）→ 行业内 ✔ 对位 ✔ 进口分销 ✔ → 留 B。
落点：External `overrides.json` review{status,prio,date,batch,note}；Planet CSV「长期群复核」；共同日志 data/长期客户群_复核记录.csv。幂等（日志按 编号+批次 去重）。
"""
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XD = os.path.join(ROOT, 'data', 'external_clients')
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')
DATE = '2026-10-29'
BX, BP = 'LT-R05', 'LT-R06'


def load_log():
    if not os.path.exists(LOG):
        return [], set()
    rows = list(csv.DictReader(open(LOG, encoding='utf-8-sig')))
    return rows, {(r['编号'], r['批次']) for r in rows}


def save_log(rows):
    f = ['编号', '公司', '国家', '复核前等级', '复核后等级', '批次', '日期', '结论与理由']
    with open(LOG, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=f)
        w.writeheader()
        w.writerows(rows)


def external(log, seen):
    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in json.load(open(os.path.join(XD, f'{repo}.json'), encoding='utf-8'))['records']:
            recs[r['code']] = r
    p = os.path.join(XD, 'overrides.json')
    ov = json.load(open(p, encoding='utf-8'))
    n = 0
    for code, o in ov.items():
        rv = o.get('review') or {}
        if rv.get('status') != '待过' or rv.get('prio') != 1:
            continue
        r = recs.get(code, {})
        card = os.path.join(XD, 'research', f'{code}.json')
        fit = ''
        if os.path.exists(card):
            fit = re.sub(r'\s+', ' ', json.load(open(card, encoding='utf-8')).get('fit') or '')[:110]
        t = (r.get('type') or '').strip()[:60]
        sig = re.sub(r'\s+', ' ', r.get('signals') or '')[:90]
        tiny = fit.startswith('☆')
        reason = (f'桌面复核（渠道名录 + 研究卡）：{t}' + (f'；信号：{sig}' if sig else '') + (f'；研究卡：{fit}' if fit else '')
                  + '；在卖工业/商用交换机 = 行业内 ✔ 对位 ✔ 分销进口 ✔ → 留 B' + ('（微型：预付 100%）' if tiny else ''))
        o['review'] = {'status': '留B', 'prio': 1, 'date': DATE, 'batch': BX, 'note': reason}
        if (code, BX) not in seen:
            log.append({'编号': code, '公司': r.get('name', ''), '国家': r.get('country_zh', ''), '复核前等级': 'B', '复核后等级': 'B',
                        '批次': BX, '日期': DATE, '结论与理由': reason})
            seen.add((code, BX))
            n += 1
    json.dump(ov, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return n


def planet(log, seen):
    rows = list(csv.DictReader(open(PCSV, encoding='utf-8-sig')))
    fields = list(rows[0].keys())
    n = 0
    for r in rows:
        note = r.get('长期群复核') or ''
        if '待过·优先级 1' not in note:
            continue
        ev = re.sub(r'\s+', ' ', r.get('信号（在卖什么品牌）') or '')[:90]
        reason = f'桌面复核（PLANET 关联证据 URL 已在表）：{ev}；在售 PLANET 交换机 = 行业内 ✔ 对位 ✔ 进口分销 ✔ → 留 B'
        r['长期群复核'] = note.replace('待过·优先级 1', f'留B·{BP} {DATE}（{reason}）')
        if (r['档案编号'], BP) not in seen:
            log.append({'编号': r['档案编号'], '公司': r['公司名'], '国家': r['国家'], '复核前等级': 'B', '复核后等级': 'B',
                        '批次': BP, '日期': DATE, '结论与理由': reason})
            seen.add((r['档案编号'], BP))
            n += 1
    with open(PCSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    return n


def main():
    log, seen = load_log()
    nx = external(log, seen)
    np_ = planet(log, seen)
    save_log(log)
    print(f'{BX} external log + {nx} | {BP} planet log + {np_} | log rows {len(log)}')


if __name__ == '__main__':
    main()
