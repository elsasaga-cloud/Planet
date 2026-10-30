#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A 类「挖个底掉」情报库（T29-U138 2026-10-30，Simon：年报 / 领英 / KP / 人事变动 / 展会 / 论坛 / GitHub …商业世界里挂得上的都挖进仓库）。

研究档 research[code]['intel'] = {'as_of': date, 'items': [ {kind, date, quote, url, note, batch, added} ]}
kind ∈ KINDS（固定词表，便于按维度统计缺口）。幂等：同 (kind, url, quote[:60]) 不重复。
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
RESEARCH = os.path.join(ROOT, 'data', 'saga_clients', 'research')

KINDS = ['年报/财务', '登记', '领英公司页', 'KP', '人事变动', '展会/活动', '新闻/招标', 'GitHub/技术足迹', '社媒', '供应商/品牌关系', '论坛/社区', '官网变化']
# 每户至少要碰过的维度（未得也要记「查过」）
CORE = ['年报/财务', '领英公司页', 'KP', '人事变动', '展会/活动', '新闻/招标', 'GitHub/技术足迹']


def load(code):
    p = os.path.join(RESEARCH, code + '.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None


def save(code, rs):
    json.dump(rs, open(os.path.join(RESEARCH, code + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def add(code, kind, quote, url='', date='', note='', batch='', found=True, rs=None, persist=True):
    """found=False 表示该维度查过未得（记一条 kind 的「未得」，quote 写查了什么）。返回 True=新增。"""
    assert kind in KINDS, kind
    own = rs is None
    if own:
        rs = load(code)
        if rs is None:
            return False
    it = rs.setdefault('intel', {'as_of': date, 'items': []})
    key = (kind, url or '', (quote or '')[:60])
    for x in it['items']:
        if (x['kind'], x.get('url') or '', (x.get('quote') or '')[:60]) == key:
            return False
    it['items'].append({'kind': kind, 'date': date, 'quote': (quote or '')[:400], 'url': url, 'note': (note or '')[:300], 'batch': batch, 'found': bool(found), 'added': date})
    it['as_of'] = max(it.get('as_of') or '', date or '')
    if own and persist:
        save(code, rs)
    return True


def gaps(rs):
    items = ((rs or {}).get('intel') or {}).get('items') or []
    touched = {x['kind'] for x in items}
    return [k for k in CORE if k not in touched]


def stats(rs):
    items = ((rs or {}).get('intel') or {}).get('items') or []
    out = {}
    for x in items:
        out.setdefault(x['kind'], [0, 0])
        out[x['kind']][0 if x.get('found', True) else 1] += 1
    return out
