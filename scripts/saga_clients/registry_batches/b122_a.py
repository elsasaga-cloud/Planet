# -*- coding: utf-8 -*-
"""第 122 批（T29-U114，2026-10-29）第 1 段 18 户（TZ 3 + IQ 3 + NG 3 + US 3 + GH 3 + TR 3）—— 官方登记核实写入 registry（B 池收尾段二）。
TZ：BRELA 不可 1 查 → 官网 about / devex 补地址，公司自述证书号（SB-122 No. 85715）；IQ：无登记库 → D&B 法定名 + 地址（SB-588），域名失效 2 户未坐实；
NG：CAC 未得 → businesslist.com.ng / spiceworks 给地址 + MD + 成立年（SB-631）；US 3 户均个人邮箱 → 0 查；GH：ZoomInfo / ghanayello 补地址（SB-817），WA 2 户 0 查；TR：ISAF 名片 3 户 0 查。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 122
F = '2026-10-29'
TZ = '— 坦桑尼亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 达累斯萨拉姆（买方清关；TBS / TCRA 不声称）'
IQ = '— 伊拉克常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方经迪拜 / 土耳其货代自提清关）'
NG = '— 尼日利亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 拉各斯（买方清关；SON / NCC 不声称）'
US = '— 美国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP（买方清关；NDAA / TAA / UL 不声称）；周三 08–10 当地'
GH = '— 加纳常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 阿克拉（买方清关）'
TR = '— 土耳其常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 伊斯坦布尔（买方清关）；周四 10–12 当地'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ---------------- TZ 3 ----------------
row('SB-016', '坦桑尼亚 WhatsApp 买家 Richard Jackson（+255 768 043 267；**无邮箱 / 公司 → 0 查**）— 2023 主动要资料「说要下单」，2024-02 对 2 光 8 PoE 管理出货信息回「问了 catalog」；19 次推送 1 次实质回复', 'TZ',
    '0 查（无邮箱 / 公司）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '个人', '未知（坦桑尼亚）', '未取', '个人',
    ['Richard Jackson — WA 联系人（研究档 KP；无邮箱）'],
    '**曾言「要下单」→ 集成商 25% B，WA 最后一次一页纸（STI-288DGGPM $137 2 光 8 PoE 管理 一口价 + MOQ 1）' + TZ + '**；19×1 → 再无回声 → 不动',
    '集成商 25%；WA 最后一次一页纸（预付 100%）；0 查。')
row('SB-122', 'Tera Technologies and Engineering Limited（teratech.co.tz / ttel.co.tz；**公司自述：2011-09-09 依 Companies Act 2002 注册，Certificate of Incorporation No. 85715（领英公司页）；官网 about：Mbezi Beach Africana, Plot No. 2283, Block H, Tarangire Street, Africana Drive, P.O. Box 31257, Dar es Salaam；Tel/Fax +255 22 270 1612；第二办公 Sinza Block A, Plot 173（devex）；CEO & Co-Founder Eng. Dr. Daudi Charles（ERB 注册工程师 2013 起）；约 10 名工程师；世行 / TMA 中标 3 项**）→ 坐实；CRB 一级承包商（电信 / ICT / 安防）；KP Ramadhani Ndijuye（gmail，2024–2025 问 5 电口价、确认千兆、工业 16/24 口「可能会用到」）', 'TZ',
    'TZ · 1 次检索：ttel.co.tz/about（Tera Technologies and Engineering Limited；Mbezi beach Africana, Plot No. 2283, Block H Tarangire Street, Africana Drive, P.O. Box 31257；+255222701612；Eng.Dr.Daudi Charles Chief Executive Office and Co-Founder）+ devex.com（World Bank / TradeMark Africa 合同；Sinza Block A, Plot No. 173）+ 研究档领英（Certificate of Incorporation No: 85715；2011-09-09）；2026-10-29', 'https://ttel.co.tz/about',
    'Certificate of Incorporation No. 85715（公司自述；BRELA 未核）', '营业中（官网 + 中标记录）', '2011-09-09', 'Limited', '电信 / ICT / 安防 / 电力承包（达累斯萨拉姆 + 多多马）', 'Plot No. 2283, Block H, Tarangire Street, Africana Drive, Mbezi Beach, P.O. Box 31257, Dar es Salaam, Tanzania', '小型（11–50）',
    ['Ramadhani Ndijuye — 联系人（研究档 KP；rndijuye@gmail.com）= 收件人', 'Eng. Dr. Daudi Charles — CEO & Co-Founder（官网 about 2026-10-29；info@teratech.co.tz）'],
    '**CRB 一级 ICT 承包商 + 多次问价 → 集成商 25% B，一页纸一次（STI-054GP / STI-154GP 5 口工业 + STI-288DGGPM $137 / STC-2216GP 16 口 一口价 + MOQ 1 + 付费样机；抄 CEO 公共箱）' + TZ + '**；回信 → 加厚',
    '集成商 25%；一页纸一次（预付 100%）；坐实（证书号 + 官网地址 + CEO）。')
row('SB-229', 'TESCOM Company Limited（tescom.co.tz；**官网：Kijitonyama, Dar es Salaam；+255 712 565 698 / +255 738 261 794；info@；两条线 = ICT & 电信工程（电子围栏 / 门禁 / CCTV / 电动门 / Wi-Fi）+ 注册专业供应商（安防设备供货）**）；BRELA 号 1 查未得 → 部分坐实；KP Mossad Masheu；需求 1 光 2 电千兆 MC（不供）；WA 1 次无实质回复', 'TZ',
    'TZ · 1 次检索：tescom.co.tz（TESCOM COMPANY LIMITED；locally owned ICT and Telecommunication；Kijitonyama, Dar-es-salaam；+255 712 565698；+255 738 261794；info@tescom.co.tz）；BRELA 未得；2026-10-29', 'http://www.tescom.co.tz/',
    '未取（BRELA 号 1 查未得）', '营业中（官网在）', '未取', 'Limited', 'ICT / 电信工程 + 安防设备供应（达累斯萨拉姆）', 'Kijitonyama, Dar es Salaam, Tanzania', '小型',
    ['Mossad Masheu — 联系人（研究档 KP；samuisso@tescom.co.tz）= 收件人'],
    '**安防工程 + 供货两条线 → 集成商 25% B，一页纸一次（STC-028GP $28 / STC-228GP $33 CCTV PoE 一口价 + MOQ 1；千兆 MC 仅 STC-110XGE $65 明说）' + TZ + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；部分坐实（官网地址 + 电话；BRELA 未取）。')

# ---------------- IQ 3 ----------------
row('SB-080', 'Cyber-Tec（cyber-tec.net，域名已失效；**1 查无命中 → 未坐实**）— 伊拉克卡尔巴拉小型 IT / 网络公司；KP Sarmad Alwakil（yahoo 备用，WA 已加）；兴趣 TA510-FE 百兆工业收发器（不供）；19 次推送 1 次实质回复', 'IQ',
    'IQ · 1 次检索：「Cyber-Tec Karbala Iraq Sarmad Alwakil」→ 无相关结果（仅 Erbil 同类公司 / 新闻）；2026-10-29', '', '未取（1 查无命中）', '域名失效（存续待核）', '未取', '未取', 'IT / 网络（卡尔巴拉）', '未取（Karbala, Iraq）', '微型（推定）',
    ['Sarmad Alwakil — 联系人（研究档 KP；sarmad@cyber-tec.net / yahoo）'],
    '**需求百兆工业 MC（不供）+ 域名失效 + 19×1 → 不动（B 保留；来询按集成商 25% 报 STI-054GP）**' + IQ, '不动（产品不对位 + 存续待核）；未坐实。')
row('SB-588', 'WAN Company for Computer Network Design and Installation and Computer Trading Ltd.（DBA WAN Company for Networking Technology / WAN Networking Technology；wannt.co / wannt.krd；**D&B：1st Floor, Ali Namali Building, Salim Street, Sulaymaniyah；Managing Director Sarwar Ibrahim Saeed（= 研究档 KP ✓）；facebook / crunchbase：2005-01 创立，Teknim 品牌库区代理；在线商店 + WAN Academy + CCTV 展厅**）；登记号 1 查未得 → 部分坐实；表内 **PLANET 合作 10 年、Uniview 3 年**，需求千兆工业 PoE 4 / 8 / 16 口；WA 10 次无实质回复', 'IQ',
    'IQ · 1 次检索：dnb.com（WAN COMPANY FOR COMPUTER NETWORK DESIGN AND INSTALLATION AND COMPUTER TRADING LTD.；DBA WAN COMPANY FOR NETWORKING TECHNOLOGY；1st Floor, Ali Namali Building Salim Street Suleimani；Sarwar Ibrahim Saeed Managing Director）+ facebook.com/@WanCompany（founded in Jan 2005；info@wannt.co）+ crunchbase（Founded Jan 3, 2005；wannt.krd）；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.wan_company_for_computer_network_design_and_installation_and_computer_trading_ltd.5822f9dba5a299855fa2907040632e17.html',
    '未取（库区公司登记号 1 查未得）', '营业中（官网 + 社媒 2025）', '2005-01-03', 'Ltd', 'ICT 设备分销 / 集成 + 培训（苏莱曼尼亚）', '1st Floor, Ali Namali Building, Salim Street, Sulaymaniyah, Kurdistan Region, Iraq', '中小型',
    ['Sarwar Ibrahim Saeed — Managing Director / CEO（D&B 2026-10-29 吻合；研究档 KP sarwar.ibrahim@wannt.co）= 收件人'],
    '**PLANET 十年伙伴 + 明确需求千兆工业 PoE 4 / 8 / 16 → 分销 20% B，一页纸一次（STI-054GP / STI-288GPM $78.9 / STI-288DGGPM $137 / STI-488DGGPM $147 一口价 + MOQ 1 + 付费样机；PLANET / Uniview 不点名）' + IQ + '**；回信 → 加厚',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（D&B 法定名 + 地址 + MD；登记号未取）。')
row('SB-671', 'MyTec（my-tec.co / mytec-iq.com，域名失效；**1 查仅韩 / 秘 / 美同名 → 未坐实**）— 伊拉克 IT 公司；KP Mushtaq Al Takhakh；表内「有过详细产品交谈」；WA 19 次无实质回复', 'IQ',
    'IQ · 1 次检索：「MyTec Iraq mytec-iq.com Mushtaq」→ dnb MYTEC CO.,LTD.（釜山）/ linkedin Mytec（秘鲁仪表）/ MYTecSoft（美国）均非本户；2026-10-29', '', '未取（1 查未命中本体）', '域名失效（存续待核）', '未取', '未取', 'IT（伊拉克）', '未取（Iraq）', '小型（推定）',
    ['Mushtaq Al Takhakh — 联系人（研究档 KP；mushtaq@mytec-iq.com）'],
    '**域名失效 + 19×0 + 未坐实 → 不动（B 保留）**' + IQ, '不动（存续待核 + 19×0）；未坐实。')

# ---------------- NG 3 ----------------
row('SB-239', 'Empicstar（empicstar.com，域名失效；**gmail + 域名失效 → 0 查**）— 尼日利亚网络产品平台 / 转售（TP-Link / ONV 等牌）；2024-03 对商用 PoE 信息回「price」；18 次推送 1 次实质回复', 'NG',
    '0 查（gmail + 域名失效）；2026-10-29', '', '0 查', '域名失效（存续待核）', '未取', '未取', '网络产品转售（尼日利亚）', '未取', '微型（推定）',
    ['（未具名；empicstar2014@gmail.com；WA +234 803 428 6012）'],
    '**曾回「price」→ 分销 20% B，最后一次一页纸（STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1；在售品牌不点名）' + NG + '**；18×1 → 再无回声 → 不动',
    '分销 20%；最后一次一页纸（预付 100%）；0 查。')
row('SB-373', '尼日利亚 WhatsApp 联系人（**无邮箱 / 姓名 / 公司 → 0 查**）— 2024–2025 五次回复（问芯片、要价目、问「啥是 2.5G」、「MCU processor」），技术理解有限', 'NG',
    '0 查（无邮箱 / 公司）；2026-10-29', '', '0 查', '互动中（5 次）', '—', '未知', '未知（尼日利亚）', '未取', '未知',
    ['（未具名；仅 WA）'],
    '**5 次回复 → 集成商 25% B，WA 一页纸一次（STC-028GP $28 / STC-228GP $33 一口价 + MOQ 1；2.5G 等 SB-263 口径不报）+ 一句话问公司名' + NG + '**；再无回声 → 不动',
    '集成商 25%；WA 一页纸一次（预付 100%）；0 查。')
row('SB-631', 'Gigaxysafe Technologies Ltd（gigaxysafe.com.ng；**businesslist.com.ng / spiceworks：Suite 28F Sabondale Shopping Complex, Obafemi Awolowo Way, Jabi, Abuja；+234 803 930 8003 / +234 702 500 1983；MD Kayode Oluwaseyi；2012 年成立；约 10 人；注册安防技术公司（通信 / 安防设备进出口、分销、安装）；网店卖 Cisco / PLANET / Ubiquiti / 2.5G 16 口 + 太阳能**）；RC 号 1 查未得 → 部分坐实；自站 RFQ「RUCKUS Cisco Switch」；无跟进', 'NG',
    'NG · 1 次检索：businesslist.com.ng/company/266231（Gigaxysafe Technologies Ltd；Suit 28F Sabondale Shopping Complex, Obafemi Awolowo Way, Jabi, Abuja；+234 803 930 8003；MD kayode.oluwaseyi@gigaxysafe.com.ng；info@gigaxysafe.com.ng）+ spiceworks（registered security technology company；Founded 2012；Employees 10；Incorporated）；RC 未得；2026-10-29', 'https://www.businesslist.com.ng/company/266231/gigaxysafe-technologies-ltd',
    '未取（CAC RC 号 1 查未得）', '营业中（网店 2022+）', '2012', 'Ltd', '安防 / 通信设备进口分销 + 网店（阿布贾）', 'Suite 28F, Sabondale Shopping Complex, Obafemi Awolowo Way, Jabi, Abuja, Nigeria', '微型（约 10 人）',
    ['Kayode Oluwaseyi — Managing Director（businesslist 2022 公开页；kayode.oluwaseyi@gigaxysafe.com.ng）= 收件人（抄 info@gigaxysafe.com.ng）'],
    '**进口分销 + 网店（在售 PLANET / 2.5G）→ 分销 20% B，一页纸一次（STC-028GP $28 / STC-2216GP / STC-2224GP $86 / STC-4424GCPM $165 一口价 + MOQ 1 + 付费样机；在售品牌不点名；2.5G 不报）' + NG + '**；回信 → 加厚',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（名录地址 + MD + 成立年；RC 未取）。')

# ---------------- US 3 ----------------
row('SB-332', '自建站询盘人 Alex Malinovich（unpledged154@simplelogin.com = Proton 别名邮箱；**无公司 → 0 查**；WA 已加）— 询「2 光 8 PoE 管理 Vitesse」机型；无跟进', 'US',
    '0 查（别名邮箱 + 无公司）；2026-10-29', '', '0 查', '互动中（自建站询盘）', '—', '个人', '未知（美国）', '未取', '个人',
    ['Alex Malinovich — 自建站询盘人（研究档 KP；别名邮箱）'],
    '**明确机型需求 → 集成商 25% B，一页纸一次（STI-288DGGPM $137 2 SFP + 8 PoE L2 管理 一口价 + MOQ 1；芯片平台不声称）' + US + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；0 查（别名邮箱）。')
row('SB-476', '美国路易斯安那 Wayne（computerwayne@gmail.com；**个人邮箱 → 0 查**）— 需求工业 PoE 注入器（Red Lion 100-PoE 参照；不供）；1 次回复后 20 次跟进无果', 'US',
    '0 查（gmail + 无公司）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '个人', 'IT 服务（美国 +1 318）', '未取', '个人 / 微型',
    ['Wayne — 联系人（研究档；computerwayne@gmail.com）'],
    '**需求注入器（不供）+ 20×0 → 不动（B 保留）**' + US, '不动（产品不对位 + 20×0）；0 查。')
row('SB-701', '美国亚特兰大 Chavan Koya（chk999@outlook.com；**个人邮箱 → 0 查**；2022 注册 Alibaba）— 需求「1 光 8 口工业 PoE 非管理」；1 次回复后 14 次跟进无果；WA 加不上', 'US',
    '0 查（outlook + 无公司）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '个人', '未知（美国 +1 678）', '未取', '个人 / 微型',
    ['Chavan Koya — 来信署名人（研究档 KP；chk999@outlook.com）= 收件人'],
    '**明确机型需求 → 集成商 25% B，最后一次一页纸（STI-288GPM $78.9 1 SFP + 8 PoE 非管理 一口价 + MOQ 1）' + US + '**；14×0 → 再无回声 → 不动',
    '集成商 25%；最后一次一页纸（预付 100%）；0 查。')

# ---------------- GH 3 ----------------
row('SB-340', 'ROCKBIOS Limited（**仅 WA 电话 +233 26 465 3169，无邮箱 / 域名 → 0 查**）— 加纳转售商，KP Abraham Sam；2023-12 要价目（已发商业 + 电源册），2024-02 对 24 光 combo 信息回「price」；19 次推送 1 次实质回复', 'GH',
    '0 查（无邮箱 / 域名）；2026-10-29', '', '0 查', '互动中（1 次）', '—', 'Limited（表内）', '网络 / 安防产品转售（加纳）', '未取', '微型（推定）',
    ['Abraham Sam — WA 联系人（研究档 KP；无邮箱）= 收件人'],
    '**两次要价 → 分销 20% B，WA 最后一次一页纸（STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1；光端机不供明说）' + GH + '**；19×1 → 再无回声 → 不动',
    '分销 20%；WA 最后一次一页纸（预付 100%）；0 查。')
row('SB-587', 'Truetech Security Solutions（**仅 WA +233 20 497 9197，无邮箱 / 域名 → 0 查**；表内联系人「İbrahim Gürgüneş」疑串行录入）— 加纳安防公司；18 次 WA 1 次回复「在和 dja 合作」（已有供应商）', 'GH',
    '0 查（无邮箱 / 域名）；2026-10-29', '', '0 查', '互动中（1 次）', '—', '未取', '安防（加纳）', '未取', '微型（推定）',
    ['（联系人姓名待核；仅 WA）'],
    '**已有供应商 + 18×1 + 无 KP → 不动（B 保留）**' + GH, '不动（已有供应商 + 18×1）；0 查。')
row('SB-817', 'MassTrack Technologies / Masstrack（masstracktech.com，账户停用；**ZoomInfo：B33/41 Opposite Trinity Presby Church, Kwashieman, Accra；+233 20 648 5957；David Akoto = Technical Manager（2013 起）；ghanayello 2021：车辆跟踪设备供应商**）；RGD 号 1 查未得 → 部分坐实；2024-08 对 4 / 8 口工业 PoE 回「154」；WA 19 次无实质回复', 'GH',
    'GH · 1 次检索：zoominfo.com/p/David-Akoto（Technical Manager at MassTrack Technologies；2013-present；B33/41 Opposite Trinity Presby Church Kwashieman, Accra；+233 206485957）+ ghanayello.com/question/31146（Masstrack Technologies 车辆跟踪问答 2021）；RGD 未得；2026-10-29', 'https://www.zoominfo.com/p/David-Akoto/-2106421416',
    '未取（RGD 号 1 查未得）', '域名停用（名录在册）', '未取（KP 2013 起）', 'Limited（推定）', '车队 / 车辆跟踪技术服务（阿克拉）', 'B33/41 Opposite Trinity Presby Church, Kwashieman, Accra, Ghana', '小型',
    ['David Opoku Akoto — Technical Manager（ZoomInfo 2026-10-29；研究档 KP info@masstracktech.com）= 收件人'],
    '**曾点名「154」→ 集成商 25% B，WA 最后一次一页纸（STI-154GP 一口价 + STI-054GP + MOQ 1 + 付费样机）' + GH + '**；域名停用 + 19×0 → 再无回声 → 不动',
    '集成商 25%；WA 最后一次一页纸（预付 100%）；部分坐实（ZoomInfo 地址 + 职务；RGD 未取）。')

# ---------------- TR 3 ----------------
row('SB-563', 'ISAF 名片 Holil（+90 538 985 94 29，WA 已加；**无邮箱 / 公司 → 0 查**）— 要 PoE 交换机、拿了彩页；无跟进', 'TR',
    '0 查（无邮箱 / 公司）；2026-10-29', '', '0 查', '互动中（展会）', '—', '未知', '未知（土耳其）', '未取', '未知',
    ['Holil — ISAF 名片（研究档 KP；仅 WA）'],
    '**展会明确要 PoE 交换机 → 集成商 25% B，WA 一页纸一次（STC-028GP $28 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1）' + TR + '**；再无回声 → 不动',
    '集成商 25%；WA 一页纸一次（预付 100%）；0 查。')
row('SB-727', 'ISAF 名片 Fadi（姓氏待核；WA 已加；**无邮箱 / 公司 → 0 查**）— 问了收发器（SFP 不供）和交换机，英文不是很好；无跟进', 'TR',
    '0 查（无邮箱 / 公司）；2026-10-29', '', '0 查', '互动中（展会）', '—', '未知', '未知（土耳其）', '未取', '未知',
    ['Fadi — ISAF 名片（研究档 KP；仅 WA）'],
    '**问过交换机 → 集成商 25% B，WA 一页纸一次（STC-028GP $28 / STC-228GP $33 一口价 + MOQ 1；SFP 不供明说；短句英文）' + TR + '**；再无回声 → 不动',
    '集成商 25%；WA 一页纸一次（预付 100%）；0 查。')
row('SB-903', 'ISAF 名片 Necdet Şenkaya（bilecik@hotmail.com；**hotmail + 无公司 → 0 查**；疑比莱吉克省个体安装商）— 要工业级 PoE 交换机；无跟进', 'TR',
    '0 查（hotmail + 无公司）；2026-10-29', '', '0 查', '互动中（展会）', '—', '个体（推定）', '安装（土耳其，疑 Bilecik）', '未取', '个人',
    ['Necdet Şenkaya — ISAF 名片（研究档 KP；bilecik@hotmail.com）= 收件人'],
    '**展会要工业 PoE → 集成商 25% B，一页纸一次（STI-288GPM $78.9 / STI-154GP / STI-054GP 一口价 + MOQ 1）' + TR + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；0 查。')
