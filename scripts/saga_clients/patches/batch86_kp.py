#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 86 批（T29-U68，公司底数第四轮 · B 档欧美土俄起步）：把官方 / 准官方登记核出来的「老板 / 董事 / 规模 / 财务」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=86 行）。
结构同 batch85_kp.py；新增：UPD[code] 可为 list（同一户多条 KP 更新）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 86 批 官方登记核实 2026-10-27）'
UPD = {
    # ---------- RU ----------
    'SB-003': {'kp_match': 'rio-import2003@mail.ru', 'role': '订单邮箱 → 法人 ООО «РИО-ИМПОРТ»（ОГРН 1092468006047 · ИНН 2460214069，Красноярск 2009-02-19，资本 10,000 ₽）；现任总经理 Сергеева Н. М.，创始人 / 2012 年 100% 股东 Попов И. Ю.；营收 38 млн ₽' + TAG, 'name': None,
               'add_kp': {'name': 'Сергеева Надежда Михайловна', 'role': 'Генеральный директор（现任；companies.rbc）= 签字人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.rio-krsk.ru/company/requisites/'},
               'facts': {'legal_name': 'ООО «РИО-ИМПОРТ»（ОГРН 1092468006047 · ИНН 2460214069 · КПП 246001001；Красноярск；2009-02-19；资本 10,000 ₽；创始人 Попов Игорь Юрьевич）', 'staff': '小型；营收 38.13 млн ₽（最近一期）' + TAG}},
    'SB-163': {'kp_match': 'npa@skeo.ru', 'role': '采购 / 产品经办（非登记人员）；拍板人 = 总经理 Деркач А. А.（10% 股东，2021-11 起），实控人 = 80% 股东 Афакова Э. К.；ООО «СКЕО» 3 人、2025 营收 100.7 млн ₽（+34%）' + TAG, 'name': None,
               'add_kp': {'name': 'Деркач Алексей Александрович', 'role': 'Генеральный директор（2021-11-19 起）+ 10% 股东 = 拍板人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.companium.ru/id/1147847171185-skeo'},
               'facts': {'legal_name': 'ООО «СКЕО»（ОГРН 1147847171185 · ИНН 7810990736；СПб；2014-05-14；资本 10,000 ₽；股东 Афакова 80% / Деркач 10% / Гатина 10%）', 'staff': '3（ССЧ）；营收 2023 102.5 → 2024 75.6 → 2025 100.7 млн ₽' + TAG}},
    'SB-113': {'kp_match': 'info@regionprof.ru', 'role': 'Генеральный директор（2020-07-10 起）= 受雇总经理 / 签字人，非所有者；所有者 ООО «Прософт» 100%；84 人；2024 营收 1.73 млрд ₽ 净亏 −247.5 млн → 2025 营收 1.34 млрд ₽（−22%）净利 +118 млн' + TAG, 'name': None,
               'facts': {'legal_name': 'ООО «РЕГИОН-ПРОФ»（ОГРН 1067759114675 · ИНН 7728599583；СПб；2006-11-02；资本 30,000 ₽；唯一股东 ООО «Прософт»）', 'staff': '84（ФНС 2023）；92（2018）→ 80（2025）' + TAG}},
    # ---------- US ----------
    'SB-020': {'kp_match': 'uzair@52networks.com', 'role': 'GSA 登记联系人 = 业主（SAM.gov 自证少数族裔 / 印度裔所有，1–10 人，营收 <$1M）= 老板 = 联系人；52 Networks, Inc.（VA 2018-03-12；UEI FV4KBSNE5S75 · CAGE 907X4；GSA MAS 47QTCA22D00B3 至 2027-07）' + TAG, 'name': None,
               'facts': {'legal_name': '52 NETWORKS, INC.（Virginia，2018-03-12；UEI FV4KBSNE5S75 · CAGE 907X4；SAM 有效至 2027-06-15）', 'staff': '1–10；SAM 自报营收 $0–1M' + TAG}},
    'SB-085': {'kp_match': 'stan@thorfiber.com', 'role': 'CEO / CFO / Secretary / Director（California SOS 四职一人 = Slawomir Sochur）= 老板 = 联系人；Thor Fiber, Inc. CA 4095985（2017-12-26；业务 2011 / 2007 起）' + TAG, 'name': 'Stan (Slawomir) Sochur',
               'facts': {'legal_name': 'THOR FIBER, INC.（California SOS 4095985，2017-12-26，Good Standing；dba Thor Broadcast；Torrance CA）', 'staff': '1–10 实际（LinkedIn 51–200 不可信）；营收估 $0.4–4M 区间' + TAG}},
    'SB-826': {'kp_match': 'gmassott@versitron.com', 'role': 'Technical Sales Product Specialist（2008 起即此职；NAVAIR 名录联系人）= **非老板、非拍板人**；拍板人 = President Richard W. (Rich) Tull（cage.report / 2024–2025 新闻稿署名）' + TAG, 'name': None,
               'add_kp': {'name': 'Richard W. Tull', 'role': 'President（cage.report 现任负责人；新闻稿署名 R. W. Tull）= 老板 / 拍板人；邮箱来自 2026-03-11 OOO 自动回复（k=4ac602505b7d8db3），从未发过' + TAG, 'email': 'rwtull@versitron.com', 'phone': '', 'source': 'https://cage.report/DUNS/837605443'},
               'facts': {'legal_name': 'VERSITRON, INC.（Delaware；品牌 1958、现法人 1995-10-18；DUNS 837605443；NAVAIR OSBP 小企业供应商）', 'staff': '2–10 实际；营收 $2–5M（自报 EC21；第三方 $21–30M 不可信）' + TAG}},
    'SB-831': {'kp_match': 'pchurley@actelis.com', 'role': 'VP Sales – Strategic Accounts（卖方高管，非采购）；Actelis FY2025 营收 $3.7M（−53%）净亏 $8.3M、累计亏损 $56.2M（2026-06）、**持续经营存疑 + Nasdaq 退市通知**；采购 / 运营在以色列（34 人）' + TAG, 'name': None,
               'add_kp': {'name': 'Tuvia Barlev', 'role': 'Chairman & CEO（创始人；SEC 10-K）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.sec.gov/Archives/edgar/data/1141284/000121390026030946/ea028228701ex99-1.htm'},
               'facts': {'legal_name': 'ACTELIS NETWORKS, INC.（SEC CIK 1141284；ASNS；Delaware；Fremont / Sunnyvale CA + 以色列）', 'staff': '51 含承包商（39 全职；以色列 34 / 美国 15）；FY2025 营收 $3.7M、净亏 $8.3M；2026-H1 营收 $2.1M（+26%）' + TAG}},
    'SB-010': {'kp_match': 'sales@americanfibertek.com', 'role': 'President & Owner（2020-03 via Sunny-Z Inc. 整体收购，女性所有；公开路线「American made / 规避 foreign elements」→ 与进口中国交换机冲突）' + TAG, 'name': None,
               'facts': {'legal_name': 'AMERICAN FIBERTEK, INC.（1984 Somerset NJ；2020 迁 St. Petersburg FL；母公司 Sunny-Z Inc.）', 'staff': '7–28；营收估 $8–11M' + TAG}},
    # ---------- GB / FR ----------
    'SB-1115': {'kp_match': 'ifolayan@millievolution.com', 'role': 'Director（Companies House 16807798，2025-10-24 起；尼日利亚籍居英）= 老板之一 = 联系人；公司 **2025-10 刚注册**、虚拟地址 128 City Road、IT 咨询 SIC、零财务记录；另两位董事 Aderonke Folayan（家属）+ Andrew Oladipo' + TAG, 'name': None,
                'add_kp': {'name': 'Aderonke Folayan', 'role': 'Director（2025-10-24 起；Wakefield）= 家属 / 共同股东' + TAG, 'email': '', 'phone': '', 'source': 'https://find-and-update.company-information.service.gov.uk/company/16807798/officers'},
                'facts': {'legal_name': 'MILLISECONDS EVOLUTION LIMITED（Companies House 16807798；2025-10-24；128 City Road London EC1V 2NX（注册代理地址）；SIC 62020 / 62030 / 70229 / 85590；首份账目 2027-07-24 到期）', 'staff': '初创微型（3 董事）' + TAG}},
    'SB-910': {'kp_match': 'charles.chaussonnier@etictelecom.com', 'role': 'Directeur Général（SIRENE / RNE；1966-09 生）= 联合拍板人（另一 DG Philippe Duchesne；总裁为控股公司 ETIC FINANCES 810380733）= 联系人本人就是总经理' + TAG, 'name': None,
               'facts': {'legal_name': 'ETIC TELECOM SAS（SIREN 380927475 · SIRET 38092747500026；NAF 26.30Z；1991；Montbonnot-Saint-Martin 38330；PME）', 'staff': '20–49（员工档 12，2024）；2024 营收 €3,930,958 / 净利 €321,866' + TAG}},
    # ---------- DE ----------
    'SB-103': [{'kp_name': 'Ludwig Bergschneider', 'role': 'Geschäftsführer 2017-12-15 → **2026-09-14 卸任**（Handelsregister；2024-06 起登记名 Hans Ludwig Bergschneider）= 已非拍板人；现任 GF Kagan Kandemir（2026-09-14 起）、Prokurist Janek Brock' + TAG},
               {'kp_name': 'Yalcin Demirak', 'role': '登记网络中出现（Eschweiler；股东 / 前任职务待核）' + TAG},
               {'add_kp': {'name': 'Kagan Kandemir', 'role': 'Geschäftsführer（2026-09-14 起，Düsseldorf）= 现任唯一 GF / 拍板人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.northdata.de/Abetechs%20GmbH,%20Erkrath'},
                'facts': {'legal_name': 'Abetechs GmbH（Amtsgericht Wuppertal HRB 35197，前 Düsseldorf HRB 82264；2017-12-15；Stammkapital €800,000；3 名股东；商标 C WERK；关联 i-Alarmsysteme GmbH 奥地利）', 'staff': '11–50；资产负债表总额 €1,061,495（2025-12-31）' + TAG}}],
    'SB-205': [{'kp_match': 'rohr.rudolf@barox.ch', 'role': 'Mitgründer / Geschäftsführer（AG CEO 2005 起；GmbH 共同 GF）/ geschäftsführender Gesellschafter = 老板 = 联系人；barox Kommunikation AG 1998-09-01 Baden（CH），GmbH 2003 Lörrach（HRB 413457 Freiburg，€25,000）' + TAG},
               {'kp_match': 'mail@barox.de', 'role': 'Leiter Technik（2024-10 任命）= 技术选型人' + TAG},
               {'facts': {'legal_name': 'Barox Kommunikation GmbH（Lörrach；HRB 413457 Freiburg / Impressum HRB 3457 Lörrach；USt-ID DE228975346；100% 子公司 of barox Kommunikation AG，CH-400.3.019.774-7，Baden-Dättwil）', 'staff': '估 20–50（两国三址）' + TAG}}],
    'SB-018': {'kp_match': 'info@walker-security.systems', 'role': 'Geschäftsführer（2020-02-17 起，接替创始人 Oktay Zuki）= 老板 = 联系人；UG €6,000、7 年 5 次迁址、2025-03 更名 Walker Security Systems UG；Prokuristin Nina Jasmin Walker（配偶）' + TAG, 'name': None,
               'facts': {'legal_name': 'Walker Security Systems UG (haftungsbeschränkt)（Amtsgericht Krefeld HRB 20953；原 SMART+ Communications UG，Köln HRB 95644，2018-09-13；Nettetal）', 'staff': '微型（夫妻 2 人管理）' + TAG}},
    # ---------- IN / SK / PL / AU / TR ----------
    'SB-062': [{'kp_match': 'manan@a-ites.com', 'role': 'Director（DIN 02469366，2008-12-31 创立至今）= 老板 = 联系人；夫妻公司（Ketana Manan Bhavsar 亦为董事）；创始合伙人 2009–2016 全部退出；实缴 ₹24.64 lakh；MCA 年报镜像停在 FY23' + TAG},
               {'kp_match': 'chirag.s@a-ites.com', 'role': '非董事（注意：历任董事 Chirag Pandit Satishkumar 2009–2013 为另一人）' + TAG},
               {'facts': {'legal_name': 'AARYA ITES PRIVATE LIMITED（CIN U72900GJ2008PTC055798；2008-12-31；Ahmedabad；实缴 ₹24.64 lakh；董事 Manan + Ketana Bhavsar）' + TAG}}],
    'SB-005': {'kp_match': 'rovez@rovez.sk', 'role': '联系人（konateľ / 股东身份待 FinStat 登记页确认）；ROVEZ, s.r.o. 1997-12-22、3–4 人、2025 营收 €646,579（+28%）净利 €192,182（30%）、负债率 7%' + TAG, 'name': None,
               'facts': {'legal_name': 'ROVEZ, s.r.o.（IČO 36225801 · IČ DPH SK2020163277；ORSR Trnava Sro 10793/T；1997-12-22；základné imanie €6,639）', 'staff': '3–4（2026）；2025 营收 €646,579 / 净利 €192,182 / 权益 €586,271' + TAG}},
    'SB-038': {'kp_match': 'contact@tricomp.com.pl', 'role': 'Prezes Zarządu（59 岁）+ **98 / 100 股** = 老板 = 联系人；代表方式 = 董事 + Prokurent（Grażyna Piekus）联签' + TAG, 'name': None,
               'facts': {'legal_name': '„TRICOMP” SP. Z O.O.（KRS 0000121281 · NIP 5222477449 · REGON 016022377；2002-07-04；Warszawa Al. Prymasa Tysiąclecia 78A；资本 50,000 PLN）' + TAG}},
    'SB-936': {'kp_match': 'info@altronics.com.au', 'role': '研究档联系人（职务待核：创始家族 / 高管）；交易主体 = The Trustee for ALTRONICS UNIT TRUST（ABN 84 177 396 871，GST 2000 起），受托人 ALTRONIC DISTRIBUTORS PTY LTD（ACN 008 801 161，无 GST）' + TAG, 'name': None,
               'facts': {'legal_name': 'The Trustee for ALTRONICS UNIT TRUST（ABN 84 177 396 871）/ ALTRONIC DISTRIBUTORS PTY LTD（ACN 008 801 161；ABN 89 008 801 161）；商号 Altronic Distributors；Perth WA 6003' + TAG}},
    'SB-181': {'kp_match': 'hkultur@inter-pos.com', 'role': 'Yönetim Kurulu Başkanı / President（1995 创立至今 30 年）= 老板 = 联系人；A.Ş. 10–19 人、$1–5M（ZoomInfo）' + TAG, 'name': None,
               'facts': {'legal_name': 'İNTERPOS BİLGİ TEKNOLOJİLERİ ELEKTRONİK SAN. VE TİC. A.Ş.（1995-04-10；Ataşehir İstanbul）', 'staff': '10–19（ZoomInfo）' + TAG}},
    'SB-180': {'kp_match': 'mahmut.cesur@foline.com.tr', 'role': 'Genel Müdür（名片）= 总经理 = 联系人（大概率老板；Ltd. Şti. 登记不免费）；数据中心 / 集装箱数据中心工程商 → CENTEC 敲门砖对口' + TAG, 'name': None,
               'facts': {'legal_name': 'FOLİNE BİLİŞİM TEKNOLOJİLERİ SAN. VE TİC. LTD. ŞTİ.（Kağıthane İstanbul；官网法定全称）' + TAG}},
}


def apply(d, u):
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if TAG not in (k.get('role') or '') and TAG not in (k.get('title') or ''):
                    key = 'role' if 'role' in k or 'title' not in k else 'title'
                    k[key] = u['role']
                if u.get('name'):
                    k['name'] = u['name']
    if u.get('kp_name'):
        for k in kps:
            if (k.get('name') or '') == u['kp_name'] and TAG not in (k.get('role') or ''):
                k['role'] = u['role']
    if u.get('add_kp') and not any(u['add_kp']['name'] == (k.get('name') or '') for k in kps):
        kps.append(u['add_kp'])
    seen, dedup = set(), []
    for k in kps:
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


for code, u in UPD.items():
    p = os.path.join(RESEARCH_DIR, f'{code}.json')
    d = json.load(open(p, encoding='utf-8'))
    for one in (u if isinstance(u, list) else [u]):
        apply(d, one)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(code, 'ok')
