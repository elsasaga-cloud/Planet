# XC-C0712 · TPAO · 土耳其

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-59-part5-turkey.md`:30 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）
>
> **C 池三闸筛选（External 同法，`data/external_clients/sieve_x.json`）：留 XC 储备**（闸 1 · G1-auto · 2026-10-29）：终端 / 应用方 / 市场注记（国家石油公司  ）：走集成商与框架采购，不是直接买家；仅官网 tpao.gov.tr → 留 C 待巡检

## 1. 初判与理由
- 初判：**XC** — 终端用户 / 渠道触点（机场、大学、超市、政府、军队…走集成商与框架采购，不是 Saga 的直接买家）
- 标记：profile批次文件、多处出现×2、终端触点
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | TPAO |
| 国家 / 城市 | 土耳其 |
| ISO | TR |
| 网站 | tpao.gov.tr |
| 类型 / 角色 | 国家石油公司 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 59 Part 5: 土耳其住房+零售+银行+港口+油气 > 5渠道: TOKİ世纪住房+BİM/A101/ŞOK/Migros+Ziraat/İşbank/Garanti+Mersin/Ambarlı港+TPAO/BOTAŞ > 渠道AC: 油气 (2家) |
| 来源库字段·城市 | Ankara |
| 来源库字段·网站 | tpao.gov.tr |
| 来源库字段·Sakarya气田 | 黑海最大发现 |
| 来源库字段·合作伙伴 | ExxonMobil (MoU 2026年1月), TotalEnergies (MoU 2026年4月), Saipem ($1.5B合同), Baker Hughes |
| 来源库字段·陆上设施 | **Filyos工业区**(Zonguldak省), 天然气处理厂 |
| 来源库字段·融资 | $4B债券发行计划 |
| 来源库字段·PoE需求 | 陆上处理厂+海上平台+管道站(工业级PoE, SCADA+安全摄像+环境监控) |
| 来源库字段·Saga匹配 | 工业级PoE交换机(耐高温/防尘), 油气行业专用 |
| 来源库字段·优先级 | ⭐⭐⭐⭐⭐ |
| 来源文件 | `profile/new-customers-batch-59-part5-turkey.md` 第 30 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `03-海外客户开发清单.md`:5841（🇹🇷 Batch 59 Part 5: 土耳其住房建设+零售连锁+银行+港口+油） |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> - **101.39 TPAO** 🇹🇷 A类 | **Sakarya气田785 bcm**, 9.5→40 mcm/天, Filyos处理厂
>
> ——另见 `03-海外客户开发清单.md`:5841：
> 101.39 TPAO (Türkiye Petrolleri) — 国家石油公司
> - **国家**: 🇹🇷 Turkey | **城市**: Ankara
> - **公司名**: Türkiye Petrolleri Anonim Ortaklığı
> - **网站**: tpao.gov.tr
> - **Sakarya气田**: 黑海最大发现
>   - **785 bcm储量**(含Göktepe-3 75bcm, 2025年5月)
>   - 当前产量: **9.5百万m³/天**
>   - 目标: **40百万m³/天**(2028), 满足土耳其30%天然气需求
>   - 水深: 2,200m, 离岸165km
>   - **Osman Gazi浮式生产平台**(2026 Q3投产, 产量翻倍至20mcm/d)
> - **合作伙伴**: ExxonMobil (MoU 2026年1月), TotalEnergies (MoU 2026年4月), Saipem ($1.5B合同), Baker Hughes
> - **陆上设施**: **Filyos工业区**(Zonguldak省), 天然气处理厂
> - **融资**: $4B债券发行计划
> - **PoE需求**: 陆上处理厂+海上平台+管道站(工业级PoE, SCADA+安全摄像+环境监控)
> - **Saga匹配**: 工业级PoE交换机(耐高温/防尘), 油气行业专用

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
