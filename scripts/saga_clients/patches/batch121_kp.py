#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 121 批（T29-U114，公司底数第三十九轮 · 巴西池余 4 + 以色列 B 池 8 + 肯尼亚 B 池 5 + 日本 B 池 5 + 哈萨克斯坦 B 池 4 + 赞比亚 B 池 4 + 香港 B 池 4 + 黎巴嫩 B 池 4 + 墨西哥 B 池 4 = 42 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 成立 / 总部 / 规模 / 定性 回写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/other_registry_2026-10-27.json（batch=121 行）。
本批定性：升 A 候选 2 ★（SB-1120 Obmac 2024-01 已成单 $9,350、创始人 CEO 为 KP → 回信即升；SB-927 RARMX 阿里 RTS 已成单 + 2025 真实进口记录 → 回信即升）；
一页纸一次 · 集成商 25% 14（SB-798 Getec CNPJ 11.641.497 / SB-900 Eleandro WA / SB-378 Pal Wintec 贴标选项 / SB-337 Kimberley / SB-586 Matrix 付费样机 / SB-897 Peter Weru / SB-705 Eware 最后一次 / SB-717 SkyWare 最后一次 / SB-202 EGC 30 台环网 最后一次 / SB-703 Engitel RFQ / SB-892 Telcofusion 10G MC ×4 最后一次 / SB-222 赞比亚 WA / SB-1120 ★ 复购 / SB-927 ★ 复购）；
一页纸一次 · 分销 20% 9（SB-695 LRI CNPJ 94.574.647 / SB-704 Ethical 512146788 / SB-037 Pulsar БИН 100740012554 / SB-622 Avantazh БИН 221040045999 最后一次 / SB-102 Denso / SB-1027 Everbest CR 334414 / SB-327 Techno Tower / SB-324 MTCO 双轨 ↔ 贴标 30% / SB-157 Data Controls 双轨 ↔ 贴标 30%）；
一页纸一次 · 贴标 OEM 30% 9（SB-328 Advice 511393159 双轨 ↔ 分销 / SB-915 RADWIN 配件贴标 / SB-934 Alibi 自有品牌 / SB-1076 Simplifi 双轨 ↔ 分销 / SB-158 Diatrend 5120001026515 / SB-161 Mahanet 7390001009301 最后一次 / SB-164 UNEAX 6021001077094 新壳预付 / SB-822 Solid 双轨 ↔ 分销 / SB-219 Siera 最后一次）；
不动 10（SB-990 Precision DWDM 不对位 / SB-148 ISR 车载 E-mark / SB-228 Negoh-Op 光模块 / SB-911 itmarket 16×0 无 KP / SB-799 Vertex Invader 查无对口 / SB-941 CompTek 分离器 / SB-296 BHS 广播 HDMI / SB-960 Steren Q-33 待口径 / SB-896 Musine PoE MC / SB-865 Bulaya Cisco 兼容）。
坐实 12（SB-695 / 798 / 990 / 328 / 704 / 158 / 161 / 164 / 037 / 622 / 799 / 1027）/ 部分坐实 20（SB-148 / 228 / 378 / 915 / 934 / 1076 / 157 / 822 / 941 / 102 / 1120 / 219 / 705 / 717 / 202 / 296 / 324 / 327 / 927 / 960）/ 未坐实 4（SB-911 / 586 / 703 / 892）/ 0 查 6（SB-900 / 337 / 896 / 897 / 222 / 865）。
KP 坐实 = 老板 / 总经理 / 法人本人 7（SB-695 Leandro Roisenberg 个体业主 / SB-158 宮下清哉 代表取締役 / SB-915 Sharon Sher CEO / SB-1120 Pythias Kachepa 创始人 CEO / SB-202 Mohammad Hammoud 创始人 GM / SB-324 Adnan Melhem 所有者 MD / SB-327 Abou Jaoudeh 家族 GM）；新增 KP 9（SB-378 Ophir Reuveni / SB-704 Ran Broudo / SB-934 Brian Wood CEO / SB-161 Akira Ohe CEO / SB-822 徳岡達人 代表取締役 / SB-037 Sabit Karimov Director / SB-799 Alina Nurpeisova / SB-324 Jad Melhem / SB-327 Fadi Abou Jaoudeh）。
法定名补全 / 更正 36；**country_fix 2（SB-934 Alibi → 美国：实体 Observint Technologies 奥斯汀，表内以色列误；SB-296 BHS Media → 阿联酋：总部 Dubai Media City，表内黎巴嫩 = KP 电话归属）**。
IL 路径实测（首次，8 户 2 个公司号）：kycisrael.com/companies/<公司号>（含成立日 / 状态 / 年报年份，SB-704）；new-techguide 供应商页「Company ID」（SB-328）；D&B / tradeindia / inter-fair / Google Play 开发者信息补地址与成立年；ica.justice.gov.il 不可 1 查。
KE 路径实测（首次，5 户 0 个注册号）：BRS 不可 1 查；hotfrog.co.ke / africa2trust / RocketReach 补地址 + 成立年 + 人数（SB-1076）；同名极多（Matrix Systems）→ 未坐实；gmail 3 户 0 查。
JP 路径实测（续，5 户 3 个法人番号）：houjin.jp / gBizINFO / helloboss / alarmbox 1 查即得法人番号 + 設立 + 本店 + 代表（SB-158 / 161 / 164）；会社案内 PDF / PR 稿补地址与代表者（SB-157 / 822）。
KZ 路径实测（首次，4 户 3 个 БИН）：statsnet.co / adata.kz / kyc.kz / niac.kz / wikicity.kz / ba.prg.kz 1 查即得 БИН + 注册日 + 负责人 + ОКЭД + 规模；官网 реквизиты 自列 БИН（SB-622）；名录无 БИН 的 1 户部分坐实（SB-941）。
ZM 路径实测（首次，4 户 0 个注册号）：PACRA 不可 1 查；官网 + 领英 + datanyze 补成立日 / CEO / 人数（SB-102 / 1120）；无身份 WA + hotmail 2 户 0 查。
HK 路径实测（续，4 户 1 个 CR 号）：inriskable 镜像给 CR + BR 号（SB-1027）；官网 contact + 领英 + tradeeasy 补地址（SB-219 / 705 / 717）。
LB 路径实测（首次，4 户 0 个登记号）：lb.kompass.com 给所有者姓名 + 成立年 + 地址（SB-324 / 327）；crunchbase + RocketReach 补创始人 / 成立年（SB-202）；官网地址核出迪拜实体 → country_fix（SB-296）。
MX 路径实测（续，4 户 0 个 RFC）：D&B / verif / volza（SB-960）；tendata 进口记录证法人形式 + 真实进口（SB-927）；域名 1 查无命中 2 户 → 未坐实（SB-703 / 892）。
Simon 待决：SB-934 以色列 → 美国 / SB-296 黎巴嫩 → 阿联酋 更正；SB-1120 / SB-927 回信即升 A；SB-960 Steren 并入 Q-33 口径（HRUI 在供）；SB-222 WA 问一句公司名。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 121 批 官方登记核实 2026-10-29）'
BR = '— 巴西常规：英文稿（可附葡语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（进口税自理）、Anatel 不声称'
IL = '— 以色列常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP（买方清关）、SII 不声称'
KE = '— 肯尼亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 内罗毕、KEBS 不声称'
JP = '— 日本常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP、技適 / PSE 不声称'
KZ = '— 哈萨克斯坦常规：英文稿、20 / 25 / 30 + T/T 预付 100%（哈国银行）+ FOB 深圳 或 DAP 阿拉木图 / 阿斯塔纳、EAC 不声称'
ZM = '— 赞比亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 卢萨卡、ZABS 不声称'
HK = '— 香港常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 香港（免税）'
LB = '— 黎巴嫩常规：英文稿、20 / 25 / 30 + T/T 预付 100%（不接受信用证）+ FOB 深圳 或 DAP 贝鲁特'
MX = '— 墨西哥常规：英文稿（可附西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP、NOM / IFT 不声称'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜、TDRA 不声称'
US = '— 美国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP（买方清关）、NDAA / TAA / UL 不声称；周三 08–10 当地'
UPD = {
    # ---------------- BR 池余 4 ----------------
    'SB-695': [{'kp_match': 'leandro@', 'role': 'Director / 业主（个体企业 Leandro Roisenberg FI 法人本人；官网 contato 2026-10-29）= 收件人 — 一页纸一次：分销 20% B、工业线中性包装一口价（STI-154GP / STI-288DGGPM $137 / STI-280GE $46.6）+ MOQ 1 + 付费样机；在售进口品牌不点名 ' + BR + TAG},
               {'facts': {'legal_name': 'Leandro Roisenberg Firma Individual（商号 LRI Automação Industrial / LRI Store；CNPJ 94.574.647/0005-02）', 'founded': '未取（INPI 商标 910048894）' + TAG, 'hq': 'Rua Maria Lopes Borba 474, Navegantes - SC 88370-340, Brazil（表内 +55 11 / +972 为业主个人电话）' + TAG, 'size': '微型（个体企业）' + TAG,
                          'other': '第 121 批：同行工业交换机分销（有巴西库存开 NF-e）→ **分销 20% 一页纸一次（预付 100%）**；坐实（官网自列 CNPJ + 地址）' + TAG}}],
    'SB-798': [{'kp_match': 'leonardo@', 'role': '技术负责人（研究档 KP）= 收件人 — 一页纸一次：集成商 25% B、监控项目 PoE（STC-028GP $28 / STC-228GP $33 / STC-2216GP）一口价 + 付费样机；2019 欠税公示 → 预付 100% 不让步 ' + BR + TAG},
               {'facts': {'legal_name': 'GETECSEG Segurança Eletrônica Ltda ME（CNPJ 11.641.497/0001-43）', 'founded': '未取' + TAG, 'hq': 'Rua João Pessoa 1839, Velha, Blumenau - SC 89036, Brazil（+55 47）' + TAG, 'size': '微型（ME）' + TAG,
                          'other': '第 121 批：圣卡塔琳娜州法院公报 2019-04-01 税务名单给出 CNPJ + 地址（欠税 R$4,924.98 红旗）；同名 Gettec 巴西利亚 ≠ 本户 → **集成商 25% 一页纸一次（预付 100%）**；坐实' + TAG}}],
    'SB-900': [{'kp_name': 'Eleandro', 'role': 'WA 联系人（无邮箱 / 公司；研究档）— WA 一页纸一次：集成商 25% B、STC-028GP $28 / STC-228GP $33 + STC-110XGE $65 一口价；千兆 MC 不供明说；葡语备注 ' + BR + TAG},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 公司名）', 'founded': '未取' + TAG, 'hq': '未取（RS，+55 54）' + TAG, 'size': '个人' + TAG,
                          'other': '第 121 批：曾主动问 MC + 商用 PoE 价 → **WA 一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-990': [{'kp_match': 'eduardo.ken', 'role': 'Director（研究档 KP）— 不动：需求 DWDM / DCI / 1.6T 高端（不供）+ 光纤测试仪表分销商（EXFO / Fujikura）' + BR + TAG},
               {'facts': {'legal_name': 'Precision Solutions（CNPJ 05.573.595/0001-98；I.E. 149.927.916.115）', 'founded': '未取（自述 20+ 年）' + TAG, 'hq': 'Avenida Nova Independência 87, conj. 32, Brooklin Paulista, São Paulo - SP 04570-000, Brazil（+55 11 5103-3260）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：支持站页脚自列 CNPJ + 地址；同名 Precision Solutions Informática 10.730.077 ≠ 本户 → **不动（B 保留；来询按分销 20% 报 STH / STC-110XGE）**；坐实' + TAG}}],
    # ---------------- IL 池 8 ----------------
    'SB-148': [{'kp_match': 'novick@', 'role': '联系人（研究档 KP）— 不动：需求工业 8 电口 E-mark 车载认证（不供）+ 5×0 ' + IL + TAG},
               {'facts': {'legal_name': 'I.S.R. Technologies (Israel) Ltd（ISR Tech；公司号 1 查未得）', 'founded': '1986' + TAG, 'hq': '5 Eliav Yaacov St., P.O. Box 34556, Jerusalem 9546205, Israel（02-6520570）' + TAG, 'size': '微型（1–10，Crunchbase）' + TAG,
                          'other': '第 121 批：智慧出行 / 车队 ITS 方案商（以色列 + 印度）→ **不动（产品不对位：车载认证）**；部分坐实（官网 + Google Play 开发者地址）' + TAG}}],
    'SB-228': [{'kp_match': 'dov@', 'role': 'CEO（研究档 KP）— 不动：需求 10G 光模块（不供）+ RF 光子学测试测量非目标行业 ' + IL + TAG},
               {'facts': {'legal_name': 'Negoh-Op Ltd（公司号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Shabazi St. 10, Yahud 5623028, Israel（+972 3 528 5972）' + TAG, 'size': '小型（11–50，ZoomInfo）' + TAG,
                          'other': '第 121 批：进口光延迟线 / RF-光转换器（tendata 5 票）→ **不动（产品不对位 + 非目标行业）**；部分坐实（贸易库地址）' + TAG}}],
    'SB-328': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 sales@advice.co.il Attn: Communication Products Manager — 一页纸一次：贴标 OEM 30%（STI-154GP 对 IGS-4215-4T2S / STI-054GP 对 ISW-501T）↔ 分销 20% 双轨 B + MOQ + 付费样机；PLANET 不点名 ' + IL + TAG}},
               {'facts': {'legal_name': 'Advice Electronics Ltd（公司号 511393159）', 'founded': '1988（领英口径 1989）' + TAG, 'hq': '16 Atir Yeda St., Kfar Saba, Israel（+972 3 900 0900）' + TAG, 'size': '中小型（51–200）' + TAG,
                          'other': '第 121 批：电源 / UPS / 通信方案分销 + 制造，ISO9001，站内在售 PLANET 工业机且自有 logo → **贴标 30% ↔ 分销 20% 双轨 一页纸一次（预付 100%）**；坐实（new-techguide Company ID + 地址 + 成立年）' + TAG}}],
    'SB-378': [{'kp_match': 'efi@', 'role': 'VP（研究档 KP）= 收件人 — 一页纸一次：集成商 25% B、对讲 / IP 监视器随机配套 PoE（STC-028GP $28 / STC-2216GP）一口价 + 贴标 30% 选项一句 + MOQ 1 + 付费样机 ' + IL + TAG},
               {'add_kp': {'name': 'Ophir Reuveni', 'role': '联系人（tradeindia 供应商档 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Pal Wintec Systems Ltd（公司号 1 查未得）', 'founded': '2000' + TAG, 'hq': '20 Hamagshimim St., P.O. Box 7184, Petah Tikva 4934829, Israel（+972 3 922 2051）' + TAG, 'size': '小型（约 35 人）' + TAG,
                          'other': '第 121 批：对讲 / 门禁 / 电话系统自研制造 + 出口；需求 af/at 常规 PoE、无需云管理 → **集成商 25% 一页纸一次（预付 100%）**；部分坐实（D&B 地址 + 成立年 + 人数）' + TAG}}],
    'SB-704': [{'add_kp': {'name': 'Ran Broudo', 'role': '联系人 / 负责人（cellpex 供应商档 2026-10-29；无公开邮箱）→ 收件 ethical@ethical-ltd.com Attn: Ran Broudo — 一页纸一次：分销 20% B、STC-110XGE $65 / STI-154GP / STI-288DGGPM $137 一口价 + MOQ 1 + 付费样机；在供 MC / 工业机品牌不点名 ' + IL + TAG}},
               {'facts': {'legal_name': 'Ethical Ltd（אתיקל בע"מ；公司号 512146788；Private Limited；Active）', 'founded': '1995-05-10（最近年报 2025）' + TAG, 'hq': '33 Shmuel Tamir St., Tel Aviv 6963717, Israel' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：采购服务 + 通信 / 电子产品供应商（元件、MC、终端服务器、工业交换机；在供 Perle 类）→ **分销 20% 一页纸一次（预付 100%）**；坐实（kycisrael 公司号 + 成立日 + 年报 + 地址）' + TAG}}],
    'SB-911': [{'facts': {'legal_name': '未取（1 查无命中；仅域名 itmarket.co.il + WA 电话）', 'founded': '未取' + TAG, 'hq': '未取（以色列）' + TAG, 'size': '小型（推定）' + TAG,
                          'other': '第 121 批：CCTV / 网络设备供应商（在售 ONV 工业 FS / MC）；16×0 + 无 KP + 未坐实 → **不动（B 保留）**' + TAG}}],
    'SB-915': [{'kp_match': 'dave_a@', 'role': 'Director of Product Management（研究档 KP）= 收件人 — 一页纸一次：贴标 OEM 30% B、CPE / IDU 配套 PoE 交换机贴标（STC-028GP $28 / STC-228GP $33 + 户外机柜 STI-154GP）+ MOQ + 付费样机；大厂一次即止 ' + IL + TAG},
               {'kp_match': 'sharon_sher', 'role': 'CEO（D&B / datanyze 2026-10-29 吻合）' + TAG},
               {'facts': {'legal_name': 'RADWIN Ltd（公司号 1 查未得）', 'founded': '1997' + TAG, 'hq': '27 Habarzel St., Tel Aviv 6971039, Israel（+972 3 766 2900）' + TAG, 'size': '大型（约 270 人；营收约 $68M）' + TAG,
                          'other': '第 121 批：运营商级固定无线 PtP / PtMP 原厂 → 仅配件贴标入口 → **贴标 OEM 30% 一页纸一次（预付 100%）**；部分坐实（企业库地址 + 成立年 + 人数 + CEO）' + TAG}}],
    'SB-934': [{'country_fix': '美国'},
               {'kp_match': 'billy.grumbles', 'role': '联系人（研究档 KP）= 收件人 — 一页纸一次：贴标 OEM 30% B、Alibi 自有品牌 PoE（STC-028GP $28 / STC-2216GP / STC-2224GP $86）贴标 + MOQ + 付费样机；在售 D-Link / TP-Link / Vigitron 不点名 ' + US + TAG},
               {'add_kp': {'name': 'Brian Wood', 'role': 'CEO（een.com 新闻 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Alibi Security（Observint Technologies 旗下品牌；德州登记号未取）', 'founded': '约 1990（自述 30+ 年经销商网络）' + TAG, 'hq': '15505 Long Vista Drive, Suite 250, Austin, TX 78728, USA（888-858-1442）' + TAG, 'size': '中型（100–200）' + TAG,
                          'other': '第 121 批：表内国别「以色列」误 → country_fix 美国（总部奥斯汀）；自有品牌安防 + 经销商渠道，转售 D-Link / TP-Link PoE → **贴标 OEM 30% 一页纸一次（预付 100%）**；NDAA 不声称；部分坐实' + TAG}}],
    # ---------------- KE 池 5 ----------------
    'SB-1076': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 kenya@simplifinetworks.com Attn: Product Manager — 一页纸一次：贴标 OEM 30%（自标 PoE 配件 / 工业 FS：STC-028GP / STC-2216GP / STI-154GP）↔ 分销 20% 双轨 B + MOQ + 付费样机；Ubiquiti / MikroTik 不点名 ' + KE + TAG}},
                {'facts': {'legal_name': 'Simplifi Networks Ltd（BRS 注册号 1 查未得）', 'founded': '2014' + TAG, 'hq': 'Unit 28, Fortis Industrial Park, off Mombasa Road, Nairobi 80100, Kenya（+254 727 401 262）' + TAG, 'size': '小型（约 12 人）' + TAG,
                           'other': '第 121 批：东非 Ubiquiti 直接分销 + MikroTik 主分销（内罗毕 / 坎帕拉 / 达市）；自有 logo PoE 配件 → **贴标 30% ↔ 分销 20% 双轨 一页纸一次（预付 100%）**；部分坐实（名录地址 + 成立年 + 人数）' + TAG}}],
    'SB-337': [{'kp_match': 'gadsatoh', 'role': '联系人（未具名；2024-07 回「price」）= 收件人 — 一页纸一次：集成商 25% B、passive PoE 不供明说 → STC-2216GP 标准 af/at + STC-228GP $33 一口价 + MOQ 1；PLANET 不点名 ' + KE + TAG},
               {'facts': {'legal_name': 'Kimberley Telecommunications（0 查：gmail + 无域名）', 'founded': '未取' + TAG, 'hq': '未取（肯尼亚）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 121 批：电信工程商，在用 PLANET，需求 2 光 16 电管理 passive PoE（非标）→ **集成商 25% 一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-586': [{'kp_match': 'mogeni@', 'role': '技术总监（研究档 KP；2024-03 回「有用，需沟通拿样」）= 收件人 — 一页纸一次：集成商 25% B、光纤上行摄像机接入（STI-154GP / STC-228GP $33）付费样机一口价 + 运费 ' + KE + TAG},
               {'facts': {'legal_name': 'Matrix Vision Systems / Matrix Systems（1 查仅美国 / 中东同名 → 本体未命中）', 'founded': '未取（自述 10 年以上）' + TAG, 'hq': '未取（Nairobi, Kenya）' + TAG, 'size': '小型（11–50）' + TAG,
                          'other': '第 121 批：电气 / 安防 / ICT 集成商（Hikvision 伙伴，NCA / CA 认证）→ **集成商 25% 一页纸一次（付费样机 + 预付 100%）**；未坐实' + TAG}}],
    'SB-896': [{'kp_match': 'wafulamusine', 'role': '联系人（研究档 KP；2025-04 回「interested」）— 不动：需求千兆 PoE 媒体转换器（不供）+ 无公司 ' + KE + TAG},
               {'facts': {'legal_name': '未取（0 查：gmail + 无公司名）', 'founded': '未取' + TAG, 'hq': '未取（肯尼亚）' + TAG, 'size': '个人' + TAG,
                          'other': '第 121 批：**不动（产品不对位 + 个人；来询按集成商 25% 报 STC-028GP）**；0 查' + TAG}}],
    'SB-897': [{'kp_match': 'wellspeter8', 'role': '业主（小型安装 / 转售；WA 已加；2024-06 要 price list）= 收件人 — 一页纸一次：集成商 25% B、STC-028GP $28 / STC-228GP $33 / STC-2216GP 一口价 + MOQ 1；百兆 MC 不供明说 ' + KE + TAG},
               {'facts': {'legal_name': '未取（0 查：gmail + 无公司名）', 'founded': '未取（2016 起用国际站）' + TAG, 'hq': '未取（肯尼亚）' + TAG, 'size': '微型' + TAG,
                          'other': '第 121 批：19 次推送 2 次实质回复 → **集成商 25% 一页纸一次（预付 100%）**；0 查' + TAG}}],
    # ---------------- JP 池 5 ----------------
    'SB-157': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 info@dci.jp Attn: 購買担当 / Purchasing — 一页纸一次：分销 20%（STC-110XGE $65 / STI-154GP / STI-288DGGPM $137）↔ 贴标 OEM 30% 双轨 B + MOQ 1 + 付费样机；在供品牌不点名 ' + JP + TAG}},
               {'facts': {'legal_name': 'データコントロルズ株式会社 Data Controls Inc.（法人番号 1 查未得）', 'founded': '1983' + TAG, 'hq': '〒111-0052 東京都台東区柳橋 1-20-4 深代ビル 8F, Japan（03-5829-5805；日经登記住所同址）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：网络设备（MC / 工业交换机）开发 + 进口销售 + 修理 → **分销 20% ↔ 贴标 30% 双轨 一页纸一次（预付 100%）**；部分坐实（会社案内 PDF + 登記住所）' + TAG}}],
    'SB-158': [{'kp_match': 'info@diatrend', 'role': '代表取締役 / Managing Director（法人登記 宮下清哉 2026-10-29 吻合）= 收件人 — 一页纸一次：贴标 OEM 30% B、STI-154GP / STI-288DGGPM $137 + STC-110XGE $65 贴标 + MOQ + 付费样机；SFP 不供明说 ' + JP + TAG},
               {'facts': {'legal_name': 'ダイヤトレンド株式会社 Diatrend Corporation（法人番号 5120001026515；子会社 DT エンジニアリング）', 'founded': '1971-08' + TAG, 'hq': '〒530-0011 大阪府大阪市北区大深町 3-1, Japan（2017-01 起；旧址 中央区南船場 2-2-14）' + TAG, 'size': '中小型' + TAG,
                          'other': '第 121 批：电子应用产品企划开发・制造・销售（接口 / 光缆 / PoE 延长），自有 label 工业 FS / MC / SFP → **贴标 OEM 30% 一页纸一次（预付 100%）**；坐实（法人番号 + 設立 + 代表 + 本店）' + TAG}}],
    'SB-161': [{'add_kp': {'name': 'Akira Ohe（大江）', 'role': 'CEO / 代表取締役（官网会社概要 2026-10-29）→ 收件 info@mahanet-jp.com Attn: Mr. Ohe — 最后一次一页纸：贴标 OEM 30% B、MH-7204E / 7208E / 7216E-L2 / 7224E-L2 对位 STC-028GP $28 / STC-2216GP / STC-4424GCPM $165 贴标 + MOQ + 付费样机；UTEPO 不点名 ' + JP + TAG}},
               {'facts': {'legal_name': 'マハネット株式会社 Mahanet Co., Ltd.（法人番号 7390001009301；資本金 1,000 万円）', 'founded': '2005-02-25' + TAG, 'hq': '〒999-3716 山形県東根市大字蟹沢 1646-33, Japan（0237-42-5833）' + TAG, 'size': '微型（被保険者 4 人）' + TAG,
                          'other': '第 121 批：防犯カメラ販売施工 + 自有 MH 系列 IP 摄像机 / NVR / PoE 交换 HUB，全省庁統一資格 → **贴标 OEM 30% 最后一次一页纸（预付 100%）**；7×0；坐实（gBizINFO 法人番号 + 設立 + 本店）' + TAG}}],
    'SB-164': [{'facts': {'legal_name': 'UNEAX 株式会社（法人番号 6021001077094）', 'founded': '2022-10-04（新壳）' + TAG, 'hq': '〒242-0007 神奈川県大和市中央林間 5-5-23-6, Japan' + TAG, 'size': '微型（従業員 1 人，eigyo-mfg）' + TAG,
                          'other': '第 121 批：微型同行（SSD 販売 + 産業用イーサネットスイッチ開発・販売 + IoT + 金型加工）；2026-04/05 在谈「国内外壳」工业机自标 → **贴标 OEM 30% 一页纸一次（STI-054GP / STI-154GP / STI-288DGGPM $137 贴标 + MOQ + 付费样机；合规只给 CE / RoHS / FCC 现有件；1 人新壳 → 预付 100% 不让步）**；KP 角色沿用研究档（Ryosuke Osako 收件 / Mari Inoue 技术合规）；坐实（法人番号 + 設立 + 本店）' + JP + TAG}}],
    'SB-822': [{'add_kp': {'name': 'Tatsuto Tokuoka（徳岡達人）', 'role': '代表取締役（PR 稿会社概要 2026-10-29；无公开邮箱）→ 收件 support@solidcable.com Attn: 仕入担当 / Purchasing — 一页纸一次：贴标 OEM 30%（STC-110XGE $65 / STC-028GP $28 自标）↔ 分销 20% 双轨 B + MOQ + 付费样机；在供品牌不点名 ' + JP + TAG}},
               {'facts': {'legal_name': 'ソリッド株式会社 Solid Corp.（品牌 ソリッドケーブル；企业站 solid-corp.com；法人番号 1 查未得）', 'founded': '未取（EC 2004 起）' + TAG, 'hq': '〒541-0042 大阪府大阪市中央区今橋 2-3-16 5F, Japan（06-6228-0577）' + TAG, 'size': '小型（<500 自报）' + TAG,
                          'other': '第 121 批：线缆 / 通信周边製造直販 EC（TV / 网络线缆、当日発送；在售 ONV 类 MC）→ **贴标 30% ↔ 分销 20% 双轨 一页纸一次（预付 100%）**；部分坐实（PR 会社概要 + 代表）' + TAG}}],
    # ---------------- KZ 池 4 ----------------
    'SB-037': [{'add_kp': {'name': 'Sabit Karimov（Каримов Сабит Мухтарович）', 'role': 'Директор（adata.kz 2026-10-29；无公开邮箱）→ 收件 info@pulsar.kz Attn: Mr. Karimov — 一页纸一次：分销 20% B、16 PoE + 2 SFP 类对位 STC-2216GP $63–76 / STC-2224GP $86 / STC-4424GCPM $165 一口价 + MOQ 1 + 付费样机；在代 PoE 品牌不点名；俄罗斯转售买方自理 ' + KZ + TAG}},
               {'facts': {'legal_name': 'ТОО «Pulsar Systems» / Pulsar Systems LLP（БИН 100740012554）', 'founded': '2010-07-23' + TAG, 'hq': 'пр. Бауыржан Момышұлы 2В, оф. 16, район Алматы, Астана 010000, Kazakhstan（阿拉木图办公 ул. Ходжанова 79）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：PoE 交换机品牌哈 + 俄独家代理 + ZKTeco / Hikvision 在售；ОКЭД 47421 → **分销 20% 一页纸一次（预付 100%）**；坐实（statsnet / adata / kyc.kz БИН + 注册日 + 负责人）' + TAG}}],
    'SB-622': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 info@market-telecom.kz Attn: Отдел закупок / Purchasing — 最后一次一页纸：分销 20% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 / STI-154GP 一口价 + MOQ 1 + 付费样机；在售 ONV / Planet 类不点名 ' + KZ + TAG}},
               {'facts': {'legal_name': 'ТОО «Авантаж Маркет» Avantazh Market（БИН 221040045999；关联 ТОО «Авантаж Маркет-телеком» БИН 170740023007）', 'founded': '2022-10（现法人；业务 2010 起，关联法人 2017）' + TAG, 'hq': 'ул. Нурсултана Назарбаева 133, НП1, Петропавловск 150000, Kazakhstan（阿斯塔纳 ул. Дотык 18；阿拉木图仓；+7 7172 97 84 70）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：通信 / 安防 / IT 设备网店 + 工程，多品牌（TP-Link / Dahua / Hikvision / Ubiquiti / MikroTik + ONV / Witech / Planet 交换机）→ **分销 20% 最后一次一页纸（预付 100%）**；18×0；坐实（官网自列 БИН + e-gov 核验 2026-10-12）' + TAG}}],
    'SB-799': [{'kp_match': 'invest_01otp', 'role': '联系人（未具名；mail.ru 身份不明）— 不动：招标杂货供应商 + 无对口需求 ' + KZ + TAG},
               {'add_kp': {'name': 'Alina Nurpeisova（Нурпеисова Алина Бакытжановна）', 'role': 'Руководитель（niac.kz 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'ТОО «VERTEX INVADER»（БИН 181140013835）', 'founded': '2018（niac 2018-11-13 / wikicity 2018-01-13 口径不一）' + TAG, 'hq': 'ул. Александра Пушкина 41/2, район Байқоңыр, Астана 010000, Kazakhstan' + TAG, 'size': '小型（11–15）' + TAG,
                          'other': '第 121 批：ОКЭД 47.99.9 店外零售 / 其他设备批发，ETS 招标平台参与者；表内「俄罗斯」已更正哈萨克斯坦（研究档）→ **不动（查无对口业务；来询预付 100%）**；坐实（БИН + 地址 + 负责人）' + TAG}}],
    'SB-941': [{'kp_match': 'comtek@', 'role': '联系人（研究档 KP；阿里 RFQ 来源）— 不动：企业级 IT 分销（Cisco / Dell / Ubiquiti 等）+ 唯一需求 PoE 分离器（不供）' + KZ + TAG},
               {'facts': {'legal_name': 'ТОО «CompTek CA»（БИН 1 查未得）', 'founded': '未取' + TAG, 'hq': 'пр. Райымбека 165А, 3 этаж, офис 6, Алматы, Kazakhstan（+7 727 246-82-21 / -22；n.drobysheva@comptek.kz）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：**不动（产品不对位；来询按分销 20% 报 STC 商用线）**；部分坐实（zoon / tel-spravochnik / facebook 地址）' + TAG}}],
    # ---------------- ZM 池 4 ----------------
    'SB-102': [{'kp_match': 'sales@densoelectronics', 'role': '联系人（研究档 KP，表内 Mr.）= 收件人 — 一页纸一次：分销 20% B、STC-028GP $28 / STC-228GP $33 / STC-110XGE $65 一口价 + MOQ 1；千兆工业 MC 不供明说 ' + ZM + TAG},
               {'facts': {'legal_name': 'Denso Electronic Solutions（PACRA 号 1 查未得）', 'founded': '1997' + TAG, 'hq': 'Suite 02-37 Compensation House, Broadway / Moffat Roads, Ndola, Zambia（+260 212 615190；WA +260 977 823 625）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：电子元件 / ICT 综合供应商（有进口经验）→ **分销 20% 一页纸一次（预付 100%）**；部分坐实（官网地址 + 成立年）' + TAG}}],
    'SB-1120': [{'kp_match': 'pythiask', 'role': 'Founder / CEO / Managing Director（官网 + 领英 2026-10-29 吻合；2024-01 订单单据联系人）= 收件人 — 复购一页纸一次：STC-4248 系列复购价 + STI-154GP / STI-288DGGPM $137 太阳能 EPC 配套 DIN 机 + MOQ 1 ' + ZM + TAG},
                {'facts': {'legal_name': 'Obmac Systems（PACRA 号 1 查未得）', 'founded': '2007-02-13' + TAG, 'hq': '未取（Lusaka, Zambia；起家 Ndola）' + TAG, 'size': '微型（约 7 人；营收约 $2.6M，datanyze）' + TAG,
                           'other': '第 121 批：★ 已成单（2024-01 $9,350，PI 包「gg」= Simon 定级难复购）+ 创始人 CEO 为 KP；ICT / 电气 / 机械项目承包与采购，转向太阳能 EPC → **复购一页纸一次（预付 100%）；B 保留，回信即升 A 候选**；部分坐实（官网成立日 + 领英 CEO）' + TAG}}],
    'SB-222': [{'add_kp': {'name': '（未具名 WA 联系人）', 'role': 'WA +260 97…（5 次实质回复；2026-06 问价）— WA 一页纸一次：集成商 25% B、STI-054GP / STI-154GP / STI-280GE $46.6 一口价 + MOQ 1 + 付费样机；同时一句话问公司名 / 邮箱 ' + ZM + TAG}},
               {'facts': {'legal_name': '未取（0 查：无邮箱 / 姓名 / 公司）', 'founded': '未取' + TAG, 'hq': '未取（赞比亚）' + TAG, 'size': '未知' + TAG,
                          'other': '第 121 批：「小工业机近期可能有需求」→ **WA 一页纸一次（预付 100%）**；0 查' + TAG}}],
    'SB-865': [{'kp_match': 'dbjcontrad', 'role': '联系人（研究档 KP；2022 起与 e. 账号来往）— 不动：需求 Cisco 兼容交换机 + 10G DAC（不供）+ 无公司 ' + ZM + TAG},
               {'facts': {'legal_name': '未取（0 查：hotmail + 无公司名）', 'founded': '未取' + TAG, 'hq': '未取（赞比亚）' + TAG, 'size': '微型' + TAG,
                          'other': '第 121 批：IT 承包 / 网络 → **不动（产品不对位 + 个人；来询按集成商 25% 报 STC-4424GCPM $165）**；0 查' + TAG}}],
    # ---------------- HK 池 4 ----------------
    'SB-1027': [{'kp_match': 'allenc@', 'role': 'Director（研究档 KP）= 收件人 — 一页纸一次：分销 20% B、STC-028GP $28 / STC-2224GP $86 / STC-4424GCPM $165 / STI-154GP 一口价 + MOQ 1 + 付费样机；在代 LevelOne / Zyxel 类不点名 ' + HK + TAG},
                {'kp_match': 'sales@everbesthk', 'role': 'Product Manager（研究档 KP）' + TAG},
                {'facts': {'legal_name': 'Everbest Technologies Limited 永佳科技有限公司（CR No. 334414；BR No. 15215848）', 'founded': '约 1991（自述港澳代理起）' + TAG, 'hq': '14/F Wing Hang Insurance Building, 11 Wing Kut Street, Central, Hong Kong（+852 2541 2982）' + TAG, 'size': '小型' + TAG,
                           'other': '第 121 批：IT / 网络产品港澳分销（ATEN 官方 where-to-buy 2026 列名；Zyxel / LevelOne / DrayTek）→ **分销 20% 一页纸一次（预付 100%）**；坐实（inriskable CR + BR 号 + 官网地址）' + TAG}}],
    'SB-219': [{'kp_match': 'venta@', 'role': 'Electronic Engineer（研究档 KP）= 收件人 — 最后一次一页纸：贴标 OEM 30% B、STC-028GP $28 / STC-2216GP / STC-2224GP $86 Siera 贴标 + MOQ + 付费样机；在供 ONV 不点名；西语备注 ' + HK + TAG},
               {'facts': {'legal_name': 'Siera Electronics（Siera Holding Group；CR 号 1 查未得）', 'founded': '1995' + TAG, 'hq': '565-567 Nathan Road, Unit 2201B, 22/F, Kowloon, Hong Kong' + TAG, 'size': '小型（11–50；领英自报 201–500 偏高）' + TAG,
                          'other': '第 121 批：自有品牌安防（Sieco）面向拉美，自有 label 商用 PoE 在售 → **贴标 OEM 30% 最后一次一页纸（预付 100%）**；18×0；部分坐实（领英地址 + 成立年）' + TAG}}],
    'SB-705': [{'kp_match': 'info@eware', 'role': 'System Engineer（研究档 KP）= 收件人 — 最后一次一页纸：集成商 25% B、IP 话机 / AP 供电配套（STC-2216GP / STC-2224GP $86 / STC-4424GCPM $165）一口价 + MOQ 1 + 付费样机 ' + HK + TAG},
               {'facts': {'legal_name': 'Eware Networks Limited（CR 号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Unit 2102-03, 21/F, Two Sky Parc, 51 Hung To Road, Kwun Tong, Kowloon, Hong Kong（+852 2565 0165；旧址 Rm 1107 Futura Plaza）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：UC / 视频会议 / IP 电话集成（穗深支持热线）→ **集成商 25% 最后一次一页纸（预付 100%）**；8×0；部分坐实（官网地址 + 电话）' + TAG}}],
    'SB-717': [{'add_kp': {'name': '（无具名 KP）', 'role': '收件 sales@skyware.com.hk Attn: Sales Manager — 最后一次一页纸：集成商 25% B、楼宇 IoT 配套工业小机（STI-054GP / STI-154GP / STI-280GE $46.6）一口价 + MOQ 1 ' + HK + TAG}},
               {'facts': {'legal_name': 'SkyWare ProTech Limited（2017 年名 Skyware Technologies Limited；CR 号 1 查未得）', 'founded': '约 2001（自述）' + TAG, 'hq': 'Room 3806A, 38/F, Cable TV Tower, 9 Hoi Shing Road, Tsuen Wan, N.T., Hong Kong（+852 3106 0868）' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：可编程网络 / 楼宇 IoT 设备商（HMP200；SensMax 经销）→ **集成商 25% 最后一次一页纸（预付 100%）**；8×0；部分坐实（官网 + tradeeasy 地址）' + TAG}}],
    # ---------------- LB 池 4 ----------------
    'SB-202': [{'kp_match': 'egc@', 'role': 'Founder / General Manager（crunchbase + 领英 2026-10-29 吻合）= 收件人 — 最后一次一页纸：集成商 25% B、30 台环网 STI-288DGGPM $137 ERPS 一口价 + STC-228GP $33 接入；光端机 / VC 不供明说 ' + LB + TAG},
               {'facts': {'legal_name': 'Engineering Group Contractors (EGC)（贝鲁特商业登记号 1 查未得）', 'founded': '1988（RocketReach）' + TAG, 'hq': 'Borj Al Jazeera Bldg., Ibn El Asir St., Corniche El Mazraa, Beirut, Lebanon（+961 1 701546）' + TAG, 'size': '小型（7–50）' + TAG,
                          'other': '第 121 批：安防设备分销 / 集成 + 避雷接地系统；曾谈 30 台 2 光 10 电环网 → **集成商 25% 最后一次一页纸（预付 100%）**；19×0；部分坐实（官网地址 + 企业库成立年 + GM）' + TAG}}],
    'SB-296': [{'country_fix': '阿联酋'},
               {'kp_match': 'k.haidar', 'role': 'Director（表内；研究档 KP）— 不动：卫星上行 / 广播服务商 + 需求 HDMI over IP（不供）' + AE + TAG},
               {'facts': {'legal_name': 'BHS Media / BHS Telecommunications（Dubai Media City 执照号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'No.401, Building No.1, Dubai Media City, Sheikh Zayed Road, Dubai, UAE（+971 4 551 5523）' + TAG, 'size': '小型（约 20 人，ZoomInfo）' + TAG,
                          'other': '第 121 批：表内国别「黎巴嫩」= KP 电话归属，总部迪拜媒体城 → country_fix 阿联酋；**不动（产品不对位 + 非目标行业；来询按集成商 25% 报 STC-4424GCPM）**；部分坐实（官网地址 + 人数）' + TAG}}],
    'SB-324': [{'kp_match': 'melhem@', 'role': 'Owner / Managing Director（kompass 所有者 Adnan A. Melhem 2026-10-29 吻合）= 收件人 — 一页纸一次：分销 20%（STC-028GP $28 / STC-2216GP / STC-2224GP $86）↔ 贴标 OEM 30% 双轨 B + MOQ 1 / 贴标 MOQ + 付费样机 ' + LB + TAG},
               {'add_kp': {'name': 'Jad A. Melhem', 'role': 'Owner（kompass 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Melhem Trading Co. SARL (MTCO)（商业登记号 1 查未得；所有者 Adnan A. Melhem / Rouba N. Khoury / Jad A. Melhem）', 'founded': '2004（黎巴嫩 + 尼日利亚）' + TAG, 'hq': 'Ground floor, Riachi Building, Dora Highway, Bauchrieh (Metn), Lebanon（+961 1 245 000）' + TAG, 'size': '小型（11–50）' + TAG,
                          'other': '第 121 批：CCTV / 线缆 / 灯光 / 音响 / 通信进口分销 + 自有品牌（韩 / 中 / 台代工）→ **分销 20% ↔ 贴标 30% 双轨 一页纸一次（预付 100%）**；部分坐实（kompass 地址 + 成立年 + 所有者）' + TAG}}],
    'SB-327': [{'kp_match': 'amine@', 'role': 'General Manager（家族企业；kompass 所有者 Fadi J. / Grace Y. Abou Jaoudeh；2024-04 问价）= 收件人 — 一页纸一次：分销 20% B、STC-028GP $28 / STC-228GP $33 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1 + 付费样机 ' + LB + TAG},
               {'add_kp': {'name': 'Fadi J. Abou Jaoudeh', 'role': 'Owner（kompass 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Techno Tower SARL（商业登记号 1 查未得；P.O. Box 90-1776）', 'founded': '1998（kompass；官网口径 1989）' + TAG, 'hq': 'Ground floor, Abou Karam 1 Building, Jdeideh (Metn), Lebanon' + TAG, 'size': '小型' + TAG,
                          'other': '第 121 批：自动化 / 安防 / CCTV / 消防 / 卫星 / 灯光进口分销商 → **分销 20% 一页纸一次（预付 100%）**；部分坐实（kompass 地址 + 成立年 + 所有者）' + TAG}}],
    # ---------------- MX 池 4 ----------------
    'SB-703': [{'kp_match': 'ecamberos', 'role': '联系人（研究档 KP；自站 RFQ 2 光 10 电）= 收件人 — 一页纸一次：集成商 25% B、STI-288DGGPM $137（2 SFP + 8 GE）或 STC-2216GP 16+2 一口价 + MOQ 1；西语备注 ' + MX + TAG},
               {'facts': {'legal_name': 'Engitel（墨西哥；1 查仅命中意大利 Engitel S.p.A. ≠ 本户）', 'founded': '未取' + TAG, 'hq': '未取（Mexico）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 121 批：IT 咨询 / 网络小型企业 → **集成商 25% 一页纸一次（预付 100%）**；未坐实' + TAG}}],
    'SB-892': [{'kp_match': 'telcofusion1', 'role': '联系人（研究档 KP；2024-08 问 10G MC ×4）= 收件人 — 最后一次一页纸：集成商 25% B、STC-110XGE $65 ×4 一口价 + 运费；反向 PoE 不供明说；西语备注 ' + MX + TAG},
               {'facts': {'legal_name': 'Telcofusion（1 查无命中；gmail 联系）', 'founded': '未取' + TAG, 'hq': '未取（Mexico）' + TAG, 'size': '微型（推定）' + TAG,
                          'other': '第 121 批：电信承包 / 安装商 → **集成商 25% 最后一次一页纸（预付 100%）**；15×0；未坐实' + TAG}}],
    'SB-927': [{'kp_match': 'info@rarmx', 'role': '联系人（研究档 KP；阿里 RTS 订单「5 电口」）= 收件人 — 复购一页纸一次：STI-054GP / STI-280GE $46.6 / STI-154GP 水厂 DIN 机一口价 + MOQ 1；西语备注 ' + MX + TAG},
               {'facts': {'legal_name': 'RARMX Engineering, S.A. de C.V.（RFC 1 查未得；tendata 进口主体）', 'founded': '未取' + TAG, 'hq': '未取（Monterrey, N.L., Mexico；+52 81）' + TAG, 'size': '小型（推定）' + TAG,
                          'other': '第 121 批：★ 阿里 RTS 已成单 + 2025-08 自中 / 美 7 家供应商进口控制模块 / 过滤设备件（真实进口主体）；水处理 / 工程 → **复购一页纸一次（预付 100%）；回信即升 A 候选**；部分坐实（进口记录 + 法人形式）' + TAG}}],
    'SB-960': [{'add_kp': {'name': 'Goyazlay Keri González Rodríguez', 'role': 'Key Principal（D&B 2026-10-29；无公开邮箱）；收件 info@steren.com.mx — 口径定前不动 ' + MX + TAG}},
               {'facts': {'legal_name': 'Electrónica Steren, S.A. de C.V.（RFC 不公开；Active）', 'founded': '未取（1956 起，研究档）' + TAG, 'hq': 'Biólogo Maximino Martínez No. 3408, Col. San Salvador Xochimanca, Azcapotzalco, Ciudad de México 02870, Mexico' + TAG, 'size': '大型（连锁；进口 69,873 票 / 539 家供应商，volza）' + TAG,
                          'other': '第 121 批：电子产品批发 + 自有品牌连锁零售；自有品牌商用 PoE 且 HRUI 在供 → **Q-33 口径待 Simon（只推 SmartByte / Marvell 管理 + 工业线 贴标 OEM 30%：STC-4424GCPM $165 / STI 系列）→ 口径定前不动（B 保留；同 SB-523 / SB-1102）**；部分坐实（D&B 地址 + 进口记录）' + TAG}}],
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
