#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p78 · AB-FINAL-01 应用 A 级终评（T29-U136 2026-10-30，Simon 规则：A = 成单 + 有过回信沟通 + 极贴合）。
读 data/saga_clients/A类终评_2026-10-30.json（由 ab_final/a_select.py 生成），对每户：
  · target A（三档 A1 成单 / A2 回信 / A3 贴合）→ research.grade_override='A' + override_reason + override_history（batch AB-FINAL-01）
  · 现 A 而 target B（无成单无回信、婉拒、巨头/台湾/守界、仅自动回复）→ grade_override='B'
  · 现 C 而 target B（有实质回复但非主攻区薄回复 / 排除项）→ grade_override='B'（U128 ② C 捞出直接 B），sieve 行 verdict→pool（等级 B）
  · 所有触及户写 research['ab_final'] = {date, tier, target, reason, why_not, evidence}
人工定级.csv 有码的户（Simon 亲定）不动，只记录。幂等：history 以 batch 去重；重复运行不改变结果。
之后需 build.py → render.py 才生效。日志追加 data/长期客户群_复核记录.csv。
"""
import csv
import importlib.util
import json
import os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
RESEARCH = os.path.join(SD, 'research')
DATE = '2026-10-30'
BATCH = 'AB-FINAL-01'
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')


def load_sieve_mod():
    spec = importlib.util.spec_from_file_location('sieve_mod', os.path.join(ROOT, 'scripts', 'saga_clients', 'sieve.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def build_mail_review(e, r, d):
    facts = []
    for m in d.get('msgs') or []:
        if m['cls'] == 'auto':
            continue
        facts.append({'date': m['date'], 'dir': '来', 'who': m['from'], 'quote': (m['subj'] + '｜' + m['excerpt'])[:300], 'why': f"{ {'S': 'S 邮箱', 'A': 'Alan 邮箱', 'E': 'Elsa 邮箱'}.get(m['box'], m['box']) } 真人来信（{m['cls']}）", 'k': m['k']})
    for t in d.get('tbl_replies') or []:
        facts.append({'date': t['date'], 'dir': 'Simon', 'who': '用户表（Simon 跟进记录）', 'quote': f"推「{t['content']}」→ 对方「{t['reply']}」", 'why': f"表内客户回复（{t['kind']}）", 'k': 'Clients/ 表格'})
    return facts, {'as_of': DATE, 'facts': facts,
                   'binding': {'level': '轻度触达（有来信/表内回复，见 facts；无成单）', 'note': f'{BATCH} 建档'},
                   'situation': f"{e.get('country') or ''}；{(facts[-1]['date'] if facts else '')} 最后一次来信/回复：{(facts[-1]['quote'][:80] if facts else '—')}",
                   'need': (r['evidence'] or '—')[:160], 'breakpoint': '来信后无成单；公司底数未查，不知对方身份/体量',
                   'saga_now': {'p1': '—', 'tier': 25, 'price': '他见过的实报：见 facts / S邮箱_报价史；同款信稿只能写现价'},
                   'next_move': {'when': '待公司底数', 'channel': 'email', 'action': '先查公司底数（新入库即查）再按上次话题续谈', 'one_question': ''}}


def ensure_card(code, r, ents, dossier):
    """无研究档的 C 户（从未调研）→ 以回信证据建最小研究档（U128：定级前必须有档；公司底数走「新入库即查」）。"""
    p = os.path.join(RESEARCH, code + '.json')
    if os.path.exists(p):
        return False
    e = ents[code]
    d = dossier.get(code) or {}
    facts = []
    for m in d.get('msgs') or []:
        if m['cls'] == 'auto':
            continue
        facts.append({'date': m['date'], 'dir': '来', 'who': m['from'], 'quote': (m['subj'] + '｜' + m['excerpt'])[:300], 'why': f"{ {'S': 'S 邮箱', 'A': 'Alan 邮箱', 'E': 'Elsa 邮箱'}.get(m['box'], m['box']) } 真人来信（{m['cls']}）", 'k': m['k']})
    for t in d.get('tbl_replies') or []:
        facts.append({'date': t['date'], 'dir': 'Simon', 'who': '用户表（Simon 跟进记录）', 'quote': f"推「{t['content']}」→ 对方「{t['reply']}」", 'why': f"表内客户回复（{t['kind']}）", 'k': 'Clients/ 表格'})
    card = {'code': code, 'name_official': e.get('name') or '', 'researched_at': DATE, 'website_status': '待快照',
            'summary': f"{e.get('country') or ''}客户（{', '.join((e.get('domains') or [])[:1]) or '无域名'}）：{BATCH} 以回信证据建档——{r['reason'] or r['why_not']}。公司底数未查（新入库即查排队）。",
            'type': '', 'size': '', 'brands_seen': [], 'evidence': [{'kind': '邮箱来信/用户表', 'claim': f['quote'][:120], 'quote': f['quote'], 'url': f.get('k', ''), 'date': f['date']} for f in facts[:6]],
            'kp': [], 'notes': f'（{BATCH} 建档：仅回信证据，无首轮调研；公司底数待查）', 'deep': {'done_at': DATE, 'level': f'{BATCH} 回信建档'},
            'saga_fit': {'p1': None, 'tier': 25, 'why': '待调研后给对位机型'},
            'mail_review': {'as_of': DATE, 'facts': facts,
                            'binding': {'level': '轻度触达（有来信/表内回复，见 facts；无成单）', 'note': f'{BATCH} 建档'},
                            'situation': f"{e.get('country') or ''}；{(facts[-1]['date'] if facts else '')} 最后一次来信/回复：{(facts[-1]['quote'][:80] if facts else '—')}",
                            'need': (r['evidence'] or '—')[:160], 'breakpoint': '来信后无成单；公司底数未查，不知对方身份/体量',
                            'saga_now': {'p1': '—', 'tier': 25, 'price': '他见过的实报：见 facts / S邮箱_报价史；同款信稿只能写现价'},
                            'next_move': {'when': '待公司底数', 'channel': 'email', 'action': '先查公司底数（新入库即查）再按上次话题续谈', 'one_question': ''}}}
    json.dump(card, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return True


def main():
    rows = json.load(open(os.path.join(SD, f'A类终评_{DATE}.json'), encoding='utf-8'))
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    dossier = json.load(open(os.path.join(SD, f'回信档案_{DATE}.json'), encoding='utf-8'))
    manual = set()
    if os.path.exists(os.path.join(SD, '人工定级.csv')):
        for r in csv.DictReader(open(os.path.join(SD, '人工定级.csv'), encoding='utf-8-sig')):
            manual.add((r.get('档案编号') or r.get('编号') or list(r.values())[0] or '').strip())
    sieve_mod = load_sieve_mod()
    sv = sieve_mod.load_sieve()
    cnt = Counter()
    log_rows = []
    for r in rows:
        c = r['code']
        touch = r['target'] != r['grade_now'] or bool(r['tier'])
        if not touch:
            continue
        p = os.path.join(RESEARCH, c + '.json')
        if ensure_card(c, r, ents, dossier):
            cnt['new_card'] += 1
        rs = json.load(open(p, encoding='utf-8'))
        if r['target'] in ('A', 'B') and not rs.get('mail_review'):
            _f, rs['mail_review'] = build_mail_review(ents[c], r, dossier.get(c) or {})
            cnt['mail_review_added'] += 1
        rs['ab_final'] = {'date': DATE, 'batch': BATCH, 'tier': r['tier'], 'target': r['target'], 'grade_before': r['grade_now'], 'reason': r['reason'], 'why_not': r['why_not'], 'excl': r['excl'], 'deal': r['deal'], 'reply_class': r['reply_class'], 'evidence': r['evidence'][:400]}
        if c in manual:
            cnt['manual_skip'] += 1
            json.dump(rs, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            continue
        if r['target'] == 'A':
            reason = f"{BATCH} {DATE} A 级终评（Simon 规则：成单 + 回信沟通 + 极贴合）{r['tier']}：{r['reason']}"
            to = 'A'
        elif r['target'] == 'B' and r['grade_now'] in ('A', 'C'):
            reason = f"{BATCH} {DATE} A 级终评：{'降 B' if r['grade_now'] == 'A' else 'C 捞出 → B（U128 ②）'}：{r['why_not']}"
            to = 'B'
        else:
            continue
        hist = rs.setdefault('override_history', [])
        if not any(h.get('batch') == BATCH for h in hist):
            hist.append({'batch': BATCH, 'date': DATE, 'from_override': rs.get('grade_override'), 'to': to, 'prev_reason': rs.get('override_reason') or '', 'reason': reason})
        if rs.get('grade_override') != to or rs.get('override_reason') != reason:
            rs['grade_override'] = to
            rs['override_reason'] = reason
        json.dump(rs, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        if r['grade_now'] == 'C' and to in ('A', 'B'):
            row = sv.get(c)
            if row and row.get('verdict') != 'pool':
                row['lt_prev_verdict'] = row.get('verdict')
                row['lt_prev_batch'] = row.get('batch')
                row['verdict'] = 'pool'
                row['batch'] = BATCH
                row['reason'] = f'A 级终评捞出（{BATCH}）→ {to}：' + (r['reason'] or r['why_not']) + '｜原：' + (row.get('reason') or '')
                row['date'] = DATE
        cnt[f"{r['grade_now']}→{to}"] += 1
        if r['target'] != r['grade_now']:
            log_rows.append([c, r['name'], r['country'], r['grade_now'], to, BATCH, DATE, (r['reason'] or r['why_not'])[:200]])
    sieve_mod.save_sieve(sv)
    have = set()
    if os.path.exists(LOG):
        have = {(x['编号'], x['批次']) for x in csv.DictReader(open(LOG, encoding='utf-8-sig'))}
    new = [x for x in log_rows if (x[0], x[5]) not in have]
    with open(LOG, 'a', encoding='utf-8-sig', newline='') as f:
        csv.writer(f).writerows(new)
    print(BATCH, dict(cnt), 'log +', len(new))


if __name__ == '__main__':
    main()
