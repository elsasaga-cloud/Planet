#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 122 批（T29-U114，公司底数第四十轮 · B 池收尾段二：TZ 3 + IQ 3 + NG 3 + US 3 + GH 3 + TR 3 + UZ 3 + EG 3 + 国别待核 3 + PE 2 + BH 2 + ZW 2 + QA 2 + UG 2 = 37 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 成立 / 总部 / 规模 / 定性 回写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/other_registry_2026-10-27.json（batch=122 行）。
本批定性：升 A 候选 4 ★（SB-1139 Beltetón CENTEC STH1G 真回 2 次 → 建议升 A（Simon 定）；SB-051 Prestige 老客户 买过 MC + PoE → 回信即升；SB-166 Crown 200 台工业 5 口 + CPSE 面谈 + CTO → 回信即升；SB-976 Boltayev 成交 2 次 → 回信即升）；
一页纸一次 · 集成商 25% 19（SB-122 Tera 证书 85715 / SB-229 Tescom / SB-031 OM Telecom RUC 20600792858 / SB-033 Marvel / SB-1062 Al-Tamyeez / SB-183 Onyx / SB-049 Multi-Link 回访 / SB-051 ★ 回访 / SB-629 C-TECH / SB-582 SmartIntercom 欠答 / SB-1139 ★ / SB-016 WA 最后一次 / SB-373 WA / SB-332 别名邮箱 / SB-701 最后一次 / SB-563 WA / SB-727 WA / SB-903 / SB-817 WA 最后一次）；
一页纸一次 · 分销 20% 8（SB-588 WAN PLANET 十年伙伴 / SB-631 Gigaxysafe / SB-965 VIDCOM / SB-166 ★ WA / SB-340 WA 最后一次 / SB-976 ★ 复购 最后一次 / SB-192 回访 / SB-239 最后一次）；
一页纸一次 · 贴标 OEM 30% 2（SB-991 Tubal SKD / SB-110 iTKATI 自有标）；
不动 8（SB-080 Cyber-Tec 百兆 MC + 域名失效 / SB-671 MyTec 域名失效 19×0 / SB-971 IPS 光端机 / SB-476 注入器 20×0 / SB-587 已有供应商 / SB-608 PON 20×1 / SB-116 光模块 + 婉拒 / SB-973 查无实体）。
坐实 3（SB-122 / 031 / 051）/ 部分坐实 14（SB-229 / 588 / 631 / 817 / 965 / 629 / 971 / 991 / 033 / 1062 / 166 / 110 / 183 / 049）/ 未坐实 4（SB-080 / 671 / 582 / 1139）/ 0 查 16（SB-016 / 373 / 332 / 476 / 701 / 340 / 587 / 563 / 727 / 903 / 608 / 976 / 192 / 116 / 239 / 973）。
KP 坐实 = 老板 / 总经理 / 法人本人 4（SB-588 Sarwar Ibrahim Saeed MD / SB-051 Robert Howell Owner / SB-166 Mohamed Safeer CTO / SB-976 Boltayev 本人）；新增 KP 8（SB-122 Daudi Charles CEO 角色 / SB-631 Kayode Oluwaseyi MD / SB-629 Hamdy Elbadeea MD / SB-991 Fibi Bakhoum Toma / SB-051 William Bye President / SB-049 Divine Ndhlukula MD / SB-110 Sarah Basemera 角色 / SB-1062 收件 Attn）。
法定名补全 / 更正 21；**country_fix 2（SB-051 Prestige → 美国：Sunbiz P16000009000 劳德代尔堡，表内「秘鲁 S.A.C.」误；SB-608 Sadybekov → 哈萨克斯坦：号段 +7 775，表内乌兹别克斯坦疑误）**；域名更正 1（SB-1062 odoo.com → tamyeezsecurity.com）。
路径实测：TZ（BRELA ✗；官网 about + devex；公司自述证书号）；IQ（D&B 法定名 + MD；域名失效 2 户）；NG（businesslist.com.ng 给地址 + MD 邮箱；CAC 未得）；US 个人邮箱 0 查 / Sunbiz 1 查即得；GH（ZoomInfo 地址 + 职务）；TR ISAF 名片 0 查；UZ（goldenpages.uz ИНН 打码）；EG（官网页脚 + RocketReach MD + D&B）；PE（universidadperu RUC + 状态）；BH（官网页脚 W.L.L.）；ZW（集团公开资料）；QA（doha.directory / RocketReach）；UG（eastafricatenders 登记日 / yellow.ug）。
Simon 待决：SB-1139 建议升 A；SB-051 / SB-608 国别更正；SB-051 / SB-166 / SB-976 回信即升；SB-373 / SB-222 WA 问公司名；SB-1139 / SB-582 问国别。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 122 批 官方登记核实 2026-10-29）'
TZ = '— 坦桑尼亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 达市、TBS / TCRA 不声称'
IQ = '— 伊拉克常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方经迪拜 / 土耳其货代清关）'
NG = '— 尼日利亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 拉各斯、SON / NCC 不声称'
US = '— 美国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP（买方清关）、NDAA / TAA / UL 不声称；周三 08–10 当地'
GH = '— 加纳常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 阿克拉'
TR = '— 土耳其常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 伊斯坦布尔；周四 10–12 当地'
UZ = '— 乌兹别克斯坦常规：英文稿（可附俄语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 塔什干、UzStandard 不声称'
KZ = '— 哈萨克斯坦常规：英文稿（可附俄语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 阿拉木图、EAC 不声称'
EG = '— 埃及常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方清关）、NTRA 不声称'
PE = '— 秘鲁常规：英文稿（可附西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 利马'
BH = '— 巴林常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 麦纳麦、TRA 不声称'
ZW = '— 津巴布韦常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 哈拉雷'
QA = '— 卡塔尔常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 多哈、CRA 不声称'
UG = '— 乌干达常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 坎帕拉、UCC 不声称'
UPD = {
    # ---------------- TZ 3 ----------------
    'SB-016': [{'kp_name': 'Richard Jackson', 'role': 'WA 联系人（无邮箱 / 公司）— WA 最后一次一页纸：集成商 25% B、STI-288DGGPM $137 2 光 8 PoE 管理 一口价 + MOQ 1 ' + TZ + TAG},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 公司）', 'founded': '未取' + TAG, 'hq': '未取（坦桑尼亚；+255 768 043 267）' + TAG, 'size': '个人' + TAG,
                          'other': '第 122 批：曾言「要下单」、19×1 → **WA 最后一次一页纸（预付 100%）**；0 查' + TAG}}],
    'SB-122': [{'kp_match': 'rndijuye', 'role': '联系人（研究档 KP；2024–2025 问 5 电口价 / 确认千兆 / 工业 16–24 口「可能会用到」）= 收件人 — 一页纸一次：集成商 25% B、STI-054GP / STI-154GP + STI-288DGGPM $137 / STC-2216GP 一口价 + MOQ 1 + 付费样机；抄 CEO 公共箱 ' + TZ + TAG},
               {'kp_match': 'info@teratech', 'role': 'CEO & Co-Founder（官网 about 2026-10-29；ERB 注册工程师）' + TAG},
               {'facts': {'legal_name': 'Tera Technologies and Engineering Limited（Certificate of Incorporation No. 85715，公司自述；BRELA 未核）', 'founded': '2011-09-09' + TAG, 'hq': 'Plot No. 2283, Block H, Tarangire Street, Africana Drive, Mbezi Beach, P.O. Box 31257, Dar es Salaam, Tanzania（+255 22 270 1612；第二办公 Sinza Block A, Plot 173）' + TAG, 'size': '小型（11–50；约 10 名工程师）' + TAG,
                          'other': '第 122 批：CRB 一级承包商（电信 / ICT / 安防），世行 / TMA 中标 → **集成商 25% 一页纸一次（预付 100%）**；坐实（证书号 + 官网地址 + CEO）' + TAG}}],
    'SB-229': [{'kp_match': 'samuisso', 'role': '联系人（研究档 KP）= 收件人 — 一页纸一次：集成商 25% B、STC-028GP $28 / STC-228GP $33 CCTV PoE 一口价 + MOQ 1；千兆 MC 仅 STC-110XGE $65 明说 ' + TZ + TAG},
               {'facts': {'legal_name': 'TESCOM Company Limited（BRELA 号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Kijitonyama, Dar es Salaam, Tanzania（+255 712 565 698 / +255 738 261 794）' + TAG, 'size': '小型' + TAG,
                          'other': '第 122 批：ICT / 电信工程 + 注册专业供应商两条线 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网地址）' + TAG}}],
    # ---------------- IQ 3 ----------------
    'SB-080': [{'kp_match': 'sarmad@', 'role': '联系人（研究档 KP；WA 已加）— 不动：需求百兆工业 MC（不供）+ 域名失效 + 19×1 ' + IQ + TAG},
               {'facts': {'legal_name': 'Cyber-Tec（1 查无命中；域名 cyber-tec.net 失效）', 'founded': '未取' + TAG, 'hq': '未取（Karbala, Iraq）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 122 批：**不动（产品不对位 + 存续待核）**；未坐实' + TAG}}],
    'SB-588': [{'kp_match': 'sarwar.ibrahim', 'role': 'Managing Director / CEO（D&B 2026-10-29 吻合）= 收件人 — 一页纸一次：分销 20% B、千兆工业 PoE 4 / 8 / 16（STI-054GP / STI-288GPM $78.9 / STI-288DGGPM $137 / STI-488DGGPM $147）一口价 + MOQ 1 + 付费样机；PLANET / Uniview 不点名 ' + IQ + TAG},
               {'facts': {'legal_name': 'WAN Company for Computer Network Design and Installation and Computer Trading Ltd.（DBA WAN Company for Networking Technology；库区登记号 1 查未得）', 'founded': '2005-01-03' + TAG, 'hq': '1st Floor, Ali Namali Building, Salim Street, Sulaymaniyah, Kurdistan Region, Iraq' + TAG, 'size': '中小型' + TAG,
                          'other': '第 122 批：PLANET 十年伙伴 + Teknim 库区代理 + 在线商店 / 培训 / CCTV 展厅 → **分销 20% 一页纸一次（预付 100%）**；部分坐实（D&B 法定名 + 地址 + MD）' + TAG}}],
    'SB-671': [{'kp_match': 'mushtaq@', 'role': '联系人（研究档 KP）— 不动：域名失效 + 19×0 ' + IQ + TAG},
               {'facts': {'legal_name': 'MyTec（伊拉克；1 查仅韩 / 秘 / 美同名）', 'founded': '未取' + TAG, 'hq': '未取（Iraq）' + TAG, 'size': '小型（推定）' + TAG,
                          'other': '第 122 批：**不动（存续待核 + 19×0）**；未坐实' + TAG}}],
    # ---------------- NG 3 ----------------
    'SB-239': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 empicstar2014@gmail.com / WA +234 803 428 6012 — 最后一次一页纸：分销 20% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1；在售品牌不点名 ' + NG + TAG}},
               {'facts': {'legal_name': 'Empicstar（0 查：gmail + 域名失效）', 'founded': '未取' + TAG, 'hq': '未取（尼日利亚）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 122 批：平台转售（TP-Link / ONV 等）、18×1 → **分销 20% 最后一次一页纸（预付 100%）**；0 查' + TAG}}],
    'SB-373': [{'add_kp': {'name': '（未具名 WA 联系人）', 'role': 'WA（2024–2025 五次回复：芯片 / 价目 / 2.5G / MCU）— WA 一页纸一次：集成商 25% B、STC-028GP $28 / STC-228GP $33 一口价 + MOQ 1；2.5G 等 SB-263 口径不报；一句话问公司名 ' + NG + TAG}},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 姓名 / 公司）', 'founded': '未取' + TAG, 'hq': '未取（尼日利亚）' + TAG, 'size': '未知' + TAG,
                          'other': '第 122 批：**WA 一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-631': [{'add_kp': {'name': 'Kayode Oluwaseyi', 'email': 'kayode.oluwaseyi@gigaxysafe.com.ng', 'role': 'Managing Director（businesslist.com.ng 公开页 2022；抄 info@gigaxysafe.com.ng）= 收件人 — 一页纸一次：分销 20% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 / STC-4424GCPM $165 一口价 + MOQ 1 + 付费样机；在售品牌不点名；2.5G 不报 ' + NG + TAG}},
               {'facts': {'legal_name': 'Gigaxysafe Technologies Ltd（CAC RC 号 1 查未得）', 'founded': '2012' + TAG, 'hq': 'Suite 28F, Sabondale Shopping Complex, Obafemi Awolowo Way, Jabi, Abuja, Nigeria（+234 803 930 8003 / +234 702 500 1983）' + TAG, 'size': '微型（约 10 人）' + TAG,
                          'other': '第 122 批：注册安防技术公司（通信 / 安防设备进口分销 + 网店 Cisco / PLANET / Ubiquiti / 2.5G）→ **分销 20% 一页纸一次（预付 100%）**；部分坐实（名录地址 + MD + 成立年）' + TAG}}],
    # ---------------- US 3 ----------------
    'SB-332': [{'kp_match': 'unpledged154', 'role': '自建站询盘人（别名邮箱；WA 已加）= 收件人 — 一页纸一次：集成商 25% B、STI-288DGGPM $137 2 SFP + 8 PoE L2 管理 一口价 + MOQ 1；芯片平台不声称 ' + US + TAG},
               {'facts': {'legal_name': '未取（0 查：Proton 别名邮箱 + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（美国）' + TAG, 'size': '个人' + TAG,
                          'other': '第 122 批：明确机型「2 光 8 PoE 管理」→ **一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-476': [{'add_kp': {'name': 'Wayne', 'role': '联系人（computerwayne@gmail.com）— 不动：需求注入器（不供）+ 20×0 ' + US + TAG}},
               {'facts': {'legal_name': '未取（0 查：gmail + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（美国 +1 318）' + TAG, 'size': '个人 / 微型' + TAG,
                          'other': '第 122 批：**不动（产品不对位 + 20×0）**；0 查' + TAG}}],
    'SB-701': [{'kp_match': 'chk999', 'role': '来信署名人（研究档 KP）= 收件人 — 最后一次一页纸：集成商 25% B、STI-288GPM $78.9 1 SFP + 8 PoE 非管理 一口价 + MOQ 1 ' + US + TAG},
               {'facts': {'legal_name': '未取（0 查：outlook + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（美国 +1 678）' + TAG, 'size': '个人 / 微型' + TAG,
                          'other': '第 122 批：明确机型 + 14×0 → **最后一次一页纸（预付 100%）**；0 查' + TAG}}],
    # ---------------- GH 3 ----------------
    'SB-340': [{'kp_name': 'Abraham Sam', 'role': 'WA 联系人（研究档 KP；两次要价）= 收件人 — WA 最后一次一页纸：分销 20% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1；光端机不供明说 ' + GH + TAG},
               {'facts': {'legal_name': 'ROCKBIOS Limited（0 查：无邮箱 / 域名）', 'founded': '未取' + TAG, 'hq': '未取（加纳；+233 26 465 3169）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 122 批：转售商、19×1 → **分销 20% WA 最后一次一页纸（预付 100%）**；0 查' + TAG}}],
    'SB-587': [{'facts': {'legal_name': 'Truetech Security Solutions（0 查：无邮箱 / 域名；表内联系人姓名疑串行）', 'founded': '未取' + TAG, 'hq': '未取（加纳；+233 20 497 9197）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 122 批：已有供应商（「在和 dja 合作」）+ 18×1 + 无 KP → **不动（B 保留）**；0 查' + TAG}}],
    'SB-817': [{'kp_match': 'info@masstracktech', 'role': 'Technical Manager（ZoomInfo 2026-10-29；2013 起）= 收件人 — WA 最后一次一页纸：集成商 25% B、STI-154GP 一口价 + STI-054GP + MOQ 1 + 付费样机 ' + GH + TAG},
               {'facts': {'legal_name': 'MassTrack Technologies（RGD 号 1 查未得；域名停用）', 'founded': '未取（KP 2013 起）' + TAG, 'hq': 'B33/41 Opposite Trinity Presby Church, Kwashieman, Accra, Ghana（+233 20 648 5957）' + TAG, 'size': '小型' + TAG,
                          'other': '第 122 批：车队 / 车辆跟踪服务商、曾点名「154」、19×0 → **WA 最后一次一页纸（预付 100%）**；部分坐实（ZoomInfo 地址 + 职务）' + TAG}}],
    # ---------------- TR 3 ----------------
    'SB-563': [{'kp_name': 'Holil', 'role': 'ISAF 名片（仅 WA）— WA 一页纸一次：集成商 25% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1 ' + TR + TAG},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 公司）', 'founded': '未取' + TAG, 'hq': '未取（土耳其）' + TAG, 'size': '未知' + TAG,
                          'other': '第 122 批：展会要 PoE 交换机 + 拿彩页 → **WA 一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-727': [{'kp_name': 'Fadi（姓氏待核）', 'role': 'ISAF 名片（仅 WA；英文不佳）— WA 一页纸一次：集成商 25% B、STC-028GP $28 / STC-228GP $33 一口价 + MOQ 1；SFP 不供明说；短句英文 ' + TR + TAG},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 公司）', 'founded': '未取' + TAG, 'hq': '未取（土耳其）' + TAG, 'size': '未知' + TAG,
                          'other': '第 122 批：问过收发器 + 交换机 → **WA 一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-903': [{'kp_match': 'bilecik@', 'role': 'ISAF 名片（hotmail；疑比莱吉克省个体安装商）= 收件人 — 一页纸一次：集成商 25% B、STI-288GPM $78.9 / STI-154GP / STI-054GP 一口价 + MOQ 1 ' + TR + TAG},
               {'facts': {'legal_name': '未取（0 查：hotmail + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（土耳其，疑 Bilecik）' + TAG, 'size': '个人' + TAG,
                          'other': '第 122 批：展会要工业 PoE → **一页纸一次（预付 100%）**；0 查' + TAG}}],
    # ---------------- UZ 3 ----------------
    'SB-608': [{'country_fix': '哈萨克斯坦'},
               {'kp_name': 'Marlen Sadybekov', 'role': 'WA 联系人（无邮箱 / 公司；号段 +7 775 = 哈萨克斯坦）— 不动：需求 PON（不供）+ 20×1 ' + KZ + TAG},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 公司）', 'founded': '未取' + TAG, 'hq': '未取（按号段 +7 775 为哈萨克斯坦；表内乌兹别克斯坦疑误）' + TAG, 'size': '个人' + TAG,
                          'other': '第 122 批：表内国别乌兹别克斯坦 ↔ 电话 +7 775 哈萨克斯坦号段 → country_fix 哈萨克斯坦（Simon 可回正）；**不动（产品不对位 + 20×1）**；0 查' + TAG}}],
    'SB-965': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 info@vidcom.uz Attn: Отдел закупок / Purchasing — 一页纸一次：分销 20% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 CCTV PoE 一口价 + MOQ 1 + 付费样机；在售品牌不点名 ' + UZ + TAG}},
               {'facts': {'legal_name': '"VIDCOM" ООО / VIDCOM Ltd（ИНН 30548****，名录打码）', 'founded': '未取' + TAG, 'hq': 'ул. Арнасай, кв-л Чиланзар-2, 26, Чиланзарский район, Ташкент 100115, Uzbekistan（+998 90 900 77 30）' + TAG, 'size': '小型' + TAG,
                          'other': '第 122 批：安防系统分销 / 安装（Dahua / Hikvision / Ajax）→ **分销 20% 一页纸一次（预付 100%）**；部分坐实（名录地址 + ООО）' + TAG}}],
    'SB-976': [{'kp_match': 'dauren.boltaev', 'role': '贸易商本人（成交 2 次；WA 已加）= 收件人 — 复购最后一次一页纸：分销 20% B、上次型号复购价 + STC-028GP $28 / STC-2216GP + MOQ 1；俄语备注 ' + UZ + TAG},
               {'facts': {'legal_name': '未取（个体贸易商；0 查：mail.ru + 无公司）', 'founded': '未取' + TAG, 'hq': '未取（乌兹别克斯坦；+998 77 009 91 388）' + TAG, 'size': '个体' + TAG,
                          'other': '第 122 批：★ 成交 2 次、27×0 → **复购最后一次一页纸（预付 100%）；B 保留，回信即升 A 候选**；0 查' + TAG}}],
    # ---------------- EG 3 ----------------
    'SB-629': [{'kp_match': 'ahmed.sonbol', 'role': '联系人（研究档 KP；自站 RFQ 工业 1 光 1 电 PoE）= 收件人 — 一页纸一次：集成商 25% B、STI-154GP（1 SFP + 1 GE + 4 PoE）+ STI-054GP 一口价 + MOQ 1 + 付费样机 ' + EG + TAG},
               {'add_kp': {'name': 'Hamdy Elbadeea', 'role': 'Managing Director（RocketReach 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'C-TECH（埃及系统集成商；商业登记号 1 查未得）', 'founded': '2017' + TAG, 'hq': 'Mohamed Maqrif St. 25, Nasr City, Cairo, Egypt（另 5th Settlement, New Cairo；+20 102 858 0334）' + TAG, 'size': '小型（<25–33）' + TAG,
                          'other': '第 122 批：网络 / 网安 / 数据中心 / ELV 集成 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网地址 + 成立年 + MD）' + TAG}}],
    'SB-971': [{'kp_match': 'ahmed@integrated', 'role': '联系人（研究档 KP）— 不动：询盘视频光端机「4V1D」（不供）+ 证卡打印为主 ' + EG + TAG},
               {'facts': {'legal_name': 'IPS – Integrated Premium Solutions（商业登记号 1 查未得）', 'founded': '未取' + TAG, 'hq': '171 El Banafseg 7, First Settlement, New Cairo, Egypt（+20 2 2307 8803）' + TAG, 'size': '小型' + TAG,
                          'other': '第 122 批：**不动（产品不对位）**；部分坐实（官网地址）' + TAG}}],
    'SB-991': [{'kp_match': 'info@tubal', 'role': 'Board Member（研究档 KP；亲自谈 PoE / EMS 告警口 / SKD 清关）= 收件人 — 一页纸一次：贴标 OEM 30% B、STC-2216GP / STI-288DGGPM $137「2 光 10 电」对位 + SKD（整机拆箱分供，不做定制板）+ 贴标 MOQ + 付费样机 ' + EG + TAG},
               {'add_kp': {'name': 'Fibi Bakhoum Toma', 'role': 'Key Principal（D&B 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Egyptian Aluminium Tubes Company – Tubal Egypt（商业登记号 1 查未得；PoE 为新业务）', 'founded': '未取' + TAG, 'hq': '18 Ashmoun St. / 9 El Zahaby Square, Heliopolis, Cairo 11341, Egypt（+202 2417 6301）' + TAG, 'size': '中型（制造）' + TAG,
                          'other': '第 122 批：铝管制造商（HS 761210 出口）董事会成员谈 PoE 进口 + SKD → **贴标 OEM 30% 一页纸一次（预付 100%）**；部分坐实（D&B 地址 + 负责人 + 出口记录）' + TAG}}],
    # ---------------- 国别待核 3 ----------------
    'SB-1139': [{'kp_match': 'arnoldomohr', 'role': 'Solution Architect（研究档 KP；2026-01-15 真回 CENTEC「great alternative in our market」；2026-03-10 带 C9300L-48P-4X 等价 8 台堆叠需求）= 收件人 — 一页纸 + 补答：STH1G 48×1G PoE+ + 4×10G SFP+ 堆叠 按主表报 + 堆叠带宽 / PoE 预算 / 交期如实 + 付费样机；FOB 深圳；一句话问国别 ' + TAG},
                {'facts': {'legal_name': '未取（0 查：gmail + 无公司；人名 1 查无命中；姓氏 Beltetón 多见危地马拉，待证）', 'founded': '未取' + TAG, 'hq': '未取（国别待核）' + TAG, 'size': '未知' + TAG,
                           'other': '第 122 批：★ 仓内唯一把 CENTEC STH1G 谈到参数层面的客户 → **建议升 A（Simon 定）；先按集成商 25% 一页纸 + 补答**；0 查' + TAG}}],
    'SB-582': [{'kp_match': 'roh@', 'role': '联系人（研究档 KP；主动要 4 口工业 PoE 报价）= 收件人 — 一页纸一次：集成商 25% B、STI-054GP 4 PoE + 1 GE / STI-154GP 一口价 + MOQ 1 + 付费样机；FOB 深圳 或 DAP 欧盟 买方清关；周四 12–14 当地；一句话问国别 ' + TAG},
               {'facts': {'legal_name': 'SmartIntercom（.eu；1 查无命中；国别待核）', 'founded': '未取' + TAG, 'hq': '未取（欧洲，.eu）' + TAG, 'size': '小型（推定）' + TAG,
                          'other': '第 122 批：Akuvox 高端门禁对讲分销商、我方欠一页纸 → **集成商 25% 一页纸一次（预付 100%）**；未坐实' + TAG}}],
    'SB-973': [{'kp_match': 'info@multi-technology', 'role': '未具名（域名现为无关数字市场页）— 不动：查无实体 + 国别未知 ' + TAG},
               {'facts': {'legal_name': 'Multi Technology System（0 查：域名误配 + 国别未知）', 'founded': '未取' + TAG, 'hq': '未取' + TAG, 'size': '未知' + TAG,
                          'other': '第 122 批：**不动（查无实体）**；0 查' + TAG}}],
    # ---------------- PE 2 ----------------
    'SB-031': [{'kp_match': 'clyver.ore', 'role': 'Sales Manager（研究档 KP；WA 已加；2023-11 问 L3 工业）= 收件人 — 一页纸一次：集成商 25% B、STI-288DGGPM $137 / STI-488DGGPM $147 工业 L2 管理 + STC-4424GCPM $165 L2+ + STC-110XGE $65 一口价；工业 L3 不供如实说；西语备注 ' + PE + TAG},
               {'kp_name': 'Joel Ore', 'role': 'CFO（connectamericas 2026-10-29 吻合）' + TAG},
               {'facts': {'legal_name': 'OM TELECOM S.R.L.（RUC 20600792858；Activo / Habido）', 'founded': '2015-11-02' + TAG, 'hq': 'Av. Ramón Castilla 1120 Int. 503A, Santiago de Surco, Lima, Peru（办公 Calle Rocca de Vergallo 263 Of. 101, Magdalena）' + TAG, 'size': '微型（7 人）' + TAG,
                          'other': '第 122 批：工业电信集成（能源自动化 / 矿业 / 油气），RNP 政府供应商，Bureau Veritas → **集成商 25% 一页纸一次（预付 100%）**；坐实（RUC + 状态 + 成立日 + 法定地址）' + TAG}}],
    'SB-051': [{'country_fix': '美国'},
               {'kp_match': 'rob@prestigevsat', 'role': 'Owner（ZoomInfo：Howell Robert = Rob）= 收件人 — 回访一页纸一次：集成商 25% B、STC-110XGE $65 + STC-228GP $33 / STC-2216GP 游艇机房一口价 + MOQ 1；船级 / 海事认证不声称 ' + US + TAG},
               {'add_kp': {'name': 'William Bye', 'role': 'President / Registered Agent / Director & Engineer（Sunbiz + ZoomInfo 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Prestige Satellite Communications Inc.（Florida Profit Corporation；Document No. P16000009000；EIN 81-1222208；ACTIVE）', 'founded': '2016-01-26' + TAG, 'hq': '2873 SW 14th Street, Fort Lauderdale, FL 33312, USA' + TAG, 'size': '微型（1–10）' + TAG,
                          'other': '第 122 批：表内「秘鲁 S.A.C.」误 → country_fix 美国（Sunbiz 登记劳德代尔堡）；★ 老客户（买过 MC + PoE）→ **回访一页纸一次；回信即升 A 候选**；坐实（Sunbiz 文件号 + EIN + 状态 + 地址）' + TAG}}],
    # ---------------- BH 2 ----------------
    'SB-033': [{'kp_match': 'info@marvelitcs', 'role': '联系人（研究档 KP；要 Cisco 同款型号）= 收件人 — 一页纸一次：集成商 25% B、CBS / SG 类对位 → STC-2224GP $86 / STC-4424GCPM $165 / STC-2216GP 一口价 + MOQ 1 + 付费样机；在用品牌不点名 ' + BH + TAG},
               {'facts': {'legal_name': 'Marvel Business Consultants Co. W.L.L.（品牌 Marvel IT Solutions；CR 号 1 查未得）', 'founded': '约 2008（自述 17 年）' + TAG, 'hq': 'Office 0, Building 100, Road 56, Block 203, Muharraq, Bahrain（+973 3988 5090）' + TAG, 'size': '小型（<50 推定）' + TAG,
                          'other': '第 122 批：托管 IT + 安防 + 网络交换 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网法定名 + 地址）' + TAG}}],
    'SB-192': [{'kp_match': 'core.and.clad', 'role': '采购（研究档 KP；2011 买过 2 次收发器）= 收件人 — 回访一页纸一次：分销 20% B、STC-110XGE $65 + STC-028GP $28 / STC-228GP $33 一口价 + MOQ 1 ' + BH + TAG},
               {'facts': {'legal_name': 'Core and Clad（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（巴林）' + TAG, 'size': '小型（推定）' + TAG,
                          'other': '第 122 批：老客户（Intersec 2011）→ **回访一页纸一次（预付 100%）**；0 查' + TAG}}],
    # ---------------- ZW 2 ----------------
    'SB-049': [{'kp_match': 'info@securico', 'role': '表内联系人（研究档 KP；职务待核）= 收件人 — 回访一页纸一次：集成商 25% B、FS 对位 STI-154GP / STI-288DGGPM $137 + STC-2216GP / STC-2224GP $86 一口价 + MOQ 1；光端机不供明说 ' + ZW + TAG},
               {'add_kp': {'name': 'Divine Ndhlukula', 'role': 'Managing Director, DDNS Security Operations (Pvt) Ltd（控股；公开资料 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Multi-Link (Pvt) Ltd = SECURICO 电子安防事业部（控股 DDNS Security Operations (Pvt) Ltd；注册号 1 查未得）', 'founded': '1998（SECURICO）/ 2008 并入' + TAG, 'hq': 'Ebenezer House, 10 Millwood Road, Workington, Harare, Zimbabwe' + TAG, 'size': '大型（集团 4,300+）' + TAG,
                          'other': '第 122 批：津巴布韦第二大电子安防系统商；老客户（2011–2013 光端机 + FS）→ **回访一页纸一次（预付 100%）**；部分坐实（集团公开资料 + 地址）' + TAG}}],
    'SB-116': [{'kp_match': 'pyramidenterprises3', 'role': '联系人（研究档 KP）— 不动：需求 10G 光模块（不供）+ 多次「暂时没需求」 ' + ZW + TAG},
               {'facts': {'legal_name': 'Pyramid Enterprises（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（津巴布韦）' + TAG, 'size': '微型' + TAG,
                          'other': '第 122 批：**不动（产品不对位 + 婉拒）**；0 查' + TAG}}],
    # ---------------- QA 2 ----------------
    'SB-1062': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 info@tamyeezsecurity.com Attn: Procurement Manager — 一页纸一次：集成商 25% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1 + 付费样机；在用品牌不点名 ' + QA + TAG}},
                {'facts': {'legal_name': 'Al-Tamyeez Security Systems Co.（域名 tamyeezsecurity.com，表内 odoo.com 误；CR 号 1 查未得）', 'founded': '2012' + TAG, 'hq': 'Al-Markhiya Complex, Zone 33, P.O. Box 15394, Doha, Qatar（+974 4488 4600；另 Street 370, Bldg 252, Unit 81）' + TAG, 'size': '小型' + TAG,
                           'other': '第 122 批：安防 + 网络 SI（在用 UTEPO 类 PoE）→ **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网地址 + 成立年）' + TAG}}],
    'SB-166': [{'kp_name': 'Mohamed Safeer', 'role': 'Chief Technology Officer（RocketReach 2026-10-29；Crown Group 2012 起；仅 WA）= 收件人 — WA 一页纸 + 规格书：分销 20% B、STI-054GP / STI-280GE $46.6 ×200 阶梯一口价 + 工业 16 / 24 口 STI-0240GE $130 规格书 + 付费样机；Cudy 不点名 ' + QA + TAG},
               {'facts': {'legal_name': 'Crown Security Solutions W.L.L.（Crown Group；地址 / CR 1 查未得）', 'founded': '未取' + TAG, 'hq': '未取（Doha, Qatar）' + TAG, 'size': '小型' + TAG,
                          'other': '第 122 批：★ 200 台工业 5 电口需求 + 2025-02 要工业 16 / 24 口规格书 + 2025-10 CPSE 面谈 → **分销 20% WA 一页纸（预付 100%）；回信即升 A 候选**；部分坐实（KP 职务）' + TAG}}],
    # ---------------- UG 2 ----------------
    'SB-110': [{'kp_match': 'technical@itkati', 'role': '技术 / 采购（研究档 KP；WA 已加；价格 OK、要样、要自有标）= 收件人 — 一页纸一次：贴标 OEM 30% B、STC-028GP $28 / STC-228GP $33 / STC-2216GP 贴标 + 贴标 MOQ + 付费样机；小量先按集成商 25% 中性包装 ' + UG + TAG},
               {'kp_name': 'Sarah Basemera', 'role': 'Company manager（yellow.ug 2026-10-29；无公开邮箱）' + TAG},
               {'facts': {'legal_name': 'iTKATI UG Ltd（ITKati Corp.；URSB 号 1 查未得；登记日 2018-07-25）', 'founded': '2009（登记 2018-07-25）' + TAG, 'hq': 'Block 244, Plot 965, Kyadondo, Makindye, Kampala, Uganda（+256 393 225 713 / +256 704 575 328）' + TAG, 'size': '微型（6–10）' + TAG,
                          'other': '第 122 批：IT / 网络 / 安防集成（企业网络 / CCTV / Starlink / VoIP）→ **贴标 OEM 30% 一页纸一次（小量 25%；预付 100%）**；部分坐实（登记日 + 地址 + 人数）' + TAG}}],
    'SB-183': [{'kp_match': 'onyxtechnologysolutionsltd', 'role': '联系人（研究档 KP；对 154 有兴趣、要价目）= 收件人 — 一页纸一次：集成商 25% B、STI-154GP / STI-054GP 塔站供电 + STC-228GP $33 一口价 + MOQ 1；注入器不供明说 ' + UG + TAG},
               {'facts': {'legal_name': 'Onyx Technology Solutions Ltd（URSB 号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Room S.11, Nathur Building, Victoria Street, Masaka City, Uganda（+256 704 803 724 / +256 200 906 532）' + TAG, 'size': '微型' + TAG,
                          'other': '第 122 批：WISP / ICT / 电气 / 安防（Cambium 用户）→ **集成商 25% 一页纸一次（预付 100%）**；部分坐实（官网地址）' + TAG}}],
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
