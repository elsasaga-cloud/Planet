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

# 一国一文件：registry/<key>_<date>.json；key 决定来源说明
SOURCES = {
    'gb': ('gb_companies_house', 'UK Companies House（find-and-update.company-information.service.gov.uk，免费官方登记）'),
    'fr': ('fr_sirene', "France · API Recherche d'entreprises（recherche-entreprises.api.gouv.fr：INSEE SIRENE + RNE + 年报，官方免费）"),
    'pl': ('pl_krs', 'Poland · KRS 官方 API（api-krs.ms.gov.pl）+ 财政部 VAT 白名单 API（wl-api.mf.gov.pl）'),
    'cz': ('cz_ares', 'Czechia · ARES 官方 API（ares.gov.cz）+ or.justice.cz 商业登记'),
    'de': ('de_register', 'Germany · Handelsregister / Northdata（登记摘要）'),
    'ru': ('ru_egrul', 'Russia · ЕГРЮЛ / Росстат 公开数据（rusprofile / list-org 镜像）'),
    'in': ('in_mca', 'India · MCA 公司登记（Zauba Corp / Tofler 镜像）'),
    'au': ('au_abr', 'Australia · ABN Lookup（abr.business.gov.au，官方）'),
    'us': ('us_sos', 'USA · 州务卿登记 / OpenCorporates'),
    'tr': ('tr_ticaret', 'Turkey · Ticaret Sicil / MERSIS（公开可得部分）'),
    'it': ('it_registro', 'Italy · Registro Imprese 公开摘要'),
    'lt': ('lt_rekvizitai', 'Lithuania · Registrų centras / Sodra 公开数据（rekvizitai.vz.lt）'),
    'se': ('se_bolagsverket', 'Sverige · Bolagsverket 登记镜像（allabolag / rating.se / hitta）'),
    'bg': ('bg_tr_registry', 'България · Търговски регистър（papagal.bg 镜像）'),
    'gr': ('gr_gemi', 'Ελλάδα · ΓΕΜΗ / 公开名录'),
    'ca': ('ca_corporations', 'Canada · Corporations Canada / Ontario 登记（OpenCorporates 摘要）'),
    'cy': ('cy_registrar', 'Κύπρος · Registrar of Companies（OpenCorporates 摘要）'),
    'tw': ('tw_moea', '台灣 · 經濟部商工登記 / 名錄摘要'),
    'kr': ('kr_registry', '대한민국 · 사업자등록 / 名錄摘要（DART 僅上市）'),
    'il': ('il_registrar', 'ישראל · רשם החברות（名錄摘要）'),
    'other': ('other_registry', '其他国家官方 / 准官方登记'),
}


def path_for(key='gb', date=TODAY):
    stem, _ = SOURCES.get(key, SOURCES['other'])
    # 同 key 已有文件（任意日期）则续写同一文件，避免一国多文件
    ex = sorted(glob.glob(os.path.join(REG_DIR, f'{stem}_*.json')))
    return ex[-1] if ex else os.path.join(REG_DIR, f'{stem}_{date}.json')


FILE = path_for('gb')
SRC_GB = SOURCES['gb'][1]


def load(path=None, key='gb'):
    path = path or path_for(key)
    if os.path.exists(path):
        return json.load(open(path, encoding='utf-8'))
    return {'_meta': {'kind': 'registry', 'source': SOURCES.get(key, SOURCES['other'])[1], 'created': TODAY}, 'rows': {}}


def save(d, path=None, key='gb'):
    path = path or path_for(key)
    os.makedirs(REG_DIR, exist_ok=True)
    d['_meta']['updated'] = TODAY
    d['_meta']['count'] = len(d['rows'])
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def put(code, key='gb', **kw):
    """key = 国家文件键（gb / fr / pl / cz / de / ru / in / au / us / tr / it / lt / other）。"""
    path = path_for(key)
    d = load(path, key)
    row = d['rows'].get(code, {})
    row.update({k: v for k, v in kw.items()})
    row.setdefault('fetched', TODAY)
    row['code'] = code
    d['rows'][code] = row
    save(d, path, key)
    return row


def load_all():
    """{code: row}，合并 registry/*.json（多个国家）。"""
    out = {}
    for p in sorted(glob.glob(os.path.join(REG_DIR, '*.json'))):
        d = json.load(open(p, encoding='utf-8'))
        for c, r in (d.get('rows') or {}).items():
            r = dict(r)
            r['_src'] = d.get('_meta', {}).get('source', '')
            out[c] = r
    return out


if __name__ == '__main__':
    rows = load_all()
    print(len(rows), sorted(rows))
