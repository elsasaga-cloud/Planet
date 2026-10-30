#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-14（T29-U143 2026-10-30）· 南亚 8 户：MT-Link / DevRay / Apollo Infoways（WatchDog）/ Litech / Microtech / Futurist / San Telequip / Telexcell。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-14'
ITEMS = [
    ('SA-039', '人事变动', 'Indeed Pakistan（2026-02）：MT-LINK TECHNOLOGIES CO.（Karachi）在招 Channel Sales Executive（「Develop and manage channel partnerships with ISPs and ICT vendors · Drive B2B sales」）、Network Technician（pre-sales & post-sales technical support for our networking products）、Digital Marketing & Graphic Designer（Meta/Google Ads）', 'https://pk.indeed.com/q-mt-jobs.html', '2026 年在扩渠道销售 + 技术支持 → 自牌网络产品线在起量；ISP 渠道是其目标'),
    ('SB-1138', '登记', 'Scribd（MCA 摘录）：DEVRAY IT SOLUTIONS PRIVATE LIMITED · CIN U62013UP2024PTC204532 · incorporated 2024-06-13（Kanpur）· authorized & paid-up capital Rs 1,00,000 · Directors Yogendra Kumar Rajput, Neha Jain；官网：Noida Sector 63 办公，产品 DevGate NGFW / Router / SD-WAN / Industrial Switches / Data Center Switches；关联 Maplecloud Technologies（Greater Noida，Yogendra Rajput Managing Partner，IndiaMART 在售「DevRay Network Switches · Made in India」）', 'https://www.devray.in/', '2024-06 新注册、实缴 1 万卢比的贴牌品牌 → A-DEEP-06 下放 B（B1 观察：ODM 需求真实但主体太新太小）'),
    ('SB-641', '领英公司页', 'Datanyze / ZoomInfo / IndiaMART：Apollo Infoways Pvt. Ltd. · G-149, G-Block, Sector 63, Noida · Founded 2009 · 28 employees（IndiaMART 26–50）· Revenue $6M（IndiaMART 年营业额 ₹5–25 Cr）· Founder & CEO Ravi Prakash · 自称「biggest Manufacturer of CCTV Camera, Security Alarm System」+ routers / switches / wireless APs（WatchDog 品牌 = mywatchdog.in，SC-1371 同一公司）', 'https://www.datanyze.com/companies/apollo-infoways-pvt/425988672', 'WatchDog 品牌主体；SC-1371 作为同一公司的副档降 B（A-DEEP-06），跟进只走 SB-641'),
    ('SB-1116', '领英公司页', 'ZoomInfo / D&B / RocketReach：LITECH PAKISTAN (PRIVATE) LIMITED · Layallpur Regency Plaza, 949-Mall Road, New Civil Lines, Faisalabad · 501–1,000 employees（ZoomInfo）· Key Principal / Director Operations Bilal Asad（Lahore）· 办公点 Lahore / Islamabad / Doha', 'https://www.zoominfo.com/c/litech-pakistan/557123995', '华为渠道的电信基建承包商（OSP），人数量级 500+（现场施工队）'),
    ('SB-1116', '人事变动', 'ZoomInfo「recently hired」：Muhammad Azam — General Manager Technical（Joined 2025-02-18）；Hassan Cheema — Manager Business Development / Project Manager OSP（Joined 2025-01-31）', 'https://www.zoominfo.com/c/litech-pakistan/557123995', '2025 新技术总经理 = 设备选型新对口'),
    ('SC-2513', '供应商/品牌关系', 'microtech.net.pk：Microtech Inc（est. 1997）· Suite 503, Progressive Plaza, Beaumont Road, Civil Lines, Karachi · 「Pakistan’s authorized distributor for Ubiquiti, MikroTik, Huawei eKit」+ V-SOL, Ruijie, ZKTeco, IMOU · 「transformed ourselves from System Integrators to Distributors」· 分支 Karachi / Lahore / Islamabad · 博客 2026-04 仍更新', 'https://microtech.net.pk/contact/', '巴基斯坦全国性网络分销商（MikroTik/Ubiquiti 渠道）→ 交换机白牌线对位，分销 20% 档'),
    ('SB-869', '供应商/品牌关系', 'Tendata（2025-09-15 核验）：FUTURIST PVT. LTD.（Islamabad，House No. 524, Double Road, I-10/4）「importing … from 11 suppliers across China」；Jamals：电信线缆/光纤/测试仪/UPS/太阳能/CCTV/网络 + 电信规划承包', 'https://www.tendata.com/en/supplier/futurist-pvt-ltd-PAKI21deee967283195299660619e5e4c79f.html', '有中国进口记录（11 家供应商）= 「有进口经验者」；伊斯兰堡电信工程 + 贸易'),
    ('SC-1657', '领英公司页', 'LinkedIn / ZoomInfo：San Telequip Pvt. Ltd. · Pune（Baner Road，Deron Heights 504/505）· Founded 1991 · 11–50 employees · Revenue $7.5M · ISO 9001:2015 · 25,000+ installations；自研接口转换器 / 工业终端服务器 / 协议网关 / 无线转换器 + Networking & Surveillance Solutions；近期帖：IOCL Kandla–Gorakhpur ~3,000 km LPG 管线项目', 'https://www.linkedin.com/company/san-telequip-p-ltd.-', '浦那工业数据通信 OEM（三十年），油气/电力/楼宇渠道 → 工业交换机 OEM 配套位'),
    ('SC-1771', '领英公司页', 'Glassdoor / IndiaMART：Telexcell Information Systems（Telexcell Information System Ltd.，GST 07AAACT2423K1ZH）· New Delhi（Modi Tower, Nehru Place）· founded 1987（Glassdoor 写 1993）· 26–50（IndiaMART）/ 51–200（Glassdoor）· 网络与安防基础设施系统集成（高校项目如 Central University of Haryana）；Glassdoor 评论提到发薪不及时', 'https://www.glassdoor.co.in/Overview/Working-at-Telexcell-Information-Systems-EI_IE532780.11,40.htm', '德里中型 SI；现金流评价一般 → 前 T/T'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
