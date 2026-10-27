# -*- coding: utf-8 -*-
"""External Clients 第 2 步研究卡存取：data/external_clients/research/<code>.json
字段（与 Saga research 同名者同义；多出的为外部库专用）：
  code, name, round, researched_at, alive, summary, type_final, size, brands_seen[], saga_line, fit,
  evidence[{kind, claim, quote, url, date}], contacts{email, email_status, kp[{name, role, source}]},
  touch_status, saga_overlap, grade_final(A|B|C), grade_reason_final,
  next_move{action(第二封|首触|不动|并线|等回), angle, model, price, window, when},
  draft_en{subject, body} | None, deep(bool), notes
用法：from research_store import put, get, all_cards
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import DATA

RDIR = os.path.join(DATA, 'research')
REQUIRED = ('code', 'name', 'round', 'researched_at', 'alive', 'summary', 'type_final', 'saga_line', 'evidence',
            'touch_status', 'grade_final', 'grade_reason_final', 'next_move')


def put(card):
    for k in REQUIRED:
        assert k in card and card[k] not in (None, ''), f"{card.get('code')}: 缺 {k}"
    assert card['grade_final'] in ('A', 'B', 'C'), card['code']
    nm = card['next_move']
    assert nm.get('action') in ('第二封', '首触', '不动', '并线', '等回'), card['code']
    if nm.get('action') in ('第二封', '首触'):
        assert card.get('draft_en') and card['draft_en'].get('subject') and card['draft_en'].get('body'), f"{card['code']}: 要发就要有稿"
        assert 'Re:' not in card['draft_en']['subject'], card['code']
        body = card['draft_en']['body']
        bad = [w for w in ('list price', 'in stock', 'free sample', 'trading company', 'OEM Factory', 'NDAA', 'general agent', 'Re:') if w.lower() in body.lower()]
        if re.search(r'\bUL\b', body):
            bad.append('UL')
        assert not bad, f"{card['code']}: 稿里有禁词 {bad}"
    for e in card['evidence']:
        for k in ('kind', 'claim', 'url', 'date'):
            assert k in e, f"{card['code']}: 证据缺 {k}"
    card.setdefault('deep', False)
    card.setdefault('draft_en', None)
    card.setdefault('notes', '')
    card.setdefault('contacts', {})
    card.setdefault('saga_overlap', '无')
    os.makedirs(RDIR, exist_ok=True)
    with open(os.path.join(RDIR, card['code'] + '.json'), 'w', encoding='utf-8') as f:
        json.dump(card, f, ensure_ascii=False, indent=1)
    return card['code']


def get(code):
    p = os.path.join(RDIR, code + '.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None


def all_cards():
    out = {}
    if not os.path.isdir(RDIR):
        return out
    for fn in sorted(os.listdir(RDIR)):
        if fn.endswith('.json'):
            c = json.load(open(os.path.join(RDIR, fn), encoding='utf-8'))
            out[c['code']] = c
    return out
