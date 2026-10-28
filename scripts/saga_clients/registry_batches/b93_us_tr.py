#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 93 批 · US 5 户 + TR 4 户（T29-U88 同轮续做，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 93

# ---------------- US 5 ----------------
put('SB-150', key='us', batch=B, name='Nexxus（nexxus.cc）— 1 次未命中', iso='US', fetched=F,
    source='US · 1 次检索「Nexxus nexxus.cc industrial Ethernet switch」：返回全是同名他户（墨西哥工业地产 Nexxus、马萨诸塞软件 The Nexxus Group、Nexius 电信、护发品牌 Nexxus）；唯一同品类线索 nexxusnetworks.com（「第一家智能 PoE 制造商，17 年」，2024-04）域名不同、未证同一',
    url='https://nexxusnetworks.com/home-2/',
    number='未取', status='未命中（域 nexxus.cc 无法与任何登记主体对上）', incorporated='—', company_type='—',
    sic=['（研究档）ONV 工业 FS 贴自有标'], address='USA（州 / 城市未取）', accounts='—', accounts_due='—', size_band='—',
    officers=[], psc='', charges='', prev_names=[],
    lines=['**一次检索未命中 → 按规程停**；nexxus.cc 与 nexxusnetworks.com 是否同一家待下轮一次直查（Impressum / WHOIS 镜像）',
           '同名陷阱极多（护发品牌 / 地产 / 软件 / 电信），任何第三方「Nexxus」营收 / 人数都不可用',
           '不影响跟进：研究档已有「工业 FS 贴标」兴趣 → 仍按 OEM 30% 一页纸等回信'],
    notes='第 93 批 1 次未命中；下轮若再 1 次不中则永久标「底数不可查」。')
put('SB-353', key='us', batch=B, name='Fiber Optic Cable Shop（fiberopticcableshop.com / FiberMailbox.com；Richmond CA）', iso='US', fetched=F,
    source='US · 1 次检索：fiberopticcableshop.com 首页 + about（1976 年起、三次 INC 500、Richmond CA 地址、Sales@FiberMailbox.com）+ photonics.com 公司页（1976 / 15 人 / 15,000 sq ft / 私有）+ ZoomInfo（8 人；Gerry Schumacher、Paul Fletcher）',
    url='https://www.fiberopticcableshop.com/about-fiber-optic-cable-shop.html',
    number='加州登记号未取（CA SoS 为 JS 页）', status='Active（官网在售、2024-11 快照）', incorporated='1976（业务起点；法人类型未取）', company_type='私有公司（dba Fiber Optic Cable Shop；法定名未取）',
    sic=['光纤跳线 / 配线 / MC / 光纤交换机制造 + 网店零售（SIC 33/335）'],
    address='136 South Second Street, Richmond, CA 94804（800-777-6269 / 510-234-9090）', accounts='—', accounts_due='—', size_band='微型–小型（8–15 人；营收 <$5M 第三方区间）',
    officers=['Mark W（研究档 KP，mark@fibermailbox.com）— 职务未取', 'Gerry Schumacher / Paul Fletcher — ZoomInfo 列为主要员工（职务未取）'], psc='', charges='', prev_names=[],
    lines=['**50 年老店、自产光纤组件 + 自有标 MC / 机架 / 交换机**（研究档「14 槽机架 MC 自己的标」）→ **OEM 30%：MC + 机架式 MC 机箱 + 小口数光纤口交换机**贴他们的标；主品类 SFP / 光缆 Saga 不供，只做交换机 / MC 一条线',
           '8–15 人、老板型公司 → 回信即拍板；写 mark@（研究档已有）抄 Sales@FiberMailbox.com',
           '加州实体 → 发信窗口 Wed 08–10 PT；年度复核看官网是否仍更新'],
    notes='法定名 / 州登记号未取（CA SoS JS）；不再追。')
put('SB-730', key='us', batch=B, name='ITSS Inc.（it2ss.com；Grand Prairie TX）— Alasad 家族多元集团', iso='US', fetched=F,
    source='US · 1 次检索：it2ss.com 首页（2003 年创立；医疗 / 电商 / 建筑 / 安防 IT / 中美跨境多元集团；807 S. Great Southwest Pkwy, Grand Prairie TX 75051；+1 916 238 6844）+ RocketReach VastMed LLC（Jehad Alasad CEO/President，Mahmoud Alasad COO，Grand Prairie）；同名陷阱：ITSS Inc. Goldsboro NC（itss.us，2002）、瑞士 ITSS（银行软件）',
    url='http://it2ss.com/',
    number='TX 登记号未取（TX SoS 付费）', status='Active（官网 2026 在线）', incorporated='2003（自述）', company_type='Inc.（德州公司，法定全名未取）',
    sic=['多元控股：医疗耗材（VastMed）、电商、建筑、安防 / IT、中美跨境贸易'],
    address='807 S. Great Southwest Pkwy, Grand Prairie, TX 75051', accounts='—', accounts_due='—', size_band='微型（安防 / IT 线 ≤10 人；VastMed 9 人）',
    officers=['Jehad Alasad — CEO / President（研究档 KP jalasad@it2ss.com；兼 VastMed LLC CEO）= 老板', 'Mahmoud Alasad — COO（VastMed；家族成员）'], psc='', charges='', prev_names=[],
    lines=['**老板直联（Jehad Alasad 本人）+ 自述「中美跨境供应链」= 有进口经验** → 分销 20% 线：工业 PoE 交换机小批量（研究档「PoE 工业级」），一页纸 + 现货期',
           '多元集团、安防只是一条线 → 量小、不稳定；别投入超过 2 封信',
           '同名陷阱：北卡 ITSS Inc.（itss.us）与瑞士 ITSS 都不是；第三方「1,072 人」数据是瑞士那家，不可用'],
    notes='德州登记号未取（TX SoS 付费）；不再追。')
put('SB-756', key='us', batch=B, name='FluxLight, Inc.（fluxlight.com；Irving / Dallas TX）', iso='US', fetched=F,
    source='US · 1 次检索：fluxlight.com/about-us（2003 年 Irving TX 创立；光互连产品：收发器 / MC / 跳线；25,000+ 订单）+ BBB（Business Started 2004-12-15；Incorporated 2007-08-17；Corporation；Anthony Farinholt CEO & Director，Denise Farinholt Director）+ RocketReach / LinkedIn（6 人；Tony Farinholt Owner & President，Dominic Farinholt VP，Denise Farinholt CFO，Mark Mulvaney Dir. Ops）',
    url='https://www.bbb.org/us/tx/irving/profile/fiber-optics/fluxlight-inc-0875-90796041',
    number='TX 登记号未取（BBB 记 Incorporated 2007-08-17）', status='Active（BBB 档案 + 官网在线）', incorporated='2007-08-17（公司；业务始于 2003 / 2004-12）', company_type='Corporation（德州）',
    sic=['光收发器 / MC / 跳线 自有品牌（FluxLight）制造 + 直销'],
    address='2035 Royal Ln Suite 280, Dallas, TX 75229（BBB 记 Irving）', accounts='—', accounts_due='—', size_band='微型（6 人；营收 $1M 第三方估）',
    officers=['Anthony (Tony) Farinholt — Owner & President / CEO & Director', 'Denise Farinholt — CFO / Director（家族）', 'Dominic Farinholt — Vice President（家族）', 'Mark Mulvaney — Director of Operations'], psc='', charges='', prev_names=[],
    lines=['**Farinholt 家族 6 人公司、自有品牌 FluxLight（主品类 SFP，Saga 不供）**；研究档「MC + 机架 自己的 logo」→ 只剩 **OEM 30%：MC / 机架式 MC 机箱 + 光口小交换机**一条线',
           '写 Tony Farinholt（老板）或 Mark Mulvaney（运营）；研究档无邮箱 → 先用官网表单 / sales@ 公域，不编邮箱',
           '微型 → B 档维持；年度复核即可'],
    notes='第三方营收（$1M / $5–10M）互相矛盾，只记「微型」。')
put('SB-761', key='us', batch=B, name='Security Camera Warehouse, Inc.（SCW；getscw.com；Asheville NC）', iso='US', fetched=F,
    source='US · 1 次检索：BBB（Business Started 2009-09-01；Incorporated 2016-07-26；Corporation；Matthew Nederlanden President，Micah Shearer Secretary，Christopher M. Craig；33 人）+ HigherGov / GovTribe（UEI RR46YDVKTNJ1，CAGE 6ELB6，S 公司，2011-06 起联邦供应商，海军为主）+ Inc.com（INC 5000，2010 创立）+ getscw.com/about（15 年、Asheville）+ Capital at Play 2019（Nederlanden 从营销顾问接手跑路创始人的公司）',
    url='https://www.bbb.org/us/nc/asheville/profile/security-cameras/security-camera-warehouse-inc-0473-92005262',
    number='UEI RR46YDVKTNJ1 / CAGE 6ELB6（SAM 联邦登记）', status='Active（SAM 在册、INC 5000）', incorporated='2016-07-26（公司；业务始于 2009-09 / 2010-10）', company_type='S Corporation（北卡）',
    sic=['NAICS 561621 安防系统服务：自有品牌 SCW 相机 / NVR + Survail VSaaS + 安装；联邦（海军）供应商'],
    address='11 Richland St, Asheville, NC 28806（828-483-4237）', accounts='—', accounts_due='—', size_band='小型（31–50 人；第三方营收 ≈$7.7M 区间）',
    officers=['Matthew Nederlanden — CEO / President / 创始人（2009 接手）', 'Micah Shearer — Secretary', 'Christopher M. Craig — 管理层（BBB）', 'Benjamin Larue — 研究档 KP ben.larue@getscw.com（职务未取）'], psc='', charges='', prev_names=[],
    lines=['**自有品牌 SCW + 联邦（海军）供应商 = 对 NDAA 敏感**：政府线我们进不去（Saga 不做任何 NDAA / TAA 声明），**只能走商用线 OEM 30%：SCW 标 PoE 交换机**配自家相机套装',
           '31–50 人、INC 5000 成长型 → 有采购岗（研究档 KP Larue）；信里只谈商用客户用的 8/16/24 口 PoE，不碰联邦',
           'Nederlanden 是营销出身的老板，看重软件 / 服务 → 卖点写「保修 + 固件长期供应」而非价格'],
    notes='INC 5000 / 联邦供应商 = 公开可核；营收只记区间。')

# ---------------- TR 4 ----------------
put('SB-112', key='tr', batch=B, name='Opax Güvenlik Sistemleri Dış Tic. Ltd. Şti.（opax.com；İstanbul）— 研究档 KP damian@opax.pl 误归属', iso='TR', fetched=F,
    source='TR · 1 次检索：opax.com 用户协议页（法定全名「Opax Mühendislik Kamera Alarm ve Güvenlik Sistemleri … Dış Ticaret Pazarlama Limited Şirketi」/「OPAX GÜVENLİK SİSTEMLERİ DIŞ TİC. LTD. ŞTİ.」）+ 页脚「Opax İthalat Dış Ticaret Ltd. Şti. 2007-2022」+ YouTube 自述 2004 年创立（OPAX-W20 GSM/WiFi 报警）；**opax.pl = 波兰 Przytkowice 纸箱印刷厂 OPAX Sp. z o.o. Sp.k.（KRS 0000593709），Damian Brózda 是其董事会成员 → 与土耳其 Opax 无关**',
    url='https://www.opax.com/kullanici/hesap.aspx',
    number='Mersis / VKN 未取', status='Aktif（官网在线）', incorporated='2004（自述；页脚 2007 起）', company_type='Limited Şirket',
    sic=['报警系统自有品牌 OPAX（GPRS / GSM / WiFi 无线报警）+ 相机 / 安防进出口'],
    address='İstanbul（街道地址未取；客服 0 444 9890）', accounts='—', accounts_due='—', size_band='小型（估 10–30 人）',
    officers=['Aleksandar Radonic — satis@opax.com（研究档 KP，销售）', '**Damian Brózda / damian@opax.pl — 误归属：波兰纸箱厂 OPAX 的董事，删除**'], psc='', charges='', prev_names=[],
    lines=['**国别 TR 正确；研究档第一 KP 是波兰同名包装厂的人 → 误归属，改写 satis@opax.com**',
           '自有品牌报警商（OPAX-W 系列）→ PoE 交换机只是配套（研究档「商业 PoE 用洪瑞的」）→ **OEM 30%：8/16 口 PoE 贴 OPAX 标**配报警 + 相机套装',
           '老板姓名未公开 → 写 satış / satın alma；季度复核域名即可'],
    notes='kp 修正通过 patches/batch93_kp.py 落地（Damian Brózda 标 误归属）。')
put('SB-276', key='tr', batch=B, name='Han Elektronik Bilgisayar ve Güvenlik Sistemleri San. Tic. A.Ş.（hanelektronik.com；Küçükçekmece / İstanbul）', iso='TR', fetched=F,
    source='TR · 1 次检索：EMIS（法定全名；成立 2003-06-25；20 人 2026；Mehmet Akif Mah. 1904 Sk. No:15-15/A Küçükçekmece 34307）+ hanelektronik.com/iletisim（HAN ELEKTRONİK A.Ş. 地址）+ bayimiz-olun（「Han Grup 40 人、百万美元营收」）+ RocketReach（Hakan Kasap G.Müdür；Fadime Maden Purchasing Manager）+ LinkedIn（2000 / 51–200；Kerim Yeşilyurt 董事会成员）',
    url='https://www.emis.com/php/company-profile/TR/Han_Elektronik_Bilgisayar_Ve_Guvenlik_Sistemleri_Sanayi_Ticaret_AS_en_3355230.html',
    number='Mersis / VKN 未取', status='Aktif（官网 / LinkedIn 活跃；444 1 426）', incorporated='2003-06-25（EMIS；LinkedIn 记 2000）', company_type='Anonim Şirket',
    sic=['安防批发 + 自有品牌（相机 / 录像机 / 交换机 / 无线 / 火灾报警 / IoT）；经销商网络（bayi）'],
    address='Mehmet Akif Mah. Bahariye Cad. (Basın Ekspres Yolu) 1904 Sk. No:15/A, Küçükçekmece / İstanbul 34307', accounts='—', accounts_due='—', size_band='小型（20–52 人；集团自述 40 人）',
    officers=['Hakan Kasap — Genel Müdür', 'Fadime Maden — Purchasing Manager（采购经理）= 对口', 'Kerim Yeşilyurt — Yönetim Kurulu Üyesi（董事会成员）'], psc='', charges='', prev_names=[],
    lines=['**A.Ş.、40 人、自有品牌含交换机、有专职采购经理（Fadime Maden）** → **OEM 30% 首选：Han 标 PoE 交换机**（研究档「商业 PoE 看着是 hisource 的」= 现为深圳同类货 → 一对一替代）',
           '本批 TR 最厚一户；写 Fadime Maden（采购）抄 Hakan Kasap（GM）；邮箱未公开 → 先 info@ 点名收件人，不编邮箱',
           '经销商网络（bayi）= 他们自己是分销 → 不要再把他们的 bayi 当客户（Q-33 不碰）'],
    notes='建议：若回信即可列为 A 候选（Simon 定）。')
put('SB-285', key='tr', batch=B, name='RF Teknoloji Makine ve Otomasyon San. Tic. Ltd. Şti.（rfteknoloji.com.tr；Sefaköy / Küçükçekmece）', iso='TR', fetched=F,
    source='TR · 1 次检索：rfteknoloji.com.tr kurumsal（2012 年成立；法定全名 + 发票地址 Tevfik Bey Mah. Şehit Adem Tamrak Sk. No:2/5 Sefaköy）+ perpaonline（Genel Müdür Raif Gündüz）+ 官网产品页（CalAmp 代表、3onedata 工业交换机、Wlink 路由）+ firmadan（0212 210 95 65）',
    url='https://www.rfteknoloji.com.tr/kurumsal',
    number='Mersis / VKN 未取', status='Aktif（官网在线）', incorporated='2012', company_type='Limited Şirket',
    sic=['无线数据通信（RF / GSM 数据调制解调器、CalAmp 代理）+ 工业以太网交换机分销（3onedata）'],
    address='Tevfik Bey Mah. Şehit Adem Tamrak Sk. No:2/5, Sefaköy / Küçükçekmece / İstanbul 34295', accounts='—', accounts_due='—', size_band='微型（估 3–10 人）',
    officers=['Raif Gündüz — Genel Müdür（Perpa 名录）', 'Orhan Özdemir — 官网内容负责人（职务未取）'], psc='', charges='', prev_names=[],
    lines=['**工业无线 + 3onedata（深圳三旺）工业交换机分销** → 已有深圳工业货源，比价激烈 → 分销 20% 线：STI 工业 DIN 轨 PoE 作第二货源，一页纸即可',
           'GM Raif Gündüz = 老板 = 拍板；微型公司，量小',
           '季度复核：看官网是否仍挂 3onedata；若换牌子即是窗口'],
    notes='同行分销（3onedata）但非制造商 → 不守界降级，B 维持。')
put('SB-875', key='tr', batch=B, name='Lemax Güvenlik ve Bilişim Sistemleri Toptan Satış Paz. İç ve Dış Tic. Ltd. Şti.（lemaxguvenlik.com；Kartal / İstanbul）', iso='TR', fetched=F,
    source='TR · 1 次检索：lemaxguvenlik.com 产品页（法定全名 Ltd. Şti.）+ hakkımızda（2010 起；另页写 2007 / 2008 / 2012，自述不一致）+ n11 / PttAVM 店铺信息（个体「Semih Sengir / Proses Bilgisayar」为电商主体）+ Yandex（Kartal Üsküdar Cad. 127C；0216 473 72 77）',
    url='https://www.lemaxguvenlik.com/sayfa/hakkimizda/1',
    number='Mersis / VKN 未取（电商主体为个体工商户，个人税号不记）', status='Aktif（官网 2026-05 博客更新）', incorporated='2007–2012（自述不一致）', company_type='Limited Şirket + 个体（Semih Sengir）双主体',
    sic=['安防相机批发 / 零售（网店 + 门店）；自有标 Lemax PRO HD 套装；太阳能小系统'],
    address='Üsküdar Cad. 127C, Kartal / İstanbul', accounts='—', accounts_due='—', size_band='微型（1–5 人）',
    officers=['Semih Sengir — 电商店铺登记人（n11 / PttAVM）= 老板'], psc='', charges='', prev_names=[],
    lines=['**微型网店、个体 + Ltd. 双主体、相机套装贴 Lemax 标** → 量极小、价格敏感（研究档「现供新桥」）→ 分销 20% 线一页纸，不再投入',
           '老板 Semih Sengir 直联即可；B 维持，年度复核',
           '自述成立年份四个版本 → 以 Ltd. 法定名为准，不写年份给客户'],
    notes='个人税号 / MERSİS（个体）属个人数据，不入库。')
print('b93 us+tr 9 ok')
