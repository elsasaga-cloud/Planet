#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 100 批 · US 6 户 + TR 6 户（T29-U93，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）。可重复运行（put 按 code 合并）。
选户 = 规程 §3「第 100 批」名单（B 档未建底数，按「自有 logo」+「打开次数」排序）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 100

# ---------------- US 6 ----------------
put('SB-741', key='us', batch=B, name='Canary Communications, Inc.（canarycom.com；San Jose, CA）— 1987 年起的以太网连接 / 光纤媒体转换器 / 数据二极管自有品牌商（1–10 人；经分销商 / OEM / VAR 销售；表内「从 VOLKTEK 买 MC」「可以尝试多跟进一下」）', iso='US', fetched=F,
    source='US · 1 次检索：bizprofile.net（CA SoS 登记：Canary Communications, Inc.；General Corporation；Document Number 1418771；Filed 1987-09-25；Active，SoS / FTB / Agent 均 Good Standing；CEO Vinh Quang Tran（San Jose）；CFO & Director James McSeaton（Santa Clara）；Secretary & Director Roland Yamaguchi；类型 ELECTRONIC COMPUTER NETWORKING）+ Bloomberg（0060361D:US；成立 1987-09-25；6040 Hellyer Ave Suite 150, San Jose CA 95138）+ ZoomInfo（1–10 人；<$5M；Jim McSeaton Director, Sales）+ opengovus SAM（UEI WVRYXAA7DEK9；2001 注册，2026-02-12 激活至 2027-02-10；业务起始 1988-08-09）+ Crunchbase（设计制造以太网连接、媒体转换与数据安全二极管；经 distributors / OEMs / VARs / dealers 销售）+ 官网 About / Contact（1987；首个紧凑多 AUI 口收发器；info@canarycom.com）',
    url='https://www.bizprofile.net/ca/san-jose/canary-communications-inc',
    number='CA SoS 1418771（General Corporation）；SAM UEI WVRYXAA7DEK9', status='Active（Good Standing；SAM 2026-02 续期）', incorporated='1987-09-25', company_type='加州公司（私有；CEO Vinh Quang Tran）',
    sic=['以太网物理层连接产品自有品牌：光纤 / 铜媒体转换器（FE / GE、CWDM、LFS）、串口服务器、桥接转换器、模块化机箱、单向数据二极管（物理安全）'],
    address='6040 Hellyer Avenue, Suite 150, San Jose, CA 95138-1040（旧址 5884 Eden Park Place）', accounts='—', accounts_due='—', size_band='微型（1–10 人；<$5M）',
    officers=['Vinh Quang Tran — Chief Executive Officer', 'James (Jim) McSeaton — CFO / Director / Director of Sales', 'Roland Yamaguchi — Secretary / Director', 'Charles McKee — Account Executive = 研究档 KP cmckee@'], psc='三位高管（推定股东）', charges='', prev_names=[],
    lines=['**自有标 MC 品牌商、经 OEM / VAR 渠道销售、SAM 在册政府供应商** → 表内「从 VOLKTEK 买 MC」= 已有台系代工 → **贴标 OEM 30% 目标 small**：Canary 标 STI-054GP / STI-144GP（工业 PoE 补其 MC 线）+ STC-110XGE；Simon「可以尝试多跟进一下」→ 加厚一次（规格 + 对比价）但预期小（1–10 人）',
           '收件人：Charles McKee（AE）主送、Jim McSeaton（Director of Sales / CFO）抄；10 次群发无回复 → 换主题「industrial PoE to pair with your converters」；发信窗口 Wed 08–10 PT',
           '政府 / 军工客户 → 不提 TAA / NDAA、不提军用'],
    notes='自有标贴标 small；KP 老板层坐实；加厚一次。')
put('SB-743', key='us', batch=B, name='Cleerline Technology Group, LLC（cleerline.com / clrtec.com；Missoula, MT）— SSF 专利光纤品牌（2012，D’Addario & Co 关联企业；主理人 Ryan Prentice = President / Partner）；兼售工业交换机 / 10G MC / SFP', iso='US', fetched=F,
    source='US · 1 次检索：USITT / Worship Facility 新闻稿（Cleerline Technology Group 2012 年由 Robert D’Addario、Ryan Prentice、Rick Sant 作为 D’Addario & Co 关联企业创立；总部 Missoula, Montana）+ old.cleerline.com About（2009 Planet Waves 与 Custom Install Supply 合作；2012 合并成立；Prentice / Sant 来自西北太平洋集成商）+ D&B（Cleerline Technology Group, LLC；Key Principal Ryan Prentice）+ RocketReach（15 人；8404 Elway Dr Ste 2B, Missoula MT 59808）+ LinkedIn（11–50 人）+ Datanyze（Rick Sant Managing Partner；Ryan Prentice Partner）+ 2024-12 / 2025-12 / 2026-05 新闻（Ryan Prentice = President）',
    url='https://www.usitt.org/news/cleerline-introduces-ultra-compact-high-density-fiber-trunks',
    number='LLC（蒙大拿；SoS 号未取）', status='Active（2026-05 / 2026-07 新品发布）', incorporated='2012（前身 Custom Install Supply 2000 年代中）', company_type='LLC（D’Addario 家族 + Prentice + Sant 合伙）',
    sic=['专利 SSF（玻璃-玻璃-聚合物）光纤线缆、预端接 / 跳线 / 配线、熔接盒、安装工具（AV 集成、数据中心、演出）', '周边：工业交换机、10G 媒体转换器、串口光纤转换器（2025-05 新品）、SFP'],
    address='8404 Elway Drive, Suite 2B, Missoula, MT 59808', accounts='—', accounts_due='—', size_band='小型（11–50 人；15）',
    officers=['Ryan Prentice — President / Partner = 研究档 KP ryan@ 本人', 'Rick Sant — Managing Partner', 'Robert D’Addario — Principal（D’Addario & Co）', 'Gina D’Addario — PR Manager'], psc='D’Addario / Prentice / Sant', charges='', prev_names=['Custom Install Supply（Missoula）', 'Planet Waves Custom Installation'],
    lines=['**研究档 KP Ryan Prentice 坐实 = President / 合伙人本人**（拍板人）；D’Addario 集团背书 = 付款与规模无忧',
           '自有标光纤品牌 + 已卖工业交换机 / 10G MC / SFP 周边（表内 MC 供应商为「光路」）→ **贴标 OEM 30% 目标（Cleerline 标 10G 上联交换机 STC-110XGE / 工业 STI-144GP 配其光纤）**；B；18 次群发无回复 → 第二次触达换主题「a switch line to match SSF」',
           '发信窗口 Wed 08–10 MT；加厚一次（一页规格 + 贴标流程）'],
    notes='KP = President 本人；贴标 OEM 30% 目标；加厚一次。')
put('SB-754', key='us', batch=B, name='FasterCable（fastercable.com；Las Vegas, NV）— 电气 / 通信线缆与配件经销（Hellermann Tyton / Lutze 等；自有 EISW8-100T / EISW16-100T 百兆工业交换机）；Ozols 家族经营 5 人（≠ 宾州 Faster Cables LLC）', iso='US', fetched=F,
    source='US · 1 次检索：ZoomInfo（Fastercable；3325 W Ali Baba Ln Ste 619, Las Vegas NV 89118；(702) 456-8900；5 人；Juliette Ozols = Director, Operations；Richard Ozols = Sales Manager；电气 / 通信线缆、VFD 线缆、端子、断路器；经销商批量价）；检索同时命中 **Faster Cables LLC（宾州 Union City，业主 Gabriel Hershberger，fastercables.com）= 同名他户，不采**；NV SoS 法定名未取（1 次即停）',
    url='https://www.zoominfo.com/pic/fastercable/104466062',
    number='部分坐实（NV 实体名 / SoS 号未取）', status='Active（站点在线）', incorporated='未取', company_type='推定 NV 公司 / LLC（Ozols 家族）',
    sic=['电气 / 通信线缆与配件经销（plenum、VFD、Cat 线、端子、断路器、线管理）', '自有标百兆工业以太网交换机 EISW8-100T / EISW16-100T'],
    address='3325 W Ali Baba Ln, Ste 619, Las Vegas, NV 89118', accounts='—', accounts_due='—', size_band='微型（5 人）',
    officers=['Juliette Ozols — Director, Operations = 研究档「Juliette O（V. President）」', 'Richard Ozols — Sales Manager = 研究档 KP richard@'], psc='Ozols 家族（推定）', charges='', prev_names=[],
    lines=['**微型家族经销 + 自有标百兆工业交换机** → 贴标 small：千兆升级 STI-054GP / STI-288DGGPM 贴 EISW 系列后继；一页纸即止',
           '收件人 Richard Ozols；发信窗口 Wed 08–10 PT；不加厚；**不要与宾州 Faster Cables LLC 混淆**'],
    notes='部分坐实；贴标 small；一页纸。')
put('SB-783', key='us', batch=B, name='S.I. Tech, Inc.（sitech-bitdriver.com；Batavia, IL）— 1984 年起光纤调制解调器 / 复用器 / 中继器制造商（收购 Belden 光纤系统部 1984、Honeywell 光纤复用器部 1988；品牌 Bit-Driver / Fiber Cluster；ISO 9001:2015；2–10 人；业主 Ramesh Sheth）', iso='US', fetched=F,
    source='US · 1 次检索：官网 Company（创办人曾管理 Belden 光纤新业务；1984-03 作为 Illinois Corporation 开业并收购 Belden 光纤系统部；1988-01 收购 Honeywell 光纤复用器部）+ BBB（S I Tech；Business Incorporated 1983-09-22；Started 1984-03-01；Corporation；Ramesh Sheth, Owner）+ ZoomInfo / explorium（Ramesh Sheth = President；1–10 人；<$5M）+ RocketReach（5 人；1101 N. Raddant Road, Batavia IL 60510）+ IndustryNet（品牌 Bit-Driver / Fiber Cluster / S.I. Tech；ISO 9001:2015）+ CB Insights（航空航天 / 国防 / 国土安全 / 工业）+ LinkedIn（2–10 人；1984）',
    url='https://www.bbb.org/us/il/batavia/profile/fiber-optics/s-i-tech-0654-88092127',
    number='Illinois Corporation（1983-09-22；IL SoS 文件号未取）', status='Active（BBB 档案；站点在线）', incorporated='1983-09-22（开业 1984-03-01）', company_type='Corporation（业主 Ramesh Sheth）',
    sic=['光纤调制解调器、复用器、光中继、集线器、线缆组件（LAN / WAN / 工业 / 航空航天 / 国防）；Bit-Driver 网店兼售 MC / 工业交换机 / 串口设备'],
    address='1101 N. Raddant Road, Batavia, IL 60510-4214（汇款 P.O. Box 609, Geneva IL）', accounts='—', accounts_due='—', size_band='微型（2–10 人；<$5M）',
    officers=['Ramesh Sheth — President / Owner = 研究档 KP「Ramesh S」sales@ 本人'], psc='Ramesh Sheth', charges='', prev_names=[],
    lines=['**研究档 KP 坐实 = 业主 / 总裁本人**（sales@ 即老板）；40 年老店、ISO 9001',
           '自产光纤调制解调器 + Bit-Driver 网店卖 MC / 工业交换机 / 串口 → **贴标 small（OEM 30%）**：Bit-Driver 标 STI-054GP / STI-144GP / STC-110XGE；Simon「可以尝试多跟进一下」→ 一页纸 + 对比价一次',
           '客户含国防 / 航空航天 → 信里**不提军用、不提 TAA**；发信窗口 Wed 08–10 CT'],
    notes='KP = 业主本人；贴标 small；一页纸。')
put('SB-559', key='us', batch=B, name='VIPA ControlsAmerica（vipausa.com；Alpharetta, GA）— 德国 VIPA GmbH（YASKAWA 旗下）PLC / I/O / HMI 的北美销售与服务公司（1998；8 人；President & CEO Thomas Kosse；表内「工业 FS 自己的 logo」）', iso='US', fetched=F,
    source='US · 1 次检索：官网 / LinkedIn（VIPA ControlsAmerica；980 Birmingham Rd Ste 721 / 825, Alpharetta GA 30004；「North American arm of VIPA GmbH of Germany (a Yaskawa company)」；Established 1998；面向 OEM / 终端用户 / 系统集成商）+ ContactOut（1998；Thomas Kosse = President & CEO）+ RocketReach（8 人）+ 官网 About（VIPA GmbH 1985 Wolfgang Seel 创立；2012 YASKAWA Europe 收购多数股权；2019 法律合并入 Yaskawa Europe GmbH）；GA 实体法定名 / LLC 号未取（1 次即停）',
    url='https://www.linkedin.com/company/vipa-controls-america',
    number='GA 实体名 / SoS 号未取（公开名 VIPA ControlsAmerica）', status='Active（站点在线；墨西哥线 ventas@）', incorporated='1998', company_type='私有（美国独立销售公司；President & CEO Thomas Kosse；与 Yaskawa 关系为品牌授权 / 代理，未核股权）',
    sic=['VIPA（Yaskawa）PLC / 远程 I/O / HMI / PROFIBUS 连接器北美销售、服务与支持；Siemens STEP7 兼容；GermanAutomation® 站'],
    address='980 Birmingham Rd. Ste 721 / 825, Alpharetta, GA 30004', accounts='—', accounts_due='—', size_band='微型（8 人）',
    officers=['Thomas Kosse — President & CEO（研究档无 KP）'], psc='未取', charges='', prev_names=['VIPA Controls America'],
    lines=['**PLC 分销商卖自有 logo 工业交换机** = 柜内配套品，量随 PLC 项目 → **贴标 small（OEM 30%）**：STI-054GP / STI-144GP / STI-288DGGPM（导轨、宽温、PROFINET 环境常见需求 = 管理型 + 快速环网）',
           '收件人 Thomas Kosse（President & CEO；info@vipausa.com 点名）；18 次群发无回复 → 换主题「DIN-rail managed PoE for PLC panels」；发信窗口 Wed 08–10 ET；一页纸'],
    notes='贴标 small；一页纸。')
put('SB-061', key='us', batch=B, name='Megatel Industries Corporation（megatelindustries.com；North Wales, PA）— 1991/1994 起的数据通信 / 光纤产品批发商、出口商兼 OEM 品牌商（IFS / IGS / IMC / FMC 系列 = CTC Union / ONV 贴牌；DoD 供应商 CAGE IRRG5；3 人；总裁 Zack Yu）', iso='US', fetched=F,
    source='US · 1 次检索：官网 About（Founded in 1994, Megatel Industries corp.；批发 / 出口至亚洲、欧洲、非洲、加勒比、南美；664 Wagner Court, North Wales PA 19454；sales@）+ Buzzfile（Megatel Industries Corporation；Zack Yu = President；3 人；≈$0.42M；经营约 34 年；亚裔业主）+ D&B（Founded 1991；Incorporated PA；$1M；3 人）+ RocketReach（$2M；DoD 供应商 CAGE Code IRRG5；客户含联邦 / 州 / 市政府、军方、学校、出口贸易公司、批发商）+ Govcb / MapQuest（旧址 6 Crimson Drive, Norristown PA 19401）+ ZoomInfo（Zack Yu Sales Manager）',
    url='https://www.megatelindustries.com/info.html',
    number='PA Corporation（PA DOS 号未取；CAGE IRRG5）', status='Active（站点在线）', incorporated='1991（D&B）/ 1994（自述）', company_type='Corporation（宾夕法尼亚；业主 Zack Yu）',
    sic=['数据通信 / 光纤设备批发与出口 + 自有 logo：工业以太网 / PoE 交换机与转换器（IFS / IGS / IMC / ITP / IPSW / FMC）、EN50155 工业 PoE+ 管理型交换机、SFP、CWDM、T1/E1 / SDH 转换、工业电源'],
    address='664 Wagner Court, North Wales, PA 19454（旧址 6 Crimson Dr, Norristown PA 19401）', accounts='—', accounts_due='—', size_band='微型（3 人；$0.4–2M）',
    officers=['Zack Yu — President / Sales Manager = 研究档 KP zack@ 本人（业主）'], psc='Zack Yu', charges='', prev_names=[],
    lines=['**研究档 KP 坐实 = 业主 / 总裁本人**；微型（3 人）但自有 logo 全线工业交换机 + 政府 / 军方 + 出口客户 → **贴标 small（OEM 30%）**：Megatel 标 STI-054GP / STI-288DGGPM / STI-488DGGPM 对标其 CTC Union 贴牌款（表内其 8 口千兆管理 PoE 标 $1,800 → 我方 $147 级有巨大空间）',
           '华人老板（Zack Yu）→ 可中文直联（Q 默认 no，先英文）；发信窗口 Wed 08–10 ET；一页纸 + 对比价；不提军用 / TAA'],
    notes='KP = 业主本人；贴标 small；一页纸。')


# ---------------- TR 6 ----------------
put('SB-687', key='tr', batch=B, name='Telkotim Bilişim Teknolojileri Tic. Ltd. Şti.（telkotim.com / telkotim.com.tr；Ankara Yenimahalle）— 2008 年起的光纤 / 网络基础设施产品分销商（「Türkiye’nin Fiber & Network Alt Yapı Merkezi」；TTAF / HCS 光缆、D-Link / Ruijie 交换机；GM Veli Uysal）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 İletişim / Hakkımızda / Çerez（Telkotim Bilişim Teknolojileri Tic. Ltd. Şti.；Çamlıca Mah. Anadolu Bulvarı Timko İşyerleri No 20 c-4, Yenimahalle / Ankara；(0312) 473 09 99；bilgi@telkotim.com；2008 年成立；铜缆 / 光缆 / 数据中心布线方案，多品牌 bayi / dağıtıcı）+ Anadolu Ajansı 2022-04-19（Telkotim Bilişim Teknolojileri Genel Müdürü Veli Uysal：2008 起从事 IT / 光纤 / 数据系统；「Türkiye’den 136 ülkeye fiber optik ürün ihracatı」报道）+ Elektrik Dünyası 2024-11（ISAF 2024 参展）+ telkotim.com.tr（TTAF 集团 2003 İstanbul 成立，六大板块；页脚 © 2026 Telkotim … Ltd. Şti. ❤ İnfonet）',
    url='https://www.telkotim.com/iletisim',
    number='Ltd. Şti.（Ankara；MERSİS 号未取）', status='Active（ISAF 2024 参展；站点 2026）', incorporated='2008', company_type='Limited Şirket（私有；GM Veli Uysal；关联 İnfonet / TTAF 光缆）',
    sic=['光纤 / 铜缆布线、数据中心、光缆与配件、熔接测试设备、机柜、交换机 / PoE 交换机（D-Link 铜口 / 光口 / 工业 / PoE；Ruijie）分销 —— 面向大型光纤 / 网络项目供货'],
    address='Çamlıca Mahallesi Anadolu Bulvarı Timko İşyerleri No 20 c-4, Yenimahalle / Ankara', accounts='—', accounts_due='—', size_band='小型（人数未取；AA 报道的出口主体为关联光缆厂）',
    officers=['Veli Uysal — Genel Müdür（总经理）= 研究档 KP「Veli」veli@ 本人'], psc='Veli Uysal（推定）', charges='', prev_names=[],
    lines=['**研究档 KP 坐实 = 总经理本人**（veli@ 即老板）；安卡拉光纤 / 网络项目供货商，已卖 D-Link 工业 / PoE 交换机 → **分销 20%**：STC-228GP / STC-2224GP（PoE）+ STI-144GP / STI-288DGGPM（工业光口，配其光缆项目）+ STI-0240GE（24 口 L2+ 投标）',
           '表内 1 次跟进无回复 → 第二次触达换主题「fiber-port switches to ship with your cable」；发信窗口 Thu 10–12 TRT；加厚一次（规格 + 三档价）'],
    notes='KP = GM 本人；分销 20%；加厚一次。')
put('SB-475', key='tr', batch=B, name='CCTVDEPO Güvenlik Teknolojileri A.Ş.（cctvdepo.com；İstanbul Yenibosna / Bahçelievler + Perpa B Blok）— 2004 年起土耳其最早的安防 B2B 电商 / 全国 bayi 批发商；自有品牌 SECUZI / TİRENZO 的生产商兼进口商（51–200 人；站内自有标 SZNT- PoE 交换机）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 Gizlilik（Satıcı CCTVDEPO Güvenlik Teknolojileri A.Ş.；Remzi Özkaya Cad. No 18 Yenibosna；Yenibosna VD；MERSİS 0203034849100015；Ticaret sicil 70431-5；KEP cctvdepo@hs01.kep.tr）+ ETBİS（MERSİS 0203034849100015；Vergi No 2030348491；CCTVDEPO GÜVENLİK TEKNOLOJİLERİ ANONİM ŞİRKETİ；2004 年成立，电子安防系统批发）+ 官网 Hakkımızda（20 年以上团队；**SECUZI ve TİRENZO markalı ürünlerin üreticisi ve ithalatçısı**；客户代表 Asuman Özüdoğru / Mehmet Sağlam / Mert Yıldız；总部 Hürriyet Mh Güngören Sk 4b Bahçelievler；Perpa CepDepo B Blok K8 No 836）+ LinkedIn / SignalHire（51–200 / 100–200 人；2004；$1–10M）+ Kariyer 2026-06（招 Bayi Kanalı 销售；全国安防 bayi 供货）',
    url='https://www.eticaret.gov.tr/siteprofil/CE3F46BF44034071A9956AA7132E34DF/wwwcctvdepocombayi',
    number='MERSİS 0203034849100015 · Ticaret Sicil 70431-5（İstanbul）· VKN 2030348491', status='Active（ETBİS 在册；2026-06 招聘）', incorporated='2004', company_type='Anonim Şirket（私有）',
    sic=['电子安防系统 B2B 批发电商（摄像机 / NVR / PoE 网络 / 电脑配件 / 手机配件 / 安装材料 / 智能安防；全国 bayi）', '自有品牌 SECUZI / TİRENZO（生产 + 进口；站内 SZNT-PSY0420FL / PSP0820FLR / PSP0420GLR 等自有标 PoE 交换机）'],
    address='Remzi Özkaya Cad. No 18, Yenibosna / İstanbul（注册）；Hürriyet Mh Güngören Sk 4b, Bahçelievler 34188（总部仓）；Perpa Ticaret Merkezi B Blok K8 No 836, Şişli（门店）', accounts='—', accounts_due='—', size_band='中型（51–200 人；$1–10M）',
    officers=['Asuman Özüdoğru — Müşteri Temsilcisi（客户代表）= 研究档 KP（研究档误配 can@）', 'Mehmet Sağlam / Mert Yıldız — 客户代表', 'Can Gürcan — 研究档 KP can@（职务未核）', '董事会未取'], psc='未取', charges='', prev_names=[],
    lines=['**第 100 批 TR 最大户、OEM 30% 首选**：自有品牌 SECUZI / TİRENZO 下已卖自有标 PoE 交换机（SZNT- 型号 = 华南贴牌）+ 全国 bayi 批发 + 51–200 人 → **SECUZI 标 STC-028GP / STC-228GP / STC-2216GP / STC-2224GP 贴标 OEM 30%，B BIG，升 A 候选（回信即 A）**',
           '收件人：研究档 can@（Can Gürcan）主送、Asuman Özüdoğru 抄，点名「satın alma / ürün müdürü」；表内无跟进 → 首信即一页纸 + 对比价（其 4 口 / 8 口 PoE 在售价）；发信窗口 Thu 10–12 TRT；**加厚**'],
    notes='OEM 30% 首选；B BIG；升 A 候选；加厚。')
put('SB-478', key='tr', batch=B, name='Eurocam GD Güvenlik Elektronik ve Bilişim Sistemleri San. Dış Tic. Ltd. Şti.（eurocamguvenlik.com.tr；İstanbul Perpa A Blok）— 2017 年起安防进口商：自有品牌 Eurocam（安防）+ **Eurolink（网络 / 连接设备）**；2020 起自产摄像机；500+ bayi；CEO / 创办人 Gökhan Demir', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 EN About（「As the family of GD Güvenlik Sistemleri San. Dış Tic. Ltd. Şti … 2017」；「imports security systems products under the Eurocam brand, and imports network and connection equipment under the Eurolink brand」；「Since 2020 … producing many models of security cameras」；Gökhan DEMİR CEO - Founding Manager gokhandemir@；Perpa A Blok 8. Kat No 918 Şişli）+ Hakkımızda（500 多家 bayi；直接进口；页脚 © 2026 Eurocam GD Güvenlik ve Elektronik Sistemleri San. Dış Tic. Ltd. Şti.）+ b2b 站 İletişim（Eurocam GD Güvenlik Elektronik ve Bilişim Sistemleri San. Dış Tic. Ltd. Şti.）+ ZoomInfo（11–50 人）+ nereninmali / kiminmali（Eurocam 显示器 = GD Güvenlik 2017 成立，İstanbul）；Bursa 的 Eurocam Yapı Sistemleri（玻璃幕墙）为同名他户，不采',
    url='https://www.eurocamguvenlik.com.tr/en.php',
    number='Ltd. Şti.（İstanbul；MERSİS 号未取）', status='Active（站点 2026；b2b 站运行）', incorporated='2017', company_type='Limited Şirket（创办人 CEO Gökhan Demir）',
    sic=['安防系统进口与分销（Eurocam 品牌：CCTV / IP 摄像机、显示器、车牌识别、考勤、消防、报警；2020 起自产摄像机）', '网络 / 连接设备进口（**Eurolink 品牌** = 自有标交换机 / 线材）；Hikvision / Dahua / Ruijie 在售'],
    address='Halil Rıfat Paşa Mah. Yüzer Havuz Sok. Perpa Ticaret Merkezi A Blok 8. Kat No 918, 34384 Şişli / İstanbul', accounts='—', accounts_due='—', size_band='小型（11–50 人；500+ bayi）',
    officers=['Gökhan Demir — CEO / Founding Manager（创办人）= 研究档 KP gokhandemir@ 本人'], psc='Gökhan Demir', charges='', prev_names=['GD Güvenlik Sistemleri San. Dış Tic. Ltd. Şti.'],
    lines=['**研究档 KP 坐实 = 创办人 CEO 本人**；**自有网络品牌 Eurolink 已存在 + 直接进口 + 500 bayi → OEM 30% 首选（Eurolink 标 PoE 交换机：STC-028GP / STC-228GP / STC-2216GP / STC-2224GP），B BIG，升 A 候选（回信即 A）**',
           '表内 1 次跟进无回复 → 第二次触达换主题「Eurolink PoE line: 8 / 16 / 24-port with 2-year warranty you already promise」（其官网承诺 2 年保修 → HRUI 1 年需说明 / STI 3 年可对齐）；发信窗口 Thu 10–12 TRT；**加厚**（贴标流程 + 三档价）'],
    notes='OEM 30% 首选；KP = CEO 本人；B BIG；升 A 候选；加厚。')
put('SB-489', key='tr', batch=B, name='PORTEL TEKNOLOJİ SAN. VE TİC. A.Ş.（portel.com.tr / industrialnetworkcenter.com；İstanbul Kartal）— 2017 年成立的工业网络产品 + 半导体元件供应商（NACE 46.52.01 电信设备批发；在线商城 IndustrialNetworkCenter；表内「买 3onedata（三旺）的」）', iso='TR', fetched=F,
    source='TR · 1 次检索：vknsorgula（PORTEL TEKNOLOJİ SANAYİ VE TİCARET ANONİM ŞİRKETİ；VKN 7320767976；Kuruluş 2017-05-23；VD 工作开始 2017-05-23 / 2021-01-29；Ticaret sicil 1075179；NACE 46.52.01；Yalı Mah. Kadir Sk. No 14 Kartal；电话 216 464 50 00；活跃）+ industrialnetworkcenter.com İletişim（Firma Resmi Adı PORTEL TEKNOLOJİ SAN. VE TİC. A.Ş.；Helis More Residence Kat 7 Daire 82；TL / USD / EUR 账户）+ 官网 Hakkımızda（20 年以上半导体供应经验；工业网络产品）+ 旧址 Kozyatağı-Kadıköy（隐私政策 2021）+ Tendata（2024-11：73 票进口，13 家供应商）',
    url='https://vknsorgula.net/7320767976',
    number='VKN 7320767976 · Ticaret Sicil 1075179（İstanbul）', status='Active（2025-12 官网更新；2024 进口 73 票）', incorporated='2017-05-23', company_type='Anonim Şirket（私有，小型；注册地为住宅楼）',
    sic=['工业网络产品（工业交换机 / 串口服务器 / 光纤设备 —— 三旺等）与半导体元件供应；在线商城 IndustrialNetworkCenter；客户：电商 / 能源 / 海事 / 铁路网络与控制'],
    address='Yalı Mah. Kadir Sk. No 14, Helis More Residence Kat 7 Daire 82, 34873 Kartal / İstanbul（旧址 Kozyatağı）', accounts='—', accounts_due='—', size_band='微型 / 小型（A.Ş. 但住宅楼办公；人数未取）',
    officers=['Okay Yücedağ — 研究档 KP（Sales；职务未核）', '董事会未取'], psc='未取', charges='', prev_names=[],
    lines=['**已直接从华南（三旺）进口工业交换机的小型 A.Ş. 电商** → 价格认知已到位 → **分销 20%**：切口 = 三旺没有的「Marvell 管理型 L2+ 工业 PoE」（STI-288DGGPM / STI-488DGGPM）+ 3 年保修 + MOQ 1；铁路客户不碰（守界）',
           '收件人 Okay Yücedağ；发信窗口 Thu 10–12 TRT；一页纸即止（不点名三旺）'],
    notes='分销 20%；已直采三旺；一页纸。')
put('SB-490', key='tr', batch=B, name='Radio Teknoloji Hizmetleri A.Ş.（radioteknoloji.com.tr；İstanbul Bakırköy）— 2015 年起户外宽带无线（PtP / PtMP / 室外 Wi-Fi / WiMAX / LTE）分销商兼系统集成商（KGYS / MOBESE 城市监控、TEDES、边境 / 港口 / 机场 / 市政；11–50 人；SAHA 国防展参展）', iso='TR', fetched=F,
    source='TR · 1 次检索：LinkedIn（Radio Teknoloji Hizmetleri A.Ş；2015；11–50 人；Bakırköy；「Türkiye’nin önde gelen Dış Ortam Kablosuz Distribütör ve Entegretör firması」；KGYS / EDS / Mobese / WISP / FBWA / TEDES）+ MÜSİAD Expo 参展名录（RADIO TEKNOLOJİ HİZMETLERİ A.Ş.；Ataköy 7-8-9-10. Kısım Mah. Çobançeşme E-5 Yan Yol Cad. Avrupa Residence No 8/1 A Blok Daire 10, Bakırköy）+ Facebook（+90 212 644 07 84；info@；客户 KGYS / TEDES / TSK / 边境 / 港口 / 机场 / 市政；接待国防部质保局长）+ SAHA Expo 参展页（分销商 + 系统集成商；PtP / PtMP / 室外 Wi-Fi / 车载移动通信 / 4G-5G LTE）+ 官网（InfiNet Wireless 等）',
    url='https://in.linkedin.com/company/radio-teknoloji-hizmetleri-a.%C5%9F',
    number='A.Ş.（İstanbul；MERSİS 号未取）', status='Active（2026 官网改版；SAHA / MÜSİAD 参展）', incorporated='2015', company_type='Anonim Şirket（私有，少数股东）',
    sic=['户外宽带无线设备分销与集成：PtP / PtMP 网桥、室外 Wi-Fi、WiMAX / LTE、微波、SCADA 数据传输、智慧城市 / 城市监控（KGYS）、国防通信基础设施'],
    address='Ataköy 7-8-9-10. Kısım Mah. Çobançeşme E-5 Yan Yol Cad. Avrupa Residence No 8/1 A Blok D 10, Bakırköy / İstanbul', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Salih Yıldırım — Project Manager = 研究档 KP salih.yildirim@（职务为研究档记录，未另核）', 'Abdurrahman Pehlivanoğlu — 研究档 KP', '董事会未取'], psc='未取', charges='', prev_names=[],
    lines=['**户外无线分销 + 集成商** → 每个无线站点 / KGYS 杆位都要一台宽温 PoE 交换机 → **集成商 25%（兼分销 20%）**：STI-054GP / STI-144GP / STI-288DGGPM（导轨、-40~75 °C、PoE 给网桥与摄像机供电）',
           '客户含 TSK（军方）→ 信里**只谈市政 / KGYS / 港口场景，不提军用**；收件人 Salih Yıldırım（项目经理 = 选型人）；发信窗口 Thu 10–12 TRT；一页纸 + 杆位配置图一张'],
    notes='集成商 25%；不提军用；一页纸。')
put('SB-496', key='tr', batch=B, name='By Bora Teknoloji Dünyası（Ağrı；Facebook 主页；无域名）— 土耳其东部阿勒的微型弱电 / 电脑 / 安防门店（Bora Erim；WhatsApp 已加；询盘 2 光 8 PoE 商业级 10 台）', iso='TR', fetched=F,
    source='TR · 1 次检索：Facebook 主页「By Bora Teknoloji Dünyası, Ağrı」（Zayıf Akım Sistemleri、Bilgisayar、Akıllı ev sistemleri、Güvenlik Kamerası、Hırsız alarm、İnternet alt yapı）= 与研究档一致；**Trabzon 的 Bora Teknoloji（borateknoloji.com.tr，2006）与 İstanbul Maltepe 的手机维修店为同名他户，不采**；无商业登记可查（个体门店）',
    url='https://www.facebook.com/ByBoraErimAgri/',
    number='部分坐实（Facebook 主页；无 VKN / MERSİS）', status='Active（主页在线）', incorporated='未取', company_type='个体门店（推定 şahıs işletmesi）',
    sic=['弱电系统、电脑、智能家居、监控摄像机、防盗报警、网络布线（阿勒本地安装 + 零售）'],
    address='Ağrı（门牌未取）', accounts='—', accounts_due='—', size_band='微型（1–5 人推定）',
    officers=['Bora Erim — 业主 = 研究档 KP（boraerim@gmail.com；WhatsApp 已加）'], psc='Bora Erim', charges='', prev_names=[],
    lines=['**微型门店但需求明确（2 SFP + 8 PoE 商业级 ×10）** → 直接 WhatsApp 报 STC-228GP（8+2 SFP，$33 ×10）+ 运费（DAP 走百运网）；WhatsApp 客户不走编号群发（规则）',
           '不加厚、不建卡；成交即记一笔；下轮不追'],
    notes='微型门店；WhatsApp 直报 STC-228GP；不加厚。')

print('b100 US 6 + TR 6 written')
