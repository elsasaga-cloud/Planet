#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-13（T29-U142 2026-10-30）· 南亚：Sundar Techno（PI）/ United Control（PI）/ Vintron。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-13'
ITEMS = [
    ('SA-032', '供应商/品牌关系', 'sundartechno.com：SUNDAR TECHNO SOLUTIONS, INDIA（Bangalore；WA/MOB +91-9482081014；sales@sundartechno.com）产品线：Industrial Ethernet Unmanaged / Lite Managed / Managed Switches、DNV GL / Railway / Substation Certified Switches、10Gbps Core Switch、4G LTE Router、PoE、工业 PC/IIoT 网关、PLC/HMI/SCADA、传感器；「Make in India approach」', 'https://sundartechno.com/', 'PI 成单户：自牌 STS 工业交换机全系在售（含我们供的机型可能性）→ 持续 OEM；注意其页面标「Railway / Substation Certified」是其叙事，我们只供商用/工业线'),
    ('SA-032', '新闻/招标', '官网博客高频更新：2026-04-29「Firewall Suppliers in India」（STS 4/6 口无风扇防火墙硬件，pfSense/OPNsense/Sophos）、2026-05-16「Oil, Gas & Petrochemical Industrial Automation Solutions」（industrial Layer 3 switches、industrial PoE switches、redundant ring）', 'https://sundartechno.com/2026/05/16/oil-gas-petrochemical-industrial-automation-india/', '2026 年仍在做 SEO 内容营销 → 活跃；油气/管线是其目标行业（工业环网 + PoE）'),
    ('SB-006', '领英公司页', 'Crunchbase / RocketReach：United Control Engineers India Pvt. Ltd. · Greater Noida（Plot No. 218, Udyog Kendra 1, Ecotech 3）· Founded 2001 · 28 employees · Revenue $15.2M（2025）· Office@unitedcontrolengg.com · +91 9311150492；「distributor of Industrial Automation & Switchgears products along with panel building & System Integration … Authorized Channel partner of Delta, ABB, Eldon, BCH, Phoenix, Polycab, TTPL, Connectwell, Controlwell」；官网 2025-06：Schneider Electric 授权分销（VFD/PLC/HMI/Servo）', 'https://rocketreach.co/united-control-engineers-india-pvt-ltd-profile_b7dc2582c0cb47fa', 'PI 成单户：大诺伊达工业自动化分销 + 盘柜集成，28 人 $15M；Delta/ABB/Schneider 渠道 → 工业交换机随盘柜走量'),
    ('SB-189', '领英公司页', 'RocketReach：Vintron Informatics Ltd. · F-90/1 A, Okhla Industrial Area Phase-1, New Delhi 110020 · Founded 1991 · 74 employees · Revenue $19.3M（2025）· +91 11 4374 0000；ZoomInfo：Director & CEO Varun Gupta；clodura：CCTV camera, DVR, video door phones, smart TV box, video conferencing；区域销售经理多人（Vijay Gundecha、Raghvendra Singh）', 'https://rocketreach.co/vintron-informatics-ltd-profile_b5f6c9a9f42e8ef3', '德里 CCTV 制造商（自有 PoE 交换机线）：74 人 $19M，CEO Varun Gupta 可直联；OEM 30% 档'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
