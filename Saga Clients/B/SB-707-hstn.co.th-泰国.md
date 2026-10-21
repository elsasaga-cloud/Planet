# hstn.co.th

> **评级 B**　|　泰国　|　档案编号 `SB-707`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：分销商/经销商（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：A优质名单(Thailand)、AI评估(TH)·DONE　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-707
rating: B
rating_auto: B
score: 34
country: 泰国
region: 亚太
website: hstn.co.th
type: 分销商/经销商
tier_tags: ["A优质名单(Thailand)", "AI评估(TH)·DONE"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-448DGGPM
price_tier: 20%
research: pending
site_snapshot: none
sources: 2
updated: 2026-10-21
```

## SALES BRIEF（压缩模型）

- **是谁**：泰国的分销商/经销商；兴趣/在卖：Switches；提到的品牌：Cisco, Hikvision, Dahua, Aruba, HPE
- **为什么是 B 级**：+6 在 A/DONE 优质国家名单（已做过整轮推送）；+2 在 AI 客户评估名单；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+3 区域 亚太/泰国
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推）**：STC-448DGGPM — 48 口 PoE 走量款；$308.5 USD EXW（20% 档，SmartByte LT-S8352GP-4GX48GT 1720 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：采购/产品负责人姓名（表内只有公司级邮箱）；网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：放入慢跟队列（4–6 周一次）；有回复即重评

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | hstn.co.th（取自域名，公司全名待核） | 推断 |
| 国家 | 泰国 | 事实（用户表）|
| 网站/域名 | hstn.co.th | 事实（用户表 URL/邮箱域名） |
| 类型 | 分销商/经销商 | 推断（据兴趣/备注关键词） |
| 联系人 | — | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | Switches | 事实（用户表） |
| 用户备注（Remark） | 早期ai: 20% B<br>泰国IT设备分销商，销售企业网络设备和IT基础设施<br>发送PoE交换机产品线邮件，强调性价比和快速交期<br>24口PoE交换机、L2管理交换机<br>官网销售Ruckus等品牌网络设备，属于多品牌IT设备分销<br>Ruckus是红灯品牌体系（HPE/Aruba级别），但这家是多品牌IT分销商，不是只卖Ruckus<br>可以群发但别抱太大期望 \| max: 25% B<br>泰国中型系统集成商/项目商，主要承接酒店、园区弱电及CCTV/IPTV系统集成项目。<br>以项目降本为切入点，推荐用于CCTV和园区边缘接入的高性价比PoE交换机，避开其在核心层（Ruckus）的竞争。<br>24/48口商业PoE交换机、CCTV专用交换机<br>官网项目案例使用Ruckus（红灯核心网络）及Hikvision/Dahua（黄灯安防）；作为项目商关注方案可行性与成本，虽有红灯品牌但安防接入层存在让利渗透空间。 \| gpt: 15% C<br>核心销售Ruckus高端网络设备，偏品牌代理/企业网络方案，供应商体系可能较严格<br>交换机涉及高端WiFi/园区网络生态，存在红灯品牌属性，不适合作为重点开发目标 \| gemini: 15%  C<br>主要代理Ruckus、Cisco、Aruba等国际一线红灯品牌，供应链极度封闭且预算门槛高 \| claude4.5: 10% C<br>官网主推Ruckus ICX高端核心交换机（25G/汇聚核心级，Ruckus属于Commscope旗下，红灯品牌级别）；产品定位高端企业/数据中心市场，远超我司产品定位；公司规模约100-200人，供应商准入门槛高；价格预算与我司不在同一量级 | 事实（用户表） |
| 所在清单 | A优质名单(Thailand)、AI评估(TH)·DONE | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | Cisco, Hikvision, Dahua, Aruba, HPE | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SB-707.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| Cisco | 企业级大牌（Cisco/HPE/华为类） | Saga 只能接接入层/工业层，不对标核心；问清是否有白牌接入层需求 |
| Hikvision | 安防摄像头品牌 | 对方是安防集成/经销：主推 PoE 交换机配套（看门狗、长距、bt 口） |
| Dahua | 安防摄像头品牌 | 对方是安防集成/经销：主推 PoE 交换机配套（看门狗、长距、bt 口） |
| Aruba | 企业级大牌（Cisco/HPE/华为类） | Saga 只能接接入层/工业层，不对标核心；问清是否有白牌接入层需求 |
| HPE | 企业级大牌（Cisco/HPE/华为类） | Saga 只能接接入层/工业层，不对标核心；问清是否有白牌接入层需求 |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`info@hstn.co.th`〔企业邮箱；来源：用户表原值〕
- 邮箱：`rungruengh@hstn.co.th`〔企业邮箱；来源：用户表原值〕
- 邮箱：`khomkits@hstn.co.th`〔企业邮箱；来源：用户表原值〕
- 网站/域名：hstn.co.th
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| —（未具名） | 公司级 | info@hstn.co.th / rungruengh@hstn.co.th | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:hstn.co.th`, `e:info@hstn.co.th`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/Thailand 2.27.xlsx#总表:6 | 5 | https://www.hstn.co.th/en/product/58341-60808/icx-7850-48f-ruckus-high-end-aggregationcore-48-ports-25gsfp24-chassis-replacement-switch-network-system-wifi-wire-system | 泰国 |  | 谷歌 | Switches | info@hstn.co.th |  | — |
| AI客户评估/DONE/AI客户评估_TH 09.28.xlsx#总表:6 | 5 | https://www.hstn.co.th/en/product/58341-60808/icx-7850-48f-ruckus-high-end-aggregationcore-48-ports-25gsfp24-chassis-replacement-switch-network-system-wifi-wire-system | 泰国 |  | 谷歌 | Switches | info@hstn.co.th<br>rungruengh@hstn.co.th<br>khomkits@hstn.co.th | 早期ai: 20% B<br>泰国IT设备分销商，销售企业网络设备和IT基础设施<br>发送PoE交换机产品线邮件，强调性价比和快速交期<br>24口PoE交换机、L2管理交换机<br>官网销售Ruckus等品牌网络设备，属于多品牌IT设备分销<br>Ruckus是红灯品牌体系（HPE/Aruba级别），但这家是多品牌IT分销商，不是只卖Ruckus<br>可以群发但别抱太大期望 \| max: 25% B<br>泰国中型系统集成商/项目商，主要承接酒店、园区弱电及CCTV/IPTV系统集成项目。<br>以项目降本为切入点，推荐用于CCTV和园区边缘接入的高性价比PoE交换机，避开其在核心层（Ruckus）的竞争。<br>24/48口商业PoE交换机、CCTV专用交换机<br>官网项目案例使用Ruckus（红灯核心网络）及Hikvision/Dahua（黄灯安防）；作为项目商关注方案可行性与成本，虽有红灯品牌但安防接入层存在让利渗透空间。 \| gpt: 15% C<br>核心销售Ruckus高端网络设备，偏品牌代理/企业网络方案，供应商体系可能较严格<br>交换机涉及高端WiFi/园区网络生态，存在红灯品牌属性，不适合作为重点开发目标 \| gemini: 15%  C<br>主要代理Ruckus、Cisco、Aruba等国际一线红灯品牌，供应链极度封闭且预算门槛高 \| claude4.5: 10% C<br>官网主推Ruckus ICX高端核心交换机（25G/汇聚核心级，Ruckus属于Commscope旗下，红灯品牌级别）；产品定位高端企业/数据中心市场，远超我司产品定位；公司规模约100-200人，供应商准入门槛高；价格预算与我司不在同一量级 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-448DGGPM | 48 口 PoE 走量款 | $308.5 USD EXW（20% 档，SmartByte LT-S8352GP-4GX48GT 1720 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 据用户表兴趣/备注推断；档位 20%（分销商/经销商） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $181.2 USD EXW（20% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-448DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-448DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：名单内已有联系记录，不是零起点
- **W**：无具名决策人，仍是公司级触达
- **O**：P1 STC-448DGGPM 按 20% 档报价，做现供应商的第二货源；对位其在用/在卖的 Cisco, Aruba, HPE：涨价、断货或交期拉长时切入
- **T**：深圳同行（ONV / Utepo / 迈威等）价格战；现有品牌分销协议可能限制同品类采购；汇率与海运波动吃掉 20–30% 的价差

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（在卖/在用交换机或 PoE） | ✅ |
| 决策人识别 | ❌ 未识别（公司级） |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ✅ Cisco, Hikvision, Dahua, Aruba |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 采购/产品负责人姓名（表内只有公司级邮箱）
- [ ] 网页调研未做（公司规模/业务/在卖品牌待核）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-448DGGPM - 48-port Gigabit PoE+ L2+ managed switch (Marvell-based, neutral label)

```text
Hello,

We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option.

We supply a Marvell-based 48-port Gigabit PoE+ L2+ managed switch - model STC-448DGGPM - that fits the same slot as the Cisco class you work with at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $308.5 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Are PoE / industrial switches something you still source today, or has that line been dropped?

If useful, I can send one unit for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-20**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 34）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
