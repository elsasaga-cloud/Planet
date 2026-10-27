# Marvell 生态获客方法论（Saga 专用）

> 本文档把 Claude 的 18 条 + GPT 的 12 条**全部保留**（共 30 条），按"现在能不能用"分四梯队。
> **砍掉的方法不删除，只冷冻** —— 每条都记录了解冻条件，将来你有预算/有官网/有团队时可直接启用。
> 这些都是资产，今天用不上的不等于永远用不上。

---

# ⚠️ 第零条：台厂不是客户，但要往死里挖它的客户

**这条单独放最前面，因为它是整套方法里最容易搞反、也最值钱的一条。**

## 铁律（再说一次）

```
台湾厂商 = 信号源，不是客户
台湾厂商的欧洲/北美经销商 = 客户
```

## 为什么这条最值钱

台湾厂（PLANET、ORing、Moxa、EtherWAN、CTC Union、Korenix、Atop、Advantech……）
**是欧洲工业交换机市场最大的一股供给**。它们自己在卖，所以：

1. 它们**不会买你的交换机** —— 发邮件只会暴露你的价盘，还可能被反向抄价
2. 但它们**已经替你把客户筛选好了** —— 能在欧洲卖台湾工业交换机的人，具备三样东西：
   - 懂工业交换机（不用你教育市场）
   - 有终端客户（不用你从零获客）
   - 知道台湾货的痛点（交期长、MOQ 高、改款慢、贵）→ **这就是你的切入点**

## 正确姿势（一句话）

```
台厂官网 → Dealer Locator / Where to buy / Partner Locator
        → 逐国筛选，一个都不放过
        → 拿到的是几十家已在卖工业交换机的欧洲分销商
        → 这些才是客户
```

## 已挖 / 待挖清单

| 台厂 | 状态 | 已产出 |
|---|---|---|
| ORing | ✅ 已挖 | **64 家**授权分销 |
| Antaira | ✅ 已挖 | 9 家 |
| **PLANET** | ⏳ **待挖（最大一块）** | 已零星摸到 Saratota、Netceed UK、NSI Distribution |
| Moxa | ⏳ 待挖 | — |
| EtherWAN | ⏳ 待挖 | — |
| CTC Union | ⏳ 待挖 | — |
| Korenix | ⏳ 待挖 | — |
| Atop | ⏳ 待挖 | — |
| Advantech | ⏳ 待挖 | — |

> **PLANET 是最大的一块没挖的矿**：它是台厂里工业线最全、欧洲渠道最深的，
> 预计单它一家就能出 **50–80 家**欧洲分销商。

## 挖到之后怎么开口（台厂渠道专用话术）

不要说"我在做交换机"，要说：

> 你现在代理的台湾品牌，交期多久？改个固件要等多久？MOQ 多少？
> 我这边同样的规格，交期 7 天、MOQ 10 台、中性包装贴你自己的型号。

**这是台湾渠道最痛的三根刺**：交期长、MOQ 高、改款慢。

---

# 一、四梯队总览

| 梯队 | 数量 | 含义 | 什么时候做 |
|---|---|---|---|
| **第一梯队** | 4 条 | 本周就做，零成本，已验证 | 现在 |
| **第二梯队** | 6 条 | 本月做，需要一点时间投入 | 这周排期 |
| **第三梯队** | 8 条 | 有预算/有官网/有帮手后启用 | 条件成熟时 |
| **冷冻区** | 12 条 | 当前不成立，但保留理由 | 见每条"解冻条件" |

---

# 二、第一梯队（本周就做，零成本，已验证）

## ① 竞品经销商据点名录 ★★★★★

**逻辑**：卖竞品的渠道商 = 已在卖、已有客户、已懂技术。

**步骤**
1. 竞品官网找 `Where to buy` / `Dealer Locator` / `Partner Locator`
2. **逐国筛选**，只看总部所在国会漏掉一大半
3. 拿到公司名 → 官网 → 联系人 → 进 CSV
4. 优先标记：**同时代理 ≥2 个竞品品牌**的（纯渠道，不忠于单一品牌）

**已挖**：ORing（64）、Antaira（9）、Westermo（14）、ComNet（7）、HMS/N-Tron/Red Lion（111）、MikroTik 官方分销（246）、Netonix（部分）
**待挖**：**PLANET（最大）**、Moxa、EtherWAN、CTC Union、Korenix、Atop、Advantech、Ubiquiti UISP

**本轮成果**：Westbase Networks、Saratota、Netceed UK（3 家新客户）

---

## ② 生命周期 / EOL 替换 ★★★★★

**逻辑**：客户不是不想换，是**还没到必须换**。停产 = 备件断供 = 他必须现在决定。
**这是唯一一种"不需要说服、对方自己有痛点"的场景。**

**数据源（必须双源确认）**
- `mikrotik-store.eu/en/archive-discontinued`（官方分销商停产清仓页）
- `cloudrouterswitches.com/mikrotik-eol.asp`

**产出**：见 → `MikroTik停产机型替换矩阵_2026-09.md`（8 个停产型号 → SmartByte 替换 + 进价）

**获客钩子（一句话）**
> "你们手里还有多少 CRS125 / CRS226 / CRS112 的老客户？"

答得出数字 → A 级；答"有一些" → B 级；答"主要卖 CRS3xx" → C 级

**⚠️ 已排除的错误源**：`linknewnet.com` 把在售的 CRS326/CRS328/CRS520 说成停产。那是二手 SEO 博客。
**跟客户说"你的在售设备停产了"是不可挽回的信任损失。**

---

## ③ 型号替代矩阵 ★★★★★

**状态**：`MikroTik_vs_SmartByte_替代对照表.xlsx` → 表页 `替代对照表`（19 行 × 13 列，含 MSRP/进价/匹配度/你赢在哪）

**还缺**：Netonix 替代（WISP）、Ubiquiti UISP 替代、Allied Telesis 老型号替代

**用法**：客户说"我用 XXX" → 30 秒内回型号 + 差价 + 我赢在哪

---

## ④ LinkedIn / Apollo 换关键词 ★★★★

**核心**：**不要搜 `switch`**，太宽，全是求职者。

**搜技能词（不是职位词）**
```
Prestera · 98DX · Marvell · Industrial Ethernet · PoE Switch
Fiber Switch · Managed Ethernet · Layer2/Layer3 Switch
ERPS · ITU-T G.8032 · DIN-rail switch · IEC 61850 · Network Appliance
```

**职位优先搜 Product Manager**（不是采购）
> 产品经理懂技术、懂缺口、**有动力找第二供应商**；采购只会问价格。

**规模筛 51–200 人**（决策链短）

**地区**：意 / 西 / 波 / 德 / 希 / 捷 / 葡 / 乌
**避开**：北欧、波罗的海（实测挪威 0、冰岛 0、斯洛文尼亚 0——生态空白，不是没市场）

**Apollo.io**：免费版每月有额度，可导出邮箱

---

# 三、第二梯队（本月做）

## ⑤ ImportYeti 海关数据 ★★★★（免费）

1. `importyeti.com` → 搜 `ethernet switch` 或 HS Code **`8517.62`**
2. 看谁在从中国进口、**进口频率、数量、对应出口商**
3. 筛**持续批量**进口的欧美公司

**为什么高价值**：能过滤掉"嘴上说要、手上不买"的。**进口记录是真金白银的行为证据。**

**进阶**：同一进口商在跟**多家**中国出口商买 → 正在比价 → 你插进去的机会最大

---

## ⑥ NMS / SCADA 生态 ★★★★

**逻辑**：做网络/工业监控软件的公司给客户做方案，方案里必须有交换机，
**而它自己不造硬件** —— 完美互补。

```
network monitoring software company Europe
SCADA + industrial ethernet + integration
"network management" software vendor + OEM hardware
```

**为什么优先级高于分销商**
- 分销商卖**价格**，随时被更低价的替换
- 方案商卖**方案**，交换机嵌在里面，**替换成本极高**

⚠️ 中文"监控"有歧义，要区分 **NMS 网管** 与 **CCTV 视频监控**（见 README 坑 5）

---

## ⑦ FCC ID + DoC/CE PDF ★★★（全免费）

**FCC（北美）**：`fcc.gov/oet/ea/fccid` → 搜 `ethernet switch`
看谁在认证网络产品、型号、**认证时间** → 认证时间新 = 新品即将上市 = 采购窗口期

**CE / DoC（欧洲）**
```
"Declaration of Conformity" "ethernet switch" filetype:pdf
"CE" "managed switch" filetype:pdf manufacturer importer
```
DoC 里常写明 **Manufacturer / OEM / Importer** → 直接看出**谁在贴牌、谁在代工**

---

## ⑧ Reddit / 垂直论坛 ★★★

```
r/wisp · r/networking · r/sysadmin · r/homelab
"netonix alternative" · "replace netonix" · "mikrotik switch" recommendation
```

**本轮实证（r/wisp）**
> "The ASIC family in the CRS3xx uses **Marvell Prestera**（same chipset Cisco Meraki uses）"
> "we are starting to see a lot of our clients **use the CRS328 to replace Netonix**"

**两条结论**：
1. CRS3xx = Marvell Prestera 得到用户侧确认
2. **WISP 运营商正成批换掉 Netonix** —— 活的替换窗口，且 WISP 是 PoE+户外，正是工业款强项

---

## ⑨ Marvell 品牌 / 芯片库 ★★（长期资产）

**状态**：表页 `Marvell品牌全景`（46 行 × 8 列）

**补的字段**：芯片型号 · SDK 版本 · 是否 OEM · 竞争关系 · 对应 SmartByte 型号

**已知实证**
| 品牌 | 芯片 | 证据 |
|---|---|---|
| MikroTik | 98DX3236/3257/226S/2528/8332/4310 | **官方文档**逐型号列出 |
| Allied Telesis | 98DX3236/3336/4251 | Linux 内核补丁（作者邮箱 `alliedtelesis.co.nz`） |
| Edgecore（Accton） | 98DX3236 | 官方规格书 |
| CRS3xx 系列 | Prestera | r/wisp 用户侧确认 + 官方文档 |

---

## ⑩ Firmware / MIB / 软件能力库 ★★

**状态**：已有 `Marvell Based CLI Manual.docx` / `Web Manual.docx`

**补的字段**：SNMP · MIB · Trap · CLI · SSH · REST API · NETCONF · Ansible · Cloud

**用途**：客户问"支不支持 API？" → 30 秒回答 + 知道差距在哪

---

# 四、第三梯队（有预算 / 有官网 / 有帮手后启用）

| # | 方法 | 解冻条件 | 备注 |
|---|---|---|---|
| 11 | **规格书 SEO 长尾页** | **需要有官网** | `Alternative to MikroTik CRS326`、`CRS326 replacement`、`Marvell-based managed switch`。Google 吃长尾，一旦有站就是躺赚的流量 |
| 12 | **Apollo.io 付费版** | 免费额度不够用时 | 月费几十美元，可按行业+规模+地区批量导出 |
| 13 | **Thomasnet / Europages / Kompass** | 有空闲时间时 | 工业采购平台，交换机询盘不多，但可作为补充 |
| 14 | **展会名单**（Interop、Network+Interop） | 展会恢复且你能到场 | `exhibitor list filetype:pdf` |
| 15 | **YouTube / 技术博主** | 有样机可送测时 | Homelab 博主影响力大，送测换评测 |
| 16 | **行业报告**（G2 / Gartner Peer Insights） | 需要大客户案例时 | 看谁在评价网络设备，评价者是真实用户 |
| 17 | **Panjiva / ImportGenius** | ImportYeti 数据不够深时 | 付费海关数据，颗粒度更细 |
| 18 | **Zoominfo / 邓白氏** | 需要查客户信用与体量时 | 大额订单前做背调用 |

---

# 五、冷冻区（当前不成立，但保留）

> **每条都记了"为什么现在不做"和"什么条件下会启用"。将来条件变了，这里直接能用。**

| # | 方法 | 现在不做的理由 | 🔓 解冻条件 |
|---|---|---|---|
| 19 | **SONiC 生态** | 技术门槛太高、决策链太长，客户是数据中心级 | 你开始做数据中心白牌时 |
| 20 | **ONIE 生态** | 同上，且客户技术能力极强 | 同上 |
| 21 | **招聘 / SDK 反推**（Marvell SDK / Prestera / 98DX） | **本轮实测证伪**：公开网络检索拿不到有效职位信息，搜出来全是 Linux 内核邮件列表和厂商软文 | 有 LinkedIn Recruiter 或本地招聘平台账号时 |
| 22 | **GitHub 挖掘**（Prestera / switchdev / ONIE） | 慢，但精准 | 有空闲时间做长期布局时 |
| 23 | **专利数据库**（Google Patents / Espacenet） | 投入产出比最低 | 需要判断某家是否有自研能力时 |
| 24 | **众筹平台**（Kickstarter / Indiegogo） | 众筹硬件要的是 **ODM 伙伴**，你不是工厂 | 你能对接工厂做 ODM 时 |
| 25 | **亚马逊 / Newegg 卖家反查** | 需 Jungle Scout / Helium 10（付费），且亚马逊卖家要消费级价格 | 你做消费级/SOHO 产品线时 |
| 26 | **图片反搜** | 效率低，找到的多半还是竞品官网 | 需要查谁在盗用你的产品图时（反向用法） |
| 27 | **行业协会会员名单**（CompTIA / BICSI / CEDIA） | 名单获取成本高于收益 | CEDIA（AV/智能建筑）在你做 PoE+AV 时值得入会 |
| 28 | **Gartner / IDC / MarketsandMarkets** | 报告里是**大企业案例**，你的客户是中小分销商 | 需要向大客户证明市场规模时 |
| 29 | **Digi-Key / Mouser / Arrow 找品牌** | 那是**元器件**分销，整机管理型交换机基本不在上面卖 | 你开始卖芯片/模组时 |
| 30 | **"Marvell Knowledge Graph" 知识图谱** | **过度工程**。先把表建到能发邮件，再谈图谱 | 前四梯队全部跑通、数据积累到 1000+ 条时 |

---

# 六、执行顺序（未来两周）

| 序 | 动作 | 预期产出 | 周期 |
|---|---|---|---|
| 1 | **扒 PLANET 的 Dealer Locator**（最大一块没挖的矿） | +50~80 家 | 1–2 天 |
| 2 | EOL 替换钩子群发现有 708 家 | 直接询盘 | 半天 |
| 3 | Netonix → SmartByte 替代表（WISP 垂直） | 一张表 | 半天 |
| 4 | 扒 Moxa / EtherWAN / Advantech 经销商 | +40~60 家 | 1 天 |
| 5 | Apollo 按 `Prestera`/`Industrial Ethernet` 筛 PM | 联系人清单 | 1 天 |
| 6 | ImportYeti 查 `8517.62` 欧洲进口商 | 真实买家清单 | 1 天 |
| 7 | Allied Telesis 老型号替代表 | 欧洲最大替换池 | 1 天 |
| 8 | NMS/SCADA 方案商名单 | 高价值客户池 | 持续 |

---

# 七、一句话总结

> **别再想"找更多客户"，先想"找正在被迫做决定的客户"。**
>
> 停产替换、台湾渠道的痛点、方案商配套、海关数据里的真实进口商 ——
> 这四类人今天就有痛点。
>
> **尤其是台湾渠道**：台厂不是你的客户，但台厂的欧洲经销商是你最好的客户，
> 因为他们已经在卖工业交换机、已经有客户、并且**已经受够了台湾货的交期和 MOQ**。

---

*整理：2026-09-22 ｜ 30 条方法全部保留，分四梯队*
*本轮实证：EOL 双源验证成立、招聘反推证伪、Reddit 出实证（WISP 换 Netonix）*
*新增 3 家客户（Westbase / Saratota / Netceed UK），4 家已有账号补 Netonix 信号*

---

## 零·五条（2026-09-23 新增，优先级高于下面所有方法）：**只挖集成商，别再挖分销**

### 数据事实（728 行实测）

| 类型 | 家数 | 占比 | A 级 | **A 级率** |
|---|---|---|---|---|
| **集成商 / 顾问** | 200 | 27% | **69** | **34.5%** |
| 分销 | 510 | 70% | 19 | **3.7%** |

> **集成商用 27% 的数量贡献了 78% 的 A 级，A 级率是分销的 9 倍。**

原因很直白：分销商有现成品牌线、有采购流程、要护盘；集成商按项目选货，**决策链短、能自己定用谁**。
对小贸易商来说，**分销是"too hard"，集成商才是"yes"。**

### 国家层面的缺口（缺的不是数量，是集成商）

| 国家 | 家数 | A 级 | A 级率 | 判断 |
|---|---|---|---|---|
| 意大利 | 40 | 11 | 27.5% | ✅ 已挖透（集成商多） |
| 波兰 | 33 | 7 | 21.2% | ✅ |
| **法国** | 29 | **1** | 3.4% | ❌ **最大缺口** |
| **捷克** | 26 | 1 | 3.8% | ❌ |
| **荷兰** | 24 | 2 | 8.3% | ❌ |
| **美国** | 115 | 6 | 5.2% | ⚠️ 基数最大但密度低，值得专攻 |

### 首选信源（已验证，含 URL 规律）

**① MikroTik 官方认证顾问名录** —— 目前产出质量最高

> 🎯 **MTCSWE = 交换认证 = A 级直通信号**（2026-09-23 实测确立）
> 荷兰/捷克新增 13 位顾问中，**持 MTCSWE 的 3 位全部判 A，其余 10 位判 B**。
> **挖顾问时优先抓 MTCSWE 持有者**，命中率最高。其余证书（MTCRE 路由 / MTCWE 无线 /
> MTCINE 互联 / MTCSE 安全）均不构成交换或供电需求信号。

```
https://mikrotik.com/consultants/{europe|asia|...}/{国家名小写}
例：mikrotik.com/consultants/europe/france
    mikrotik.com/consultants/europe/germany
```

- **每页字段齐全**：姓名、城市、所持证书（MTCNA/MTCRE/MTCSWE…）、电话、**邮箱** —— 拿到就能发信
- 覆盖 90+ 国家，欧洲各国均有页面
- ⚠️ 页面含大量地图瓦片。**技巧：改用 web_search 搜索 `mikrotik.com consultants {国家}`**，
  拿到的 snippet 干净得多**且带电话号码**，比 fetch_page 省 3–5 倍上下文
- 已知：法国仅 2 位（Habib Kanso/图卢兹、Adnan RIHAN/巴黎）

**② 各国本地集成商目录**（法国为例）
- `europages.fr/entreprises/france/integrateur%20reseau%20informatique.html` —— 可按行业/地区筛

### ❌ 已采尽，别再浪费时间

| 信源 | 状态 |
|---|---|
| Antaira 官方 where-to-buy（欧洲全境） | ❌ **14 家分销商全部已在库** |
| Westermo 官方 where-to-buy（欧洲全境） | ❌ **同上，全部已在库** |
| PLANET / Moxa / EtherWAN / Advantech 经销商名录 | ❌ 前几轮已挖完 |
| `installers.ui.com`（Ubiquiti 官方） | ❌ JS 动态加载，HTML 无数据 |
| `elioplus.com` Cambium 伙伴库 | ❌ 只给 5 条，国家筛选仅英美加印肯 |
| `moxa.com/en/where-to-buy` | ❌ 已 404 |

> **结论：工业品牌的经销商名录这条路已经采尽了。**
> 下一轮增量只能来自**集成商/安装商/顾问**，不要再回头挖分销。

### ⚠️ 沙箱限制

工作区 **无直连网络**（`curl` 返回 HTTP 000），只能用 `fetch_page` 工具逐页抓，
**无法用脚本批量抓取**。这限制了单轮可覆盖的国家数量——**按国家优先级排队，一次抓 1–2 国**。

