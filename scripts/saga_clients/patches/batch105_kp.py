#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 105 批（T29-U98，公司底数第二十三轮 · B 档「自有 logo + 打开」三国 23 户：US 10 / TR 10 / DE 3；DE 池清空）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=105 行）。
结构同 batch104_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：可谈贴标 1（SB-132 F.A.S.T. A.Ş. 自有 RASCH 标 + 16 区域工业经销网 → 升 A 候选）；
分销 20% 大户 / 渠道 4（SB-873 ISTC = International Security and Trading Corp. BDCOM 拉美独家分销 ≈168 人 → 升 A 候选 / SB-757 Flytec Computers Ubiquiti 主分销 $19M / SB-542 LANOPIA Omnitron DACH VAD / SB-143 BroadStar AON 运营商采购型）；
分销 / 集成商一般 4（SB-868 Fiberden 网店 / SB-889 TeamOn 安卡拉卖 PLANET / SB-139 Acusense Hikvision 批发 / SB-137 Oral 北塞浦路斯）；集成商 25% 加厚 2（SB-131 Desecure Technology 集团 1,400+ 人太阳能监控塔 / SB-074 Bilge Güvenlik A.Ş. ISAF 面对面）；
渠道代理型 1（SB-845 Osborn Sales Solutions 美西制造商代表 → line card 切口）；低概率一页纸 4（SB-1083 System Fabric Works HPC / SB-356 Infinicore 白盒包探针 / SB-004 FiberHome 北美 / SB-801 Aurcore 同行品牌商）；
零星小单 / 采购型 small 5（SB-079 Cansis / SB-082 Voltech / SB-135 Labor / SB-321 BWsystems 个体 / SB-460 4G GmbH 已成交零星）；不动 2（SB-795 Yacht Gurus 直发网店 / SB-519 Kyber 未坐实）。
坐实 14 / 部分坐实 6（SB-1083 TX 号 / SB-845 CA 号 / SB-004 美国实体号 / SB-889 法定形式 / SB-079 个体 / SB-131 技术公司法定名 / SB-137 KKTC）/ 未坐实 3（SB-519 / SB-082 / SB-135）；
KP 坐实 = 老板 / GF / CEO / GM 本人 12（SB-1083 Kevin Moran / SB-143 Tyler Bell / SB-795 Addison Sammet / SB-757 Bruno Rocha + Freddy Sigal / SB-845 William Osborn + Kyle DeSousa / SB-079 Ahmet Can / SB-132 Şener Üstbaş / SB-137 Metin Oral / SB-321 Hans-Georg Werner / SB-460 Michael Kleiböhmer / SB-542 Martina + Paul Ochmann）；
城市 / 地点更正 3（SB-889 安卡拉 / SB-137 北塞浦路斯 KKTC（表内 TR 不改）/ SB-845 加州登记 + 华盛顿州办公）；法定名补全 10（SB-868 NRL Teknoloji / SB-873 International Security and Trading Corp. / SB-143 BroadStar Commercial Communications LLC / SB-074 Bilge Güvenlik Sistemleri ve Teknoloji A.Ş. / SB-132 Fabrika Aygıtları Sistem Teknolojisi A.Ş. / SB-139 Acusense Teknoloji ve Güvenlik Sistemleri Ltd. Şti. / SB-460 4G GmbH 前身 Westhoff Engineering / SB-542 LANOPIA GmbH / SB-321 个体 / SB-801 Aurcore Technology Inc.）；
守界 / 只记档 3（SB-004 母体实体清单 / SB-801 同行 / SB-854 已在 104）；升 A 候选 2（SB-132 / SB-873，回信即 A；次候选 SB-757 / SB-542 / SB-131 / SB-143）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 105 批 官方登记核实 2026-10-28）'
UPD = {
    # ---------- US 10 ----------
    'SB-801': [{'kp_match': 'bryan@aurcore.net', 'name': 'Bryan W', 'role': 'VP（研究档）= 收件人' + TAG},
               {'add_kp': {'name': 'MC Leo', 'role': 'CEO（2026-03 新闻稿）= 拍板人' + TAG, 'email': '', 'source': 'https://www.aurcore.net/news/5/'}},
               {'facts': {'legal_name': 'Aurcore Technology Inc.（CA SoS 6354007；General Corporation；IEEE OUI 在册）', 'founded': '2024-08-20' + TAG,
                          'other': '第 105 批：Lake Forest CA 开放架构网络品牌商（台湾生产基地；Marvell Prestera / Teralynx 400G/800G；AIS4001P 工业 PoE）→ **同行品牌商，贴标低概率；一页纸后不动**' + TAG}}],
    'SB-1083': [{'add_kp': {'name': 'Kevin Moran', 'role': 'President & CEO（ThinkinQ 合资 CEO）= 拍板人 / 收件人（经 info@）' + TAG, 'email': '', 'source': 'https://www.inknowvation.com/sbir/companies/system-fabric-works-inc'}},
                {'facts': {'legal_name': 'System Fabric Works Inc（TX；SoS 号未取 → 部分坐实）', 'founded': '2002-04-01' + TAG,
                           'other': '第 105 批：Cedar Park TX HPC / RDMA 集成商（InfiniBand、BeeGFS；2–10 人）→ **集成商 25% 低概率；一页纸（STH 25G/100G 管理网 / 存储网）**' + TAG}}],
    'SB-143': [{'add_kp': {'name': 'Tyler Bell', 'role': 'CEO = 拍板人（抄送）' + TAG, 'email': '', 'source': 'https://www.linkedin.com/company/broadstar-communications'}},
               {'add_kp': {'name': 'Douglas Bell', 'role': 'President & Owner（The BroadStar Companies）' + TAG, 'email': '', 'source': 'https://www.broadstar.com/douglas-bell/'}},
               {'facts': {'legal_name': 'BroadStar Commercial Communications LLC（FL Sunbiz L14000110165；FEI 47-1348982；旧 Broadstar Communications, LLC M03000000083 已注销）', 'founded': '2014-07-11（品牌 1994 起）' + TAG,
                          'other': '第 105 批：West Palm Beach FL 社区型 AON 光纤 ISP（52 社区；5 Gig；IP Infusion 白盒；$18.9M / 63 人）→ **采购型 20%，B BIG，加厚一次（光口接入 / 10G 上联 / 25G 汇聚）；升 A 次候选**' + TAG}}],
    'SB-356': [{'add_kp': {'name': 'Yonghong Tian', 'role': '登记代理人（创始人推定；华裔）' + TAG, 'email': '', 'source': 'https://ca.ltddir.com/INFINICORE/'}},
               {'facts': {'legal_name': 'Infinicore Incorporated（CA Corporation ID 3278330；Active）', 'founded': '2010-01-20' + TAG,
                          'other': '第 105 批：San Jose 白盒包探针 / 流量生成软硬件商（硬件外采 Netberg 等；3 人口径）→ **采购型 / STH 平台供货 低概率；一页纸后不动**；中文直联 Simon 定（默认否）' + TAG}}],
    'SB-795': [{'add_kp': {'name': 'Addison Sammet', 'role': 'President / 登记代理人' + TAG, 'email': '', 'source': 'https://www.bizprofile.net/fl/miami-beach/yacht-gurus-incorporated'}},
               {'facts': {'legal_name': 'Yacht Gurus, Incorporated（FL Sunbiz P17000038904；FEI 82-1410191；登记地址为邮箱 PMB 613）', 'founded': '2017-05-01' + TAG,
                          'other': '第 105 批：Miami Beach 游艇用品直发网店（交换机零星转售；10 次无回复）→ **不动**' + TAG}}],
    'SB-873': {'facts': {'legal_name': 'International Security and Trading Corp.（ISTC Corp.；SAM UEI ZR9SDV9PUY65；FL Sunbiz 号未取）', 'founded': '1995-02-27' + TAG,
                         'other': '第 105 批：Doral FL 拉美 / 加勒比安防区域分销商（8 处办公室；BDCOM 全拉美独家分销；≈168 人；$25–50M）→ **分销 20%，B BIG，加厚一次（BDCOM 旁第二来源）；升 A 候选（回信即 A）**；稿内不点名 BDCOM' + TAG}},
    'SB-519': [{'kp_match': 'justin@kyber-e.com', 'name': 'Justin Hansen', 'role': '研究档 KP（职务未核；主体未坐实）' + TAG},
               {'facts': {'legal_name': 'Kyber Electronics（未坐实：1 次检索仅命中首页）', 'founded': '未取' + TAG,
                          'other': '第 105 批：工程套件 / 工具小厂（表内「5 电口」零星；8 次无回复）→ **不动**；未坐实不补查' + TAG}}],
    'SB-757': [{'kp_match': 'fsigal@', 'name': 'Freddy Sigal', 'role': 'Director of Product Management = 选品对口 / 收件人本人' + TAG},
               {'kp_match': 'bruno@flyteccomputers.com', 'name': 'Bruno T. Rocha', 'role': 'CEO（2021 起；2009 入职销售工程师）= 拍板人（抄送）' + TAG},
               {'facts': {'legal_name': 'FLYTEC COMPUTERS INC（FL Sunbiz P07000099060；Active）', 'founded': '2007' + TAG,
                          'other': '第 105 批：Doral FL 有线 / 无线 / 光纤 / VoIP 主分销商（Ubiquiti Master Distributor、MikroTik 官方；美加拉美；$19.1M / 73 人）→ **分销 20%，B BIG，加厚一次；升 A 次候选**；18 次群发无回复 → 二次触达必换切口' + TAG}}],
    'SB-845': [{'kp_match': 'sales@osbornsalessolutions.com', 'name': 'Kyle DeSousa', 'role': 'Managing Partner（LA；登记代理人；研究档拼作 Desouza）= 收件人（kyle@）' + TAG},
               {'kp_match': 'bill@osbornsalessolutions.com', 'name': 'William Osborn', 'role': 'President（Gig Harbor WA；36 年电气 / 通信行业）= 拍板人' + TAG},
               {'facts': {'legal_name': 'Osborn Sales Solutions LLC（CA LLC，Ladera Ranch 登记 / Gig Harbor WA 办公；SoS 号未取 → 部分坐实）', 'founded': '2013' + TAG,
                          'other': '第 105 批：美西数据通信 / 企业网制造商销售代表公司（2026-01 起承接南加州代表权；2–10 人）→ **渠道代理型（不买货、拿佣金）；Simon「多跟进一下」→ 一页纸改「line card 增补」切口**；Q-33 不碰其终端' + TAG}}],
    'SB-004': {'facts': {'legal_name': 'FiberHome North America（推定 FiberHome Telecom USA, Inc. Santa Clara CA / FiberHome Telecommunications Technologies Inc. Arlington VA；美国实体号未取 → 部分坐实）；母体烽火通信 SSE 600498', 'founded': '母体 1999-12-25' + TAG,
                         'other': '第 105 批：烽火北美分支（当年兴趣 SFP 收发器 — Saga 不做光模块；母体 2020-05 入美国实体清单，只记档不入稿）→ **机会型采购 低概率；一页纸只讲交换机线后不动**；若 Simon 确认其北美独立采购且需求持续可改回 A' + TAG}},
    # ---------- TR 10 ----------
    'SB-868': {'facts': {'legal_name': 'NRL Teknoloji İletişim San. ve Tic. Ltd. Şti.（品牌站 Fiberden；İstanbul Bayrampaşa；Vergi No 6320974310 Tuna VD；MERSİS 未取）', 'founded': '未取' + TAG,
                         'other': '第 105 批：光纤产品网店（光缆 / 配线 / V-SOL ONT·OLT / PoE / SFP / MC）→ **分销 20% small；一页纸；2 次无回复 → 二次一次后不动**' + TAG}},
    'SB-889': [{'kp_match': 'info@teamon.com.tr', 'name': '（未具名）', 'role': 'info@（点名 satın alma / proje müdürü）' + TAG},
               {'facts': {'legal_name': 'TeamOn Teknoloji Çözümleri / Teamon İletişim Teknolojileri（**安卡拉 Emek**；法定形式 / MERSİS 未取 → 部分坐实）', 'founded': '未取' + TAG,
                          'other': '第 105 批：安卡拉 ICT 系统集成商 / 多品牌经销（在售 PLANET、Allied Telesis、Netgear、Ruijie 等）→ **分销 20% / 集成商 small；一页纸（PLANET 价位替代，不点名）后不动**' + TAG}}],
    'SB-074': {'facts': {'legal_name': 'Bilge Güvenlik Sistemleri ve Teknoloji A.Ş.（İstanbul Ataşehir Örnek Mah. Dr. Suphi Ezgi Sok. No:6；A.Ş. 2018-02-08 登记；前身 Bilge Elektronik Güvenlik ve Bilgisayar Sistemleri Tic. Ltd. Şti. 1998；MERSİS 未取）', 'founded': '2003/2004（业务）；A.Ş. 2018-02-08' + TAG,
                         'other': '第 105 批：电子安防系统集成商（CCTV / 弱电 / 布线 / 道路交通管理；安卡拉 / 伊兹密尔分支；11–50 人；$5.7M 口径）→ **集成商 25%，B，加厚一次（ISAF 面对面要 PoE）**；WA 土耳其语模板一次 + 英文一页纸抄 satis@bilgeguvenlik.com' + TAG}},
    'SB-079': [{'kp_match': 'acan@cansisteknoloji.com', 'name': 'Ahmet Can', 'role': '店主（ASKON Konya 会员；Armiya 经销商）= 收件人本人' + TAG},
               {'facts': {'legal_name': 'Cansis Teknoloji / Can-Sis Güvenlik ve Bilgisayar Sistemleri（科尼亚 Çumra İzzetbey Mah. Hıdır Sok. No:7/A；个体工商推定 → 部分坐实）', 'founded': '未取' + TAG,
                          'other': '第 105 批：Çumra 小型安防 / 电脑店（ISAF 问 12 光 12 电 PoE 网管，已报 $150）→ **零星小单；WA 一次性跟进报价有效期后不动**' + TAG}}],
    'SB-082': {'facts': {'legal_name': 'Voltech Elektronik（Silivri；官网为占位页；法定名 / 地址 / 登记均未取 → 未坐实）', 'founded': '未取' + TAG,
                         'other': '第 105 批：Silivri 小型电子 / 安防服务商（ISAF 找工业 PoE 网管）→ **零星小单；WA 一次（STI-288DGGPM 图 + 价）后不动**；未坐实不补查' + TAG}},
    'SB-131': [{'kp_match': 'serdar.turker@', 'name': 'Serdar Türker', 'role': '研究档 KP（用户表；职务未核）= 收件人（抄 bilgi@desecuretechnology.com）' + TAG},
               {'facts': {'legal_name': 'Desecure Technology（Desecure 集团安防技术公司；总部 Vadistanbul Sarıyer İstanbul，技术中心 Desecure Plaza Pamukkale Denizli；技术公司法定名 / MERSİS 未取 → 部分坐实；集团保安公司 Desecure Özel Güvenlik Hizmetler A.Ş.）', 'founded': '集团 2008（报警监控中心 2007）' + TAG,
                          'other': '第 105 批：关键设施安防集成 + 7/24 监控中心 + 太阳能移动安防塔（能源 / 光伏 / 港口；集团 1,400+ 人 9 地点；技术公司 ≈60 工程 / 软件）→ **集成商 25%，B BIG，加厚一次（户外工业 PoE：STI-054GP / 144GP / 288DGGPM / 488DGGPM）；升 A 次候选**；EIF 2026 安塔利亚 11-05～07 只记档' + TAG}}],
    'SB-132': [{'kp_match': 'ercan@fasttr.com', 'name': 'Ercan Erinç', 'role': '研究档 KP（用户表；职务未核）= 收件人（抄 GM）' + TAG},
               {'kp_name': 'Şener Üstbaş', 'role': 'Genel Müdür（General Manager；LinkedIn / RocketReach）= 拍板人' + TAG},
               {'facts': {'legal_name': 'Fabrika Aygıtları Sistem Teknolojisi A.Ş.（F.A.S.T.；İstanbul Ticaret Sicil 358519；FAST Plaza Küçükbakkalköy Mah. Dereyolu Sok. No:4 Ataşehir 34750）', 'founded': '1994' + TAG,
                          'other': '第 105 批：工厂自动化分销商（Meanwell / Shihlin / Renu / Texcomputer / Siboni；16 区域经销网；≈30 人）+ **自有注册品牌 RASCH**（PLC / HMI / 温控）→ **贴标 OEM 30% 可谈（RASCH 标导轨工业 PoE）+ 分销 20%，B BIG，加厚一次；升 A 候选（回信即 A）**' + TAG}}],
    'SB-135': [{'kp_match': 'info@labormuhendislik.com.tr', 'name': 'Ramazan Daş', 'role': 'ISAF 名片联系人（不会英文）= 收件人' + TAG},
               {'facts': {'legal_name': 'Labor Mühendislik（域名无搜索结果；1 次检索未命中任何同名实体 → 未坐实）', 'founded': '未取' + TAG,
                          'other': '第 105 批：ISAF 明确需求（工业 PoE + 价格表）但主体未坐实 → **零星小单；一页纸（工业线价格卡）一次后不动**' + TAG}}],
    'SB-137': [{'kp_match': 'info@oralguvenlik.com', 'name': 'Muhammad Azeem (Ullah)', 'role': 'Manager = 收件人本人' + TAG},
               {'kp_name': 'Metin Oral', 'role': 'Business Owner（Oral Companies，1982 起）= 拍板人' + TAG},
               {'facts': {'legal_name': 'Oral Güvenlik Sistemleri（Oral Companies 旗下；**北塞浦路斯 KKTC 尼科西亚**；KKTC 登记不可达 → 部分坐实）', 'founded': '2008（安防单元）；集团 1982' + TAG,
                          'other': '第 105 批：KKTC 小型安防零售 / 安装（Hikvision；≈6 人）→ **集成商 25% small；一页纸后不动**；表内 TR 不改 country_fix，物流经土耳其' + TAG}}],
    'SB-139': [{'kp_match': 'info@acusenseteknoloji.com', 'name': 'Ümit Çelik', 'role': '研究档 KP（用户表；职务未核）= 收件人' + TAG},
               {'facts': {'legal_name': 'Acusense Teknoloji ve Güvenlik Sistemleri Ltd. Şti.（İstanbul Kadıköy Merdivenköy Business İstanbul Plaza B Blok No:179；bayifi 名录 TOPTANCI；MERSİS 未取）', 'founded': '未取' + TAG,
                          'other': '第 105 批：Hikvision / Paradox 安防批发与项目供应（acusenseteknoloji.com + hikvisionsatis.com.tr）→ **分销 20%；一页纸（摄像机配套 PoE 第二线）**；稿内不点名 Hikvision' + TAG}}],
    # ---------- DE 3 ----------
    'SB-321': [{'kp_match': 'service@bwsystems.de', 'name': 'Hans-Georg Werner', 'role': 'Inhaber（Einzelunternehmen；USt-ID DE137120780）= 收件人本人' + TAG},
               {'facts': {'legal_name': 'BWsystems – Hans-Georg Werner（柏林 Köpenick Pritstabelstraße 52A；个体经营，无 HRB；USt-ID DE137120780）', 'founded': '未取' + TAG,
                          'other': '第 105 批：一人 IT 店 / eBay 网店（阿里 RFQ 2+8 PoE）→ **采购型 small；一页纸直接报 STC-228GP / STC-028GP 后不动**' + TAG}}],
    'SB-460': [{'kp_match': 'mk@4g-gmbh.de', 'name': 'Michael Kleiböhmer', 'role': 'Geschäftsführer（2023-06 起，单独代表；Münster HRB 15069 在册）= 收件人本人' + TAG},
               {'facts': {'legal_name': '4G GmbH（Amtsgericht Münster HRB 15069；Sendenhorst Industrieweg 19；股本 €63,000；原 Westhoff Engineering GmbH）', 'founded': '2014-07-04' + TAG,
                          'other': '第 105 批：电驱动技术开发 / 生产小厂（Shopify 光旁路配件已成交零星，「珊姐跟进了」）→ **采购型 small；复购一页纸后不动；成单客户只记档监控不群发**' + TAG}}],
    'SB-542': [{'kp_match': 'info@lanopia.de', 'name': 'Martina Ochmann', 'role': 'Geschäftsführerin（2002 起；Omnitron 名录联系人 martina.ochmann@）= 收件人' + TAG},
               {'add_kp': {'name': 'Paul Antony Ochmann', 'role': 'Geschäftsführer（2004 起，单独代表）= 拍板人' + TAG, 'email': '', 'source': 'https://www.companyhouse.de/LANOPIA-GmbH-Altomuenster'}},
               {'facts': {'legal_name': 'LANOPIA GmbH（Amtsgericht München HRB 143448；Altomünster Gewerbepark 23；股本 €25,000；Ochmann 家族）', 'founded': '2002-07-05' + TAG,
                          'other': '第 105 批：光纤 / 铜缆网络技术 DACH 增值分销商（Omnitron Systems 分销；MC / 交换机 / 复用器 / 光模块）→ **分销 20%，B BIG，加厚一次（工业 PoE 光口配其 MC 线）；升 A 次候选**；8 次无回复 → 二次触达换切口；稿内不点名 Omnitron' + TAG}}],
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
