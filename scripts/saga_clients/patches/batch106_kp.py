#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 106 批（T29-U99，公司底数第二十四轮 · 五国 B 池收尾 25 户：US 9 / TR 13 + A 档补齐 3；US / TR / DE / GB / PL B 池清空）：把官方 / 准官方登记核出来的「老板 / 法定名 / 成立日」回写研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=106 行）。
结构同 batch105_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 30% 可谈 3（SB-760 Galaxy Security Corporation **加拿大 Markham** 自有品牌 CCTV 批发 → country_fix 加拿大 / SB-808 Deponet Elektronik A.Ş. 1998 Ruijie 最佳 VAD + 卖 Planet + 自有品牌 Nets → 升 A 候选 / SA-069 BPTEHNO 代理贴俄标中国货，A 维持）；
分销 20% / 采购型加厚 4（SB-392 MAKRO SİSTEM DIŞ TİCARET A.Ş. 2023-11-13 i-PRO 土耳其 Premium 分销 → 升 A 次候选 / SB-274 Fiberix İletişim Hizmetleri Ltd. Şti. 加济安泰普 ISP RIPE AS205768 / SA-066 CCS 莫斯科 Microsens 合作伙伴 A 维持 / SB-377 PROVES A.Ş. 2020-02-14 Hanwha SI 加厚 small）；
集成商 / 小店一页纸 8（SB-742 VIZMA TECHNOLOGY, LLC WA 602984088 / SB-252 Platinum CCTV 自有标 + Simon 点名 加厚 small / SB-140 AG Bilgisayar / SB-302 Antalya Turkuaz Ltd. Şti. / SB-374 3S Güvenlik（守界国防不碰）/ SB-388 FH Güvenlik Ltd. Şti. 2025-02-13 / SB-225 CESS Güvenlik / SB-548 Netsys-America, LLC 同行代理）；
采购型 small 一页纸 5（SB-262 Software Effect Enterprises, Inc / SB-293 VIRTUAL PROTECTIVE LLC TX 0802032860 / SB-300 Çamsan Ordu A.Ş. 终端大厂 / SB-413 LTE Elektronik Ltd. Şti. IoT 元器件分销 / SB-662 HSSL Systems Integrator LLC 虚拟办公室目录型）；
不动 5（SB-466 MicroFast 未坐实 + EoC 不做 / SB-477 eminnovate 未坐实 / SB-153 Sinerjik 未坐实 / SB-921 Dimas 未坐实 / SA-004 Boecek 未坐实但 A 维持，Simon 侧发票抬头可补）。
坐实 10（SB-742 / SB-293 / SB-274 / SB-300 / SB-388 / SB-392 / SB-808 + 官网法定名 SB-548 / SB-662 / SB-377 计部分）/ 部分坐实 10 / 未坐实 5（SB-466 / SB-477 / SB-153 / SB-921 / SA-004）；
KP 坐实 = 老板 / CEO / 创始人本人 7（SB-760 Annie Chen / SB-742 Val Zakharov / SB-262 Charles Deling / SB-293 Louis + Jon Byrd / SB-374 Savaş Tulgar / SB-377 Serdar Karasu / SB-662 James Dubois）；国别更正 1（SB-760 美国 → 加拿大）；
法定名补全 9（SB-548 / SB-742 / SB-293 / SB-274 / SB-300 / SB-377 / SB-388 / SB-392 / SB-808 / SA-069 ООО «БИЗНЕС ПАРТНЕР»）；升 A 候选 1（SB-808，回信即 A；次候选 SB-760 / SB-392）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 106 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- US 9 ----------
    'SB-548': {'facts': {'legal_name': 'Netsys-America, LLC（d/b/a netsys-direct.com；MD LLC，SDAT 号未取 → 部分坐实）', 'founded': '未取' + TAG,
                         'other': '第 106 批：Millersville MD；台湾 Netsys 网通产品美 / 加 / 中南美授权代表（Shopify 直销 DSL / G.hn / EoC / PoE 延长器）→ **同行代理，PoE 交换机为相邻缺口：分销 20% small，一页纸后不动**' + TAG}},
    'SB-742': [{'add_kp': {'name': 'Val Zakharov', 'role': '业主 / 注册代理人（WA SoS）= 收件人' + TAG, 'email': '', 'source': 'http://www.datalog.co.uk/browse/detail.php/CompanyNumber/USWA602984088/CompanyName/VIZMA+TECHNOLOGY,+LLC'}},
               {'facts': {'legal_name': 'VIZMA TECHNOLOGY, LLC（d/b/a CCTVROOM / VIZMA / S-VIDIA；WA UBI 602984088；Active）', 'founded': '2010-01-11' + TAG,
                          'other': '第 106 批：Tacoma WA 家族 CCTV 网店 + 安装（2–4 人；用 Utepo 工业 FS）→ **集成商 25% small；一页纸（STI-054GP / STI-144GP 替代工业 FS）一次后不动**；18 次无回复' + TAG}}],
    'SB-760': [{'kp_match': 'annie@galaxysecurity.com', 'name': 'Annie Chen', 'role': 'CEO（2006 起；LinkedIn / 官网署名）= 拍板人 / 收件人本人' + TAG},
               {'kp_match': 'info@galaxysecurity.com', 'name': 'Sven Liang', 'role': 'Branch Manager（研究档）' + TAG},
               {'country_fix': '加拿大'},
               {'facts': {'legal_name': 'Galaxy Security Corporation（Galaxy Security Inc. / Smart Vision Direct；安大略公司号未取 → 部分坐实）', 'founded': '2006' + TAG,
                          'other': '第 106 批：**加拿大安大略 Markham（研究档误记美国 → country_fix）**；北美 CCTV 自有品牌商 / 批发（面向 dealers & installers；Uniview Canada 合作伙伴；25–50 人；Markham + Mississauga）→ **贴标 OEM 30% 可谈（Galaxy 标 PoE 交换机配其摄像机套装）+ 分销 20%，B BIG，加厚一次；升 A 次候选**；华裔 CEO → 中文直联 Simon 定（默认否）' + TAG}}],
    'SB-262': [{'kp_match': 'charles@softwareeffect.com', 'name': 'Charles H. Deling', 'role': '业主（2 人公司）= 收件人本人' + TAG},
               {'facts': {'legal_name': 'Software Effect Enterprises, Inc（seei.biz；GA；控制号未取 → 部分坐实）', 'founded': '未取' + TAG,
                          'other': '第 106 批：Newnan GA 2 人网络支持工具站（Red Hat / Nagios / Juniper）→ **采购型 small；一页纸（回 MIB 可提供 + STC-228GP 价）一次后不动**' + TAG}}],
    'SB-293': [{'kp_match': 'jon@virtualprotective.com', 'name': 'Jonathan (Jon) Byrd', 'role': 'Technical Manager（Google Play 开发者联系人）= 收件人' + TAG},
               {'add_kp': {'name': 'Louis Byrd', 'role': 'President / 注册代理人（TX SoS）= 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://opencorporates.com/companies/us_tx/0802032860'}},
               {'facts': {'legal_name': 'VIRTUAL PROTECTIVE LLC（TX SoS 0802032860；In Existence；TX 安保执照 B19488）', 'founded': '2014-07-24' + TAG,
                          'other': '第 106 批：New Braunfels TX 工地 / 物业移动太阳能监控塔租赁 + 远程监控（SPP-2SP；≈8 人）→ **采购型 small；一页纸（塔内小型工业 PoE STI-054GP / STI-144GP）一次后不动**；其 NDAA 口径我方稿内不碰' + TAG}}],
    'SB-466': {'facts': {'legal_name': 'MicroFast Technologies / MRDS Distributers（未坐实：1 次检索仅命中印度 CIN U72900TG2018PTC125645 与英国 06696569 同名他家）', 'founded': '未取' + TAG,
                         'other': '第 106 批：酒店 / 办公 CCTV·PBX·布线方案商自述；阿里询盘 EoC（非 Saga 品类）→ **不动**；未坐实不补查' + TAG}},
    'SB-477': {'facts': {'legal_name': 'eminnovate.com（未坐实：1 次检索仅命中印度浦那 Eminnovate eminnovate.co 同名他家）', 'founded': '未取' + TAG,
                         'other': '第 106 批：业务未知 → **不动**；曾 1 次实质回复，若再回信先问公司全称与业务' + TAG}},
    'SB-252': [{'kp_match': 'paul@platinumcctv.com', 'name': 'Paul Cutrano', 'role': 'Director of Field Operations（2019 起；前 AT&T 技师）= 收件人' + TAG},
               {'add_kp': {'name': 'Scott Davidson', 'role': 'Account Manager（RocketReach）' + TAG, 'email': '', 'source': 'https://rocketreach.co/platinum-cctv-management_b46d69c0fc5c87a1'}},
               {'facts': {'legal_name': 'Platinum CCTV（Warrenville IL；自有品牌 Platinum CCTV™；法定主体名 / IL 号未取 → 部分坐实）', 'founded': '2003（Ez-Toyz.com 网店起家）' + TAG,
                          'other': '第 106 批：商用监控选型 / 安装 / 展厅（≈6 人；自有标）+ Simon「可以尝试多跟进一下」→ **集成商 25% + 小批量贴标 30% 可提，B，加厚一次（small）**；10 次无回复 → 换切口' + TAG}}],
    'SB-662': [{'add_kp': {'name': 'James Dubois', 'role': '业主（域名注册人；HSSL Systems Integrator LLC）= 收件人（info@hssl.us）' + TAG, 'email': '', 'source': 'https://www.scamadviser.com/check-website/hssl.us'}},
               {'facts': {'legal_name': 'HSSL Systems Integrator LLC（d/b/a HSSL Technologies；NY 99 Wall St Suite 553 虚拟办公室 + Irvine CA 邮箱；NY DOS 号未取 → 部分坐实；关联 hssl.ng 尼日利亚 + 英国 Kemp House）', 'founded': '2018' + TAG,
                          'other': '第 106 批：目录型企业 IT 硬件经销 / 报价站（自称 6,000+ 厂商；≈12 人口径）→ **分销 20% 低概率；一页纸一次后不动；成交 100% 前 T/T**' + TAG}}],
    # ---------- TR 13 ----------
    'SB-140': [{'kp_match': 'info@ag-bilgisayar.com', 'name': 'Aycan Çam', 'role': '研究档 KP（用户表）= 收件人' + TAG},
               {'facts': {'legal_name': 'AG Bilgisayar（博德鲁姆 Yokuşbaşı Mah. Külcü Sok. Şeref Konday İşhanı No:29；法定形式 / MERSİS 未取 → 部分坐实）', 'founded': '未取（自述 10+ 年）' + TAG,
                          'other': '第 106 批：度假区小型 IT / 安防 / 门禁 / 闸机安装商（官网 2020 版维护弱）→ **集成商 25% small；一页纸一次后不动**' + TAG}}],
    'SB-153': {'facts': {'legal_name': 'Sinerjik（sinerjik.net；未坐实：1 次检索仅命中词典释义）', 'founded': '未取' + TAG,
                         'other': '第 106 批：ISAF 需求 PoE 分离器（非 Saga 品类）→ **不动**' + TAG}},
    'SB-274': [{'kp_match': 'zafery@', 'name': 'Zafer Yılmaz', 'role': 'RIPE 管理联系人（网络负责人推定）= 收件人' + TAG},
               {'kp_match': 'karasu@', 'name': 'Karasu', 'role': '用户表联系人（抄送）' + TAG},
               {'facts': {'legal_name': 'Fiberix İletişim Hizmetleri Ltd. Şti.（BTK 授权基础设施 / ISP；RIPE LIR tr.fiberixinternet；AS205768；MERSİS 未取）', 'founded': 'AS 2017-06-08（公司约 2017）' + TAG,
                          'other': '第 106 批：加济安泰普地方 FTTH 运营商（1,024 IPv4；TR eyeball #107；在招 10 销售）→ **采购型 20%，B，加厚一次（接入汇聚 STC-228GP / STC-2224GP + 10G 上联 STC-110XGE / STH 25G）**' + TAG}}],
    'SB-300': {'facts': {'legal_name': 'Çamsan Ordu Ağaç Sanayi ve Ticaret A.Ş.（Vergi No 2280750226；安卡拉 YDA Center 总部 + 奥尔杜工厂；YYS 经认证经营者 2024-10-09；董事会副主席 Sedat Aksakallı）', 'founded': '1984（建厂）；2011 分立' + TAG,
                         'other': '第 106 批：MDF / 强化地板大厂（≈780 人）= 终端用户 → **项目 25% 低概率；一页纸（厂区工业环网 STI-288DGGPM / STI-488DGGPM / STI-0240GE）一次后不动**；KP 邮箱前缀 sclcule.o 姓名未核，稿内不猜名' + TAG}},
    'SB-302': [{'kp_match': 'naktar@', 'name': 'Gökhan Naktar', 'role': '研究档 KP（用户表）= 收件人' + TAG},
               {'facts': {'legal_name': 'Antalya Turkuaz Bilişim Teknolojileri Ltd. Şti.（Muratpaşa Altındağ Mah. 166. Sok. Doğan Apt No:24/C；MERSİS 未取 → 部分坐实）', 'founded': '未取（自述 25+ 年）' + TAG,
                          'other': '第 106 批：安防 + 网络双线集成商（11–50 口径；旧址 Teomanpaşa 停用非注销）→ **集成商 25% small；一页纸（STC-228GP / STC-2224GP 配 AI 摄像机项目）**' + TAG}}],
    'SB-374': [{'kp_match': 'savas@3s.com.tr', 'name': 'Savaş Tulgar', 'role': 'Yönetim Kurulu Başkanı（3S Teknoloji Savunma ve Yapı Sanayi Ticaret A.Ş. 设立公告）= 收件人本人' + TAG},
               {'facts': {'legal_name': '3S Güvenlik Sistemleri（3s.com.tr；Sultangazi Esentepe Mah. 2403/1 Sok. No:11）/ 3S Teknoloji Savunma ve Yapı Sanayi Ticaret A.Ş.（股本 5 万 TL；同址；MERSİS 未取 → 部分坐实）', 'founded': 'A.Ş. 11-25 设立（年份未取）' + TAG,
                          'other': '第 106 批：老板本人 ISAF 要工业级交换机 → **集成商 25% small；一页纸（STI 工业线卡 + 价）一次后不动；守界：经营范围含国防，只报民用工业 / 安防场景**；同名 3-S Mühendislik / 3S Teknik ≠' + TAG}}],
    'SB-377': [{'kp_match': 'bilgi@proves.com.tr', 'name': 'Serdar Karasu', 'role': '创始人 / 负责人（ZoomInfo Founder；LinkedIn）= 收件人本人' + TAG},
               {'facts': {'legal_name': 'PROVES BİLGİ TEKNOLOJİLERİ SANAYİ VE TİCARET ANONİM ŞİRKETİ（find.com.tr；Bayraklı 设立 → Bornova → Buca；MERSİS 未取 → 部分坐实）', 'founded': '2020-02-14' + TAG,
                          'other': '第 106 批：弱电 / IT SI（Hanwha Vision 案例：Pamukkale 市政 150 摄像机）→ **集成商 25%，B，加厚一次（small：STC-2224GP / STC-4424GCPM + STI-144GP）**；ZoomInfo 334 人为错配' + TAG}}],
    'SB-388': [{'kp_match': 'hasti@fhguvenlik.com', 'name': 'Hasti F. Göller', 'role': '研究档 KP（用户表）= 收件人' + TAG},
               {'facts': {'legal_name': 'FH GÜVENLİK SİSTEMLERİ VE BİLİŞİM SANAYİ TİCARET LİMİTED ŞİRKETİ（Beşiktaş Sinanpaşa Mah. Süleyman Seba Cad. No:6/4；Perpa B Blok K:11 No:1730 技术办公室；NACE 631108）', 'founded': '2025-02-13' + TAG,
                          'other': '第 106 批：2025 新设弱电 / 安防小集成商 → **集成商 25% small；一页纸一次后不动**' + TAG}}],
    'SB-392': [{'kp_match': 'm.demirel@', 'name': 'Mustafa Demirel', 'role': '研究档 KP（用户表）= 收件人（抄 info@ 点名 Engin Ertürk）' + TAG},
               {'add_kp': {'name': 'Engin Ertürk', 'role': 'Yönetici（管理者；ZoomInfo）= 拍板人' + TAG, 'email': '', 'source': 'https://www.zoominfo.com/pic/makro-sistem/1340413263'}},
               {'facts': {'legal_name': 'MAKRO SİSTEM DIŞ TİCARET ANONİM ŞİRKETİ（单一股东 A.Ş.；Şişli Kuştepe Mah. Leylak 1 Sok. Nursanlar İş Merkezi No:1 K:7 D:26；MERSİS 未取）', 'founded': '2023-11-13' + TAG,
                          'other': '第 106 批：i-PRO（原 Panasonic Security）土耳其 Premium 分销商（11–50 人）→ **分销 20%，B BIG，加厚一次（PoE 交换机配 i-PRO 项目 + 1:1 规格对照）；升 A 次候选**；稿内不点名 i-PRO' + TAG}}],
    'SB-413': [{'kp_match': 'enes@ebcoelectronic.com', 'name': 'Enes（姓待核）', 'role': '研究档 KP（用户表；EBCO 邮箱）= 收件人' + TAG},
               {'facts': {'legal_name': 'LTE Elektronik Sanayi ve Ticaret Ltd. Şti.（安卡拉 Çankaya Mustafa Kemal Mah. 2131 Sk. Aslanlar Plaza No:24/10；关联 EBCO Electronic 香港 / m2mmarket / iot.com.tr；MERSİS 未取 → 部分坐实）', 'founded': '约 2010' + TAG,
                          'other': '第 106 批：IoT 模块 / 网关 / 天线元器件分销（Ebyte 土耳其分销；RAKwireless 合作伙伴；1–10 人）→ **分销 20% 低契合；一页纸（STI 工业线卡配其 LoRa 网关客户）一次后不动**' + TAG}}],
    'SB-921': {'facts': {'legal_name': 'Dimas Teknoloji ve Güvenlik（Gmail；未坐实：1 次检索仅命中同名他人）', 'founded': '未取' + TAG,
                         'other': '第 106 批：ISAF 需求 SFP（非 Saga 品类）+ 不会英文 → **不动**' + TAG}},
    'SB-808': [{'add_kp': {'name': 'Hasan Kara', 'role': 'Teknik Servis Müdürü（2017 起；ZoomInfo）= 技术把关人（抄送）' + TAG, 'email': '', 'source': 'https://www.zoominfo.com/p/Hasan-Kara/-1038805985'}},
               {'facts': {'legal_name': 'Deponet Elektronik Mamulleri Sanayi Pazarlama A.Ş.（EMIS 1998-03-10；Kadıköy Kozyatağı Sok. Parlarbaşoğlu Apt. No:28B + 安卡拉 Via Tower 分部；MERSİS 未取）', 'founded': '1998-03-10' + TAG,
                          'other': '第 106 批：网络产品进口分销商（Ruijie 2017 / 2018 全球最佳 VAD、Maipu、Allied Telesis、Teltonika、Leviton、Planet）+ **自有品牌 Nets** → **贴标 OEM 30% 可谈（Nets 标 PoE / 工业线）+ 分销 20%（Planet 价位替代），B BIG，加厚一次；升 A 候选（回信即 A）**；收件人 istanbul@ 点名 ürün müdürü / satın alma；稿内不点名 Planet / Ruijie' + TAG}}],
    'SB-225': [{'kp_match': 'sahin@shnrise.com', 'name': 'Şahin Öztürk', 'role': 'ISAF 名片（域名 shnrise.com 与 CESS 关系未证实）= 收件人' + TAG},
               {'facts': {'legal_name': 'CESS Güvenlik Sistemleri（cessguvenlik.com；İstanbul；MERSİS 未取 → 部分坐实；KP 域名 shnrise.com 无检索结果）', 'founded': '2018' + TAG,
                          'other': '第 106 批：小型安防 / 弱电 / 网络安装商；ISAF 需求 SFP（不做）→ **一页纸（PoE 配套 + 说明光模块不在线上）一次后不动**；同名 Şahin Teknoloji Kocaeli / SHN Teknoloji ≠' + TAG}}],
    # ---------- A 档补齐 3 ----------
    'SA-004': {'facts': {'legal_name': 'Boecek Sec（boecek.de；未坐实：域名无公开页；同名 boeck GmbH Leipheim HRB 15558 / Sicherheitstechnik Bock Berlin ≠）', 'founded': '未取' + TAG,
                         'other': '第 106 批：**A 维持（样品订单 + 具体型号问价为 Simon 一手证据）**；主体改由 Simon 侧样品订单发票抬头 / 收货地址 / VAT 号补，或下一封跟进顺手要「公司全称 + 送货地址 + VAT」' + TAG}},
    'SA-066': {'facts': {'legal_name': 'CCS（ccs-msk.ru；107589 Москва ул. Красноярская д.1 корп.1；ООО 法定名 / ИНН 官网未列 → 部分坐实；同名 ООО «ССС» 7708393591 / 7814529565、ООО «Сложные облачные системы» 7713417625 ≠）', 'founded': '未取（自述 10+ 年）' + TAG,
                         'other': '第 106 批：MICROSENS / LENOVO 官方合作伙伴 + SUMITOMO 分销商（工业以太网 / FTTO / 光模块 / 线缆）→ **A 维持；分销 20%；加厚（STI 工业线 1:1 对照 Microsens 价位）**；俄罗斯收款路径待核（Simon 定）；回信时问 реквизиты 补法定名' + TAG}},
    'SA-069': {'facts': {'legal_name': 'ООО «БИЗНЕС ПАРТНЕР»（官网安防页 + 2017 行业新闻署名）/ ООО «БПТЕХНО»（品牌页）二选一；bptehno.ru；Москва；ИНН 未取 → 部分坐实', 'founded': '未取（2017 已在业）' + TAG,
                         'other': '第 106 批：俄罗斯 + 独联体光纤传输系统分销商（代理「Optic」俄方设计 / 中国制造、Raycom 周界探测、华泰光端机）→ **A 维持；贴标 OEM 30% 可谈（BPTEHNO / Optic 标工业 PoE 与光口机）+ 分销 20%；加厚**；收款路径待核；回信时问 реквизиты 定法定名' + TAG}},
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
