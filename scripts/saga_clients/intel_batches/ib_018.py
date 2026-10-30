#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-18（T29-U143 2026-10-30）· 中东 5 户 + 欧洲 7 户。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-18'
ITEMS = [
    ('SA-027', '领英公司页', 'LinkedIn / contactout / SignalHire：Al Salami Trading L.L.C.（AST）· founded 1989 by chairman Rashid Al Salami（Al Salami Group of Companies）· Dubai, Al Quds Street, Binsougat Building Office 8 · 11–50（13–19 可见）· electronic security & surveillance design/integration/installation · GM Nazeeh Naeem · 042650333', 'https://www.linkedin.com/company/al-salami-trading-establishment/', '迪拜老牌家族集团下的安防集成公司（≈15 人）；GM 直联'),
    ('SB-043', '登记', '2GIS / ReachUAE：Euro Technology（Euro Technology Civil Company）· 136 Al Zajil Street, Mezzanine Office 4, Al Danah, Abu Dhabi · Safety and security systems · Fax 026417333；RocketReach 另有「EURO® Technology Group」（interactiveeuro.co.uk，$7M / 9 人 / 1998）——是否同一主体未确认', 'https://2gis.ae/dubai/firm/70000001038659183', '阿布扎比安防集成商；规模按研究档 ≈9 人 / ≈$7M 采信（待官网核）'),
    ('SA-048', '年报/财务', 'alrajhitel.com / Crunchbase：Al Rajhi Telecom Company · Riyadh（7687 King Fahad Branch Road, Al Murabba）· Established 2014 as a subsidiary of Al Rajhi Building & Construction · 501–1,000 employees · ICT infrastructure / MEP / ELV / cybersecurity / data center & power · 10,000+ customers · showrooms Riyadh, Al Khobar, Jeddah · e-commerce ekhalas.com（2025-11 发文）· 目标「leading IT wholesale distributor in the Kingdom」', 'https://www.alrajhitel.com/about-us/', '沙特大集团（Al Rajhi）旗下 ICT 集成 + 分销 + 电商（500–1,000 人）——自身是分销方，按 K8 留 A；采购走正式供应商注册'),
    ('SC-097', '登记', 'ZoomInfo / ai3lines：Three Lines（3Lines Advanced Technologies）· King Abdullah Rd Fl 4, Riyadh · Aerospace & Defense · 51–200 · $5.4M · 「first licensed Saudi company specializing in the supply of aircraft spare parts, ground support equipment, and simulators … civil and military aircraft」· 另设 AI Division（sovereign AI）', 'https://www.zoominfo.com/c/three-lines/547055702', '航空国防 MRO 主业 → 守界，A-DEEP-09 下放 B'),
    ('SB-924', '登记', 'ZoomInfo / powrbot：INTRACOM Middle East（Intracom Middle East FZE/FZ-LLC）· Dubai, Bldg 3 Ofc 204 · 1–10 employees（Office Manager Oumou Keltoum、Engineer Mohammad Yaacoub、HR Director Sulaiman Rawther）· 母公司 Intracom Telecom（希腊电信系统厂商）', 'https://www.zoominfo.com/c/intracom-middle-east/369307611', '母公司项目办公室（2–10 人），采购在雅典总部 → A-DEEP-09 下放 B'),
    ('SA-072', '年报/财务', 'reportaziende / aziendeeasy：TRANS AUDIO VIDEO S.R.L. · P.IVA 01675270613 · Caserta（Viale Melvin Jones 12）· Data Iscrizione 1987-06-18 · Dipendenti 20–49（RocketReach 28）· Fatturato 2022 €22.3M → 2023 €23.7M → **2024 €17.96M（−24.2%）** · Utile 2024 €33.8K（margine 0.2%）· ATECO 46.43.3；「distribution company operating into Broadcast, Cinema, Pro Foto/Video and high-end CCTV」', 'https://www.reportaziende.it/trans_audio_video_srl_ce_01675270613', '采购线索：营收下滑 24%、利润见底 → 在找降本货源；高端 CCTV 分销线 → PoE 交换机配套'),
    ('SB-038', '登记', 'GoWork / pkt.pl：「TRICOMP」Sp. z o.o. · Al. Prymasa Tysiąclecia 78A, 01-424 Warszawa · KRS 0000121281 · NIP 5222477449 · REGON 016022377 · 2002 · 股本 50 000 zł · PKD 95.11.Z / 95.12.Z（电脑与电信设备维修）· contactpl@tricomp.com.pl', 'https://www.gowork.pl/tricomp-sp.-z-o.o.,29703/dane-kontaktowe-firmy', '华沙小型 IT/电信维修服务公司（股本 5 万 PLN）→ A-DEEP-09 下放 B'),
    ('SB-104', '年报/财务', 'ufficiocamerale：STS ITALIA S.R.L. · P.IVA 00865310247 · Via Spinelli 134, 20862 Arcore (MB) · REA 1490600 · Data Iscrizione 1984-05-11 · Dipendenti 73（2026）· Fatturato €7,973,181（2024）· Utile €438,664 · ATECO 432102 Installazione di cablaggi per telecomunicazioni e altre reti · PEC stsitaliasrl@pec.telemar.it；RocketReach：Security and Investigations，Silvio Stefani — Commerciale', 'https://www.ufficiocamerale.it/4755/sts-italia-srl', '米兰北郊 73 人安防/布线安装集成商，年销 €8M、盈利 → 集成 25% 档'),
    ('SB-542', '登记', 'implisense / D&B：LANOPIA GmbH · Amtsgericht München HRB 143448 · 2002-05-09 · Euphemiaweg 20a / Gewerbepark 23, 85250 Altomünster · Stammkapital €25,000 · Wholesale of electronic and telecommunications equipment（Datenkommunikationsprodukte）· Small enterprise（1–24）· GF Martina Ochmann，Partner Paul Ochmann', 'https://app.implisense.com/en/companies/lanopia-gmbh-altomuenster--DEIDEIEX1021', '巴伐利亚家族式数据通信批发商（小型）'),
    ('SB-193', '登记', 'online-handelsregister / cylex：DEMA Vertriebs-GmbH · Amtsgericht Stuttgart HRB 571318 · Gründung 1963-01-17 · Im Tobel 4, 74547 Untermünkheim · Kapital €800,000 · USt-IdNr. DE146279485 · WZ Elektroinstallationsmaterial (Großhandel), Industriemaschinen (Großhandel) · 07944 981010', 'https://www.online-handelsregister.de/handelsregisterauszug/bw/Stuttgart/HRB/571318/DEMA-Vertriebs-GmbH', '1963 年起的电气安装材料/工业设备批发商（资本 80 万欧）→ 交换机为电气批发品类扩展'),
    ('SB-342', '供应商/品牌关系', 'Crunchbase / LinkedIn：SURE Transport（sister of SURE24 Ltd，Bingham, Nottinghamshire，1992，11–50）· 「supplies and installs vehicle CCTV equipment for bus, coach, and van fleets」· SURE24：CCTV specialists，links with Police Technical Support Units, Government Agencies, Private Investigators（covert）', 'https://www.crunchbase.com/organization/sure-transport', '车载 CCTV（需 E-mark）+ 警务/隐蔽监控 → 品类与守界双重不对位，A-DEEP-09 下放 B'),
    ('SA-074', '年报/财务', 'papagal.bg / finansi.bg：ЕЛИТ - ТИМ - СЕКЮРИТИ ООД（ELITE TEAM SECURITY）· ЕИК 202351530 · 2012-12-07 · Враца, ж.к. Река Лева, ул. Остри връх 1 · 12 служители（2021）· оборот 248 999 €（2020）· 管理人 Радка Иванова / Тихомир Иванов · 业务：физическа охрана + СОТ + видеонаблюдение', 'https://papagal.bg/eik/202351530/4f70', '保安公司（12 人、年营业额 25 万欧）兼装监控 → 终端/微型，A-DEEP-09 下放 B'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
