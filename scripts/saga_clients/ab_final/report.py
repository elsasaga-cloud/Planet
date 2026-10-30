#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AB-FINAL · 报告生成：docs/requirements/A类终评_2026-10-30.md + .html（从 A类终评 JSON / 回信档案 JSON / A深挖核验 JSON / entities 渲染，不手写名单）。"""
import csv
import json
import os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-30'
MD = os.path.join(ROOT, 'docs', 'requirements', f'A类终评_{DATE}.md')
HTML = os.path.join(ROOT, 'docs', 'requirements', f'A类终评_{DATE}.html')


def cell(x, n=None):
    s = str(x if x is not None else '').replace('|', '／').replace('\n', ' ')
    return s[:n] + '…' if n and len(s) > n else s


def main():
    rows = json.load(open(os.path.join(SD, f'A类终评_{DATE}.json'), encoding='utf-8'))
    deep = json.load(open(os.path.join(SD, f'A深挖_核验_{DATE}.json'), encoding='utf-8'))
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    dossier = json.load(open(os.path.join(SD, f'回信档案_{DATE}.json'), encoding='utf-8'))
    R = {r['code']: r for r in rows}
    finalA = [c for c, e in ents.items() if e['grade'] == 'A']
    tier_of = {c: (deep.get(c) or {}).get('tier') or R.get(c, {}).get('tier') or ('A1' if ents[c].get('pi') else '') for c in finalA}
    by_tier = {t: sorted([c for c in finalA if tier_of[c] == t]) for t in ('A1', 'A2', 'A3')}
    demoted = [(c, o) for c, o in deep.items() if o['verdict'] == '下放B']
    outA = [r for r in rows if r['grade_now'] == 'A' and r['target'] == 'B']
    c2b = [r for r in rows if r['grade_now'] == 'C' and r['target'] == 'B']
    not_saga = [r for r in rows if r['deal'].startswith('备注成单')]
    old_deal = [r for r in rows if r['deal'].startswith('老成单')]
    reg = Counter(ents[c]['region'] for c in finalA)
    boxes = Counter()
    for c in by_tier['A2']:
        d = dossier.get(c)
        for b in ((d['boxes'] if d else '') or 'R'):
            boxes[b] += 1
    L = []
    L.append(f'# A 级终评（Saga 成单 + 实质回信沟通 + 极贴合 → 逐户落池核验）· {DATE}\n')
    L.append('> 对应 T29-U136 / U137（Simon 2026-10-30）。本页由 `scripts/saga_clients/ab_final/report.py` 从 `A类终评_2026-10-30.json` + `A深挖_核验_2026-10-30.json` + `entities.json` 渲染；名单不手写。\n')
    L.append('## 0. 规则（Simon 原话要旨 → 执行口径）\n')
    L.append('1. **A 的主力军 = 成单客户 + 有过回信沟通的客户**；再加大池里极贴合 Saga 产品线 / 想法的户；先 A 后 B。')
    L.append('2. **成单只认 PI 包 20 户**（Simon 2026-10-30：「Saga 的成交客户就那 20 个 … 其他的都不算成交」）——表格备注里的「成单/样品单」是 Simon 本职公司时期的单，不是 Saga 的；`客户主表` 的「成交」列已改为只标 PI 包，另加「备注提及成交(非Saga)」列；MD 里的「老客户回访 / 感谢上次订单」话术只对 PI 包 20 户出现。')
    L.append('3. **「回信」按实质认**：问价 / 要样 / 要规格 / 报数量 / 谈项目 / 约谈 / 提 OEM 才算；自动回复、工单、休假、卖家反推销、只一句 thanks 不算；最后一句硬婉拒不进 A；2022 年前（Saga 之前）的互动、问的是 Saga 产品线外（AHD/HDMI/光猫/线缆…）的不算。Simon 表内备注里记的当面 / WhatsApp 对话（「问了 2 款 2.5G 价格」这类）算回信。')
    L.append('4. **有实质回复的逐户深挖核验（A-DEEP-01）**：六项——① 身份（登记 / 官网 / 法定名）② 角色与对位（分销 / 集成 / OEM 品牌 / ISP / 终端；是否卖或用交换机·PoE·工业·光纤）③ 需求证据 ④ 路径（企业邮箱 MX / WhatsApp / 最近来信距今）⑤ 规模 ⑥ 否决项（婉拒在后 / 守界 / 巨头 / 同行卖家 / Q-33 / 台湾 / 中国大陆 / 轨交军工主业）。六项过 → 留 A；不过 → 下放 B。网查补缺口的（11 户）每条带 URL 写进研究档。')
    L.append('5. **B/C 之间只做一件事**：有实质回复的 C 捞到 B（U128 ②）；其余 B/C 不动。\n')
    L.append('## 1. 结果一览\n')
    L.append('| 项 | 数 |\n|---|---|')
    L.append(f'| **A 终评 = {len(finalA)}**（评定前 169 → 终评 224 → 核验 203 → 「极为 OK」{len(finalA)}） | A1 Saga 成单 {len(by_tier["A1"])} / A2 实质回信 {len(by_tier["A2"])} / A3 极贴合 {len(by_tier["A3"])} |')
    L.append(f'| 深挖核验候选 | {len(deep)} 户 → 留 A {sum(1 for o in deep.values() if o["verdict"] == "留A")} / 下放 B {len(demoted)}（§4）；SB-061 按人工定级留 B |')
    L.append(f'| A2 证据来源箱 | Alan {boxes["A"]} / S {boxes["S"]} / Elsa {boxes["E"]} 户（一户可多箱）；仅表内 / 研究档 {boxes["R"]} |')
    L.append(f'| 非 Saga 成单澄清 | {len(not_saga)} 户不再按成单计（§6）；老成单品类不符 {len(old_deal)} 户留 B |')
    L.append(f'| C 捞到 B | {len(c2b)} 户（有实质回复但不够 A） |')
    L.append('| A 分区 | ' + '、'.join(f'{k} {v}' for k, v in reg.most_common()) + ' |\n')
    L.append('**邮箱体量（Alan / S 的跟进量）：** Alan 箱发 2025 年 11,363 / 2026 年 8,517 封，收 641 封；S 箱发 2024 年 8,714 / 2025 年 1,312 / 2026 年 935 封，收 2,617 封。回信档案 637 户有信号。\n')
    L.append('## 2. 旋钮（默认已执行；一句话可翻）\n')
    L.append('| 旋钮 | 默认 | 说明 |\n|---|---|---|')
    L.append('| K1 非主攻区（美加 / 欧洲 / 土以外；俄 / 印 / 韩也算）只有 1 句 price/catalog 的户 | 不进 A，留 / 捞到 B | 要「有来有往」（≥2 条实质信号，或 1 封带样品 / 数量 / 项目 / OEM 的信）才进 A 候选 |')
    L.append('| K2 旧 A 无成单无回信也不在贴合名单 | 降 B | §5 |')
    L.append('| K3 只有薄回复（thanks / ok / 稍后谈）的旧 A | 降 B | §5 |')
    L.append('| K4 台湾品牌商回过信（alfa、EDIMAX、Winsonic、Lilin、AD-NET、Tailyn、AirLive） | 按老规矩最高 B | 想做台系 OEM 可翻成 A |')
    L.append('| K5 gg 8 户（Simon 标「凉了」的 Saga 成单） | 按「成单即 A」进 A1 | 要退就退 |')
    L.append('| K6 深挖核验：2 年以上只回过一句泛问价、无 WA、身份 / 角色也薄的 | 下放 B | §4 里标「路径弱」的那些 |\n')
    for t, title in (('A1', '3.1 A1 Saga 成单（PI 包）'), ('A2', '3.2 A2 实质回信沟通（深挖核验通过）'), ('A3', '3.3 A3 极贴合（无回信；身份 / 角色 / 对位核验通过）')):
        cs = by_tier[t]
        L.append(f'## {title}（{len(cs)} 户）\n')
        L.append('| 编号 | 公司 | 国家 | 身份 | 角色 | 需求 | 路径 | 最近来信 | 故事线 |\n|---|---|---|---|---|---|---|---|---|')
        for c in sorted(cs, key=lambda x: (ents[x]['region'], x)):
            o = deep.get(c) or {}
            L.append(f"| {c} | {cell(ents[c]['name'], 26)} | {cell(ents[c]['country'], 8)} | {cell((o.get('ident') or ['', ''])[0], 10)} | {cell(o.get('role', ''), 14)} | {cell(o.get('need', ''), 12)} | {cell((o.get('path') or ['', ''])[0], 4)} | {o.get('last_in', '')} | {cell(o.get('story', ''), 260)} |")
        L.append('')
    L.append(f'## 4. 深挖核验未过 → 下放 B（{len(demoted)} 户）——请扫一眼，要留的指名\n')
    L.append('| 编号 | 公司 | 国家 | 评定前 | 没过的原因 | 身份 / 角色 / 路径 |\n|---|---|---|---|---|---|')
    for c, o in sorted(demoted, key=lambda kv: (kv[1]['region'], kv[0])):
        why = (o['gaps'][-1] if o['gaps'] and o['gaps'][-1].startswith('人工终判') else ('否决：' + '、'.join(o['veto']) if o['veto'] else '缺口：' + '、'.join(o['gaps'])))
        L.append(f"| {c} | {cell(o['name'], 26)} | {cell(o['country'], 8)} | {o['grade_now']} | {cell(why.replace('人工终判：', ''), 170)} | {cell((o.get('ident') or ['', ''])[0] + ' / ' + o.get('role', '') + ' / ' + (o.get('path') or ['', ''])[0], 40)} |")
    L.append('')
    # A-DEEP-02「不是极为 OK 的就 B」
    d2 = []
    for c, e in ents.items():
        rs = e.get('research') or {}
        for h in rs.get('override_history') or []:
            if h.get('batch') in ('A-DEEP-02', 'A-DEEP-03', 'A-DEEP-04', 'A-DEEP-05'):
                d2.append((c, e, (rs.get('a_deep') or {}).get('verdict2_reason') or h.get('reason', '')))
    L.append(f'## 4b. 「不是极为 OK 的就 B」下放（A-DEEP-02/03/04/05，{len(d2)} 户；Simon 2026-10-30 定口径）——要捞回的指名\n')
    L.append('口径：PI 成单不动；个人 / 微型（≤10 人或 <£1M 级）且无进行中项目、结构性采购障碍（只买美国/TAA 产地、自有海外制造、国防/铁路主业）、巨头集团子公司、非主攻区 + 互动薄 → B（研究档与情报全保留，B1 重点普通跟）。\n')
    L.append('| 编号 | 公司 | 国家 | 原因 |\n|---|---|---|---|')
    for c, e, why in sorted(d2, key=lambda x: (x[1]['region'], x[0])):
        L.append(f"| {c} | {cell(e['name'], 26)} | {cell(e['country'], 8)} | {cell(why, 150)} |")
    L.append('')
    L.append(f'## 5. 出 A（评定前 A → B，{len(outA)} 户；非 Saga 成单澄清 / 婉拒 / 巨头 / 台湾 / 仅自动回复 / 无证据）\n')
    L.append('| 编号 | 公司 | 国家 | 原因 | 证据摘录 |\n|---|---|---|---|---|')
    for r in outA:
        L.append(f"| {r['code']} | {cell(r['name'], 26)} | {cell(r['country'], 8)} | {cell(r['why_not'], 90)} | {cell(r['evidence'], 110)} |")
    L.append('')
    L.append(f'## 6. 非 Saga 成单澄清（{len(not_saga)} 户；表格备注里的单是本职公司时期的）+ 老成单品类不符（{len(old_deal)} 户）\n')
    L.append('| 编号 | 公司 | 国家 | 现等级 | 说明 |\n|---|---|---|---|---|')
    for r in not_saga + old_deal:
        L.append(f"| {r['code']} | {cell(r['name'], 26)} | {cell(r['country'], 8)} | {ents[r['code']]['grade']} | {cell(r['deal'], 100)} |")
    L.append('')
    L.append(f'## 7. C 捞到 B（{len(c2b)} 户）\n')
    L.append('| 编号 | 公司 | 国家 | 原因 | 证据摘录 |\n|---|---|---|---|---|')
    for r in c2b:
        L.append(f"| {r['code']} | {cell(r['name'], 26)} | {cell(r['country'], 8)} | {cell(r['why_not'], 60)} | {cell(r['evidence'], 110)} |")
    L.append('')
    L.append('## 8. 机制与文件\n')
    L.append('- 规则落地：研究档 `grade_override` A/B + `override_reason` + `override_history`（batch `AB-FINAL-01/02`、`A-DEEP-01`）+ `ab_final` / `a_deep` 块；`人工定级.csv` 最高优先（SB-061）。每个 A 户的 MD 多了一节「A 落池核验」（六项 + 故事线 + 末 12 条往来时间线 + 网查事实）。')
    L.append('- 证据：`data/saga_clients/回信档案_2026-10-30.json/.csv`（637 户逐封分类）；决定：`A类终评_2026-10-30.json/.csv`；核验：`A深挖_核验_2026-10-30.json/.csv`（246 候选六项 + 时间线）。脚本 `scripts/saga_clients/ab_final/{reply_dossier,a_select,a_deep,report}.py` + `patches/p78_a_final.py`（按批次参数）/ `p79_a_deep.py`（幂等）。')
    L.append('- `build.py`：`flags.deal` 只由 PI 包置位；备注正则改为 `flags.deal_note`（评分不变，状态改「历史合作·维护（非 Saga 成单）」）；`render.py` 的成交话术只认 PI 包。')
    L.append('- 36 户从未调研的 C 户因回信进 A/B，已用回信证据建最小研究档（公司底数走「新入库即查」）。')
    md = '\n'.join(L) + '\n'
    open(MD, 'w', encoding='utf-8').write(md)
    try:
        import markdown
        body = markdown.markdown(md, extensions=['tables'])
        open(HTML, 'w', encoding='utf-8').write('<!doctype html><html lang="zh"><head><meta charset="utf-8"><title>A 级终评 2026-10-30</title><style>body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;max-width:1600px;margin:24px auto;padding:0 16px;line-height:1.5}table{border-collapse:collapse;font-size:12.5px}td,th{border:1px solid #ccc;padding:3px 6px;vertical-align:top}th{background:#f3f3f3;position:sticky;top:0}tr:nth-child(even){background:#fafafa}blockquote{color:#555;border-left:3px solid #ccc;padding-left:10px}</style></head><body>' + body + '</body></html>')
    except Exception as ex:  # noqa
        print('html skipped', ex)
    print(MD, len(finalA), {t: len(v) for t, v in by_tier.items()}, 'demoted', len(demoted), 'outA', len(outA), 'c2b', len(c2b))


if __name__ == '__main__':
    main()
