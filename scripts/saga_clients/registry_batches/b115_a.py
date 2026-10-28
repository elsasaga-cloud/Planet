# -*- coding: utf-8 -*-
"""第 115 批（T29-U108，2026-10-28）第 1 段 14 户（IN 收尾 5 + KR 第 1–9 户）—— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 115
F = '2026-10-28'
IN = '— 印度常规：20 / 25 / 30 + T/T 预付 + FOB 深圳'
KR = '— 韩国常规：20 / 25 / 30 + T/T 预付 + FOB 深圳（KC 不声称、由买方自办）'

# ───────── IN 收尾 5 ─────────
put('SB-635', key='in', batch=B, name='LMD Hitech India Private Limited（radiantgroup.org 表内域名不可达；**CIN U29240HR2013PTC048422（2013-02-27；RoC Delhi）**；Plot No. 620, Sector 8, IMT Manesar, Haryana 122052；注册邮箱 sales1@hitech-eng.in）— **特种机械 / 矿山建筑机械制造（NIC 29240）**，非网络行业；董事 **Dinesh Sharma（= KP）**/ Chanchal Sharma；法定资本 ₹5 lakh / 实缴 ₹1 lakh；最近报表 2023-03-31；WA 已加无实质回复', iso='IN', fetched=F,
    source='IN · 1 次检索：zaubacorp（LMD HITECH INDIA PRIVATE LIMITED CIN U29240HR2013PTC048422；incorporated 27 February 2013；ROC Delhi；Active；Manufacture of special purpose machinery / machinery for mining, quarrying and construction；Authorised ₹500,000 / Paid up ₹100,000；directors DINESH SHARMA DIN 02249388 (2013-02-27) / CHANCHAL SHARMA DIN 02283323 (2016-09-30)；Plot No 620 Sector 8 IMT Manesar 122052；balance sheet last filed 31 March 2023）+ tofler（Gurgaon；Company Email Sales1@hitech-eng.in）；2026-10-28',
    url='https://www.zaubacorp.com/company/LMD-HITECH-INDIA-PRIVATE-LIMITED/U29240HR2013PTC048422',
    number='CIN U29240HR2013PTC048422', status='Active', incorporated='2013-02-27', company_type='Private Limited',
    sic=['特种机械 / 矿山建筑机械 制造（马内萨尔）'],
    address='Plot No. 620, Sector 8, IMT Manesar, Haryana 122052', accounts='实缴 ₹1 lakh；报表至 2023-03-31', accounts_due='—', size_band='微型（实缴 ₹1 lakh）',
    officers=['Dinesh Sharma — Director（DIN 02249388；研究档 KP）', 'Chanchal Sharma — Director（DIN 02283323）'], psc='Sharma 夫妇（推定）', charges='', prev_names=[],
    lines=['**机械制造商、无网络业务、域名不可达 + WA 无回复 → 非目标行业，不动（B 保留）**'],
    notes='不动（非目标行业 + 微型 + 无回声）；坐实（CIN + 董事 = KP + 地址）。')
put('SB-640', key='in', batch=B, name='Technoverse Business Solutions（technoversebs.com；**个体经营；GSTIN 27CWEPK3302H2ZS（2023-11-07）**；2nd Floor, 202, Shiv Sambhav CHS, Savarkar Road, Kalyan, Dombivli, Thane 421201, Maharashtra）— 孟买都市圈 IT 硬件 / 网络产品经销（Ubiquiti / Cisco / TP-Link / Aruba / Juniper / Netgear；IndiaMART 列 断路器 / PLC 柜 / 光模块 / 路由器 / 交换机）；营业额 ₹0–40 lakh；KP Suyash Mishra（WA 已加无实质回复）', iso='IN', fetched=F,
    source='IN · 1 次检索：indiamart（Technoverse Business Solutions；Dombivli, Thane；GST 27CWEPK3302H2ZS；GST Registration Date 07-11-2023；Service Provider and Others；0 - 40 L；2 ND Floor 202 Shiv Sambhav CHS Savarkar Road Kalyan Dombivli Thane-421201）+ crunchbase（supplies switches, routers and wireless products；Mumbai；11-50 虚高）+ salezshark（name@technoversebs.com；421201）；2026-10-28',
    url='https://www.indiamart.com/company/70154489/',
    number='GSTIN 27CWEPK3302H2ZS', status='Active', incorporated='2023（GST 2023-11-07）', company_type='Proprietorship（个体）',
    sic=['IT 硬件 / 网络产品 经销（东比夫利 / 孟买）'],
    address='2nd Floor, 202, Shiv Sambhav CHS, Savarkar Road, Kalyan, Dombivli, Thane 421201', accounts='₹0–40 lakh（自报）', accounts_due='—', size_band='个体 / 微型',
    officers=['Suyash Mishra — 研究档 KP（sales@technoversebs.com）'], psc='未取（GST 登记人未公开）', charges='', prev_names=[],
    lines=['**2023 年新设个体经销、WA 无回复 → 不动（B 保留；自来询盘按一口价 + T/T 预付）**'],
    notes='不动（个体 + 新设 + 无回声）；坐实（GSTIN + 地址）。')
put('SB-1106', key='in', batch=B, name='Ruhan Farook（印度个人联系人；无邮箱、无公司、无域名；2024-02 对无线 IP / 24 光 combo 回复「catalog」后 16 次跟进无实质进展）— **0 查（个人，无可检索主体）**', iso='IN', fetched=F,
    source='IN · 0 查：个人姓名 + 无公司 / 域名 / 邮箱 → 不具备检索主体（第 115 批规则：个人 1 查即停、无线索则 0 查）；2026-10-28',
    url='', number='未取', status='个人', incorporated='未取', company_type='个人',
    sic=['个人联系人（印度）'],
    address='未取', accounts='—', accounts_due='—', size_band='个人',
    officers=[], psc='—', charges='', prev_names=[],
    lines=['**个人、无主体、16 次无进展 → 不动**'],
    notes='不动（个人 + 0 查）；未坐实。')
put('SB-1107', key='in', batch=B, name='Surya Namberdar（印度个人联系人；无邮箱、无公司、无域名；2023-09 收商用 PoE 价目后要「印度货币价格」，此后无实质进展）— **0 查（个人，无可检索主体）**', iso='IN', fetched=F,
    source='IN · 0 查：个人姓名 + 无公司 / 域名 / 邮箱 → 不具备检索主体（第 115 批规则：个人 1 查即停、无线索则 0 查）；2026-10-28',
    url='', number='未取', status='个人', incorporated='未取', company_type='个人',
    sic=['个人联系人（印度）'],
    address='未取', accounts='—', accounts_due='—', size_band='个人',
    officers=[], psc='—', charges='', prev_names=[],
    lines=['**个人、无主体、只问卢比价 → 不动（Saga 只报 USD）**'],
    notes='不动（个人 + 0 查）；未坐实。')
put('SB-595', key='in', batch=B, name='（表内 mpcl.in；chetan@mpcl.in 群发退信）— **1 次检索只命中同名 MPCL Industries Limited（mpcl.co.in；CIN U26959DL1993PLC219546；德里电气设备 / 广播集团，≠ 表内域名）**；mpcl.in 主体无公开记录 → 未坐实；用户表来源「买过商业 PoE（从同行进口）」非 Saga 成交', iso='IN', fetched=F,
    source='IN · 1 次检索：「mpcl.in India company Chetan MPCL networking PoE switch importer」→ tracxn / zoominfo / emis 仅 MPCL INDUSTRIES LIMITED（mpcl.co.in；CIN U26959DL1993PLC219546；Pitampura Delhi；电气设备制造）≠ mpcl.in；1 查即停；2026-10-28',
    url='', number='未取', status='主体不明', incorporated='未取', company_type='未取',
    sic=['主体不明（印度）'],
    address='未取', accounts='—', accounts_due='—', size_band='未取',
    officers=[], psc='未取', charges='', prev_names=[],
    lines=['**域名无主体、邮箱退信、非 Saga 成交 → 不动（地址失效；同名 MPCL Industries 不并线）**'],
    notes='不动（地址失效 + 未坐实）；未坐实（同名陷阱）。')

# ───────── KR 第 1–9 户 ─────────
put('SB-210', key='other', batch=B, name='(주)디오넷 DEONET Co., Ltd.（deonet.co.kr；**사업자등록번호 229-81-33168 / 법인등록번호 110111-1564940；设立 1998-07-13**；서울 구로구 디지털로 242, 한화비즈메트로 802호（08394）；电话 02-3664-5874）— **家庭网络 / 超高速互联网交换机研发与销售（컴퓨터 제조업；主要产品 스위치 / 허브 / 게이트웨이、PON / CPE）**；代表 **이혁재 Lee Hyuk-jae**；24–25 人；资本金 18억；**营收 2024 295억원（≈$21M）/ 2025 260억원；외감 法人；信用 양호（2025-04）**；非上市（통일주권 1,993,600 주）；KP Chris（Kim Yeong Man）：工商业交换机都有、PoE 问芯片、另问 GPON / EPON；23 次跟进无实质回复', iso='KR', fetched=F,
    source='KR · 2 次检索：bizno（(주)디오넷 DEONET Co.,Ltd.；설립 1998-07-13；대표 이혁재；02-3664-5874；서울 구로구 디지털로 242, 802호 한화비즈메트로；종업원 24명；사업자등록번호 229-81-33168；법인등록번호 110111-1564940；컴퓨터 제조업；스위치, 허브, 게이트웨이）+ seoulexchange（비상장；1,993,600주；대표이사 이혁재）+ jobkorea（사원수 25명；자본금 18억원；매출 2022 257.9억 / 2023 272.9억 / 2024 295.4억 / 2025 260.1억；홈네트워크 및 초고속인터넷 스위치 개발 및 판매）+ catch（외감；신용등급 양호 2025.04；사원수 21명 2024.12）；2026-10-28',
    url='https://bizno.net/article/2298133168',
    number='사업자등록번호 229-81-33168 / 법인등록번호 110111-1564940', status='계속사업자（Active）', incorporated='1998-07-13', company_type='주식회사（非上市；외감）',
    sic=['网络交换机 / PON / CPE 研发制造 + 销售（首尔九老）'],
    address='서울특별시 구로구 디지털로 242, 802호 (구로동, 한화비즈메트로) 08394', accounts='매출 2024 295억원 / 2025 260억원；자본금 18억', accounts_due='—', size_band='中小（24–25 人；≈$20M）',
    officers=['이혁재 Lee Hyuk-jae — 대표이사（拍板人）', 'Chris（Kim Yeong Man）— 研究档 KP（chris@deonet.co.kr）= 收件人（抄 info@）'], psc='未取（非上市）', charges='', prev_names=[],
    lines=['**自研交换机厂商（ISP / 家庭网络线）、曾问 PoE 芯片 + 工业线 → 贴标 / 配套 OEM 30% B BIG，加厚一次（切口：其 ISP 线之外的工业 + PoE 补位：STI-288DGGPM / STI-488DGGPM（工业管理）+ STC-2224GP / STC-4424GCPM（Marvell 管理 PoE，芯片平台明写）+ 中性包装 / 自编货号 / 付费样机；GPON / EPON 明说没有；英文，Chris 直呼、抄 info@）' + KR + '**；回信 → 次候选',
           '守界：不点名其 KT / SK / LGU+ 供货；不提芯片之外的 ODM 承诺；KC 不声称'],
    notes='贴标 / 配套 30%；B BIG 加厚一次；坐实（사업자등록번호 + 법인등록번호 + 代表 + 营收）。')
put('SB-322', key='other', batch=B, name='BlackBear TechHive（blackbear-ics.com）= **台灣黑熊網路安全股份有限公司 BlackBear (Taiwan) Industrial Networking Security Ltd.（統編 83305324；設立 2020-11-26；新竹縣竹北市東興路一段146號 = Atop 四零四科技同址；代表人 謝秋蓮；董監事 蘇柏豪 / 劉德豐）+ 日本子公司 BlackBear TechHive Japan 株式会社（法人番号 8010401158437；2021-03；東京都港区六本木3-6-9）**— 工业单向网闸 / 数据二极管（DD9000 / BIG9000）厂商，Atop 关联；President Takashi Eki（易傑，日本人，+81；= KP）；SECON 2023 问 Saga 是否做 OEM/ODM；33 次跟进无实质回复；**表内 iso KR 系展会地，主体在台湾 → country_fix 台湾**', iso='TW', fetched=F,
    source='KR→TW · 2 次检索：alarmbox.jp（ＢｌａｃｋＢｅａｒ ＴｅｃｈＨｉｖｅ Ｊａｐａｎ株式会社；法人番号 8010401158437；東京都港区六本木３丁目６番９号；設立 2021年3月）+ twincn（台灣黑熊網路安全股份有限公司 BlackBear(Taiwan) Industrial Networking Security Ltd.；統編 83305324；代表人 謝秋蓮；董監事 謝秋蓮, 蘇柏豪, 劉德豐；新竹縣竹北市東興里東興路一段146號；設立 109-11-26；國貿局登記 20201130；營業中）；2026-10-28',
    url='https://www.twincn.com/item.aspx?no=83305324',
    number='統一編號 83305324（TW）/ 法人番号 8010401158437（JP）', status='核准設立 / 營業中', incorporated='2020-11-26（TW）/ 2021-03（JP）', company_type='股份有限公司 + 日本株式会社',
    sic=['工业网络安全 / 数据二极管 厂商（新竹竹北；Atop 关联）'],
    address='No. 146, Sec. 1, Dongxing Rd., Zhubei City, Hsinchu County 30261, Taiwan（JP：東京都港区六本木3-6-9）', accounts='未取', accounts_due='—', size_band='小型（新设 2020）',
    officers=['謝秋蓮 — 代表人（TW）', 'Takashi Eki（易傑）— President（研究档 KP；eki@blackbear-ics.com）'], psc='Atop 关联（同址；推定）', charges='', prev_names=[],
    lines=['**工业交换机厂 Atop 关联的网安硬件商、问的是 OEM/ODM 代工（Saga 不制造）、33 次 0 回复 → 同行集团 + 守界（关键基础设施安全）→ 不动（B 保留）**',
           'country_fix：KR → 台湾（主体統編 + 日本子公司；KP 在东京）'],
    notes='不动（同行集团 + 33 次 0 回复）；坐实（統編 + 法人番号 + 代表人）；country_fix 台湾。')
put('SB-329', key='other', batch=B, name='CANSOL Co., Ltd.（cansol.co.kr；**MONAD Inc.（monadinc.co.kr）研发 + CANSOL 销售的姊妹对；#1209 B-Dong, Seongnam Central BIZ Tower 2차, 사기막골로 99, 중원구, 성남시 13201**）— **自研工业 L2 交换机（韩国道路公社 BMT 通过；世宗 / 东滩 U-City、ITS、高速公路、隧道、广安大桥项目）+ CCTV 远程清洗系统（专利）**；**CEO KJ Lee（= KP kjlee@）**；사업자등록번호 未取 → 部分坐实；11 次跟进无回复', iso='KR', fetched=F,
    source='KR · 2 次检索：第 1 次「캔솔 Cansol … 사업자등록번호」落空（同名 코나솔 / 찬솔 ≠）；第 2 次 monadinc.co.kr/about/History（History of CANSOL；Founding of MONAD Inc.；Developed Industrial L2 Switch 1st / 2nd version；BMT passed by Korea Expressway Corporation；Sejong / Dongtan U-city / Ansan ITS / Gwangan Bridge installations；Founding of CANSOL Co., Ltd., split business role with MONAD；#1209 B-Dong Seongnam Central BIZ Tower 2Cha Sagimaggolro 99 Jungwon-Gu Seongnam 13201）+ cansol.co.kr/about（started as Monad focused on R&D；sister company Cansol sales & marketing；KJ Lee CEO of CANSOL Co., Ltd.）；2026-10-28',
    url='http://www.monadinc.co.kr/about/History.html',
    number='未取（사업자등록번호 两查未得）', status='营业中（官网 2025 在线）', incorporated='未取', company_type='주식회사 ×2（MONAD 研发 / CANSOL 销售）',
    sic=['工业 L2 交换机 自研 + ITS / 道路项目 集成（城南）'],
    address='#1209 B-Dong, Seongnam Central BIZ Tower 2cha, Sagimakgol-ro 99, Jungwon-gu, Seongnam 13201', accounts='未取', accounts_due='—', size_band='小型（研发型）',
    officers=['KJ Lee — CEO of CANSOL（研究档 KP kjlee@cansol.co.kr）= 拍板人 / 收件人'], psc='未取', charges='', prev_names=[],
    lines=['**自研工业交换机 + ITS 项目方、CEO 本人为 KP、曾问 bypass 工业机 → 贴标 / 配套 30% B small，一页纸一次（切口：bypass 机型明说没有；作其自研机之外的性价比配套：STI-288DGGPM / STI-488DGGPM / STI-0240GE 宽温 + 3 年保 + 自编货号；英文，KJ Lee 直呼）' + KR + '**；再无回声 → 不动（同行自研为主）',
           '守界：道路 ITS 可谈、轨交不接；不引用其 BMT / 专利；사업자등록번호 未取 → 部分坐实、只做预付'],
    notes='贴标 / 配套 30% small；一页纸一次；部分坐实（官网沿革 + 地址 + CEO = KP；号码未取）。')
put('SB-336', key='other', batch=B, name='(주)인터코엑스 INTERCOAX Co., Ltd.（intercoax.com；**사업자등록번호 140-81-85228；设立 2014-04-17**；경기도 안양시 동안구 학의로 250）— **EoC（同轴以太网 + 供电）发射 / 接收 / 交换设备制造商（IP 摄像机改造场景；经 SI / 代理商销售）**；代表 **이일묵 Lee Il-muk**；17 人（2021）；资本金 6억；**营收 2025 11.3억원（≈$0.8M；2024 档 10–50억）**；此前买过 Saga 样品；KP Byron / Jongmin 多次交谈、问 2+2+8 型号；44 次跟进无实质回复', iso='KR', fetched=F,
    source='KR · 1 次检索：jobkorea（㈜인터코엑스；그 외 기타 전기장비 제조업；사원수 17명 2021.12.31；설립일 2014.04.17；자본금 6억원；매출액 11억 3천만원 2025.12.31；대표자 이일묵；EOC 기술을 IP 카메라 보안시장에 세계최초 적용）+ rndcircle（(주)인터코엑스；대표 이일묵；사업자번호 1408185228；경기도 안양시 동안구 학의로 250；2014.04.17；2024 연 매출 10억~50억；EoC 송신기 / 수신기 / 스위치 제조 판매；SI 및 대리점 네트워크）；2026-10-28',
    url='https://www.jobkorea.co.kr/recruit/co_read/c/intercoax',
    number='사업자등록번호 140-81-85228', status='계속사업자（Active）', incorporated='2014-04-17', company_type='주식회사',
    sic=['EoC 同轴以太网 设备 制造（安养）'],
    address='경기도 안양시 동안구 학의로 250', accounts='매출 2025 11.3억원；자본금 6억', accounts_due='—', size_band='小型（17 人；<$1M）',
    officers=['이일묵 Lee Il-muk — 대표이사（拍板人）', 'Byron — 研究档 KP（byron@intercoax.com；+82 10 3605 5714）= 收件人', 'Jongmin — 研究档 KP（jongmin@intercoax.com）= 抄送'], psc='未取', charges='', prev_names=[],
    lines=['**自有品牌 EoC 厂商、买过样品、明确要 8 PoE + 2 GE + 2 SFP → 贴标 OEM 30% B，加厚一次（切口：对位 STC-228GP（8 PoE + 2 GE + 2 SFP）一口价 + 自编货号 / 中性包装 + 付费样机复购价；英文，Byron 直呼、抄 Jongmin）' + KR + '**；回信 → 次候选',
           '守界：2025 营收下滑明显 → 只做 T/T 预付；不提其 EoC 产品竞品；KC 不声称'],
    notes='贴标 OEM 30%；B 加厚一次；坐实（사업자등록번호 + 代表 + 地址 + 营收）。')
put('SB-513', key='other', batch=B, name='주식회사 유비큐넷 Ubiqnet Co., Ltd.（starlink.co.kr / ubiqnet.co.kr；**사업자등록번호 876-81-02587；통신판매업신고 제2022-서울용산-1075호；서울 용산구 청파로 113-6, 넥서스밸리 905호**；电话 02-711-0056）— 网络方案 + 分销（**自有品牌 Starlink：工业 FS / MC / EoC / 10G SFP+ 贴标**；Cisco / HPE / Netgear / Soltech 代理；综合布线；B2B 商城）；**대표이사 이재식 Lee Jae-sik（= KP Jaesik Lee）**；2022 年前后设立（通信販売 2022）；23 次跟进无回复', iso='KR', fetched=F,
    source='KR · 1 次检索：starlink.co.kr 页脚（주식회사 유비큐넷；사업자등록번호 876-81-02587；대표이사 이재식；서울 용산구 청파로113-6, 넥서스밸리 905호；통신판매업신고 제2022-서울용산-1075호；02-711-0056；개인정보관리책임자 이재식）+ ubiqnet.co.kr B2B몰（[SFP10G-SR] 스타링크 10G SFP+ 자체 브랜드；에스크로가입）；2026-10-28',
    url='https://starlink.co.kr/main/page.html?pid=8',
    number='사업자등록번호 876-81-02587 / 통신판매업 2022-서울용산-1075', status='营业中（商城在线）', incorporated='≈2022（通信贩卖申报 2022）', company_type='주식회사',
    sic=['网络设备 分销 + 自有品牌 Starlink（首尔龙山）'],
    address='서울 용산구 청파로 113-6, 넥서스밸리 905호', accounts='未取', accounts_due='—', size_band='小型（新设 2022）',
    officers=['이재식 Lee Jae-sik — 대표이사（研究档 KP Jaesik Lee；help@ubiqnet.co.kr）= 拍板人 / 收件人'], psc='이재식（推定）', charges='', prev_names=[],
    lines=['**自有品牌 Starlink 贴标 + 代表本人为 KP → 贴标 OEM 30% B，加厚一次（切口：Starlink 标 STI-154GP / STI-288DGGPM（工业）+ STC-228GP / STC-2224GP（商用 PoE）+ 中性包装 / 自编货号 / MOQ 1 / 付费样机；英文，Jaesik 直呼）' + KR + '**；回信 → 次候选',
           '守界：不点名 Soltech 合作；光模块 / MC 明说不做；KC 不声称'],
    notes='贴标 OEM 30%；B 加厚一次；坐实（页脚 사업자등록번호 + 代表 = KP + 地址 + 通信贩卖号）。')
put('SB-929', key='other', batch=B, name='㈜솔텍 SOLTECH（soltech.co.kr；**设立 1996-05-01；대표 이동화 Lee Dong-hwa；서울 영등포구 당산로41길 11, 당산 SK V1센터 1702–1704호（关联 솔텍인포넷(주) 同址 210호、同代表）**）— **光通信设备自研 / 自产 / 直销厂商（INNO-BIZ；光转换器 / 工业光纤交换机 / 光猫 / 光链路 / 复用器；FTTH、ITS、隧道、变电站、大坝 CCTV、军方；SFC 系列；Fibermart 网店）**；**110 人；营收 300억원（≈$21M）**；资本金 2억；Simon 客户（研究档）；KP Kim Kwang Young（金广永）/ Jason；사업자등록번호 未取 → 部分坐实；23 次跟进无回复', iso='KR', fetched=F,
    source='KR · 2 次检索：jobkorea（㈜솔텍；사원수 110명；설립일 1996.05.01；자본금 2억원；매출액 300억；대표자 이동화；INNO-BIZ 광통신장비 개발, 제조, 판매；주소 서울 영등포구 당산동4가 80번지 당산 SK V1센터 1702,3,4호；광컨버터 / 광허브 / 광모뎀 / 광링크 국산화；ITS, 터널, 변전소, 댐 CCTV, 군관련）+ saramin（솔텍인포넷(주)；대표 이동화；soltech.co.kr；서울 영등포구 당산로41길 11, 210호；유선 통신장비 제조 / 정보통신공사）；bizno 同名 양산 SOLTECH LTD. 621-81-36599 为塑料厂 ≠；2026-10-28',
    url='https://www.jobkorea.co.kr/Recruit/Co_Read/C/soltech99',
    number='未取（사업자등록번호 两查未得；同名塑料厂 621-81-36599 ≠）', status='营业中', incorporated='1996-05-01', company_type='주식회사（+ 关联 솔텍인포넷(주)）',
    sic=['光通信 / 工业光纤网络设备 制造 + 施工（首尔永登浦）'],
    address='서울 영등포구 당산로41길 11, 당산 SK V1센터 1702–1704호 (당산동4가)', accounts='매출 ≈300억원；자본금 2억', accounts_due='—', size_band='中型（110 人；≈$21M）',
    officers=['이동화 Lee Dong-hwa — 대표（两法人）', 'Kim Kwang Young（金广永）— 研究档 KP（kky@soltech.co.kr）= 收件人', 'Jason — 研究档 KP（jasonk@soltech.co.kr）= 抄送'], psc='未取', charges='', prev_names=[],
    lines=['**自产光网络设备 110 人厂、Simon 既有联系人 → 贴标 / 配套 OEM 30% B BIG，加厚一次（切口：其光转换器线之外的 PoE / 管理交换机补位：STC-2224GP / STC-4424GCPM（Marvell 管理 PoE）+ STI-288DGGPM / STI-488DGGPM（工业环网）+ 自编货号 / 中性包装 / 付费样机；英文，Kim Kwang Young 直呼、抄 Jason）' + KR + '**；回信 → 次候选',
           '守界：군관련 / 变电站 不提、不投标；不点名其 SFC 系列竞品；사업자등록번호 未取 → 部分坐实，只做预付'],
    notes='贴标 / 配套 30%；B BIG 加厚一次；部分坐实（两法人名 + 代表 + 地址 + 规模；号码未取）。')
put('SB-967', key='other', batch=B, name='주식회사 와이앤엠시스템즈 YNM Systems Inc.（ynminc.com；**사업자등록번호 106-87-07961 / 법인등록번호 110111-5457109；设立 2014-07-04**；서울 금천구 가산디지털1로 119, SK트윈테크타워 A동 1105 / 1106 / 1108호（08589）；电话 02-838-4353）— **广播级 PTZ / POV 摄像机制造商（방송용 PTZ / 비디오 카메라；C-NK200 / ZCB-100）**；代表 **이명호 Lee Myung-ho（= KP MH Lee, CEO）**；6–8 人；营收 <$5M（ZoomInfo 档）；17 次跟进无回复', iso='KR', fetched=F,
    source='KR · 1 次检索：bizno（주식회사 와이앤엠시스템즈 YNM Systems Inc.；설립 2014-07-04；대표 이명호；02-838-4353；서울 금천구 가산디지털1로 119, A동 1105호 1106호, 1108호 SK트윈테크타워；종업원 6명；사업자등록번호 106-87-07961；법인등록번호 110111-5457109；www.ynminc.com）+ cookiedeal（와이앤엠시스템즈；Manufacture of broadcasting apparatuses；8 people；Small enterprise；방송용 PTZ / 비디오 카메라）+ zoominfo（CEO Mh Lee；revenue <$5M）；2026-10-28',
    url='https://www.bizno.net/article/1068707961',
    number='사업자등록번호 106-87-07961 / 법인등록번호 110111-5457109', status='계속사업자（Active）', incorporated='2014-07-04', company_type='주식회사（소기업）',
    sic=['广播 PTZ 摄像机 制造（首尔衿川）'],
    address='서울특별시 금천구 가산디지털1로 119, SK트윈테크타워 A동 1105·1106·1108호 08589', accounts='<$5M（ZoomInfo 档）', accounts_due='—', size_band='微型（6–8 人）',
    officers=['이명호 Lee Myung-ho — 대표이사（研究档 KP MH Lee；mhlee@ynminc.com）= 拍板人 / 收件人'], psc='이명호（推定）', charges='', prev_names=[],
    lines=['**微型广播摄像机品牌、CEO 本人为 KP、研究档建议多跟 → 配套 25% B small，一页纸一次（切口：随其 NDI / IP PTZ 成套出货的 PoE 交换机 STC-028GP / STC-228GP（PoE+ 预算、每口 30 W）+ 贴其标可谈 30%、MOQ 1、付费样机；英文，MH Lee 直呼）' + KR + '**；再无回声 → 不动',
           '守界：不提广播级 SDI / 光端机（Saga 无）；KC 不声称'],
    notes='配套 25% small（贴标可 30%）；一页纸一次；坐实（사업자등록번호 + 법인등록번호 + 代表 = KP + 地址）。')
put('SB-220', key='other', batch=B, name='（表内 sun-flowers.co.kr；sun@sun-flowers.co.kr；「CCTV 商业 PoE 自己的 logo」「质量高」）— **官网为防机器人验证页；2 次检索均落空（bizno 同名 썬플라워리조트 / 썬플라워 电商个体（已歇业）/ 썬플라워유통 均 ≠）→ 主体未坐实**；无 KP；23 次跟进无回复', iso='KR', fetched=F,
    source='KR · 2 次检索：「sun-flowers.co.kr 선플라워스 CCTV PoE 스위치 사업자등록번호」→ bizno 仅同名 (주)썬플라워리조트 121-81-04340（养牛业）/ 썬플라워 407-12-41904（电商个体、2024-05 폐업）/ 썬플라워유통（医疗器械、2026-02 폐업）≠；「"sun-flowers.co.kr" OR "Sun-Flowers Co" CCTV」→ 无命中；2 查即停；2026-10-28',
    url='', number='未取', status='主体不明', incorporated='未取', company_type='未取',
    sic=['主体不明（韩国 CCTV）'],
    address='未取', accounts='—', accounts_due='—', size_band='未取',
    officers=[], psc='未取', charges='', prev_names=[],
    lines=['**官网不可读 + 两查无主体 + 无 KP + 23 次 0 回复 → 不动（B 保留；对方自来再核）**'],
    notes='不动（未坐实 + 官网不可达 + 无 KP）；未坐实。')
put('SB-502', key='other', batch=B, name='엘림광통신㈜ Elim Optical Communication Co., Ltd.（elimopt.co.kr；**사업자등록번호 123-81-89423；设立 2003-06-23**；경기도 수원시 권선구 산업로155번길 234, 2동 4층 (고색동, 산업3단지 / 더좋은생활)；电话 031-257-7157；elimopt@elimopt.co.kr）— **光传输网络开发 + 施工（光传输系统 / 以太网 / 影音数据；MAS 多数供应者政府采购品）；自有品牌 PoE 管理交换机 EL-G48E6TG-POE / G24E4G-POE / G16E2G-POE / G8E4G-POE / PG8E2G-BP（bypass），2024-11 以「제조자 엘림광통신」送 KC 测试**；代表 **유영록 Yoo Young-rok**；13 人；资本金 8억；**营收 ≈45억원（≈$3.2M）**；客户 K-water / 浦项 / 光阳 / 道路公社（年 50억 项目规模自报）；无具名 KP；23 次跟进无回复', iso='KR', fetched=F,
    source='KR · 1 次检索：elimopt.co.kr 页脚（엘림광통신；경기도 수원시 권선구 산업로 155번길 234 2동 4층 고색동 산업3단지；사업자등록번호 123-81-89423；031-257-7157；elimopt@elimopt.co.kr；다수공급자(MAS)제품）+ jobkorea（엘림광통신㈜；사원수 13명；설립일 2003.06.23；자본금 8억원；매출액 45억；대표자 유영록；광전송 네트워크 개발 및 시공；한국수자원공사, 포항제철, 광양제철, 한국도로공사 연간 50억 규모）+ elimopt.co.kr KC 시험성적서 PDF（제조자 엘림광통신주식회사；Fiber Optic Managed Switch EL-G48E6TG-POE；접수 2024-11-07；대표 유영록；사업자등록번호 123-81-89423）；2026-10-28',
    url='https://www.jobkorea.co.kr/recruit/co_read/c/elimopt',
    number='사업자등록번호 123-81-89423', status='계속사업자（Active）', incorporated='2003-06-23', company_type='주식회사',
    sic=['光传输 / 自有品牌 PoE 交换机 + 信息通信施工（水原）'],
    address='경기도 수원시 권선구 산업로155번길 234, 2동 4층 (고색동) ', accounts='매출 ≈45억원；자본금 8억', accounts_due='—', size_band='小型（13 人；≈$3M）',
    officers=['유영록 Yoo Young-rok — 대표이사（拍板人）', '（研究档无具名 KP：h0824@ / khs10623@elimopt.co.kr → 收件 elimopt@ + 两个人名邮箱）'], psc='유영록（推定）', charges='', prev_names=[],
    lines=['**自有品牌 PoE 管理交换机（以制造者名义送 KC）+ 政府 MAS 渠道 → 贴标 OEM 30% B，加厚一次（切口：对位其 EL-G48E6TG-POE / G24E4G-POE / G16E2G-POE / G8E4G-POE 全系的 STC-4424GCPM / STC-2224GP / STC-2216GP / STC-228GP 阶梯价 + 自编货号 / 中性包装 + 付费样机；bypass 机型明说没有；KC 由其自办、我方给 CE / FCC / RoHS 报告；英文，收 elimopt@ + 两人名邮箱、称 Mr. Yoo）' + KR + '**；回信 → 次候选',
           '守界：不点名其 MAS / 政府项目；不声称 KC；无具名 KP → 先 info 线'],
    notes='贴标 OEM 30%；B 加厚一次；坐实（页脚 + KC 报告 사업자등록번호 + 代表 + 营收）。')
print('b115 第 1 段 14 written')
