#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 85 批（T29-U67，公司底数第三轮）：把各国官方 / 准官方登记核出来的「老板 / 董事 / 规模 / 财务」写回 research/<code>.json 的 kp[] / company_facts。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=85 行）。
结构同 batch84_kp.py（kp_match / role / name / add_kp / facts + 同邮箱去重）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 85 批 官方登记核实 2026-10-27）'
UPD = {
    # ---------- US ----------
    'SA-054': {'kp_match': 'nealc@softnetworks.net', 'role': 'Vice President（2014 至今）= 采购拍板人；老板 / 成员待核（NJ LLC 不公开成员）；Softnetworks LLC 2011 年 NJ 注册，EIN 46-1347043，18 人，K-12 学区投标常客（Red Bank BOE 等）' + TAG, 'name': None,
               'facts': {'legal_name': 'SOFTNETWORKS LLC（New Jersey，2011；Whippany NJ；EIN 46-1347043）', 'staff': '18' + TAG}},
    'SA-026': {'kp_match': 'expresssupply.net', 'role': 'President（Florida 登记管理层）= 老板 = 联系人；Secretary Carmen Schulting（家族）；法人 Express Supply Inc（FL 2006），品牌 Hardened Networks = ITS Express（2008）；Florida DOT APL 在册供应商' + TAG, 'name': 'Mark V. Schulting',
               'add_kp': {'name': 'Carmen Schulting', 'role': 'Secretary（Florida 登记；家族）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.corporationwiki.com/Florida/Tampa/mark-v-schulting/'},
               'facts': {'legal_name': 'EXPRESS SUPPLY INC（Florida，2006；dba Hardened Networks / ITS Express 2008）' + TAG}},
    'SA-060': {'kp_match': 'irivera@fiberx.net', 'role': 'Presidente y CEO（创始人）= 老板 = 联系人；FiberX LLC（Puerto Rico 2016/17，ISP + 数据中心，PeeringDB fac 14857，~34 人）' + TAG, 'name': 'Iván Rivera',
               'facts': {'legal_name': 'FIBERX LLC（Puerto Rico，2016/17；Guaynabo PR；ISP + DC）', 'staff': '~34' + TAG}},
    'SA-025': {'kp_match': 'info@getsecurityalarm.com', 'role': '总机 → 实际收件人 = Owner Brandon Walter Adams（TX 登记 0800828533，2007-05；微型报警装机商）' + TAG, 'name': None,
               'facts': {'legal_name': 'AVENGER SECURITY SERVICES INC（Texas 0800828533；Hutto TX；Owner Brandon Walter Adams）', 'staff': '1–5' + TAG}},
    # ---------- TR ----------
    'SA-009': {'kp_match': 'info@coptek.com.tr', 'role': '总机（Koptek Ltd. Şti. İstanbul 2006-02-07 成立；自有品牌交换机；Ltd. Şti. 高管不免费公开 → 下一轮 Ticaret Sicil Gazetesi）' + TAG, 'name': None,
               'facts': {'legal_name': 'KOPTEK … LTD. ŞTİ.（İstanbul，2006-02-07；find.com.tr / EMIS 3700640）' + TAG}},
    'SA-055': {'kp_match': 'ali@nova-grup.com', 'role': '**非 Genel Müdür**（用户记录「CEO」待修正）：Genel Müdür 为 Cem Aytaç；Ali Pekyürek 为管理层 / 股东待核；Nova Grup Mühendislik（Ankara 2002）= 进口商 + 自有品牌 Novacom + 4 城门店 + TSE 服务站，35–36 人' + TAG, 'name': None,
               'add_kp': {'name': 'Cem Aytaç', 'role': 'Genel Müdür（总经理；官网 TSE 服务站清单 / ZoomInfo）= 拍板人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.zoominfo.com/c/nova-grup/1319836017'},
               'facts': {'legal_name': 'NOVA GRUP MÜHENDİSLİK … LTD. ŞTİ.（Ankara，2002；品牌 Novacom）', 'staff': '35–36' + TAG}},
    'SA-049': {'kp_match': 'info@iotsistem.com', 'role': '已回复联系人 = 大概率老板（微型公司，Bosgem Otomasyon / IoT Sistem，İstanbul Maltepe 2010；USR IoT 土耳其分销 + 自有 BOSGEM 品牌；法定全称待补）' + TAG, 'name': None,
               'facts': {'legal_name': 'BOSGEM OTOMASYON …（İstanbul Maltepe，2010；品牌 IoT Sistem / BOSGEM；法定全称待补）', 'staff': '微型（1–5）' + TAG}},
    'SA-030': {'kp_match': 'info@snexus.com.tr', 'role': '总机 → 法人为 HEMMAH GROUP BİLİŞİM VE MİMARLIK TİCARET LTD. ŞTİ.（Çekmeköy），品牌 Snexus Networks；品牌负责人 Erdem Timur Koca' + TAG, 'name': None,
               'add_kp': {'name': 'Erdem Timur Koca', 'role': 'Snexus 品牌负责人（LinkedIn；官网销售合同卖方 = Hemmah Group）= 拍板人' + TAG, 'email': '', 'phone': '', 'source': 'https://www.snexus.com.tr/en/sözleşme'},
               'facts': {'legal_name': 'HEMMAH GROUP BİLİŞİM VE MİMARLIK TİCARET LTD. ŞTİ.（Çekmeköy İstanbul；品牌 Snexus Networks）' + TAG}},
    # ---------- RU ----------
    'SA-036': {'kp_match': 'zakaz@svn-video.ru', 'role': '订单邮箱 → 法律主体为 ИП（个体企业家）Криволуцкая Юлия Викторовна = 老板本人；ОГРНИП 318402700048713 · ИНН 402910363642，2018-08-02 登记，ОКВЭД 46.43' + TAG, 'name': 'ИП Криволуцкая Юлия Викторовна',
               'facts': {'legal_name': 'ИП Криволуцкая Юлия Викторовна（ОГРНИП 318402700048713 · ИНН 402910363642；Калуга；2018-08-02；品牌 SVN svn-video.ru）', 'staff': '1–5' + TAG}},
    # ---------- IT ----------
    'SA-081': {'kp_match': None, 'kp_name': 'Pasquale Pirozzi', 'role': 'Direzione Generale（总经理，LinkedIn；大概率创始合伙人 / 老板）= 拍板人（但 17 封 0 开）' + TAG, 'name': None,
               'add_kp': {'name': 'Gaetano Chiaese', 'role': 'Technical Networking Manager（4Net 有源产品技术负责人；研究档收件人 g.chiaese@）' + TAG, 'email': 'g.chiaese@4power.it', 'phone': '', 'source': 'https://it.linkedin.com/company/4power-srl'},
               'facts': {'legal_name': '4POWER S.R.L.（C.F./P.IVA 04527921219；Casandrino NA；2003；ISO 9001/14001/45001；自有品牌 4Net + Planet 意大利官方分销）', 'staff': '10–19（Kompass）' + TAG}},
    'SA-083': {'kp_match': 'info@kyma.it', 'role': '兄妹家族经营者（la Repubblica 2023：guidata dai fratelli Davide e Mara Zisios）= 老板 = 联系人；Kyma S.r.l. 1995 成立，3–5 人，2024 营收 €3.52M / 净利 €216k；Planet + 3onedata 意大利分销' + TAG, 'name': None,
               'facts': {'legal_name': 'KYMA S.R.L.（P.IVA 01612520351 · REA RE-199577；1995-03-20；Reggio Emilia；PEC kymasrl@legalmail.it）', 'staff': '3–5；2024 营收 €3,519,588 / 净利 €215,669' + TAG}},
    # ---------- IN ----------
    'SA-038': {'kp_match': None, 'name': None,
               'add_kp': {'name': 'Lakshman Lakshmannivas Deepak', 'role': 'Director（DIN 06562153，2013-05-20 创立至今，唯一在任创始董事）= 实控人；Whole-time Director Nomitha Soundrarajan（2023-07）；MCA 年报停在 FY2022-23' + TAG, 'email': '', 'phone': '', 'source': 'https://www.zaubacorp.com/DNC-TECHNOSOLUTIONS-PRIVATE-LIMITED-U33125KL2013PTC034130'},
               'facts': {'legal_name': 'DNC TECHNOSOLUTIONS PRIVATE LIMITED（CIN U33125KL2013PTC034130；2013-05-20；Ernakulam Kerala；实缴 ₹1 lakh）' + TAG}},
    # ---------- PL ----------
    'SA-034': {'kp_match': 'tomasz.paszkowski@rfog.pl', 'role': '业主（CEIDG 个体经营 RFOG POLAND TOMASZ PASZKOWSKI，2011-02-22；NIP 8571157213 · REGON 811833063）= 老板 = 联系人；兼 ARiMR 动物标识政府供应商' + TAG, 'name': None,
               'facts': {'legal_name': 'RFOG POLAND TOMASZ PASZKOWSKI（CEIDG 个体经营；NIP 8571157213 · REGON 811833063 · VAT UE PL8571157213；Gryfice；2011-02-22）' + TAG}},
    # ---------- TW ----------
    'SA-013': {'kp_match': 'johnson@alfa.com.tw', 'role': '来信署名人（职务待核，非负责人）；负责人 President Huang Lili（D&B）、硬件总监 Jeremy Wu；ALFA Network 2002 成立、11–50 人、欧洲电商自营（法国 SIREN 901445445）' + TAG, 'name': None,
               'add_kp': {'name': 'Huang Lili（Bai Lian）', 'role': 'President（D&B Key Principal）= 负责人 / 老板' + TAG, 'email': '', 'phone': '', 'source': 'https://www.dnb.com/business-directory/company-profiles.alfa_network_inc.92c8275df8b0f94300f98ff30d74ce55.html'},
               'facts': {'legal_name': 'ALFA NETWORK INC.（Taipei Neihu；2002；法国 SIREN 901445445 = 欧洲远距销售 VAT 登记 2021-05）', 'staff': '11–50' + TAG}},
    # ---------- KR ----------
    'SA-010': {'kp_match': 'marketing@ez-net.co.kr', 'role': '대표이사（CEO / 创始人）= 老板 = 联系人；(주)이지넷유비쿼터스 2006-04-04 法人登记（2004 开业），사업자 106-86-42660，44 人，2024 营收 251.6 억원（≈ $18M）、品牌 NEXT 约 1,000 SKU' + TAG, 'name': None,
               'facts': {'legal_name': '(주)이지넷유비쿼터스 EZ-NET Ubiquitous Co., Ltd.（사업자등록번호 106-86-42660；2006-04-04；서울 용산구；资本金 5,000 만원）', 'staff': '43–44（국민연금 2026）；2024 营收 251.6 억원' + TAG}},
    'SA-029': {'kp_match': 'master@gtwave.co.kr', 'role': '대표이사 박문수（bizno 名录代表 + 研究档联系人同名）= 老板 = 联系人；(주)지티웨이브 有线通信设备制造业，판교；2026-03 入选富川产业振兴院 창업도약패키지' + TAG, 'name': None,
               'facts': {'legal_name': '(주)지티웨이브 GTWAVE Co., Ltd.（성남 분당구 판교로 723；사업자번호待补）' + TAG}},
    # ---------- GR / PY / DE（据研究档入库，无新检索）----------
    'SA-056': {'kp_match': 'imports@bselectronics.gr', 'role': 'CEO / Founder = 个人企业业主（Ατομική επιχείρηση Βασίλειος Σταυρίδης）= 老板 = 联系人；ΓΕΜΗ 号待补（JS 查询不可达）' + TAG, 'name': None},
    'SA-061': {'kp_match': None, 'name': None,
               'facts': {'other': 'RYMTECH E.A.S.（RUC 80125463-9；股东 Osorio 夫妇；DNCP 政府供应商 Micro 档）—— 巴拉圭登记据研究档入库' + TAG}},
    'SA-075': {'kp_match': 'info@falke-security.de', 'role': 'Inhaber（业主，Creditreform 登记名 Nuri Sahin Sicherheitsdienste „Falke Security“；Einzelunternehmen 无 HRB）= 老板 = 联系人' + TAG, 'name': None},
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
    if u.get('kp_name'):
        for k in kps:
            if (k.get('name') or '') == u['kp_name'] and TAG not in (k.get('role') or ''):
                k['role'] = u['role']
    if u.get('add_kp') and not any(u['add_kp']['name'] == (k.get('name') or '') for k in kps):
        kps.append(u['add_kp'])
    seen, dedup = set(), []
    for k in kps:  # 同邮箱 KP 改名后重复 → 去重
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
