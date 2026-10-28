#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 95 批（T29-U89 同轮续做，公司底数第十三轮 · B 档「筛=1」五国 17 户 + 补项 3）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=95 行）。
结构同 batch94_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：同行 / 守界 6（SB-372 AMG 自产工业交换机 / SB-214 LevelOne 台资同行品牌 + Peter 既有客户 / SB-217 Microsens / SB-528 CommFront 准同行 / SB-211 Eagle Eye 云管理 + 并入 Brivo / SB-544 Mako 云管理）→ 不动；
国别更正 2（SB-528 美国 → 新加坡；SB-370 英国 → 爱沙尼亚）；并线坐实 1（SB-906 Avizio → SB-445 AICOM）；KP 误归属 1（SB-211）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 95 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US ----------
    'SB-501': [{'add_kp': {'name': 'Dave Gattis', 'role': 'VP Engineering（DITEK 2024-Q1 社区稿）= 产品 / 选型口 = 首收件人（邮箱未公开 → 官网表单 / sales@ 点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.diteksurgeprotection.com/ditek-community-involvement-2024-q1/'}},
               {'add_kp': {'name': 'Wendy Gattis', 'role': 'CEO（2021-03-04 起；创始人 Robert McIntyre 之女）= 拍板人 = 抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://www.thomasnet.com/company/01182816/profile'},
                'facts': {'legal_name': 'DITEK Corporation（佛州；FL 登记号未取 Sunbiz ✗）', 'founded': '1988（Robert McIntyre）' + TAG, 'staff': '100–120 人；$19.9M 级（第三方）', 'hq': '1720 Starkey Road, Largo, FL 33771',
                          'other': '第 95 批：美国本土浪涌保护制造商 + 自有标 PoE / 工业交换机（外采贴标）→ OEM 30%，对口 VP Engineering；对外叙事「美国制造」→ 只谈部件配套 + 中性包装，不碰产地' + TAG}}],
    'SB-551': [{'kp_match': 'deepali@sanspot.com', 'role': '研究档 KP（职务未取；SanSpot / OptoSpan 同一班人）= 收件人' + TAG},
               {'facts': {'legal_name': 'SanSpot（品牌名；纽约法定实体未取，疑与 OptoSpan 同一公司）', 'founded': '2000（第三方）/ 域名 2003-06' + TAG, 'staff': '11–50 人', 'hq': '125 Kennedy Dr, Suite 500, Hauppauge, NY 11788',
                          'other': '第 95 批：主品类光纤线缆 / 配线（Saga 不供）→ 只剩 MC + 光口小交换机贴标一条线 OEM 30%，一页纸即止' + TAG}}],
    'SB-881': {'add_kp': {'name': 'Rodrigo (Rod) Lima', 'role': 'Founder / Manager（BBB 登记管理人；2006 创业、2007 LLC）= 老板 = 收件人（rod@nexlar.com 新闻稿公开）' + TAG, 'email': 'rod@nexlar.com', 'phone': '', 'source': 'https://www.nexlar.com/press-release/virtual-security-guard-services/'},
               'facts': {'legal_name': 'Nexlar Security, LLC（德州；TX 登记号未取；BBB 记 2007-10-08 成立；德州执照 B14634）', 'founded': '2006-04-20（开业）/ 2007-10-08（LLC）' + TAG, 'staff': '13–49 人；<$5M', 'hq': '2825 Wilcrest Dr, Suite 170, Houston, TX 77042',
                         'other': '第 95 批：休斯顿持牌安防集成商、老板邮箱公开 → 小项目集成商 25%，商用 PoE 配监控项目，直接写老板' + TAG}},
    'SB-528': {'facts': {'legal_name': 'COMMFRONT COMMUNICATIONS PTE. LTD.（新加坡 ACRA UEN 201131527M；Exempt Private Company）', 'founded': '2011-10-22（业务自称 2005）' + TAG, 'staff': '16 人；$4M 级（第三方）', 'hq': '1 Yishun Industrial Street 1, #05-31 A\'Posh BizHub, Singapore 768160（美国 Bethesda MD 地址为商务中心）',
                         'other': '第 95 批：国别更正美国 → 新加坡；自有品牌工业转换器 / 交换机制造兼网店 = 准同行（华南代工）→ 不发价格表、B 不动' + TAG},
               'country_fix': '新加坡'},
    'SB-211': [{'kp_match': 'alludolearning.com', 'role': '**误归属**：alludolearning.com 与 Eagle Eye Networks 无关 → 不发' + TAG},
               {'kp_name': 'Steve Roskowski', 'role': '来源不明（研究档；与 een.com 无公开关联）→ 不发' + TAG},
               {'facts': {'legal_name': 'Eagle Eye Networks, Inc.（Austin TX；2025-12 与 Brivo 合并，合并后以 Brivo 名义运营；登记号未取）', 'founded': '2012-07（Dean Drako）' + TAG, 'staff': '≈500 人（2023 487）', 'hq': 'Austin, TX',
                          'other': '第 95 批：云视频监控平台 = 守界（云管理）+ 2025-12 并入 Brivo 大集团 → B 不动、不发；KP 误归属已标' + TAG}}],
    'SB-544': [{'kp_match': 'toddv@makonetworks.com', 'role': 'Senior Vice President of Sales（theorg / Datanyze）= 卖方，不管采购' + TAG},
               {'add_kp': {'name': 'Andrzej Krupa', 'role': 'Director of Procurement（theorg）= 采购口（仅记档；守界不发）' + TAG, 'email': '', 'phone': '', 'source': 'https://theorg.com/org/mako-networks'},
                'facts': {'legal_name': 'Mako Networks, Inc.（美国 Elgin IL）+ Mako Networks NZ Limited（2000 年奥克兰 YellowTuna Networks 起家）', 'founded': '2000' + TAG, 'staff': '75–77 人；$18.5M 级（第三方）', 'hq': '1355 North McLean Blvd, Elgin, IL 60123',
                          'other': '第 95 批：云管理 PCI 网络设备商 = 守界（其交换机绑自家云平台、需 ODM 固件）→ 不发价格表、B 不动' + TAG}}],
    # ---------- GB / EE ----------
    'SB-215': [{'kp_match': 'darren.casey@lindy.co.uk', 'role': 'Managing Director / Director / Secretary / PSC（Companies House 02132710；1971-01 生）= **英国公司拍板人 = 研究档 KP 本人**；贴牌归 Mannheim 总部' + TAG},
               {'kp_match': 'internationalsales@lindy.com', 'role': 'International Sales（集团销售口，不管采购）' + TAG},
               {'facts': {'legal_name': 'LINDY ELECTRONICS LIMITED（Companies House 02132710；母公司 Lindy-Elektronik GmbH, Mannheim；LEI 529900RIHMCCKO7G8T48）', 'founded': '1987-05-19（英国）；集团 1932' + TAG, 'staff': '英国 37 人；集团 €16M 资产负债表（2023）', 'hq': 'Unit 103 Sadler Forster Way, Teesside Industrial Estate, Thornaby, Stockton-On-Tees TS17 9JY',
                          'other': '第 95 批：自有品牌已含交换机（亚洲代工）→ OEM 30% 对口是 Mannheim 产品管理；英国线分销 20% 补空白型号（2.5G / 10G 上联 PoE），写 MD Darren Casey' + TAG}}],
    'SB-370': {'facts': {'legal_name': 'Wildix（总部 Tallinn：VAT EE101984698；运营 Wildix S.r.l., Trento；登记号未取）', 'founded': '2005（Trento；Steve + Dimitri Osler）' + TAG, 'staff': '360 人（2025）', 'hq': 'Laeva tn. 2, 10111 Tallinn, Estonia（运营 Loc. le Basse 3, 38123 Trento）',
                         'other': '第 95 批：国别更正英国 → 爱沙尼亚（英国 Coventry 仅办事处）；UCaaS 平台 + 自有品牌 PoE 交换机（代工）→ B BIG，只认工厂级 ODM，一页纸给 Trento 产品部即止' + TAG},
               'country_fix': '爱沙尼亚'},
    'SB-372': [{'kp_match': 'steve.clarke@amgsystems.com', 'name': 'Stephen Edwin Clarke', 'role': 'Director（2019-08-09 任；1955-01 生；Companies House 02838846）= 董事本人；**同行（自产工业交换机）→ 不发**' + TAG},
               {'facts': {'legal_name': 'AMG SYSTEMS LIMITED（Companies House 02838846；Edgenet Solutions Limited 11974182 控股 ≥75%）', 'founded': '1993-07-23' + TAG, 'staff': '<50 人（Small）', 'hq': '3 Omega Centre, Stratton Business Park, Biggleswade SG18 8QB',
                          'other': '第 95 批：英国工业以太网交换机 / 光传输制造商 = 同行 → 守界：不发价格表、不加厚、B 不动；2019–2020 Edgenet 接盘已久，非进门时机' + TAG}}],
    # ---------- DE ----------
    'SB-214': [{'kp_match': 'saeid.habibi@ddc-group.com', 'role': 'DDC 集团销售口（研究档）；**LevelOne = 同行品牌 + Peter 既有客户 → 不碰**' + TAG},
               {'facts': {'legal_name': 'Digital Data Communications GmbH（Amtsgericht Dortmund HRB 9821；USt DE124728154；GF Amanda (Shu-Wen) Chen；台北 DDC 集团）', 'founded': '1991-03-27' + TAG, 'staff': '60–100 人；股本 €5.5M', 'hq': 'Im Defdahl 10F, 44141 Dortmund',
                          'other': '第 95 批：LevelOne 台资同行品牌（台湾 / 中国代工）；研究档「Peter 的产品已经做进去了」= SmartByte 既有供应链一环 → Saga 不横插，B 不动、不发；价值仅为欧洲品牌加价参照' + TAG}}],
    'SB-217': [{'kp_match': 'adevries@microsens.de', 'role': '市场 / 销售口（研究档）；**同行 → 不发**' + TAG},
               {'kp_match': 'nfaut@microsens.de', 'role': '市场 / 销售口（研究档）；**同行 → 不发**' + TAG},
               {'facts': {'legal_name': 'MICROSENS GmbH & Co. KG（Amtsgericht Hamm HRA 1669；Komplementärin MICROSENS Beteiligungs GmbH HRB 1981；GF Frank Konrad + Dirk Korn）', 'founded': '1993（创立）/ 1995-12-06（KG）' + TAG, 'staff': '50–99 人；€10–50M', 'hq': 'Küferstr. 16, 59067 Hamm',
                          'other': '第 95 批：德国本土光纤 / 工业交换机制造商（原 euromicron 80%，euromicron 2020 破产后独立）= 同行 → 守界不发、B 不动' + TAG}}],
    'SB-369': {'facts': {'legal_name': 'Wieland Electric GmbH（Amtsgericht Bamberg HRB 105；LEI 5299001AC5UDXKZ6J390；GF Dr.-Ing. Börne Rensing + Dr. Christian Wahlers）', 'founded': '1910（创立）/ 1949-09-27（GmbH）' + TAG, 'staff': '2,200 人（集团）；营收 €181.8M（2024）', 'hq': 'Brennerstraße 10-14, 96052 Bamberg',
                         'other': '第 95 批：工业连接集团，wienet 交换机为代工自有品牌 → 理论 OEM 30% 但集团采购 + 工厂级审核 → B BIG 一页纸即止；2023–24 连亏 + 2025–26 新增 Prokurist = 降本期，但 Saga 不包装成制造商' + TAG}},
    # ---------- PL ----------
    'SB-416': {'add_kp': {'name': 'Artur Rafał Bogucki', 'role': '业主（CEIDG；NIP 7742987442）= 拍板人 = 收件人（批发口 oferta@abcvision.pl，官网公开）' + TAG, 'email': 'oferta@abcvision.pl', 'phone': '', 'source': 'https://abcv.pl/pl/contact'},
               'facts': {'legal_name': 'ABC VISION - SYSTEMY ZABEZPIECZEŃ Artur Bogucki（CEIDG；NIP 7742987442；REGON 142729969）', 'founded': '2011' + TAG, 'staff': '微型（个体户）', 'hq': 'ul. 1 Maja 12/35, 09-402 Płock',
                         'other': '第 95 批：个体户网店 + 公共采购投标，现供 Hasivo → 分销 20% 小量，一页纸对标 Hasivo 价位 + CE / RoHS 文件（投标用）' + TAG}},
    'SB-1068': [{'kp_match': 'biuro@rbline.pl', 'name': 'Bartosz Ryszka', 'role': '业主（CEIDG 2010-08-01；NIP 7542138394；Roline 波兰独家代表）= 拍板人（公域 biuro@）' + TAG},
                {'facts': {'legal_name': 'RBLINE Bartosz Ryszka（CEIDG；NIP 7542138394；REGON 160340714；关联 Rb-Com s.c. Roman Ryszka Bartosz Ryszka）', 'founded': '2010-08-01' + TAG, 'staff': '小型（自述 10,000 托盘位仓）', 'hq': 'ul. Kępska 12, 45-130 Opole',
                           'other': '第 95 批：Roline（瑞士 Secomp / Rotronic）波兰独家代表 → 交换机货架被 Roline 占住，分销 20% 只补其空白型号；有国防工业 B2B 专页 → 军工 PASS' + TAG}}],
    'SB-405': [{'kp_match': 'notek@ats.pl', 'role': '业主 / 制造者（tinycontrol Marcin Nosek；CEIDG 2023-11-01；NIP 7961580284）= 拍板人 = 收件人' + TAG},
               {'facts': {'legal_name': 'tinycontrol Marcin Nosek（CEIDG；NIP 7961580284；REGON 526800704）', 'founded': '2023-11-01（现实体；品牌 / ATS 更早）' + TAG, 'staff': '微型', 'hq': 'ul. Tadeusza Mazowieckiego 7G, 26-600 Radom',
                          'other': '第 95 批：自研 LAN 控制器 + 外采配套交换机（2 光 10 电）→ OEM 30% 微量，一页纸写业主' + TAG}}],
    'SB-1085': {'add_kp': {'name': 'Maciej Prandota', 'role': 'Prezes Zarządu（TAYAMA Sp. z o.o. KRS 0000430899 自 2015-07；TAYAMA GROUP Sp. z o.o. KRS 0000947226）= 拍板人 = 收件人（m.prandota@tayama.pl 第三方目录公开）' + TAG, 'email': 'm.prandota@tayama.pl', 'phone': '', 'source': 'https://rejestr.io/krs/430899/tayama'},
                'facts': {'legal_name': 'TAYAMA Sp. z o.o.（KRS 0000430899；NIP 6272733091）+ TAYAMA Sp. z o.o. Sp.k.（KRS 0000619990；NIP 6342182846）+ TAYAMA GROUP Sp. z o.o.（KRS 0000947226；NIP 6343005879）— Prandota 家族', 'founded': '2012-08-24（Sp. z o.o.）' + TAG, 'staff': '小型（Sp.k. 营收 1.9–3.1 mln zł 区间）', 'hq': 'ul. Słoneczna 4, 40-135 Katowice',
                          'other': '第 95 批：自有品牌 CCTV + 商用 PoE / 机箱已在贴牌 → OEM 30%，写 Prezes Maciej Prandota；家族三实体重组期，采购仍在 Maciej 手里' + TAG}},
    # ---------- TR ----------
    'SB-718': {'facts': {'other': '第 95 批：底数 1 次检索未命中（gmail 名片户；结果全是无关 toptan 安防站）→ 标「底数不可查（名片户）」，不再查' + TAG}},
    # ---------- 补项 ----------
    'SB-906': {'facts': {'other': '第 95 批：avizio.pl 直查 → /kontakt 404、根域名 302 跳 a-lan.pl（A-LAN Technologie = AICOM 体系，品牌墙含 Avizio CCTV / Avizio Power；Ruijie Reyee 波兰授权分销）→ **并线 SB-445 坐实**，不再单独发 / 查' + TAG}},
    'SB-585': {'add_kp': {'name': 'Zhaoping Wei', 'role': 'Prezes Zarządu / 80% 股东 / 实际受益人（rejestr.io KRS 0000857683；2020-09-03 起）= 老板 = 拍板人（华人；可中文直联 —— 由 Simon 决定；邮箱未公开 → 官网公域点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/857683/vidos'},
               'facts': {'legal_name': 'VIDOS Sp. z o.o.（KRS 0000857683；NIP 5342626018；REGON 386943260；资本 5,000 zł；Zhaoping Wei 80% + Aneta Kaczmarczyk Wei 20%）', 'founded': '2020-09-03' + TAG, 'staff': '小型（2025 营收 29.6 mln zł、净利 2.5 mln zł；人数付费未取）', 'hq': 'Sokołowska 44, Sokołów, 05-806 Komorów',
                         'other': '第 95 批：老板华人 Zhaoping Wei、2025 营收 2,960 万 zł 盈利 → 自有品牌 PoE 必有国内货源 → OEM 30% 下调为「一对一替代」（交期 / Marvell 管理型才有戏）；收件人 = 老板本人' + TAG}},
    'SB-1046': {'add_kp': {'name': 'Konrad Ryszard Koperski', 'role': 'Prezes Zarządu（rejestr.io KRS 0000023698；2008-07-21 起，职业经理人；股东 Olesiewicz 父子各 50% 不管日常）= 拍板层（邮箱未公开；收件人仍用采购 / 产品公域）' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/23698/volta'},
                'facts': {'legal_name': 'VOLTA Sp. z o.o.（KRS 0000023698；NIP 5211367444；REGON 010829096；资本 1 mln zł；Janusz + Konrad Olesiewicz 各 50%）', 'founded': '2001-06-28' + TAG, 'staff': '70+ 人；2025 营收 90.8 mln zł、净亏 0.27 mln zł（经审计）', 'hq': 'Jutrzenki 94, 02-230 Warszawa',
                          'other': '第 95 批：2025 年报 = 营收持平、小亏、正在「发展与国内外供应商的合作」+ 开拓新市场 → 分销 20% 值得一封正式信（写采购口；信中不得引用年报，改谈 Hikvision / Dahua 配套 PoE 毛利）' + TAG}},
}


def apply(d, u):
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if u.get('name') and not k.get('name'):
                    k['name'] = u['name']
                if u.get('name') and k.get('name') and k.get('name') != u['name'] and TAG not in (k.get('role') or ''):
                    k['name'] = u['name']
                if u.get('role') and TAG not in (k.get('role') or ''):
                    k['role'] = u['role']
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
    if u.get('country_fix'):
        d['country_fix'] = u['country_fix']


if __name__ == '__main__':
    for code, u in UPD.items():
        p = os.path.join(RESEARCH_DIR, f'{code}.json')
        d = json.load(open(p, encoding='utf-8'))
        for one in (u if isinstance(u, list) else [u]):
            apply(d, one)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(code, 'ok')
