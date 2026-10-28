# -*- coding: utf-8 -*-
"""第 103 批（T29-U96，2026-10-28）TR 8 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 103
F = '2026-10-28'

put('SB-670', key='tr', batch=B, name='Monkas Bilişim Teknolojileri A.Ş.（monkas.com.tr；**安卡拉 Yenimahalle**，非伊斯坦布尔）— 安防摄像机 / 网络设备网店与进口商（Hikvision / HiLook、Dahua、TP-Link、ZKTeco；海关库 2022 起 99 条进口记录）；KP Murat（murat@）；MERSİS / 税号未取 → 部分坐实', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 İletişim（Monkas Bilişim Teknolojileri A.Ş.；Çamlıca Mah. Anadolu Blv. Timko 1 Sokak No:20 A-5 Yenimahalle / ANKARA；info@monkas.com.tr）+ whois（MONKAS BİLİŞİM TEKNOLOJİLERİ ANONİM ŞİRKETİ；çamlıca mah. anadolu bulvarı A blok 20A/5 Ankara）+ yenifirma.com.tr（同名同址）+ 纽佰德海关库（2022-06-20 收录；99 条进出口记录；采购商 2 / 供应商 2）+ Instagram（0553 840 49 87；Hilook 推广）+ Facebook 员工页（Monkas Satış Pazarlama）',
    url='https://monkas.com.tr/iletisim',
    number='A.Ş.（Ankara 商事登记；MERSİS / Vergi No 未取 → 部分坐实）', status='Active（站点在线、Instagram 活跃）', incorporated='未取（域名 ≥2020）', company_type='Anonim Şirket（股份公司；私有）',
    sic=['安防摄像机 / NVR / 网络设备 / 门禁 零售批发网店（Hikvision / HiLook / Dahua / TP-Link / ZKTeco；Wi-Fi、光纤配件）+ 直接进口'],
    address='Çamlıca Mah. Anadolu Blv. Timko 1 Sok. No:20 A-5 (Tekno Bilgisayar İş Merkezi), 06200 Yenimahalle / Ankara', accounts='—', accounts_due='—', size_band='小微（推定 <10 人）',
    officers=['Murat — 研究档 KP（murat@；职务未核）', 'Hande Beyaz — Satış Pazarlama（Facebook）'], psc='未取', charges='', prev_names=[],
    lines=['**安卡拉安防网店 + 自行进口（海关记录 99 条）→ 采购型 small，分销 20%**：STC-028GP / STC-228GP / STC-2216GP 作其 HiLook / Dahua 摄像机配套 PoE（对标 TP-Link 价）；一页纸；不加厚',
           '收件人 murat@ 点名；表内 1 次跟进无回复 → 二次触达换切口「PoE 交换机配摄像机套餐」；发信窗口 Thu 10–12 TRT；城市改安卡拉（研究档地址待修）'],
    notes='采购型 small / 分销 20%；一页纸；城市 = 安卡拉。')
put('SB-691', key='tr', batch=B, name='Vitel Veri İletişimi ve Telekomünikasyon Sistemleri A.Ş.（Vitel A.Ş.；vitel.com.tr；伊斯坦布尔 Kadıköy）— 1993-01-08 成立的土耳其增值 IT 分销商（企业 / SMB / 工业网络、视频会议、软件、服务器存储、IoT；ManageEngine 土耳其独家分销 20 年；Yamaha、CrowdStrike；Bilişim 500（2024）总榜第 93）；51–200 人（≈90）；KP Gökhan Kanat', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 Hakkımızda（1993 年起增值分销商；30 年；5,000+ 企业网络）+ 官网首页（İlk 500 Bilişim Şirketleri 2024：Genel 93. / İstanbul 75.）+ kariyer.net（法定名 VİTEL VERİ İLETİŞİMİ ve TELEKOMÜNİKASYON SİS. A.Ş.；1993-01-08 成立）+ LinkedIn（Bilgisayar Ağları Ürünleri；51–200；İstanbul；1993；Özel Şirket）+ ContactOut（19 Mayıs Mah. İnönü Cad. Yıldız Sok. STFA Blokları B7 Blok No:17/1, 34736 İstanbul；90 人）+ RocketReach（+90 216 464 50 00；$6.3M）+ Great Place To Work 认证页 + ManageEngine Partner 页（2006 起独家分销）',
    url='https://www.vitel.com.tr/hakkimizda/',
    number='A.Ş.（İstanbul 商事登记；MERSİS 未取）', status='Active（Bilişim 500 2024 在榜）', incorporated='1993-01-08', company_type='Anonim Şirket（私有）',
    sic=['增值 IT 分销（企业 / SMB / 工业网络、视频会议、软件 ManageEngine、服务器存储、IoT）+ 培训与技术支持；经销商网络'],
    address='19 Mayıs Mah. İnönü Cad. Yıldız Sok. STFA Blokları B7 Blok No:17/1, 34736 Kadıköy / İstanbul', accounts='第三方 $4.8–6.3M（仅作区间，疑低估）', accounts_due='—', size_band='中型（51–200 人）',
    officers=['Gökhan Kanat — 研究档 KP（gokhan.kanat@；职务未核）'], psc='未取', charges='', prev_names=[],
    lines=['**30 年增值 IT 分销商，有「工业网络」线 → 分销 20%，B BIG（土耳其四主战场之一）**：STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W + STI-288DGGPM 作其网络线的价值档；一页纸 + 产品线卡，加厚一次（产品经理 / 新品牌引入路径）',
           '收件人 gokhan.kanat@ 点名；表内 1 次跟进无回复 → 二次触达换切口「a value line under your networking portfolio, Turkey stock-free DAP」；发信窗口 Thu 10–12 TRT；升 A 候选（回信即 A）'],
    notes='分销 20%；B BIG；加厚一次；升 A 候选。')
put('SB-858', key='tr', batch=B, name='Areskom İletişim Sistemleri Tic. Ltd. Şti.（areskom.com.tr / areskom.com；伊斯坦布尔 Üsküdar）— 2004 年成立的工业通信增值分销商（**Westermo 土耳其官方分销**、Teltonika、Etic Telecom、Acromag、Lanner、Atop、Sena、Welotec、Systembase、Tektelic；轨交展商）；仅 info@ / satis@', iso='TR', fetched=F,
    source='TR · 1 次检索：官网首页 / Hakkımızda（Kuruluş Yılı 2004；Altunizade Mh. Kısıklı Cd. No:35/1 Kat 1 Üsküdar / İSTANBUL；+90 216 428 78 78；2004-2026 Areskom İletişim Sistemleri Tic.）+ areskom.com（Areskom Communication LTD；Ataşehir Ata 2-3 Plaza 地址；Value Added Distributor since 2004）+ westermo.com Where to buy（Türkiye Distributor：Areskom Iletisim Sistemleri）+ Eurasia Rail 2025 展商（与 Westermo 同展位）+ 2. Rail Industry Show 公告 + all.biz / alo118（旧址 Muhittin Üstündağ Cad. No:23 Koşuyolu Kadıköy；satis@areskom.com.tr）',
    url='https://areskom.com.tr/',
    number='Ltd. Şti.（İstanbul 商事登记；MERSİS 未取）', status='Active（2026 版权；Westermo 官方分销名录）', incorporated='2004', company_type='Limited Şirket（私有）',
    sic=['工业通信 / 数据通信增值分销（工业以太网、远程接入、M2M / LTE 路由、IoT；Westermo 主线）；行业：轨交、工厂自动化、油气、能源'],
    address='Altunizade Mah. Kısıklı Cad. No:35/1 Kat 1, Üsküdar / İstanbul（另 Ataşehir Ata 2-3 Plaza B2 Blok No:6/59）', accounts='—', accounts_due='—', size_band='小型（推定 10–30 人）',
    officers=['无具名（仅 info@ / satis@）'], psc='未取', charges='', prev_names=['旧址 Koşuyolu, Kadıköy'],
    lines=['**Westermo 官方分销 + 轨交重心 → 工业线被占、轨交守界** → **分销 20% 低概率，一页纸即止**：STI-054GP / STI-144GP / STI-288DGGPM 作其工厂自动化 / 油气客户的入门价位（不碰轨交、不点名 Westermo）；不加厚',
           '收件人 satis@ 点名 satış müdürü；表内「仅 info@」→ 首信一页纸；发信窗口 Thu 10–12 TRT'],
    notes='分销 20% 低概率（Westermo + 轨交守界）；一页纸。')
put('SB-862', key='tr', batch=B, name='Cebeci Teleteks San. ve Tic. Ltd. Şti.（Cebeci Grup；cebecigrup.com；伊斯坦布尔 Şişli Okmeydanı）— 1978 年以 Cebeci Telefon 起家、1995 年改制 Ltd. 的光纤 / 电信测试与接入设备分销商（OTDR / 光功率计、熔接与配线、Greenlee 工具、**自有 Cifocs 光纤 USB 转换器**；HTK 通信技术集群成员；e-Mağaza）；11–50 人；Hakan Cebeci（hakancebeci@）；KP Mustafa Engin', iso='TR', fetched=F,
    source='TR · 1 次检索：magaza.cebecigrup.com Hakkımızda（1978 Cebeci Telefon 起步，1995 Cebeci Teleteks San. ve Tic. Ltd. Şti.）+ Mesafeli Satış Sözleşmesi（法定名 + Halil Rıfat Paşa Mah. Yüzer Havuz Sok. No:8 D:24 Okmeydanı 34384 Şişli / İstanbul）+ 银行账户页（户名 Cebeci Teleteks San. ve Tic. Ltd. Şti.）+ HTK（Haberleşme Teknolojileri Kümelenmesi）会员页（hakancebeci@cebecigrup.com；+90 212 320 08 88 / +90 532 377 42 42）+ globalpiyasa（Limited Şirket；11–50；Üretici）+ 官网 Cifocs 光纤 USB 转换器页',
    url='https://magaza.cebecigrup.com/author/admin/',
    number='Ltd. Şti.（İstanbul 商事登记；MERSİS 未取）', status='Active（2025 站点更新）', incorporated='1995（Ltd.；1978 起家）', company_type='Limited Şirket（私有；Cebeci 家族）',
    sic=['光纤 / 电信测试仪表与接入设备分销（OTDR、OPM、OLS、熔接、配线箱、Greenlee / Tempo 工具）+ 自有 Cifocs 品牌光纤转换器 + e-Mağaza B2B'],
    address='Halil Rıfat Paşa Mah. Yüzer Havuz Sok. No:8 D:24, 34384 Okmeydanı, Şişli / İstanbul', accounts='—', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Hakan Cebeci — 负责人（HTK 联系人；推定 Genel Müdür）', 'Mustafa Engin — 研究档 KP（mustafaengin@；职务未核）'], psc='Cebeci 家族（推定）', charges='', prev_names=['Cebeci Telefon（1978）'],
    lines=['**光纤分销 + 自有 Cifocs 品牌 → 分销 20%，可谈 Cifocs 贴标**：STI-144GP / STC-228GP / STC-110XGE / STC-2224GP（光口交换机 / MC 替代，挂 Cifocs 标 OEM 30%）；一页纸 + 贴标条款，加厚一次',
           '收件人 mustafaengin@ + 抄 hakancebeci@；表内无跟进 → 首信一页纸；发信窗口 Thu 10–12 TRT；升 A 次候选'],
    notes='分销 20% / Cifocs 贴标可谈；加厚一次。')
put('SB-864', key='tr', batch=B, name='DAC-EL Elektrik Elektronik Mühendislik Sistemleri San. ve Tic. Ltd. Şti.（DACEL Mühendislik；dacel.com.tr / dacelsolutions.com；伊斯坦布尔 Esenler + Ataşehir）— 1995 年奠基的工业自动化产品分销 + 交钥匙集成商（Belden Preferred Partner 2010 起：Hirschmann / Belden / Macmon；Aveva、Banner、Lumberg、Wecon、Autonics、American Fibertek；弱电：CCTV、火灾探测）；≈32 人；KP Ibrahim Gokcen / Erkan Cirit', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 Kurumsal（DAC-EL Mühendislik Ltd Şti 1995 奠基；工业 / 楼宇 / 交通自动化）+ 官网首页（Çözüm Ortakları：Aveva、Belden、Hirschmann、Macmon、American Fibertek、Banner、Lumberg、Wecon、Xecro、Autonics；Avrupa Yakası Merkez Oruçreis Mah. Tekstilkent Cd. A-08 No:10 AM/Z08-9 34235 Esenler；Anadolu Yakası Atatürk Mah. Erzincan Sok. No:6 Ataşehir）+ dacelsolutions.com Firma Profili（0212 210 76 46；info@dacel.com.tr）+ ContactOut（法定名 DACEL ELEKTRİK ELEKTRONİK MÜHENDİSLİK SİSTEMLERİ SAN VE TİC LTD ŞTİ；1995；32 人）+ 博客（2010-11 受邀 Belden Preferred Partner Programı）+ 2026-09 Robotik Otomasyon Çözümleri 参展',
    url='https://www.dacel.com.tr/kurumsal',
    number='Ltd. Şti.（İstanbul 商事登记；MERSİS 未取）', status='Active（2026-09 参展）', incorporated='1995', company_type='Limited Şirket（私有）',
    sic=['工业自动化产品分销与技术服务（PLC / HMI / SCADA / 驱动 / 工业网络 Hirschmann）+ 交钥匙自动化工程 + 弱电（CCTV、火灾探测、门禁）'],
    address='Oruçreis Mah. Tekstilkent Cad. Tekstilkent Sanayi Sit. A-08 Apt. No:10 AM/Z08-9, 34235 Esenler / İstanbul（另 Ataşehir）', accounts='第三方 $222K（明显低估，不采）', accounts_due='—', size_band='小型（≈32 人）',
    officers=['Ibrahim Gokcen — 研究档 KP（info@；职务未核）', 'Erkan Cirit — 研究档 KP（ecirit@；职务未核）', 'Ali Icoez — 研究档 KP（无邮箱）'], psc='未取', charges='', prev_names=[],
    lines=['**Belden / Hirschmann 优选伙伴（工业线被占）+ 自己做弱电交钥匙 → 集成商 25%，弱电侧切入**：STC-028GP / STC-228GP / STC-2224GP（CCTV / 门禁项目 PoE）+ STI-054GP（非 Hirschmann 预算的边缘点位）；一页纸；不加厚',
           '收件人 ecirit@ 点名 Erkan Cirit，抄 info@；表内无跟进 → 首信一页纸；发信窗口 Thu 10–12 TRT'],
    notes='集成商 25%（弱电侧）；一页纸；Hirschmann 伙伴。')
put('SB-879', key='tr', batch=B, name='MCS Factory Digitalization Endüstriyel Bilişim Teknolojileri Ltd. Şti.（MFD / MCS Otomasyon；mfd.com.tr / mfdstore.com；伊斯坦布尔 Ümraniye）— 2016 年成立的工厂数字化 / 工业 4.0 小型集成商（Siemens 解决方案伙伴：S7-1500 交钥匙、CodeMaster 生产效率平台、SCADA、RF200/300/600；MFD Store 网店）；≈4 人；**KP Mustafa Cimic = Project Manager**', iso='TR', fetched=F,
    source='TR · 1 次检索：官网首页（MCS Factory Digitalization Endüstriyel Bil.Tek.Ltd.Şti.；Armağanevler Mah. Mithatpaşa Cad. No:148/13 34760 Ümraniye - İstanbul；0216 505 0 701；info@mfd.com.tr；© 2026）+ CodeMaster 页（Siemens çözüm ortağı ve Endüstri 4.0 partneri）+ RocketReach（2016 成立；4 人；Mustafa Cimic — Project Manager；Nazım Ergül — Software and Automation Engineer）+ Facebook 页 + mfdstore.com（同法定名、同址）；同名 MFD Yazılım（Tuzla）/ MFD Akaryakıt / MFD İnşaat = 他家，不采',
    url='http://www.mfd.com.tr/',
    number='Ltd. Şti.（İstanbul 商事登记；MERSİS 未取）', status='Active（2026 版权）', incorporated='2016', company_type='Limited Şirket（私有）',
    sic=['工厂数字化 / 工业 4.0 系统集成（Siemens PLC / SCADA / MES 数据平台 CodeMaster、工业网络）+ 网店 MFD Store'],
    address='Armağanevler Mah. Mithatpaşa Cad. No:148/13, 34760 Ümraniye / İstanbul', accounts='第三方 $3M（仅作区间）', accounts_due='—', size_band='小微（≈4 人）',
    officers=['Mustafa Cimic — Project Manager = 研究档 KP 本人', 'Nazım Ergül — Software and Automation Engineer'], psc='未取', charges='', prev_names=[],
    lines=['**4 人 Siemens 伙伴 SI（项目制、工业网络 Scalance 预算型）→ 集成商 25% small，一页纸即止**：STI-054GP / STI-144GP / STI-288DGGPM（Scalance 之外的边缘点位价位）；不加厚',
           '收件人 info@ 点名 Project Manager Mustafa Cimic；表内无跟进 → 首信一页纸；发信窗口 Thu 10–12 TRT'],
    notes='集成商 25% small；一页纸。')
put('SB-410', key='tr', batch=B, name='4S Elektrik Elektronik Telekomünikasyon İleri Teknoloji Ar-Ge Ltd. Şti.（Red Lion 名录作「4s Elektrik Elektronik Telekominikasyon İth. İhr. Paz. Tic. Ltd. Şti.」；4sltd.com.tr；**伊兹密尔 Konak**）— **Red Lion Controls 官方分销** + Thor Guard 雷电预警 / Secty / Dinnteco / Meteorage / Joslyn Clark / K-Surge 土耳其销售；行业：矿业、石化、港口海事、可再生能源、机场、国防（Roketsan / Aselsan 参考 → 守界）；研究档无 KP', iso='TR', fetched=F,
    source='TR · 1 次检索：官网首页 / Hakkımızda（4S Elektrik Elektronik Telekominikasyon İleri Teknoloji Ar & Ge Ltd. Şti.；İzmir；Thorguard / Secty / Dinnteco / Redlion Türkiye Satış；Roketsan、Aselsan 参考）+ redlion.net Distributor Locator（4s Elektrik Elektronik Telekominikasyon İth. İhr. Paz. Tic. Ltd. Şti.；Halkapınar Mahallesi 1203/5 İkiz Çarşı 2 Apt. No:3 B/B, Konak, İzmir 35170；info@4sltd.com.tr；+90 532 218 09 65）+ 官网 Contact（+90 850 223 47 62 PBX；4steknolojiltd@gmail.com）+ Elektrikport 签约采访（Thor Guard 美国品牌代理）',
    url='https://tst.redlion.net/distributors/4s-elektrik-elektronik-telekominikasyon-th-hr-paz-tic-ltd-ti',
    number='Ltd. Şti.（İzmir 商事登记；MERSİS 未取；两种商号写法）', status='Active（Red Lion 官方名录 2024；站点在线）', incorporated='未取', company_type='Limited Şirket（私有）',
    sic=['电气 / 电子材料销售与代理（Red Lion 工业自动化与网络、Thor Guard 雷电预警、浪涌保护、电机控制）；行业：矿业、石化、港口、能源、机场、国防'],
    address='Halkapınar Mah. 1203/5 Sok. İkiz Çarşı 2 Apt. No:3 B/B, 35170 Konak / İzmir', accounts='—', accounts_due='—', size_band='小微（推定 <10 人）',
    officers=['无具名（研究档无 KP；info@ / Gmail）'], psc='未取', charges='', prev_names=[],
    lines=['**Red Lion 官方分销（工业交换机线被占）+ 国防参考 → 守界、低概率** → **分销 20% 一页纸即止**：STI-054GP / STI-144GP / STI-0240GE 作矿业 / 港口 / 能源客户的入门价位（不碰国防、不点名 Red Lion）；不加厚；无回复 → `不动`',
           '收件人 info@ 点名 satış müdürü；表内无跟进 → 首信一页纸；发信窗口 Thu 10–12 TRT；城市 = 伊兹密尔'],
    notes='分销 20% 低概率（Red Lion + 国防守界）；一页纸后不动。')
put('SB-642', key='tr', batch=B, name='Apres Teknoloji（apresteknoloji.com.tr；伊斯坦布尔 Kartal + Pendik 门店 + 布尔萨 Osmangazi 分部）— 面向经销商网络的电子安防 + IT B2B 分销商（报警、火灾探测与灭火、结构化布线与网络、门禁、机柜；**BDCOM 分销**：Wi-Fi 6 / 室外 AP / 市政项目）；Genel Müdür İnanç Karabayır；法定商号后缀未见 → 部分坐实', iso='TR', fetched=F,
    source='TR · 1 次检索：官网 Hakkımızda（电子安防 + 信息技术产品向经销商供货；B2B 在线订货与收款；全球品牌土耳其分销）+ B2B Gizlilik / Satış Sözleşmesi（Firma Ünvanı APRES TEKNOLOJİ；Orhantepe Mah. Tekel Cad. No:32/C Kartal İSTANBUL；0850 305 25 99；info@；Bursa 分部 Hacı İlyas Mah. Celal Bayar Cad. No:46/A Osmangazi）+ LinkedIn İnanç Karabayır（Apres Teknoloji Genel Müdür；#BDCOM #WiFi6 #OutdoorAP #BelediyeProjeleri；Pendik）+ Yandex Maps（Apres Teknoloji Güvenlik Sistemleri；Çınardere Mah. Erenler Cad. 2A Pendik；+90 534 233 38 38）',
    url='https://www.apresteknoloji.com.tr/hakkimizda-s1',
    number='商号 APRES TEKNOLOJİ（法定形式 / MERSİS 未取 → 部分坐实）', status='Active（B2B 站点在线；LinkedIn 2025-10 活跃）', incorporated='未取', company_type='未取（合同主体仅写商号，疑个体 / Ltd.）',
    sic=['电子安防 + IT 产品 B2B 分销（报警、火灾、CCTV、结构化布线 / 网络、门禁、机柜；BDCOM 网络设备分销；经销商网络 + 市政 Wi-Fi 项目）'],
    address='Orhantepe Mah. Tekel Cad. No:32/C, Kartal / İstanbul（门店 Çınardere Mah. Erenler Cad. 2A Pendik；分部 Hacı İlyas Mah. Celal Bayar Cad. No:46/A Osmangazi / Bursa）', accounts='—', accounts_due='—', size_band='小型（推定 10–30 人）',
    officers=['İnanç Karabayır — Genel Müdür（LinkedIn，2K 关注）'], psc='未取', charges='', prev_names=[],
    lines=['**经销商网络 B2B 分销 + 已分销 BDCOM（中国品牌网络设备）→ 懂中国直采、价格敏感 → 分销 20%，可谈二线价位**：STC-028GP / STC-228GP / STC-2216GP / STC-2224GP（对标 BDCOM PoE 价）；一页纸 + 价格对照，加厚一次',
           '收件人 info@ 点名 Genel Müdür İnanç Karabayır；表内 1 次跟进无回复 → 二次触达换切口「a second PoE line beside your current one, DAP Istanbul, MOQ 1」；发信窗口 Thu 10–12 TRT；升 A 次候选'],
    notes='分销 20%（BDCOM 同类经销；价格敏感）；加厚一次；部分坐实。')
print('b103 TR 8 written')
