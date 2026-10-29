# -*- coding: utf-8 -*-
"""第 121 批（T29-U114，2026-10-29）第 2 段 20 户（KZ 池 4 + ZM 池 4 + HK 池 4 + LB 池 4 + MX 池 4）—— 官方登记核实写入 registry。
KZ 路径首测：БИН = statsnet.co / adata.kz / kyc.kz / niac.kz / ba.prg.kz 1 查即得（3/4，含注册日、ОКЭД、负责人、规模）；官网 реквизиты 自列 БИН；
ZM 路径首测：PACRA 不可 1 查 → 官网 + 领英 / datanyze 补地址与人数 → 部分坐实常态；无邮箱 / hotmail 2 户 0 查；
HK 路径沿用：CR 号靠 inriskable 等镜像（1/4），官网 contact 页 + 领英补地址；
LB 路径首测：无登记库 → kompass.com（所有者姓名 + 成立年 + 地址）/ crunchbase / yelleb 补 → 部分坐实常态；1 户经地址核为迪拜实体 → country_fix 阿联酋；
MX 路径沿用：aviso de privacidad / D&B / tendata 进口记录；域名 2 户 1 查无命中 → 未坐实。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 121
F = '2026-10-29'
KZ = '— 哈萨克斯坦常规：英文稿、20 / 25 / 30 + T/T 预付 100%（哈国银行）+ FOB 深圳 或 DAP 阿拉木图 / 阿斯塔纳（买方清关；EAC 不声称）'
ZM = '— 赞比亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 卢萨卡（买方清关；ZABS 不声称）'
HK = '— 香港常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 香港（免税；OFCA 不声称）'
LB = '— 黎巴嫩常规：英文稿、20 / 25 / 30 + T/T 预付 100%（不接受信用证）+ FOB 深圳 或 DAP 贝鲁特（买方清关）'
MX = '— 墨西哥常规：英文稿（可附西语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP（买方清关；NOM / IFT 不声称）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ---------------- KZ 池 4 ----------------
row('SB-037', 'ТОО «Pulsar Systems» / Pulsar Systems LLP（pulsar.kz；**БИН 100740012554；注册 2010-07-23；法定地址 г. Астана, район Алматы, проспект Бауыржан Момышұлы, дом 2В, к. 16；负责人 Каримов Сабит Мухтарович；ОКЭД 47421（电信设备专卖零售）；阿拉木图办公 ул. Ходжанова 79；表内 UNIPOE 哈萨克斯坦 + 俄罗斯独家代理、ZKTeco / Hikvision 在售**）→ 坐实；无具名邮件 KP（info@）；未跟进', 'KZ',
    'KZ · 1 次检索：statsnet.co/companies/kz/27130484（PULSAR SYSTEMS, ТОО, БИН 100740012554；Астана, проспект Бауыржан Момышұлы, дом 2в；Дата регистрации 23.07.2010）+ pk.adata.kz（Директор Каримов Сабит Мухтарович；ОКЭД 47421；к. 16；Алматы, ул. Ходжанова, 79）+ kyc.kz 同号；2026-10-29', 'https://statsnet.co/companies/kz/27130484',
    'БИН 100740012554', '存续（企业库 2026）', '2010-07-23', 'ТОО（有限责任合伙）', '电信 / 安防设备分销与零售（阿斯塔纳 + 阿拉木图）', 'пр. Бауыржан Момышұлы 2В, оф. 16, район Алматы, Астана 010000, Kazakhstan', '小型',
    ['Sabit Karimov（Каримов Сабит Мухтарович）— Директор（adata.kz 2026-10-29；无公开邮箱）→ 收件 info@pulsar.kz Attn: Mr. Karimov'],
    '**PoE 交换机品牌独家代理（哈 + 俄）→ 分销 20% B，一页纸一次（PM3018GSNL 类 16 PoE + 2 SFP 对位 STC-2216GP $63–76 / STC-2224GP $86 / STC-4424GCPM $165 一口价 + MOQ 1 + 付费样机；在代品牌不点名）' + KZ + '**；俄罗斯转售部分 = 买方自理；回信 → 加厚',
    '分销 20%；一页纸一次（预付 100%）；坐实（БИН + 注册日 + 地址 + 负责人 + ОКЭД）。')
row('SB-622', 'ТОО «Авантаж Маркет» Avantazh Market（market-telecom.kz；**官网 реквизиты 自列 БИН 221040045999（2022-10 注册；150000 Петропавловск, ул. Нурсултана Назарбаева 133, НП1 — ba.prg.kz 同）；前身 / 关联 ТОО «Авантаж Маркет-телеком» БИН 170740023007（2017；Астана, ул. Дотык 18）；自述 2010 年起 16 年、阿斯塔纳 / 阿拉木图 / 彼得罗巴甫洛夫斯克三仓；+7 7172 97 84 70 / +7 727 237 90 53；表内 TP-Link / Dahua / Hikvision / Ubiquiti / MikroTik + ONV / Witech / Planet 交换机**）→ 坐实；无具名 KP（info@）；群发 18 次无回复', 'KZ',
    'KZ · 1 次检索：market-telecom.kz/about_shop（Реквизиты ТОО «Авантаж Маркет» БИН 221040045999；150000 Петропавловск ул. Нурсултана Назарбаева, 133, НП1；info@market-telecom.kz）+ ba.prg.kz/591010000-petropavlovsk/221040045999（同址，Проверено 12.10.2026）+ mp.kz（ТОО "Авантаж Маркет-телеком" БИН 170740023007；Астана, ул. Дотык, 18）；2026-10-29', 'https://market-telecom.kz/about_shop',
    'БИН 221040045999（关联 ТОО «Авантаж Маркет-телеком» БИН 170740023007）', '存续（e-gov 核验 2026-10-12）', '2022-10（现法人；业务 2010 起）', 'ТОО（有限责任合伙）', '通信 / 安防 / IT 设备网店 + 工程（彼得罗巴甫洛夫斯克 / 阿斯塔纳 / 阿拉木图）', 'ул. Нурсултана Назарбаева 133, НП1, Петропавловск 150000, Kazakhstan', '小型',
    ['（无具名 KP：info@market-telecom.kz；Attn: Отдел закупок / Purchasing）'],
    '**多品牌网店 + 在售 ONV / Planet 类交换机 → 分销 20% B，最后一次一页纸（STC-028GP $28 / STC-2216GP / STC-2224GP $86 / STI-154GP 一口价 + MOQ 1 + 付费样机；在售品牌不点名）' + KZ + '**；18×0 → 再无回声 → 不动',
    '分销 20%；最后一次一页纸（预付 100%）；坐实（官网自列 БИН + e-gov 核验地址 + 关联法人）。')
row('SB-799', 'ТОО «VERTEX INVADER»（**БИН 181140013835；注册 2018（niac 2018-11-13 / wikicity 2018-01-13 口径不一）；г. Астана, район Байқоңыр, ул. Александра Пушкина 41/2；负责人 Нурпеисова Алина Бакытжановна；ОКЭД 47.99.9 / 其他机械设备批发；小型企业（11–15 人）；ETS 招标平台参与者**）→ 坐实；表内国别「俄罗斯」已更正为哈萨克斯坦；邮箱 mail.ru、无兴趣记录、业务与我方无对口；未跟进', 'KZ',
    'KZ · 1 次检索：ets-tender.kz/firms/too-vertex-invader/34696（ТОО "VERTEX INVADER"；010000 Астана, улица Александра Пушкина, здание 41/2；БИН 181140013835）+ niac.kz/181140013835（Действующая；Нурпеисова Алина Бакытжановна；ОКЭД 47.99.9）+ wikicity.kz（Оптовая торговля прочей техникой；Малое предприятие 11-15 чел.）；2026-10-29', 'https://niac.kz/181140013835',
    'БИН 181140013835', '存续（niac 2026）', '2018', 'ТОО（有限责任合伙）', '其他设备批发 / 店外零售（阿斯塔纳；招标供应商）', 'ул. Александра Пушкина 41/2, район Байқоңыр, Астана 010000, Kazakhstan', '小型（11–15）',
    ['Alina Nurpeisova（Нурпеисова Алина Бакытжановна）— Руководитель（niac 2026-10-29；无公开邮箱）；表内 invest_01otp@mail.ru 身份不明'],
    '**招标杂货供应商 + 无对口需求 + mail.ru 身份不明 → 不动（B 保留；来询按分销 20% 报 + 预付 100%）**' + KZ, '不动（查无对口业务）；坐实（БИН + 地址 + 负责人 + ОКЭД）。')
row('SB-941', 'ТОО «CompTek CA»（comptek.kz；**zoon / tel-spravochnik / facebook：г. Алматы, проспект Райымбека 165А, 3 этаж, офис 6；+7 727 246-82-21 / -22；n.drobysheva@comptek.kz；企业级 IT 分销（Cisco / Dell / Ubiquiti / Avaya / F5 / SUSE 等，研究档）**）；БИН 1 查未得 → 部分坐实；KP Faim Ahmetzjnov（comtek@mail.ru，阿里 RFQ 来源）；需求 PoE 分离器（不供）；未跟进', 'KZ',
    'KZ · 1 次检索：zoon.kz/almaty/shops/distribyutorskaya_kompaniya_comptek_ca（Алматы, Райымбека проспект, 165а, 3 этаж; 6 офис；+7 (727) 246-82-21；comptek.kz）+ almati.tel-spravochnik.ru（CompTek CA, ТОО）+ facebook.com/CompTekCA（n.drobysheva@comptek.kz；+7 7272 46 82 22）；БИН 未得；2026-10-29', 'https://zoon.kz/almaty/shops/distribyutorskaya_kompaniya_comptek_ca/',
    '未取（БИН 1 查未得）', '营业中（2024-11 活动贴）', '未取', 'ТОО（有限责任合伙）', '企业级 IT / 网络设备分销（阿拉木图）', 'пр. Райымбека 165А, 3 этаж, офис 6, Алматы, Kazakhstan', '小型',
    ['Faim Ahmetzjnov — 联系人（研究档 KP；comtek@mail.ru，阿里 RFQ）'],
    '**原厂级 IT 分销（Cisco 等）+ 唯一需求 PoE 分离器（不供）→ 不动（B 保留；来询按分销 20% 报 STC 商用线 + 预付 100%）**' + KZ, '不动（产品不对位）；部分坐实（名录地址 + 电话；БИН 未取）。')

# ---------------- ZM 池 4 ----------------
row('SB-102', 'Denso Electronic Solutions（densoelectronics.com；**官网：Suite 02-37 Compensation House, Broadway / Moffat Roads, Ndola, Zambia；1997 年起电子元件供应 + ICT 方案；+260 212 615190 / 615367；WA +260 977 823 625；sales@**）；PACRA 号 1 查未得 → 部分坐实；表内「网站卖的比较杂」；KP Joedy Snafu；需求工业 MC（仅 STC-110XGE）；未跟进', 'ZM',
    'ZM · 1 次检索：densoelectronics.com（Denso Electronic Solutions, based in Ndola CB, trusted source for electronic supplies since 1997；Suite 02-37 Compensation House - Broadway/ Moffat Roads, Ndola；+260212615190；Sales@densoelectronics.com）+ zambiadirectory.com（Ndola, Copperbelt）；PACRA 未得；2026-10-29', 'https://www.densoelectronics.com/',
    '未取（PACRA 号 1 查未得）', '营业中（官网 2026）', '1997', 'Ltd（推定）', '电子元件 / ICT 设备供应（恩多拉，铜带省）', 'Suite 02-37 Compensation House, Broadway / Moffat Roads, Ndola, Zambia', '小型',
    ['Joedy Snafu — 联系人（研究档 KP；sales@densoelectronics.com）= 收件人'],
    '**电子 / ICT 综合供应商（有进口经验）→ 分销 20% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-110XGE $65 一口价 + MOQ 1；千兆工业 MC 不供明说）' + ZM + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（官网地址 + 成立年；PACRA 未取）。')
row('SB-1120', 'Obmac Systems（obmacsystems.com；**官网：2007-02-13 成立，ICT / 电气 / 机械项目与采购（恩多拉起家，现卢萨卡）；创始人 / CEO Pythias Kachepa（领英：Director Operations 2007–09 → CEO 2009–今，2013–14 南苏丹 Toplinks）；datanyze 约 7 人、营收约 $2.6M**）；PACRA 号 1 查未得 → 部分坐实；**2024-01 已成单 $9,350（PI 包「gg」）**；2025 起 9 次群发无回复；KP Pythias Kachepa（pythiask@gmail.com）', 'ZM',
    'ZM · 1 次检索：obmacsystems.com（founded on February 13th 2007；Telecommunications, Electrical and Mechanical projects and procurement；Pythias Kachepa Founder）+ linkedin.com/in/pythias-kachepa-7a097618（CEO Obmac Systems Feb 2009 - Present；Director Operations 2007-2009 Ndola）+ datanyze（Employees 7；Revenue $2.6M）；PACRA 未得；2026-10-29', 'http://obmacsystems.com/',
    '未取（PACRA 号 1 查未得）', '营业中（官网 + 领英）', '2007-02-13', 'Ltd（推定）', 'ICT / 电气 / 机械项目承包与采购（卢萨卡）', '未取（Lusaka, Zambia；起家 Ndola）', '微型（约 7 人）',
    ['Pythias Kachepa — Founder / CEO / Managing Director（官网 + 领英 2026-10-29 吻合；研究档 KP pythiask@gmail.com）= 收件人'],
    '**★ 已成单（2024-01 $9,350）+ 创始人 CEO 为 KP → 复购一页纸一次（STC-4248 系列复购价 + STI-154GP / STI-288DGGPM $137 太阳能 EPC 配套 DIN 机 + MOQ 1）' + ZM + '**；Simon 定级「gg 难复购」→ B 保留，回信即升 A 候选',
    '复购（集成商 25%）；一页纸一次（预付 100%）；部分坐实（官网成立日 + 领英 CEO；PACRA 未取）；★ 回信即升。')
row('SB-222', '赞比亚 WhatsApp 联系人（+260 97；**无邮箱 / 姓名 / 公司 → 0 查**）— WA 5 次实质回复，「小工业机近期可能有需求」；2026-06 主动问价；无群发', 'ZM',
    '0 查（无邮箱 / 公司）；2026-10-29', '', '0 查', '互动中（WA 5 次）', '—', '未知', '未知（赞比亚）', '未取', '未知',
    ['（未具名；WA +260 97…）'],
    '**WA 多次实质回复 + 工业小机需求 → 集成商 25% B，WA 一页纸一次（STI-054GP / STI-154GP / STI-280GE $46.6 一口价 + MOQ 1 + 付费样机）' + ZM + '**；同时问公司名 / 邮箱（一句话）',
    '集成商 25%；WA 一页纸一次（预付 100%）；0 查（无身份）。')
row('SB-865', 'Kennedy Bulaya（hotmail；**无公司名 → 0 查**）— 赞比亚 IT 承包 / 网络，2022 起多次与 e. 账号来往；需求 Cisco 兼容交换机 + 10G DAC（不供）；WA 无回复', 'ZM',
    '0 查（hotmail + 无公司名）；2026-10-29', '', '0 查', '互动中（2022–）', '—', '个人 / 微型', 'IT 承包（赞比亚）', '未取', '微型',
    ['Kennedy Bulaya — 联系人（研究档 KP；hotmail）'],
    '**需求 Cisco 兼容 + DAC（不供）+ 无公司 → 不动（B 保留；来询按集成商 25% 报 STC-4424GCPM $165 + 预付 100%）**' + ZM, '不动（产品不对位 + 个人）；0 查。')

# ---------------- HK 池 4 ----------------
row('SB-1027', 'Everbest Technologies Limited 永佳科技有限公司（everbesthk.com；**inriskable 镜像：CR No. 334414，BR No. 15215848；官网 contact：14/F Wing Hang Insurance Building, 11 Wing Kut Street, Central；+852 2541 2982；sales@；1991 年起港澳代理（ATEN 官方 where-to-buy 2026 列名；研究档 Zyxel / LevelOne / DrayTek 等）**）→ 坐实；KP Allen Chan（Director）/ Ariel Cheng（PM）；未跟进', 'HK',
    'HK · 1 次检索：inriskable.com/business_info/company/hk/15215848（永佳科技有限公司 EVERBEST TECHNOLOGIES LIMITED；Business registration number 15215848；Company registration number 334414）+ everbesthk.com/contact（14th Floor, Wing Hang Insurance Building, 11 Wing Kut Street, Central；(852) 2541 2982；since 1991）+ aten.com where-to-buy HK（Everbest Technologies Ltd.）；2026-10-29', 'https://www.inriskable.com/business_info/company/hk/15215848',
    'CR No. 334414；BR No. 15215848', '存续（官网 + ATEN 2026 列名）', '约 1991（自述）', 'Limited（私人有限）', 'IT / 网络产品港澳分销（中环）', '14/F Wing Hang Insurance Building, 11 Wing Kut Street, Central, Hong Kong', '小型',
    ['Allen Chan — Director（研究档 KP；everbesthk.com）= 收件人', 'Ariel Cheng — Product Manager（研究档 KP）'],
    '**多品牌网络产品分销（在代 LevelOne / Zyxel 类交换机）→ 分销 20% B，一页纸一次（STC-028GP $28 / STC-2224GP $86 / STC-4424GCPM $165 / STI-154GP 一口价 + MOQ 1 + 付费样机；在代品牌不点名）' + HK + '**；回信 → 加厚',
    '分销 20%；一页纸一次（预付 100%）；坐实（CR + BR 号 + 地址）。')
row('SB-219', 'Siera Electronics（sieraelectronics.com；Siera Holding Group 成员，面向拉美西语市场；**领英 / contactout：565-567 Nathan Road, Unit 2201B, 22/F, Kowloon；1995 年成立；自有品牌安防（Sieco 摄像机、门禁、对讲、音响）；11–50 人（领英自报 201–500 偏高）**）；CR 号 1 查未得 → 部分坐实；表内「商用 PoE 用 ONV，自己的 label」；KP Mauro Fleitas（Electronic Engineer，venta@）；群发 18 次无回复', 'HK',
    'HK · 1 次检索：hk.linkedin.com/company/siera-electronics（565-567 Nathan Road Unit 2201B, 22/F Kowloon；Founded 1995；manufactures … Electronic Security, CCTV, Access Control）+ contactout.com（11-50 employees；same address）；CR 未得；2026-10-29', 'https://hk.linkedin.com/company/siera-electronics',
    '未取（CR 号 1 查未得）', '营业中（领英 2026 更新）', '1995', 'Limited（推定）', '自有品牌安防电子（九龙；拉美市场）', '565-567 Nathan Road, Unit 2201B, 22/F, Kowloon, Hong Kong', '小型（11–50）',
    ['Mauro Fleitas — Electronic Engineer（研究档 KP；venta@sieraelectronics.com）= 收件人'],
    '**自有 label 商用 PoE 在售（他牌贴标）→ 贴标 OEM 30% B，最后一次一页纸（STC-028GP $28 / STC-2216GP / STC-2224GP $86 Siera 贴标 + MOQ + 付费样机；在供品牌不点名；西语备注）' + HK + '**；18×0 → 再无回声 → 不动',
    '贴标 OEM 30%；最后一次一页纸（预付 100%）；部分坐实（领英地址 + 成立年；CR 未取）。')
row('SB-705', 'Eware Networks Limited（eware.com.hk；**官网 contact：Unit 2102-03, 21/F, Two Sky Parc, 51 Hung To Road, Kwun Tong；+852 2565 0165；info@ / sales@；广州 / 深圳支持热线；whois 旧址 Rm 1107 Futura Plaza, How Ming Street；视频会议 / IP 电话 / UC 方案商（研究档 Yealink 类）**）；CR 号 1 查未得 → 部分坐实；KP Ivan Lau（System Engineer）；群发 8 次无回复', 'HK',
    'HK · 1 次检索：eware.com.hk/en/contact_us（Head Office Unit 2102-03, 21/F, Two Sky Parc, 51 Hung To Road, Kwun Tong；+852 25650165；info@eware.com.hk）+ eware.com.hk career（Eware Networks Limited）+ webrate whois（EWARE NETWORKS LTD；Rm.1107, Futura Plaza）；CR 未得；2026-10-29', 'https://www.eware.com.hk/en/contact_us/',
    '未取（CR 号 1 查未得）', '营业中（官网在）', '未取', 'Limited（私人有限）', 'UC / 视频会议 / IP 电话方案集成（观塘；穗深支持）', 'Unit 2102-03, 21/F, Two Sky Parc, 51 Hung To Road, Kwun Tong, Kowloon, Hong Kong', '小型',
    ['Ivan Lau — System Engineer（研究档 KP；info@eware.com.hk）= 收件人'],
    '**UC 集成商（IP 话机 / AP 供电配套）→ 集成商 25% B，最后一次一页纸（STC-2216GP / STC-2224GP $86 / STC-4424GCPM $165 一口价 + MOQ 1 + 付费样机）' + HK + '**；8×0 → 再无回声 → 不动',
    '集成商 25%；最后一次一页纸（预付 100%）；部分坐实（官网地址 + 电话；CR 未取）。')
row('SB-717', 'SkyWare ProTech Limited（skyware.com.hk；**官网 contact：Room 3806A, 38/F, Cable TV Tower, 9 Hoi Shing Road, Tsuen Wan；+852 3106 0868；sales@；tradeeasy 同址；2017 年 SensMax 客流系统经销时名 Skyware Technologies Limited（Wing Hing Industrial Bldg, Tsuen Wan）；可编程网络设备 HMP200（研究档）**）；CR 号 1 查未得 → 部分坐实；无具名 KP；群发 8 次无回复', 'HK',
    'HK · 1 次检索：skyware.com.hk/en/contact.php（SkyWare ProTech Limited；Room 3806A, Cable TV Tower 9 Hoi Shing Road, Tsuen Wan；(852) 3106 0868；sales@skyware.com.hk）+ tradeeasy.com/supplier/841625（Skyware Protech Limited；同址）+ sensmax.eu 2017（Skyware Technologies Limited）；CR 未得；2026-10-29', 'http://www.skyware.com.hk/en/contact.php',
    '未取（CR 号 1 查未得）', '营业中（官网在）', '约 2001（自述）', 'Limited（私人有限）', '可编程网络 / 楼宇 IoT 设备（荃湾）', 'Room 3806A, 38/F, Cable TV Tower, 9 Hoi Shing Road, Tsuen Wan, N.T., Hong Kong', '小型',
    ['（无具名 KP：sales@skyware.com.hk；Attn: Sales Manager）'],
    '**楼宇 IoT / 可编程设备商（配套工业小机）→ 集成商 25% B，最后一次一页纸（STI-054GP / STI-154GP / STI-280GE $46.6 一口价 + MOQ 1）' + HK + '**；8×0 → 再无回声 → 不动',
    '集成商 25%；最后一次一页纸（预付 100%）；部分坐实（官网地址 + 电话；CR 未取）。')

# ---------------- LB 池 4 ----------------
row('SB-202', 'Engineering Group Contractors (EGC)（egc-lb.com；**官网 contact：Beirut, Kornich El Mazraa, Ibn El Asir St., Borj Al Jazeera Bldg.；+961 1 701546；info@；crunchbase：安防设备分销商，11–50，创始人 / GM Mohammad Hammoud（= 研究档 KP ✓）；RocketReach：1988 年成立、约 7 人、避雷接地系统 + 安防分销 / 集成**）；商业登记号 1 查未得 → 部分坐实；曾谈 30 台 2 光 10 电环网（研究档）；WA 19 次无实质回复', 'LB',
    'LB · 1 次检索：egc-lb.com/contact（Lebanon, Beirut, Kornich El Mazraa, Ibn El Asir St., Borj Al Jazeera Bldg.；info@egc-lb.com）+ crunchbase（distributor of electronic and security equipment；11-50；Mohammad Hammoud Founder and General Manager；+961 1 701546）+ rocketreach（Founded 1988；Employees 7；distributors/Integrator of security equipment and Lightning-Earthing Systems）；登记号未得；2026-10-29', 'https://egc-lb.com/contact',
    '未取（贝鲁特商业登记号 1 查未得）', '营业中（官网 2025-09）', '1988', 'SARL（推定）', '安防设备分销 / 集成 + 避雷接地（贝鲁特）', 'Borj Al Jazeera Bldg., Ibn El Asir St., Corniche El Mazraa, Beirut, Lebanon', '小型（7–50）',
    ['Mohammad Hammoud — Founder / General Manager（crunchbase + 领英 2026-10-29 吻合；研究档 KP egc@egc-lb.com）= 收件人'],
    '**GM 为 KP + 曾谈 30 台环网 → 集成商 25% B，最后一次一页纸（STI-288DGGPM $137 ×30 环网 ERPS 一口价 + STC-228GP $33 接入；光端机 / VC 不供明说）' + LB + '**；19×0 → 再无回声 → 不动',
    '集成商 25%；最后一次一页纸（预付 100%）；部分坐实（官网地址 + 企业库成立年 + GM；登记号未取）。')
row('SB-296', 'BHS Media / BHS Telecommunications（bhs-media.com；**官网 Contact-Us：Head Office No.401, Building No.1, Dubai Media City, Sheikh Zayed Road, Dubai, UAE；+971 4 551 5523；info@；ZoomInfo 约 20 人；卫星上行 / 转播车 / 远程制作服务商 → 表内国别「黎巴嫩」= KP 电话归属，实体在迪拜 → country_fix 阿联酋**）；迪拜执照号未取 → 部分坐实；KP Khalil Haidar（Director）；需求 HDMI over IP 延长（不供）；未跟进', 'AE',
    'AE · 1 次检索：bhs-media.com/Contact-Us（Head Office: No.401, Building No.1, Dubai Media City, Sheikh Zayed Road, Dubai, UAE；Tel +97145515523）+ zoominfo.com/c/bhs-media/375098581（20 employees；MPEG2/4 DVB-S/S2 … BHS TELECOMMUNICATIONS）；执照号未得；2026-10-29', 'http://bhs-media.com/Contact-Us',
    '未取（Dubai Media City 执照号 1 查未得）', '营业中（官网 + ZoomInfo）', '未取', 'FZ-LLC（推定，Dubai Media City）', '卫星上行 / 广播传输服务（迪拜媒体城）', 'No.401, Building No.1, Dubai Media City, Sheikh Zayed Road, Dubai, UAE', '小型（约 20 人）',
    ['Khalil Haidar — Director（研究档 KP；k.haidar@bhs-media.com）'],
    '**广播 / 卫星服务商 + 需求 HDMI over IP（不供）→ 不动（B 保留；来询按集成商 25% 报 STC-4424GCPM $165 IP 制作网交换）— 阿联酋常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 迪拜（买方清关）**',
    '不动（产品不对位 + 非目标行业）；部分坐实（官网地址 + 人数；执照号未取）；country_fix 阿联酋。')
row('SB-324', 'Melhem Trading Co. SARL (MTCO)（mtco-lb.com；**kompass：Ground floor, Riachi building, Dora highway, Bauchrieh (Metn)；2004 年起（黎巴嫩 + 尼日利亚）；所有者 Adnan A. Melhem（= 研究档 KP ✓）/ Rouba N. Khoury / Jad A. Melhem；进口分销 CCTV / 线缆 / 灯光 / 音响 / 通信 / 门禁，自有产品（韩 / 中 / 台代工）；+961 1 245 000；info@**）；商业登记号 1 查未得 → 部分坐实；KP Adnan Melhem（MD）；未跟进', 'LB',
    'LB · 1 次检索：lb.kompass.com/c/melhem-trading-co-sarl/lb023964（Melhem Trading Co. Sarl；Ground floor, Riachi building, Dora highway, Bauchrieh (Metn)；established since 2004 in Lebanon and Nigeria；Main owners Mr. Adnan A Melhem, Ms. Rouba N Khoury, Mr. Jad A Melhem；own products … Korea, China, Taiwan）+ crunchbase（11-50；+961 1 245 000；info@mtco-lb.com）+ yelleb（Dora, Beirut）；登记号未得；2026-10-29', 'https://lb.kompass.com/c/melhem-trading-co-sarl/lb023964/',
    '未取（商业登记号 1 查未得）', '营业中（官网 + 名录）', '2004', 'SARL', 'CCTV / 线缆 / 灯光 / 通信进口分销 + 自有品牌（Bauchrieh, Metn）', 'Ground floor, Riachi Building, Dora Highway, Bauchrieh (Metn), Lebanon', '小型（11–50）',
    ['Adnan Melhem — Owner / Managing Director（kompass 2026-10-29 吻合；研究档 KP melhem@mtco-lb.com）= 收件人', 'Jad A. Melhem — Owner（kompass；无公开邮箱）', 'Rouba N. Khoury — Owner（kompass；无公开邮箱）'],
    '**进口分销商 + 自有品牌代工经验 → 分销 20%（STC-028GP $28 / STC-2216GP / STC-2224GP $86）↔ 贴标 OEM 30% 双轨 B，一页纸一次（MOQ 1 / 贴标 MOQ + 付费样机）' + LB + '**；回信 → 加厚',
    '分销 20% ↔ 贴标 30% 双轨；一页纸一次（预付 100%）；部分坐实（kompass 地址 + 成立年 + 所有者；登记号未取）。')
row('SB-327', 'Techno Tower SARL（technotower-lb.com；**kompass：Ground floor, Abou Karam 1 building, Jdeideh (Metn), P.O. Box 90-1776；成立 1998（官网口径 1989）；所有者 Fadi J. Abou Jaoudeh / Grace Y. Abou Jaoudeh；自动化 / 安防 / CCTV / 消防 / 卫星 / 灯光设备进口分销商**）；商业登记号 1 查未得 → 部分坐实；KP Amine Abou Jaoude（GM，家族同姓）2024-04 问价（研究档）；无回复', 'LB',
    'LB · 1 次检索：lb.kompass.com/c/techno-tower-sarl/lb015188（Techno Tower Sarl；Ground floor, Abou Karam 1 building, Jdeideh (Metn) P.O.Box 90-1776；Founded in 1998；Main owners Mr. Fadi J Abou Jaoudeh, Ms. Grace Y Abou Jaoudeh；Distributor Service Importer）+ indexoflebanon（Techno Tower, Jdeideh）；登记号未得；2026-10-29', 'https://lb.kompass.com/c/techno-tower-sarl/lb015188/',
    '未取（商业登记号 1 查未得）', '营业中（官网 + 名录）', '1998（官网 1989）', 'SARL', '自动化 / 安防 / CCTV / 消防 / 灯光进口分销（Jdeideh, Metn）', 'Ground floor, Abou Karam 1 Building, Jdeideh (Metn), P.O. Box 90-1776, Lebanon', '小型',
    ['Amine Abou Jaoude — General Manager（研究档 KP；amine@technotower-lb.com）= 收件人', 'Fadi J. Abou Jaoudeh — Owner（kompass 2026-10-29；无公开邮箱）'],
    '**进口分销商 + GM 曾问价 → 分销 20% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2216GP / STC-2224GP $86 一口价 + MOQ 1 + 付费样机）' + LB + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；部分坐实（kompass 地址 + 成立年 + 所有者；登记号未取）。')

# ---------------- MX 池 4 ----------------
row('SB-703', 'Engitel（engitel.com.mx；**1 查仅命中意大利 Engitel S.p.A.（engitel.com，米兰）→ 墨西哥本体未命中 → 未坐实**；研究档：IT 咨询 / 网络小型企业，自站 RFQ「2 光 10 电」）；KP Enrique Camberos；无回复', 'MX',
    'MX · 1 次检索：「"Engitel" engitel.com.mx S.A. de C.V.」→ engitel.com/en/privacy（Engitel S.p.A, Via Zarotto 6, Milan）≠ 本户；无墨西哥命中；2026-10-29', '', '未取（1 查未命中本体）', '营业中（研究档官网）', '未取', 'S.A. de C.V.（推定）', 'IT 咨询 / 网络（墨西哥）', '未取（Mexico）', '微型（推定）',
    ['Enrique Camberos — 联系人（研究档 KP；ecamberos@engitel.com.mx）= 收件人'],
    '**自站 RFQ 2 光 10 电 → 集成商 25% B，一页纸一次（STI-288DGGPM $137 2 SFP + 8 GE 或 STC-2216GP 16+2 一口价 + MOQ 1；西语备注）' + MX + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；未坐实（1 查无命中）。')
row('SB-892', 'Telcofusion（telcofusion.com.mx；**1 查无命中 → 未坐实**；gmail 联系）— 电信承包 / 安装商（研究档）；需求反向 PoE（不供）+ 2024-08 问 10G MC ×4；KP Jose Gregorio；WA 15 次无实质回复', 'MX',
    'MX · 1 次检索：「"Telcofusion" telcofusion.com.mx」→ 无结果；2026-10-29', '', '未取（1 查无命中）', '未知', '未取', '未取', '电信承包 / 安装（墨西哥）', '未取（Mexico）', '微型（推定）',
    ['Jose Gregorio — 联系人（研究档 KP；telcofusion1@gmail.com）= 收件人'],
    '**曾问 10G MC ×4 → 集成商 25% B，最后一次一页纸（STC-110XGE $65 ×4 一口价 + 运费；反向 PoE 不供明说；西语备注）' + MX + '**；15×0 → 再无回声 → 不动',
    '集成商 25%；最后一次一页纸（预付 100%）；未坐实（1 查无命中）。')
row('SB-927', 'RARMX Engineering, S.A. de C.V.（rarmx.com.mx；**tendata 进口记录：2025-08 自中 / 美 7 家供应商进口控制模块 / 过滤设备件（HS 9027 / 9030 / 9026）→ 真实进口主体；研究档：蒙特雷水处理 / 工程（+52 81）**；RFC / 地址 1 查未得 → 部分坐实；**阿里巴巴 RTS 已成单「5 电口」**；KP Marisol Mendoza（info@）；需求小工业机', 'MX',
    'MX · 1 次检索：tendata.com/en/supplier/rarmx-engineering-sa-de-cv（RARMX ENGINEERING SA DE CV；Mexico；rarmx.com.mx；imported CONTROL MODULE, FILTER HOLDER, PARTS OF FILTRATION EQUIPMENT 08 Aug 2025；7 suppliers from China and United States）；RFC / 地址未得；2026-10-29', 'https://www.tendata.com/en/supplier/rarmx-engineering-sa-de-cv-MEXI31753e9e9e4fdc3f8b4320b2d01d1f14.html',
    '未取（RFC 1 查未得；法人形式 S.A. de C.V. 已核）', '营业中（2025-08 进口记录）', '未取', 'S.A. de C.V.', '水处理 / 工程（蒙特雷）', '未取（Monterrey, N.L., Mexico）', '小型（推定）',
    ['Marisol Mendoza — 联系人（研究档 KP；info@rarmx.com.mx）= 收件人'],
    '**★ 阿里 RTS 已成单（5 电口）+ 真实进口主体 → 复购一页纸一次（STI-054GP / STI-280GE $46.6 / STI-154GP 水厂 DIN 机一口价 + MOQ 1；西语备注）' + MX + '**；回信即升 A 候选',
    '复购（集成商 25%）；一页纸一次（预付 100%）；部分坐实（进口记录 + 法人形式；RFC 未取）；★ 回信即升。')
row('SB-960', 'Electrónica Steren, S.A. de C.V.（steren.com.mx；**D&B / verif：Biólogo Maximino Martínez No. 3408, Col. San Salvador Xochimanca, Azcapotzalco, CDMX 02870；电子产品批发 + 自有品牌连锁零售（墨西哥 / 拉美）；volza：进口 69,873 票 / 539 家供应商；D&B 主要负责人 Goyazlay Keri González Rodríguez**）；RFC 未取 → 部分坐实（大型）；表内「自有品牌商用 PoE，HRUI 在供」→ Q-33 口径待 Simon；无具名 KP（info@）；未跟进', 'MX',
    'MX · 1 次检索：dnb.com（Electrónica Steren, S.A. de C.V.；Biólogo Maximino Martínez No. 3408 San Salvador Xochimanca, Azcapotzalco 02870；Key Principal Goyazlay Keri González Rodríguez）+ verif.com（Active；4652 Wholesale of electronic and telecommunications equipment）+ volza（69,873 import shipments；539 suppliers）；RFC 未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.electr%C3%B3nica_steren_sa_de_cv.d226ba7d6e837eca174c082fca0c32c6.html',
    '未取（RFC 不公开）', 'Active（verif）', '未取（1956 起，研究档）', 'S.A. de C.V.', '电子产品批发 + 自有品牌连锁零售（墨西哥城）', 'Biólogo Maximino Martínez No. 3408, Col. San Salvador Xochimanca, Azcapotzalco, Ciudad de México 02870, Mexico', '大型（连锁）',
    ['Goyazlay Keri González Rodríguez — Key Principal（D&B 2026-10-29；无公开邮箱）；收件 info@steren.com.mx'],
    '**自有品牌商用 PoE 且 HRUI 在供 → Q-33 口径待 Simon（只推 SmartByte / Marvell 管理 + 工业线：STC-4424GCPM $165 / STI 系列贴标 OEM 30%）→ 口径定前不动（B 保留）**' + MX,
    '不动（Q-33 口径待定；同 SB-523 / SB-1102）；部分坐实（D&B 地址 + 进口记录；RFC 未取）。')
