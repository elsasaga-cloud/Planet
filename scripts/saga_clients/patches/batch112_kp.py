#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 112 批（T29-U105，公司底数第三十轮 · 欧洲其他国家 B 池收尾 17 户 + 加拿大 B 池第 1 轮 23 户 = 40 户：BY 3 / NL 1 / RS 1 / IT 2 / ES 2 / BG 3 / NO 1 / FI 1 / RO 1 / FR 1 / HU 1 + CA 23（其中 6 户查实为美国 → country_fix US））官方登记核实 → 研究档 KP 角色 / 法定名 / 事实 补写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=112 行）。
结构同 batch111_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：B BIG · 加厚一次 7（SB-238 DIGIMAX SRL 00916230246 €61.3M 93 人 Mean Well 意大利首家分销 M2 NEXT HOLDING KP Matteo Tirapelle / SB-758 FOSS FIBER OPTICS AS 936 010 229 NOK 265M discoverIE 100% 贴标配套 30% / SB-825 ООО «Территория Автоматизации» УНП 193074735 Advantech 白俄官方分销 待 BY 路径 / SB-371 Wirewerks 布线制造商 自有标 MC 贴标配套 30% / SB-983 Northern Light Technologies 井下网络 OEM 配套 30%（无本安认证守界）/ SB-284 Provo Ltd. 1958 年全国低压 CCTV 分销 + 自有开发线 / SB-749 E.C.I. Networks Inc. 开放网络集成 CENTEC 敲门砖）+ 加厚一次 1（SB-354 RLH Industries, Inc. Orange CA 贴标 30% country_fix US）；
加厚 small 一次 6（SB-433 RISTER TECNOLOGIA SL B67260901 自有品牌 PRESENTCO 贴标 30% / SB-809 ECONNET S.R.L. 02965231208 VAD / SB-162 Optigo Networks Inc. 自有 Optigo Connect 硬件线 / SB-233 AVYCON Irvine 贴标 30% country_fix US / SB-393 Mapleye Technologies Corp. 联邦号 14357191 贴标 small / SB-766 INNOVATIVE VIDEO TECHNOLOGY, INC. SAM UEI C15VFM1N1VS6 贴标 30% country_fix US）；
一页纸一次 · 有回声再加厚 15（SB-993 Arcobel Embedded Solutions BV = AbiGo4u KvK 17140959 / SB-1132 NAT tech doo 待证 欠答补发 / SB-279 MARLEX CONEXION SL B65398588 / SB-811 eSoft Tmi 1962756-7 PoE 专精一人例外 / SB-821 ООО «Серверы и сети» УНП 193472550 待 BY 路径 / SB-096 Oviss Labs Inc. Fremont 贴标 small country_fix US / SB-613 7546246 Canada Inc. Cozzmic 集成 small / SB-815 Lendoux + 关联品牌 Houper 贴标 small / SB-355 GAO Tek Inc. 贴牌目录平台 退信 低优先 / SB-409 XLR Security Inc. 分销 small（Lysora = 第三方品牌，研究档更正）/ SB-1125 Globall Distribution 分销 small / SB-999 Algo Communication Products Ltd. 配套 small / SB-387 Fatwire Distributors 分销 small / SB-165 YM Inc. 服装零售集团 终端 IT small（研究档类型更正）/ SB-484 Moso Networks Sacramento 贴标配套 small country_fix US）；
不动 11（SB-819 ООО «ДМД системс» УНП 691575989 微型无 KP / SB-989 Julien Desbrosses 个人 0 查 / SB-725 Elektronik LTD 查无实体 / SB-224 Arsenal TV 查无实体 / SB-786 S. Stamenov 个人 0 查 / SB-803 НОВАТЕХ ЕООД ЕИК 175202821 综合电脑网店 / SB-901 Hersnet = Aura Trans Kft. 待证 HDMI KVM 非品类 / SB-395 Mercku Inc. + SB-173 Inaxsys Security Systems Inc. = 现由洪瑞（HRUI）供货 → Q-33 标记不跟 / SB-106 WinWealth Tech Inc. citiCalls 一人网店 country_fix US / SB-291 Technosource Smart Services Inc. 微型住宅安装）；
坐实 19 / 部分坐实 18 / 未坐实 3（SB-786 / SB-725 / SB-224；另 SB-989 个人 0 查）；
KP 坐实 = 老板 / 董事 / 总裁本人 12（SB-238 Matteo Tirapelle / SB-279 Joan Albert Torras Madolell / SB-433 Manu Mari / SB-758 Peter Fric / SB-811 Erno T. / SB-613 Rob Simmons / SB-815 Rasel Haddadi / SB-393 Elmir Mammadov / SB-409 Jaeden Wiens / SB-766 Joe Troiano / SB-284 Elliot Greenberg / SB-749 Wassim Mekkaoui）；
法定名补全 / 更正 30；country_fix 6（SB-354 / SB-096 / SB-233 / SB-766 / SB-484 / SB-106 研究档国别 CA 实为美国；SB-819 / 821 / 825 研究档「保加利亚」实为白俄罗斯但 entities iso 已为 BY，不改）。
旁线索（≠ 目标，另立户评估）：Arcobel Embedded Solutions BV（NL，SB-993 同一法人）；M2 NEXT HOLDING SRL / Gruppo Giovannini（SB-238 母公司）；discoverIE Group plc（SB-758 母公司）；NAT tech doo Belgrade（SB-1132 待证）；Aura Trans Kft.（HU，SB-901 关联）；AZECAM Security Systems（SB-393 姊妹安装公司）；HOUPER（SB-815 关联品牌）；Levitt-Safety（SB-983 母公司）；NoviFlow（SB-749 并入）；ENS Security（美国 Lysora 分销，≠ 目标）。
Simon 待决（累计见 PR-02-53 追记）：升 A 候选 SB-238 / SB-758 / SB-825（BY）/ SB-371 / SB-983 / SB-284 / SB-749 回信即升；BY 户 SB-821 / SB-825 收款 / 物流路径同 RU 议题。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 112 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- 第 1/3 欧洲其他 14 ----------
    'SB-819': {'facts': {'legal_name': 'ООО «ДМД системс»（nabludenie.by；УНП 691575989；Минская обл.）', 'founded': '2013-04-12' + TAG,
                         'other': '第 112 批：白俄微型监控网店（无 KP、0 打开）→ **不动（微型无 KP；B 保留）**；研究档国别「保加利亚」有误，实为白俄罗斯（entities iso 已 BY，不改）' + TAG}},
    'SB-821': {'facts': {'legal_name': 'ООО «Серверы и сети»（server-x.by；自有品牌 Server-X 服务器；УНП 193472550；Минск）', 'founded': '2020-09-28' + TAG,
                         'other': '第 112 批：明斯克服务器组装 / IT 分销（自有品牌服务器）→ **分销 20% small，一页纸一次（STC-2224GP / STC-4424GCPM / STC-110XGE 机房配套；预付款）— 待 Simon 定 BY 收款 / 物流路径后再发**；研究档国别「保加利亚」有误，实为白俄罗斯' + TAG}},
    'SB-825': {'facts': {'legal_name': 'ООО «Территория Автоматизации»（t-automation.by；УНП 193074735；Минск；Advantech 白俄官方分销；自报 >$5M）', 'founded': '2018-05-08' + TAG,
                         'other': '第 112 批：工业自动化 / 工控分销（Advantech 官方分销；自报 >$5M）→ **分销 20% B BIG，加厚一次（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM 工业线第二来源；预付款）— 待 Simon 定 BY 收款 / 物流路径后再发**；升 A 候选；研究档国别「保加利亚」有误，实为白俄罗斯' + TAG}},
    'SB-989': {'facts': {'legal_name': '未具名（Julien Desbrosses 个人；WhatsApp；0 查）', 'founded': '—' + TAG,
                         'other': '第 112 批：个人户（无公司名 / 域名）→ **不动（WA 一口价可选，Simon 定）**' + TAG}},
    'SB-993': {'facts': {'legal_name': 'Arcobel Embedded Solutions BV（网店 AbiGo4u / abigo4u.com；KvK 17140959；BTW NL810271382801；Heesch）', 'founded': '≈2002（KvK 1714…）' + TAG,
                         'other': '第 112 批：Heesch 嵌入式 / 工业计算分销商的网店品牌（同一法人）→ **分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-154GP / STI-288GPM 工业线 + 中性包装）**；旁线索 Arcobel Embedded Solutions BV（同法人，主站另评估）' + TAG}},
    'SB-1132': [{'kp_name': 'Aleksandar Nedić', 'role': 'NAT tech doo（LinkedIn 自述；贝尔格莱德；法人待证）= 收件人 / 拍板人' + TAG},
                {'facts': {'legal_name': 'NAT tech doo（Beograd；仅 LinkedIn 自述，APR 登记未取 → 部分坐实）', 'founded': '未取' + TAG,
                           'other': '第 112 批：塞尔维亚小型网络集成（我方欠答）→ **集成 25% small，一页纸一次（欠答补发：STC-028GP / STC-228GP / STC-2224GP 一口价 + 非欧盟 DAP 买方清关）**' + TAG}}],
    'SB-238': [{'add_kp': {'name': 'Matteo Tirapelle', 'role': '研究档 KP = 收件人 / 拍板人（DIGIMAX SRL；ufficiocamerale）' + TAG, 'email': '', 'source': 'https://www.ufficiocamerale.it/'}},
               {'facts': {'legal_name': 'DIGIMAX SRL（P.IVA / CF 00916230246；REA VI-237542；Vicenza；母公司 M2 NEXT HOLDING SRL / Gruppo Giovannini；Mean Well 意大利首家分销）', 'founded': '1996-05-27' + TAG,
                          'other': '第 112 批：维琴察工业电子 / 电源分销商（2025 营收 €61.28M；93 人）→ **分销 20% B BIG，加厚一次（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM 工业线 + STC-2224GP；Matteo 直呼）**；升 A 候选；旁线索 M2 NEXT HOLDING SRL' + TAG}}],
    'SB-279': [{'add_kp': {'name': 'Joan Albert Torras Madolell', 'role': 'Administrador único / 业主（empresia / iberinform）= 拍板人 / 收件人' + TAG, 'email': '', 'source': 'https://www.empresia.es/'}},
               {'facts': {'legal_name': 'MARLEX CONEXION SL（CIF B65398588；Barcelona；2 人；≈€0.5M）', 'founded': '≈2010' + TAG,
                          'other': '第 112 批：巴塞罗那微型网络分销（2 人）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP / STC-2224GP 一口价 + MOQ 1）**' + TAG}}],
    'SB-433': [{'add_kp': {'name': 'Manu Mari', 'role': 'CCO（rister.com / LinkedIn）= 收件人 / 拍板人' + TAG, 'email': '', 'source': 'https://www.rister.com/'}},
               {'facts': {'legal_name': 'RISTER TECNOLOGIA SL（CIF B67260901；自有品牌 PRESENTCO；10 人）', 'founded': '2018-07-16' + TAG,
                          'other': '第 112 批：巴塞罗那自有品牌（PRESENTCO）AV / 网络方案商 → **贴标 30% small，加厚 small 一次（PRESENTCO 标 PoE STC-028GP / STC-228GP / STC-2224GP + 中性包装 / 自编货号 + 小 MOQ；Manu 直呼）**' + TAG}}],
    'SB-725': {'facts': {'legal_name': '未坐实（名片「Elektronik LTD」Toshko Todorov；保加利亚登记未命中）', 'founded': '未取' + TAG,
                         'other': '第 112 批：1 查即停，查无实体 → **不动（WA 对公司名可选，Simon 定）**' + TAG}},
    'SB-758': [{'kp_name': 'Peter Fric', 'role': '研究档 KP（SK；FOSS FIBER OPTICS AS / discoverIE 集团）= 收件人' + TAG},
               {'facts': {'legal_name': 'FOSS FIBER OPTICS AS（org.nr 936 010 229；Drammen；discoverIE Group plc 100%；FY2026-03 营收 NOK 265.3M；65–73 人）', 'founded': '1984-11-02' + TAG,
                          'other': '第 112 批：挪威光纤 / 工业通信配套制造分销（集团 discoverIE）→ **贴标 / 配套 30% B BIG，加厚一次（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM 工业线贴标 + 中性包装 + 非欧盟 DAP 买方清关；Peter 直呼）**；升 A 候选；旁线索 discoverIE Group plc' + TAG}}],
    'SB-809': {'facts': {'legal_name': 'ECONNET S.R.L.（P.IVA 02965231208；REA BO-0481011；Bologna；Edge-Core 增值分销；2–10 人）', 'founded': '2009-09-15' + TAG,
                         'other': '第 112 批：博洛尼亚网络增值分销（VAD）→ **分销 20% small，加厚 small 一次（STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W / STC-110XGE 作第二价位 + STH 10G / 25G 敲门砖；中性包装）**；稿内不点名 Edge-Core' + TAG}},
    'SB-811': [{'add_kp': {'name': 'Erno T.', 'role': 'Tmi 业主（eSoft Tmi Erno T.；finder.fi）= 拍板人 / 收件人' + TAG, 'email': '', 'source': 'https://www.finder.fi/'}},
               {'facts': {'legal_name': 'eSoft Tmi Erno T.（Y-tunnus 1962756-7；toiminimi；在售 PLANET + HRUI）', 'founded': '2009-10-30' + TAG,
                          'other': '第 112 批：芬兰一人 PoE 专精网店（已售同类 PoE）→ **分销 20% small，一页纸一次（一人网店例外：PoE 专精；STC-028GP / STC-228GP / STC-2224GP 一口价 + MOQ 1）**；稿内不点名 PLANET / HRUI' + TAG}}],
    'SB-224': {'facts': {'legal_name': '未坐实（「Arsenal TV」Gmail；罗马尼亚 SRL 登记未命中）', 'founded': '未取' + TAG,
                         'other': '第 112 批：1 查即停，查无实体 → **不动**' + TAG}},
    # ---------- 第 2/3 欧洲其他 3 + CA 10 ----------
    'SB-786': {'facts': {'legal_name': '未具名（S. Stamenov 个人 Gmail；保加利亚；0 查）', 'founded': '—' + TAG,
                         'other': '第 112 批：个人户、明示无需求 + 19 次无果 → **不动（B 保留）**' + TAG}},
    'SB-803': {'facts': {'legal_name': 'НОВАТЕХ ЕООД（BestPC.BG；ЕИК 175202821；ДДС BG175202821；София 1582 ж.к. Дружба-2 бл. 304）', 'founded': '≈2001（业务）' + TAG,
                         'other': '第 112 批：索非亚电脑综合门店 / 网店（网络仅附带类目、无 KP）→ **不动（综合网店规则；B 保留）**' + TAG}},
    'SB-901': {'facts': {'legal_name': '「Hersnet Ltd」未登记；电话 +36 20 946 6366 与 info@hersnet.hu 挂在 Aura Trans Kft.（Budapest, Rákóczi út 22；2009）名下 → 疑为其商号（待证）', 'founded': '2009（Aura Trans Kft.）' + TAG,
                         'other': '第 112 批：匈牙利天线 / 弱电微型户，需求 HDMI KVM 延长器（非 Saga 品类）+ 20 次无果 → **不动**' + TAG}},
    'SB-354': [{'kp_match': 'ggunning@fiberopticlink.com', 'role': 'RLH Industries 研究档 KP（职务待核）= 抄' + TAG},
               {'kp_name': 'Albert G', 'role': 'Executive Vice President（Albert Gregory；agregory@）= 拍板人（抄）' + TAG},
               {'kp_name': 'Cesar H', 'role': 'Purchasing Agent（Cesar Ordaz；cordaz@）= 收件人' + TAG},
               {'facts': {'legal_name': 'RLH Industries, Inc.（商号 Fiber Optic Link；fiberopticlink.com / rlhfiber.com；936 N. Main Street, Orange, CA 92867, USA；CA SoS 号未取）', 'founded': '1988' + TAG,
                          'other': '第 112 批：研究档国别 CA 有误 → 美国加州（714 区号）→ **country_fix US**；加固型光纤 MC / 工业以太网交换机自有品牌商（定价高、有采购专员）→ **贴标 OEM 30%，B，加厚一次（RLH 标 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM 第二代工源 + 中性包装 / 自编货号 + 3 年保 + FCC / CE；Cesar 直发 + Albert 抄）**；守界：不提政府 / 军用线' + TAG},
                'country_fix': '美国'}],
    'SB-371': [{'kp_match': 'clindquist@wirewerks.com', 'role': 'Wirewerks 研究档 KP（职务待核）= 收件人，一问产品经理' + TAG},
               {'facts': {'legal_name': 'Wirewerks（法定名 / NEQ 未取；19144 Cruickshank Avenue, Baie-d\'Urfé, QC H9X 3P1；1991；估 44 人 / $24.4M）', 'founded': '1991' + TAG,
                          'other': '第 112 批：蒙特利尔结构化布线制造商（自有标 MC 副线、有人转售）→ **贴标 / 配套 30% B BIG，加厚一次（Wirewerks 标 MC / 交换机 STC-028GP / STC-228GP / STC-2224GP / STI-054GP / STI-144GP 作布线系统有源端 + 中性包装 / 自编货号 + 加拿大 DAP；英 / 法文，Carl 直呼）**；升 A 候选' + TAG}}],
    'SB-096': {'facts': {'legal_name': 'Oviss Labs Inc.（商号 OVISS CCTV；46259 Warm Springs Blvd, Fremont, CA 94539, USA；CA SoS 号未取）', 'founded': '2004（业务）' + TAG,
                         'other': '第 112 批：研究档国别 CA 有误 → 美国加州 → **country_fix US**；湾区商用监控托管安装商 / 品牌（11–50 人）→ **贴标 30% small，一页纸一次（OVISS 标 STC-028GP / STC-228GP / STC-2224GP 配托管摄像机系统 + 中性包装 + FCC + 小 MOQ；hello@ 一问采购 / 运营负责人）**' + TAG},
               'country_fix': '美国'},
    'SB-613': [{'kp_name': 'Rob Simmons', 'role': 'Chief Do-er / 创始人 · 业主（contactout / shopbrantford；7546246 Canada Inc.）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Sachinder Singh', 'role': 'Network & VoIP Engineer / Azure 管理员 = 抄' + TAG},
               {'facts': {'legal_name': '7546246 Canada Inc.（商号 Cozzmic / Cozzmic Communications；联邦公司号 7546246；20 Ryan Place, Unit 3, Brantford, ON N3S 7S1；BCT Communication Systems 并入）', 'founded': '2010-05-07（营业 2013-10-01）' + TAG,
                          'other': '第 112 批：布兰特福德 6 人 VoIP + CCTV 集成商（CRTC 登记 ISP 转售）→ **集成 25% small，一页纸一次（STC-028GP / STC-228GP / STC-2224GP 一口价 + MOQ 1 + 加拿大 DAP；Rob 直呼）**' + TAG}}],
    'SB-815': [{'kp_name': 'Rasel Haddadi', 'role': 'CEO（LinkedIn；同时任 HOUPER 区域经理 → Houper 疑为关联自有品牌）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'Lendoux / Lendoux Group（Toronto, ON；法定名 / 登记号未取）', 'founded': '≈2024（LinkedIn 任期）' + TAG,
                          'other': '第 112 批：多伦多目录式 IT / 安防 / 仪表商店 + 关联品牌 Houper → **贴标 30% small，一页纸一次（Houper / Lendoux 标 STI-054GP / STI-144GP / STI-154GP + STC-2224GP 作目录第二价位 + 中性包装 + 加拿大 DAP；Rasel 直呼）**；守界：站内有「military」类目，稿内只谈商用 / 工业' + TAG}}],
    'SB-983': [{'kp_match': 'mnoveloso@nltinc.com', 'role': 'Northern Light Technologies 研究档 KP（职务待核）= 收件人，一问采购 / 产品负责人' + TAG},
               {'kp_match': 'spanton@nltinc.com', 'role': 'Northern Light Technologies 研究档 KP（职务待核）= 抄' + TAG},
               {'facts': {'legal_name': 'Northern Light Technologies（NLT；法定名 / 登记号未取；533 McNicoll Ave., Toronto, ON M2H 2C9；1984 年 Levitt-Safety 事业部起；≈100 人；加 / 澳 / 智利）', 'founded': '1984' + TAG,
                          'other': '第 112 批：矿用矿灯 + 井下数字网络（N-Connex）制造商，反复外购 MC / MC 板 → **OEM 配套 30% B BIG，加厚一次（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM 板级 / 整机 + 3 年保 + 加拿大 DAP；Marlon 直呼 + Spanton 抄）**；升 A 候选；守界：Saga 无本安 / 防爆认证（IS / ATEX / MSHA），稿内只谈非危险区设备、绝不声称矿用认证；旁线索 Levitt-Safety' + TAG}}],
    'SB-162': [{'add_kp': {'name': 'Pook-Ping Yao', 'role': 'CTO / Co-Founder（crunchbase）= 拍板人（邮箱未取；info@ 点名）' + TAG, 'email': '', 'source': 'https://www.crunchbase.com/organization/optigo-networks'}},
               {'facts': {'legal_name': 'Optigo Networks Inc.（#320 – 887 Great Northern Way, Vancouver, BC V5T 4T5；BC 登记号未取；21–50 人；估 $2.4M）', 'founded': '2012' + TAG,
                          'other': '第 112 批：智能楼宇 OT 网络软件 + 自有品牌 Optigo Connect 硬件线 → **贴标 OEM 30%，加厚 small 一次（Optigo Connect 标 STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM + STC-2224GP 第二代工源 + 管理型 L2 + 3 年保 + 加拿大 DAP；info@ 点名 CTO）**' + TAG}}],
    'SB-233': [{'kp_name': 'John L', 'role': 'President（john@avycon.com）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Jorge D', 'role': 'Technical Support Team Manager（Jorge Del Valle；zoominfo）= 抄' + TAG},
               {'facts': {'legal_name': 'AVYCON（法定名待取 Avycon Inc.；16682 Millikan Ave., Irvine, CA 92606, USA；CA SoS 号未取；17–50 人；估 $6.1M）', 'founded': '2012' + TAG,
                          'other': '第 112 批：研究档国别 CA 有误 → 美国加州 → **country_fix US**；北美视频监控品牌（190+ 款含网络产品）→ **贴标 OEM 30%，加厚 small 一次（AVYCON 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM 第二代工源 + 中性包装 / 自编货号 + FCC + 小 MOQ；John 直呼）**；稿内绝不提 NDAA / TAA' + TAG},
                'country_fix': '美国'}],
    'SB-355': [{'kp_match': 'sales@gaotek.com', 'role': 'Network Specialist（研究档 KP Ashish Prakash；sales@gaotek.com 2025-06-26 退信 → 改经 sales@gaorfid.com / 站内表单）' + TAG},
               {'add_kp': {'name': 'Frank Gao', 'role': 'Founder & CEO, Ph.D.（LinkedIn；GAO Tek Inc. 2005–）= 拍板人（邮箱未取）' + TAG, 'email': '', 'source': 'https://gaotek.com/about-us/'}},
               {'facts': {'legal_name': 'GAO Tek Inc.（GAO Group；1885 Clements Rd, Suites 215-218, Pickering, ON L1W 3V4 + 244 Fifth Avenue Suite A31, New York；登记号未取；员工数各源 1–50 ↔ 自报数千）', 'founded': '2005（GAO Tek；集团 1992）' + TAG,
                          'other': '第 112 批：B2B 技术目录供应 / 贴牌平台（自有 logo MC / PoE；sales@ 退信）→ **贴标 30% small，一页纸一次（GAO 标 STC-028GP / STI-054GP 第二代工源 + 中性包装；经 sales@gaorfid.com 或站内表单一问采购）**；平台型低优先' + TAG}}],
    'SB-393': [{'kp_name': 'Elmir Mammadov', 'role': 'Director / Co-Founder（Corporations Canada 14357191；elmir@；姊妹公司 AZECAM Security Systems Founder/CEO）= 拍板人 / 收件人' + TAG},
               {'add_kp': {'name': 'Aytan Mammadova', 'role': 'Director（Corporations Canada）' + TAG, 'email': '', 'source': 'https://www.canadacompanyregistry.com/companies/mapleye-technologies-corp/'}},
               {'facts': {'legal_name': 'Mapleye Technologies Corp.（联邦公司号 14357191；BN 704129105RC0001；CBCA 2022-09-09；16-207 Edgeley Boulevard, Vaughan, ON L4K 4B5；Active）', 'founded': '2022-09-09' + TAG,
                          'other': '第 112 批：多伦多自有品牌安防（Mapleye 摄像机 / NVR / PoE 套装，Amazon.ca 在售）+ 姊妹安装公司 → **贴标 30% small，加厚 small 一次（Mapleye 标 STC-028GP / STC-228GP / STC-2224GP 配 4K 套装 + 中性包装 / 自编货号 + 小 MOQ + 加拿大 DAP；Elmir 直呼）**；稿内不点名 HiSource；旁线索 AZECAM Security Systems' + TAG}}],
    # ---------- 第 3/3 CA 13 ----------
    'SB-395': [{'kp_name': 'Ge Shi', 'role': 'CEO（LinkedIn；研究档 Co-Founder；此前 CFO / COO）— Q-33 不跟' + TAG},
               {'facts': {'legal_name': 'Mercku Inc.（51 Breithaupt St, Kitchener, ON N2H；2017-09 创立于 Waterloo：Prof. Yihong Qi / Dr. Fred Yu / Alex Qi；登记号未取；≈50 人）', 'founded': '2017-09' + TAG,
                          'other': '第 112 批：Mesh Wi-Fi / CPE 品牌商；**PoE 现由洪瑞（HRUI）供货 → Q-33「不碰，标记」→ 不动（B 保留；不发信、不报价）**' + TAG}}],
    'SB-409': [{'kp_name': 'Jaeden Wiens', 'role': 'Founder / 业主（xlrsecurity.com legalName XLR Security Inc.；BBB）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'XLR Security Inc.（Unit 15 – 1 High Meadow Pl, Toronto, ON M9L 0A3；登记号未取；2–10 人）', 'founded': '2022' + TAG,
                          'other': '第 112 批：新创 CCTV 增值分销（Uniview 授权）；**研究档「自有云管理交换机品牌 Lysora」有误 — Lysora 为第三方品牌（美国由 ENS Security 分销），XLR 仅授权分销** → **分销 20% small，一页纸一次（非云管理 PoE STC-028GP / STC-228GP / STC-2224GP 作经销商第二价位 + MOQ 1 + 加拿大 DAP；Jaeden 直呼）**；稿内不点名 Uniview / Lysora' + TAG}}],
    'SB-766': [{'kp_name': 'Joe Troiano', 'role': 'President（SAM / GSA 联系人；joe.troiano@）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Matt Troiano', 'role': 'Director of Sales = 抄' + TAG},
               {'facts': {'legal_name': 'INNOVATIVE VIDEO TECHNOLOGY, INC.（dba InVid Tech；SAM UEI C15VFM1N1VS6 / CAGE 8N8G4；355 Oser Avenue, Hauppauge, NY 11788, USA；GSA 47QTCA25D004R；NY DOS 号未取）', 'founded': '2016' + TAG,
                          'other': '第 112 批：研究档国别 CA 有误 → 美国纽约州 → **country_fix US**；北美安防品牌（商用 PoE 现由深圳同行供货）→ **贴标 OEM 30%，加厚 small 一次（InVid 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM 第二代工源 + 中性包装 / 自编货号 + FCC + 小 MOQ；Joe 直呼）**；守界：持 GSA 合同，稿内绝不提政府 / NDAA / TAA / GSA；不点名 Centro' + TAG},
                'country_fix': '美国'}],
    'SB-1125': [{'kp_name': 'Corinne Defay', 'role': 'Marketing Manager（研究档 KP，无邮箱）；收件 info@globall.ca 一问业主' + TAG},
                {'facts': {'legal_name': 'Globall Distribution（法定名 / NEQ 未取；仓库 4185 rue Marcel Lacasse, Boisbriand, QC J7H 1N4；旧址 773 Boul. Industriel, Blainville；Self-Owned；2–10 人）', 'founded': '2011' + TAG,
                           'other': '第 112 批：微型进口分销（PLANET 加拿大分销 + 站内「Globall」自有系列）→ **分销 20% small，一页纸一次（Globall 标或中性 STC-028GP / STC-228GP / STC-2224GP + STI-054GP 作目录第二价位 + 小 MOQ + 加拿大 DAP；法 / 英双语，info@ 一问业主）**；稿内不点名 PLANET' + TAG}}],
    'SB-999': [{'add_kp': {'name': 'Ryan Zoehner', 'role': 'CEO（indeed / theorg）= 拍板人（邮箱未取；info@ 点名产品 / 渠道负责人）' + TAG, 'email': '', 'source': 'https://ca.linkedin.com/company/algo-communication-products-ltd'}},
               {'facts': {'legal_name': 'Algo Communication Products Ltd.（4500 Beedie Street, Burnaby, BC V5J 5L2；SAM UEI ZXSBJM33KYN5 / CAGE 3AC08；BC 号未取；≈95 人；估 $27.2M）', 'founded': '1968-12-01' + TAG,
                          'other': '第 112 批：IP 寻呼 / 告警终端制造商（交换机非其品类、部署全靠 PoE）→ **配套 30% small，一页纸一次（Algo 标或中性 PoE / PoE+ STC-028GP / STC-228GP / STC-2224GP 作寻呼套件配套 SKU + 中性包装）**；稿内不提 K-12 / 政府' + TAG}}],
    'SB-173': [{'kp_name': 'Mark McRae', 'role': 'President（inaxsys.com 2024 新闻；ex-Paradox / ADT）— Q-33 不跟' + TAG},
               {'facts': {'legal_name': 'Inaxsys Security Systems Inc.（11685 Avenue Philippe-Panneton, Montréal, QC H1E 4M1；NEQ 未取；22–24 人；Ajax 加拿大首家官方分销 2022）', 'founded': '2004' + TAG,
                          'other': '第 112 批：蒙特利尔安防品牌 / 分销；**交换机现由洪瑞（HRUI）代工贴标 → Q-33「不碰，标记」→ 不动（B 保留；不发信、不报价）**' + TAG}}],
    'SB-387': [{'kp_name': 'Ray', 'role': 'Managing Director（Ray Haugland；zoominfo；ray.h@）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Michael Pothier', 'role': 'Inside Sales Specialist（2019–）= 抄' + TAG},
               {'facts': {'legal_name': 'Fatwire Distributors / Fat Wire Distribution（法定名 / 阿省登记号未取；9325 63 Avenue NW, Edmonton, AB T6E 0G2；3–11 人；估 $5.1M）', 'founded': '2010' + TAG,
                          'other': '第 112 批：埃德蒙顿经销商型低压 / 信号分配分销（PoE 卖中系）→ **分销 20% small，一页纸一次（STC-028GP / STC-228GP / STC-2224GP 作第二价位 + MOQ 1 + 加拿大 DAP；Ray 直呼 + Mike 抄）**；稿内不点名 Wi-Tek' + TAG}}],
    'SB-165': [{'kp_name': 'Mario Elia', 'role': 'Director, Network Infrastructure（YM Inc.；2025–；终端 IT 采购）= 收件人' + TAG},
               {'facts': {'legal_name': 'YM Inc.（服装零售集团 Urban Planet / Stitches / Bluenotes 等；50 Dufflaw Road, Toronto, ON M6A 2W1；销售实体 YM INC. (SALES) 联邦公司号 8228426 / BN 105261705RC0005；CEO Eric Grundy；1,300+ 人）', 'founded': '2012-10-28（销售实体）' + TAG,
                          'other': '第 112 批：**研究档类型「网络 / 安防贸易商」有误 → 零售连锁终端 IT**（≈700 店门店网络）→ **终端 25% small，一页纸一次（门店摄像机 / AP / POS 用 STC-028GP / STC-228GP / STC-2224GP 一口价 + 1 年保 + 付费样机；Mario 直呼；PoE 延长器非我方品类明说不做）**' + TAG}}],
    'SB-484': [{'kp_name': 'Stephen Leotis', 'role': 'President & CEO / Co-Founder（prnewswire 2025-02；ex-Sercomm / ARRIS）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'Moso Networks（原 MosoLabs；法定名待取 MosoLabs Inc.；2108 N St #9184, Sacramento, CA 95816, USA；CA SoS 号未取）', 'founded': '未取（2025-02 更名）' + TAG,
                          'other': '第 112 批：研究档国别 CA 有误 → 美国加州 → **country_fix US**；私有 5G / CBRS 小基站设备商（自有品牌、全靠 PoE 供电）→ **贴标 / 配套 30% small，一页纸一次（Moso 标或中性 PoE+ / PoE++ STC-228GP / STC-2224GP / STI-288GPM 配套供电 + FCC + 中性包装；Stephen 直呼）**；稿内绝不提 TAA / 政府 / 运营商名' + TAG},
                'country_fix': '美国'}],
    'SB-106': {'facts': {'legal_name': 'WinWealth Tech Inc.（商号 citiCalls；170 W Pomona Ave, Monrovia, CA 91016, USA；CA SoS 号未取；2003-05 起；eBay 卖家 2006 起；估 $2.4M / 0 员工）', 'founded': '2003-05（业务）' + TAG,
                         'other': '第 112 批：研究档国别 CA 有误 → 美国加州 → **country_fix US**；一人 VoIP 网店（无 KP、0 打开）→ **不动（一人网店规则；B 保留）**' + TAG},
               'country_fix': '美国'},
    'SB-291': {'facts': {'legal_name': 'Technosource Smart Services Inc.（3000 Danforth Avenue, Unit #4, Toronto, ON M4C 1M7；安省登记号未取）', 'founded': '2016' + TAG,
                         'other': '第 112 批：士嘉堡微型住宅 / 小商业 CCTV 安装 + 零售套装（无 KP、0 打开）→ **不动（微型无 KP；B 保留）**' + TAG}},
    'SB-284': [{'kp_name': 'Elliot Greenberg', 'role': 'Vice President of Operations（rocketreach；Greenberg 家族；elliot@）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Sy Greenberg', 'role': 'Procurement and Operations / Digital Marketing（LinkedIn Sy Greenberg, MBA）= 抄' + TAG},
               {'facts': {'legal_name': 'Provo Ltd. / Provo Ltée（620 Rowntree Dairy Rd., Woodbridge, ON L4L 5T8 + 401 rue Locke, St-Laurent, QC H4T 1X7；登记号未取；Key Principal Haskell Greenberg；≈44 人；估 $14.8M）', 'founded': '1958' + TAG,
                          'other': '第 112 批：加拿大最大低压线缆 / CCTV / AV 配件分销之一（自有开发产品线 + 代理线）→ **分销 20% + 贴标 30% 两线，B BIG，加厚一次（Provo 标或中性 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI-054GP / STI-144GP + 两仓 DAP；英 / 法文，Elliot 直呼 + Sy 抄）**；升 A 候选；稿内不点名 PLANET / BDCOM / Provision-ISR' + TAG}}],
    'SB-749': [{'kp_name': 'Wassim Mekkaoui', 'role': 'President / CEO（2015–；LinkedIn / businesswire）= 拍板人 / 收件人' + TAG},
               {'kp_name': 'Hassan Khanafer', 'role': 'CTO（theorg）= 技术抄' + TAG},
               {'facts': {'legal_name': 'E.C.I. Networks Inc.（ECI Networks；1405 Trans Canada Route, Dorval, QC H9P 2V9（总部 Rigaud, QC）；NEQ 未取；18 人；2024-10 收购 NoviFlow）', 'founded': '1998' + TAG,
                          'other': '第 112 批：蒙特利尔开放网络 / 数据中心系统集成 + 分销（SONiC 白盒、光模块、TAP、时钟；120 站点边缘案例）→ **集成 / 分销 20–25% B BIG，加厚一次，CENTEC 敲门砖（STH-2C24XF-HSI / STH-8C48DX-HSI / STH-32C-HSI 作边缘 / 汇聚固定配置 L3 第二来源 + STI 副线；Wassim 直呼 + Hassan 抄，一问是否愿评估付费样机）**；升 A 候选；守界：稿内不声称 SONiC / ONIE 兼容（未验证），不点名 Utepo；旁线索 NoviFlow' + TAG}}],
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
