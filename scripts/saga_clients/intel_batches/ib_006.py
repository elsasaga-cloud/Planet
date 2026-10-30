#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-06（T29-U139 2026-10-30）· 欧洲四户：EMOS（CZ）/ Visiotech（ES）/ Case Communications（UK）/ Proxeet（CY）。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-06'
ITEMS = [
    ('SB-461', '年报/财务', 'Elektrotechnická asociace ČR 会员档：EMOS spol. s r. o. · Lipnická 2844, 750 02 Přerov · Zaměstnanců 290 · Obrat 2 115 mil. CZK；「V roce 2020 přesáhl konsolidovaný obrat holdingu EMOS 2,3 mld. CZK. V roce 2022 se společnosti EMOS staly součástí nadnárodní francouzské skupiny Legrand」', 'https://www.electroindustry.cz/clenska-zakladna/clenske-organizace/detail/921', '采购线索：2022 年起是 Legrand 集团成员（38,200 人）→ 采购可能走集团框架；要不要按「巨头子公司」降 B 请 Simon 定（K7）；EMIS：2025 年 250–499 人，2024 净销售 +5.01%'),
    ('SB-461', '供应商/品牌关系', 'EMIS / 协会档：自有品牌 EMOS——baterie, světelné zdroje a svítidla, prodlužovací přívody, svítilny, antény, multimetry, zvonky（家用电气为主）；子公司 SK / PL / SI / HU，出口覆盖 CEE', 'https://www.emis.com/php/company-profile/CZ/Emos_Spol_S_RO_en_1420136.html', '消费电气品牌商，网络产品不是主线 → 交换机只可能作为自牌配件品类进入；对位低'),
    ('SC-371', '年报/财务', 'Visiotech 招聘页（2025-04）：「VISIOTECH es el mayor distribuidor europeo de material de seguridad electrónica, AV y redes, con una facturación total aproximada de 140M de euros, más de 330 empleados y presencia comercial en la gran mayoría de los países de Europa Occidental, con la sede principal ubicada en Madrid」（2024 初版本：130M€ / 300+ 人）', 'https://empleo.visiotechsecurity.com/jobs/comercial-interno-canal-retail', '欧洲最大安防/AV/网络分销商之一，一年营收 +10M€；网络品类在其主营里 → 分销 20% 档的头部目标'),
    ('SC-371', '人事变动', 'LinkedIn Jobs：Delegado Comercial (norte de España) — 向 Director Comercial 汇报，负责 País Vasco 区域经销商/集成商/安装商渠道；Comercial Interno canal retail（Madrid，混合办公）', 'https://es.linkedin.com/jobs/view/delegado-comercial-norte-de-espa%C3%B1a-at-visiotech-3801952271', '持续扩销售团队 = 增长期'),
    ('SC-371', '领英公司页', 'KonaEquity：Visiotech · Torrejón de Ardoz, Madrid · founded 2007 · 263 employees（2024-12 估）· distributes to companies in more than 10 countries · LinkedIn company/visiotech · X @visiotech_es', 'https://www.konaequity.com/company/visiotech-10402389140/', ''),
    ('SB-474', '登记', 'Endole（Companies House 数据）：Case Communications Limited · 03913540 · incorporated 26 January 2000 · Active · Micro（Turnover under £1M，Balance sheet under £500,000，Under 10 employees；2025-03-31 账目：Employees 3）· North’s Estate, Old Oxford Road, Piddington, High Wycombe HP14 3BE · Founder/PSC Andrew Thomas Saoulis', 'https://open.endole.co.uk/insight/company/03913540-case-communications-limited', '实际是 3 人微型公司（ZoomInfo「51–200 / $17.5M」失真，不采）；已加 Companies House 申报监控'),
    ('SB-474', '供应商/品牌关系', '1stdirectory：「Case Communications specialise in the design, development and manufacturer of ‘Street Hardened’ / Rugged communications products … Rugged Ethernet Switches – Fan less DC Powered, rugged 10 port Switches operating from -40C to +80C using X-Ring technology … 2 Gigabit combo / Mini GBIC SFP ports. SNMP managed」；ISO 9001；人员 Jan Corbett — Marketing Manager；VAT GB776 7485 65', 'https://1stdirectory.co.uk/companies/case-communications-ltd/', '自牌加固交换机（10 口 X-Ring）明显是白牌贴标 → 直接 ODM 对位 STI-288DGGPM 一类；3 人公司量小但英国主攻区'),
    ('SB-326', '供应商/品牌关系', 'Chiprian（Proxeet 新品牌）：「L3 switches with non-blocking architecture … Designed and assembled in Cyprus by Proxeet Ltd.」—— 10G 上联（S10G02）、24 电口（E01G24）、PoE af/at/bt 最高 90 W、Passive PoE 24/48 V、「your choice of open-source or proprietary OS」、802.1Qbb PFC、10G-KR', 'https://chiprian.com/mobile', '在塞浦路斯组装 L3 交换机 + 可选开源 OS → 主板/整机 ODM 候选（CENTEC/Marvell 方案正对位）；被动 PoE 24V 是其 ISP 客群需求'),
    ('SB-326', 'KP', 'RocketReach：Aleksei Kizriakov — Chief Executive Officer, ProXeet（Limassol；НГТУ 航空工程 1995–98；曾任 Daxinet、AlphaNet (Superdatch Ltd)、NEW Ltd）；Alexey Vasilenko — Lead Embedded Software Developer（Larnaca）', 'https://rocketreach.co/aleksei-kizriakov-email_793836745', '俄语背景工程师创业公司；嵌入式软件负责人在 = 能谈 SDK/OS 层'),
    ('SB-326', '登记', 'Direktronik（瑞典经销商）产品 PDF 的合规声明：Manufacturer PROXEET LIMITED · Cyprus, Paphos, 61 Neofytou Nikolaidi, Yiannis court, office 201, 8011 · +357-25100999 · info@proxeet.com；产品 iBlock Essential 便携中跨 PoE 注入器', 'https://www.direktronik.se/globalassets/_product-images--pdf/2.-kommunikation-datacenter/2.1-stromforsorjning/06.-power-over-ethernet-poe-90/poe-injektor-med-batteridrift.pdf', '已有北欧经销渠道（Direktronik）'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
