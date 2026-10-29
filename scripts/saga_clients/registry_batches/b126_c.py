# -*- coding: utf-8 -*-
"""第 126 批（T29-U118c，2026-10-29）—— **C 池三闸 · 闸 2 第三批**：闸 1 第 07 / 08 批候选中的四主区 + 波兰 28 户（US 13 / GB 8 / DE 3 / PL 4）查底数。
路径：US 名录（LeadIQ / SignalHire / Apollo / ZoomInfo / RocketReach / Crunchbase / PitchBook / buzzfile）+ SAM.gov（DCB UEI YX2BCLJKZ456）+ 官网 Business Profile（Grid Connect）；州登记号均未取 → US 常态「部分坐实」，法人名 + 地址 + 规模坐实；
GB Companies House 1 查即得（Euro Security Solutions 11094000）/ 名录（Blue Helix 04836349 aihitdata；Mayflex Holdings 06732855 endole；Videcon 1995 endole 营业额 £36.27M）；
DE unternehmen24 / creditreform（Fiber24 HRB 104376 Hamburg）+ 官网 company 页（1ST-embedded GmbH）+ 行业名录（EasyWind）；PL 官网自列 / bizraport / aleo（Assmann Distribution NIP 8951883569；Dipol KRS 0000094703；Batna/Extralink KRS 0001003926；NetTrans 个体 NIP 712-239-07-96）。
1 查未得：cctvvideo.com（仅返回 e-link 厂页）→ 未坐实。国别纠偏：SISEG USA 实为厄瓜多尔 Guayaquil 批发商 + 迈阿密 LLC；Streakwave 表内「加拿大」实为美国 San Jose。红旗：Ogar Technology（虚拟办公室 + 4 人 + 主销尼日利亚）；Blue Helix CH 04836349 名录标 SIC 99999 休眠（法人待核）。每户 1 查、depth 1。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 126
F = '2026-10-29'
EU = '— 欧洲常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ DAP（买方清关）或 FOB 深圳；周四 12–14 当地'
US = '— 北美常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ FOB 深圳 / DAP（买方清关）；周三 08–10 当地'
Q33 = '；洪瑞现供 → Q-33 口径（默认只推 SmartByte / Marvell 管理 + 工业线）'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 美国 ----------------
row('SC-2255', 'us', 'PoE Texas（poetexas.com；**LeadIQ / SignalHire / Apollo：11821 Buckner Rd, Austin TX 78726；2011 年创立；约 10 人；营收估 $1–10M；自有产品线 PoE 注入器 / 分离器 / 测试仪 / 电源，WiFi-Texas 母公司；CEO T. A.（= 表内 tandrews@）、CTO Joe Herbst（= 表内 jherbst@）；+1 512 479 0317**）；表内：在亚马逊卖 Utepo 商业 PoE；8 推 0 回；Simon 曾判不行', 'US',
    'US · 1 次检索：leadiq（Austin 地址；2011；2–10 人；Ceo T. A. / Cto J. H.）+ signalhire（$1–10M）+ apollo（Joe Herbst CTO）；TX SoS 未取；2026-10-29', 'https://leadiq.com/c/poe-texas/5e94745703157faf174e393d',
    '未取（TX SoS 未查）', '营业中（名录 2025）', '2011', 'LLC / Corp（推定）', 'PoE 配件自有品牌 + 亚马逊渠道（奥斯汀）', '11821 Buckner Rd, Austin, TX 78726', '微型 / 小型（约 10）',
    ['T. Andrews — CEO（tandrews@poetexas.com 表内 = 决策人直达）', 'Joe Herbst — CTO（jherbst@poetexas.com 表内）'],
    '**自有品牌 PoE 配件 + 已卖 Utepo → OEM 30% / 分销 20% 双轨：点名 CEO 一页纸一次（STC-028GP $28 / STC-228GP $33 + 丝印 MOQ + 付费样机；Utepo 不点名）' + US + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（自有品牌 + CEO / CTO 邮箱在表 + 进口经验）；部分坐实（州号未取）；Simon 曾判不行。')
row('SC-2402', 'other', 'SISTEMAS DE SEGURIDAD S.A. — SISEGUSA（sisegusa.com；**官网：厄瓜多尔 Guayaquil, Urdesa Central, Av. Las Lomas 403；+593 4 371 2850；安防 / 网络批发（CCTV / 对讲 / 门禁 / 报警 / 路由）；ventasdeseguridad 名录：进口 + 分销 + 培训；关联 Siseg Global Solutions = 迈阿密注册 LLC（电商 / 3PL，服务拉美）**）→ 国别纠偏：美国 → 厄瓜多尔（经迈阿密进口）；表内：Utepo 商业 PoE；19 推 0 回；Simon 曾判不行', 'EC',
    'EC · 1 次检索：sisegusa.com/home（Guayaquil 地址 / 电话）+ sisegglobal.com（Miami LLC）+ ventasdeseguridad 名录；RUC 未取；2026-10-29', 'https://www.sisegusa.com/home',
    '未取（RUC 未查）', '营业中（官网在线）', '未取', 'S.A.（+ 美国 LLC）', '安防 / 网络批发（厄瓜多尔；迈阿密转运）', 'Urdesa Central, Av. Las Lomas 403, Guayaquil, Ecuador', '小型（推定）',
    ['j.linares@sisegusa.com（表内具名；职务未取）', '（info@sisegusa.com 官网公开）'],
    '**拉美批发（区域外）→ 分销 20%：一页纸一次（STC-028GP / STC-228GP + MOQ 1 + 付费样机；FOB 深圳 / 迈阿密 DAP）' + US + '**；区域外低优先',
    '分销 20%；P 池候选 △（进口 Utepo ✔ 对位 ✔ 坐实 ✔，区域外 → 观察档）；部分坐实；国别纠偏 EC；Simon 曾判不行。')
row('SC-2418', 'us', 'Streakwave Wireless, Inc.（streakwave.com；**官网 Our Story + siliconmaps：全球增值分销商，总部 840 Jury Court, San Jose CA 95112，分仓 Salt Lake City / Cincinnati / 墨尔本 / 新西兰；无线宽带 / 电信 / IP 监控 / 绿色能源全线；服务 WISP / 集成商 / VAR**）→ 国别纠偏：表内「加拿大」→ 美国；表内：卖很多牌子（商业 PoE / 工业 FS / SFP）；1 推 0 回；Simon 曾判不行', 'US',
    'US · 1 次检索：streakwave.com/about.asp（San Jose HQ + 分仓）+ siliconmaps（840 Jury Court；888-604-5234）；CA SoS 未取；2026-10-29', 'https://streakwave.com/about.asp',
    '未取（CA SoS 未查）', '营业中（官网 2022 版权）', '未取', 'Inc.', '无线 / 网络 / 安防增值分销（多仓；北美 + 澳新）', '840 Jury Court, San Jose, CA 95112', '中型（多仓分销）',
    ['（sales@ / info@streakwave.com 表内总邮箱；采购 KP 待 LinkedIn）'],
    '**大分销 → 分销 20%（长线）：一页纸一次（WISP 配套：STI-154GP 工业 PoE + STC-228GP + MOQ 1 + 付费样机）' + US + '**；Simon 可否决',
    '分销 20%；P 池候选 ○（中型分销 + 对位；冷）；部分坐实；国别纠偏 US；Simon 曾判不行。')
row('SC-2429', 'us', 'El Paso Communication Systems, Inc. — EPCOM（epcom.net；**buzzfile：1630 E Paisano Dr, El Paso TX 79901；1987 年创立；Texas 公司；本部约 60 人 / 全部 95 人；营收约 $23.7M；进口 + 出口 + 制造；少数族裔企业；LeadIQ：29 年经验、San Antonio / El Paso / Miami 三仓、99% 当日发货、51–200 人**）；表内：PLANET 商用 + 工业两线备货、Wi-Tek 在用；研究档对位 STC-424DGGM；8 推 0 回；Simon 曾判不行', 'US',
    'US · 1 次检索：buzzfile（1987；Texas；95 人；$23.7M；1630 E Paisano Dr）+ leadiq（三仓；51–200）+ datanyze；TX SoS 号未取；2026-10-29', 'https://www.buzzfile.com/business/Epcom-915-533-5119',
    '未取（TX SoS 号未查；法人名已坐实）', '营业中', '1987', 'Inc.（Texas）', '无线电 / 无线网络 / 电子安防分销（Syscom 美方；三仓）', '1630 E Paisano Dr, El Paso, TX 79901', '中型（95 人；$23.7M）',
    ['（purchasing@epcom.net 表内 = 采购部直达；sales@ 表内；具名采购 KP 待 LinkedIn）'],
    '**PLANET 双线分销 → 分销 20%：点名 purchasing@ 一页纸一次（STC-424DGGM 对标 Planet 同口型 + STI-288GPM 工业 + MOQ 1 + 付费样机）' + US + '**；Simon 可否决',
    '分销 20%；P 池候选 ★（中型分销 + Planet 渠道 + 采购邮箱在表）；坐实（法人 + 地址 + 规模）；Simon 曾判不行。')
row('SC-2542', 'us', 'Grid Connect, Inc.（gridconnect.com；**官网 Business Profile：1630 W Diehl Rd, Naperville IL 60563；2002 年创立；25 人；ISO 9001:2015；工业网络分销 + 自有品牌 GRID 产品（Naperville 组装）+ 白标设备 / 定制 IoT 硬件；创始人兼总裁 Mike Justice、CEO Adam Justice、COO Anthony Linder；(630) 245-1445；sales@gridconnect.com**）；表内：Atop 的；完整地址 + 直线电话；互动过；Simon 曾判不行', 'US',
    'US · 1 次检索：gridconnect.com/pages/grid-connect-inc-business-profile（法人 / 地址 / 2002 / 25 人 / 高管）+ linkedin（11–50）+ 官网 Who is Grid Connect（分销起家 → GRID 自有产品）；IL SoS 未取；2026-10-29', 'https://www.gridconnect.com/pages/grid-connect-inc-business-profile',
    '未取（IL SoS 未查）', '营业中（官网 2026）', '2002', 'Inc.（私有）', '工业网络分销 + 自有品牌 GRID + 白标 / 定制 IoT', '1630 W Diehl Rd, Naperville, IL 60563', '小型（25）',
    ['Mike Justice — Founder & President', 'Adam Justice — CEO', 'Anthony Linder — COO', 'jeanineh@gridconnect.com（表内具名；职务未取）'],
    '**分销 + 自有品牌 + 白标 → OEM 30% / 分销 20% 双轨：点名 Adam Justice 一页纸一次（STI-154GP / STI-288GPM 工业 + 丝印 MOQ + 付费样机；Atop 不点名）' + US + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（自有品牌 + 白标业务 + 高管具名）；坐实（官网法人档案）；Simon 曾判不行。')
row('SC-2597', 'us', 'Urban Security Group — cctv.supplies / cctv.nyc（**官网 About：布鲁克林家族小企业，40+ 年；CCTV 批发 + 零售 + 安装；718-701-5850**）；法人注册号未取 → 部分坐实；表内：商业 PoE 主要是洪瑞的；20 推 0 回；Simon 曾判不行', 'US',
    'US · 1 次检索：cctv.supplies 首页 About Us（Urban Security Group；Brooklyn；40+ 年；718-701-5850）；NY DOS 未取；2026-10-29', 'https://www.cctv.supplies/',
    '未取（NY DOS 未查）', '营业中（官网 2026-03）', '未取（40+ 年）', '未取（家族企业）', 'CCTV 批发 / 零售 / 安装（纽约）', 'Brooklyn, New York', '微型 / 小型',
    ['（support@cctv.nyc 表内；具名 KP 未取）'],
    '**安防批零 → 分销 20%：一页纸一次（STC-028GP $28 / STC-228GP $33 + MOQ 1 + 付费样机）' + US + Q33 + '**；Simon 可否决',
    '分销 20%；P 池候选 △（进口洪瑞 ✔ 主区 ✔ 对位 ✔；微型 → 观察档）；部分坐实；Simon 曾判不行；Q-33。')
row('SC-2606', 'us', 'Logicbus, Inc.（logicbus.com；**Crunchbase：法人 Logicbus, Inc.，Chula Vista CA，Active，11–50；官网 Support：2001 年创立，863 Bowsprit Road Chula Vista；ContactOut：San Diego 8268 Clairemont Mesa Blvd Suite 302 + 墨西哥瓜达拉哈拉办公室，40 人；CEO Blasioz Valenzuela；Daniel Flores — Gerente de Sucursal México（= 表内 danielflores@）；Luis Eduardo Rodríguez — Ejecutivo de compras**）；表内：Atop / 三旺工业 FS 电口；20 推 0 回；Simon 曾判不行', 'US',
    'US · 1 次检索：crunchbase（Logicbus, Inc.；Active；11–50）+ logicbus.com/support（2001；Chula Vista）+ contactout（40 人；高管 / 采购）；CA SoS 未取；2026-10-29', 'https://www.crunchbase.com/organization/logicbus',
    '未取（CA SoS 未查）', 'Active（Crunchbase）', '2001', 'Inc.', '工业自动化 / 工业通信分销（美墨双边）', '863 Bowsprit Road, Chula Vista, CA（+ San Diego / Guadalajara）', '小型（40）',
    ['Blasioz Valenzuela — CEO', 'Daniel Flores — Gerente de Sucursal México（danielflores@logicbus.com 表内）', 'Luis Eduardo Rodríguez Luvian — Ejecutivo de compras（采购）', 'teodoro@logicbus.com（表内具名；职务未取）'],
    '**工业分销（美墨）→ 分销 20%：点名 Daniel Flores 一页纸一次（STI-154GP / STI-280GE 工业电口对标 Atop / 三旺 + MOQ 1 + 付费样机）' + US + '**；Simon 可否决',
    '分销 20%；P 池候选 ○（工业分销 + 进口中国工业品牌 + 具名 KP）；坐实；Simon 曾判不行。')
row('SC-2619', 'us', 'Alantek Communications（alantekusa.com；**ZoomInfo：Alantek Communications Asia Pte Ltd；4639 Sandydale Ln, Houston TX 77039；1–10 人；营收 <$5M；官网 About：1998 年创立、「总部美国」、光纤 / LAN 无源布线制造商，经授权分销商销售**）→ 实为亚洲运营的布线品牌美国壳；表内：工业 FS / PoE / MC 周边；Simon 曾判不行', 'US',
    'US · 1 次检索：alantekusa.com/about-us + zoominfo（Asia Pte Ltd；Houston；1–10；<$5M）；2026-10-29', 'https://www.alantekusa.com/about-us/',
    '未取', '营业中（官网 2020 更新）', '1998', 'Pte Ltd（新加坡）+ 美国联络地址', '无源布线 / 光纤品牌（主销亚洲 / 中东渠道）', '4639 Sandydale Ln, Houston, TX 77039', '微型（1–10）',
    ['（info@alantekusa.com 表内；具名 KP 未取）'],
    '**微型品牌壳、以无源为主 → 不动；回 C 储备**' + US, '不动；回 C；部分坐实；Simon 曾判不行。')
row('SC-2622', 'us', 'cctvvideo.com（support@；**1 查「cctvvideo.com」仅返回 e-link China 厂页（其供货商）→ 公司本体未坐实**）；表内：VC / SFP / 工业 FS，有 e-link 的；Simon 曾判不行', 'US',
    'US · 1 次检索无命中（仅 e-link 供货商页）；2026-10-29', '',
    '未取（1 查无命中）', '存续待核（域名 MX 正常）', '未取', '未取', '安防 / 光传输网店（美国，推定）', '未取', '微型（推定）',
    ['（support@cctvvideo.com 表内；具名 KP 未取）'],
    '**未坐实 + Simon 判不行 → 不动，回 C 储备**' + US, '不动；回 C；未坐实。')
row('SC-2657', 'us', 'Lynn Electronics Corporation / Inc.（lynnelec.com / thinklynn.com；**RocketReach：154 Railroad Dr, Ivyland PA 18974；1964 年创立；营收 $18.6M；29 人（konaequity 108 人 / Indeed 51–200）；(215) 355-8200；Shad Sechrist — Director, Data Center Solutions；konaequity：Walter Corrar 经理、Marci Price 区域销售**）；表内：MC / switch / SFP，从 VOLKTEK 买 MC；kedsall@thinklynn.com 具名；11 推 0 回；Simon 曾判不行', 'US',
    'US · 1 次检索：rocketreach（1964；$18.6M；29；Ivyland）+ konaequity（108 人；wcorrar@ / mprice@ 公开）+ indeed（51–200）；PA 登记号未取；2026-10-29', 'https://rocketreach.co/lynn-electronics-corporation-profile_b44d75e7fd255469',
    '未取（PA 登记号未查）', '营业中（2025 营收数据）', '1964', 'Corporation', '连接 / 网络产品制造 + 分销（自有品牌；数据中心方案线）', '154 Railroad Dr, Ivyland, PA 18974', '中型（29–108；$18.6M）',
    ['Shad Sechrist — Director, Data Center Solutions（DC 线 KP）', 'kedsall@thinklynn.com（表内具名；职务未取）', 'Walter Corrar — Manager（wcorrar@lynnelec.com 公开）'],
    '**自有品牌 + 进口 Volktek + DC 方案线 → OEM 30%：点名 Shad Sechrist 一页纸一次（STC-110XGE 10G MC + STC-424XGGM 对标 + 丝印 MOQ；CENTEC STH 线作敲门砖提一句）' + US + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（中型自有品牌 + 进口经验 + DC 线 KP）；坐实（名录三源一致）；Simon 曾判不行。')
row('SC-284', 'us', 'Data Comm for Business, Inc. — DCB（dcbnet.com；**GovTribe / SAM.gov：UEI YX2BCLJKZ456、CAGE 0GGX7，注册 2002-02-04，有效至 2027-07-08；2949 County Road 1000 E, Dewey IL 61840（+ Plano TX 办公室）；1981 年创立；1–10 / 11–50 人；营收估 $1–10M；NAICS 334210 电话设备制造；联邦交通领域供应商；LinkedIn：Brad Boles VP Sales & Systems；RocketReach：Dan Smith VP Sales**）；表内：有自己一套型号、「感觉还行」；mgadel@ / rpeterson@ 具名；19 推 0 回', 'US',
    'US · 1 次检索：govtribe（UEI / CAGE / SAM 有效期 / 地址 / 1981）+ linkedin（11–50；Plano）+ rocketreach；IL SoS 未取；2026-10-29', 'https://govtribe.com/vendors/data-comm-for-business-incorporated-0ggx7',
    'UEI YX2BCLJKZ456 / CAGE 0GGX7', 'SAM.gov Active（至 2027-07-08）', '1981', 'Inc.', '数据通信设备自研 + 集成（串口 / 加密 / SCADA；联邦客户）', '2949 County Road 1000 E, Dewey, IL 61840', '小型（1–50）',
    ['Brad Boles — VP Sales & Systems', 'Dan Smith — VP Sales', 'mgadel@dcbnet.com / rpeterson@dcbnet.com（表内具名；职务未取）'],
    '**自研厂商 + 联邦客户（TAA 门槛）→ OEM 30% 观察：一页纸一次（STI-154GP 工业 PoE 作其 SCADA 配套 + 丝印 MOQ；不提 NDAA / TAA）' + US + '**；联邦项目不碰',
    'OEM 30%；P 池候选 △（自有型号 ✔ 主区 ✔ 对位 ✔，但联邦导向 TAA 门槛 → 观察档）；坐实（SAM.gov）。')
row('SC-2993', 'us', 'Cables N More（cablesnmore.com / tlnetworx.com；**ZoomInfo：550 Commerce Dr, Quakertown PA 18951；(215) 259-5279；11–50 人；Crunchbase：1–10，计算机 / 音视频线缆 + 消费电子 + 网络安装设备销售商**）；法人注册号未取 → 部分坐实；表内：宇航的工业 FS、MC 好几个外壳、SFP，**自己的 logo 和型号**；17 推 0 回 + 退信；Simon 曾判不行', 'US',
    'US · 1 次检索：zoominfo（Quakertown 地址 / 电话 / 11–50）+ crunchbase（1–10）；PA 登记号未取；2026-10-29', 'https://www.zoominfo.com/c/cables-n-more/15567269',
    '未取（PA 登记号未查）', '营业中（名录）', '未取', 'LLC / Inc.（推定）', '线缆 / 网络设备网店 + 自有 logo 贴牌（宾州）', '550 Commerce Dr, Quakertown, PA 18951', '小型（1–50）',
    ['（customerservice@cablesnmore.com / info@tlnetworx.com 表内；具名 KP 未取 → LinkedIn 找 owner）'],
    '**自有 logo 型号 + 进口宇航 → OEM 30%：找 owner 后一页纸一次（STC-110XGE MC + STI-154GP 工业 + 丝印 / 彩盒 MOQ + 付费样机）' + US + '**；Simon 可否决',
    'OEM 30%；P 池候选 ○（自有 logo 贴牌 + 进口经验；小型、退信待换地址）；部分坐实；Simon 曾判不行。')
row('SC-503', 'us', 'LUTZE Inc.（lutze.com；**PitchBook / BounceWatch / Wiza：13330 South Ridge Drive, Charlotte NC 28273；1982 / 1989 创立；73–77 人；Friedrich Lütze GmbH（德国 Weinstadt）北美总部；工业线缆 / 电源 / 断路器 / 网络产品；总裁 Juergen Seybold、北美销售总监 Brad Meeks、业务发展经理 Ray Eksir；经授权分销商销售**）；表内：工业 FS 自己的 PVC 膜和编号（自有品牌贴牌）；sgregson@ 具名；11 推 0 回；表内标「体量过大」', 'US',
    'US · 1 次检索：pitchbook（Charlotte；73 人；1989）+ bouncewatch（77 人；1982；北美总部）+ wiza（高管名单）；NC SoS 未取；2026-10-29', 'https://pitchbook.com/profiles/company/120730-78',
    '未取（NC SoS 未查）', '营业中（2025 名录）', '1982（美国公司）', 'Inc.（德国 Lütze 集团子公司）', '工业自动化连接 / 控制产品制造 + 自有品牌网络产品', '13330 South Ridge Drive, Charlotte, NC 28273', '中型（73–77；集团约 500）',
    ['Juergen Seybold — President', 'Brad Meeks — Director of Sales, North America', 'Ray Eksir — Business Development Manager', 'sgregson@lutze.com（表内具名；职务未取）'],
    '**自有品牌工业交换机（贴牌）→ OEM 30%：点名产品 / 采购 KP 一页纸一次（STI-154GP / STI-288GPM / STI-488DGGPM 工业线对标 + 丝印 PVC 膜 MOQ + 付费样机；集团采购在德国 → 同时核 Weinstadt 总部）' + US + '**',
    'OEM 30%；P 池候选 ★（品牌商自有工业线 = 目标顺位 1；中型非巨头）；坐实（名录三源一致）。')
# ---------------- 英国 ----------------
row('SC-2383', 'gb', '3G Router Store — Westlake Communications Ltd / Millbeck Communications（3grouterstore.co.uk；**ZoomInfo：Westlake Communications Ltd，Essex，+44 1708 388799；tuugo：D10 & D11 Seedbed Centre, Davidson Way, Romford RM7 0AZ；LinkedIn：Millbeck Communications 2002 年创立、2–10 人、运营 3GRouterStore 网店 + 自有品牌 Proroute 路由器 / Fullband 天线、Teltonika 合作**）；Companies House 号未取 → 部分坐实；表内：商业 PoE 主要是洪瑞的；18 推 0 回；Simon 曾判不行', 'GB',
    'GB · 1 次检索：zoominfo（Westlake Communications Ltd）+ tuugo（Romford 地址）+ linkedin（Millbeck；Proroute / Fullband 自有品牌；2002）；CH 号未取；2026-10-29', 'https://gh.linkedin.com/company/millbeck-communications',
    '未取（CH 1 查未得；两法人名待分辨）', '营业中（网店在线）', '2002', 'Ltd', 'IoT / 4G-5G 路由器网店 + 自有品牌（Proroute / Fullband）', 'D10 & D11 Seedbed Centre, Davidson Way, Romford, Essex RM7 0AZ', '微型（2–10）',
    ['（sales@3grouterstore.co.uk 表内；具名 KP 未取）'],
    '**自有品牌路由 / 天线贴牌 + 卖洪瑞 PoE → OEM 30% / 分销 20%：一页纸一次（STC-028GP / STI-154GP 工业 PoE 配 4G 路由场景 + 丝印 MOQ）' + EU + Q33 + '**；Simon 可否决',
    'OEM 30%；P 池候选 ○（自有品牌 ✔ 进口经验 ✔ 主区 ✔；微型）；部分坐实；Simon 曾判不行；Q-33。')
row('SC-2608', 'gb', 'Mayflex（mayflex.com；**PitchBook：Excel House, Junction Six Industrial Park, Electric Avenue, Birmingham B6 7JJ；1917 年创立；250 人；Sonepar UK 子公司；数据通信产品分销（安装商 / 集成商）；Endole：Mayflex Holdings Limited 06732855（2008-10-24，Sonepar 集团）；自有品牌 Excel Networking**）；表内：商业 PoE；andrew.percival@ 具名；19 推 0 回；Simon 曾判不行', 'GB',
    'GB · 1 次检索：pitchbook（Birmingham；1917；250；Sonepar UK）+ endole（Mayflex Holdings 06732855）+ glassdoor；运营公司 CH 号未取；2026-10-29', 'https://pitchbook.com/profiles/company/65358-73',
    'Mayflex Holdings Ltd 06732855（控股；运营公司号未取）', 'Active（Sonepar 集团）', '1917（控股 2008-10-24）', 'Ltd（Sonepar UK 子公司）', '布线 / 网络 / 安防分销 + 自有品牌 Excel', 'Excel House, Junction Six Industrial Park, Electric Avenue, Birmingham B6 7JJ', '大型（250；母公司 Sonepar 巨头）',
    ['Andrew Percival（andrew.percival@mayflex.com 表内具名；职务未取）', '（sales@mayflex.com 表内）'],
    '**巨头旗下自有品牌 Excel → OEM 30% 长线：点名 Andrew Percival / Excel 产品经理一页纸一次（STC-228GP / STC-2224GP 对标 Excel 口型 + 丝印彩盒 MOQ + 付费样机）' + EU + '**；Simon 可否决；集团采购流程长',
    'OEM 30%；P 池候选 △（自有品牌 ✔ 主区 ✔ 具名 KP ✔，但 Sonepar 巨头体系 → 长线观察档）；坐实（名录）；Simon 曾判不行。')
row('SC-2728', 'gb', 'Blue Helix Limited（bluehelix.co.uk；**aihitdata：CH 04836349，Votec House, Hambridge Lane, Newbury RG14 5TN；CEO Steven Westbrook、秘书 Leo Yu；VAT 927 2027 36；名录标 SIC 99999（Dormant）；另有注册号 06248590；laserfocusworld（2018）：Crawley RH11 0PH，28 人；官网：AMG Systems / ComNet / D-Link / Trend Networks 光纤 + 铜缆方案分销，面向数据中心 / 安防 / 公用 / 国防 / 政府客户**）→ 法人状态待核；表内：主要卖 AMG / Comnet；marke@ 具名；19 推 0 回；Simon 曾判不行', 'GB',
    'GB · 1 次检索：aihitdata（04836349；SIC 99999；Newbury；Westbrook）+ bluehelix.co.uk 品类页（AMG 108 / ComNet 110 / D-Link 132 SKU）+ laserfocusworld（28 人）；CH 直查未做；2026-10-29', 'https://www.aihitdata.com/company/0034F506/blue-helix/overview',
    '04836349（名录标 Dormant；另 06248590 待核）', '待核（名录 SIC 99999 休眠 vs 官网在营）', '2003（推定，20 年）', 'Ltd', '工业 / 安防网络 + 布线分销（AMG / ComNet / D-Link）', 'Votec House, Hambridge Lane, Newbury RG14 5TN', '小型（28）',
    ['Steven Westbrook — CEO / Director', 'marke@bluehelix.co.uk（表内具名；职务未取）'],
    '**工业网络分销 → 分销 20%：先 CH 直查两号分清运营主体，再点名 marke@ 一页纸一次（STI-154GP / STI-288GPM 对标 AMG / ComNet 口型 + MOQ 1 + 付费样机）' + EU + '**；法人未清前 预付 100%',
    '分销 20%；P 池候选 △（分销主体 ✔ 主区 ✔ 对位 ✔，但法人状态存疑 → 观察档 + 预付）；部分坐实；Simon 曾判不行。')
row('SC-2802', 'gb', 'EURO SECURITY SOLUTIONS LIMITED（eurosecuritysolutions.co.uk；**Companies House 11094000；2 Guillemot Court, Taylor Close, London SE8 5UU；2017-12-04 成立；Active；SIC 62020 IT 咨询 + 80200 安防系统服务；最近账目至 2023-12-31；2024 年账目应于 2025-09-30 前递交（页面快照时未见 → 是否逾期待核）**）；表内：展会很在意 AC/DC 输入、问 VC 用法、要 full info、想拿样；退信；WA 号在表', 'GB',
    'GB · 1 次检索：find-and-update.company-information.service.gov.uk/company/11094000；2026-10-29', 'https://find-and-update.company-information.service.gov.uk/company/11094000',
    '11094000', 'Active（2024 账目递交情况待核）', '2017-12-04', 'Private limited company', 'IT 咨询 + 安防系统服务（伦敦；疑似住宅注册地址）', '2 Guillemot Court, Taylor Close, London SE8 5UU', '微型（推定）',
    ['（info@eurosecuritysolutions.co.uk 表内曾退信；WA +44 7830 323788 表内 → 改走 WA）'],
    '**样品意向户 → 集成商 25%：WA 续上展会话题一次（AC/DC 双输入 STI-154GP 工业 + VC 用法说明 + 付费样机）' + EU + '**；微型 → 预付 100%',
    '集成商 25%；P 池候选 △（样品意向 ✔ 主区 ✔ 对位 ✔；微型 + 退信 → 观察档 WA 触达）；坐实（CH）。')
row('SC-2809', 'gb', 'Ogar Technology Limited（ogartechnology.com；**RocketReach：36-37 Albert Embankment, Suite 7, Vintage House, London SE1 7TL（虚拟办公室型地址）；2015 年创立；4 人；CEO / MD Sunday Ogar；EC21：分支 Ogar Technology Consulting Ltd（尼日利亚 Ikeja Computer Village）+ Ogar Technology LLC（美国 8 The Green = 注册代理地址）；自称安防 / 太阳能设备制造商**）→ 红旗：微型 + 虚拟地址 + 主销尼日利亚；表内：商业 PoE 看着像 ONV 的；17 推 0 回 + 退信；Simon 曾判不行', 'GB',
    'GB · 1 次检索：rocketreach（London 地址；4 人；2015；Sunday Ogar）+ crunchbase + ec21 分支页；CH 号未取；2026-10-29', 'https://rocketreach.co/ogar-technology-profile_b45d2847fc628fbd',
    '未取（CH 号未查）', '营业中（名录）', '2015', 'Ltd', '安防 / 太阳能贸易（伦敦壳 + 尼日利亚销售）', '36-37 Albert Embankment, Suite 7, London SE1 7TL（虚拟）', '微型（4）',
    ['Sunday Ogar — Managing Director & CEO'],
    '**红旗（虚拟地址 + 微型 + 主销尼日利亚）→ 不动；回 C 储备**' + EU, '不动；回 C；部分坐实（红旗）；Simon 曾判不行。')
row('SC-2954', 'gb', 'Videcon Ltd（videcon.co.uk；**Endole：1995-07-31 成立，Active，Heckmondwike West Yorkshire，营业额 £36.27M；Tracxn：150 人，自有品牌 Concept Pro（1998 起，IP / AHD / 模拟 CCTV），ISO 9001 分销；prospeo：WF16 0PN，+44 1924 528000，分销 Concept Pro / UNV / Apollo / Advanced / Hochiki / Ajax / WD / CDVI**）；CH 号未取；表内：CCTV 为主、有商业 PoE；退信；Simon 曾判不行', 'GB',
    'GB · 1 次检索：endole 品牌页（Videcon Ltd；1995；£36.27M）+ tracxn（150 人；Concept Pro）+ prospeo（地址 / 电话）；CH 号未取；2026-10-29', 'https://open.endole.co.uk/insight/brand/206497-videcon',
    '未取（CH 号 1 查未得；法人名 Videcon Ltd 坐实）', 'Active', '1995-07-31', 'Ltd', '安防分销 + 自有品牌 Concept Pro（trade-only）', 'Heckmondwike, West Yorkshire WF16 0PN', '中型（150；£36M）',
    ['（sales@videcon.co.uk 表内曾退信；Concept Pro 产品经理 KP 待 LinkedIn）'],
    '**自有品牌 Concept Pro + 中型分销 → OEM 30%：找产品经理后一页纸一次（STC-028GP / STC-228GP / STC-2224GP 安防 PoE 丝印彩盒 MOQ + 付费样机）' + EU + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（自有品牌 + 中型分销 + 主区）；坐实（法人 + 营业额）；Simon 曾判不行。')
row('SC-2976', 'gb', 'Blake UK Ltd（blake-uk.com；**PitchBook：1971 年创立，Sheffield，20 人，曾用名 Blake Aerials Limited，私募债融资；NPIF（2017）：24 人、营业额 £2.2M（2016 财年）、天线制造 + 进口商（RF / 电子 / 元件）；ZoomInfo：TV 信号 / CCTV / Wi-Fi 产品设计制造，11–50，<$5M**）；CH 号未取；表内：CCTV / networking / fiber 销售平台；Simon 曾判不行', 'GB',
    'GB · 1 次检索：pitchbook（1971；20 人；Sheffield）+ npif.co.uk（24 人；£2.2M）+ zoominfo（11–50）；CH 号未取；2026-10-29', 'https://pitchbook.com/profiles/company/179962-84',
    '未取（CH 号 1 查未得；法人名 Blake UK Ltd）', '营业中', '1971', 'Ltd', '天线 / 信号分配 / CCTV / 网络产品制造 + 进口分销（谢菲尔德）', 'Sheffield, South Yorkshire', '小型（20–24；£2.2M）',
    ['Paul Blake — MD（NPIF 报道）', 'Cavin Carver — Operations Director（NPIF 报道）', '（sales@blake-uk.com 表内）'],
    '**制造 + 进口商（自有品牌 Blake）→ OEM 30% / 分销 20%：点名 Paul Blake 一页纸一次（STC-028GP / STC-228GP 安防 PoE + 丝印 MOQ + 付费样机）' + EU + '**；Simon 可否决',
    '分销 20% / OEM 30%；P 池候选 ○（进口商 + 自有品牌 + 主区；小型）；部分坐实；Simon 曾判不行。')
row('SC-331', 'gb', 'Industrial Communication Products Ltd — IndustrialComms（industrialcomms.com；**官网 Press 页脚：The Angel Business Centre, 1 Luton Road, Toddington, Bedfordshire LU5 6DE；Advantech 英国分销 + INSYS icom 分销协议 + Bobcat 交换机；ZoomInfo：2008 年创立、<$5M；modernrailways：服务铁路基础设施 + 机车车辆（EN50155 交换机）**）；CH 号未取；表内：bypass / 工业 FS 基本是研华的；名单内未触达', 'GB',
    'GB · 1 次检索：industrialcomms.com/pages/press（法人 + 地址 + Advantech / INSYS）+ zoominfo（2008）+ modernrailways（铁路）；CH 号未取；2026-10-29', 'https://www.industrialcomms.com/pages/press',
    '未取（CH 号 1 查未得；法人名坐实）', '营业中（官网 2025 版权）', '2008', 'Ltd', '工业通信产品分销（Advantech / INSYS；公用 / 交通 / 铁路）', 'The Angel Business Centre, 1 Luton Road, Toddington, Bedfordshire LU5 6DE', '小型（推定）',
    ['（sales@industrialcomms.com 表内；具名 KP 未取）'],
    '**工业分销（铁路占比高，守界只做非轨交场景）→ 分销 20%：一页纸一次（STI-154GP / STI-288GPM 公用 / 交通路侧场景 + MOQ 1 + 付费样机；不提 EN50155）' + EU + '**',
    '分销 20%；P 池候选 ○（工业分销 + 进口台湾品牌 + 主区；冷户 §5 四条）；部分坐实；守界注记：轨交项目不碰。')
# ---------------- 德国 ----------------
row('SC-2262', 'de', '1ST-embedded GmbH（1st-embedded.com / supersrv.de；**官网 company 页：2010 年 7 月成立；Neu Wulmstorf（汉堡都市圈）；CEO Sven Trommer（Dipl.-Ing.；= 表内 sven.trommer@）；嵌入式 PC / 5G 路由 / 交换机 / 网关 / 网络安全 / 光电器件的系统集成商 + 分销商；+49 40 7003550；info@1ST-embedded.com**）；HRB 未取；表内：ISON 的，少量工业电口；3 推 0 回；Simon 曾判不行', 'DE',
    'DE · 1 次检索：v22018035980363305.supersrv.de/company（2010-07；Neu Wulmstorf；Sven Trommer CEO；+49 40 7003550）；HRB 未取；2026-10-29', 'https://v22018035980363305.supersrv.de/company',
    '未取（HRB 1 查未得）', '营业中（官网 + 网店在线）', '2010-07', 'GmbH', '嵌入式 / 工业网络系统集成 + 分销（汉堡）', 'Neu Wulmstorf, Metropolregion Hamburg', '微型 / 小型',
    ['Sven Trommer — CEO / Geschäftsführer（sven.trommer@1st-embedded.com 表内 = 决策人直达）', 'Jelena Dronowa — Head of Digital Media'],
    '**集成 + 分销（已进口 ISON）→ 分销 20%：点名 Sven Trommer 一页纸一次（STI-154GP / STI-280GE 工业电口对标 ISON + MOQ 1 + 付费样机）' + EU + '**；Simon 可否决',
    '分销 20%；P 池候选 ○（CEO 邮箱在表 + 进口经验 + 主区；体量小）；部分坐实（HRB 未取）；Simon 曾判不行。')
row('SC-2488', 'de', 'Fiber24 GmbH（fiber24.net；**unternehmen24 / creditreform / webvalid：HRB 104376 Amtsgericht Hamburg；Wandsbeker Königstraße 50, 22041 Hamburg；2008-03-04 登记；股本 €25,000；UID DE259003489；经营范围「电信与网络产品的贸易与销售」；2021-11-11 与 RIK Holding GmbH（Selmsdorf，AG Schwerin HRB 11665）签控制与利润转移协议；2021 年报可查；wirtschaftsaktiv**）；表内：光路 / Planet 的 / 工业 FS 很多牌子；shop@ 表内；8 推 0 回；Simon 曾判不行', 'DE',
    'DE · 1 次检索：unternehmen24（HRB 104376；2008；€25,000；DE259003489）+ creditreform（Großhandel IKT；aktiv；2022-05 变更）+ webvalid（RIK Holding 控制协议）；2026-10-29', 'https://www.unternehmen24.info/Firmeninformationen/Deutschland/Firma/3123567',
    'HRB 104376（Hamburg）', 'wirtschaftsaktiv（2021 年报已公示）', '2008-03-04', 'GmbH（RIK Holding GmbH 控制）', 'ICT / 网络产品批发 + 网店（汉堡）', 'Wandsbeker Königstraße 50, 22041 Hamburg', '小型（推定；股本 €25,000）',
    ['（shop@fiber24.net 表内 / info@fiber24.net 名录；Geschäftsführer 姓名未取 → handelsregister 待查）'],
    '**多品牌网店分销（Planet 在售）→ 分销 20%：一页纸一次（STC-228GP / STC-2224GP 对标 Planet 同口型 + STI 工业 + MOQ 1 + 付费样机）' + EU + '**；Simon 可否决',
    '分销 20%；P 池候选 ○（分销主体 + Planet 渠道 + 主区 + 坐实；冷）；坐实（HRB）；Simon 曾判不行；dayjob 线索光路。')
row('SC-364', 'de', 'EasyWind GmbH（easywind.org；**ee-sh.de / wind-turbine-models / bds-sh：Lecker Straße 7（Gebäude 2c），25917 Enge-Sande（GreenTEC Campus）；2008 年起小型风机（6 kW）制造商，全球 300+ 台；+49 4662 88431-0；联系人 Hans-Günter Feddersen**）；HRB 未取；表内：阿里巴巴 RTS 成单 4 台 1 光 4 电小壳非 PoE（风机通信配套）；produktion@ 表内；电话加不上', 'DE',
    'DE · 1 次检索：ee-sh.de 能源地图（地址 / 电话 / Feddersen）+ wind-turbine-models（制造商档案）+ bds-sh（2008；300+ 台）；HRB 未取；2026-10-29', 'https://ee-sh.de/de/energymap/data/EasyWind-GmbH.php',
    '未取（HRB 1 查未得）', '营业中（2024 展会参展）', '2008', 'GmbH', '小型风力发电机制造（终端自用网络设备）', 'Lecker Straße 7, Gebäude 2c, 25917 Enge-Sande', '小型（推定）',
    ['Hans-Günter Feddersen — 联系人（能源地图）', '（produktion@easywind.org 表内 = 成单对接邮箱）'],
    '**成单回访（终端自用 25%）：按原单回访一次（同款 MC 复购 + 风机机舱工业级 STI-154GP 升级建议；MOQ 1）' + EU + '**；体量小不加码',
    '终端自用 25%；P 池候选 △（成单 ✔ 主区 ✔ 对位 ✔；复购体量低 → 观察档，Simon 定）；坐实（法人 + 地址）。')
# ---------------- 波兰 ----------------
row('SC-276', 'pl', 'ASSMANN Distribution Sp. z o.o.（assmann.pl；**官网 Contact：Gilarska 10/1 lok.1, 03-589 Warszawa；+48 22 586 11 60；office@assmann.pl；NIP PL8951883569；REGON 020543570；ASSMANN Group（DIGITUS 品牌，德国 Lüdenscheid 总部）波兰分销公司；旧法人 ASSMANN Electronic Sp. z o.o. KRS 0000203233（Wrocław，已 wykreślona）**）；表内：「很大的一个公司，由国内较多合作商」', 'PL',
    'PL · 1 次检索：assmann.pl/en/company/contact（法人 / NIP / REGON / 地址）+ bizraport / krs-pobierz（旧法人 KRS 0000203233 已注销）；2026-10-29', 'https://www.assmann.pl/en/company/contact/',
    'NIP 8951883569 / REGON 020543570（KRS 号未取）', '营业中（官网）', '未取（旧法人 2004）', 'Sp. z o.o.（ASSMANN Group 子公司）', '网络 / 布线产品品牌分销（DIGITUS；波兰）', 'Gilarska 10/1 lok.1, 03-589 Warszawa', '中型（集团约 500；波兰公司小型）',
    ['（office@assmann.pl 表内 = 官网公开总邮箱；DIGITUS 产品经理在德国总部 → LinkedIn 挖）'],
    '**DIGITUS 自有品牌（贴牌中国）→ OEM 30%：波兰公司一页纸探路 + 同步找 Lüdenscheid 总部 Product Management（STC-028GP / STC-228GP / STI-154GP 对标 DIGITUS 口型 + 丝印彩盒 MOQ + 付费样机）' + EU + '**',
    'OEM 30%；P 池候选 ★（品牌商自有网络线 = 目标顺位 1；集团中型）；坐实（NIP / REGON）。')
row('SC-2834', 'pl', 'DIPOL Gołaszewski, Waśniowski Spółka Jawna（dipol.com.pl；**aleo / baza-firm：ul. Ciepłownicza 40, 31-574 Kraków；NIP 6780101049；REGON 350509592；KRS 0000094703；1990 年创立；欧洲 CCTV / WLAN / TV-SAT 分销 + 天线制造，1200+ 品项，自有品牌 Signal / Ultimax / Ultipower；多城分部（表内 sandomierz@ / warszawa@）**）；表内：VC / MC / SFP / 工业 FS；IFSEC 参展；Simon 曾判不行', 'PL',
    'PL · 1 次检索：aleo.com（KRS 0000094703；NIP 6780101049；Ciepłownicza 40）+ baza-firm（1990；品牌 / 品类）；2026-10-29', 'https://aleo.com/int/company/dipol-golaszewski,-gwizdala,-wasniowski-spolka-jawna',
    'KRS 0000094703 / NIP 6780101049', '营业中（KRS 2026 更新）', '1990', 'Spółka jawna（合伙）', '安防 / 网络 / 卫星电视分销 + 自有品牌（克拉科夫；全国分部）', 'ul. Ciepłownicza 40, 31-574 Kraków', '中型（全国分部）',
    ['Gołaszewski / Waśniowski — 合伙人（KRS）', '（sandomierz@ / warszawa@dipol.com.pl 表内分部邮箱；总部采购 KP 待 LinkedIn）'],
    '**自有品牌 Ultipower（PoE / 交换机）→ OEM 30%：找总部产品经理后一页纸一次（STC-028GP / STC-228GP / STC-2224GP 对标 Ultipower 口型 + 丝印彩盒 MOQ + 付费样机）' + EU + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（自有品牌 + 中型分销 + 波兰次主区）；坐实（KRS）；Simon 曾判不行；dayjob 线索 VC / MC。')
row('SC-2943', 'pl', 'Batna Sp. z o.o. — 品牌 Extralink（extralink24.com / .eu；**官网 Regulamin：KRS 0001003926（Sąd Rejonowy w Częstochowie XVII Wydział）；NIP 5732901461；REGON 380387214；ul. Boznańskiej Olgi 3E, 42-202 Częstochowa（通信地址 ul. 1 Maja 23）；rakow.com：Extralink 品牌所有者 Batna 经营 20+ 年、多品牌官方分销商，光纤 + 以太网产品起家，产品入驻 x-kom / Neonet，Ekstraklasa 联赛赞助**）；表内：很多国内的外壳 switch / PoE 配件 / PON，「有人在卖他们的」；退信；Simon 曾判不行', 'PL',
    'PL · 1 次检索：extralink24.com/regulamin（KRS / NIP / REGON / 地址）+ rakow.com（品牌所有者 Batna；20+ 年；x-kom / Neonet 渠道）；2026-10-29', 'https://www.extralink24.com/regulamin/',
    'KRS 0001003926 / NIP 5732901461', '营业中（2024–2026 赞助 / 网店）', '未取（经营 20+ 年；现法人 2022 重组）', 'Sp. z o.o.', '网络 / 光纤自有品牌 Extralink + 多品牌分销（琴斯托霍瓦）', 'ul. Boznańskiej Olgi 3E, 42-202 Częstochowa', '中型（推定；全国零售渠道）',
    ['（sales@extralink24.eu 表内曾退信；Batna 管理层 / 产品经理待 LinkedIn）'],
    '**自有品牌 Extralink（贴牌中国）→ OEM 30%：找产品经理 + 新地址后一页纸一次（STC-028GP / STC-228GP / STI-154GP 对标 Extralink 口型 + 丝印彩盒 MOQ + 付费样机）' + EU + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（自有品牌 + 全国渠道 + 波兰次主区）；坐实（KRS）；Simon 曾判不行。')
row('SC-3023', 'pl', 'NetTrans Jarosław Żydek（nettrans.pl；**官网 Kontakt：ul. Poznańska 115, 20-731 Lublin；NIP 712-239-07-96；REGON 366956479；个体经营（jednoosobowa działalność）；技术 / 售后 biuro@ +48 577 677 288；销售 handlowy@ +48 570 477 388**）；表内：工业 FS 国内 3C Link / ONV 的；退信；Simon 曾判不行', 'PL',
    'PL · 1 次检索：nettrans.pl/kontakt.html（法人 / NIP / REGON / 地址 / 电话）；2026-10-29', 'https://nettrans.pl/kontakt.html',
    'NIP 712-239-07-96 / REGON 366956479', '营业中（官网）', '未取（REGON 2017 前后）', '个体经营', '工业网络 / 光纤设备网店（卢布林）', 'ul. Poznańska 115, 20-731 Lublin', '微型（个体）',
    ['Jarosław Żydek — 业主（handlowy@nettrans.pl 表内 = 销售邮箱）'],
    '**个体进口商 → 分销 20%：点名 Jarosław 一页纸一次（STI-154GP / STI-280GE 对标 3C Link / ONV + MOQ 1 + 付费样机）' + EU + '**；个体 → 预付 100%；Simon 可否决',
    '分销 20%；P 池候选 △（进口中国品牌 ✔ 波兰 ✔ 坐实 ✔ 对位 ✔；个体微型 → 观察档 + 预付）；坐实（NIP）；Simon 曾判不行。')

print('b126_c rows written: 28')
