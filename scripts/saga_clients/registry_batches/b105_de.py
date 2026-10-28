# -*- coding: utf-8 -*-
"""第 105 批（T29-U98，2026-10-28）DE 3 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 105
F = '2026-10-28'

put('SB-321', key='de', batch=B, name='BWsystems – Hans-Georg Werner（bwsystems.de；柏林 Köpenick）— 个体经营（Einzelunternehmen，无 HRB）：IT 服务 / 软件 / 网络设备 eBay 网店（USt-ID DE137120780）；表内阿里巴巴 RFQ「2+8 千兆商业 PoE」；KP Hans-Georg Werner = 业主本人；表内未跟进', iso='DE', fetched=F,
    source='DE · 1 次检索：官网 AGB（BWsystems – Hans-Georg Werner；Vertreten durch Hans-Georg Werner；Pritstabelstraße 52A 12557 Berlin；ebay@bwsystems.de；USt-ID DE137120780）+ meinestadt 名录（Hans-Georg Werner BW-Systems；Pritstabelstr. 52a；030 65880749；service@bwsystems.de；软件开发 / IT 咨询 / 培训）+ Das Örtliche / Telefonbuch（同址；Software）+ haendlerschutz（Onlineshops；Computer, Tablets & Netzwerk）；个体经营无 HRB',
    url='http://www.bwsystems.de/agb.htm',
    number='Einzelunternehmen（无 HRB）；USt-ID DE137120780', status='Active（名录在线）', incorporated='未取', company_type='个体经营（Hans-Georg Werner）',
    sic=['IT 服务 / 软件 / 网络设备网店（eBay）'],
    address='Pritstabelstraße 52A, 12557 Berlin（Köpenick）', accounts='—', accounts_due='—', size_band='小微（1 人）',
    officers=['Hans-Georg Werner — Inhaber = 研究档 KP = 收件人（service@）'], psc='Hans-Georg Werner', charges='', prev_names=['BW-Systems'],
    lines=['**一人 IT 店，阿里 RFQ 2+8 PoE → 采购型 small，一页纸（直接报 STC-228GP $33 / STC-028GP $28）后不动**',
           '收件人 service@ 直呼 Herr Werner；发信窗口 Thu 12–14 CET'],
    notes='采购型 small；一页纸（报价）后不动；坐实（USt-ID）。')
put('SB-460', key='de', batch=B, name='4G GmbH（4g-gmbh.de；北威州 Sendenhorst；Amtsgericht Münster HRB 15069）— 2014-07-04 以 Westhoff Engineering GmbH 成立、2015 更名 4G GmbH 的电驱动技术开发 / 生产 / 销售公司（股本 €63,000）；GF Michael Heinrich Wilhelm Kleiböhmer（2023-06 起；= 研究档 KP mk@）；表内 Shopify 订单 OM-FBS-22-SLC（光旁路 / 光开关类配件）「珊姐跟进了」→ 已成交零星小单', iso='DE', fetched=F,
    source='DE · 1 次检索：webvalid（4G GmbH Sendenhorst；Handelsregister Münster HRB 15069；Gründung 04.07.2014；Gegenstand Entwicklung, Produktion und Vertrieb von elektrischer Antriebstechnik；2023-06-21 Bestellt zum Geschäftsführer Kleiböhmer, Michael Heinrich Wilhelm, Adelsdorf，einzelvertretungsberechtigt；Geschäftsanschrift Industrieweg 19 48324 Sendenhorst）+ Northdata（4G GmbH / 原 Westhoff Engineering GmbH；HRB 15069；MD Michael Kleiböhmer）+ online-handelsregister（Kapital 63.000 EUR；Gesellschaftsvertrag 2014-07-04；首任 GF Jörg Westhoff）；同名 4G GmbH Würzburg HRB 16332 为他家，不采',
    url='https://www.northdata.com/4G%20GmbH,%20Sendenhorst/Amtsgericht%20M%C3%BCnster%20HRB%2015069',
    number='HRB 15069（Amtsgericht Münster）', status='Active', incorporated='2014-07-04（Westhoff Engineering GmbH）；2015 更名 4G GmbH', company_type='GmbH（私有；股本 €63,000）',
    sic=['电驱动技术开发 / 生产 / 销售（工程型小厂；网络 / 光配件为研发采购）'],
    address='Industrieweg 19, 48324 Sendenhorst（NRW）', accounts='—', accounts_due='—', size_band='小型（推定 5–20 人）',
    officers=['Michael Heinrich Wilhelm Kleiböhmer — Geschäftsführer（2023-06 起，单独代表）= 研究档 KP = 收件人', 'Andre Borgmann — 前 GF（2023-06 卸任）', 'Jörg Westhoff — 创始 GF（2014–2023）'], psc='未取', charges='', prev_names=['Westhoff Engineering GmbH（2014–2015）'],
    lines=['**已成交零星（Shopify 光旁路配件）的工程小厂 → 采购型 small，复购一页纸（研发 / 测试台 PoE 与 10G：STC-228GP / STC-110XGE）后不动**；按成单客户规则只记档监控，不群发',
           '收件人 mk@ 直呼 Herr Kleiböhmer；切口「your earlier order with us」（仅当 S-box / Shopify 记录能证实，否则不提）；发信窗口 Thu 12–14 CET'],
    notes='采购型 small；已成交零星；复购一页纸后不动；HRB 已取。')
put('SB-542', key='de', batch=B, name='LANOPIA GmbH（lanopia.de；巴伐利亚 Altomünster；Amtsgericht München HRB 143448）— 2002-07-05 成立的光纤 / 铜缆网络技术增值分销商（Omnitron Systems DACH 分销商；媒体转换器、交换机、复用器、光模块；站内 poe 247 / switch 233 / industrial 126 / MC 45）；GF Martina Ochmann（2002 起）+ Paul Antony Ochmann（2004 起）；股本 €25,000；表内「MC 工业 FS；卖 Omnitron？可以着重跟一下」；群发 8 次无回复', iso='DE', fetched=F,
    source='DE · 1 次检索：companyhouse.de（LANOPIA GmbH；Euphemiaweg 20 A 85250 Altomünster；HRB 143448 Amtsgericht München；Gegründet 2002；Geschäftsführung Paul Antony Ochmann（2004-09-27 起）/ Martina Ochmann（2002-07-04 起），均 alleinvertretungsberechtigt；VAD 光纤 / 铜缆网络技术）+ unternehmen24（Gründung 05.07.2002；Kapital 25.000 EUR；info@；+49 8254 4869944）+ 官网 Company / Contact / Location（2002 起 VAD；Gewerbepark 23 85250 Altomünster）+ Omnitron 分销名录（LanOpia Germany；DACH；martina.ochmann@lanopia.de）+ D&B（Key Principal Martina Ochmann）',
    url='https://www.companyhouse.de/LANOPIA-GmbH-Altomuenster',
    number='HRB 143448（Amtsgericht München）', status='Active', incorporated='2002-07-05', company_type='GmbH（Ochmann 家族私有；股本 €25,000）',
    sic=['光纤 / 铜缆网络技术增值分销（媒体转换器、交换机、复用器、光模块；Omnitron DACH 分销；接入与传输）'],
    address='Gewerbepark 23, 85250 Altomünster（登记地址 Euphemiaweg 20a）', accounts='—', accounts_due='—', size_band='小微（家族 VAD；推定 <10 人）',
    officers=['Martina Ochmann — Geschäftsführerin（2002 起；Omnitron 名录联系人）= 收件人', 'Paul Antony Ochmann — Geschäftsführer（2004 起）= 拍板人'], psc='Ochmann 家族', charges='', prev_names=[],
    lines=['**MC / 工业 / PoE 三类目齐全的 DACH 小 VAD，Simon「着重跟一下」→ 分销 20%，B BIG，加厚一次**：STI-144GP / STI-154GP / STI-288DGGPM（工业 PoE 光口，配其 Omnitron MC 线卖）+ STC-228GP / STC-2224GP / STC-110XGE；一页纸 + 工业线卡 + 1:1 规格对照；稿内不点名 Omnitron',
           '收件人 martina.ochmann@（公开名录）直呼 Frau Ochmann，抄 info@；8 次群发无回复 → 二次触达换切口「an industrial PoE line next to your media converters」；发信窗口 Thu 12–14 CET；升 A 次候选'],
    notes='分销 20%；B BIG；加厚一次；升 A 次候选；HRB 已取。')
print('b105 DE 3 written')
