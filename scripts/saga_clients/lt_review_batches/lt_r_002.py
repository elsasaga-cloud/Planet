#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群复核 · 批 LT-R02（T29-U128，2026-10-29）：优先级 1（C 捞上来的 Saga 户）· 四主区 + 波兰 / 欧洲其他 · 余下 61 户（★★ / ★ / ○ 坐实档）。

过法：桌面复核。这 61 户在闸 2（G2-124…136 / G2R-01/02）已拿到登记号 / 规模 / 业务线 / 进口品牌等证据（见 sieve.json reason），
对「行业内 + 对位 + 成单可能」三问全部成立（品牌商 OEM 目标 / 多牌进口分销 / 工业分销 / 成单户），不需要新查；本批不新检索。
例外规则：Q-33（经销体系现供）★ 品牌商 → 留 B 但 q33_hold 只盯不发（SC-2609 Partizan）；全退信户留 B 但标「补路径」（SC-634）。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lt_review_lib import run, DATA  # noqa: E402

BATCH = 'LT-R02'
CODES = ['SC-1230', 'SC-1443', 'SC-1450', 'SC-161', 'SC-1675', 'SC-1965', 'SC-2066', 'SC-2255', 'SC-2429', 'SC-2481', 'SC-2510', 'SC-2516',
         'SC-2542', 'SC-259', 'SC-2598', 'SC-2657', 'SC-276', 'SC-2776', 'SC-2834', 'SC-2943', 'SC-2954', 'SC-503', 'SC-568', 'SC-571', 'SC-634',
         'SC-671', 'SC-678', 'SC-683', 'SC-770', 'SC-855', 'SC-956', 'SC-1014', 'SC-1033', 'SC-1053', 'SC-1181', 'SC-1194', 'SC-1215', 'SC-1335',
         'SC-1629', 'SC-1713', 'SC-1714', 'SC-1881', 'SC-2219', 'SC-2258', 'SC-2452', 'SC-2609', 'SC-274', 'SC-2760', 'SC-2941', 'SC-2957',
         'SC-3135', 'SC-3302', 'SC-345', 'SC-371', 'SC-468', 'SC-490', 'SC-575', 'SC-656', 'SC-783', 'SC-908', 'SC-925']
NOTES = {
    'SC-259': '成单户（展会买样机 + 问 500 台 + 政府项目），公司名仍缺 → 留 B；Simon / Evelyn 微信补公司名后再坐实',
    'SC-2609': 'Q-33：配套 PoE 现由洪瑞供 → 留 B 但 q33_hold 只盯不发（欧洲自有品牌，换供应商时第一时间知道）',
    'SC-634': '18 推全退信 → 路径待补（官网联系表 / 找采购新地址），补到前只巡检不发',
    'SC-2776': '≈2,500 人巨头 → 长线（不期待快单，季度一封新品即可）',
    'SC-1714': '表内「智利」实为瑞士（CHE-105.959.689）→ country_fix 随下一次 build 处理',
    'SC-345': 'DC 开放网络集成 → CENTEC 敲门砖线（STH 一页纸，客户稿不提 SONiC）',
}
STRIP = re.compile(r'^[★☆○△]+ P 池(正式入池|观察档)（[^）]*）：')


def main():
    s = json.load(open(os.path.join(DATA, 'sieve.json'), encoding='utf-8'))
    V = {}
    for c in CODES:
        why = re.sub(r'\s+', ' ', STRIP.sub('', s[c].get('reason') or ''))
        why = why[:220] + ('…' if len(why) > 220 else '')
        extra = NOTES.get(c)
        V[c] = ('留B', f'桌面复核（闸 2 证据充分，三问成立）：{why}' + (f'；备注：{extra}' if extra else ''), [])
    run(BATCH, V)


if __name__ == '__main__':
    main()
