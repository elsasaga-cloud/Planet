# Dema Vertriebs GmbH
**官方名称（调研核实）**：DEMA Vertriebs-GmbH（dema-vertrieb.com / dema-handel.net，Untermünkheim-Übrigshausen, DE）

> **评级 C**　|　德国　|　档案编号 `SB-126`　|　优先级 —　|　状态：有回复·跟进中
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：实质回复 1 次；推送 1 次（2025-07-10 → 2025-07-10）　|　**所在清单**：A已回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-126
rating: C
rating_auto: B
rating_research: C  # 2026-10-21 核实：DEMA 为五金/园艺/农用品电商与进口集团（Stabilo 连锁，>1,200 人、>€300M），无网络设备品类 → C（子原因
name_official: "DEMA Vertriebs-GmbH（dema-vertrieb.com / dema-handel.net，Untermünkheim-Übrigshausen, DE）"
score: 51
country: 德国
region: 欧洲
website: dema-vertrieb.com
type: 经销/集成（类型待核）
tier_tags: ["A已回复"]
deal: no
replies: 1
followups: 1
first_contact: 2025-07-10
last_contact: 2025-07-10
s_mail: 11 msgs (out 10 / in 1), 2025-04-14 -> 2026-03-30
p1: STC-28DGGPM
price_tier: 20%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：德国巴符州 Untermünkheim 的**五金/园艺/农用/车间用品**进口与电商集团公司（HRB 571318 Stuttgart；1963 年登记；注册资本 €800k；德国 100–249 人，集团含 Stabilo Fachmärkte 连锁 >1,200 人、>€300M 营收；自有品牌 DEMA / Fix Aktiv / Denner Edition；CEO Ulrich Abendschein）。品类与 PoE/工业交换机无关，且属大型集团——行业外 + 规模大。用户表：1 次实质回复，1 次跟进。（调研 2026-10-21；表内兴趣：两个公司名字，找PoE交换机，可以推荐工业级的）
- **为什么是 C 级**：**调研后定级 C**（2026-10-21 核实：DEMA 为五金/园艺/农用品电商与进口集团（Stabilo 连锁，>1,200 人、>€300M），无网络设备品类 → C（子原因：行业外 + 规模大））；自动分级 B：+22 实质回复 1 次；+18 在「已回复」名单（A/E Replied）；-25 邮件发不过去且无 WhatsApp 通道；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/德国；+5 最近活动 2025；C 级细分：调研后定级 C
- **历史互动**：实质回复 1 次；推送 1 次（2025-07-10 → 2025-07-10）；最近一次客户回复：2025-07-10：MOQ  8/24口的
- **P1**：不推（C 级）；若对方主动来询，起手 STC-28DGGPM（深挖对位：不推进；若其电商想增网络品类，按电商 20% 档报 STC-28DGGPM）
- **最大未知**：年走量与现供应商
- **下一步**：不动（C）；Simon 复核后再定 A 邮箱 —

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-126` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（2025-06-10 Alan 出全铜口工业系列报价单：STI-050FE $22.5 / STI-054FP $30 / STI-050GE $25 / STI-054GP $32.5 / STI-080FE $25.5 / STI-088FP $36.5；用户表「有回复·跟进中」；C 级人工定级不改）** ｜ 类型：德国分销商 Dema Vertriebs GmbH（Markus Geck） ｜ 筛子：2（要报价、已收报价单） ｜ 停点：报价后无记录（S/A 邮箱）；C 级 ｜ 复活：德国 = 四主之一；若 Simon 复核愿升 B，则按 2026-11 一句话回访 ｜ 通路：DE 未通 ｜ 节奏：最后 2025-06-10 报价单 ｜ 证据：A 邮箱外发报价单正文（`data/gmail_a/attachments/text/`，2026-10-24 对表）
- **现状一句话**：Alan 2025-06-09 群发 16 口 DIN 千兆铜口机 → Markus 次日回「very interesting. What are the purchase quantities and what is the price for the 8 and 24 switches?」→ Alan 当天给整表 + 长 datasheet，但没正面答「数量」→ 无回；其后 6 封群发（1U PoE、MINI、10G SFP $280、Booster、Alert、…）全无回。
- **对方真实需求（有据）**：5/8 口百兆与千兆工业非管理（PoE/非 PoE）整系列价格
- **断点 / 为什么停在这里**：报价后无回；C 级未再跟
- **Saga 现在该推什么**：P1 **STI-054GP / STI-088GP 级（HRUI 对照表列表价）**（20% 档，他见过的实报（2025-06-10 整表）：STI-080GE $32.5 / 088GP $43.5 / 0160GE $94.5 / 01616GP $125 / 0240GE $130（5 口 $22.5~32.5）；历史锚见 2025-06-10 报价单；现按 `列表价 USD EXW（2026-10-17 快照，15 天有效）`；群发里他已看到的价（续，第 66 批全量复核）：2025-05-12 $300（48 Port PoE Managed Switch）、2025-10-06 $280（10G Enterprise SFP Switch））——分销商 20% 档
- **下一步（具体）**：不动（C）；Simon 复核后再定　A 邮箱　—
  - 第一问（只问一个）：Markus — did the June-2025 copper industrial switch quotation go anywhere, or was it only for a price check?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-06-10 | 去 | Alan（Quotation_Copper Switch.pdf，Buyer Dema Vertriebs GmbH / Markus Geck，EXW Germany） | STI-050FE $22.5；STI-054FP $30；STI-050GE $25；STI-054GP $32.5；STI-080FE $25.5；STI-088FP $36.5（全铜口非管理工业系列，validity 15 days） | 德国分销商拿到的整表价（2025-06，老汇率） | `gmail_a att 2025-06-10` |
| 2025-06-10 | 来 | Markus Geck（Dema Vertriebs GmbH，德国） | Thank you very much for thinking of me. Yes, that is very interesting. What are the purchase quantities and what is the price for the 8 and 24 switches? | A 邮箱 2025-06 对 16 口机群发的真人回信：问 8 口与 24 口的起订量和价——Alan 当天回了全铜口工业系列报价单（见上一行）。C 级是人工定级（DEMA = 五金/园艺电商集团，行业外），不改；但这位 Markus 的询价是真的，留作「行业外个人兴趣」备注 | `gmail_a 2025-06-10 AW: 16 Port Ethernet Switch` |
| 2025-06-10 | 去 | Alan → Markus Geck（Re: 16 Port Ethernet Switch；附 Quotation_Copper Switch.pdf + STI-0160GE.pdf） | 全铜口工业非管理整表（Buyer: Dema Vertriebs GmbH）：STI-050FE $22.5 / 054FP $30 / 050GE $25 / 054GP $32.5 / 080FE $25.5 / 088FP $36.5 / **080GE $32.5 / 088GP $43.5 / 0160GE $94.5 / 01616GP $125 / 0240GE $130**（Marvell Chip，-40~75℃，DIN）；Alan 补充「24-port PoE 不常订所以没列，要的话需批量」+「请花时间读 STI-0160GE 的长 datasheet」。 | Markus 当天只问了两件事：**购买数量（MOQ）** 和 8 口/24 口的价——价给了，但「数量」这问题没有被正面回答（报价单备注里只有 validity/neutral/warranty）；他之后再没回，Alan 继续群发 6 封无回。德国户，重启时先把 MOQ 1 / 样品价说清 | `k=869ab8494c880aed（A 邮箱 2025-06-10 06:44Z）；附件 sha=9ffabb9a4b4a3787` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：C 级定级与「有回复·跟进中」状态矛盾，待 Simon 复核

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Dema Vertriebs GmbH | 事实（用户表） |
| 其他名称写法 | Stabilo-Markt Duisburg GmbH | 事实（用户表） |
| 国家 | 德国 | 事实（用户表）|
| 网站/域名 | dema-vertrieb.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Markus Geck / 发不过去 | 事实（用户表） |
| 来源（From） | 埃森展2024 | 事实（用户表） |
| 兴趣（Interested in） | 两个公司名字，找PoE交换机，可以推荐工业级的 | 事实（用户表） |
| 用户备注（Remark） | 49 151 10820 367 | 事实（用户表） |
| 所在清单 | A已回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：德国巴符州 Untermünkheim 的**五金/园艺/农用/车间用品**进口与电商集团公司（HRB 571318 Stuttgart；1963 年登记；注册资本 €800k；德国 100–249 人，集团含 Stabilo Fachmärkte 连锁 >1,200 人、>€300M 营收；自有品牌 DEMA / Fix Aktiv / Denner Edition；CEO Ulrich Abendschein）。品类与 PoE/工业交换机无关，且属大型集团——行业外 + 规模大。用户表：1 次实质回复，1 次跟进。
- **在卖/在用品牌**：DEMA / Fix Aktiv / Denner Edition（自有品牌，非网络）
- **【官网】业务与自有品牌**
  > Mit über 10 Jahren Erfahrung im Bereich des eCommerce vertreiben wir erfolgreich Produkte unter den Eigenmarken Dema, Fix Aktiv und Denner Edition. Unser hochwertiges Angebot können Sie in jedem Stabilo Baumarkt oder online in einem unserer eShops erwerben. Wir bieten alles für Handwerker, Monteure, Mechaniker und Heimwerker
  > 来源：http://dema-vertrieb.com/（抓取 2026-10-21）
- **【公司档案】注册信息与规模**
  > DEMA Vertriebs-GmbH Adresse: Im Tobel 4 74547 Untermünkheim … HR-Nummer: HRB 571318 … Gründung: 17.01.1963 … Kapital: 800.000,00 EUR … Mitarbeiter: 100-249
  > 来源：https://www.unternehmen24.info/Firmeninformationen/Deutschland/Firma/2364036（抓取 2026-10-21）
- **【集团站】集团规模**
  > Sie erwirtschaftet in Deutschland mit den Stabilo Fachmärkten über 300 Millionen Umsatz und beschäftigt im ganzen Konzern mehr als 1200 Angestellte. Dema Deutschland alleine beschäftigt 125 Personen.
  > 来源：https://dema-handel.ch/ueber-uns/（抓取 2026-10-21）
- **【用户表】1 次实质回复；1 次跟进**
  > （用户表字段）
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **调研后定级**：C（原自动 B）——2026-10-21 核实：DEMA 为五金/园艺/农用品电商与进口集团（Stabilo 连锁，>1,200 人、>€300M），无网络设备品类 → C（子原因：行业外 + 规模大）
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（公司档案核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | DEMA Vertriebs-GmbH |
| 总部/地址 | Im Tobel 4, 74547 Untermünkheim (Übrigshausen), Deutschland（+49 7944 98101-0；info@fixversand.de） |
| 注册/税号 | HRB 571318（Amtsgericht Stuttgart）· USt-ID DE146279485 · LEI 529900NC79L6B29H5354 |
| 其他 | 电商 10+ 年；自有品牌 DEMA、Fix Aktiv、Denner Edition；产品进 Stabilo 建材市场与多家网店 |

- **业务线**：五金/工具、园艺、农用、车间设备进口与自有品牌；Stabilo Fachmärkte 连锁与电商
- **触达通道（公开）**：网站: http://dema-vertrieb.com/ · https://dema-handel.net/
- **近况信号**：
  - 无网络设备品类；1 次回复可能为礼貌性
- **风险/边界**：行业外（DIY/园艺）+ 大集团采购流程——不符合 Saga 小单长期跟进模式
- **Saga 对位结论**：P1 STC-28DGGPM（20% 档）——不推进；若其电商想增网络品类，按电商 20% 档报 STC-28DGGPM
- **邮件切入句（英文）**：（不发送：行业外 + 大集团）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 1 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-07-10 | 2025.7.10 | 16电 | MOQ  8/24口的 | A |  | A Replied 09.04.xlsx#2 |

## 联系方式（已有 · 原值照录）

- 邮箱：`m.geck@dema-vertrieb.com`〔企业邮箱；用户备注含「发不过去」——发送前核对是哪一个地址；来源：用户表原值〕
- 电话：`+4915110820367`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Markus Geck / 发不过去
- 网站/域名：dema-vertrieb.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Markus Geck | — | m.geck@dema-vertrieb.com / +4915110820367 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发；备注含「发不过去」：发送前核对是哪一个地址，退信地址保留不删

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A Replied 09.04.xlsx#总表:3 | 2 | Dema Vertriebs GmbH<br>Stabilo-Markt Duisburg GmbH | 德国 | Markus Geck<br>发不过去 | 埃森展2024 | 两个公司名字，找PoE交换机，可以推荐工业级的 | m.geck@dema-vertrieb.com | 49 151 10820 367 | 1 条 |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：调研后定级 C。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SB-126,B,理由` 后重跑即可。

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
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

> C 级不出邮件样板（不主动跟进）。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- 不复核。对方主动来询 → 在 `data/saga_clients/人工定级.csv` 写一行升级后重跑。

## 变更日志

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 51）；人工/调研定级 → C

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
