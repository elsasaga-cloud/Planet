# -*- coding: utf-8 -*-
"""第 117 批（T29-U110，2026-10-28）第 2 段 13 户（TH 第 8–19 户 12 + AE 第 1 户）—— 官方登记核实写入 registry（AE 路径首测：官网 contact 给 JLT 地址 + P.O. Box，牌照号 1 查未得）。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 117
F = '2026-10-28'
TH = '— 泰国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳（NBTC 不声称、由买方自办；DAP 买方清关）'
AE = '— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP 迪拜（买方清关；TDRA / ESMA 不声称、由买方自办）'

# ───────── TH 第 8–19 户 ─────────
put('SB-458', key='other', batch=B, name='SATS Digital（satsdigital.com；**最接近法人 บริษัท แซทดิจิตอล จำกัด SATDIGITAL CO., LTD. เลขทะเบียน 0105568002761；注册 2025-01-06；注册资本 ฿1,000,000；88/468 Kanlapaphruek Rd., Bang Khae, Bangkok 10160；登记业务 光纤 / 网络 / CCTV / Wi-Fi / 太阳能 / 门禁设备销售（与网店品类吻合）；网站未在登记页展示 → 部分坐实**；另有同名 หจก. แซทดิจิตอล ดอทคอม 0103557023531（2014 设、2015 注销））— **比价型网店（MC / FS / 工业 FS / SFP / VC「价格便宜」；站内 8 口千兆工业 PoE、Dahua PoE 页面）**；表内「可以尝试多跟进一下」；无 KP（info@）；9 次跟进无回复', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（บริษัท แซทดิจิตอล จำกัด SATDIGITAL CO., LTD.；ทะเบียน 0105568002761；จำหน่ายอุปกรณ์ระบบไฟเบอร์ออฟติก เครือข่ายใยแก้วนำแสง กล้องวงจรปิด ไวไฟ โซล่าเซลล์ … ระบบควบคุมการเข้าออก；ร้านขายปลีกอุปกรณ์การสื่อสารโทรคมนาคม；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 6 มกราคม 2568；ทุนจดทะเบียน 1,000,000 บาท；88/468 ถนนกัลปพฤกษ์ แขวงบางแค เขตบางแค กรุงเทพมหานคร 10160）+ creden（ห้างหุ้นส่วนจำกัด แซทดิจิตอล ดอทคอม 0103557023531；จดทะเบียน 24 ต.ค. 2557；วันที่เลิก 27 ม.ค. 2558）；域名 satsdigital.com 与法人名 SatDigital 近似、未在登记页核到 → 部分坐实；2026-10-28',
    url='https://www.dataforthai.com/company/0105568002761/',
    number='เลขทะเบียนนิติบุคคล 0105568002761（最接近法人；待核）', status='ยังดำเนินกิจการอยู่（营业中）', incorporated='2025-01-06', company_type='บริษัทจำกัด（Co., Ltd.）',
    sic=['电信 / 网络设备零售（网店；Bang Khae）'],
    address='88/468 Kanlapaphruek Rd., Bang Khae, Bangkok 10160', accounts='注册资本 ฿1,000,000（2025 新设）', accounts_due='—', size_band='微型',
    officers=['（研究档无 KP：info@satsdigital.com）'], psc='未取', charges='', prev_names=['หจก. แซทดิจิตอล ดอทคอม（2014–2015，已注销；疑前身）'],
    lines=['**2025 新设的 ฿1M 比价网店、无 KP、9 次 0 回复、法人仅近似 → 不动（B 保留）**'],
    notes='不动（新设微型 + 比价 + 无 KP）；部分坐实（法人近似 + 业务吻合；网站未核）。')
put('SB-614', key='other', batch=B, name='บริษัท โฟคอมม์ (ประเทศไทย) จำกัด FOCOMM (THAILAND) COMPANY LIMITED（focomm-cabling.com；**เลขทะเบียน 0105559051071；注册 2016-03-24；注册资本 ฿1,000,000；3 名泰籍股东；状态 营业中；网站 www.focomm-cabling.com 登记页核到**；12 Soi Sukhaphiban 5 Soi 5 Yaek 3, Tha Raeng, Bang Khen, Bangkok；登记业务 计算机软硬件购销；**与 SB-609 Ablelink (Thailand)（0105561132341）同地址同股东数 → 姊妹公司，并线 → SB-609**）— 布线 / 网络设备分销（光缆 / UTP / 机柜 / PoE / MC / SFP / GPON ONU；表内「ONV 的工业 FS」）；无 KP（info@）；16 次跟进无回复', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（บริษัท โฟคอมม์ (ประเทศไทย) จำกัด FOCOMM (THAILAND) COMPANY LIMITED；ทะเบียน 0105559051071；ซื้อจัดหาผลิตและพัฒนาซอฟต์แวร์คอมพิวเตอร์ … ตลอดจนอุปกรณ์คอมพิวเตอร์；ร้านขายปลีกคอมพิวเตอร์และอุปกรณ์ต่อพ่วงคอมพิวเตอร์；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 24 มีนาคม 2559；ทุนจดทะเบียน 1,000,000 บาท；12 ซอยสุขาภิบาล5 ซอย5แยก3 แขวงท่าแร้ง เขตบางเขน กรุงเทพมหานคร；เว็บไซต์ www.focomm-cabling.com；ไทย 3 ราย 100%）；同地址 = ABLELINK(THAILAND) 0105561132341（SB-609）；2026-10-28',
    url='https://www.dataforthai.com/company/0105559051071/',
    number='เลขทะเบียนนิติบุคคล 0105559051071', status='ยังดำเนินกิจการอยู่（营业中）', incorporated='2016-03-24', company_type='บริษัทจำกัด（Co., Ltd.）',
    sic=['计算机 / 网络设备零售（布线分销；Bang Khen）'],
    address='12 Soi Sukhaphiban 5 Soi 5 Yaek 3, Tha Raeng, Bang Khen, Bangkok 10220', accounts='注册资本 ฿1,000,000', accounts_due='—', size_band='微型（3 名股东）',
    officers=['（研究档无 KP：info@focomm-cabling.com）'], psc='3 名泰籍股东（与 Ablelink 同构）', charges='', prev_names=[],
    lines=['**与 SB-609 Ablelink (Thailand) 同址同构 → 并线 → SB-609，本户不另发（B 保留；Ablelink 一页纸里只提 Focomm 品类，不重复触达）**'],
    notes='并线 → SB-609（同址姊妹公司）；坐实（登记号 + 注册日 + 资本 + 地址 + 网站）。')
put('SB-813', key='other', batch=B, name='บริษัท โฟกัส ซิสเต็ม แอนด์ ดีไซน์ จำกัด FOCUS SYSTEM AND DESIGN COMPANY LIMITED（iFocus；ifocusshop.com；**เลขทะเบียน 0205549023031；注册 2006-08-24；注册资本 ฿3,000,000；状态 营业中**；149/237 9th Fl., Moo 9, …, Chonburi（芭提雅）；登记业务 网络与通信系统批发 / 设计 / 安装）— 芭提雅 / 春武里 CCTV 设计安装商（Hikvision / Dahua / Uniview 经销点；站内 Dahua PFS / Hikvision DS-3E PoE 页面；表内「在用 Itoonertech 商业 PoE，很多其他牌子」）；联系邮箱 hotmail；无 KP；9 次跟进无回复', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（บริษัท โฟกัส ซิสเต็ม แอนด์ ดีไซน์ จำกัด FOCUS SYSTEM AND DESIGN COMPANY LIMITED；ทะเบียน 0205549023031；ขายส่ง แก้ไข ออกแบบ ติดตั้งระบบเครือข่ายและโครงข่ายสื่อสาร；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 24 สิงหาคม 2549；ทุนจดทะเบียน 3,000,000 บาท；149/237 ชั้นที่ 9 หมู่ที่ 9 … ชลบุรี）；2026-10-28',
    url='https://www.dataforthai.com/company/0205549023031/',
    number='เลขทะเบียนนิติบุคคล 0205549023031', status='ยังดำเนินกิจการอยู่（营业中）', incorporated='2006-08-24', company_type='บริษัทจำกัด（Co., Ltd.）',
    sic=['网络 / 通信系统 批发 + 安装（CCTV；春武里 / 芭提雅）'],
    address='149/237 9th Fl., Moo 9, Chonburi（芭提雅；门牌后段未取）', accounts='注册资本 ฿3,000,000', accounts_due='—', size_band='小型',
    officers=['（研究档无 KP：focus.sys@hotmail.com）'], psc='未取', charges='', prev_names=[],
    lines=['**地方 CCTV 安装店（原厂 PoE 随摄像机走）、hotmail、无 KP、9 次 0 回复 → 不动（B 保留）**'],
    notes='不动（安装店 + 无 KP + 9×0）；坐实（登记号 + 注册日 + 资本 + 府）。')
put('SB-882', key='other', batch=B, name='บริษัท พี.ซี. เทเลคอม จำกัด P.C. TELECOM CO., LTD.（pctelecom.co.th；**เลขทะเบียน 0105539072803；注册 1996-07-01；注册资本 ฿10,000,000；状态 营业中；网站登记页核到**；100/215 Soi Kanchanaphisek 005, Lak Song, Bang Khae, Bangkok 10160；登记业务 计算机网络设计 / 软件；最近财报业务 CCTV 布线安装 + 电话交换机安装）— CCTV 销售安装（LG 摄像机直销；在售 Utepo PoE / L3 交换机；Axis）；无 KP（service@）；**31 次跟进无回复**', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（บริษัท พี.ซี. เทเลคอม จำกัด P.C. TELECOM CO., LTD.；ทะเบียน 0105539072803；ออกแบบ ระบบเครือข่ายคอมพิวเตอร์ สร้างและพัฒนา โปรแกรมคอมพิวเตอร์；ธุรกิจที่ส่งงบการเงินล่าสุด ให้บริการติดตั้งสายระบบกล้องโทรทัศน์วงจรปิด ระบบตู้สาขาโทรศัพท์；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 1 กรกฎาคม 2539；ทุนจดทะเบียน 10,000,000 บาท；100/215 ซอยกาญจนาภิเษก 005 แขวงหลักสอง เขตบางแค กรุงเทพมหานคร 10160；เว็บไซต์ www.pctelecom.co.th）；2026-10-28',
    url='https://www.dataforthai.com/company/0105539072803/',
    number='เลขทะเบียนนิติบุคคล 0105539072803', status='ยังดำเนินกิจการอยู่（营业中）', incorporated='1996-07-01', company_type='บริษัทจำกัด（Co., Ltd.）',
    sic=['CCTV / 电话交换机 布线安装（登记：网络设计 / 软件；Bang Khae）'],
    address='100/215 Soi Kanchanaphisek 005, Lak Song, Bang Khae, Bangkok 10160', accounts='注册资本 ฿10,000,000（财报未取）', accounts_due='—', size_band='小型',
    officers=['（研究档无 KP：service@pctelecom.co.th）'], psc='未取', charges='', prev_names=[],
    lines=['**30 年 CCTV 安装商、已用深圳 Utepo、但 31 次 0 回复 + 无 KP → 不动（B 保留；若来询按集成商 25% 预付）**'],
    notes='不动（31×0 + 无 KP）；坐实（登记号 + 注册日 + 资本 + 地址 + 网站）。')
put('SB-200', key='other', batch=B, name='ห้างหุ้นส่วนจำกัด ซิสเน็ต เซ็นเตอร์ SYSNET CENTER LIMITED PARTNERSHIP（sysnetcenter.com；**เลขทะเบียน 0133552003338；注册 2009-07-21；有限合伙；注册资本 ฿500,000；财报 2564–2568 连续；状态 营业中；官网 About 页自列商业登记号 + NBTC 无线电设备经营许可 050356000200 + 电子商务登记 3309800241321**；807/147 Moo 8 (Soi 1, Phummarin Village, behind Zeer Rangsit), Khu Khot, Lam Luk Ka, Pathum Thani 12130；电话 02-102-4284）— 网络设备销售安装店 15 年+（TP-Link Omada / Reyee / Ruijie 工业 PoE / UniFi / Cisco / MikroTik / Zyxel；Line @sysnet）；无 KP（info@）', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（ห้างหุ้นส่วนจำกัด ซิสเน็ต เซ็นเตอร์ SYSNET CENTER LIMITED PARTNERSHIP；ทะเบียน 0133552003338；ขายเครือข่ายแบบสาย ไร้สาย โทรศัพท์แบบไอพี …；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 21 กรกฎาคม 2552；ทุนจดทะเบียน 500,000 บาท；807/147 หมู่ที่ 8 ตำบลคูคต อำเภอลำลูกกา จ.ปทุมธานี 12130；เว็บไซต์ www.sysnetcenter.com）+ sysnetcenter.com/content/about-us（ทะเบียนการค้าเลขที่ 0133552003338；ใบอนุญาตค้าซึ่งเครื่องวิทยุคมนาคม 050356000200；เลขทะเบียนพาณิชย์อิเล็กทรอนิกส์ 3309800241321；02-102-4284；info@sysnetcenter.com；15 ปี）+ creden（ปีที่ส่งงบการเงิน 2564–2568；TSIC 26209）；2026-10-28',
    url='https://www.dataforthai.com/company/0133552003338/',
    number='เลขทะเบียนนิติบุคคล 0133552003338（NBTC 经营许可 050356000200）', status='ยังดำเนินกิจการอยู่（营业中；财报连续 5 年）', incorporated='2009-07-21', company_type='ห้างหุ้นส่วนจำกัด（Limited Partnership）',
    sic=['电话 / 电信设备批发 + 网络设备零售安装（Rangsit）'],
    address='807/147 Moo 8, Khu Khot, Lam Luk Ka, Pathum Thani 12130', accounts='注册资本 ฿500,000；财报 2021–2025 连续', accounts_due='—', size_band='微型（有限合伙）',
    officers=['（研究档无 KP：info@sysnetcenter.com）'], psc='未取', charges='', prev_names=[],
    lines=['**多品牌网店 + 安装（原厂渠道货为主）、有限合伙 ฿500k、无 KP → 不动（B 保留；若来询按分销 20% 预付）**'],
    notes='不动（微型多品牌店 + 无 KP）；坐实（登记号 + 注册日 + 类型 + 资本 + 地址 + 官网自列许可号）。')
put('SB-955', key='other', batch=B, name='OMC Tech（omctech.com；**最接近法人 บริษัท โอเอ็มซีเทค จำกัด OMC TECH COMPANY LIMITED เลขทะเบียน 0105559034613；注册 2016-02-26；注册资本 ฿4,000,000；3 名泰籍股东；99/349 Chaeng Watthana Rd., Thung Song Hong, Lak Si, Bangkok 10210；登记业务 电气系统材料销售（最近财报 机械设备批发）≠ 站内光端机 / 视频转换器 → 部分坐实**）— 视频光端机 / 转换器 / MC 为主，「基本没有 switch」；多办事处邮箱（sales@ / rugged@ / apac@）；表内「可以尝试多跟进一下」；9 次跟进无回复', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（บริษัท โอเอ็มซีเทค จำกัด OMC TECH COMPANY LIMITED；ทะเบียน 0105559034613；จำหน่ายวัสดุและอุปกรณ์งานระบบไฟฟ้า；ธุรกิจที่ส่งงบการเงินล่าสุด การขายส่งเครื่องจักรและอุปกรณ์อื่นๆ；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 26 กุมภาพันธ์ 2559；ทุนจดทะเบียน 4,000,000 บาท；99/349 ถนนแจ้งวัฒนะ แขวงทุ่งสองห้อง เขตหลักสี่ กรุงเทพมหานคร 10210；ไทย 3 ราย）；网站未在登记页展示、业务口径不同 → 部分坐实；2026-10-28',
    url='https://www.dataforthai.com/company/0105559034613/',
    number='เลขทะเบียนนิติบุคคล 0105559034613（最接近法人；待核）', status='ยังดำเนินกิจการอยู่（营业中）', incorporated='2016-02-26', company_type='บริษัทจำกัด（Co., Ltd.）',
    sic=['登记：电气材料 / 机械设备批发；站内：视频光端机 / MC'],
    address='99/349 Chaeng Watthana Rd., Thung Song Hong, Lak Si, Bangkok 10210', accounts='注册资本 ฿4,000,000', accounts_due='—', size_band='小型（3 名股东）',
    officers=['（研究档无 KP：sales@ / rugged@ / apac@omctech.com）'], psc='3 名泰籍股东', charges='', prev_names=[],
    lines=['**产品不对位（光端机 / 视频转换器；Saga 仅 STC-110XGE 一款 MC、无 SFP）+ 无 KP + 9 次 0 回复 → 不动（B 保留）**'],
    notes='不动（产品不对位）；部分坐实（法人名吻合、业务口径不同）。')
put('SB-1081', key='other', batch=B, name='泰国 CCTV / 通讯产品销售平台（sswmcctvshop.com 已失效；siamskyworth@gmail.com；**无法人名 + 免费邮箱 + 域名失效 → 0 查**）— 在售丰润达工业 FS；16 次跟进无实质回复', iso='TH', fetched=F,
    source='0 查（无法人名、gmail、域名失效；按 1 查纪律不检索）；2026-10-28',
    url='', number='未查', status='域名失效', incorporated='未查', company_type='未查',
    sic=['CCTV / 通讯产品网店（已下线）'],
    address='未查（泰国）', accounts='未查', accounts_due='—', size_band='未查',
    officers=['（未具名；siamskyworth@gmail.com）'], psc='未查', charges='', prev_names=[],
    lines=['**域名失效 + gmail + 16 次 0 回复 + 丰润达在供（Q-33 口径）→ 不动（B 保留）**'],
    notes='不动；0 查。')
put('SB-609', key='other', batch=B, name='บริษัท เอเบิลลิ้งค์(ประเทศไทย) จำกัด ABLELINK(THAILAND) COMPANY LIMITED（ablelink.co.th；**เลขทะเบียน 0105561132341；注册 2018-08-03；注册资本 ฿1,000,000；股东权益 ฿1,553,464（资本 155%）；3 名泰籍股东；状态 营业中**；12 Soi Sukhaphiban 5 Soi 5 Yaek 3, Tha Raeng, Bang Khen, Bangkok 10220；登记业务 安防 + 网络信号系统设备销售；**与 SB-614 Focomm (Thailand)（0105559051071，2016）同地址同构 → 姊妹公司，SB-614 并入本线**）— Network & Security Distributor（面向 SI / 承包商；表内「好几个牌子 Witek、Oring；MC 工业 FS SFP 等」「可以尝试多跟进一下」）；无 KP（info@）；18 次跟进无回复', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（บริษัท เอเบิลลิ้งค์(ประเทศไทย) จำกัด ABLELINK(THAILAND) COMPANY LIMITED；ทะเบียน 0105561132341；จำหน่ายอุปกรณ์ รักษาความปลอดภัย；ธุรกิจที่ส่งงบการเงินล่าสุด จำหน่ายอุปกรณ์ ระบบรักษาความปลอดภัยและระบบเครือข่ายสัญญาณ；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 3 สิงหาคม 2561；ทุนจดทะเบียน 1,000,000 บาท；12 ซอยสุขาภิบาล 5 ซอย 5 แยก 3 แขวงท่าแร้ง เขตบางเขน กรุงเทพมหานคร；ไทย 3 ราย 100%）+ creden（มูลค่าบริษัท รวมจากส่วนของผู้ถือหุ้น 1,553,464 บาท (155.35%)）；同址 = FOCOMM (THAILAND) 0105559051071（SB-614）；2026-10-28',
    url='https://www.dataforthai.com/company/0105561132341/',
    number='เลขทะเบียนนิติบุคคล 0105561132341', status='ยังดำเนินกิจการอยู่（营业中）', incorporated='2018-08-03', company_type='บริษัทจำกัด（Co., Ltd.）',
    sic=['安防 + 网络设备分销（Bang Khen；与 Focomm 同址）'],
    address='12 Soi Sukhaphiban 5 Soi 5 Yaek 3, Tha Raeng, Bang Khen, Bangkok 10220', accounts='股东权益 ฿1,553,464（资本 ฿1M 的 155%）', accounts_due='—', size_band='微型（3 名股东）',
    officers=['（研究档无 KP：info@ablelink.co.th）'], psc='3 名泰籍股东（与 Focomm 同构）', charges='', prev_names=[],
    lines=['**双牌照分销小户（Ablelink 安防网络 + Focomm 布线）、已卖多个国内工业牌、Simon「可以尝试多跟进」→ 分销 20% B small，一页纸一次（代表两户：切口 = 工业 PoE 阶梯 STI-054GP / STI-154GP / STI-288DGGPM / STI-488DGGPM + 10G MC STC-110XGE 一口价 + MOQ 1 + 付费样机；SFP / ONU 不做明说；英文，收 info@ablelink.co.th，抄 info@focomm-cabling.com）' + TH + '**；再无回声 → 两户一起不动',
           '守界：资本 ฿1M → 只做预付 100%；不点名 Witek / ORing；NBTC 不声称'],
    notes='分销 20% small；一页纸一次（代表 SB-609 + SB-614 一线；预付）；坐实（登记号 + 注册日 + 资本 + 权益 + 地址）。')
put('SB-612', key='other', batch=B, name='บริษัท คลาวด์ ไอที เน็ทเวิร์ค จำกัด CLOUD IT NETWORK CO., LTD.（clouditnetwork.com；**เลขทะเบียน 0125554018059；注册 2011-09-29；注册资本 ฿1,000,000；股东权益 ฿1,880,014（资本 188%）；3 名泰籍股东；财报 2563–2567 连续；状态 营业中**；51/1 Mongkhon Niwet Village, Soi Ngamwongwan 48, Lat Yao, Chatuchak, Bangkok 10900；登记业务 计算机软硬件购销 / 进出口 / 租赁 / 服务）— VoIP 与云方案商（佛山 LVswitch IP PBX / FXS 网关 / Grandstream；表内「switch 周边产品」「可以尝试多跟进一下」）；无 KP（sales@）；16 次跟进无回复', iso='TH', fetched=F,
    source='TH · 1 次检索：dataforthai（บริษัท คลาวด์ ไอที เน็ทเวิร์ค จำกัด CLOUD IT NETWORK CO.,LTD.；ทะเบียน 0125554018059；ซื้อ ขาย นำเข้า ส่งออก ให้เช่า ให้บริการ เกี่ยวกับคอมพิวเตอร์；การขายส่งคอมพิวเตอร์อุปกรณ์ต่อพ่วงคอมพิวเตอร์และซอฟต์แวร์；สถานะ ยังดำเนินกิจการอยู่；จดทะเบียน 29 กันยายน 2554；ทุนจดทะเบียน 1,000,000 บาท；51/1 หมู่บ้าน มงคลนิเวศน์ ซอยงามวงศ์วาน 48 ถนนงามวงศ์วาน แขวงลาดยาว เขตจตุจักร กรุงเทพมหานคร 10900；ไทย 3 ราย）+ creden（ปีที่ส่งงบการเงิน 2563–2567；มูลค่าบริษัท รวมจากส่วนของผู้ถือหุ้น 1,880,014 บาท (188%)）；2026-10-28',
    url='https://www.dataforthai.com/company/0125554018059/',
    number='เลขทะเบียนนิติบุคคล 0125554018059', status='ยังดำเนินกิจการอยู่（营业中；财报连续 5 年）', incorporated='2011-09-29', company_type='บริษัทจำกัด（Co., Ltd.）',
    sic=['计算机 / 外设 / 软件批发（VoIP 方案；Chatuchak）'],
    address='51/1 Mongkhon Niwet Village, Soi Ngamwongwan 48, Lat Yao, Chatuchak, Bangkok 10900', accounts='股东权益 ฿1,880,014（资本 ฿1M 的 188%）；财报 2020–2024 连续', accounts_due='—', size_band='微型（3 名股东）',
    officers=['（研究档无 KP：sales@clouditnetwork.com）'], psc='3 名泰籍股东', charges='', prev_names=[],
    lines=['**15 年 VoIP 方案商、已从佛山进口 PBX、Simon「可以尝试多跟进」→ 分销 20% B small，一页纸一次（切口：IP 话机 / 网关 配套 PoE：STC-028GP / STC-2216GP / STC-2224GP 一口价 + 管理机 STC-4424GCPM（VLAN 分话音）+ MOQ 1 + 付费样机；英文，收 sales@）' + TH + '**；再无回声 → 不动',
           '守界：资本 ฿1M → 预付 100%；VoIP 设备不做；NBTC 不声称'],
    notes='分销 20% small；一页纸一次（预付）；坐实（登记号 + 注册日 + 资本 + 权益 + 财报年份 + 地址）。')
put('SB-034', key='other', batch=B, name='TJ Computer（泰国电脑 / CCTV 店；tj2003.net 失效；tjcomputercctv@tj2003.net / tjcomputer2003@gmail.com；**通名店号 + 域名失效 → 0 查**）— **经营者 Peter（Ponganan Ruenboon / พงศ์นันท์ รื่นบุญ；08-0069-1918）：2025-03 对 2 光 8 PoE 回复 Interested，2025-05 要 5 电口具体产品信息**', iso='TH', fetched=F,
    source='0 查（通名店号「TJ Computer」+ 域名失效 + gmail；按 1 查纪律不检索；KP 与需求来自 2025-03 / 05 来信）；2026-10-28',
    url='', number='未查', status='域名失效（邮箱 2025-05 仍通）', incorporated='未查', company_type='未查（个体店推定）',
    sic=['电脑 / CCTV 零售安装店（泰国）'],
    address='未查（泰国）', accounts='未查', accounts_due='—', size_band='微型',
    officers=['Peter (Ponganan Ruenboon) — 经营者（研究档 KP；tjcomputercctv@tj2003.net；08-0069-1918 / 06-2217-9229）= 收件人'], psc='Peter（推定）', charges='', prev_names=[],
    lines=['**店主本人回过 Interested + 两次具体需求（2 光 8 PoE / 5 电口）→ 集成商 25% B small，一页纸一次（切口：直接报 STC-228GP（8 PoE + 2 SFP）一口价 + 5 口 = STI-054GP（4 PoE + 1 GE）按主表现价 + MOQ 1 + 付费样机 + 100% 预付 + FOB 深圳；opener 引 2025-05 他要的具体信息；英文，Peter 直呼；发 tj2003.net 邮箱抄 gmail）' + TH + '**；再无回声 → 不动',
           '守界：个体店 → 预付 100%、小额以快递 DAP 报价'],
    notes='集成商 25% small；一页纸一次（预付）；0 查。')
put('SB-510', key='other', batch=B, name='Pongpanot Kwanmuang（泰国项目型买家；pongpanot.k@hotmail.com；**个人 + 免费邮箱 → 0 查**）— 需求 12 光 12 电 / 8 光 8 电 / 工业 MC；2024-06 问一个项目「工业 2+4 PoE、2+8」；19 次推送 1 次实质回复；表内「可以尝试多跟进一下」；无 WA', iso='TH', fetched=F,
    source='0 查（个人 hotmail、无公司名；按 1 查纪律不检索）；2026-10-28',
    url='', number='未查', status='个人', incorporated='未查', company_type='个人（项目买家）',
    sic=['项目型采购（工业 PoE / 光电混合）'],
    address='未查（泰国）', accounts='未查', accounts_due='—', size_band='个人',
    officers=['Pongpanot Kwanmuang — 表内联系人（研究档 KP；pongpanot.k@hotmail.com）= 收件人'], psc='—', charges='', prev_names=[],
    lines=['**需求具体（工业 2+4 / 2+8 PoE）+ 回过 1 次实质 + Simon「可以尝试多跟进」→ 集成商 25% B small，一页纸一次（切口：2+4 = STI-154GP（4 PoE + 1 GE + 1 SFP）/ 2+8 = STI-288DGGPM $137 一口价 + 12 光 12 电 / 8 光 8 电 明说主表无此配置、以 STC-4424GCPM + SFP 口替代 + 100% 预付 + 付费样机；opener 引 2024-06 他的项目；英文，Pongpanot 直呼）' + TH + '**；再无回声 → 不动',
           '守界：个人买家 → 预付 100%；身份不清不升 A'],
    notes='集成商 25% small；一页纸一次（预付）；0 查。')
put('SB-603', key='other', batch=B, name='Wirote（泰国个人联系人；witotejan1@gmail.com；+66 65 426 3626；**个人 + 免费邮箱 → 0 查**）— 需求 4 光 8 电工业大壳；2023-11 对 PoE 看门狗系列「不需要样品」；WA 14 次无实质回复', iso='TH', fetched=F,
    source='0 查（个人 gmail、无公司名；按 1 查纪律不检索）；2026-10-28',
    url='', number='未查', status='个人', incorporated='未查', company_type='个人',
    sic=['个人询价（工业交换机）'],
    address='未查（泰国）', accounts='未查', accounts_due='—', size_band='个人',
    officers=['Wirote — 表内联系人（研究档 KP；witotejan1@gmail.com；+66 65 426 3626）'], psc='—', charges='', prev_names=[],
    lines=['**个人 + WA 14 次 0 实质 + 2023 后无新需求 → 不动（B 保留；来询再按集成商 25% 预付）**'],
    notes='不动（个人 + 14×0）；0 查。')

# ───────── AE 第 1 户（路径首测）─────────
put('SB-918', key='other', batch=B, name='Alston Systems Inc.（alston-systems.com；**中东非总部 801 Reef Tower, Jumeirah Lake Towers, P.O. Box 62201, Dubai, UAE（JLT = DMCC 自贸区推定）；美国法人 Alston Systems LLC, 919 North Market Street Suite 950, Wilmington DE 19801（= 注册代理地址）；阿联酋牌照号 1 查未得 → 部分坐实**）— **自有品牌 ICT / 安防 / 节能产品商（铜缆 / 光缆 / 配线 / 有源产品（PoE MC 等）/ 电源 / CCTV / LED / 太阳能；自称制造商、海外制造基地）**；表内「FS SFP 模块 MC」；KP Kennedy / Ross（purchase@）；16 次跟进无回复', iso='AE', fetched=F,
    source='AE · 1 次检索（路径首测）：alston-systems.com/contact（USA: Alston Systems LLC, 919 North Market Street, Suite 950, Wilmington 19801 Delaware；Middle East & Africa: Alston Systems Inc., 801 Reef Tower, Jumeira Lake Towers, P.O. Box 62201, Dubai, UAE；mea@alston-systems.com）+ alston-systems.com 产品目录 PDF 2022-10（ICT, Security and Energy Savings Products Manufacturer；Communications and Network Cables and Components, Active products, Power Solutions, CCTV, LED, solar；corporate offices USA and UAE）+ letfindout（JLT Dubai；mea@）；牌照号 / DMCC 登记未命中 → 部分坐实；2026-10-28',
    url='https://alston-systems.com/contact/',
    number='未取（AE 牌照号 1 查未得；JLT/DMCC 推定）', status='营业中（官网 + 目录在线）', incorporated='未取', company_type='Inc.（自贸区推定）+ 美国 LLC（Delaware）',
    sic=['自有品牌 布线 / 有源网络 / 电源 / CCTV 产品（迪拜 JLT）'],
    address='801 Reef Tower, Jumeirah Lake Towers, P.O. Box 62201, Dubai, UAE', accounts='未取', accounts_due='—', size_band='小型',
    officers=['Kennedy — 研究档 KP（kennedy@alston-systems.com；姓氏 / 职务待核）= 收件人', 'Ross — 研究档 KP（purchase@alston-systems.com）= 抄送'], psc='未取', charges='', prev_names=[],
    lines=['**自有品牌（Alston 标有源产品 = 外购贴牌）→ 贴标 OEM 30% B，一页纸一次（切口：Alston 标 / 中性包装 的 STC-028GP / STC-228GP / STC-2216GP / STC-2224GP / STC-4424GCPM + MC STC-110XGE 阶梯一口价 + 付费样机 + MOQ 1；SFP 模块不做明说；英文，Kennedy 直呼、抄 purchase@）' + AE + '**；16 次 0 回复在先 → 再无回声即不动',
           '守界：牌照未核 → 只做预付 100%；TDRA / ESMA 不声称'],
    notes='贴标 OEM 30%；一页纸一次（最后一次；预付）；部分坐实（官网 contact 地址 + P.O. Box；牌照号未取）。')
print('b117 第 2 段 13 written')
