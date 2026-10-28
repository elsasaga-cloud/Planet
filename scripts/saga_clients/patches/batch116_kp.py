#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 116 批（T29-U109，公司底数第三十四轮 · 韩国 B 池收尾 4 户 + 台湾 B 池 23 户 + 新加坡 B 池前 13 户 = 40 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 事实 补写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=116 行）。
结构同 batch115_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：升 A 候选 · 一页纸一次 4（SB-087 阿斯門亞洲 53733622 德國 DIGITUS 亞洲採購辦 貼標 30% / SB-249 網脈 Netberg 42648064 DC 白牌方案商 CENTEC STH 補位 貼標 30% / SB-330 Omni-Comm 198803797H 38 年分銷 + 越南 已貼自 logo 貼標 30% / SB-776 Fida Int'l PROLiNK 199101937H 35 年品牌 三地址活 貼標 30%）；
一页纸一次 · 贴标 OEM 30% 13（SB-138 定揚 Volktek 明確 OEM 工業 L2/L3 / SB-820 PRISM = 普羅通信 Browan Wi-Fi 品牌 配套 PoE / SB-715 Netsys 延長器廠 交換機非核心 / SB-947 ISON 24728059 工業品牌 外購 Edgecore 機型 / SB-019 高譽 AETEK PoE 品牌 PM 曾言「便宜方案找 Saga」/ SB-812 Ethernet Direct 北美工業品牌 / SB-952 名翔 MSTronic 23804228 PoE 配件廠 / SB-083 利凌 LILIN 36165005 攝影機品牌 KP 要貼 logo / SB-084 艾德 AD-NET 27843840 深圳拿貨小品牌 / SB-088 訊舟 EDIMAX 22164580 上市 採購 PM 回 INFO 工業線外購 / SB-089 Winsonic 工控機廠 現供 UniPoE 未坐實 / SB-708 Hyconext 純品牌 招分銷 / SB-697 Allied Asia ATZ 品牌 現供 ONV）；
一页纸一次 · 分销 20% 4（SB-070 네오와인 芯片 CEO 想做代理 / SB-839 譯麓 iLu 貿易 總裁親問 8 口 PoE / SB-1035 GPON Network 身份不清 預付 Simon「可多跟進」/ SB-937 Anewtech 199903145E 工業 PC 三國辦公室 在供 ORing）；一页纸一次 · 集成商 25% 1（SB-1050 Keydence 201019151W CCTV 集成）；
不动 14（SB-953 네몬 bypass 專營 微型 / SB-032 파이오링크 119-81-41089 上市同行 ODM 線 Simon 微信 / SB-909 대진네트웍스 Centec 原廠渠道 + 退信 / SB-710 KTI 1983 自研品牌 同行 / SB-946 嚮樂 Intrising 53116727 工業 L3 自研 同行 / SB-702 康聯訊 CTS 16744506 上櫃 同行 / SB-086 台林 Tailyn 12278439 上櫃 自產 ODM 同行 / SB-438 主向位 CTC Union 84297462 自研 同行 / SB-933 鑫志 AirLive 53110625 19×0 / SB-500 CET Electric 201523201G 中資電力計量分支 15×0 / SB-506 Fibertek 17×0 無 KP 已有國內貨源 / SB-797 Excel Engineering 201332361M 實繳 S$1,000 虛擬地址 / SB-945 Grep Tech 軟體 行業外 15×0 / SB-719 Trioms 201131509H 儀器分銷 非目標）；
并线 4（SB-1112 占位行 = SB-839 Styven Tseng 來信 → SB-839 / SB-804 bm-switch = Netberg 分部 → SB-249 / SB-800 Acelink = 訊舟同址 ODM 分部 → SB-088 / SB-346 ATZ = Allied Asia 商標 → SB-697）；
坐实 22（SB-032 / 946 / 947 / 702 / 952 / 083 / 084 / 086 / 087 / 088 / 438 / 933 / 249 / 804 / 500 / 330 / 776 / 1050 / 797 / 719 / 937 / 346）/ 部分坐实 15（SB-953 / 070 / 909 / 138 / 710 / 820 / 715 / 019 / 839 / 800 / 506 / 708 / 697 / 945 / 1035）/ 未坐实 2（SB-812 / 089）/ 0 查 1（SB-1112）；
KP 坐实 = 代表 / 老板本人 4（SB-070 이효승 = John H. Lee / SB-839 Angus Tseng President / SB-945 Robin Luo Founder / SB-249 Alexander Ustyuzhanin Director（代表人另為 約理師））；补代表 / 负责人 add_kp 14；补邮箱 1（SB-697 Kelvin Tan kelvin.tan@）；KP 更正 1（SB-839 Styven Tseng 邮箱 → 併記 styvent@gmail.com 來信地址）；
法定名补全 / 更正 29；country_fix 0（SB-330 omninet.com.vn 僅為越南側默認頁，HQ 新加坡 UEN 198803797H 確認 → iso SG 不動）。
TW 检索路径实测：「中文名 / 英文名 + 統一編號」1 查 → twincn / twfile / opengovtw / findit / aibee / alphaloan 皆回 統編 + 代表人 + 設立日 + 資本額 + 工廠登記；猜中文名易誤中同名（鉅康 ≠ Volktek、光紅建聖 ≠ KTI）→ 先用 英文名 + 域名；國貿局英文名未索引者（Volktek / KTI / Netsys / AETEK / Winsonic）統編取不到 → 部分 / 未坐實。
SG 检索路径实测（首次）：「英文名 + Pte Ltd + UEN」1 查 → recordowl（UEN + 注册日 + 类型 + 曾用名 + 实缴 + 抵押 + 年报）/ sgpbusiness（UEN + 地址 + 域名注册人）/ sg.ltddir（UEN + SSIC + 高管数）/ bizapore；官网页脚 Reg/GST No. 亦可（trioms）；品牌 ≠ 法人名时先找法人名（PROLiNK → Fida Int'l；Omnicomm → Omni-Comm）。
旁线索（≠ 目标，另立户评估）：주식회사 네모 404-81-41274 / 네모온（SB-953 同名）；鉅康科技 NETVOX 96856329 / 勝康科技（SB-138 同名）；光紅建聖 EZconn 97119975（SB-710 同名）；英特力國際（SB-946 同名）；Browan 普羅通信（SB-820 母體）；Daejin Semiconductor（SB-909 關聯）；環隆科技 / 世譽先進（SB-702 法人股東）；AETEK 連城路192-1號 與 Volktek 192號 相鄰 → 姊妹品牌（推定）；Velocity Technology Industries / Fiberlan（SB-506 同樓）；EcoXplore（SB-500 夥伴）；Hungsway 澳洲（SB-839 關聯）；GREP ADVISORY 202411162K（SB-945 同名他企）；ANEWTECH PTE. LTD.（SB-937 同名他企）。
Simon 待决（累计见 PR-02-53 追记）：升 A 候选 SB-087 / 249 / 330 / 776（回信即升）；SB-032 PIOLINK ODM 線走 Simon 微信；2.5G 口径（SB-708 Hyconext 2.5G 主推 → 待 SB-263）；SB-138 / 019 Volktek–AETEK 兩戶一線由誰收（建議 Karen 先）。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 116 批 官方登记核实 2026-10-28）'
KR = '— 韩国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳、KC 不声称'
TW = '— 台灣常規：英文稿、20 / 25 / 30 + T/T 預付 + FOB 深圳、BSMI 不聲稱'
SG = '— 新加坡常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳、IMDA 不声称'
UPD = {
    # ───────── KR 收尾 4 ─────────
    'SB-953': [{'add_kp': {'name': '조주철 Cho Ju-cheol', 'email': '', 'role': '대표 / 拍板人（jobkorea；support@ 無具名 KP）— 不動，不發' + TAG, 'source': 'jobkorea.co.kr/recruit/co_read/c/nemon0701'}},
               {'facts': {'legal_name': '(주)네몬 Nemon Co., Ltd.（사업자등록번호 未取；벤처 2017-06 / 기업부설연구소 2017-11）', 'founded': '2016-07-01' + TAG, 'hq': '경기 수원시 영통구 법조로 25, 광교SK뷰레이크타워 A동 2514호（2019-12 自城南遷入）' + TAG, 'size': '4–6 人；자본금 5,000만' + TAG,
                          'other': '第 116 批：bypass / TAP 網安交換機專營（Saga 無此線）+ 微型 + 無 KP + 23 次 0 回覆 → **不動（B 保留）**；部分坐实（求職站）' + TAG}}],
    'SB-032': [{'kp_match': 'gooleebiz@gmail.com', 'role': 'GM, Piolink, Inc.（KOSDAQ 170790；119-81-41089；414 人）— 同行上市交換機廠；ODM / 代工線僅經 Simon 微信直聯，不進群發' + TAG},
               {'add_kp': {'name': '조영철 Cho Young-chul', 'email': '', 'role': '대표이사（bizno + 官網；上市公司代表）— 不發' + TAG, 'source': 'https://www.piolink.com/kr/company/Company-Overview.php'}},
               {'facts': {'legal_name': '주식회사 파이오링크 Piolink, Inc.（사업자등록번호 119-81-41089；법인등록번호 110111-2035578；KOSDAQ 170790 2013-08）', 'founded': '2000-07-26' + TAG, 'hq': '서울 금천구 가산디지털2로 98, IT캐슬 1동 401호 08506（02-2025-6900）' + TAG, 'size': '414 人；國內 ADC 第一；日本分公司' + TAG,
                          'other': '第 116 批：上市 ADC / TiFRONT 安全交換機廠 = **同行，不動群發**；其所要（Realtek 高端方案 / 24 光口 ODM）由 Simon 微信單獨定；守界：不給成本結構、不轉介供應商' + TAG}}],
    'SB-070': [{'kp_match': 'godinus@neowine.com', 'role': 'CEO / 대표이사（= 登記代表 이효승 Lee Hyo-seung，jobkorea；设立 2002-06-04；20 人；매출 ≈25억）= 拍板人 / 收件人 — 一頁紙一次：分銷 20%、非獨家、MOQ 1、48 口付費樣機（STC-448XGGPM）、英文' + KR + TAG},
               {'kp_match': 'dexter@neowine.com', 'role': 'Director（研究档）= 抄送' + TAG},
               {'facts': {'legal_name': '㈜네오와인 Neowine Co., Ltd.（사업자등록번호 未取；벤처；ISO 9001 / 14001）', 'founded': '2002-06-04' + TAG, 'hq': '경기 성남시 분당구 판교역로 182, 한국반도체산업협회 4층' + TAG, 'size': '20 人；자본금 5억；매출 ≈25억원' + TAG,
                          'other': '第 116 批：Fabless 安全芯片商（行業外），CEO 本人想做代理 → **分銷 20% B small，一頁紙一次**；再無回聲 → 不動；部分坐实（求職站）' + TAG}}],
    'SB-909': [{'add_kp': {'name': '이수봉 Lee Soo-bong', 'email': '', 'role': 'CEO（官網；设立 2021-01-18）— 不動，不發（info / sales 均退信 = 地址失效）' + TAG, 'source': 'https://www.daejinnetworks.com/en'}},
               {'facts': {'legal_name': '대진네트웍스 Daejin Networks（사업자등록번호 未取；대진반도체 Daejin Semiconductor 關聯）', 'founded': '2021-01-18' + TAG, 'hq': '서울 금천구 벚꽃로 278, SJ테크노빌 1207호 08511（1588-9809）' + TAG, 'size': '小型（2021 新設）' + TAG,
                          'other': '第 116 批：Centec 交換機（V/E 系列）+ HiSilicon 光模塊 韓國分銷 = **CENTEC 原廠渠道 同線競對 + 郵箱全退信 → 不動（B 保留；地址失效）**；守界：不向 Centec 渠道報 STH 價' + TAG}}],
    # ───────── TW 23 ─────────
    'SB-138': [{'kp_match': 'karen.hua@volktek.com', 'role': '業務專員（皮凱太）= 收件人 — 一頁紙一次：貼標 OEM 30%，只給其自產線之外的成本型工業管理機 STI-288DGGPM / STI-488DGGPM / STI-0240GE + 自編貨號 / 中性包裝 / 付費樣機；bypass 明說沒有' + TW + TAG},
               {'kp_match': 'joseph.pi@volktek.com', 'role': '研究档联系人 = 抄送' + TAG},
               {'facts': {'legal_name': '定揚科技股份有限公司 Volktek Corp.（統一編號 未取；1994 年成立）', 'founded': '1994' + TAG, 'hq': '新北市中和區連城路192號4樓（總部）/ 苗栗縣竹南鎮國泰路17-1號（廠）' + TAG, 'size': '51–200 人；自有 SMT / DIP 產線' + TAG,
                          'other': '第 116 批：台系工業交換機品牌廠（同行）但明確想 OEM 工業 L2/L3 → **以 OEM 採購方計：貼標 OEM 30% B，一頁紙一次**；與 AETEK（SB-019，連城路192-1號）姊妹品牌 → 兩戶一線；守界：不給成本結構；統編未取 → 只做預付' + TAG}}],
    'SB-710': {'facts': {'legal_name': 'KTI Networks Inc.（統一編號 未取；1983 年成立；Houston 分公司 + KTI South Europe）', 'founded': '1983' + TAG, 'hq': '15F-7, No. 79, Sec. 1, Hsin Tai Wu Rd., Xizhi Dist., New Taipei City（+886 2 2698 3878）' + TAG, 'size': '中小（海外分支）' + TAG,
                         'other': '第 116 批：自研自產品牌廠（北美 / 歐洲 / 日本自有通路）= **同行，無 OEM 訊號 + 9 次 0 回覆 → 不動（B 保留）**；部分坐实' + TAG}},
    'SB-820': {'facts': {'legal_name': 'PRISM = 普羅通信 Browan Communications Inc. 2022 年推出的企業無線品牌（統編 未取）', 'founded': '1999 / 2002（普羅通信）；品牌 2022' + TAG, 'hq': '未取（台灣；普羅通信 新竹 推定）' + TAG, 'size': '未取' + TAG,
                         'other': '第 116 批：Wi-Fi 品牌、PoE 交換機 MS8P8 / MS12P8 / MS18P16 / MS28P24 / MS52P48 為配套（推定外購）→ **貼標 OEM 30% B，一頁紙一次**（對位 STC-028GP / 228GP / 2216GP / 2224GP / 4424GCPM / 448XGGPM 階梯 + PRISM 標 + 付費樣機；收 sales@）；回信 → 加厚；部分坐实' + TW + TAG}},
    'SB-946': [{'kp_match': 'kenlee@intrising.com.tw', 'role': '官網聯絡信箱持有人（疑 = 代表人 李金璋）— 同行，不動' + TAG},
               {'add_kp': {'name': '李金璋', 'email': '', 'role': '代表人（twfile；統編 53116727）— 不發' + TAG, 'source': 'twfile.com 嚮樂科技股份有限公司 53116727'}},
               {'facts': {'legal_name': '嚮樂科技股份有限公司 INTRISING NETWORKS, INC.（統一編號 53116727；國貿局 2015-06-02；ISO 9001:2015）', 'founded': '≤2015' + TAG, 'hq': '臺北市南港區園區街3號14樓之6（02-2790-6867）' + TAG, 'size': '小型' + TAG,
                          'other': '第 116 批：自研工業 L3 / IEC 61850 / TSN 交換機品牌 = **同行，19 次 0 回覆 → 不動（B 保留）**；坐实' + TAG}}],
    'SB-715': {'facts': {'legal_name': 'National Enhance Technology Corp.（Netsys；統一編號 未取）', 'founded': '1999-06' + TAG, 'hq': '9F, No. 208, Sec. 3, Datong Rd., Xizhi Dist., New Taipei City 221（+886-2-6616-2880）' + TAG, 'size': '11–50 人' + TAG,
                         'other': '第 116 批：VDSL2 延長器 / MC 品牌廠、交換機非核心（推定外購）→ **貼標 OEM 30% B small，一頁紙一次**（STC-228GP / STC-2224GP + STI-154GP / STI-288DGGPM + Netsys 標；MC / 延長器明說不做；收 sales@，ContactOut 業務名單 Jason Kung AM 可補）；再無回聲 → 不動；部分坐实' + TW + TAG}},
    'SB-947': {'facts': {'legal_name': 'ISON Technology Co., Ltd.（統一編號 24728059；實收資本額 NT$40,619,030；Active）', 'founded': '2015' + TAG, 'hq': '桃園市（詳址未取）' + TAG, 'size': '小型' + TAG,
                         'other': '第 116 批：工業網路品牌「Industrial Solution Over Network」、站內含 Edgecore 機型 ECS4150-54P = 外購貼牌 → **貼標 OEM 30% B，一頁紙一次**（STI-154GP / 288DGGPM / 488DGGPM / 0240GE + STC-2224GP / 4424GCPM + ISON 標；電力 61850 / 鐵路 EN 50155 明說不做；收 sales@）；回信 → 加厚；坐实' + TW + TAG}},
    'SB-019': [{'kp_match': 'jone.chen@aetektec.com', 'name': 'Jone (John) Chen', 'role': 'Product Manager（ZoomInfo）= 收件人 — 一頁紙一次：貼標 OEM 30%，對位其「2 光 10 電」的 STC-228GP / STC-2216GP + 管理機 STC-4424GCPM 一口價 + AETEK 標 + 付費樣機；NDAA / TAA 明說無法聲稱' + TW + TAG},
               {'add_kp': {'name': '李慧玉', 'email': '', 'role': 'asmag 供應商頁聯絡人（高譽科技）— 備用' + TAG, 'source': 'asmag.com.tw 供應商 高譽科技股份有限公司'}},
               {'facts': {'legal_name': '高譽科技股份有限公司 AETEK Inc.（統一編號 未取）', 'founded': '未取' + TAG, 'hq': '6F, No. 192-1, Lien-Cheng Rd., Zhonghe Dist., New Taipei City 235（+886-2-8245-2822；舊址 五股區五工三路106巷3號）' + TAG, 'size': '11–50 人' + TAG,
                          'other': '第 116 批：PoE 專業品牌、PM 曾言「便宜方案可找 Saga / 他們軟體 + Saga 硬體」→ **貼標 OEM 30% B，一頁紙一次**；與 Volktek（SB-138，連城路192號）同集團推定 → 兩戶一線、不重複報價；守界：不提 NDAA / TAA / UL；部分坐实' + TAG}}],
    'SB-702': [{'kp_match': 'koichi_ito@ctsystem.com', 'role': '研究档 KP（已加微信）— 上櫃同行，不動群發；有需求對方會來' + TAG},
               {'add_kp': {'name': '陳友信', 'email': '', 'role': '董事長 / 總經理（twincn；上櫃 3672；統編 16744506）— 不發' + TAG, 'source': 'https://twincn.com/item.aspx?no=16744506'}},
               {'facts': {'legal_name': '康聯訊科技股份有限公司 Connection Technology Systems Inc.（CTS；統一編號 16744506；TPEx 3672；資本額 NT$407,903,750）', 'founded': '1998-10-06' + TAG, 'hq': '新北市汐止區新台五路一段79號18F-6（廠 16F-6 生產中；02-2698-9661）' + TAG, 'size': '中型（上櫃；法人股東 環隆科技 / 世譽先進）' + TAG,
                          'other': '第 116 批：上櫃自研自產光通訊 / 工業 PoE 交換機廠 = **同行，8 次 0 回覆 → 不動群發（B 保留）**；坐实' + TAG}}],
    'SB-812': {'facts': {'legal_name': 'Ethernet Direct Corporation（美國 NY 銷售 / CA 物流；GSA 核准公司；台灣站 ethernetdirect-tw.com；統編 / 實體 未取）', 'founded': '≥2005（2015 自述「over a decade」）' + TAG, 'hq': '未取（台灣聯絡站；美國 NY / CA）' + TAG, 'size': '小型' + TAG,
                         'other': '第 116 批：工業品牌商（Cobra 系列；推定 ODM 外購、北美通路）→ **貼標 OEM 30% B small，一頁紙一次**（STI-154GP / 288DGGPM / 488DGGPM 寬溫 PoE+ + 自編貨號 + 付費樣機；GSA / NDAA 明說無法聲稱；收 sales@）；再無回聲 → 不動；未坐实 → 只做預付' + TW + TAG}},
    'SB-952': [{'kp_match': 'arthur@mse.com.tw', 'role': '研究档 KP = 收件人 — 一頁紙一次：貼標 OEM 30%，補其 PoE 交換機線 STC-028GP / STC-228GP / STC-2224GP + 工業 STI-154GP / STI-288DGGPM + MSE 標 + 付費樣機；EN 50155 / EN 60945 / IP67 明說不做' + TW + TAG},
               {'facts': {'legal_name': '名翔電子有限公司 MSTronic Co., Ltd.（統一編號 23804228；品牌 MSE）', 'founded': '未取' + TAG, 'hq': '未取（+886-2-2293-0159 → 新北五股 / 新莊一帶；英國 +44 7522 399644）' + TAG, 'size': '小型' + TAG,
                          'other': '第 116 批：PoE 注入器 / 分離器 / 24VAC / DIN / 太陽能 PoE 自產（Made in Taiwan），交換機為配套線（推定外購）→ **貼標 OEM 30% B small，一頁紙一次**；再無回聲 → 不動；坐实（頁腳統編）' + TAG}}],
    'SB-083': [{'kp_match': 'ginahsu@meritlilin.com.tw', 'role': '採購 / 產品（表內：周邊要貼 LILIN logo）= 收件人 — 一頁紙一次：貼標 OEM 30%，攝影機配套 PoE 階梯 STC-028GP / 228GP / 2216GP / 2224GP + 工業 STI-154GP + LILIN 標 / 自編貨號 / 付費樣機；MC 只有 STC-110XGE、SFP 不做' + TW + TAG},
               {'add_kp': {'name': '許正忠', 'email': '', 'role': '代表人 / 董事長（twincn；統編 36165005；家族董監 許家雄 / 許家銘 / 許瑞文）— 拍板人，不直發' + TAG, 'source': 'https://twincn.com/item.aspx?no=36165005'}},
               {'facts': {'legal_name': '利凌企業股份有限公司 MERIT LILIN ENT. CO., LTD.（統一編號 36165005；資本總額 NT$120,000,000；工廠登記 99618299 同址）', 'founded': '1983-09-01' + TAG, 'hq': '新北市五股區五工六路20號（02-2298-8988）' + TAG, 'size': '中小（家族企業；自有工廠）' + TAG,
                          'other': '第 116 批：攝影機品牌、KP 明說周邊貼 LILIN logo → **貼標 OEM 30% B，一頁紙一次**；回信 → 加厚；坐实' + TAG}}],
    'SB-084': [{'kp_match': 'robin@ad-net.com.tw', 'role': '研究档 KP（2025-09 回「M12 Switch??」）= 收件人 — 一頁紙一次：貼標 OEM 30%，非 M12 工業線 STI-154GP / 288DGGPM / 488DGGPM / 0240GE + STC-228GP / 2224GP + AD-NET 標；M12 / E1 / GEPON / 光模組 明說不做' + TW + TAG},
               {'add_kp': {'name': '羅惠玲', 'email': '', 'role': '代表人 / 唯一董事（twincn；統編 27843840）— 拍板人' + TAG, 'source': 'https://www.twincn.com/item.aspx?no=27843840'}},
               {'facts': {'legal_name': '艾德科技有限公司 AD-NET TECHNOLOGY CO., LTD.（統一編號 27843840；商標 AD-NET 及圖 01258240 至 2027-04-15）', 'founded': '2005-07-14' + TAG, 'hq': '苗栗縣苗栗市福星里國華路210號（037-269585）' + TAG, 'size': '小型（有限公司）' + TAG,
                          'other': '第 116 批：自有商標、深圳拿貨的小型品牌商 → **貼標 OEM 30% B small，一頁紙一次**；再無回聲 → 不動；只做預付；坐实' + TAG}}],
    'SB-086': [{'kp_match': 'garychen@tailyn.com.tw', 'role': '研究档 KP（2025-07 對 Alarm 回 INFO）— 上櫃同行（自產 + ODM），不動群發' + TAG},
               {'kp_match': 'jill@tailyn.com.tw', 'role': '研究档联系人 — 不動' + TAG},
               {'add_kp': {'name': '陳俊廷', 'email': '', 'role': '董事長 / 總經理（twincn；上櫃 5353；統編 12278439）— 不發' + TAG, 'source': 'https://twincn.com/item.aspx?no=12278439'}},
               {'facts': {'legal_name': '台林電通股份有限公司 Tailyn Technologies, Inc.（統一編號 12278439；TPEx 5353；資本總額 NT$1.25B / 實收 NT$750M；工廠同址）', 'founded': '1980-04-10' + TAG, 'hq': '桃園市蘆竹區內厝里榮安路10號（03-322-2201）' + TAG, 'size': '中型（上櫃）' + TAG,
                          'other': '第 116 批：上櫃、自研自產工業 / 商用交換器並承接 ODM = **同行，不動群發（B 保留）**；若其主動詢 OEM 再按 30% 檔單議；坐实' + TAG}}],
    'SB-087': [{'kp_match': 'kent.wang@assmann.com.tw', 'role': 'PM, ASSMANN Electronic Asia（德國 DIGITUS 亞洲採購辦；2025-12 回「I/O modules」）= 收件人 — 一頁紙一次：貼標 OEM 30%，DIGITUS PoE 線對位 STC-028GP / 228GP / 2216GP / 2224GP / 4424GCPM + STC-110XGE 一口價 + DIGITUS 標 / 彩盒 / CE / RoHS / REACH 文件；串口 / HDMI / I/O 模組 明說不做；回信 → 加厚 + 升 A' + TW + TAG},
               {'add_kp': {'name': 'Matthias Christian Listl', 'email': '', 'role': '代表人 / 董事（twincn；統編 53733622；董事另 漆曉燕）— 拍板人，不直發' + TAG, 'source': 'https://twincn.com/item.aspx?no=53733622'}},
               {'facts': {'legal_name': '阿斯門亞洲有限公司 ASSMANN ELECTRONIC ASIA CO. LTD.（統一編號 53733622；資本額 NT$5,000,000；母公司 ASSMANN Electronic GmbH, Lüdenscheid；寧波 / 東莞 / 香港 辦公室）', 'founded': '2012-01-31' + TAG, 'hq': '臺北市內湖區新湖一路77號7樓（02-2793-4088）' + TAG, 'size': '小型（採購辦；集團 歐洲 10 國）' + TAG,
                          'other': '第 116 批：德國 DIGITUS 的亞洲貼牌採購辦 = 歐洲主戰場的源頭採購 → **貼標 OEM 30% B（升 A 候選），一頁紙一次**；守界：UKCA 只對 GB 提、不點名現供應商；坐实' + TAG}}],
    'SB-088': [{'kp_match': 'jessechen@edimax.com.tw', 'role': '採購 / PM（2025-07 對 16 電回 INFO）= 收件人 — 一頁紙一次：貼標 OEM 30%，只給工業線 STI-154GP / 288DGGPM / 488DGGPM / 0240GE + 16 口 PoE STC-2216GP 一口價 + EDIMAX 標 / 自編貨號 / 付費樣機；SFP / 無線 明說不做；守界：同行 不給成本結構' + TW + TAG},
               {'kp_match': 'bruceyang@edimax.com.tw', 'role': '研究档联系人 = 抄送' + TAG},
               {'add_kp': {'name': '任冠生', 'email': '', 'role': '董事長（twfile；上市 3047；統編 22164580；2026-03 代表人變更為 潘良榮）— 不發' + TAG, 'source': 'https://www.twfile.com/item.aspx?no=22164580&sn=2461840'}},
               {'facts': {'legal_name': '訊舟科技股份有限公司 EDIMAX TECHNOLOGY CO., LTD.（統一編號 22164580；TWSE 3047；資本總額 NT$3B / 實收 NT$2,246,491,080；ODM 分部 Acelink Technology = SB-800 同址）', 'founded': '1986-06-28' + TAG, 'hq': '臺北市內湖區新湖一路278號（02-7739-6888；舊址 新北五股 五權三路3號）' + TAG, 'size': '大型（上市；集團 501–1,000）' + TAG,
                          'other': '第 116 批：上市網路品牌（同行）但工業 / PoE 線外購、採購 PM 已回 INFO → **以採購方計：貼標 OEM 30% B，一頁紙一次**；再無回聲 → 不動；與 SB-800 一線；坐实' + TAG}}],
    'SB-089': [{'kp_match': 'rex.lin@ewinsonic.com', 'role': '採購 / 產品（表內：在用 UniPoE 工業 FS；2025-11 對升壓 PoE 回 INFO）= 收件人 — 一頁紙一次：貼標 OEM 30%，對位 UniPoE 的 STI-154GP / STI-288DGGPM / STI-0240GE + Winsonic 標 + 付費樣機；升壓 PoE 明說不做；只做預付' + TW + TAG},
               {'facts': {'legal_name': 'Winsonic Electronics Co., Ltd.（統一編號 1 查未得 → 未坐實；命中 伍仕電子 27966146 / 文聲電子 04348572 均不對應）', 'founded': '未取' + TAG, 'hq': '未取' + TAG, 'size': '未取' + TAG,
                          'other': '第 116 批：工業面板 PC / 工控機廠、工業交換機外購（現供 UniPoE 深圳）→ **貼標 OEM 30% B small，一頁紙一次**；再無回聲 → 不動；未坐实 → 預付；不點名 UniPoE' + TAG}}],
    'SB-438': [{'kp_match': 'micro-chang@ctcu.com.tw', 'role': '研究档 KP（已有回覆）— 自研自產同行，不動群發；若詢 ODM 補位由 Simon 單議' + TAG},
               {'add_kp': {'name': '張靖駭', 'email': '', 'role': '代表人 / 董事長（twincn；統編 84297462）— 不發' + TAG, 'source': 'https://twincn.com/item.aspx?no=84297462'}},
               {'facts': {'legal_name': '主向位科技股份有限公司 CTC UNION TECHNOLOGIES CO., LTD.（統一編號 84297462；資本總額 NT$600M / 實收 NT$322,139,660；曾興櫃 1926，2012-07 暫停發行）', 'founded': '1993-07-19' + TAG, 'hq': '臺北市內湖區洲子街60、62號8、9樓（02-2659-1021）' + TAG, 'size': '中型（全球經銷網）' + TAG,
                          'other': '第 116 批：1993 年起自研自產 L2/L3 / 工業交換機 = **同行，不動群發（B 保留）**；守界：不談 2.5G 口徑、不給成本結構；坐实' + TAG}}],
    'SB-839': [{'kp_match': 'angus@ilucoltd.com', 'role': 'President, iLu Co., Ltd. 譯麓有限公司（官網）= 拍板人 / 收件人 — 一頁紙一次：分銷 20% small，直接答 2024-10 之問：8 口 PoE 非管理 STC-028GP / STC-228GP 一口價，8 口管理型按主表現有型號報；SFP / bypass 模組不做；付費樣機、MOQ 1、預付' + TW + TAG},
               {'kp_match': 'styven@ilucoltd.com', 'role': '2024-10-25 來信人（來信地址 styvent@gmail.com；= SB-1112 占位行 同一來信，已併線）= 抄送' + TAG},
               {'add_kp': {'name': 'Hung Cheng', 'email': '', 'role': '澳洲 Hungsway 聯絡人（官網 sitemap；Lane Cove NSW）— 備用' + TAG, 'source': 'https://www.ilucoltd.com/sitemap/'}},
               {'facts': {'legal_name': '譯麓有限公司 iLu CO., LTD.（統一編號 未取；德國 Teltow 聯絡點 + 澳洲 Hungsway）', 'founded': '未取' + TAG, 'hq': '新北市蘆洲區鹿江街105號 / No. 105, Lujiang St., Luzhou Dist., New Taipei City 24748（+886-2-8286-3598 ext 101）' + TAG, 'size': '微型（總裁親答）' + TAG,
                          'other': '第 116 批：小型貿易商、總裁與家人親自問 8 口扁平 PoE → **分銷 20% B small，一頁紙一次**；再無回聲 → 不動；SB-1112 併線至此；部分坐实' + TAG}}],
    'SB-933': [{'kp_match': 'john.lai@airlive.com', 'role': '研究档 KP — 19 次 0 回覆，不動' + TAG},
               {'add_kp': {'name': '蔡伯坤', 'email': '', 'role': '代表人 / 董事長（twincn；統編 53110625；2020-05 起）— 不發' + TAG, 'source': 'https://www.twincn.com/item.aspx?no=53110625'}},
               {'facts': {'legal_name': '鑫志股份有限公司 AirLive Technology Corporation（統一編號 53110625；資本額 NT$27,000,000；2020-09-28 由 鑫立投資股份有限公司 更名）', 'founded': '2010-11-22（AirLive 品牌承接 2020）' + TAG, 'hq': '新北市新店區寶橋路235巷120號7樓（02-8912-1060）' + TAG, 'size': '小型' + TAG,
                          'other': '第 116 批：2020 年由投資公司殼承接的 AirLive 品牌（外購貼牌推定）、19 次 0 回覆 → **不動（B 保留）**；若其來詢 OEM 按 30% 檔；坐实' + TAG}}],
    'SB-1112': {'facts': {'legal_name': '（占位行）= SB-839 譯麓 iLu 的 Styven Tseng 2024-10-25 來信（逐字相同）→ 併線 SB-839', 'founded': '—' + TAG, 'hq': '—' + TAG, 'size': '—' + TAG,
                          'other': '第 116 批：**併線 SB-839，本行不動、不單發**；0 查' + TAG}},
    'SB-804': {'facts': {'legal_name': 'Bare Metal Switch（bm-switch.com）= 網脈有限公司 Netberg Ltd.（統編 42648064；SB-249）旗下網店分部（官網 about-us 自述；電匯戶名 Netberg Ltd. 玉山銀行）', 'founded': '—（分部）' + TAG, 'hq': '10F, No. 111-3, Xiyuan Rd., Zhongli Dist., Taoyuan City 320（+886-3-260-9203；同 SB-249）' + TAG, 'size': '—' + TAG,
                         'other': '第 116 批：**同一法人的網店分部 → 併線 SB-249，本行不單發**；坐实' + TAG}},
    'SB-800': {'facts': {'legal_name': 'Acelink Technology Co., Ltd.（統編 未單獨取；HQ No. 278, Xinhu 1st Rd., Neihu = 訊舟 EDIMAX 22164580 登記地址；「since 1986」= 訊舟設立年；EW-78xx 型號 = EDIMAX 編碼 → 訊舟集團 ODM 分部 / 關係企業）', 'founded': '1986（集團口徑）' + TAG, 'hq': 'No. 278, Xinhu 1st Rd., Neihu Dist., Taipei City（同 SB-088）' + TAG, 'size': '大型（集團 501–1,000；ODM Sales Division Eunice Lu）' + TAG,
                         'other': '第 116 批：**訊舟集團 ODM 分部 → 併線 SB-088，一線一稿（Jesse Chen 線），本行不單發**；部分坐实' + TAG}},
    'SB-249': [{'kp_match': 'au@netbergtw.com', 'role': 'Director, Netberg Ltd. 網脈有限公司（登記代表人另為 約理師；已回覆 1 次）= 收件人 — 一頁紙一次：貼標 OEM 30%，CENTEC 平台 STH-2C24XF-HSI $1,500 / STH-8C48DX-HSI $4,800 / STH-32C-HSI $6,000 作其 Broadcom 線之外的成本型補位 + Netberg 標 + 付費樣機；NOS 只答「可提供軟體清單」不聲稱 SONiC / ONIE；opener 引其上次回覆；回信 → 加厚 + 升 A' + TW + TAG},
               {'add_kp': {'name': '約理師', 'email': '', 'role': '代表人 / 董事 / 經理人（twincn；統編 42648064；外籍）— 不直發' + TAG, 'source': 'https://twincn.com/item.aspx?no=42648064'}},
               {'facts': {'legal_name': '網脈有限公司 NETBERG LTD.（統一編號 42648064；國貿局 2015-10-12；網店分部 Bare Metal Switch = SB-804）', 'founded': '2015-10-02' + TAG, 'hq': '桃園市中壢區西園路111之3號10樓（03-260-9203；2022-12 自 臺北市信義區光復南路419號5樓之1 遷入）' + TAG, 'size': '小型（有限公司）' + TAG,
                          'other': '第 116 批：不自產、靠 ODM 夥伴出白牌 DC 交換機的方案商（Broadcom 線）= DC 交換機客戶（Simon 優先類）→ **貼標 OEM 30% B（升 A 候選），一頁紙一次**；守界：不談 Broadcom 對標、不報成本結構；只做預付；與 SB-804 一線；坐实' + TAG}}],
    # ───────── SG 13 ─────────
    'SB-500': {'facts': {'legal_name': 'CET Electric Technology Pte. Ltd.（UEN 201523201G；Exempt Private Company Limited By Shares；曾用名 Ceiec Electric Technology Singapore = 中電 CET 集團分支；年報 2026-07-23 已報）', 'founded': '2015-05-15' + TAG, 'hq': '7 Mandai Link #05-33 Mandai Connection, Singapore 728653（+65 6677 7279；2024-12 自 1 Corporation Drive #09-02 遷入）' + TAG, 'size': '小型（集團分支）' + TAG,
                         'other': '第 116 批：中資電力計量集團的新加坡分支（電能表 / 電能質量 / 串口網關 PMC-1308），工業交換機由集團內部配套、15 次 0 回覆、電力計量屬守界邊緣 → **不動（B 保留）**；坐实' + TAG}},
    'SB-506': {'facts': {'legal_name': 'Fibertek Pte Ltd（sgpbusiness 同址索引 FIBERTEK PTE LTD；UEN 1 查未得）', 'founded': '未取' + TAG, 'hq': '3015A Ubi Road 1, Singapore（樓層未取；與 Velocity Technology Industries / Fiberlan 同樓）' + TAG, 'size': '未取' + TAG,
                         'other': '第 116 批：已直接從國內拿貨的小品牌（SFP / 光貓為主）、無 KP、17 次 0 回覆、主體未坐實 → **不動（B 保留）**；部分坐实' + TAG}},
    'SB-708': {'facts': {'legal_name': 'Hyconext（法人名 / UEN 未取；Singapore HQ + 美國 City of Industry, CA 辦公室）', 'founded': '未取' + TAG, 'hq': '128 Tanjong Pagar Road, Singapore 088535（美國 1170 Centre Dr #F, City of Industry, CA 91789）' + TAG, 'size': '小型' + TAG,
                         'other': '第 116 批：純品牌方（PoE / 2.5G NextWav / DC 交換機 外購，全球招分銷）→ **貼標 OEM 30% B，一頁紙一次**（1G 線 STC-028GP / 228GP / 2216GP / 2224GP + STC-4424GCPM + STC-110XGE + Hyconext 標；2.5G 一句「另議」待 SB-263 口徑；收 sales@）；再無回聲 → 不動；部分坐实 → 只做預付' + SG + TAG}},
    'SB-330': [{'kp_match': 'victor@omnicomm.com.sg', 'role': 'Operations Manager, Omni-Comm Pte Ltd（UEN 198803797H；1988 年起分銷 + 越南）= 收件人 — 一頁紙一次：貼標 OEM 30%，對位其現有貼標線 STC-028GP / 228GP / 2216GP / 2224GP / 4424GCPM 階梯 + Omni-Comm 標 / 自編貨號 + 越南直發 FOB 深圳（買方清關）+ 付費樣機；光模塊明說不做；回信 → 加厚 + 升 A' + SG + TAG},
               {'kp_match': 'chuong@omnicomm.com.sg', 'role': '越南側聯絡人（omninet.com.vn 為其越南側默認頁）= 抄送' + TAG},
               {'facts': {'legal_name': 'Omni-Comm Pte Ltd（UEN 198803797H；Exempt Private Company Limited By Shares；Live；.SG 域名註冊人 omnicomm.com.sg）', 'founded': '1988-10-20' + TAG, 'hq': '623 Aljunied Road #06-08 Aljunied Industrial Complex, Singapore 389835（+65 6319 9000）' + TAG, 'size': '小型（1–10 人；ZoomInfo 營收 $17.4M 不引用）' + TAG,
                          'other': '第 116 批：38 年老分銷商、已貼自己 logo 的交換機 + 覆蓋越南 → **貼標 OEM 30% B（升 A 候選），一頁紙一次**；iso SG 正確（HQ 新加坡），不做 country_fix；坐实' + TAG}}],
    'SB-776': [{'kp_match': 'karen_kwek@prolink2u.com', 'role': 'PROLiNK（Fida Int\'l (S) Pte Ltd，UEN 199101937H）研究档 KP = 收件人 — 一頁紙一次：貼標 OEM 30%，SMB PoE 非管理階梯 STC-028GP / 228GP / 2216GP / 2224GP + PROLiNK 標 / 彩盒 / 自編貨號 / 付費樣機 + 中東分站可直發 DAP；opener 引 2024-11 自動回覆；回信 → 加厚 + 升 A' + SG + TAG},
               {'kp_match': 'shijie_leong@prolink2u.com', 'role': '研究档联系人（2025-01 自動回覆 = 地址有效）= 抄送' + TAG},
               {'add_kp': {'name': 'Goh Wan Lin', 'email': 'wanlin_goh@prolink2u.com', 'role': 'Karen Kwek 休假代理人（2024-11-02 自動回覆）= 抄送' + TAG, 'source': 'S 郵箱 2024-11 自動回覆表頭'}},
               {'facts': {'legal_name': "FIDA INT'L (S) PTE LTD = PROLiNK 品牌（UEN 199101937H；年報 2026-07-20 已報；中東分站 PROLink.ME）", 'founded': '1991' + TAG, 'hq': '16 Kallang Place #06-01/04, Singapore 339156（+65 6357 0668）' + TAG, 'size': '中小（51–100 人）' + TAG,
                          'other': '第 116 批：35 年本土品牌、PoE 自己 logo、三個收件地址均活但從未真正跟進 → **貼標 OEM 30% B（升 A 候選），一頁紙一次**；守界：IMDA / 網安標籤 不聲稱、不評價其現貨質量；坐实' + TAG}}],
    'SB-1050': [{'kp_match': 'lawrence@keydence.com', 'role': 'Keydence Systems Pte. Ltd.（UEN 201019151W）研究档 KP（姓氏待核）= 收件人 — 一頁紙一次：集成商 25% small，CCTV 配套 PoE STC-028GP / 228GP / 2216GP 一口價 + 長距 PoE 250 m 模式 + 付費樣機；船用認證不聲稱' + SG + TAG},
                {'facts': {'legal_name': 'Keydence Systems Pte. Ltd.（UEN 201019151W；Local Company；Live；SSIC 61011 + 30110 船上安裝維護）', 'founded': '2010-09-09' + TAG, 'hq': '7030 Ang Mo Kio Avenue 5 #01-62 Northstar @ AMK, Singapore 569880（+65 6459 0780）' + TAG, 'size': '小型' + TAG,
                           'other': '第 116 批：CCTV / 門禁 / 布線集成商（含船上安裝）→ **集成商 25% B small，一頁紙一次**；再無回聲 → 不動；守界：船舶 / 海事認證不碰；坐实' + TAG}}],
    'SB-1035': [{'kp_match': 'info@gponnetwork.com', 'role': 'Director, GPON Network（RocketReach；新加坡；hotmail 並用）= 收件人 — 一頁紙一次、只做預付：分銷 20% small，工業 FS STI-154GP / STI-288DGGPM / STI-0240GE 一口價 + 付費樣機；WDM / SFP 明說不做' + SG + TAG},
                {'facts': {'legal_name': 'GPON Network（法人名 / UEN 未取；自稱 HEAD OFFICE 1660 South Highway 100, St Louis Park, MN 55416 USA + SINGAPORE OFFICE 400 Orchard Road #06-03 — 兩處皆商務中心特徵 → 身份不清）', 'founded': '自稱 2000 年起' + TAG, 'hq': '400 Orchard Road #06-03, Singapore 238875（商務中心；+65 8729 1383）' + TAG, 'size': '微型（9 人自述；營收 $2M 口徑不實）' + TAG,
                           'other': '第 116 批：身份不清的供應鏈 / 參考價站，但 Simon 表內「可以多跟進一下」→ **分銷 20% B small，一頁紙一次（預付 100%、不賒）**；再無回聲 → 不動；未坐实' + TAG}}],
    'SB-697': [{'kp_match': 'danny@alliedasia.com.sg', 'role': 'Allied Asia Resources Pte. Ltd.（自有品牌 ATZ = SB-346）研究档 KP = 收件人 — 一頁紙一次：貼標 OEM 30% small，對位其 ATZ PoE 線的 STC-028GP / 228GP / 2216GP / 2224GP 階梯 + ATZ 標 / 自編貨號 / 中性包裝 + 10G MC 只有 STC-110XGE + 付費樣機；14 槽機架 / SFP 明說不做；不點名 ONV' + SG + TAG},
               {'kp_name': 'Kelvin Tan', 'role': 'Sales Engineer（研究档；kelvin.tan@alliedasia.com.sg 見 entities）= 抄送' + TAG},
               {'facts': {'legal_name': 'Allied Asia Resources Pte. Ltd.（UEN 1 查未得；Alibaba 認證 Manufacturer / Trading / Distributor；商標 ATZ ×4；國內市場 90% / 東南亞 10%）', 'founded': '2012' + TAG, 'hq': '55 Serangoon North Ave 4 #01-18, Singapore 555859' + TAG, 'size': '小型（5–10 人；自述年營收 US$1–2.5M）' + TAG,
                          'other': '第 116 批：自有品牌 ATZ 的小型連接方案商、PoE 現用 ONV 貼標 → **貼標 OEM 30% B small，一頁紙一次**；再無回聲 → 不動；UEN 未取 → 只做預付；SB-346 併線至此；部分坐实' + TAG}}],
    'SB-797': [{'kp_match': 'sales@excelengineeringsg.net', 'role': '研究档 KP（9697 0621）— 微型（實繳 S$1,000、虛擬地址、官網失效）+ 需求只有 MC → 不動' + TAG},
               {'facts': {'legal_name': 'Excel Engineering (SG) Pte. Ltd.（UEN 201332361M；Live；實繳資本 S$1,000；2 名高管 / 股東；SSIC 71129 + 46900；無抵押）', 'founded': '2013-12-02' + TAG, 'hq': '100 Peck Seah Street #08-14 PS100, Singapore 079333（虛擬辦公地址；6898 4451）' + TAG, 'size': '微型（2 人）' + TAG,
                          'other': '第 116 批：微型 + 虛擬地址 + 需求只有 MC（Saga 僅 STC-110XGE）+ 7 次 0 回覆 → **不動（B 保留）**；坐实' + TAG}}],
    'SB-945': [{'kp_match': 'robin@grep.sg', 'role': 'Founder / CEO / Managing Director, Grep Tech（Crunchbase / Tracxn；2012 創辦；SMS 網關 / 軟體 = 行業外）— 15 次 0 回覆，不動' + TAG},
               {'facts': {'legal_name': 'Grep Tech Pte Ltd（LinkedIn 法人名；UEN 未取；GREP ADVISORY PTE. LTD. 202411162K ≠）', 'founded': '2012' + TAG, 'hq': '未取（新加坡）' + TAG, 'size': '微型（1–10 人）' + TAG,
                          'other': '第 116 批：SMS 網關 / 企業軟體公司（行業外）+ 15 次 0 回覆 + 官網報錯 → **不動（B 保留）**；部分坐实' + TAG}}],
    'SB-346': {'facts': {'legal_name': 'ATZ（atz.com.sg）= Allied Asia Resources Pte. Ltd.（SB-697）的自有商標（Alibaba 認證頁 Trademarks(4) ATZ；alliedasia.com.sg 貨號前綴 ATZ）', 'founded': '—（商標）' + TAG, 'hq': '55 Serangoon North Ave 4 #01-18, Singapore 555859（同 SB-697）' + TAG, 'size': '—' + TAG,
                         'other': '第 116 批：**同一公司的品牌站 → 併線 SB-697，本行不單發**；坐实（商標歸屬）' + TAG}},
    'SB-719': {'facts': {'legal_name': 'Trioms Technology Pte Ltd（UEN 201131509H，官網 Reg / GST；General Standards 新加坡分銷商）', 'founded': '2011（UEN 年份）' + TAG, 'hq': '200 Jalan Sultan #03-11 Textile Centre, Singapore 199018（+65 9021 9589；舊址 10 Anson Road #17-22 International Plaza）' + TAG, 'size': '微型（手機為總機）' + TAG,
                         'other': '第 116 批：科學 / 海洋 / 氣象儀器多品牌分銷（JW Fishers / Kestrel / Boltek），網路只是一款 AOA 工業 MC 的點綴（非目標行業）+ 14 次 0 回覆 → **不動（B 保留）**；坐实' + TAG}},
    'SB-937': {'facts': {'legal_name': 'Anewtech Systems Pte Ltd（UEN 199903145E；Live；實繳資本 S$1,262,500；抵押 7 項；5 名高管；SSIC 26209；MY 雪蘭莪 + VN 胡志明市 辦公室）', 'founded': '1999（UEN 簽發記錄 2008-09-11）' + TAG, 'hq': '62 Ubi Road 1 #04-14 Oxley Bizhub 2, Singapore 408734（+65 6292 0801）' + TAG, 'size': '中小（三國辦公室）' + TAG,
                         'other': '第 116 批：工業計算機集成商 / 分銷商（Advantech / IEI / Supermicro …；工業交換機在供 ORing）= 真實進口商 → **分銷 20% B，一頁紙一次**（寬溫工業線 STI-154GP / 288DGGPM / 488DGGPM / 0240GE 一口價 + 3 年保 + MOQ 1 + 付費樣機；EN 50155 明說不做；收 sales@）；再無回聲 → 不動；守界：不點名 ORing；抵押 7 項 → 只做預付；坐实' + SG + TAG}},
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
