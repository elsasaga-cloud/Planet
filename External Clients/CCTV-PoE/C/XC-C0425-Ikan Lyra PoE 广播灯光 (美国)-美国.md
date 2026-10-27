# XC-C0425 · Ikan Lyra PoE 广播灯光 (美国) · 美国

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-51.md`:181 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XC** — 终端用户 / 渠道触点（机场、大学、超市、政府、军队…走集成商与框架采购，不是 Saga 的直接买家）
- 标记：profile批次文件、终端触点
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Ikan Lyra PoE 广播灯光 (美国) |
| 国家 / 城市 | 美国 |
| ISO | US |
| 网站 | — |
| 类型 / 角色 | B类 - 广播PoE++ DMX-over-IP |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 51 — 垂直场景PoE：医疗 + 教育校园 + 酒店 + 体育场 + 广播演播室 > 📺 五、广播演播室 PoE |
| 来源库字段·类型 | B类 - 广播PoE++ DMX-over-IP |
| 来源库字段·特点 | PoE演播室灯光改变部署模型 (电力+控制单Cat6→无电工+无管道+无许可大多数辖区), 灯具成IP设备网络 (AV团队已管理平台控制), DMX-over-IP (Art-Net+sACN标准广播控制语言→与视频流+控制信号同网络→无需独立DMX控制台), Q-SYS认证插件控制256灯/宇宙 (无需独立灯光控制台) |
| 来源库字段·案例 | Gwinnett County Public Schools Georgia 40+广播工作室PoE灯光 (无任何位置拉电气许可) |
| 来源库字段·交换机 | PoE++ 802.3bt管理足够每口瓦数+总预算, Ikan预匹配Netgear Ultra90 PoE++ 802.3bt (380W非管理小部署/720W管理大部署+VLAN分段) |
| 来源库字段·开发策略 | 美国广播PoE++ DMX-over-IP (Q-SYS+Art-Net+sACN) ★★★★★ |
| 来源文件 | `profile/new-customers-batch-51.md` 第 181 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 26. Ikan Lyra PoE 广播灯光 (美国)
> - **类型**: B类 - 广播PoE++ DMX-over-IP
> - **产品**:
>   - LBX8-POE: 50W PoE++ 802.3bt单Cat6, 双色3200K-5600K, Art-Net+sACN+DMX-over-IP, Q-SYS认证插件, 钨等效500W, 97CRI
>   - LBX10-POE: 85W PoE++同样控制栈, 钨等效750W, 5-pin XLR传统DMX512
>   - LBX20-POE: 170W双PoE++连接, 钨等效1000W, 大工作室
> - **特点**: PoE演播室灯光改变部署模型 (电力+控制单Cat6→无电工+无管道+无许可大多数辖区), 灯具成IP设备网络 (AV团队已管理平台控制), DMX-over-IP (Art-Net+sACN标准广播控制语言→与视频流+控制信号同网络→无需独立DMX控制台), Q-SYS认证插件控制256灯/宇宙 (无需独立灯光控制台)
> - **案例**: Gwinnett County Public Schools Georgia 40+广播工作室PoE灯光 (无任何位置拉电气许可)
> - **交换机**: PoE++ 802.3bt管理足够每口瓦数+总预算, Ikan预匹配Netgear Ultra90 PoE++ 802.3bt (380W非管理小部署/720W管理大部署+VLAN分段)
> - **开发策略**: 美国广播PoE++ DMX-over-IP (Q-SYS+Art-Net+sACN) ★★★★★

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
