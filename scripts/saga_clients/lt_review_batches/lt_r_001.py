#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群复核 · 批 LT-R01（T29-U128，2026-10-29）：优先级 1（C 捞上来的 Saga 户）· 四主区 + 波兰 / 欧洲其他 · △ 与 ○ 档前 40 户。

过法：三闸（闸 1 对位 / 闸 2 坐实）已有证据为底，本批对「存续 / 实体 / 业务线」存疑的 8 户新查（web_search 8 次，2026-10-29，结果写进 facts）；
其余按闸 2 证据桌面复核。标准（Simon U128 ⑤）：行业内 + 对位 + 有一定成单可能（进口同类 / 分销集成主体 / 具体需求 / 成单回信）→ 留 B；
不明朗（法人休眠 / 个体建站中 / Q-33 经销体系现供 / 无路径微型网店）→ 打回 C 储备（回信即回 B）。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lt_review_lib import run  # noqa: E402

BATCH = 'LT-R01'
V = {
    # ---- △ 观察档 ----
    'SC-1009': ('留B', 'Varel Alarm Sistemleri（1990；Siemens Solution Partner；2012 并入荷兰 ARAS；≈14 人）= 土耳其主区弱电 / 安防集成商，项目型采购；行业内 ✔ 对位 ✔ 成单可能 ✔（项目配套）', []),
    'SC-1013': ('留B', 'geMaxx 自有品牌网络产品：gemaxxnetwork.com 在线目录含非 PoE / PoE / 管理 / 工业交换机 + 光纤收发器（产品页 2023-09）；母体 GEMAXX Communications GmbH（Duisburg，11–50 人，crunchbase 标 Active）→ OEM 30% 目标；存续以 info@gemaxx.net 试探，预付',
                [('gemaxxnetwork.com 产品分类：Network Switch（SFPTURSW… 系列 24G+2GF PoE 等）、Industrial Switch Solution、Fiber Switch / Converter', 'https://gemaxxnetwork.com/product-category/network-switch/'),
                 ('GEMAXX Communications GmbH — Duisburg，11–50 人，Active；info@gemaxx.net', 'https://www.crunchbase.com/organization/gemaxx-communications')]),
    'SC-2597': ('打回C', 'Urban Security Group（布鲁克林家族 CCTV 批零）：Q-33 经销体系现供（进口洪瑞），规则「不碰，标记」= 群内也不会主动发；微型；Simon 曾判不行 → C 储备保留 q33_hold 标签', []),
    'SC-2608': ('留B', 'Mayflex（Birmingham 1917；250 人；Sonepar UK；自有品牌 Excel Networking；具名 KP Andrew Percival）：英国主区 OEM 30% 长线目标，巨头采购体系慢但值得挂着；行业内 ✔ 对位 ✔ 自牌 ✔', []),
    'SC-2728': ('打回C', 'Blue Helix Limited（CH 04836349）：Companies House 账目类别 Dormant / SIC 99999 休眠，名录（kompass）却标 20–49 人在营 → 交易主体不明朗（可能经 06248590 等关联号）；按「不明朗 → C 储备」，对方回信即回 B',
                [('BLUE HELIX LIMITED 04836349 — Account category DORMANT；SIC 99999 Dormant Company；Newbury RG14 5TN', 'https://www.aihitdata.com/company/0034F506/blue-helix/overview'),
                 ('kompass：Blue Helix，SIC 46520 电子电信设备批发，20–49 人，成立 2003', 'https://gb.kompass.com/c/blue-helix/gb25016169/')]),
    'SC-2802': ('留B', 'Euro Security Solutions Limited（CH 11094000；2017；伦敦；微型安防集成）：有样品意向 ✔（真实需求信号）；主区 ✔ 对位 ✔ → 留 B，预付；邮箱退信走表内 WA', []),
    'SC-284': ('留B', 'Data Comm for Business, Inc.（Dewey IL 1981；SAM.gov UEI 有效；自研数据通信设备；联邦交通客户）：自有型号 ✔ 对位 ✔ 主区 ✔；联邦 TAA 门槛 → 只做其非联邦 / 商业线，长线', []),
    'SC-3023': ('留B', 'NetTrans Jarosław Żydek（Lublin 个体；NIP 坐实；已直接进口 3C Link / ONV 中国交换机）：个体但有进口同类经验 = 真买家；波兰 ✔ 对位 ✔ → 留 B，预付 100%', []),
    'SC-364': ('留B', 'EasyWind GmbH（Enge-Sande 小型风机制造商；RTS 成单 4 台 MC 自用）：终端自用，复购低但已成单 → 留 B（普通跟 = 只走群发 / 新品通知，零成本）', []),
    'SC-827': ('打回C', 'itjan.de = Dipl.-Ing. Dittmar Janetzky IT Ingenieurbüro（Zirndorf；heinze 标 1–2 人；站点仍为 Impressum 占位页）：个体 + 建站中，表内「100 台用于 Amazon 销售」无日期无后续 → 不明朗 → C 储备；对方再来信即回 B',
                [('itjan.de 首页 = Impressum（Dipl.-Ing. Dittmar Janetzky，Humboldtstr. 1, 90513 Zirndorf）', 'https://itjan.de/'),
                 ('heinze.de 专家档案：Dipl.-Ing. Dittmar Janetzky IT Ingenieurbüro，Anzahl Mitarbeiter 1-2', 'https://www.heinze.de/expertenprofil/dipl-ing-dittmar-janetzky-it-ingenieurbuero/9990227/')]),
    'SC-1173': ('留B', 'JEVASO S.L.（Arteixo；纺织企业电子部门；已成单）：终端自用，复购低但已成单 → 留 B（普通跟 = 群发 / 新品通知）', []),
    'SC-1220': ('留B', 'Starelec Oy（Vaasa 1984；电子元件 / 仪表分销；网络为副线且已有 ONV 同类）：分销主体 ✔ 进口同类 ✔ 对位 ✔ → 留 B', []),
    'SC-1446': ('留B', 'lojaCCTV = Neurónio Digital, Unipessoal Lda.（Ramada；一人公司）：曾回信 ✔（真实信号）+ 安防网店对位 ✔ → 留 B，预付 100%', []),
    'SC-1706': ('留B', 'ITV-Security ApS（CVR 38937456；Randers；安防网店 + 分销；进口 Vivotek + acorid）：进口经验 ✔ 对位 ✔ 欧洲 ✔ → 留 B（微型）', []),
    'SC-2256': ('留B', 'REDFOX S.R.L.（San Benedetto del Tronto；REA AP-180065；安防集成 15+ 年；进口 Utepo；CEO 公开邮箱）：集成主体 ✔ 进口同类 ✔ 对位 ✔ → 留 B', []),
    'SC-2260': ('打回C', 'DEMA s.a.s. = videosorveglianza.it（Vimercate 微型网店）：Q-33 经销体系现供（「不碰，标记」）+ Simon 曾判不行 → C 储备，q33_hold 标签保留', []),
    'SC-2633': ('打回C', 'SiSeCam Solutions S.L.U.（Fuengirola；Axis 全线网店；CIF 未取）：邮箱 fail 无路径 + Axis 体系微型 + Simon 曾判不行 → 不明朗 → C 储备；补到可用邮箱即回 B', []),
    'SC-2718': ('留B', 'MERCASAT SL（Málaga；CIF B92538883；22 年；多牌直进）：直接进口多品牌 = 进口经验 ✔ 对位 ✔ → 留 B，预付（资本微型）', []),
    'SC-2725': ('留B', 'TODO TELECOM, S.L.（Dénia；CIF B53673364；多牌直进网店）：进口经验 ✔ 对位 ✔ 欧洲 ✔ → 留 B，预付', []),
    'SC-2969': ('留B', 'Metrikingdom Unipessoal Lda（Lisboa；NIF 515518425；微型 IT 服务商）：有具体规格需求（2 SFP + 2 RJ45）+ 电话可达 → 有成单可能（小单）→ 留 B，预付 100%', []),
    'SC-427': ('留B', 'TBK Vision（西班牙品牌 1996 起；Picanya；官网称 600,000 台摄像机；产品线含 NETWORK CCTV DEVICES；经 Hommax Sistemas 销售）：自有品牌 ✔ 进口 Utepo ✔ → OEM 30% 目标，留 B；西班牙法人 / 新 KP 待补',
               [('TBK Vision is present in the market since 1996 … NETWORK CCTV DEVICES … A spanish brand', 'https://tbkvision.com/'),
                ('TBK Vision … whose products are marketed in the Spanish market by Hommax Sistemas（2016-10-25）', 'https://www.digitalsecuritymagazine.com/en/2016/10/25/tbk-vision-presenta-su-nuevo-porfolio-con-una-gama-de-camaras-4-en-1/')]),
    # ---- ○ 正式档 ----
    'SC-1297': ('留B', 'Winncom Technologies Corp（Solon OH；1996 起；100–160 人；WISP / 宽带分销）：分销主体 ✔ 体量 ✔ 对位 ✔ 主区 ✔；10 推 0 回 → 换稿一页纸后观察', []),
    'SC-1855': ('留B', 'Kıraç Bilgi ve İletişim Teknolojileri A.Ş.（Eskişehir OSB；2005 起；ZKR 品牌 IP 护士呼叫 / 急救代码系统制造商，2011 前做弱电 + IT）：医院 IP 系统项目需 PoE 交换机，且是品牌制造商 → OEM 30% / 项目配套；行业相邻 ✔ 对位 ✔',
                [('Kıraç Bilgi iletişim Teknolojileri San.Tic. A.Ş. was established by Kıraç Group in 2005 … weak current technologies and IT sector until 2011 … nurse call systems under the ZKR brand', 'https://www.zkr.com.tr/about-us/')]),
    'SC-1935': ('留B', 'LEUNIG GmbH（HRB 1531 Siegburg；1980；KVM / 线缆 / 工业网络批发，Moxa 线）：45 年分销主体 ✔ 工业网络对位 ✔ 主区 ✔ → 留 B', []),
    'SC-2262': ('留B', '1ST-embedded GmbH（Neu Wulmstorf 2010；GF Torsten Sven Trommer = 表内邮箱）：自述「Hersteller und Distributor für Industrie-Computer, 5G Router, Firewall, Switche, IoT Gateway」+ 进口 ISON → 行业内 ✔ 对位 ✔ 决策人直达 ✔',
                [('1ST-embedded GmbH ist ein Hersteller und Distributor für Industrie-Computer, KI-Computer, Mini-PC, 5G Router, Netzwerksicherheits-Appliance, Panel PC, Switche, IoT Gateway, Embedded-Systeme', 'https://www.landkreis-harburg.de/info/poi/1st-embedded-gmbh-913000245-20160.html'),
                 ('D&B：1ST-embedded GmbH，Key Principal Torsten Sven Trommer，Vierkaten 28a Neu Wulmstorf', 'https://www.dnb.com/business-directory/company-profiles/1st-embedded-gmbh.e862275de674cee9453ac6ecc423ac87')]),
    'SC-2372': ('留B', 'Eurosat (Scotland) Limited（SC204360；2000；Glasgow；Oprema 渠道；KP Director Graeme Miller）：25 年安防分销 ✔ 对位 ✔ 主区 ✔ → 留 B', []),
    'SC-2383': ('留B', 'Millbeck Communications / 3G Router Store（2002；Leeds；自有品牌 Proroute 路由 / Fullband 天线；M2M / IoT 硬件 + SIM 分销；进口洪瑞）：网络硬件行业内 ✔ 自牌 ✔ 进口经验 ✔；交换机为相邻品类，体量小 → 留 B',
                [('Millbeck … Founded in 2002 … operate the 3GRouterStore IoT web shop, Proroute Routers and Fullband Antenna brands … UK leader in the distribution of both hardware and data SIMs for 4G/5G IoT & M2M', 'https://gh.linkedin.com/company/millbeck-communications')]),
    'SC-2418': ('留B', 'Streakwave Wireless, Inc.（San Jose 总部 + 4 分仓；无线 / 安防 / 网络增值分销）：中型分销 ✔ 对位 ✔ 主区 ✔ → 留 B（长线；Simon 曾判不行，群发即可）', []),
    'SC-2488': ('留B', 'Fiber24 GmbH（HRB 104376 Hamburg；2008；Planet 在售）：在卖同类台厂品牌 = 对位 + 进口经验 ✔ 分销 ✔ 主区 ✔ → 留 B', []),
    'SC-2606': ('留B', 'Logicbus, Inc.（Chula Vista 2001；40 人；美墨双边工业分销；进口 Atop / 三旺；具名 KP + 采购专员）：行业内 ✔ 进口同类 ✔ 对位 ✔ → 留 B', []),
    'SC-292': ('留B', 'Fiber Instrument Sales, Inc.（Oriskany NY 1985；SAM 有效；100–250 人；$10–53M；自有标 MC；Owner Frank Giotto）：分销 20% 可升贴标 30%；行业内 ✔ 自牌 ✔ 对位 ✔ 主区 ✔', []),
    'SC-2976': ('留B', 'Blake UK Ltd（Sheffield 1971；20–24 人；£2.2M；天线制造 + 进口商；MD Paul Blake）：进口 ✔ 自牌 ✔ 对位 ✔ 主区 ✔ → 留 B', []),
    'SC-2993': ('留B', 'Cables N More（Quakertown PA；2002；ZoomInfo 11–50 人 / <$5M；网络安装器材 + 光纤配件 + 收发器，自有 logo 型号；进口宇航）：进口经验 ✔ 自牌 ✔ 对位 ✔ 主区 ✔ → 留 B；退信 → 找 owner 新地址',
                [('Cables N More offers … networking products, including cables, adapters, and media converters … patch panels, fiber optic accessories；550 Commerce Dr, Quakertown PA；11-50 Employees；<$5 Million；Founded 2002', 'https://www.zoominfo.com/c/cables-n-more/15567269')]),
    'SC-331': ('留B', 'Industrial Communication Products Ltd（Toddington 2008；Advantech / INSYS 英国分销；铁路占比高）：工业分销 ✔ 进口台湾品牌 ✔ 对位 ✔ 主区 ✔ → 留 B；守界：只做非轨交场景', []),
    'SC-440': ('留B', 'İnterland Bilişim Teknolojileri（İstanbul；VKN 4781181726；NACE 461401 电子 / 电信设备批发代理；展会名片）：土耳其主区分销 ✔ 对位 ✔ 坐实 ✔ → 留 B', []),
    'SC-442': ('留B', 'MEPA Elektronik（Kayseri；弱电集成 15 年；11–50 人；Co-Owner Eren Gül；WA 可达；4 / 8 / 16 / 24 口需求）：具体需求 ✔ 决策人 ✔ 对位 ✔ 主区 ✔ → 留 B', []),
    'SC-562': ('留B', 'Baltic Networks（Lisle IL；2005；≈9 人；$6M；WISP 增值分销 50+ 厂牌）：分销主体 ✔ 对位 ✔ 主区 ✔ → 留 B；9 推 0 回 → 换稿', []),
    'SC-700': ('留B', 'AMC – Analytik & Messtechnik GmbH Chemnitz（HRB 995；1990 起 Advantech / NI / Gantner 伙伴）：工业集成 ✔ 进口台湾工业品牌 ✔ 对位 ✔ 主区 ✔ → 留 B', []),
    'SC-704': ('留B', 'ANNICOM LIMITED（Bordon；24 人；董事 Dennis Gates；工业控制电子设计制造 + Kyland 分销）：进口 Kyland 同类 ✔ 对位 ✔ 主区 ✔ → 留 B', []),
    'SC-935': ('留B', 'Semaphore Systems Ltd（London 1979；Advantech 英国分销 1988 起 + IPC 组装；1–10 人）：进口台湾工业品牌 ✔ 对位 ✔ 主区 ✔ → 留 B（微型，低频）', []),
}

if __name__ == '__main__':
    run(BATCH, V)
