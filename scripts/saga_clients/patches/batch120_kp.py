#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 120 批（T29-U113，公司底数第三十八轮 · 沙特池余 3 + 菲律宾 B 池 11 + 南非 B 池 10 + 印尼 B 池 10 + 巴西 B 池前 6 = 40 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 成立 / 总部 / 规模 / 定性 回写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/other_registry_2026-10-27.json（batch=120 行）。
本批定性：升 A 候选 0（SB-1137 Infotec 直接进口商 + 两次主动要价 → 回信即升 候选）；
一页纸一次 · 集成商 25% 15（SB-404 TEAMAC 沙迦 / SB-071 NKS 电力 SCADA 按单核 / SB-1012 Bitstream Core / SB-141 Agile Cebu / SB-227 NKF 付费样机 / SB-979 iOne CEO KP / SB-443 Spring Network / SB-615 Hands On Security / SB-904 Nuthill 7 台询盘 / SB-050 PT AAG 2011 老客户回访 / SB-1100 Firman / SB-115 Catur Citra Wisesa 182592 / SB-203 Suryatama / SB-512 Solus CNPJ 07.270.661 / SB-591 Elementu CNPJ 14.458.461）；
一页纸一次 · 分销 20% 9（SB-054 Testronix SEC CS200518694 / SB-312 Fibercom / SB-314 RSPOT / SB-1117 Switchcom 2015/334722/07 / SB-042 Regal 双轨 ↔ 贴标 30% / SB-978 Eurobyte 对价 PLANET / SB-456 Panca Kumala DCN 渠道 / SB-1089 tpnet 未坐实 / SB-1137 Infotec CNPJ 05.590.805 进口商）；
一页纸一次 · 贴标 OEM 30% 3（SB-672 Netshield 自有品牌 1994 / SB-142 Airpo 自有品牌 / SB-498 Daiken CNPJ 10.497.398 电子制造）；
不动 13（SB-464 Hamdaz IT 服务 新壳 阿布扎比 / SB-008 个人 / SB-067 CREC 上市电力终端 / SB-412 MC 不对位 / SB-735 个人 / SB-516 Brigit 消防 OEM / SB-636 Marzetek 投标杂货 / SB-860 Basithami 15×0 / SB-179 主体待核 / SB-382 个人 / SB-414 全 SFP 不对位 / SB-610 个人 / SB-1090 tramaweb 误归属 新闻社）。
坐实 9（SB-054 / 067 / 1117 / 115 / 1090 / 1137 / 498 / 512 / 591）/ 部分坐实 15（SB-404 / 464 / 071 / 312 / 314 / 979 / 042 / 516 / 615 / 672 / 860 / 904 / 978 / 050 / 456）/ 未坐实 5（SB-1012 / 636 / 142 / 203 / 1089）/ 0 查 11（SB-008 / 141 / 227 / 412 / 735 / 1100 / 179 / 382 / 414 / 610 / 443）。
KP 坐实 = 老板 / 总经理 / 法人本人 5（SB-979 Alberto A. Catangui CEO / SB-516 Deon van Zyl MD / SB-672 Inus Dreckmeyr CEO / SB-1137 Ema Ines Rodriguez Rodriguez 法人 / SB-404 Khursheed Ahmed Khan Sales & Technical Director）；新增 KP 5（SB-312 Emanuel Fryszer / SB-314 Juner D. Yaneza / SB-904 Abrie Joubert CEO / SB-1137 Ema Ines Rodriguez Rodriguez / SB-050 Gunawan）。
法定名补全 / 更正 29；**country_fix 2（SB-404 → 阿联酋：实体沙迦 Hamriyah FZ，回正 Q-65 的 +966 手机判定；SB-464 → 阿联酋：总部阿布扎比 Millennium Tower）**。
PH 路径实测（首次，11 户 2 个 SEC 号）：companyhouse.ph「SEC Code」（SB-054）/ 上市公司 SEC 17-C / 17-Q（SB-067）；官网页脚 + D&B / verif / businesslist.ph / aihitdata 补地址；厂商经销名录（Foxcom / Vericom）给具名联络人（SB-312 / 314）。
ZA 路径实测（首次，10 户 1 个注册号）：官网 T&C 自列「registration number YYYY/NNNNNN/07」（SB-1117）；D&B / yellosa / hsbd / ZoomInfo / RocketReach 补地址 + CEO；CIPC 不可 1 查；政府投标名单可证 (Pty) Ltd 存在（SB-636）。
ID 路径实测（首次，10 户 1 个登记号）：companieshouse.id / companyhouse.id 镜像（登记号 + 注册地址，SB-115）；官网 contact 补地址（SB-050 / 456）；品牌站 + 经销名单证自有品牌（SB-142）；同名极多（PT Suryatama）→ 未坐实；gmail / yahoo 无公司名 5 户 → 0 查。
BR 路径实测（首次，6 户 5 个 CNPJ，命中率最高之一）：cnpj.biz / casadosdados / econodata / serasa 1 查即得 CNPJ + 法人 + 开业日 + CNAE + Simples + 地址 + 电话（SB-1137 / 498 / 512 / 591 / 1090）；jusbrasil 进口税诉讼可证直接进口商（SB-1137）；域名实体 ≠ 表内业务 → 误归属（SB-1090）；同名多家无域名对齐 → 未坐实（SB-1089）。
Simon 待决：SB-404 / SB-464 沙特 → 阿联酋 更正；SB-1090 / SB-179 / SB-008 WA 问一句公司名；SB-1137 回信即升 A。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 120 批 官方登记核实 2026-10-29）'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜、TDRA / ESMA 不声称'
SA = '— 沙特常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP、SASO / SABER 不声称'
PH = '— 菲律宾常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 马尼拉、NTC 不声称'
ZA = '— 南非常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 约堡、ICASA / NRCS 不声称'
ID = '— 印尼常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 雅加达、SDPPI 不声称'
BR = '— 巴西常规：英文稿（可附葡语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（进口税自理）、Anatel 不声称'
UPD = {
    # ---------------- SA 余 3 ----------------
    'SB-404': [{'country_fix': '阿联酋'},
               {'kp_match': 'khursheed', 'name': 'Khursheed Ahmed Khan', 'role': 'Sales & Technical Director（tradeindia 2026-10-29；= 表内 KP）= 收件人 — 一页纸一次：集成商 25% B、询盘「8 光 8 PoE 管理」→ STI-288DGGPM / STI-488DGGPM + STC-4424GCPM 组合一口价 + MOQ 1 + 付费样机 ' + AE + TAG},
               {'facts': {'legal_name': 'TEAMAC Arabia（Hamriyah Free Zone 实体；FZ 牌照号 1 查未得）', 'founded': '2008（tradeindia）' + TAG, 'hq': 'Hamriyah Free Zone, P.O. Box 50342, Sharjah, UAE' + TAG, 'size': '小型' + TAG,
                          'other': '第 120 批：BMS / HVAC 控制 + 弱电 + 进口贸易；实体在沙迦自贸区 → country_fix 阿联酋（回正 Q-65 按 +966 手机的沙特判定；KP 沙特手机 = KSA 销售驻点）；部分坐实（名录地址 + 成立年 + KP 职务）' + TAG}}],
    'SB-464': [{'country_fix': '阿联酋'},
               {'kp_match': 'rea@', 'role': '联系人（职务未得；研究档 KP）— 不动：IT / 托管软件服务商 + 2023/24 新壳 + WA 无实质回复 ' + AE + TAG},
               {'add_kp': {'name': 'Jishad Mohammed Vakatel', 'role': 'Founder & CEO（prospeo 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'HAMDAZTECH TECHNOLOGY SERVICES LLC（阿布扎比；牌照号未取）/ HAMDAZ TECHNOLOGIES LLP（印度 Kozhikode；CIN ACA-6304）', 'founded': '2023-04-18（印度 LLP）/ 2024（UAE，prospeo 口径）' + TAG, 'hq': 'PO Box 5758, Office 22, 2nd Floor, Millennium Tower, Hamdan Street, Abu Dhabi, UAE（+971 2 309 0211；印度 +91 92077 73300 = 表内电话）' + TAG, 'size': '小型（21–50 自报）' + TAG,
                          'other': '第 120 批：表内「HAMDAZTECH TECHNOLOGIES INC LLC」+ 沙特 = 误录，总部阿布扎比 → country_fix 阿联酋；IT 服务 + 新壳 → **不动（B 保留）**；部分坐实' + TAG}}],
    'SB-008': {'facts': {'legal_name': '未取（WhatsApp 个人 Abdulaziz Al Jowasem；无公司 / 域名 / 邮箱 → 0 查）', 'other': '第 120 批：0 查；个人 + 19×0 → **不动（B 保留；WA 只问一句公司 / 网站）** ' + SA + TAG}},
    # ---------------- PH 11 ----------------
    'SB-054': {'facts': {'legal_name': 'Testronix, Inc.（SEC Code CS200518694，companyhouse.ph）', 'founded': '2005（SEC 号前缀）' + TAG, 'hq': 'Unit 415, VGP Center, 6772 Ayala Avenue, Makati City 1226, Philippines（Globe 0966 190 3000）' + TAG, 'size': '小型' + TAG,
                         'other': '第 120 批：测试仪表 / 数通 / 光模块 / MC 分销商（JDSU / Furukawa）→ **分销 20% B，一页纸一次（Attn: Sales Manager；STC-110XGE + STC-228GP / STC-2224GP；SFP 不做明说）** ' + PH + '；坐实（SEC 号 + 地址）' + TAG}},
    'SB-067': [{'add_kp': {'name': 'Oliver Y. Tan', 'role': 'Key Principal（D&B 2026-10-29；无公开邮箱）— 不动：上市电力终端用户，采购经 EPC' + TAG}},
               {'facts': {'legal_name': 'Citicore Renewable Energy Corporation（SEC Reg. No. CS201807415；BIR TIN 010-007-383-000；PSE 上市）', 'founded': '2018（SEC 号前缀；SEC 17-C 2025-06-18）' + TAG, 'hq': '11F Rockwell Santolan Town Plaza, 276 Col. Bonny Serrano Avenue, San Juan City, Metro Manila 1500（+632 8826 5698）' + TAG, 'size': '大型（上市）' + TAG,
                          'other': '第 120 批：上市可再生能源发电终端 + 采购经 EPC / O&M → **不动（B 保留；电力按单核；对口的是其集成商如 SB-071 NKS）**；坐实（SEC 披露文件）' + TAG}}],
    'SB-071': [{'kp_name': 'Mark Delapaz', 'role': 'NKS 员工（ZoomInfo 公开；职务待核）= 收件人 — 一页纸一次：集成商 25% B、已外采 Maiwe 的变电站自动化集成商 → STI-288DGGPM / STI-488DGGPM + STI-280GE 一口价 + 付费样机；不声称 IEC 61850 / 电力认证；电力项目按单核 ' + PH + TAG},
               {'facts': {'legal_name': 'Nayon Kontrol Systems（NKS；SEC 号 1 查未得；关联 NKS Solar One, Inc. / NKS Energy Utilities, Inc. / NKS Global Limited）', 'founded': '约 1996（aihitdata「29 years」）' + TAG, 'hq': 'No. 4 Illinois St., Brgy. Silangan, District III, Cubao, Quezon City 1109, Philippines' + TAG, 'size': '中小型' + TAG,
                          'other': '第 120 批：电力合作社 SCADA / 变电站自动化 / RTU 集成商；部分坐实（企业库地址 + 成立年；SEC 未取）' + TAG}}],
    'SB-1012': [{'kp_match': 'ieviola', 'role': 'General Manager（研究档）= 收件人 — 一页纸一次：集成商 25% B、2 光 2 电 → STC-228GP / STC-028GP + STI-154GP 一口价 + 付费样机；SFP 不做明说 ' + PH + TAG},
                {'facts': {'legal_name': 'Bitstream Core（bitstreamcore.com；1 查无命中 → 未坐实）', 'other': '第 120 批：未坐实（1 查仅无关结果）；GM 为 KP + 口型明确 → 一页纸一次（预付 100%）' + TAG}}],
    'SB-141': [{'kp_match': 'ph.agilenetwork', 'role': 'CEO（表内）= 收件人 — 一页纸一次：集成商 25% B、STC-110XGE 一口价（光模块不供明说）+ STC-228GP + 付费样机 ' + PH + TAG},
               {'facts': {'legal_name': '未取（Agile Network，宿务 Pari-an；通名 + gmail → 0 查；表内域名 agilenetworks.com 为美国 ISP，误归）', 'other': '第 120 批：0 查；CEO 为 KP + 2024-08 问过 10G MC 单 / 多模价 → 一页纸一次（预付 100%）' + TAG}}],
    'SB-227': [{'kp_match': 'joemar', 'role': '业主（小型 WISP）= 收件人 — 一页纸一次：集成商 25% B、2026-01 索样 → STI-154GP / STC-228GP 付费样机一口价 + 运费；PON 不供明说 ' + PH + TAG},
               {'facts': {'legal_name': '未取（NKF Wireless Internet and Services；gmail + 无域名 → 0 查）', 'other': '第 120 批：0 查；索样已回 → 付费样机一页纸一次（预付 100%）' + TAG}}],
    'SB-312': [{'add_kp': {'name': 'Emanuel Fryszer', 'email': 'efryszer@fibercomtelecoms.com', 'role': 'Contact Person / 负责人（Foxcom 全球经销名录 2026-10-29）= 收件人 — 一页纸一次：分销 20% B、STC-228GP / STC-2224GP / STC-110XGE 一口价 + MOQ 1 + 付费样机；跳线 / SFP 不做明说 ' + PH + TAG}},
               {'facts': {'legal_name': 'Fibercom Telecom Phils., Inc.（官网页脚；SEC 号 1 查未得）', 'founded': '约 1998（自述「27 Years」）' + TAG, 'hq': '2006-A West Tower, PSE Centre (Tektite Towers), Exchange Road, Ortigas Center, Pasig City 1605（+63 995 581 4199）' + TAG, 'size': '小型' + TAG,
                          'other': '第 120 批：光纤 / 电信产品分销 + turnkey；Foxcom 经销名录给出具名负责人；部分坐实（官网地址 + 名录 KP；SEC 未取）' + TAG}}],
    'SB-314': [{'add_kp': {'name': 'Juner D. Yaneza', 'email': 'vericom@rspotsolutions.com', 'role': '经销联络负责人（Vericom 菲律宾经销页 2026-10-29）= 收件人 — 一页纸一次：分销 20% B、STC-028GP / STC-2216GP / STC-2224GP + STI-154GP 一口价 + MOQ 1 + 付费样机 ' + PH + TAG}},
               {'facts': {'legal_name': 'RSPOT Solutions, Inc.（官网；SEC 号 1 查未得）', 'hq': 'Unit 7B-19 Bldg. 7, Residencias de Manila, Pandacan, Manila（+63 2 8293-9507；VisMin 088 326-0093）' + TAG, 'size': '小型' + TAG,
                          'other': '第 120 批：ICT / 布线 / CCTV 增值分销商（Vericom 经销）；部分坐实（官网地址 + 经销页 KP；SEC 未取）' + TAG}}],
    'SB-412': {'facts': {'legal_name': '未取（InterConnectivity Computer Solutions；无邮箱 / 域名 → 0 查）', 'other': '第 120 批：0 查；需求百兆单纤 MC（不供）+ 无邮箱 → **不动（B 保留）** ' + PH + TAG}},
    'SB-735': {'facts': {'legal_name': '未取（WhatsApp 联系人 Steve +63 917；无公司 / 邮箱 → 0 查）', 'other': '第 120 批：0 查；个人 + 4×0 → **不动（B 保留）** ' + PH + TAG}},
    'SB-979': [{'kp_match': 'acatangui', 'name': 'Alberto A. Catangui', 'role': 'CEO / Chairperson（D&B + verif + RocketReach 2026-10-29）= 收件人 — 一页纸一次：集成商 25% B、TP-Link 在用 → STC-028GP / STC-2224GP / STC-4424GCPM + STI-154GP 一口价 + MOQ 1 + 付费样机 ' + PH + TAG},
               {'add_kp': {'name': 'Charles Catangui', 'role': 'VP Operations（RocketReach 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'iOne Resources, Inc.（SEC 号 1 查未得）', 'founded': '2002（RocketReach 口径）' + TAG, 'hq': 'Unit 1006 The Centerpoint Condominium, Julia Vargas Avenue cor. Garnet Road, Ortigas Center, Pasig City 1605, Philippines' + TAG, 'size': '小型（约 45 人）' + TAG,
                          'other': '第 120 批：托管 ICT / 现场部署 / 网络安全服务（6202 计算机咨询）；部分坐实（企业库地址 + 成立年 + KP 职务；SEC 未取）' + TAG}}],
    # ---------------- ZA 10 ----------------
    'SB-042': [{'kp_match': 'enquiries@', 'role': '联系人（研究档）— 一页纸一次（Attn: Network Product Manager）：分销 20%（对价在售 PLANET GS-4210-8P2S → STC-228GP / STI-154GP）↔ 贴标 OEM 30%（Securi-Prod 网络线）双轨 B；2025-10 报价为开场 ' + ZA + TAG},
               {'facts': {'legal_name': 'Regal Security Distributors SA (Pty) Ltd（CIPC 注册号 1 查未得）', 'founded': '1981（1998 现东家收购）' + TAG, 'hq': '26 Greenstone Place, Greenstone Hill, Edenvale, Gauteng（+27 11 553 3300；旧址 9 Electron Ave, Linbro Business Park）' + TAG, 'size': '中型（201–500；24–30 分支）' + TAG,
                          'other': '第 120 批：南非最大多品牌安防分销之一 + 自有标；部分坐实（行业名录地址 + 电话 + 成立年；CIPC 未取）' + TAG}}],
    'SB-1117': [{'kp_match': 'kevin@', 'role': 'Account Manager（销售侧，非采购；研究档）— 一页纸一次收件 sales@ Attn: Procurement / Product Manager、抄 Kevin：分销 20% B、渠道 / 贴标角度 STC-2224GP / STC-4424GCPM / STI-154GP 一口价 + MOQ 1 + 付费样机 ' + ZA + TAG},
                {'facts': {'legal_name': 'Switchcom Distribution (Pty) Ltd（注册号 2015/334722/07，官网 T&C 自列）', 'founded': '2015' + TAG, 'hq': '49 Galaxy Avenue, Linbro Business Park, Sandton 2090, Gauteng（另址 Randview Business Park, 1 Avon Rd, Ferndale, Randburg 2194）' + TAG, 'size': '中小型' + TAG,
                           'other': '第 120 批：多品牌 ICT 分销（Cambium / Hikvision / MikroTik / Ubiquiti）；坐实（注册号 + 注册地址）' + TAG}}],
    'SB-443': [{'kp_match': 'adejumokojo', 'role': '业主（网络承包商）= 收件人 — 一页纸一次：集成商 25% B、4 光 8 电工业 PoE → STI-488DGGPM 一口价 + 付费样机；DAC 不供明说 ' + ZA + TAG},
               {'facts': {'legal_name': '未取（Spring Network；gmail + 无域名 → 0 查）', 'other': '第 120 批：0 查；口型明确 + 曾回复 → 一页纸一次（预付 100%）' + TAG}}],
    'SB-516': [{'kp_match': 'deon@', 'name': 'Deon van Zyl', 'role': 'Managing Director / Founder（prospeo + Crunchbase 2026-10-29）— 不动：消防探测 / 气体灭火 OEM（Hudaco 集团成员），非目标行业 + WA 7×0 ' + ZA + TAG},
               {'facts': {'legal_name': 'Brigit Fire / Brigit Systems（Hudaco Group 成员；CIPC 注册号 1 查未得）', 'founded': '2006（prospeo）' + TAG, 'hq': '10 Ridge Road, Laser Park, Honeydew, Gauteng 2041（+27 11 794 2217）' + TAG, 'size': '小型（21–50）' + TAG,
                          'other': '第 120 批：消防系统 OEM（BSI Kitemark）；非目标行业 + 无具体需求 → **不动（B 保留）**；部分坐实（企业库地址 + 成立年 + KP 职务）' + TAG}}],
    'SB-615': {'facts': {'legal_name': 'Hands On Security (Pty) Ltd（D&B；CIPC 注册号 1 查未得）', 'hq': '17 Pierneef Blvd, Shop 7, Meyerton, Gauteng 1961（另址 Unit 4, 49 Galloway St, Meyerton）' + TAG, 'size': '微型 / 小型' + TAG,
                         'other': '第 120 批：业主亲自勘察的本地 CCTV / 报警安装商（在售 UTEPO 口型）→ **集成商 25% B，一页纸一次（Attn: Owner；STC-028GP / STC-2216GP + STI-054GP；UTEPO 不点名）** ' + ZA + '；部分坐实（D&B 地址）' + TAG}},
    'SB-636': [{'kp_match': 'procurement@', 'role': 'Sales Engineer（研究档）— 不动：1 查唯一命中 = DFFE 打印耗材投标名单（政府投标杂货供应商）+ 官网占位 + 7×0 ' + ZA + TAG},
               {'facts': {'legal_name': 'Marzetek (Pty) Ltd（仅 DFFE RFQ 000908 (24/25) 投标收到名单第 50 位证实存在；地址 / 注册号未得）', 'other': '第 120 批：未坐实；政府投标杂货供应商 → **不动（B 保留）**' + TAG}}],
    'SB-672': [{'kp_match': 'inus@', 'role': 'Electrical Engineer and Chief Executive Officer（研究档）= 收件人 — 一页纸一次：贴标 OEM 30% B、自有品牌交换机 / MC 制造商 → STI-154GP / STI-288DGGPM + STC-110XGE 中性包装 / 贴标 + MOQ 1 + 付费样机；SFP 不供明说 ' + ZA + TAG},
               {'add_kp': {'name': 'Marien Dreckmeyr', 'role': 'Director, National Marketing（ZoomInfo 2026-10-29；2009– ；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Netshield (Pty) Ltd（CIPC 注册号 1 查未得）', 'founded': '1994（RocketReach）' + TAG, 'hq': '10 Pony Street, Concept House, Unit B, Silver Lakes, Pretoria, Gauteng（旧址 407 Atterbury Road, Menlo Park；(012) 424-9340）' + TAG, 'size': '小型（约 16 人）' + TAG,
                          'other': '第 120 批：自研 IoT / UPS / 交换机 / MC 自有品牌制造商；部分坐实（企业库地址 + 成立年 + 人数 + 职务；CIPC 未取）' + TAG}}],
    'SB-860': {'facts': {'legal_name': 'Basithami Trading and Projects t/a Basithami Technology（官网自述；CIPC 注册号 1 查未得）', 'founded': '约 2000（自述 20 年）' + TAG, 'hq': '10313 c/o Pudi & Tshepe Street, Kagiso Ext 4, Mogale City, Gauteng（+27 11 419 3110）' + TAG, 'size': '微型' + TAG,
                         'other': '第 120 批：微型安防安装 / 电子维修 + 15×0 + 无具名 KP → **不动（B 保留）** ' + ZA + '；部分坐实（官网地址 + 电话）' + TAG}},
    'SB-904': [{'kp_match': 'accounts@', 'role': 'Accounts（研究档；收件 Attn: Abrie Joubert, CEO）— 一页纸一次：集成商 25% B、自建站询盘「7 台工业 8 电口轻管理」→ STI-288GPM ×7 一口价 + STI-280GE 备选 + 付费样机；Moxa 不点名 ' + ZA + TAG},
               {'add_kp': {'name': 'Abrie Joubert', 'role': 'Chief Executive Officer（ZoomInfo 2026-10-29；无公开邮箱）' + TAG}},
               {'facts': {'legal_name': 'Nuthill Technologies（(Pty) Ltd 推定；CIPC 注册号 1 查未得）', 'hq': '31 Boncker St, Middelburg, Mpumalanga（+27 13 246 1140；另址 Stoffberg Road R555）' + TAG, 'size': '小型（11–50）' + TAG,
                          'other': '第 120 批：矿业 / 冶金 / 电气 / 仪表自动化集成（NutProM / DepthMaster / WAGO；客户 Glencore / South32 / Eskom）；部分坐实（企业库地址 + 电话 + CEO；CIPC 未取）' + TAG}}],
    'SB-978': [{'kp_match': 'jacqueline@', 'role': 'Network Product Manager（研究档）= 收件人 — 一页纸一次：分销 20% B、直接对价在售 PLANET 工业 4 / 5 口 → STI-054GP / STI-154GP + STC-110XGE + STI-280GE 一口价 + MOQ 1 + 付费样机 ' + ZA + TAG},
               {'facts': {'legal_name': 'Eurobyte Technology (Pty) Ltd（D&B；CIPC 注册号 1 查未得）', 'hq': 'Unit 8 Cambridge Commercial Park, 22 Witkoppen Rd, Bryanston / Paulshof, Gauteng 2056（011 234 0142）' + TAG, 'size': '小型' + TAG,
                          'other': '第 120 批：ICT / CCTV / 网络硬件分销（PLANET / Ruijie / Huawei / Uniview）；部分坐实（D&B 地址 + 电话；CIPC 未取；名录 2013 在册）' + TAG}}],
    # ---------------- ID 10 ----------------
    'SB-050': [{'add_kp': {'name': 'Gunawan', 'email': 'gunawan@pt-aag.co.id', 'role': '联系人（Clients 表 / entities 邮箱；职务待核）= 收件人 — 回访一页纸一次：集成商 25% B、2011 成交（延长器 12 台）为开场 → 延长器不供 → STC-028GP / STC-228GP / STI-054GP 一口价 + MOQ 1 + 付费样机 ' + ID + TAG}},
               {'facts': {'legal_name': 'PT Anugerah Artha Guna（pt-aag.co.id 官网；NIB / NPWP 1 查未得）', 'hq': 'Sawangan Permai, Jalan Anggrek Blok B5 no.2, RT.03 RW.09, Depok 16519（另址 Jalan MPR 1, Jakarta Selatan 12430；+62 851-8282-8360）' + TAG, 'size': '小型' + TAG,
                          'other': '第 120 批：IT / 应用 / 网络顾问与集成；法定名解出；部分坐实（官网地址 + 电话；NIB 未取）' + TAG}}],
    'SB-1100': [{'kp_match': 'kosovaku', 'role': '负责人（领英来源；研究档）= 收件人 — 一页纸一次：集成商 25% B、2023 主动问购买渠道 → 直购 + bypass 不供明说 → STI-288DGGPM / STI-154GP 一口价 + 付费样机 ' + ID + TAG},
                {'facts': {'legal_name': '未取（IT Broadcast & Cyber Security Infra System；gmail + 无域名 → 0 查）', 'other': '第 120 批：0 查；主动问渠道 → 一页纸一次（预付 100%）' + TAG}}],
    'SB-115': [{'kp_match': 'rizkyadips', 'role': '联系人（研究档）= 收件人 — 一页纸一次：集成商 25% B、设备自用 DIN 5 口 PoE → STI-054GP 一口价 + STI-154GP 备选 + 付费样机（设备随机配套 → 小量复购） ' + ID + TAG},
               {'facts': {'legal_name': 'PT. Catur Citra Wisesa（AHU 登记号 182592，companieshouse.id 镜像；Active）', 'founded': '未取（自述 20+ 年）' + TAG, 'hq': 'Jl. Taman Harapan Baru Blok D 10/11, RT.003/022, Pejuang, Bekasi（业务地 Gambir, Jakarta）' + TAG, 'size': '小型' + TAG,
                          'other': '第 120 批：制药 / 化妆品 / 食品饮料生产机械与备件制造（非网络行业，但 DIN 交换机为设备配套）；坐实（登记号 + 注册地址 + 领英业务）' + TAG}}],
    'SB-142': [{'kp_match': 'airpowireless', 'role': '联系人（研究档）= 收件人 — 一页纸一次：贴标 OEM 30% B、自有品牌 Airpo（PoE 交换机 / AP 自标 + 经销网络）→ STC-228GP 贴标 / STC-4424GCPM / STC-2224GP + MOQ + 付费样机；工业线不推 ' + ID + TAG},
               {'facts': {'legal_name': '未取（Airpo Wireless 品牌方；airpo.co.id 产品页 + hsairpo.co.id 经销名单在，法人 / 地址 1 查未得）', 'size': '小型' + TAG,
                          'other': '第 120 批：自有品牌（SG1210FP 8 PoE + 2 SFP、W312 AP）+ 经销商 LANGITNET / PT Ilufa Abadi Indonesia / Aratech；未坐实（法人未得）' + TAG}}],
    'SB-179': {'facts': {'legal_name': '未取（「CRISPY CREPES」疑为微信名；yahoo → 0 查）', 'other': '第 120 批：0 查；主体不明 + 现用锐捷 → **不动（B 保留；微信只问一句公司 / 网站）** ' + ID + TAG}},
    'SB-203': [{'kp_match': 'dedi.suryonugroho', 'role': 'Mr.（表内；WA 已加）= 收件人 — 一页纸一次：集成商 25% B、2024-04 明确需求 4 光 16 电 L2 管理工业 → STI-244DGGPM / STI-288DGGPM 一口价 + 付费样机；WA 同步 ' + ID + TAG},
               {'facts': {'legal_name': 'PT. Suryatama（1 查仅同名异业：PT. Suryatama Mitra Sejati 1431499 泗水 2023 / PT. Suryatama Indo Semesta 坦格朗编织袋 → 均未对齐）', 'other': '第 120 批：未坐实（同名异业）；需求明确 + 曾回复 → 一页纸一次（预付 100%）' + TAG}}],
    'SB-382': {'facts': {'legal_name': '未取（Yusuf；gmail + 无公司名 → 0 查）', 'other': '第 120 批：0 查；无公司 + 无回声 → **不动（B 保留）** ' + ID + TAG}},
    'SB-414': {'facts': {'legal_name': '未取（Rolins +62 852；无邮箱 / 公司 → 0 查）', 'other': '第 120 批：0 查；需求全 SFP 12–24 口汇聚机（无对口商用款）→ **不动（B 保留）** ' + ID + TAG}},
    'SB-456': {'facts': {'legal_name': 'PT Panca Kumala Jaya（官网；NIB / NPWP 1 查未得）', 'founded': '≤ 2011（旧站 © 2011）' + TAG, 'hq': 'Ruko Golden Green No.8, Jl. Panjang (Arteri Kedoya), Jakarta Barat 11520（021-564 3366；旧址 Rukan Golden Green No.6）' + TAG, 'size': '小型' + TAG,
                         'other': '第 120 批：SMATV / IPTV + 安防门禁 + 3play 分销、DCN 交换机印尼渠道（含工业 DIN 品类页）→ **分销 20% B，一页纸一次（Attn: Purchasing / Product Manager；DCN 之下白牌 / 低价 STC-2224GP / STC-4424GCPM + STI-154GP / STI-288DGGPM；DCN 不点名）** ' + ID + '；部分坐实（官网地址 + 电话 + 起始年）' + TAG}},
    'SB-610': {'facts': {'legal_name': '未取（Ahmad Ariyanto；gmail + 无公司名 → 0 查）', 'other': '第 120 批：0 查；只要价表 + 无回声 → **不动（B 保留）** ' + ID + TAG}},
    # ---------------- BR 6 ----------------
    'SB-1089': [{'kp_match': 'sanche@', 'role': '联系人（研究档）= 收件人 — 一页纸一次：分销 20% B、面向 ISP 的分销 / 电商 → STC-2224GP / STC-4424GCPM / STC-110XGE 一口价 + MOQ 1 + 付费样机；葡语备注 ' + BR + TAG},
                {'facts': {'legal_name': 'tpnet.com.br（1 查三家同名未对齐：Timmers Tecnologia Ltda t/a Tpnet Tecnologia CNPJ 54.793.965/0001-08（2024-04-18 开业，里约 Barra da Tijuca，CNAE 8020-0/01）/ TPNET Informática Ltda-ME 31.258.395/0001-50（1986，SUSPENSA）/ Tp Net 16.679.928/0001-84）', 'hq': '未取（Rio de Janeiro, RJ；表内 +55 21）' + TAG, 'size': '小型' + TAG,
                           'other': '第 120 批：未坐实（同名多家；若为 Timmers → 2024 新壳红旗）；一页纸一次（预付 100%）' + TAG}}],
    'SB-1090': [{'kp_match': 'fabio@', 'role': '联系人（研究档；归属存疑 — 域名实体为新闻社）— 不动：误归属 ' + BR + TAG},
                {'facts': {'legal_name': 'Tramaweb Agência de Notícias Ltda - ME（域名实体；CNPJ 14.254.716/0001-20；ATIVA）', 'founded': '2011-08-15' + TAG, 'hq': 'Rua Cubatão 86, Conj 1007, Vila Mariana, São Paulo - SP 04013-000（(11) 3388-3063；marcos@tramaweb.com.br）' + TAG, 'size': '微型（ME；资本 R$10k）' + TAG,
                           'other': '第 120 批：域名实体 = 新闻 / 公关公司（CNAE 6391-7/00），与表内「MC FS 自有 logo」业务不符 → **误归属，不动（B 保留；Simon 若有 WA 只问一句公司 / 网站，答后重建档）**；坐实（CNPJ + 地址，业务不符）' + TAG}}],
    'SB-1137': [{'kp_match': 'transivideo', 'role': '联系人（研究档；2024-06 / 2024-11 两次主动要价）= 收件人 — 一页纸一次：分销 20% B、以 2024-06 报价为开场再报 STC-028GP / STC-2216GP / STC-2224GP 现价 + STI-280GE 工业非管理 + MOQ 1；葡语备注；回信 → 升 A 候选 ' + BR + TAG},
                {'add_kp': {'name': 'Ema Ines Rodriguez Rodriguez', 'email': 'admin@infotecsistemas.com.br', 'role': 'Sócia-Administradora（casadosdados 2026-10-29；2009-08-13 入股；登记邮箱）' + TAG}},
                {'facts': {'legal_name': 'Infotec Comércio de Equipamentos e Sistemas de Segurança Ltda - ME（CNPJ 05.590.805/0001-56；分支 0002-37 Florianópolis；ATIVA；Simples 2009 起）', 'founded': '2003-03-26（分支 2010-06-04）' + TAG, 'hq': 'São José - SC（分支 Florianópolis - SC；(48) 4052-9066）' + TAG, 'size': '微型 / 小型（ME）' + TAG,
                           'other': '第 120 批：安防设备商贸 + TRF4 多起进口税 / PIS-Cofins 进口诉讼（2015–2018）→ 直接进口商；坐实（CNPJ + 法人 + 开业日 + 进口记录）' + TAG}}],
    'SB-498': [{'kp_match': 'oscar', 'role': '技术负责人（研究档）= 收件人 — 一页纸一次：贴标 OEM 30% B、注入器不供明说 → STC-028GP / STC-228GP 贴标 + 批量阶梯 + MOQ + 付费样机 ' + BR + TAG},
               {'facts': {'legal_name': 'DTI Tecnologia Ltda - EPP（Daiken；CNPJ 10.497.398/0001-77；ATIVA）', 'founded': '2008-11-12' + TAG, 'hq': 'Colombo - PR（库里蒂巴都会区）, Brazil' + TAG, 'size': '小型（EPP）' + TAG,
                          'other': '第 120 批：CNAE 电子元器件制造 → 自有品牌电子制造商（500 pcs injector 询盘量级）；坐实（CNPJ + 开业日 + CNAE）' + TAG}}],
    'SB-512': [{'kp_match': 'eduardo@', 'role': '联系人（研究档）= 收件人 — 一页纸一次：集成商 25% B、2 光 6 PoE → STC-228GP 一口价 + STC-2216GP 备选 + 付费样机；葡语备注 ' + BR + TAG},
               {'facts': {'legal_name': 'Solus Tecnologia em Sistemas Ltda EPP（CNPJ 07.270.661/0001-86）', 'founded': '2005-03-08（自述 2000 起）' + TAG, 'hq': 'Rodovia Demócrito Moreira 176, Fátima, Aracruz - ES 29192-243（(27) 3256-3002）' + TAG, 'size': '小型（EPP）' + TAG,
                          'other': '第 120 批：电子安防 / CCTV / 门禁 / 布线集成（CNAE 安防服务）；坐实（CNPJ + 地址 + 开业日 + 电话）' + TAG}}],
    'SB-591': [{'kp_match': 'carlos@', 'role': '联系人（研究档）= 收件人 — 一页纸一次：集成商 25% B、ITS 路侧机柜 → 90 W 注入器不供明说 → STI-154GP / STI-288DGGPM / STI-488DGGPM 一口价 + 付费样机；葡语备注 ' + BR + TAG},
               {'facts': {'legal_name': 'Elementu Engenharia e Integração Ltda（CNPJ 14.458.461/0001-17；ATIVA；Sociedade Empresária Limitada）', 'founded': '2011-09-26' + TAG, 'hq': 'Rua Pedro José Laroca 1667, Jardim Santa Marta, Araraquara - SP 14808-300（nfe@elementuengenharia.com.br）' + TAG, 'size': '小型' + TAG,
                          'other': '第 120 批：道路基础设施 / ITS 工程集成（HS-WIM、龙门架、可变情报板；CNAE 7112-0/00）；坐实（CNPJ + 地址 + 开业日 + CNAE）' + TAG}}],
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
