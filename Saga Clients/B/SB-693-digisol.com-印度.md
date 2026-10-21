# digisol.com

> **评级 B**　|　印度　|　档案编号 `SB-693`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：系统集成/工程商（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：AI评估(IN)·DONE　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-693
rating: B
rating_auto: B
score: 34
country: 印度
region: 南亚
website: digisol.com
type: 系统集成/工程商
tier_tags: ["AI评估(IN)·DONE"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STI-288DGGPM
price_tier: 25%
research: pending
sources: 1
updated: 2026-10-21
```

## SALES BRIEF（压缩模型）

- **是谁**：印度的系统集成/工程商；兴趣/在卖：工业FS MC 线缆 Pon 周边产品 洪瑞 Upeto的工业FS  新桥商业 洪瑞工业 https://www.digisol.com/product/switching-solutions/industrial-switches/；提到的品牌：Upeto, 洪瑞, FS
- **为什么是 B 级**：+2 在 AI 客户评估名单；+15 AI/Claude 评估 A；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/印度
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推）**：STI-288DGGPM — 工业 L2+ 8 PoE + 2×2.5G SFP；$145.7 USD EXW（25% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：放入慢跟队列（4–6 周一次）；有回复即重评

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | digisol.com（取自域名，公司全名待核） | 推断 |
| 国家 | 印度 | 事实（用户表）|
| 网站/域名 | digisol.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 系统集成/工程商 | 推断（据兴趣/备注关键词） |
| 联系人 | Nandini Singh / Deputy Manager / Ranjan Gupta / Dy. Business Development Manager | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 工业FS MC 线缆 Pon 周边产品<br>洪瑞 Upeto的工业FS <br>新桥商业 洪瑞工业<br>https://www.digisol.com/product/switching-solutions/industrial-switches/ | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 用户 AI 评估 | AI 40% A | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | AI评估(IN)·DONE | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | Upeto, 洪瑞, FS | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **AI**（AI客户评估_IN 08.31.xlsx）：
  > 40% A
  > 印度本土知名网络设备品牌商，产品线覆盖商业交换机、工业交换机、PoE交换机、媒体转换器等，产品线齐全且交换机为核心品类之一；备注显示使用洪瑞（HRUI）、Utepo的工业交换机，新桥的商业交换机（均为4.3绿灯深圳品牌）
  > 发送定制合作提案，重点强调：①工业交换机的深度定制能力（管理UI/功能定制），②与洪瑞/Utepo的差异化（Marvell方案稳定性、PoE++、ERPS环网），③OEM贴牌+长期稳定供货能力
  > 工业PoE交换机（替代洪瑞）、24口商业PoE交换机（替代新桥）、ERPS环网交换机
  > 官网交换机为核心产品线（工业+商业全覆盖）；已确认使用多个深圳白牌供应商（洪瑞、Utepo、新桥），供应链完全开放且有多供应商策略；Digisol为印度本土品牌，有OEM/贴牌需求；属于典型的"品牌商+深圳供应链开放"组合，高度匹配

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SB-693.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| Upeto | 深圳/国内白牌或品牌供应商 | 对方已在买中国货：以 Marvell 芯片 + L2+ 功能 + 交期为差异点做第二货源 |
| 洪瑞 | 洪瑞 = HRUI（Saga 的 Realtek 辅线供应商） | 同源货：Saga STC Realtek 线（见 data/hrui_STC对照表.csv）可直接对型号报价 |
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`nandini.singh@digisol.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`ranjan.gupta@digisol.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Nandini Singh / Deputy Manager / Ranjan Gupta / Dy. Business Development Manager
- 网站/域名：digisol.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| AI客户评估/DONE/AI客户评估_IN 08.31.xlsx#总表:7 | 6 | https://www.digisol.com/products/switching-solutions/ | 印度 | Nandini Singh<br>Deputy Manager<br><br>Ranjan Gupta<br>Dy. Business Development Manager | 谷歌 | 工业FS MC 线缆 Pon 周边产品<br>洪瑞 Upeto的工业FS <br>新桥商业 洪瑞工业<br>https://www.digisol.com/product/switching-solutions/industrial-switches/ | nandini.singh@digisol.com<br>ranjan.gupta@digisol.com |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $145.7 USD EXW（25% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 据用户表兴趣/备注推断；档位 25%（系统集成/工程商） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $188.7 USD EXW（25% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-288DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 34）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
