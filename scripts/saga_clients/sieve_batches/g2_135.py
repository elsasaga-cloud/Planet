#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 135 批（2026-10-29）—— 闸 1 第 36–46 批候选余 **印度 6 / 越南 9 = 15 户** 查底数（闸 1 候选至此归零），底数见 registry_batches/b135_c.py。
本批跑完 → candidate 15 → 0；P 池候选累计 189 → 199。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-135）：
  · pool_candidate 10 = IN：San Telequip ○（CIN 坐实）/ Axis Solutions ○（官网页脚，CIN 未取）/ VIgIL – Udaya Security Vision ○ oem_target（官网，GST 未取）/ RoundRobin Tech ○（目录，CIN 未取）/ Hanutech △ 预付（GST 坐实，独资微型）；VN：Viễn Thông Thiên Tân ○（MST）/ Tân Tiến – mangcongnghiep.vn ○（MST 官网页脚）/ Hoàng Thạch △ 预付（MST，2021 微型）/ Mạng Viễn Thông 3 Miền – vienthonghanoi.vn ○（MST 官网自署）/ Thanh Bình – switchquang ○（MST）。
  · keep_C 5 = 未坐实（Projexon IN、Mạng Viễn Thông VN、Thuận An VN、Việt Long VN、Tùng Lâm VN = 1 查仅同名壳即停）→ 回 C 待下轮 1 查，不是 pass。
  · 无新 pass_final。

用法：python3 sieve_batches/g2_135.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批135_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-135'
DATE = '2026-10-29'

V = {
    'SC-1657': ('pool_candidate', '○ 印度 · 工业自动化渠道 25%：San Telequip Private Limited（Pune；CIN U32202PN1992PTC065720；1992；≈ 32 人；董事 Gokhale / Joshi）坐实；印度先例 ✔ 工业渠道对位 ✔ 主动问 5 / 8 电口价 ✔ → P 池候选', []),
    'SC-1793': ('pool_candidate', '○ 印度 · 工业分销 20%：Axis Solutions Pvt Ltd（Ahmedabad Kathwada GIDC；Leonton 印度授权分销；info@axisindia.in）部分坐实（CIN 未取）；印度先例 ✔ 台湾工业品牌分销 = 进口经验 ✔ 对位 ✔ → P 池候选', []),
    'SC-1916': ('pool_candidate', '○ 印度 · 自有品牌安防商 OEM 30%：VIgIL – M/s Udaya Security Vision（Cuttack, Odisha；CCTV 自有品牌 22 年；vigil_usv@yahoo.co.in）部分坐实（GST 未取）；印度先例 ✔ 自有品牌 ✔ hisource PoE 现供 ✔ → P 池候选（仅 yahoo 邮箱）', ['oem_target']),
    'SC-2154': ('pool_candidate', '○ 印度 · 增值分销 20%：RoundRobin Tech Services Pvt. Ltd.（Mumbai；网络安全 VAD 14 年+；11–50 人；Pradeep Patel Regional Manager 真回）部分坐实（CIN 未取）；印度先例 ✔ 分销对位 ✔ 真回 ✔ → P 池候选', []),
    'SC-2208': ('pool_candidate', '△ 印度 · 电商零售 20% 预付 100%：Hanutech Solution（Delhi Rohini；Proprietorship；GST 07AXLPM4765G1Z3；东主 Mahinder；≤ 10 人；₹1.5–5 Cr）坐实；丰润达 PoE ✔ 印度先例 ✔ 但独资微型电商 → P 池候选 △', []),
    'SC-1586': ('pool_candidate', '○ 越南 · 分销 20%：CÔNG TY TNHH GIẢI PHÁP VIỄN THÔNG THIÊN TÂN（Hà Nội Từ Liêm；MST 0105224649；电子 / 电信设备批发）坐实；越南先例 ✔ 中国品牌 ✔ 对位 ✔ 业务微信可达 ✔ → P 池候选；VC 本职线并行', []),
    'SC-1605': ('pool_candidate', '○ 越南 · 工业经销 20%：CÔNG TY TNHH TM & PT CÔNG NGHỆ TÂN TIẾN（Hà Nội Thanh Xuân；MST 0110079059；三旺 3onedata 经销；tantien2tech@gmail.com）坐实（官网页脚）；越南先例 ✔ 三旺经销 ✔ 工业对位 ✔ → P 池候选（新公司微型 → 首单预付）', []),
    'SC-1644': ('pool_candidate', '△ 越南 · CCTV 批零 20% 预付 100%：Công Ty TNHH Viễn Thông Hoàng Thạch（TP.HCM Tân Bình；MST 0316813026；2021；5–10 人）坐实；越南先例 ✔ utepo ✔ 但 2021 微型 CCTV 店 → P 池候选 △', []),
    'SC-1867': ('pool_candidate', '○ 越南 · 分销 20%：CÔNG TY CỔ PHẦN MẠNG VIỄN THÔNG 3 MIỀN – vienthonghanoi.vn（Hà Nội Thanh Trì；MST 0109201032；2020-05-29；光 / 网络设备分销 + 施工）坐实（官网自署）；越南先例 ✔ 中科德能 ✔ 对位 ✔；8 推 0 回 → 坐实后换稿仅一次 → P 池候选', []),
    'SC-1979': ('pool_candidate', '○ 越南 · 进口分销 20%：Công Ty TNHH Công Nghệ Mạng Viễn Thông Thanh Bình – switchquang（Hà Nội Hai Bà Trưng；MST 0108196975；2018；进口 3onedata / Optone / Allied Telesis / DCN 等；客户 Viettel / Mobifone / EVN）坐实；越南先例 ✔ 多品牌进口 ✔ 全线对位 ✔；8 推 0 回 → 换稿仅一次 → P 池候选', []),
    'SC-1177': ('keep_C', '印度 Projexon（R. Vignesh Director，WA）：1 查仅同名工程公司壳 = 未坐实 → 回 C 待下轮 1 查（WA 问法人全名 / GST）；不是 pass', []),
    'SC-1606': ('keep_C', '越南 Mạng Viễn Thông（mangvienthong.com.vn）：1 查仅命中 .vn 另一主体（Công Nghệ Mới）= 未坐实 → 回 C 待下轮 1 查（官网页脚 MST）；不是 pass', ['dayjob_fit']),
    'SC-1638': ('keep_C', '越南 Thuận An（thuananvn.com.vn；optone）：通名 1 查仅同名壳 = 未坐实 → 回 C 待下轮 1 查（官网页脚 MST）；不是 pass', []),
    'SC-1983': ('keep_C', '越南 Việt Long Telecom（vietlongtelecom.com；G-net / hasivo）：通名 1 查仅同名壳 = 未坐实 → 回 C 待下轮 1 查（官网页脚 MST）；不是 pass', []),
    'SC-2504': ('keep_C', '越南 Tùng Lâm Technology Technical（2026-03 阿里「分销商寻求合作」；电话 ×2）：1 查仅同名壳（乙醇厂等）= 未坐实 → 回 C 待下轮 1 查（阿里后台 / 电话要邮箱 + 法人名）；不是 pass', []),
}


def main():
    assert len(V) == 15
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
    L = [f'# C 池 · 闸 2 · 第 135 批（{DATE}）—— 闸 1 第 36–46 批候选余 印度 6 / 越南 9 = 15 户查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b135_c.py`，第 135 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 7（San Telequip CIN、Hanutech GST、Thiên Tân / Tân Tiến / Hoàng Thạch / 3 Miền / Thanh Bình MST）/ 部分坐实 3（Axis Solutions、VIgIL、RoundRobin 注册号未取）/ 未坐实 5（Projexon、Mạng Viễn Thông、Thuận An、Việt Long、Tùng Lâm = 1 查仅同名壳即停，下轮再查）。'
         ' 本批跑完 → candidate 15 → 0（闸 1 第 01–48 批候选全部过闸 2）；P 池候选累计 189 → 199。', '',
         '> 档位：○ 8 = San Telequip / Axis Solutions / VIgIL（oem_target）/ RoundRobin（印度）+ Thiên Tân / Tân Tiến / 3 Miền / Thanh Bình（越南）；△ 2 = Hanutech IN / Hoàng Thạch VN（微型，预付 100%）。回 C 5 户均「未坐实」→ 下轮官网页脚 1 查，不是 pass。**Simon 可按编号否决**。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批135_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
