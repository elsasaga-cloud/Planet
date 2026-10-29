#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 126 批（2026-10-29）—— 闸 1 第 07 / 08 批候选中的四主区 + 波兰 28 户（US 13 / GB 8 / DE 3 / PL 4），底数见 registry_batches/b126_c.py。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-126）：
  · pool_candidate = 法人 / 官网坐实或部分坐实 + §5 条数够（有关系户 ≥2 条 / 冷户 ≥4 条）→ 「P 池候选」，等 Simon 定夺。
  · keep_C = 红旗（虚拟地址微型 / 品牌壳）/ 未坐实 → 回 C 储备。无新 pass_final。
tier：★★ 首选 / ★ 品牌商 · 中型分销 / ○ 分销 · 进口商 / △ 观察档（微型 / 终端 / 巨头体系 / 法人存疑 / 区域外）。

用法：python3 sieve_batches/g2_126.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批126_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-126'
DATE = '2026-10-29'

V = {
    # 美国
    'SC-2255': ('pool_candidate', '★ 自有品牌 · OEM 30%：PoE Texas（Austin 2011；约 10 人；自有 PoE 配件线；CEO tandrews@ / CTO jherbst@ 都在表）部分坐实（州号未取）；自有品牌 ✔ 进口 Utepo ✔ 主区 ✔ 决策人直达 ✔ → P 池候选；Simon 曾判不行，可否决', ['oem_target']),
    'SC-2402': ('pool_candidate', '△ 观察档 · 分销 20%：SISEGUSA = Sistemas de Seguridad S.A.（厄瓜多尔 Guayaquil 安防批发 + 迈阿密 LLC）→ 国别纠偏 美国 → 厄瓜多尔；进口 Utepo ✔ 对位 ✔ 坐实 ✔ 但区域外 → 入池观察档；Simon 曾判不行，可否决', []),
    'SC-2418': ('pool_candidate', '○ 中型分销 20%：Streakwave Wireless, Inc.（San Jose 总部 + 4 分仓；无线 / 安防 / 网络增值分销）部分坐实；国别纠偏 加拿大 → 美国；对位 ✔ 主区 ✔ 体量 ✔ 坐实 ✔ → P 池候选（长线）；Simon 曾判不行，可否决', ['dayjob_fit']),
    'SC-2429': ('pool_candidate', '★ 中型分销 20%：El Paso Communication Systems, Inc. — EPCOM（1987；95 人；$23.7M；三仓；PLANET 双线在售；purchasing@ 在表）坐实；对位 ✔ 主区 ✔ 体量 ✔ 坐实 ✔ → P 池候选；Simon 曾判不行，可否决', []),
    'SC-2542': ('pool_candidate', '★ 自有品牌 + 白标 · OEM 30%：Grid Connect, Inc.（Naperville 2002；25 人；ISO 9001；分销 + GRID 自有产品 + 白标 / 定制 IoT；CEO Adam Justice）坐实；OEM ✔ 主区 ✔ 对位 ✔ 互动过 ✔ → P 池候选；Simon 曾判不行，可否决', ['oem_target']),
    'SC-2597': ('pool_candidate', '△ 观察档 · 分销 20%：Urban Security Group（布鲁克林家族 CCTV 批零 40+ 年）部分坐实；进口洪瑞 ✔ 主区 ✔ 对位 ✔ 微型 → 入池观察档；Q-33 口径；Simon 曾判不行，可否决', []),
    'SC-2606': ('pool_candidate', '○ 工业分销 20%：Logicbus, Inc.（Chula Vista 2001；40 人；美墨双边；Daniel Flores 墨西哥分公司经理 = 表内邮箱；有采购专员）坐实；进口 Atop / 三旺 ✔ 主区 ✔ 对位 ✔ 具名 KP ✔ → P 池候选；Simon 曾判不行，可否决', []),
    'SC-2619': ('keep_C', '闸 2 查实：Alantek Communications（新加坡 Pte Ltd 运营的布线品牌，休斯敦联络地址；1–10 人；以无源为主）→ 微型品牌壳，回 C 储备', []),
    'SC-2622': ('keep_C', '闸 2 未坐实：cctvvideo.com 1 查仅返回 e-link 供货商页 + Simon 判不行 → 回 C 储备', ['dayjob_fit']),
    'SC-2657': ('pool_candidate', '★ 自有品牌 · OEM 30%：Lynn Electronics Corporation（Ivyland PA 1964；$18.6M；29–108 人；进口 Volktek；Director Data Center Solutions 在职）坐实；自有品牌 ✔ 进口经验 ✔ 主区 ✔ 体量 ✔ → P 池候选（DC 线可提 CENTEC）；Simon 曾判不行，可否决', ['oem_target', 'dayjob_fit']),
    'SC-284': ('pool_candidate', '△ 观察档 · OEM 30%：Data Comm for Business, Inc.（Dewey IL 1981；SAM.gov UEI YX2BCLJKZ456 有效至 2027；自研数据通信设备；联邦交通客户）坐实；自有型号 ✔ 主区 ✔ 对位 ✔ 但联邦 TAA 门槛 → 入池观察档', ['oem_target']),
    'SC-2993': ('pool_candidate', '○ 自有 logo 贴牌 · OEM 30%：Cables N More（Quakertown PA；1–50 人；自己的 logo 和型号；进口宇航）部分坐实；OEM ✔ 进口经验 ✔ 主区 ✔ 对位 ✔ → P 池候选（退信 → 找 owner 新地址）；Simon 曾判不行，可否决', ['oem_target', 'dayjob_fit']),
    'SC-503': ('pool_candidate', '★ 品牌商 · OEM 30%：LUTZE Inc.（Charlotte NC；73–77 人；德国 Lütze 集团北美总部；自有品牌工业交换机贴牌）坐实；OEM ✔ 主区 ✔ 对位 ✔ 体量 ✔ → P 池候选（同步核德国总部采购）', ['oem_target']),
    # 英国
    'SC-2383': ('pool_candidate', '○ 自有品牌 · OEM 30%：3G Router Store = Westlake / Millbeck Communications（Romford；2002；2–10 人；自有品牌 Proroute 路由 / Fullband 天线）部分坐实；OEM ✔ 进口洪瑞 ✔ 主区 ✔ 对位 ✔ → P 池候选；Q-33 口径；Simon 曾判不行，可否决', ['oem_target']),
    'SC-2608': ('pool_candidate', '△ 观察档（长线）· OEM 30%：Mayflex（Birmingham 1917；250 人；Sonepar UK 子公司；自有品牌 Excel Networking；Andrew Percival 在表）坐实；OEM ✔ 主区 ✔ 具名 KP ✔ 但巨头采购体系 → 入池长线观察档；Simon 曾判不行，可否决', ['oem_target']),
    'SC-2728': ('pool_candidate', '△ 观察档 · 分销 20%：Blue Helix Limited（CH 04836349；AMG / ComNet / D-Link 分销；28 人）部分坐实，名录标 SIC 99999 休眠 vs 官网在营 → 法人待 CH 直查；分销 ✔ 主区 ✔ 对位 ✔ → 入池观察档 + 预付；Simon 曾判不行，可否决', []),
    'SC-2802': ('pool_candidate', '△ 观察档 · 集成商 25%：Euro Security Solutions Limited（CH 11094000；2017；伦敦；微型）坐实；样品意向 ✔ 主区 ✔ 对位 ✔ → 入池观察档（退信 → 走表内 WA）+ 预付', ['dayjob_fit']),
    'SC-2809': ('keep_C', '闸 2 红旗：Ogar Technology Limited（伦敦虚拟办公室地址；4 人；主销尼日利亚；美国壳 LLC）→ 不动，回 C 储备', []),
    'SC-2954': ('pool_candidate', '★ 自有品牌 · OEM 30%：Videcon Ltd（Heckmondwike 1995；£36.27M；150 人；自有品牌 Concept Pro；trade-only 分销）坐实；OEM ✔ 主区 ✔ 体量 ✔ 对位 ✔ → P 池候选（退信 → 找产品经理）；Simon 曾判不行，可否决', ['oem_target']),
    'SC-2976': ('pool_candidate', '○ 进口商 + 自有品牌 · 分销 20% / OEM 30%：Blake UK Ltd（Sheffield 1971；20–24 人；£2.2M；天线制造 + 进口商；MD Paul Blake）部分坐实；进口 ✔ 自有品牌 ✔ 主区 ✔ 对位 ✔ → P 池候选；Simon 曾判不行，可否决', ['oem_target']),
    'SC-331': ('pool_candidate', '○ 工业分销 20%：Industrial Communication Products Ltd（Toddington 2008；Advantech / INSYS 英国分销；铁路占比高）部分坐实；分销 ✔ 进口台湾品牌 ✔ 主区 ✔ 对位 ✔ = 冷户四条 → P 池候选；守界：只做非轨交场景', []),
    # 德国
    'SC-2262': ('pool_candidate', '○ 集成 + 分销 20%：1ST-embedded GmbH（Neu Wulmstorf 2010；CEO Sven Trommer = 表内邮箱）部分坐实（HRB 未取）；决策人直达 ✔ 进口 ISON ✔ 主区 ✔ 对位 ✔ → P 池候选；Simon 曾判不行，可否决', []),
    'SC-2488': ('pool_candidate', '○ 分销 20%：Fiber24 GmbH（HRB 104376 Hamburg；2008；RIK Holding 控制；Planet 在售）坐实；分销 ✔ 主区 ✔ 坐实 ✔ 对位 ✔ = 冷户四条 → P 池候选；Simon 曾判不行，可否决', ['dayjob_fit']),
    'SC-364': ('pool_candidate', '△ 观察档 · 成单回访：EasyWind GmbH（Enge-Sande；小型风机制造商；RTS 成单 4 台 MC 自用）坐实；成单 ✔ 主区 ✔ 对位 ✔ ≥2 条 → 入池观察档，复购体量低 → Simon 定', ['dayjob_fit']),
    # 波兰
    'SC-276': ('pool_candidate', '★ 品牌商 · OEM 30%：ASSMANN Distribution Sp. z o.o.（Warszawa；NIP 8951883569；ASSMANN Group / DIGITUS 波兰分销公司）坐实；OEM ✔ 波兰 ✔ 对位 ✔ 体量 ✔ → P 池候选（同步找德国总部产品管理）', ['oem_target']),
    'SC-2834': ('pool_candidate', '★ 自有品牌 · OEM 30%：DIPOL Sp. j.（Kraków 1990；KRS 0000094703；自有品牌 Signal / Ultimax / Ultipower；全国分部）坐实；OEM ✔ 波兰 ✔ 体量 ✔ 对位 ✔ → P 池候选；Simon 曾判不行，可否决', ['oem_target', 'dayjob_fit']),
    'SC-2943': ('pool_candidate', '★ 自有品牌 · OEM 30%：Batna Sp. z o.o. — Extralink（Częstochowa；KRS 0001003926；20+ 年；x-kom / Neonet 渠道；Ekstraklasa 赞助）坐实；OEM ✔ 波兰 ✔ 体量 ✔ 对位 ✔ → P 池候选（退信 → 找产品经理）；Simon 曾判不行，可否决', ['oem_target']),
    'SC-3023': ('pool_candidate', '△ 观察档 · 分销 20%：NetTrans Jarosław Żydek（Lublin 个体；NIP 712-239-07-96；进口 3C Link / ONV）坐实；进口 ✔ 波兰 ✔ 坐实 ✔ 对位 ✔ 但个体微型 → 入池观察档 + 预付；Simon 曾判不行，可否决', []),
}


def main():
    assert len(V) == 28
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    for code, (verdict, reason, tags) in V.items():
        assert verdict in ('pool_candidate', 'keep_C', 'pass_final') and len(reason) >= 12, code
        cur = sv.get(code) or {}
        assert cur.get('verdict') in ('candidate', verdict) or cur.get('batch') == BATCH, ('not a gate-1 candidate', code, cur)
        g1_batch = cur.get('g1_batch') or (cur.get('batch') if cur.get('gate') == 1 else None)
        g1_reason = cur.get('g1_reason') or (cur.get('reason') if cur.get('gate') == 1 else None)
        row = {'verdict': verdict, 'gate': 2, 'rule': 'G2', 'reason': reason, 'date': DATE, 'manual': True, 'batch': BATCH,
               'g1_batch': g1_batch, 'g1_reason': g1_reason}
        old_tags = set(cur.get('tags') or [])
        new_tags = sorted(old_tags | set(tags))
        if new_tags:
            row['tags'] = new_tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    L = [f'# C 池 · 闸 2 · 第 126 批（{DATE}）—— 闸 1 第 07 / 08 批候选 · 四主区 + 波兰 28 户查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b126_c.py`，第 126 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 15 / 部分坐实 12（US 州登记号常态未取；GB 3 户 CH 号未取；1ST-embedded / EasyWind HRB 未取）/ 未坐实 1（cctvvideo.com）/ 红旗 2（Ogar 虚拟地址微型 → 回 C；Blue Helix 法人状态存疑 → 观察档）。国别纠偏 2（SISEGUSA → 厄瓜多尔；Streakwave → 美国）。', '',
         '> 档位：★ 品牌商 / 自有品牌 8 = PoE Texas / Grid Connect / Lynn Electronics / Lütze / Videcon / Assmann / Dipol / Extralink + EPCOM（中型 Planet 分销）；○ Streakwave / Logicbus / Cables N More / 3G Router Store / Blake UK / IndustrialComms / 1ST-embedded / Fiber24；'
         '△ 观察档 SISEGUSA（区域外）/ Urban Security（微型）/ DCB（联邦 TAA）/ Mayflex（Sonepar 体系）/ Blue Helix（法人待核）/ Euro Security（微型）/ EasyWind（成单终端）/ NetTrans（个体）。'
         '**Simon 可按编号否决**；曾判不行的 20 户均已在理由里标注。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批126_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
