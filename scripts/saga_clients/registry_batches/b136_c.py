# -*- coding: utf-8 -*-
"""第 136 批（T29-U118g，2026-10-29）—— **C 池三闸 · 闸 2 第十三批**：第 134–135 批「未坐实」11 户中有官网的 7 户，改走官网页脚 / About 页直取（fetch_page，每户 1 页）；其余 4 户（Bilimsa / NAZEMCO 无站、Tùng Lâm 无站、Signalizācija 网店）留待下轮。
结果：坐实 / 部分坐实 5（ORIGO 品牌站在营 ★、Conexpro = 捷克 Plzeň 品牌 ★ 国别纠偏 RU→CZ、Viễn Thông Thành Công ○、THUANAN Automation ○、Việt Long – G-NET 代理 ○）；坐实但非渠道 1（IT Group Kazakhstan = 软件公司）；域名错配 1（projexon.com = 商务咨询公司，非 CCTV）。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 136
F = '2026-10-29'
RU = '— 俄语区常规：英 / 俄稿、20 / 25 / 30；收款 / 物流路径待 Simon；FOB 深圳'
CZ = '— 捷克（欧洲）常规：英文稿、20 / 25 / 30 + T/T 50/50 + DAP 买方清关（CE / RoHS / REACH）；周二 / 周四 10–12 CET'
VN = '— 越南常规：英文 / 越南语稿、20 / 25 / 30 + T/T 50/50（微型预付 100%）+ FOB 深圳 / DAP 河内；Zalo / 微信可用；周二 / 周四 10–12 ICT'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


row('SC-1613', 'ru', 'ORIGO Networks（origo-networks.ru；**官网首页 2026-10-29 直取：自有品牌 ORIGO 全线 —— L3 交换机 OS5230P+/370W（24×2.5G PoE + 6×10G SFP+）、CCTV PoE 交换机（250 m 供电）、OS3228 / OS3254 L3 交换机 2025-09-11 取得通信设备合格证、Wi-Fi 6 Mesh 路由器 OWR3030AXM、10G 媒体转换器 OMCG03LC；新闻：2025-05-29 参展 COMPUTEX 2025、2025-09-09 与 Hadal Project 技术合作 = 在营且活跃**）；/contacts 404，ИНН 仍未取；Simon「自己的白色外壳 / 比较重要」', 'RU',
    'RU · 官网首页直取（产品线 / 新闻 2025）；ИНН 未取（联系页 404）；2026-10-29', 'https://origo-networks.ru/',
    '未取（ИНН 未查；品牌站在营坐实）', '营业中（新闻 2025-09）', '未取', '未取（ООО 待核）', '网络设备自有品牌（交换机 / 路由 / MC），俄罗斯', '未取（官网未列）', '中型（全线产品 + 参展 COMPUTEX）',
    [],
    '**俄罗斯 · 自有品牌商 OEM 30%（长线）：官网产品页找 sales@ / 采购后一页纸（STC-028GP $28 / STC-2224GP $86 / STC-424XGGPM-280W $198 中性包装 + 贴 ORIGO 牌；他们已有 2.5G L3 线 → 推 SmartByte / Marvell 管理线差异）' + RU + '**',
    'OEM 30%；P 池候选 ★ 长线（自有品牌 ✔ 活跃 ✔ 对位 ✔ Simon「比较重要」✔）；部分坐实（ИНН 未取）；收款待定。')
row('SC-2957', 'cz', 'Conexpro（conexpro.com；**官网 About / Contact 直取：Conexpro brand —— 面向 ISP / 安装商的全线网络配件品牌（PoE 交换机、SFP / SFP28 光模块、PoE 注入器、网线 / 跳线、机柜、电池、太阳能配件），3–5 年保修，分销 / 经销遍及捷克及他国；总部 Hřbitovní 1479/25, 312 00 Plzeň, Czech Republic（另列 Sídlo Daimlerova 6, 312 00 Plzeň）；info@conexpro.com；周一–五 08:30–17:00**）；法人（疑 i4wifi a.s.）/ IČO 未取；**表内「俄罗斯」→ 实为捷克 = 国别待 Simon 确认纠偏**；Simon 二筛「基本是全线帧田的」', 'CZ',
    'CZ · 官网 About + Contact 页直取（品牌 / 地址 / 邮箱 / 分销网）；IČO 未取；2026-10-29', 'https://conexpro.com/about',
    '未取（IČO 未查；法人疑 i4wifi a.s.）', '营业中（官网 2026）', '未取', '未取（品牌，法人待核）', 'ISP / 安装商网络配件自有品牌（比尔森）', 'Hřbitovní 1479/25, 312 00 Plzeň, Czech Republic', '中型（全线品牌 + 多国分销）',
    [],
    '**捷克（欧洲）· 自有品牌商 OEM 30%（长线）：info@conexpro.com 一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 / STC-4424GCPM $165 中性包装 + 贴 Conexpro 牌 + MOQ 1；帧田现供 → 推 SmartByte / Marvell 管理线差异）' + CZ + '**',
    'OEM 30%；P 池候选 ★ 长线（欧洲 ✔ 自有品牌 ✔ 已用中国 OEM ✔ 对位 ✔ 邮箱 ✔）；部分坐实（IČO 未取）；国别纠偏 RU→CZ 待 Simon；Simon 原「判定不行」可否决。')
row('SC-574', 'kz', 'ТОО «IT GROUP KAZAKHSTAN»（itgroup.kz；**官网直取：软件开发 / 网站 / CRM / ERP / AI / 外包公司，22 年、30+ 员工、5000+ 项目、CMS Magazine 哈萨克 Top 10 网站工作室；090000 РК, ЗКО, г. Уральск, ул. Гумара Караша 33/2；+7 (727) 364-53-77 = niac.kz БИН 151040005191 同址同名 ✔**）；表内 2022 RFQ「找 ONV 的商业管理交换机」有回 = 项目性采购', 'KZ',
    'KZ · 官网首页直取（业务 / 地址 / 电话）与 niac.kz БИН 151040005191 对上；2026-10-29', 'https://itgroup.kz/',
    '151040005191（БИН）', '在营（官网 2026）', '2015-10-07', 'ТОО', '软件开发 / 网站 / 外包（乌拉尔斯克）—— 非网络设备渠道', '090000 Уральск, ул. Гумара Караша 33/2', '小型（30+ 人）',
    ['Дудниченков Михаил Михайлович — 负责人（niac.kz）'],
    '**哈萨克斯坦 · 软件公司项目性采购：不主动；来询被动报价（STC-2224GP $86 / STC-4424GCPM $165）' + RU + '**',
    '坐实（БИН 对上）但非渠道（软件公司）→ 回 C 储备，不入池；收款待定。')
row('SC-1177', 'in', 'Projexon（projexon.com；**官网直取：projexon.com = 国际商务咨询 / 企业培训公司（Corporate Strategic Consulting、Oil & Gas 培训、客户含 NNPC 尼日利亚）—— 与表内「印度 CCTV 公司、R. Vignesh Director、WA 问 L2 / L3 交换机」完全不符 = 域名错配**）；Vignesh 真实公司 / 域名待 WA 追问', 'IN',
    'IN · 官网直取：projexon.com 为商务咨询公司，非该户；2026-10-29', '',
    '未取（域名错配，法人未明）', '未知', '未取', '未取', 'CCTV / 网络集成（印度；公司待明）', '未取', '未取',
    ['R. Vignesh — Director（表内 WA）'],
    '**印度 · 待坐实：WA 问 Vignesh 公司全名 / 网址 / GST 后再一页纸（STC-2224GP $86 / STC-4424GCPM $165）**',
    '域名错配 → 回 C 待 WA 追问公司名；印度先例 ✔ 决策人 ✔ WA 可达 ✔。')
row('SC-1606', 'other', 'Viễn Thông Thành Công（mangvienthong.com.vn；**官网直取：「Viễn Thông Thành Công – Giải Pháp Mạng Viễn Thông」；Lô số 04 - DV14 Khu Đô Thị Tây Nam Linh Đàm, Phường Hoàng Liệt, Quận Hoàng Mai, Hà Nội；inbox.thanhcong@gmail.com；8h–17h30；光缆总仓 + 3onedata MC / 光交换机 / 光模块 / 视频光端机 / ODF / 网线 / 防火墙 / 机柜分销 + 光缆熔接施工（2026 年 ADSS 工程贴）**）；法人全名 / MST 未取', 'VN',
    'VN · 官网首页直取（商号 / 地址 / 邮箱 / 产品线）；MST 未取；2026-10-29', 'https://mangvienthong.com.vn/',
    '未取（MST 未查；商号 + 地址坐实）', '营业中（官网 2026）', '未取', '未取（Công ty 待核）', '光 / 网络 / 电信设备分销 + 施工（河内 Hoàng Mai）', 'Lô 04 - DV14 KĐT Tây Nam Linh Đàm, Hoàng Liệt, Hoàng Mai, Hà Nội', '小型',
    [],
    '**越南 · 分销 20%：gmail 一页纸（STC-028GP $28 / STC-228GP $33 / STC-110XGE $65 / STI-280GE $46.6 + MOQ 1）；VC / 光模块本职线并行' + VN + '**',
    '分销 20%；P 池候选 ○（越南先例 ✔ 中国品牌 3onedata ✔ 对位 ✔ 邮箱 ✔）；部分坐实（MST 未取）。')
row('SC-1638', 'other', 'THUANAN – Automation Components Company（thuananvn.com.vn；**官网直取：工业自动化元件分销 —— M-System（R3 远程 I/O / 信号隔离）、Azbil Yamatake（记录仪 / 流量 / 差压变送器）、ASCO Numatic 电磁阀、Honeywell 燃烧控制；thuanan.sales1@gmail.com；0989 174 796**）；法人全名 / MST 未取（通名「Thuận An」无法经 masothue 指认）；表内：工业交换机 optone ✔', 'VN',
    'VN · 官网首页直取（商号 / 代理品牌 / 邮箱 / 电话）；MST 未取；2026-10-29', 'https://thuananvn.com.vn/home/',
    '未取（MST 未查；商号 + 品牌线坐实）', '营业中（官网）', '未取', '未取（Công ty 待核）', '工业自动化元件分销（越南）', '未取（官网首页未列）', '小型',
    [],
    '**越南 · 工业自动化渠道 25%：gmail 一页纸对标 optone（STI-280GE $46.6 / STI-288GPM $78.9 / STI-054GP + MOQ 1 + 付费样机）' + VN + '**',
    '渠道 25%；P 池候选 ○（越南先例 ✔ 工业自动化渠道对位 ✔ 中国工业品牌在用 ✔ 邮箱 ✔）；部分坐实（MST 未取）。')
row('SC-1983', 'other', 'Việt Long（vietlongtelecom.com；**官网直取：G-NET 河内分销 + 保修代理（「Đại lý PP & Bảo hành G-NET tại Hà Nội」，合作 Cty Hợp Nhất thietbiquang.net）；024 3551 1222 / 0966 100 110 / 0936 559 898；产品 G-NET 工业交换机 G-IES / G-IMS、PoE 交换机 GX-PES、MC G-UMC / HHD、Hikvision 摄像机**）；法人全名 / MST 未取（通名）', 'VN',
    'VN · 官网首页直取（商号 / G-NET 代理 / 电话 / 产品线）；MST 未取；2026-10-29', 'https://vietlongtelecom.com/',
    '未取（MST 未查；商号 + 代理身份坐实）', '营业中（官网 2024–）', '未取', '未取（Công ty 待核）', '网络 / 光设备分销（河内；G-NET 代理）', '未取（官网「Liên hệ」待取）', '小型',
    [],
    '**越南 · 分销 20%：gmail 换稿一页纸一次（零回应 → 仅一次；STC-028GP $28 / STI-280GE $46.6 对标 G-NET）' + VN + '**',
    '分销 20%；P 池候选 ○（越南先例 ✔ 中国 OEM 品牌 G-NET 代理 ✔ 对位 ✔）；部分坐实（MST 未取）；8 推 0 回。')

print('b136_c done')
