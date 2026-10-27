#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 84 批（T29-U66，公司底数第二轮）：把各国官方 / 准官方登记核出来的「老板 / 董事 / 规模 / 财务」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=84 行）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 84 批 官方登记核实 2026-10-27）'
UPD = {
    # ---------- US ----------
    'SA-021': {'kp_match': 'sales@optiviewusa.com', 'role': 'President（BBB 登记管理层）= 老板；Optiview 为 Florida 公司（2000-01-21 注册），另用 5 个零售别名 + 经销商门户' + TAG, 'name': None,
               'facts': {'legal_name': 'OPTIVIEW, INC.（Florida corporation，2000-01-21；BBB 档：Alternate Business Names 5 个零售品牌）' + TAG}},
    'SA-042': {'kp_match': 'jimtaxdahl@', 'role': 'VP Sales（非买方、非股东）；Antronix 为 NJ 公司（1980-03-12），Tang 家族持有：Danny Tang（2016 年故）→ 子 Neil Tang CEO/CTO；2018 与 Teleste 合资' + TAG, 'name': None,
               'facts': {'legal_name': 'ANTRONIX, INC.（New Jersey，1980-03-12；Cranbury NJ；家族持有）', 'staff': '30–34（Cranbury）' + TAG}},
    'SA-022': {'kp_match': 'matt@addoncomputer.com', 'role': 'CEO（经营者，非所有者）；AddOn Networks = ADD-ON COMPUTER PERIPHERALS, LLC（California LLC 2002-12-26，前身 Inc. 2000），Patton 家族所有（President Jimmy Patton）；NY OGS 合同 PM69867；EIN 05-0549009' + TAG, 'name': None,
               'facts': {'legal_name': 'ADD-ON COMPUTER PERIPHERALS, LLC（dba AddOn Networks；California LLC，2002-12-26）', 'staff': '201–500；营收估 ~$61.8M（第三方）' + TAG}},
    'SA-018': {'kp_match': None, 'name': None,
               'add_kp': {'name': 'Preston Wily', 'role': 'President（Utah 登记；Owner David Sewell 为登记代理人 = 研究档 KP）；Sewell Development Corp 1034201-0142，1989-05-11；CAGE 38UZ7（2021 过期）' + TAG, 'email': '', 'phone': '', 'source': 'https://opencorporates.com/companies/us_ut/1034201-0142'},
               'facts': {'legal_name': 'SEWELL DEVELOPMENT CORPORATION（Utah 1034201-0142，1989-05-11）', 'staff': '营收估 $6.5–11M（第三方区间）' + TAG}},
    'SA-006': {'kp_match': 'thupvilink16@', 'role': 'Owner（商会名录 / D&B 联系人 / 2018 OCTA 投标联系人）= 老板 = 联系人；公司已收缩至微型（Brea 关店、D&B 1 人），现址 450 Goddard Irvine' + TAG, 'name': None,
               'facts': {'legal_name': 'VILINK COMMUNICATIONS, INC.（California，1993；Self-Owned）', 'staff': '1–数人（D&B 1 人；第三方营收估值不可信）' + TAG}},
    'SA-059': {'add_kp': {'name': 'Barry G. Patton', 'role': 'Founder / President & CEO / Resident Agent（1989 至今）= 老板；Patton Electronics 创始人家族的兄弟；SCADA 线销售 Michael Spellerberg、SMB 线 Daniel Rowe' + TAG, 'email': '', 'phone': '', 'source': 'https://govtribe.com/vendors/data-connect-enterprise-inc-dot-0mr56'},
               'facts': {'legal_name': 'DATA CONNECT ENTERPRISE, INC.（Maryland Subchapter S Corp，1989-01-13；SAM.gov 在册至 2026-08-29；DLA 供应商）', 'staff': '13–19' + TAG}},
    'SA-044': {'kp_match': 'sales@dymec.com', 'role': 'President（Sales & Engineering，两项交通组网专利）= 拍板人；**同时是 SA-033 BlueWARRIOR 的联系人**；法人 Kyland-USA, LLC（dba DYMEC，VOSB 退伍军人小企业，2015-02 收购 DYMEC 品牌、2015-12 统一更名）' + TAG, 'name': None,
               'facts': {'legal_name': 'KYLAND-USA, LLC dba DYMEC（原 DYMEC, Inc. 1970 年创立、2006 并入 GarrettCom；Kyland-USA 2008 前后成立）', 'staff': '4–11' + TAG}},
    'SA-033': {'kp_match': 'sales@bluewarrior.com', 'role': '= SA-044 DYMEC President Thomas West 本人 → 两户并一线；BlueWARRIOR 疑为 Kyland-USA, LLC 的第二品牌（法人待核）' + TAG, 'name': None,
               'facts': {'other': '与 SA-044 DYMEC 同团队（Blue Springs MO / Katy TX）；该团队已有东土（Kyland）+ 迈威（MISCOM）两条中国货源' + TAG}},
    'SA-046': {'kp_match': 'sales@ipcampower.com', 'role': 'Owner / Founder / 发明人 = 老板 = 联系人；2008 创 Nelly\'s Security（2023 出售）、2015 创 IPCamPower；2025 主推 UL + TAA 合规 PoE 线（Saga 做不了，信里不碰）' + TAG, 'name': None,
               'facts': {'legal_name': 'IPCamPower（Broken Arrow, OK；独资；OK SOS 实体号待补）', 'staff': '1–17（第三方）' + TAG}},
    'SA-058': {'kp_match': 'nate.cline@', 'role': 'President（2013 起）/ Yelp 店主 = 老板（第二代；创始人 Thomas J. Cline 1986 创立、2012 退休）' + TAG, 'name': None,
               'facts': {'legal_name': 'Alpha Net Communications（San Antonio TX，1986；法人形式待核）', 'staff': '2–10' + TAG}},
    # ---------- TR ----------
    'SA-085': {'kp_match': 'ctuncbilek@', 'role': '采购 / 销售经办，**非老板**；HCS 为 HES Hacılar Elektrik 集团（Kayseri）旗下 A.Ş.，董事长 Yusuf Öksüzömer；İstanbul Ticaret Sicil 12401448，LEI 7890008F3LXUBMYF0N25' + TAG, 'name': None,
               'facts': {'legal_name': 'HCS KABLOLAMA SİSTEMLERİ SANAYİ VE TİCARET A.Ş.（İstanbul Ticaret Sicil 12401448；2000-11-22；LEI 7890008F3LXUBMYF0N25）', 'staff': '51–200；Kayseri 工厂 30,000 m²' + TAG}},
    'SA-076': {'add_kp': {'name': 'Abdullah Unakıtan', 'role': 'Yönetim Kurulu Başkanı（董事长）；副主席 Fatma Unakıtan / Zeynep Basutçu Unakıtan（家族）；研究档联系人为项目经办' + TAG, 'email': '', 'phone': '', 'source': 'https://www.emis.com/php/company-profile/TR/Telemobil_Bilgi_Iletisim_Hizmetleri_AS_en_3350443.html'},
               'facts': {'legal_name': 'TELEMOBİL BİLGİ İLETİŞİM HİZMETLERİ SANAYİ VE TİCARET A.Ş.（2005-01-14；Üsküdar İstanbul；前身 A.B GRUP IT 部门）', 'staff': '50–97' + TAG}},
    'SA-084': {'kp_match': 'eds@eds.com.tr', 'role': 'Genel Müdür（总经理）= 拍板人；Gülnihal Özdemir Yılmaz = Import Export Manager（进口经办）；EDS 1990-02 成立、Sancaktepe 5,000 m² 工厂、出口 35+ 国、官方认可 R&D 中心' + TAG, 'name': None,
               'facts': {'legal_name': 'EDS ELEKTRONİK DESTEK SANAYİ VE TİCARET LTD. ŞTİ.（1990-02；İSO / İTO / TÜYAK / GESİDER / TÜBİSAD 会员）', 'staff': '57–74' + TAG}},
    'SA-047': {'kp_match': 'muratg@', 'role': 'Teknik Müdür（技术总监，2009-11 起；YTÜ 电气工程）= 技术拍板、非老板；CEO Özgür Ünver；公司 2007-11-28 成立、16 人（2025）、2024 销售额 −9.5% / 资产 +23.5%' + TAG, 'name': None,
               'facts': {'legal_name': 'SGE MÜHENDİSLİK ELEKTRİK OTOMASYON BİLGİ İŞLEM SAN. VE TİC. LTD. ŞTİ.（2007-11-28；Çekmeköy İstanbul）', 'staff': '16（EMIS 2025）' + TAG}},
    # ---------- RU ----------
    'SA-016': {'kp_match': 'info@bitbuk.ru', 'role': 'Директор + 100% учредитель（ЕГРЮЛ，2018-04-24 起）= 老板 = 一人公司；登记主业不动产出租、住宅地址；2025 营收 64 млн ₽' + TAG, 'name': 'Андрей Александрович Татарников（Andrey Tatarnikov）',
               'facts': {'legal_name': 'ООО «БИТБУК»（ОГРН 1186658033220 · ИНН 6623126845；Нижний Тагил；资本 10,000 ₽）', 'staff': '1（平均人数）' + TAG}},
    'SA-035': {'kp_match': 'air@td-fe.ru', 'role': 'Учредитель（股东之一）= 拍板人之一；总经理 2023-11-10 起为 Твердохлеб Татьяна Владимировна（签字人）；另一股东 Авраменко Е. Е.；6 人、营收 98 млн ₽；商标 TD-FE®（马德里 2019）' + TAG, 'name': None,
               'facts': {'legal_name': 'ООО «ТОРГОВЫЙ ДОМ «ФАРАДЕЙ ЭЛЕКТРОНИКС»（ОГРН 1167847053934 · ИНН 7820046904；СПб Шушары；2016-01-14）', 'staff': '6' + TAG}},
    # ---------- SE / IT / PL / CA / BG ----------
    'SA-043': {'kp_match': 'anders.hedin@', 'role': '产品 / 采购经办，非董事；Direktronik AB（556281-9663，1986）为上市集团 Lagercrantz Group 100% 子公司；外聘 VD Henrik Ringstedt、董事长 Mats Rydén；财年 3 月止 2025 营收 133.0 MSEK / 28 人' + TAG, 'name': None,
               'facts': {'legal_name': 'DIREKTRONIK AKTIEBOLAG（Org.nr 556281-9663 · VAT SE556281966301；1986-09-11；母公司 Lagercrantz Group AB）', 'staff': '28（2025）；营收 133.0 MSEK（FY 2025-03）' + TAG}},
    'SA-072': {'kp_match': 'f.brighel@', 'role': 'General Manager（Brighel 家族：President Salvatore / MD Marco / GM Francesco / 行政 Rita）= 老板家族；采购经办 Corrado Novi；2024 营收 €17.96M（−24%）、净利 €33.8k' + TAG, 'name': None,
               'facts': {'legal_name': 'TRANS AUDIO VIDEO S.R.L.（P.IVA 01675270613 · REA CE-116878；1987-06-18 成立 / 1998-01-29 登记；资本 €500,000；PEC transaudiovideo@pec.it）', 'staff': '29（2026）' + TAG}},
    'SA-041': {'kp_match': 'sales@fibermarkt.com', 'role': 'Prezes Zarządu（2026-02-17 起；此前 Magdalena Podgórska 任 Prezes，现为 Prokurent）；股东 Grzegorz Szydełko + GEMINVE（2020-08 起）；2024 亏 −705k、2025 亏 −432k PLN' + TAG, 'name': 'Krzysztof Podgórski',
               'facts': {'legal_name': 'FIBERMARKT SP. Z O.O.（KRS 0000356815 · NIP 6772343192 · REGON 121230858；2010-05-19；资本 123,700 PLN；Kraków）', 'staff': '2–10；2025 营收 1.9 mln PLN / 亏损 −431.8 tys. PLN' + TAG}},
    'SA-087': {'kp_match': 'norm@nsidistribution.com', 'role': 'Sales and Product Development / 官网唯一具名负责人（投诉、招聘、门店均指向他）= 实际经营者；Amanda Matinnia 管采购（家族）；D&B 登记负责人 Frank Bruno（Norelco 时代 President，待核）' + TAG, 'name': None,
               'facts': {'legal_name': '2164929 ONTARIO INC. o/a NSI Distribution（前 Norelco SafeCam / Norelco Telecom；Brampton ON；6 个门店）', 'staff': '23（Datanyze）/ 11–50' + TAG}},
    'SA-074': {'add_kp': {'name': 'Радка Ангелова Иванова', 'role': 'Управител（2020-03-19 起）= 签字人；股东 „ВЪЛК - 80“ ЕООД 34% / Д. Конецовска 33% / Т. Иванова 33%（2024-06-04 起，股权 4 次易手）；МВР 私人保安许可 № 288 З/02-770（2023-01-10）' + TAG, 'email': '', 'phone': '', 'source': 'https://papagal.bg/eik/202351530/4f70'},
               'facts': {'legal_name': '„ЕЛИТ - ТИМ - СЕКЮРИТИ“ ООД（ЕИК 202351530 · ДДС BG202351530；2012-12-07；Враца）' + TAG}},
    # ---------- B 档起步：GB ----------
    'SB-1121': {'kp_match': 'mark.basham@', 'role': '研究档联系人（非登记董事）；Technetix Limited 02484988（1990-03-26，Active；前 Technetix PLC）董事 Paul Antony Broadhurst（1991 年前即在任）+ Philip James Deakin（2024-01-30）；母公司 Technetix Group Ltd 05303822' + TAG, 'name': None,
                'facts': {'legal_name': 'TECHNETIX LIMITED（Companies House 02484988；SIC 26110 / 26400 / 46520；账目至 2025-12-31 已报，下期 2027-09-30 到期）' + TAG}},
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
    seen, dedup = set(), []
    for k in kps:  # SA-016 两条 info@ 同邮箱 KP 改名后重复 → 去重
        key = (k.get('name'), k.get('email'), k.get('role') or k.get('title'))
        if key in seen:
            continue
        seen.add(key); dedup.append(k)
    d['kp'] = dedup
    cf = d.get('company_facts') or {}
    for fk, fv in (u.get('facts') or {}).items():
        if TAG not in str(cf.get(fk, '')) and fv:
            cf[fk] = fv if fk != 'other' or not cf.get('other') else (cf['other'] + '；' + fv)
    d['company_facts'] = cf
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(code, 'ok')
