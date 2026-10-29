#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 125 批（2026-10-29）—— 闸 1 候选中的欧洲（非四主区）20 户，底数见 registry_batches/b125_c.py。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-125）：
  · pool_candidate = 登记 / 官网坐实或部分坐实 + §5 条数够（有关系户 ≥2 条 / 冷户 ≥4 条：对位、欧洲、坐实、复购体量 / 进口经验）→ 「P 池候选」，等 Simon 定夺。
  · keep_C = 红旗（破产程序 / 法人已注销）/ 未坐实 → 回 C 储备。
  · 无新 pass_final（H1 Telekom 法人虽注销，KP 去向未核 → 不 pass）。
tier 注记：★★ 首选 / ★ 品牌商 · 中型分销 / ○ 分销 · 进口商 / △ 观察档。

用法：python3 sieve_batches/g2_125.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批125_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-125'
DATE = '2026-10-29'

V = {
    # 西班牙
    'SC-1014': ('pool_candidate', '★ 品牌商 · OEM 30%：GOTE, S.A.（品牌 GTLAN；Paterna 1984；自有品牌网络产品制造 + 分销，已在卖宇航 / GXcom 工业线）坐实（法人 + 地址，CIF 未取）；对位 ✔ 欧洲 ✔ 自有品牌 ✔ 进口经验 ✔ → P 池候选', ['oem_target']),
    'SC-1053': ('pool_candidate', '○ 分销 20%（冷户）：Casmar Electrónica SA（A08551061；Barcelona 1979；82 人；安防分销 / 制造）坐实；对位 ✔ 欧洲 ✔ 坐实 ✔ 体量 ✔ = §5 四条 → P 池候选；从未触达 → 先发 casmar@casmar.es', []),
    'SC-1173': ('pool_candidate', '△ 观察档 · 成单回访：JEVASO S.L.（B15299548；Arteixo；纺织企业的电子部门 = 终端自用；abbolli.com 关系待核）坐实；成单 ✔ 欧洲 ✔ 对位 ✔ ≥2 条 → 入池观察档，复购体量低 → Simon 定', []),
    'SC-1556': ('keep_C', '闸 2 红旗：Bunker Seguridad Electrónica SL（B62851712）**Concursal 破产程序 / Iberinform 标 Inactiva** → 不动，回 C 储备（巡检 BORME）', []),
    'SC-2452': ('pool_candidate', '○ 贴牌渠道 · 分销 20% / OEM 30%：A-SECUR = Leistung S.L.U.（Mos, Pontevedra；11–50；安防批发 + 自有线 Movok；ONV / Utepo 页面）部分坐实（CIF 未取）；进口经验 ✔ 欧洲 ✔ 对位 ✔ 自有线 ✔ → P 池候选；Simon 曾判不行，可否决', ['oem_target']),
    'SC-371': ('pool_candidate', '★★ 首选 · OEM 30%：Visiotech Security S.L.（B80645518；Madrid；自有品牌 Safire / X-Security / Nivian；欧洲多国大分销）坐实；成单 ✔ 曾谈 OEM 交换机 ✔ 自有品牌 ✔ 具名 KP emussons@ ✔ → P 池候选', ['oem_target']),
    'SC-427': ('pool_candidate', '△ 观察档 · OEM 30%：TBK Vision（品牌真实：DVR 手册；域名关联法国 TBK SOLUTION SIREN 750660060；西班牙法人未得）部分坐实；自有品牌 ✔ 进口 Utepo ✔ 欧洲 ✔ → 入池观察档，预付 100%，先核法人 + 找新 KP', ['oem_target']),
    # 比利时 / 匈牙利 / 挪威 / 拉脱维亚 / 芬兰 / 丹麦 / 克罗地亚
    'SC-1033': ('pool_candidate', '○ 分销 20%（冷户）：Bausch Datacom NV（0437.286.193；Bierbeek 1997；电子 / 电信设备批发；年报 2024 已递）坐实；对位 ✔ 欧洲 ✔ 坐实 ✔ 体量 ✔ = §5 四条 → P 池候选；具名 dominiek@', []),
    'SC-1181': ('pool_candidate', '○ 进口商 · 分销 20%：Agenda-Age Kft.（Budapest 2002；B2B 网络批发；>514M HUF；20–49；总经理邮箱 ugyvezeto@ 公开）坐实；进口 credfiber ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔ → P 池候选', []),
    'SC-1194': ('pool_candidate', '○ 分销 20%：Eldi AS（924312963；Lørenskog；2019 新司、股本 NOK 30,300；楼宇自动化批发；Daglig leder Tony = 表内 tony@eldi.no）坐实；决策人直达 ✔ 进口宇航 ✔ 欧洲 ✔ 对位 ✔ → P 池候选，体量小 → 预付', []),
    'SC-1215': ('pool_candidate', '○ 分销 20%：SPX SIA（40003637852；Riga；MikroTik 官方分销 + 维尔纽斯仓）坐实；对位渠道 ✔ 进口 Utepo ✔ 欧洲 ✔ 坐实 ✔ → P 池候选', []),
    'SC-1220': ('pool_candidate', '△ 观察档 · 分销 20%：Starelec Oy（0549989-1；Vaasa 1984；电子元件 / 仪表分销，网络为副线，有 ONV）坐实；§5 四条技术上齐，但副线 + 体量小 → 入池观察档，Simon 定', []),
    'SC-1706': ('pool_candidate', '△ 观察档 · 分销 20%：ITV-Security ApS（CVR 38937456；Randers；安防网店 + 分销；Vivotek + acorid）坐实；进口中国品牌 ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔ → 入池观察档（微型）', []),
    'SC-667': ('keep_C', '闸 2 查实：H1 Telekom d.d.（OIB 88551335012；Split）**法人已注销（Neaktivan / izbrisan，推定并购吸收）** → 回 C；KP Silvana Pavić 去向待核（若在承继运营商任职再议）；品类偏光模块 = 本职线', ['dayjob_fit']),
    # 捷克 / 葡萄牙 / 立陶宛 / 斯洛伐克 / 塞浦路斯 / 意大利
    'SC-1335': ('pool_candidate', '★ 中型分销 20%：DISCOMP s.r.o.（25236792；Plzeň 1999；50–99 人；Planet 渠道；具名 Dan Pacanda / Milan Harmáček）坐实；对位 ✔ 欧洲 ✔ 坐实 ✔ 体量 ✔ → P 池候选；与 Planet 仓并线核对', ['dayjob_fit']),
    'SC-1446': ('pool_candidate', '△ 观察档 · 分销 20%：lojaCCTV = Neurónio Digital, Unipessoal Lda.（NIF 517867990；Ramada；一人公司 1–10）坐实；回信 ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔ → 入池观察档，预付 100%', []),
    'SC-1629': ('pool_candidate', '○ 进口商 · 分销 20%：UAB SOMI NETWORKS（300528292；Vilnius 2006；8 人；+ SIA 拉脱维亚；中性产品来自不同国内供应商）坐实；进口经验 ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔ → P 池候选；并线核对 SC-2767 SOMI RT', ['dayjob_fit']),
    'SC-1881': ('pool_candidate', '★ 中型分销 20%：TSS Group a.s.（36323551；Dubnica nad Váhom 2002；102–150 人；Dahua / Avigilon / Sony 进口分销 + 制造）坐实；对位 ✔ 欧洲 ✔ 坐实 ✔ 体量 ✔ 具名 sokol@ / roxer@ → P 池候选', ['dayjob_fit']),
    'SC-2143': ('keep_C', '闸 2 未坐实：Cygnus（cygnus.la）1 查无命中（仅无关同名）+ Simon 判不行 + 4 推 0 回 → 回 C 储备', []),
    'SC-2219': ('pool_candidate', '★ 品牌商 · OEM 30%：Comelit Group S.p.A.（01546400167；Rovetta 1985；€112M / 250–499 人；自有品牌 UniPoE 交换机贴牌）坐实；对位 ✔ 欧洲 ✔ 自有品牌 ✔ 体量 ✔ → P 池候选（长线：需挖总部产品 / 采购 KP）；Simon 曾判不行，可否决', ['oem_target']),
}


def main():
    assert len(V) == 20
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
    L = [f'# C 池 · 闸 2 · 第 125 批（{DATE}）—— 闸 1 候选 · 欧洲（非四主区）20 户查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b125_c.py`，第 125 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 15 / 部分坐实 3（GTLAN CIF 未取、A-SECUR CIF 未取、TBK 法人国别未得）/ 未坐实 1（Cygnus）/ 红旗 2（Bunker 破产程序、H1 Telekom 已注销）。', '',
         '> 档位：★★ Visiotech（成单 + 自有品牌 Safire + 大分销）；★ GTLAN（自有品牌）/ Comelit（€112M 品牌商自有 PoE 线）/ Discomp（50–99 人 Planet 渠道）/ TSS Group（102–150 人进口分销）；'
         '○ Casmar / Bausch / Agenda-Age / Eldi（CEO 邮箱在表）/ SPX（MikroTik 分销）/ Somi / A-SECUR；△ 观察档 JEVASO（成单终端）/ TBK（法人未坐实）/ Starelec / ITV-Security / lojaCCTV。'
         '**Simon 可按编号否决**；曾判不行的：A-SECUR SC-2452、Comelit SC-2219（Cygnus 已回 C）。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批125_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
