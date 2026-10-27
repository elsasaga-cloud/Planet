# XC-C0642 · Ziraat Bankası · 土耳其

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-59-part2-turkey.md`:34 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XC** — 终端用户 / 渠道触点（机场、大学、超市、政府、军队…走集成商与框架采购，不是 Saga 的直接买家）
- 标记：profile批次文件、多处出现×3、终端触点
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Ziraat Bankası |
| 国家 / 城市 | 土耳其 |
| ISO | TR |
| 网站 | ziraatbank.com.tr |
| 类型 / 角色 | 土耳其最大银行 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 59 Part 2: 土耳其深度挖掘 Part 2 > 8渠道: ISP+酒店+数据中心+国防+太阳能+政府采购+机场+技术社区 > 渠道J: 数据中心 (10家+行业情报) |
| 来源库字段·城市 | Istanbul/Ümraniye (总部) |
| 来源库字段·网站 | ziraatbank.com.tr |
| 来源库字段·成立 | 1863年(土耳其最古老银行) |
| 来源库字段·规模 | **1,773分行**(1,744国内+29海外), **7,901 ATM**, 25,000+员工 |
| 来源库字段·资产 | ~₺8.47T ($190B), **土耳其最大金融机构** |
| 来源库字段·唯一银行 | 369个地区只有Ziraat(农村覆盖最广) |
| 来源库字段·IT子公司 | **Ziraat Teknoloji A.Ş.**(2001年成立, Yıldız Technopark, 土耳其第3大软件公司) |
| 来源库字段·PoE需求 | 1,773分行 × PoE(4-8摄像头+WiFi AP+门禁+IP电话+ATM监控) |
| 来源库字段·联系方式 | ziraatteknoloji.com.tr (IT采购) |
| 来源库字段·Saga匹配 | 银行分行PoE方案, 通过Ziraat Teknoloji进入 |
| 来源库字段·优先级 | ⭐⭐⭐⭐⭐ |
| 来源文件 | `profile/new-customers-batch-59-part2-turkey.md` 第 34 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `profile/new-customers-batch-59-part5-turkey.md`:17（5渠道: TOKİ世纪住房+BİM/A101/ŞOK/Migros+Ziraat）；`03-海外客户开发清单.md`:5718（🇹🇷 Batch 59 Part 5: 土耳其住房建设+零售连锁+银行+港口+油） |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> - **99.24 Ziraat Bankası** 🇹🇷 B类 | Tier III Gold
>
> ——另见 `profile/new-customers-batch-59-part5-turkey.md`:17：
> - **101.30 Ziraat Bankası** 🇹🇷 A类 | **1,773分行**, ₺8.47T资产, Ziraat Teknoloji IT子公司
>
> ——另见 `03-海外客户开发清单.md`:5718：
> 101.30 Ziraat Bankası — 土耳其最大银行
> - **国家**: 🇹🇷 Turkey | **城市**: Istanbul/Ümraniye (总部)
> - **公司名**: T.C. Ziraat Bankası A.Ş.
> - **网站**: ziraatbank.com.tr
> - **成立**: 1863年(土耳其最古老银行)
> - **规模**: **1,773分行**(1,744国内+29海外), **7,901 ATM**, 25,000+员工
> - **资产**: ~₺8.47T ($190B), **土耳其最大金融机构**
> - **唯一银行**: 369个地区只有Ziraat(农村覆盖最广)
> - **IT子公司**: **Ziraat Teknoloji A.Ş.**(2001年成立, Yıldız Technopark, 土耳其第3大软件公司)
>   - 自研核心银行系统**Finart**(6,000屏幕)
>   - 为22国Ziraat集团提供IT服务
> - **PoE需求**: 1,773分行 × PoE(4-8摄像头+WiFi AP+门禁+IP电话+ATM监控)
>   - **17,000+ PoE端口**
> - **联系方式**: ziraatteknoloji.com.tr (IT采购)
> - **Saga匹配**: 银行分行PoE方案, 通过Ziraat Teknoloji进入

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
