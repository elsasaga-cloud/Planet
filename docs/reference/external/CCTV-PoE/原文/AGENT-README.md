# AGENT-README.md

> **用途**：AI Agent 的"对话状态快照"，用于会话中断/刷新/切换时让新 Agent 无缝衔接。  
> **维护规则**：每次对话结束或阶段性完成后必须更新。新对话开始时 Agent 必须首先读取本文件。

---

## 📌 项目概览

| 字段 | 内容 |
|------|------|
| 项目名称 | `CCTV-PoE` — Saga Telecom 网络设备海外贸易项目 |
| 仓库路径 | `/home/user/CCTV-PoE` |
| GitHub | `SimonSaga-202306/CCTV-PoE` |
| 当前主分支 | `main` |
| 工作分支 | `arena/01a0c908-cctv-poe` |
| 最后更新时间 | `2026-09-22 18:30` |
| 最后更新由 | 全局型号替换 + Agent宪法/README创建 |

---

## 🎯 项目目标

为 **Saga Telecom**（用户自有品牌）建立完整的海外市场开发体系，包括：
1. 产品分析与定价策略（非管理型PoE交换机 + 管理型交换机）
2. 全球竞品分析
3. 海外客户开发清单（含详细联系人、推荐产品、卖点话术）
4. 客户跟进策略（分级跟进计划、邮件模板）
5. 展会参展商开发（从5大安防展会筛选的潜在推广目标）

**供应商关系**：
- **非管理型系列**（HRUI/洪瑞/欧林克代工）→ 贴 Saga 品牌销售
- **管理型系列**（SmartByte代工）→ 贴 Saga 品牌销售
- **Saga 自有价格册**：3个 XLS 文件已上传到 main 分支

---

## 🗺️ 当前任务状态

### 正在进行的任务
```
任务：✅ 海外客户深度挖掘（7批次完成，含方法论调整）
状态：**349家客户，覆盖42国家/地区**，全球前15大PoE进口国100%覆盖
**方法论调整**: Batch 7起按`Agent搜索客户方法论.docx`重新聚焦A/B/C类客户
**已完成10批次**：Batch 1-10全部入库，方法论20项中已使用16项
下一步：继续按方法论深挖MAC OUI/LinkedIn/政府招标/更多区域细分
```

### 已完成的任务（最近5条）
- [x] **第四批客户挖掘：乌兹别克斯坦/斯里兰卡/土耳其/荷兰/保加利亚/VMS合作** — 完成于 2026-09-22，commit `5f07edc`，+28家
- [x] **第五批客户挖掘：哥斯达黎加/厄瓜多尔/东欧/加纳/澳洲/中东/阿根廷/西欧/秘鲁智利/韩国/印度** — 完成于 2026-10-25，commit `8b0deda`，+71家
- [x] **第六批客户挖掘：印尼/菲律宾/新加坡/摩洛哥/埃塞俄比亚/坦桑尼亚** — 完成于 2026-10-25，commit `3a6eb91`，+23家
- [x] **第三批客户挖掘：哈萨克斯坦/哥伦比亚/墨西哥/坦桑尼亚/智利** — 完成于 2026-09-22，commit `125acce`，+35家
- [x] **第二批客户挖掘：东非/越南/泰国/Amazon D2C/东欧/英国** — 完成于 2026-09-22，commit `4fa2053`，+28家
- [x] **全局型号替换 HRUI/SmartByte → Saga** — 完成于 2026-09-22，commit `ce4b226`
- [x] **深度重写 HRUI+SmartByte 客户清单和档案** — 完成于 2026-09-22

### 待办任务（按优先级）
- [ ] 🔴 高优：**验证 Saga 型号映射准确性** — 部分型号标注"Saga最近似型号"，需用户确认是否接受
- [ ] 🟡 中优：**更新 MD 文件中的价格为 Saga 实际 EXW 价格** — 用户说"你不用管价格"，目前 MD 中的价格仍是旧供应商价格
- [ ] 🟡 中优：**补充更多客户档案** — HRUI有46家客户但只有约18个独立档案文件
- [ ] 🟢 低优：**创建 PR** — 当前所有工作在 arena 分支，PR #1 已存在但未更新最新提交

---

## 🌿 分支全景图

```
main (77a2d14)
├── arena/01a0c908-cctv-poe (ce4b226)  ← 当前工作分支
│   含: 完整市场分析+客户开发+型号替换
└── origin/main (eac0e2b)
    含: 原始HRUI报价 + 3个Saga价格册
```

**关键 Commit 记录**

| Commit Hash | 分支 | 说明 |
|-------------|------|------|
| `ce4b226` | arena | refactor: 全仓库供应商型号替换为Saga Telecom产品线 |
| `3f3abd8` | arena | feat: 深度重写HRUI客户清单和档案 |
| `789bb1e` | arena | feat: 深度重写SmartByte客户清单和档案 |
| `945317a` | arena | feat: SmartByte管理型交换机完整市场分析 |
| `0153ca9` | arena | feat: 完整市场分析、客户开发及展会参展商档案体系 |
| `77a2d14` | main | 初始上传（HRUI报价XLS） |
| `eac0e2b` | main | 用户上传3个Saga价格册XLS |

---

## 🏗️ 架构 & 关键文件

```
CCTV-PoE/
├── AGENT-README.md                    # 本文件（Agent上下文）
├── AGENT-CONSTITUTION.md              # Agent宪法规范
├── README.md                          # 项目总览（含Saga/SmartByte/展会三部分）
│
├── 洪瑞报价-欧林克 26818.xls           # 原始HRUI报价单（供应商价格参考）
├── Price List_Realtek Based Commercial Switch.xls        # ⭐ Saga自有价格册(非管理型)
├── Price List_Marvell Based Commercial Managed Switch.xls # ⭐ Saga自有价格册(Marvell管理型)
├── Price List_Commercial Web Managed Switch.xls           # ⭐ Saga自有价格册(Web管理型)
├── SmartByte managed Ethernet switch pricelist for Simon-*.xlsx  # SmartByte原始报价
│
├── 01-产品分析与市场策略.md            # Saga非管理型产品线分析（已替换型号）
├── 02-中国大陆同行竞品分析.md          # 中国大陆竞品品牌分析
├── 03-海外客户开发清单.md              # 46家HRUI/Saga海外客户（含联系人/产品/卖点）
├── 04-客户跟进策略.md                  # 客户分级跟进策略
│
├── profile/                           # HRUI/Saga客户详细档案（17个文件）
│   ├── Security-Warehouse-SouthAfrica.md   # A级, 5分支, exports@regalsecurity.co.za
│   ├── Regal-Security-SouthAfrica.md       # A级, 出口部, 45年历史
│   ├── AAC-Distribution-Malaysia.md        # A级, WhatsApp +6016-227-1728
│   ├── Mahadev-Computers-India.md          # A级, IndiaMart
│   ├── CCTV-CameraWorld-USA.md             # A级(OEM), +1-716-229-0080
│   ├── CCTV-Direct-SouthAfrica.md          # A级, WhatsApp Kishka 071 493 5476
│   ├── GCTL-Bangladesh.md                  # A级, sales@gctlbd.com
│   ├── DSE-Torino-Italy.md                 # 已有自有品牌PoE(OEM机会)
│   └── ... (其他9个档案)
│
├── exhibition/                        # 展会参展商档案（6个文件）
│   ├── Quantum-Star-Security-UAE.md       # ★★★★★ 已有Quant品牌PoE(OEM!)
│   ├── Altronix-USA.md                    # ★★★★★ 美国PoE制造商
│   ├── Axis-Communications-UAE.md         # ★★★★★ 瑞典/中东, Canon集团
│   ├── Antaira-Technologies-USA.md        # 工业级PoE
│   └── other-exhibitors-batch.md          # 21家其他参展商
│
└── smartbyte/                         # SmartByte管理型交换机专项分析
    ├── 01-SmartByte产品分析与市场策略.md   # 20款产品(已替换为Saga型号)
    ├── 02-SmartByte竞品分析.md             # 8国际+5中国OEM竞品
    ├── 03-SmartByte海外客户开发清单.md     # 44家客户(已替换为Saga型号)
    ├── 04-SmartByte客户跟进策略.md         # 分级跟进+话术+价格策略
    └── profile/                            # 10个SmartByte客户档案
        ├── scoop-distribution-south-africa.md
        ├── tlm-international-uae.md
        ├── alselsal-trading-uae.md
        ├── wav-usa.md
        └── ... (其他6个)
```

---

## 🧠 关键决策 & 背景知识

### 供应商与价格
- **决策**：HRUI报价单价格扣除10%才是实际进货价  
  **原因**：用户明确说明，HRUI给的是终端报价
- **决策**：SmartByte XLSX 价格就是实际采购价，不需要扣减  
  **原因**：用户明确说明，SmartByte给的是代理商价
- **决策**：Saga 自有价格册的价格是 EXW 出厂价（USD）  
  **原因**：价格册标注"Price term: EXW"
- **决策**：用户说"你不用管价格" — MD中的价格保持不变  
  **原因**：型号替换时用户指示不需要调整价格

### 型号映射规则
- **决策**：所有 MD 文件中 HRUI/SmartByte 供应商型号替换为 Saga 对应型号  
  **原因**：用户要求"把我2个供应商的型号替换为我的"
- **决策**：无精确匹配时标注 `Saga最近似型号，原XXX`  
  **原因**：用户要求"不确定的直接保留供应商的并在旁边注释"
- **已踩过的坑**：部分 HRUI 型号（如 ZX902-AF-42N 6口百兆PoE）在 Saga 产品线中没有精确对应，用了最近似的 STC-028FP（8口PoE）
- **已踩过的坑（重要）**：全局替换脚本过度替换了 HRUI 供应商品牌名 → Saga  
  **修复方案**：型号(ZX/LT开头)替换为Saga(STC)✅正确，但供应商公司名/品牌名应保留HRUI原文。已在01/02/smartbyte-01/smartbyte-README中恢复HRUI供应商信息

### 市场策略
- **决策**：SmartByte 只做商业级管理型交换机，不做工业产品  
  **原因**：用户明确限定范围
- **决策**：竞品分析只含中国大陆，不含台湾  
  **原因**：用户明确排除台湾
- **决策**：客户档案放在 `profile/` 文件夹作为独立 MD 文件  
  **原因**：用户的工作习惯

### 用户偏好/要求
- **用户要求**：客户档案必须包含联系人、推荐产品、卖点话术 — 不能太简单
- **用户要求**：整个仓库的推荐型号都要改为 Saga（不仅是某一个目录）
- **用户要求**：HRUI 是"非管理系列"主力，SmartByte 是"管理系列"二线
- **用户要求**：按深度审计协议记录和审计所有工作

---

## 📊 Saga Telecom 产品线速查

### Realtek 非管理型（价格册1: Price List_Realtek Based Commercial Switch.xls）

**以太网交换机（非PoE）：**
| 型号 | 规格 | EXW($) |
|------|------|--------|
| STC-05GE | 5口千兆 | $6.05 |
| STC-08GE | 8口千兆 | $10.45 |
| STC-016GE | 16口千兆, VLAN/Extend, AC | $33 |
| STC-024GE-U | 24口千兆, VLAN/Extend, AC, 机架 | $48.4 |
| STC-224GE | 2×1G SFP + 24口千兆 | $52.8 |
| STC-248GE | 2×1G SFP + 48口千兆 | $137.5 |
| STC-15XGDGE | 1×10G SFP + 5×2.5G | $38.5 |
| STC-18XGDGE | 1×10G SFP + 8×2.5G | $50.05 |

**PoE 交换机（非管理型）：**
| 型号 | 规格 | EXW($) |
|------|------|--------|
| STC-024FP | 2×百兆上联 + 4×百兆PoE, 55W | $9.9 |
| STC-028FP | 2×百兆上联 + 8×百兆PoE, 96W | $13.75 |
| STC-028GFP | 2×千兆上联 + 8×百兆PoE, 96W | $17.6 |
| STC-0216GFP | 2×千兆上联 + 16×百兆PoE, 300W | $37.4 |
| STC-0224GFP | 2×千兆上联 + 24×百兆PoE, 300W | $52.8 |
| STC-128GFP | 1×1G SFP + 2×千兆上联 + 8×百兆PoE, 120W | $22.55 |
| STC-1216GFP | 1×1G SFP + 2×千兆上联 + 16×百兆PoE, 300W | $44 |
| STC-1224GFP | 1×1G SFP + 2×千兆上联 + 24×百兆PoE, 300W | $60.5 |
| STC-024GP | 2×千兆上联 + 4×千兆PoE, 60W | $18.7 |
| STC-028GP | 2×千兆上联 + 8×千兆PoE, 120W | $24.2 |
| STC-228GP | 2×1G SFP + 2×千兆上联 + 8×千兆PoE, 120W, Watchdog | $30.8 |
| STC-2016GP | 2×1G SFP + 16×千兆PoE, 300W | $88 |
| STC-2024GP | 2×1G SFP + 24×千兆PoE, 300W | $93.5 |

### Marvell 管理型（价格册2: Price List_Marvell Based Commercial Managed Switch.xls）

**L2+ 非PoE：**
| 型号 | 规格 | EXW($) |
|------|------|--------|
| STC-28DGGM | L2+, 2×1G/2.5G SFP + 8×千兆, DC | $84.7 |
| STC-424DGGM | L2+, 4×1G/2.5G SFP + 24×千兆, AC | $110 |
| STC-424XGGM | L2+, 4×1G/2.5G/10G SFP + 24×千兆, AC | $143 |
| STC-448DGGM | L2+, 4×1G/2.5G SFP + 48×千兆, AC | $220 |
| STC-448XGGM | L2+, 4×10G SFP + 48×千兆, AC | $286 |

**L3 非PoE：**
| 型号 | 规格 | EXW($) |
|------|------|--------|
| STC-424XGGM(L3) | L3, 4×10G SFP + 24×千兆, AC | $294.8 |
| STC-448XGGM(L3) | L3, 4×10G SFP + 48×千兆, AC | $511.5 |
| STC-448XGGMO | L3, 4×10G SFP + 48×1G SFP, AC | $687.5 |
| STC-4168XGGCM | L3, 4×10G SFP + 16×1G SFP + 8×Combo | $412.5 |
| STC-4816XGCGM | L3, 4×10G SFP + 8×Combo + 16×千兆 | $353.1 |

**L2+ PoE 管理型：**
| 型号 | 规格 | EXW($) |
|------|------|--------|
| STC-424DGGPM-280W | L2+, 4×1G/2.5G SFP + 24×千兆PoE, 280W | $165 |
| STC-424DGGPM-440W | L2+, 同上, 440W | $220 |
| STC-424XGGPM-280W | L2+, 4×10G SFP + 24×千兆PoE, 280W | $198 |
| STC-424XGGPM-440W | L2+, 同上, 440W | $264 |
| STC-448DGGPM | L2+, 4×1G/2.5G SFP + 48×千兆PoE, 440W | $308 |
| STC-448XGGPM | L2+, 4×10G SFP + 48×千兆PoE, 440W | $368.5 |

**L3 PoE 管理型：**
| 型号 | 规格 | EXW($) |
|------|------|--------|
| STC-424XGGPM(L3) | L3, 4×10G SFP + 24×千兆PoE, 440W | $374 |
| STC-448XGGPM(L3) | L3, 4×10G SFP + 48×千兆PoE, 440W | $583 |
| STC-4816XGCGPM | L3, 4×10G SFP + 8×Combo + 16×千兆PoE, 440W | $610.5 |

### Web 管理型（价格册3: Price List_Commercial Web Managed Switch.xls）

| 型号 | 规格 | EXW($) |
|------|------|--------|
| STC-80XGWO | 8×10G SFP, fanless, DC | $93.5 |
| STC-120XGWO | 12×10G fiber, fan, AC | $143 |
| STC-05XGWE | 5×10G Ethernet, fan, DC | $137.5 |
| STC-15XGDGWE | 1×10G fiber + 5×2.5G, fanless | $44 |
| STC-18XGDGWE | 1×10G fiber + 8×2.5G, fanless | $55 |
| STC-28GPW | 2×1G fiber + 8×千兆PoE, 150W | $42.9 |
| STC-216GPW | 2×1G fiber + 16×千兆PoE, 200W | $91.3 |
| STC-224GPW | 2×1G fiber + 24×千兆PoE, 300W | $102.3 |

---

## 🔑 HRUI→Saga 型号映射表

> 以下是仓库 MD 文件中已执行的替换映射。标注"Saga最近似"的型号需要用户确认。

| 旧型号 (HRUI/SmartByte) | Saga 型号 | 精确匹配? |
|---|---|---|
| ZX902-AF-42N (6口百兆PoE) | STC-028FP | ⚠️ 近似（Saga最小8口PoE） |
| ZX902-AF-82N (10口百兆PoE) | STC-028GFP | ⚠️ 近似 |
| ZX902-AF-82GN (10口百千兆PoE) | STC-028GFP | ✅ |
| ZX901-AF-821GNS (11口+SFP) | STC-128GFP | ✅ |
| ZX902-AF-162G (18口百千兆PoE) | STC-1216GFP | ✅ |
| ZX902-AF-242G (26口百千兆PoE) | STC-1224GFP | ✅ |
| ZX902-AFG-82N (10口千兆PoE) | STC-208GP | ✅ |
| ZX902-AFG-822NS (12口千兆PoE+2SFP) | STC-228GP | ✅ |
| ZX-SW0050 (5口百兆) | STC-05GE | ⚠️ 近似 |
| ZX-SWG1080 (8口千兆) | STC-08GE | ✅ |
| ZX-SWG10160D (16口千兆) | STC-016GE | ✅ |
| ZX-SWG10240D (24口千兆) | STC-024GE-U | ✅ |
| LT-S8328XG-4XS24GT-S (L2+ 24GE+4×10G) | STC-424XGGM | ✅ |
| LT-S8328XGP-4XS24GT-S (L2+ 24GE PoE+4×10G) | STC-424XGGPM-280W | ✅ |
| LT-S8528XG-4XS24GT (L3 24GE+4×10G) | STC-424XGGM(L3) | ✅ |
| LT-S8552XG-4XS48GX (L3 48口SFP) | STC-448XGGMO | ✅ |
| LT-IS8528XG-4XS16GT8GC | STC-4816XGCGM | ✅ |
| LT-S8352XGP-4XS48GT | STC-448XGGPM | ✅ |

---

## 💬 对话历史摘要

### 对话 1 — 2026-09-22（本次长对话）

**主题**：完整的 SmartByte 管理型交换机市场分析 + HRUI/SmartByte 客户档案深度重写 + 全局 Saga 型号替换

**产出**：

**Phase 1 — SmartByte 分析（commit `945317a`）**
- `smartbyte/01-SmartByte产品分析与市场策略.md` — 20款L3/L2+管理型交换机全参数
- `smartbyte/02-SmartByte竞品分析.md` — 8国际品牌+5中国OEM竞品
- `smartbyte/03-SmartByte海外客户开发清单.md` — 44家海外客户
- `smartbyte/04-SmartByte客户跟进策略.md` — 分级跟进+话术+价格策略
- `smartbyte/profile/` — 8个客户档案（Scoop/TLM/Inter Projekt/WAV/IT Warehouse/MokerLink/Radiant/Synchroweb）

**Phase 2 — 用户反馈"太简单"，深度重写 SmartByte（commit `789bb1e`）**
- 03-客户清单：每家增加联系人姓名/电话/邮箱/WhatsApp、具体推荐型号+FOB+对标竞品+价差%、3-5条针对性卖点话术
- 10个客户档案深度重写（含CEO/高管联系人、OEM方案、首封邮件模板）
- 新增 `alselsal-trading-uae.md` 和 `tlm-international-uae.md`

**Phase 3 — 用户反馈"HRUI和exhibition也要改"，深度重写 HRUI（commit `3f3abd8`）**
- `03-海外客户开发清单.md` — 增加产品速查表+7大通用卖点+每家具体型号/FOB/对标/卖点
- 16个 HRUI 客户档案重写：
  - Security Warehouse: 5个分支联系信息、Dahua PoE对标表、OEM方案、首封邮件模板
  - Regal Security: 出口部 exports@regalsecurity.co.za、8+分支、45年历史
  - AAC Distribution: 4个办公室、WhatsApp +6016-227-1728、Ruijie对标
  - Mahadev Computers: INR利润计算表
  - CCTV Camera World: AvaEye OEM方案、NDAA注意
  - CCTV Direct: WhatsApp Kishka 071 493 5476
  - GCTL: sales@gctlbd.com、全社交媒体
  - 其他9家（AlAqili/Bluvalue/DSE/Intertrade/OMEIO/Paktron/PT-Pasifik/AVExport）

**Phase 4 — 用户要求全局型号替换（commit `ce4b226`）**
- 用户上传3个Saga价格册XLS到main分支
- 合并main分支获取价格册
- 读取3个XLS提取完整Saga产品线（Realtek非管理型/Marvell管理型/Web管理型）
- 建立HRUI→Saga和SmartByte→Saga型号映射表
- Python脚本批量替换40个MD文件
- 无精确匹配型号标注"Saga最近似型号，原XXX"
- 品牌名HRUI→Saga Telecom全部替换
- 最终验证：0个HRUI残留引用，0个旧型号残留

**决策**：
- HRUI报价扣10%=实际进货价
- SmartByte XLSX=实际采购价
- Saga价格册=EXW USD
- 用户说"不用管价格" → MD中价格保持不变
- SmartByte只做商业级管理型（非工业）
- 竞品只含中国大陆（排除台湾）

**遗留问题**：
- 部分型号映射为"Saga最近似"而非精确匹配（如 ZX902-AF-42N → STC-028FP），需用户确认
- MD中的旧价格（HRUI进货价/SmartByte进货价）未更新为Saga EXW价格（用户说不管价格）
- HRUI 04-客户跟进策略.md 中的价格策略部分仍引用旧供应商价格
- 展会档案中的型号已替换但部分描述可能需要人工复核

**下一步**：用户验证型号映射准确性 → 开始实际客户开发

**审计状态**：✅ 已完成深度审计

---

## ⚠️ 当前已知问题

| 问题描述 | 严重程度 | 状态 |
|----------|----------|------|
| 部分Saga型号为"最近似"而非精确匹配 | 🟡中 | 待用户确认 |
| MD中价格仍为旧供应商价格 | 🟢低 | 用户说"不用管价格" |
| 04-客户跟进策略中价格引用旧数据 | 🟢低 | 待后续更新 |
| PR #1 未包含最新提交 | 🟢低 | 推送后PR自动更新 |
| **型号替换过度：HRUI供应商品牌名被错误替换为Saga** | 🔴高 | **已修复** |

---

## 🔍 深度审计记录

| 对话轮次 | 预估信息点 | 已记录 | 待确认 | 审计方法 |
|---------|-----------|--------|--------|---------|
| 对话1 | 45 | 43 | 2 | ✅ 分块+分类穷举+锚点核对 |

**待用户确认的信息**：
1. ZX902-AF-42N (6口百兆PoE) 映射到 STC-028FP (8口PoE) — 端口数不同，是否接受？
2. ZX902-AF-82N (10口百兆PoE) 映射到 STC-028GFP (2千兆上联+8百兆PoE) — 上联口速度不同，是否接受？

---

## 🤖 给新 Agent 的交接指令

```
Step 1: 读取 AGENT-CONSTITUTION.md，理解规范
Step 2: 读取本文件（AGENT-README.md），理解全部上下文
Step 3: 执行 git status / git branch -a / git log --oneline -10
Step 4: 读取"正在进行的任务"，确认下一步行动
Step 5: 向用户输出状态确认，等待确认后再操作
```

**禁止行为**
- ❌ 不得在未读取本文件前执行任何 git 操作
- ❌ 不得假设分支内容，必须实际读取文件确认
- ❌ 不得在用户确认前自行决定修改方向
- ❌ 不得覆盖用户已有的本地修改

---

*最后人工校验：2026-09-22*
