# -*- coding: utf-8 -*-
"""第 120 批（T29-U113，2026-10-29）第 2 段 16 户（ID 池 10 + BR 池前 6）—— 官方登记核实写入 registry。
ID 路径首测：AHU 不可 1 查；companieshouse.id / companyhouse.id 镜像给登记号 + 注册地址（1/10）；官网 contact 补地址；同名极多（PT Suryatama ×N）→ 以域名 / 联系人对齐，否则 未坐实；gmail / yahoo 无公司名 → 0 查（5/10）。
BR 路径首测：CNPJ = cnpj.biz / casadosdados / econodata / serasa 1 查即得（5/6；含法人、开业日、CNAE、Simples、地址、电话）；域名实体 ≠ 表内业务（SB-1090 新闻社）→ 误归属；同名 3 家无域名对齐（SB-1089）→ 未坐实。命中率为全部路径最高之一。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 120
F = '2026-10-29'
ID = '— 印尼常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 雅加达（买方清关；SDPPI / Postel 不声称）'
BR = '— 巴西常规：英文稿（可附葡语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（买方清关、进口税自理；Anatel 不声称）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ---------------- ID 池 10 ----------------
row('SB-050', 'PT Anugerah Artha Guna（pt-aag.co.id；**官网 contact：Sawangan Permai, Jalan Anggrek Blok B5 no.2, RT.03 RW.09, Depok 16519；另址 Jalan MPR 1, RT.03 RW.11, Jakarta Selatan 12430；marketing@pt-aag.co.id；+62 851-8282-8360（WA）；「Konsultan IT – Aplikasi – Jaringan」= IT / 应用 / 网络顾问**）；NIB / NPWP 1 查未得 → 部分坐实；表内 2011 年买过 12 台延长器（老客户）；KP gunawan@（研究档「见 Clients 表联系人」）', 'ID',
    'ID · 1 次检索：pt-aag.co.id/?page_id=57（Sawangan Permai, Jalan Anggrek Blok B5 no.2, Rt.03 Rw.09, DEPOK 16519；Jalan MPR 1 … Jakarta Selatan 12430；marketing@pt-aag.co.id；+62 851-8282-8360；Anugerah Artha Guna Konsultan IT – Aplikasi – Jaringan）；NIB 未得；2026-10-29', 'https://pt-aag.co.id/?page_id=57',
    '未取（NIB / NPWP 1 查未得）', '营业中（官网在）', '未取', 'PT', 'IT / 网络顾问与集成（德波 / 南雅加达）', 'Sawangan Permai, Jalan Anggrek Blok B5 no.2, RT.03 RW.09, Depok 16519, Indonesia', '小型',
    ['Gunawan — 联系人（研究档 / Clients 表；gunawan@pt-aag.co.id）= 收件人'],
    '**2011 老客户（延长器 12 台）+ IT 网络集成 → 集成商 25% B，回访一页纸一次（延长器不供 → STC-028GP $28 / STC-228GP $33 / STI-054GP + MOQ 1 + 付费样机；以 2011 成交为开场）' + ID + '**；再无回声 → 不动',
    '集成商 25%；回访一页纸一次（预付 100%）；部分坐实（官网地址 + 电话；法定名解出 PT Anugerah Artha Guna；NIB 未取）。')
row('SB-1100', 'IT Broadcast & Cyber Security Infra System（**gmail + 无域名 → 0 查**）— 印尼 IT / 广播 / 网络安全服务商 Firman Wahyudi（领英来源）；2023 年问购买渠道 / 印尼分销商 / 网站；对 bypass 系列回复有用', 'ID',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（2023）', '—', '个体 / 微型', 'IT / 广播 / 网络安全服务（印尼）', '未取', '微型',
    ['Firman Wahyudi — 负责人（研究档 KP；kosovaku@gmail.com）= 收件人'],
    '**主动问购买渠道 → 集成商 25% B，一页纸一次（bypass 不供明说 → STI-288DGGPM $137 / STI-154GP + MOQ 1 + 付费样机；直购 + 预付 100%）' + ID + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；0 查（gmail）。')
row('SB-115', 'PT. Catur Citra Wisesa（**companieshouse.id：登记号 182592；注册地址 Jl. Taman Harapan Baru Blok D 10/11, RT.003/022, Pejuang, Bekasi；PT 有限责任；状态 Active；领英：制药 / 化妆品 / 食品饮料生产机械与备件（采购、制造、改造），20+ 年，Gambir, Jakarta**）→ 坐实；KP Rizky Adi Prastanto（yahoo）；需求 5 电口带 PoE（设备自用）', 'ID',
    'ID · 1 次检索：companieshouse.id/catur-citra-wisesa（PT. Catur Citra Wisesa；registration number 182592；JL. TAMAN HARAPAN BARU BLOK D 10/11, RT.003/022, PEJUANG, BEKASI；Active）+ companyhouse.id（Business No. 43；同址）+ linkedin.com/in/catur-citra-wisesa-pt（Penyedia Mesin Produksi Farmasi, Kosmetik, Makanan dan Minuman；20 tahun；Gambir, Jakarta）；2026-10-29', 'https://companieshouse.id/catur-citra-wisesa',
    'AHU 登记号 182592（镜像）', '营业中（Active；领英在）', '未取（自述 20+ 年）', 'PT（Perseroan Terbatas）', '制药 / 食品机械与备件制造（勿加泗 / 雅加达）', 'Jl. Taman Harapan Baru Blok D 10/11, RT.003/022, Pejuang, Bekasi, Indonesia', '小型',
    ['Rizky Adi Prastanto — 联系人（研究档 KP；rizkyadips@yahoo.com）= 收件人'],
    '**机械设备商自用 DIN 5 口 PoE（口型明确）→ 集成商 25% B，一页纸一次（STI-054GP 一口价 + STI-154GP 备选 + 付费样机；设备随机配套 → 复购小量）' + ID + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；坐实（登记号 + 注册地址 + 领英业务）。')
row('SB-142', 'Airpo Wireless（airpo.co.id；**官网产品页在：PoE 交换机 SG1210FP「8-Port Gigabit PoE+ with 2 SFP」、自标 AP「Airpo W312」(Cloud Management)；hsairpo.co.id 经销名单：LANGITNET（Sidoarjo）、PT ILUFA ABADI INDONESIA（Mangga Dua Mall Lt.4 No.37B, Jakarta）、ARATECH COMPUTER (CV ARUNA MULTI COMPUTER)（Makassar）→ 自有品牌 + 经销网络；法人名 / 地址 1 查未得 → 未坐实**）；KP Janm（gmail）；表内「不咋喜欢工业品」；需求 2 光 8 PoE 长壳 / 8 PoE 管理 / 4 光 24 电', 'ID',
    'ID · 1 次检索：airpo.co.id/produk/poe-switch（SG1210FP 8-Port Gigabit PoE+ with 2 SFP Switch；130W）+ airpo.co.id/produk/index.html（Airpo W312 Ceiling AP；Cloud Management）+ hsairpo.co.id/hubungi-kami（LANGITNET Sidoarjo；PT ILUFA ABADI INDONESIA Mangga Dua Mall Jakarta；ARATECH COMPUTER Makassar）；法人 / 地址未得；2026-10-29', 'http://airpo.co.id/produk/poe-switch',
    '未取（法人 / NIB 1 查未得）', '营业中（产品页 + 经销名单在）', '未取', '未取（品牌方；PT 推定）', '自有品牌无线 / 网络设备（印尼；经销网络）', '未取', '小型',
    ['Janm — 联系人（研究档 KP；airpowireless@gmail.com）= 收件人'],
    '**自有品牌（Airpo）+ 商用口型明确 → 贴标 OEM 30% B，一页纸一次（STC-228GP $33 贴标 / STC-4424GCPM $165 / STC-2224GP $86 + MOQ + 付费样机；工业线不推）' + ID + '**；再无回声 → 不动',
    '贴标 OEM 30%；一页纸一次（预付 100%）；未坐实（品牌与经销网络在、法人 / 地址未得）。')
row('SB-179', '「CRISPY CREPES」/ Ade Tj（**yahoo + 公司名疑为微信名 → 0 查**）— 印尼客户（已加微信），问 SFP 兼容、工业 MC 反馈、要工业 16 / 24 口机 datasheet；2025-04 回「用锐捷」', 'ID',
    '0 查（yahoo + 主体不明）；2026-10-29', '', '0 查', '互动中（2025-04）', '—', '个人', '未知（印尼）', '未取', '个人',
    ['Ade Tj — 联系人（研究档 KP；adren_tj@yahoo.com；微信已加）'],
    '**主体不明 + 现用锐捷 → 不动（B 保留；微信只问一句公司 / 网站，答后补档再评）**' + ID, '不动（主体待核）；0 查。')
row('SB-203', 'PT. Suryatama（**gmail；1 查仅同名异业：PT. Suryatama Mitra Sejati（登记号 1431499，2023-04-10 成立，泗水仓储区）/ PT. Suryatama Indo Semesta（坦格朗，PP 编织袋）→ 均无网络业务、无 Dedi Suryo Nugroho → 未坐实**）；KP Dedi Suryo Nugroho（gmail，WA 已加）；2024-04 明确需求「4 光 16 电 2 层管理工业交换机」；18 次推送 1 次实质回复', 'ID',
    'ID · 1 次检索：companieshouse.id/suryatama-mitra-sejati（PT. Suryatama Mitra Sejati；1431499；Surabaya；10 April 2023）+ suryatamaindosemesta.co.id（PT. Suryatama Indo Semesta；Tangerang；jumbo bag）→ 均非目标；2026-10-29', '', '未取（同名异业，未对齐）', '未知', '未取', 'PT', '未知（表内工业交换机需求）', '未取', '小型（推定）',
    ['Dedi Suryo Nugroho — Mr.（研究档 KP；dedi.suryonugroho@gmail.com；WA 已加）= 收件人'],
    '**需求明确（4 光 16 电 L2 管理工业）+ 曾回复 → 集成商 25% B，一页纸一次（STI-244DGGPM $121 / STI-288DGGPM $137 一口价 + 付费样机；WA 同步）' + ID + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；未坐实（同名异业）。')
row('SB-382', 'Yusuf（akoe.yusuf@gmail.com；**无公司名 → 0 查**）— 兴趣工业光纤交换机；2024-06 / 2025-11 群发收件，无回复', 'ID',
    '0 查（gmail + 无公司名）；2026-10-29', '', '0 查', '未知', '—', '个人', '未知（印尼）', '未取', '个人',
    ['Yusuf（研究档 KP；akoe.yusuf@gmail.com）'],
    '**无公司 + 无回声 → 不动（B 保留）**' + ID, '不动（个人）；0 查。')
row('SB-414', 'Rolins（+62 852；**无邮箱 / 公司 → 0 查**）— 兴趣「FS 板子」；2025-06 问「12–24 SFP switch ready?」（全光口汇聚机，Saga 无对口商用款）', 'ID',
    '0 查（无邮箱 / 公司）；2026-10-29', '', '0 查', '互动中（2025-06）', '—', '个人', '未知（印尼）', '未取', '个人',
    ['Rolins（WA；研究档无邮箱）'],
    '**产品不对位（全 SFP 12–24 口）+ 无邮箱 → 不动（B 保留；WA 来询如可接受 STH-2C24XF-HSI $1,500 数据中心机再报）**' + ID, '不动（产品不对位）；0 查。')
row('SB-456', 'PT Panca Kumala Jaya（pancakumala.co.id / pancakumala.com；**官网：Ruko Golden Green No.8, Jl. Panjang (Arteri Kedoya), Jakarta Barat 11520；021-564 3366；customerservice.pkj@gmail.com；旧站 © 2011（Rukan Golden Green No.6；sales@pancakumala.com）；SMATV / IPTV + 安防门禁 + 3play 分销，DCN 交换机印尼渠道（S5750E-28X 等）**）；NIB 1 查未得 → 部分坐实；2025-10 回复带联系方式；KP 客服', 'ID',
    'ID · 1 次检索：pancakumala.co.id（Panca Kumala Jaya；Ruko Golden Green No.8. Jl. Panjang (Arteri Kedoya) Jakarta Barat-11520；021-5643366；customerservice.pkj@gmail.com）+ pancakumala.com/announcement/news（PANCA KUMALA JAYA, PT；Rukan Golden Green No.6；+62(21) 564 3366；sales@pancakumala.com；© 2011）+ /product/s5750e-28x-si（DCN）；NIB 未得；2026-10-29', 'http://www.pancakumala.co.id/',
    '未取（NIB / NPWP 1 查未得）', '营业中（官网在；2025-10 回复）', '≤ 2011', 'PT', 'SMATV / 安防 / 网络分销（西雅加达）', 'Ruko Golden Green No.8, Jl. Panjang (Arteri Kedoya), Jakarta Barat 11520, Indonesia', '小型',
    ['（客服 — 研究档 KP：customerservice.pkj@gmail.com / info@pancakumala.co.id；Attn: Purchasing / Product Manager）'],
    '**DCN 渠道分销商（含工业 DIN 品类页）+ 已回复 → 分销 20% B，一页纸一次（DCN 之下白牌 / 低价：STC-2224GP $86 / STC-4424GCPM $165 + STI-154GP / STI-288DGGPM；DCN 不点名；MOQ 1 + 付费样机）' + ID + '**；回信 → 加厚',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网地址 + 电话 + 起始年；NIB 未取）。')
row('SB-610', 'Ahmad Ariyanto（ahmadariyanto105@gmail.com；**无公司名 → 0 查**）— 要价格表等各种信息；2024-06 / 2025-11 群发收件，无回复', 'ID',
    '0 查（gmail + 无公司名）；2026-10-29', '', '0 查', '未知', '—', '个人', '未知（印尼）', '未取', '个人',
    ['Ahmad Ariyanto（研究档 KP；ahmadariyanto105@gmail.com）'],
    '**无公司 + 只要价表 → 不动（B 保留）**' + ID, '不动（个人）；0 查。')

# ---------------- BR 池前 6 ----------------
row('SB-1089', 'tpnet.com.br（**1 查三家同名、均未与域名对齐 → 未坐实**：① Timmers Tecnologia Ltda t/a「Tpnet Tecnologia」CNPJ 54.793.965/0001-08，Av. das Américas 4200 Bl 1 Sala 305, Barra da Tijuca, Rio de Janeiro 22640-907，2024-04-18 开业，CNAE 8020-0/01 电子安防监控（若为本户 → 2024 新壳红旗）；② TPNET Informática Ltda-ME CNPJ 31.258.395/0001-50，1986 年，状态 SUSPENSA；③ Tp Net（Reclame Aqui）CNPJ 16.679.928/0001-84**）；表内里约 +55 21 面向 ISP 的网络设备分销 / 电商（TP-Link）；KP Sanche；WA 无实质回复', 'BR',
    'BR · 1 次检索：econodata.com.br/consulta-empresa/54793965000108（Tpnet Tecnologia；Timmers Tecnologia Ltda；Avenida das Americas 4200 … Barra da Tijuca；fundada em 18/04/2024；N-8020-0/01）+ serasaexperian（TPNET INFORMATICA LTDA - ME；31.258.395/0001-50；1986；SUSPENSA）+ reclameaqui（Tp Net；16.679.928/0001-84）；域名未对齐；2026-10-29', 'https://www.econodata.com.br/consulta-empresa/54793965000108-TIMMERS-TECNOLOGIA-LTDA',
    '未取（候选 CNPJ 54.793.965/0001-08 / 16.679.928/0001-84，未对齐）', '未知（候选之一 2024 新壳）', '未取', 'Ltda（推定）', 'ISP 网络设备分销 / 电商（里约）', '未取（Rio de Janeiro, RJ）', '小型',
    ['Sanche — 联系人（研究档 KP；sanche@tpnet.com.br）= 收件人'],
    '**面向 ISP 的分销 / 电商 → 分销 20% B，一页纸一次（STC-2224GP $86 / STC-4424GCPM $165 / STC-110XGE $65 + MOQ 1 + 付费样机；葡语备注）' + BR + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；未坐实（三同名未对齐；新壳风险）。')
row('SB-1090', 'tramaweb.com.br（**域名实体 = Tramaweb Agência de Notícias Ltda，CNPJ 14.254.716/0001-20，Rua Cubatão 86, Conj 1007, Vila Mariana, São Paulo 04013-000；2011-08-15 开业；CNAE 6391-7/00 新闻社；资本 R$10,000；marcos@tramaweb.com.br；(11) 3388-3063；ATIVA → 新闻 / 公关公司（Grupo Trama），与表内「MC FS 自己的 logo、别人在卖他们的 MC」业务不符 → 误归属坐实**）；KP Fabio（fabio@tramaweb.com.br）；表内未跟进', 'BR',
    'BR · 1 次检索：jusbrasil.com.br/nome/tramaweb-agencia-de-noticias-ltda（CNPJ 14.254.716/0001-20；15/08/2011；Ativa；6391700 Agências de notícias；R$10.000,00；Rua Cubatao, 86, Conj 1007 Vila Mariana；marcos@tramaweb.com.br）+ econodata + serasaexperian（TRAMAWEB AGENCIA DE NOTICIAS LTDA - ME；ATIVA）；2026-10-29', 'https://www.econodata.com.br/consulta-empresa/14254716000120-tramaweb-agencia-de-noticias-ltda',
    'CNPJ 14.254.716/0001-20（域名实体）', 'ATIVA（新闻社）', '2011-08-15', 'Ltda - ME', '新闻 / 公关传播（圣保罗）— 非网络设备', 'Rua Cubatão 86, Conj 1007, Vila Mariana, São Paulo - SP 04013-000, Brazil', '微型（资本 R$10k）',
    ['Fabio — 联系人（研究档 KP；fabio@tramaweb.com.br；归属存疑）'],
    '**域名实体为新闻社、表内 MC 业务主体无法对应 → 不动（B 保留；误归属；Simon 若有 WA 只问一句公司 / 网站，答后重建档）**' + BR,
    '不动（误归属）；坐实（域名实体 CNPJ + 地址，业务不符）。')
row('SB-1137', 'Infotec Comércio de Equipamentos e Sistemas de Segurança Ltda（**CNPJ 05.590.805/0001-56（总部 São José/SC，2003-03-26 开业，ATIVA，Simples 2009 起；分支 0002-37 Florianópolis 2010-06-04）；sócia-administradora Ema Ines Rodriguez Rodriguez（2009-08-13 入股）；admin@infotecsistemas.com.br；(48) 4052-9066；联邦法院 TRF4 多起进口税 / PIS-Cofins 进口案（2015–2018）→ 直接进口商**）→ 坐实；S 邮箱 2024-06 三封来信要 8+2 / 16+2 / 24+2 PoE 价，Simon 当日报价；2024-11 再要工业非管理 4/8/16/24 价表；未成；KP Fabian Alonzo（gmail）', 'BR',
    'BR · 1 次检索：casadosdados.com.br/solucao/cnpj/…-05590805000156（INFOTEC COMERCIO DE EQUIPAMENTOS E SISTEMAS DE SEGURANCA LTDA；ATIVA；26/03/2003；SAO JOSE SC；ADMIN@INFOTECSISTEMAS.COM.BR；48 40529066；Simples 01/01/2009；EMA INES RODRIGUEZ RODRIGUEZ Sócio-Administrador 13/08/2009）+ cnpj.biz/05590805000237（filial Florianópolis；04/06/2010）+ jusbrasil 进口税诉讼列表；2026-10-29', 'https://casadosdados.com.br/solucao/cnpj/infotec-comercio-de-equipamentos-e-sistemas-de-seguranca-ltda-05590805000156',
    'CNPJ 05.590.805/0001-56（分支 0002-37）', 'ATIVA（Simples）', '2003-03-26', 'Ltda - ME', '安防设备与系统商贸（圣若泽 / 弗洛里亚诺波利斯，SC）', 'São José - SC, Brazil（分支 Florianópolis - SC）', '微型 / 小型（ME；Simples）',
    ['Fabian Alonzo — 联系人（研究档 KP；transivideo@gmail.com）= 收件人', 'Ema Ines Rodriguez Rodriguez — Sócia-Administradora（casadosdados 2026-10-29；admin@infotecsistemas.com.br 登记邮箱）'],
    '**直接进口商（进口税诉讼可证）+ 两次主动要价未成 → 分销 20% B，一页纸一次（再报 STC-028GP $28 / STC-2216GP / STC-2224GP $86 现价 + STI-280GE $46.6 工业非管理 + MOQ 1；葡语备注；以 2024-06 报价为开场）' + BR + '**；回信 → 加厚 / 升 A 候选',
    '分销 20%；一页纸一次（预付 100%）；坐实（CNPJ + 法人 + 开业日 + 进口记录）。')
row('SB-498', 'DTI Tecnologia Ltda - EPP（Daiken；daiken.com.br；**CNPJ 10.497.398/0001-77；Colombo/PR（库里蒂巴都会区）；2008-11-12 开业；ATIVA；CNAE 电子元器件制造 → 自有品牌电子制造商**）→ 坐实；需求 500 个 802.3af PoE injector（不供）；KP Oscar Yamawaki（技术负责人）；WA 6 次无实质回复', 'BR',
    'BR · 1 次检索：empresas.serasaexperian.com.br/consulta-gratis/DTI-TECNOLOGIA-LTDA-10497398000177（DTI TECNOLOGIA LTDA - EPP；10.497.398/0001-77；COLOMBO, PR；fundada em 12/11/2008；ATIVA；Fabricação de componentes eletrônicos）；2026-10-29', 'https://empresas.serasaexperian.com.br/consulta-gratis/DTI-TECNOLOGIA-LTDA-10497398000177',
    'CNPJ 10.497.398/0001-77', 'ATIVA', '2008-11-12', 'Ltda - EPP', '电子元器件制造（自有品牌 Daiken；科隆博 / 库里蒂巴，PR）', 'Colombo - PR, Brazil', '小型（EPP）',
    ['Oscar Yamawaki — 技术负责人（研究档 KP；oscar.yamawaki@daiken.com.br / oscar@daiken.com.br）= 收件人'],
    '**自有品牌电子制造商 + 500 pcs 量级询盘 → 贴标 OEM 30% B，一页纸一次（注入器不供明说 → STC-028GP $28 / STC-228GP $33 贴标 + 批量阶梯；MOQ + 付费样机）' + BR + '**；再无回声 → 不动',
    '贴标 OEM 30%；一页纸一次（预付 100%）；坐实（CNPJ + 开业日 + CNAE）。')
row('SB-512', 'Solus Tecnologia em Sistemas Ltda EPP（solustecnologia.com；**CNPJ 07.270.661/0001-86；Rodovia Demócrito Moreira 176, Subsolo, Fátima, Aracruz - ES 29192-243；2005-03-08 开业（自述 2000 起）；CNAE 电子安防 / 监控 / 车辆追踪 / 火警服务；(27) 3256-3002；financeiro@solustecnologia.com；ZoomInfo：CCTV / 门禁 / 结构化布线 / 电信安装**）→ 坐实；KP Eduardo；需求 2 光 6 PoE 大壳；WA 6 次无实质回复', 'BR',
    'BR · 1 次检索：cnpj.biz/07270661000186（Solus Tecnologia em Sistemas LTDA；07.270.661/0001-86；Rodovia Democrito Moreira 176 Subsl Subsolo Fatima Aracruz ES 29192-243；fundada em 08/03/2005；CNAEs 安防服务）+ zoominfo（176 R. Democrito Moreira, Aracruz；CCTV, access control, structured cabling；Since 2000）+ NF-e PDF（(27) 3256-3002；financeiro@solustecnologia.com；EPP）；2026-10-29', 'https://cnpj.biz/07270661000186',
    'CNPJ 07.270.661/0001-86', 'ATIVA（推定；NF-e 2022 在开）', '2005-03-08', 'Ltda - EPP', '电子安防 / CCTV / 布线集成（阿拉克鲁斯，ES）', 'Rodovia Demócrito Moreira 176, Fátima, Aracruz - ES 29192-243, Brazil', '小型（EPP）',
    ['Eduardo — 联系人（研究档 KP；eduardo@solustecnologia.com）= 收件人'],
    '**20+ 年安防集成商 + 口型明确（2 光 6 PoE）→ 集成商 25% B，一页纸一次（STC-228GP $33 一口价 + STC-2216GP 备选 + 付费样机；葡语备注）' + BR + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；坐实（CNPJ + 地址 + 开业日 + 电话）。')
row('SB-591', 'Elementu Engenharia e Integração Ltda（elementuengenharia.com.br；**CNPJ 14.458.461/0001-17；Rua Pedro José Laroca 1667, Jardim Santa Marta, Araraquara - SP 14808-300；2011-09-26 开业；ATIVA；CNAE 7112-0/00 工程服务；Sociedade Empresária Limitada；nfe@elementuengenharia.com.br**）→ 坐实；道路基础设施技术集成（HS-WIM 动态称重、龙门架 / 可变情报板；Ecovias do Araguaia）；阿里 RFQ「90W PoE Injector」（不供）；KP Carlos Gabriel Alonso；表内未跟进', 'BR',
    'BR · 1 次检索：empresas.serasaexperian.com.br/consulta-gratis/ELEMENTU-ENGENHARIA-E-INTEGRACAO-LTDA-14458461000117（14.458.461/0001-17；ARARAQUARA, SP；26/09/2011；ATIVA；Serviços de engenharia）+ econodata（Rua Pedro Jose Laroca, 1667 - Jardim Santa Marta, Araraquara - SP, 14.808-300）+ solutudo（nfe@elementuengenharia.com.br；Sociedade Empresária Limitada）；2026-10-29', 'https://www.econodata.com.br/consulta-empresa/14458461000117-elementu-engenharia-e-integracao-ltda',
    'CNPJ 14.458.461/0001-17', 'ATIVA', '2011-09-26', 'Ltda（Sociedade Empresária Limitada）', '道路基础设施 / ITS 工程集成（阿拉拉夸拉，SP）', 'Rua Pedro José Laroca 1667, Jardim Santa Marta, Araraquara - SP 14808-300, Brazil', '小型',
    ['Carlos Gabriel Alonso — 联系人（研究档 KP；carlos@elementuengenharia.com.br）= 收件人'],
    '**ITS 路侧集成商（机柜工业机天然对口）→ 集成商 25% B，一页纸一次（90 W 注入器不供明说 → STI-154GP / STI-288DGGPM $137 / STI-488DGGPM $147 + 付费样机；葡语备注）' + BR + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；坐实（CNPJ + 地址 + 开业日 + CNAE）。')
