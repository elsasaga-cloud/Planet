#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 83 批（T29-U65）：把各国官方登记核出来的「老板 / 董事 / 规模 / 财务」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 83 批 官方登记核实 2026-10-27）'
UPD = {
    'SA-011': {'add_kp': {'name': 'Carmine Oliva', 'role': 'Président de SAS（法定代表，1942 年生）—— 法国实体 CXR Anderson Jacobson 唯一登记高管' + TAG, 'email': '', 'phone': '', 'source': 'https://annuaire-entreprises.data.gouv.fr/entreprise/785754706'},
               'facts': {'legal_name': 'CXR ANDERSON JACOBSON SAS（SIREN 785754706，1983-04-10 成立，Active；NAF 26.30Z 通信设备制造；员工档 20–49）', 'staff': '20–49（INSEE 2024 员工档 12）' + TAG, 'other': '2025 年报净利 −57,478 €；历史 5 个机构仅剩 Abondant 总部' + TAG}},
    'SA-023': {'add_kp': {'name': 'Piotr Frydel / Jarosław Cisowski / Krzysztof Smugowski / A. J. Frydel', 'role': '管理委员会 4 名成员 = 4 名各 25% 股东（KRS 0001095976）；任一人可单独签 ≤100,000 PLN，超过需两人联签' + TAG, 'email': '', 'phone': '', 'source': 'https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/0001095976?rejestr=P&format=json'},
               'facts': {'legal_name': 'FCNET SP. Z O.O.（KRS 0001095976 · NIP 7542916466 · REGON 160150149；2007 起民事合伙，2023-12 转有限公司，2024-03 入 KRS；PKD 46.52.Z 批发；资本 100,000 PLN）'}},
    'SA-089': {'add_kp': {'name': 'Zdeněk Zíta / Tomáš Jahoda', 'role': '两名执行董事（jednatel），2007-07-16 起未变，各自可单独代表公司' + TAG, 'email': '', 'phone': '', 'source': 'https://ares.gov.cz/ekonomicke-subjekty/27929795'},
               'facts': {'legal_name': 'LANCOMAT s.r.o.（IČO 27929795 · DIČ CZ27929795 · 卷宗 C 127222/MSPH；2007-07-16 成立；资本 200,000 CZK；NACE 46 / 47 / 47.99）'}},
    'SA-008': {'kp_match': 'f.kriewitz@', 'role': 'Systems Engineer / 网络负责人（成单联系人）；**非合伙人**——NYNEX satellite OHG（Amtsgericht Darmstadt HRA 84829）两名无限责任合伙人为创始人 Gunter Frank / Andreas Buxbaum' + TAG, 'name': None,
               'facts': {'registry_de': 'Amtsgericht Darmstadt HRA 84829（OHG，2012-11-27 登记）；商标 GigManiac / HOME SPEED HOME / skyZIP / GigCity；关联 NYNEX space GmbH' + TAG}},
    'SA-057': {'kp_match': 'sales@born-spb.ru', 'role': 'Генеральный директор / 唯一创始人（ЕГРЮЛ）；公司 9 人、2025 营收 2.94 亿 ₽、毛利率 0.6%、2026 年两起供货仲裁被告、56 份有效 EAC 声明、2026-04 注册商标 VIGILIX' + TAG, 'name': None,
               'facts': {'staff': '9（ФНС 平均人数）' + TAG, 'other': 'ФНС 2025：营收 294.0M ₽ / 净利 1.47M ₽；223-ФЗ 政府采购 7 单（核安保 / 核物理研究所客户）' + TAG}},
    'SA-073': {'add_kp': {'name': 'Rajesh Kumar Bhutoria', 'role': 'Director 兼股东（DIN 00516745，1995 创立至今）= 老板；另一董事 Praloy Shankar Chowdhury（2013 起）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.tofler.in/vicom-security-private-limited/company/U51109WB1995PTC070096'},
               'facts': {'legal_name': 'VICOM SECURITY PRIVATE LIMITED（CIN U51109WB1995PTC070096，1995-03-28，Active；实缴 ₹20 lakh；前名 Dinesh Enterprises Pvt. Ltd.；最近 AGM 2025-09-29）'}},
    'SA-024': {'kp_match': 'sales@cabledistribution.com.au', 'role': '创始人 Ross Wasserman（The Wasserman Family Trust 2000 年起经营商号 CDS）；2025-08 起商号登记在 Damita Investments Pty Ltd（ABN 99 125 638 548）名下' + TAG, 'name': 'Ross Wasserman（官网「Ross W.」）',
               'facts': {'legal_name': 'Cable Distribution Services = 商号；法人 Damita Investments Pty Ltd（ABN 99 125 638 548，2025-08-06 起）/ 原 The Trustee for The Wasserman Family Trust（ABN 20 634 509 214，2000-05-31 起）' + TAG}},
    'SA-070': {'kp_match': None, 'facts': {'legal_name': 'TOP ITALIA S.R.L.（P.IVA 04592850871 · REA CT-306496；2008-05-08 成立；资本 €110,000；ATECO 46.47.3；PEC topit@pec.top-srl.com；SDI T04ZHR3）', 'staff': '5–6（2026）' + TAG, 'other': '营收 2023 €2.7M → 2024 €2.17M → 2025 €1.72M；净利 2025 €11,477' + TAG}},
    'SA-019': {'kp_match': None, 'facts': {'legal_name': 'ALLNET GmbH Computersysteme（Amtsgericht München HRB 95992，1991-08-14；LEI 5299008GWAOUQEZ8HJ12）', 'other': '2024 营收 €243.2M、资产 €117.6M（Bundesanzeiger）；股东 Alldis Computersystem GmbH / Allnet Schweiz AG / SAS Allnet France；唯一 GF Wolfgang Marcus Bauer' + TAG}},
    'SA-082': {'kp_match': None, 'facts': {'other': 'Northdata：HRB 472 Cottbus 1990-09-28 登记；GF Ralph-Peter Hannemann（2005 起，= 自建站询盘人）+ Diego Noack（2014 起）；Prokura Falk Noack；Hannemann & Noack 两家族控股；2024 资产 €5.76M、毛利 €8.0M；曾用名 Fleischhauer Cottbus GmbH' + TAG}},
    'SA-088': {'kp_match': None, 'facts': {'legal_name': 'U.T.E. Electronic GmbH & Co. KG（Amtsgericht Bochum HRA 4773，1997-04-11；PhG U.T.E. Electronic Verwaltungs-GmbH；有限合伙人 269 M Ltd.（UK））', 'other': '2024 资产总额 €1.28M（仅公告资产负债表）；商标 6swaps（2007）' + TAG}},
    'SA-050': {'add_kp': {'name': 'Marcin Chojnacki', 'role': 'Prezes Zarządu（董事长 / CEO）—— 只签框架；日常对接 product@ 的产品经理' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/585900/impakt'},
               'facts': {'legal_name': 'IMPAKT S.A.（KRS 0000585900 · NIP 7831720485 · REGON 360441981；2015-11-13；资本 60,761,002 PLN 实缴）', 'other': '2025 营收 152.2M PLN、净利 8.6M PLN、资产 87.2M PLN；品牌 Genesis / Lanberg / Natec' + TAG}},
    'SA-020': {'add_kp': {'name': 'Dariusz Pietrzyk', 'role': 'Prezes Zarządu（从 Sp. z o.o. 时代起的当家人）' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/1010572/bitstream'},
               'facts': {'legal_name': 'BITSTREAM S.A.（KRS 0001010572，2023-01-02 由 Sp. z o.o. KRS 0000266288 转制；NIP 9462508588；资本 200,000 PLN；PKD 26.30.Z 通信设备制造）', 'other': '最近年报营业收入 18.24M PLN、总成本 14.29M PLN；2026-08-18 监事会变更' + TAG}},
    'SA-064': {'kp_match': None, 'facts': {'staff': '1（ФНС 平均人数）' + TAG, 'other': 'ЕГРЮЛ：Елизаров Н.Н. 100% 股东兼总经理（2012-08-15 起）；2025 营收 21.8M ₽、净利 1.2M ₽；25 次投标；仲裁 9 件、执行程序 3–15 件' + TAG}},
    'SA-037': {'add_kp': {'name': 'Devendra Jagdishprasad Sharma', 'role': 'Founder / CEO / Director（DIN 09626912）= 老板；儿子 Ashutosh Sharma（Director，MCA 登记邮箱 ashu.ent@gmail.com）管日常；配偶 Ritu Sharma 挂名董事；Mandar Joshi 2023 加入' + TAG, 'email': '', 'phone': '', 'source': 'https://www.falconebiz.com/company/AECONNECT-INDIA-PRIVATE-LIMITED-U31200GJ2022PTC132573'},
               'facts': {'legal_name': 'AECONNECT INDIA PRIVATE LIMITED（CIN U31200GJ2022PTC132573，2022-06-01，Active；实缴 ₹100,000；RoC Ahmedabad）'}},
    'SA-086': {'kp_match': None, 'facts': {'ownership': 'ZTE Cooperatief U.A. 48.05% + TSKGV（土耳其武装部队强化基金会）15.00% + 公众 36.95%（2025-09 季报）' + TAG, 'other': 'KAP：营收 2024 91.8 亿 TL / 2025 前三季 83.6 亿 TL；净亏 2024 −2.72 亿、2025 全年 −3.41 亿 TL；两年未分红' + TAG}},
    'SA-063': {'add_kp': {'name': 'Rashmi Jain', 'role': 'Director 兼股东（DIN 01336337，2018-03-20 起）= 现任实控人；2026-04-24 新增董事 Nilesh Bastimal Jain；Gutta Venkata Kumari（2015 起）2026 名单疑已卸任' + TAG, 'email': '', 'phone': '', 'source': 'https://www.falconebiz.com/company/ARECA-EMBEDDED-SYSTEMS-PRIVATE-LIMITED-U72200TG2007PTC053397'},
               'facts': {'legal_name': 'ARECA EMBEDDED SYSTEMS PRIVATE LIMITED（CIN U72200TG2007PTC053397，2007-03-29，Active；实缴 ₹46,522,500；RoC Hyderabad；2018 年易主 Jain 家族）'}},
    'SA-077': {'kp_match': None, 'facts': {'legal_name': 'ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİCARET SANAYİ A.Ş.（2016-11-28 设立；NACE 62.09.02；登记地 Alacaatlı Mah. Park Cad. 47/31 Yenimahalle, Ankara）' + TAG}},
    'SA-002': {'kp_match': 'frank@simrex.com', 'role': 'General Manager；SAM.gov 登记联系人（CAGE 1WEC8 / DUNS 087787573，Delaware 公司，S-Corp，Woman Owned Business，业务始于 1996-01-18，SAM 续期至 2027-05-04）' + TAG, 'name': None,
               'facts': {'legal_name': 'SIMREX CORPORATION（Delaware 注册，纽约 Buffalo 经营；CAGE 1WEC8；SAM 分类 U.S. manufacturer；Woman Owned）' + TAG}},
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
