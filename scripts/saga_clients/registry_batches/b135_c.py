# -*- coding: utf-8 -*-
"""第 135 批（T29-U118g，2026-10-29）—— **C 池三闸 · 闸 2 第十二批**：闸 1 第 36–46 批候选余 **印度 6 / 越南 9 = 15 户** 查底数（闸 1 候选至此归零）。
路径：IN → zaubacorp / thecompanycheck（CIN / 董事 / 成立）、官网页脚（注册地址）、IndiaMART（GST / 规模）、rocketreach / crunchbase（KP / 规模）；VN → masothue / trangvang / yellowpages.vn / 官网「Giới thiệu」页脚（MST / 地址 / 代表 / 成立年 / 人数）。
每户 1 查、depth 1；1 查未中或仅同名壳即停 = 未坐实（url=''），下轮再查 1 次（官网页脚 MST / CIN）。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 135
F = '2026-10-29'
IN = '— 印度常规：英文稿、20 / 25 / 30 + T/T 50/50（微型预付 100%）+ FOB 深圳 / CIF 孟买·金奈·德里，买方清关（BIS 由买方自理需如实说）；周二 / 周四 11–13 IST'
VN = '— 越南常规：英文 / 越南语稿、20 / 25 / 30 + T/T 50/50（微型预付 100%）+ FOB 深圳 / DAP 河内·胡志明，买方清关；Zalo / 微信可用；周二 / 周四 10–12 ICT'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 印度 ----------------
row('SC-1657', 'in', 'San Telequip Private Limited（santelequip.com；**CIN U32202PN1992PTC065720；ROC Pune；1992-03-04 成立；NIC 3220 通信设备制造；实缴 ₹1.11 M；约 32 人；董事 Leena Anant Gokhale / Nitin Shreekant Joshi / Hemant Laxman Joshi（增补）；最近年报 2023-03-31**）；表内：Chetan Kamdi，gmail；Profibus 连接器商，主动问 5 / 8 电口价格', 'IN',
    'IN · 1 次检索：zaubacorp（CIN / 董事 / NIC）+ thecompanycheck（成立 / 实缴 / 人数 / 年报）；2026-10-29', 'https://www.zaubacorp.com/SAN-TELEQUIP-PRIVATE-LIMITED-U32202PN1992PTC065720',
    'U32202PN1992PTC065720（CIN）', 'Active（年报 2023-03-31）', '1992-03-04', 'Private Limited', '工业通信 / 现场总线连接器制造与分销（浦那）', 'Pune, Maharashtra（注册地址见 MCA）', '小型（≈ 32 人）',
    ['Leena Anant Gokhale — Director', 'Nitin Shreekant Joshi — Director', 'Chetan Kamdi — 表内联系人'],
    '**印度 · 工业自动化渠道 25%：回 Chetan 引用其 5 / 8 电口问价，报 STI-054GP（4 PoE + 1 GE）/ STC-028GP $28 / STI-280GE $46.6 + MOQ 1 + 付费样机' + IN + '**',
    '集成 / 渠道 25%；P 池候选 ○（印度先例 ✔ 工业渠道对位 ✔ 主动问价 ✔ 坐实 ✔；1992 老牌 32 人）；坐实（CIN）。')
row('SC-1793', 'in', 'Axis Solutions Pvt Ltd / Axis Solutions Limited（axisindia.in；**Registered Office 324, Road No. 5, Kathwada GIDC, Ahmedabad 382430, Gujarat；+91 99099 06354；info@axisindia.in；LEONTON（台湾工业以太网）印度授权分销商，官网挂 Leonton 工业交换机全系**）；CIN 未取；表内：Lavesh Savale Sales Engineer，gmail；2022-12 问 website', 'IN',
    'IN · 1 次检索：axisindia.in 产品页页脚（法人名 / 注册地址 / 电话）+ Leonton 数据表（授权分销）；CIN 未取；2026-10-29', 'https://axisindia.in/products/partners/automation/leonton/industrial-ethernet-switch/unmanaged-switch/16-port-industrial-gigabit-ethernet-switch/',
    '未取（CIN 未查；官网页脚坐实法人名 + 地址）', '营业中（官网 2022–2026）', '未取', 'Pvt Ltd（官网另写 Limited，待核）', '工业自动化分销（艾哈迈达巴德；Leonton 授权）', '324, Road No. 5, Kathwada GIDC, Ahmedabad 382430, Gujarat', '小型',
    ['Lavesh Savale — Sales Engineer（表内）'],
    '**印度 · 工业分销 20%：info@ + Lavesh 一页纸对标 Leonton（STI-280GE $46.6 / STI-288GPM $78.9 / STI-244DGGPM $121 + MOQ 1 + 付费样机）' + IN + '**',
    '分销 20%；P 池候选 ○（印度先例 ✔ 台湾工业品牌分销 = 有进口经验 ✔ 对位 ✔）；部分坐实（CIN 未取）。')
row('SC-1916', 'in', 'VIgIL — M/s Udaya Security Vision（vigilworld.com；**VIgIL Tower, Mahatab Road, Cuttack, Odisha；vigil_usv@yahoo.co.in；奥里萨邦 CCTV 自有品牌 VIgIL「manufacturer – supplier – service provider」22 年**）；GST / 法人形式未取；表内：PoE switch 用 hisource 的 ✔', 'IN',
    'IN · 1 次检索：vigilworld.com/contact-us（法人名 / 地址 / 邮箱 / 业务）；GST 未取；2026-10-29', 'https://vigilworld.com/contact-us/',
    '未取（GST 未查；官网坐实商号 + 地址）', '营业中（官网）', '未取（约 2000 年「22 年前」）', '未取（疑 Proprietorship / Partnership）', 'CCTV 自有品牌制造 + 供应 + 服务（卡塔克）', 'VIgIL Tower, Mahatab Road, Cuttack, Odisha', '小型',
    ['（具名 KP 未取；官网 Contact 仅 yahoo 邮箱）'],
    '**印度 · 自有品牌安防商 OEM 30%：yahoo 邮箱一页纸一次（STC-028GP $28 / STC-228GP $33 中性包装 + 贴 VIgIL 牌 + MOQ 1；hisource 现供 → 推 SmartByte 管理线差异）' + IN + '**',
    'OEM 30%；P 池候选 ○（印度先例 ✔ 自有品牌 ✔ 已用中国 PoE ✔；仅 yahoo 邮箱）；部分坐实（GST 未取）。')
row('SC-2154', 'in', 'RoundRobin Tech Services Pvt. Ltd.（roundrobintech.com；**孟买总部；网络安全产品增值分销商（VAD），印度 + SAARC 14 年+；11–50 人；Pradeep Patel — Regional Manager（艾哈迈达巴德）；另 Rajesh Makwana Regional Pre-Sales、Dhagash Thaker Product Manager**）；CIN 未取；表内：Pradeep「分销商，有需求会说」真回；Bakhtavar Usmani', 'IN',
    'IN · 1 次检索：crunchbase（业务 / 规模 / 孟买）+ rocketreach（Pradeep Patel 职务 / 团队）；CIN 未取；2026-10-29', 'https://www.crunchbase.com/organization/roundrobin-tech-services',
    '未取（CIN 未查；目录坐实法人名）', '营业中（目录 2026）', '未取（≈ 2010）', 'Pvt. Ltd.', '网络安全 / 网络基础设施增值分销（孟买）', 'Mumbai, Maharashtra', '小型（11–50 人）',
    ['Pradeep Patel — Regional Manager（表内真回）', 'Dhagash Thaker — Product Manager'],
    '**印度 · 增值分销 20%：回 Pradeep 引用其「有需求会说」，一页纸价格锚（STC-028GP $28 / STC-2224GP $86 / STC-4424GCPM $165）+ 抄 Product Manager' + IN + '**',
    '分销 20%；P 池候选 ○（印度先例 ✔ 分销对位 ✔ 真回 ✔ 决策链具名 ✔）；部分坐实（CIN 未取）。')
row('SC-2208', 'in', 'Hanutech Solution（hanutechsolution.com / .co.in；**Proprietorship；GST 07AXLPM4765G1Z3（2018-06-28 登记）；CEO / 东主 Mahinder；≤ 10 人；年营业额 ₹1.5–5 Cr；B-16/1 Vijay Vihar Phase-2, Rohini, Delhi 110085（IndiaMART 另列 B 73）；hanutechsolution2018@gmail.com；+91 89204 13407；光纤 / FTTH / CCTV / 光收发器店，Amazon / Flipkart 卖家；关联 RAMEX（Bhiwadi）**）；表内：丰润达商业 PoE ✔', 'IN',
    'IN · 1 次检索：IndiaMART aboutus（GST / 东主 / 规模 / 营业额）+ hanutechsolution.co.in 页脚（地址 / 邮箱 / 电话）；2026-10-29', 'https://www.indiamart.com/hanutech-solution/aboutus.html',
    '07AXLPM4765G1Z3（GST）', '营业中（官网 + IndiaMART）', '2018-06-28（GST）', 'Proprietorship', 'IT / 网络 / 光纤 / CCTV 零售 + 电商（德里 Rohini）', 'B-16/1 Vijay Vihar Phase-2, Rohini, Delhi 110085', '微型（≤ 10 人）',
    ['Mahinder — Proprietor / CEO'],
    '**印度 · 电商零售 20% 预付 100%：gmail 一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-110XGE $65 + MOQ 1）' + IN + '**',
    '零售 20%；P 池候选 △ 预付 100%（印度先例 ✔ 中国品牌 ✔ 坐实 ✔ 但独资微型 + 电商卖家）；坐实（GST）。')
row('SC-1177', 'in', 'Projexon（projexon.com；表内 CCTV 为主，WA 问 L2 / L3 交换机；R. Vignesh Director；**1 次检索未中：zaubacorp 两家同名 Projexon Engineering（中央邦 2017 / 德里 2021，董事 Pandey / Tripathi / Devi / Kumar）均非 Vignesh 的 CCTV 公司 = 同名壳**）', 'IN',
    'IN · 1 次检索：zaubacorp「Projexon」仅同名工程公司，未指向 projexon.com；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', 'CCTV / 网络集成（印度）', '未取', '未取',
    ['R. Vignesh — Director（表内）'],
    '**印度 · 待坐实：WA 问 Vignesh 法人全名 / GST / 城市后一页纸（STC-2224GP $86 / STC-4424GCPM $165）' + IN + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查（官网页脚 GST）；印度先例 ✔ WA 可达 ✔ 决策人 ✔。')

# ---------------- 越南 ----------------
row('SC-1586', 'other', 'CÔNG TY TNHH GIẢI PHÁP VIỄN THÔNG THIÊN TÂN（vienthongthientan.com / holinktech.com / chuyendoiquang.com；**MST 0105224649；Số nhà 45, Ngõ 50, Phố Mễ Trì Thượng, Phường Từ Liêm, Hà Nội；Đang hoạt động；Công ty TNHH ngoài NN；主业 Bán buôn thiết bị và linh kiện điện tử, viễn thông（masothue 2025-12-24 更新）**）；表内：VC 很多国内牌子 + MC G-net + 工业 FS / 商业 PoE；「有他们业务微信」；gmail', 'VN',
    'VN · 1 次检索：masothue（MST / 地址 / 状态 / 主业）+ tratencongty；2026-10-29', 'https://masothue.com/0105224649-cong-ty-tnhh-giai-phap-vien-thong-thien-tan',
    '0105224649（MST）', 'Đang hoạt động（2025-12）', '未取（MST 0105 段 ≈ 2011）', 'Công ty TNHH', '电子 / 电信设备批发（河内 Từ Liêm）', 'Số nhà 45, Ngõ 50, Phố Mễ Trì Thượng, Phường Từ Liêm, Hà Nội', '小型',
    ['（法定代表人未取；表内有业务微信）'],
    '**越南 · 分销 20%：业务微信 + gmail 一页纸（STC-028GP $28 / STC-228GP $33 / STI-280GE $46.6 + MOQ 1 + 付费样机）；VC 本职线并行' + VN + '**',
    '分销 20%；P 池候选 ○（越南先例 ✔ 中国品牌 ✔ 对位 ✔ 微信可达 ✔ 坐实 ✔）；坐实（MST）。')
row('SC-1605', 'other', 'CÔNG TY TNHH THƯƠNG MẠI VÀ PHÁT TRIỂN CÔNG NGHỆ TÂN TIẾN（mangcongnghiep.vn；**MST 0110079059；Nhà 6A, ngách 207/28 phố Bùi Xương Trạch, Tổ 14, Phường Khương Đình, Quận Thanh Xuân, Hà Nội；Hotline 097 787 0110；tantien2tech@gmail.com；3onedata（三旺）工业交换机越南经销（官网页脚自署）**）；表内：工业交换机 三旺 ✔', 'VN',
    'VN · 1 次检索：mangcongnghiep.vn 产品页页脚（法人名 / MST / 地址 / 热线 / 邮箱 / 三旺经销）；2026-10-29', 'https://mangcongnghiep.vn/switch-mang-cong-nghiep-5-port-4-rj45-1-cong-quang-3onedata-ies215-1f/',
    '0110079059（MST）', '营业中（官网 2022–）', '未取（MST 0110 段 ≈ 2022）', 'Công ty TNHH', '工业网络 / 电信设备贸易（河内 Thanh Xuân）', 'Nhà 6A, ngách 207/28 phố Bùi Xương Trạch, Khương Đình, Thanh Xuân, Hà Nội', '微型',
    ['（法定代表人未取）'],
    '**越南 · 工业经销 20%：gmail 一页纸对标三旺（STI-280GE $46.6 / STI-288GPM $78.9 / STI-054GP + MOQ 1 + 付费样机）' + VN + '**',
    '分销 20%；P 池候选 ○（越南先例 ✔ 三旺经销 = 对位 + 进口经验 ✔ 坐实 ✔；2022 新公司微型 → 首单预付 100%）；坐实（MST 官网页脚）。')
row('SC-1644', 'other', 'Công Ty TNHH Viễn Thông Hoàng Thạch（vienthonghoangthach.com；**MST 0316813026；425 Cộng Hòa, Phường 15, Quận Tân Bình, TP.HCM；2021 成立；5–10 人；0972 742 245；vienthonghoangthach@gmail.com；面向安装工的 CCTV 批零（Hikvision / Dahua / Kbvision / EZVIZ）；yellowpages.vn 2023-08 核验**）；表内：switch 有 utepo 的 ✔', 'VN',
    'VN · 1 次检索：yellowpages.vn（MST / 地址 / 电话 / 邮箱 / 成立 / 人数）+ jobsgo / topvietnam；2026-10-29', 'https://www.yellowpages.vn/lgs/1187845410/cong-ty-tnhh-vien-thong-hoang-thach.html',
    '0316813026（MST）', '营业中（目录 2023）', '2021', 'Công ty TNHH', 'CCTV 批零（胡志明市 Tân Bình）', '425 Cộng Hòa, Phường 15, Quận Tân Bình, TP.HCM', '微型（5–10 人）',
    ['（法定代表人未取）'],
    '**越南 · CCTV 批零 20% 预付 100%：gmail 一页纸一次（STC-028GP $28 / STC-228GP $33 + MOQ 1）' + VN + '**',
    '零售 / 分销 20%；P 池候选 △ 预付 100%（越南先例 ✔ 中国品牌 utepo ✔ 坐实 ✔ 但 2021 微型 CCTV 店）；坐实（MST）。')
row('SC-1867', 'other', 'CÔNG TY CỔ PHẦN MẠNG VIỄN THÔNG 3 MIỀN（vienthonghanoi.vn；**MST / GPKD 0109201032（2020-05-29 河内计划投资局）；VPGD Chung Cư 9 Tầng Cầu Bươu, Tả Thanh Oai, Thanh Trì, Hà Nội；0914 180 199；inbox.vienthonghanoi@gmail.com；光 / 网络 / 电信设备分销 + 施工 5 年+，自称服务 1 万客户（官网「Giới thiệu」2026-06）**）；表内：工业 FS 主要是中科德能的 ✔；8 推 0 回', 'VN',
    'VN · 1 次检索：vienthonghanoi.vn/gioi-thieu（法人名 / MST / 成立 / 地址 / 电话 / 邮箱 / 业务）；2026-10-29', 'https://vienthonghanoi.vn/gioi-thieu/',
    '0109201032（MST）', '营业中（官网 2026-06）', '2020-05-29', 'Công ty Cổ phần', '网络 / 光 / 电信设备分销 + 施工（河内 Thanh Trì）', 'Chung Cư 9 Tầng Cầu Bươu, Tả Thanh Oai, Thanh Trì, Hà Nội', '小型',
    ['（法定代表人未取）'],
    '**越南 · 分销 20%：换稿一页纸一次（零回应 → 坐实后仅一次；STI-280GE $46.6 / STC-028GP $28 对标中科德能）' + VN + '**',
    '分销 20%；P 池候选 ○（越南先例 ✔ 中国工业品牌 ✔ 对位 ✔ 坐实 ✔；8 推 0 回 → 仅一次）；坐实（MST 官网自署）。')
row('SC-1979', 'other', 'Công Ty TNHH Công Nghệ Mạng Viễn Thông Thanh Bình（switchquang.com / switchquang.com.vn；**MST 0108196975；Số 37, ngõ 130, đường Nguyễn Khoái, Phường Thanh Lương, Quận Hai Bà Trưng, Hà Nội；2018 成立；5–10 人；0856 888 666；info@switchquang.com；进口分销 3onedata / Huahuan / Optone / Baudcom / Allied Telesis / DCN / Advantech 等，客户 Mobifone / Viettel / Vinaphone / EVN**）；表内：ONV、三旺 ✔；全线；8 推 0 回', 'VN',
    'VN · 1 次检索：trangvangtructuyen（MST / 地址 / 电话 / 邮箱 / 品牌 / 客户）+ niengiamtrangvang（人数）；2026-10-29', 'https://trangvangtructuyen.vn/cong-ty-tnhh-cong-nghe-mang-vien-thong-thanh-binh.html',
    '0108196975（MST）', '营业中（目录 2023）', '2018', 'Công ty TNHH', '电信 / 光 / 工业网络设备进口分销（河内 Hai Bà Trưng）', 'Số 37, ngõ 130, đường Nguyễn Khoái, Thanh Lương, Hai Bà Trưng, Hà Nội', '微型（5–10 人）',
    ['（法定代表人未取）'],
    '**越南 · 进口分销 20%：info@switchquang.com 换稿一页纸一次（全线：STI-280GE $46.6 / STC-028GP $28 / STC-2224GP $86 + MOQ 1）；VC 本职线并行' + VN + '**',
    '分销 20%；P 池候选 ○（越南先例 ✔ 多品牌进口 = 进口经验 ✔ 全线对位 ✔ 坐实 ✔；8 推 0 回 → 仅一次）；坐实（MST）。')
row('SC-1606', 'other', 'Mạng Viễn Thông（mangvienthong.com.vn；联系 inbox.thanhcong@gmail.com；**1 次检索未中：仅命中 mangvienthong.vn = CÔNG TY TNHH THƯƠNG MẠI VÀ KỸ THUẬT CÔNG NGHỆ MỚI（河内 Hoàng Mai）—— 域名不同（.vn ≠ .com.vn），不能认定同一主体**）', 'VN',
    'VN · 1 次检索：「mangvienthong.com.vn」仅命中 mangvienthong.vn 另一主体；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', 'PoE / FS / MC / VC / 工业交换机贸易（越南）', '未取', '未取',
    [],
    '**越南 · 待坐实：官网页脚取 MST 后一页纸' + VN + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查（官网页脚 MST）；中科德能 ✔ 对位 ✔。')
row('SC-1638', 'other', 'Thuận An（thuananvn.com.vn；thuanan.sales1@gmail.com；工业交换机 optone ✔；**1 次检索未中：「Công ty TNHH Thuận An」为通名，命中河内 2002（已停）/ 岘港 / 河南省三家均无法与域名对应**）', 'VN',
    'VN · 1 次检索：masothue / dailychukyso「Thuận An」仅同名壳；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', '工业交换机贸易（越南）', '未取', '未取',
    [],
    '**越南 · 待坐实：官网页脚取 MST 后一页纸（STI-280GE / STI-288GPM 对标 optone）' + VN + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查（官网页脚 MST）；optone ✔ 工业对位 ✔。')
row('SC-1983', 'other', 'Việt Long Telecom（vietlongtelecom.com；gmail；商业 PoE 用 G-net / hasivo ✔；**1 次检索未中：「Công ty TNHH Việt Long」通名，命中同奈 2001 / 清化 / 河内 1998 等均非电信设备商**）', 'VN',
    'VN · 1 次检索：thuvienphapluat / dulieuphapluat「Việt Long」仅同名壳；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', '商业 PoE 交换机贸易（越南）', '未取', '未取',
    [],
    '**越南 · 待坐实：官网页脚取 MST 后换稿一页纸' + VN + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查（官网页脚 MST）；8 推 0 回。')
row('SC-2504', 'other', 'Tùng Lâm Technology Technical Co., Ltd.（表内；2026-03-19 阿里询盘「分销商寻求合作」；电话 0969 396 686 / 0858 344 388；**1 次检索未中：「Công ty TNHH Tùng Lâm」命中 1994 乙醇制造 / 巴维等同名壳，均非技术公司**）', 'VN',
    'VN · 1 次检索：masothue / dulieuphapluat「Tùng Lâm」仅同名壳；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', '网络设备分销意向（越南）', '未取', '未取',
    [],
    '**越南 · 待坐实：阿里后台 / 电话要邮箱 + 法人全名（Kỹ thuật Công nghệ Tùng Lâm）后一页纸' + VN + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查；分销意向新鲜（2026-03）✔ 电话 / 阿里后台可达 ✔。')

print('b135_c done')
