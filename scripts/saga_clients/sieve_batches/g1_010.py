#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 10 批（2026-10-29）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 551–605 户（按编号序，SC-756 … SC-877）。

构成：全部「群发冷名单无回应 · 名单内未触达」或「综合分低 · 未触达」的欧美 / 土耳其 / 波兰网店 · 光模块商 · 工业分销冷名单（仅 infralinknetworks.ca 推过 8 次）。
  · 候选 6 = 已进口 Wi-Tek 同类品牌（expressalarm.cz / htv-hodina.cz / megamobile.be / mastdigital.co.uk + 大华）或 波兰工业分销主体（ELMARK）或 数量信号（itjan.de「100 个用于 Amazon 销售」）→ 闸 2 查底数。
  · 永久 pass 0：本批无刚性 pass 证据（企业邮箱域正常、无婉拒 / 停发要求）。
  · 其余留 C：巨头 / 同行（Distrelec · Murrelektronik · Lorex · Multilink · Flexoptix · Electro Standards）/ 本职线（CWDM SFP · 彩光模块 → dayjob_fit）/ 销售平台 · 网店 / 仅卖欧美日名牌（Perle · Red Lion · Antaira · TRENDnet · StarTech · Digitus · D-Link · Tycon）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_010.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批10_2026-10-29.md）
"""
import os
import sys
import json
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import sieve  # noqa: E402
from g1_005 import compose, SUB_WHY  # noqa: E402

SUB_WHY.insert(0, (r'用户判定不行', 'Simon 曾判不行 / 不相关；无刚性 pass 证据、企业邮箱域正常 → 留 C（不主动碰，除非出现新信号）'))

BATCH = 'G1-10'
DATE = '2026-10-29'
CODES = ["SC-756", "SC-759", "SC-760", "SC-764", "SC-766", "SC-767", "SC-768", "SC-769", "SC-770", "SC-771", "SC-773", "SC-774", "SC-775", "SC-779", "SC-780", "SC-783", "SC-786", "SC-787", "SC-788", "SC-789", "SC-790", "SC-793", "SC-794", "SC-797", "SC-798", "SC-803", "SC-804", "SC-809", "SC-811", "SC-813", "SC-819", "SC-821", "SC-822", "SC-827", "SC-833", "SC-834", "SC-835", "SC-837", "SC-843", "SC-845", "SC-847", "SC-849", "SC-855", "SC-856", "SC-857", "SC-858", "SC-863", "SC-864", "SC-867", "SC-868", "SC-870", "SC-871", "SC-872", "SC-875", "SC-877"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2 ----
    'SC-770': ('candidate', '波兰 ELMARK Automatyka（elmark.com.pl；很多牌子 = 波兰工业自动化 / 工业网络分销主体）：波兰 + 分销主体 + 对位 ✔；名单内未触达 → 闸 2 查底数（冷户四条待坐实）', []),
    'SC-783': ('candidate', '捷克 Express Alarm（expressalarm.cz；卖几个有名牌子 + Wi-Tek 很多其他产品）：欧洲 + 已进口中国同类品牌 + 对位 ✔；未触达 → 闸 2 查底数，低优先', []),
    'SC-809': ('candidate', '捷克 HTV Hodina（htv-hodina.cz；Wi-Tek）：欧洲 + 已进口中国同类品牌 + 对位 ✔；未触达 → 闸 2 查底数，低优先', []),
    'SC-827': ('candidate', '德国 ITJAN / Janetzky（itjan.de / janetzky.net；表内「100 个 用于 Amazon 销售」= 数量信号）：四主区 + 数量意向 + 对位 ✔；→ 闸 2 查底数（亚马逊卖家微型 → 预付）', []),
    'SC-855': ('candidate', '英国 Mast Digital（mastdigital.co.uk；Dahua + Wi-Tek）：四主区 + 已进口中国同类品牌 + 对位 ✔；未触达 → 闸 2 查底数', []),
    'SC-856': ('candidate', '比利时 Megamobile（megamobile.be；Wi-Tek）：欧洲 + 已进口中国同类品牌 + 对位 ✔；未触达 → 闸 2 查底数，低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-759': ('keep_C', '意大利 Distrelec（distrelec.it / .com；目录分销巨头，主要是 Planet 的）：巨头采购体系；未触达 → 留 C（oem 备注：Planet 渠道）', []),
    'SC-764': ('keep_C', '爱沙尼亚 dwdm.me（CWDM SFP）：光模块 = 本职线 / 同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-766': ('keep_C', '拉脱维亚 Edge Optic（edgeoptic.com；彩光模块）：光模块同行 / 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-768': ('keep_C', '美国 Electro Standards Laboratories（electrostandards.com；自产光开关 / bypass / 转换器）：同行制造商；未触达 → 留 C', []),
    'SC-786': ('keep_C', '美国 Fibertool（fibertool.com；CWDM SFP）：光模块 = 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-789': ('keep_C', '德国 Flexoptix（flexoptix.net；基本都是 SFP = 光模块品牌商）：同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-794': ('keep_C', '德国 GHIP Systems（ghipsystems.com；CWDM SFP）：光模块 = 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-819': ('keep_C', '加拿大 Infralink Networks（infralinknetworks.ca；无源配件为主、有 MC）：品类偏无源；8 推 0 回 → 留 C', []),
    'SC-847': ('keep_C', '美国 Lorex（lorex.com；消费级 CCTV 品牌商）：巨头 / 自有供应链；未触达 → 留 C', []),
    'SC-849': ('keep_C', '美国 Luma Optics（lumaoptics.net；基本都是 SFP）：光模块同行 / 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-858': ('keep_C', '英国 Metrodata / Kenton Group（metrodata.co.uk；CWDM SFP 为主）：光模块 = 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-867': ('keep_C', '美国 Multilink（multilink.us；宽带 / 光纤机柜制造商，很多牌子的产品）：同行属性 + 冷；未触达 → 留 C', []),
    'SC-868': ('keep_C', '美国 Murrelektronik（murrelektronik.com；工业连接巨头）：巨头采购体系；未触达 → 留 C', []),
    'SC-877': ('keep_C', '荷兰 Netways Europe（netwayseurope.com；CWDM SFP / Network）：光模块为主 = 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
}


def main():
    assert len(CODES) == 55 and len(set(CODES)) == 55
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    rd = os.path.join(sieve.ROOT, 'data', 'saga_clients', 'research')
    V = {}
    for code in CODES:
        e = ents[code]
        assert e.get('grade') == 'C', code
        cur = sv.get(code) or {}
        assert not cur or cur.get('batch') == BATCH, ('already judged elsewhere', code, cur)
        if code in OVERRIDE:
            V[code] = OVERRIDE[code]
        else:
            p = os.path.join(rd, code + '.json')
            research = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None
            reason, tags = compose(e, research)
            V[code] = ('keep_C', reason, tags)
    for code in OVERRIDE:
        assert code in V, ('override not in batch', code)
    for code, (verdict, reason, tags) in V.items():
        assert verdict in ('pass_final', 'keep_C', 'candidate') and len(reason) >= 12, code
        cur = sv.get(code) or {}
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True, 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    tg = Counter(t for v in V.values() for t in v[2])
    L = [f'# C 池 · 闸 1 · 第 10 批（{DATE}）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 551–605 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：全部冷名单未触达（仅 infralinknetworks.ca 推过 8 次）。候选 6 = 已进口 Wi-Tek 同类品牌（Express Alarm / HTV Hodina / Megamobile / Mast Digital + 大华）、波兰工业分销主体（ELMARK）、数量信号（ITJAN 100 个 Amazon）；'
         '永久 pass 0（无刚性证据）。留 C：巨头 / 同行（Distrelec · Murrelektronik · Lorex · Multilink · Flexoptix · Electro Standards）、本职线（CWDM SFP · 彩光模块 → dayjob_fit）、销售平台 / 网店、仅卖欧美日名牌。「stop」flag = 文本命中，不作 pass 依据。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批10_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
