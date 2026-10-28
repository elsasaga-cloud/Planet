#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 119 批（T29-U112，公司底数第三十七轮 · 马来西亚 B 池 15 + 越南 B 池 15 + 沙特 B 池前 10 = 40 户；时限压缩版）官方登记核实 → 研究档 KP 角色 / 法定名 / 成立 / 总部 / 规模 / 定性 回写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/other_registry_2026-10-27.json（batch=119 行）。
本批定性：升 A 候选 ★ 2（SB-002 Xspec Technology Sdn Bhd 200501018493 (700608-K) 已成单 MD KP · 分销 20% 复购 / SB-497 Quang Lâm MST 0310601970 自有品牌 Wintop CEO KP · 贴标 OEM 30%）；
一页纸一次 · 集成商 25% 9（SB-732 Maxitulin / SB-366 TH IT / SB-736 Sun Energy 800805-W MD KP / SB-734 Sigma Rectrix / SB-733 Preciso / SB-746 Cybron / SB-468 Ninh Thanh MST 0106778512 CEO = 法人代表 / SB-788 TSS Khobar NEOM 承包 / SB-451 e-Saudi 2001 运营经理回过信）；
一页纸一次 · 分销 20% 8（SB-307 Saxco 1995 采购主动问 / SB-002 ★ / SB-315 Song Thành Công MST 0309279999 Moxa 分销 / SB-634 Hoàng Thiên Ân MST 0313394377 / SB-883 Phương Dung MST 0315321631 老板 = 法人代表 / SB-236 Minh Phước MST 0313120792 进口商 / SB-561 Zoom Line 迪拜 工业交换机分销页 / SB-685 Techsouq MD 回过 interesting）；
一页纸一次 · 贴标 OEM 30% 4（SB-852 展会问 OEM 0 查 / SB-497 ★ / SB-633 Hoàng Long MST 0102354061 自产工业交换机 / SB-876 LILIN Vietnam 自有 logo 未坐实）；
不动 19（SB-1131 marugged 美国 PLANET 分销 / 729 HeiTech 上市政府 SI / 790 Vulsan X 安全服务 / 052 个体 / 628 要光模块 / 912 个人 / 568 0 查 / 1102 HRUI 在供 Q-33 新壳 / 066 Comtec 产品线不对位 / 367 MTS 液压 / 579 NNC 电力守界 / 584 IT 服务 / 958 白牌网店 / 917 SCADA 项目 7×0 / 818 个人 / 577 无 KP 3×0 / 706 Moxa 官方分销 / 722 指定原厂 + 杂业 / 175 油气承包 24×0）。
坐实 14（SB-736 / 729 / 002 / 1102 / 497 / 633 / 066 / 367 / 468 / 579 / 584 / 634 / 883 / 236）/ 部分坐实 20（SB-307 / 732 / 1131 / 366 / 790 / 734 / 733 / 746 / 628 / 315 / 958 / 917 / 561 / 788 / 577 / 706 / 451 / 685 / 722 / 175）/ 未坐实 1（SB-876 同名异业）/ 0 查 5（SB-852 / 052 / 912 / 568 / 818）。
KP 坐实 = 老板 / 总经理 / 法人代表本人 8（SB-736 Tan Chan Sun MD / SB-002 Sugito Wibawa MD / SB-497 Hồ Lâm CEO / SB-468 Vũ Đình Tư 法人代表 / SB-883 Văn Đức Phương 法人代表 / SB-584 Trần Minh Hùng Giám đốc / SB-685 Ahmad Pervez MD / SB-451 Saeed Mohammed Operation Manager）；职务公开源吻合 1（SB-788 Murad Abusal）。
法定名补全 / 更正 35；**country_fix 7（SB-1131 → 美国 Mid-Atlantic Rugged Systems MD；SB-917 / 561 / 577 / 706 / 685 / 722 → 阿联酋：表内沙特实为迪拜 / 阿布扎比实体）**。
MY 路径实测（首次，15 户 4 个 SSM 号）：experian.com.my（新旧双格式 + 注册日 + 州 + 登记业务，SB-002）/ maukerja（SSM No，SB-736）/ 领英「Registration No」（上市公司，SB-729）/ 官网页脚「(xxxxxx-X)」（SB-366 姊妹）；contact.page / panpages / MATRADE 名录补地址；其余 部分坐实。
VN 路径实测（首次，15 户 11 个 MST，命中率最高）：masothue.com/<MST>-slug、thuvienphapluat / thongtincongty / infodoanhnghiep / yellowpages.vn（MST + 成立年 + 法人代表 + 地址 + 登记主业）；官网页脚常自列 MST（SB-497 / 236 / 883 / 584 / 958）；登记主业 ≠ 网站业务 → 部分坐实 + 标记（SB-315）；同名极多 → 以域名 / 法人代表 / 地址对齐，否则 未坐实（SB-876）或 归属未定（SB-958）。
SA 路径实测（首次，10 户 0 CR 号）：CR 不可 1 查；可得 = 官网 contact + ZoomInfo / RocketReach / 领英 → 部分坐实常态；**沙特池 10 户中 6 户实为阿联酋实体（表内按销售市场填沙特）→ 一律 country_fix**；沙特 / 阿联酋 一律 预付 100%、SASO / SABER / TDRA 不声称。
旁线索：TH IT Networks Sdn Bhd 198301012255（SB-366 姊妹）/ Wintop（SB-497 自有品牌 wintop.com.vn）/ Torque Automation Systems FZE（SB-917 域名主体，KP 已在 Fuzzy Logic）/ Vạn Phát Đạt Group 4400990704（≠ SB-584）/ Silversea 水产（≠ SB-876）/ Thiên Long Telecom 0312485663（SB-958 候选）。
Simon 待决：升 A 候选 SB-002（已成单，建议直接升）/ SB-497（回信即升）；SB-1102 Q-33 口径；6 户沙特 → 阿联酋 国别更正已执行（表内按市场填的，若要保留沙特口径请说）。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 119 批 官方登记核实 2026-10-28）'
MY = '— 马来西亚常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳、SIRIM 不声称'
VN = '— 越南常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳、MIC 不声称'
SA = '— 沙特常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP、SASO / SABER 不声称'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜、TDRA / ESMA 不声称'
UPD = {
    # ───────── MY 15 ─────────
    'SB-307': [{'kp_match': 'purchaser5@saxco.com.my', 'role': 'Purchaser（研究档；主动问网络交换机）= 收件人 — 一页纸一次：分销 20% B、摄像机 PoE STC-028GP $28 / STC-228GP / STC-2216GP / STC-2224GP 一口价 + MOQ 1 + 付费样机 ' + MY + TAG},
               {'facts': {'legal_name': 'Saxco Marketing Sdn Bhd（SSM 号 1 查未得；槟城 / 沙巴 / 古晋 / 马六甲 4 家姊妹 Sdn Bhd）', 'founded': '1995' + TAG, 'hq': '8 & 10, Jalan SS 4C/5, Taman Rasa Sayang, 47301 Petaling Jaya, Selangor（03-7880 2299）' + TAG, 'size': '中小（51–100）' + TAG,
                          'other': '第 119 批：全马安防产品分销商（CCTV 起家），采购本人主动问交换机、从未跟进 → **分销 20% B，一页纸一次**；回信 → 加厚；部分坐实（官网 + jobstreet）' + TAG}}],
    'SB-852': [{'kp_match': 'thiru_vajram@yahoo.com', 'role': '表内联系人（yahoo；展会谈 1+2+8 商用 PoE、问过 OEM）= 收件人 — 一页纸一次：贴标 OEM 30% B small、STC-228GP 中性包装 / 贴标 MOQ 起订 + 付费样机、预付 100% ' + MY + TAG},
               {'facts': {'legal_name': '0 查（yahoo + 公司名泛称 Alam Jaya Management）', 'size': '未取' + TAG, 'other': '第 119 批：展会问过 OEM → **贴标 OEM 30% B small，一页纸一次（预付 100%）**；再无回声 → 不动；0 查' + TAG}}],
    'SB-732': [{'kp_match': 'kumar@maxitulin.com', 'role': 'Design Analyst Engineer（研究档；PoE 用量大、项目 Cisco / Aruba）= 收件人（选型）— 一页纸一次：集成商 25% B、STC-2216GP / 2224GP + 室外 STI-154GP / STI-288DGGPM + STC-4424GCPM 一口价、bypass 不做明说、MOQ 1 + 付费样机 ' + MY + TAG},
               {'facts': {'legal_name': 'Maxitulin Sdn Bhd（MATRADE 服务名录；SSM 号 1 查未得）', 'hq': 'Unit 2-1, 1st Floor, Pusat Komersial Koi, Jalan Puchong Batu 13 1/2, 47100 Puchong, Selangor（+60 3 8062 2255；旧址 No. 29, Jalan Puteri 5/16）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：CCTV 供应 / 安装 / 维保 + 门禁 SI，工程师为 KP → **集成商 25% B，一页纸一次**；再无回声 → 不动；部分坐实（官网 + MATRADE）' + TAG}}],
    'SB-1131': [{'country_fix': '美国'},
                {'facts': {'legal_name': 'Mid-Atlantic Rugged Systems（marugged.com；州登记号 1 查未得）', 'hq': '95 Monocacy Blvd, Suite B18, Frederick, MD 21701, USA（855-784-4334）' + TAG, 'size': '微型（<25）' + TAG,
                           'other': '第 119 批：加固计算 / 工业网络 VAD（PLANET 授权分销专页 + Moxa / Teltonika），表内误归马来西亚 → country_fix 美国；原厂授权分销 + 无 KP → **不动（B 保留）**；部分坐实（官网 + ZoomInfo）' + TAG}}],
    'SB-366': [{'kp_match': 'inquiry@th-it.com', 'role': '表内联系人 Lee（职务待核；商业 PoE 需求记录）= 收件人 — 一页纸一次：集成商 25% B small、AP 供电 STC-028GP / STC-2216GP / 2224GP 一口价 + MOQ 1 + 付费样机 ' + MY + TAG},
               {'facts': {'legal_name': 'TH IT Resource Centre Sdn Bhd（本体 SSM 未取；页脚姊妹 TH IT Networks Sdn Bhd 198301012255 (107648-T)，Ekahau 授权分销）', 'founded': '姊妹 1983' + TAG, 'hq': 'No. 130, Jalan Kapar 27/89, Seksyen 27, 40400 Shah Alam, Selangor（+6016-280 3363）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：IT 设备租赁 + 无线网络设计，有商业 PoE 需求记录 → **集成商 25% B small，一页纸一次**；再无回声 → 不动；部分坐实（官网页脚）' + TAG}}],
    'SB-729': [{'kp_match': 'rizaki@heitech.com.my', 'role': 'Cybersecurity Consultant（研究档；展会对工业 PoE 有兴趣；非采购）— 不动，不发（企业项目来询按集成商 25% 报）' + TAG},
               {'facts': {'legal_name': 'HeiTech Padu Berhad（Registration No. 199401024950 (310628-D)；Bursa Malaysia 主板 HTPADU）', 'founded': '1994 / 1995' + TAG, 'hq': 'HeiTech Village, Persiaran Kewajipan, USJ 1, 47600 UEP Subang Jaya, Selangor（+60 3 8601 3000）' + TAG, 'size': '大型（约 979 人；营收 $56.9M）' + TAG,
                          'other': '第 119 批：上市政府 / 企业 ICT 系统集成商，招标采购 + 政府守界 + KP 非采购 → **不动（B 保留）**；坐实（登记号 + 上市代码）' + TAG}}],
    'SB-736': [{'kp_match': 'chansun@sunenergy.com.my', 'role': 'Managing Director（研究档；陈先生，会中文 → 英文稿；关心电源输入上限与防雷）= 拍板人 / 收件人 — 一页纸一次：集成商 25% B、STI 导轨机 DC 输入范围 / 浪涌等级按规格书逐条答、STC-2216GP / 2224GP 摄像机 PoE 一口价 + MOQ 1 + 付费样机 ' + MY + TAG},
               {'facts': {'legal_name': 'Sun Energy Enterprise Sdn Bhd（SSM 800805-W）', 'hq': '54-1, Jalan Metro Perdana Timur 9, Taman Usahawan Kepong, 52100 Kuala Lumpur（+60 3 6242 6818）' + TAG, 'size': '小型（<50）' + TAG,
                          'other': '第 119 批：CCTV / 报警 / 停车 / 门禁 / 网络 供应安装商，MD 本人 KP、问题具体 → **集成商 25% B，一页纸一次**；回信 → 加厚；坐实（SSM 号 + 地址 + 电话）' + TAG}}],
    'SB-790': [{'kp_match': 'mery@vulsanx.com', 'role': 'OSINT Researcher（研究档；非采购；在用知名品牌 24/48 口）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'Vulsan X（Sdn Bhd 推定；SSM 号 1 查未得）', 'founded': '2016-09-26' + TAG, 'hq': '59-2, Jalan MPK 3, Medan Perdagangan Kepayang, 70200 Seremban, Negeri Sembilan（06-851 5911）' + TAG, 'size': '小型（11–50）' + TAG,
                          'other': '第 119 批：网络安全 / AI 分析公司（非目标）+ 硬件量小 + KP 非采购 → **不动（B 保留）**；部分坐实（名录）' + TAG}}],
    'SB-734': [{'kp_match': 'mohamadfaiza@sigmarectrix.com', 'role': 'Pre-Sales Consultant（研究档；对 2 光 8 bypass 工业机有兴趣）= 收件人（售前选型）— 一页纸一次：集成商 25% B、STI-288DGGPM $137（无 bypass 明说）/ STI-488DGGPM $147 + 3 年保 + MOQ 1 + 付费样机 ' + MY + TAG},
               {'facts': {'legal_name': 'Sigma Rectrix Systems (M) Sdn Bhd（SSM 号 1 查未得；MyCC 认证防火墙开发商）', 'founded': '2003' + TAG, 'hq': 'Suite 3-05, 4805 CBD Perdana 2, Jalan Perdana, Cyber 12, 63000 Cyberjaya, Selangor（+60 3 8318 6696）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：ICT / IoT 集成 + 软件 + 培训（Ubiquiti 在用），售前明确要 2 光 8 工业机 → **集成商 25% B，一页纸一次**；再无回声 → 不动；部分坐实（官网 + 伙伴页 + 认证库）' + TAG}}],
    'SB-733': [{'kp_match': 'cschong@precisotechnology.com.my', 'role': 'Senior Manager（研究档；张志祥，会中文 → 英文稿；问工业级 85 ℃）= 收件人 — 一页纸一次：集成商 25% B、直接答 STI 线 -40～75 ℃（85 ℃ 不做）、STI-288DGGPM / STI-154GP 一口价 + 3 年保 + MOQ 1 + 付费样机 ' + MY + TAG},
               {'facts': {'legal_name': 'Preciso Technology Sdn Bhd（SSM 号 1 查未得；Volza 进口记录 10 票）', 'founded': '2018-06' + TAG, 'hq': '48-2, Jalan PJU 5/20D, The Strand, Kota Damansara, 47810 Petaling Jaya, Selangor（+603 6151 2777）' + TAG, 'size': '小型（11–50）' + TAG,
                          'other': '第 119 批：电信同步 / 主时钟系统专家 + IoT 集成（客户 运营商 / 金融 / 医院 / 轨交），高管为 KP → **集成商 25% B，一页纸一次**；轨交不主动提；再无回声 → 不动；部分坐实（官网 + 海关）' + TAG}}],
    'SB-002': [{'kp_match': 'sugito@xspec.com.my', 'role': 'Managing Director（abc-gcc 名录；研究档 KP；WA 在联；表内有成单记录）= 拍板人 / 收件人 — 复购一页纸：分销 20% B（升 A 候选 ★）、上次成交型号续单价 + STI-288DGGPM / STC-2224GP 一口价 + MOQ 1；WA 为主 ' + MY + TAG},
               {'facts': {'legal_name': 'Xspec Technology Sdn Bhd（SSM 200501018493 (700608-K)；登记业务 无损检测设备贸易 / 工业化学品批发 / 管理咨询；experian 数据至 2026-10-04）', 'founded': '2005-06-20' + TAG, 'hq': 'No 8, Jalan Industri USJ 1/8, Taman Perindustrian USJ 1, Subang Jaya, Selangor（+60 3 8023 1161）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：制造商代表 / 分销（NDT、军警安防、医疗、实验室；马 / 印尼 / 新），**已成单客户 + MD 本人 KP → 分销 20% B，复购一页纸；升 A 候选 ★（建议直接升）**；军警项目不主动提；坐实（SSM 号 + 注册日 + 地址 + MD）' + TAG}}],
    'SB-746': [{'kp_match': 'hussen@cybron.com.my', 'role': '表内联系人（研究档；要 5 电口资料、实需带光口工业 PoE；WA 无实质回复）= 收件人 — 一页纸一次：集成商 25% B、STI-154GP / STI-288DGGPM 一口价 + 3 年保 + MOQ 1 + 付费样机；邮件 + WA ' + MY + TAG},
               {'add_kp': {'name': 'Mohd Jamaluddin', 'email': '', 'role': 'Manager, Operations（ZoomInfo，2016 至今）= 抬头抄送' + TAG, 'source': 'zoominfo.com/p/Mohd-Jamaluddin/3456271277'}},
               {'facts': {'legal_name': 'Cybron System Sdn Bhd（SSM 号 1 查未得）', 'hq': 'No 10, Jalan Alfa A, U6/A Pusat Perdagangan Subang Permai, 40150 Shah Alam, Selangor（03 7831 3883）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：安防系统方案商（CCTV 为主），需求明确（带光口工业 PoE）→ **集成商 25% B，一页纸一次**；再无回声 → 不动；部分坐实（官网 + ZoomInfo）' + TAG}}],
    'SB-052': [{'kp_match': 'wanrohizal501@gmail.com', 'role': '表内联系人（gmail；需求 8 电口 + 4 光 6 电管理；问过样品）— 不动，不发（来询即按集成商 25% 报，付费样机，预付 100%）' + TAG},
               {'facts': {'legal_name': '0 查（gmail + 无域名；excellent data communications）', 'size': '个人' + TAG, 'other': '第 119 批：个体网络工程商 → **不动（B 保留；来询即报）**；0 查' + TAG}}],
    'SB-628': [{'kp_match': 'diana.wang@bright.net.my', 'role': 'Inside Sales & Administrative（研究档；非拍板；阿里巴巴询光模块）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'BrightNet Services Sdn Bhd（SSM 号 1 查未得）', 'hq': 'No. 20-4-10, Jalan 2/101C, Cheras Business Centre, 56100 Kuala Lumpur（03-9130 9887）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：一站式 SI（Cisco / Aruba / Huawei / Ubiquiti 含翻新），需求 = 光模块（Saga 无）+ KP 非拍板 → **不动（B 保留）**；部分坐实（名录）' + TAG}}],
    'SB-912': [{'kp_match': 'jentrx@gmail.com', 'role': '表内联系人 Tony（gmail；无需求描述；WA×0）— 不动，不发' + TAG},
               {'facts': {'legal_name': '0 查（gmail；jentronics）', 'size': '个人' + TAG, 'other': '第 119 批：个人 + 无需求描述 → **不动（B 保留）**；0 查' + TAG}}],
    # ───────── VN 15 ─────────
    'SB-568': [{'kp_match': 'semtec2017@gmail.com', 'role': '表内联系人 Trung（gmail；需求 16 / 24 / 32 口 PoE；2025-11 / 12 邮件无回）— 不动，不发（来询即按集成商 25% 报 STC-2216GP / 2224GP，预付 100%）' + TAG},
               {'facts': {'legal_name': '0 查（gmail + 无域名；Tiên Phong CP）', 'size': '未取' + TAG, 'other': '第 119 批：0 查 + 无回声 → **不动（B 保留；来询即报）**' + TAG}}],
    'SB-1102': [{'add_kp': {'name': 'Nguyễn Văn Đông', 'email': '', 'role': '法人代表（masothue 0109246393）— 不动（Q-33 待定）' + TAG, 'source': 'masothue.com/0109246393'}},
                {'facts': {'legal_name': 'CÔNG TY TNHH VIỄN THÔNG GIÁ TỐT / GOOD PRICE TELECOMMUNICATIONS CO., LTD（MST 0109246393；Công ty TNHH 2 thành viên；Đang hoạt động）', 'founded': '2020-07-01' + TAG, 'hq': 'Thôn Tiên Kha, Xã Phúc Thịnh, Hà Nội（0963 508 809）' + TAG, 'size': '微型（2020 新设）' + TAG,
                           'other': '第 119 批：网络设备电商 + 弱电施工（PLANET / TP-Link / Cisco / HRUI 正品 / 工业交换机），HRUI 在供（Q-33 口径待定）+ 2020 新壳 + 无 KP → **不动（B 保留；Q-33 放开则按分销 20% 推 Marvell 管理线，预付 100%）**；坐实（MST + 法人代表 + 成立日）' + TAG}}],
    'SB-315': [{'kp_match': 'linh@songthanhcong.com', 'role': '采购（研究档；表内注 MaiWe；2024 多次要价）= 收件人 — 一页纸一次：分销 20% B、STI-288DGGPM / STI-488DGGPM / STI-154GP 一口价 + 3 年保 + MOQ 1 + 付费样机、串口 MC 不做明说、不点名 Moxa / Maiwe ' + VN + TAG},
               {'kp_match': 'duc@stc-vietnam.com', 'role': 'Sales（研究档）= 抄送' + TAG},
               {'facts': {'legal_name': 'CÔNG TY TNHH THƯƠNG MẠI DỊCH VỤ SONG THÀNH CÔNG（STC Vietnam；MST 0309279999；登记主业「消防设备批发」≠ 网站工业自动化 → 标记）', 'founded': '2009' + TAG, 'hq': '247/8B Hoàng Hoa Thám, P.5, Q. Phú Nhuận, TP. Hồ Chí Minh（(028) 3507 4676；代表处 Thủ Đức）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：16 年工业自动化元器件贸易商（Moxa / Advantech 等数十品牌；报价部 pricing@），采购多次要价 → **分销 20% B，一页纸一次**；回信 → 加厚；部分坐实（MST + 地址；登记主业不符已标记）' + TAG}}],
    'SB-497': [{'kp_match': 'lamho@quanglam.com.vn', 'role': 'CEO（研究档 + 黄页公开；自有品牌 Wintop）= 拍板人 / 收件人 — 一页纸一次：贴标 OEM 30% B（升 A 候选 ★）、Wintop 标 / 中性包装 STI-288DGGPM / STI-488DGGPM / STI-154GP + STC-2224GP / 4424GCPM，MOQ 起订 + 付费样机、MC 仅 STC-110XGE 明说 ' + VN + TAG},
               {'facts': {'legal_name': 'CÔNG TY TNHH CÔNG NGHỆ QUANG LÂM / QLC CO., LTD（MST 0310601970；NNT đang hoạt động；自有品牌 Wintop wintop.com.vn）', 'founded': '2011-01-22（发证）' + TAG, 'hq': '99/1 Huỳnh Văn Nghệ, P.12 (An Hội Tây), Gò Vấp, TP. Hồ Chí Minh（(028) 3831 3119；办公 / 仓库 160/1/67 Phan Huy Ích）' + TAG, 'size': '中小' + TAG,
                          'other': '第 119 批：光通信设备分销 + 制造（自产跳线 / ODF；SFP / GPON / 交换机）+ 自有品牌 Wintop，CEO 本人 KP、已大量进口国内工业机 → **贴标 OEM 30% B，一页纸一次；升 A 候选 ★**；回信 → 加厚 + 升 A；坐实（MST + 发证日 + 地址 + CEO）' + TAG}}],
    'SB-633': [{'kp_match': 'nguyenhoang@hlc.vn', 'role': '表内联系人（研究档；职务未核；阿里巴巴询 16 槽机架）= 收件人 — 一页纸一次：贴标 OEM 30% B、HLC 标 / 中性包装 STI-288DGGPM / STI-488DGGPM / STI-0240GE，MOQ 起订 + 付费样机、机架不做明说、不点名三旺 ' + VN + TAG},
               {'facts': {'legal_name': 'CÔNG TY CỔ PHẦN XUẤT NHẬP KHẨU VÀ THƯƠNG MẠI HOÀNG LONG（MST 0102354061；ISO 9001）', 'founded': '2007' + TAG, 'hq': 'Số 9B Nguyễn Gia Thiều, P. Trần Hưng Đạo, Q. Hoàn Kiếm, Hà Nội（(024) 3939 3737）' + TAG, 'size': '小型（31–50）' + TAG,
                          'other': '第 119 批：电信 / IT / 工业网络设备供应安装 + 自述「专业生产工业交换机 / 光电转换器」（外购贴牌）+ 经销 Lantronix 工业 PoE、与国内同行合作 → **贴标 OEM 30% B，一页纸一次**；再无回声 → 不动；坐实（MST + 地址 + 成立年）' + TAG}}],
    'SB-066': [{'kp_match': 'caobaduy@comtec', 'role': 'Phó Giám Đốc（副总经理；黄页公开）— 不动，不发（交换机来询按分销 20% 报）' + TAG},
               {'facts': {'legal_name': 'CÔNG TY TNHH CÔNG NGHỆ VÀ TRUYỀN THÔNG COMTEC（MST 0100774014；主业 机械设备批发；所有人 Vũ Thái Hải）', 'founded': '1998-11-09' + TAG, 'hq': 'Số 9, ngách 45, ngõ 91 Nguyễn Chí Thanh, Láng Hạ, Đống Đa, Hà Nội（现办公 GoldSeason 47 Nguyễn Tuân；(024) 3773 4926）' + TAG, 'size': '中小' + TAG,
                          'other': '第 119 批：27 年电信设备 / 元器件批发（Viettel / MobiFone / VNPT 供应商；电源 / OTDR / 光模块 / 光缆配件），产品线不对位 + 无互动 → **不动（B 保留）**；坐实（MST + 成立日 + 所有人）' + TAG}}],
    'SB-367': [{'kp_match': 'hydraulics@vnn.vn', 'role': '表内联系人 Lee（液压公司；偶发询 2 光 6 电）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'CÔNG TY CỔ PHẦN MTS / MTS JSC（MST 0101892941）', 'founded': '2006-03-20' + TAG, 'hq': 'Số 166 đường Tựu Liệt, Tam Hiệp, Thanh Trì, Hà Nội（门店 Kiốt 7 CT4C X2 Bắc Linh Đàm；(024) 3641 6189）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：液压设备贸易（非目标行业）→ **不动（B 保留）**；坐实（MST + 发证日 + 地址）' + TAG}}],
    'SB-468': [{'kp_match': 'dinhtu.vu@ninhthanh.com', 'role': 'CEO / 法人代表（登记 VŨ ĐÌNH TƯ 吻合；阿里巴巴 RFQ 1 光 4 电）= 拍板人 / 收件人 — 一页纸一次：集成商 25% B small、STI-154GP / STC-228GP $33 一口价 + MOQ 1 + 付费样机、opener 引其 RFQ ' + VN + TAG},
               {'facts': {'legal_name': 'CÔNG TY TNHH SẢN XUẤT VÀ THƯƠNG MẠI NINH THANH / NINH THANH PRODUCTION AND TRADING CO., LTD（MST 0106778512）', 'founded': '2015-02-27（发证）' + TAG, 'hq': 'Số 20, ngách 24, ngõ 38, đường Xuân La, Xuân Đỉnh / Tây Hồ, Hà Nội（0904 550 273）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：电信 / 数字化方案分销商，CEO 本人发过 RFQ 且从未跟进 → **集成商 25% B small，一页纸一次**；再无回声 → 不动；坐实（MST + 发证日 + 地址 + 法人代表 = KP）' + TAG}}],
    'SB-579': [{'kp_match': 'kinhdoanh8@nnc.net.vn', 'role': 'Kinh doanh（销售）Hoa（研究档；询盘表来源；WA×0）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'Công ty TNHH Nhất Nước (NNC)（MST 0101403703；义安分厂 -001）', 'founded': '2003' + TAG, 'hq': 'Tòa G03 Căn 2412, Vinhomes Greenbay, 7 Đại Lộ Thăng Long, Nam Từ Liêm, Hà Nội（024 3784 9934）' + TAG, 'size': '中小' + TAG,
                          'other': '第 119 批：电气设备制造 + 电站 / 变电站 / 线路工程（电力守界）+ 无需求描述 → **不动（B 保留）**；坐实（MST + 成立年 + 地址）' + TAG}}],
    'SB-584': [{'kp_match': 'hungtran@vanphatdat.vn', 'role': 'Giám đốc（官网自列 Trần Minh Hùng；IT 外包商）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'Vạn Phát Đạt（vanphatdat.vn / it-support.vn；ĐKKD / MST 0315053647；≠ 富安省 Vạn Phát Đạt Group 4400990704）', 'founded': '2018-05-17（发证）' + TAG, 'hq': '26/37/6 Đường B3, P. Tây Thạnh, Q. Tân Phú, TP. Hồ Chí Minh（028 6265 5310；河内代表处 Sannam Bldg 78 Duy Tân）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：IT 外包 / Helpdesk 服务商（非目标）+ 无需求 → **不动（B 保留）**；坐实（官网自列登记号 + 发证日 + 总监）' + TAG}}],
    'SB-634': [{'kp_match': 'anhpt@hoangthienan.com.vn', 'role': 'Project Director（研究档；自建站询 16 槽机架）= 收件人 — 一页纸一次：分销 20% B small、STI-288DGGPM / STI-154GP 对位 + 3 年保 + MOQ 1 + 付费样机、机架 / SFP 不做明说、不点名 ORing ' + VN + TAG},
               {'facts': {'legal_name': 'CÔNG TY CỔ PHẦN THƯƠNG MẠI KỸ THUẬT HOÀNG THIÊN ÂN / HOANG THIEN AN TECHNOLOGY CORP（MST 0313394377；法人代表 Lê Thị Kim Thoa；黄页列域名 hoangthienan.vn，表内 .com.vn）', 'founded': '2015-08-11（发证）' + TAG, 'hq': '29 Đường DD11, P. Tân Hưng Thuận, Q.12, TP. Hồ Chí Minh' + TAG, 'size': '微型（5–24）' + TAG,
                          'other': '第 119 批：SFP / GPON SFP / Wintop MC / Cisco / EtherWAN / ORing / Huawei 小贸易商，项目总监为 KP → **分销 20% B small，一页纸一次**；再无回声 → 不动；坐实（MST + 发证日 + 地址 + 法人代表；域名后缀差异已注）' + TAG}}],
    'SB-883': [{'kp_match': 'info@phuongdung.com', 'role': '负责人 / 法人代表（masothue VĂN ĐỨC PHƯƠNG 吻合；另代表 Univision Việt Nam JSC、Sài Gòn New；1 次跟进无回复）= 拍板人 / 收件人 — 一页纸一次：分销 20% B small、摄像机 PoE STC-028GP $28 / STC-228GP / STC-2216GP 一口价 + MOQ 1 + 付费样机、不点名 ONV ' + VN + TAG},
               {'facts': {'legal_name': 'CÔNG TY TNHH VIỄN THÔNG PHƯƠNG DUNG / PHUONG DUNG TELECOM CO., LTD（MST 0315321631；GCN 变更 2024-04-10）', 'founded': '约 2018（MST 0315 段）' + TAG, 'hq': '40/14 Tân Thành, P. Tân Phú, TP. Hồ Chí Minh（0989 865 766；分支 Đà Nẵng / Tây Ninh）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：监控摄像机批发零售 + 安装（Vantech / KBVision / Hikvision / Dahua；站内 ONV 交换机），老板 = 法人代表 → **分销 20% B small，一页纸一次**；1×0 在先 → 再无回声即不动；坐实（MST + 地址 + 法人代表 + 分支）' + TAG}}],
    'SB-236': {'facts': {'legal_name': 'CÔNG TY TNHH GIẢI PHÁP CÔNG NGHỆ MINH PHƯỚC / MINH PHUOC SOLUTIONS TECHNOLOGY CO., LTD（MST 0313120792；官网自列；≠ 平顺省 Cty TNHH Minh Phước 油品）', 'founded': '2015-01-30' + TAG, 'hq': '11/31 Nguyễn Thái Sơn, P.3, Q. Gò Vấp, TP. Hồ Chí Minh' + TAG, 'size': '小型' + TAG,
                         'other': '第 119 批：电信 / 光跳线 / 光缆 / 摄像机 / 机柜 进口 + 生产分销（表内：从国内同行大量进口光产品）→ **分销 20% B small，一页纸一次（Attn: Purchasing；gmail 公用箱 → 预付 100%）**；再无回声 → 不动；坐实（官网自列 MST + 成立日 + 地址 + 英文名）' + TAG}},
    'SB-876': {'facts': {'legal_name': 'LILIN Vietnam / Silversea HCM（法人 1 查未得；同名 Silversea 水产 4202007157 / New Material 3801292166 ≠）', 'hq': '未取（TP. Hồ Chí Minh）' + TAG, 'size': '未取' + TAG,
                         'other': '第 119 批：台湾 LILIN CCTV 越南分销商，表内「自己的 logo」「工业交换机」→ **贴标 OEM 30% B small，一页纸一次（Attn: Marketing / Purchasing；未坐实 → 预付 100%）**；再无回声 → 不动；未坐实（同名异业，1 查止）' + TAG}},
    'SB-958': {'facts': {'legal_name': 'Siêu Thị Viễn Thông（sieuthivienthong.com 归属未定：.com.vn = Công ty TNHH Kỹ Thuật Viễn Thông Thiên Long MST 0312485663（Q.12）/ .net = Công ty TNHH Siêu Thị Viễn Thông（Tân Bình））', 'hq': 'TP. Hồ Chí Minh（Q.12 或 Tân Bình，待定）' + TAG, 'size': '微型' + TAG,
                         'other': '第 119 批：电信 / 安防设备电商（Hikvision / Dahua / TP-Link / Ubiquiti；在卖深圳白牌 PoE）+ 无 KP + 归属未定 → **不动（B 保留）**；部分坐实（两同名候选）' + TAG}},
    # ───────── SA 10 ─────────
    'SB-917': [{'country_fix': '阿联酋'},
               {'kp_match': 'arjun.murali@fuzzylogicautomation.com', 'role': '项目 / 技术（研究档；邮箱域 = Fuzzy Logic Equipment Trading Ltd，阿布扎比 KIZAD；+971 54 585 1777 吻合；7×0）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'Torque Automation Systems FZE（torqsys.com；沙迦 P.O. Box 121718 + 迪拜 SZR）；KP 现属 Fuzzy Logic Equipment Trading Ltd（阿布扎比 KIZAD）；牌照号 1 查未得', 'hq': 'Building 280, Taweelah, KIZAD Free Zone, Abu Dhabi, UAE（Torque：P.O. Box 121718, Sharjah；+971 4 432 9204）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：工业自动化 / SCADA 承包（水 / 污水 / 工业厂站），表内沙特实为阿联酋 → country_fix 阿联酋；项目型 + 7×0 → **不动（B 保留）**；部分坐实（两官网 + 企业库）' + TAG}}],
    'SB-818': {'facts': {'legal_name': '0 查（gmail + 05x 手机；个人 / 小商户）', 'size': '个人' + TAG, 'other': '第 119 批：需求 2 光 16 管理 ×4、23 推 1 回 → **不动（B 保留；WA 来询即按集成商 25% 报 STI-288DGGPM，预付 100%）**；0 查' + TAG}},
    'SB-561': [{'country_fix': '阿联酋'},
               {'kp_match': 'faisal@zoomlinenetwork.com', 'role': 'Business Development Manager（研究档）= 收件人 — 一页纸一次：分销 20% B、STI-288DGGPM / STI-488DGGPM / STI-154GP + STC-2224GP / 4424GCPM 一口价 + MOQ 1 + 付费样机、DAP 迪拜 ' + AE + TAG},
               {'facts': {'legal_name': 'Zoom Line Networks Technology（法人名 / 牌照号 1 查未得；联系电话全为迪拜 +971 4 325 7866 / +971 55 378 6444；KSA 页为 SEO 分页）', 'hq': 'Dubai, UAE（门牌未取）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：IT / 网络 / 安防分销（TP-Link / Ubiquiti / MikroTik / Cisco / Fortinet；「Industrial Switches Distributor」专页；面向 KSA），表内沙特实为迪拜 → country_fix 阿联酋；BDM 为 KP → **分销 20% B，一页纸一次**；再无回声 → 不动；部分坐实（官网电话）' + TAG}}],
    'SB-788': [{'kp_match': 'murad@tss-e.com', 'role': 'Senior Manager, Accounts & Projects（ZoomInfo「Murad Abusal」吻合；需求 工业光口交换机 + SFP）= 收件人 — 一页纸一次：集成商 25% B、STI-288DGGPM $137 / STI-488DGGPM $147 + STC-4424GCPM 一口价、SFP 不做明说、MOQ 1 + 付费样机 ' + SA + TAG},
               {'facts': {'legal_name': 'Telecom Special Solutions (TSS)（合伙企业，领英口径；NEOM 核准 ICT 与基础设施承包商；CR 号 1 查未得）', 'founded': '2012' + TAG, 'hq': 'Prince Faisal Bin Fahad Road, Al Moosa Building, Al Khobar（+966 13 846 8882；分支 Riyadh / NEOM）' + TAG, 'size': '小型（11–50；自报 51–200）' + TAG,
                          'other': '第 119 批：数据中心 / MEP / 安防 / 电信 turnkey 承包商，项目经理为 KP、需求明确 → **集成商 25% B，一页纸一次**；NEOM / 政府项目按单核；回信 → 加厚；部分坐实（领英 + ZoomInfo）' + TAG}}],
    'SB-577': [{'country_fix': '阿联酋'},
               {'facts': {'legal_name': 'MetaWorld Computers LLC（官网自列；牌照号 1 查未得；自有「Metacom」光纤产品线）', 'hq': 'Deyaar Building, Office 331, Damascus Street, Al Qussais Industrial Area 1, Dubai, UAE（+971 4 353 7555 / +971 56 213 4555）' + TAG, 'size': '小型' + TAG,
                          'other': '第 119 批：光纤 / 连接 / ELV / 安防 / 电信设备供应，表内沙特实为迪拜 → country_fix 阿联酋；无 KP + 3×0 → **不动（B 保留；Metacom 自有线要交换机再按贴标 30% 报）**；部分坐实（官网）' + TAG}}],
    'SB-706': [{'country_fix': '阿联酋'},
               {'kp_match': 'm.nejadi@eworldme.com', 'role': 'Chief Operating Officer（研究档；Moxa 官方分销商）— 不动，不发（自有品牌 / 低价补位线诉求出现再按贴标 OEM 30% 报）' + TAG},
               {'kp_name': 'Akram Jafari', 'role': 'Sales Manager（研究档）— 不动' + TAG},
               {'facts': {'legal_name': 'Easy World Automation L.L.C（eWorld；牌照号 1 查未得；Moxa 中东领先分销商近 20 年）', 'founded': '2002' + TAG, 'hq': 'Office 204, Building 1, Emaar Business Park, Sheikh Zayed Road, Dubai, UAE (P.O. Box 29505；+971 4 447 1137)；分支 Al Khobar（+966 13 850 6010）/ Riyadh（+966 11 275 1110）/ Muscat' + TAG, 'size': '中小' + TAG,
                          'other': '第 119 批：工业数据通信 / 自动化 VAD（Moxa 官方分销 = 同行渠道），总部迪拜 → country_fix 阿联酋；无 OEM 诉求 → **不动（B 保留）**；部分坐实（官网）' + TAG}}],
    'SB-451': [{'kp_match': 'saeed@e-saudi.net', 'role': 'Operation Manager / Business Development Manager（RocketReach，2005 至今；表内 1 次跟进有回复 要 Catalog）= 拍板人 / 收件人 — 一页纸一次：集成商 25% B、远端站点 STI-154GP / STI-288DGGPM 宽温 + 机房 STC-4424GCPM 一口价 + 3 年保 + MOQ 1 + 付费样机、opener 引其要 Catalog ' + SA + TAG},
               {'facts': {'legal_name': '(e-Saudi) Electronic Saudi Network（e-saudi.net / e-saudi.net.sa；CR 号 1 查未得）', 'founded': '2001' + TAG, 'hq': 'Abdallah Bahamdan St, Suleimaniya, Riyadh（吉达分支）' + TAG, 'size': '小型（11–50；14 人 RocketReach）' + TAG,
                          'other': '第 119 批：远程自动化 / 控制与通信 + 固定宽带连接方案商，运营经理本人回过信 → **集成商 25% B，一页纸一次**；回信 → 加厚；部分坐实（企业库）' + TAG}}],
    'SB-685': [{'country_fix': '阿联酋'},
               {'kp_match': 'ahmad@techsouq.com', 'role': 'Managing Director（ZoomInfo，2009 至今；2024-09 回 interesting）= 拍板人 / 收件人 — 一页纸一次：分销 20% B small、电商上架 STC-028GP $28 / STC-228GP / STC-2216GP 一口价 + MOQ 1 + 付费样机 + DAP 迪拜、机架 / 周边不做明说 ' + AE + TAG},
               {'kp_match': 'info@techsouq.com', 'role': 'Co-Founder（研究档 Shifan Shivani）= 抄送' + TAG},
               {'facts': {'legal_name': 'Techsouq Computers L.L.C.（迪拜；牌照号 1 查未得）', 'founded': '1999（自述）' + TAG, 'hq': 'Bayan Business Center, Dubai Investments Park 1, Dubai, UAE (P.O. Box 27570；+971 4 355 0600；旧址 Al Abbas Bldg, Khalid Bin Al Waleed Rd)' + TAG, 'size': '微型（约 8 人）' + TAG,
                          'other': '第 119 批：老牌 IT 电商（「难找的 IT 产品」采购），表内沙特为分站 → country_fix 阿联酋；MD 本人回过 interesting → **分销 20% B small，一页纸一次**；再无回声 → 不动；部分坐实（企业库）' + TAG}}],
    'SB-722': [{'country_fix': '阿联酋'},
               {'kp_match': 'info@aptvelglobal.com', 'role': '表内联系人 Arunima Raj（职务未核；要 PLANET 48 口、问 bypass；WA×0）— 不动，不发' + TAG},
               {'facts': {'legal_name': 'Aptvel Global（法人 / 牌照号 1 查未得）', 'founded': '约 2020（自述 5+ 年）' + TAG, 'hq': '204, Building 3, Arenco Offices, DIP 1, Dubai, UAE（+971 4 882 4871）' + TAG, 'size': '微型' + TAG,
                          'other': '第 119 批：电气 / 自动化 / IoT / AV / 家庭影院 / 软件 杂业方案商，表内沙特实为迪拜 → country_fix 阿联酋；需求指定原厂（PLANET 48 口）+ bypass（Saga 无）→ **不动（B 保留）**；部分坐实（官网 + ZoomInfo）' + TAG}}],
    'SB-175': [{'kp_match': 'prabhu@mbtc.com.sa', 'role': 'Project Manager（研究档；2024-01「有用但现在没需求」；WA 24×0）— 不动，不发' + TAG},
               {'kp_match': 'ei-telcomlead@aamindustrial.com', 'role': 'E&I / Telecom lead（研究档 Wasi Akthar；AAM Industrial 项目组）— 不动' + TAG},
               {'facts': {'legal_name': 'M. Al-Barghash Trading & Contracting Company (MBTC)（1976；100% 沙资；关联 AAM Industrial；CR 号 1 查未得）', 'founded': '1976' + TAG, 'hq': 'Al-Khobar 31952 / P.O. Box 31996 Dammam, Eastern Province, Saudi Arabia' + TAG, 'size': '大型（1001–5000 brandfetch，口径存疑）' + TAG,
                          'other': '第 119 批：油气 / 建筑设备材料供应 + 承包（项目型），明说没需求 + WA 24×0 → **不动（B 保留；项目来询按集成商 25% 报，预付 100%）**；部分坐实（名录）' + TAG}}],
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
