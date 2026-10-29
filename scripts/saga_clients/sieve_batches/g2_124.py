#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 124 批（2026-10-29）—— 闸 1 候选中的四主区 19 + 波兰 2 = 21 户，底数见 registry_batches/b124_c.py。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-124）：
  · pool_candidate = 登记 / 官网坐实或部分坐实 + §5 条数够（有关系户 ≥2 条 / 冷户 ≥4 条：对位、主区、坐实、复购体量）→ 进「P 池候选」，等 Simon 定夺后转正。
  · keep_C = 查实微型 / 红旗 / 未坐实 → 回 C 储备。
  · 没有新的 pass_final（闸 2 不新增永久 pass，除非查实注销）。
标签沿用 oem_target / dayjob_fit；新增 tier 注记写在理由里：★★ 首选（品牌商 + KP 直达）/ ★ 品牌商 · 进口商 / ○ 分销 / △ 观察档。

用法：python3 sieve_batches/g2_124.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批124_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-124'
DATE = '2026-10-29'

V = {
    # 土耳其
    'SC-1009': ('pool_candidate', '△ 观察档 · 集成商 25%：Varel Alarm Sistemleri Tic. A.Ş.（1990；Siemens Solution Partner；2012 并入荷兰 ARAS B.V.；约 14 人）部分坐实；对位 ✔ 主区 ✔ 坐实 ✔ 复购体量（项目型）△ → 入池观察档；先换 varelalarm.com 地址重发', []),
    'SC-1855': ('keep_C', '闸 2 未坐实：1 查无命中（仅同业）+ 9 推 0 回 → 回 C 储备', []),
    'SC-1965': ('pool_candidate', '★ 品牌商 · OEM 30%：Entegron Network 官网自有品牌「Entegron Switch」（BT 90W / 反向 PoE / 8 PoE+2 SFP 管理 = 贴牌中国货）；MERSIS 未取 → 部分坐实；对位 ✔ 主区 ✔ OEM ✔ → P 池候选；Simon 曾判不行，可否决', ['oem_target']),
    'SC-2481': ('pool_candidate', '★ 进口商 · 分销 20%：Okisan Güvenlik Teknolojileri San. ve Tic. A.Ş.（1986；Şişli；Tiandy / Dahua 授权分销；11–50）部分坐实；进口经验 ✔（HSGQ）主区 ✔ 对位 ✔ KP Gökhan（WA 已加）→ P 池候选；Simon 曾判不行，可否决', []),
    'SC-259': ('pool_candidate', '★ 成单户 · 回访（集成商 25%）：Sami Çeuik 展会买 1 台样机 $100 + 问 500 台 2 光 8 PoE 网管价 + 政府项目；无公司名 → 0 查；§5 有关系户 ≥2 条（成单 + 主区 + 对位）→ P 池候选；**请 Simon / Evelyn 补公司名**（微信）', []),
    # 英国
    'SC-1010': ('keep_C', '闸 2 查实微型：Crony Trading Ltd 05732999 一人公司、股本 £1、住宅注册地、登记主业纺织代理 + 退信 → 回 C 储备', []),
    'SC-2372': ('pool_candidate', '○ 分销 20%：Eurosat (Scotland) Limited SC204360（2000；Glasgow；Oprema 渠道；3 董事）坐实；KP graeme@ = Director Graeme Colin Miller；对位 ✔ 主区 ✔ 坐实 ✔ 体量 ✔（25 年分销）→ P 池候选；Simon 曾判不行，可否决', []),
    'SC-678': ('pool_candidate', '★ 品牌商 · OEM 30%：Qvis（运营主体推定 Qvis Lighting & Security Ltd 08877091，Portsmouth，Energy & Safety Group 100%；另 2 壳公司）坐实；曾问 fiber optics 想买样品；对位 ✔ 主区 ✔ 自有品牌 ✔ → P 池候选（KP 待取）', ['oem_target']),
    # 德国
    'SC-1013': ('pool_candidate', '△ 观察档 · OEM 30%：geMaxx 自有品牌（关联 GEMAXX Communications GmbH, Duisburg；11–50）；about 页 2022 + sales@ 退信 + 集团站「2001-2023」→ 存续待核；先用 info@gemaxx.net 一封试探，退信 / 无回声 → 回 C', ['oem_target']),
    'SC-161': ('pool_candidate', '★★ 首选 · OEM 30%：2direct GmbH（LogiLink；2001；Schalksmühle；5,000+ SKU、14,000 经销商、12 国；OEM 方案为副业）部分坐实；KP grohnert@2direct.de = Geschäftsführer Wilfried Grohnert；在售宇航工业机 → 对位 ✔ 主区 ✔ 品牌商 ✔ KP 直达 ✔ → P 池候选；Simon 曾判不行，可否决', ['oem_target', 'dayjob_fit']),
    'SC-1935': ('pool_candidate', '○ 分销 20%：LEUNIG GmbH（HRB 1531 Siegburg；1980；Hennef；GF Hermann-J. Vester；KVM / 线缆 / 工业网络，Moxa 线）坐实；对位 ✔ 主区 ✔ 坐实 ✔ 体量 ✔（45 年批发）→ P 池候选；先换 sales@leunig.de 公开地址', ['dayjob_fit']),
    'SC-683': ('pool_candidate', '★ 品牌商 · OEM 30%：VOYGAR SYSTEMS GmbH（Berlin Stresemannstr 23；自有品牌 SCS 布线 25 年质保 + 认证安装商体系；<$5M）部分坐实；Josef Klaus 54 台工业 1 光 4 电询盘 → 对位 ✔ 主区 ✔ 数量 ✔ 品牌 ✔ → P 池候选', ['oem_target']),
    # 美国 / 加拿大
    'SC-1230': ('pool_candidate', '★ 品牌商 · OEM 30%：wantec, inc（德国 1999 创立 CEO Stefan Rupp；美国分销 Simpsonville SC；自有品牌 Wantec 3405 工业 4+1 SFP = 贴牌，经销在售 €158）部分坐实；对位 ✔ 主区 ✔（DE+US）品牌 ✔ → P 池候选', ['oem_target']),
    'SC-1297': ('pool_candidate', '○ 分销 20%：Winncom Technologies Corp（Ohio 1999 注册；Solon OH；1996 起；100–160 人；WISP / 宽带分销）坐实；对位 ✔ 主区 ✔ 坐实 ✔ 体量 ✔ → P 池候选（冷户，10 推 0 回；一页纸后观察）', []),
    'SC-1443': ('pool_candidate', '★ 品牌商 · OEM 30%：Infinique（Mississauga ON；2002；11–50；自有品牌安防 + 布线 + 交换机 = ONV 贴牌；迪拜 / 印度分部）部分坐实；对位 ✔ 主区 ✔ OEM ✔ → P 池候选；先换地址', ['oem_target']),
    'SC-1450': ('pool_candidate', '★ 品牌商 · OEM 30%：MICROLINK NETWORKS LLC / NODEXON（1994；NY + Houston；51–200；$10M；CEO Yaseen Khalid；20+ 分销商）部分坐实；长飞 / 中科贴牌 → 对位 ✔ 主区 ✔ OEM ✔ 体量 ✔ → P 池候选；先换地址', ['oem_target', 'dayjob_fit']),
    'SC-2066': ('pool_candidate', '★ 品牌商 + 成单 · OEM 30%：EthoSwitch LLC（NJ + CA；2012 起自有品牌加固工业交换机；「中国制造事业部」）部分坐实；买过 KONTEN 工业 FS → 成单 ✔ 主区 ✔ 对位 ✔ OEM ✔ → P 池候选', ['oem_target']),
    'SC-2598': ('pool_candidate', '★ 品牌商 · OEM 30%：Digital Watchdog（Tampa FL；1987；80–125 人；$11–39M；CEO HK Lee）部分坐实；KP wade@ = President / COO Wade Thomas；自有 logo 商业 PoE → 对位 ✔ 主区 ✔ 品牌 ✔ KP 直达 ✔ → P 池候选（体量偏大）；Simon 曾判不行，可否决', ['oem_target']),
    'SC-292': ('pool_candidate', '○ 分销 20%（可升贴标 30%）：Fiber Instrument Sales, Inc.（Oriskany NY；1985；UEI H7LXDNB9UAY8 / CAGE 0CKD9 SAM 有效；100–250 人；$10–53M；Owner Frank Giotto）坐实；自有标 MC / CWDM + 在卖 Signamax → 对位 ✔ 主区 ✔ 坐实 ✔ 体量 ✔ → P 池候选（冷户，19 推 0 回）', ['oem_target', 'dayjob_fit']),
    # 波兰
    'SC-2510': ('pool_candidate', '★★ 首选 · OEM 30%：ELTROX Sp. z o.o.（KRS 0000175807；NIP 6462490527；Częstochowa；2003 起；36 直营 + 52 合作门店；批发品牌 Hurton；自有品牌 KENIK / GetFort 含网络设备；进口商）坐实；对位 ✔ 波兰次主区 ✔ 品牌商 ✔ 进口商 ✔ 体量 ✔ → P 池候选（采购 KP 待取；与 Planet 仓 PB-051 并线）；Simon 曾判不行，可否决', ['oem_target']),
    'SC-2516': ('pool_candidate', '★ 品牌商 · OEM 30%：AAT Systemy Bezpieczeństwa sp. z o.o.（KRS 0000838329；Warszawa；1993 起；201–500 人；自有品牌 NOVUS / KADE / ZEUS / EVIX）坐实；KP Stiepan Sedrakian / Dariusz Rośniak 在表；对位 ✔ 波兰 ✔ 品牌商 ✔ 体量 ✔ → P 池候选（体量偏大）；Simon 曾判不行，可否决', ['oem_target']),
}


def main():
    assert len(V) == 21
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    for code, (verdict, reason, tags) in V.items():
        e = ents[code]
        assert e.get('grade') == 'C', code
        cur = sv.get(code) or {}
        assert cur.get('verdict') in ('candidate', verdict) or cur.get('batch') == BATCH, ('not a gate-1 candidate', code, cur)
        assert verdict in ('pool_candidate', 'keep_C', 'pass_final') and len(reason) >= 12, code
        row = {'verdict': verdict, 'gate': 2, 'rule': 'G2', 'reason': reason, 'date': DATE, 'manual': True, 'batch': BATCH,
               'g1_batch': cur.get('g1_batch') or cur.get('batch'), 'g1_reason': cur.get('g1_reason') or cur.get('reason')}
        tg = list(dict.fromkeys((cur.get('tags') or []) + tags))
        if tg:
            row['tags'] = tg
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    L = [f'# C 池 · 闸 2 · 第 124 批（{DATE}）—— 闸 1 候选 · 四主区 19 + 波兰 2 = 21 户 查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b124_c.py`，第 124 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]}** / 回 C {c["keep_C"]} / 永久 pass {c["pass_final"]}。', '',
         '> 分档：★★ 首选（品牌商 + 决策人直达：LogiLink / Eltrox）· ★ 品牌商 / 进口商 / 成单（Entegron、Okisan、Sami、Qvis、Voygar、Wantec、Infinique、NODEXON、EthoSwitch、Digital Watchdog、AAT）· ○ 分销（Eurosat、Leunig、Winncom、FIS）· △ 观察档（Varel 小型集成商、geMaxx 存续待核）。'
         ' 回 C 2 户：Crony Trading（一人公司 £1 股本）、Kıraç（未坐实）。', '',
         '> **Simon 要做的**：① 这 19 户 P 池候选按编号否决（其中 8 户你以前判过「不行」：Entegron、Okisan、Eurosat、LogiLink、Digital Watchdog、Eltrox、AAT + Sami 需补公司名）；② Sami Çeuik 的公司名（Evelyn 微信）。'
         ' 不否决 = 默认进 P 池，下一步按「一页纸一次」稿件方向触达，再按回声升降。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows, key=lambda x: (0 if '★★' in x[1][1] else 1 if '★' in x[1][1] else 2 if '○' in x[1][1] else 3, x[0])):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sv[k].get('tags') or [])} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批124_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
