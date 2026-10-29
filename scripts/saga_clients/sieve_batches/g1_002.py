#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 02 批（2026-10-29）—— 「自有品牌」桶 117 户（用户表记「自己的 logo / 自己的牌子」；多数有调研 JSON）。

判定口径：docs/C池三闸筛选_方案_2026-10-29.md §3 + §5 补充。
  自有品牌户三类：① 厂商 / 巨头 / 同行（自研自产、上市、中资分支）→ keep_C；② 伊朗 / 俄 / 乌克兰等口径受限 → keep_C；
  ③ 真正的贴牌渠道商（买别人的刷自己 logo 卖）→ 体量大 / 主区 / 有 AI 高评 → candidate（闸 2 查底数，入池仍需 §5 四条）；
    其余打 oem_target 留 C。
  pass_final 只给硬证据（本批仅 SC-009 Landatel：2026-05 宣布停业清算）。
标签：dayjob_fit（光端机 / DWDM / 光模块）、oem_target（贴牌渠道商）。

用法：python3 sieve_batches/g1_002.py   （幂等）
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G1-02'
DATE = '2026-10-29'
DJ = ['dayjob_fit']
OEM = ['oem_target']
BOTH = ['oem_target', 'dayjob_fit']

V = {
    # ---- 厂商 / 巨头 / 同行 / 集团品牌（非渠道，不判死）----
    'SC-038': ('keep_C', '香港 ANSEC（Utepo 贴牌 AS- 型号，+86 内地手机）→ 港 / 内地背景同行贸易商；17 推 0 回', []),
    'SC-046': ('keep_C', '美国 Crystal Group：国防加固服务器 / 军用 PoE 交换机制造商（AS9100D）→ 军工守界 + 自研厂商', []),
    'SC-047': ('keep_C', '德国 Indu-Sol 美国公司（PROMESH 工业交换机为德国自产）→ 厂商海外销售机构，非 OEM 买家', []),
    'SC-048': ('keep_C', 'Yamaha Corporation（SWX/SWR 自研交换机线，media@）→ 巨头', []),
    'SC-055': ('keep_C', '台湾 SMANEX（自有工业交换机 SW31xx 系列，Hannover Messe 参展）→ 台湾同行厂商', []),
    'SC-080': ('keep_C', 'OMEGA Engineering（全球仪器集团，印度站 info@）→ 体量过大；官网 http_error', []),
    'SC-082': ('keep_C', '以色列 Techaya：军用加固以太网交换机设计制造商 → 军工守界 + 厂商；16 推 0 回', []),
    'SC-085': ('keep_C', 'Grandstream（自有 GWN 交换机线、ODM 体系成熟，仅 marketing@）→ 品牌厂商；19 推 0 回', []),
    'SC-088': ('keep_C', 'Lantronix（纳斯达克，Transition Networks 线）→ 上市厂商；19 推 0 回', DJ),
    'SC-093': ('keep_C', 'TKH Security（荷兰上市 TKH Group，多国办事处）→ 上市集团体量过大；25 推 0 回', []),
    'SC-094': ('keep_C', 'Vantron 成都万创美国站 → 中国厂商海外分支，采购在国内；18 推 0 回', []),
    'SC-098': ('keep_C', '美国 Altronix：自研自产 PoE / EoC 交换机与安防电源品牌 → 同行 / 自研厂商；未触达', []),
    'SC-106': ('keep_C', '西班牙 Phicus：运营商 GPON / DOCSIS 供给监控软件与工程（不经销硬件）→ 品类不符；4 推 0 回', []),
    'SC-142': ('keep_C', 'Araknis（Snap One / Resideo 集成商网络品牌，OvrC 云管理）→ 集团品牌既定 ODM；22 推 0 回', []),
    'SC-143': ('keep_C', '台湾盛达 Billion Electric（上市，PoE 注入器 / 路由器）→ 台湾上市厂商', []),
    'SC-145': ('keep_C', 'DrayTek 澳洲分销站（台湾厂商自研 VigorSwitch）→ 厂商区域办事处；22 推 0 回', []),
    'SC-156': ('keep_C', '台湾奇偶 GeoVision（上市，GV-POE 系列既定 ODM）→ 台湾厂商', []),
    'SC-168': ('keep_C', '台湾 Zulite（SDI / AHD 视频转换器自有 logo，部分工业 FS 为 Allied Telesis）→ 台湾同行；官网 http_error', DJ),
    'SC-186': ('keep_C', '俄罗斯 Nateks（本土研发制造、国产替代定位，35+ 年）→ 俄产同行厂商；18 推 0 回', DJ),
    'SC-188': ('keep_C', '俄罗斯 QTECH（国家替代计划、政府 / 运营商客户，官方经销 OCS）→ 俄产品牌厂商；18 推 0 回', []),
    'SC-191': ('keep_C', 'Foscam 欧洲总代（PoE 由原厂配套）→ 专营中国品牌无切入点', []),
    'SC-193': ('keep_C', '俄罗斯 IPTRONIC（政府项目导向、法规符合性卖点）→ 俄区守界 + 结算物流受限', []),
    'SC-207': ('keep_C', '台湾 Fiberbit（MC / SFP / PoE 自有品牌，价格较高）→ 台湾同行；18 推 0 回；官网 http_error', DJ),
    'SC-211': ('keep_C', 'Linksys（富士康旗下消费 / SMB 网络品牌，linksyscares@）→ 巨头消费级；14 推 0 回', []),
    'SC-219': ('keep_C', 'Molex（Koch 旗下连接器巨头，自有工业网络产品；KP Fred Bell）→ 巨头；18 推 0 回', []),
    'SC-242': ('keep_C', '巴西 Intelbras（上市安防巨头，自有 PoE 交换机线 SF-18xx / SI-0402；KP Vanessa Ramos）→ 巨头既定 ODM；未触达', []),
    'SC-1027': ('keep_C', '印度 Tejas Networks（Tata 集团上市电信设备厂）→ 巨头 / 厂商；未触达', []),
    'SC-2219': ('candidate', '意大利 Comelit Group（对讲 / 安防集团，UniPoE 工业 FS + 商业 PoE 自有 logo；之前跟过西班牙分公司）→ 欧洲主区 + 品牌商体量；Simon 曾判不行 → 闸 2 查底数，入池需 §5 四条', OEM),
    'SC-2399': ('keep_C', 'Nexans（法国线缆巨头，自有工业 FS / SFP / MC 少量；KP Jacques Adam）→ 巨头；Simon 判不行', []),
    'SC-2686': ('keep_C', '台湾 Micronet（自有工业 FS / SFP，CCTV 商业 PoE）→ 台湾厂商；19 推 0 回', []),
    'SC-2483': ('keep_C', '台湾 Soarnex（工业 FS 自有 logo，国内有办公室，官网打不开、发送失败）→ 台湾厂商', []),
    'SC-2490': ('keep_C', '台湾 G-Net（MC / 工业 FS / PoE / SFP / 光猫 自有 logo，很多人卖他们的；发送失败）→ 台湾厂商', []),
    'SC-2712': ('keep_C', '以色列 Fibrolan（2.5G / 10G 自有 logo、CWDM）→ 厂商；17 推 0 回；光传输本职可参考', DJ),
    'SC-2805': ('keep_C', 'Buffalo Technology 美国（千兆交换机自有 logo，非工业）→ 品牌厂商；退信 + 域 no_mx；Simon 判不行', []),
    'SC-2806': ('keep_C', '意大利 ESA Automation（HMI / 工业自动化厂商，电口工业 FS 自有品牌）→ 厂商；退信；Simon 判不行', []),
    'SC-3063': ('keep_C', 'Peplink（SD-WAN 品牌厂商，商业 PoE 自有 logo）→ 厂商；表记 Spam = 不宜骚扰，非客户拒绝', []),
    'SC-2227': ('keep_C', 'Loocam（美国亚马逊 CCTV 套装品牌）→ 品牌电商，PoE 随套装；11 推 0 回；Simon 判不行', []),
    # ---- 口径受限地区（伊朗 / 俄 / 乌克兰 / 中国大陆 / 叙利亚等）----
    'SC-260': ('keep_C', '乌克兰 Dynamix（Switch 自有 logo）→ 乌克兰守界（Simon：不永久 pass）；8 推 0 回', OEM),
    'SC-263': ('keep_C', '乌克兰 PoE-Link（普通 PoE / FS / MC / PoE 电源 自有牌子）→ 乌克兰守界；17 推 0 回', OEM),
    'SC-1940': ('keep_C', '乌克兰 Romsat / RCI（SFP / MC / 无源 自有 logo，大分销商）→ 乌克兰守界', BOTH),
    'SC-2713': ('keep_C', '乌克兰 DEPS / Foxgate（买别人的刷自己 logo：FS / MC / SFP / VC / WDM / 商业 PoE）→ 乌克兰守界', BOTH),
    'SC-524': ('keep_C', '俄罗斯 Smartec（洪瑞商业 PoE 自有型号；crimea.tech 链接）→ 俄区 + 克里米亚制裁敏感；退信', OEM),
    'SC-572': ('keep_C', '俄罗斯 HiQ（yandex，商业 PoE 自有 logo，展示少）→ 俄区；未触达', OEM),
    'SC-1874': ('keep_C', '俄罗斯 Modultech（模块 / 收发器 / 无源 WDM 自有 logo；Simon 跟过）→ 俄区；光模块本职可参考', DJ),
    'SC-1942': ('candidate', '俄罗斯 Satvision（CCTV 品牌，自有 logo，Mike Yakushev 回过 1 次，15 次跟进）→ 真回 + 自有品牌；俄区收款路径待 Simon → 闸 2 查底数', OEM),
    'SC-2428': ('keep_C', '俄罗斯 DGSys / TMC（Kyland 华飞 / ONV 工业 FS 自有 logo 型号）→ 俄区；16 推 0 回；Simon 判不行', OEM),
    'SC-2823': ('keep_C', '俄罗斯 ST Space Technology（商业 PoE / CCTV 自有 logo，WeChat LudaAppel）→ 俄区；退信但 WeChat 在；Simon 判不行', OEM),
    'SC-2964': ('keep_C', '俄罗斯 Mlaxlink（MC / 高速 SFP 自有牌子）→ 俄区；退信 + no_mx；光模块本职可参考', DJ),
    'SC-2966': ('keep_C', '俄罗斯 Tantos（商业 PoE / CCTV 自有 logo，videooko.ru 在卖）→ 俄区；退信；Simon 判不行', OEM),
    'SC-2696': ('keep_C', '伊朗 KDT（少量工业 FS 自有 logo，大量周边）→ 制裁口径；10 推 0 回', []),
    'SC-2907': ('keep_C', '伊朗 PFN（商业 PoE 自有 logo）→ 制裁口径；退信', []),
    'SC-3418': ('keep_C', '国内光通信贸易商 ZhenHui Optical（Tina，163 邮箱，连要电话被 Alan 拒）→ 中国大陆规则（国内单只走私账）；不判死', DJ),
    # ---- 贴牌渠道商 · 体量大 / 主区 / 高评 → 候选（闸 2 查底数）----
    'SC-427': ('candidate', '西班牙 TBK Vision（安防品牌商，Utepo 工业交换机 + 自有型号，早期 AI 45% A）→ 主区 + 自有品牌 OEM 对象；退信但域名正常；14 次跟进 → 闸 2 找新 KP', OEM),
    'SC-1045': ('candidate', '泰国 Alfabase（自有品牌 + 同时卖 ONV / Elink，早期 AI 45% A）→ 典型贴牌渠道商（OEM 30% 对象）；16 推 0 回 → 闸 2 查底数', OEM),
    'SC-1053': ('candidate', '西班牙 Casmar（国际化安防分销集团，无邮箱）→ 主区 + 分销体量；未触达 → 闸 2 查底数找 KP', OEM),
    'SC-292': ('candidate', '美国 Fiber Instrument Sales（FIS，大型光纤工具 / 无源分销商，在卖 Signamax 交换机，自有 logo 无源 / MC / CWDM）→ 北美主区 + 分销体量；19 推 0 回 → 闸 2', BOTH),
    'SC-343': ('candidate', '印度 Optilink（MC / SFP / FS / 周边自有品牌，KP Vinit Savla）→ 印度次优区 + 自有品牌 OEM 对象；未触达 → 闸 2 查底数', OEM),
    'SC-347': ('candidate', '印度 Prama India（CCTV 为主 + 商业 PoE 自有 logo）→ 印度次优区 + 品牌体量；未触达 → 闸 2 查底数', OEM),
    'SC-2372': ('candidate', '英国 Eurosat / Oprema（大型安防分销商，在卖 Dahua PoE）→ 英国主区 + 分销体量；19 推 0 回；Simon 判不行 → 闸 2 查底数，入池需 §5 四条', OEM),
    'SC-2437': ('candidate', '泰国 Nana-tech（工业网络分销商，大量 Utepo，早期 AI 50% A）→ 贴牌渠道商；8 推 0 回；Simon 判不行 → 闸 2 查底数', OEM),
    'SC-2452': ('candidate', '西班牙 A-Secur（安防分销商，ONV / Utepo 页面，早期 AI 50% A）→ 主区 + 贴牌渠道；15 推 0 回；Simon 判不行 → 闸 2 查底数', OEM),
    'SC-2510': ('candidate', '波兰 Eltrox / getfort（全国性安防分销 + 连锁门店，MikroTik Master；Planet 仓 PB-051 评 B）→ 波兰次主区 + 分销体量；Simon 判不行 → 闸 2 查底数（并线 PB-051）', OEM),
    'SC-2516': ('candidate', '波兰 AAT / Novus（波兰最大安防分销商之一，自有品牌 Novus 工业 FS / PoE 延长器 / SFP；KP Stiepan Sedrakian）→ 自有品牌体量 + 波兰；Simon 判不行 → 闸 2 查底数', OEM),
    'SC-2598': ('candidate', '美国 Digital Watchdog（大型安防品牌，商业 PoE 自有 logo）→ 北美主区 + 品牌体量；20 推 0 回；Simon 判不行 → 闸 2 查底数，入池需 §5 四条', OEM),
    # ---- 贴牌渠道商 · 其余 → oem_target 留 C ----
    'SC-009': ('pass_final', '西班牙 Landatel（Ubiquiti / MikroTik 老牌分销商）2026-05 宣布因业务不可持续关闭并清算库存（调研 JSON：公司已停业，Inactiva）→ 主体消失', []),
    'SC-010': ('keep_C', '英国 Xceltra（工业交换机自有品牌，主要是 Moxa）→ 英国主区贴牌渠道；退信但域名正常；5 推 0 回；Simon 判不行', OEM),
    'SC-266': ('keep_C', '新加坡 IDE Security（MC / 跳线）→ 品类弱；8 推 0 回', DJ),
    'SC-280': ('keep_C', '越南 Cablexa（MC / FS / VC 自有标）→ 贴牌渠道（东南亚）；8 推 0 回；cablexa.com.vn NXDOMAIN 但 .vn 正常', BOTH),
    'SC-329': ('keep_C', '印度 Fibros Technology（MC / 工业 FS / 周边 自有牌子）→ 小型贴牌渠道；未触达', BOTH),
    'SC-420': ('keep_C', 'Nexconec（国别未填，MC / AOC / DAC / SFP 自有牌子）→ 光模块类贴牌；16 推 0 回', BOTH),
    'SC-522': ('keep_C', '香港 Sec-on（卖丰润达工业 FS 贴自己 logo；852 号加不上）→ 港区贴牌渠道；退信', OEM),
    'SC-604': ('keep_C', 'Oringnet 表行实为 gmail 个人（mamjadzafar@），工业 FS → 主体不明；8 推 0 回', []),
    'SC-631': ('keep_C', '澳大利亚 MSS Data Solutions（MC 自有 logo、无源、方案商）→ 光传输类；22 推 0 回', DJ),
    'SC-1017': ('keep_C', '瑞士 Lightwin（MC 自有 logo 别人在卖、SFP、机架、无源）→ 欧洲光模块类贴牌商；未触达；Q-70 定后可转候选', BOTH),
    'SC-1030': ('keep_C', 'Zorko（.tv 域，洪瑞商业 PoE 贴膜自有 logo）→ 贴牌渠道（国别待核）；退信 1 次', OEM),
    'SC-1116': ('keep_C', '芬兰 Sun-Evo（光模块 / fiber optics / 网络安全，模块自有 logo）→ 光模块类；15 推 0 回', DJ),
    'SC-1145': ('keep_C', '加拿大 Ariatech（Bypass、无源、MC 自有 logo）→ 光传输类；未触达', DJ),
    'SC-1165': ('keep_C', '澳大利亚 Serveredge（MC 自有牌子别人在卖、SFP / FS）→ 贴牌渠道；退信（.com no_mx，.com.au 正常）；23 推 0 回', BOTH),
    'SC-1204': ('keep_C', '台湾 Liye Systems（ONV 工业 FS / SFP / 工业电源 自有 logo）→ 台湾贴牌商；退信', OEM),
    'SC-1236': ('keep_C', '多米尼加 Alternativas Tecnologicas（gmail，工业 MC）→ 区域外 + 免费邮箱', DJ),
    'SC-1560': ('keep_C', '越南 Hung Quan（MC / SFP / VC / HDMI 自有牌子）→ 域名 dead，仅 huudinh@ 邮箱；光传输类', DJ),
    'SC-1674': ('keep_C', '美国 SerialComm（光猫 / MC / 串口 自有牌子，标价高）→ 产品外为主；8 推 0 回', DJ),
    'SC-1856': ('keep_C', '台湾 Melbye（工业 FS / 机架 MC 自有 logo）→ 台湾贴牌商；退信 + no_mx', OEM),
    'SC-1905': ('keep_C', '越南 Optone（3 旺标语、刷自己 logo；域名 NXDOMAIN，仅 gmail）→ 东南亚贴牌商；陈旧', OEM),
    'SC-1928': ('keep_C', '印尼 Flextreme（MC / 机架 / SFP 自有 logo，有人在卖）→ 光传输类贴牌；退信但两域正常', BOTH),
    'SC-2088': ('keep_C', '英国 Antiference（商业 PoE 自有 logo，别人在卖）→ 英国主区贴牌渠道；18 推 0 回；Simon 判不行 → oem_target 等专项', OEM),
    'SC-2091': ('keep_C', '意大利 DSE Italia（商业 PoE 自有 logo）→ 主区贴牌渠道；16 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2092': ('keep_C', '美国 Eline Technology（CCTV 为主，商业 PoE 自有 logo 不同外壳）→ 北美贴牌渠道；20 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2094': ('keep_C', '意大利 GV Informatica（CCTV 为主，商业 PoE 自有 logo 有 ONV，网站有 WA 按钮）→ 主区贴牌渠道；14 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2102': ('keep_C', '意大利 Vultech Security（商业 PoE 自有 logo）→ 主区贴牌渠道；16 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2115': ('keep_C', '美国 CableRack / JunoBlue / DiabloCable（MC 自有 logo）→ 光传输类贴牌；19 推 0 回；Simon 判不行', DJ),
    'SC-2226': ('keep_C', '德国 Longshine（商业 PoE / MC 自有 logo，产品不多）→ 主区贴牌品牌；8 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2341': ('keep_C', '意大利 Sicurit Alarmitalia（商业 PoE + 工业 FS 自有 logo 有 ONV，ecogreenshop 在卖，WA 按钮）→ 主区贴牌渠道；退信但域名正常；14 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2356': ('keep_C', '韩国 N-Ring（工业 FS / SFP 自有 logo，很像 ONV）→ 韩国次优区贴牌商；9 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2379': ('keep_C', '美国 Seco-Larm（安防配件品牌，商业 PoE 自有 logo）→ 北美品牌商；20 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2661': ('keep_C', '印度 Spiktel（工业 FS / MC / VC 买来刷自己 logo）→ 印度贴牌渠道；未触达；Simon 判不行 → oem_target', BOTH),
    'SC-2673': ('keep_C', '韩国 Dasans（工商业 switch 自有 logo；无邮箱、域 no_mx）→ 韩国贴牌商；Simon 判不行', OEM),
    'SC-2677': ('keep_C', '澳大利亚 VIP Vision（Cornick 旗下 CCTV 品牌，工业 FS / 大口 FS / SFP 自有 logo；无邮箱）→ 品牌体量但无联系路径；Simon 判不行 → oem_target', OEM),
    'SC-2762': ('keep_C', '香港 Lightem（多功能 VC / SDI / SFP / MC / CWDM 自有 logo；2011 年买过 6 对 OM4301）→ 成单户 + 光传输类；退信、852 加不上；22 推 0 回', DJ),
    'SC-2788': ('keep_C', '波兰 Comparta24（工业 FS 自有牌子，有小壳）→ 波兰贴牌渠道；表记 Spam = 不宜骚扰；7 推 0 回 → oem_target', OEM),
    'SC-2804': ('keep_C', '英国 Agatel（MC / serial / 工业 FS 自有标，KP Ray）→ 英国贴牌商；退信但域名正常；Simon 判不行 → oem_target', BOTH),
    'SC-2829': ('keep_C', '危地马拉 Lisintec（商业 PoE 自有 logo，ONV / Witek）→ 区域外贴牌渠道；退信；Simon 判不行', OEM),
    'SC-2833': ('keep_C', '土耳其 Teknoloji Pazar（洪瑞商业 PoE，freelink 疑自有品牌）→ 土耳其主区贴牌渠道；退信但域名正常；2 推 0 回 → oem_target（闸 2 可补）', OEM),
    'SC-2847': ('keep_C', '泰国 Advice（全国 IT 连锁零售，MC 商品页）→ 零售体量大但非 OEM 采购口；退信；9 推 0 回；Simon 判不行', []),
    'SC-2850': ('keep_C', '新加坡 poe.com.sg / Alstron（自有品牌工业 FS、PoE 配件）→ 东南亚贴牌品牌；退信；15 推 0 回；Simon 判不行 → oem_target', OEM),
    'SC-2867': ('keep_C', '美国 NetConnex / Networx（工业 MC、亚马逊店）→ Simon 记「不用跟了」（我方决定）；退信；留 C 不再主动', DJ),
    'SC-2879': ('keep_C', '德国 Beratung-Service Thomas（AP 类自有品牌，个人站）→ 域名 NXDOMAIN + 退信，但有手机号 → 不满足 G0-2；留 C', []),
    'SC-2880': ('keep_C', '美国 Cabling-Supplies（MC / 布线 自有 logo）→ 光传输类；退信；Simon 判不行', DJ),
    'SC-2881': ('keep_C', '美国 DC Americas（MC 自有 logo）→ 光传输类；退信；Simon 判不行', DJ),
    'SC-2883': ('keep_C', '香港 Morrell Telecom（MC / SDI / HDMI / VC / 工业 FS 自有 logo；WA 已加）→ 港区贴牌商；退信但 WA 在', BOTH),
    'SC-2899': ('keep_C', '美国 Multicom（工业 FS / 视频 / CWDM / MC / 机架 / SFP，自有 + 他牌；KP Matt）→ 北美综合分销；退信但域名正常；Simon 判不行 → oem_target', BOTH),
    'SC-2937': ('keep_C', '巴西 Flexmedia（工业 FS）→ 区域外；退信；Simon 判不行', []),
    'SC-2942': ('keep_C', '巴西 D-Networks（工业 / 商业 FS 自有 logo，像国内买的）→ 区域外贴牌；域 null_mx（不收信）；Simon 判不行', OEM),
    'SC-2953': ('keep_C', '巴西 Vid8（MC / 机架 / VC / PoE 自有 logo，明显外采）→ 区域外贴牌；退信；Simon 判不行', BOTH),
    'SC-2965': ('keep_C', '摩洛哥 Rik-com（MC / 机架 FS / 无源 / 工业 FS / SFP 自有标）→ 区域外贴牌；退信；Simon 判不行', BOTH),
    'SC-2968': ('keep_C', '韩国 Fostec（无源为主，国内工业 FS 贴自己标、MC）→ 韩国贴牌商；退信；Simon 判不行 → oem_target', BOTH),
    'SC-3075': ('keep_C', '美国 Prolink（prolink.us.com，MC 自有 logo，其余无源）→ 光传输类；退信；Simon 判不行', DJ),
}


def main():
    assert len(V) == 117, len(V)
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    for code, (verdict, reason, tags) in V.items():
        assert code in ents and ents[code].get('grade') == 'C', code
        assert verdict in ('pass_final', 'keep_C', 'candidate'), (code, verdict)
        assert len(reason) >= 12, code
        cur = sv.get(code) or {}
        if cur.get('gate', 0) >= 1 and cur.get('batch') != BATCH:
            continue
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True, 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    from collections import Counter
    c = Counter(v[0] for v in V.values())
    tg = Counter(t for v in V.values() for t in v[2])
    L = [f'# C 池 · 闸 1 · 第 02 批（{DATE}）—— 「自有品牌」桶 117 户', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 + §5 补充；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 oem_target {tg["oem_target"]} / dayjob_fit {tg["dayjob_fit"]}。', '',
         '> 自有品牌户大多是厂商 / 巨头 / 同行（自研自产）或口径受限地区，按 Simon U117 一律留 C 不 pass；真正「买来贴自己 logo 卖」的渠道商里体量大、主区、AI 高评的 12 户进闸 2 查底数（入池仍需 §5 四条），其余打 `oem_target` 等 OEM 专项。', '']
    for verdict, title in (('pass_final', '永久 pass'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批02_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
