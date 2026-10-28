#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 117 批（T29-U110，公司底数第三十五轮 · 新加坡 B 池收尾 7 户 + 泰国 B 池 19 户 + 阿联酋 B 池前 14 户 = 40 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 事实 补写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=117 行）。
结构同 batch116_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：升 A 候选 · 一页纸一次 6（SB-059 Avanca 200207710N 24 年工业通信分销 GM/MD 回过 info 分销 20% / SB-361 Lucky Joint 198200882E 1982 电信承包商 实缴 S$2M 问 250 m 集成商 25% / SB-885 Riverplus 0125548003398 21 年进口分销 权益 ฿141.8M 采购经理 KP 分销 20% / SB-878 Magnus Infotech Trading LLC 迪拜 VAD 总经理 KP 分销 20% / SB-495 Topnet Distribution FZCO DAFZA 工业连接分销 总经理 KP 分销 20% / SB-298 VNS Technologies LLC 阿布扎比 4 国 VAD 执行董事问 L2/L3 分销 20%）；
一页纸一次 · 分销 20% 6（SB-133 Gigalight 布线分销 Director 要过海报 / SB-515 3Tel 201325873K 在供 Utepo 联合创始人 KP / SB-023 ITK 0205557021718 网店卖 ONV 工业线 / SB-609 Ablelink 0105561132341（+ SB-614 Focomm 并线）双牌照小分销 / SB-612 Cloud IT Network 0125554018059 VoIP 配套 PoE / SB-995 ACIX ME 安防渠道 VAD 销售总监 KP）；
一页纸一次 · 集成商 25% 7（SB-552 Securevision 200614644E 持牌安防 SI HRUI 在供 Q-33 口径 / SB-267 Bio-Cognitive 200807513Z 问过 16 口 年报停 2012 预付 / SB-663 HSTN 0105552017802 酒店网络 SI / SB-034 TJ Computer 店主回过 Interested / SB-510 Pongpanot 个人项目买家 工业 2+4 / 2+8 / SB-325 Hamed Electronics LLC Lootah 集团弱电 SI / SB-043 Euro Technology 41 次里回 4 次要资料 守界）；
一页纸一次 · 贴标 OEM 30% 2（SB-919 Bismon 0105546131011 ฿20M 自有品牌 CEO KP / SB-918 Alston Systems Inc. JLT 自有品牌有源产品）；
不动 18（SB-567 TGM Global 电力监测 要机架 / SB-381 Accesso Franco 0105558125585 登记汽配 ฿1M MaiWe 在供 / SB-407 Winner Intertech Moxa 官方经销 国防展 未坐实 / SB-505 ESO Tech 0205566032166 2023 新设 传感器 PLC / SB-458 SATS Digital 2025 新设 ฿1M 比价网店 / SB-813 Focus System 0205549023031 芭提雅 CCTV 店 hotmail / SB-882 P.C. Telecom 0105539072803 31×0 / SB-200 Sysnet Center 0133552003338 有限合伙 ฿500k 多品牌店 / SB-955 OMC Tech 光端机 产品不对位 / SB-1081 域名失效 gmail / SB-603 Wirote 个人 14×0 / SB-421 Distribolutions FZE 需求光模块 / SB-400 Safa Networks FZE-LLC 身份空泛 / SB-926 Osool RAK 23×0 / SB-928 Seven Stars 汽车集团 / SB-935 Al Shuaib Control Equipment LLC HDMI 延长器 22×0 / SB-581 Sheildify LLC 2020 网店 / SB-136 Metalog DMCC 油气贸易）；
并线 1（SB-614 Focomm (Thailand) 0105559051071 = Ablelink 同址同构 → SB-609）；
坐实 16（SB-515 / 552 / 059 / 267 / 361 / 663 / 919 / 023 / 505 / 885 / 614 / 813 / 882 / 200 / 609 / 612）/ 部分坐实 19（SB-133 / 567 / 381 / 458 / 955 / 918 / 995 / 421 / 325 / 878 / 400 / 495 / 926 / 928 / 935 / 581 / 298 / 043 / 136）/ 未坐实 1（SB-407）/ 0 查 4（SB-1081 / 034 / 510 / 603）；
KP 坐实 = 老板 / 总经理本人 7（SB-133 Jimmy Wee Director / SB-515 Elvin Tan Co-founder / SB-059 Steven Fu GM & MD（LinkedIn 2024-01 起）/ SB-919 Anek Thongdee CEO / SB-878 Saleem Shaikh MD / SB-495 Kandasamy Ganesan MD / SB-298 Abdul Gafoor Executive Director）；补代表 / 负责人 add_kp 3（SB-567 Chang Poo Geok Key Principal / SB-136 Jaideep Paul Director / SB-043 M. Maarouf 表内邮箱 收件人）；KP 更正 1（SB-928 Nibu Basheer「Director」→ ZoomInfo 汽配 Client Relations Associate，身份待核）；
法定名补全 / 更正 36；country_fix 0（SB-995 表内误记沙特，research 已 AE → 不动）。
TH 检索路径实测（首次，19 户 15 命中）：「英文名 + Co., Ltd. + Thailand + เลขทะเบียน OR dataforthai + 域名」1 查 → dataforthai.com/company/<13 位>（泰英法定名 + 登记号 + 注册日（佛历 − 543）+ 注册资本 + 股东国籍 / 人数 + 地址 + 网站 + 登记业务）/ data.creden.co（TSIC + 股东权益 + 财报年份 + 旧登记号）；官网页脚 Tax ID（hstn / sysnetcenter 自列登记号 + NBTC 许可）亦可；登记业务 ≠ 站内业务（Accesso Franco 汽配 / OMC Tech 电气材料）→ 部分坐实 + 标记；通名（Winner Intertech）命中同名 → 未坐实；同址同构 = 姊妹公司（Focomm / Ablelink）→ 并线。
AE 检索路径实测（首次，14 户 0 牌照号）：阿联酋无公开免费法人库；可得 = 官网 contact / footer 的法定后缀（LLC / FZE / FZCO / DMCC）+ P.O. Box + 地址，辅以 aiwa.ae / haiuae.com / atninfo.com / townin.com / yellowpages-uae / protenders 名录（法定名 + 成立年 + P.O. Box）→ 全部只能部分坐实 → 阿联酋一律预付 100%、DAP 迪拜 / 阿布扎比由买方清关。
旁线索（≠ 目标，另立户评估）：3TEL SOLAR & ENERGY PTE. LTD.（SB-515 姊妹）；WINNER TECH (THAILAND) 0105556021529 / WINNER INTERGREAT LP 0103557011622 / WE WINER INTERTRADE 0205560020883（SB-407 同名）；SATDIGITAL DOTCOM LP 0103557023531（SB-458 疑前身，已注销）；ESE (THAILAND) 0105556109876 / I.S.O. TECHNOLOGY 0105540068849（SB-505 同页）；P.L.C. TELECOM 0125545006795（SB-882 同名）；Mohammed Hamed Electronics Trading LLC Box 65146（SB-325 同名）；Topnet Distribution LLC Deira + Topnet Communications and IT 沙特（SB-495 集团）；Seven Stars Technology（SB-928 旁支）。
Simon 待决（累计见 PR-02-53 追记）：升 A 候选 SB-059 / 361 / 885 / 878 / 495 / 298（回信即升）；SB-552 Securevision 的 Q-33 口径（HRUI 在供 → 只推 Marvell 管理 / 工业线）仍待确认；SB-298 Gafoor 「会来深圳」→ 面谈时间 Simon 定。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 117 批 官方登记核实 2026-10-28）'
SG = '— 新加坡常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳、IMDA 不声称'
TH = '— 泰国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳、NBTC 不声称'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜（买方清关）、TDRA / ESMA 不声称'
UPD = {
    # ───────── SG 收尾 7 ─────────
    'SB-133': [{'kp_match': 'jw@gigalight.com.sg', 'role': 'Director（= 老板本人；要过海报产品信息）= 拍板人 / 收件人 — 一页纸一次：分销 20% B small、承包商渠道 PoE 阶梯 STC-028GP / 228GP / 2216GP / 2224GP + STC-4424GCPM、MOQ 1、付费样机、预付' + SG + TAG},
               {'facts': {'legal_name': 'Gigalight Pte. Ltd.（UEN 1 查未得；与深圳易飞扬 Gigalight 无关）', 'founded': '未取' + TAG, 'hq': '970 Toa Payoh North #02-04, Singapore 318992（+65 6353 3679）' + TAG, 'size': '小型；营收 <$5M（ZoomInfo 口径）' + TAG,
                          'other': '第 117 批：结构化布线 / 光纤配线分销商（Softing 区域分销、Schneider Actassi、Premium Line）→ **分销 20% B small，一页纸一次**；再无回声 → 不动；部分坐实（分销商页 + 企业库，UEN 未取）' + TAG}}],
    'SB-515': [{'kp_match': 'elvin.tan@3tel.com.sg', 'role': 'Co-founder & Director（3 名高管之一；UEN 201325873K）= 拍板人 / 收件人 — 一页纸一次（最后一次）：分销 20% B small、对位其 Utepo 页的 STC 阶梯 + STI-288DGGPM + STC-4424GCPM、付费样机' + SG + TAG},
               {'facts': {'legal_name': '3TEL INTERNATIONAL PTE. LTD.（UEN 201325873K；Local Company；Live；年报 2025-09-30）', 'founded': '2013-09-24' + TAG, 'hq': '15 Yishun Industrial Street 1 #01-17 Win 5, Singapore 768091（+65 6583 1334）' + TAG, 'size': '小型（3 名高管 / 股东；营收 <$5M）' + TAG,
                          'other': '第 117 批：SSIC 61012 电信 / 光纤 turnkey + 43210 电气工程；安防 + 网络供应与工程，站内 Utepo PoE 在供 → **分销 20% B small，一页纸一次（最后一次）**；15×0 在先 → 再无回声即不动；坐实' + TAG}}],
    'SB-552': [{'kp_match': 'ler@securevision.com.sg', 'role': '研究档 KP（PLRD 持牌安防集成商；UEN 200614644E）= 收件人 — 一页纸一次：集成商 25% B、Q-33 口径只推 Marvell 管理 PoE STC-4424GCPM + STC-110XGE + 工业 STI、不碰其 HRUI 非管理同款、付费样机' + SG + TAG},
               {'kp_name': 'Abdul Hameed', 'role': 'Technical Specialist = 抄送' + TAG},
               {'facts': {'legal_name': 'SECUREVISION PTE. LTD.（UEN 200614644E；Live；PLRD 保安承包商牌照 + bizSAFE Level 3 + BCA 注册）', 'founded': '2006-10-03' + TAG, 'hq': '新加坡（recordowl 未展示详址）' + TAG, 'size': '中小（2,000+ 新加坡安装点）' + TAG,
                          'other': '第 117 批：20 年持牌安防 SI（CCTV / 门禁 / 报警 / LPR / 数据中心门禁）、HRUI 在供、Simon「可以多跟进」→ **集成商 25% B，一页纸一次（Q-33 口径）**；回信 → 加厚；坐实（UEN + 注册日 + 牌照）' + TAG}}],
    'SB-059': [{'kp_match': 'steven@avanca.com.sg', 'role': 'General Manager & Managing Director（LinkedIn：2024-01 起 GM & MD，2015 入职；2025-11 对 10G MC 群发回 info）= 拍板人 / 收件人 — 一页纸一次：分销 20% B（升 A 候选）、宽温 STI-154GP / 288DGGPM / 488DGGPM / 0240GE + STC-110XGE 一口价、3 年保、付费样机' + SG + TAG},
               {'facts': {'legal_name': 'AVANCA TECHNOLOGIES PTE. LTD.（UEN 200207710N；Private Company Limited By Shares；Live；.SG 域名注册人）', 'founded': '2002-09-06' + TAG, 'hq': '23 New Industrial Road #07-06/07 Solstice Business Center, Singapore 536209（+65 6242 5108）' + TAG, 'size': '小型（24 年工业通信分销）' + TAG,
                          'other': '第 117 批：工业 4G/5G 路由 / 工业交换机 / PoE / MC（Red Lion N-Tron 在供）/ 带外管理 分销商，总经理本人回过 info → **分销 20% B（升 A 候选），一页纸一次**；回信 → 加厚 + 升 A；坐实' + TAG}}],
    'SB-267': [{'kp_match': 'amyhoi@bio-cognitive.com', 'role': '名录登记联系人（manufacturerss：Contact Person Ms. Amy Hoi；2025-07 问过 16 电口具体型号）= 收件人 — 一页纸一次：集成商 25% B small、直接答 16 电口 = STC-2216GP（+ STC-2224GP 带 SFP）、MOQ 1、付费样机、预付 100%' + SG + TAG},
               {'facts': {'legal_name': 'BIO-COGNITIVE SOLUTIONS PTE. LTD.（UEN 200807513Z；Exempt Private Company Limited By Shares；Live；recordowl 最近年报 2012-04-27）', 'founded': '2008-04-17' + TAG, 'hq': '5 Ang Mo Kio Industrial Park 2A #05-30 AMK Tech II, Singapore 567760（旧址 67 Ubi Crescent #04-11）' + TAG, 'size': '小型（自称 200+ 安装点）' + TAG,
                          'other': '第 117 批：生物识别门禁 / CCTV 集成 + IT/OT 安全；年报记录停于 2012 → 只做预付；Simon「可以多跟进」→ **集成商 25% B small，一页纸一次（预付）**；再无回声 → 不动；坐实（年报停滞待核）' + TAG}}],
    'SB-361': [{'kp_match': 'robin@luckyjoint.com.sg', 'role': 'Senior Manager, Network Engineering（研究档；问过「PoE 能传 250 m 吗」）= 收件人 — 一页纸一次：集成商 25% B（升 A 候选）、答 250 m = STC-028GP / 228GP 延长模式 250 m（10 Mbps）+ 标准 100 m 千兆 + 项目量 STC-4424GCPM、付费样机' + SG + TAG},
               {'kp_match': 'sales@luckyjoint.com.sg', 'role': '研究档联系人（Kee Ching Hai）= 抄送' + TAG},
               {'facts': {'legal_name': 'LUCKY JOINT CONSTRUCTION PTE. LTD.（UEN 198200882E；Exempt Private Company Limited By Shares；Live；实缴 S$2,000,000；bizSAFE Star 至 2028-01-20）', 'founded': '1982-03-08' + TAG, 'hq': '17 Tuas Avenue 3, Singapore 639414' + TAG, 'size': '中型（251–500 人，Crunchbase 口径）' + TAG,
                          'other': '第 117 批：SSIC 42202 通信 / 电力线路建设 + 43909 网络基础设施 / FTTx；44 年电信网络承包商；Simon「可以多跟进」→ **集成商 25% B（升 A 候选），一页纸一次**；回信 → 加厚 + 升 A；坐实' + TAG}}],
    'SB-567': [{'add_kp': {'name': 'Chang Poo Geok', 'email': '', 'role': 'Key Principal（D&B）— 不动，不发' + TAG, 'source': 'dnb.com TGM GLOBAL PTE. LTD.'}},
               {'facts': {'legal_name': 'TGM Global Pte. Ltd.（UEN 1 查未得）', 'founded': '2011' + TAG, 'hq': '50 Ubi Crescent #01-04, Singapore 408568（+65 6848 2146；旧址 10 Ubi Crescent #06-92）' + TAG, 'size': '小型（10–50 人）' + TAG,
                          'other': '第 117 批：电力资产状态监测（局放 / DTS / SF6）+ 数据中心能效方案商，客户 油气 / 发电 / 输电（守界边缘），唯一需求 16 槽收发器机架（Saga 无）→ **不动（B 保留）**；部分坐实（企业库）' + TAG}}],
    # ───────── TH 19 ─────────
    'SB-663': {'facts': {'legal_name': 'บริษัท ไฮ โซลูชั่น อ๊อฟ เทคโนโลยี เน็ตเวิร์ค จำกัด HIGH SOLUTION OF TECHNOLOGY NETWORK CO., LTD.（HSTN；เลขทะเบียน 0105552017802；注册资本 ฿5,140,000；9 名泰籍股东）', 'founded': '2009-02-20' + TAG, 'hq': '17/14 Moo 6, Phutthamonthon Sai 5 Rd., Bang Krathuek, Sam Phran, Nakhon Pathom 73210（02-889-4701）' + TAG, 'size': '小型' + TAG,
                         'other': '第 117 批：酒店 / 医院 IPTV / SMATV / FTTx / CCTV 集成商（在用 Cisco 智能交换机）、无具名 KP → **集成商 25% B small，一页纸一次**（收 info@，抄 rungruengh@ / khomkits@）；再无回声 → 不动；坐实' + TAG}},
    'SB-919': [{'kp_match': 'sale@bismon.com', 'role': 'Chief Executive Officer（研究档；自有品牌 Bismon；เลขทะเบียน 0105546131011）= 拍板人 / 收件人（发 sale@，抬头 Attn: Mr. Anek Thongdee, CEO）— 一页纸一次（最后一次）：贴标 OEM 30% B、Bismon 标 / 自编货号 / 中性包装 STC 阶梯 + STI-154GP / 288DGGPM、MC 只有 STC-110XGE、付费样机' + TH + TAG},
               {'facts': {'legal_name': 'บริษัท บิสม่อน จำกัด BISMON COMPANY LIMITED（เลขทะเบียน 0105546131011；注册资本 ฿20,000,000；营业中）', 'founded': '2003-10-29' + TAG, 'hq': '298 Moo 1, O Ngoen, Sai Mai, Bangkok 10220' + TAG, 'size': '小型（23 年进口商）' + TAG,
                          'other': '第 117 批：登记业务 进口 / 销售计算机设备 + 网络布设；自有品牌 Bismon 与 Saga 产品线相似（= 外购贴牌）；Simon「可以尝试多跟进」→ **贴标 OEM 30% B，一页纸一次（最后一次）**；16×0 在先 → 再无回声即不动；坐实' + TAG}}],
    'SB-023': [{'kp_match': 'sales@itk.co.th', 'role': '公用销售箱（无具名 KP）= 收件人 — 一页纸一次：分销 20% B small、对位其网店 ONV 工业线的 STI 8 口 PoE + 2 SFP 档（STI-288GPM / STI-288DGGPM）、MOQ 1、付费样机' + TH + TAG},
               {'facts': {'legal_name': 'บริษัท ไอทีเค คอนเน็คติ้ง จำกัด ITK CONNECTING COMPANY LIMITED（เลขทะเบียน 0205557021718；注册资本 ฿5,000,000；股东权益 ฿10,035,499；2 名泰籍股东）', 'founded': '2014-06-25' + TAG, 'hq': '2/6 Rat Phatthana Rd., Rat Phatthana, Saphan Sung, Bangkok 10240（02-460-9200）' + TAG, 'size': '小型（权益 = 资本 2 倍）' + TAG,
                          'other': '第 117 批：IT 产品电商 + 安装商，网店在售深圳 ONV 工业交换机全线 → **分销 20% B small，一页纸一次**；再无回声 → 不动；坐实' + TAG}}],
    'SB-381': {'facts': {'legal_name': 'บริษัท แอ็คเซสโซ่ ฟรานโก้ จำกัด ACCESSO FRANCO COMPANY LIMITED（เลขทะเบียน 0105558125585；注册资本 ฿1,000,000；2 名泰籍股东；登记业务 = 汽车零配件零售 ≠ 站内能源智能方案）', 'founded': '2015-08-03' + TAG, 'hq': '23/2 Soi Punnawithi 29, Bang Chak, Phra Khanong, Bangkok 10260' + TAG, 'size': '微型' + TAG,
                         'other': '第 117 批：微型 + 登记业务与站内不符 + 已直接用国内 MaiWe 工业线 + 无 KP → **不动（B 保留）**；部分坐实（业务不符）' + TAG}},
    'SB-407': {'facts': {'legal_name': 'Winner Intertech Co., Ltd.（法人 1 查未得 → 未坐实；命中 WINNER TECH (THAILAND) 0105556021529 / WINNER INTERGREAT LP / WE WINER INTERTRADE 均 ≠）', 'founded': '未取' + TAG, 'hq': '未取（泰国）' + TAG, 'size': '未取' + TAG,
                         'other': '第 117 批：Moxa / Adder / Robustel 官方经销（原厂渠道）+ Defense & Security 展客户（守界）+ 6×0 + 未坐实 → **不动（B 保留）**' + TAG}},
    'SB-505': {'facts': {'legal_name': 'บริษัท อีเอสโอ เทค จำกัด ESO TECH CO., LTD.（เลขทะเบียน 0205566032166；注册资本 ฿5,000,000；2 名泰籍股东）', 'founded': '2023-06-07' + TAG, 'hq': '242/7 Moo 6, Thung Sukhla, Si Racha, Chonburi 20230' + TAG, 'size': '小型（2023 新设）' + TAG,
                         'other': '第 117 批：工业传感器 / PLC / SCADA 分销（WECON 代理），交换机只是入门配件，无 KP，7×0 → **不动（B 保留；来询工业 PoE 按分销 20% 预付）**；坐实' + TAG}},
    'SB-885': [{'kp_match': 'sales@riverplus.com', 'role': 'Purchasing Manager（研究档 Jiraporn Teeramasvanich；เลขทะเบียน 0125548003398）= 收件人 — 一页纸一次：分销 20% B（升 A 候选）、对位其工业 LAN 交换机线的 STI-154GP / 288DGGPM / 488DGGPM / 0240GE + CCTV PoE STC-2216GP / 2224GP、3 年保、付费样机、串口 / 路由不做' + TH + TAG},
               {'kp_match': 'prapapim@riverplus.com', 'role': 'System Engineer = 抄送' + TAG},
               {'facts': {'legal_name': 'บริษัท ริเวอร์พลัส จำกัด RIVERPLUS COMPANY LIMITED（เลขทะเบียน 0125548003398；旧号 0127354803391；注册资本 ฿5,000,000；股东权益 ฿141,848,531；6 名泰籍股东；财报 2564–2568 连续）', 'founded': '2005-03-14' + TAG, 'hq': '85/120-121 Moo 3, Bang Kruai-Sai Noi Rd., Bang Rak Phatthana, Bang Bua Thong, Nonthaburi 11110' + TAG, 'size': '中小（权益 ฿141.8M ≈ $4.2M）' + TAG,
                          'other': '第 117 批：TSIC 46521；2005 年起工业 4.0 / IoT 进口分销（工业 5G/4G 路由网关 + 交换机 + CCTV PoE 方案），采购经理为 KP → **分销 20% B（升 A 候选），一页纸一次**；回信 → 加厚 + 升 A；坐实' + TAG}}],
    'SB-458': {'facts': {'legal_name': 'SATS Digital（最接近法人 บริษัท แซทดิจิตอล จำกัด SATDIGITAL CO., LTD. เลขทะเบียน 0105568002761；注册资本 ฿1,000,000；网站未在登记页核到 → 部分坐实）', 'founded': '2025-01-06' + TAG, 'hq': '88/468 Kanlapaphruek Rd., Bang Khae, Bangkok 10160' + TAG, 'size': '微型（2025 新设）' + TAG,
                         'other': '第 117 批：2025 新设 ฿1M 比价网店 + 无 KP + 9×0 + 法人仅近似 → **不动（B 保留）**' + TAG}},
    'SB-614': {'facts': {'legal_name': 'บริษัท โฟคอมม์ (ประเทศไทย) จำกัด FOCOMM (THAILAND) COMPANY LIMITED（เลขทะเบียน 0105559051071；注册资本 ฿1,000,000；3 名泰籍股东；网站 focomm-cabling.com 登记页核到）', 'founded': '2016-03-24' + TAG, 'hq': '12 Soi Sukhaphiban 5 Soi 5 Yaek 3, Tha Raeng, Bang Khen, Bangkok（与 SB-609 Ablelink 同址）' + TAG, 'size': '微型' + TAG,
                         'other': '第 117 批：与 SB-609 Ablelink (Thailand) 同址同构 → **并线 → SB-609，本户不另发**；坐实' + TAG}},
    'SB-813': {'facts': {'legal_name': 'บริษัท โฟกัส ซิสเต็ม แอนด์ ดีไซน์ จำกัด FOCUS SYSTEM AND DESIGN COMPANY LIMITED（iFocus；เลขทะเบียน 0205549023031；注册资本 ฿3,000,000）', 'founded': '2006-08-24' + TAG, 'hq': '149/237 9th Fl., Moo 9, Chonburi（芭提雅；门牌后段未取）' + TAG, 'size': '小型' + TAG,
                         'other': '第 117 批：地方 CCTV 安装店（Hikvision / Dahua 经销点，原厂 PoE 随摄像机走）+ hotmail + 无 KP + 9×0 → **不动（B 保留）**；坐实' + TAG}},
    'SB-882': {'facts': {'legal_name': 'บริษัท พี.ซี. เทเลคอม จำกัด P.C. TELECOM CO., LTD.（เลขทะเบียน 0105539072803；注册资本 ฿10,000,000；网站登记页核到）', 'founded': '1996-07-01' + TAG, 'hq': '100/215 Soi Kanchanaphisek 005, Lak Song, Bang Khae, Bangkok 10160' + TAG, 'size': '小型' + TAG,
                         'other': '第 117 批：30 年 CCTV / PBX 布线安装商、已用深圳 Utepo，但 31×0 + 无 KP → **不动（B 保留；来询按集成商 25% 预付）**；坐实' + TAG}},
    'SB-200': {'facts': {'legal_name': 'ห้างหุ้นส่วนจำกัด ซิสเน็ต เซ็นเตอร์ SYSNET CENTER LIMITED PARTNERSHIP（เลขทะเบียน 0133552003338；有限合伙；注册资本 ฿500,000；NBTC 无线电设备经营许可 050356000200；财报 2564–2568 连续）', 'founded': '2009-07-21' + TAG, 'hq': '807/147 Moo 8, Khu Khot, Lam Luk Ka, Pathum Thani 12130（behind Zeer Rangsit；02-102-4284）' + TAG, 'size': '微型（有限合伙）' + TAG,
                         'other': '第 117 批：多品牌网店 + 安装（TP-Link / Reyee / Ruijie / UniFi 原厂渠道货）+ 无 KP → **不动（B 保留；来询按分销 20% 预付）**；坐实（官网自列登记号 + 许可号）' + TAG}},
    'SB-955': {'facts': {'legal_name': 'OMC Tech（最接近法人 บริษัท โอเอ็มซีเทค จำกัด OMC TECH COMPANY LIMITED เลขทะเบียน 0105559034613；注册资本 ฿4,000,000；3 名泰籍股东；登记业务 电气材料 ≠ 站内光端机 → 部分坐实）', 'founded': '2016-02-26' + TAG, 'hq': '99/349 Chaeng Watthana Rd., Thung Song Hong, Lak Si, Bangkok 10210' + TAG, 'size': '小型' + TAG,
                         'other': '第 117 批：视频光端机 / 转换器 为主「基本没有 switch」（Saga 仅 STC-110XGE 一款 MC）+ 无 KP + 9×0 → **不动（B 保留）**' + TAG}},
    'SB-1081': {'facts': {'legal_name': '未查（无法人名；sswmcctvshop.com 失效；siamskyworth@gmail.com）', 'founded': '未查' + TAG, 'hq': '未查（泰国）' + TAG, 'size': '未查' + TAG,
                          'other': '第 117 批：域名失效 + gmail + 16×0 + 丰润达在供（Q-33 口径）→ **不动（B 保留）**；0 查' + TAG}},
    'SB-609': {'facts': {'legal_name': 'บริษัท เอเบิลลิ้งค์(ประเทศไทย) จำกัด ABLELINK(THAILAND) COMPANY LIMITED（เลขทะเบียน 0105561132341；注册资本 ฿1,000,000；股东权益 ฿1,553,464；3 名泰籍股东；与 SB-614 Focomm 同址同构）', 'founded': '2018-08-03' + TAG, 'hq': '12 Soi Sukhaphiban 5 Soi 5 Yaek 3, Tha Raeng, Bang Khen, Bangkok 10220' + TAG, 'size': '微型（双牌照小分销）' + TAG,
                         'other': '第 117 批：安防 + 网络分销（已卖多个国内工业牌）、Simon「可以尝试多跟进」→ **分销 20% B small，一页纸一次（代表 SB-609 + SB-614 一线；预付 100%）**（收 info@ablelink.co.th，抄 info@focomm-cabling.com）；再无回声 → 两户一起不动；坐实' + TAG}},
    'SB-612': {'facts': {'legal_name': 'บริษัท คลาวด์ ไอที เน็ทเวิร์ค จำกัด CLOUD IT NETWORK CO., LTD.（เลขทะเบียน 0125554018059；注册资本 ฿1,000,000；股东权益 ฿1,880,014；3 名泰籍股东；财报 2563–2567 连续）', 'founded': '2011-09-29' + TAG, 'hq': '51/1 Mongkhon Niwet Village, Soi Ngamwongwan 48, Lat Yao, Chatuchak, Bangkok 10900' + TAG, 'size': '微型' + TAG,
                         'other': '第 117 批：15 年 VoIP 方案商（已从佛山进口 IP PBX）、Simon「可以尝试多跟进」→ **分销 20% B small，一页纸一次（IP 话机配套 PoE STC-028GP / 2216GP / 2224GP + STC-4424GCPM VLAN；预付）**（收 sales@）；再无回声 → 不动；坐实' + TAG}},
    'SB-034': [{'kp_match': 'tjcomputercctv@tj2003.net', 'role': '经营者（2025-03 回 Interested；2025-05 要 5 电口具体信息）= 收件人 — 一页纸一次：集成商 25% B small、直接报 STC-228GP（8 PoE + 2 SFP）+ 5 口 STI-054GP（4 PoE + 1 GE）按主表现价、MOQ 1、付费样机、预付 100%、小额快递 DAP' + TH + TAG},
               {'facts': {'legal_name': 'TJ Computer（泰国电脑 / CCTV 店；通名 + 域名失效 → 0 查）', 'founded': '未查' + TAG, 'hq': '未查（泰国）' + TAG, 'size': '微型（个体店推定）' + TAG,
                          'other': '第 117 批：店主本人回过 Interested + 两次具体需求 → **集成商 25% B small，一页纸一次（预付）**；再无回声 → 不动；0 查' + TAG}}],
    'SB-510': [{'kp_match': 'pongpanot.k@hotmail.com', 'role': '项目型买家本人（2024-06 问工业 2+4 / 2+8 PoE；19 次里 1 次实质）= 收件人 — 一页纸一次：集成商 25% B small、2+4 = STI-154GP / 2+8 = STI-288DGGPM $137、12 光 12 电 / 8 光 8 电 主表无此配置明说、预付 100%、付费样机' + TH + TAG},
               {'facts': {'legal_name': '未查（个人 Pongpanot Kwanmuang；hotmail）', 'founded': '未查' + TAG, 'hq': '未查（泰国）' + TAG, 'size': '个人' + TAG,
                          'other': '第 117 批：需求具体 + 1 次实质回复 + Simon「可以尝试多跟进」→ **集成商 25% B small，一页纸一次（预付）**；身份不清不升 A；再无回声 → 不动；0 查' + TAG}}],
    'SB-603': {'facts': {'legal_name': '未查（个人 Wirote；gmail；+66 65 426 3626）', 'founded': '未查' + TAG, 'hq': '未查（泰国）' + TAG, 'size': '个人' + TAG,
                         'other': '第 117 批：个人 + WA 14×0 实质 + 2023 后无新需求 → **不动（B 保留；来询再按集成商 25% 预付）**；0 查' + TAG}},
    # ───────── AE 14 ─────────
    'SB-918': [{'kp_match': 'kennedy@alston-systems.com', 'role': '研究档 KP（姓氏 / 职务待核；自有品牌 Alston）= 收件人 — 一页纸一次（最后一次）：贴标 OEM 30% B、Alston 标 / 中性包装 STC 阶梯 + STC-4424GCPM + MC STC-110XGE、SFP 模块不做、付费样机' + AE + TAG},
               {'kp_match': 'purchase@alston-systems.com', 'role': '采购箱（Ross）= 抄送' + TAG},
               {'facts': {'legal_name': 'Alston Systems Inc.（迪拜 JLT；美国法人 Alston Systems LLC, Delaware（注册代理地址）；阿联酋牌照号 1 查未得）', 'founded': '未取' + TAG, 'hq': '801 Reef Tower, Jumeirah Lake Towers, P.O. Box 62201, Dubai, UAE' + TAG, 'size': '小型' + TAG,
                          'other': '第 117 批：自有品牌 ICT / 安防 / 节能产品商（铜缆 / 光缆 / 有源 / 电源 / CCTV / LED），自称制造商 → **贴标 OEM 30% B，一页纸一次（最后一次；预付）**；16×0 在先 → 再无回声即不动；部分坐实（官网 contact）' + TAG}}],
    'SB-995': [{'kp_match': 'dipesh.p@acixme.com', 'role': 'Sales Director（研究档；安防渠道 VAD，Oud Metha）= 收件人 — 一页纸一次：分销 20% B、安装商渠道 CCTV / 门禁 PoE 阶梯 STC-028GP / 228GP / 2216GP / 2224GP + STC-4424GCPM、MOQ 1、付费样机、DAP 迪拜' + AE + TAG},
               {'kp_match': 'sales@acixme.com', 'role': 'Operations Executive（Akkeef P）= 抄送' + TAG},
               {'facts': {'legal_name': 'ACIX Middle East（acixme.com；牌照号 1 查未得；表内误记沙特 → 迪拜）', 'founded': '约 2010（「15 年+」）' + TAG, 'hq': '#217 Business Venue Building, Oud Metha, Dubai, UAE (P.O. Box 28474)' + TAG, 'size': '小型' + TAG,
                          'other': '第 117 批：IT 与安防产品增值分销 / 供应商（门禁 / 考勤 / IP CCTV / VMS；面向经销商 / SI / 安装商；2026-05 新闻稿活跃；Utepo 在供）→ **分销 20% B，一页纸一次（预付）**；回信 → 加厚；部分坐实（名录 + 新闻稿）' + TAG}}],
    'SB-421': {'facts': {'legal_name': 'Distributed Business Solutions Trading FZE（Distribolutions；牌照号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'SIT Tower, Nadd Hessa Street, Dubai Silicon Oasis, Dubai, UAE (P.O. Box 341455；另一名录 341355；+971 4 388 6508)' + TAG, 'size': '小型（11–50，Crunchbase 口径）' + TAG,
                         'other': '第 117 批：ICT 基础设施 / 网络安全集成；唯一需求 10G / 100G 光模块（Saga 不做，Q-32 缺口）→ **不动（B 保留；交换机需求出现再按集成商 25%）**；部分坐实（法定名 + 地址 + P.O. Box + 电话吻合）' + TAG}},
    'SB-325': [{'kp_match': 'agrajan@eim.ae', 'role': 'Project Manager（ZoomInfo；邮箱域 eim.ae 归属待核 → 同发 info@hamedelectronics.com）= 收件人 — 一页纸一次：集成商 25% B small、酒店 / 校园弱电 PoE STC-2216GP / 2224GP / STC-4424GCPM + STI-154GP、MOQ 1、付费样机、DAP 迪拜' + AE + TAG},
               {'facts': {'legal_name': 'Hamed Electronics LLC（Nasser Abdullatif Ahmed Lootah Group 成员；Dubai Police 认可；牌照号 1 查未得；同名 Mohammed Hamed Electronics Trading LLC Box 65146 ≠）', 'founded': '1985' + TAG, 'hq': 'P.O. Box 379738, Deira, Dubai, UAE（04-228 1214）' + TAG, 'size': '微型（1–10 人；营收 <$5M 口径）' + TAG,
                          'other': '第 117 批：40 年本地集团弱电集成商（CCTV / SMATV / 门禁 / PA；客户 酒店 / 教育 / 政府 / 医疗）→ **集成商 25% B small，一页纸一次（预付；政府项目不主动提）**；再无回声 → 不动；部分坐实（官网）' + TAG}}],
    'SB-878': [{'kp_match': 'saleem.a@magnusgulf.com', 'role': 'Managing Director（研究档；Magnus Infotech Trading LLC）= 拍板人 / 收件人 — 一页纸一次：分销 20% B（升 A 候选）、其品牌组合价格空档 = 价值档 PoE STC 阶梯 + Marvell 管理 STC-4424GCPM + 工业 STI-288DGGPM、中性包装、MOQ 1、付费样机、DAP 迪拜' + AE + TAG},
               {'kp_match': 'vishnu.n@magnusgulf.com', 'role': 'Product Specialist = 抄送' + TAG},
               {'facts': {'legal_name': 'Magnus Infotech Trading LLC（Magnus Gulf；牌照号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Al Tawhidi Building II – M4, Al Mankhool Rd, Bur Dubai, Dubai, UAE（+971 4 874 7373）' + TAG, 'size': '小型' + TAG,
                          'other': '第 117 批：B2B IT 增值分销（Cisco / Aruba / Ubiquiti / Netgear / D-Link / Teltonika / Vivotek；面向中东经销商与 SI），总经理为 KP → **分销 20% B（升 A 候选），一页纸一次（预付）**；回信 → 加厚 + 升 A；部分坐实（官网法定名 + 地址）' + TAG}}],
    'SB-400': {'facts': {'legal_name': 'Safa Networks FZE-LLC（沙迦自贸区；分支 UAE / 沙特 / 印度；牌照号 / 地址 1 查未得）', 'founded': '未取' + TAG, 'hq': '未取（Sharjah, UAE）' + TAG, 'size': '未取' + TAG,
                         'other': '第 117 批：进口数据 = 从印度进硬盘 / 内存的 IT 硬件贸易，官网通用文案，无 KP，7×0 → **不动（B 保留）**；部分坐实（法定后缀 + 进口数据）' + TAG}},
    'SB-495': [{'kp_match': 'ganesan@topnet.ae', 'role': 'Managing Director（官网 For Emergency Ganesan K +971 55 652 2648；NTI 经销联系人）= 拍板人 / 收件人 — 一页纸一次：分销 20% B（升 A 候选）、对位其工业线的 STI-154GP / 288DGGPM / 488DGGPM / 0240GE + STC-110XGE、3 年保、中性包装、MOQ 1、付费样机、DAP 迪拜 / 沙特转口自理' + AE + TAG},
               {'kp_match': 'athira@topnet.ae', 'role': 'Sales Engineer = 抄送' + TAG},
               {'facts': {'legal_name': 'Topnet Distribution FZCO（DAFZA；集团 Topnet Distribution LLC, Deira + Topnet Communications and Information Technology, 沙特；牌照号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Warehouse Unit K-11, Dubai Airport Free Zone, Dubai, UAE (P.O. Box 54791；+971 4 299 1162)' + TAG, 'size': '小型（3 法人集团）' + TAG,
                          'other': '第 117 批：ICT / 工业连接产品分销（经 SI / 电信安装商 / VAR；工业光纤交换机 / MC / PoE / ITS；表内 三旺 / Nsgate 在供），总经理为 KP，只跟过 2 次 → **分销 20% B（升 A 候选），一页纸一次（预付）**；回信 → 加厚 + 升 A；部分坐实（官网 + NTI 经销页）' + TAG}}],
    'SB-926': {'facts': {'legal_name': 'Osool Communications & Technical Systems（RAK；protenders 分包商；牌照号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'Villa Y1 Al Hamra near Al Jazeera Port, Ras Al Khaimah, UAE（+971 7 244 4355；手机 +971 50 686 8944 = Hossam Ayyad）' + TAG, 'size': '微型' + TAG,
                         'other': '第 117 批：机电 + 弱电分包；需求曾具体（2 光 8 电工业网管 PoE = STI-288DGGPM）但 WA 23×0 → **不动（B 保留；来询即报 STI-288DGGPM $137 预付）**；部分坐实（官网）' + TAG}},
    'SB-928': [{'kp_match': 'nibu@sevenstarsuae.com', 'role': '表内「Director」；ZoomInfo = Seven Stars Auto Spare Parts 的 Client Relations Associate（2021 起）→ 身份待核 — 不动，不发' + TAG},
               {'facts': {'legal_name': 'Seven Stars（阿布扎比多元集团：Rent A Car / Auto Garage / Auto Spare Parts / Technology / Five Stars 运输 / 校车；集团多牌照，1 查未得）', 'founded': '未取' + TAG, 'hq': 'Corporate Office: Nice Karak Refreshment Bldg, Hamdan Street, Abu Dhabi, UAE' + TAG, 'size': '中小（集团）' + TAG,
                          'other': '第 117 批：非目标行业（汽车 / 运输集团，IT 为旁支）+ KP 身份不符 + WA 23×0 → **不动（B 保留）**；部分坐实（官网）' + TAG}}],
    'SB-935': {'facts': {'legal_name': 'AL SHUAIB CONTROL EQUIPMENT L.L.C.（alshuaibelectronics.com；CP Plus CCTV 经销；牌照号 1 查未得）', 'founded': '2005' + TAG, 'hq': 'P.O. Box 30453, Near Central Post Office, Ras Al Khaimah, UAE' + TAG, 'size': '微型' + TAG,
                         'other': '第 117 批：RAK 弱电集成（CCTV / 布线 / BMS / IPTV）；主需求 HDMI 延长器（Saga 无）+ WA 22×0 → **不动（B 保留；工业 FS 来询再报 STI 线预付）**；部分坐实（名录）' + TAG}},
    'SB-581': {'facts': {'legal_name': 'Sheildify Security Equipment Trading LLC（Shieldify；牌照号 1 查未得）', 'founded': '2020' + TAG, 'hq': 'Tanvi Building Office 20, Port Saeed, Deira, Dubai, UAE (P.O. Box 118467；名录旧址 Khalifa BA Balila Bldg, 22B St, Abu Hail；+971 58 554 2050)' + TAG, 'size': '微型' + TAG,
                         'other': '第 117 批：2020 新设安防 / 医疗 / 消防 / 电池 UPS 多品牌网店（原厂 PoE 随 CCTV 走）+ 无 KP → **不动（B 保留）**；部分坐实（名录 + 官网页脚）' + TAG}},
    'SB-298': [{'kp_match': 'gafoor@vnstech.com', 'role': 'Executive Director（研究档；VNS Technologies LLC；与 AETEK 合作 5 年；问过 L2 还是 L3、说会来深圳）= 拍板人 / 收件人 — 一页纸一次：分销 20% B（升 A 候选）、直接答 L2 / L3：工业 2 光 8 电管理 = STI-288DGGPM（L2）$137；商用 24 电 = STC-2224GP（非管理）$86 / STC-4424GCPM（L2+，Marvell）$165、中性包装、MOQ 1、付费样机、DAP 阿布扎比、邀深圳面谈（时间 Simon 定）' + AE + TAG},
               {'facts': {'legal_name': 'VNS Technologies LLC（vnstech.com；LinkedIn 435 关注；区域办事处 迪拜 / 卡塔尔 / 印度 / 斯里兰卡；牌照号 1 查未得）', 'founded': '2009' + TAG, 'hq': 'Mina Zayed, Abu Dhabi, UAE (P.O. Box 51216；+971 2 666 7757)' + TAG, 'size': '小型（11–50）' + TAG,
                          'other': '第 117 批：安防 / 网络 / 存储增值分销（H3C / Huawei / AETEK / Network Optix / Rasilient / Irisity；经 VAR / SI / 顾问 / 承包商），执行董事本人看过具体型号 → **分销 20% B（升 A 候选），一页纸一次（预付）**；回信 → 加厚 + 升 A；守界：不评价 AETEK（另有 SB-138 / 019 一线）、Airspace Safety 类项目不碰；部分坐实（官网 + LinkedIn）' + TAG}}],
    'SB-043': [{'add_kp': {'name': 'M. Maarouf', 'email': 'm.maarouf@eurotechnology.ae', 'role': '表内具名邮箱（姓名职务待核；WA +971 50 751 4160 在线；41 次里回 4 次要资料）= 收件人 — 一页纸一次：集成商 25% B small、只给他要过的「资料」= CCTV PoE 阶梯 STC-028GP / 228GP / 2216GP / 2224GP + STC-4424GCPM 一口价、付费样机、MOQ 1、DAP 阿布扎比、WA 发链接' + AE + TAG, 'source': 'Clients 表邮箱（entities）'}},
               {'facts': {'legal_name': 'Euro Technology（eurotechnology.ae / .net；Paradox / CAME / Deister 授权经销；另列 迪拜 Abu Hail-Deira 总部 + 孟买；牌照号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'M4 Ruby Saloon Bldg, Opp Al Wahda Mall, Defence Rd (Hazaa Bin Zaid Rd), Abu Dhabi, UAE (P.O. Box 27709；+971 2 641 7222)' + TAG, 'size': '微型（约 9 人；营收估 $7M 口径不引用）' + TAG,
                          'other': '第 117 批：安防系统集成（CCTV / 门禁 / 报警 / 门闸 / PA / 消防报警）；唯一在 41 次里回过 4 次要资料的阿联酋安防集成商 → **集成商 25% B small，一页纸一次（预付；守界：军方 / 宫殿 / 政府 / 伊拉克项目一律不提不接）**；再无回声 → 不动；部分坐实（名录）' + TAG}}],
    'SB-136': [{'kp_match': 'pankaj@metalogint.com', 'role': 'Assistant Marketing Manager（rocketreach；2015 起）— 非拍板；不动，不发' + TAG},
               {'add_kp': {'name': 'Jaideep Paul', 'email': '', 'role': 'Director（rocketreach）— 不动，不发' + TAG, 'source': 'rocketreach.co Metalog International DMCC'}},
               {'facts': {'legal_name': 'Metalog International DMCC（DMCC 自贸区公司；行业 能源 / 油气供应链；尼日利亚 Port Harcourt 技术销售；牌照号 1 查未得）', 'founded': '未取' + TAG, 'hq': 'DMCC, Jumeirah Lake Towers, Dubai, UAE（门牌未取；+971 4 886 xxxx）' + TAG, 'size': '小型' + TAG,
                          'other': '第 117 批：非目标行业（油气供应链贸易）+ KP 非拍板 + 无具体兴趣 → **不动（B 保留）**；部分坐实（企业库）' + TAG}}],
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
