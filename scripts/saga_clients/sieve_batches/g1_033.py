#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 33 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 1156–1210 户（按综合分序，SC-3003 … SC-3128）。

构成：「用户判定不行 / 不相关」54 / 55 + 巨头 1（Panasonic 中东），退信 42（域名绝大多数仍正常 → 待巡检）、韩国 13、巴西 7（WA 加不上 5）、马来西亚 3、菲律宾 3、俄罗斯 5、印度 4。
  · 口径同桶 ⑥ 首批；本批起**收紧 G0-2 口径**：`no_mx`（有 A 记录、无 MX）≠ 方案 §G0-2 的 {nxdomain, dead} —— 网站可能仍活、可从官网找新地址 → 不属刚性，退信 + no_mx 一律留 C 待巡检；
    据此**回改第 28–32 批 6 户**（SC-1823 Zaviyehdid IR / SC-2125 OK Computers PK / SC-2370 CCTVapp VN / SC-2493 KVMswitches IN / SC-2659 Optimaunit RU / SC-3001 GMD Telecom KR）永久 pass → 留 C 待巡检（原批次保留在 fixed_from）。
  · 永久 pass 1 = repairitnetworks.com（国别未填；拿了 catalog 无沟通；退信 + 唯一域 nxdomain + 无电话 / WA → 闸 0 刚性 G0-2）。
  · 候选 0：本段为桶 ⑥ 尾部低分退信户，无一满足「中国 / 台湾品牌 + 点名国 / 先例国 + 可达」；印度 Evteq（新桥商业 PoE）/ 泰国 Technology Solution（新桥）/ 俄罗斯 Netelit（工业 FS）/ 澳大利亚 Madison（大分销）/ 韩国 Imadang（Red Lion）等均退信 → 留 C 待巡检，通了即转候选。
  · 其余留 C：本职线 dayjob_fit（KS IT Solutions WDM、Zaram 光模块、DELTA 视频光传、Mekshaf 光端机、Uside bypass、Net-Optic 光猫 / VC / MC、Alma Asia VC / SFP）；巨头终端 Holcim / Ambuja、Panasonic（GDPR 邮箱不作收件人）；守界 Infotech 叙利亚、alles.dp.ua（表内俄罗斯，.dp.ua = 乌克兰第聂伯罗 → 国别待核）；
    国别错位 FG Spectral（.com.tr + A.Ş. = 土耳其主区，WA 未试）、Best / GSD Bilişim（土耳其语网店 → 国别待核）；机构 pit.or.kr。
  · 「用户判定不行」/「stop」flag 均非客户明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_033.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批33_2026-10-29.md）
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

BATCH = 'G1-33'
DATE = '2026-10-29'
CODES = ["SC-3003", "SC-3004", "SC-3006", "SC-3007", "SC-3009", "SC-3012", "SC-3014", "SC-3015", "SC-3016", "SC-3017", "SC-3018", "SC-3019", "SC-3027", "SC-3028", "SC-3031", "SC-3033", "SC-3038", "SC-3039", "SC-3040", "SC-3041", "SC-3043", "SC-3050", "SC-3053", "SC-3060", "SC-3064", "SC-3065", "SC-3068", "SC-3076", "SC-3077", "SC-3080", "SC-3081", "SC-3082", "SC-3085", "SC-3088", "SC-3093", "SC-3094", "SC-3095", "SC-3097", "SC-3101", "SC-3102", "SC-3104", "SC-3106", "SC-3107", "SC-3112", "SC-3115", "SC-3116", "SC-3117", "SC-3118", "SC-3120", "SC-3059", "SC-3123", "SC-3125", "SC-3126", "SC-3127", "SC-3128"]

VETO = '；Simon 曾判不行 → 可按编号否决'
NOMX = '（no_mx = 有 A 记录无 MX，不属 G0-2 刚性集合 {nxdomain, dead}）'

# 回改：第 28–32 批 6 户曾以 no_mx 当「域名死」判永久 pass → 不刚性 → 回 C 待巡检
FIX = {
    'SC-1823': '回改（原 G1-28 永久 pass）：伊朗 Zaviyehdid（zaviyehdid.com / i30cctv.com 双域 no_mx，A 记录在；退信；卖很多洪瑞的产品）' + NOMX + ' → 留 C 待巡检（官网找新地址；伊朗同时守界；下次巡检网站也死即 pass）',
    'SC-2125': '回改（原 G1-30 永久 pass）：巴基斯坦 OK Computers（okcomputers.com.pk 唯一域 no_mx，A 记录在；退信；有 Utepo 的）' + NOMX + ' → 留 C 待巡检（官网找新地址；下次巡检网站也死即 pass）',
    'SC-2370': '回改（原 G1-31 永久 pass）：越南 CCTVapp（cctvapp.net no_mx，A 记录在；wificamera.vn nxdomain；退信）' + NOMX + ' → 留 C 待巡检（下次巡检网站也死即 pass）',
    'SC-2493': '回改（原 G1-31 永久 pass）：印度 KVMswitches（kvmswitches.co.in 唯一域 no_mx，A 记录在；退信；Bypass）' + NOMX + ' → 留 C 待巡检 + dayjob_fit（下次巡检网站也死即 pass）',
    'SC-2659': '回改（原 G1-31 永久 pass）：俄罗斯 Optimaunit（optimaunit.ru 唯一域 no_mx，A 记录在；退信；CCTV 类）' + NOMX + ' → 留 C 待巡检（下次巡检网站也死即 pass）',
    'SC-3001': '回改（原 G1-32 永久 pass）：韩国 GMD Telecom（gmdtelecom.co.kr 唯一域 no_mx，A 记录在；退信；无人名 / 电话）' + NOMX + ' → 留 C 待巡检（下次巡检网站也死即 pass）',
}
FIX_TAGS = {'SC-2493': ['dayjob_fit']}

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-3031': ('pass_final', 'repairitnetworks.com（国别未填；「客户拿了 catalog，没做较多沟通」；退信「发不过去」；唯一域 nxdomain；无电话 / WA / 人名）：退信 + 全部域名 nxdomain + 无备用路径 → 闸 0 刚性 G0-2 → 永久 pass', []),
    # ---- 退信 + no_mx → 留 C 待巡检（不刚性）----
    'SC-3003': ('keep_C', '韩国 Hytec Korea（hyteckorea.co.kr no_mx，A 记录在；退信；PoE 配件 + Etherwan 产品）：退信 + no_mx 不属刚性' + NOMX + ' → 留 C 待巡检（韩国点名国 + Etherwan 工业线代理 → 官网找新地址，通了可转候选）', []),
    'SC-3016': ('keep_C', '泰国 Technology Solution（technologysolution.co.th no_mx，A 记录在；退信；商业 PoE + 几个工业 FS，用新桥的 = 中国品牌同类 ✔）：退信 + no_mx 不属刚性 → 留 C 待巡检（通了可转候选；泰国无先例）', []),
    'SC-3068': ('keep_C', '哈萨克斯坦 Voltroom（voltroom.kz no_mx，A 记录在；退信；主要商业 FS 没啥工业品）：退信 + no_mx 不属刚性 → 留 C 待巡检', []),
    'SC-3082': ('keep_C', '乌干达 SGT Technical（sgt-technical.com / sgttechnical.com 双域 no_mx；无退信记录；MC + CCTV 安防；wronald@ 具名）：无 MX 但无退信 → 留 C 复核 MX（不作 pass）', []),
    # ---- 退信但域名正常 → 留 C 待巡检 ----
    'SC-3004': ('keep_C', '韩国 Imadang（imadang.co.kr 域正常；退信；Red Lion 工业 FS 代理；仅 webmaster@ 非买家地址）：退信待巡检 + 韩国点名国 + 工业品牌代理 ✔ → 留 C（找 sales 地址后可转候选）', []),
    'SC-3006': ('keep_C', '韩国 KG Auto（kgauto.co.kr 域正常；退信；「少量电口，别人在卖他们的」= 疑自有产品厂商）：疑同行 / 厂商 + 退信 → 留 C 待巡检', []),
    'SC-3007': ('keep_C', '马来西亚 KS IT Solutions（ks-itsolutions.com 域正常；退信；懂 WDM、问 CWDM 是否无源；地址 i-City Selangor；igbal@ 具名；手机在表；1 推）：本职线 WDM → 留 C + dayjob_fit；退信待巡检（手机路径在）', ['dayjob_fit']),
    'SC-3009': ('keep_C', '澳大利亚 Madison Technologies（madison.tech no_mx / madisontech.com.au 正常；退信 leona.skene@；工业 FS，卖比较多牌子）：大分销 + 退信 → 留 C 待巡检（澳大利亚先例在；找新地址后复看）', []),
    'SC-3012': ('keep_C', '台湾 N-Port（nport.com.tw 域正常；退信 ally.cheng@；switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3014': ('keep_C', '韩国 SS CCTV（sscctv.com 域正常；退信「发不过去」；PoE switch 类目下找到）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3015': ('keep_C', '马来西亚 Suntrec（suntrec.net 域正常；退信；MC / SFP / switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3017': ('keep_C', '新加坡 Telescience（telescience.asia 域正常；退信；商业 PoE 看着像国内外壳 + SFP）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3018': ('keep_C', '阿联酋 Vsign Computers（vsigncomputers.com / vsign.com 均正常；退信 info@vsign.com；商业 PoE）：退信待巡检（换 vsigncomputers.com 地址）→ 留 C', []),
    'SC-3019': ('keep_C', '韩国 Zaram Technology（zaram.com 域正常；退信；主要光模块 + 少量 PoE 配件）：光模块厂商 = 本职线 / 同行 → 留 C + dayjob_fit；退信待巡检', ['dayjob_fit']),
    'SC-3033': ('keep_C', '韩国 Songam（songam.co.kr 域正常；退信；Ethernet switch 周边；9 推 0 回）：退信 + 零回应 → 留 C 待巡检', []),
    'SC-3050': ('keep_C', '菲律宾 Ansys PH（ansysph.com 域正常；退信 support@；Cisco 产品 + 从国内买一些 switch）：进口中国同类 ✔ 但退信 + 菲律宾无先例 → 留 C 待巡检（通了复看）', []),
    'SC-3053': ('keep_C', 'alles.dp.ua（表内「俄罗斯」，.dp.ua = 乌克兰第聂伯罗 → 国别待核；退信 alex@；商业 PoE）：乌克兰 = 守界（非永久 pass）+ 退信 → 留 C', []),
    'SC-3060': ('keep_C', '俄罗斯 Netelit（netelit.ru 域正常；退信 info@；工业 FS）：俄罗斯点名国 ✔ 工业对位 ✔ 但退信 + 无品牌证据 → 留 C 待巡检（通了可转候选；收款待定）', []),
    'SC-3064': ('keep_C', '俄罗斯 Promarchive / Indexprom（promarchive.ru / indexprom.ru 均正常；退信 info@indexprom.ru；工业交换机「主要是牌子的」= 品牌货目录站）：疑行业目录 / 平台型 + 退信 → 留 C 待巡检', []),
    'SC-3065': ('keep_C', '越南 Thuan Phat Tech（thuanphattech.com 域正常；退信 thongin@；switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3081': ('keep_C', '韩国 Maver（maver.com 域正常；退信 gms97c52@；PoE switch；23 推 0 回）：退信 + 零回应 → 留 C 待巡检', []),
    'SC-3085': ('keep_C', '科威特 Al-Wassen Est（alwassen.com 域正常；退信 george@；SM to MM MC）：MC 需求（Saga 仅 STC-110XGE 千兆）+ 退信 → 留 C 待巡检', []),
    'SC-3088': ('keep_C', 'FG Spectral Teknoloji A.Ş.（fgmarket.com.tr nxdomain；表内国别未填，.com.tr + A.Ş. = 土耳其主区 → 国别待核；商业 PoE 销售平台；微信 TR20064224 + 手机 90 536 966 9277「还没加」；退信）：域死但手机 / 微信路径未试 → 不刚性 → 留 C（土耳其主区：试加 WA 后复看；平台型）', []),
    'SC-3093': ('keep_C', '马来西亚 Alma Asia / Alma CCTV（almacctv.com / alma-asia.com 均正常；退信 1 地址，另有 sales.kl@ / sales.jb@ / sales.mlk@ 分支地址；VC / SFP / MC / switch 很多国内牌子）：多分支分销 + 进口中国同类 ✔ 但马来西亚无先例 + 品牌未点名 → 留 C（储备；巡检时换分支地址推一次，有回应再转候选）+ dayjob_fit（VC / SFP / MC）', ['dayjob_fit']),
    'SC-3094': ('keep_C', 'Best Bilişim / GSD Bilişim（bestabilisim.com 正常 / gsdbilisim.com no_mx；表内国别未填，土耳其语网店「6lı PoE switch fiyat」= 土耳其主区 → 国别待核；退信 info@；switch 很多国内同行的外壳 = 进口中国同类 ✔）：网店型 + 退信 → 留 C 待巡检（核实土耳其后换地址复看）', []),
    'SC-3095': ('keep_C', '卡塔尔 Blueland Qatar（bluelandqatar.com 域正常；退信 binoy.chacko@；MC trading）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3097': ('keep_C', 'Skynettel（skynettel.com 域正常；国别未填；退信 info@；商业 PoE）：退信 + 国别未知 → 留 C 待巡检', []),
    'SC-3101': ('keep_C', '巴西 2Flex（2flex.com.br 域正常；退信 contato@；商业 switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3104': ('keep_C', '阿根廷 Jaros（jaros.com.ar 域正常；退信 info@；有 DCN 的）：进口中国同类 ✔ 但退信 + 阿根廷无先例 → 留 C 待巡检', []),
    'SC-3107': ('keep_C', '洪都拉斯 Skytek Security（skyteksecurity.hn 域正常；退信 sales@；商业 PoE 好几家国内牌子；WA 3184-8605 在表未加）：进口中国同类 ✔ 但洪都拉斯无先例 → 留 C（试加 WA 后复看）', []),
    'SC-3115': ('keep_C', '韩国 Essentec（essentec.co.kr 域正常；退信 help@；在用 Allied Telesis 大口）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3116': ('keep_C', '韩国 IoT Solution（iot-solution.co.kr 域正常；退信 korea@；IoT）：退信 + 对位弱 → 留 C 待巡检', []),
    'SC-3117': ('keep_C', '韩国 pit.or.kr（.or.kr 机构域；退信 hyuk@；「看着比较专业」）：机构 / 研究单位（非渠道）→ 留 C', []),
    'SC-3118': ('keep_C', '以色列 Telran（telran.co.il 域正常；退信 office@；「Visionnet 似乎是他们自己品牌」）：自有品牌线索待证（→ oem_target 备查）+ 退信 → 留 C 待巡检（通了 + 证实自有品牌可转候选）', ['oem_target']),
    'SC-3120': ('keep_C', '韩国 Uside（uside.co.kr 域正常；退信；bypass）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3059': ('keep_C', '俄罗斯 Net-Optic（net-optic.ru 正常 / net-optics.ru nxdomain；退信；「产品线很相似，工业 FS 还没上线」光猫 / VC / MC / 配件）：产品线相似 = 同类分销 / 疑同行 + 本职线 → 留 C + dayjob_fit；退信待巡检（俄罗斯点名国，通了复看）', ['dayjob_fit']),
    'SC-3125': ('keep_C', '埃及 Computech（computecheg.com 域正常；退信 info@；商业 PoE 都是有名牌子）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-3126': ('keep_C', '印度 Evteq Global（evteqglobal.com 域正常；退信 info@；新桥商业 PoE = 中国品牌同类 ✔）：印度点名国 ✔ 对位 ✔ 但退信 + 无电话 → 留 C 待巡检（找新地址后即转候选）', []),
    'SC-3127': ('keep_C', '尼泊尔 Group Singh（groupsingh.com 域正常；退信 info@；商业 PoE 国内外壳）：退信 + 非点名国 → 留 C 待巡检', []),
    'SC-3128': ('keep_C', '孟加拉 Logicgo（logicgo.com.bd 域正常；退信 info@；商业 PoE + CCTV 配件）：退信 + 非点名国 → 留 C 待巡检', []),
    # ---- 域死 / WA 加不上但无退信记录 → 留 C 待巡检（不刚性）----
    'SC-3038': ('keep_C', '巴西 Clickduplo（clickduplo.com.br nxdomain；WA 加不上 ×2；无退信记录；备注 fail）：域死 + WA 失败但无退信 → 不满足 G0-2 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3041': ('keep_C', '巴西 Guvision（guvision.com.br nxdomain；WA 加不上 ×2；无退信记录）：域死 + WA 失败但无退信 → 不满足 G0-2 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3077': ('keep_C', '利比亚 Itqaan Co（itqaan-ly.com nxdomain；WA 加不上；无退信记录；无产品信息）：域死但无退信 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3112': ('keep_C', '沙特 Mekshaf Est for Trading（securityprosys.com nxdomain；光端机 fail；电话 966-1-2173255 在表；无退信记录）：本职线 光端机 + 域死无退信 → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    # ---- WA 加不上、域名正常 → 留 C ----
    'SC-3039': ('keep_C', '巴西 Dips（dips.com.br 域正常；WA 加不上；无兴趣记录）：冷户 + WA 失败 → 留 C 储备', []),
    'SC-3040': ('keep_C', '巴西 Discabos（discabos.com.br 域正常；WA 加不上；Cables）：线缆商 + 对位弱 → 留 C', []),
    'SC-3043': ('keep_C', '巴西 Masterseg（interjato.com.br 域正常；WA 加不上；备注 fail）：冷户 + WA 失败 → 留 C 储备', []),
    'SC-3076': ('keep_C', '印度 A.P.K. Trading & Investing Pvt Ltd（apktrade@mtnl.net.in = ISP 托管信箱；「will need in a couple of months, take for future reference」；WA 加不上）：弱意向 + 印度点名国 → 留 C（储备；一页纸一次后看）', []),
    'SC-3028': ('keep_C', '叙利亚 Infotech（infotech-sy.net 域正常；amer@ 具名；IT solutions；WA 加不上）：叙利亚 = 制裁 / 守界（不做不 pass）→ 留 C', []),
    # ---- 巨头 / 本职 / 其他 ----
    'SC-3027': ('keep_C', '俄罗斯 DELTA（deltapsu.com = Delta 电源官网域；「they do LED walls, sometimes need video over fiber for long distance」）：视频光传 = 本职线 + 巨头域 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3080': ('keep_C', '印度 Holcim / Ambuja Cement（sanjeev.saxena@ambujacement.com；「TA210-FE/S25 $18, TA510 $50 think good price」；WA 加不上）：巨头终端用户（水泥集团）曾问价 → 不 pass → 留 C（来询被动报价）', []),
    'SC-3123': ('keep_C', 'Panasonic Marketing Middle East（privacy-lsnetworks@ml.jp.panasonic.com = GDPR / 隐私信箱，不作收件人；商业 PoE / catalogue；2 推）：巨头品牌商 → 按 U117 不 pass → 留 C', []),
    'SC-3102': ('keep_C', '菲律宾 CCTV Pinoy（cctvpinoy.com 域正常；admin@；Wi-Tek + 大华，CCTV 为主）：CCTV 店 + 菲律宾无先例 → 留 C 储备', []),
    'SC-3106': ('keep_C', '菲律宾 Marstech（marstech.com.ph 域正常；线缆 / 工具类较多，Lightem 供货）：对位弱 → 留 C', []),
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
    # 回改 6 户（幂等）
    fixed = []
    for code, reason in FIX.items():
        cur = sv.get(code) or {}
        assert cur, ('fix target missing', code)
        assert cur.get('verdict') in ('pass_final', 'keep_C') and cur.get('gate') == 1, (code, cur)
        origin = cur.get('fixed_from') or cur.get('batch')
        row = {'verdict': 'keep_C', 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True,
               'batch': BATCH, 'fixed_from': origin}
        tags = sorted(set(cur.get('tags') or []) | set(FIX_TAGS.get(code, [])))
        if tags:
            row['tags'] = tags
        sv[code] = row
        fixed.append((code, origin))
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    tg = Counter(t for v in V.values() for t in v[2])
    L = [f'# C 池 · 闸 1 · 第 33 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 1156–1210 户（{len(V)} 户）+ 回改 6 户', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> **口径收紧（本批起）**：`no_mx`（域名有 A 记录、无 MX）不属方案 §G0-2 的「域名死」集合 {nxdomain, dead} —— 网站可能仍活、可从官网找新地址，不是「无备用路径」→ 退信 + no_mx 一律留 C 待巡检（下次巡检网站也死即 pass）。'
         ' 据此回改第 28–32 批 6 户永久 pass → 留 C：' + '、'.join(f'`{k}`（原 {o}）' for k, o in fixed) + '。', '',
         '> 构成：「用户判定不行」54 / 55 + 巨头 1（Panasonic 中东），退信 42（域名绝大多数仍正常 → 待巡检）、韩国 13、巴西 7（WA 加不上 5）、俄罗斯 5、印度 4、马来西亚 3、菲律宾 3。候选 0 —— 本段为桶 ⑥ 尾部低分退信户，无一同时满足「中国 / 台湾品牌 + 点名国 / 先例国 + 可达」；'
         '最接近的 Evteq（IN，新桥 PoE）/ Technology Solution（TH，新桥）/ Netelit（RU，工业 FS）/ Madison（AU，大分销）/ Imadang（KR，Red Lion）/ Hytec（KR，Etherwan）均退信 → 待巡检，通了即转候选。'
         ' 永久 pass 1 = repairitnetworks.com（退信 + 唯一域 nxdomain + 无电话 / WA）。国别错位：FG Spectral（.com.tr + A.Ş. = 土耳其主区，WA 未试）、Best / GSD Bilişim（土耳其语网店）、alles.dp.ua（表内俄罗斯 → 乌克兰守界）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    L += [f'## 回改：永久 pass → 留 C 待巡检（{len(fixed)}）', '', '| 编号 | 公司 / 名 | 国家 | 原批次 | 回改理由 |', '|---|---|---|---|---|']
    for k, o in fixed:
        e = ents[k]
        L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {o} | {sieve.md(FIX[k])} |")
    L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批33_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'fixed', len(fixed), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
