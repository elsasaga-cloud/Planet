# Saga Telecom 全景信息包（给其他 Agent 的参考手册）

> **生成时间戳**：2026-10-29 16:14:40 UTC（北京时间 2026-10-30 00:14）｜仓库 `elsasaga-cloud/Planet` 分支 `arena/3f35b9b3-planet` @ `6e839807d`｜生成器 `scripts/saga_intro/build.py`
>
> **一句话**：Saga Telecom = Simon 一个人用三个名字经营的、以 Marvell（SmartByte）接入层交换机为核心、CENTEC（Hohunet）为汇聚/核心层、Realtek（HRUI）补位的中国出口 SOHO 品牌；只做海外、只做长期关系、不打价格战、不做云管/轨交/IP67/消费级；四主区土耳其 / 美国 / 英国 / 德国 + 波兰；对外口径「An Engineering & Supply-Chain-First Telecom Partner — Built to Last, Continuous Supply, Evolving Together」。
>
> **性质**：内部参考（含进价 / 毛利 / 邮箱 / 成单明细），不得整段外发。数据截至 2026-10-29（长期客户群 2,045 = A 170 / B 1,875；价格表 SmartByte 2026-09 / 洪瑞 2026-09-30；汇率 6.69 @ 2026-10-17）。

## 目录

- 0. 这份文档怎么用
- 1. 身份卡（一页看完）
- 2. Simon 其人与 Saga 的运行方式
- 3. 商业模式：Saga = 接口层
- 4. 三家供应商
- 5. 产品体系
- 6. 技术能力与边界
- 7. 商务条款（销售口径）
- 8. 定价规则（两套并存，都是底线不是策略）
- 9. 品牌口径与对外话术
- 10. 市场与区域策略
- 11. 目标客户画像、判读框架与分级标准
- 12. 客户资产现状（2026-10-29）
- 13. 成单客户 20 家（PI 包，2023-07 → 2026-10）
- 14. 跟进节奏与渠道
- 15. 概念词典与内部术语表
- 16. 仓库地图（elsasaga-cloud/Planet，分支 arena/3f35b9b3-planet）
- 17. 规则总表（写任何东西前过一遍）
- 18. 未决事项（Q 清单与 backlog，默认执行中）
- 19. 来源清单（本文每一句都能回到这些文件）

---
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

#### 5.3.1 SmartByte / Marvell 线（`data/价格主表.csv`，135 行，CNY 为 SmartByte 未税价，汇率 6.69 @ 2026-10-17）

**Layer 2 Managed Industrial Ethernet Switches Full Gigabit Series**（6 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-240FM | LT-IS3206F-2FX4TX | ● 4*10/100Base-T RJ45 ports, 1*100Base-X SFP ports / ● DC 12~58V input, redundant power supply with polarity … | 280 | 50.2 | 52.3 | 54.4 | 55.0 | L2 |
| STI-244FPM | LT-IS3206FP-2FX4TX | PoE 衍生型（同主型规格 + PoE） | 320 | 57.4 | 59.8 | 62.2 | 66.0 | L2 |
| STI-240GM | LT-IS3206G-2GX4GT | ● 4*10/100/1000Base-T RJ45 ports, 2*100/1000Base-X SFP ports / ● DC 12~58V input, redundant power supply with… | 320 | 57.4 | 59.8 | 62.2 | 66.0 | L2 |
| STI-244GPM | LT-IS3206GP-2GX4GT | PoE 衍生型（同主型规格 + PoE） | 360 | 64.6 | 67.3 | 70.0 | 77.0 | L2 |
| STI-280GM | LT-IS3210G-2GX8GT | ● 8*10/100/1000Base-T RJ45 ports, 2*1000/2500Base-X SFP ports / ● DC 12~58V input, redundant power supply wit… | 380 | 68.2 | 71.0 | 73.8 | 77.0 | L2 |
| STI-288GPM | LT-IS3210GP-2GX8T | PoE 衍生型（同主型规格 + PoE） | 440 | 78.9 | 82.2 | 85.5 | 88.0 | L2 |

**Layer 2+ Managed Industrial Ethernet Switches Full Gigabit Series**（23 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-240DGGM | LT-IS6306G-2GX4GT | ● 4*10/100/1000Base-T RJ45 ports, 2*1G/2.5GBase-X SFP ports / ● DC 12~58V input, redundant power supply with … | 660 | 118.4 | 123.3 | 128.3 | 110.0 | L2+ |
| STI-244DGGPM | LT-IS6306GP-2GX4GT | PoE 衍生型（同主型规格 + PoE） | 720 | 129.1 | 134.5 | 139.9 | 121.0 | L2+ |
| STI-244DGGPM-2BT | LT-IS6306GP-2GX4GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 820 | 147.1 | 153.2 | 159.3 | 143.0 | L2+ |
| STI-280DGGM | LT-IS6310G-2GX8GT | ●8*10/100/1000Base-T RJ45 ports, 2*1G/2.5GBase-X SFP slots / ● DC 12~58V input, redundant power supply with p… | 700 | 125.6 | 130.8 | 136.0 | 121.0 | L2+ |
| STI-288DGGPM | LT-IS6310GP-2GX8GT | PoE 衍生型（同主型规格 + PoE） | 780 | 139.9 | 145.7 | 151.6 | 137.5 | L2+ |
| STI-288DGGPM-2BT | LT-IS6310GP-2GX8GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 880 | 157.8 | 164.4 | 171.0 | 154.0 | L2+ |
| STI-480DGGM | LT-IS6312G-4GX8GT | ●8*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots / ● DC 12~58V input, redundant power supply with p… | 740 | 132.7 | 138.3 | 143.8 | 132.0 | L2+ |
| STI-488DGGPM | LT-IS6312GP-4GX8GT | PoE 衍生型（同主型规格 + PoE） | 820 | 147.1 | 153.2 | 159.3 | 148.5 | L2+ |
| STI-488DGGPM-2BT | LT-IS6312GP-4GX8GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 920 | 165.0 | 171.9 | 178.8 | 165.0 | L2+ |
| STI-448DGGGM | LT-IS6316G-8GX8GT | ●8*10/100/1000Base-T RJ45 ports, 4*100/1000M SFP, 4*1G/2.5G SFP / ● DC 12~58V input, redundant power supply w… | 1100 | 197.3 | 205.5 | 213.8 | 220.0 | L2+ |
| STI-448DGGGPM | LT-IS6316GP-8GX8GT | PoE 衍生型（同主型规格 + PoE） | 1180 | 211.7 | 220.5 | 229.3 | 236.5 | L2+ |
| STI-2160DGGM | LT-IS6318G-2GX16GT | ●16*10/100/1000Base-T RJ45 ports, 2*1G/2.5GBase-X SFP slots / ● DC 12~58V input, redundant power supply with … | 1180 | 211.7 | 220.5 | 229.3 | 220.0 | L2+ |
| STI-21616DGGPM | LT-IS6318GP-2GX16GT | PoE 衍生型（同主型规格 + PoE） | 1340 | 240.4 | 250.4 | 260.4 | 242.0 | L2+ |
| —（沿用 LT-） | LT-IS6320G-4GX16GT-D | ●16*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots ,DI/DO/RS485 / ● DC 12~75V input, redundant power… | 1560 | 279.8 | 291.5 | 303.1 |  | 16×GE + 4×2.5G SFP + DI/DO/RS485：Saga 无 4×2.5G 上联的 16 口型（就近… |
| —（沿用 LT-） | LT-IS6320GP-4GX16GT-D | PoE 衍生型（同主型规格 + PoE） | 1760 | 315.7 | 328.8 | 342.0 |  | 16×GE PoE + 4×2.5G SFP + DI/DO：Saga 暂无对应——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6320GP-4GX16GT-D-4BT | PoE++ 衍生型 | 1960 | 351.6 | 366.2 | 380.9 |  | 16×GE PoE（4 口 bt）+ 4×2.5G SFP + DI/DO：Saga 暂无对应——沿用 SmartBy… |
| STI-4240DGGM | LT-IS6328G-4GX24GT-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots,DI/DO/RS485 / ● DC 12~75V input, redundant power … | 1660 | 297.8 | 310.2 | 322.6 | 330.0 | L2+ |
| STI-42424DGGPM | LT-IS6328GP-4GX24GT | PoE 衍生型（同主型规格 + PoE） | 1900 | 340.8 | 355.0 | 369.2 | 363.0 | L2+ |
| STI-42424DGGPM-4BT | LT-IS6228GP-4GX24GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2100 | 376.7 | 392.4 | 408.1 | 407.0 | L2+ |
| STI-4240DGGM-U | LT-IS6328G-4GX24GT-U-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots / ● AC/DC redundant power supply with polarity re… | 1800 | 322.9 | 336.3 | 349.8 | 363.0 | L2+ |
| STI-42424DGGPM-U | LT-IS6328GP-4GX24GT-U | PoE 衍生型（同主型规格 + PoE） | 2100 | 376.7 | 392.4 | 408.1 | 407.0 | L2+ |
| STI-42424DGGPM-U-2BT | LT-IS6328GP-4GX24GT-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2200 | 394.6 | 411.1 | 427.5 | 440.0 | L2+ |
| STI-4168DGGCM-U | LT-IS6328G-20GX8GC-D | ●16*100/1000Base-X SFP slots, 8*1000Base Combo, 4*1G/2.5G SFP slots / ● AC/DC redundant power supply with pol… | 2350 | 421.5 | 439.1 | 456.7 | 467.5 | L2+ |

**Layer 2+ Managed Industrial Ethernet Switches with 10G Uplink Series**（15 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-480XGGM | LT-IS6312XG-4XS8GT | ●8*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP+ slots / ● DC 12~58V input, redundant power supply w… | 840 | 150.7 | 157.0 | 163.2 | 253.0 | L2+ |
| STI-488XGGPM | LT-IS6312XGP-4XS8GT | PoE 衍生型（同主型规格 + PoE） | 920 | 165.0 | 171.9 | 178.8 | 269.5 | L2+ |
| —（沿用 LT-） | LT-IS6312XGP-4XS8GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 1020 | 183.0 | 190.6 | 198.2 |  | 8×GE PoE（2 口 bt）+ 4×10G：Saga 无 bt + 4×10G 组合（就近 STI-288DGGP… |
| STI-448XGGGM | LT-IS6316XG-4XS4GX8GT | ●8*10/100/1000Base-T RJ45 ports, 4*1000Base-X SFP, 4*1G/2.5G/10GBase-X SFP+ slots / ● DC 12~58V input, redund… | 1400 | 251.1 | 261.6 | 272.0 | 275.0 | L2+（另有 L3 档） |
| STI-448XGGGPM | LT-IS6316XGP-4XS4GX8GT | PoE 衍生型（同主型规格 + PoE） | 1480 | 265.5 | 276.5 | 287.6 | 297.0 | L2+（另有 L3 档） |
| STI-2160XGGM | LT-IS6318XG-2XS16GT | ●16*10/100/1000Base-T RJ45 ports, 2*1G/2.5G/10GBase-X SFP+ slots / ● DC 12~58V input, redundant power supply … | 1500 | 269.1 | 280.3 | 291.5 | 291.5 | L2+（另有 L3 档） |
| STI-21616XGGPM | LT-IS6318XGP-2XS16GT | PoE 衍生型（同主型规格 + PoE） | 1660 | 297.8 | 310.2 | 322.6 | 324.5 | L2+（另有 L3 档） |
| STI-488DGGGM | LT-IS6320XG-4XS8GX8GT-D | ●8*10/100/1000Base-T RJ45 ports, 8*100/1000Base-X SFP, 4*1G/2.5G/10GBase-X SFP+ slots / ● DC 12~75V input, re… | 1780 | 319.3 | 332.6 | 345.9 | 352.0 | L2+ |
| STI-4240XGGM | LT-IS6328XG-4XS24GT-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP+ slots / ● DC 12~75V input, redundant power supply … | 1960 | 351.6 | 366.2 | 380.9 | 385.0 | L2+（另有 L3 档） |
| STI-42424XGGPM | LT-IS6328XGP-4XS24GT | PoE 衍生型（同主型规格 + PoE） | 2200 | 394.6 | 411.1 | 427.5 | 423.5 | L2+（另有 L3 档） |
| STI-42424XGGPM-4BT | LT-IS6328XGP-4XS24GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2400 | 430.5 | 448.4 | 466.4 | 456.5 | L2+（另有 L3 档） |
| STI-4240XGGM-U | LT-IS6328XG-4XS24GT-U-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP slots / ● AC/DC redundant power supply with polarit… | 2100 | 376.7 | 392.4 | 408.1 | 412.5 | L2+（另有 L3 档） |
| STI-42424XGGPM-U | LT-IS6328XGP-4XS24GT-U | PoE 衍生型（同主型规格 + PoE） | 2400 | 430.5 | 448.4 | 466.4 | 451.0 | L2+（另有 L3 档） |
| STI-42424XGGPM-U-2BT | LT-IS6328XGP-4XS24GT-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2500 | 448.4 | 467.1 | 485.8 | 484.0 | L2+（另有 L3 档） |
| STI-4168XGGCM-U | LT-IS6328XG-4XS16GX8GC-D | ●16*100/1000Base-X SFP slots, 8*1000Base Combo, 4*1G/2.5G/10G Base-X SFP+ slots / ● AC/DC redundant power sup… | 2650 | 475.3 | 495.1 | 514.9 | 511.5 | L2+（另有 L3 档） |

**L3 Managed Industrial Ethernet Switch with 10G uplink series**（19 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-448XGGGM(L3) | LT-IS6516XG-4XS4GX8GT | Industrial L3, 8*10/100/1000Base-T RJ45,4*100/1000Base-X SFP, 4*1G/2.5G/10G SFP+ | 1900 | 340.8 | 355.0 | 369.2 | 363.0 | L3 |
| STI-448XGGGPM(L3) | LT-IS6516XGP-4XS4GX8GT | PoE 衍生型（同主型规格 + PoE） | 1980 | 355.2 | 370.0 | 384.8 | 385.0 | L3 |
| STI-2160XGGM(L3) | LT-IS6518XG-2XS16GT | Industrial L3, 16*10/100/1000Base-T RJ45, 2*1G/2.5G/10G SFP+ | 2000 | 358.7 | 373.7 | 388.6 | 385.0 | L3 |
| STI-21616XGGPM(L3) | LT-IS6518XGP-2XS16GT | PoE 衍生型（同主型规格 + PoE） | 2160 | 387.4 | 403.6 | 419.7 | 412.5 | L3 |
| —（沿用 LT-） | LT-IS6520XG-4XS8GX8GT | Industrial L3, 8*10/100/1000Base-T RJ45, 8*100/1000Base-X SFP, 4*1G/2.5G/10G SFP+ | 2280 | 409.0 | 426.0 | 443.0 |  | 工业 L3：8×GE + 8×SFP + 4×10G——Saga L3 档无此端口组合，沿用 SmartByte 并注明 |
| STI-4160XGGM | LT-IS6520XG-4XS16GT | Industrial L3, 16*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+ | 2350 | 421.5 | 439.1 | 456.7 | 462.0 | L3 |
| STI-41616XGGPM | LT-IS6520XGP-4XS16GT | PoE 衍生型（同主型规格 + PoE） | 2510 | 450.2 | 469.0 | 487.7 | 495.0 | L3 |
| STI-41616XGGPM-4BT | LT-IS6520XGP-4XS16GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2710 | 486.1 | 506.4 | 526.6 | 528.0 | L3 |
| STI-4240XGGM(L3) | LT-IS6528XG-4XS24GT | Industrial L3, 24*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+ | 2460 | 441.3 | 459.6 | 478.0 | 478.5 | L3 |
| STI-42424XGGPM(L3) | LT-IS6528XGP-4XS24GT | PoE 衍生型（同主型规格 + PoE） | 2700 | 484.3 | 504.5 | 524.7 | 517.0 | L3 |
| STI-42424XGGPM-4BT(L3) | LT-IS6528XGP-4XS24GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2900 | 520.2 | 541.9 | 563.5 | 550.0 | L3 |
| STI-4240XGGM-U(L3) | LT-IS6528XG-4XS24GT-U | Industrial L3, 24*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+, rack-mount | 2600 | 466.4 | 485.8 | 505.2 | 506.0 | L3 |
| STI-42424XGGPM-U(L3) | LT-IS6528XGP-4XS24GT-U | PoE 衍生型（同主型规格 + PoE） | 2900 | 520.2 | 541.9 | 563.5 | 550.0 | L3 |
| STI-42424XGGPM-U-2BT(L3) | LT-IS6528XGP-4XS24GT-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 3000 | 538.1 | 560.5 | 583.0 | 583.0 | L3 |
| STI-4816XGCGM-U | LT-IS6528XG-4XS16GT8GC-U | Industrial L3, 16*10/100/1000Base-T RJ45, 8*gigabit Combo, 4*1G/2.5G/10G SFP+, rack-mount | 2900 | 520.2 | 541.9 | 563.5 | 572.0 | L3 |
| STI-4816XGCGPM-U | LT-IS6528XGP-4XS16GT8GC-U | PoE 衍生型（同主型规格 + PoE） | 3060 | 548.9 | 571.7 | 594.6 | 605.0 | L3 |
| STI-4816XGCGPM-U-2BT | LT-IS6528XGP-4XS16GT8GC-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 3160 | 566.8 | 590.4 | 614.1 | 638.0 | L3 |
| STI-4168XGGCM-U(L3) | LT-IS6528XG-4XS16GX8GC-U | Industrial L3, 16*100/1000Base-X SFP, 8*gigabit Combo, 4*1G/2.5G/10G SFP+, rack-mount | 3100 | 556.1 | 579.2 | 602.4 | 605.0 | L3 |
| STI-4480XGGM-U | LT-IS6552XG-4XS48GT-U | Industrial L3, 48*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+, rack-mount | 4500 | 807.2 | 840.8 | 874.4 | 847.0 | L3 |

**Layer 3 Managed Ethernet Switches, 10G uplink series (Supports static and dynam**（8 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STC-424XGGM(L3) | LT-S8528XG-4XS24GT | 4*10G/2.5G/1G SFP+ ports ，24*10/100/1000M RJ45 ports, without SFP module, Layer 3 management | 1500 | 269.1 | 280.3 | 291.5 | 295.0 | L3 |
| STC-424XGGPM(L3) | LT-S8528XGP-4XS24GT | 4*10G/2.5G/1G SFP+ ports ，24*10/100/1000M RJ45 ports, without SFP module, Layer 3 management ,single AC power… | 1900 | 340.8 | 355.0 | 369.2 | 374.0 | L3 |
| STC-4816XGCGM | LT-IS8528XG-4XS16GT8GC | 4*10G/2.5G/1G SFP+ slots，16*10/100/1000M RJ45 ports，8*GE COMBO ports, without SFP module, Layer 3 management | 1600 | 287.0 | 299.0 | 310.9 | 353.0 | L3 |
| STC-4816XGCGPM | LT-IS8528XGP-4XS16GT8GC | 4*10G/2.5G/1G SFP+ slots，16*10/100/1000M RJ45 ports，8*GE COMBO ports, without SFP module, Layer 3 management,… | 2000 | 358.7 | 373.7 | 388.6 | 611.0 | L3 |
| STC-4168XGGCM | LT-S8528XG-4XS16GX8GC | 4*10G/2.5G/1G SFP+ slots，16*1G SFP ports，8*GE COMBO ports, without SFP module, Layer 3 management | 2100 | 376.7 | 392.4 | 408.1 | 413.0 | L3 |
| STC-448XGGM(L3) | LT-S8552XG-4XS48GT | 4*10G/2.5G/1G SFP+ ports ，48*10/100/1000M RJ45 ports, without SFP module, Layer 3 management | 2600 | 466.4 | 485.8 | 505.2 | 512.0 | L3 |
| STC-448XGGPM(L3) | LT-S8552XGP-4XS48GT | 4*10G/2.5G/1G SFP+ ports ，48*10/100/1000M RJ45 ports, without SFP module, Layer 3 management , single AC powe… | 3100 | 556.1 | 579.2 | 602.4 | 583.0 | L3 |
| STC-448XGGMO | LT-S8552XG-4XS48GX | 4*1G/2.5G/10G SFP+ ports ，48*1G SFP ports, without SFP module, Layer 3 management, single AC power supply | 3500 | 627.8 | 654.0 | 680.1 | 688.0 | L3 |

**Layer 2+ Managed Ethernet Switch Non-PoE/PoE Series(Support DHCP server, IPv4/IP**（11 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STC-28DGGM | LT-S8310G-2GX8GT | L2+, 8*10/100/1000Base-T + 4*1G/2.5G SFP | 380 | 68.2 | 71.0 | 73.8 | 85.0 | L2+ |
| STC-28DGGPM | LT-S8310GP-2GX8GT | L2+, 8*10/100/1000Base-T PoE + 4*1G/2.5G SFP, 120W power supply | 450 | 80.7 | 84.1 | 87.4 | 99.0 | L2+ |
| STC-424DGGM | LT-S8328G-4GX24GT-S | L2 +, 24*10/100/1000Base-T + 4*1G/2.5G SFP, AC5爆款 | 460 | 82.5 | 85.9 | 89.4 | 110.0 | L2+ |
| STC-424DGGPM-280W | LT-S8328GP-4GX24GT-S | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G SFP, AC5爆款,280W power supply | 750 | 134.5 | 140.1 | 145.7 | 165.0 | L2+ |
| STC-424DGGPM-440W | LT-S8328GP-4GX24GT | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G SFP,440W power supply | 1200 | 215.2 | 224.2 | 233.2 | 220.0 | L2+ |
| STC-424XGGM | LT-S8328XG-4XS24GT-S | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G/10G SFP+, AC5 爆款 | 710 | 127.4 | 132.7 | 138.0 | 143.0 | L2+（另有 L3 档） |
| STC-424XGGPM-280W | LT-S8328XGP-4XS24GT-S | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G/10G SFP+, AC5爆款,280W power supply | 1010 | 181.2 | 188.7 | 196.3 | 198.0 | L2+ |
| STC-448DGGM | LT-S8352G-4GX48GT | L2+, 48*10/100/1000Base-T + 4*1G/2.5G SFP | 1320 | 236.8 | 246.6 | 256.5 | 220.0 | L2+ |
| STC-448DGGPM | LT-S8352GP-4GX48GT | L2+, 48*10/100/1000Base-T PoE+ 4*1G/2.5G SFP, 440W power supply; 850W power supply optional | 1720 | 308.5 | 321.4 | 334.2 | 308.0 | L2+ |
| STC-448XGGM | LT-S8352XG-4XS48GT | L2+, 48*10/100/1000Base-T + 4*1G/2.5G SFP | 1470 | 263.7 | 274.7 | 285.7 | 286.0 | L2+（另有 L3 档） |
| STC-448XGGPM | LT-S8352XGP-4XS48GT | L2+, 48*10/100/1000Base-T PoE+ 4*1G/2.5G/10G SFP+, 440W power supply; 850W power supply optional | 1870 | 335.4 | 349.4 | 363.4 | 369.0 | L2+（另有 L3 档） |

**Unmanaged Ultra-compact Industrial Fast Media Converters(PoE/Non-PoE)**（6 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-110FE | LT-IMC30F-E | ● 1*10/100Base-TX RJ45 port, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 12~58V input, redundant p… | 110 | 19.7 | 20.6 | 21.4 | 23.1 | 1×FE + 1×100M SFP |
| STI-111FP | LT-IMC30FP-E | ● 1*10/100Base-TX RJ45 PoE/PoE+ port, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 44~57V input, re… | 140 | 25.1 | 26.2 | 27.2 | 29.7 | 1×FE PoE + 1×100M SFP |
| STI-120FE | LT-IMC30F-1FX2TX-E | ● 2*10/100Base-TX RJ45 port, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 12~58V input, redundant p… | 120 | 21.5 | 22.4 | 23.3 | 26.4 | 2×FE + 1×100M SFP |
| STI-122FP | LT-IMC30FP-1FX2TX-E | ● 2*10/100Base-TX RJ45 PoE/PoE+ port, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 44~57V input, re… | 150 | 26.9 | 28.0 | 29.1 | 33.0 | 2×FE PoE + 1×100M SFP |
| STI-220FE | LT-IMC30F-2FX2TX-E | ● 2*10/100Base-TX RJ45 port, 2*100Base-FX SFP port / ● DC 12~58V input, redundant power supply with polarity … | 140 | 25.1 | 26.2 | 27.2 | 29.7 | 2×FE + 2×100M SFP |
| STI-222FP | LT-IMC30FP-2FX2TX-E | ● 2*10/100Base-TX RJ45 PoE/PoE+ port, 2*100Base-FX SFP port / ● DC 44~57V input, redundant power supply with … | 170 | 30.5 | 31.8 | 33.0 | 36.3 | 2×FE PoE + 2×100M SFP |

**Unmanaged Ultra-compact Industrial Gigabit Media Converters(PoE/Non-PoE)**（6 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-110GE | LT-IMC30G-E | ●1*10/100/1000Base-T RJ45 port, 1*100/1000Base-X SFP(/SC/ST/FC optional) fiber port / ● DC 12~58V input, redu… | 125 | 22.4 | 23.4 | 24.3 | 29.7 | 1×GE + 1×1G SFP |
| STI-111GP | LT-IMC30GP-E | ● 1*10/100/1000Base-T RJ45 PoE/PoE+ port, 1*100/1000Base-X SFP(/SC/ST/FC optional) fiber port / ● DC 44~57V i… | 155 | 27.8 | 29.0 | 30.1 | 36.3 | 1×GE PoE + 1×1G SFP |
| STI-120GE | LT-IMC30G-1GX2GT-E | ● 2*10/100/1000Base-T RJ45 ports, 1*100/1000Base-X SFP(/SC/ST/FC optional) fiber port / ● DC 12~58V input, re… | 135 | 24.2 | 25.2 | 26.2 | 29.7 | 2×GE + 1×1G SFP |
| STI-122GP | LT-IMC30GP-1GX2GT-E | ● 2*10/100/1000Base-T RJ45 PoE/PoE+ ports, 1*100/1000Base-X SFP(/SC/ST/FC optional) fiber port / ● DC 44~57V … | 165 | 29.6 | 30.8 | 32.1 | 36.3 | 2×GE PoE + 1×1G SFP |
| STI-220GE | LT-IMC30G-2GX2GT-E | ● 2*2*10/100/1000Base-T RJ45 ports, 2*100/1000Base-X SFP ports / ● DC 12~58V input, redundant power supply wi… | 155 | 27.8 | 29.0 | 30.1 | 36.3 | 2×GE + 2×1G SFP |
| STI-222GP | LT-IMC30GP-2GX2GT-E | ● 2*10/100/1000Base-T RJ45 PoE ports, 2*100/1000Base-X SFP ports / ● DC 44~57V input, redundant power supply … | 185 | 33.2 | 34.6 | 35.9 | 39.6 | 2×GE PoE + 2×1G SFP |

**Unmanaged Industrial Ethernet Switches**（15 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-140FE | LT-IS3005F-1FX4TX | ● 4*10/100Base-TX RJ45 ports, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 12~58V input, redundant … | 130 | 23.3 | 24.3 | 25.3 | 29.7 | 4×FE + 1×100M SFP |
| STI-050FE | LT-IS3005F-5TX-M | ● 5*10/100Base-TX RJ45 ports / ● DC 12~36V input, redundant power supply with polarity reverse/over-voltage p… | 85 | 15.2 | 15.9 | 16.5 | 27.5 | 5×FE（Saga 为 DC12-58V；SmartByte -M 为 12-36V——核对） |
| STI-050FE | LT-IS3005F-5TX-E | ● 5*10/100Base-TX RJ45 ports（NO.5 is the uplink port) / ● DC 12~58V input, redundant power supply with polari… | 122 | 21.9 | 22.8 | 23.7 | 27.5 | 5×FE |
| STI-240FE | LT-IS3006F-2FX4TX | ● 4*10/100Base-TX RJ45 ports, 2*100Base-FX SFP fiber ports / ● DC 12~58V input, redundant power supply with p… | 140 | 25.1 | 26.2 | 27.2 | 33.0 | 4×FE + 2×100M SFP |
| STI-080FE | LT-IS3008F-8TX | ● 8*10/100M RJ45 ports(No.8 is uplink port) / ● DC 12~58V input, redundant power supply with polarity reverse… | 136 | 24.4 | 25.4 | 26.4 | 44.0 | 8×FE |
| STI-180FE | LT-IS3009F-1FX8TX | ● 8*10/100Base-TX RJ45 ports, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 12~58V input, redundant … | 155 | 27.8 | 29.0 | 30.1 | 48.4 | 8×FE + 1×100M SFP |
| STI-050GE | LT-IS3005G-5GT-M | ● 5*10/100/1000Base-TX RJ45 ports / ● DC 12~36V input, redundant power supply with polarity reverse/over-volt… | 95 | 17.0 | 17.8 | 18.5 | 34.1 | 5×GE（电压范围核对） |
| STI-050GE | LT-IS3005G-5GT | ● 4*10/100/1000Base-T RJ45 ports downlink, 1*10/100/1000Base-T RJ45 port uplink / ● DC 12~58V input, redundan… | 134 | 24.0 | 25.0 | 26.0 | 34.1 | 5×GE |
| STI-140GE | LT-IS3005G-1GX4GT | ● 4*10/100/1000M RJ45 ports, 1*1000Base-X SFP(/SC/ST/FC optional) fiber port / ● DC 12~58V input, redundant p… | 150 | 26.9 | 28.0 | 29.1 | 37.4 | 4×GE + 1×1G SFP |
| STI-150GE | LT-IS3006G-1GT1GX4GT | ● 4*10/100/1000M RJ45 ports downlink, 1*1000Base-X SFP port and 1*10/100/1000Base-T RJ45 port uplink / ● DC 1… | 170 | 30.5 | 31.8 | 33.0 | 42.9 | 5×GE + 1×1G SFP |
| STI-240GE | LT-IS3006G-2GX4GT | ● 4*10/100/1000M RJ45 ports, 2*1000Base-X SFP fiber ports / ● DC 12~58V input, redundant power supply with po… | 156 | 28.0 | 29.1 | 30.3 | 40.7 | 4×GE + 2×1G SFP |
| STI-080GE | LT-IS3008G-8GT | ● 8*10/100/1000M RJ45 ports(No.8 is uplink port) / ● DC 12~58V input, redundant power supply with polarity re… | 175 | 31.4 | 32.7 | 34.0 | 55.0 | 8×GE |
| STI-280GE | LT-IS3010G-2GX8GT | ●8*10/100/1000M RJ45 ports, 2*1000Base-X SFP (/SC/ST/FC optional) fiber ports / ● DC 12~58V input, redundant … | 260 | 46.6 | 48.6 | 50.5 | 63.8 | 8×GE + 2×1G SFP |
| STI-0160GE | LT-IS6016G-16GT | ●16*10/100/1000Base-T RJ45 ports / ● Redundant power DC 12-58V input with polarity reverse/over-voltage/over-… | 510 | 91.5 | 95.3 | 99.1 | 115.5 | 16×GE |
| STI-2160GE | LT-IS6018G-2GX16GT | ●16*10/100/1000Base-T RJ45 ports, 2*1000Base-X SFP slots / ● Redundant power DC 12-58V input with polarity re… | 790 | 141.7 | 147.6 | 153.5 | 170.5 | 16×GE + 2×1G SFP |

**Unmanaged Industrial PoE Switches**（14 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| STI-144FP | LT-IS3005FP-1FX4TX | ●4*10/100Base-TX RJ45 PoE ports, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 44~57V input, redunda… | 170 | 30.5 | 31.8 | 33.0 | 37.4 | 4×FE PoE + 1×100M SFP |
| STI-054FP | LT-IS3005FP-5TX | ●4*10/100Base-TX RJ45 PoE ports downlink , 1*10/100Base-TX RJ45 port uplink / ● DC 44~57V input, redundant po… | 162 | 29.1 | 30.3 | 31.5 | 35.2 | 4×FE PoE + 1×FE 上联 |
| STI-244FP | LT-IS3006FP-2FX4TX | ● 4*10/100Base-TX RJ45 ports, 2*100Base-FX SFP fiber ports / ● DC 44~57V input, redundant power supply with p… | 180 | 32.3 | 33.6 | 35.0 | 40.7 | 4×FE PoE + 2×100M SFP |
| STI-088FP | LT-IS3008FP-8TX | ● 8*10/100M RJ45 ports(No.8 is uplink port) / ● DC 44~57V input, redundant power supply with polarity reverse… | 196 | 35.2 | 36.6 | 38.1 | 51.7 | 8×FE PoE |
| STI-188FP | LT-IS3009FP-1FX8TX | ● 8*10/100Base-TX RJ45 ports, 1*100Base-FX SFP(/SC/ST/FC optional) fiber port / ● DC 44~57V input, redundant … | 215 | 38.6 | 40.2 | 41.8 | 56.1 | 8×FE PoE + 1×100M SFP |
| STI-054GP | LT-IS3005GP-5GT | ● 4*10/100/1000Base-T PoE downlink, 1*10/100/1000Base-T RJ45 uplink / ● DC 44~57V input, redundant power supp… | 174 | 31.2 | 32.5 | 33.8 | 42.9 | 4×GE PoE + 1×GE 上联 |
| STI-144GP | LT-IS3005GP-1GX4GT | ● 4*10/100/1000Base-T PoE downlink, 1*1000Base-X SFP uplink / ● DC 44~57V input, redundant power supply with … | 190 | 34.1 | 35.5 | 36.9 | 46.2 | 4×GE PoE + 1×1G SFP |
| STI-154GP | LT-IS3006GP-1GT1GX4GT | ● 4*10/100/1000M RJ45 ports downlink, 1*1000Base-X SFP port and 1*10/100/1000Base-T RJ45 port uplink / ● DC 4… | 210 | 37.7 | 39.2 | 40.8 | 51.7 | 4×GE PoE + 1×GE + 1×1G SFP |
| STI-244GP | LT-IS3006GP-2GX4GT | ● 4*10/100/1000Base-T RJ45 PoE ports, 2*1000Base-X SFP ports / ● DC 44~57V input, redundant power supply with… | 196 | 35.2 | 36.6 | 38.1 | 49.5 | 4×GE PoE + 2×1G SFP |
| STI-088GP | LT-IS3008GP-8GT | ● 8*10/100/1000Base-T PoE ports / ● DC 44~57V input, redundant power supply with polarity reverse/over-voltag… | 235 | 42.2 | 43.9 | 45.7 | 66.0 | 8×GE PoE |
| STI-288GP | LT-IS3010GP-2GX8GT | ● 8*10/100/1000Base-T RJ45 PoE ports, 2*1000Base-X SFP ports / ● DC 44~57V input, redundant power supply with… | 320 | 57.4 | 59.8 | 62.2 | 74.8 | 8×GE PoE + 2×1G SFP |
| STI-488GP | LT-IS6012GP-4GX8GT | ● 8*10/100/1000Base-T RJ45 PoE ports, 4*1000Base-X SFP ports / ● DC 44~57V input, redundant power supply with… | 600 | 107.6 | 112.1 | 116.6 | 132.0 | 8×GE PoE + 4×1G SFP（Saga PDF 规格行写 2 port Fiber，型号名为 488——报价… |
| STI-01616GP | LT-IS6016GP-16GT | ● 16*10/100/1000Base-T RJ45 PoE/PoE+ ports / ● DC 44~57V input, redundant power supply with polarity reverse/… | 670 | 120.2 | 125.2 | 130.2 | 143.0 | 16×GE PoE |
| STI-21616GP | LT-IS6018GP-2GX16GT | ● 16*10/100/1000Base-T RJ45 PoE ports, 2*1000Base-X SFP slots / ● DC 44~57V input, redundant power supply wit… | 950 | 170.4 | 177.5 | 184.6 | 203.5 | 16×GE PoE + 2×1G SFP |

**1 channel single fiber Bypass**（6 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| —（沿用 LT-） | LT-IS6312G-4GX8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots and 1 cha… | 960 | 172.2 | 179.4 | 186.5 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312GP-4GX8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 4*1G/2.5GBase-X SFP slots and 1… | 1040 | 186.5 | 194.3 | 202.1 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312GP-4GX8GT-2BT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 1-2 ports support PoE++ 60-90W,… | 1140 | 204.5 | 213.0 | 221.5 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312XG-4XS8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP+ slots and … | 1160 | 208.1 | 216.7 | 225.4 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312XGP-4XS8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 4*1G/2.5G/10GBase-X SFP+ slots … | 1240 | 222.4 | 231.7 | 241.0 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312XGP-4XS8GT-2BT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 1-2 ports support PoE++ 60-90W,… | 1340 | 240.4 | 250.4 | 260.4 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |

**2 channels single fiber Bypass or 1 channel dual fiber Bypass**（6 款）

| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |
|---|---|---|---|---|---|---|---|---|
| —（沿用 LT-） | LT-IS6312G-4GX8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots and 2 cha… | 1260 | 226.0 | 235.4 | 244.8 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312GP-4GX8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 4*1G/2.5GBase-X SFP slots and 2… | 1340 | 240.4 | 250.4 | 260.4 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312GP-4GX8GT-2BT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 1-2 ports support PoE++ 60-90W,… | 1440 | 258.3 | 269.1 | 279.8 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312XG-4XS8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP+ slots and … | 1460 | 261.9 | 272.8 | 283.7 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312XGP-4XS8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 4*1G/2.5G/10GBase-X SFP+ slots … | 1540 | 276.2 | 287.7 | 299.3 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| —（沿用 LT-） | LT-IS6312XGP-4XS8GT-2BT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE ports, 1-2 ports support PoE++ 60-90W,… | 1640 | 294.2 | 306.4 | 318.7 |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |

- **Saga 暂无对应型号（17 款，只能写 SmartByte LT- 型号并注明「Saga 暂无对应型号，沿用 SmartByte 型号 LT-xxx」）**：LT-IS6320G-4GX16GT-D、LT-IS6320GP-4GX16GT-D、LT-IS6320GP-4GX16GT-D-4BT、LT-IS6312XGP-4XS8GT-2BT、LT-IS6520XG-4XS8GX8GT、LT-IS6312G-4GX8GT-FBP、LT-IS6312GP-4GX8GT-FBP、LT-IS6312GP-4GX8GT-2BT-FBP、LT-IS6312XG-4XS8GT-FBP、LT-IS6312XGP-4XS8GT-FBP、LT-IS6312XGP-4XS8GT-2BT-FBP、LT-IS6312G-4GX8GT-2FBP、LT-IS6312GP-4GX8GT-2FBP、LT-IS6312GP-4GX8GT-2BT-2FBP、LT-IS6312XG-4XS8GT-2FBP、LT-IS6312XGP-4XS8GT-2FBP、LT-IS6312XGP-4XS8GT-2BT-2FBP

#### 5.3.2 HRUI 洪瑞 / Realtek 线（`data/价格主表_HRUI.csv`，55 行，CNY 不含税含运费，来源《洪瑞报价-天龙2026930.xls》，汇率 6.69 @ 2026-10-17）

> 用法：只在客户自己说 Realtek / 低价 / 功能简单时给；报价按本表（2026-09-30 新进价）重算，不要用 Drive 2026 Q3 老美元表（39 款隐含加价 <20%，Q-47）。ZX- 为洪瑞报价单中性型号；「Saga 对应型号」空 = 尚未对照（Q-42）。

| ZX 型号 | Saga 对应型号 | 品名 | 规格摘要 | CNY 成本 | USD +20% | USD +25% | USD +30% | 最近采购价 RMB / 日期 |
|---|---|---|---|---|---|---|---|---|
| ZX-SW0050 |  | 5口百兆以太网交换机 | 5个百兆网口，背板带宽1.0Gbps，DC5V1A，金属外壳，桌面式 | 26.5 | 4.8 | 5.0 | 5.1 |  |
| ZX-SW0080 |  | 8口百兆以太网交换机 | 8个百兆网口，背板带宽1.6Gbps，DC5V1A，金属外壳，桌面式 | 35.0 | 6.3 | 6.5 | 6.8 |  |
| ZX-SWG1050 | STC-05GE | 5口千兆以太网交换机 | 5个千兆网口 DC5V1A，金属外壳 背板带宽10Gbps | 33.0 | 5.9 | 6.2 | 6.4 |  |
| ZX-SWG1080 | STC-08GE | 8口千兆以太网交换机 | 5个千兆网口 DC5V1A，金属外壳 背板带宽10Gbps | 56.0 | 10.0 | 10.5 | 10.9 |  |
| ZX-SWG10160D | STC-016GE | 16口千兆以太网交换机 | 端口形态：16*GE 背板带宽：32Gbps 电源规格：AC100-240V 12V1A 硬件功能：VLAN、Default、Extend 三种模式、环路告警、QoS优先级 | 182.0 | 32.6 | 34.0 | 35.4 |  |
| ZX-SWG10240D | STC-024GE-D / STC-024GE-U | 24口千兆以太网交换机 | 24个千兆网口，AC220V，金属外壳，桌面式，内置电源，12V2A，支持VLAN、Extend、环路告警，背板带宽48Gbps，默认搭配1U挂耳，支持机架安装 | 249.0 | 44.7 | 46.5 | 48.4 |  |
| ZX-SWG10240 | STC-024GE-D / STC-024GE-U | 24口千兆以太网交换机 | 24个千兆网口，AC220V，金属外壳，桌面式，内置电源，12V2A，支持VLAN、Extend、环路告警，背板带宽48Gbps，标准1U机架式 | 285.0 | 51.1 | 53.3 | 55.4 |  |
| ZX-SWG10242S | STC-224GE | 26口千兆以太网交换机 | 24个千兆网口+2个上联SFP口，AC220V，金属外壳，内置电源12V2A，支持VLAN、Extend，背板带宽52Gbps，1U机架式安装 | 310.0 | 55.6 | 57.9 | 60.2 |  |
| ZX-SWG10482S | STC-248GE | 50口千兆以太网交换机 | 48个千兆网口+2个上联SFP口，AC220V，金属外壳，内置电源12V4A，支持VLAN（1-46），背板带宽100Gbps，1U机架式安装 | 805.0 | 144.4 | 150.4 | 156.4 |  |
| ZX-SWG2082NS | STC-28GM | 10口千兆管理型以太网交换机 | 8个千兆网口+2个千兆SFP口+1个管理端口，背板带宽20Gbps，二层网络管理功能，支持路由、DHCP、VLAN、MAC地址、ACL访问控制、QOS、组播、风暴抑制、IPV4/IPV6等业务功能，… | 315.0 | 56.5 | 58.9 | 61.2 |  |
| ZX-SWG20244S | STC-424GM | 千兆28口管理型交换机 | 24个千兆网口+4个千兆SFP口+1个管理端口，背板带宽52Gbps，二层网络管理功能，支持路由、DHCP、VLAN、MAC地址、ACL访问控制、QOS、组播、风暴抑制、IPV4/IPV6等业务功能… | 590.0 | 105.8 | 110.2 | 114.6 | 530.0 / 2025-08-04 |
| ZX-SWTG3424S | STC-424XGGM | 28口万兆上联三层管理型以太网交换机 | 24个千兆下联网口+4个万兆上联SFP光口+1个USB串口+1个Console口，背板带宽128Gbps，三层网络管理功能，支持路由、DHCP、VLAN、MAC地址、ACL访问控制、QOS、组播、风… | 720.0 | 129.1 | 134.5 | 139.9 |  |
| ZX-SWTG342408F | STC-4248XGGCM | 28口万兆上联三层管理型以太网交换机 | 24个千兆SFP光口+8个千兆电口(光电复用)+4个万兆SFP光口+1个Console口背板带宽128Gbps，三层网络管理功能，支持路由、DHCP、VLAN、MAC地址、ACL访问控制、QOS、组… | 1750.0 | 313.9 | 327.0 | 340.1 | 1600.0 / 2024-02-19 |
| ZX-SWTG3448S | STC-448XGGM | 52口万兆上联三层管理型以太网交换机 | 48个千兆下联网口+4个万兆上联SFP光口+1个USB串口+1个Console口，背板带宽176Gbps，三层网络管理功能，支持路由、DHCP、VLAN、MAC地址、ACL访问控制、QOS、组播、风… | 1500.0 | 269.1 | 280.3 | 291.5 |  |
| ZX-SWTG3C12F | STC-120XGM | 12口万兆三层管理型以太网交换机 | 12个万兆SFP光口+1个Console口，背板带宽240Gbps，三层网络管理功能，支持路由、DHCP、VLAN、MAC地址、ACL访问控制、QOS、组播、风暴抑制、IPV4/IPV6等业务功能，… | 950.0 | 170.4 | 177.5 | 184.6 |  |
| ZX-SWTG3624AS | STC-624XGDGM | 30口管理型万兆上联2.5G 交换机 | 24个2.5G 网口+6个万兆上联SFP光口+1个Console口，背板带宽240Gbps，三层网络管理功能，支持路由、DHCP、VLAN、MAC地址、ACL访问控制、QOS、组播、风暴抑制、IPV… | 1900.0 | 340.8 | 355.0 | 369.2 |  |
| ZX902-AF-42N | STC-024FP | 百兆6口PoE交换机 | 5口10/100M交换机，其中1-4口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率55W，上联口1个百兆电口，背板带宽1.2Gbps，网口传输支持250米… | 57.0 | 10.2 | 10.7 | 11.1 |  |
| ZX902-AF-82N | STC-028FP | 百兆10口PoE交换机 | 10口10/100M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率96W，上联口2个百兆电口，背板带宽2.0Gbps，网口传输支持250… | 78.0 | 14.0 | 14.6 | 15.2 |  |
| ZX902-AF-82GN | STC-028GFP | 百千兆10口PoE交换机 | 10口10/100M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率120W，上联口2个千兆电口，背板带宽5.6Gbps，网口传输支持25… | 100.0 | 17.9 | 18.7 | 19.4 |  |
| ZX901-AF-821GNS | STC-128GFP | 百千兆11口PoE交换机 | 8个百兆PoE网口+2个千兆上联网口+1个千兆上联SFP光口 1-8口支持POE供电，兼容IEEE802.3af/at国际标准 3挡拨码支持VLAN、Default、Extend三种模式 | 130.0 | 23.3 | 24.3 | 25.3 |  |
| ZX902-AF-162G | STC-0216GFP | 百千兆18口PoE交换机 | 18口100/1000M混合型交换机，其中1-16口为百兆口，支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率200W，背板带宽7.2Gbps，上联口为2个千… | 215.0 | 38.6 | 40.2 | 41.8 |  |
| ZX902-AF-242G | STC-0224GFP | 百千兆26口PoE交换机 | 26口100/1000M混合型交换机，其中1-24口为百兆口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率300W，背板带宽8.8Gbps，上联口为2千兆电… | 315.0 | 56.5 | 58.9 | 61.2 |  |
| ZX902-AFG-411NS-65 | STC-114GP | 千兆6口PoE交换机 | 4个千兆PoE网口+1个千兆上联网口+1个千兆上联SFP光口 1-4口支持标准POE供电，兼容IEEE 802.3af/at国际标准 -10℃-50℃运行，4KV防雷，8KV防静电 AC 100-2… | 95.0 | 17.0 | 17.8 | 18.5 |  |
| ZX902-AFG-42NS-65 |  | 千兆6口PoE交换机 | 4个千兆PoE网口+2个千兆上联SFP光口 1-4口支持标准POE供电，兼容IEEE 802.3af/at国际标准 -10℃-50℃运行，4KV防雷，8KV防静电 AC 100-240V 输入，内置… | 125.0 | 22.4 | 23.4 | 24.3 |  |
| ZX902-AFG-42N-65 | STC-024GP | 千兆6口PoE交换机 | 4个千兆PoE网口+2个千兆上联网口 1-4口支持标准POE供电，兼容IEEE 802.3af/at国际标准 -10℃-50℃运行，4KV防雷，8KV防静电 AC 100-240V 输入，内置电源总… | 115.0 | 20.6 | 21.5 | 22.3 |  |
| ZX902-AFG-82N | STC-028GP / STC-208GP | 千兆10口PoE交换机 | 10口10/100/1000M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，上联口为2个千兆电口，整机总功率120W，背板带宽20.0Gbps | 140.0 | 25.1 | 26.2 | 27.2 |  |
| ZX902-AFG-822NS | STC-228GP | 千兆12口PoE交换机 | 12口10/100/1000M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率120W，背板带宽24Gbps，支持拨码Extend延长，支… | 185.0 | 33.2 | 34.6 | 35.9 |  |
| ZX-AFGM-82NS | STC-28GPM | 10口千兆管理型PoE交换机 | 8个千兆PoE网口+2个千兆SFP口+1个Console口，其中1-8口支持IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率120W，背板带宽20Gbps，二层网络管理功… | 396.0 | 71.0 | 74.0 | 77.0 | 355.1 / 2026-07-18 |
| ZX-AFGM-1622S-200 | STC-2216GPM | 20口千兆管理型PoE交换机 | 16个千兆PoE网口+2个千兆网口+2个千兆SFP光口+1个Console口，其中1-16口支持IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率200W，背板带宽40Gb… | 790.0 | 141.7 | 147.6 | 153.5 |  |
| ZX-AFGM-1622S-300 | STC-2216GPM | 20口千兆管理型PoE交换机 | 16个千兆PoE网口+2个千兆网口+2个千兆SFP光口+1个Console口，其中1-16口支持IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率300W，背板带宽40Gb… | 840.0 | 150.7 | 157.0 | 163.2 |  |
| ZX-AFGM-2444S-300 | STC-4424GCPM | 32口千兆管理型PoE交换机 | 24个千兆PoE网口+4个千兆网口+4个千兆SFP光口+1个Console口，其中1-24口支持IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率300W，背板带宽56Gb… | 900.0 | 161.4 | 168.2 | 174.9 | 820.0 / 2025-08-04 |
| ZX-AFGM-2444S-400 | STC-4424GCPM | 32口千兆管理型PoE交换机 | 24个千兆PoE网口+4个千兆网口+4个千兆SFP光口+1个Console口，其中1-24口支持IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率400W，背板带宽56Gb… | 960.0 | 172.2 | 179.4 | 186.5 |  |
| ZX200-AFGM-SWTG3424S-400 | STC-424XGGPM | 28口万兆上联三层管理型PoE交换机 | 24个千兆下联网口+4个万兆上联SFP+光口+1个USB串口+1个Console口，其中1-24口符合IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机PoE功率400W（双路电… | 1500.0 | 269.1 | 280.3 | 291.5 |  |
| ZX-AXGM-SWTG3448S-400 | STC-448XGGPM | 52口万兆上联三层管理型PoE交换机 | 48个千兆PoE网口+4个万兆上联SFP光口+1个USB串口+1个Console口，POE符合IEEE 802.3af/at/bt国际标准，1-8端口最大供电功率90W，整机总功率650W，背板带宽… | 2350.0 | 421.5 | 439.1 | 456.7 |  |
| ZX-AXGM-SWTG3624AS-450 | STC-624XGDGPM | 30口管理型万兆上联2.5G POE交换机 | 24个2.5G PoE网口+6个万兆上联SFP光口+1个Console口，其中1-4口符合IEEE 802.3af/at/bt国际标准，整机总功率450W，PoE输出400W，背板带宽240Gbps… | 2400.0 | 430.5 | 448.4 | 466.4 |  |
| ZX900-AFG-N301 |  | 30W千兆POE供电器 | 1路AC电源输入+1路千兆RJ45端口POE输出+1路千兆RJ45端口网络输入 输入电压：AC100-240V，输出电压：DC52V 输出功率：30W 供电线序：12+/36- 支持输出状态显示：L… | 46.0 | 8.3 | 8.6 | 8.9 |  |
| ZX-BTG-N601 |  | BT60W千兆POE供电器 | 1路AC电源输入+1路千兆RJ45端口POE输出+1路千兆RJ45端口网络输入 输入电压：AC100-240V，输出电压：DC52V 输出功率：60W 供电线序：12-/36+、45+/78- 支持… | 135.0 | 24.2 | 25.2 | 26.2 |  |
| ZX-BTG-N901 |  | BT90W千兆POE供电器 | 1路AC电源输入+1路千兆RJ45端口POE输出+1路千兆RJ45端口网络输入 输入电压：AC100-240V，输出电压：DC52V 输出功率：90W 供电线序：12-/36+、45+/78- 支持… | 154.0 | 27.6 | 28.8 | 29.9 |  |
| ZX900-AF-42N | STC-024FP | 百兆6口PoE交换机 | 6口10/100M交换机，其中1-4口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率65W，上联口2个百兆电口，背板带宽1.2Gbps，网口传输支持200米… | 62.0 | 11.1 | 11.6 | 12.0 |  |
| ZX900-AF-82N | STC-028FP | 百兆10口PoE交换机 | 10口10/100M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率120W，上联口2个百兆电口，背板带宽2.0Gbps，网口传输支持20… | 90.0 | 16.1 | 16.8 | 17.5 |  |
| ZX900-AF-82GN | STC-028GFP | 百千兆10口PoE交换机 | 10口10/100M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率120W，上联口2个千兆电口，背板带宽5.6Gbps，网口传输支持25… | 108.0 | 19.4 | 20.2 | 21.0 |  |
| ZX900-AF-1621GS-200 | STC-1216GFP | 百千兆19口PoE交换机 | 19口100/1000M混合型交换机，其中1-16口为百兆口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率200W，背板带宽9.2Gbps，上联口为2千兆电… | 249.0 | 44.7 | 46.5 | 48.4 |  |
| ZX900-AF-1621GS-300 | STC-1216GFP | 百千兆19口PoE交换机 | 19口100/1000M混合型交换机，其中1-16口为百兆口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率300W，背板带宽9.2Gbps，上联口为2千兆电… | 285.0 | 51.1 | 53.3 | 55.4 |  |
| ZX900-AF-2421GS-300 | STC-1224GFP | 百千兆27口智能型PoE交换机 | 27口100/1000M混合型交换机，其中1-24口为百兆口支持PoE，IEEE 802.3af/at国际标准，单端口供电功率最大30W，整机总功率300W，背板带宽10.8Gbps，上联口为2千兆… | 365.0 | 65.5 | 68.2 | 70.9 |  |
| ZX900-AFG-411NS | STC-114GP | 千兆6口PoE交换机 | 6口10/100/1000M交换机，其中1-4口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，上联口1个千兆电口+1个千兆光口，整机总功率65W，背板带宽12Gbps… | 115.0 | 20.6 | 21.5 | 22.3 |  |
| ZX900-AFG-42NS | STC-204GP | 千兆6口PoE交换机 | 6口10/100/1000M交换机，其中1-4口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，上联口2个千兆光口，整机总功率65W，背板带宽12Gbps，网口传输支持… | 135.0 | 24.2 | 25.2 | 26.2 |  |
| ZX900-AFG-42N | STC-024GP | 千兆6口POE交换机 | 6口10/100/1000M交换机，其中1-4口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，上联口2个千兆电口，整机总功率65W，背板带宽12Gbps，网口传输支持… | 115.0 | 20.6 | 21.5 | 22.3 |  |
| ZX900-AFG-82N | STC-028GP / STC-208GP | 千兆10口PoE交换机 | 10口10/100/1000M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率120W，背板带宽20Gbps，网口传输支持250米，支持拨… | 170.0 | 30.5 | 31.8 | 33.0 |  |
| ZX900-AFG-82NS |  | 千兆10口PoE交换机 | 10口10/100/1000M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率120W，背板带宽20Gbps，支持拨码Extend延长，支… | 180.0 | 32.3 | 33.6 | 35.0 |  |
| ZX900-AFG-822NS |  | 千兆12口PoE交换机 | 12口10/100/1000M交换机，其中1-8口支持PoE，IEEE 802.3af/at国际标准，单端口最大供电功率30W，整机总功率120W，背板带宽24Gbps，支持拨码Extend延长，支… | 200.0 | 35.9 | 37.4 | 38.9 |  |
| ZX900-AFG-1622S-200 | STC-2216GP | 千兆20口PoE交换机 | 20口千兆交换机，支持PoE，IEEE 802.3af/at国际标准，整机总功率200W，背板带宽40Gbps，上联口为2千兆电口，2个千兆SFP光口，支持POE优先级，从1至16口依次顺序，支持拨… | 350.0 | 62.8 | 65.4 | 68.0 |  |
| ZX900-AFG-1622S-300 | STC-2216GP | 千兆20口PoE交换机 | 20口千兆交换机，支持PoE，IEEE 802.3af/at国际标准，整机总功率300W，背板带宽40Gbps，上联口为2千兆电口，2个千兆SFP光口，支持POE优先级，从1至16口依次顺序，支持拨… | 425.0 | 76.2 | 79.4 | 82.6 |  |
| ZX900-AFG-2422S-300D | STC-2224GP | 千兆28口PoE交换机 | 28口千兆交换机，支持PoE，IEEE 802.3af/at国际标准，整机总功率300W，背板带宽56Gbps，上联口为2千兆电口，2个千兆SFP光口，支持POE优先级，从1至24口依次顺序，支持拨… | 470.0 | 84.3 | 87.8 | 91.3 |  |
| ZX900-AFG-2422S-300 | STC-2224GP | 千兆28口PoE交换机 | 28口千兆交换机，支持PoE，IEEE 802.3af/at国际标准，整机总功率300W，背板带宽56Gbps，上联口为2千兆电口，2个千兆SFP光口，支持POE优先级，从1至24口依次顺序，支持拨… | 490.0 | 87.9 | 91.6 | 95.2 |  |
| ZX900-AFG-2422S-400 | STC-2224GP | 千兆28口PoE交换机 | 28口千兆交换机，支持PoE，IEEE 802.3af/at国际标准，整机总功率400W，背板带宽56Gbps，上联口为2千兆电口，2个千兆SFP光口，支持POE优先级，从1至24口依次顺序，支持拨… | 545.0 | 97.8 | 101.8 | 105.9 |  |

### 5.4 Saga 暂无对应、不要承诺的产品形态（范围护栏）

Saga **没有**（信稿 / 报价里出现即错，客户点名问时按 §9.4 两层答法）：反向 PoE、PoE 注入器 / 分离器单卖、光模块 / SFP 单卖（只随整机）、Bypass / TAP（Saga 无对应型号，只能沿用 LT- 型号且标注）、GPON / OLT / ONT、Wi-Fi / AP、M12 轨交、HDMI、百兆介质转换器以外的 MC（只有 STC-110XGE 为 10G MC）、WDM、升压 PoE（Booster 线未进价表）、机柜 / 配件、路由器、定制 ODM 开发、PoE BT 整机（只有 -2BT/-4BT 部分口）、L3 工业机以外的 L3 功能承诺、被动 PoE 整机（只有 -24V/-Auto 三款）、KC 认证、云管理 / 控制器 / REST API、堆叠（AC5 线；CENTEC STH1G 可堆叠 ≤8 台 / 360 Gbps 是另一层）、2.5G **铜口**（AC5 线 2.5G 只在 SFP/SFP+ 笼子；CENTEC 有 Multi-Gig 铜口但无价无现货；Realtek 商用线有 2.5G/10G 铜口 → 待 SB-263 裁定）、SFP28+ 高速 Marvell、SDK / 源码（「source code mode is NEVER an option」）、Cisco 私有协议（CDP/HSRP）、NAT / TSN / MPLS（AC5）/ SD-WAN / BFD / IP SLA / PIM-DM / RIPng / PBR（AC5）。

---

## 6. 技术能力与边界

### 6.1 AC5 7.5 L2+ 功能表（已核，`Saga Feature List_7.5.x_L2+.xlsx`）

HTTPS ☑ · SNMP v1/v2c/v3 ☑ · SSH2 ☑ · SFTP/SCP Client+Server ☑ · sFlow ☑ · MQTT ☑ · PIM-SM ☑（仅 CLI）· ERPS <20 ms ☑（单环/相切/相交）· LACP 64 组 ☑ · 静态路由 v4/v6 ☑ · IGMP Snooping / VLAN / QoS / ACL（AC5 3K–6K 条 vs Realtek 256–512）· LLDP · Syslog · Voice VLAN · PoE watchdog / 定时 / 250 m 延长（工业 PoE）。**无** MLAG / OSPF / RIP / VRRP / NAT（L2+ 档）；L3 型号另有 RIP/OSPF（按型号表）。「高阶管理 = 可编程 + API」是早期思路，**现行口径不卖 API**。

### 6.2 硬件事实

- 工作温度：非 PoE / PoE ≤240W **-40 ~ +75 ℃**（部分 +70 ℃）；370W 机型 -40 ~ +60 ℃；防护 **IP40**（NOT IP67/IP68）；CENTEC 0 ~ 40 ℃（Netaş 曾指不够）。
- 工业机 DC 12–58 V（部分 12–75 V）冗余输入、极性反接/过载保护；PoE 机 DC 44–57 V；`-U` 机架型 AC/DC 冗余。
- PoE：802.3af/at 标配；bt 60–90 W 只在 `-2BT/-4BT` 衍生型的 1–2/1–4 口；PoE 机 GUI 只显示 **PD 侧**电压/功率，不显示交换机自身输入电压。
- 单台重量/尺寸（报 DAP 直接用）：STI-21616DGGPM/XGGPM 158×115×54 mm 净 1.2 kg（12 台/箱 20 kg）；STI-288DGGPM 1.2 kg；8 口管理型与 STI-21616DGGPM 同尺寸（一款彩盒通用）；STC-424XGGPM ≈3.4–3.5 kg，440×180/205×44 mm；STC-448XGGPM ≈5.6 kg；STC-2224GFP-24V 2.9/3.6 kg，440×290×45 mm；SmartByte 原箱 8 PoE+2 SFP 两台/箱 3 kg，24/48 口机 10.6 kg（53.5×20.5×40.8 cm）；ANW-2116-PG 8 台/箱 21 kg。
- 芯片（Case 1 德国客户问答）：Marvell 98DX336S + 88E1680 + 88E1548（AC3 代）；PoE 用独立小板；无 TSN、无 virtual stacking；10G 收发器 LT-MC80X 用 Marvell 88X3310 PHY。
- 出货前 **5 个工作日稳定性测试**（公司政策；常订型号 STI-244GP、STI-050GE 只做 8 小时老化）。

### 6.3 OEM / ODM 菜单（对外英文可直接用）

"Company logo / Packaging / Front panel (PVC mask) / Product label / Model name / Serial number / User manual / Default login IP / SNMP OID customization / Web GUI language — all mature options. We can also discuss firmware customization for specific project requirements, subject to technical evaluation."

| 项目 | 口径 |
|---|---|
| 免费、1 台也做 | logo、型号名、SN、MAC 段、默认登录 IP、SNMP OID、Web UI logo、标签、彩盒去 Made in China |
| 收费 / 有 MOQ | Web UI 配色/字体（「改码量大，样单不做」）、PVC 面膜丝印（整批开模，余料 Saga 代存；SA-006 $50 一次性）、定制彩盒 **$2.5/套、200 套起**（盒 + 异形泡棉 + 顶片 + 说明书）、特殊包装 |
| SKD / CKD / ODM | SKD 可做；CKD/ODM 需评估；**源代码不开放**；SDK/API 不作为卖点（2025-11 曾说「part of our TTC services」——不再使用） |
| 功能开发 | 只在**有订金 / 订单确认后**排期，否则不给时间表（AC5 加 SFTP 先例） |
| 中性包装 | 可做中性包装 / 标签；不打 Made in China；不出现 Saga 以外品牌痕迹（INH-04） |
| 文件 | COO 产地证 $15/份；其他认证文件复印件免费；**只发 Saga 名义证书**，SmartByte 名义（LT- 型号）证书不外发 |
| 自有 PEN | NYNEX 2025-03 发现 SmartByte 通用 MIB 含其他 OEM 企业 OID（.57430 / .56813 / .171 D-Link）；Q-35/Q-45 按 T29-U15 口径：**不申请不更换**（宣传 SmartByte 品牌是合作约定、订单归 Saga）；OEM 菜单里 SNMP OID 写 "Private MIB under your own IANA PEN (please send us your PEN) or under Saga's enterprise tree" |

### 6.4 Not-to-Do 清单（边界即资本）

合并版：云管理 / 控制器、EN50155 轨交 / 车载、IP67、消费级 / 家用路由、UL / E-mark / KC 行业、SFP28 及以上高速 Marvell、L3 组播级固件、SDK / 源码、国内公账单、视频营销 / Facebook / YouTube / 付费广告、极低价客户、「无未来的贸易商」、不尊重工程时间的、拉开会不买的、不稳定需求的项目型、无法连续复购的产品、OEM 贴牌的超重活、硬件售后「换新，不修」。客户需求命中清单 → 直接写「停点：边界」，不设计绕路。

### 6.5 认证登记（Saga 名义，可外发）

| 类别 | 证书号 / 报告号 | 日期 | 机构 | 标准 | 覆盖 |
|---|---|---|---|---|---|
| CE-EMC | JAT24070502534EC-1 / ER-1 | 2024-07-05 | 东莞骏安 Jun'an | EMC 2014/30/EU；EN 55032:2015+A11:2020；EN 55035:2017+A11:2020；EN IEC 61000-3-2/-3-3 | Ethernet Switch 24 型 |
| CE-LVD | JAT24070502534SC-1 / SR-1 | 2024-07-05 | 东莞骏安 | LVD 2014/35/EU；EN IEC 62368-1:2024 | 同上 |
| RoHS | JAT24070502534RC-1 / RR-1 | 2024-07-05 | 东莞骏安 | 2011/65/EU & (EU)2015/863 & 2017/2102 | 同上 |
| REACH | — / JAT24070502534CR-1 | 2024-07-05 | 东莞骏安 | SVHC 240 项 | 同上 |
| UKCA-EMC / LVD | JAT24070502535EC-1 / SC-1 | 2024-07-05 | 东莞骏安 | BS EN 55032 / 55035 / 61000-3 / BS EN IEC 62368-1:2024 | 同上 |
| FCC SDoC | NCT24028321XE1-1 | 2024-07-11 | 深圳中测通 NCT | 47 CFR Part 15 Subpart B | 同上 |
| 介质转换器 CE/FCC/RoHS | HK2104211224E / HK2104210402S / HK2104211225E / HK2104210399R | 2021-04-29 | 深圳华科 HUAK | 同上系列 | Media Converters |
| 介质转换器 UKCA | HTT202210092ER / LR | 2022-10-17 | 深圳华通 HTT | BS EN 55032 / 62368-1 | 主测 STC-110XGE |

- 证书覆盖的型号范围需人工打开 PDF 确认后再对外承诺（原件在 Drive `MUST KNOW/Certification/`，索引 `docs/drive/Certification/认证证书索引.md`；登记表 `docs/reference/证书登记表_2026-10-22.md/.csv`）。
- 认证口径（统一）：持有 CE / FCC / RoHS / REACH / UKCA；**无 UL**（2024-01 曾对 AirLive 说过「CE/UL compliant」——错，不再用）；TAA/GSA 不满足；日本 PSE/VCCI 可以客户名义办、费用客户自担（PSE 电源用 MEAN WELL GST120A48/240A48）；KC/BIS/EAC 由客户方办；UKCA 只对 GB 客户提。

来源：`docs/对外口径一致性_2026-10-24.md` #3/#5/#10/#22、`docs/reference/Saga商务条款速查.md` §4/§5/§9/§11、`docs/reference/证书登记表_2026-10-22.md`、`docs/Saga理念摘读_2026-10-23.md` A29。

---

## 7. 商务条款（销售口径）

### 7.1 交期与起订

| 项目 | 口径 |
|---|---|
| 生产启动 | 收到货款后开始（银行到账 1–2 个工作日） |
| 标准品 | ≤50 台 **4–7 个工作日**（Simon 现行对客户：「3–5 working days」+ 5 天老化；NYNEX 2026-09「3 weeks (15 working days) after order confirmed」）；定制/大单另议 |
| 大单 | 备料约 3 周（PCB、PoE 芯片、AC5 芯片）；**≥25% 订金起备料**；优先谈分批交付；250 台 ≈ 40 个自然日；1K 台 3–6 周 |
| 运输 | 快递 DHL/FedEx/UPS 4–7 天；海运/空运按单询价；下单到收货 ≈10–15 个自然日 |
| MOQ | **1 台**；定制（贴牌 / 面膜 / 固件）MOQ 按项目 |
| 样品 | **不免费**（"Saga Telecom do NOT do FREE SAMPLES"）；按 partner price 收费、样品款抵扣首个批量订单；5 个工作日出货；建议 ≥2 台。唯一例外：2026-04 对日本 UNEAX 说过「lending a piece is OK」（对方未接；对 UNEAX 不要改口） |

### 7.2 付款

| 项目 | 口径 |
|---|---|
| 币种 / 条款 | **USD EXW**（仓库规则）；Drive FAQ 写 DAP/DDP 为主 → 客户要到门价时按 DAP 单独核算运费；非欧盟客户常用 DAP / FOB 深圳 |
| 方式 | T/T（默认）、PayPal（+5%，样机 / 小额）、Xtransfer（Angora / James / NYNEX / Netaş）、EUR 账户（NYNEX 2026-09 三币报价 USD 6.71 / EUR 7.6 / RMB 2,015）、HK 账户收 TRY、RMB 经中国付款代理（俄罗斯 / 土耳其部分） |
| 比例 | 标准品批量 **50% 预付 + 50% 发货前**；定制/OEM 100% 预付；小额/样品 100% 预付；要求锁定排期需预付 25% 物料押金 |
| 手续费 | T/T 银行费 $25/单（买方承担）；PayPal 5% |
| 首笔外汇 | 中国银行对首笔境外来款要**买方股东信息**（一个股东即可，只首笔）——新客户首付前先说 |
| 有效期 | 报价 15 天；汇率剧烈波动重新定价；TRY 报价只给 3–7 天 |
| 国内 | 国内客户只接私账（支付宝 / 微信 / 银行卡），不接公账 |
| 待清路径 | RU / BY / KZ / UZ 收款路径未清前不报价（Backlog） |

### 7.3 保修与售后

| 项目 | 口径 |
|---|---|
| 保修期（对外） | **商用 STC 1 年 / 工业 STI 3 年 / DIN 电源 3 年 / 介质转换器与 PoE 配件 1 年 / CENTEC STH 1 年**，自交付日起，终身技术支持；SmartByte 官网 5 年是工厂政策，**不引用** |
| DOA | 发货后 3 个月内到货即坏 = DOA：往返运费与更换由工厂承担；保内客户寄回自付、工厂承担回寄与维修；保外全部客户承担 |
| RMA | **每 100 台同型号随货送 2 台备件**（或等值 2% 货款抵扣）；**不接受退货**，坏机以备件 / 下单补发处理；「硬件售后：换新，不修」 |
| 支持 | 邮件 + 远程（Web/CLI 日志）；固件升级免费；不含现场服务 |
| 除外 | 雷击、过压、进水、私自改装、SN 涂改、未授权维修 |

### 7.4 物流与清关实务（只记实际发生过的）

| 项目 | 做法 |
|---|---|
| 两条物流线 | ① **客户自己的广州货代**（Mbata 尼日利亚：Saga 只送到广州仓，发货信息单写「品名 / 数量 / 重量 / HS 8517622990 / 品牌 无 / 不带电不带磁」）；② **Saga 自己的深圳买单报关线**（James 加拿大、Angora 土耳其、Sugito 马来西亚、NYNEX 德国、Rishi 印度…）：填「出口货物确认函 / 货物情况说明表」 |
| HS 编码 | 交换机 **8517622990**；光模块 8517795000；光纤清洁笔 8517799000 |
| 品牌栏 | OEM/贴牌客户一律「**无品牌**」；自有品牌出货写「Saga Telecom · 境内自主品牌 · 生产厂家 Zhengzhou Saga Telecom Co., Ltd.」 |
| 报关费 | 大货运费基础上再加 ≈250 元（150 报关 + 100 保险） |
| 大单运费 | Angora 176 台 = 23 箱 471.9 kg，运费 22,426 RMB ≈ 127 RMB/台（≈$18），把毛利从 ~24% 压到 15.9% → 同规模报价时**运费单列、空运/海运分开报** |
| 印度清关 | FedEx 需收货人先在 kyc.fedex.com 上传 GSTIN + 身份/地址证明 + POA，否则卡海关 |
| 装箱单 | 工厂 PACKING LIST 开给 Zhengzhou Saga Telecom（Consignee），再由 Saga 转出口；客户只看到 Saga 的 CI/PL |
| 出口管制分类 | **EAR99 · NLR · CCATS 不适用 · HTS 8517622990 · 原产国 China**（对 Netaş 已填；大企业供应商入库问 ECCN 照此答） |
| 个人数据 | Netaş《Annex 1》已签：客户方个人数据只用于履约、不转第三方 → Netaş 联系人不进群发、不转给工厂 |
| 客户资料夹 | 成单客户一户一个 Google Drive 订单文件夹，把对方指定人加为编辑，请其上传测试报告 |

### 7.5 Simon 2026-09/10 现行口径（S 邮箱原话，可直接复用）

| 项目 | 英文原话 |
|---|---|
| 群发主推 | "Marvell AC5 based L2+ switch: 24 Port PoE af/at + 10G Fiber Uplinks + OEM and customizable Web GUI — Price: 180USD/PC" |
| 样品 | "Normally evaluation units are provided at a partner price, and the sample cost will be credited toward your first commercial order. For long-term partners we can discuss additional support based on the project and cooperation plan." |
| 分销 | "For now, we do not have a distributor in the UK. We are certainly open to discussing a distributorship after we get to know each other and see good cooperation." |
| 控制器 / API 问法 | 先反问 "REST API / SNMP-based / SSH-CLI automation / NETCONF / other controller platform?"——实际可承诺 SNMP + CLI/SSH + Web；**无云控制器、无 REST API**，下一封应直说 |
| 资料包 | 先发 `Saga Feature List_7.5.x_L2+.xlsx` + `Product Link_2026Q3.pdf`；深谈再发 `STC-424XGGPM-280W.docx` + `Marvell Based CLI/Web Manual.docx` + `SWITCH-MIBS-release.docx` |
| 涨价 | "in recent days, PCB and material costs are rising. This is one of the very competitive models."（统一说法：2026 年 PCB/RAM 成本 + 汇率，AC5 整线约 +$15；**不说「高价是为了筛选客户」**） |

来源：`docs/reference/Saga商务条款速查.md` §1–§3/§8/§10/§11、`docs/对外口径一致性_2026-10-24.md` #6–#9/#12、`docs/Saga理念摘读_2026-10-23.md` A24。

---

## 8. 定价规则（两套并存，都是底线不是策略）

### 8.1 公式（仓库规则，用户 2026-10-19 认可）

```
报价 USD（EXW）= SmartByte 未税人民币价 × (1 + 档位) ÷ USD/CNY 近期汇率
档位 ∈ { 20%, 25%, 30% }      汇率快照 1 USD = 6.69 CNY（2026-10-17；报价当天重核）
```

| 客户类型 | 档位 | 理由 |
|---|---|---|
| 分销商 / 电商 / 明显比价型 | **20%** | 走量、价格敏感、与台系品牌正面比价 |
| 集成商 / 项目型 / 方案商 | **25%** | 看方案可行性，让利空间保留在 25% 内 |
| OEM/ODM 深度定制、小批量技术型（CLI/MIB/私有 UI） | **30%** | 定制与技术支持成本高，Saga 核心差异化 |

### 8.2 芯片线 / 账户类型底线（《计划.docx》，Simon 原话）

- **Realtek ≥ 20 个点**（特殊客户或量大可压至 15）；**Marvell ≥ 25 个点**（可压至 20）；**CENTEC ≥ 35 个点**（必要时可加至 50 甚至更高）。
- 小单 **3 成左右**（按型号 / 数量 / 国家调整，**不低于 2.5 成**，含运费杂费）；大单私账 2–2.5 成；大单公账扣 10 个点税后**不低于 15 个点**。
- 封顶：「给我 100，我最多卖 130」（**30% 天花板**）；「Mbata 就是 20 个点，不能再低了」。
- 两套口径（按客户类型 20/25/30 vs 按芯片线 20/25/35）并存，写档案时注明选哪一档、为什么。

### 8.3 价格书写与有效期

`$xx USD EXW（快照 YYYY-MM-DD，15 天有效，报价前核价）`；首触邮件只报 **一个** P1 价格、只写 Saga 型号；同名 L2+/L3 注档位；对照表标「核对」的条目报价前与 SmartByte 确认规格。

### 8.4 价格异议处理

价格异议一律不让步（iotsistem、Aironix、case.uk 先例）；来信只有「target price / extremely expensive / cheaper alternative」而无任何技术问题 → 价格流客户 → 降级或 PASS，不在档案里设计「让价方案」。折扣「基于数量且在样品测试之后，只有客户对质量满意时谈价才有意义；分销商给最好价」。

### 8.5 常用价格锚（USD，CNY 6.69，20% 档为主）

Realtek 商用线以 §5.3.2 为准（例：STC-028GP = ZX900-AFG-82N，CNY 170 → $30.5 / 31.8 / 33.0；2023-11 首版曾报 $24.5；STC-2224GP = ZX900-AFG-2422S-300 CNY 490 → $87.9 / 91.6 / 95.2）· STC-424DGGM $82.5 · STC-424DGGPM-280W $134.5 · STC-424XGGM $127.4 · **STC-424XGGPM-280W $181.2（群发 $180）** · STC-448XGGM $263.7 · STC-448XGGPM $335.4 · STC-4168XGGCM $376.7（L3 列表 $413）· STI-280GE $46.6 · STI-288GPM $78.9 · STI-288DGGPM $139.9 · STI-21616DGGPM $240.4 · STI-21616XGGPM $297.8 · STI-488XGGPM $165 · STI-42424XGGPM-4BT $430.5 · STC-110XGE $65 · **STH-2C24XF-HSI $1,500（含 MA $1,250）· STH-2C6QX $1,200 · STH-2C24XE-HSI $1,700（2026-07 现货）· STH-8C48DX-HSI $4,800 · STH-32C-HSI $6,000**。

### 8.6 CENTEC（STH）报价锚（无成本价，只有对外锚）

| 平台 | 代表型号 | 锚 |
|---|---|---|
| XLite | STH-2C6QX-HSI/-SFI（6×40G + 2×100G） | $1,200（2026 Q2 价表） |
| XLite | STH-2C24XF-HSI（24×10G SFP+ + 2×100G） | HSI $1,250 含 MA（2026-06 对 SA-060）；群发 $1,500；SFI 无 DC 输入 |
| VastLakes STH10G | STH-2C24XE-HSI（24×10G Multi-Gig 铜 + 2×100G） | $1,700（2026-07 现货） |
| BigFlow / PeakNetX | STH-8C48DX-HSI（48×25G + 8×100G）/ STH-32C-HSI / STH-32QC（32×400G） | $4,800 / $6,000 / 400G 随 ITM 单 6 台 + 36 × 400G-SR4 @ $300 |
| STH1G（可堆叠 ≤8） | STH-2QX4DX48GP-HSI 等 5 款 | **仓内无任何价格（Q-54）** |
| Multi-Gig 铜口 PoE++（STH2.5G/5G/10G 20 余款） | STH-8DX24VP-HSI、STH-2C24XP-HSI、STH-2QX4DX8XP40DP-HSI… | **无价、现货未知（Q-56）**，不主动报 |

STOS 功能按许可分层：**EB 基础 / MS 高级 / MA 城域 / ST 堆叠**；EB 即有 RIPv1/v2、PBR、IP SLA、VRRP、ERPS、QinQ、sFlow、IPFIX；MLAG / VXLAN-EVPN / MPLS / BGP-OSPF 在高层许可。2026-01 群发写过 CENTEC「Full L3 features (VXLAN, EVPN, MPLS, Stacking etc.)」——Stacking 是否删除待核。

### 8.7 价表版本与已知矛盾（报价前必看）

- 仓内三代 Marvell 价表：① Drive `Extra Info/Price/2026 Price List_*.xls`（老抬头；STI-288DGGPM $125、STC-424XGGPM-280W $180、STC-4168XGGCM $375）= Angora 2024-11 成交价 = **Simon 2025–26 所有实际报价的量级**；② 仓库根目录三份《Price List_Marvell Based …》PDF（2026-06-22，新抬头，85/94 款 = ① × 1.10：$137.5 / $198 / $413）= `价格主表` 的「Saga列表价USD」，但 2026-06→10 四个月外发里**几乎没用过**；③ 仓库公式价（本表 USD 列）。
- 118 款对照：+20% 档中位数 = ② 列表价的 90%；**12 款 +20% 档 ≤ 列表价 70%**（STI-480XGGM $150.7 vs $253、STI-488XGGPM $165 vs $269.5、STC-4816XGCGPM $358.7 vs $611、STI-050GE $17 vs $34.1…）→ Q-59 待 Simon 定（跟着 SmartByte 降还是守列表价；默认按档位）；10 款 +20% 档 > 列表价（2.5G-SFP 工业 DGG 家族，如 STI-288DGGPM $139.9 vs $137.5——列表价按旧汇率 ≈7.1 算）。
- 非管理工业线成本表是 2024-01 的，算出的档位价（STI-054GP $31–34、STI-244GP $35–38）比 Simon 2026-04 实报（$33 / $45）还低——**不可靠，报前核**。
- 群发里的低价（Elsa $170 / STI-21616GP $165 / STI-488XGGBPM $215）是**旧汇率引流价**（U28），不是现行报价基准。
- HRUI 线：Drive 2026 Q3 美元表 61 款对洪瑞 2026-09-30 新进价的隐含加价 47 款可对照里 **39 款 < 20%、2 款为负**（Q-47）——Realtek 线报价必须按新进价重算。
- Simon 实际毛利（PI 包 `成本统计.xlsx`）：Angora 大单 ~24% → 运费后 15.9%；NYNEX 2024–2026 USD 19.6k 利润 RMB 7,082；Obmac 一单 265 台 USD 9,350 利润 RMB 23,118；利润点来源「13 + 5（返点）+ 20 个点价格 = 接近 40 个点」（出口退税 13% + 返点 5% + 加价 20%）。内部数字，**不外发**。

来源：`docs/rules/报价与型号规则.md`、`docs/reference/价格表_三档加价_USD.md`、`docs/reference/价格表_HRUI_三档加价_USD.md`、`docs/reference/CENTEC_产品表与报价锚_2026-10-24.md`、`docs/对外口径一致性_2026-10-24.md` #15/#19–#21、`docs/成单客户_毛利复盘_内部_2026-10-24.md`、`docs/Saga理念摘读_2026-10-23.md` A11。

---

## 9. 品牌口径与对外话术

### 9.1 固定四句（英文，逐字，不改写）

| 场景 | 原文 |
|---|---|
| 邮件签名 / 落款 | `<名字>` / https://sagatele.com/ / **An Engineering & Supply-Chain-First Telecom Partner** / **Built to Last, Continuous Supply, Evolving Together** |
| 一句话介绍 | **Tailored Managed Networking Solutions — A Scalable Path from Access to Core** |
| 三个关键词 | **Architectural Stability, Continuous Supply, and Lifecycle Continuity** |
| 使命 | Ensure that the journey from the first access switch to a mature, high-speed core remains scalable, coherent, stable, and low-friction |

仓库信稿签名统一：**「Saga Telecom - sagatele.com」**（首触样板落款 "Saga Telecom — An Engineering & Supply-Chain-First Telecom Partner · PoE / industrial switch OEM-ODM supplier (neutral packing available) · https://sagatele.com/"）。

### 9.2 口号史（知道就行，别用旧的）

3C「Connecting, Converting, Creating」→「Saga Telecom, OEM Factory / Tailored Managed Networking Solutions Provider / Built to Last, Continuous Supply, Evolving Together」→ 2026-07-29 中间句改为「An Engineering & Supply-Chain-First Telecom Partner」（「solutions 太泛化了，本身我们只有硬件」「叫 partner 比较亲切」）；「**OEM factory 不要加了，有点 low**」；第三句不变。2025–2026 签名「Saga Telecom/OEM Factory」127 封已发出——不翻案，新材料一律新口径。

### 9.3 理念语录（Roadmap / 官网原句，可直接引用）

- Continuity Over Novelty — "Upgrading from Access to Core is treated as a system extension rather than a replacement. By maintaining familiar workflows, we ensure that as bandwidth increases, operational complexity does not."
- Rational Technology Selection — "Silicon choice is an engineering decision, not a marketing one. Access Layer: Anchored on Marvell platforms selected for their industrial pedigree, field-proven stability, and mature ecosystem. Aggregation & Core Layer: Built on CENTEC solutions introduced only after comprehensive validation of ecosystem maturity, long-term supply alignment, and backbone-grade reliability."
- "A single, accountable technical contact across the entire network lifecycle."
- "These are not isolated hardware SKUs, but a coherent, scalable system that can evolve with network demands."
- "The transition from Access → Aggregation/Core is often the highest-risk point in a network's lifecycle."
- 官网："Built to engineer, not just to sell." / "We commit to Marvell and CENTEC architectures and go deep — not broad." / "Chip inventory, held on purpose." / "Strategic inventory isn't a cost center. It's the product." / "We're not a marketing-driven company. We put resources into engineering and inventory because that's where we actually create value for clients." / "Typical response within one business day. We don't use contact forms — direct email gets a faster, more useful reply."
- "We are backing our clients and following the market trend. Let's evolve together!!"
- 官网 At-a-Glance：Positioning = Engineering & Supply-Chain-First；Chipset Platforms = Marvell · CENTEC · Realtek；Customization = OEM / ODM / SKD / CKD；Supply Model = Strategic Inventory · Fast Lead Time；Certifications = CE · FCC · RoHS · REACH · UKCA；We Don't = Rail / transit certified (EN50155)、IP67、Consumer / home routers（UL 与 KC 官网写「available on request for qualified projects」——比仓库「无 UL」松，原样保留但信稿按仓库口径）。

### 9.4 口径规则 R1–R7 + 用词表

| # | 规则 |
|---|---|
| R1 | 自我定位只用 §9.1 四句；不自称 factory / manufacturer / we build；统一 "we supply / our Marvell-based portfolio / our manufacturing partner's facility"；About 文案「不要说是贸易商，换个说法」；对外不说 SOHO，说 "a specialized networking solutions provider" |
| R2 | **禁用** SmartByte 标语与工厂自述（"Genuine Source Factory • Robust R&D Support"、"SmartByte is specializing in R & D…"、Factory Tour 图文） |
| R3 | SmartByte 官网只借事实（型号、端口、PoE 预算、固件版本、认证、保修年限按 Saga 口径） |
| R4 | 网址只写 sagatele.com |
| R5 | 不主动承诺云管理（CENTEC DHCS 客户点名问时只答 "exists, self-hosted DHCS, not part of our standard offer"） |
| R6 | 芯片口径：接入层 Marvell、汇聚/核心 CENTEC；「CENTEC 不是 access 是 core」；不写 SKU 之外的性能承诺 |
| R7 | 客户语言英文、仓库笔记中文；英文引用照抄原句 |

- **用词白名单**：engineering-driven、supply-chain-first、architectural stability、lifecycle continuity、strategic inventory、low-friction deployment、predictable delivery。
- **禁用词 / banned phrases（信稿审计直接报错）**：cheap、best price、leading manufacturer、high quality with low price、professional service、list price、in stock（CENTEC 400G 群发写过，实际交期要核）、free samples、trading company、OEM Factory、NDAA、TAA、UL、GSA、general agent、we manufacture、Marvell ecosystem、SONiC、ONIE、"I researched your website"、产地、竞品名字。
- **信稿结构规则**：单一 P1、只问 **ONE question**、英文、付费样品、不写电话（WhatsApp 只给跳转）、UKCA 只对 GB、非欧盟 → DAP / FOB 深圳、模型必须在有效型号集合内。
- **两层答法**（客户问「有没有 X」）：第一层 Marvell AC5 线有/无；第二层 CENTEC 线有/无（查 `CENTEC_产品表与报价锚` + `客户功能需求台账` 看谁问过、当年怎么答）。例：多千兆铜口——"Marvell line: 2.5G/10G on the fiber cages only; our commercial Realtek line has 2.5G/10G copper; CENTEC Multi-Gig PoE++ models exist on request."

### 9.5 敏感问题的统一答法（口径表 #1–#22 精华）

| 主题 | 统一口径 |
|---|---|
| Saga ↔ SmartByte 关系 | "SmartByte is our Marvell-platform manufacturing partner; Saga owns the product definition, firmware branding (including the private MIB) and after-sales. The firmware you receive is built for Saga and does not carry third-party OEM identifiers." 合规部门追问以 Peter 2025-03-25 的说明为准；不主动翻 2024 年「completely self-developed」旧话 |
| 堆叠 | 接入 AC5 **不堆叠**；可堆叠线 = CENTEC STH-2QX4DX48GP-HSI（≤8 台 / 360 Gbps，ST 许可） |
| 源码 / SDK / API | "source code mode is NEVER an option"；SKD 可谈；API/SDK 不卖；转介第三方（Joey）做 CKD/源码不背书 |
| L3 / 协议边界 | L2+（AC5 7.5）静态路由 v4/v6 + PIM-SM；L3 型号另有 RIP/OSPF；不做 NAT / 云管 / TSN / MPLS（AC5）/ SD-WAN / BFD / IP SLA / Cisco 私有协议 |
| 代理 / 分销身份 | 可与客户签区域分销（客户当 Saga 的代理，"after we get to know each other"）；Saga 自己不自称任何上游总代；不接触客户的下游（SI/ISP）；无海外分公司 |
| 第三方转介 | 可转介不背书；轨交 / 源码 / 云管三类一律转出（轨交 M12 → Inmax） |
| 对 MikroTik 用户 | 不比功能（RouterOS 脚本 / REST API / 云 NMS 我们没有），只说三件真事：OEM 贴牌 + 定制 Web GUI/默认配置、同为 Marvell Prestera、可作部分项目的替代；$130 级别 |
| 涨价 | PCB/RAM + 汇率，AC5 整线约 +$15 |
| 光模块 | 不单卖；随整机按 §5.1 价位 |
| Realtek 线 | 只在客户自己说 Realtek / 低价 / 功能简单时给；「management functions are even worse than Marvell」（Alan 原话） |
| 日本 / 美国政府 / 韩国 | PSE/VCCI 客户名义办费用自担；TAA/GSA 不满足；KC 客户方办 |
| 国内冲突 | 项目可能与 SmartByte 国内客户重叠（大型校园 / 运营商 / 无软件裸机）→ 标「待 Simon 判断冲突」，不推进（Q-49） |

### 9.6 FAQ 英文一句话（可直接贴）

- Lead time: "Standard models ship in 4–7 working days after payment, plus 4–7 days by express."
- Samples: "Samples are charged at unit price and fully deductible from your first bulk order."
- Warranty: "1-year warranty on commercial models (STC) and 3-year on industrial models (STI) and DIN power supplies, from the delivery date, with lifetime technical support."
- Payment: "T/T 50% deposit, balance before shipment; PayPal accepted with 5% fee."
- Spares: "2 free spare units per 100 pcs of the same model instead of RMA returns."
- OEM: "Logo, label, carton and Web-UI logo customization are free of charge; neutral packing available."
- Distributorship: "We are certainly open to discussing a distributorship after we get to know each other and see good cooperation."
- Export classification: "EAR99, NLR; HTS 8517.62.2990; country of origin China."

来源：`docs/reference/Saga品牌口径与宣传语录.md`、`docs/对外口径一致性_2026-10-24.md`、`docs/reference/Saga商务条款速查.md` §6–§9、`docs/Saga理念摘读_2026-10-23.md` A10/A25、`scripts/saga_clients/audit_ab.py`（banned phrases）。


---

## 10. 市场与区域策略

### 10.1 区域优先级（Simon 的话为准，AI 建议为辅）

| 层级 | 国家 | Simon 原话 / 依据 | 运行方式（收款 / 物流 / 合规是否已通） |
|---|---|---|---|
| **四主区** | **土耳其、美国、英国、德国** | 「本身我是有土耳其、英国、德国客户的，成单的，质量都不错，这 3 个国家肯定是重点」；「美国：重要做，市场足够大，业务国际化，客户质量也不错，我手上有一些不错的，可以突破一下」（**没有听 AI 的「放弃美国」**）；「土耳其 = 现金流底盘，美国 = 爆发潜力，英国 = 高质量利润池，德国 = 技术 + 口碑市场」 | TR：TRY 收款（HK 账户）+ Xtransfer + 小批量多批次 + WhatsApp + DAP 伊斯坦布尔；US/CA：PayPal/T/T + DHL/UPS DAP（无 UL、TAA 不满足 → 只推私营企业 / WISP / 中小 DC / MSP / 行业 SI，不碰政府军队 Tier-1）；UK/DE：T/T、EUR 账户、Xtransfer——**全部已通** |
| 次重点 | **波兰** | 「地理位置 OK，对中国产品也不太排斥」「波兰可稍微重点」 | 已有群发基础（585 封），无成单 |
| 范围内 | 欧洲其他（意大利「我手上客户多」但「不是特别好的突破方向」、捷克、北欧、西班牙、法国、荷比、奥地利、瑞士等）+ 加拿大 | T05/T06「北美 + 欧洲 + 土耳其」 | 大多已通或同 EU |
| 次级 | **俄罗斯、印度、韩国** | 「欧洲 美国这 2 个是绝对大头，然后一些俄罗斯 印度 韩国客户」；俄罗斯「我手上有成单客户，整个客户 list 也长，我也去过俄罗斯，对中国产品相对友好」 | RU：货代人民币、不走公账（**RU/BY/KZ/UZ 收款路径未清前不报价**）；IN：FedEx KYC（GSTIN/POA）、倒推式价格客户、通路「未通」；KR：需 KC（无）→ 守界 |
| 已有成单但不主攻 | 尼日利亚、泰国、马来西亚、阿联酋、新加坡、赞比亚、格鲁吉亚 | 成单 20 家里的「其他」 | NG：客户货代 + WhatsApp only；TH/MY：货代 RMB；AE：T/T |
| 守界 / 不做 | **乌克兰、伊朗、叙利亚**（守界，留 C 不发）；军工 / 公共采购 / 生命安全领域；轨交主营；巴西（「目前来看是最麻烦的一个国家」）；日本（PSE 自担，部分通）；韩国 KC；小国（SI/HR/RS/RO/BG/EE/LV/LT/LU/IS）不主动挖；大陆公司一律不入库 | INH-11、《计划》、U117 | — |

- 「国家 = 运行方式，不是市场规模」：一个国家能不能做取决于收款、物流、合规三件事是否已有现成通路。已通：TR、US、CA、UK、DE、UAE、NG、RU（货代）；部分：JP（PSE）、IL；未通：IN、KR、BR、ZA。
- 「在对的 4 个国家，把对的 20 个客户，服务成离不开你的 8 个」；每个核心市场「1 个标杆客户 + 2–3 个稳定客户 + 5–8 个潜在客户」。
- DC 交换机（CENTEC 400G 等）当**项目入口**，只在美 / 德 / 英推，只卖给有现成 DC / 项目经验或已有部署计划的；CENTEC 市场判断：第一梯队土耳其（Angora / Netaş 找降 BOM 做自有品牌），第二梯队德 / 英（Open Networking Whitebox，企业网 / 教育 / 非关键 DC），第三梯队美国（私营 / WISP）；「俄罗斯是 Centec 的天堂」；不适合 NDAA / TAA 项目。
- 土耳其细节：Angora 合作两年多（近来以项目为主）；Netaş 把 Saga 列入供应商 list、常收 compliance 邮件；里拉贬值 → HK 账户直收 TRY；Q3（6–8 月）停摆，1–2 月与 9–10 月是窗口；Yerli Malı 本土制造 15% 加分 → SKD/CKD 玩法；TAREKS 抽检、CE DoC / 土耳其语标签 / OEM 需客户商标授权书；`TR重点公司.xlsx` 8 家：Kron（主推 CENTEC 高速）、Karel（商业 PoE 国产化替代）、Netaş（在谈）、Turkcell（与 Netaş 关系紧密，不主动推）、Vodafone TR、KoçSistem、Aselsan / Havelsan（军工 — 守界）。
- 英国跳板想法：Angora 在英国的公司 **Connexite** 可作对接 / 投标 / 中转平台；ITM 想做英国基地（可签分销）。
- 展会清单（Simon 存档）：COMPUTEX Taipei、Secon Korea、SVIAZ / MIPS Russia、Exposec Brazil、Intersec Saudi、Essen Germany；德国 SPS / Hannover Messe。
- PLANET 渠道（本仓库原始任务）：PLANET Technology（台湾）的欧美分销商 / 集成商 / 安防工业经销 / 贴牌品牌商 = 「在和台湾品牌合作」的客户池（已接受台系价位、习惯亚洲供货）；**台厂本身不是客户**（INH-03）；该矿脉 2026-10-20 起**暂停不是搁置**（T22 / T29-U8 / U28），129 户已入库并按同一尺度复核。

### 10.2 发信窗口与来询季节（全库 S/A 邮箱统计，对方本地时间）

| 国家 | 群发封数 / 平均打开率 | 最好的时段 | 最差的时段 | 来询高峰月 |
|---|---|---|---|---|
| 美国 | 2,491 / 5.4% | 周三 08–10（13.6%）、周二 08–10 | 周五 14–16、周四 12–14 | 8 月、11 月、1 月 |
| 英国 | 1,094 / 5.0% | 周四 12–14（11.9%）、周二 14–16 | 周四 14–16、周五 12–14 | 1 月、5–6 月 |
| 德国 | 922 / 4.4% | 周四 12–14、周二 08–10 | 周五（12–14 为 0%） | 9–12 月 |
| 土耳其 | 901 / 4.0% | 周四 10–12、周一 10–12 | 周二 14–16、周五 08–10 | 5 月、1–2 月 |
| 加拿大 | 681 / 5.7% | 周五 12–14、周二 12–14 | 周四 10–12 | — |
| 波兰 | 585 / 5.5% | 周四 12–14 | — | — |
| 俄罗斯 | 577 / 6.2% | — | — | 12 月、5 月 |
| 韩国 | 1,206 / 5.1% | 周一 / 周二 10–12 | 周三 / 周四 | — |

- 打开率最高的主题：「24 port poe switch」20.4%、「10g fiber media converter」17.9%、「24 port fiber switch」17.2%；最低：「10g l3 managed switch」1.3%、「managed poe switches」1.2%。德国对「oem core switching solution」0%。
- 假日避让表：`docs/各国假日避让_2026-11_2027-03.md`。

来源：`docs/Saga理念摘读_2026-10-23.md` A5/A6/A9/A12/A25、`docs/Saga内在逻辑与概念_2026-10-24.md` C7、`docs/各国发信窗口与来询季节_2026-10-27.md`、`docs/成单客户_PI复盘_2026-10.md` 看点 6、`docs/reference/Saga公司画像与边界.md` §6。

---

## 11. 目标客户画像、判读框架与分级标准

### 11.1 目标客户排序（Simon 原话顺序）

1. **品牌商 / 方案商（有 OEM/ODM 需求）→ 最优先**；偏技术的客户谈深度定制（功能、管理 UI）——核心差异化。「有自有品牌的交换机产品线」是最强正向信号。
2. **明显有从中国进口经验或合作供应商者**（Utepo / ONV / UNIPOE / HRUI / Scodeno…）；**在和台湾品牌合作的也可以（ORing / PLANET / Edgecore）**——长期潜力客户，慢慢跟。
3. **分销商 / 电商**（卖现成品牌、要现货标品）→ 可跟（可 OEM、有芯片库存、交期快）；纯转售知名品牌的分销商（Sava 类）绑定最弱。
4. **集成商 / 项目商**（CCTV / 工业 / 园区）→ 可跟，**最好是小项目**；大集团很难拿下。
5. 同行（明确在用大陆 / 台湾品牌的）→ 通过长期跟进有希望。
- 偏好 **项目型**（弱化贸易商身份）与 **技术型**（CLI / MIB / 深度功能是主场）；「深度合作基本上还是要过工程师这一关」；客户判据一句话：「他是不是在构建一个系统，而不是买一台设备？」
- 反向信号：只问 price list / target price / MOQ 的价格流；主营轨交；巨头分销（Ingram、TD SYNNEX、Arrow、Wesco/Anixter、Bechtle、Computacenter、Also…直接 C）；巨头运营商（hard 但**不是**永久 pass）；要求 API/SDK/云 NMS 的（Latmedia 类 → 转介，不是绑定对象）。

### 11.2 每户判读框架 J1–J7（加厚与 A/B 调查直接用，每个答案必须带证据）

| # | 维度 | 取值 | 证据长什么样 |
|---|---|---|---|
| J1 | 客户类型 | OEM 品牌商 / 有进口经验者 / 分销商 / 集成商 / 其他 | 官网自有品牌交换机线；PI/报关/货代经验、问 HS code/Incoterm；多品牌目录；项目案例页 |
| J2 | 技术流 or 价格流 | 技术 / 价格 / 混合 / 未知 | 问 VLAN·ERPS·MIB·CLI·固件·温度·PoE 预算（技术）；只问 price list / target price / MOQ（价格） |
| J3 | 走到第几道筛子 | 0 未触达 / 1 回过群发 / 2 读过 Drive / 3 走过 Template | 引用型号或价表数字 = 2；PI 编号、付款凭证、保修证书、NDA/ECCN 表 = 3 |
| J4 | 绑定等级 | 无 / 轻度（样品在手）/ 中度（批量 + 客户文档出现 Saga 规格）/ 较深（客户系统依赖 Saga 固件·OID·CLI）/ 深（自研集成 + 多年复购） | 监控快照里的产品页、GitHub、博客、招标文件、LibreNMS 提交 |
| J5 | 停点 + 复活条件 | 停点 ∈ {功能上限, 温度/认证, 价格, Saga 边界, 国内冲突, 对方不需要, 无回音}；复活条件写成**外部事件** | 停点取客户最后一封实质邮件原话；复活例：「固件 7.5 补 PIM-SM」「客户发布新一代产品」「招标公告」 |
| J6 | 国家通路 | 已通 / 部分 / 未通 | 见 §10.1 |
| J7 | 节奏 | 最后接触日期 / 由哪个名字 / 累计触达次数 / 下一次触发条件 | 三邮箱合并后的时间线 |

每户输出一行（可被脚本读取）：`绑定等级：轻度 ｜ 类型：集成商(技术流) ｜ 筛子：3 ｜ 停点：功能上限—L3 组播 ｜ 复活：固件补 PIM-SM/DM 或 CENTEC 工业温度机型 ｜ 通路：TR 已通 ｜ 节奏：最后 2026-07-17 Alan，第 9 次 ｜ 证据：A 邮箱 2026-02-27 / 2026-03-02`。绑定深度 Simon 的标签（轻度 / 较深 / 深）是基线，证据充分可升但要注明 Simon 原级。

### 11.3 长期客户群 A/B 标准 v5（2026-10-29，Q-76 收口，三库同尺）

- **A（精华跟）满足任一**：A1 复购 ≥2 或绑定 ≥中度 ｜ A2 成单 / 样品 / PI + 真人往来 ｜ A3 真人往来 + 对位 + 四主区/波兰 + （坐实 或 自牌）｜ A4 Simon 点名 ｜ A5 自牌 + 对位 + 真人往来 ｜ A6 真回 ≥3 + 对位。
- **B 底线** = 对位 + 活着 + 有路径。留 B 规则：行业内 + 对位 + （进口同类 / established 分销·集成·品牌商 / 成单·样品·回信·需求）；微型 + 有进口证据 = 留 B 预付；未坐实 + 有路径 = 留 B 待坐实。
- **打回 C 储备（可逆）**：个人 Gmail / 无主体；微型零售无进口证据；dormant；未坐实 + 无路径；非对位 + 区域外；红旗 / 制裁；明确没需求。dead 域 + 备用路径 = 留 B 换路径。
- **梯子**：回信 / 询价 / 样品 / 成单 → 升；两轮无动静 → 降；弹回 / 停发 → pass；UA/IR/SY → C；gg 8 家永不 A。
- **永久 pass（Gate 0，必须刚性）**：仅三种——无邮箱且无 WA；弹回且无备用地址；明确婉拒 / 要求停发。**不是**永久 pass：乌克兰、巨头运营商、品类不对位（光端机 / DWDM / 光模块——Simon 本职可用）、「研究后定 C」。「一旦入选 永不考虑」——所以不刚性的一律留 C 储备。
- **C ≠ 垃圾**：C = 储备，不发信、两月巡检、来信即回 B。
- **Q-33**：经销体系 / 洪瑞现供的 reseller 客户「不碰，标记」（`q33_hold` 只巡检），SA-040 例外可跟。
- **Simon 的分层方向（U128，绑定）**：A/B 都是长期跟群；等级随反馈 / 挖掘 / 公司进展 / 产品线演变；C 捞出直接 B；External + Planet 同尺；核心规模不设硬指标；「再去过一遍客户 = 调研 + 加厚」，没深挖过的必须挖，不清楚的进 C 储备。
- **§6 默认分层（Q-77，待 Simon，默认执行）**：A 精华跟 — 季度个人信 + 两月巡检 + 回信 48 h；B1（≈300–450）— 群发 + 一年两次人工点名；B2（≈1,500–1,700）— 只群发 6–8 周一封，弹回即 pass；C 储备 — 不发、两月巡检、来信即回 B。B2 = 桌面卡 + 快照 + 邮箱域活；A + B1 需登记 + 具名 KP。
- 旧规则（继承，仍是底色）：A = 真实可追溯需求 + 可直达的人；B = 有邮箱可群发；C = 无邮箱 / 体量过大 / 区域外 / 业务不对口；`人工定级` 列优先于机器评级；集成商 / 顾问优先于分销商（Mikrotik 仓实测 A 率 34.5% vs 3.7%）。

### 11.4 公司底数登记（坐实）

- 「坐实」= 在官方 / 半官方登记源核到法人主体（Companies House / northdata / pappers / KRS / proff / allabolag / MD SDAT / BBB / D&B / Crunchbase…），写入 `data/saga_clients/registry/<key>_2026-10-27.json`（1,487 码）；规则「**1 查未得即停**」；38 家 A 部分坐实（付费墙）只做 A 季度复核；新入库即查。规程：`docs/公司底数_作业规程.md`。

来源：`docs/reference/Saga公司画像与边界.md` §4/§5、`docs/Saga内在逻辑与概念_2026-10-24.md` §4、`docs/AB判定_新标准_讨论稿_2026-10-29.md`、`docs/长期客户群_方案与复核_2026-10-29.md`、`docs/rules/客户分级与去重规则.md`、`docs/requirements/用户要求总账.md` INH-05/07/11。

---

## 12. 客户资产现状（2026-10-29）

### 12.1 三个客户库

| 库 | 来源 | 编号 | 规模 | 渲染 / 真源 |
|---|---|---|---|---|
| **Saga Clients** | S/A/E 三邮箱全部往来 + PI 包 + Drive 客户名单 + 补录 | SA-/SB-/SC- + 三位连号（2026-10-25 重编，映射 `data/saga_clients/编号映射_2026-10-25.csv`） | **A 169 / B 1,225 / C 3,253**（entities 4,647） | `data/saga_clients/entities.json` + `research/<code>.json`（1,698 份）→ `build.py` → `render.py` → `Saga Clients/A|B|C/*.md` |
| **External Clients** | Simon 三个旧仓库 `CCTV-PoE` / `Edgecore` / `mikrotik-info`（4,351 户导入；大陆公司删除；CCTV agent 永不再跑） | XA-/XB-/XC- + 来源字母 C/E/M | 渲染 **B 647 / C 3,704**（长期群 B 601 + 46 副档） | `data/external_clients/{cctv,edgecore,mikrotik}.json` + `overrides.json` + `research/<code>.json`（1,096 卡）→ `scripts/external_clients/render.py` → `External Clients/<repo>/A|B|C/` |
| **Planet** | 本仓库 PLANET 渠道挖掘 W01–W22（2026-10-19/20） | PA-/PB-/PC- | **129**（A 2 / B 109 / C 18） | `data/客户名单_Planet渠道_2026-10.csv`（26 列，唯一真源）+ `batch/*.json` → `scripts/render.py` → `profile/A|B|C/` |

### 12.2 长期客户群（三库并池，`docs/长期客户群_名册_2026-10-29.md`）

- **唯一 2,045 = A 170 / B 1,875**（Saga A 169 / B 1,225；External B 601；Planet A 1 / B 49）+ **107 副档随主档**（同一公司跨库重复：External 46、Planet 61；如 PA-003 = SA-034）。
- 区域分布（A / B）：四主区 + 波兰 77 / 665；欧洲其他 8 / 498；俄语区 13 / 96；印度/南亚 21 / 99；东亚/东南亚/大洋洲 24 / 258；中东/非洲 21 / 157；拉美 4 / 49；其他 2 / 56。
- 复核日志 `data/长期客户群_复核记录.csv` 1,219 条（留 B 1,039 / 打回 C 180）。
- C 储备：Saga 3,253 / External 3,704 / Planet 18；**永久 pass 1,431**（刚性三条）。
- **A 170 的完备度**：136 户五项全齐（桌面卡 / 官网快照 / 快照后加厚 / 公司登记 / 具名 KP）；其余只缺官网快照 33（GitHub Actions 夜跑补）、PB-046 快照+加厚、SB-110 / SB-1103 邮箱域异常（留 B 备用路径）、PA-003 副档；38 A 部分坐实（付费墙，按规则停）。
- 缺口表 `docs/长期客户群_深挖缺口_2026-10-29.md`：External 快照+加厚 647 / 登记 627 / KP 322 / 邮箱 17；Planet 快照 111 / 登记 110 / KP 60 / 邮箱 2；Saga 齐 952 / 快照 370 / 快照后加厚 185 / KP 116 / 邮箱 11 / 域异常 5。官网快照 ≈1,100 由 Actions `customer-watch` 两夜补齐，`lt_snapshot_thicken.py` 自动加厚。
- 「跟进总台」`docs/跟进总台.md`；P 池总名册 `docs/P池_总名册.md`；周发送包（W44 待发）。

### 12.3 Gmail 资产

| 箱 | 入库 | 规模 / 要点 |
|---|---|---|
| S（Simon） | `data/gmail_s/messages/<year>/<yyyy-mm>.jsonl` | 2023-11 → 2026-10；群发活动与公开价格点 `docs/reference/S邮箱_群发活动与公开价格点_2026-10-22.md`、报价史 `data/S邮箱_报价史_2026-10-22.csv` |
| A（Alan） | `data/gmail_a/`（含附件文本 `attachments/text/`） | 14,500 发 → 真实来信 208 → 实质线程 91；总览 `docs/gmail/A邮箱_总览_2026-10-24.md`、真实往来 `A邮箱_真实往来线程_2026-10-24.md` |
| E（Elsa） | `data/gmail_e/`；触达表 `data/gmail_已触达清单.csv`（271 行） | 3,675 封 / 3,288 会话；`Replied` 51 会话（南亚/东南亚/拉美为主，欧美极少）；退订：westwardsales.com（US）永久不触达；starcom.net.pk 要求公司域名发件 |

- 原则：Gmail 是次要源；客户事实进仓只写「日期 + 主题 + 对方域名 + 原话摘录」；首触前先查触达表；659 个「群发过但从未回信」域名不建档（Q-44）。

来源：`docs/长期客户群_名册_2026-10-29.md`、`docs/长期客户群_深挖缺口_2026-10-29.md`、`docs/gmail/00-Gmail盘点与使用方案.md`、`External Clients/00-总索引.md`、`README.md`。

---

## 13. 成单客户 20 家（PI 包，2023-07 → 2026-10）

单据销售额合计 **USD 109,988 + RMB 158,432**（RMB = 走货代的 3 家）；Simon 成本统计利润合计 RMB 127,097。Simon 自己的标签（文件夹名）= 最硬的信号：**活跃 6 / 可发展 7 / gg（已凉，= 难复购）8**；收款渠道 Xtransfer 4、货代走账 3、PayPal 2；轻度绑定 5。单号前缀 = 经手账号（STSC = Simon / STAG = Alan / STEC = Elsa）。

| # | 客户（国家） | 编号 | Simon 标签 | 单数 / 期间 | 销售额 | 型号 / 要点 |
|---|---|---|---|---|---|---|
| 1 | **Angora Networks**（TR） | SA-077 | 活跃 · Xtransfer · 轻度绑定 | 10 / 2024-05 → 2025-06 | USD 61,669（一单 178 台 USD 47,174） | STC-28DGGPM / 416DGGPM / 424XGGPM / 448XGGPM、自有品牌 **Verge / ANW-2248-PX**；大单运费 ≈$18/台压毛利到 15.9%；2024-11 Simon 把 Turkey Client List 64 家交给 Angora（Q-51）；PVC 面膜 / 彩盒 $2.5 / MAC 段等 OEM 先例多出自此户；英国公司 Connexite |
| 2 | **Biz-Ethics Ltd / BEL Networks**（NG，Mbata） | SA-079 | 活跃 · 货代走账 · 轻度绑定 | 12 / 2024-09 → 2026-08 | RMB 101,353 | BNSC- 贴牌系列（STC-28GPM / 4168XGGCM / 424DGDPM…）；SmartByte + HRUI + Hohunet 三家都采购过；**只用 WhatsApp**；客户自己的广州货代（末端 VALENTINE, Lagos）；「Mbata 就是 20 个点，不能再低了」；belnetworks.com 域已被第三方停放（2024-08 重注册）→ 邮件不可达 |
| 3 | **NYNEX satellite OHG / fiberONE**（DE，Frederik） | SA-008 | 活跃 · Xtransfer · 可发展 | 5 / 2024-11 → 2026-10 | USD 19,634 | STC-4168XGGCM（2026-10-06 复购 20 台）、STC-424XGGM；**绑定最深**：向 LibreNMS 提交 OID、坚持 SmartByte OID、2025-03 合规部门追问 Saga↔SmartByte 关系、要求自有 PEN；GitHub `freddy36` 监控（宪法第九条）；PeeringDB AS200519；三币报价 USD 6.71 / EUR 7.6 / RMB 2,015；维护计划 `docs/成单客户_NYNEX_维护计划_2026-10-22.md`；T29-U15 安排：Saga 推 SmartByte、Peter 处理技术 |
| 4 | **PBA Forever Technology**（TH，Peeranun） | SA-080 | 活跃 · 货代走账 · 轻度绑定 | 6 / 2024-10 → 2026-07 | RMB 37,489 | 工业 16/24 口 PoE 为主（STC-05XGWE / 08XGWE / 108XGDGP / 114XGDGP…）；泰文 CCTV 安装商 pbacctv.com；LINE 沟通 |
| 5 | **James Clendenan Systems**（CA，James） | SA-078 | 活跃 · Xtransfer · 轻度绑定 | 4 / 2024-06 → 2026-09 | USD 6,740 | 贴牌 **SW-3200-16GP** = STI-21616DGGPM/XGGPM、STI-488XGGPM、STC-424XGGM；「DI/DO/RS485 + 10G + PoE BT = James 出货的 AC5 方案」；**WeChat / LinkedIn 只对 James 用过**；新品牌 Control Ready（controlready.ca）；2026-08 问 2.5G/mgig PoE + 双电源 + 机架（未答，SB-263 线） |
| 6 | **NETAŞ Telekomünikasyon A.Ş.**（TR，Burak） | SA-086 | 活跃 · Xtransfer · 轻度绑定 | 1 / 2025-12 | USD 545 | STI-488DGGPM-2BT 首单 + 保修证书「Three (3) years」；买样后不符项目需求但把 Saga 列入供应商 list；法务要 NDA / ECCN（EAR99 已填）、KVKK 个人数据附加协议已签；上市公司（2026-08 H1 订单 +96%）；接受 CENTEC；温度要求 -40~+71 ℃ |
| 7 | **Vi-Link, Inc.**（US，Thu） | SA-006 | 可发展 | 4 / 2024-04 → 2026-09 | USD 1,147 | Fiber MC、STC-110FE / 110XGE / 14DUR / 4168XGGCM；新网店 vilink.us（80+ SKU 自有 IE/ME/EN 工业交换机线）；PayPal 税务敏感（「please kindly try bank… its about tax」） |
| 8 | **GOGREENIT**（UK，Chris Clemson） | SA-007 | 可发展 · PayPal | 1 / 2025-08 | USD 588 | STI-42424XGGPM-4BT；写博客、报告 SSH 终端 bug（进入客户运维循环）；自建 Mastodon / PeerTube（每日活跃） |
| 9 | **BitBook LLC / БитБук**（RU，Andrey Татарников） | SA-016 | 可发展 · 货代走账 | 2 / 2023-11 → 2025-07 | USD 6,038 | STC-128GFP / 28GPM / 424GM / 4424GCPM、STI-288GPM；网店 bitbuk.ru 自有品牌 **PRIORAT** PoE 交换机，2026-07-06 博文公开承接 OEM/ODM 贴牌 |
| 10 | **Sundar Techno Solutions**（IN，Manoj） | SA-032 | 可发展 | 4 / 2025-01 → 2026-02 | USD 875 | STI-0160GE；IBASE / Volktek / Panasonic 代理 |
| 11 | **ASTEL DIGICOM Electronics LLC**（AE，Sanjay） | SA-001 | 可发展 | 1 / 2025-11 | USD 166 | HDR-15-24、STI-110GE / 140GE；2025-11 外发含 s. 邮箱 PayPal 与 152 手机号（已发生）→ 后续只用 a. 邮箱 + WhatsApp 跳转 |
| 12 | **WIZARDSINC SDN BHD**（MY，Raja Kumaran） | SA-090 | 可发展 | 3 / 2026-08 | RMB 19,590 | NDR-240-48、STI-21616GP / 21616GPM / 288GP / 288GPM、STI-G2-MD / G20-SD 光模块 |
| 13 | DELTA CONSULTING LLC（GE，George） | SB-375 | gg | 1 / 2023-07 | USD 100 | STC-028GFP / 128GFP；兼营 ISP（AS209786） |
| 14 | Fastball（IN，Rishi） | SB-1113 | gg | 1 / 2023-10 | USD 260 | IndiaMART 挂 **FBC-204GP = STC-204GP** 贴牌 |
| 15 | Obmac Systems（ZM，Pythias） | SB-1120 | gg | 1 / 2024-01 | USD 9,350（265 台） | STC-4248XGGCM、STI-244GP、光模块；利润 RMB 23,118；重心转光伏 EPC |
| 16 | UNITED CONTROL ENGINEERS INDIA（IN，Rajesh） | SB-006 | gg | 1 / 2024-04 | USD 120 | FedEx KYC 先例（GSTIN 09AACCU4195M1ZP）；Phoenix Contact 等授权分销 |
| 17 | «Rio-Import» LLC（RU，Igor） | SB-003 | gg | 1 / 2024-05 | USD 1,140 | STI-050GE / 080GE；推 Phoenix Contact 工业 PoE |
| 18 | XSPec Hospitech / XSPec Technology（MY，Sugito） | SB-002 | gg | 2 / 2024-06 → 07 | USD 1,146 | 商用交换机；2026 新目录站 54 品牌；MINDTCE 2026-11 参展 |
| 19 | Resonant Networks Pte Ltd（SG，Au） | SB-001 | gg | 1 / 2024-09 | USD 185 | 2026-08 新开 GitHub 组织 Resonant-Networks（DC 自动化「source of truth」仓库）→ 监控中；2024-10 Alan 曾说「we are a factory manufacturer… do trading/reselling」 |
| 20 | 52 Networks Inc.（US，John） | SB-020 | gg · PayPal | 1 / 2025-07 | USD 285 | NDR-240-48、STI-288GP；GSA MAS 要 TAA → 样机收后沉默；2025 仍出政府单 |

- 定级规则：Simon 标活跃 / 可发展 → A；gg → B（成交过·慢慢跟进），`人工定级.csv` 仍优先；档案有「成交记录（PI 包 · 自动汇总）」节。
- 活跃平台与监控：每户的官网 / RSS / GitHub / LinkedIn / 行业名录都已登记到 `scripts/web_watch/targets.json`，GitHub Actions `customer-watch` 每夜 02:23Z 巡检；详情 `docs/成单客户_活跃平台与监控_2026-10-23.md`。
- 内部毛利复盘：`docs/成单客户_毛利复盘_内部_2026-10-24.md`（**不外发**）。
- 没进成单表但重要的往来户：Larch（SB-359，8,000 台询盘，$250 目标价 + 无软件 + 国内冲突 → 主动停）、ITM Components（SB-767，英国，400G 6 台 + 36 模块报价，想做英国基地）、Versitron（SB-826，堆叠问答史）、Milliseconds Evolution（SB-1115，UK MikroTik 顾问，2026-10 两台样机 PI STSC-20261017-001）、Fikes Media（SB-1114，OEM 菜单 / API 问答）、UNEAX（SB-164，日本 PSE/VCCI、借样例外）、Kron / Karel / Turkcell（TR 重点）、Supermicro（SC-262，板级询盘，巨头规则冲突 Q-55）。

来源：`docs/成单客户_PI复盘_2026-10.md`、`docs/成单客户_活跃平台与监控_2026-10-23.md`、`docs/成单客户_毛利复盘_内部_2026-10-24.md`、`docs/reference/Saga商务条款速查.md` §10/§11、`docs/对外口径一致性_2026-10-24.md`。

---

## 14. 跟进节奏与渠道

- **群发 = 引流到资料，不是销售**：任务是让 1% 的人点开 Drive 链接并自我筛选；主题按月换产品（Industrial PoE Switch / Mini Industrial PoE Switch / 8 Port Industrial PoE Switch / 16 Port Ethernet Switch / 90W PoE Managed Switch / Marvell Alleycat5 Solution / 24 Port Fiber Switch / 48 Port PoE Managed Switch / Managed Optical Bypass Switch / 10G Enterprise SFP Switch / Booster PoE Switch / OEM Core Switching Solution…），附件永远是 Product Link PDF 不是价格；「回复过群发」本身几乎不含信息，看回复内容类型。**减少群发是战略取舍**（U28），不是能力问题。
- **慢是武器**：对停滞客户不催、不让价（Netaş 停滞 4 个月后再发一次特性表；ITM 400G 报价后不催）；每户要有**节奏记录**（最后触达 / 次数 / 下一次触发条件），复活条件写成外部事件。
- **渠道规则**：邮件英文为主；WhatsApp 跳转（不显示号码；WhatsApp 客户档案不写代号）；WeChat / LinkedIn 只对 James；LinkedIn 公司页「必须」（Simon 2026-08），YouTube / Facebook 暂时 pass，X 一般；平台店铺 FindLight 10 / EC21 15 / Made-in-China 20 / Global Sources 100（免费上限已用满，Global Sources 已不投广告）；不用联系表单（"direct email gets a faster, more useful reply"）。
- **监控（每 2 个月一轮，覆盖面要广）**：官网 / RSS / GitHub / LinkedIn / Facebook / 展会 / 政府采购 / 域名 RDAP；自动部分 = `scripts/web_watch/`（`targets.json` 2,987 源 / 1,405 客户，`checklist.py`），GitHub 部分 = `scripts/github_watch/`；人工看 LinkedIn。
- **周发送包与跟进总台**：`docs/跟进总台.md` 汇总每周发送包（W44 待发）；`board.py` 会重排发送包——不要重复跑。
- **Elsa 首触尚未决定**（T13–T16：Elsa first-touch not decided → send nothing）；Planet 仓首触与 Elsa 群发不混发。
- **退信 / 婉拒**：退信不删邮箱，标「发不过去」并给替代通道；明确「take us off」→ 永久不触达（westwardsales.com）；Q-33 reseller 只巡检。

来源：`docs/Saga内在逻辑与概念_2026-10-24.md` C8/C12、`docs/gmail/00-Gmail盘点与使用方案.md`、`docs/Saga理念摘读_2026-10-23.md` A23/A25、`docs/成单客户_活跃平台与监控_2026-10-23.md` §2/§4、`docs/跟进总台.md`。


---

## 15. 概念词典与内部术语表

### 15.1 Saga 的 13 个核心概念（C1–C13，概念层）

| # | 概念 | 一句话定义 | 在数据里长什么样 |
|---|---|---|---|
| C1 | 两层三供应商（Saga = 接口层） | Saga 不是产品公司，是接口层：三家供应商在下、客户在上，Saga 提供统一命名 / 资料 / 条款 / 对接人 | PI「Manufacturer: Zhengzhou Saga Telecom」+「Marvell Chip」；STC/STI/STH 覆盖三家来源 |
| C2 | 三道筛子 | 口号「Marvell 管理型」→ Drive 自助资料 → Template 条款；过滤优先于转化 | 群发附件永远是 Product Link PDF；客户能引用型号/价表 = 过第 2 道；付样 / PI / 标签 = 第 3 道 |
| C3 | 顺手单 vs 拼命单 | 只做边际努力小、复购可能大的单；不为一次性大单改变运营方式 | Larch 8,000 台被主动停止；需要新认证 / 新物流 / 新付款 / 新固件的客户权重下调 |
| C4 | 技术流绑定 | 让型号、CLI/MIB、固件行为、规格书进入客户系统；放弃 API/SDK 伪绑定 | NYNEX LibreNMS OID；Go Green IT 博客 + bug 报告；Netaş 样机留在终端客户 |
| C5 | 中性与隐身 | 设备中性无中文；SmartByte 隐身在 Saga 后、Saga 隐身在客户品牌后 | Angora Verge、Fastball FBC-204GP、Mbata BNSC-、James SW-3200 |
| C6 | 价格被动 → 利润底线制 | 不定价不谈价，只守底线（20/25/30 与 20/25/35 两套）+ 30% 封顶 | 价格异议不让步；「target price」无技术问题 = 价格流 → 降级 |
| C7 | 国家 = 运行方式 | 能不能做看收款 / 物流 / 合规通路是否已有，不看需求大小 | TR TRY+WA；RU 货代；NG 客户货代；US/EU PayPal/T/T+DAP；JP PSE |
| C8 | 群发 = 引流到资料 | 让 1% 点开 Drive 自我筛选，不是促成回复 | 14,500 → 1,011 → 208 → 91 → ≈10 → 4 |
| C9 | 三个名字 = 一个流程 | Elsa 首触 → Alan 报价/PI → Simon 早期关系/收款 | STEC / STAG / STSC；「My friend Simon sent you some info… I will take over」 |
| C10 | 边界即资本 | Not-to-Do 清单是让一个人持续可运营的方法 | 命中清单 → 「停点：边界」，不绕路 |
| C11 | 供应商关系优先于客户机会 | 冲突时 Saga 让路；CENTEC 敲门砖但 Peter 产品优先 | Larch 让路；可能与 SmartByte 国内客户重叠 → 「待 Simon 判断冲突」 |
| C12 | 慢是武器 | 固定成本极低，可以等客户替换周期；每次触达增加熟悉度不增加成本 | 群发连续两年；Netaş 4 个月后再发特性表；每户节奏记录 |
| C13 | 信息资产化 | 资料一次做好、季度更新、所有客户共用；既是筛子也是绑定工具 | Resource Library（Roadmap.pdf、STOS V2.4、7.5.x 特性表）；加厚产出是结构化字段 |

因果链：约束（一人 / 无库存 / 不能打价 / 认证有限 / 不做国内 / 供应商优先）→ C10 → C3；→ C2（C8 把人引到筛子，C13 做筛子）→ 少客户 → C4 绑定；→ C6 → C12 → 十年现金流；→ C7；→ C5 → OEM 品牌商最优先；→ C1 → C11；→ C9。

### 15.2 内部术语表（仓库 / 对话里反复出现的黑话）

| 术语 | 含义 |
|---|---|
| **P 池 / 资产池 / 长期客户群** | 三库并池后的长期跟进群（A + B），U115–U117 起的主线「把客户挖干净 → 长期客户资产池」 |
| **精华跟 / 普通跟** | A = 精华跟（季度个人信 + 两月巡检 + 回信 48 h）；B = 普通跟（群发 + 点名） |
| **C 储备** | C ≠ 垃圾；不发、两月巡检、来信即回 B；只有永久 pass 才是 bye |
| **永久 pass** | Gate 0 刚性三条（无邮箱且无 WA / 弹回且无备用 / 明确婉拒），「一旦入选 永不考虑」 |
| **三闸（Gate 0/1/2）** | C 池筛选：闸 0 机筛永久 pass；闸 1 人工批量复核；闸 2 Planet/External 补证；报告在 `docs/requirements/C池闸*` |
| **坐实 / 部分坐实 / 登记底数** | 在官方登记源核到法人主体；付费墙只到部分坐实；「1 查未得即停」 |
| **桌面卡 / 研究档 / 加厚 / 快照后加厚** | 桌面卡 = 一页公司事实卡（External `research/<code>.json`）；研究档 = Saga `research/<code>.json`；加厚 = 补证据字段；快照后加厚 = 用官网快照 `site_snapshots/<code>.json` 再补 `site_contacts` / `snap_thicken` |
| **五项全齐** | 桌面卡 / 官网快照 / 快照后加厚 / 公司登记 / 具名 KP 都有 |
| **副档 / 主档（dup_of）** | 跨库同一公司：副档随主档，不单独计数（名册 2,045 唯一） |
| **对位 / 非对位 / dayjob_fit** | 对位 = 行业与品类与 Saga 交换机对得上；非对位但 Simon 本职可用的（光端机 / DWDM / 光模块）= dayjob_fit，不永久 pass |
| **守界** | 乌克兰 / 伊朗 / 叙利亚、军工、公共采购、生命安全、轨交——留 C 不发 |
| **巨头** | 大分销 / 大运营商 / 大厂（`build.py GIANT_DOMAINS` -45 分）→ C，但不是永久 pass（Supermicro 例外争议 Q-55） |
| **gg** | Simon 的标签「已凉」= 难复购；8 家成单 gg 永不 A |
| **q33_hold** | Q-33 reseller / 洪瑞经销体系客户：不碰、标记、只巡检 |
| **人工定级 / grade_override / overrides.json** | 三库各自的人工覆盖机制（Planet CSV `人工定级` 列 / Saga 研究档 `grade_override` / External `overrides.json`）；PI 活跃·可发展强制 A |
| **四主区** | 土耳其 / 美国 / 英国 / 德国（+ 波兰次重点） |
| **门面机型** | 品牌站 / 产品站 / 群发主推的 9+3 款（§5.2） |
| **两层答法** | 客户问「有没有 X」：先 Marvell AC5 线，再 CENTEC 线 |
| **口径表 #n** | `docs/对外口径一致性_2026-10-24.md` 第 n 行的统一口径 |
| **INH-xx / PR-xx-yy / Q-xx / T29-Uxx / 第 n 批** | 继承规则 / 用户要求总账编号 / 待裁定问题 / 对话轮次 / 变更日志批次 |
| **发送包 / 跟进总台 / 名册 / 缺口表** | 周发送包（W44）/ `docs/跟进总台.md` / `docs/长期客户群_名册_*.md` / `docs/长期客户群_深挖缺口_*.md` |
| **打回候选（快照）** | 两个不同夜晚官网抓取都失败才成为打回候选；单夜失败只记录；**永不自动打回** |
| **MS / MC / TS / TC** | 《计划》状态码：Manufacture Stock / Manufacture Customize / Trade Stock / Trade Customize |
| **STSC / STAG / STEC** | PI 单号前缀 = 经手账号 Simon / Alan / Elsa |
| **Must-Read / A Word / Order Procedure / TTC / CCF** | Drive Template 条款文件；TTC = Saga 对外服务条款名（OEM/ODM/SKD/CKD）；CCF = Commercial Contract Framework |

来源：`docs/Saga内在逻辑与概念_2026-10-24.md` §2/§3、`docs/长期客户群_方案与复核_2026-10-29.md`、`docs/requirements/待统一处理问题清单.md`、本会话记忆。

---

## 16. 仓库地图（elsasaga-cloud/Planet，分支 arena/3f35b9b3-planet）

### 16.1 目录

| 路径 | 内容 |
|---|---|
| `AGENT-CONSTITUTION.md` / `AGENT-README.md` / `README.md` | 宪法（开工先读 / 对话全记录 / 零臆造 / 不可手改 / README 自检 / GitHub 监控…）；操作记录；每轮进度表（第 167 轮） |
| `docs/requirements/` | **对话全记录.md**（每轮原文 + 时间戳，只增不删）、**用户要求总账.md**（PR-xx + INH-01…17）、**待统一处理问题清单.md**（Q-01…Q-77）、**变更日志.md**（995 行提交记录）、AB加厚审计、C池三闸报告 |
| `docs/reference/` | Saga 画像 / 品牌口径 / 商务条款 / 官网全文 / 价格表三档 (SmartByte·HRUI·CENTEC·Realtek 工业·2.5G-10G·2023 首版) / 群发价台账 / 群发剔除名单 / 证书登记表 / 实际进价与毛利 / PLANET 对照 / 继承规则摘要 |
| `docs/rules/` | 客户分级与去重规则、客户档案结构与内容规则、报价与型号规则 |
| `docs/methodology/` | Planet 客户挖掘方法论、死路与死链备案 |
| `docs/smartbyte/`、`docs/suppliers/{HRUI,Hohunet}`、`docs/drive/{MUST-KNOW,Certification,Resource-Library}` | 供应商与 Drive 入库资料 |
| `docs/gmail/` | 三邮箱盘点、A 邮箱总览与真实往来、S 邮箱核对、Elsa 来询未回 |
| `docs/` 根 | Saga 理念摘读 / 内在逻辑与概念 / 对外口径一致性 / 方法论全集 / 两家公司逻辑 HTML / 理解与方向 V0·V1 HTML / 成单客户三件 / 客户功能需求台账 / 各国发信窗口 / 假日避让 / AB 判定讨论稿 / 长期客户群方案·名册·缺口 / 公司底数作业规程 / P 池总名册 / 跟进总台 / **本文** / **方法论全集 2026-10-29 增补版**（`docs/方法论_全集_2026-10-29.md`：§Ⅰ 思维方法 M1–M14 + 新法 A7 / B5–B8 / C8–C13 / D4–D5 / E6–E10；生成器 `scripts/methodology_v2/build.py`；初版 10-27 保留）/ **像素级 SOP**（`docs/方法论_V2_像素级SOP_2026-10-29.md`，方法论的命令级附录；`scripts/sop_v2/build.py`） |
| `Saga Clients/A|B|C/` · `External Clients/<repo>/A|B|C/` · `profile/A|B|C/` | 三库渲染档案（**只读，脚本生成**） |
| `data/saga_clients/` | `entities.json`、`客户主表.csv`、`research/`、`registry/`、`site_snapshots/`、`site_digest.json`、`sieve.json`、`编号映射`、`人工定级.csv` |
| `data/external_clients/` | `{cctv,edgecore,mikrotik}.json`、`overrides.json`、`research/` |
| `data/客户名单_Planet渠道_2026-10.csv` + `batch/*.json` | Planet 库真源 |
| `data/价格主表.csv` / `价格主表_HRUI.csv` / `hohunet_STH对照表.csv` / `hrui_STC对照表.csv` | 价格与型号真源 |
| `data/gmail_{s,a,e}/`、`data/pi_2026-10/`、`data/pi_orders/`、`data/drive_r3/`、`data/smartbyte_*`、`data/hrui_*`、`data/hohunet_*`、`data/sagatele_site/`、`data/wechat_smartbyte_ocr/` | 原始入库资料（邮件 / PI 包 / Drive / 官网抓取 / 微信 OCR） |
| `data/长期客户群_*.csv`、`data/customer_watch/`、`data/github_watch/` | 长期群复核记录、监控产物 |
| 仓库根目录 xls/pdf/docx | SmartByte / HRUI 原始价表、Saga 价表 PDF、特性表 7.5.x、CLI/Web 手册、《Saga公司背景信息.docx》 |

### 16.2 脚本与链路

| 链 | 命令 |
|---|---|
| Saga 库 | `cd scripts/saga_clients && python3 renumber.py --snapshot-md && python3 build.py && python3 render.py` → `renumber.py --restore-dates` → `audit_full.py`（hard 0 / soft 370 基线）+ `audit.py` |
| External 库 | `python3 scripts/external_clients/render.py` |
| Planet 库 | `cd scripts && python3 render.py`（129）；`python3 scripts/audit.py` → errors: 0 |
| 长期群 | `python3 scripts/lt_roster.py`（名册 2,045）、`python3 scripts/lt_gap_audit.py [--no-dns]`（缺口）、`python3 scripts/lt_snapshot_list.py`（补快照清单）、`python3 scripts/saga_clients/lt_snapshot_thicken.py [--dry]`（快照消费 → 加厚 + 打回候选）、`p_roster.py`、`web_watch/checklist.py` |
| 价格 | `scripts/pricing.py`（主表三档）、`scripts/pricing_hrui.py` |
| 入库 | `scripts/gmail_ingest/`、`scripts/drive_ingest/`、`scripts/pi_orders/parse_pi.py`、`scripts/smartbyte_crawl/`、`scripts/suppliers_crawl/`、`scripts/wechat_ocr.py` |
| 监控 | `scripts/web_watch/watch.py`（`--layer all|a|b|…` 大小写不敏感；`snapshot_missing()` / `snapshot_thicken()` / `git_commit()` 带 pull --rebase；`--selftest`）、`scripts/github_watch/watch.py` |
| 台账 | `python3 scripts/changelog.py`（变更日志批次号，~130 s）；README / 总账 / Q 清单手工追加（幂等检查） |
| 本文 | `python3 scripts/saga_intro/build.py` → `docs/Saga全景信息包_<日期>.md/.html` |

### 16.3 GitHub Actions（`.github/workflows/`，沙箱不能推工作流文件、`gh` 403）

| 工作流 | 触发 | 作用 |
|---|---|---|
| `customer-watch.yml` | cron 02:23Z 每夜 + 手动 `workflow_dispatch`（输入 `layer`） | 监控源巡检 + 缺失官网快照补抓 + 快照加厚，bot 自动 commit/push 到本分支（timeout 90 min） |
| `saga-clients-snapshot.yml` | 手动 / 定时 | Saga 客户官网快照 |
| `drive-smartbyte-ingest.yml` | 手动 | Drive 入库 |
| `smartbyte-crawl.yml` | 手动 | SmartByte 官网全量抓取 |

- Actions bot 随时可能推送到本分支 → 任何 push 前 `git fetch && git pull --rebase`；Actions 改过的研究档 / Planet CSV 不要覆盖，rebase 后重跑渲染链。
- 沙箱：2 CPU / 3 GB；外网只有 github / pypi / npm；`curl` 被封用 `fetch_page`；客户网站不可达（靠 Actions）；pip 安装会随重置消失；**沙箱频繁重置 → 尽早 commit**。

### 16.4 Git 配方

```
git -c user.name=elsasaga-cloud -c user.email=elsasaga-cloud@users.noreply.github.com commit -m "..."
git fetch -q origin arena/3f35b9b3-planet && git pull -q --rebase origin arena/3f35b9b3-planet
git push -q origin arena/3f35b9b3-planet && git ls-remote origin arena/3f35b9b3-planet
```

`main` 是 orphan，**永远不要 rebase/merge main**；破坏性 git 操作需 Simon 许可；commit 信息里转义 `$`；中文 / 空格路径用 python 处理。

来源：`AGENT-CONSTITUTION.md`、`AGENT-README.md`、`README.md`、`scripts/*/操作步骤.md`。

---

## 17. 规则总表（写任何东西前过一遍）

### 17.1 继承硬规则 INH-01…17

| # | 规则 |
|---|---|
| INH-01 | Saga = 小型贸易商（SOHO），预算小、不投广告；长期跟进为主 |
| INH-02 | 目标：Marvell 方案接入层交换机；地区欧洲 + 美国/加拿大 + 土耳其；A 类优先，数量不是目标 |
| INH-03 | 台厂不是客户（PLANET 本身及其办事处）；只挖其欧美分销商 / 集成商 / 方案商 |
| INH-04 | 中性包装 / 贴客户型号；不出现 Made in China |
| INH-05 | ABC 定级：A = 真实可追溯需求 + 可直达的人；B = 有邮箱可群发；C = 无邮箱 / 过大 / 区域外 / 不对口；`人工定级` 优先 |
| INH-06 | 编号冻结、只追加；不重排、不回填、不复用（Saga 库 2026-10-25 一次性重编为例外，映射表留存） |
| INH-07 | 集成商 / 顾问优先于分销商；巨头分销直接 C |
| INH-08 | 邮箱只记真实公开找到的；不猜不拼；优先具名 KP，通用邮箱兜底 |
| INH-09 | 每个事实带证据（原文 + URL + 日期），否则「待补证」；事实 / 推断 / 假设分层 |
| INH-10 | 同国 + 法律后缀去重；每个跳过的名字说明原因 |
| INH-11 | 小国不主动挖；乌克兰 / 军工 / 公共采购 / 生命安全标「守界」只做民用商用 |
| INH-12 | 价格格式 `$xx USD EXW（快照日期，15 天有效，报价前核价）` |
| INH-13 | 首触：单一 P1、只问一个问题、不写 "I researched your website"、不提产地；客户英文、笔记中文 |
| INH-14 | 跟进在仓库外进行；仓库只记用户报告的回复 / 退信；退信不删邮箱 |
| INH-15 | 不手改档案；批次 JSON + 脚本渲染；每轮更新 README 并 grep 自检 |
| INH-16 | 破坏性 git 需许可；时间戳未知如实写明，不编造 |
| INH-17 | Saga 不做云管理 / 轨交 / IP67 / 消费级；无 UL / E-mark / KC——命中即降级或 PASS |

### 17.2 Simon 的常设指令（节选，按时间）

- 每轮对话原文 + 时间戳进 `对话全记录.md`；提炼进总账；决策进 Q 清单按默认执行，不一轮一问（T07）。
- 档案与邮件用 Saga 型号；SmartByte 兜底注明；报价 20/25/30；Versa / Planet USA = C。
- 区域：US/CA + 全欧洲 + 土耳其；四主区 + 波兰；V0「TR/中东/东南亚/非洲主战场」是错的；Planet 挖掘暂停不是搁置。
- Drive 为主、SmartByte 官网为真源；Drive 内容全部入库后 Drive 已删除；Elsa 首触未定 → 不发；Actions 跑着也不闲着。
- 客户去重完成；渲染只从 JSON；A 长期跟 / B 慢慢跟 / C 储备（U115 修正「C 垃圾」）；T27 待核留着。
- S/A Gmail 连不上连接器——不要再建议。
- 「啥都入库 不要漏掉」；加厚不套公式、证据为本；**永不覆盖/删除 V0，V1 新文件**；不唠叨；每次复核带时间戳 + commit。
- NYNEX 安排（Saga 推 SmartByte、Peter 技术）；CENTEC 跟进 / 备货 / 固件是 Simon 的事；不说 Saga 是欧洲总代；监控 `freddy36`。
- 成单客户每个活跃平台都挖都监控；HTML 先、MD 定向加厚后。
- 物流两条线；三账号一人；gg = 难复购；绑定深度证据可升但注明 Simon 原级；减少群发是战略取舍；CENTEC 敲门砖；WeChat/LinkedIn 只 James；WhatsApp 客户不写代号；群发低价是旧汇率；加厚顺序 A → B 欧美土 → 其他。
- **永远不要让 Simon 去问 Peter/HRUI 要价格**；grep 证据再说「缺」；「省你的时间 + 有没有长期复利」。
- 回答大白话：搞定 / 没搞定 + 你要做啥 / 不用做啥；批量大、任务长（40–60 分钟一轮）。
- External Clients：按仓库分目录；CCTV agent 永不再跑；按 Saga 实际情况重评；旧仓私有不删；每轮文字报告。
- C 池：先设计再做、不着急；A 90 太少以后再议；闸 0 刚性；乌克兰 / 巨头 / 不对位 / 研究后定 C 不是永久 pass；External 4,351 同池、Planet 也要搞；两月一次监控覆盖面广。
- 《计划》/《背景信息》红线：对外无 152 手机 / s. 邮箱；国内单只私账；芯片线底线；网站永不中文；无电话只 WhatsApp 跳转；slogan 不变；去掉 OEM Factory；不自称贸易商；CENTEC = 核心线之一；LinkedIn 必须；30% 封顶；目标顺序 OEM 品牌商 > 有进口经验 > 分销 > 小集成；轨交主营 PASS；无 UL/E-mark/KC。

### 17.3 Agent 作业守则与踩过的坑

- 价格 / 型号：有效型号集合之外不写；2.5G 等待 SB-263 裁定；RMB 报价待 Simon；Realtek 线按 2026-09-30 新进价；非管理工业线旧成本不可靠。
- 邮箱：`emails_live` 镜像 `emails`；Simon 备注不是 pass 依据；公开页邮箱只进 facts / `site_contacts` / `kp[].email`，**绝不自动写入实体邮箱**；绝不发明邮箱。
- 分级：按 entities grade 选，不按前缀（SC- 可以是 B）；跨库计数以名册 `dup_of` 为准；grade 只经 `grade_override` / `overrides.json` / `人工定级` 改。
- 域名：External `domain_prev`；Planet `网站` 可能带子路径（`host_of`/`reg_domain`）；DNS `nxdomain/dead` 复查两次；域名修正后重生成补快照清单。
- 快照：本地测试用 `--snap-dir /tmp/...`；失败记录含域名；单夜失败不打回；消费端已去膨胀。
- 台账：幂等存在性检查；README 可能无尾换行；PR 行 5 格、Q 行 8 格；CSV `utf-8-sig`；对话全记录只追加、真实 `date -u`。
- 脚本：`ast.parse` 后跑两遍；f-string 内无反斜杠；heredoc 里 f-string 不能有字面 `{}`；`scripts/saga_clients/calendar.py` 会遮蔽标准库 → 用 `importlib` 按路径加载；MX 缓存格式 `[[pref, host], …]`。
- 渲染：`renumber.py --snapshot-md` 前、`--restore-dates` 后；`board.py` 会重排发送包不要重跑；清理 `__pycache__`；HTML 交付物只用内联 CSS（预览沙箱无网）。
- 调研：注册库「1 查未得即停」；A 季度复核；死路见 `docs/methodology/死路与死链备案.md`；不重爬 Mikrotik；不再搜已做过的 registry（从文件重推导）。

来源：`docs/requirements/用户要求总账.md`、`docs/requirements/对话全记录.md`、`AGENT-CONSTITUTION.md`、本会话记忆。

---

## 18. 未决事项（Q 清单与 backlog，默认执行中）

| 编号 | 事项 | 默认 |
|---|---|---|
| Q-77 | §6 默认分层 A / B1 / B2 / C 储备（§11.3） | 默认执行，Simon 一句话可改 |
| Q-75 / Q-73 / Q-62 / Q-63 / Q-64 | U125–U129 期间的分层与并池细则 | 按默认 |
| Q-59 | 12 款 +20% 档远低于列表价：跟 SmartByte 降还是守列表价 | 按档位规则 |
| Q-54 / Q-56 | STH1G 可堆叠线、CENTEC Multi-Gig 铜口 PoE++ 无价 | 不主动报价 |
| Q-52 | Realtek/HRUI 线是否对海外老客户开放（NYNEX FTTH 10G ONT/MC 1,000+/年、$30–40） | 只在客户点名 Realtek 时给 |
| Q-49 / Q-48 / Q-50 | 国内冲突边界 / 「深」绑定画像 / CENTEC DC 线地位 | 按概念层推断执行 |
| Q-47 / Q-42 / Q-41 | HRUI 隐含加价不足 20% / ZX ↔ HR ↔ STC 对照不全 / 三档是否下调 | 按新进价重算；默认档位 |
| Q-51 | 交给 Angora 的 Turkey Client List 64 家（53 在库）Saga 是否继续直发 | 待 Simon |
| Q-46 | 《销售额 & 利润.xlsx》密码保护 | 待 Simon |
| Q-35 / Q-45 | 自有 PEN / MAC 块 | 不申请不更换（T29-U15） |
| Backlog | civil_only 3；SC-2143；StarNet；RU/KZ/BY/UZ 收款；2.5G（SB-263）；SB-583 RMB；W44 发送包；SC-1177 WA；TR 微信；gmail-only 户；SC-3066/3067；RVi；SC-455 / SC-259 / SC-1714 问 Simon；XC-C0157；reg_pending Akçaba / Smartplus / Sapphire / IT Warehouse + US 20；SC-729（ООО «Мицар»）；КОМИКОН；XC-E063；SB-595；gg 8；G1 33；P 池监控扩面；SC-634 补路径；可逆打回名单复核；`build.py` 对位标志回填；ipc2u.de nxdomain；SB-582 国别；SB-110 FB gmail 不自动加；134 快照失败户二夜复核；**Actions 跑完后：Saga 链 + External/Planet 渲染 + 名册 + 缺口审计 + 看 `data/长期客户群_快照打回候选_<日>.csv`** |

来源：`docs/requirements/待统一处理问题清单.md`、本会话记忆。

---

## 19. 来源清单（本文每一句都能回到这些文件）

| 主题 | 文件 |
|---|---|
| 公司画像 / 边界 | `docs/reference/Saga公司画像与边界.md`、`Saga公司背景信息.docx`（根目录） |
| 品牌口径 / 语录 / 官网 | `docs/reference/Saga品牌口径与宣传语录.md`、`docs/reference/Saga官网_sagatele.com_全文_2026-10-22.md`、`data/sagatele_site/` |
| 商务条款 / 物流 / 口径 | `docs/reference/Saga商务条款速查.md`、`docs/对外口径一致性_2026-10-24.md`、`docs/drive/MUST-KNOW/*.md` |
| 理念与概念 | `docs/Saga理念摘读_2026-10-23.md`（A1–A38 / D1–D14 / E1–E26）、`docs/Saga内在逻辑与概念_2026-10-24.md`、`docs/理解与方向_V1_深度串联_2026-10-24.html`、`docs/两家公司逻辑与方向_SmartByte-Saga.html`、`docs/方法论_全集_2026-10-27.md` |
| 价格 / 型号 | `data/价格主表.csv`、`data/价格主表_HRUI.csv`、`docs/reference/价格表_*.md`、`docs/reference/CENTEC_产品表与报价锚_2026-10-24.md`、`docs/reference/实际进价与毛利_校验_2026-10-22.md`、`docs/reference/规格书有_价格表无_型号清单_2026-10-22.md`、`docs/rules/报价与型号规则.md` |
| 认证 | `docs/reference/证书登记表_2026-10-22.md/.csv`、`docs/drive/Certification/认证证书索引.md` |
| 供应商 | `docs/smartbyte/*`、`docs/smartbyte_wechat_summary.md`、`docs/suppliers/HRUI/*`、`docs/suppliers/Hohunet/*` |
| 成单客户 | `docs/成单客户_PI复盘_2026-10.md`、`docs/成单客户_活跃平台与监控_2026-10-23.md`、`docs/成单客户_毛利复盘_内部_2026-10-24.md`、`docs/成单客户_NYNEX_维护计划_2026-10-22.md`、`data/pi_orders/*.csv` |
| 客户需求 / 窗口 | `docs/客户功能需求台账_2026-10-24.md`、`docs/各国发信窗口与来询季节_2026-10-27.md`、`docs/各国假日避让_2026-11_2027-03.md` |
| 分级 / 长期群 | `docs/rules/客户分级与去重规则.md`、`docs/rules/客户档案结构与内容规则.md`、`docs/AB判定_新标准_讨论稿_2026-10-29.md`、`docs/长期客户群_方案与复核_2026-10-29.md`、`docs/长期客户群_名册_2026-10-29.md`、`docs/长期客户群_深挖缺口_2026-10-29.md`、`docs/公司底数_作业规程.md`、`docs/P池_总名册.md`、`docs/跟进总台.md` |
| 规则 / 台账 | `AGENT-CONSTITUTION.md`、`docs/requirements/用户要求总账.md`、`docs/requirements/待统一处理问题清单.md`、`docs/requirements/对话全记录.md`、`docs/requirements/变更日志.md`、`docs/reference/从Mikrotik仓库继承的规则摘要.md` |
| Gmail | `docs/gmail/*`、`data/gmail_{s,a,e}/` |
