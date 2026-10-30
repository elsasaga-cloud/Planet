#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-07（T29-U140 2026-10-30）· 北美第二批：Antronix / Optiview / 52 Networks（PI）/ EION / Epygi。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-07'
ITEMS = [
    ('SA-042', '领英公司页', 'Crustdata（2026-09）：Antronix · Cranbury, New Jersey（440 Forsgate Drive）· 33 employees · founded 1980 · Privately Held · headcount growth 0.0% YoY；compworth 估营收 $10.7M（41 人）；Cience：$5–10M，11–50', 'https://profiles.crustdata.com/company/antronix', ''),
    ('SA-042', 'KP', 'Crustdata Leadership：Neil Tang — President/CEO；Jim Taxdahl — Vice President of Sales（我方 KP）；Juan Bravo — Vice President of Sales；Andre Coulombe — VP Sales, Canadian Division；Jonathan Rigby — Director International Business Development；Cience：Ted Brown — Sales Executive', 'https://profiles.crustdata.com/company/antronix', 'CATV 无源/有源器件制造商（Olson Technology 是其加州分部 SB-984）；拓以太网交换机线的 OEM 目标——找 CEO Neil Tang / 国际 BD Rigby'),
    ('SA-021', '领英公司页', 'RocketReach：Optiview · Jacksonville, Florida（5211 Fairmont Street）· Revenue $5.3M（2025）· 17 employees · Founded 1999 · President Stephen Lebowitz；ZoomInfo：<25 人', 'https://rocketreach.co/optiview-profile_b44dcabbfd1f98a9', ''),
    ('SA-021', 'KP', 'SignalHire / RocketReach：Stephen Lebowitz — President（18 年）；Gary Bibeau — Director of Sales and Business Development；Georgia Fishel — Director of Marketing and Purchasing（采购）；Jaime Baas — Product Testing and Development Engineer；Zach Roth — Account Manager', 'https://www.signalhire.com/companies/optiview-inc/employees', 'Georgia Fishel 管采购 + 市场 = OEM 采购对口；Jaime Baas 做产品测试 = 样机对口'),
    ('SB-020', '登记', 'GSA eLibrary：52 NETWORKS, INC. · 5142 Meeting Pl, Woodbridge, VA 22193 · Contract 47QTCA22D00B3（MAS，Current Option Period End 2027-07-25，Ultimate 2042-07-25）· SAM UEI FV4KBSNE5S75 · NAICS 334111 · Small Business，SBA Certified Small Disadvantaged Business · uzair@52networks.com', 'https://www.gsaelibrary.gsa.gov/ElibMain/home.do/contractorInfo.do?contractNumber=47QTCA22D00B3&contractorName=52+NETWORKS,+INC.&executeQuery=YES', 'PI 成单户（gg）：联邦 GSA 供应商资格在手，到 2027 年有效'),
    ('SB-020', '新闻/招标', 'HigherGov：Delivery Order 47QTCA22D00B3-W912LA25FA053 worth up to $29,270 awarded to 52 Networks on 2025-09-24 by California National Guard（MAS；Small Business Total set aside；NAICS 334111；PSC 7125；3 bids received）', 'https://www.highergov.com/contract/47QTCA22D00B3-W912LA25FA053/', '2025-09 仍在拿政府小单 → 公司活着、还在投标；我们的产品进其政府单要看产地要求，先做商业单'),
    ('SB-970', '领英公司页', 'ZoomInfo：EION · Canada · Computer Equipment & Peripherals / Manufacturing / Telecommunications · 51–200 Employees · Revenue $21.8M · founded 2001 · Kalai Kalaichelvan President；highperformr：555 Legget Drive, Suite 720, Ottawa · Total employees 58', 'https://www.zoominfo.com/c/eion-inc/12567474', ''),
    ('SB-970', 'KP', 'highperformr（2025-04 领导层）：Dr. Kalai S. Kalaichelvan — President & CEO；Saf Assadi — Founder & CTO（我方 KP）；Sumit Kumar — VP Engineering；Manny Mistry — VP Sales & Business Development', 'https://www.highperformr.ai/company/eion', '无线宽带设备制造商（企业/农村宽带/公共安全/智慧城市/工业 IoT）→ 配套工业 PoE 交换机 OEM；CTO Assadi 是产品决策人'),
    ('SB-1026', '领英公司页', 'LeadIQ（2026-06）：Epygi Technologies LLC ≈26 employees across Europe & North America；HQ Altamonte Springs, Florida（销售/市场/制造）；R&D 在 Yerevan, Armenia；2000 年成立的 IP PBX / 网关 / ecQX 云服务厂商，40 国有销售支持；theorg：CEO Mario Cuello（我方 KP），SW director Levon Harutyunyan', 'https://leadiq.com/c/epygi-technologies-llc/5a1d89ff24000024006359d3', '总部已从 Plano TX 迁至佛州（研究档地址需更新）；PBX 厂商配套 PoE 交换机 = 典型 OEM 捆绑'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
