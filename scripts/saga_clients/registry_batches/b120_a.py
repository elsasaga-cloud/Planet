# -*- coding: utf-8 -*-
"""第 120 批（T29-U113，2026-10-29）第 1 段 24 户（SA 池余 3 + PH 池 11 + ZA 池 10）—— 官方登记核实写入 registry。
PH 路径首测：SEC 号 = companyhouse.ph（SEC Code）/ 上市公司 SEC 17-C / 17-Q 披露；官网页脚 + D&B / verif / businesslist.ph 补地址 → 2/11 SEC 号。
ZA 路径首测：CIPC 注册号 = 官网 T&C 自列（YYYY/NNNNNN/07）；D&B / yellosa / hsbd / ZoomInfo 补地址 → 1/10 注册号。
SA 余 3：2/3 实为阿联酋实体（沙迦 / 阿布扎比）→ country_fix 阿联酋；1 户 0 查。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 120
F = '2026-10-29'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜（买方清关；TDRA / ESMA 不声称）'
SA = '— 沙特常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP（买方清关；SASO / SABER 不声称）'
PH = '— 菲律宾常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 马尼拉（买方清关；NTC 不声称）'
ZA = '— 南非常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 约堡（买方清关；ICASA / NRCS 不声称）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ---------------- SA 池余 3 ----------------
row('SB-404', 'TEAMAC Arabia（teamac-arabia.com；**tradeindia 企业页：Hamriyah Free Zone, P.O. Box 50342, Sharjah, UAE；2008 年成立；Sales & Technical Director Mr. Khursheed Ahmed Khan = 表内 KP ✓；进口 / 贸易（化工、电气、机械）+ BMS / HVAC 控制、弱电方案**）；ZoomInfo 员工页（BMS Project Engineer / Mechanical HVAC Engineer）地址为英国占位、不采信；表内原国别阿联酋，Q-65 机检按 +966 手机改沙特 → 本轮按实体地址回正 **country_fix 阿联酋**（KP 沙特手机 = 沙特销售驻点，备注保留）；牌照号 1 查未得 → 部分坐实', 'AE',
    'AE · 1 次检索：tradeindia.com/teamac-arabia-2748001（Hamriyah Free Zone, Po box 50342, Sharjah；Established in 2008；Sales & Technical Director Mr. Khursheed Ahmed Khan；Importer, Trading Company of chemical, electrical products, machinery）+ zoominfo 员工页 ×2（Teamac Arabia；地址英国占位 ✗）；2026-10-29', 'https://www.tradeindia.com/teamac-arabia-2748001/',
    '未取（FZ 牌照号 1 查未得）', '营业中（名录 + ZoomInfo 在职 2020– / 2021–）', '2008', 'FZE / FZC（Hamriyah Free Zone，推定）', 'BMS / HVAC 控制 + 弱电 + 进口贸易（沙迦；KSA 销售）', 'Hamriyah Free Zone, P.O. Box 50342, Sharjah, UAE', '小型',
    ['Khursheed Ahmed Khan — Sales & Technical Director（tradeindia 2026-10-29；研究档 KP khursheed.khan@teamac-arabia.com）= 收件人'],
    '**自建站询盘「8 光 8 PoE 管理」+ 销售技术总监为 KP → 集成商 25% B，一页纸一次（无 8 光 8 电单机：STI-288DGGPM $137 / STI-488DGGPM $147 + STC-4424GCPM $165 组合 + MOQ 1 + 付费样机；Siemens BMS 配套中性包装）' + AE + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（名录地址 + 成立年 + KP 职务；牌照号未取）；country_fix 阿联酋（回正）。')
row('SB-464', 'Hamdaz（hamdaz.com；**官网 contact：UAE = HAMDAZTECH TECHNOLOGY SERVICES LLC, PO Box 5758, Office 22, 2nd Floor, Millennium Tower, opp. Hamdan Centre, Hamdan Street, Abu Dhabi，+971 2 309 0211 / +971 2 626 5780；India = HAMDAZ TECHNOLOGIES LLP, Raha Lavender, Kozhikode, Kerala 673005，+91 92077 73300 = 表内电话 ✓（tracxn：LLP CIN ACA-6304，2023-04-18 成立）；prospeo：2024 年、21–50 人、Founder & CEO Jishad Mohammed Vakatel；业务 = Managed Software Services（IT 服务）**）→ 表内「HAMDAZTECH TECHNOLOGIES INC LLC」+ 沙特 = 误录，实体阿布扎比 → **country_fix 阿联酋**；KP Rea Cabidog 职务未得', 'AE',
    'AE · 1 次检索：hamdaz.com/contact-us（UAE - HAMDAZTECH TECHNOLOGY SERVICES LLC … Abu Dhabi；HAMDAZ TECHNOLOGIES LLP … Kozhikode … +91 9207773300）+ prospeo.io/c/hamdaz-technologies（Abu Dhabi；Founded 2024；21-50；Jishad Mohammed Vakatel Founder & Ceo）+ tracxn（Hamdaz Technologies Llp；CIN ACA-6304；incorporated Apr 18, 2023；Kozhikode）；2026-10-29', 'https://hamdaz.com/contact-us/',
    'UAE LLC 牌照号未取；印度 LLP CIN ACA-6304（2023-04-18）', '营业中（官网 + 企业库）', '2023 / 2024（新壳）', 'LLC（阿布扎比）+ LLP（印度）', 'IT / 托管软件服务（阿布扎比 + 科泽科德）', 'Office 22, 2nd Floor, Millennium Tower, Hamdan Street, Abu Dhabi, UAE', '小型（21–50 自报）',
    ['Rea Cabidog — 职务未得（研究档 KP；rea@hamdaz.com）', 'Jishad Mohammed Vakatel — Founder & CEO（prospeo 2026-10-29；无公开邮箱）'],
    '**IT 服务商 + 2023/24 新壳 + 无兴趣描述 + WA 无实质回复 → 不动（B 保留；国别更正阿联酋）**' + AE,
    '不动（非目标行业 + 新壳）；部分坐实（官网地址 + 电话；印度 LLP CIN 坐实、UAE 牌照未取）；country_fix 阿联酋。')
row('SB-008', '沙特 WhatsApp 联系人 Abdulaziz Al Jowasem（**无公司名 / 无域名 / 无邮箱 → 0 查**）— 谈合作，看过中科德能工业 FS + 金升阳工业电源；1 次实质回复后 19 次推送无回应', 'SA',
    '0 查（无公司 / 域名 / 邮箱）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '个人', '个人（沙特）', '未取', '个人',
    ['Abdulaziz Al Jowasem（WA 已加；研究档无邮箱）'],
    '**0 查 + 个人 → 不动（B 保留；WA 只问一句公司 / 网站，答后补档再评；来询按集成商 25% 报 STI DIN + 预付 100%）**' + SA, '不动（个人）；0 查。')

# ---------------- PH 池 11 ----------------
row('SB-054', 'Testronix, Inc.（testronix.com.ph / testronix.ph；**SEC Code CS200518694（companyhouse.ph）→ 2005 年注册；Unit 415, VGP Center (formerly Manila Bank Building), 6772 Ayala Avenue, Makati City 1226；sales@testronix.com.ph / techsupport@；Globe 0966 190 3000；测试仪表 + 数通 + 光模块 / MC 分销（JDSU / Acterna、Furukawa 熔接机、Midtronics）**）；表内曾向 uponcomm 大量买光模块；E 冷名单 1 次跟进 0 回复；无具名 KP（sales@）', 'PH',
    'PH · 1 次检索：companyhouse.ph/testronix-inc（TESTRONIX INC.；SEC Code: CS200518694）+ businesslist.ph/company/138062（Unit 415, VGP Center … 6772 Ayala Avenue, 1226, Makati City；test equipment, BER, datacom, transceiver, SFP, media converter）+ testronix.ph/contact（sales@testronix.com.ph；Globe 0966 190 3000）；2026-10-29', 'https://companyhouse.ph/testronix-inc',
    'SEC CS200518694', '营业中（官网 2025 + SEC 在册）', '2005（SEC 号前缀 CS2005）', 'Inc.（Stock Corporation）', '测试仪表 / 数通 / 光模块 / MC 分销（马卡蒂）', 'Unit 415, VGP Center, 6772 Ayala Avenue, Makati City 1226, Philippines', '小型',
    ['（无具名 KP：sales@testronix.com.ph；Attn: Sales Manager）'],
    '**光模块 / MC 分销商、SEC 坐实 → 分销 20% B，一页纸一次（STC-110XGE $65 + STC-228GP $33 / STC-2224GP $86 + MOQ 1 + 付费样机；SFP / 光模块 不做明说）' + PH + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；坐实（SEC 号 + 地址 + 官网）。')
row('SB-067', 'Citicore Renewable Energy Corporation（CREC；crec.com.ph；**SEC Reg. No. CS201807415；BIR TIN 010-007-383-000；11F Rockwell Santolan Town Plaza, 276 Col. Bonny Serrano Avenue, San Juan City, Metro Manila 1500；+632 8826 5698；PSE 上市（SEC 17-C 2025-06-18 / 17-Q 1Q2025）；Key Principal Oliver Y. Tan；行业 D35100 电力生产**）；表内 info@；曾外采 Maiwe；采购经 EPC', 'PH',
    'PH · 1 次检索：edge.pse.com.ph SEC Form 17-C（SEC Identification Number CS201807415；BIR 010-007-383-000；Citicore Renewable Energy Corporation；11F Rockwell Santolan Town Plaza, 276 Col. …）+ crec.com.ph 1Q2025 SEC 17-Q（SEC Registration No. CS201807415；San Juan City；8826-5698）+ dnb（Oliver Y. Tan）；2026-10-29', 'https://edge.pse.com.ph/downloadHtml.do?file_id=1777348',
    'SEC CS201807415（TIN 010-007-383-000）', '营业中（上市；季报在）', '2018（SEC 号前缀 CS2018）', 'Stock Corporation（PSE 上市）', '可再生能源发电（光伏 / 水电；D35100）', '11F Rockwell Santolan Town Plaza, 276 Col. Bonny Serrano Avenue, San Juan City, Metro Manila 1500, Philippines', '大型（上市）',
    ['Oliver Y. Tan — Key Principal（D&B 2026-10-29；无公开邮箱）', '（研究档无 KP：info@crec.com.ph）'],
    '**上市电力终端用户 + 采购经 EPC / O&M → 不动（B 保留；守界：电力按单核；其 EPC / 集成商（如 SB-071 NKS）才是对口）**' + PH,
    '不动（上市电力终端；按单核）；坐实（SEC 号 + TIN + 地址 + 披露文件）。')
row('SB-071', 'Nayon Kontrol Systems（NKS；nkstech.net；**No. 4 Illinois St., Brgy. Silangan, District III, Cubao, Quezon City 1109；成立约 1996（aihitdata「29 years」）；电力合作社 SCADA / 变电站自动化 / RTU 集成；关联 NKS Solar One, Inc. / NKS Energy Utilities, Inc. / NKS Global Limited / NKS Biomass One, Inc.；ZoomInfo 员工页地址一致**）；SEC 号 1 查未得 → 部分坐实；KP Mark Delapaz（研究档）；客户 NGCP / Meralco / Citicore（SB-067）', 'PH',
    'PH · 1 次检索：aihitdata.com/company/01B1B037（NAYON KONTROL SYSTEMS；Age 29 years；No. 4 Illinois St., Brgy. Silangan, District III, Cubao, Quezon City 1109；SCADA and Automation systems primarily for electric utilities；Also known as NKS Solar One, Inc. …）+ zoominfo 员工页 ×2（4 Illinois St Brgy. Silangan, Quezon City）；SEC 未得；2026-10-29', 'https://www.aihitdata.com/company/01B1B037/nayon-kontrol-systems/overview',
    '未取（SEC 号 1 查未得）', '营业中（官网 + 企业库）', '约 1996', 'Inc.（推定）', '电力 SCADA / 变电站自动化集成（奎松市）', 'No. 4 Illinois St., Brgy. Silangan, District III, Cubao, Quezon City 1109, Philippines', '中小型',
    ['Mark Delapaz — NKS 员工（研究档 KP；ZoomInfo 公开）'],
    '**已外采 Maiwe 工业机的变电站自动化集成商 → 集成商 25% B，一页纸一次（STI-288DGGPM $137 / STI-488DGGPM $147 + STI-280GE $46.6；不声称 IEC 61850 / 电力认证；MOQ 1 + 付费样机）' + PH + '**；电力项目按单核；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%；电力按单核）；部分坐实（企业库地址 + 成立年；SEC 未取）。')
row('SB-1012', 'Bitstream Core（bitstreamcore.com；**1 查无命中（仅无关结果）→ 未坐实**）— 菲律宾网络公司，GM Engr. Lito E. Viola；需求 2 光 2 电、主要对 SFP 感兴趣；1 次跟进无实质回复', 'PH',
    'PH · 1 次检索：「"Bitstream Core" Philippines bitstreamcore.com address Viola」→ 无相关结果（MEGA65 文档噪声）；2026-10-29', '', '未取（1 查无命中）', '未知（域名在研究档）', '未取', '未取', '网络集成（菲律宾）', '未取', '小型（推定）',
    ['Engr. Lito E. Viola — General Manager（研究档 KP；ieviola@bitstreamcore.com）= 收件人'],
    '**GM 为 KP + 口型明确（2 光 2 电）→ 集成商 25% B，一页纸一次（STC-228GP $33 / STC-028GP $28 + STI-154GP；SFP 不做明说；MOQ 1 + 付费样机）' + PH + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；未坐实（1 查无命中）。')
row('SB-141', 'Agile Network（宿务 Pari-an；**gmail + 通名 → 0 查**；表内域名 agilenetworks.com 为美国 ISP，不采信）— CEO Neil Rule；2024-08 问 10G MC 单模 / 多模是否同价；20 次推送 1 次实质回复', 'PH',
    '0 查（通名 + gmail；表内域名误归）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '未取', '小型网络公司（宿务）', 'Pari-an, Cebu City, Philippines（表内）', '小型',
    ['Neil Rule — CEO（表内；ph.agilenetwork@gmail.com）= 收件人'],
    '**CEO 为 KP + 10G MC 具体问题曾被问 → 集成商 25% B，一页纸一次（STC-110XGE $65 一口价 + 光模块不供明说 + STC-228GP；MOQ 1 + 付费样机）' + PH + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；0 查（gmail）。')
row('SB-227', 'NKF Wireless Internet and Services（**gmail + 无域名 → 0 查**）— 菲律宾小型 WISP，Joemar Baquiran；兴趣 PON（不供）；2026-01 对 2 光 2 电 mini 工业机回「sample?」', 'PH',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（2026-01 索样）', '—', '个体 / 微型', 'WISP（菲律宾）', '未取', '微型',
    ['Joemar Baquiran — 业主（研究档 KP；joemar.baquiran@gmail.com）= 收件人'],
    '**索样已回 → 集成商 25% B，一页纸一次（STI-154GP / STC-228GP 付费样机一口价 + 运费；PON 不供明说；预付 100%）' + PH + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（付费样机 + 预付 100%）；0 查（gmail）。')
row('SB-312', 'Fibercom Telecom Phils., Inc.（fibercomtelecoms.com；**官网页脚：2006-A West Tower, PSE Centre (Tektite Towers), Exchange Road, Ortigas Center, Pasig City 1605；+63 995 581 4199；inquiry@ / sales@；「27 Years」→ 约 1998 起；Foxcom 全球经销名录：Contact Person Emanuel Fryszer, efryszer@fibercomtelecoms.com（Unit W1203A, 12F PSE Center）**）；SEC 号 1 查未得 → 部分坐实；表内大量进口跳线', 'PH',
    'PH · 1 次检索：fibercomtelecoms.com/excellence-turnkey-solutions（Fibercom Telecom Phils. Inc. - 2006-A West Tower, PSE Centre … Pasig City 1605；+63 995 581 4199；27 Years）+ foxcom.com/resellers-contact-us（Fibercom Telecoms；Contact Person Emanuel Fryszer；efryszer@fibercomtelecoms.com；Unit W1203A, 12th Floor, PSE Center）+ jobscity（FIBERCOM TELECOMS PHILS., INC.）；SEC 未得；2026-10-29', 'https://fibercomtelecoms.com/excellence-turnkey-solutions/',
    '未取（SEC 号 1 查未得）', '营业中（官网 2025-11）', '约 1998（自述 27 年）', 'Inc.', '光纤 / 电信产品分销 + turnkey（帕西格）', '2006-A West Tower, PSE Centre, Exchange Road, Ortigas Center, Pasig City 1605, Philippines', '小型',
    ['Emanuel Fryszer — Contact Person / 负责人（Foxcom 经销名录 2026-10-29；efryszer@fibercomtelecoms.com）= 收件人', '（研究档 KP：inquiry@fibercomtelecoms.com）'],
    '**光纤产品分销商、具名负责人公开 → 分销 20% B，一页纸一次（STC-228GP $33 / STC-2224GP $86 / STC-110XGE $65 + MOQ 1 + 付费样机；跳线 / SFP 不做明说）' + PH + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网地址 + 电话 + 名录 KP；SEC 未取）。')
row('SB-314', 'RSPOT Solutions, Inc.（rspotsolutions.com；**官网：Unit 7B-19 Bldg. 7 Residencias de Manila, Pandacan, Manila；manila@；+63 2 8293-9507；VisMin 线 088 326-0093；Value Added Distributor（数据中心、结构化布线、CCTV、无线、工业 GSM 网关）；Vericom 菲律宾经销联络人 Mr. Juner D. Yaneza（vericom@rspotsolutions.com）**）；SEC 号 1 查未得 → 部分坐实；表内从中国直采 HDMI 类', 'PH',
    'PH · 1 次检索：rspotsolutions.com（RSPOT SOLUTIONS, INC.；Unit 7B-19 Bldg. 7 Residencias de Manila Pandacan Manila；+63 2 8293-9507；088 326-0093；Value Added Distributor）+ intl.vericomsolutions.com/ContactUs/philippines（RSPOT Solutions, Inc.；Mr. Juner D. Yaneza；vericom@rspotsolutions.com）；SEC 未得；2026-10-29', 'https://www.rspotsolutions.com/',
    '未取（SEC 号 1 查未得）', '营业中（官网 © 2026）', '未取', 'Inc.', 'ICT / 布线 / CCTV 增值分销（马尼拉 + 米沙鄢-棉兰老）', 'Unit 7B-19 Bldg. 7, Residencias de Manila, Pandacan, Manila, Philippines', '小型',
    ['Juner D. Yaneza — 经销联络负责人（Vericom 经销页 2026-10-29；vericom@rspotsolutions.com）= 收件人', '（研究档 KP：vismin@rspotsolutions.com）'],
    '**布线 / CCTV 增值分销商、已习惯中国直采 → 分销 20% B，一页纸一次（STC-028GP $28 / STC-2216GP / STC-2224GP $86 + STI-154GP + MOQ 1 + 付费样机）' + PH + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网地址 + 电话 + 经销页 KP；SEC 未取）。')
row('SB-412', 'InterConnectivity Computer Solutions（**无邮箱 / 无域名 → 0 查**）— 菲律宾小型网络工程商 Ronald Dumaguing；需求 100M 单纤 20 km MC + 长距 PoE（MC 不供）', 'PH',
    '0 查（无邮箱 / 域名）；2026-10-29', '', '0 查', '未知', '—', '个体 / 微型', '网络工程（菲律宾）', '未取', '微型',
    ['Ronald Dumaguing — 业主（研究档 KP；无邮箱）'],
    '**产品不对位（百兆单纤 MC）+ 无邮箱 → 不动（B 保留；WA 来询按集成商 25% 报 STI-154GP / STC-228GP + 预付 100%）**' + PH, '不动（产品不对位 + 无邮箱）；0 查。')
row('SB-735', 'WhatsApp 联系人 Steve（+63 917 855 2172；**无公司 / 邮箱 → 0 查**）— 问过 2 光 4 电 PoE 未成；WA 4 次无实质回复', 'PH',
    '0 查（无公司 / 邮箱）；2026-10-29', '', '0 查', '未知', '—', '个人', '个人（菲律宾）', '未取', '个人',
    ['Steve（WA 已加；研究档无邮箱）'],
    '**0 查 + 个人 + 4×0 → 不动（B 保留）**' + PH, '不动（个人）；0 查。')
row('SB-979', 'iOne Resources, Inc.（ioneresources.net；**D&B：Unit 1006 The Centerpoint Condominium, Julia Vargas Avenue cor. Garnet Road, Ortigas Center, Pasig, Metro Manila 1605；verif：6202 计算机咨询，Chairperson Alberto A. Catangui；RocketReach：2002 年成立、约 45 人、CEO Alberto Catangui，Director Joel Orias，VP Operations Charles Catangui，Sales Manager Philip Eleda**）；SEC 号 1 查未得 → 部分坐实；TP-Link 在用；表内阿里巴巴推送来源，未跟进', 'PH',
    'PH · 1 次检索：dnb.com（IONE RESOURCES, INC.；Unit 1006 The Centerpoint Condominium Julia Vargas Avenue corner Garnet Road, Ortigas Center, Pasig 1605；Key Principal Alberto A. Catangui）+ verif.com（6202 Computer consultancy；Alberto A. Catangui Chairperson）+ rocketreach（Founded 2002；Employees 45；CEO Alberto Catangui）；SEC 未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.ione_resources_inc.4dae52036adcd6cbc574241d68b0cb84.html',
    '未取（SEC 号 1 查未得）', '营业中（官网 + 企业库）', '2002（RocketReach 口径）', 'Inc.', '托管 ICT / 现场部署 / 网络安全服务（帕西格）', 'Unit 1006 The Centerpoint Condominium, Julia Vargas Avenue cor. Garnet Road, Ortigas Center, Pasig City 1605, Philippines', '小型（约 45 人）',
    ['Alberto A. Catangui — CEO / Chairperson（D&B + verif + RocketReach 2026-10-29；研究档 KP acatangui@ioneresources.net）= 收件人', 'Charles Catangui — VP Operations（RocketReach；无公开邮箱）'],
    '**CEO 为 KP、现场部署 / 托管 ICT（TP-Link 在用）→ 集成商 25% B，一页纸一次（STC-028GP $28 / STC-2224GP $86 / STC-4424GCPM $165 + STI-154GP + MOQ 1 + 付费样机）' + PH + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（企业库地址 + 成立年 + KP 职务；SEC 未取）。')

# ---------------- ZA 池 10 ----------------
row('SB-042', 'Regal Security Distributors SA (Pty) Ltd（regalsecurity.co.za；**总部 26 Greenstone Place, Greenstone Hill, Edenvale（hsbd / securityrsa）；+27 11 553 3300；1981 年成立、1998 年现东家收购；24–30 家分支 + 出口部（engnet 旧址 9 Electron Ave, Linbro Business Park）；南非最大多品牌安防分销之一；在售 PLANET GS-4210-8P2S / Genata / TP-Link / UTEPO + 自有标 Securi-Prod**）；CIPC 注册号 1 查未得 → 部分坐实；2025-10 已报价 2+2+8；KP Jacques Plessis（enquiries@）/ Josephine（sales@）', 'ZA',
    'ZA · 1 次检索：hsbd.co.za/supplier.aspx?acc=683（Regal Security Distributors SA；26 Greenstone Place, Greenstone Hill, Edenvale；+27 11 553 3300；over 40 years）+ securityrsa.net（Regal Distributors SA (PTY) LTD；0115533300）+ engnet.co.za/c/f.aspx/REG012（Established in 1981 … acquired 1998 … 24 branches … Exports Division … Linbro Park）；CIPC 未得；2026-10-29', 'https://www.hsbd.co.za/supplier.aspx?acc=683',
    '未取（CIPC 注册号 1 查未得）', '营业中（行业名录 2025 + 官网）', '1981', '(Pty) Ltd', '电子安防多品牌分销（豪登；撒哈拉以南出口）', '26 Greenstone Place, Greenstone Hill, Edenvale, Gauteng, South Africa', '中型（201–500；24–30 分支）',
    ['Jacques Plessis — 联系人（研究档 KP；enquiries@regalsecurity.co.za）', 'Josephine — 销售（研究档 KP；sales@regalsecurity.co.za）'],
    '**在售 PLANET 同口型 + 自有标体系 → 分销 20%（对价 GS-4210-8P2S：STC-228GP $33 / STI-154GP）↔ 贴标 OEM 30%（Securi-Prod 网络线）双轨 B，一页纸一次（Attn: Network Product Manager；2025-10 报价为开场）' + ZA + '**；回信 → 加厚',
    '分销 20% ↔ 贴标 30% 双轨；一页纸一次（预付 100%）；部分坐实（名录地址 + 电话 + 成立年；CIPC 未取）。')
row('SB-1117', 'Switchcom Distribution (Pty) Ltd（switchcom.co.za；**官网 T&C 自列注册号 2015/334722/07；registered office 49 Galaxy Avenue, Linbro Business Park, Sandton 2090（D&B 一致）；另址 Randview Business Park, 1 Avon Rd, Ferndale, Randburg 2194；2015 年成立；有线 / 无线 / VoIP / 监控 / 光纤 ICT 分销（Cambium / Hikvision / MikroTik / Ubiquiti）**）→ 坐实；KP Kevin Maphanga（Account Manager，销售侧）；两次把 Saga 当买家', 'ZA',
    'ZA · 1 次检索：switchcom.co.za/pages/our-terms-conditions（SWITCHCOM DISTRIBUTION … registration number 2015/334722/07 … 49 GALAXY AVENUE, LINBRO BUSINESS PARK, SANDTON, 2090）+ switchcom.co.za 首页（founded in 2015；Cambium Networks, Hikvision, MikroTik, Ubiquiti）+ dnb（49 GALAXY AV LINBRO PARK SANDTON 2196）；2026-10-29', 'https://www.switchcom.co.za/pages/our-terms-conditions',
    '2015/334722/07', '营业中（官网 + 电商在）', '2015', '(Pty) Ltd', 'ICT / 网络 / 监控分销（桑顿 / 兰德堡）', '49 Galaxy Avenue, Linbro Business Park, Sandton 2090, Gauteng, South Africa', '中小型',
    ['Kevin Maphanga — Account Manager（研究档 KP；kevin@switchcom.co.za；销售侧，非采购）', '（采购 / 品类经理未得：sales@switchcom.co.za；Attn: Product / Procurement Manager）'],
    '**多品牌分销商、注册号坐实 → 分销 20% B，一页纸一次（渠道 / 贴标角度：STC-2224GP $86 / STC-4424GCPM $165 / STI-154GP + MOQ 1 + 付费样机；收件 sales@ Attn: Procurement Manager，抄 Kevin）' + ZA + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；坐实（官网 T&C 注册号 + 注册地址）。')
row('SB-443', 'Spring Network（**gmail + 无域名 → 0 查**）— 南非网络承包商 Sylvanus Adejumo（表内「可以多跟进一下」）；需求 4 光 8 电工业大壳 PoE；已持有 2 光 4 与 154 同口型机；2025-10 DAC 资料 + 邮件跟进', 'ZA',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（2024 回复）', '—', '个体 / 微型', '网络承包（南非）', '未取', '微型',
    ['Sylvanus Adejumo — 业主（研究档 KP；adejumokojo@gmail.com）= 收件人'],
    '**口型明确（4 光 8 电工业 PoE）+ 曾回复 → 集成商 25% B，一页纸一次（STI-488DGGPM $147 一口价 + 付费样机；DAC 不供明说）' + ZA + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；0 查（gmail）。')
row('SB-516', 'Brigit Group / Brigit Fire（brigit.co.za；**prospeo：BRIGIT FIRE - Member of the Hudaco Group；10 Ridge Road, Laser Park, Honeydew, Gauteng 2041；+27 11 794 2217；2006 年；21–50 人；Managing Director Deon Van Zyl = 表内 KP ✓；Crunchbase：消防探测 / 气体灭火系统 OEM（BSI Kitemark）；公司简介董事 Ivor Whitcher / David Esterhuysen / Deon van Zyl / Johan Henning**）；CIPC 注册号 1 查未得 → 部分坐实；展会拿目录、无具体需求；WA 7 次无实质回复', 'ZA',
    'ZA · 1 次检索：prospeo.io/c/brigit-fire-member-of-the-hudaco-group（10 RIDGE ROAD LASER PARK, HONEYDEW, Gauteng 2041；+27117942217；Founded 2006；Deon Van Zyl Managing Director）+ crunchbase（Brigit Systems；fire detection, suppression systems；Deon Van Zyl Founder, MD & CEO）+ brigit.co.za 公司简介 PDF（One Source Total Fire Protection；OEM of gaseous extinguishing systems）；CIPC 未得；2026-10-29', 'https://brigit.co.za/pdf/Brigit-Systems-Company-profile.pdf',
    '未取（CIPC 注册号 1 查未得；Hudaco 集团成员）', '营业中（官网 + 企业库）', '2006', '(Pty) Ltd（Hudaco Group 成员）', '消防探测 / 气体灭火系统 OEM（豪登）', '10 Ridge Road, Laser Park, Honeydew, Gauteng 2041, South Africa', '小型（21–50）',
    ['Deon van Zyl — Managing Director（prospeo / Crunchbase 2026-10-29；研究档 KP deon@brigit.co.za）', 'Lyle Olivier — PM（研究档 KP；lyle@brigit.co.za）'],
    '**消防系统 OEM（非目标行业）+ 无具体需求 + WA 7×0 → 不动（B 保留；来询按集成商 25% 报 STI DIN 机柜内置）**' + ZA,
    '不动（非目标行业 + 7×0）；部分坐实（企业库地址 + 电话 + 成立年 + KP 职务；CIPC 未取）。')
row('SB-615', 'Hands On Security (Pty) Ltd（handsonsecurity.co.za；**D&B：17 Pierneef Blvd, Shop 7, Meyerton, Gauteng 1961；另址 Unit 4, 49 Galloway St, Meyerton；业主亲自勘察的本地 CCTV / 报警 / 自动化安装商（住宅 / 商业 / 工业）**）；CIPC 注册号 1 查未得 → 部分坐实；表内「有 Utepo 的 switch 销售平台」「可以多跟进一下」；群发 8 次无回复；无具名 KP', 'ZA',
    'ZA · 1 次检索：dnb.com（HANDS ON SECURITY (PTY) LTD；17 PIERNEEF BLV, 7 SHOP MEYERTON, GAUTENG, 1961）+ fire-and-security.co.za / cctvinstallers.co.za（Meyerton；CCTV solutions；owner-led site visits；Unit 4, 49 Galloway St）；CIPC 未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.hands_on_security_(pty)_ltd.2cea8d8ccfec6c5f6995d3df421911bb.html',
    '未取（CIPC 注册号 1 查未得）', '营业中（名录 2026-02）', '未取', '(Pty) Ltd', 'CCTV / 报警安装（梅耶顿，豪登）', '17 Pierneef Blvd, Shop 7, Meyerton, Gauteng 1961, South Africa', '微型 / 小型',
    ['（无具名 KP：info@handsonsecurity.co.za；Attn: Owner）'],
    '**CCTV 安装商 + 在售 UTEPO 口型 → 集成商 25% B，一页纸一次（STC-028GP $28 / STC-2216GP + STI-054GP；UTEPO 不点名；Attn: Owner）' + ZA + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（D&B 地址 + 名录；CIPC 未取）。')
row('SB-636', 'Marzetek (Pty) Ltd（marzetek.com；**1 查唯一命中 = 南非环境部 DFFE RFQ 000908 (24/25) 打印耗材投标收到名单第 50 位「Marzetek (Pty) Ltd」→ 政府投标杂货供应商；地址 / 注册号未得 → 未坐实；官网为托管占位页**）；表内「4+24、4+48 10G 光」；KP Lloyd Thembani Moyo（Sales Engineer）；群发 7 次无回复', 'ZA',
    'ZA · 1 次检索：dffe.gov.za/sites/default/files/tenders/rfq000908.24.25bidsreceived__printercartridges.pdf（50. Marzetek (Pty) Ltd）；其余无命中；2026-10-29', 'https://www.dffe.gov.za/sites/default/files/tenders/rfq000908.24.25bidsreceived__printercartridges.pdf',
    '未取（仅投标名单证实 (Pty) Ltd 存在）', '存续（2024/25 投标在册）', '未取', '(Pty) Ltd', '政府投标综合供应（南非）', '未取', '微型（推定）',
    ['Lloyd Thembani Moyo — Sales Engineer（研究档 KP；procurement@marzetek.com）'],
    '**政府投标杂货供应商 + 官网占位 + 7×0 → 不动（B 保留；来询按分销 20% 报 STC-4424GCPM / STC-448XGGPM + 预付 100%）**' + ZA,
    '不动（投标杂货商 + 7×0）；未坐实（仅投标名单）。')
row('SB-672', 'Netshield (Pty) Ltd（netshieldsa.com；**RocketReach：1994 年成立；10 Pony Street, Concept House, Unit B, Silver Lakes, Pretoria；约 16 人；自研 IoT / UPS / 交换机 / MC / 光纤 / 嵌入式；ZoomInfo：Marien Dreckmeyr Director, National Marketing（2009–）；yellosa 旧址 407 Atterbury Road, Menlo Park, Pretoria，(012) 424-9340**）；CIPC 注册号 1 查未得 → 部分坐实；KP Inus Dreckmeyr（Electrical Engineer & CEO）/ Celia Gagiano；表内「MC SFP 工业 FS」；电话 +27 12 841 0320', 'ZA',
    'ZA · 1 次检索：rocketreach.co/netshield-sa-profile（Established in 1994；10 Pony Street, Concept House, Unit B, Silver lakes, Pretoria；Employees 16；inhouse developed … OEM integrated）+ zoominfo（Marien Dreckmeyr Director, National Marketing；Silver Lakes Rd, Pretoria 0081）+ yellosa（NETSHIELD (PTY) LTD.；407 Atterbury Road, Menlo Park；(012)424-9340）；CIPC 未得；2026-10-29', 'https://rocketreach.co/netshield-sa-profile_b4508966fc78962b',
    '未取（CIPC 注册号 1 查未得）', '营业中（官网 + 企业库）', '1994', '(Pty) Ltd', '自有品牌网络 / 电源 / IoT 制造（比勒陀利亚）', '10 Pony Street, Concept House, Unit B, Silver Lakes, Pretoria, Gauteng, South Africa', '小型（约 16 人）',
    ['Inus Dreckmeyr — Electrical Engineer and CEO（研究档 KP；inus@netshieldsa.com）= 收件人', 'Celia Gagiano — 联系人（研究档 KP；celia@netshieldsa.com）', 'Marien Dreckmeyr — Director, National Marketing（ZoomInfo 2026-10-29；无公开邮箱）'],
    '**自有品牌制造商（交换机 / MC 自标）+ CEO 为 KP → 贴标 OEM 30% B，一页纸一次（STI-154GP / STI-288DGGPM $137 + STC-110XGE $65 中性包装 / 贴标 + MOQ 1 + 付费样机；SFP 不供明说）' + ZA + '**；回信 → 加厚',
    '贴标 OEM 30%；一页纸一次（预付 100%）；部分坐实（企业库地址 + 成立年 + 人数 + 职务；CIPC 未取）。')
row('SB-860', 'Basithami Trading and Projects t/a Basithami Technology（basithamitech.com；**官网 contact：10313 c/o Pudi & Tshepe Street, Kagiso Ext 4, Mogale City（克鲁格斯多普）；+27 11 419 3110；claims@ / info@；自述安防安装 20 年；名录另列「电子维修」**）；CIPC 注册号 1 查未得 → 部分坐实；表内「工商业 FS 有 Utepo 的」；群发 15 次无回复；无具名 KP', 'ZA',
    'ZA · 1 次检索：basithamitech.com/contact-us（BASITHAMI TRADING AND PROJECTS Trading as BASITHAMI TECHNOLOGY；10313 c/o Pudi & Tshepe Street Kagiso Ext 4. Mogale City；+27-11-419-3110；20 Years）+ cybo（Electronics repair；Krugersdorp）；CIPC 未得；2026-10-29', 'https://www.basithamitech.com/contact-us/',
    '未取（CIPC 注册号 1 查未得）', '营业中（官网 2020 + 名录）', '约 2000（自述 20 年）', '(Pty) Ltd / 商号（Trading as）', '安防安装 / 家庭自动化 / 电子维修（莫哈莱市）', '10313 c/o Pudi & Tshepe Street, Kagiso Ext 4, Mogale City, Gauteng, South Africa', '微型',
    ['（无具名 KP：info@basithamitech.com）'],
    '**微型安装商 + 15×0 + 无具名 KP → 不动（B 保留）**' + ZA, '不动（微型 + 15×0 + 无 KP）；部分坐实（官网地址 + 电话；CIPC 未取）。')
row('SB-904', 'Nuthill Technologies（nuthill.co.za；**ZoomInfo：31 Boncker St, Middelburg, Mpumalanga；+27 13 246 1140；11–50 人；CEO Abrie Joubert；矿业 / 冶金 / 电气 / 仪表方案（NutProM 监控、DepthMaster、WAGO）；客户 Glencore Coal / South32 / Eskom / Columbus Stainless；findglocal 另址 Stoffberg Road R555, Middelburg**）；CIPC 注册号 1 查未得 → 部分坐实；自建站询盘「7 台 Moxa 工业 8 电口轻管理」；KP Ivanka（accounts@）', 'ZA',
    'ZA · 1 次检索：zoominfo.com/c/nuthill-technologies/464005553（31 Boncker St, Middelburg, Mpumalanga；+27 132461140；CEO Abrie Joubert；11-50；mining, metal, electrical, and instrumentation；Glencore Coal South Africa, South32 Coal, ESKOM）+ findglocal（Stoffberg Road R555 Middelburg）；CIPC 未得；2026-10-29', 'https://www.zoominfo.com/c/nuthill-technologies/464005553',
    '未取（CIPC 注册号 1 查未得）', '营业中（官网 + 企业库）', '未取', '(Pty) Ltd（推定）', '矿业 / 工业自动化与仪表集成（米德尔堡，普马兰加）', '31 Boncker St, Middelburg, Mpumalanga, South Africa', '小型（11–50）',
    ['Ivanka — Accounts（研究档 KP；accounts@nuthill.co.za）= 收件人（Attn: Abrie Joubert, CEO）', 'Abrie Joubert — Chief Executive Officer（ZoomInfo 2026-10-29；无公开邮箱）'],
    '**矿业自动化集成商 + 询盘明确（7 台工业 8 电口轻管理）→ 集成商 25% B，一页纸一次（STI-288GPM $78.9 ×7 一口价 + STI-280GE $46.6 备选；Moxa 不点名；MOQ 1 + 付费样机）' + ZA + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（企业库地址 + 电话 + CEO；CIPC 未取）。')
row('SB-978', 'Eurobyte Technology (Pty) Ltd（eurobyte.co.za；**D&B：Unit 8 Cambridge Commercial Park, 22 Witkoppen Rd, Bryanston / Paulshof, Gauteng 2056；011 234 0142；ICT / 安防 / 网络 / 电源方案分销（在售 PLANET 工业 4 / 5 口 + MC、Ruijie / Huawei / Uniview）；yellosa 2013 年在册**）；CIPC 注册号 1 查未得 → 部分坐实；KP Jacqueline Irshwadhar（Network Product Manager）/ Tiffany Hope', 'ZA',
    'ZA · 1 次检索：dnb.com（EUROBYTE TECHNOLOGY (PTY) LTD；UNIT 8 CAMBRIDGE COMMERCIAL PARK, 22 WITKOPPEN RD BRYANSTON, GAUTENG, 2056）+ yellosa（22 Witkoppen Road, Paulshof 2191；011 234 0142；distributes international brands in the ICT sector）+ goafricaonline（CCTV Distributor, Networking and IT Hardware）；CIPC 未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.eurobyte_technology_(pty)_ltd.f635a8c40b418ebbcf68375205c68200.html',
    '未取（CIPC 注册号 1 查未得）', '营业中（官网 + 企业库）', '未取（名录 2013 在册）', '(Pty) Ltd', 'ICT / CCTV / 网络硬件分销（布莱恩斯顿，豪登）', 'Unit 8 Cambridge Commercial Park, 22 Witkoppen Rd, Bryanston, Gauteng 2056, South Africa', '小型',
    ['Jacqueline Irshwadhar — Network Product Manager（研究档 KP；jacqueline@eurobyte.co.za）= 收件人', 'Tiffany Hope — 联系人（研究档 KP）'],
    '**在售 PLANET 工业 4 / 5 口 + 网络产品经理为 KP → 分销 20% B，一页纸一次（直接对价：STI-054GP / STI-154GP + STC-110XGE $65 + STI-280GE $46.6；MOQ 1 + 付费样机）' + ZA + '**；回信 → 加厚',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（D&B 地址 + 电话；CIPC 未取）。')
