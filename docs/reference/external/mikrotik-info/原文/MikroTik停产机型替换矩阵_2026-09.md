# MikroTik 停产（EOL）机型替换矩阵

> **为什么这份表是最高 ROI 的获客资产**
> 客户不换品牌，往往不是因为满意，而是因为**还没到必须换的时候**。
> 原型号停产 = 备件断供 = 扩容买不到 = **他必须现在做决定**。
> 这是唯一一种"不需要说服、对方自己有痛点"的场景。

---

## 0. 置信度声明（先读这个）

MikroTik **没有统一的官方 EOL 公告页**，网上流传的"EOL 清单"质量参差。

**本次采信标准：至少两个独立来源一致。**

| 来源 | 性质 | 权重 |
|---|---|---|
| `mikrotik-store.eu/en/archive-discontinued` | **MikroTik 官方分销商**的停产清仓页 | 高 |
| `cloudrouterswitches.com/mikrotik-eol.asp` | 经销商 EOL 清单 | 中高 |
| `linknewnet.com/blog/mikrotik-eol-equipment-complete-list` | **二手设备 SEO 博客** | ❌ **不采信** |

> ⚠️ **已排除的错误信息**：linknewnet 那篇把 **CRS326 / CRS328 / CRS520 列为 EOL**。
> 这三款目前仍在正常销售，是**当代主力**，不是停产型号。
> 该文写的是"我们常供货的型号"，不是 EOL —— **典型的 SEO 博客把"我们卖二手"包装成"官方停产"**。
> 如果你拿这个去跟客户说"你的 CRS328 停产了"，**当场就会被打脸**。

---

## 1. 交叉验证确认的停产交换机型号

| 停产型号 | 端口形态 | 定位 | 双源确认 |
|---|---|---|---|
| **CRS125-24G-1S-IN / -RM** | 24×GbE + 1×SFP | 早期接入 | ✅ |
| **CRS125-24G-1S-2HnD-IN** | 24×GbE + 1×SFP + AP | 早期接入（带无线） | ✅ |
| **CRS226-24G-2S+IN / -RM** | 24×GbE + 2×SFP+ | 早期万兆上行接入 | ✅ |
| **CRS210-8G-2S+IN** | 8×GbE + 2×SFP+ | 小型万兆上行 | ✅ |
| **CRS212-1G-10S-1S+IN** | 1×GbE + 10×SFP + 1×SFP+ | 光纤汇聚 | ✅ |
| **CRS112-8G-4S-IN** | 8×GbE + 4×SFP | 小型接入 | ✅ |
| **CRS109-8G-1S-2HnD-IN** | 8×GbE + 1×SFP + AP | SOHO 一体机 | ✅ |
| **RB260GS** | 5×GbE + 1×SFP | 桌面智能交换 | ✅ |
| **RB260GSP** | 5×GbE（PoE 输出）+ 1×SFP | 桌面 PoE 智能交换 | ✅ |

> 同批停产的还有 **RB2011 系列、CCR1009/1016/1036 系列**（路由器，不在我们替换范围）、
> **SXT 系列**无线（同样不替换）。

---

## 2. 替换矩阵（停产型号 → SmartByte）

| 停产型号 | SmartByte 替换 | 端口对比 | 进价 RMB | 匹配度 | 话术要点 |
|---|---|---|---|---|---|
| CRS125-24G-1S | `LT-S8328G-4GX24GT-S` | 1×SFP → **4×1G/2.5G SFP** | **460** | ★★★★★ | 上行从 1 口变 4 口，还便宜 |
| CRS226-24G-2S+ | `LT-S8328XG-4XS24GT-S` | 2×SFP+ → **4×SFP+ 10G** | **710** | ★★★★★ | 万兆上行翻倍；对标现役 CRS326 |
| CRS112-8G-4S-IN | `LT-IS6312G-4GX8GT` | 4×SFP → **4×2.5G SFP**，且**宽温 -40~75℃** | **740** | ★★★★★ | 几乎一对一，还升级成工业级 |
| CRS210-8G-2S+IN | `LT-IS6312XG-4XS8GT` | 2×SFP+ → **4×SFP+ 10G** | **840** | ★★★★ | 商业 8 口暂停出货，用工业款顶 |
| CRS109-8G-1S-2HnD | `LT-IS6310G-2GX8GT` | 1×SFP → 2×SFP；**不替代无线功能** | **700** | ★★★ | 只替换交换部分，AP 另配 |
| CRS212-1G-10S-1S+ | `LT-IS6316XG-4XS4GX8GT` | 纯光口 → 8G+4SFP+4SFP+ | **1400** | ★★★ | 端口形态变了，只能当"重新设计"卖 |
| RB260GSP | `LT-IS6306G-2GX4GT`（PoE 版） | 5 口 → **4 口**，PoE 保留 | **720** | ★★★ | ⚠️ 少一口，见下方缺口 |
| RB260GS | `LT-IS6306G-2GX4GT` | 5 口 → **4 口** | **660** | ★★ | ⚠️ 少一口 |

---

## 3. ⚠️ 发现的产品缺口（要跟工厂提）

**SmartByte 最小端口数是 4 口（工业）／8 口（商业），没有 5 口、6 口。**

而 MikroTik 停产的 **RB260 系列是 5 口桌面型**，欧洲存量极大（SOHO、小办公室、监控小盒子）。

两个后果：
1. RB260 的替换单我们接不住（少 1 口，客户会纠结）
2. 更重要的：这个价位段本来是**最好的试单入口**（单价低、决策快、容易建立第一笔信任）

**建议向工厂确认**：
- 是否有 5 口 / 6 口管理型（商业 + 工业）？
- 若无，最小 MOQ 多少能开一个 5 口 SKU？

---

## 4. 怎么用这份表获客

### 4.1 对现有 705 家客户：换新钩子

每一家 MikroTik 分销商手里都压着一批 **CRS125 / CRS226 / CRS112** 的老客户。
他们自己知道这些型号停产，但**不一定有替代方案**。

**邮件钩子（可直接用）**：

> Subject: CRS125 / CRS226 are EOL — drop-in replacements?
>
> Hi [name],
>
> You probably know MikroTik has taken CRS125, CRS226, CRS112 and the RB260
> series off the catalogue. Your customers running those boxes can still buy
> spares today, but not for much longer.
>
> We build the shapes they need: 24×GbE with 4×SFP+ uplinks (replaces CRS226),
> 8×GbE with 4×2.5G SFP and -40~75°C (replaces CRS112).
>
> Do you have install base on any of these? Happy to send the cross-reference
> table and a 30-day evaluation unit.

### 4.2 判断优先级：问一句就够

**"你手里还有多少 CRS1xx / CRS2xx 的老客户？"**

答得出具体数字 → A 级，立刻报价
答"应该有一些" → B 级，发对照表
答"我们主要卖 CRS3xx" → C 级，当代型号正面竞争，不好打

---

## 5. 维护规则

- **每季度复查一次**两个 EOL 来源页，新增停产型号进表
- **新增任何型号前必须双源确认** —— 一次误报"你的设备停产了"会直接毁掉信任
- 替换型号与进价以 `SmartByte关键SKU` 表页为准，降价后同步更新
- ⚠️ **不要把"我们常卖的二手型号"当成"官方停产型号"**

---

*建表：2026-09-22 ｜ 数据来源：mikrotik-store.eu 停产清仓页 + cloudrouterswitches.com EOL 清单（双源交叉）*
*已排除：linknewnet.com（SEO 博客，把在售的 CRS326/CRS328/CRS520 误标为 EOL）*
