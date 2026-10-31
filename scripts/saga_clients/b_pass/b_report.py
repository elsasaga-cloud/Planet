#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B-PASS-01 报告 + 跟进分组：docs/requirements/B类分层_<date>.md/.html；data/saga_clients/B跟进分组_<date>.csv（B1/B2 × 区域 × 类型组 × 语言 → 群发/点名节奏）。"""
import csv
import json
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-31'
MD = os.path.join(ROOT, 'docs', 'requirements', f'B类分层_{DATE}.md')
HTML = os.path.join(ROOT, 'docs', 'requirements', f'B类分层_{DATE}.html')
LANG = {'TR': 'tr', 'DE': 'de', 'AT': 'de', 'CH': 'de', 'IT': 'it', 'ES': 'es', 'MX': 'es', 'AR': 'es', 'CO': 'es', 'CL': 'es', 'PE': 'es', 'EC': 'es', 'BO': 'es', 'PY': 'es', 'SV': 'es', 'FR': 'fr', 'PL': 'pl', 'RU': 'ru', 'KZ': 'ru', 'BY': 'ru', 'UZ': 'ru', 'UA': 'ru', 'PT': 'pt', 'BR': 'pt', 'NL': 'nl', 'KR': 'ko', 'JP': 'ja', 'VN': 'vi', 'TH': 'th', 'ID': 'id'}


def cell(x, n=None):
    s = str(x if x is not None else '').replace('|', '／').replace('\n', ' ')
    return s[:n] + '…' if n and len(s) > n else s


def type_group(o):
    t = (o.get('type') or '') + ' ' + (o.get('why') or '')
    if re.search(r'OEM|品牌|自牌|自有', t):
        return 'OEM/品牌商（30%）'
    if re.search(r'分销|经销|distribut|批发', t):
        return '分销商（20%）'
    if re.search(r'ISP|运营商', t):
        return 'ISP/运营商'
    if re.search(r'集成|integrat|安装|工程', t):
        return '集成/安装商（25%）'
    return '其他/待核'


def main():
    sel = json.load(open(os.path.join(SD, f'B类分层_{DATE}.json'), encoding='utf-8'))
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    tiers = Counter(o['tier'] for o in sel.values())
    L = [f'# B 池分层（B-PASS-01）· {DATE}\n',
         '> 对应 T29-U146（Simon：「那就开始搞B吧」）。本页由 `scripts/saga_clients/b_pass/b_report.py` 从 `B类分层_2026-10-31.json` 渲染。\n',
         '## 0. 口径（沿 A 的逻辑降一档）\n',
         '1. B = 长期慢慢跟的群；进 B 的前提是「OK」：身份能核（登记 / 法定名 / 官网）、角色对位（分销 / 集成 / OEM 品牌 / ISP / 工业自动化）、路径活（企业邮箱 MX 正常，或 WhatsApp / 电话 / 官网表单）、无否决项。',
         '2. **不 OK 的下放 C 储备（只巡检不发）**：同行卖家、中国大陆、品类不对位（学校 / 政府 / 军工轨交主业 / 二手 / 纯软件…）、路径断（无邮箱无 WA 无电话且官网不可用）、最后一句硬婉拒（R-）、个人免费邮箱 + 身份未坐实 + 0 回复 + 非主攻区、身份未坐实 + 0 回复 + 官网不可用。',
         '3. **B1 重点普通跟**：出 A 的户（AB-FINAL / A-DEEP 下放且非守界 / 同行 / 不可核原因）、有实质回信（R+ / Rw / R±）、强对位角色（研究档 type = OEM / 品牌 / 分销 / ISP / 集成）+ 登记坐实 + 主攻区（美加欧土）+ 路径活 + 官网在线。',
         '4. **B2 普通跟**：其余 OK 的；Q-33 代理商客户「不碰，标记」与巨头「不追，标记」放 B2 只巡检。',
         '5. 台湾品牌商按老规矩最高 B（可在 B1）；守界国已在池外。\n',
         '## 1. 结果\n', '| 项 | 数 |\n|---|---|',
         f"| 评定前 B | {len(sel)} |", f"| **B1 重点普通跟** | {tiers['B1']} |", f"| **B2 普通跟** | {tiers['B2']} |", f"| 下放 C 储备 | {tiers['C']}（§3 供捞回） |",
         '| B1 分区 | ' + '、'.join(f'{k} {v}' for k, v in Counter(o['region'] for o in sel.values() if o['tier'] == 'B1').most_common()) + ' |',
         '| B1 依据 | ' + '、'.join(f'{k} {v}' for k, v in Counter(o['why'].split('（')[0] for o in sel.values() if o['tier'] == 'B1').most_common()) + ' |',
         '| B2 分区 | ' + '、'.join(f'{k} {v}' for k, v in Counter(o['region'] for o in sel.values() if o['tier'] == 'B2').most_common()) + ' |\n',
         '## 2. 跟进节奏（Q-77 默认，B 层执行口径）\n',
         '| 层 | 节奏 | 内容 | 谁 |\n|---|---|---|---|',
         '| B1（重点普通跟） | 按「区域 × 类型组 × 语言」分组群发，**每 6 周一轮**；一年两次点名（1:1 短信，接着对方上次的话题） | 一款对位机型 + 一口价 + 一个问题；出 A 户接着 A 时期最后一封的话题 | 群发 = Agent 起草 / Simon 批；点名 = Simon |',
         '| B2（普通跟） | 同分组群发，**每 8 周一轮**；不点名 | 行业 + 机型为主，不报价或只报参考价 | Agent 起草 / Simon 批 |',
         '| C 储备 | 不发；两月巡检一次（官网 / 邮箱 / 新闻），有动静再捞回 B | — | 日跑 |',
         '| 升级 | B 户出现实质回信 → 进 A 候选，走 A 的六项核验 | — | Agent |\n',
         f'分组文件：`data/saga_clients/B跟进分组_{DATE}.csv`（编号 / 层 / 区域 / 类型组 / 语言 / 最近来信 / 下次群发月）。\n',
         f'## 3. 下放 C 储备（{tiers["C"]} 户）——要捞回的指名\n', '| 编号 | 公司 | 国家 | 原因 | 回信 | 官网 |\n|---|---|---|---|---|---|']
    for c, o in sorted(sel.items(), key=lambda kv: (kv[1]['why'], kv[0])):
        if o['tier'] == 'C':
            L.append(f"| {c} | {cell(o['name'], 26)} | {cell(o['country'], 8)} | {cell(o['why'], 80)} | {o['rc']} | {o['site']} |")
    L.append('')
    L.append(f'## 4. B1 重点普通跟（{tiers["B1"]} 户，按区域）\n')
    L.append('| 区域 | 编号 | 公司 | 国家 | 类型组 | 依据 | 身份 | 路径 | 回信 | 最近来信 |\n|---|---|---|---|---|---|---|---|---|---|')
    for c, o in sorted(sel.items(), key=lambda kv: (kv[1]['region'], kv[0])):
        if o['tier'] == 'B1':
            L.append(f"| {o['region']} | {c} | {cell(o['name'], 26)} | {cell(o['country'], 6)} | {type_group(o)} | {cell(o['why'], 60)} | {o['ident']} | {o['path']} | {o['rc']} | {o['last_in']} |")
    L.append('')
    L.append(f'## 5. B2 普通跟（{tiers["B2"]} 户）—— 按区域 × 类型组计数\n')
    L.append('| 区域 | 类型组 | 户数 |\n|---|---|---|')
    cnt2 = Counter((o['region'], type_group(o)) for o in sel.values() if o['tier'] == 'B2')
    for (r, g), n in sorted(cnt2.items(), key=lambda kv: (-kv[1], kv[0])):
        L.append(f'| {r} | {g} | {n} |')
    L.append('')
    L.append('## 6. 机制与文件\n')
    L.append('- 规则落地：研究档 `b_tier {tier, why, ident, path, reply, focus}`；C 下放 = `grade_override C` + `override_history`（batch `B-PASS-01`）+ 复核记录；MD 新增「B 分层」一行。')
    L.append('- 脚本：`scripts/saga_clients/b_pass/{b_select,b_report}.py` + `patches/p82_b_pass.py`（幂等）。B 的情报维度沿用 A 的 `intel` 机制（watch 源已覆盖「挖过的 B 户」；B1 下一步纳入 `intel_targets` 新闻 RSS）。')
    md = '\n'.join(L) + '\n'
    open(MD, 'w', encoding='utf-8').write(md)
    try:
        import markdown
        body = markdown.markdown(md, extensions=['tables'])
        open(HTML, 'w', encoding='utf-8').write('<!doctype html><html lang="zh"><head><meta charset="utf-8"><title>B 池分层 2026-10-31</title><style>body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;max-width:1500px;margin:24px auto;padding:0 16px;line-height:1.5}table{border-collapse:collapse;font-size:12.5px}td,th{border:1px solid #ccc;padding:3px 6px;vertical-align:top}th{background:#f3f3f3;position:sticky;top:0}tr:nth-child(even){background:#fafafa}blockquote{color:#555;border-left:3px solid #ccc;padding-left:10px}</style></head><body>' + body + '</body></html>')
    except Exception as ex:  # noqa
        print('html skipped', ex)
    # 跟进分组
    month = {'B1': ['2026-11', '2026-12', '2027-02', '2027-03', '2027-05'], 'B2': ['2026-12', '2027-02', '2027-04', '2027-06']}
    with open(os.path.join(SD, f'B跟进分组_{DATE}.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '公司', '国家', '区域', '层', '类型组', '语言', '依据', '最近来信', '首次群发月', '节奏'])
        for c, o in sorted(sel.items(), key=lambda kv: (kv[1]['tier'], kv[1]['region'], kv[0])):
            if o['tier'] == 'C':
                continue
            e = ents[c]
            lang = LANG.get(e.get('iso') or '', 'en')
            w.writerow([c, o['name'], o['country'], o['region'], o['tier'], type_group(o), lang, o['why'], o['last_in'], month[o['tier']][0], '每 6 周' if o['tier'] == 'B1' else '每 8 周'])
    print(MD, dict(tiers))


if __name__ == '__main__':
    main()
