# Infotec Comercio de Equipamentos e Sistemas de Segurança Ltda.
**官方名称（调研核实）**：Infotec Comércio de Equipamentos e Sistemas de Segurança Ltda.（巴西；KP Fabian Alonzo，transivideo@gmail.com）

> **评级 B**　|　巴西　|　档案编号 `SB-1137`　|　优先级 ★★　|　状态：名单内·未触达
>
> **P 池并入（B 档，等级不动）：○ P 池 · 正式入池（资产池，终身跟进 + 每 2 个月巡检）**（批 AB-01 · 2026-10-29 · 下次巡检 2026-12-28）：○ P 池正式（P 正式候选，B 档并池 · 等级不动）：真回 ✔ + 对位 ✔ + 坐实 ✔；命中 3/6（成单/样品 — · 真回 ✔ · WA — · 对位 ✔ 交换机 · 登记 ✔ · 体量 微型 / 小型（ME；Sim）
>
> **类型**：巴西安防设备经销（CCTV）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：E冷名单(巴西)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1137
rating: B
rating_auto: C
sieve: pool  # 闸 3 AB1 2026-10-29
rating_research: B  # 两轮主动要价（2024-06、2024-11），规格明确（CCTV 用 8+2/16+2/24+2 PoE）；巴西非主攻 → B 慢慢跟进。
name_official: "Infotec Comércio de Equipamentos e Sistemas de Segurança Ltda.（巴西；KP Fabian Alonzo，transivideo@gmail.com）"
score: -2
country: 巴西
region: 拉美
website: none
type: 巴西安防设备经销（CCTV）
tier_tags: ["E冷名单(巴西)"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 20 msgs (out 16 / in 4), 2024-06-19 -> 2025-09-18
p1: STC-28DGGPM（8 PoE + 4 SFP，$99）/ STC-424DGGPM-280W（24 PoE + 4×2.5G SFP，$165）
price_tier: 20%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：S 邮箱 2024-06-25 三封来信：要 8+2 / 16+2 / 24+2 PoE 的型号与价（「lo más usado aquí」）、确认 19" 机架、问有无 VPN 设备；Simon 当日给报价单 + 规格书，答机架 OK / 无 VPN；2024-11-19 再要 4/8/16/24 口工业非管理价表 → 给了。此后无回。（调研 2026-10-24；表内兴趣：买的MC和机架 公司做: VC Switch和MC  工程）
- **为什么是 B 级**：**调研后定级 B**（两轮主动要价（2024-06、2024-11），规格明确（CCTV 用 8+2/16+2/24+2 PoE）；巴西非主攻 → B 慢慢跟进。）；自动分级 C：-6 E 冷名单（按国家群发）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+0 仅免费邮箱；-4 区域 拉美/巴西
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-28DGGPM $99 / STC-424DGGPM-280W $165 / 工业非管理 STI-154GP 级 — 已发资料（勿重发）：报价单 + 规格书(2024-06-25)、工业非管理价表(2024-11-20)｜档位说明（原 tier 字段文字「经销 20%」移此）：经销 20%；2024 报价单（老汇率 7.2，仓内未解析逐项）；再报按 2026-10 表；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-08-07 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-07；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170）
- **第一问（只问一个）**：Fabian — for the 8+2 / 16+2 / 24+2 PoE models you priced twice in 2024: what yearly volume and landed target price would make it work in Brazil? I will tell you honestly whether we can meet it.
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）
- **下一步**：2027-Q1 S 邮箱 → transivideo@gmail.com 首封前知悉：Elsa 2026-08-07 单发过「24 Port PoE Managed Switch」（未见回复（Elsa 箱 Replied 标签无））；一句话问 8+2/16+2/24+2 的年量与目标价（他两次要价都没说量）（第 76 批(b) 2026-10-25：audit_ab 硬错误修正：tier 字段规范为数字）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1137` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（S 邮箱 2024-06-25 ×3 + 2024-11-19：两轮要价，Simon 都当日给了；无后续）；Elsa 单发去信 1 封（2026-08-07「24 Port PoE Managed Switch」；To 本户、非 BCC；未见回复（Elsa 箱 Replied 标签无））（第 74 批(e) Elsa 箱 in:sent 排锚扫描）** ｜ 类型：CCTV 经销 ｜ 筛子：3（要价层面） ｜ 停点：两次拿到价表后沉默——价格/进口成本 ｜ 复活：一句话问 8+2/16+2/24+2 的年量与目标价；不发群发 ｜ 通路：巴西 非主攻 ｜ 节奏：半年 ｜ 证据：gmail_s 2024-06-25、2024-11-19/20；digest in 4
- **现状一句话**：巴西安防经销 Fabian 两次要价（CCTV 常用 8+2/16+2/24+2 PoE；工业非管理 4–24 口），都给了，没有下文。
- **对方真实需求（有据）**：CCTV 用 PoE 交换机价表（8+2/16+2/24+2）；工业非管理小机。
- **断点 / 为什么停在这里**：拿到价表后沉默；我们没问他的目标价和年量。
- **Saga 现在该推什么**：P1 **STC-28DGGPM $99 / STC-424DGGPM-280W $165 / 工业非管理 STI-154GP 级**（20% 档，2024 报价单（老汇率 7.2，仓内未解析逐项）；再报按 2026-10 表；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-08-07 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-07；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170））——已发资料（勿重发）：报价单 + 规格书(2024-06-25)、工业非管理价表(2024-11-20)｜档位说明（原 tier 字段文字「经销 20%」移此）：经销 20%
  - 复购/在买项：经；销；：；若；价；格；进；得；去；是；持；续；量
  - 做不了 / 要先核的：目；标；价；；；年；量；；；进；口；方；式
- **下一步（具体）**：2027-Q1　S 邮箱 → transivideo@gmail.com　首封前知悉：Elsa 2026-08-07 单发过「24 Port PoE Managed Switch」（未见回复（Elsa 箱 Replied 标签无））；一句话问 8+2/16+2/24+2 的年量与目标价（他两次要价都没说量）（第 76 批(b) 2026-10-25：audit_ab 硬错误修正：tier 字段规范为数字）
  - 第一问（只问一个）：Fabian — for the 8+2 / 16+2 / 24+2 PoE models you priced twice in 2024: what yearly volume and landed target price would make it work in Brazil? I will tell you honestly whether we can meet it.

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-06-25 | 来 | Fabian Alonzo | Puedes enviarme modelos y valores de switchs 8+2 Poe 16+2 PoE 24+2 Poe Esto es lo mas usado aqui en el mercado | 市场常用规格 | `rfq` |
| 2024-06-25 | 来 | Fabian Alonzo | Todos los modelos 8, 16 y 24 puertas tienen los soportes para Rack 19"? Tu tienes algun equipamiento de switch con posibilidad de hacer VPN? | 机架 + VPN（无） | `q` |
| 2024-06-26 | 去 | Simon | Yes, all the 3 models support 19" Rack mount… Sorry, we do not have any devices that could support/make a VPN. | 口径正确 | `reply` |
| 2024-11-19 | 来 | Fabian Alonzo | Can you send me your price list with the 4-8-16 and 24 door models? | 二次要价 | `rfq` |
| 2026-08-07 | out | Elsa → transivideo@gmail.com | 24 Port PoE Managed Switch（Elsa 2026 年 1:1 名单重发；To 仅本户；正文价 170usd/pc，第 74 批(p) 读稿 msg 1a05bfb71364077f） | 本户在 Elsa 的 1:1 名单里（非 BCC 批次）；未见回复（Elsa 箱 Replied 标签无） | `elsa_1to1` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：2024-06-25 报价单逐项价格（附件未解析）；公司规模

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 4 封（2024-06-25 → 2024-11-19）；多在 6 月（3）；对方本地时间中位 10:36，四分位 08:12–15:06（= 北京时间 21:36）；周二最多（4）；**他们回信中位 70.6 小时**（4 次，50% 在 24 小时内）；我方回信中位 4.9 小时（4 次）。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 10 封（2024-09-30 → 2025-09-18），打开标签 1 次（近 12 个月 0，最后 2024-11-19）；打开过：「Mini Industrial PoE Switch」×1（2024-11-19）；从未打开：「Industrial PoE Switch」、「8 Port Industrial PoE Switch」、「16 Port Ethernet Switch」；**最近连续 7 封没打开**（近 180 天发 0 封 0 打开）→ 群发对这户已失效，停两个月，改一句 1:1 或换收件人。
- **写信的人（来信签名机械抽取）**：Fabian Alonzo（transivideo@gmail.com，4 封，2024-06-25 → 2024-11-19）。
- **他们嘴里的词（4 封来信、去引用后 938 字符的词频）**：话题（次数，最近一次）：PoE ×3（2024-06-25）、光纤 / 媒体转换 ×1（2024-06-25）、价格 / 折扣 ×1（2024-11-19）。
- **渠道反应**：S 箱（Simon） 去 11（1:1 6 / 群发 5）回 4，最近回 2024-11-19；A 箱（Alan） 去 5（1:1 0 / 群发 5）回 0，从未回 → 只对 S 箱 Simon 有反应，下一封别换箱。
- **最后一球**：1:1 对话 2 段，最长一段 8 封 / 跨 55 天（2024-06-19 → 2024-08-14，「10G switch」）；最后一句是我们说的（2024-11-20，706 天前，「Re: Mini Industrial PoE Switch」，`f02f65b1e31a43e0`）→ 球在对方手里。
- **日历窗口**：对方：2026-11-15 共和国日；2026-12-24 圣诞–元旦 ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `gmail.com` → Google Workspace（MX：gmail-smtp-in.l.google.com、alt1.gmail-smtp-in.l.google.com、alt2.gmail-smtp-in.l.google.com、alt3.gmail-smtp-in.l.google.com）。Gmail → Gmail 同生态投递最稳；但 Gmail 图片代理会预抓像素 → 「已打开」偏高，别把 open 当成读过；三个发信箱别同一天给这个域发

**假日避让（巴西 · 按下一步「2027-Q1」窗口 2027-01-01→2027-03-31）：**

- 法定假日：01-01 Universal Fraternization Day；03-26 Good Friday —— 假日前一个工作日下午、当天、长假后第一个上午都别发
- 【惯例】12-21→01-03：圣诞-新年停摆：多数公司 12-21 起只剩值班，决策人 1-04 以后才回
- 【供应侧】01-25→02-21：我方供应侧春节停摆：SmartByte / HRUI 工厂约 2-01→2-17 放假，1-25 前不锁单的 2 月出不了货，节后出货排队到 2 月底；任何「现在要货」的客户 1 月中就得催 PI
- 【惯例】02-08→02-10：狂欢节（2-08/2-09 + 2-10 上午）

**公司底数 · 第 120 批（BR · 1 次检索：casadosdados.com.br/solucao/cnpj/…-05590805000156（INFOTEC COMERCIO DE EQUIPAMENTOS E SISTEMAS DE SEGURANCA LTDA；ATIVA；26/03/2003；SAO JOSE SC；ADMIN@INFOTECSISTEMAS.COM.BR；48 40529066；Simples 01/01/2009；EMA INES RODRIGUEZ RODRIGUEZ Sócio-Administrador 13/08/2009）+ cnpj.biz/05590805000237（filial Florianópolis；04/06/2010）+ jusbrasil 进口税诉讼列表；2026-10-29，2026-10-29 查；https://casadosdados.com.br/solucao/cnpj/infotec-comercio-de-equipamentos-e-sistemas-de-seguranca-ltda-05590805000156）：**

- 法定名 / 登记号：Infotec Comércio de Equipamentos e Sistemas de Segurança Ltda（**CNPJ 05.590.805/0001-56（总部 São José/SC，2003-03-26 开业，ATIVA，Simples 2009 起；分支 0002-37 Florianópolis 2010-06-04）；sócia-administradora Ema Ines Rodriguez Rodriguez（2009-08-13 入股）；admin@infotecsistemas.com.br；(48) 4052-9066；联邦法院 TRF4 多起进口税 / PIS-Cofins 进口案（2015–2018）→ 直接进口商**）→ 坐实；S 邮箱 2024-06 三封来信要 8+2 / 16+2 / 24+2 PoE 价，Simon 当日报价；2024-11 再要工业非管理 4/8/16/24 价表；未成；KP Fabian Alonzo（gmail） · CNPJ 05.590.805/0001-56（分支 0002-37） · 状态 **ATIVA（Simples）** · 成立 2003-03-26 · Ltda - ME
- 行业码 / 经营范围：安防设备与系统商贸（圣若泽 / 弗洛里亚诺波利斯，SC）
- 注册地址：São José - SC, Brazil（分支 Florianópolis - SC）
- 规模档：微型 / 小型（ME；Simples）
- 账目：未取；—
- 高管：Fabian Alonzo — 联系人（研究档 KP；transivideo@gmail.com）= 收件人
- 高管：Ema Ines Rodriguez Rodriguez — Sócia-Administradora（casadosdados 2026-10-29；admin@infotecsistemas.com.br 登记邮箱）
- 控制人 / 股东：未取
- **这意味着什么：**
  - **直接进口商（进口税诉讼可证）+ 两次主动要价未成 → 分销 20% B，一页纸一次（再报 STC-028GP $28 / STC-2216GP / STC-2224GP $86 现价 + STI-280GE $46.6 工业非管理 + MOQ 1；葡语备注；以 2024-06 报价为开场）— 巴西常规：英文稿（可附葡语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方清关、进口税自理；Anatel 不声称）**；回信 → 加厚 / 升 A 候选
- 备注：分销 20%；一页纸一次（预付 100%）；坐实（CNPJ + 法人 + 开业日 + 进口记录）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Infotec Comercio de Equipamentos e Sistemas de Segurança Ltda. | 事实（用户表） |
| 国家 | 巴西 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 巴西安防设备经销（CCTV） | 推断（据兴趣/备注关键词） |
| 联系人 | Mr. Fabian Alonzo | 事实（用户表） |
| 来源（From） | 朱姐转的 | 事实（用户表） |
| 兴趣（Interested in） | 买的MC和机架<br>公司做: VC Switch和MC  工程 | 事实（用户表） |
| 用户备注（Remark） | #51 4063-9602<br>加了Skype | 事实（用户表） |
| 所在清单 | E冷名单(巴西) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：（gmail 联系人；公司域未知）
- **是谁**：S 邮箱 2024-06-25 三封来信：要 8+2 / 16+2 / 24+2 PoE 的型号与价（「lo más usado aquí」）、确认 19" 机架、问有无 VPN 设备；Simon 当日给报价单 + 规格书，答机架 OK / 无 VPN；2024-11-19 再要 4/8/16/24 口工业非管理价表 → 给了。此后无回。
- **类型**：巴西安防设备经销（CCTV）
- **规模**：（未核）
- **【邮件】巴西最常用规格 8+2/16+2/24+2 PoE**
  > Puedes enviarme modelos y valores de switchs 8+2 Poe 16+2 PoE 24+2 Poe Esto es lo mas usado aqui en el mercado
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2024-06-25）
- **【邮件】二次要价表**
  > Can you send me your price list with the 4-8-16 and 24 door models?
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2024-11-19）
- **KP**：Fabian Alonzo（联系人（研究档；2024-06 / 2024-11 两次主动要价）= 收件人 — 一页纸一次：分销 20% B、以 2024-06 报价为开场再报 STC-028GP / STC-2216GP / STC-2224GP 现价 + STI-280GE 工业非管理 + MOQ 1；葡语备注；回信 → 升 A 候选 — 巴西常规：英文稿（可附葡语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（进口税自理）、Anatel 不声称（第 120 批 官方登记核实 2026-10-29））transivideo@gmail.com 51 98144-0559（信尾）〔data/gmail_a|gmail_s/messages/<year>/<month>.jsonl〕
- **KP**：Ema Ines Rodriguez Rodriguez（Sócia-Administradora（casadosdados 2026-10-29；2009-08-13 入股；登记邮箱）（第 120 批 官方登记核实 2026-10-29））admin@infotecsistemas.com.br 〔〕
- **调研后定级**：B（原自动 C）——两轮主动要价（2024-06、2024-11），规格明确（CCTV 用 8+2/16+2/24+2 PoE）；巴西非主攻 → B 慢慢跟进。
- 备注：西/葡语混写；要价都给了，没成——价格或进口门槛（巴西关税高）。

### 加厚挖掘（2026-10-24 · 邮件证据）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Infotec Comércio de Equipamentos e Sistemas de Segurança Ltda - ME（CNPJ 05.590.805/0001-56；分支 0002-37 Florianópolis；ATIVA；Simples 2009 起） |
| 成立 | 2003-03-26（分支 2010-06-04）（第 120 批 官方登记核实 2026-10-29） |
| 总部/地址 | São José - SC（分支 Florianópolis - SC；(48) 4052-9066）（第 120 批 官方登记核实 2026-10-29） |
| 其他 | 第 120 批：安防设备商贸 + TRF4 多起进口税 / PIS-Cofins 进口诉讼（2015–2018）→ 直接进口商；坐实（CNPJ + 法人 + 开业日 + 进口记录）（第 120 批 官方登记核实 2026-10-29） |

- **触达通道（公开）**：role: 经销；region: 巴西
- **风险/边界**：巴西进口税/清关——小量不划算；价格导向经销
- **Saga 对位结论**：P1 STC-28DGGPM（8 PoE + 4 SFP，$99）/ STC-424DGGPM-280W（24 PoE + 4×2.5G SFP，$165）（20% 档）——典型 CCTV 经销；两次要价后沉默 = 价格；只做季度问候
- **邮件切入句（英文）**：（见 mail_review.draft_en）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：20 封（去 16 / 来 4）　|　**期间**：2024-06-19 → 2025-09-18　|　**最后去信**：2025-09-18
- **对方邮箱**：transivideo@gmail.com
- **最后一封来信**：2024-11-19 transivideo@gmail.com「Re: Mini Industrial PoE Switch」：Good afternoon Simon, how are you? Can you send me your price list with the 4-8-16 and 24 door models? *Best regards,* *Fabian Alonzo* 51 98144-0559 Em ter., 19 de nov. de 2024 às 15:01, Simon <s.sagatelecom@gmail.com> escreveu:

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 90W PoE Managed Switch | 2025-09-18 | 2025-09-18 | 0 | 1 | 1 |
| 24 Port Fiber Switch | 2025-08-26 | 2025-08-26 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-07-17 | 2025-07-17 | 0 | 1 | 1 |
| 48 Port PoE Managed Switch | 2025-06-19 | 2025-06-19 | 0 | 1 | 1 |
| Marvell Alleycat5 Solution | 2025-03-14 | 2025-03-14 | 0 | 1 | 1 |
| Industrial PoE Switch | 2025-01-06 | 2025-01-06 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2024-12-11 | 2024-12-11 | 0 | 1 | 1 |
| Mini Industrial PoE Switch | 2024-11-19 | 2024-11-20 | 1 | 2 | 4 |
| 8 Port Industrial PoE Switch | 2024-10-23 | 2024-10-23 | 0 | 1 | 1 |
| Industrial PoE Switch | 2024-09-30 | 2024-09-30 | 0 | 1 | 1 |
| 10G switch | 2024-06-19 | 2024-08-14 | 3 | 5 | 16 |

## 联系方式（已有 · 原值照录）

- 邮箱：`transivideo@gmail.com`〔免费邮箱；来源：用户表原值〕
- 电话：`+5140639602`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Mr. Fabian Alonzo
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Fabian Alonzo | 联系人（研究档；2024-06 / 2024-11 两次主动要价）= 收件人 — 一页纸一次：分销 20% B、以 2024-06 报价为开场再报 STC-028GP / STC-2216GP / STC-2224GP 现价 + STI-280GE 工业非管理 + MOQ 1；葡语备注；回信 → 升 A 候选 — 巴西常规：英文稿（可附葡语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（进口税自理）、Anatel 不声称（第 120 批 官方登记核实 2026-10-29） | transivideo@gmail.com / 51 98144-0559（信尾） | 调研核实（公开页） | data/gmail_a\|gmail_s/messages/<year>/<month>.jsonl |
| Ema Ines Rodriguez Rodriguez | Sócia-Administradora（casadosdados 2026-10-29；2009-08-13 入股；登记邮箱）（第 120 批 官方登记核实 2026-10-29） | admin@infotecsistemas.com.br | 调研核实（公开页） | 调研 |
| Mr. Fabian Alonzo | — | transivideo@gmail.com / +5140639602 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；仅免费邮箱：可发，但优先找官网公开的企业邮箱（见调研 KP）

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/2026.08.04/巴西.xlsx#总表:20 | 19 | Infotec Comercio de Equipamentos e Sistemas de Segurança Ltda. | 巴西 | Mr. Fabian Alonzo | 朱姐转的 | 买的MC和机架<br>公司做: VC Switch和MC  工程 | transivideo@gmail.com | #51 4063-9602<br>加了Skype | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM（8 PoE + 4 SFP，$99）/ STC-424DGGPM-280W（24 PoE + 4×2.5G SFP，$165） | 深挖对位：典型 CCTV 经销；两次要价后沉默 = 价格；只做季度问候 | 价格待核（价格主表无此型号） | 深挖对位；档位 20%（巴西安防设备经销（CCTV）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：20% 档 $139.9 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），20% 档公式为 $181.2——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM（8 PoE + 4 SFP，$99）/ STC-424DGGPM-280W（24 PoE + 4×2.5G SFP，$165）），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-28DGGPM（8 PoE + 4 SFP，$99）/ STC-424DGGPM-280W（24 PoE + 4×2.5G SFP，$165） 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：名单内已有联系记录，不是零起点
- **W**：拉美：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-28DGGPM（8 PoE + 4 SFP，$99）/ STC-424DGGPM-280W（24 PoE + 4×2.5G SFP，$165） 按 20% 档报价，做现供应商的第二货源；规模（调研）：（未核）
- **T**：深圳同行（ONV / Utepo / 迈威等）价格战；汇率与海运波动吃掉 20–30% 的价差

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
| 触达通道 | ⚠️ 仅免费邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：8+2 / 16+2 / 24+2 PoE — volume and target price?

```text
Hi, Fabian,

You priced our 8+2 / 16+2 / 24+2 PoE switches twice in 2024 and we never heard what happened — usually that means the landed price did not work.

One question: what yearly volume and landed target price per unit would make it work in Brazil? With that I can tell you honestly whether we can meet it, instead of sending another price list.

Thank you.
Simon
Saga Telecom - sagatele.com
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-28**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-29：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 -2）；人工/调研定级 → B

---

*建档日期：2026-10-29　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
