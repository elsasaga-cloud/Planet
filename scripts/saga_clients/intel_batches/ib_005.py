#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-05（T29-U139 2026-10-30）· 土耳其 Klasnet + 北美品牌商三家（Hardened Networks / American Fibertek / TC Communications）。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-05'
ITEMS = [
    ('SB-149', '登记', '官网：KLASNET İLETİŞİM VE GÜVENLİK · Üçevler Mah. Dumlupınar Cad. 120 A Nilüfer/BURSA · info@klasnet.com.tr · +90 224 443 55 27 · GSM +90 546 546 37 43；「Sektördeki 14 yıllık tecrübemizin verdiği güven ile 2021 yılında ticari faaliyetlerimize başlamış bulunmaktayız」；业务 Fiber Optik Kablolama / Kamera / Network / Güvenlik / Zayıf Akım 交钥匙项目', 'https://klasnet.com.tr/', '2021 年成立的布尔萨小型弱电/光纤布线承包商（创始人 14 年行业经验）；注意不要与 Şanlıurfa 的 klassnet.com.tr 网吧混淆'),
    ('SA-026', '供应商/品牌关系', '官网 Products：Hardened Networks / ITS Express Ethernet Switches —— 80 Series V3：HN-8004-16（Full Layer 3 OSPF/PIM/VRRP/BGP，4×USFP+ 1G/2.5G/10G，16×铜口，192 GB 背板）；HN-8042（Base L3，2×USFP+，2×ESFP，8×铜口，SHA-256，FIPS-197）；HN-MC-1000 媒体转换器；HN-3488 / HN-3416 已 EOL；「All ITS Express/Hardened Networks switches are on the Florida Approved Products List (APL)」', 'https://hardenednetworks.com/products/', '自有品牌 ITS 加固交换机全系（有白牌来源）；2026-06/07 页面仍在更新 = 活跃；佛州 DOT APL 门槛 → 我们做其下一代机型的 ODM 候选，规格对位 2.5G/10G 上联 + L3'),
    ('SA-026', '新闻/招标', '官网首页（2026-06-26 抓取日期）：「Hardened Networks switches have been specifically engineered to handle … 8k multi-cast, high bandwidth video applications」；渠道：Express Supply（expresssupply.us/hardened-networks）', 'https://hardenednetworks.com/', '8K 组播视频 = 交通摄像头骨干；经销商 Express Supply 可作第二触点'),
    ('SB-010', '领英公司页', 'LinkedIn：American Fibertek Inc. · 131 followers · Computers and Electronics Manufacturing · 11–50 employees（12 on LinkedIn）· Headquarters St Petersburg, Florida · Founded 1984；「manufactured in America … meeting all BAA compliance requirements … also offers a full array of sourced TAA compliant products」；产品含 Ethernet switches and fiber switches', 'https://www.linkedin.com/company/american-fibertek', '总部已在佛州圣彼得堡（研究档旧址 Edison NJ 需更新）；外采线要求 TAA 合规 → 中国产地不合规，只能走非 TAA 的商业线或海外产地；信里不提 TAA'),
    ('SB-010', 'KP', 'ZoomInfo：Donna Poulos — President（我方 KP 核实）；LinkedIn：Matt Poulos — Vice President, Operations & Strategy；Aaron Parise — Engineer；Ana L Rodriguez — Production expediter supervisor；ZoomInfo 营收估计 $8.4M', 'https://www.zoominfo.com/c/american-fibertek-inc/1736750', 'Poulos 家族企业；运营 VP 管外采'),
    ('SB-010', '供应商/品牌关系', 'Cience：「American Fibertek has hundreds of replacement products for IFS, Interlogix and Comnet」', 'https://www.cience.com/company/american-fibertek/-5146488774677515066', '定位 = IFS/Interlogix/ComNet 替代品供应商 → 其外采目录正是我们 MC/光口交换机的位置'),
    ('SB-787', '领英公司页', 'LinkedIn：TC Communications · 591 followers · Irvine, CA · 51–200 employees（47 on LinkedIn）· Founded 1991 ·「Integrating legacy devices onto modern networks. Made in the USA since 1991」· Specialties：Teleprotection, ITS, Carrier Ethernet, Power Utilities, Public Safety, Freight/Passenger Rail, Military Communications, SCADA；近 3 天帖：JumboSwitch TDM over Ethernet/IP 白皮书', 'https://www.linkedin.com/company/tccomm', '美国本土制造叙事 + 铁路/军方客群（守界只谈电力/ITS/SCADA）；入门工业交换机可 OEM 是研究档既有判断'),
    ('SB-787', 'KP', 'LinkedIn / explorium：Steve Cragg — Vice President Sales Marketing（我方 KP 核实）；Ted Langford — Marketing and Sales Director；Ben Huai — Assistant Manager, Engineering；Scott Browder — Regional Sales Manager；Dean Maravilla — Account Manager；地址 17881 Cartwright Road, Irvine CA 92614；营收 $5–10M，≈54 人', 'https://www.explorium.ai/manufacturing/companies/tc-communications', ''),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
