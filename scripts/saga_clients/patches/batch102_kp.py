#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 102 批（T29-U95，公司底数第二十轮 · B 档「自有 logo + 打开」五国 24 户）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=102 行）。
结构同 batch101_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：贴标 OEM 30% 目标 8（SB-221 Tycon / SB-364 Nitrotel / SB-529 DMSI / SB-772 Mencom / SB-787 TC Communications 入门工业线 / SB-792 Weltron / SB-1026 Epygi / SB-657 Egesan Coremax 兼分销）；
分销 20% 7（SB-248 Nelly’s + IPCamPower 贴标 / SB-665 Marsa / SB-669 MNS 兼集成 / SB-791 Wachendorff 可谈贴标 / SB-611 Avanis / SB-172 Consteel / SB-859 Baburtech small）；分销 small 1（SB-805 CCTVSpot = MB Vision 保加利亚）；
集成商 25% 2（SB-660 Fonet / SB-411 Flöter 低优先）；采购型 small 2（SB-040 4Demand / SB-264 Tier1 均 100% 预付）；贴标 small + 100% 预付 1（SB-661 Gold-Net konkordato）；翻新商不动 1（SB-590 Carritech）；
未坐实 2（SB-668 Midosa；SB-626 Vision Dynamics ElectronX，同名 GmbH 不采）；部分坐实 3（SB-665 / SB-1026 / SB-792 州号）；KP 坐实 = 老板 / GF / President / VP / Founder / Prezes 本人 9（SB-221 / SB-364 / SB-787 / SB-669 / SB-411 / SB-611 / SB-264 / SB-172 / SB-248 技术运营官）；
州别 / 国别更正 2（SB-792 Weltron = NC 非 FL；SB-805 CCTVSpot → 保加利亚 country_fix）；法定名更正 3（SB-529 DMSI = Diversified Material Specialists, Inc.；SB-805 = MB Vision Ltd.；SB-660 ≠ 上市 FONET Bilgi Teknolojileri）；
升 A 候选 7（SB-221 / SB-364 / SB-529 / SB-772 / SB-792 / SB-669 / SB-791，回信即 A；次候选 SB-248 / SB-787 / SB-657 / SB-665 / SB-611 / SB-172）；新查号路径：TR 商务部 ETBİS 站点档案（eticaret.gov.tr/siteprofil）给 MERSİS。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 102 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US 8 ----------
    'SB-221': [{'kp_match': 'scottp@tyconsystems.com', 'name': 'Scott Parsons', 'role': 'President / 创办人（Tycon Systems Inc.；SAM UEI V8M1PCBVGN91）= **拍板人本人 = 收件人**' + TAG},
               {'kp_match': 'daimyn@', 'role': '研究档 KP（职务未核）= 抄送' + TAG},
               {'facts': {'legal_name': 'Tycon Systems Inc.（DBA Tycon Power Systems；犹他 S 型公司；UT DBA 6970120-0151；SAM UEI V8M1PCBVGN91；CAGE 5XBL3）', 'founded': '2008-01-01' + TAG, 'staff': '小型（SAM 制造商；人数未取）', 'hq': '930 W 14600 S, Suite 600, Bluffdale, UT 84065',
                          'other': '第 102 批：自有 TP- 系列 PoE 产品线 + 总裁本人收件 → **贴标 OEM 30% 目标**（Tycon 标 STI-054GP / STI-144GP / STI-288DGGPM + STC-228GP）；B BIG；加厚；升 A 候选' + TAG}}],
    'SB-248': [{'kp_match': 'rodaniel@nellyssecurity.com', 'role': 'Technical Operations Officer（2010 起；选型人）= 收件人' + TAG},
               {'kp_match': 'customerservice@nellyssecurity.com', 'role': 'Sales（官网团队页）= 抄送' + TAG},
               {'add_kp': {'name': 'Sean Nelson', 'role': '创始人（2008；另营自有 PoE 交换机品牌 IPCamPower）= 贴标线点名对象' + TAG, 'email': ''},
                'facts': {'legal_name': 'Nelly’s Security LLC（Broken Arrow OK；BBB 列为 Rackmount Solutions 一部门，CEO / Owner Jeff Morton；PitchBook 列 Acquired / Merged — 待核）', 'founded': '2008-01-01' + TAG, 'staff': '15–25 人；$3.5M（第三方）', 'hq': '501 N Aspen Ave, Broken Arrow, OK 74012',
                          'other': '第 102 批：安防分销电商 + 创始人自有 PoE 交换机品牌 IPCamPower → **分销 20%（STC-028GP / STC-228GP / STC-2216GP / STC-2224GP）+ IPCamPower 贴标 OEM 30%**；加厚一次；股权变更后先探采购人' + TAG}}],
    'SB-364': [{'kp_match': 'dmorera@nitrotelmanufacturing.com', 'name': 'Daniel Morera', 'role': 'Senior Technical Director / VP New Business Development（RCDD；2022 起）= **产品线决策人本人 = 收件人**' + TAG},
               {'add_kp': {'name': 'Ivette Patterson', 'role': 'President（D&B / CAGE；Sunbiz P18000064924）= 拍板人（点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'Nitrotel Manufacturing Corp.（Florida Profit Corporation；Sunbiz P18000064924，2018-07-27；FEI 83-1401215；旧 Nitrotel International Group, LLC 已注销）', 'founded': '2001 品牌 / 2006 公司 / 2018-07-27 现主体' + TAG, 'staff': '11–50 人', 'hq': '10440 NW 37th Terrace, Doral, FL 33178（登记 4626 SW 147 Court, Miami, FL 33185）',
                          'other': '第 102 批：自有品牌整线商（UL/ETL；已贴标 MC / SFP）+ 技术副总本人收件 → **贴标 OEM 30% 目标**（Nitrotel 标 STC-228GP / STC-2224GP / STC-4424GCPM + STI-144GP）；B BIG；加厚；升 A 候选' + TAG}}],
    'SB-529': [{'kp_name': 'Randy Harris', 'role': 'Director, Data Center & Broadband Sales（2023 起；Lenoir NC；randy.harris@dmsimfg.com）= 产品线决策人 / 收件人' + TAG},
               {'kp_match': 'dustin@dmsimfg.com', 'role': '研究档 KP（职务未核）= 抄送' + TAG},
               {'kp_match': 'evan@dmsimfg.com', 'role': '研究档写 General Manager（姓名 / 邮箱对应待核）' + TAG},
               {'add_kp': {'name': 'Jeneth D’Alonzo', 'role': 'President & CEO（Tampa Bay Business Journal 2025-05）= 拍板人（点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'Diversified Material Specialists, Inc.（DMSI / DMSI International；佛州公司；BBB 1996-07-05 注册；Sunbiz 文件号未取）', 'founded': '1996-07-05' + TAG, 'staff': '51–200 人（63）；$18.5M（第三方）', 'hq': '105 Triple Diamond Blvd, Unit 101, North Venice, FL 34275',
                          'other': '第 102 批：光纤连接合同制造商（为全球品牌 OEM / 自有标代工）+ 自有标 MC 周边 → **贴标 OEM 30% 目标**（DMSI 标 STC-228GP / STI-144GP / STC-110XGE）+ DC 线 STH-2C24XF-HSI / STH-32C-HSI；B BIG；加厚；升 A 候选' + TAG}}],
    'SB-772': [{'kp_match': 'john.heath@mencom.com', 'role': 'Engineering Manager（选型人）= 收件人' + TAG},
               {'kp_match': 'john@mencom.com', 'role': 'Sales（growjo；Kompass 误列 Owner）= 抄送' + TAG},
               {'add_kp': {'name': 'Bruce E. Mistarz', 'role': 'President / CEO / 创办人（1987；GA Domestic Profit Corporation 注册代理）= 拍板人（点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'Mencom Corporation（Georgia Domestic Profit Corporation；SoS 控制号未取；Secretary Barbara Mistarz）', 'founded': '1987（伊利诺伊起家，1990 年代迁乔治亚）' + TAG, 'staff': '39–200 人；$26.2M（第三方）', 'hq': '5750 McEver Rd, Suite A, Oakwood, GA 30566（15 万平方英尺工厂）',
                          'other': '第 102 批：美国工业连接器制造商，自有标工业交换机「标价高」且外采 → **贴标 OEM 30% 目标**（Mencom 标 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM）；B BIG；加厚；升 A 候选' + TAG}}],
    'SB-787': [{'kp_match': 'stevec@tccomm.com', 'role': 'Vice President Sales & Marketing（TC Communications, Inc.）= **产品线扩充决策人本人 = 收件人**' + TAG},
               {'kp_name': 'Fredrick Chow', 'role': '研究档 KP（职务未核）' + TAG},
               {'add_kp': {'name': 'Kai Liang', 'role': 'President & CEO / 创办人（1991）= 拍板人（点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'TC Communications, Inc.（加州公司；CAGE 0S5C7；SoS 实体号未取）', 'founded': '1991-12（Yorba Linda；1995 迁 Irvine）' + TAG, 'staff': '11–200 人', 'hq': '17881 Cartwright Road, Irvine, CA 92614（4 万平方英尺）',
                          'other': '第 102 批：自产 JumboSwitch 工业平台的制造商 → 入门级导轨工业交换机可外采贴标 → **贴标 OEM 30% 目标**（TC 标 STI-054GP / STI-144GP / STI-154GP / STI-244GP）；只谈公用事业 / 交通 / 商用，**不碰轨道 EN 50155 与国防**；加厚一次；larry@novaca.com 为外域代表（待核）' + TAG}}],
    'SB-792': [{'kp_match': 'robwinston@winstonele.com', 'role': 'Winston 家族成员（robwinston@ 列于 CAGE 3AZP6 官方邮箱；职务未核）= 收件人' + TAG},
               {'add_kp': {'name': 'Francis Winston', 'role': 'President（Wikipedia；创办人 James Pratt Winston = CEO）= 拍板人（点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'Winston International, Ltd.（Weltron® 品牌独家制造商；北卡公司；CAGE 3AZP6；DUNS 056291859；SoS 号未取；Sunbiz 的 Winston Electronics, Inc. 440526 为已解散同名他户）', 'founded': '1980（Winston International）；Weltron 品牌 1968' + TAG, 'staff': '11–50 人；<$5M（第三方）', 'hq': 'Oxford, North Carolina（**州别更正：NC 非 FL**；门牌未取）',
                          'other': '第 102 批：自有品牌 Weltron 已含 PoE 交换机 + 家族企业直收 → **贴标 OEM 30% 目标**（Weltron 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + STI-144GP）；B BIG；加厚；升 A 候选' + TAG}}],
    'SB-1026': {'add_kp': {'name': 'Mario Cuello', 'role': 'CEO（Epygi Technologies, LLC）= 拍板人（sales@ 点名）' + TAG, 'email': ''},
                'facts': {'legal_name': 'Epygi Technologies, LLC（原 Epygi Technologies, Ltd.；TX / FL 登记号未取 → 部分坐实）', 'founded': '2000' + TAG, 'staff': '11–50 人；$10–50M（第三方）', 'hq': '561 Maitland Avenue, Altamonte Springs, FL 32701（原 1400 Preston Road Ste 300, Plano, TX 75093）',
                          'other': '第 102 批：IP PBX 厂商 → 配套 IP 话机的 PoE 交换机可挂 Epygi 标 → **贴标 OEM 30% 目标 / 次选分销 20%**（STC-028GP / STC-228GP / STC-2224GP，VLAN / QoS 语音优先）；一页纸 + 贴标条款' + TAG}},
    # ---------- TR 7 ----------
    'SB-859': {'kp_match': 'ayse@baburtech.com', 'name': 'Ayşe Narinsöz', 'role': '研究档 KP（职务待核；采购 / 产品推定）= 收件人' + TAG,
               'facts': {'legal_name': 'BABURTECH BİLİŞİM SANAYİ VE TİCARET ANONİM ŞİRKETİ（MERSİS 0128085731200001 — 商务部 ETBİS；Vergi No 1280857312 Çankaya）', 'founded': '2007（ETBİS 登记 2017-12-29）' + TAG, 'staff': '小型 / 中型（自报 201–500 存疑）', 'hq': 'Cumhuriyet Mah. Ziya Gökalp Cad. No 9/3, Kızılay, Çankaya / Ankara',
                         'other': '第 102 批：笔记本 / 手机配件电商 + 网络品转售（海思白牌交换机在售）→ **分销 20% small**（STC-028GP / STC-228GP / STC-2216GP）；一页纸' + TAG}},
    'SB-657': {'kp_match': 'gokhan@egesanteknoloji.com.tr', 'role': '研究档 KP（职务未核；疑业主 / 采购）= 收件人' + TAG,
               'facts': {'legal_name': 'EGESAN TEKNOLOJİ PAZARLAMA İTH. İHR. VE TİC. LTD. ŞTİ.（Vergi No 3250872231 Bodrum；MERSİS 未取；HiLook 土耳其官方分销；自有品牌 Coremax 商标持有人）', 'founded': '2005（自述）' + TAG, 'staff': '小型（人数未取）', 'hq': 'Akçaalan Mah. Cumhuriyet Blv. No 120/1 A Blok, 48400 Bodrum / Muğla（**地域更正：Bodrum，非 İzmir**）',
                         'other': '第 102 批：多品牌安防批发 + 自有品牌 Coremax 进口商 → **分销 20% + Coremax 贴标 OEM 30% 目标**（STC-028GP / STC-228GP / STC-2216GP / STC-2224GP 对标 Ruijie Reyee RG-ES 价）；加厚一次；升 A 次候选' + TAG}},
    'SB-660': {'kp_match': 'akgun@fonet.com.tr', 'role': '研究档 KP（职务未核）= 收件人' + TAG,
               'facts': {'legal_name': 'Fonet Fiber Optik Bilgisayar Hizmetleri Ticaret Limited Şirketi（Vergi No 3880095179；MERSİS 未取；**与上市公司 FONET Bilgi Teknolojileri A.Ş.（Ankara 医疗信息化）无关**）', 'founded': '1995' + TAG, 'staff': '小型（人数未取）', 'hq': 'İstanbul（门牌未取）',
                         'other': '第 102 批：30 年结构化布线 / 交钥匙数据中心集成商 → **集成商 25%**（STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W + STC-448XGGPM / STH-2C24XF-HSI）；一页纸 + DC 规格' + TAG}},
    'SB-661': {'kp_match': 'murat@goldnet.com.tr', 'role': '业主 Murat Gündeğer 推定同人（konkordato 申请人之一；未证）= 收件人' + TAG,
               'facts': {'legal_name': 'GOLD-NET BİLİŞİM ELEKTRONİK SANAYİ VE TİCARET LİMİTED ŞİRKETİ（MERSİS 0396049037300015；Vergi No 3960490373；Ticaret Sicil 7956 Çorlu；关联 Teknogon Güvenlik）', 'founded': '2004-10-01' + TAG, 'staff': '小型（人数未取）', 'hq': 'Kazımiye Mah. Dadaloğlu Cad. No 42, Çorlu / Tekirdağ 59860（**地域更正：Çorlu，非 İstanbul**）',
                         'other': '第 102 批：自有品牌 GOLDNET NVR / 摄像机，但 **2019 起 konkordato 重整程序（2019/297 → 2021/219 → 2024/79）→ 回款风险高** → 贴标 small，仅 100% 预付、不赊、不备货（STC-028GP / STC-228GP）；一页纸一次；对客不提重整' + TAG}},
    'SB-665': {'kp_match': 'ali.yildiz@marsateknoloji.com', 'role': '研究档 KP（职务未核）= 收件人；点名 satın alma / genel müdür' + TAG,
               'facts': {'legal_name': 'Marsa Teknoloji ve Yazılım A.Ş.（İstanbul Ümraniye；Vergi No / MERSİS 未取 → 部分坐实；U-Prox / Ur-fog / BAS-IP / Fanvil 土耳其授权分销）', 'staff': '小型（人数未取）' + TAG, 'hq': 'İnkılap Mah. İlkkurşun Cad. No 83/A-B, Ümraniye / İstanbul',
                         'other': '第 102 批：有进口经验的品牌分销商（IP 对讲 + IP 话机 = PoE 交换机配套需求）→ **分销 20%**（STC-028GP / STC-228GP / STC-2224GP + STI-144GP）；加厚一次；升 A 次候选' + TAG}},
    'SB-668': {'kp_match': 'tanersahin@midosa.com.tr', 'role': '研究档 KP（职务未核；1 次检索未命中登记主体 → 未坐实）= 收件人' + TAG,
               'facts': {'legal_name': 'Midosa（midosa.com.tr；登记主体 / Vergi No 未取 → 未坐实；站点 http_error）',
                         'other': '第 102 批：**未坐实 + 站点失效** → 一页纸一次（STC-228GP / STC-2224GP），不回复即不动；下轮补项：whois / İletişim 页 Vergi No' + TAG}},
    'SB-669': {'kp_match': 'mahmut.bektas@mnsbilisim.com', 'role': 'Founder / 业主（MNS Bilişim Hizmetleri San. ve Tic. Ltd. Şti.，2005 起）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'MNS Bilişim Hizmetleri San. ve Tic. Ltd. Şti.（Vergi No 6220446809 Zincirlikuyu；MERSİS 未取；电商 mnspazar.com；Ruijie / Ubiquiti 土耳其授权销售）', 'founded': '2005-07-07' + TAG, 'staff': '11–50 人', 'hq': 'Mecidiyeköy Mah. Cemal Sahir Sk. Polat Mecidiyeköy İş Merkezi No 29, K:4 D:43, Şişli / İstanbul',
                         'other': '第 102 批：Ruijie / UniFi 增值经销 + 老板本人收件 + 已卖 10G/25G → **集成商 25% + 分销 20%**（STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM + STH-2C24XF-HSI + STC-110XGE 对标 Ruijie 6120）；B BIG；加厚；升 A 候选' + TAG}},
    # ---------- DE 4 ----------
    'SB-791': {'add_kp': {'name': 'Robert Wachendorff', 'role': 'Geschäftsführer & Inhaber（Dipl.-Wirtsch.-Ing.；Wachendorff Prozesstechnik GmbH & Co. KG，HRA 7403 Wiesbaden）= 拍板人（wp@ / vertrieb@ 点名）' + TAG, 'email': ''},
               'facts': {'legal_name': 'Wachendorff Prozesstechnik GmbH & Co. KG（Amtsgericht Wiesbaden HRA 7403；Komplementär Wachendorff GmbH HRB 20054；USt-ID DE113657232）', 'founded': '1978-11-17' + TAG, 'staff': '集团 >110 人；>€25M（2022）', 'hq': 'Industriestraße 7, 65366 Geisenheim',
                         'other': '第 102 批：老牌工业电子进口分销（有进口经验者）+ 表内「可以着重跟一下」→ **分销 20%，可谈 Wachendorff 标 OEM 30%**（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM / STI-0240GE）；B BIG；加厚；升 A 候选；研究档 kontakt@segno.de 为关联域，收件改官方 wp@ / vertrieb@' + TAG}},
    'SB-411': {'kp_match': 'd@floeter-sdt.de', 'role': 'Geschäftsführer / Alleingesellschafter（Amtsgericht Leipzig HRB 38796；另任 SignalTech GmbH GF）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'Flöter SDT | Sicherheit, Detektei und Technik GmbH（HRB 38796 Leipzig；资本 €25,000）', 'founded': '2021-04-22（登记 2021-04-28）' + TAG, 'staff': '微型 / 小型（人数未取）', 'hq': 'Dewitzer Straße 77h, 04425 Taucha',
                         'other': '第 102 批：保安服务为主、安防技术为辅 + 表内 7 次跟进无回复 → **集成商 25% 低优先**（STC-028GP / STC-228GP），一页纸最后一次后不动' + TAG}},
    'SB-611': [{'kp_match': 'tpasslack@avanis.de', 'role': 'Geschäftsführer / Gesellschafter（Avanis GmbH，HRB 37834 Bielefeld；2003 起）= **拍板人本人 = 收件人**' + TAG},
               {'kp_name': 'Valentin Kaiser', 'role': '研究档 KP（职务未核）' + TAG},
               {'add_kp': {'name': 'Paul Peter Kaiser', 'role': 'Geschäftsführer / Gesellschafter（2003 起；pkaiser@avanis.de 官网团队页）= 抄送' + TAG, 'email': 'pkaiser@avanis.de'},
                'facts': {'legal_name': 'Avanis GmbH（Amtsgericht Bielefeld HRB 37834；资本 €70,000；LEI 529900I6QC9S0TFPUY37；USt-ID DE813687094）', 'founded': '2003-04-22（登记 2003-05-15）' + TAG, 'staff': '8–19 人', 'hq': 'Meisenstraße 79a, 33607 Bielefeld（Technologiepark）',
                          'other': '第 102 批：有源网络设备经销 + WLAN 规划（已用 Edgecore）+ 老板本人收件 → **分销 20% / 集成商 25% 两可**（STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM + STC-110XGE 对标 Edgecore ECS-4650）；B BIG；加厚；升 A 候选' + TAG}}],
    'SB-626': {'kp_match': 'joseph.nb@visiondynamics.de', 'role': '研究档 KP（职务未核；1 次检索未命中本户登记 → 未坐实）= 收件人' + TAG,
               'facts': {'legal_name': 'Vision Dynamics ElectronX（visiondynamics.de；法人主体未取 → 未坐实；vision-dynamics.de 的 Vision Dynamics GmbH（HRB München 235057，工业自动化咨询）为同名他户，不采）',
                         'other': '第 102 批：**未坐实** → 表内「之前谈过」仍值一封一页纸（STC-228GP / STC-2224GP / STI-144GP）点回旧话题；下轮补项：Impressum / whois' + TAG}},
    # ---------- GB 4 ----------
    'SB-040': [{'kp_match': 'procurement@4demand.co.uk', 'role': '采购（表内；WhatsApp +971 已加 → 海湾一线）= 收件人' + TAG},
               {'kp_name': 'Mohsen Tavakoli Zaniani', 'role': 'Director / PSC 75–100%（*1992-02；British；Companies House 14564199，2022-12-30 起）= 拍板人（抄送 / 点名）' + TAG},
               {'facts': {'legal_name': '4DEMAND LTD（Companies House 14564199；股本 £1；SIC 46900 / 62012 / 62020 / 62090；UK Skilled Worker 担保资质）', 'founded': '2022-12-30' + TAG, 'staff': '微型（<10 人；营业额 <£1M）', 'hq': '227 Nether Street, London N3 1NT（2024-10-23 起；前址 80 Golders Green Road NW11 8LN）',
                          'other': '第 102 批：£1 资本微型贸易 / 转口公司（面向海湾）→ **采购型 small：一页纸 + 100% 预付、不赊、不备货**（STC-028GP / STC-228GP / STC-2224GP 按单）；目的地 / 最终用户按出口合规核对' + TAG}}],
    'SB-590': {'add_kp': {'name': 'Miguel Asín Barcos', 'role': 'Director / PSC / Sales Director（2011 起；Madrid；Companies House 07260202）= 收件点名；创始董事 Bruce Iain Sutherland（2010）' + TAG, 'email': ''},
               'facts': {'legal_name': 'CARRITECH LTD（Companies House 07260202；SIC 61900；股本 £200；注册地 124 City Road EC1V 2NX 为虚拟办公地址）', 'founded': '2010-05-20' + TAG, 'staff': '11 人（2025 账）；营收约 $1.45M（第三方）', 'hq': 'London（注册）+ Madrid（运营）',
                         'other': '第 102 批：运营商旧设备备件 / 翻新 / WEEE 回收商（同行·翻新类）+ 表内 2 次跟进无回复 → **一页纸一次后不动**（仅 STI-144GP / STC-228GP 配其光模块业务）' + TAG}},
    'SB-264': {'kp_match': 'sales@tier1ds.com', 'name': 'Mohammad Samir Jamjam', 'role': 'Director / 创始人 / PSC（*1990-05；Indian；Companies House 11652776，2018-10-31 起；研究档拼写「Sameer JamJam」）= **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'TIER1 DATA SYSTEMS LIMITED（Companies House 11652776；VAT GB311899586；SIC 46520 / 47910；1 人；多名印度籍董事进出）', 'founded': '2018-10-31' + TAG, 'staff': '微型（1 人）', 'hq': '167-169 Great Portland Street, 5th Floor, London W1W 5PF（商务中心；前址 85 Great Portland Street）',
                         'other': '第 102 批：品牌货经纪（Cisco 为主）+ 商务中心壳 → **采购型 small：一页纸 + 100% 预付、不赊**（STC-2224GP / STC-4424GCPM / STC-110XGE 按单）' + TAG}},
    'SB-805': {'facts': {'legal_name': 'MB Vision Ltd.（保加利亚 Plovdiv；BG VAT / ЕИК 202150972；UK VAT GB411290538；cctvspot.co.uk 为英国销售前台）', 'founded': '2012（自述）' + TAG, 'staff': '微型（人数未取）', 'hq': 'ul. Sredets 20, 4003 Plovdiv, Bulgaria（**国别更正：保加利亚**）',
                         'other': '第 102 批：保加利亚在线 CCTV 进口零售商（Hikvision / Dahua 授权；表内用 UTEPO PoE）→ **分销 20% small**（STC-028GP / STC-228GP / STC-2216GP）；一页纸；联系 = 站点公示 Gmail cctv.mbvision@' + TAG},
               'country_fix': '保加利亚'},
    # ---------- PL 1 ----------
    'SB-172': {'kp_match': 'sklep@consteel-electronics.com', 'role': 'Prezes Zarządu（普通合伙人 CONSTEEL ELECTRONICS Sp. z o.o.，KRS 0000681591）/ 股东 50% = **拍板人本人 = 收件人**' + TAG,
               'facts': {'legal_name': 'CONSTEEL Electronics Sp. z o.o. Sp. k.（KRS 0000691687；NIP 5862321609；REGON 368059985；普通合伙人 KRS 0000681591，资本 50,000 zł；股东 Bartosz Marciszewski / Marta Ewa Borkowska）', 'founded': '2017-08-22' + TAG, 'staff': '8–11 人；营收 7.9 mln zł（bizraport，2024 -22%）', 'hq': 'ul. Rzemieślnicza 17-19, 81-855 Sopot',
                         'other': '第 102 批：3onedata 波兰分销（表内「质量一般」）+ 老板本人收件 → Saga STI 作其第二工业线 → **分销 20%**（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM / STI-0240GE 对标 3onedata IES 价）；轨道 EN 50155 / IEC 61850 守界不谈；B BIG；加厚；升 A 候选' + TAG}},
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
