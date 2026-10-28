# -*- coding: utf-8 -*-
"""第 103 批（T29-U96，2026-10-28）US 8 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 103
F = '2026-10-28'

put('SB-1030', key='us', batch=B, name='Fibertronics, Inc.（fibertronics.com；Melbourne, Florida）— 2009-06-05 成立的美国定制光纤线缆组件制造商（MTP/MPO、MDC/MMC、FOFCA 柔性光路、MIL-SPEC；TL 9000 / ISO 9001 / AS9100D、ITAR；女性所有小企业；2.5 万平方英尺）；FL Sunbiz **P09000049074**；创办人 Doug & Barbara Larson；11–50 人，$1–4.9M；研究档无 KP', iso='US', fetched=F,
    source='US · 1 次检索：intercreditreport / Sunbiz 摘录（FIBERTRONICS, INC.；Domestic for Profit；Document P09000049074；Date of Incorporation 2009-06-05；FEI 38-3801080；Status Active；Principal 2900 Dusa Dr., Melbourne, FL 32934；Larson Douglas P）+ 官网 About（2009 Melbourne FL 成立；TL 9000 / AS9100D / ISO 9001:2015；ITAR；BABA / TAA 选项；SBA 女性所有小企业）+ Florida Today 转载（创办人 Doug 与 Barbara Larson，车库起家 → North Drive 2.5 万平方英尺）+ LinkedIn（11–50；Melbourne FL；2009）+ Thomasnet（$1–4.9M；Manufacturer / Distributor；Est. 2009）+ Bloomberg（3735 Peacock Dr, Melbourne, FL 32904）',
    url='https://florida.intercreditreport.com/company/fibertronics-inc-p09000049074',
    number='FL Sunbiz P09000049074 · FEI 38-3801080', status='Active', incorporated='2009-06-05', company_type='Florida Profit Corporation（私有；Larson 家族；SBA 女性所有）',
    sic=['定制光纤线缆组件制造（MTP/MPO、MDC/MMC、FOFCA、MIL-SPEC；100% 光学测试）+ 光纤配件分销', '国防 / ITAR 线 —— **守界，不提**'],
    address='2900 Dusa Drive, Melbourne, FL 32934（Bloomberg 列 3735 Peacock Dr, Melbourne, FL 32904）', accounts='第三方 $1–4.9M（仅作区间）', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Douglas P. Larson — 创办人 / 登记负责人', 'Barbara Larson — 创办人 / 所有人（女性所有）'], psc='Larson 家族', charges='', prev_names=[],
    lines=['**光纤组件制造 + 配件分销（表内「线缆 MC switch VC」）→ 分销 20% small**：STI-144GP / STC-228GP / STC-110XGE 作其光纤分销目录的有源配套（MC 替代：光口交换机）；一页纸；**不提国防 / ITAR / TAA**',
           '收件人 sales@ 点名 Owner Barbara Larson / purchasing；表内未跟进 → 首信一页纸；发信窗口 Wed 08–10 ET'],
    notes='分销 20% small；一页纸；国防守界。')
put('SB-984', key='us', batch=B, name='Olson Technology, Inc.（现「Antronix of California（Olson Technology Division）」；olsontech.com；Sierra Village / Mi-Wuk Village, California）— 1985-07 成立的 CATV / FTTH / L-Band 光纤与射频头端设备设计制造商（LaserPlus 光发射机、EDFA、EdgePON、edgeswitch；OEM 射频设计）；Owner-President Thomas R. Olson（1961 年起从业）；11–50 人；群发 11 次无回复', iso='US', fetched=F,
    source='US · 1 次检索：官网 company.html（「Antronix of California, (Olson Technology Division) is a privately held corporation」；CATV 头端产品经分销渠道；OEM 射频设备设计制造；总部 Sierra Village CA，Sonora 收发）+ ZoomInfo（Olson Technology, Inc. 1985-07 成立；Thomas Olson Owner-President；工程实验室 Greenback, Tennessee）+ LinkedIn（Olson Technology Division；11–50；Mi-Wuk Village CA；1984；Thomas Olson Owner-President 1985 起）+ leadiq / prospeo（24926 Highway 108, Mi-Wuk Village, CA 95346；SIC 3663；11–20 人）+ explorium（Sue Olson — Owner and Vice President）+ Crunchbase（Legal Name Olson Technology, Inc.）；CA SoS 号未取',
    url='http://www.olsontech.com/company.html',
    number='CA 公司（SoS 号未取）；现为 Antronix of California 的 Olson Technology Division', status='Active（已并入 Antronix 体系）', incorporated='1985-07', company_type='Corporation（私有；Olson 夫妇；Antronix 关联）',
    sic=['CATV / FTTH / L-Band 光纤与射频头端设备设计制造（光发射机、EDFA、PON、调制解调；OEM 射频设计）'],
    address='24926 Highway 108, Mi-Wuk Village (Sierra Village), CA 95346（Sonora CA 收发；Greenback TN 工程）', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Thomas R. Olson — Owner-President（1985 起）', 'Sue Olson — Owner / Vice President', 'Jerry Thorne — 员工（LinkedIn）'], psc='Olson 夫妇 / Antronix', charges='', prev_names=['Olson Technology, Inc.（现 Antronix of California – Olson Technology Division）'],
    lines=['**自产光设备制造商，以太网交换机 / MC 为边角配套 + 群发 11 次无回复** → **贴标 small：一页纸最后一次后 `when=不动`**（edgeswitch 一类入门交换机可挂其标：STC-028GP / STC-228GP / STI-144GP）',
           '收件人 sales@ 点名 Owner-President Thomas Olson；发信窗口 Wed 08–10 PT'],
    notes='贴标 small；一页纸一次后不动；11 次无回复。')
put('SB-1034', key='us', batch=B, name='GSS / GOGSS（gogss.com；Fresh Meadows, New York + City of Industry, CA + Westbury NY + Orange NJ）— 2015 年起的「工厂直采备货进口商」型安防批发商（Global Security Solution USA Inc. / 站点法律页写 Allspec Security NY, Inc.；自有 BLUE|LINE / GREY|LINE 品牌 NVR / 摄像机 / PoE 交换机，专为分销做通用与 OEM 贴标品）；11–50 人；Owner Gary Greve；**研究档 KP Tina = Hong (Tina) Chen，Sales Manager GSS New York**；NY DOS 号未取 → 部分坐实', iso='US', fetched=F,
    source='US · 1 次检索：官网 About（「GSS is a wholesaler of leading security technology products … offers generic and OEM labeled products designed specifically for distribution」；分部 GSS CA 15222 Stafford St, City of Industry, CA 91744；GSS NY 59-43 Fresh Meadow Lane, Fresh Meadows, NY 11365；Long Island 789 Old Country Road Unit 1, Westbury, NY 11590）+ Privacy Policy（版权主体 Allspec Security NY, Inc.，同址 Fresh Meadows）+ Crunchbase（Global Security Solution USA Inc.；sales@gogss.com；Stafford TX 为误标）+ LinkedIn（GSS；Wholesale；11–50；New York；2015；「factory direct stocking importer」；员工 Hong (Tina) Chen — Sales Manager GSS New York；Gary Greve — Owner；Roman K. — Head of R&D）+ 官网 Our Brands（BLUE|LINE IP、GREY|LINE 配件、POE SWITCH、电源）+ whois（gogss.com 2009-09-18 创建）',
    url='https://gogss.com/about-us/',
    number='NY 公司（Global Security Solution USA Inc. / Allspec Security NY, Inc.；DOS 号未取 → 部分坐实）', status='Active（站点 2025 版权）', incorporated='2015（LinkedIn；域名 2009）', company_type='Corporation（私有；Owner Gary Greve）',
    sic=['安防设备进口批发（工厂直采备货；自有通用 / OEM 贴标品牌 BLUE|LINE / GREY|LINE：NVR、摄像机、PoE 交换机、电源、线缆、支架、工具），多州分部'],
    address='59-43 Fresh Meadow Lane, Fresh Meadows, NY 11365（NY 主）；15222 Stafford St, City of Industry, CA 91744；789 Old Country Road Unit 1, Westbury, NY 11590；50 S Center St Unit 8, Orange, NJ 07050', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Gary Greve — Owner', 'Hong (Tina) Chen — Sales Manager, GSS New York（IPVM 认证）= **研究档 KP tina@ 本人**', 'Roman K. — Head of R&D', 'Kai-Hsi Chao — Senior Software Architect'], psc='Gary Greve（推定）', charges='', prev_names=[],
    lines=['**自有贴标安防线（含 PoE 交换机）+ 工厂直采进口商 + 多州仓 → 贴标 OEM 30% 目标**：GSS 标 STC-028GP / STC-228GP / STC-2216GP / STC-2224GP（对标其在售 GREY|LINE PoE 交换机价）；B BIG，**加厚**；华裔销售经理收件 → 英文为主，可备中文直联（Simon 定）',
           '表内未跟进 → 首信即贴标一页纸「a managed L2+ PoE line under your BLUE|LINE label — 3-year option, MOQ 1」；发信窗口 Wed 08–10 ET；升 A 候选（回信即 A）'],
    notes='贴标 OEM 30% 目标；KP = 销售经理本人；B BIG；加厚；升 A 候选；部分坐实（DOS 号）。')
put('SB-1024', key='us', batch=B, name='DOW Technologies = DEDC, Inc.（控股 DOW Equity Holdings, Inc.；dowtechnologies.com；Tampa, Florida）— 1959 年创立（DOW Electronics，2021-03-01 更名）的独立家族技术分销商（定制集成 / AV、12V 车载、卫星电视、安防、网络；站内 Ubiquiti / Luxul / Intellinet PoE 交换机；面向集成商与独立零售商，提供培训与营销支持）；$93.3M、98 人；President & CEO John Yodzis，Executive Chairman Chip Yodzis；研究档无 KP', iso='US', fetched=F,
    source='US · 1 次检索：官网 Executive（Chip Yodzis — Executive Chairman，亦任控股公司 DOW Equity Holdings, Inc. 执行主席，1982 加入岳父 Phil Decker 的 DOW；John Yodzis — President and CEO，2008 加入，2013 主导由卫星电视单渠道转型）+ Tampa Bay Business Journal（$93.3M；98 人；8603 Adamo Dr., Tampa, FL 33619；私有）+ Strata-gee 2022（1959 成立 DOW Electronics；法定实体 **DEDC, Inc.** 官员：John J. Yodzis PCEO、Carolyn D. Yodzis SVP、John P. Yodzis EVP、Daniel T. Carr CFO/VP、Stephen O. Decker VP）+ 官网新闻 2021-03-01（DOW Electronics 更名 DOW Technologies）+ LinkedIn（1959；51–200；Tampa）+ theorg（Dave Elkin — SVP Sales & Product Management；Steve Decker — VP & General Counsel）；FL Sunbiz 文件号未取',
    url='https://www.dowtechnologies.com/executive',
    number='FL 公司 DEDC, Inc.（Sunbiz 文件号未取）；控股 DOW Equity Holdings, Inc.', status='Active（2025 新聘报道）', incorporated='1959（DOW Electronics）', company_type='Corporation（私有；Yodzis / Decker 家族）',
    sic=['技术产品分销与物流（定制集成 AV、12V 车载、卫星电视 / 宽带、安防、网络、VoIP），面向集成商 / 独立零售商；多区域配送中心'],
    address='8603 Adamo Drive, Tampa, FL 33619', accounts='第三方 $93.3M（仅作区间）', accounts_due='—', size_band='中型（98 人）',
    officers=['John J. Yodzis — President & CEO（DEDC, Inc. PCEO）', 'Chip Yodzis — Executive Chairman（DOW Equity Holdings）', 'John P. Yodzis — EVP', 'Daniel T. Carr — CFO / VP', 'Dave Elkin — SVP Sales & Product Management = 供应商准入对口', 'Stephen O. Decker — VP & General Counsel'], psc='Yodzis / Decker 家族', charges='', prev_names=['DOW Electronics（1959–2021）'],
    lines=['**$93M 家族分销商（Ubiquiti / Luxul / Intellinet PoE 在售）→ 分销 20%，低中概率但体量大**：切口 = 「集成商渠道的价值型管理 PoE 线」STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W（对标 Luxul / Intellinet 价）；一页纸 + 产品线卡，加厚一次（供应商准入资料：CE/FCC/RoHS、保修、MOQ 1、美国 DAP）',
           '收件人 info@ / vendor 入口点名 SVP Sales & Product Management Dave Elkin；表内未跟进 → 首信一页纸；发信窗口 Wed 08–10 ET'],
    notes='分销 20%（大分销商，低中概率）；加厚一次；Sunbiz 号下轮补。')
put('SB-1028', key='us', batch=B, name='Fiber Savvy = CRN Solutions, LLC dba Fiber Savvy（fibersavvy.com；Lake Elsinore, California）— CRN Solutions 1996 年起、Fiber Savvy 商号 2009/2010 年起的光纤网络与连接产品分销电商（光缆裁切、跳线、配线、工具、MC / 交换机周边；自有 Fibersavvy 系列；3 万平方英尺仓；少数族裔所有；BICSI 会员；ISO 9001 / 14001）；11–50 人，<$5M；研究档无 KP', iso='US', fetched=F,
    source='US · 1 次检索：官网 About / Terms（「Fiber Savvy is a division of CRN Solutions, LLC」；Master Terms 合同主体 CRN Solutions, LLC dba Fiber Savvy；29415 Hunco Way, Lake Elsinore, CA 92530；951-801-5780；sales@；Wildomar 2 万 → Lake Elsinore 3 万平方英尺仓）+ eBay 店 About（CRN Solutions 1996 成立，多个 DBA；少数族裔所有；BBB 认证；BICSI 会员）+ Yelp（Established 2009）+ photonics.com（Established 2010；20 人；30,000 sq ft）+ GoPhotonics（ISO 9001 / ISO 14001）+ ZoomInfo（11–50；<$5M；1996）+ LinkedIn 个人页（Marketing 2010 起 Wildomar）；CA SoS 号未取',
    url='https://www.fibersavvy.com/pages/about-fiber-savvy',
    number='CA LLC（CRN Solutions, LLC；SoS 号未取）', status='Active（站点在线）', incorporated='1996（CRN Solutions）；Fiber Savvy 商号 2009/2010', company_type='Limited Liability Company（私有；少数族裔所有）',
    sic=['光纤网络与连接产品分销电商（光缆按长度裁切、跳线、配线架、连接器、工具；MC / 交换机周边；自有 Fibersavvy 系列）'],
    address='29415 Hunco Way, Suite F, Lake Elsinore, CA 92530', accounts='第三方 <$5M（仅作区间）', accounts_due='—', size_band='小型（16–20 人）',
    officers=['无具名（研究档无 KP；sales@；LinkedIn 仅「Marketing」）'], psc='未取', charges='', prev_names=['Wildomar, CA 旧址'],
    lines=['**光纤电商 + 自有 Fibersavvy 系列 + MC 周边多 → 分销 20%，可谈 Fibersavvy 标**：STI-144GP / STC-228GP / STC-2224GP / STC-110XGE（光口交换机替代 MC 组合）；一页纸 + 贴标条款，加厚一次',
           '收件人 sales@ 点名 purchasing / owner；表内未跟进 → 首信一页纸；发信窗口 Wed 08–10 PT'],
    notes='分销 20% / 可谈贴标；加厚一次。')
put('SB-1059', key='us', batch=B, name='Neteon Technologies Inc（neteon.net / shopmoxa.neteon.net；North Brunswick / East Brunswick, New Jersey + Brea, California）— 2002-08 成立的工业网络 / 边缘计算分销商（**Moxa Premier Distributor 24 年、连续两届 Moxa Partner Excellence Award**；Cincoze、ASUS IoT）；President Hubert Yu；$7.8M、16 人；SAM UEI X3SPD5JCJD67，CAGE 3DMQ6；研究档无 KP', iso='US', fetched=F,
    source='US · 1 次检索：官网（24+ Years Partnership | Moxa Premier Distributor；Moxa Partner Excellence Award）+ ShopMoxa About（Neteon 子品牌；2002 起授权 Premier Moxa Partner）+ LinkedIn（2002；11–50；North Brunswick NJ；825 Georges Road Suite 3B；Brea CA 2913 Saturn Street Unit F）+ Bloomberg（foundingDate 2002-08-12）+ HigherGov（UEI X3SPD5JCJD67；CAGE 3DMQ6；East Brunswick NJ；2002-09 成立，2003-02 联邦注册）+ RocketReach / ZoomInfo（President Hubert Yu；$7.8M；16 人；1 Tower Center Blvd STE 1510, East Brunswick NJ 08816）+ D&B（Brea CA 92821）；NJ 登记号未取',
    url='https://www.highergov.com/awardee/neteon-technologies-inc-12751592/',
    number='NJ 公司（登记号未取）· SAM UEI X3SPD5JCJD67 · CAGE 3DMQ6', status='Active（联邦供应商在册）', incorporated='2002-08-12', company_type='Corporation（私有；President Hubert Yu）',
    sic=['工业网络 / IIoT / 边缘计算分销（Moxa 主线：串口服务器、工业交换机、协议网关、无线；Cincoze 面板 PC；ASUS IoT）+ 应用咨询与技术支持'],
    address='825 Georges Road, Suite 3B, North Brunswick, NJ 08902（另 1 Tower Center Blvd STE 1510, East Brunswick, NJ 08816）；仓 2913 Saturn St Unit F, Brea, CA 92821', accounts='第三方 $7.8M（仅作区间）', accounts_due='—', size_band='小型（16 人）',
    officers=['Hubert Yu — President = 拍板人（研究档无 KP）'], psc='Hubert Yu（推定）', charges='', prev_names=['ShopMoxa（子品牌）'],
    lines=['**深度绑定 Moxa 的首席分销 → 对咱们是「价值线补位」低概率** → **分销 20%，一页纸即止**：STI-054GP / STI-144GP / STI-288DGGPM / STI-0240GE 作其 Moxa 之下的入门价位线（不点名 Moxa）；不加厚',
           '收件人 sales@ 点名 President Hubert Yu；表内无跟进 → 首信一页纸；发信窗口 Wed 08–10 ET'],
    notes='分销 20% 低概率（Moxa 绑定）；一页纸。')
put('SB-1075', key='us', batch=B, name='Silmar Electronics, Inc.（silmarelectronics.com；Miami / Doral, Florida）— 1963-11-13 成立的美国最大独立电子安防分销商之一（CCTV / IP / 门禁 / 消防 / 音视频 / 家庭自动化；9 个网点；古巴裔 Smith 家族二代）；FL Sunbiz **275645**；President & CEO Jorge E. Smith（Jr.），Chairman Carlos J. Smith；51–200 人；研究档仅 marketing@', iso='US', fetched=F,
    source='US · 1 次检索：Sunbiz（SILMAR ELECTRONICS, INC.；Florida Profit Corporation；Document 275645；FEI 59-1028324；Date Filed 1963-11-13；ACTIVE；Principal 3405 NW 113th Court, Miami, FL 33178）+ intercreditreport（注册代理 Smith, Jorge E.；President / Director Jorge E. Smith；Chairman Carlos J. Smith）+ 官网 About（1963 Jorge M. Smith 创办；1968 转批发；1974 停安装专注批发；1986 Ft. Myers 首个外地网点；President and CEO Jorge Smith）+ Security Systems News 2023（60 周年；9 个网点；CEO Jorge Smith Jr.）+ LinkedIn（1963；51–200；Doral FL；Self-Owned）+ FMCSA SAFER（法定名 SILMAR ELECTRONICS INC；(305) 513-0484）',
    url='https://search.sunbiz.org/Inquiry/CorporationSearch/ByName',
    number='FL Sunbiz 275645 · FEI 59-1028324', status='ACTIVE', incorporated='1963-11-13', company_type='Florida Profit Corporation（私有；Smith 家族）',
    sic=['电子安防 / 低压设备批发分销（CCTV、IP、门禁、消防、A/V、中央吸尘、家庭自动化；9 个网点，面向安装商）'],
    address='3405 NW 113th Court, Miami (Doral), FL 33178', accounts='—', accounts_due='—', size_band='中型（51–200 人；9 网点）',
    officers=['Jorge E. Smith — President & CEO / 注册代理（二代）', 'Carlos J. Smith — Chairman'], psc='Smith 家族', charges='', prev_names=[],
    lines=['**美国最大独立安防分销商之一（表内「PoE 分销」）→ 分销 20%，B BIG，低中概率但一旦入线量大**：STC-028GP / STC-228GP / STC-2216GP / STC-2224GP / STC-4424GCPM（安装商渠道 PoE 全档）；一页纸 + 产品线卡 + 供应商准入资料，加厚一次',
           '收件人改 purchasing / vendor 入口（marketing@ 非采购）点名 President & CEO Jorge Smith；表内未跟进 → 首信一页纸；发信窗口 Wed 08–10 ET；升 A 次候选'],
    notes='分销 20%；B BIG；加厚一次；大分销商准入。')
put('SB-1096', key='us', batch=B, name='West Penn Wire（westpennwire.com；Washington, Pennsylvania）— 1971 年 Claysville PA 创立的低压线缆制造商（AV / 广播 / 安防 / 网络 / 工业；1990 CDT，**2004 起属 Belden 集团（NYSE: BDC）**）；100–249 人，第三方 $26–100M；提供定制标签 / 私标 / 套件；有源副线（MC / 交换机）；研究档无 KP', iso='US', fetched=F,
    source='US · 1 次检索：官网首页 / About（「established in 1971 and is part of the Belden group of companies (NYSE:BDC)」；Washington, PA）+ IPMA / Accu-Tech 历史（1971 Claysville PA 创立；1990 成为首家 Cable Design Technologies 公司 West Penn Wire/CDT；2004 CDT 与 Belden 合并后去掉 CDT）+ 官网新闻 2016（增值服务：定制标签、条码、logo、私标、特殊包装、套件）+ 50 周年博客（1971 家族经营起家；NSCA 创始成员）+ LinkedIn（1971；51–200）+ Manta（Washington PA 15301；$50–100M；100–249 人）+ ZoomInfo（$26.2M；Brian Prusinski — Director, Sales）+ ContactOut（决策人 Glenn Crouse、Mark Sams）；PA 实体号未取',
    url='https://www.westpennwire.com/about.php',
    number='PA 实体（Belden Inc. 旗下；实体号未取）', status='Active（Belden 子品牌）', incorporated='1971', company_type='Belden Inc.（NYSE: BDC）集团成员（上市公司子公司）',
    sic=['低压线缆制造（AV、广播、安防、网络、工业；UTP / 同轴 / 光纤）+ 配件与信号管理；私标 / 定制套件服务'],
    address='Washington, PA 15301（门牌未取）', accounts='第三方 $26–100M（仅作区间）', accounts_due='—', size_band='中型（100–249 人）',
    officers=['Glenn Crouse / Mark Sams — 决策层（ContactOut，职务未核）', 'Brian Prusinski — Director, Sales'], psc='Belden Inc.', charges='', prev_names=['West Penn Wire/CDT（1990–2004）'],
    lines=['**Belden 子公司（集团自有 Hirschmann 工业交换机）→ 有源外采走集团采购，概率低** → **一页纸即止**：STC-228GP / STC-2224GP（AV / 安防线缆配套 PoE，表内「sigmax」在售类）；不加厚；回复即转供应商准入流程',
           '收件人 sales@ 点名 product management（有源配件线）；表内未跟进 → 首信一页纸；发信窗口 Wed 08–10 ET'],
    notes='分销 20% 低概率（Belden 集团）；一页纸。')
print('b103 US 8 written')
