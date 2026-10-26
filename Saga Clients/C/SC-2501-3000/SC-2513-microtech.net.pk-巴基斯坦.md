# microtech.net.pk
**官方名称（调研核实）**：Microtech Inc（巴基斯坦卡拉奇；Noman Asghar）

> **评级 C**　|　巴基斯坦　|　档案编号 `SC-2513`　|　优先级 —　|　状态：已推送 3 次·未回复
>
> **类型**：巴基斯坦 IT 分销/集成（MikroTik 渠道）（推断）　|　**历史关系**：推送 3 次（2025-06-03 → 2025-10-02）　|　**所在清单**：E已回复、用户判定不行　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-2513
rating: C
rating_auto: C
name_official: "Microtech Inc（巴基斯坦卡拉奇；Noman Asghar）"
score: -23
country: 巴基斯坦
region: 南亚
website: microtech.net.pk
type: 巴基斯坦 IT 分销/集成（MikroTik 渠道）
tier_tags: ["E已回复", "用户判定不行"]
deal: no
replies: 0
followups: 3
first_contact: 2025-06-03
last_contact: 2025-10-02
s_mail: 6 msgs (out 6 / in 0), 2024-07-02 -> 2026-10-22
p1: STH-2C24XF-HSI（24×10G SFP+ + 2×100G）
price_tier: 20%
research: done
site_snapshot: none
sources: 2
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：Elsa 邮箱两线程 5 封：2025-06-04 对「10G Media Converter」回「These Product Are Not Available」（把我们当买家）；2026-05-11 对「10G Enterprise SFP Switch」回「Please find the attachment」= 他们自己的报价单 S10616：MikroTik CRS326-24S-2Q+RM PKR 165,500（≈US$590，另 18% 税）——反向对标，线程里无 Elsa 回复 = 我方欠答。用户表「用户判定不行」。（调研 2026-10-25；表内兴趣：工业FS PoE 周边产品 有洪瑞的商业PoE V-sol的；洪瑞的商业POE）
- **为什么是 C 级**：+18 在「已回复」名单（A/E Replied）；-60 用户已归入「不行及不太相关的」；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/巴基斯坦；+5 最近活动 2025；-3 跟进表最近平台标记 E（已降为群发）；C 级细分：用户判定不行/不相关
- **历史互动**：推送 3 次（2025-06-03 → 2025-10-02）
- **P1**：不推（C 级）；若对方主动来询，起手 STH-2C24XF-HSI（24×10G SFP+ + 2×100G）（深挖对位：只为交代反向报价；按群发价 $1,500 说清不是同级）
- **最大未知**：年走量与现供应商
- **下一步**：现在（仅此一封；Simon 用户表判「不行」，发不发由 Simon） Elsa 邮箱 → info@microtech.net.pk（回 2026-05-11 真实线程「Re: 10G Enterprise SFP Switch」） 一封交代：CRS326-24S-2Q+RM（24×10G SFP+ + 2×40G）与我们 24×1G SFP + 8 combo + 4×10G 不是同级；同级机 STH-2C24XF-HSI $1,500；一问用途；之后不动（第 77 批 2026-10-25 T29-U56「值得捞的处理一下」）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-25）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SC-2513` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-25。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：Elsa 1:1 去信 2 轮 + 真人回 2 封（2025-06-04、2026-05-11）；我方欠答 1 处（2026-05-11 反向报价单）；C 不改（Simon 用户表「不行」）** ｜ 类型：巴基斯坦 MikroTik 渠道商 ｜ 筛子：1（反向对标，未表达采购意向） ｜ 停点：他发来的是自己的 MikroTik 报价单——我们没回 ｜ 复活：一封交代：不是同级机 + 我们 24×10G SFP+ 的价位 + 一问用途；之后不动 ｜ 通路：巴基斯坦（非主战场） ｜ 节奏：仅此一封 ｜ 证据：`data/gmail_e/text/19e15908306082b4.json`；附件 `data/gmail_e/attachments/SC-2513_Quotation-S10616_2026-05-11.pdf`；`docs/gmail/Elsa邮箱_来询未回清单_2026-10.md` 第 2 条
- **现状一句话**：卡拉奇 Microtech 对 Elsa 2026-05-11 的 24×1G SFP 机群发，回了一张他们自己卖 MikroTik CRS326-24S-2Q+RM 的报价单（PKR 165,500 + 18% 税），等于问「你们这台对得上这个价吗」；我们没答。
- **对方真实需求（有据）**：24×10G SFP+ 级别的汇聚/核心机价格参照（MikroTik 心理价 ≈ US$590）
- **断点 / 为什么停在这里**：反向报价单无人答（2026-05-11 起）
- **Saga 现在该推什么**：P1 **STH-2C24XF-HSI**（None% 档，锚价：STH-2C24XF-HSI $1,500（2026-07-20 群发价；SA-060 实报 $1,250 含 MA 不外推）；24×1G SFP 机（群发原机）$280 他已见）——CENTEC 按项目锚价；此处只为说清不是同级，不求成交
  - 复购/在买项：无
  - 做不了 / 要先核的：用；途；（；I；S；P； ；环； ；/； ；企；业；核；心；）
- **下一步（具体）**：现在（仅此一封；Simon 用户表判「不行」，发不发由 Simon）　Elsa 邮箱 → info@microtech.net.pk（回 2026-05-11 真实线程「Re: 10G Enterprise SFP Switch」）　一封交代：CRS326-24S-2Q+RM（24×10G SFP+ + 2×40G）与我们 24×1G SFP + 8 combo + 4×10G 不是同级；同级机 STH-2C24XF-HSI $1,500；一问用途；之后不动（第 77 批 2026-10-25 T29-U56「值得捞的处理一下」）
  - 第一问（只问一个）：Noman - was the CRS326 quoted for an ISP aggregation ring or an enterprise core?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-06-04 | 来 | Noman Asghar（Microtech Inc） | Dear Elsa, These Product Are Not Available. | 把 Elsa 的 10G 媒体转换器推介当成了询价——说明对方是渠道商；Elsa 06-06 已回 | `gmail_e 1973b67afb1f650a` |
| 2026-05-11 | 来 | Noman Asghar（cc sales@microtech.net.pk） | Please Find The Attachment.（附 Quotation - S10616.pdf：MikroTik CRS326-24S-2Q+RM，PKR 165,500 + 18% 税；另附我方 Dual AC.jpg） | 反向报价 = 巴基斯坦渠道对 24×10G SFP+ 的心理价位 ≈ US$590；线程无 Elsa 回复 → 我方欠答 | `gmail_e 19e15908306082b4` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：用途未知

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | microtech.net.pk（取自域名，公司全名待核） | 推断 |
| 国家 | 巴基斯坦 | 事实（用户表）|
| 网站/域名 | microtech.net.pk / hugebestvs.live | 事实（用户表 URL/邮箱域名） |
| 类型 | 巴基斯坦 IT 分销/集成（MikroTik 渠道） | 推断（据兴趣/备注关键词） |
| 联系人 | Noman Asghar | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 工业FS PoE 周边产品<br>有洪瑞的商业PoE V-sol的 / 洪瑞的商业POE | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | E已回复、用户判定不行 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | 洪瑞, FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-25）**　网站状态：未查
- **是谁**：Elsa 邮箱两线程 5 封：2025-06-04 对「10G Media Converter」回「These Product Are Not Available」（把我们当买家）；2026-05-11 对「10G Enterprise SFP Switch」回「Please find the attachment」= 他们自己的报价单 S10616：MikroTik CRS326-24S-2Q+RM PKR 165,500（≈US$590，另 18% 税）——反向对标，线程里无 Elsa 回复 = 我方欠答。用户表「用户判定不行」。
- **类型**：巴基斯坦 IT 分销/集成（MikroTik 渠道）
- **KP**：Noman Asghar（）info@microtech.net.pk / sales@microtech.net.pk 〔Elsa 邮箱〕
- 备注：（建档：第 77 批 C 薄切片，T29-U56；证据全部来自 Elsa 邮箱 `data/gmail_e/text/` + `index_replied.jsonl`）

### 加厚挖掘（2026-10-25 · 仅 Elsa 邮箱证据）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Microtech Inc |
| 总部/地址 | 巴基斯坦卡拉奇 |

- **触达通道（公开）**：role: 巴基斯坦 IT 分销/集成（MikroTik 渠道）；region: 巴基斯坦卡拉奇
- **风险/边界**：MikroTik 价位（24×10G SFP+ ≈ $590）Saga 10G 机型追不上；Simon 用户表已判「不行」
- **Saga 对位结论**：P1 STH-2C24XF-HSI（24×10G SFP+ + 2×100G）（None% 档）——只为交代反向报价；按群发价 $1,500 说清不是同级
- **邮件切入句（英文）**：（见 mail_review.draft_en）

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| 洪瑞 | 洪瑞 = HRUI（Saga 的 Realtek 辅线供应商） | 同源货：Saga STC Realtek 线（见 data/hrui_STC对照表.csv）可直接对型号报价 |
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 3 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-06-03 | 2025.6.3 | 群发了10GMC |  | E |  | E Replied 2026.08.04.xlsx#6 |
| 2025-06-21 | 621 | 28PoE |  | E |  | E Replied 2026.08.04.xlsx#6 |
| 2025-10-02 | 102 | dac |  | E |  | E Replied 2026.08.04.xlsx#6 |

## 联系方式（已有 · 原值照录）

- 邮箱：`info@microtech.net.pk`〔企业邮箱；来源：用户表原值〕
- 邮箱：`sales@microtech.net.pk`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Noman Asghar
- 网站/域名：microtech.net.pk
- 网站/域名：hugebestvs.live
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Noman Asghar | — | info@microtech.net.pk / sales@microtech.net.pk | 调研核实（公开页） | Elsa 邮箱 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:microtech.net.pk`, `e:info@microtech.net.pk`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E Replied 2026.08.04.xlsx#总表:7 | 6 | https://www.microtech.net.pk/ | 巴基斯坦 | Noman Asghar | 谷歌 | 工业FS PoE 周边产品<br>有洪瑞的商业PoE V-sol的 | info@microtech.net.pk<br>sales@microtech.net.pk |  | 3 条 |
| 不行及不太相关的.xlsx#总表:740 |  | https://hugebestvs.live/product_details/18071961.html | 巴基斯坦 |  | 谷歌 | 洪瑞的商业POE | info@microtech.net.pk |  | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：用户判定不行/不相关。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-2513,B,理由` 后重跑即可。

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
| 决策人识别 | ✅ |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ✅ 洪瑞, FS |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: 10G Enterprise SFP Switch

```text
Hello Noman,

Your quotation S10616 from 11 May (MikroTik CRS326-24S-2Q+RM, PKR 165,500 plus tax) sat in my inbox without an answer - apologies.

The two units are not the same class. The CRS326-24S-2Q+RM is 24 x 10G SFP+ with 2 x 40G; the unit I showed you is 24 x 1G SFP + 8 combo + 4 x 10G SFP+, an access/aggregation box at a fraction of that price. Our like-for-like 24 x 10G SFP+ unit is CENTEC-based - model STH-2C24XF-HSI, 24 x 10G SFP+ + 2 x 100G QSFP28, full L3 - at $1,500 USD EXW (MOQ 1, 15-day validity). That is above MikroTik money, so it only makes sense where 100G uplinks and the L3 feature set matter.

One question: was the CRS326 quoted for an ISP aggregation ring or an enterprise core? That tells me whether to send the 24 x 1G SFP price instead.

Thank you.
Elsa
Saga Telecom - sagatele.com
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- 不复核。对方主动来询 → 在 `data/saga_clients/人工定级.csv` 写一行升级后重跑。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 C，分数 -23）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
