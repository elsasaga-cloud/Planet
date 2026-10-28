#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 114 批（T29-U107，公司底数第三十二轮 · 俄罗斯 B 池收尾 8 户 + 印度 B 池第 1 轮前 32 户 = 40 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 事实 补写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=114 行）。
结构同 batch113_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：B BIG · 加厚一次 9（SB-914 MRO-TEK Realty → UMIYA BUILDCON / 拟更名 MRO-TEK Networks L28112KA1984PLC005873 BSE 上市 OEM 贴标 30% / SB-684 Technics Infosolutions U72900DL2013PTC252728 Advantech Premier 250 台询价 分销 20% / SB-305 Bits and Byte IT Consulting U72900KA2015PTC145953 ≈57 人 集成 25% / SB-486 NextGen Automation U31200WB2002PTC094683 ≈75 人 集成 25% / SB-641 Apollo Infoways（WatchDog）U72900DL2014PTC264342 贴标 30%（Q-33 丰润达口径）/ SB-655 DIGISOL Systems Smartlink 100% 子公司 贴标 30%（Q-33 HRUI 口径；CIN 未取）/ SB-857 AirPro Technology India U72900RJ2014PLC045127 SME IPO 贴标 30% / SB-678 Quantum Networks 工业子线 贴标 30%（CIN 未取）/ SB-1138 DevRay U62013UP2024PTC204532 + MapleCloud U72900DL2018PTC338066 MD 具名追问 CENTEC L3 → 升 A 候选）；
加厚一次 2（SB-652 Comxus 工业 OEM 贴标 30% CIN 未取 / SB-304 AADONA Communication U72900CT2018PTC008600 贴标 30%）；
加厚 small 一次 3（SB-060 ООО «Баргас» 7716715348 业主 Гречкин = KP 曾回 interested（待 RU 路径）/ SB-308 Alcon Wireless U64200OR2010PTC011564 董事 Baral = KP 贴标 30% / SB-111 Nivox Technologies 29AAIFN5171H1ZZ Lantech 分销 分销 20%）；
一页纸一次 · 有回声再加厚 11（SB-562 АлтВижен 法人未取（待 RU 路径）/ SB-343 Zekko Tech U74999MH2016PTC285972 4 人 / SB-169 AGS Plus / Xexagon Hi-Tech U28299GJ2025PTC160203 身份未清 / SB-954 NETSTAR = Infonet Technologies 24AAGFI3821H1ZN 反向 PoE 不做 / SB-044 Win-Tech Alliance 香港法人 2.5G CKD 待 2.5G 口径 / SB-802 MSPL Limited U13100MH1961PLC012160 矿业终端 / SB-447 Automation Systems & Solution 07AOCPK7395A1Z0 个体例外 工业专营 / SB-306 Digital Systems 0 查 / SB-341 Smart Security Systems 0 查 / SB-632 Grypen Technologies CIN 未取）；
不动 15（SB-597 查无实体 / SB-619 JMDV 远东微型安装 / SB-623 ООО «ЭЛПРО» 6732103213 电加热元件 非目标 / SB-627 ИП Дроков 315615400000259 个体 / SB-895 ООО «ВИЛКОМ ХОЛДИНГ» 7710370947 破产观察 2026-02 / SB-320 个人 0 查 / SB-607 Jayani Technologies LLP AAA-6913 光模块 + 实质婉拒 / SB-064 Amity Technologies 军规加固 守界 + 同行 / SB-072 TECHNOSYS 27AWZPS2792Q2ZY 个体 <₹40 lakh / SB-1104 Agility Elektrotekniks U31908UP2014PTC066111 KP Atul Tiwari 已离职 / SB-1113 Fastball 07AJJPR5445G1ZX 个体 gg / SB-357 域名错配 需求 ONU / SB-630 Core IT Solutions 同名 Strike Off 身份不清 KP 退信 / SB-045 未坐实 站点占位 / SB-194 未坐实 站点失效 / SB-1105 个人 0 查）；
坐实 25 / 部分坐实 8（SB-619 / 562 / 652 / 678 / 655 / 169 / 044 / 632）/ 未坐实 7（SB-597 / 320 / 357 / 630 / 045 / 1105 / 194 / 306 / 341 中 306 / 341 / 1105 / 320 为 0 查）；
KP 坐实 = 老板 / 董事 / MD 本人 9（SB-060 Гречкин / SB-304 Pinaki Chatterjee / SB-305 Ramachandra Raju / SB-308 Pratap Kumar Baral / SB-607 Vijay Gupta / SB-641 Ravi Prakash / SB-857 Deepak Jain / SB-111 Hemanth Kumar / SB-1138 Yogendra Kumar Rajput）；KP 更正 2（SB-684「Prakash」→ Om (O.P.) Sharma；SB-1104 Atul Tiwari 已离职 → Essen Deinki）；
法定名补全 / 更正 24；country_fix 0（RU 8 户 iso 均 RU；IN 32 户 iso 均 IN；SB-044 法人在香港、操盘在孟买 → iso 保留 IN）。RU 8 户稿件一律「预付款 + 待 Simon 定 RU 收款 / 物流路径」；IN 32 户常规 T/T 预付 + FOB 深圳，不受限。
旁线索（≠ 目标，另立户评估）：Smartlink Holdings Ltd（SB-655 上市母公司）；WIS Networks Digital Technologies India Pvt Ltd U72900OR2017PTC027046（SB-308 关联）；Iris Global Services（SB-1138 全国分销商）；Xexagon Solutions Pvt Ltd U72900MP2019PTC048356（≠ SB-169）；Comus Electronics & Technologies India U32109TN2004PTC053620（≠ SB-652）；Netstar Technologies Pvt Ltd 德里 U30007DL1997PTC087232（≠ SB-954）；Technosys Software & Networking Solutions Pvt Ltd U72900MH2020PTC351625（≠ SB-072）；Essen Deinki（SB-1104 前 KP 现东家）。
Simon 待决（累计见 PR-02-53 追记）：RU 收款 / 物流路径（RU 累计 44 户 + BY 4 户压着；本批 SB-060 / 562 两户待发）；升 A 候选 SB-1138（回信即升）+ SB-914 / 684 / 305 / 486 / 641 / 655 / 857；2.5G 型号口径（SB-044 + SB-263 同一待办）；Q-33 HRUI / 丰润达口径确认（本批 SB-641 / 655 按「只推 Marvell 管理 / 工业线」起草）。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 114 批 官方登记核实 2026-10-28）'
RU = '— 稿件一律「预付款」，待 Simon 定 RU 收款 / 物流路径后再发'
UPD = {
    # ---------- 第 1/3 RU 8 + IN 6 ----------
    'SB-597': {'facts': {'legal_name': '未坐实（plus-nn.ru 域名无站点；yandex 邮箱；1 查无法人 / 品牌线索）', 'founded': '未取' + TAG,
                         'other': '第 114 批：查无实体 + 站点失效 + 23 封 0 打开 → **不动（B 保留）**' + RU + TAG}},
    'SB-619': {'facts': {'legal_name': 'JMDV（jmdv.ru；г. Уссурийск, ул. Льва Толстого, 15А, оф. 131；分店 Спасск-Дальний / Хабаровск；法人 / ИНН 未取）', 'founded': '未取' + TAG,
                         'other': '第 114 批：远东 CCTV 微型门店 + 安装、法人未取、0 打开 → **不动（B 保留）**；Q-33 丰润达口径若有回声只推 Marvell 管理 / 工业线' + RU + TAG}},
    'SB-623': [{'add_kp': {'name': 'Тамилин Андрей Леонидович', 'role': 'Генеральный директор ООО «ЭЛПРО»（spark）— 非目标行业，不动' + TAG, 'email': '', 'source': 'http://www.spark-interfax.ru/smolenskaya-oblast-smolensk/ooo-elpro-inn-6732103213-ogrn-1156733004284-fbafa7c5a275492a9403f62b6ea5648a'}},
               {'facts': {'legal_name': 'ООО «ЭЛПРО»（ИНН 6732103213；ОГРН 1156733004284；214019 Смоленск, ул. Крупской, д. 66, оф. 1；2015）', 'founded': '2015' + TAG,
                          'other': '第 114 批：主业电加热元件（ТЭН）制造 + 电气材料供应，PoE 仅站内附带类目 → **不动（非目标行业；B 保留）**' + TAG}}],
    'SB-627': {'facts': {'legal_name': 'ИП Дроков（ОГРНИП 315615400000259；Зона GSM；Таганрог, Мариупольское ш., 1А, цок. эт., оф. 3）', 'founded': '2015' + TAG,
                         'other': '第 114 批：塔甘罗格个体工商户无线上网设备门店、0 打开 → **不动（个体规则；B 保留）**' + TAG}},
    'SB-060': [{'kp_match': 'ag@bargas.ru', 'name': 'Гречкин Александр Юрьевич (Alexander Grechkin)', 'role': 'Генеральный директор / 100% 股东 ООО «Баргас»（2012-04-28–；rusprofile）= 拍板人 / 收件人；2025-12 对 mini 工业机回「interested」' + TAG},
               {'facts': {'legal_name': 'ООО «Баргас»（ИНН 7716715348；ОГРН 1127746340622；127238 Москва, Локомотивный пр-д, д. 21, стр. 5, оф. 313；微型企业；营收 214.4 млн ₽）', 'founded': '2012-04-28' + TAG,
                          'other': '第 114 批：莫斯科安防系统销售 + 安装 + 网店（СКУД / 道闸 / 监控），业主本人曾回 interested → **分销 / 集成 20–25% small，加厚 small 一次（接上 mini 工业机 STI-054GP / STI-144GP / STI-154GP + 门禁 / 监控配套 PoE STC-028GP / STC-228GP + 付费样机；Александр 直呼）**' + RU + TAG}}],
    'SB-562': [{'kp_match': '22opt@mail.ru', 'role': 'АлтВижен / ALTVISION 研究档 KP（WA 21 次无实质回复）= 收件人' + TAG},
               {'facts': {'legal_name': 'АлтВижен / ALTVISION（22opt.ru；г. Барнаул, ул. Малахова, 95 + Москва, Чермянский пр., 7；10 年；TopVision / HIVIDEO 品牌；法人 / ИНН 未取）', 'founded': '≈2015' + TAG,
                          'other': '第 114 批：阿尔泰安防批发 + 安装（有莫斯科点）→ **分销 20% small，一页纸一次（工业 PoE STI-054GP / STI-144GP + STC-2224GP 一口价 + MOQ 1；GPON 明说不做）**；再无回声 → 不动；法人未取 → 部分坐实' + RU + TAG}}],
    'SB-895': [{'add_kp': {'name': 'Амеличкин Александр Борисович', 'role': 'Руководитель ООО «ВИЛКОМ ХОЛДИНГ»（zachestnyibiznes）— 破产观察中，不动' + TAG, 'email': '', 'source': 'https://www.list-org.com/company/71963'}},
               {'facts': {'legal_name': 'ООО «ВИЛКОМ ХОЛДИНГ»（ИНН 7710370947；ОГРН 1037700037792；107140 Москва, пер. Леснорядский, д. 10, стр. 2；54 人；2001-02-22）', 'founded': '2001-02-22' + TAG,
                          'other': '第 114 批：28 年系统集成商，但 **2026-02-07 起破产观察程序（наблюдение）** → **不动（法人状态异常；B 保留，观察结果再定）**' + TAG}}],
    'SB-320': {'facts': {'legal_name': '未具名（Vasiliy Kryukov 个人 mail.ru / list.ru；成单 1 次；在用 HRUI 产品；0 查）', 'founded': '—' + TAG,
                         'other': '第 114 批：个人成单客户（WA 在手）→ **不动（B 保留；复购走 WA；Q-33 HRUI 口径补充推 Marvell 管理 / 工业线，不报同款）**' + RU + TAG}},
    'SB-652': [{'kp_match': 'umesh.palanpuri@comxus.com', 'role': 'Deputy GM（研究档）= 收件人 / 拍板人（抄 info@）' + TAG},
               {'facts': {'legal_name': 'Comxus（comxus.com；印度工业网络 OEM 品牌 CX-NPA / CX-ND 系列；自述 India-based manufacturing + TEC 认证叙事；法定名 / CIN 未取）', 'founded': '未取' + TAG,
                          'other': '第 114 批：自有品牌工业交换机全线、现中系代工 → **贴标 OEM 30% B，加厚一次（Comxus 标 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM 第二代工源，整机 / SKD + 中性包装 + 3 年保；Umesh 直呼）**；稿内不声称 TEC / BIS；CIN 未取 → 部分坐实' + TAG}}],
    'SB-914': [{'kp_match': 'arun.raj@mro-tek.com', 'role': 'AVP – Solution Sales（研究档）= 收件人' + TAG},
               {'kp_name': 'Satish', 'role': 'MRO-TEK 研究档 KP = 抄' + TAG},
               {'add_kp': {'name': 'Aniruddha Mehta', 'role': 'Chairman & Managing Director（DIN 00720504；BSE 年报）= 拍板人（不直接收件）' + TAG, 'email': '', 'source': 'https://www.zaubacorp.com/company/MRO-TEK-REALTY-LIMITED/L28112KA1984PLC005873'}},
               {'facts': {'legal_name': 'MRO-TEK Realty Limited → UMIYA BUILDCON LIMITED（2026 更名；RoC 已同意再更名 MRO-TEK Networks Limited）；CIN L28112KA1984PLC005873；BSE 532376；GSTIN 29AAACM9875E1Z1；No. 6, New BEL Road, Chikkamaranahalli, Bangalore 560054；工厂 Konnappana Agrahara', 'founded': '1984-12-10' + TAG,
                          'other': '第 114 批：上市 Make-in-India 网络 / 电信 OEM，产品板块 FY2025-26 ₹3,267 lakhs（+80%）→ **贴标 / 配套 30% B BIG，加厚一次（CORNUS / LAVENDER 类工业与接入交换机 SKD / 板级 + 整机第二来源 STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM + STC-4424GCPM / STC-424XGGPM-280W + 中性包装；Arun 直呼 + Satish 抄；一问 SKD 本地化比例）**；回信 → 次候选升 A；稿内不声称 BIS / TEC' + TAG}}],
    'SB-684': [{'kp_match': 'opsharma@technicsonline.com', 'name': 'Om (O.P.) Sharma', 'role': 'Technics Infosolutions 研究档 KP（1996–；zoominfo；职务待核；研究档原名「Prakash」更正）= 收件人' + TAG},
               {'add_kp': {'name': 'Kapil Gupta', 'role': '联系人（mytat 目录）' + TAG, 'email': '', 'source': 'https://mytat.co/mart-details/modbus-gateway/technics-infosolutions-private-limited-2246859'}},
               {'facts': {'legal_name': 'Technics Infosolutions Private Limited（CIN U72900DL2013PTC252728；4648/21, Sedhumal Building, Daryaganj, New Delhi 110002；销售办公 4731/21 Dayanand Road；业务 1990 起；Advantech Premier Channel Partner IN250001；11–50 人；₹10–25 Cr）', 'founded': '2013-05-25（业务 1990）' + TAG,
                          'other': '第 114 批：新德里工业自动化分销（Advantech / Kyland）+ 250 台工业 FS 具体询价 → **分销 20% B BIG，加厚一次（接上「IM-FS240GM 250 pcs」→ STI-244GP / STI-0240GE 250 台阶梯价 + 付费样机 2 台 + FOB 深圳；Om Sharma 直呼）**；回信 → 次候选升 A；守界：Indian Railways / Delhi Metro 客户 → 只谈非轨交线；不点名 Advantech / Kyland' + TAG}}],
    'SB-304': [{'kp_match': 'ceo@aadona.com', 'role': 'Director / CEO（indiafilings 董事 2018-06-18–；pinaki.chatterjee@aadona.com 为登记邮箱）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'govind.madhav@aadona.com', 'role': 'AADONA 研究档 KP = 抄' + TAG},
               {'facts': {'legal_name': 'AADONA Communication Private Limited（CIN U72900CT2018PTC008600；RoC Chhattisgarh；注册地 07, SBI Colony, Mahoba Bazar, Raipur 492099；总部 Phoenix Tech Tower, IDA Uppal, Hyderabad 500039；董事 Pinaki Chatterjee / Shivani Chattirajee / Soma Chatterjee；实缴 ₹23.04 lakh；<₹10 Cr；11–50 人）', 'founded': '2018-06-18' + TAG,
                          'other': '第 114 批：Start-up India「Made in India」纯渠道自有品牌（MII Class I / II；全线外采）→ **贴标 OEM 30% B，加厚一次（AADONA 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP / STI-144GP 整机或 SKD + 中性包装 / 自编货号；Pinaki 直呼 + Govind 抄）**；稿内不声称 MII 分类 / 不提政府项目' + TAG}}],
    'SB-305': [{'kp_match': 'ramachandra.r@bitsandbyte.net', 'name': 'Ramachandra Raju (R)', 'role': 'Co-Founder / Director（MCA 董事；tracxn）= 拍板人' + TAG},
               {'kp_match': 'ankit@bitsandbyte.net', 'role': 'Executive Director – Global Sales and Alliances（2025-11–；LinkedIn）= 收件人' + TAG},
               {'add_kp': {'name': 'Prakash Uppunda Rao', 'role': 'Co-Founder / Director（MCA 董事）' + TAG, 'email': '', 'source': 'https://www.zaubacorp.com/company/BITS-AND-BYTE-IT-CONSULTING-PRIVATE-LIMITED/U72900KA2015PTC145953'}},
               {'facts': {'legal_name': 'Bits and Byte IT Consulting Private Limited（bits&BYTE；CIN U72900KA2015PTC145953；#52, 2nd Floor, Vittal Mallya Road, Bangalore 560001；≈57 人；₹10–50 Cr FY2025；研究档「Bits&Byte Consulting Pvt Ltd」更正）', 'founded': '2015-05-20' + TAG,
                          'other': '第 114 批：班加罗尔网络与数字集成商，曾问环网 <20 ms / 2 光 10 电非 PoE / 10G / bypass / 100G → **集成 25% B BIG，加厚一次（逐条答复：STI-288DGGPM / STI-488DGGPM 环网（收敛按规格书据实）、STI-0240GE、STC-424XGGPM-280W 10G 上行、STH-32C-HSI 100G；bypass 如无明说无；Ankit 直呼 + Ramachandra 抄）**；回信 → 次候选升 A' + TAG}}],
    'SB-308': [{'kp_match': 'pratap@alconlink.com', 'name': 'Pratap Kumar Baral', 'role': 'Director Alcon Wireless Private Limited（DIN 02545994；2010-02-03–；indiafilings）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'Alcon Wireless Private Limited（AlconLink；CIN U64200OR2010PTC011564；Plot C-3, 1st Floor, Jayadurga Nagar, Bomikhal, Bhubaneswar 751006；办公 Delhi / Mumbai / Kolkata；董事 Pratap Kumar Baral / Anusuya Patra；最近 AGM 2022-09-30；关联 WIS Networks Digital Technologies India Pvt Ltd 2017）', 'founded': '2010-02-03' + TAG,
                          'other': '第 114 批：2010 从台湾 Alcon 独立的印度 IP 监控品牌 + 自有 logo PoE / 工业交换机 + 全国渠道（3 进口商 / 16 分销 / 200 SI）→ **贴标 OEM 30% B，加厚 small 一次（AlconLink 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP / STI-144GP 第二代工源 + 中性包装 + 小 MOQ；Pratap 直呼）**；AGM 申报滞后 → 只做 T/T 预付；不点名其台湾前身' + TAG}}],
    # ---------- 第 2/3 IN 13 ----------
    'SB-343': [{'kp_match': 'yashraj@zekko.co.in', 'role': 'Manager（研究档）= 收件人' + TAG},
               {'kp_match': 'santosh@zekko.co.in', 'role': 'Manager（研究档；与前董事 Seema Santosh Singh 关联待证）= 抄' + TAG},
               {'add_kp': {'name': 'Chandrasekaran Iyer', 'role': 'Whole-Time Director（MCA；DIN 06879733）= 拍板人（不直接收件）' + TAG, 'email': '', 'source': 'https://www.zaubacorp.com/company/ZEKKO-TECH-PRIVATE-LIMITED/U74999MH2016PTC285972'}},
               {'facts': {'legal_name': 'Zekko Tech Private Limited（CIN U74999MH2016PTC285972；Unit 122, 1st Floor, C-56/1, Turbhe Industrial Park, TTC Industrial Area, Turbhe MIDC, Navi Mumbai 400705；4 人；实缴 ₹1 lakh；未清抵押 ₹2.25 Cr）', 'founded': '2016-09-16' + TAG,
                          'other': '第 114 批：4 人微型方案商、WA 已加无实质回复 → **集成 25% small，一页纸一次（工业 PoE STI-054GP / STI-144GP + STC-228GP 一口价 + MOQ 1；光模块不做；Yashraj 直呼）**；再无回声 → 不动' + TAG}}],
    'SB-486': [{'kp_match': 'info@ngapl.com', 'role': 'Operation Head（研究档）= 收件人（info@ 职能箱）' + TAG},
               {'add_kp': {'name': 'Sanjiv Dua', 'role': 'Founder / Managing Director（IIT Delhi；ngapl.in；MCA 董事）= 拍板人' + TAG, 'email': '', 'source': 'https://ngapl.in/?page_id=11105'}},
               {'facts': {'legal_name': 'NextGen Automation Private Limited（NGAPL；CIN U31200WB2002PTC094683；PS PACE, Unit 102, 1/1A Mahendra Roy Lane, Kolkata 700046；注册地 Stephen Court, 18A Park Street；≈75 人；₹10–50 Cr FY2025；未清抵押 ₹29.43 Cr；66,865 sq ft 车间）', 'founded': '2002-05-24' + TAG,
                          'other': '第 114 批：钢铁 / 矿山大型工业电气 + 自动化集成商，已有「8 电口工业交换机（Atop EHG6408）」询盘 → **集成 25% B BIG，加厚一次（STI-280GE 8 GE 非管理 / STI-288GPM 8 PoE + 2 SFP 管理 + 环网 STI-288DGGPM，导轨 + 宽温 + 3 年保 + 付费样机 2 台；Rajendra 直呼 + info@）**；回信 → 次候选升 A；守界：不声称 IEC 61850 / 防爆；不点名 Atop / Siemens' + TAG}}],
    'SB-607': [{'kp_match': 'vijay@jtoptics.com', 'name': 'Vijay Jankiprasad Gupta', 'role': 'Designated Partner / Founder & CEO Jayani Technologies LLP（DIN 05103167；2011-11-17–）— 价格敏感 + 已选他家 → 不动' + TAG},
               {'facts': {'legal_name': 'Jayani Technologies LLP（JTOPTICS®；LLPIN AAA-6913；Office 23, 3rd Floor, Building A, Gami Industrial Park, TTC MIDC, Pawane, Navi Mumbai 400705；指定合伙人 Vijay Jankiprasad Gupta / Nidhi Vijay Gupta；≈12 人）', 'founded': '2011-11-17' + TAG,
                          'other': '第 114 批：主业光模块 / DAC / MPO（Saga 不做），交换机 / MC 价格敏感、称已与他家合作 → **不动（实质婉拒；B 保留，其上交换机需求时再看）**' + TAG}}],
    'SB-678': [{'kp_match': 'vidur.batra@qntmnet.com', 'role': 'Vice President – System Engineering, Pre-Sales & Post-Sales Strategy（signalhire / rocketreach）= 收件人' + TAG},
               {'kp_match': 'abhijit@qntmnet.com', 'role': 'Corporate Vice President（rocketreach；New Delhi）= 拍板人 / 抄' + TAG},
               {'facts': {'legal_name': 'Quantum Networks（qntmnet.com；Ahmedabad 总部 + 多城团队；≈57 人；COO Dishen Majithia / CRO Edgar Dias；关联 Quantum Networks SG Pte Ltd；印度法人 / CIN 未取）', 'founded': '未取' + TAG,
                          'other': '第 114 批：云管理全栈自有品牌（含工业 PoE 子线 QN-IS），现用中国产工业交换机 → **贴标 OEM 30% B BIG，加厚一次（只做 QN-IS 工业线第二代工源 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM + 中性包装 + 3 年保；云管理线不碰、不声称云管理；Vidur 直呼 + Abhijit 抄）**；CIN 未取 → 部分坐实；T/T 预付' + TAG}}],
    'SB-169': [{'kp_match': 'sales@agsplus.in', 'role': 'AGS Plus 研究档 KP（+91 98105 德里号段；2025-06 对 24 PoE 回「price」）= 收件人' + TAG},
               {'kp_match': 'gunjan@xexagon.co.in', 'role': 'Xexagon 研究档 KP = 抄' + TAG},
               {'add_kp': {'name': 'Tusharkumar Rajeshbhai Patel', 'role': 'CEO / Director Xexagon Hi-Tech Private Limited（tofler / xexagon.co.in）' + TAG, 'email': '', 'source': 'https://www.tofler.in/xexagon-hi-tech-private-limited/company/U28299GJ2025PTC160203'}},
               {'facts': {'legal_name': 'AGS Plus（agsplus.in 占位；法人未取）+ 关联 Xexagon（Odhav, Ahmedabad；个体 GSTIN 24BWZPP0936L1ZR → Xexagon Hi-Tech Private Limited CIN U28299GJ2025PTC160203，Block A-209, Global Business Park, Odhav, Ahmedabad 382415；≤10 人；₹5–25 Cr）；两实体关系未清', 'founded': 'Xexagon 2019 → 2025-03-12' + TAG,
                          'other': '第 114 批：曾对 24 口 PoE 问价 → **分销 20% small，一页纸一次（STC-2224GP 一口价 + STC-228GP + 工业 STI-054GP，MOQ 1；Vinod 直呼 + Gunjan 抄）**；再无回声 → 不动；身份未清 → 部分坐实；Xexagon 代理防爆区产品 → 稿内不碰防爆' + TAG}}],
    'SB-641': [{'kp_match': 'ravi@apolloinfoways.in', 'role': 'Founder / CEO / Director Apollo Infoways Private Limited（MCA 董事 2014-02-03–）= 拍板人 / 收件人' + TAG},
               {'add_kp': {'name': 'Ivy Prakash', 'role': 'Director（MCA；2014-02-03–）' + TAG, 'email': '', 'source': 'https://www.zaubacorp.com/APOLLO-INFOWAYS-PRIVATE-LIMITED-U72900DL2014PTC264342'}},
               {'facts': {'legal_name': 'Apollo Infoways Private Limited（WatchDog；CIN U72900DL2014PTC264342；注册地 E-703, Plot 60, Mayur Dhwaj Apartment, I.P. Extension, New Delhi 110092；运营 Noida；实缴 ₹10 lakh；₹10–50 Cr FY2025；11–50 人）', 'founded': '2014-02-03' + TAG,
                          'other': '第 114 批：安防 + 网络 OEM 品牌，自有型号交换机全线，现用丰润达商用 PoE + AOA 工业 → **贴标 OEM 30% B BIG，加厚一次（Q-33 口径：只推 SmartByte / Marvell 管理线 STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM + 工业 STI-144GP / STI-288DGGPM 作 WatchDog 标第二源 + 中性包装；不报与丰润达同款；Ravi 直呼）**；回信 → 次候选升 A；不点名丰润达 / AOA' + TAG}}],
    'SB-655': [{'kp_match': 'ranjan.gupta@digisol.com', 'role': 'Dy. Business Development Manager（研究档）= 收件人' + TAG},
               {'kp_match': 'nandini.singh@digisol.com', 'role': 'Deputy Manager（研究档）= 抄' + TAG},
               {'add_kp': {'name': 'Devendra Kamtekar', 'role': 'CEO DIGISOL Systems Limited（owler）= 拍板人（不直接收件）' + TAG, 'email': '', 'source': 'https://www.owler.com/company/digisol'}},
               {'facts': {'legal_name': 'DIGISOL Systems Limited（Smartlink Holdings Ltd（BSE 上市）100% 子公司；孟买总部 / 果阿 Verna 工厂；Q2 FY26 营收 ₹6,327.58 lakh / 季、PAT ₹268.43 lakh；CIN 未取）', 'founded': '未取（品牌 1993）' + TAG,
                          'other': '第 114 批：上市集团 Make-in-India 品牌，工业线现由 HRUI 供 → **贴标 OEM 30% B BIG，加厚一次（Q-33 HRUI 口径：只推 SmartByte / Marvell 管理线 STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM + 工业管理 STI-288DGGPM / STI-488DGGPM（SKD / 板级可谈）+ 中性包装；不报与 HRUI 同款；Ranjan 直呼 + Nandini 抄）**；回信 → 次候选升 A；CIN 未取 → 部分坐实；不点名 HRUI / 不声称 BIS / TEC' + TAG}}],
    'SB-857': [{'kp_match': 'sales@airpro.in', 'name': 'Deepak Jain', 'role': 'Promoter / Director AirPro Technology India Limited（DIN 06504116；2014-02-17–；deepak@airpro.in 为登记邮箱）= 拍板人 / 收件人' + TAG},
               {'add_kp': {'name': 'Pankaj Bhansali', 'role': 'Promoter / Director（DIN 03154793；2017-09-29–）' + TAG, 'email': '', 'source': 'https://www.zaubacorp.com/company/AIRPRO-TECHNOLOGY-INDIA-PRIVATE-LIMITED/U72900RJ2014PTC045127'}},
               {'facts': {'legal_name': 'AirPro Technology India Limited（原 Private Limited，2025-04-28 转公众公司；CIN U72900RJ2014PLC045127；D-30, Gautam Marg, Nirman Nagar, Ajmer Road, Jaipur 302019；实缴 ₹1.89 Cr；₹10–50 Cr FY2025；SME IPO 招股书 36 lakh 股）', 'founded': '2014-02-17' + TAG,
                          'other': '第 114 批：自有品牌交换机全线（AP-ESG3024P 等）+ IPO 扩张期 → **贴标 OEM 30% B BIG，加厚一次（AirPro 标 Marvell 管理 L2 / L3 STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM + 工业 STI-144GP / STI-288DGGPM 第二代工源 + 中性包装 + 小 MOQ；Deepak 直呼）**；回信 → 次候选升 A；稿内不提 IPO / 不引用招股书' + TAG}}],
    'SB-954': [{'kp_match': 'switch@netstar.in', 'role': 'NETSTAR 交换机采购职能箱（WA 13 次无实质回复）= 收件人' + TAG},
               {'add_kp': {'name': 'Dharmesh Patel', 'role': 'Manager Infonet Technologies / NETSTAR（tradeindia）= 候选具名收件人' + TAG, 'email': '', 'source': 'https://www.tradeindia.com/products/netstar-outdoor-reverse-poe-switch-with-fiber-uplink-port-single-fiber-sc-rpoe-switch-with-fiber-uplink-10-100mbps-7128379.html'}},
               {'facts': {'legal_name': 'Infonet Technologies（NETSTAR 品牌；合伙企业；GSTIN 24AAGFI3821H1ZN；IEC AAGFI3821H；Shop 19, Limbani Complex, Ambli Bopal Road, Ahmedabad 380058；11–25 人；₹5–10 Cr）', 'founded': '1995' + TAG,
                          'other': '第 114 批：ISP / WISP 反向 / 无源 PoE 自有品牌（Saga 无此线）→ **贴标 30% small，一页纸一次（NETSTAR 标标准 802.3af/at PoE STC-028GP / STC-228GP + 小 MOQ + 中性包装；反向 PoE / 注入器明说不做）**；再无回声 → 不动' + TAG}}],
    'SB-044': [{'kp_match': 'luthra@win-alliance.com', 'role': 'Win-Tech Alliance Ltd（香港法人）孟买负责人；提出 5 / 8 口 2.5G 交换机 CKD = 收件人' + TAG},
               {'facts': {'legal_name': 'Win-Tech Alliance Ltd（香港：Room 702B, 7/F, Valley Centre, 80-82 Morrison Hill Road, Wanchai；海关记录 17 票对印度进口商 Radix Electrosystems / Greenglobe / Pushpam；HK 公司编号未取）', 'founded': '未取' + TAG,
                          'other': '第 114 批：香港贸易商替印度组装厂找 2.5G CKD → **分销 20% small，一页纸一次（2.5G 整机 / SKD 方案 + MOQ + 单价区间；待 Simon 定 SmartByte 2.5G 型号口径（与 SB-263 同一待办）后再发；WA 同步）**；无口径或再无回声 → 不动；法人 HK、操盘 Mumbai → iso 保留 IN；部分坐实' + TAG}}],
    'SB-064': {'facts': {'legal_name': 'Amity Technologies（合伙企业，2009-05-04；Udyam Small 2022-23；Plot 279, 2nd Floor, Vivekananda Nagar, Kukatpally, Hyderabad 500072 + Plot 38, Meridian Enclave, Nizampet Road 500085；ISO 9001:2015；16–25 人；$1–2.5M）', 'founded': '2009-05-04' + TAG,
                         'other': '第 114 批：军规加固 COTS 计算机 + 自制加固以太网交换机（military mission-critical）→ **不动（守界：军用不碰 + 同行；B 保留）**' + TAG}},
    'SB-072': [{'add_kp': {'name': 'Randhir Kumar Singh', 'role': 'Proprietor TECHNOSYS（GST 登记人）— 个体微型，不动' + TAG, 'email': '', 'source': 'https://www.knowyourgst.com/gst-number-search/technosys-27AWZPS2792Q2ZY/'}},
               {'facts': {'legal_name': 'TECHNOSYS（个体经营 Randhir Kumar Singh；GSTIN 27AWZPS2792Q2ZY；#104, Raven Home, Plot 36, Sector 21, Kamothe, Khandeshwar, Navi Mumbai 410209；₹0–40 lakh）', 'founded': '2010-06-05' + TAG,
                          'other': '第 114 批：新孟买个体 IT 服务 / 小网店（营业额 <₹40 lakh）→ **不动（个体规则；B 保留；其主动询工业 FS 再按 STI-288DGGPM 对位报）**' + TAG}}],
    'SB-1104': [{'kp_match': 'agilitybaroda@gmail.com', 'role': '前 Regional Sales Representative（Vadodara；2021-04 → 2024-04；LinkedIn）**已离职 → 现 Essen Deinki 区域销售经理** → 原联系线失效' + TAG},
                {'facts': {'legal_name': 'Agility Elektrotekniks Private Limited（CIN U31908UP2014PTC066111；总部 A-10/64, Meerut Road Industrial Area, Site-III, Ghaziabad 201003；12 人；实缴 ₹1.24 Cr；营收 ₹139 Cr（tracxn 口径，待核））', 'founded': '2014-09-16' + TAG,
                           'other': '第 114 批：继电器接口模块制造 + 自动化元件特许分销；KP 已离职、仅 gmail 分部地址 → **不动（地址失效；B 保留；总部公开邮箱待补后可一页纸：bypass 系列 + STI-144GP / STI-288DGGPM 配套）**' + TAG}}],
    # ---------- 第 3/3 IN 13 ----------
    'SB-111': [{'kp_match': 'hemanth@nivoxtech.com', 'role': 'Director / 合伙人 Nivox Technologies（kompass / dnb）= 拍板人 / 收件人；2024–2025 多次问价（含 EN 50155）' + TAG},
               {'add_kp': {'name': 'Kavitha D.', 'role': 'Director & CEO / 合伙人（crunchbase / kompass）' + TAG, 'email': '', 'source': 'https://in.kompass.com/c/nivox-technologies/in433614/'}},
               {'facts': {'legal_name': 'Nivox Technologies（合伙企业；GSTIN 29AAIFN5171H1ZZ；IEC 0711010331；401B, 4th Floor, Nugen Residency, 105 Dollars Scheme, Nandini Layout, Bengaluru 560096；≤10 人；₹5–25 Cr；Lantech（台湾）工业交换机印度分销 + 自有品牌 IVEONET）', 'founded': '2011' + TAG,
                          'other': '第 114 批：台湾品牌工业交换机分销 + 业主本人多次问价 → **分销 20% small，加厚 small 一次（性价比第二线 STI-144GP / STI-154GP / STI-288DGGPM + 工业 MC 对位 STC-110XGE，3 年保 + 付费样机；EN 50155 明说没有、轨交不接；Hemanth 直呼）**；回信 → 次候选；不点名 Lantech' + TAG}}],
    'SB-1113': [{'kp_match': 'office@fastball.in', 'role': 'Proprietor / CEO Fastball（GST 07AJJPR5445G1ZX）— 成单 1 次后 gg' + TAG},
                {'facts': {'legal_name': 'Fastball（Fastball Telecom & Networking；个体经营 Rishi Kumar Bansal；GSTIN 07AJJPR5445G1ZX；A-47/A, Gali No. 4, Main Shukra Bazar Road, Ashok Nagar, Delhi 110093；≤10 人；Signal Fire 熔接机印度独家进口）', 'founded': '2016（GST 2021）' + TAG,
                           'other': '第 114 批：个体 FTTH 工具 / 光配线分销，成单 1 次（STSC20231009002）后已凉 → **不动（B 保留；复购自来按老价 + T/T）**' + TAG}}],
    'SB-1138': [{'kp_match': 'yogendra.rajput@', 'name': 'Yogendra Kumar Rajput', 'role': 'Founder / Managing Director（CISA & CISM）；DevRay IT Solutions Pvt Ltd + MapleCloud Tech Services Pvt Ltd 两家董事（MCA）= 拍板人 / 收件人；Elsa 线程 12 封具名追问 CENTEC L3' + TAG},
                {'add_kp': {'name': 'Neha Jain', 'role': 'Director DevRay IT Solutions Private Limited（MCA）' + TAG, 'email': '', 'source': 'https://www.falconebiz.com/company/DEVRAY-IT-SOLUTIONS-PRIVATE-LIMITED-U62013UP2024PTC204532'}},
                {'facts': {'legal_name': 'DevRay IT Solutions Private Limited（CIN U62013UP2024PTC204532；2024-06-13；Noida）+ MapleCloud Tech Services Private Limited（CIN U72900DL2018PTC338066；2018-08-31；实缴 ₹4 lakh；董事 Yogendra Kumar Rajput / Ruchi Lal / Suresh Chand Jain）；100+ 人；500+ 企业客户；FY26 目标 ₹100 Cr（含 Iris Global 全国分销）', 'founded': '2018-08-31（MapleCloud）/ 2024-06-13（DevRay）' + TAG,
                           'other': '第 114 批：本土网络安全 + 网络设备 OEM，MD 本人追问 CENTEC L3 核心机型（8 GB RAM / 16 GB Flash）+ 价格 + 中国以外产地 → **贴标 OEM 30% B BIG（CENTEC 敲门砖），加厚一次（STH-2C24XF-HSI / STH-8C48DX-HSI / STH-32C-HSI 的 RAM / Flash 按规格书据实、datasheet + 阶梯价、产地只能深圳明说 + 中性包装 / 自编货号；Yogendra 直呼）**；回信 → **升 A 候选**；守界：不声称 SONiC / ONIE；不提其政府 / CERT-In 项目' + TAG}}],
    'SB-802': [{'kp_match': 'ps.vijay@mspllimited.com', 'role': 'MSPL Limited 研究档 KP（WA 已加无实质回复；职务待核）= 收件人' + TAG},
               {'add_kp': {'name': 'Narendra Baldota', 'role': 'Chairman & Managing Director MSPL Limited（Baldota 集团）— 不直接收件' + TAG, 'email': '', 'source': 'https://en.wikipedia.org/wiki/MSPL_Limited'}},
               {'facts': {'legal_name': 'MSPL Limited（CIN U13100MH1961PLC012160；注册地 117, Baldota Bhavan, Maharshi Karve Road, Mumbai 400020；运营 Baldota Enclave, Hospet 583203；≈1,000 人；>₹1,000 Cr FY2025；实缴 ₹38.4 Cr；原名 Mineral Sales Private Limited）', 'founded': '1961-10-18' + TAG,
                          'other': '第 114 批：大型铁矿 / 球团 / 风电终端用户 → **终端 25% B 低优先，一页纸一次（矿区 / 选矿厂非防爆区工业 PoE 环网 STI-288DGGPM / STI-488DGGPM + 宽温 + 3 年保 + 付费样机；防爆区明说不做；Vijaykumar 直呼）**；再无回声 → 不动；守界：防爆 / IS-ATEX 不碰' + TAG}}],
    'SB-447': [{'kp_match': 'infoautomation18@gmail.com', 'role': 'GST 登记人 / 合伙经营 Automation Systems & Solution（indiamart）= 收件人；2025-04 对 2 光 4 PoE 回复要 DS' + TAG},
               {'add_kp': {'name': 'R.K. (Rakesh Kumar) Sharma', 'role': 'CEO Automation Systems & Solution（indiamart / tatanexarc）' + TAG, 'email': '', 'source': 'https://www.indiamart.com/automation-systems-solution/profile.html'}},
               {'facts': {'legal_name': 'Automation Systems & Solution（个体经营；GSTIN 07AOCPK7395A1Z0；T-12, 3rd Floor, Pankaj Central Market, I.P. Extension, Patparganj, Delhi 110092；2007 起；≤10 人；₹0–40 lakh 自报；Teltonika / Procon / Banner / Shavison / Citel 授权分销）', 'founded': '2007' + TAG,
                          'other': '第 114 批：个体但工业网络专营（自有编号工业交换机 IND-D-M-FG-0402-N + 授权进口商）、主动要 DS → **分销 20% small，一页纸一次（补发 2 光 4 PoE 对位 STI-154GP / STI-144GP 规格书 + 一口价 + MOQ 1 + 付费样机；Azad 直呼）**；再无回声 → 不动（个体规则例外：工业专营）' + TAG}}],
    'SB-357': {'facts': {'legal_name': '未坐实（infonet-tech.com 站点为北美 POS 软件公司；「Sudesh Verma」1 查仅同名记者 / 律师 ≠；需求 ONU）', 'founded': '未取' + TAG,
                         'other': '第 114 批：主体未坐实（域名错配）+ 需求 ONU（Saga 无）→ **不动（B 保留）**' + TAG}},
    'SB-630': {'facts': {'legal_name': 'Core IT Solutions（citsindia.com；孟买；1 查仅见同名 CORE IT SOLUTIONS PRIVATE LIMITED CIN U72100MH2005PTC153203（Thane；Strike Off）—— 是否同一主体未证）', 'founded': '未取' + TAG,
                         'other': '第 114 批：KP Sarwar 邮箱退信 + 法人线索仅为 Strike Off 同名 → **身份不清；不动（B 保留；info@ 回声再核）**' + TAG}},
    'SB-045': {'facts': {'legal_name': '未坐实（advancedigital.co.in 占位页；1 查命中均为他国 / 他城同名主体 ≠）', 'founded': '未取' + TAG,
                         'other': '第 114 批：未坐实 + 站点占位 + 多轮「暂时没需求」→ **不动（B 保留；其主动询价再报）**' + TAG}},
    'SB-1105': {'facts': {'legal_name': '未具名（Suraj Katte 个人；仅 WA；0 查）', 'founded': '—' + TAG,
                          'other': '第 114 批：个人买家、多次 0 回复 → **不动（B 保留；WA 不再推送）**' + TAG}},
    'SB-194': {'facts': {'legal_name': '未坐实（Sri Annai Business Associates；sabaindia.com 失效；Erode；1 查仅见同名家具 / 塑料经销 Sri Annai Agency ≠）', 'founded': '未取' + TAG,
                         'other': '第 114 批：未坐实 + 官网失效 + 报价后 18 个月无进展 → **不动（B 保留；yahoo 箱回声再按 STC-228GP 老价续）**' + TAG}},
    'SB-306': [{'kp_match': 'digital_sys@hotmail.com', 'role': 'Digital Systems 经营者（古吉拉特；WA；2024-04 对 10G MC 回 Yes + 名片）= 收件人' + TAG},
               {'facts': {'legal_name': '未坐实（「Digital Systems」泛名 + hotmail；0 查）', 'founded': '未取' + TAG,
                          'other': '第 114 批：有明确进口意愿但主体不可核 → **分销 20% small，一页纸一次（STC-110XGE 10G MC + STC-028GP / STC-228GP 一口价，MOQ 1、T/T 预付、FOB 深圳 / 百运网 DAP 可选；Jayesh 直呼；WA 同步）**；再无回声 → 不动；只做预付' + TAG}}],
    'SB-341': [{'kp_match': 'rkahir65@gmail.com', 'role': 'Smart Security Systems 经营者（2025-07 对 2 光 8 PoE 回「price」）= 收件人' + TAG},
               {'facts': {'legal_name': '未坐实（「Smart Security Systems」泛名 + gmail；0 查）', 'founded': '未取' + TAG,
                          'other': '第 114 批：刚问过价 → **分销 20% small，一页纸一次（STC-228GP 一口价 + STC-028GP，MOQ 1、T/T 预付、FOB 深圳）**；再无回声 → 不动；只做预付' + TAG}}],
    'SB-632': [{'kp_match': 'sucheytaa@grypen.in', 'role': 'Grypen Technologies 研究档 KP（职务待核）= 收件人（抄 info@grypen.in）' + TAG},
               {'facts': {'legal_name': 'Grypen Technologies Private Limited（grypen.in；Plot 467/A, Mahipalpur, New Delhi 110037；IT & C 系统集成 + 咨询 / 培训；CIN 未取）', 'founded': '未取' + TAG,
                          'other': '第 114 批：小型集成商 + 「商业交换机」询盘 → **集成 25% small，一页纸一次（STC-228GP / STC-2224GP / STC-4424GCPM 三档一口价 + MOQ 1；Shubham 直呼 + info@ 抄）**；再无回声 → 不动；CIN 未取 → 部分坐实；只做预付' + TAG}}],
}

def apply(d, u):
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if u.get('name') and not k.get('name'):
                    k['name'] = u['name']
                if u.get('name') and k.get('name') and k.get('name') != u['name'] and TAG not in (k.get('role') or ''):
                    k['name'] = u['name']
                if u.get('role') and TAG not in (k.get('role') or ''):
                    k['role'] = u['role']
    if u.get('kp_name'):
        for k in kps:
            if (k.get('name') or '') == u['kp_name'] and TAG not in (k.get('role') or ''):
                k['role'] = u['role']
    if u.get('add_kp') and not any(u['add_kp']['name'] == (k.get('name') or '') for k in kps):
        kps.append(u['add_kp'])
    seen, dedup = set(), []
    for k in kps:
        key = (k.get('name'), k.get('email'), k.get('role') or k.get('title'))
        if key in seen:
            continue
        seen.add(key); dedup.append(k)
    d['kp'] = dedup
    cf = d.get('company_facts') or {}
    for fk, fv in (u.get('facts') or {}).items():
        if TAG not in str(cf.get(fk, '')) and fv:
            cf[fk] = fv if fk != 'other' or not cf.get('other') else (cf['other'] + '；' + fv)
    d['company_facts'] = cf
    if u.get('country_fix'):
        d['country_fix'] = u['country_fix']


if __name__ == '__main__':
    for code, u in UPD.items():
        p = os.path.join(RESEARCH_DIR, f'{code}.json')
        d = json.load(open(p, encoding='utf-8'))
        for one in (u if isinstance(u, list) else [u]):
            apply(d, one)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(code, 'ok')
