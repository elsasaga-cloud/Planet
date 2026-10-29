# -*- coding: utf-8 -*-
"""第 133 批（T29-U118f，2026-10-29）—— **C 池三闸 · 闸 2 第十批**：闸 1 第 35 批（桶 ⑦ 首批）候选 3 户查底数（KR 1 / TR 2）。
路径：KR → namu.wiki 企业条目（法人名 / 设立日 / 本社 / 代表；사업자등록번호 未取，bizno 补查待）；TR → vknsorgula（VKN / NACE / 地址）+ 官网 / zoominfo / facebook（地址 / 规模 / 负责人）。
每户 1 查、depth 1。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 133
F = '2026-10-29'
KR = '— 韩国常规：英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳；KC 认证 Saga 无 → 由买方自理需如实说；周二 / 周四 10–12 KST'
TR = '— 土耳其常规：英文 / 土耳其语 WA 稿、20 / 25 / 30 + T/T 50/50（首单可预付 100%）+ FOB 深圳 / DAP 买方清关（CE / RoHS）；周二 / 周四 10–12 TRT'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 韩国 ----------------
row('SC-380', 'kr', '주식회사 이에프엠네트웍스 EFM NETWORKS CO., LTD. — ipTIME（iptime.com；**2001-08-07 设立；본사 경기도 용인시 기흥구 죽전로 15, 6층（보정동）；대표 김인；업종 통신·방송장비 및 부품 도매업；중소기업；韩国消费 / SOHO 路由器第一品牌（市场占有率压倒性）；路由器由深圳 ZIONCOM（合资关联）制造 = 已用中国 ODM**）；사업자등록번호 未取；表内：「CCTV，似乎是有洪瑞的 switch」；Simon「可以尝试多跟进一下」；无邮箱', 'KR',
    'KR · 1 次检索：namu.wiki EFM 네트웍스 条目（法人名 / 设立日 / 本社 / 代表 / 业种 / ZIONCOM 代工）；사업자등록번호 未取；2026-10-29', 'https://namu.wiki/w/EFM%20%EB%84%A4%ED%8A%B8%EC%9B%8D%EC%8A%A4',
    '未取（사업자등록번호 未查；法人名坐实）', '营业中（品牌在售）', '2001-08-07', '주식회사（Co., Ltd.）', '消费 / SOHO 网络设备自有品牌（龙仁）', '경기도 용인시 기흥구 죽전로 15, 6층 (보정동)', '大型（韩国第一路由器品牌；中小企业分类）',
    ['김인（Kim In）— 대표이사'],
    '**韩国 · 巨头品牌商 OEM 30%（长线）：官网找采购 / 合作邮箱后一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 中性包装 + 贴 ipTIME 牌 + MOQ 1；洪瑞现供 → Q-33 口径：默认只推 SmartByte / Marvell 管理线）' + KR + '**',
    'OEM 30%；P 池候选 ★ 长线（巨头自有品牌 ✔ 已用中国 ODM ✔ 韩国点名国 ✔ 对位 ✔；无邮箱 → 需先找路径）；部分坐实（사업자등록번호 未取）；Q-33 洪瑞现供待 Simon；KC 由买方自理。')

# ---------------- 土耳其 ----------------
row('SC-440', 'tr', 'İnterland Bilişim Teknolojileri Ticaret Limited Şirketi（表内「Interland Network & Security」；**VKN 4781181726；NACE 461401 = 计算机 / 软件 / 电子与电信设备批发代理；Namık Kemal Mah. Motif Sk. No:23 A, Ümraniye, İstanbul 34762；同区另有 Interland Group（interlandgroup.com；Tatvani Mah. Estergon Cad. Suryapı Exen Sit. F Blok Kat.11 No:161 Ümraniye 34764；info@interlandgroup.com；+90 216 70 975 34）— 与展会名片主体对应待 WA 确认**）；表内：Ady 展会加了 WhatsApp +90 533 833 8258，要多口商业级交换机', 'TR',
    'TR · 1 次检索：vknsorgula（VKN / NACE / 地址）+ interlandgroup.com 联系页（地址 / 邮箱 / 电话）+ yenifirma；2026-10-29', 'https://vknsorgula.net/4781181726',
    '4781181726（VKN）', '营业中（目录 2024 / 官网 2023）', '未取', 'Limited Şirketi', 'IT / 电信设备批发 + 网络安全集成（伊斯坦布尔 Ümraniye）', 'Namık Kemal Mah. Motif Sk. No:23 A, Ümraniye, İstanbul 34762', '小型（Ltd. Şti.）',
    ['（具名 KP 未取；WA 联系人在表）'],
    '**土耳其主区 · 分销 / 集成 20–25%：WA 一页纸一次（STC-2224GP $86 / STC-4424GCPM $165 / STC-228GP $33 + MOQ 1 + 付费样机；先确认法人名 = İnterland Bilişim）' + TR + '**',
    '分销 20% / 集成 25%；P 池候选 ○（土耳其主区 ✔ WA 可达 ✔ 具体需求 ✔ 坐实 ✔）；坐实（VKN；展会主体对应待 WA 确认）。')
row('SC-442', 'tr', 'MEPA Elektronik（mepaelektronik.com；**Sahabiye Mah. Otak Sk. No:41, Kocasinan / Kayseri 38010；+90 352 220 6678；弱电系统集成 15 年：CCTV、火灾探测、数据网络（结构化布线 + 可管理交换机）、对讲、卫星电视、智能家居；11–50 人；Co-Owner Eren Gül（zoominfo）**）；vergi no 未取；表内：Furkan；Ady 展会加了 WhatsApp +90 535 875 1129，要 4 / 8 / 16 / 24 口 PoE 交换机', 'TR',
    'TR · 1 次检索：mepaelektronik.com/data-network（业务）+ zoominfo（地址 / 电话 / 人数 / Co-Owner）+ facebook（Kayseri）；vergi no 未取；2026-10-29', 'https://www.zoominfo.com/c/mepa-elektronik/1333329689',
    '未取（vergi no 未查；官网 + 目录坐实）', '营业中（官网 / FB）', '未取（15 年经验 ≈ 2010）', '未取（疑 Ltd. Şti.）', '弱电 / 安防 / 网络集成（开塞利）', 'Sahabiye Mah. Otak Sk. No:41, Kocasinan, Kayseri 38010', '小型（11–50 人）',
    ['Eren Gül — Co-Owner', 'Furkan — 表内 WA 联系人'],
    '**土耳其主区 · 安防集成 25%：WA 一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2216GP / STC-2224GP $86 + MOQ 1 + 付费样机；土耳其语稿）' + TR + '**',
    '集成 25%；P 池候选 ○（土耳其主区 ✔ WA 可达 ✔ 具体口数需求 ✔ 决策人 Co-Owner 具名 ✔）；部分坐实（vergi no 未取）。')

print('b133_c done')
