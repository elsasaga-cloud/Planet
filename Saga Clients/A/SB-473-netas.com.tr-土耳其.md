# netas.com.tr
**官方名称（调研核实）**：Netaş Telekomünikasyon A.Ş.（İstanbul, TR；netas.com.tr；BIST: NETAS）

> **评级 A**　|　土耳其　|　档案编号 `SB-473`　|　优先级 ★★★　|　状态：成交过·活跃（Simon）
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：成交/下单过；WhatsApp 已加　|　**所在清单**：询盘流水、成交(PI)、Simon:活跃、Xtransfer　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-473
rating: A
rating_auto: A
rating_research: A  # 规模大 + 守界：BIST 上市电信设备/系统集成巨头（1967 年成立；约 1,264–1,403 名员工；ZTE 持股 48.05%、土耳其武装部队基金会持
name_official: "Netaş Telekomünikasyon A.Ş.（İstanbul, TR；netas.com.tr；BIST: NETAS）"
score: 90
country: 土耳其
region: 土耳其
website: netas.com.tr
type: 经销/集成（类型待核）
tier_tags: ["询盘流水", "成交(PI)", "Simon:活跃", "Xtransfer"]
deal: yes
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 67 msgs (out 32 / in 35), 2025-10-13 -> 2026-08-12
p1: none
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：土耳其电信设备与系统集成上市公司 Netaş（1967 年成立，1993 年上市；2025 年末员工 1,264 人、年均 1,368 人；ZTE Cooperatief U.A. 持股 48.05%，Türk Silahlı Kuvvetleri Güçlendirme Vakfı 持股 15%，其余流通；总经理 Sinan Dumlu；业务：电信运营商网络产品、本土基站、系统集成）。Saga 自建站询盘：Ender Bulut 询 OM6X2424(2)-PSE-GW（型号疑为他牌 PoE 交换机/网关）；无跟进。按规则归 C（资料保留）。（调研 2026-10-22；表内兴趣：—）
- **为什么是 A 级**：**调研后定级 A**（规模大 + 守界：BIST 上市电信设备/系统集成巨头（1967 年成立；约 1,264–1,403 名员工；ZTE 持股 48.05%、土耳其武装部队基金会持股 15%）——集团级采购、ZTE 供应链关联且军方基金会股东，超出 Saga 可赢范围；PI 包成单客户，Simon 标签 活跃 → A）；自动分级 A：+50 有成单/下单/买过记录（用户备注或跟进表）；+12 主动询盘（阿里巴巴/自建站/转介）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 土耳其/土耳其；+5 最近活动 2025
- **历史互动**：成交/下单过；WhatsApp 已加
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-488DGGPM-2BT（在手样机）→ 若重开则 STI 系列 L3 型 + 固件 7.5 — 集成商档 25%；对方已有 Saga 供应商账号与报关记录，复购的行政成本为零（C3 顺手单）；样机单 3 台 $545 已成交（PI 2025-12）；重开报价按 CNY ×1.25 ÷ 6.69，快照日期另写
- **第一问（只问一个）**：Does your end customer's multicast design actually require PIM-DM, or would PIM-SM (now available in firmware 7.5 via CLI) be sufficient for the vehicle network?
- **最大未知**：具体需求型号（表内兴趣列为空）
- **下一步**：2026-11 第一周（距 7-17 单向更新满 3 个月） A 邮箱（Alan 主线，抄 Ender 的 gmail endearbulut@gmail.com——他 2026-01-23 主动给的） 一封三行：7.5 固件 PIM-SM 已可用（CLI）、PIM-DM 仍无、问客户的 L3 组播是否 PIM-SM 即可；顺带问留在客户处那台样机的测试结论

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-473` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度（1 台样机留在终端客户处）** ｜ 类型：系统集成商 / 国防通信项目承包（技术流） ｜ 筛子：3（NDA·ECCN 供应商表、PO、PI、付款、报关、样机） ｜ 停点：功能上限——终端客户要 L3 组播 PIM-SM **和** PIM-DM + RIPng/PBR + IP SLA；CENTEC 线 0~40 °C 不够（要 -40~+71 °C） ｜ 复活：固件 7.5（AC5）已支持 PIM-SM（仅 CLI）；若客户能接受「PIM-SM 无 PIM-DM」或出现新的 L2 需求即可重开；车载容器网络另需宽温 L3 接入机 ｜ 通路：TR 已通（USD T/T、DHL；Netaş 自有报关与合规流程） ｜ 节奏：最后 2026-07-17 Alan 发 AC5 特性表（无回）；实质往来 2025-10-13 → 2026-03-02，约 9 轮；Netaş 合规部季度群发仍在抄 Saga ｜ 证据：A 邮箱 k=221f4293f7917453 / 575f6cc1f5d1c75d / 10e6fdf62c477b46 / bbdc059bf34b2fbc / 2b615482de0608a5
- **现状一句话**：土耳其 Netaş（国防/运营商系统集成商，KAP 上市）采购专家 Ender Bulut 2025-10 经 Simon 转给 Alan；2025-12-01 决定以 **STI-488DGGPM-2BT** 作 L2 方案，走完 NDA/ECCN 供应商开户 → 12-23 PO → 12-24 PI 批准 → 2026-01-13 付款（3 台，$545）→ 1 月发货报关；2026-02-26/27 终端客户（车载容器网络）转向 **L3 组播**，Alan 明示 PIM-SM/DM、RIPng/PBR、IP SLA「NOT available with the current chipset」、CENTEC 温度不够，3-02 Ender 留 1 台样机在客户处并「等新 L2 机会」；此后只有 Alan 7-17 单向更新。
- **对方真实需求（有据）**：① 已买：工业 L2+ 8 口 PoE（2×BT）3 台做实验室 + POC；② 真正的项目需求（2026-02-27 原话）：车载容器内多网络整合，2–4 台交换机/车，非核心汇聚，但**必须 L3 + PIM-SM/PIM-DM**，工作温度 **-40~+71 °C**，Netaş 自己做加固外壳；③ 2025-10-17 曾要 Marvell 模组 PCBA 的年量阶梯价（1–10 / 11–25 / 26–…）——说明他们考虑自制整机。
- **断点 / 为什么停在这里**：不是价格、不是信任（PO/付款/报关都走完了），是**芯片方案的功能上限 + 温度**。Alan 2026-02-27 原话「PIM-SM/DM, problem; RIPng/PBR, big problem; IP SLA, problem. It is really hard to move on: R&D, ROI etc.」——属于 C10 边界，不设计绕路。但 7.5 固件已补 PIM-SM（仅 CLI、无 PIM-DM、无 IP SLA，见微信 Peter 2026 原话），边界比 2 月时小了一格。
- **Saga 现在该推什么**：P1 **STI-488DGGPM-2BT（在手样机）→ 若重开则 STI 系列 L3 型 + 固件 7.5**（25% 档，样机单 3 台 $545 已成交（PI 2025-12）；重开报价按 CNY ×1.25 ÷ 6.69，快照日期另写）——集成商档 25%；对方已有 Saga 供应商账号与报关记录，复购的行政成本为零（C3 顺手单）
  - 复购/在买项：STI-488DGGPM-2BT 样机 3 台（2026-01 付款）
  - 做不了 / 要先核的：PIM-DM、IP SLA、RIPng/PBR：7.5 仍不支持（Peter 微信明确）——只能老实说；-40~+71 °C L3 机型：Marvell 工业线温度范围需查规格书后再承诺，不猜；不替 Simon 向 SmartByte 问 PCBA 阶梯价（U29）；若 Netaş 再提 PCBA，由 Simon 决定是否开这条线
- **下一步（具体）**：2026-11 第一周（距 7-17 单向更新满 3 个月）　A 邮箱（Alan 主线，抄 Ender 的 gmail endearbulut@gmail.com——他 2026-01-23 主动给的）　一封三行：7.5 固件 PIM-SM 已可用（CLI）、PIM-DM 仍无、问客户的 L3 组播是否 PIM-SM 即可；顺带问留在客户处那台样机的测试结论
  - 第一问（只问一个）：Does your end customer's multicast design actually require PIM-DM, or would PIM-SM (now available in firmware 7.5 via CLI) be sufficient for the vehicle network?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-12-01 | 来 | Ender Bulut（Netaş） | We have decided to move forward with your STI-488DGGPM-2BT as our L2 switch solution… colleagues… will assist with the NDA and compliance process | 正式选型 + 进入供应商开户流程（筛子第 3 道） | `221f4293f7917453` |
| 2025-12-23 | 来 | Burak Özdemir（采购） | Please find in the attachment the PO | PO 落地；12-24「The PI is approved… We don't require any logo」 | `575f6cc1f5d1c75d` |
| 2026-01-13 | 来 | Burak Özdemir | The payment has been made. Could you help me with the delivery of the products? | 3 台样机 $545 付清（A 总览 §3） | `c1778580f27190ae` |
| 2026-01-21 | 来 | Ender Bulut | IGMPv2, IGMPv3, and IPv4 Multicast (PIM-SM, PIM-DM) specifications are necessary for a Layer-3 switch | 第一次提出组播硬需求 | `bbbaee1e4e6d88df` |
| 2026-01-29 | 来 | Burak Özdemir | The invoice you sent us is from SAGA TELECOM; however… an invoice from SONG LIANG. Why were two different invoices sent? | 报关单据暴露了货代/出口主体与 Saga 不一致——下次出口前统一单据口径（物流两条线，U28） | `2a8ead0c64c4f045` |
| 2026-02-26 | 来 | Ender Bulut | Do you have any idea when L3 Multicast PIM-SM and PIM-DM will be ready? Our costumer wants to go with layer-3 solution and must be include PIM-SM and PIM DM | 停点原话 | `10e6fdf62c477b46` |
| 2026-02-27 | 来 | Ender Bulut | For the CENTEC-based solutions, the operating temperature range (0°C to 40°C) does not seem enough… Our requirement is -40°C to +71°C | CENTEC 替代路线被温度否决 | `bbdc059bf34b2fbc` |
| 2026-02-27 | 去 | Alan | PIM-SM/DM, problem; RIPng/PBR, big problem; IP SLA, problem. It is really hard to move on: R&D, ROI etc. | Saga 明确划边界（C10） | `7adbcd07a050e85a` |
| 2026-03-02 | 来 | Ender Bulut | We have left one STI-488DGGGPM-2BT sample with our customer for basic testing… If we receive new requests for Layer-2 switches… we will contact you | 轻度绑定证据 + 复活条件由对方说出 | `2b615482de0608a5` |
| 2026-07-17 | 去 | Alan | We updated our feature list. 1. Our models are now Marvell AC5 based. 2. This update focuses on L2+ features | 最后一次触达，未提 7.5 已有 PIM-SM（对 Go Green IT 7-10 的邮件提了） | `a323d408b374a3d1` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：A 邮箱 2025-03~08 分片重跑后核对 Simon 最初转介 Netaş 的 S 侧邮件是否有更早接触；留在客户处那台样机的测试结论（对方未反馈）

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | netas.com.tr（取自域名，公司全名待核） | 推断 |
| 国家 | 土耳其 | 事实（用户表）|
| 网站/域名 | netas.com.tr | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Ender Bulut | 事实（用户表） |
| 来源（From） | 2025.10.6 | 事实（用户表） |
| 兴趣（Interested in） | — | 事实（用户表） |
| 用户备注（Remark） | OM6X2424(2)-PSE-GW / from: 自建站 | 事实（用户表） |
| 所在清单 | 询盘流水、成交(PI)、Simon:活跃、Xtransfer | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：在线
- **是谁**：土耳其电信设备与系统集成上市公司 Netaş（1967 年成立，1993 年上市；2025 年末员工 1,264 人、年均 1,368 人；ZTE Cooperatief U.A. 持股 48.05%，Türk Silahlı Kuvvetleri Güçlendirme Vakfı 持股 15%，其余流通；总经理 Sinan Dumlu；业务：电信运营商网络产品、本土基站、系统集成）。Saga 自建站询盘：Ender Bulut 询 OM6X2424(2)-PSE-GW（型号疑为他牌 PoE 交换机/网关）；无跟进。按规则归 C（资料保留）。
- **【年报】员工数与股东**
  > Netaş'ta 2025 yıl sonu itibarıyla çalışan sayısı 1.264'e ulaştı … ZTE, Netaş'ın yüzde 48,04 hissesini ZTE Cooperatief U.A. kanalıyla satın aldı.
  > 来源：https://netas.com.tr/docs/tr/faaliyet_raporlari/2025/Netas%20Faaliyet%20Raporu%202025.pdf（抓取 2026-03-10）
- **【官网 IR】股权结构**
  > ZTE Cooperatief U.A. is the controlling shareholder of Netaş with 48.05%. 15% of shares owned by Turkish Armed Forces Foundation and remaining 36.95% of shares is listed on Istanbul Stock Exchange.
  > 来源：https://netas.com.tr/investor-relations/share-and-investor-information?lang=en（抓取 2021-03-16）
- **【用户表】自建站询盘型号**
  > OM6X2424(2)-PSE-GW / from: 自建站
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【PI】成交单据 STAG20251224020（PI，2025-12-24）：STI-488DGGPM-2BT 共 3 台，USD 545.0；采购 SmartByte RMB 2616.0；Simon 成本表利润 RMB 903.53**
  > 来源：PI.zip:20 土耳其 Burak 活跃 Xtransfer 轻度绑定/STAG20251224020.xls（抓取 2025-12-24）
- **【PI】PI 包文件夹「土耳其 Burak 活跃 Xtransfer 轻度绑定」：Simon 标签 活跃，收款 Xtransfer，轻度绑定；单号 1 个，2025-12-24 → 2025-12-24，销售 USD 545.0 / RMB 0，Simon 成本统计利润合计 RMB 903.53**
  > 来源：PI.zip:20 土耳其 Burak 活跃 Xtransfer 轻度绑定（抓取 2026-10-22）
- **【公开平台核查（T29-U18）】H1 2026 业绩：订单 110 亿 TL（+96%），销售 86 亿 TL（+55%），税前利 2.02 亿 TL**
  > 2026’nın ilk yarısında siparişlerini yüzde 96 artışla 11 milyar TL’ye, satış gelirleri ise yüzde 55 artışla 8,6 milyar TL’ye çıkaran Netaş, 202 milyon TL vergi öncesi kâr elde etti
  > 来源：https://www.capital.com.tr/sirket-panosu/sirket-panosu-haberleri/netas-2026nin-ilk-yarisinda-gelirlerini-ve-karliligini-artirdi（抓取 2026-08-14）
- **【公开平台核查（T29-U18）】2026-08-03 董事长任命 Zhi Ling；Turkcell 与 ZTE/Netaş 合作 5G + Wi-Fi 7 新一代 Superbox**
  > Netaş’ta Üst Düzey Atama: Yönetim Kurulu Başkanlığı Görevine Zhi Ling Getirildi 3 Ağustos 2026 … Turkcell ve ZTE/Netaş’tan 5G ve Wi-Fi 7 Destekli Yeni Nesil Superbox İş Birliği
  > 来源：https://netas.com.tr/medya-merkezi（抓取 2026-08-03）
- **【公开平台核查（T29-U18）】2026-06 KAP 披露：来自土耳其头部运营商 19,584,122 美元服务器订单，2026 年内交付，售后 7 年**
  > müşterisinden sunucu satışına ilişkin olarak 19.584.122 ABD Doları tutarında sipariş almıştır
  > 来源：https://www.cnbce.com/borsa/netas-duyurdu-turkiyenin-onde-gelen-telekom-operatorunden-195-milyon-dolarlik-sunucu-siparisi-h31685（抓取 2026-06-16）
- **【Simon 文档】绑定等级：轻度绑定——「SmartByte 也背书了」**
  > 土耳其 Netas　轻度绑定 = Smartbyte也背书了
  > 来源：Extra Info.zip 根目录《客户绑定情况分析.docx》（data/extra_info_2026-10/text/Extra_Info__客户绑定情况分析.docx__6d196b92.json）（抓取 2026-10-22）
- **KP**：Ender Bulut（（自建站询盘人；职务待核））ebulut@netas.com.tr（用户表） —〔（本地 Clients/ 表格，无公开 URL）〕
- **KP**：Burak Ozdemir（单据联系人）buozdemir@netas.com.tr 〔PI.zip 单据〕
- **调研后定级**：A（原自动 A）——规模大 + 守界：BIST 上市电信设备/系统集成巨头（1967 年成立；约 1,264–1,403 名员工；ZTE 持股 48.05%、土耳其武装部队基金会持股 15%）——集团级采购、ZTE 供应链关联且军方基金会股东，超出 Saga 可赢范围；PI 包成单客户，Simon 标签 活跃 → A
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（年报核对 → 规模大降 C））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Netaş Telekomünikasyon A.Ş. |
| 成立 | 1967-03-31 |
| 总部/地址 | İstanbul, Türkiye |
| 其他 | ZTE 48.05%、TSKGV 15%；总经理 Sinan Dumlu |

- **业务线**：电信运营商网络产品与本土基站；系统集成与 IT 服务
- **触达通道（公开）**：网站: https://netas.com.tr/；公开动态平台（监控中，T29-U18）: 官网媒体中心 netas.com.tr/medya-merkezi（季报/任命/合作新闻，持续更新）；KAP 公开披露（BIST: NETAS）；LinkedIn 公司页；土耳其财经媒体聚合（hurriyet / capital / cnbce）
- **近况信号**：
  - 2026-08-14 H1 2026：订单 +96% 至 110 亿 TL，营收 +55% 至 86 亿 TL，税前利润 2.02 亿 TL；2026-08-03 董事长改任 Zhi Ling（ZTE 系）；2026-06 获国内头部运营商 1,958 万美元服务器订单（2026 年内交付，7 年售后）——公司景气、采购活跃；监控其媒体中心即可知新项目方向
  - 询盘型号 OM6X2424(2)-PSE-GW 非 Saga 型号 → 可能为比价/替代件询价
- **风险/边界**：集团采购 + ZTE 关联 + 军方基金会股东 → C
- **Saga 对位结论**：P1 待核型（无标准对应）（25% 档）——不推进
- **邮件切入句（英文）**：（不主动发送）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 成交记录（PI 包 · 自动汇总）

- **Simon 的标签**（PI 包文件夹名）：**活跃**　|　收款：Xtransfer　|　轻度绑定　|　买方抬头：NETAŞ Telekomünikasyon A.Ş.
- **单号** 1 个（2025-12-24 → 2025-12-24）　|　**销售** USD 545　|　**Simon 成本表利润** RMB 904

| 单号 | 日期 | 单据 | 型号 | 数量 | 金额 | 采购（卖方 / RMB） | Simon 成本表（成本 / 收款 / 利润 RMB） |
|---|---|---|---|---|---|---|---|
| STAG20251224020 | 2025-12-24 | PI | STI-488DGGPM-2BT | 3 | USD 545.0 | SmartByte / 2616.0 | 2885.8 / 3789.33 / 903.53 |

> 口径：同一单号多份文件取 CI > PI（最新修订）> Quotation；Quotation 行不计入销售合计；明细见 `data/pi_orders/销售单据明细.csv`、采购价见 `采购合同明细.csv`；原件在 Release `files-pi_2026-10`。

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：a.sagatelecom　|　**邮件**：67 封（去 32 / 来 35）　|　**期间**：2025-10-13 → 2026-08-12　|　**最后去信**：2026-07-17
- **对方邮箱**：buozdemir@netas.com.tr、cbilik@netas.com.tr、compliance@netas.com.tr、ebaskurt@netas.com.tr、ebulut@netas.com.tr、maltinoz@netas.com.tr
- **最后一封来信**：2026-08-12 compliance@netas.com.tr「Q2/2026 Baş İhracat Uyum Yöneticisi'nden Tüm İş Ortaklarına Mektup - Q2/2026 Let」：[cid:image001.png@01DCDC99.83BD71D0] Değerli İş Ortağımız, Ekte bulunan Baş İhracat Uyum Yöneticimiz tarafından kaleme alınan mektubu iletmekten ve 2026 yılının ikinci çeyreğinde ihracat uyum adına gerçekleştirdiğimiz önemli çalışmaları paylaşmaktan memnuniyet

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Q2/2026 Baş İhracat Uyum Yöneticisinden Tüm İş Ortaklarına Mektup - Q2/2026 Lett | 2026-08-12 | 2026-08-12 | 1 | 0 | 4 |
| Q2/2026 Baş İhracat Uyum Yöneticisi'nden Tüm İş Ortaklarına Mektup - Q2/2026 Let | 2026-08-12 | 2026-08-12 | 1 | 0 | 4 |
| Industrial L2/L3 Managed Switches | 2025-10-13 | 2026-07-17 | 25 | 27 | 285 |
| Q1/2026 Baş İhracat Uyum Yöneticisi'nden Tüm İş Ortaklarına Mektup - Q1/2026 Let | 2026-05-05 | 2026-05-05 | 2 | 0 | 8 |
| Netaş İhracat Uyum Politikası ve Yönetim Taahhüdü / Netaş Export Compliance Poli | 2026-03-02 | 2026-03-02 | 1 | 0 | 4 |
| Q4/2025 Baş İhracat Uyum Yöneticisi’nden İş Ortaklarına Mektup  - Q4/2025 Letter | 2026-02-09 | 2026-02-09 | 1 | 0 | 4 |
| Request for NDA and ECCN form Completion_Saga | 2025-12-02 | 2025-12-04 | 4 | 5 | 67 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：成单精选层　|　**自动源**：4 个　|　**数据截至**：2026-10-23T06:51:07Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-473/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [media_center](https://netas.com.tr/medya-merkezi) | html | HTTP 200 | 2026-10-23T03:05:43Z | 3241 字符；首行：Kariyer |
| [home](https://netas.com.tr/) | html | HTTP 200 | 2026-10-23T02:54:23Z | 6603 字符；首行：NETAŞ - Bilgi ve İletişim Teknolojileri |
| [kap_search](https://www.kap.org.tr/tr/sirket-bilgileri/ozet/1061-netas-telekomunikasyon-a-s) | html | HTTP 200 | 2026-10-23T02:54:23Z | 1980 字符；首行：KAP |
| [feed_auto](https://netas.com.tr/feed) | rss | HTTP 200 | 2026-10-23T04:20:51Z | 10 条；最新：Sat, 15 Aug 2026 09:00:45 Netaş, 2026’nın ilk yarısında gelirlerini ve kârlılığını |

- **人工定期看（登录墙，不自动抓）**：https://www.linkedin.com/company/netas（员工 2,000+；KP Ender Bulut / Burak Ozdemir 个人页用 web 搜索看动态）；https://www.hurriyet.com.tr/haberleri/netas（媒体聚合）

## 联系方式（已有 · 原值照录）

- 邮箱：`ebulut@netas.com.tr`〔企业邮箱；来源：用户表原值〕
- 电话：`+905348602136`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Ender Bulut
- 网站/域名：netas.com.tr
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Ender Bulut | （自建站询盘人；职务待核） | ebulut@netas.com.tr（用户表） / — | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |
| Burak Ozdemir | 单据联系人 | buozdemir@netas.com.tr | 调研核实（公开页） | PI.zip 单据 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 询盘统计表.xlsx#Sheet1:198 |  | https://netas.com.tr/ | 土耳其 | Ender Bulut | 2025.10.6 |  | ebulut@netas.com.tr 90 534 860 2136 已加 | OM6X2424(2)-PSE-GW from: 自建站 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | 待核型（无标准对应，向 SmartByte 核） | 深挖对位：不推进 | — | 深挖对位；档位 25%（经销/集成（类型待核）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $145.7 USD EXW（25% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $188.7 USD EXW（25% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STC-424DGGPM-280W）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付；WhatsApp 直达；土耳其主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
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
| 需求面成立（在卖/在用交换机或 PoE） | ❓ 表内兴趣不含交换机关键词 |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ✅ 有成交史（量待确认） |
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 具体需求型号（表内兴趣列为空）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Follow-up on your switch requirement (model confirmation in progress)

```text
Hi Ender,

Picking up our earlier exchange about PoE / industrial switches. （不主动发送）

One question: is the port mix fixed by the design, or can we propose an equivalent layout?

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 该需求无 Saga 标准型号对应（见「产品决策」P1 待核型）：此样板只确认需求与核型进度，不报价；核型后再出带型号/价格的版本。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-07**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 90）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
