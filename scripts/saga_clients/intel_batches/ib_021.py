#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-21（T29-U144 2026-10-30）· 第一遍收口：剩余 34 户（中东 3 / 亚太 13 / 俄语区 2 / 北美 1 / 拉美 5 / 欧洲 6 / 非洲 4）。来源 web_search 结果页，引文原样；查无者记「未得」。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-21'
ITEMS = [
    # 中东
    ('SB-053', '领英公司页', 'LinkedIn：Onnet Technologies & Innovations LLC（OTAI）· Ajman Industrial Area-1（Shed #1, Street 80-81 Junction）· 11–50 · 成立 2012 ·「the only #TDRA approved Telecom Products / Solution manufacturer based in UAE」· 产品：Carrier-Grade Wireless、High Power Industrial PoE Switch、PoE Extenders、Outdoor Communication UPS、Solar Communication Systems、CCTV/Smart Poles；联系人 Piyush Shah（piyush@onnettechnologies.com）', 'https://ae.linkedin.com/company/otaillc', '阿治曼本地「制造商」（实为自牌集成），TDRA 认证 → 高功率 PoE 交换机 OEM 口；KP Piyush Shah'),
    ('SB-175', '领英公司页', 'SignalHire / RocketReach / AeroLeads：M. Al Barghash Trading & Contracting（MBTC）· Al-Khobar（4th St corner Kharj St, Thuqbah-2）· Energy / Saudi Aramco approved contractor · 1,000–5,000 employees（AeroLeads 70）· revenue ≈$414.6M · Head of IT Hariprasath Ramu · Procurement Engineer Venkatesh Raja · 项目工程师多人（Buqayq 等）', 'https://www.signalhire.com/companies/m-al-barghash-company', '阿美认证的大型 EPC 承包商 = 项目型终端，设备需走阿美供应商名录 → A-DEEP-11 下放 B（B1 观察）'),
    ('SB-451', '领英公司页', 'LinkedIn / RocketReach：(e-Saudi) Electronic Saudi Network · Riyadh（P.O. Box 61461，+966 1 4650832）· Founded 2001 · 11–14 employees · revenue ≈$1.4M · Remote Automation, Control and Communication + fixed broadband · Sales Managers Muhammad Rashid、Varughese Mathew；Operation Manager Saeed Mohammed', 'https://www.linkedin.com/company/-e-saudi-electronic-saudi-network', '14 人、年销 ≈$1.4M 的小型 SI/贸易 → A-DEEP-11 下放 B'),
    # 亚太
    ('SA-028', '供应商/品牌关系', 'entasource.co.th：ENTA SOURCE Co., Ltd.（曼谷）进口分销 SFP 1G/10G/25G/40G/100G（兼容 Cisco/Juniper/Aruba/Huawei，3 年保）、Media Converter、Rack/DIN-Rail Industrial Ethernet Switch、Industrial PoE Switch、HDMI/4K over Fiber、光纤配件；售后保 1–3 年', 'https://www.entasource.co.th/17430328/network', '曼谷自标进口分销商（光模块 + 工业交换机）→ 换源对位'),
    ('SA-029', '登记', '未得（第二次）：网查「지티웨이브 GTWAVE」仍只命中无关同名公司；研究档已有 매거진한경 报道', '', '两查未得即停；韩国品牌商身份以研究档为准'),
    ('SB-047', '登记', 'whois.ipip.net / Facebook：Topica LLC · Ulaanbaatar（Chingeltei district, 3a building；P.O.Box 44/575）· AS10109 TOPNET-AS-MN-AP「Internet Service Provider」· Facebook「Topica」18,163 likes：Мэдээллийн технологи, автоматжуулалтын шилдэг шийдэл, тоног төхөөрөмжийн худалдаа, үйлчилгээ（IT/自动化设备销售与服务）+「Topica.mn Network Shop」', 'https://whois.ipip.net/AS10109', '乌兰巴托 ISP（自有 AS）兼网络设备商店 → 接入/汇聚交换机真实买家'),
    ('SB-059', '登记', 'ZoomInfo / EMIS / Kompass：Avanca Technologies Pte Ltd · 23 New Industrial Road #07-06/07 Solstice Business Center, Singapore 536209 · incorporated 2002-09-06 · 1–10 employees · regional distributor：Serial Server、Industrial Switches、4G/5G industrial routers、Audio/IO over IP · Sales Manager Benny Chee Fu', 'https://www.zoominfo.com/c/avanca-technologies-pte-ltd/480924629', '1–10 人工业网络分销 → A-DEEP-11 下放 B'),
    ('SB-071', '领英公司页', 'aihitdata / ZoomInfo / JobStreet：Nayon Kontrol Systems（NKS）· No. 4 Illinois St., Brgy. Silangan, Cubao, Quezon City · established 1996 · 11–50 · est. revenue $14.8M · SCADA & automation SI for electric utilities（first real SCADA in electric cooperatives）+ oil/gas/water/railway/BMS · 关联 NKS Energy Utilities, NKS Solar One, NKS Biomass One', 'https://www.aihitdata.com/company/01B1B037/nayon-kontrol-systems/overview', '菲律宾电力 SCADA 集成商（≈$15M）→ 变电站工业交换机对位（railway 部分守界）'),
    ('SB-1102', '登记', 'infocom.vn：CÔNG TY TNHH VIỄN THÔNG GIÁ TỐT（GOOD PRICE TELECOMMUNICATIONS COMPANY LIMITED）· MST 0109246393 · 成立 2020-07-01 · 代表 Nguyễn Văn Đông · Đông Anh, Hà Nội · 批发电子/电信设备；官网：网络设备 + 摄像头 + 光纤熔接施工（Hotline 0963.508.809）', 'https://infocom.vn/cong-ty-tnhh-vien-thong-gia-tot.html', '2020 年成立的「低价」小型网络经销/施工商 → A-DEEP-11 下放 B'),
    ('SB-164', '登记', 'unea-x.com 会社概要：UNEAX株式会社（UNEAX Co., Ltd.）· 設立 2022-09-28 · 代表者 大迫 麗莉 · 本社 神奈川県大和市中央林間五丁目5番；東京支社 港区虎ノ門4-3-1 21F · TEL 0462-11-8013 · 事業：SSD 販売（パートナー ScaleFlux）、産業用イーサネットスイッチの開発と販売、IoT センサー、金型部品加工；iPROS 2023-08：産業用イーサネットスイッチ 12 種類をリリース', 'https://unea-x.com/company/', '2022 年新公司但已有 12 款自牌工业交换机 → ODM 换源对位（日本非主攻，留 A 观察）'),
    ('SB-226', '年报/财务', '官网 / JobKorea / Saramin：(주)한창인포텍 · 서울 용산구 청파로 40 삼구빌딩 1610호 · 사업자등록번호 106-86-81310 · 설립 2011-09-06 · 대표 배성훈 · 직원 4–10 명 · 매출 18–40억 원 · Sony 디지털카메라 총판 + 2020 년부터 자체 브랜드 RFOINT 네트워크 장비/컨버터/케이블 수입 유통 · jryoun74@hcin4.com', 'https://www.jobkorea.co.kr/recruit/co_read/c/hcinfo117', '4–10 人、自牌 RFOINT 进口商 → A-DEEP-11 下放 B（俄/韩二级 + 微型）'),
    ('SB-267', '登记', 'corpiness / mfgpages / yellowpages.net：Bio-Cognitive Solutions Pte Ltd · 4008 Ang Mo Kio Avenue 10 #02-04 Techplace I, Singapore 569625 · +65 6553 2128 · biometric access / CCTV / alarm / autogate / carpark barrier 供应与安装（网页产品停留在 2012 年款）', 'https://www.corpiness.com/bio-cognitive-solutions-pte-ltd/contact.htm', '新加坡小型安防安装商、网页陈旧 → A-DEEP-11 下放 B'),
    ('SB-315', '供应商/品牌关系', 'stcvietnam.biz：Công ty TNHH TM DV Song Thành Công（STC Vietnam）「là nhà phân phối chính thức thiết bị hãng MOXA Inc tại thị trường Việt Nam」· 工业自动化备件/设备分销：Industrial Ethernet Switch、Serial Device Server、Industrial Router、Media Converter、NSD 编码器、Balluff 传感器、E2S、Enerdoor', 'https://stcvietnam.biz/', '越南 Moxa 官方分销 + 工业自动化渠道 → 工业交换机白牌补位（Moxa 价差大）'),
    ('SB-367', '登记', 'thuyluc.com：Công ty Cổ Phần MTS（MTS Hydraulics & Automation）· Số 166 Đường Tựu Liệt, Tam Hiệp, Thanh Trì, Hà Nội · GPKD 0101892941（2006-03-14）· 水电项目液压/阀门/SCADA 电柜供应（源自某总公司高科技中心私有化，Dr. Ly Thanh Ha 主要股东；该总公司 20 家成员企业约 1 万人）', 'https://www.thuyluc.com/gioi-thieu', '水电 EPC 配套（液压为主，SCADA 电柜顺带）= 项目型终端 → A-DEEP-11 下放 B'),
    ('SB-485', '年报/财务', 'JobKorea / Incruit / lab.incruit：엔아이투스㈜（N-ITUS Co., Ltd.）· 경기 군포시 엘에스로 153-8 4층 · 설립 2007-09-03 · 대표 장세봉 · 유선 통신장비 제조업 · 사원수 40–43 명 · 자본금 6억 1,582만원 · 매출 2022 348.8억 → 2023 310억 → 2024 200억（순손실 −21.1억）→ 2025 240.4억 원（순이익 3.3억）', 'https://www.jobkorea.co.kr/Recruit/Co_Read/C/nitus/Company_name/%EC%97%94%EC%95%84%EC%9D%B4%ED%88%AC%EC%8A%A4%E3%88%9C', '韩国有线通信设备制造商（40 人、≈$17M），2024 亏损后 2025 回升 → 外采降本期，OEM 对位'),
    ('SB-982', '登记', 'mcss.co.kr / JobKorea / sharedit：㈜엠씨에스솔루션（MCSS）· 서울 금천구 디지털로 178 A동 1009호 · 사업자 106-86-25768 · 설립 2004-01-30 · 대표 이일우 · 사원수 9–10 명 · 매출 45억 원 · PLANET / Ubiquiti（공식 총판）/ Omnitron / Teltonika 유통 + NI/SI · 영업대표 함종섭', 'https://www.mcss.co.kr/', 'PLANET/UniFi 渠道但 9–10 人 → A-DEEP-11 下放 B（韩国 B1 重点）'),
    # 俄语区
    ('SA-066', '登记', '未得（第二次）：「ccs-msk.ru」仍只命中同名「МСК」等无关公司；需 whois/官网 реквизиты', '', '两查未得即停；研究档（Microsens/Lenovo 合作伙伴）为准'),
    ('SC-1942', '供应商/品牌关系', 'shop.satvision-cctv.ru：Satvision —「одна из крупнейших компаний в области производства и поставок оборудования для систем безопасности и видеонаблюдения в России」· Самара, ул. Санфировой 95, к.1 · 品牌：Satvision、SatvisionSP（项目线）、Divisat（数字/卫星接收机）、Satvision Smart Systems（VMS）；fastvideo.ru 将其列为俄罗斯本土摄像机厂商', 'https://shop.satvision-cctv.ru/company/brands/', '萨马拉 CCTV 大牌（OEM 采购方）→ PoE 交换机贴 Satvision 的 30% 档'),
    # 北美
    ('SA-078', '登记', 'Alignable / Infobel / controlready.ca：James Clendenan Systems Ltd. · launched 2012-09 · North Vancouver（1528 Bowser Ave V7P 2Y3；Control Ready：1127 15th Street West）· Owner James Clendenan（Computer Engineer；ex Pixar Canada、Sophos、HootSuite、Olympic Broadcasting Service）· 服务：managed networks（$15/device/month）、ISP/SMB 网络设计、Wi-Fi、Fixed Wireless、Fiber；品牌 Control Ready（SCOUT 移动办公箱、BARK 移动报警、POST 数字标牌）', 'https://www.controlready.ca/about', 'PI 成单户（活跃）：一人工程公司 + 自牌移动设备 → 复购在其项目节奏'),
    # 拉美
    ('SA-061', '登记', 'contrataciones.gov.py：RYMTECH E.A.S. · RUC 80125463-9 · Nombre de Fantasía RYMTECH TACTICAL CYBEROPS（Nancy Carolina Elizalde de Osorio, Ruslan Osorio Guerra）· Empresa de Acciones Simplificada · Tamaño Micro · inscripción 2022-06-16 · Hernandarias, Alto Paraná · 服务：SOCaaS、渗透测试、DFIR、Hardware as a Service；官网：「No comercializamos tecnología」', 'https://www.contrataciones.gov.py/proveedor/rymtech-e-a-s.html', '微型网络安全服务商（官方登记 Micro）、自述不卖硬件 → A-DEEP-11 下放 B'),
    ('SA-071', '登记', 'Facebook / boliviayp：Sur-Link Technology Bolivia · Av. Guapay #2675 esq. Calle 10, Santa Cruz de la Sierra · +591 3 3477677 / 74927328 · Emiranda@surlink-tech.com ·「Distribuidor mayorista de tecnología: Cat6a cat6 cat5e, fibra óptica SM/MM, ferretería ADSS, racks」· 覆盖 La Paz / Cochabamba / Santa Cruz 等 9 省', 'https://www.boliviayp.com/company/64839/SUR_LINK_TECHNOLOGY_BOLIVIA', '圣克鲁斯布线/光纤批发分销（全国覆盖）；KP E. Miranda'),
    ('SB-031', '登记', 'universidadperu / LinkedIn / PAR：OM TELECOM S.R.L. · RUC 20600792858 · inicio 2015-11-02 · Santiago de Surco, Lima（Av. Ramón Castilla 1120 Int. 503A）· 2–10 empleados · 能源/矿业/变电站自动化电信方案（光纤、载波、IP 电话、CCTV、SDH/PDH）· 国家供应商登记 · 运营区域 CO/EC/PE/BO/CL/AR/PY/BR', 'https://pe.linkedin.com/company/omtelecomperu', '2–10 人项目型 → A-DEEP-11 下放 B'),
    ('SB-1134', '供应商/品牌关系', 'conexionderedes.com：Conexión de Redes（San Salvador；+503 2262-1049；WhatsApp +503 7553-2289；gerencia@conexionderedes.com）· 服务：Redes XGPON/FTTx、Fibra Óptica FTTH、POLAN 智能楼宇、IPTV、Data Center、LTE、微波 IP、PoE 照明咨询 · 网店含 switches/routers/FTTH/XGPON', 'https://www.conexionderedes.com/servicios', '中美洲电信设备供应 + 集成（网店 + 咨询）；规模未见'),
    ('SB-1137', '登记', '未得：Infotec Comércio de Equipamentos e Sistemas（巴西，无域名）网查无法锁定主体', '', '不可核 → A-DEEP-11 下放 B'),
    # 欧洲
    ('SA-070', '登记', '未得（第二次）：Top Italia S.r.l.（Misterbianco/Catania，topsicurezza.com）网查仍只见同名 Top Security；需官网 P.IVA 核', '', '两查未得即停；研究档为准'),
    ('SB-056', '登记', '未得：「Net Work Business Solutions nbs.ee」网查无命中（结果为美国 NBS / 其他爱沙尼亚 IT 公司）', '', '不可核 → A-DEEP-11 下放 B'),
    ('SB-1115', '登记', '（无新增）Milliseconds Evolution Limited：Companies House 已在登记库（第 86 批）；2026-10-17 样品 PI 已开未付', '', '活跃样品单，留 A 观察'),
    ('SA-004', '登记', '（无新增）Boecek Sec：无公开网页，登记线索在登记库；WhatsApp +49 172 5368536 在联（Simon 2026-10-30）', '', '留 A（Simon 亲联）'),
    ('SA-007', '登记', '（无新增）GO GREEN IT LTD 07614771：Companies House 在登记库 + 申报历史已 watch', '', 'PI 成单户'),
    ('SA-008', '登记', '（无新增）NYNEX satellite OHG / fiberONE：Handelsregister HRA 84829 在登记库', '', 'PI 成单户'),
    # 非洲
    ('SB-110', '登记', 'yellow.ug：iTKATI UG LTD · plot 4646 Muwaire Rd, Kampala（Makindye）· established 2009 · Employees 6–10 · manager Sarah Basemera · +256 785 284579 · IT / CCTV / network / software / websites', 'https://www.yellow.ug/company/40803/itkati-ug-ltd', '6–10 人 IT 小公司 → A-DEEP-11 下放 B'),
    ('SB-1120', '登记', '（未查）Obmac Systems（赞比亚，无域名）：PI 成单户（gg），按成单保留 A1', '', 'PI'),
    ('SB-183', '登记', '未得：Onyx Technology Solutions Limited（乌干达，无域名）网查无法锁定', '', '不可核 → A-DEEP-11 下放 B'),
    ('SB-331', '领英公司页', 'algeriayp / SignalHire / RocketReach：EPE RETELEM SPA（ex-SONATITE）· 54 Rue Omar Benaissa, Alger · established 2008（历史 50+ 年）· 200–500 employees（RocketReach 59 可见）· est. revenue $10M–50M · 业务：telephony IP/hybrid, télécommunications, sécurité industrielle, réception satellitaire · CEO Benchelef Kamel（+213 555 050 850）· Project Director Mustapha Mehessem', 'https://www.signalhire.com/companies/epe-retelem-spa', '阿尔及利亚国有电信/安防集成商（200–500 人）→ 国企采购走招标，留 A 观察'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, bool(url))
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
