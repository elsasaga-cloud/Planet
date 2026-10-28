# -*- coding: utf-8 -*-
"""第 103 批（T29-U96，2026-10-28）DE 7 + GB 1 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 103
F = '2026-10-28'

put('SB-675', key='de', batch=B, name='Pan Dacom Direkt GmbH（pandacomdirekt.de；Dreieich bei Frankfurt）— 2002 年成立的传输网络设备开发商 + 系统集成商（WDM SPEED-OTS-5000「Made in Germany」、微波、收发器、加密；2022-01 收购 Pan Dacom Networking AG 多数股权，合称「德国唯一自研软硬件的 IT 系统集成商」）；HRB 35050 Offenbach；GF Dirk Bachmann（2002 起）；**研究档 KP Markus Förster = Prokurist（总代理权人）**', iso='DE', fetched=F,
    source='DE · 1 次检索：companyhouse.de（Pan Dacom Direkt GmbH；Dreieich Plaza 1B, 63303 Dreieich；HRB 35050 Amtsgericht Offenbach am Main；Eintragung 2002-10-17；Kapital 150.000 €；USt-ID DE813529743；GF Dirk Bachmann 2002-10-17 起；Prokuristen Jörg Elsässer、**Markus Förster**、Slavka Geuligova、Christina Jilly、Dr. Melanie Martina Stähler；最后变更 2026-03-10）+ Northdata（HRB 35050；LEI 529900QZSNZ1ZE3HYA38；2002-12-17 登记 GF Dirk Bachmann / Thomas Seel）+ implisense（成立 2002-09-01）+ pandacom.de Impressum（Pan Dacom Networking AG HRB 34647；Vorstand Dirk Bachmann / Thomas Klein）+ finanznachrichten 2022-01（Direkt GmbH 收购 Networking AG 多数股权）',
    url='https://www.companyhouse.de/Pan-Dacom-Direkt-GmbH-Dreieich',
    number='HRB 35050 Amtsgericht Offenbach am Main · USt-ID DE813529743 · LEI 529900QZSNZ1ZE3HYA38', status='Active（2026-03 登记变更）', incorporated='2002-10-17（成立 2002-09-01）', company_type='GmbH（私有；控股 Pan Dacom Networking AG）',
    sic=['传输网络设备自研与销售（WDM、微波、光收发器、加密）+ 企业 / 运营商 / 数据中心网络系统集成（经 Networking AG）'],
    address='Dreieich Plaza 1B, 63303 Dreieich', accounts='股本 150,000 €（营收未取）', accounts_due='—', size_band='中型（集团 ≈200+ 人；推定）',
    officers=['Dirk Bachmann — Geschäftsführer（2002 起；兼 Networking AG Vorstandsvorsitzender）', 'Markus Förster — Prokurist = **研究档 KP 本人**', 'Jörg Elsässer / Slavka Geuligova / Christina Jilly / Dr. Melanie Stähler — Prokuristen'], psc='Dirk Bachmann 体系（推定）', charges='', prev_names=[],
    lines=['**自研传输设备 + 系统集成（同行色彩重；自带交换机线经 Networking AG）→ 低概率** → **一页纸即止，无回复 `不动`**：切口 = 「projects where a value L2+ PoE edge is needed beside your WDM/transport」STC-2224GP / STC-424XGGPM-280W；不加厚；不点名其产品',
           '收件人 foerster@ 点名 Prokurist Markus Förster；表内无跟进 → 首信一页纸；发信窗口 Thu 12–14 CET'],
    notes='低概率（同行 / 系统集成）；一页纸后不动。')
put('SB-707', key='de', batch=B, name='Götz Automation — Dipl.-Ing. (FH) Peter Götz（goetz-automation.de；Heiligkreuzsteinach, Baden-Württemberg）— **一人工程师事务所**（自述「1Mann Ing. Büro」：机器与工业设备自动化设计、SPS 编程、可视化、驱动技术；时薪 79 €）；USt-ID DE216371896；IHK Rhein-Neckar；站点 2007 年版；2008 年阿里巴巴 RFQ 10 台', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（Dipl. Ing. (FH) Peter Götz；Mühlweg 6, 69253 Heiligkreuzsteinach；06220 / 922222；Peter@Goetz-Automation.de；Geschäftsführer Peter Götz；USt-ID DE 216 371 896；Kammer IHK Rhein-Neckar；Stundensatz 79 €/h）+ 官网 Leistungen1（「Götz Automation ist ein 1Mann Ing. Büro」）+ cylex（同址同人）；无 HRB（自由职业 / 个体，不登记）',
    url='http://www.goetz-automation.de/Impressum.htm',
    number='个体 / 自由职业工程师（无 HRB）· USt-ID DE216371896', status='Active（站点在线；内容 2007 年版）', incorporated='未取', company_type='Einzelunternehmen / Freiberufler（Dipl.-Ing. (FH) Peter Götz）',
    sic=['工业自动化工程服务（设计、SPS 编程、可视化、驱动技术、文档、调试）—— 一人事务所'],
    address='Mühlweg 6, 69253 Heiligkreuzsteinach', accounts='—', accounts_due='—', size_band='一人',
    officers=['Peter Götz — Inhaber / Dipl.-Ing. (FH) = 研究档 KP 本人'], psc='Peter Götz', charges='', prev_names=[],
    lines=['**一人工程师事务所，2008 年一次 10 台 RFQ 后无交集 → 采购型 micro → `不动`**（项目来了会自己找；不值 Simon 时间）',
           '若其主动来询：STI-054GP / STI-144GP 单台报价即可（25%）'],
    notes='不动（一人事务所；2008 RFQ）。')
put('SB-539', key='de', batch=B, name='IPCOMM GmbH（ipcomm.de；纽伦堡 — 非 Ebermannstadt）— 2004-01 成立的工业协议网关 / 变电站通信产品开发商（ipConv 网关：IEC 61850 / IEC 60870-5-101/104 / DNP3 等协议转换；能源 / 水 / 燃气公用事业交钥匙方案；工作坊培训）；HRB 31759 Nürnberg；GF Artur Votteler；小型企业；群发 8 次无回复', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Imprint（IPCOMM GmbH；Managing Director Artur Votteler；Walter-Bouhon-Straße 4, 90427 Nuremberg；+49 911 18 07 91-0；Amtsgericht Nürnberg HRB 31759；USt-IDNr. DE813859506）+ 官网 About Us（2004 年初成立；工业网关与网间通信方案；20 年）+ Northdata（2004-01-05 登记，GF Artur Votteler，Kapital 25.000 €，Sitz Erlangen → 2015-05 迁 Nürnberg）+ Creditsafe（HRB 31759 beim Amtsgericht Nürnberg）+ UCAIug IEC 61850 证书 #2059（ipConv Gateway）+ Smart Grid Forums 2023 展商',
    url='https://www.ipcomm.de/article/Impressum/en/sheet.html',
    number='HRB 31759 Amtsgericht Nürnberg · USt-ID DE813859506', status='Active（2023 展会、2025 implisense 在册）', incorporated='2004-01-05', company_type='GmbH（私有）',
    sic=['工业通信协议网关 / 协议转换器开发与销售（能源、水、燃气 SCADA 通信；IEC 61850 认证产品）+ 交钥匙通信方案 + 培训'],
    address='Walter-Bouhon-Straße 4, 90427 Nürnberg', accounts='股本 25,000 €（营收未取）', accounts_due='—', size_band='小型（自称中型；推定 10–30 人）',
    officers=['Artur Votteler — Geschäftsführer（2004 起）'], psc='Artur Votteler（推定）', charges='', prev_names=['Sitz Erlangen（2004–2015）'],
    lines=['**网关制造商，交钥匙方案里的交换机多为变电站级（IEC 61850-3 / IEC 61850 咱们不能声称）→ 守界 + 8 次无回复** → **一页纸即止后 `不动`**：仅提「non-substation edge / office side」STI-144GP / STC-228GP；不加厚',
           '收件人 info@ 点名 GF Artur Votteler；表内「可以着重跟一下」但 8 次群发无回复 → 二次触达一次换切口；发信窗口 Thu 12–14 CET；城市改纽伦堡'],
    notes='低概率（IEC 61850 守界；8 次无回复）；一页纸后不动；城市 = 纽伦堡。')
put('SB-550', key='de', batch=B, name='reichelt elektronik GmbH（原 reichelt elektronik GmbH & Co. KG，2023-08 改制；reichelt.de；Sande, Friesland）— 1969 年创立的大型电子 / 技术产品目录电商（15 万+ SKU；B2B / B2C）；**2010 年起属瑞士 Dätwyler Holding（非家族企业）**；≈280 人（2021），营收 1.76 亿 €（2020）；HRB 219874 Oldenburg；GF Ulf Timmermann；群发 8 次无回复', iso='DE', fetched=F,
    source='DE · 1 次检索：reicheltpedia / reichelt.com Impressum（reichelt elektronik GmbH；Geschäftsführer Ulf Timmermann；Elektronikring 1, 26452 Sande；Amtsgericht Oldenburg HRB 219874；USt-ID DE 259817039；WEEE DE 58715331）+ companyhouse.de（2023-08-31 新登记 GmbH，自 GmbH & Co. KG HRA 200654 改制；Kapital 3.000.000 €；Prokuristin Pia Sylvia Pakusa；最后变更 2026-02-25）+ Wikipedia（1969 成立；2010 Angelika Reichelt 售予 Dätwyler Holding；280 人 2021；176 Mio. € 2020；Sprecher der GF Ulf Timmermann）+ unternehmen24（100–249 人）',
    url='https://www.companyhouse.de/en/Reichelt-Elektronik-GmbH-Sande',
    number='HRB 219874 Amtsgericht Oldenburg（原 HRA 200654）· USt-ID DE259817039', status='Active（2026-02 登记变更）', incorporated='1969（GmbH 2023-08-31 改制登记）', company_type='GmbH（Dätwyler Holding AG 子公司；股本 3,000,000 €）',
    sic=['电子元器件 / IT / 网络 / 工具 / 测量等 15 万+ SKU 目录电商（B2B / B2C；欧洲多国站点）'],
    address='Elektronikring 1, 26452 Sande', accounts='第三方 1.76 亿 €（2020；仅作区间）', accounts_due='—', size_band='大型（100–280 人）',
    officers=['Ulf Timmermann — Geschäftsführer（Sprecher）', 'Pia Sylvia Pakusa — Prokuristin'], psc='Dätwyler Holding AG（瑞士）', charges='', prev_names=['reichelt elektronik GmbH & Co. KG（HRA 200654 Oldenburg）；Verwaltungs-GmbH HRB 130281'],
    lines=['**大型目录电商，新品牌上架走 Produktmanagement / Einkauf 流程，群发 8 次无回复 → 分销 20% 低概率** → **一页纸即止**：切口 = 「a value managed PoE line for your Netzwerk category（对标其在售 TP-Link / Digitus 价）」STC-028GP / STC-228GP / STC-2224GP；提供 EAN / 数据表 / CE 文件包；不加厚',
           '收件人改 Einkauf / Produktmanagement 入口（非 info@）；表内「可以着重跟一下」→ 二次触达一次；发信窗口 Thu 12–14 CET；非家族企业（研究档待修）'],
    notes='分销 20% 低概率（大目录商准入）；一页纸；Dätwyler 子公司。')
put('SB-667', key='de', batch=B, name='Münchner Glasfaser-Technik GmbH（mgt.bayern；Gilching bei München，2022-12 自 München Ubostr. 迁入）— 2018-10-30 成立的光纤 / 通信网络建设与运营公司（章程：Bau und Betrieb von Kommunikationsanlagen — Glasfaser、Netzwerktechnik、Kommunikationstechnik）；HRB 244603 München；GF Richard Verhülsdonk（Inhaber）/ Matthias Sanderbeck / Christoph Gentz；11–50 人；姊妹 Münchner Elektro-Technik GmbH、Glasfaser für Alle GmbH；表内 2 次跟进无回复', iso='DE', fetched=F,
    source='DE · 1 次检索：mgt.bayern Impressum（Münchner Glasfaser-Technik GmbH；Rudolf-Diesel-Straße 12, 82205 Gilching；+49 89 427509510；GF Richard Verhülsdonk, Matthias Sanderbeck, Christoph Gentz；Amtsgericht München HRB 244603）+ Northdata（HRB 244603；2018-11-08 登记；GF Sanderbeck / Verhülsdonk；Kapital 25.200 €）+ implisense（成立 2018-10-30；USt-ID DE322142460；small enterprise）+ Creditreform（2022-12-15 变更：Geschäftsanschrift Gilching；3 GF；3 Gesellschafter）+ companyhouse.de（章程目的；旧址 Ubostr. 21, 81245 München；关联 Münchner Elektro-Technik GmbH）+ LinkedIn（Construction；11–50；Gilching；2018；Richard Verhülsdonk Unternehmensinhaber und GF）',
    url='https://www.mgt.bayern/impressum-und-datenschutz',
    number='HRB 244603 Amtsgericht München · USt-ID DE322142460', status='Active（2022-12 登记变更；站点在线）', incorporated='2018-10-30（登记 2018-11-08）', company_type='GmbH（私有；3 股东）',
    sic=['光纤 / 通信网络建设与运营（FTTH 施工、网络技术、通信技术）+ 电气（姊妹公司）'],
    address='Rudolf-Diesel-Straße 12, 82205 Gilching（旧址 Ubostr. 21, 81245 München）', accounts='股本 25,200 €（营收未取）', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Richard Johannes Verhülsdonk — Geschäftsführer / Inhaber', 'Matthias Sanderbeck — Geschäftsführer', 'Christoph Gentz — Geschäftsführer'], psc='三位 GF（股东）', charges='', prev_names=[],
    lines=['**光纤施工承包商（FTTH 建设）→ 集成商 25% small，交换机为项目附带** → **一页纸即止**：STI-144GP / STC-228GP / STC-110XGE（光纤末端有源）；不加厚；2 次无回复 → 一次后 `不动`',
           '收件人 info@ 点名 Inhaber Richard Verhülsdonk；发信窗口 Thu 12–14 CET；地址改 Gilching'],
    notes='集成商 25% small；一页纸后不动。')
put('SB-753', key='us', batch=B, name='profichip USA, Inc.（profichipusa.com；Alpharetta, Georgia — **国家应为美国，研究档「德国」待核 → country_fix 美国**）— 德国 profichip GmbH（Herzogenaurach；2012 起属 Yaskawa Europe GmbH）的美国销售公司（工业通信 ASIC：PROFIBUS / PROFINET / EtherCAT 控制器、ANTAIOS 实时以太网芯片、开发板）；1 人（第三方）；2009 起；研究档「3 旺工业 FS」与 eu.com 域名为误记', iso='US', fetched=F,
    source='US · 1 次检索：官网首页 / Contact（profichip USA, Inc.；980 Birmingham Rd. #721, Alpharetta, GA 30004；+1 678 880-6910；info@profichipusa.com；库存自 Alpharetta 总部发货）+ 官网 About（profichip 为 Herzogenaurach 私有公司）+ LinkedIn profichip（2012 起属 Yaskawa Europe GmbH；Alpharetta Deerfield Pkwy 办公点）+ RocketReach（profichip USA, Inc.；2009；1 人；$6M 存疑）+ ZoomInfo（Alpharetta GA；ASIC 供应商）+ germanautomation.com（profichip 现为 Yaskawa 公司）；GA SoS 号未取',
    url='https://profichipusa.com/',
    number='GA 公司（SoS 号未取）；母体 profichip GmbH（Yaskawa Europe）', status='Active（站点在线）', incorporated='2009（第三方）', company_type='Corporation（Yaskawa 体系关联销售公司）',
    sic=['工业通信 ASIC / 嵌入式芯片与开发板销售（PROFIBUS、PROFINET、EtherCAT、Mechatrolink）'],
    address='980 Birmingham Rd. #721, Alpharetta, GA 30004（邮箱套房）', accounts='—', accounts_due='—', size_band='一人（美国销售点）',
    officers=['无具名（info@）'], psc='profichip GmbH / Yaskawa Europe GmbH', charges='', prev_names=[],
    lines=['**芯片供应商的 1 人美国销售点（上游同行，不买交换机；表内条目系误记）→ `不动`**；国家改美国，研究档域名 eu.com 误记一并注明',
           '不发信'],
    notes='不动（芯片供应商；误记）；country_fix 美国。')
put('SB-834', key='de', batch=B, name='VIDEOR E. Hartig GmbH（videor.com / eneo-security.com；Rödermark bei Frankfurt）— 1975 年 Ernst Hartig 创办、1987-08-23 登记 GmbH 的专业视频与安防技术分销商（**自有品牌 eneo**：摄像机、NVR、**PoE 交换机 —— 表内「UTEPO 的」= eneo 交换机现由 UTEPO 代工**；外贸型）；HRB 32047 Offenbach；股本 870,000 €；GF Dominik Mizdrak（2021 起）+ Lars Alexander Hagenlocher（2025-03 起；创办人之孙、三代股东）；4 名 Prokuristen；群发 9 次无回复', iso='DE', fetched=F,
    source='DE · 1 次检索：eneo-security.com Impressum（eneo ist eine eingetragene Marke der VIDEOR E. Hartig GmbH；Carl-Zeiss-Straße 8, 63322 Rödermark；GF Lars Hagenlocher, Dominik Mizdrak；+49 6074 888-0；Amtsgericht Offenbach HRB 32047）+ implisense（成立 1987-08-23；Kapital 870.000 €；USt-ID DE113592980；LEI 529900I9XJZT6A9R6M34）+ Creditreform（HRB 32047；2025-03-18 变更：Hagenlocher, Lars Alexander *1995 任 GF；4 Prokuristen + 2 GF；2 Gesellschafter；Außenhandel）+ videor.com Facts（1975 Ernst Hartig 创办）+ protector.de / prosecurity.de 2025-04（Hagenlocher 为创办人之孙、三代股东，原 Aufsichtsratsvorsitzender）+ op-online 2025-06（50 周年）+ Northdata（曾用名 Videor Technical E. Hartig GmbH）',
    url='https://eneo-security.com/de/impressum',
    number='HRB 32047 Amtsgericht Offenbach am Main · USt-ID DE113592980 · LEI 529900I9XJZT6A9R6M34', status='Active（2025-03 登记变更；2025-06 50 周年）', incorporated='1987-08-23（公司 1975 创办）', company_type='GmbH（家族三代持股；股本 870,000 €）',
    sic=['专业视频 / 安防技术分销（自有品牌 eneo：摄像机、录像机、PoE 交换机、配件；第三方品牌；欧洲多国销售）+ 解决方案部门'],
    address='Carl-Zeiss-Straße 8, 63322 Rödermark', accounts='股本 870,000 €（营收未取；推定 50–100 M€ 级）', accounts_due='—', size_band='中型（推定 100–200 人）',
    officers=['Dominik Mizdrak — Geschäftsführer（2021 起）', 'Lars Alexander Hagenlocher — Geschäftsführer / 三代股东（2025-03 起）', 'Ina Hauck — Aufsichtsratsvorsitzende（2024 文件）', '4 名 Prokuristen（姓名未取）'], psc='Hartig / Hagenlocher 家族', charges='', prev_names=['Videor Technical E. Hartig GmbH'],
    lines=['**自有品牌 eneo 已在卖贴标 PoE 交换机（现代工方 UTEPO）→ 贴标 OEM 30% 首选目标，B BIG，加厚**：切口 = 「a second-source managed PoE line under the eneo label — Marvell L2+ STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W + unmanaged STC-028GP / STC-228GP，CE/RoHS，3-year option，MOQ 1」；不点名 UTEPO；9 次群发无回复 → 二次触达必须换成产品经理路径',
           '收件人改 eneo Produktmanagement / Einkauf 入口点名 GF Dominik Mizdrak（经营侧）；发信窗口 Thu 12–14 CET；升 A 候选（回信即 A）'],
    notes='贴标 OEM 30% 首选（eneo 自有标，现 UTEPO 代工）；B BIG；加厚；升 A 候选。')
put('SB-401', key='gb', batch=B, name='SECURASOUND LIMITED（securasound.co.uk；Whitchurch, Shropshire）— 1987-03-17 成立的面向安装商的微型安防设备分销商（CCTV、门禁、门口对讲「Soul」2 线套件；医疗 / 教育 / 住宅）；CH **02111547**；MD / PSC Philip Anthony John Wainwright（b. 1946-06）+ Susan Olga Wainwright（Director / Secretary）；**研究档 KP Jason Wainwright = General Manager（家族二代）**；2–10 人，营收 <£1M；VAT 453682634', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House（SECURASOUND LIMITED 02111547；Private limited Company；Incorporated 1987-03-17；Active；Registered office Thornlea, 165 Wrexham Road, Whitchurch, Shropshire SY13 1JG；Officers Philip Anthony John Wainwright Director b. 1946-06 / Susan Olga Wainwright Director & Secretary b. 1948-06，均 1992-06-14 前任职）+ companycheck（SIC 80200；3 officers）+ Endole（Micro；turnover <£1M；PSC Philip A. J. Wainwright；2 shareholders）+ 官网 About（1987 年由现任 MD Philip Wainwright 创办；Company Number 2111547；VAT 453682634；通信寄 Trading Address）+ LinkedIn（security equipment distributor；The Hollies, Chester Road, Whitchurch SY13 1LZ；2–10；Jason Wainwright — General Manager）+ Kompass（0–9 人；MD Philip Wainwright）',
    url='https://find-and-update.company-information.service.gov.uk/company/02111547',
    number='CH 02111547 · VAT 453682634', status='Active', incorporated='1987-03-17', company_type='Private limited company（Wainwright 家族）',
    sic=['80200 Security systems service activities（实际：面向安装商的 CCTV / 门禁 / 对讲设备分销；Kompass 另列 26400）'],
    address='Reg: Thornlea, 165 Wrexham Road, Whitchurch, Shropshire SY13 1JG；Trading: The Hollies, Chester Road, Whitchurch SY13 1LZ', accounts='Micro（turnover <£1M）', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Philip Anthony John Wainwright — Director / Managing Director / PSC（b. 1946-06；创办人）', 'Susan Olga Wainwright — Director / Company Secretary（b. 1948-06）', 'Jason Wainwright — General Manager = **研究档 KP 本人**（家族二代，实际经营）'], psc='Philip Anthony John Wainwright', charges='', prev_names=[],
    lines=['**微型安装商分销（CCTV + ONV PoE 在售）→ 分销 20% small**：STC-028GP / STC-228GP / STC-2216GP（对标其在售 ONV PoE 价；UKCA/CE）；一页纸；不加厚',
           '收件人 jason@ 点名 General Manager Jason Wainwright；表内「可以多跟进一下」→ 二次触达换切口「a second PoE line beside your current one, DAP UK, MOQ 1」；发信窗口 Thu 12–14 GMT'],
    notes='分销 20% small；一页纸；KP = GM 本人。')
print('b103 DE 7 + GB 1 written')
