# lanberg.pl

> **评级 B**　|　波兰　|　档案编号 `SB-574`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：波兰 IT 配件品牌商（Lanberg，OEM 采购；体量较大）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：群发(筛选后质量一般的_群发)、表:PL　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-574
rating: B
rating_auto: B
score: 37
country: 波兰
region: 欧洲
website: lanberg.pl
type: 波兰 IT 配件品牌商（Lanberg，OEM 采购；体量较大）
tier_tags: ["群发(筛选后质量一般的_群发)", "表:PL"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 6 msgs (out 6 / in 0), 2024-06-25 -> 2024-11-21
p1: STC-28DGGPM
price_tier: 30%
research: done
site_snapshot: http_error  # 2026-10-21
sources: 1
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：波兰 Lanberg（IT 配件品牌（Impakt S.A. 旗下）：PoE 设备、商用 FS、周边，自有 logo；官网快照 HTTP 错误；表内「质量一般」；邮箱 export@）；表内未跟进。（调研 2026-10-21；表内兴趣：PoE设备 商业FS 周边产品 自己的logo）
- **为什么是 B 级**：-6 群发批次名单；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/波兰
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-25）**：STC-28DGGPM（研究档） — 自有品牌 + 体量；按主表 OEM 30% 档；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-07-22 $65（10G media converter）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2025-10-09 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 1 轮 2025-10-09；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：官网当前状态异常（HTTP 错误）——公司是否仍在运营待核
- **下一步**：随 SA-050 A 邮箱 → lukasz.gasiewicz@impakt.com.pl 并档；不再对 support@lanberg.pl 群发

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-25）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-574` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-25。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：同一集团见 SA-050（Lanberg = Impakt S.A. 旗下品牌）：A 邮箱 19 封群发 0 回，但 E 邮箱 2025-08-25 收到 support@lanberg.pl 对「90W PoE Managed Switch」的回复并转给 lukasz.gasiewicz@impakt.com.pl——Lanberg 的采购在 Impakt；Elsa 群发 BCC 已触达 2025-10-09「10G Enterprise SFP Switch」（正文「Price: 280usd/pc」，第 74 批(p) 读稿），PL-3（大分销 aat/lanberg/elmark/dipol/a2s） 批次 To info@axuse.com，0 回（第 74 批 Bcc 头核对 msg 199c8653559f6d15）** ｜ 类型：波兰 IT 配件品牌（Lanberg；Impakt S.A. 旗下，OEM 采购，体量大） ｜ 筛子：2（support@ 读信并内部转交） ｜ 停点：support@ 不是采购；真正的对口在 Impakt（SA-050 已有绑定线） ｜ 复活：并入 SA-050 跟进，不单独群发 ｜ 通路：PL 次级（但 OEM 品牌商 = 目标第一档） ｜ 节奏：随 SA-050 ｜ 证据：E 邮箱 index_replied 2025-08-25 support@lanberg.pl → lukasz.gasiewicz@impakt.com.pl；A 邮箱 out 19 / 0 回；data/gmail_e/bcc_batches_2026.json；批次时间线：同批次（To info@axuse.com）本户见于 2025-10-09 名单；该批次最早 2025-04-03 起共 7 轮，更早轮次 Bcc 未读
- **现状一句话**：Lanberg 是 Impakt 的自有品牌；A 邮箱对 lanberg.pl 群发 19 封无回，E 邮箱在 2025-08-25 收到 support@lanberg.pl 的回复，内容是把 Saga 的 90W PoE 信转给 Impakt 的 Łukasz Gąsiewicz。这说明两户是同一个采购体系。
- **对方真实需求（有据）**：见 SA-050。
- **断点 / 为什么停在这里**：双档并行。
- **Saga 现在该推什么**：P1 **STC-28DGGPM（研究档）**（30% 档，按主表 OEM 30% 档；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-07-22 $65（10G media converter）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2025-10-09 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 1 轮 2025-10-09；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档））——自有品牌 + 体量
- **下一步（具体）**：随 SA-050　A 邮箱 → lukasz.gasiewicz@impakt.com.pl　并档；不再对 support@lanberg.pl 群发

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-08-25 | 来（E 邮箱） | Support Lanberg | RE: [EXTERNAL] 90W PoE Managed Switch（转 lukasz.gasiewicz@impakt.com.pl） | Lanberg 采购在 Impakt | `gmail_e/index_replied` |
| 2025-10-09 | 去 | Elsa 群发（BCC；To info@axuse.com，PL-3（大分销 aat/lanberg/elmark/dipol/a2s） 批次） | 10G Enterprise SFP Switch — This is our 24-port Marvell-based managed SFP switch. 1, 4 port 1G SFP+8-port 1G SFP/RJ45 Combo +4*10G SFP+ 2, Dual AC input 3, Support fan monitoring（正文价 280usd/pc，第 74 批(p) 读稿 msg 19984c1d62ba38d6 / 19df5ef64e6ba213） | Elsa 箱群发 BCC 触达证据（命中地址 export@lanberg.pl, lanberg.pl, support@lanberg.pl）；S/A digest 看不到 Elsa 的 BCC，之前据此写的「未发信/未触达」不成立 | `elsa_bcc` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：E 邮箱该信正文未入库（仅索引）

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **发信窗口（PL 全库 585 封群发的打开标签，对方本地时间；均值 5.5%）**：周四 12–14 点 4.8%（42 封）、周五 10–12 点 2.4%（41 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 6 封（2024-06-25 → 2024-11-21），打开标签 0 次；**最近连续 6 封没打开**（近 180 天发 0 封 0 打开）→ 群发对这户已失效，停两个月，改一句 1:1 或换收件人。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 0 条 + 个性化群发价 1 条，2024-07-22 → 2024-07-22；「今天」= 价格主表 2026-10-17 汇率、30% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2024-07-22 | 「Price: 65usd/pc, 1×10G SFP+1×100M/1G/2.5G/10G Ethernet, unmanaged, non」 | $65 | —（原句无型号） | — | 群发价 | 10G media converter | `efc2205da3206b1c` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **同国同档参照（PL，30% 档、主推线「商用 2.5G PoE 管理型」，共 2 户有动静，列前 3）**：SA-023 fcnet.pl（A，同线：回过 2 次（最近 2025-04-22））；SA-050 impakt.com.pl（A，同档：回过 2 次（最近 2025-10-03））。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-11-11 独立日；2026-12-24 圣诞–元旦 ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | lanberg.pl（取自域名，公司全名待核） | 推断 |
| 国家 | 波兰 | 事实（用户表）|
| 网站/域名 | lanberg.pl | 事实（用户表 URL/邮箱域名） |
| 类型 | 波兰 IT 配件品牌商（Lanberg，OEM 采购；体量较大） | 推断（据兴趣/备注关键词） |
| 联系人 | 质量一般 | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | PoE设备 商业FS 周边产品<br>自己的logo | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | 群发(筛选后质量一般的_群发)、表:PL | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：快照失败（http_error）
- **是谁**：波兰 Lanberg（IT 配件品牌（Impakt S.A. 旗下）：PoE 设备、商用 FS、周边，自有 logo；官网快照 HTTP 错误；表内「质量一般」；邮箱 export@）；表内未跟进。
- **类型**：波兰 IT 配件品牌商（Lanberg，OEM 采购；体量较大）
- **【用户表】表内兴趣/备注**
  > PoE设备 商业FS 周边产品 自己的logo
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【用户表】PoE 设备 商业 FS 自己的 logo**
  > PoE设备 商业FS 周边产品 自己的logo；质量一般
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- 备注：（无首轮调研；由 deepen.py 建档） ｜ 规则加厚 2026-10-21（autodeep.py；T 档 T4）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（人工复核：官网快照逐家核对 + 表内；T4/T5 信号优先））

| 公司事实 | 内容 |
|---|---|
| 总部/地址 | 波兰 |
| 其他 | 官网 lanberg.pl，语言 ?，快照状态 http_error；角色判定来源：用户表 |

- **业务线**：IT 配件 / 网络产品（品牌 Lanberg）
- **触达通道（公开）**：role: 波兰 IT 配件品牌商（Lanberg，OEM 采购；体量较大）；region: 波兰；contact: support@lanberg.pl、export@lanberg.pl
- **近况信号**：
  - 表内：PoE 设备 商业 FS 周边产品 自己的 logo；质量一般；邮箱 support@ / export@
  - 快照：lanberg.pl http_error
- **风险/边界**：体量较大（Impakt S.A. 旗下品牌，既定 ODM 体系）；官网快照 HTTP 错误；表内「质量一般」；未跟进过
- **Saga 对位结论**：P1 STC-28DGGPM（30% 档）——自有 Lanberg 标 PoE/商用 FS → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$87.4 @30%）；非管理 5/8/16 口位 HRUI（列表价，注明）
- **邮件切入句（英文）**：For the PoE and unmanaged switches in the Lanberg range, we can be an ODM source on a Marvell platform (8-PoE + 2 SFP L2+, 24-PoE + 4 SFP) plus budget 5/8/16-port units in your retail packaging from small lots, CE/RoHS — which switch SKU sells most through your distribution?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：HTTP 错误）

- 尝试域名：lanberg.pl
  > https://lanberg.pl/ http 403 ct=text/html; charset=utf-8
  > https://www.lanberg.pl/ http 403 ct=text/html; charset=utf-8
  > http://lanberg.pl/ http 403 ct=text/html; charset=utf-8
- **提示**：抓取失败不代表公司不在；人工打开一次即可。
- 数据文件：`data/saga_clients/site_snapshots/SB-574.json`

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：6 封（去 6 / 来 0）　|　**期间**：2024-06-25 → 2024-11-21　|　**最后去信**：2024-11-21
- **对方邮箱**：export@lanberg.pl、support@lanberg.pl
- 对方从未回信（全部为我方去信）
- **邮件里报过的价**：2024-07-22 $65

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Industrial PoE Switch | 2024-11-21 | 2024-11-21 | 0 | 1 | 1 |
| 24 Port Passive PoE Switch | 2024-10-30 | 2024-10-30 | 0 | 1 | 1 |
| 8 Port Ethernet Switch | 2024-09-11 | 2024-09-11 | 0 | 1 | 1 |
| 2.5G switch | 2024-08-18 | 2024-08-18 | 0 | 1 | 1 |
| 10G media converter | 2024-07-22 | 2024-07-22 | 0 | 1 | 1 |
| cctv poe switch | 2024-06-25 | 2024-06-25 | 0 | 1 | 1 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-26T07:56:19Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-574/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://lanberg.pl/) | html | HTTP 403 | 2026-10-23T04:20:51Z | 官网首页（T27 快照状态 http_error） |

## 联系方式（已有 · 原值照录）

- 邮箱：`support@lanberg.pl`〔企业邮箱；来源：用户表原值〕
- 邮箱：`export@lanberg.pl`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：质量一般
- 网站/域名：lanberg.pl
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| —（未具名） | 公司级 | support@lanberg.pl / export@lanberg.pl | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/群发/筛选后质量一般的_群发.xlsx#PL:24 | 23 | https://lanberg.pl/en/kategoria/SKA-SWI | 波兰 | 质量一般 | 谷歌 | PoE设备 商业FS 周边产品<br>自己的logo | support@lanberg.pl<br>export@lanberg.pl |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：自有 Lanberg 标 PoE/商用 FS → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$87.4 @30%）；非管理 5/8/16 口位 HRUI（列表价，注明） | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（波兰 IT 配件品牌商（Lanberg，OEM 采购；体量较大）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：自有品牌/贴牌需求 = 现成 OEM 客户；欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-28DGGPM 按 30% 档报价，做现供应商的第二货源；贴牌 + 定制 UI/型号 → 30% 档与长期绑定
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
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ✅ FS |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 官网当前状态异常（HTTP 错误）——公司是否仍在运营待核
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-28DGGPM - 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks (Marvell-based, neutral label)

```text
Hello,

Some time ago you had a product mail from us - "10G Enterprise SFP Switch" on 9 October 2025 - and there was no reason to answer a mass mail. This one is specific. For the PoE and unmanaged switches in the Lanberg range, we can be an ODM source on a Marvell platform (8-PoE + 2 SFP L2+, 24-PoE + 4 SFP) plus budget 5/8/16-port units in your retail packaging from small lots, CE/RoHS — which switch SKU sells most through your distribution?

We supply a Marvell-based 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks - model STC-28DGGPM - that fits the same slot as the units you source today at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $87.4 USD EXW (price snapshot 2026-10-17, valid 15 days).

If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.

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

- **2026-11-26**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 37）

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
