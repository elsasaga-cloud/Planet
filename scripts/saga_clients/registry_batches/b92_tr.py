#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 92 批 · TR 6 户（T29-U88，2026-10-28）：web_search depth 1 各一次（一户一查）。可重复运行（put 按 code 覆盖）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 92
put('SB-097', key='tr', batch=B, name='Lansan（lansan.com.tr；Şişli / İstanbul）', iso='TR', fetched=F,
    source='TR · 1 次检索：find.com.tr 工商镜像（ünvan / 类型 / 成立日 / 区）+ lansan.com.tr 首页（光纤配线架制造商自述）+ everychina「Shenzhen Lianxun High-Tech & LANSAN INTL LIMITED」（品牌 Lansan，200–300 人，2003）',
    url='https://www.find.com.tr/Company/lansanteknolojianonimsirketi',
    number='Mersis / VKN 未取', status='Aktif（域在用，2019-12 设立）', incorporated='2019-12-04', company_type='Anonim Şirket（多股东 A.Ş.）',
    sic=['网络连接器材批发 + 光纤配线架制造（SFP/QSFP/DAC、交换机、光纤、防雷、门禁、机柜、线缆）'],
    address='Şişli / İstanbul（街道地址未取）', accounts='—', accounts_due='—', size_band='小型（估 5–20 人）',
    officers=['董事会成员未取（A.Ş.；find.com.tr 不列姓名）'], psc='', charges='', prev_names=[],
    lines=['**2019 年底新设的多股东 A.Ş.，自有 Lansan 标签 + 自产光纤配线架 = 典型「有进口经验的自有品牌商」** → OEM 30% 线（MC 交换机 / 8–24 口 PoE 贴 Lansan 标），不走分销价',
           '**同名陷阱 / 供货链警示：深圳联迅（Shenzhen Lianxun）用「LANSAN INTL LIMITED」+ Lansan 品牌出口，成立 2003、200–300 人** → 土耳其 Lansan 极可能是该深圳品牌的土耳其公司 / 总代（名称完全一致、品类一致）→ 已有中国货源，PoE 交换机大概率也从同源拿 → 期望值调低：只给一页价 + 一款样机价，不再加厚',
           '信件写采购 / 产品经理（无官方姓名）；A.Ş. 多股东 = 签单在董事会，不必追个人'],
    notes='研究档「MC switch 自己的 logo」与本批「深圳 Lansan 品牌」相互印证：标签是他们的，货可能是深圳的。')
put('SB-100', key='tr', batch=B, name='Telkolink（telkolink.com；Perpa A Blok K.5 No:295-297 Şişli）= GelecekBT 同一老板', iso='TR', fetched=F,
    source='TR · 1 次检索：perpahaber / perpalife 商户名录（法定全名 + 楼层）+ telkolink.com/tr/iletisim.html（Satış yusuf@；Teknik sait@）+ LinkedIn Yusuf Ölçer（Gelecekbt.com General Manager；GelecekBT 为 Telkolink / CLR / ONET 土耳其分销）+ RocketReach / Lusha（2004 年由 GYM Bilgi Teknolojileri 创立；1–10 人）',
    url='https://www.perpahaber.com/telkolink-gelecek-yonetim-merkezi/',
    number='Mersis / VKN 未取', status='Aktif（域 telkolink.com 在用，Perpa 名录 2024）', incorporated='2004（GYM Bilgi Teknolojileri 创立 Telkolink 品牌）', company_type='Limited Şirket',
    sic=['网络 / 光纤 / 电信产品批发 + 自有标签 Telkolink（光纤收发器、MC、PoE、配线）'],
    address='Perpa Ticaret Merkezi A Blok K.5 No:295-297（名录另记 K:4,5,6 No:0297）Okmeydanı Şişli / İstanbul', accounts='—', accounts_due='—', size_band='微型（1–10 人）',
    officers=['Yusuf Ölçer — Yetkili / General Manager（katalogrehberi 法定联系人；LinkedIn 同时任 Gelecekbt.com GM）= 老板 = 联系人', 'Sait（姓氏未取）— Teknik Destek sait@telkolink.com'], psc='', charges='', prev_names=['GYM Bilgi Teknolojileri（创立方 / 旧名，gym-tech.net）'],
    lines=['**Telkolink（自有标签）与 GelecekBT（gelecekbt.com，分销店）是同一老板 Yusuf Ölçer 的两块牌子** → Saga 侧 SB-100 + SB-275 + 外部 XB-C0688 **并成一线**：只写 yusuf@telkolink.com 一封，不许三处各发',
           '老板 = 联系人 = 拍板人，微型公司（≤10 人）→ 决策快但量小；研究档「合作很密切 / VC 自己牌子」→ **OEM 30% 走 Telkolink 标**（PoE 8/16 口 + MC），MOQ 1 箱、100% 预付',
           '2004 年起做光纤 / 电信产品，Perpa A Blok 老商户 = 稳定、不会倒；复盘月：按 TR 惯例季度看一次域与 LinkedIn'],
    notes='三处记录合一：SB-100（主）/ SB-275（gelecekbt.com 并线）/ XB-C0688（外部 CCTV 库，本批改 C 并线）。')
put('SB-105', key='tr', batch=B, name='Cenova Güvenlik（cenova.com.tr；Perpa B Blok K:8 No:902-904 Şişli）', iso='TR', fetched=F,
    source='TR · 1 次检索：cenova.com.tr hakkımızda + üyelik sözleşmesi（法定全名、地址、Şişli VD 2060665571）+ LinkedIn 公司页（2004 / 11–50 / 18 人）+ kariyer.net（25–49 人）+ guvenliksistemleri.gen.tr（Cenova + TIANDY 相机、Wisetech 报警 土耳其分销，bayi 导向）+ perpa.com.tr 名录',
    url='https://www.cenova.com.tr/sayfa/uyelik-sozle%C5%9Fmesi',
    number='VKN 2060665571（Şişli VD）', status='Aktif（2024 招聘、官网 / X 活跃）', incorporated='2002（业务起点；LinkedIn 记 2004）', company_type='Limited Şirket',
    sic=['电子安防批发 / 进出口（CCTV、DVR/NVR、报警、门禁；自有品牌 Cenova + TIANDY / Wisetech 土耳其分销）'],
    address='Perpa Ticaret Merkezi Elektrokent B Blok Kat:8 No:902-903-904, Şişli / İstanbul（客服 0850 333 66 82）', accounts='—', accounts_due='—', size_band='小型（16–49 人）',
    officers=['经理 / 股东姓名未取（官网不列）', 'Necla Güler — Genel Muhasebe Sorumlusu（datanyze）', 'Abdurrahman Erkarslan — Technical Supervisor（datanyze）'], psc='', charges='', prev_names=[],
    lines=['**Perpa 老牌安防分销，20 余年、16–49 人，自有品牌 Cenova（相机 / 录像机）+ TIANDY 总代** → **OEM 30%：PoE 交换机贴 Cenova 标**配自家相机套装；TIANDY 自带 PoE 交换机 = 他们现有基线，报价要落在 TIANDY 同口数以下',
           '关联店 Syscom Güvenlik（Perpa A Blok K:7 No:859）同一客服号 → 若回信来自 Syscom 不算新客户',
           '无公开老板姓名 → 写 satış / satın alma（采购）+ 抄技术主管；VKN 已取，可用于后续 e-fatura 对账'],
    notes='')
put('SB-174', key='tr', batch=B, name='Karer Güvenlik Sistemleri（karerguvenlik.com；Pendik / İstanbul）', iso='TR', fetched=F,
    source='TR · 1 次检索：PESİAD（Pendik 工商协会）会员页（法定全名 + 代表 Nurbaki KARATAŞ + 2006 + 1000 m²）+ ZoomInfo / RocketReach（CEO Nurbaki Karataş 2006–今；Samet Şahin 技术总监；11–50）+ DESi 经销商页（地址 Yayalar Atasever Cd No 44 Pendik）',
    url='https://www.pesiad.org.tr/firmalar/karer-guvenlik-sistemleri-sanayi-ve-ticaret-ltd-sti',
    number='Mersis / VKN 未取', status='Aktif（PESİAD 会员、X / Facebook 活跃）', incorporated='2006', company_type='Limited Şirket',
    sic=['报警 + 监控摄像系统 批发 & 零售（AHD/IP 相机、DVR/NVR、报警、网络设备）'],
    address='Yayalar Mah. Atasever Cd. No:44, Pendik / İstanbul（1000 m² 自有场地；0216 397 33 88）', accounts='—', accounts_due='—', size_band='小型（11–50；datanyze 13）',
    officers=['Nurbaki Karataş — CEO / 创始人（2006–今；PESİAD 会员代表）= 老板 = 联系人', 'Samet Şahin — Director of Technical Services', 'Ebru Tekin — Muhasebe（2021–）'], psc='', charges='', prev_names=[],
    lines=['**老板 Nurbaki Karataş 本人就是研究档里的 KP（info@）→ 写他，不用找别人**；20 年老店、1000 m² 仓 + 批零兼营 = 亚洲区安防小分销的标准样本',
           '研究档「打开 1 次」+ 商业 PoE 需求 → **分销 20%**：8/16 口 PoE（STC-028GP / STC-228GP）配相机套装，样机 1 台付费试；同城 Pendik 有 Netaş 等大客户不相干',
           '技术总监 Samet Şahin 可抄送（技术问题由他回）；复盘：TR 季度扫一次'],
    notes='')
put('SB-867', key='tr', batch=B, name='Erete Bilgi Sistemleri（erete.com.tr；Şişli / İstanbul）', iso='TR', fetched=F,
    source='TR · 1 次检索：erete.com.tr Hakkımızda（2001-12 成立；创始合伙人 Pınar Kabil / Murat Soyak / Timur Yıldız；「Network Okulu」培训）+ kariyer.net（法定全名 Erete Bilgi Sis. Dış Tic. ve San. Ltd. Şti.）+ xp-networks.com 分销商页（Güven Sok 4/2 Şişli；联系人 Murat Soyak）+ ZoomInfo（Murat Soyak = Kurucu Ortak；11–50）',
    url='https://www.erete.com.tr/Kullanici/Home/Hakkimizda',
    number='Mersis / VKN 未取', status='Aktif', incorporated='2001-12', company_type='Limited Şirket',
    sic=['网络基础设施产品分销（铜缆 / 光纤 / 配线到机箱交换机）+ 网络培训（Erete Network Okulu）'],
    address='Güven Sok. 4/2, Şişli / İstanbul（+90 212 212 81 03）', accounts='—', accounts_due='—', size_band='小型（11–50）',
    officers=['Murat Soyak — Kurucu Ortak（创始合伙人）= 联系人（murat.soyak@erete.com.tr）', 'Pınar Kabil — Kurucu Ortak', 'Timur Yıldız — Kurucu Ortak', 'Özen Taylanlı — 研究档 KP（职务待核）'], psc='', charges='', prev_names=[],
    lines=['**研究档 KP Murat Soyak 就是三位创始合伙人之一 → 信已经写到拍板层**；24 年老分销 + 自办「网络学校」= 行业口碑型公司，不是网店',
           '他们是 XP-Networks（研究档记 Etherwan）工业交换机分销商 = **已有工业 PoE 品牌线** → STI 工业 DIN 只能做「第二货源 + 低价位」：STI-154GP / STI-288DGGPM 报价对标 Etherwan 同口数 6–7 折，不要硬推 CENTEC',
           '分销 20%；三合伙人制 → 回信慢属正常，第二封隔 6 周；复盘 TR 季度'],
    notes='')
put('SB-866', key='tr', batch=B, name='Egemen Elektronik Güvenlik Bilgisayar Sistemleri San. ve Tic. Ltd. Şti.（egemenelektronik.com / egemendepo.com；Ümraniye）', iso='TR', fetched=F,
    source='TR · 1 次检索：EMIS 公司档（2013-07-25 注册；2025 年 10 人；地址）+ LinkedIn 公司页（2013 / 11–50；Levent Pişman Co-Owner）+ 官网 hakkımızda（2013-07 开业，团队 20 年经验）+ Crunchbase（法定名 / Active）+ RocketReach（7 人；Deryanur Bulun 销售、Kerem Albayrak 物流）',
    url='https://www.emis.com/php/company-profile/TR/Egemen_Elektronik_Guvenlik_Bilgisayar_Sistemleri_San_Ve_Tic_Ltd_Sti_en_14288247.html',
    number='Mersis / VKN 未取', status='Aktif（EMIS 2026-03 更新）', incorporated='2013-07-25', company_type='Limited Şirket',
    sic=['电气 / 电子安防设备批发（CCTV、报警、门禁、电脑系统；B2B 商城 egemendepo.com）'],
    address='Ihlamurkuyu Mh. Malazgirt Cd. Şendal Sk. No:1 Egemen Plaza, 34771 Ümraniye / İstanbul（0216 611 61 00）', accounts='—', accounts_due='—', size_band='微型 / 小型（7–19 人）',
    officers=['Levent Pişman — Co-Owner（LinkedIn，10 年以上）= 老板之一 = 联系人（研究档 KP satis@）', 'Hüseyin Akkuş — 员工（LinkedIn）', 'Belkız Çınar — 销售（研究档 KP）'], psc='', charges='', prev_names=[],
    lines=['**研究档 KP Levent Pişman = 共同所有人 → 直接写他**（satis@ 为公用箱，抬头写 Levent Bey）；自有「Egemen Plaza」楼 = 有点家底的 10 人批发商',
           '安防批发 + B2B 商城 egemendepo.com → **分销 20%**：8/16 口 PoE + 4 口 DIN，先上商城一两个 SKU；研究档「打开 1 次」→ 第二封换主题（价格表 PDF 一页）',
           '2013 年公司、ZoomInfo 营收 $0.5–1M 仅作量级参考 → 单笔 ≤ $3k，100% 预付或 50/50'],
    notes='')
print('TR 6 ok')
