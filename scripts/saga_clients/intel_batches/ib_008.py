#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-08（T29-U140 2026-10-30）· 北美/英国品牌商四家：BlueWARRIOR / DMSI / Megnet（Chimera）/ Versitron。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-08'
ITEMS = [
    ('SA-033', '供应商/品牌关系', '官网（页面日期 2021-11）：「Blue Warrior is rugged industrial Ethernet – built for harsh environments」；「DYMEC helps utility providers ensure the safety and security …」；应用：电信（数据中心到山顶基站）、水务/污水处理（冗余以太网 + VLAN + 冗余供电/上联）、农村电信 Q-Guard 激光雷达周界', 'https://bluewarrior.com/solutions/water-waste-treatment/', 'BlueWARRIOR 与 DYMEC 同站共述 → 同一体系的加固工业交换机品牌（白牌来源）；官网内容 2021 后未更新，需核活性'),
    ('SA-033', '供应商/品牌关系', 'Trafsig（交通信号分销商）产品页：「The BlueWARRIOR BlueKey™ System consists of robust locks, encrypted “intelligent” keys, and state-of-the-art web-based system software」', 'https://www.trafsig.com/products', '已有 ITS 渠道（Trafsig）在卖其产品'),
    ('SB-529', '领英公司页', 'Crunchbase：DMSI International（DIVERSIFIED MATERIAL SPECIALISTS, INC.）· Venice, Florida · 51–100 · 光纤连接产品制造（fiber hardware, optic cable, converters, splitters）· OEM & Contract Manufacturing（component-level products in-house，global manufacturing capabilities）· +1 941 244 0935 · info@dmsimfg.com', 'https://www.crunchbase.com/organization/dmsi-international', '自有制造 + 代工能力的光纤连接厂商；MC/交换机是其外采补位 → OEM 30% 对位'),
    ('SB-529', 'KP', 'ZoomInfo：Jeneth D’Alonzo — Chief Executive Officer；同事 Dustin Hall（我方 KP）、Brandon Woodward、Jeff D’Alonzo；官网：Randy Harris — Director, Data Center & Broadband Sales（828-320-7632，Randy.Harris@dmsimfg.com；我方 KP）；产品线 MMC / MDC（VSFF 连接器）、MTP、OMNIA、IllumiCore+', 'https://www.zoominfo.com/p/Jeneth-Dalonzo/1489666208', ''),
    ('SA-015', '领英公司页', 'LinkedIn：Megnet Limited · 5,083 followers · London · 11–50 employees（37 on LinkedIn）· Founded 2003 ·「Leading Global Distributor of OEM Compatible Networking Products and Solutions」· 自有品牌 Chimera（compatible transceivers 1G–400G，「produced in partnership with leading ISO compliant industry manufacturers」）· Specialties 含 switches, media converters, DAC/AOC', 'https://uk.linkedin.com/company/megnet-limited-specialist-global-supplier-of-compatible-network-solutions', '兼容光模块品牌商 = 中国 ODM 采购老手；交换机是其品类扩展口；每周有 LinkedIn 更新'),
    ('SA-015', 'KP', 'Prospeo：Megnet Limited · Mortlake Business Centre, 20 Mortlake High Street, London SW14 8JN · 21–50 · Key Contact Anna Penez — Global Account Director', 'https://prospeo.io/c/megnet-limited', ''),
    ('SB-826', '供应商/品牌关系', 'Ultimate Guide for Security Professionals：VERSITRON, Inc. · 83 Albe Dr Ste C, Newark, DE 19702 · Contact Greg Massott · 302-894-0699；「In 1958, VERSITRON established itself as the first and trusted source of fiber optic technology」；产品：Fiber Optic Modems、Transceivers、MicroModems、Media Converters（10/100、10/100/1000）、Ethernet Switches（5, 6, 8, 16, 24 port, Modular）、Fiber Optic Video Transmission', 'https://ultimateguideforsecurityprofessionals.com/Listing/Company/47908', '1958 年起的光纤品牌，交换机/MC 全系外采贴牌 → OEM 30%；Greg Massott 20 封往来是我方最活跃的美国品牌商对话'),
    ('SB-826', '新闻/招标', 'ACCESSWIRE 2025-01-07（Newark, Delaware）：「Enhancing AV Over IP Efficiency: Best Practices for Network Infrastructure」—— R.W. Tull, President of Versitron：「The right network switches and media converters are critical for seamless AV delivery」；联系人 Greg Massott sales@versitron.com', 'https://www.itnewsonline.com/news/Enhancing-AV-Over-IP-Efficiency-Best-Practices-for-Network-Infrastructure/27317', '总裁 R.W. Tull（我方 KP Richard W. Tull 核实）；2025 年仍在发 AV over IP 方向稿 + GitHub 产品页 SEO → 活跃推广中'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
