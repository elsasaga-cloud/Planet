#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 92 批 · PL 4 户（T29-U88，2026-10-28）：web_search depth 1 各一次（rejestr.io / bizraport / 官网页脚 KRS 摘要）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 92
put('SB-092', key='pl', batch=B, name='Spacetronik Sp. z o.o.（spacetronik.pl；Kościan, wielkopolskie）', iso='PL', fetched=F,
    source='PL · 1 次检索：wyszukiwarkakrs / bizraport / aleo / gowork（KRS 0000993625；NIP 6981862105；REGON 523197029；2022-09-23 登记；股本 50,000 zł = 1,000 股全部由 Mikołaj Adam Tomaszewski 持有；Prezes Zarządu 同人；bizraport 财报：营收 29.7 mln zł / 资产 22.3 mln zł；KRZ 无破产重整）+ okredo（VAT 活跃 2022-09-29；主 PKD 46.65.Z 办公家具批发 —— 登记分类与实际电子品类不符）+ spacetronik.pl 联系页（店主 NIP 6981681757 / REGON 300138031 = 同一老板更早的个体户 JDG）',
    url='https://www.bizraport.pl/krs/0000993625/spacetronik-spolka-z-ograniczona-odpowiedzialnoscia',
    number='KRS 0000993625 · NIP 6981862105 · REGON 523197029（旧个体户 NIP 6981681757）', status='Aktywna（VAT 活跃；KRZ 无记录；最近登记 2025-06-04）', incorporated='2022-09-23（sp. z o.o.；个体户 ≈2005 起，REGON 3001 段）', company_type='Spółka z o.o.（股本 50,000 zł，一人持股）',
    sic=['PKD 46.65.Z（登记）；实际：消费 / 安装电子自有品牌 Spacetronik（电视支架、天线、网络 / PoE 交换机、智能家居）电商 + 批发'],
    address='ul. Wiśniowa 36, 64-000 Kościan（波兹南以南）', accounts='KRS 财报：营收 ≈29.7 mln zł（≈$7.4M）、资产 22.3 mln zł（年度未标，取最近一期）', accounts_due='PL：年报 7 月前报 KRS → 7 月复盘',
    size_band='中小型（估 30–80 人；营收 ≈$7M）',
    officers=['Mikołaj Adam Tomaszewski — Prezes Zarządu 兼唯一股东（1,000 股）= 老板 = 签单人'], psc='Mikołaj Adam Tomaszewski 100%', charges='无（KRZ 无记录）', prev_names=['（个体户 Spacetronik Mikołaj Tomaszewski，NIP 6981681757）'],
    lines=['**一人持股、年营收 ≈3,000 万 zł 的自有品牌电商（Spacetronik 标，研究档记「洪瑞 工商 switch 自己 logo」）= OEM 品牌商序列第一位，且现货源是深圳同类** → **OEM 30% 一对一替代**：按 spacetronik.pl 在售 PoE / 工商交换机型号列对照（8/16/24 口 PoE、工业 DIN），贴 Spacetronik 标 + 波兰语包装；MOQ 1 箱起、量大按 20 尺柜谈',
           '老板 Mikołaj Tomaszewski 既是唯一股东又是总裁 → 没有采购部门绕路；17 封群发无回 = 群发不对路 → 第二封直接写他本人（英文），附对照表',
           '2022 才从个体户改制 + 资产 2,230 万 zł = 在扩张期，现金充裕 → 可谈 T/T 30/70；复盘 2027-07 看 2026 年报'],
    notes='建议升 A 候选（证据：自有品牌 + 深圳货源 + 老板即签单人 + 营收 ≈$7M）；Simon 定级优先。')
put('SB-156', key='pl', batch=B, name='Cyberteam Sp. z o.o.（cyberteam.pl；Zamość, lubelskie）', iso='PL', fetched=F,
    source='PL · 1 次检索：rejestr.io（KRS 0000285290；NIP 9222908443；REGON 060265810；2007-07-24 登记；股本 200 tys. zł；Prezes Tomasz Bartłomiej Nowak 2007 起；董事会多人时各自单独代表）+ bizraport（营收 23.5 mln zł / 资产 8.2 mln zł；prokurent Mirosława Ziemian）+ infoveriti（Nowak 1975 生）+ kompass（Wiceprezes Radosław Marcin Skwarek）+ cyberteam.pl 联系页（Strefowa 8）+ D&B（行业含通信设备制造）+ nowaktechnologie.pl（关联「Nowak Technologie」）',
    url='https://rejestr.io/krs/285290/cyberteam',
    number='KRS 0000285290 · NIP 9222908443 · REGON 060265810', status='Aktywna（VAT 活跃）', incorporated='2007-07-24', company_type='Spółka z o.o.（股本 200,000 zł）',
    sic=['网络 / 光纤 / 媒体转换器 自有品牌 Cyberteam + 电子元件批发与制造（PKD 多项含通信设备制造）；经济特区地址'],
    address='ul. Strefowa 8, 22-400 Zamość（另记 Kalinowice 157）', accounts='KRS 财报：营收 ≈23.5 mln zł（≈$5.9M）、资产 8.2 mln zł', accounts_due='7 月复盘',
    size_band='中小型（估 20–50 人）',
    officers=['Tomasz Bartłomiej Nowak — Prezes Zarządu / 股东（2007 起；1975 生；研究档 KP t.b.nowak@）= 老板 = 联系人', 'Radosław Marcin Skwarek — Wiceprezes Zarządu（kompass）', 'Mirosława Ziemian — Prokurent（商务代理）', 'Monika Patron — 研究档 KP（职务待核）'], psc='Tomasz Nowak（推定主要股东）', charges='', prev_names=[],
    lines=['**研究档 KP Tomasz Nowak 就是总裁兼股东 → 信已到拍板人**；自有品牌 MC / 光纤产品（研究档「MC 自己 logo」）+ 营收 ≈2,350 万 zł = 有规模的 OEM 品牌商 → **OEM 30%：Cyberteam 标 MC + 8/16 口 PoE + 工业 DIN**',
           '2007 年公司、股本 20 万 zł、经济特区厂址 = 有自己的组装 / 制造 → 他们可能要「半成品 / 裸板 + 自己壳」—— 这我们不做，只给整机贴标；17 封无回 → 第二封换成 Tomasz 一句话 + 对照表',
           '复盘 2027-07 看 2026 年报；关联公司 Nowak Technologie 若回信算同一线'],
    notes='')
put('SB-177', key='pl', batch=B, name='Eltcrac System Sp. z o.o.（EC System；ecsystem.pl / sklep-ecsystem.pl；Kraków）', iso='PL', fetched=F,
    source='PL · 1 次检索：rejestr.io（KRS 0000181283；NIP 6792784999；REGON 356766841；Prezes Mirosław Gabzdyl；股本 50 tys. zł）+ sklep-ecsystem.pl 规章（克拉克夫 Śródmieście 法院 XI 处；三家网店 sklep-ecsystem.pl / knivesfamilia.pl / gards.pl 同一主体）+ ecsystem.pl（集成商：CCTV / 门禁 / 报警 / 可视对讲；站点 dsdi.pl、audyt-ecsystem.pl；电商英文客服 Daniel Ochman；秘书 Joanna Mrozowska）+ alarmy.org（esklep@ / handel@ / biuro@）',
    url='https://rejestr.io/krs/181283/eltcrac-system',
    number='KRS 0000181283 · NIP 6792784999 · REGON 356766841', status='Aktywna', incorporated='≈2003（KRS 18 万段；REGON 3567 段）', company_type='Spółka z o.o.（股本 50,000 zł）',
    sic=['安防系统集成（CCTV / 门禁 / 报警 / 对讲）+ 安防电商 sklep-ecsystem.pl（Hasivo 商业 PoE 在售）+ 刀具 / 园艺网店（knivesfamilia / gards）'],
    address='ul. Ruciana 3, 30-803 Kraków（+48 12 292 48 61）', accounts='未取', accounts_due='7 月复盘',
    size_band='小型（估 10–25 人）',
    officers=['Mirosław Gabzdyl — Prezes Zarządu = 老板', 'Daniel Ochman — 电商 / 英文客服（研究档 KP esklep@ 对应人）', 'Joanna Mrozowska — 秘书处'], psc='Mirosław Gabzdyl（推定）', charges='', prev_names=[],
    lines=['**克拉克夫安防集成商 + 自营网店（卖 Hasivo 等深圳 PoE）** → 不是品牌商，是渠道 → **分销 20%**：STC-028GP / STC-228GP / STC-2224GP 对标 Hasivo 同口数报价，MOQ 1 箱',
           '研究档 KP 是网店信箱（esklep@）→ 换写 handel@（批发口）抬头 Daniel Ochman（会英文）抄 Prezes Gabzdyl；19 封无回 → 第二封只给价格对照',
           '同主体兼营刀具 / 园艺网店 = 电商为主、安防集成为辅 → 量小、价格敏感；100% 预付'],
    notes='')
put('SB-250', key='pl', batch=B, name='PF Electronic Sp. z o.o.（pf-electronic.pl；Gliwice，原 Katowice）', iso='PL', fetched=F,
    source='PL · 1 次检索：rejestr.io（KRS 0000046753；NIP 6342396659；REGON 276904785；2001-10-15 登记；股本 127.5 tys. zł；Prezes Jacek Andrzej Nędza 与 Wiceprezes Dariusz Przemysław Piwowar 均 2005-09-06 起；各自单独代表；营收 9.3 mln zł；行业：批发为主 + 机器维修安装 + 电子制造 + 电信 + IT）+ pf-electronic.pl o-firmie / kontakt（Konarskiego 18C Gliwice；info@）+ krs-online（2000 起做工业自动化技术咨询 / 服务；旧址 Katowice Bednorza 2a-6）+ elektroonline（dariusz.piwowar@）',
    url='https://rejestr.io/krs/46753/pf-electronic',
    number='KRS 0000046753 · NIP 6342396659 · REGON 276904785', status='Aktywna（VAT 活跃）', incorporated='2001-10-15（业务 2000 起）', company_type='Spółka z o.o.（股本 127,500 zł）',
    sic=['工业自动化元器件批发 + 维修 / 安装服务 + 网店 sklep.pf-electronic.pl（PLC / 变频 / 工业网络）'],
    address='ul. Stanisława Konarskiego 18C, 44-100 Gliwice（+48 32 256 25 33；旧址 Katowice Bednorza 2a-6）', accounts='KRS 财报：营收 ≈9.3 mln zł（≈$2.3M）', accounts_due='7 月复盘',
    size_band='小型（估 10–25 人）',
    officers=['Jacek Andrzej Nędza — Prezes Zarządu（2005-09 起）= 老板之一', 'Dariusz Przemysław Piwowar — Wiceprezes Zarządu（2005-09 起；研究档 KP dariusz.piwowar@）= 老板之一 = 联系人', 'Ireneusz Marczyk / Adam Goździcki — 决策人（krs-online 历史记录）'], psc='Nędza + Piwowar（推定两人持股）', charges='', prev_names=[],
    lines=['**研究档 KP Dariusz Piwowar 是副总裁 / 合伙人 → 信已到拍板层**；公司 = 西里西亚工业自动化分销 + 服务商（PLC / 变频 / 工业网络），25 年、营收 ≈930 万 zł → **工业 DIN 线分销 20%**：STI-054GP / STI-154GP / STI-288DGGPM 配 PLC 柜，1 台样机付费试',
           '打开 1 次无回 → 第二封只写工业场景（-40~75℃、DIN、冗余供电、ERPS 环网）不写 CCTV；他们客户是工厂维保 = 复购型',
           '复盘 2027-07 看 2026 年报'],
    notes='')
print('PL 4 ok')
