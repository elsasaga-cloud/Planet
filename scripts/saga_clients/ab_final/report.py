#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AB-FINAL-01 · 报告生成：docs/requirements/A类终评_2026-10-30.md + .html（从 A类终评 JSON / 回信档案 JSON 渲染，不手写名单）。"""
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
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    dossier = json.load(open(os.path.join(SD, f'回信档案_{DATE}.json'), encoding='utf-8'))
    A = [r for r in rows if r['target'] == 'A']
    by_tier = {t: [r for r in A if r['tier'] == t] for t in ('A1', 'A2', 'A3')}
    outA = [r for r in rows if r['grade_now'] == 'A' and r['target'] == 'B']
    c2b = [r for r in rows if r['grade_now'] == 'C' and r['target'] == 'B']
    old_deal = [r for r in rows if r['deal'].startswith('老成单')]
    simon_no = [r for r in rows if r['deal'].startswith('表内成单但')]
    reg = Counter(ents[r['code']]['region'] for r in A)
    boxes = Counter()
    for r in by_tier['A2']:
        d = dossier.get(r['code'])
        for b in (d['boxes'] if d else 'R') or 'R':
            boxes[b] += 1
    L = []
    L.append(f'# A 级终评（成单 + 回信沟通 + 极贴合）· {DATE}\n')
    L.append('> 对应 T29-U136（Simon 2026-10-30）。本页由 `scripts/saga_clients/ab_final/report.py` 从 `data/saga_clients/A类终评_2026-10-30.json` 渲染；名单不手写。\n')
    L.append('## 0. 我对你规则的理解（先复述，再干活）\n')
    L.append('1. **A 的主力军 = 成单客户 + 有过回信沟通的客户。** 回信证据三箱都挖：Alan 邮箱（`A Replied 09.04` + Alan Takeout 全量来信，最重）、S 邮箱（Takeout 全量来信 + 你表内的跟进记录，极重）、Elsa 邮箱（`E Replied` + 连接器来信，次之；Elsa 名单多在非欧美）。')
    L.append('2. **再加一层：大池里极贴合 Saga 产品线 / 想法 / 相关跟进的户**（没回过信也可以进 A），由我用 Saga 的理解 + 研究档去挑，但要逐户写理由。')
    L.append('3. **先把 A 筛出来，B 的事之后再说**——本轮只动 A（进 A / 出 A），B/C 之间只做「有实质回复的 C 捞到 B」（你 U128 的第 ② 条），其余 B/C 不动。')
    L.append('4. 「回信」我按**实质**认：问价 / 要样 / 要规格 / 报数量 / 谈项目 / 约谈 / 提 OEM 才算；自动回复、工单确认、休假、卖家反过来推销、只一句 thanks 不算；最后一句是硬性婉拒（not interested / 有自己的方案 / 不是我们市场）不进 A。')
    L.append('5. 守界（乌/伊/叙）、巨头、台湾品牌商（老规矩最高 B）、中国大陆、永久 pass、没有任何联系路径的，即使回过信也不进 A。\n')
    L.append('## 1. 结果一览\n')
    L.append('| 项 | 数 |\n|---|---|')
    L.append(f'| A 终评总数 | **{len(A)}**（评定前 A = 169） |')
    L.append(f'| A1 成单 | {len(by_tier["A1"])}（PI 包 19 + 核定成单 {len(by_tier["A1"]) - 19}） |')
    L.append(f'| A2 回信沟通 | {len(by_tier["A2"])}（证据来源箱：Alan {boxes["A"]} / S {boxes["S"]} / Elsa {boxes["E"]} 户，一户可多箱；仅表内/研究档 {boxes["R"]}） |')
    L.append(f'| A3 极贴合（无回信） | {len(by_tier["A3"])} |')
    L.append(f'| 进 A：B→A / C→A | {sum(1 for r in A if r["grade_now"] == "B")} / {sum(1 for r in A if r["grade_now"] == "C")} |')
    L.append(f'| 出 A：A→B | {len(outA)}（§4 列给你否决） |')
    L.append(f'| C 捞到 B（有实质回复但不够 A） | {len(c2b)} |')
    L.append(f'| 人工定级保留 | SB-061（你定的 B，不动） |')
    L.append('| A 分区 | ' + '、'.join(f'{k} {v}' for k, v in reg.most_common()) + ' |\n')
    L.append('**邮箱体量（证明 Alan/S 的跟进量）：** Alan 箱发 2025 年 11,363 / 2026 年 8,517 封，收真人+自动 641 封；S 箱发 2024 年 8,714 / 2025 年 1,312 / 2026 年 935 封，收 2,617 封。回信档案共 637 户有信号，其中实质回复（R+）267 户。\n')
    L.append('## 2. 五个旋钮（默认已执行；你一句话可翻）\n')
    L.append('| 旋钮 | 默认 | 影响 |\n|---|---|---|')
    L.append('| K1 非主攻区（美加/欧洲/土以外）只有 1 句 price/catalog 的户 | 不进 A，捞到/留 B | 约 40 户（§5） |')
    L.append('| K2 评定前是 A、但无成单无回信也不在贴合名单 | 降 B | SA-041、SA-069、SB-017、SB-325 等（§4） |')
    L.append('| K3 只有薄回复（thanks / ok / 稍后谈）的旧 A | 降 B | SA-038、SA-057、SB-015、SB-306、SB-499（§4） |')
    L.append('| K4 台湾品牌商回过信（alfa、EDIMAX、Winsonic、Lilin、AD-NET、Tailyn、AirLive） | 按老规矩最高 B | 若你想做台系 OEM 可翻成 A |')
    L.append('| K5 gg 8 户（你标「凉了」的成单） | 按「成单即 A」进 A1 | SB-375/1113/1120/006/003/002/001/020；你要的话一键退 B |\n')
    for t, title in (('A1', '3.1 A1 成单'), ('A2', '3.2 A2 回信沟通'), ('A3', '3.3 A3 极贴合（无回信）')):
        rs = by_tier[t]
        L.append(f'## {title}（{len(rs)} 户）\n')
        L.append('| 编号 | 公司 | 国家 | 前 | 依据 | 证据摘录 |\n|---|---|---|---|---|---|')
        for r in sorted(rs, key=lambda x: (ents[x['code']]['region'], x['code'])):
            L.append(f"| {r['code']} | {cell(r['name'], 28)} | {cell(r['country'], 8)} | {r['grade_now']} | {cell(r['reason'], 70)} | {cell(r['evidence'], 150)} |")
        L.append('')
    L.append(f'## 4. 出 A（A→B，{len(outA)} 户）——请扫一眼，要留的指名\n')
    L.append('| 编号 | 公司 | 国家 | 原因 | 证据摘录 |\n|---|---|---|---|---|')
    for r in outA:
        L.append(f"| {r['code']} | {cell(r['name'], 28)} | {cell(r['country'], 8)} | {cell(r['why_not'], 80)} | {cell(r['evidence'], 120)} |")
    L.append('')
    L.append(f'## 5. C 捞到 B（{len(c2b)} 户）+ 非主攻区薄回复留 B（K1）\n')
    L.append('| 编号 | 公司 | 国家 | 原因 | 证据摘录 |\n|---|---|---|---|---|')
    for r in c2b + [r for r in rows if r['grade_now'] == 'B' and r['target'] == 'B' and 'K1' in r['why_not']]:
        L.append(f"| {r['code']} | {cell(r['name'], 28)} | {cell(r['country'], 8)} | {cell(r['why_not'], 60)} | {cell(r['evidence'], 120)} |")
    L.append('')
    L.append('## 6. 老成单但品类/年代不符（不进 A，留 B）+ 你亲判「不行」的成单\n')
    L.append('| 编号 | 公司 | 国家 | 现等级 | 说明 |\n|---|---|---|---|---|')
    for r in old_deal + simon_no:
        L.append(f"| {r['code']} | {cell(r['name'], 28)} | {cell(r['country'], 8)} | {r['target']} | {cell(r['deal'], 90)} |")
    L.append('')
    L.append('## 7. 机制与文件\n')
    L.append('- 规则落地：研究档 `grade_override` A/B + `override_reason` + `override_history`（batch `AB-FINAL-01`）+ `ab_final` 块（档次/理由/证据）；`人工定级.csv` 仍最高优先（只有 SB-061）。')
    L.append('- 证据：`data/saga_clients/回信档案_2026-10-30.json/.csv`（637 户逐封分类）；决定：`data/saga_clients/A类终评_2026-10-30.json/.csv`；脚本 `scripts/saga_clients/ab_final/{reply_dossier,a_select,report}.py` + `patches/p78_a_final.py`（幂等）。')
    L.append('- 22 户从未调研的 C 户因回信进 A/B，已用回信证据建最小研究档（公司底数走「新入库即查」，下一轮补）。')
    L.append('- `客户主表.csv` 的「成交=是」100 户里 80 户是备注正则命中（含买了同行、2010–13 老产品线、光端机/HDMI），不等于 Saga 成单；本轮 A1 只认 PI 包 + 逐户核定的 14 户。')
    md = '\n'.join(L) + '\n'
    open(MD, 'w', encoding='utf-8').write(md)
    try:
        import markdown
        body = markdown.markdown(md, extensions=['tables'])
        open(HTML, 'w', encoding='utf-8').write('<!doctype html><html lang="zh"><head><meta charset="utf-8"><title>A 级终评 2026-10-30</title><style>body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;max-width:1500px;margin:24px auto;padding:0 16px;line-height:1.5}table{border-collapse:collapse;font-size:12.5px}td,th{border:1px solid #ccc;padding:3px 6px;vertical-align:top}th{background:#f3f3f3;position:sticky;top:0}tr:nth-child(even){background:#fafafa}blockquote{color:#555;border-left:3px solid #ccc;padding-left:10px}</style></head><body>' + body + '</body></html>')
    except Exception as ex:  # noqa
        print('html skipped', ex)
    print(MD, len(A), {t: len(v) for t, v in by_tier.items()}, 'outA', len(outA), 'c2b', len(c2b))


if __name__ == '__main__':
    main()
