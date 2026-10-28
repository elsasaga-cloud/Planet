# -*- coding: utf-8 -*-
"""第 119 批（T29-U112，2026-10-28）第 2 段 10 户（SA 池前 10）—— 官方登记核实写入 registry（SA 路径首测：CR 号 1 查不出；可得 = 官网 contact + ZoomInfo / RocketReach / 领英；6 户实为阿联酋实体 → country_fix 阿联酋）。时限压缩版。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 119
F = '2026-10-28'
SA = '— 沙特常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP（买方清关；SASO / SABER 不声称）'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜（买方清关；TDRA / ESMA 不声称）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

row('SB-917', 'Torque Automation Systems FZE（torqsys.com；**P.O. Box 121718, Sharjah + Sheikh Zayed Rd, Dubai 办公室；+971 6 557 9973 / +971 4 432 9204；自动化控制承包商（PLC / RTU / SCADA / DCS）**）；表内 KP Arjun Muralidharan 邮箱域 = **Fuzzy Logic Equipment Trading Ltd（Building 280, Taweelah, KIZAD Free Zone, Abu Dhabi；+971 54 585 1777 = 表内电话 ✓；水 / 污水 / 工业厂站 SCADA、100+ 项目）**→ 两家均阿联酋 → country_fix 阿联酋；牌照号未得 → 部分坐实；7 次跟进无实质回复', 'AE',
    'AE · 1 次检索：fuzzylogicautomation.com（Fuzzy Logic Equipment Trading Ltd, headquartered in Abu Dhabi；Building Number 280 Taweelah, Kizad Free Zone；+971 545851777；SCADA / PLC / UPS）+ zoominfo（Torque Automation；Sheikh Zayed Rd, Dubai；+971 44329204）+ abc-gcc（Torque Automation Systems FZE；P.O Box 121718 Sharjah；sales@torqsys.com）；2026-10-28', 'https://www.fuzzylogicautomation.com/',
    '未取（FZE / Ltd；牌照号 1 查未得）', '营业中（两官网在）', '未取', 'FZE（Torque）/ Ltd（Fuzzy Logic，KIZAD）', '工业自动化 / SCADA 承包（阿布扎比 / 沙迦 / 迪拜）', 'Building 280, Taweelah, KIZAD Free Zone, Abu Dhabi, UAE（Torque：P.O. Box 121718 Sharjah）', '小型',
    ['Arjun Muralidharan — 项目 / 技术（研究档 KP；arjun.murali@fuzzylogicautomation.com；+971 54 585 1777）'],
    '**水 / 污水 SCADA 项目型（关键基础设施边缘）+ 7×0 → 不动（B 保留；国别更正阿联酋）**' + AE,
    '不动（项目型 + 7×0）；部分坐实（两官网 + 企业库；牌照号未取）；country_fix 阿联酋。')
row('SB-818', '沙特个人 / 小商户买家（gmail + 05x 手机；WA 已加；**0 查**）— 需求「2 光 16 管理 ×4 台」；23 次推送 1 次实质回复', 'SA',
    '0 查（gmail + 无公司名）；2026-10-28', '', '0 查', '互动中（1 次）', '—', '个人', '小型买家（沙特）', '未取', '个人',
    ['（研究档无 KP：mdirphanmdirphan151@gmail.com；WA 已加）'],
    '**0 查 + 个人 → 不动（B 保留；WA 来询即按集成商 25% 报 STI-288DGGPM ×4，预付 100%）**' + SA, '不动（个人）；0 查。')
row('SB-561', 'Zoom Line Networks Technology（zoomlinenetwork.com；**联系电话全为迪拜 +971 4 325 7866 / +971 55 378 6444；KSA 页面为 SEO 分页、无沙特地址 → country_fix 阿联酋；法人名 / 牌照号 1 查未得 → 部分坐实**）— IT / 网络 / 安防分销（TP-Link / Ubiquiti / MikroTik / Cisco / Fortinet；专页「Industrial Switches Distributor」+ 光纤 / 熔接机 / IP PBX 分销 KSA 页）；KP Mohammad Faisal（BDM）', 'AE',
    'AE · 1 次检索：zoomlinenetwork.com/fiber-optics-distributor-ksa 等 KSA 页（+971 55 378 6444；+971 4 325 7866；sales@zoomlinenetwork.com；leading supplier of networking solutions in Saudi Arabia (KSA)）；法人 / 地址未得；2026-10-28', 'https://zoomlinenetwork.com/fiber-optics-distributor-ksa/',
    '未取（牌照号 1 查未得）', '营业中（官网 2025）', '未取', 'LLC / FZ（推定）', 'IT / 网络 / 安防分销（迪拜；面向 KSA）', '未取（Dubai, UAE）', '小型',
    ['Mohammad Faisal — Business Development Manager（研究档 KP；faisal@zoomlinenetwork.com）= 收件人'],
    '**自称工业交换机分销商、BDM 为 KP → 分销 20% B，一页纸一次（STI-288DGGPM / STI-488DGGPM / STI-154GP + 商用 STC-2224GP / 4424GCPM 一口价 + MOQ 1 + 付费样机；DAP 迪拜）' + AE + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网电话；法人 / 地址未取）；country_fix 阿联酋。')
row('SB-788', 'Telecom Special Solutions (TSS)（tss-e.com；**总部 Prince Faisal Bin Fahad Road, Al Moosa Building, Al Khobar；+966 13 846 8882；2012 年成立（自述 16+ 年）；合伙企业；11–50 / 51–200 人（口径不一）；NEOM 核准 ICT 与基础设施承包商；分支利雅得 / NEOM；CR 号 1 查未得 → 部分坐实**）— 数据中心 / MEP / 安防 / 电信 turnkey 承包（SOC / NOC、网络、CCTV、IPTEL、IPTV、消防）；KP Eng. Murad = ZoomInfo「Murad Abusal, Senior Manager, Accounts & Projects」✓；需求 工业带光口交换机 + SFP', 'SA',
    'SA · 1 次检索：linkedin.com/company/telecom-special-solutions-tss（MEP, Data Center Technology Contracting … Approved NEOM ICT & Infrastructure Contractor；Khobar, Riyadh, NEOM；Partnership；Founded 2012；51-200）+ zoominfo（Prince Fisal Bin Fahad Road Al Moosa Bld, Khobar；+966 138468882；11-50；Murad Abusal Senior Manager, Accounts & Projects）；CR 未得；2026-10-28', 'https://www.linkedin.com/company/telecom-special-solutions-tss',
    '未取（CR 1 查未得）', '营业中（领英 + 企业库）', '2012', '合伙企业（领英口径）', '数据中心 / 电信 / 安防 turnkey 承包（Al Khobar；利雅得 / NEOM）', 'Prince Faisal Bin Fahad Road, Al Moosa Building, Al Khobar, Saudi Arabia', '小型（11–50；自报 51–200）',
    ['Eng. Murad (Murad Abusal) — Senior Manager, Accounts & Projects（研究档 KP；murad@tss-e.com；ZoomInfo 吻合）= 收件人'],
    '**东部省 turnkey 承包商、项目经理为 KP、需求明确（工业光口交换机）→ 集成商 25% B，一页纸一次（STI-288DGGPM $137 / STI-488DGGPM $147 + STC-4424GCPM 一口价；SFP 不做明说；MOQ 1 + 付费样机）' + SA + '**；NEOM / 政府项目按单核；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（领英 + ZoomInfo：总部 + 电话 + 成立年 + KP 职务；CR 未取）。')
row('SB-577', 'MetaWorld Computers LLC（metaworldcomputers.com；**Deyaar Building, Office 331, Damascus Street, Al Qussais Industrial Area 1, Dubai；+971 4 353 7555 / +971 56 213 4555；官网自列 LLC → country_fix 阿联酋；牌照号未得 → 部分坐实**）— 光纤 / 连接产品 + ELV / 安防 / 电信设备供应（自有「Metacom」光纤产品线；500+ 客户自述）；无 KP（info@）；3 次跟进无回复', 'AE',
    'AE · 1 次检索：metaworldcomputers.com/contact-us（MetaWorld Computers LLC；Damascus Street, office 331, Deyaar Building, Al Qussais, Dubai；+971 56 2134555；sales@ / info@）+ 首页（+971 4 3537555；ELV, Security Surveillance and Telecom Equipments）+ /fiberproducts（Metacom Fiber Products）；2026-10-28', 'https://www.metaworldcomputers.com/contact-us.html',
    '未取（LLC；牌照号 1 查未得）', '营业中（官网在）', '未取', 'LLC', '光纤 / 连接 / ELV / 安防设备供应（Al Qussais, Dubai）', 'Deyaar Building, Office 331, Damascus Street, Al Qussais Industrial Area 1, Dubai, UAE', '小型',
    ['（研究档无 KP：info@metaworldcomputers.com）'],
    '**无 KP + 3×0 + 光纤为主 → 不动（B 保留；国别更正阿联酋；若其 Metacom 自有线要交换机再按贴标 30% 报）**' + AE,
    '不动（无 KP + 3×0）；部分坐实（官网：法定后缀 + 地址 + 电话）；country_fix 阿联酋。')
row('SB-706', 'Easy World Automation L.L.C（eWorld；eworldme.com；**2002 年成立；总部 P.O. Box 29505, Office 204, Building 1, Emaar Business Park, Sheikh Zayed Road, Dubai；+971 4 447 1137；分支 Al Khobar（Office 2-5, Al Mukhaizeem Tower, 6248 Prince Turkey St；+966 13 850 6010）/ Riyadh（Office 104, Bldg 6, Imam Abdullah Ibn Saud St；+966 11 275 1110）/ Muscat；总部迪拜 → country_fix 阿联酋；牌照号未得 → 部分坐实**）— **Moxa 中东领先分销商（近 20 年，价格匹配保证）**+ 工业数据通信 / 自动化 / 电信 VAD；KP Mohsen Nejadi（COO）/ Akram Jafari（Sales Manager）', 'AE',
    'AE · 1 次检索：moxa.eworldme.com contact（Easy World Automation LLC (eworld) is the leading distributor of Moxa … Middle East；P.O. Box 29505, Office 204, Building no.1, Emaar Business Park, Sheikh Zayed Road, Dubai；+971 4 447 1137）+ eworldme.com/PARTNERS/MOXA（Al Khobar / Riyadh / Muscat 办公室）+ 产品页页脚（established in 2002）；2026-10-28', 'https://eworldme.com/PARTNERS/MOXA',
    '未取（L.L.C；牌照号 1 查未得）', '营业中（官网 2026）', '2002', 'L.L.C（迪拜）+ KSA / 阿曼分支', '工业数据通信 / 自动化 VAD（Moxa 官方分销）（Dubai；Al Khobar / Riyadh / Muscat）', 'Office 204, Building 1, Emaar Business Park, Sheikh Zayed Road, Dubai, UAE (P.O. Box 29505)', '中小',
    ['Mohsen Nejadi — Chief Operating Officer（研究档 KP；m.nejadi@eworldme.com）', 'Akram Jafari — Sales Manager（研究档 KP）'],
    '**原厂（Moxa）官方分销 = 同行渠道 + 无 OEM 诉求 → 不动（B 保留；国别更正阿联酋；若提出自有品牌 / 低价补位线再按贴标 OEM 30% 报）**' + AE,
    '不动（原厂官方分销）；部分坐实（官网：成立年 + 总部 + 分支 + 电话；牌照号未取）；country_fix 阿联酋。')
row('SB-451', '(e-Saudi) Electronic Saudi Network（e-saudi.net / e-saudi.net.sa；**2001 年成立；利雅得 Abdallah Bahamdan St, Suleimaniya（ZoomInfo）+ 吉达分支；11–50 / 14 人、营收约 $1.4M（RocketReach）；CR 号 1 查未得 → 部分坐实**）— 远程自动化 / 控制与通信 + 固定宽带连接（电信设备制造 / 分销 口径）；KP Saeed Mohammed = RocketReach「Operation Manager / Business Development Manager（2005 至今）」✓；表内 1 次跟进有回复（要 Catalog）', 'SA',
    'SA · 1 次检索：rocketreach.co/e-saudi-electronic-saudi-network-profile（specialized in Remote Automation, Control and Communication. Fixed broadband connectivity；based in Riyadh；Founded 2001；14 employees；$1.4M）+ rocketreach Saeed Mohammed（Operation Manager @ Electronic saudi network 2005-now）+ zoominfo（Abdallah Bahamdan St Suleimaniya, Riyadh；11-50；Telecommunication Equipment）；CR 未得；2026-10-28', 'https://rocketreach.co/e-saudi-electronic-saudi-network-profile_b4438538fdf7a71a',
    '未取（CR 1 查未得）', '营业中（企业库）', '2001', '未取（沙特公司）', '远程自动化 / 通信 / 宽带连接（Riyadh；吉达分支）', 'Abdallah Bahamdan St, Suleimaniya, Riyadh, Saudi Arabia', '小型（11–50）',
    ['Saeed Mohammed — Operation Manager / Business Development Manager（研究档 KP；saeed@e-saudi.net；RocketReach 吻合）= 拍板人 / 收件人'],
    '**25 年远程自动化 / 通信方案商、运营经理本人回过信 → 集成商 25% B，一页纸一次（远端站点 STI-154GP / STI-288DGGPM 宽温 + 机房 STC-4424GCPM 一口价 + 3 年保 + MOQ 1 + 付费样机；opener 引其要 Catalog）' + SA + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（企业库：成立年 + 地址 + KP 职务；CR 未取）。')
row('SB-685', 'Techsouq Computers L.L.C.（techsouq.com；**迪拜：Bayan Business Center, Dubai Investments Park 1（旧址 Al Abbas Bldg, Khalid Bin Al Waleed Rd；P.O. Box 27570）；+971 4 355 0600；MD Ahmad Pervez（2009 至今，ZoomInfo）；表内误归沙特（沙特为分站）→ country_fix 阿联酋；牌照号未得 → 部分坐实**）— 老牌 IT 电商（1999 起；约 8 人；「难找的 IT 产品」采购；政府 / 企业 / 消费者）；表内兴趣 MC / 机架 / 周边，2024-09 对电源转换器回 interesting；KP Ahmad Pervez（MD）/ Shifan Shivani（Co-Founder）', 'AE',
    'AE · 1 次检索：resource.geospatialworld.net（Techsouq Computers L.L.C.；online retailer；Managing Director Ahmad Pervez；Bayan Business Center, Dubai Investments Park First）+ zoominfo（Ahmad Pervez Managing Director 2009-present；Al Abbas Bldg Khalid Bin Al Waleed Rd；27570）+ apnagulf（PO Box 27570；+97143550600）；2026-10-28', 'https://resource.geospatialworld.net/company/techsouq-computers-llc',
    '未取（L.L.C.；牌照号 1 查未得）', '营业中（官网 + 企业库）', '1999（自述）/ 2009（MD 任期）', 'L.L.C.（迪拜）', 'IT / 电子产品电商（Dubai Investments Park）', 'Bayan Business Center, Dubai Investments Park 1, Dubai, UAE (P.O. Box 27570)', '微型（约 8 人）',
    ['Ahmad Pervez — Managing Director（研究档 KP；ahmad@techsouq.com；ZoomInfo 吻合）= 拍板人 / 收件人', 'Shifan Shivani — Co-Founder（研究档 KP；info@）= 抄送'],
    '**老牌电商、MD 本人回过 interesting → 分销 20% B small，一页纸一次（电商上架：STC-028GP $28 / STC-228GP / STC-2216GP 一口价 + MOQ 1 + 付费样机 + DAP 迪拜；机架 / 周边不做明说）' + AE + '**；再无回声 → 不动',
    '分销 20% small；一页纸一次（预付 100%）；部分坐实（企业库：法定名 + 地址 + MD；牌照号未取）；country_fix 阿联酋。')
row('SB-722', 'Aptvel Global（aptvelglobal.com；**总部 204, Building 3, Arenco Offices, DIP 1, Dubai；+971 4 882 4871 / +971 50 839 4997；5+ 年；美国地址 Fall River MA 为陈列；表内误归沙特 → country_fix 阿联酋；法人 / 牌照号未得 → 部分坐实**）— 电气 / 自动化 / IoT + AV / 家庭影院 / 软件 / 数字媒体 杂业方案商；表内要 PLANET 48 口交换机（指定原厂）、问 bypass；KP Arunima Raj（另一邮箱 klasseducation.com）；WA 无实质回复', 'AE',
    'AE · 1 次检索：aptvelglobal.com（5+ Years；electrical, automation, and IoT solutions；HEADQUARTERS 204, Building 3 Arenco Offices, DIP 1 Dubai；+971 48 824 871；Audio Visual / Automation & Security / Custom Software / Home Cinemas）+ zoominfo（Arenco Business Tower 4 Ofc 115, Dubai；Custom Software & IT Services）；2026-10-28', 'https://aptvelglobal.com/',
    '未取（牌照号 1 查未得）', '营业中（官网 2025）', '约 2020（自述 5+ 年）', 'LLC / FZ（推定）', '电气 / 自动化 / IoT / AV 杂业方案（DIP, Dubai）', '204, Building 3, Arenco Offices, DIP 1, Dubai, UAE', '微型',
    ['Arunima Raj — 表内联系人（研究档 KP；info@aptvelglobal.com；职务未核）'],
    '**需求指定原厂（PLANET 48 口）+ bypass（Saga 无）+ 杂业微型 + WA×0 → 不动（B 保留；国别更正阿联酋）**' + AE,
    '不动（需求不对位 + 微型）；部分坐实（官网 + ZoomInfo）；country_fix 阿联酋。')
row('SB-175', 'M. Al-Barghash Trading & Contracting Company (MBTC)（mbtc.com.sa；**1976 年成立；100% 沙资；总部 Al-Khobar 31952 / P.O. Box 31996 Dammam, Eastern Province；关联 AAM Industrial（ei-telcomlead@ = 电气仪表 / 电信项目组）；1001–5000 人（brandfetch，口径存疑）；CR 号 1 查未得 → 部分坐实**）— 建筑 / 制造 / 油气行业设备与材料供应 + 承包；表内 Project Manager Prabhu Manickam 2024-01「有用但现在没需求」+ Wasi Akthar；WhatsApp 24 次无实质回复', 'SA',
    'SA · 1 次检索：protenders.com（M. Al-Barghash Trading & Contracting Company was established in the year 1976 in Eastern Province … 100% Saudi Owned；Head Office Al-Khobar 31952；P.O. Box 31996 Dammam；www.mbtc.com.sa）+ brandfetch（Year founded 1976；1001-5000 employees；Energy Industry）+ mustakbil（Oil & Energy；Ad Dammam）；CR 未得；2026-10-28', 'https://www.protenders.com/companies/mohammad-al-barghash-trading-construction-company',
    '未取（CR 1 查未得）', '营业中（名录）', '1976', '沙特私营公司（100% 沙资）', '油气 / 建筑设备材料供应 + 承包（Al-Khobar / Dammam）', 'Al-Khobar 31952 / P.O. Box 31996 Dammam, Eastern Province, Saudi Arabia', '大型（口径存疑）',
    ['Prabhu Manickam — Project Manager（研究档 KP；prabhu@mbtc.com.sa）', 'Wasi Akthar — E&I / Telecom lead（研究档 KP；ei-telcomlead@aamindustrial.com）'],
    '**油气项目型大承包商 + 明说没需求 + WA 24×0 → 不动（B 保留；项目来询按集成商 25% 报，预付 100%）**' + SA,
    '不动（项目型 + 24×0）；部分坐实（名录：成立年 + 总部；CR 未取）。')
print('b119 第 2 段 10 written')
