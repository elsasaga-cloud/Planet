#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 92 批 · DE 5 户（T29-U88，2026-10-28）：web_search depth 1 各一次（Northdata / 官网 Impressum 摘要）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 92
put('SB-170', key='de', batch=B, name='Balter GmbH（balter.de / redshop.de；Langenfeld (Rheinland)）', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata（AG Düsseldorf HRB 60247；GF Igor Balter / Eduard Mushkatin；Stammkapital €25,000；2008-12-23 作为 Balter Security GmbH 登记、2009-01 股东名单；LEI 9845005D0A88DC60F633；词标「BALTER」）+ balter.de Impressum（USt DE263994622；WEEE DE 53076790）+ 官网「2006 起 Düsseldorf」+ feinkosten.de 品牌史（由安防批发扩展到 Balter 牌厨电）+ XING（Heiko Mehner、Bauleiter Holger Müller）',
    url='https://www.northdata.com/Balter%20GmbH,%20Langenfeld%20(Rheinland)/Amtsgericht%20D%C3%BCsseldorf%20HRB%2060247',
    number='AG Düsseldorf HRB 60247（USt DE263994622；LEI 9845005D0A88DC60F633）', status='Aktiv', incorporated='2006（业务）/ 2008-12-23 登记为 Balter Security GmbH', company_type='GmbH（Stammkapital €25,000）',
    sic=['安防技术批发 + 自有品牌 BALTER（网络 / HD 视频监控、视频门禁、报警、Smart Home；另有 Balter 牌厨电 + 网店 redshop.de）'],
    address='Elisabeth-Selbert-Str. 19, 40764 Langenfeld (Rheinland)（+49 211 22975914）', accounts='Bundesanzeiger 小型公司简表（未取）', accounts_due='DE：年报次年 12-31 前；3 月复盘',
    size_band='小型（估 10–30 人）',
    officers=['Igor Balter — Geschäftsführer / 创始股东（2006 起）= 老板', 'Eduard Mushkatin — Geschäftsführer / 创始股东（XING 对外联系人）= 老板 = 联系人'], psc='Igor Balter + Eduard Mushkatin（推定两人持股）', charges='', prev_names=['Balter Security GmbH（2008 → 更名 Balter GmbH）'],
    lines=['**两位创始人自有品牌 BALTER（视频监控 / 门禁 / 报警全系贴标，研究档记 Utepo / 洪瑞 PoE）= OEM 品牌商序列第一位，且目前 PoE 货源是深圳同类** → **OEM 30% 一对一替代**：按 balter.de 在售 PoE 型号列对照表（4/8/16 口 + 工业 DIN），贴 BALTER 标、德语包装、CE/RoHS/WEEE 他们已有号',
           '**品牌已外延到厨电（Balter 空气炸锅）** = 安防不再是唯一重心、老板精力分散 → 回信概率中等；写 Eduard Mushkatin（对外口）抄 Igor Balter，一封讲清价差即可',
           '€25k 股本小型 GmbH + 两家网店 = 单笔 $3–10k；T/T 50/50；复盘 2027-03（Bundesanzeiger 2025 年报）'],
    notes='')
put('SB-145', key='de', batch=B, name='DigiComm Gesellschaft für Kommunikationssysteme mbH → AddSecure DigiComm GmbH（digicomm.de；Meerbusch）', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata（AG Neuss HRB 5172；2024-09-25 合并为 AddSecure DigiComm GmbH；2024-05-27 GF Andreas Kluß 接替 Carl von Campe；2021-08 Jörg Brunk 接替 Hans Theo Bongartz）+ LinkedIn（1987；11–50；Breite Str. 10 Meerbusch）+ CB Insights（2023-11 被 AddSecure 收购；工业通信：modem / 路由 / 交换机 / MC）+ finanzen.net OTS（2021 前属 Bechtle 集团）',
    url='https://www.northdata.com/DigiComm%20Gesellschaft%20f%C3%BCr%20Kommunikationssysteme%20mbH,%20Meerbusch/Amtsgericht%20Neuss%20HRB%205172',
    number='AG Neuss HRB 5172（合并后主体 AddSecure DigiComm GmbH，新号未取）', status='Aktiv（2024-09 吸收合并入 AddSecure 德国主体）', incorporated='1987', company_type='GmbH → 集团子公司（AddSecure，瑞典 Castik Capital 旗下）',
    sic=['工业通信 / 远程监控（Fernwirk）设备：modem、路由器、交换机、媒体转换器 + 软件；能源 / 水务客户'],
    address='Breite Str. 10, 40670 Meerbusch（02159 69375-0）', accounts='集团合并报表（AddSecure）', accounts_due='—',
    size_band='小型（11–50）；母公司 AddSecure 1,000+ 人',
    officers=['Andreas Kluß — Geschäftsführer（2024-05 起；AddSecure 任命）', 'Carl von Campe — 前 GF（→ 2024-05）', 'Jörg Brunk — 前 GF（2021-08 → ）', 'Hans Theo Bongartz — 前 GF / 创始世代（→ 2021-08）'], psc='AddSecure Group（2023-11 收购；此前 Bechtle 集团）', charges='', prev_names=['DigiComm GmbH（商号）'],
    lines=['**研究档「自有 logo 工业交换机」成立，但公司已两易其主：Bechtle → 2023-11 AddSecure（瑞典安全通信集团）→ 2024-09 并入 AddSecure DigiComm GmbH** → 采购 / OEM 决策上收集团 = 我们这种体量进不去 → **B「不再补查」**',
           '23 封群发无回符合「集团化后信箱无人管」；不再发；若集团有 OEM 招标另当别论（不会找我们）',
           '复盘：无（挂起）'],
    notes='守界：集团子公司；不发价格表。')
put('SB-213', key='de', batch=B, name='KTI Distribution GmbH Netzwerkkomponentenhandel（kti.de；Bielefeld）', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata（AG Bielefeld HRB 35444；GF Peter Kaiser；Thomas Passlack；Stammkapital 50,000 DEM = 2002 前设立；LEI 5299004AYCZJWJVHYO42；经营范围「网络组件贸易」）+ implisense（小企业；info@kti.de）+ kti.de über-uns / team（25 年独家进口台湾 Katron Technologies Inc.「KTI Networks」产品；团队 Paul Kaiser pkaiser@、Thomas Passlack、Danuta Kaiser；产品页列「OEM & ODM」服务）+ bielefeld.de 企业录',
    url='https://www.northdata.com/KTI%20Distribution%20GmbH%20Netzwerkkomponentenhandel,%20Bielefeld/HRB%2035444',
    number='AG Bielefeld HRB 35444（LEI 5299004AYCZJWJVHYO42）', status='Aktiv', incorporated='≈1998–2001（DEM 股本；官网「25 年」）', company_type='GmbH（Stammkapital 50,000 DEM）',
    sic=['网络组件批发（KTI Networks 台湾品牌 DACH 独家进口：媒体转换器、交换机、工业以太网、光模块）'],
    address='Meisenstraße 79a, 33607 Bielefeld（+49 521 966800）', accounts='小型公司简表（未取）', accounts_due='3 月复盘',
    size_band='微型 / 小型（家族，估 3–10 人）',
    officers=['Peter Kaiser — Geschäftsführer = 老板', 'Paul Kaiser — Management（研究档 KP pkaiser@kti.de；推定二代）', 'Thomas Passlack — Management / 登记人员', 'Danuta Kaiser — 团队（家族）'], psc='Kaiser 家族（推定）', charges='', prev_names=[],
    lines=['**台湾 Katron（KTI Networks，1983）在 DACH 的独家进口 + 品牌代理 = 「captive 分销」**：他们的交换机 / MC / 工业机全部来自 Katron，研究档「自己的牌子」其实是 Katron 的牌子 → **B 不动**；唯一缝隙是 Katron 缺的口型（2.5G PoE / 高瓦 BT），可一句话问 Paul Kaiser 是否补货源',
           '家族微型公司（Kaiser 一家 + Passlack）= 决策快但忠于单一供应商 25 年；打开 1 次无回符合预期',
           '复盘：每年 3 月看 kti.de 产品线是否出现非 Katron 型号（= 开始多货源）'],
    notes='守界：同行品牌代理；不发价格表。')
put('SB-368', key='de', batch=B, name='Welotec GmbH — a Westermo Company（welotec.com；Laer bei Münster）', iso='DE', fetched=F,
    source='DE · 1 次检索：welotec.com Legal notice（GF Dr. Reinhard Lülff、Jos Zenner；AG Steinfurt HRB 3363；USt DE121631449；「a Westermo Company」）+ online-handelsregister（1979-05-15 设立；Stammkapital €67,000）+ companyhouse.de（2025-07-21：Reinhard Lülff 登记为单独代表 GF，Daniel Maurice 退出）+ unternehmen24（2023 年报：总资产 €8.34M，负债 €6.68M）+ westermo.com 2025-04-03 公告（收购 Welotec：≈70 人，2024 营收 ≈ €23.6M）+ majunke（ARTHOS 顾问：2024 营收 ≈ €24M，经营利润率 13.4%，2020 起年均增长 12%）',
    url='https://www.westermo.com/news-and-events/news/2025-04-03-westermo-welotec',
    number='AG Steinfurt HRB 3363（USt DE121631449）', status='Aktiv（2025-04 被 Westermo / Ependion 收购）', incorporated='1979-05-15（业务 1969 起）', company_type='GmbH（Stammkapital €67,000）→ Ependion AB 集团子公司',
    sic=['工业路由器 / 交换机 / 边缘计算 自有品牌（能源、机械制造、OEM、系统集成客户）'],
    address='Zum Hagenbach 7, 48366 Laer（+49 2554 9130-00）', accounts='2023 年报：总资产 €8.34M；2024 营收 ≈ €24M（公告）', accounts_due='集团合并（Ependion，斯德哥尔摩上市）；3 月复盘',
    size_band='中型（≈70 人；营收 €24M）',
    officers=['Dr. Reinhard Lülff — Geschäftsführer（2025-07 起单独代表；Westermo 派驻）', 'Jos Zenner — Geschäftsführer / CTO（2018-03 起 GF；研究档 KP j.zenner@）', 'Daniel Maurice — 前 GF（2018-03 → 2025-07）'], psc='Westermo（Ependion AB，瑞典）2025-04 起 100%；此前 WELOTEC Holding GmbH（HRB 9320 Steinfurt）', charges='', prev_names=[],
    lines=['**2025-04 起属 Westermo（全球头部工业交换机制造商）集团** → 他们的交换机货源 = 母公司 → **B「不再补查」**，研究档 KP Jos Zenner（CTO）不可能外采 PoE 交换机',
           '€24M 营收 / 70 人 = 本就超出我们体量；打开 1 次无回符合预期；不再发',
           '复盘：无（挂起）'],
    notes='守界：同行集团子公司。')
put('SB-698', key='de', batch=B, name='cbo GmbH（cbo-it.de；Schliersee —— 推定匹配）', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata「cbo GmbH, Schliersee」（AG München HRB 93986；原名 cbo Computer- und Bürotechnikvertrieb Oberland GmbH；Miesbacher Str. 16, 83727 Schliersee；股东 BTW-IT GmbH；GF Michael Abel、Thomas Seebauer；Stammkapital 80,000 DEM；经营范围：电脑系统 / 外设 / 软件 / 通信设备销售、规划、维护）。**匹配依据：研究档「主业光模块 / AOC（CBO 品牌）」+ 名称 cbo + 唯一同名 Schliersee 主体；Impressum 未取 → 推定**',
    url='https://www.northdata.com/cbo%20GmbH,%20Schliersee/Amtsgericht%20M%C3%BCnchen%20HRB%2093986',
    number='AG München HRB 93986（推定）', status='Aktiv', incorporated='≈1990 年代（DEM 股本）', company_type='GmbH（Stammkapital 80,000 DEM；股东 BTW-IT GmbH）',
    sic=['光模块 / AOC / DAC 自有品牌 CBO + 网络设备（工业 FS / MC 副线）；IT 系统销售维护（登记范围）'],
    address='Miesbacher Str. 16, 83727 Schliersee（上巴伐利亚）', accounts='小型公司简表（未取）', accounts_due='3 月复盘',
    size_band='小型（估 10–30 人）',
    officers=['Michael Abel — Geschäftsführer', 'Thomas Seebauer — Geschäftsführer', 'Sandra Go — Project Manager（研究档 KP，用户表）'], psc='BTW-IT GmbH（控股公司，推定 Abel / Seebauer 持有）', charges='', prev_names=['cbo Computer- und Bürotechnikvertrieb Oberland GmbH'],
    lines=['**光模块自有品牌商（CBO 标 SFP/QSFP/AOC），交换机只是副线** → Saga 不供光模块（Q-32）→ 对他们只有一条线：**CBO 标工业 / 商用交换机 OEM 30%**（配他们自家光模块卖套装），写两位 GF 之一（Michael Abel）而非项目经理',
           '24 封群发打开 1 次 → 第二封只给「CBO 标 8 口 PoE+2SFP 工业机 $xx / 24 口 +4 SFP 管理型 $xx」两行；MOQ 1 箱',
           '控股结构（BTW-IT GmbH）+ DEM 股本 = 老牌稳健 → T/T 50/50 可谈；复盘 2027-03'],
    notes='推定匹配；回信后用邮件签名 / Impressum 核 HRB。')
print('DE 5 ok')
