#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 99 批 · DE 4 + GB 4 + PL 4（T29-U92，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 99

# ---------------- DE 4 ----------------
put('SB-1015', key='de', batch=B, name='BR Network Solutions GmbH（br-network-shop.de / br-network.de；Kleve）— 数据网络 / 电信 / 监控技术专业批发商（Fachgroßhandel）+ 自有品牌「BR Network」（自配线缆 / 机柜；3M Volition 主分销）', iso='DE', fetched=F,
    source='DE · 1 次检索：Impressum（BR Network Solutions GmbH, Emmericher Str. 261, 47533 Kleve；Amtsgericht Kleve HRB 3402；GF Wilfried van den Beek, Barthel Robitzsch；USt-ID DE 813 479 263）+ handelsregister.ai（登记 2002-05-28；GF 二人 2004 起；Prokura Gerome Ramakers / Kyra Kubina 2024 起；股东 van den Beek 50% / Robitzsch 50%，各 165k €）+ Northdata（2004-02 登记，原 Sitz Emmerich am Rhein，资本 45k → 65k €）+ Kompass（WZ08 46520 电子元件与电信设备批发；10–19 人）+ 官网 Markenseite（inhabergeführt；20+ 年；合作 3M / Corning / CommScope / Prysmian / KTI Networks / MICROSENS；3M Volition Master Distributor；延续原 Quante AG 机柜产品线）',
    url='https://www.br-network-shop.de/content/2-impressum',
    number='HRB 3402（Amtsgericht Kleve）', status='Active（AGB 2025-09；2024 新增两名 Prokura）', incorporated='2002-05-28（Northdata 2004-02-19 迁址登记）', company_type='GmbH（两位创办人各 50%）',
    sic=['WZ08 46520 电子元件与电信设备批发：数据网络布线 / 电信 / 监控系统（Fachgroßhandel）', '自有品牌 BR Network（自配线缆、机柜、工具）；KTI Networks / MICROSENS 交换机在售'],
    address='Emmericher Straße 261, 47533 Kleve（下莱茵，荷兰边境）', accounts='—（小型 GmbH，Bundesanzeiger 简式）', accounts_due='—', size_band='小型（10–19 人；股本 330k €）',
    officers=['Wilfried van den Beek — Geschäftsführer（2004 起；50%）', 'Barthel Robitzsch — Geschäftsführer（2004 起；50%；网站内容负责人）', 'Gerome Ramakers — Prokura（2024）', 'Kyra Kubina — Prokura（2024）'], psc='van den Beek 50% / Robitzsch 50%', charges='', prev_names=[],
    lines=['**老板直营专业批发 + 自有标「BR Network」+ 已卖 KTI / MICROSENS 交换机** → 分销 20% 为主、贴标 small 为辅（BR Network 标 PoE 交换机补齐其机柜 + 布线套餐）',
           '对口：HRUI STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 对标其 KTI 同级；2024 新任两名 Prokura = 接班梯队，适合「新供应商」议题',
           '收件人：Barthel Robitzsch（GF，网站负责人）；info@br-network.de；发信窗口 Thu 12–14 CET；一页纸'],
    notes='分销 20% + 贴标 small；一页纸。')
put('SB-1039', key='de', batch=B, name='ICO Innovative Computer GmbH（ico.de；Diez, Rheinland-Pfalz）— 1982 年起家的 IT 分销商 / 进口商 + 自产工业 PC / 服务器 / POS（120 人；≈€20M；ISO 9001；20,000 客户，60% 经销商 / 40% 工业客户）', iso='DE', fetched=F,
    source='DE · 1 次检索：Impressum（ICO Innovative Computer GmbH；GF Oliver Schröder, Alexander Solzer；Amtsgericht Montabaur HRB 20217；USt-ID DE 246038247）+ Northdata（HRB 20217；资本 €500,000；曾用名 DRJ GmbH）+ implisense（登记 2005-01-15；2023 资产负债表 €5.03M）+ cylex（2006-03-03 登记；Zuckmayerstr. 15, 65582 Diez）+ wer-zu-wem（120 人；营收档 €10–50M；1982 Klaus Jeschke 创立）+ LinkedIn / 官网（1991 由 Klaus Jeschke Hard- und Software 转为 GmbH；「Distributor und Importeur von Computer- und Kommunikations-Komponenten」；DIN EN ISO 9001:2015；自有装配）+ Wiley 2025（120+ 员工、8 学徒；20,000 客户；2022/23 营收 ≈€20M）',
    url='https://www.ico.de/impressum',
    number='HRB 20217（Amtsgericht Montabaur）', status='Active', incorporated='1982（个体）→ 1991 GmbH → 2005/2006 现登记（原 DRJ GmbH 壳）', company_type='GmbH（资本 €500,000；私有）',
    sic=['IT 分销与进口（服务器、存储、工业 PC、面板 PC、嵌入式、条码 / MDE、POS 组件、医疗 PC）', '自有装配 / 系统集成（Systemhaus）'],
    address='Zuckmayerstraße 15, 65582 Diez', accounts='2023 资产负债表 €5.03M；营收 ≈€20M（2022/23）', accounts_due='—', size_band='中型（120 人）',
    officers=['Oliver Schröder — Geschäftsführer', 'Alexander Solzer — Geschäftsführer', 'Klaus Jeschke — 创办人（1982）'], psc='未取（私有）', charges='', prev_names=['DRJ GmbH（壳名）', 'Klaus Jeschke Hard- und Software（1982–1991）'],
    lines=['**第 99 批 DE 最大户**：自称「Distributor und Importeur」+ 20,000 客户（60% 经销商）+ 自有工业 PC 装配 → **分销 20% 首选（B BIG，升 A 候选）**；进口经验 = 《背景信息》目标顺位第二',
           '对口：工业 PC / 嵌入式客群 → STI-054GP / STI-288DGGPM 工业 PoE；POS / Systemhaus 客群 → STC-228GP / STC-2224GP / STI-0240GE；卖点 = 直接进口价 + 3 年保修 + MOQ 1 试单',
           '收件人：vertrieb@ico.de 点名「Produktmanagement Netzwerk / Einkauf」，抄 GF Oliver Schröder；发信窗口 Thu 12–14 CET；**加厚**（一页规格 + 三档价）'],
    notes='分销 20% 首选；B BIG；升 A 候选；加厚。')
put('SB-1080', key='de', batch=B, name='SPHINX Computer Vertriebs-GmbH（sphinxcomputer.de；Laudenbach bei Weinheim）— 工业通信 / 数据通信分销商（MOXA、Advantech、Perle、Adder、Opengear、Raritan 等；1989）', iso='DE', fetched=F,
    source='DE · 1 次检索：Impressum（SPHINX Computer Vertriebs-GmbH, Heinrich-Lanz-Straße 14, 69514 Laudenbach；GF Hubert Engelhardt；Registergericht Mannheim HRB 431843；USt-ID DE 113585714）+ openregister.de（成立 1989-07-06；GF Hubert Engelhardt 2005-11-18 起（70 岁）；Einzelprokura Markus Brenner 2005 起（63）、Stefanie Engelhardt 2012 起（66）；原资本 300,000 DEM）+ handelsregister.ai（1989-04-25 登记；GF 为 Diplom-Volkswirt，Hemsbach；单独代表，免 §181）+ Creditreform（1 名股东；3 名管理者）+ implisense（股本 €155,000）+ 官网 Über（1989 成立；「führender Distributor von Industrieautomationsprodukten in Europa」；总部与主仓 Laudenbach；自称 19 个欧洲站点）',
    url='https://shop.sphinxcomputer.de/Quick-Links/Impressum/',
    number='HRB 431843（Amtsgericht Mannheim）', status='Active（2020-01 章程修订）', incorporated='1989-04-25', company_type='GmbH（单一股东；家族：Engelhardt）',
    sic=['工业通信 / 数据通信分销：MOXA（工业交换机 / 串口服务器）、Advantech、Perle、Adder、Multitech、Barix、Opengear、Raritan、Server Technology、VXL'],
    address='Heinrich-Lanz-Straße 14, 69514 Laudenbach（Rhein-Neckar）', accounts='—', accounts_due='—', size_band='小型（股本 €155k；人数未取）',
    officers=['Hubert Engelhardt — Geschäftsführer（2005 起；Diplom-Volkswirt；70 岁）', 'Markus Brenner — Einzelprokura（2005 起）= 研究档 KP markus.brenner@', 'Stefanie Engelhardt — Einzelprokura（2012 起）'], psc='Hubert Engelhardt（单一股东，推定）', charges='', prev_names=[],
    lines=['**研究档 KP Markus Brenner 坐实 = 2005 起单独代理权 Prokurist**（相当于总经理级别）→ 收件人正确',
           '但主业是 **MOXA 等品牌工业交换机的正规分销** → 品牌忠诚度高，Saga 只能做「预算线 / 第二来源」→ **分销 20% 低概率，一页纸即止**：STI-054GP / STI-144GP / STI-288DGGPM 对标 MOXA EDS 系列价差（不点名 MOXA）',
           'GF 70 岁 + 女儿 Prokura = 传承期，决策保守；发信窗口 Thu 12–14 CET；不加厚'],
    notes='分销 20% 低概率；KP 坐实；一页纸。')
put('SB-281', key='de', batch=B, name='multiGuide GmbH（multiguide.com；Oberhaching bei München）— 停车引导系统（Parkleitsystem：传感器 / 显示 / 软件）开发与制造商（2011；GF 兼股东 Dr. Roland Kraus，前 Siemens 全球停车业务负责人）', iso='DE', fetched=F,
    source='DE · 1 次检索：Impressum（Multiguide GmbH, Linienstraße 1, 82041 Oberhaching；GF Dr. Roland Kraus；Amtsgericht München HRB 194714；USt-ID DE279778200）+ Northdata（HRB 194714；2011-10-12 登记；资本 €25,000 → €26,596；经营范围「Entwicklung, Produktion, Vertrieb und Wartung von Verkehrssystemen」）+ companyhouse.de（成立 2011-10-17；Prokura Marion Schmitz / Javier Ferre Torres / Annika Heinz）+ firmenwissen（4 名管理者；最近变更 2021-03）+ XING（Dr. Roland Kraus 2012 起 GF；2007–2011 Leiter Urban Parking Siemens AG）+ LinkedIn（11–50 人；Javier Ferre Torres = Produkt Manager Parkleitsystem；Kraus = Geschäftsführender Gesellschafter）',
    url='https://www.multiguide.com/Impressum/',
    number='HRB 194714（Amtsgericht München）', status='Active（2025-08 最近变更）', incorporated='2011-10-17', company_type='GmbH（GF 兼股东 Dr. Roland Kraus）',
    sic=['停车引导系统（单车位传感器、LED 显示、控制器、软件；停车场 / 商场 / 机场）— 开发 / 生产 / 安装 / 维护'],
    address='Linienstraße 1, 82041 Oberhaching（慕尼黑南）', accounts='—（小型 GmbH）', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Dr. Roland Kraus — Geschäftsführender Gesellschafter（2012 起）', 'Javier Ferre Torres — Prokura / Produkt Manager Parkleitsystem = 研究档 KP javier.ferre@', 'Marion Schmitz — Prokura', 'Annika Heinz — Prokura'], psc='Dr. Roland Kraus', charges='', prev_names=[],
    lines=['**研究档 KP Javier Ferre 坐实 = Prokurist + 停车引导产品经理**（选型人）',
           '系统商自用 + 项目配套 → **集成商 25%**：停车场是 PoE 交换机典型场景（传感器 / 摄像机 / 显示屏供电，地下车库宽温）→ STI-054GP / STI-144GP（导轨）+ STC-2224GP（机房）；卖点 = 工业温宽 + 3 年保修 + 小批量',
           '收件人 Javier Ferre Torres；发信窗口 Thu 12–14 CET；一页纸即止（单一行业、量随项目）'],
    notes='集成商 25%；KP 坐实；一页纸。')

# ---------------- GB 4 ----------------
put('SB-1094', key='gb', batch=B, name='VideoBits（videobits.co.uk）= L2tek 的网店，运营主体 Leading Light Technologies Ltd（Lincoln）— 广播 / ProAV 零配件电商（光模块、BNC / SDI / HDMI 延长器、小批量现货）', iso='GB', fetched=F,
    source='GB · 1 次检索：videobits.co.uk 页脚（Leading Light Technologies Ltd；Registered in England & Wales Reg No. 06496207；Reg Office Tower House, Lucy Tower Street, Lincoln LN1 1XW）+ About（「VideoBits is the online store for L2tek」；广播 / ProAV 硬件；小批量 / 样品；英国现货）+ ZoomInfo（<25 人；<$5M；Telecommunication Equipment）+ X 账号（2017-10 上线）',
    url='https://videobits.co.uk/about/',
    number='06496207（Leading Light Technologies Ltd；CH 页未开，页脚自述）', status='Active（站点 2025-07）', incorporated='2008（06496207 号段推定；未开 CH）', company_type='Private limited company（L2tek 品牌 / VideoBits 网店）',
    sic=['广播 / ProAV 硬件电商：光模块（SMPTE 视频 SFP / QSFP）、BNC / 光纤线缆、SDI / HDMI 延长器、视频流系统；小批量'],
    address='Tower House, Lucy Tower Street, Lincoln LN1 1XW（注册处）', accounts='—', accounts_due='—', size_band='微型（<25 人）',
    officers=['未取（研究档无 KP；CH 页未开）'], psc='未取', charges='', prev_names=['L2tek（母品牌）'],
    lines=['**广播 / ProAV 小批量电商**，主营光模块 / 线缆（Saga 不做光模块）→ 唯一切口是 **AV-over-IP 的 PoE 交换机（IGMP / 多播）**：STC-2224GP / STC-424XGGPM-280W → 分销 20% small，一页纸即止',
           '发信窗口 Thu 12–14 GMT；不加厚'],
    notes='分销 20% small；一页纸。')
put('SB-1099', key='gb', batch=B, name='ZXTECH LTD（zxtech.co / zxtechuk.com；注册地 Mayfair 虚拟办公室）— 英国家用安防摄像系统品牌（PoE NVR 套装；经 domar.com 销售；FCA 消费信贷授权）', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House（ZXTECH LTD 12495813；成立 2020-03-03；Berkeley Square House, Berkeley Square, Mayfair, London W1J 6BD；Active；1 名董事）+ Endole（Micro；营业额 <£1M；董事 / PSC Timothy Mak，1980-01 生；2 名股东）+ opengovuk（PSC 75–100% 股权与表决权）+ Northdata（资本 £1.00）+ zxtechuk.com 页脚（FCA 授权号 940104）+ 2020-12 迁址（自 Lansdowne House）',
    url='https://find-and-update.company-information.service.gov.uk/company/12495813',
    number='12495813', status='Active（账目至 2025-12-31）', incorporated='2020-03-03', company_type='Private limited company（Micro；资本 £1）',
    sic=['家用 CCTV 品牌电商（5MP / 4K / 12MP IP 与模拟套装、PoE 摄像机、配套 6 口 PoE 小交换机）；直销 + domar.com'],
    address='Berkeley Square House, Berkeley Square, Mayfair, London W1J 6BD（虚拟办公室；实际仓储未取）', accounts='Micro（营业额 <£1M）', accounts_due='—', size_band='微型（1 董事）',
    officers=['Timothy Mak — Director / PSC（75–100%）'], psc='Timothy Mak', charges='', prev_names=[],
    lines=['**定性：不是同行**，是消费级 CCTV 自有标卖家（Amazon / 自营站套装）；配套 PoE 交换机已随套装从华南采购 → 守界（消费级）+ 微型 → **一页纸即止、不加厚**：若要试探只报 HRUI STC-028GP $28（4/8 口 PoE）贴 Zxtech 标 MOQ',
           '发信窗口 Thu 12–14 GMT；收件人 Timothy Mak（董事本人）'],
    notes='消费级自有标；微型；一页纸。')
put('SB-1019', key='gb', batch=B, name='Connectix Limited（Connectix Cabling Systems；connectix.co.uk；Braintree, Essex）— 英国结构化布线 / 机柜 / 光纤连接制造商（1993；137 人；营业额 £46.3M；Hancock 家族；2026-03 宣布关闭 4 家英国工厂、生产外移印度 / 中国）', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House（CONNECTIX LIMITED 02814569；成立 1993-05-04；500 Avenue West, Skyline 120, Great Notley, Braintree CM77 7AA；Active；董事 Kevin Arthur Hancock 1993 起、Timothy Roland Brown / Mark Hancock / Steven John Hancock 1998-12-01 起；秘书 Sarah Jane Hancock）+ Endole（Medium；137 人；营业额 £46.32M；Kevin Hancock = MD / PSC，1968-01 生）+ LinkedIn（51–200；1993；Structured Cabling / Data Centres / Cabinets / Networking Equipment）+ The Manufacturer 2026-03-16（MD Kevin Hancock：将关闭 4 家英国工厂，生产迁往印度或中国；1999 Daily Mail 奖）+ ContactOut（Tim Dickens = Director of Brands）',
    url='https://find-and-update.company-information.service.gov.uk/company/02814569',
    number='02814569', status='Active（2026-03 重组：生产外移）', incorporated='1993-05-04', company_type='Private limited company（Hancock 家族控股）',
    sic=['结构化布线（Cat 5e–7、OM/OS 光纤）、机柜 / 机箱、光纤连接件、FTTx / 数据中心 / 广播 / 恶劣环境 / 智能家居 — 自有品牌 Connectix，英国研发 + 生产（外移中）'],
    address='500 Avenue West, Skyline 120, Great Notley, Braintree, Essex CM77 7AA', accounts='营业额 £46.32M；137 人（Endole 最新）', accounts_due='—', size_band='中型（137 人；£46M）',
    officers=['Kevin Arthur Hancock — Managing Director / PSC（创办人，1993 起）', 'Timothy Roland Brown — Marketing & Development Director（1998 起）', 'Mark Hancock — Director（1998 起）', 'Steven John Hancock — Director（1998 起）', 'Sarah Jane Hancock — Company Secretary', 'Tim Dickens — Director of Brands', 'Matthew Craig — 研究档 KP matt.craig@（职务未核）'], psc='Kevin Arthur Hancock', charges='', prev_names=[],
    lines=['**第 99 批 GB 最大户、OEM 30% 首选**：自有品牌 Connectix 涵盖「Networking Equipment」，£46M 规模，2026-03 公开宣布把生产外移到印度 / 中国 = **正在找亚洲供应商的窗口期** → Connectix 标 PoE / 管理型交换机补齐其布线 + 机柜套餐；**B BIG，升 A 候选（回信即 A）**',
           '对口：STC-228GP / STC-2224GP / STI-0240GE / STC-424XGGPM-280W（数据中心 / 园区）+ STI 系列（恶劣环境线）；卖点 = Marvell 管理型 + 3 年保修 + 小批量贴标 + 已服务欧洲品牌（不点名）',
           '收件人：Tim Dickens（Director of Brands）主送，Timothy Brown（Marketing & Development Director）抄，研究档 Matthew Craig 保留；**不提**其关厂新闻；发信窗口 Thu 12–14 GMT；**加厚**（一页规格 + 贴标流程 + 三档价）'],
    notes='OEM 30% 首选；B BIG；升 A 候选；加厚。')
put('SB-1045', key='gb', batch=B, name='ITM Components Limited（itm-components.co.uk；Wimborne, Dorset）— 连接 / KVM / AV 延长小众分销商（L-Com、NTI、Extron、Aten、Austin Hughes 等；1991 起；7 人）', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House（ITM COMPONENTS LIMITED 03129914；成立 1995-11-23；10 Whittle Road, Ferndown Industrial Estate, Wimborne BH21 7RU；Active；账目至 2024-05-31，小型豁免；2024-10-28 Ian Flemming 辞任董事 / 秘书 / PSC；2024-09 新章程）+ datalog（董事 Michael John Cook 1997 起；营业额 <£6.5M；<50 人）+ Endole（Michael John Cook 85 岁；1 名股东 / PSC；7 人；现金 £671.87K，同比 −46%；关联 ITM Direct Ltd）+ checkthecompany（1991 起营业；分销 L-Com / NTI / Extron / Ophit / VPI / Gefen / Acces IO / Aten / Austin Hughes / EKS / Hetec / Ingke / Newnex）+ firmbase（7 人）',
    url='https://find-and-update.company-information.service.gov.uk/company/03129914',
    number='03129914', status='Active（2024-10 股权集中至 Michael John Cook）', incorporated='1995-11-23（1991 起营业）', company_type='Private limited company（单一股东）',
    sic=['电子连接 / KVM / AV 延长 / 工控卡分销（L-Com、NTI、Extron、Aten、Austin Hughes 等；定制线缆）'],
    address='10 Whittle Road, Ferndown Industrial Estate, Wimborne, Dorset BH21 7RU', accounts='小型豁免（营业额 <£6.5M）；现金 £672K（2025-05）', accounts_due='2026-02-28（2025 账目）', size_band='微型（7 人）',
    officers=['Michael John Cook — Director / PSC（1997 起；1940-12 生）', 'Ian Flemming — 前董事 / 秘书（1999–2024-10-28 辞任）', 'Neil Stratford / Philip Savill — 研究档 KP（职务未核）'], psc='Michael John Cook（2024-10 起唯一）', charges='', prev_names=[],
    lines=['**微型、85 岁单一股东、合伙人 2024-10 退出、现金减半** → 复利低 → **分销 20% small，一页纸即止**：Aten / NTI 客群配套的 STC-028GP / STC-228GP',
           '收件人：研究档 Neil Stratford / Philip Savill（销售）；发信窗口 Thu 12–14 GMT；不加厚、下轮不追'],
    notes='分销 20% small；一页纸。')

# ---------------- PL 4 ----------------
put('SB-1065', key='pl', batch=B, name='DELTA-OPTI Monika Matysiak sp. z o.o.（原 DELTA-OPTI MATYSIAK sp. k.；delta.poznan.pl / shopdelta.eu；Poznań）— CCTV / 天线 / WLAN 批发 + 零售 + 自产机械配件（桅杆 / 支架）；多语种出口网店', iso='PL', fetched=F,
    source='PL · 1 次检索：shopdelta.eu About Us（Trading Company DELTA-OPTI MATYSIAK SPÓŁKA KOMANDYTOWA, ul. Graniczna 10, 60-713 Poznań；NIP PL 7792602869；REGON 544106600；Design & Manufacturing Company Przedsiębiorstwo Wielobranżowe DELTA Arkadiusz Matysiak NIP 779-000-84-58）+ rejestr.io（KRS 0001225221；sp. z o.o.；2026-03-02 登记；资本 100 tys. zł；Prezes Arkadiusz Jerzy Matysiak、Wiceprezes Monika Małgorzata Matysiak、Członek Arkadiusz Tomasz Topolski）+ krs-pobierz（2026-03-02 注册，2026-03-25 最近变更）+ X @delta_opti（批发 + 零售：监控、报警、Smart Home、电气 / 网络配件、电源）+ shopdelta.eu 数据表页脚（delta-opti@delta.poznan.pl）',
    url='https://rejestr.io/krs/1225221/delta-opti-monika-matysiak',
    number='KRS 0001225221 · NIP 7792602869 · REGON 544106600', status='Active（2026-03 由 sp. k. 转为 sp. z o.o.）', incorporated='sp. k. 期未取 → 2026-03-02 sp. z o.o. 登记', company_type='Spółka z o.o.（Matysiak 家族；资本 100k zł）+ 关联个体制造企业 P.W. DELTA Arkadiusz Matysiak',
    sic=['CCTV（模拟 / AHD / CVI / TVI / IP）、录像机、光纤、放大器、天线 / SAT、WLAN、网络配件批发与零售', '自产机械配件（桅杆、烟囱 / 墙面抱箍、支架、夹具）'],
    address='ul. Graniczna 10, 60-713 Poznań', accounts='—（新主体首年）', accounts_due='—', size_band='小型（人数未取；多语种出口网店 + 自产车间）',
    officers=['Arkadiusz Jerzy Matysiak — Prezes Zarządu（兼 P.W. DELTA 业主）', 'Monika Małgorzata Matysiak — Wiceprezes Zarządu', 'Arkadiusz Tomasz Topolski — Członek Zarządu'], psc='Matysiak 家族', charges='', prev_names=['DELTA-OPTI MATYSIAK SPÓŁKA KOMANDYTOWA'],
    lines=['**家族批发商 + 自产配件 + 多语种出口网店（shopdelta.eu）** → 分销 20%（B BIG 候选）：PoE 交换机是其 CCTV 套餐刚需 → HRUI STC-028GP $28 / STC-228GP $33 / STC-2216GP + 工业 STI-054GP（户外天线 / 桅杆场景）',
           '2026-03 刚改制为 sp. z o.o. = 扩张 / 传承节点，适合「新供应商」议题；收件人 Prezes Arkadiusz Matysiak（delta-opti@delta.poznan.pl）；发信窗口 Thu 12–14 CET；**加厚一次**（规格 + 三档价）'],
    notes='分销 20%；B BIG 候选；加厚。')
put('SB-1095', key='pl', batch=B, name='VIDOM（vidom.pl；LED 照明 + Grenton 智能家居网店，PoE / CCTV / WiFi 为配套）— 官方登记 1 次未命中（检索命中的 VIDOM Systemy Zabezpieczeń sp. z o.o. Mińsk Mazowiecki = vidom.com.pl 同名他户，不采）→ 未坐实', iso='PL', fetched=F,
    source='PL · 1 次检索「Vidom sp. z o.o. KRS NIP vidom.pl」→ 仅命中 vidom.com.pl 的 VIDOM Systemy Zabezpieczeń sp. z o.o.（KRS 0001021691；Mińsk Mazowiecki；Grązka 家族）与其关联公司 —— 域名不同、业务（安防集成）不同于研究档 vidom.pl（LED / Grenton 智能家居网店，邮箱 grenton@）→ 视为同名他户，按规程停；研究档：表内「PoE switch 国内的」「质量一般」',
    url='',
    number='未坐实（vidom.pl 运营主体 NIP / KRS 未取）', status='未核（站点在线 2026-10-21）', incorporated='未取', company_type='未取',
    sic=['LED 照明 / Grenton 智能家居网店（PoE 交换机、CCTV、WiFi 为配套类目）'],
    address='未取', accounts='—', accounts_due='—', size_band='未取（疑微型网店）',
    officers=['未取（研究档无 KP；grenton@ 邮箱）'], psc='未取', charges='', prev_names=[],
    lines=['**未坐实 + 同名陷阱**（vidom.pl ≠ vidom.com.pl）；智能家居网店对 PoE 只是配套且表内「质量一般」→ **一页纸即止**：STC-028GP $28 单品；不加厚、下轮不追'],
    notes='未坐实；同名他户不采；一页纸。')
put('SB-1058', key='pl', batch=B, name='PHU Multiproject（Multiproject Hurtownia Teletechniczna；multiproject.com.pl；Gdańsk）— 弱电 / 安防 / 电子全品类 B2B 批发电商（PLANET 工业 PoE 在售；NIP 5842509422）', iso='PL', fetched=F,
    source='PL · 1 次检索：multiproject.com.pl 页脚（Multiproject Hurtownia Teletechniczna；NIP 5842509422（584 = Gdańsk 税务局号段）；biuro@multiproject.com.pl；具名 Damian Lis 535 840 740 damian.lis@ / Sławomir Janusch 535 840 640 slawek.janusch@）；同名 Multiprojekt（Białystok / Kraków / Wrocław / Szczecin / Radom 多家 sp. z o.o.）均为他户，不采；CEIDG 未查（1 次即停）',
    url='https://www.multiproject.com.pl/',
    number='NIP 5842509422（法律形式未核；「PHU」= 个体商号 Przedsiębiorstwo Handlowo-Usługowe 推定）', status='部分坐实（NIP 已核；站点在线）', incorporated='未取', company_type='推定 JDG / PHU（个体经营）',
    sic=['弱电批发：CCTV / SSWiN / PPOŻ、双绞线 / 网络配件（PLANET IGS-624HPT / GSD-1002M / GSW-4800 在售）、汽车 / 家用电子全品类 B2B 电商'],
    address='Gdańsk（门牌未取）', accounts='—', accounts_due='—', size_band='微型 / 小型（两位具名销售）',
    officers=['Damian Lis — 销售（研究档 KP）', 'Sławomir Janusch — 销售（研究档 KP）'], psc='未取', charges='', prev_names=[],
    lines=['**PLANET 工业 PoE 在售但两款缺货** = 现成替代切口 → **分销 20% small**：STI-288DGGPM $137 对标 PLANET IGS-624HPT（1 350 zł 净 ≈ $335）、STC-110XGE / STC-228GP 对标 GSD / GSW 系列',
           '收件人 Damian Lis（具名销售）；发信窗口 Thu 12–14 CET；一页纸即止（全品类批发，弱电只是一类）'],
    notes='分销 20% small；PLANET 替代切口；一页纸。')
put('SB-1025', key='pl', batch=B, name='ELFON Miękina Sp. K.（原 ELFON BIS Sp. z o.o. Sp. K.；elfon.com.pl；Kraków）— 波兰楼宇对讲 / IP-SIP 可视对讲制造商（2007 起；普通合伙人 ELFON BIS Sp. z o.o.，Prezes Marek Miękina）', iso='PL', fetched=F,
    source='PL · 1 次检索：官网 Polityka / Regulamin / Kontakt（KRS 0000700362；NIP 6792955142；BDO 000010168；ul. Półłanki 27A, 30-740 Kraków，2026-02-01 自 Ruciana 3 迁入；普通合伙人 KRS 0000583435 NIP 6793117911；「polski producent domofonów, wideodomofonów IP/SIP」）+ bizraport（ELFON BIS Sp. z o.o. Sp. K.；登记 2017-10-23；开业 2007-10-12；spółka komandytowa）+ rejestr.io（ELFON MIĘKINA KRS 0000700362 REGON 120559355；ELFON BIS Sp. z o.o. KRS 0000583435 Prezes Marek Andrzej Miękina 2015-10-29 起，资本 5 tys. zł）+ elfon-sklep.pl（ELFON Miękina Sp.K.）',
    url='https://rejestr.io/krs/700362/elfon-miekina',
    number='KRS 0000700362 · NIP 6792955142 · REGON 120559355（GP：KRS 0000583435）', status='Active（2026-02 迁新址；招聘区域销售经理）', incorporated='2007-10-12（开业）/ 2017-10-23（现 sp. k. 登记）', company_type='Spółka komandytowa（普通合伙人 ELFON BIS Sp. z o.o.；Miękina 家族）',
    sic=['楼宇对讲制造：数字 / 模拟 / 两线制对讲、ELFON Optima、IP/SIP 可视对讲、电源 / 继电器（多户住宅 + 独栋）；分销可视对讲、CO / 燃气探测器'],
    address='ul. Półłanki 27A, 30-740 Kraków（2026-02 起）；旧址 ul. Ruciana 3 / ul. Pana Tadeusza 4', accounts='—', accounts_due='—', size_band='小型（人数未取；自有生产 + 区域销售网）',
    officers=['Marek Andrzej Miękina — Prezes Zarządu（普通合伙人 ELFON BIS Sp. z o.o.）= 实控人'], psc='Marek Miękina（推定）', charges='', prev_names=['ELFON BIS Sp. z o.o. Sp. K.'],
    lines=['**本土制造商 + IP/SIP 对讲产品线** → IP 对讲必配 PoE 交换机 → **贴标 small（OEM 30%）/ 配套 25%**：ELFON 标 STC-028GP（8+2，对讲 + 门口机供电）/ STI-054GP（楼道配电箱导轨）随其 IP 系统成套卖给安装商',
           '收件人 Marek Miękina（实控人）抄 biuro@；发信窗口 Thu 12–14 CET；一页纸 + 一张配套图即可（不加厚）'],
    notes='贴标 small / 配套 25%；一页纸。')

print('b99 DE 4 + GB 4 + PL 4 written')
