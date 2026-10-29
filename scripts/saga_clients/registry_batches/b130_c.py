# -*- coding: utf-8 -*-
"""第 130 批（T29-U118e，2026-10-29）—— **C 池三闸 · 闸 2 第七批 · 其他区段**：闸 1 第 12–25 批（桶 ⑥）候选 75 户中的非俄语区 42 户查底数
（IN 17 / KR 6 / TW 5 / JP 1 / ZA 7 / AU 1 / BR 2 / MX 1 / AE 2）。
路径：IN → zaubacorp / tofler / thecompanycheck / indiafilings / tracxn（CIN / 实收 / 董事）或官网页脚 CIN；KR → bizno / DART / 官网页脚（사업자등록번호）；
TW → twincn / findcompany / 官网（統編）；JP → industlink / baseconnect（法人番号）；ZA → 官网 T&C / 信用申请表 / b2bhint（Reg No / VAT）；
AU → buy.nsw.gov.au（ABN）；BR → 官网页脚 / econodata（CNPJ）；MX → crunchbase / 目录（Razón social）；AE → 官网 / 目录（执照号未取）。
1 查未得 → 未坐实（Enercore / Nextik / TrueView / Lapis / ASI / Mayenet 仅返回同名他户或无结果）；法人 Strike Off 同名（Lapis）→ 不采；
SDT 主业已转量子计算 → 回 C；AGS 域名经 ZoomInfo 落美国 Albuquerque → 国别存疑（KR → US 待核）；Leap Networks 总部阿联酋 + 沙特姊妹公司（表内沙特，两地皆有）。
每户 1 查、depth 1（SC-577 首查误中同名 Leap Technologies，补查 1 次 leap-networks.ae）。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 130
F = '2026-10-29'
IN = '— 印度常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 / 微型 预付 100%）+ FOB 深圳 / DAP 买方清关（进口认证要求由买方核，Saga 仅 CE / RoHS / FCC / REACH / UKCA）；周二 / 周四 11–13 IST'
KR = '— 韩国常规：英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳；无 KC（买方自行认证，SDT 先例）；周二 / 周四 10–12 KST'
TW = '— 台湾常规：中文 / 英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳；周二 / 周四 10–12'
ZA = '— 南非常规：英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳 / DAP 买方清关；周二 / 周四 10–12 SAST'
OT = '— 其他区常规：英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳 / DAP 买方清关；周二 / 周四 当地 10–12'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 印度 · 自有品牌 / 制造商（OEM 对象） ----------------
row('SC-413', 'in', 'Hi-Focus Electronics India Private Limited — HiFocus CCTV（hifocuscctv.com；**CIN U51909TN2015PTC099815；GSTIN 33AADCH5807L1ZJ；2015-03-25 登记；ROC Chennai；实收 ₹1 Cr；15 个 GST 登记（12 活跃）= 多邦分销网络；MD Shobhalal Mukesh Kumar；董事 Mudit Jain / Vikram Singhvi / Meena Bafna**）；表内：自有 HiFocus 品牌 CCTV + PoE 交换机，中国代工', 'IN',
    'IN · 1 次检索：thecompanycheck（CIN / GSTIN / 董事 / 官网 hifocuscctv.com 对上）+ indiafilings + falconebiz（4 董事）；2026-10-29', 'https://www.thecompanycheck.com/company/hifocus-electronics-india-private-limited/U51909TN2015PTC099815',
    'U51909TN2015PTC099815（CIN）', 'Active（MCA 2026）', '2015-03-25', 'Private Limited', '电子安防自有品牌 / 多邦分销（金奈）', 'No. 3 Sunkuvar Agraharam Street, Chintadripet, Chennai, Tamil Nadu 600002', '中型（实收 ₹1 Cr；15 GST 登记）',
    ['Shobhalal Mukesh Kumar — Managing Director', 'Mudit Jain — Director', 'Vikram Singhvi — Director', 'Meena Bafna — Director'],
    '**自有品牌 CCTV 配套 PoE → OEM 30%：一页纸一次（STC-028GP $28 / STC-228GP $33 中性包装 + 贴牌 HiFocus + MOQ 1 + 付费样机）' + IN + '**',
    'OEM 30%；P 池候选 ★（自有品牌 ✔ 中国代工 ✔ 对位 ✔ 坐实 ✔ 多邦网络 ✔）；坐实（CIN / GSTIN / 官网对上）。')
row('SC-1042', 'in', 'Aditya Infotech Limited — CP PLUS / Aditya Group（adityagroup.com；**NSE: CPPLUS / BSE 544466；ISIN INE819V01029；A-12, Sector 4, Noida, UP 201301；1995 起；1,402 人；CP PLUS = 印度最大视频监控品牌（FY26 价值份额 43.3%，Frost & Sullivan 引自年报）；800+ 分销商 / 30,000+ 渠道伙伴；品牌商 + 分销 + 电子制造**）；表内：CP Plus 品牌 CCTV / NVR / PoE 配套', 'IN',
    'IN · 1 次检索：mool.ai/research/nse/cpplus（上市 / 规模 / 份额 / 总部）+ zoominfo（1995 / Noida A-12）；2026-10-29', 'https://mool.ai/research/nse/cpplus',
    'NSE: CPPLUS / BSE 544466（CIN 未抄）', '上市（2025 起）', '1995', 'Public Limited（上市）', '视频监控品牌商 / 分销 / 制造（诺伊达）', 'A-12, Sector 4, Noida, Uttar Pradesh 201301', '巨型（1,402 人；印度第一 CCTV 品牌）',
    ['（具名 KP 未取；表内邮箱为公共）'],
    '**巨头品牌商 OEM 30%（长线）：找 PoE 交换机 / 网络产品线采购负责人一页纸一次（STC-228GP / STC-2224GP / STC-4424GCPM 贴牌 CP PLUS + 中性包装）；不指望群发，LinkedIn 点名**' + IN,
    'OEM 30%；P 池候选 ★ 长线（自有品牌 ✔ 巨型 ✔ 对位 ✔ 坐实 ✔；巨头难进 → 长线）；坐实（上市信息）。')
row('SC-1352', 'in', 'Globus Infocom Limited（globusinfocom.com；**官网页脚 CIN U72100UP2001PLC126647；A-66, Sector-4, Noida, UP 201301；2001 起 25 年；Make-in-India 品牌：教育科技 / 协作会议 & 专业显示 / 安防监控 / 机构家具；销售 +91 8588839434；info@globusinfocom.com；InfoComm 2019 / 2023 / 2024、SECUTECH 2018、Engineer’s Meet 2025 参展**）；表内：自有品牌 CCTV / 显示 / 配套网络', 'IN',
    'IN · 1 次检索：globusinfocom.com（页脚 CIN / 地址）+ /contacts + /events（参展）；2026-10-29', 'https://www.globusinfocom.com/',
    'U72100UP2001PLC126647（CIN）', 'Active（官网 2025）', '2001', 'Public Limited（非上市）', '教育科技 / 显示 / 安防自有品牌（诺伊达）', 'A-66, Sector-4, Noida, District Gautam Buddha Nagar, Uttar Pradesh 201301', '中型（25 年品牌；多条产品线）',
    ['（具名 KP 未取；销售热线 +91 8588839434）'],
    '**自有品牌多线 → OEM 30%：一页纸一次（STC-228GP / STC-2224GP 贴牌 Globus + 中性包装 + MOQ 1 + 付费样机；教育校园 PoE 场景）' + IN + '**',
    'OEM 30%；P 池候选 ★（自有品牌 ✔ 参展活跃 ✔ 对位 ✔ 坐实 ✔）；坐实（官网页脚 CIN）。')
row('SC-1365', 'in', 'Masibus Automation And Instrumentation Private Limited（masibus.com；**CIN U32201GJ1987PTC009994；1987-09-21 登记（1975 起）；ROC Ahmedabad；授权 ₹3.70 Cr / 实收 ₹3.08 Cr；B-30, GIDC Electronics Estate, Sector-25, Gandhinagar, Gujarat 382042；135 人（2024-10，tracxn）；FY25 营收 ₹100–500 Cr；AGM 2025-09-29；董事 Vidya Subramaniam / Dominic Joseph Cordeiro；Associate Director Operation Sales D Kachhiya（indiamart）**）；表内：工业仪表制造商，进口三旺工业交换机配套', 'IN',
    'IN · 1 次检索：thecompanycheck（CIN / 资本 / 地址 / AGM）+ tracxn（135 人 / 营收档）+ indiamart 注册信息页（董事 DIN / 销售负责人）；2026-10-29', 'https://www.thecompanycheck.com/company/masibus-automation-and-instrumentation-private-limited/U32201GJ1987PTC009994',
    'U32201GJ1987PTC009994（CIN）', 'Active（MCA 2026）', '1987-09-21', 'Private Limited', '工业自动化仪表制造（甘地讷格尔）', 'B-30, GIDC Electronics Estate, Sector-25, Gandhinagar, Gujarat 382042', '中型（135 人；₹100–500 Cr）',
    ['Vidya Subramaniam — Director（DIN 00022694）', 'Dominic Joseph Cordeiro — Director（DIN 00022731）', 'D Kachhiya — Associate Director Operation Sales'],
    '**工业仪表商配套工业交换机 → OEM 30%：点名 D Kachhiya 一页纸一次（STI-280GE $46.6 / STI-288GPM $78.9 / STI-244DGGPM 贴牌 Masibus + 中性包装；三旺不点名）' + IN + '**',
    'OEM 30%；P 池候选 ★（制造商 ✔ 已进口中国工业交换机 ✔ 对位 ✔ 坐实 ✔ 具名销售负责人 ✔）；坐实。')
row('SC-1371', 'in', 'WatchDog = Apollo Infoways Pvt. Ltd.（mywatchdog.in；**官网：H-102, Sector-63, Noida, UP 201301；Toll Free 1800 309 9415；info@mywatchdog.in；自有品牌 WatchDog：PoE / 工业 / 数据中心（自述至 800G）交换机 + 路由 / 无线 / 光模块 / 防火墙；"Engineered in Noida"；GeM 上架、政府 / PSU / 国防采购资质自述；Bangalore / Dubai / Singapore 办事处；产品 PDF 页脚署 Apollo Infoways Pvt. Ltd.**）；CIN 未取；表内：自有品牌交换机全线（洪瑞 / 丰润达 / AOA 现供 → Q-33）', 'IN',
    'IN · 1 次检索：mywatchdog.in 首页 + /contact.html（地址 / 办事处）+ 10G-Data-Center-Switch PDF（法人名 Apollo Infoways）；CIN 未取；2026-10-29', 'https://www.mywatchdog.in/',
    '未取（法人 Apollo Infoways Pvt. Ltd. 自报，CIN 未查）', '营业中（官网 2025）', '未取', 'Private Limited', '网络设备自有品牌（诺伊达）', 'H-102, Sector-63, Noida, Gautam Budh Nagar, Uttar Pradesh 201301', '中型（4 城办事处；全线产品）',
    ['（具名 KP 未取；Toll Free + info@ 官网公开）'],
    '**全线自有品牌 = OEM 对象 → OEM 30%：一页纸一次（STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W 贴牌 WatchDog + MOQ 1；洪瑞现供 → Q-33 口径：默认只推 SmartByte / Marvell 管理 + 工业线；现供厂商不点名）' + IN + '**',
    'OEM 30%；P 池候选 ★（自有品牌全线 ✔ 对位 ✔ 多城 ✔）；部分坐实（法人名自报，CIN 未取）；Q-33 洪瑞现供待 Simon。')
row('SC-1521', 'in', 'Nivetti Systems Private Limited（nivettisystems.com；**166, 21st Main Road, 2nd Phase, J P Nagar, Bangalore 560078（Bloomberg）；2014 创立；51–200 人（ZoomInfo）；自研路由 / 交换 / NiOS 网络操作系统 / HawkSecure；2024-03-09 印度首台自研 2.4 Tbps 路由器（联邦部长 Vaishnaw 揭幕，PTI）**）；CIN 未取；表内：自有品牌路由 / 交换机', 'IN',
    'IN · 1 次检索：bloomberg profile（地址）+ cbinsights（2014 / 产品 / 2.4 Tbps 新闻）+ zoominfo（规模）；CIN 未取；2026-10-29', 'https://www.cbinsights.com/company/nivetti-systems',
    '未取（CIN 未查）', '营业中（2024 新闻 / 2026 目录）', '2014', 'Private Limited', '安全网络设备自研品牌（班加罗尔）', '166, 21st Main Road, 2nd Phase, J P Nagar, Bangalore, Karnataka 560078', '中型（51–200 人）',
    ['（具名 KP 未取）'],
    '**高端自研、接入层 / PoE 可能贴牌 → OEM 30%（长线）：一页纸一次（STC-2224GP / STC-4424GCPM 贴牌 + 中性包装 + MOQ 1；不谈 SONiC / 白盒）' + IN + '**',
    'OEM 30%；P 池候选 ○ 长线（自有品牌 ✔ 对位（接入层）✔）；部分坐实（CIN 未取）。')

# ---------------- 印度 · 分销 / 集成 / ISP ----------------
row('SC-898', 'in', 'Plexonics Technologies Limited（plexonics.com；**CIN U72900CH2011PLC033105；PAN AACCE7703P；2011-07-12 登记；非上市公众公司；ROC Chandigarh；授权 ₹10 Cr / 实收 ₹5.35 Cr（tofler；thecompanycheck 载 ₹1.35 Cr）；181/23 First Floor, Industrial Area Phase 1, Chandigarh 160002；董事 Come Alexandre Carpentier / Avneet Bansal / Akshay Sharma；finance@plexonics.com；IT 产品零售 & 分销**）；表内：Belden + 多牌中国 PoE 分销', 'IN',
    'IN · 1 次检索：thecompanycheck（CIN / 董事 / 地址）+ tofler（PAN / 实收 / 邮箱）；2026-10-29', 'https://www.tofler.in/plexonics-technologies-limited/company/U72900CH2011PLC033105',
    'U72900CH2011PLC033105（CIN）', 'Active（MCA 2026）', '2011-07-12', 'Public Limited（非上市）', 'IT / 网络产品分销（昌迪加尔）', '181/23 First Floor, Industrial Area Phase 1, Chandigarh 160002', '中型（实收 ₹5.35 Cr）',
    ['Come Alexandre Carpentier — Director', 'Avneet Bansal — Director', 'Akshay Sharma — Director'],
    '**中型分销 20%：一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 分销价 + MOQ 1 + 付费样机；Belden 不点名）' + IN + '**',
    '分销 20%；P 池候选 ★（分销主体 ✔ 多牌进口 ✔ 对位 ✔ 坐实 ✔）；坐实。')
row('SC-463', 'in', 'Atronic Systems Pvt Ltd（atronic.co.in；**官网页脚：1st & 3rd Floors, CM-17, Gopala Sweet, Sector-122, Noida, UP 201316；+91 87964 26475；ZoomInfo：51–200 人 / <$5M / 另址 26 Block C, Noida 201304；Operations Head Arti Kohli；门禁 / RFID / RTLS / 机器人 / 远程塔站管理 / 公共监控信息系统**）；CIN 未取；表内：方案商，ONV 交换机原样转售', 'IN',
    'IN · 1 次检索：atronic.co.in/products/（页脚法人 / 地址 / 电话）+ zoominfo（规模 / Operations Head）；CIN 未取；2026-10-29', 'https://atronic.co.in/products/',
    '未取（CIN 未查）', '营业中（官网 2022 / 目录 2026）', '未取', 'Private Limited', '安防 / 物联网方案集成（诺伊达）', '1st & 3rd Floors, CM-17, Gopala Sweet, Sector-122, Noida, Uttar Pradesh 201316', '中型（51–200 人）',
    ['Arti Kohli — Operations Head'],
    '**方案商集成 25%：点名 Arti Kohli 一页纸一次（STC-228GP / STI-288GPM 塔站 / 门禁 PoE 场景 + MOQ 1 + 付费样机；ONV 不点名）' + IN + '**',
    '集成 25%；P 池候选 ○（集成主体 ✔ 已用中国 PoE ✔ 对位 ✔）；部分坐实（CIN 未取）。')
row('SC-1339', 'in', 'Econtrol Devices Private Limited（econtroldevices.com；**CIN U51909HR2019PTC081687；PAN AAFCE5794H；2019-07-29 登记；ROC Delhi；实收 ₹1 lakh；FY22 营收 <₹1 Cr；Plot No-A2, BPTP District-1, Block-B, Sector-81, Faridabad, Haryana 121002；董事 Rekha Sorout（MCA 登记邮箱 rekha.sorout@econtroldevices.com）/ Amit Kumar；其他批发**）；表内：Atop（台湾）工业交换机进口', 'IN',
    'IN · 1 次检索：zaubacorp（CIN / 董事 / 地址）+ tofler（PAN / 营收档 / 登记邮箱）+ thecompanycheck；2026-10-29', 'https://www.tofler.in/econtrol-devices-private-limited/company/U51909HR2019PTC081687',
    'U51909HR2019PTC081687（CIN）', 'Active（MCA 2026）', '2019-07-29', 'Private Limited', '工业网络设备批发（法里达巴德）', 'Plot No-A2, BPTP District-1, Block-B, Sector-81, Faridabad, Haryana 121002', '微型（₹1 lakh；<₹1 Cr）',
    ['Rekha Sorout — Director（rekha.sorout@econtroldevices.com = MCA 登记邮箱）', 'Amit Kumar — Director'],
    '**微型进口商 → 分销 20% + 预付 100%：点名 Rekha Sorout 一页纸一次（STI-280GE $46.6 / STI-288GPM $78.9 + MOQ 1 + 付费样机；Atop 不点名）' + IN + '**',
    '分销 20% + 预付 100%；P 池候选 △（进口台湾工业线 ✔ 对位 ✔ 坐实 ✔ 但微型 → 观察档）；坐实。')
row('SC-1344', 'in', 'Excell Media Private Limited（excellmedia.net；**CIN U64203TG1998PTC030014；1998-08-26 登记；ROC Hyderabad；授权 / 实收 ₹6 Cr；Quinn House, 8-2-268/N/28/A/2, Road No. 2, Banjara Hills, Hyderabad, Telangana 500034；info@excellmedia.net（MCA 登记）；ISP / 宽带服务**）；表内：区域 ISP 自用，进口 Volktek 管理型交换机', 'IN',
    'IN · 1 次检索：zaubacorp（CIN / 地址 / 邮箱）+ thecompanycheck（实收 / 行业）+ edgeinsights（官网对上）；2026-10-29', 'https://www.zaubacorp.com/EXCELL-MEDIA-PRIVATE-LIMITED-U64203TG1998PTC030014',
    'U64203TG1998PTC030014（CIN）', 'Active（MCA 2026）', '1998-08-26', 'Private Limited', '区域 ISP / 宽带（海得拉巴）', '8-2-268/N/28/A/2, Road No. 2, Banjara Hills, Hyderabad, Telangana 500034', '中型（实收 ₹6 Cr；28 年）',
    ['（具名 KP 未取；info@ 为 MCA 登记邮箱）'],
    '**中型区域 ISP 自用进口 = 有进口经验者 → 直客 25%：一页纸一次（STC-2224GP $86 / STC-4424GCPM $165 接入 + 付费样机；Volktek 不点名）' + IN + '**',
    '直客 25%；P 池候选 ○（已进口台湾管理型 ✔ 对位 ✔ 坐实 ✔；中型区域 ISP ≠ 巨头运营商）；坐实。')
row('SC-1403', 'in', 'Triflex Infocom（triflexinfo.com；**#497/B, 1st Floor, 8th Cross, 8th Main, HAL 3rd Stage, Bangalore 560075（fundoodata / vcsdata）；2004 创立；IT 基建 SME；<$5M（ZoomInfo）**）；CIN 未取；表内：IT 集成，进口中国 MC / PoE', 'IN',
    'IN · 1 次检索：fundoodata（地址 / 行业）+ zoominfo（2004 / 规模）+ vcsdata；CIN 未取；2026-10-29', 'https://www.fundoodata.com/companies-detail/Triflex-Infocom/56479.html',
    '未取（CIN 未查）', '营业中（目录 2026）', '2004', '未取（SME）', 'IT 基础设施集成（班加罗尔）', '#497/B, 1st Floor, 8th Cross, 8th Main, HAL 3rd Stage, Bangalore, Karnataka 560075', '小型（<$5M）',
    ['（具名 KP 未取）'],
    '**小集成 25%：一页纸一次（STC-028GP $28 / STC-228GP $33 + MOQ 1 + 付费样机）' + IN + '**',
    '集成 25%；P 池候选 ○（集成主体 ✔ 已进口中国同类 ✔ 对位 ✔）；部分坐实（目录页，CIN 未取）。')

# ---------------- 印度 · 回 C（未坐实 / 红旗） ----------------
row('SC-324', 'in', 'Enercore（enercore.co.in；**1 查仅得 Enercore Solutions Private Limited（CIN U62013HR2023PTC113183；2023-07-10；Gurgaon Sector-56 住宅地址 J-6058 Devender Vihar；实收 ₹1 lakh；董事 Manav Yadav / Sanjeev Yadav；IT 服务类）— 与 enercore.co.in 归属未证 → 未坐实**）；表内：询过工业交换机', 'IN',
    'IN · 1 次检索：tofler / thecompanycheck / filesure 同名 Enercore Solutions（Gurgaon 2023 微型）→ 域名未对上；2026-10-29', '',
    '未取（同名 CIN U62013HR2023PTC113183 不采）', '未坐实', '未取', '未取', '工业网络（印度，待证）', '未取', '未知（同名户为微型）',
    ['（具名 KP 未取）'],
    '**未坐实 → 回 C 储备；来信再起则预付 100%**' + IN,
    '回 C（未坐实：1 查仅同名微型他户）。')
row('SC-509', 'in', 'Nextik（nextik.co.in；**1 查仅得 X 账号 @nextik_official（"Advanced data communication equipment / Customized Innovations"，India）+ 同名他户 Netik IT Technologies（Hyderabad）/ Nextlink Technologies（Bangalore）→ 法人未取 → 未坐实**）；表内：自称数据通信设备品牌', 'IN',
    'IN · 1 次检索：x.com/nextik_official + indiafilings / zaubacorp 同名他户 → 法人未取；2026-10-29', '',
    '未取', '未坐实', '未取', '未取', '数据通信设备（印度，待证）', '未取', '未知',
    ['（具名 KP 未取）'],
    '**未坐实 → 回 C 储备；来信再起则 OEM 30% + 预付 100%**' + IN,
    '回 C（未坐实：仅社媒账号，法人未取）。')
row('SC-969', 'in', 'TrueView（trueview.co.in；**1 查仅得同名：True View Technologies Private Limited（CIN U74999MR2008PTC475132；L-305-A, Dua Complex, Shakarpur, East Delhi 110092；2008-06-04；54 人（2025-08）；FY25 <₹10 Cr）/ TrueView Corporate Services（Mumbai 2022）— trueview.co.in 归属未证（疑 Delhi 户）→ 未坐实**）；表内：自有 TrueView 品牌 CCTV；具名 KP manish@ / rupesh.bagde@', 'IN',
    'IN · 1 次检索：tracxn 同名两户（Delhi 2008 / Mumbai 2022）→ 域名未对上；2026-10-29', '',
    '未取（疑似 CIN U74999MR2008PTC475132 未证，不采）', '未坐实', '未取', '未取', 'CCTV 自有品牌（印度，待证）', '未取（疑 Shakarpur, East Delhi）', '未知（疑 54 人）',
    ['Manish — （表内具名邮箱）', 'Rupesh Bagde — （表内具名邮箱）'],
    '**未坐实 → 回 C 储备；具名 KP 在 → 来信再起则补查 CIN + OEM 30% + 预付 100%**' + IN,
    '回 C（未坐实：同名多户，域名归属未证；自有品牌线索保留）。')
row('SC-1203', 'in', 'Lapis Technologies（lapistechnologies.in；**1 查仅得 Lapis Technologies Private Limited（CIN U74993KA2018PTC109130；R 11/12, Megur Prakash, APMC Yard, Sagar Road, Shimoga, Karnataka 577204；2018-01-02；₹1 lakh；gmail 登记邮箱；zaubacorp 状态 Strike Off（tracxn 载 Active）；董事 Sriranga Talavane / Siddarth Hebbar）— 与 CCTV / PoE 站归属未证 + 注销红旗 → 未坐实**）', 'IN',
    'IN · 1 次检索：zaubacorp（Strike Off）+ tracxn 同名 → 域名未对上；2026-10-29', '',
    '未取（同名 CIN U74993KA2018PTC109130 Strike Off 不采）', '未坐实（同名户 Strike Off）', '未取', '未取', 'CCTV / PoE 配件（印度，待证）', '未取', '未知',
    ['（具名 KP 未取）'],
    '**未坐实 + 同名注销红旗 → 回 C 储备；来信再起则预付 100%**' + IN,
    '回 C（未坐实 + 红旗）。')
row('SC-1322', 'in', 'ASI（asi.ind.in；**1 查仅得 ASI Industries（孟买 矿业上市 502015）/ Asiatic Electrical & Switchgear（New Delhi）等同名 → 法人未取 → 未坐实**）；表内：admin@asi.ind.in 公共邮箱', 'IN',
    'IN · 1 次检索：pitchbook / contactout / crunchbase 同名他户 → 域名未对上；2026-10-29', '',
    '未取', '未坐实', '未取', '未取', '未知（印度，待证）', '未取', '未知',
    ['（具名 KP 未取）'],
    '**未坐实 → 回 C 储备**' + IN,
    '回 C（未坐实：1 查仅同名他户）。')
row('SC-1366', 'in', 'Mayenet（mayenet.com / mayenetsolutions.com；**1 查仅得 Mazenet Solution（Chennai Nungambakkam；IT 服务 / 铁路项目）等近名他户 → 法人未取 → 未坐实**）；表内：真意向 — 想拿样；具名 ikar@mayenet.com', 'IN',
    'IN · 1 次检索：crunchbase / devex / rocketreach 近名 Mazenet → 域名未对上；2026-10-29', '',
    '未取', '未坐实', '未取', '未取', '网络方案（印度，待证）', '未取', '未知',
    ['Ikar — （表内具名邮箱 ikar@mayenet.com）'],
    '**未坐实但真意向（想拿样）→ 回 C 储备 + 例外：直接回一次样品报价（STC-228GP 样机 $35 + 运费，预付 100%）看回信，回信即补查法人**' + IN,
    '回 C（未坐实；真意向保留 → 单次样品报价例外）。')

# ---------------- 韩国 ----------------
row('SC-185', 'kr', '(주)다산네트웍스 DASAN Networks, Inc.（dasannetworks.com；**사업자등록번호 129-81-16613；법인등록번호 110111-0924765；KOSDAQ 039560；1993-03-04 설립；대표 남민우 Nam Min Woo；DASAN Tower 10F, 49 Daewangpangyo-ro 644beon-gil, Bundang-gu, Seongnam, Gyeonggi 13493；070-7010-1000；유선 통신장비 제조；44 人在册（控股层面）**）；表内：长期进口三旺工业交换机；具名 KP 在', 'KR',
    'KR · 1 次检索：bizno.net/article/1298116613（사업자 / 법인번호 / 대표 / 주소）+ englishdart.fss.or.kr（KOSDAQ 039560 / 1993）；2026-10-29', 'https://englishdart.fss.or.kr/dsbc001/selectPopup.ax?selectKey=00268251',
    '129-81-16613（사업자등록번호）/ 110111-0924765（법인등록번호）', '계속사업자（KOSDAQ 上市）', '1993-03-04', '주식회사（上市）', '有线通信设备制造（城南板桥）', 'DASAN Tower 10F, 49 Daewangpangyo-ro 644beon-gil, Bundang-gu, Seongnam-si, Gyeonggi-do 13493', '大型（上市集团；DZS 母体）',
    ['남민우 Nam Min Woo — 대표이사'],
    '**上市设备商贴牌 / 配套 → OEM 30%（长线）：点名表内 KP 一页纸一次（STI-288GPM / STI-488DGGPM 工业线 + STC-4424GCPM 贴牌 + 中性包装；三旺不点名；无 KC 买方自证）' + KR + '**',
    'OEM 30%；P 池候选 ★ 长线（上市品牌商 ✔ 已进口中国工业线 ✔ 对位 ✔ 坐实 ✔）；坐实（DART）。')
row('SC-387', 'kr', '(주)디지타스 DGTAS（dgtas.co.kr；**官网页脚：사업자등록번호 114-87-02536；대표 최상윤；경기도 안산시 단원구 범지기로 147；TEL 031-455-0017 / FAX 031-491-0420；DGTAS@DGTAS.CO.KR；AHD / IP / 特种摄像机 R&D 制造 + 整新（Refurbishment）业务**）；表内：摄像机厂，微信路径在', 'KR',
    'KR · 1 次检索：dgtas.co.kr（页脚 사업자 / 대표 / 地址 / 产品页）；2026-10-29', 'https://www.dgtas.co.kr/page/page11',
    '114-87-02536（사업자등록번호）', '营业中（官网 2026）', '未取', '주식회사', '摄像机 R&D 制造（安山）', '경기도 안산시 단원구 범지기로 147', '小型 / 中型（制造 + 整新）',
    ['최상윤 — 대표'],
    '**摄像机厂配套 PoE → OEM 30%：微信 / 邮件一页纸一次（STC-028GP $28 / STC-228GP $33 贴牌 DGTAS + 中性包装 + MOQ 1 + 付费样机）' + KR + '**',
    'OEM 30%；P 池候选 ★（制造商 ✔ 微信路径 ✔ 对位 ✔ 坐实 ✔）；坐实（官网页脚）。')
row('SC-455', 'other', 'AGS Electronics（ags-electronics.com；**1 查 ZoomInfo：AGS-Electronics, 6565 Americas Pkwy NE Ste 200, Albuquerque, NM（美国）；(505) 550-6501；11–50 人；<$5M；电子制造 — 表内「韩国」与检索结果国别不一致 → 国别存疑（KR → US 待核）；韩国法人未取**）；表内：Atop 工业交换机经销，sales@ 公共邮箱', 'KR',
    'KR/US · 1 次检索：zoominfo.com/c/ags-electronics-inc/368409713（域名对上但落美国）；韩国 사업자 未取；2026-10-29', 'https://www.zoominfo.com/c/ags-electronics-inc/368409713',
    '未取（国别待核）', '营业中（目录 2026）', '未取', '未取', '工业网络 / 电子（国别存疑：韩国表内 / 美国检索）', '6565 Americas Pkwy NE Ste 200, Albuquerque, NM（ZoomInfo，待核）', '小型（11–50 人）',
    ['（具名 KP 未取）'],
    '**国别待核：若美国 = 主区 ✔ → 分销 20% 一页纸（STI-280GE / STI-288GPM 工业线 + MOQ 1；Atop 不点名）；若韩国 → 常规 + 无 KC**' + OT,
    '分销 20%；P 池候选 △（进口台湾工业线 ✔ 对位 ✔ 但国别存疑 KR → US 待核 + 法人未取 → 观察档）；部分坐实。')
row('SC-493', 'kr', '(주)아이디스 IDIS Co., Ltd.（Intelligent Digital Integrated Security Co., Ltd.；idisglobal.com / idis.co.kr；**사업자 314-86-25786；법인 160111-0302755；1997-09-24 설립（2011-07-01 인적분할 신설）；대표 김영달；대전 유성구 테크노3로 8-10（관평동）34012；031-723-5000；409 人；KOSDAQ**）；表内：韩国监控品牌龙头，自有 PoE 配套', 'KR',
    'KR · 1 次检索：bizno.net/article/3148625786（사업자 / 법인 / 대표 / 주소 / 409 人）+ IDIS Holdings 사업보고서（1997 / 分割）；2026-10-29', 'https://bizno.net/article/3148625786',
    '314-86-25786（사업자등록번호）/ 160111-0302755（법인등록번호）', '계속사업자（KOSDAQ 上市）', '1997-09-24', '주식회사（上市）', '视频监控设备制造（大田）', '대전광역시 유성구 테크노3로 8-10（관평동）34012', '大型（409 人；上市）',
    ['김영달 — 대표이사'],
    '**监控品牌龙头 → OEM 30%（长线）：找硬件采购一页纸一次（STC-228GP / STC-2224GP 贴牌 IDIS + 中性包装 + MOQ 1；无 KC 买方自证）' + KR + '**',
    'OEM 30%；P 池候选 ★ 长线（上市品牌商 ✔ 对位 ✔ 坐实 ✔）；坐实。')
row('SC-1191', 'kr', '(주)씨앤지시스템 CNG System（cngsystem.com → dialogic.co.kr；**站点标题「::: CNG System ::: ㈜씨앤지시스템」；服务器定位 Seoul 동작구；Dialogic / AudioCodes / Sangoma 通信卡 / 录音板分销；사업자 未取（同名 주식회사 씨앤지 127-86-49224 为杨州金属加工，不采）**）；表内：问过 CENTEC 交换机；support@dialogic.co.kr', 'KR',
    'KR · 1 次检索：dialogic.co.kr.siteindices.com（站点标题 / 定位）；bolta 同名不对应；사업자 未取；2026-10-29', 'https://dialogic.co.kr.siteindices.com/',
    '未取（사업자 未查到）', '营业中（站点在线）', '未取', '주식회사', '通信卡 / 电信设备分销（首尔）', '未取（Seoul, 동작구 服务器定位）', '小型 / 中型',
    ['（具名 KP 未取）'],
    '**CENTEC 敲门砖 → 分销 20%：一页纸一次（STH-2C24XF-HSI $1,500 / STH-8C48DX-HSI $4,800 + STC 接入线；无 KC 买方自证）换 dialogic.co.kr 地址再发' + KR + '**',
    '分销 20%；P 池候选 ○（CENTEC 意向 ✔ 分销主体 ✔ 对位 ✔）；部分坐实（사업자 未取）。')
row('SC-1243', 'kr', 'SDT Inc. 에스디티 주식회사（sdt.inc；**官网页脚：사업자등록번호 630-87-00933；서울 강남구 테헤란로44길 5, 10층 06211；CEO 윤지원 Jiwon Yune；主业 = 全栈量子计算（QDM：控制电子 / 极低温机械 / 量子计算机；QubeStack GS 认证 1 等级；Quantum Korea 2026 参展）**）；表内：曾想分销工业交换机（KC 问题）', 'KR',
    'KR · 1 次检索：sdt.inc 首页 + /about-us/events/quantum-korea-2026（页脚 사업자 / 地址 / 主业）；2026-10-29', 'https://sdt.inc/',
    '630-87-00933（사업자등록번호）', '营业中（官网 2026）', '未取', '주식회사', '量子计算软硬件（首尔；原工业 IoT）', '서울시 강남구 테헤란로44길 5, 10층 06211', '中型（量子初创）',
    ['윤지원 Jiwon Yune — CEO'],
    '**主业已转量子计算 → 分销意向过期 → 回 C 储备（来信再起则常规 + KC 买方自证）**' + KR,
    '回 C（坐实但主业转向，品类不再对位；KC 待 Simon 口径）。')

# ---------------- 台湾 / 日本 ----------------
row('SC-172', 'tw', 'COP Security System Corp.（cop-security.com；**1992 创立；4-6F, No.5, Lane 130, Minquan Rd, Xindian, New Taipei；sales@cop-security.com；联系人 Tony Jiang（asmag）；ZoomInfo 营收 $14.5M；CCTV / IP 摄像机 / 浪涌保护 / IR 照明 / 传输 制造**）；統編未取；表内：监控厂配套', 'TW',
    'TW · 1 次检索：zoominfo（营收 / 地址）+ crunchbase（法人名 / sales@）+ asmag（1992 / Tony Jiang）；統編未取；2026-10-29', 'https://www.asmag.com/suppliers/companyinfo.aspx?co=copsecurity',
    '未取（統編未查）', '营业中（目录 2026）', '1992', '股份有限公司', 'CCTV 制造（新北新店）', '4-6F, No.5, Lane 130, Minquan Rd, Xindian Dist., New Taipei City', '中型（$14.5M）',
    ['Tony Jiang — 联系人（asmag）'],
    '**监控厂配套 PoE → OEM 30%：点名 Tony Jiang 中文一页纸一次（STC-028GP $28 / STC-228GP $33 贴牌 COP + MOQ 1 + 付费样机）' + TW + '**',
    'OEM 30%；P 池候选 ★（制造商 ✔ 对位 ✔ 具名联系人 ✔）；部分坐实（統編未取）。')
row('SC-465', 'tw', '陞泰科技股份有限公司 AV TECH CORPORATION（avtech.com.tw；**統編 97092770；上市 8072；設立 1996-06-26；實收資本 NT$8 億；代表人 陳世忠；新北市三重區中興北街 193-2 號；02-2655-3866；登记信箱 lydia.lin@avtech.com.tw；出進口廠商登記 1996-08-29**）；表内：上市监控品牌，自有 PoE 配套中国代工', 'TW',
    'TW · 1 次检索：twincn.com/item.aspx?no=97092770（統編 / 上市 / 代表人 / 地址）+ findcompany（資本 / 登记信箱）；2026-10-29', 'https://twincn.com/item.aspx?no=97092770',
    '97092770（統編）', '核准設立（上市 8072）', '1996-06-26', '股份有限公司（上市）', '视频监控设备制造（新北三重）', '新北市三重區中興北街 193-2 號', '大型（上市；實收 NT$8 億）',
    ['陳世忠 — 代表人 / 董事長', 'lydia.lin@avtech.com.tw — 登记信箱（findcompany）'],
    '**上市监控品牌 → OEM 30%（长线）：找采购 / 产品部中文一页纸一次（STC-228GP / STC-2224GP 贴牌 AVTECH + 中性包装 + MOQ 1）' + TW + '**',
    'OEM 30%；P 池候选 ★ 长线（上市品牌商 ✔ 对位 ✔ 坐实 ✔）；坐实。')
row('SC-491', 'tw', '昇銳智慧科技股份有限公司 Hi Sharp Intelligence Technology Co., Ltd.（原 昇銳電子股份有限公司；hisharp.com；**統編 22601576；上櫃 3128；成立 1987-09-23；實收 NT$4.73 億；董事長 江添貴；總經理 / 發言人 蕭哲彥；桃園市八德區長興路 673 號；03-3653121；fred@hisharp.com.tw（公司資料）**）；表内：监控品牌，洪瑞现供 → Q-33', 'TW',
    'TW · 1 次检索：twincn.com/item.aspx?no=22601576（統編 / 上櫃 / 代表人）+ hisharp.com/zh-tw/governance.php（公司基本資料）+ wantgoo（實收 / 邮箱）；2026-10-29', 'https://www.hisharp.com/zh-tw/governance.php',
    '22601576（統編）', '核准設立（上櫃 3128）', '1987-09-23', '股份有限公司（上櫃）', '电子监视系统制造 / 进出口（桃园八德）', '桃園市八德區長興路 673 號', '大型（上櫃；實收 NT$4.73 億）',
    ['江添貴 — 董事長', '蕭哲彥 — 總經理 / 發言人', '鄭忠恕 — 代理發言人'],
    '**上櫃监控品牌 → OEM 30%：中文一页纸一次（STC-228GP / STC-2224GP 贴牌 Hi Sharp + 中性包装；洪瑞现供 → Q-33 口径：默认只推 SmartByte / Marvell 管理 + 工业线）' + TW + '**',
    'OEM 30%；P 池候选 ★（上櫃品牌商 ✔ 对位 ✔ 坐实 ✔）；坐实；Q-33 洪瑞现供待 Simon。')
row('SC-1029', 'tw', 'Xentino Technologies Corp.（xentino.com；**官网 Company Tax Number 54303706；9F, No 20, Zhong 1st Road, Keelung 20041（EC21 另载 5F, No.89, Aly. 3, Ln. 182, Sec. 2, Wenhua Rd., Banqiao）；2013 起（品牌 2000 起 xDSL 中东 / 东欧）；6–10 人；年营收 USD 100–500k；GM Sinan Bedir；+886-2-82581593**）；表内：自有品牌交换机 / 工业交换机 / 路由 / GPON 全线', 'TW',
    'TW · 1 次检索：xentino.com/index.cfm?fuseaction=objects2.company（Tax No / 地址 / 产品线）+ xentino.en.ec21.com（规模 / GM）；2026-10-29', 'https://www.xentino.com/index.cfm?fuseaction=objects2.company',
    '54303706（統編，官网自报）', '营业中（官网 / EC21）', '2013', '有限公司', '网络设备自有品牌（基隆 / 新北）', '9F, No 20, Zhong 1st Road, Keelung 20041', '微型（6–10 人；USD 100–500k）',
    ['Sinan Bedir — GM'],
    '**微型自有品牌面向土耳其 / 中东 / 东欧（= 主区）→ OEM 30% + 预付 100%：点名 Sinan Bedir 英文 / 土耳其语一页纸一次（STC-228GP / STI-288GPM 贴牌 Xentino + MOQ 1 + 付费样机）' + TW + '**',
    'OEM 30% + 预付 100%；P 池候选 △（自有品牌 ✔ 主区市场 ✔ 坐实 ✔ 但微型 → 观察档）；坐实（統編官网自报）。')
row('SC-1134', 'tw', 'XP Networks / XP Active Systems = ANTEK TECHNOLOGY CO., LTD.（xp-networks.com；**官网 About / Contact：11F, 51 Hengyang Road, Taipei 100；+886 2-29124340 / FAX 2-29100012；info@xp-networks.com**）；統編未取；表内：自有 XP 品牌交换机', 'TW',
    'TW · 1 次检索：xp-networks.com/about-us/ + /contact-info/contact-us/（法人名 / 地址 / 电话）；統編未取；2026-10-29', 'https://www.xp-networks.com/about-us/',
    '未取（統編未查）', '营业中（官网在线）', '未取', '有限公司', '网络设备自有品牌（台北）', '11F, 51 Hengyang Road, Taipei 100', '小型',
    ['（具名 KP 未取）'],
    '**自有品牌 → OEM 30%：中文一页纸一次（STC-228GP / STC-2224GP 贴牌 XP + 中性包装 + MOQ 1 + 付费样机）' + TW + '**',
    'OEM 30%；P 池候选 ○（自有品牌 ✔ 对位 ✔）；部分坐实（統編未取）。')
row('SC-485', 'other', 'FXC株式会社 FXC, Inc.（fxc.jp；**法人番号 4010501029351；設立 2001-01；資本金 1 億円；50–100 人；〒111-0053 東京都台東区浅草橋 3-20-15 浅草橋ミハマビル 7F；関西（新大阪）/ 九州（博多）営業所；ネットワーク機器の製造・販売・導入支援（メディアコンバータ / スイッチ 自有品牌）**）；表内：日本自有品牌 MC / 交换机', 'JP',
    'JP · 1 次检索：industlink.jp/company/1562839232/（法人番号 / 地址 / 規模 / 拠点）+ baseconnect（資本金 / 2001）；2026-10-29', 'https://industlink.jp/company/1562839232/',
    '4010501029351（法人番号）', '营业中（2026）', '2001-01', '株式会社', '网络设备制造 / 销售（东京台东）', '〒111-0053 東京都台東区浅草橋 3-20-15 浅草橋ミハマビル 7F', '中型（50–100 人；資本金 1 億円）',
    ['（具名 KP 未取）'],
    '**日本自有品牌 → OEM 30%：英文 / 日文一页纸一次（STC-228GP / STC-2224GP / STI-288GPM 贴牌 FXC + 中性包装 + MOQ 1 + 付费样机）' + OT + '**',
    'OEM 30%；P 池候选 ★（自有品牌 ✔ 中型 ✔ 对位 ✔ 坐实 ✔）；坐实（法人番号）。')

# ---------------- 南非 ----------------
row('SC-298', 'other', 'MiRO Distribution（miro.co.za；**Enterprise No. B2002068592（2002-08-26 注册；Close corporation → 公司转换）；VAT 9199666141；R25M+ 档；法定地址 Unit 6, N1 Industrial Park, Landsmark Avenue, Kosmosdal Ext.11, Samrand 1685 / 营业 9 Landmarks Ave, Samrand Business Park, Centurion；+27 12 657 0960；sales@miro.co.za；品牌 Cambium / Ubiquiti / Grandstream / BDCOM / MikroTik / Siklu / Tenda / TP-Link / Mimosa / Edge-corE / Radwin / Ajax；覆盖南部非洲 10 国**）；表内：无线 / 网络大分销', 'ZA',
    'ZA · 1 次检索：b2bhint（注册号 / VAT / 法定地址 / 规模档）+ opening-hours（品牌 / 覆盖国）+ africabz；2026-10-29', 'https://b2bhint.com/en/company/za/miro-distribution--B2002068592',
    'B2002068592（Enterprise No.）/ VAT 9199666141', 'Active（2024-12 核）', '2002-08-26', '(Pty) Ltd（原 CC）', '网络 / 无线 / IP 视频分销（森图里恩）', '9 Landmarks Ave, Samrand Business Park, Centurion 0157', '中型 / 大型（R25M+；10 国）',
    ['（具名 KP 未取；sales@ 官网公开）'],
    '**大分销 20%：找产品经理一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 分销价 + MOQ 1 + 付费样机；BDCOM / Edge-corE 不点名）' + ZA + '**',
    '分销 20%；P 池候选 ★（分销主体 ✔ 已进口中国同类 ✔ 对位 ✔ 坐实 ✔ 同区先例 ✔）；坐实。')
row('SC-382', 'other', 'Security Warehouse (Pty) Ltd（securitywarehouse.co.za；**官网 T&C：Reg 2003/015829/07；VAT 4600163721；118 Theuns Street, Cnr Theuns & Jakaranda, Hennopspark, Centurion 0172；+27 12 653 1005；info@securitywarehouse.co.za；创始人 / MD Pasco Lattuca（crunchbase）；101–250 人；电子安防分销 覆盖非洲**）；表内：CCTV 分销', 'ZA',
    'ZA · 1 次检索：securitywarehouse.co.za/support/terms-conditions/（Reg / VAT / 地址）+ crunchbase（MD / 规模）；2026-10-29', 'https://securitywarehouse.co.za/support/terms-conditions/',
    '2003/015829/07（Reg No.）/ VAT 4600163721', 'Active（官网 2025）', '2003', '(Pty) Ltd', '电子安防分销（森图里恩）', '118 Theuns Street, Hennopspark, Centurion 0172', '中型（101–250 人）',
    ['Pasco Lattuca — Founder & Managing Director'],
    '**安防分销 20%：点名 Pasco Lattuca 一页纸一次（STC-028GP $28 / STC-228GP $33 CCTV 配套 + MOQ 1 + 付费样机）' + ZA + '**',
    '分销 20%；P 池候选 ★（分销主体 ✔ 对位 ✔ 坐实 ✔ 决策人具名 ✔）；坐实。')
row('SC-622', 'other', 'Industrial Automation and Control (Pty) Ltd — IAC（iacontrol.co.za；**官网：Communica Building, 53 Landmarks Avenue, Samrand Business Park, Centurion；P.O. Box 2860, The Reeds 0158；+27 12 657 3600；info@iacontrol.co.za；Hirschmann / Belden / Lumberg / Korenix / Advantech / Mobotix 非洲分销（Communica 集团；域名 1998 起）**）；Reg No 未取；表内：工业网络分销', 'ZA',
    'ZA · 1 次检索：shop.iacontrol.co.za/pages/contact-us（法人 / 地址 / 电话）+ website.informer（品牌 / 域名 1998）；Reg No 未取；2026-10-29', 'https://shop.iacontrol.co.za/pages/contact-us',
    '未取（Reg No 未查）', '营业中（官网 2025）', '未取（域名 1998）', '(Pty) Ltd', '工业网络 / 自动化分销（森图里恩）', 'Communica Building, 53 Landmarks Avenue, Samrand Business Park, Centurion', '中型（集团成员）',
    ['（具名 KP 未取）'],
    '**工业分销 20%：一页纸一次（STI-280GE $46.6 / STI-288GPM $78.9 / STI-244DGGPM $121 作价位补充线 + MOQ 1；Hirschmann / Korenix 不点名）' + ZA + '**',
    '分销 20%；P 池候选 ○（工业分销主体 ✔ 对位 ✔）；部分坐实（Reg No 未取）。')
row('SC-644', 'other', 'Scoop Distribution (Pty) Ltd（scoop.co.za；**T&C：Company Registration 2001/007610/07；VAT 4830195584；注册办公 1A Harvest Close, Richmond Park, Richwood, Cape Town 7441；Midrand 分部 Unit 4, CDE Premium Park, 362 Roan Cres, Corporate Park North；+27 11 312 9414；Ubiquiti / MikroTik / Tenda / Linkbasic / Reyee / Zycoo / Fanvil 授权分销**）；表内：网络批发', 'ZA',
    'ZA · 1 次检索：scoop.co.za Terms_And_Conditions.pdf（Reg / VAT / 注册地址）+ yellosa（Midrand / 品牌）；2026-10-29', 'https://scoop.co.za/download/applications/Terms_And_Conditions.pdf',
    '2001/007610/07（Reg No.）/ VAT 4830195584', 'Active（T&C 2021 / 目录 2022）', '2001', '(Pty) Ltd', '网络 / 电信批发分销（开普敦 / 米德兰）', '1A Harvest Close, Richmond Park, Richwood, Cape Town 7441', '中型（双城）',
    ['（具名 KP 未取）'],
    '**批发分销 20%：一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 分销价 + MOQ 1 + 付费样机；Tenda / Reyee 不点名）' + ZA + '**',
    '分销 20%；P 池候选 ★（分销主体 ✔ 已进口中国同类 ✔ 对位 ✔ 坐实 ✔）；坐实。')
row('SC-1283', 'other', 'Reditron (Pty) Ltd（reditron.co.za；**信用申请表自报 registration number 2002/028391/07；9 Electron Street, Linbro Business Park, Sandton / Johannesburg 2090；+27 87 802 2288；CCTV 分销**）；表内：安防分销', 'ZA',
    'ZA · 1 次检索：reditron.co.za Credit-Application PDF（Reg No / 地址）+ cylex / firmania（地址 / 电话）；2026-10-29', 'https://reditron.co.za/wp-content/uploads/2024/10/Reditron-Credit-Application-2022_Editable.pdf',
    '2002/028391/07（Reg No.，自报）', 'Active（官网 2024）', '2002', '(Pty) Ltd', '电子安防分销（约翰内斯堡）', '9 Electron Street, Linbro Business Park, Sandton 2090', '中型',
    ['（具名 KP 未取）'],
    '**安防分销 20%：一页纸一次（STC-028GP $28 / STC-228GP $33 CCTV 配套 + MOQ 1 + 付费样机）' + ZA + '**',
    '分销 20%；P 池候选 ★（分销主体 ✔ 对位 ✔ 坐实 ✔）；坐实（自报注册号）。')
row('SC-1332', 'other', 'DBG Distribution（原 Uniterm Direct；dbg.co.za；**2002 起；JHB 10 Angus Crescent, Longmeadow Business Estate East, Modderfontein 1645；CPT Unit 12 & 13, Rivergate Park 2, 35 Columbus Crescent, Parklands 7441；DBN Unit 51 Micro Park, Cornubia；自有品牌 UltraLAN：PoE 交换机 / PoE 延长器 / 注入器 / 分离器 / 光纤 / 机柜 / Mini UPS；代理 Ubiquiti / Tenda / Fanvil / Optcore / Ajax / DTECH；服务 ISP / 安装商 / 经销商**）；Reg No 未取；表内：光纤分销（本职线）', 'ZA',
    'ZA · 1 次检索：dbg.co.za/about-us/（2002 / 更名 / 三城）+ /our-brands/（UltraLAN 自有品牌线）+ shop.dbg.co.za（分部地址）；Reg No 未取；2026-10-29', 'https://dbg.co.za/our-brands/',
    '未取（Reg No 未查）', '营业中（官网 2026）', '2002', '(Pty) Ltd', '网络 / 光纤分销 + 自有品牌 UltraLAN（约翰内斯堡）', '10 Angus Crescent, Longmeadow Business Estate East, Modderfontein 1645', '中型（三城分部）',
    ['（具名 KP 未取）'],
    '**自有品牌 UltraLAN PoE 交换机 = OEM 对象 → OEM 30%：一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 贴牌 UltraLAN + 中性包装 + MOQ 1；光纤 / SFP 走本职线）' + ZA + '**',
    'OEM 30%；P 池候选 ★（自有品牌 ✔ 分销网络 ✔ 对位 ✔）；部分坐实（Reg No 未取）；dayjob_fit（光纤线）。')
row('SC-1552', 'other', 'Chiisa Technologies Pty Ltd（chiisa.co.za / chiisa.com；**2015 创立；99A Genl Mauritz, Bendor Ext10, Polokwane 0699；015 298 2125 / 084 360 9412；support@chiisa.co.za；SMME IT 服务（自述）**）；Reg No 未取；表内：小 IT 服务商', 'ZA',
    'ZA · 1 次检索：chiisa.com/about-us/（2015 / 地址 / 邮箱）；LinkedIn 同名 Chisa Technologies（Bryanston 2005）不对应；2026-10-29', 'https://chiisa.com/about-us/',
    '未取（Reg No 未查）', '营业中（官网在线）', '2015', '(Pty) Ltd', 'IT 服务（波罗克瓦尼）', '99A Genl Mauritz, Bendor Ext10, Polokwane 0699', '微型（SMME）',
    ['（具名 KP 未取）'],
    '**微型 IT 服务 → 回 C 储备（来信再起则预付 100%）**' + ZA,
    '回 C（微型 SMME；部分坐实）。')

# ---------------- 澳 / 巴西 / 墨西哥 / 海湾 ----------------
row('SC-397', 'au', 'Alloy Computer Products (Australia) Pty. Ltd.（alloy.com.au；**ABN 41 006 507 473（buy.nsw.gov.au 供应商库）；制造商 + 增值分销；自有品牌 PoE 交换机 AS2008-P / AS2024-P / AS1008-P / AS1026-P、L3 Lite 管理型 AS5010-P / AS5128-F、MC GCR2000SC / AC1020SC；自述向英美澳新菲政府机构供光纤设备 15 年+**）；表内：澳洲自有品牌交换机 / MC', 'AU',
    'AU · 1 次检索：buy.nsw.gov.au/supplier/profile/103131（ABN）+ alloy.com.au/products/vendor/alloy/ + /alloy/（自有品牌线）；2026-10-29', 'https://buy.nsw.gov.au/supplier/profile/103131',
    '41 006 507 473（ABN）', 'Active（NSW 供应商库 / 官网）', '未取', 'Pty Ltd', '网络设备自有品牌 / 增值分销（墨尔本）', '未取（Victoria，官网未抄）', '中型（SME）',
    ['（具名 KP 未取）'],
    '**自有品牌 → OEM 30%：一页纸一次（STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM 贴牌 Alloy + 中性包装 + MOQ 1 + 付费样机）' + OT + '**',
    'OEM 30%；P 池候选 ★（自有品牌 ✔ 对位 ✔ 坐实 ✔）；坐实（ABN）。')
row('SC-1038', 'other', 'Teltex Tecnologia SA（teltex.com.br；**页脚 CNPJ 73.442.360/0001-17；33 年；Rua França Pinto 1089, Vila Mariana, São Paulo SP 04016-030；+55 11 3840-6400；comercial@teltex.com.br；2022 巴西前 5 大安防集成商（Informática Hoje Top 200 / FGV 审计）；2025 年鉴前 10 盈利；葡萄牙 Torres Vedras / 美国 Hallandale Beach 办事处；100% 自有团队全国项目**）；表内：大集成商', 'BR',
    'BR · 1 次检索：teltex.com.br/en/（CNPJ / 排名 / 海外办）+ /homepage-portugues/（地址 / 电话 / 邮箱）；2026-10-29', 'https://teltex.com.br/en/',
    '73.442.360/0001-17（CNPJ）', 'Ativa（官网 2026）', '1993（33 年）', 'S.A.', '电子安防 / 技术基建集成（圣保罗）', 'Rua França Pinto 1089, Vila Mariana, São Paulo SP 04016-030', '大型（巴西前 5 安防集成）',
    ['（具名 KP 未取；comercial@ 官网公开）'],
    '**大集成商 25%（长线）：找采购 / 工程部一页纸一次（STC-2224GP $86 / STC-4424GCPM $165 / STI-288GPM $78.9 项目价 + 付费样机；DAP 买方清关）' + OT + '**',
    '集成 25%；P 池候选 ★ 长线（大集成 ✔ 对位 ✔ 坐实 ✔）；坐实（CNPJ）。')
row('SC-1379', 'other', 'Parks S.A. Comunicações Digitais（parks.com.br；**CNPJ 92.679.331/0001-18；1972-08-01 成立；S.A. fechada；Av. Cruzeiro 530, Distrito Industrial, Cachoeirinha RS 94930-615；CNAE 2631-1/00 通信传输设备制造；Ativa**）；表内：巴西自有品牌电信设备制造（GPON / 交换机；本职线重叠）', 'BR',
    'BR · 1 次检索：econodata（CNPJ / CNAE / 成立）+ informecadastral / speedio（地址 / 状态）；2026-10-29', 'https://www.econodata.com.br/consulta-empresa/92679331000118-parks-sa-comunicacoes-digitais',
    '92.679.331/0001-18（CNPJ）', 'Ativa（Receita 2026）', '1972-08-01', 'S.A.（fechada）', '通信传输设备制造（南大河州）', 'Av. Cruzeiro 530, Distrito Industrial, Cachoeirinha RS 94930-615', '大型（53 年制造商）',
    ['（具名 KP 未取）'],
    '**自有品牌制造商 → OEM 30%：找硬件采购一页纸一次（STC-2224GP / STC-4424GCPM / STI-288GPM 贴牌 Parks + 中性包装 + MOQ 1；GPON / 光模块走本职线）' + OT + '**',
    'OEM 30%；P 池候选 ★（自有品牌 ✔ 制造商 ✔ 对位 ✔ 坐实 ✔）；坐实（CNPJ）；dayjob_fit。')
row('SC-1117', 'other', 'SYSCOM = Sistemas y Servicios de Comunicación, S.A. de C.V.（syscom.mx；**Chihuahua：Av. 20 de Noviembre 805, Col. Centro 31000 / Calle Sexta 3407, Col. Santa Rosa 31050；501–1000 人（crunchbase）；电信 + 电子安防批发（comercio al por mayor de equipo de telecomunicaciones）；RFC 未取**）；表内：墨西哥最大电信 / 安防分销之一', 'MX',
    'MX · 1 次检索：crunchbase（法人名 / 规模）+ mexicopymes / directorioempresarialmexico（razón social / 地址 / 行业）；RFC 未取；2026-10-29', 'https://www.crunchbase.com/organization/syscom-73a0',
    '未取（RFC 未查）', '营业中（目录 2020 / crunchbase 2026）', '未取', 'S.A. de C.V.', '电信 / 安防批发分销（奇瓦瓦）', 'Av. 20 de Noviembre 805, Col. Centro, Chihuahua 31000', '巨型（501–1000 人）',
    ['（具名 KP 未取）'],
    '**巨头分销 20%（长线）：找网络产品线经理一页纸一次（STC-028GP / STC-228GP / STC-2224GP 分销价 + MOQ 1 + 付费样机；DAP 买方清关）' + OT + '**',
    '分销 20%；P 池候选 ★ 长线（巨型分销 ✔ 对位 ✔ 坐实（法人名 + 地址）✔；巨头难进 → 长线）；坐实。')
row('SC-577', 'other', 'Leap Networks（leap-networks.ae；**2012 成立；Guardian Office Tower, Al Murror Road, Dhafeer Street 407, Abu Dhabi 37855（prospeo）；11–20 人；CEO Muhammad Ashfaq（= 表内具名 KP muhammad.ashfaq@）；ISO 9001 / 14001 / 45001；油气 / 石化 / 矿业 / 交通电信系统集成（DWDM / TETRA / SDH / CCTV / PAGA / 门禁）；姊妹公司 Leap Networks Arabia（沙特，CEO Asif Imam）**）；执照号未取；表内国别沙特（两地皆有）', 'AE',
    'AE · 1 次检索（补查）：leap-networks.ae/about-us/（2012 / ISO / 行业）+ prospeo（地址 / CEO / 规模）+ theorg（沙特姊妹公司）；首查误中同名 Leap Technologies 不采；2026-10-29', 'https://www.leap-networks.ae/about-us/',
    '未取（执照号未查）', '营业中（官网 2025）', '2012', 'LLC（待核）', '油气电信系统集成（阿布扎比 / 沙特）', 'Guardian Office Tower, Al Murror Road, Dhafeer Street 407, Abu Dhabi 37855', '小型（11–20 人；双国）',
    ['Muhammad Ashfaq — Chief Executive Officer（表内具名邮箱）', 'Tarek Bary — （表内具名邮箱）', 'Asif Imam — CEO, Leap Networks Arabia'],
    '**油气工业集成 25%：点名 Muhammad Ashfaq 一页纸一次（STI-288GPM $78.9 / STI-244DGGPM $121 / STI-488DGGPM $147 工业线 + 付费样机；DWDM / SDH 走本职线）' + OT + '**',
    '集成 25%；P 池候选 ○（决策人具名 ✔ 工业对位 ✔）；部分坐实（执照未取）；dayjob_fit；表内沙特 ↔ 总部阿联酋 备注。')
row('SC-1248', 'other', 'Avensia Group — Avensia Tech Solution（avensiauae.com；**Al Qusais, Damascus Street, Dubai；P.O. Box 87334；TEL +9714-2636886 / FAX 2636883；General Trading +971 509962388；IT & Technical +971 526456607；info@avensiauae.com；综合贸易 + IT + 技术服务 + 设施管理；交换机 / AP 页「Get in Touch for Bulk Orders」**）；执照未取；表内：想换供应商（真意向），WA 路径', 'AE',
    'AE · 1 次检索：avensiauae.com/it-products/network-switches-avensia-group-uae/ + wifi 页（地址 / 电话 / 业务）+ topfirms（Al Qusais）；执照未取；2026-10-29', 'https://www.avensiauae.com/it-products/network-switches-avensia-group-uae/',
    '未取（执照未查）', '营业中（官网 2021 / 目录）', '未取', 'LLC（待核）', '综合贸易 / IT（迪拜）', 'Al Qusais, Damascus Street, Dubai, P.O. Box 87334', '小型（综合贸易）',
    ['（具名 KP 未取；WA 路径在表）'],
    '**真意向（想换供应商）→ 贸易 / 集成 25% + 预付 100%：WA + 邮件一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 + MOQ 1 + 付费样机；DAP 买方清关）' + OT + '**',
    '集成 25% + 预付 100%；P 池候选 ○（真意向 ✔ WA ✔ 对位 ✔）；部分坐实（执照未取）。')

print('b130_c done')
