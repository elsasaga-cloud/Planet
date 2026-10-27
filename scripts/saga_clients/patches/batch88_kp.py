#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 88 批（T29-U70，公司底数第六轮 · B 档按互动强度续挖）：把官方 / 准官方登记核出来的「老板 / 董事 / 股权 / 规模 / 财务」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=88 行；SB-151 / SB-005 / SB-836 为 87 行补核）。
结构同 batch87_kp.py：UPD[code] 可为 dict 或 list（同一户多条更新）；键 kp_match / kp_name / name / role / add_kp / facts。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 88 批 官方登记核实 2026-10-27）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- DE ----------
    'SB-193': [{'add_kp': {'name': 'Ulrich Abendschein', 'role': 'Geschäftsführer（2006 起；同时任 STABILO Fachmarkt 连锁多家公司 GF）= 拍板人；研究档原无具名 KP → 对表信抬头 z. Hd. Herrn Abendschein' + TAG, 'email': '', 'phone': '', 'source': 'https://www.northdata.de/DEMA%20Vertriebs-GmbH,%20Unterm%C3%BCnkheim'},
                'facts': {'legal_name': 'DEMA Vertriebs-GmbH（Amtsgericht Stuttgart HRB 571318；LEI 529900NC79L6B29H5354；1963-01-17 登记；Im Tal 1, 74547 Untermünkheim；Stammkapital €800,000（2009）；2 名股东（付费未取）；商标 DEMA 文字 2021 + 图形 2026-10）', 'founded': '1963-01-17（Handelsregister）' + TAG, 'staff': 'Bilanzsumme €29.8M（2024-12-31）；2021-07 州补贴 €742,684；= STABILO 五金建材连锁集团的采购 / 批发公司（同址 Hohenloher Elektrogroßhandel GmbH）' + TAG, 'size': '中型（集团采购公司；资产 €29.8M）' + TAG}},
               {'add_kp': {'name': 'Günther Denner', 'role': 'Prokurist（Kupferzell；自有品牌「Denner Edition」）= 采购 / 经营层第二签字人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.northdata.de/DEMA%20Vertriebs-GmbH,%20Unterm%C3%BCnkheim'}}],
    # ---------- GB ----------
    'SB-781': [{'kp_match': 'cdiprima@silvernet.com', 'role': '员工（非董事 / 非 PSC；Companies House 05386276 董事仅 Ballard 夫妇）—— 25 封群发收件人之一，0 回' + TAG},
               {'kp_match': 'knewton@silvernet.com', 'role': '员工（非董事 / 非 PSC）—— 25 封群发收件人之一，0 回' + TAG},
               {'add_kp': {'name': 'Christopher Roland Ballard', 'role': 'Director（2005-03-09 创立至今，1973-10 生，身份已核）+ PSC 持股 50–75% = **老板 = 该写的人**（我们 25 封都寄给了员工）' + TAG, 'email': '', 'phone': '', 'source': CH + '05386276/persons-with-significant-control'},
                'facts': {'legal_name': 'SILVERNET LIMITED（Companies House 05386276；2005-03-09 成立，原名 COMPLETE SECURITY SOLUTIONS LIMITED 至 2005-05-11；19 Presley Way, Crownhill, Milton Keynes MK8 0ES；SIC 26309 通信设备制造；账目至 2025-11-30 已报，下期 2027-08-31；有 charges 记录）', 'founded': '2005-03-09（Companies House）' + TAG, 'staff': '家族制造小厂（夫妻 100% 持股：Chris >50% + Mandy 25–50%）；自有品牌无线 + PoE 交换机' + TAG, 'size': '小型（家族企业；人数未公示）' + TAG}},
               {'add_kp': {'name': 'Mandy Joyce Ballard', 'role': 'Secretary + PSC 持股 25–50%（1970-08 生；配偶）—— 不必抄送' + TAG, 'email': '', 'phone': '', 'source': CH + '05386276/officers'}}],
    'SB-745': {'kp_match': 'tim.jones@comtrol.co.uk', 'role': 'Director（Companies House 09041682：2014-05-15 创始董事 → 2020-02-03 辞任 → 2023-01-18 回任至今；1973-07 生）= **董事 / 共同创办人 = 联系人**；公司 2020-02 换班、2021–2025 有挪威籍董事（投资方）、2025-01 再换班、2025-10 挪威董事退出 → 正处「重选供应商」窗口' + TAG, 'name': 'Timothy (Tim) Jones',
               'add_kp': {'name': 'Nigel Robert Wesley', 'role': 'Director（2020-02→2022-07；2025-01-13 回任至今；1957-04 生）= 与 Jones 共同当家' + TAG, 'email': '', 'phone': '', 'source': CH + '09041682/officers'},
               'facts': {'legal_name': 'COMTROL UK LIMITED（Companies House 09041682；2014-05-15；登记地址 168 Church Road, Hove BN3 2DL = 代理地址；同名旧体系 COMTROL GMBH 英国分支 BR008786 Bicester / FC026768 Zug 均已 Closed；SIC / 账目 / PSC 下轮补）', 'founded': '2014-05-15（现法人；「30+ 年」承自旧 Comtrol 英国分支）' + TAG, 'staff': '小型（9 名董事进出，现 2 名在任；人数 / 账目未取）' + TAG}},
    'SB-151': {'facts': {'other': 'PSC 页（2026-10-27）：Timothy Mathangani Chege ≥75% 股权 + 表决权（2022-10-01 起；2016-04→2021-06 曾持 ≥75%，2021-06→2022-11 由 Faith Mathangani 持 ≥75%）→ 一人公司坐实' + TAG}},
    # ---------- NL ----------
    'SB-055': {'kp_match': 'j.slob@dios-industries.com', 'role': 'CEO + 经个人控股 Kiyi Holding B.V.（KvK 59106808）任 Epic Europe B.V. 唯一 bestuurder（2013-10-29 起）= **老板 = 联系人**；2025-03 本人两封要价表，我们给了两份后无下文 = 价表没对上需求（他卖监控配套 PoE）' + TAG, 'name': 'Jacco (Jacob) Slob',
               'facts': {'legal_name': 'Epic Europe B.V.（KvK 59111380 · vestiging 000028430891；2013-10-29；法定住所 Etten-Leur、经营地 De Meeten 82, 4706 NH Roosendaal；SBI 80.20；商号 DIOS / DIOS Industries / DIOS Ultra HD Security Systems；母公司 Kiyi Holding B.V.；旧 Dios Industries V.O.F. KvK 76083926（2019）已注销；2026-01-23 另有新登记 KvK 99697149 待核）', 'founded': '2013-10-29（KvK）' + TAG, 'staff': '5–9 人（de10beste / KvK 人数档）；年报存档记录至 2021 账年' + TAG, 'size': '微型（5–9 人）' + TAG}},
    # ---------- PL ----------
    'SB-246': {'kp_match': 'marek@is-net.pl', 'role': '业主（个体工商户 IS NETWORKS Marek Kubas；CEIDG 决策人；1996 年起）= **老板 = 联系人**；2026-02 他要 CENTEC 参数 + 价格，我们欠一张价表' + TAG, 'name': 'Marek Kubas',
               'facts': {'legal_name': 'IS NETWORKS Marek Kubas（jednoosobowa działalność gospodarcza；NIP 8130069738 · REGON 690005253；1996；ul. Warszawska 24, 35-205 Rzeszów；PKD 43.21.Z；网店 isnetworks.pasaz24.pl）', 'founded': '1996（CEIDG 镜像）' + TAG, 'staff': '微型（个体户 + 少量雇员）' + TAG, 'size': '微型（个体户）' + TAG}},
    # ---------- US ----------
    'SB-1114': {'kp_match': 'cfikes@fikesmedia.com', 'role': 'Owner / Founder（2007-01 起；Crunchbase / Tracxn）= **老板 = 联系人**；本职 Evadale ISD（德州学区）Director of IT（2018-08 起）—— FikesMedia 是他的一人 MikroTik 咨询 / 集成公司，客户 = 学区 + 市政；GitHub 开源作者 → 技术人，别催样，给 API / SNMP / CLI 文档' + TAG, 'name': None,
                'facts': {'legal_name': 'FikesMedia（FikesMedia LLC，ZoomInfo；TX SoS 编号未取；105 George St, Silsbee TX 77656；另 109 Pinecrest Dr）', 'founded': '2007（官网 about / Tracxn）' + TAG, 'staff': '1–10 人（Tracxn 2024-07）；未融资；业主兼职' + TAG, 'size': '微型（一人公司）' + TAG, 'hq': 'Silsbee, Texas（休斯敦东北 Hardin 县）' + TAG}},
    # ---------- UA ----------
    'SB-007': {'kp_match': 'sergiy.khodun@gmail.com', 'role': 'Керівник + 唯一 засновник（ЄДРПОУ 40277067，2016-02-15 起）= **老板 = 联系人**；但公司身份 = PLANET 乌克兰官方进口商且对外卖点「台湾产、非中国大陆」→ 与我们天然冲突，留档不追' + TAG, 'name': 'Sergiy Khodun（Ходун Сергій Олександрович）',
               'facts': {'legal_name': 'ТОВ «ДОЙЧ ІМПОРТ»（LLC "DEUTSCHE IMPORT"；ЄДРПОУ 40277067；2016-02-15；Київ, вул. Анни Ахматової；статутний капітал 1,000 UAH；КВЕД 46.90；品牌 Germany24 / planet.kiev.ua）', 'founded': '2016-02-15（ЄДР）' + TAG, 'staff': '微型（一人 ТОВ；资本 1,000 UAH）' + TAG, 'size': '微型' + TAG}},
    # ---------- TR ----------
    'SB-185': {'kp_match': 'mehmet@zeytek.com.tr', 'role': 'Genel Koordinatör（2019 创立起；公司名 Zeytek = Zeytinli + Teknoloji）= **老板 = 联系人**（Ltd. Şti. 股东付费未取）；5 人布线材料供应商（总协调 + 销售助理 Kamuran İpek + 记账 Sinem Doğan）' + TAG, 'name': None,
               'facts': {'founded': '2019（官网 Hakkımızda / LinkedIn）' + TAG, 'staff': '5 人（RocketReach；ZoomInfo 11–50 偏高）' + TAG}},
    'SB-187': {'kp_match': 'bilgi@pelikanbilgisayar.com', 'role': 'Kurucu ortak / Firma Sahibi（2003-07 起，「tüm operasyonlar」；LinkedIn）= **老板 = 联系人**；Perpa 电子商城 DIGITUS 配件经销档口 + Şişli 仓库' + TAG, 'name': None,
               'facts': {'legal_name': 'PELİKAN BİLGİSAYAR HİZMETLERİ İTHALAT İHRACAT（Pelikan Bilişim；Perpa Ticaret Merkezi A Blok Sarı Avlu K:4 No:271, Şişli / İstanbul；旧址 Dereboyu Cad. No:60 Mecidiyeköy；Ticaret Sicil No 未取）', 'founded': '2003-07（LinkedIn 创始人履历）' + TAG, 'staff': '微型（档口 + 仓库，估 3–10 人）' + TAG}},
    'SB-093': {'kp_match': 'satis@konakguvenlik.com.tr', 'role': '销售邮箱联系人；个人推特 2018 起转发公司账号 → 疑为业主 / 核心人员（未证实）；本轮 1 次检索未能定位法人（「Konak」= 伊兹密尔区名，噪音大）→ 不再检索；Q-33 口径留档' + TAG, 'name': None,
               'facts': {'legal_name': 'Konak Güvenlik（konakguvenlik.com.tr；法定全称 / Ticaret Sicil 未定位）' + TAG}},
    # ---------- RS ----------
    'SB-887': {'kp_match': 'cegar@stasanet.rs', 'role': 'Direktor + 法定代表 + **15% 股东**（85% = 捷克 MVA GROUP s.r.o. / 布拉格 Stasanet 集团）= 经营者 = 联系人，大额采购布拉格拍板；公司 = Dahua 塞尔维亚分销（dahua.rs）、<5 人、营收 50–100 M RSD（≈ €0.4–0.85 M）' + TAG, 'name': None,
               'facts': {'staff': '<5 人；营收 50–100 M RSD、利润 0.1–0.5 M RSD（cubepartner 区间）；贝尔格莱德 + 诺维萨德两处；年合作约 200 家安装商（RS + BiH / ME / MK）' + TAG, 'other': '股权：MVA GROUP s.r.o.（CZ）85% + Predrag Čegar 15%；开户 Unicredit Bank Srbija；PDV 纳税人；= 布拉格 Stasanet s.r.o.（创始人 Jakubík）第 8 家 / 最小分部；dahua.rs 即本公司' + TAG}},
    # ---------- NO（财务补核）----------
    'SB-836': {'facts': {'staff': '23–24 人（Aa 登记）/ 19 全职（Åpenhetsloven 2026 声明）；**2025 营收 NOK 138.4 M（≈ €11.7 M）、EBIT 36.9 M（27%）、净利 29.4 M；2024 营收 136.2 M、分红 24.7 M**（proff / 1881，2026-06）' + TAG, 'other': '股东：Sorb Industri AB（瑞典）100%；董事长 Martin Roland Linder；DAGL Roger Allan Wahlgren；2026 发布挪威透明法供应链声明 → 预备供应商问卷' + TAG}},
    # ---------- SK（死胡同记录）----------
    'SB-005': {'facts': {'other': 'FinStat 免费登记页（IČO 36225801，2026-10-27 两段读完）：DIČ 2020163277、Ul. 9. mája 49 Trnava、vznik 1997-12-22（Sro 10793/T）、资本 €6,639、3–4 人、营收 €0.5–1 M 档、含电信安装（2002）+ 安防技术牌照 §7（2006）—— **konateľ 不在免费页** → Marián Ondrejíček 是否老板仍待一次 web_search（下轮）' + TAG}},
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
