#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A / B 新评级标准 · 模拟（只读，不改任何等级；T29-U125，2026-10-29）。

目的：给「判定 A/B + 新标准」讨论一个可以拍板的底稿——把草案标准（docs/AB判定_新标准_讨论稿_2026-10-29.md §3）
按库里现成的证据字段算一遍，看 A / B 各会变成什么样，差异逐户列出来给 Simon 勾。

证据字段（全部已有，不新查）：
  成单 flags.deal / 样品 flags.sample / PI pi / 邮件真回次数 reply_sub / 打开 reply_read / WA flags.wa_added、wa_in_fu
  绑定深度 research.mail_review.binding.level 前缀（深 / 较深 / 中度 / 轻度… / 未绑定 / 未触达…）
  对位 fit.switch / fit.mc_sfp / 自有品牌 flags.own_brand / 最近往来 fu_last / 表内状态 status / 标签 tags（S重点）
  登记 ✔ · 体量 · 区域组 · 红旗（gg / 巨头 / 注销）：取 data/saga_clients/AB并池_预演_2026-10-29.csv（ab_pool_dryrun.py 已算）
  池位：data/saga_clients/sieve.json（AB-01 后 A/B 行）

草案标准 v1（命中即定，自上而下）：
  A  = A1 复购（成单 ≥2）或绑定 ≥ 中度，且非 gg
     | A2 成单 / 付样 / PI ≥1 + 真人往来（邮件真回 ≥1 或 WA 已加）+ 近 24 个月有往来，且非 gg
     | A3 决策人真回 ≥2 + 交换机对位 + 四主区 / 波兰 + 登记坐实 + （体量 ≥10 人 或 自有品牌）
     | A4 Simon 点名（tags S重点 / 状态含「（Simon）」且非 gg）
  B  = B1 成单 / 付样 / PI 但 gg / 凉 / 无近期往来
     | B2 真回 ≥1 或 WA 已加 或 读而不回（有打开 ≥2）+ 对位（交换机 / MC）
     | B3 自有品牌 + 交换机对位（OEM 对象，任何区域）
     | B4 四主区 / 波兰 + 交换机对位 + 登记坐实（冷但坐实）
  C  = 其余（冷 / 不对位 / 守界 UA·IR·SY / 注销）
两档口径同时算（给 Simon 调旋钮用）：
  严（strict）= 上面的 v1 原样。
  宽（wide）  = A2 去掉「近 24 个月」限制并把「展会面谈 / 名片」算作真人往来；A3 真回 ≥1（或展会面谈）+ 对位 + 四主区 / 波兰 + （坐实 或 自有品牌）；
                新增 A5 自有品牌 + 交换机对位 + 任一真人往来（OEM 品牌商，任何区域）、A6 真回 ≥3 + 对位（任何区域，关系深度本身算数）；B 新增 B5 四主区 / 波兰 + 交换机对位（未坐实的冷户也留 B 走发送包）。
  真回次数 = reply_sub 与 mail_review.facts「来」向真人来信条数取大者（Elsa 箱 2026 年来信只在 facts 里，如 SB-1139 / SB-1134）。
  宽留冷（keep_cold）= 宽 + B6 对位的冷户任何区域都留 B（只有不对位 / 守界 / 注销才去 C）。
  「对位」字段漏标不少：有成单 / 样品 / PI / 真回 ≥3 的户视同对位；登记注销（非 Simon 点名）最高 B；守界 UA / IR / SY 一律 C。
输出：data/saga_clients/AB新标准_模拟_2026-10-29.csv（两列建议：建议-严 / 建议-宽）+ 统计打印。
"""
import collections
import csv
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
OUT = os.path.join(DATA, 'AB新标准_模拟_2026-10-29.csv')
DRY = os.path.join(DATA, 'AB并池_预演_2026-10-29.csv')
MAIN = '四主区 + 波兰'
GUARD = {'乌克兰', '伊朗', '叙利亚'}
RECENT = '2024-11-01'   # 近 24 个月（以 2026-10-29 为基准）


def bind_class(e):
    s = (((e.get('research') or {}).get('mail_review') or {}).get('binding') or {}).get('level') or ''
    head = re.match(r'^([^\（(：:；;，,]+)', s)
    head = head.group(1) if head else s
    if re.match(r'^(深|较深|中度)', head):
        return 3, head[:6]
    if head.startswith('轻度') and '触达' not in head[:4]:
        return 2, head[:6]
    if head.startswith('轻度触达') or head.startswith('读而不回'):
        return 1, head[:6]
    return 0, (head[:6] or '—')


def employees(txt):
    m = re.search(r'(\d{1,4})(?:\s*[–\-~]\s*(\d{1,4}))?\s*人', txt or '')
    if not m:
        m2 = re.search(r'≈\s*(\d{1,4})', txt or '')
        return int(m2.group(1)) if m2 else None
    return int(m.group(2) or m.group(1))


def main():
    ents = {e['code']: e for e in json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))}
    dry = {r['编号']: r for r in csv.DictReader(open(DRY, encoding='utf-8-sig'))}
    sieve = json.load(open(os.path.join(DATA, 'sieve.json'), encoding='utf-8'))
    rows = []
    for code, r in dry.items():
        e = ents[code]
        f = e.get('flags') or {}
        deals = int(f.get('deal') or 0)
        sample = bool(f.get('sample'))
        pi = bool(e.get('pi'))
        # 真回次数 = 用户表 / S·A digest 的 reply_sub，与 mail_review.facts 里「来」向真人来信条数取大者（Elsa 箱 2026 年的来信只在 facts 里）
        facts = ((e.get('research') or {}).get('mail_review') or {}).get('facts') or []
        n_in = sum(1 for x in facts if isinstance(x, dict) and x.get('dir') == '来' and not re.search(r'noreply|no-reply|auto|out of office|delivery|mailer-daemon|退信|自动回复', (x.get('who') or '') + ' ' + (x.get('quote') or ''), re.I))
        replies = max(int(e.get('reply_sub') or 0), n_in)
        opens = int(e.get('reply_read') or 0)
        wa = bool(f.get('wa_added')) or bool(e.get('wa_in_fu'))
        bc, bhead = bind_class(e)
        fit = e.get('fit') or {}
        sw = bool(fit.get('switch'))
        mc = bool(fit.get('mc_sfp'))
        own = bool(f.get('own_brand'))
        recent = (e.get('fu_last') or '') >= RECENT
        reg = (r['登记'] or '').startswith('✔')
        emp = employees(r['体量'])
        grp = r['区域组']
        flag = r['红旗'] or ''
        gg = 'gg' in flag
        dead = '注销' in flag
        guard = (e.get('country') or '') in GUARD
        simon = ('S重点' in (e.get('tags') or [])) or ('（Simon）' in (e.get('status') or ''))
        blob = ' '.join((e.get('reasons') or []) + (e.get('remarks') or []) + [e.get('status') or '']) + ' ' + ' '.join(str(x) for x in (e.get('interests') or []))
        fair = bool(re.search(r'展会|ISAF|名片|面谈|到访|booth|fair', blob, re.I))
        human = replies >= 1 or wa
        human_w = human or fair
        # 「对位」字段（fit.switch / mc_sfp）是从兴趣词推的，漏标不少（ОПТА 18 次真回却无对位标）——有成单 / 样品 / PI / 真回 ≥3 的户视同对位
        fit_ok = sw or mc or deals >= 1 or sample or pi or replies >= 3 or (e['grade'] == 'A' and not fit.get('off'))   # A 档是人工挑过的，未标 off 视同对位

        def judge(wide, keep_cold=False):
            hits = []
            if deals >= 2 or bc >= 3:
                hits.append('A1 复购/绑定≥中度')
            if (deals >= 1 or sample or pi) and ((human_w) if wide else (human and recent)):
                hits.append('A2 成单/样品/PI+真人往来' + ('' if wide else '+近24月'))
            if wide:
                if human_w and fit_ok and grp == MAIN and (reg or own):
                    hits.append('A3 真人往来+对位+四主区+坐实/自牌')
                if own and fit_ok and human_w:
                    hits.append('A5 自有品牌+对位+真人往来')
                if replies - int(e.get('reply_neg') or 0) >= 3 and fit_ok and not re.search(r'无需求|拒|停发|不要', e.get('status') or ''):
                    hits.append('A6 真回≥3+对位（任何区域）')
            elif replies >= 2 and fit_ok and grp == MAIN and reg and ((emp or 0) >= 10 or own):
                hits.append('A3 真回≥2+对位+四主区+坐实+体量/自牌')
            if simon:
                hits.append('A4 Simon 点名')
            a_hits = [] if gg else hits
            bh = []
            if deals >= 1 or sample or pi:
                bh.append('B1 成单/样品/PI（gg/凉/无近期往来）')
            if (replies >= 1 or wa or opens >= 2 or (fair if wide else False)) and fit_ok:
                bh.append('B2 真回/WA/有打开' + ('/展会' if wide else '') + '+对位')
            if own and fit_ok:
                bh.append('B3 自有品牌+对位')
            if grp == MAIN and fit_ok and reg:
                bh.append('B4 四主区+对位+坐实')
            if wide and grp == MAIN and fit_ok:
                bh.append('B5 四主区+对位（冷）')
            if keep_cold and fit_ok:
                bh.append('B6 对位（冷，任何区域）')
            if guard:
                return 'C', '守界（' + (e.get('country') or '') + '）'
            if dead and not simon:
                bh.insert(0, '登记注销 / 主体不明 → 最高 B，待核')
                a_hits = []
            if a_hits:
                return 'A', '；'.join(a_hits)
            if gg and hits:
                bh.insert(0, 'gg：' + '/'.join(h.split(' ')[0] for h in hits) + ' 不计 A')
            if bh:
                return 'B', '；'.join(bh)
            return 'C', '冷 / 不对位（' + ('对位 ✔' if fit_ok else '不对位') + f'，真回 {replies}，WA {"✔" if wa else "—"}，展会 {"✔" if fair else "—"}，绑定 {bhead}）'

        prop, basis = judge(False)
        prop_w, basis_w = judge(True)
        prop_k, basis_k = judge(True, keep_cold=True)
        cur = e['grade']

        def chg(p):
            return '不变' if p == cur else ('升' if (cur, p) in (('B', 'A'), ('C', 'B'), ('C', 'A')) else '降')
        change, change_w, change_k = chg(prop), chg(prop_w), chg(prop_k)
        sv = sieve.get(code) or {}
        pool = (sv.get('grade') or '') + ('正式' if sv.get('verdict') == 'pool' else ('观察' if sv.get('verdict') == 'pool_watch' else '—'))
        rows.append({'编号': code, '现等级': cur, '建议-严': prop, '变化-严': change, '命中-严': basis, '建议-宽': prop_w, '变化-宽': change_w, '命中-宽': basis_w,
                     '建议-宽留冷': prop_k, '变化-宽留冷': change_k, '命中-宽留冷': basis_k,
                     '公司': r['公司（登记名优先）'], '国家': e.get('country') or '', '区域组': grp,
                     '成单': deals or '', '样品': '✔' if sample else '', 'PI': '✔' if pi else '', '真回次数': replies, '打开': opens, 'WA': '✔' if wa else '', '展会': '✔' if fair else '', '绑定': bhead,
                     '对位': '✔ 交换机' if sw else ('✔ MC' if mc else '—'), '自有品牌': '✔' if own else '', '登记': '✔' if reg else '', '体量(人)': emp or '', '最近往来': e.get('fu_last') or '',
                     '表内状态': e.get('status') or '', '红旗': flag, '现池位': pool, '预演结论': r['预演结论'], 'Simon 裁定': ''})
    order = {'降': 0, '升': 1, '不变': 2}
    rows.sort(key=lambda x: (order[x['变化-宽']], order[x['变化-严']], x['现等级'], x['建议-宽'], x['编号']))
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(os.path.relpath(OUT, ROOT), len(rows))
    for tag, pk, hk in (('严', '建议-严', '命中-严'), ('宽', '建议-宽', '命中-宽'), ('宽留冷', '建议-宽留冷', '命中-宽留冷')):
        mat = collections.Counter((x['现等级'], x[pk]) for x in rows)
        print(f'[{tag}]', {cur: {p: mat[(cur, p)] for p in ('A', 'B', 'C')} for cur in ('A', 'B')}, '→ 新 A', mat[('A', 'A')] + mat[('B', 'A')], '新 B', mat[('A', 'B')] + mat[('B', 'B')], '→C', mat[('A', 'C')] + mat[('B', 'C')])
        rules = collections.Counter(h.split(' ')[0] for x in rows for h in x[hk].split('；') if re.match(r'^[AB]\d', h))
        print('   rule hits', dict(sorted(rules.items())))
        print('   升 A (B→A):', [x['编号'] for x in rows if x['现等级'] == 'B' and x[pk] == 'A'])
        print('   A→C:', [x['编号'] for x in rows if x['现等级'] == 'A' and x[pk] == 'C'])
    return rows


if __name__ == '__main__':
    main()
