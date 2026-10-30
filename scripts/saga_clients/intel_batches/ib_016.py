#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-16（T29-U143 2026-10-30）· 亚太 9 户：EZ-NET（NEXTU）/ GTWave（未得）/ Impulse / Resonant（PI）/ Xspec（PI）/ PBA（PI）/ WizardsInc（PI）/ Widen / Trường Sơn。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-16'
ITEMS = [
    ('SA-010', '年报/财务', 'Incruit / Saramin / JobKorea：㈜이지넷유비쿼터스（EZ-NET Ubiquitous）· 서울 용산구 새창로45길 78 진성빌딩 · 설립 2004（법인 2006-04）· 대표 김우경 · 사원수 35–44 · 자본금 5,000만원 · 매출액 2023 292억 → 2024 251.6억 → 2025 254.1억 원 · 순이익 2023 49.4억 → 2024 30.3억 → 2025 13.3억 · 자본총계 230.2억（2025）· 고용노동부 강소기업', 'https://www.incruit.com/company/1687650747', '采购线索：年销 ≈$18M 的自牌（NEXT/NEXTU，~1,000 SKU）网络/周边品牌商，利润连续两年下滑 → 在找更便宜的 ODM 货源是合理推断；OEM 30% 档'),
    ('SA-010', 'KP', 'JobKorea：대표자 김우경（Kim Woo-kyung）；주요사업 네트워크 및 컨트롤러 제품 제조·유통；「기업 및 관공서에는 고성능 전문 네트워크 장비를 공급」', 'https://www.jobkorea.co.kr/recruit/co_read/c/jjwpac22', ''),
    ('SA-029', '登记', '未得：网查「지티웨이브 GTWAVE」命中 티웨이브（핀테크）/ 지웨이브（화훼）等无关公司；研究档已有 매거진한경 2 年保固报道，本轮未增', '', '1 查未得即停'),
    ('SA-014', '领英公司页', 'ZoomInfo：Impulse Networks · HQ Vancouver, British Columbia · impulsecctv.com · 51–200 · $5.4M；RocketReach：Impulse CCTV · 4 employees · Gaurav Sharma — Business Development Manager（New Delhi）、Abhinav Garg — Product Specialist（Delhi）', 'https://rocketreach.co/impulse-cctv-profile_b77f830fc533f0c2', '新加坡/温哥华/德里三地叙事、可见团队 4 人（德里）→ 主体与规模不清 → A-DEEP-08 下放 B'),
    ('SB-001', '登记', 'globaldatabase / sgpgrid / SignalHire：RESONANT NETWORKS PTE. LTD. · UEN 201316122M · 2013-06-14 起 · 81 Ubi Avenue 4 #09-28 UB. One, Singapore 408830 · +65 6871 4128 · 11–50 人 · Optical Fibre, DWDM, Cloud Interconnect, Data Centre Network · 运营 Singapore + Malaysia · 关联 APEIRO NETWORKS PTE. LTD.', 'https://sgpgrid.com/company/resonant-networks-pte-ltd-ID0000', 'PI 成单户：新加坡 DC/光网络集成商（马来西亚有团队）'),
    ('SB-001', 'KP', 'globaldatabase / sgpgrid：Hong Zhiwei — AVP Sales；Richard Lapitan — Team Lead OTN & DWDM Implementation；Hafiz Mohd Rizal — Solution Architect & Presales；Ts Mohd Idhamm Ibrahim — Country Manager（MY）；Jerlyn Chia — Finance Manager；Nick Su — Senior Optical Network Engineer', 'https://sg.globaldatabase.com/company/resonant-networks-pte-ltd', 'AVP Sales 与预售架构师是复购对口'),
    ('SB-002', '展会/活动', 'MINDTCE：XSPEC TECHNOLOGY SDN BHD 为第 8 届 Malaysia International NDT Conference & Exhibition（2026-11-17～18）参展商；Contact Sugito Wibawa · sugito@xspec.com.my · +60 12 988 8086；JobStreet：11–50 人，Manufacturing Representatives，MY / ID / SG 三地；地址 No.8, Jalan Industri USJ1/8, Subang Jaya', 'https://mindtce.com.my/companyprofile/B2611000001', 'PI 成单户：NDT/安防制造商代表（含「Uniformed Bodies」客群 → 守界只谈民用）；每年 11 月 MINDTCE'),
    ('SA-080', '登记', 'dataforthai：บริษัท พีบีเอ ฟอร์เอฟเวอร์ เทคโนโลยี จำกัด（PBA FOREVER TECHNOLOGY CO., LTD.）· ทะเบียน 0115558019700 · จดทะเบียน 2015-10-01 · ทุน 5,000,000 บาท · 334 หมู่บ้านกราฟฟิคเพลส ซอย 2 ถ.เทพารักษ์ ต.บางเสาธง สมุทรปราการ 10570 · ธุรกิจ จำหน่ายและติดตั้งกล้องวงจรปิด CCTV + อุปกรณ์เครือข่าย / ไฟเบอร์ออฟติก；网店 pbacctv.com / pbashop.in.th（PBA Supply）', 'https://www.dataforthai.com/company/0115558019700/', 'PI 成单户：曼谷东郊 CCTV + 网络安装/零售商，注册资本 500 万泰铢'),
    ('SA-090', '登记', 'Experian MY / CreditScan：WIZARDSINC SDN. BHD. · 201101002484 (930621-U) · incorporated 2011-01-24 · Wilayah Persekutuan · ICT solution & software/hardware, embedded system & security & communication systems, access control & CCTV；官网：Lot 1-2A Incubator 1, Technology Park Malaysia, Bukit Jalil, KL · +603 4044 4044 · info@wizardsinc.co', 'https://buy.experian.com.my/index.php/search/Malaysia-Company/930621/WIZARDSINC-SDN.-BHD.', 'PI 成单户：吉隆坡科技园 ICT/安防集成商（2011 年）'),
    ('SA-012', '供应商/品牌关系', 'widen.co.th：บริษัท ไวเด้น เทรดดิ้ง จำกัด（Widen Trading Co., Ltd.）· 99/223 หมู่ 5 ต.ไทรม้า อ.เมืองนนทบุรี · 02-149-3922 · thawat@widen.co.th · LINE @widencompany · 光纤产品进口分销（Patch Cord, Closure, Media Converter, Video Converter, Rack Mount）· 分支 Chiang Mai / Khon Kaen · ISO 9001:2015 · 招经销商（「ครอบครัวไวเด้น」）· 网店 shop-widen.com', 'http://www.widen.co.th/index.php?content=about', '泰国光纤分销商（三地分支 + 经销网络）；KP Thawat'),
    ('SA-031', '供应商/品牌关系', 'switchcongnghiep.com（「Switch công nghiệp ONV Việt Nam」）：由 Truong Son Solutions Co., Ltd.（CÔNG TY TNHH GIẢI PHÁP VÀ XÂY LẮP TRƯỜNG SƠN）分销 PLANET、Advantech、ONV 工业交换机 + HDLink 摄像机 · 总部 Phòng 702A, Centre Point, 106 Nguyễn Văn Trỗi, Phú Nhuận, TPHCM · 营业办 214/11 Nguyễn Oanh, Gò Vấp · Hotline 0916 799 345 · info@truongsonsolutions.com', 'https://switchcongnghiep.com/san-pham/switch-cong-nghiep-planet-igt-905a/', '胡志明市工业交换机垂直分销（在卖 PLANET/Advantech/ONV = 同品类进口老手）→ 白牌换源对位'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, bool(url))
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
