#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-10（T29-U141 2026-10-30）· 欧洲 5 户 + 俄语区 2 户 + 印度上市 HFCL + 2 户网查未得。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-10'
ITEMS = [
    ('SA-023', '年报/财务', 'bizraport：FCNET SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ · KRS 0001095976 · NIP 7542916466 · REGON 160150149 · ul. Św. Jacka 2, 45-073 Opole · 收入 10 241 580 zł（2025）/ 7 242 043 zł（2024）· 净利 1 833 945 zł · 股本 100 000 zł · PKD 27.31.Z 光缆生产 / 27.32.Z；董事会 Anna Joanna Frydel、Jarosław Krzysztof Cisowski、Krzysztof Marek Smugowski、Piotr Frydel', 'https://www.bizraport.pl/krs/0001095976/fcnet-spolka-z-ograniczona-odpowiedzialnoscia', '奥波莱光纤分销/制造商，收入一年 +41%、净利率 18% → 现金好、在扩张；自有 logo 采购户'),
    ('SA-034', '登记', 'monitorfirm / 官网：RFOG POLAND Tomasz Paszkowski · ul. Starogrodzka 1/2, 72-300 Gryfice · NIP 8571157213 · REGON 811833063 · 成立 2011-02-22 · 主业 Sprzedaż hurtowa sprzętu elektronicznego i telekomunikacyjnego；产品：光纤器件、SFP/GBIC、媒体转换器、复用器、WDM/DWDM、CATV 光传输、门禁/生物识别', 'https://www.rfog.pl/rfog,9,kontakt', '个体工商户（一人公司）形式的批发商 → A-DEEP-04 下放 B'),
    ('SB-077', '年报/财务', 'Validatis（Unternehmensregister，Jahresabschluss 2025 vom 20.05.2026）：LivEye GmbH · Amtsgericht Wittlich HRB 44506 · EUID DET2408V.HRB44506 · Bilanzsumme 37,9 Mio. € · Eigenkapital −22 Tsd. €（Eigenkapitalquote −0,1 %）· 2025 年平均 101 名员工 · WZ 46 Großhandel；DDW：Umsatz 3,5 Mio. €（估，偏低）· Inhaber/GF Marc Thurn · Europa-Allee 27, 54343 Föhren', 'https://www.validatis.de/unternehmen/liveye-gmbh-3022d228-ce61-41c3-b0dc-5f89ce48b5e2/', '采购线索：101 人、资产 3,790 万欧但净资产为负 → 靠股东/PE 融资扩张；设备采购活跃但要注意账期'),
    ('SB-077', '人事变动', 'Dealroom：LivEye GmbH 2018 年成立（品牌 2012 年由 Marc Thurn 注册，起于风电场安防）；Carsten Simons 加入共同领导；**2022-08 NORD Holding 收购多数股权**；从集成商转为自研硬件/软件制造商（移动监控塔 LivEye PRO / ONE、FIREGUARD 火情早期探测）；在波兰、瑞士、奥地利设子公司', 'https://app.dealroom.co/companies/liveye_gmbh', 'PE 控股 + 自研监控塔 → 塔内交换机/PoE 是明确的 OEM 配套位；决策人 Thurn / Simons'),
    ('SB-905', '领英公司页', 'LinkedIn：TELTRONIX - BRITICOM · Northampton · 1,978 followers · 11–50 employees（17 on LinkedIn）· Partnership · Founded 2004 ·「Certified & High-Quality Copper & Fibre Optic Passive Structured Cabling - Approved By Telecom Operators & Data Centres」· Specialties FTTH, GPON, Data Centre；contactout：24 人，HQ 7 Premier Court, Northampton NN3 6LF', 'https://uk.linkedin.com/company/teltronix', ''),
    ('SB-905', 'KP', 'contactout / LinkedIn / ZoomInfo：Justin Niles — Sales Director；Emil Etibarov — Sales Director, Country（2019 至今）；Mohamed Ben Abeda — International Sales Manager；Salim Diakhite — Regional Sales Manager, Africa French Speaking；Paul Green — Product Engineering Manager；Cedric Monnet — Procurement / Sourcing Specialist', 'https://contactout.com/company/TELTRONIX-BRITICOM-40818', '有专职采购 Sourcing Specialist（Cedric Monnet）和产品工程经理 → 无源布线品牌扩有源品类的对口人'),
    ('SB-160', '领英公司页', 'Datanyze / RocketReach / ZoomInfo：Linxcom UK Ltd · Leicester（3 Oakland Rd LE2 6AN）/ Daventry（Unit 3 Stephenson Close NN11 8RF）· Founded 2010 · 13–16 employees · Revenue $4.4–7M · Managing Director Mohamed Okba · Director Craig Blake（Queensland）· Director, Projects Jim Freeman · Technical & Sales Manager Aneesah Fataar（Johannesburg）· BDM Africa Zaid Mayat', 'https://www.datanyze.com/companies/linxcom-uk-ltd/354198590', '英国电信设备品牌/分销，销售团队布在南非/澳洲 → 面向非洲出口的渠道；MD Okba 是决策人'),
    ('SB-599', '年报/财务', 'checko / companium：ООО «СИМАНИТРОН» · ИНН 7720609470 · ОГРН 1087746277740 · Москва, ул. Руднёвка 17, оф. 103 · 生产/销售工业通信设备 · 收入 116,4 млн руб.（峰值）→ 64,2 млн руб.（2022，−45%，净亏 −6 млн）· 员工 4–5 人（2019–2020）· 总经理/创始人 Гришин Александр Владимирович；关联 ООО НПП «СИМАНИТРОН-ЭЛЕКТРОНИКА»（Саратов，生产，收入 52,6 млн руб.）', 'https://checko.ru/company/simanitron-1087746277740', '俄罗斯工业网络品牌 + 萨拉托夫生产子公司；莫斯科主体 4 人、收入下滑 → A-DEEP-04 下放 B（俄区二级，保留 B1）'),
    ('SA-066', '登记', '未得：网查「ccs-msk.ru」只命中同名「МСК」等无关公司；需以域名 whois / 官网 реквизиты 再核', '', '1 查未得即停'),
    ('SA-007', '登记', '未得：网查「Go Green IT Ltd gogreenit.net」命中的是 Doncaster 的 Go Green Ltd（运输/太阳能，270 人）——非本户；本户公司号 07614771 已在登记库（UK Companies House），申报历史已纳入 watch', '', 'PI 成单户；身份以 Companies House 07614771 为准'),
    ('SB-243', '年报/财务', 'HFCL 新闻稿（UFR Q4FY2024-25）：FY25 standalone Revenue ₹3795.22 Crores · EBITDA ₹475.79 Cr · PBT ₹241.43 Cr · PAT ₹194.75 Cr；Q4FY25 Revenue ₹800.72 Cr（Q-o-Q −20.87%，Y-o-Y −39.62%），Q4 standalone EBITDA −27.20 Cr、PAT −72.59 Cr；H1FY25 revenue ₹2251.85 Cr（+6.89% YoY）', 'https://www.hfcl.com/insights/news/press-release-on-ufr-q4fy2024-25-both-on-standalone-and-consolidated-basis', '采购线索：印度上市电信制造集团（自有 IO 标交换机，OEM 采购户）；FY25 Q4 急转亏损 → 采购收紧期；年报季报每季 NSE 公告（已排 watch）'),
    ('SB-243', '年报/财务', 'HFCL Inc.（美国子公司）FY2024-25 财报：Revenue $6,621,648（FY24：$1,149,000）· Cost of Sales $5,098,500 · 2025-03-31 working capital $(356,929)、net worth $(25,319)', 'https://www.hfcl.com/wp-content/uploads/2025/08/HFCL_INC_Financial%20Statements_FY2024-25.pdf', '美国子公司刚起量、净资产为负 → 美国市场扩张期'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, bool(url))
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
