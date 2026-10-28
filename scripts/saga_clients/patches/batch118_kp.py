#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 118 批（T29-U111，公司底数第三十六轮 · 阿联酋 B 池收尾 5 户 + 澳大利亚 B 池 18 户 + 巴基斯坦 B 池 17 户 = 40 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 成立 / 总部 / 规模 / 定性 回写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/other_registry_2026-10-27.json（batch=118 行）。
结构同 batch117_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：升 A 候选 ★ 2（SB-1116 Litech Pakistan (Private) Limited 2018 光缆制造商 主动 RFQ 我方欠答 集成商 25% + 补答 / SB-570 CERTECH Pty Ltd ABN 17 149 306 785 50 人分销商 自有品牌 分销 20% 可转贴标 30%）；
一页纸一次 · 集成商 25% 8（SB-251 Pixcom Technologies LLC 标牌全案 要组播交换机 / SB-693 Bin Hilal Holdings 2005 集团采购负责人 5 口 RFQ / SB-931 Wave1 Pty Ltd ABN 74 006 395 026 1985 无线集成 CEO KP 最后一次 / SB-068 ICT Integrators 拉合尔 SI LCCI 会员 CEO 具名 / SB-109 ITE 2004 卡拉奇 SI Director 回信 / SB-1116 ★ / SB-114 Swift Solution & Services 2003 业主 KP 要过价目 / SB-299 AyeZee Group 项目型供应商 WA）；
一页纸一次 · 分销 20% 7（SB-383 Autech Control Group Pty Ltd 自动化分销 Maiwe 在供 产品经理 KP / SB-618 JEA Technologies Pty Ltd 2003 澳新工业分销 ORing 在售 / SB-570 ★ / SB-471 Austec.net Pty Ltd 紧急电话制造 + 分销 ONV 在售 / SB-949 KSM Australia Pty Ltd ABN 98 071 589 690 一人网店 Director 最后一次 / SB-583 Usman 来询即报 RMB 口径待 Simon / SB-869 FUTURIST (PVT) LTD. 2011 进口商 128 票 多次问价）；
一页纸一次 · 贴标 OEM 30% 3（SB-184 Vernetzen Pty Ltd 矿业 OT 自有产品线 需求具体 / SB-504 Eltech Australia Pty Ltd 1995 进口批发 自有 logo 最后一次 / SB-956 PSA Products Pty Ltd ABN 99 076 468 703 多自有品牌安防分销 GM KP 最后一次）；
并线 1（SB-902 Magnus Infotech Dubai = SB-878 Magnus Infotech Trading LLC → SB-878，Gireesh 作备用联系人）；
不动 21（SB-190 A Hamson Cisco 体系 要光模块 / SB-578 Niaar 比价平台 23×0 / SB-755 Fibresales MC 网店 无 KP / SB-523 Aristel ABN 57 095 422 450 HRUI 在供 Q-33 22×0 / SB-844 oeMarket = Bitline System ABN 48 093 949 921 光子学网店 / SB-880 NetSolutionStore Extreme 专营 / SB-948 Krysma 周边 24×0 / SB-624 UBWH = Freenet Warehouse ABN 79 153 180 888 Ubiquiti 专营 / SB-380 Yellowbox ABN 14 634 603 697 要注入器 初创 / SB-604 Burns Precision Ag 升压 微型 / SB-606 HME Solutions 升压 井下 / SB-065 Ayk (Pvt) Ltd 电力守界 + PLANET 经销 / SB-069 Mutex Systems Ltd IT 服务 英国总部 / SB-1101 身份不清 / SB-1108 Sunmars 微型消防 无邮箱 / SB-120 Pronet 200 人 要 5–7 USD 收发器 / SB-204 AAA Group 未坐实 要 ONU / SB-518 个体 2.5G 待口径 / SB-824 SYNCHCOM 进口商 要 USB MC 4×0 / SB-872 个人 E1 / bypass / SB-830 个人 要免费样）；
坐实 9（SB-931 / 570 / 844 / 956 / 949 / 624 / 380 / 824 / 869）/ 部分坐实 24（SB-190 / 251 / 578 / 693 / 755 / 523 / 184 / 383 / 618 / 880 / 471 / 504 / 948 / 604 / 606 / 068 / 065 / 069 / 109 / 1108 / 1116 / 114 / 120 / 299）/ 未坐实 1（SB-204 同名异域）/ 0 查 6（SB-902 并线 / 583 / 1101 / 518 / 872 / 830）。
KP 坐实 = 老板 / 总经理本人 9（SB-931 Wayne Anderson CEO / SB-949 Kevin Director / SB-956 Marcus Ooi GM / SB-068 Muhammad Waleed CEO & Managing Partner（LCCI）/ SB-109 Faisal Javed Director（ZoomInfo）/ SB-114 Abdul Mateen Awan Proprietor / SB-1108 Ghulam Mohiuddin CEO（lookup.pk）/ SB-380 Adrian Brossard Founder / SB-606 Todd Pearce Owner & MD）；职务由公开源坐实 2（SB-693 Mehar Asad = ZoomInfo Head of Procurement Department / SB-824 Muhammad Babar = SYNCHCOM 广告署名）。
法定名补全 / 更正 33；country_fix 0（SB-069 英国总部 + 巴基斯坦办公室，按采购地保持 PK；SB-1108 表内「未填」research 已 PK）。
AU 检索路径实测（首次，18 户 7 个 ABN）：「"<名>" Pty Ltd ABN <域名>」1 查 → 官网 T&C / 页脚 / 质保页 自列 ABN 最常见；creditorwatch.com.au/credit/profile/<ABN> 直出 ABN / ACN / ASIC 注册日 / ABN 生效日 / GST / 实体类型（SB-931 样本）；buy.nsw.gov.au 供应商库 亦出 ABN（SB-380）；名录（processonline / electronicsonline / misterwhat）补地址；RocketReach / ZoomInfo 人数口径不一 → 只记区间。ABN 未得者记「未取」= 部分坐实。
PK 检索路径实测（首次，17 户 0 SECP 号）：SECP eServices / FBR NTN 不可 1 查；可得 = 官网 contact（法定后缀 (Pvt) Ltd / Enterprises）+ 商会名录（LCCI / ICCI）+ 黄页（jamals / lookup.pk / businesslist.pk / businessbook.pk）+ 海关记录（tendata / volza：法定名 + 地址 + 最近进口日）；坐实 仅给「法定名 + 地址 + 进口记录」三合一（SB-824 / 869），其余 部分坐实；个人邮箱 / 无公司名 → 0 查（6 户，PK 池 0 查比例最高）。巴基斯坦一律 预付 100% + FOB 深圳，PTA 不声称。
旁线索（≠ 目标，另立户评估）：BIN HILAL ENTERPRISES L.L.C.（bhe.ae；SB-693 姊妹）；Bitline System Pty Ltd（= SB-844 法人）；Uniqmac Technologies（SB-948 母体）；Freenet Warehouse Pty Ltd / netonix.com.au（SB-624 法人）；Virtual Graffiti Australia Pty Limited（SB-880 母公司）；Litech Sdn Bhd（SB-1116 马来西亚母公司）；OAKTEQ（SB-299 软件子品牌）；aaa-group.com.pk / AAA Group Korangi（SB-204 同名异域，不采信）。
Simon 待决（累计见 PR-02-53 追记）：升 A 候选 SB-1116 / 570（回信即升）；SB-523 Aristel 的 Q-33 口径（HRUI 在供）；SB-583 Usman 的 RMB 报价 / 私账口径；SB-518 的 2.5G 口径（随 SB-263）；SB-1116 技术符合性声明由 Simon 定稿。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 118 批 官方登记核实 2026-10-28）'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜（买方清关）、TDRA / ESMA 不声称'
AU = '— 澳洲常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳、RCM 不声称（DAP 买方清关）'
PK = '— 巴基斯坦常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳、PTA 不声称'
UPD = {
    # ───────── AE 收尾 5 ─────────
    'SB-190': [{'kp_match': 'tahmad@ahamson.com', 'role': '表内联系人（WA +971 55 144 9500 已加；职务未核；2024-04 询 Cisco 光模块）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'A Hamson Middle East FZE（FZE 牌照号 1 查未得；集团 A Hamson Inc. 加拿大 1985）', 'founded': '集团 1985（多伦多）；FZE 未取' + TAG, 'hq': '920 Burjuman Business Towers, Dubai；巴基斯坦 3rd Floor, Al-Baber Centre, F-8 Markaz, Islamabad（+92 51 281 8094）；集团总部多伦多' + TAG, 'size': '中小（51–200 量级；IBM PartnerPlus SI / MSP / VAR）' + TAG,
                          'other': '第 118 批：Cisco 体系网络集成商（迪拜 / 伊斯兰堡 / 多伦多），唯一需求 Cisco GLC-LH-SMD 光模块（Saga 无）→ **不动（B 保留；交换机需求再按集成商 25% 预付）**；部分坐实（官网 contact + IBM 目录）' + TAG}}],
    'SB-251': [{'kp_match': 'khaleel.abckrk@gmail.com', 'role': '表内联系人（gmail；WA +971 50 671 7325 已加；2024-03 回「multicast support switch」）= 收件人（WA 为主）— 一页纸一次：集成商 25% B small、直接答组播 = STC-4424GCPM（L2+ Marvell，IGMP Snooping）$165 / STI-288DGGPM $137、非管理 STC 不做组播控制明说、MOQ 1 + 付费样机 + DAP 迪拜 ' + AE + TAG},
               {'facts': {'legal_name': 'PIXCOM TECHNOLOGIES LLC（牌照号 1 查未得；集团 Pixcom Industries / Prosign Systems）', 'founded': '2003 / 2004（自述）' + TAG, 'hq': 'P.O. Box 252173, Dubai（+971 4 580 6222）；办公室 印度 HQ / 迪拜 / 香港 / 伦敦' + TAG, 'size': '中小（100–200+ 级，自述）' + TAG,
                          'other': '第 118 批：数字标牌 / LED / 互动 kiosk 全案 + 自制（City Walk LED、迪拜智能警局合作方），KP 明确要支持组播的交换机 → **集成商 25% B small，一页纸一次（WA）**；再无回声 → 不动；部分坐实（官网：法定名 + P.O. Box + 电话 + 四地办公室）；gmail KP → 预付 100%' + TAG}}],
    'SB-578': [{'kp_match': 'pouriya@niaar.net', 'role': '负责人（研究档；WA 23 次无回复；2024-01「暂时没需求」）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'Niaar General Trading LLC（牌照号 1 查未得）', 'founded': '2006' + TAG, 'hq': 'Office 109, Al Wasl Building, Sheikh Zayed Road, Dubai（P.O. Box 183583）' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：工业品采购 / 供应平台（矿业 / 能源 / 制造；ABB / Advantech / Schneider / Moxa / SKF …，比价型）+ 明说没需求 + 23×0 → **不动（B 保留）**；部分坐实（yello.ae 名录 + 官网页脚）' + TAG}}],
    'SB-693': [{'kp_match': 'mehar.asad786@gmail.com', 'role': 'Head of Procurement Department（ZoomInfo「Muhammad Asad」职务吻合；gmail；阿里巴巴 RFQ 5 电口）= 收件人 — 一页纸一次：集成商 25% B small、直接答 5 口 = STI-054GP（4 PoE + 1 GE）+ 桌面 STC-028GP $28 + 设施管理量用 STC-2216GP / 2224GP、MOQ 1 + 付费样机 + DAP 迪拜 ' + AE + TAG},
               {'facts': {'legal_name': 'Bin Hilal Holdings（集团；法人 Bin Hilal Group Corporate Management LLC / Bin Hilal Enterprises L.L.C. / BinHilal Trading；牌照号 1 查未得）', 'founded': '2005（集团）' + TAG, 'hq': 'Bin Hilal Holding Head Office, 9th Street, Umm Ramool, Rashidiya, Dubai（+971 521 77 1075）' + TAG, 'size': '中型（201–500，ZoomInfo 口径）' + TAG,
                          'other': '第 118 批：多元集团（安防 / 消防 / 设施管理 / 贸易 / 建筑；Honeywell / Dahua 经销），集团采购部负责人本人发过 RFQ 且从未跟进 → **集成商 25% B small，一页纸一次**；再无回声 → 不动；部分坐实（官网 + ZoomInfo + D&B）；gmail KP → 预付 100%；能源 / 公用板块不主动提' + TAG}}],
    'SB-902': [{'kp_match': 'gireeshk70@gmail.com', 'role': '领英线索（gmail；职务待核）— 并入 SB-878 Magnus Infotech Trading LLC 备用联系人，不另发' + TAG},
               {'facts': {'legal_name': '= SB-878 Magnus Infotech Trading LLC（Magnus Gulf）— 并线', 'hq': '= SB-878：Al Tawhidi Building II – M4, Al Mankhool Rd, Bur Dubai' + TAG,
                          'other': '第 118 批：无域名 + gmail → 0 查；公司名 = SB-878 法定名 → **并线 → SB-878（一页纸发 Saleem Shaikh MD；Gireesh 作备用联系人）**' + TAG}}],
    # ───────── AU 18 ─────────
    'SB-755': {'facts': {'legal_name': 'Fibresales（法人 / ABN 1 查未得）', 'hq': 'Melbourne VIC（03-9761-7925；门牌未取）' + TAG, 'size': '微型' + TAG,
                         'other': '第 118 批：光纤配件 / MC / SFP 网店（自有牌 Yamasaki MC；「质量一般」）→ 产品不对位（Saga 仅 STC-110XGE）+ 无 KP + 从未跟进 → **不动（B 保留）**；部分坐实（社媒 + 电话）' + TAG}},
    'SB-523': [{'kp_match': 'sales@aristel.com.au', 'role': 'Technical Manager（研究档；sales@；22 次跟进无回复）— 不动，不发（Q-33 口径确认后若 Simon 点名再发管理线一页纸）' + TAG},
               {'facts': {'legal_name': 'Aristel Networks Pty Ltd（ABN 57 095 422 450；D&B 行业 电器电子产品批发）', 'founded': '未取（ABN 095 段 ≈ 2000–2001）' + TAG, 'hq': 'Unit 1, 25 Howleys Road, Notting Hill VIC 3168（03 8542 2308 / 1800 00 21 33）' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：电话 / 网络系统分销商（Yeastar Australia 总代、EnGenius、Durafon；自有 AN42N 4 口 PoE = HRUI 在供 → Q-33 口径）+ 22×0 → **不动（B 保留）**；坐实（yeastar.com.au 自列 ABN + 地址 + 电话）' + AU + TAG}}],
    'SB-184': [{'kp_match': 'luke@vernetzen.com.au', 'role': '负责人 / 技术（研究档；WA +61 422 049 988；需求 4 光 8 电 / 4 光 16 电 / 10G + 大功率）= 拍板人 / 收件人 — 一页纸一次：贴标 OEM 30% B、Vernetzen 标 / 中性包装 STI-488DGGPM $147（4 光 8 电）、4 光 16 电 主表无 → STC-4424GCPM 替代明说、10G 上联 + 大功率 = STC-424XGGPM-280W $198（商用级明说）、BT 90 W 不声称、付费样机 + MOQ 1 + 3 年保 ' + AU + TAG},
               {'facts': {'legal_name': 'Vernetzen Pty Ltd（ABN 1 查未得）', 'hq': 'Unit 26, 23 Ashtan Place, Banyo QLD 4014（(07) 4276 6665）；欧洲 Richtistrasse 7, 8304 Wallisellen, Switzerland' + TAG, 'size': '小型（两国办公室）' + TAG,
                          'other': '第 118 批：矿业 OT 网络专家（自有 Wi-Fi over Coax / 光纤 PoE 注入器 / PoE+ 延长器；官网 2026-10 更新），自有产品线 + 需求具体 → **贴标 OEM 30% B，一页纸一次**；回信 → 加厚；部分坐实（官网两国地址 + 电话；ABN 未取）；井下防爆不做不声称' + TAG}}],
    'SB-844': {'facts': {'legal_name': 'Bitline System Pty Ltd（ABN 48 093 949 921；经营 oeMarket.com）', 'founded': '未取（ABN 093 段 ≈ 2000）' + TAG, 'hq': '8 Princes Street, Bexley NSW 2207 / 10 Fishburns Rd, Galston NSW（+61 2 9899 1412）' + TAG, 'size': '微型' + TAG,
                         'other': '第 118 批：光电子 / 光纤产品网店 + 自研设计制造（MC / 收发器 / 激光二极管 / 无源 / 测试仪；全球 30+ 国科研电信客户）→ 产品不对位 + 无 KP → **不动（B 保留）**；坐实（官网 about 自列 ABN + 法人名）' + TAG}},
    'SB-383': [{'kp_match': 'zli@autechcontrol.com.au', 'role': 'Automation Products Manager（研究档；4 次跟进无回复）= 收件人（sales@ 抄送）— 一页纸一次：分销 20% B small、对位其 5 口导轨机的 STI-054GP / STI-154GP + 管理 STI-288DGGPM 一口价、3 年保 + MOQ 1 + 付费样机、串口服务器 / 网关不做明说、英文称呼不走中文直联 ' + AU + TAG},
               {'facts': {'legal_name': 'Autech Control Group Pty Ltd（ABN 1 查未得；名录页所示 22 152 305 336 为 Westwick-Farrow Media ≠）', 'hq': 'Unit 15, 104-106 Ferntree Gully Road, Oakleigh East VIC 3166（+61 3 9544 0733）' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：自动化 / 电气 / 仪表产品分销（Schneider 电表、Horner HMI、Advantech 网关、Maiwe 5 口导轨机在供），产品经理为 KP、只跟过 4 次 → **分销 20% B small，一页纸一次**；再无回声 → 不动；部分坐实（processonline 名录 + 社媒）' + TAG}}],
    'SB-618': [{'kp_match': 'craigk@jeatech.com.au', 'role': 'Manager（研究档；7 次跟进无回复）= 收件人 — 一页纸一次：分销 20% B、对位其在售 10 口工业 PoE 的 STI-288DGGPM $137 / STI-488DGGPM $147 + STI-154GP、宽温 3 年保 + 备库存 MOQ 1 起 + 付费样机、路由 / HMI 不做明说 ' + AU + TAG},
               {'kp_name': 'Tony Ioannidis', 'role': 'Operations Manager（研究档）= 抄送' + TAG},
               {'facts': {'legal_name': 'JEA Technologies Pty Ltd（ABN 1 查未得）', 'founded': '2003' + TAG, 'hq': 'Unit 1, 72 Bayfield Road East, Bayswater North VIC 3153（(03) 8736 0330；旧址 Unit 36, 41-49 Norcal Rd, Nunawading）' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：澳新工业电子外设专业分销（Robustel / Teltonika / Milesight 路由、工业面板 PC、ORing IDGPS-C1042GP 在售；备库存 + 自修）→ **分销 20% B，一页纸一次**；回信 → 加厚；部分坐实（名录 + ithistory：成立年 + 地址）' + TAG}}],
    'SB-931': [{'kp_match': 'wayne@wave1.com.au', 'role': 'CEO（研究档；备用 wayneand4305@icloud.com；22 次跟进无回复；Simon「可以多跟进一下」）= 拍板人 / 收件人 — 一页纸一次（最后一次）：集成商 25% B、基站 / 塔架侧宽温 PoE STI-154GP / STI-288DGGPM（802.3at 给 PoE 电台 / 摄像机供电）+ 机房 STC-4424GCPM 一口价、无源 PoE 电台不兼容明说、3 年保 + MOQ 1 + 付费样机 ' + AU + TAG},
               {'facts': {'legal_name': 'Wave1 Pty Ltd（ABN 74 006 395 026 / ACN 006 395 026；Australian Proprietary Company, Limited by Shares；Active；GST 2000-07-01 起）', 'founded': '1985-04-01（ASIC）；ABN 2000-02-09' + TAG, 'hq': '19 Laser Drive, Rowville VIC 3178（+61 3 9212 7200）' + TAG, 'size': '小型（11–50）' + TAG,
                          'other': '第 118 批：41 年无线 / 微波通信集成商（许可微波、楼宇间无线、塔架 / 拖车、安装），CEO 为 KP → **集成商 25% B，一页纸一次（最后一次）**；22×0 在先 → 再无回声即不动；坐实（creditorwatch：ABN + ACN + 注册日 + 类型 + GST）；微波 / 射频不碰' + TAG}}],
    'SB-880': {'facts': {'legal_name': 'NetSolutionStore.com.au = Virtual Graffiti Australia Pty Limited 分部（ABN 1 查未得；Extreme Networks 授权经销）', 'hq': '未取（澳洲）' + TAG,
                         'other': '第 118 批：单一原厂（Extreme）专营网店 + 无 KP + 7×0 → **不动（B 保留）**；部分坐实（页脚母公司名）' + TAG}},
    'SB-570': [{'kp_match': 'info@certech.com.au', 'role': 'Product & Brands Program Manager（研究档；sophiaw@ / info@）= 收件人（选品拍板）— 一页纸一次：分销 20% B（升 A 候选 ★）、① 对位其 Edimax 工业线的 STI-288DGGPM / STI-488DGGPM / STI-0240GE + 商用 STC-2216GP / 2224GP / 4424GCPM 一口价 ② 或 CERTECH 标 / 中性包装 贴标 30% 二选一、MOQ 1 + 付费样机 + 3 年保 ' + AU + TAG},
               {'kp_match': 'thomasb@certech.com.au', 'role': 'Senior Network Solutions Specialist（研究档）= 抄送' + TAG},
               {'facts': {'legal_name': 'CERTECH Pty Ltd（ABN 17 149 306 785 / ACN 149 306 785）', 'founded': '约 2011（ACN 149 段推定）' + TAG, 'hq': '1/33 Heathcote Road, Moorebank NSW 2170（1300 144 111 / 02 8798 9965；旧址 Unit 2/12 Cunningham St）' + TAG, 'size': '中小（约 50 人，名录口径）' + TAG,
                          'other': '第 118 批：数据 / AV / 安防 / 连接产品分销商 + 自有 CERTECH 品牌布线机柜（20 年布线质保；Edimax 工业交换机在售），品牌项目经理为 KP → **分销 20% B，一页纸一次；升 A 候选 ★**；回信 → 加厚 + 升 A；坐实（官网页脚 + T&C 自列 ABN / ACN）；不点名 Edimax' + TAG}}],
    'SB-471': [{'kp_match': 'sales@austec.net', 'role': '公用销售箱（无具名 KP；11 次跟进无实质回复；Simon「有兴趣」）= 收件人（Attn: Sales Manager）— 一页纸一次：分销 20% B、对位其在售工业 PoE 的 STI-154GP / STI-288DGGPM / STI-488DGGPM 宽温 + 3 年保 + MOQ 1 + 付费样机、给求助电话 / 摄像机供电的 802.3at 口 ' + AU + TAG},
               {'facts': {'legal_name': 'Austec.net Pty Ltd / Austec Communications（ABN 1 查未得）', 'founded': '未取（自述 30+ 年）' + TAG, 'hq': '1025A Pumicestone Road, Toorbul QLD 4510（1300 663 442）' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：偏远 / 恶劣环境通信方案商（自研自产防风雨紧急电话 + 分销 Dahua / Teltonika / Cambium / ONV 工业 PoE；客户 公路 / 铁路 / 矿山 / 电站 / 警消）→ **分销 20% B，一页纸一次**；11×0 在先 → 再无回声即不动；部分坐实（官网 contact：法定名 + 地址）；铁路 / 电站 / 警消项目不主动提，不点名 ONV' + TAG}}],
    'SB-504': [{'kp_match': 'todd.cuneo@eltech.com.au', 'role': 'Product Manager（研究档；21 次跟进无回复）= 收件人 — 一页纸一次（最后一次）：贴标 OEM 30% B、Eltech 标 / 中性包装 STC-028GP / STC-228GP / STC-2216GP + 导轨 STI-054GP / STI-154GP（配电柜场景）、MOQ 1 起贴标试单 + 付费样机 ' + AU + TAG},
               {'kp_name': 'Jolyn Soo', 'role': 'Engineering Manager（研究档；邮箱未取）= 抬头抄送' + TAG},
               {'facts': {'legal_name': 'Eltech Australia Pty Ltd（ABN 1 查未得）', 'founded': '1995（墨尔本）' + TAG, 'hq': '31 Jersey Road, Bayswater VIC 3153（1800 007 458）；墨尔本 / 悉尼 / 布里斯班三仓' + TAG, 'size': '中小（11–78 人，口径不一；$5.7M RocketReach）' + TAG,
                          'other': '第 118 批：独立进口 + 电气配件批发分销（工业电缆 / 箱体 / KIKBLOX 配电 / 面板配件），自有 logo 已上过交换机 → **贴标 OEM 30% B，一页纸一次（最后一次）**；21×0 在先 → 再无回声即不动；部分坐实（企业库 + 名录）' + TAG}}],
    'SB-956': [{'kp_match': 'marcus@psaproducts.com.au', 'role': 'General Manager（研究档；2022 调价函署名 marcus@；21 次跟进无回复；Simon「可以多跟进一下」）= 拍板人 / 收件人 — 一页纸一次（最后一次）：贴标 OEM 30% B、PSA / Panacom 标 PoE STC-028GP $28 / STC-228GP / STC-2216GP / STC-2224GP（摄像机 250 m 延长模式）+ 管理 STC-4424GCPM、MOQ 1 起贴标 + 付费样机 ' + AU + TAG},
               {'kp_match': 'enquiry@psaproducts.com.au', 'role': 'Business Development Manager（研究档）= 抄送' + TAG},
               {'facts': {'legal_name': 'PSA Products Pty Ltd（ABN 99 076 468 703）', 'founded': '未取（ABN 076 段 ≈ 1996–1997）' + TAG, 'hq': 'PSA House, 17 Millicent Street, Burwood VIC 3125（03 9888 9889）' + TAG, 'size': '中小' + TAG,
                          'other': '第 118 批：澳洲安防批发分销商（自有品牌 PSA Centrii / Lifesaver / Panacom / Homeguard + HiLook 代理；电气批发渠道 Rexel），GM 为 KP → **贴标 OEM 30% B，一页纸一次（最后一次）**；21×0 在先 → 再无回声即不动；坐实（三源一致 ABN + 地址）；对位 HiLook 不点名' + TAG}}],
    'SB-948': {'facts': {'legal_name': 'Krysma – Beyond Connectivity = Uniqmac Technologies 的商号（法人 / ABN 1 查未得）', 'hq': 'Unit 6, 26 Rushdale St, Knoxfield VIC 3180（03 8806 8356）' + TAG, 'size': '微型' + TAG,
                         'other': '第 118 批：消费 + 工业连接产品（AOA 周边为主）+ 无 KP + 24×0 → **不动（B 保留）**；部分坐实（官网 contact：商号 + 母体 + 地址）' + TAG}},
    'SB-949': [{'kp_match': 'kevin@ksm.com.au', 'role': 'Director（官网署名「Kevin - Director」；22 次跟进无回复）= 拍板人 / 收件人 — 一页纸一次（最后一次）：分销 20% B small、STI-288DGGPM $137 / STI-488DGGPM $147 / STI-154GP 宽温 + 3 年保 + MOQ 1 + 付费样机、与现供应商同级比价 ' + AU + TAG},
               {'facts': {'legal_name': 'KSM Australia Pty Ltd / KSM Solutions 网店（ABN 98 071 589 690）', 'founded': '未取（ABN 071 段 ≈ 1995–1996）' + TAG, 'hq': 'Suite 18, 12 Tryon Rd, Lindfield NSW 2070（+61 412 921 435 / 02 8003 3372）' + TAG, 'size': '微型（一人公司级）' + TAG,
                          'other': '第 118 批：工业 MC / FS / SFP 网店、已直接进口国内工业机，Director 为 KP → **分销 20% B small，一页纸一次（最后一次）**；22×0 在先 → 再无回声即不动；坐实（官网 T&C 自列 ABN + 地址 + Director）' + TAG}}],
    'SB-624': [{'add_kp': {'name': 'Robert Clark', 'email': '', 'role': '所有人（域名 whois：Freenet Warehouse Pty Ltd）— 不动，不发' + TAG, 'source': 'scamadviser.com/check-website/ubwh.com.au'}},
               {'facts': {'legal_name': 'Freenet Warehouse Pty Ltd（ABN 79 153 180 888；经营 UBWH Australia / netonix.com.au）', 'founded': '未取（ABN 153 段 ≈ 2011）' + TAG, 'hq': '3 Barker Place, Bicton WA 6157（02 8412 8312）' + TAG, 'size': '微型' + TAG,
                          'other': '第 118 批：Ubiquiti 专营进口网店（「lowest possible price」囤货）+ 无 KP + 6×0 → **不动（B 保留）**；坐实（网店自列 ABN + 地址；法人名 whois）' + TAG}}],
    'SB-380': [{'kp_match': 'contact@yellowbox.app', 'role': 'Founder（Crunchbase 创始人；公开手册 +61 426 292 533 / adrian@yellowbox.com.au；阿里巴巴 RFQ 千兆 PoE 注入器）— 不动，不发（kiosk 组网要小 PoE 交换机再按集成商 25% 报 STI-054GP）' + TAG},
               {'facts': {'legal_name': 'Yellowbox Co Pty Ltd（ABN 14 634 603 697；buy.nsw 供应商 SME / NSW-based）', 'founded': '约 2019（ACN 634 段推定）' + TAG, 'hq': 'Kensington SA / NSW（门牌未取）' + TAG, 'size': '微型（1–10；Pre-Seed）' + TAG,
                          'other': '第 118 批：职场 / 公共智能储物柜系统初创（澳 / 欧 / 新 / 北美装机），需求 = PoE 注入器（Saga 无）→ **不动（B 保留）**；坐实（政府供应商库 ABN + 法人名）' + TAG}}],
    'SB-604': [{'kp_match': 'preston@burnsprecisionag.com.au', 'role': '负责人（研究档；阿里巴巴询盘 升压 5 口）— 不动，不发（标准 48 V PoE 需求再按分销 20% 报）' + TAG},
               {'facts': {'legal_name': 'Burns Precision Ag（法人 / ABN 1 查未得；NSW 安防 Master Licence 000104216）', 'founded': '2017-06' + TAG, 'hq': '22 Main Street, Gooloogong NSW 2805（02 6344 8246）' + TAG, 'size': '微型' + TAG,
                          'other': '第 118 批：精准农业硬件经销（Arag / AgLeader / CHCNAV；自产 KestrelEye 农机摄像头；网站有 Network Switches 页），需求 = 升压 PoE（Saga 无）+ 乡镇微型 → **不动（B 保留）**；部分坐实（官网 + agtechfinder）' + TAG}}],
    'SB-606': [{'kp_match': 'info@hmesolutions.com.au', 'role': 'Owner / Founder / Managing Director（prospeo + 领英；阿里巴巴询盘 升压 5 口）— 不动，不发（地面 / 井口侧工业 PoE 需求再按集成商 25% 报）' + TAG},
               {'facts': {'legal_name': 'HME Solutions（法人名 / ABN 1 查未得）', 'hq': 'Perth WA（门牌未取）' + TAG, 'size': '小型（11–20）' + TAG,
                          'other': '第 118 批：矿业重型移动设备车队管理系统制造商（FMS Live™ 露天 / 井下；VDL 车载硬件 + 软件 + 网络），需求 = 车载升压 PoE（Saga 无）+ 井下防爆不做 → **不动（B 保留）**；部分坐实（企业库 + 官网）' + TAG}}],
    # ───────── PK 17 ─────────
    'SB-068': [{'kp_match': 'apac@ict-integrators.com', 'role': 'CEO / Managing Partner（官网 + LCCI 会员名录；公司箱 apac@）= 拍板人 / 收件人（Attn）— 一页纸一次：集成商 25% B、工业栏目对位 STI-288DGGPM $137 / STI-488DGGPM $147 + 企业接入 STC-4424GCPM $165 / STC-2224GP $86 一口价、MOQ 1 + 付费样机 ' + PK + TAG},
               {'kp_name': 'Ihsan Ullah', 'role': 'Director Commercial（官网）= 抄送抬头' + TAG},
               {'facts': {'legal_name': 'ICT Integrators（LCCI 口径 Managing Partner → 合伙企业；SECP / NTN 1 查未得）', 'founded': '约 2007（自述 11+ 年）' + TAG, 'hq': '349-H/3, Johar Town, Lahore（+92 42 3595 1406-7 / 3586 7776）' + TAG, 'size': '小型（22 人 RocketReach；领英 51–200 存疑）' + TAG,
                          'other': '第 118 批：IT / 电信系统集成 + 增值分销（运营商 / 企业 / 工业 / 医疗 / 教育 / 银行；官网 Industrial Grade Networking 栏），CEO 具名 → **集成商 25% B，一页纸一次**；回信 → 加厚；部分坐实（官网 + LCCI 名录）；运营商 / 银行项目不主动提' + TAG}}],
    'SB-065': [{'add_kp': {'name': 'Sajjad Qaiser', 'email': '', 'role': 'Omicron 业务联系人（OMICRON 官网 partner 页）— 不动，不发' + TAG, 'source': 'omicronenergy.com/en/contact/addresses/pakistan/'}},
               {'facts': {'legal_name': 'Ayk (Pvt.) Ltd.（SECP / NTN 1 查未得；OMICRON 巴基斯坦官方 Sales & Service Partner）', 'founded': '1996 创立 / 2006 注册（自述）' + TAG, 'hq': '2nd Floor, U-Block, Trust Plaza, opposite Standard Chartered Bank, Model Town, Gujranwala 52250（+92 55 3822444 / 3255800）；分支 拉合尔 / 伊斯兰堡 / 木尔坦 / 费萨拉巴德' + TAG, 'size': '中小（约 90 人，自述）' + TAG,
                          'other': '第 118 批：电力测试与工程公司（高压测试服务 + Omicron 等测试设备独家分销 + 自制变电站充电器 NTDC 认证；官网 PLANET 工业以太网专区 = 原厂经销）→ 电力守界 + 原厂经销 + 无具名 KP → **不动（B 保留）**；部分坐实（官网 + Omicron 官方 partner 页）' + TAG}}],
    'SB-069': {'facts': {'legal_name': 'Mutex Systems Ltd（英国 Ltd；CH 号 1 查未取；巴基斯坦区域办公室）', 'hq': '英国总部 Ealing Cross, 85 Uxbridge Road, London W5 5BW；巴基斯坦 Suite 716, 7th Floor, Park Avenue, PECHS Block 6, Shahrah-e-Faisal, Karachi（+92 21 3433 1335）；工程中心 卡拉奇 / 拉合尔 / 伊斯兰堡' + TAG, 'size': '小型' + TAG,
                         'other': '第 118 批：软件 / AI / 网络安全 / 云 DevOps 服务 + 自有 POS ERP / CRM 产品（IT 服务 = 非目标行业）+ 无 KP + 无互动 → **不动（B 保留）**；部分坐实（官网两国地址）；国别按采购地保持 PK' + TAG}},
    'SB-583': [{'kp_match': 'usman2c@hotmail.com', 'role': '买家本人（hotmail / gmail；WA +92 331 471 3140 已加；6 次实质回复、一律要 RMB 最低价）— 不另发一页纸：来询即按 USD 一口价 分销 20% 预付 100% FOB 深圳 回；RMB 报价 / 私账口径待 Simon ' + PK + TAG},
               {'facts': {'legal_name': '个人 / 小贸易商（0 查：无公司名 / 域名）', 'size': '个人' + TAG,
                          'other': '第 118 批：互动最多但只压价 + 要人民币价 → **分销 20% B（贸易商）：来询即报，不另发**；0 查' + TAG}}],
    'SB-1101': [{'kp_match': 'powerlogic1965@gmail.com', 'role': '表内联系人（gmail；要目录、想代推；身份不明）— 不动，不发（报出公司名 / 网站再核）' + TAG},
                {'facts': {'legal_name': '0 查（gmail + 无公司名）', 'size': '个人' + TAG,
                           'other': '第 118 批：身份不清 + 想白拿资料代推 → **不动（B 保留）**；0 查' + TAG}}],
    'SB-109': [{'kp_match': 'faisal@ite.net.pk', 'role': 'Director（ZoomInfo；2025-04 回信问 1 GE + 4 FE 路由器）= 拍板人 / 收件人 — 一页纸一次：集成商 25% B、路由器不做明说、接入 STC-4424GCPM $165 / STC-2224GP $86 / STC-228GP $33 一口价、MOQ 1 + 付费样机 ' + PK + TAG},
               {'facts': {'legal_name': 'International Technology Exchanger (ITE)（SECP / NTN 1 查未得）', 'founded': '2004' + TAG, 'hq': 'The Forum, Suite 611, 6th Floor, Clifton, Karachi 75600（021-3459 8598）；另 M1-A Falak Naz Center, Shahrah-e-Faisal + 拉合尔 Johar Town' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：20 年 IT 方案商（Cisco / Juniper / Fortinet / HPE / Dell 伙伴；企业 / 工业 / 政府；三城），Director 本人回信 → **集成商 25% B，一页纸一次**；再无回声 → 不动；部分坐实（官网 + ZoomInfo + FB）；政府项目不主动提' + TAG}}],
    'SB-1108': [{'kp_name': 'Ghulam Mohuied Din', 'role': 'CEO（lookup.pk「Managed By Mr. Ghulam Mohiuddin - CEO」吻合；WA +92 321 275 5707）— 不动，不发（WA 来询按集成商 25% 报摄像机 PoE，预付 100%）' + TAG},
                {'kp_name': 'Asma (Aasma) Nasir', 'role': 'Marketing（研究档；2010 至今）— 不动' + TAG},
                {'facts': {'legal_name': 'SUNMARS Enterprises（独资 / 合伙口径；SECP / NTN 1 查未得；Honeywell 经销）', 'founded': '2006' + TAG, 'hq': 'M-2, Mezzanine Floor, Raza Arcade, Main Shahrah-e-Faisal, PECHS Block 7 & 8, Karachi 75400（+92 321 275 5707 / 021 3454 4758）' + TAG, 'size': '微型（1–10）' + TAG,
                           'other': '第 118 批：消防 / 安防系统集成（FACP / 气体灭火 / PA / CCTV / 门禁 / BMS），微型 + 无邮箱 + 目录已发无下文 → **不动（B 保留）**；部分坐实（名录三源）' + TAG}}],
    'SB-1116': [{'kp_match': 'hassancheema@litech.com.pk', 'role': 'Manager Business Development（S 邮箱签名；+92 310 092 4444 = 官网电话；2024-03-09 主动 RFQ 接入 / 汇聚交换机 + 路由器，我方欠答）= 收件人 — 一页纸 + 补答：集成商 25% B（升 A 候选 ★）、接入 STC-4424GCPM $165（L2+ Marvell）/ 汇聚 10G STH-2C24XF-HSI $1,500（CENTEC）、路由器不做明说、技术符合性按我方实际规格逐条答不套华为型号、MOQ 1 + 付费样机、opener 引其 2024-03-09 RFQ 主题 ' + PK + TAG},
                {'facts': {'legal_name': 'LITECH Pakistan (Private) Limited（D&B 收录；SECP 号 1 查未得；母公司 Litech Sdn Bhd 马来西亚 1999）', 'founded': '2018' + TAG, 'hq': 'Office No. 01, Ground Floor, Layallpur Regency Plaza, 949-Mall Road, New Civil Lines, Faisalabad 38850（+92 41 262 6672）；5.25 英亩光缆制造基地；办公室 伊斯兰堡 / 费萨拉巴德 / 拉合尔 / 卡拉奇' + TAG, 'size': '中小（制造 + 四地办公室）' + TAG,
                           'other': '第 118 批：光缆 / 光纤器材制造 + 分销 + 项目承包（客户 PTCL / Wateen / Zong / Mobilink + Huawei / ZTE 承包商），主动 RFQ + 多项目 + 我方欠答 → **集成商 25% B，一页纸 + 补答；升 A 候选 ★**；回信 → 加厚 + 升 A；部分坐实（官网 + D&B）；技术符合性声明由 Simon 定稿' + TAG}}],
    'SB-114': [{'kp_match': 'mateen@swift.net.pk', 'role': 'Proprietor（ICCI 会员名录 + 领英；2024-05 要商用交换机价目；兴趣 1 光 8 电）= 拍板人 / 收件人 — 一页纸一次：集成商 25% B、STC-228GP $33（8 电 + 2 SFP）/ STI-288DGGPM $137 / STC-2224GP $86 一口价、MOQ 1 + 付费样机、opener 引 2024-05 他要价目 ' + PK + TAG},
               {'facts': {'legal_name': 'Swift Solution & Services（独资；登记号 1 查未得）', 'founded': '2003' + TAG, 'hq': 'Islamabad（门牌未取）' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：电信 / 网络 / 广播方案商（视频会议 / 数据通信 / RFID / IP 电话；客户含政府 / 广播 / 国防 / 教育）→ **集成商 25% B，一页纸一次**；再无回声 → 不动；部分坐实（商会名录 + 领英）；国防 / 政府 / 广播项目按单核不主动提' + TAG}}],
    'SB-120': [{'kp_match': 'ayousfani@pronet-tech.net', 'role': '表内联系人（职务未核；2024-01 要 5–7 USD 商用收发器目标价；「有需求会说」×3）— 不动，不发（企业接入 / 数据中心需求来询按集成商 25% 报）' + TAG},
               {'facts': {'legal_name': 'Pronet (Pvt) Ltd（表内 Pronet Connectivity (Pvt) Ltd.；SECP 号 1 查未得）', 'founded': '1996' + TAG, 'hq': 'Horizon Tower, Plot Commercial 2/6, Block 3, Clifton, Karachi（+92 21 3582 2401-4）；伊斯兰堡 3rd Floor, Redco Plaza, Jinnah Avenue, Blue Area；拉合尔；迪拜采购联络' + TAG, 'size': '中型（约 200 人，自述）' + TAG,
                          'other': '第 118 批：IT 基础设施 / 安全 / 数据中心 / 联络中心集成商（Avaya 巴基斯坦独家 Diamond、Fortinet Expert；金融 / 企业客户），需求 = 低端收发器 + 婉拒式回复 → **不动（B 保留）**；部分坐实（官网）；金融 / 关键基础设施项目不主动提' + TAG}}],
    'SB-204': [{'kp_match': 'nadeem.sd@aaagroup.pk', 'role': '表内联系人（职务未核；WA 已加；2023-04 要 4 口光猫；主动发过新年贺卡）— 不动，不发（交换机需求来询即按集成商 25% 报，预付 100%）' + TAG},
               {'facts': {'legal_name': 'AAA Group（aaagroup.pk；1 查仅得同名异域 aaa-group.com.pk / AAA Group Korangi → 未坐实）', 'size': '未取' + TAG,
                          'other': '第 118 批：需求（ONU）不在 Saga 产品线 + 实体未坐实 → **不动（B 保留；关系在）**；未坐实（同名异域，1 查止）' + TAG}}],
    'SB-299': [{'kp_name': 'Syed', 'role': '表内联系人（WA +92 300 850 5900 已加；无邮箱；职务未核）= 收件人（WA 发链接）— 一页纸一次：集成商 25% B small、STC-228GP $33 / STC-2224GP $86 / STC-4424GCPM $165 + 工业 STI-288DGGPM $137 一口价、MOQ 1 + 付费样机 ' + PK + TAG},
               {'facts': {'legal_name': 'AyeZee Group（合伙企业，自述 1999 创立 / 2009 登记；NTN 1 查未得；子品牌 OAKTEQ）', 'founded': '1999 / 2009（自述）' + TAG, 'hq': '363 Rehman Abad Stop, Main Murree Road, Rawalpindi / Gulberg Greens Expressway Service Road, Islamabad 44000（+92 51 232 6001）' + TAG, 'size': '小型（10 人 RocketReach；领英 51–200 存疑）' + TAG,
                          'other': '第 118 批：电信 + 电源 + IT 设备项目型供应商（PCM / PDH / MC、UPS、管理 / 非管理交换机、Cisco / Huawei 路由、防火墙；sales.dubai@），只有 WA → **集成商 25% B small，一页纸一次（WA）**；再无回声 → 不动；部分坐实（ZoomInfo + 黄页）；不点名 Cisco / Huawei 替代' + TAG}}],
    'SB-518': [{'kp_name': 'Malik Yousaf Mahmood', 'role': '经营者（仅手机；2025-09 对 2.5G「稍后谈」）— 不动，不发（WA 来询即按分销 20% 报；2.5G 随 SB-263 口径）' + TAG},
               {'facts': {'legal_name': '0 查（无域名 / 邮箱；公司名泛称 Info Systems Lahore）', 'hq': 'Lahore（未取）' + TAG, 'size': '个人' + TAG,
                          'other': '第 118 批：个体 + 无邮箱 + 2.5G 等口径 → **不动（B 保留）**；0 查' + TAG}}],
    'SB-824': [{'kp_match': 'bob@synchsoft.com.pk', 'role': '表内联系人（SYNCHCOM 分类广告署名 +92 321 528 0052 吻合；需求 USB 千兆 MC；价格敏感；WA 4 次无实质回复）— 不动，不发（交换机来询按分销 20% 报，预付 100%）' + TAG},
               {'facts': {'legal_name': 'SYNCHCOM (Pvt) Ltd（synchsoft.com.pk / synchcom.com.pk；SECP 号 1 查未得；海关进口记录至 2026-05，HS 8517.69 / 8517.62 / 8534）', 'founded': '2004' + TAG, 'hq': '693 Rehman Baba Road, Sector I-8/4, Islamabad 44000（+92 335 522 5522）；海关地址 House 915, Street 90, I-8/4' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：电信 / 光纤器材贸易 + 进口商（SDH / PMUX / 光 modem / ODF / 无线路由），需求 USB MC（Saga 无）+ 4×0 → **不动（B 保留）**；坐实（businesslist 名录 + KP 广告署名 + tendata 进口记录）' + TAG}}],
    'SB-869': [{'kp_match': 'tajamal@futurist.com.pk', 'role': 'Manager（研究档；多次问 2 光 8 电管理 PoE / 2 光 4 小壳 / mini 工业机价格）= 收件人 — 一页纸一次：分销 20% B、STI-288DGGPM $137 / STI-154GP / STI-054GP mini + 工业电源搭配说明、一口价 + MOQ 1 + 付费样机、光猫不做明说 ' + PK + TAG},
               {'kp_name': 'Aqeel Abbas', 'role': 'CEO（研究档；邮箱未取）= 抄送抬头' + TAG},
               {'facts': {'legal_name': 'FUTURIST (PVT) LTD.（Jamals 黄页 + tendata 海关 2025-09；SECP 号 1 查未得）', 'founded': '2011' + TAG, 'hq': 'House 898, Street 27, I-10/4, Islamabad（051-444 6394）；海关地址 House 524, Ground Floor, Double Road, I-10/4' + TAG, 'size': '小型' + TAG,
                          'other': '第 118 批：网络工程承包 + 通信 / 电测 / 电源 / 安防设备经销 + 进口商（Volza 128 票 / 47 家供应商；2025-09 仍从 11 家中国供应商进口）→ **分销 20% B，一页纸一次**；回信 → 加厚；坐实（黄页 + 海关：法定名 + 地址 + 成立年）' + TAG}}],
    'SB-872': [{'kp_match': 'israr_awan@hotmail.com', 'role': '买家本人（hotmail；WA +92 321 507 5737 已加；需求 E1 modem / bypass / MC 均不在产品线；3 次实质回复）— 不动，不发（WA 来询按分销 20% 报 STI-154GP 替代 MC 场景）' + TAG},
               {'facts': {'legal_name': '个人 / 小买家（0 查）', 'size': '个人' + TAG,
                          'other': '第 118 批：需求全不在 Saga 产品线 + 个人买家 → **不动（B 保留）**；0 查' + TAG}}],
    'SB-830': [{'add_kp': {'name': 'Usman', 'email': '', 'role': '个人联系人（无邮箱 / 公司；2023-11 想免费测样）— 不动，不发' + TAG, 'source': '用户 Clients 表'}},
               {'facts': {'legal_name': '个人（0 查：无邮箱 / 公司名）', 'size': '个人' + TAG,
                          'other': '第 118 批：个人 + 要免费样 + 无邮箱 → **不动（B 保留；付费样机口径不变）**；0 查' + TAG}}],
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
