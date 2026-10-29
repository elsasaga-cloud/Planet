#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 35 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 1–55 户（按综合分序，SC-043 … SC-553）—— 桶 ⑦ 首批。

桶 ⑦ 口径（在桶 ⑥ 口径之上）：
  · 免费邮箱 / 仅电话 ≠ 无路径 → 不触发 G0-1；仅网址（无邮箱无电话）且域名活 → 留 C 待巡检（找邮箱）；域名死且无邮箱无电话无退信记录 → 留 C 待巡检「下次巡检仍死即 pass」（G0-1 要求连网址 / 平台链接也没有）。
  · 阿里巴巴 RFQ / 自建站询盘的免费邮箱个人 / 无公司名 → 个人 / 非渠道买家，留 C（来询被动报价），不入池、不 pass。
  · 展会 WhatsApp 加好友（Ady / Evelyn / Yvette）= 真实可达 + 具体需求：**有公司名 + 四主区（土耳其）+ 对位 → 候选**（闸 2 查底数后 WA 一页纸）；无公司名 → 留 C 储备（WA 问到公司名 + 有回应即转候选）。
  · 升压 PoE / 注入器 / EoC / 无源 / 光开关 / 光猫 / bypass / SDI / 收发器 = Saga 不供或本职线 → 留 C（+ dayjob_fit）。

构成：阿里巴巴 RFQ / 自建站免费邮箱 30、土耳其展会 WA 13（主区）、仅网址 8、韩国 5。候选 3 = ipTIME KR（iptime.com；EFM Networks 韩国消费网络巨头品牌；「似乎有洪瑞的 switch」→ Q-33；Simon「可以尝试多跟进一下」；无邮箱 → 闸 2 查底数 + 官网找采购邮箱）/
  Interland Network & Security TR（Ady 加了 WA，要多口商业级交换机）/ MEPA Elektronik TR（Ady 加了 WA，要 4 / 8 / 16 / 24 口 PoE）。永久 pass 0。

用法：python3 sieve_batches/g1_035.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批35_2026-10-29.md）
"""
import os
import sys
import json
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import sieve  # noqa: E402
from g1_005 import compose, SUB_WHY  # noqa: E402

SUB_WHY.insert(0, (r'用户判定不行', 'Simon 曾判不行 / 不相关；无刚性 pass 证据、企业邮箱域正常 → 留 C（不主动碰，除非出现新信号）'))

BATCH = 'G1-35'
DATE = '2026-10-29'
CODES = ["SC-043", "SC-076", "SC-079", "SC-084", "SC-103", "SC-138", "SC-139", "SC-140", "SC-141", "SC-147", "SC-196", "SC-202", "SC-203", "SC-210", "SC-213", "SC-222", "SC-224", "SC-225", "SC-226", "SC-228", "SC-229", "SC-230", "SC-231", "SC-232", "SC-265", "SC-269", "SC-278", "SC-288", "SC-290", "SC-293", "SC-315", "SC-361", "SC-367", "SC-379", "SC-380", "SC-384", "SC-394", "SC-429", "SC-3316", "SC-3317", "SC-430", "SC-431", "SC-433", "SC-436", "SC-438", "SC-440", "SC-441", "SC-442", "SC-443", "SC-445", "SC-458", "SC-481", "SC-545", "SC-547", "SC-553"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
IND = '：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）'
TRWA = '：土耳其主区 ✔ 展会 WA 已加 = 真实可达 ✔ 具体需求 ✔ 但无公司名 → 留 C 储备（WA 一页纸 + 问公司名，有回应即转候选）'

OVERRIDE = {
    # ---- 候选 → 闸 2 ----
    'SC-380': ('candidate', '韩国 ipTIME（iptime.com = EFM Networks 韩国消费 / SOHO 网络第一品牌；表内「CCTV，似乎是有洪瑞的 switch」= 已贴牌中国 PoE；Simon「可以尝试多跟进一下」；无邮箱、官网正常）：巨头品牌商 = OEM 对象 ✔ 韩国点名国 ✔ 对位 ✔ → 闸 2 查底数（bizno / 公司官网）+ 官网找采购 / 合作邮箱；KC 认证由买方自理需如实说' + Q33, ['oem_target']),
    'SC-440': ('candidate', '土耳其 Interland Network & Security（Ady 展会加了 WhatsApp +90 533 833 8258；要多口商业级交换机）：土耳其主区 ✔ 公司名 ✔ WA 已加 = 可达 ✔ 对位 ✔（§5 ≥4 条）→ 闸 2 查底数（土耳其目录 / ticaret sicil 镜像）后 WA 一页纸（STC-2224GP $86 / STC-4424GCPM $165）', []),
    'SC-442': ('candidate', '土耳其 MEPA Elektronik（Furkan；Ady 展会加了 WhatsApp +90 535 875 1129；要 4 / 8 / 16 / 24 口 PoE 交换机）：土耳其主区 ✔ 公司名 ✔ WA 已加 ✔ 具体口数需求 ✔（§5 ≥4 条）→ 闸 2 查底数后 WA 一页纸（STC-028GP $28 / STC-228GP $33 / STC-2216GP / STC-2224GP $86）', []),
    # ---- 土耳其展会 WA（无公司名 / 本职线）→ 留 C 储备 ----
    'SC-265': ('keep_C', '土耳其 GÜNGÖR ELEKTRONİK（仅电话 +90 534 793 1874；「不会英文，没做过多交谈，拿了彩页」）：土耳其主区 ✔ 公司名 ✔ 但无邮箱 / 需求不明 / 语言障碍 → 留 C 储备（土耳其语 WA 一页纸一次后看，有回应即转候选）', []),
    'SC-436': ('keep_C', '土耳其 Ertan Kral（Evelyn 加了 WhatsApp +90 532 113 1189；要商业级 8 口「扁的那种」）' + TRWA, []),
    'SC-445': ('keep_C', '土耳其 Mehmet Karaal（Ady 加了 WhatsApp +90 543 908 3606；要工业级交换机 Price List）' + TRWA + '（工业线一页纸 STI-280GE $46.6 / STI-288GPM $78.9）', []),
    'SC-545': ('keep_C', '土耳其（未具名；Evelyn 加了 WhatsApp +90 543 780 2223，合影；PoE 商业级 4 / 8 / 16 口）' + TRWA, []),
    'SC-3317': ('keep_C', '土耳其（未具名；电话 07701305606 格式存疑；要商业级千兆 PoE 24 口，会英文）：具体需求 ✔ 但无公司名 / 无邮箱 / 号码格式待核 → 留 C 储备（WA 试加后看）', []),
    'SC-3316': ('keep_C', '表内土耳其（未具名；Ady 加了 WhatsApp +381 63 224 651 = 塞尔维亚号段 → 国别待核；CCTV，主要要商业级 PoE）：WA 已加 ✔ 需求 ✔ 但无公司名 + 国别存疑 → 留 C 储备（WA 问公司名后看）', []),
    'SC-431': ('keep_C', '土耳其 Ali Goktork（Ady 加了 WhatsApp +90 543 760 6156；要工业光猫）：工业光猫 = 本职线 → 留 C + dayjob_fit（WA 路径在）', ['dayjob_fit']),
    'SC-438': ('keep_C', '土耳其 IHM Technology（Mehmef；Ady 加了 WhatsApp +90 532 668 9892；问独立式 bypass + 2 光 8 带 bypass、SC 口、不带管理）：bypass = 本职线（Saga 无）→ 留 C + dayjob_fit；公司名 + WA 在 → 若改问交换机即转候选', ['dayjob_fit']),
    'SC-278': ('keep_C', '土耳其 b2bherz.com（ozantutku@hotmail.com；域名正常但联系用免费邮箱；1 推 0 回；无需求记录）：土耳其主区 ✔ 但主体 / 需求不明 → 留 C 储备', []),
    'SC-290': ('keep_C', '土耳其 fatihkirim3@gmail.com（自建站询盘「5 电口」；无公司名）' + IND, []),
    # ---- 韩国 ----
    'SC-429': ('keep_C', '韩国（未具名；Yvette 加了微信，说中文，去过深圳；问 KC / 安规认证；要工业级 8 光口 PoE 网管 + 16 / 24 口；问定制丝印、包装盒刷 logo = OEM 意向 ✔；手机 010-7935-4177）：韩国点名国 ✔ OEM 意向 ✔ 可达（微信）✔ 但无公司名 + KC 认证 Saga 无 → 留 C + oem_target（微信问到公司名即转候选；KC 由买方自理需如实说）', ['oem_target']),
    'SC-379': ('keep_C', '韩国 industrial.kr（switch，主要是 Lantech 的 = 台湾品牌 ✔；无邮箱、官网正常）：韩国点名国 ✔ 台湾工业品牌代理 ✔ 但无联系路径 → 留 C 待巡检（官网找邮箱后即转候选）', []),
    'SC-232': ('keep_C', '韩国 YJsoft（yjsoft.kr；阿里巴巴询盘「Bypass」；KP YJ Jeon；无邮箱）：bypass 本职线 + 软件公司 → 留 C + dayjob_fit', ['dayjob_fit']),
    # ---- 仅网址 / 无联系路径 → 留 C 待巡检 ----
    'SC-210': ('keep_C', '美国 IEC（iec.net；「EoC / MC / switch 等」；无邮箱、无电话；官网 http_error 但域名 MX 正常）：美国主区 ✔ 但无联系路径 → 留 C 待巡检（官网找邮箱；EoC 非 Saga 线）', []),
    'SC-213': ('keep_C', '新西兰 AllTheGeek（allthegeek.com；SFP / MC / VC / 工业 FS「标价较高」，AOA 的；无邮箱）：网络配件网店 + 无路径 → 留 C 待巡检', ['dayjob_fit']),
    'SC-222': ('keep_C', '香港 Shogun Technology（shoguncctv.com no_mx；ONV 工业 FS / MC 换 PVC 膜贴 SG- 型号 = 自有标签贸易商 ✔；无邮箱、无电话）：贴牌 = OEM 对象 ✔ 但无联系路径 + 域无 MX → 留 C + oem_target 待巡检（找到邮箱即转候选）', ['oem_target']),
    'SC-361': ('keep_C', '俄罗斯 xn--80aftrjl.xn--p1ai（中科德能 / ONV 的工业 FS；无邮箱、无电话；域名 dead，无退信记录）：有网址但死 → 不满足 G0-1 字面（需连网址也无）→ 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-481': ('keep_C', 'faxontechnologies.com（国别未填；商业 PoE 有 ONV 的；「销售平台」；无邮箱）：平台型 + 无路径 → 留 C 待巡检', []),
    # ---- 欧美主区零散询盘（免费邮箱）→ 留 C ----
    'SC-043': ('keep_C', '德国 Carb UG (haftungsbeschränkt)（Regensburg；2013 年阿里巴巴 RFQ「48V 0.5A 1G PoE injector」；KP Karim Belkacem CEO；miloud30@gmail.com；carb-tech.de dead）：注入器 Saga 不供 + 陈旧 + 域死（gmail 路径在，不刚性）→ 留 C', []),
    'SC-076': ('keep_C', '德国 WBS-Bauservice（建筑服务；2022 年 RFQ「3 台 1 光 8，10G 光 2.5G PoE」；Sven Harder；gmx 免费邮箱）：个人 / 终端小单 + 2.5G 待口径（SB-263）→ 留 C（来询被动报价）', []),
    'SC-079': ('keep_C', '意大利 InvisionTech Group（托管 / 网络安全；2013 年 RFQ「Smart City Box」；Edoardo Zambon CEO；gmail）：品类不符 + 陈旧 → 留 C', []),
    'SC-084': ('keep_C', '加拿大 LEGF / remoteham.com（业余无线电爱好者；RFQ「1X2 光开关」；Guy Fleurant；gmail）：个人爱好者 + 光开关本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-103': ('keep_C', '斯洛文尼亚 Kimax（2014 年 RFQ「8 口商业 PoE」；Miroslav Kral；gmail）' + IND, []),
    'SC-138': ('keep_C', '美国 CLEC Networks Inc（RFQ「2.5G / 10G 商业级」；Paul Butler；yahoo；电话在）：2.5G 待口径（SB-263）+ 免费邮箱 → 留 C（来询被动报价）', []),
    'SC-139': ('keep_C', '瑞典 Electric Avenue（RFQ「工业电源」；outlook）：品类不符 → 留 C', []),
    'SC-140': ('keep_C', '德国 Super Shops（RFQ「16 槽管理机架」；两个 hotmail）：机架 Saga 不供 + 疑可疑 RFQ → 留 C', []),
    'SC-141': ('keep_C', '意大利 Traderoid（RFQ「Kyland Switch」品牌指定；gmail）：贸易中介 + 品牌指定 → 留 C', []),
    'SC-147': ('keep_C', '英国 jemtec ltd（询盘「升压 5 电口」；onetalentfoundation@gmail.com）：升压 PoE Saga 不供 + 免费邮箱 → 留 C', []),
    'SC-202': ('keep_C', '美国 Official All Star Café（RFQ「16 电口」；hotmail；WA 加不上）：非渠道 / 疑可疑 RFQ → 留 C', []),
    'SC-228': ('keep_C', '英国 Delatim（阿里巴巴 RTS 订单「EoC」；Andrew Armstrong；hotmail）：个人买家（付过钱）+ EoC 非 Saga 线 → 不 pass → 留 C（来询被动报价）', []),
    'SC-230': ('keep_C', '希腊 Ntwnhs Group Ltd（RFQ「Networking devices」；gmail）' + IND, []),
    'SC-231': ('keep_C', '英国 Vimo Group ltd.（询盘「升压 5 口」；gmail / outlook；座机在）：升压 PoE Saga 不供 → 留 C', []),
    'SC-269': ('keep_C', '匈牙利 Omni Realty（RFQ「千兆收发器」；outlook；WA 加不上）：收发器本职线 + 疑可疑 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-288': ('keep_C', '法国 exodimsociete@gmail.com（2023 年 RFQ「PoE Switch 和相关配件」；Moussa Djighaly；无公司名）：法国主区 ✔ 对位 ✔ 但免费邮箱 / 无公司名 → 留 C（一页纸一次后看，问到公司名即转候选）', []),
    'SC-293': ('keep_C', '加拿大 grid.surveillance@gmail.com（2025 年 RFQ「PoE++ Switch / injector 带认证」；Ryan Kennedy）：北美主区 ✔ 新鲜需求 ✔ 但 PoE++ 90W / 注入器 Saga 无 + 免费邮箱 → 留 C（一页纸如实说 PoE+ 线后看）', []),
    'SC-315': ('keep_C', '美国 andrespuricelli@gmail.com（2022 年询盘「2 光 10 电」；1 推 0 回）' + IND, []),
    'SC-394': ('keep_C', '英国 Sumtec Exports Limited（J.L. Frydman Director；btinternet.com；展会介绍 WDM「似乎懂一些」、主动提 bypass、拿了 catalog；座机 + 手机；17 推 0 回）：英国主区 ✔ 但需求为 WDM / bypass 本职线 + 零回应 → 留 C + dayjob_fit', ['dayjob_fit']),
    # ---- 其他区零散询盘 ----
    'SC-196': ('keep_C', '香港 Artifex Engineering & Technology Ltd.（RFQ「8+2 百兆商业 PoE」；Jackson Choy；gmail）：百兆 Saga 不供 + 免费邮箱 → 留 C', []),
    'SC-203': ('keep_C', '香港 虹科電子 Aiportek（aiportek.com；工业标准品一站式方案供应商；gmail 联系；5 推 0 回）：同行 / 技术分销 → 留 C', []),
    'SC-224': ('keep_C', '伊拉克 AHF（自建站询盘「1 光 6 工业交换机」；Muhammad Sultan；gmail；叙利亚号码）' + IND, []),
    'SC-225': ('keep_C', '亚美尼亚 Amazon IMPORT（RFQ「24 口商业 switch」；Georgi Vardanov；gmail）' + IND, []),
    'SC-226': ('keep_C', '保加利亚 BGTRONICA LTD（索非亚；2010 年 RFQ「无人机」；Teodor Kazandjiev；gmail；bgtronica.com nxdomain；WA 加不上）：品类不符 + 陈旧 + 域死（gmail 路径在，不刚性）→ 留 C', []),
    'SC-229': ('keep_C', '基里巴斯 KariTeo Enterprises（询盘「升压 5 电口」；gmail）：升压 PoE Saga 不供 + 区域外 → 留 C', []),
    'SC-367': ('keep_C', 'Island Engineering Palau（表内澳门，实为帕劳 → 国别待核；自建站询盘「Moxa network switches」；John Swords；gmail；WA 加不上）：工程商 + 品牌指定 Moxa + 区域外 → 留 C', []),
    'SC-384': ('keep_C', '智利 Chile Nuts Spa（RFQ「PoE injector 及摄像头」；gmail）：注入器 Saga 不供 + 非渠道 → 留 C', []),
    'SC-430': ('keep_C', '泰国 A Team Studio parts Ltd（RFQ「SDI」；hotmail）：SDI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-433': ('keep_C', '以色列 Darium Technologies（RFQ「无人机光纤」；gmail）：品类不符 → 留 C', []),
    'SC-441': ('keep_C', '阿联酋 Kampala bazaar（询盘「2 光 4 升压」；Muhidini Ali；仅电话）：升压 PoE Saga 不供 → 留 C', []),
    'SC-443': ('keep_C', '泰国 MULTIPROOF CO., LTD.（询盘「OM523S-1BL22-TCP」型号指定；Peerapol；仅电话）：型号指定（非 Saga 型号）→ 留 C（来询被动报价）', []),
    'SC-458': ('keep_C', '叙利亚 alsalam（自建站询盘「Huawei PON」；Tareq Bitar；gmail）：叙利亚守界 + PON 品类不符 → 留 C', []),
    'SC-547': ('keep_C', '印度尼西亚 Airnav（自建站询盘「工业光猫」印尼语；Untung Legowo；gmail；WA 加不上）：AirNav = 国营空管（政府 / 巨头终端）+ 光猫本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-553': ('keep_C', '巴基斯坦 MND Industrial Link（RFQ「5 电口」；Muhammad Bilal CEO；gmail）' + IND, []),
}


def main():
    assert len(CODES) == 55 and len(set(CODES)) == 55
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    rd = os.path.join(sieve.ROOT, 'data', 'saga_clients', 'research')
    V = {}
    for code in CODES:
        e = ents[code]
        assert e.get('grade') == 'C', code
        cur = sv.get(code) or {}
        assert not cur or cur.get('batch') == BATCH, ('already judged elsewhere', code, cur)
        if code in OVERRIDE:
            V[code] = OVERRIDE[code]
        else:
            p = os.path.join(rd, code + '.json')
            research = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None
            reason, tags = compose(e, research)
            V[code] = ('keep_C', reason, tags)
    for code in OVERRIDE:
        assert code in V, ('override not in batch', code)
    for code, (verdict, reason, tags) in V.items():
        assert verdict in ('pass_final', 'keep_C', 'candidate') and len(reason) >= 12, code
        cur = sv.get(code) or {}
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True, 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    tg = Counter(t for v in V.values() for t in v[2])
    L = [f'# C 池 · 闸 1 · 第 35 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 1–55 户（{len(V)} 户）—— 桶 ⑦ 首批', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 桶 ⑦ 口径：免费邮箱 / 仅电话 ≠ 无路径（不触发 G0-1）；仅网址且域名活 → 留 C 待巡检找邮箱；域名死且无邮箱 / 电话 / 退信记录 → 留 C 待巡检「下次仍死即 pass」。阿里巴巴 RFQ / 自建站免费邮箱个人 → 个人 / 非渠道买家留 C（来询被动报价）。'
         ' **展会 WhatsApp 加好友 = 真实可达 + 具体需求：有公司名 + 土耳其主区 + 对位 → 候选**；无公司名 → 留 C 储备（WA 问到公司名 + 有回应即转候选）。升压 / 注入器 / EoC / 无源 / 光开关 / 光猫 / bypass / SDI / 收发器 → 留 C（+ dayjob_fit）。', '',
         '> 构成：阿里巴巴 RFQ / 自建站免费邮箱 30、土耳其展会 WA 13（主区）、仅网址 8、韩国 5。候选 3 = ipTIME KR（EFM Networks 巨头品牌，疑有洪瑞 switch → Q-33；Simon「可以尝试多跟进一下」；无邮箱 → 闸 2 + 官网找采购）/ Interland Network & Security TR / MEPA Elektronik TR（均 Ady 展会加 WA + 具体口数需求）。'
         ' 值得留意的留 C：SC-429 韩国微信客户（问 KC + 定制丝印 / 刷 logo = OEM 意向，无公司名）、SC-222 Shogun HK（ONV 换膜贴 SG- 型号 = 自有标签，无邮箱）、SC-379 industrial.kr（Lantech 代理，无邮箱）、SC-445 Mehmet Karaal TR（要工业 price list）。国别待核：SC-3316（+381 塞尔维亚号段）、SC-367（澳门 → 帕劳）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批35_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
