# Saga Clients — Saga 历史客户全量档案（A / B / C）

> 生成：2026-10-29　|　来源：`Clients/`（Simon 上传到 main 的 137 个文件：6,246 行线索 + 20,819 条跟进记录）　|　归并后 **4647 个客户**：A 169 / B 1229 / C 3249
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
| 北美 | 29 | 163 | 293 | 485 |
| 欧洲 | 41 | 425 | 531 | 997 |
| 土耳其 | 15 | 120 | 72 | 207 |
| 中东 | 12 | 61 | 253 | 326 |
| 亚太 | 24 | 210 | 718 | 952 |
| 俄语区 | 13 | 92 | 399 | 504 |
| 南亚 | 21 | 80 | 359 | 460 |
| 拉美 | 4 | 30 | 215 | 249 |
| 非洲 | 9 | 46 | 286 | 341 |
| 乌克兰 | 0 | 0 | 55 | 55 |
| 中国大陆 | 0 | 0 | 17 | 17 |
| 未知 | 1 | 2 | 51 | 54 |
| **合计** | 169 | 1229 | 3249 | 4647 |

状态分布：名单内 2011；已推送 1239；WhatsApp 526；用户判定不行 444；有回复 229；成交过 100；发不过去 83；回复暂无需求 15

C 级细分：群发冷名单无回应 1047；用户判定不行/不相关 500；综合分低 361；品类不符（VC/DWDM/CCTV 等） 335；无联系方式 145；低价值区域冷线索 131；陈旧线索无互动 113；发不过去 102；无邮箱（仅电话） 72；守界：乌克兰 53；体量过大/品牌厂商/运营商 48；调研后定级 C 43；用户备注不再跟进/Spam 43；储备·复核打回 32；品类不符/终端用户 17；体量过大 17；品类不符 16；中国大陆（非出口客户） 16；个人买家 10；同行/台湾厂商 9；渠道冲突（Q-33 8；守界：军工 6；品类不符（软件） 6；巨头/集团 4；同行/厂商 4；区域外/品类不符 4；品类不符（非网络设备） 4；区域外/个人买家 4；中国厂商海外办事处 3；同行/自研 3；运营商 3；品类不符/非渠道 3；无邮箱 3；区域外/伊朗制裁合规风险 2；同行/贸易商 2；厂商办事处/同行 2；品类不符（板级/芯片） 2；专营品牌无切入点 2；守界（军工） 2；守界（公共部门） 2；体量过大/集团自有线 2；厂商/上市（非渠道） 2；体量过大/守界 2；品类不符（工程服务） 2；厂商/集团品牌（非渠道） 2；厂商/台湾（非渠道） 2；巨头/台湾厂商 2；运营商/体量过大 2；非渠道（工程服务） 2；储备·守界 1；明确退订 1；疑似同行/休眠公司 1；已停业 1；守界（轨道） 1；守界（公共部门/关键基础设施） 1；同行/国内厂商海外站 1；守界（军警/公共安全） 1；陈旧询盘 1；品类不符（防爆认证） 1；运营商/品类不符 1；品类不符（软件/信息服务） 1；品类不符/陈旧线索 1；体量过大/品牌厂商 1；上市集团/体量过大 1；同行/自研厂商 1；陈旧询盘/个人买家 1；守界（军工）/体量过大 1；品类不符（线缆集团） 1；品类不符（无源） 1；巨头/运营商 1；体量过大/品类不符（板级） 1；守界（军工/政府） 1；品类不符（品牌二手经纪） 1；守界：轨道/车载 1；守界（车载/轨道） 1；守界：轨道 1；个人买家/品类不符 1；厂商办事处/台湾厂商 1；同行/区域外 1；品类不符（消费级）/中国大陆背景 1；巨头/集团（同行） 1；巨头/上市（非渠道） 1；巨头/厂商 1；品类不符（轨道/车载） 1；区域外/终端用户 1；中介/品类不符 1；同行/专营俄产 1；厂商品牌/政府客户（俄区） 1；守界：政府客户（俄区） 1；板级/非渠道 1；区域外/同行 1；巨头/消费级 1；品类不符（板级嵌入式） 1；陈旧询盘/品类不符 1；守界（军工/国防） 1；巨头/区外（误并待拆） 1；巨头/上市 1；品类不符（软件/工程服务） 1；非渠道（服务商） 1；厂商/品类不符（PON） 1；品类不符（板级/芯片）/守界 1

## 调研覆盖（A 候选逐家网页核实）

- 自动评级曾为 A 的候选 **全部** 做了网页核实：1698 家（`data/saga_clients/research/`，每家含引文 + URL + 日期）；维持 A 994 / 调研后降 B 296 / 调研后降 C 291。
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

### A 级（169）— `Saga Clients/A/`

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
| SA-015 | megnet.co.uk | 英国 | 分销商 + 自有品牌（Chimera，OEM 采购） | 有回复·跟进中 | 94 | 已 | [SA-015-megnet.co.uk-英国.md](A/SA-015-megnet.co.uk-英国.md) |
| SA-016 | BitBook LLC | 俄罗斯 | 分销商 + 自有品牌（条码为主，网络 PoE 为辅） | 成交过·可发展（Simon） | 90 | 已 | [SA-016-BitBook LLC-俄罗斯.md](A/SA-016-BitBook%20LLC-俄罗斯.md) |
| SA-017 | parallaxdigital.co.uk | 英国 | 微型 OEM/ODM 品牌商（自有品牌网络设备） | 有回复·跟进中 | 89 | 已 | [SA-017-parallaxdigital.co.uk-英国.md](A/SA-017-parallaxdigital.co.uk-英国.md) |
| SA-018 | Sewell | 美国 | 品牌商/电商（消费 AV 连接；PoE 电源复购客户） | 成交过·维护 | 88 | 已 | [SA-018-Sewell-美国.md](A/SA-018-Sewell-美国.md) |
| SA-019 | allnet.de | 德国 | 分销商 + 自有品牌（ALLNET，OEM 采购） | 有回复·跟进中 | 88 | 已 | [SA-019-allnet.de-德国.md](A/SA-019-allnet.de-德国.md) |
| SA-020 | bitstream.pl | 波兰 | 品牌商/制造商（工业网络自有品牌；MC/SFP/部分交换机可能外采贴牌） | 有回复·跟进中 | 88 | 已 | [SA-020-bitstream.pl-波兰.md](A/SA-020-bitstream.pl-波兰.md) |
| SA-021 | optiviewusa.com | 美国 | 分销商/品牌商（CCTV 批发，自有品牌 OEM 采购） | 有回复·跟进中 | 88 | 已 | [SA-021-optiviewusa.com-美国.md](A/SA-021-optiviewusa.com-美国.md) |
| SA-022 | Addon Computer Products | 美国 | 品牌商/制造商（兼容光模块；MC 等外采贴牌） | 成交过·维护 | 86 | 已 | [SA-022-Addon Computer Products-美国.md](A/SA-022-Addon%20Computer%20Products-美国.md) |
| SA-023 | fcnet.pl | 波兰 | 分销商/进口商（自有 logo 采购） | 有回复·跟进中 | 85 | 已 | [SA-023-fcnet.pl-波兰.md](A/SA-023-fcnet.pl-波兰.md) |
| SA-025 | Avenger Security（getsecurityalarm.com） | 美国 | 安防集成/安装商（小型，自装自用采购） | 有回复·跟进中 | 84 | 已 | [SA-025-Avenger Security（getsecurityalarm.com）-美国.md](A/SA-025-Avenger%20Security（getsecurityalarm.com）-美国.md) |
| SA-026 | hardenednetworks.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌 | 有回复·跟进中 | 84 | 已 | [SA-026-hardenednetworks.com-美国.md](A/SA-026-hardenednetworks.com-美国.md) |
| SA-027 | Al Salami Trading L.L.C | 阿联酋 | 安防集成商（项目型小批量） | 有回复·跟进中 | 83 | 已 | [SA-027-Al Salami Trading L.L.C-阿联酋.md](A/SA-027-Al%20Salami%20Trading%20L.L.C-阿联酋.md) |
| SA-028 | entasource.co.th | 泰国 | 进口分销商（自有 logo） | 有回复·跟进中 | 83 | 已 | [SA-028-entasource.co.th-泰国.md](A/SA-028-entasource.co.th-泰国.md) |
| SA-029 | gtwave.co.kr | 韩国 | 品牌商（OEM/ODM 需求） | 有回复·跟进中 | 83 | 已 | [SA-029-gtwave.co.kr-韩国.md](A/SA-029-gtwave.co.kr-韩国.md) |
| SA-030 | snexus.com.tr | 土耳其 | 品牌商/经销（自有品牌白牌采购） | 已推送 2 次·未回复 | 83 | 已 | [SA-030-snexus.com.tr-土耳其.md](A/SA-030-snexus.com.tr-土耳其.md) |
| SA-031 | Truong Son Solutions | 越南 | 分销商/电商（工业交换机垂直） | 有回复·跟进中 | 67 | 已 | [SA-031-Truong Son Solutions-越南.md](A/SA-031-Truong%20Son%20Solutions-越南.md) |
| SA-032 | sundartechno.com | 印度 | 方案商/自有品牌贴牌（成交客户） | 成交过·可发展（Simon） | 82 | 已 | [SA-032-sundartechno.com-印度.md](A/SA-032-sundartechno.com-印度.md) |
| SA-034 | rfog.pl | 波兰 | 分销商（自有型号贴牌） | 有回复·跟进中 | 81 | 已 | [SA-034-rfog.pl-波兰.md](A/SA-034-rfog.pl-波兰.md) |
| SA-035 | td-fe.com | 俄罗斯 | 品牌商/贸易公司（电源主业，工业交换机为配套） | 有回复·跟进中 | 81 | 已 | [SA-035-td-fe.com-俄罗斯.md](A/SA-035-td-fe.com-俄罗斯.md) |
| SA-036 | svn-video.ru | 俄罗斯 | 电商/安装商（自有型号贴牌） | 有回复·跟进中 | 80 | 已 | [SA-036-svn-video.ru-俄罗斯.md](A/SA-036-svn-video.ru-俄罗斯.md) |
| SA-037 | aeconnect.co.in | 印度 | 品牌商（部分进口贴牌 + 本地组装） | 有回复·跟进中 | 79 | 已 | [SA-037-aeconnect.co.in-印度.md](A/SA-037-aeconnect.co.in-印度.md) |
| SA-038 | dncsolutions.co.in | 印度 | 品牌商（光纤配套，MC 贴牌） | 有回复·跟进中 | 79 | 已 | [SA-038-dncsolutions.co.in-印度.md](A/SA-038-dncsolutions.co.in-印度.md) |
| SA-039 | mt-link.com | 巴基斯坦 | 品牌商（中国白牌贴牌，ODM 买家） | 有回复·跟进中 | 79 | 已 | [SA-039-mt-link.com-巴基斯坦.md](A/SA-039-mt-link.com-巴基斯坦.md) |
| SA-041 | lightoptics.pl | 波兰 | 分销商/电商（自有品牌贴牌） | 有回复·跟进中 | 78 | 已 | [SA-041-lightoptics.pl-波兰.md](A/SA-041-lightoptics.pl-波兰.md) |
| SA-042 | antronix.com | 美国 | 品牌制造商（拓展以太网交换机产品线，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-042-antronix.com-美国.md](A/SA-042-antronix.com-美国.md) |
| SA-044 | dymec.com | 美国 | 品牌商（白牌贴牌，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-044-dymec.com-美国.md](A/SA-044-dymec.com-美国.md) |
| SA-045 | energyplusystems.cl | 智利 | 工业/矿业集成供应商（工业交换机为配套品类） | 有回复·跟进中 | 76 | 已 | [SA-045-energyplusystems.cl-智利.md](A/SA-045-energyplusystems.cl-智利.md) |
| SA-048 | ekhalas.com | 沙特阿拉伯 | 系统集成商+电商分销 | 有回复·跟进中 | 75 | 已 | [SA-048-ekhalas.com-沙特阿拉伯.md](A/SA-048-ekhalas.com-沙特阿拉伯.md) |
| SA-049 | iotsistem.com | 土耳其 | 工业/IoT 分销商（网店） | 已推送 2 次·未回复 | 75 | 已 | [SA-049-iotsistem.com-土耳其.md](A/SA-049-iotsistem.com-土耳其.md) |
| SA-050 | impakt.com.pl | 波兰 | 品牌商（自有品牌 OEM 采购）+ 分销商 | 有回复·跟进中 | 74 | 已 | [SA-050-impakt.com.pl-波兰.md](A/SA-050-impakt.com.pl-波兰.md) |
| SA-051 | Tecpro Solutions | 阿联酋 | 系统集成商（IT/ELV） | 有回复·跟进中 | 73 | 已 | [SA-051-Tecpro Solutions-阿联酋.md](A/SA-051-Tecpro%20Solutions-阿联酋.md) |
| SA-053 | infrateq.id | 印度尼西亚 | 系统集成商+分销（VoIP/安防/工业网络） | 有回复·跟进中 | 73 | 已 | [SA-053-infrateq.id-印度尼西亚.md](A/SA-053-infrateq.id-印度尼西亚.md) |
| SA-054 | softnetworks.net | 美国 | 二手/翻新网络设备经销商 | 有回复·跟进中 | 73 | 已 | [SA-054-softnetworks.net-美国.md](A/SA-054-softnetworks.net-美国.md) |
| SA-055 | NOVA Group Engineering Project Electronic Co LTD | 土耳其 | 进口批发商/分销商（弱电安防） | 已推送 4 次·未回复 | 72 | 已 | [SA-055-NOVA Group Engineering Project Electroni-土耳其.md](A/SA-055-NOVA%20Group%20Engineering%20Project%20Electroni-土耳其.md) |
| SA-057 | Born SPb LLC | 俄罗斯 | 多品牌贸易商/分销 | 有回复·跟进中 | 70 | 已 | [SA-057-Born SPb LLC-俄罗斯.md](A/SA-057-Born%20SPb%20LLC-俄罗斯.md) |
| SA-058 | alphanetcom.com | 美国 | 布线承包商/小型系统集成商 | 有回复·跟进中 | 70 | 已 | [SA-058-alphanetcom.com-美国.md](A/SA-058-alphanetcom.com-美国.md) |
| SA-059 | data-connect.com | 美国 | 品牌商（自有品牌）+ 分销 | 有回复·跟进中 | 70 | 已 | [SA-059-data-connect.com-美国.md](A/SA-059-data-connect.com-美国.md) |
| SA-060 | gofiberx.com | 美国 | ISP/运营商（终端用户） | 有回复·跟进中 | 70 | 已 | [SA-060-gofiberx.com-美国.md](A/SA-060-gofiberx.com-美国.md) |
| SA-061 | RYMTECH EAS | 巴拉圭 | 系统集成/工程商 | 有回复·跟进中 | 69 | 已 | [SA-061-RYMTECH EAS-巴拉圭.md](A/SA-061-RYMTECH%20EAS-巴拉圭.md) |
| SA-062 | ipns-uae.com | 阿联酋 | 系统集成商（兼自有 logo 贴牌采购） | 已推送 11 次·未回复 | 68 | 已 | [SA-062-ipns-uae.com-阿联酋.md](A/SA-062-ipns-uae.com-阿联酋.md) |
| SA-063 | Areca Embedded Systems Pvt Ltd | 印度 | 系统集成/设备商 | 有回复·跟进中 | 67 | 已 | [SA-063-Areca Embedded Systems Pvt Ltd-印度.md](A/SA-063-Areca%20Embedded%20Systems%20Pvt%20Ltd-印度.md) |
| SA-064 | optat.ru | 俄罗斯 | 招投标供货商/贸易商 | 有回复·跟进中 | 67 | 已 | [SA-064-optat.ru-俄罗斯.md](A/SA-064-optat.ru-俄罗斯.md) |
| SA-067 | Latmedia Group, LLC | 乌兹别克斯坦 | IT 集成/贸易商 | 名单内·未触达 | 63 | 已 | [SA-067-Latmedia Group, LLC-乌兹别克斯坦.md](A/SA-067-Latmedia%20Group,%20LLC-乌兹别克斯坦.md) |
| SA-068 | Pt.ras otomasi indonesia | 印度尼西亚 | 工业自动化/MEP 系统集成商 | 有回复·跟进中 | 63 | 已 | [SA-068-Pt.ras otomasi indonesia-印度尼西亚.md](A/SA-068-Pt.ras%20otomasi%20indonesia-印度尼西亚.md) |
| SA-069 | bptehno.ru | 俄罗斯 | 分销商（光纤传输/视频光端机） | 有回复·跟进中 | 62 | 已 | [SA-069-bptehno.ru-俄罗斯.md](A/SA-069-bptehno.ru-俄罗斯.md) |
| SA-077 | Angora Networks | 土耳其 | 系统集成商 + 自有品牌贴牌（OEM）——公共部门/运营商投标型 | 成交过·活跃（Simon） | 108 | 已 | [SA-077-Angora Networks-土耳其.md](A/SA-077-Angora%20Networks-土耳其.md) |
| SA-078 | James Clendenan Systems Ltd. | 加拿大 | 系统集成/工程（北温哥华） | 成交过·活跃（Simon） | 98 | 已 | [SA-078-James Clendenan Systems Ltd-加拿大.md](A/SA-078-James%20Clendenan%20Systems%20Ltd-加拿大.md) |
| SA-079 | Biz-Ethics Ltd.（BEL Networks） | 尼日利亚 | 网络设备经销/自有品牌 BNSC-（拉各斯） | 成交过·活跃（Simon） | 84 | 已 | [SA-079-Biz-Ethics Ltd.（BEL Networks）-尼日利亚.md](A/SA-079-Biz-Ethics%20Ltd.（BEL%20Networks）-尼日利亚.md) |
| SA-080 | PBA Forever Technology Co., Ltd. | 泰国 | 系统集成/工程 | 成交过·活跃（Simon） | 66 | 已 | [SA-080-PBA Forever Technology Co., Ltd-泰国.md](A/SA-080-PBA%20Forever%20Technology%20Co.,%20Ltd-泰国.md) |
| SA-082 | ISIMKO GmbH,Guhrower Straße | 德国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 54 | 已 | [SA-082-ISIMKO GmbH,Guhrower Straße-德国.md](A/SA-082-ISIMKO%20GmbH,Guhrower%20Straße-德国.md) |
| SA-085 | HCS | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 43 | 已 | [SA-085-HCS-土耳其.md](A/SA-085-HCS-土耳其.md) |
| SA-086 | netas.com.tr | 土耳其 | 经销/集成（类型待核） | 成交过·活跃（Simon） | 90 | 已 | [SA-086-netas.com.tr-土耳其.md](A/SA-086-netas.com.tr-土耳其.md) |
| SA-090 | WizardsInc Sdn Bhd | 马来西亚 | 经销/集成（类型待核） | 成交过·可发展（Simon） | 62 | 已 | [SA-090-WizardsInc Sdn Bhd-马来西亚.md](A/SA-090-WizardsInc%20Sdn%20Bhd-马来西亚.md) |
| SB-004 | fhn-na.com | 美国 | 中资大厂海外分公司（终端/项目采购） | 有回复·跟进中 | 23 | 已 | [SB-004-fhn-na.com-美国.md](A/SB-004-fhn-na.com-美国.md) |
| SB-005 | rovez.sk | 斯洛伐克 | 安防集成商（Avigilon 经销） | 成交过·维护 | 109 | 已 | [SB-005-rovez.sk-斯洛伐克.md](A/SB-005-rovez.sk-斯洛伐克.md) |
| SB-009 | sicurmax.com | 意大利 | 安防集成商（含军方/NATO 场所资质） | 成交过·维护 | 93 | 已 | [SB-009-sicurmax.com-意大利.md](A/SB-009-sicurmax.com-意大利.md) |
| SB-010 | americanfibertek.com | 美国 | 品牌商（美国本土制造 + TAA 外采线） | 有回复·跟进中 | 88 | 已 | [SB-010-americanfibertek.com-美国.md](A/SB-010-americanfibertek.com-美国.md) |
| SB-011 | greentechme.net | 阿联酋 | 未知（疑为太阳能/能源方案商） | 成交过·维护 | 88 | 已 | [SB-011-greentechme.net-阿联酋.md](A/SB-011-greentechme.net-阿联酋.md) |
| SB-013 | synchcom.com.pk | 巴基斯坦 | 系统集成 + 分销（电信/IT/国防） | 成交过·维护 | 87 | 已 | [SB-013-synchcom.com.pk-巴基斯坦.md](A/SB-013-synchcom.com.pk-巴基斯坦.md) |
| SB-015 | suministros-industriales.es | 西班牙 | 工业 MRO 供应商（非网络渠道） | 有回复·跟进中 | 80 | 已 | [SB-015-suministros-industriales.es-西班牙.md](A/SB-015-suministros-industriales.es-西班牙.md) |
| SB-017 | Securitytec | 英国 | 安防批发商（小型） | 成交过·维护 | 78 | 已 | [SB-017-Securitytec-英国.md](A/SB-017-Securitytec-英国.md) |
| SB-038 | tricomp.com.pl | 波兰 | IT/电信工程与咨询公司 | 有回复·跟进中 | 68 | 已 | [SB-038-tricomp.com.pl-波兰.md](A/SB-038-tricomp.com.pl-波兰.md) |
| SB-040 | 4Demand Co | 英国 | IT 贸易商 | 有回复·跟进中 | 67 | 已 | [SB-040-4Demand Co-英国.md](A/SB-040-4Demand%20Co-英国.md) |
| SB-043 | Euro Technology | 阿联酋 | 安防系统集成商 | 有回复·跟进中 | 65 | 已 | [SB-043-Euro Technology-阿联酋.md](A/SB-043-Euro%20Technology-阿联酋.md) |
| SB-053 | onnettechnologies.com | 阿联酋 | IT 贸易商 | 有回复·跟进中 | 63 | 已 | [SB-053-onnettechnologies.com-阿联酋.md](A/SB-053-onnettechnologies.com-阿联酋.md) |
| SB-058 | SABMARtv | 波兰 | 视频/广电技术经销商 | 成交过·维护 | 47 | 已 | [SB-058-SABMARtv-波兰.md](A/SB-058-SABMARtv-波兰.md) |
| SB-069 | mutexsystemsltd.com | 巴基斯坦 | IT 公司 | 成交过·维护 | 61 | 已 | [SB-069-mutexsystemsltd.com-巴基斯坦.md](A/SB-069-mutexsystemsltd.com-巴基斯坦.md) |
| SB-071 | nkstech.net | 菲律宾 | 经销/集成商 | 成交过·维护 | 61 | 已 | [SB-071-nkstech.net-菲律宾.md](A/SB-071-nkstech.net-菲律宾.md) |
| SB-074 | Bilge SECURITY SYSTEMS | 土耳其 | 安防安装/经销商 | WhatsApp 已加·未回复 | 60 | 已 | [SB-074-Bilge SECURITY SYSTEMS-土耳其.md](A/SB-074-Bilge%20SECURITY%20SYSTEMS-土耳其.md) |
| SB-077 | Liveye | 德国 | 安防产品商 | WhatsApp 已加·未回复 | 60 | 已 | [SB-077-Liveye-德国.md](A/SB-077-Liveye-德国.md) |
| SB-083 | MERIT LILIN ENT. CO., LTD. | 台湾 | 品牌商/贴牌需求（OEM/ODM） | 有回复·跟进中 | 91 | 已 | [SB-083-MERIT LILIN ENT. CO., LTD-台湾.md](A/SB-083-MERIT%20LILIN%20ENT.%20CO.,%20LTD-台湾.md) |
| SB-084 | AD-NET TECHNOLOGY CO., LTD. | 台湾 | 品牌商/贴牌需求（OEM/ODM） | 有回复·跟进中 | 83 | 已 | [SB-084-AD-NET TECHNOLOGY CO., LTD-台湾.md](A/SB-084-AD-NET%20TECHNOLOGY%20CO.,%20LTD-台湾.md) |
| SB-085 | DIGI Group | 美国 | 经销/集成（类型待核） | 有回复·跟进中 | 83 | 已 | [SB-085-DIGI Group-美国.md](A/SB-085-DIGI%20Group-美国.md) |
| SB-086 | TAILYN | 台湾 | 经销/集成（类型待核） | 有回复·跟进中 | 83 | 已 | [SB-086-TAILYN-台湾.md](A/SB-086-TAILYN-台湾.md) |
| SB-103 | Grundig | 德国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 59 | 已 | [SB-103-Grundig-德国.md](A/SB-103-Grundig-德国.md) |
| SB-1031 | findcontrols.com | 英国 | 分销商/经销商 | WhatsApp 已加·未回复 | 25 | 已 | [SB-1031-findcontrols.com-英国.md](A/SB-1031-findcontrols.com-英国.md) |
| SB-1054 | luxritesecurity.com | 英国 | 英国 Trade 安防分销商（Ruijie PoE） | 名单内·未触达 | 25 | 已 | [SB-1054-luxritesecurity.com-英国.md](A/SB-1054-luxritesecurity.com-英国.md) |
| SB-110 | itkati.com | 乌干达 | 经销/集成（类型待核） | 有回复·跟进中 | 59 | 已 | [SB-110-itkati.com-乌干达.md](A/SB-110-itkati.com-乌干达.md) |
| SB-1103 | ara.com.bd | 孟加拉国 | 品牌商/贴牌需求（OEM/ODM） | 有回复·跟进中 | 20 | 已 | [SB-1103-ara.com.bd-孟加拉国.md](A/SB-1103-ara.com.bd-孟加拉国.md) |
| SB-111 | nivoxtech.com | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 59 | 已 | [SB-111-nivoxtech.com-印度.md](A/SB-111-nivoxtech.com-印度.md) |
| SB-1114 | Fikes Media | 美国 | IT 集成 / 网络顾问（一人公司；客群 = 地方政府 / K-12 与高校 / SMB；方案 = 企业网络、数据中心网络、VoIP、MikroTik 咨询） | 名单内·未触达 | 58 | 已 | [SB-1114-Fikes Media-美国.md](A/SB-1114-Fikes%20Media-美国.md) |
| SB-1115 | Milliseconds Evolution Limited | 英国 | 网络集成/MikroTik 顾问（拟经销） | 名单内·未触达 | 46 | 已 | [SB-1115-Milliseconds Evolution Limited-英国.md](A/SB-1115-Milliseconds%20Evolution%20Limited-英国.md) |
| SB-1117 | Switchcom Distribution (Pty) Ltd | 南非 | 网络设备分销商（ICT 分销：无线 / 网络 / VoIP / 监控 / 光纤；服务 reseller / installer / ISP / WISP / 终端；Shopify 网店） | 名单内·未触达 | 31 | 已 | [SB-1117-Switchcom Distribution (Pty) Ltd-南非.md](A/SB-1117-Switchcom%20Distribution%20(Pty)%20Ltd-南非.md) |
| SB-1121 | technetix.com | 英国 | OEM 品牌商（光纤/宽带接入设备） | 有回复·跟进中 | 18 | 已 | [SB-1121-technetix.com-英国.md](A/SB-1121-technetix.com-英国.md) |
| SB-1122 | comtinu.ru | 俄罗斯 | 俄罗斯网络项目商（25G/100G 项目） | 名单内·未触达 | 17 | 已 | [SB-1122-comtinu.ru-俄罗斯.md](A/SB-1122-comtinu.ru-俄罗斯.md) |
| SB-1134 | conexionderedes.com | 萨尔瓦多 | 中美洲网络集成/分销商（为其客户转发方案） | 已推送 13 次·未回复 | 7 | 已 | [SB-1134-conexionderedes.com-萨尔瓦多.md](A/SB-1134-conexionderedes.com-萨尔瓦多.md) |
| SB-1135 | raisecom.su | 俄罗斯 | 俄罗斯经销/项目商（Raisecom 代理） | 成交过·维护 | 5 | 已 | [SB-1135-raisecom.su-俄罗斯.md](A/SB-1135-raisecom.su-俄罗斯.md) |
| SB-1137 | Infotec Comercio de Equipamentos e Sistemas de Segurança Ltda. | 巴西 | 巴西安防设备经销（CCTV） | 名单内·未触达 | -2 | 已 | [SB-1137-Infotec Comercio de Equipamentos e Siste-巴西.md](A/SB-1137-Infotec%20Comercio%20de%20Equipamentos%20e%20Siste-巴西.md) |
| SB-1138 | devray.in | 印度 | 印度 Make-in-India OEM（自称 OEM for Switches / NGFW / SDWAN；ISO 27001 / CERT-In Empanelled） | 名单内·未触达 | -4 | 已 | [SB-1138-devray.in-印度.md](A/SB-1138-devray.in-印度.md) |
| SB-1139 | arnoldomohr@gmail.com | 未填 | 方案商 / 项目经理（为终端客户找 Cisco 替代） | 名单内·未触达 | -18 | 已 | [SB-1139-arnoldomohr@gmail.com-未填.md](A/SB-1139-arnoldomohr@gmail.com-未填.md) |
| SB-118 | genrov.com | 英国 | 经销/集成（类型待核） | 有回复·跟进中 | 58 | 已 | [SB-118-genrov.com-英国.md](A/SB-118-genrov.com-英国.md) |
| SB-119 | wirestar.net | 美国 | 经销/集成（类型待核） | 有回复·跟进中 | 58 | 已 | [SB-119-wirestar.net-美国.md](A/SB-119-wirestar.net-美国.md) |
| SB-122 | Tera Technologies and Engineering Ltd | 坦桑尼亚 | 系统集成/工程商 | 有回复·跟进中 | 57 | 已 | [SB-122-Tera Technologies and Engineering Ltd-坦桑尼亚.md](A/SB-122-Tera%20Technologies%20and%20Engineering%20Ltd-坦桑尼亚.md) |
| SB-132 | F.A.S.T | 土耳其 | 工业自动化/IoT 方案商 | 名单内·未触达 | 55 | 已 | [SB-132-F.A.S.T-土耳其.md](A/SB-132-F.A.S.T-土耳其.md) |
| SB-143 | broadstar.com | 美国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 55 | 已 | [SB-143-broadstar.com-美国.md](A/SB-143-broadstar.com-美国.md) |
| SB-144 | bsdnetworks.com | 加拿大 | 品牌商/贴牌需求（OEM/ODM） | 已推送 16 次·未回复 | 55 | 已 | [SB-144-bsdnetworks.com-加拿大.md](A/SB-144-bsdnetworks.com-加拿大.md) |
| SB-160 | linx-com.com | 英国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 54 | 已 | [SB-160-linx-com.com-英国.md](A/SB-160-linx-com.com-英国.md) |
| SB-164 | unea-x.com | 日本 | IT/工业产品贸易商（日本，工业 switch 现国内货） | 已推送 2 次·未回复 | 54 | 已 | [SB-164-unea-x.com-日本.md](A/SB-164-unea-x.com-日本.md) |
| SB-167 | ONSIS ELEKTRONIK | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 53 | 已 | [SB-167-ONSIS ELEKTRONIK-土耳其.md](A/SB-167-ONSIS%20ELEKTRONIK-土耳其.md) |
| SB-173 | inaxsys.com | 加拿大 | 加拿大安防品牌商（交换机现由 HRUI 代工贴标 → Q-33 口径，OEM 采购） | 已推送 8 次·未回复 | 53 | 已 | [SB-173-inaxsys.com-加拿大.md](A/SB-173-inaxsys.com-加拿大.md) |
| SB-179 | CRISPY CREPES | 印度尼西亚 | 电信/ISP/网络运营 | 有回复·跟进中 | 52 | 已 | [SB-179-CRISPY CREPES-印度尼西亚.md](A/SB-179-CRISPY%20CREPES-印度尼西亚.md) |
| SB-183 | Onyx Technology Solutions Limited | 乌干达 | 系统集成/工程商 | 有回复·跟进中 | 52 | 已 | [SB-183-Onyx Technology Solutions Limited-乌干达.md](A/SB-183-Onyx%20Technology%20Solutions%20Limited-乌干达.md) |
| SB-189 | vintronsmartvision.com | 印度 | 印度 CCTV 制造商（自有 PoE 交换机线，OEM/SKD 采购） | 名单内·未触达 | 52 | 已 | [SB-189-vintronsmartvision.com-印度.md](A/SB-189-vintronsmartvision.com-印度.md) |
| SB-193 | Dema Vertriebs GmbH | 德国 | 经销/集成（类型待核） | 有回复·跟进中 | 51 | 已 | [SB-193-Dema Vertriebs GmbH-德国.md](A/SB-193-Dema%20Vertriebs%20GmbH-德国.md) |
| SB-205 | barox.de | 德国 | 视频网络交换机品牌商（德/瑞，自有 logo，OEM 采购） | 已推送 8 次·未回复 | 50 | 已 | [SB-205-barox.de-德国.md](A/SB-205-barox.de-德国.md) |
| SB-222 | （未具名） | 赞比亚 | 经销/集成（类型待核） | 有回复·跟进中 | 50 | 已 | [SB-222-（未具名）-赞比亚.md](A/SB-222-（未具名）-赞比亚.md) |
| SB-226 | HANCHANG Infotech CO.,LTD | 韩国 | 韩国网络品牌商（自有标商用 FS，现 Volktek） | 已推送 2 次·未回复 | 49 | 已 | [SB-226-HANCHANG Infotech CO.,LTD-韩国.md](A/SB-226-HANCHANG%20Infotech%20CO.,LTD-韩国.md) |
| SB-241 | gluszek.tomasz@gmail.com | 爱尔兰 | 经销/集成（类型待核） | 有回复·跟进中 | 49 | 已 | [SB-241-gluszek.tomasz@gmail.com-爱尔兰.md](A/SB-241-gluszek.tomasz@gmail.com-爱尔兰.md) |
| SB-243 | hfcl.com | 印度 | 印度上市电信制造集团（IO 自有标交换机，OEM 采购；有回复） | 已推送 1 次·未回复 | 49 | 已 | [SB-243-hfcl.com-印度.md](A/SB-243-hfcl.com-印度.md) |
| SB-246 | isnetworks.pl | 波兰 | 网络集成商兼产品销售（波兰） | 已推送 8 次·未回复 | 49 | 已 | [SB-246-isnetworks.pl-波兰.md](A/SB-246-isnetworks.pl-波兰.md) |
| SB-248 | nellyssecurity.com | 美国 | 安防集成/经销 | 已推送 9 次·未回复 | 49 | 已 | [SB-248-nellyssecurity.com-美国.md](A/SB-248-nellyssecurity.com-美国.md) |
| SB-256 | tvprzemyslowa.pl | 波兰 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 49 | 已 | [SB-256-tvprzemyslowa.pl-波兰.md](A/SB-256-tvprzemyslowa.pl-波兰.md) |
| SB-274 | fiberix.com.tr | 土耳其 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 48 | 已 | [SB-274-fiberix.com.tr-土耳其.md](A/SB-274-fiberix.com.tr-土耳其.md) |
| SB-306 | Digital systems | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 46 | 已 | [SB-306-Digital systems-印度.md](A/SB-306-Digital%20systems-印度.md) |
| SB-315 | stc-vietnam.com | 越南 | 分销商/经销商 | 有回复·跟进中 | 46 | 已 | [SB-315-stc-vietnam.com-越南.md](A/SB-315-stc-vietnam.com-越南.md) |
| SB-320 | 353311@mail.ru | 俄罗斯 | 经销/集成（类型待核） | 成交过·维护 | 45 | 已 | [SB-320-353311@mail.ru-俄罗斯.md](A/SB-320-353311@mail.ru-俄罗斯.md) |
| SB-325 | Hamed electronics LLC | 阿联酋 | 经销/集成（类型待核） | 成交过·维护 | 45 | 已 | [SB-325-Hamed electronics LLC-阿联酋.md](A/SB-325-Hamed%20electronics%20LLC-阿联酋.md) |
| SB-331 | retelem-dz.com | 阿尔及利亚 | 经销/集成（类型待核） | 有回复·跟进中 | 45 | 已 | [SB-331-retelem-dz.com-阿尔及利亚.md](A/SB-331-retelem-dz.com-阿尔及利亚.md) |
| SB-343 | Zekko Tech Private Limited | 印度 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 44 | 已 | [SB-343-Zekko Tech Private Limited-印度.md](A/SB-343-Zekko%20Tech%20Private%20Limited-印度.md) |
| SB-356 | infinicoreinc.com | 美国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 44 | 已 | [SB-356-infinicoreinc.com-美国.md](A/SB-356-infinicoreinc.com-美国.md) |
| SB-359 | larch-networks.com | 以色列 | 网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购） | 名单内·未触达 | 44 | 已 | [SB-359-larch-networks.com-以色列.md](A/SB-359-larch-networks.com-以色列.md) |
| SB-366 | th-it.com | 马来西亚 | IT 设备租赁商（马来西亚） | 名单内·未触达 | 44 | 已 | [SB-366-th-it.com-马来西亚.md](A/SB-366-th-it.com-马来西亚.md) |
| SB-373 | （未具名） | 尼日利亚 | 经销/集成（类型待核） | 有回复·跟进中 | 44 | 已 | [SB-373-（未具名）-尼日利亚.md](A/SB-373-（未具名）-尼日利亚.md) |
| SB-388 | fhguvenlik.com | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 43 | 已 | [SB-388-fhguvenlik.com-土耳其.md](A/SB-388-fhguvenlik.com-土耳其.md) |
| SB-389 | hiperonline.com | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 43 | 已 | [SB-389-hiperonline.com-土耳其.md](A/SB-389-hiperonline.com-土耳其.md) |
| SB-392 | makrosisas.com.tr | 土耳其 | 系统集成/工程商 | 名单内·未触达 | 43 | 已 | [SB-392-makrosisas.com.tr-土耳其.md](A/SB-392-makrosisas.com.tr-土耳其.md) |
| SB-441 | Metal Union | 波兰 | 经销/集成（类型待核） | 成交过·维护 | 41 | 已 | [SB-441-Metal Union-波兰.md](A/SB-441-Metal%20Union-波兰.md) |
| SB-450 | comtech.net.pk | 巴基斯坦 | 经销/集成（类型待核） | 有回复·跟进中 | 41 | 已 | [SB-450-comtech.net.pk-巴基斯坦.md](A/SB-450-comtech.net.pk-巴基斯坦.md) |
| SB-451 | e-saudi.net | 沙特阿拉伯 | IT/网络贸易商（沙特，有回复，业务待核） | 已推送 1 次·未回复 | 41 | 已 | [SB-451-e-saudi.net-沙特阿拉伯.md](A/SB-451-e-saudi.net-沙特阿拉伯.md) |
| SB-462 | Eter biometric technologies Srl | 意大利 | 门禁/消防系统集成商（意大利，bypass 需求） | 已推送 5 次·未回复 | 40 | 已 | [SB-462-Eter biometric technologies Srl-意大利.md](A/SB-462-Eter%20biometric%20technologies%20Srl-意大利.md) |
| SB-474 | casecomms.com | 英国 | 品牌商/贴牌需求（OEM/ODM） | 有回复·跟进中 | 40 | 已 | [SB-474-casecomms.com-英国.md](A/SB-474-casecomms.com-英国.md) |
| SB-497 | Cong Ty TNHH CONG NGHE QUANG LAM | 越南 | 品牌商/贴牌需求（OEM/ODM） | WhatsApp 已加·未回复 | 39 | 已 | [SB-497-Cong Ty TNHH CONG NGHE QUANG LAM-越南.md](A/SB-497-Cong%20Ty%20TNHH%20CONG%20NGHE%20QUANG%20LAM-越南.md) |
| SB-499 | b.medvedev11@mail.ru | 吉尔吉斯斯坦 | 经销/集成（类型待核） | 有回复·跟进中 | 39 | 已 | [SB-499-b.medvedev11@mail.ru-吉尔吉斯斯坦.md](A/SB-499-b.medvedev11@mail.ru-吉尔吉斯斯坦.md) |
| SB-510 | pongpanot.k@hotmail.com | 泰国 | 经销/集成（类型待核） | 有回复·跟进中 | 39 | 已 | [SB-510-pongpanot.k@hotmail.com-泰国.md](A/SB-510-pongpanot.k@hotmail.com-泰国.md) |
| SB-529 | dmsimfg.com | 美国 | 网络配件品牌商（美国，自有标 MC；官网待核） | 已推送 19 次·未回复 | 38 | 已 | [SB-529-dmsimfg.com-美国.md](A/SB-529-dmsimfg.com-美国.md) |
| SB-542 | lanopia.de | 德国 | 经销/集成（类型待核） | 已推送 8 次·未回复 | 38 | 已 | [SB-542-lanopia.de-德国.md](A/SB-542-lanopia.de-德国.md) |
| SB-583 | usman2c@hotmail.com | 巴基斯坦 | 经销/集成（类型待核） | 有回复·跟进中 | 37 | 已 | [SB-583-usman2c@hotmail.com-巴基斯坦.md](A/SB-583-usman2c@hotmail.com-巴基斯坦.md) |
| SB-599 | symanitron.ru | 俄罗斯 | 俄罗斯工业网络品牌/合同制造（自有 logo，OEM 采购） | 已推送 18 次·未回复 | 36 | 已 | [SB-599-symanitron.ru-俄罗斯.md](A/SB-599-symanitron.ru-俄罗斯.md) |
| SB-641 | apolloinfoways.in | 印度 | 印度网络品牌商（自有 WatchDog 型号，中国 ODM 采购） | 名单内·未触达 | 34 | 已 | [SB-641-apolloinfoways.in-印度.md](A/SB-641-apolloinfoways.in-印度.md) |
| SB-692 | Anda Telecom | 印度 | 电信/ISP/网络运营 | WhatsApp 已加·未回复 | 33 | 已 | [SB-692-Anda Telecom-印度.md](A/SB-692-Anda%20Telecom-印度.md) |
| SB-696 | aironix.co.il | 以色列 | 工业网络分销商（以色列，ORing 在供） | 已推送 8 次·未回复 | 33 | 已 | [SB-696-aironix.co.il-以色列.md](A/SB-696-aironix.co.il-以色列.md) |
| SB-728 | Fast-Track Systems & Services Pte Ltd | 新加坡 | 经销/集成（类型待核） | 成交过·维护 | 32 | 已 | [SB-728-Fast-Track Systems & Services Pte Ltd-新加坡.md](A/SB-728-Fast-Track%20Systems%20&%20Services%20Pte%20Ltd-新加坡.md) |
| SB-737 | UGUR IMRE | 土耳其 | 品牌商/贴牌需求（OEM/ODM） | 名单内·未触达 | 32 | 已 | [SB-737-UGUR IMRE-土耳其.md](A/SB-737-UGUR%20IMRE-土耳其.md) |
| SB-767 | itmsystems.co.uk | 英国 | 安防/IT 集成商（英国，有回复，工业 FS 现 Utepo） | 已推送 16 次·未回复 | 32 | 已 | [SB-767-itmsystems.co.uk-英国.md](A/SB-767-itmsystems.co.uk-英国.md) |
| SB-826 | versitron.com | 美国 | 经销/集成（类型待核） | 名单内·未触达 | 31 | 已 | [SB-826-versitron.com-美国.md](A/SB-826-versitron.com-美国.md) |
| SB-827 | GOIP Global Services Pvt Ltd | 印度 | 品牌商/贴牌需求（OEM/ODM） | WhatsApp 已加·未回复 | 30 | 已 | [SB-827-GOIP Global Services Pvt Ltd-印度.md](A/SB-827-GOIP%20Global%20Services%20Pvt%20Ltd-印度.md) |
| SB-831 | actelis.com | 美国 | 经销/集成（类型待核） | 有回复·跟进中 | 30 | 已 | [SB-831-actelis.com-美国.md](A/SB-831-actelis.com-美国.md) |
| SB-869 | futurist.com.pk | 巴基斯坦 | 经销/集成（类型待核） | 有回复·跟进中 | 29 | 已 | [SB-869-futurist.com.pk-巴基斯坦.md](A/SB-869-futurist.com.pk-巴基斯坦.md) |
| SB-872 | israr_awan@hotmail.com | 巴基斯坦 | 经销/集成（类型待核） | 有回复·跟进中 | 29 | 已 | [SB-872-israr_awan@hotmail.com-巴基斯坦.md](A/SB-872-israr_awan@hotmail.com-巴基斯坦.md) |
| SB-905 | TELTRONIX \| BRITICOM | 英国 | 品牌商/贴牌需求（OEM/ODM） | 有回复·跟进中 | 28 | 已 | [SB-905-TELTRONIX BRITICOM-英国.md](A/SB-905-TELTRONIX%20BRITICOM-英国.md) |
| SB-910 | etictelecom.com | 法国 | 经销/集成（类型待核） | 有回复·跟进中 | 28 | 已 | [SB-910-etictelecom.com-法国.md](A/SB-910-etictelecom.com-法国.md) |
| SB-933 | airlive.com | 台湾 | 台湾品牌商（按「台湾厂商口径」只谈 OEM/ODM） | 已推送 19 次·未回复 | 27 | 已 | [SB-933-airlive.com-台湾.md](A/SB-933-airlive.com-台湾.md) |
| SB-949 | ksm.com.au | 澳大利亚 | 工业网络经销商（澳大利亚，国内货源在供） | 已推送 22 次·未回复 | 27 | 已 | [SB-949-ksm.com.au-澳大利亚.md](A/SB-949-ksm.com.au-澳大利亚.md) |
| SB-970 | EION Inc | 加拿大 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 26 | 已 | [SB-970-EION Inc-加拿大.md](A/SB-970-EION%20Inc-加拿大.md) |
| SB-976 | dauren.boltaev@mail.ru | 乌兹别克斯坦 | 分销商/经销商 | 成交过·维护 | 26 | 已 | [SB-976-dauren.boltaev@mail.ru-乌兹别克斯坦.md](A/SB-976-dauren.boltaev@mail.ru-乌兹别克斯坦.md) |
| SB-988 | Infinity Hardware | 美国 | 分销商/经销商 | WhatsApp 已加·未回复 | 25 | 已 | [SB-988-Infinity Hardware-美国.md](A/SB-988-Infinity%20Hardware-美国.md) |

### B 级（1229）— `Saga Clients/B/`（子目录 `SB-0001-0500/` / `SB-0501-1000/` / `SB-1001-1500/` / `SB-1501-2000/` / `SB-2001-2500/` / `SB-2501-3000/` / `SB-3001-3500/`）

全部 1229 个档案见 `Saga Clients/B/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

### C 级（3249）— `Saga Clients/C/`（子目录 `SC-0001-0500/` / `SC-0501-1000/` / `SC-1001-1500/` / `SC-1501-2000/` / `SC-2001-2500/` / `SC-2501-3000/` / `SC-3001-3500/`）

全部 3249 个档案见 `Saga Clients/C/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

