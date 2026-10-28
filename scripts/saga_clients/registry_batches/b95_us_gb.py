#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 95 批 · US 6 户 + GB 3 户（T29-U89 同轮续做，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。
选户 = 规程 §3「第 95 批」名单：US 按「自有 logo / 牌子」优先；GB 三户先定性（同行？）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 95
CH = 'https://find-and-update.company-information.service.gov.uk/company/'

# ---------------- US 6 ----------------
put('SB-501', key='us', batch=B, name='DITEK Corporation（diteksurgeprotection.com；Largo FL）', iso='US', fetched=F,
    source='US · 1 次检索：diteksurgeprotection.com/about（1988 年海军退伍 Robert (Bob) McIntyre 创立；夫妻 Bob + Joanne；100+ 美国本土员工；女儿 Wendy Gattis = CEO、Melissa Lostraglio = VP Administration；Bob 任 Board Chairman）+ Thomasnet 新闻（2021-03-04 Wendy Gattis 升 CEO）+ Security Systems News 2023-05（107 人）+ LinkedIn（51–200 人；Founded 1988）+ RocketReach（1720 Starkey Road, Largo FL 33771；99 人；$19.9M 第三方估）+ DITEK 2024-Q1 社区稿（Dave Gattis = VP Engineering）',
    url='https://www.diteksurgeprotection.com/about/',
    number='FL 登记号未取（Sunbiz ✗）', status='Active（官网 2026-09 更新；Thomasnet 在册）', incorporated='1988', company_type='Corporation（佛州；家族持有，第二代经营）',
    sic=['浪涌保护器制造（安防 / 消防 / 数据线路）+ 「network solutions」自有标 PoE / 工业交换机线（研究档：PoE 及配件、工业 FS 自有 logo）'],
    address='1720 Starkey Road, Largo, FL 33771', accounts='—（私有）', accounts_due='—', size_band='中型（100–120 人；$20M 级第三方估；50,000 sq ft 自有厂房）',
    officers=['Wendy Gattis — CEO（2021-03 起；创始人之女）', 'Dave Gattis — VP Engineering（产品 / 选型口）', 'Melissa Lostraglio — VP Administration', 'Robert (Bob) McIntyre — Founder / Chairman'], psc='McIntyre / Gattis 家族（推定）', charges='', prev_names=[],
    lines=['**美国本土浪涌保护制造商，交换机不是自产而是贴标外采（研究档「工业 FS 自己的 logo」）→ OEM 30%**：工业 PoE 小口数 + 商用 PoE 给其安防渠道配套；对口是 VP Engineering Dave Gattis（产品）而非销售',
           '家族企业第二代、「坚持美国制造」是其对外叙事 → 发信**只讲部件级配套 + 中性包装 + FCC / CE**，不碰「产地」话题；先款后货、MOQ 1',
           '主业与 Saga 不冲突（我们不做浪涌）→ 可提「互补」：他们的 PoE 浪涌保护 + 我们的 PoE 交换机同一张 BOM；发信窗口 Wed 08–10 ET'],
    notes='FL 实体号未取（Sunbiz ✗）；第三方营收只作区间。')
put('SB-551', key='us', batch=B, name='SanSpot（sanspot.com；Hauppauge NY）— 光纤线缆 / 配线自有品牌，OptoSpan 同门', iso='US', fetched=F,
    source='US · 1 次检索：sanspot.com/about-sanspot（「10 年以上」；30,000 sq ft 纽约仓；经销 OptoSpan / Cisco / Brocade / Finisar 等；地址 125 Kennedy Dr. Suite 500, Hauppauge NY 11788）+ Crunchbase（Hauppauge；11–50 人；sameAs LinkedIn optospan）+ craft.co / salary.com（Founded 2000；旧址 50 Alexander Ct, Ronkonkoma NY 11779）+ WHOIS 镜像（域名 2003-06-15 注册，隐私代理）',
    url='https://www.sanspot.com/about-sanspot',
    number='NY 登记号未取（NY DOS 按法定名查，SanSpot 为品牌名；法定实体疑为 OptoSpan 同一公司）', status='官网在线（2026）', incorporated='2000（第三方）/ 域名 2003', company_type='私有公司（纽约；法定名未取）',
    sic=['光纤跳线 / MPO / 铠装光缆 / 配线架自有品牌（SanSpot + OptoSpan）+ 网络设备转售'],
    address='125 Kennedy Dr, Suite 500, Hauppauge, NY 11788', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Deepali（姓未取）— 研究档 KP deepali@sanspot.com（职务未取）'], psc='未取', charges='', prev_names=[],
    lines=['主品类是光纤线缆 / 配线（Saga 不供）；研究档「MC 自有 logo」→ **只剩 MC + 光口小交换机一条线 OEM 30%**，一页纸即止',
           'SanSpot 与 OptoSpan 同一班人（Crunchbase sameAs）→ 若回信，两牌一并谈；不投第 2 封',
           '法定名未取（品牌名查不到 NY DOS）→ 底数到此为止'],
    notes='NY DOS 需法定名；不再追。')
put('SB-881', key='us', batch=B, name='Nexlar Security, LLC（nexlar.com；Houston TX）', iso='US', fetched=F,
    source='US · 1 次检索：BBB Houston（Nexlar Security, LLC；Business Started 2006-04-20；Incorporated 2007-10-08；LLC；Mr. Rodrigo Lima, Manager；A+）+ nexlar.com 新闻稿 2025-01（创始人 Rodrigo Lima，rod@nexlar.com 公开）+ nexlar.com 博客 2026-08（2825 Wilcrest Dr, Houston；德州执照 #B14634；1,000+ 商业客户）+ LinkedIn（11–50 人；Founded 2007）+ RocketReach（13 人）+ D&B（Key Principal Rod Lima）',
    url='https://www.bbb.org/us/tx/houston/profile/security-systems-consultants/nexlar-security-llc-0915-90015595',
    number='TX 登记号未取（TX SoS 付费；BBB 记 2007-10-08 成立）', status='Active（BBB A+；官网 2026-08 更新）', incorporated='2006-04-20（开业）/ 2007-10-08（LLC）', company_type='Limited Liability Company（德州）',
    sic=['商用安防集成（监控 / 门禁 / 可视对讲 / 自动门 / 虚拟保安）'],
    address='2825 Wilcrest Dr, Suite 170, Houston, TX 77042', accounts='—', accounts_due='—', size_band='小型（13–49 人；<$5M 第三方估）',
    officers=['Rodrigo (Rod) Lima — Founder / Manager（老板；rod@nexlar.com 新闻稿公开）'], psc='Rodrigo Lima（推定）', charges='', prev_names=[],
    lines=['休斯顿安防集成商、老板 Rod Lima 邮箱公开 → **小项目集成商 25%**：商用 PoE（STC-028GP / STC-2224GP）配监控项目，直接写老板',
           '研究档「自有 logo」= 项目贴牌（Alfred360 等自有产品名）→ 可提中性包装；量按项目走，不加厚',
           '德州执照 B14634 = 正规持牌集成商；发信窗口 Wed 08–10 CT'],
    notes='TX SoS 付费未查。')
put('SB-528', key='other', batch=B, name='CommFront Communications Pte. Ltd.（commfront.com）— 实为新加坡公司（美国地址为 Bethesda 虚拟办公室）', iso='SG', fetched=F,
    source='SG · 1 次检索：ACRA 镜像 sgpbusiness / recordowl / sgpgrid（COMMFRONT COMMUNICATIONS PTE. LTD.；UEN 201131527M；2011-10-22 注册；Exempt Private Company；实缴 S$50,100；1 Yishun Industrial Street 1 #05-31 A\'Posh BizHub, Singapore 768160；主业 72102 电子研发；6 名高管 / 2 名股东）+ commfront.com/pages/contact-us（美国 3 Bethesda Metro Center Suite 700 Bethesda MD = 商务中心地址；新加坡 Yishun 地址；「since 2005」）+ ZoomInfo / Datanyze（新加坡；16 人；$4.4M 第三方估；2005）',
    url='https://www.sgpbusiness.com/company/Commfront-Communications-Pte-Ltd',
    number='ACRA UEN 201131527M', status='Live Company', incorporated='2011-10-22（业务自称 2005）', company_type='Exempt Private Company Limited by Shares（新加坡）',
    sic=['72102 电子研发（自有品牌工业串口 / 光纤 / 以太网转换器 + 工业交换机，Shopify 网店直销）'],
    address='1 Yishun Industrial Street 1, #05-31 A\'Posh BizHub, Singapore 768160（美国通讯地址 Bethesda MD 20814）', accounts='—（豁免私人公司）', accounts_due='—', size_band='小型（16 人；$4M 级第三方估）',
    officers=['高管 6 人（ACRA 镜像未列名；付费）'], psc='2 名股东（未列名）', charges='', prev_names=[],
    lines=['**国别更正：美国 → 新加坡**（美国地址只是商务中心）；自有品牌工业转换器 / 交换机制造兼网店 = **准同行**（华南代工为主）→ 不发价格表、B 不动',
           '若要碰只有 OEM 30% 工业 PoE 一条线，但其货源本就在华南 → 低概率，不加厚',
           '发信窗口若用 = 新加坡时区（与我同区）'],
    notes='country_fix 新加坡；高管名单付费未取。')
put('SB-211', key='us', batch=B, name='Eagle Eye Networks, Inc.（een.com；Austin TX）— 2025-12 与 Brivo 合并', iso='US', fetched=F,
    source='US · 1 次检索：Wikipedia（2012 年 Dean Drako（Barracuda 创始人）创立；Austin；487 人（2023）；2023 年 SECOM 投资 $100M；**2025-12 与 Brivo 合并，合并后以 Brivo 名义运营，Drako 任 CEO**）+ Owler（Private Subsidiary of Brivo Systems, LLC）+ BusinessWire 2022-07（2012-07 注册；2,500+ 渠道伙伴；12 个数据中心；Amsterdam / Tokyo / Bangalore 办事处）+ ZoomInfo 2026-04（合并后高管变动：Steven Till 任 President）',
    url='https://en.wikipedia.org/wiki/Eagle_Eye_Networks',
    number='TX / DE 登记号未取', status='Active（合并入 Brivo 2025-12）', incorporated='2012-07', company_type='Inc.（Delaware 推定）；现为 Brivo 集团一部分',
    sic=['云视频监控 VMS / 视频 API（SaaS；自有云桥接盒 + 配套交换机）'],
    address='Austin, TX（总部；具体门牌未取）', accounts='—（私有）', accounts_due='—', size_band='大型（≈500 人；SECOM / 私募股东）',
    officers=['Dean Drako — Founder / CEO（合并后 Brivo CEO；多数股东）', 'Steven Till — President（合并后，原 Brivo 创始人）'], psc='Dean Drako（多数）+ SECOM（2023 投资）', charges='', prev_names=[],
    lines=['**云管理视频监控平台 = 守界（Saga 不做云管理）+ 2025-12 并入 Brivo 大集团** → B 不动、不发',
           '研究档 KP 邮箱 alludolearning.com 与 een.com 无关 = **误归属**（Jaime Becker / Steve Roskowski 不属该公司）→ 标注不发',
           '若日后要碰，只有其云桥接盒配套的 PoE 交换机 ODM 一条线，需工厂级资质 → 不是 Saga 的菜'],
    notes='KP 误归属已标；不再查。')
put('SB-544', key='us', batch=B, name='Mako Networks, Inc.（makonetworks.com；Elgin IL）— 云管理 PCI 网络设备商（2000 年奥克兰创立）', iso='US', fetched=F,
    source='US · 1 次检索：makonetworks.com/about（2000 年 Chris Massam + Simon Gamble 创立；PCI DSS / SD-WAN / 云管理；美国总部 + 英 / 澳 / 新西兰）+ LinkedIn（Elgin IL；51–200 人；Founded 2000）+ Crunchbase（CEO Jason Kubasak；President Simon Gamble；CTO Chris Massam；CFO Mike Bryniarski）+ RocketReach（1355 North McLean Blvd, Elgin IL 60123；77 人；$18.5M 第三方估）+ theorg（Director of Procurement Andrzej Krupa；SVP Sales Todd Vojta = 研究档 KP）+ docs.makonetworks.com（原新西兰 YellowTuna Networks）',
    url='https://makonetworks.com/about/',
    number='IL / NZ 登记号未取', status='Active', incorporated='2000（新西兰 YellowTuna Networks）；美国总部 Elgin IL', company_type='Inc.（美国）+ Mako Networks NZ Limited',
    sic=['云管理网络设备（Mako 系列防火墙 / 交换机 / LTE 失效切换）+ PCI DSS 合规管理服务（零售 / 加油站）'],
    address='1355 North McLean Blvd, Elgin, IL 60123', accounts='—（私有）', accounts_due='—', size_band='中型（75–77 人；$18.5M 第三方估）',
    officers=['Jason Kubasak — CEO', 'Simon Gamble — President / Co-founder', 'Chris Massam — CTO / Co-founder', 'Andrzej Krupa — Director of Procurement（采购口）', 'Todd Vojta — SVP Sales（研究档 KP = 销售，不管采购）'], psc='创始人 + 投资人（未取）', charges='', prev_names=[],
    lines=['**云管理网络 = 守界**（其交换机走自家云平台，需 ODM 固件配合）→ 不发价格表、B 不动',
           '研究档 KP Todd Vojta 是 SVP Sales（卖方），采购口是 Director of Procurement Andrzej Krupa → 若日后碰，只写采购，且只有 ODM 工厂级才有戏 = 不是 Saga 的菜',
           '记档价值：知道它是「同行里的平台商」，别再群发'],
    notes='不再查。')

# ---------------- GB 3 ----------------
put('SB-215', key='gb', batch=B, name='LINDY ELECTRONICS LIMITED（lindy.co.uk；Stockton-on-Tees）— LINDY-Elektronik GmbH（Mannheim）集团英国公司', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 02132710（1987-05-19 注册；Unit 103 Sadler Forster Way, Thornaby, Stockton-On-Tees TS17 9JY；Active；Small；1 项在押抵押）+ Endole（37 人；资产负债表 <£7.5M；4 officers / 3 股东 / 2 PSC；**Darren Neil Casey = Director / Secretary / PSC / Managing Director，1971-01 生**；Lesley Jean Gray；Jurgen Lindenberg 在册）+ lindy.com/global-locations（德国 LINDY-Elektronik GmbH, Markircher Str. 20/22, 68229 Mannheim = 总部；英国 Stockton 公司）+ LEI 529900RIHMCCKO7G8T48（Lindy-Elektronik GmbH；Mannheim；1964-10-20 登记）+ implisense（2023 年资产负债表 €16.1M）',
    url=CH + '02132710',
    number='Companies House 02132710（母公司 Lindy-Elektronik GmbH，Amtsgericht Mannheim；LEI 529900RIHMCCKO7G8T48）', status='Active', incorporated='1987-05-19（英国）；集团 1932 创立 / GmbH 1964 登记', company_type='Private limited company（德国家族集团 Lindenberg 旗下）',
    sic=['46520 电信设备批发（自有品牌 LINDY 线缆 / KVM / 转换器 / 小交换机 / 工业交换机）'],
    address='Unit 103 Sadler Forster Way, Teesside Industrial Estate, Thornaby, Stockton-On-Tees TS17 9JY', accounts='Total Exemption Full；最近账目 2025-06-29 递交', accounts_due='—', size_band='英国公司小型（37 人）；集团中型（€16M 资产负债表 2023）',
    officers=['Darren Neil Casey — Managing Director / Director / Secretary / PSC（= 研究档 KP darren.casey@lindy.co.uk 本人）', 'Lesley Jean Gray — Officer', 'Jurgen Lindenberg — Director（集团家族）'], psc='Darren Neil Casey + 集团（Lindenberg 家族）', charges='1 项在押', charges_note='', prev_names=[],
    lines=['**研究档 KP Darren Casey 就是英国公司 MD + PSC** → 英国渠道拍板人；但 LINDY 产品线由 Mannheim 总部 / 台北采购统一开发 → 英国 MD 能拍「本地库存 / 项目补货」，拍不了贴牌',
           '自有品牌已含交换机 / 工业交换机（亚洲代工）= **OEM 30% 理论对口是 Mannheim 产品管理**，英国线只做分销 20%（SmartByte 品牌补其空白型号：2.5G / 10G 上联 PoE）',
           '发信窗口 Thu 12–14 GMT；一页纸 + 一个问题：「英国仓现有 PoE 型号的交期痛点？」'],
    notes='Mannheim HRB 号两说（LEI 页 HRB 786 / 第三方 HRB 712565）→ 未定，不作底数。')
put('SB-370', key='other', batch=B, name='Wildix（wildix.com）— 总部 Tallinn（Wildix OÜ，VAT EE101984698）/ 运营 Trento（Wildix S.r.l.）；英国 Coventry 办事处', iso='EE', fetched=F,
    source='EE/IT · 1 次检索：wildix.com/about（2005 年 Steve + Dimitri Osler 兄弟创立；Laeva tn. 2, 10111 Tallinn；VAT EE 101984698；100% 渠道）+ wildix.com/it/contatti（Wildix S.r.l. 运营地 Loc. le Basse 3, 38123 Trento）+ LinkedIn（HQ Tallinn；201–500 人；办事处 Trento / Paris / Coventry）+ dealroom（2023 年首轮外部融资 Livonia Partners 私募；2018 起持续盈利）+ Cavell 2025-11（360 人；ARR +36%）+ Wildix 2025-03 新闻稿（Dimitri Osler 任 CIO）',
    url='https://www.wildix.com/about-wildix/',
    number='爱沙尼亚商业登记号未取（VAT EE101984698）；意大利 Wildix S.r.l.（P.IVA 未取）', status='Active', incorporated='2005（Trento）', company_type='OÜ（爱沙尼亚）+ S.r.l.（意大利）+ 多国子公司；私募 Livonia Partners 参股（2023）',
    sic=['UCaaS / VoIP 平台 + 自有品牌话机 / 网关 / PoE 交换机（W-PoE 系列，代工）'],
    address='Laeva tn. 2, 10111 Tallinn, Estonia（运营：Loc. le Basse 3, 38123 Trento, Italy）', accounts='—', accounts_due='—', size_band='中型（360 人；百万级用户）',
    officers=['Steve Osler — CEO / Co-founder', 'Dimitri Osler — CIO / Co-founder（技术 / 产品）'], psc='Osler 兄弟 + Livonia Partners', charges='', prev_names=[],
    lines=['**国别更正：英国 → 爱沙尼亚（总部）**；英国只是办事处；产品 / 采购在 Trento',
           '自有品牌 PoE 交换机是话机配套（代工）→ 理论 OEM 30%，但 360 人集团 + 私募 → 只认工厂级 ODM → **B BIG，一页纸给 Trento 产品部即止**，不加厚',
           '没有 KP → 若发只写 Trento 公域；发信窗口 Thu 12–14 CET'],
    notes='country_fix 爱沙尼亚；登记号未取（爱沙尼亚 e-Business Register 付费 / 需名）。')
put('SB-372', key='gb', batch=B, name='AMG SYSTEMS LIMITED（amgsystems.com；Biggleswade）— 英国工业以太网交换机制造商 = 同行', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 02838846（1993-07-23 注册；3 Omega Centre, Stratton Business Park, Biggleswade SG18 8QB；Active；24 officers / 21 resignations）+ companycheck（现任董事：**Stephen Edwin Clarke 2019-08-09 任，1955-01 生**；Stephen Paul Kummik + Thomas Alexander Exley 2020-02-04 任）+ PSC 页（Edgenet Solutions Limited 11974182 持股 ≥75% + 任免权）+ 2019-08-12 TM01（Allen William Mabbitt 退任）+ Endole（Small；<50 人）+ amgsystems.com 数据表（AMG9HM2P 工业加固 PoE+ 管理型交换机自产）',
    url=CH + '02838846',
    number='Companies House 02838846', status='Active', incorporated='1993-07-23', company_type='Private limited company（Edgenet Solutions Limited 11974182 控股 ≥75%，2019–2020 换手）',
    sic=['工业以太网 / 光纤传输设备设计制造（AMG 系列加固交换机、MC）'],
    address='3 Omega Centre, Stratton Business Park, Biggleswade, Bedfordshire SG18 8QB', accounts='Small（<50 人）', accounts_due='—', size_band='小型（<50 人）',
    officers=['Stephen Edwin Clarke — Director（2019-08-09 任；= 研究档 KP steve.clarke@amgsystems.com 本人）', 'Stephen Paul Kummik — Director（2020-02-04 任）', 'Thomas Alexander Exley — Director（2020-02-04 任）'], psc='Edgenet Solutions Limited（11974182；≥75%）', charges='', prev_names=[],
    lines=['**自产工业以太网交换机 = 同行** → 守界：不发价格表、不加厚、B 不动',
           '研究档 KP Steve Clarke 是董事（2019-08 任，2019–2020 Edgenet 接盘后的管理层）→ 记档：若其日后找「商用 PoE 配套外采」才有戏，等他来',
           '2019-08 / 2020-02 换手完成已 6 年 → 不是进门时机'],
    notes='不再查。')

print('b95_us_gb ok')
