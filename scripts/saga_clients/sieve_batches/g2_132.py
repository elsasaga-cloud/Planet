#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 132 批（2026-10-29）—— 闸 1 第 34 批（桶 ⑥ 收口段 第 1211–1257 户）候选 **3 户**查底数（MX / PK / IN 各 1），底数见 registry_batches/b132_c.py。
本批跑完 → 闸 1 第 01–34 批（桶 ①–⑥ 全部）候选全部过闸 2，candidate 归零；P 池候选累计 182。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-132）：
  · pool_candidate 3 = TVC MX ★（RFC 坐实；201–500 人大分销）/ Starcom PK ○（法人名坐实，SECP 未取；真人回）/ Techroutes IN ★（CIN 坐实；自有品牌 → oem_target；Simon 标 Spam 可否决）。
  · 无 keep_C / 无新 pass_final。

用法：python3 sieve_batches/g2_132.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批132_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-132'
DATE = '2026-10-29'

V = {
    'SC-3130': ('pool_candidate', '★ 墨西哥 · CCTV 大分销 20%（长线）：TVC en Línea.com, S.A. de C.V.（Monterrey；RFC TVC060802NE4；2000；201–500 人；蒙特雷 + 墨西哥城）坐实；大分销 ✔ Utepo / 大华中国品牌进口 ✔ 对位 ✔ 墨西哥先例 SYSCOM ✔ → P 池候选（换 ventas / compras 地址 + WA）', []),
    'SC-3149': ('pool_candidate', '○ 巴基斯坦 · 集成 25% + 预付 100%：Starcom Technologies (Pvt) Ltd（Karachi Saddar；2004；22–32 人；$5.3M；CEO Asghar Ali）部分坐实（SECP 未取）；2026-02 真人回「请用公司域名邮箱发」✔ Raisecom 采购 ✔ 对位 ✔ 决策人具名 ✔ → P 池候选（用 sagatele.com 域名重发）', []),
    'SC-3198': ('pool_candidate', '★ 印度 · 自有品牌 OEM 30%：Techroutes Network Pvt Ltd（Gurgaon；CIN U72200RJ2003PTC018583；2003；实收 ₹2 Cr；营业额 ₹5–25 Cr；自有路由 / 交换 / VoIP 产品线经分销商销售）坐实；自有品牌 ✔ 印度点名国 ✔ 对位 ✔ 决策人具名 ✔ → P 池候选（Simon 曾标 Spam → 可否决）', ['oem_target']),
}


def main():
    assert len(V) == 3
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
    L = [f'# C 池 · 闸 2 · 第 132 批（{DATE}）—— 闸 1 第 34 批（桶 ⑥ 收口段）候选 3 户查底数（桶 ①–⑥ 候选全部过闸 2）', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b132_c.py`，第 132 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 2（TVC RFC、Techroutes CIN）/ 部分坐实 1（Starcom，SECP 未取）。'
         ' 本批跑完 → 闸 1 第 01–34 批（桶 ①–⑥）候选全部过闸 2，candidate 归零；P 池候选累计 182。', '',
         '> 档位：★ 2 = TVC（墨西哥大分销 201–500 人，长线）/ Techroutes（印度自有品牌 OEM 对象；Simon 曾标 Spam → 可否决）；○ 1 = Starcom（巴基斯坦集成，真人回，预付 100%）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批132_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
