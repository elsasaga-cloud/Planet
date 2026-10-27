# XC-C0478 · Marvell-switching/sai-poe (美国) · 美国

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-56.md`:59 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XC** — 品牌原厂 / 芯片商 / VMS 厂商 / 同行，不是买家
- 标记：profile批次文件、原厂或同行
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Marvell-switching/sai-poe (美国) |
| 国家 / 城市 | 美国 |
| ISO | US |
| 网站 | — |
| 类型 / 角色 | A类 - Marvell官方PoE开源 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 56 — 芯片平台+GitHub开源+欧洲专业客户 (Marvell/Realtek/Broadcom芯片+开源项目+LinkedIn欧洲) > 💻 二、GitHub开源PoE项目 |
| 来源库字段·类型 | A类 - Marvell官方PoE开源 |
| 来源库字段·项目 | sai-poe, 基于V3协议的PoE方案 |
| 来源库字段·组件 | poelibsai-debian/usr/lib/libsai.so (SAI实现共享库), libapp_scpu.a (SAI-硬件通信vendor specific库ARM64), sai-poe-implementation/board_info/xml+md5 (板卡信息端口/PSE等), poelibsai (debian包含SAI环境PoE数据+函数), PDLIB (解析机制) |
| 来源库字段·构建 | Ubuntu 20.04.6 LTS aarch64-linux-gnu-gcc 9.4.0 + Marvell Tool chain GCC 12 ARM64 |
| 来源库字段·Issues | 802.3bt不工作 (PD请求4 pair ~38W+DUT提供2 pair ~18.5W), 错误PoE budget (24口请求~624W每26W+DUT仅提供~610W给23口), 错误PoE priority (budget exceeded) |
| 来源库字段·开发策略 | 美国Marvell官方PoE开源 (SAI V3协议+ARM64) ★★★★★ |
| 来源文件 | `profile/new-customers-batch-56.md` 第 59 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 6. Marvell-switching/sai-poe (美国)
> - **类型**: A类 - Marvell官方PoE开源
> - **项目**: sai-poe, 基于V3协议的PoE方案
> - **组件**: poelibsai-debian/usr/lib/libsai.so (SAI实现共享库), libapp_scpu.a (SAI-硬件通信vendor specific库ARM64), sai-poe-implementation/board_info/xml+md5 (板卡信息端口/PSE等), poelibsai (debian包含SAI环境PoE数据+函数), PDLIB (解析机制)
> - **构建**: Ubuntu 20.04.6 LTS aarch64-linux-gnu-gcc 9.4.0 + Marvell Tool chain GCC 12 ARM64
> - **Issues**: 802.3bt不工作 (PD请求4 pair ~38W+DUT提供2 pair ~18.5W), 错误PoE budget (24口请求~624W每26W+DUT仅提供~610W给23口), 错误PoE priority (budget exceeded)
> - **开发策略**: 美国Marvell官方PoE开源 (SAI V3协议+ARM64) ★★★★★

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
