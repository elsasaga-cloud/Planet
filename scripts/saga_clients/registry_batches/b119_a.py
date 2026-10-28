# -*- coding: utf-8 -*-
"""第 119 批（T29-U112，2026-10-28）第 1 段 30 户（MY 15 + VN 15）—— 官方登记核实写入 registry（MY 路径首测：SSM 号 经 experian / maukerja / 领英「Registration No」/ 官网页脚；VN 路径首测：MST 经 masothue / yellowpages.vn / thongtincongty / 官网页脚，命中率最高）。时限压缩版：字段精简。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 119
F = '2026-10-28'
MY = '— 马来西亚常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳（SIRIM 不声称；DAP 买方清关）'
VN = '— 越南常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（MIC 型号核准不声称；买方清关）'
US = '— 美国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 / DAP（买方清关；FCC 有、UL / NDAA / TAA 不声称）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ───────── MY 15 ─────────
row('SB-307', 'Saxco Marketing Sdn Bhd（saxco.com.my；**1995 年本地注册；总部 8 & 10, Jalan SS 4C/5, Taman Rasa Sayang, 47301 Petaling Jaya, Selangor；03-7880 2299；槟城 / 沙巴 / 古晋 / 马六甲 4 家姊妹公司；51–100 人；SSM 号 1 查未得 → 部分坐实**）— 全马安防产品分销商（CCTV 起家、报警 / 门禁 / 一站式）；KP Heng Lee Sun（Purchaser）主动问网络交换机；无跟进', 'MY',
    'MY · 1 次检索：saxco.com.my/find-us（HQ 8, Jalan SS 4c/5, Taman Rasa Sayang, 47301 PJ；03-7880 2299；PG / South / KCH / MLK 分公司）+ contact.page（incorporated in the year of 1995）+ jobstreet（51-100 employees；Distributor of all kinds of security products）；SSM 号未得；2026-10-28', 'https://saxco.com.my/find-us',
    '未取（SSM 1 查未得）', '营业中（官网 2025）', '1995', 'Sdn Bhd（+ 4 家区域 Sdn Bhd）', '安防产品分销（Petaling Jaya）', '8, Jalan SS 4C/5, 47301 Petaling Jaya, Selangor, Malaysia', '中小（51–100）',
    ['Heng Lee Sun — Purchaser（研究档 KP；purchaser5@saxco.com.my）= 收件人（采购本人主动问）'],
    '**全马安防分销 + 采购本人主动问交换机、从未跟进 → 分销 20% B，一页纸一次（摄像机 PoE STC-028GP $28 / STC-228GP / STC-2216GP / STC-2224GP 一口价 + MOQ 1 + 付费样机；opener 引其来询）' + MY + '**；回信 → 加厚',
    '分销 20%；一页纸一次；部分坐实（官网 + 名录：成立年 + 总部 + 分公司；SSM 号未取）。')
row('SB-852', 'Alam Jaya Management（Thiruvaluvar Vajram；yahoo；**0 查**）— 展会谈 1+2+8 商用 PoE、问过 OEM；无跟进', 'MY',
    '0 查（yahoo + 公司名泛称）；2026-10-28', '', '0 查', '未核', '—', '未取', '未核（马来西亚）', '未取', '未取',
    ['Thiruvaluvar Vajram — 表内联系人（研究档 KP；thiru_vajram@yahoo.com）'],
    '**展会问过 OEM → 贴标 OEM 30% B small，一页纸一次（1 光 2 电 8 口 = STC-228GP 中性包装 / 贴标 MOQ 起订说明 + 付费样机；yahoo → 预付 100%）' + MY + '**；再无回声 → 不动',
    '贴标 OEM 30% small；一页纸一次（预付 100%）；0 查。')
row('SB-732', 'Maxitulin Sdn Bhd（maxitulin.com；**MATRADE 服务名录收录（系统集成）；总部 Unit 2-1, 1st Floor, Pusat Komersial Koi, Jalan Puchong Batu 13 1/2, 47100 Puchong, Selangor（旧址 No. 29, Jalan Puteri 5/16, Bandar Puteri）；+60 3 8062 2255；SSM 号 1 查未得 → 部分坐实**）— CCTV 供应 / 安装 / 维保 + 门禁 + 巡更；KP P. Kumar（Design Analyst Engineer）PoE 用量大、项目 Cisco / Aruba；无跟进', 'MY',
    'MY · 1 次检索：maxitulin.com/contact（Maxitulin Sdn Berhad；Unit 2-1, Pusat Komersial Koi, Jalan Puchong Batu 13 1/2, 47100 Puchong；603-8062-2255）+ malaysiaservices.matrade.gov.my/company-info/12184（MAXITULIN SDN BHD；System Integration）+ contact.page；SSM 号未得；2026-10-28', 'https://maxitulin.com/contact/',
    '未取（SSM 1 查未得）', '营业中（官网 + MATRADE 名录）', '未取', 'Sdn Bhd', '安防系统集成（Puchong）', 'Unit 2-1, Pusat Komersial Koi, Jalan Puchong Batu 13 1/2, 47100 Puchong, Selangor, Malaysia', '小型',
    ['P. Kumar — Design Analyst Engineer（研究档 KP；kumar@maxitulin.com）= 收件人（选型）'],
    '**安防 SI、PoE 用量大、工程师为 KP → 集成商 25% B，一页纸一次（STC-2216GP / 2224GP 摄像机 PoE + 室外箱 STI-154GP / STI-288DGGPM + 管理 STC-4424GCPM 一口价；bypass 不做明说；MOQ 1 + 付费样机）' + MY + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次；部分坐实（官网 + MATRADE 名录；SSM 号未取）。')
row('SB-1131', 'Mid-Atlantic Rugged Systems（marugged.com；**美国马里兰：95 Monocacy Blvd, Suite B18, Frederick, MD 21701；855-784-4334；<25 人；表内误归马来西亚 → country_fix 美国**）— 加固计算 / 工业网络 VAD（PLANET 授权分销专页、Moxa 10 年+、Teltonika / ATOP / Cincoze / Lanner）；无 KP（sales@）', 'US',
    'US · 1 次检索：marugged.com/teltonika（Mid-Atlantic Rugged Systems 95 Monocacy Blvd, Suite B18 Frederick, MD 21701；sales@marugged.com；855-784-4334；Shop By Brands Moxa / PLANET Technology / Teltonika …）+ zoominfo（Frederick, Maryland；<25 Employees）；州登记号未得；2026-10-28', 'https://marugged.com/teltonika/',
    '未取（MD 州登记 1 查未得）', '营业中（网店在）', '未取', 'LLC / Inc（未取）', '加固计算 / 工业网络分销（Frederick MD）', '95 Monocacy Blvd, Suite B18, Frederick, MD 21701, USA', '微型（<25）',
    ['（研究档无 KP：sales@marugged.com）'],
    '**原厂（PLANET / Moxa）授权分销 + 无 KP → 不动（B 保留；国别更正美国）**' + US,
    '不动（原厂授权分销）；部分坐实（官网 + ZoomInfo）；country_fix 美国。')
row('SB-366', 'TH IT Resource Centre Sdn Bhd（th-it.com；**页脚姊妹公司 TH IT Networks Sdn Bhd 198301012255 (107648-T)；No. 130, Jalan Kapar 27/89, Seksyen 27, 40400 Shah Alam, Selangor；+6016-280 3363；Ekahau 授权分销（Wi-Fi 设计）；本体 SSM 号 1 查未得 → 部分坐实**）— IT 设备短长期租赁（笔记本 / PC / 服务器 / 投影）+ 无线网络设计；KP Lee；表内「商业 PoE」；未跟进', 'MY',
    'MY · 1 次检索：th-it.com/services（TH IT RESOURCE CENTRE SDN BHD；TH IT NETWORKS SDN BHD 198301012255 (107648-T)；No. 130, Jalan Kapar 27/89, Seksyen 27, 40400 Shah Alam；+6016-280 3363；inquiry@th-it.com）+ th-it.com 租赁方案页（sister company … authorized Ekahau partner distributor；41, Jalan Pengeluaran U1/78, Hicom-Glenmarie）；2026-10-28', 'https://www.th-it.com/services/stag/13449/pc-rental-kuala-lumpur-malaysia/',
    '未取（本体；姊妹 198301012255 (107648-T)）', '营业中（官网在）', '姊妹 1983', 'Sdn Bhd', 'IT 设备租赁 + 无线网络设计（Shah Alam）', 'No. 130, Jalan Kapar 27/89, Seksyen 27, 40400 Shah Alam, Selangor, Malaysia', '小型',
    ['Lee — 表内联系人（研究档 KP；inquiry@th-it.com；职务待核）'],
    '**租赁 + Wi-Fi 设计、有商业 PoE 需求记录 → 集成商 25% B small，一页纸一次（AP 供电 STC-028GP / STC-2216GP / 2224GP 一口价 + MOQ 1 + 付费样机）' + MY + '**；再无回声 → 不动',
    '集成商 25% small；一页纸一次；部分坐实（官网页脚姊妹登记号 + 地址）。')
row('SB-729', 'HeiTech Padu Berhad（heitech.com.my；**Registration No. 199401024950 (310628-D)；Bursa Malaysia 主板上市 HTPADU；1995；HeiTech Village, Persiaran Kewajipan, USJ 1, 47600 UEP Subang Jaya, Selangor；+60 3 8601 3000；约 979 人 / 营收 $56.9M**）— 政府 / 企业 ICT 系统集成（SI、托管网络、数据中心）；KP Ts. Rizaki bin Napi（Cybersecurity Consultant）展会对工业 PoE 有兴趣；无跟进', 'MY',
    'MY · 1 次检索：linkedin.com/company/heitechpaduberhad（HEITECH PADU BERHAD Registration No: 199401024950 (310628-D)；public listed … Bursa Malaysia；Founded 1995）+ marketscreener AGM 纪要（Registration No. 199401024950 (310628-D)）+ rocketreach（HeiTech Village, Persiaran Kewajipan, USJ 1, UEP Subang Jaya 47600；+60 3-8601 3000；979 employees）；2026-10-28', 'https://www.linkedin.com/company/heitechpaduberhad',
    'SSM 199401024950 (310628-D)', '上市营业中（HTPADU）', '1994 / 1995', 'Berhad（上市公司）', '政府 / 企业 ICT 系统集成（Subang Jaya）', 'HeiTech Village, Persiaran Kewajipan, USJ 1, 47600 UEP Subang Jaya, Selangor, Malaysia', '大型（约 1,000）',
    ['Ts. Rizaki bin Napi — Cybersecurity Consultant（研究档 KP；rizaki@heitech.com.my；非采购）'],
    '**上市大型 SI、政府项目为主（守界）、KP 为安全顾问非采购、招标采购 → 不动（B 保留；企业项目来询按集成商 25% 报）**',
    '不动（大型招标 SI + 政府守界）；坐实（登记号 + 上市代码 + 地址）。')
row('SB-736', 'Sun Energy Enterprise Sdn Bhd（sunenergy.com.my；**SSM 800805-W；54-1, Jalan Metro Perdana Timur 9, Taman Usahawan Kepong, 52100 Kuala Lumpur；+60 3 6242 6818；<50 人**）— CCTV / 报警 / 停车场 / 门禁对讲 / SMATV / 考勤 / 网络与服务器 供应安装；MD Tan Chan Sun（陈先生，会中文）关心电源输入上限与防雷；无跟进', 'MY',
    'MY · 1 次检索：maukerja.my/en/company/sun-energy-enterprise-sdn-bhd（Company SSM No 800805-W；<50 Employees；54-1, Jalan Metro Perdana Timur 9, Taman Usahawan Kepong）+ facebook（+60 3-6242 6818；info@sunenergy.com.my）+ caricari（Wholesale & Retail；52100 Kuala Lumpur）；2026-10-28', 'https://www.maukerja.my/en/company/sun-energy-enterprise-sdn-bhd',
    'SSM 800805-W', '营业中（名录 + 社媒）', '未取（800805 ≈ 2008 段）', 'Sdn Bhd', '安防 / 弱电系统供应安装（Kepong KL）', '54-1, Jalan Metro Perdana Timur 9, Taman Usahawan Kepong, 52100 Kuala Lumpur, Malaysia', '小型（<50）',
    ['Tan Chan Sun（陈先生）— Managing Director（研究档 KP；chansun@sunenergy.com.my）= 拍板人 / 收件人（英文稿，不走中文直联）'],
    '**本地安防 SI、MD 本人为 KP、问题具体（电源输入上限 / 防雷）→ 集成商 25% B，一页纸一次（直接答：STI 导轨机 DC 输入范围与浪涌等级按规格书逐条给、STC-2216GP / 2224GP 摄像机 PoE 一口价 + MOQ 1 + 付费样机）' + MY + '**；回信 → 加厚',
    '集成商 25%；一页纸一次；坐实（SSM 号 + 地址 + 电话）。')
row('SB-790', 'Vulsan X（vulsanx.com；**59-2, Jalan MPK 3, Medan Perdagangan Kepayang, 70200 Seremban, Negeri Sembilan；06-851 5911；成立 2016-09-26（startup-asean）；11–50 人；法人名 / SSM 号 1 查未得 → 部分坐实**）— 网络安全 / AI 分析公司；KP Annamery Raja（OSINT Researcher）问过 PoE、在用知名品牌 24/48 口；无跟进', 'MY',
    'MY · 1 次检索：startup-asean.org（Vulsan X；59-2 JALAN MPK 3 MEDAN PERDAGANGAN KEPAYANG SEREMBAN；Founded 2016-09-26；11-50；Cybersecurity）+ bizmalay（06-851 5911）+ signalhire（Seremban 70200；10-50）；SSM 号未得；2026-10-28', 'https://startup-asean.org/startup-detail?Id=3a1bb4f9-e0d6-037e-0bda-3181b4fcc865',
    '未取（SSM 1 查未得）', '营业中（名录 ACTIVE）', '2016-09-26', 'Sdn Bhd（推定）', '网络安全 / AI（Seremban）', '59-2, Jalan MPK 3, Medan Perdagangan Kepayang, 70200 Seremban, Negeri Sembilan, Malaysia', '小型（11–50）',
    ['Annamery Raja — OSINT Researcher（研究档 KP；mery@vulsanx.com；非采购）'],
    '**非目标行业（安全服务）+ 硬件量小 + KP 非采购 → 不动（B 保留）**',
    '不动（非目标 + 量小）；部分坐实（名录：地址 + 成立日；SSM 号未取）。')
row('SB-734', 'Sigma Rectrix Systems (M) Sdn Bhd（sigmarectrix.com；**2003 年成立；Suite 3-05, 4805 CBD Perdana 2, Jalan Perdana, Cyber 12, 63000 Cyberjaya, Selangor；+60 3 8318 6696；MyCC（CyberSecurity Malaysia）认证防火墙产品开发商；SSM 号 1 查未得 → 部分坐实**）— ICT / IoT 集成 + 软件开发 + 培训（Ubiquiti 在用）；KP Mohamad Faiza bin Ismail（Pre-Sales Consultant）对 2 光 8 bypass 工业机有兴趣；无跟进', 'MY',
    'MY · 1 次检索：sigmarectrix.com/contactus（Sigma Rectrix Systems (M) Sdn Bhd；Suite 3-05, 4805 CBD Perdana 2, Jalan Perdana Cyber 12, Cyberjaya 63000；+60383186696）+ exabytes 伙伴页（founded in 2003；ICT and IOT integration）+ iscb.cybersecurity.my MyCC 认证产品页；SSM 号未得；2026-10-28', 'https://sigmarectrix.com/contactus',
    '未取（SSM 1 查未得）', '营业中（官网 + 认证库）', '2003', 'Sdn Bhd', 'ICT / IoT 集成 + 软件（Cyberjaya）', 'Suite 3-05, 4805 CBD Perdana 2, Jalan Perdana, Cyber 12, 63000 Cyberjaya, Selangor, Malaysia', '小型',
    ['Mohamad Faiza bin Ismail — Pre-Sales Consultant（研究档 KP；mohamadfaiza@sigmarectrix.com）= 收件人（售前选型）'],
    '**ICT / IoT 集成商、售前明确要 2 光 8 工业机 → 集成商 25% B，一页纸一次（STI-288DGGPM $137（2 光 8 电管理 PoE，无 bypass 明说）/ STI-488DGGPM $147 + 3 年保 + MOQ 1 + 付费样机）' + MY + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次；部分坐实（官网 + 伙伴页 + 认证库；SSM 号未取）。')
row('SB-733', 'Preciso Technology Sdn Bhd（precisotechnology.com.my；**2018-06 成立；48-2, Jalan PJU 5/20D, The Strand, Kota Damansara, 47810 Petaling Jaya, Selangor；+603 6151 2777；11–50 人；Volza 进口记录 10 票 / 4 家供应商；SSM 号 1 查未得 → 部分坐实**）— 电信同步 / 主时钟 / 数字时钟系统专家（代理 Albedo / Elproma / Gorgy / Protempis / Sapling；客户 运营商 / 金融 / 医院 / 轨交 / 学校）+ IoT 集成；KP C.S. Chong（张志祥，Senior Manager，会中文）问工业级 85 ℃；无跟进', 'MY',
    'MY · 1 次检索：precisotechnology.com.my/about-us（established in June 2018；Master Clock / Digital Clock；48-2, Jalan PJU 5/20D, The Strand, Kota Damansara, 47810 PJ；+603 6151 2777）+ volza（10 Bill of Ladings, 2 Buyers and 4 Suppliers）+ zoominfo（11-50）；SSM 号未得；2026-10-28', 'https://www.precisotechnology.com.my/about-us/',
    '未取（SSM 1 查未得；Volza 进口记录在）', '营业中（官网 2024）', '2018-06', 'Sdn Bhd', '电信同步 / 时钟系统 + IoT 集成（Kota Damansara）', '48-2, Jalan PJU 5/20D, The Strand, Kota Damansara, 47810 Petaling Jaya, Selangor, Malaysia', '小型（11–50）',
    ['C.S. Chong（张志祥）— Senior Manager（研究档 KP；cschong@precisotechnology.com.my）= 收件人（英文稿）'],
    '**专业集成商 + 进口商、高管为 KP、问题具体（85 ℃）→ 集成商 25% B，一页纸一次（直接答：STI 线 -40～75 ℃，85 ℃ 不做；STI-288DGGPM / STI-154GP 一口价 + 3 年保 + MOQ 1 + 付费样机）' + MY + '**；轨交项目不主动提；再无回声 → 不动',
    '集成商 25%；一页纸一次；部分坐实（官网 + 海关记录；SSM 号未取）。')
row('SB-002', 'Xspec Technology Sdn Bhd（xspec.com.my；**SSM 200501018493 (700608-K)；注册 2005-06-20；Selangor；No 8, Jalan Industri USJ 1/8, Taman Perindustrian USJ 1, Subang Jaya；+60 3 8023 1161；MD Sugito Wibawa；登记业务 无损检测设备贸易 / 工业化学品批发 / 管理咨询（experian，数据至 2026-10-04）**）— 制造商代表 / 分销（NDT、军警安防、医疗、生物实验室设备；马 / 印尼 / 新）；**表内 WhatsApp 跟进、有成单记录**', 'MY',
    'MY · 1 次检索：buy.experian.com.my（XSPEC TECHNOLOGY SDN. BHD. (200501018493 (700608-K))；Incorporation Date 20 June 2005；State SELANGOR；trading in non-destructive equipments …）+ abc-gcc（No 8, Jalan Industri USJ 1/8, Subang Jaya；+60-3-80231161；Managing Director Sugito Wibawa）+ newpages；2026-10-28', 'https://buy.experian.com.my/index.php/buy-report/malaysia-company/700608/xspec-technology-sdn-bhd',
    'SSM 200501018493 (700608-K)', '营业中（登记在 2026-10）', '2005-06-20', 'Sdn Bhd', '设备制造商代表 / 分销（Subang Jaya）', 'No 8, Jalan Industri USJ 1/8, Taman Perindustrian USJ 1, Subang Jaya, Selangor, Malaysia', '小型',
    ['Sugito Wibawa — Managing Director（研究档 KP；sugito@xspec.com.my；WA 在联）= 拍板人 / 收件人'],
    '**已成单客户（表内）+ MD 本人 KP + 21 年登记实体 → 分销 20% B（升 A 候选 ★）：复购一页纸（上次成交型号续单价 + 新品 STI-288DGGPM / STC-2224GP 一口价 + MOQ 1；WA 为主）' + MY + '**；回信 → 升 A；军警项目不主动提',
    '分销 20%（升 A 候选 ★，已成单）；复购一页纸；坐实（SSM 号 + 注册日 + 地址 + MD）。')
row('SB-746', 'Cybron System Sdn Bhd（cybron.com.my；**No 10, Jalan Alfa A, U6/A Pusat Perdagangan Subang Permai, 40150 Shah Alam, Selangor；03 7831 3883；Operations Manager Mohd Jamaluddin（ZoomInfo，2016 至今）；SSM 号 1 查未得 → 部分坐实**）— 安防系统方案（CCTV 为主）；KP Hussen 要 5 电口资料、实需带光口工业 PoE；WA 无实质回复', 'MY',
    'MY · 1 次检索：cybron.com.my/contact-us（CYBRON SYSTEM SDN BHD；No 10, Jalan Alfa A, U6/A Pusat Perdagangan Subang Permai, 40150 Shah Alam；sales@cybron.com.my；03 7831 3883）+ zoominfo（Mohd Jamaluddin Manager, Operations）+ fobshanghai 名录；SSM 号未得；2026-10-28', 'https://www.cybron.com.my/contact-us/',
    '未取（SSM 1 查未得）', '营业中（官网在）', '未取', 'Sdn Bhd', '安防系统集成（Shah Alam）', 'No 10, Jalan Alfa A, U6/A Pusat Perdagangan Subang Permai, 40150 Shah Alam, Selangor, Malaysia', '小型',
    ['Hussen — 表内联系人（研究档 KP；hussen@cybron.com.my）= 收件人', 'Mohd Jamaluddin — Manager, Operations（ZoomInfo）= 抬头抄送'],
    '**安防 SI、需求明确（带光口工业 PoE）→ 集成商 25% B，一页纸一次（STI-154GP（4 PoE + 1 GE + 1 SFP）/ STI-288DGGPM（8 PoE + 2 SFP 管理）一口价 + 3 年保 + MOQ 1 + 付费样机；邮件 + WA）' + MY + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次；部分坐实（官网 + ZoomInfo；SSM 号未取）。')
row('SB-052', 'excellent data communications（Wan Rohizal；gmail；**0 查**）— 小型网络工程商；需求 8 电口 + 4 光 6 电管理；2024-04 问 2 光 4 小壳样品', 'MY',
    '0 查（gmail + 无域名）；2026-10-28', '', '0 查', '未核', '—', '个体 / 小商户', '网络工程（马来西亚）', '未取', '个人',
    ['Wan Rohizal — 表内联系人（研究档 KP；wanrohizal501@gmail.com）'],
    '**个体 + gmail → 不动（B 保留；来询即按集成商 25% 报 STC-028GP / STI-154GP，付费样机，预付 100%）**',
    '不动（个体）；0 查。')
row('SB-628', 'BrightNet Services Sdn Bhd（bright.net.my；**No. 20-4-10, Jalan 2/101C, Cheras Business Centre, 56100 Kuala Lumpur；03-9130 9887；SSM 号 1 查未得 → 部分坐实**）— 一站式 SI（自动化 / 硬件 / 网络安防 / 现场支持；在售 Cisco / Aruba / Huawei / Ubiquiti 含翻新）；阿里巴巴询「光模块」（Saga 无）；KP Diana Wang（Inside Sales）；无跟进', 'MY',
    'MY · 1 次检索：contact.page / panpages（BrightNet Services Sdn. Bhd.；No. 20-4-10, Jalan 2/101C, Cheras Business Centre, 56100 KL；Tel 03-9130 9887；System Integrator / Automation Systems）；SSM 号未得；2026-10-28', 'https://www.panpages.my/listings/my740116-brightnet-services-sdn-bhd',
    '未取（SSM 1 查未得）', '营业中（名录）', '未取', 'Sdn Bhd', 'IT 系统集成 + 翻新设备（Cheras KL）', 'No. 20-4-10, Jalan 2/101C, Cheras Business Centre, 56100 Kuala Lumpur, Malaysia', '小型',
    ['Diana Wang — Inside Sales & Administrative（研究档 KP；diana.wang@bright.net.my；非拍板）'],
    '**需求 = 光模块（Saga 无）+ 原厂 / 翻新渠道 + KP 非拍板 → 不动（B 保留）**',
    '不动（需求不对位）；部分坐实（名录：法定名 + 地址 + 电话；SSM 号未取）。')
row('SB-912', 'jentronics（Tony；gmail；**0 查**）— 询盘表来源，无兴趣描述；WA 无实质回复', 'MY',
    '0 查（gmail + 无域名）；2026-10-28', '', '0 查', '未核', '—', '个人', '未核（马来西亚）', '未取', '个人',
    ['Tony — 表内联系人（研究档 KP；jentrx@gmail.com）'],
    '**个人 + 无需求描述 + WA×0 → 不动（B 保留）**', '不动（个人）；0 查。')

# ───────── VN 15 ─────────
row('SB-568', 'Tiên Phong CP（Trung；gmail semtec2017；**0 查**）— 需求 16 / 24 / 32 口 PoE；2025-11 / 12 收过 48 口 + 2+2 mini 邮件无回', 'VN',
    '0 查（gmail + 无域名）；2026-10-28', '', '0 查', '未核', '—', '未取', '未核（越南）', '未取', '未取',
    ['Trung — 表内联系人（研究档 KP；semtec2017@gmail.com）'],
    '**0 查 + gmail + 无回声 → 不动（B 保留；来询即按集成商 25% 报 STC-2216GP / 2224GP，预付 100%）**' + VN, '不动（0 查）；0 查。')
row('SB-1102', 'CÔNG TY TNHH VIỄN THÔNG GIÁ TỐT / GOOD PRICE TELECOMMUNICATIONS CO., LTD（vienthonggiatot.com；**MST 0109246393；2020-07-01 起营业；Thôn Tiên Kha, Xã Phúc Thịnh, Hà Nội；法人代表 Nguyễn Văn Đông；0963 508 809；两人以上有限公司；Đang hoạt động**）— 网络设备电商 + 弱电施工，站内按品牌卖 PLANET / TP-Link / Cisco / **HRUI 正品 PoE** / 工业交换机；无 KP（gmail 公用箱）', 'VN',
    'VN · 1 次检索：masothue.com/0109246393（CÔNG TY TNHH VIỄN THÔNG GIÁ TỐT；Mã số thuế 0109246393；Thôn Tiên Kha, Xã Phúc Thịnh, Hà Nội；Đang hoạt động；Người đại diện NGUYỄN VĂN ĐÔNG；Ngày hoạt động 2020-07-01）；2026-10-28', 'https://masothue.com/0109246393-cong-ty-tnhh-vien-thong-gia-tot',
    'MST 0109246393', 'Đang hoạt động（营业中）', '2020-07-01', 'Công ty TNHH 2 thành viên trở lên', '网络设备电商 + 弱电施工（Hà Nội）', 'Thôn Tiên Kha, Xã Phúc Thịnh, Hà Nội, Việt Nam', '微型（2020 新设）',
    ['Nguyễn Văn Đông — 法人代表（masothue）', '（研究档无 KP：vienthonggiatotvn@gmail.com）'],
    '**HRUI 在供（Q-33 口径待定）+ 2020 新壳 + 无 KP → 不动（B 保留；Q-33 定后若放开则按分销 20% 推 Marvell 管理线，预付 100%）**',
    '不动（Q-33 待定 + 新壳）；坐实（MST + 地址 + 法人代表 + 成立日）。')
row('SB-315', 'CÔNG TY TNHH THƯƠNG MẠI DỊCH VỤ SONG THÀNH CÔNG（STC Vietnam；stc-vietnam.com / songthanhcong.com；**MST 0309279999；2009 年成立；247/8B Hoàng Hoa Thám, P.5, Q. Phú Nhuận, TP.HCM；(028) 3507 4676；代表处 Thủ Đức；登记主业「消防设备批发」≠ 网站工业自动化（部分坐实 + 标记）**）— 工业自动化元器件贸易（Moxa / Advantech / NSD / E2S 等数十品牌；报价部 pricing@）；KP Mr. Linh（采购；表内注 MaiWe）/ Mr. Đức（Sales）2024 多次要价', 'VN',
    'VN · 1 次检索：masothue.com/0309279999（CÔNG TY TNHH THƯƠNG MẠI DỊCH VỤ SONG THÀNH CÔNG；247/8B Hoàng Hoa Thám, Phường 05, Quận Phú Nhuận；Đang hoạt động；Bán buôn các thiết bị phòng cháy, chữa cháy）+ yellowpages.vn（Mã số thuế 0309279999；Thành lập 2009；(028) 35074676；pricing@stc-vietnam.com）+ stc-vietnam.com/nha-san-xuat/moxa-1；2026-10-28', 'https://masothue.com/0309279999-cong-ty-tnhh-thuong-mai-dich-vu-song-thanh-cong',
    'MST 0309279999', 'Đang hoạt động（营业中）', '2009', 'Công ty TNHH（民营）', '工业自动化元器件贸易（登记 消防设备批发）（Phú Nhuận, HCMC）', '247/8B Hoàng Hoa Thám, P.5, Q. Phú Nhuận, TP. Hồ Chí Minh, Việt Nam', '小型',
    ['Mr. Linh — 采购（研究档 KP；linh@songthanhcong.com）= 收件人', 'Mr. Đức — Sales（研究档 KP；duc@stc-vietnam.com）= 抄送'],
    '**16 年工业品贸易商、采购多次要价、在供台系 + 国内工业机 → 分销 20% B，一页纸一次（STI-288DGGPM / STI-488DGGPM / STI-154GP 一口价 + 3 年保 + MOQ 1 + 付费样机；串口 MC 不做明说；不点名 Moxa / Maiwe）' + VN + '**；回信 → 加厚',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（MST + 地址 + 成立年；登记主业 ≠ 网站业务，标记）。')
row('SB-497', 'CÔNG TY TNHH CÔNG NGHỆ QUANG LÂM / QLC CO., LTD（quanglam.com.vn + wintop.com.vn；**MST 0310601970；发证 2011-01-22；开票地址 99/1 Huỳnh Văn Nghệ, P.12 (An Hội Tây), Gò Vấp, TP.HCM；交易办公室 / 仓库 160/1/67 Phan Huy Ích；(028) 3831 3119；CEO Hồ Lâm；NNT đang hoạt động**）— 光通信设备分销 + 制造（自产跳线 / 尾纤 / ODF；SFP / GPON / 交换机；**自有品牌 Wintop（MC 等）= 表内「有自己的 logo」**）；KP Hồ Lâm（CEO）；AOA 工业 FS 较多', 'VN',
    'VN · 1 次检索：yellowpages.vn（Công Ty TNHH Công Nghệ Quang Lâm；99/1 Đường Huỳnh Văn Nghệ, P. 12, Q. Gò Vấp；(028) 38313119；lamho@quanglam.com.vn；Mã số thuế 0310601970）+ wintop.com.vn/pages/thong-tin-lien-he（Công ty TNHH Công Nghệ Quang Lâm；MST 0310601970；văn phòng 160/1/67 Phan Huy Ích）+ thongtincongty.vn（Ngày cấp 22/01/2011；NNT đang hoạt động；Tên giao dịch QLC CO.,LTD）；2026-10-28', 'https://thongtincongty.vn/ma-so-thue/0310601970-cong-ty-trach-nhiem-huu-han-cong-nghe-quang-lam-474073398',
    'MST 0310601970', 'NNT đang hoạt động（营业中）', '2011-01-22', 'Công ty TNHH', '光通信设备分销 + 制造 + 自有品牌 Wintop（Gò Vấp, HCMC）', '99/1 Huỳnh Văn Nghệ, P. An Hội Tây (Gò Vấp), TP. Hồ Chí Minh, Việt Nam', '中小',
    ['Hồ Lâm (Ho Lam) — CEO（研究档 KP；lamho@quanglam.com.vn；黄页公开）= 拍板人 / 收件人'],
    '**15 年实体 + 自有品牌 Wintop + CEO 本人 KP + 已大量进口国内工业机 → 贴标 OEM 30% B（升 A 候选 ★），一页纸一次（Wintop 标 / 中性包装：STI-288DGGPM / STI-488DGGPM / STI-154GP 工业线 + STC-2224GP / 4424GCPM 商用线，MOQ 起订 + 付费样机；MC 仅 STC-110XGE 明说）' + VN + '**；回信 → 加厚 + 升 A',
    '贴标 OEM 30%（升 A 候选 ★）；一页纸一次（预付 100%）；坐实（MST + 发证日 + 两地址 + CEO）。')
row('SB-633', 'CÔNG TY CỔ PHẦN XUẤT NHẬP KHẨU VÀ THƯƠNG MẠI HOÀNG LONG（hlc.vn；**MST 0102354061；2007 年成立；Số 9B Nguyễn Gia Thiều, P. Trần Hưng Đạo, Q. Hoàn Kiếm, Hà Nội；(024) 3939 3737；31–50 人；ISO 9001**）— 电信 / IT / 工业网络 / 传输 / 自动化设备供应与安装 + **自述「专业生产工业交换机 / 光电转换器」= 自有品牌贴牌**；经销 Lantronix 工业 PoE；表内「和三旺有合作」；阿里巴巴询 16 槽收发器机架（Saga 无）；KP Hoang Nguyen Anh', 'VN',
    'VN · 1 次检索：trangdoanhnghiep.com（CÔNG TY CỔ PHẦN XUẤT NHẬP KHẨU VÀ THƯƠNG MẠI HOÀNG LONG；Số 9B Nguyễn Gia Thiều, Hoàn Kiếm；hlc@hlc.vn；(024) 39393737；Mã số thuế 0102354061；Năm thành lập 2007；31 – 50 người；ISO 9001）；2026-10-28', 'https://trangdoanhnghiep.com/cong-ty-co-phan-xuat-nhap-khau-va-thuong-mai-hoang-long/',
    'MST 0102354061', '营业中（名录 2024 + 官网）', '2007', 'Công ty Cổ phần（股份公司）', '电信 / 工业网络设备供应 + 自有品牌工业交换机（Hoàn Kiếm, Hà Nội）', 'Số 9B Nguyễn Gia Thiều, P. Trần Hưng Đạo, Q. Hoàn Kiếm, Hà Nội, Việt Nam', '小型（31–50）',
    ['Hoang Nguyen Anh — 表内联系人（研究档 KP；nguyenhoang@hlc.vn；职务未核）= 收件人'],
    '**自有品牌工业交换机（外购贴牌）+ 已与国内同行合作 → 贴标 OEM 30% B，一页纸一次（HLC 标 / 中性包装 STI-288DGGPM / STI-488DGGPM / STI-0240GE，MOQ 起订 + 付费样机；机架不做明说；不点名三旺）' + VN + '**；再无回声 → 不动',
    '贴标 OEM 30%；一页纸一次（预付 100%）；坐实（MST + 地址 + 成立年 + 规模）。')
row('SB-066', 'CÔNG TY TNHH CÔNG NGHỆ VÀ TRUYỀN THÔNG COMTEC（comtec.com.vn；**MST 0100774014；成立 1998-11-09；所有人 Vũ Thái Hải；登记地址 Số 9, ngách 45, ngõ 91 Nguyễn Chí Thanh, Láng Hạ, Đống Đa, Hà Nội（现办公 GoldSeason 47 Nguyễn Tuân）；(024) 3773 4926；主业 机械设备批发；黄页 2024-11 已验证**）— 电信设备与元器件批发（Viettel / MobiFone / VNPT 供应商；电源 / OTDR / 光模块 / 光缆配件 / 熔接机）；KP Cao Bá Duy（副总经理，公开）；无互动', 'VN',
    'VN · 1 次检索：congtydoanhnghiep.com（Công Ty TNHH Công Nghệ Và Truyền Thông Comtec；MST 0100774014；Thành lập 09-11-1998；Chủ sở hữu Vũ Thái Hải；Số nhà 9, ngách 45, ngõ 91 Nguyễn Chí Thanh；Bán buôn máy móc, thiết bị）+ yellowpages.vn（Được xác minh 25/11/2024；(024) 37734926）；2026-10-28', 'https://www.yellowpages.vn/lgs/720336/comtec-cong-ty-tnhh-cong-nghe---truyen-thong-comtec.html',
    'MST 0100774014', '营业中（已验证 2024-11）', '1998-11-09', 'Công ty TNHH', '电信设备 / 元器件批发（Đống Đa, Hà Nội）', 'Số 9, ngách 45, ngõ 91 Nguyễn Chí Thanh, Láng Hạ, Đống Đa, Hà Nội, Việt Nam', '中小',
    ['Cao Bá Duy — Phó Giám Đốc（研究档 KP；caobaduy@comtec.com.vn，黄页公开）', 'Vũ Thái Hải — 所有人（登记）'],
    '**27 年运营商供应商但产品线（电源 / 仪表 / 光模块 / 光缆）不对位 + 无互动 → 不动（B 保留；交换机来询按分销 20% 报，预付 100%）**',
    '不动（产品线不对位 + 无互动）；坐实（MST + 成立日 + 所有人 + 地址）。')
row('SB-367', 'CÔNG TY CỔ PHẦN MTS / MTS JSC（thuyluc.com；**MST 0101892941；发证 2006-03-20；Số 166 đường Tựu Liệt, Tam Hiệp, Thanh Trì, Hà Nội（门店 Kiốt 7 CT4C X2 Bắc Linh Đàm）；(024) 3641 6189**）— 液压设备（软管 / 阀 / 泵 / 油缸），非网络行业；表内 Lee 曾询 2 光 6 电非管理 SC 20 km（未成）', 'VN',
    'VN · 1 次检索：thuvienphapluat.vn（CÔNG TY CỔ PHẦN MTS；Tên quốc tế MTS JSC；Mã số thuế 0101892941；Ngày cấp 20/03/2006；Số 166 đường Tựu Liệt）+ trangvangvietnam（Kiốt 7 CT4C X2 Bắc Linh Đàm；(024) 36416189；Thiết Bị Thủy Lực；www.thuyluc.com）；2026-10-28', 'https://thuvienphapluat.vn/ma-so-thue/cong-ty-co-phan-mts-mst-0101892941.html',
    'MST 0101892941', '营业中', '2006-03-20', 'Công ty Cổ phần', '液压设备贸易（Thanh Trì, Hà Nội）', 'Số 166 đường Tựu Liệt, Tam Hiệp, Thanh Trì, Hà Nội, Việt Nam', '小型',
    ['Ly Thanh Ha (Lee) — 表内联系人（研究档 KP；hydraulics@vnn.vn）'],
    '**非目标行业（液压）+ 偶发需求 → 不动（B 保留）**', '不动（非目标行业）；坐实（MST + 发证日 + 地址）。')
row('SB-468', 'CÔNG TY TNHH SẢN XUẤT VÀ THƯƠNG MẠI NINH THANH / NINH THANH PRODUCTION AND TRADING CO., LTD（ninhthanh.com；**MST 0106778512；发证 2015-02-27；Số 20, ngách 24, ngõ 38, đường Xuân La, Xuân Đỉnh / Tây Hồ, Hà Nội；法人代表 VŨ ĐÌNH TƯ = 表内 KP Đinh Tú Vũ ✓；0904 550 273**）— 电信 / 数字化转型 / 数字地图 方案分销；阿里巴巴 RFQ「商业千兆 1 光 4 电」；KP Đinh Tú Vũ（CEO）；未跟进', 'VN',
    'VN · 1 次检索：thuvienphapluat.vn（CÔNG TY TNHH SẢN XUẤT VÀ THƯƠNG MẠI NINH THANH；NINH THANH PRODUCTION AND TRADING COMPANY LIMITED；Mã số thuế 0106778512；Ngày cấp 27/02/2015；Số 20, ngách 24, ngõ 38, đường Xuân La；Người đại diện VŨ ĐÌNH TƯ；0904550273）+ dulieuphapluat.vn；2026-10-28', 'https://thuvienphapluat.vn/ma-so-thue/cong-ty-tnhh-san-xuat-va-thuong-mai-ninh-thanh-mst-0106778512.html',
    'MST 0106778512', '营业中（已发 MST）', '2015-02-27', 'Công ty TNHH', '电信 / 数字化方案分销（Tây Hồ, Hà Nội）', 'Số 20, ngách 24, ngõ 38, đường Xuân La, Xuân Đỉnh, Hà Nội, Việt Nam', '小型',
    ['Đinh Tú Vũ (Vũ Đình Tư) — CEO / 法人代表（研究档 KP；dinhtu.vu@ninhthanh.com；登记吻合）= 拍板人 / 收件人'],
    '**CEO 本人发过 RFQ（1 光 4 电）、从未跟进 → 集成商 25% B small，一页纸一次（直接答：STI-154GP（4 PoE + 1 GE + 1 SFP）/ 商用 8+2 STC-228GP $33 一口价 + MOQ 1 + 付费样机；opener 引其 RFQ）' + VN + '**；再无回声 → 不动',
    '集成商 25% small；一页纸一次（预付 100%）；坐实（MST + 发证日 + 地址 + 法人代表 = KP）。')
row('SB-579', 'Công ty TNHH Nhất Nước (NNC)（nnc.net.vn；**MST 0101403703；2003 年成立；河内 Tòa G03 Căn 2412, Vinhomes Greenbay, 7 Đại Lộ Thăng Long, Nam Từ Liêm；024 3784 9934；义安省 Vinh 分厂 MST 0101403703-001**）— 电气设备制造 / 贸易 + 电站 / 变电站 / 线路建设安装 + 投资；KP Hoa（kinhdoanh8@）；询盘表来源、WA 无回复', 'VN',
    'VN · 1 次检索：hoainamgroup.com/gioi-thieu-cong-ty-tnhh-nhat-nuoc（Công ty TNHH Nhất Nước (NNC) thành lập từ năm 2003；Gia công chế tạo thiết bị điện；Xây dựng, lắp đặt (Nhà máy điện, trạm biến áp, đường dây)；Vinhomes Greenbay；ceo@nnc.net.vn；Mã số thuế 0101403703；Nghệ An 分厂）；2026-10-28', 'https://hoainamgroup.com/gioi-thieu-cong-ty-tnhh-nhat-nuoc/',
    'MST 0101403703', '营业中（集团页）', '2003', 'Công ty TNHH', '电气设备制造 + 电力工程（Hà Nội / Nghệ An）', 'Tòa G03 Căn 2412, Vinhomes Greenbay, 7 Đại Lộ Thăng Long, Nam Từ Liêm, Hà Nội, Việt Nam', '中小',
    ['Hoa — Kinh doanh（研究档 KP；kinhdoanh8@nnc.net.vn）'],
    '**电力工程为主（守界 电力）+ 无需求描述 + WA×0 → 不动（B 保留）**', '不动（电力守界）；坐实（MST + 成立年 + 地址，集团页）。')
row('SB-584', 'Vạn Phát Đạt（vanphatdat.vn / it-support.vn；**ĐKKD 0315053647，HCMC 计投局 2018-05-17 发证；26/37/6 Đường B3, P. Tây Thạnh, Q. Tân Phú, TP.HCM；028 6265 5310；河内代表处 Sannam Building 78 Duy Tân；Giám đốc Trần Minh Hùng = 表内 KP ✓**）— IT 外包 / Helpdesk / IT Onsite（24/7）；询盘表来源、WA 无回复（注：同名 Vạn Phát Đạt Group 富安省 MST 4400990704 为化肥 / 投资集团 ≠）', 'VN',
    'VN · 1 次检索：vanphatdat.vn/lien-he（Văn phòng Hồ Chí Minh 26/37/6 Đường B3, Phường Tây Thạnh, Quận Tân Phú；hungtran@vanphatdat.vn；Giấy chứng nhận Đăng ký Kinh doanh số 0315053647 … cấp ngày 17 tháng 05 năm 2018；Giám Đốc Trần Minh Hùng）；2026-10-28', 'https://vanphatdat.vn/lien-he/',
    'ĐKKD / MST 0315053647', '营业中（官网）', '2018-05-17', 'Công ty TNHH（推定）', 'IT 服务外包（Tân Phú, HCMC）', '26/37/6 Đường B3, P. Tây Thạnh, Q. Tân Phú, TP. Hồ Chí Minh, Việt Nam', '小型',
    ['Hùng Trần (Trần Minh Hùng) — Giám đốc（研究档 KP；hungtran@vanphatdat.vn；官网吻合）'],
    '**IT 服务商（非目标）+ 无需求 + WA×0 → 不动（B 保留）**', '不动（非目标行业）；坐实（官网自列登记号 + 发证日 + 地址 + 总监）。')
row('SB-634', 'CÔNG TY CỔ PHẦN THƯƠNG MẠI KỸ THUẬT HOÀNG THIÊN ÂN / HOANG THIEN AN TECHNOLOGY CORP（hoangthienan.com.vn，黄页列 hoangthienan.vn；**MST 0313394377；发证 2015-08-11；29 Đường DD11, P. Tân Hưng Thuận, Q.12, TP.HCM；法人代表 Lê Thị Kim Thoa；5–24 人**）— SFP / GPON SFP / Wintop MC / Cisco / EtherWAN / ORing / Huawei 贸易；自建站询「16 槽收发器机架」（Saga 无）；KP Anh Phan（Project Director）；无跟进', 'VN',
    'VN · 1 次检索：infodoanhnghiep.com（Công Ty Cổ Phần Thương Mại Kỹ Thuật Hoàng Thiên Ân；HOANG THIEN AN TECHNOLOGY CORP；MST 0313394377；Lê Thị Kim Thoa；cấp 11/08/2015；29 đường DD 11, Phường Tân Hưng Thuận, Quận 12）+ yellowpages.vn（Thành lập 2015；5-10 人；www.hoangthienan.vn）+ timviec365（10-24 人）；域名 .vn / .com.vn 差异，以法定英文名 + 地址对上；2026-10-28', 'https://infodoanhnghiep.com/thong-tin/Cong-Ty-Co-Phan-Thuong-Mai-Ky-Thuat-Hoang-Thien-an-94377.html',
    'MST 0313394377', 'Đang hoạt động（营业中）', '2015-08-11', 'Công ty Cổ phần', '网络 / 光通信设备贸易（Q.12, HCMC）', '29 Đường DD11, P. Tân Hưng Thuận, Q.12, TP. Hồ Chí Minh, Việt Nam', '微型（5–24）',
    ['Anh Phan — Project Director（研究档 KP；anhpt@hoangthienan.com.vn）= 收件人', 'Lê Thị Kim Thoa — 法人代表（登记）'],
    '**在售台系工业交换机的小贸易商、项目总监为 KP → 分销 20% B small，一页纸一次（STI-288DGGPM / STI-154GP 对位 + 3 年保 + MOQ 1 + 付费样机；机架 / SFP 不做明说；不点名 ORing）' + VN + '**；再无回声 → 不动',
    '分销 20% small；一页纸一次（预付 100%）；坐实（MST + 发证日 + 地址 + 法人代表；域名后缀差异已注）。')
row('SB-883', 'CÔNG TY TNHH VIỄN THÔNG PHƯƠNG DUNG / PHUONG DUNG TELECOM CO., LTD（phuongdung.com；**MST 0315321631；GCN 变更 2024-04-10（HCMC 计投局）；总部 40/14 Tân Thành, P. Tân Thành, Q. Tân Phú, TP.HCM；分支 岘港 / 西宁；法人代表 VĂN ĐỨC PHƯƠNG = 表内 KP ✓（另代表 Univision Việt Nam JSC、Sài Gòn New）；0989 865 766**）— 监控摄像机批发零售 + 安装（Vantech / KBVision / Hikvision / Dahua / Ezviz …；站内 ONV 交换机）；表内 1 次跟进无回复', 'VN',
    'VN · 1 次检索：masothue.com/0315321631（CÔNG TY TNHH VIỄN THÔNG PHƯƠNG DUNG；PHUONG DUNG TELECOM COMPANY LIMITED；40/14 Tân Thành, Phường Tân Phú；Đang hoạt động；Người đại diện VĂN ĐỨC PHƯƠNG）+ phuongdung.com 页脚（GCNĐKDN số 0315321631 Ngày Cấp 10/04/2024；Chi nhánh Đà Nẵng / Tây Ninh；Hotline 0989865766）；2026-10-28', 'https://masothue.com/0315321631-cong-ty-tnhh-vien-thong-phuong-dung',
    'MST 0315321631', 'Đang hoạt động（营业中）', '约 2018（MST 0315 段）；GCN 变更 2024-04-10', 'Công ty TNHH', '监控摄像机批发零售 + 安装（Tân Phú, HCMC；2 分支）', '40/14 Tân Thành, P. Tân Phú, TP. Hồ Chí Minh, Việt Nam', '小型',
    ['Văn Đức Phương — 负责人 / 法人代表（研究档 KP；info@phuongdung.com；登记吻合）= 拍板人 / 收件人'],
    '**三地摄像机分销 + 老板本人为法人代表 + 在售国内交换机 → 分销 20% B small，一页纸一次（摄像机 PoE STC-028GP $28 / STC-228GP / STC-2216GP 一口价 + MOQ 1 + 付费样机；不点名 ONV）' + VN + '**；1×0 在先 → 再无回声即不动',
    '分销 20% small；一页纸一次（预付 100%）；坐实（MST + 地址 + 法人代表 = KP + 分支）。')
row('SB-236', 'CÔNG TY TNHH GIẢI PHÁP CÔNG NGHỆ MINH PHƯỚC / MINH PHUOC SOLUTIONS TECHNOLOGY CO., LTD（congtyminhphuoc.vn；**MST 0313120792；成立 2015-01-30；11/31 Nguyễn Thái Sơn, P.3, Q. Gò Vấp, TP.HCM；官网自列**）— 电信设备 / 光跳线 / 光缆 / 摄像机 / 机柜 进口 + 生产分销；表内「从 BTON 买了很多」= 大量进口国内光产品；无具名 KP（tmphuocvn@gmail.com）；群发无互动', 'VN',
    'VN · 1 次检索：congtyminhphuoc.vn/kinh-nghiem-mua-sam（CÔNG TY TNHH GIẢI PHÁP CÔNG NGHỆ MINH PHƯỚC；Thành lập 30/01/2015；Mã Số Thuế 0313120792；11/31 Nguyễn Thái Sơn, Phường 3 quận Gò Vấp；MINH PHUOC SOLUTIONS TECHNOLOGY COMPANY LIMITED；tmphuocvn@gmail.com；nhà nhập khẩu và sản xuất phân phối）；同名 Cty TNHH Minh Phước 平顺省（油品）≠；2026-10-28', 'https://congtyminhphuoc.vn/kinh-nghiem-mua-sam',
    'MST 0313120792', '营业中（官网）', '2015-01-30', 'Công ty TNHH', '电信 / 光纤产品进口 + 生产分销（Gò Vấp, HCMC）', '11/31 Nguyễn Thái Sơn, P.3, Q. Gò Vấp, TP. Hồ Chí Minh, Việt Nam', '小型',
    ['（研究档无具名 KP：tmphuocvn@gmail.com 公用箱）'],
    '**真实进口商（同行大量采购）→ 分销 20% B small，一页纸一次（STC-228GP / STC-2216GP / STI-154GP 一口价 + MOQ 1 + 付费样机；MC 仅 STC-110XGE 明说；Attn: Purchasing）' + VN + '**；再无回声 → 不动',
    '分销 20% small；一页纸一次（预付 100%；无具名 KP）；坐实（官网自列 MST + 成立日 + 地址 + 英文名）。')
row('SB-876', 'LILIN Vietnam / Silversea HCM（lilin.vn / silverseahcm.vn；**1 查仅得同名异业（Silversea 水产 MST 4202007157、Silversea New Material 3801292166）→ 未坐实**）— 台湾 LILIN CCTV 越南分销商；表内「自己的 logo」「工业交换机」；无 KP（marketing@）；未跟进', 'VN',
    'VN · 1 次检索：thuvienphapluat / masothue 仅 CÔNG TY TNHH THỦY SẢN SILVERSEA（庆和省水产）与 SILVERSEA NEW MATERIAL（同奈省）— 均 ≠ 安防分销；lilin.vn 法人未得；2026-10-28', '',
    '未坐实（同名异业）', '未坐实', '未取', '未取', 'CCTV 品牌分销（HCMC，推定）', '未取（TP. Hồ Chí Minh）', '未取',
    ['（研究档无 KP：marketing@silverseahcm.vn）'],
    '**自有 logo + 工业交换机需求记录 → 贴标 OEM 30% B small，一页纸一次（中性包装 / 贴标 STI-288DGGPM / STC-2216GP，MOQ 起订 + 付费样机；Attn: Marketing / Purchasing；未坐实 → 预付 100%）' + VN + '**；再无回声 → 不动',
    '贴标 OEM 30% small；一页纸一次（预付 100%）；未坐实（同名异业，1 查止）。')
row('SB-958', 'Siêu Thị Viễn Thông（sieuthivienthong.com；**1 查得两同名候选：.com.vn = Công ty TNHH Kỹ Thuật Viễn Thông Thiên Long MST 0312485663（10 Bis Trường Chinh, Q.12, HCMC）/ .net = Công ty TNHH Siêu Thị Viễn Thông（27A Hoàng Việt, Tân Bình, HCMC）— .com 归属未定 → 部分坐实**）— 电信 / 安防 / 网络设备电商（Hikvision / Dahua / TP-Link / Ubiquiti；表内「商业 PoE 主要是 Hasivo 的」= 在卖深圳白牌）；无 KP（info@）；未跟进', 'VN',
    'VN · 1 次检索：sieuthivienthong.com.vn/gioi-thieu（Công Ty TNHH Kỹ Thuật Viễn Thông Thiên Long；Mã số thuế 0312485663；10 Bis Trường Chinh, P. Tân Hưng Thuận, Q.12）+ sieuthivienthong.net/lien-he（Công Ty TNHH Siêu Thị Viễn Thông；27A Hoàng Việt, P.4, Q. Tân Bình）；.com 对应方未定；2026-10-28', 'https://sieuthivienthong.com.vn/gioi-thieu/',
    '未定（候选 MST 0312485663 / 另一同名）', '营业中（电商在）', '未取', 'Công ty TNHH', '电信 / 安防设备电商（HCMC）', 'TP. Hồ Chí Minh（Q.12 或 Tân Bình，待定）', '微型',
    ['（研究档无 KP：info@sieuthivienthong.com）'],
    '**白牌 PoE 网店 + 无 KP + 归属未定 → 不动（B 保留）**', '不动（网店 + 无 KP）；部分坐实（两同名候选，域名归属未定）。')
print('b119 第 1 段 30 written')
