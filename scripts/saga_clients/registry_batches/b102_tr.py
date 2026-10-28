# -*- coding: utf-8 -*-
"""第 102 批（T29-U95，2026-10-28）TR 7 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 102
F = '2026-10-28'

put('SB-859', key='tr', batch=B, name='BABURTECH BİLİŞİM SANAYİ VE TİCARET ANONİM ŞİRKETİ（baburtech.com；Ankara Kızılay）— 2007 年起的笔记本 / 手机原厂配件与维修电商（兼售 Hikvision / Dahua / TP-Link / Ubiquiti / Planet 网络安防品）；**MERSİS 0128085731200001**（商务部 ETBİS 电商登记，2017-12-29）；Vergi No 1280857312（Çankaya）；研究档 KP Ayşe Narinsöz（职务待核）', iso='TR', fetched=F,
    source='TR · 1 次检索：T.C. Ticaret Bakanlığı ETBİS 站点档案（www.baburtech.com；Mersis No 0128085731200001；İşletme Adı BABURTECH BİLİŞİM SANAYİ VE TİCARET ANONİM ŞİRKETİ；İşletme Türü Anonim Şirket；ETBİS 登记 2017-12-29）+ 官网 İletişim（Vergi No 1280857312；Vergi Dairesi Çankaya；Ziya Gökalp Cad. No 9 Kızılay；技术服务 Necatibey Cad. No 51 Çankaya；0850 302 06 47）+ LinkedIn（2007；Çankaya Ankara；自报 201–500 人 — 存疑）+ TrustBuy（Ankara 中央仓 Ziya Gökalp Cad. 9/3 Kızılay；电脑 / 移动设备配件大仓）+ başkentrehber（负责人「Genel Müdür」未具名）',
    url='https://www.eticaret.gov.tr/siteprofil/DBF006896AD84356AECB2A471AD82BE2/wwwbaburtechcom',
    number='MERSİS 0128085731200001 · Vergi No 1280857312（Çankaya）', status='Aktif（ETBİS 在册；站点在线）', incorporated='2007（LinkedIn；ETBİS 登记 2017-12-29）', company_type='Anonim Şirket（私有）',
    sic=['电脑 / 笔记本 / 手机原厂配件与维修电商（B2C + B2B）', '网络 / 安防品转售（Hikvision / Dahua / TP-Link / Ubiquiti / Planet；表内「switch，有海思的」）'],
    address='Cumhuriyet Mah. Ziya Gökalp Cad. No 9/3, Kızılay, Çankaya / Ankara', accounts='—', accounts_due='—', size_band='小型 / 中型（自报 201–500 存疑；实体配件电商）',
    officers=['Genel Müdür — 未具名（başkentrehber）', 'Ayşe Narinsöz — 研究档 KP ayse@（职务待核；采购 / 产品推定）'], psc='未取', charges='', prev_names=[],
    lines=['**配件电商 + 网络品转售（已卖海思方案交换机）→ 分销 20% small，一页纸**：STC-028GP / STC-228GP / STC-2216GP（对标其在售 TP-Link / 海思白牌价）；不加厚',
           '收件人 ayse@ 点名 satın alma；群发已打开 → 第二次触达换主题「managed PoE switches at unmanaged-level prices — MOQ 1, DAP Ankara」；发信窗口 Thu 10–12 TRT；ETBİS 站点档案 = 新增 TR 查号路径（已记规程 §1）'],
    notes='分销 20% small；一页纸；MERSİS 坐实（ETBİS）。')
put('SB-657', key='tr', batch=B, name='EGESAN TEKNOLOJİ PAZARLAMA İTH. İHR. VE TİC. LTD. ŞTİ.（egesanteknoloji.com.tr；**Bodrum / Muğla**，非 İzmir）— 2005 年起的电子安防 / 消防探测 / 报警 / 摄像机批发商：HiLook 土耳其官方分销、Hikvision / Fujitron / Westa / Decon / Ajax / Ruijie Reyee 主分销、**自有品牌 Coremax 进口商兼商标持有人**；Vergi No 3250872231（Bodrum）；研究档 KP Gökhan（职务未核）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 İletişim（Egesan Teknoloji Pazarlama İth.；Akçaalan Mahallesi Cumhuriyet Blv. No 120/1 A Blok, 48400 Bodrum/Muğla；Vergi No 3250872231；Vergi Dairesi Bodrum；0 252 382 32 36；info@）+ Yenibiriş 公司页（EGESAN TEKNOLOJİ PAZARLAMA İTH.İHR VE TİC.LTD. ŞTİ.；「2005 yılından bugüne」；Hi Look Türkiye Resmi Distribütörü；Hikvision / Fujitron / Westa / Decon / Ajax / Ruijie Reyee ana dağıtıcısı；**Coremax marka ürünlerin ithalatçısı ve marka sahibi**；总部 Muğla；Karabağ Mah. Turgut Özal Cad. No 4 Bodrum）+ bayifi.com（Hikvision 批发商 Muğla；Ajax / Dahua / Hikvision）',
    url='https://www.egesanteknoloji.com.tr/iletisim',
    number='Vergi No 3250872231（Bodrum）；MERSİS 未取（按规则推定 0325087223100001，未核）', status='Aktif（站点在线）', incorporated='2005（自述）', company_type='Limited Şirket（私有）',
    sic=['电子安防 / 消防 / 报警 / CCTV / 网络批发（HiLook 官方分销；Hikvision、Ajax、Ruijie Reyee 主分销）', '自有品牌 Coremax（进口 + 商标持有）'],
    address='Akçaalan Mah. Cumhuriyet Blv. No 120/1 A Blok, 48400 Bodrum / Muğla（另址 Karabağ Mah. Turgut Özal Cad. No 4 Bodrum）', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['Gökhan（姓未取）— 研究档 KP gokhan@（职务未核；疑业主 / 采购）'], psc='未取', charges='', prev_names=[],
    lines=['**多品牌安防批发 + 自有品牌 Coremax 进口商 → 分销 20% + 贴标 OEM 30% 目标**：Coremax 标 STC-028GP / STC-228GP / STC-2216GP / STC-2224GP（对标其在售 Ruijie Reyee RG-ES 系列价）；加厚一次（两线各一张价）',
           '收件人 gokhan@；表内 1 次跟进无回复 → 第二次触达换主题「PoE switches under the Coremax label — managed L2+, MOQ 1」；发信窗口 Thu 10–12 TRT；地域更正：Bodrum / Muğla；升 A 次候选'],
    notes='分销 20% + Coremax 贴标 OEM 30%；加厚一次；地域 Bodrum；升 A 次候选。')
put('SB-660', key='tr', batch=B, name='Fonet Fiber Optik Bilgisayar Hizmetleri Ticaret Limited Şirketi（fonet.com.tr；İstanbul）— 1995 年成立的结构化布线 / LAN-WAN / 无线 / 交钥匙数据中心基础设施集成商（光纤布线与熔接、测试、机柜、有源设备配置与维护；机场 / 大桥 / 酒店项目）；Vergi No 3880095179；**与上市公司 FONET Bilgi Teknolojileri A.Ş.（Ankara 医疗信息化，BIST:FONET）无关**；研究档 KP Akgün（职务未核）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 Hakkımızda / 首页 schema（legalName「Fonet Fiber Optik Bilgisayar Hizmetleri Ticaret Limited Şirketi」；foundingDate 1995-01-01；taxID 3880095179；1995 İstanbul 成立；结构化布线、LSN、WAN、Wireless、交钥匙 Data Center；服务：光纤布线与端接、测试分析、数据布线与机柜安装、数据中心与无线、有源设备配置维护、勘察设计与产品销售）；检索同时返回 FONET BİLGİ TEKNOLOJİLERİ A.Ş.（Ankara；Vergi No 3880651486；1997 医疗信息化；BIST 上市）= **同名他户，不采**',
    url='https://fonet.com.tr/hakkimizda/',
    number='Vergi No 3880095179；MERSİS 未取', status='Aktif（站点 2024 更新）', incorporated='1995', company_type='Limited Şirket（私有）',
    sic=['网络 / 电信基础设施集成：结构化布线、光纤、无线、数据中心交钥匙、有源设备配置维护与产品销售'],
    address='İstanbul（门牌未取）', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['Akgün（姓未取）— 研究档 KP akgun@（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**30 年布线 / 数据中心集成商 → 集成商 25%**：STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W（楼宇接入 PoE）+ STC-448XGGPM / STH-2C24XF-HSI（机房汇聚 / ToR）；一页纸 + DC 规格；不加厚',
           '收件人 akgun@；表内 1 次跟进无回复 → 第二次触达换主题「access + ToR switches for your turnkey data center projects — 15-day quote」；发信窗口 Thu 10–12 TRT；下轮补项：MERSİS / 门牌'],
    notes='集成商 25%；一页纸；同名上市公司不采。')
put('SB-661', key='tr', batch=B, name='GOLD-NET BİLİŞİM ELEKTRONİK SANAYİ VE TİCARET LİMİTED ŞİRKETİ（goldnet.com.tr；**Çorlu / Tekirdağ**）— 2004-10-01 成立的安防 / 电子产品公司（自有品牌 GOLDNET NVR / 摄像机经由经销商销售；Teknogon Güvenlik 关联）；**MERSİS 0396049037300015**；Vergi No 3960490373；Ticaret Sicil 7956 Çorlu；**2019 起 konkordato（破产重整保护）程序（2019/297 → 2021/219 → 2024/79），业主 Murat Gündeğer / Mustafa Gündeğer**；研究档 KP Murat（murat@）疑 = Murat Gündeğer', iso='TR', fetched=F,
    source='TR · 1 次检索：konkordatotakip 2024-07（GOLD-NET BİLİŞİM ELEKTRONİK SANAYİ VE TİCARET LİMİTED ŞİRKETİ；Vergi No 3960490373；Ticaret Sicil 7956 / ÇORLU / TEKİRDAĞ；Dosya 2019/297 >> 2021/219 >> 2024/79；申请人 Gold-Net（MERSİS 0396049037300015）、Teknogon Güvenlik Sistemleri İth. İhr. San. Tic. Ltd. Şti.（0734055181700012）、Murat Gündeğer、Mustafa Gündeğer）+ EMIS（incorporated 2004-10-01；Kazımiye Mah. Dadaloğlu Cad. No 42 Çorlu Tekirdağ 59860；Electronics Stores）+ Çorlu TSO 名录（Muhittin Mh. Omurtak Cad. Peksoy Apt. K4 D11 Çorlu；0850 333 26 50）+ Yandex（Çorlu 安防与报警系统）+ leventelektronik（GOLDNET GN-5104 NVR 自有品牌产品）；find.com.tr 的 GOLDNET BİLİŞİM TEKNOLOJİLERİ（个体，1999）与 Ankara 的 Goldennet 为同名他户',
    url='https://www.konkordatotakip.com/2024/07/gold-net-bilisim-elektronik-sanayi-ve-ticaret-limited-sirketi-11/',
    number='MERSİS 0396049037300015 · Vergi No 3960490373 · Ticaret Sicil 7956（Çorlu）', status='Aktif（但 konkordato 程序进行中 2019–2024+）', incorporated='2004-10-01', company_type='Limited Şirket（Gündeğer 家族；关联 Teknogon Güvenlik）',
    sic=['安防 / 电子产品销售（自有品牌 GOLDNET NVR / 摄像机，经销商渠道）'],
    address='Kazımiye Mah. Dadaloğlu Cad. No 42, Çorlu / Tekirdağ 59860', accounts='—（重整程序中）', accounts_due='—', size_band='小型（人数未取）',
    officers=['Murat Gündeğer — 业主 / 申请人（konkordato 文件）= 研究档 KP murat@ 推定同人', 'Mustafa Gündeğer — 业主 / 申请人'], psc='Gündeğer 家族', charges='konkordato（债务重整）程序 2019/297 → 2021/219 → 2024/79', prev_names=[],
    lines=['**自有品牌 GOLDNET + 业主本人收件，但公司处于 konkordato 重整 → 回款风险高 → 贴标 small，`when=不动` 之外的唯一例外是 100% 预付**：Goldnet 标 STC-028GP / STC-228GP 一页纸，T/T 100% 预付、不赊、不备货；不加厚；**对客不提重整**',
           '收件人 murat@；表内 1 次跟进无回复 → 第二次触达一次即止；发信窗口 Thu 10–12 TRT；地域更正：Çorlu / Tekirdağ'],
    notes='贴标 small；konkordato 风险 → 100% 预付；一页纸；地域 Çorlu。')
put('SB-665', key='tr', batch=B, name='Marsa Teknoloji ve Yazılım A.Ş.（marsateknoloji.com；İstanbul Ümraniye）— 进口型安防 / 通信分销商：U-Prox（门禁）、Ur-fog（防盗烟雾）、BAS-IP（IP 对讲，捷克产）、Fanvil（IP 话机）土耳其授权 / 独家分销；Hikvision / Dahua / Tiandy / Teletek 销售与技术服务点；海关记录显示直接进口（UR FOG S.R.L / BAS-IP DISTRIBUTION LTD / BAS-IP TECHNOLOGY S.R.O）；研究档 KP Ali Yıldız（职务未核）', iso='TR', fetched=F,
    source='TR · 1 次检索：官网首页 / Distribütörlüklerimiz（Marsa Teknoloji A.Ş.；U-Prox、Urfog、BasIP、Fanvil Türkiye Distribütörü；Hikvision / Dahua / Tiandy / Teletek 销售与技术服务点；İnkılap Mah. İlkkurşun Cad. 83B Ümraniye İstanbul；0216 256 56 86；info@）+ U-Prox / BAS-IP 官方「Where to buy」（Marsa Teknoloji ve Yazilum A.S.，同址）+ u-prox.com.tr（Marsa Teknoloji ve Yazılım A.Ş，No 83/A）+ nbd.ltd 贸易数据（MARSA TEKNOLOJİ VE YAZILIM ANONİM ŞİRKETİ；贸易伙伴 UR FOG S.R.L、BAS-IP DISTRIBUTION LTD.、BAS-IP TECHNOLOGY S.R.O）；Vergi No / MERSİS 未取',
    url='https://www.marsateknoloji.com/distributorluklerimiz',
    number='A.Ş.（İstanbul；Vergi No / MERSİS 未取 → 部分坐实）', status='Aktif（站点在线；2025 仍列为 U-Prox 土耳其分销）', incorporated='未取', company_type='Anonim Şirket（私有）',
    sic=['安防 / 通信设备进口分销（门禁 U-Prox、防盗烟雾 Ur-fog、IP 对讲 BAS-IP、IP 话机 Fanvil；经销商计划）', 'Hikvision / Dahua / Tiandy / Teletek 销售与技术服务'],
    address='İnkılap Mah. İlkkurşun Cad. No 83/A-B, Ümraniye / İstanbul', accounts='—', accounts_due='—', size_band='小型（人数未取）',
    officers=['Ali Yıldız — 研究档 KP ali.yildiz@（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**有进口经验的品牌分销商（IP 对讲 + IP 话机 = 天然 PoE 交换机配套需求）→ 分销 20%**：STC-028GP / STC-228GP / STC-2224GP（PoE 预算满足 BAS-IP 面板 / Fanvil 话机；VLAN / QoS 语音优先）+ STI-144GP（室外门禁柜）；加厚一次（配套方案价表）',
           '收件人 ali.yildiz@ 点名 satın alma / genel müdür；表内 1 次跟进无回复 → 第二次触达换主题「PoE switches sized for IP intercom and IP phone deployments — a dealer-programme price list」；发信窗口 Thu 10–12 TRT；下轮补项：Vergi No / MERSİS；升 A 次候选'],
    notes='分销 20%；进口经验；加厚一次；部分坐实。')
put('SB-668', key='tr', batch=B, name='Midosa（midosa.com.tr；土耳其）— 研究档 KP Taner Şahin tanersahin@（电话 +90 544 …）；官网 http_error；**本轮 1 次检索未命中任何登记 / 名录条目 → 未坐实**', iso='TR', fetched=F,
    source='TR · 1 次检索（关键词 Midosa midosa.com.tr Taner Şahin 公司 vergi no）→ 仅返回 ITO 新设公司名单、HİB 名单、Midas Menkul 等无关条目；按「1 次未中即停」规则不再追；业务范围沿用研究档（待核）',
    url='https://midosa.com.tr/',
    number='未坐实（登记主体未取）', status='站点 http_error（研究档快照）', incorporated='未取', company_type='未取',
    sic=['IT / 网络（研究档待核）'],
    address='土耳其（门牌未取）', accounts='—', accounts_due='—', size_band='未取',
    officers=['Taner Şahin — 研究档 KP tanersahin@（职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**未坐实 + 站点失效** → 只发一页纸（STC-228GP / STC-2224GP）一次，不回复即 `when=不动`；下轮补项：域名 whois / 站点恢复后 İletişim 页 Vergi No',
           '收件人 tanersahin@；表内 1 次跟进无回复；发信窗口 Thu 10–12 TRT'],
    notes='未坐实（1 次未中）；一页纸一次；低优先。')
put('SB-669', key='tr', batch=B, name='MNS Bilişim Hizmetleri San. ve Tic. Ltd. Şti.（mnsbilisim.com / 电商 mnspazar.com；İstanbul Şişli Mecidiyeköy）— 2005-07-07 成立的企业网络方案商 / 增值经销商（Ruijie Networks 与 Ubiquiti UniFi 土耳其授权销售 + 项目 / 安装 / 维护；RG-WALL 防火墙、Ruijie 6120 25G/40G 交换机）；Vergi No 6220446809（Zincirlikuyu）；**创始人 Mahmut Bektaş = 研究档 KP 本人**；11–50 人', iso='TR', fetched=F,
    source='TR · 1 次检索：mnspazar.com İletişim（MNS BİLİŞİM HİZ. SAN. TİC. LTD. ŞTİ.；Mahmut Bektaş；Mecidiyeköy Mh. Cemal Sahir Sk. Polat Mecidiyeköy İş Merkezi No 29 K:4 D:43 Şişli İstanbul；Vergi No 6220446809；Vergi Dairesi Zincirlikuyu；0 212 347 90 66；info@ / teknik@）+ EMIS（Mns Bilisim Hizmetleri San. Ve Tic. Ltd. Sti.；established 2005-07-07；İstanbul）+ ZoomInfo（Mahmut Bektaş — Founder，2005–；11–50 人；Harun Kara — Network Systems Specialist）+ 官网（Kurumsal Network Çözümleri；UniFi AP；Ruijie 6120；Ruijie 土耳其授权销售与方案伙伴）+ whois（域名 2005-04-09 创建）',
    url='https://www.mnspazar.com/iletisim',
    number='Vergi No 6220446809（Zincirlikuyu）；MERSİS 未取（推定 0622044680900001，未核）', status='Aktif（电商 2025 在线）', incorporated='2005-07-07', company_type='Limited Şirket（创始人 Mahmut Bektaş）',
    sic=['企业网络方案 / 增值经销（Ruijie、Ubiquiti 授权；防火墙 / 交换机 / AP / 布线；项目 + 维护）', '网络设备电商（mnspazar.com）'],
    address='Mecidiyeköy Mah. Cemal Sahir Sk. Polat Mecidiyeköy İş Merkezi No 29, K:4 D:43, Şişli / İstanbul', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Mahmut Bektaş — Founder / 业主 = **研究档 KP mahmut.bektas@ 本人**', 'Harun Kara — Network Systems Specialist'], psc='Mahmut Bektaş（推定）', charges='', prev_names=[],
    lines=['**Ruijie / UniFi 增值经销 + 老板本人收件 + 已卖 10G/25G → 集成商 25%（项目）+ 分销 20%（电商）**：STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM（对标 Ruijie 6120 系列价）+ STH-2C24XF-HSI（25G ToR）+ STC-110XGE；B BIG，**加厚**（对标价表）',
           '表内 1 次跟进无回复 → 第二次触达换主题「10G/25G switches priced against your current 6120 line — managed L3 on the STH line」（不点名 Ruijie）；发信窗口 Thu 10–12 TRT；升 A 候选（回信即 A）'],
    notes='集成商 25% + 分销 20%；KP = 创始人本人；B BIG；加厚；升 A 候选。')
print('b102 TR 7 written')
