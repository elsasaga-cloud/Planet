#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 134 批（2026-10-29）—— 闸 1 第 36–46 批（桶 ⑦ 第 56–660 户）候选 25 户中 **欧洲 / 土耳其 / 俄语区 10 户** 查底数（DE 1 / TR 3 / PT 1 / LV 1 / RU 2 / KZ 2），底数见 registry_batches/b134_c.py；其余 15 户（印度 6 / 越南 9）留第 135 批。
本批跑完 → candidate 25 → 15；P 池候选累计 185 → 189。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-134）：
  · pool_candidate 4 = EFB-Elektronik DE ★ 长线（HRB 33008 坐实）/ Karel TR ★ 长线（法人名 + 地址 + 2,500 人坐实，sicil 未取）/ Metrikingdom PT △ 预付（NIF 坐实，微型 IT 服务）/ LS Service KZ △ 预付（БИН 坐实，ОКЭД 不符待核）。
  · keep_C 6 = 未坐实 / 主体未唯一（Bilimsa TR、NAZEMCO TR、Signalizācija LV、ORIGO RU、ConexPro RU、IT Group KZ）→ 回 C 待下轮 1 查，不是 pass。
  · 无新 pass_final。

用法：python3 sieve_batches/g2_134.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批134_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-134'
DATE = '2026-10-29'

V = {
    'SC-568': ('pool_candidate', '★ 德国主区 · 自有品牌分销商 OEM 30%（长线）：EFB-Elektronik GmbH（Bielefeld；HRB 33008 AG Bielefeld；USt-ID DE126943218；GF Robin Ohle；Hersteller + Großhändler = 自有品牌网络 / 布线产品线）坐实；德国主区 ✔ 自有品牌 ✔ 对位 ✔ Simon「专业」✔ → P 池候选（info@ 在；先找 Einkauf 具名）', ['oem_target']),
    'SC-2776': ('pool_candidate', '★ 土耳其主区 · 巨头品牌商 OEM 30%（长线）：Karel Elektronik Sanayi ve Ticaret A.Ş.（Ankara Cyberpark 总部 + Sincan OSB 工厂；1986；≈ 2,500 人；100% 土耳其资本；IT 500 本土 IT 制造第一）部分坐实（ticaret sicil 未取）；Simon 二筛「用的丰润达的」= 已用中国 OEM ✔ 自有品牌 ✔ 土耳其主区 ✔ → P 池候选（无邮箱 → 先找 Satın Alma 路径；Simon 原「判定不行」可按编号否决）', ['oem_target']),
    'SC-2969': ('pool_candidate', '△ 葡萄牙（欧洲）· 微型 IT 服务商 25% 预付 100%：Metrikingdom Unipessoal Lda（Lisboa；NIF 515518425；2019-06-04；资本 € 6k；CAE 62100 编程）坐实；具体需求 2 SFP + 2 RJ45 ✔ 电话 ✔ 欧洲 ✔ 但微型 + 非设备商 → P 池候选 △（复购存疑，先样机）', []),
    'SC-1602': ('pool_candidate', '△ 哈萨克斯坦 · 集成 25% 预付 100%：ТОО «LS SERVICE»（Астана；БИН 210740005950；2021-07-06；负责人 Ерсабиров С.Ж.；ОКЭД 43220 水暖安装 ≠ 网络设备 → 同一主体待核）部分坐实；先例 ✔ 对位 ✔ 表内「俄罗斯」→ KZ 国别待核；收款待定 → P 池候选 △', []),
    'SC-1190': ('keep_C', '土耳其 Bilimsa Teknoloji：1 查未中（vknsorgula 仅同名壳）= 未坐实 → 回 C 待下轮 1 查（先回 gmail 问法人名 / 网址，引用已报 $110）；不是 pass', []),
    'SC-2271': ('keep_C', '土耳其 NAZEMCO（Osama，微信）：1 查未中 = 未坐实 → 回 C 待下轮 1 查（微信先问公司全名 / 网址，并入「土耳其微信追问公司名」清单）；不是 pass', []),
    'SC-1976': ('keep_C', '拉脱维亚 Signalizācija：1 查未中（Lursoft 仅 SIA Signal 等；通名难指认）= 未坐实 → 回 C 待下轮 1 查（官网页脚 Reģ. nr.）；不是 pass', []),
    'SC-1613': ('keep_C', '俄罗斯 ORIGO Networks（自有品牌，Simon「比较重要」）：1 查未中（rusprofile 两家 ООО «Ориго» 均非网络设备 = 同名壳）= 未坐实 → 回 C 待下轮 1 查（官网 Реквизиты 取 ИНН）；oem_target 保留；不是 pass', ['oem_target']),
    'SC-2957': ('keep_C', '俄罗斯 ConexPro（全线帧田 OEM 自有品牌）：1 查未中（rusprofile 仅 ООО «Коннект-Про» 同名壳）= 未坐实 → 回 C 待下轮 1 查（官网 Контакты / Реквизиты）；oem_target 保留；无邮箱；不是 pass', ['oem_target']),
    'SC-574': ('keep_C', '哈萨克斯坦 IT Group（itgroup.kz；2022 RFQ 找 ONV 管理交换机，有回）：1 查出两家同名（IT GROUP KAZAKHSTAN 乌拉尔斯克 软件 / KAZ-IT GROUP 奇姆肯特 监控电信）主体未唯一 = 部分坐实 → 回 C 待下轮 1 查（官网页脚 БИН）；不是 pass', []),
}


def main():
    assert len(V) == 10
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
    L = [f'# C 池 · 闸 2 · 第 134 批（{DATE}）—— 闸 1 第 36–46 批候选 25 户中欧洲 / 土耳其 / 俄语区 10 户查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b134_c.py`，第 134 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 2（EFB HRB 33008、Metrikingdom NIF）/ 部分坐实 3（Karel sicil 未取、LS Service ОКЭД 不符、IT Group 两家同名）/ 未坐实 5（Bilimsa、NAZEMCO、Signalizācija、ORIGO、ConexPro = 1 查未中即停，下轮再查）。'
         ' 本批跑完 → candidate 25 → 15（印度 6 / 越南 9 留第 135 批）；P 池候选累计 185 → 189。', '',
         '> 档位：★ 2 = EFB-Elektronik DE（自有品牌分销，长线）/ Karel TR（巨头品牌商，长线；Simon 原「判定不行」）；△ 2 = Metrikingdom PT（微型 IT 服务，预付）/ LS Service KZ（ОКЭД 不符待核，预付）。回 C 6 户均「未坐实 / 主体未唯一」→ 下轮官网页脚 1 查，不是 pass。**Simon 可按编号否决**。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批134_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
