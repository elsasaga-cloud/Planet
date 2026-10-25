# Computer Store Uganda Limited

> **评级 C**　|　乌干达　|　档案编号 `SC-111`　|　优先级 —　|　状态：名单内·未触达
>
> **类型**：IT 零售商（乌干达，延长器 RFQ）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：询盘流水　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-111
rating: C
rating_auto: B
rating_research: C  # 区域外且品类不供；c_sub=区域外/品类不符
score: 34
country: 乌干达
region: 非洲
website: computerstore.ug
type: IT 零售商（乌干达，延长器 RFQ）
tier_tags: ["询盘流水"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: none
price_tier: 20%
research: done
site_snapshot: timeout  # 2026-10-21
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：乌干达 Computer Store Uganda Limited（阿里巴巴 RFQ「工业 PoE Extender」；KP Wasswa Charles（Manager）；官网 timeout）；表内未跟进。（调研 2026-10-21；表内兴趣：—）
- **为什么是 C 级**：**调研后定级 C**（区域外且品类不供；c_sub=区域外/品类不符）；自动分级 B：+12 主动询盘（阿里巴巴/自建站/转介）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 非洲/乌干达；+5 最近活动 2025；C 级细分：区域外/品类不符
- **历史互动**：名单内·无互动记录
- **P1**：不推（C 级）；若对方主动来询，起手 STC-424DGGPM-280W（深挖对位：区域外、RFQ 品类 PoE 延长器（Saga 不供）→ 改 C）
- **最大未知**：具体需求型号（表内兴趣列为空）；官网当前状态异常（超时（站慢或封锁））——公司是否仍在运营待核
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Computer Store Uganda Limited | 事实（用户表） |
| 国家 | 乌干达 | 事实（用户表）|
| 网站/域名 | computerstore.ug | 事实（用户表 URL/邮箱域名） |
| 类型 | IT 零售商（乌干达，延长器 RFQ） | 推断（据兴趣/备注关键词） |
| 联系人 | Wasswa Charles, Manager | 事实（用户表） |
| 来源（From） | 2025.6.23 | 事实（用户表） |
| 兴趣（Interested in） | — | 事实（用户表） |
| 用户备注（Remark） | 工业PoE Extender / from: 阿里巴巴RFQ | 事实（用户表） |
| 所在清单 | 询盘流水 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：快照失败（timeout）
- **是谁**：乌干达 Computer Store Uganda Limited（阿里巴巴 RFQ「工业 PoE Extender」；KP Wasswa Charles（Manager）；官网 timeout）；表内未跟进。
- **类型**：IT 零售商（乌干达，延长器 RFQ）
- **【用户表】表内兴趣/备注**
  > 工业PoE Extender / from: 阿里巴巴RFQ
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【用户表】工业 PoE Extender RFQ**
  > 工业PoE Extender / from: 阿里巴巴RFQ
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **调研后定级**：C（原自动 B）——区域外且品类不供；c_sub=区域外/品类不符
- 备注：（无首轮调研；由 deepen.py 建档） ｜ 规则加厚 2026-10-21（autodeep.py；T 档 T5）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（人工复核：官网快照逐家核对 + 表内；T4/T5 信号优先））

| 公司事实 | 内容 |
|---|---|
| 总部/地址 | 乌干达 |
| 其他 | 官网 computerstore.ug，语言 ?，快照状态 timeout；角色判定来源：用户表 |

- **业务线**：IT 零售（乌干达）
- **触达通道（公开）**：role: IT 零售商（乌干达，延长器 RFQ）；region: 乌干达；contact: charles@computerstore.ug
- **近况信号**：
  - 表内：工业 PoE Extender / from: 阿里巴巴 RFQ；KP Wasswa Charles, Manager
  - 快照：timeout
- **风险/边界**：区域外（乌干达）；PoE 延长器品类 Saga 不供（Q-32）；官网 timeout
- **Saga 对位结论**：P1 待核型（无标准对应）（20% 档）——区域外、RFQ 品类 PoE 延长器（Saga 不供）→ 改 C
- **邮件切入句（英文）**：（不发送：区域外/品类）

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：超时（站慢或封锁））

- 尝试域名：computerstore.ug
  > https://computerstore.ug/ conn: HTTPSConnectionPool(host='computerstore.ug', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(
  > https://www.computerstore.ug/ timeout
  > http://computerstore.ug/ conn: HTTPSConnectionPool(host='computerstore.ug', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(
- **提示**：抓取失败不代表公司不在；人工打开一次即可。
- 数据文件：`data/saga_clients/site_snapshots/SC-111.json`

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`charles@computerstore.ug`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Wasswa Charles, Manager
- 网站/域名：computerstore.ug
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Wasswa Charles, Manager | — | charles@computerstore.ug | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 询盘统计表.xlsx#Sheet1:153 |  | Computer Store Uganda Limited | 乌干达 | Wasswa Charles, Manager | 2025.6.23 |  | charles@computerstore.ug 2022年使用国际站 | 工业PoE Extender from: 阿里巴巴RFQ | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：区域外/品类不符。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-111,B,理由` 后重跑即可。

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
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 具体需求型号（表内兴趣列为空）
- [ ] 官网当前状态异常（超时（站慢或封锁））——公司是否仍在运营待核
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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 34）；人工/调研定级 → C

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
