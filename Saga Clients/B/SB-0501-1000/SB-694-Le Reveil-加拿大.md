# Le Reveil
**官方名称（调研核实）**：Le Reveil（加拿大渥太华区号 613；联系人 François Burton，Gmail）

> **评级 B**　|　加拿大　|　档案编号 `SB-694`　|　优先级 ★★　|　状态：回复暂无需求
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：回复暂无需求 1 次；WhatsApp 已加；推送 15 次（2024-06-27 → 2025-10-17）　|　**所在清单**：A优质名单(Canada)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-694
rating: B
rating_auto: B
name_official: "Le Reveil（加拿大渥太华区号 613；联系人 François Burton，Gmail）"
score: 33
country: 加拿大
region: 北美
website: none
type: 经销/集成（类型待核）
tier_tags: ["A优质名单(Canada)"]
deal: no
replies: 0
followups: 15
first_contact: 2024-06-27
last_contact: 2025-10-17
s_mail: 22 msgs (out 20 / in 2), 2024-06-17 -> 2026-03-05
p1: none
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：加拿大（电话 +1 613，渥太华地区）个人/小型需求方 François Burton（Gmail）：明确需求「8/12 个 SFP+ 甚至更高规格光口、不要网管(或不要电口)、工业级温度」；WhatsApp 已加、以邮件跟进为主，15 次跟进 0 回复。Saga 工业线最多 4×10G SFP+（STI-488DGGGM：8×1G SFP + 4×10G SFP+ + 8 GE），无 8/12 口 SFP+ 工业机型——待核型。（调研 2026-10-21；表内兴趣：8/12个SFP+甚至更高规格的光 不要网  工业级温度!!）
- **为什么是 B 级**：+6 有互动但表示暂无需求/已有供应商 1 次；+6 在 A/DONE 优质国家名单（已做过整轮推送）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+0 仅免费邮箱；+8 区域 北美/加拿大；+5 最近活动 2025
- **历史互动**：回复暂无需求 1 次；WhatsApp 已加；推送 15 次（2024-06-27 → 2025-10-17）；最近一次客户回复：2024-06-27：不需要网口 只需要光
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STH 系列半宽 10G — 已打开的主题（4/20 封有打开记录）：「Re: 48 port managed switch」(2024-06-18)、「Re: 48 port managed switch」(2024-06-24)、「24 port managed switch」(2024-08-14)、「90W PoE Managed Switch」(2024-11-14) → 读者兴趣偏「其他」；当前 P1 属「10G 汇聚/L3」，下一封按「其他」给，不按 P1｜已发资料（勿重发）：STC-120XGM(2024-06-18)、STC-448XGGMO(2024-06-18)、STI-4168XGGCM-U(2024-06-18)、Product Link_2026Q2(2026-03-05)；还没给过：7.5 Feature List、Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）；按 CENTEC 价表；群发里他已看到的价（续，第 66 批全量复核）：2024-12-11 $65（10G Media Converter）、2025-07-25 $300（48 Port PoE Managed Switch）、2025-08-29 $240（24 Port Fiber Switch）、2025-09-24 $280（10G Enterprise SFP Switch）
- **第一问（只问一个）**：François — a half-width 12×10G SFP+ / 12×25G, front-to-back airflow, L3 (VXLAN/EVPN): still relevant?
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）
- **下一步**：2026-11 S 邮箱 → francois.burton0@gmail.com（回 2024 「48 port managed switch」原串） 只发 CENTEC；回原串沿用原主题（邮件客户端自动加 Re:），上面的主题只在另起新信时用

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-694` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（2024-06 两封：「any SFP/SFP+ switches only? No need for copper」→「looking for SFP+ ports with ventilation front to back」；Saga 无前后风道全 SFP+ 款；之后 18 封群发无回；Elsa 箱：`to:francois.burton0@gmail.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 20 / 来 2）（第 74 批(h)））** ｜ 类型：加拿大小型网络/托管（Gmail 个人） ｜ 筛子：2 ｜ 停点：规格：全 SFP+ + 前后风道（数据中心口径）——AC5 线没有；CENTEC STH-2C12XF12XE 类有 ｜ 复活：若发，只发 CENTEC 半宽 10G/25G ｜ 通路：CA ｜ 节奏：一封 ｜ 证据：k=2974def9d7ffbd3f / 75e864d4417eab48；第 19 批回补来信原文 1 条（gmail_s/gmail_a）
- **现状一句话**：需求是数据中心 ToR 口径。
- **对方真实需求（有据）**：全 SFP+，前后风道。
- **断点 / 为什么停在这里**：产品线。
- **Saga 现在该推什么**：P1 **STH 系列半宽 10G**（25% 档，按 CENTEC 价表；群发里他已看到的价（续，第 66 批全量复核）：2024-12-11 $65（10G Media Converter）、2025-07-25 $300（48 Port PoE Managed Switch）、2025-08-29 $240（24 Port Fiber Switch）、2025-09-24 $280（10G Enterprise SFP Switch））——已打开的主题（4/20 封有打开记录）：「Re: 48 port managed switch」(2024-06-18)、「Re: 48 port managed switch」(2024-06-24)、「24 port managed switch」(2024-08-14)、「90W PoE Managed Switch」(2024-11-14) → 读者兴趣偏「其他」；当前 P1 属「10G 汇聚/L3」，下一封按「其他」给，不按 P1｜已发资料（勿重发）：STC-120XGM(2024-06-18)、STC-448XGGMO(2024-06-18)、STI-4168XGGCM-U(2024-06-18)、Product Link_2026Q2(2026-03-05)；还没给过：7.5 Feature List、Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）
- **下一步（具体）**：2026-11　S 邮箱 → francois.burton0@gmail.com（回 2024 「48 port managed switch」原串）　只发 CENTEC；回原串沿用原主题（邮件客户端自动加 Re:），上面的主题只在另起新信时用
  - 第一问（只问一个）：François — a half-width 12×10G SFP+ / 12×25G, front-to-back airflow, L3 (VXLAN/EVPN): still relevant?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-06-17 | 来 | francois.burton0@gmail.com | No thanks... any SFP/SFP+ switches only? No need for copper... | 来信原文（主题「Re: 48 port managed switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `2974def9d7ffbd3f` |
| 2024-06-18 | 去 | Saga（Simon） | Hi, Francois, Thanks for your reply. We got 2 commercial models. 1, Realtek chip, 12 port SFP+, L2 managed 2, Marvell chip, 4 port SFP+ and 48 port SFP, L3 managed There is a Marvell based industrial model FYI. Its 4 port SFP+ and 16 port SFP+8*1G SFP/RJ45, L3 managed Please see attached datasheets… | Saga 实质答复原文（主题「Re: 48 port managed switch」；第 20 批从 gmail_s 回补）——承诺/口径以此为准 | `9c34ff9a98f0c773` |
| 2024-06-24 | 来 | François Burton | Not really, looking for SFP+ ports with ventilation front to back. | 规格 | `75e864d4417eab48` |
| 2024-09-09 | 去 | Saga（Simon） | Hi, Francois, How are you? We are now introducing a new series, high-speed switches. Previously you said you need a switch that just has fiber ports. Please check this one. 32*100G We have many other specifications. Please let me know if this is useful to you.… | Saga 实质答复原文（主题「Re: 24 port managed switch」；第 20 批从 gmail_s 回补）——承诺/口径以此为准 | `5b93217dc580dc09` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Le Reveil | 事实（用户表） |
| 国家 | 加拿大 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Francois Burton | 事实（用户表） |
| 来源（From） | alibaba RFQ | 事实（用户表） |
| 兴趣（Interested in） | 8/12个SFP+甚至更高规格的光<br>不要网  工业级温度!! | 事实（用户表） |
| 用户备注（Remark） | 1 - 613 - 322 3444<br>已加 邮件跟进为主 | 事实（用户表） |
| 所在清单 | A优质名单(Canada) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：无域名（仅表内信息）
- **是谁**：加拿大（电话 +1 613，渥太华地区）个人/小型需求方 François Burton（Gmail）：明确需求「8/12 个 SFP+ 甚至更高规格光口、不要网管(或不要电口)、工业级温度」；WhatsApp 已加、以邮件跟进为主，15 次跟进 0 回复。Saga 工业线最多 4×10G SFP+（STI-488DGGGM：8×1G SFP + 4×10G SFP+ + 8 GE），无 8/12 口 SFP+ 工业机型——待核型。
- **【用户表】需求：8/12×SFP+ 以上光口、工业级温度；WhatsApp 已加、邮件跟进为主；15 次跟进 0 回复**
  > 8/12个SFP+甚至更高规格的光 不要网 工业级温度!!
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Francois Burton（询盘人（2024-06 回「No thanks… any SFP/SFP+ switches only?」，只要 SFP+ 口、前后通风））francois.burton0@gmail.com 〔S 邮箱 2024-06-17 / 06-24 来信表头〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · 无域名 · 仅表内信息（需求已映射））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Le Reveil（表内名称；未能核实法人） |
| 总部/地址 | 加拿大（+1 613 渥太华区号） |

- **业务线**：未知（需求为工业级多 SFP+ 光口交换机）
- **触达通道（公开）**：邮箱: （表内 Gmail）；WhatsApp: 已加
- **近况信号**：
  - 需求具体（8/12×SFP+、工业温度）→ 若有 10G 光口密集机型可成单
- **风险/边界**：Saga 工业线 SFP+ 最多 4 口；15 次跟进 0 回复
- **Saga 对位结论**：P1 待核型（无标准对应）（25% 档）——待核型：最接近 STI-488DGGGM（8×1G SFP + 4×10G SFP+ + 8 GE，−40~+75 ℃，$332.6 @25%）或 STI-4168XGGCM-U（16×1G SFP + 8 Combo + 4×10G，$495.1）；纯 10G 多口需向 SmartByte 核 LT-IS65xx 系列是否有 8/12×SFP+ 型号
- **邮件切入句（英文）**：François — a half-width 12×10G SFP+ / 12×25G, front-to-back airflow, L3 (VXLAN/EVPN): still relevant?

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 15 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2024-06-27 | 2024.6.27 | 群发了48口引流信息 | 不需要网口 只需要光 | Email |  | Canada 3.5.xlsx#32 |
| 2024-07-17 | 2024.7.17 | 1光8 2.5G |  | Email |  | Canada 3.5.xlsx#32 |
| 2024-08-14 | 2024.8.14 | 工业24光combo |  | Email |  | Canada 3.5.xlsx#32 |
| 2024-09-09 | 2024.9.9 | 核心交换机图问需求 |  | Email |  | Canada 3.5.xlsx#32 |
| 2024-10-15 | 1015 | PC |  | Email |  | Canada 3.5.xlsx#32 |
| 2024-11-15 | 1115 | 28bt |  | Email |  | Canada 3.5.xlsx#32 |
| 2024-12-12 | 1212 | 10gmc |  | Email |  | Canada 3.5.xlsx#32 |
| 2025-01-04 | 1.4 | 16电 |  | Email |  | Canada 3.5.xlsx#32 |
| 2025-03-07 | 2025.3.7 | 4 24 |  | A |  | Canada 3.5.xlsx#32 |
| 2025-05-27 | 527 | bypass |  | A |  | Canada 3.5.xlsx#32 |
| 2025-06-27 | 627 | alarm |  | A |  | Canada 3.5.xlsx#32 |
| 2025-07-25 | 725 | 48口 |  | A |  | Canada 3.5.xlsx#32 |
| 2025-08-29 | 829 | 24fiber |  | A |  | Canada 3.5.xlsx#32 |
| 2025-09-24 | 924 | dac |  | A |  | Canada 3.5.xlsx#32 |
| 2025-10-17 | 1017 | 22mini |  | A |  | Canada 3.5.xlsx#32 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：22 封（去 20 / 来 2）　|　**期间**：2024-06-17 → 2026-03-05　|　**最后去信**：2026-03-05
- **对方邮箱**：francois.burton0@gmail.com
- **最后一封来信**：2024-06-24 francois.burton0@gmail.com「Re: 48 port managed switch」：Not really, looking for SFP+ ports with ventilation front to back.

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Updated Ethernet Switches Links | 2026-03-05 | 2026-03-05 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-29 | 2026-01-29 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2026-01-02 | 2026-01-02 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-21 | 2025-11-21 | 0 | 1 | 1 |
| Mini Industrial PoE Switch | 2025-10-17 | 2025-10-17 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-09-24 | 2025-09-24 | 0 | 1 | 1 |
| 24 Port Fiber Switch | 2025-08-29 | 2025-08-29 | 0 | 1 | 1 |
| 48 Port PoE Managed Switch | 2025-07-25 | 2025-07-25 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-06-26 | 2025-06-26 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-05-27 | 2025-05-27 | 0 | 1 | 1 |
| L3 Managed Switch | 2025-03-06 | 2025-03-06 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-01-03 | 2025-01-03 | 0 | 1 | 1 |
| …共 17 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 联系方式（已有 · 原值照录）

- 邮箱：`francois.burton0@gmail.com`〔免费邮箱；来源：用户表原值〕
- 电话：`+16133223444`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Francois Burton
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Francois Burton | 询盘人（2024-06 回「No thanks… any SFP/SFP+ switches only?」，只要 SFP+ 口、前后通风） | francois.burton0@gmail.com | 调研核实（公开页） | S 邮箱 2024-06-17 / 06-24 来信表头 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；邮件已推送 15 次无回复 → 换通道（电话 / LinkedIn / 官网表单），不要再发同模板

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/Canada 3.5.xlsx#总表:33 | 32 | Le Reveil | 加拿大 | Francois Burton | alibaba RFQ | 8/12个SFP+甚至更高规格的光<br>不要网  工业级温度!! | francois.burton0@gmail.com | 1 - 613 - 322 3444<br>已加 邮件跟进为主 | 15 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | 待核型（无标准对应，向 SmartByte 核） | 深挖对位：待核型：最接近 STI-488DGGGM（8×1G SFP + 4×10G SFP+ + 8 GE，−40~+75 ℃，$332.6 @25%）或 STI-4168XGGCM-U（16×1G SFP + 8 Combo + 4×10G，$495.1）；纯 10G 多口需向 SmartByte 核 LT-IS65xx 系列是否有 8/12×SFP+ 型号 | — | 深挖对位；档位 25%（经销/集成（类型待核）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-424DGGPM-280W 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：WhatsApp 直达；北美主攻区，复购与口碑可外溢
- **W**：已推送 15 次无回复，邮件通道疲劳
- **O**：P1 — 按 25% 档报价，做现供应商的第二货源
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
| 触达通道 | ✅ WhatsApp 已加 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：SFP+ switch with front-to-back airflow

```text
Hi, Francois,

In June 2024 you said what you need is SFP+ ports with front-to-back ventilation, and we had nothing to offer. Now there is a CENTEC-based L3 unit: 24x 10G SFP+ + 2x 100G QSFP28, front-to-rear airflow, hot-swap PSU, VXLAN/EVPN/MPLS; indicative price around $1,250 USD EXW for the DC/MA-license version (project quote, 15 days validity).

One question: is this still relevant for your racks, and is it AC or DC power?

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

- **2026-11-24**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 33）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
