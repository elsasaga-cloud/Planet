# -*- coding: utf-8 -*-
"""第 118 批（T29-U111，2026-10-28）第 2 段 13 户（AU 第 10–18 户 + PK 第 1–4 户）—— 官方登记核实写入 registry（PK 路径首测：SECP / NTN 1 查不出；官网 contact + LCCI 商会名录 + 原厂 partner 页 → 部分坐实 常态）。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 118
F = '2026-10-28'
AU = '— 澳洲常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳（RCM 不声称、由买方自办；DAP 买方清关）'
PK = '— 巴基斯坦常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（PTA 不声称；进口清关 / 关税全由买方）'

# ───────── AU 第 10–18 户 ─────────
put('SB-471', key='other', batch=B, name='Austec.net Pty Ltd / Austec Communications（austec.net；**1025A Pumicestone Road, Toorbul QLD 4510；1300 663 442；30+ 年；ABN 1 查未得 → 部分坐实**）— **偏远 / 恶劣环境语音数据通信方案商：自研自产防风雨紧急求助电话 + 分销（Dahua CCTV、Teltonika 工业路由、Cambium、D-Link、ONV 工业 PoE 在售；客户 公路 / 铁路 / 矿山 / 电站 / 警消急救，覆盖亚太）**；表内「ONV 的工业 FS 比较少，有兴趣」；无具名 KP（sales@）；11 次跟进无实质回复', iso='AU', fetched=F,
    source='AU · 1 次检索：austec.net/contact-us（Austec.net Pty Ltd；Austec Communications；1025A Pumicestone Road, Toorbul QLD 4510；1300 663 442；sales@austec.net）+ /about-us（Australia’s leading provider of weatherproof emergency telephones；design, manufacture and distribute；over 30 years；roadside and rail applications, mines, power stations, police …）+ /products（Emergency Help Phones / 3G 4G 5G / WiFi / CCTV / M2M / Solar）；ABN 未得；2026-10-28',
    url='https://www.austec.net/contact-us/',
    number='未取（ABN 1 查未得）', status='营业中（官网在）', incorporated='未取（自述 30+ 年）', company_type='Pty Ltd',
    sic=['紧急电话制造 + 通信设备分销（Toorbul QLD）'],
    address='1025A Pumicestone Road, Toorbul QLD 4510, Australia', accounts='未取', accounts_due='—', size_band='小型',
    officers=['（研究档无具名 KP：sales@austec.net；+61 1300 663 442）'], psc='未取', charges='', prev_names=[],
    lines=['**自产 + 分销、已在售国内工业 PoE、Simon「有兴趣」→ 分销 20% B，一页纸一次（切口：对位其在售工业 PoE 的 STI-154GP / STI-288DGGPM / STI-488DGGPM 宽温 + 3 年保 + MOQ 1 + 付费样机；给求助电话 / 摄像机供电的 802.3at 口；英文，sales@ 抬头 Attn: Sales Manager）' + AU + '**；11×0 在先 → 再无回声即不动',
           '守界：铁路 / 电站 / 警消项目不主动提（只供通用工业 PoE）；不点名 ONV；RCM 不声称'],
    notes='分销 20%；一页纸一次（无具名 KP）；部分坐实（官网：法定名 + 地址 + 电话；ABN 未取）。')
put('SB-504', key='other', batch=B, name='Eltech Australia Pty Ltd（eltech.com.au；**1995 年墨尔本创立；31 Jersey Road, Bayswater VIC 3153；1800 007 458；墨尔本 / 悉尼 / 布里斯班三仓；78 人 / 营收 $5.7M（RocketReach 口径）；ABN 1 查未得 → 部分坐实**）— **独立进口 + 电气配件批发分销商（工业电缆、箱体、开关设备 KIKBLOX 模块化配电、面板配件、线缆管理 / 端接、线管）**；表内「少量 switch，自己的 logo」；KP Todd Cuneo（Product Manager）/ Jolyn Soo（Engineering Manager）；21 次跟进无回复', iso='AU', fetched=F,
    source='AU · 1 次检索：rocketreach（Eltech Australia Pty Ltd；31 Jersey Rd, Bayswater VIC 3153；+61 1800 007 458；Founded 1995；78 employees；$5.7M）+ top4.com.au（established in 1995 in Melbourne … standalone importer and wholesale distributor of electrical accessories；Industrial Cables / Enclosures / Switchgear / Panel Accessories）+ lusha（Wholesale；1995；11-50）；ABN 未得；2026-10-28',
    url='https://rocketreach.co/eltech-australia-pty-ltd-profile_b5f09e47f622651c',
    number='未取（ABN 1 查未得）', status='营业中（官网在）', incorporated='1995', company_type='Pty Ltd',
    sic=['电气配件进口 + 批发分销（Bayswater VIC；三仓）'],
    address='31 Jersey Road, Bayswater VIC 3153, Australia', accounts='未取', accounts_due='—', size_band='中小（11–78，口径不一）',
    officers=['Todd Cuneo — Product Manager（研究档 KP；todd.cuneo@eltech.com.au）= 收件人', 'Jolyn Soo — Engineering Manager（研究档 KP；邮箱未取）= 抬头抄送'], psc='未取', charges='', prev_names=[],
    lines=['**自有 logo 已上过交换机、产品经理为 KP、30 年进口批发商 → 贴标 OEM 30% B，一页纸一次（最后一次：Eltech 标 / 中性包装 STC-028GP / STC-228GP / STC-2216GP 非管理 PoE + 导轨 STI-054GP / STI-154GP（配电柜场景）+ MOQ 1 起贴标试单 + 付费样机；英文，Todd 直呼）' + AU + '**；21×0 在先 → 再无回声即不动',
           '守界：RCM 不声称；配电 / 开关设备不碰'],
    notes='贴标 OEM 30%；一页纸一次（最后一次）；部分坐实（企业库 + 名录：法定名 + 地址 + 成立年；ABN 未取）。')
put('SB-956', key='other', batch=B, name='PSA Products Pty Ltd（psaproducts.com.au；**ABN 99 076 468 703；PSA House, 17 Millicent Street, Burwood VIC 3125；03 9888 9889；官网 2026-10 在线**）— **澳洲安防批发分销商（自有品牌 PSA Centrii / Lifesaver 烟感 / Panacom 对讲 / Homeguard + HiLook 代理；电气批发渠道 Rexel 等）**；表内「商业 PoE 主要是 HiLook 牌子的」「可以多跟进一下」；KP Marcus Ooi（General Manager；marcus@ 见 2022 调价函）/ Vince Bruzzese（BDM）；21 次跟进无回复', iso='AU', fetched=F,
    source='AU · 1 次检索：psaproducts.com.au 2026-10-01（17 Millicent Street, Burwood VIC 3125；PSA Centrii / Lifesaver / Panacom / Homeguard / Hilook）+ rexelha.com.au 2022-04 PDF（PSA Products Pty Ltd ABN 99 076 468 703；PSA House 17 Millicent Street, Burwood VIC 3125；03 9888 9889 or marcus@psaproducts.com.au）+ psacentrii.com.au/pages/warranty（PSA Products Pty Ltd (ABN: 99 076 468 703)）；2026-10-28',
    url='https://www.rexelha.com.au/wp-content/uploads/2022/04/PSA-Price-change-notification-1st-May-2022.pdf',
    number='ABN 99 076 468 703', status='营业中（ABN 在；官网 2026-10）', incorporated='未取（ABN 076 → 约 1996–1997 ACN 段）', company_type='Pty Ltd',
    sic=['安防产品批发分销 + 自有品牌（Burwood VIC）'],
    address='PSA House, 17 Millicent Street, Burwood VIC 3125, Australia', accounts='未取', accounts_due='—', size_band='中小',
    officers=['Marcus Ooi — General Manager（研究档 KP；marcus@psaproducts.com.au；2022 调价函署名）= 拍板人 / 收件人', 'Vince Bruzzese — Business Development Manager（研究档 KP；enquiry@）= 抄送'], psc='未取', charges='', prev_names=[],
    lines=['**多自有品牌安防分销商、GM 为 KP、Simon「可以多跟进」→ 贴标 OEM 30% B，一页纸一次（最后一次：PSA / Panacom 标 PoE：STC-028GP $28 / STC-228GP / STC-2216GP / STC-2224GP（摄像机供电 250 m 延长模式）+ 管理 STC-4424GCPM + MOQ 1 起贴标 + 付费样机；对位其 HiLook 商业 PoE 不点名；英文，Marcus 直呼、抄 Vince）' + AU + '**；21×0 在先 → 再无回声即不动',
           '守界：RCM 不声称；烟感 / 对讲 / 摄像机不碰'],
    notes='贴标 OEM 30%；一页纸一次（最后一次）；坐实（ABN + 法定名 + 地址 + 电话，三源一致）。')
put('SB-948', key='other', batch=B, name='Krysma – Beyond Connectivity = Uniqmac Technologies 的品牌 / 商号（krysma.com.au；**Unit 6, 26 Rushdale St, Knoxfield VIC 3180；03 8806 8356；法人 / ABN 1 查未得 → 部分坐实**）— 消费 + 工业连接产品（AOA 周边为主；工业 FS / MC 少）；表内「可以多跟进一下」；无 KP（sales@）；24 次跟进无回复', iso='AU', fetched=F,
    source='AU · 1 次检索：krysma.com.au（Unit 6, 26 Rushdale St, Knoxfield, VIC 3180；03 8806 8356；sales@krysma.com.au；consumer and industrial connectivity products）+ krysma.com.au/contact 2024-10（Contact Info Uniqmac Technologies；Fax 03 8555 0816）+ uniqmac.com.au/product/krysma-beyond-connectivity；ABN 未得；2026-10-28',
    url='https://krysma.com.au/contact/',
    number='未取（ABN 1 查未得；母体 Uniqmac Technologies）', status='营业中（官网 2024 更新）', incorporated='未取', company_type='商号（Uniqmac Technologies 旗下）',
    sic=['连接产品 / 周边 分销（Knoxfield VIC）'],
    address='Unit 6, 26 Rushdale St, Knoxfield VIC 3180, Australia', accounts='未取', accounts_due='—', size_band='微型',
    officers=['（研究档无 KP：sales@krysma.com.au）'], psc='Uniqmac Technologies', charges='', prev_names=[],
    lines=['**周边产品为主 + 无 KP + 24×0 → 不动（B 保留）**'],
    notes='不动（24×0 + 无 KP）；部分坐实（官网：商号 + 母体名 + 地址 + 电话；ABN 未取）。')
put('SB-949', key='other', batch=B, name='KSM Australia Pty Ltd / KSM Solutions 网店（ksm.com.au；**ABN 98 071 589 690；Suite 18, 12 Tryon Rd, Lindfield NSW 2070；+61 412 921 435 / 02 8003 3372；Kevin = Director（官网署名）；官网 2026 在线**）— 工业 MC / 工业 FS / 商业 FS / SFP 网店（产品外壳「有像国内的」「常总的工业 FS」= 已直接进口国内工业机）；KP Kevin（Director；kevin@）；22 次跟进无回复', iso='AU', fetched=F,
    source='AU · 1 次检索：ksm.com.au/terms-conditions（KSM Australia Pty Ltd ABN: 98 071 589 690；Suite 18, 12 Tryon Rd, Lindfield, NSW 2070；Tel 02 8003 3372）+ ksm.com.au 首页 2026（Welcome to KSM Solutions e-store；+61 (0)41 2921435；Kevin - Director）+ /form/contact-us；2026-10-28',
    url='https://www.ksm.com.au/terms-conditions/',
    number='ABN 98 071 589 690', status='营业中（官网 2026；ABN 在）', incorporated='未取（ABN 071 → 约 1995–1996 ACN 段）', company_type='Pty Ltd',
    sic=['工业网络产品网店（Lindfield NSW）'],
    address='Suite 18, 12 Tryon Rd, Lindfield NSW 2070, Australia', accounts='未取', accounts_due='—', size_band='微型（一人公司级）',
    officers=['Kevin — Director（研究档 KP；kevin@ksm.com.au；官网署名）= 拍板人 / 收件人'], psc='Kevin（推定）', charges='', prev_names=[],
    lines=['**已直接进口国内工业机的一人网店、Director 为 KP → 分销 20% B small，一页纸一次（最后一次：STI-288DGGPM $137 / STI-488DGGPM $147 / STI-154GP 宽温 + 3 年保 + MOQ 1 + 付费样机 + 现供应商同级比价；英文，Kevin 直呼）' + AU + '**；22×0 在先 → 再无回声即不动',
           '守界：MC / SFP 不碰（仅 STC-110XGE）；RCM 不声称'],
    notes='分销 20% small；一页纸一次（最后一次）；坐实（官网自列 ABN + 法定名 + 地址 + Director）。')
put('SB-624', key='other', batch=B, name='UBWH Australia = Freenet Warehouse Pty Ltd（ubwh.com.au / netonix.com.au；**ABN 79 153 180 888；Office 3 Barker Place, Bicton WA 6157；02 8412 8312；所有人 Robert Clark（域名 whois）**）— **Ubiquiti 专营进口网店（UniFi / airFiber / EdgeMAX；「lowest possible price」大量进口囤货）**；无 KP（cs@ / store@）；6 次跟进无回复', iso='AU', fetched=F,
    source='AU · 1 次检索：ubwh.com.au（UBWH Australia；02 8412 8312；store@ubwh.com.au；Office: 3 Barker Place Bicton WA 6157；Australian business focused on bringing Ubiquiti products to the Australian market；ABN: 79 153 180 888）+ scamadviser（Organisation Freenet Warehouse Pty Ltd；Owner Robert Clark；ubwh.com.au / netonix.com.au）；2026-10-28',
    url='https://ubwh.com.au/index.php?nfc=1&page=1',
    number='ABN 79 153 180 888', status='营业中（网店在）', incorporated='未取（ABN 153 → 约 2011 ACN 段）', company_type='Pty Ltd',
    sic=['Ubiquiti 专营进口网店（Bicton WA）'],
    address='3 Barker Place, Bicton WA 6157, Australia', accounts='未取', accounts_due='—', size_band='微型',
    officers=['Robert Clark — 所有人（域名 whois）', '（研究档无 KP：cs@ubwh.com.au）'], psc='Robert Clark（推定）', charges='', prev_names=[],
    lines=['**单一原厂（Ubiquiti）专营网店 + 无 KP + 6×0 → 不动（B 保留）**'],
    notes='不动（原厂专营 + 无 KP）；坐实（网店自列 ABN + 地址；法人名 whois）。')
put('SB-380', key='other', batch=B, name='Yellowbox Co Pty Ltd（yellowbox.app / yellowboxglobal.com；**ABN 14 634 603 697（ACN 634 段 ≈ 2019 注册）；NSW 政府 buy.nsw 供应商（SME、NSW-based）；Crunchbase 1–10 人、Pre-Seed、Kensington SA；创始人 Adrian Brossard（+61 426 292 533，公开手册 adrian@yellowbox.com.au）**）— 职场 / 公共智能储物柜系统（电子锁 + 触屏 kiosk + App；澳 / 欧 / 新 / 北美装机）；阿里巴巴 RFQ「千兆 PoE Injector」；表内未跟进', iso='AU', fetched=F,
    source='AU · 1 次检索：buy.nsw.gov.au/supplier/profile/43702（Yellowbox Co Pty Ltd；ABN 14 634 603 697；SME；NSW-based）+ crunchbase（Legal Name Yellowbox Co Pty Ltd；Kensington, South Australia；1-10；Pre-Seed；founder Adrian Brossard）+ ict.co 手册（Adrian Brossard +61 426 292 533 adrian@yellowbox.com.au；Australia / NZ / US）；2026-10-28',
    url='https://buy.nsw.gov.au/supplier/profile/43702',
    number='ABN 14 634 603 697', status='营业中（ABN 在；官网在）', incorporated='约 2019（ACN 634 段推定）', company_type='Pty Ltd（初创）',
    sic=['智能储物柜系统（软硬件；澳洲）'],
    address='Kensington SA / NSW（门牌未取）, Australia', accounts='未取', accounts_due='—', size_band='微型（1–10）',
    officers=['Adrian Brossard — Founder（研究档 KP；contact@yellowbox.app；公开手册 adrian@yellowbox.com.au + 手机）'], psc='Adrian Brossard（推定）', charges='', prev_names=[],
    lines=['**需求 = PoE 注入器（Saga 无）+ 初创 1–10 人 + kiosk 单点用电 → 不动（B 保留；若 kiosk 组网要小 PoE 交换机再按集成商 25% 报 STI-054GP）**'],
    notes='不动（需求不对位 + 微型初创）；坐实（政府供应商库 ABN + 法人名）。')
put('SB-604', key='other', batch=B, name='Burns Precision Ag（burnsprecisionag.com.au；**22 Main Street, Gooloogong NSW 2805；02 6344 8246；2017-06 成立；NSW 安防 Master Licence 000104216；法人 / ABN 1 查未得 → 部分坐实**）— 精准农业硬件经销（Arag / AgLeader 经销、CHCNAV GNSS 分销、MM 喷洒设备、自产 KestrelEye 农机摄像头；网站设「Network Switches」页）；阿里巴巴询盘「升压 5 口」；KP Preston Burns（负责人）；表内未跟进', iso='AU', fetched=F,
    source='AU · 1 次检索：burnsprecisionag.com.au（02 6344 8246；22 Main Street, Gooloogong NSW 2805；Master Licence 000104216；ISOBUS / SAGRO 10 / IBX100）+ agtechfinder（Dealer for Arag & AgLeader；Distributor for CHCNAV GNSS；Manufacturers of KestrelEye Products；Year Established June 2017；0401 441 050）+ 官网 Network Switches 页；ABN 未得；2026-10-28',
    url='https://www.agtechfinder.com/company/burns-precision-ag',
    number='未取（ABN 1 查未得；安防牌照 000104216）', status='营业中（官网 2024 更新）', incorporated='2017-06', company_type='未取（Pty Ltd 推定）',
    sic=['精准农业硬件经销 + 农机摄像头制造（Gooloogong NSW）'],
    address='22 Main Street, Gooloogong NSW 2805, Australia', accounts='未取', accounts_due='—', size_band='微型',
    officers=['Preston Burns — 负责人（研究档 KP；preston@burnsprecisionag.com.au）'], psc='Preston Burns（推定）', charges='', prev_names=[],
    lines=['**需求 = 升压 PoE（车载 12/24 V；Saga 无）+ 乡镇微型经销 → 不动（B 保留；标准 48 V PoE 需求来询再按分销 20% 报 STI-054GP / STC-028GP）**'],
    notes='不动（需求不对位 升压 + 微型）；部分坐实（官网 + 名录：地址 + 电话 + 成立年 + 牌照；ABN 未取）。')
put('SB-606', key='other', batch=B, name='HME Solutions（hmesolutions.com.au；**珀斯 WA；11–20 人；Todd Pearce = Owner / Founder / Managing Director（prospeo + 领英）；CTO Ajay Koppisetty；法人名 / ABN 1 查未得 → 部分坐实**）— **矿业重型移动设备车队管理系统制造商（FMS Live™ 露天 / 井下、Asset IQ、VDL 车载硬件 + 软件 + 网络基础设施一体，按月服务费）**；阿里巴巴询盘「升压 5 口」（车载）；Ubiquiti 在用；表内未跟进', iso='AU', fetched=F,
    source='AU · 1 次检索：prospeo.io/c/hme-solutions（Perth, Western Australia；11-20；Todd Pearce Owner/Founder Managing Director；Ajay Koppisetty CTO；Manufacturer of Fleet Management Solutions）+ hmesolutions.com.au（FMS Live™ open-pit and underground；fully integrated ecosystem of software, hardware, and networking infrastructure）+ 领英 todd-pearce-101a7419；ABN 未得；2026-10-28',
    url='https://www.hmesolutions.com.au/',
    number='未取（ABN 1 查未得）', status='营业中（官网 + 领英活跃）', incorporated='未取', company_type='Pty Ltd（推定）',
    sic=['矿业车队管理系统 软硬件制造（Perth WA）'],
    address='Perth WA（门牌未取）, Australia', accounts='未取', accounts_due='—', size_band='小型（11–20）',
    officers=['Todd Pearce — Owner / Founder / Managing Director（研究档 KP；info@hmesolutions.com.au）'], psc='Todd Pearce', charges='', prev_names=[],
    lines=['**需求 = 车载升压 PoE（Saga 无）+ 井下（防爆不做）→ 不动（B 保留；地面 / 井口侧工业 PoE 需求来询再按集成商 25% 报 STI 线）**'],
    notes='不动（需求不对位 升压 + 井下）；部分坐实（企业库 + 官网：城市 + 规模 + 创始人；法人 / ABN 未取）。')

# ───────── PK 第 1–4 户（PK 路径首测）─────────
put('SB-068', key='other', batch=B, name='ICT Integrators（ict-integrators.com；**349-H/3, Johar Town, Lahore；+92 42 3595 1406-7 / 3586 7776；拉合尔商会 LCCI 会员名录：Muhammad Waleed = Managing Partner、业务线 Telecom Equipment & Accessories（→ 合伙企业口径，非 Pvt Ltd）；SECP / NTN 1 查未得 → 部分坐实**）— **IT / 电信系统集成 + 增值分销（电信运营商 / 企业 / 工业 / 医疗 / 教育 / 银行；融合数据网 / 宽带 / 光网 / UC / 安防；官网设「Industrial Grade Networking」栏）**；KP Muhammad Waleed（CEO）/ Ihsan Ullah（Director Commercial）', iso='PK', fetched=F,
    source='PK · 1 次检索：ict-integrators.com/integrators（Over 11 years；IT and Telecom Value Added Reseller for Telcos, Enterprise and SMEs；Muhammad Waleed CEO；349 - H/3, Johar Town, Lahore；+92-42-35951406-7；Industrial Grade Networking）+ lcci.pk/listing/ict-integrators 2021-11（MR. MUHAMMAD WALEED – MANAGING PARTNER；TELECOM EQUPT & ACCESSORIES；349-H/3 Johar Town；+92-42-35867776）+ branches.pk；SECP / NTN 未得；2026-10-28',
    url='https://lcci.pk/listing/ict-integrators/',
    number='未取（SECP / NTN 1 查未得；LCCI 会员）', status='营业中（官网 + 商会名录）', incorporated='约 2007（自述 11+ 年 / 研究档 2007）', company_type='合伙企业（LCCI 口径 Managing Partner）',
    sic=['IT / 电信系统集成 + 增值分销（Johar Town, Lahore）'],
    address='349-H/3, Johar Town, Lahore, Pakistan', accounts='未取', accounts_due='—', size_band='小型（22 人 RocketReach；领英 51–200 存疑）',
    officers=['Muhammad Waleed — CEO / Managing Partner（研究档 KP；apac@ict-integrators.com 公司箱）= 拍板人 / 收件人（Attn）', 'Ihsan Ullah — Director Commercial（研究档 KP）= 抄送抬头'], psc='Muhammad Waleed（推定）', charges='', prev_names=[],
    lines=['**真实 SI / VAR、有工业网络栏目、CEO 具名 → 集成商 25% B，一页纸一次（切口：工业栏目对位 STI-288DGGPM $137 / STI-488DGGPM $147 + 企业接入 STC-4424GCPM $165 / STC-2224GP $86 一口价 + MOQ 1 + 付费样机；英文，Attn: Muhammad Waleed, CEO）' + PK + '**；回信 → 加厚',
           '守界：电信运营商 / 银行项目不主动提；PTA 型号核准不声称'],
    notes='集成商 25%；一页纸一次（预付 100%）；部分坐实（官网 + 商会名录：地址 + 电话 + 负责人；SECP 号未取）。')
put('SB-065', key='other', batch=B, name='Ayk (Pvt.) Ltd.（ayk.com.pk；**总部 2nd Floor, U-Block, Trust Plaza, opposite Standard Chartered Bank, Model Town, Gujranwala 52250；+92 55 3822444 / 3255800；分支 拉合尔 Gulberg-II / 伊斯兰堡 G-11 Markaz / 木尔坦 / 费萨拉巴德；OMICRON 官网列为巴基斯坦官方 Sales & Service Partner（联系人 Sajjad Qaiser）；SECP / NTN 1 查未得 → 部分坐实**）— **电力测试与工程公司（变压器 / 电缆 / 开关设备高压测试服务、电力测试设备独家分销 Omicron / Chauvin Arnoux / Opal-RT …、自制变电站蓄电池充电器 NTDC 认证；官网设 PLANET 工业以太网专区 = 原厂经销）**；无具名 KP（info@）', iso='PK', fetched=F,
    source='PK · 1 次检索：omicronenergy.com/en/contact/addresses/pakistan（AYK (Pvt) Ltd；Contact Sajjad Qaiser；Al-Sharif Market, Main Model Town Road, Gujranwala；+92 55 3255800）+ ayk.com.pk/contact-us（Head Office 2nd Floor, U-Block, Trust Plaza, Model Town, Gujranwala 52250；Lahore / Islamabad / Multan 办公室）+ ayk.com.pk/products/omicorn/mpd-600（+92-55-3822444；Faisalabad 分支）；SECP / NTN 未得；2026-10-28',
    url='https://ayk.com.pk/contact-us/',
    number='未取（SECP / NTN 1 查未得）', status='营业中（官网 + 原厂 partner 页）', incorporated='1996 创立 / 2006 注册（自述）', company_type='(Pvt.) Ltd.',
    sic=['电力测试服务 + 测试设备分销（Gujranwala；四地分支）'],
    address='2nd Floor, U-Block, Trust Plaza, Model Town, Gujranwala 52250, Pakistan', accounts='未取', accounts_due='—', size_band='中小（约 90 人，自述）',
    officers=['Sajjad Qaiser — Omicron 业务联系人（原厂 partner 页）', '（研究档无具名 KP：info@ayk.com.pk）'], psc='未取', charges='', prev_names=[],
    lines=['**电力行业（守界）+ PLANET 原厂经销 + 无具名 KP → 不动（B 保留）**'],
    notes='不动（守界 电力 + 原厂经销）；部分坐实（官网 + Omicron 官方 partner 页：法定名 + 总部 + 分支；SECP 号未取）。')
put('SB-069', key='other', batch=B, name='Mutex Systems Ltd（mutexsystemsltd.com；**英国总部 Ealing Cross, 85 Uxbridge Road, London W5 5BW + 巴基斯坦区域办公室 Suite 716, 7th Floor, Park Avenue, PECHS Block 6, Shahrah-e-Faisal, Karachi（+92 21 3433 1335）；工程中心 卡拉奇 / 拉合尔 / 伊斯兰堡；英国 Companies House 号 1 查未取 → 部分坐实**）— **软件 / AI / 网络安全 / 云 DevOps 服务 + 自有 POS ERP / CRM / 金融 POS 产品（含「hardware manufacturing」自述）**；曾买非管理 / 百兆交换机；无 KP（support@ / info@）；群发无互动', iso='PK', fetched=F,
    source='PK · 1 次检索：mutexsystemsltd.com/about（UK-headquartered technology company with engineering hubs in Pakistan；Ealing Cross, 85 Uxbridge Road, London W5 5BW；Karachi · Lahore · Islamabad；Pakistan Regional Office Suite # 716, 7th Floor, Park Avenue, PECHS Block 6, Sharah-e-Faisal, Karachi）+ /contact + /get-a-quote 2025-07（+92 213-4331335）；CH 号 / SECP 未得；2026-10-28',
    url='https://mutexsystemsltd.com/about',
    number='未取（英国 Ltd；CH 号 1 查未取）', status='营业中（官网 2025 更新）', incorporated='未取', company_type='Ltd（英国）+ 巴基斯坦办公室',
    sic=['IT 服务 / 软件 / 网络安全（伦敦 + 卡拉奇）'],
    address='Suite 716, 7th Floor, Park Avenue, PECHS Block 6, Shahrah-e-Faisal, Karachi, Pakistan（英国总部 London W5 5BW）', accounts='未取', accounts_due='—', size_band='小型',
    officers=['（研究档无 KP：info@ / support@mutexsystemsltd.com）'], psc='未取', charges='', prev_names=[],
    lines=['**IT 服务公司（非目标行业）+ 无 KP + 无互动 → 不动（B 保留；国别保持 PK 按采购地，英国总部备注）**'],
    notes='不动（非目标行业 + 无 KP）；部分坐实（官网：两国地址 + 电话；登记号未取）。')
put('SB-583', key='other', batch=B, name='Usman（巴基斯坦小型贸易 / 工程买家；hotmail + gmail；WA +92 331 471 3140 已加；**0 查（无公司名 / 域名）**）— 2023-08 起 6 次实质回复：2 光 8 管理 50/100 台、2 光 4 小壳、24 光 combo、工业 mini、4/8/16 口工业 PoE「L2 managed」，一律「best price in RMB」压价', iso='PK', fetched=F,
    source='0 查（个人邮箱 + 无公司名；研究档 / Clients 表互动记录）；2026-10-28',
    url='', number='0 查（个人）', status='互动中（6 次实质回复）', incorporated='—', company_type='个人 / 小贸易商',
    sic=['小型贸易 / 工程采购（巴基斯坦）'],
    address='未取', accounts='—', accounts_due='—', size_band='个人',
    officers=['Usman — 买家本人（研究档 KP；usman2c@hotmail.com / usman65@gmail.com；WA 已加）'], psc='—', charges='', prev_names=[],
    lines=['**互动最多但只压价 + 要人民币价 → 分销 20% B（贸易商）：不另发一页纸，来询即按 USD 一口价 预付 100% FOB 深圳 回；RMB 报价 / 私账口径待 Simon**' + PK],
    notes='分销 20%（来询即报；RMB 口径待 Simon）；0 查（个人）。')
print('b118 第 2 段 13 written')
