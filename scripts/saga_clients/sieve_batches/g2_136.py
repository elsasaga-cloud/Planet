#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 136 批（2026-10-29）—— 第 134–135 批「未坐实」11 户中有官网的 7 户改走官网页脚 / About 页直取（每户 1 页），底数见 registry_batches/b136_c.py。
本批跑完 → P 池候选 199 → 204；闸 2 回 C「未坐实」余 4（Bilimsa / NAZEMCO / Tùng Lâm 无站；Signalizācija 网店）。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-136）：
  · pool_candidate 5 = ★ ORIGO RU（品牌站在营、2025 新闻，ИНН 未取）/ ★ Conexpro（实为捷克 Plzeň 品牌，国别纠偏 RU→CZ 待 Simon；info@ 在）/ ○ Viễn Thông Thành Công VN / ○ THUANAN Automation VN / ○ Việt Long – G-NET 代理 VN。
  · keep_C 2 = IT Group Kazakhstan（坐实 БИН 但为软件公司 = 非渠道）/ Projexon（projexon.com 为商务咨询公司 = 域名错配，待 WA 追问）。
  · 无新 pass_final。

用法：python3 sieve_batches/g2_136.py
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-136'
DATE = '2026-10-29'

V = {
    'SC-1613': ('pool_candidate', '★ 俄罗斯 · 自有品牌商 OEM 30%（长线）：ORIGO Networks（origo-networks.ru 官网直取：L3 24×2.5G PoE / CCTV PoE 交换机 / Wi-Fi 6 / 10G MC 全线自有品牌；2025-05 参展 COMPUTEX、2025-09 L3 取证）部分坐实（ИНН 未取，联系页 404）；Simon「自己的白色外壳 / 比较重要」✔ 对位 ✔ → P 池候选（官网找 sales@；收款待定）', ['oem_target']),
    'SC-2957': ('pool_candidate', '★ 捷克（欧洲）· 自有品牌商 OEM 30%（长线）：Conexpro（conexpro.com About / Contact 直取：ISP / 安装商全线网络配件品牌，PoE 交换机 / SFP / 注入器 / 机柜 / 电池；Hřbitovní 1479/25, 312 00 Plzeň；info@conexpro.com；多国分销）部分坐实（IČO 未取，法人疑 i4wifi a.s.）；表内「俄罗斯」→ 实为捷克 = 国别纠偏待 Simon；Simon 二筛「全线帧田」= 已用中国 OEM ✔ 欧洲 ✔ 邮箱 ✔ → P 池候选（Simon 原「判定不行」可否决）', ['oem_target']),
    'SC-1606': ('pool_candidate', '○ 越南 · 分销 20%：Viễn Thông Thành Công（mangvienthong.com.vn 官网直取：河内 Hoàng Mai Tây Nam Linh Đàm；光缆 / 3onedata MC / 光交换机 / 光模块 / VC / ODF 分销 + 熔接施工；inbox.thanhcong@gmail.com）部分坐实（MST 未取）；越南先例 ✔ 中国品牌 ✔ 对位 ✔ → P 池候选', ['dayjob_fit']),
    'SC-1638': ('pool_candidate', '○ 越南 · 工业自动化渠道 25%：THUANAN – Automation Components Company（thuananvn.com.vn 官网直取：M-System / Azbil / ASCO / Honeywell 工业元件分销；thuanan.sales1@gmail.com；0989 174 796）部分坐实（MST 未取，通名）；越南先例 ✔ 工业渠道对位 ✔ optone 在用 ✔ → P 池候选', []),
    'SC-1983': ('pool_candidate', '○ 越南 · 分销 20%：Việt Long（vietlongtelecom.com 官网直取：G-NET 河内分销 + 保修代理；G-IES / G-IMS 工业交换机、GX-PES PoE、MC；电话 ×3）部分坐实（MST 未取，通名）；越南先例 ✔ 中国 OEM 品牌代理 ✔ 对位 ✔；8 推 0 回 → 换稿仅一次 → P 池候选', []),
    'SC-574': ('keep_C', '哈萨克斯坦 IT Group Kazakhstan（itgroup.kz 官网直取 = 软件开发 / 外包公司，乌拉尔斯克，30+ 人；与 niac.kz БИН 151040005191 同名同址 ✔）坐实但非渠道（2022 RFQ = 项目性采购）→ 回 C 储备，来询被动报价；不是 pass', []),
    'SC-1177': ('keep_C', '印度 Projexon：projexon.com 官网直取 = 国际商务咨询 / 企业培训公司（Oil & Gas 培训，客户 NNPC）≠ 表内 CCTV 公司 → 域名错配；Vignesh 真实公司待 WA 追问 → 回 C（印度先例 ✔ 决策人 ✔ WA 可达 ✔）；不是 pass', []),
}


def main():
    assert len(V) == 7
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    for code, (verdict, reason, tags) in V.items():
        assert verdict in ('pool_candidate', 'keep_C', 'pass_final') and len(reason) >= 12, code
        cur = sv.get(code) or {}
        assert cur.get('verdict') in ('candidate', 'keep_C', verdict) or cur.get('batch') == BATCH, ('not a gate-1 candidate', code, cur)
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
    L = [f'# C 池 · 闸 2 · 第 136 批（{DATE}）—— 第 134–135 批「未坐实」11 户中有官网的 7 户官网直取复查', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b136_c.py`，第 136 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。部分坐实 5（ORIGO、Conexpro、Thành Công、THUANAN、Việt Long —— 注册号均未取，官网直取商号 / 地址 / 品牌线）/ 坐实但非渠道 1（IT Group Kazakhstan 软件公司）/ 域名错配 1（Projexon）。'
         ' 本批跑完 → P 池候选累计 199 → 204；闸 2 回 C「未坐实」余 4（Bilimsa / NAZEMCO / Tùng Lâm 无站；Signalizācija 网店）。', '',
         '> 档位：★ 2 = ORIGO RU（自有品牌，活跃）/ Conexpro CZ（自有品牌，国别纠偏 RU→CZ 待 Simon）；○ 3 = Thành Công / THUANAN / Việt Long（越南）。回 C 2 = IT Group KZ（软件公司）/ Projexon IN（域名错配）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批136_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
