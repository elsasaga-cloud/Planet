#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 103 批（T29-U96，公司底数第二十一轮 · B 档「自有 logo + 打开」四国 24 户：US 8 / TR 8 / DE 7 / GB 1）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=103 行）。
结构同 batch102_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 OEM 30% 目标 2（SB-834 VIDEOR/eneo 自有标 PoE 交换机现 UTEPO 代工 = 首选 / SB-1034 GSS 自有 BLUE|LINE 贴标安防线）；可谈贴标 3（SB-1028 Fiber Savvy 自有系列 / SB-862 Cebeci 自有 Cifocs 标 / SB-984 Olson 入门交换机 small）；
分销 20% 大户 3（SB-1024 DOW Technologies $93M / SB-1075 Silmar 9 网点 / SB-691 Vitel Bilişim 500 第 93）；分销 20% 一般 4（SB-1030 Fibertronics small / SB-670 Monkas 采购型 small / SB-642 Apres BDCOM 同类经销 / SB-401 Securasound small）；
分销 20% 低概率（品牌绑定 / 集团 / 目录准入）5（SB-1059 Neteon = Moxa / SB-858 Areskom = Westermo + 轨交守界 / SB-410 4S = Red Lion + 国防守界 / SB-1096 West Penn Wire = Belden 集团 / SB-550 reichelt = Dätwyler 目录商）；
集成商 25% 3（SB-864 DAC-EL 弱电侧 / SB-879 MFD 4 人 Siemens 伙伴 small / SB-667 Münchner Glasfaser 光纤施工 small）；低概率一页纸后不动 2（SB-675 Pan Dacom 同行系统集成 / SB-539 IPCOMM IEC 61850 守界）；不动 2（SB-707 Götz 一人事务所 / SB-753 profichip USA 芯片商 + 误记）；
坐实 20 / 部分坐实 4（SB-1034 NY DOS 号 / SB-670 MERSİS / SB-642 法定形式 / SB-753 GA 号）/ 未坐实 0；KP 坐实 = 老板 / GF / Prokurist / GM / 销售经理本人 6（SB-1034 Tina = Sales Manager Hong Chen / SB-675 Markus Förster = Prokurist / SB-879 Mustafa Cimic = Project Manager / SB-401 Jason Wainwright = GM / SB-707 Peter Götz = Inhaber / SB-1075·1024 补 CEO 名）；
国别 / 城市更正 4（SB-753 → 美国 country_fix；SB-670 安卡拉非伊斯坦布尔；SB-539 纽伦堡非 Ebermannstadt；SB-667 Gilching）；法定名更正 6（SB-1034 = Global Security Solution USA Inc. / Allspec Security NY, Inc.；SB-1024 = DEDC, Inc.；SB-1028 = CRN Solutions, LLC；SB-691 = Vitel Veri İletişimi ve Telekomünikasyon Sistemleri A.Ş.；SB-864 = DAC-EL Elektrik Elektronik Mühendislik Sistemleri Ltd. Şti.；SB-834 = VIDEOR E. Hartig GmbH）；
事实更正 2（SB-550 reichelt 非家族企业 = Dätwyler 子公司；SB-984 Olson 现属 Antronix）；守界 4（SB-1030 ITAR / SB-858 轨交 / SB-410 国防 / SB-539 IEC 61850 —— 稿内不提）；
升 A 候选 4（SB-834 / SB-1034 / SB-691 / SB-1024，回信即 A；次候选 SB-1075 / SB-862 / SB-642 / SB-1028）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 103 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US 8 ----------
    'SB-1030': [{'add_kp': {'name': 'Barbara Larson', 'role': '创办人 / 所有人（SBA 女性所有；与 Douglas P. Larson 共同创办）= 收件人（经 sales@）' + TAG, 'email': '', 'source': 'https://florida.intercreditreport.com/company/fibertronics-inc-p09000049074'}},
                {'facts': {'legal_name': 'Fibertronics, Inc.（FL Sunbiz P09000049074；FEI 38-3801080；Active）', 'founded': '2009-06-05' + TAG,
                           'other': '第 103 批：Melbourne FL 定制光纤组件制造商（AS9100D / TL 9000 / ISO 9001；ITAR 线守界不提）+ 光纤配件分销 → **分销 20% small**（光口交换机作 MC 替代）；一页纸' + TAG}}],
    'SB-984': [{'add_kp': {'name': 'Thomas R. Olson', 'role': 'Owner-President（1985 起；现 Antronix of California – Olson Technology Division）= 收件人（经 sales@）' + TAG, 'email': '', 'source': 'http://www.olsontech.com/company.html'}},
               {'facts': {'legal_name': 'Olson Technology, Inc.（现 Antronix of California, Olson Technology Division；私有）', 'founded': '1985-07' + TAG,
                          'other': '第 103 批：Mi-Wuk Village CA CATV / FTTH 光设备制造商，交换机为边角配套；群发 11 次无回复 → **贴标 small：一页纸最后一次后不动**' + TAG}}],
    'SB-1034': [{'kp_match': 'tina@gogss.com', 'name': 'Hong (Tina) Chen', 'role': 'Sales Manager, GSS New York（IPVM 认证）= 收件人本人' + TAG},
                {'add_kp': {'name': 'Gary Greve', 'role': 'Owner = 拍板人（抄送路径经 Tina）' + TAG, 'email': '', 'source': 'https://gogss.com/about-us/'}},
                {'facts': {'legal_name': 'Global Security Solution USA Inc.（Crunchbase）/ Allspec Security NY, Inc.（站点法律页）— GSS / GOGSS；NY DOS 号未取 → 部分坐实', 'founded': '2015（域名 2009）' + TAG,
                           'other': '第 103 批：Fresh Meadows NY 工厂直采备货进口商，自有 BLUE|LINE / GREY|LINE 贴标安防线（含 PoE 交换机），多州仓 → **贴标 OEM 30% 目标，B BIG，升 A 候选**' + TAG}}],
    'SB-1024': [{'add_kp': {'name': 'Dave Elkin', 'role': 'SVP Sales & Product Management = 供应商准入对口 / 收件人' + TAG, 'email': '', 'source': 'https://www.dowtechnologies.com/executive'}},
                {'add_kp': {'name': 'John J. Yodzis', 'role': 'President & CEO（DEDC, Inc.）= 拍板人（二代）' + TAG, 'email': '', 'source': 'https://www.dowtechnologies.com/executive'}},
                {'facts': {'legal_name': 'DEDC, Inc.（DBA DOW Technologies；控股 DOW Equity Holdings, Inc.；原 DOW Electronics，2021-03-01 更名）', 'founded': '1959' + TAG,
                           'other': '第 103 批：Tampa FL 家族技术分销商（$93.3M / 98 人；Ubiquiti / Luxul / Intellinet PoE 在售）→ **分销 20%，B BIG，加厚一次；升 A 候选**' + TAG}}],
    'SB-1028': [{'facts': {'legal_name': 'CRN Solutions, LLC dba Fiber Savvy（CA LLC；SoS 号未取）', 'founded': '1996（CRN）；Fiber Savvy 商号 2009/2010' + TAG,
                           'other': '第 103 批：Lake Elsinore CA 光纤电商（3 万平方英尺仓；自有 Fibersavvy 系列；少数族裔所有；ISO 9001/14001）→ **分销 20%，可谈 Fibersavvy 贴标；加厚一次**' + TAG}}],
    'SB-1059': [{'add_kp': {'name': 'Hubert Yu', 'role': 'President = 拍板人 / 收件人（经 sales@）' + TAG, 'email': '', 'source': 'https://rocketreach.co/neteon-technologies-inc-profile'}},
                {'facts': {'legal_name': 'Neteon Technologies Inc（NJ；SAM UEI X3SPD5JCJD67；CAGE 3DMQ6）', 'founded': '2002-08-12' + TAG,
                           'other': '第 103 批：North Brunswick NJ（非 CA）Moxa Premier Distributor 24 年 → **分销 20% 低概率（Moxa 绑定）；一页纸**' + TAG}}],
    'SB-1075': [{'add_kp': {'name': 'Jorge E. Smith', 'role': 'President & CEO（二代；FL 注册代理）= 拍板人；收件人改 purchasing / vendor 入口' + TAG, 'email': '', 'source': 'https://search.sunbiz.org/Inquiry/CorporationSearch/ByName'}},
                {'facts': {'legal_name': 'Silmar Electronics, Inc.（FL Sunbiz 275645；FEI 59-1028324；ACTIVE）', 'founded': '1963-11-13' + TAG,
                           'other': '第 103 批：Miami / Doral FL 美国最大独立安防分销商之一（9 网点；51–200 人）→ **分销 20%，B BIG，加厚一次；升 A 次候选**' + TAG}}],
    'SB-1096': [{'add_kp': {'name': 'Brian Prusinski', 'role': 'Director, Sales（ZoomInfo）= 收件人（经 sales@，点名 product management）' + TAG, 'email': '', 'source': 'https://www.westpennwire.com/about.php'}},
                {'facts': {'legal_name': 'West Penn Wire（Belden Inc. 集团成员，NYSE: BDC；PA 实体号未取）', 'founded': '1971（Claysville PA；1990 CDT；2004 Belden）' + TAG,
                           'other': '第 103 批：Washington PA 线缆制造商 + 私标服务；Belden 集团自有工业交换机品牌 → **分销 20% 低概率；一页纸即止**' + TAG}}],
    # ---------- TR 8 ----------
    'SB-670': [{'kp_match': 'murat@monkas.com.tr', 'role': '研究档 KP（职务未核；安卡拉网店）= 收件人' + TAG},
               {'facts': {'legal_name': 'Monkas Bilişim Teknolojileri A.Ş.（Ankara Yenimahalle；MERSİS 未取 → 部分坐实）', 'hq': '安卡拉 Yenimahalle（Çamlıca Mah. Anadolu Blv. Timko 1 Sok. No:20 A-5）— 非伊斯坦布尔' + TAG,
                          'other': '第 103 批：安防网店 + 自行进口（海关记录 99 条）→ **采购型 small / 分销 20%；一页纸**' + TAG}}],
    'SB-691': [{'kp_match': 'gokhan.kanat@vitel.com.tr', 'role': '研究档 KP（职务未核；Vitel A.Ş.）= 收件人' + TAG},
               {'facts': {'legal_name': 'Vitel Veri İletişimi ve Telekomünikasyon Sistemleri A.Ş.（Vitel A.Ş.；İstanbul Kadıköy）', 'founded': '1993-01-08' + TAG,
                          'other': '第 103 批：30 年增值 IT 分销商（51–200 人；Bilişim 500 2024 第 93；ManageEngine 独家）→ **分销 20%，B BIG，加厚一次；升 A 候选**' + TAG}}],
    'SB-858': [{'kp_match': 'info@areskom.com.tr', 'role': '通用信箱（另有 satis@areskom.com.tr）= 收件人点名 satış müdürü' + TAG},
               {'facts': {'legal_name': 'Areskom İletişim Sistemleri Tic. Ltd. Şti.（İstanbul Üsküdar；MERSİS 未取）', 'founded': '2004' + TAG,
                          'other': '第 103 批：Westermo 土耳其官方分销 + 轨交展商（守界）→ **分销 20% 低概率；一页纸即止**' + TAG}}],
    'SB-862': [{'kp_match': 'mustafaengin@cebecigrup.com', 'role': '研究档 KP（职务未核）= 收件人；抄 Hakan Cebeci' + TAG},
               {'add_kp': {'name': 'Hakan Cebeci', 'role': '负责人（HTK 集群联系人；推定 Genel Müdür）= 抄送' + TAG, 'email': 'hakancebeci@cebecigrup.com', 'source': 'https://www.htk.org.tr/companies/cebeci-teleteks-1'}},
               {'facts': {'legal_name': 'Cebeci Teleteks San. ve Tic. Ltd. Şti.（İstanbul Şişli Okmeydanı；MERSİS 未取）', 'founded': '1995（Ltd.；1978 Cebeci Telefon 起家）' + TAG,
                          'other': '第 103 批：光纤测试 / 接入设备分销 + 自有 Cifocs 品牌 → **分销 20%，可谈 Cifocs 贴标；加厚一次；升 A 次候选**' + TAG}}],
    'SB-864': [{'kp_match': 'ecirit@dacel.com.tr', 'role': '研究档 KP（职务未核）= 收件人' + TAG},
               {'kp_match': 'info@dacel.com.tr', 'role': '研究档 KP（经 info@；职务未核）= 抄送' + TAG},
               {'facts': {'legal_name': 'DAC-EL Elektrik Elektronik Mühendislik Sistemleri San. ve Tic. Ltd. Şti.（DACEL Mühendislik；İstanbul Esenler + Ataşehir）', 'founded': '1995' + TAG,
                          'other': '第 103 批：工业自动化分销 + 交钥匙集成（Belden Preferred Partner 2010 起 = Hirschmann 线被占）+ 弱电 → **集成商 25%，弱电侧切入；一页纸**' + TAG}}],
    'SB-879': [{'kp_match': 'info@mfd.com.tr', 'name': 'Mustafa Cimic', 'role': 'Project Manager（MCS Factory Digitalization）= 收件人本人' + TAG},
               {'facts': {'legal_name': 'MCS Factory Digitalization Endüstriyel Bilişim Teknolojileri Ltd. Şti.（MFD；İstanbul Ümraniye）', 'founded': '2016' + TAG,
                          'other': '第 103 批：4 人 Siemens 伙伴 SI（CodeMaster 平台）→ **集成商 25% small；一页纸即止**' + TAG}}],
    'SB-410': [{'facts': {'legal_name': '4S Elektrik Elektronik Telekomünikasyon İleri Teknoloji Ar-Ge Ltd. Şti.（Red Lion 名录：4s Elektrik Elektronik Telekominikasyon İth. İhr. Paz. Tic. Ltd. Şti.；İzmir Konak）',
                          'hq': '伊兹密尔 Konak（Halkapınar Mah. 1203/5 Sok. İkiz Çarşı 2 Apt. No:3 B/B）' + TAG,
                          'other': '第 103 批：Red Lion Controls 官方分销 + Thor Guard 代理；国防参考（守界）→ **分销 20% 低概率；一页纸后不动**' + TAG}}],
    'SB-642': [{'add_kp': {'name': 'İnanç Karabayır', 'role': 'Genel Müdür（LinkedIn）= 收件人（经 info@）' + TAG, 'email': '', 'source': 'https://tr.linkedin.com/in/inanç-karabayır-1a7475195'}},
               {'facts': {'legal_name': 'APRES TEKNOLOJİ（商号；法定形式 / MERSİS 未取 → 部分坐实；İstanbul Kartal + Pendik 门店 + Bursa 分部）',
                          'other': '第 103 批：经销商网络 B2B 安防 + IT 分销，BDCOM 分销（懂中国直采）→ **分销 20%，可谈二线价位；加厚一次；升 A 次候选**' + TAG}}],
    # ---------- DE 7 ----------
    'SB-675': [{'kp_match': 'foerster@pandacomdirekt.de', 'role': 'Prokurist（总代理权人，companyhouse.de 登记）= 收件人本人' + TAG},
               {'add_kp': {'name': 'Dirk Bachmann', 'role': 'Geschäftsführer（2002 起；兼 Pan Dacom Networking AG Vorstandsvorsitzender）= 拍板人' + TAG, 'email': '', 'source': 'https://www.companyhouse.de/Pan-Dacom-Direkt-GmbH-Dreieich'}},
               {'facts': {'legal_name': 'Pan Dacom Direkt GmbH（HRB 35050 Amtsgericht Offenbach am Main；USt-ID DE813529743；LEI 529900QZSNZ1ZE3HYA38）', 'founded': '2002-10-17（成立 2002-09-01）' + TAG,
                          'other': '第 103 批：自研传输设备 + 系统集成（控股 Pan Dacom Networking AG）→ **低概率；一页纸即止后不动**' + TAG}}],
    'SB-707': [{'kp_match': 'peter@goetz-automation.de', 'role': 'Inhaber / Dipl.-Ing. (FH)（一人工程师事务所）' + TAG},
               {'facts': {'legal_name': 'Götz Automation — Dipl.-Ing. (FH) Peter Götz（Einzelunternehmen；无 HRB；USt-ID DE216371896；IHK Rhein-Neckar）',
                          'other': '第 103 批：自述「1Mann Ing. Büro」；2008 一次 10 台 RFQ 后无交集 → **不动**' + TAG}}],
    'SB-539': [{'add_kp': {'name': 'Artur Votteler', 'role': 'Geschäftsführer（2004 起）= 收件人（经 info@）' + TAG, 'email': '', 'source': 'https://www.ipcomm.de/article/Impressum/en/sheet.html'}},
               {'facts': {'legal_name': 'IPCOMM GmbH（HRB 31759 Amtsgericht Nürnberg；USt-ID DE813859506）', 'founded': '2004-01-05' + TAG,
                          'hq': '纽伦堡（Walter-Bouhon-Straße 4, 90427 Nürnberg；2015 前 Erlangen）' + TAG,
                          'other': '第 103 批：协议网关制造商（IEC 61850 方案 = 咱们守界）+ 8 次无回复 → **低概率；一页纸即止后不动**' + TAG}}],
    'SB-550': [{'add_kp': {'name': 'Ulf Timmermann', 'role': 'Geschäftsführer（Sprecher）；收件人改 Einkauf / Produktmanagement 入口' + TAG, 'email': '', 'source': 'https://www.companyhouse.de/en/Reichelt-Elektronik-GmbH-Sande'}},
               {'facts': {'legal_name': 'reichelt elektronik GmbH（HRB 219874 Amtsgericht Oldenburg；原 GmbH & Co. KG HRA 200654；USt-ID DE259817039；Dätwyler Holding AG 子公司）', 'founded': '1969（GmbH 改制登记 2023-08-31）' + TAG,
                          'other': '第 103 批：15 万+ SKU 目录电商（≈280 人；1.76 亿 € 2020）；**非家族企业（2010 起 Dätwyler）**；8 次无回复 → **分销 20% 低概率；一页纸即止**' + TAG}}],
    'SB-667': [{'add_kp': {'name': 'Richard Verhülsdonk', 'role': 'Geschäftsführer / Inhaber = 收件人（经 info@）' + TAG, 'email': '', 'source': 'https://www.mgt.bayern/impressum-und-datenschutz'}},
               {'facts': {'legal_name': 'Münchner Glasfaser-Technik GmbH（HRB 244603 Amtsgericht München；USt-ID DE322142460）', 'founded': '2018-10-30' + TAG,
                          'hq': 'Gilching bei München（Rudolf-Diesel-Straße 12, 82205；2022-12 自 München Ubostr. 21 迁入）' + TAG,
                          'other': '第 103 批：光纤 / 通信网络建设承包商（11–50 人；3 GF）→ **集成商 25% small；一页纸后不动**' + TAG}}],
    'SB-753': [{'country_fix': '美国'},
               {'facts': {'legal_name': 'profichip USA, Inc.（Alpharetta, GA；母体 profichip GmbH Herzogenaurach，2012 起属 Yaskawa Europe GmbH；GA 号未取）',
                          'hq': '美国 Alpharetta, GA（980 Birmingham Rd. #721）— 研究档「德国」与 eu.com 域名均为误记' + TAG,
                          'other': '第 103 批：工业通信 ASIC 供应商的 1 人美国销售点（上游同行；表内「3 旺工业 FS」为误记）→ **不动，不发信**' + TAG}}],
    'SB-834': [{'add_kp': {'name': 'Dominik Mizdrak', 'role': 'Geschäftsführer（2021 起）= 经营侧拍板人；收件人改 eneo Produktmanagement / Einkauf 入口' + TAG, 'email': '', 'source': 'https://eneo-security.com/de/impressum'}},
               {'add_kp': {'name': 'Lars Alexander Hagenlocher', 'role': 'Geschäftsführer / 三代股东（2025-03 起；创办人 Ernst Hartig 之孙）' + TAG, 'email': '', 'source': 'https://eneo-security.com/de/impressum'}},
               {'facts': {'legal_name': 'VIDEOR E. Hartig GmbH（eneo 为其注册商标；HRB 32047 Amtsgericht Offenbach am Main；USt-ID DE113592980；LEI 529900I9XJZT6A9R6M34；股本 870,000 €）', 'founded': '1987-08-23（公司 1975 创办）' + TAG,
                          'other': '第 103 批：专业视频 / 安防分销商，自有品牌 eneo 已卖贴标 PoE 交换机（现 UTEPO 代工，稿内不点名）→ **贴标 OEM 30% 首选目标，B BIG，加厚；升 A 候选**；9 次群发无回复 → 二次触达走产品经理路径' + TAG}}],
    # ---------- GB 1 ----------
    'SB-401': [{'kp_match': 'jason@securasound.co.uk', 'role': 'General Manager（家族二代；实际经营）= 收件人本人' + TAG},
               {'add_kp': {'name': 'Philip Anthony John Wainwright', 'role': 'Managing Director / Director / PSC（创办人；b. 1946-06）= 拍板人' + TAG, 'email': '', 'source': CH + '02111547/officers'}},
               {'facts': {'legal_name': 'SECURASOUND LIMITED（CH 02111547；VAT 453682634；Active；Micro）', 'founded': '1987-03-17' + TAG,
                          'other': '第 103 批：Whitchurch, Shropshire 微型安装商分销（2–10 人；<£1M）→ **分销 20% small；一页纸**' + TAG}}],
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
