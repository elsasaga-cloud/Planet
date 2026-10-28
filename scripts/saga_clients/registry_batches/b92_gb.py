#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 92 批 · GB 4 户（T29-U88，2026-10-28）：web_search 取号 ×3 + Companies House fetch_page ×5（overview / officers）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 92
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
put('SB-147', key='gb', batch=B, name='Genie Products（genieproducts.co.uk；法定主体 BIOACCESS SALES LIMITED；Stevenage）', iso='GB', fetched=F,
    source='GB · web_search 取号（官网页脚「Registered in England 12058650 · VAT 325 6941 88 · 注册地 c/o Becktech Limited, Chichester」）→ Companies House overview + officers 2 页；LinkedIn 公司页（Stevenage；11–50；设计 / 制造 / 供应生物识别门禁 + IP / HD CCTV；Tek Onbashi 2008 加入）；LeadIQ（≈13 人；Technical Director T.O. / Operations Director A.B. / Export Divisional Director R.H.）。**同名陷阱：GENIE PRODUCTS LTD 16201440（Newquay，2025 新设）/ GENIE PRODUCTS LIMITED 09877102（Uttoxeter，2024 已注销）均非本户**',
    url=CH + '12058650',
    number='12058650（VAT GB 325 6941 88）', status='Active', incorporated='2019-06-19', company_type='Private limited company',
    sic=['26309 其他通信设备制造'],
    address='注册 c/o Becktech Limited, Terminus Road, Chichester PO19 8DW（会计师地址）；营业 Caxton Point Business Centre, Caxton Way, Stevenage SG1 2XU', accounts='至 2025-11-30 已报（微型 / 小型账目）', accounts_due='下期至 2026-11-30，2027-08-31 到期；确认声明 2027-07-02',
    size_band='小型（11–50；LeadIQ ≈13 人）',
    officers=['GORF, Sharon — Director（唯一在任，2023-03-21 起）= 现老板 / 法定代表', 'WEBB, Robert John — Director（2019-06-19 → 2023-03-21 辞）', 'SARGENT, Mark John — Director（2020-03-16 → 2023-03-21 辞）', 'Tek Onbashi — Technical Director（研究档 KP tek@；2008 起在 Genie 品牌，非登记董事）'],
    psc='待补（PSC 页未取；两位创始董事 2023-03 同日辞任 → 推定股权同时转手给 Sharon Gorf 方）', charges='', prev_names=['（品牌 Genie / Genie CCTV 早于 2019 法人；现主体 2019 新设 = 品牌重组）'],
    lines=['**英国「Designed in Britain」安防自有品牌（CCTV + 门禁），Trade Only 只做装机商渠道，全部外采贴标 = OEM 品牌商序列第一位** → OEM 30%：PoE 交换机贴 Genie 标配他们 IP 相机 / NVR 套装；31 封群发打开 1 次 = 读过 → 第二封只给「Genie 标 8/16/24 口 PoE 单价 + 定制 logo / 包装 + UKCA」一页',
           '**2023-03 公司换手**（两位创始董事同日辞任，Sharon Gorf 独任董事）→ 新东家两年内会重审供应链 = 进门时机；研究档 KP Tek Onbashi 是技术总监（老员工、不是董事）→ 他能把样机测过，但签单在 Sharon Gorf / 运营总监',
           '法人 2019 新设 + 微型账目 + 注册地在会计师处 = 规模小、现金流有限 → T/T 50/50、MOQ 1 箱；复盘：2027-08-31 账目到期后看是否仍 Active'],
    notes='')
put('SB-129', key='gb', batch=B, name='Addon Technology Ltd（addon-tech.co.uk；North London）', iso='GB', fetched=F,
    source='GB · 研究档已有公司号 04256748 → Companies House overview + officers 2 页（本批直接取）',
    url=CH + '04256748',
    number='04256748', status='Active', incorporated='2001-07-23', company_type='Private limited company',
    sic=['62090 其他信息技术服务'],
    address='Ground Floor, Building 3, Oakleigh Road South, North London Business Centre, London N11 1GN', accounts='至 2025-03-31 已报', accounts_due='下期至 2026-03-31，2026-12-31 到期；确认声明 2027-08-13',
    size_band='微型（估 2–10 人）',
    officers=['LEE, Wen-Cheng — Director（2006-07-31 起）兼 Secretary（2001-10-27 起；英籍，1965 生；身份已核验）= 老板 = 唯一在任高管', 'LING, Tsuen Her — Director（2001-10-27 → 2015-08-01 辞；同住址 = 家属 / 前合伙人）', '（2001 成立当月的代持董事 / 秘书 RAMM / SHARPE / FIRST SECRETARIES 均同年辞任 = 公司成立时用的代理注册服务）'],
    psc='待补（推定 Wen-Cheng Lee 100%）', charges='', prev_names=[],
    lines=['**台裔（Wen-Cheng Lee）一人公司，2001 起做网络 / 电脑配件分销 24 年，在任董事只他一人** → 他本人就是采购 + 老板；研究档 27 封群发打开 1 次 = 他看过 → 写他本人（Mr Lee），中英皆可但正文仍英文',
           'SIC 62090 是「IT 服务」而网站卖的是配件 = 典型华人小分销（有进口经验、懂中国供应链）→ **分销 20%**（不是 OEM）：报 STC-028GP / STC-228GP / STC-2224GP 三款含税到仓价，MOQ 1 箱，100% 预付',
           '账目微型、注册地商务中心 = 量小但稳定（24 年未断）；复盘 2026-12-31 账目'],
    notes='')
put('SB-206', key='gb', batch=B, name='Brainboxes Limited（brainboxes.com；Speke, Liverpool）', iso='GB', fetched=F,
    source='GB · web_search 取号（Companies House 03245094 + officers 摘要 + companycheck 董事任命日 + Endole 股东 4 / PSC 3 / VAT GB414568352 + RocketReach 管理层 + Crunchbase「1984 创立、Walsh 家族、Made in Britain、终身保修」）→ Companies House overview 1 页',
    url=CH + '03245094',
    number='03245094（VAT GB 414 5683 52；DUNS 525564092）', status='Active', incorporated='1996-09-03（业务 1984 起）', company_type='Private limited company',
    sic=['26512 电子工业过程控制设备制造'],
    address='18 Hurricane Court, Hurricane Drive, Speke, Liverpool L24 8RL（0151 220 2500）', accounts='至 2025-10-31 已报', accounts_due='下期至 2026-10-31，2027-07-31 到期；确认声明 2027-07-25',
    size_band='中小型（估 30–60 人；第三方营收 $7.8M 仅作区间）',
    officers=['WALSH, Eamonn Thomas — Director 兼 Secretary（1996 起；创始人，1955 生；Endole「Founder / Designer」）', 'WALSH, Patricia Anne — Director（1996 起；创始人配偶）', 'WALSH, Luke James — Director（2015-04-20 起）= Managing Director（RocketReach / LinkedIn）= 研究档 KP luke.walsh@', 'WALSH, Joanne — Director（2023-07-11 起）', 'GREER, Stephen John — Director（2023-07-11 起）= Sales Director = 研究档 KP stephen.greer@', 'Kevin Whittaker — Purchasing Manager（RocketReach；非董事）= 采购口', 'Antony McLoughlin — VP of Engineering'],
    psc='3 名控制人（Endole；推定 Walsh 家族）', charges='', prev_names=['BRAIN BOXES LIMITED（1996-09-03 → 2006-09-05）'],
    lines=['**利物浦家族制造商（Walsh 家族，1984 起；自产串口 / 以太网 IO 模块 + 工业交换机，「Made in Britain + 终身保修」是招牌）** → 他们的工业交换机自产 = 我们 STI 对其是竞品而非货源 → **B 不加厚**；唯一缝隙：他们 PoE / 千兆管理型口数少，可问采购经理 Kevin Whittaker 是否补一款 OEM（贴 Brainboxes 标会与「Made in Britain」冲突 → 概率低）',
           '研究档两位 KP（Luke Walsh MD、Stephen Greer 销售总监）都是登记董事 = 信已到顶层；21 封群发无回 = 没需求，不是没看到 → 转季度一封新品 note',
           '2023-07 新增两名董事（Joanne Walsh、Stephen Greer）= 二代 + 销售总监进董事会，公司在交接中；复盘 2027-07-31'],
    notes='守界：同行制造商；不发价格表。')
put('SB-740', key='gb', batch=B, name='Britanic Cabling Production Limited（britaniccablingproduction.com；Northampton）', iso='GB', fetched=F,
    source='GB · web_search 取号（Companies House 12459641；companycheck 董事 Wadii Kherfani 2020-02-12 / Anna Kherfani 2021-05-26；Northdata：Britanic 为 Teltronix Holdings Ltd 12455268 的 PSC 股东（2024-12）；官网 about-us「2004 起、ISO 9000 工厂代工、北安普顿总部 R&D / 库存 / 全球物流」）→ Companies House overview 1 页',
    url=CH + '12459641',
    number='12459641', status='Active', incorporated='2020-02-12', company_type='Private limited company',
    sic=['26309 通信设备制造', '27310 光缆制造', '27320 其他电线电缆制造', '46520 电子与电信设备批发'],
    address='注册 7 Premier Court, Boarden Close, Moulton Park Industrial Estate, Northampton NN3 6LF；营业 Unit 7 Cirrus Park, Lower Farm Road, Northampton NN3 6UR（+44 1604 434188）', accounts='至 2025-03-31 已报', accounts_due='下期至 2026-03-31，2026-12-31 到期；确认声明 2027-03-30',
    size_band='微型 / 小型（估 3–15 人）',
    officers=['KHERFANI, Wadii — Director（2020-02-12 起；1978 生）= 老板 = 联系人', 'KHERFANI, Anna — Director（2021-05-26 起；1985 生）= 配偶 / 合伙人'], psc='待补（推定 Kherfani 夫妇）', charges='', prev_names=['TELTRONIX INTERNATIONAL LIMITED（2020-02-12 → 2021-02-18）'],
    lines=['**夫妻店自有品牌「BCP」结构化布线 + 机柜（自称 British manufacturer，实为 ISO 9000 工厂代工贴标）+ 关联 Teltronix Holdings** → 产品线缺有源设备 → **OEM 30%：BCP 标 PoE 交换机 / 工业 DIN 补他的「end-to-end」方案**；研究档打开 1 次 = 读过',
           '写 Wadii Kherfani 本人（董事 = 采购）；2020 新公司、微型账目 → MOQ 1 箱、T/T 50/50 或 100% 预付',
           '曾用名 Teltronix International + 持股 Teltronix Holdings = 同一老板的多牌子 → 若回信来自 Teltronix 不算新客户；复盘 2026-12-31 账目'],
    notes='')
print('GB 4 ok')
