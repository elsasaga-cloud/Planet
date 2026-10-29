# -*- coding: utf-8 -*-
"""第 123 批（T29-U114，2026-10-29）第 2 段 18 户（BD / ET / SV / AO / MR / BW / LY / TN / CM / SN / KG / MZ / BI / MM / LK / CO / CL / NE 各 1）—— B 池收尾段三（清零）官方登记核实写入 registry。
CO：RUES 镜像 NIT 805017291-1（1 查即得，SB-920）；BD：官网 about + RocketReach（RJSC ✗）；SV：官网 contact（NIT ✗）；MR：官网 contact BP 3384；TN：官网 2 门店地址（RNE ✗）；
MZ：PeeringDB AS328223 法定名 VOIPTECH LIMITADA + 地址 + KP CTO；LK：BOI 公开报道 + 招聘页注册地址；CL：官网地址（RUT ✗）；LY：1 查仅同名 ARKAN → 未坐实；
gmail / hotmail / mail.ru 户（ET / AO / BW / CM / SN / KG / BI / MM / NE）0 查。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 123
F = '2026-10-29'
AF = '— 非洲常规：英文稿（法语区附法语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方货代清关）；周二 / 周四 10–12 当地'
LA = '— 拉美常规：英文稿（可附西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP（买方清关）；周二 / 周四 10–12 当地'
AS = '— 亚洲常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方清关）；周二 / 周四 10–12 当地'
KG = '— 吉尔吉斯斯坦常规：英文稿（可附俄语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 比什凯克（买方清关；EAC 不声称）；周四 10–12 当地'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

row('SB-1103', 'ARA Technologies Limited（Advanced Resources And Technologies；aratechbd.com，旧域 ara.com.bd；**官网 about：2005 年起；Banani C/A 17, Banani, Dhaka 1213；+880 1678 004434；工厂 Bhaluka, Mymensingh；光电 / LAN / WAN / CATV 产品制造 + 分销；RocketReach 20 人；Md. Chan Miah Sarker = Sr. Executive, Support & Maintenance（非决策人）**）；RJSC 号 1 查未得 → 部分坐实；表内：买过磊通设备、Switch / MC 周边、非自有品牌；support@ 退信；9 次跟进 1 次回复', 'BD',
    'BD · 1 次检索：aratechbd.com/about（ARATECH 2005；ARA Team Md. Chan Miah Sarker Sr. Executive, Support & Maintenance；FACTORY Bhaluka, Mymensingh）+ rocketreach（ARA Technologies Limited；Banani C/A 17, Banani TSO, Dhaka 1213；Founded 2005；Employees 20；+880 1678-004434）；RJSC 未得；2026-10-29', 'https://aratechbd.com/about/',
    '未取（RJSC 号 1 查未得）', '营业中（官网 2025-12）', '2005', 'Limited（私营）', '网络 / 光电产品制造 + 分销（达卡）', 'Banani C/A 17, Banani, Dhaka 1213, Bangladesh（工厂 Bhaluka, Mymensingh）', '小型（约 20）',
    ['Md. Chan Miah Sarker — Sr. Executive, Support & Maintenance（官网 2026-10-29；研究档 KP；smchan91@gmail.com；support@ara.com.bd 退信）= 收件人（请转采购）'],
    '**经销同类商用 PoE / MC（进口过中国品牌）→ 分销 20% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-110XGE $65 一口价 + MOQ 1 + 付费样机；请转采购负责人；在售品牌不点名）' + AS + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网地址 + 成立年 + KP 职务；RJSC 未取）。')
row('SB-1109', 'Mulugeta Wendosen（mulugetawendosen@gmail.com；+251 955 019 650；**个人 gmail、无公司 → 0 查**）— 2022-11 自建站最早询盘：千兆双纤 20 km 工业光模块（不供）；消息未读，无后续；7 次跟进', 'ET',
    '0 查（gmail + 无公司）；2026-10-29', '', '0 查', '存续待核（未读）', '—', '个人', '未知（埃塞俄比亚）', '未取', '个人',
    ['（未具名；mulugetawendosen@gmail.com）'],
    '**需求光模块（不供）+ 无公司 + 未读 → 不动（B 保留）**' + AF, '不动（产品不对位）；0 查。')
row('SB-1134', 'Conexión de Redes de Centro América（conexionderedes.com；**官网：San Salvador, El Salvador；+503 2262-1049；gerencia@；业务 XGPON / FTTH / POLAN 智能楼宇 / IPTV / 数据中心 / LTE / IP 微波 / PoE LED 照明，面向中美洲企业与运营商**）；NIT 1 查未得 → 部分坐实；**A 邮箱 24 去 3 来，总经理 Antonio Alberto Guadron 三次真回：2025-05 要旁路交换机资料、2026-01-19 对 CENTEC「OEM Core Switching Solution」回「Interesting solution. Please send the technical information so we can share it with our clients」**；13 次跟进', 'SV',
    'SV · 1 次检索：conexionderedes.com/servicios（Conexion de Redes；Teléfono +503 2262-1049；Email gerencia@conexionderedes.com；Ubicación San Salvador, El Salvador；XGPON / FTTH / POLAN / IPTV / Data Center / LTE）；NIT 未得；2026-10-29', 'https://www.conexionderedes.com/servicios',
    '未取（NIT 1 查未得）', '营业中（官网 2026）', '未取', 'S.A. de C.V.（推定）', '电信 / 网络集成与分销（圣萨尔瓦多）', 'San Salvador, El Salvador（街道未取；+503 2262-1049）', '小型',
    ['Antonio Alberto Guadron — Gerente General（官网 gerencia@ 吻合；研究档 KP；gerencia@conexionderedes.com）= 收件人'],
    '**★ CENTEC 核心机真回 + 代客转发型 → 建议升 A（Simon 定）；集成商 25% B 先行：一页纸（STH-8C48DX-HSI $4,800 / STH-2C24XF-HSI $1,500 CENTEC 规格书 + 接入 STC-424XGGPM-280W $198 / STC-4424GCPM $165 + 付费样机；西语备注）' + LA + '**；回信即升',
    '集成商 25%（CENTEC 线）；一页纸 + 规格书（预付 100%）；部分坐实（官网地址 + 电话 + GM 邮箱）；★ 建议升 A。')
row('SB-125', 'Anfiris, Lda（安哥拉；Carlos da Silva；**repintalimitada@gmail.com、无域名 → 0 查**）— 表内「8 口 network switch 成样品单」= 已付款样品客户；无后续跟进', 'AO',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（成样品单）', '—', 'Lda（表内）', '未知（安哥拉）', '未取（+244 923 545 606）', '微型（推定）',
    ['Carlos da Silva — 联系人（研究档 KP；repintalimitada@gmail.com）= 收件人'],
    '**样品已成单 → 回访一页纸一次（集成商 25%：8 口样品同型复购价 + STC-028GP $28 8 PoE 一口价 + MOQ 1；葡语备注）' + AF + '**；回信即升 A 候选',
    '回访（集成商 25%）；一页纸一次（预付 100%）；0 查。')
row('SB-168', 'Wimex Technologies（Groupe WIMEX；wimex.mr；**官网 contact：55 Ilot C, Zone Château d\'Eau, BP 3384, Nouakchott；+222 45 25 23 56；info@wimex.mr；flcompres：System Integrator；研究档：1993 / 1995 创立、51–200 人、微波传输 / GSM 站点 / 光网络 / 企业网；PDG Mohamed Waled**）；RC / NIF 1 查未得 → 部分坐实；KP Moustapha Elemine（官网合作页同邮箱；WA 已加；要 80 km 光模块（不供）+ 曾回「2 光 4」小机价）；19 次跟进 1 次回复', 'MR',
    'MR · 1 次检索：wimex.mr/wimexTechnologie/contact（55 Ilot C Zone Château d\'Eau BP 3384 Nouakchott；(+222) 45 25 23 56；info@wimex.mr）+ flcompres（System Integrator, Nouakchott）+ yellowpagesofafrica（WIMEX BP 3384）；RC / NIF 未得；2026-10-29', 'https://www.wimex.mr/wimexTechnologie/contact',
    '未取（RC / NIF 1 查未得）', '营业中（官网 + 名录）', '1993 / 1995（集团）', 'SARL / SA（推定）', '电信工程 / 系统集成（努瓦克肖特）', '55 Ilot C, Zone Château d\'Eau, BP 3384, Nouakchott, Mauritania', '中型（51–200）',
    ['Moustapha Elemine — 表内联系人（研究档 KP；moustapha@wimex.mr；WA 已加）= 收件人', 'Mohamed Waled — PDG（研究档；无公开邮箱）'],
    '**电信集成集团 + 曾回「2 光 4」小机价 → 集成商 25% B，一页纸一次（STI-244DGGPM $121 2 SFP + 4 PoE 管理 / STI-154GP 一口价 + MOQ 1 + 付费样机；80 km 光模块不供明说；法语备注）' + AF + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网地址 + BP；RC / NIF 未取）。')
row('SB-182', 'Netbowl (Pty) Ltd（博茨瓦纳；Lenamile Catlass Pogiso；**lpogiso@gmail.com、无域名 → 0 查**）— 网络公司；需求工业小壳 1 光 4；2024-05 谈过项目未成，2025-06「slow business」；WA 已加；14 次跟进 2 次回复', 'BW',
    '0 查（gmail + 无域名；CIPA 不开放）；2026-10-29', '', '0 查', '互动中（2025-06 回复）', '—', '(Pty) Ltd（表内）', '网络工程（博茨瓦纳）', '未取（+267 71 704 050）', '微型（推定）',
    ['Lenamile Catlass Pogiso — 联系人（研究档 KP；lpogiso@gmail.com；WA 已加）= 收件人'],
    '**明确口型 1 光 4 工业 + 曾谈项目 → 集成商 25% B，最后一次一页纸（STI-154GP / STI-054GP 一口价 + MOQ 1；一句话问是否要 PoE）' + AF + '**；再无回声 → 不动',
    '集成商 25%；最后一次一页纸（预付 100%）；0 查。')
row('SB-310', 'Arcan Libya（arcanlibya.com；**1 查仅同名 ARKAN IT Solutions（+218 91 370 6338，与研究档 +218 91 366 2420 不符）/ Arkan Security → 未匹配 → 未坐实**）；的黎波里 IT / 网络公司，GM Ahmed Ezzarrough；2025 ISAF 展接触：问 8 光 8 电价格、要价格表、要工业 PoE 管理交换机；WA 无实质回复', 'LY',
    'LY · 1 次检索：「Arcan Libya arcanlibya.com Tripoli」→ libyayp ARKAN IT Solutions（Al-Jamahirya Street；+218 91 370 6338）/ linkedin Arkan Security（信息安全）均未匹配域名 / 电话；2026-10-29', '',
    '未取（1 查无命中）', '营业中（研究档官网 ok）', '未取', '未取', 'IT / 网络（的黎波里）', '未取（Tripoli, Libya；+218 21 712 8108）', '小型（推定）',
    ['Ahmed Ezzarrough — General Manager（研究档 KP；info@arcanlibya.com；WA 已加）= 收件人'],
    '**ISAF 展主动要价（8 光 8 电 + 工业 PoE 管理 + 价格表）→ 集成商 25% B，一页纸一次（8 光 8 电工业 按主表报 + STI-288DGGPM $137 / STI-488DGGPM $147 一口价 + 工业线价目 + MOQ 1 + 付费样机；FOB 深圳 买方货代）' + AF + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次 + 价目（预付 100%）；未坐实。')
row('SB-338', 'Max Protect（max-protect.com；**官网：哈马马特 2 家门店 — Avenue Habib Bourguiba, 8050 Hammamet / Avenue Abou Dhabi（Route de Nabeul）；72 324 111；全突尼斯 48h 配送；监控 / 报警 / 可视对讲（Dahua / Uniview / Imou / Ajax）**）；RNE 号 1 查未得 → 部分坐实；Manager Aymen Gabsi 很在意价格，**曾以 $40 买走 2 光 8 电管理 PoE 样品**；6 次跟进无实质回复', 'TN',
    'TN · 1 次检索：max-protect.com（Max Protect – caméras, alarmes et visiophones；2 magasins à Hammamet；Avenue Habib Bourguiba 8050 Hammamet；72 324 111）；RNE 未得；2026-10-29', 'https://max-protect.com/',
    '未取（RNE 号 1 查未得）', '营业中（官网 2026）', '未取', 'SARL（推定）', '安防设备零售 / 分销 / 安装（哈马马特）', 'Avenue Habib Bourguiba, 8050 Hammamet, Tunisia（第二店 Avenue Abou Dhabi, Route de Nabeul）', '微型（2 门店）',
    ['Aymen Gabsi — Manager（研究档 KP；direction@max-protect.com）= 收件人'],
    '**样品已购（$40 2 光 8 PoE 管理）→ 分销 20% B，一页纸一次（问测试结果 + STC-228GP $33 / STC-028GP $28 整箱 10 台一口价 + MOQ 1；法语；在售品牌不点名）' + AF + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网门店地址 + 电话；RNE 未取）。')
row('SB-339', 'OMEGATEC SARL（喀麦隆；Stephane Mbongou；**omegatec3@gmail.com、无域名 → 0 查（研究档：搜索无公开资料）**）— 网络设备转售商（自称 Reseller）；要 16 口千兆 PoE + 价格表；2024 问多光口 / 12 光 L3；WA 已加；20 次推送 1 次实质回复', 'CM',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（1 次）', '—', 'SARL（表内）', '网络设备转售（喀麦隆）', '未取（+237 53 283 301）', '微型（推定）',
    ['Stephane Mbongou — 联系人（研究档 KP；omegatec3@gmail.com；WA 已加）= 收件人'],
    '**Reseller 要 16 口 PoE + 价格表 → 分销 20% B，最后一次一页纸（STC-2216GP $63–76 / STC-2224GP $86 一口价 + 商用线价目 + MOQ 1；12 光 L3 不供明说；法语）' + AF + '**；20×1 → 再无回声 → 不动',
    '分销 20%；最后一次一页纸 + 价目（预付 100%）；0 查。')
row('SB-463', 'Groupe Penda Telecoms（塞内加尔；Seydou Jah；**bigbocar@hotmail.com、无域名 → 0 查**）— 2019-03 询盘，**千兆 SFP 收发器成样品单**（有自己的货代）；无后续跟进', 'SN',
    '0 查（hotmail + 无域名）；2026-10-29', '', '0 查', '互动中（2019 成样品单）', '—', '未取', '电信产品贸易（塞内加尔）', '未取', '微型（推定）',
    ['Seydou Jah — 联系人（研究档 KP；bigbocar@hotmail.com）= 收件人'],
    '**样品已成单（SFP，现不供）→ 回访一页纸一次（集成商 25%：STC-110XGE $65 + STC-228GP $33 / STC-028GP $28 一口价 + MOQ 1；SFP 不供明说；法语）' + AF + '**；再无回声 → 不动',
    '回访（集成商 25%）；一页纸一次（预付 100%）；0 查。')
row('SB-499', 'Bogdan（Medvedev，按邮箱推断；b.medvedev11@mail.ru；+996 555 772 975 = 吉尔吉斯斯坦；**MIPS 莫斯科展名片，无公司 → 0 查**；表内国别「沙特」已按号段改 KG）— 拿了彩页，问过工业 FS / SFP；WA 已加；23 次跟进 3 次回复（无实质）', 'KG',
    '0 查（mail.ru + 无公司）；2026-10-29', '', '0 查', '互动中（MIPS 名片）', '—', '个人', '未知（吉尔吉斯斯坦）', '未取', '个人',
    ['Bogdan Medvedev — MIPS 名片（研究档 KP；b.medvedev11@mail.ru；WA 已加）= 收件人'],
    '**展会名片 + 问过工业 FS → 集成商 25% B，最后一次一页纸（STI-280GE $46.6 / STI-288GPM $78.9 / STI-288DGGPM $137 一口价 + MOQ 1；SFP 不供明说；俄语备注）' + KG + '**；23×0 → 再无回声 → 不动',
    '集成商 25%；最后一次一页纸（预付 100%）；0 查。')
row('SB-564', 'VOIPTECH LIMITADA（品牌 Latitude / Conecte Internet e Soluções；voiptech.co.mz / conecte.co.mz；**PeeringDB：AS328223，ISP / 网络服务，5–10 Gbps，MOZIX 10G 对等；Av. Ho Chi Minh nº 677, 1º andar, Maputo；技术联系人 Manuel Manjala +258 84 042 3759；LinkedIn：Manuel Manjala = Chief Technology Officer**）；NUIT 1 查未得 → 部分坐实；阿里询盘「WDM Switch」（= 单纤 BiDi 光口交换机；光模块不供）；1 次跟进无实质回复', 'MZ',
    'MZ · 1 次检索：peeringdb.com/net/20853（VOIPTECH LIMITADA；AS328223；Cable/DSL/ISP；5-10Gbps；Technical Manuel Manjala manjala@voiptech.co.mz）+ peeringdb.com/org/23811（Ho Chi Mi nº677, First floor, Maputo）+ linkedin（Manuel Manjala Chief Technology Officer at Voiptech Limitada）；NUIT 未得；2026-10-29', 'https://www.peeringdb.com/net/20853',
    '未取（NUIT 1 查未得；AS328223）', '营业中（PeeringDB 2024 + MOZIX）', '未取', 'Limitada', 'ISP / VoIP / 网络服务（马普托）', 'Av. Ho Chi Minh nº 677, 1º andar, Maputo, Mozambique', '小型',
    ['Manuel Manjala — Chief Technology Officer（LinkedIn + PeeringDB 2026-10-29；研究档 KP；manjala@voiptech.co.mz）= 收件人'],
    '**ISP + 询盘 2 SFP 交换机（BiDi 自配）→ 集成商 25% B，一页纸一次（STC-228GP $33 / STI-288DGGPM $137 / STC-4424GCPM $165 一口价 + MOQ 1 + 付费样机；光模块不供明说；葡语备注）' + AF + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（PeeringDB 法定名 + 地址 + ASN + KP 职务；NUIT 未取）。')
row('SB-580', 'Paul Nsavyumwami（布隆迪；**nsavyumwamip@gmail.com、无公司 → 0 查**）— 曾要求出合同「2 光 6 管理」；2024-03 对 2 光 8 PoE 管理回「price」，2025-10 对 2.5G / 10G 回「price」；WA 已加；19 次推送 2 次回复', 'BI',
    '0 查（gmail + 无公司）；2026-10-29', '', '0 查', '互动中（两次要价）', '—', '个人 / 微型', '网络设备采购（布隆迪）', '未取（+257 71 736 181）', '个人',
    ['Paul Nsavyumwami — 联系人（研究档 KP；nsavyumwamip@gmail.com；WA 已加）= 收件人'],
    '**两次要价 + 曾要合同 → 集成商 25% B，一页纸一次 + PI（STI-288DGGPM $137 / STC-228GP $33 一口价 + MOQ 1；2.5G / 10G 等 SB-263 口径不报；预付 100%）' + AF + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次 + PI（预付 100%）；0 查。')
row('SB-639', 'T3K Technology Co., Ltd.（缅甸；Kyaw Aung Myint；**kyawam@hotmail.com、无域名 → 0 查**）— IT 公司；需求工业 4 光 8 电；2024-05 对 mini 工业机「暂时没需求」；WA 19 次无实质回复', 'MM',
    '0 查（hotmail + 无域名；DICA 不开放）；2026-10-29', '', '0 查', '互动中（婉拒 1 次）', '—', 'Co., Ltd.（表内）', 'IT（缅甸）', '未取（+95 97 931 14588）', '微型（推定）',
    ['Kyaw Aung Myint — 联系人（研究档 KP；kyawam@hotmail.com；WA 已加）'],
    '**婉拒「暂时没需求」+ 19×0 → 不动（B 保留；来询按集成商 25% 报 STI-488DGGPM $147）**' + AS, '不动（婉拒 + 19×0）；0 查。')
row('SB-916', 'Skipod Manufacture Pvt Ltd（skipod.lk；**rooster.jobs / BOI 报道：斯里兰卡首家运动模拟器制造商，BOI Section 17 批准公司；厂区 Mirigama Export Processing Zone；注册办公 215 R A De Mel Mawatha, Colombo 3；母公司纽约 SkiPod（Continam Group 投资），一期 300 万美元；主市场北美 / 欧洲 / UAE**）；ROC 号 1 查未得 → 部分坐实；2026 阿里 RFQ「10 个 8 电口」（设备内嵌）；KP Akaloosha Dolage；未跟进', 'LK',
    'LK · 1 次检索：rooster.jobs/company/156343（Skipod Manufacture Pvt Ltd；BOI section 17 approved；Mirigama Export Processing Zone；215 R A De Mel Mawatha, Colombo 3）+ themorning.lk 2025-12 / hirunews（US-backed SkiPod invests US$ 3mn；BOI agreement）；ROC 未得；2026-10-29', 'https://rooster.jobs/company/156343',
    '未取（ROC 号 1 查未得；BOI Section 17）', '营业中（2025-12 BOI 签约 + 招聘）', '未取（2025 建厂）', 'Pvt Ltd（BOI 外资制造）', '运动模拟器制造（米里加马出口加工区）', 'Mirigama Export Processing Zone, Sri Lanka（注册办公 215 R A De Mel Mawatha, Colombo 00300）', '小型（新厂）',
    ['Akaloosha Dolage — 联系人（研究档 KP；akalooshad@skipod.lk）= 收件人'],
    '**设备制造商 RFQ 10 × 8 电口（内嵌）→ 贴标 OEM 30% B，一页纸一次（STI-280GE $46.6 工业 8 GE / 商用 8 GE 按主表 ×10 一口价 + 中性 / 贴标 + 付费样机 + 3 年工业保修）' + AS + '**；回信 → 加厚（OEM 品牌商优先级最高）',
    '贴标 OEM 30%（设备内嵌）；一页纸一次（预付 100%）；部分坐实（BOI 公开报道 + 注册办公地址；ROC 未取）。')
row('SB-920', 'BLUE SKILL S.A.S.（原 Blue Skill Ltda.；blueskill.co；**RUES 镜像（larepublica / empresite）：NIT 805017291-1；Valle del Cauca, Jamundí；MICRO；活动 = IT 咨询 / 设施管理；官网 contactenos：Calle 2 # 22-175, Oficina 303, Centro Comercial Alfaguara, Jamundí – Valle；(2) 592 4547；Gerencia General javier.zuniga@**）→ 坐实；阿里询盘「2 光 4 PoE 5 个」；KP Francisco Javier Zúñiga = Gerente General；1 次跟进无回复', 'CO',
    'CO · 1 次检索：empresas.larepublica.co/colombia/valle-del-cauca/jamundi/blue-skill-s-a-s-805017291（BLUE SKILL S.A.S.；NIT 805017291；JAMUNDI；MICRO）+ empresite（NIT 8050172911；SOCIEDAD POR ACCIONES SIMPLIFICADA；CALLE 2 22 175 OF 303）+ blueskill.co/contactenos.html（Gerencia General javier.zuniga@blueskill.co）；2026-10-29', 'https://empresas.larepublica.co/colombia/valle-del-cauca/jamundi/blue-skill-s-a-s-805017291',
    'NIT 805017291-1', '登记在册（RUES 镜像）', '未取', 'S.A.S.', '电信 / 安防技术服务（哈蒙迪，考卡山谷省）', 'Calle 2 # 22-175, Oficina 303, Centro Comercial Alfaguara, Jamundí, Valle del Cauca, Colombia', '微型（MICRO）',
    ['Francisco Javier Zúñiga — Gerencia General（官网 2026-10-29 吻合；研究档 KP；javier.zuniga@blueskill.co）= 收件人'],
    '**总经理本人询盘 2 光 4 PoE ×5 → 集成商 25% B，一页纸一次（STI-244DGGPM $121 2 SFP + 4 PoE 管理 ×5 / STI-154GP 一口价 + MOQ 1 + 付费样机；西语备注）' + LA + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；坐实（NIT + 法律形式 + 地址 + 总经理）。')
row('SB-930', 'Socra SpA（socraonline.com / socra.cl；**官网：Av. Las Condes 6770, Of. 202, Santiago 7560759；+56 2 2249 7726；WA +56 9 7972 0669；ventasweb@；矿业工业品分销（自动化 / 接触器 / 继电器 / 传感器；欧美亚供应商联盟）**）；RUT 1 查未得 → 部分坐实；阿里询盘「百兆收发器」（百兆 MC 不供）；KP Santiago de la Cruz（product marketer）；未跟进', 'CL',
    'CL · 1 次检索：socra.cl（Socra SpA；ventasweb@socra.cl；(+56) 9 7972 0669；(+56) 2 22497726；Av Las condes 6770 OF 202 Santiago）+ automa.net（Socra Spa；mining industry；Av. Las Condes 6770 OF 202；7560759）+ socraonline.com/nosotros；RUT 未得；2026-10-29', 'https://socra.cl/',
    '未取（RUT 1 查未得）', '营业中（官网 2026）', '未取（「young company」）', 'SpA', '矿业工业品分销（圣地亚哥）', 'Av. Las Condes 6770, Oficina 202, Las Condes, Santiago 7560759, Chile', '微型',
    ['Santiago de la Cruz — Product Marketer（研究档 KP；ventasweb@socraonline.com）= 收件人'],
    '**矿业工业品分销商 + 询盘 MC → 分销 20% B，一页纸一次（STC-110XGE $65 千兆 / 万兆 MC + STI-280GE $46.6 / STI-288DGGPM $137 工业线 一口价 + MOQ 1；百兆 MC 不供明说；西语备注）' + LA + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网地址 + 电话；RUT 未取）。')
row('SB-969', '3STI Technologies（尼日尔尼亚美；3sti-technologies.com = 未完成模板站；Issa Hamadou Seyni Laboukoye；+227 90 70 70 77；**无可查主体 → 0 查**）— 阿里询盘「升压 5 口」（不供）；WA 无实质回复', 'NE',
    '0 查（模板站 + 无公开资料）；2026-10-29', '', '0 查', '存续待核（模板站）', '—', '未取', 'IT（尼亚美）', '未取', '微型（推定）',
    ['Issa Hamadou Seyni Laboukoye — 联系人（研究档 KP；issa.hamadou@3sti-technologies.com）'],
    '**需求升压 PoE（不供）+ 模板站 → 不动（B 保留；来询按集成商 25% 报 STC-028GP）**' + AF, '不动（产品不对位 + 查无实体）；0 查。')
