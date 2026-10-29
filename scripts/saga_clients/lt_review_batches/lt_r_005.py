#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群复核 · 批 LT-R05-S（Saga 优先级 2 余下 81 户：研究档无 type 74 + 业务待核 7）· T29-U128 2026-10-29。

依据 = 研究档 summary / mail_review 事实 + 表内互动（回复 / WA / 兴趣 / 跟进次数）。口径同 §2（docs/长期客户群_方案与复核_2026-10-29.md）：
留 B = 行业内 ✔ + 对位 ✔ + 有路径或有互动；打回 C 储备（可逆）= 个人 Gmail / 无公司主体、非行业内（MDF 厂 / POS / 翻新二手）、需求全非对位
（PON / GPON / 升压 / 百兆 MC / WDM）且区域外、官网空或默认页业务不明、微型安装商无需求无进口证据。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lt_review_lib import run  # noqa: E402

BATCH = 'LT-R05S'
B = {
    'SB-1005': '意大利 CCTV / 网络分销商（在线商店，Ubiquiti / Dahua / D-Link 货架）：行业内 ✔ 对位 ✔（PoE 交换机类目）；A 箱推送 4 次 → 留 B 群发',
    'SB-1018': '米兰北郊布线 + 网络分销商，目录中 PLANET 工业小交换机有自有货号：进口台湾同类 ✔ 对位 ✔ → 留 B',
    'SB-104': 'STS Italia（Arcore，1984 起安防 / 特种设施集成商）：回复 1 次 + WA 已加，要光纤传输资料 → 真人往来 ✔ 对位 ✔ → 留 B',
    'SB-1089': '巴西里约面向 ISP 的网络设备分销 / 电商（TP-Link 等），自建站询盘「光开关 130 个」：分销 ✔ 对位 ✔ 具体需求 ✔ → 留 B（区域外，预付）',
    'SB-1100': '印尼 IT / 广播 / 网络安全服务商（Firman Wahyudi）：回复 2 次，问如何购买 / 印尼有无分销 → 真人往来 ✔ 行业内 ✔ → 留 B',
    'SB-1102': '越南网络设备电商 + 弱电施工（站内按品牌卖 Switch / PoE，含洪瑞）：问价 1 次 → 进口中国同类 ✔ 对位 ✔ → 留 B',
    'SB-1104': '印度 Vadodara 电气 / 自动化工程公司（Atul Tiwari）：回复 2 次，问证书、「产品对他有用」→ 真人往来 ✔ 工业线对位 ✔ → 留 B',
    'SB-1108': '卡拉奇消防 / 安防系统集成商 Sunmars（多办事处，网站偏 CCTV）：WA 回复 + 目录已发 → 行业内 ✔ 对位 ✔ → 留 B（预付）',
    'SB-1119': '伊斯坦布尔安防 / 网络分销商 Nokta Elektronik（ORing 授权，主推 PLANET GS-5220）：进口台湾同类 ✔ 四主区 → 留 B',
    'SB-1123': 'Wrexham 安防 / 网络 / 电气贸易分销商 Connectec（PLANET 授权分销，供全英安装商）：进口 ✔ 对位 ✔ 四主区 → 留 B',
    'SB-1124': '琴斯托霍瓦安防分销商 Fonex（SATEL 授权；PLANET 为 CCTV 配套）：行业内 ✔ 对位 ✔ 波兰 → 留 B',
    'SB-1126': 'KLINGER 芬兰公司 CCTV 系统事业部在用 PLANET 工业交换机：终端但有部门级复购可能、欧洲 → 留 B（群发）',
    'SB-1127': '温哥华 B2B IT / AV / 安防硬件批发商，自台湾直接进口 PLANET、也从中国进口：进口证据 ✔ 对位 ✔ 北美 → 留 B',
    'SB-1128': '北波希米亚三店 IT 商 Losan，e-shop PLANET 工业交换机带价带库存：进口 ✔ 对位 ✔ 欧洲 → 留 B',
    'SB-1129': '布鲁塞尔 1989 起 B2B IT 供应商兼电商 Redcorp，PLANET 品牌页以工业 IGS 为主：对位 ✔ 欧洲 → 留 B',
    'SB-1131': '马里兰加固计算 / 工业网络 VAD（PLANET + Moxa 分销）：进口台湾同类 ✔ 工业线对位 ✔ 美国 → 留 B',
    'SB-130': '罗马尼亚 Voinești 小型安防 / 自动化安装商 Bonmag（CUI 登记）：WA 回复 2 次、要「洪瑞档 4/8 PoE + 2 LAN」→ 具体需求 ✔ 对位 ✔ → 留 B（预付）',
    'SB-180': '伊斯坦布尔数据中心 / 弱电工程商 Foline（展会名片，WA 已加）：DC 线 = CENTEC 对位 ✔ 四主区 → 留 B',
    'SB-185': '伊斯坦布尔弱电 / 布线材料供应商 Zeytek（2019 成立，展会要了名片 + 彩页，WA 已加）：行业内 ✔ 四主区 → 留 B',
    'SB-187': 'Perpa 商贸中心 IT 硬件电商 / 批发商 Pelikan Bilgisayar（展会名片，WA 已加）：分销 ✔ 四主区 → 留 B',
    'SB-188': '萨克森-安哈尔特开关柜制造商 SAF（HRB 19446）：自建站询 IM-FP888GW、WA 已加、7 次跟进 → 具体需求 ✔ 工业线对位 ✔ 德国 → 留 B',
    'SB-190': 'A Hamson（1985 起网络集成商，多伦多总部 + 迪拜）：WA 回复，问 GLC-LH-SMD（Saga 无）与 2.5G → 真人往来 ✔ 行业内 ✔ → 留 B',
    'SB-197': '意大利工业网络 / 监控 / 自动化方案商 Intellisystem（站内 poe 377 / switch 条目，三旺在售）：进口中国同类 ✔ 对位 ✔ → 留 B',
    'SB-198': '立陶宛网络设备分销商 Katalita（Ubiquiti / MikroTik / Teltonika；自有品牌 Extralink）：自牌 + 分销 ✔ 对位 ✔ → 留 B',
    'SB-199': '波兰网络设备经销 Korekonect（poe 113 / switch 104 / industrial 54 条目，有 Ewind）：进口中国同类 ✔ 对位 ✔ 波兰 → 留 B',
    'SB-224': '罗马尼亚 Arsenal TV（小型电视 / 视频机构）：WA 回复 2 次，对 48 口工业 PoE + 24 V PoE 有兴趣 → 具体需求 ✔ 欧洲 → 留 B（终端，群发）',
    'SB-267': '新加坡 IT/OT + 物理安防融合服务商 Bio-Cognitive：来信问 4 口 PoE+1 上联 / 8 口 PoE 价格 → 具体需求 ✔ 对位 ✔ → 留 B',
    'SB-277': '西班牙网络 / 无线 / VoIP / 监控专业批发商 Instantbyte（Huawei / Ubiquiti 货架）：分销 ✔ 对位 ✔ 欧洲 → 留 B',
    'SB-301': '加济安泰普 IT 方案商 Ebatek（2005 成立；展会拿彩页，让用 WA 联系）：IT 经销 ✔ 四主区 → 留 B',
    'SB-302': '安塔利亚安防 / 网络技术公司 Antalya Turkuaz（25+ 年；展会拿彩页）：行业内 ✔ 对位 ✔ 四主区 → 留 B',
    'SB-324': '黎巴嫩贸易公司 Elhem Trading（Adnan Melhem）：WA 回复，要 VC 价目 + 看过商业交换机「近期可能有需求」→ 贸易商 ✔ 有互动 ✔ → 留 B（只盯 + 季度一封）',
    'SB-327': '贝鲁特 1989 起自动化与安防承包商 Techno Tower：WA 回复「pls me the price for 8 16 & 24」→ 具体需求 ✔ 对位 ✔ → 留 B',
    'SB-333': '罗马尼亚门禁系统分销商 YLI（Dahua / ZKTeco；poe 35 条目，Utepo 在售）：进口中国同类 ✔ 对位 ✔ 欧洲 → 留 B',
    'SB-434': '西班牙工业 IoT 分销商 S-Connect（Moxa / Advantech 等台湾品牌）：进口同类 ✔ 工业线对位 ✔ 欧洲 → 留 B',
    'SB-435': '宾州客运巴士车载远程信息方案商 Saucon（1997 起）：问过技术问题、Elsa 1:1 单发 9 次 → 终端有互动 ✔ 美国 → 留 B（群发）',
    'SB-439': '巴黎西郊弱电 / 安防集成商 Exxell Vision（2006 成立；家乐福 / 欧尚项目）：WA 已加，要分销价目 → 具体需求 ✔ 对位 ✔ 欧洲 → 留 B',
    'SB-447': '德里工业自动化元器件分销商（工业网络设备在售，从 ONV + 台湾品牌进货）：回复 1 次 → 进口中国同类 ✔ 对位 ✔ → 留 B',
    'SB-467': '安塔利亚通信 / 网络集成商 Nortel İletişim（展会要 catalog，WA 已加）：行业内 ✔ 四主区 → 留 B',
    'SB-477': 'eminnovate.com（美国，表内「基本都是 PLANET 的」）：回复 1 次、2 次跟进；公开检索未坐实但有邮件路径 → 留 B 待坐实（未坐实 + 有路径 ≠ 打回）',
    'SB-492': '诺瓦拉省小型网络方案商 Sistel（布线 + 机柜 + PLANET 工业交换机整包）：进口台湾同类 ✔ 对位 ✔ 欧洲 → 留 B',
    'SB-566': '伊斯坦布尔 Kartal 企业 IT 分销 / 集成商 PCG Bilgisayar（1998 起；珊姐转介 network appliance）：行业内 ✔ 四主区 → 留 B',
    'SB-572': '布尔萨天线 / 卫星 + CCTV / 报警批发零售商 Özel Elektronik（不会英文，要 catalog）：CCTV 批发 ✔ 对位 ✔ 四主区 → 留 B（群发）',
    'SB-586': '内罗毕电气工程 + 安防 + 软件集成商 Matrix Vision（11–50 人，Hikvision）：WA 回复「有用，和 team 沟通是否拿样」→ 真人往来 ✔ 对位 ✔ → 留 B（预付）',
    'SB-602': 'Perpa 商贸中心安防 / 通信分销商 Anıl Telekom（2002 起；老板给名片）：行业内 ✔ 对位 ✔ 四主区 → 留 B',
    'SB-621': '美国光纤 / 铜缆组件制造 + 网店 LANshack（ISO 9001；sfp 1028 / poe 239 / industrial 条目，Ewind 产品多）：进口中国同类 ✔ 对位 ✔ 美国 → 留 B',
    'SB-646': '土耳其大型 IT 分销商 Art Sistem（22 年，135 品牌，5,000+ 经销商；含安防 / 网络）：分销 ✔ 对位 ✔ 四主区 → 留 B',
    'SB-671': '伊拉克 IT 公司 MyTec（Mushtaq Al Takhakh）：WA 已加、「有过详细产品交谈」、19 次跟进 → 真人往来 ✔ 行业内 ✔ → 留 B（预付）',
    'SB-676': '土耳其 IT 批发网店 PC Tedarik（Ruijie / TP-Link / Hikvision 货架）：分销 ✔ 对位 ✔ 四主区 → 留 B',
    'SB-679': '赫特福德郡小型进口代理商 Saratota（代理 PLANET / Patton / LAVA 六家厂商）：进口台湾同类 ✔ 对位 ✔ 四主区 → 留 B',
    'SB-686': '布尔萨 İnegöl 安防与网络方案商 Tek Nokta Destek（CCTV / 报警 / 智能系统；展会拿彩页，WA 已加）：行业内 ✔ 四主区 → 留 B',
    'SB-691': '土耳其 IT / 通信增值分销商 Vitel（KP Gökhan K.；A 箱推送 1 次）：分销 ✔ 四主区 → 留 B（业务细节待核，不影响群发）',
    'SB-798': '巴西 SC 州安防公司 Getec（技术负责人 Leonardo Sezerino，WA 已加，Surveillance projects）：行业内 ✔ 对位 ✔ → 留 B（区域外，预付）',
    'SB-832': 'ALIDEX 西班牙站（与 SB-417 同公司；工业网络 / IoT 分销，ORing 等多品牌）：进口台湾同类 ✔ 工业线对位 ✔ 欧洲 → 留 B',
    'SB-887': '贝尔格莱德安防技术分销商 Stasanet（2013 注册；展会拿彩页，Ady 加了 WA）：行业内 ✔ 对位 ✔ 欧洲 → 留 B',
    'SB-917': '阿联酋工业自动化集成商 Torqsys（SCADA / PLC / UPS；水与污水厂站，100+ 客户）：工业线对位 ✔ 做项目 → 留 B',
}
C = {
    'SB-016': '坦桑尼亚个人买家 Richard Jackson（仅 WA 电话，无公司无邮箱）：2023 起「说要下单」19 次跟进无单 → 无主体无进口证据 → C 储备（下单即回 B）',
    'SB-1101': '巴基斯坦个人 Gmail（Waseem Shah）要目录：无公司主体 → C 储备',
    'SB-1106': '印度个人 WA 联系人 Ruhan Farook（「catalog」一词回复）：无公司主体 → C 储备',
    'SB-1107': '印度个人 WA 联系人 Surya Namberdar（要印度货币价格后无进展）：无公司主体 → C 储备',
    'SB-1110': '阿尔及利亚个人 Gmail（LinkedIn 来源）要 WDM 资料：Saga 无 WDM + 无主体 → C 储备',
    'SB-1111': '西班牙 WA 未具名联系人（身份待核，总表第 42 行）：主体不明 → C 储备（身份坐实即回）',
    'SB-1112': '台湾 Taiwan.xlsx 无公司名 / 无邮箱的回复行：无路径无主体 → C 储备',
    'SB-171': '法兰克福机场旁电信设备翻新 / 维修 / 二手采购商 Comtek（阿里 RFQ 华为 OTN）：二手翻新 + OTN 本职线 ≠ 新品白牌交换机买家 → C 储备',
    'SB-181': '伊斯坦布尔零售自动化 / POS 设备公司 İnterpos（展会名片，没交谈）：POS 非本行业 → C 储备',
    'SB-186': '巴勒克埃西尔 Gömeç 本地安防安装商 Başaran（拿彩页没说要什么）：微型安装商 + 无需求无进口证据 → C 储备',
    'SB-204': '巴基斯坦 AAA Group（Nadeem Shar Din）：需求「光猫 4 路」= GPON（Saga 无）、业务主体不明、1 次负面 → C 储备',
    'SB-227': '菲律宾小型 WISP（Joemar Baquiran）要 PON 产品 + 免费测试：PON 非 Saga 品类 + 微型 → C 储备',
    'SB-300': '土耳其 MDF / 强化地板制造商 Çamsan Ordu（展会拿彩页）：非行业内终端 → C 储备',
    'SB-412': '菲律宾小型网络工程商（Ronald Dumaguing）：需求百兆单纤 20 km MC（Saga 百兆 MC 不供）+ 微型 → C 储备',
    'SB-516': '南非 Brigit 集团（展会拿 2 本 catalog，「会联系」后无下文）：业务线不明 + 区域外 → C 储备（明朗即回）',
    'SB-610': '印尼个人 Gmail（Ahmad Ariyanto）要价格表：无公司主体 → C 储备',
    'SB-642': '土耳其 Apres Teknoloji：官网快照仅标题、业务范围不明、1 次推送无回复 → C 储备（业务明朗即回）',
    'SB-653': '土耳其 Coredata：官网为 Plesk 默认页、业务不明、2 次推送无回复 → C 储备',
    'SB-661': '土耳其 Goldnet：官网快照空、业务不明、1 次推送无回复 → C 储备',
    'SB-668': '土耳其 Midosa：仅联系人 + 电话、业务不明、1 次推送无回复 → C 储备',
    'SB-731': '加拿大个体电信承包 JTS Telecom（Hotmail）：VC（本职线）对他是新领域、一人 → C 储备',
    'SB-786': '保加利亚个人 / 小型安装商 S. Stamenov（Gmail）：回复「最近没需求」+ 1 次负面 → C 储备',
    'SB-821': '白俄罗斯 Server-X（IT / 服务器经销待核）：官网 http_error、表内未跟进无往来、收款待定 → C 储备',
    'SB-855': '捷克 Nextlan：19 次推送无回复、经营状态待核（早期 AI 判「网络设备分销」无现证）→ C 储备（官网恢复或来信即回）',
    'SB-897': '肯尼亚个人 Gmail 安装 / 转售商 Peter Weru：需求百兆单纤 50 对（Saga 百兆 MC 不供）+ 无主体 → C 储备',
    'SB-969': '尼日尔 IT 公司 3STI（阿里询盘升压 5 口）：Saga 无升压 PoE + 区域外 + 无往来 → C 储备',
}


def main():
    assert not (set(B) & set(C))
    V = {c: ('留B', r, []) for c, r in B.items()}
    V.update({c: ('打回C', r, []) for c, r in C.items()})
    print('batch size', len(V), 'B', len(B), 'C', len(C))
    run(BATCH, V)


if __name__ == '__main__':
    main()
