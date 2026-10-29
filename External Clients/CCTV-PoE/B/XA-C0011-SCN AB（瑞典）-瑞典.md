# XA-C0011 · SCN AB（瑞典） · 瑞典

> **现判 XB 慢慢跟进** ｜ 人工改级 2026-10-29：B（Q-76 LT-01 2026-10-29：XA → B 普通跟（长期群 A = 真人往来 / 成单证据；外部库无往来）；原 XA 优先级留痕 x_prio） ｜ 来源 CCTV-PoE `profile/new-customers-batch-8.md`:82 ｜ 导入 2026-10-27 ｜ 研究状态：已研究（LT-T03 2026-10-29）→ 下一动作 首触

## 1. 初判与理由
- 初判：**XA** — 主攻区（美加/欧/土）+ 渠道型买家（分销/集成/安装/零售/OEM 品牌）+ 有邮箱
- 人工改级：XB（2026-10-29，Q-76 LT-01 2026-10-29：XA → B 普通跟（长期群 A = 真人往来 / 成单证据；外部库无往来）；原 XA 优先级留痕 x_prio）；编号不变
- 标记：profile批次文件、多处出现×2
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | SCN AB（瑞典） |
| 国家 / 城市 | 瑞典 |
| ISO | SE |
| 网站 | switches.shop |
| 类型 / 角色 | C类 — Moxa官方分销 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 8 — FCC ID反查 + VMS生态品牌 + 工业品牌渠道 + ERPS技术品牌 > 三、B/C类：工业交换机品牌渠道反挖（Moxa/Antaira/Hirschmann/Perle） |
| 来源库字段·类型 | C类 — Moxa官方分销 |
| 来源库字段·网站 | switches.shop |
| 来源库字段·邮箱 | moxa@switches.shop |
| 来源库字段·电话 | +46 8 668 21 00, +44 1634 300 900 |
| 来源库字段·地址 | Truckvägen 16B, 194 52 Upplands Väsby, Sweden |
| 来源库字段·开发策略 | Moxa瑞典分销，Saga工业PoE可作为性价比替代 |
| 来源库字段·置信度 | ★★★★★ |
| 来源库字段·# | 6 |
| 来源库字段·联系方式 | +46 8 668 21 00 |
| 来源库字段·月潜力 | $10K-30K |
| 来源文件 | `profile/new-customers-batch-8.md` 第 82 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `03-海外客户开发清单.md`:1060（海外客户开发清单 — Saga PoE交换机 > 四十二、A类FCC品牌 + V） |

## 3. 联系方式
- 邮箱：moxa@switches.shop（公开）
- 电话：+46 8 668 21 00；+44 1634 300 900（内部用，不进外发材料）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 10. SCN AB（瑞典）
> - **类型**: C类 — Moxa官方分销
> - **网站**: switches.shop
> - **邮箱**: moxa@switches.shop
> - **电话**: +46 8 668 21 00, +44 1634 300 900
> - **地址**: Truckvägen 16B, 194 52 Upplands Väsby, Sweden
> - **开发策略**: Moxa瑞典分销，Saga工业PoE可作为性价比替代
> - **置信度**: ★★★★★
>
> ——另见 `03-海外客户开发清单.md`:1060：
> | # | 公司名 | 国家 | 类型 | 联系方式 | 月潜力 |
> | 6 | **SCN AB** | 瑞典 | C类(Moxa分销) | +46 8 668 21 00 | $10K-30K |

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究卡（第 2 步，LT-T03，2026-10-29）

- **结论：XA** — SE 工业分销、未触达 → A 首触
- 活着吗：在线（switches.shop，快照 2026-10-29）：Buy MOXA switches online | SCN SWITCHES
- 一句话：Moxa 官方分销（SCN AB / switches.shop）
- 是什么人：Moxa 官方分销（SCN AB / switches.shop）；规模：未量化
- 在卖/在用：Moxa
- 对口哪条线：SmartByte 商用 L2+ + HRUI 入门 PoE + Saga STI 工业 L2+ PoE — 工业交换机专类
- 找得到人吗：moxa@switches.shop（来源库公开邮箱）；KP：无具名
- 已触达：S 箱 9–10 月群发名单未见本域 → 未触达
- 与 Saga Clients：无
- **下一动作：首触** — 工业 DIN 轨 PoE 首触；型号 STI-288DGGPM；价 USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)；窗口 SE 周四 12–14；建议 2026-11-26

证据：
| 类型 | 说明 | 摘录 | 来源 | 日期 |
|---|---|---|---|---|
| 来源库官网/名录核对 | C类 — Moxa官方分销 |  | https://switches.shop/ | 2026-09-28 |
| 官网快照 | 官网在线；Buy MOXA switches online ｜ SCN SWITCHES | Shop premium mechanical, industrial, and custom switches at Switches.shop! Explore high-quality switches for every need with fast shipping and secure checkout. | https://switches.shop/ | 2026-10-29 |

草稿（英文，首触；Simon 发，Agent 不发）：

```text
Subject: DIN-rail industrial PoE switches - second source for your line card

Hi,

Saga Telecom builds DIN-rail industrial Ethernet switches for distributors who already carry automation and industrial communication brands and want a second source at a lower price point (CE certified).

STI-288DGGPM: DIN-rail industrial L2+ switch, 8 x GE PoE+ (240 W budget) + 2 x SFP (1G/2.5G), -40 to +75 C, dual DC input, ERPS ring, SNMPv3, USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days), CE/RoHS, 3-year warranty. Same family: STI-244DGGPM (4 x PoE+ + 2 x SFP, 120 W) at USD 121 and STI-488DGGPM (8 x PoE+ + 4 x SFP, 240 W) at USD 147.

Would a lower-priced DIN-rail PoE switch be worth a test unit as a second source next to your Moxa range?

Simon
Saga Telecom - sagatele.com
```

- 备注：LT-T03 官网快照加厚（2026-10-29）：alive/brands_seen/contacts.page/evidence/site_p1_hint。
轻卡：本轮未外查，沿用来源库官网/名录核对。
