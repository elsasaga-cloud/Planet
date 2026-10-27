#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 82 批（T29-U64）：把 Companies House 核出来的「来信人 = 董事」写回 research/<code>.json 的 kp[].role / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 82 批 Companies House 核实 2026-10-27）'
UPD = {
    'SB-474': {'kp_match': 'andys@case.uk.com', 'role': 'Director / 老板 —— Andrew Thomas Saoulis，唯一在任董事，2000 年创办，1950 年生' + TAG, 'name': 'Andy（Andrew Thomas Saoulis）',
               'facts': {'legal_name': 'CASE COMMUNICATIONS LIMITED（Companies House 03913540，2000-01-26 成立；前名 Case Technology Central Europe Ltd）', 'founded': '2000-01-26（品牌沿用 1970 年老 Case Communications / Dowty，老公司 00730286 已于 2019 注销）'}},
    'SA-007': {'kp_match': 'info@gogreenit.net', 'role': 'Director（2021-06-04 起在册董事，与创始人 Kathryn Sterling 共两名董事）；PI 单据联系人' + TAG, 'name': 'Chris Clemson（Christopher Bruce Athelstan Clemson）',
               'facts': {'legal_name': 'GO GREEN IT LTD（Companies House 07614771，2011-04-26 成立，Active；SIC 62020）'}},
    'SA-017': {'kp_match': 'jeff.ferrier@', 'role': 'Founder / 唯一董事（Companies House 10314407，2016-08-05 起；1965 年生）' + TAG, 'name': None, 'facts': {}},
    'SA-015': {'kp_match': None, 'add_kp': {'name': 'Omar Ismat Miqdadi', 'role': '唯一在任董事（2003-11 起）—— 实际拍板人；邮箱待核（现有入口 info@ / sales@）' + TAG, 'email': '', 'phone': '', 'source': 'https://find-and-update.company-information.service.gov.uk/company/04748999/officers'},
               'facts': {'legal_name': 'MEGNET LTD.（Companies House 04748999，2003-04-30 成立，Active；SIC 82990；2021-06 有 1 项抵押登记）'}},
    'SB-160': {'kp_match': 'hussain.alqahtani@', 'role': 'Purchasing and Product Development Manager（邮件签名）；**非董事**，拍板人是唯一董事 Mohamed Abdelhamid Okba（法国籍，2011-07 起）' + TAG, 'name': None,
               'facts': {'hq': '50 Woodgate, Leicester LE3 5GF（Companies House 注册地 2026-10；研究档旧址 3 Oakland Road 为经营地 / 旧址）', 'other': 'SIC 26309 / 27310 / 27320 全为制造类；前董事 Wadii Kherfani（2011–2018）现为 SB-905 Teltronix / Briticom 董事' + TAG}},
    'SB-905': {'kp_match': 'wadii@teltronix.net', 'role': 'Director / 老板 —— Teltronix Holdings Ltd 两名董事之一（另一位 Anna Kherfani，同姓）；2011–2018 曾任 Linxcom Ltd（SB-160）董事' + TAG, 'name': 'Wadii Kherfani', 'facts': {}},
    'SB-767': {'kp_match': 'info@itmsystems.net', 'role': '「Steve」（用户表）—— Companies House 在任董事为 Inneh Emmanuel Aig-Imoru（2012 起）与 Dr Stanislas Bael Nyokas-Mountsambote（创始人，2024-11 回任）；Steve ≈ Stan 待核' + TAG, 'name': None,
               'facts': {'legal_name': 'ITM SYSTEMS LIMITED（Companies House 07747218，2011-08-22 成立，Active；SIC 26110 / 62020 / 63110 / 80200；有抵押登记）'}},
    'SB-118': {'kp_match': 'mike@genrov.com', 'role': 'Director / 唯一股东（Companies House 06899120 Active，2009-05-07 成立，SIC 74909，无抵押）' + TAG, 'name': None, 'facts': {}},
    'SB-176': {'kp_match': None, 'facts': {'legal_name': 'OKSA AUTOMATION LIMITED（Companies House 13062295，2020-12-04 成立，Active）', 'founded': '2020-12-04'}},
}
for code, u in UPD.items():
    p = os.path.join(RESEARCH_DIR, f'{code}.json')
    d = json.load(open(p, encoding='utf-8'))
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if TAG not in (k.get('role') or '') and TAG not in (k.get('title') or ''):
                    key = 'role' if 'role' in k or 'title' not in k else 'title'
                    k[key] = u['role']
                if u.get('name'):
                    k['name'] = u['name']
    if u.get('add_kp') and not any(TAG in (k.get('role') or '') for k in kps):
        kps.append(u['add_kp'])
    d['kp'] = kps
    cf = d.get('company_facts') or {}
    for fk, fv in (u.get('facts') or {}).items():
        if TAG not in str(cf.get(fk, '')) and fv:
            cf[fk] = fv if fk != 'other' or not cf.get('other') else (cf['other'] + '；' + fv)
    d['company_facts'] = cf
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(code, 'ok')
