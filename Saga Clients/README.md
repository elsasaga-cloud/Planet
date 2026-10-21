# Saga Clients — Saga 历史客户全量档案（A / B / C）

> 生成：2026-10-21　|　来源：`Clients/`（Simon 上传到 main 的 137 个文件：6,246 行线索 + 20,819 条跟进记录）　|　归并后 **4649 个客户**：A 135 / B 1315 / C 3199
>
> 流水线：`scripts/saga_clients/extract.py`（逐表逐行抽取）→ `build.py`（归并重复 + 规则分级 + 人工定级/调研覆盖）→ `render.py`（本目录）。**MD 不手改**：改 `data/saga_clients/人工定级.csv` 或 `research/<编号>.json` 后重跑。

## 等级定义（用户口径 → 执行口径）

| 等级 | 用户定义 | 执行口径（build.py） |
|---|---|---|
| **A** | 值得长期跟进 / OK 的 | 分数 ≥ 60 **且**有互动证据（成交 / 实质回复 / 询盘 / 展会面谈 / S 重点名单）；台系品牌商、巨头、守界区域、品类不符封顶 B 或 C |
| **B** | 一般的，慢慢跟进 | 分数 25–59；或有实质回复但分数低（托底 B）；或 A 候选但无互动证据（封顶 B） |
| **C** | 垃圾 / 基本或压根不值得跟进 | 分数 < 25；或硬规则：用户已归「不行及不太相关」、无联系方式、中国大陆、乌克兰（守界）、巨头/品牌厂商/运营商、备注「不再跟进/Spam」 |

分数 = 用户信号（成单 +50、实质回复 +22/+30、S 名单 +25、已回复名单 +18、WhatsApp +15、询盘 +12、ISAF 面谈 +12、1类 +15、AI/Claude A +15…）− 负面（不行 −60、不再跟进 −40、发不过去 −25、巨头 −45、聋名单 −10/−16/−22…）+ 契合（自有品牌 +12、交换机主线 +8、品类不符 −15）+ 通道（企业邮箱 +10、有网站 +5、无联系方式 −40）+ 区域（北美/欧洲/土耳其 +8 … 南亚/非洲 −6、中国大陆 −40、乌克兰 −20）+ 时效。每个档案的「为什么是 X 级」逐项列出。

## 分布

| 区域 | A | B | C | 合计 |
|---|---|---|---|---|
| 北美 | 19 | 208 | 257 | 484 |
| 欧洲 | 36 | 461 | 503 | 1000 |
| 土耳其 | 9 | 139 | 63 | 211 |
| 中东 | 12 | 78 | 235 | 325 |
| 亚太 | 25 | 226 | 704 | 955 |
| 俄语区 | 11 | 71 | 420 | 502 |
| 南亚 | 15 | 55 | 385 | 455 |
| 拉美 | 5 | 21 | 225 | 251 |
| 非洲 | 3 | 51 | 283 | 337 |
| 乌克兰 | 0 | 1 | 55 | 56 |
| 中国大陆 | 0 | 1 | 15 | 16 |
| 未知 | 0 | 3 | 54 | 57 |
| **合计** | 135 | 1315 | 3199 | 4649 |

状态分布：名单内 2012；已推送 1240；WhatsApp 528；用户判定不行 448；有回复 230；成交过 92；发不过去 84；回复暂无需求 15

C 级细分：群发冷名单无回应 1144；用户判定不行/不相关 548；综合分低 395；品类不符（VC/DWDM/CCTV 等） 343；无联系方式 148；低价值区域冷线索 143；发不过去 117；陈旧线索无互动 116；无邮箱（仅电话） 78；守界：乌克兰 54；体量过大/品牌厂商/运营商 47；用户备注不再跟进/Spam 44；中国大陆（非出口客户） 15；体量过大 5； 2

## 配套文件

- `data/saga_clients/客户主表.csv` — 一行一个客户（编号 / 等级 / 分数 / 联系方式 / 来源定位 / 评级依据）
- `data/saga_clients/重复客户归并记录.md` — 多来源客户与归并键、正负名单冲突
- `data/saga_clients/rows_raw.jsonl` / `followups.jsonl` / `extract_report.json` — 原始逐行抽取与逐文件行数（不漏复核）
- `data/saga_clients/research/` — 调研 JSON（引文 + URL + 日期；含 grade_override）
- `data/saga_clients/人工定级.csv` — 人工覆盖（列：键或编号, 等级, 理由）
- `Clients/` — 原件（只读，不改名不改内容）

## 索引

### A 级（135）— `Saga Clients/A/`

| 编号 | 公司 | 国家 | 类型 | 状态 | 分数 | 调研 | 档案 |
|---|---|---|---|---|---|---|---|
| SA-001 | asteldigicom.com | 阿联酋 | 分销商/网店（线缆·网络·太阳能） | 成交过·维护 | 164 | 已 | [SA-001-asteldigicom.com-阿联酋.md](A/SA-001-asteldigicom.com-阿联酋.md) |
| SA-002 | simrex.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机 | 有回复·跟进中 | 88 | 已 | [SA-002-simrex.com-美国.md](A/SA-002-simrex.com-美国.md) |
| SA-003 | Eyescan security Systems | 塞浦路斯 | 安防集成/经销（兼分销） | 成交过·维护 | 133 | 已 | [SA-003-Eyescan security Systems-塞浦路斯.md](A/SA-003-Eyescan%20security%20Systems-塞浦路斯.md) |
| SA-005 | Boecek Sec | 德国 | 安防集成/经销（据用户备注推断） | 成交过·维护 | 131 | 已 | [SA-005-Boecek Sec-德国.md](A/SA-005-Boecek%20Sec-德国.md) |
| SA-006 | resonantnetworks.com | 新加坡 | 系统集成/工程商（数据中心·光网络） | 成交过·维护 | 130 | 已 | [SA-006-resonantnetworks.com-新加坡.md](A/SA-006-resonantnetworks.com-新加坡.md) |
| SA-008 | rio-krsk.ru | 俄罗斯 | 分销商/经销商（工业自动化） | 成交过·维护 | 120 | 已 | [SA-008-rio-krsk.ru-俄罗斯.md](A/SA-008-rio-krsk.ru-俄罗斯.md) |
| SA-010 | Taurus Vision | 南非 | 安防集成商（CCTV/视频管理） | 有回复·跟进中 | 67 | 已 | [SA-010-Taurus Vision-南非.md](A/SA-010-Taurus%20Vision-南非.md) |
| SA-011 | vilinknet.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——光传输+工业以太网自有品牌 | 成交过·维护 | 117 | 已 | [SA-011-vilinknet.com-美国.md](A/SA-011-vilinknet.com-美国.md) |
| SA-013 | fiberone.de | 德国 | 运营商/ISP（终端 + 自有 logo 贴牌需求） | 成交过·维护 | 112 | 已 | [SA-013-fiberone.de-德国.md](A/SA-013-fiberone.de-德国.md) |
| SA-014 | coptek.com.tr | 土耳其 | 分销商（网络设备，DCN 土耳其分销） | 成交过·维护 | 110 | 已 | [SA-014-coptek.com.tr-土耳其.md](A/SA-014-coptek.com.tr-土耳其.md) |
| SA-016 | unitedcontrolengg.com | 印度 | 分销商 + 系统集成（工业自动化） | 成交过·维护 | 107 | 已 | [SA-016-unitedcontrolengg.com-印度.md](A/SA-016-unitedcontrolengg.com-印度.md) |
| SA-017 | NEXTU EZ-NET | 韩国 | 品牌商/分销商（自有品牌 NEXTU，OEM 采购） | 有回复·跟进中 | 103 | 已 | [SA-017-NEXTU EZ-NET-韩国.md](A/SA-017-NEXTU%20EZ-NET-韩国.md) |
| SA-019 | cxr.com | 法国 | 品牌商/贴牌需求（OEM/ODM）——工业网络设备自有品牌 | 有回复·跟进中 | 100 | 已 | [SA-019-cxr.com-法国.md](A/SA-019-cxr.com-法国.md) |
| SA-020 | widen.co.th | 泰国 | 分销商/品牌商（光纤产品自有 logo，OEM 采购） | 成交过·维护 | 97 | 已 | [SA-020-widen.co.th-泰国.md](A/SA-020-widen.co.th-泰国.md) |
| SA-021 | alfa.com.tw | 台湾 | 品牌商（台系无线网络品牌，PoE 交换机外采贴牌） | 有回复·跟进中 | 95 | 已 | [SA-021-alfa.com.tw-台湾.md](A/SA-021-alfa.com.tw-台湾.md) |
| SA-023 | impulsecctv.com | 新加坡 | 品牌商/贴牌需求（OEM/ODM）——安防品牌自有 PoE 交换机线 | 有回复·跟进中 | 94 | 已 | [SA-023-impulsecctv.com-新加坡.md](A/SA-023-impulsecctv.com-新加坡.md) |
| SA-024 | megnet.co.uk | 英国 | 分销商 + 自有品牌（Chimera，OEM 采购） | 有回复·跟进中 | 94 | 已 | [SA-024-megnet.co.uk-英国.md](A/SA-024-megnet.co.uk-英国.md) |
| SA-027 | parallaxdigital.co.uk | 英国 | 微型 OEM/ODM 品牌商（自有品牌网络设备） | 有回复·跟进中 | 89 | 已 | [SA-027-parallaxdigital.co.uk-英国.md](A/SA-027-parallaxdigital.co.uk-英国.md) |
| SA-028 | Sewell | 美国 | 品牌商/电商（消费 AV 连接；PoE 电源复购客户） | 成交过·维护 | 88 | 已 | [SA-028-Sewell-美国.md](A/SA-028-Sewell-美国.md) |
| SA-029 | allnet.de | 德国 | 分销商 + 自有品牌（ALLNET，OEM 采购） | 有回复·跟进中 | 88 | 已 | [SA-029-allnet.de-德国.md](A/SA-029-allnet.de-德国.md) |
| SA-031 | bitstream.pl | 波兰 | 品牌商/制造商（工业网络自有品牌；MC/SFP/部分交换机可能外采贴牌） | 有回复·跟进中 | 88 | 已 | [SA-031-bitstream.pl-波兰.md](A/SA-031-bitstream.pl-波兰.md) |
| SA-033 | optiviewusa.com | 美国 | 分销商/品牌商（CCTV 批发，自有品牌 OEM 采购） | 有回复·跟进中 | 88 | 已 | [SA-033-optiviewusa.com-美国.md](A/SA-033-optiviewusa.com-美国.md) |
| SA-036 | Addon Computer Products | 美国 | 品牌商/制造商（兼容光模块；MC 等外采贴牌） | 成交过·维护 | 86 | 已 | [SA-036-Addon Computer Products-美国.md](A/SA-036-Addon%20Computer%20Products-美国.md) |
| SA-037 | fcnet.pl | 波兰 | 分销商/进口商（自有 logo 采购） | 有回复·跟进中 | 85 | 已 | [SA-037-fcnet.pl-波兰.md](A/SA-037-fcnet.pl-波兰.md) |
| SA-038 | Cable Distribution Services | 澳大利亚 | 分销商（工业线缆；拓展工业交换机） | 有回复·跟进中 | 84 | 已 | [SA-038-Cable Distribution Services-澳大利亚.md](A/SA-038-Cable%20Distribution%20Services-澳大利亚.md) |
| SA-039 | getsecurityalarm.com | 美国 | 安防集成/安装商（小型，自装自用采购） | 有回复·跟进中 | 84 | 已 | [SA-039-getsecurityalarm.com-美国.md](A/SA-039-getsecurityalarm.com-美国.md) |
| SA-040 | hardenednetworks.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌 | 有回复·跟进中 | 84 | 已 | [SA-040-hardenednetworks.com-美国.md](A/SA-040-hardenednetworks.com-美国.md) |
| SA-041 | Al Salami Trading L.L.C | 阿联酋 | 安防集成商（项目型小批量） | 有回复·跟进中 | 83 | 已 | [SA-041-Al Salami Trading L.L.C-阿联酋.md](A/SA-041-Al%20Salami%20Trading%20L.L.C-阿联酋.md) |
| SA-043 | entasource.co.th | 泰国 | 进口分销商（自有 logo） | 有回复·跟进中 | 83 | 已 | [SA-043-entasource.co.th-泰国.md](A/SA-043-entasource.co.th-泰国.md) |
| SA-044 | gtwave.co.kr | 韩国 | 品牌商（OEM/ODM 需求） | 有回复·跟进中 | 83 | 已 | [SA-044-gtwave.co.kr-韩国.md](A/SA-044-gtwave.co.kr-韩国.md) |
| SA-045 | snexus.com.tr | 土耳其 | 品牌商/经销（自有品牌白牌采购） | 已推送 2 次·未回复 | 83 | 已 | [SA-045-snexus.com.tr-土耳其.md](A/SA-045-snexus.com.tr-土耳其.md) |
| SA-046 | westwardsales.com | 美国 | 增值分销商/电商平台（工业） | 有回复·跟进中 | 83 | 已 | [SA-046-westwardsales.com-美国.md](A/SA-046-westwardsales.com-美国.md) |
| SA-048 | Truong Son Solutions | 越南 | 分销商/电商（工业交换机垂直） | 有回复·跟进中 | 82 | 已 | [SA-048-Truong Son Solutions-越南.md](A/SA-048-Truong%20Son%20Solutions-越南.md) |
| SA-049 | sundartechno.com | 印度 | 方案商/自有品牌贴牌（成交客户） | 成交过·维护 | 82 | 已 | [SA-049-sundartechno.com-印度.md](A/SA-049-sundartechno.com-印度.md) |
| SA-050 | bluewarrior.com | 美国 | 品牌商（白牌贴牌，OEM 目标） | 有回复·跟进中 | 81 | 已 | [SA-050-bluewarrior.com-美国.md](A/SA-050-bluewarrior.com-美国.md) |
| SA-051 | rfog.pl | 波兰 | 分销商（自有型号贴牌） | 有回复·跟进中 | 81 | 已 | [SA-051-rfog.pl-波兰.md](A/SA-051-rfog.pl-波兰.md) |
| SA-052 | td-fe.com | 俄罗斯 | 品牌商/贸易公司（电源主业，工业交换机为配套） | 有回复·跟进中 | 81 | 已 | [SA-052-td-fe.com-俄罗斯.md](A/SA-052-td-fe.com-俄罗斯.md) |
| SA-054 | svn-video.ru | 俄罗斯 | 电商/安装商（自有型号贴牌） | 有回复·跟进中 | 80 | 已 | [SA-054-svn-video.ru-俄罗斯.md](A/SA-054-svn-video.ru-俄罗斯.md) |
| SA-055 | aeconnect.co.in | 印度 | 品牌商（部分进口贴牌 + 本地组装） | 有回复·跟进中 | 79 | 已 | [SA-055-aeconnect.co.in-印度.md](A/SA-055-aeconnect.co.in-印度.md) |
| SA-056 | dncsolutions.co.in | 印度 | 品牌商（光纤配套，MC 贴牌） | 有回复·跟进中 | 79 | 已 | [SA-056-dncsolutions.co.in-印度.md](A/SA-056-dncsolutions.co.in-印度.md) |
| SA-057 | mt-link.com | 巴基斯坦 | 品牌商（中国白牌贴牌，ODM 买家） | 有回复·跟进中 | 79 | 已 | [SA-057-mt-link.com-巴基斯坦.md](A/SA-057-mt-link.com-巴基斯坦.md) |
| SA-058 | success-network.co.th | 泰国 | 分销商/系统集成（多品牌） | 有回复·跟进中 | 79 | 已 | [SA-058-success-network.co.th-泰国.md](A/SA-058-success-network.co.th-泰国.md) |
| SA-063 | lightoptics.pl | 波兰 | 分销商/电商（自有品牌贴牌） | 有回复·跟进中 | 78 | 已 | [SA-063-lightoptics.pl-波兰.md](A/SA-063-lightoptics.pl-波兰.md) |
| SA-064 | 52networks.com | 美国 | 经销商（政府/商业小单，已成交） | 成交过·维护 | 77 | 已 | [SA-064-52networks.com-美国.md](A/SA-064-52networks.com-美国.md) |
| SA-066 | antronix.com | 美国 | 品牌制造商（拓展以太网交换机产品线，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-066-antronix.com-美国.md](A/SA-066-antronix.com-美国.md) |
| SA-067 | direktronik.se | 瑞典 | 分销商/进口商（自有品牌 + 多品牌） | 有回复·跟进中 | 76 | 已 | [SA-067-direktronik.se-瑞典.md](A/SA-067-direktronik.se-瑞典.md) |
| SA-068 | dymec.com | 美国 | 品牌商（白牌贴牌，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-068-dymec.com-美国.md](A/SA-068-dymec.com-美国.md) |
| SA-069 | energyplusystems.cl | 智利 | 工业/矿业集成供应商（工业交换机为配套品类） | 有回复·跟进中 | 76 | 已 | [SA-069-energyplusystems.cl-智利.md](A/SA-069-energyplusystems.cl-智利.md) |
| SA-070 | ipcampower.com | 美国 | 品牌商/电商（中国白牌贴牌，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-070-ipcampower.com-美国.md](A/SA-070-ipcampower.com-美国.md) |
| SA-072 | sge.com.tr | 土耳其 | 工程分销商/集成（能源自动化；工业交换机转售） | 有回复·跟进中 | 76 | 已 | [SA-072-sge.com.tr-土耳其.md](A/SA-072-sge.com.tr-土耳其.md) |
| SA-073 | ekhalas.com | 沙特阿拉伯 | 系统集成商+电商分销 | 有回复·跟进中 | 75 | 已 | [SA-073-ekhalas.com-沙特阿拉伯.md](A/SA-073-ekhalas.com-沙特阿拉伯.md) |
| SA-074 | iotsistem.com | 土耳其 | 工业/IoT 分销商（网店） | 已推送 2 次·未回复 | 75 | 已 | [SA-074-iotsistem.com-土耳其.md](A/SA-074-iotsistem.com-土耳其.md) |
| SA-076 | impakt.com.pl | 波兰 | 品牌商（自有品牌 OEM 采购）+ 分销商 | 有回复·跟进中 | 74 | 已 | [SA-076-impakt.com.pl-波兰.md](A/SA-076-impakt.com.pl-波兰.md) |
| SA-077 | Tecpro Solutions | 阿联酋 | 系统集成商（IT/ELV） | 有回复·跟进中 | 73 | 已 | [SA-077-Tecpro Solutions-阿联酋.md](A/SA-077-Tecpro%20Solutions-阿联酋.md) |
| SA-078 | bsn-system.com | 印度尼西亚 | 安防/IT 集成商 | 有回复·跟进中 | 73 | 已 | [SA-078-bsn-system.com-印度尼西亚.md](A/SA-078-bsn-system.com-印度尼西亚.md) |
| SA-079 | infrateq.id | 印度尼西亚 | 系统集成商+分销（VoIP/安防/工业网络） | 有回复·跟进中 | 73 | 已 | [SA-079-infrateq.id-印度尼西亚.md](A/SA-079-infrateq.id-印度尼西亚.md) |
| SA-081 | softnetworks.net | 美国 | 二手/翻新网络设备经销商 | 有回复·跟进中 | 73 | 已 | [SA-081-softnetworks.net-美国.md](A/SA-081-softnetworks.net-美国.md) |
| SA-082 | NOVA Group Engineering Project Electronic Co LTD | 土耳其 | 进口批发商/分销商（弱电安防） | 已推送 4 次·未回复 | 72 | 已 | [SA-082-NOVA Group Engineering Project Electroni-土耳其.md](A/SA-082-NOVA%20Group%20Engineering%20Project%20Electroni-土耳其.md) |
| SA-083 | B&S electronics | 希腊 | 安防批发商/进口商 | WhatsApp 已加·未回复 | 71 | 已 | [SA-083-B&S electronics-希腊.md](A/SA-083-B&S%20electronics-希腊.md) |
| SA-089 | Born SPb LLC | 俄罗斯 | 经销/集成（类型待核） | 有回复·跟进中 | 70 | 待 | [SA-089-Born SPb LLC-俄罗斯.md](A/SA-089-Born%20SPb%20LLC-俄罗斯.md) |
| SA-090 | act-connectivity.com | 荷兰 | 经销/集成（类型待核） | 有回复·跟进中 | 70 | 待 | [SA-090-act-connectivity.com-荷兰.md](A/SA-090-act-connectivity.com-荷兰.md) |
| SA-091 | alphanetcom.com | 美国 | 分销商/经销商 | 有回复·跟进中 | 70 | 待 | [SA-091-alphanetcom.com-美国.md](A/SA-091-alphanetcom.com-美国.md) |
| SA-092 | data-connect.com | 美国 | 经销/集成（类型待核） | 有回复·跟进中 | 70 | 待 | [SA-092-data-connect.com-美国.md](A/SA-092-data-connect.com-美国.md) |
| SA-093 | gofiberx.com | 美国 | 经销/集成（类型待核） | 有回复·跟进中 | 70 | 待 | [SA-093-gofiberx.com-美国.md](A/SA-093-gofiberx.com-美国.md) |
| SA-094 | ETRADINGKOREA Co., Ltd | 韩国 | 分销商/经销商 | 有回复·跟进中 | 69 | 待 | [SA-094-ETRADINGKOREA Co., Ltd-韩国.md](A/SA-094-ETRADINGKOREA%20Co.,%20Ltd-韩国.md) |
| SA-095 | Medias-Com'S | 瑞士 | 经销/集成（类型待核） | 成交过·维护 | 69 | 待 | [SA-095-Medias-Com'S-瑞士.md](A/SA-095-Medias-Com'S-瑞士.md) |
| SA-096 | OM Telecom S.R.L. | 秘鲁 | 电信/ISP/网络运营 | 有回复·跟进中 | 69 | 待 | [SA-096-OM Telecom S.R.L-秘鲁.md](A/SA-096-OM%20Telecom%20S.R.L-秘鲁.md) |
| SA-097 | PIOLINK | 韩国 | 经销/集成（类型待核） | 有回复·跟进中 | 69 | 待 | [SA-097-PIOLINK-韩国.md](A/SA-097-PIOLINK-韩国.md) |
| SA-098 | RYMTECH EAS | 巴拉圭 | 经销/集成（类型待核） | 有回复·跟进中 | 69 | 待 | [SA-098-RYMTECH EAS-巴拉圭.md](A/SA-098-RYMTECH%20EAS-巴拉圭.md) |
| SA-099 | Marvel ITCS Bahrain | 巴林 | 经销/集成（类型待核） | 有回复·跟进中 | 68 | 待 | [SA-099-Marvel ITCS Bahrain-巴林.md](A/SA-099-Marvel%20ITCS%20Bahrain-巴林.md) |
| SA-100 | TJ Computer | 泰国 | 经销/集成（类型待核） | 有回复·跟进中 | 68 | 待 | [SA-100-TJ Computer-泰国.md](A/SA-100-TJ%20Computer-泰国.md) |
| SA-101 | Thimphu Techpark | 卡塔尔 | 经销/集成（类型待核） | 有回复·跟进中 | 68 | 待 | [SA-101-Thimphu Techpark-卡塔尔.md](A/SA-101-Thimphu%20Techpark-卡塔尔.md) |
| SA-102 | inthouse.eu | 捷克 | 分销商/经销商 | 已推送 6 次·未回复 | 68 | 待 | [SA-102-inthouse.eu-捷克.md](A/SA-102-inthouse.eu-捷克.md) |
| SA-103 | ipns-uae.com | 阿联酋 | 品牌商/贴牌需求（OEM/ODM） | 已推送 11 次·未回复 | 68 | 待 | [SA-103-ipns-uae.com-阿联酋.md](A/SA-103-ipns-uae.com-阿联酋.md) |
| SA-104 | pulsar.kz | 哈萨克斯坦 | 经销/集成（类型待核） | 成交过·维护 | 68 | 待 | [SA-104-pulsar.kz-哈萨克斯坦.md](A/SA-104-pulsar.kz-哈萨克斯坦.md) |
| SA-105 | tricomp.com.pl | 波兰 | 系统集成/工程商 | 有回复·跟进中 | 68 | 待 | [SA-105-tricomp.com.pl-波兰.md](A/SA-105-tricomp.com.pl-波兰.md) |
| SA-106 | zelax.ru | 俄罗斯 | 经销/集成（类型待核） | 成交过·维护 | 68 | 待 | [SA-106-zelax.ru-俄罗斯.md](A/SA-106-zelax.ru-俄罗斯.md) |
| SA-107 | 4Demand Co | 阿联酋 | 经销/集成（类型待核） | 有回复·跟进中 | 67 | 待 | [SA-107-4Demand Co-阿联酋.md](A/SA-107-4Demand%20Co-阿联酋.md) |
| SA-108 | Areca Embedded Systems Pvt Ltd | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 67 | 待 | [SA-108-Areca Embedded Systems Pvt Ltd-印度.md](A/SA-108-Areca%20Embedded%20Systems%20Pvt%20Ltd-印度.md) |
| SA-109 | Telcam Fire&securoty Ltd | 英国 | 品牌商/贴牌需求（OEM/ODM） | 已推送 17 次·未回复 | 67 | 待 | [SA-109-Telcam Fire&securoty Ltd-英国.md](A/SA-109-Telcam%20Fire&securoty%20Ltd-英国.md) |
| SA-110 | optat.ru | 俄罗斯 | 经销/集成（类型待核） | 有回复·跟进中 | 67 | 待 | [SA-110-optat.ru-俄罗斯.md](A/SA-110-optat.ru-俄罗斯.md) |
| SA-111 | regalsecurity.co.za | 南非 | 经销/集成（类型待核） | 有回复·跟进中 | 67 | 待 | [SA-111-regalsecurity.co.za-南非.md](A/SA-111-regalsecurity.co.za-南非.md) |
| SA-112 | smbit.co.il | 以色列 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 66 | 待 | [SA-112-smbit.co.il-以色列.md](A/SA-112-smbit.co.il-以色列.md) |
| SA-113 | Euro Technology | 阿联酋 | 经销/集成（类型待核） | 有回复·跟进中 | 65 | 待 | [SA-113-Euro Technology-阿联酋.md](A/SA-113-Euro%20Technology-阿联酋.md) |
| SA-114 | Win-Tech Alliance Ltd | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 65 | 待 | [SA-114-Win-Tech Alliance Ltd-印度.md](A/SA-114-Win-Tech%20Alliance%20Ltd-印度.md) |
| SA-115 | advancedigital.co.in | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 65 | 待 | [SA-115-advancedigital.co.in-印度.md](A/SA-115-advancedigital.co.in-印度.md) |
| SA-116 | ccs-msk.ru | 俄罗斯 | 经销/集成（类型待核） | 有回复·跟进中 | 65 | 待 | [SA-116-ccs-msk.ru-俄罗斯.md](A/SA-116-ccs-msk.ru-俄罗斯.md) |
| SA-117 | domoticalia.es | 西班牙 | 品牌商/贴牌需求（OEM/ODM） | 成交过·维护 | 65 | 待 | [SA-117-domoticalia.es-西班牙.md](A/SA-117-domoticalia.es-西班牙.md) |
| SA-118 | topica.mn | 蒙古国 | 经销/集成（类型待核） | 有回复·跟进中 | 65 | 待 | [SA-118-topica.mn-蒙古国.md](A/SA-118-topica.mn-蒙古国.md) |
| SA-119 | Almaks Security SystemsGospodara | 塞尔维亚 | 安防集成/经销 | 成交过·维护 | 64 | 待 | [SA-119-Almaks Security SystemsGospodara-塞尔维亚.md](A/SA-119-Almaks%20Security%20SystemsGospodara-塞尔维亚.md) |
| SA-120 | Latmedia Group, LLC | 乌兹别克斯坦 | 经销/集成（类型待核） | 名单内·未触达 | 63 | 待 | [SA-120-Latmedia Group, LLC-乌兹别克斯坦.md](A/SA-120-Latmedia%20Group,%20LLC-乌兹别克斯坦.md) |
| SA-121 | MULTILINK (PVT) LTD | 津巴布韦 | 经销/集成（类型待核） | 成交过·维护 | 63 | 待 | [SA-121-MULTILINK (PVT) LTD-津巴布韦.md](A/SA-121-MULTILINK%20(PVT)%20LTD-津巴布韦.md) |
| SA-122 | PT. ANUGERAH | 印度尼西亚 | 经销/集成（类型待核） | 成交过·维护 | 63 | 待 | [SA-122-PT. ANUGERAH-印度尼西亚.md](A/SA-122-PT.%20ANUGERAH-印度尼西亚.md) |
| SA-123 | Prestige Satellites Communications S.A.C. | 秘鲁 | 经销/集成（类型待核） | 成交过·维护 | 63 | 待 | [SA-123-Prestige Satellites Communications S.A.C-秘鲁.md](A/SA-123-Prestige%20Satellites%20Communications%20S.A.C-秘鲁.md) |
| SA-124 | Pt.ras otomasi indonesia | 印度尼西亚 | 系统集成/工程商 | 有回复·跟进中 | 63 | 待 | [SA-124-Pt.ras otomasi indonesia-印度尼西亚.md](A/SA-124-Pt.ras%20otomasi%20indonesia-印度尼西亚.md) |
| SA-125 | excellent data communications | 马来西亚 | 经销/集成（类型待核） | 有回复·跟进中 | 63 | 待 | [SA-125-excellent data communications-马来西亚.md](A/SA-125-excellent%20data%20communications-马来西亚.md) |
| SA-126 | onnettechnologies.com | 阿联酋 | 经销/集成（类型待核） | 有回复·跟进中 | 63 | 待 | [SA-126-onnettechnologies.com-阿联酋.md](A/SA-126-onnettechnologies.com-阿联酋.md) |
| SA-127 | testronix.ph | 菲律宾 | 经销/集成（类型待核） | 成交过·维护 | 63 | 待 | [SA-127-testronix.ph-菲律宾.md](A/SA-127-testronix.ph-菲律宾.md) |
| SA-128 | DIOS ULTRA HD VIDEO SECURITY SYSTEMS | 荷兰 | 经销/集成（类型待核） | 有回复·跟进中 | 62 | 待 | [SA-128-DIOS ULTRA HD VIDEO SECURITY SYSTEMS-荷兰.md](A/SA-128-DIOS%20ULTRA%20HD%20VIDEO%20SECURITY%20SYSTEMS-荷兰.md) |
| SA-129 | Net Work Business Solutions | 爱沙尼亚 | 系统集成/工程商 | 有回复·跟进中 | 62 | 待 | [SA-129-Net Work Business Solutions-爱沙尼亚.md](A/SA-129-Net%20Work%20Business%20Solutions-爱沙尼亚.md) |
| SA-130 | Rfcom | 希腊 | 经销/集成（类型待核） | 有回复·跟进中 | 62 | 待 | [SA-130-Rfcom-希腊.md](A/SA-130-Rfcom-希腊.md) |
| SA-132 | avanca.com.sg | 新加坡 | 经销/集成（类型待核） | 有回复·跟进中 | 62 | 待 | [SA-132-avanca.com.sg-新加坡.md](A/SA-132-avanca.com.sg-新加坡.md) |
| SA-133 | bargas.ru | 俄罗斯 | 分销商/经销商 | 有回复·跟进中 | 62 | 待 | [SA-133-bargas.ru-俄罗斯.md](A/SA-133-bargas.ru-俄罗斯.md) |
| SA-134 | bptehno.ru | 俄罗斯 | 经销/集成（类型待核） | 有回复·跟进中 | 62 | 待 | [SA-134-bptehno.ru-俄罗斯.md](A/SA-134-bptehno.ru-俄罗斯.md) |
| SA-135 | megatelindustries.com | 美国 | 品牌商/贴牌需求（OEM/ODM） | 已推送 22 次·未回复 | 62 | 待 | [SA-135-megatelindustries.com-美国.md](A/SA-135-megatelindustries.com-美国.md) |
| SA-136 | Aarya ITES Pvt. Ltd. | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 61 | 待 | [SA-136-Aarya ITES Pvt. Ltd-印度.md](A/SA-136-Aarya%20ITES%20Pvt.%20Ltd-印度.md) |
| SA-137 | Avesta | 英国 | 品牌商/贴牌需求（OEM/ODM） | 已推送 17 次·未回复 | 61 | 待 | [SA-137-Avesta-英国.md](A/SA-137-Avesta-英国.md) |
| SA-138 | Top Italia | 意大利 | 经销/集成（类型待核） | 已推送 14 次·未回复 | 61 | 待 | [SA-138-Top Italia-意大利.md](A/SA-138-Top%20Italia-意大利.md) |
| SA-139 | amitytechnologies.co.in | 印度 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-139-amitytechnologies.co.in-印度.md](A/SA-139-amitytechnologies.co.in-印度.md) |
| SA-140 | ayk.com.pk | 巴基斯坦 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-140-ayk.com.pk-巴基斯坦.md](A/SA-140-ayk.com.pk-巴基斯坦.md) |
| SA-141 | comtec.com.vn | 越南 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-141-comtec.com.vn-越南.md](A/SA-141-comtec.com.vn-越南.md) |
| SA-142 | crec.com.ph | 菲律宾 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-142-crec.com.ph-菲律宾.md](A/SA-142-crec.com.ph-菲律宾.md) |
| SA-143 | ict-integrators.com | 巴基斯坦 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-143-ict-integrators.com-巴基斯坦.md](A/SA-143-ict-integrators.com-巴基斯坦.md) |
| SA-144 | mutexsystemsltd.com | 巴基斯坦 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-144-mutexsystemsltd.com-巴基斯坦.md](A/SA-144-mutexsystemsltd.com-巴基斯坦.md) |
| SA-145 | neowine | 韩国 | 经销/集成（类型待核） | 有回复·跟进中 | 61 | 待 | [SA-145-neowine-韩国.md](A/SA-145-neowine-韩国.md) |
| SA-146 | nkstech.net | 菲律宾 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-146-nkstech.net-菲律宾.md](A/SA-146-nkstech.net-菲律宾.md) |
| SA-147 | surlink-tech.com | 玻利维亚 | 经销/集成（类型待核） | 有回复·跟进中 | 61 | 待 | [SA-147-surlink-tech.com-玻利维亚.md](A/SA-147-surlink-tech.com-玻利维亚.md) |
| SA-148 | technosys.co.in | 印度 | 经销/集成（类型待核） | 成交过·维护 | 61 | 待 | [SA-148-technosys.co.in-印度.md](A/SA-148-technosys.co.in-印度.md) |
| SA-149 | trans audio video group | 意大利 | 经销/集成（类型待核） | 已推送 14 次·未回复 | 61 | 待 | [SA-149-trans audio video group-意大利.md](A/SA-149-trans%20audio%20video%20group-意大利.md) |
| SA-150 | vicomsecurity.com | 印度 | 安防集成/经销 | 有回复·跟进中 | 61 | 待 | [SA-150-vicomsecurity.com-印度.md](A/SA-150-vicomsecurity.com-印度.md) |
| SA-151 | ANB rimex | 比利时 | 经销/集成（类型待核） | 已推送 6 次·未回复 | 60 | 待 | [SA-151-ANB rimex-比利时.md](A/SA-151-ANB%20rimex-比利时.md) |
| SA-152 | Bilge SECURITY SYSTEMS | 土耳其 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 60 | 待 | [SA-152-Bilge SECURITY SYSTEMS-土耳其.md](A/SA-152-Bilge%20SECURITY%20SYSTEMS-土耳其.md) |
| SA-153 | Elite Team Security Ltd | 保加利亚 | 系统集成/工程商 | 回复暂无需求 | 60 | 待 | [SA-153-Elite Team Security Ltd-保加利亚.md](A/SA-153-Elite%20Team%20Security%20Ltd-保加利亚.md) |
| SA-154 | Falke security | 德国 | 安防集成/经销 | 已推送 7 次·未回复 | 60 | 待 | [SA-154-Falke security-德国.md](A/SA-154-Falke%20security-德国.md) |
| SA-155 | Gmka | 希腊 | 经销/集成（类型待核） | 已推送 6 次·未回复 | 60 | 待 | [SA-155-Gmka-希腊.md](A/SA-155-Gmka-希腊.md) |
| SA-157 | Liveye | 德国 | 安防集成/经销 | WhatsApp 已加·未回复 | 60 | 待 | [SA-157-Liveye-德国.md](A/SA-157-Liveye-德国.md) |
| SA-158 | Sitis Sarl | 瑞士 | 经销/集成（类型待核） | 已推送 6 次·未回复 | 60 | 待 | [SA-158-Sitis Sarl-瑞士.md](A/SA-158-Sitis%20Sarl-瑞士.md) |
| SA-159 | Telemobil | 土耳其 | 系统集成/工程商 | WhatsApp 已加·未回复 | 60 | 待 | [SA-159-Telemobil-土耳其.md](A/SA-159-Telemobil-土耳其.md) |
| SA-160 | ar telecom | 葡萄牙 | 电信/ISP/网络运营 | 名单内·未触达 | 60 | 待 | [SA-160-ar telecom-葡萄牙.md](A/SA-160-ar%20telecom-葡萄牙.md) |
| SA-161 | bornelectronics.com | 英国 | 经销/集成（类型待核） | 有回复·跟进中 | 60 | 待 | [SA-161-bornelectronics.com-英国.md](A/SA-161-bornelectronics.com-英国.md) |
| SA-162 | cansisteknoloji.com | 土耳其 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 60 | 待 | [SA-162-cansisteknoloji.com-土耳其.md](A/SA-162-cansisteknoloji.com-土耳其.md) |
| SA-163 | cyber-tec.net | 伊拉克 | 经销/集成（类型待核） | 有回复·跟进中 | 60 | 待 | [SA-163-cyber-tec.net-伊拉克.md](A/SA-163-cyber-tec.net-伊拉克.md) |
| SA-164 | dabos.com | 美国 | 经销/集成（类型待核） | 名单内·未触达 | 60 | 待 | [SA-164-dabos.com-美国.md](A/SA-164-dabos.com-美国.md) |
| SA-166 | landatel.com | 西班牙 | 品牌商/贴牌需求（OEM/ODM） | 已推送 1 次·未回复 | 60 | 待 | [SA-166-landatel.com-西班牙.md](A/SA-166-landatel.com-西班牙.md) |
| SA-167 | voltechelektronik.com | 土耳其 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 60 | 待 | [SA-167-voltechelektronik.com-土耳其.md](A/SA-167-voltechelektronik.com-土耳其.md) |

### B 级（1315）— `Saga Clients/B/`

全部 1315 个档案见 `Saga Clients/B/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

### C 级（3199）— `Saga Clients/C/`

全部 3199 个档案见 `Saga Clients/C/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

