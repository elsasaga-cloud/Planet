#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群复核 · 批 LT-R04（T29-U128，2026-10-29）：优先级 2（Saga 冷 B，宽留冷口径曾判「不对位冷户」）中已有研究档类型的 137 户。

发现：这 211 户的「不对位」= build.py 的 fit 标志没从研究档类型回填（表内无「交换机 / 收发器」关键词），不是真不对位。
研究档 type + saga_fit（首推型号 / 切入理由）已写明业务线：安防 / IT / 网络分销与集成、自有品牌商、工业分销 → 行业内 ✔ 对位 ✔ 成单可能 ✔ → 留 B。
打回 C（6）：非本行业代理（SB-070）/ 域名不可达无路径（SB-080）/ 进出口中介仅 VC 一次 RFQ（SB-469）/ 制造商销售代表非采购主体（SB-845）/
            Extreme 专营网店白牌契合低（SB-880）/ 定位转型待核不明朗（SB-473）。
继续待过（7，业务「待核」且无法从研究档判断）：SB-642 / 653 / 661 / 668 / 691（土耳其 IT 公司）、SB-855（捷克经营状态待核）、SB-821（白俄 IT 经销待核）。
研究档 type 为空的 74 户不在本批（下批查官网）。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lt_review_lib import run, DATA, RESEARCH  # noqa: E402

BATCH = 'LT-R04'
DROP = {
    'SB-070': 'neowine（韩国）：研究档「潜在代理（非本行业）」，唯一动作是 48 口索样后无下文 → 非本行业 → C 储备',
    'SB-080': 'cyber-tec.net（伊拉克）：域名不可达（快照失败），百兆收发器一次询价后无路径 → C 储备；对方来信即回 B',
    'SB-469': 'novytel（捷克）：进出口贸易中介，仅一次 VC（光端机）RFQ = 本职线 + 中介 → C 储备（dayjob_fit）',
    'SB-845': 'Osborn Sales（美国）：制造商销售代表公司，非采购主体 → C 储备（如要代理合作另议）',
    'SB-880': 'netsolutions（澳大利亚）：Extreme Networks 专营网店，白牌契合度低、预期低 → C 储备',
    'SB-473': 'bturesearch（美国）：边缘基础设施平台商「定位转型待核」，业务不明朗 → C 储备；明朗后回 B',
}
HOLD = {'SB-642', 'SB-653', 'SB-661', 'SB-668', 'SB-691', 'SB-855', 'SB-821'}


def main():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    V = {}
    for e in ents:
        rs = e.get('research') or {}
        rv = rs.get('lt_review') or {}
        if rv.get('prio') != 2 or rv.get('status') != '待过':
            continue
        t = (rs.get('type') or '').strip()
        if not t or e['code'] in HOLD:
            continue
        if e['code'] in DROP:
            V[e['code']] = ('打回C', DROP[e['code']], [])
            continue
        sf = rs.get('saga_fit') or {}
        why = re.sub(r'\s+', ' ', (sf.get('why') if isinstance(sf, dict) else str(sf)) or '')[:140]
        V[e['code']] = ('留B', f'桌面复核（研究档类型 + 对位首推）：{t}；切入：{why}；行业内 ✔ 对位 ✔（宽留冷「不对位」系 fit 标志未回填，非真不对位）', [])
    for c in DROP:
        assert c in V, c
    print('batch size', len(V))
    run(BATCH, V)


if __name__ == '__main__':
    main()
