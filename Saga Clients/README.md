# Saga Clients — Saga 历史客户全量档案（A / B / C）

> 生成：2026-10-27　|　来源：`Clients/`（Simon 上传到 main 的 137 个文件：6,246 行线索 + 20,819 条跟进记录）　|　归并后 **4648 个客户**：A 90 / B 1139 / C 3419
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
| 北美 | 17 | 161 | 309 | 487 |
| 欧洲 | 24 | 377 | 591 | 992 |
| 土耳其 | 10 | 124 | 74 | 208 |
| 中东 | 6 | 65 | 255 | 326 |
| 亚太 | 14 | 198 | 740 | 952 |
| 俄语区 | 8 | 72 | 424 | 504 |
| 南亚 | 6 | 67 | 386 | 459 |
| 拉美 | 3 | 21 | 226 | 250 |
| 非洲 | 2 | 49 | 290 | 341 |
| 乌克兰 | 0 | 1 | 54 | 55 |
| 中国大陆 | 0 | 0 | 17 | 17 |
| 未知 | 0 | 4 | 53 | 57 |
| **合计** | 90 | 1139 | 3419 | 4648 |

状态分布：名单内 2011；已推送 1239；WhatsApp 526；用户判定不行 445；有回复 229；成交过 100；发不过去 83；回复暂无需求 15

C 级细分：群发冷名单无回应 1128；用户判定不行/不相关 548；综合分低 389；品类不符（VC/DWDM/CCTV 等） 340；无联系方式 147；低价值区域冷线索 141；发不过去 116；陈旧线索无互动 116；无邮箱（仅电话） 78；守界：乌克兰 53；体量过大/品牌厂商/运营商 48；调研后定级 C 44；用户备注不再跟进/Spam 43；体量过大 20；品类不符/终端用户 17；品类不符 16；中国大陆（非出口客户） 16；同行/台湾厂商 10；个人买家 10；渠道冲突（Q-33 8；守界：军工 6；品类不符（软件） 6；巨头/集团 4；同行/厂商 4；区域外/品类不符 4；品类不符（非网络设备） 4；区域外/个人买家 4；中国厂商海外办事处 3；同行/自研 3；运营商 3；品类不符/非渠道 3；无邮箱 3；区域外/伊朗制裁合规风险 2；同行/贸易商 2；厂商办事处/同行 2；品类不符（板级/芯片） 2；专营品牌无切入点 2；守界（军工） 2；守界（公共部门） 2；体量过大/集团自有线 2；厂商/上市（非渠道） 2；体量过大/守界 2；品类不符（工程服务） 2；厂商/集团品牌（非渠道） 2；厂商/台湾（非渠道） 2；巨头/台湾厂商 2；运营商/体量过大 2；非渠道（工程服务） 2；明确退订 1；疑似同行/休眠公司 1；已停业 1；守界（轨道） 1；守界（公共部门/关键基础设施） 1；同行/国内厂商海外站 1；守界（军警/公共安全） 1；陈旧询盘 1；品类不符（防爆认证） 1；运营商/品类不符 1；品类不符（软件/信息服务） 1；品类不符/陈旧线索 1；体量过大/品牌厂商 1；上市集团/体量过大 1；同行/自研厂商 1；陈旧询盘/个人买家 1；守界（军工）/体量过大 1；品类不符（线缆集团） 1；品类不符（无源） 1；巨头/运营商 1；体量过大/品类不符（板级） 1；守界（军工/政府） 1；品类不符（品牌二手经纪） 1；守界：轨道/车载 1；守界（车载/轨道） 1；守界：轨道 1；个人买家/品类不符 1；厂商办事处/台湾厂商 1；同行/区域外 1；品类不符（消费级）/中国大陆背景 1；巨头/集团（同行） 1；巨头/上市（非渠道） 1；巨头/厂商 1；品类不符（轨道/车载） 1；区域外/终端用户 1；中介/品类不符 1；体量过大/同行 1；同行/专营俄产 1；厂商品牌/政府客户（俄区） 1；守界：政府客户（俄区） 1；板级/非渠道 1；区域外/同行 1；巨头/消费级 1；品类不符（板级嵌入式） 1；陈旧询盘/品类不符 1；守界（军工/国防） 1；巨头/区外（误并待拆） 1；巨头/上市 1；品类不符（软件/工程服务） 1；非渠道（服务商） 1；厂商/品类不符（PON） 1；品类不符（板级/芯片）/守界 1

## 调研覆盖（A 候选逐家网页核实）

- 自动评级曾为 A 的候选 **全部** 做了网页核实：1490 家（`data/saga_clients/research/`，每家含引文 + URL + 日期）；维持 A 1113 / 调研后降 B 100 / 调研后降 C 255。
- 降级口径：≥14 次推送 0 回复（即便面谈/OEM 意向）→ B 并标「回复即升 A」；核心需求在 Saga 线外（IP67、M12、HDMI 延长器、仅 SFP/DWDM、400G）→ B；已停业 / 休眠壳公司 / 疑似同行 / 军工守界 / TKH 等集团子公司 → C；中国直采的纯比价客户 → B。
- B/C 级未逐家网页核实（量级 4,500+），分级依据为用户表信号 + 规则；任一 B 升 A 前先补一份 research JSON。

## 档案结构（与 `profile/` 同骨架）

头部引言（评级/编号/状态）→ `yaml structured_profile` → SALES BRIEF → 基本事实（分层）→ 用户 AI/Claude 评估原文 → 客户调研（引文+URL+日期）→ 在卖/在用品牌→Saga 对位 → 历史跟进记录（原表照录）→ 联系方式（原值）→ 关键人（KP）与触达通道 → 来源与归并（原始行定位）→ 产品决策（P1 + 备选 + 价格快照）→ 跟进建议（3 步）→ SWOT → 触达与风险红线 → Qualification 清单 → Unknowns → 英文跟进邮件（样板）→ 新跟进记录 → 下次复核 → 变更日志。C 级省略产品决策/SWOT/邮件样板。

## 配套文件

- `data/saga_clients/客户主表.csv` — 一行一个客户（编号 / 等级 / 分数 / 联系方式 / 来源定位 / 评级依据）
- `data/saga_clients/重复客户归并记录.md` — 多来源客户与归并键、正负名单冲突
- `data/saga_clients/rows_raw.jsonl` / `followups.jsonl` / `extract_report.json` — 原始逐行抽取与逐文件行数（不漏复核）
- `data/saga_clients/research/` — 调研 JSON（引文 + URL + 日期；含 grade_override）
- `data/saga_clients/人工定级.csv` — 人工覆盖（列：键或编号, 等级, 理由）
- `Clients/` — 原件（只读，不改名不改内容）

## 索引

目录结构：A 平铺；B / C 每 500 户一个子目录（`B/SB-0001-0500/`、`B/SB-0501-1000/`、`B/SB-1001-1500/` …，GitHub 网页一个目录只显示前 1,000 个文件），编号连号，看编号就知道在哪个子目录；各级 `_索引.md` 的链接直达文件。

### A 级（90）— `Saga Clients/A/`

| 编号 | 公司 | 国家 | 类型 | 状态 | 分数 | 调研 | 档案 |
|---|---|---|---|---|---|---|---|
| SA-001 | asteldigicom.com | 阿联酋 | 分销商/网店（线缆·网络·太阳能） | 成交过·可发展（Simon） | 164 | 已 | [SA-001-asteldigicom.com-阿联酋.md](A/SA-001-asteldigicom.com-阿联酋.md) |
| SA-002 | simrex.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机 | 有回复·跟进中 | 88 | 已 | [SA-002-simrex.com-美国.md](A/SA-002-simrex.com-美国.md) |
| SA-003 | Eyescan security Systems | 塞浦路斯 | 安防集成/经销（兼分销） | 成交过·维护 | 133 | 已 | [SA-003-Eyescan security Systems-塞浦路斯.md](A/SA-003-Eyescan%20security%20Systems-塞浦路斯.md) |
| SA-004 | Boecek Sec | 德国 | 安防集成/经销（据用户备注推断） | 成交过·维护 | 131 | 已 | [SA-004-Boecek Sec-德国.md](A/SA-004-Boecek%20Sec-德国.md) |
| SA-005 | Taurus Vision | 南非 | 安防集成商（CCTV/视频管理） | 有回复·跟进中 | 67 | 已 | [SA-005-Taurus Vision-南非.md](A/SA-005-Taurus%20Vision-南非.md) |
| SA-006 | Vi-Link（vilinknet.com） | 美国 | 品牌商/贴牌需求（OEM/ODM）——光传输+工业以太网自有品牌 | 成交过·可发展（Simon） | 150 | 已 | [SA-006-Vi-Link（vilinknet.com）-美国.md](A/SA-006-Vi-Link（vilinknet.com）-美国.md) |
| SA-007 | gogreenit.net | 英国 | IT 服务商/终端（非渠道） | 成交过·可发展（Simon） | 116 | 已 | [SA-007-gogreenit.net-英国.md](A/SA-007-gogreenit.net-英国.md) |
| SA-008 | fiberone.de | 德国 | 运营商/ISP（终端 + 自有 logo 贴牌需求） | 成交过·活跃（Simon） | 112 | 已 | [SA-008-fiberone.de-德国.md](A/SA-008-fiberone.de-德国.md) |
| SA-009 | coptek.com.tr | 土耳其 | 分销商（网络设备，DCN 土耳其分销） | 成交过·维护 | 110 | 已 | [SA-009-coptek.com.tr-土耳其.md](A/SA-009-coptek.com.tr-土耳其.md) |
| SA-010 | NEXTU EZ-NET | 韩国 | 品牌商/分销商（自有品牌 NEXTU，OEM 采购） | 有回复·跟进中 | 103 | 已 | [SA-010-NEXTU EZ-NET-韩国.md](A/SA-010-NEXTU%20EZ-NET-韩国.md) |
| SA-011 | CXR | 法国 | 品牌商/贴牌需求（OEM/ODM）——工业网络设备自有品牌 | 有回复·跟进中 | 100 | 已 | [SA-011-CXR-法国.md](A/SA-011-CXR-法国.md) |
| SA-012 | widen.co.th | 泰国 | 分销商/品牌商（光纤产品自有 logo，OEM 采购） | 成交过·维护 | 97 | 已 | [SA-012-widen.co.th-泰国.md](A/SA-012-widen.co.th-泰国.md) |
| SA-013 | alfa.com.tw | 台湾 | 品牌商（台系无线网络品牌，PoE 交换机外采贴牌） | 有回复·跟进中 | 95 | 已 | [SA-013-alfa.com.tw-台湾.md](A/SA-013-alfa.com.tw-台湾.md) |
| SA-014 | impulsecctv.com | 新加坡 | 品牌商/贴牌需求（OEM/ODM）——安防品牌自有 PoE 交换机线 | 有回复·跟进中 | 94 | 已 | [SA-014-impulsecctv.com-新加坡.md](A/SA-014-impulsecctv.com-新加坡.md) |
| SA-015 | megnet.co.uk | 英国 | 分销商 + 自有品牌（Chimera，OEM 采购） | 有回复·跟进中 | 94 | 已 | [SA-015-megnet.co.uk-英国.md](A/SA-015-megnet.co.uk-英国.md) |
| SA-016 | BitBook LLC | 俄罗斯 | 分销商 + 自有品牌（条码为主，网络 PoE 为辅） | 成交过·可发展（Simon） | 90 | 已 | [SA-016-BitBook LLC-俄罗斯.md](A/SA-016-BitBook%20LLC-俄罗斯.md) |
| SA-017 | parallaxdigital.co.uk | 英国 | 微型 OEM/ODM 品牌商（自有品牌网络设备） | 有回复·跟进中 | 89 | 已 | [SA-017-parallaxdigital.co.uk-英国.md](A/SA-017-parallaxdigital.co.uk-英国.md) |
| SA-018 | Sewell | 美国 | 品牌商/电商（消费 AV 连接；PoE 电源复购客户） | 成交过·维护 | 88 | 已 | [SA-018-Sewell-美国.md](A/SA-018-Sewell-美国.md) |
| SA-019 | allnet.de | 德国 | 分销商 + 自有品牌（ALLNET，OEM 采购） | 有回复·跟进中 | 88 | 已 | [SA-019-allnet.de-德国.md](A/SA-019-allnet.de-德国.md) |
| SA-020 | bitstream.pl | 波兰 | 品牌商/制造商（工业网络自有品牌；MC/SFP/部分交换机可能外采贴牌） | 有回复·跟进中 | 88 | 已 | [SA-020-bitstream.pl-波兰.md](A/SA-020-bitstream.pl-波兰.md) |
| SA-021 | optiviewusa.com | 美国 | 分销商/品牌商（CCTV 批发，自有品牌 OEM 采购） | 有回复·跟进中 | 88 | 已 | [SA-021-optiviewusa.com-美国.md](A/SA-021-optiviewusa.com-美国.md) |
| SA-022 | Addon Computer Products | 美国 | 品牌商/制造商（兼容光模块；MC 等外采贴牌） | 成交过·维护 | 86 | 已 | [SA-022-Addon Computer Products-美国.md](A/SA-022-Addon%20Computer%20Products-美国.md) |
| SA-023 | fcnet.pl | 波兰 | 分销商/进口商（自有 logo 采购） | 有回复·跟进中 | 85 | 已 | [SA-023-fcnet.pl-波兰.md](A/SA-023-fcnet.pl-波兰.md) |
| SA-024 | Cable Distribution Services | 澳大利亚 | 分销商（工业线缆；拓展工业交换机） | 有回复·跟进中 | 84 | 已 | [SA-024-Cable Distribution Services-澳大利亚.md](A/SA-024-Cable%20Distribution%20Services-澳大利亚.md) |
| SA-025 | Avenger Security（getsecurityalarm.com） | 美国 | 安防集成/安装商（小型，自装自用采购） | 有回复·跟进中 | 84 | 已 | [SA-025-Avenger Security（getsecurityalarm.com）-美国.md](A/SA-025-Avenger%20Security（getsecurityalarm.com）-美国.md) |
| SA-026 | hardenednetworks.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌 | 有回复·跟进中 | 84 | 已 | [SA-026-hardenednetworks.com-美国.md](A/SA-026-hardenednetworks.com-美国.md) |
| SA-027 | Al Salami Trading L.L.C | 阿联酋 | 安防集成商（项目型小批量） | 有回复·跟进中 | 83 | 已 | [SA-027-Al Salami Trading L.L.C-阿联酋.md](A/SA-027-Al%20Salami%20Trading%20L.L.C-阿联酋.md) |
| SA-028 | entasource.co.th | 泰国 | 进口分销商（自有 logo） | 有回复·跟进中 | 83 | 已 | [SA-028-entasource.co.th-泰国.md](A/SA-028-entasource.co.th-泰国.md) |
| SA-029 | gtwave.co.kr | 韩国 | 品牌商（OEM/ODM 需求） | 有回复·跟进中 | 83 | 已 | [SA-029-gtwave.co.kr-韩国.md](A/SA-029-gtwave.co.kr-韩国.md) |
| SA-030 | snexus.com.tr | 土耳其 | 品牌商/经销（自有品牌白牌采购） | 已推送 2 次·未回复 | 83 | 已 | [SA-030-snexus.com.tr-土耳其.md](A/SA-030-snexus.com.tr-土耳其.md) |
| SA-031 | Truong Son Solutions | 越南 | 分销商/电商（工业交换机垂直） | 有回复·跟进中 | 67 | 已 | [SA-031-Truong Son Solutions-越南.md](A/SA-031-Truong%20Son%20Solutions-越南.md) |
| SA-032 | sundartechno.com | 印度 | 方案商/自有品牌贴牌（成交客户） | 成交过·可发展（Simon） | 82 | 已 | [SA-032-sundartechno.com-印度.md](A/SA-032-sundartechno.com-印度.md) |
| SA-033 | bluewarrior.com | 美国 | 品牌商（白牌贴牌，OEM 目标） | 有回复·跟进中 | 81 | 已 | [SA-033-bluewarrior.com-美国.md](A/SA-033-bluewarrior.com-美国.md) |
| SA-034 | rfog.pl | 波兰 | 分销商（自有型号贴牌） | 有回复·跟进中 | 81 | 已 | [SA-034-rfog.pl-波兰.md](A/SA-034-rfog.pl-波兰.md) |
| SA-035 | td-fe.com | 俄罗斯 | 品牌商/贸易公司（电源主业，工业交换机为配套） | 有回复·跟进中 | 81 | 已 | [SA-035-td-fe.com-俄罗斯.md](A/SA-035-td-fe.com-俄罗斯.md) |
| SA-036 | svn-video.ru | 俄罗斯 | 电商/安装商（自有型号贴牌） | 有回复·跟进中 | 80 | 已 | [SA-036-svn-video.ru-俄罗斯.md](A/SA-036-svn-video.ru-俄罗斯.md) |
| SA-037 | aeconnect.co.in | 印度 | 品牌商（部分进口贴牌 + 本地组装） | 有回复·跟进中 | 79 | 已 | [SA-037-aeconnect.co.in-印度.md](A/SA-037-aeconnect.co.in-印度.md) |
| SA-038 | dncsolutions.co.in | 印度 | 品牌商（光纤配套，MC 贴牌） | 有回复·跟进中 | 79 | 已 | [SA-038-dncsolutions.co.in-印度.md](A/SA-038-dncsolutions.co.in-印度.md) |
| SA-039 | mt-link.com | 巴基斯坦 | 品牌商（中国白牌贴牌，ODM 买家） | 有回复·跟进中 | 79 | 已 | [SA-039-mt-link.com-巴基斯坦.md](A/SA-039-mt-link.com-巴基斯坦.md) |
| SA-040 | success-network.co.th | 泰国 | 分销商/系统集成（多品牌） | 有回复·跟进中 | 79 | 已 | [SA-040-success-network.co.th-泰国.md](A/SA-040-success-network.co.th-泰国.md) |
| SA-041 | lightoptics.pl | 波兰 | 分销商/电商（自有品牌贴牌） | 有回复·跟进中 | 78 | 已 | [SA-041-lightoptics.pl-波兰.md](A/SA-041-lightoptics.pl-波兰.md) |
| SA-042 | antronix.com | 美国 | 品牌制造商（拓展以太网交换机产品线，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-042-antronix.com-美国.md](A/SA-042-antronix.com-美国.md) |
| SA-043 | direktronik.se | 瑞典 | 分销商/进口商（自有品牌 + 多品牌） | 有回复·跟进中 | 76 | 已 | [SA-043-direktronik.se-瑞典.md](A/SA-043-direktronik.se-瑞典.md) |
| SA-044 | dymec.com | 美国 | 品牌商（白牌贴牌，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-044-dymec.com-美国.md](A/SA-044-dymec.com-美国.md) |
| SA-045 | energyplusystems.cl | 智利 | 工业/矿业集成供应商（工业交换机为配套品类） | 有回复·跟进中 | 76 | 已 | [SA-045-energyplusystems.cl-智利.md](A/SA-045-energyplusystems.cl-智利.md) |
| SA-046 | ipcampower.com | 美国 | 品牌商/电商（中国白牌贴牌，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-046-ipcampower.com-美国.md](A/SA-046-ipcampower.com-美国.md) |
| SA-047 | sge.com.tr | 土耳其 | 工程分销商/集成（能源自动化；工业交换机转售） | 有回复·跟进中 | 76 | 已 | [SA-047-sge.com.tr-土耳其.md](A/SA-047-sge.com.tr-土耳其.md) |
| SA-048 | ekhalas.com | 沙特阿拉伯 | 系统集成商+电商分销 | 有回复·跟进中 | 75 | 已 | [SA-048-ekhalas.com-沙特阿拉伯.md](A/SA-048-ekhalas.com-沙特阿拉伯.md) |
| SA-049 | iotsistem.com | 土耳其 | 工业/IoT 分销商（网店） | 已推送 2 次·未回复 | 75 | 已 | [SA-049-iotsistem.com-土耳其.md](A/SA-049-iotsistem.com-土耳其.md) |
| SA-050 | impakt.com.pl | 波兰 | 品牌商（自有品牌 OEM 采购）+ 分销商 | 有回复·跟进中 | 74 | 已 | [SA-050-impakt.com.pl-波兰.md](A/SA-050-impakt.com.pl-波兰.md) |
| SA-051 | Tecpro Solutions | 阿联酋 | 系统集成商（IT/ELV） | 有回复·跟进中 | 73 | 已 | [SA-051-Tecpro Solutions-阿联酋.md](A/SA-051-Tecpro%20Solutions-阿联酋.md) |
| SA-052 | bsn-system.com | 印度尼西亚 | 安防/IT 集成商 | 有回复·跟进中 | 73 | 已 | [SA-052-bsn-system.com-印度尼西亚.md](A/SA-052-bsn-system.com-印度尼西亚.md) |
| SA-053 | infrateq.id | 印度尼西亚 | 系统集成商+分销（VoIP/安防/工业网络） | 有回复·跟进中 | 73 | 已 | [SA-053-infrateq.id-印度尼西亚.md](A/SA-053-infrateq.id-印度尼西亚.md) |
| SA-054 | softnetworks.net | 美国 | 二手/翻新网络设备经销商 | 有回复·跟进中 | 73 | 已 | [SA-054-softnetworks.net-美国.md](A/SA-054-softnetworks.net-美国.md) |
| SA-055 | NOVA Group Engineering Project Electronic Co LTD | 土耳其 | 进口批发商/分销商（弱电安防） | 已推送 4 次·未回复 | 72 | 已 | [SA-055-NOVA Group Engineering Project Electroni-土耳其.md](A/SA-055-NOVA%20Group%20Engineering%20Project%20Electroni-土耳其.md) |
| SA-056 | B&S electronics | 希腊 | 安防批发商/进口商 | WhatsApp 已加·未回复 | 71 | 已 | [SA-056-B&S electronics-希腊.md](A/SA-056-B&S%20electronics-希腊.md) |
| SA-057 | Born SPb LLC | 俄罗斯 | 多品牌贸易商/分销 | 有回复·跟进中 | 70 | 已 | [SA-057-Born SPb LLC-俄罗斯.md](A/SA-057-Born%20SPb%20LLC-俄罗斯.md) |
| SA-058 | alphanetcom.com | 美国 | 布线承包商/小型系统集成商 | 有回复·跟进中 | 70 | 已 | [SA-058-alphanetcom.com-美国.md](A/SA-058-alphanetcom.com-美国.md) |
| SA-059 | data-connect.com | 美国 | 品牌商（自有品牌）+ 分销 | 有回复·跟进中 | 70 | 已 | [SA-059-data-connect.com-美国.md](A/SA-059-data-connect.com-美国.md) |
| SA-060 | gofiberx.com | 美国 | ISP/运营商（终端用户） | 有回复·跟进中 | 70 | 已 | [SA-060-gofiberx.com-美国.md](A/SA-060-gofiberx.com-美国.md) |
| SA-061 | RYMTECH EAS | 巴拉圭 | 系统集成/工程商 | 有回复·跟进中 | 69 | 已 | [SA-061-RYMTECH EAS-巴拉圭.md](A/SA-061-RYMTECH%20EAS-巴拉圭.md) |
| SA-062 | ipns-uae.com | 阿联酋 | 系统集成商（兼自有 logo 贴牌采购） | 已推送 11 次·未回复 | 68 | 已 | [SA-062-ipns-uae.com-阿联酋.md](A/SA-062-ipns-uae.com-阿联酋.md) |
| SA-063 | Areca Embedded Systems Pvt Ltd | 印度 | 系统集成/设备商 | 有回复·跟进中 | 67 | 已 | [SA-063-Areca Embedded Systems Pvt Ltd-印度.md](A/SA-063-Areca%20Embedded%20Systems%20Pvt%20Ltd-印度.md) |
| SA-064 | optat.ru | 俄罗斯 | 招投标供货商/贸易商 | 有回复·跟进中 | 67 | 已 | [SA-064-optat.ru-俄罗斯.md](A/SA-064-optat.ru-俄罗斯.md) |
| SA-065 | smbit.co.il | 以色列 | ICT 系统集成商（含市政智慧城市项目） | WhatsApp 已加·未回复 | 66 | 已 | [SA-065-smbit.co.il-以色列.md](A/SA-065-smbit.co.il-以色列.md) |
| SA-066 | ccs-msk.ru | 俄罗斯 | 分销商（企业网络 + 工业以太网） | 有回复·跟进中 | 65 | 已 | [SA-066-ccs-msk.ru-俄罗斯.md](A/SA-066-ccs-msk.ru-俄罗斯.md) |
| SA-067 | Latmedia Group, LLC | 乌兹别克斯坦 | IT 集成/贸易商 | 名单内·未触达 | 63 | 已 | [SA-067-Latmedia Group, LLC-乌兹别克斯坦.md](A/SA-067-Latmedia%20Group,%20LLC-乌兹别克斯坦.md) |
| SA-068 | Pt.ras otomasi indonesia | 印度尼西亚 | 工业自动化/MEP 系统集成商 | 有回复·跟进中 | 63 | 已 | [SA-068-Pt.ras otomasi indonesia-印度尼西亚.md](A/SA-068-Pt.ras%20otomasi%20indonesia-印度尼西亚.md) |
| SA-069 | bptehno.ru | 俄罗斯 | 分销商（光纤传输/视频光端机） | 有回复·跟进中 | 62 | 已 | [SA-069-bptehno.ru-俄罗斯.md](A/SA-069-bptehno.ru-俄罗斯.md) |
| SA-070 | Top Italia | 意大利 | 经销/集成商 | 已推送 14 次·未回复 | 61 | 已 | [SA-070-Top Italia-意大利.md](A/SA-070-Top%20Italia-意大利.md) |
| SA-071 | surlink-tech.com | 玻利维亚 | 批发分销商（布线/光纤/网络） | 有回复·跟进中 | 61 | 已 | [SA-071-surlink-tech.com-玻利维亚.md](A/SA-071-surlink-tech.com-玻利维亚.md) |
| SA-072 | trans audio video group | 意大利 | AV/安防集成商 | 已推送 14 次·未回复 | 61 | 已 | [SA-072-trans audio video group-意大利.md](A/SA-072-trans%20audio%20video%20group-意大利.md) |
| SA-073 | vicomsecurity.com | 印度 | 安防系统集成商 + 自有品牌 | 有回复·跟进中 | 61 | 已 | [SA-073-vicomsecurity.com-印度.md](A/SA-073-vicomsecurity.com-印度.md) |
| SA-074 | Elite Team Security Ltd | 保加利亚 | 安保服务商 + 视频监控集成（终端用户/集成商） | 回复暂无需求 | 60 | 已 | [SA-074-Elite Team Security Ltd-保加利亚.md](A/SA-074-Elite%20Team%20Security%20Ltd-保加利亚.md) |
| SA-075 | Falke security | 德国 | 安防经销/项目商 | 已推送 7 次·未回复 | 60 | 已 | [SA-075-Falke security-德国.md](A/SA-075-Falke%20security-德国.md) |
| SA-076 | Telemobil | 土耳其 | IT/网络系统集成商 | WhatsApp 已加·未回复 | 60 | 已 | [SA-076-Telemobil-土耳其.md](A/SA-076-Telemobil-土耳其.md) |
| SA-077 | Angora Networks | 土耳其 | 系统集成商 + 自有品牌贴牌（OEM）——公共部门/运营商投标型 | 成交过·活跃（Simon） | 108 | 已 | [SA-077-Angora Networks-土耳其.md](A/SA-077-Angora%20Networks-土耳其.md) |
| SA-078 | James Clendenan Systems Ltd. | 加拿大 | 系统集成/工程（北温哥华） | 成交过·活跃（Simon） | 98 | 已 | [SA-078-James Clendenan Systems Ltd-加拿大.md](A/SA-078-James%20Clendenan%20Systems%20Ltd-加拿大.md) |
| SA-079 | Biz-Ethics Ltd.（BEL Networks） | 尼日利亚 | 网络设备经销/自有品牌 BNSC-（拉各斯） | 成交过·活跃（Simon） | 84 | 已 | [SA-079-Biz-Ethics Ltd.（BEL Networks）-尼日利亚.md](A/SA-079-Biz-Ethics%20Ltd.（BEL%20Networks）-尼日利亚.md) |
| SA-080 | PBA Forever Technology Co., Ltd. | 泰国 | 系统集成/工程 | 成交过·活跃（Simon） | 66 | 已 | [SA-080-PBA Forever Technology Co., Ltd-泰国.md](A/SA-080-PBA%20Forever%20Technology%20Co.,%20Ltd-泰国.md) |
| SA-081 | 4power.it | 意大利 | 分销商/经销商 | 已推送 6 次·未回复 | 59 | 已 | [SA-081-4power.it-意大利.md](A/SA-081-4power.it-意大利.md) |
| SA-082 | ISIMKO GmbH,Guhrower Straße | 德国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 54 | 已 | [SA-082-ISIMKO GmbH,Guhrower Straße-德国.md](A/SA-082-ISIMKO%20GmbH,Guhrower%20Straße-德国.md) |
| SA-083 | kyma.it | 意大利 | 经销/集成（类型待核） | 已推送 12 次·未回复 | 49 | 已 | [SA-083-kyma.it-意大利.md](A/SA-083-kyma.it-意大利.md) |
| SA-084 | Eds protection technology | 土耳其 | 经销/集成（类型待核） | 已推送 2 次·未回复 | 43 | 已 | [SA-084-Eds protection technology-土耳其.md](A/SA-084-Eds%20protection%20technology-土耳其.md) |
| SA-085 | HCS | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 43 | 已 | [SA-085-HCS-土耳其.md](A/SA-085-HCS-土耳其.md) |
| SA-086 | netas.com.tr | 土耳其 | 经销/集成（类型待核） | 成交过·活跃（Simon） | 90 | 已 | [SA-086-netas.com.tr-土耳其.md](A/SA-086-netas.com.tr-土耳其.md) |
| SA-087 | norelcosafecam.com | 加拿大 | 经销/集成（类型待核） | 已推送 13 次·未回复 | 38 | 已 | [SA-087-norelcosafecam.com-加拿大.md](A/SA-087-norelcosafecam.com-加拿大.md) |
| SA-088 | ute.de | 德国 | 分销商/经销商 | 名单内·未触达 | 25 | 已 | [SA-088-ute.de-德国.md](A/SA-088-ute.de-德国.md) |
| SA-089 | lancomat.cz | 捷克 | 经销/集成（类型待核） | 名单内·未触达 | 17 | 已 | [SA-089-lancomat.cz-捷克.md](A/SA-089-lancomat.cz-捷克.md) |
| SA-090 | WizardsInc Sdn Bhd | 马来西亚 | 经销/集成（类型待核） | 成交过·可发展（Simon） | 62 | 已 | [SA-090-WizardsInc Sdn Bhd-马来西亚.md](A/SA-090-WizardsInc%20Sdn%20Bhd-马来西亚.md) |

### B 级（1139）— `Saga Clients/B/`（子目录 `SB-0001-0500/` / `SB-0501-1000/` / `SB-1001-1500/`）

全部 1139 个档案见 `Saga Clients/B/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

### C 级（3419）— `Saga Clients/C/`（子目录 `SC-0001-0500/` / `SC-0501-1000/` / `SC-1001-1500/` / `SC-1501-2000/` / `SC-2001-2500/` / `SC-2501-3000/` / `SC-3001-3500/`）

全部 3419 个档案见 `Saga Clients/C/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

