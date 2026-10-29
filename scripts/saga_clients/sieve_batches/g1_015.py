#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 15 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 166–220 户（按综合分序，SC-497 … SC-592）。

构成：澳新 / 台湾 / 韩国 / 泰国 / 印尼 / 菲律宾冷名单（0 触达或推 1 次）、韩国 23 推 0 回户、中东零星。
  · 口径同桶 ⑥ 首批：四主区外默认留 C；「已进口中国 / 台湾同类品牌」+ 俄 / 印 / 韩（或同区先例）→ 闸 2 低优先；「自有品牌 = OEM 品牌商」不限国别 → 闸 2 低优先；退信但域正常 + 数量 / 进口信号 → 闸 2 找新地址。
  · 候选 2 = Nextik IN（BDCOM 核心交换机 + WDM = 进口中国同类，点名印度）/ Leap Networks AE（表内「4 光 4 管理 PoE 64 个」= 数量询盘，Tarek Bary 邮箱退信但域正常 → 闸 2 找新地址 / WA）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：澳新平台与分销（PLE · Willdoo / Streakwave · X-ON · Tekdis ORing · Optical Solutions 台湾牌 · ITPlus Wi-Tek · Not Just Cables）/ 台湾周边与 CCTV 厂（JSTT · Netiotek · QCTek · SCT · Songxin · TopsCCC · TWPro-Link · Waveform）/ 韩国美牌专营（Korins · PDK · TM Solutions Red Lion）/ 韩国 23 推 0 回（Megacraft WDM · MRDNS）/ 泰 · 印尼 · 菲 · 缅 推 1 次 0 回储备（Optiviel「要特别注意」· Gigantika 3 牌 · Ronisys Genata · Macktech Elink）/ 同行（SolidRun）/ 本职线 dayjob_fit。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_015.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批15_2026-10-29.md）
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

BATCH = 'G1-15'
DATE = '2026-10-29'
CODES = ["SC-497", "SC-498", "SC-499", "SC-500", "SC-501", "SC-502", "SC-504", "SC-505", "SC-507", "SC-508", "SC-509", "SC-510", "SC-511", "SC-512", "SC-513", "SC-514", "SC-516", "SC-517", "SC-519", "SC-520", "SC-521", "SC-523", "SC-525", "SC-526", "SC-527", "SC-528", "SC-529", "SC-530", "SC-531", "SC-533", "SC-534", "SC-535", "SC-536", "SC-537", "SC-538", "SC-539", "SC-540", "SC-541", "SC-542", "SC-543", "SC-549", "SC-554", "SC-555", "SC-558", "SC-564", "SC-569", "SC-570", "SC-573", "SC-576", "SC-577", "SC-578", "SC-580", "SC-582", "SC-585", "SC-592"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-509': ('candidate', '印度 Nextik（nextik.co.in；表内「BD 的核心交换机 / WDM 核心交换机」= 在售 BDCOM 中国品牌）：进口中国同类 ✔ 对位 ✔（企业 / DC 线）Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-577': ('candidate', '阿联酋 / 沙特 Leap Networks（leap-networks.ae；表内「4 光 4 管理 PoE 64 个」= 数量询盘；KP Tarek Bary，邮箱退信 8 次但域正常，+971 手机在表）：数量信号 ✔ 对位 ✔ 退信 ≠ 死 → 闸 2 找新地址 + WA 路径；四主区外，低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-497': ('keep_C', '新西兰 ITPlus（itplus.co.nz；在卖 Wi-Tek 商业 / 工业 FS）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-512': ('keep_C', '澳大利亚 Optical Solutions（opticalsolutions.com.au；工业 FS / MC / SFP / 串口分销，卖台湾的牌子）：进口台湾同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-516': ('keep_C', '澳大利亚 PLE Computers（ple.com.au；大型 IT 零售平台，很多牌子 / Planet）：大平台 → 留 C', []),
    'SC-526': ('keep_C', '以色列 SolidRun（solid-run.com；Marvell 平台 SBC / 网络设备厂商）：同行 → 留 C', []),
    'SC-534': ('keep_C', '澳大利亚 Tekdis（tekdis.com.au；ORing 工业 FS / bypass / serial 分销）：进口台湾同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-542': ('keep_C', '澳大利亚 X-ON Electronics（x-on.com.au；xonelec.kr 域 nxdomain；大型元器件分销）：巨头体系 → 留 C', []),
    'SC-555': ('keep_C', '印尼 PT. Optiviel Cable（optiviel.com；行业分销 MC / SFP / 14 槽机架 / 工业 FS，Simon 注「工业 FS 这个要特别注意」）：进口同类 ✔ 但四主区外非点名国；推 1 次 0 回 → 留 C（储备；若点名东南亚可升候选）', []),
    'SC-570': ('keep_C', '印尼 Gigantika（gigantika.co.id；管理 FS / PoE，工业 FS 在用 3 个品牌）：多牌进口 ✔ 但四主区外非点名国；推 1 次 0 回 → 留 C（储备）', []),
    'SC-592': ('keep_C', '菲律宾 Ronisys（ronisys.ph；在卖 Genata 商业 PoE + 锐捷）：进口中国同类 ✔ 但四主区外非点名国；推 1 次 0 回 → 留 C（储备）', []),
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
    L = [f'# C 池 · 闸 1 · 第 15 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 166–220 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：澳新 / 台 / 韩 / 泰 / 印尼 / 菲冷名单（0 触达或推 1 次）、韩国 23 推 0 回户、中东零星。口径同桶 ⑥ 首批。候选 2 = Nextik（IN，BDCOM）/ Leap Networks（AE，64 台数量询盘 + 退信找新地址）；永久 pass 0。留 C：澳新平台与分销、台湾周边与 CCTV 厂、韩国美牌专营、韩国 23 推 0 回、东南亚推 1 次 0 回储备（Optiviel「要特别注意」）、同行、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批15_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
