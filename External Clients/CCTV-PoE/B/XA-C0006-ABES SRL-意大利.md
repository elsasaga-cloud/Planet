# XA-C0006 · ABES SRL · 意大利

> **现判 XB 慢慢跟进** ｜ 人工改级 2026-10-29：B（Q-76 LT-01 2026-10-29：XA → B 普通跟（长期群 A = 真人往来 / 成单证据；外部库无往来）；原 XA 优先级留痕 x_prio） ｜ 来源 CCTV-PoE `profile/new-customers-batch-5.md`:429 ｜ 导入 2026-10-27 ｜ 研究状态：已研究（W2-R05b 2026-10-27）→ 下一动作 首触

## 1. 初判与理由
- 初判：**XA** — 主攻区（美加/欧/土）+ 渠道型买家（分销/集成/安装/零售/OEM 品牌）+ 有邮箱
- 人工改级：XB（2026-10-29，Q-76 LT-01 2026-10-29：XA → B 普通跟（长期群 A = 真人往来 / 成单证据；外部库无往来）；原 XA 优先级留痕 x_prio）；编号不变
- 标记：profile批次文件、多处出现×2
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | ABES SRL |
| 国家 / 城市 | 意大利 |
| ISO | IT |
| 网站 | — |
| 类型 / 角色 | Hikvision分销 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 5 新发现海外客户档案 > 八、法国/西班牙/德国/意大利 (Western Europe) |
| 来源库字段·电话 | 011 2290703 |
| 来源库字段·邮箱 | info@abes.it |
| 来源库字段·地址 | Via Traversella 13a, 10148 Torino |
| 来源库字段·业务 | Hikvision分销 |
| 来源库字段·采购潜力 | $5K-15K/批 |
| 来源库字段·开发策略 | 意大利Hikvision渠道 |
| 来源库字段·# | 6 |
| 来源库字段·联系方式 | 011 2290703, info@abes.it |
| 来源库字段·月采购潜力 | $5K-15K |
| 来源文件 | `profile/new-customers-batch-5.md` 第 429 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `03-海外客户开发清单.md`:736（海外客户开发清单 — Saga PoE交换机 > 三十、西欧（法国/德国/西班牙） |

## 3. 联系方式
- 邮箱：info@abes.it（公开）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 48. ABES SRL
> - **国家**: 意大利
> - **电话**: 011 2290703
> - **邮箱**: info@abes.it
> - **地址**: Via Traversella 13a, 10148 Torino
> - **业务**: Hikvision分销
> - **采购潜力**: $5K-15K/批
> - **开发策略**: 意大利Hikvision渠道
>
> ——另见 `03-海外客户开发清单.md`:736：
> | # | 公司名 | 国家 | 联系方式 | 月采购潜力 |
> | 6 | **ABES SRL** | 意大利 | 011 2290703, info@abes.it | $5K-15K |

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究卡（第 2 步，W2-R05b，2026-10-27）

- **结论：XA** — IT 区域安防分销、未触达 → A 首触
- 活着吗：来源库 2026-09-28 核对在线；本轮未复查
- 一句话：安防专业分销（ABES S.r.l.，Torino；1985 起，Hikvision 皮埃蒙特/利古里亚/奥斯塔分销，防火/防盗/TVCC，三处门市，5–9 人）
- 是什么人：安防专业分销（ABES S.r.l.，Torino；1985 起，Hikvision 皮埃蒙特/利古里亚/奥斯塔分销，防火/防盗/TVCC，三处门市，5–9 人）；规模：安防专业分销（ABES S.r.l.，Torino；1985 起，Hikvision 皮埃蒙特/利古里亚/奥斯塔分销，防火/防盗/TVCC，三处门市，5–9 人）
- 对口哪条线：SmartByte 商用 L2+ + HRUI 入门 PoE + Saga STI 工业 L2+ PoE — 安防批发，PoE 配摄像机
- 找得到人吗：info@abes.it（来源库公开邮箱）；KP：无具名
- 已触达：S 箱 9–10 月群发名单未见本域 → 未触达
- 与 Saga Clients：无
- **下一动作：首触** — 分销三件套：HRUI 24 口 + SmartByte 24 口 L2+ + STI；型号 STC-2224GP / STC-424XGGPM-280W / STI-288DGGPM；价 USD 86 / USD 170 / USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)；窗口 IT 周四 12–14；建议 2026-11-26

证据：
| 类型 | 说明 | 摘录 | 来源 | 日期 |
|---|---|---|---|---|
| 来源库官网/名录核对 | Hikvision分销 |  | https://abes.it/ | 2026-09-28 |

草稿（英文，首触；Simon 发，Agent 不发）：

```text
Subject: PoE switch line for your reseller channel - distributor pricing

Hi,

Saga Telecom supplies network and security distributors in Europe and North America with PoE and industrial switches; we are an engineering and supply-chain-first telecom partner, so you deal directly with the people who specify the product.

Three PoE switches our distributor partners move most, all EXW Shenzhen (snapshot 2026-10-27, valid 15 days), CE, under our label or yours:

- STC-2224GP: 24 x GE PoE+ (300 W) + 2 x GE + 2 x SFP, USD 86.
- STC-424XGGPM-280W: 24 x GE PoE+ (280 W) + 4 x 10G SFP+, Marvell-based L2+ managed, USD 170.
- STI-288DGGPM: DIN-rail industrial L2+, 8 x GE PoE+ (240 W) + 2 x SFP, -40 to +75 C, USD 137, 3-year warranty (12 months on the commercial units).

Which would be worth a sample for your installers first - the 24-port entry PoE switch or the DIN-rail unit?

Simon
Saga Telecom - sagatele.com
```

- 备注：本轮 web_search：abes.it/azienda「2012 … distribuzione per Piemonte Liguria e Val D'Aosta con Hikvision」；europages 5–9 人。 轻卡：本轮未外查，沿用来源库官网/名录核对。
