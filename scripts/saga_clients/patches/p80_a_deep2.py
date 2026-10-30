#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p80 · A-DEEP-02「不是极为 OK 的就 B」（T29-U140 2026-10-30，Simon：EMOS「B吧 不是极为OK的就B 继续挖」）。
口径：PI 成单 20 户不动；其余 A 户凡 ① 个人 / 微型（≤10 人或 <£1M 级）且无进行中的具体项目/样品单 ② 结构性采购障碍（只买美国/TAA 产地、自有海外制造、国防/铁路主业）
③ 巨头集团子公司（Legrand 等）④ 非主攻区 + 互动薄 → 下放 B（保留全部研究档与情报，B1 重点普通跟）。
写 grade_override='B' + override_history（batch A-DEEP-02）+ a_deep.verdict2；追加 复核记录。幂等。"""
import csv
import json
import os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
RESEARCH = os.path.join(SD, 'research')
DATE = '2026-10-30'
BATCH = 'A-DEEP-02'
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')

DEMOTE = {
    'SB-461': 'EMOS（捷克，290 人）2022 年起为 Legrand 集团成员 → 巨头子公司，Simon 2026-10-30 定 B',
    'SB-010': 'American Fibertek：Made in America / BAA + 外采线要求 TAA 合规（中国产地不合规）→ 结构性障碍',
    'SB-787': 'TC Communications：「Made in the USA since 1991」+ 铁路/军方主客群 → 结构性障碍 + 守界',
    'SB-831': 'Actelis：10-K 自述在以色列 + 台湾制造、原料直采两地；FIPS/国防路线；一年三轮融资；回信只「Maybe…」→ 结构性障碍',
    'SB-474': 'Case Communications：Companies House 3 人、营业额 <£1M 微型（自牌加固交换机 ODM 对位保留为 B1 重点）',
    'SB-137': 'Oral Güvenlik：北塞浦路斯家族集团下 6 人安防公司 → 微型',
    'SB-167': 'Onsis：安卡拉约 6 人弱电承包商 → 微型',
    'SB-185': 'Zeytek：伊斯坦布尔 5 人 IT 经销 → 微型',
    'SB-149': 'Klasnet：2021 年成立的布尔萨小型弱电承包商 → 微型',
    'SB-130': 'Bonmag / OMNI Security：罗马尼亚微型安装商 → 微型',
    'SB-079': 'Cansis Teknoloji：微型安防/电脑零售安装商 → 微型',
    'SA-005': 'Taurus Vision：南非 1–10 人集成商，非主攻区 → 微型 + 非主攻',
    'SB-1139': 'Arnoldo Beltetón Mohr：危地马拉个人方案顾问（项目型）→ 个人 + 非主攻',
    'SC-584': 'Namba Software：巴西小型 IT 方案商，只要测 1 台 → 非主攻 + 薄',
    'SC-1623': 'Southern Elements：南非光纤网店，一次问 10 台价 → 非主攻 + 薄',
    'SB-018': 'Walker Security Systems UG：夫妻 2 人微型安装商 → 微型',
    'SB-022': 'Desk Technologies：德国微型安防项目商，仅表内备注、0 回信 → 微型',
    'SB-027': 'VoIPDistri：1 人 + 兼职 → 微型',
    'SB-040': '4Demand：<10 人、营业额 <£1M → 微型',
    'SB-063': 'Avesta：1–9 人微型 → 微型',
    'SB-151': 'Optiwatch：1 名董事小微账目 → 微型',
    'SB-360': 'Longtek：夫妻 2 人 → 微型',
    'SB-1031': 'Findcontrols：1 名股东微型 → 微型',
    'SB-246': 'isnetworks.pl：个体户 → 微型',
    'SB-696': 'Aironix：微型（经营者 + 1 销售）→ 微型',
    'SB-129': 'Addon Technology Ltd：估 2–10 人、SIC 62090 IT 咨询 → 微型 + 对位弱',
    'SC-2802': 'Euro Security Solutions：微型（推定）→ 微型',
    'SA-025': 'Avenger Security：1–5 人安装商、自装自用 → 微型',
    'SA-036': 'svn-video.ru：1–5 人 → 微型',
    'SB-085': 'DIGI Group / Thor Fiber：实际 1–10 人，3 封回信 2025 → 微型',
    'SB-1114': 'Fikes Media：1 人副业 → 个人',
    'SB-988': 'Infinity Hardware：2–10 人 → 微型',
    'SA-058': 'Alphanet：2–10 人布线承包商 → 微型',
    'SA-053': 'infrateq.id：2–10 人、非主攻区 → 微型 + 非主攻',
    'SB-692': 'Anda Telecom：1–10 人、FY2024 营收 ₹12.8M → 微型 + 非主攻',
    'SB-055': 'DIOS：荷兰 5–9 人安防经销，2 封回信（要价目表）→ 微型',
    'SA-068': 'PT. RAS Otomasi：非主攻区、0 封邮件回信、只 2023–24 表内备注 → 非主攻 + 薄',
}


DEMOTE3 = {  # A-DEEP-03（T29-U141 2026-10-30）：土耳其收尾网查后的微型 / 不可核
    'SB-140': 'AG Bilgisayar：博德鲁姆本地电脑维修 + 监控安装小店 → 微型',
    'SB-153': 'Sinerjik：sinerjik.net 无可核官网，网查未得 → 身份不可核',
    'SB-225': 'Shnrise / CESS Güvenlik：同一经营者两块牌子的小型安装商 → 微型',
    'SB-388': 'FH Güvenlik：2025-02 新注册的小型弱电集成商 → 微型（观察一年）',
}


def main():
    manual = set()
    p_m = os.path.join(SD, '人工定级.csv')
    if os.path.exists(p_m):
        for r in csv.DictReader(open(p_m, encoding='utf-8-sig')):
            manual.add((r.get('键或编号') or list(r.values())[0] or '').strip())
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    cnt = Counter()
    rows = []
    for c, why in list(DEMOTE.items()) + list(DEMOTE3.items()):
        batch = 'A-DEEP-03' if c in DEMOTE3 else BATCH
        p = os.path.join(RESEARCH, c + '.json')
        if not os.path.exists(p):
            cnt['no_research'] += 1
            continue
        if ents.get(c, {}).get('pi'):
            cnt['pi_skip'] += 1
            continue
        if c in manual:
            cnt['manual_skip'] += 1
            continue
        rs = json.load(open(p, encoding='utf-8'))
        reason = f'{batch} {DATE} 「不是极为 OK 的就 B」（Simon）→ 下放 B：{why}'
        hist = rs.setdefault('override_history', [])
        if not any(h.get('batch') == batch for h in hist):
            hist.append({'batch': batch, 'date': DATE, 'from_override': rs.get('grade_override'), 'to': 'B', 'prev_reason': rs.get('override_reason') or '', 'reason': reason})
            rows.append([c, ents.get(c, {}).get('name', ''), ents.get(c, {}).get('country', ''), ents.get(c, {}).get('grade', ''), 'B', batch, DATE, reason[:200]])
        rs['grade_override'] = 'B'
        rs['override_reason'] = reason[:600]
        ad = rs.setdefault('a_deep', {})
        ad['verdict2'] = '下放B'
        ad['verdict2_batch'] = batch
        ad['verdict2_reason'] = why
        json.dump(rs, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        cnt['下放B'] += 1
    have = set()
    if os.path.exists(LOG):
        have = {(x['编号'], x['批次']) for x in csv.DictReader(open(LOG, encoding='utf-8-sig'))}
    new = [x for x in rows if (x[0], x[5]) not in have]
    with open(LOG, 'a', encoding='utf-8-sig', newline='') as f:
        csv.writer(f).writerows(new)
    print(BATCH, dict(cnt), 'log +', len(new))


if __name__ == '__main__':
    main()
