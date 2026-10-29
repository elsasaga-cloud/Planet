#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 123 批（T29-U114，公司底数第四十一轮 · B 池收尾段三 = **B 池清零**：DZ 2 + KW 2 + EC 2 + EU 国别待核 2 + NZ 2 + NP 2 + OM 2 + JO 2 + 单户 20 = 36 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 成立 / 总部 / 规模 / 定性 回写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/other_registry_2026-10-27.json（batch=123 行）。
本批定性：升 A 候选 2 ★（SB-1134 Conexión de Redes 总经理三次真回 + CENTEC 核心机「Interesting solution」→ **建议升 A（Simon 定）**；SB-047 Topica 回信点名 16 口 → 回信即升）；回访 2（SB-125 Anfiris 样品成单 / SB-463 Penda SFP 样品成单）；
一页纸一次 · 集成商 25% 19（SB-331 RETELEM 国企 / SB-117 Softline 欠答 / SB-530 DSS / SB-334 / SB-335 WA / SB-376 GST LLC / SB-689 TIS / SB-482 KEME-TEC RFQ / SB-035 NANO ISP / SB-1134 ★ / SB-125 回访 / SB-168 WIMEX / SB-182 最后一次 / SB-310 Arcan ISAF / SB-463 回访 / SB-499 最后一次 / SB-564 VOIPTECH / SB-580 + PI / SB-920 Blue Skill NIT）；
一页纸一次 · 分销 20% 9（SB-196 EURODIGITAL UAB / SB-316 SWL / SB-319 Viewtech / SB-785 Smart Systems / SB-047 ★ / SB-1103 ARA / SB-338 Max Protect 样品已购 / SB-339 最后一次 / SB-930 Socra）；
一页纸一次 · 贴标 OEM 30% 2（SB-560 WoMaster 同行补 SKU 最后一次 / SB-916 SkiPod 设备内嵌）；
不动 6（SB-1110 WDM / SB-124 Telconet 大型运营商 + SFP / SB-517 GPON + 路由 / SB-1109 光模块 / SB-639 婉拒 / SB-969 升压 PoE）。
坐实 4（SB-124 RUC 0991327371001 / SB-196 kodas 300638881 / SB-319 Co. No. 1763634 / SB-920 NIT 805017291-1）/ 部分坐实 16（SB-331 / 530 / 560 / 316 / 376 / 482 / 785 / 035 / 047 / 1103 / 1134 / 168 / 338 / 564 / 916 / 930）/ 未坐实 2（SB-689 / 310）/ 0 查 14（SB-1110 / 117 / 517 / 334 / 335 / 1109 / 125 / 182 / 339 / 463 / 499 / 580 / 639 / 969）。
KP 坐实 = 老板 / 总经理 / 法人本人 4（SB-785 Motaz Alsharif Owner / SB-1134 Antonio Guadron Gerente General / SB-920 Javier Zúñiga Gerencia General / SB-564 Manuel Manjala CTO）；新增 KP 4（SB-124 Marion Topic Granados 法定代表人 / SB-196 Saulius Razlevičius Vadovas / SB-035 Tshering Norbu MD / SB-316 Andrew Jones MD 角色）。
**country_fix 3（SB-196 欧洲 → 立陶宛：登记码 300638881 考纳斯；SB-560 欧洲 → 西班牙：WoMaster Europe 巴塞罗那总部；SB-517 厄瓜多尔 → 尼加拉瓜：仅号段 +505，Simon 可回正）**。
路径实测：EC（BVG 发行人页 / ARCOTEL 公文 RUC ✓）；LT（rekvi.lt ✓ 1 查即得）；NZ（公司号镜像 ✓；D&B 法定名）；CO（RUES 镜像 larepublica / empresite ✓）；MZ（PeeringDB 法定名 + 地址 ✓）；LK（BOI 报道 + 招聘页）；DZ / KW / OM / JO / BT / MN / BD / SV / MR / TN / CL = 官网页脚 + 名录（CNRC / CR / MOCI / RJSC / RNE / RUT ✗）；LY 同名干扰 → 未坐实。
**B 池清零：公司底数主线自此转入「A 90 复核 + 新入库即查」常态。**
Simon 待决：SB-1134 建议升 A；SB-196 / 560 / 517 国别更正；SB-047 回信即升；SB-117 / SB-047 欠答一页纸优先。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 123 批 官方登记核实 2026-10-29）'
DZ = '— 阿尔及利亚常规：英文稿（法语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳'
KW = '— 科威特常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 科威特城'
EC = '— 厄瓜多尔常规：英文稿（西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 瓜亚基尔'
EU = '— 欧盟常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP（买方清关）；周四 12–14 当地'
NZ = '— 新西兰常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 奥克兰；周二 / 周四 09–11 NZST'
NP = '— 尼泊尔常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方经加尔各答 / 空运清关）'
OM = '— 阿曼常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 马斯喀特'
JO = '— 约旦常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 安曼'
BT = '— 不丹常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方经加尔各答 / 空运清关）'
MN = '— 蒙古常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 乌兰巴托'
AF = '— 非洲常规：英文稿（法语区附法语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳；周二 / 周四 10–12 当地'
LA = '— 拉美常规：英文稿（西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP；周二 / 周四 10–12 当地'
AS = '— 亚洲常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳；周二 / 周四 10–12 当地'
KG = '— 吉尔吉斯斯坦常规：英文稿（俄语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 比什凯克'
UPD = {
    # ---------------- DZ 2 ----------------
    'SB-1110': [{'kp_match': 'amineachoura21', 'role': '联系人（研究档 KP）— 不动：需求 WDM（不供）+ 无公司 ' + DZ + TAG},
                {'facts': {'legal_name': '未取（0 查：gmail + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（阿尔及利亚；+213 669 116 595）' + TAG, 'size': '个人' + TAG,
                           'other': '第 123 批：**不动（产品不对位）**；0 查' + TAG}}],
    'SB-331': [{'kp_match': 'hichem.akchiche', 'role': '联系人（研究档 KP；WA 已加；2024 要工业交换机 datasheet、对 2 光 8 PoE 有兴趣）= 收件人 — 一页纸一次：集成商 25% B、STI-288DGGPM $137 L2 管理 / STI-288GPM $78.9 非管理 一口价 + MOQ 1 + 付费样机；关键基础设施按单核；法语备注 ' + DZ + TAG},
               {'facts': {'legal_name': 'EPE RETELEM SPA（ex-SONATITE；ELEC EL DJAZAIR 控股；RC / NIF 1 查未得）', 'founded': '1971（SONATITE）' + TAG, 'hq': '54, Rue Omar Benaissa, Bab El Oued, Alger, Algeria' + TAG, 'size': '中型（200–500）' + TAG,
                          'other': '第 123 批：国企网络 / 光纤 / 数据中心 / SCADA 集成商 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（名录地址 + 人数）' + TAG}}],
    # ---------------- KW 2 ----------------
    'SB-117': [{'kp_match': 'rajaanand42', 'role': '联系人（研究档 KP；WA 已加；2025-11 要公司资料 + 价格，欠答）= 收件人 — 一页纸一次：集成商 25% B、工业 2 光 16 电 PoE 按主表 + STI-288DGGPM $137 / STC-2216GP 一口价 + 公司一页简介 + MOQ 1 + 付费样机 ' + KW + TAG},
               {'facts': {'legal_name': 'Softline Technology（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（科威特；+965 9415 7777）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：主动要资料 + 价格（欠答）→ **一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-530': [{'kp_match': 'majdi@', 'role': '表内联系人（研究档 KP）= 收件人 — 一页纸一次：集成商 25% B、STI-288DGGPM $137 / STI-288GPM $78.9 工业 2 光 8 PoE + STC-2224GP $86 一口价 + MOQ 1 + 付费样机；在用品牌不点名 ' + KW + TAG},
               {'facts': {'legal_name': 'Digital Security Systems Est.（DSS；CR 号 1 查未得）', 'founded': '未取' + TAG, 'hq': '1st Floor, Office 15, Ahmad Al Jaber Street, Sharq, P.O. Box 631, Dasman 15457, Kuwait City, Kuwait（+965 2220 0023）' + TAG, 'size': '中小型' + TAG,
                          'other': '第 123 批：安防 SI（Sensormatic / DSC / Software House 代理；ONV 工业 FS 在用）→ **集成商 25% 一页纸一次（预付 100%）**；15×0；部分坐实（官网地址 + 伙伴页）' + TAG}}],
    # ---------------- EC 2 ----------------
    'SB-124': [{'add_kp': {'name': 'Marion Tomislav Topic Granados', 'role': 'Gerente General / Representante Legal（BVG 发行人页 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'TELCONET S.A.（RUC 0991327371001；BVG 登记发行人；ARCOTEL Título Habilitante 1795361）', 'founded': '未取' + TAG, 'hq': 'Av. Luis Orrantia SL. 21 y Av. V.H. Sicouret, Kennedy Norte, Guayaquil, Ecuador' + TAG, 'size': '大型' + TAG,
                          'other': '第 123 批：大型光纤运营商 + 主需求 SFP（不供）+ 无 KP + 零互动 → **不动（B 保留；运营商按单核）**；坐实（RUC + 法定代表人 + 法定地址）' + TAG}}],
    'SB-517': [{'country_fix': '尼加拉瓜'},
               {'kp_name': 'Ernesto Guevara', 'role': 'WA 联系人（无邮箱 / 公司；号段 +505 = 尼加拉瓜）— 不动：需求 GPON + 路由器（不供）+ 18×1 ' + TAG},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 公司）', 'founded': '未取' + TAG, 'hq': '未取（按号段 +505 为尼加拉瓜；表内厄瓜多尔疑误）' + TAG, 'size': '个人' + TAG,
                          'other': '第 123 批：表内国别厄瓜多尔 ↔ 电话 +505 尼加拉瓜号段 → country_fix 尼加拉瓜（Simon 可回正）；**不动（产品不对位）**；0 查' + TAG}}],
    # ---------------- EU 国别待核 2 ----------------
    'SB-196': [{'country_fix': '立陶宛'},
               {'kp_match': 'info@extradigital', 'role': '来信署名人（研究档 KP）= 收件人 — 一页纸一次：分销 20% B、STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 整箱一口价 + MOQ 1 + 付费样机；CE / RoHS / REACH；在售品牌不点名 ' + EU + TAG},
               {'add_kp': {'name': 'Saulius Razlevičius', 'role': 'Vadovas / 董事（rekvi.lt 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'UAB "Eurodigital"（Įmonės kodas 300638881；PVM LT100002890717；e-shop ExtraDigital）', 'founded': '2007-01-29' + TAG, 'hq': 'Žemaičių g. 31-301, LT-44175 Kaunas, Lithuania（+370 603 88188）' + TAG, 'size': '小型（Sodra 2026-04 员工 13）' + TAG,
                          'other': '第 123 批：表内「欧洲（国别未填）」→ country_fix 立陶宛；泛欧 Dahua 分销电商 → **分销 20% 一页纸一次（预付）**；坐实（登记码 + VAT + 成立日 + 地址 + 董事）' + TAG}}],
    'SB-560': [{'country_fix': '西班牙'},
               {'kp_match': 'info@womaster', 'role': '欧洲站公共箱（未具名）— 最后一次一页纸：贴标 OEM 30% B、STI-288DGGPM $137 / STI-0240GE $130 贴标补 SKU + 贴标 MOQ + 付费样机；1U 机架工业 / 串口服务器不供明说 ' + EU + TAG},
               {'facts': {'legal_name': 'WoMaster Europe（WoMaster Group 欧洲总部；集团 QNAP / HMS / HolyStone 合资；ES / TW 登记号 1 查未得）', 'founded': '未取（集团 20+ 年）' + TAG, 'hq': 'Barcelona, Spain（欧洲总部；业务总部 New Taipei）' + TAG, 'size': '中型（集团；自有 EMS）' + TAG,
                          'other': '第 123 批：表内「欧洲」→ country_fix 西班牙；同行品牌 + 自有工厂，表内「自己的 logo」→ **贴标 OEM 30% 最后一次一页纸（预付）**；16×0；部分坐实（官网总部 + 集团背景）' + TAG}}],
    # ---------------- NZ 2 ----------------
    'SB-316': [{'kp_match': 'jabe@', 'role': 'Technical Sales Representative（研究档 KP）= 收件人 — 一页纸一次：分销 20% B、STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 整箱一口价 + MOQ 1 + 付费样机；中性包装；在售品牌不点名 ' + NZ + TAG},
               {'kp_match': 'trade@swl', 'role': 'Managing Director / Key Principal（D&B + ZoomInfo 2026-10-29）' + TAG},
               {'facts': {'legal_name': 'Security Wholesale 2001 Limited（DBA SWL；NZBN 1 查未得）', 'founded': '2001（名称推定）' + TAG, 'hq': '922 Great South Road, Penrose, Auckland 1061, New Zealand（基督城分部 4/91 Byron St）' + TAG, 'size': '小型' + TAG,
                          'other': '第 123 批：本土安防批发（Provision-ISR / Ajax / DSC；Utepo 在售）→ **分销 20% 一页纸一次（预付 100%）**；部分坐实（D&B 法定名 + 地址 + MD）' + TAG}}],
    'SB-319': [{'kp_match': 'matthew@', 'role': 'Commercial Manager（研究档 KP）= 收件人 — 一页纸一次：分销 20% B、STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 一口价 + MOQ 1 + 付费样机；车载 / 宽温 STI-054GP；在售品牌不点名 ' + NZ + TAG},
               {'kp_name': 'Darren Jenkinson', 'role': 'Managing Director / Director（NZ Companies 镜像 + LinkedIn 2026-10-29）' + TAG},
               {'facts': {'legal_name': 'VIEWTECH LIMITED（Company No. 1763634；NZBN 9429034325599；Registered）', 'founded': '2006-02-01' + TAG, 'hq': '97 Wordsworth Street, Sydenham, Christchurch 8023, New Zealand（注册地 Unit 4, 211 Ferry Rd, Christchurch 8011）' + TAG, 'size': '微型（2–10）' + TAG,
                          'other': '第 123 批：CCTV 固定 + 车载 + 安防批发（Utepo / Dahua 在售）→ **分销 20% 一页纸一次（预付 100%）**；坐实（公司号 + NZBN + 成立日 + 董事）' + TAG}}],
    # ---------------- NP 2 ----------------
    'SB-334': [{'kp_match': 'dtechnic02', 'role': '联系人（研究档 KP；WA 已加）= 收件人 — WA 一页纸一次：集成商 25% B、STI-054GP / STI-280GE $46.6 一口价 + MOQ 1；竞品不点名 ' + NP + TAG},
               {'facts': {'legal_name': 'DG Enterprises（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（尼泊尔；+977 986 863 1483）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：明确口型 5 电口工业 → **WA 一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-335': [{'kp_match': 'pchhatra02', 'role': '联系人（研究档 KP；WA 已加）= 收件人 — WA 一页纸一次：集成商 25% B、STI-288DGGPM $137 / STC-228GP $33 一口价 + MOQ 1；一句话问是否要 PoE ' + NP + TAG},
               {'facts': {'legal_name': 'Golden Hub Nepal Pvt. Ltd.（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（尼泊尔；+977 985 284 9417）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：明确口型 2 光 10 电 → **WA 一页纸一次（预付 100%）**；0 查' + TAG}}],
    # ---------------- OM 2 ----------------
    'SB-376': [{'kp_match': 'a.engineering@', 'role': '工程部（研究档 KP；自站询盘 1 光 4 工业）= 收件人 — 一页纸一次：集成商 25% B、STI-154GP / STI-054GP 一口价 + MOQ 1 + 付费样机；百兆版不供明说 ' + OM + TAG},
               {'facts': {'legal_name': 'GLOBAL SECURITY TECHNOLOGY LLC（品牌 Leamratech；CR 号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Flat 609–606, 6th Floor, Business Center Building, Al Khuwair, 3341 Way, Muscat, Oman（+968 2448 0700）' + TAG, 'size': '小型' + TAG,
                          'other': '第 123 批：安防 / 生物识别 / LED 显示集成 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网法定名 + 地址）' + TAG}}],
    'SB-689': [{'kp_match': 'mamun@', 'role': '联系人（研究档 KP；阿里询盘导轨式 PoE 管理 / 非管理）= 收件人 — 一页纸一次：集成商 25% B、STI-288DGGPM $137 管理 + STI-288GPM $78.9 非管理 + STI-054GP 一口价 + MOQ 1 + 付费样机 ' + OM + TAG},
               {'facts': {'legal_name': 'TIS Control Oman（mkseoman.com；地址 / CR 1 查未得）', 'founded': '未取' + TAG, 'hq': '未取（Muscat, Oman）' + TAG, 'size': '小型' + TAG,
                          'other': '第 123 批：智能家居 / 弱电品牌经销（2026-04 仍在招聘）→ **集成商 25% 一页纸一次（预付 100%）**；未坐实' + TAG}}],
    # ---------------- JO 2 ----------------
    'SB-482': [{'kp_match': 'projects@keme', 'role': 'Project Manager（研究档 KP；阿里 RFQ 24 口管理）= 收件人 — 一页纸一次：集成商 25% B、STC-4424GCPM $165 24 PoE + 4 SFP L2+ / 24 GE 非 PoE 管理版 按主表 一口价 + MOQ 1 + 付费样机；一句话问是否要 PoE ' + JO + TAG},
               {'facts': {'legal_name': 'Khaleel Electro Mechanical Est.（KEME-TEC；مؤسسة خليل قطناني للكهروميكانيك；登记号 1 查未得）', 'founded': '2008' + TAG, 'hq': 'Al-Hizam Street, Abu Alanda, Amman, Jordan（+962 6 475 3322）' + TAG, 'size': '小型' + TAG,
                          'other': '第 123 批：工业自动化 / 机电供应商 RFQ → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网成立年 + 地址）' + TAG}}],
    'SB-785': [{'kp_match': 'motaz@', 'role': 'Owner（prospeo 2026-10-29 吻合；研究档 KP）= 收件人 — 一页纸一次：分销 20% B、STC-4424GCPM $165 / STC-424XGGPM-280W $198 / STC-448XGGPM $335 一口价 + MOQ 1 + 付费样机；在供品牌不点名 ' + JO + TAG},
               {'facts': {'legal_name': 'Smart Systems For Computers（شركة الأنظمة الذكية；登记号 1 查未得）', 'founded': '1991' + TAG, 'hq': 'Jawhara Halima Complex, 6 Wasfi Al Tal Street (Gardens), Amman, Jordan（+962 6 562 7771）' + TAG, 'size': '小型（16–25）' + TAG,
                          'other': '第 123 批：电脑门店 + 网络集成（BDCOM 在供，大口交换机常购）→ **分销 20% 一页纸一次（预付 100%）**；部分坐实（名录成立年 + 地址 + Owner）' + TAG}}],
    # ---------------- BT 1 ----------------
    'SB-035': [{'kp_match': 'sonam@nano', 'role': '表内联系人（研究档 KP；WA 已加；要收发器 / SFP / PoE 交换机）= 收件人 — 一页纸一次：集成商 25% B、STC-4424GCPM $165 / STC-424XGGPM-280W $198 汇聚 + STC-228GP $33 接入 一口价 + MOQ 1；SFP / 收发器不供明说 ' + BT + TAG},
               {'add_kp': {'name': 'Tshering Norbu', 'role': 'Managing Director（官网 2026-10-29；曾任 Thimphu TechPark Ltd 董事；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'NANO（不丹持牌 ISP；公司注册号 1 查未得）', 'founded': '2017（入市）' + TAG, 'hq': 'IT Park, PO Box 633, Wangchuktaba, Babesa, Thimphu, Bhutan（+975 2 330330）' + TAG, 'size': '微型（约 11）' + TAG,
                          'other': '第 123 批：三家持独立国际网关 ISP 之一 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网注册地址 + MD）' + TAG}}],
    # ---------------- MN 1 ----------------
    'SB-047': [{'kp_match': 'info@topica', 'role': '收件箱（回信署名 Bayar；2025-11 点名「需要 16 port 的」，欠答）= 收件人 — 一页纸：分销 20% B、STC-2216GP $63–76 / 16 口管理版 按主表 / STC-2224GP $86 一口价 + MOQ 1 + 付费样机；在售品牌不点名 ' + MN + TAG},
               {'facts': {'legal_name': 'Topica LLC（Топика ХХК；注册号 1 查未得）', 'founded': '2005' + TAG, 'hq': 'Office 3A, 1st Khoroo, Chingeltei District, Ulaanbaatar, Mongolia（+976 7012 5001 / 5002）' + TAG, 'size': '中小型（名录 51–200 偏高）' + TAG,
                          'other': '第 123 批：★ 网店 + 分销 + 集成（LuxDev 医院 IT 中标），回信点名 16 口 → **分销 20% 一页纸（预付 100%）；回信即升 A 候选**；部分坐实（名录成立年 + 地址）' + TAG}}],
    # ---------------- 单户 18 ----------------
    'SB-1103': [{'kp_match': 'smchan91', 'role': 'Sr. Executive, Support & Maintenance（官网 2026-10-29；非决策人；support@ara.com.bd 退信）= 收件人（请转采购）— 一页纸一次：分销 20% B、STC-028GP $28 / STC-228GP $33 / STC-110XGE $65 一口价 + MOQ 1 + 付费样机 ' + AS + TAG},
                {'facts': {'legal_name': 'ARA Technologies Limited（Advanced Resources And Technologies；RJSC 号 1 查未得）', 'founded': '2005' + TAG, 'hq': 'Banani C/A 17, Banani, Dhaka 1213, Bangladesh（工厂 Bhaluka, Mymensingh；+880 1678 004434）' + TAG, 'size': '小型（约 20）' + TAG,
                           'other': '第 123 批：网络 / 光电产品制造 + 分销，进口过中国品牌 → **分销 20% 一页纸一次（预付 100%）**；部分坐实（官网地址 + 成立年 + KP 职务）' + TAG}}],
    'SB-1109': [{'facts': {'legal_name': '未取（0 查：gmail + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（埃塞俄比亚；+251 955 019 650）' + TAG, 'size': '个人' + TAG,
                           'other': '第 123 批：需求光模块（不供）+ 未读 → **不动（B 保留）**；0 查' + TAG}}],
    'SB-1134': [{'kp_match': 'gerencia@', 'role': 'Gerente General（官网 gerencia@ 吻合；研究档 KP；三次真回）= 收件人 — 一页纸 + 规格书：STH-8C48DX-HSI $4,800 / STH-2C24XF-HSI $1,500 CENTEC + 接入 STC-424XGGPM-280W $198 / STC-4424GCPM $165 + 付费样机；西语备注 ' + LA + TAG},
                {'facts': {'legal_name': 'Conexión de Redes de Centro América（NIT 1 查未得）', 'founded': '未取' + TAG, 'hq': 'San Salvador, El Salvador（+503 2262-1049）' + TAG, 'size': '小型' + TAG,
                           'other': '第 123 批：★ 代客转发型集成商，总经理三次真回 + CENTEC「Interesting solution」→ **建议升 A（Simon 定）；先按集成商 25% 一页纸 + 规格书**；部分坐实（官网地址 + 电话 + GM 邮箱）' + TAG}}],
    'SB-125': [{'kp_match': 'repintalimitada', 'role': '联系人（研究档 KP；8 口交换机样品已成单）= 收件人 — 回访一页纸一次：集成商 25% B、样品同型复购价 + STC-028GP $28 一口价 + MOQ 1；葡语备注 ' + AF + TAG},
               {'facts': {'legal_name': 'Anfiris, Lda（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（安哥拉；+244 923 545 606）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：样品成单客户 → **回访一页纸一次（预付 100%）；回信即升 A 候选**；0 查' + TAG}}],
    'SB-168': [{'kp_match': 'moustapha@wimex', 'role': '表内联系人（研究档 KP；官网合作页同邮箱；WA 已加；曾回「2 光 4」小机价）= 收件人 — 一页纸一次：集成商 25% B、STI-244DGGPM $121 / STI-154GP 一口价 + MOQ 1 + 付费样机；80 km 光模块不供明说；法语备注 ' + AF + TAG},
               {'kp_name': 'Mohamed Waled', 'role': 'PDG（集团总裁；研究档；无公开邮箱）' + TAG},
               {'facts': {'legal_name': 'Wimex Technologies（Groupe WIMEX；RC / NIF 1 查未得）', 'founded': '1993 / 1995（集团）' + TAG, 'hq': "55 Ilot C, Zone Château d'Eau, BP 3384, Nouakchott, Mauritania（+222 45 25 23 56）" + TAG, 'size': '中型（51–200）' + TAG,
                          'other': '第 123 批：电信工程 / 系统集成集团 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网地址 + BP）' + TAG}}],
    'SB-182': [{'kp_match': 'lpogiso', 'role': '联系人（研究档 KP；WA 已加；2025-06「slow business」）= 收件人 — 最后一次一页纸：集成商 25% B、STI-154GP / STI-054GP 一口价 + MOQ 1；一句话问是否要 PoE ' + AF + TAG},
               {'facts': {'legal_name': 'Netbowl (Pty) Ltd（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（博茨瓦纳；+267 71 704 050）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：明确口型 1 光 4 工业 + 曾谈项目 → **最后一次一页纸（预付 100%）**；0 查' + TAG}}],
    'SB-310': [{'kp_match': 'info@arcanlibya', 'role': 'General Manager（研究档 KP；ISAF 2025 要价；WA 已加）= 收件人 — 一页纸一次 + 工业线价目：集成商 25% B、8 光 8 电工业 按主表 + STI-288DGGPM $137 / STI-488DGGPM $147 一口价 + MOQ 1 + 付费样机；FOB 深圳 买方货代 ' + AF + TAG},
               {'facts': {'legal_name': 'Arcan Libya（1 查仅同名 ARKAN 干扰；未匹配）', 'founded': '未取' + TAG, 'hq': '未取（Tripoli, Libya；+218 21 712 8108）' + TAG, 'size': '小型（推定）' + TAG,
                          'other': '第 123 批：展会主动要价 → **集成商 25% 一页纸一次 + 价目（预付 100%）**；未坐实' + TAG}}],
    'SB-338': [{'kp_match': 'direction@max-protect', 'role': 'Manager（研究档 KP；$40 购 2 光 8 PoE 管理样品）= 收件人 — 一页纸一次：分销 20% B、问测试结果 + STC-228GP $33 / STC-028GP $28 整箱 10 台一口价 + MOQ 1；法语；在售品牌不点名 ' + AF + TAG},
               {'facts': {'legal_name': 'Max Protect（哈马马特；RNE 号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Avenue Habib Bourguiba, 8050 Hammamet, Tunisia（第二店 Avenue Abou Dhabi, Route de Nabeul；72 324 111）' + TAG, 'size': '微型（2 门店）' + TAG,
                          'other': '第 123 批：安防零售 / 分销 / 安装（Dahua / Uniview / Imou / Ajax），样品已购 → **分销 20% 一页纸一次（预付 100%）**；部分坐实（官网门店地址）' + TAG}}],
    'SB-339': [{'kp_match': 'omegatec3', 'role': '联系人（研究档 KP；自称 Reseller；WA 已加）= 收件人 — 最后一次一页纸 + 商用线价目：分销 20% B、STC-2216GP $63–76 / STC-2224GP $86 一口价 + MOQ 1；12 光 L3 不供明说；法语 ' + AF + TAG},
               {'facts': {'legal_name': 'OMEGATEC SARL（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（喀麦隆；+237 53 283 301）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：Reseller 要 16 口 PoE + 价格表、20×1 → **分销 20% 最后一次一页纸（预付 100%）**；0 查' + TAG}}],
    'SB-463': [{'kp_match': 'bigbocar', 'role': '联系人（研究档 KP；2019 SFP 样品成单）= 收件人 — 回访一页纸一次：集成商 25% B、STC-110XGE $65 + STC-228GP $33 / STC-028GP $28 一口价 + MOQ 1；SFP 不供明说；法语 ' + AF + TAG},
               {'facts': {'legal_name': 'Groupe Penda Telecoms（0 查：hotmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（塞内加尔）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：样品成单客户（有自己的货代）→ **回访一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-499': [{'kp_match': 'b.medvedev11', 'role': 'MIPS 名片（研究档 KP；WA 已加；问过工业 FS / SFP）= 收件人 — 最后一次一页纸：集成商 25% B、STI-280GE $46.6 / STI-288GPM $78.9 / STI-288DGGPM $137 一口价 + MOQ 1；SFP 不供明说；俄语备注 ' + KG + TAG},
               {'facts': {'legal_name': '未取（0 查：mail.ru + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（吉尔吉斯斯坦；+996 555 772 975）' + TAG, 'size': '个人' + TAG,
                          'other': '第 123 批：展会名片、23×0 → **最后一次一页纸（预付 100%）**；0 查' + TAG}}],
    'SB-564': [{'kp_match': 'manjala@', 'role': 'Chief Technology Officer（LinkedIn + PeeringDB 2026-10-29；研究档 KP）= 收件人 — 一页纸一次：集成商 25% B、STC-228GP $33 / STI-288DGGPM $137 / STC-4424GCPM $165 一口价 + MOQ 1 + 付费样机；光模块不供明说；葡语备注 ' + AF + TAG},
               {'facts': {'legal_name': 'VOIPTECH LIMITADA（Latitude / Conecte Internet e Soluções；AS328223；NUIT 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Av. Ho Chi Minh nº 677, 1º andar, Maputo, Mozambique' + TAG, 'size': '小型' + TAG,
                          'other': '第 123 批：ISP（5–10 Gbps，MOZIX 对等）询盘 2 SFP 交换机 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（PeeringDB 法定名 + 地址 + ASN + KP 职务）' + TAG}}],
    'SB-580': [{'kp_match': 'nsavyumwamip', 'role': '联系人（研究档 KP；WA 已加；两次要价 + 曾要合同）= 收件人 — 一页纸一次 + PI：集成商 25% B、STI-288DGGPM $137 / STC-228GP $33 一口价 + MOQ 1；2.5G / 10G 等 SB-263 口径不报 ' + AF + TAG},
               {'facts': {'legal_name': '未取（0 查：gmail + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（布隆迪；+257 71 736 181）' + TAG, 'size': '个人 / 微型' + TAG,
                          'other': '第 123 批：两次要价 → **一页纸一次 + PI（预付 100%）**；0 查' + TAG}}],
    'SB-639': [{'kp_match': 'kyawam', 'role': '联系人（研究档 KP；WA 已加）— 不动：婉拒「暂时没需求」+ 19×0 ' + AS + TAG},
               {'facts': {'legal_name': 'T3K Technology Co., Ltd.（0 查：hotmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（缅甸；+95 97 931 14588）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：**不动（婉拒 + 19×0）**；0 查' + TAG}}],
    'SB-916': [{'kp_match': 'akalooshad', 'role': '联系人（研究档 KP；2026 阿里 RFQ 10 × 8 电口 设备内嵌）= 收件人 — 一页纸一次：贴标 OEM 30% B、STI-280GE $46.6 工业 8 GE / 商用 8 GE 按主表 ×10 一口价 + 中性 / 贴标 + 付费样机 + 3 年工业保修 ' + AS + TAG},
               {'facts': {'legal_name': 'Skipod Manufacture Pvt Ltd（BOI Section 17；母公司纽约 SkiPod / Continam Group；ROC 号 1 查未得）', 'founded': '未取（2025 建厂）' + TAG, 'hq': 'Mirigama Export Processing Zone, Sri Lanka（注册办公 215 R A De Mel Mawatha, Colombo 00300）' + TAG, 'size': '小型（新厂）' + TAG,
                          'other': '第 123 批：运动模拟器制造商（设备内嵌交换机）→ **贴标 OEM 30% 一页纸一次（预付 100%）**；部分坐实（BOI 报道 + 注册办公地址）' + TAG}}],
    'SB-920': [{'kp_match': 'javier.zuniga', 'role': 'Gerencia General（官网 2026-10-29 吻合；研究档 KP；阿里询盘 2 光 4 PoE ×5）= 收件人 — 一页纸一次：集成商 25% B、STI-244DGGPM $121 ×5 / STI-154GP 一口价 + MOQ 1 + 付费样机；西语备注 ' + LA + TAG},
               {'facts': {'legal_name': 'BLUE SKILL S.A.S.（原 Blue Skill Ltda.；NIT 805017291-1；MICRO）', 'founded': '未取' + TAG, 'hq': 'Calle 2 # 22-175, Oficina 303, Centro Comercial Alfaguara, Jamundí, Valle del Cauca, Colombia（(2) 592 4547）' + TAG, 'size': '微型（MICRO）' + TAG,
                          'other': '第 123 批：总经理本人询盘 → **集成商 25% 一页纸一次（预付 100%）**；坐实（NIT + 法律形式 + 地址 + 总经理）' + TAG}}],
    'SB-930': [{'kp_match': 'ventasweb', 'role': 'Product Marketer（研究档 KP；阿里询盘百兆 MC）= 收件人 — 一页纸一次：分销 20% B、STC-110XGE $65 + STI-280GE $46.6 / STI-288DGGPM $137 一口价 + MOQ 1；百兆 MC 不供明说；西语备注 ' + LA + TAG},
               {'facts': {'legal_name': 'Socra SpA（RUT 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Av. Las Condes 6770, Oficina 202, Las Condes, Santiago 7560759, Chile（+56 2 2249 7726）' + TAG, 'size': '微型' + TAG,
                          'other': '第 123 批：矿业工业品分销商 → **分销 20% 一页纸一次（预付 100%）**；部分坐实（官网地址 + 电话）' + TAG}}],
    'SB-969': [{'kp_match': 'issa.hamadou', 'role': '联系人（研究档 KP）— 不动：需求升压 PoE（不供）+ 模板站 ' + AF + TAG},
               {'facts': {'legal_name': '3STI Technologies（0 查：模板站 + 无公开资料）', 'founded': '未取' + TAG, 'hq': '未取（尼亚美；+227 90 70 70 77）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 123 批：**不动（产品不对位 + 查无实体）**；0 查' + TAG}}],
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
