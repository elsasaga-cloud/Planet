## 0. 这份文档怎么用

- **读者**：任何要替 Saga 写信、报价、定级客户、做调研、改脚本的 Agent（任何模型、任何会话）。读完本文不必再翻 300+ 份仓内文档就能掌握「Saga 是谁、卖什么、怎么卖、给谁卖、什么不能做、仓库里东西在哪」。
- **性质**：**内部参考**。含进价、毛利、邮箱账号、成单客户明细——**不得整段外发给客户**；对外只用 §9 的英文口径。
- **真源优先级**（Simon 多次裁定）：
  1. Simon 当轮的原话（`docs/requirements/对话全记录.md`）> 本文；
  2. 产品事实：SmartByte 官网（2026-09 改版，`docs/smartbyte/*`）> SmartByte 2026-09 价格表（`data/价格主表.csv`）> Saga Drive 旧版；Realtek 线进价真源 = 《洪瑞报价-天龙2026930.xls》；
  3. 商务/口径：S/A 邮箱 2026-09/10 Simon 现行说法（§7.9）> Drive《MUST KNOW》> 早期 Profile；
  4. 客户事实：研究档 JSON（`data/saga_clients/research/<code>.json` 等）> 渲染出的 MD 档案（档案永远由脚本渲染，**禁止手改**）。
- **引用格式**：本文每一节末尾给出「来源」路径；拿不准的事回源文件看原文，不要凭本文转述再加工。
- **更新**：本文由 `scripts/saga_intro/build.py` 生成（叙述部分在 `scripts/saga_intro/parts/*.md`，型号/价格表直接读 `data/价格主表.csv`、`data/价格主表_HRUI.csv`）。改数据后重跑脚本即可，文件名带日期，旧版不覆盖。

---

## 1. 身份卡（一页看完）

| 项 | 内容 |
|---|---|
| 对外品牌 | **Saga / Saga Telecom**（型号前缀 STC- / STI- / STH-） |
| 法律主体（PI / 报关 / 证书名义） | **Zhengzhou Saga Telecom Equipment Co., Ltd.**（郑州）；官网 At-a-Glance 写「Base = Shenzhen, China」——Simon 人在深圳、主体在郑州，两者并存（复盘 F14），对外材料不强调地址 |
| 官网 | **https://sagatele.com/**（2026-07-28 注册 10 年，GitHub Pages 托管，仓库 `SimonSaga-202306/sagatele-site`，单页 index.html）；旧站 sagatelecom.com.cn 已停、曾计划改为产品站；对外只写 sagatele.com |
| 一句话定位（英文，固定） | **An Engineering & Supply-Chain-First Telecom Partner** |
| Slogan（英文，固定，Simon：「这个不考虑变」） | **Built to Last, Continuous Supply, Evolving Together** |
| 成立/运营 | Simon 2023 年起以 SOHO 形式运营（最早单据 2023-07；Simon 自述「在通信行业 ACCESS switch 干了 6、7 年」，Saga 「经营了 2 年，净利润分别是 5 万和 10 万元」） |
| 人员 | **一个人**：Simon。对外三个名字 = 三个 Gmail 账号（§2.2）。无员工、无海外分公司、无独家代理 |
| 性质 | **副业**（Simon 有本职工作：在职销售，所在公司做视频光端机 / DWDM / 光模块）；固定成本 2–3k/年；不压货、不投广告 |
| 货源 | 三家供应商、两层架构：接入层 **SmartByte（Marvell，核心货源）** + **HRUI 洪瑞（Realtek，补型号 / 价格敏感客户）**；汇聚/核心层 **Hohunet（CENTEC）** |
| 产品 | 商用 / 工业 PoE 与非 PoE 交换机（5–48 口，L2 / L2+ / L3）、工业介质转换器、CENTEC 10G–400G 汇聚/核心/DC 交换机；光模块/DAC/电源只随整机搭售 |
| 认证（Saga 名义） | **CE（EMC+LVD）/ RoHS / REACH SVHC 240 / UKCA（EMC+LVD）/ FCC SDoC**（2024-07 同批，东莞骏安 + 深圳中测通）；介质转换器另有 2021/2022 一批。**无 UL / cUL / E-mark / KC / EN50155 / IP67 / ATEX** |
| 市场 | 只做海外。**四主区：土耳其 / 美国 / 英国 / 德国；波兰次重点**；欧洲其他国家与加拿大在范围内；俄罗斯 / 印度 / 韩国有客户但次级；**不做国内市场，网站永远不出现中文** |
| 成单 | PI 包 20 个成单客户（2023-07 → 2026-10），单据销售额 USD 109,988 + RMB 158,432；真正的量在 Angora（TR）、Biz-Ethics/Mbata（NG）、NYNEX（DE）、PBA Forever（TH）四家（§13） |
| 报价 | USD **EXW**（非欧盟客户可 DAP / FOB 深圳）；`$xx USD EXW（快照 YYYY-MM-DD，15 天有效，报价前核价）`；T/T 50% 预付 + 50% 发货前；PayPal +5%；MOQ 1；标准品 4–7 个工作日 + 5 天老化 |
| 收款 | T/T（中国银行；首笔境外来款需买方股东信息）、Xtransfer、PayPal（s. 账户）、HK 账户可收 TRY、EUR 账户可用；俄罗斯 / 尼日利亚 / 泰国 / 马来西亚等走**货代人民币**；RU / BY / KZ / UZ 收款路径未清前不报价 |
| 沟通渠道 | 邮件为主（英文）；WhatsApp（官网悬浮按钮只跳转不显示号码）；WeChat / LinkedIn 只对 James（加拿大）用过；**对外材料不出现 152 手机号与 s. 邮箱** |
| 不做 | 云管理 / 控制器、轨交 EN50155、IP67、消费级 / 家用路由、UL/E-mark/KC 行业、SFP28+ 高速 Marvell、SDK / 源码、国内公账单、视频营销 / Facebook / YouTube / 付费广告（§6.4 完整清单） |

来源：`docs/reference/Saga公司画像与边界.md`、`docs/reference/Saga品牌口径与宣传语录.md`、`docs/Saga理念摘读_2026-10-23.md` A1/A4/A8/A25/A27、`docs/reference/证书登记表_2026-10-22.md`、`docs/成单客户_PI复盘_2026-10.md`。

---

## 2. Simon 其人与 Saga 的运行方式

### 2.1 Simon（唯一的人）

- 销售出身，英语专业（专八），非通信科班；「我自己也有工作，这个外贸公司是我的副业，也就是我没有那么多精力去搞非常技术的东西」。
- 人在**深圳**（「通信资源、供应链、人文环境很不错」）；日常「每天 1–2 小时固定处理贸易事务，每周 1 天拓展，每月一次升级」是他给自己定的节奏。
- 自我评价：「我这个公司品牌的优势劣势很明显，非常两极化：如果客户很在意价格、公司实力，我很吃亏；但如果更在意我们的 capability、产品的功能，我们非常 OK」。
- 价值观（原话）：「只做顺手单不做拼命单」；「1 次跟进不行就 10 次，10 次不行就 2 年 5 年」；「不是 2 选 1，是都要有，比例不一样，前期 82 甚至 91，慢慢地 73、64、55、甚至 46 开了，give it time!!」（欧洲因果型客户 vs 印度倒推型客户的比例）；「在对的 4 个国家，把对的 20 个客户，服务成离不开你的 8 个」。
- 对 Agent 的工作要求（必须遵守）：答复用**大白话**、每项「搞定 / 没搞定 + 你要做啥 / 不用做啥」；不要一轮一问（决策进 `待统一处理问题清单.md` Q-xx 并按默认执行）；任务要**长、批量大**（40 分钟到 1 小时一轮）；每轮结束有文字报告；每一轮对话原文带时间戳记入 `docs/requirements/对话全记录.md`；判断标准「省你的时间 + 有没有长期复利」；**永远不要让 Simon 去问 Peter/HRUI 要价格**；断言「缺」之前先 grep 证据。

### 2.2 三个名字 = 一个流程的三个阶段

| 对外名字 | Gmail | 用途 / 阶段 | 单号前缀 | 签名 |
|---|---|---|---|---|
| **Simon** | `s.sagatelecom@gmail.com` | 最早的账号；早期客户关系、群发（2026-09/10 的「24 Port PoE Managed Switch」813 封）、PayPal 收款账户；**对外材料已清理 152 手机号与 s. 邮箱** | STSC- | `- Simon / https://sagatele.com/ / An Engineering & Supply-Chain-First Telecom Partner / Built to Last, Continuous Supply, Evolving Together` |
| **Alan** | `a.sagatelecom@gmail.com` | 报价、PI、订单、技术问答、品牌站联系邮箱；交接句式「My friend Simon sent you some info… I will take over」 | STAG- | 同上格式 |
| **Elsa** | `e.sagatelecom@gmail.com`（显示 "Elsa from Saga Telecom"） | 首触群发（2025-03 起每月一波 ≈12 个主题）、产品站联系邮箱；3,675 封 / 3,288 会话；标签 `Replied` 51 会话 | STEC- | `Elsa / https://sagatele.com/ / An Engineering & Supply-Chain-First Telecom Partner / Built to Last, Continuous Supply, Evolving Together` |

- 「三个账号都是我」（T29-U28）。一个客户的完整历史分散在三个邮箱，**合并后才是一条线**；加厚每户要三箱都查，写明「最后一次由哪个名字接触」。
- `STS-/STSC-2026xxxx-001` = 2026 新版报价/PI 模板。
- S / A 邮箱**无法**连到 Arena 连接器（T28-U2）——不要再建议；S/A 的历史已整箱入库 `data/gmail_s|gmail_a`（jsonl 按月）；E 箱可经 Gmail 连接器只读。
- 首触样板两套**不混发**（Q-21）：Elsa 群发 = 「3 条短特性 → 1 个问题 "Do you need some units for testing?" → 1 张产品图 → 签名」，不写价格不写公司简介；Planet 仓样板 = 「观察 → 相关性 → 单一 P1 报价 → 一问」。

### 2.3 运行事实（SOHO 的硬约束）

| 约束 | 出处 | 直接推出的做法 |
|---|---|---|
| 一个人、副业、固定成本 2–3k/年 | 《总结反思》；U28 | 必须筛客户；不做售后密集产品；时间是最贵资源 |
| 不压货、全预付、供应商 → 货代直发，「我自己是不经手产品的」 | 《由Sales转向Projects》；PI 全 T/T·PayPal | MOQ 1、样品付费、交期随供应商；「库存」= 供应商的芯片库存 |
| 贸易商身份、价格被动（「给我 100，我最多卖 130」；后文「我卖 110 是极限价格了」） | 《背景信息》 | 不打价格战 → 利润底线制 + 30% 封顶 + 拒绝价格流客户 |
| 认证只到 CE 级 | 《背景信息》 | 守界：不进强制认证行业；UL/PSE 项目让客户自担认证 |
| 不做国内；**国内单只走私账**（支付宝/微信/银行卡，「宁可不接也不处理税相关的东西」） | 《计划》；Saga.md 2026-08 | 网站无中文；与 SmartByte 国内客户冲突时让路（Larch 案） |
| 供应商关系 > 单笔机会 | U28「CENTEC 敲门砖、Peter 产品优先」 | 产品边界由供应商能力与 ROI 决定 |
| 贸易公司 = 「天然美元收入 + 合法结汇通道」（个人财务文档里与 Saga 唯一相关的一句） | 《USD和RMB》 | 其余个人财务内容**不入库不引用** |

- 两年净利润：第一年 5 万、第二年 10 万元（第二年接了一个大项目 = Angora 178 台）。
- 销售漏斗（A 邮箱两年）：14,500 发 → Opened 1,011 → 真实来信 208 → 实质线程 91 → 深谈 ≈10 → 成单 4。这不是「转化率低」，是三道筛子 + 顺手单 + 边界清单共同设计出的形状（§15 C2/C3/C10）。

来源：`docs/Saga内在逻辑与概念_2026-10-24.md` §1、`docs/Saga理念摘读_2026-10-23.md` A1–A8/A20/A25、`docs/gmail/00-Gmail盘点与使用方案.md`、`docs/成单客户_PI复盘_2026-10.md`。

---

## 3. 商业模式：Saga = 接口层

- **Saga 不是产品公司，是接口层**：下面三家供应商，上面客户；Saga 提供统一的型号命名（STC/STI/STH 覆盖三家来源）、资料、条款、单一对接人。PI 上写「Manufacturer: Zhengzhou Saga Telecom」+「Marvell Chip」；工厂装箱单抬头是 Saga 郑州（客户看不到 SmartByte）。
- **三道被动筛子**（过滤优先于转化）：① 口号「Marvell 管理型」把只看价格的 Realtek 客户从芯片源头筛掉；② Drive 自助资料（Product Link PDF 五个文件夹）筛掉不愿读的；③ Template 条款（Must-Read / A Word / Order Procedure / Warranty / Customization）筛掉不接受规则的。**客户走到第几道筛子 = 他的真实阶段**（读了 Drive 能引用型号/价表 = 第 2 道；付样、确认 PI/标签、填供应商表 = 第 3 道）。
- **技术流绑定**（不是 API）：让客户把 Saga 的型号、CLI/MIB、固件行为、规格书写进自己的系统、标书、运维文档；五个真实信号：客户把 MIB 导入 NMS / 写了基于 CLI 的内部文档 / 型号进入标准 BOM / 正式测试留档 / 新项目直接复用——「出现 3 个以上，你就已经不是可替代供应商了」。明确放弃「伪绑定」：API 深度对接、定制开发、SDK、深度 NMS 集成、特殊协议。三问：「如果今天我消失，客户要付出多少工程代价？客户内部是否有痕迹证明你存在？下一个项目，默认是谁？」要向客户灌输 **Change is Expense**。
- **中性与隐身**：设备中性、无中文、logo 只印标签；SmartByte 隐身在 Saga 之后，Saga 又隐身在客户品牌之后（Angora「Verge」系列、Fastball FBC-204GP = STC-204GP、Mbata BNSC- 系列、James SW-3200）。**OEM 品牌商最优先的根因在这里**——客户为自有品牌投入的型号、包装、文档都是沉没成本。
- **信息资产化**：规格书、价表、手册、特性表、Roadmap、Profile 都按「一次做好、季度更新、所有客户共用」设计；每个成单客户一个按「国家 / 客户名」命名的 Google Drive 文件夹（Datasheet / User Manual / Certificate of Warranty / Warranty Policy / Web & CLI Manual / Product Photos / Shipping Document / Details of This Order）。
- **How We Do Business（Saga 原文）**：「digital and paperless… #gogreen」；「Simplified, Standard, Solution based」；「buffet-style business communication」（公开 Google 链接、季度更新、价值自显）；「It is not only about fiber optic connection, but also about human connection.」
- **CCF（Commercial Contract Framework）**：付款 / 交付物流 / 质量规格 / 保修 / RMA / 出口合规 / 一般权利义务，Saga 内部标准季度复审（早期版本写「renewed ON YEARLY BASIS」）。
- **远期想法（不是当前执行项）**：SaXa 矩阵——Saxa 光模块/DAC/AOC/跳线、Sala DWDM、Safa PON/WAP、Sava 品牌标品纯贸易、M12 交换机补充线；状态码 MS/MC/TS/TC；Simon 2026-08：「这是早期的规划… not now」。「由 Sales 转向 Projects」：已有 sales 托底、开发信照发，方向向项目（BOM、竞标）靠拢；DC Switches 当项目入口只在美/德/英推。

来源：`docs/Saga内在逻辑与概念_2026-10-24.md` §2 C1–C5/C13、`docs/Saga理念摘读_2026-10-23.md` A1/A2/A4/A5/A11、`docs/reference/Saga品牌口径与宣传语录.md` §1。

---

## 4. 三家供应商

| | SmartByte（接入层主力） | HRUI 洪瑞（接入层补充） | Hohunet（汇聚/核心） |
|---|---|---|---|
| 芯片 | **Marvell**（AC3 98DX226S/336S 时代 → **AC5 / AC5 Lite 98DX2515/2518**；AC5X 2.5G/25G；Aldrin2 / Falcon DC 白盒） | **Realtek**（RTL83xx；ACL 256–512） | **CENTEC 盛科**（VastLakes / BigFlow / PeakNetX 平台；STOS 软件） |
| 官网 | https://www.smartbyte-switch.com/（2026-09 改版，**产品事实真源**） | https://www.hruitech.com/ | https://hohunet.com/ |
| 公司 | SmartByte Technology Co., Ltd，2020 深圳；母公司**凌特华盛**（惠州 8 楼，Marvell 方案，主打欧美），100% 控股**进为时代**（7 楼，MTK 方案，主打东南亚/印度）；惠州工厂 7,000 ㎡、月产 3K DIN 导轨机（早期 Profile 自述口径） | 深圳洪瑞光电（hruitech.com / hrgdkj），报价单型号 ZX-、官网 HR 码；**价格月变（「1 个月变 4–5 次」）** | CENTEC 方案商；SmartByte 2025–2026 也在预研 Centec 平台 |
| 对接人 | **Peter**（技术窗口；「Peter 产品优先」；NYNEX 技术问题由 Peter 处理） | 天龙 / 欧林克报价单（`洪瑞报价-天龙2026930.xls`、`洪瑞报价-欧林克 26818.xls`） | — |
| Saga 前缀 | STC-（商用）/ STI-（工业）/ 介质转换器 | STC-（商用 Realtek 线）/ STI-（Realtek 工业 DIN 线，Drive 2025-04 表 21 款 $80–205） | **STH-** |
| 价格真源 | SmartByte 2026-09 CNY 价表（管理型有效期 2026-09-01 → 2026-12-30）；非管理表 2024-01-11、Bypass 表 2025-03-12（旧，报价前核） | 《洪瑞报价-天龙2026930.xls》（2026-09-30）> PI 采购合同成交价 > 微信口径 | A 邮箱附件 2026 Q2 价表 / 群发价（§8.6） |
| 保修（工厂政策） | 官网：工业 6 系列 5 年 / 3 系列 3 年；商用 3 年；ODM 另议 | — | 2026Q2 价表「Warranty: 1 year」 |
| Saga 对外保修 | **STC 1 年 / STI 3 年**（Drive《Warranty Policy》+ 75 份实发 PI 普查）；官网 5 年不引用 | 同 | STH 同商用 1 年 |
| 固件 | AC3 终版 lite-hotfix-7.3.13（只维护）；AC5 2026-08 给客户 ac5-hotfix-7.4.2；**7.5.x** = AC5 Lite 发布版（`Saga Feature List_7.5.x_L2+/L3.xlsx` 在仓库根目录） | — | STOS《Saga Software Function List_EN_V2.4》（2026/Q2）按许可分层 EB / MS / MA / ST |
| 关系口径（对外） | "SmartByte is our Marvell-platform manufacturing partner; Saga owns the product definition, firmware branding and after-sales." 不自称工厂；Factory Tour 只能以 "our manufacturing partner's ISO9001/14001 facility" 引用 | 不对客户提 HRUI 名字；只在客户自己说 Realtek / 低价 / 功能简单时给 Realtek 线 | 对外「CENTEC 是 core 不是 access」；Saga 不是 CENTEC/Hohunet 的欧洲总代 |
| 仓内资料 | `docs/smartbyte/*`（官网全量抓取、公司与政策页、微信 OCR 13,943 条、新闻与固件）、`data/smartbyte_site*`、`data/smartbyte_drive*`、`docs/smartbyte_wechat_summary.md` | `docs/suppliers/HRUI/00–05`、`data/hrui_*`、`data/价格主表_HRUI.csv`、`docs/reference/价格表_HRUI_三档加价_USD.md` | `docs/suppliers/Hohunet/*`、`data/hohunet_*`、`docs/reference/CENTEC_产品表与报价锚_2026-10-24.md` |

- **供应商筛选原则**（Simon 存档的 5 条硬门槛）：生命周期 ≥5 年、保守型硬软件策略、技术沟通可降维、供应商不干你这套系统的事、**价格稳定 > 价格便宜**。
- **供应商关系优先于客户机会**：Larch 8,000 台（$250 目标价 + 无软件 + 与 SmartByte 国内客户冲突）被主动停止；CENTEC 是「敲门砖」但 Peter 的产品优先（T29-U15/U16）。CENTEC 跟进 / 备货 / 固件都是 Simon 自己的事，Agent 不代办。
- SmartByte 2024-11「六个不做」（AC3 时代原话）：NAT / 堆叠 / SD-WAN / TSN / MPLS / 云管理——MPLS 现在 CENTEC 线有，其余仍不做。
- SmartByte 产品路线（官网）：2024 AC5X 24/48×2.5G + 6×25G、Fiber Bypass；2025 AC3→AC5 100%、DI/DO/RS485、Booster PoE；2026 MQTT/1588 PTP/Modbus/Profinet、首款 TSN（Ironman）、Centec 管理型；2027 EN50155 系列——**路线图不等于 Saga 现货，未进价表的一律不承诺**。

来源：`docs/reference/Saga商务条款速查.md`、`docs/smartbyte/公司与政策页_2026-10-20.md`、`docs/Saga理念摘读_2026-10-23.md` A8/A29、`docs/对外口径一致性_2026-10-24.md` #4/#18、`docs/reference/CENTEC_产品表与报价锚_2026-10-24.md`。

---

## 5. 产品体系

### 5.1 命名规则

- **三大类目**（Simon 原话）：**STI = Saga Telecom Industrial**、**STC = Commercial**、**STH = High speed network = Core & Aggregation**；「是不是 PoE 以及管理啥的都体现在命名里，而不是类目分项里」。
- **AC5 / Realtek 线字母表（STC/STI）**：`ST{C|I}-` + 上联口数 + 下联口数 + 速率/介质字母 + 管理/PoE 后缀。常见读法：
  - 速率/介质：`F` 百兆、`G` 千兆电、`DG` 1G/2.5G SFP、`XG` 1G/2.5G/10G SFP+、`GC` Combo、`GF` 千兆光；
  - 功能：`M` 管理型、`P` PoE（af/at）、`-2BT`/`-4BT` 1–2/1–4 口 PoE++ 60–90W、`-U` 机架 AC/DC 冗余、`-D` 带 DI/DO/RS485、`(L3)` 三层档、`-280W/-440W` 电源、`-24V` 24V 被动 PoE 输出、`-Auto` 24/48V 自适应、`E` 非管理（工业）；
  - 介质转换器：`STI-1xx/2xx` + `FE/GE/FP/GP`；
  - 例：**STC-424XGGPM-280W** = 商用、4×10G SFP+ 上联、24 口千兆 PoE 管理型、280W（= SmartByte LT-S8328XGP-4XS24GT-S，「AC5 爆款」，群发 $180）；**STI-288DGGPM** = 工业、2×2.5G SFP、8 口千兆 PoE 管理型（= LT-IS6310GP-2GX8GT）。
- **STH 线字母表（CENTEC）**：`C` 100G QSFP28、`QC` 400G QSFP112、`QX` 40G QSFP+、`DX/DF` 25G SFP28、`XF` 10G SFP+、`XE` 10G Multi-Gig 铜、`VE` 5G 铜、`DE` 2.5G 铜、`XP/VP/DP` 对应速率 Multi-Gig 铜 + PoE++、`GE/GP/GF` 1G 铜 / 1G PoE++ / 1G SFP；后缀 `-HSI` 双 CRPS + 热插拔风扇、`-SFI` 固定单电源。例：STH-2C24XF-HSI = 24×10G SFP+ + 2×100G 双电源。
- **光模块与 PoE 配件命名（Saga 自定，随整机搭售）**：STI/STC + M/G/DG/XG（速率）+ 距离 km + SD（单模双纤）/SS（单模单纤 T/R 成对）/MD（多模双纤）/T（电口）；PoE 配件 PI（Injector，如 STI-PI-G90W-48V）、PS（Splitter）、PE（Extender）。SFP 只到 10G；25G/40G/100G 随 STH 整机报（Angora 实成交 1G $5 / 10G $8–10 / 25G $20 / 40G $33 / 100G $42；ITM 400G-SR4 $300）。
- **型号书写规则**：档案、邮件、CSV 一律写 **Saga 型号**；Saga 无对应规格的（光纤 Bypass 全系、带 DI/DO 的 16 口 4×2.5G 上联、bt + 4×10G 组合、L3 8GE+8SFP+4×10G 等 17 个）写 SmartByte `LT-` 型号并注明「Saga 暂无对应型号，沿用 SmartByte 型号 LT-xxx」；同名有 L2+/L3 两档的（STC-424XGGM $143/$295）必须注档位；**有效型号集合 = `data/价格主表.csv` 的 `Saga对应型号` ∪ `audit_ab.py` 的 HRUI_MODELS ∪ CENTEC 表**——信稿里出现不在集合内的型号即错。

### 5.2 门面机型（品牌站 / 产品站 / 群发主推）

| 型号 | 一句话 | 现行对外价锚 |
|---|---|---|
| **STC-424XGGPM-280W** | Marvell AC5 L2+，24 口 PoE af/at + 4×10G SFP+，OEM + 可定制 Web GUI，280W | 群发 **$180/pc**（= CNY 1,010 × 1.20 ÷ 6.69 = $181.2，20% 档）；Elsa 旧群发 $170 |
| STC-424XGGM | 同上非 PoE | $127–138 三档；2026-07 对 MikroTik 顾问「130USD」 |
| STC-4168XGGCM | L3，16×1G SFP + 8 Combo + 4×10G SFP+ | NYNEX 2026-10 复购 20 台；列表价 $413 |
| STC-448XGGPM / STC-448XGGM | 48 口 PoE / 非 PoE + 4×10G | $335 / $264（20% 档） |
| STI-288DGGPM | 工业 L2+，8 口 PoE + 2×2.5G SFP，DI/DO/RS485，240W | $139.9（20% 档）；Saga 列表 $137.5；老表 $125 |
| STI-488XGGPM2B-2BT | 工业，光旁路 ≤10 ms + 4×10G 上联 + 2×90W | 品牌站展示款 |
| STI-21616GP | 16 口 PoE+ 240W 非管理工业，PoE watchdog，1–4 口 250 m | Elsa 群发 $165 |
| STI-21616DGGPM / STI-21616XGGPM | 工业 16 口 PoE 管理型 2×2.5G / 2×10G（James SW-3200-16GP 贴牌） | $240 / $298（20% 档） |
| STI-488DGGPM-2BT | 工业 8 口 PoE 含 2 口 bt + 4×2.5G SFP | $165–179 三档；Netaş 2025-12 首单机型（单据 USD 545） |
| STC-110XGE | 10G 介质转换器（UKCA 主测款；Vi-Link 采购过） | $65（老表口径，不在 2026-09 主表内，报前核） |
| STH-2C24XF-HSI | 24×10G SFP+ + 2×100G，双电源 | 群发 $1,500；2026-06 对 SA-060 HSI $1,250 含 MA |
| STH-8C48DX-HSI | 48×25G + 8×100G | $4,800 |
| STH-32C-HSI / STH-32QC | 32×100G / 32×400G DC | $6,000 / 400G 群发「Ready in stock」236 封（实际交期要核） |
| STC-2224GFP-24V / STC-208GP-Auto / STC-4424GCP-4BT-Auto | 24V 被动 PoE 方案（Ubiquiti/Cambium/护士呼叫等 24V PD） | 案例文档已成文 |

### 5.3 完整型号 × 价格表（自动生成）

下表由 `data/价格主表.csv`（SmartByte 2026-09 CNY 价表 × 三档 ÷ 6.69，共 135 行）与 `data/价格主表_HRUI.csv`（洪瑞 2026-09-30，55 行）生成；CENTEC 表无成本价，只有报价锚（§8.6）。USD 列 = **对外档位价**（20% 分销 / 25% 集成 / 30% OEM），**不是**列表价；列表价（2026-06 PDF）≈ 20% 档 ÷ 0.9，见 §8.7 的矛盾说明。
