#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 104 批（T29-U97，公司底数第二十二轮 · B 档「自有 logo + 打开」三国 24 户：US 10 / TR 10 / DE 4）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=104 行）。
结构同 batch103_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 OEM 30% 目标 3（SB-209 DENWA 自有 IP 话机 / 交换机贴标 / SB-810 ENS Security 自有贴标厂 / SB-981 L-com 自有 PoE 交换机线）+ 可谈贴标 3（SB-659 ENTPA 自有 Entcam 标 / SB-658 Ekingen 自营多标 + Wi-Tek 分销 / SB-1127 Lin Haw 进口商）；
贴标 低中 1（SB-775 Patton 同行制造商）；贴标 small 1（SB-1032 Foppex 塞浦路斯）；
分销 20% 大户 / 渠道 3（SB-796 EDS Elektronik Destek 制造 + 独家分销 ≈60 人 / SB-888 STORDIS 开放网络 VAD = STH 高速线渠道 / SB-658 同上）；分销 20% 一般 3（SB-673 NODAC 拉美渠道 / SB-648 A Telekomünikasyon 对讲分销 / SB-681 SER Rack 机柜捆绑）；
分销 20% 低概率 2（SB-974 b-plus 实验室线 / SB-854 NetCat 采购型 + 翻新半同行）；集成商 25% small 6（SB-643 Arby / SB-645 ART / SB-656 Dijital Bina 未坐实 / SB-666 MaviAlarm / SB-690 Troyy 安卡拉 / SB-891 Tech-Point）；
一页纸后不动 2（SB-835 FiberOptic Supply / SB-682 Server Blink）；不动 1（SB-473 INTEPO 未坐实 + IP68 / 国防守界）。
坐实 13 / 部分坐实 9（SB-810 NY 号 / SB-1032 HE 号 / SB-1127 BC 号 / SB-835 CO 号 / SB-682 KY 号 / SB-645 法定形式 / SB-648 法定形式 / SB-643 MERSİS / SB-854 HRB）/ 未坐实 2（SB-473 / SB-656）；
KP 坐实 = 老板 / GF / 总经理 / 产品经理本人 11（SB-209 Juan Jose Michel PM / SB-775 Bobby Patton / SB-810 Kevin Zhou / SB-981 Steve Smith PM / SB-835 Bryan Hogan / SB-673 Oscar Cortes / SB-682 Muhammad Amir / SB-666 Aziz Vasıf Durmaz / SB-891 Cedric Krämer / SB-974 Alexander Noack / SB-854 Jörg Ridder CEO / SB-888 Waldemar Scheck）；
国别 / 城市更正 3（SB-1032 → 塞浦路斯 country_fix / SB-1127 → 加拿大 country_fix / SB-690 安卡拉非伊斯坦布尔）；法定名更正 / 补全 9（SB-209 DENWA TECHNOLOGY CORP / SB-981 L-com, LLC / SB-796 Destek Elektronik = EDS Elektronik Destek San. ve Tic. Ltd. Şti. / SB-658 / SB-659 / SB-666 / SB-681 / SB-690 / SB-891 Tech-Point GmbH 前身 Hansebau Krämer）；
守界 4（SB-473 国防 + IP68 / SB-854 国防供货不提 / SB-888 国防细分不提 / SB-974 车载以太网不对口）；
升 A 候选 3（SB-209 / SB-810 / SB-981，回信即 A；次候选 SB-658 / SB-659 / SB-1127 / SB-796 / SB-888）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 104 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- US 10 ----------
    'SB-209': [{'kp_match': 'juanjomichel@', 'name': 'Juan Jose Michel', 'role': 'Product Manager = 收件人本人 / 选型人' + TAG},
               {'facts': {'legal_name': 'DENWA TECHNOLOGY CORP（FL Sunbiz P11000054719；另 DENWAIP TECH LLC L21000046981）', 'founded': '2002（GlobalThink 起源）；FL 登记 2011' + TAG,
                          'other': '第 104 批：Miami / Pembroke Pines FL 统一通信 / IP 话机品牌商（自有 Denwa 标话机、网关、交换机，美 / 阿根廷 / 拉美渠道）→ **贴标 OEM 30% 目标，B BIG，加厚一次；升 A 候选**；11 次无回复 → 二次触达换切口' + TAG}}],
    'SB-775': [{'kp_match': 'jenn@patton.com', 'name': 'Jennefer Staub', 'role': 'Account Manager（销售侧，非采购；改投产品 / 采购）' + TAG},
               {'add_kp': {'name': 'Robert R. (Bobby) Patton', 'role': 'President & CEO（2009 起；共同创办人）= 拍板人' + TAG, 'email': '', 'source': 'https://www.patton.com/company/'}},
               {'facts': {'legal_name': 'Patton Electronics Co.（Maryland Corporation；SAM UEI CETFWF46TQ69）', 'founded': '1984' + TAG,
                          'other': '第 104 批：Gaithersburg MD 网络 / 通信设备制造商（VoIP 网关、以太网延长、工业交换机自有线）→ **同行制造商，贴标 OEM 30% 低中概率；一页纸**（补位其没有的 L2+ PoE 规格）' + TAG}}],
    'SB-810': [{'kp_match': 'marcela.g@', 'name': 'Marcela Garza', 'role': '分部销售 / 采购（职务未核；经其转产品部）' + TAG},
               {'add_kp': {'name': 'Kevin Zhou', 'role': 'Founder & CEO（华裔；2000 年 College Point NY 起家）= 拍板人' + TAG, 'email': '', 'source': 'https://www.enssecurity.com/about-us'}},
               {'facts': {'legal_name': 'ENS Security（原 EasternCCTV；NY 实体法定名 / DOS 号未取 → 部分坐实）', 'founded': '2000' + TAG,
                          'other': '第 104 批：Plainview NY 安防批发商 + 自有贴标厂（11 个分部，自有 ENS 标 NVR / 摄像机 / PoE 交换机）→ **贴标 OEM 30% 目标，B BIG，加厚一次；升 A 候选**；15 次无回复 → 二次触达换切口；中文直联由 Simon 定（默认否）' + TAG}}],
    'SB-981': [{'kp_match': 'ssmith@l-com.com', 'name': 'Steve Smith', 'role': 'Product Manager = 收件人本人 / 选型对口' + TAG},
               {'facts': {'legal_name': 'L-com, LLC（MA；母体 Infinite Electronics International, Inc.，UEI NYEMFJ7MMJB5 · CAGE 43321）', 'founded': '1983-01-02（1982 创立）' + TAG,
                          'other': '第 104 批：North Andover MA 连接产品品牌商（自有 L-com 标 PoE 交换机 / 注入器线，PE 控股 Infinite Electronics 集团）→ **贴标 OEM 30% 目标，B BIG，加厚一次；升 A 候选**' + TAG}}],
    'SB-1032': [{'country_fix': '塞浦路斯'},
                {'facts': {'legal_name': 'Foppex Ltd.（塞浦路斯 Private Limited；HE 号未取 → 部分坐实；Akçaba Communications 股东）', 'founded': '2010-04' + TAG,
                           'other': '第 104 批：尼科西亚 Strovolos（研究档「美国」误 → country_fix 塞浦路斯；站内「Melbourne FL」为模板占位地址）电信 / 网络产品小分销商 → **贴标 small / 分销 20%；一页纸**；发信窗口 Thu 12–14 EET；稿内 UKCA 不适用（CE / RoHS）' + TAG}}],
    'SB-1127': [{'country_fix': '加拿大'},
                {'facts': {'legal_name': 'Lin Haw International Company Ltd（BC 公司；注册号未取 → 部分坐实）', 'founded': '1986' + TAG,
                           'other': '第 104 批：本拿比 Burnaby BC（研究档归美国误 → country_fix 加拿大）网络 / 电源产品进口分销商（自有网店 linhawstore；进口 PLANET 等台系品牌）→ **分销 20% / 可谈贴标；加厚一次；升 A 次候选**；发信窗口 Wed 08–10 PT' + TAG}}],
    'SB-835': [{'add_kp': {'name': 'Bryan Hogan', 'role': 'Owner / President（2001 起）= 拍板人 / 收件人（经 sales@）' + TAG, 'email': '', 'source': 'https://www.bbb.org/us/co/denver/profile/fiber-optics/fiberoptic-supply-1296-14001062'}},
               {'facts': {'legal_name': 'FiberOptic Supply（CO Corporation；SoS 号未取 → 部分坐实；勿与 Fiber Optic Supply, Inc. fosupply.com 混淆）', 'founded': '1997-04（BBB 登记 1998-04-02）' + TAG,
                          'other': '第 104 批：Denver CO 通信级光纤产品分销商（交换机为边角配套）→ **分销 20% small；一页纸后不动**' + TAG}}],
    'SB-673': [{'add_kp': {'name': 'Oscar Cortes', 'role': 'President / Owner（Sunbiz 在册）= 拍板人 / 收件人' + TAG, 'email': '', 'source': 'https://search.sunbiz.org/ P05000037533'}},
               {'facts': {'legal_name': 'NODAC TECHNOLOGY, INC.（FL Sunbiz P05000037533；FEI 20-2538531；Active）', 'founded': '2005-03-10（业务 2001 起）' + TAG,
                          'other': '第 104 批：Doral / Miami FL + Pompano Beach 安防与网络产品分销商（拉美出口渠道、价格敏感）→ **分销 20%；一页纸**' + TAG}}],
    'SB-682': [{'add_kp': {'name': 'Muhammad Amir', 'role': 'Owner（KY LLC）= 收件人' + TAG, 'email': '', 'source': 'https://serverblink.com/about'}},
               {'facts': {'legal_name': 'Server Blink LLC（KY；SoS 号未取 → 部分坐实；登记地址为邮箱套房 PMB 5001）', 'founded': '2022' + TAG,
                          'other': '第 104 批：Louisville KY IT 硬件网店（PC / 服务器配件 / 网络设备转售）→ **采购型 small；一页纸后不动**' + TAG}}],
    'SB-473': [{'kp_match': 'mkanarellis@', 'name': 'Michael Kanarellis', 'role': '研究档 KP（职务未核；INTEPO 转型后不再对口）' + TAG},
               {'facts': {'legal_name': 'BTU Research / INTEPO（未坐实：1 次检索未命中登记）', 'founded': '未取' + TAG,
                          'other': '第 104 批：现以「INTEPO Sovereign Infrastructure」定位（AI 推理边缘基础设施、IP68 / 国防线守界）→ **不动**；未坐实不补查' + TAG}}],
    # ---------- TR 10 ----------
    'SB-643': {'facts': {'legal_name': 'Arby Bilgisayar San. Tic. Ltd. Şti.（İstanbul Maltepe；MERSİS 未取 → 部分坐实）', 'founded': '2004' + TAG,
                         'other': '第 104 批：Maltepe 企业 IT 维护合约 / IT 咨询 / 网络安全 + IP 摄像机系统（MSP 型，11–50 人）→ **集成商 25% small；一页纸后不动**；收件人 bilgi@ 点名 satın alma / teknik müdür' + TAG}},
    'SB-645': {'facts': {'legal_name': 'ART Haberleşme ve Güvenlik Sistemleri（Tuzla；Karel 授权经销与服务；法定形式 / MERSİS 未取 → 部分坐实；勿与 Arter Haberleşme Kartal 混淆）', 'founded': '未取' + TAG,
                         'other': '第 104 批：Tuzla Karel PBX / IP 交换机经销小店（云 PBX、MPLS、对讲、安防）→ **集成商 25% small；一页纸后不动**' + TAG}},
    'SB-648': {'facts': {'legal_name': 'A Telekomünikasyon（Şişli Perpa A Blok Kat 8 No:827-829；法定形式 / MERSİS 未取 → 部分坐实）', 'founded': '2002' + TAG,
                         'other': '第 104 批：Perpa 弱电产品分销商（Siemens / Panasonic / Karel PBX；Hikvision 对讲系统土耳其分销商；Hikvision PoE 在售）→ **分销 20%（对讲配套 PoE 第二线）；一页纸**' + TAG}},
    'SB-656': {'facts': {'legal_name': 'Dijital Bina（dijitalbina.com；Schneider EcoXpert 伙伴；法定名 / 地址 / 登记均未取 → 未坐实）', 'founded': '未取' + TAG,
                         'other': '第 104 批：楼宇自动化 / BMS 集成商（Jade Bird / Esmi 火灾、CCTV）→ **集成商 25% small；一页纸后不动**；未坐实不补查' + TAG}},
    'SB-658': {'facts': {'legal_name': 'Ekingen Elektronik Paz. İth. İhr. San. ve Tic. Ltd. Şti.（İstanbul Bağcılar Mahmutbey；MERSİS 未取）', 'founded': '1985' + TAG,
                         'other': '第 104 批：安防 / 电子批发进出口商（Uniview 官方分销 + Wi-Tek 土耳其分销；Ajax / Ezviz / GST / Edwards；自营品牌 GENBAYİ B2B / DIGILINE / WESTA / DECON / LEXENCE / FUJITRON；多门店；43–200 人；第三方 $5.8M）→ **分销 20% + 可谈贴标（DIGILINE / WESTA 标），B BIG，加厚一次；升 A 次候选**；收件人 info@ 点名 satın alma müdürü；稿内不点 Wi-Tek 名' + TAG}},
    'SB-659': {'facts': {'legal_name': 'ENTPA Elektronik Cihazlar Ticaret Pazarlama ve Turizm A.Ş.（İstanbul Ümraniye Y. Dudullu OSB 1. Cad. No:23；ENTES Elektronik 股东创立；MERSİS 未取）', 'founded': '2003' + TAG,
                         'other': '第 104 批：Hanwha Vision 官方分销 + Honeywell / Sunell + **自有品牌 Entcam CCTV**，背靠 ENTES 制造集团（1980 起，出口 50 国）→ **贴标 OEM 30% 可谈（Entcam 标 PoE）+ 分销 20%，B BIG，加厚一次；升 A 候选（回信即 A）**；收件人 etekyildiz@ 点名 + 抄 satis@' + TAG}},
    'SB-666': [{'add_kp': {'name': 'Aziz Vasıf Durmaz', 'role': 'Yetkili / Genel Müdür（makinaturkiye 在册负责人）= 收件人' + TAG, 'email': '', 'source': 'https://www.makinaturkiye.com/firma/mavi-alarm-kamera-ve-guvenlik-teknolojileri-tic-ltd-sti'}},
               {'facts': {'legal_name': 'MaviAlarm Kamera ve Güvenlik Teknolojileri Tic. Ltd. Şti.（İstanbul Kartal Yakacık Çarşı Mah. Mülayim Sok. No:55；MERSİS 未取）', 'founded': '2010' + TAG,
                          'other': '第 104 批：Kartal 电子安防安装商 / 多品牌经销站（hikvisiontr.net / dahua-tr.com；11–50 人）→ **集成商 25% small；一页纸**' + TAG}}],
    'SB-681': {'facts': {'legal_name': 'SER Rack Kabin Teknoloji ve Bilişim Sistemleri San. Tic. Ltd. Şti.（İstanbul Sancaktepe Emek Mah. Ordu Cad. Arzu Sok. No:46；Perpa 销售处 A Blok Kat 11 No:1469；LANDE 家族；MERSİS 未取）', 'founded': '2013' + TAG,
                         'other': '第 104 批：19" 机柜 / 数据中心机柜制造销售商（本土制造；铜缆 / 光纤 / 有源设备配套；1–10 人）→ **分销 20% small / 可谈 SER 标捆绑；一页纸**；收件人 satis@ 点名 satış müdürü' + TAG}},
    'SB-690': {'facts': {'legal_name': 'Troyy Bilişim Geçiş Kontrol Sistemleri Elektronik Güvenlik San. ve Tic. Ltd. Şti.（Troyy Kontrol；MERSİS 0859063031500011 · Vergi No 8590630315）', 'founded': '2016' + TAG,
                         'other': '第 104 批：**安卡拉 İvedik OSB（非伊斯坦布尔）** 门禁 / 考勤 PDKS 软硬件开发商与集成商（自研 Smek PDKS / Access Nova 面板、闸机、道闸；n11 店 Msec）→ **集成商 25% small / 可谈 Troyy 标小批量；一页纸**；收件人 info@ 点名 teknik müdür' + TAG}},
    'SB-796': {'facts': {'legal_name': 'EDS Elektronik Destek San. ve Tic. Ltd. Şti.（品牌站 Destek Elektronik；İstanbul Sancaktepe Meclis Mah. Teraziler Cad. Hayran Sok. No:4；MERSİS 未取；品牌名单与 Hanwha 名录完全一致 → 推定同一主体）', 'founded': '1990-02' + TAG,
                         'other': '第 104 批：安防电子制造（火灾 / 入侵 / 门禁 / 环境监控 / 电力电子，5,000 m² 工厂）+ Hanwha Vision / FLIR / Aritech / Texecom / Paxton / Phihong 等土耳其独家分销，出口 35+ 国，≈60 人 → **分销 20%，B BIG，可谈 EDS 标，加厚一次；升 A 次候选**；收件人 pazarlama@eds.com.tr 点名 ürün müdürü' + TAG}},
    # ---------- DE 4 ----------
    'SB-891': [{'add_kp': {'name': 'Cedric Krämer', 'role': 'Geschäftsführer & Gründer（Walsrode HRB 211027 在册）= 收件人（经 info@）' + TAG, 'email': '', 'source': 'https://www.northdata.com/Tech-Point%20GmbH,%20Stuhr/Amtsgericht%20Walsrode%20HRB%20211027'}},
               {'add_kp': {'name': 'Jussef Hussein', 'role': 'Geschäftsführung（官网团队页）' + TAG, 'email': '', 'source': 'https://www.techpoint-gmbh.de/ueber-uns/'}},
               {'facts': {'legal_name': 'Tech-Point GmbH（Amtsgericht Walsrode HRB 211027；Stuhr；股本 €25,000；前身 Hansebau Krämer，2022 更名；勿与 TechPoint GmbH Krefeld / TecPoint GmbH Wolfratshausen 混淆）', 'founded': '≈2022（更名登记）' + TAG,
                          'other': '第 104 批：零售 / 数字标牌技术系统全国现场服务商（规划、安装、维护、维修）→ **集成商 25% small；首触一页纸后不动**' + TAG}}],
    'SB-974': [{'add_kp': {'name': 'Alexander Noack', 'role': 'Geschäftsführer b-plus technologies GmbH（HRB 5261；ADAS 测试工具实体）= 对口实体负责人' + TAG, 'email': '', 'source': 'https://www.b-plus.com/de/impressum'}},
               {'add_kp': {'name': 'Michael Sieg', 'role': 'Geschäftsführer b-plus GmbH（集团母公司 HRB 1753；2005 年接任）= 拍板人' + TAG, 'email': '', 'source': 'https://www.b-plus.com/de/impressum'}},
               {'facts': {'legal_name': 'b-plus GmbH（Amtsgericht Deggendorf HRB 1753；股本 €62,000）+ b-plus technologies GmbH（HRB 5261）+ b-plus automotive GmbH（HRB 4269）+ b-plus mobile control GmbH', 'founded': '1996-07-17（母公司）' + TAG,
                          'other': '第 104 批：Deggendorf 自动驾驶 / ADAS 开发工具集团（数据记录仪、车载 10G/25G 以太网；automotive ≈70 人）→ 车载以太网不对口，只有实验室 / 测试台汇聚一线 → **采购型 20% 低概率；按 Simon「着重跟一下」做一次定向一页纸（STC-110XGE / STI-0240GE / STH-2C24XF-HSI），之后不动**' + TAG}}],
    'SB-854': [{'kp_match': 'joerg.ridder@', 'name': 'Jörg Ridder', 'role': 'CEO / Geschäftsführer = 收件人本人 / 拍板人' + TAG},
               {'facts': {'legal_name': 'NetCat SYSTEMS GmbH（Kamen NRW Weißdornweg 24；HRB 未取 → 部分坐实；ISO 9001:2015）', 'founded': '2003' + TAG,
                          'other': '第 104 批：IT 采购 / 供应链服务商（Cisco / HP / Lenovo / Ubiquiti 转售、EOL / 翻新硬件买卖、OEM 光模块、项目型供货含国防 — 守界不提）→ **分销 20% 低概率（采购型 + 翻新半同行）；按 Simon「着重跟一下」对 CEO 做一次定向一页纸（标案 Cisco 替代位），之后不动**' + TAG}}],
    'SB-888': [{'kp_match': 'tomasz.sadowski@', 'name': 'Tomasz Sadowski', 'role': 'Technical（研究档）= 技术收件人' + TAG},
               {'kp_match': 'mariusz.szlezak@', 'name': 'Mariusz Ślęzak', 'role': '研究档 KP（职务未核）' + TAG},
               {'add_kp': {'name': 'Waldemar Scheck', 'role': 'Geschäftsführer（单独代表；Stuttgart HRB 724261 在册）= 拍板人（经 info@ 转）' + TAG, 'email': '', 'source': 'https://stordis.com/legal-notice-impressum/'}},
               {'facts': {'legal_name': 'STORDIS GmbH（Amtsgericht Stuttgart HRB 724261；Rübteile 24, 72574 Bad Urach，原 Rosenwiesstr. 17 Stuttgart；股本 €50,000；VAT DE 256406445；英国分公司）', 'founded': '2007-09-18' + TAG,
                          'other': '第 104 批：开放网络 / 白盒交换机增值分销商（600+ 产品；Microtel 10/25/100G 包探针分销；学术 / 媒体 / 安全 / 运营商 / 金融 / 国防细分 — 国防不提）→ **分销 20%，STH 高速线天然渠道，B BIG，加厚一次（STH-2C24XF-HSI / 8C48DX / 32C + STC-448XGGPM）；升 A 次候选**；6 次无回复 → 二次触达换切口' + TAG}}],
}


def apply(d, u):
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if u.get('name') and not k.get('name'):
                    k['name'] = u['name']
                if u.get('name') and k.get('name') and k.get('name') != u['name'] and TAG not in (k.get('role') or ''):
                    k['name'] = u['name']
                if u.get('role') and TAG not in (k.get('role') or ''):
                    k['role'] = u['role']
    if u.get('kp_name'):
        for k in kps:
            if (k.get('name') or '') == u['kp_name'] and TAG not in (k.get('role') or ''):
                k['role'] = u['role']
    if u.get('add_kp') and not any(u['add_kp']['name'] == (k.get('name') or '') for k in kps):
        kps.append(u['add_kp'])
    seen, dedup = set(), []
    for k in kps:
        key = (k.get('name'), k.get('email'), k.get('role') or k.get('title'))
        if key in seen:
            continue
        seen.add(key); dedup.append(k)
    d['kp'] = dedup
    cf = d.get('company_facts') or {}
    for fk, fv in (u.get('facts') or {}).items():
        if TAG not in str(cf.get(fk, '')) and fv:
            cf[fk] = fv if fk != 'other' or not cf.get('other') else (cf['other'] + '；' + fv)
    d['company_facts'] = cf
    if u.get('country_fix'):
        d['country_fix'] = u['country_fix']


if __name__ == '__main__':
    for code, u in UPD.items():
        p = os.path.join(RESEARCH_DIR, f'{code}.json')
        d = json.load(open(p, encoding='utf-8'))
        for one in (u if isinstance(u, list) else [u]):
            apply(d, one)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(code, 'ok')
