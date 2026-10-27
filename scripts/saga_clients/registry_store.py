#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T29-U64 · 第 82 批 · 公司底数（官方工商 / 年报登记）存储：data/saga_clients/registry/<country>_<date>.json

一户一条：
  put(code, name=, iso=, source=, url=, number=, status=, incorporated=, company_type=, sic=[], address=,
      accounts=, accounts_due=, size_band=, officers=[], psc=, charges=, prev_names=[], lines=[], notes=, fetched=)
render.py 的 fmt_registry() 读全部 registry/*.json 渲染「公司底数」。手工录入来自 fetch_page 的页面原文，禁止猜。
"""
import datetime as dt
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA  # noqa: E402

REG_DIR = os.path.join(DATA, 'registry')
TODAY = dt.date.today().isoformat()
FILE = os.path.join(REG_DIR, f'gb_companies_house_{TODAY}.json')

SRC_GB = 'UK Companies House（find-and-update.company-information.service.gov.uk，免费官方登记）'


def load(path=FILE):
    if os.path.exists(path):
        return json.load(open(path, encoding='utf-8'))
    return {'_meta': {'kind': 'registry', 'source': SRC_GB, 'created': TODAY}, 'rows': {}}


def save(d, path=FILE):
    os.makedirs(REG_DIR, exist_ok=True)
    d['_meta']['updated'] = TODAY
    d['_meta']['count'] = len(d['rows'])
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def put(code, **kw):
    d = load()
    row = d['rows'].get(code, {})
    row.update({k: v for k, v in kw.items()})
    row.setdefault('fetched', TODAY)
    row['code'] = code
    d['rows'][code] = row
    save(d)
    return row


def load_all():
    """{code: row}，合并 registry/*.json（将来多个国家）。"""
    out = {}
    for p in sorted(glob.glob(os.path.join(REG_DIR, '*.json'))):
        d = json.load(open(p, encoding='utf-8'))
        for c, r in (d.get('rows') or {}).items():
            r = dict(r)
            r['_src'] = d.get('_meta', {}).get('source', '')
            out[c] = r
    return out


if __name__ == '__main__':
    print(json.dumps(load_all(), ensure_ascii=False, indent=1)[:3000])
