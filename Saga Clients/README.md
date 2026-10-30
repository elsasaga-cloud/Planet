# Saga Clients — Saga 历史客户全量档案（A / B / C）

> 生成：2026-10-30　|　来源：`Clients/`（Simon 上传到 main 的 137 个文件：6,246 行线索 + 20,819 条跟进记录）　|　归并后 **4647 个客户**：A 158 / B 1311 / C 3178
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
| 北美 | 22 | 174 | 289 | 485 |
| 欧洲 | 33 | 442 | 522 | 997 |
| 土耳其 | 16 | 119 | 72 | 207 |
| 中东 | 13 | 67 | 246 | 326 |
| 亚太 | 23 | 233 | 696 | 952 |
| 俄语区 | 12 | 94 | 398 | 504 |
| 南亚 | 24 | 90 | 346 | 460 |
| 拉美 | 7 | 31 | 212 | 250 |
| 非洲 | 8 | 59 | 274 | 341 |
| 乌克兰 | 0 | 0 | 55 | 55 |
| 中国大陆 | 0 | 0 | 17 | 17 |
| 未知 | 0 | 2 | 51 | 53 |
| **合计** | 158 | 1311 | 3178 | 4647 |

状态分布：名单内 2011；已推送 1239；WhatsApp 526；用户判定不行 444；有回复 229；发不过去 83；历史合作 80；成交过 20；回复暂无需求 15

C 级细分：群发冷名单无回应 1025；用户判定不行/不相关 485；综合分低 359；品类不符（VC/DWDM/CCTV 等） 327；无联系方式 145；低价值区域冷线索 123；陈旧线索无互动 112；发不过去 101；无邮箱（仅电话） 72；守界：乌克兰 53；体量过大/品牌厂商/运营商 48；用户备注不再跟进/Spam 40；调研后定级 C 37；储备·复核打回 29；品类不符/终端用户 17；体量过大 17；品类不符 16；中国大陆（非出口客户） 16；个人买家 10；同行/台湾厂商 8；渠道冲突（Q-33 8；守界：军工 6；品类不符（软件） 6；巨头/集团 4；同行/厂商 4；区域外/品类不符 4；品类不符（非网络设备） 4；区域外/个人买家 4；中国厂商海外办事处 3；同行/自研 3；运营商 3；品类不符/非渠道 3；无邮箱 3；区域外/伊朗制裁合规风险 2；同行/贸易商 2；厂商办事处/同行 2；品类不符（板级/芯片） 2；专营品牌无切入点 2；守界（军工） 2；守界（公共部门） 2；体量过大/集团自有线 2；厂商/上市（非渠道） 2；体量过大/守界 2；品类不符（工程服务） 2；厂商/集团品牌（非渠道） 2；厂商/台湾（非渠道） 2；巨头/台湾厂商 2；运营商/体量过大 2；非渠道（工程服务） 2；储备·守界 1；明确退订 1；已停业 1；守界（轨道） 1；守界（公共部门/关键基础设施） 1；同行/国内厂商海外站 1；守界（军警/公共安全） 1；陈旧询盘 1；品类不符（防爆认证） 1；运营商/品类不符 1；品类不符（软件/信息服务） 1；品类不符/陈旧线索 1；体量过大/品牌厂商 1；上市集团/体量过大 1；同行/自研厂商 1；陈旧询盘/个人买家 1；守界（军工）/体量过大 1；品类不符（线缆集团） 1；品类不符（无源） 1；巨头/运营商 1；体量过大/品类不符（板级） 1；守界（军工/政府） 1；品类不符（品牌二手经纪） 1；守界：轨道/车载 1；守界（车载/轨道） 1；守界：轨道 1；个人买家/品类不符 1；厂商办事处/台湾厂商 1；同行/区域外 1；品类不符（消费级）/中国大陆背景 1；巨头/集团（同行） 1；巨头/上市（非渠道） 1；巨头/厂商 1；品类不符（轨道/车载） 1；区域外/终端用户 1；中介/品类不符 1；同行/专营俄产 1；厂商品牌/政府客户（俄区） 1；守界：政府客户（俄区） 1；板级/非渠道 1；区域外/同行 1；巨头/消费级 1；品类不符（板级嵌入式） 1；陈旧询盘/品类不符 1；守界（军工/国防） 1；巨头/区外（误并待拆） 1；巨头/上市 1；品类不符（软件/工程服务） 1；非渠道（服务商） 1；厂商/品类不符（PON） 1；品类不符（板级/芯片）/守界 1

## 调研覆盖（A 候选逐家网页核实）

- 自动评级曾为 A 的候选 **全部** 做了网页核实：1756 家（`data/saga_clients/research/`，每家含引文 + URL + 日期）；维持 A 880 / 调研后降 B 438 / 调研后降 C 280。
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

### A 级（158）— `Saga Clients/A/`

| 编号 | 公司 | 国家 | 类型 | 状态 | 分数 | 调研 | 档案 |
|---|---|---|---|---|---|---|---|
| SA-001 | asteldigicom.com | 阿联酋 | 分销商/网店（线缆·网络·太阳能） | 成交过·可发展（Simon） | 164 | 已 | [SA-001-asteldigicom.com-阿联酋.md](A/SA-001-asteldigicom.com-阿联酋.md) |
| SA-002 | simrex.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机 | 有回复·跟进中 | 88 | 已 | [SA-002-simrex.com-美国.md](A/SA-002-simrex.com-美国.md) |
| SA-003 | Eyescan security Systems | 塞浦路斯 | 安防集成/经销（兼分销） | 历史合作·维护（非 Saga 成单） | 133 | 已 | [SA-003-Eyescan security Systems-塞浦路斯.md](A/SA-003-Eyescan%20security%20Systems-塞浦路斯.md) |
| SA-004 | Boecek Sec | 德国 | 安防集成/经销（据用户备注推断） | 历史合作·维护（非 Saga 成单） | 131 | 已 | [SA-004-Boecek Sec-德国.md](A/SA-004-Boecek%20Sec-德国.md) |
| SA-006 | Vi-Link（vilinknet.com） | 美国 | 品牌商/贴牌需求（OEM/ODM）——光传输+工业以太网自有品牌 | 成交过·可发展（Simon） | 150 | 已 | [SA-006-Vi-Link（vilinknet.com）-美国.md](A/SA-006-Vi-Link（vilinknet.com）-美国.md) |
| SA-007 | gogreenit.net | 英国 | IT 服务商/终端（非渠道） | 成交过·可发展（Simon） | 116 | 已 | [SA-007-gogreenit.net-英国.md](A/SA-007-gogreenit.net-英国.md) |
| SA-008 | fiberone.de | 德国 | 运营商/ISP（终端 + 自有 logo 贴牌需求） | 成交过·活跃（Simon） | 112 | 已 | [SA-008-fiberone.de-德国.md](A/SA-008-fiberone.de-德国.md) |
| SA-009 | coptek.com.tr | 土耳其 | 分销商（网络设备，DCN 土耳其分销） | 历史合作·维护（非 Saga 成单） | 110 | 已 | [SA-009-coptek.com.tr-土耳其.md](A/SA-009-coptek.com.tr-土耳其.md) |
| SA-010 | NEXTU EZ-NET | 韩国 | 品牌商/分销商（自有品牌 NEXTU，OEM 采购） | 有回复·跟进中 | 103 | 已 | [SA-010-NEXTU EZ-NET-韩国.md](A/SA-010-NEXTU%20EZ-NET-韩国.md) |
| SA-011 | CXR | 法国 | 品牌商/贴牌需求（OEM/ODM）——工业网络设备自有品牌 | 有回复·跟进中 | 100 | 已 | [SA-011-CXR-法国.md](A/SA-011-CXR-法国.md) |
| SA-012 | widen.co.th | 泰国 | 分销商/品牌商（光纤产品自有 logo，OEM 采购） | 历史合作·维护（非 Saga 成单） | 97 | 已 | [SA-012-widen.co.th-泰国.md](A/SA-012-widen.co.th-泰国.md) |
| SA-014 | impulsecctv.com | 新加坡 | 品牌商/贴牌需求（OEM/ODM）——安防品牌自有 PoE 交换机线 | 有回复·跟进中 | 94 | 已 | [SA-014-impulsecctv.com-新加坡.md](A/SA-014-impulsecctv.com-新加坡.md) |
| SA-015 | megnet.co.uk | 英国 | 分销商 + 自有品牌（Chimera，OEM 采购） | 有回复·跟进中 | 94 | 已 | [SA-015-megnet.co.uk-英国.md](A/SA-015-megnet.co.uk-英国.md) |
| SA-016 | BitBook LLC | 俄罗斯 | 分销商 + 自有品牌（条码为主，网络 PoE 为辅） | 成交过·可发展（Simon） | 90 | 已 | [SA-016-BitBook LLC-俄罗斯.md](A/SA-016-BitBook%20LLC-俄罗斯.md) |
| SA-020 | bitstream.pl | 波兰 | 品牌商/制造商（工业网络自有品牌；MC/SFP/部分交换机可能外采贴牌） | 有回复·跟进中 | 88 | 已 | [SA-020-bitstream.pl-波兰.md](A/SA-020-bitstream.pl-波兰.md) |
| SA-021 | optiviewusa.com | 美国 | 分销商/品牌商（CCTV 批发，自有品牌 OEM 采购） | 有回复·跟进中 | 88 | 已 | [SA-021-optiviewusa.com-美国.md](A/SA-021-optiviewusa.com-美国.md) |
| SA-023 | fcnet.pl | 波兰 | 分销商/进口商（自有 logo 采购） | 有回复·跟进中 | 85 | 已 | [SA-023-fcnet.pl-波兰.md](A/SA-023-fcnet.pl-波兰.md) |
| SA-026 | hardenednetworks.com | 美国 | 品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌 | 有回复·跟进中 | 84 | 已 | [SA-026-hardenednetworks.com-美国.md](A/SA-026-hardenednetworks.com-美国.md) |
| SA-027 | Al Salami Trading L.L.C | 阿联酋 | 安防集成商（项目型小批量） | 有回复·跟进中 | 83 | 已 | [SA-027-Al Salami Trading L.L.C-阿联酋.md](A/SA-027-Al%20Salami%20Trading%20L.L.C-阿联酋.md) |
| SA-028 | entasource.co.th | 泰国 | 进口分销商（自有 logo） | 有回复·跟进中 | 83 | 已 | [SA-028-entasource.co.th-泰国.md](A/SA-028-entasource.co.th-泰国.md) |
| SA-029 | gtwave.co.kr | 韩国 | 品牌商（OEM/ODM 需求） | 有回复·跟进中 | 83 | 已 | [SA-029-gtwave.co.kr-韩国.md](A/SA-029-gtwave.co.kr-韩国.md) |
| SA-030 | snexus.com.tr | 土耳其 | 品牌商/经销（自有品牌白牌采购） | 已推送 2 次·未回复 | 83 | 已 | [SA-030-snexus.com.tr-土耳其.md](A/SA-030-snexus.com.tr-土耳其.md) |
| SA-031 | Truong Son Solutions | 越南 | 分销商/电商（工业交换机垂直） | 有回复·跟进中 | 67 | 已 | [SA-031-Truong Son Solutions-越南.md](A/SA-031-Truong%20Son%20Solutions-越南.md) |
| SA-032 | sundartechno.com | 印度 | 方案商/自有品牌贴牌（成交客户） | 成交过·可发展（Simon） | 82 | 已 | [SA-032-sundartechno.com-印度.md](A/SA-032-sundartechno.com-印度.md) |
| SA-033 | bluewarrior.com | 美国 | 品牌商（白牌贴牌，OEM 目标） | 有回复·跟进中 | 81 | 已 | [SA-033-bluewarrior.com-美国.md](A/SA-033-bluewarrior.com-美国.md) |
| SA-035 | td-fe.com | 俄罗斯 | 品牌商/贸易公司（电源主业，工业交换机为配套） | 有回复·跟进中 | 81 | 已 | [SA-035-td-fe.com-俄罗斯.md](A/SA-035-td-fe.com-俄罗斯.md) |
| SA-039 | mt-link.com | 巴基斯坦 | 品牌商（中国白牌贴牌，ODM 买家） | 有回复·跟进中 | 79 | 已 | [SA-039-mt-link.com-巴基斯坦.md](A/SA-039-mt-link.com-巴基斯坦.md) |
| SA-042 | antronix.com | 美国 | 品牌制造商（拓展以太网交换机产品线，OEM 目标） | 有回复·跟进中 | 76 | 已 | [SA-042-antronix.com-美国.md](A/SA-042-antronix.com-美国.md) |
| SA-043 | direktronik.se | 瑞典 | 分销商/进口商（自有品牌 + 多品牌） | 有回复·跟进中 | 76 | 已 | [SA-043-direktronik.se-瑞典.md](A/SA-043-direktronik.se-瑞典.md) |
| SA-045 | energyplusystems.cl | 智利 | 工业/矿业集成供应商（工业交换机为配套品类） | 有回复·跟进中 | 76 | 已 | [SA-045-energyplusystems.cl-智利.md](A/SA-045-energyplusystems.cl-智利.md) |
| SA-047 | sge.com.tr | 土耳其 | 工程分销商/集成（能源自动化；工业交换机转售） | 有回复·跟进中 | 76 | 已 | [SA-047-sge.com.tr-土耳其.md](A/SA-047-sge.com.tr-土耳其.md) |
| SA-048 | ekhalas.com | 沙特阿拉伯 | 系统集成商+电商分销 | 有回复·跟进中 | 75 | 已 | [SA-048-ekhalas.com-沙特阿拉伯.md](A/SA-048-ekhalas.com-沙特阿拉伯.md) |
| SA-049 | iotsistem.com | 土耳其 | 工业/IoT 分销商（网店） | 已推送 2 次·未回复 | 75 | 已 | [SA-049-iotsistem.com-土耳其.md](A/SA-049-iotsistem.com-土耳其.md) |
| SA-050 | impakt.com.pl | 波兰 | 品牌商（自有品牌 OEM 采购）+ 分销商 | 有回复·跟进中 | 74 | 已 | [SA-050-impakt.com.pl-波兰.md](A/SA-050-impakt.com.pl-波兰.md) |
| SA-051 | Tecpro Solutions | 阿联酋 | 系统集成商（IT/ELV） | 有回复·跟进中 | 73 | 已 | [SA-051-Tecpro Solutions-阿联酋.md](A/SA-051-Tecpro%20Solutions-阿联酋.md) |
| SA-054 | softnetworks.net | 美国 | 二手/翻新网络设备经销商 | 有回复·跟进中 | 73 | 已 | [SA-054-softnetworks.net-美国.md](A/SA-054-softnetworks.net-美国.md) |
| SA-055 | NOVA Group Engineering Project Electronic Co LTD | 土耳其 | 进口批发商/分销商（弱电安防） | 已推送 4 次·未回复 | 72 | 已 | [SA-055-NOVA Group Engineering Project Electroni-土耳其.md](A/SA-055-NOVA%20Group%20Engineering%20Project%20Electroni-土耳其.md) |
| SA-059 | data-connect.com | 美国 | 品牌商（自有品牌）+ 分销 | 有回复·跟进中 | 70 | 已 | [SA-059-data-connect.com-美国.md](A/SA-059-data-connect.com-美国.md) |
| SA-060 | gofiberx.com | 美国 | ISP/运营商（终端用户） | 有回复·跟进中 | 70 | 已 | [SA-060-gofiberx.com-美国.md](A/SA-060-gofiberx.com-美国.md) |
| SA-061 | RYMTECH EAS | 巴拉圭 | 系统集成/工程商 | 有回复·跟进中 | 69 | 已 | [SA-061-RYMTECH EAS-巴拉圭.md](A/SA-061-RYMTECH%20EAS-巴拉圭.md) |
| SA-063 | Areca Embedded Systems Pvt Ltd | 印度 | 系统集成/设备商 | 有回复·跟进中 | 67 | 已 | [SA-063-Areca Embedded Systems Pvt Ltd-印度.md](A/SA-063-Areca%20Embedded%20Systems%20Pvt%20Ltd-印度.md) |
| SA-064 | optat.ru | 俄罗斯 | 招投标供货商/贸易商 | 有回复·跟进中 | 67 | 已 | [SA-064-optat.ru-俄罗斯.md](A/SA-064-optat.ru-俄罗斯.md) |
| SA-066 | ccs-msk.ru | 俄罗斯 | 分销商（企业网络 + 工业以太网） | 有回复·跟进中 | 65 | 已 | [SA-066-ccs-msk.ru-俄罗斯.md](A/SA-066-ccs-msk.ru-俄罗斯.md) |
| SA-067 | Latmedia Group, LLC | 乌兹别克斯坦 | IT 集成/贸易商 | 名单内·未触达 | 63 | 已 | [SA-067-Latmedia Group, LLC-乌兹别克斯坦.md](A/SA-067-Latmedia%20Group,%20LLC-乌兹别克斯坦.md) |
| SA-070 | Top Italia | 意大利 | 经销/集成商 | 已推送 14 次·未回复 | 61 | 已 | [SA-070-Top Italia-意大利.md](A/SA-070-Top%20Italia-意大利.md) |
| SA-071 | surlink-tech.com | 玻利维亚 | 批发分销商（布线/光纤/网络） | 有回复·跟进中 | 61 | 已 | [SA-071-surlink-tech.com-玻利维亚.md](A/SA-071-surlink-tech.com-玻利维亚.md) |
| SA-072 | trans audio video group | 意大利 | AV/安防集成商 | 已推送 14 次·未回复 | 61 | 已 | [SA-072-trans audio video group-意大利.md](A/SA-072-trans%20audio%20video%20group-意大利.md) |
| SA-074 | Elite Team Security Ltd | 保加利亚 | 安保服务商 + 视频监控集成（终端用户/集成商） | 回复暂无需求 | 60 | 已 | [SA-074-Elite Team Security Ltd-保加利亚.md](A/SA-074-Elite%20Team%20Security%20Ltd-保加利亚.md) |
| SA-076 | Telemobil | 土耳其 | IT/网络系统集成商 | WhatsApp 已加·未回复 | 60 | 已 | [SA-076-Telemobil-土耳其.md](A/SA-076-Telemobil-土耳其.md) |
| SA-077 | Angora Networks | 土耳其 | 系统集成商 + 自有品牌贴牌（OEM）——公共部门/运营商投标型 | 成交过·活跃（Simon） | 108 | 已 | [SA-077-Angora Networks-土耳其.md](A/SA-077-Angora%20Networks-土耳其.md) |
| SA-078 | James Clendenan Systems Ltd. | 加拿大 | 系统集成/工程（北温哥华） | 成交过·活跃（Simon） | 98 | 已 | [SA-078-James Clendenan Systems Ltd-加拿大.md](A/SA-078-James%20Clendenan%20Systems%20Ltd-加拿大.md) |
| SA-079 | Biz-Ethics Ltd.（BEL Networks） | 尼日利亚 | 网络设备经销/自有品牌 BNSC-（拉各斯） | 成交过·活跃（Simon） | 84 | 已 | [SA-079-Biz-Ethics Ltd.（BEL Networks）-尼日利亚.md](A/SA-079-Biz-Ethics%20Ltd.（BEL%20Networks）-尼日利亚.md) |
| SA-080 | PBA Forever Technology Co., Ltd. | 泰国 | 系统集成/工程 | 成交过·活跃（Simon） | 66 | 已 | [SA-080-PBA Forever Technology Co., Ltd-泰国.md](A/SA-080-PBA%20Forever%20Technology%20Co.,%20Ltd-泰国.md) |
| SA-082 | ISIMKO GmbH,Guhrower Straße | 德国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 54 | 已 | [SA-082-ISIMKO GmbH,Guhrower Straße-德国.md](A/SA-082-ISIMKO%20GmbH,Guhrower%20Straße-德国.md) |
| SA-085 | HCS | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 43 | 已 | [SA-085-HCS-土耳其.md](A/SA-085-HCS-土耳其.md) |
| SA-086 | netas.com.tr | 土耳其 | 经销/集成（类型待核） | 成交过·活跃（Simon） | 90 | 已 | [SA-086-netas.com.tr-土耳其.md](A/SA-086-netas.com.tr-土耳其.md) |
| SA-090 | WizardsInc Sdn Bhd | 马来西亚 | 经销/集成（类型待核） | 成交过·可发展（Simon） | 62 | 已 | [SA-090-WizardsInc Sdn Bhd-马来西亚.md](A/SA-090-WizardsInc%20Sdn%20Bhd-马来西亚.md) |
| SB-001 | resonantnetworks.com | 新加坡 | 系统集成/工程商（数据中心·光网络） | 成交过·已凉（Simon: gg） | 130 | 已 | [SB-001-resonantnetworks.com-新加坡.md](A/SB-001-resonantnetworks.com-新加坡.md) |
| SB-002 | Xspec Technology Sdn Bhd | 马来西亚 | 分销商/制造商代表（NDT·国防安防·医疗） | 成交过·已凉（Simon: gg） | 123 | 已 | [SB-002-Xspec Technology Sdn Bhd-马来西亚.md](A/SB-002-Xspec%20Technology%20Sdn%20Bhd-马来西亚.md) |
| SB-003 | Rio-Import LLC（ООО «РИО-ИМПОРТ»） | 俄罗斯 | 分销商/经销商（工业自动化） | 成交过·已凉（Simon: gg） | 128 | 已 | [SB-003-Rio-Import LLC（ООО «РИО-ИМПОРТ»）-俄罗斯.md](A/SB-003-Rio-Import%20LLC（ООО%20«РИО-ИМПОРТ»）-俄罗斯.md) |
| SB-006 | unitedcontrolengg.com | 印度 | 分销商 + 系统集成（工业自动化） | 成交过·已凉（Simon: gg） | 107 | 已 | [SB-006-unitedcontrolengg.com-印度.md](A/SB-006-unitedcontrolengg.com-印度.md) |
| SB-020 | 52networks.com | 美国 | 经销商（政府/商业小单，已成交） | 成交过·已凉（Simon: gg） | 77 | 已 | [SB-020-52networks.com-美国.md](A/SB-020-52networks.com-美国.md) |
| SB-031 | OM Telecom S.R.L. | 秘鲁 | 电信设备经销商 | 有回复·跟进中 | 69 | 已 | [SB-031-OM Telecom S.R.L-秘鲁.md](A/SB-031-OM%20Telecom%20S.R.L-秘鲁.md) |
| SB-038 | tricomp.com.pl | 波兰 | IT/电信工程与咨询公司 | 有回复·跟进中 | 68 | 已 | [SB-038-tricomp.com.pl-波兰.md](A/SB-038-tricomp.com.pl-波兰.md) |
| SB-043 | Euro Technology | 阿联酋 | 安防系统集成商 | 有回复·跟进中 | 65 | 已 | [SB-043-Euro Technology-阿联酋.md](A/SB-043-Euro%20Technology-阿联酋.md) |
| SB-047 | topica.mn | 蒙古国 | 贸易商 | 有回复·跟进中 | 65 | 已 | [SB-047-topica.mn-蒙古国.md](A/SB-047-topica.mn-蒙古国.md) |
| SB-053 | onnettechnologies.com | 阿联酋 | IT 贸易商 | 有回复·跟进中 | 63 | 已 | [SB-053-onnettechnologies.com-阿联酋.md](A/SB-053-onnettechnologies.com-阿联酋.md) |
| SB-056 | Net Work Business Solutions | 爱沙尼亚 | IT/网络服务商 | 有回复·跟进中 | 62 | 已 | [SB-056-Net Work Business Solutions-爱沙尼亚.md](A/SB-056-Net%20Work%20Business%20Solutions-爱沙尼亚.md) |
| SB-057 | Rfcom | 希腊 | 经销/集成商 | 有回复·跟进中 | 62 | 已 | [SB-057-Rfcom-希腊.md](A/SB-057-Rfcom-希腊.md) |
| SB-059 | avanca.com.sg | 新加坡 | 工业产品经销商 | 有回复·跟进中 | 62 | 已 | [SB-059-avanca.com.sg-新加坡.md](A/SB-059-avanca.com.sg-新加坡.md) |
| SB-071 | nkstech.net | 菲律宾 | 经销/集成商 | 历史合作·维护（非 Saga 成单） | 61 | 已 | [SB-071-nkstech.net-菲律宾.md](A/SB-071-nkstech.net-菲律宾.md) |
| SB-074 | Bilge SECURITY SYSTEMS | 土耳其 | 安防安装/经销商 | WhatsApp 已加·未回复 | 60 | 已 | [SB-074-Bilge SECURITY SYSTEMS-土耳其.md](A/SB-074-Bilge%20SECURITY%20SYSTEMS-土耳其.md) |
| SB-077 | Liveye | 德国 | 安防产品商 | WhatsApp 已加·未回复 | 60 | 已 | [SB-077-Liveye-德国.md](A/SB-077-Liveye-德国.md) |
| SB-093 | konakguvenlik.com.tr | 土耳其 | 安防电商（土耳其，HRUI/丰润达在售 → Q-33 口径） | 已推送 2 次·未回复 | 63 | 已 | [SB-093-konakguvenlik.com.tr-土耳其.md](A/SB-093-konakguvenlik.com.tr-土耳其.md) |
| SB-1026 | epygi.com | 美国 | IP PBX 厂商（美国，配套交换机 OEM 采购） | 名单内·未触达 | 25 | 已 | [SB-1026-epygi.com-美国.md](A/SB-1026-epygi.com-美国.md) |
| SB-103 | Grundig | 德国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 59 | 已 | [SB-103-Grundig-德国.md](A/SB-103-Grundig-德国.md) |
| SB-104 | STS Italia S.r.l. | 意大利 | 经销/集成（类型待核） | 有回复·跟进中 | 59 | 已 | [SB-104-STS Italia S.r.l-意大利.md](A/SB-104-STS%20Italia%20S.r.l-意大利.md) |
| SB-109 | ite.net.pk | 巴基斯坦 | 经销/集成（类型待核） | 有回复·跟进中 | 59 | 已 | [SB-109-ite.net.pk-巴基斯坦.md](A/SB-109-ite.net.pk-巴基斯坦.md) |
| SB-110 | itkati.com | 乌干达 | 经销/集成（类型待核） | 有回复·跟进中 | 59 | 已 | [SB-110-itkati.com-乌干达.md](A/SB-110-itkati.com-乌干达.md) |
| SB-1102 | vienthonggiatot.com | 越南 | 经销/集成（类型待核） | 有回复·跟进中 | 21 | 已 | [SB-1102-vienthonggiatot.com-越南.md](A/SB-1102-vienthonggiatot.com-越南.md) |
| SB-111 | nivoxtech.com | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 59 | 已 | [SB-111-nivoxtech.com-印度.md](A/SB-111-nivoxtech.com-印度.md) |
| SB-1113 | Fastball | 印度 | 经销/贸易（德里） | 成交过·已凉（Simon: gg） | 77 | 已 | [SB-1113-Fastball-印度.md](A/SB-1113-Fastball-印度.md) |
| SB-1115 | Milliseconds Evolution Limited | 英国 | 网络集成/MikroTik 顾问（拟经销） | 名单内·未触达 | 46 | 已 | [SB-1115-Milliseconds Evolution Limited-英国.md](A/SB-1115-Milliseconds%20Evolution%20Limited-英国.md) |
| SB-1116 | Litech (Pvt) Ltd | 巴基斯坦 | 系统集成/项目承包（华为渠道） | 名单内·未触达 | 31 | 已 | [SB-1116-Litech (Pvt) Ltd-巴基斯坦.md](A/SB-1116-Litech%20(Pvt)%20Ltd-巴基斯坦.md) |
| SB-1120 | Obmac systems 可以推一下 | 赞比亚 | 系统集成/工程商 | 成交过·已凉（Simon: gg） | 18 | 已 | [SB-1120-Obmac systems 可以推一下-赞比亚.md](A/SB-1120-Obmac%20systems%20可以推一下-赞比亚.md) |
| SB-1122 | comtinu.ru | 俄罗斯 | 俄罗斯网络项目商（25G/100G 项目） | 名单内·未触达 | 17 | 已 | [SB-1122-comtinu.ru-俄罗斯.md](A/SB-1122-comtinu.ru-俄罗斯.md) |
| SB-1132 | nedic.aleksandar@gmail.com | 塞尔维亚 | 塞尔维亚小型集成/经销（拓展网络业务） | 已推送 14 次·未回复 | 8 | 已 | [SB-1132-nedic.aleksandar@gmail.com-塞尔维亚.md](A/SB-1132-nedic.aleksandar@gmail.com-塞尔维亚.md) |
| SB-1134 | conexionderedes.com | 萨尔瓦多 | 中美洲网络集成/分销商（为其客户转发方案） | 已推送 13 次·未回复 | 7 | 已 | [SB-1134-conexionderedes.com-萨尔瓦多.md](A/SB-1134-conexionderedes.com-萨尔瓦多.md) |
| SB-1135 | raisecom.su | 俄罗斯 | 俄罗斯经销/项目商（Raisecom 代理） | 历史合作·维护（非 Saga 成单） | 5 | 已 | [SB-1135-raisecom.su-俄罗斯.md](A/SB-1135-raisecom.su-俄罗斯.md) |
| SB-1136 | fiberoptics4sale.com | 美国 | 线上零售/分销（光纤配件多品牌） | 已推送 8 次·未回复 | 2 | 已 | [SB-1136-fiberoptics4sale.com-美国.md](A/SB-1136-fiberoptics4sale.com-美国.md) |
| SB-1137 | Infotec Comercio de Equipamentos e Sistemas de Segurança Ltda. | 巴西 | 巴西安防设备经销（CCTV） | 名单内·未触达 | -2 | 已 | [SB-1137-Infotec Comercio de Equipamentos e Siste-巴西.md](A/SB-1137-Infotec%20Comercio%20de%20Equipamentos%20e%20Siste-巴西.md) |
| SB-1138 | devray.in | 印度 | 印度 Make-in-India OEM（自称 OEM for Switches / NGFW / SDWAN；ISO 27001 / CERT-In Empanelled） | 名单内·未触达 | -4 | 已 | [SB-1138-devray.in-印度.md](A/SB-1138-devray.in-印度.md) |
| SB-119 | wirestar.net | 美国 | 经销/集成（类型待核） | 有回复·跟进中 | 58 | 已 | [SB-119-wirestar.net-美国.md](A/SB-119-wirestar.net-美国.md) |
| SB-122 | Tera Technologies and Engineering Ltd | 坦桑尼亚 | 系统集成/工程商 | 有回复·跟进中 | 57 | 已 | [SB-122-Tera Technologies and Engineering Ltd-坦桑尼亚.md](A/SB-122-Tera%20Technologies%20and%20Engineering%20Ltd-坦桑尼亚.md) |
| SB-131 | DE secure | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 55 | 已 | [SB-131-DE secure-土耳其.md](A/SB-131-DE%20secure-土耳其.md) |
| SB-132 | F.A.S.T | 土耳其 | 工业自动化/IoT 方案商 | 名单内·未触达 | 55 | 已 | [SB-132-F.A.S.T-土耳其.md](A/SB-132-F.A.S.T-土耳其.md) |
| SB-143 | broadstar.com | 美国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 55 | 已 | [SB-143-broadstar.com-美国.md](A/SB-143-broadstar.com-美国.md) |
| SB-144 | bsdnetworks.com | 加拿大 | 品牌商/贴牌需求（OEM/ODM） | 已推送 16 次·未回复 | 55 | 已 | [SB-144-bsdnetworks.com-加拿大.md](A/SB-144-bsdnetworks.com-加拿大.md) |
| SB-160 | linx-com.com | 英国 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 54 | 已 | [SB-160-linx-com.com-英国.md](A/SB-160-linx-com.com-英国.md) |
| SB-163 | skeo.ru | 俄罗斯 | 经销/集成（类型待核） | 有回复·跟进中 | 54 | 已 | [SB-163-skeo.ru-俄罗斯.md](A/SB-163-skeo.ru-俄罗斯.md) |
| SB-164 | unea-x.com | 日本 | IT/工业产品贸易商（日本，工业 switch 现国内货） | 已推送 2 次·未回复 | 54 | 已 | [SB-164-unea-x.com-日本.md](A/SB-164-unea-x.com-日本.md) |
| SB-166 | Crown Security Solutions | 卡塔尔 | 分销商/经销商 | 有回复·跟进中 | 53 | 已 | [SB-166-Crown Security Solutions-卡塔尔.md](A/SB-166-Crown%20Security%20Solutions-卡塔尔.md) |
| SB-169 | agsplus.in | 印度 | 安防集成/经销 | 有回复·跟进中 | 53 | 已 | [SB-169-agsplus.in-印度.md](A/SB-169-agsplus.in-印度.md) |
| SB-173 | inaxsys.com | 加拿大 | 加拿大安防品牌商（交换机现由 HRUI 代工贴标 → Q-33 口径，OEM 采购） | 已推送 8 次·未回复 | 53 | 已 | [SB-173-inaxsys.com-加拿大.md](A/SB-173-inaxsys.com-加拿大.md) |
| SB-175 | mbtc.com.sa | 沙特阿拉伯 | 系统集成/工程商 | 回复暂无需求 | 53 | 已 | [SB-175-mbtc.com.sa-沙特阿拉伯.md](A/SB-175-mbtc.com.sa-沙特阿拉伯.md) |
| SB-183 | Onyx Technology Solutions Limited | 乌干达 | 系统集成/工程商 | 有回复·跟进中 | 52 | 已 | [SB-183-Onyx Technology Solutions Limited-乌干达.md](A/SB-183-Onyx%20Technology%20Solutions%20Limited-乌干达.md) |
| SB-189 | vintronsmartvision.com | 印度 | 印度 CCTV 制造商（自有 PoE 交换机线，OEM/SKD 采购） | 名单内·未触达 | 52 | 已 | [SB-189-vintronsmartvision.com-印度.md](A/SB-189-vintronsmartvision.com-印度.md) |
| SB-193 | Dema Vertriebs GmbH | 德国 | 经销/集成（类型待核） | 有回复·跟进中 | 51 | 已 | [SB-193-Dema Vertriebs GmbH-德国.md](A/SB-193-Dema%20Vertriebs%20GmbH-德国.md) |
| SB-201 | Elsi | 意大利 | 安防集成/经销 | 已推送 14 次·未回复 | 50 | 已 | [SB-201-Elsi-意大利.md](A/SB-201-Elsi-意大利.md) |
| SB-226 | HANCHANG Infotech CO.,LTD | 韩国 | 韩国网络品牌商（自有标商用 FS，现 Volktek） | 已推送 2 次·未回复 | 49 | 已 | [SB-226-HANCHANG Infotech CO.,LTD-韩国.md](A/SB-226-HANCHANG%20Infotech%20CO.,LTD-韩国.md) |
| SB-243 | hfcl.com | 印度 | 印度上市电信制造集团（IO 自有标交换机，OEM 采购；有回复） | 已推送 1 次·未回复 | 49 | 已 | [SB-243-hfcl.com-印度.md](A/SB-243-hfcl.com-印度.md) |
| SB-248 | nellyssecurity.com | 美国 | 安防集成/经销 | 已推送 9 次·未回复 | 49 | 已 | [SB-248-nellyssecurity.com-美国.md](A/SB-248-nellyssecurity.com-美国.md) |
| SB-255 | switchtek | 英国 | 分销商/经销商 | 已推送 17 次·未回复 | 49 | 已 | [SB-255-switchtek-英国.md](A/SB-255-switchtek-英国.md) |
| SB-267 | bio-cognitive.com | 新加坡 | 安防集成/经销 | 有回复·跟进中 | 48 | 已 | [SB-267-bio-cognitive.com-新加坡.md](A/SB-267-bio-cognitive.com-新加坡.md) |
| SB-274 | fiberix.com.tr | 土耳其 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 48 | 已 | [SB-274-fiberix.com.tr-土耳其.md](A/SB-274-fiberix.com.tr-土耳其.md) |
| SB-315 | stc-vietnam.com | 越南 | 分销商/经销商 | 有回复·跟进中 | 46 | 已 | [SB-315-stc-vietnam.com-越南.md](A/SB-315-stc-vietnam.com-越南.md) |
| SB-326 | PROXEET LIMITED | 塞浦路斯 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 45 | 已 | [SB-326-PROXEET LIMITED-塞浦路斯.md](A/SB-326-PROXEET%20LIMITED-塞浦路斯.md) |
| SB-331 | retelem-dz.com | 阿尔及利亚 | 经销/集成（类型待核） | 有回复·跟进中 | 45 | 已 | [SB-331-retelem-dz.com-阿尔及利亚.md](A/SB-331-retelem-dz.com-阿尔及利亚.md) |
| SB-342 | Sure Transport | 英国 | 经销/集成（类型待核） | 已推送 18 次·未回复 | 44 | 已 | [SB-342-Sure Transport-英国.md](A/SB-342-Sure%20Transport-英国.md) |
| SB-343 | Zekko Tech Private Limited | 印度 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 44 | 已 | [SB-343-Zekko Tech Private Limited-印度.md](A/SB-343-Zekko%20Tech%20Private%20Limited-印度.md) |
| SB-359 | larch-networks.com | 以色列 | 网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购） | 名单内·未触达 | 44 | 已 | [SB-359-larch-networks.com-以色列.md](A/SB-359-larch-networks.com-以色列.md) |
| SB-367 | thuyluc.com | 越南 | 经销/集成（类型待核） | 有回复·跟进中 | 44 | 已 | [SB-367-thuyluc.com-越南.md](A/SB-367-thuyluc.com-越南.md) |
| SB-375 | Delta Consulting | 格鲁吉亚 | 经销/集成（类型待核） | 成交过·已凉（Simon: gg） | 93 | 已 | [SB-375-Delta Consulting-格鲁吉亚.md](A/SB-375-Delta%20Consulting-格鲁吉亚.md) |
| SB-389 | hiperonline.com | 土耳其 | 经销/集成（类型待核） | 名单内·未触达 | 43 | 已 | [SB-389-hiperonline.com-土耳其.md](A/SB-389-hiperonline.com-土耳其.md) |
| SB-392 | makrosisas.com.tr | 土耳其 | 系统集成/工程商 | 名单内·未触达 | 43 | 已 | [SB-392-makrosisas.com.tr-土耳其.md](A/SB-392-makrosisas.com.tr-土耳其.md) |
| SB-447 | automationsystem.in | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 41 | 已 | [SB-447-automationsystem.in-印度.md](A/SB-447-automationsystem.in-印度.md) |
| SB-451 | e-saudi.net | 沙特阿拉伯 | IT/网络贸易商（沙特，有回复，业务待核） | 已推送 1 次·未回复 | 41 | 已 | [SB-451-e-saudi.net-沙特阿拉伯.md](A/SB-451-e-saudi.net-沙特阿拉伯.md) |
| SB-485 | n-itus.com | 韩国 | 经销/集成（类型待核） | 有回复·跟进中 | 40 | 已 | [SB-485-n-itus.com-韩国.md](A/SB-485-n-itus.com-韩国.md) |
| SB-487 | npotelecom.ru | 俄罗斯 | 电信设备企业（俄罗斯，有回复，用户标重要） | 已推送 17 次·未回复 | 40 | 已 | [SB-487-npotelecom.ru-俄罗斯.md](A/SB-487-npotelecom.ru-俄罗斯.md) |
| SB-529 | dmsimfg.com | 美国 | 网络配件品牌商（美国，自有标 MC；官网待核） | 已推送 19 次·未回复 | 38 | 已 | [SB-529-dmsimfg.com-美国.md](A/SB-529-dmsimfg.com-美国.md) |
| SB-542 | lanopia.de | 德国 | 经销/集成（类型待核） | 已推送 8 次·未回复 | 38 | 已 | [SB-542-lanopia.de-德国.md](A/SB-542-lanopia.de-德国.md) |
| SB-630 | CORE IT SOLUTIONS | 印度 | 经销/集成（类型待核） | 有回复·跟进中 | 34 | 已 | [SB-630-CORE IT SOLUTIONS-印度.md](A/SB-630-CORE%20IT%20SOLUTIONS-印度.md) |
| SB-641 | apolloinfoways.in | 印度 | 印度网络品牌商（自有 WatchDog 型号，中国 ODM 采购） | 名单内·未触达 | 34 | 已 | [SB-641-apolloinfoways.in-印度.md](A/SB-641-apolloinfoways.in-印度.md) |
| SB-767 | itmsystems.co.uk | 英国 | 安防/IT 集成商（英国，有回复，工业 FS 现 Utepo） | 已推送 16 次·未回复 | 32 | 已 | [SB-767-itmsystems.co.uk-英国.md](A/SB-767-itmsystems.co.uk-英国.md) |
| SB-826 | versitron.com | 美国 | 经销/集成（类型待核） | 名单内·未触达 | 31 | 已 | [SB-826-versitron.com-美国.md](A/SB-826-versitron.com-美国.md) |
| SB-869 | futurist.com.pk | 巴基斯坦 | 经销/集成（类型待核） | 有回复·跟进中 | 29 | 已 | [SB-869-futurist.com.pk-巴基斯坦.md](A/SB-869-futurist.com.pk-巴基斯坦.md) |
| SB-905 | TELTRONIX \| BRITICOM | 英国 | 品牌商/贴牌需求（OEM/ODM） | 有回复·跟进中 | 28 | 已 | [SB-905-TELTRONIX BRITICOM-英国.md](A/SB-905-TELTRONIX%20BRITICOM-英国.md) |
| SB-910 | etictelecom.com | 法国 | 经销/集成（类型待核） | 有回复·跟进中 | 28 | 已 | [SB-910-etictelecom.com-法国.md](A/SB-910-etictelecom.com-法国.md) |
| SB-924 | Intracom Middle East FZ-LLC | 阿联酋 | 电信系统厂商中东项目公司（项目采购 PoE，体量大） | 名单内·未触达 | 27 | 已 | [SB-924-Intracom Middle East FZ-LLC-阿联酋.md](A/SB-924-Intracom%20Middle%20East%20FZ-LLC-阿联酋.md) |
| SB-949 | ksm.com.au | 澳大利亚 | 工业网络经销商（澳大利亚，国内货源在供） | 已推送 22 次·未回复 | 27 | 已 | [SB-949-ksm.com.au-澳大利亚.md](A/SB-949-ksm.com.au-澳大利亚.md) |
| SB-970 | EION Inc | 加拿大 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 26 | 已 | [SB-970-EION Inc-加拿大.md](A/SB-970-EION%20Inc-加拿大.md) |
| SB-982 | mcss.co.kr | 韩国 | 系统集成 + 在线商城（PLANET / UniFi 渠道） | 名单内·未触达 | 26 | 已 | [SB-982-mcss.co.kr-韩国.md](A/SB-982-mcss.co.kr-韩国.md) |
| SB-984 | olsontech.com | 美国 | CATV/PON 光设备商（美国，MC 为副线） | 已推送 11 次·未回复 | 26 | 已 | [SB-984-olsontech.com-美国.md](A/SB-984-olsontech.com-美国.md) |
| SC-002 | Intelligent | 沙特阿拉伯 | 中资同行（制造+分销） | 有回复·跟进中 | 83 | 已 | [SC-002-Intelligent-沙特阿拉伯.md](A/SC-002-Intelligent-沙特阿拉伯.md) |
| SC-023 | Central Gospel School | 加纳 | 经销/集成（类型待核） | 有回复·跟进中 | 50 | 已 | [SC-023-Central Gospel School-加纳.md](A/SC-023-Central%20Gospel%20School-加纳.md) |
| SC-097 | Three Lines Company | 沙特阿拉伯 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 37 | 已 | [SC-097-Three Lines Company-沙特阿拉伯.md](A/SC-097-Three%20Lines%20Company-沙特阿拉伯.md) |
| SC-1056 | cloudinfotech.co.in | 印度 | 经销/集成（类型待核） | 名单内·未触达 | 15 | 已 | [SC-1056-cloudinfotech.co.in-印度.md](A/SC-1056-cloudinfotech.co.in-印度.md) |
| SC-1200 | futurepointt.com | 巴基斯坦 | 经销/集成（类型待核） | WhatsApp 已加·未回复 | 13 | 已 | [SC-1200-futurepointt.com-巴基斯坦.md](A/SC-1200-futurepointt.com-巴基斯坦.md) |
| SC-1371 | mywatchdog.in | 印度 | OEM（闸 2 判定 · 30% 档） | 名单内·未触达 | 11 | 已 | [SC-1371-mywatchdog.in-印度.md](A/SC-1371-mywatchdog.in-印度.md) |
| SC-1399 | team5tech.com | 印度 | 经销/集成（类型待核） | 名单内·未触达 | 11 | 已 | [SC-1399-team5tech.com-印度.md](A/SC-1399-team5tech.com-印度.md) |
| SC-1657 | San Telequip Pvt. Ltd. | 印度 | 工业自动化渠道（闸 2 判定 · 25% 档） | 名单内·未触达 | 6 | 已 | [SC-1657-San Telequip Pvt. Ltd-印度.md](A/SC-1657-San%20Telequip%20Pvt.%20Ltd-印度.md) |
| SC-1771 | telexcell.com | 印度 | 印度系统集成/贸易商 | WhatsApp 已加·未回复 | 4 | 已 | [SC-1771-telexcell.com-印度.md](A/SC-1771-telexcell.com-印度.md) |
| SC-190 | Crontr Technology | 厄瓜多尔 | 经销/集成（类型待核） | 名单内·未触达 | 23 | 已 | [SC-190-Crontr Technology-厄瓜多尔.md](A/SC-190-Crontr%20Technology-厄瓜多尔.md) |
| SC-1904 | optimal.com.ph | 菲律宾 | 分销商/经销商 | 名单内·未触达 | 1 | 已 | [SC-1904-optimal.com.ph-菲律宾.md](A/SC-1904-optimal.com.ph-菲律宾.md) |
| SC-1942 | satvision-cctv.ru | 俄罗斯 | OEM（闸 2 判定 · 30% 档） | 有回复·跟进中 | 0 | 已 | [SC-1942-satvision-cctv.ru-俄罗斯.md](A/SC-1942-satvision-cctv.ru-俄罗斯.md) |
| SC-2513 | microtech.net.pk | 巴基斯坦 | 巴基斯坦 IT 分销/集成（MikroTik 渠道） | 已推送 3 次·未回复 | -23 | 已 | [SC-2513-microtech.net.pk-巴基斯坦.md](A/SC-2513-microtech.net.pk-巴基斯坦.md) |
| SC-2904 | firsttech.co.za | 南非 | 经销/集成（类型待核） | 用户判定不行 | -51 | 已 | [SC-2904-firsttech.co.za-南非.md](A/SC-2904-firsttech.co.za-南非.md) |
| SC-371 | Visiotech | 西班牙 | OEM（闸 2 判定 · 30% 档） | 历史合作·维护（非 Saga 成单） | 22 | 已 | [SC-371-Visiotech-西班牙.md](A/SC-371-Visiotech-西班牙.md) |

### B 级（1311）— `Saga Clients/B/`（子目录 `SB-0001-0500/` / `SB-0501-1000/` / `SB-1001-1500/` / `SB-1501-2000/` / `SB-2001-2500/` / `SB-2501-3000/` / `SB-3001-3500/`）

全部 1311 个档案见 `Saga Clients/B/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

### C 级（3178）— `Saga Clients/C/`（子目录 `SC-0001-0500/` / `SC-0501-1000/` / `SC-1001-1500/` / `SC-1501-2000/` / `SC-2001-2500/` / `SC-2501-3000/` / `SC-3001-3500/`）

全部 3178 个档案见 `Saga Clients/C/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。

