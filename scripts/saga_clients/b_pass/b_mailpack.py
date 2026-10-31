#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B1 第一轮群发包（2026-11）：按「类型组 × 变体（再接 / 首触）」出 10 份母稿 + 按「区域 × 类型组 × 变体」出收件分组（Bcc 列表，≤30/批）。
价格只取 data/价格主表.csv（USD@+20/25/30% 列，快照 2026-10-17），不手写；英文；一机型一价一问；签名 Saga Telecom - sagatele.com。Simon 复制发送，Agent 不发信。"""
import csv
import json
import os
import re
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-31'
OUT_MD = os.path.join(ROOT, 'docs', '发送包', 'B1_R1_2026-11.md')
OUT_CSV = os.path.join(SD, 'B1_R1_2026-11_分组.csv')
BATCH = 30
FREE = re.compile(r'@(gmail|hotmail|yahoo|outlook|live|icloud|mail|yandex|protonmail|aol|gmx|web|list|bk|inbox|rambler|163|qq|126|telus|ymail|msn)\.', re.I)
BANNED = re.compile(r'list price|in stock|free sample|trading company|OEM Factory|NDAA|TAA|\bUL\b|GSA|general agent|we manufacture|Marvell ecosystem|SONiC|ONIE|cheap|best price|leading manufacturer', re.I)

# 型号选择（按 Simon 价阶：分销 20 / 集成 25 / OEM 30）
PLAN = {
    '分销商（20%）': ('STC-424DGGPM-280W', 'USD@+20%', '24 x GE PoE+ (280 W budget) + 4 x 1G/2.5G SFP, L2+ managed (ERPS ring, VLAN, SNMPv3), 1U steel, Marvell switching core', 'Which port count moves most in your channel - 8, 24 or 48 - so I quote the right SKU first?'),
    '集成/安装商（25%）': ('STC-28DGGPM', 'USD@+25%', '8 x GE PoE+ (120 W budget) + 4 x 1G/2.5G SFP, L2+ managed, fanless desktop/wall-mount, Marvell switching core', 'Is your next project standard PoE+ cameras, or PoE++ (90 W) devices that need the BT version?'),
    'OEM/品牌商（30%）': ('STI-288DGGPM', 'USD@+30%', '8 x GE PoE+ + 2 x 1G/2.5G SFP industrial L2+ managed, DIN-rail, 12-58 V dual input, -40 to +75 C, ERPS ring; your logo, label and firmware strings on request', 'If this goes under your own label, what MOQ per year should I price - 100, 300 or 1,000 units?'),
    'ISP/运营商': ('STC-424XGGM', 'USD@+25%', '24 x GE + 4 x 1G/2.5G/10G SFP+ uplinks, L2+ managed (ERPS, QinQ, IGMP snooping), 1U, Marvell switching core', 'Are your access rings still 1G, or already moving to 2.5G/10G uplinks?'),
    '其他/待核': ('STC-28DGGM', 'USD@+25%', '8 x GE + 4 x 1G/2.5G SFP, L2+ managed, fanless, Marvell switching core', 'What is the one switch model you buy most often today - so I can send a like-for-like quote?'),
}
OPENER = {
    '再接': 'Picking up our earlier exchange about PoE / industrial switches - one concrete option this time instead of a catalogue.',
    '首触': 'Short note from Saga Telecom, a Shenzhen switch OEM/ODM source built on Marvell silicon (and Centec for L3/10G), supplying distributors and integrators in Europe, North America and Turkiye under our label or theirs.',
}
CERT = {'欧洲': 'CE / RoHS / REACH documentation included; UKCA for UK shipments.', '北美': 'FCC / CE documentation included.', '土耳其': 'CE / RoHS documentation included.', '俄语区': 'CE / RoHS documentation included; EAC on request for volume orders.', '南亚': 'CE / RoHS documentation included.', '亚太': 'CE / RoHS documentation included.', '中东': 'CE / RoHS documentation included.', '非洲': 'CE / RoHS documentation included.', '拉美': 'CE / RoHS / FCC documentation included.'}
SHIP = {'欧洲': 'EXW Shenzhen; DAP to your door on request.', '北美': 'EXW Shenzhen; DAP or FOB Shenzhen on request.'}


def load_prices():
    px = {}
    for r in csv.DictReader(open(os.path.join(ROOT, 'data', '价格主表.csv'), encoding='utf-8-sig')):
        m = r.get('Saga对应型号', '').strip()
        if m:
            px[m] = r
    return px


def main():
    sel = json.load(open(os.path.join(SD, f'B类分层_{DATE}.json'), encoding='utf-8'))
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    px = load_prices()
    import importlib.util
    spec = importlib.util.spec_from_file_location('br', os.path.join(os.path.dirname(__file__), 'b_report.py'))
    br = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(br)
    groups = defaultdict(list)
    for c, o in sel.items():
        if o['tier'] != 'B1':
            continue
        e = ents[c]
        emails = [m for m in (e.get('emails') or []) if not FREE.search(m)] or list(e.get('emails') or [])
        if not emails:
            emails = [m for m in ((e.get('research') or {}).get('site_contacts') or {}).get('emails', []) if '@' in str(m)]
        variant = '再接' if (o['exA'] or o['rc'] in ('R+', 'Rw', 'R±')) else '首触'
        groups[(o['region'], br.type_group(o), variant)].append((c, e.get('name'), e.get('country'), emails[0] if emails else '', len(emails)))
    # 母稿
    L = [f'# 发送包 B1 第一轮（2026-11）· 生成 {DATE}\n',
         '**Simon 复制发送；Agent 不发信。** 口径：B1 重点普通跟 = 分组群发（Bcc，每批 ≤30），每封一机型一价一问；再接变体给「出 A 户 / 有过回信」，首触变体给「强对位但没聊过」。价格只取 `data/价格主表.csv`（快照 2026-10-17，15 天有效；表内价效期至 2026-12-30）。发出后在对应户 MD「新跟进记录」补一行，或丢给我批量记。\n',
         '## 1. 十份母稿（类型组 × 变体）\n']
    masters = {}
    for tg, (model, col, spec_txt, q) in PLAN.items():
        r = px.get(model)
        price = r[col] if r else '（价格主表无此型号 → 不发）'
        for variant in ('再接', '首触'):
            subj = f"{model} - {spec_txt.split(',')[0]} - USD {price} EXW"
            body = '\n'.join([
                'Hi {first_name},', '',
                OPENER[variant], '',
                f"{model}: {spec_txt}.",
                f"USD {price} EXW Shenzhen per unit (price snapshot 2026-10-17, valid 15 days from this mail; paid samples at the same price, shipped by express).",
                '{cert_line}', '',
                q, '',
                'Simon', 'Saga Telecom - sagatele.com'])
            assert not BANNED.search(subj + body), (tg, variant)
            masters[(tg, variant)] = (subj, body, model, price)
            L.append(f'### {tg} · {variant}\n')
            L.append(f'- 型号 {model} · 价列 {col} = **USD {price}**（SmartByte {r["SmartByte型号"] if r else "—"}）· 一问：{q}\n')
            L.append('```text')
            L.append('Subject: ' + subj)
            L.append('')
            L.append(body)
            L.append('```')
            L.append('')
    L.append('`{first_name}` 群发时统一用 "Hi there," 或各组主语言的通用称呼；`{cert_line}` 按区域替换：' + '；'.join(f'{k} → {v}' for k, v in CERT.items()) + '。欧洲/北美可加运输一句：' + '；'.join(f'{k} → {v}' for k, v in SHIP.items()) + '\n')
    L.append('## 2. 收件分组（区域 × 类型组 × 变体；Bcc，每批 ≤30）\n')
    rows = []
    for (region, tg, variant), lst in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2])):
        subj, body, model, price = masters[(tg, variant)]
        batches = [lst[i:i + BATCH] for i in range(0, len(lst), BATCH)]
        L.append(f'### {region} · {tg} · {variant} · {len(lst)} 户 · {len(batches)} 批 · 母稿「{tg} · {variant}」· {CERT.get(region, "")}\n')
        for bi, b in enumerate(batches, 1):
            L.append(f'- 批 {bi}（{len(b)}）：' + ', '.join(f"{c} {m}" for c, n, cn, m, k in b if m) + (('；无邮箱：' + ', '.join(c for c, n, cn, m, k in b if not m)) if any(not m for c, n, cn, m, k in b) else ''))
            for c, n, cn, m, k in b:
                rows.append([region, tg, variant, bi, c, n, cn, m, k, model, price, subj])
        L.append('')
    L.append('## 3. 规矩\n- 每封只一问；不提竞品名；不写 UL / NDAA / TAA / GSA / 免费样品 / 现货 / 最低价；样品付费；UKCA 只对英国；非欧盟默认 DAP 或 FOB 深圳；英文发、中文只做备注。\n- 回信（问价 / 要样 / 报量 / 项目）→ 进 A 候选走六项核验；婉拒 → C 储备；无回 → 6 周后第二轮（换机型 + 换问题）。\n')
    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    with open(OUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['区域', '类型组', '变体', '批', '编号', '公司', '国家', '收件', '邮箱数', '型号', 'USD', '主题'])
        w.writerows(rows)
    print(OUT_MD, 'groups', len(groups), 'recipients', len(rows), 'no-email', sum(1 for r in rows if not r[7]))


if __name__ == '__main__':
    main()
