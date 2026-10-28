#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 96 批（T29-U90，公司底数第十四轮 · B 档「自有 logo + 打开」五国 24 户 + 补项 SB-445 自身一行）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=96 行）。
结构同 batch95_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：OEM 30% 首选 SB-549 PoEWit（KP = Co-CEO）/ SB-099 Rocstor（KP = 老板）/ SB-840 InLine（INTOS AG）/ SB-453 GMTCNT / SB-651 Biges / SB-646 Art Sistem（升 A 候选）；
同行 / 守界 2（SB-533 eks Engel 自产工业交换机 / SB-1073 SensoGuard 军工）→ 不动；国别更正 2（SB-1078 美国 → 加拿大；SB-1073 美国 → 以色列）；地址更正 1（SB-1021 Płock → Zamość）；
KP 误归属 1（SB-452 Paul Panini = ESG 总监）；研究档「关联 ATTE」更正（SB-420）；补项坐实 SB-445（2025 营收 86.7 mln zł）；法定实体未坐实 2（SB-091 / SB-782 → 待补）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 96 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US / CA / IL ----------
    'SB-1078': {'add_kp': {'name': 'Nader Kashani', 'role': 'Founding Director / 老板（LinkedIn 2012-01 起；D&B Key Principal；邮箱未公开 → sales@solimedia.net 点名）= 收件人' + TAG, 'email': '', 'phone': '', 'source': 'https://solimedia.net/about/'},
                'facts': {'legal_name': 'Solimedia Technology Inc.（加拿大 BC 省公司；Soliton 集团成员；BC 登记号未取）', 'founded': '2011-09-01' + TAG, 'staff': '1–10 人', 'hq': '329-470 Granville Street, Vancouver, BC V6C 1V5',
                          'other': '第 96 批：国别更正美国 → 加拿大；MikroTik / Grandstream VAR 网店 + 集团自有亚洲货源 → 分销 20% 一页纸，补 MikroTik 没有的商用 PoE' + TAG},
                'country_fix': '加拿大'},
    'SB-391': [{'kp_match': 'sergio.fe@inscapedata.com', 'role': '研究档 KP（PoEsuperstore 网店销售口）= 收件人' + TAG},
               {'add_kp': {'name': 'David D Lin', 'role': 'Founder / CEO / CTO / 加州登记代理人（CA SoS 2438912）= 老板（华人；台北关联公司 Inscape International）= 抄送公域' + TAG, 'email': '', 'phone': '', 'source': 'https://www.cacompanyregistry.com/Agent/DAVID+D+LIN/'},
                'facts': {'legal_name': 'Inscape Data Corporation（California SoS 2438912）', 'founded': '2004-02-11' + TAG, 'staff': '10–19 人', 'hq': '2012 Hartog Court, San Jose, CA 95131',
                          'other': '第 96 批：自产户外 IP68 PoE 交换机（守界不碰）+ PoEsuperstore 室内商用 PoE 网店 → 只做室内线分销 20% / 贴标 30% 试探；老板华人 + 台湾货源 → 低概率、不加厚' + TAG}}],
    'SB-549': {'kp_match': 'dusan@poewit.com', 'role': 'Co-Founder / Co-CEO（2018-02 起；前 Pakedge 联合创始人 / CTO，2016 售予 Control4；FCC Grantee 2A24W 联系人）= **拍板人 = 研究档 KP 本人**' + TAG,
               'facts': {'legal_name': 'PoEWit Technologies Inc.（佛州；FL 登记号未取 Sunbiz ✗；FCC Grantee 2A24W）', 'founded': '2018-02（Victor Pak + Dusan Jankov + Steve Latham 自筹）' + TAG, 'staff': '11–50 人；<$5M（第三方）', 'hq': '3301 S Andrews Ave, Suite 5, Fort Lauderdale, FL 33316',
                         'other': '第 96 批：「PoE 供电一切」的定制安装品牌，交换机是系统心脏且外采贴标 → OEM 30% 首选（802.3bt 大功率 + 中性包装）；其云管理 = 他们的旁挂盒，不碰固件 ODM' + TAG}},
    'SB-099': {'kp_match': 'david@rocstor.com', 'role': 'President / CEO / 加州登记代理人 / SAM 登记高管 = **老板 = 研究档 KP 本人**' + TAG,
               'facts': {'legal_name': 'Rocstor, Inc.（加州 S Corporation；SAM UEI K79NXW8ZGNK4；CA SoS 号未取）', 'founded': '2002-03-07（业务 2000）' + TAG, 'staff': '5–20 人；$3–6M（第三方）', 'hq': '12979 Arroyo St, 2F, San Fernando, CA 91340',
                         'other': '第 96 批：自有品牌 1,500 SKU 已含网络交换机 → OEM 30% 直接写老板；SAM 政府供应商会问 NDAA / TAA（禁词）→ 只谈商用 / 教育渠道' + TAG}},
    'SB-1001': [{'kp_match': 'ken.burgner@altelix.com', 'role': '研究档 KP（职务未取）= 收件人、抄 sales@' + TAG},
                {'add_kp': {'name': 'Peter Roth', 'role': 'President / CEO（Datanyze / Manta；FL L16000173253 管理人）= 老板（邮箱未公开）' + TAG, 'email': '', 'phone': '', 'source': 'https://bisprofiles.com/fl/altelix-l16000173253'},
                 'facts': {'legal_name': 'Altelix LLC（Florida L16000173253；FEI 81-3917803）', 'founded': '2016-09-15' + TAG, 'staff': '11–20 人；$3.6–10M（第三方）', 'hq': '1201 Clint Moore Road, Boca Raton, FL 33487',
                           'other': '第 96 批：NEMA 防水机箱 / 天线制造商，机箱内交换机外采配套 → 工业 PoE 小口数一条线（STI-054GP / STI-144GP），分销 20% 或贴标 30%' + TAG}}],
    'SB-1073': [{'kp_match': 'tomer@sensoguard.com', 'role': 'CEO / CTO / 联合创始人（前 Rafael 20 年）—— 守界：不发' + TAG},
                {'kp_match': 'ido@sensoguard.com', 'role': 'Product Manager —— 守界：不发' + TAG},
                {'facts': {'legal_name': 'SensoGuard Ltd.（以色列；ח.פ. 未取）', 'founded': '2012' + TAG, 'staff': '10–13 人', 'hq': '1 HaHaruv St, Modi\'in Region Industrial Park, Shoham, Israel',
                           'other': '第 96 批：国别更正美国 → 以色列；以色列国防军 / 国防部地震波周界承包商 = 军工守界 → B 不动、不发' + TAG},
                 'country_fix': '以色列'}],
    # ---------- DE ----------
    'SB-533': {'kp_match': 're@eks-engel.de', 'role': 'Geschäftsführer / Inhaber（1994 接班；HRA 8091 Siegen 代表）= 老板 —— **同行（自产工业以太网交换机）：不发**' + TAG,
               'facts': {'legal_name': 'eks Engel FOS GmbH & Co. KG（Amtsgericht Siegen HRA 8091；Komplementärin eks Engel Verwaltungs GmbH HRB 8256；LEI 529900CLZQKLQC1QA289）', 'founded': '1931（创立）/ 2007-01-31（KG 登记）' + TAG, 'staff': '36 人；<€10M', 'hq': 'Schützenstr. 2, 57482 Wenden',
                         'other': '第 96 批：光纤 / 工业以太网交换机制造商 = 同行 → 不发价格表、B 不动；2026-09-01 Michael Matthesius 接管销售 / 产品管理，2027 国际扩张 —— 若其要外采商用 PoE 补线，对口是他' + TAG}},
    'SB-022': [{'kp_match': 'dr@desk-sicherheit.de', 'name': 'Daniel Salim Rupp', 'role': 'Geschäftsführer / 创始人（HRB 717686 Mannheim 唯一 GF；前联邦国防军）= 老板 = 收件人' + TAG},
               {'facts': {'legal_name': 'Desk Sicherheit GmbH（Amtsgericht Mannheim HRB 717686；2013 UG → 2022-12 GmbH，资本 €25,000）', 'founded': '2013-06-28' + TAG, 'staff': '微型', 'hq': 'Roonstraße 25, 76137 Karlsruhe',
                          'other': '第 96 批：一人 GmbH 安保服务 + 安防网店 → 小项目集成商 25% 一页纸；反无人机 / 渗透测试偏军警 → 只谈商用安防' + TAG}}],
    'SB-828': {'kp_match': 'friedel@luxmediaplan.de', 'role': 'Technical Managing Director / Unternehmensinhaber（官网 contact；登记业主为 Sabine Lux）= 收件人' + TAG,
               'facts': {'legal_name': 'LMP Lux Media Plan（Einzelunternehmen Sabine Lux；USt DE113809490；无 HRB）', 'founded': '1986' + TAG, 'staff': '微型（夫妻企业）', 'hq': 'Platter Strasse 168a, 65193 Wiesbaden',
                         'other': '第 96 批：广电定制微型相机 / 光纤组件 = 非品类 → 只剩 MC / 光口小交换机一条线，一页纸即止、不投第 2 封' + TAG}},
    'SB-840': {'add_kp': {'name': 'Wolfgang Isenberg', 'role': 'Vorstand（INTOS ELECTRONIC AG，HRB 4020 Gießen；Impressum）= 拍板人（邮箱未公开 → service@inline-info.com 点名 Produktmanagement Netzwerk）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.inline-info.com/Rechtliches/Impressum/'},
               'facts': {'legal_name': 'INTOS ELECTRONIC AG（Amtsgericht Gießen HRB 4020；InLine® 为其商标）', 'founded': '未取（AG）' + TAG, 'staff': '中型（4,500+ SKU；人数未取）', 'hq': 'Siemensstraße 11, 35394 Gießen',
                         'other': '第 96 批：自有品牌 InLine 已含网络交换机 / PoE（亚洲代工）→ OEM 30%，B BIG；多品类贴牌买家会比价 → 价格直接给到位' + TAG}},
    # ---------- GB ----------
    'SB-091': {'add_kp': {'name': 'Borer Data Systems — 产品经理（公域）', 'role': 'info@borer.co.uk 点名「Product Manager」= 收件人（fingerprint-access-control.com 为其 SEO 站）' + TAG, 'email': 'info@borer.co.uk', 'phone': '', 'source': 'https://www.fingerprint-access-control.com/'},
               'facts': {'legal_name': 'Borer Data Systems Ltd（Companies House 号本次未取 → 待补）', 'founded': '≈1980s（自述 40+ 年）' + TAG, 'staff': '小型（未取）', 'hq': '4 Winnersh Fields, Gazelle Close, Winnersh, Berkshire RG41 5QS',
                         'other': '第 96 批：PoE 生物识别门禁制造商，项目必配 PoE 交换机（外采）→ 配套一条线分销 20% / 贴标 30%，一页纸' + TAG}},
    'SB-452': [{'kp_match': 'paul@esp-uk.com', 'role': 'ESG & Sustainability Director（LinkedIn）= **误对口（不管采购）→ 不发给他**' + TAG},
               {'add_kp': {'name': 'ESP 产品管理（公域）', 'role': 'Elite Security Products Limited 产品 / 采购公域（Scolmore 集团，Redditch）= 收件人；National Sales Manager Ben Mackrill 仅记档' + TAG, 'email': '', 'phone': '', 'source': CH + '02769392'},
                'facts': {'legal_name': 'ELITE SECURITY PRODUCTS LIMITED（Companies House 02769392；母公司 Scolmore (International) Limited 02513009，Tamworth）', 'founded': '1992-12-01（1996 更名 ESP；2011 起 Scolmore 集团）' + TAG, 'staff': '集团 51–200 人', 'hq': 'Unit 7 Target Park, Shawbank Road, Lakeside, Redditch B98 8YN',
                          'other': '第 96 批：自有品牌 ESP CCTV 走电工批发渠道 → PoE 配套贴标 OEM 30% 理论成立，采购在 Scolmore 集团产品部 → B BIG 一页纸；研究档 KP 为 ESG 总监 = 误归属' + TAG}}],
    'SB-763': {'facts': {'legal_name': 'IDOME LIMITED（Companies House 14430734）', 'founded': '2022-10-19' + TAG, 'staff': '微型', 'hq': '23 Minterne Avenue, Southall UB2 4HW（门店 32 King Street, Southall UB2 4DB）',
                         'other': '第 96 批：2022 新注册微型 CCTV 网店 / eBay 批发，Trustpilot 2.2 分；账目 2025-10-31 期应 2026-07-31 递交（是否逾期待核）→ 分销 20% 一页纸、先款后货、不投第 2 封' + TAG}},
    'SB-782': {'kp_match': 'nigilm@simpleuk.com', 'role': '研究档 KP（职务未取；4 人公司）= 收件人' + TAG,
               'facts': {'legal_name': 'Simple Technology (UK) Ltd.（第三方；Companies House 同名候选 11667603 / 04652365 均为已解散他司 → 法定实体待核）', 'founded': '1991（第三方）' + TAG, 'staff': '4 人', 'hq': 'Warrington（电话区号 01925）',
                         'other': '第 96 批：微型配件商、法定实体一次未坐实 → 分销 20% 一页纸即止、不加厚' + TAG}},
    # ---------- PL ----------
    'SB-420': {'kp_match': 'magdalena@cdr.pl', 'role': '研究档 KP（销售）= 收件人' + TAG,
               'facts': {'legal_name': 'CDR Prosta Spółka Akcyjna（KRS 0001049574；NIP 6511717587；REGON 360676767；前身 CDR Sp. z o.o. Sp.k. KRS 0000541514）', 'founded': '2023-08-01（P.S.A.；前身 2015）' + TAG, 'staff': '小型（前身资产 57 mln zł 量级，待核）', 'hq': 'ul. Produkcyjna 14, 44-240 Żory',
                         'other': '第 96 批：研究档「关联 ATTE」有误 —— ATTE Power Sp. z o.o.（KRS 0001013262，Myślenice）是独立的波兰 PoE 交换机制造商（同行、不入库），CDR 只是其分销商 → CDR 分销 20%；自有 CDR 标 PoE 适配器 → 贴标 30% 一句试探' + TAG}},
    'SB-1021': {'kp_match': 'm.blaszczyk@cyberbajt.pl', 'role': '销售（研究档 KP）= 收件人；业主 Tadeusz Nowak（CEIDG）' + TAG,
                'facts': {'legal_name': 'Cyberbajt Tadeusz Nowak（CEIDG 个体工商户；NIP 9221003243；REGON 950190918）', 'founded': '未取（CEIDG）' + TAG, 'staff': '小型', 'hq': 'ul. Młyńska 27, 22-400 Zamość（研究档 Płock 有误）',
                          'other': '第 96 批：地址更正 Płock → Zamość；波兰最早一批 MikroTik 分销商 + 自有天线 / CBF 光纤品牌 → 分销 20%，贴标 30% 一句试探' + TAG}},
    'SB-178': {'add_kp': {'name': 'Artur Łukasz Mikołajewicz', 'role': '股东 / 实际负责人（KRS 0000379258；aleo）= 老板 = 收件人（邮箱未公开 → 官网公域）' + TAG, 'email': '', 'phone': '', 'source': 'https://wisp.pl/info/'},
               'facts': {'legal_name': 'Allnet Sp. z o.o. Sp.k.（KRS 0000379258；NIP 6423156422；REGON 241888846）', 'founded': '2011-02-28（网店 2003 起）' + TAG, 'staff': '5–10 人；营收 ≈ 32 mln zł 量级（第三方，待核）', 'hq': 'ul. Dębowa 2A, 44-237 Bełk（k. Rybnika）',
                         'other': '第 96 批：MikroTik VAD + Ubiquiti 走量批发（5–10 人做 32 mln zł）→ 分销 20%：价格到位的商用 PoE 一页纸，不加厚' + TAG}},
    'SB-428': [{'kp_name': 'Marek Kowalski', 'role': 'Prezes Zarządu（KRS 0001157117；10%）= 收件人；儿子 Tomasz Kowalski 持股 90%（2025-05-22 起）= 接班人、抄公域' + TAG},
               {'facts': {'legal_name': 'INTER-COMP.PL KOWALSKI sp. z o.o.（KRS 0001157117；NIP 5543033437；REGON 540999936；前身 CEIDG Inter-Comp.Pl Marek Kowalski 2003 起）', 'founded': '2025-02-25' + TAG, 'staff': '微型', 'hq': 'ul. Dworcowa 36a/9, 86-010 Koronowo',
                          'other': '第 96 批：父子微型网店（MC / 光口）→ 分销 20% 一页纸即止（STC-110XGE 等光口型号）' + TAG}}],
    'SB-445': {'kp_match': 'marcin.buczak@a-lan.pl', 'role': '研究档 KP = 收件人（点名产品管理）；合伙人 Adam Popiołek / Jerzy Piłat 单独代表（2026-09-30 起）' + TAG,
               'facts': {'legal_name': 'A-LAN TECHNOLOGIE POPIOŁEK, PIŁAT SPÓŁKA KOMANDYTOWA（KRS 0000654397；NIP 6782913975；REGON 356808516）', 'founded': '2016-12-22（sp. k.；前身更早）' + TAG, 'staff': '中型；2025 营收 86.7 mln zł / 净利 8.9 mln / 资产 61.5 mln（rejestr.io）', 'hq': 'ul. Dobrego Pasterza 36A, 31-416 Kraków',
                         'other': '第 96 批（补第 95 批遗留）：波兰布线龙头、自有品牌 → B BIG；分销 20% 起、贴标 OEM 30% 为目标；SB-906 Avizio 已并线至此；2026-09-30 合伙人 / 代表权刚变更 → 一页纸不提财报' + TAG}},
    # ---------- TR ----------
    'SB-422': {'kp_match': 'a.tugrul@efb-elektronik.com.tr', 'role': 'Genel Müdür（EFB Elektronik Türkiye；bthaber 2017 访谈 / LinkedIn）= **土耳其分公司拍板人 = 研究档 KP 本人**；贴牌归 Bielefeld 总部' + TAG,
               'facts': {'legal_name': 'EFB Elektronik Ltd. Şti.（EFB-Elektronik GmbH, Bielefeld HRB 33008 → TKH Group N.V. 子公司；MERSİS 未取）', 'founded': '2007（土耳其）；集团 1988' + TAG, 'staff': '小型（分公司）；集团 330 人', 'hq': 'Halide Edip Adıvar Mah. Sultan Sok. Mavi Plaza No:22 D:11/22A, 34381 Şişli / İstanbul',
                         'other': '第 96 批：集团子公司，交换机贴牌决策在德国 → B BIG；但 GM 本人是 KP 且做项目配套 → 分销 20% 一页纸（USD 报价、小批量本地备货）' + TAG}},
    'SB-453': {'kp_match': 'abdullahaydin@gmtcontrol.com', 'role': 'Project Manager（LinkedIn；嵌入式硬件背景）= 技术口 = 收件人，抄 gmt@ 点名「ürün yönetimi」' + TAG,
               'facts': {'legal_name': 'GMT Endüstriyel Elektronik San. ve Tic. A.Ş.（原 Ltd. Şti.；MERSİS 未取）', 'founded': '2014' + TAG, 'staff': '40–100 人；$8M 级（第三方）', 'hq': 'Çubuklu Mah. Boğaziçi Cad. Boğaziçi Plaza No:6/B, 34805 Beykoz / İstanbul',
                         'other': '第 96 批：土耳其首家国产 PLC 制造商（GMTCNT），目录含工业通讯产品但不自产交换机 → 工业以太网 / DIN 导轨 PoE 贴 GMTCNT 标 = OEM 30% 正解（STI-054GP / STI-144GP / STI-288DGGPM）' + TAG}},
    'SB-282': {'kp_match': 'hasan.basarir@nfsteknoloji.com', 'role': 'Teknik Destek Uzmanı（官网 teknikdestek 页）= **技术支持，非采购** → 收件人加 info@ 点名「satın alma」' + TAG,
               'facts': {'legal_name': 'NFS Teknoloji ve Otomasyon Sistemleri San. ve Tic. Ltd. Şti.（EMIS；MERSİS 未取）', 'founded': '2006-11-09（5 名工程师合伙）' + TAG, 'staff': '7 人；$4M 级（第三方）', 'hq': 'Aydınevler Mah. Öncel Sok. Meda Marmara Sit. No:1-13A, 34854 Maltepe / İstanbul',
                         'other': '第 96 批：7 人项目型安防分销（Pelco / Hanwha / TDSI）→ 分销 20% 一页纸，商用 PoE 配项目，不加厚' + TAG}},
    'SB-646': {'kp_match': 'serkank@artsistem.com', 'name': 'Serkan Kekik', 'role': '创始人 / Genel Müdür（2004-09-04 创办；gesider「Ayın CEO’su」；官网总经理致辞）= **老板 = 研究档 KP「Serkan K.」大概率本人**' + TAG,
               'facts': {'legal_name': 'Art Sistem Bilgisayar ve Güvenlik Teknolojileri Ltd. Şti.（LinkedIn 写 A.Ş. 待核；MERSİS 未取）', 'founded': '2004-09-04' + TAG, 'staff': '100–200 人；$10–50M 级（第三方）；5,000+ 经销商；3 分公司', 'hq': 'Gültepe Mah. Florya Kavşağı E-5 Yanyol Cad. 1. Bilge Sok. No:1 Art Sistem Plaza, 34295 Küçükçekmece / İstanbul',
                         'other': '第 96 批：土耳其大户 —— 5,000+ 经销商 + 自有品牌 Artes（2006 起）+ 已做 OEM 摄像机 + TP-Link VIGI 独家 → B BIG；贴标 OEM 30% 为目标、分销 20% 为底；老板直联 → **升 A 候选（回信即 A）**' + TAG}},
    'SB-651': {'kp_match': 'erdal.goksen@biges.com', 'role': '研究档 KP（职务未取）= 收件人，抄 arge@ / info@ 点名「ürün yönetimi」' + TAG,
               'facts': {'legal_name': 'Biges Güvenli Hayat Teknolojileri Elektronik A.Ş.（MERSİS 未取）', 'founded': '1998' + TAG, 'staff': '77–149 人；$20M 级（第三方）', 'hq': 'Piyalepaşa Bulvarı No:77 Famas Plaza B Blok, 34384 Şişli / İstanbul',
                         'other': '第 96 批：自有 biges 品牌 + 自建研发（GitHub arge@）→ 系统内 PoE 交换机外采贴标 → OEM 30%，B BIG' + TAG}},
    'SB-677': [{'kp_match': 'cenk@perkotek.com', 'role': '研究档 KP（全名 / 职务未取）= 收件人，抄 info@ 点名「ürün yönetimi / satın alma」' + TAG},
               {'add_kp': {'name': 'Selçuk Erdoğan', 'role': 'Firma Yetkilisi（teketekhaber 企业名录 2021；登记负责人）= 仅记档' + TAG, 'email': '', 'phone': '', 'source': 'https://teketekhaber.com/firmarehberi/perkotek-teknoloji-dis-tic-a-s'},
                'facts': {'legal_name': 'Perkotek Teknoloji Dış Tic. A.Ş.（EMIS 2016-06-01 注册；旧实体 Biometrik PERKOTEK … Ltd. Şti.；MERSİS 未取）', 'founded': '2016-06-01（A.Ş.）；品牌 1995' + TAG, 'staff': '68–200 人；3,000+ 经销商；出口 65 国', 'hq': 'Mahmutbey Mah. Ordu Cad. Perkotek Plaza No:29, 34218 Bağcılar / İstanbul',
                          'other': '第 96 批：门禁 / 考勤终端制造商、出口 65 国 → PoE 交换机为项目配套（外采）→ 配套贴标 OEM 30% 小口数一条线，B' + TAG}}],
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
