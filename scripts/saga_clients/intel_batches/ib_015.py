#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-15（T29-U143 2026-10-30）· 南亚 8 户：Fastball（PI）/ Zekko / AGS Plus / Nivox / Areca / ITE / Core IT / Automation Systems。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-15'
ITEMS = [
    ('SB-1113', '登记', 'IndiaMART：Fastball · Established 2021 · Proprietorship · CEO Rishi Kumar Bansal · Upto 10 People · GST 2021 · Trader/Retailer of fiber splicers, joint enclosures, patch panels, PLC splitters；官网：Fastball Building, Unit A-61, Jhilmil Industrial Area, Delhi 110095 · Sales +91-9871 753 979', 'https://www.indiamart.com/fastball/profile.html', 'PI 成单户（gg）：德里光纤工具/配件贸易（≤10 人，个体）——A1 按成单保留'),
    ('SB-343', '登记', 'thecompanycheck / Tofler：Zekko Tech Private Limited · CIN U74999MH2016PTC285972 · incorporated 2016-09-16 · Navi Mumbai（Turbhe Industrial Park）· authorized & paid-up ₹1.00 lac · Employee Count 4 · Directors Chandrasekaran Iyer, Anjana Maju, Valli Malaichamy · mchamy@zekko.co.in', 'https://www.thecompanycheck.com/company/zekko-tech-private-limited/U74999MH2016PTC285972', '4 人、实缴 1 万卢比 → A-DEEP-07 下放 B'),
    ('SB-169', '登记', 'Facebook / ZoomInfo / X：AGS PLUS（agsplus.in）· Ghaziabad（Major Asharam Road, Sihani Rd, Ghukna）· 「Manufactur for Surveillance and Entrance Automation」· +91 7290005897 · 社媒 2023-10 起 · 营收 <$5M', 'https://www.zoominfo.com/c/agsagsplus/1327107504', '加济阿巴德小型监控/门禁贴牌商，规模无证 → A-DEEP-07 下放 B'),
    ('SB-111', '领英公司页', 'Crunchbase / IndiaMART / TradeIndia：Nivox Technologies · Bangalore（No.59, 5th Cross, Urbam 560086）· Registered 2011 · 51–100（Crunchbase）· 「manufacturer and supplier of rugged fiber optic products」· 自牌 Iveonet（光纤配线）+ Unmanaged / Managed / PoE Industrial Ethernet Switches、Media Converters、Video over Fiber · Founders Hemanth Kumar（Director）、Kavitha D.（Director & CEO）', 'https://www.crunchbase.com/organization/nivox-technologies', '班加罗尔光纤产品制造 + 工业交换机贴牌 → OEM 30% 档'),
    ('SA-063', '领英公司页', 'ZoomInfo / Tracxn：Areca Embedded Systems Pvt Ltd · Hyderabad（Plot 5B, Phase V, IDA Cherlapally）· ROC Hyderabad · Paid Up ₹4.65 Cr · 23 employees（ZoomInfo）/ 95（Tracxn EPFO 2024-02，波动大）· 岗位含 Senior RAMS and Validation Engineer、Embedded Firmware Engineer、Supply Chain Manager Kishore Guturi；2025-05 / 09 / 10 持续入职', 'https://www.zoominfo.com/c/areca-embedded-systems-pvt-ltd/426946019', '嵌入式系统设备商（RAMS 岗位暗示轨道信号领域——守界核对：若主业轨交则不追）；有供应链经理可直接对接'),
    ('SB-109', '领英公司页', 'ZoomInfo：International Technology Exchanger (ITE) · Lahore（Block G4/737 Khokhar Chowk, Johar Town）· established 2004 · 20 employees · LAN/WAN, network security, unified communications · partnerships Cisco, Fortinet, HPE · 客群 corporate / industrial / government；员工 Rashid Zia（Senior Network Engineer）、Muhammad Sulehri（Sales Executive，2006 至今）', 'https://www.zoominfo.com/pic/international-technology-exchanger/429968141', '拉合尔 20 人 SI（思科/飞塔渠道）'),
    ('SB-630', '登记', 'IndiaMART / Glassdoor：Core IT Solutions（CITS）· Mumbai（Sayba Palace, Mill Road, Kurla）· Partnership Firm 2010 · 11–25 人 · Annual Turnover ₹1.5–5 Cr · CEO Santosh（Khargotre）· 合伙人 Imran Usman Khan、Sarwar Alam Ansari · 在售 Techroutes Network Switch、网络安全、AMC', 'https://www.indiamart.com/coreitsolutionsmumbai/profile.html', '孟买小型 SI（营业额 ≈$0.2–0.6M）→ A-DEEP-07 下放 B'),
    ('SB-447', '供应商/品牌关系', 'automationsystem.in / Facebook：Automation Systems and Solution · Delhi（T-12, 3rd Floor, Pankaj Central Market, I.P. Extension, Patparganj）· incorporated 2007 · ISO 9001:2015 · 工业自动化制造/经销：传感器、GSM 路由器、Manage/Unmanage Ethernet Switch、FO converter、SFP；代理 Banner, Relpol, Profichip, EKS, Teltonika, Procon', 'http://automationsystem.in/', '德里工业自动化分销（含工业交换机品类）；规模未见，联系邮箱为 gmail'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
