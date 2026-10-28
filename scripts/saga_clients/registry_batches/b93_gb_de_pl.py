#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 93 批 · GB 4 户（Companies House 官方 officers 页 fetch_page ×4 + 取号 web_search ×1）+ DE 4 户 + PL 3 户（web_search 各一次）。T29-U88 同轮续做，2026-10-28。可重复运行。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 93
CH = 'https://find-and-update.company-information.service.gov.uk/company/'

# ---------------- GB 4（Companies House 官方） ----------------
put('SB-017', key='gb', batch=B, name='SECURITYTEC LIMITED（securitytec.co.uk；Coulsdon, Surrey）', iso='GB', fetched=F,
    source='GB · securitytec.co.uk/about-us 页脚（Company Number 05585047）+ Companies House officers 页（05585047）；同名陷阱 SECURITYTEC LTD 10186386（Manchester，2017-02 注销）',
    url=CH + '05585047/officers',
    number='05585047', status='Active', incorporated='2005-10-06', company_type='Private limited company',
    sic=['80200 安防系统服务（Hikvision 授权批发 HIK00006690；CCTV / 门禁 / 对讲 / 报警 + 自有标 PoE 交换机网店）'],
    address='Units 2 & 3 Redlands Centre, Redlands, Ullswater Industrial Estate, Coulsdon CR5 2HT（020 8660 5888）', accounts='有 charges 页（抵押 / 贷款记录存在，未展开）', accounts_due='未取', size_band='微型（0–9 人，Kompass）',
    officers=['Graham David Smith — Director（1959-09 生，2005-10-06 起）= 研究档 KP graham@securitytec.co.uk = 老板', 'Katie Ann Smith — Secretary（2005-12-01 起；家族）'], psc='未取（officers 页未含 PSC；两 Smith 大概率 100%）', charges='存在（页面有 Charges 标签）', prev_names=[],
    lines=['**夫妻店 20 年、老板 Graham Smith 本人 = 研究档 KP**；自有标 PoE 交换机已在网店（NTP3-GSW0802S）→ **OEM 30%：8/16 口 PoE 贴 Securitytec 标**替换现款',
           'Hikvision 授权批发 → 相机线不碰；只谈交换机',
           'GB 复盘：accounts_due 下轮补（overview 页）'],
    notes='第 93 批 GB 首户；PSC / accounts 下轮一次补齐。')
put('SB-041', key='gb', batch=B, name='TELCAM FIRE & SECURITY LTD（12383574；London W7）', iso='GB', fetched=F,
    source='GB · Companies House officers 页（12383574）：2 officers / 1 resignation',
    url=CH + '12383574/officers',
    number='12383574', status='Active', incorporated='2020-01-02', company_type='Private limited company',
    sic=['安防安装（Texecom 报警、门禁、CCTV、火灾报警 — 火灾主系统守界不供）'],
    address='5 Broadway Buildings, Boston Road, London W7 3TT', accounts='未取', accounts_due='未取', size_band='微型（1–5 人）',
    officers=['John Dhunay — Director（1969-05 生，2020-01-02 起，在任）', 'Rajinder Singh Dhunay — Director（2020-01-02 起，**2026-02-23 辞任**）'], psc='未取', charges='', prev_names=['Telcam Security Services Ltd（研究档）'],
    lines=['**Dhunay 家族安装商，2026-02 一名董事退出 → 现为一人公司** → 小项目集成商（目标客户序列末位），分销 20% 线一页纸即可',
           '火灾报警是其主业之一 → 守界：只谈 CCTV 配套 PoE，不碰火灾',
           'B 维持、年度复核'],
    notes='无需再查。')
put('SB-063', key='gb', batch=B, name='AVESTA (MANCHESTER) LTD（07964960；HiLook 授权分销）', iso='GB', fetched=F,
    source='GB · Companies House officers 页（07964960）：3 officers / 2 resignations；页面含 Charges 标签',
    url=CH + '07964960/officers',
    number='07964960', status='Active', incorporated='2012-02-24', company_type='Private limited company',
    sic=['安防产品分销（HiLook UK 授权分销；64 Waterloo Road, Manchester）'],
    address='64 Waterloo Road, Manchester（研究档）；董事通讯地址 6 Hasper Avenue, Manchester M20 1AX', accounts='未取', accounts_due='未取', size_band='微型（1–9 人）',
    officers=['Javid Aria — Director（1982-09 生，英国籍，2013-11-11 起在任）= 老板', 'Farima Aria — Director（阿富汗籍，2012-02-24 → 2013-12-12 辞任；家族）'], psc='未取', charges='存在（Charges 标签）', prev_names=[],
    lines=['**一人公司（Javid Aria）、HiLook（海康子品牌）授权分销** → 相机线是海康的，PoE 交换机可换 → 分销 20% 线：8/16 口 PoE 一页纸',
           '有 charges（抵押）→ 现金紧、看价格；T/T 50/50 坚持',
           'B 维持、年度复核'],
    notes='无需再查。')
put('SB-076', key='gb', batch=B, name='IST SURVEILLANCE LTD（11228236；London N5）', iso='GB', fetched=F,
    source='GB · Companies House officers 页（11228236）：1 officer / 0 resignations',
    url=CH + '11228236/officers',
    number='11228236', status='Active', incorporated='2018-02-27', company_type='Private limited company',
    sic=['82990 其他商业支持服务（研究档）；监控安装 / 转售'],
    address='Office 408, Screenworks, 22 Highbury Grove, London N5 2ER', accounts='账目截至 2025-04-30 应于 2026-01-31 前提交（研究档）', accounts_due='2026-01-31（上期）', size_band='微型（1 人）',
    officers=['Senay Huseyin Bozaci — Director（1980-01 生，英国籍，2018-02-27 起，唯一董事）'], psc='未取（唯一董事 → 大概率 100%）', charges='', prev_names=[],
    lines=['**一人公司、17 次推送 0 回复** → 底数已清：不再投入，`when=不动`',
           '若日后回信：唯一董事 Bozaci 即拍板人',
           'B 维持'],
    notes='17 次推送 0 回复 → 不动；本行只为底数完整。')

# ---------------- DE 4 ----------------
put('SB-027', key='de', batch=B, name='Mathias Gottensträter VoIPDistri.com（voipdistri.com；Halle (Westf.)）— 个体工商', iso='DE', fetched=F,
    source='DE · 1 次检索：firmenwissen / Creditreform（Rechtsform Gewerbebetrieb，1 Inhaber，Außenhandel / Import，WZ 47；Im Hagen 3, 33790 Halle）+ aihitdata（VAT DE814065254；CEO Mathias Gottensträter）+ XING（Unternehmer VoIP Distribution；MG-MediaStudio GF）+ 官网 B2B 门槛「Gewerbeschein oder Handelsregister notwendig」',
    url='https://www.firmenwissen.de/az/firmeneintrag/33790/4010155801/MATHIAS_GOTTENSTRAETER_VOIPDISTRI_COM.html',
    number='无 HRB（个体工商 Gewerbebetrieb）；USt-IdNr. DE814065254', status='Aktiv（官网 / 电商在线，2020 起 Kleinanzeigen Pro）', incorporated='≈2003–2010（VoIPphones.de 编辑 2003–2010 后创业）', company_type='Einzelunternehmen（个体）',
    sic=['VoIP / 网络产品增值分销（B2B 门槛）+ 工业通信（Teltonika、M12 交换机）；进口'],
    address='Im Hagen 3, 33790 Halle (Westfalen)（+49 5201 730030）', accounts='—（个体无公示）', accounts_due='—', size_band='微型（1 人 + 兼职）',
    officers=['Mathias Gottensträter — Inhaber / CEO（研究档 KP communication@voipdistri.com）= 老板'], psc='', charges='', prev_names=[],
    lines=['**一人 VoIP 分销、自营进口（Creditreform 标 Außenhandel/Import）** → 有进口经验、决策快 → 分销 20% 线：工业 M12 / DIN 轨 PoE（研究档「Elink 工业交换机、M12」）作第二货源',
           '个体 → 量小、信用线短 → T/T 预付坚持',
           'DE 复盘 3 月：看域名与 Kleinanzeigen 是否仍活跃'],
    notes='无 HRB 可查，底数到此为止。')
put('SB-077', key='de', batch=B, name='LivEye GmbH（HRB 44506 Wittlich；Föhren）— 移动视频监控塔制造商', iso='DE', fetched=F,
    source='DE · 1 次检索：liveye.com Impressum（HRB 44506 Amtsgericht Wittlich；USt DE321392908；GF Carsten Simons）+ online-handelsregister（2021-03-12 Simons 单独代表权）+ Creditreform（2025-09-25 新任 GF Markus Diederichs；关联 LivEye Beteiligungs GmbH HRB 46290）+ GIT-Sicherheit（≈95 人、5 地点 DACH + 波兰）+ Indeed（2018 创立；营收 €4.25–21.5M 区间）',
    url='https://www.liveye.uk/impressum-en/',
    number='HRB 44506（Amtsgericht Wittlich）；USt-IdNr. DE321392908；D-U-N-S 315185493', status='Aktiv', incorporated='2018（Indeed；HRB 登记年份未取）', company_type='GmbH（控股 LivEye Beteiligungs GmbH HRB 46290）',
    sic=['移动 / 临时视频监控塔自研自产（NSTR 订阅模式）；安防服务'],
    address='Europa-Allee 56b, 54343 Föhren（+49 6502 4034722）', accounts='Bundesanzeiger 未取', accounts_due='—', size_band='中型（≈95 人；营收 €4–21M 区间）',
    officers=['Carsten Simons — Geschäftsführer（创始人型 GF；研究档 KP info@）', 'Markus Diederichs — Geschäftsführer（**2025-09 起**；前 BDO Cyber Security；主推「自研 / 德国制造 / 主权」）', 'Marc Thurn — 曾任 GF（2022 Impressum，现已不列）'], psc='', charges='', prev_names=[],
    lines=['**产品公司（监控塔）→ PoE 交换机是塔内部件** → OEM / 部件采购 30% 线：工业级小口数 PoE（宽温、DIN）配塔；量稳定但要样机验证（付费样品）',
           '**2025-09 新 GF 主打「Souveränität made in Germany / 摆脱全球供应链」** → 对中国部件更挑 → 卖点写长期供货 + 固件 + 3 年保修，不提产地',
           'DE 复盘 3 月：Bundesanzeiger 2025 账目 + 是否再换 GF'],
    notes='95 人 = 本批 DE 最大户；B 维持，等回信再升。')
put('SB-090', key='de', batch=B, name='Adler ELREHA GmbH / Adler Security Systems（adlerss.com；Hockenheim）— 约旦 Elreha 集团', iso='DE', fetched=F,
    source='DE · 1 次检索：adlerss.com/contact（Adler ELREHA GmbH, Schwetzinger Str. 103, 68766 Hockenheim；美国 Adler Systems LLC, St Petersburg FL）+ about（自研 IP 相机，美 / 德 / 台 / 中设施）+ aeconline（2012 年并入约旦 Elreha 家族，联系人 Hashim Sholy，电话 +962）+ LinkedIn（2013 / 11–50 人）+ signalhire（Zain Sana Ullah = Operations Engineer）；HRB 号 1 次未取',
    url='https://adlerss.com/contact/',
    number='HRB 未取（Mannheim 法院；下轮 Northdata 直链「Adler ELREHA GmbH, Hockenheim」）', status='Aktiv（官网 2026 在线）', incorporated='2012 / 2013', company_type='GmbH（约旦 Elreha 集团子公司 + 美国 LLC）',
    sic=['IP / 热成像相机制造（自有品牌 Adler）；边境 / 市政 / 太阳能独立监控系统'],
    address='Schwetzinger Str. 103, 68766 Hockenheim', accounts='未取', accounts_due='—', size_band='小型（11–50 人）',
    officers=['Hashim Sholy — 集团联系人（Elreha，约旦）', 'Zain (Sana) Ullah — Operations Engineer（研究档 KP zain@adlerss.com）'], psc='', charges='', prev_names=[],
    lines=['**相机制造商（自有品牌）→ 交换机是系统部件**（研究档「ONV 工业 FS」）→ OEM 30% 线：工业 PoE / 光口交换机贴 Adler 标配太阳能独立站',
           '边境 / 政府项目为主 → 项目制、量不稳；军用 / 边防整机不碰（守界），只供通用交换机',
           'KP 是运营工程师（非采购）→ 技术切入：宽温、PoE 预算、SFP 兼容；DE 复盘 3 月补 HRB'],
    notes='HRB 1 次未取 → 下轮 Northdata 直链一次。')
put('SB-242', key='de', batch=B, name='Grothe GmbH（HRB 6442 Siegburg；Hennef）— 意大利 Urmet 集团德国子公司', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata（HRB 6442 Siegburg；2002-04-23 登记；资本 €1.5M；LEI 529900VY9SISWY0OKP81；2 GF + 2 ppa）+ implisense（2001-08-27 成立；VAT DE813326876；70 人 2023；资产 €9.38M 2023）+ wer-zu-wem / DDW / protector（1892 Köln 创立，1998 迁 Hennef，2001 起属 Urmet；GF Andreas Rosen；70–71 人；营收 €13–21M）',
    url='https://www.northdata.com/Grothe%20GmbH,%20Hennef/Amtsgericht%20Siegburg%20HRB%206442',
    number='HRB 6442（Amtsgericht Siegburg）；LEI 529900VY9SISWY0OKP81；USt-IdNr. DE813326876', status='Aktiv', incorporated='2001-08-27（GmbH；品牌 1892）', company_type='GmbH（意大利 Urmet S.p.A. 集团，€270–470M）',
    sic=['楼宇 / 安防技术制造与分销（门铃 / 对讲 / 2 线 IP / 报警 / CCTV）'],
    address='Löhestr. 22, 53773 Hennef (Sieg)（02242-8890-0）', accounts='Bundesanzeiger：资产 €9.38M（2023）；9 份年报在档', accounts_due='—', size_band='中型（70 人；营收 €13–21M）',
    officers=['Andreas Rosen — Geschäftsführer（**= 研究档 KP arosen@grothe.de**）', '第二 GF + 2 名 ppa（姓名未取）'], psc='Urmet（意大利）100%', charges='', prev_names=[],
    lines=['**研究档 KP 就是 GF 本人（Andreas Rosen）** → 一封信直达拍板人；但 **Urmet 集团子公司 → CCTV / 网络件可能集团统采（意大利）** → 只能试 OEM 30%：Grothe 标 PoE 交换机配其 IP 对讲 / CCTV 线',
           '130 年品牌、70 人、€1.5M 资本 → 稳定、付款好；量取决于集团是否放权',
           'DE 复盘 3 月：Bundesanzeiger 2024 账目 + GF 是否变动'],
    notes='集团子公司 → 不算守界（非同行制造交换机）；B 维持。')

# ---------------- PL 3 ----------------
put('SB-664', key='pl', batch=B, name='JM elektronik Sp. z o.o.（jm.pl；KRS 0000416117；Gliwice）— 元器件 / 自动化分销（ICP DAS）', iso='PL', fetched=F,
    source='PL · 1 次检索：bizraport / rejestr.io（KRS 0000416117；NIP 6312645365；REGON 242895943；登记 2012-04-03；资本 1,000,000 zł；营收 2025 58.5 mln zł / 2024 58.2 / 2023 64.1；利润 236 tys. zł；资产 32.4 mln zł；PKD 46.90.Z）+ rejestrkrs（Prezes Sławomir Jarosław Pieszczek；Wiceprezes Teresa Jadwiga Suchoń）+ automatykab2b（2009 起 ICP DAS 授权分销）+ jm.pl 公司数据页（D-U-N-S 422187464）',
    url='https://rejestr.io/krs/416117/jm-elektronik',
    number='KRS 0000416117 / NIP 6312645365 / REGON 242895943', status='Aktywna（2025 年报已提交 2026-06）', incorporated='2012-04-03（Sp. z o.o.；业务更早）', company_type='Sp. z o.o.（资本 1,000,000 zł）',
    sic=['46.90.Z 非专业化批发（电子元器件 + 工业自动化 ICP DAS；B2B 门户）'],
    address='ul. Karolinki 58, 44-100 Gliwice', accounts='2025：营收 58.5 mln zł、利润 0.24 mln、资产 32.4 mln（低利润率元器件分销）', accounts_due='2026-07（PL 惯例）', size_band='中型（营收 ≈58 mln zł ≈ $14M）',
    officers=['Sławomir Jarosław Pieszczek — Prezes Zarządu', 'Teresa Jadwiga Suchoń — Wiceprezes Zarządu'], psc='未取（rejestr.io 受益人页未读）', charges='', prev_names=[],
    lines=['**元器件广线分销（58 mln zł）、工业交换机走 ICP DAS（台湾）** → 大 broadline → B BIG：分销 20% 线、STI 工业 DIN 轨作第二货源，一页纸即可',
           '利润率 0.4% → 对价格极敏感、对账期有要求 → T/T 预付会被拒，量不大时不值得让步',
           'PL 复盘 7 月：2026 年报 + 是否仍挂 ICP DAS'],
    notes='研究档「inhand 的 试试跟进」→ 工业路由 / 交换机兴趣确认；B 维持。')
put('SB-1098', key='pl', batch=B, name='Zintronic Sp. z o.o.（zintronic.pl；KRS 0000690689；Białystok）— 自有品牌相机', iso='PL', fetched=F,
    source='PL · 1 次检索：rejestr.io / krs-pobierz / imsig（KRS 0000690689；NIP 9662114233；REGON 368007675；登记 2017-08-11；资本 5,000 zł；PKD 26.40.Z 消费电子生产；受益人 Marek Ziniewicz 4/5 股 + Dominika Talarczyk 1/5；最近 KRS 变更 2026-03-16 RDF）+ zintronic.pl 规则页（biuro@zintronic.pl；85 677 70 55）',
    url='https://rejestr.io/krs/690689/zintronic',
    number='KRS 0000690689 / NIP 9662114233 / REGON 368007675', status='Aktywna（2025 年报 RDF 2026-03）', incorporated='2017-08-11', company_type='Sp. z o.o.（资本 5,000 zł）',
    sic=['26.40.Z 消费电子生产（自有品牌 Zintronic 相机 / 录像机 / 套装；网店）'],
    address='ul. Karola Modzelewskiego 2, 15-535 Białystok', accounts='RDF 已提交（金额未读）', accounts_due='2026-07', size_band='微型–小型（估 5–15 人）',
    officers=['Marek Ziniewicz — Prezes Zarządu / 80% 股东 = 老板', 'Dominika Talarczyk — 20% 股东'], psc='Marek Ziniewicz 80% / Dominika Talarczyk 20%', charges='', prev_names=[],
    lines=['**自有品牌（PKD 生产类）+ 现供 Hasivo（深圳）PoE 交换机** → **OEM 30%：Zintronic 标 PoE 交换机一对一替代 Hasivo**（研究档「商业 PoE hasivo 的」）',
           '老板 Marek Ziniewicz 80% → 一人拍板；写 biuro@ 点名 Prezes',
           '资本 5,000 zł 微型 → MOQ 1 箱、T/T 预付；PL 复盘 7 月'],
    notes='建议：PL 第二 OEM 候选（Spacetronik 之后）。')
put('SB-270', key='pl', batch=B, name='FHU DAMIX Damian Marciniak（damixsat.pl；Kościan）— 个体 SAT/RTV 网店', iso='PL', fetched=F,
    source='PL · 1 次检索：damixsat.pl o-firmie / regulamin / polityka（FHU DAMIX，CEIDG 个体；ul. Balcera 40, 64-000 Kościan；NIP 698-162-04-19；REGON 386854875；2006 起）+ yellowpages / firmagodnazaufania（DAMIX Damian Marciniak；旧 NIP 6981560781 / REGON 300273697）+ 首页「akcesoria Spacetronik」',
    url='https://www.damixsat.pl/webpage/o-firmie.html',
    number='NIP 6981620419 / REGON 386854875（CEIDG 个体；另见旧登记 NIP 6981560781）', status='Aktywna（官网 2026-10 更新）', incorporated='2006', company_type='个体工商（CEIDG；FHU）',
    sic=['卫星 / RTV / 电脑配件网店 + 门店；Spacetronik 配件经销'],
    address='ul. Balcera 40, 64-000 Kościan（wielkopolskie）', accounts='—（个体）', accounts_due='—', size_band='微型（1–3 人）',
    officers=['Damian Marciniak — 业主'], psc='', charges='', prev_names=[],
    lines=['**个体网店、交换机只是配件** → 不再投入，分销 20% 一页纸也不必单发；`when=不动`',
           '它卖 Spacetronik（SB-092）配件 → 若 Spacetronik 做成 OEM，这类店会自动跟着卖',
           'B 维持'],
    notes='底数完整即可。')
print('b93 gb+de+pl 11 ok')
