#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-09（T29-U141 2026-10-30）· 土耳其收尾 6 户 + 北美 3 户 + 欧洲 6 户（年报/登记为主）。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-09'
ITEMS = [
    # ---- 土耳其
    ('SA-049', '登记', 'all.biz / 官网：Bosgem Otomasyon Ltd. Şti. · 旧址 Şerif Ali Mah. Yunus Sok. No:35/27 Y.Dudullu；现址 Cevizli Mah. Bağdat Cad. Çoşkunlar Sok. Dragos Center No:16-18/11 Maltepe/İstanbul · 0216 466 1 440 · info@bosgem.com；iotsistem.com 版权「2025 © BOSGEM OTOMASYON」', 'https://www.bosgem.com/bize-ulasin/', '法定主体 Bosgem Otomasyon Ltd. Şti.（研究档原「法定全称待补」已补）；网店 2025 年仍在维护'),
    ('SB-131', '展会/活动', 'Desecure Technology 官网：「Visit us at our booth from November 7-9, 2024, at TÜYAP … Solar Storage Istanbul 2024」—— 展示能源设施物理安防、远程监控、MAS（Mobile Alarm Stand）；Enerji Rehberi：亦参加 TÜREK 等能源展，23 şehirde aktif saha operasyonu', 'https://desecuretechnology.com/en/solar-storage/', '全国性私人安保 + 技术公司，主攻光伏/风电场安防（户外远程监控 = 工业 PoE 交换机场景）；每年 11 月 Solar Storage Istanbul'),
    ('SB-131', '供应商/品牌关系', 'Deviser 2025-06：Desecure——Alarm izleme merkezi, geçiş kontrol, video analiz, plaka tanıma ve kamera sistemleri「tam entegre güvenlik altyapısı」；自研移动产品 MIA（Mobil İzleme Aracı）/ MID（Mobil İzleme Direği）/ MAS', 'https://deviser.tech/2025/06/27/en-iyi-ozel-guvenlik-sirketi-desecure-ile-guvendesiniz/', '自有移动监控产品 = 需要紧凑工业交换机/光口（MID 移动监控杆）'),
    ('SB-140', '登记', '官网 / turgutreisrehberi：AG Bilgisayar · Yokuşbaşı Mah. Külcü Sok. Şeref Konday İşhanı No:29, 48400 Bodrum/Muğla · 0546 609 99 06；「10 yılı aşkın deneyimi」；业务：Bodrum güvenlik kamerası, ağ kurulumu, geçiş sistemleri, sunucu kurulumu, teknik servis（兼电脑维修）', 'https://ag-bilgisayar.com/', '博德鲁姆本地电脑维修 + 监控安装小店 → 微型，A-DEEP-03 下放 B'),
    ('SB-153', '登记', '未得：网查「sinerjik.net / Sinerjik / Ufuk Gökalp」只命中同名 SinerjiNet Bilişim A.Ş.、Sinerji BT 等无关公司；sinerjik.net 无可核官网', '', '1 查未得即停；身份不可核 → A-DEEP-03 下放 B'),
    ('SB-225', '登记', 'Shnrise Güvenlik Sistemleri（shnrise.com.tr，İstanbul；0850 840 68 01）：kamera, alarm, plaka okuma（LPR/ANPR）, PDKS, network altyapı；同一经营者另有 CESS Güvenlik Sistemleri（cessguvenlik.com：kamera / alarm / PDKS / network altyapı / yangın ihbar）', 'https://www.shnrise.com.tr/tr/hizmet/plaka-okuma-sistemleri-25', '两块牌子的小型安装商 → A-DEEP-03 下放 B'),
    ('SB-388', '登记', 'find.com.tr：FH GÜVENLİK SİSTEMLERİ VE BİLİŞİM SANAYİ TİCARET LİMİTED ŞİRKETİ · Kuruluş 13 Şubat 2025 · NACE 631108 · Sinanpaşa Mah. Süleyman Seba Cad. No:6 İç Kapı No:4 Beşiktaş/İstanbul；官网：「2025 yılında İstanbul’da kurulmuş … 15 yılı aşkın tecrübe」；技术办公室 Perpa Ticaret Merkezi B Blok Kat:11 No:1730 Şişli', 'https://www.find.com.tr/Company/fhguvenliksistemlerivebilisimsanayiticaretlimitedsirketi', '2025 年 2 月新注册的小型弱电集成商 → A-DEEP-03 下放 B（观察一年）'),
    # ---- 北美
    ('SB-143', '领英公司页', 'Datanyze / ZoomInfo：BroadStar · 3965 Investment Ln Ste A5, West Palm Beach, FL 33404 · CEO Tyler Bell（2009 至今）· Revenue $18.9M · 70 employees（ZoomInfo 51–200）· Founded 2004 · (561) 472-5022；CFO Howard Bernstein；Senior NOC Engineer Francisco Petazzi', 'https://www.datanyze.com/companies/broadstar/33904157', '佛州 FTTH/MDU 运营商，70 人 $19M——接入/汇聚交换机、SFP 的真实买家；NOC 工程师是技术对口'),
    ('SA-059', '供应商/品牌关系', 'Crunchbase：Data Connect Enterprise Inc · Olney, Maryland · 11–50 ·「A wide variety of products previously manufactured under the ctek, relcomm, synxcom, telenetics, and other names have been purchased by Data Connect, including intellectual property, manufacturing, and/or licencing rights」；GlobalSpec：parent of DSL Warehouse, ClickITDirect；地址 3405 Olandwood Ct, Olney MD 20832 · 301.924.7400', 'https://www.crunchbase.com/organization/data-connect-enterprise', '收购多家老牌工业调制解调器/延长器品牌的 IP → 自牌工业网络设备商，交换机外采贴牌对位'),
    ('SB-119', '领英公司页', 'RocketReach / ZoomInfo / D&B：WireStar Networks（WireStar, Inc.）· College Station, Texas（4156 State Highway 6 S）· President Kyle Leissner（2005 至今；Texas A&M BBA/MS）· 42 employees · Revenue $5.1M · unified communications, data and internet connectivity, television', 'https://rocketreach.co/wirestar-networks-profile_b40e3dbaffe3b8fd', '德州区域 ISP/电信，总裁本人是我方 KP'),
    # ---- 欧洲
    ('SA-011', '领英公司页', 'Prospeo / RocketReach：CXR Larus（美国 San Jose 分部，+1 408-573-2700）· Telecommunications · 11–20 employees · 年营收估 $1.6M · VP of Sales Bruce Bartley · 另有 Shanghai Manager Gary Lv、Molde（NO）Web Developer', 'https://prospeo.io/c/cxr-larus', '查到的是 CXR 集团美国侧（CXR Larus）；法国主体 CXR（Abondant）规模待另查；集团整体偏小'),
    ('SA-020', '登记', 'KRS-online：Bitstream Sp. z o.o. · Mełgiewska 7 lok. 9, 20-209 Lublin · NIP 9462508588 · REGON 060184269 · KRS 0000266288 · PKD 26.30.Z Produkcja sprzętu (tele)komunikacyjnego · 决策人 Dariusz Pietrzyk；EMIS：成立 2006-10-20，2021 年 40 人；Aplikuj：BitStream Sp. z o.o（KRS 0001010572，spółka akcyjna，2023-01-02 登记）', 'https://www.krs-online.com.pl/firma/1764805-bitstream-sp-z-o-o', '卢布林（不是研究档写的 Opole）数据传输设备制造商，40 人；2023 年疑改制为股份公司 → 扩张信号；OEM 伙伴对位'),
    ('SA-043', '年报/财务', 'proff.se / hitta.se：Direktronik Aktiebolag · org.nr 556281-9663 · Registreringsår 1986 · Nynäshamn（Konsul Johnsons väg 15）· Bokslut 2024-03：Omsättning 130 548 Tkr（−8.1%）· Resultat efter finansnetto 23 742 Tkr · Anställda 26（bolagsfakta：28，+1 vs 2023）· SNI 46521 Partihandel med elektronikkomponenter；经营范围含 import, tillverkning och försäljning av datakomponenter', 'https://proff.se/befattningshavare/direktronik-aktiebolag/-/-/5562819663/', '瑞典老牌进口分销商，年销 ≈1.3 亿瑞典克朗、利润率 ≈18%（现金充裕）；已在卖 Proxeet 的 PoE 注入器 → 自牌/多品牌采购老手'),
    ('SA-050', '年报/财务', 'bizraport（KRS 0000585900）：IMPAKT S.A. · 股本 60 761 002 PLN · 收入 152 188 554 zł（2025）/ 149 208 335 zł（2024）· 净利 8 624 996 zł · 雇员 112（2025，2023 年 107）；LinkedIn：Mosina, Wielkopolska · 1997 年 · 51–200 · 自有品牌 Genesis, Lanberg, Natec, Fury, Armac, Audictus · 6,800 SKU · 产品销往 40 国', 'https://www.bizraport.pl/krs/0000585900/impakt-spolka-akcyjna', '采购线索：Lanberg 是其网络品牌（交换机/线缆）→ 自牌交换机 OEM 直接对位；年销 ≈1.5 亿 PLN、112 人、仍在增员'),
    ('SB-103', '人事变动', 'XING：Yalcin Demirak — Head of Sales, Abetechs GmbH (GRUNDIG Security)，2017-09 → **2025-09 离任**（「Herstellung und Vertrieb von Sicherheitstechnischen Produkten. IP Cameras, TVI Cameras, NVR’s, DVR’s …」）；Dirk Reinders — Sales Manager（2018-06 至今，Erkrath）', 'https://www.xing.com/profile/Yalcin_Demirak', '销售负责人 2025-09 换人 → 下次信先问新的采购/产品负责人是谁'),
    ('SB-103', '登记', 'PRO-4-PRO：Abetechs GmbH: GRUNDIG Security · Steinhof 39, 40699 Erkrath · +49 211 53806832 · www.grundig-security.com；GRUNDIG 品牌授权经营的视频安防（IP/TVI 摄像机、录像机、VMS powered by C-WERK）', 'https://pro-4-pro.com/de/firma/30582-abetechs-gmbh-grundig-security.html', '品牌授权商（非 Grundig 集团）；PoE 交换机是其配套品类'),
    ('SB-910', '年报/财务', 'Le Figaro Entreprises / Xerfi / polesocietes：ETIC TELECOM · SIREN 380927475 · SAS · 创立 1991 · Montbonnot-Saint-Martin（Isère）· 10–19 salariés · CA：2 498 k€（03/2020）→ 4 964 k€（03/2021）→ 6 644 k€（03/2022）→ 6 M€（2023）→ **3 930 958 €（exercice clos 31/03/2025，résultat net 321 866 €）** · Délai de paiement fournisseur 106 jours（2023）', 'https://entreprises.lefigaro.fr/etic-telecom-38/entreprise-380927475', '采购线索：工业路由器/远程访问设备制造商，营收两年腰斩（6.6M→3.9M€）；对供应商付款周期 106 天 → 合作要前 T/T'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, bool(url))
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
