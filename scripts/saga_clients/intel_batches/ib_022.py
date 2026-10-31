#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-22（T29-U148 2026-10-31）· B1 挖底第一批：土耳其 4 + 北美 10。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-31'
B = 'INTEL-22'
ITEMS = [
    ('SB-105', '领英公司页', 'LinkedIn / Datanyze：CENOVA BİLİŞİM TEKNOLOJİLERİ İTH. İHR. ve TİC. LTD. ŞTİ.（Cenova Güvenlik）· Perpa Ticaret Merkezi B Blok Kat 8 No 902, Okmeydanı, İstanbul · 2002/2004 年起 · 11–50（16–18 人）· 「yurtdışındaki üreticiler ile distribütörlük temsilcilik anlaşmaları」· 在售 Tiandy 热成像/PTZ、Dayzip AHD；员工：Rıdvan Baydemir（销售）、Abdurrahman Erkarslan（技术主管）、Ramazan Pişkin（仓库）', 'https://tr.linkedin.com/company/cenova-bili%C5%9Fim', 'Perpa 安防进口分销商（Tiandy 等），16–18 人'),
    ('SB-283', '领英公司页', 'LinkedIn / SignalHire / X：Öncü Güvenlik Sistemleri A.Ş. · Kavacık, İstanbul（Yaya Beyi Sokak）· 2002 年 · 51–200（100–200）· 「elektronik güvenlik sistemlerinde uluslararası markaların … ulaştırılması」· Hikvision 土耳其分销（2024-04 Hikvision MEA 毛里求斯分销商大会获奖）· 自牌 Sec-on · 集团人物 Osman Çalışkan（Öncü Group / MÜSİAD 副主席）；销售 Hakan Kırmızıgül、Çağla Battal、Banu；技术服务经理 Ali Rifat Türk', 'https://tr.linkedin.com/company/oncuguvenliksistemleri', '土耳其头部安防分销商（Hikvision 获奖 + 自牌 Sec-on）→ 回信即 A 候选；B1 第一轮重点'),
    ('SB-489', '供应商/品牌关系', 'portel.com.tr：PORTEL TEKNOLOJİ SAN. VE TİC. A.Ş. · Yalı Mah. Kadir Sk. No:14 Helis More Residence Kat:7 D:82, Kartal / İstanbul · +90 216 464 44 50 · bilgi@industrialnetworkcenter.com ·「her türlü endüstriyel network ürünleri ve yarı iletken ürünlerin temini」；Eurotech 官网列其为土耳其分销商', 'https://www.portel.com.tr/', '工业网络 + 半导体分销（Eurotech 渠道；研究档记现三旺）→ 工业交换机换源对位'),
    ('SB-475', '供应商/品牌关系', 'LinkedIn / SignalHire / Yenibiriş：CCTV Depo Güvenlik Teknolojileri A.Ş. · Hürriyet Mh. Güngören Sk. 4B Bahçelievler, İstanbul（+ Perpa B Blok K:8 No:836）· 2004 年 · 51–200（100–200）· 「Güvenlik sektörünün ilk B2B sitesi」· 自牌 SECUZI 的制造/进口商，2022 年起进军美国等海外市场 · 0850 303 03 17', 'https://www.yenibiris.com/firma/cctvdepo-guvenlik-teknolojileri-a-s/286309', 'B2B 安防电商 + 自牌 SECUZI（出口美国）→ OEM 30% 档，回信即 A 候选'),
    ('SA-044', 'KP', 'dymec.com：DYMEC · 2243 N. Mason Rd, Suite 402, Katy, Texas 77449 · (816) 988-7861 · sales@dymec.com ·「Proudly Owned and Operated by Veterans」· 产品：DIN-Rail & Rack L2/L3 工业交换机、EN50155 / IEC61850-3 系列、SFP、TraffiClair AI 交通检测 · Tom West — Design & Engineering（twest@dymec.com）· Ray Renaud — VP Sales & Marketing（rrenaud@dymec.com）', 'https://www.dymec.com/get-quote/', '美国加固工业交换机品牌（白牌贴标；与 BlueWARRIOR SA-033 同体系）；EN50155 线守界只谈 ITS/电力'),
    ('SB-221', '领英公司页', 'ZoomInfo / Datanyze / Tracxn：Tycon Systems · 14641 S 800 W Ste A, Bluffdale, Utah 84065 · Founded 2008 · 15–18 employees · Revenue $5.9M · 离网供电（太阳能/风能）+ PoE 转换器 + 无线桥接 · 融资 $150K', 'https://www.zoominfo.com/c/tycon-systems-inc/346482214', '自牌 TP- 系列 PoE/供电产品商（15–18 人、$5.9M）→ PoE 交换机 OEM 对位'),
    ('SB-780', '领英公司页', 'ZoomInfo / Datanyze / Manta：Signamax, Inc. · 999 NW 159th Dr, Miami, FL 33169 · Founded 1983 · 51–200（Datanyze 71 / Manta 29）· Revenue $9.8M · CEO Indika Kulatunga（Manta：President Vyacheslav Stein）· 产品线 media converters, Ethernet switches, copper & fiber cabling · 面向中小安防集成商 / AV 集成商 / 布线承包商，有分销与安装商计划', 'https://www.datanyze.com/companies/signamax/158368051', '迈阿密连接产品品牌（交换机/MC 全系贴牌，$10M 级）→ OEM 30% 重点'),
    ('SB-775', '领英公司页', 'SignalHire / ZoomInfo：Patton, LLC（Patton Electronics Co.）· 7622 Rickenbacker Dr., Gaithersburg, MD 20882 · 1984 年 · 100–200 employees · Revenue ≈$29.9M · VoIP 网关 / SBC / 路由器 / 数据通信 · 含 Artel Video Products 事业部', 'https://www.signalhire.com/companies/patton-electronics-co', '美国电信设备厂商（$30M、100–200 人）：自有 CopperLink/工业交换机线 → 可能的 OEM 外采方；回过信'),
    ('SB-951', '领英公司页', 'ZoomInfo / explorium / seamless：Montavue（LLC）· Missoula/Bozeman, Montana · Founded 2015 · 11–50（11 可见）· Revenue $1–5M（ZoomInfo $5.1M）· CEO & Founder Cody Gordon · DTC 安防摄像品牌；Wholesale Account Manager Jack Burns、Sales Manager Russ Simmons', 'https://www.zoominfo.com/c/montavue-llc/443156558', '美国 DTC 安防品牌（自标 PoE 交换机配套）11 人 → OEM 小量'),
    ('SB-761', '领英公司页', 'Inc. / LeadIQ / Glassdoor：SCW（Security Camera Warehouse）· Asheville, NC · founded 2009/2010 · CEO Matthew Nederlanden · 51–200（LeadIQ 129）· revenue $10M–25M · 专业监控设备 + 自有标 PoE', 'https://leadiq.com/c/scw---security-technology/5a1da2162300005a0093b796', '美国商用安防品牌（$10–25M、100+ 人）→ OEM 30% 重点'),
    ('SB-913', '登记', 'ZoomInfo / Manta：LanPro Networks Inc（Lanpro of Miami）· Doral, FL · 1996 / 2012 · 1–10 employees（5–9）· Revenue <$5M（$1–2.5M）· CFO Kathryn Jechura · 网络组件品牌（拉美导向）', 'https://www.zoominfo.com/c/lanpro-networks-inc/354457623', '实为 5–9 人小品牌（研究档「量大」不成立）→ B-PASS-02 调 B2'),
    ('SB-712', '领英公司页', 'RocketReach / LeadIQ：Maple Systems, Inc. · 808 134th St. SW Suite 120, Everett, WA 98204 · Founded 1983 · 44–60 employees · Revenue $7.4M（LeadIQ 估 $50–100M 不采）· CEO Larry St. Peter · HMI / HMI+PLC / 工业面板 PC 品牌，兼容 AB/Schneider/Siemens', 'https://rocketreach.co/maple-systems-inc-profile_b5e2be5ff42e6351', '工业自动化 HMI 品牌商（60 人）→ 配套工业交换机 OEM 口'),
    ('SB-741', '登记', 'ZoomInfo / Tracxn / Lightwave：Canary Communications Inc · 6040 Hellyer Ave Ste 150, San Jose（Tracxn：Morgan Hill）· 1987 年 · 1–10（Tracxn 2026-07：4 人）· 数据二极管 / 以太网与串口转换器 / CWDM-DWDM · 市场含 government, military · Director Sales Jim McSeaton', 'https://tracxn.com/d/companies/canary-communications/__TXVOO8fAzG3QoM4xiGXji5R7NciR4SM0RtwlrZSTK4U', '4 人 + 政府/军方市场 → B-PASS-02 调 B2'),
    ('SB-673', '供应商/品牌关系', 'nodactechnology.com：Nodac Technology · 2236 NW 82 Av, Miami FL 33122 + 1301 W Copans Rd Pompano Beach + Hong Kong · since 2001 · 分销 Hikvision, ZKTeco, Ruijie, TP-Link, Wi-Tek, Dahua, Uniview, TVT, Alula · 覆盖 USA / Caribbean / Central America · **自牌 Lysora**（新品 LS2P-16MG4XS-HP 16 口 2.5G L2+ 管理 PoE）· WhatsApp +1 786 377 4190', 'https://nodactechnology.com/', '已在用自牌 Lysora 卖 2.5G PoE 交换机 = 现成 ODM 买家 → 回信即 A 候选；香港办公室可面谈'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
