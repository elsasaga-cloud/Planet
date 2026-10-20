# 00 · Gmail 盘点与使用方案（T13，2026-10-20）

> 账号：e.sagatelecom@gmail.com（发件人显示 "Elsa from Saga Telecom"）。3,675 封 / 3,288 个会话。自定义标签：`Replied`（有回复，51 个会话）、`Daily`。  
> 方针：Gmail 是**次要源**，只做索引级读取，不整箱导出到仓库；任何客户事实进仓库时只写"日期 + 主题 + 对方域名"，不复制邮件正文。

## 一、看到了什么
1. **外发群发为主**：2025-03 起每月一波，同一批收件人反复收到 ≈12 个主题（Industrial PoE Switch / Mini Industrial PoE Switch / 8 Port Industrial PoE Switch / 16 Port Ethernet Switch / 90W PoE Managed Switch / Marvell Alleycat5 Solution / 24 Port Fiber Switch / 48 Port PoE Managed Switch / Managed Optical Bypass Switch / 10G Enterprise SFP Switch / Booster PoE Switch / OEM Core Switching Solution / DWDM Core Switching Solution / Updated Ethernet Switches Links / Marvell Managed Commercial Switches / 24 Port PoE Managed Switch / 16 Port Industrial PoE Switch）。最近一波 2026-09-14/15，每 20–30 分钟一封定时发送。
2. **邮件里公开报过的价格**（仅记录，不改仓库报价规则）：24 口 PoE L2+ 10G 上联商用管理型 **170 USD/pc**；STI-21616GP（16 口工业 PoE 非管理 240W）**165 USD/pc**；STI-488XGGBPM（8 口 BT 工业管理型 10G）**215 USD/pc**；快递到门 5 kg 约 130 USD。
3. **回复者地域**：`Replied` 51 个会话以南亚/东南亚/拉美为主（andatelecom.com、microtech.net.pk、starcom.net.pk、ite.net.pk、hfcl.com、devray.in、apolloinfoways.in、bbcpl.in、multybyte.com、optimal.com.ph、omnicom.co.id、quanglam.com.vn、dhakanetworkltd 等），欧美极少。
4. **负面/退订**：westwardsales.com（US）2025-10-13 "not interested… take us off your emailing list" → 永久不再触达；starcom.net.pk 要求必须用公司域名邮箱发件（Gmail 发件被拒）。
5. **欧洲收件人样本**（都在 Elsa 的群发名单里，与本仓库客户有重叠风险）：zintronic.pl、mbs-systems.pl、ergate.cz、all4fiber.com、cablenet.co.uk、idelectro.ru、solimedia.net、multitradepac.com、luxritesecurity.com、avigilon.com。

## 二、与本仓库 87 家客户的交叉检查（本轮结果）
- A 级 15 家 + W11 两家做了域名检索：仅 **PA-006 Kyma（info@kyma.it）** 在 2025-02-17 收到过 "16 Port Ethernet Switch"（无回复）。→ 已在本文件记录，待下一轮把"曾触达 2025-02-17（无回复）"写进 PA-006 档案证据。
- B/C 级 71 家用"多域名 OR"批量检索**不可靠**（Gmail 把 `to:xxx.net` 这类词拆成 token，返回大量无关收件人），结果作废、不采用。

## 三、正确做法（下一轮执行，预计 1 个回合）
1. 分页拉取 `in:sent`（只取 to/date/subject 三个字段，100 封/页，约 35 页），本地 Python 去重得到 `data/gmail_已触达清单.csv`（域名、首次/最近触达日、主题数、是否 Replied、是否退订）。
2. 用该 CSV 与 `data/客户名单_Planet渠道_2026-10.csv` 和 Mikrotik 对照表按域名精确匹配，命中的写进档案"触达历史"，退订的标 `发不过去/已退订`。
3. 以后每次首触前先查这张表（规则化到 `docs/rules/客户档案结构与内容规则.md`）。
4. 不读、不导出任何邮件正文到仓库；需要引用时只写日期+主题。

## 四、对首触邮件写法的启示
- Elsa 的群发模板是"产品 3 个卖点 + 价格 + Do you need samples"，与本仓库规则（单一 P1、一个问题、不报价）不同；两套不要混发给同一家公司——触达表建好前，Planet 仓库的首触暂不发。
