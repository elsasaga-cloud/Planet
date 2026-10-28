# -*- coding: utf-8 -*-
"""第 106 批（T29-U99，2026-10-28）A 档补齐 3 —— 官方登记核实写入 registry。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put, load_all
B = 106
F = '2026-10-28'

put('SA-004', key='de', batch=B, name='Boecek Sec（boecek.de；用户表原值；德国）— 1 次检索未命中该域名的任何公开页面（同名 boeck GmbH Leipheim HRB 15558 / Sicherheitstechnik Bock Berlin / Böck Technik GmbH 均 ≠）→ 未坐实；A 级依据为 Simon 一手证据（买过 5 电口样品、要工业电源、问 2 款 2.5G 价、对机架式工业网管机有兴趣）', iso='DE', fetched=F,
    source='DE · 1 次检索未命中（boeck-technology.de / sicherheitstechnik-bock.de / cboeck.de / boeck-technik.de 均为同名他家，不采）→ 未坐实，按规程不补查；主体信息改由 Simon 侧样品订单的发票抬头 / 收货地址补',
    url='', number='未取', status='未知（域名无公开页）', incorporated='未取', company_type='未知',
    sic=['安防（用户表）'], address='未取（德国）', accounts='—', accounts_due='—', size_band='未知',
    officers=['（未具名）— 用户表联系人（样品买家）'], psc='未取', charges='', prev_names=[],
    lines=['**A 级维持（有样品订单 + 具体型号问价）；主体未坐实 → 下一封跟进顺手要一次「公司全称 + 送货地址 + 增值税号」（报价单需要，不突兀）**',
           '**Simon 可做**：把该样品订单的发票抬头 / 收货地址 / VAT 号给我，底数当场补齐；2.5G 两款 + 机架式工业网管机（STI-288DGGPM / STI-488DGGPM）继续按 A 跟'],
    notes='A 维持；未坐实（域名无公开页）；Simon 侧发票抬头可补。')
put('SA-066', key='other', batch=B, name='CCS（ccs-msk.ru；莫斯科 107589 ул. Красноярская д.1 корп.1）— 十余年的 IT / 电信设备分销商：MICROSENS（德国工业交换机 / FTTO 微型交换机）与 LENOVO 官方合作伙伴、日本 SUMITOMO 分销商；在售 Brocade、LR-LINK、光模块 / AOC / DAC / SAS·Infiniband 线缆、SpaceWire；法定名（ООО 名称 / ИНН）官网未列、1 次检索未命中（同名 ООО «ССС» ИНН 7708393591 / 7814529565、ООО «Сложные облачные системы» ccs.msk.ru ИНН 7713417625 均 ≠）→ 部分坐实；2026 最新回复（A）', iso='RU', fetched=F,
    source='RU · 1 次检索：官网 О компании（официальный партнёр MICROSENS и LENOVO, дистрибьютор SUMITOMO；более чем десятилетняя история；активное / пассивное сетевое оборудование, промышленный Ethernet, FTTO / Smart Office, кабели）+ Контакты（107589 Москва ул. Красноярская д.1 корп.1；(495) 926-86-95；sales@ccs-msk.ru）+ Каталог（BROCADE / Lenovo / MICROSENS / LR-LINK / SUMITOMO / 100G QSFP28 / трансиверы）+ Zoon（Торговая компания CCS；Пн-пт 10–18）；Контур.Фокус / rusprofile 同名 ООО «ССС» 为他家，不采',
    url='https://www.ccs-msk.ru/about',
    number='ИНН / ОГРН 未取（官网未列法定名）', status='Active（官网在线；2026 有回复）', incorporated='未取（自述 10+ 年）', company_type='ООО（推定）',
    sic=['IT / 电信设备分销（工业以太网 Microsens、服务器 Lenovo、光纤 Sumitomo、光模块 / 线缆；自有 / 白牌 SFP 目录）'],
    address='107589, г. Москва, ул. Красноярская д.1, корп. 1', accounts='—', accounts_due='—', size_band='小型（推定 10–30 人）',
    officers=['（见 Clients 表回复签名）— 收件人 sales@ccs-msk.ru'], psc='未取', charges='', prev_names=[],
    lines=['**卖德系高价工业交换机（Microsens）的分销商 → Saga STI 工业线是天然的「第二价位」：分销 20%，A 维持；加厚（STI-288DGGPM / STI-488DGGPM / STI-0240GE 1:1 对照 Microsens 价位；FTTO 场景用 STC-028GP / STI-054GP）**；稿内不点名 Microsens',
           '**俄罗斯收款路径待核（Simon 定：第三国 / 人民币 / 代理）**；法定名下一封回信顺手问「реквизиты для счёта」；发信窗口 Thu 10–12 MSK；英文 + 一句俄语引子'],
    notes='A 维持；分销 20%；加厚；部分坐实（官网地址 + 合作资质）；收款路径待核。')
put('SA-069', key='other', batch=B, name='BPTEHNO = ООО «БИЗНЕС ПАРТНЕР»（官网与 2017 行业新闻署名；品牌页另写 ООО «БПТЕХНО»；bptehno.ru；莫斯科）— 面向俄罗斯及独联体的光纤传输系统分销商（视频 / 音频 / 数据 / 电话光端机、KVM 光纤延长、光开关、IPTV 头端、EDFA；代理「Optic」（俄方设计 / 中国制造）、Raycom RF960 / RF970 光纤周界入侵探测、杭州华泰等；提供方案设计与到门交付）；ИНН 未取 → 部分坐实；用户表「可能是公司之前的合作商」，WA 在线，22 次跟进 5 次回复（A）', iso='RU', fetched=F,
    source='RU · 1 次检索：官网首页（BPTEHNO поставляет на российский рынок и стран СНГ продукцию ведущих мировых производителей оптоволоконных систем；+7 926 527-42-98；info@bptehno.ru）+ Бренды 页（В России компанию представляет дистребьютер ООО «БПТЕХНО»）+ Системы безопасности 页（ООО «БИЗНЕС ПАРТНЕР» … RF-960 (www.bptehno.ru)）+ depo-magazine 2017-01-26 新闻（Оптоволоконные системы … от ООО "БИЗНЕС ПАРТНЕР"；Компания BPTehno）+ 产品页（Optic — российская разработка-китайское производство；8 495 740-32-53）',
    url='https://bptehno.ru/',
    number='ИНН / ОГРН 未取', status='Active（官网在线；WA 在线）', incorporated='未取（新闻 2017 已在业）', company_type='ООО（ООО «БИЗНЕС ПАРТНЕР» / ООО «БПТЕХНО»）',
    sic=['光纤传输系统 / 信号处理设备分销（俄罗斯 + 独联体；安防光端机、周界探测、IPTV 头端）；代理中国制造贴俄标产品'],
    address='Москва（具体地址官网未列）', accounts='—', accounts_due='—', size_band='小型（推定 <20 人）',
    officers=['（见 Clients 表联系人）— 收件人 info@bptehno.ru'], psc='未取', charges='', prev_names=[],
    lines=['**已在卖「俄方设计 / 中国制造」贴牌光传输产品 → 贴标 OEM 30% 可谈（BPTEHNO / Optic 标工业 PoE 与光口交换机）+ 分销 20%，A 维持；加厚（STI-144GP / STI-154GP / STI-288DGGPM 光口工业机 + STC-228GP；品类从光端机向 IP / PoE 迁移）**；稿内不点名其代理品牌',
           '**俄罗斯收款路径待核（同 SA-066）**；法定名二选一（ООО «БИЗНЕС ПАРТНЕР» vs «БПТЕХНО»）回信时问 реквизиты；WA 在线可短消息；发信窗口 Thu 10–12 MSK'],
    notes='A 维持；贴标 30% 可谈 + 分销 20%；加厚；部分坐实（法定名二选一）；收款路径待核。')
print('b106 A 3 written')
