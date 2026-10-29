#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""External XC · 「路径未建」补邮箱 批 X1-02（2026-10-29，T29-U121 Simon「OK 继续」）。

对象：闸 1 自动判「渠道型主体但路径未建 → 补到邮箱再闸 2」的 keep_C 户里，按对位（工业 / 安防 / 数据中心渠道）+ 区域
（四主区 + 波兰 > 欧洲其他 > 其他）优先挑出的 54 户。每户一次 depth-1 检索（未中即止），结果（邮箱 / 法人 / 注册号 /
地址 / 事实 + URL）落在 data/external_clients/xc_path_fill_2026-10-29.json（本脚本只读它，不再外查）。

本脚本把「找到的路径」落回三处（全部幂等）：
  1. data/external_clients/{cctv,edgecore,mikrotik}.json['records'] —— emails 追加 {addr, status:'公开·X1-02 补'}、
     emails_live 同步、flags「无可用邮箱 / 缺联系」改为「邮箱已补（X1-02 …）」；XC-E064 国别 PT→ES（官网电话 +34 Madrid）。
  2. data/external_clients/research/<code>.json —— 轻研究卡（round X1-02；证据带 URL + 日期；等级不动 = C，池位在 sieve_x）。
  3. data/external_clients/sieve_x.json —— 同一轮检索顺带拿到官方注册号 / 官网页脚法人名的，按闸 2 / 闸 3 口径直接定：
       pool ★ / ○（登记坐实或部分坐实 + reg_pending；对位 ✔；渠道主体 ✔；邮箱 ✔）、pool_watch ☆（微型 / 对位一般但坐实，
       试单后转正）、keep_C（对位弱 / 微型安装商 / 电商 / 运营商 / 被并购 / 仍无邮箱）—— 有邮箱者标 email_found，群发可用。
     入池户追加到 data/saga_clients/P池_巡检表_2026-10-29.csv（正式 / 观察）+ docs/P池_资产池名册_2026-10-29.md「External 并池 · 批 X1-02」。

用法：python3 sieve_batches_x/x1_002_email.py
"""
import collections
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve_x  # noqa: E402
import research_store  # noqa: E402

BATCH = 'X1-02'
DATE = '2026-10-29'
NEXT_CHECK = '2026-12-28'
ROOT = sieve_x.ROOT
DATA = os.path.join(ROOT, 'data', 'external_clients')
FILL = os.path.join(DATA, f'xc_path_fill_{DATE}.json')
WATCH = os.path.join(ROOT, 'data', 'saga_clients', f'P池_巡检表_{DATE}.csv')
ROSTER = os.path.join(ROOT, 'docs', f'P池_资产池名册_{DATE}.md')
CHECK_ITEMS = '官网改版 / 新品 / 招聘 / 社媒（LinkedIn / FB / IG）/ GitHub / 展会出席 / 新闻稿 / 域名 MX 存活'
REPO_FILE = {'cctv-info': 'cctv.json', 'edgecore-info': 'edgecore.json', 'mikrotik-info': 'mikrotik.json'}
MAIN = '四主区 + 波兰'
EU = '欧洲其他'

# code: dict(verdict, star, group, company, country, links, tags, reason)
# 口径：★ 体量 + 对位 + 登记齐；○ 对位 + 登记（或页脚法人 + reg_pending）但体量一般；☆ 观察（微型 / 对位一般，试单后转正）；keep_C 留储备。
D = {
    # ---- 直接入池 ★ ----
    'XC-M095': dict(verdict='pool', star='★', group=EU, company='GOMA ELETTRONICA SpA', country='意大利', links='goma.it', tags=['industrial', 'oem_target', 'civil_only'],
                    reason='★ 嵌入式 / 工业计算分销 + 自产平台 20%（自有品牌 → 30% OEM 线）：GOMA ELETTRONICA SpA（Torino；P.IVA 02367820012；资本 €3,000,000；1977 起；190+ 人、两厂；CEO Irene Gozzo）坐实；ORing 授权 → STI 工业对位；市场含工业 / 交通 / 国防 → 只谈工业与交通民用项目；info@goma.it'),
    'XC-M093': dict(verdict='pool', star='★', group=EU, company='Compass Distribution（Sirius S.p.A.）', country='意大利', links='compass-distribution.it', tags=['security_dist'],
                    reason='★ IT / 网络 / 安防 / 布线分销 20%：Compass Distribution = Sirius S.p.A.（Grugliasco TO；P.IVA 01240900397；R.E.A. RA 130368；资本 €1.16M；2011 起；21–50 人；CEO Giampaolo Sabbatani、SMB Sales Director Rossella Barbieri）坐实；ComNet 授权 → PoE / 工业对位；info@compass-distribution.it'),
    'XC-M185': dict(verdict='pool', star='★', group=EU, company='Koning & Hartman B.V.', country='荷兰', links='koningenhartman.com | koningenhartman.nl', tags=['industrial'],
                    reason='★ 工业 / 电信 / 安防技术分销 20%：Koning & Hartman B.V.（Zwijndrecht Voltastraat 4，2024-06 新总部 + 物流中心；KvK 34222312；BTW NL814169144B01；比利时 Vilvoorde 分部）坐实；ORing 授权 → STI 工业对位；中型；info@koningenhartman.com'),
    'XC-M186': dict(verdict='pool', star='★', group=EU, company='SmartSD B.V.', country='荷兰', links='smartsd.com', tags=['security_dist'],
                    reason='★ 安防分销 20%：SmartSD B.V.（Breda Minervum 7118；KvK 24430056；51–100 人；NL + BeLux + 西班牙 SmartSD Hommax）坐实；ComNet 授权 → PoE / 工业对位；info@smartsd.com'),
    # ---- 直接入池 ○（登记坐实）----
    'XC-M112': dict(verdict='pool', star='○', group=EU, company='E.V.D.I. SAS（Environnement Voix Données Image）', country='法国', links='evdi.fr', tags=['security_dist', 'civil_only'],
                    reason='○ 关键基础设施视频 / 传输 / 布线 B2B 分销 20%：E.V.D.I. SAS（Malaucène；RCS Avignon 399 343 870；SIRET 399 343 870 00040；资本 €80,000；1994 起；Président Laurent Duboc）坐实；ComNet / AMG / KBC 授权 → 工业 / PoE 对位；客户含核电 / 军用 → 只谈民用项目；contact@evdi.fr'),
    'XC-M115': dict(verdict='pool', star='○', group=EU, company='PHOEBE Ile de France', country='法国', links='phoebe.fr | distribution.phoebe.fr', tags=['industrial', 'dayjob_fit'],
                    reason='○ 电信 / 光传输工程 + 产品分销 25%：PHOEBE Ile de France（Les Ulis；SIRET 412 080 814 00095；1996 起；75 人；子公司 PHOEBE Fibres 供光缆跳线）坐实；ORing 授权分销 → STI / FS 对位（光传输亦合日职线）；contact@phoebe.fr'),
    'XC-M117': dict(verdict='pool', star='○', group=EU, company='SPHINX CONNECT FRANCE（Sphinx France）', country='法国', links='sphinxfrance.com', tags=['industrial'],
                    reason='○ 工业连接 / OT / IoT 方案欧洲分销 20%：SPHINX CONNECT FRANCE（Montaigu-Vendée；SIREN 439 398 462；Moxa / Sierra Wireless / Kerlink / Sintrones；自述「vente de routeurs 4G, switchs Ethernet」）坐实；体量待量化（Nantes / Paris / Lyon + ES / IT 站）→ 先 ○；sales@sphinxfrance.fr，具名 Christelle Joncheray'),
    'XC-M125': dict(verdict='pool', star='○', group=EU, company='Electrobit OÜ', country='爱沙尼亚', links='electrobit.ee', tags=['industrial'],
                    reason='○ 工业自动化分销 20%：Electrobit OÜ（Tallinn Suur-Sõjamäe 13A；Registrikood 10668940；KMKR EE101082723；原 Beijer Electronics Eesti OÜ）坐实；Westermo Reseller → STI 对位；官网具名销售工程师（arvo.lokk@ / andrei.dorosh@ / rene.erkman@）；info@electrobit.ee'),
    'XC-M127': dict(verdict='pool', star='○', group=EU, company='AUTOMATIKOS CENTRAS, UAB', country='立陶宛', links='automatikoscentras.lt', tags=['industrial'],
                    reason='○ 工业自动化分销 + 集成 20%：AUTOMATIKOS CENTRAS, UAB（Kaunas Pramonės pr. 17H；Įmonės kodas 111760799；Vadovas Liudgardas Skruodenis）坐实；Westermo Reseller → STI 对位；info@automatikoscentras.lt'),
    'XC-M187': dict(verdict='pool', star='○', group=EU, company='MVA - Electrotécnia, Lda.', country='葡萄牙', links='mva.pt', tags=['industrial'],
                    reason='○ 自动化 / 通信 / 能源系统方案伙伴 20%：MVA - Electrotécnia, Lda.（Carnaxide；NIF 502 539 186；Ethernet / 光纤 / RF 通信系统线）坐实；Westermo Reseller → STI 对位；报价箱 comercial@mva.pt'),
    'XC-M194': dict(verdict='pool', star='○', group=EU, company='Tektraco Ltd.', country='马耳他', links='tektraco.com | tektracotelecoms.com', tags=['industrial'],
                    reason='○ 电信基础设施分销 20%：Tektraco Ltd.（San Gwann；C11363；VAT MT1204-6917；1990 起；10–49 人；GPON / OSP 光纤 / LAN / 测试线，另有实验室 / 医疗气体业务）坐实；Westermo Reseller → FS / STI 对位；sales@ / telecomsales@tektraco.com，CEO K. Sciberras 具名'),
    'XC-M131': dict(verdict='pool', star='○', group=EU, company='SC IMPERIAL ELECTRIC SA', country='罗马尼亚', links='imperialelectric.ro', tags=['industrial', 'civil_only'],
                    reason='○ 工业通信分销 + 集成 20%：SC IMPERIAL ELECTRIC SA（București；CIF RO 6755；J40/16226/91；1991 起；营收 ≈€1M；1–9 人；DG Mihai Georgescu / Director Executiv Vlad Georgescu 具名）坐实；ORing / MOXA / ICP DAS 代理 → STI 对位；产品线含 EN50155 轨道认证 → 只谈非轨交项目；office@imperialelectric.ro'),
    'XC-M109': dict(verdict='pool', star='○', group=EU, company='ELKOTEX d.o.o.', country='斯洛文尼亚', links='elkotex.si | b2b.elkotex.si', tags=['isp_channel'],
                    reason='○ IT 分销 20%：ELKOTEX podjetje za trgovino in zastopanje d.o.o.（Ljubljana Magistrova 1；MŠ 1447025000；DŠ SI80941427；1999 起；29 人；外资控股）坐实；MikroTik 官方分销 → SmartByte 管理型 + STI 对位；prodaja@elkotex.si'),
    'XC-M122': dict(verdict='pool', star='○', group=EU, company='ATC AUTOMATION LIMITED', country='爱尔兰', links='atcautomation.ie', tags=['industrial'],
                    reason='○ 工业自动化集成 + 批发 25%：ATC AUTOMATION LIMITED（Tallaght Dublin 24；CRO 336758；2000 起；11–50 人）坐实；Red Lion / N-Tron 渠道 → STI 对位；automationsales@atc.ie'),
    'XC-M103': dict(verdict='pool', star='○', group=EU, company='Last Mile Communication AS（Last Mile AS）', country='挪威', links='lastmile.no', tags=['industrial'],
                    reason='○ 工业数据通信 + IP 视频方案分销 20%：Last Mile Communication AS（Asker Lensmannslia 4；Org.nr 913821289；1999 起；11–50 人；CEO Hans-Jørgen Solli；市政 / 电力 / 海事 / 油气）坐实；Westermo Gold → STI 工业对位；salg@lastmile.no'),
    'XC-M121': dict(verdict='pool', star='○', group=EU, company='Avtera BH d.o.o.', country='波黑', links='avtera.ba', tags=['isp_channel', 'prepay'],
                    reason='○ IT / 消费电子进口分销 20%：Avtera BH d.o.o.（Sarajevo Blažuj 78；Reg. 065-0-Reg-08-002025 Općinski sud Sarajevo；PDV 201375920000；资本 900,000 KM；Direktor Ajdin Babić）坐实；Westermo Reseller 名录 → 对位 ✔ 但 IT 大分销口径；非 EU → 预付 100% 起步；avtera@avtera.ba'),
    'XC-C1466': dict(verdict='pool', star='○', group=MAIN, company='Hartford Electronics GmbH', country='德国', links='hartford-electronics.de', tags=['security_dist', 'oem_target'],
                     reason='○ 安防（报警 / 视频 / 传感）制造 + 分销 20–30%：Hartford Electronics GmbH（Dortmund；HRB 28743 Amtsgericht Dortmund；资本 €25,000）坐实；自有 PoE 摄像线 → 交换机捆绑 / 贴牌对位；主区 DE；体量小 → ○；kundendienst@hartford-electronics.de（客服箱，待挖销售 KP）'),
    'XC-E060': dict(verdict='pool', star='○', group=MAIN, company='Delta Computer Products GmbH', country='德国', links='deltacomputer.de', tags=['dc'],
                    reason='○ IT 系统商 / 服务器与存储 25%：Delta Computer Products GmbH（Reinbek Röntgenstr. 4；HRB 3678 RE Amtsgericht Lübeck；USt DE135110550）坐实；Edgecore 经销商名录 → 数据中心交换机对位（CENTEC 敲门砖）；主区 DE；info@deltacomputer.de'),
    # ---- 直接入池 ○（官网 / 名录法人名 = 部分坐实 → reg_pending）----
    'XC-M132': dict(verdict='pool', star='○', group=MAIN, company='ABP Technology（ABP TECH）', country='美国', links='abptech.com', tags=['industrial', 'reg_pending'],
                    reason='○ IP 技术 / 工业网络专业分销 20%：ABP Technology（Dallas TX；PLANET 美国授权分销，在售 PLANET 工业以太网全系）官网部分坐实（州注册号待补）；主区 US；sales@ / partners@abptech.com'),
    'XC-M154': dict(verdict='pool', star='○', group=MAIN, company='Pulse Supply', country='美国', links='pulsesupply.com', tags=['industrial', 'reg_pending'],
                    reason='○ 网络技术分销 20%：Pulse Supply（Sparks MD；PLANET 授权分销；设区域销售总监 bpicardi@ / jomack@ 与 reseller 授权表）官网部分坐实（州注册号待补）；主区 US；sales@ / reseller@pulsesupply.com'),
    'XC-M158': dict(verdict='pool', star='○', group=MAIN, company='Santa Clara Systems, Inc.', country='美国', links='santaclarasystems.com', tags=['industrial', 'reg_pending'],
                    reason='○ 工业自动化与控制分销 20%：Santa Clara Systems, Inc.（Alameda CA；Moxa 授权；11–50 人）官网部分坐实（CA SOS 号待补）；主区 US；sales@santaclarasystems.com'),
    'XC-M168': dict(verdict='pool', star='○', group=MAIN, company='Marshall Wolf Automation, Inc.', country='美国', links='wolfautomation.com', tags=['industrial', 'reg_pending'],
                    reason='○ 全线工业自动化分销 20%：Marshall Wolf Automation, Inc.（Algonquin IL；50+ 品牌授权含 Advantech；11–50 人）官网部分坐实（IL SOS 号待补）；主区 US；sales@wolfautomation.com'),
    'XC-M177': dict(verdict='pool', star='○', group=MAIN, company='Distec Ltd', country='英国', links='distec.co.uk', tags=['industrial', 'reg_pending'],
                    reason='○ 工业计算 / IIoT 方案分销 20%：Distec Ltd（Irlam Manchester；InHand Networks 区域渠道分销 2025-09；Industry 4.0 Summit 参展）官网部分坐实（Companies House 号待补）；主区 GB；sales@ / info@distec.co.uk'),
    'XC-M179': dict(verdict='pool', star='○', group=MAIN, company='LC Automation Ltd', country='英国', links='lca.co.uk', tags=['industrial', 'reg_pending'],
                    reason='○ 自动化 / 运动控制 / 机械安全分销 20%：LC Automation Ltd（Blackburn + Chippenham；Red Lion 分销商）官网部分坐实（Companies House 号待补）；主区 GB；sales@lca.co.uk'),
    'XC-E068': dict(verdict='pool', star='○', group=MAIN, company='Vesper Technologies Ltd.', country='英国', links='vespertec.com', tags=['dc', 'reg_pending'],
                    reason='○ 数据中心服务器 / 网络 / 存储方案 25%：Vesper Technologies Ltd.（Stockport SK4 3EJ；NVIDIA 北欧之星伙伴，HGX / DGX；11–50 人；MD Allan Kaye）官网部分坐实（Companies House 号待补）；Edgecore 经销商 → DC 交换机对位（CENTEC 敲门砖）；主区 GB；info@vespertec.com'),
    'XC-M124': dict(verdict='pool', star='○', group=EU, company='DataLink Communications Ltd', country='爱尔兰', links='datalinkcom.net', tags=['industrial', 'reg_pending'],
                    reason='○ 工业通信分销 20%：DataLink Communications Ltd（Loughrea Co. Galway；ORing 授权；emacsys 分销名录；11–50 人；覆盖 IE / UK）名录 + 官网部分坐实（CRO 号待补）；sales@datalinkcom.net'),
    'XC-M100': dict(verdict='pool', star='○', group=EU, company='Adeptor AS', country='挪威', links='adeptor.no', tags=['industrial', 'reg_pending'],
                    reason='○ 电子 / 电气设备增值分销 20%：Adeptor AS（Bergen；20 年；HMS Red Lion / N-Tron 渠道；官网具名部门负责人 elen.arnoy@ / leah.foseid@ / elias.storaas@）官网部分坐实（Org.nr 待补）；sales@adeptor.no'),
    'XC-M101': dict(verdict='pool', star='○', group=EU, company='Autic System AS', country='挪威', links='autic.no', tags=['industrial', 'reg_pending'],
                    reason='○ 自动化 / 工业 IT + 工业通信方案供应 20%：Autic System AS（Tønsberg；NO / SE / DK 站点；HMS Red Lion / N-Tron 渠道）官网部分坐实（Org.nr 待补）；post@ / support@autic.no'),
    'XC-M072': dict(verdict='pool', star='○', group=EU, company='КОМИКОН ООД（Comicon Ltd.）', country='保加利亚', links='comicon.bg', tags=['industrial', 'oem_target', 'reg_pending'],
                    reason='○ 工业自动化方案 + 自产无线 / 网关 / 接口转换器 20–30%：КОМИКОН ООД（Sofia；802.15.4 / EnOcean / LoRa 自有品牌；HMS / Red Lion 渠道；联系人 Живка Колева）官网部分坐实（ЕИК 待补）；自有品牌 → OEM 线；comicon@comicon.bg'),
    'XC-M073': dict(verdict='pool', star='○', group=EU, company='Ритбул ЕООД（Rittbul EOOD）', country='保加利亚', links='rittbul.bg', tags=['industrial', 'reg_pending'],
                    reason='○ 德系电气 / 自动化产品进口分销 20%：Ритбул ЕООД（Sofia + Plovdiv 展厅；Druseidt 等；Westermo Reseller；所有人 Мария Божкова）官网部分坐实（ЕИК 待补）；office@rittbul.bg'),
    'XC-E063': dict(verdict='pool', star='○', group=EU, company='Xentech B.V.', country='荷兰', links='xentech.nl', tags=['dc', 'reg_pending'],
                    reason='○ SDN / 白牌交换机 + 定制服务器 25%：Xentech B.V.（Zaandam Vredeweg 46/D1；Pica8 / Cumulus / HFT；Edgecore 经销商）官网部分坐实（KvK 待补）；数据中心交换机对位（CENTEC 敲门砖）；小型 → ○；sales@xentech.nl'),
    # ---- 观察档 ☆（坐实但微型 / 对位一般，试单后转正）----
    'XC-M174': dict(verdict='pool_watch', star='☆', group=MAIN, company='Control Technologies UK Ltd', country='英国', links='controltech.uk.com', tags=['industrial', 'micro'],
                    reason='☆ CAN / 嵌入式与工业通信分销 20%：Control Technologies UK Ltd（Sharnbrook；Company No 07901679；VAT GB266046990；Ixxat / Kunbus / CSS Electronics）坐实；主区 GB；微型 + 以 CAN 为主 → 观察档；info@controltech.uk.com'),
    'XC-M189': dict(verdict='pool_watch', star='☆', group=EU, company='Ekanet Soluciones, S.L.', country='西班牙', links='ekanet.es', tags=['industrial', 'micro'],
                    reason='☆ 19" 机柜制造 + 网络设备（交换机 / UPS / 光纤）分销 20%：Ekanet Soluciones, S.L.（Humanes de Madrid；CIF B86905536）坐实；小型 → 观察档；comercial@ekanet.es'),
    'XC-M097': dict(verdict='pool_watch', star='☆', group=EU, company='Piero Bersanini', country='意大利', links='pierobersanini.com', tags=['industrial', 'micro'],
                    reason='☆ 工业电气 / 自动化元件网店 + 分销 20%：Piero Bersanini（Milano；P.IVA IT09290730150；Westermo Gold / PULS / E-T-A）坐实；仅客服箱 help@ → 观察档，待挖采购 KP'),
    'XC-M087': dict(verdict='pool_watch', star='☆', group=EU, company='Χ. Β. Τσακαρέλος & ΣΙΑ Ε.Ε.（NetAP）', country='希腊', links='netap.gr', tags=['industrial', 'micro', 'reg_pending'],
                    reason='☆ 网络 / 自动化 / 保护系统分销 + 技术支持 20%：Χ. Β. Τσακαρέλος & ΣΙΑ Ε.Ε.（GR + CY；Westermo Reseller；R. STAHL 名录）官网部分坐实（ΓΕΜΗ 待补）；合伙微型 → 观察档；info@netap.gr'),
    'XC-M147': dict(verdict='pool_watch', star='☆', group=MAIN, company='International Trade Carrier, LLC', country='美国', links='internationaltradecarrier.com', tags=['industrial', 'reg_pending'],
                    reason='☆ 电子元件 / 电源 B2B 批发采购 20%：International Trade Carrier, LLC（Bethesda MD；EtherWAN 授权）官网部分坐实（州注册号待补）；主区 US 但元件批发口径、仅 info@ → 观察档'),
    'XC-M116': dict(verdict='pool_watch', star='☆', group=EU, company='QL3D', country='法国', links='ql3d.fr', tags=['industrial', 'reg_pending'],
                    reason='☆ 工业 / 交通 / 数据中心网络方案分销 20%：QL3D（Bazainville 78；HW group 法国独家；HMS Red Lion / N-Tron；联系人 Ludovic Debôves）名录部分坐实（SIREN 待补）；小型 → 观察档；info@ql3d.fr'),
    'XC-E059': dict(verdict='pool_watch', star='☆', group=EU, company='Alyseo', country='法国', links='alyseo.com | infra.alyseo.com', tags=['dc', 'reg_pending'],
                    reason='☆ 存储 / 虚拟化 / 基础设施集成商 25%：Alyseo（Saint-Sébastien-sur-Loire；Nexenta 伙伴；Edgecore 经销商名录）官网部分坐实（SIREN 待补）；数据中心对位一般（存储为主）→ 观察档；contact@ / sales@alyseo.com'),
    'XC-M083': dict(verdict='pool_watch', star='☆', group=EU, company='Aspect（Skopje）', country='北马其顿', links='aspect.com.mk', tags=['industrial', 'prepay', 'reg_pending'],
                    reason='☆ 自动化方案 / 计算机设备分销 20%：Aspect（Skopje Orce Nikolov 190/3-1；20–49 人 / $1–5M）官网 + ZoomInfo 部分坐实（法人全名 / ЕМБС 待补）；Westermo Reseller；非 EU → 预付 100%；观察档；office@aspect.com.mk'),
    # ---- 留 C（有邮箱 → 群发可用，但对位 / 体量 / 形态不够入池）----
    'XC-M106': dict(verdict='keep_C', reason='留 C：SECOMP a.s.（Praha；IČO 25141228；1997）坐实但主业消费电子零售 / 批发（pcplus.cz）→ 对位弱；邮箱已补 secomp@secomp.cz，随群发节奏', tags=['email_found']),
    'XC-C1467': dict(verdict='keep_C', reason='留 C：HON Security and Fire Distribution GmbH（Köln；HRB 114529；GF Sven Kniesche）坐实但 2023 起专做 Esser（Honeywell）火灾报警 / 应急照明 → 交换机对位弱；邮箱已补 info@fire-distribution.de', tags=['email_found']),
    'XC-M128': dict(verdict='keep_C', reason='留 C：FRINETA, UAB（Kaunas；235738890；2001）坐实但 2–3 人网络安装商 → ≤5 人安装商不入池；邮箱已补 info@frineta.lt', tags=['email_found', 'micro']),
    'XC-M130': dict(verdict='keep_C', reason='留 C：S.C. ELTREC POWER SRL（București；CIF RO37513951；J40/6436/2017）坐实但一人公司（元件 / 传感器 / Red Lion）→ 微型；邮箱已补 george.barbalata@eltrec.ro', tags=['email_found', 'micro']),
    'XC-M129': dict(verdict='keep_C', reason='留 C：Atys-co Romania S.R.L.（Cluj-Napoca + București；1–10 人；电源 / 传感 / 工业调制解调器）微型 —— 匈牙利 ATYS-CO Kft（XC-M082 ★）同系；邮箱已补 cluj@ / bucuresti@atysco.ro，随主档节奏', tags=['email_found', 'micro']),
    'XC-M108': dict(verdict='keep_C', reason='留 C：StarNet（Chișinău；摩尔多瓦主要 ISP / 电信运营商，501–1000 人）—— 运营商采购走招标，「巨头运营商」口径不入池；邮箱已补 clientbusiness@starnet.md', tags=['email_found', 'giant']),
    'XC-M175': dict(verdict='keep_C', reason='留 C：Diamond Technologies, Inc.（Hudson MA；11–50 人）已被 Beacon EmbeddedWorks 收购 → 采购主体在变，仅 info@；邮箱已补 info@diamondt.com，观察母公司后再定', tags=['email_found']),
    'XC-M183': dict(verdict='keep_C', reason='留 C：Westbase Networks / Westbase.io（Caldicot NP26 + NL）4G/5G / IoT / XR 行业分销（Netonix 官方）→ 蜂窝为主、交换机对位一般；邮箱已补 info@ / sales@westbase.io', tags=['email_found']),
    'XC-E064': dict(verdict='keep_C', reason='留 C：Telcaria Ideas S.L.（Madrid，国别修正 PT→ES）应急通信 / 5G / NFV-SDN 咨询开发 → 服务型微型，对位弱；邮箱已补 info@telcaria.com', tags=['email_found', 'micro']),
    'XC-C0089': dict(verdict='keep_C', reason='留 C：IP Phone Warehouse（Milwaukee WI）VoIP 电话电商 + 代发货履约 → 电商 / drop-ship 形态不入池；邮箱已补 service@ipphone-warehouse.com', tags=['email_found']),
    'XC-M150': dict(verdict='keep_C', reason='留 C：Platinum Micro, Inc.（Van Nuys CA；2000 起电脑系统零售 + 网络安装；CEO Bobby Sirichalermchai）微型零售；邮箱已补 sales@platinummicro.com', tags=['email_found', 'micro']),
    'XC-M088': dict(verdict='keep_C', reason='留 C：Planet Shop（希腊 PLANET 区域授权转售小店；Skroutz 评价沟通差）微型；邮箱已补 info@planet-shop.gr', tags=['email_found', 'micro']),
    # ---- 留 C（一次检索仍无直接邮箱 → 止）----
    'XC-M173': dict(verdict='keep_C', reason='留 C：Consyst Limited（Edgware；2006；1–10 人；Director Lior Golani）公开页只有邮箱格式、无直接邮箱 → 路径仍未建（官网表单），一次检索即止', tags=[]),
    'XC-M162': dict(verdict='keep_C', reason='留 C：Synergy Micro Solutions, LLC（Richardson TX；EtherWAN 授权；President & CEO Clive Berman）公开页只有邮箱格式 → 路径仍未建（官网表单），一次检索即止', tags=[]),
    'XC-M123': dict(verdict='keep_C', reason='留 C：Profibus Ireland Ltd（Limerick）一次检索未中（profibus.ie 无结果页）→ 路径仍未建，止', tags=[]),
}
COUNTRY_FIX = {'XC-E064': ('ES', '西班牙')}


def main():
    fill = json.load(open(FILL, encoding='utf-8'))['rows']
    assert set(fill) == set(D), set(fill) ^ set(D)
    sieve = sieve_x.load_sieve()
    recs = {r['code']: (r, repo) for r, repo in sieve_x.load_xc()}

    # 1) 来源记录：邮箱 / 国别
    touched = collections.Counter()
    for repo, fn in REPO_FILE.items():
        p = os.path.join(DATA, fn)
        d = json.load(open(p, encoding='utf-8'))
        changed = False
        for r in d['records']:
            code = r.get('code')
            if code not in fill:
                continue
            emails = fill[code]['emails']
            have = {e['addr'].lower() for e in (r.get('emails') or [])}
            for e in emails:
                if e.lower() not in have:
                    r.setdefault('emails', []).append({'addr': e, 'status': f'公开·{BATCH} 补'})
                    r.setdefault('emails_live', []).append(e)
                    have.add(e.lower())
                    changed = True
                    touched['emails+'] += 1
            if emails:
                tag = f'邮箱已补（{BATCH} {DATE}）'
                fl = [x for x in (r.get('flags') or []) if x not in ('无可用邮箱', '缺联系')]
                if tag not in fl:
                    fl.append(tag)
                if fl != r.get('flags'):
                    r['flags'] = fl
                    changed = True
            if code in COUNTRY_FIX and r.get('iso') != COUNTRY_FIX[code][0]:
                r['iso'], r['country_zh'] = COUNTRY_FIX[code]
                changed = True
                touched['country_fix'] += 1
        if changed:
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # 2) 轻研究卡（只给有邮箱的；已有卡不覆盖）
    for code, f in fill.items():
        if not f['emails'] or research_store.get(code):
            continue
        r, repo = recs[code]
        v = D[code]
        research_store.put({
            'code': code, 'name': r['name'], 'round': BATCH, 'researched_at': DATE,
            'alive': f'{DATE} 检索命中官网 / 名录（在线）', 'summary': (f['legal'] or r['name']) + '：' + f['note'][:120],
            'type_final': (r.get('type') or '渠道') + ('；' + f['legal'] if f['legal'] else ''), 'size': '',
            'saga_line': 'Saga STI 工业 / SmartByte 商用 PoE' if 'dc' not in (v.get('tags') or []) else 'CENTEC 数据中心（敲门砖）+ SmartByte',
            'fit': v.get('reason', '')[:60], 'brands_seen': [],
            'contacts': {'email': f['emails'][0], 'email_status': f'官网 / 名录公开（{BATCH} 补路径）', 'kp': []},
            'evidence': [{'kind': '官网 / 名录', 'claim': w, 'quote': '', 'url': u, 'date': DATE} for w, u in f['facts']],
            'touch_status': f'未触达（路径 {DATE} 新补）', 'saga_overlap': '无', 'grade_final': 'C',
            'grade_reason_final': f'{BATCH} 补路径：{v["reason"][:110]}（等级不动，池位见 sieve_x）',
            'next_move': {'action': '不动', 'angle': {'pool': '已入 P 池 → 按巡检节奏首触', 'pool_watch': '观察档 → 试单后转正', 'keep_C': '留 C 储备，随群发节奏'}[v['verdict']]},
            'deep': False, 'notes': '；'.join(x for x in (f['legal'], f['addr'], f['reg'], f['phone']) if x),
        })
        touched['cards+'] += 1

    # 3) sieve_x
    for code, v in D.items():
        assert code in recs, code
        cur = sieve.get(code) or {}
        assert cur.get('batch') in ('X1-auto', 'X1-01', BATCH), (code, cur.get('batch'))
        gate = 3 if v['verdict'] in ('pool', 'pool_watch') else 1
        row = {'verdict': v['verdict'], 'gate': gate, 'rule': 'G3' if gate == 3 else 'G1', 'reason': v['reason'], 'date': DATE, 'manual': True,
               'repo': recs[code][1], 'origin': 'External', 'batch': BATCH,
               'facts': [{'what': w, 'url': u, 'date': DATE} for w, u in fill[code]['facts']]}
        if cur.get('batch') in ('X1-auto', 'X1-01') and cur.get('reason'):
            row['g1_reason'] = cur['reason']
            row['g1_batch'] = cur['batch']
        elif cur.get('g1_reason'):
            row['g1_reason'], row['g1_batch'] = cur['g1_reason'], cur['g1_batch']
        if v.get('star'):
            row['star'] = v['star']
        tags = list(v.get('tags') or [])
        if fill[code]['emails'] and 'email_found' not in tags:
            tags.append('email_found')
        if tags:
            row['tags'] = tags
        if fill[code]['emails']:
            row['emails'] = fill[code]['emails']
        sieve[code] = row
    cnt = sieve_x.save_sieve(sieve)

    # 4) 巡检表（幂等：按编号）
    with open(WATCH, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    header, body = rows[0], rows[1:]
    have = {r[0] for r in body}
    added = 0
    for code, v in D.items():
        if v['verdict'] not in ('pool', 'pool_watch') or code in have:
            continue
        body.append([code, v['star'], '正式' if v['verdict'] == 'pool' else '观察', v['company'], v['country'], v['group'], v['links'],
                     '、'.join(x for x in (v.get('tags') or []) if x != 'email_found'), DATE, NEXT_CHECK, CHECK_ITEMS,
                     f'来源：External/{recs[code][1]}；{v["reason"][:160]}'])
        added += 1
    with open(WATCH, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(body)

    # 5) 名册小节（幂等：按标记）
    marker = f'## External 并池 · 批 {BATCH}'
    md = open(ROSTER, encoding='utf-8').read()
    if marker not in md:
        pools = [(c, v) for c, v in D.items() if v['verdict'] == 'pool']
        watch = [(c, v) for c, v in D.items() if v['verdict'] == 'pool_watch']
        keep = [(c, v) for c, v in D.items() if v['verdict'] == 'keep_C']
        n_mail = sum(1 for f in fill.values() if f['emails'])
        lines = ['', marker + f'（{DATE}，正式 {len(pools)} / 观察 {len(watch)}）', '',
                 f'> 来源：External Clients「渠道型主体但路径未建」keep_C 户补邮箱（`data/external_clients/xc_path_fill_{DATE}.json`，每户一次检索）。'
                 f'54 户查到邮箱 {n_mail}；同轮顺带拿到官方注册号 / 页脚法人者按闸 2 / 闸 3 口径直接定：入池 ★ {sum(1 for _, v in pools if v["star"] == "★")} / ○ {sum(1 for _, v in pools if v["star"] == "○")}、'
                 f'观察 ☆ {len(watch)}、留 C {len(keep)}（其中有邮箱 {sum(1 for c, _ in keep if fill[c]["emails"])} 户随群发节奏）。'
                 f'`reg_pending` = 官网 / 名录法人名部分坐实、注册号待补；`civil_only` = 客户群含军用 / 轨交，只谈民用项目。巡检同表 `data/saga_clients/P池_巡检表_{DATE}.csv`，下次 {NEXT_CHECK}。',
                 '', '| 编号 | 档 | 公司 | 国家 | 区域组 | 来源库 | 标签 | 判语（摘） |', '|---|---|---|---|---|---|---|---|']
        for c, v in pools + watch:
            lines.append(f'| {c} | {v["star"]} | {v["company"]} | {v["country"]} | {v["group"]} | External/{recs[c][1]} | {"、".join(x for x in (v.get("tags") or []) if x != "email_found")} | {v["reason"][:140].replace("|", "｜")}… |')
        lines += ['', '留 C：' + '；'.join(f'{c} {(fill[c]["legal"] or recs[c][0]["name"])[:36]}（{v["reason"].split("：", 1)[-1][:46]}…）' for c, v in keep), '']
        open(ROSTER, 'a', encoding='utf-8').write('\n'.join(lines))

    print(BATCH, dict(collections.Counter(v['verdict'] + (v.get('star') or '') for v in D.values())), dict(touched), 'watch+', added, dict(cnt))


if __name__ == '__main__':
    main()
