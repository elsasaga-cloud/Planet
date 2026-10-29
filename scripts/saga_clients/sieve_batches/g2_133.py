#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 133 批（2026-10-29）—— 闸 1 第 35 批（桶 ⑦ 首批 第 1–55 户）候选 **3 户**查底数（KR 1 / TR 2），底数见 registry_batches/b133_c.py。
本批跑完 → candidate 归零；P 池候选累计 185。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-133）：
  · pool_candidate 3 = ipTIME / EFM Networks KR ★ 长线（法人名坐实，사업자등록번호 未取；Q-33 洪瑞现供；无邮箱先找路径）/ İnterland Bilişim TR ○（VKN 坐实）/ MEPA Elektronik TR ○（官网 + 目录，vergi no 未取）。
  · 无 keep_C / 无新 pass_final。

用法：python3 sieve_batches/g2_133.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批133_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-133'
DATE = '2026-10-29'

V = {
    'SC-380': ('pool_candidate', '★ 韩国 · 巨头品牌商 OEM 30%（长线）：주식회사 이에프엠네트웍스 EFM Networks Co., Ltd. — ipTIME（龙仁；2001-08-07；代表 김인；韩国第一路由器品牌；路由器由深圳 ZIONCOM 代工 = 已用中国 ODM）部分坐实（사업자등록번호 未取）；自有品牌 ✔ 韩国点名国 ✔ 对位 ✔ Simon「多跟进」✔ → P 池候选（无邮箱 → 官网找采购路径；洪瑞现供 → Q-33 待 Simon；KC 买方自理）', ['oem_target']),
    'SC-440': ('pool_candidate', '○ 土耳其主区 · 分销 / 集成 20–25%：İnterland Bilişim Teknolojileri Tic. Ltd. Şti.（İstanbul Ümraniye；VKN 4781181726；NACE 461401 电子 / 电信设备批发代理）坐实（展会名片「Interland Network & Security」对应待 WA 确认）；土耳其主区 ✔ WA 可达 ✔ 具体需求 ✔ → P 池候选', []),
    'SC-442': ('pool_candidate', '○ 土耳其主区 · 安防集成 25%：MEPA Elektronik（Kayseri；弱电集成 15 年；11–50 人；Co-Owner Eren Gül）部分坐实（vergi no 未取）；土耳其主区 ✔ WA 可达 ✔ 4 / 8 / 16 / 24 口需求 ✔ 决策人具名 ✔ → P 池候选', []),
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
    L = [f'# C 池 · 闸 2 · 第 133 批（{DATE}）—— 闸 1 第 35 批（桶 ⑦ 首批）候选 3 户查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b133_c.py`，第 133 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 1（İnterland VKN）/ 部分坐实 2（EFM Networks 사업자등록번호 未取、MEPA vergi no 未取）。'
         ' 本批跑完 → candidate 归零；P 池候选累计 185。', '',
         '> 档位：★ 1 = ipTIME / EFM Networks（韩国巨头品牌，长线；Q-33 洪瑞现供；无邮箱先找路径）；○ 2 = İnterland Bilişim（伊斯坦布尔批发 / 集成）/ MEPA Elektronik（开塞利弱电集成）—— 均土耳其主区展会 WA 可达。**Simon 可按编号否决**。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批133_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
