# -*- coding: utf-8 -*-
"""第 122 批（T29-U114，2026-10-29）第 2 段 19 户（UZ 3 + EG 3 + 国别待核 3 + PE 2 + BH 2 + ZW 2 + QA 2 + UG 2）—— 官方登记核实写入 registry（B 池收尾段二）。
UZ：goldenpages.uz / pc.uz 给 ООО + 地址（ИНН 打码，SB-965）；WA / mail.ru 2 户 0 查（1 户电话号段 +7 775 = 哈萨克斯坦 → country_fix）；
EG：无 1 查登记库 → 官网页脚 / ZoomInfo / RocketReach / D&B 补地址 + MD；国别待核 3 户：1 户 .eu 未命中、1 户 gmail 0 查（CENTEC 线索 ★）、1 户域名误配 0 查；
PE：RUC = universidadperu / connectamericas 1 查即得（SB-031）；BH：官网页脚 W.L.L. 法定名 + 地址（SB-033），gmail 老客户 0 查；ZW：Securico 集团公开资料（SB-049），gmail 0 查；
QA：qbusinessgate / doha.directory 给地址 + 成立年（SB-1062）；RocketReach 证 KP 为 CTO（SB-166）；UG：eastafricatenders 登记日 + yellow.ug（SB-110）/ 官网地址（SB-183）。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 122
F = '2026-10-29'
UZ = '— 乌兹别克斯坦常规：英文稿（可附俄语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 塔什干（买方清关；UzStandard 不声称）'
EG = '— 埃及常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方清关；NTRA 不声称）'
PE = '— 秘鲁常规：英文稿（可附西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 利马（买方清关）'
BH = '— 巴林常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 麦纳麦（买方清关；TRA 不声称）'
ZW = '— 津巴布韦常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 哈拉雷（买方清关）'
QA = '— 卡塔尔常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 多哈（买方清关；CRA 不声称）'
UG = '— 乌干达常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 坎帕拉（买方清关；UCC 不声称）'
US = '— 美国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP（买方清关；NDAA / TAA / UL / 船级不声称）；周三 08–10 当地'
KZ = '— 哈萨克斯坦常规：英文稿（可附俄语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 阿拉木图（买方清关；EAC 不声称）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ---------------- UZ 3 ----------------
row('SB-608', 'Marlen Sadybekov（**仅 WA 电话 8 775 748 2644 = +7 775 哈萨克斯坦移动号段 → 表内「乌兹别克斯坦」疑误 → country_fix 哈萨克斯坦；无邮箱 / 公司 → 0 查**）— 兴趣「商业 FS」，2024-04 对 10G MC 回「有 PON 产品吗？」（不供）；20 次推送 1 次实质回复', 'KZ',
    '0 查（无邮箱 / 公司；号段 +7 775 = 哈萨克斯坦）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '个人', '未知（哈萨克斯坦，按号段）', '未取', '个人',
    ['Marlen Sadybekov — WA 联系人（研究档 KP；无邮箱）'],
    '**需求 PON（不供）+ 20×1 + 无公司 → 不动（B 保留；来询按集成商 25% 报 STC-028GP）**' + KZ, '不动（产品不对位 + 20×1）；0 查；country_fix 哈萨克斯坦（号段证据）。')
row('SB-965', '"VIDCOM" ООО / VIDCOM Ltd（vidcom.uz；**goldenpages.uz / pc.uz：100115 Ташкент, Чиланзарский район, ул. Арнасай, кв-л Чиланзар-2, 26；+998 90 900 77 30；info@vidcom.uz；ИНН 30548****（打码）；安防系统商（视频监控 / 门禁 / 消防报警；Dahua / Hikvision / Ajax）**）→ 部分坐实（ООО + 地址；ИНН 未全）；无具名 KP；表内无跟进', 'UZ',
    'UZ · 1 次检索：goldenpages.uz/en/company/?Id=97905（VIDCOM. LTD；TIN 30548****；100115, Tashkent, Chilanzar district, Street Arnasay, block Chilanzar-2, 26；(+99890) 9007730）+ pc.uz/company/124350-vidcom（"VIDCOM" ООО；Системы безопасности；info@vidcom.uz）；2026-10-29', 'https://www.goldenpages.uz/en/company/?Id=97905',
    'ИНН 30548****（名录打码；未全）', '营业中（官网 + 名录 verified）', '未取', 'ООО（有限责任公司）', '安防系统分销 / 安装（塔什干）', 'ул. Арнасай, кв-л Чиланзар-2, 26, Чиланзарский район, Ташкент 100115, Uzbekistan', '小型',
    ['（无具名 KP：info@vidcom.uz；Attn: Отдел закупок / Purchasing）'],
    '**安防分销（Dahua / Hikvision / Ajax）→ 分销 20% B，一页纸一次（STC-028GP $28 / STC-2216GP / STC-2224GP $86 CCTV PoE 一口价 + MOQ 1 + 付费样机；在售品牌不点名）' + UZ + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（名录地址 + ООО；ИНН 未全）。')
row('SB-976', 'Dauren Boltayev（dauren.boltaev@mail.ru；+998 77 009 91 388；**个人贸易商，无公司 / 域名 → 0 查**）— 表内「成单客户」：通讯产品贸易，**成交 2 次**；WA 已加；27 次跟进无回复', 'UZ',
    '0 查（mail.ru + 无公司）；2026-10-29', '', '0 查', '互动中（已成单 2 次）', '—', '个体贸易商', '通讯产品贸易（乌兹别克斯坦）', '未取', '个体',
    ['Dauren Boltayev — 贸易商本人（研究档 KP；dauren.boltaev@mail.ru）= 收件人'],
    '**★ 成交 2 次 → 复购最后一次一页纸（分销 20%：上次型号复购价 + STC-028GP $28 / STC-2216GP + MOQ 1；俄语备注）' + UZ + '**；27×0 → B 保留，回信即升 A 候选',
    '复购（分销 20%）；最后一次一页纸（预付 100%）；0 查；★ 回信即升。')

# ---------------- EG 3 ----------------
row('SB-629', 'C-TECH（c-techeg.com；**官网：2017 年成立的系统集成商（网络 / 网络安全 / 数据中心 / ELV / AV / 楼宇自动化）；页脚 Cairo, Nasr City, Mohamed Maqrif 25；+20 102 858 0334；info@c-tech.com.eg；ZoomInfo / RocketReach：5 5th Settlement, New Cairo；<25–33 人；MD Hamdy Elbadeea**）；商业登记号 1 查未得 → 部分坐实；自站 RFQ「工业 1 光 1 电 PoE」；KP Ahmed Sonbol；未跟进', 'EG',
    'EG · 1 次检索：c-techeg.com（Founded in 2017, C-TECH is a leading systems integrator in Egypt；Cairo, Nasr City Mohamed Maqrif 25；01028580334；info@c-tech.com.eg）+ zoominfo（5 5th Settlement, New Cairo；<25）+ rocketreach（Founded 2017；Employees 33；Hamdy Elbadeea Managing Director）；登记号未得；2026-10-29', 'https://c-techeg.com/',
    '未取（商业登记号 1 查未得）', '营业中（官网在）', '2017', 'LLC / S.A.E.（推定）', '系统集成（开罗纳斯尔城 / 新开罗）', 'Mohamed Maqrif St. 25, Nasr City, Cairo, Egypt（另 5th Settlement, New Cairo）', '小型（<25–33）',
    ['Ahmed Sonbol — 联系人（研究档 KP；ahmed.sonbol@c-techeg.com）= 收件人', 'Hamdy Elbadeea — Managing Director（RocketReach 2026-10-29；无公开邮箱）'],
    '**SI 自站 RFQ → 集成商 25% B，一页纸一次（STI-154GP 1 SFP + 1 GE + 4 PoE 对「1 光 1 电 PoE」+ STI-054GP 一口价 + MOQ 1 + 付费样机）' + EG + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网地址 + 成立年 + MD；登记号未取）。')
row('SB-971', 'IPS – Integrated Premium Solutions（integrated-ps.com；**官网 contacts / facebook：171 El Banafseg 7, First Settlement, New Cairo；+20 2 2307 8803 / +20 10 2121 2027；Info@；安防 + 证卡打印 / 跟踪系统方案商（Edikio / Agilia / BENTSAI）**）；登记号 1 查未得 → 部分坐实；自站询盘「4V1D 1080P」= 视频光端机（不供）；KP Ahmed；未跟进', 'EG',
    'EG · 1 次检索：integrated-ps.com/contacts（171 El Banfseg 7, New Cairo；+2 (02) 23 07 88 03；+2 (010) 21 21 20 27）+ facebook（IPS - Integrated premium solutions；171 El Banafseg 7, First Settlement, Cairo；Info@integrated-ps.com）；登记号未得；2026-10-29', 'https://integrated-ps.com/contacts/',
    '未取（商业登记号 1 查未得）', '营业中（官网在）', '未取', 'LLC（推定）', '安防 / 证卡打印 / 跟踪方案（新开罗）', '171 El Banafseg 7, First Settlement, New Cairo, Egypt', '小型',
    ['Ahmed — 联系人（研究档 KP；ahmed@integrated-ps.com）'],
    '**询盘视频光端机（不供）+ 证卡打印为主 → 不动（B 保留；来询按集成商 25% 报 STC-028GP）**' + EG, '不动（产品不对位）；部分坐实（官网地址）。')
row('SB-991', 'Egyptian Aluminium Tubes Company – Tubal Egypt（tubal-egypt.com；**D&B：9 El Zahaby Square, Roxi, Heliopolis, Cairo；Key Principal Fibi Bakhoum Toma；+202 2417 6301 / 2290 5751；trademo：HS 761210 铝管出口商；官网地址 18 Ashmoun St., Heliopolis 11341**）；登记号 1 查未得 → 部分坐实（制造商实体）；董事会成员 Daniel Adel Harvey 处理 PoE 新业务（2 光 10 电讲解在行、问告警口接 EMS、问 **SKD 分供便于清关** —— 我方已答可以）；1 次跟进无实质回复', 'EG',
    'EG · 1 次检索：dnb.com（EGYPTIAN ALUMINIUM TUBES COMPANY (TUBAL EGYPT)；9 El Zahaby Square, Roxi, Heliopolis Cairo；Key Principal Fibi Bakhoum Toma）+ trademo（HS 761210 egypt；18 ashmoun st heliopolis 11341）+ teg-designs 目录（(+202) 24176301）；登记号未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.egyptian_aluminium_tubes_company_(tubal_egypt).a3feb8608b1be15e8ac0ce4ca87e6db8.html',
    '未取（商业登记号 1 查未得）', '营业中（官网 + 出口记录）', '未取', 'S.A.E.（推定）', '铝管制造（赫利奥波利斯）+ PoE 进口新业务', '18 Ashmoun St. / 9 El Zahaby Square, Heliopolis, Cairo 11341, Egypt', '中型（制造）',
    ['Daniel Adel Harvey — Board Member（研究档 KP；info@tubal-egypt.com）= 收件人', 'Fibi Bakhoum Toma — Key Principal（D&B 2026-10-29；无公开邮箱）'],
    '**董事会成员亲自谈 PoE + SKD 清关需求（我方已答可以）→ 贴标 OEM 30% B，一页纸一次（STC-2216GP / STI-288DGGPM $137「2 光 10 电」对位 + SKD（整机拆箱分供，不做定制板）+ 贴标 MOQ + 付费样机；告警口 / EMS 按规格书答）' + EG + '**；回信 → 加厚',
    '贴标 OEM 30%（SKD）；一页纸一次（预付 100%）；部分坐实（D&B 地址 + 负责人 + 出口记录；登记号未取）。')

# ---------------- 国别待核 3 ----------------
row('SB-1139', 'Arnoldo Beltetón Mohr（arnoldomohr@gmail.com；Solution Architect 署名；**无公司 / 国别（姓氏 Beltetón 多见于危地马拉，待证）→ 0 查（1 次人名检索仅 facebook 同名 + 1980 年代同姓部长）**）— **A 邮箱 2025-04 起 8 轮群发后 2026-01-15 真回「CENTEC could be a great alternative in our market」，2026-03-10 带终端客户需求：Cisco C9300L-48P-4X 等价物（48×1G PoE+ + 4×10G SFP+，8 台堆叠 320 Gbps）** — 仓内唯一把 STH1G（CENTEC 48×1G PoE 堆叠线）谈到参数层面的客户', '??',
    '0 查（gmail + 无公司；人名 1 查无命中）；2026-10-29', '', '0 查', '互动中（2026-01 / 03 两次真回）', '—', '未知', '方案架构（国别待核；疑危地马拉）', '未取', '未知',
    ['Arnoldo Beltetón Mohr — Solution Architect（研究档 KP；arnoldomohr@gmail.com）= 收件人'],
    '**★ CENTEC 堆叠线真实需求 → 建议升 A（Simon 定）；集成商 25% B 先行：一页纸（STH1G 48×1G PoE+ + 4×10G SFP+ 堆叠 按主表报 + 堆叠带宽 / PoE 预算 / 交期如实 + 付费样机；FOB 深圳；国别一句话问清）**；回信即升',
    '集成商 25%（CENTEC STH1G）；一页纸 + 补答（预付 100%）；0 查；★ 建议升 A。')
row('SB-582', 'SmartIntercom（smartintercom.eu；**1 查仅 Akuvox 通用结果 → 未坐实**；.eu 域名，国别未填）— Akuvox 合作的高端门禁对讲分销商；表内「4 口工业级 PoE 交换机报价」；KP Ronald（roh@）；6 次跟进无回复', 'EU',
    'EU · 1 次检索：「SmartIntercom smartintercom.eu Akuvox distributor」→ 无本体命中（sourcesecurity / Akuvox 法务页）；2026-10-29', '', '未取（1 查无命中）', '营业中（研究档官网 ok）', '未取', '未取', '门禁对讲分销（欧洲，国别待核）', '未取（.eu）', '小型（推定）',
    ['Ronald — 联系人（研究档 KP；roh@smartintercom.eu）= 收件人'],
    '**主动要 4 口工业 PoE 报价（我方欠一页纸）→ 集成商 25% B，一页纸一次（STI-054GP 4 PoE + 1 GE / STI-154GP 一口价 + MOQ 1 + 付费样机；FOB 深圳 或 DAP 欧盟 买方清关；周四 12–14 当地）**；国别一句话问清；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；未坐实（国别待核）。')
row('SB-973', 'Multi Technology System（info@multi-technology.com；**域名现为无关数字市场页（误配）+ 国别未填 → 0 查**）—「杂」表来源，对工业 PoE / 非 PoE 工业机有兴趣；无跟进', '??',
    '0 查（域名误配 + 国别未知）；2026-10-29', '', '0 查', '存续待核（域名易主）', '未取', '未取', '未知', '未取', '未知',
    ['（未具名；info@multi-technology.com）'],
    '**查无实体 + 国别未知 + 无 KP → 不动（B 保留）**', '不动（查无实体）；0 查。')

# ---------------- PE 2 ----------------
row('SB-031', 'OM TELECOM S.R.L.（om-telecom.com；**SUNAT 镜像 universidadperu：RUC 20600792858；Activo / Habido；Fecha Inicio 2015-11-02；CIIU 64207 电信；Dirección Legal Av. Ramón Castilla 1120 Int. 503A, Santiago de Surco, Lima；RNP 政府供应商；connectamericas：7 人、2015、Bureau Veritas 认证；工业电信集成（能源自动化 / 矿业 / 油气：光网络、载波、远动保护、CCTV）**）→ 坐实；KP Clyver Ore M.（Sales Manager，WA 已加；2023-11 问「L3 工业」）/ Joel Ore（CFO）；2 次回复 / 18 次跟进', 'PE',
    'PE · 1 次检索：universidadperu.com/empresas/om-telecom.php（RUC 20600792858；OM TELECOM S.R.L.；Activo；02/Noviembre/2015；CIIU 64207；Av. Ramon Castilla Nro. 1120 Int. 503a, Santiago de Surco；Habido；RNP）+ connectamericas（7 funcionários；Fundado em 2015；Joel Ore CFO）；2026-10-29', 'https://www.universidadperu.com/empresas/om-telecom.php',
    'RUC 20600792858', 'Activo / Habido（SUNAT 镜像）', '2015-11-02', 'S.R.L.', '工业电信集成（利马）', 'Av. Ramón Castilla 1120 Int. 503A, Santiago de Surco, Lima, Peru（办公 Calle Rocca de Vergallo 263 Of. 101, Magdalena）', '微型（7 人）',
    ['Clyver Ore M. — Sales Manager（研究档 KP；clyver.ore@om-telecom.com；WA 已加）= 收件人', 'Joel Ore — CFO（connectamericas 2026-10-29 吻合；研究档 KP）'],
    '**工业电信集成（矿业 / 能源）+ 曾问 L3 工业 → 集成商 25% B，一页纸一次（工业 L2 管理 STI-288DGGPM $137 / STI-488DGGPM $147 + 机柜侧 STC-4424GCPM $165 L2+ 一口价 + STC-110XGE $65；工业 L3 不供如实说；西语备注）' + PE + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；坐实（RUC + 状态 + 成立日 + 法定地址）。')
row('SB-051', 'Prestige Satellite Communications Inc.（prestigevsat.com；**Sunbiz：Florida Profit Corporation，Document No. P16000009000，FEI/EIN 81-1222208，Filed 2016-01-26，Status ACTIVE；2873 SW 14th Street, Fort Lauderdale, FL 33312；President / Registered Agent William Bye；ZoomInfo：Owner Howell Robert（= 表内 Rob ✓）、Director & Engineer William Bye、1–10 人；豪华游艇 VSAT / TVRO / IT 服务 → 表内「秘鲁 S.A.C.」误 → country_fix 美国**）→ 坐实；表内「买了 MC、PoE」= 老客户；0 次跟进', 'US',
    'US · 1 次检索：search.sunbiz.org（PRESTIGE SATELLITE COMMUNICATIONS INC；P16000009000；FEI/EIN 81-1222208；Date Filed 01/26/2016；ACTIVE；2873 SW 14th Street FORT LAUDERDALE, FL 33312；President BYE, WILLIAM）+ zoominfo（805 NE 18th Ave Apt 5, Fort Lauderdale；1-10；William Bye Director and Engineer；Howell Robert Owner）；2026-10-29', 'https://search.sunbiz.org/Inquiry/corporationsearch/SearchResultDetail?inquirytype=EntityName&directionType=Initial&searchNameOrder=PRESTIGESATELLITECOMMUNICATION+P160000090000&aggregateId=domp-p16000009000-20d41eec-a083-4d54-9313-5c26da829222',
    'FL Document No. P16000009000；EIN 81-1222208', 'ACTIVE（Sunbiz）', '2016-01-26', 'Florida Profit Corporation', '游艇 VSAT / TVRO / IT 服务（劳德代尔堡）', '2873 SW 14th Street, Fort Lauderdale, FL 33312, USA', '微型（1–10）',
    ['Rob = Robert Howell — Owner（ZoomInfo 2026-10-29；研究档 KP rob@prestigevsat.com）= 收件人', 'William Bye — President / Director & Engineer（Sunbiz 2026-10-29；无公开邮箱）'],
    '**★ 老客户（买过 MC + PoE）→ 回访一页纸一次（集成商 25%：STC-110XGE $65 + STC-228GP $33 / STC-2216GP 游艇机房一口价 + MOQ 1；船级 / 海事认证不声称）' + US + '**；回信即升 A 候选',
    '回访（集成商 25%）；一页纸一次（预付）；坐实（Sunbiz 文件号 + EIN + 状态 + 地址）；country_fix 美国；★ 回信即升。')

# ---------------- BH 2 ----------------
row('SB-033', 'Marvel Business Consultants Co. W.L.L.（品牌 Marvel IT Solutions / Marvel ITCS；marvelitcs.com；**官网页脚：Office 0, Building 100, Road 56, Block 203, Muharraq, Bahrain；+973 3988 5090；sales@；自述 17 年；托管 IT + 安防 + 网络交换（名录类目）**）；CR 号 1 查未得 → 部分坐实；KP Nasir（info@；要「Cisco 同款型号」；2024-07 passive PoE 手册回 OK）；2 次回复 / 15 次跟进', 'BH',
    'BH · 1 次检索：marvelitcs.com（© Marvel Business Consultants Co. W.L.L；Office 0 Building 100 Road 56 Block 203, Muharraq；+973 39885090；sales@marvelitcs.com；17 YEARS）+ namibiayponline 名录（Marvel Business Consultants CO WLL；Network Switches / Access Control）；CR 未得；2026-10-29', 'https://marvelitcs.com/',
    '未取（CR 号 1 查未得）', '营业中（官网 2026）', '约 2008（自述 17 年）' , 'W.L.L.', '托管 IT / 安防 / 网络（穆哈拉格）', 'Office 0, Building 100, Road 56, Block 203, Muharraq, Bahrain', '小型（<50 推定）',
    ['Nasir — 联系人（研究档 KP；info@marvelitcs.com）= 收件人'],
    '**MSP 要 Cisco 对位 → 集成商 25% B，一页纸一次（CBS / SG 类对位表 → STC-2224GP $86 / STC-4424GCPM $165 L2+ / STC-2216GP 一口价 + MOQ 1 + 付费样机；在用品牌不点名）' + BH + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网法定名 + 地址；CR 未取）。')
row('SB-192', 'Core and Clad（**gmail + 无域名 → 0 查**；Intersec 2011 名片）— 巴林光纤领域贸易 / 工程商；KP Ebrahim Y. Alsada（采购）；**2011 年买过 2 次收发器** = 老客户；E 冷名单 1 次跟进 0 回复', 'BH',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（2011 成交 2 次）', '—', '未取', '光纤产品贸易 / 工程（巴林）', '未取', '小型（推定）',
    ['Ebrahim Y. Alsada — 采购（研究档 KP；core.and.clad@gmail.com）= 收件人'],
    '**老客户（2011 收发器 ×2）→ 回访一页纸一次（分销 20%：STC-110XGE $65 + STC-028GP $28 / STC-228GP $33 一口价 + MOQ 1）' + BH + '**；再无回声 → 不动',
    '回访（分销 20%）；一页纸一次（预付 100%）；0 查。')

# ---------------- ZW 2 ----------------
row('SB-049', 'Multi-Link (Pvt) Ltd = SECURICO 电子安防事业部（securico.co.zw；**公开资料：DDNS Security Operations (Pvt) Ltd 为控股公司（SECURICO / Canine / MULTI-LINK P/L），MD Divine Ndhlukula；SECURICO 1998 年创立，2008 年收购 Multi-Link，津巴布韦第二大电子安防系统商；Ebenezer House, 10 Millwood Road, Workington, Harare（研究档）；ISO 9001 / 45001 / 14001；4,300+ 员工**）；注册号 1 查未得 → 部分坐实（大型集团）；表内 **2011–2013 买过光端机（8V1D / 16V1D / 18 机架）+ 多种 FS** = 老客户；KP Samuel Kanoyangwa / Blessing Murondiwa（info@）', 'ZW',
    'ZW · 1 次检索：gravatar.com/newsletter160（SECURICO … acquiring … MultiLink (Pvt) Ltd … 2008 … Electronic Division … second largest electronic security systems provider in Zimbabwe）+ pindula.co.zw（Founded 1998；2008 acquired Multi-Link）+ divinesimbindhlukula.co.zw（Managing Director of DDNS Security Operations (Pvt) Ltd … holding company for SECURICO … MULTI-LINK P/L）；注册号未得；2026-10-29', 'https://www.pindula.co.zw/Securico_Security_Services',
    '未取（津巴布韦公司注册号 1 查未得）', '营业中（集团官网 + 公开资料）', '1998（SECURICO）/ Multi-Link 2008 并入', '(Pvt) Ltd（DDNS Security Operations 控股）', '电子安防系统（哈拉雷）', 'Ebenezer House, 10 Millwood Road, Workington, Harare, Zimbabwe', '大型（集团 4,300+）',
    ['Samuel Kanoyangwa / Blessing Murondiwa — 表内联系人（研究档 KP；info@securico.co.zw）= 收件人', 'Divine Ndhlukula — Managing Director, DDNS Security Operations（公开资料 2026-10-29；无公开邮箱）'],
    '**老客户（2011–2013 光端机 + FS）→ 回访一页纸一次（集成商 25%：FS 对位 STI-154GP / STI-288DGGPM $137 工业线 + STC-2216GP / STC-2224GP $86 一口价 + MOQ 1；光端机不供明说）' + ZW + '**；再无回声 → 不动',
    '回访（集成商 25%）；一页纸一次（预付 100%）；部分坐实（集团公开资料 + 地址；注册号未取）。')
row('SB-116', 'Pyramid Enterprises（pyramidenterprises3@gmail.com；**gmail + 无域名 → 0 查**）— 津巴布韦小型 IT 商 Cuthbert Mukumbi；需求 10G 850nm 光模块（不供）；2024–2025 对 MC / 工业 PoE / 2.5G / 16–24 口一律「暂时没需求」', 'ZW',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（多次「暂时没需求」）', '—', '未取', 'IT 供应（津巴布韦）', '未取', '微型',
    ['Cuthbert Mukumbi — 联系人（研究档 KP；pyramidenterprises3@gmail.com）'],
    '**需求光模块（不供）+ 多次婉拒 → 不动（B 保留）**' + ZW, '不动（产品不对位 + 婉拒）；0 查。')

# ---------------- QA 2 ----------------
row('SB-1062', 'Al-Tamyeez Security Systems Co.（tamyeezsecurity.com；表内域名误记 odoo.com；**官网 / doha.directory / qbusinessgate：2012 年起卡塔尔公司；Al-Markhiya Complex, Al-Markhiya, Zone 33, P.O. Box 15394, Doha（另 Street 370, Bldg 252, Unit 81）；+974 4488 4600；info@；安防 + 网络方案（CCTV / 对讲 / 智能家居）**）；CR 号 1 查未得 → 部分坐实；表内「有 Utepo 的交换机」；无具名 KP；4 次跟进无回复', 'QA',
    'QA · 1 次检索：tamyeezsecurity.com（© 2012-2020 Al-Tamyeez Security Systems Co；Al-Markhiya Complex, Zone 33, P.O.Box 15394 Doha；+974 44884600；info@tamyeezsecurity.com）+ doha.directory（since 2012；Street No: 370, Building No: 252, Unit No: 81）+ qbusinessgate（since 2012）；CR 未得；2026-10-29', 'https://www.doha.directory/al-tamyeez-security-systems/i/2157',
    '未取（CR 号 1 查未得）', '营业中（官网 + 名录 2025）', '2012', 'W.L.L.（推定）', '安防 / 网络系统集成（多哈）', 'Al-Markhiya Complex, Zone 33, P.O. Box 15394, Doha, Qatar', '小型',
    ['（无具名 KP：info@tamyeezsecurity.com；Attn: Procurement Manager）'],
    '**安防 SI（在用 UTEPO 类 PoE）→ 集成商 25% B，一页纸一次（STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1 + 付费样机；在用品牌不点名）' + QA + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网地址 + 成立年；CR 未取；域名更正 tamyeezsecurity.com）。')
row('SB-166', 'Crown Security Solutions W.L.L.（卡塔尔；Crown Group；**RocketReach：Mohamed Safeer = Chief Technology Officer（2018 起；2012–2018 Crown Group 技术支持）**；地址 / CR 1 查未得 → 部分坐实（KP 职务坐实）；Cudy 分销商；**提出 200 台工业 5 电口需求**，2025-02 要工业 16 / 24 口 datasheet，2025-10 CPSE 展会面谈；无邮箱（WA）', 'QA',
    'QA · 1 次检索：rocketreach.co/mohamed-safeer-email_25509741（Chief Technology Officer @ CROWN SECURITY SOLUTIONS LIMITED / Crown Security Solutions WLL；Qatar；2018 - now；Crown Group 2012–2018）；地址 / CR 未得；2026-10-29', 'https://rocketreach.co/mohamed-safeer-email_25509741',
    '未取（CR 号 1 查未得）', '营业中（展会 2025-10 面谈）', '未取', 'W.L.L.', '安防分销（多哈；Cudy 分销）', '未取（Doha, Qatar）', '小型',
    ['Mohamed Safeer — Chief Technology Officer（RocketReach 2026-10-29；研究档 KP；仅 WA）= 收件人'],
    '**★ 200 台工业 5 电口需求 + 展会面谈 + CTO 为 KP → 分销 20% B，WA 一页纸（STI-054GP / STI-280GE $46.6 ×200 阶梯一口价 + 工业 16 / 24 口 STI-0240GE $130 规格书 + 付费样机；Cudy 不点名）' + QA + '**；回信即升 A 候选',
    '分销 20%；WA 一页纸 + 规格书（预付 100%）；部分坐实（KP 职务；地址 / CR 未取）；★ 回信即升。')

# ---------------- UG 2 ----------------
row('SB-110', 'iTKATI UG Ltd（ITKati Corp.；itkati.com；**eastafricatenders：Registration Date 2018-07-25，Block 244 Plot 965, Kyadondo, Makindye, Kampala；yellow.ug：2009 年起、6–10 人、Company manager Sarah Basemera；+256 393 225 713 / +256 704 575 328；企业网络 / CCTV / Starlink / VoIP / 软件**）；URSB 号 1 查未得 → 部分坐实；KP Bob（technical@；WA 已加；价格 OK、要样、**要贴自有标**）', 'UG',
    'UG · 1 次检索：eastafricatenders.com/directory/itkati-ug-ltd（Registration Date Jul 25, 2018；Block 244 Plot 965 Kampala）+ yellow.ug/company/40803（established in 2009；Company manager sarah basemera；Employees 6-10）+ worldplaces（Makindye；+256704575328）；URSB 未得；2026-10-29', 'https://eastafricatenders.com/directory/itkati-ug-ltd/',
    '未取（URSB 号 1 查未得；登记日 2018-07-25）', '营业中（官网 + 名录 2026-07 更新）', '2009（登记 2018-07-25）', 'Ltd', 'IT / 网络 / 安防集成（坎帕拉 Makindye）', 'Block 244, Plot 965, Kyadondo, Makindye, Kampala, Uganda', '微型（6–10）',
    ['Bob — 技术 / 采购（研究档 KP；technical@itkati.com；WA 已加）= 收件人', 'Sarah Basemera — Company manager（yellow.ug 2026-10-29；无公开邮箱）'],
    '**价格 OK + 要样 + 要自有标 → 贴标 OEM 30% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2216GP 贴标 + 贴标 MOQ + 付费样机；小量先按集成商 25% 中性包装）' + UG + '**；回信 → 加厚',
    '贴标 OEM 30%（小量 25%）；一页纸一次（预付 100%）；部分坐实（登记日 + 地址 + 人数；URSB 号未取）。')
row('SB-183', 'Onyx Technology Solutions Ltd（onyxtechnologysolutionsltd.com；**官网：Room S.11 Nathur Building, Victoria Street, Masaka City, Uganda；+256 704 803 724 / +256 200 906 532；gmail；ISP / WISP + 电气 / ICT / 安防方案（马萨卡、姆巴拉拉）**）；URSB 号 1 查未得 → 部分坐实；KP Steven Ntengo；Cambium Force 用户，需求工业 PoE 注入器（不供）；2024 问工业机 / 48 口 / 228 价，对 154 有兴趣，要价目', 'UG',
    'UG · 1 次检索：onyxtechnologysolutionsltd.com（Onyx Technology Solutions Ltd；Room S.11 Nathur Building, Victoria Street Masaka City；+256-704-803-724；onyxtechnologysolutionsltd@gmail.com；ISP）；URSB 未得；2026-10-29', 'https://onyxtechnologysolutionsltd.com/',
    '未取（URSB 号 1 查未得）', '营业中（官网 2025）', '未取', 'Ltd', 'WISP / ICT / 电气 / 安防（马萨卡）', 'Room S.11, Nathur Building, Victoria Street, Masaka City, Uganda', '微型',
    ['Steven Ntengo — 联系人（研究档 KP；onyxtechnologysolutionsltd@gmail.com）= 收件人'],
    '**对 154 有兴趣 + 要价目 → 集成商 25% B，一页纸一次（STI-154GP / STI-054GP 塔站供电 + STC-228GP $33 一口价 + MOQ 1；注入器不供明说）' + UG + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网地址；URSB 号未取）。')
