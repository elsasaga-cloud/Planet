# -*- coding: utf-8 -*-
"""第 123 批（T29-U114，2026-10-29）第 1 段 18 户（DZ 2 + KW 2 + EC 2 + EU 国别待核 2 + NZ 2 + NP 2 + OM 2 + JO 2 + BT 1 + MN 1）—— B 池收尾段三（清零）官方登记核实写入 registry。
DZ：国企 EPE SPA 仅名录（signalhire）地址 + 人数；KW：官网 contact 地址（CR ✗）；EC：Telconet RUC 0991327371001（ARCOTEL / BVG 公开件 1 查即得）；
EU 国别待核：EURODIGITAL UAB 立陶宛登记码 300638881（rekvi.lt 1 查即得 → country_fix 立陶宛）、WoMaster 欧洲总部巴塞罗那（官网 about → country_fix 西班牙）；
NZ：Viewtech 公司号 1763634 / NZBN 9429034325599（公开镜像）；SWL = Security Wholesale 2001 Limited（D&B）；NP gmail 0 查；OM 官网页脚 / indeed；JO 官网 about + 名录；BT 官网注册地址；MN 名录 + devex。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 123
F = '2026-10-29'
DZ = '— 阿尔及利亚常规：英文稿（可附法语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方清关；进口许可自理）'
KW = '— 科威特常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 科威特城（买方清关；KUCAS 不声称）'
EC = '— 厄瓜多尔常规：英文稿（可附西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 瓜亚基尔（买方清关）'
EU = '— 欧盟常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP（买方清关；CE / RoHS / REACH）；周四 12–14 当地'
NZ = '— 新西兰常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 奥克兰（买方清关；RCM 不声称）；周二 / 周四 09–11 NZST'
NP = '— 尼泊尔常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方经加尔各答 / 空运清关）'
OM = '— 阿曼常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 马斯喀特（买方清关；TRA 不声称）'
JO = '— 约旦常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 安曼（买方清关；JSMO 不声称）'
BT = '— 不丹常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方经加尔各答 / 空运清关）'
MN = '— 蒙古常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 乌兰巴托（铁路 / 公路；买方清关）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ---------------- DZ 2 ----------------
row('SB-1110', 'Amine Achoura（amineachoura21@gmail.com；+213 669 116 595；**个人 gmail、无公司 → 0 查**）— LinkedIn 来源，2023-09 要 WDM 资料（不供）；1 次跟进 1 次回复', 'DZ',
    '0 查（gmail + 无公司）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '个人', '未知（阿尔及利亚）', '未取', '个人',
    ['Amine Achoura — 联系人（研究档 KP；amineachoura21@gmail.com）'],
    '**需求 WDM（不供）+ 无公司 → 不动（B 保留；来询按集成商 25% 报 STC-228GP）**' + DZ, '不动（产品不对位）；0 查。')
row('SB-331', 'EPE RETELEM SPA（ex-SONATITE；retelem-dz.com；**signalhire 名录：54, Rue Omar Benaissa, Bab El Oued, Alger；200–500 人；ELEC EL DJAZAIR 控股的国有经济公共企业（研究档：1971 年成立，14 个分支）**）；RC / NIF 1 查未得 → 部分坐实；关键数字基础设施集成商（LAN / WAN / 光纤 / 数据中心 / SCADA / 视频监控）；KP Hichem Akchiche（WA 已加；2024 要工业交换机 datasheet，对 2 光 8 PoE 有兴趣）；16 次跟进 3 次回复', 'DZ',
    'DZ · 1 次检索：signalhire.com/companies/epe-retelem-spa（EPE RETELEM SPA；54, Rue Omar Benaissa B.E.O Alger；200-500 employees；retelem-dz.com；更新 2026-09-25）；RC / NIF 未得（CNRC 不开放）；2026-10-29', 'https://www.signalhire.com/companies/epe-retelem-spa',
    '未取（RC / NIF 1 查未得）', '营业中（国企；官网 + 名录）', '1971（SONATITE）', 'EPE SPA（国有经济公共企业）', '网络 / 光纤 / 数据中心 / SCADA 集成（阿尔及尔）', '54, Rue Omar Benaissa, Bab El Oued, Alger, Algeria', '中型（200–500）',
    ['Hichem Akchiche — 联系人（研究档 KP；hichem.akchiche@retelem-dz.com；WA 已加）= 收件人'],
    '**国企集成商（SCADA / 光纤 / 监控）+ 明确兴趣 2 光 8 PoE 工业 → 集成商 25% B，一页纸一次（STI-288DGGPM $137 L2 管理 / STI-288GPM $78.9 非管理 一口价 + MOQ 1 + 付费样机；关键基础设施按单核；法语备注）' + DZ + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（名录地址 + 人数；RC / NIF 未取）。')

# ---------------- KW 2 ----------------
row('SB-117', 'Softline Technology（科威特；Anand Rajendiran；**rajaanand42@gmail.com、无域名 → 0 查**）— 网络工程商（印度裔联系人，2014 起用国际站）；需求 2 光 16 电工业 PoE；2025-07 对 24 / 48 口回 useful，**2025-11 要公司资料与价格（我方欠答）**；WA 已加；14 次跟进 2 次回复', 'KW',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（2025-11 要价）', '—', '未取', '网络工程（科威特）', '未取（+965 9415 7777）', '微型（推定）',
    ['Anand Rajendiran — 联系人（研究档 KP；rajaanand42@gmail.com；WA 已加）= 收件人'],
    '**主动要公司资料 + 价格（欠答）→ 集成商 25% B，一页纸一次（工业 2 光 16 电 PoE 按主表报 + STI-288DGGPM $137 / STC-2216GP 一口价 + 公司一页简介 + MOQ 1 + 付费样机）' + KW + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；0 查。')
row('SB-530', 'Digital Security Systems Est.（DSS；dss-kuwait.com；**官网 contact：1st Floor, Office 15, Ahmad Al Jaber Street, Sharq, P.O. Box 631 Dasman 15457, Kuwait City；+965 2220 0023；epicos 2018：代理 Sensormatic / DSC / American Dynamics / Software House / Cardax；Tiandy 伙伴页同址**）；CR 号 1 查未得 → 部分坐实；表内「工业 FS 和 ONV 深度合作」；KP Majdi Yosef / Dalal Jadallah / Azzam Abbas；群发 15 次无回复', 'KW',
    'KW · 1 次检索：dss-kuwait.com/contactus.php（1st Floor, Office 15, Ahmad Al Jaber Street P.O. BOX: 631 Dasman, Code 15457, Kuwait City, Sharq）+ tiandy.com 伙伴页（00965 222 000 23；Presales@dss-kuwait.com）+ epicos（Digital Security Systems Est.；品牌代理）；CR 未得；2026-10-29', 'http://www.dss-kuwait.com/contactus.php',
    '未取（CR 号 1 查未得）', '营业中（官网 + 伙伴页）', '未取', 'Est.（个人机构 / W.L.L. 待核）', '安防系统集成 / 运维（科威特城）', '1st Floor, Office 15, Ahmad Al Jaber Street, Sharq, P.O. Box 631, Dasman 15457, Kuwait City, Kuwait', '中小型',
    ['Majdi Yosef — 表内联系人（研究档 KP；majdi@dss-kuwait.com）= 收件人', 'Dalal Jadallah — 表内联系人（dalal@dss-kuwait.com）', 'Azzam Abbas — 表内联系人（azzam@dss-kuwait.com）'],
    '**安防 SI（ONV 工业 FS 在用）→ 集成商 25% B，一页纸一次（STI-288DGGPM $137 / STI-288GPM $78.9 工业 2 光 8 PoE 一口价 + STC-2224GP $86 + MOQ 1 + 付费样机；在用品牌不点名）' + KW + '**；15×0 → 再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网地址 + 伙伴页；CR 未取）。')

# ---------------- EC 2 ----------------
row('SB-124', 'TELCONET S.A.（telconet.ec；**RUC 0991327371001；法定代表人 Marion Tomislav Topic Granados（Gerente General）；Dirección Legal Guayaquil, Kennedy Norte, Av. Luis Orrantia SL. 21 y Av. V.H. Sicouret；瓜亚基尔证券交易所登记发行人；ARCOTEL 电信许可（Título Habilitante 1795361）；大型光纤运营商**）→ 坐实；表内「从国内买了很多 SFP」（直采 SFP，不供）；无 KP；群发无互动', 'EC',
    'EC · 1 次检索：bolsadevaloresguayaquil.com/emisores/info-emisor.asp?emicodi=E.87（TELCONET S.A.；RUC 0991327371001；Representante Legal TOPIC GRANADOS MARION TOMISLAV；Dirección Legal Guayaquil Kennedy Norte）+ arcotel.gob.ec 2022-06 公文（RUC 0991327371001；Título Habilitante 1795361）+ ecuadorpapers RUC-SCV 2016（ESTADO ABIERTO）；2026-10-29', 'https://www.bolsadevaloresguayaquil.com/emisores/info-emisor.asp?emicodi=E.87',
    'RUC 0991327371001', '营业中（BVG 发行人 + ARCOTEL 许可）', '未取（1990 年代）', 'S.A.（证券交易所登记发行人）', '光纤电信运营 / 数据中心（瓜亚基尔）', 'Av. Luis Orrantia SL. 21 y Av. V.H. Sicouret, Kennedy Norte, Guayaquil, Ecuador', '大型',
    ['（无 KP：info@telconet.ec）', 'Marion Tomislav Topic Granados — Gerente General / Representante Legal（BVG 2026-10-29；无公开邮箱）'],
    '**大型运营商 + 主需求 SFP（不供）+ 无 KP + 零互动 → 不动（B 保留；供应商准入门槛高，运营商按单核）**' + EC, '不动（大型运营商 + 产品不对位 + 无 KP）；坐实（RUC + 法定代表人 + 法定地址）。')
row('SB-517', 'Ernesto Guevara（**仅 WA 电话 +505 7778 9314 = 尼加拉瓜区号 → 表内「厄瓜多尔」疑误 → country_fix 尼加拉瓜；无邮箱 / 公司 → 0 查**）— 需求 GPON 交换机 + 路由器（均不供）；2024-08 对 10G MC 问不相关产品；18 次推送 1 次实质回复', 'NI',
    '0 查（无邮箱 / 公司；号段 +505 = 尼加拉瓜）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '个人', '未知（尼加拉瓜，按号段）', '未取', '个人',
    ['Ernesto Guevara — WA 联系人（研究档 KP；无邮箱）'],
    '**需求 GPON + 路由器（不供）+ 无公司 → 不动（B 保留；来询按集成商 25% 报 STC-028GP）**', '不动（产品不对位 + 18×1）；0 查；country_fix 尼加拉瓜（号段证据，Simon 可回正）。')

# ---------------- EU 国别待核 2 ----------------
row('SB-196', 'UAB "Eurodigital"（e-shop ExtraDigital.eu / .lt；**rekvi.lt / taurageje.lt：Įmonės kodas 300638881；PVM LT100002890717；Registruota 2007-01-29；Žemaičių g. 31-301, LT-44175 Kaunas；Vadovas Saulius Razlevičius；Sodra 2026-04 员工 13；「active, has employees and sufficient capital」；IRT 设备批发**）→ 坐实；表内区域「欧洲（国别未填）」→ country_fix 立陶宛；泛欧 Dahua CCTV 分销 / 光伏 / EV 充电电商；KP Austėja（info@）；11 次跟进 1 次回复', 'LT',
    'LT · 1 次检索：rekvi.lt/en/companies/view/62317（UAB "Eurodigital"；kodas 300638881；PVM LT100002890717；Vadovas Saulius Razlevičius；Žemaičių g. 31-301, Kaunas；+370 603 88188；active）+ taurageje.lt（Registruota 2007-01-29；Darbuotojai 12–13；IRT įrangos didmeninė prekyba）；2026-10-29', 'https://rekvi.lt/en/companies/view/62317',
    'Įmonės kodas 300638881；PVM LT100002890717', '存续（active；Sodra 2026-04 员工 13）', '2007-01-29', 'UAB（有限责任公司）', 'ICT 设备批发 / 电商（考纳斯）', 'Žemaičių g. 31-301, LT-44175 Kaunas, Lithuania', '小型（12–13）',
    ['Austėja — 来信署名人（研究档 KP；info@extradigital.eu）= 收件人', 'Saulius Razlevičius — Vadovas / 董事（rekvi.lt 2026-10-29；无公开邮箱）'],
    '**泛欧 Dahua 分销电商 → 分销 20% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 整箱一口价 + MOQ 1 + 付费样机；CE / RoHS / REACH；在售品牌不点名）' + EU + '**；回信 → 加厚',
    '分销 20%；一页纸一次（预付）；坐实（登记码 + VAT + 成立日 + 地址 + 董事）；country_fix 立陶宛。')
row('SB-560', 'WoMaster Europe（womaster.eu；**官网 about：WoMaster Group 欧洲总部 Barcelona, Spain（欧洲运营 / 技术支持 / 仓库）；业务总部 WoM Asia 新北；集团为 QNAP / HMS / HolyStone 合资；自有 EMS 工厂（SMT / DIP / 老化）；工业以太网交换机 / 工业无线 / 5G 路由品牌**）；西班牙 / 台湾登记号 1 查未得 → 部分坐实；表内区域「欧洲」→ country_fix 西班牙；表内「工业 FS SFP 1U 机架工业 / 工业串口 / 自己的 logo」；群发 16 次无回复', 'ES',
    'EU · 1 次检索：womaster.eu/about.php（offices in Spain (Barcelona), Taiwan (New Taipei), and China；WoMaster Europe headquarters in Spain Barcelona；WoM EMS over 20 years）+ womtek.com/aboutus（joint venture of QNAP Group, HMS Industrial Networks, HolyStone Group；Headquartered in Taiwan）；登记号未得；2026-10-29', 'https://www.womaster.eu/about.php',
    '未取（ES / TW 登记号 1 查未得）', '营业中（集团官网）', '未取（集团 20+ 年）', 'S.L.（欧洲公司；推定）', '工业网络设备品牌（巴塞罗那 / 新北）', 'Barcelona, Spain（欧洲总部；街道未取）', '中型（集团）',
    ['（欧洲站未具名：info@womaster.eu）'],
    '**同行品牌 + 自有 EMS，表内「自己的 logo」→ 贴标 OEM 30% B，最后一次一页纸（STI-288DGGPM $137 / STI-0240GE $130 贴标补 SKU + 贴标 MOQ + 付费样机；1U 机架工业 / 串口服务器不供明说；竞品不点名）' + EU + '**；16×0 → 再无回声 → 不动',
    '贴标 OEM 30%（同行补 SKU）；最后一次一页纸（预付）；部分坐实（官网总部 + 集团背景；登记号未取）；country_fix 西班牙。')

# ---------------- NZ 2 ----------------
row('SB-316', 'Security Wholesale 2001 Limited（DBA SWL；swl.co.nz；**D&B：Key Principal Andrew Eric Jones；922 Great South Rd, Penrose, Auckland 1061；cylex：基督城分部 4/91 Byron St, Christchurch 8023；ZoomInfo：Andrew Jones Managing Director**）；NZBN 1 查未得 → 部分坐实；100% 新西兰本土安防批发（Provision-ISR / Ajax / DSC / Kantech；表内「有 Utepo 的」）；KP Jabe Hura（Technical Sales）；1 次跟进无回复', 'NZ',
    'NZ · 1 次检索：dnb.com（SECURITY WHOLESALE 2001 LIMITED；DBA SWL；Key Principal Andrew Eric JONES；922 Great South Rd Penrose Auckland 1061）+ zoominfo（Andrew Jones Managing Director at Swl）+ cylex.co.nz（SWL Christchurch 4/91 Byron St；03-595 1372）；NZBN 未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.security_wholesale_2001_limited.ae524adacb574def950a62011c209631.html',
    '未取（NZBN 1 查未得；法定名 Security Wholesale 2001 Limited）', '营业中（D&B + 官网）', '2001（名称推定）', 'NZ Limited Company', '安防批发（奥克兰 / 基督城）', '922 Great South Road, Penrose, Auckland 1061, New Zealand', '小型',
    ['Jabe Hura — Technical Sales Representative（研究档 KP；jabe@swl.co.nz）= 收件人', 'Andrew Eric Jones — Managing Director / Key Principal（D&B + ZoomInfo 2026-10-29；trade@swl.co.nz）'],
    '**安防批发（Utepo 在售）→ 分销 20% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 整箱一口价 + MOQ 1 + 付费样机；中性包装；在售品牌不点名）' + NZ + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（D&B 法定名 + 地址 + MD；NZBN 未取）。')
row('SB-319', 'VIEWTECH LIMITED（viewtech.co.nz；**NZ Companies 镜像：Company No. 1763634；NZBN 9429034325599；Incorporated 2006-02-01；Status Registered；Director Darren Jenkinson；Registered address Unit 4, 211 Ferry Rd, Christchurch 8011；营业地 97 Wordsworth St, Sydenham, Christchurch 8023；0800 888 324；LinkedIn 2–10 人**）→ 坐实；CCTV 固定 + 车载方案 + 安防批发（Milesight / Dahua / Teltonika / Utepo）；KP Matthew Peacey（Commercial Manager）；1 次跟进无回复', 'NZ',
    'NZ · 1 次检索：newzealand-company.com/co/viewtech-limited（Company Number 1763634；Incorporated 01 Feb 2006；Registered；Directors Darren JENKINSON；Unit 4, 211 Ferry Rd, Christchurch 8011）+ 镜像（NZBN 9429034325599）+ linkedin（Founded 2006；2-10；97 Wordsworth St Christchurch 8023；Darren Jenkinson Managing Director）；2026-10-29', 'https://newzealand-company.com/co/viewtech-limited',
    'Company No. 1763634；NZBN 9429034325599', 'Registered（NZ Companies 镜像）', '2006-02-01', 'NZ Limited Company', 'CCTV / 车载安全 / 安防批发（基督城）', '97 Wordsworth Street, Sydenham, Christchurch 8023, New Zealand（注册地 Unit 4, 211 Ferry Rd, Christchurch 8011）', '微型（2–10）',
    ['Matthew Peacey — Commercial Manager（研究档 KP；matthew@viewtech.co.nz）= 收件人', 'Darren Jenkinson — Managing Director / Director（Companies 镜像 + LinkedIn 2026-10-29；darren@viewtech.co.nz）'],
    '**安防批发（Utepo / Dahua 在售）→ 分销 20% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 一口价 + MOQ 1 + 付费样机；车载 / 宽温用 STI-054GP；在售品牌不点名）' + NZ + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；坐实（公司号 + NZBN + 成立日 + 状态 + 董事）。')

# ---------------- NP 2 ----------------
row('SB-334', 'DG Enterprises（尼泊尔；Dhan Bahadur；**dtechnic02@gmail.com、无域名 → 0 查**）— 小型网络商；需求 5 电口工业（曾指名竞品口型）；2024-06 收 228 商用 PoE 资料；WA 已加；13 次跟进 1 次回复', 'NP',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '未取', '网络设备（尼泊尔）', '未取（+977 986 863 1483）', '微型（推定）',
    ['Dhan Bahadur — 联系人（研究档 KP；dtechnic02@gmail.com；WA 已加）= 收件人'],
    '**明确口型 5 电口工业 → 集成商 25% B，WA 一页纸一次（STI-054GP 4 PoE + 1 GE / STI-280GE $46.6 8 GE 工业 一口价 + MOQ 1；竞品不点名）' + NP + '**；再无回声 → 不动',
    '集成商 25%；WA 一页纸一次（预付 100%）；0 查。')
row('SB-335', 'Golden Hub Nepal Pvt. Ltd.（Chhatra Puri；**pchhatra02@gmail.com、无域名 → 0 查**）— 网络商；需求 2 光 10 电；2025-11 收 10G MC 资料；WA 已加；14 次跟进 1 次回复', 'NP',
    '0 查（gmail + 无域名；OCR 不开放）；2026-10-29', '', '0 查', '互动中（1 次）', '—', 'Pvt. Ltd.（表内）', '网络设备（尼泊尔）', '未取（+977 985 284 9417）', '微型（推定）',
    ['Chhatra Puri — 联系人（研究档 KP；pchhatra02@gmail.com；WA 已加）= 收件人'],
    '**明确口型 2 光 10 电 → 集成商 25% B，WA 一页纸一次（STI-288DGGPM $137 2 SFP + 8 PoE 管理 / STC-228GP $33 一口价 + MOQ 1；一句话问是否要 PoE）' + NP + '**；再无回声 → 不动',
    '集成商 25%；WA 一页纸一次（预付 100%）；0 查。')

# ---------------- OM 2 ----------------
row('SB-376', 'GLOBAL SECURITY TECHNOLOGY LLC（品牌 Leamratech；leamratech.com；**官网：Flat 609–606, 6th floor, Business Center Building, Al Khuwair, 3341 Way, Muscat；+968 2448 0700；info@ / support@；生物识别 / CCTV / LED 大屏（住房部项目）**）；CR 号 1 查未得 → 部分坐实；自建站询盘「工业百兆 1 光 4」（百兆不供 → 千兆对位）；KP Ahmar（工程部）；WA 无实质回复', 'OM',
    'OM · 1 次检索：leamratech.com（GLOBAL SECURITY TECHNOLOGY LLC；Flat 609 -606, 6th floor Business center building Al Khuwair, Muscat；24480700）+ leamratech.com/contact-us（info@leamratech.com）+ cybo（support@；9413 2835）；CR 未得；2026-10-29', 'https://leamratech.com/',
    '未取（CR 号 1 查未得）', '营业中（官网 2026）', '未取', 'LLC', '安防 / 生物识别 / LED 显示集成（马斯喀特）', 'Flat 609–606, 6th Floor, Business Center Building, Al Khuwair, 3341 Way, Muscat, Oman', '小型',
    ['Ahmar — 工程部（研究档 KP；a.engineering@leamratech.com）= 收件人'],
    '**自站询盘 1 光 4 工业 → 集成商 25% B，一页纸一次（STI-154GP 1 SFP + 1 GE + 4 PoE / STI-054GP 一口价 + MOQ 1 + 付费样机；百兆版不供明说）' + OM + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网法定名 + 地址；CR 未取）。')
row('SB-689', 'TIS Control Oman（mkseoman.com / tiscontrol.com；**1 查仅 indeed 招聘（2026-04，hr@mkseoman.com，Muscat，智能家居 / 弱电）→ 未坐实（地址 / CR 未得）**）；智能家居 / 酒店自动化品牌经销体系；阿里询盘「导轨式 PoE 管理 / 非管理」；KP Mamunur Rashid；1 次跟进无回复', 'OM',
    'OM · 1 次检索：om.indeed.com（Smart Home Engineer — TIS Control Oman, Muscat；hr@mkseoman.com；2026-04-11）；地址 / CR 未得；2026-10-29', 'https://om.indeed.com/q-smart-technologies-jobs.html',
    '未取（1 查无地址 / CR）', '营业中（2026-04 招聘）', '未取', 'LLC（推定）', '智能家居 / 弱电（马斯喀特）', '未取（Muscat, Oman）', '小型',
    ['Mamunur Rashid — 联系人（研究档 KP；mamun@mkseoman.com）= 收件人'],
    '**阿里询盘导轨式 PoE 管理 / 非管理 → 集成商 25% B，一页纸一次（STI-288DGGPM $137 管理 + STI-288GPM $78.9 非管理 + STI-054GP 一口价 + MOQ 1 + 付费样机）' + OM + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；未坐实。')

# ---------------- JO 2 ----------------
row('SB-482', 'Khaleel Electro Mechanical Est.（KEME-TEC；مؤسسة خليل قطناني للكهروميكانيك；keme-tec.com；**官网 about：2008 年成立；Al-Hizam Street, Abu Alanda, Amman；+962 79 780 0706 / 78 780 0706；Info@；ZoomInfo：+962 6 475 3322，<$5M；工业自动化 / 变频 / 发电机组 / SCADA 供应与维护**）；商业登记号 1 查未得 → 部分坐实；阿里 RFQ「商业 24 口管理」；KP Rateb Mahmoud（project manager）；未跟进', 'JO',
    'JO · 1 次检索：keme-tec.com/about-us（KHALEEL ELECTRO MECHANICAL EST. (KEME-TEC) was founded in 2008；Al-Hizam Street - Abu Alanda - Amman；0797800706；Info@keme-tec.com）+ zoominfo（+962 64753322；<$5 Million）；登记号未得；2026-10-29', 'https://keme-tec.com/about-us/',
    '未取（商业登记号 1 查未得）', '营业中（官网 2023 + ZoomInfo）', '2008', 'Est.（个人机构）', '工业自动化 / 机电（安曼）', 'Al-Hizam Street, Abu Alanda, Amman, Jordan', '小型',
    ['Rateb Mahmoud — Project Manager（研究档 KP；projects@keme-tec.com）= 收件人'],
    '**RFQ 24 口管理 → 集成商 25% B，一页纸一次（STC-4424GCPM $165 24 PoE + 4 SFP L2+ / 24 GE 非 PoE 管理版 按主表 一口价 + MOQ 1 + 付费样机；一句话问是否要 PoE）' + JO + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网成立年 + 地址；登记号未取）。')
row('SB-785', 'Smart Systems For Computers（شركة الأنظمة الذكية；smartsystems.jo；**jordanyp：1991 年成立；Jawhara Halima Complex, 6 Wasfi Al Tal St (Gardens), Amman；+962 6 562 7771；16–25 人；prospeo：Owner Motaz Alsharif（= 表内 KP ✓）；电脑 / 配件门店 + 网络**）；登记号 1 查未得 → 部分坐实；表内「大口 FS / BDCOM / switch」；未跟进', 'JO',
    'JO · 1 次检索：jordanyp.com/company/356802（Smart Systems For Computers；established 1991；Jawhara Halima Complex, 6 Wasfi Al Tal St, Amman；+962-6-5627771；16-25）+ prospeo.io/c/smart-systems（Motaz Alsharif Owner）+ jordanict.com；登记号未得；2026-10-29', 'https://www.jordanyp.com/company/356802/Smart_Systems',
    '未取（商业登记号 1 查未得）', '营业中（名录 + 官网）', '1991', 'L.L.C.（推定）', '电脑 / 网络设备零售与集成（安曼）', 'Jawhara Halima Complex, 6 Wasfi Al Tal Street (Gardens), Amman, Jordan', '小型（16–25）',
    ['Motaz Alsharif — Owner（prospeo 2026-10-29 吻合；研究档 KP；motaz@smartsystems.jo）= 收件人'],
    '**门店 + 集成、大口交换机常购（BDCOM 在供）→ 分销 20% B，一页纸一次（STC-4424GCPM $165 / STC-424XGGPM-280W $198 / STC-448XGGPM $335 一口价 + MOQ 1 + 付费样机；在供品牌不点名）' + JO + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（名录成立年 + 地址 + Owner）。')

# ---------------- BT 1 ----------------
row('SB-035', 'NANO（nano.bt；**官网：不丹三家持独立国际网关牌照的 ISP 之一（DWDM / 光纤；ISP + 托管安全 + 企业 IT）；Registered Address IT Park, PO Box 633, Wangchuktaba, Babesa, Thimphu；+975 2 330330；MD Tshering Norbu（曾任 Thimphu TechPark Ltd 董事、.BT ccTLD 技术联系人）**）；公司注册号 1 查未得 → 部分坐实；表内国别「卡塔尔」已改不丹；KP Sonam Rinchen（WA 已加；要收发器 / SFP / PoE 交换机）；19 次跟进 1 次回复', 'BT',
    'BT · 1 次检索：nano.bt（one of the three fully-fledged and licensed ISPs in Bhutan；Registered Address: IT Park, PO Box 633, Wangchuktaba, Babesa, Thimphu；+975 2 330330；Tshering Norbu Managing Director）+ cbinsights / datacenterjournal（Wangchuktaba, Thimphu）；注册号未得；2026-10-29', 'http://www.nano.bt/',
    '未取（公司注册号 1 查未得；持牌 ISP）', '营业中（官网 + 数据中心名录）', '2017（入市）', 'Pvt. Ltd.（推定）', 'ISP / 托管安全 / 企业网络（廷布）', 'IT Park, PO Box 633, Wangchuktaba, Babesa, Thimphu, Bhutan', '微型（约 11）',
    ['Sonam Rinchen — 表内联系人（研究档 KP；sonam@nano.bt；WA 已加）= 收件人', 'Tshering Norbu — Managing Director（官网 2026-10-29；无公开邮箱）'],
    '**持牌 ISP 自用 + 企业客户 → 集成商 25% B，一页纸一次（STC-4424GCPM $165 L2+ / STC-424XGGPM-280W $198 汇聚 + STC-228GP $33 接入 一口价 + MOQ 1；SFP / 收发器不供明说）' + BT + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网注册地址 + MD；注册号未取）。')

# ---------------- MN 1 ----------------
row('SB-047', 'Topica LLC（Топика ХХК；topica.mn；**devex：2005 年由电子 / IT 工程师创立；Chingeltei District, 1st Khoroo, Office 3A, Ulaanbaatar；+976 7012 5001 / 5002；admin@ / info@；LuxDev 医院 IT 设备中标 ×3；网店 + 分销（MikroTik / Cisco / Milesight / Schneider / ZKTeco / Ruijie / D-Link / Huawei）**）；注册号 1 查未得 → 部分坐实；**2025-11 对 24 PoE 回「需要 16 port 的」（我方欠答）**；KP info@（回复签名 Bayar）；1 次跟进 1 次回复', 'MN',
    'MN · 1 次检索：devex.com/organizations/topica-40614（Topica LLC established in 2005；Chingeltei District 1R-Khoroo Office 3A, Ulaanbaatar；LuxDev lots）+ miniihot.com（Топика ХХК；70125001；admin@topica.mn）+ zoominfo（+976 70125002；51-200）；注册号未得；2026-10-29', 'https://www.devex.com/organizations/topica-40614',
    '未取（蒙古注册号 1 查未得）', '营业中（名录 + 网店）', '2005', 'ХХК / LLC', '网络 / 电气设备网店 + 分销 + 系统集成（乌兰巴托）', 'Office 3A, 1st Khoroo, Chingeltei District, Ulaanbaatar, Mongolia', '中小型（名录 51–200 偏高）',
    ['Bayar — 回信署名人（研究档 KP；info@topica.mn）= 收件人'],
    '**★ 回信点名「16 port」（欠答）→ 分销 20% B，一页纸（STC-2216GP 16 PoE + 2 SFP $63–76 / 16 口管理版 按主表 / STC-2224GP $86 一口价 + MOQ 1 + 付费样机；在售品牌不点名）' + MN + '**；回信即升 A 候选',
    '分销 20%；一页纸（预付 100%）；部分坐实（名录成立年 + 地址；注册号未取）；★ 回信即升。')
