#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 115 批（T29-U108，公司底数第三十三轮 · 印度 B 池收尾 5 户 + 韩国 B 池第 1 轮前 35 户 = 40 户；Simon「韩国的好好挖挖」→ KR 允许第 2 次定向检索）官方登记核实 → 研究档 KP 角色 / 法定名 / 事实 补写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=115 行）。
结构同 batch114_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：B BIG · 加厚一次 5（SB-210 (주)디오넷 229-81-33168 营收 295억 自研交换机 贴标 / 配套 30% / SB-929 ㈜솔텍 110 人 300억 光网络自产 配套 30% / SB-511 (주)리버네트워크 106-86-14301 NEXI 自有品牌 280억 贴标 30% / SB-485 엔아이투스(주) 119-86-00900 200억 외감 回「Price and ODM」贴标 / ODM 30% 升 A 候选 / SB-336 (주)인터코엑스 140-81-85228 买过样品 要 8+2+2 = STC-228GP 贴标 30%）；
加厚一次 4（SB-513 (주)유비큐넷 876-81-02587 Starlink 自有品牌 代表 = KP / SB-502 엘림광통신㈜ 123-81-89423 自有标 PoE 管理交换机送 KC / SB-029 (주)이트레이딩코리아 109-86-25355 ETK 自有品牌 代表 = KP Woosy / SB-226 (주)한창인포텍 106-86-81310 自有 logo + Volktek 代理 Director 会英文）；
一页纸一次 · 有回声再加厚 14（SB-329 CANSOL / MONAD 自研工业 L2 CEO = KP 号码未取 / SB-967 와이앤엠시스템즈 106-87-07961 广播 PTZ 代表 = KP / SB-536 (주)하이링크 工业无线 + HRUI 在供 Q-33 口径 / SB-545 미래정보기술 792-87-00191 HRUI 贴标在供 Q-33 口径 / SB-938 씨포라인 654-86-03297 微型 OEM/ODM 传输设备 KP 已是代表 / SB-982 (주)엠씨에스솔루션 106-86-25768 PLANET 代理 / SB-480 (주)한요 代表 = KP 光 / MC 厂 / SB-968 (주)제니스텍 206-81-71494 Ruggedcom 分销 守界 / SB-553 (주)DG-ITX 120-81-78820 CCTV 出口厂 / SB-922 파이버베이스 135-17-28243 OTDR + 光分销 代表 = KP / SB-923 ㈜혜성테크윈 491-88-01315 自有标工业光交换机 MAS / SB-940 Cominet President Song 号码未取 / SB-557 UBITRON 138-81-55769 工厂 CCTV 集成 / SB-957 써보테크TS 130-86-06691 自动化分销）；
不动 17（SB-635 LMD Hitech U29240HR2013PTC048422 机械厂 非目标 / SB-640 Technoverse 27CWEPK3302H2ZS 2023 个体 / SB-1106 个人 0 查 / SB-1107 个人 0 查 / SB-595 mpcl.in 地址失效 + 同名陷阱 / SB-322 BlackBear 83305324 Atop 关联 同行集团 country_fix 台湾 / SB-220 sun-flowers 未坐实 / SB-508 gotinc 未坐实 / SB-440 (주)제이엠피시스템 214-86-68224 52 次 0 回复 / SB-598 solway 未坐实 / SB-925 (주)미래시그널 142-81-31693 婉拒 / SB-961 팩토스 708-35-00450 个体 / SB-962 트리플네트웍스 138-81-53140 业务不明 / SB-963 (주)유니텔 138-81-80123 非主业 / SB-966 (주)뷰텔 214-87-56744 非目标 / SB-509 ionetech 身份不清 / SB-637 NaSys 35 次 0 回复）；
坐实 26 / 部分坐实 7（SB-329 / 929 / 536 / 480 / 940 / 962 / 637：号码或地址未取）/ 未坐实 7（SB-1106 / 1107 / 595 / 220 / 508 / 598 / 509，其中 1106 / 1107 为 0 查）；
KP 坐实 = 代表 / 老板本人 9（SB-513 이재식 / SB-967 이명호 / SB-440 홍순진 / SB-938 김건 / SB-029 우성영 / SB-480 남상준 / SB-922 강민철（推定）/ SB-940 송태진（推定）/ SB-329 KJ Lee）；KP 更正 1（SB-485 Peter 邮箱退信 → 地址失效、只发 Y.H. Ahn）；补代表姓名 add_kp 22；补邮箱 1（SB-480 sales@hanyotele.com）；
法定名补全 / 更正 31；country_fix 1（SB-322 KR → 台湾：主体 統編 83305324 新竹竹北 + 日本子公司 法人番号 8010401158437）。KR 稿件一律英文、20 / 25 / 30 + T/T 预付 + FOB 深圳、KC 不声称（由买方自办）。
KR 检索路径实测：页脚 사업자등록번호（10 位）最稳（starlink / mcss / etradingkorea / hcin4 / elimopt / zenithtek / hyesungtechwin / view-tel / servo-tech / top-fa / miraesignal / rivershop）→ bizno.net（法人号 + 设立日 + 代表 + 员工数）→ jobkorea / catch / saramin（매출 / 사원수 / 자본금 / 외감）→ rndcircle / cookiedeal（补充）；DART 仅上市 / 外监登记（view-tel 命中）；英文名 + 「사업자등록번호 대표」 1 查命中率约 2/3，落空多为同名（썬플라워 / 지오티 / 솔웨이 / 코미넷）→ 第 2 次用 「"域名" OR "英文名" + 产品词」。
旁线索（≠ 目标，另立户评估）：MONAD Inc.（SB-329 研发姊妹）；솔텍인포넷(주)（SB-929 关联法人）；VMSoft（SB-553 子公司）；(주)FB정보통신 DOTPIA（SB-922 关联）；Atop 四零四科技（SB-322 同址母体，同行）；BlackBear TechHive Japan 株式会社（SB-322 日本子公司）；MPCL Industries Limited U26959DL1993PLC219546（SB-595 同名 ≠）。
Simon 待决（累计见 PR-02-53 追记）：升 A 候选 SB-485（回「Price and ODM」即升）+ SB-210 / 929 / 511 / 336；Q-33 HRUI 口径（本批 SB-536 / 545 两户按「只推 Marvell 管理 / 工业线」起草）；2.5G 口径（SB-545 MR- 2.5G 线等 SB-263 口径）；KR 发送窗 Tue/Thu 10–12 KST。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 115 批 官方登记核实 2026-10-28）'
KR = '— 韩国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳、KC 不声称'
UPD = {
    # ---------- 第 1/3 IN 5 + KR 9 ----------
    'SB-635': [{'kp_match': 'sales@radiantgroup.org', 'name': 'Dinesh Sharma', 'role': 'Director, LMD Hitech India Pvt Ltd（DIN 02249388；zaubacorp）— 机械厂非目标，不动' + TAG},
               {'facts': {'legal_name': 'LMD Hitech India Private Limited（CIN U29240HR2013PTC048422；Plot No. 620, Sector 8, IMT Manesar, Haryana 122052；特种机械 / 矿山建筑机械制造；实缴 ₹1 lakh）', 'founded': '2013-02-27' + TAG,
                          'other': '第 115 批：机械制造商、无网络业务、域名不可达 + WA 无回复 → **非目标行业，不动（B 保留）**' + TAG}}],
    'SB-640': [{'kp_match': 'sales@technoversebs.com', 'role': 'Technoverse Business Solutions 研究档 KP（个体经销；WA 已加无回复）' + TAG},
               {'facts': {'legal_name': 'Technoverse Business Solutions（个体经营；GSTIN 27CWEPK3302H2ZS，2023-11-07；202, Shiv Sambhav CHS, Savarkar Road, Dombivli, Thane 421201；营业额 ₹0–40 lakh）', 'founded': '2023' + TAG,
                          'other': '第 115 批：2023 年新设个体经销、WA 无回复 → **不动（B 保留；自来询盘按一口价 + T/T 预付）**' + TAG}}],
    'SB-1106': {'facts': {'legal_name': '（个人联系人 Ruhan Farook；无公司 / 域名 / 邮箱；0 查）', 'founded': '未取' + TAG,
                          'other': '第 115 批：个人、无主体、16 次无进展 → **不动**' + TAG}},
    'SB-1107': {'facts': {'legal_name': '（个人联系人 Surya Namberdar；无公司 / 域名 / 邮箱；0 查）', 'founded': '未取' + TAG,
                          'other': '第 115 批：个人、无主体、只问卢比价（Saga 只报 USD）→ **不动**' + TAG}},
    'SB-595': {'facts': {'legal_name': '未坐实（mpcl.in 无公开主体；1 查仅命中同名 MPCL Industries Limited U26959DL1993PLC219546 mpcl.co.in 德里电气设备集团 ≠）', 'founded': '未取' + TAG,
                         'other': '第 115 批：域名无主体 + 邮箱退信 + 非 Saga 成交 → **不动（地址失效；同名不并线）**' + TAG}},
    'SB-210': [{'kp_match': 'chris@deonet.co.kr', 'role': 'DEONET Co., Ltd. 研究档 KP（可多跟进）= 收件人；代表이사 이혁재 = 拍板人' + TAG},
               {'add_kp': {'name': '이혁재 Lee Hyuk-jae', 'role': '대표이사 (주)디오넷 DEONET Co., Ltd.（bizno / jobkorea）= 拍板人' + TAG, 'email': '', 'source': 'https://bizno.net/article/2298133168'}},
               {'facts': {'legal_name': '(주)디오넷 DEONET Co., Ltd.（사업자등록번호 229-81-33168；법인등록번호 110111-1564940；서울 구로구 디지털로 242, 한화비즈메트로 802호；24–25 人；매출 2024 295억 / 2025 260억원；자본금 18억；외감；非上市）', 'founded': '1998-07-13' + TAG,
                          'other': '第 115 批：自研交换机厂（ISP / 家庭网络线）、曾问 PoE 芯片 + 工业线 → **贴标 / 配套 OEM 30% B BIG，加厚一次（工业 STI-288DGGPM / STI-488DGGPM + Marvell 管理 PoE STC-2224GP / STC-4424GCPM、芯片平台明写；GPON / EPON 明说没有；Chris 直呼、抄 info@）**；回信 → 次候选 / 升 A 候选' + KR + TAG}}],
    'SB-322': [{'kp_match': 'eki@blackbear-ics.com', 'role': 'President, BlackBear TechHive（日本子公司 BlackBear TechHive Japan 株式会社 法人番号 8010401158437；母体 台灣黑熊網路安全 統編 83305324，Atop 同址）— 同行集团，不动' + TAG},
               {'facts': {'legal_name': '台灣黑熊網路安全股份有限公司 BlackBear (Taiwan) Industrial Networking Security Ltd.（統編 83305324；新竹縣竹北市東興路一段146號 = Atop 同址；代表人 謝秋蓮）+ BlackBear TechHive Japan 株式会社（法人番号 8010401158437；東京都港区六本木3-6-9）', 'founded': '2020-11-26（TW）/ 2021-03（JP）' + TAG,
                          'other': '第 115 批：工业交换机厂 Atop 关联的网安硬件商、问的是 OEM/ODM 代工、33 次 0 回复 → **同行集团 + 守界，不动（B 保留）**；表内 iso KR 为展会地 → country_fix 台湾' + TAG},
                'country_fix': '台湾'}],
    'SB-329': [{'kp_match': 'kjlee@cansol.co.kr', 'name': 'KJ Lee', 'role': 'CEO, CANSOL Co., Ltd.（cansol.co.kr/about；MONAD Inc. 研发姊妹）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'CANSOL Co., Ltd.（销售）+ MONAD Inc.（研发；monadinc.co.kr）；#1209 B-Dong, Seongnam Central BIZ Tower 2차, 사기막골로 99, 중원구, 성남시 13201；사업자등록번호 两查未取', 'founded': '未取' + TAG,
                          'other': '第 115 批：自研工业 L2 交换机 + ITS / 道路项目方、CEO = KP、曾问 bypass → **贴标 / 配套 30% B small，一页纸一次（bypass 明说没有；STI-288DGGPM / STI-488DGGPM / STI-0240GE 宽温 + 3 年保 + 自编货号；KJ Lee 直呼）**；再无回声 → 不动；部分坐实、只做预付' + KR + TAG}}],
    'SB-336': [{'kp_match': 'byron@intercoax.com', 'role': 'INTERCOAX 研究档 KP（买过样品；问 8 PoE + 2 GE + 2 SFP = STC-228GP）= 收件人' + TAG},
               {'kp_match': 'jongmin@intercoax.com', 'role': 'INTERCOAX 研究档 KP = 抄送' + TAG},
               {'add_kp': {'name': '이일묵 Lee Il-muk', 'role': '대표이사 (주)인터코엑스 INTERCOAX Co., Ltd.（jobkorea / rndcircle）= 拍板人' + TAG, 'email': '', 'source': 'https://www.jobkorea.co.kr/recruit/co_read/c/intercoax'}},
               {'facts': {'legal_name': '(주)인터코엑스 INTERCOAX Co., Ltd.（사업자등록번호 140-81-85228；경기도 안양시 동안구 학의로 250；17 人；자본금 6억；매출 2025 11.3억원）', 'founded': '2014-04-17' + TAG,
                          'other': '第 115 批：自有品牌 EoC 厂、买过样品、明确要 8+2+2 → **贴标 OEM 30% B，加厚一次（对位 STC-228GP 一口价 + 自编货号 / 中性包装 + 付费样机复购价；Byron 直呼、抄 Jongmin）**；营收下滑 → 只做 T/T 预付' + KR + TAG}}],
    'SB-513': [{'kp_match': 'help@ubiqnet.co.kr', 'name': 'Jaesik Lee（이재식）', 'role': '대표이사 주식회사 유비큐넷 Ubiqnet Co., Ltd.（starlink.co.kr 页脚）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': '주식회사 유비큐넷 Ubiqnet Co., Ltd.（사업자등록번호 876-81-02587；통신판매업 제2022-서울용산-1075호；서울 용산구 청파로 113-6, 넥서스밸리 905호；自有品牌 Starlink）', 'founded': '≈2022（通信贩卖申报 2022）' + TAG,
                          'other': '第 115 批：自有品牌 Starlink 贴标 + 代表本人为 KP → **贴标 OEM 30% B，加厚一次（Starlink 标 STI-154GP / STI-288DGGPM + STC-228GP / STC-2224GP + 中性包装 / 自编货号 / MOQ 1 / 付费样机；Jaesik 直呼）**；回信 → 次候选' + KR + TAG}}],
    'SB-929': [{'kp_match': 'kky@soltech.co.kr', 'role': 'SOLTECH 研究档 KP（Simon 既有联系人）= 收件人；대표 이동화 = 拍板人' + TAG},
               {'kp_match': 'jasonk@soltech.co.kr', 'role': 'SOLTECH 研究档 KP = 抄送' + TAG},
               {'add_kp': {'name': '이동화 Lee Dong-hwa', 'role': '대표 ㈜솔텍 SOLTECH / 솔텍인포넷(주)（jobkorea / saramin）= 拍板人' + TAG, 'email': '', 'source': 'https://www.jobkorea.co.kr/Recruit/Co_Read/C/soltech99'}},
               {'facts': {'legal_name': '㈜솔텍 SOLTECH（+ 关联 솔텍인포넷(주)，同代表 이동화；서울 영등포구 당산로41길 11, 당산 SK V1센터 1702–1704호；110 人；매출 ≈300억원；자본금 2억；INNO-BIZ；사업자등록번호 未取）', 'founded': '1996-05-01' + TAG,
                          'other': '第 115 批：自产光网络设备 110 人厂、Simon 既有联系人 → **贴标 / 配套 OEM 30% B BIG，加厚一次（PoE / 管理交换机补位 STC-2224GP / STC-4424GCPM + 工业环网 STI-288DGGPM / STI-488DGGPM + 自编货号 / 中性包装 / 付费样机；Kim Kwang Young 直呼、抄 Jason）**；군관련 / 变电站不提；部分坐实、只做预付' + KR + TAG}}],
    'SB-967': [{'kp_match': 'mhlee@ynminc.com', 'name': 'MH Lee（이명호 Lee Myung-ho）', 'role': '대표이사 / CEO 주식회사 와이앤엠시스템즈 YNM Systems Inc.（bizno）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': '주식회사 와이앤엠시스템즈 YNM Systems Inc.（사업자등록번호 106-87-07961；법인등록번호 110111-5457109；서울 금천구 가산디지털1로 119, SK트윈테크타워 A동 1105·1106·1108호；6–8 人；广播 PTZ 摄像机制造）', 'founded': '2014-07-04' + TAG,
                          'other': '第 115 批：微型广播摄像机品牌、CEO = KP → **配套 25% B small，一页纸一次（随其 IP PTZ 成套的 PoE 交换机 STC-028GP / STC-228GP + 贴标可谈 30%、MOQ 1、付费样机；MH Lee 直呼）**；再无回声 → 不动' + KR + TAG}}],
    'SB-220': {'facts': {'legal_name': '未坐实（sun-flowers.co.kr 官网为防机器人验证页；2 查仅同名 썬플라워리조트 / 썬플라워 电商个体 / 썬플라워유통 ≠）', 'founded': '未取' + TAG,
                         'other': '第 115 批：官网不可读 + 两查无主体 + 无 KP + 23 次 0 回复 → **不动（B 保留）**' + TAG}},
    'SB-502': [{'add_kp': {'name': '유영록 Yoo Young-rok', 'role': '대표이사 엘림광통신㈜ Elim Optical Communication Co., Ltd.（jobkorea / KC 시험성적서）= 拍板人（研究档无具名 KP → 收件 elimopt@ + h0824@ / khs10623@）' + TAG, 'email': 'elimopt@elimopt.co.kr', 'source': 'https://www.jobkorea.co.kr/recruit/co_read/c/elimopt'}},
               {'facts': {'legal_name': '엘림광통신㈜ Elim Optical Communication Co., Ltd.（사업자등록번호 123-81-89423；경기도 수원시 권선구 산업로155번길 234, 2동 4층；13 人；자본금 8억；매출 ≈45억원；自有标 PoE 管理交换机 EL-G48E6TG-POE 等（2024-11 以制造者名义送 KC）；MAS 多数供应者）', 'founded': '2003-06-23' + TAG,
                          'other': '第 115 批：自有品牌 PoE 管理交换机 + 政府 MAS 渠道 → **贴标 OEM 30% B，加厚一次（对位 EL-G48E6TG / G24E4G / G16E2G / G8E4G 全系的 STC-4424GCPM / STC-2224GP / STC-2216GP / STC-228GP 阶梯价 + 自编货号 / 中性包装 + 付费样机；bypass 明说没有；KC 由其自办、我方给 CE / FCC / RoHS 报告；收 elimopt@ 称 Mr. Yoo）**；回信 → 次候选' + KR + TAG}}],
    # ---------- 第 2/3 KR 13 ----------
    'SB-508': {'facts': {'legal_name': '未坐实（gotinc.co.kr 官网为防机器人验证页；2 查仅同名 (주)지오티 船用发动机 / 지아이오티 / 지오테크놀로지 / 美国 GOT Inc 货运 ≠）', 'founded': '未取' + TAG,
                         'other': '第 115 批：官网不可读 + 两查无主体 + 无 KP + 22 次 0 回复 → **不动（B 保留）**' + TAG}},
    'SB-511': [{'add_kp': {'name': '한석준 Han Seok-jun', 'role': '대표이사 주식회사 리버네트워크 River Network Co., Ltd.（rivershop.co.kr 页脚 / jobkorea）= 拍板人（研究档无具名 KP → 收件 scale@goriver.co.kr 称 Mr. Han）' + TAG, 'email': '', 'source': 'https://rivershop.co.kr/'}},
               {'facts': {'legal_name': '주식회사 리버네트워크 River Network Co., Ltd.（사업자등록번호 106-86-14301；통신판매업 용산 01487；서울 용산구 원효로 68-5；45 人；매출 ≈280억원；自有品牌 NEXI（2009 起）；Cisco SMB / QNAP / Dell / HPE Aruba / TP-Link 代理）', 'founded': '2002-11-14' + TAG,
                          'other': '第 115 批：自有品牌 NEXI 进口分销商（≈$20M）→ **贴标 OEM 30% B BIG，加厚一次（补「NEXI Pro」管理 / PoE / 工业层：STC-228GP / STC-2224GP / STC-4424GCPM + STI-154GP / STI-288DGGPM + 自编货号 / 中性包装 / MOQ 1 / 付费样机；收 scale@ 称 Mr. Han）**；回信 → 次候选 / 升 A 候选' + KR + TAG}}],
    'SB-536': [{'add_kp': {'name': '김윤섭 Kim Yoon-seop', 'role': '대표이사 주식회사 하이링크 Highlink Co., Ltd.（highlink.co.kr/about-us）= 拍板人（研究档无具名 KP → 收件 support@ 称 Mr. Kim）' + TAG, 'email': '', 'source': 'https://www.highlink.co.kr/about-us'}},
               {'facts': {'legal_name': '주식회사 하이링크 Highlink Co., Ltd.（경기도 광주시 464-865；工业无线 DIVA 系列 / RF 调制解调器自研自产；在售 HRUI 商用 PoE；사업자등록번호 两查未取）', 'founded': '未取' + TAG,
                          'other': '第 115 批：自研工业无线厂 + HRUI 商用 PoE 在供（Q-33 口径：只推 Marvell 管理 / 工业线）→ **配套 OEM 30% B small，一页纸一次（工业 PoE STI-154GP / STI-288DGGPM / STI-488DGGPM + 商用只给 STC-4424GCPM；贴 Highlink 标可谈；收 support@ 称 Mr. Kim）**；再无回声 → 不动；部分坐实、只做预付' + KR + TAG}}],
    'SB-545': [{'add_kp': {'name': '김기성 Kim Ki-seong', 'role': '대표이사 미래정보기술 주식회사 Mirae Information Technology Co., Ltd.（bizno）= 拍板人（研究档无具名 KP → 收件 customer@ 称 Mr. Kim）' + TAG, 'email': '', 'source': 'https://bizno.net/article/7928700191'}},
               {'facts': {'legal_name': '미래정보기술 주식회사 Mirae Information Technology Co., Ltd.（사업자등록번호 792-87-00191；법인등록번호 131111-0424132；경기도 성남시 중원구 둔촌대로 388, 302호 크란츠 테크노；5 人；自有 MR- 系列 PoE = HRUI 贴标在供）', 'founded': '2015-10-01' + TAG,
                          'other': '第 115 批：HRUI 商用 PoE 贴标在供（Q-33 口径：不碰现线、只推 Marvell 管理 / 工业线）→ **贴标 OEM 30% B small，一页纸一次（MR- 标的上层机型 STC-4424GCPM + STI-154GP / STI-288DGGPM + 自编货号 / 中性包装 / MOQ 1；2.5G 等 SB-263 口径；收 customer@ 称 Mr. Kim）**；再无回声 → 不动' + KR + TAG}}],
    'SB-440': [{'kp_match': 'cs@jmpsystem.com', 'name': 'Hong Soon Jin（홍순진）', 'role': '대표이사 (주)제이엠피시스템 JMP Systems Co., Ltd.（bizno）= 拍板人 — 52 次 0 回复，不动' + TAG},
               {'facts': {'legal_name': '(주)제이엠피시스템 JMP Systems Co., Ltd.（사업자등록번호 214-86-68224；법인등록번호 110111-2076415；통신판매업 2015-경기하남-0054；경기도 하남시 조정대로 150, 아이테코 블루존 304·310호；19 人；소기업）', 'founded': '2000-09-26' + TAG,
                          'other': '第 115 批：代表本人为 KP、需求明确（FE 6 口 4 PoE 贴标 ×10）但 52 次 0 回复 → **多次 0 回复规则：不动（B 保留；自来询盘按 HRUI FE 款 + 30% 贴标、MOQ 10、T/T 预付报）**' + TAG}}],
    'SB-938': [{'kp_match': 'shkim@c4line.com', 'name': 'Gun Kim（김건）', 'role': '대표 씨포라인 C4Line（2024-07 新法人；rndcircle）/ OEM/ODM Product Manager = 拍板人 / 收件人' + TAG},
               {'kp_match': 'info@c4line.com', 'role': 'President / MD C4Line（rocketreach）= 抄送' + TAG},
               {'facts': {'legal_name': '씨포라인 C4Line（사업자번호 654-86-03297，2024-07-25 新设；경기도 수원시 영통구 신원로 88, 디지털엠파이어2 101동 908호；3 人；2024 매출 5.2억원；品牌 2004 起；EoC / UTP / 2-Wire IP 传输设备 OEM/ODM，主销欧美）', 'founded': '2024-07-25（品牌 2004）' + TAG,
                          'other': '第 115 批：微型 OEM/ODM 传输设备厂、KP 已是代表 → **配套 25% B small，一页纸一次（与 Easy Coax 成套出口的 STC-028GP / STC-228GP + 贴标可谈 30% + MOQ 1 / 付费样机；Gun Kim 直呼、抄 Sung Kim）**；再无回声 → 不动；新法人 + 微型 → 只做预付' + KR + TAG}}],
    'SB-982': [{'kp_match': 'support@mcss.co.kr', 'role': 'MCS Solution 研究档 KP（support@）= 收件人（抄 sales@）；대표이사 이일우 = 拍板人' + TAG},
               {'add_kp': {'name': '이일우 Lee Il-woo', 'role': '대표이사 (주)엠씨에스솔루션 MCS Solution Co., Ltd.（mcss.co.kr 页脚 / jobkorea）= 拍板人' + TAG, 'email': 'sales@mcss.co.kr', 'source': 'https://www.mcss.co.kr/'}},
               {'facts': {'legal_name': '(주)엠씨에스솔루션 MCS Solution Co., Ltd.（사업자등록번호 106-86-25768；통신판매업 제2017-서울금천-1333호；서울 금천구 디지털로 178, 현대가산퍼블릭 A동 1009호；9 人；자본금 1억；매출 2025 23.4억원（2022 58.7억）；PLANET 工业网络代理 + UniFi）', 'founded': '2004-01-30' + TAG,
                          'other': '第 115 批：PLANET 工业线代理 + UniFi 集成、未触达 → **集成 25% B small，一页纸一次（台系工业线的性价比第二来源 STI-154GP / STI-288DGGPM / STI-488DGGPM + STC-2224GP；不点名 PLANET / UniFi；收 support@ + 抄 sales@）**；营收腰斩 → 只做 T/T 预付' + KR + TAG}}],
    'SB-029': [{'kp_match': 'woosy777@naver.com', 'name': 'Woosy（우성영 Woo Sung-young）', 'role': '대표이사 (주)이트레이딩코리아 ETRADINGKOREA Co., Ltd.（etradingkorea.com 公司概要）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'reesung.park@etradingkorea.com', 'role': 'ETRADINGKOREA 研究档联系人（公司邮箱）= 抄送' + TAG},
               {'facts': {'legal_name': '(주)이트레이딩코리아 ETRADINGKOREA Co., Ltd.（사업자등록번호 109-86-25355；서울 영등포구 영신로 220, KnK디지털타워 1413호；3 人；营收 10–50억 档；自有品牌 ETK 交换机 / 光模块 / 工业 bypass；进口代行；公共采购供应商；파랑새 网店）', 'founded': '2010-09-15' + TAG,
                          'other': '第 115 批：自有品牌 ETK + 自营进口 + 代表本人为 KP、2025-06 有回声 → **贴标 OEM 30% B，加厚一次（ETK 标 STI-288DGGPM / STI-488DGGPM / STI-0240GE + STC-2224GP / STC-4424GCPM + 自编货号 / 中性包装 / MOQ 1 / 付费样机；bypass / 光模块明说没有；Woosy 直呼、抄 reesung.park@）**；回信 → 次候选；微型 → 只做预付' + KR + TAG}}],
    'SB-226': [{'kp_match': 'jryoun74@hcin4.com', 'role': 'Director, (주)한창인포텍 HANCHANG Infotech（公司对外邮箱 = KP 邮箱；会英文）= 收件人；대표이사 배성훈 = 拍板人' + TAG},
               {'kp_match': 'parkhj4003@hcin4.com', 'role': 'HANCHANG Infotech 研究档联系人 = 抄送' + TAG},
               {'add_kp': {'name': '배성훈 Bae Seong-hoon', 'role': '대표이사 (주)한창인포텍 HANCHANG Infotech Co., Ltd.（hcin4.com 회사개요）= 拍板人' + TAG, 'email': '', 'source': 'https://hcin4.com/default/01/02.php'}},
               {'facts': {'legal_name': '(주)한창인포텍 HANCHANG Infotech Co., Ltd.（사업자등록번호 106-86-81310；통신판매업 00960；서울 용산구 청파로 40, 삼구빌딩 1610호；10 人；交换机 / RJ45 / DP 线缆制造 + 分销；Volktek 代理；R.FOINT MALL）', 'founded': '2011-09-06' + TAG,
                          'other': '第 115 批：自有 logo 商用 FS + Volktek 代理、Director 会英文、仅触达 2 次 → **贴标 OEM 30% B，加厚一次（管理 / PoE 升级 STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-154GP / STI-288DGGPM + 自编货号 / 中性包装 / MOQ 1 / 付费样机；不点名 Volktek；Peter Youn 直呼、抄 Park）**；回信 → 次候选' + KR + TAG}}],
    'SB-485': [{'kp_match': 'yhahn@n-itus.com', 'role': 'N-iTUS 研究档 KP（2025-11 回「Price and ODM」）= 收件人；대표 장세봉 = 拍板人' + TAG},
               {'kp_match': 'peter01@n-itus.com', 'role': 'Director（邮箱退信 → 地址失效、不再发）' + TAG},
               {'add_kp': {'name': '장세봉 Jang Se-bong', 'role': '대표이사 엔아이투스(주) N-iTUS Co., Ltd.（bizno / catch）= 拍板人' + TAG, 'email': '', 'source': 'https://bizno.net/article/1198600900'}},
               {'facts': {'legal_name': '엔아이투스(주) N-iTUS Co., Ltd.（사업자등록번호 119-86-00900；법인등록번호 110111-3736141；경기 군포시 엘에스로 153-8, 4층；37–40 人；매출 ≈200억원；외감；信用 양호；运营商级交换机 / FTTH ONT / G.fast / PLC 制造）', 'founded': '2007-08-14' + TAG,
                          'other': '第 115 批：运营商级设备厂、主动回「Price and ODM」→ **贴标 / ODM OEM 30% B BIG，加厚一次（升压 PoE 价目无（Q-32）明说 → 标准 PoE STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-288DGGPM 阶梯价；ODM = 现机型贴 N-iTUS 标 + 自编货号 / 中性包装 / 固件 logo 可谈，不做全新设计；付费样机；Y.H. Ahn 直呼）**；回信 → **升 A 候选**' + KR + TAG}}],
    'SB-598': [{'kp_match': 'jskim@solway.co.kr', 'role': 'Solway 研究档 KP（主体未坐实；需求 bypass，Saga 无）' + TAG},
               {'facts': {'legal_name': '未坐实（solway.co.kr 官网为防爬验证页；2 查仅同名 소울웨어 / 솔내시스템 / 한국에스웨이 / Solway Group 矿业 ≠）', 'founded': '未取' + TAG,
                          'other': '第 115 批：官网不可读 + 两查无主体 + 需求 bypass（Saga 无）→ **不动（B 保留）**' + TAG}}],
    'SB-480': [{'kp_name': 'Nam Sang Jun', 'role': '대표이사 (주)한요 Hanyo Co., Ltd.（jobkorea / incruit）= 拍板人 / 收件人（sales@hanyotele.com）' + TAG},
               {'add_kp': {'name': '(주)한요 영업팀 sales@', 'role': '官方销售邮箱（blog.naver hanyotele）= 收件地址' + TAG, 'email': 'sales@hanyotele.com', 'source': 'https://m.blog.naver.com/hanyotele/220024781772'}},
               {'facts': {'legal_name': '(주)한요 Hanyo Co., Ltd.（인천 계양구 장제로 714, 5층 세종팰리스빌딩；27 人（2013）；자본금 2억；매출 2021 9.8억원（2016 27억）；光通信元件 / PoE 媒体转换器制造 + 出口；사업자등록번호 未取）', 'founded': '2001-02-01' + TAG,
                          'other': '第 115 批：自有 logo 光 / MC 厂、代表本人为 KP、从未触达 → **配套 OEM 30% B small，一页纸一次（随其光配线 / MC 成套的 STC-228GP / STC-2224GP + STI-154GP / STI-288DGGPM + 贴 Hanyo 标 / 自编货号 / MOQ 1 / 付费样机；光模块 / 尾纤明说不做；收 sales@ 称 Mr. Nam）**；营收下滑 → 只做预付；部分坐实' + KR + TAG}}],
    'SB-925': [{'kp_match': 'sjyeo@miraesignal.com', 'role': 'Mirae Signal 研究档 KP（展会当面婉拒：已有深圳供应商）— 不动' + TAG},
               {'add_kp': {'name': '심수만 Shim Su-man', 'role': '대표 (주)미래시그널 Mirae Signal Co., Ltd.（miraesignal.com 页脚）— 婉拒，不动' + TAG, 'email': '', 'source': 'http://www.miraesignal.com/'}},
               {'facts': {'legal_name': '(주)미래시그널 Mirae Signal Co., Ltd.（사업자번호 142-81-31693；경기도 성남시 분당구 판교로 744, 분당테크노파크 C동 405호；매출 ≈19.4억원；自有 MV- 系列交换机 + 无线网桥 + 军用无线开发）', 'founded': '2010-10-28' + TAG,
                          'other': '第 115 批：自有品牌 MV- 线已有深圳交换机供应商、当面婉拒 → **婉拒者剔出群发：不动（B 保留）**；군 무선통신 线不碰' + TAG}}],
    # ---------- 第 3/3 KR 13 ----------
    'SB-968': [{'add_kp': {'name': '윤석열 Yoon Seok-yeol', 'role': 'CEO (주)제니스텍 ZENITHTEK Co., Ltd.（zenithtek.co.kr）= 拍板人（研究档无具名 KP → 收件 zenithtek@ 称 Mr. Yoon）' + TAG, 'email': '', 'source': 'http://www.zenithtek.co.kr/kr/company/intro.php'}},
               {'facts': {'legal_name': '(주)제니스텍 ZENITHTEK Co., Ltd.（사업자등록번호 206-81-71494；서울 성동구 성수일로4길 25, 서울숲코오롱디지털타워 601–603호；Ruggedcom 韩国分销 2005 起 / Softing / Perle / Garland / Xelas；电力 IT + 工业自动化）', 'founded': '2002-06' + TAG,
                          'other': '第 115 批：高端工业以太网（Ruggedcom）分销商、客户多在守界行业 → **分销 20% B small，一页纸一次（只谈钢铁 / 石化 / 水泥等工厂非关键段：STI-288DGGPM / STI-488DGGPM / STI-0240GE + 付费样机；IEC 61850 / EN 50155 / 军用明说不做；不点名 Ruggedcom；收 zenithtek@ 称 Mr. Yoon）**；再无回声 → 不动' + KR + TAG}}],
    'SB-553': [{'kp_match': 'ussales@sequrinet.com', 'role': 'Team Leader, US sales, SEQURINET / (주)DG-ITX = 收件人；대표이사 박상열 = 拍板人' + TAG},
               {'add_kp': {'name': '박상열 Park Sang-yeol', 'role': '대표이사 (주)DG-ITX（SEQURINET；前 ㈜아이티엑스시큐리티）（sequrinet.com 회사연혁）= 拍板人' + TAG, 'email': '', 'source': 'http://sequrinet.com/KR/Sequrinet/history.asp'}},
               {'facts': {'legal_name': '(주)DG-ITX（SEQURINET；前 ㈜아이티엑스시큐리티 ITX Security，2008-03 改名；사업자등록번호 120-81-78820；통신판매업 제2016-서울금천-0029호；서울 금천구 가산디지털1로 212, 코오롱디지털타워 애스턴 906호；水原工厂 2007；2008 三千万美元出口塔；子公司 VMSoft；에스원 S1 协力企业）', 'founded': '≤2007' + TAG,
                          'other': '第 115 批：出口型 CCTV / NVR 品牌厂、在用台系工业 FS、KP 为美国销售线 → **配套 OEM 30% B，一页纸一次（随 NVR 套件出货的 STC-028GP / STC-228GP / STC-2224GP + STI-154GP / STI-288DGGPM 贴 SEQURINET 标 + 中性包装 / 自编货号 / MOQ 1 / 付费样机；CE / FCC / RoHS 报告齐；Eva 直呼）**；再无回声 → 不动；不点名 Utepo、不提 NDAA' + KR + TAG}}],
    'SB-922': [{'kp_match': 'michael_kang@fiberbase.co.kr', 'role': '대표 파이버베이스 Fiberbase（강민철 Kang Min-cheol；kofis.co.kr 页脚；推定同人）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': '파이버베이스 Fiberbase（个人事业者 사업자번호 135-17-28243；통신판매 제2011-경기수원-2231호；경기 용인시 기흥구 영덕동 흥덕IT밸리 컴플렉스동 516호；后设 (주)파이버베이스 法人（号未取）；OTDR FISCAN9 制造 + 光网络分销；kofis.co.kr 商城）', 'founded': '≤2011' + TAG,
                          'other': '第 115 批：光测试仪器自产 + 光网络分销（在用 Diva MC）、代表本人为 KP → **分销 20% B small，一页纸一次（PoE / 工业交换机补位 STC-228GP / STC-2224GP + STI-154GP / STI-288DGGPM + 贴 Fiberbase 标可谈 30%、MOQ 1、付费样机；MC / 光模块明说不做；Michael Kang 直呼）**；再无回声 → 不动；个人事业者档 → 只做预付' + KR + TAG}}],
    'SB-923': [{'kp_match': 'kis@hstw.net', 'role': 'Director, ㈜혜성테크윈 HYESUNG TECHWIN = 收件人；대표이사 우윤학 = 拍板人' + TAG},
               {'kp_match': 'lsk@hstw.net', 'role': '官网对外邮箱 = 抄送' + TAG},
               {'add_kp': {'name': '우윤학 Woo Yoon-hak', 'role': '대표이사 ㈜혜성테크윈 HYESUNG TECHWIN Co., Ltd.（hyesungtechwin.com）= 拍板人' + TAG, 'email': '', 'source': 'http://hyesungtechwin.com/about/about2.php'}},
               {'facts': {'legal_name': '㈜혜성테크윈 HYESUNG TECHWIN Co., Ltd.（사업자등록번호 491-88-01315；경기도 성남시 중원구 사기막골로 99, 성남센트럴비즈타워2차 B동 1508–1510호；情报通信工事业 / 工厂登记 / 直接生产确认 2018-12；商标 40-1827358；自有标工业光交换机 HSTW-IEL-6800M；나라장터 MAS）', 'founded': '2018-11-05' + TAG,
                          'other': '第 115 批：自有标工业光交换机 + 公共采购 MAS 渠道、Director 为 KP → **贴标 OEM 30% B，一页纸一次（对位 HSTW-IEL-6800M 的 STI-288DGGPM / STI-488DGGPM + STI-0240GE 阶梯价 + 自编货号 / 中性包装 / 付费样机；bypass 明说没有；KC 由其自办；Kang In-Su 直呼、抄 lsk@）**；回信 → 次候选；不投标 MAS / 政府项目' + KR + TAG}}],
    'SB-940': [{'kp_match': 'tcsong@cominet.co.kr', 'name': 'Song Tae-jin（송태진；推定同人）', 'role': 'President, Cominet Corp.（tradekorea 公司页）= 拍板人 / 收件人' + TAG},
               {'facts': {'legal_name': 'Cominet Corp.（190-1 Sangdaewon-dong, Jungwon-gu, Seongnam；+82-31-776-2877；光视频链路 / 光中继 / 交换机 / 热像仪；主销 UAE / 伊朗 / 马来西亚 / 沙特 / 泰国；1–50 人；사업자등록번호 两查未取）', 'founded': '≤2000' + TAG,
                          'other': '第 115 批：光传输小厂、出口中东 / 东南亚、KP 推定为 President → **配套 25% B small，一页纸一次（与光链路 / 热像仪成套出口的 STC-228GP / STC-2224GP + STI-154GP / STI-288DGGPM + 贴 Cominet 标可谈 30%、MOQ 1、付费样机；收 tcsong@ 称 Mr. Song）**；再无回声 → 不动；伊朗转售不问不答、只交 FOB 深圳；部分坐实、只做预付' + KR + TAG}}],
    'SB-557': [{'add_kp': {'name': '정현욱 Jung Hyun-wook', 'role': '대표이사 UBITRON Co., Ltd. 유비트론（ubitron.co.kr / jobkorea）= 拍板人（研究档无具名 KP → 收件 ubitron@ 称 Mr. Jung）' + TAG, 'email': '', 'source': 'https://ubitron.co.kr/kr/company/history.php'}},
               {'facts': {'legal_name': 'UBITRON Co., Ltd. 유비트론（사업자등록번호 138-81-55769；통신판매 제2021-강원춘천-0464호；강원도 춘천시 신북로 61-14, 강원테크노파크 204·205호；7 人；자본금 2.24억；매출 2025 18.2억원；CCTV / 计算机外设制造 + 影像安防 / 智能工厂集成（三星 SDI 海外厂、现代 Mobis、军方项目））', 'founded': '2009-10-25' + TAG,
                          'other': '第 115 批：工厂 CCTV / 智能工厂项目集成商（在用 ONV 工业 FS）→ **集成 25% B small，一页纸一次（工厂 CCTV 骨干 STI-288DGGPM / STI-488DGGPM + 汇聚 STC-4424GCPM + 3 年保 / 付费样机；不点名 ONV；收 ubitron@ 称 Mr. Jung）**；军方 / 潜艇项目不提；营收下滑 → 只做预付' + KR + TAG}}],
    'SB-957': [{'add_kp': {'name': '김영일 Kim Young-il', 'role': '대표 써보테크TS(주) Servo-Tech TS Co., Ltd.（servo-tech.co.kr 页脚）= 拍板人（研究档无具名 KP → 收件 sales@ 称 Mr. Kim）' + TAG, 'email': 'sales@servo-tech.co.kr', 'source': 'https://www.servo-tech.co.kr/'}},
               {'facts': {'legal_name': '써보테크TS(주) Servo-Tech TS Co., Ltd.（사업자등록번호 130-86-06691；경기도 광명시 새빛공원로 67, 광명자이타워 B동 409–411호；三菱 / Apex / Weidmüller / Alpha Robotics 特约店；设立 / 规模未取）', 'founded': '未取' + TAG,
                          'other': '第 115 批：自动化元器件分销、无网络线 → **分销 20% B small，一页纸一次（配 PLC / 伺服柜的 DIN 导轨工业交换机 STI-054GP / STI-144GP / STI-154GP + 管理 STI-288DGGPM、宽温、3 年保、MOQ 1、付费样机；不点名 Weidmüller；收 sales@ 称 Mr. Kim）**；再无回声 → 不动' + KR + TAG}}],
    'SB-961': [{'add_kp': {'name': '정기조 Jung Ki-jo', 'role': '대표 팩토스 FACTOS / TOP-FA（个人事业者；top-fa.com）— 不动' + TAG, 'email': 'master@factos.co.kr', 'source': 'http://www.top-fa.com/sub11.php'}},
               {'facts': {'legal_name': '팩토스 FACTOS / TOP-FA（个人事业者 사업자등록번호 708-35-00450；통신판매 2019-안양동안-1270；경기도 안양시 동안구 엘에스로116번길 25-32, 안양 SK V1 센터 1003호；工业自动化网店：工业电脑 / 采集 / 视觉 / 通信模块、ICP DAS）', 'founded': '2019' + TAG,
                          'other': '第 115 批：个体自动化网店（串口 / 采集为主、非 PoE 专营）+ 23 次 0 回复 → **不动（B 保留；自来询盘按一口价 + T/T 预付）**' + TAG}}],
    'SB-962': [{'add_kp': {'name': '송광호 Song Kwang-ho', 'role': '대표 트리플네트웍스(주) Triple Networks Co., Ltd.（triplenet.co.kr 页脚）— 业务不明，不动' + TAG, 'email': '', 'source': 'http://www.triplenet.co.kr/'}},
               {'facts': {'legal_name': '트리플네트웍스(주) Triple Networks Co., Ltd.（사업장번호 138-81-53140；경기도 안양시 동안구 관양동 883, 에이스평촌타워 512호；官网停更（公告 2013 / © 2020）；业务不明，邮箱前缀 HRIS）', 'founded': '未取' + TAG,
                          'other': '第 115 批：业务不明 + 官网停更 + 无 KP + 23 次 0 回复 → **不动（B 保留）**' + TAG}}],
    'SB-963': [{'add_kp': {'name': '손창환 Son Chang-hwan', 'role': '대표 주식회사 유니텔 UNITEL Co., Ltd.（bizno）— 非主业，不动' + TAG, 'email': '', 'source': 'https://bizno.net/article/1388180123'}},
               {'facts': {'legal_name': '주식회사 유니텔 UNITEL Co., Ltd.（사업자등록번호 138-81-80123；법인등록번호 134111-0229638；031-389-1660；7 人；通信 / 广播设备批发，主要产品协议分析仪；地址未取）', 'founded': '2013-01-01（登记）' + TAG,
                          'other': '第 115 批：协议分析仪批发为主、交换机非主业、无 KP + 23 次 0 回复 → **不动（B 保留）**' + TAG}}],
    'SB-966': [{'add_kp': {'name': '윤지현 Yun Ji-hyeon', 'role': '대표이사 (주)뷰텔 VIEWTEL Co., Ltd.（DART / view-tel.co.kr）— 非目标行业，不动' + TAG, 'email': 'marketing@view-tel.co.kr', 'source': 'https://englishdart.fss.or.kr/dsbc001/selectPopup.ax?selectKey=01694903'}},
               {'facts': {'legal_name': '(주)뷰텔 VIEWTEL Co., Ltd.（사업자등록번호 214-87-56744；법인등록번호 110111-3053511；경기도 성남시 중원구 둔촌대로 484, 시콕스타워 508–510호；Wi-Fi 测试仪 / WLAN 放大器制造 벤처；DART 登记非上市）', 'founded': '2004-07-21' + TAG,
                          'other': '第 115 批：Wi-Fi 测试仪器厂、交换机非主业、无 KP + 22 次 0 回复 → **非目标行业，不动（B 保留）**' + TAG}}],
    'SB-509': [{'kp_match': 'cjkim@ione.kr', 'role': '研究档「CEO Kim」（ione.kr）— 与 ionetech.com 主体（(주)아이원테크놀러지 대표 황동현）不符，身份不清，不动' + TAG},
               {'facts': {'legal_name': '未坐实（ionetech.com = (주)아이원테크놀러지 iOne Technology；사업자번호 113-86-34135；대표 황동현；서울 구로구 구로3동 1128-4 HK-Tower 817；IT 方案 / 备份 — 代表非 Kim，与 KP 域 ione.kr 对应关系未证）', 'founded': '未取' + TAG,
                          'other': '第 115 批：域名主体与 KP 身份不符（误归属嫌疑）+ 19 次 0 回复 → **不动（B 保留；对方自来再核 ione.kr 主体）**' + TAG}}],
    'SB-637': [{'kp_match': 'korino77@naver.com', 'role': 'Sales Director, NaSys Inc.（Naver 邮箱）— 35 次 0 回复，不动' + TAG},
               {'add_kp': {'name': '양승희 Yang Seung-hee', 'role': '대표 나시스 주식회사 NaSys Inc.（nasys.kr）— 不动' + TAG, 'email': '', 'source': 'http://nasys.kr/web/company.html'}},
               {'facts': {'legal_name': '나시스 주식회사 NaSys Inc.（27, Dunchon-daero 457beon-gil, Jungwon-gu, Seongnam；070-8221-9264；广播编码器 / 转码器 / IP 广播设备开发制造；벤처 + 工厂 + 贸易业登记 2013；사업자등록번호 两查未取）', 'founded': '2013-01-02' + TAG,
                          'other': '第 115 批：广播设备厂的项目型询价、35 次 0 回复 → **多次 0 回复规则：不动（B 保留；自来询盘按 STI-288DGGPM + STC-2216GP 一口价 + T/T 预付报）**；部分坐实' + TAG}}],
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
