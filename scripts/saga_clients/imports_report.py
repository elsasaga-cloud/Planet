"""T29-U62 · 进口记录（公开海关数据）总表生成器。
读取 data/saga_clients/imports/*.json（imports_store.put 写入的逐户查询结果）+ entities.json + dims.json，
输出 docs/进口记录_公开海关_<date>.md：边界说明 / 关键发现（手写）/ 逐户总表 / 查无名单 / 新线索（海关里出现、库里没有的美国进口商）/ 第七节其他国家（第 81 批，T29-U63）。
重跑：python3 scripts/saga_clients/imports_report.py
"""
import json, os, sys, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
IMP = os.path.join(DATA, 'imports')
TODAY = dt.date.today().isoformat()
OUT = os.path.join(ROOT, 'docs', f'进口记录_公开海关_{TODAY}.md')

E = {e['code']: e for e in json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))}
DIMS = json.load(open(os.path.join(DATA, 'dims.json'), encoding='utf-8')) if os.path.exists(os.path.join(DATA, 'dims.json')) else {}
rows = {}    # 第 80 批：ImportYeti 美国海运提单（kind 缺省）
orows = {}   # 第 81 批：其他国家来源（_meta.kind == 'other'）
for fn in sorted(os.listdir(IMP)):
    if fn.endswith('.json'):
        d = json.load(open(os.path.join(IMP, fn), encoding='utf-8'))
        (orows if d.get('_meta', {}).get('kind') == 'other' else rows).update(d.get('rows', {}))

CN_SWITCH = {  # 提单里明写从中国厂买交换机的户 → 对手名单
    'SA-021': 'Shenzhen Centro Technology（深圳西乡）· PoE switches ≥11 票 2020-10 → 2024-09-28，之后没再来',
    'SB-108': 'HRUI 洪瑞（宝安沙井）· PoE switch 14 票 2023-03 →，最近 2026-10-14 170 ctn；三票/年、每票 100–170 箱',
    'SB-248': 'ONV 光网视（龙华大浪）· PoE switch 15 票 2016 → 2022-12，2023 创始人卖掉公司后停',
    'SB-780': 'ONV 光网视 · Ethernet/PoE switch 35 票，最近 2026-07-12（1,032 kg 58 ctn）；工业款从台湾 Etherwan',
    'SB-951': 'Dahua 大华 · 25/26 票整包（交换机随套装），海运 2024-04-16 后停',
    'SB-761': 'UNV 宇视 · 77 票整包，2026-08-26 / 09-02 提单明写 Ethernet Switch',
    'SB-541': '上海申航进出口（代理）· Ethernet switch / 光端机 7 票 2016-01 → 2018-11，之后无',
    'SB-544': 'ONV 光网视 1 票试单 2020-04-10（18 ctn）→ 没续；交换机改台湾 Emplus 贴牌（2025 起放量）',
    'SB-221': 'HRUI 洪瑞 4 票 PoE switch（主供台湾 Mstronic 385 票）',
    'SB-303': 'Shenzhen Utepo 优特普 4 票 PoE switch（2022-02 → 2023-12）→ 2025-04-26 换成 Shenzhen CSE 1 票 23 ctn；每 1～1.5 年换一次中国 PoE 交换机供应商',
    'SB-211': 'Shenzhen CSE Technology 9 票 PoE switch（2023 前）；2024-03 起中国供应全停、转越南 / 台湾（去中国化户）',
}
TW_SWITCH = {
    'SB-751': 'Senao 神準（台湾）100%，351 票，月度，最近 2026-09-25',
    'SB-544': 'Emplus（台湾，Senao 系）15 票：24 口 PoE 管理 720 ctn（2025-08-07）、48 口 PoE 管理 500 ctn（2025-08-19）、2026-06-18 540 ctn',
    'SB-1127': 'Planet 普莱德（台湾）24 票 Gigabit/Fast Ethernet switch（2024-06 后的近期清单里已看不到）',
    'SB-775': 'Patton 自家台湾产线，2017 后无',
    'SB-780': 'Etherwan（台湾）工业交换机',
    'SB-221': 'Mstronic（台湾）385 票 PoE 设备',
}


def name(code):
    r = rows.get(code) or {}
    return r.get('name') or (E.get(code) or {}).get('name') or code


def heat(code):
    return (DIMS.get(code) or {}).get('heat', {}).get('score') if isinstance((DIMS.get(code) or {}).get('heat'), dict) else (DIMS.get(code) or {}).get('heat')


L = []
L.append(f'# 进口记录（公开海关数据）· A/B 类客户逐户查询 · {TODAY}')
L.append('')
L.append('> T29-U62「能挖一下这些公司的进口情况 尤其是从中国进口的订单 日期 金额啥的吗」的交付。'
         '来源：ImportYeti 整理的 **美国海关（CBP）海运提单**（2015-01 → synced 2026-10-21），逐户按公司名查 `importyeti.com/company/<slug>`。'
         '每户结果写在该户 MD 的「进口记录（公开海关数据）」一节，原始数据在 `data/saga_clients/imports/importyeti_us_2026-10-27.json`，'
         '重跑本表：`python3 scripts/saga_clients/imports_report.py`。')
L.append('')
L.append('## 一、先说边界（能查到什么、查不到什么）')
L.append('')
L.append('| 想要的 | 能不能 | 为什么 |')
L.append('|---|---|---|')
L.append('| 美国客户从中国海运进了什么、谁发的、哪天到港、多重多少箱 | **能** | 美国海关舱单公开，ImportYeti 免费页给到港日 / 发货人 / 重量 / 件数 / 品名 / 集装箱数 |')
L.append('| **金额（货值）** | **不能** | 美国舱单不含发票金额；页面上的「Est. Shipping Spend」是 ImportYeti 估的**海运费**，不是货款。本表所有「$」都是运费估算 |')
L.append('| 空运 / 快递（DHL、FedEx）/ 陆运 | **不能** | 舱单数据只有海运；交换机这种轻货很多走空运，所以「查无」≠ 不进口 |')
L.append('| 欧洲 / 土耳其 / 英国 / 加拿大客户的进口 | **不能（按公司）** | 这些国家海关数据不按公司公开；加拿大户若经美国港口转运才看得到（Lin Haw、Infinite Cables 就是这样看到的） |')
L.append('| 印度 / 巴基斯坦客户 | **能但未做** | Zauba / Volza 有逐单含金额的数据（SB-869 早先已用 Volza 核过 128 单）；本轮先做美国，Q-63 决定要不要补 |')
L.append('| 中国出口端（我们这边）数据 | **不能** | 中国海关不公开企业级出口明细 |')
L.append('')
found = [c for c, r in rows.items() if r.get('found')]
nf = [c for c, r in rows.items() if not r.get('found')]
A_done = [c for c in rows if c.startswith('SA-')]
B_done = [c for c in rows if c.startswith('SB-')]
CA_VIA_US = ['SB-1127', 'SB-538']  # 加拿大户，经美国港口转运才看得到
L.append(f'本轮查了 **{len(rows)} 户**（A {len(A_done)} / B {len(B_done)}；美国 A 全部 15 户 + 美国 B 按热度顺序 {len(B_done) - len(CA_VIA_US)} 户 + 加拿大经美转运 {len(CA_VIA_US)} 户），'
         f'查到 **{len(found)}** 户有海运提单，**{len(nf)}** 户查无。')
L.append('')
L.append('## 二、关键发现（对 Saga 有用的 9 条）')
L.append('')
L.append(f'1. **真正「从中国海运买交换机」的只有 {len(CN_SWITCH)} 户，而且名字都对得上我们的对手**（HRUI / ONV 光网视 / Shenzhen Centro / Utepo 优特普 / Shenzhen CSE / Dahua·UNV 整包）：')
for c, t in CN_SWITCH.items():
    L.append(f'   - {c} {name(c)} ← {t}')
L.append('2. **GW Security（SB-108）就是 HRUI 的美国直客**（14 票、最近 2026-10-14 170 箱、年 3 票）：给他们推 HRUI 同款 = 自己打自己，只推 Marvell 管理型 / CENTEC 这类 HRUI 没有的；且他们走 LCL 到洛杉矶，有现成拼箱通道，样品可以搭。')
L.append('3. **Signamax（SB-780）是 ONV 的最大美国客户**（35 票 ONV 交换机、2026-07-12 还在来），迈阿密 96% LCL。ONV 的 PoE 交换机与 HRUI/SmartByte 同价位段，这是「换供应商」型机会：要价格表对位 + 替代型号（STC-2024GP / STC-424XGGPM 对位 ONV 24 口 PoE），不是「新品类」型。')
L.append('4. **Nelly\'s（SB-248）/ IPCamPower（SA-046）是一家人**：Sean Nelson 2016–2022 用 Nelly\'s 名义从 ONV 进了 15 票 PoE 交换机，2023 把 Nelly\'s 卖了专做 IPCamPower；IPCamPower 名下查无海运 → 他现在的 PoE 交换机要么空运、要么用别的主体。对 SA-046 的话术：他自己就是 ONV 的老买家，知道中国 PoE 交换机的价格与坑，直接谈规格和 MOQ，不用科普。')
L.append('5. **Optiview（SA-021）的中国 PoE 交换机供应商 Shenzhen Centro 从 2024-09-28 后没再发过**，2025 全年 Optiview 没有任何 PoE 交换机海运记录 → 要么改空运、要么换了供应商/断了。这是 A 级里最像「正在找新供应商」的信号，值得一封专门的信（不提 Centro 名字）。')
L.append('6. **Montavue（SB-951，Dahua 美国 OEM）海运 2024-04-16 后全停**；Nelly\'s 2024-10-17 后全停；KBC 美国 2021 后全停；Patton 2017 后全停——这四户「断流」要么是改空运、要么业务收缩，群发时不要按「活跃进口商」对待。')
L.append('7. **台湾 ODM 是美国品牌商交换机的主流来源，不是中国**：EnGenius（Senao 100%）、Mako（Emplus，2025 起每票 500–720 箱）、Lin Haw（Planet）、Tycon（Mstronic 385 票）、Patton（自家台湾厂）。这些户换供应商的门槛是「固件/云管理适配」而不是价格——Mako 2020 年试过 ONV 一票 18 箱就没续，就是例子。')
L.append('8. **「整柜进口商」是最容易搭货的**：52 Networks（SB-020）每年 2–3 个整柜网线从深圳光明/广州白云发，最近 2025-10-13；Lin Haw（SB-1127）月月一柜机柜从香港 Safewell 发；Altelix（SB-1001）8.4 TEU/月户外机箱+天线从宁波发；Fibertronics（SB-1030）月 1.4 票光纤配线从宁波/深圳发。这些户一句「下次整柜顺带 2 箱交换机样机，运费几乎为零」比任何价格话术都实在。')
L.append('9. **海关里有一批「已经在买中国 PoE 交换机、但不在我们库里」的美国进口商**（见第五节）：Components Specialties（Amityville NY，HRUI 9 票，2026-10-12 还在来）、Spectrumvoip（Irving TX，HRUI 9 票）、Interwebz Distributing（Broken Arrow OK，ONV 2 票）、Tristate Telecom（Suffern NY，Centro PoE switches）、Syncom Technologies、Vino Technologies、Videoworld、Great Wall Security、PoE Texas、CCTV Supply——都是 Simon 要的第二梯队「有进口经验者」，要不要建档 → Q-63。')
L.append('')
L.append('## 三、逐户总表（按 A → B、热度降序）')
L.append('')
L.append('| 编号 | 客户 | 热度 | 查到 | 海运票数 | 最近一票 | 中国占比 | 中国交换机发货人 | 一句话 |')
L.append('|---|---|---|---|---|---|---|---|---|')
def _key(c):
    h = heat(c)
    return (0 if c.startswith('SA-') else 1, -(h if isinstance(h, (int, float)) else -1), c)
for c in sorted(rows, key=_key):
    r = rows[c]
    h = heat(c)
    cn = CN_SWITCH.get(c, '—' if r.get('found') else '')
    cn = cn.split('·')[0].strip() if cn not in ('—', '') else cn
    note = (r.get('notes') or '').replace('|', '／')
    if len(note) > 110:
        note = note[:108] + '…'
    L.append(f"| {c} | {name(c).replace('|', '／')} | {h if h is not None else ''} | {'✅' if r.get('found') else '✗'} | {r.get('total_shipments', '') if r.get('found') else ''} | {r.get('last_shipment', '') if r.get('found') else ''} | {(r.get('china_share') or '').replace('|', '／')} | {cn} | {note} |")
L.append('')
L.append('## 四、查无名单（按公司名在美国海运提单里找不到）')
L.append('')
L.append('查无 ≠ 不进口：可能走空运 / 快递、用别的报关主体、或申请了舱单保密（ImportYeti FAQ）。下次有新线索（公司全名、仓库地址）再查。')
L.append('')
for c in sorted(nf, key=_key):
    r = rows[c]
    L.append(f"- {c} {name(c)}：{'；'.join(r.get('tried') or [])}{('。' + r['notes']) if r.get('notes') else ''}")
L.append('')
L.append('## 五、海关里出现、库里没有的美国进口商（新线索，未建档）')
L.append('')
L.append('来自供应商页反查（HRUI `supplier/shenzhen-hongrui-optical-technology`、ONV `supplier/optical-network-video-technologies`、Centro `supplier/shenzhen-centro-technology`，synced 2026-10-21）。这些户**已经在从中国海运 PoE 交换机**，是「有进口经验者」；建不建档、给不给 B → Q-63（默认：建档为 B，走正常建档流程，不手改 entities.json）。')
L.append('')
L.append('| 进口商 | 地点 | 从谁买 | 票数 | 品名 | 最近一票 |')
L.append('|---|---|---|---|---|---|')
for row in [
    ('Components Specialties Inc', 'Amityville, NY', 'HRUI', 9, 'PoE switch / PoE injector / SFP module', '2026-10-12（950 kg 71 ctn）'),
    ('Spectrumvoip Inc', 'Irving, TX', 'HRUI', 9, 'PoE switch', '见 HRUI 供应商页（2026 年内）'),
    ('Great Wall Security', 'US', 'HRUI', 3, 'PoE switch', '—'),
    ('PoE Texas', 'US', 'HRUI', 1, 'PoE switch', '—'),
    ('CCTV Supply Inc', 'Buffalo Grove, IL', 'HRUI', 1, 'PoE switch（2018-07-11，194 kg 8 ctn，HRUI 第一票美国客）', '2018-07-11'),
    ('Spanish Fork City', 'Spanish Fork, UT', 'HRUI', 1, 'fiber media converter（市政府，不是客户）', '—'),
    ('Interwebz Distributing', 'Broken Arrow, OK（与 Nelly\'s / IPCamPower 同镇）', 'ONV', 2, 'PoE switch / Ethernet switch', '—'),
    ('Videoworld Security Distributors', 'US', 'ONV', 1, 'Ethernet switch', '—'),
    ('Syncom Technologies', 'Washington Boro, NJ', 'ONV', 1, 'PoE switch', '—'),
    ('Vino Technologies', 'Chino, CA', 'ONV', 1, 'PoE switch / splitter / extender', '—'),
    ('Tristate Telecom', 'Suffern, NY', 'Shenzhen Centro', 1, 'PoE extender + PoE switches', '—'),
    ('Gaffney RDC Warehouse Newark', 'Gaffney, SC', 'Shenzhen Centro', 3, 'PoE injector, camera housing（仓库主体）', '—'),
    ('KOA CCTV / CCTV Outlet / Jetview Electronics (CA)', 'US / Canada', 'Shenzhen Centro', 1, 'power adapters / DVR locks', '—'),
]:
    L.append('| ' + ' | '.join(str(x) for x in row) + ' |')
L.append('')
L.append('## 六、怎么用（写进各户 MD 的「进口记录」一节之外）')
L.append('')
L.append(f'- **群发名单**：第二节第 1 条的 {len(CN_SWITCH)} 户是「已经在买中国交换机」的，把他们从通用群发里拿出来，各自一封对位信（ONV / Centro / HRUI / Utepo / CSE 对位型号 + 拼箱说明）；Watchnet（SB-303）每 1～1.5 年换一次 PoE 交换机供应商，是其中最该排进 2026 下半年日历的。')
L.append('- **话术禁区**：对 GW Security 不提 HRUI；对 Nelly\'s/IPCamPower 不提 ONV 名字；任何信里不写其他客户名（INH 规则）。')
L.append(f'- **再查节奏**：ImportYeti 每周同步一次，查过的 {len(rows)} 户不用再翻；只在 ① 某户来信 ② 季度末，重看 GW Security / Signamax / Optiview / Mako / Watchnet 五户有没有新票（看供应商有没有换）。')
L.append('- **其他国家**：见第七节（第 81 批，T29-U63）。')
L.append('')
# ---------------- 第 81 批：其他国家 ----------------
L.append('## 七、其他国家（第 81 批 · T29-U63「其他国家的不能查询吗」）')
L.append('')
L.append('> 美国之外，**只有英国有官方免费的按公司查询**（HMRC Find UK Traders）；印度 / 越南 / 土耳其 / 巴基斯坦 / 印尼靠聚合站的免费「公司页摘要」（Volza / NBD / ImportGenius / Tendata / MarketInsideData），能看到票数、供应商数、HS、年份、少量伙伴名，**明细与金额付费，我们不买**；'
         '欧盟各国、加拿大、韩国、台湾、澳洲、海湾、以色列、南非、泰国、俄罗斯（2022 年后）没有按公司公开的海关记录——这些国家的 A/B 户只能靠官网 / 邮件 / 展会判断，不再花时间找海关。'
         '原始数据：`data/saga_clients/imports/other_countries_2026-10-27.json`；每户结果已写进该户 MD 的「进口记录（第 81 批）」一节。')
L.append('')
L.append('### 7.1 各国能不能查（本轮实测）')
L.append('')
L.append('| 国家 | A/B 户数 | 来源 | 能看到什么 | 看不到什么 | 本轮查了 |')
L.append('|---|---|---|---|---|---|')
for row in [
    ('英国 GB', '3 / 57', 'HMRC Find UK Traders（官方，免费）', '公司名 + 8 位商品编码 + 非欧盟来源的**逐月**记录（2016→2026-08）', '供应商、数量、金额；欧盟来源只到年', '8 户（7 有记录 / 1 查无）'),
    ('印度 IN', '5 / 43', 'NBD Trade Data 公司页（按 IEC / PAN 拼 URL）+ Volza 搜索摘要', '记录数、供应商数、HS、4 家伙伴名、分年票数、最近 5 条品名', '金额、供应商全名（打码）', '6 户（4 有记录 / 2 查无）'),
    ('土耳其 TR', '10 / 124', 'Volza 公司页 / Tendata / MarketInsideData 免费层', '票数、来源国占比、HS 章、前 3 供应商（Volza）、12 个月进口额（MID）', '逐单明细；Volza 土耳其数据只到 2023', '2 户有记录（Angora、Netaş）；Koptek / Snexus / SGE / IoT Sistem 搜索未索引'),
    ('越南 VN', '1 / 15', 'ImportGenius 越南进口商页（免费窗口 2018-01 → 2022-02）', '票数、伙伴、最近 3 条含型号 / 数量 / HS / 口岸', '2022-02 之后', '1 户（Trường Sơn）'),
    ('巴基斯坦 PK', '1 / 19', 'Volza（SB-869 Futurist 曾索引）', '同 Volza 摘要', '—', 'MT-Link 查无'),
    ('印尼 ID', '3 / 11', 'Volza', '同 Volza 摘要', '—', 'Divatel 查无'),
    ('俄罗斯 RU', '7 / 52', '无（2022 年后只在付费俄语库）', '—', '全部', 'Faraday 代表性确认查无'),
    ('乌兹别克 UZ / 哈萨克 KZ', '1 / 3、0 / 多', '无公开来源', '—', '全部', '未查'),
    ('欧盟 DE/IT/PL/CZ…、加拿大、韩国、台湾、澳洲、阿联酋、沙特、以色列、南非、泰国、马来西亚、巴西、菲律宾', '合计 A 30+ / B 400+', '无按公司公开的海关记录（加拿大只能靠美国转运提单）', '—', '全部', '不查'),
]:
    L.append('| ' + ' | '.join(str(x) for x in row) + ' |')
L.append('')
L.append('### 7.2 关键发现（其他国家）')
L.append('')
for x in [
    '**英国 7 户里 6 户在持续非欧盟直采 8517 62 00**：Case Communications（SB-474）连续 11 年、2024–2025 年各 5–6 个月、最近 2026-08；Linxcom（SB-160）每年 4–11 个月、最近 2026-08；Technetix（SB-1121）几乎逐月（自家 HFC 产品代工）；Teltronix UK（SB-905）2026 年 1/2/4/6 月；Parallax（SA-017）每半年一次、最近 2026-01（姊妹公司 Parallax Digital Media 2025-09/11 也进）；Megnet（SA-015）2025-10 刚进过一次（主业 8471 电脑部件）。**ITM Systems（SB-767）的 8517 行全无月份 → 网络设备走欧盟渠道**；**Go Green IT（SA-007）完全查无 → 从英国分销商拿货**。',
    '→ 英国话术分两种：有直采记录的（Case / Linxcom / Teltronix / Parallax / Megnet）报 **EXW / FOB 深圳 + 拼它现有的柜**，不用推 DAP；没有直采的（Go Green IT / ITM）必须报 **DAP 英国含税到门**，把「不会进口」这个理由拿掉。',
    '**Case Communications（SB-474）是本轮最像《背景信息》第一目标（有进口经验的 OEM 品牌商）的户**：英国工业通信品牌、每年亚洲直采贴牌、节奏在加密（2016–21 年均 2–3 个月 → 2024–25 年 5–6 个月）。切入 = 它产品线缺的工业 DIN 导轨管理型 PoE（STI-42424XGGPM / STI-288DGGPM）做 OEM 30% 档；按节奏下一到货窗口 2026-10/11。',
    '**印度：Sundar（SA-032）2025 年进口 165 票 / 31 家供应商，是 2023 年（17 票）的十倍**，主业工控 / 加固电脑（C&T、IBASE、Emdoor、Twinhead），HS 里有 85176290 但供应商里没有交换机厂 → 工业导轨机配套切入，MOQ 1。**Apollo（SB-641）2026-01-24 进的是「PoE 交换机散件 PCBA + 外壳」**（HS 85177990，台湾供应商）→ 已转本地组装，整机 8/16/24 口 PoE 别报；只报它不自产的万兆 L3 / 工业 / 2.5G，或 SKD（需 SmartByte 点头）。Areca（SA-063）2023 年 121 票、2025 年只剩 TI 芯片 → 项目配套买家。Vicom（SA-073）年营收 $3.27M 却只有 1 票进口（土耳其铁路信号）→ 全部境内采购，要 DDP 才有戏。',
    '**土耳其：Angora（SA-077）45 票进口里 82% 来自中国，前三供应商 = 深圳 Ewind（交换机 ODM）+ 以色列 Larch（= 我方 B 户 SB-359）+ Neme Engae** → 它的 Verge 交换机是中国 ODM + 以色列贴牌；「做 Saga 代理」应反转为「先做它的第二家 ODM」。Netaş（SA-086）Tendata 130 票 / 39 家供应商 HS 8517.62，MID 12 个月进口 $517.61K / 28 票，大量经自家马耳他公司转口 → 项目型、合规文件优先。',
    '**越南：Trường Sơn（SA-031）4 年只有一张 60 台明纬 48V 电源的快件单、没有任何 8517 申报** → ONV 工业 PoE 不是它自己进口的（走 ONV 越南总代）；对它只能 DAP 快件小批量 + VILINK 贴牌补 ONV 没有的型号。',
    '**Larch Networks（SB-359，以色列）既是 Angora 的供应商、也是我方 B 户** → 内部对账：两边的信里都不提对方（话术禁区新增：Ewind / Larch 不对 Angora 提；Angora 不对 Larch 提）。',
]:
    L.append(f'- {x}')
L.append('')
L.append('### 7.3 逐户（其他国家）')
L.append('')
L.append('| 编号 | 国家 | 报关主体 / 公司 | 热度 | 来源 | 结果 | 最近记录 | 一句话 |')
L.append('|---|---|---|---|---|---|---|---|')
def _okey(c):
    h = heat(c)
    return (0 if c.startswith('SA-') else 1, (orows[c].get('iso') or ''), -(h if isinstance(h, (int, float)) else -1), c)
for c in sorted(orows, key=_okey):
    r = orows[c]
    h = heat(c)
    first = (r.get('lines') or [''])[0].replace('|', '／')
    if len(first) > 120:
        first = first[:118] + '…'
    nm = (r.get('name') or name(c)).replace('|', '／')
    if len(nm) > 60:
        nm = nm[:58] + '…'
    L.append(f"| {c} | {r.get('iso', '')} | {nm} | {h if h is not None else ''} | {(r.get('source') or '').split('（')[0]} | {'✅' if r.get('found') else '✗ 查无'} | {r.get('latest', '') if r.get('found') else ''} | {first} |")
L.append('')
L.append('### 7.4 怎么用')
L.append('')
L.append('- **英国 Find UK Traders 可以常态化**：每季度末把 GB 的 A/B 户名在 `uktradeinfo.com/search/traders/?q=<名>&traders=Importers` 过一遍，看 8517 62 00 有没有新月份（= 刚进过货 = 刚付过款，正是跟进时点）；结果用 `scripts/saga_clients/imports_other.py` 的 `put()` 追加。')
L.append('- **印度按 IEC 查**：拿到客户 GSTIN（IndiaMART / 发票 / 邮件签名）→ 第 3–12 位是 PAN = 新制 IEC → `https://en.nbd.ltd/trader/info/26IN<PAN>`（老公司可能是 10 位数字旧 IEC，同样拼在 26IN 后）。')
L.append('- **土耳其 / 其他聚合站**：只在客户回信、需要判断「它到底在从谁买」时查一次；搜索引擎索引不到的就放弃，不买会员。')
L.append('- **不再查**：欧盟、加拿大、韩国、台湾、澳洲、海湾、以色列、南非、泰国、俄罗斯、中亚——没有公开来源，别再花时间。')
L.append('')
L.append(f'*生成：{TODAY}　|　脚本：`scripts/saga_clients/imports_report.py`　|　数据：`data/saga_clients/imports/`*')
open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(OUT, len(rows), 'US rows;', len(found), 'found;', len(orows), 'other-country rows;', sum(1 for r in orows.values() if r.get('found')), 'found')
