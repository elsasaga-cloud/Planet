#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 94 批 · US 6 户 + TR 4 户 + 补项 2（SB-150 直查 / SB-017 总览页）（T29-U89，2026-10-28）：web_search depth 1 各一次（一户一查，1 次未命中即停）；Companies House 总览页 fetch_page。可重复运行（put 按 code 合并）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 94

# ---------------- US 6 ----------------
put('SB-098', key='us', batch=B, name='Nexxt Solutions（nexxtsolutions.com；Miami FL）— Intcomex 集团自有品牌', iso='US', fetched=F,
    source='US · 1 次检索：LinkedIn 公司页（Computer Hardware Manufacturing；201–500 人；Miami FL；Founded 2006；3505 NW 107 Ave）+ ZoomInfo / Datanyze（同址；2006；51–200 / 69 人；$26.4M 第三方估）+ Intcomex 公司史（1988/89 Shalom 父子创立；Delaware 公司；拉美 / 加勒比 IT 分销；40,000+ 客户 / 45 国；2,600 人；曾 2007 申请上市）',
    url='https://www.linkedin.com/company/nexxt-solutions',
    number='FL / DE 登记号未取（Sunbiz ✗）', status='Active（LinkedIn / 官网在线）', incorporated='2006（品牌；母公司 Intcomex 1988）', company_type='Intcomex, Inc.（Delaware）旗下自有品牌 / 事业部（独立法人与否未取）',
    sic=['网络 / 连接 / 电源自有品牌（Nexxt：交换机、PoE、路由、配线、UPS），母公司 IT 分销（NAICS 423430）'],
    address='3505 NW 107th Ave, Miami (Doral), FL 33178', accounts='—（私有）', accounts_due='—', size_band='大型集团内品牌（Nexxt 51–500 人；Intcomex ≈2,600 人 / 数亿美元级）',
    officers=['Paula Aguilera / Luis Garcia — 研究档 KP（职务未取）', 'Michael Shalom — Intcomex CEO（集团层，不写）', 'Anthony (Thony) Shalom — Intcomex Chairman / 创始人'], psc='Intcomex, Inc.（Shalom 家族 + 机构股东）', charges='', prev_names=[],
    lines=['**Intcomex 的自有品牌 = 典型「贴牌商用 PoE」买家**（研究档「一部分贴牌的商业 PoE」）→ **OEM 30%**；但采购在迈阿密产品部、量大且走招标式比价 → B BIG，别指望一封信',
           '研究档 KP Paula Aguilera / Luis Garcia 继续写，开场点「Nexxt 现有 PoE 交换机系列」+ 一页纸 STC-028GP / STC-2224GP 贴标报价，一个问题：现用 ODM 交期？',
           '市场是拉美 / 加勒比（不在 Saga 主战场）但买家在美国 → 发信窗口 Wed 08–10 ET；年度复核'],
    notes='FL 实体号未取（Sunbiz ✗）；第三方营收只作区间。')
put('SB-1114', key='us', batch=B, name='FikesMedia LLC（fikesmedia.com；Silsbee TX）', iso='US', fetched=F,
    source='US · 1 次检索：Tracxn（2007 年 Christopher Fikes 创立；Silsbee；未融资）+ fikesmedia.com/about（2007；「与老朋友 Mikrotik 的新合作」）+ /contact（105 George St, Silsbee TX 77656；旧址 109 Pinecrest Dr）+ Crunchbase 人物页（Christopher Fikes：Evadale ISD 信息技术主任 2018– + FikesMedia Owner 2007–）+ bizstanding（Fikesmedia.Com, Member Christopher Fikes / Principal, inactive）',
    url='https://www.fikesmedia.com/about',
    number='TX 登记号未取（TX SoS 付费；bizstanding 镜像显示旧登记 inactive）', status='官网在线（2026）；登记状态存疑（镜像 inactive）', incorporated='2007', company_type='LLC（德州）',
    sic=['MikroTik 转售 + IT 服务（副业）'],
    address='105 George St, Silsbee, TX 77656', accounts='—', accounts_due='—', size_band='微型（1 人；老板另有全职 = 学区 IT 主任 + 兼职教授）',
    officers=['Christopher Fikes — Owner（研究档 KP；同时任 Evadale ISD Director of IT）'], psc='Christopher Fikes 100%（推定）', charges='', prev_names=[],
    lines=['**一人副业（老板全职在学区）** → 量极小；分销 20% 线只给一页纸，不投第 2 封',
           '唯一价值：他管一个学区的网络 → 若他回信，问的是「学区项目用 PoE 交换机」而不是经销',
           '德州登记可能已失效（镜像 inactive）→ 不作为可靠底数；不动 B'],
    notes='TX SoS 付费未查；不再追。')
put('SB-951', key='us', batch=B, name='Montavue LLC（montavue.com；Missoula MT）', iso='US', fetched=F,
    source='US · 1 次检索：OpenCorporates MT C1022717（Domestic LLC；Active Good Standing；Agent Cody Gordon，5707 W Harrier Dr Missoula）+ BBB（Business Started 2016-09-19；LLC；Cody Gordon, Member）+ Justia 商标 MONTAVUE（2017-05-17 申请）+ montavue.com/about（2017 年 Cody Gordon 创立，此前转售他牌）+ LinkedIn（11–50 人；Founded 2015）+ RocketReach（9 人；$5.1M 估）',
    url='https://opencorporates.com/companies/us_mt/C1022717',
    number='Montana SoS C1022717', status='Active Good Standing', incorporated='2016-09-19（BBB）/ 品牌 2017', company_type='Domestic Limited Liability Company（Montana）',
    sic=['自有品牌安防相机 / NVR 网店 + 经销商计划（Montavue Partners）'],
    address='5707 W Harrier Dr, Missoula, MT 59808', accounts='—', accounts_due='—', size_band='小型（9–16 人；$5M 级第三方估）',
    officers=['Cody Gordon — President / Founder / Member（老板）'], psc='Cody Gordon（推定）', charges='', prev_names=[],
    lines=['**自有品牌 + 只有一款自标工业 PoE（研究档）= 正好缺商用 PoE 全系** → **OEM 30% 首选户**：STC-028GP / STC-228GP / STC-2224GP 贴 Montavue 标，一页纸直接写老板 Cody Gordon',
           '蒙大拿 16 人老板公司 → 回信即拍板；Partners 经销计划说明他们有自己的渠道 = 复购面',
           '发信窗口 Wed 08–10 MT；年度复核 OpenCorporates 状态'],
    notes='研究档曾记 Lacey WA（错，实为 Missoula MT）→ 以登记为准。')
put('SB-959', key='us', batch=B, name='Silarius LLC（silarius.com；Brooklyn NY / Clifton NJ）', iso='US', fetched=F,
    source='US · 1 次检索：BBB（Silarius LLC；155 Water St Brooklyn NY 11201；Founding 2019-03-25）+ buzzfile（Silarius LLC；2019；5 人；$0.86M 估）+ silarius.com（「NJ 团队自 2008 年起服务」；1033 US Highway 46 Ste 204, Clifton NJ 07013；230,000+ 产品；自有品牌 Silarius 相机 / NVR「NDAA Section 889 compliant」）+ LinkedIn（2–10 人；Founded 2008）+ Google Play 开发者（ben@silarius.com）',
    url='https://www.bbb.org/us/ny/brooklyn/profile/information-technology-services/silarius-llc-0121-87158748',
    number='NY LLC 登记号未取（NY DOS 为 JS 页）', status='Active（官网 / App 在线）', incorporated='2019-03-25（LLC；业务自称 2008）', company_type='LLC（New York）',
    sic=['IT / AV / 安防设备网店（23 万 SKU 代销）+ 自有品牌 Silarius 相机 / NVR + 云监控服务'],
    address='1033 US Highway 46, Suite 204, Clifton, NJ 07013（登记地 Brooklyn NY）', accounts='—', accounts_due='—', size_band='微型（2–10 人）',
    officers=['Ben（ben@silarius.com）— 开发者账户联系人（职务未取；疑为老板）'], psc='', charges='', prev_names=[],
    lines=['**自有品牌打「NDAA 合规」旗号** → 我方不能也不要配合这个话术（禁词）；研究档「工业 FS 自己的 logo」→ 只做 **商用 PoE 贴标一条线（OEM 30%）**，不提合规',
           '23 万 SKU 代销网店 = 比价平台，自有品牌才是入口；写 ben@silarius.com（公域出现）',
           '微型 → B 维持；不投第 2 封'],
    notes='NY 登记号未取；不再追。')
put('SB-408', key='us', batch=B, name='XBLUE Networks, LLC（xblue.com；Phoenix AZ）', iso='US', fetched=F,
    source='US · 1 次检索：Crunchbase（法定名 XBLUE Networks, LLC；Founder & President Larry Steinmetz；Phoenix AZ；产品经 Amazon / Staples / Office Depot 等零售）+ LinkedIn（Telecommunications；11–50 人；Founded 2005；20801 N. 19th Ave Phoenix）+ Datanyze（11 人；$2M 估）+ contactout（Larry Steinmetz President；Paul Lynch VP Product Development；Alan Parker VP Marketing）+ NENA 登记（Paul Falanga VP Product Development；Winter Park FL 通信地址）+ 旧址 Lenexa KS',
    url='https://www.crunchbase.com/organization/xblue-networks',
    number='AZ / KS 登记号未取（AZ CC 为 JS 页）', status='Active（官网 2026-10 更新）', incorporated='2005', company_type='LLC',
    sic=['小企业电话系统（云 / VoIP / 本地 PBX）自有品牌，经零售 / 电商销售'],
    address='20801 N. 19th Ave, Suite 2 & 3, Phoenix, AZ 85027', accounts='—', accounts_due='—', size_band='小型（11–14 人；$2M 级第三方估）',
    officers=['Larry Steinmetz — Founder & President（老板）', 'Paul Lynch — VP Product Development（产品 = 选型人）', 'Paul Falanga — VP Product Development（NENA 登记）', 'Alan Parker — VP Marketing'], psc='Larry Steinmetz（推定）', charges='', prev_names=[],
    lines=['**研究档「商业 PoE 似乎是 ONV 去掉 logo」= 已在贴标** → **OEM 30%：8 口 PoE（电话机配套）STC-028GP / STC-228GP**，写产品副总 Paul Lynch，开场点「XBLUE 现有 PoE 交换机配件」',
           '零售渠道（Amazon / Staples）= 包装 / 说明书 / FCC 标识要求高 → 报价时注明中性包装可贴标、FCC 有',
           '20 年老公司、老板 + 产品副总两个人拍板 → 两封信够；年度复核'],
    notes='AZ 登记号未取；不再追。')
put('SB-351', key='us', batch=B, name='ENET Solutions, Inc.（enetusa.com；Aliso Viejo CA）— 2023-12 起属 NSI Industries', iso='US', fetched=F,
    source='US · 1 次检索：LinkedIn（ENET Solutions, Inc.；2003；11–50 人；Irvine CA）+ contactout / RocketReach（75 Argonaut Suite B, Aliso Viejo CA 92656；27 人；$10.8M 估）+ svconline / ewweb / nsiindustries.com 2023-12-12（NSI Industries（Huntersville NC）收购 ENET Solutions；2003 年 Chris Brock 创立；30+ 人；10,000+ 兼容收发器 / AOC / DAC / 内存 / MC / NIC / 线缆）',
    url='https://www.ewweb.com/news/mergers-acquisitions/article/21279116/nsi-buys-enet-solutions-to-bolster-vdv-position',
    number='CA 登记号未取（CA SoS JS）', status='Active（NSI 旗下品牌）', incorporated='2003', company_type='Inc.（加州；2023-12 起为 NSI Industries 子公司 / 品牌）',
    sic=['OEM 兼容光收发器 / DAC / AOC / 内存 / MC / 线缆 自有品牌 ENET（美国本土编程测试）'],
    address='75 Argonaut, Suite B, Aliso Viejo, CA 92656', accounts='—', accounts_due='—', size_band='小型（27–30+ 人；$10M 级）；母公司 NSI 为 PE 控股的电气产品集团',
    officers=['Chris Brock — 创始人（收购后职务未取）', 'Jason Barrette — President（growjo 记）'], psc='NSI Industries, LLC（Huntersville NC）100%', charges='', prev_names=['ENET Components, Inc.（旧名 / 关联）'],
    lines=['**主品类 SFP / DAC / 内存（Saga 不供）**；研究档「MC 自己的 logo」→ 只剩 **MC 贴标一条线（OEM 30%）**，且 2023-12 被 NSI 收购后采购并入集团 → 概率低',
           '不投入：一页纸 MC 报价即可，不写第 2 封；若回信再谈',
           '同名注意：ENET 与 eNet Components 为同一家的前后名'],
    notes='CA 登记号未取；不再追。')

# ---------------- TR 4 ----------------
put('SB-273', key='tr', batch=B, name='Eretekne（eretekne.com）= Erete Bilgi Sistemleri Dış Tic. ve San. Ltd. Şti. 的 B2B 站 → 并线 SB-867', iso='TR', fetched=F,
    source='TR · 1 次检索：eretekne.com/sayfa/hakkimizda（Erete Bilgi Sistemleri Ltd. Şti. 2001-12 创立；创始合伙人 Pınar Kabil / Murat Soyak / Timur Yıldız；Edge-Core（Accton）土耳其分销、Etherwan 工业交换机分销、Fluke Networks 分销；XPS 工业交换机）+ /iletisim（Firma Adı Eretekne | Erete B2B Sitesi；Yetkili Kişi Pınar Kabil；19 Mayıs Mah. Güven Sk. No:4/2 Şişli İstanbul；Vergi No 3540201016 Mecidiyeköy V.D.；IBAN 户名 ERETE BILGI SISTEMLERİ DIŞ. TIC. ve SAN. LTD.ŞTİ）+ erete.com.tr 公告（B2B 平台 = eretekne.com）',
    url='https://www.eretekne.com/iletisim',
    number='VKN 3540201016（Mecidiyeköy V.D.）', status='Active（B2B 站 2025 公告在线）', incorporated='2001-12（Erete）', company_type='Ltd. Şti.（同 SB-867 Erete 一个法人）',
    sic=['网络布线 + 有源设备分销（Edge-Core / Etherwan / XPS / Fluke）B2B 平台'],
    address='19 Mayıs Mah. Güven Sk. No:4/2, Şişli, İstanbul', accounts='—', accounts_due='—', size_band='小型（同 SB-867）',
    officers=['Pınar Kabil — 创始合伙人 / B2B 站负责人（Yetkili Kişi）', 'Murat Soyak — 创始合伙人（研究档 SB-867 KP）', 'Timur Yıldız — 创始合伙人'], psc='三位创始合伙人（推定）', charges='', prev_names=[],
    lines=['**SB-273 = SB-867 Erete 的 B2B 网店，一个法人（VKN 3540201016）→ 并线 SB-867，只跟一线**',
           '他们是 **Edge-Core（Accton）与 Etherwan 的土耳其分销商** = 卖竞品；对 Saga 只有「补位 / 低价线」价值：XPS / Etherwan 之外的商用 PoE 走 SmartByte 分销 20%',
           '写 Murat Soyak（已有）抄 Pınar Kabil；一封信，不加厚'],
    notes='并线：SB-273 → SB-867（第 94 批）。')
put('SB-653', key='tr', batch=B, name='Coredata Telekom A.Ş.（coredata.com.tr；Kağıthane İstanbul）', iso='TR', fetched=F,
    source='TR · 1 次检索：coredata.com.tr 首页 / iletişim / hakkımızda（Coredata Telekom A.Ş；Hamidiye Mah. Alp Sk. C Blok Apt. No:4/C/2 Kağıthane / İstanbul；info@ / satis@coredata.com.tr；+90 212 999 01 03；愿景页空泛；「2026 Tüm Hakları Saklıdır」）；MERSİS / 商会号未出现',
    url='http://coredata.com.tr/iletisim',
    number='MERSİS / 商会号未取（1 次检索未出现）', status='Active（官网 2026 在线；此前 Plesk 默认页已换成正式站）', incorporated='未取', company_type='A.Ş.',
    sic=['电信服务 / 网络集成（自述「Telekom」）'],
    address='Hamidiye Mah. Alp Sk. C Blok Apt. No:4/C/2, Kağıthane, İstanbul', accounts='—', accounts_due='—', size_band='微型–小型（人数未取）',
    officers=[], psc='', charges='', prev_names=[],
    lines=['**站活了（原 Plesk 默认页）但内容空泛，无人名、无产品页** → 身份只到「伊斯坦布尔小电信 / 集成商」',
           '研究档无 KP → 写 satis@coredata.com.tr 一封（分销 20% 一页纸），不加厚',
           'A.Ş. 形式但无披露 → 不作 BIG 判断；年度复核即可'],
    notes='法人号未取；不再追。')
put('SB-575', key='tr', batch=B, name='Marbim（marbim.com.tr）— 1 次未命中', iso='TR', fetched=F,
    source='TR · 1 次检索「Marbim marbim.com.tr bilişim güvenlik PoE switch」：返回全是通用 PoE 文章 / 他户（Atlantis Grup、Netser、Turkbim、Rima、Poe Güvenlik Batman…），无 Marbim 任何页面',
    url='', number='未取', status='未命中', incorporated='—', company_type='—',
    sic=['（研究档）安防 / 网络零售，仅 WhatsApp 联系'], address='Türkiye（城市未取）', accounts='—', accounts_due='—', size_band='—',
    officers=['Ecevit — 研究档 KP（仅 WhatsApp）'], psc='', charges='', prev_names=[],
    lines=['**一次未命中 → 按规程停**；名片户（WhatsApp only）本就不走邮件群发，底数价值低',
           '不再查；研究档维持'],
    notes='第 94 批 1 次未命中；标「底数不可查（名片户）」。')
put('SB-323', key='tr', batch=B, name='D&N Elektrik Mühendislik（Doğan Tanrıkulu；gmail）— 1 次未命中', iso='TR', fetched=F,
    source='TR · 1 次检索「"D&N Elektrik" Mühendislik Doğan Tanrıkulu」：返回 Doğan Mühendislik（安卡拉 1991）、D&T Group、美国 D&N Electric（亚特兰大 / 圣迭戈）等同名他户，无命中',
    url='', number='未取', status='未命中', incorporated='—', company_type='—（疑个体 / 小 Ltd.）',
    sic=['（研究档）电气工程承包'], address='Türkiye（城市未取）', accounts='—', accounts_due='—', size_band='—',
    officers=['Doğan Tanrıkulu — 研究档 KP（gmail）'], psc='', charges='', prev_names=[],
    lines=['**一次未命中 → 停**；gmail 名片户、同名陷阱多（美国 D&N Electric）',
           '研究档维持；不再查'],
    notes='第 94 批 1 次未命中；标「底数不可查（名片户）」。')

# ---------------- 补项 ----------------
put('SB-150', key='us', batch=B, name='Nexxus（nexxus.cc）— 直查：站活、自有标 3 口千兆 PoE', iso='US', fetched=F,
    source='US · 第 94 批补项 1 次直查 nexxus.cc 首页（fetch_page 2026-10-28）：「Reliable Networking Solutions」；产品线 IP 电话 / UC、Wi-Fi、网络交换机、安防 / 防火墙、存储；首页主推自有「3-Port Gigabit PoE Switch（Smart PoE / Plug & Play）」；案例：全球 3D 打印龙头、全球最大玻璃制造商；客户 logo 含 EHNAC；2024-03 / 2025-03 更新；无 Impressum / 地址 / 人名',
    url='https://nexxus.cc/',
    number='未取（站无法人信息）', status='Active（2025-03 产品图更新）', incorporated='未取', company_type='未取',
    sic=['网络方案 / VAR（交换、Wi-Fi、UC、防火墙、存储）+ 自有标小口数 PoE'],
    address='未取（站无地址；研究档 US）', accounts='—', accounts_due='—', size_band='未取',
    officers=[], psc='', charges='', prev_names=[],
    lines=['**站活、有自有标 PoE 小交换机 → 研究档「工业 FS 贴标」兴趣成立**；OEM 30% 一页纸照发（STI-054GP / STI-154GP + 商用 STC-028GP）',
           '与 nexxusnetworks.com **不是**同一家（产品 / 文案 / 客户群都不同）→ 第 93 批线索作废',
           '法人 / 地址不可查（站无 Impressum）→ 永久标「底数不可查」，不再追'],
    notes='第 93 批 1 次未命中 + 第 94 批 1 次直查 → 永久「底数不可查」。')
put('SB-017', key='gb', batch=B, name='SECURITYTEC LIMITED（05585047；Purley, Surrey）— 总览页补项', iso='GB', fetched=F,
    source='GB · Companies House 总览页 fetch_page 2026-10-28：Registered office 132 Riddlesdown Road, Purley, Surrey, CR8 1DE；Active；Private limited；Incorporated 2005-10-06；Last accounts to 2025-10-31；Next accounts to 2026-10-31 due 2027-07-31；Confirmation statement last 2026-10-05（next due 2027-10-19）；SIC 46520；Previous name FIRST SECURITY TEC LIMITED（2005-10-06 → 2017-03-02）',
    url='https://find-and-update.company-information.service.gov.uk/company/05585047',
    number='05585047', status='Active（账目 2025-10 + 确认声明 2026-10 均按时）', incorporated='2005-10-06', company_type='Private limited Company',
    sic=['46520 Wholesale of electronic and telecommunications equipment and parts'],
    address='132 Riddlesdown Road, Purley, Surrey, CR8 1DE（住宅地址）', accounts='Last accounts to 2025-10-31（微型）', accounts_due='2027-07-31（to 2026-10-31）', size_band='微型（住宅地址、单董事）',
    officers=['Graham David Smith — Director（第 93 批）'], psc='Graham David Smith（第 93 批记）', charges='', prev_names=['FIRST SECURITY TEC LIMITED（→ 2017-03-02）'],
    lines=['**合规在册、按时申报 20 年** → 老实的一人批发商；OEM 30% 判断（第 93 批）不变',
           '住宅地址 = 无库房 → 小批量 / 代发为主，报价写 MOQ 1 + 4–7 工作日',
           '年度复核：2027-07 看账目是否按时'],
    notes='第 94 批补项：总览页已取，PSC 页不再单独取。')

print('b94_us_tr ok')
