#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群 · 批 LT-01（T29-U128，2026-10-29；Q-76 并成一套 + Q-72 口径 = 宽留冷，Simon U128 方向）。

Simon U128：「AB 长期跟…保证这一大团都是 OK 的」「C 捞上来的 349 户…直接定为 B」「之前的 A 类先不用操作」
「没咋调研过的（C 升 B 的）要深挖，不行直接打回 C」「确保剩余的 AB 类客户都是不错的」。

本脚本只做 Saga 库的「定档」层（研究档 grade_override），不做调研；调研 = 复核队列（lt_review 待过），分批另跑。
规则（docs/AB判定_新标准_讨论稿_2026-10-29.md §3 宽留冷口径 + U128 修正）：
  · 1,229 A/B：按 `AB新标准_模拟_2026-10-29.csv` 的「建议-宽留冷」——
      B→A 104：研究档 grade_override=A；A→B 24：grade_override=B（仍在长期群，普通跟）；
      B→C 212「不对位冷户」：**不降**（抽样证明多是「对位未知」而非「不对位」：SB-055 安防集成 / SB-1019 布线品牌 / SB-1001 PoE 配套机箱）
        → 留 B + lt_review 待过（优先级 2），复核后真不对位再打回 C；唯一例外 SB-007 乌克兰守界 → C（c_sub=储备·守界）。
      Simon 人工定级.csv / PI 标签「活跃 / 可发展」优先（build.py 本来就这样），脚本不与之相抵。
  · C 池捞出（sieve verdict pool / pool_watch 且现等级 C）211：grade_override=B（Simon「那就直接定为 B」）+ lt_review 待过（优先级 1）；
      无研究档的建骨架（summary = 闸 2 / 闸 1 理由，deepen.py 同款字段）。
落点：data/saga_clients/research/<code>.json（grade_override / override_reason / override_history / lt_review）
      data/saga_clients/长期客户群_LT-01_变更_2026-10-29.csv
之后：build.py → render 链 → audits。幂等（history 以 batch 守卫）。
"""
import csv
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
RESEARCH = os.path.join(DATA, 'research')
SIM = os.path.join(DATA, 'AB新标准_模拟_2026-10-29.csv')
OUT = os.path.join(DATA, '长期客户群_LT-01_变更_2026-10-29.csv')
BATCH = 'LT-01'
DATE = '2026-10-29'
TAG = f'Q-76 {BATCH} {DATE}'


def short(s, n):
    s = re.sub(r'\s+', ' ', s or '')
    return s if len(s) <= n else s[:n - 1] + '…'


def load_research(code):
    p = os.path.join(RESEARCH, code + '.json')
    if os.path.exists(p):
        return json.load(open(p, encoding='utf-8')), False
    return None, True


def skeleton(code, name, summary):
    return {'code': code, 'name_official': name or '', 'researched_at': DATE, 'website_status': '',
            'summary': summary or '（C 池三闸捞出建档；证据见闸 1 / 闸 2 理由）', 'type': '', 'size': '', 'brands_seen': [],
            'evidence': [], 'kp': [], 'grade_override': None, 'override_reason': '',
            'notes': f'（无首轮调研；{BATCH} 并入长期客户群时建骨架，待复核加厚）'}


def apply(rs, target, reason, review=None):
    """写 override + history（batch 守卫幂等）。返回 True = 本次有写。"""
    hist = rs.setdefault('override_history', [])
    if any(h.get('batch') == BATCH and h.get('to') == target for h in hist):
        if review and rs.get('lt_review', {}).get('batch') != BATCH:
            rs['lt_review'] = review
        return False
    hist.append({'batch': BATCH, 'date': DATE, 'from_override': rs.get('grade_override'), 'to': target,
                 'prev_reason': rs.get('override_reason') or '', 'reason': reason})
    rs['grade_override'] = target
    rs['override_reason'] = reason
    if review:
        rs['lt_review'] = review
    return True


def main():
    now = subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()
    ents = {e['code']: e for e in json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))}
    sieve = json.load(open(os.path.join(DATA, 'sieve.json'), encoding='utf-8'))
    sim = list(csv.DictReader(open(SIM, encoding='utf-8-sig')))
    manual = {r['键或编号'] for r in csv.DictReader(open(os.path.join(DATA, '人工定级.csv'), encoding='utf-8-sig'))}
    rows, cnt = [], {}

    def tick(k):
        cnt[k] = cnt.get(k, 0) + 1

    # ① 1,229 A/B
    for r in sim:
        code = r['编号']
        e = ents[code]
        cur, target, hit = e['grade'], r['建议-宽留冷'], r['命中-宽留冷']
        rs, new = load_research(code)
        if rs is None:
            rs = skeleton(code, e.get('name'), '')
        review = None
        if target == 'C':
            if code == 'SB-007':
                target, reason = 'C', (f'{TAG}：守界（乌克兰）→ C 储备，不发不跟，战后再看；c_sub=储备·守界 ；宽留冷命中：{hit}')
            else:
                target = 'B'
                reason = None
                review = {'batch': BATCH, 'status': '待过', 'prio': 2, 'date': DATE,
                          'why': f'宽留冷口径判「不对位冷户」（{short(hit, 80)}）；抽样证明多为「对位未知」→ 留 B 待复核：确认行业内 + 对位 + 成单可能，否则打回 C 储备'}
        elif target != cur:
            if target == 'A':
                reason = f'{TAG}：B→A 核心（精华跟）：{hit}'
            else:
                reason = f'{TAG}：A→B 普通跟（核心证据不足：{hit}）；仍在长期客户群，有真人往来 / 成单即回 A'
        else:
            reason = None
        pi_lab = (e.get('pi') or {}).get('simon') or ''
        if reason and target != 'A' and pi_lab in ('活跃', '可发展'):
            tick('skip_pi_simon')
            rows.append([code, e.get('name'), e.get('country'), cur, cur, f'跳过：Simon PI 标签「{pi_lab}」优先（build.py 强制 A）', ''])
            continue
        if reason and code in manual:
            tick('skip_manual')
            rows.append([code, e.get('name'), e.get('country'), cur, cur, '跳过：人工定级.csv（Simon 原话）优先', ''])
            continue
        changed = False
        if reason:
            changed = apply(rs, target, reason, review)
            tick(f'{cur}->{target}')
        elif review:
            if rs.get('lt_review', {}).get('batch') != BATCH:
                rs['lt_review'] = review
                changed = True
            tick('B keep 待过')
        else:
            tick(f'{cur} keep')
        if changed or new:
            json.dump(rs, open(os.path.join(RESEARCH, code + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        if reason or review:
            rows.append([code, e.get('name'), e.get('country'), cur, target, reason or '留 B', (review or {}).get('why', '')])

    # ② C 池捞出 211 → B 待过
    for code, v in sieve.items():
        if code == '_meta' or v.get('verdict') not in ('pool', 'pool_watch'):
            continue
        e = ents.get(code)
        if not e or not code.startswith('SC-'):   # C 池捞出 = SC- 前缀的池行（与当前等级无关 → 幂等）
            continue
        g2 = v.get('g2_reason') or v.get('reason') or ''
        g1 = v.get('g1_reason') or ''
        rs, new = load_research(code)
        if rs is None:
            rs = skeleton(code, e.get('name'), f'C 池三闸捞出（{v.get("grade", "")} {"正式" if v["verdict"] == "pool" else "观察"}）：{short(g2, 220)}')
        reason = (f'{TAG}：C 池三闸捞出 → B（Simon U128「那就直接定为 B」；长期客户群 · 普通跟）；闸 2：{short(g2, 200)}'
                  + (f'；闸 1：{short(g1, 120)}' if g1 else ''))
        review = {'batch': BATCH, 'status': '待过', 'prio': 1, 'date': DATE,
                  'why': f'C 升 B（池位 {v.get("grade", "")}，{"坐实" if v.get("grade") in ("★", "★★") else "部分坐实 / 未坐实"}）→ 深挖：官网 / 进口数据 / 项目，确认行业内 + 对位 + 成单可能；不明朗 → 打回 C 储备'}
        changed = apply(rs, 'B', reason, review)
        if not rs.get('mail_review'):
            # 升 B 后审计要求 A/B 研究档有邮件复盘块；C 池捞出户无往来记录 → 如实写「未绑定 / 无往来」，事实项 = 三闸证据（dir=查，不计真回）
            rs['mail_review'] = {
                'as_of': DATE,
                'binding': {'level': '未绑定（C 池捞出，仓内无往来记录）', 'basis': '三闸：闸 0 活着 + 闸 1 对位候选 + 闸 2 坐实 / 部分坐实'},
                'situation': f'C 池三闸捞出 → B（{BATCH}）：{short(g2, 200)}',
                'need': '未知（无往来；复核时从官网 / 进口数据 / 项目推断）',
                'breakpoint': '无往来（从未触达或仅群发无回）',
                'saga_now': {'p1': '', 'why': '待复核后按业务线定首推型号'},
                'next_move': {'when': '不动：LT-01 复核（待过）后再定', 'channel': '—', 'action': '长期客户群复核：确认行业内 + 对位 + 成单可能；不明朗 → 打回 C 储备'},
                'facts': [{'date': DATE, 'dir': '查', 'who': 'Agent 三闸（sieve.json）', 'quote': short(g2 or g1, 300), 'why': '闸 2 坐实 / 对位依据（非邮件事实，不计真回）'}],
                'proof_gaps': ['无往来记录；复核待补：官网业务线 / 进口数据 / 项目案例'],
            }
            changed = True
        if changed or new:
            json.dump(rs, open(os.path.join(RESEARCH, code + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        tick('C->B pool')
        rows.append([code, e.get('name'), e.get('country'), 'C', 'B', reason, review['why']])

    # 变更清单从研究档 history 重建（幂等、与运行次数无关）
    out = []
    for fn in sorted(os.listdir(RESEARCH)):
        if not fn.endswith('.json'):
            continue
        d = json.load(open(os.path.join(RESEARCH, fn), encoding='utf-8'))
        code = d.get('code') or fn[:-5]
        e = ents.get(code, {})
        hs = [h for h in d.get('override_history') or [] if h.get('batch') == BATCH]
        rv = d.get('lt_review') or {}
        if hs:
            h = hs[-1]
            frm = 'C' if code.startswith('SC-') else ('A' if h['reason'].find('A→B') >= 0 else ('B' if 'B→A' in h['reason'] or 'B→C' in h['reason'] or '守界' in h['reason'] else '?'))
            out.append([code, e.get('name'), e.get('country'), frm, h['to'], h['reason'], rv.get('why', '') if rv.get('batch') == BATCH else ''])
        elif rv.get('batch') == BATCH:
            out.append([code, e.get('name'), e.get('country'), 'B', 'B', '留 B（宽留冷判不对位冷户 → 不降，复核）', rv.get('why', '')])
    order = {'C': 0, 'A': 1, 'B': 2}
    out.sort(key=lambda r: (order.get(r[3], 9), r[4] != 'A', r[0]))
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '公司', '国家', '原等级', '新等级', '理由', '复核'])
        w.writerows(out)
    print(BATCH, now, cnt, 'rows(this run)', len(rows), 'csv', len(out))


if __name__ == '__main__':
    main()
