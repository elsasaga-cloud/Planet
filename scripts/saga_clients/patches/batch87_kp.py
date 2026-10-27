#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 87 批（T29-U69，公司底数第五轮 · B 档按互动强度续挖）：把官方 / 准官方登记核出来的「老板 / 董事 / 规模 / 财务」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=87 行；SB-910 / SB-1115 为 86 行补核）。
结构同 batch86_kp.py：UPD[code] 可为 dict 或 list（同一户多条更新）；键 kp_match / kp_name / name / role / add_kp / facts。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 87 批 官方登记核实 2026-10-27）'
UPD = {
    # ---------- GB ----------
    'SB-151': {'kp_match': 'marketing@optiwatchgroup.com', 'role': 'Director（Companies House 09595034：2015-05-18 创立，2020-06 → 2022-10 曾退出董事会，2022-10-01 复任；现为唯一董事；肯尼亚籍居英；2026-01 身份已核）= **老板 = 联系人**；董事名单 6 进 6 出，2024-10 还有一位只待 6 周' + TAG, 'name': 'Timothy Mathangani (Tim) Chege',
               'facts': {'legal_name': 'OPTIWATCH LTD（Companies House 09595034；2015-05-18；Unit 5 Martinbridge Trading Estate, Lincoln Road, Enfield EN1 1SP（真实工业园地址）；SIC 80200；账目至 2025-05-31 已报，下期 2027-02-28 到期）', 'staff': '微型（1 名董事；小微账目）' + TAG}},
    'SB-360': {'kp_match': 'admin@longtek.co.uk', 'role': 'Director（Companies House 05227994，2004-09-10 起；1975-05 生，英籍，身份已核）= **老板 = 联系人**；配偶 Tharshini Thevalojan 任 Secretary；注册地为 Enfield 住宅 = 21 年夫妻店' + TAG, 'name': None,
               'add_kp': {'name': 'Tharshini Thevalojan', 'role': 'Secretary（2004-09-10 起；同址 = 配偶）' + TAG, 'email': '', 'phone': '', 'source': 'https://find-and-update.company-information.service.gov.uk/company/05227994/officers'},
               'facts': {'legal_name': 'LONGTEK ELECTRONICS EUROPE LTD（Companies House 05227994；2004-09-10；12 Bishops Close, Enfield EN1 3QJ（住宅）；SIC 80200；账目至 2025-03-31 已报，下期 2026-12-31 到期）', 'staff': '微型（夫妻 2 人：1 董事 + 1 秘书）' + TAG}},
    'SB-1115': {'kp_match': 'ifolayan@millievolution.com', 'role': 'Director + **唯一 PSC（持股 50–75% + 任免董事权，2025-10-24 通知）** = 控股人 = 联系人；公司仍是 2025-10 新壳（虚拟地址）→ 付费样品 + 100% 预付不变' + TAG, 'name': None},
    # ---------- NO ----------
    'SB-836': {'add_kp': {'name': 'Roger Allan Wahlgren', 'role': 'Daglig leder（CEO，2019-01 起）+ Styremedlem（A 股股东代表）= 老板 / 拍板人；研究档原无具名 KP → 下一封写给他' + TAG, 'email': '', 'phone': '', 'source': 'https://data.brreg.no/enhetsregisteret/api/enheter/959977046/roller'},
               'facts': {'legal_name': 'FIBERWORKS AS（Org.nr 959977046；AS；1990-12-27 成立；Eikenga 11, 0579 Oslo；NACE 46.500；股本 NOK 500,000；前名 INS Communications AS 等 6 个；2025 年报已交）', 'founded': '1990-12-27（Brønnøysund 官方 API）' + TAG, 'staff': '22 名员工（NAV Aa-registeret 2026-10-10）' + TAG, 'size': '22 人（官方登记 2026-10）' + TAG}},
    # ---------- DE ----------
    'SB-426': {'kp_match': 'carsten.bokholt@helmholz.de', 'role': 'Geschäftsführer（Handelsregister 网络 GF 标记；Großenseebach）= **联系人 = 总经理 / 拍板人**；集团为 Manfred Helmholz 家族所有（Helmholz Holding GmbH 100%）；另一 GF Karsten Eichmüller、Prokura Andrea Fischer' + TAG, 'name': None,
               'facts': {'legal_name': 'Helmholz GmbH & Co. KG（Amtsgericht Fürth HRA 10671；2016-06-06 由 Helmholz Holding GmbH 分立；无限责任股东 Helmholz Verwaltungs GmbH HRB 15642；Hannberger Weg 2, 91091 Großenseebach；商标 FLEXTRA / NETLink / EasyConnect / Optopus，22 项外观设计；参股 Helmholz Benelux B.V. + Systeme Helmholz Kroatien d.o.o.）', 'staff': '中型家族集团（估 100–200；年报公示至 2024）' + TAG}},
    'SB-932': {'add_kp': {'name': 'Werner Kunze', 'role': 'Geschäftsführer（2001-07-16 起 25 年）+ 推定唯一股东 = 老板；收件已含 werner.kunze@acceed.com（0 真实打开、2026-08/09 有退信 → 先核退信地址，失效则只发 info@ 抬头 z. Hd. Herrn Kunze）' + TAG, 'email': 'werner.kunze@acceed.com', 'phone': '', 'source': 'https://www.northdata.de/Acceed%20GmbH,%20D%C3%BCsseldorf'},
               'facts': {'legal_name': 'Acceed GmbH（Amtsgericht Düsseldorf HRB 40029；2000-12-29；Arnoldstr. 19, 40479 Düsseldorf；Stammkapital €25,000；1 名股东；同址关联 MeyeControl GmbH HRB 48350）', 'founded': '2000-12-29（Handelsregister）' + TAG, 'staff': '微型（一人 GF 25 年；资产总额 €718,124 2024-12-31）' + TAG, 'size': '微型（估 3–8 人）' + TAG}},
    # ---------- US ----------
    'SB-119': {'kp_match': 'kyle@wirestar.net', 'role': 'Founder / Owner / President & CEO（SAM.gov 登记官员 PRESIDENT，UEI PU66QHF8L5F6；Aggie 100 「Founder, Owner, President」；Texas A&M BBA + MS MIS）= **老板 = 联系人**；公司 = 德州学生公寓 MDU 批量 Wi-Fi ISP + 布线商，20–50 人、$5M 级' + TAG, 'name': None,
               'add_kp': {'name': 'Logan Roy', 'role': 'Director of Business Development（官网 leadership；BBB 管理层）' + TAG, 'email': '', 'phone': '', 'source': 'https://wirestar.net/our-story/'},
               'facts': {'legal_name': 'WireStar, Inc.（d/b/a WireStar Networks；Texas S-Corp；2007-12-06 注册 / 业务 2005-02-01；SAM UEI PU66QHF8L5F6 有效至 2026-12-02；4156 State Highway 6 S, College Station TX 77845；前身 DIALUP.CC）', 'staff': '20–50（Datanyze 18 / RocketReach 42 / LeadIQ 48）；营收 $5.1M（第三方同源估）' + TAG}},
    'SB-750': {'kp_match': 'dconners@enableit.com', 'role': 'Director（研究档；官网无团队页，职务待核）；**公司定位 = 100% 美国制造 + TAA/NDAA/GSA + AS9100D 的延长器 OEM（产品本身属守界禁区）→ 不追**' + TAG, 'name': None,
               'facts': {'legal_name': 'Enable-IT, Inc.（Inc.；4616 W Sahara Ave, Las Vegas NV 89102；官网 legalName；Nevada SoS 编号未取）', 'founded': '1997/2000 起（官网：Ethernet Extender 1999、PoE Extender 2005）' + TAG, 'staff': '小型制造商（无可证人数）' + TAG}},
    'SB-780': [{'kp_match': 'lmccullough@signamax.com', 'role': 'Vice President of Sales（研究档）= 非老板；拍板人 = Key Principal Vyacheslav (Slav) Stein（D&B；SEC 10-K 2004「两名主要股东兼高管」之一）→ 对表信 cc / 改写给 Stein' + TAG},
               {'add_kp': {'name': 'Vyacheslav (Slav) Stein', 'role': 'Key Principal（D&B）= 创始股东 / 拍板人（AESP 1983 年成立；曾 Nasdaq 上市后私有化）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.dnb.com/business-directory/company-profiles.aesp_inc.c51369a341bc16874f588edaeaa2d197.html'},
                'facts': {'legal_name': 'AESP, Inc.（d/b/a Advanced Electronic Support Products；Florida corporation 1983；品牌 Signamax，子公司 Signamax, Inc.；SEC CIK 1026744 已退市；999 NW 159th Dr, Miami FL 33169）', 'founded': '1983（佛罗里达；SEC 10-K）' + TAG, 'staff': '历史 72 人 / 净销售 $15.8M（2004，SEC）；现规模不明（估明显缩小）' + TAG, 'size': '小型（历史 72 人 2004）' + TAG,
                          'other': '2005–2014 与捷克 Apron（Signamax LLC / signamax.cz）打了 9 年 SIGNAMAX 商标官司（E.D. Va. 2014）→ 欧洲 Signamax ≠ 美国 AESP，别混为一户；2004 年 34% 销售走俄乌独家分销' + TAG}}],
    'SB-739': {'kp_match': 'jbowman@arcdyn.com', 'role': 'President（ZoomInfo C-level；Alignable 团队首位）= **老板 = 联系人**（已收 21 封、3 开 0 回）；Arcdyn, Inc. 2016 成立、2–10 人、自有贴牌线 ArcCore（摄像机 + NVR）' + TAG, 'name': None,
               'facts': {'legal_name': 'Arcdyn, Inc.（非 LLC；2016；43 Mildred Ave, Asheville NC 28806（原 1370 Tunnel Rd）；NC SoS 编号未取）', 'founded': '2016（LinkedIn / ZoomInfo）' + TAG, 'staff': '2–10 人（President + 销售 2 + 仓库 2）；营收 <$5M（ZoomInfo；RocketReach $24M 不可信）' + TAG, 'size': '微型（2–10 人）' + TAG}},
    # ---------- IT ----------
    'SB-104': [{'kp_match': 'eros.stefani@stsitalia.com', 'role': '联系人 · 姓氏 = 创始家族 Stefani（atoka 成员表首位 Silvio Stefani）→ 推定家族第二代 / 管理层；公司 73–82 人、2024 营收 €7,973,181、净利 €438,664 —— 比研究档「小安防店」大得多' + TAG},
               {'kp_match': 'andrea.rongoni@stsitalia.com', 'role': '采购 / 技术经办（不在登记成员表）' + TAG},
               {'facts': {'legal_name': 'STS ITALIA S.R.L.（P.IVA / C.F. 00865310247；REA MB 1490600，原 VI 175684；1984-03-16 成立；Via Altiero Spinelli 134, 20862 Arcore (MB)；ATECO 43.21.02；股本 €110,000；PEC stsitaliasrl@pec.telemar.it；SDI MJ1OYNU）', 'staff': '73 人（2026 登记）/ 82（atoka）；2024 fatturato €7,973,181、utile €438,664、人工成本 €3,227,856；2023 €8.0M / 2022 €7.0M' + TAG, 'size': '中型（50–99 人档；欧盟「media impresa」）' + TAG}}],
    # ---------- RU ----------
    'SB-1135': {'kp_match': 'ddmitry@raisecom.su', 'role': 'Генеральный директор（2011-03-22 起）+ учредитель 100%（ИНН 782605495786）= **老板 = 联系人**；ООО «ДИЛЕР» = СПб 5 人的 Raisecom 俄罗斯经销商；2023 营收 141.7 млн ₽（净利率 20%）→ 2025 仅 25 млн ₽（−82%）' + TAG, 'name': 'Dmitry (Дейкун Дмитрий Александрович) Deikun',
                'facts': {'legal_name': 'ООО «ДИЛЕР»（DEALER Co Ltd；ОГРН 1117847101844 · ИНН 7840448665 · КПП 784201001；2011-03-22；191119 СПб, ул. Роменская 10 лит. К пом. 5；资本 10,000 ₽；唯一股东 Дейкун Д. А.）', 'founded': '2011-03-22（ЕГРЮЛ）' + TAG, 'staff': '5（ССЧ）；2023 выручка 141.7 млн ₽ / прибыль 27.9 млн；2025 выручка 25 млн ₽' + TAG, 'size': '微型（5 人）' + TAG}},
    'SB-1122': {'kp_match': 'yb@comtinu.ru', 'role': '（未署职务）—— 本轮 1 次 ЕГРЮЛ 镜像检索未能定位 comtinu.ru 的法人 → 不再检索；下次回信时请其提供 реквизиты（ИНН）用于形式发票' + TAG, 'name': None,
                'facts': {'legal_name': 'Comtinu（comtinu.ru；法人名未定位 —— ЕГРЮЛ 镜像无关联，官网快照 timeout）' + TAG}},
    'SB-487': [{'kp_match': 'afonin@npotelecom.ru', 'role': 'Директор（2010-02-11 起，ИНН 164700953825；官网 contacts 页列为 Директор）= **联系人 = 总经理 / 拍板人**（非股东；唯一股东 Шабутдинов Р. З.）；ЗАО НПО «Телеком» = 伊热夫斯克 64 人制造商，2025 营收 670.1 млн ₽（≈$7M，+34%）、净利 280.2 млн ₽（42%）；ТОРП 俄罗斯原产 NTS 交换机、主客户 Ростелеком；2026-05 问「工厂城市 / 是否做 CENTEC 方案」= ODM 寻源' + TAG, 'name': 'Mikhail (Афонин Михаил Владимирович) Afonin'},
               {'kp_match': 'sale@npotelecom.ru', 'role': 'Sales and Marketing Specialist（经办，非拍板）' + TAG},
               {'add_kp': {'name': 'Шабутдинов Рашит Зинатулович', 'role': '唯一股东（2002-12-02 起）= 所有人（不直接联系）' + TAG, 'email': '', 'phone': '', 'source': 'https://checko.ru/company/npo-telekom-1021801507694'},
                'facts': {'legal_name': 'ЗАО НПО «Телеком»（Закрытое акционерное общество Научно-производственное объединение «Телеком»；ОГРН 1021801507694 · ИНН 1833018276 · КПП 184001001 · ОКПО 43677374；1991 经营 / 2002-11-21 登记；426039 Ижевск, Воткинское шоссе 31；资本 8,500 ₽；ОКВЭД 26.30.16；Минпромторг ТОРП 目录 2024 №881：NTS-15080 / 25480 / 25480P）', 'founded': '1991（经营）/ 2002-11-21（ЕГРЮЛ）' + TAG, 'staff': '64 人（list-org）；2025 выручка 670.1 млн ₽、чистая прибыль 280.2 млн、капитал 215 млн；2024 выручка 501.0 млн / прибыль 177.0 млн；2017 → 2025 +447%；招标 456 / 中标 372' + TAG, 'size': '中型制造商（64 人）' + TAG}}],
    # ---------- TR ----------
    'SB-167': {'kp_match': 'esef@onsis.com.tr', 'role': 'Genel Müdür / Key Principal（D&B）= **老板 = 联系人**（Ltd. Şti. 股东名单付费未取）；1992 创业、2015-03-03 改组 Ltd.、1–24 人；展会 + WhatsApp 户（问 2 光 8 电 PoE 网管 bypass → $105 → 要 L2 + 样品）' + TAG, 'name': None,
               'facts': {'legal_name': 'ONSİS ELEKTRİK ELEKTRONİK GÜVENLİK SİSTEMLERİ İNŞAAT SANAYİ VE TİCARET LİMİTED ŞİRKETİ（Limited Şirket；2015-03-03；Emek Mah. Kırım Cad. Saruhan Apt. No:78 B/28, 06490 Çankaya / Ankara）', 'staff': '1–24（D&B）；Datanyze「359 人 / $28.2M」为错配不采信' + TAG}},
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
