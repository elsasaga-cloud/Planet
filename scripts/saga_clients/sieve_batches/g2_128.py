#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 128 批（2026-10-29）—— 闸 1 第 09 / 10 / 11 批（桶 ⑤ 收尾）候选 18 户 = GB 4 / CZ 4 / DE 3 / US 2 / PL / TR / BG / IT / BE 各 1（闸 1 候选清零），底数见 registry_batches/b128_c.py。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-128）：
  · pool_candidate = 法人 / 官网坐实或部分坐实 + §5 条数够（有关系户 ≥2 条 / 冷户 ≥4 条）→ 「P 池候选」，等 Simon 定夺。
  · keep_C = 红旗（个体微型 / 主业不对位）/ 未坐实 → 回 C 储备。无新 pass_final。
tier：★★ 首选 / ★ 品牌商 · 中型分销 / ○ 分销 · 进口商 / △ 观察档（微型 / 终端 / 巨头体系 / 法人存疑 / 区域外）。

用法：python3 sieve_batches/g2_128.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批128_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-128'
DATE = '2026-10-29'

V = {
    # 保加利亚
    'SC-575': ('pool_candidate', '○ 分销 20%：КСТ ООД / KST Ltd（София；ЕИК 831850563；1995；17–18 人；€3.26M；CATV / 布线分销 + Motorola 代表；管理人 Светлин Капитанов = 表内 skapitanov@）坐实；进口中国交换机 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔ 决策人直达 ✔ → P 池候选（13 推 0 回 → 点名换稿）', []),
    # 土耳其
    'SC-571': ('pool_candidate', '★ 中型工业分销 20%：GSL Mühendislik Sanayi ve Ticaret A.Ş.（Ankara 1988 + İstanbul；Moxa / Kyland / Robustel / Digi 土耳其分销；IT 500 强；umit@ 在表）部分坐实（MERSIS 未取）；进口 Kyland ✔ 四主区 ✔ 对位 ✔ 具名 KP ✔ → P 池候选', []),
    # 德国
    'SC-700': ('pool_candidate', '○ 集成 25%：AMC – Analytik & Messtechnik GmbH Chemnitz（HRB 995 AG Chemnitz；GF Bernd Göbel；1990 起 Advantech / NI / Gantner 伙伴）坐实；进口台湾工业品牌 ✔ 四主区 ✔ 对位 ✔ 坐实 ✔ = 冷户四条 → P 池候选', []),
    'SC-827': ('pool_candidate', '△ 观察档 · 分销 20% + 预付 100%：itjan.de = Dipl.-Ing. Dittmar Janetzky 个体（Zirndorf；Impressum 坐实；站点建设中）；表内「100 台用于 Amazon 销售」= 数量信号 ✔ 决策人直达 ✔ 四主区 ✔ 对位 ✔ → 入池观察档（个体 + 空站 → 预付 100%）；可否决', []),
    'SC-956': ('pool_candidate', '○ 分销 20%：systerra computer GmbH（Wiesbaden；HRB 32770；GF Harald Borger；11–50 人；坚固计算 + Moxa 伙伴）坐实；四主区 ✔ 对位 ✔ 坐实 ✔ 工业网络方案 ✔ = 冷户四条 → P 池候选（守界：MIL 不承诺，只做工业 / 商用场景）', []),
    # 意大利
    'SC-925': ('pool_candidate', '○ 分销 20%：SARC ITALIA SRL（Modena；P.IVA 03184880361 / REA MO-365943；€1.3M；Ateco 46.69.2 工业自动化分销）坐实；进口 Atop / USR ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔ = 冷户四条 → P 池候选', []),
    # 捷克
    'SC-656': ('pool_candidate', '★ 大分销 20%：100MEGA Distribution s.r.o.（Brno；IČO 60707968；1994；捷克主要 IT 分销商）坐实；Planet 渠道 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔ = 冷户四条 → P 池候选（长线；找网络线产品经理）', []),
    'SC-783': ('pool_candidate', '○ 分销 20%：Express Alarm Czech s.r.o.（Praha 9；IČ 26446863；2001；20–24 人；斯洛伐克姊妹公司 IČO 31630146；销售代表 Štefan Stein 官网公开）坐实；进口 Wi-Tek ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔ → P 池候选', []),
    'SC-809': ('keep_C', '闸 2 回 C：HTV Hodina = Michal Hodina 个体（Ostrava；IČ 48424986；Jablotron 安防门店）坐实但个体微型 + 非主区 + 冷户 0 互动 → 回 C 储备（来信再起则预付 100%）', []),
    'SC-908': ('pool_candidate', '○ 分销 20%：BLUECOM s.r.o. = prumysloveswitche.cz（Chrudim；IČ 25955993；KS Hradec Králové C 17530；Advantech B+B 工业交换机专卖 + Axis / Bosch / Fluke）坐实；进口台湾工业品牌 ✔ 欧洲 ✔ 对位极强 ✔ 坐实 ✔ = 冷户四条 → P 池候选', []),
    # 比利时
    'SC-856': ('keep_C', '闸 2 回 C：MegaMobile.be = M&C Technology（Mechelen；BTW BE 0479.101.014）坐实但主业手机 / 电子配件网店，PoE 为边角 + 冷户 0 互动 → 回 C 储备', []),
    # 波兰
    'SC-770': ('pool_candidate', '★ 中型工业分销 20%：ELMARK AUTOMATYKA S.A.（Warszawa；KRS 0000803828 / NIP 5252072585；1997；股本 PLN 650k；Moxa / Advantech 等多牌）坐实；波兰 ✔ 对位 ✔ 坐实 ✔ 多牌进口 ✔ = 冷户四条 → P 池候选（长线；找工业网络产品经理）', []),
    # 美国
    'SC-562': ('pool_candidate', '○ 分销 20%：Baltic Networks（Lisle IL；2005；约 9 人；$6M；WISP 增值分销 50+ 厂牌）部分坐实（IL SoS 未取）；主区 ✔ 分销主体 ✔ 对位 ✔ 坐实（名录）✔ = 冷户四条 → P 池候选（9 推 0 回 → 换稿）', []),
    'SC-634': ('pool_candidate', '★ 自有品牌 · OEM 30%：New Tech Industries, Inc.（Davie FL；11–50 人；官网在售自有型号工业 PoE DIN 交换机 NT408-2P / NT404-1 + TRENDnet）部分坐实（sunbiz 未取）；自有品牌 ✔ 进口 Wi-Tek ✔ 主区 ✔ 对位极强 ✔ → P 池候选；18 推全退信（两域 MX 正常）→ 官网表单 / LinkedIn 换址后再发', ['oem_target']),
    # 英国
    'SC-671': ('pool_candidate', '★ 自有品牌 · OEM 30%：LEADER OPTEC LIMITED（St Asaph；Co. No. 03936485；2000；11–50 人；$5.1M；董事 Paul Anthony Desmond = 表内 pauldesmond@）坐实；自有品牌布线商 ✔ 中国采购 30–40% ✔ 四主区 ✔ 决策人直达 ✔ → P 池候选', ['oem_target']),
    'SC-704': ('pool_candidate', '○ 分销 20%：ANNICOM LIMITED（Bordon GU35 0AX；24 人；董事 Dennis Gates；工业控制电子设计制造 + Kyland 分销）部分坐实（CH 号未取）；进口 Kyland ✔ 四主区 ✔ 对位 ✔ 坐实 ✔ → P 池候选', []),
    'SC-855': ('pool_candidate', '★ 中型安防分销 20%：Mast Digital (UK) Ltd（Epworth DN9 1JZ；Ltd 2014；20+ 人；Dahua Tier 1 + Wi-Tek / Ajax / TP-Link 授权；MD Stuart Smedley）部分坐实（CH 号未取）；进口 Wi-Tek ✔ 四主区 ✔ 对位 ✔ MD 具名 ✔ → P 池候选', []),
    'SC-935': ('pool_candidate', '○ 分销 20%：Semaphore Systems Ltd（London NW6；1979；1–10 人；Advantech 英国分销 1988 起 + IPC 组装）部分坐实（CH 号未取）；进口台湾工业品牌 ✔ 四主区 ✔ 对位 ✔ 坐实 ✔ = 冷户四条 → P 池候选（微型，低频）', []),
}


def main():
    assert len(V) == 18
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
    L = [f'# C 池 · 闸 2 · 第 128 批（{DATE}）—— 闸 1 第 09–11 批（桶 ⑤ 收尾）候选 18 户查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b128_c.py`，第 128 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass；闸 1 候选清零）。坐实 11 / 部分坐实 7（GSL MERSIS、Baltic IL SoS、New Tech sunbiz、Annicom / Mast Digital / Semaphore CH 号未取；均法人名坐实）/ 未坐实 0 / 0 查 0。无国别纠偏。', '',
         '> 档位：★ 6 = GSL（中型工业分销 TR）/ 100MEGA（大分销 CZ）/ Elmark Automatyka（中型工业分销 PL）/ New Tech Industries（自有品牌工业 PoE US，退信待换址）/ Leader Optec（自有品牌 + MD 在表 GB）/ Mast Digital（Dahua Tier 1 + Wi-Tek GB）；'
         '○ 9 = KST（BG）/ AMC Chemnitz / systerra（DE）/ SARC Italia（IT）/ Express Alarm / Bluecom（CZ）/ Baltic Networks（US）/ Annicom / Semaphore（GB）；'
         '△ 观察档 1 = itjan.de（DE 个体亚马逊卖家 100 台意向，预付 100%）；回 C 2 = HTV Hodina（CZ 个体门店）/ MegaMobile（BE 手机配件网店）。'
         '**Simon 可按编号否决**。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批128_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
