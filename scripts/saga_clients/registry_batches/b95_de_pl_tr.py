#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 95 批 · DE 3 户 + PL 4 户 + TR 1 户未命中 + 补项 3（SB-906 avizio.pl 直查 / SB-585 Vidos zarząd / SB-1046 Volta zarząd）（T29-U89 同轮续做，2026-10-28）。
web_search depth 1 各一次；rejestr.io 直页 fetch_page ×2；avizio.pl 直查 ×2（/kontakt 404 → 根域名 302 → a-lan.pl）。可重复运行（put 按 code 合并）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 95

# ---------------- DE 3 ----------------
put('SB-214', key='de', batch=B, name='Digital Data Communications GmbH（level1.com / digital-data.de；Dortmund）— LevelOne 品牌 = 台资 DDC 集团欧洲公司（同行品牌）', iso='DE', fetched=F,
    source='DE · 1 次检索：level1.com Imprint（GF Amanda (Shu-Wen) Chen；Amtsgericht Dortmund HRB 9821；USt DE 124728154）+ Northdata HRB 9821（Prokura Damian Nöthe / Johannes van Kempen；股本 €5,500,000；2010-12 商标 LEVEL ONE）+ implisense（1991-03-27 登记；Im Defdahl 10F, 44141 Dortmund；批发 4651）+ DDC 公司简介 PDF（1991 年 Dortmund 创立 IT 批发；60 人；研发 / 制造 / 分销网络 / 连接 / 安防产品；**生产在台湾 & 中国**；Soest 物流中心）+ non-plus-ultra（100 人）+ GITEX 2025 展商页（KAM Nico Riedl；BD Director Asia & ANZ Harry Yohannan）',
    url='https://www.level1.com/level1_en/imprint',
    number='Amtsgericht Dortmund HRB 9821', status='Active', incorporated='1991-03-27', company_type='GmbH（股本 €5.5M；台北 Digital Data Communications 集团控股 — GF 为台籍）',
    sic=['4651 网络 / 外设批发 + 自有品牌 LevelOne（交换机 / PoE / 工业交换机 / 监控）设计分销'],
    address='Im Defdahl 10F, 44141 Dortmund', accounts='—（未取）', accounts_due='—', size_band='中型（60–100 人；€5.5M 股本）',
    officers=['Amanda (Shu-Wen) Chen — Geschäftsführerin（台籍，集团派驻）', 'Damian Nöthe — Prokurist', 'Johannes Elbert van Kempen — Prokurist', 'Saeid Habibi — 研究档 KP（ddc-group.com；销售口）'], psc='台北 DDC 集团（推定）', charges='', prev_names=[],
    lines=['**LevelOne = 同行品牌（台资，产品自台湾 / 中国代工）**；研究档记「Peter 的产品已经做进去了」= **SmartByte 已是其供应链一环** → Saga 不能横插（供应商既有客户）→ B 不动、不发',
           '价值只在情报：LevelOne 欧洲选型 / 价位 = SmartByte 在欧洲的「出厂→品牌」加价参照',
           '研究档 KP Saeid Habibi 是销售（ddc-group.com）而非采购 → 即便日后碰也不是他'],
    notes='Peter 既有客户 → 不碰；不再查。')
put('SB-217', key='de', batch=B, name='MICROSENS GmbH & Co. KG（microsens.com；Hamm）— 光纤 / 工业交换机制造商 = 同行', iso='DE', fetched=F,
    source='DE · 1 次检索：microsens.com/footer/imprint（HRA Hamm 1669；Komplementärin MICROSENS Beteiligungs GmbH HRB Hamm 1981；GF Dipl.-Ing. Frank Konrad + Dipl.-Kfm. Dirk Korn；USt DE170837673；Küferstr. 16, 59067 Hamm）+ Northdata HRA 1669 + companyhouse.de（1995-12-06 登记；资本 €1,000,000；制造业；最近变更 2026-09-02）+ wer-zu-wem（50–99 人；营收 €10–50M）+ Elektroniknet 2006（euromicron AG 收购 80%；创始人 Dr. Hocine Bezzaoui 1993 创立）+ Wikipedia euromicron（2020-06 破产清算 → Microsens 已脱离）',
    url='https://www.microsens.com/footer/imprint',
    number='Amtsgericht Hamm HRA 1669（Komplementärin HRB 1981）', status='Active', incorporated='1993（创立）/ 1995-12-06（KG 登记）', company_type='GmbH & Co. KG（原 euromicron 集团 80%，euromicron 2020 破产后独立 / 易主）',
    sic=['26 光纤传输 / 工业以太网 / 楼宇微型交换机制造（自研自产，Hamm）'],
    address='Küferstr. 16, 59067 Hamm', accounts='—（KG 未公开）', accounts_due='—', size_band='中型（50–99 人；€10–50M）',
    officers=['Frank Konrad — Geschäftsführer', 'Dirk Korn — Geschäftsführer', 'Anke de Vries / Nailia Faut — 研究档 KP（microsens.de；市场 / 销售口）'], psc='未取（euromicron 破产后股东变更未公开）', charges='', prev_names=[],
    lines=['**德国本土光纤 / 工业交换机制造商 = 同行** → 守界：不发价格表、不加厚、B 不动',
           '研究档 KP 两位是市场 / 销售口 → 即便有 ODM 需求也不是她们',
           '记档价值：euromicron 2020 破产后的 Microsens 现股东未公开 → 若日后出现「外采商用 PoE 补线」信号再看'],
    notes='不再查。')
put('SB-369', key='de', batch=B, name='Wieland Electric GmbH（wieland-electric.com；Bamberg）— 工业连接 / 自动化集团，wienet 工业交换机为代工自有品牌', iso='DE', fetched=F,
    source='DE · 1 次检索：wieland-electric.com/en/imprint（HRB 105 Amtsgericht Bamberg；GF Dr.-Ing. Börne Rensing + Dr. Christian Wahlers；Brennerstraße 10-14, 96052 Bamberg）+ openregister（Prokura 2025-06 Fabian Reuß；2026-03 Thilo Döring / Eik Stachowicz）+ online-handelsregister（1949-09-27 GmbH 登记；资本 €15,500,000）+ Northdata（LEI 5299001AC5UDXKZ6J390）+ Die Deutsche Wirtschaft（2,200 人；营收 €181.8M 2024）+ craft.co（2024：营收 €181.8M、净亏 €3.5M）+ unternehmen24（净利 2022 +€5.5M → 2023 −€16.1M → 2024 −€3.5M）+ Wikipedia（1910 创立；€223.2M 2022）',
    url='https://www.wieland-electric.com/en/imprint/',
    number='Amtsgericht Bamberg HRB 105（LEI 5299001AC5UDXKZ6J390）', status='Active', incorporated='1910（创立）/ 1949-09-27（GmbH）', company_type='GmbH（股本 €15.5M；Wieland 家族集团）',
    sic=['27 工业连接器 / 安全继电器 / 楼宇电气安装系统制造 + wienet 工业交换机 / 路由（代工自有品牌）'],
    address='Brennerstraße 10-14, 96052 Bamberg', accounts='2024 营收 €181.8M、净亏 €3.5M（2023 净亏 €16.1M）', accounts_due='—', size_band='大型（2,200 人集团；€180–220M）',
    officers=['Dr.-Ing. Börne Rensing — Geschäftsführer（2021-02 起）', 'Dr. Christian Wahlers — Geschäftsführer（2021-07 起）', 'Prokura 多人（2025–2026 新增 3 人）'], psc='Wieland 家族', charges='', prev_names=[],
    lines=['**大型工业集团、wienet 交换机本就外采贴牌** → 理论 OEM 30%，但走集团采购 + 工厂级审核 → **B BIG**，一页纸工业 PoE 给产品管理即止，不加厚',
           '2023–2024 连亏（−€16.1M / −€3.5M）+ 2025–2026 新增 3 名 Prokurist = 降本换血期 → 「更便宜的工业 PoE 代工」有听众，但 Saga 不是工厂 → 不要包装成制造商（守 Saga.md）',
           '没有 KP → 若发只写 wienet 产品公域；发信窗口 Thu 12–14 CET'],
    notes='不加厚。')

# ---------------- PL 4 ----------------
put('SB-416', key='pl', batch=B, name='ABC VISION - SYSTEMY ZABEZPIECZEŃ Artur Bogucki（abcv.pl；Płock）— CEIDG 个体户', iso='PL', fetched=F,
    source='PL · 1 次检索：abcv.pl/dane-firmy + /pl/contact（ABC VISION - SYSTEMY ZABEZPIECZEŃ BOGUCKI ARTUR；NIP 7742987442；REGON 142729969；ul. 1 Maja 12/35, 09-402 Płock；批发报价 oferta@abcvision.pl；公共采购部 zamowieniapubliczne@）+ /pl/i/O-nas（2011 年起；CCTV / 报警 / 门禁 / 综合布线 / DVB-T 零售 + 批发；「Rzetelna Firma」）+ 隐私政策（管理者 Bogucki Artur Rafał）+ Ceneo 店铺页',
    url='https://abcv.pl/dane-firmy',
    number='NIP 7742987442 / REGON 142729969（CEIDG）', status='Active（网店 2026 在线）', incorporated='2011', company_type='Jednoosobowa działalność gospodarcza（个体户）',
    sic=['4652 安防 / 网络设备零售 + 批发（网店 + 公共采购投标）'],
    address='ul. 1 Maja 12/35, 09-402 Płock', accounts='—（个体户）', accounts_due='—', size_band='微型（个体户）',
    officers=['Artur Rafał Bogucki — 业主'], psc='Artur Bogucki 100%', charges='', prev_names=[],
    lines=['个体户网店 + 公共采购投标，研究档「现供 Hasivo」→ **分销 20% 小量**：一页纸 STC-028GP / STC-228GP 对标 Hasivo 价位，写业主 Artur Bogucki（oferta@ 批发口）',
           '公共采购部 = 学校 / 市政项目用 PoE 交换机 → 可提 CE / RoHS 文件齐全（投标需要）',
           '量小、不加厚；发信窗口 Thu 12–14 CET'],
    notes='')
put('SB-1068', key='pl', batch=B, name='RBLINE Bartosz Ryszka（rbline.pl；Opole）— Roline（Rotronic / Secomp）波兰独家代表，CEIDG 个体户', iso='PL', fetched=F,
    source='PL · 1 次检索：rbline.pl 首页 / kontakt（RBLINE Bartosz Ryszka；ul. Kępska 12, 45-130 Opole；NIP 7542138394；REGON 160340714；2010 年起；「Roline 品牌波兰独家代表」；近 2,000 SKU、95% 现货、10,000 托盘位自述）+ GoWork（个体户；2010-08-01 开业；关联 Rb-Com s.c. Roman Ryszka Bartosz Ryszka）+ zbrojenia.rbline.pl（国防工业 B2B 专页）+ baza-firm（Roline = 瑞士 ROTRONIC AG 品牌）',
    url='https://rbline.pl/kontakt',
    number='NIP 7542138394 / REGON 160340714（CEIDG）', status='Active', incorporated='2010-08-01', company_type='Jednoosobowa działalność gospodarcza（个体户；关联 Rb-Com s.c. 父子合伙）',
    sic=['4651 网络组件 / UPS / IP 摄像机批发（Roline 独家 + 多品牌）'],
    address='ul. Kępska 12, 45-130 Opole', accounts='—（个体户）', accounts_due='—', size_band='小型（自述 10,000 托盘位仓；人数未取）',
    officers=['Bartosz Ryszka — 业主', 'Roman Ryszka — Rb-Com s.c. 合伙人（父）'], psc='Bartosz Ryszka 100%', charges='', prev_names=[],
    lines=['**Roline（瑞士 Secomp / Rotronic 体系）波兰独家代表 → 其交换机货架已被 Roline 工业 / 商用交换机占住**；分销 20% 只能补 Roline 没有的型号（2.5G / 10G 上联 PoE、L3）',
           '有国防工业 B2B 专页 → 守界提示：军工项目 PASS，只谈商用 / 工业通用',
           '业主直联（biuro@ 公域）；一页纸即止，不加厚'],
    notes='')
put('SB-405', key='pl', batch=B, name='tinycontrol Marcin Nosek（tinycontrol.pl；Radom）— LAN 控制器 / IoT 微型制造商，CEIDG 个体户', iso='PL', fetched=F,
    source='PL · 1 次检索：tinycontrol.pl/en/contact（Manufacturer: tinycontrol Marcin Nosek, Mazowieckiego 7G, 26-600 Radom；服务 mqtt.ats.pl）+ aleo.com（NIP 7961580284；REGON 526800704；个体户；**CEIDG 开业 2023-11-01**）+ sklep.tinycontrol.pl 隐私政策（Marcin Nosek 个体经营）+ Google Play 开发者（TINYCONTROL MARCIN NOSEK）+ 100mega / i4wifi（捷克分销其 LAN Controller）',
    url='https://aleo.com/pl/firma/tinycontrol-marcin-nosek',
    number='NIP 7961580284 / REGON 526800704（CEIDG）', status='Active', incorporated='2023-11-01（CEIDG 现实体；品牌 / ATS 更早）', company_type='Jednoosobowa działalność gospodarcza（个体户）',
    sic=['26 LAN 控制器 / IoT 模块设计制造 + 网店（含 2 光 10 电交换机等外采配套）'],
    address='ul. Tadeusza Mazowieckiego 7G, 26-600 Radom', accounts='—（个体户）', accounts_due='—', size_band='微型',
    officers=['Marcin Nosek — 业主 / 制造者（= 研究档 KP notek@ats.pl 本人）'], psc='Marcin Nosek 100%', charges='', prev_names=[],
    lines=['自研 LAN 控制器 + 外采配套交换机（研究档「2 光 10 电」）→ **OEM 30% 微量**：工业 / 商用小口数贴 tinycontrol 标，直接写业主 Marcin Nosek',
           '2023-11 新实体 = 由 ATS 体系拆出来的个人品牌 → 量极小，一页纸即止',
           '发信窗口 Thu 12–14 CET'],
    notes='')
put('SB-1085', key='pl', batch=B, name='TAYAMA（tayama.pl；Katowice）— Prandota 家族三实体：TAYAMA Sp. z o.o. / TAYAMA Sp. z o.o. Sp.k. / TAYAMA GROUP Sp. z o.o.', iso='PL', fetched=F,
    source='PL · 1 次检索：rejestr.io KRS 0000430899（TAYAMA Sp. z o.o.；2012-08-24；NIP 6272733091；REGON 243016429；ul. Słoneczna 4, 40-135 Katowice；资本 15 tys. zł；**Prezes Maciej Prandota（2015-07 起）**；Henryk Tadeusz Prandota prokura 2016-12 起；最近登记 2026-05-05）+ imsig KRS 0000619990（TAYAMA Sp. z o.o. Sp.k.；2016-05-31；NIP 6342182846；46.52.Z 电子 / 电信设备批发）+ bizraport（Sp.k. 营收 1.9 / 3.1 mln zł 区间）+ tayama.pl（legalName TAYAMA GROUP Sp. z o.o.；NIP 6343005879）+ tayamagroup.pl/kontakt（KRS 0000947226；资本 100,000 zł）+ GoWork（GROUP：Prezes Maciej Prandota、Wiceprezes Mirosław Grzegorz Rydzek；关联 Tayama Polska Robert Prandota i Wspólnicy sp.j.；m.prandota@tayama.pl 公开）',
    url='https://rejestr.io/krs/430899/tayama',
    number='KRS 0000430899（Sp. z o.o.）/ 0000619990（Sp.k.）/ 0000947226（GROUP）', status='Active（三实体）', incorporated='2012-08-24 / 2016-05-31 / 2021–2022（GROUP）', company_type='Sp. z o.o. + Sp.k. + GROUP Sp. z o.o.（Prandota 家族）',
    sic=['46.52.Z 电子 / 电信设备批发（自有品牌 Tayama CCTV 摄像机 / 录像机 / 电源 / PoE 机箱）'],
    address='ul. Słoneczna 4, 40-135 Katowice', accounts='Sp.k. 营收 1.9–3.1 mln zł（bizraport 区间）', accounts_due='—', size_band='小型（家族三实体；人数未取）',
    officers=['Maciej Prandota — Prezes Zarządu（Sp. z o.o. + GROUP）= 拍板人（m.prandota@tayama.pl 第三方目录公开）', 'Mirosław Grzegorz Rydzek — Wiceprezes（GROUP）', 'Henryk Tadeusz Prandota — Prokurent', 'Robert Prandota — sp.j. 合伙人'], psc='Prandota 家族', charges='', prev_names=[],
    lines=['**自有品牌 CCTV + 研究档「商用 PoE 比较多、外壳 / 机箱」= 已在贴牌** → **OEM 30%**：STC-028GP / STC-228GP / STC-2224GP 贴 Tayama 标，写 Prezes Maciej Prandota',
           '家族三实体并存（2021–22 新设 GROUP）= 重组期，采购仍在 Maciej 手里 → 一个收件人即可',
           '规模小（Sp.k. 1.9–3.1 mln zł）→ 先款后货、MOQ 1；发信窗口 Thu 12–14 CET'],
    notes='GROUP 成立日按 KRS 0000947226 号段推定 2021–2022；未取精确日。')

# ---------------- TR 1（未命中） ----------------
put('SB-718', key='tr', batch=B, name='Düzgün Toptan Ticaret（teksarf.com；gmail 名片户）— 1 次检索未命中', iso='TR', fetched=F,
    source='TR · 1 次检索「Düzgün Toptan Ticaret teksarf.com」→ 结果全是无关 toptan 安防批发站（ZTech / Toptan Sarf / NR Güvenlik 等）→ 未命中即停',
    url='', number='未取', status='未取', incorporated='未取', company_type='未取（疑个体 / 家族批发）',
    sic=['安防耗材批发（研究档）'], address='未取', accounts='—', accounts_due='—', size_band='未取',
    officers=['Düzgün 家族业主（姓名待核）'], psc='', charges='', prev_names=[],
    lines=['gmail 名片户、1 次未命中 → 标「底数不可查（名片户）」，不再查；B 不动'],
    notes='side leads：ZTech / Starlink Güvenlik（土耳其本土品牌，进口方 Zerginar Dış Ticaret）、Toptan Sarf（Bahçelievler）、Securitech A.Ş.（2018，Muammer Korkmaz）—— 不在库，仅记。')

# ---------------- 补项 3 ----------------
put('SB-906', key='pl', batch=B, name='Avizio（avizio.pl）= A-LAN Technologie / AICOM 自有 CCTV 品牌 → 并线 SB-445', iso='PL', fetched=F,
    source='PL · 直查 ×2：avizio.pl/kontakt → 404；avizio.pl 根域名 → 302 跳转 a-lan.pl（A-LAN Technologie：图片资源来自 aicom.pl；品牌墙 A-LANTEC / WireArte / Kerpen / **Avizio CCTV / Avizio Power** / Q-lantec；Ruijie Reyee 波兰授权分销；Forbes 2025 家族企业 50 强；NASK 校园 LAN 项目机柜）',
    url='https://a-lan.pl/',
    number='= SB-445 AICOM（KRS 0000654397）', status='Active（a-lan.pl 2026 更新）', incorporated='— 见 SB-445', company_type='品牌（非独立法人）',
    sic=['CCTV / 电源自有品牌（A-LAN 集团）'], address='= SB-445', accounts='—', accounts_due='—', size_band='= SB-445',
    officers=['= SB-445'], psc='= SB-445', charges='', prev_names=[],
    lines=['**直查坐实：avizio.pl 直接跳到 a-lan.pl（A-LAN Technologie = AICOM 体系）→ SB-906 并线 SB-445，只跟一条线**',
           'A-LAN 是 Ruijie Reyee 波兰授权分销 + 自有布线品牌 → 交换机货架有 Ruijie，Saga 只能补「自有品牌 Avizio PoE」贴标一条线 OEM 30%（走 SB-445）'],
    notes='并线 SB-445；不再单独查。')
put('SB-585', key='pl', batch=B, name='VIDOS Sp. z o.o.（vidos.pl；Sokołów / Komorów）— 补项：zarząd + 2025 财报', iso='PL', fetched=F,
    source='PL · rejestr.io 直页 KRS 0000857683（VIDOS SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ；NIP 5342626018；REGON 386943260；Sokołowska 44, Sokołów, 05-806 Komorów；2020-09-03 登记；资本 5 tys. zł；**Prezes Zarządu Zhaoping Wei（80% 股东 / 实际受益人）+ Członek Zarządu Aneta Bogumiła Kaczmarczyk Wei（20%）**，两人均自 2020-09-03 起；2025 财报：营收 29.6 mln zł、成本 26.4 mln、净利 2.5 mln、资产 10.5 mln；主业 46 批发；最近登记 2026-07-17）',
    url='https://rejestr.io/krs/857683/vidos',
    number='KRS 0000857683 / NIP 5342626018 / REGON 386943260', status='Active（VAT czynny）', incorporated='2020-09-03', company_type='Sp. z o.o.（资本 5,000 zł；华人老板 Zhaoping Wei 80% + 配偶 20%）',
    sic=['46 批发（视频对讲 / 门禁 / CCTV 自有品牌 Vidos）'],
    address='Sokołowska 44, Sokołów, 05-806 Komorów（华沙西郊）', accounts='2025：营收 29.6 mln zł、净利 2.5 mln zł（利润率 8.4%）', accounts_due='已递交 2025 年报', size_band='小型（营收 ≈€7M；人数付费未取）',
    officers=['Zhaoping Wei — Prezes Zarządu / 80% 股东 / 实际受益人（华人老板）', 'Aneta Bogumiła Kaczmarczyk Wei — Członek Zarządu / 20%'], psc='Zhaoping Wei 80% + Aneta Kaczmarczyk Wei 20%', charges='', prev_names=[],
    lines=['**老板是华人（Zhaoping Wei）、2020 年新法人、2025 年营收 2,960 万 zł 且盈利** → 自有品牌 PoE 必然已有国内货源 → OEM 30% 概率下调为「一对一替代」：只有比现供更稳的交期 / 更好的 Marvell 管理型才有戏',
           '**可中文直联老板**（例外于常规英文信；由 Simon 决定）；收件人 = 老板本人而非公域 sales',
           '2.5 mln 净利 + 资产 1,050 万 = 有现金、能先款后货；发信窗口 Thu 12–14 CET'],
    notes='第 94 批 aleo 摘要 + 本批 rejestr.io 直页合并；人数需付费。')
put('SB-1046', key='pl', batch=B, name='VOLTA Sp. z o.o.（ivolta.pl；Warszawa）— 补项：zarząd + 2025 年报要点', iso='PL', fetched=F,
    source='PL · rejestr.io 直页 KRS 0000023698（VOLTA SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ；NIP 5211367444；REGON 010829096；Jutrzenki 94, 02-230 Warszawa；2001-06-28 登记；资本 1 mln zł；**Prezes Konrad Ryszard Koperski（2008-07 起）**，Członek Anetta Maria Wójcik（2017-03）/ Dariusz Szewczyk（2019-07）；股东 Janusz Tadeusz Olesiewicz 50% + Konrad Olesiewicz 50%（父子；监事会 Konrad / Anna Olesiewicz + Piotr Stefańczyk）；2025 财报：营收 90.8 mln zł、成本 91.1 mln、**净亏 266.6 tys. zł**、资产 30.4 mln；年报要点：乌克兰战争 + 建筑业低迷拖累；2025 行动 = 成本 / 流程优化、组织调整、**「发展与国内外供应商的合作」**、开拓新市场；公共补助 2020 2.9 mln zł；最近登记 2026-07-09）',
    url='https://rejestr.io/krs/23698/volta',
    number='KRS 0000023698 / NIP 5211367444 / REGON 010829096', status='Active（VAT czynny）', incorporated='2001-06-28', company_type='Sp. z o.o.（资本 1 mln zł；Olesiewicz 父子各 50%；设监事会）',
    sic=['46 批发（安防 / 网络 / 自动化分销：Hikvision / Dahua / Satel 授权）+ 62 软件'],
    address='Jutrzenki 94, 02-230 Warszawa', accounts='2025：营收 90.8 mln zł、净亏 0.27 mln zł（2024 90.85 mln）', accounts_due='已递交 2025 年报（经审计）', size_band='中型（≈€21M；70+ 人）',
    officers=['Konrad Ryszard Koperski — Prezes Zarządu（2008-07 起，职业经理人）', 'Anetta Maria Wójcik — Członek Zarządu（2017-03）', 'Dariusz Szewczyk — Członek Zarządu（2019-07）', 'Janusz / Konrad Olesiewicz — 股东各 50%（Konrad 兼监事会）'], psc='Olesiewicz 父子 50/50', charges='', prev_names=[],
    lines=['**2025 年报白纸黑字：营收持平、小亏、正在「发展与国内外供应商的合作」+ 开拓新市场** = 分销商在找新货源 / 新毛利 → **分销 20% 值得一封正式信**（写采购 / 产品经理公域，开场点「2025 年报提到拓展供应商」不可写 —— 守规：不向客户引用财报）→ 改为点「Hikvision / Dahua 配套 PoE 的毛利空间」',
           'Prezes Koperski 是 2008 年起的职业经理人，股东 Olesiewicz 父子不管日常 → 收件人 = 采购口，不写股东',
           '小亏不是风险（资产 3,040 万、经审计）；先款后货即可；发信窗口 Thu 12–14 CET'],
    notes='第 94 批 bizraport + 本批 rejestr.io 直页合并。')

print('b95_de_pl_tr ok')
