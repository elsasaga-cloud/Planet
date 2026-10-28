#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 113 批（T29-U106，公司底数第三十一轮 · 加拿大 B 池收尾 4 户 + 俄罗斯 B 池第 1 轮前 36 户 = 40 户）官方登记核实 → 研究档 KP 角色 / 法定名 / 事实 补写。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=113 行）。
结构同 batch112_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
附 Q-33 口径勘误 4 户（SB-395 / SB-173 / SB-843 / SB-811：HRUI 在供 ≠「不碰」，默认「只推 SmartByte / Marvell 管理 / 工业线，不报 HRUI 同款」）。
本批定性：B BIG · 加厚一次 11（SB-849 АО «Связьстройдеталь» 7723005557 31.5 亿 ₽ 贴标配套 30% / SB-446 ООО «КСБ Аматек» 7802622136 AMATEK 全线 PoE / SB-028 ООО «ФИБО» 7802617376 自有品牌 FIBO PoE 采购 KP / SB-851 ООО «Тайле РУС» 7715603560 33 亿 ₽ NIKOMAX / GIGALINK 等（Q-33 只推 Marvell 线）/ SB-218 ООО «НАГ» 6659099112 70 亿 ₽ SNR / SB-877 ООО «ЛУИС+» 7714334756 LTV 收件渠道待补证 / SB-884 ООО «Бизнес Центр Алгоритм» 2311218490 Polyvision 商标持有 + 唯一进口 / SB-893 DSSL / TRASSIR 7709423841 集团 90 亿 ₽ / SB-898 ТПГ «Декси» XVI 3666173040 / SB-1077 Софт-Троник 俄最大 Dahua 分销 现法人未取）+ 加厚一次 1（SB-555 TACEL LTD. 联邦号 081582-9 交通机柜制造 配套 25–30%，不声称 NEMA TS2）；
加厚 small 一次 3（SB-863 CMD 自有型号 PoE 全线 读而不回 法人未取 / SB-894 ООО «Руссбыт» 7722409934 总经理 Ким Вадим = 收件人 / SB-459 SSDCAM 自称 OEM 生产商 法人未取）；
一页纸一次 · 有回声再加厚 16（SB-123 ООО «ТОРУС» 9715255437 / SB-850 АО «Линтех» 7720021335 Symway 配套 / SB-620 АО «Карма Групп» 7727724175 SI / SB-769 ООО «Контур М» 7716774939 / SB-964 ООО «ЛИНКЕР» 7806546038 UPLINK / SB-599 ООО НПП «Симанитрон-Электроника» 6454141571 同行 / 贴标 / SB-829 Optimus 法人未取（Q-33 丰润达口径）/ SB-886 SarmatT 法人未取 / SB-430 ООО «Протэк» 5404507902（研究档法人「Модуль」更正）/ SB-870 HUNTER 法人未取 / SB-874 KENO / FOX = ООО «ФКВИДЕО» / SB-1064 ООО «Порт Депо» 7720875009 / SB-396 ООО «Море Камер» 2508134914 / SB-848 ООО «СетиЛенд» 7447215866 10 起强制执行 100% 预付 / SB-986 ООО «ТЕСТ СОЛЮШН» 5036159107 / SB-842 ООО «Фикс» 1655262545）+ Q-33 勘误后一页纸 3（SB-395 Mercku / SB-173 Inaxsys / SB-843 Мир систем безопасности，只推 Marvell 管理 / 工业线）；
并线 1（SB-837 GIGALINK = Тайле 自有品牌 → SB-851）；
不动 9（SB-1118 Alain Casault MikroTik 培训师 婉拒（研究档类型更正）/ SB-694 个人 0 查 / SB-731 查无实体 / SB-212 АО «ФТИ-Оптроник» 7802059121 同行光模块厂 壳 1 人 / SB-039 ООО НПП «Зелакс» 5044097824 同行 + 加密许可 + 政府客户 / SB-191 ООО «АСТКОМ» 7838051581 联系人为前负责人 + 主营玩具 身份不清 / SB-939 ООО «Клеверкей Ру» 9725004175 前身 ЗАО 破产清算 新壳 / SB-720 Unitech-shop 法人未取 + 邮箱永久退信）；
坐实 27 / 部分坐实 10（SB-1118 / 863 / 123 / 843 / 459 / 964 / 829 / 886 / 870 / 874 / 1077 中 1077 计入）/ 未坐实 3（SB-694 / 731 / 720）；
KP 坐实 = 老板 / 总经理 / 采购本人 9（SB-555 Gil Marques / SB-894 Ким Вадим Николаевич / SB-028 Anastasia Roshchupkina（Purchasing）/ SB-446 Kovrigo / SB-1064 Бабаев / SB-396 Букарев / SB-848 Калистратов / SB-986 Алехина / SB-870 Бобков）；
法定名补全 / 更正 31；country_fix 0（RU 36 户 iso 均 RU；CA 4 户 iso 均 CA）。RU 36 户稿件一律「预付款 + 待 Simon 定 RU 收款 / 物流路径」，本批不发。
旁线索（≠ 目标，另立户评估）：ООО ТД «Связьстройдеталь» 7704588494（SB-849 贸易公司）；КСБ 集团 НПО / ТД «КСБ»（SB-446）；ООО «Символ-Автоматика»（SB-599 关联）；ООО «Компания ЛУИС+» 5040079849 / ЛУИС+Сибирь（SB-877 集团）；ООО «ДССЛ-Первый» 7701081730 / НПП «Трассир»（SB-893 集团）；ООО «Фотон» 3661060572（SB-898 项目相机实体）；ООО «Модуль» 7802791198（SPb Eltex 供应商，SB-430 研究档误指）；svn-video.ru ИП Криволуцкая（SVN 品牌，≠ SB-843）；ENS Security / Lysora（≠）。
Simon 待决（累计见 PR-02-53 追记）：RU 收款 / 物流路径（本批 36 户 + BY 4 户全部压着）；升 A 候选 SB-849 / 446 / 028 / 851 / 218 / 877 / 884 / 893 / 898 / 1077 回信即升（但先要路径）；Q-33 HRUI 口径勘误请确认（HRUI 在供户只推 Marvell 管理 / 工业线 vs 一律不碰）。
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 113 批 官方登记核实 2026-10-28）'
RU = '— 稿件一律「预付款」，待 Simon 定 RU 收款 / 物流路径后再发'
UPD = {
    # ---------- 第 1/3 CA 4 + RU 10 ----------
    'SB-1118': [{'kp_name': 'Alain Casault', 'role': 'ing. · CSPE 副总裁 / 联合创始人 · MikroTik 认证培训师本人（alaincasault.com）= 已婉拒「现在不要」' + TAG},
                {'facts': {'legal_name': 'Télécommunications Alain Casault / CSPE（Centre de services professionnels en éducation；78 rue Blainville Ouest, Sainte-Thérèse, QC J7E 1X3；NEQ 未取；1–10 人）', 'founded': '1996（CSPE）' + TAG,
                           'other': '第 113 批：**研究档类型「教育机构 IT / 终端用户」有误 → MikroTik 培训 + 电信咨询个体业务**；非渠道 + 明示「现在不要」→ **不动（B 保留；他主动来询再报）**' + TAG}}],
    'SB-555': [{'kp_name': 'Gil Marques', 'role': 'President（2015–；LinkedIn / zoominfo；gil.marques@）= 拍板人 / 收件人' + TAG},
               {'kp_match': 'gabor.szabo@tacel.ca', 'role': 'Tacel 研究档 KP（职务待核）= 抄' + TAG},
               {'kp_name': 'George Soares', 'role': 'General Manager（datanyze）' + TAG},
               {'facts': {'legal_name': 'TACEL LTD.（联邦公司号 081582-9；CBCA 1979-02-14；1148 Bellamy Road North, Scarborough, ON M1H 1H2；分部 Anjou QC / AB / BC；ISO 9001:2015；11–50 人；估 $19.1M）', 'founded': '1979-02-14' + TAG,
                          'other': '第 113 批：加拿大 ITS / 交通控制设备供应商兼交通机柜制造商（Sensys 加拿大独家分销）→ **配套 / 集成 25–30% B，加厚一次（机柜内 CCTV / 通信用工业交换机 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM / STI-488DGGPM 第二来源 + 宽温 + 3 年保 + 加拿大 DAP；Gil 直呼 + Gabor 抄；一问非信号机网络是否可接受工业级 CE / FCC）**；守界：Saga 无 NEMA TS2 / 交通信号认证，稿内绝不声称；不点名 EtherWAN' + TAG}}],
    'SB-694': {'facts': {'legal_name': '未具名（François Burton 个人 Gmail；+1 613；0 查）', 'founded': '—' + TAG,
                         'other': '第 113 批：个人户 + 需求规格我方无（≥8×SFP+ 纯光口工业机）+ 15 次无果 → **不动（B 保留）**' + TAG}},
    'SB-731': {'facts': {'legal_name': '未坐实（「JTS Telecom」Hotmail；1 查无对应加拿大法人；jts.net 德州 JTS / JTS Consulting Inc. / JTS Mechanical 均 ≠）', 'founded': '未取' + TAG,
                         'other': '第 113 批：Hotmail 个体 + 查无实体 + 2025-11-21 已回「No」→ **不动（B 保留）**' + TAG}},
    'SB-212': [{'add_kp': {'name': 'Ильин Виктор Юрьевич', 'role': 'Генеральный директор АО «ФТИ-Оптроник»（2013-06-21–；rusprofile）— 同行，不动' + TAG, 'email': '', 'source': 'https://www.rusprofile.ru/id/1440480'}},
               {'facts': {'legal_name': 'АО «ФТИ-Оптроник»（ИНН 7802059121；ОГРН 1037804018911；194064 Санкт-Петербург, ул. Политехническая, д. 28, лит. А；АО 壳 1 人 / 2025 营收 2.6 млн ₽，经营 ООО 待证）', 'founded': '1994-05-25' + TAG,
                          'other': '第 113 批：光模块 / 光纤 MC 同行制造商（自产自销）→ **不动（同行规则；B 保留；RU 路径未定）**' + TAG}}],
    'SB-849': [{'add_kp': {'name': 'Троицкий Николай Станиславович', 'role': 'Генеральный директор АО «ССД»（2024-06-07–；rusprofile）= 拍板人（mail@ssd.ru 点名 MC / 有源产品经理）' + TAG, 'email': '', 'source': 'https://www.rusprofile.ru/id/2663562'}},
               {'facts': {'legal_name': 'АО «Связьстройдеталь»（АО «ССД»；ИНН 7723005557；ОГРН 1027700403103；115088 Москва, ул. Южнопортовая, д. 7а；2024 营收 3.154 млрд ₽ / 利润 749 млн ₽；贸易公司 ООО ТД «Связьстройдеталь» 7704588494）', 'founded': '1993-06-22' + TAG,
                          'other': '第 113 批：大型通信线路建设材料厂、自有标 MC 为边缘品类 → **贴标 / 配套 30% B BIG，加厚一次（ССД 标 MC / 工业交换机 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM 有源配套线 + 中性包装 / 自编货号；俄 / 英文）**' + RU + '；升 A 候选' + TAG}}],
    'SB-863': {'facts': {'legal_name': 'CMD（cmd-sec.ru；品牌 + 自有型号 PoE 交换机 CMD-SW104/204/GSW104/SW108/SW16/SW24-POE + LL-SW 系列坐实；页脚法人 / ИНН 未见 → 部分坐实）', 'founded': '未取' + TAG,
                         'other': '第 113 批：自有型号 PoE 全线（4–24 口 + 工业）+ 读而不回 3 次 → **贴标 30% small，加厚 small 一次（CMD 标 STC-028GP / STC-228GP / STC-2224GP / STI-054GP 第二代工源 + 中性包装 / 自编货号 + 小 MOQ；俄 / 英文，sales@ 点名采购）**' + RU + '；不点名 Utepo' + TAG}},
    'SB-446': [{'kp_name': 'Aleksandr Kovrigo', 'role': 'КСБ / Amatek 研究档联系人（kovrigo@ksb.su）= 收件人' + TAG},
               {'add_kp': {'name': 'Тарасов Руслан Евгеньевич', 'role': 'Генеральный директор ООО «КСБ Аматек»（rusprofile）= 拍板人' + TAG, 'email': '', 'source': 'https://amatek.su/pages/contacts'}},
               {'facts': {'legal_name': 'ООО «КСБ Аматек»（ИНН 7802622136；ОГРН 1177847187430；194100 Санкт-Петербург, ул. Литовская, д. 10А, пом. 2-Н, комн. 331；КСБ 集团：НПО «КСБ» 研发生产 / ТД «КСБ» 分销；商标 AMATEK 2014）', 'founded': '2017-05-26（商标 2014）' + TAG,
                          'other': '第 113 批：自有品牌全线 PoE（含云管理型号）+ 集团含分销公司 → **贴标 OEM 30% B BIG，加厚一次（AMATEK 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP 第二代工源 + 中性包装 / 自编货号；俄 / 英文，Kovrigo 直呼）**' + RU + '；升 A 候选' + TAG}}],
    'SB-123': {'facts': {'legal_name': 'ООО «ТОРУС»（ИНН 9715255437；ОГРН 1167746383980；Москва, ул. Руставели, 14, стр. 6, оф. 8（办公）；前身 / 同名 ООО «ТД "Торус"» 7724905230（2014）已清算 2026-10；总经理未取）', 'founded': '2016' + TAG,
                         'other': '第 113 批：多品牌安防分销网店 + 自有型号商业 PoE（11 大区仓）→ **分销 20% / 贴标 small，一页纸一次（Torus 标或中性 STC-028GP / STC-228GP / STC-2224GP 第二价位 + 小 MOQ；俄 / 英文，sales@ 一问采购）**' + RU + '；不点名 Dahua / Utepo' + TAG}},
    'SB-843': {'facts': {'legal_name': 'ООО «Мир систем безопасности»（MIR-SB.com；г. Вологда, ул. Щетинина, 6；10+ 年；ИНН 未取）；**研究档「SVN 自有标」有误：SVN 为第三方品牌（svn-video.ru = ИП Криволуцкая Ю.В. ИНН 402910363642）**', 'founded': '≈2014 或更早' + TAG,
                         'other': '第 113 批（Q-33 口径勘误）：PoE 现由洪瑞（HRUI）供货 ≠「不碰」；HRUI 在供户默认「只推 SmartByte / Marvell 管理 / 工业线，不报 HRUI 同款」→ **一页纸一次（银行 / 工厂项目用 Marvell 管理型 STC-4424GCPM + 工业 STI-054GP / STI-144GP；俄 / 英文，mail@ 一问采购）**' + RU + TAG}},
    'SB-850': [{'add_kp': {'name': 'Кононов Станислав Владимирович', 'role': 'Генеральный директор АО «Линтех»（2020-12-29–；rusprofile）= 拍板人（sales@lintech.ru / inbox@symway.com 点名）' + TAG, 'email': '', 'source': 'https://www.rusprofile.ru/id/2051822'}},
               {'facts': {'legal_name': 'АО «Линтех»（АО «Лаборатория информационных технологий»；ИНН 7720021335；ОГРН 1027739442862；127495 Москва, Долгопрудненское ш., д. 3；营收 427.3 млн ₽；软件实体 ООО «СИМВЭЙ» 7731392268 Сколково）', 'founded': '1994-07-19' + TAG,
                          'other': '第 113 批：Symway 对等式 PBX 厂商（100% 俄罗斯自研定位）、交换机仅配套 → **配套 30% small，一页纸一次（话机部署 PoE STC-028GP / STC-228GP / STC-2224GP 配套 SKU + 中性包装）**' + RU + '；再无回声 → 不动' + TAG}}],
    'SB-894': [{'add_kp': {'name': 'Ким Вадим Николаевич', 'role': 'Генеральный директор ООО «Руссбыт»（2026-08-06–；rusprofile；= 研究档收件 vadim@sbvs.ru）= 拍板人 / 收件人' + TAG, 'email': 'vadim@sbvs.ru', 'source': 'https://www.rusprofile.ru/id/11152155'}},
               {'facts': {'legal_name': 'ООО «Руссбыт»（原 «Спецвидеопроект» / SVP；ИНН 7722409934；ОГРН 1177746934881；111024 Москва, ул. Авиамоторная, д. 8, стр. 1, эт. 6；微型 9 人；100% 创始人 Смирнов Егор Павлович）', 'founded': '2017-09-04（团队 1998）' + TAG,
                          'other': '第 113 批：疏散广播 / 告警 + 自有品牌交换机 / MC（「俄罗斯生产商 / 进口替代」定位，实为贴牌线）+ Simon 标「比较重要」+ 总经理即收件人 → **贴标 30% small，加厚 small 一次（SVP / РУССБЫТ 标工业 MC / 交换机 STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM + STC-2224GP 第二代工源 + 中性包装 / 自编货号；俄 / 英文，Вадим 直呼）**' + RU + '；不点名 E-link' + TAG}}],
    'SB-028': [{'kp_name': 'Anastasia Roshchupkina', 'role': 'Purchasing（研究档；roshchupkina@fibotelecom.ru）= 收件人' + TAG},
               {'add_kp': {'name': 'Боровский Максим Вячеславович', 'role': '创始人 / 50% 股东 ООО «ФИБО»（2017–；tbank 变更记录）= 拍板人（邮箱未取）' + TAG, 'email': '', 'source': 'https://fibotelecom.ru/contact/'}},
               {'facts': {'legal_name': 'ООО «ФИБО»（原 ООО «Фибо-Телеком»，2024-08-20 更名；ИНН 7802617376；ОГРН 1177847130438；194214 Санкт-Петербург, пр. Энгельса, д. 71, лит. А, пом. 309；办公 Коломяжский пр., 33к2 + 莫斯科；注册资本 600 000 ₽）', 'founded': '2017-04-11' + TAG,
                          'other': '第 113 批：**研究档类型「运营商 / 光传输采购（待补证）」更正为光通信分销 + 自有品牌 FIBO（兼容 SFP + PoE 交换机 FT-S118FP / FT-S1116FP）**；采购 KP 直达 → **贴标 OEM 30% B BIG，加厚一次（FIBO 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + 工业 STI-054GP / STI-144GP 第二代工源 + 中性包装 / 自编货号 + 小 MOQ；俄 / 英文，Anastasia 直呼）**' + RU + '；升 A 候选' + TAG}}],
    'SB-039': [{'add_kp': {'name': 'Пашкевич Владимир Евгеньевич', 'role': 'Генеральный директор ООО НПП «Зелакс»（2016-04-13–；rusprofile）— 同行，不动' + TAG, 'email': '', 'source': 'https://www.rusprofile.ru/id/10436971'}},
               {'facts': {'legal_name': 'ООО НПП «Зелакс»（ИНН 5044097824；ОГРН 1165044051160；124365 Москва, Зеленоград, ул. Заводская, д. 1б, стр. 2；82 人；2024 营收 988.3 млн ₽ / 2025 831.5 млн ₽；加密设备研发分发许可证；创始人 Сухман С.М. / Степанов В.В.）', 'founded': '2016-04-13（品牌 1988）' + TAG,
                          'other': '第 113 批：自研自产交换机的同行制造商 + 加密许可证 + 政府 / 战略行业客户 → **不动（同行 + 守界；B 保留）**' + TAG}}],
    # ---------- 第 2/3 RU 13 ----------
    'SB-191': [{'kp_match': 'gordeev.inntel@mail.ru', 'role': 'ООО «АСТКОМ» 前负责人之一（vbankcenter 历任名单；现属关系待证；mail.ru）' + TAG},
               {'facts': {'legal_name': 'ООО «АСТКОМ»（圣彼得堡；ИНН 7838051581；ОГРН 1167847150910；192102 СПб, ул. Касимовская, д. 5, лит. А, пом. 10-Н；主营 ОКВЭД 32.4 玩具生产；2025 收入 773 млн ₽ / 2024 2.0 млрд ₽；10 人；95% 股东 Астров С.А.；управляющий Гегин В.С.）', 'founded': '2016-03-25' + TAG,
                          'other': '第 113 批：联系人为前负责人 + mail.ru 邮箱 + 主营登记玩具 + 1 封 0 打开 → **不动（身份不清；B 保留；RU 路径未定）**' + TAG}}],
    'SB-459': {'facts': {'legal_name': 'SSDCAM（ssdcam.ru；「OEM 生产商」自有品牌；莫斯科仓库 БЦ «Рапира», Дорогобужская ул., 14；萨马拉代表处 Ставропольская 167А；2015 换标；页脚法人 / ИНН 未见 → 部分坐实）', 'founded': '未取（品牌 2015 换标）' + TAG,
                         'other': '第 113 批：自称 OEM 生产商、自有标 PoE → **贴标 30% small，加厚 small 一次（SSDCAM 标 STC-028GP / STC-228GP / STC-2224GP 第二代工源 + 中性包装 / 自编货号；俄 / 英文，zakaz@ 点名采购）**' + RU + TAG}},
    'SB-620': [{'add_kp': {'name': 'Радкевич Константин Станиславович', 'role': 'Руководитель АО «Карма Групп»（zachestnyibiznes）= 拍板人（office@ 点名采购）' + TAG, 'email': '', 'source': 'https://www.karma-group.ru/about/contacts/'}},
               {'facts': {'legal_name': 'АО «Карма Групп»（ИНН 7727724175；ОГРН 1107746588454；115551 Москва, Шипиловский пр-д, д. 47, пом. 13Н；实际 2-й Рощинский пр., 8；自有品牌 KARMA 服务器 / ATLAS SAN）', 'founded': '2010-07-26' + TAG,
                          'other': '第 113 批：SI + 自有品牌服务器、数据中心项目 → **集成 25% small，一页纸一次（STC-4424GCPM / STC-424XGGPM-280W + STH-2C24XF-HSI / STH-8C48DX-HSI 作第二来源；俄 / 英文，office@ 点名采购）**' + RU + '；守界：政府客户线不提；不点名 DCN / Huawei / Cisco' + TAG}}],
    'SB-769': {'facts': {'legal_name': 'ООО Компания «Контур М»（ИНН 7716774939；ОГРН 1147746540325；129344 Москва, ул. Искры, д. 9, корп. 2；集团 1994 起；总经理未取）', 'founded': '2014（集团 1994）' + TAG,
                         'other': '第 113 批：多业务数据 / 有线电视网络集成 + 设备分销 → **集成 / 分销 20–25% small，一页纸一次（FTTB 接入 / 汇聚 STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W + STI-144GP；俄 / 英文，info@ 一问采购）**' + RU + '；不点名 D-Link / Cisco / Huawei / BDCOM' + TAG}},
    'SB-939': {'facts': {'legal_name': 'ООО «Клеверкей Ру»（ИНН 9725004175；ОГРН 1197746165968；115419 Москва, 2-й Рощинский проезд；前身 ЗАО «Клевер Кей» 经破产程序 2023-12-26 清算）', 'founded': '2019' + TAG,
                         'other': '第 113 批：品牌导向经销 + 前身破产新壳 → **不动（B 保留）**' + TAG}},
    'SB-964': {'facts': {'legal_name': 'ООО «ЛИНКЕР»（UPLINK；站点元数据 ИНН 7806546038（圣彼得堡；8-812-666-2-666）；ОГРН / 总经理未取；同名 9731044810 / 7716172395 ≠）', 'founded': '2018' + TAG,
                         'other': '第 113 批：自有品牌 UPLINK 光器件供应商（Saga 不做光模块），MC / 有源为副线 → **贴标 30% small，一页纸一次（UPLINK 标 STI-054GP / STI-144GP + STC-2224GP / STC-110XGE 有源补位 + 中性包装；俄 / 英文，sales@ 一问采购）**' + RU + '；不点名 DCN' + TAG}},
    'SB-851': [{'kp_match': 'akuznetsova@tayle.ru', 'role': 'Тайле 研究档 KP（职务待核）= 收件人' + TAG},
               {'kp_match': 'arubeko@tayle.ru', 'role': 'Тайле 研究档 KP（职务待核）= 抄' + TAG},
               {'add_kp': {'name': 'Белоусов Игорь Юрьевич', 'role': '创始人 / 股东 ООО «Тайле РУС»（bbnt）= 拍板人（邮箱未取）' + TAG, 'email': '', 'source': 'https://saby.ru/profile/7715603560-771501001'}},
               {'add_kp': {'name': 'Любансин Елена Александровна', 'role': 'Генеральный директор ООО «Тайле РУС»（2026-04-16–；saby）' + TAG, 'email': '', 'source': 'https://saby.ru/profile/7715603560-771501001'}},
               {'facts': {'legal_name': 'ООО «Тайле РУС»（ИНН 7715603560；ОГРН 1067746636583；127410 Москва, Алтуфьевское ш., д. 41；营收 3.3 млрд ₽；25 分支；自有品牌 NIKOMAX / NIKOLAN / NETLAN / TLK / GIGALINK（= SB-837）+ 4 代理品牌）', 'founded': '2006-05-29' + TAG,
                          'other': '第 113 批：俄罗斯头部网络设备品牌商 + 分销（Marvell 偏好、多中国供应商）→ **贴标 OEM 30% B BIG，加厚一次（Marvell 管理型 STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM + 工业 STI-288DGGPM / STI-488DGGPM + STH 10G / 25G 作 NIKOMAX / GIGALINK 标第二代工源 + 中性包装 / 自编货号；俄 / 英文，Kuznetsova 直呼 + Rubeko 抄）**' + RU + '；升 A 候选；**Q-33 口径（HRUI / 丰润达在供）= 只推 SmartByte / Marvell 管理 / 工业线，不报 HRUI 同款非管理 PoE**；不点名 ORing / BADU；SB-837 GIGALINK 并线至本户' + TAG}}],
    'SB-837': {'facts': {'legal_name': 'GIGALINK = ООО «Тайле РУС» 自有品牌之一（bbnt.ru；ИНН 7715603560 / ОГРН 1067746636583）→ 并线至 SB-851', 'founded': '2006-05-29（Тайле РУС）' + TAG,
                         'other': '第 113 批：品牌 = SB-851 Тайле 旗下 → **并线（SB-851 主户；GIGALINK 作为其品牌切口写进同一稿；本户不单发）**；Q-33 口径（HRUI 在供）= 只推 SmartByte / Marvell 管理 / 工业线' + TAG}},
    'SB-218': [{'kp_name': 'Anatoly Kovtun', 'role': '市场调研专员（研究档；a.kovtun@）= 收件人' + TAG},
               {'kp_name': 'L. Abrarova', 'role': 'НАГ 研究档联系人（l.abrarova@）= 抄' + TAG},
               {'add_kp': {'name': 'Самоделко Дмитрий Георгиевич', 'role': 'Генеральный директор ООО «НАГ»（2016-09-21–；rusprofile）= 拍板人' + TAG, 'email': '', 'source': 'https://www.rusprofile.ru/id/3282107'}},
               {'facts': {'legal_name': 'ООО «НАГ»（ИНН 6659099112；ОГРН 1046603130881；620110 Екатеринбург, ул. Краснолесья, стр. 12а, этаж 4；2021 营收 7.03 млрд ₽ / 利润 598 млн ₽；股东 Личный фонд «Гладиолус»；自有品牌 SNR）', 'founded': '2004-01-13' + TAG,
                          'other': '第 113 批：自有品牌 SNR 量大、直采中国 ODM、曾回「? ?」→ **贴标 OEM 30% B BIG，加厚一次（SNR 标 Marvell 管理型 STC-4424GCPM / STC-424XGGPM-280W / STC-448XGGPM + 工业 STI 线 + STH 10G / 25G / 100G 第二代工源；俄文为主、参数表直给；Kovtun 直呼）**' + RU + '；升 A 候选；对方需求偏 DWDM / 400G 相干（Saga 不做）→ 稿内只谈交换机' + TAG}}],
    'SB-599': [{'kp_name': 'Massov', 'role': 'Symanitron 研究档 KP（地推；massov@）= 收件人' + TAG},
               {'add_kp': {'name': 'Колбасенко Ольга Евгеньевна', 'role': 'Генеральный директор ООО НПП «Симанитрон-Электроника»（saby）= 拍板人' + TAG, 'email': '', 'source': 'https://saby.ru/profile/6454141571-645201001'}},
               {'facts': {'legal_name': 'ООО НПП «Симанитрон-Электроника»（ИНН 6454141571；ОГРН 1146454002595；410019 Саратов, ул. Крайняя, д. 129, пом. 38-39；生产 Танкистов 55Т；莫斯科实验室 8-я ул. Текстильщиков, 8；工贸部国产交换机登记册；关联 ООО «Символ-Автоматика»）', 'founded': '2014-06-30（品牌 2008）' + TAG,
                          'other': '第 113 批：工业交换机同行制造商（国产登记册）但表内自有 logo 工业 FS / MC 为外购 → **同行 / 贴标二选一：贴标 30% small，一页纸一次（登记册之外的 Symanitron 标工业 MC / 非管理 FS STI-054GP / STI-144GP 板级或整机 + 中性包装；俄 / 英文，Massov 直呼）**' + RU + '；再无回声 → 不动（同行）' + TAG}}],
    'SB-829': [{'kp_name': 'Mokerova Alina', 'role': 'Product Manager（研究档；logist4@red-dst.ru）= 收件人' + TAG},
               {'kp_name': 'Alla Kiyashkina', 'role': 'Product Manager（研究档；logist23@red-dst.ru）= 抄' + TAG},
               {'facts': {'legal_name': 'Optimus（品牌 2011；optimus-cctv.ru / red-dst.ru 运营；品牌运营法人未取；同名 ООО «Оптимус» 多家 ≠（7716642080 已清算 / 9701258974 / 9709026630 待证））', 'founded': '2011（品牌）' + TAG,
                          'other': '第 113 批：自有 logo 商用 PoE、产品经理直达 → **贴标 30% small，一页纸一次（Optimus 标 Marvell 管理型 STC-4424GCPM / STC-424XGGPM-280W + 工业 STI-054GP 第二代工源 + 中性包装；俄 / 英文，Alina 直呼）**' + RU + '；**Q-33 口径（丰润达在供）= 只推 SmartByte / Marvell 管理 / 工业线**' + TAG}}],
    'SB-877': [{'add_kp': {'name': 'Чистова-Макарова Елена Викторовна', 'role': 'Генеральный директор ООО «ЛУИС+»（LTV 品牌实体；list-org）= 拍板人（邮箱未取；收件渠道待补证：luis.ru 表单 / 采购部）' + TAG, 'email': '', 'source': 'https://companies.rbc.ru/id/1157746290680-ooo-obschestvo-s-ogranichennoj-otvetstvennostyu-luis/'}},
               {'add_kp': {'name': 'Вьюнышев Николай Валентинович', 'role': 'Генеральный директор ООО «Компания ЛУИС+»（集团；datanewton）' + TAG, 'email': '', 'source': 'https://datanewton.ru/contragents/1155040002072'}},
               {'facts': {'legal_name': 'ООО «ЛУИС+»（ИНН 7714334756；ОГРН 1157746290680；125124 Москва, ул. 1-я Ямского Поля, д. 28, эт. 3；17 人；LUIS+ 集团 1995 起：ООО «Компания ЛУИС+» 5040079849 / ЛУИС+Сибирь；自有品牌 LTV / LPA / ЛКД / LTC / ЛПТ）', 'founded': '2015-04-01（集团 1995）' + TAG,
                          'other': '第 113 批：大型安防分销集团的自有品牌 LTV（工业 FS / SFP 贴标现中系）→ **贴标 30% B BIG，加厚一次（LTV 标工业 FS / MC STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM + STC-2224GP 第二代工源 + 中性包装 / 自编货号；俄 / 英文；收件渠道待补证）**' + RU + '；升 A 候选；不点名 Hasvio；守界：防爆摄像机线不碰' + TAG}}],
    'SB-884': {'facts': {'legal_name': 'ООО «Бизнес Центр Алгоритм»（БЦА；ИНН 2311218490；ОГРН 1162375029013；350051 Краснодар, ул. Рашпилевская, д. 321, оф. 14；Polyvision™ 商标持有人 + 俄罗斯唯一官方进口商；莫斯科办公 +7 495 620-09-89；总经理未取）', 'founded': '2016（品牌 1998 / 2002）' + TAG,
                         'other': '第 113 批：商标持有人 + 唯一进口商（直接从中国进口贴标）→ **贴标 OEM 30% B BIG，加厚一次（Polyvision 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM（48 口替代其 50 口非管理）+ 中性包装 / 自编货号 + 小 MOQ；俄 / 英文，info@ 点名采购）**' + RU + '；升 A 候选；不点名 ONV' + TAG}},
    # ---------- 第 3/3 RU 13 ----------
    'SB-886': {'facts': {'legal_name': 'SarmatT（品牌 2008；sarmatt.ru；品牌运营法人未取；同名 ООО «Сармат» 多家 ≠）', 'founded': '2008（品牌）' + TAG,
                         'other': '第 113 批：CCTV 品牌、少量自有 logo 商用 PoE → **贴标 30% small，一页纸一次（SarmatT 标 STC-028GP / STC-228GP / STC-2224GP 第二代工源 + 中性包装；俄 / 英文，info@ 一问采购）**' + RU + '；再无回声 → 不动' + TAG}},
    'SB-893': [{'add_kp': {'name': 'Олейник Игорь Валерьевич', 'role': 'Генеральный директор / 100% 股东 ООО «ДССЛ»（2010–；rusprofile；集团 DSSL / TRASSIR）= 拍板人（in@trassir.ru 点名网络产品线采购）' + TAG, 'email': '', 'source': 'https://www.rusprofile.ru/id/2917866'}},
               {'facts': {'legal_name': 'DSSL 集团 / TRASSIR（ООО «ДССЛ» ИНН 7709423841 / ОГРН 1037709044460；ООО «ДССЛ-Первый» 7701081730 2025 营收 9 млрд ₽；НПП «Трассир» 2.1 млрд ₽；105082 Москва, ул. Бакунинская, д. 71, эт. 6；商标 TRASSIR / ACTIVECAM / NEUROSTATION）', 'founded': '2003-05-26' + TAG,
                          'other': '第 113 批：俄罗斯头部安防平台商、自有型号 PoE 全线 → **贴标 OEM 30% B BIG，加厚一次（TRASSIR 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + Marvell 管理型 STC-424XGGPM-280W 第二代工源 + 中性包装 / 自编货号 + 俄文技术包；in@ 点名网络产品线采购）**' + RU + '；升 A 候选；守界：本土生产 / 政府项目叙事不触及' + TAG}}],
    'SB-898': {'facts': {'legal_name': 'ТПГ «Декси» / XVI（ООО «Декси Центр» ИНН 3666173040 / ОГРН 1113668032653；394026 Воронеж, ул. Электросигнальная, д. 1, оф. 8；项目相机实体 ООО «Фотон» 3661060572；莫斯科 БЦ «Агат», Б. Семёновская, 40, стр. 1；仓库 Москва / Воронеж / Челябинск；品牌 XVI 2009 + CYFRON）', 'founded': '2011（Декси Центр；集团 20+ 年）' + TAG,
                         'other': '第 113 批：自有型号 PoE 全线（SWP1104 / 1508 / 1016 / 1016M / 1024，多外壳）现中系代工 → **贴标 OEM 30% B BIG，加厚一次（XVI 标 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM 第二代工源 + 中性包装 / 自编货号 + 2 年保对齐；俄 / 英文，sales@dexi.ru 点名产品经理）**' + RU + '；升 A 候选；不点名 HiSource' + TAG}},
    'SB-430': {'facts': {'legal_name': 'ООО «Протэк»（Protech；pro-tek.pro 页脚；ИНН 5404507902；ОГРН 1145476039840；Новосибирск, ул. Дуси Ковальчук, 378а, корп. 3, оф. 4）— **研究档法人「ООО «Модуль»（СПб；7802791198）」更正：为 Eltex 渠道同行 / 关联待证，≠ 本户法人**', 'founded': '2014-03-31' + TAG,
                         'other': '第 113 批：运营商 / 政企电信设备供应商（Eltex 体系；案例含内务部 / 国家医疗中心）→ **分销 / 集成 20–25% small，一页纸一次（接入 / 汇聚 STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W 第二来源；俄 / 英文，info@ 一问采购）**' + RU + '；守界：不提政府项目；不点名 Eltex / PLANET' + TAG}},
    'SB-870': [{'add_kp': {'name': 'Бобков В. Е.', 'role': 'Руководитель дилерского отдела HUNTER（hunter-cctv.ru）= 收件人（info@ 点名）' + TAG, 'email': '', 'source': 'https://hunter-cctv.ru/o-kompanii-hunter/'}},
               {'facts': {'legal_name': 'HUNTER（hunter-cctv.ru；品牌 2008；自述「基于中国产线推出自有品牌」；品牌运营法人未取；同名 ООО «Хантер» 0504009500 已除名 / 7718742900 待证）', 'founded': '2008（品牌）' + TAG,
                          'other': '第 113 批：预算型 CCTV 品牌、自有 logo PoE HN-SW 系列 → **贴标 30% small，一页纸一次（HUNTER 标 STC-028GP / STC-228GP 第二代工源 + 中性包装 + 小 MOQ；俄 / 英文，Бобков 直呼）**' + RU + '；再无回声 → 不动' + TAG}}],
    'SB-874': {'facts': {'legal_name': 'KENO / FOX（品牌 2012；运营方 ООО «ФКВИДЕО»（FOX 产品文件；Волоколамское ш., 116, стр. 4, оф. 517）；现址 143440 Московская обл., Путилково, тер. Гринвуд, стр. 17, эт. 1, пом. 107；ИНН 未取）', 'founded': '2012（品牌）' + TAG,
                         'other': '第 113 批：双品牌 CCTV、自有 logo PoE 现中系代工 → **贴标 30% small，一页纸一次（KENO / FOX 标 STC-028GP / STC-228GP / STC-2224GP 第二代工源 + 中性包装 / 自编货号；俄 / 英文，info@ 点名采购）**' + RU + '；守界：「Безопасный регион」政府项目线不提；不点名 ONV / 新桥' + TAG}},
    'SB-1064': [{'add_kp': {'name': 'Бабаев Рустам Азизбала оглы', 'role': 'Генеральный директор / 100% 股东 ООО «Порт Депо»（2022–；rusprofile）= 拍板人 / 收件人（sales@ 点名）' + TAG, 'email': '', 'source': 'https://portdepo.ru/legal-info'}},
                {'facts': {'legal_name': 'ООО «Порт Депо»（PORTDEPO；ИНН 7720875009；ОГРН 1227700587927；法定 111394 Москва, ул. Перовская, д. 65, стр. 3；门店 115432 ул. Трофимова, д. 8；Ubiquiti / MikroTik / Aruba / Fortinet 分销；2025 纳税 9.7 млн ₽）', 'founded': '2022-09-19' + TAG,
                           'other': '第 113 批：mik 系分销 + 网店 → **分销 20% small，一页纸一次（SmartByte 商用 STC-2224GP / STC-4424GCPM / STC-424XGGPM-280W 作 mik 替代价位 + STI-144GP；俄 / 英文，Бабаев 直呼）**' + RU + '；不点名 Ubiquiti / MikroTik' + TAG}}],
    'SB-1077': {'facts': {'legal_name': 'Софт-Троник / Soft-Tronik（总部 127018 Москва, ул. Полковая, д. 3, стр. 2；1991 起（德国 Soft-Tronik GmbH 分部 → 1996 独立）；11 分部；俄最大 Dahua 分销 2017 起；IT 认证登记册 №32644；现经营法人 ИНН 未取（旧 ООО «Софт-Троник Нетворкинг» 7731609224 2008–2019 已注销））', 'founded': '1991（业务）' + TAG,
                          'other': '第 113 批：全国性多品牌分销 → **分销 20% B BIG，加厚一次（SmartByte 商用 PoE STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM + Marvell 管理型 STC-424XGGPM-280W 作其网络线第二价位；俄 / 英文，info@ 点名网络产品线采购）**' + RU + '；现法人未取 → 部分坐实；不点名 Dahua / Axis / TP-Link 等' + TAG}},
    'SB-396': [{'add_kp': {'name': 'Букарев Борис Борисович', 'role': 'Генеральный директор / 创始人 ООО «Море Камер»（2019–；rusprofile；业务 2014 起）= 拍板人 / 收件人（mail@ 点名）' + TAG, 'email': '', 'source': 'https://www.rusprofile.ru/id/11693120'}},
               {'facts': {'legal_name': 'ООО «Море Камер»（ИНН 2508134914；ОГРН 1192536004407；692902 Приморский край, г. Находка, ул. Рылеева, д. 13；СПб 门店；Dahua / Ajax / QTech 经销；МЧС 许可；合伙人 Пономарев П.А.）', 'founded': '2019-02-07（业务 2014）' + TAG,
                          'other': '第 113 批：远东小型安防经销 + 安装 → **分销 20% small，一页纸一次（STC-028GP / STC-228GP / STC-2224GP + STI-054GP 一口价 + MOQ 1；俄 / 英文，Букарев 直呼）**' + RU + '；不点名 Utepo / Dahua' + TAG}}],
    'SB-720': {'facts': {'legal_name': 'Unitech-shop.ru（Раменское CCTV + PoE 网店 + 安装；法人未取；同名 ООО «Юнитек» 多家 ≠）', 'founded': '未取' + TAG,
                         'other': '第 113 批：法人未取 + 唯一邮箱 2024-10-09 永久退信 + 微型网店 → **不动（地址失效；B 保留）**；Q-33 HRUI 口径（若有新通道）= 只推 SmartByte / Marvell 管理 / 工业线' + TAG}},
    'SB-848': [{'add_kp': {'name': 'Калистратов Илья Владимирович', 'role': 'Генеральный директор ООО «СетиЛенд»（setilend.ru 反馈页）= 拍板人 / 收件人（mail@ 点名）' + TAG, 'email': '', 'source': 'https://setilend.ru/about/setilend.ru/nashi-rekvizity/'}},
               {'facts': {'legal_name': 'ООО «СетиЛенд»（ИНН 7447215866；ОГРН 1127447013770；454001 Челябинск, пр. Победы, д. 303, корп. 2, пом. 53；5 起仲裁 + 10 起强制执行 → 付款风险）', 'founded': '2012-10-24' + TAG,
                          'other': '第 113 批：网络设备网店（工业以太网 / PoE 栏目）→ **分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-154GP + STC-2224GP 一口价 + MOQ 1；俄 / 英文，Калистратов 直呼）**' + RU + '；付款风险 → 只做 100% 预付' + TAG}}],
    'SB-986': [{'add_kp': {'name': 'Алехина Марина Валерьевна', 'role': 'Генеральный директор ООО «ТЕСТ СОЛЮШН»（sbis / rbc；alekhina@testsol.ru）= 拍板人 / 收件人' + TAG, 'email': 'alekhina@testsol.ru', 'source': 'https://rbc.ru/companies/id/1165074054672-ooo-test-solyushn'}},
               {'facts': {'legal_name': 'ООО «ТЕСТ СОЛЮШН»（ИНН 5036159107；ОГРН 1165074054672；142100 Московская обл., г. Подольск, ул. Тепличная, д. 7Б, кв. 29；3 人；2022 营收 51.9 млн ₽；ISO 9001:2015）', 'founded': '2016-05-31' + TAG,
                          'other': '第 113 批：3 人工业自动化 / 元器件供应商（台系 / 中系工业交换机品牌页）→ **分销 20% small，一页纸一次（STI-054GP / STI-144GP / STI-154GP / STI-288DGGPM 一口价 + MOQ 1 + 3 年保；俄 / 英文，Алехина 直呼）**' + RU + '；不点名 EtherWAN / Advantech / Maiwe' + TAG}}],
    'SB-842': [{'kp_name': 'Alexander', 'role': 'Senior Manager（研究档；admin@kzn-gps.ru；WA = 店铺电话 +7 917 391 05 85）= 收件人' + TAG},
               {'facts': {'legal_name': 'New-LCD / KZN-GPS.ru — 法人 ООО «Фикс»（ИНН 1655262545；ОГРН 1131690005930；420088 Казань, ул. Ново-Азинская, д. 14А；业务 1999 / 网店 2008）', 'founded': '2013（ООО «Фикс»；业务 1999）' + TAG,
                          'other': '第 113 批：mik 系小网店（兼手机配件）→ **分销 20% small，一页纸一次（SmartByte 商用 STC-028GP / STC-228GP / STC-2224GP 作 mik 替代价位 + MOQ 1；俄 / 英文，Alexander 直呼）**' + RU + '；不点名 Ubiquiti / MikroTik' + TAG}}],
    # ---------- Q-33 口径勘误（第 112 批户） ----------
    'SB-395': {'facts': {'other': '第 113 批 Q-33 口径勘误：PoE 现由洪瑞（HRUI）供货 ≠「不碰」（Q-33「不碰」裁定仅针对 SmartByte 经销名单；HRUI 在供户默认「只推 SmartByte / Marvell 管理 / 工业线，不报 HRUI 同款」）→ 第 112 批「不动」改为 **一页纸一次（Mesh / CPE 配套的 Marvell 管理型 STC-4424GCPM / STC-424XGGPM-280W + 工业 STI-288GPM 作 ISP 项目配套，不报非管理 PoE；英文，Ge Shi 直呼）**；再无回声 → 不动' + TAG}},
    'SB-173': {'facts': {'other': '第 113 批 Q-33 口径勘误：交换机现由洪瑞（HRUI）代工贴标 ≠「不碰」→ 第 112 批「不动」改为 **一页纸一次（Inaxsys 标 Marvell 管理型 STC-4424GCPM / STC-424XGGPM-280W + 工业 STI-054GP / STI-144GP 作其 PoE 线之上的管理 / 工业补位 + 中性包装；英文，sales@ 点名 Mark McRae）**；再无回声 → 不动' + TAG}},
    'SB-811': {'facts': {'other': '第 113 批 Q-33 口径勘误：已售 HRUI 同类 PoE → 一页纸切口改为 **只推 SmartByte / Marvell 管理型 STC-4424GCPM / STC-424XGGPM-280W + 工业 STI-054GP / STI-144GP，不报 HRUI 同款非管理 PoE；MOQ 1 一口价**' + TAG}},
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
