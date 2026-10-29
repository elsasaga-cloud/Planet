# XC-C0724 · Vestel · 土耳其

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-59-part6-turkey.md`:25 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）
>
> **C 池三闸筛选（External 同法，`data/external_clients/sieve_x.json`）：留 XC 储备**（闸 1 · G1-auto · 2026-10-29）：终端 / 应用方 / 市场注记（欧洲最大电子制造综合体  ）：走集成商与框架采购，不是直接买家；仅官网 vestel.com.tr → 留 C 待巡检

## 1. 初判与理由
- 初判：**XC** — 终端用户 / 渠道触点（机场、大学、超市、政府、军队…走集成商与框架采购，不是 Saga 的直接买家）
- 标记：profile批次文件、多处出现×2、终端触点
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Vestel |
| 国家 / 城市 | 土耳其 |
| ISO | TR |
| 网站 | vestel.com.tr |
| 类型 / 角色 | 欧洲最大电子制造综合体 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 59 Part 6: 土耳其机场+大学+建筑+白电+燃气 > 5渠道: IST 9000 CCTV+208大学Ruijie+48 ENR Top 250+Arçelik/Vestel I4.0+İGDAŞ 24646km > 渠道AG: 白电制造 (2家 = 18,000+ PoE) |
| 来源库字段·城市 | Manisa (Izmir附近40km) |
| 来源库字段·网站 | vestel.com.tr |
| 来源库字段·母公司 | Zorlu Holding |
| 来源库字段·Vestel City | **1.3M m²**, 欧洲最大单体工业综合体 |
| 来源库字段·工业4.0 | 全自动智能工厂转型, AI+IoT, 机器人系统 |
| 来源库字段·消防 | 6中央火警面板+2中继, 1,000传感; Vestel City 14面板(11中央+3中继), 45回路, 光纤网络, 数据中心监控 |
| 来源库字段·品牌 | 白标ODM(Roku/VIDAA/TiVo/Android TV) + Vestel自有品牌 |
| 来源库字段·PoE需求 | Vestel City全厂区PoE(产线+仓储+安防+消防+IoT传感器) |
| 来源库字段·Saga匹配 | 工业级PoE, 大规模工厂方案 |
| 来源库字段·优先级 | ⭐⭐⭐⭐⭐ |
| 来源文件 | `profile/new-customers-batch-59-part6-turkey.md` 第 25 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `03-海外客户开发清单.md`:6093（🇹🇷 Batch 59 Part 6: 土耳其机场+大学+建筑巨头+白电工厂+燃） |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> - **101.53 Vestel** 🇹🇷 A类 | **1.3M m²** Vestel City, 3000万台/年, NatGeo Mega Factories
>
> ——另见 `03-海外客户开发清单.md`:6093：
> 101.53 Vestel — 欧洲最大电子制造综合体
> - **国家**: 🇹🇷 Turkey | **城市**: Manisa (Izmir附近40km)
> - **公司名**: Vestel Elektronik Sanayi ve Ticaret A.Ş.
> - **网站**: vestel.com.tr | vestelinternational.com
> - **母公司**: Zorlu Holding
> - **规模**:
>   - **Vestel City**: **1.3M m²**, 欧洲最大单体工业综合体
>   - 年产能: **3,000万台**(10M TV + 13.2M白电 + 4M数码)
>   - 16,000员工
>   - National Geographic **"Mega Factories"**纪录片唯一土耳其工厂
>   - 160国出口
> - **工业4.0**: 全自动智能工厂转型, AI+IoT, 机器人系统
> - **消防**: 6中央火警面板+2中继, 1,000传感; Vestel City 14面板(11中央+3中继), 45回路, 光纤网络, 数据中心监控
> - **品牌**: 白标ODM(Roku/VIDAA/TiVo/Android TV) + Vestel自有品牌
> - **PoE需求**: Vestel City全厂区PoE(产线+仓储+安防+消防+IoT传感器)

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
