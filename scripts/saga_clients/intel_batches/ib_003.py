#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-03（T29-U138 2026-10-30）· 北美第一批 5 户（Actelis 10-K / Simrex / Nelly's / Inaxsys / Vi-Link）。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-03'
ITEMS = [
    ('SB-831', '年报/财务', '10-K FY2025（SEC，2026-03）：Revenues $3,671K（2024：$7,760K）· Gross profit $1,218K · GAAP net loss $(8,261)K（2024：$(4,374)K）· R&D $2,638K · S&M $2,866K；收入下滑归因于 2024 年两年期软件服务续约与 Washington D.C. 大单', 'https://ir.actelis.com/sec-filings/all-sec-filings/content/0001213900-26-030942/ea0280379-10k_actelis.htm', '上市公司（NASDAQ: ASNS）；亏损扩大、现金紧张、Nasdaq 最低股价风险（StockTitan 摘要）→ 账期要紧、单量小'),
    ('SB-831', '人事变动', '10-K：As of December 31, 2025 approximately 51 employees and contractors, of which 39 full-time（13 sales & marketing / 20 R&D-engineering-operations / 6 G&A）；34 in Israel, 15 in the U.S., 1 Europe, 1 Asia', 'https://www.stocktitan.net/sec-filings/ASNS/10-k-actelis-networks-inc-files-annual-report-86520770001d.html', '美国 15 人中含 VP Sales Casey Hurley（我方联系人）'),
    ('SB-831', '年报/财务', 'stockanalysis：Q2 2026 revenue $1.13M（+20.3%）· TTM $4.10M（−22%）· FY2025 revenue by geography：North America $2.31M 62.8% / EMEA $1.14M 31.0% / APAC $228K 6.2% · Employees 37', 'https://stockanalysis.com/stocks/asns/revenue/', ''),
    ('SA-002', '领英公司页', 'LinkedIn：SIMREX Corporation · Wireless Services · Buffalo, New York（1223 William St）· 5 employees on LinkedIn（Shari Tona — Administration Manager）；ZoomInfo：Manufacturing / Telecommunication Equipment · 11–50 · $5.9M · founded 1996 · Frank Neuperger General Manager', 'https://www.linkedin.com/company/simrex-corporation', ''),
    ('SA-002', 'KP', 'ZoomInfo：Frank Neuperger — General Manager, SIMREX（我方既有 KP，职务核实）', 'https://www.zoominfo.com/c/simrex-corp/77234480', ''),
    ('SB-248', '领英公司页', "Indeed：Nelly's Security LLC · CEO Sean Nelson · 11 to 50 · Revenue $1M–$5M · 5807 S Garnett Rd Suite E, Tulsa OK；2008 年 Claremore 车库起家，2010 转新品，2015 迁现址", "https://www.indeed.com/cmp/Nelly's-Security-LLC-1", ''),
    ('SB-248', '供应商/品牌关系', "LeadIQ：Nelly's Security（Broken Arrow, OK；≈20 人）面向安防经销商批发：video surveillance, access control, alarm panels, home automation, PoE switches, networking tools；主营品牌 Uniview, L-Series, ZKTeco, Akuvox, 2GIG, Qolsys, PDK；含 NDAA-compliant 选项；经销商计划含 branding program", 'https://leadiq.com/c/nellys-security/5a1dac702300005c00a1b363', 'L-Series 疑为自有标 → PoE 交换机贴标口子；对方重视 NDAA 合规（我方信里不提 NDAA，只给规格）'),
    ('SB-248', '人事变动', "PitchBook：Nelly's Security · Year Founded 2008 · Status Acquired/Merged · Latest Deal Type Buyout/LBO · Employees 19 · Corporate Office 501 North Aspen Avenue, Broken Arrow, OK 74012", 'https://pitchbook.com/profiles/company/302313-43', '已被收购（LBO）→ 采购决策链可能变化，下次信里问「still the right contact?」'),
    ('SB-173', '领英公司页', 'LinkedIn：Inaxsys Security Systems · 1,687 followers · Security and Investigations · 11–50 employees（21 on LinkedIn）· Montréal, Québec（Saint-Léonard）· Founded 2004 · Specialties incl. POE network switches；distributor, developer and supplier of open architecture VMS, Access Control/Alarm, Megapixel IP camera and POE networking', 'https://ca.linkedin.com/company/inaxsys', ''),
    ('SB-173', 'KP', 'LinkedIn：Mark McRae — President；Alain Boisvert — VP International Sales & Product Development；Richard Foo — Sales Manager, Western Region；Juan Campos — Sales Manager, Central Region', 'https://ca.linkedin.com/company/inaxsys', 'Boisvert 管产品开发 = OEM 交换机规格对口人'),
    ('SB-173', '新闻/招标', 'LinkedIn 2026-09（Pipl Systems）：到访 Inaxsys 蒙特利尔拍 20 余年公司纪录片，提到 Mark McRae、Alain Boisvert、Muhammad Rahim；「grown into a manufacturer and distributor serving partners across Canada and the United States」', 'https://www.linkedin.com/in/mohammad-zamanpournpour-81907936/', ''),
    ('SA-006', '领英公司页', 'Crunchbase：Vilink Communications · Irvine, California · 11–50 · manufacturer of fiber optic digital transmission products · sales@vi-link.net · LinkedIn company/vilink-communications；NeverBounce：450 Goddard, Irvine 92618，约 25 名员工', 'https://www.crunchbase.com/organization/vilink-communications', ''),
    ('SA-006', '供应商/品牌关系', 'ProcessRegister：Vilink Communications, Inc.（Contact Robin Sun；旧址 2913 Saturn St. Brea CA）：产品线 analog/uncompressed/IP video over fiber、enterprise networks、ITS、media converter、video conferencing；NeverBounce 简介：unmanned vehicles / intelligent traffic systems / military applications；optical multiplexers；unmanaged industrial Ethernet switches', 'https://www.processregister.com/Vilink_Communications_Inc/Supplier/sid161883.htm', 'PI 成单户；有自牌非管理工业交换机线 → 管理型/PoE 是补位；军用应用守界只谈 ITS/企业'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
