# -*- coding: utf-8 -*-
"""第 131 批（T29-U118f，2026-10-29）—— **C 池三闸 · 闸 2 第八批**：闸 1 第 26–32 批（桶 ⑥ 第 771–1155 户）候选 31 户查底数
（RU 6 / IN 8（含表内「尼泊尔」实为印度 1）/ TW 3 / BR 3 / VN 2 / DE / CH / LV / HK / GE / BD / EC / TZ / ZA 各 1）。
路径：BR → casadosdados / econodata / cnpja / 官网隐私政策（CNPJ）；DE → 官网 Impressum + webvalid（HRB）；CH → northdata / kompass（CHE）；LV → 官网 + tracxn（reģ. Nr.）；
IN → correst / edgeinsights / thecompanycheck（CIN）、tracxn / zoominfo / bebee（法人名 + 规模）、indiamart（GST）、官网 about；VN → yellowpages.vn / thuvienphapluat（MST）；
RU → 官网 contact（ИНН / ОГРН）、secnews / axoft 厂商页；TW → twincn（統編 / 上市上櫃）；HK → 官网 about / contact；GE → yell.ge（ID）；BD → 官网 + YouTube 频道；EC → emis / facebook（Cia. Ltda.）；TZ → africa-internet（Cert. No.）；ZA → 官网 + rocketreach。
1 查未得 → 未坐实（Jjenka / Anfatech / PIIR / Akatel 仅返回同名他户或无结果；Jjenka / Akatel 各补 1 次纯域名查仍无）；同行 ODM 制造商（Konten）/ 网店型（VoIP Telecom）/ 商场微型（Protech）→ 回 C。
国别存疑：SC-1871 Bay Datacom 表内「尼泊尔」实为印度海得拉巴（CIN 泰伦加纳）；SC-1714 Omni Ray 表内「智利」实为瑞士；SC-1713 OAK 表内「玻利维亚」实为拉脱维亚 —— 均待 Simon 确认后改 country_fix。
每户 1 查、depth 1。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 131
F = '2026-10-29'
IN = '— 印度常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 / 微型 预付 100%）+ FOB 深圳 / DAP 买方清关（进口认证要求由买方核，Saga 仅 CE / RoHS / FCC / REACH / UKCA）；周二 / 周四 11–13 IST'
RU = '— 俄语区常规：英文 / 俄文稿、20 / 25 / 30 + 预付 100%（收款 / 物流路径待 Simon：第三国账户 / 中转）+ FOB 深圳；周二 / 周四 10–12 MSK'
TW = '— 台湾常规：中文 / 英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳；周二 / 周四 10–12'
EU = '— 欧洲常规：英文 / 德文稿、20 / 25 / 30 + T/T 50/50 + DAP 买方清关（CE / RoHS / REACH；瑞士非 EU 买方自清关）；周二 / 周四 10–12 CET'
BR = '— 巴西常规：英文 / 葡文稿、20 / 25 / 30 + 预付 100%（首单）+ FOB 深圳（巴西进口税高、买方清关；不承诺 Anatel）；周二 / 周四 10–12 BRT'
OT = '— 其他区常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 / 微型 预付 100%）+ FOB 深圳 / DAP 买方清关；周二 / 周四 当地 10–12'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 欧洲（德 / 瑞士 / 拉脱维亚） ----------------
row('SC-1675', 'de', 'tekmodul GmbH（tekmodul.de；**Impressum：Lindwurmstraße 97a, 80337 München；Registergericht München HRB 158866；USt-IdNr. DE240985730；Geschäftsführer Tassilo Halt；Gesellschaftsvertrag 2005-03-04；经营范围「技术 / 商业咨询 + 各类技术元件及电子电气设备买卖」；electronica 2024 参展（主展商 CompoTEK GmbH 名下）：5G / 4G / NB-IoT / LoRa / 蓝牙 / WLAN 模块 + 工业通信；+49 89 904 118 29-0；info@tekmodul.de**）；表内：Atop（台湾）工业交换机专业经销，国别未填 → .de', 'DE',
    'DE · 1 次检索：tekmodul.de/impressum（HRB / USt / GF）+ webvalid（2005 成立 / 经营范围）+ electronica 2024 展商页；2026-10-29', 'https://www.tekmodul.de/impressum/',
    'HRB 158866（Amtsgericht München）', 'Active（Impressum 2022 / 展会 2024）', '2005-03-04', 'GmbH', '工业通信模块 / 元件分销（慕尼黑）', 'Lindwurmstraße 97a, 80337 München', '小型（专业分销；参展）',
    ['Tassilo Halt — Geschäftsführer'],
    '**德国主区 · 工业通信专业分销 20%：点名 Tassilo Halt 一页纸一次（STI-280GE $46.6 / STI-288GPM $78.9 / STI-244DGGPM $121 工业线 + MOQ 1 + 付费样机；Atop 不点名）' + EU + '**',
    '分销 20%；P 池候选 ★（德国主区 ✔ 台湾工业品牌经销 ✔ 对位 ✔ 坐实 ✔ 决策人具名 ✔）；坐实（Impressum HRB）。')
row('SC-1714', 'other', 'Omni Ray AG（omniray.ch；**Schweizer Handelsregister CHE-105.959.689；LEI 967600D74EO0N5PVE227；Im Schörli 5, 8600 Dübendorf；1950-08-16 创立于苏黎世；AG，资本 CHF 2,050,000；20–49 人；工业自动化贸易 + 服务商（kompass：进口 西欧 / 中亚 / 北美）；MD Roger Müller；Moxa 分销**）；表内「智利」实为瑞士 → 国别待核', 'CH',
    'CH · 1 次检索：northdata（CHE / LEI / 成立日 / 地址）+ kompass（资本 / 人数 / MD / 业务）；2026-10-29', 'https://www.northdata.com/Omni%20Ray%20AG,%20D%C3%BCbendorf/CHE-105.959.689',
    'CHE-105.959.689', 'Active（Handelsregister）', '1950-08-16', 'AG', '工业自动化分销（迪本多夫）', 'Im Schörli 5, 8600 Dübendorf', '中型（CHF 2.05M 资本；20–49 人；75 年）',
    ['Roger Müller — Managing Director'],
    '**欧洲 · 工业自动化分销 20%：点名 Roger Müller 一页纸一次（STI-280GE / STI-288GPM / STI-488DGGPM $147 工业线 + MOQ 1 + 付费样机；Moxa 不点名；瑞士非 EU 自清关）' + EU + '**',
    '分销 20%；P 池候选 ★（欧洲 ✔ 台湾工业品牌分销 ✔ 对位 ✔ 坐实 ✔ 决策人具名 ✔）；坐实（Handelsregister）；表内「智利」→ 瑞士 country_fix 待 Simon。')
row('SC-1713', 'other', 'OAK INTEGRATOR Products SIA（oak-integrator.lv；**Reģ. Nr. 40003540103；2001-04-04；原 Beijer Electronics SIA，2016-02-01 更名；Rīga, Mežkalna iela 5；拉脱维亚 Mitsubishi Electric 独家分销 + Beijer / Westermo / IDEC / Power Electronics / Korenix；2023 营收 $1.33M / 3 人；姊妹 OAK Integrator Solutions SIA（Reģ. 40103496615；2011-12-30；$286K / 1 人）**）；表内「玻利维亚」实为拉脱维亚 → 国别待核', 'LV',
    'LV · 1 次检索：oak-integrator.lv/news（更名 / 品牌线）+ tracxn（两法人 Reģ. Nr. / 营收 / 人数 / 地址）；2026-10-29', 'https://tracxn.com/d/companies/oak-integrator/__O2MYpO0NTFEGt-ZrtiwTJY37PXdoWkQrf5ABZ_ov2m4',
    '40003540103（Products SIA）/ 40103496615（Solutions SIA）', 'Active（tracxn 2025）', '2001-04-04', 'SIA', '工业自动化分销 + PLC 编程（里加）', 'Mežkalna iela 5, Rīga', '小型（$1.33M；3 人）',
    ['（具名 KP 未取；官网 Happy clients 页列客户 ORKLA Latvija 等）'],
    '**欧洲 · 工业自动化小分销 20% + 首单 T/T 50/50：一页纸一次（STI-280GE / STI-288GPM 工业线 + MOQ 1 + 付费样机；Korenix / Westermo 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（欧洲 ✔ 台湾工业品牌集成 ✔ 对位 ✔ 坐实 ✔；小型）；坐实（Reģ. Nr.）；表内「玻利维亚」→ 拉脱维亚 country_fix 待 Simon。')

# ---------------- 巴西 ----------------
row('SC-1689', 'other', 'Above-Net Comercio de Informatica, Telecomunicacao e Servicos Ltda（abovenet.com.br；**CNPJ 05.920.155/0001-60；2003-09-11；Rua Dalcidio Jurandir 255, Loj 123, Barra da Tijuca, Rio de Janeiro RJ 22631-250；CNAE 4651-6/01 计算机设备批发；自述 20+ 年 / 800+ 客户 / 1,500 工程项目；sales@abovenet.com.br；+55 21 2294-3931**）；表内：三旺工业交换机进口', 'BR',
    'BR · 1 次检索：abovenet.com.br 隐私政策（法人名 / CNPJ / 地址）+ cnpjagora + econodata（成立日 / CNAE）；2026-10-29', 'https://www.econodata.com.br/consulta-empresa/05920155000160-abovenet-comercio-de-informatica-telecomunicacao-e-servicos-ltda',
    '05.920.155/0001-60（CNPJ）', 'Ativa（Receita 2026）', '2003-09-11', 'Ltda', '网络 / 电信设备批发 + 工程（里约）', 'Rua Dalcidio Jurandir, 255, Loj 123, Barra da Tijuca, Rio de Janeiro - RJ, 22631-250', '中型（22 年；800+ 客户）',
    ['（具名 KP 未取；sales@ 公共）'],
    '**巴西 · 工业网络分销 / 集成 20–25%：一页纸一次（STI-280GE / STI-288GPM / STI-244DGGPM 工业线 + STC-228GP + MOQ 1 + 付费样机；三旺不点名）' + BR + '**',
    '分销 20%；P 池候选 ★（分销 + 工程 ✔ 已进口中国工业线 ✔ 对位 ✔ 坐实 ✔ 巴西先例 Teltex / Parks）；坐实（CNPJ）。')
row('SC-1691', 'other', 'Alfacomp Automação Industrial Ltda（alfacomp.ind.br / alfacomp.net；**CNPJ 04.430.358/0001-05（总部 Porto Alegre RS，2001-05-10）+ 分支 04.430.358/0002-96（Campinas SP Swiss Park, Av. Antonio Artioli 570 Bloco Lacorno Sala 204；Ativa；资本 R$400,000；matheus@alfacomp.ind.br；(51) 3029-7161）；CNAE 4751-2/01 信息设备零售 + 4742-3/00 电气材料 + 3314-7/05 工业传输设备维修**）；表内：全线迈威产品 + 官网 WA', 'BR',
    'BR · 1 次检索：cnpja（分支 CNPJ / 资本 / 邮箱 / CNAE）+ cnpj.biz（总部 CNPJ / 成立日）；2026-10-29', 'https://cnpja.com/en/office/04430358000296',
    '04.430.358/0001-05（CNPJ 总部）', 'Ativa（Receita 2025-10）', '2001-05-10', 'Ltda', '工业自动化 / 网络设备分销 + 维修（阿雷格里港 / 坎皮纳斯）', 'Av. Antonio Artioli, 570, Bloco Lacorno Sala 204, Swiss Park, Campinas - SP, 13049-900（分支）', '中型（两地；R$400K 资本）',
    ['Matheus — 分支登记邮箱 matheus@alfacomp.ind.br（职务未取）'],
    '**巴西 · 工业分销 20%：WA + 邮件一页纸一次（STI-280GE / STI-288GPM / STI-488DGGPM 工业线 + MOQ 1 + 付费样机；迈威不点名）' + BR + '**',
    '分销 20%；P 池候选 ★（工业分销 ✔ 中国工业品牌全线 ✔ 对位 ✔ WA ✔ 坐实 ✔）；坐实（CNPJ 两处）。')
row('SC-1583', 'other', 'Cartago Comex Ltda（cartagocomex.com；**CNPJ 36.699.505/0001-33；2020-03-17；Rua Joubert de Carvalho 623, Sala 804, Zona 01, Maringá PR 87013-200；资本 R$1,000；1–10 人；CNAE 主 5250-8/02 报关行 + 次 4619-2/00 商业代理；matheus@cartagocomex.com；WhatsApp 44 98831-9311**）；表内：拿 BYXGD 牌子问 HTB MC 100 对', 'BR',
    'BR · 1 次检索：casadosdados（CNPJ / 资本 / CNAE / 邮箱 / WA）+ econodata（人数）；2026-10-29', 'https://casadosdados.com.br/solucao/cnpj/cartago-comex-ltda-36699505000133',
    '36.699.505/0001-33（CNPJ）', 'Ativa（Receita 2025-08）', '2020-03-17', 'Ltda', '报关 / 进口代理（马林加）', 'Rua Joubert de Carvalho, 623, Sala 804, Zona 01, Maringá - PR, 87013-200', '微型（R$1,000 资本；1–10 人）',
    ['Matheus — 登记邮箱 matheus@cartagocomex.com（职务未取）'],
    '**巴西 · 进口代理 △ 观察档 · 贸易 20% + 预付 100%：WA 一页纸一次（STC-110XGE $65 千兆 MC + MOQ 1；百兆 MC 无 → 如实说；代理背后终端 100 对需求）' + BR + '**',
    '贸易 20% + 预付 100%；P 池候选 △ 观察档（数量询问 ✔ 进口代理 = 有进口经验者 ✔ 对位（千兆 MC）✔；微型报关行 → 可否决）；坐实（CNPJ）。')

# ---------------- 越南 / 厄瓜多尔 / 坦桑尼亚 / 南非 / 孟加拉 ----------------
row('SC-1670', 'other', 'Công Ty TNHH Phát Triển Công Nghệ Metsuki VietNam（metsuki.com.vn；**MST 0304967173；2007-05-02 成立；41/1F Tân Thới Nhất 1, KP 3, P. Tân Thới Nhất, Quận 12, TP.HCM；51–100 人；电子电信设备进出口 + CCTV（IP / analog）生产 / 销售 / 安装 + GPS 追踪 + 太阳能；0913 770 579；info@metsuki.com.vn**）；表内：CCTV 为主 + ONV 商业 / 工业 PoE，问 4-8-16-24 口；21 推 0 回', 'VN',
    'VN · 1 次检索：yellowpages.vn（MST / 成立 / 人数 / 业务 / 地址）；2026-10-29', 'https://www.yellowpages.vn/lgs/1187674716/cong-ty-tnhh-phat-trien-cong-nghe-metsuki-vietnam.html',
    '0304967173（MST）', '营业中（目录 2024）', '2007-05-02', 'TNHH（有限）', 'CCTV / 电信设备进出口 + 安装（胡志明市）', '41/1F Tân Thới Nhất 1, Khu Phố 3, Phường Tân Thới Nhất, Quận 12, TP. Hồ Chí Minh', '中型（51–100 人）',
    ['（具名 KP 未取；0913 770 579 官网）'],
    '**越南 · CCTV 进口商 分销 20%：换稿点名 4 / 8 / 16 / 24 口（STC-028GP $28 / STC-228GP $33 / STC-2216GP / STC-2224GP $86 + MOQ 1 + 付费样机；ONV 不点名）' + OT + '**',
    '分销 20%；P 池候选 ○（进口商 ✔ 具体口数需求 ✔ 对位 ✔ 坐实 ✔；21 推 0 回 → 换稿）；坐实（MST）。')
row('SC-1900', 'other', 'Soluciones Tecnológicas Konect Cía. Ltda.（konectsoluciones.com；**Quito，Pio Valdivieso E5-10；2019-05-17 成立；17 人（2024）；电信（有线 + 无线）；emis：2024 净收入 −20.8% / 总资产 +15.8%；Tendata：进口商，36 家供应商（中国 / 拉脱维亚）光纤工具 / 适配器 / PTZ 摄像机；WhatsApp +593 99 565 3148；ventas@konectsoluciones.com**）；RUC 未取；表内：洪瑞 + 海硕 PON，1 推 0 回', 'EC',
    'EC · 1 次检索：emis（法人名 / 成立 / 人数 / 财务趋势）+ facebook（WA / 邮箱）+ tendata（进口记录）；RUC 未取；2026-10-29', 'https://www.emis.com/php/company-profile/EC/Soluciones_Tecnologicas_Konect_CiaLtda_es_9651873.html',
    '未取（RUC 未查；法人名 emis 坐实）', '营业中（emis 2025-02）', '2019-05-17', 'Cía. Ltda.', '电信设备进口 / 集成（基多）', 'Pio Valdivieso E5-10, Quito, Pichincha', '小型（17 人）',
    ['（具名 KP 未取；WA +593 99 565 3148）'],
    '**厄瓜多尔 · 进口集成 25% + 首单预付 100%：WA 一页纸一次（STC-028GP / STC-228GP / STC-2224GP + MOQ 1 + 付费样机；洪瑞现供 → Q-33 口径：默认只推 SmartByte / Marvell 管理线；海硕 PON 不碰）' + OT + '**',
    '集成 25%；P 池候选 ○（进口商 ✔ 中国品牌 ✔ 对位 ✔ 厄瓜多尔先例 SC-2402 ✔）；部分坐实（RUC 未取）；Q-33 洪瑞现供待 Simon。')
row('SC-1803', 'other', 'Habari Node Limited（habari.co.tz；**Arusha，AICC Ngorongoro Wing 4F Room 403；2010 由 Afam (T) Ltd + Arusha Node Marie 创立，Certificate of Incorporation 75466（Companies Act 2002）；接续 1994 起的 Arusha Node Marie ISP；持 National Application Services License；DSL / 无线 / 光纤 + iDirect VSAT；1 个数据中心（colocation）；+255 27 250 4220；sales@habari.co.tz**）；表内：常规千兆小外电 20 个；具名 KP liliani.mboya@ / eliangiringa@', 'TZ',
    'TZ · 1 次检索：africa-internet（Cert. No. / 创立 / 牌照 / 地址）+ datacenterplatform（数据中心 / 电话）；2026-10-29', 'https://www.africa-internet.com/en/provider/tanzania/habari-node/',
    '75466（Certificate of Incorporation）', '营业中（目录 2025）', '2010', 'Limited', '区域 ISP + 数据中心（阿鲁沙）', 'AICC Ngorongoro Wing, 4th Floor, Room 403, Arusha', '小型（区域 ISP）',
    ['Liliani Mboya — 表内具名 KP（职务未取）', 'Eliangiringa — 表内具名 KP（职务未取）'],
    '**坦桑尼亚 · 区域 ISP 自用 直客 25% + 预付 100%：点名 Liliani Mboya 一页纸一次（STC-028GP $28 ×20 / STC-228GP $33 ×20 + 运费 DAP 买方清关 + 付费样机）' + OT + '**',
    '直客 25%；P 池候选 ○（数量询问 ✔ 具名 KP ✔ 对位 ✔ 坐实 ✔；中型区域 ISP ≠ 巨头运营商）；坐实（Cert. No.）。')
row('SC-2885', 'other', 'Plug & Play Solutions = 表内 LS Networks (Pty) Ltd（plugandplay.co.za；**官网：1002 Pretorius Ave, Lyttelton Manor, Centurion 0157；012 667 2513 / 0861 PLUG PLAY；sales@plugandplay.co.za；AI 视频分析 + 门禁 + 安防集成（住宅 + 商业）；rocketreach：2012 创立 / 35 人 / $5M；Sales Executive Kelvin Jordaan**）；Reg No 未取，LS Networks 法人名与官网品牌对应未证；表内：HDMI + 工业级 PoE 交换机 + MC，Simon「单独跟进」', 'ZA',
    'ZA · 1 次检索：plugandplay.co.za（地址 / 电话 / 业务）+ facebook + rocketreach（2012 / 35 人 / $5M / 销售）；Reg No 未取；2026-10-29', 'https://plugandplay.co.za/',
    '未取（Reg No 未查；LS Networks (Pty) Ltd 法人名表内自报）', '营业中（官网 2026）', '2012', '(Pty) Ltd（待核）', '安防集成（森图里恩）', '1002 Pretorius Ave, Lyttelton Manor, Centurion, 0157', '小型（35 人；$5M）',
    ['Kelvin Jordaan — Sales Executive'],
    '**南非 · 安防集成 25%：一页纸一次（STI-288GPM $78.9 / STI-244DGGPM $121 工业 PoE + STC-110XGE 千兆 MC + MOQ 1 + 付费样机；HDMI 延长器无 → 如实说）' + OT + '**',
    '集成 25%；P 池候选 ○（真需求 ✔ 对位 ✔ 南非先例 ✔）；部分坐实（Reg No 未取；法人名待对）。')
row('SC-2891', 'other', 'Trimatrik Multimedia（trimatrikbd.com；**Corporate Office House#01 (GF), Road#20/B, Sector#04, Uttara, Dhaka-1230 + Mouchak 分店 Shop#34, 66 Property Plaza, Malibagh；热线 01711-461346 / 01785-777722 / 01711-766062 等；info@trimatrikbd.com；自述 CCTV supplier / importer / solution provider（IP / HD 摄像机、门禁、考勤）；YouTube 频道 TRIMATRIK BD**）；注册号未取；表内：ONV 商业 PoE 带标卖', 'BD',
    'BD · 1 次检索：trimatrikbd.com 两页（地址 / 分店 / 热线 / 业务）+ YouTube 频道页；注册号未取；2026-10-29', 'https://www.trimatrikbd.com/cctv-camera-company-in-bangladesh',
    '未取（RJSC 未查）', '营业中（官网 2022 / YouTube）', '未取', '未取（疑 proprietorship / Ltd）', 'CCTV 进口 + 零售 + 安装（达卡）', 'House#01 (Ground Floor), Road#20/B, Sector#04, Uttara, Dhaka-1230', '小型（2 店；多热线）',
    ['（具名 KP 未取；官网手机 +880 1785 777722 WA 可试）'],
    '**孟加拉 · 贴牌 CCTV 店 △ 观察档 · OEM 30% + 预付 100%：WA 一页纸一次（STC-028GP $28 / STC-228GP $33 中性包装 + 贴 Trimatrik 牌 + MOQ 1；ONV 不点名）' + OT + '**',
    'OEM 30% + 预付 100%；P 池候选 △ 观察档（贴自有牌 ✔ 进口商 ✔ 对位 ✔；小型 + 非点名国 → 可否决）；部分坐实（注册号未取）。')

# ---------------- 印度 ----------------
row('SC-1795', 'in', 'Bluboxx Communication Private Limited — BBCPL / BluBoxx（bbcpl.in / bluboxx.in；**102/B Surekha Apartment, Above Hira Oil, Pune-Satara Road, Pune 411037；工业网络 + 自动化设备分销（tracxn 两品牌）；ZoomInfo 营收 $5.1M；+91 7875432180**）；CIN 未取；表内：主要是 Planet 的', 'IN',
    'IN · 1 次检索：tracxn 法人页（法人名 / 品牌 / 地址）+ zoominfo（营收 / 电话）；CIN 未取；2026-10-29', 'https://tracxn.com/d/legal-entities/india/bluboxx-communication-private-limited/__4o5mhod8UCZdybdTAdXuS4HYOKFEZoqCL-v4QWaJ-30',
    '未取（CIN 未查；法人名 tracxn 坐实）', '营业中（tracxn 2026-03）', '未取', 'Private Limited', '工业网络设备分销（浦那）', '102/B, Surekha Apartment, Above Hira Oil, Pune-Satara Road, Pune, Maharashtra 411037', '小型（$5.1M）',
    ['（具名 KP 未取）'],
    '**印度 · 工业网络分销 20%：一页纸一次（STI-280GE / STI-288GPM / STC-228GP + MOQ 1 + 付费样机；Planet 不点名）' + IN + '**',
    '分销 20%；P 池候选 ★（工业分销主体 ✔ 台湾品牌经销 ✔ 对位 ✔ Simon 点名印度 ✔）；部分坐实（CIN 未取）。')
row('SC-1797', 'in', 'Cohesive Technologies (P) Ltd（cohesiveglobal.com；**官网页脚 © 2026；Grandstream 印度授权全国分销（IP 电话 + GWN 交换机 / AP / GDMS）；服务 印度 / 斯里兰卡 / 尼泊尔 / 马尔代夫；sales@cohesiveglobal.com**）；CIN / 地址未取；表内：Wi-Tek / Grandstream', 'IN',
    'IN · 1 次检索：cohesiveglobal.com 三个产品页（法人名 / 授权 / 服务区）；CIN 未取；2026-10-29', 'https://www.cohesiveglobal.com/grandstream/gwn7700-network-switch.php',
    '未取（CIN 未查；法人名官网自报）', '营业中（官网 2026）', '未取', 'Private Limited', 'VoIP / 网络分销（印度全国）', '未取（官网未列）', '中型（全国分销 + 4 国）',
    ['（具名 KP 未取；sales@ 公共）'],
    '**印度 · 全国分销 20%（交换机为副线）：一页纸一次（STC-028GP / STC-228GP / STC-2224GP 作 IP 电话配套 PoE + MOQ 1 + 付费样机；Grandstream / Wi-Tek 不点名）' + IN + '**',
    '分销 20%；P 池候选 ○（分销主体 ✔ 中国品牌 ✔ 对位（配套）✔ Simon 点名印度 ✔）；部分坐实（CIN / 地址未取）。')
row('SC-1804', 'in', 'Indra Heera Group / IHT — Indra Heera Technologies（indraheera.com / indraheera.org；**注册办公室 Narayan Colony, Old Police Line, Arrah, Bhojpur, Bihar 802301；自述 Make-in-India 制造商 + RDI（电信 / 网络 / IoT）；OEM/ODM（X 账号自述）；NSDTS「Trusted Source」+ DPIIT 认可（自述）；GeM / ONDC 上架；60% 元件本地采购（自述）；trade@indraheera.org；+91-6182 459639；Toll-free 18008908761**）；CIN 未取；表内：洪瑞现供', 'IN',
    'IN · 1 次检索：indraheera.com/aboutus + indraheera.org/aboutus（地址 / 电话 / 自述资质）+ x.com/indraheeragroup（OEM/ODM 自述）；CIN 未取；2026-10-29', 'https://www.indraheera.com/aboutus',
    '未取（CIN 未查；集团自报）', '营业中（官网 2025）', '未取', 'Private Limited（待核）', '电信 / 网络自有品牌 + 政府采购（比哈尔 Arrah）', 'Narayan Colony, Old Police Line, Arrah, Bhojpur, Bihar 802301', '小型 → 中型（政府渠道；规模自述）',
    ['（具名 KP 未取；trade@ 公共）'],
    '**印度 · 自有品牌（政府渠道）OEM 30%：一页纸一次（STC-228GP / STC-2224GP / STC-4424GCPM 中性包装 + 贴 IHT 牌 + MOQ 1；洪瑞现供 → Q-33 口径：默认只推 SmartByte / Marvell 管理 + 工业线；「Make in India」要求 = 买方自行处理，Saga 不承诺本地化）' + IN + '**',
    'OEM 30%；P 池候选 ★（自有品牌 ✔ 政府渠道 ✔ 对位 ✔ Simon 点名印度 ✔）；部分坐实（CIN 未取）；Q-33 洪瑞现供待 Simon。')
row('SC-1807', 'in', 'Mootek Technologies（mootek.in / mootek.co.in；**Chennai；GST 33AQSPM9347C1ZJ（indiamart；PAN AQSPM = 个人 → 疑 proprietorship，LinkedIn 自称 Pvt Ltd）；创始人 / CEO Moorthy D，2013 起；工业电脑 / 面板机 + 工业以太网 / PoE 交换机 + 协议转换 + GPS；indiamart 产品页以 Mootek 品牌列 IES215 / IES215-1F / IES2005-5T-P48 等型号（= 三旺型号体系 → 贴牌）；16 口工业 PoE 标 ₹21,000 "Made in India"**）；表内：三旺 / 长飞，只发过改邮箱通知', 'IN',
    'IN · 1 次检索：linkedin（Moorthy D / 2013 / 产品线）+ indiamart mootek.co.in 两页（GST / 品牌 Mootek 型号）；2026-10-29', 'https://www.mootek.co.in/industrial-ethernet-switches.html',
    '33AQSPM9347C1ZJ（GSTIN）', '营业中（indiamart 2025 / LinkedIn）', '2013', 'Proprietorship（疑；自称 Pvt Ltd）', '工业电脑 + 工业网络自有品牌 / 贴牌（金奈）', 'Chennai, Tamil Nadu（街道未取）', '小型（创始人经营）',
    ['Moorthy D — Founder / CEO'],
    '**印度 · 贴牌工业交换机 OEM 30%：点名 Moorthy D 一页纸一次（STI-280GE $46.6 / STI-288GPM $78.9 / STI-244DGGPM $121 中性包装 + 贴 Mootek 牌 + MOQ 1 + 付费样机；三旺不点名）' + IN + '**',
    'OEM 30%；P 池候选 ★（自有品牌贴牌 ✔ 已进口中国工业线 ✔ 对位 ✔ 决策人具名 ✔ Simon 点名印度 ✔）；坐实（GST）。')
row('SC-1734', 'in', 'Joohitha Power Systems Private Limited — GridX（gridx.in / joohithapower.com；**CIN U74999TG2011PTC077260；2011-11-04；ROC Hyderabad；授权 / 实收 ₹10 lakh；H.No.1-8-12/20/A/NR, 3rd Floor, Street No.8, Habsiguda, Hyderabad 500007；SCADA / RTU / OLTE（光通信）/ PLCC EPC 咨询，服务电力公用事业；11–50 人；<$5M；info@joohithapower.com**）；表内：光猫 + 工业 2 光 2 电', 'IN',
    'IN · 1 次检索：correst（CIN / 成立 / 资本 / 地址）+ zoominfo（GridX / 业务 / 规模）；2026-10-29', 'https://correst.io/public/company/joohitha-power-systems-pvt-ltd',
    'U74999TG2011PTC077260（CIN）', 'Active（MCA）', '2011-11-04', 'Private Limited', '电力 SCADA / 光通信 EPC 咨询（海得拉巴）', 'H.No.1-8-12/20/A/NR, 3rd Floor, Street No.8, Habsiguda, Hyderabad, Telangana 500007', '小型（₹10 lakh；11–50 人）',
    ['（具名 KP 未取）'],
    '**印度 · 电力 EPC 集成 25%：一页纸一次（STI-154GP $36 样机 4+1+1 SFP / STI-244DGGPM 2 光 2 电场景 + MOQ 1 + 付费样机；光猫走本职线）' + IN + '**',
    '集成 25%；P 池候选 ○（具体型号需求 ✔ 工业对位 ✔ 坐实 ✔ Simon 点名印度 ✔）；坐实（CIN）。')
row('SC-1871', 'in', 'Bay Datacom Solutions Pvt. Ltd.（baydatacom.com；**CIN U32100TG1998PTC028943；1998-02-28；Hyderabad Jubilee Hills Road No. 92, 500096（signalhire）/ Bengaluru #18 Cunningham Rd（zoominfo）；200–500 人；FY22 净销售 ₹2,405 lakh（≈₹24 Cr）；网络 / 安全 / 协作 / 数据中心 / 监控 系统集成；+91 40 4006 4430**）；表内「尼泊尔」实为印度 → 国别待核；表内：问网管工业级 4 光 24 电 PoE', 'IN',
    'IN · 1 次检索：edgeinsights（CIN / 成立 / FY22 财务）+ signalhire（地址 / 人数 / 1998）+ zoominfo（班加罗尔办事处 / 营收 $23.3M）；2026-10-29', 'https://info.edgeinsights.in/company/Bay-Datacom-Solutions-Pvt.-Ltd./131542',
    'U32100TG1998PTC028943（CIN）', 'Active（MCA）', '1998-02-28', 'Private Limited', '网络 / 安防系统集成（海得拉巴 + 班加罗尔）', 'Road Number 92, Jubilee Hills, Hyderabad, Telangana 500096', '中型（200–500 人；₹24 Cr）',
    ['（具名 KP 未取）'],
    '**印度 · 大集成 25%：点名需求 4 光 24 电（STC-4424GCPM $165 L2+ 24 PoE + 4 SFP 商规 → 如实说明非工业级；工业 24 口 STI-0240GE $130 非 PoE）一页纸一次 + 付费样机' + IN + '**',
    '集成 25%；P 池候选 ○（具体型号需求 ✔ 中型集成 ✔ 坐实 ✔ Simon 点名印度 ✔）；坐实（CIN）；表内「尼泊尔」→ 印度 country_fix 待 Simon。')
row('SC-2021', 'in', 'Acceron Infosol Pvt. Ltd.（acceron.net；**Thane 400604 / Mumbai；2007 创立；30–32 人；IT 安全 / 网络 / 无线 增值分销（VAD），自述 APAC；X @AcceronIndia；LinkedIn acceron-india**）；CIN 未取；表内名「distributor」，主动索要 company profile + catalogue，8 推 0 回', 'IN',
    'IN · 1 次检索：x.com/acceronindia（Thane / VAD）+ bebee + rocketreach（2007 / 人数 / 法人名）；CIN 未取；2026-10-29', 'https://bebee.com/in/companies/acceron-infosol-pvt-ltd',
    '未取（CIN 未查；法人名目录坐实）', '营业中（目录 2025）', '2007', 'Private Limited', 'IT 安全 / 网络增值分销（孟买 Thane）', 'Thane, Maharashtra 400604（街道未取）', '小型（30–32 人）',
    ['（具名 KP 未取）'],
    '**印度 · VAD 分销 20%：回「已发资料」稿 + 一页纸一次（STC-228GP $33 / STC-2224GP $86 / STC-4424GCPM $165 分销价 + MOQ 1 + 付费样机）' + IN + '**',
    '分销 20%；P 池候选 ★（真意向 ✔ 分销主体 ✔ 对位 ✔ Simon 点名印度 ✔）；部分坐实（CIN 未取）。')
row('SC-2078', 'in', 'Zebronics India Private Limited（zebronics.com；表内 zebeye.com 退信；**CIN U30000TN1997PTC038037（companyvakil 载 U30006TN1997PTC038037）；1997-04-23；ROC Chennai；授权 ₹4 Cr / 实收 ₹3.28 Cr；GSTIN 33AABCT0664P1Z4；31 个 GST 登记（25 活跃）= 全国网络；No.118 Poonamallee High Road, Vepery, Chennai 600084；MCA 登记邮箱 sandeep.doshi@zebronics.com；消费电子 + 监控自有品牌制造 / 零售**）；表内：洪瑞商业 PoE / FS 贴 Zebronics 牌', 'IN',
    'IN · 1 次检索：thecompanycheck（CIN / 资本 / GST 网络）+ companyvakil（地址 / MCA 邮箱）+ kompass（制造 + 分销 / 监控线）；2026-10-29', 'https://www.thecompanycheck.com/company/zebronics-india-private-limited/U30000TN1997PTC038037',
    'U30000TN1997PTC038037（CIN）', 'Active（MCA 2026）', '1997-04-23', 'Private Limited', '消费电子 / 监控自有品牌（金奈）', 'No.118, Poonamallee High Road, Vepery, Chennai, Tamil Nadu 600084', '大型（实收 ₹3.28 Cr；31 GST 登记；全国品牌）',
    ['Sandeep Doshi — MCA 登记邮箱 sandeep.doshi@zebronics.com（职务未取）'],
    '**印度 · 全国品牌商 OEM 30%（长线）：换 zebronics.com 地址点名采购 / 监控产品线一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 中性包装 + 贴 Zebronics 牌 + MOQ 1；洪瑞现供 → Q-33 口径：默认只推 SmartByte / Marvell 管理线）' + IN + '**',
    'OEM 30%；P 池候选 ★ 长线（自有品牌 ✔ 大型 ✔ 已贴牌中国 PoE ✔ 对位 ✔ 坐实 ✔）；坐实（CIN / GST）；Q-33 洪瑞现供待 Simon。')

# ---------------- 俄罗斯 ----------------
row('SC-2111', 'ru', 'ООО «Амиком» / ТД «Амиком»（ami-com.ru；**Москва；1992 起（mastermann）；安防设备批发 / 小批发分销（面向安装商；目录 25 万 SKU，1C-Битрикс 站 2018 重建）；自有商标 Just / Advert / PRIME（secnews：「新增商标 Just 与 Advert」）；大客户 РЖД / Сбербанк / ЦМТ / ТНК-BP / Ингосстрах / М.видео / McDonalds / Перекрёсток；参展 All-Over-IP / SIPS / SFITEX**）；ИНН 未取；表内：朱姐客户，很多 ONV 型号未改 + Just 疑自有牌', 'RU',
    'RU · 1 次检索：secnews.ru/company/amicom（业务 / 商标 / 客户 / 展会）+ klondike-studio 案例（规模）+ mastermann（1992）；ИНН 未取；2026-10-29', 'https://secnews.ru/company/amicom',
    '未取（ИНН 未查；rusprofile 补查待）', '营业中（目录 / 官网）', '1992', 'ООО', '安防设备批发 + 自有品牌（莫斯科）', 'Москва（街道未取）', '中型 → 大型（25 万 SKU；大客户名单）',
    ['（具名 KP 未取；朱姐渠道在）'],
    '**俄罗斯 · 自有品牌 + 大分销 OEM 30% / 分销 20%：经朱姐线索点名采购一页纸一次（STC-028GP / STC-228GP / STC-2224GP 中性包装 + 贴 Just 牌 + MOQ 1；ONV 不点名）' + RU + '**',
    'OEM 30%；P 池候选 ★（自有品牌 Just / Advert ✔ 大分销 ✔ 已进口中国同类 ✔ 对位 ✔ Simon 点名俄罗斯 ✔）；部分坐实（ИНН 未取）；收款 / 物流路径待 Simon。')
row('SC-2730', 'ru', 'RVi Group（rvigroup.ru；**俄罗斯视频监控开发 / 制造商，2007 起；隶属 ГК «Рубеж»；产品线：IP 摄像机 / NVR / 交换机及网络设备 / 监视器 / 解码器 / IP 扬声器 / 软件 R-OPERATOR；持证可用于关键基础设施 / 交通 / 防爆区（axoft 厂商页自述）；目录另列 RUBEZH™ 品牌**）；ИНН 未取；表内：「主要是 hasivo 的商业 PoE」= 贴牌，19 推 0 回', 'RU',
    'RU · 1 次检索：axoftglobal.ru/vendors/rvi（厂商介绍 / 集团 / 产品线）+ rvigroup.ru 目录两页（网络设备类目）；ИНН 未取；2026-10-29', 'https://axoftglobal.ru/vendors/rvi',
    '未取（ИНН 未查；集团 Рубеж）', '营业中（官网 2026）', '2007', 'ООО（集团成员）', '视频监控自有品牌制造（俄罗斯）', '未取', '大型（全国品牌；集团）',
    ['（具名 KP 未取）'],
    '**俄罗斯 · 品牌商 OEM 30%（长线）：点名硬件采购一页纸一次（STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM 中性包装 + 贴 RVi 牌 + MOQ 1；hasivo 不点名；关键基础设施 / 军标项目不参与）' + RU + '**',
    'OEM 30%；P 池候选 ★ 长线（自有品牌 ✔ 已贴牌中国 PoE ✔ 对位 ✔ Simon 点名俄罗斯 ✔）；部分坐实（ИНН 未取）；守界：集团是否涉制裁名单待核 + 收款路径待 Simon。')
row('SC-1917', 'ru', 'ООО «Воип Телеком» — VoIPdevice（voipdevice.ru / spb.voipdevice.ru；**ИНН 7733663234；КПП 773301001；ОГРН 1087746847506；2008 起（自述「从未更换法人」）；办公 107370 Москва, ул. Ивантеевская 25А, 3 этаж；юр. 125368 Москва, ул. Дубравная 36；АЛЬФА-БАНК 账户；网店 + IP 电话 / 网络项目实施（自述）**）；表内：CCTV + Witek 很多，17 推 0 回', 'RU',
    'RU · 1 次检索：voipdevice.ru/contact（ИНН / ОГРН / 地址）+ spb.voipdevice.ru（业务 / 2008）；2026-10-29', 'https://voipdevice.ru/contact/',
    '7733663234（ИНН）/ 1087746847506（ОГРН）', '营业中（官网 2026）', '2008', 'ООО', 'VoIP / 网络设备网店 + 实施（莫斯科 / 圣彼得堡）', 'ул. Ивантеевская, д. 25А, 3 этаж, Москва 107370', '小型（网店型）',
    ['（具名 KP 未取）'],
    '**网店型 → 回 C 储备；来信再起则分销 20% + 预付 100%**' + RU,
    '回 C（坐实但网店 + 实施型；17 推 0 回；Wi-Tek 现供）。')
row('SC-1755', 'ru', 'Jjenka（jjenka.com；**2 查（俄文 + 纯域名）均无公司信息，仅同名个人 / 无关结果 → 法人未取 → 未坐实**）；表内：「need MM GE converter about 20pcs」，8 推 0 回', 'RU',
    'RU · 2 次检索：jjenka.com 媒体转换器 ИНН（无）+ "jjenka"（无关）→ 未坐实；2026-10-29', '',
    '未取', '未坐实', '未取', '未取', '网络设备（俄罗斯，待证）', '未取', '未知',
    ['（具名 KP 未取）'],
    '**未坐实 → 回 C 储备；来信再起则 STC-110XGE $65 ×20 报价 + 预付 100%**' + RU,
    '回 C（未坐实：2 查无结果）。')
row('SC-2841', 'ru', 'PIIR（piir.ru；**1 查仅得同名 ООО «ПИИР» = Проектный институт инфраструктурных решений（ИНН 7810935340；ОГРН 1217800194622；2021-12-15；СПб Московский пр. 140；设计院，29 项 ОКВЭД）— 与 piir.ru 网络设备分销归属未证 → 未坐实**）；表内：本土牌子，用的国内的', 'RU',
    'RU · 1 次检索：spark-interfax / rusprofile 同名 ООО ПИИР（设计院）→ 域名未对上；2026-10-29', '',
    '未取（同名 ИНН 7810935340 不采）', '未坐实', '未取', '未取', '网络设备分销（俄罗斯，待证）', '未取', '未知',
    ['（具名 KP 未取）'],
    '**未坐实 → 回 C 储备；来信再起则分销 20% + 预付 100%**' + RU,
    '回 C（未坐实：1 查仅同名设计院）。')
row('SC-2972', 'ru', 'Akatel（akatel.ru no_mx / alarmex.ru；**2 查（Акател alarmex.ru ИНН + "alarmex.ru"）仅得同名他户（Альматекс / Алматекс / Арамекс；Alarmex 美国 / 墨西哥）→ 法人未取 → 未坐实**）；表内：「从中间商采购中国产品，想从中国直接购买」，两部座机，WA 加不上', 'RU',
    'RU · 2 次检索：Акател alarmex.ru（同名他户）+ "alarmex.ru"（美 / 墨同名）→ 未坐实；2026-10-29', '',
    '未取', '未坐实', '未取', '未取', '安防 / 网络采购（俄罗斯，待证）', '未取', '未知',
    ['（具名 KP 未取；座机 +7 495 748-11-96 / 973-1353 在表）'],
    '**未坐实 → 回 C 储备；真意向 ✔ → 来信或电话接通再起则分销 20% + 预付 100%**' + RU,
    '回 C（未坐实：2 查无；真意向保留）。')

# ---------------- 台湾 / 香港 ----------------
row('SC-2695', 'tw', '慧友電子股份有限公司 EverFocus Electronics Corp.（everfocus.com；**統編 89639615；上市 5484 慧友；1995 設立；實收資本 NT$1,185,078,470（twfile）；登記地址 新北市新店區寶橋路235巷133號7樓之1（twincn）/ 汐止區新台五路1段79號12樓之1（twfile）；代表人 莊永順（twincn）/ 董事長 黃佳銘（twfile）；登記工廠 65011553 生產中；(02)2662-2338**）；表内：安防品牌商，商业 PoE 自有牌', 'TW',
    'TW · 1 次检索：twincn（統編 / 上市 / 代表人 / 工廠）+ twfile（實收 / 董監事）；2026-10-29', 'https://twincn.com/item.aspx?no=89639615',
    '89639615（統編）/ 上市 5484', '核准設立 · 營業中', '1995', '股份有限公司（上市）', '安防監控品牌製造（新北）', '新北市新店區寶橋路235巷133號7樓之1', '大型（上市；實收 NT$11.85 億）',
    ['莊永順 — 代表人（twincn）', '黃佳銘 — 董事長（twfile）'],
    '**台灣 · 上市品牌商 OEM 30%（長線）：找硬體採購一頁紙一次（STC-028GP / STC-228GP / STC-2224GP 中性包裝 + 貼 EverFocus 牌 + MOQ 1；不談 NDAA）' + TW + '**',
    'OEM 30%；P 池候选 ★ 长线（自有品牌 ✔ 上市 ✔ 对位 ✔ 坐实 ✔；台湾 OEM 先例 AVTECH / Hi Sharp）；坐实（統編）。')
row('SC-2839', 'tw', '宸曜科技股份有限公司 NEOUSYS TECHNOLOGY INC.（neousys-tech.com；**統編 29169532；上櫃 6922 宸曜；2010-07-14 設立；資本額 NT$500,000,000 / 稅籍資本 202,815,000；新北市中和區建八路198號11樓（登記）/ 中正路868之3號15樓；董事長兼總經理 高明和；發言人 藍林忠（業務副總）；工廠登記 65005448（電腦電子製造）；僑外資；(02)2223-6182**）；表内：工业电脑品牌商，自有 5 电口工业 FS，20 推 0 回', 'TW',
    'TW · 1 次检索：twincn（統編 / 上櫃 / 董事長 / 發言人）+ alltwcompany（資本 / 工廠 / 進出口登記）；2026-10-29', 'https://www.twincn.com/item.aspx?no=29169532',
    '29169532（統編）/ 上櫃 6922', '核准設立 · 營業中', '2010-07-14', '股份有限公司（上櫃）', '強固型工業電腦製造 + 工業網路配套（新北中和）', '新北市中和區建八路198號11樓', '大型（上櫃；資本 NT$5 億）',
    ['高明和 — 董事長 / 總經理', '藍林忠 — 業務副總 / 發言人'],
    '**台灣 · 上櫃品牌商 OEM 30%（長線）：點名產品經理一頁紙一次（STI-280GE / STI-288GPM / STI-244DGGPM 中性包裝 + 貼 Neousys 牌作工業電腦配套 + MOQ 1；20 推 0 回 → 換 OEM 稿）' + TW + '**',
    'OEM 30%；P 池候选 ★ 长线（品牌商 ✔ 上櫃 ✔ 工业对位 ✔ 坐实 ✔）；坐实（統編）。')
row('SC-2971', 'tw', '元生工業股份有限公司 KONTEN NETWORKS INC.（konten-networks.com / sbjlink.com；**統編 65489708；2016-09-09 設立；新北市新店區民權路108號7樓；代表人 張聰洲；董監事 張聰洲 / 陳許淇 / 林雅鈴 / 張宇曦；自述「OEM/ODM 設計製造工業乙太網交換器」（ITS / 鐵路 / M12 / PoE bt / L3 / 10G）；Tendata：46 批出口至 13 家買家**）；表内：「刷的自己 logo」工业 FS / SFP / MC / 串口，5 推 0 回', 'TW',
    'TW · 1 次检索：twincn（統編 / 董監事 / 地址）+ konten-networks.com 產品頁（MP-0804G 8+4 2.5G SFP）+ tendata（出口記錄 / 自述 ODM）；2026-10-29', 'https://twincn.com/item.aspx?no=65489708',
    '65489708（統編）', '核准設立 · 營業中', '2016-09-09', '股份有限公司', '工業交換器 OEM/ODM 製造（新北新店）', '新北市新店區民權路108號7樓', '小型（2016；出口 13 買家）',
    ['張聰洲 — 代表人 / 董事'],
    '**同行 ODM 製造商 → 回 C 儲備（不推銷；觀察其出口買家線索）**' + TW,
    '回 C（坐实但同行：自述工业交换机 OEM/ODM 设计制造 = 竞品制造商，非买家）。')
row('SC-2587', 'other', 'tactio Corporation（tactio.net；**2006 创立于香港；Unit 1–9, 8/F, Global Gateway Tower, 63 Wing Hong Street, Lai Chi Kok, Kowloon；Tel (852) 3188 0767；marketing@tactio.net；自有品牌 INEO 工业 PoE 交换机（IGM0840P 8 PoE+ 4 SFP / IGU0420P 4+2）+ 交换机 8–48 口至 10G + MC + PoE + AP + 线缆；自述「R&D 与制造团队」**）；CR No. 未取；表内：「国内外壳贴自有牌，有人卖他们的」，8 推 0 回', 'HK',
    'HK · 1 次检索：tactio.net 首页 / about / contact（创立 / 地址 / 电话 / 产品线）；CR No. 未取；2026-10-29', 'https://tactio.net/about',
    '未取（CR 未查）', '营业中（官网 2023）', '2006', 'Corporation（Ltd 待核）', '网络设备自有品牌（香港荔枝角）', 'Unit 1–9, 8th Floor, Global Gateway Tower, 63 Wing Hong Street, Lai Chi Kok, Kowloon, Hong Kong', '小型 → 中型（全线自有品牌）',
    ['（具名 KP 未取；marketing@ 公共）'],
    '**香港 · 品牌商 OEM 30%：换 OEM 稿一页纸一次（STI-288GPM $78.9 / STI-244DGGPM $121 / STC-228GP $33 中性包装 + 贴 tactio / INEO 牌 + MOQ 1 + 付费样机；中文稿可）' + OT + '**',
    'OEM 30%；P 池候选 ★（自有品牌全线 ✔ 已贴牌中国同类 ✔ 对位 ✔）；部分坐实（CR 未取）。')

# ---------------- 格鲁吉亚 / 越南（回 C） ----------------
row('SC-2687', 'other', 'PROTECH（protech.com.ge；**yell.ge：Tbilisi, Nadzaladevi, 7 Ts. Dadiani St., Karvasla 商场 3F Office A308/1；Identification number 438117477；消防 / POS / 安防摄像 / BMS / 网络硬件 / 线缆 / UPS 销售 + 安装；+995 577 59 44 99；info@protech.com.ge（官网 contact 对上）**；bia.ge 同名 Protech Georgia LLC 405097005 为假肢业务 → 不采）；表内：「主要是 ONV 的，带标卖」，16 推 0 回', 'GE',
    'GE · 1 次检索：yell.ge（ID / 地址 / 类目）+ protech.com.ge/en/contact（地址 / 电话对上）；2026-10-29', 'https://www.yell.ge/company.php?id=146486&lan=eng',
    '438117477（Identification number，yell.ge）', '营业中（官网）', '未取', '未取（LLC 待核）', '安防 / 消防 / 网络安装商（第比利斯）', '7 Ts. Dadiani St., Shopping Centre Karvasla, Fl. 3, Office A308/1, Tbilisi', '微型（商场办公室）',
    ['（具名 KP 未取）'],
    '**微型商场安装商 → 回 C 储备；来信再起则 OEM 30% + 预付 100%（贴牌最小起订）**' + OT,
    '回 C（坐实但微型 + 非点名国 + 16 推 0 回；贴牌线索保留）。')
row('SC-1883', 'other', 'Anfatech（anfatech.com.vn；**1 查仅得近名 CÔNG TY CỔ PHẦN CÔNG NGHỆ ANPHATECH（MST 0317549776；2022-11-03；Thủ Đức TP.HCM；代表 Trần Hậu Toàn；税号 2024-12-12 已关闭 = 停业）及无关同名 → anfatech.com.vn 归属未证 → 未坐实（若为同一主体则为红旗）**）；表内：ONV 全线产品引进 + QNAP，8 推 0 回', 'VN',
    'VN · 1 次检索：thuvienphapluat 近名 ANPHATECH（已停业）+ 无关同名 → 域名未对上；2026-10-29', '',
    '未取（近名 MST 0317549776 不采）', '未坐实', '未取', '未取', 'ONV 全线进口（越南，待证）', '未取', '未知',
    ['（具名 KP 未取）'],
    '**未坐实 → 回 C 储备；来信再起则分销 20% + 预付 100%**' + OT,
    '回 C（未坐实：1 查仅近名已停业户）。')

print('b131_c done')
