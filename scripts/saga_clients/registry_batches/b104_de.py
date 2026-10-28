# -*- coding: utf-8 -*-
"""第 104 批（T29-U97，2026-10-28）DE 4 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 104
F = '2026-10-28'

put('SB-891', key='de', batch=B, name='Tech-Point GmbH（techpoint-gmbh.de；下萨克森 Stuhr；Amtsgericht Walsrode HRB 211027）— 零售与数字标牌行业的全国性技术服务商（规划 / 安装 / 维护 / 维修零售技术系统；前身 Hansebau Krämer，2022 年更名）；创始人 Cedric Krämer + Jussef Hussein 任 Geschäftsführung；股本 €25,000；研究档无 KP；表内未跟进', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata（Tech-Point GmbH, Stuhr；Amtsgericht Walsrode HRB 211027；EUID DEP2716.HRB211027；Managing Director Cedric Krämer；Capital €25,000）+ 官网 Über uns（Jussef Hussein Geschäftsführung；Cedric Krämer Geschäftsführung & Gründer；2022 年由 Hansebau Krämer 更名为 Tech-Point GmbH；Retail- und Digital-Signage-Branche 服务伙伴）+ 官网 Referenzen（专业服务企业：零售领域技术系统规划、安装、维护、维修）；同名 TechPoint GmbH Krefeld（HRB 20968/20969，Ahmet Pinar）、TecPoint GmbH Wolfratshausen（HRB 191653）、Tec-Point GmbH Rheda（HRB 12001）均为他家，不采',
    url='https://www.northdata.com/Tech-Point%20GmbH,%20Stuhr/Amtsgericht%20Walsrode%20HRB%20211027',
    number='HRB 211027（Amtsgericht Walsrode）', status='Active', incorporated='≈2022（更名登记；前身 Hansebau Krämer）', company_type='GmbH（私有；股本 €25,000）',
    sic=['零售 / 数字标牌技术系统的现场服务（规划、安装、维护、维修；全国出勤）'],
    address='Stuhr（下萨克森，不来梅南郊；门牌未取）', accounts='—', accounts_due='—', size_band='小型（推定 10–30 人）',
    officers=['Cedric Krämer — Geschäftsführer & Gründer（Northdata 登记）= 收件人', 'Jussef Hussein — Geschäftsführung（官网）'], psc='Cedric Krämer（推定）', charges='', prev_names=['Hansebau Krämer（2022 年前）'],
    lines=['**现场服务商（交换机为门店项目附带）→ 集成商 25% small，首触一页纸即止**：STC-028GP / STC-228GP（门店 POS / 数字标牌 / 摄像机 PoE）；不加厚；一页纸无回复 → `不动`',
           '收件人 info@ 点名 Cedric Krämer；发信窗口 Thu 12–14 CET'],
    notes='集成商 25% small；一页纸后不动；HRB 已取。')
put('SB-974', key='de', batch=B, name='b-plus 集团（b-plus.com；巴伐利亚 Deggendorf）— 母公司 b-plus GmbH（Amtsgericht Deggendorf HRB 1753；1996-07-17；股本 €62,000；GF Michael Sieg）+ 子公司 b-plus technologies GmbH（HRB 5261；GF Alexander Noack；ADAS / 自动驾驶测试验证数据记录与存储工具、车载 10G/25G 以太网）、b-plus automotive GmbH（HRB 4269；GF Marius Reuther；≈70 人）、b-plus mobile control GmbH（GF Harald Bügel）；研究档无 KP；群发 15 次无回复；表内「可以着重跟一下」', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Impressum（b-plus GmbH Ulrichsberger Straße 17 94469 Deggendorf；HRB 1753；GF Michael Sieg；USt DE 812 023 423 ／ b-plus technologies GmbH HRB 5261 GF Alexander Noack USt DE 815 887 874 ／ b-plus automotive GmbH HRB 4269 GF Marius Reuther）+ Northdata（b-plus technologies GmbH HRB 5261；MD Alexander Noack；ppa Thomas Limbrunner、Michael Sieg；€25,000）+ online-handelsregister（b-plus GmbH HRB 1753；1996-07-17；€62,000）+ 官网新闻（1996 年 Prof. Dr. Böttcher 创立；2005 年 Michael Sieg 接任后发展为四家公司的集团）+ hanser-automotive 2024-02（Marius Reuther 任 b-plus automotive GF；≈70 人；Regensburg + Deggendorf）',
    url='https://www.b-plus.com/de/impressum',
    number='HRB 1753（b-plus GmbH）/ HRB 5261（b-plus technologies GmbH）/ HRB 4269（b-plus automotive GmbH）— Amtsgericht Deggendorf', status='Active', incorporated='1996-07-17（母公司）', company_type='GmbH 集团（私有；四家公司）',
    sic=['汽车 / 越野机械的自动驾驶与 ADAS 开发工具（数据采集记录仪、测量技术、存储、车载以太网 10G/25G、IEC 62443）+ 移动机械控制单元'],
    address='Ulrichsberger Straße 17, 94469 Deggendorf（另 Regensburg / Lindau / Cham 站点）', accounts='—', accounts_due='—', size_band='中型（集团 ≈200 人；automotive ≈70）',
    officers=['Michael Sieg — Geschäftsführer b-plus GmbH（集团）', 'Alexander Noack — Geschäftsführer b-plus technologies GmbH', 'Marius Reuther — Geschäftsführer b-plus automotive GmbH（2024-01 起）', 'Harald Bügel — Geschäftsführer b-plus mobile control GmbH'], psc='Michael Sieg（推定；2005 年管理层收购）', charges='', prev_names=[],
    lines=['**自研 ADAS 测试工具厂商（实验室 / 测试台需 10G/25G 汇聚，车载以太网本身不对口）→ 采购型 / 实验室线，分销 20% 低概率**：STC-110XGE / STI-0240GE / STH-2C24XF-HSI（25G 测试台汇聚）；一页纸（按 Simon「着重跟一下」做一次定向），不加厚；15 次无回复 → 一页纸后 `不动`',
           '收件人 services@ 点名 b-plus technologies 采购 / 测试实验室负责人；发信窗口 Thu 12–14 CET'],
    notes='采购型 / 实验室线 20% 低概率；一页纸后不动；HRB 已取（三家）。')
put('SB-854', key='de', batch=B, name='NetCat SYSTEMS GmbH（netcatsystems.de；北威州 Kamen）— 2003 年成立的 IT 采购 / 供应链服务商（「We supply IT」：Cisco / HP / Lenovo / Ubiquiti 全品类，EOL / EOS 与翻新硬件买卖，ISO 9001:2015，项目型政企与国防行业供货）；CEO Jörg Ridder（= 研究档 KP joerg.ridder@）；LinkedIn 自报 51–200 人（存疑）；HRB 未取 → 部分坐实；群发 15 次无回复；表内「可以着重跟一下」', iso='DE', fetched=F,
    source='DE · 1 次检索：官网首页 / Kontakt（NetCat SYSTEMS GmbH；Weißdornweg 24, 59174 Kamen；+49 2307 96 10-0；sales@；20+ 年；ISO9001:2015）+ 官网 Netzwerk 页（Cisco、Ubiquiti、Airtame；EOL / EOS 稀缺硬件采购；翻新网络硬件买卖）+ LinkedIn 公司页（2003 年成立；IT distribution；Kamen；51–200）+ LinkedIn Jörg Ridder（CEO of NetCat SYSTEMS GmbH；帖文提及 defense industry 供货、OEM 光模块）；HRB（Amtsgericht Hamm 推定）未命中',
    url='https://netcatsystems.de/',
    number='未取（GmbH；Amtsgericht Hamm 推定；部分坐实）', status='Active（LinkedIn 近期发帖）', incorporated='2003', company_type='GmbH（私有）',
    sic=['IT 采购 / 供应链服务（Cisco / HP / Lenovo / Ubiquiti 转售、EOL/EOS 与翻新硬件买卖、OEM 光模块、项目型供货）'],
    address='Weißdornweg 24, 59174 Kamen（NRW）', accounts='—', accounts_due='—', size_band='小型（自报 51–200 存疑；推定 10–30 人）',
    officers=['Jörg Ridder — CEO / Geschäftsführer（LinkedIn）= 收件人（研究档 KP joerg.ridder@）'], psc='Jörg Ridder（推定）', charges='', prev_names=[],
    lines=['**采购型 IT 供货商 + 翻新 / EOL 贩售（半同行）→ 分销 20% 低概率；Simon「着重跟一下」→ 对 CEO 做一次定向一页纸**：STC-2224GP / STC-4424GCPM / STI-288DGGPM（标案里的 Cisco 替代位，强调 3 年保 + 持续供货）；不加厚；15 次无回复 → 一页纸后 `不动`',
           '收件人 joerg.ridder@ 直呼 Jörg；切口「a second-source managed PoE line for your project tenders」；不提国防（守界）；发信窗口 Thu 12–14 CET'],
    notes='分销 20% 低概率；一页纸后不动；部分坐实。')
put('SB-888', key='de', batch=B, name='STORDIS GmbH（stordis.com；巴登-符腾堡 Bad Urach，原斯图加特；Amtsgericht Stuttgart HRB 724261）— 2007 年成立的开放网络 / 白盒交换机增值分销商（「The Open Networking Expert」；600+ 网络产品；Microtel 包探针分销；细分：学术科研、媒体广播、网络安全、运营商、金融交易、国防）；GF Waldemar Scheck；股本 €50,000；11–50 人；英国分公司；研究档 KP Tomasz Sadowski（Technical）/ Mariusz Ślęzak；群发 6 次无回复；表内「AC5 芯片交换机很多，高速」', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 Legal Notice（STORDIS GmbH Ruebteile 24 72574 Bad Urach Hengen；District Court Stuttgart HRB 724261；VAT DE 256406445；Waldemar Scheck）+ implisense（HRB 724261；2007-09-18 登记；€50,000；批发 IT 设备）+ Northdata（Rübteile 24 Bad Urach；MD Waldemar Scheck；字图商标「STORDIS The High Performance DIstributor」）+ webvalid（迁址 Bad Urach；Scheck 单独代表权）+ cylex（2007-10-15 i.G. 登记；原址 Rosenwiesstr. 17 70567 Stuttgart；早期 GF Jeffries Alexander + Scheck Waldemar）+ LinkedIn（2007；11–50；Stuttgart）+ Chelsio 伙伴页（开放网络全服务：咨询、采购、安装、售后）+ 2021-05 新闻稿（Microtel Innovation 10/25/100G 包探针分销）',
    url='https://stordis.com/legal-notice-impressum/',
    number='HRB 724261（Amtsgericht Stuttgart）', status='Active', incorporated='2007-09-18', company_type='GmbH（私有；股本 €50,000）',
    sic=['开放网络 / 白盒交换机与存储的增值分销（咨询 + 采购 + 安装 + 售后；10/25/100G 包探针；曾为存储 VAD）'],
    address='Rübteile 24, 72574 Bad Urach（原 Rosenwiesstr. 17, 70567 Stuttgart）；英国分公司', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Waldemar Scheck — Geschäftsführer（单独代表）= 决策人', 'Tomasz Sadowski — Technical（研究档 KP）', 'Mariusz Ślęzak — 研究档 KP（职务未核）', 'Alexander Jeffries — 早期 GF（已不在册）'], psc='Waldemar Scheck（推定）', charges='', prev_names=['STORDIS GmbH i.G.（2007）'],
    lines=['**开放网络 / 白盒分销商 = STH 高速线的天然渠道 → 分销 20%，B BIG，加厚一次**：STH-2C24XF-HSI（25G/100G 汇聚）/ STH-8C48DX-HSI / STH-32C-HSI（CENTEC 敲门砖）+ STC-448XGGPM 作 10G 接入；强调 1:1 规格书对照与持续供货；不谈国防细分（守界）',
           '收件人 tomasz.sadowski@ 点名 + 抄 info@ 请转 Waldemar Scheck；6 次无回复 → 二次触达换切口「a CENTEC-based 25G/100G line beside your white-box portfolio」；发信窗口 Thu 12–14 CET；升 A 次候选'],
    notes='分销 20%（STH 高速线）；B BIG；加厚一次；升 A 次候选；HRB 已取。')
print('b104 DE 4 written')
