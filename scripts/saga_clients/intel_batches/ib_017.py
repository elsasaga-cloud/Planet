#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-17（T29-U143 2026-10-30）· KSM（AU）/ Astel Digicom（PI）/ Tecpro（AE）/ Larch Networks（IL）。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-17'
ITEMS = [
    ('SB-949', '登记', 'ksm.com.au：KSM Australia Pty Ltd · ABN 98 071 589 690 · Suite 18, 12 Tryon Rd, Lindfield NSW 2070 · 02 8003 3372 · 「Established in 1995, KSM Solutions is a supplier of both active and passive network products … Managed Industrial Switches L2, L2+ & L3, Industrial PoE Fibre Media Converter, SFP, PoE Switches」', 'https://www.ksm.com.au/about-us/', '悉尼工业网络产品供应商（在售白牌工业 L2/L3 管理交换机 = 换源对位）'),
    ('SA-001', '登记', 'ExportersIndia：ASTEL DIGICOM ELECTRONICS LLC · Shop no 22, Baghlaf Building, Satellite Market, Dubai · Year Established 2012 · Total Employees 5–10 · Annual Revenue US$1M–2.5M · Top markets Africa 70% / Mid East 20% / Eastern Europe · Contact Sanjay Singla · 主营 Coaxial / Fiber Optic / Security Cables, Fiber Optic Equipment, Media Converters', 'https://www.exportersindia.com/ae/astel-digicom-electronics-llc/about-us.htm', 'PI 成单户：迪拜卫星市场线缆/光纤贸易商（5–10 人，年销 $1–2.5M），7 成出口非洲 → 我们的货经其转非洲'),
    ('SA-051', '领英公司页', 'RocketReach / contactout / provilink：Tecpro Solutions Co. L.L.C. · founded 2003 Al Ain · offices Abu Dhabi, Dubai（Khalid Bin Waleed St）, Kochi（India）· 50–72 employees · est. revenue $6.5M · IT & ELV System Integrator & Distributor（TECPRO-Project / TECPRO-Distributions / Software）', 'https://contactout.com/company/Tecpro-Solutions-Co-LLC-74911', ''),
    ('SA-051', 'KP', 'contactout / RocketReach：Mohammed Rafi — Executive Director；Ahmed Salem Alrowahi — Executive Director；Musthafa — Director Sales & Operations；Abdul Rahiman Fahadh — Sales And Purchasing Manager（采购）；Praveen Parameswaran — Sales Manager（Dubai）；Sebin Varghese — Technical Sales Account Manager ELV（Abu Dhabi）', 'https://rocketreach.co/tecpro-solution-co-llc-profile_b45d2102fc62e2d2', '销售兼采购经理 Fahadh 是 ELV 配套交换机的采购对口'),
    ('SB-359', '领英公司页', 'ZoomInfo：Larch Networks Ltd · 11 Amal St, Rosh Ha’Ayin, Israel · 11–50 employees（C-level 6 / VP 3 / Manager 10 / 35 non-managers 可见）· Co-Founder & CEO Alexander Cheskis · CTO & Director Engineering Alexander Kaganovsky（2010 至今；ex Aricent / Flextronics Design Ukraine，Kyiv Polytechnic）· CMO Max Rassamakin · 团队含 Linux Kernel Developer（Dmitriy Zhuk，2018 至今）、Embedded Software Developer', 'https://www.zoominfo.com/c/larch-networks-ltd/355480109', '以色列交换机软硬件公司（基辅研发）：自牌工业交换机 + 定制固件能力 → 主板/SDK 级 ODM 对位；CTO 是技术决策人'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
