# XB-C0497 · rcawston/mokerlink-openwrt (社区) · 

> **初判 XB 慢慢跟进** ｜ 来源 CCTV-PoE `profile/new-customers-batch-56.md`:76 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XB** — 国别未识别，待核后再定
- 标记：profile批次文件、国别待核
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | rcawston/mokerlink-openwrt (社区) |
| 国家 / 城市 |  |
| ISO | 待核 |
| 网站 | — |
| 类型 / 角色 | A类 - MokerLink 10G PoE OpenWrt |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 56 — 芯片平台+GitHub开源+欧洲专业客户 (Marvell/Realtek/Broadcom芯片+开源项目+LinkedIn欧洲) > 💻 二、GitHub开源PoE项目 |
| 来源库字段·类型 | A类 - MokerLink 10G PoE OpenWrt |
| 来源库字段·项目 | mokerlink-openwrt, MokerLink POE-10G07110GSM开源替换固件 (7×10GBASE-T PoE++ + 1×10G SFP+, Realtek RTL9303), 目标: 交换正确转发流量+持续工作 |
| 来源库字段·OpenWrt | realtek target已支持25+ RTL930x交换包括多个近亲 |
| 来源库字段·开发策略 | 社区MokerLink 10G PoE OpenWrt (RTL9303+RTL8239 PoE驱动) ★★★★★ |
| 来源文件 | `profile/new-customers-batch-56.md` 第 76 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 8. rcawston/mokerlink-openwrt (社区)
> - **类型**: A类 - MokerLink 10G PoE OpenWrt
> - **项目**: mokerlink-openwrt, MokerLink POE-10G07110GSM开源替换固件 (7×10GBASE-T PoE++ + 1×10G SFP+, Realtek RTL9303), 目标: 交换正确转发流量+持续工作
> - **OpenWrt**: realtek target已支持25+ RTL930x交换包括多个近亲
> - **布局**:
>   - openwrt/target/linux/realtek/dts/rtl9303_mokerlink_poe-10g07110gsm.dts (板卡描述device tree)
>   - patches/ (OpenWrt修改: 板卡image recipe+MAC地址源+PoE默认+风扇控制+kernel包+交换驱动link change报告修复+uci-defaults函数PoE默认使用)
>   - openwrt/package/network/config/netifd/patches/ (netifd修改从board.json读取PoE默认)
>   - openwrt/target/linux/realtek/files-6.18, patches-6.18/83x-* (新kernel驱动+绑定: RTL8239 PoE realtek-rtl8239+PoE LEDs leds-rtl9300-port+两个绑定patches 833/834上游)
>   - scripts/ (build.sh+check-dts.sh+check-kernel.sh+make-upstream.py构建OpenWrt/netifd/Linux提交+uimage-remagic.py+uboot-wiring.py从U-Boot读取端口接线+uboot-md2bin.py转U-Boot flash dump为binary+uboot-collect.py收集所有U-Boot信息dump flash串口CRC验证+extract-poe-firmware.py复制RTL8239 PoE firmware)
> - **开发策略**: 社区MokerLink 10G PoE OpenWrt (RTL9303+RTL8239 PoE驱动) ★★★★★

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
