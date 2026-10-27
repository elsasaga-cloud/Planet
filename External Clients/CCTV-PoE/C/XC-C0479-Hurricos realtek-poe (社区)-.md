# XC-C0479 · Hurricos/realtek-poe (社区) · 

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-56.md`:67 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XC** — 品牌原厂 / 芯片商 / VMS 厂商 / 同行，不是买家
- 标记：profile批次文件、原厂或同行
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Hurricos/realtek-poe (社区) |
| 国家 / 城市 |  |
| ISO | 待核 |
| 网站 | — |
| 类型 / 角色 | A类 - Realtek PoE开源守护进程 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 56 — 芯片平台+GitHub开源+欧洲专业客户 (Marvell/Realtek/Broadcom芯片+开源项目+LinkedIn欧洲) > 💻 二、GitHub开源PoE项目 |
| 来源库字段·类型 | A类 - Realtek PoE开源守护进程 |
| 来源库字段·项目 | realtek-poe, 系统守护进程处理PoE PSE配置+控制 (Broadcom+Realtek PoE控制器) |
| 来源库字段·OpenWrt | opkg install realtek-poe, UCI poe配置/etc/config/poe, 系统守护进程init.d启动脚本编辑配置自动重载, ubus call poe reload手动重配置, ubus -v list poe运行时接口查询端口状态+管理端口, ubus call poe manage动态切换端口电力 |
| 来源库字段·芯片支持 | BCM59111 (Broadcom dialect 0x23) + RTL8238B (Realtek dialect 0x41), 调查RTL8238B协议支持 (Issue #25), TI TPS23861 I2C支持 (realtek-poe-ti Issue #27) |
| 来源库字段·问题 | Zyxel GS1900-24HP v1 PoE不工作25.12.x (Issue #23557), force_dialect 'realtek'导致完全失败 (all-0xFF+firmware v255.255), GS1900-24HP v1使用Broadcom dialect仅, parser相同但reply结构不同 |
| 来源库字段·构建 | mips_24kc不再构建 (Issue #26292), 仍构建mips_4kec, 48口Realtek交换无PoE控制器包, 应包含rtl839x默认包 |
| 来源库字段·开发策略 | 社区Realtek PoE开源守护进程 (BCM59111+RTL8238B+OpenWrt) ★★★★★ |
| 来源文件 | `profile/new-customers-batch-56.md` 第 67 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 7. Hurricos/realtek-poe (社区)
> - **类型**: A类 - Realtek PoE开源守护进程
> - **项目**: realtek-poe, 系统守护进程处理PoE PSE配置+控制 (Broadcom+Realtek PoE控制器)
> - **OpenWrt**: opkg install realtek-poe, UCI poe配置/etc/config/poe, 系统守护进程init.d启动脚本编辑配置自动重载, ubus call poe reload手动重配置, ubus -v list poe运行时接口查询端口状态+管理端口, ubus call poe manage动态切换端口电力
> - **芯片支持**: BCM59111 (Broadcom dialect 0x23) + RTL8238B (Realtek dialect 0x41), 调查RTL8238B协议支持 (Issue #25), TI TPS23861 I2C支持 (realtek-poe-ti Issue #27)
> - **问题**: Zyxel GS1900-24HP v1 PoE不工作25.12.x (Issue #23557), force_dialect 'realtek'导致完全失败 (all-0xFF+firmware v255.255), GS1900-24HP v1使用Broadcom dialect仅, parser相同但reply结构不同
> - **构建**: mips_24kc不再构建 (Issue #26292), 仍构建mips_4kec, 48口Realtek交换无PoE控制器包, 应包含rtl839x默认包
> - **开发策略**: 社区Realtek PoE开源守护进程 (BCM59111+RTL8238B+OpenWrt) ★★★★★

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
