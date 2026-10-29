#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 32 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 1101–1155 户（按综合分序，SC-2801 … SC-3002）。

构成：几乎全是「用户判定不行 / 不相关」（52 / 55；按 U115 全部过筛），其中退信 22（域名多正常 → 待巡检）、台湾 / 韩国同行与品牌商 12、俄罗斯 6、孟加拉 5、澳大利亚 5、国别错位 3（kabel.sk 写斯里兰卡 = 斯洛伐克；antena.md 写孟加拉 = 摩尔多瓦；brightsolutions.ae 写沙特）、平台邮箱 1（info@avito.ru）。
  · 口径同桶 ⑥ 首批 + 「贴牌 / 自有品牌 = OEM 对象」线（上一批起）。「刷的自己 logo」「带标卖」= 自有品牌证据。
  · 候选 6 = Neousys TW（工业电脑品牌商，自有 5 电口工业 FS；20 推 0 回 → 换 OEM 稿）/ SBJ Link → Konten Networks TW（「刷的自己 logo」工业 FS / SFP / MC / 串口）/ Trimatrik BD（「ONV 的商业 PoE 带标卖」+ 官网手机）/ Akatel RU（「从中间商采购中国产品，想从中国直接购买」= 真意向；akatel.ru no_mx 但 alarmex.ru 正常）/ PIIR RU（卖本土牌子、用的国内的 = 中国货分销）/ LS Networks ZA（HDMI + 工业 PoE + MC，Simon 备注「单独跟进」；南非有先例）→ 闸 2 查底数。
  · 永久 pass 2 = info@avito.ru（Avito 分类广告平台公共邮箱，非买家主体；19 推 0 回）/ GMD Telecom KR（gmdtelecom.co.kr 唯一域 no_mx + 退信，无人名 / 电话 → 闸 0 刚性 G0-2）。
  · 其余留 C：退信待巡检（DEONET KR 有人名 KIM YEONG MAN 域疑拼错 · Tropical Computers AU 有手机 · Vedinfo IN 三旺进口 + 手机 → 通了转候选 · Pixel Global AV 要报价 · Antena .md 洪瑞 · Techwindow BD 洪瑞 · Space Electronics LB · Advanet JP · AEparts KR · Alpha Networks TW ODM 巨头 · Ambertech AU 平台 · Avation AU · Carelink HK · Celan TW · Daara KR Moxa 代理 → 通了转候选 · Digiasia SG · Eusso TW 品牌 · Head KR Edimax）；域 dead 无退信记录（Justec TW · OXO RU · ISA Service · BrasilSeg BR · Microcomms BH · ADS-Leb）；本职线 dayjob_fit（FSN KR 1v1a1d · OXO SFP · Vitag NZ HDMI over fiber · ISA SM MC · Fibridge AU VC）；同行 / 品牌站并入（SNR = NAG 自有品牌站 → 并入 NAG 户 · RDP.ru 俄罗斯网络设备厂）；分销储备（Origo TW 用 Unipoe 18 推 0 回 · ArgSeguridad AR · Top Security PE Utepo · Hasnet TZ · Suprinordeste BR · Rasatech BD · CSE JO · Telecom Specialties GE「主要卖别人的」· Kital PH · Kabel .sk 国别待核 → 若斯洛伐克则下轮复看）；乌克兰 Elvis 守界；白俄 TCM ISP；大学 ASWAra MY；Sysnetpro CM no_mx + WA 加不上（无退信记录 → 留 C 复核 MX）。
  · 「用户判定不行」/「stop」flag 均非客户明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_032.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批32_2026-10-29.md）
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

BATCH = 'G1-32'
DATE = '2026-10-29'
CODES = ["SC-2801", "SC-2803", "SC-2807", "SC-2815", "SC-2817", "SC-2819", "SC-2827", "SC-2836", "SC-2839", "SC-2840", "SC-2841", "SC-2842", "SC-2843", "SC-2846", "SC-2851", "SC-2857", "SC-2860", "SC-2861", "SC-2863", "SC-2865", "SC-2866", "SC-2875", "SC-2885", "SC-2891", "SC-2904", "SC-2905", "SC-2908", "SC-2911", "SC-2913", "SC-2914", "SC-2916", "SC-2922", "SC-2931", "SC-2960", "SC-2963", "SC-2970", "SC-2971", "SC-2972", "SC-2975", "SC-2980", "SC-2984", "SC-2985", "SC-2986", "SC-2988", "SC-2989", "SC-2990", "SC-2991", "SC-2992", "SC-2994", "SC-2996", "SC-2997", "SC-2998", "SC-2999", "SC-3001", "SC-3002"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2 ----
    'SC-2839': ('candidate', '台湾 Neousys Technology（neousys-tech.com；工业电脑品牌商，自有 5 电口工业 FS 宣传图做得不错；20 推 0 回）：品牌商 = OEM 对象 ✔ 对位 ✔（台湾 OEM 先例已入池）；→ 闸 2 查底数（twincn）后换 OEM 稿；低优先', ['oem_target']),
    'SC-2971': ('candidate', '台湾 SBJ Link → Konten Networks（sbjlink.com / konten-networks.com；「刷的自己 logo」工业 FS / SFP / 工业 MC / 串口，看着像深圳的；5 推 0 回）：自有品牌 = OEM 对象 ✔ 对位 ✔；→ 闸 2 查底数（twincn）后换 OEM 稿；低优先', ['oem_target']),
    'SC-2891': ('candidate', '孟加拉 Trimatrik（trimatrikbd.com；「ONV 的商业 PoE 带标卖」；官网手机 +880 1785 777722）：贴自有牌 = OEM 对象 ✔ 对位 ✔；非点名国 → 闸 2 查底数（官网 / RJSC 镜像）后换 OEM 稿；低优先', ['oem_target']),
    'SC-2972': ('candidate', '俄罗斯 Akatel（akatel.ru no_mx；alarmex.ru 正常 = 换址；「从中间商采购中国产品，想从中国直接购买」；两部座机，WA 加不上）：真意向 ✔ Simon 点名俄罗斯 ✔；→ 闸 2 查底数（rusprofile）+ 换 alarmex.ru 地址；俄语区收款待定', []),
    'SC-2841': ('candidate', '俄罗斯 PIIR（piir.ru；一些本土的牌子，用的国内的 = 中国货分销）：分销 + 中国同类 ✔ Simon 点名俄罗斯 ✔；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-2885': ('candidate', '南非 LS Networks (Pty) Ltd（plugandplay.co.za；HDMI + 工业级 PoE 交换机 + MC；Simon 备注「单独跟进」）：真需求 ✔ 对位 ✔ 南非有先例（MiRO / Scoop / Reditron 已入池）；→ 闸 2 查底数（CIPC 镜像 / 官网）；低优先', []),
    # ---- 永久 pass ----
    'SC-2863': ('pass_final', 'info@avito.ru（Avito 分类广告平台公共邮箱；备注「主要是 hasivo 的商业 PoE」指平台上某卖家；19 推 0 回）：平台公共邮箱 = 非买家主体，无任何真实公司 / 人 → 永久 pass（真实卖家另行建户）', []),
    'SC-3001': ('pass_final', '韩国 GMD Telecom（gmdtelecom.co.kr 唯一域 no_mx；退信「发不过去」；无人名 / 电话）：退信 + 全部域名死 + 无备用路径 → 闸 0 刚性 G0-2 → 永久 pass', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-2846': ('keep_C', '韩国 DEONET（denot.co.kr nxdomain；退信；attn KIM YEONG MAN；问 PoE 芯片 / GPON / EPON；9 推）：域名疑拼错（deonet）+ 有人名 → 非刚性 → 留 C 待巡检（找正确域名后可转候选）', []),
    'SC-2857': ('keep_C', '澳大利亚 Tropical Computers Cairns（tropicalcompaters.com.au nxdomain 疑拼错；退信；问 VC / switch；手机 +61 4477 90936）：电话路径在 → 留 C 待巡检', []),
    'SC-2908': ('keep_C', '印度 Ved Info Services（vedinfoservices.com 正常；.co.in nxdomain；退信；从国内买 switch 等，三旺的；工业 FS / MC / VC / PoE / 机架；手机在表）：进口中国同类 ✔ 但退信 → 留 C 待巡检（通了即转候选）', []),
    'SC-2931': ('keep_C', 'Pixel Global AV（pixelglobalav.com 域正常；国别未填；退信；对 PoE switch 有兴趣、要求报价单）：真意向 ✔ 但退信 + 国别未知 → 留 C 待巡检（通了即转候选）', []),
    'SC-2975': ('keep_C', 'Antena（antena.md；表内「孟加拉国」实为 .md 摩尔多瓦 → 国别待核；退信；商业 PoE 主要洪瑞 + 国内好几家）：退信待巡检 + 洪瑞 Q-33 + 国别待核（欧洲边缘）→ 留 C', []),
    'SC-2980': ('keep_C', '孟加拉 Techwindow（techwindowbd.com 域正常；退信；商业 PoE 主要洪瑞和另一家）：退信 + 洪瑞 Q-33 → 留 C 待巡检', []),
    'SC-2986': ('keep_C', '黎巴嫩 Space Electronics Company（idm.net.lb / inco.com.lb 正常；退信；商业 PoE 为主，到处发名片；两部手机）：退信但电话路径在 → 留 C 待巡检', []),
    'SC-2988': ('keep_C', '日本 Advanet（advanet.co.jp 域正常；退信；工业 FS）：工业电脑厂同行 + 退信 → 留 C 待巡检', []),
    'SC-2989': ('keep_C', '韩国 AEparts（aeparts.kr 域正常；退信；switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2990': ('keep_C', '台湾 Alpha Networks（alphanetworks.com；退信；大口 L3 / 工业 FS）：台湾 ODM 巨头同行 → 留 C（巨头不永久 pass）', []),
    'SC-2991': ('keep_C', '澳大利亚 Ambertech（ambertech.com.au 域正常；退信；多外壳商业 PoE 销售平台）：平台型 + 退信 → 留 C 待巡检', []),
    'SC-2992': ('keep_C', '澳大利亚 Avation（avation.com.au 域正常；退信；商业 PoE）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2994': ('keep_C', '香港 Carelink（carelink.com.hk 域正常；退信；SFP / MC / 机架 / switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2996': ('keep_C', '台湾 Celan（celan.com.tw 域正常；退信；switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2997': ('keep_C', '韩国 Daara Mall（daaramall.co.kr 退信；daara.co.kr 正常；Moxa 的工业 FS）：韩国工业代理 ✔ 备用域在 → 留 C 待巡检（换 daara.co.kr，通了即转候选）', []),
    'SC-2998': ('keep_C', '新加坡 Digiasia（digiasia.com.sg 域正常；退信；MC / FS）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2999': ('keep_C', '台湾 Eusso（eusso.com 域正常；退信；PoE injector / switch 少 / VC 周边）：台湾品牌同行 + 退信 → 留 C 待巡检', []),
    'SC-3002': ('keep_C', '韩国 Head（head.co.kr 域正常；退信；Edimax 的工业 FS）：韩国代理 + 退信 → 留 C 待巡检（通了可转候选）', []),
    'SC-2807': ('keep_C', '台湾 Justec（justec.com.tw nxdomain；官网打不开）：域死但无退信记录 → 留 C 待巡检', []),
    'SC-2815': ('keep_C', '俄罗斯 OXO Electronics（oxorus.ru nxdomain；SFP）：域死无退信记录 + 本职线 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2827': ('keep_C', 'ISA Service（isaservice.com 域 dead；表内名「fail」；very interested in SM MC）：域死无退信记录 + MC 可带 STC-110XGE → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2985': ('keep_C', '巴西 BrasilSeg（brasilsegdistribuidora.com.br nxdomain；备注空）：域死无退信记录 → 留 C 待巡检', []),
    'SC-2913': ('keep_C', '巴林 Microcomms（alsaad.net no_mx；备注空）：无 MX 但无退信记录 → 留 C 复核 MX', []),
    'SC-2914': ('keep_C', 'ADS（ads-leb.com nxdomain；表内沙特，域名疑黎巴嫩 → 国别待核；take catalogue）：域死无退信记录 → 留 C 待巡检', []),
    'SC-2922': ('keep_C', '喀麦隆 Systems Network Professional（sysnetpro.com no_mx；两部电话 WA 加不上；MC）：无 MX 但无退信记录 → 留 C 复核 MX（不作 pass）', []),
    'SC-2803': ('keep_C', '韩国 FSN Corp.（fsn.co.kr；1v1a1d 光端机）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2817': ('keep_C', '新西兰 Vitag（vitag.co.nz；interested in HDMI over fiber；WA 加不上）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2860': ('keep_C', '澳大利亚 Fibridge（fibridge.com.au / graftekmarketing.com；VC 为主 + 协议转换器；23 推 0 回）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2819': ('keep_C', '俄罗斯 SNR（snr.systems；大口 FS / SFP；SNR = NAG 自有品牌站；1 推）：品牌站 → 并入 NAG 户（已在跟进）→ 留 C（不单独建线）', []),
    'SC-2842': ('keep_C', '俄罗斯 RDP.ru（bypass / 高速大口 switch 自产网络设备厂）：俄罗斯同行制造商 → 留 C', []),
    'SC-2840': ('keep_C', '台湾 Origo（origo.tw；用的 Unipoe 工业系列；18 推 0 回）：进口中国同类 ✔ 但 18 推 0 回 + 非点名国 → 留 C（储备，换稿后再看）', []),
    'SC-2836': ('keep_C', '阿根廷 ArgSeguridad（argseguridad.com；卖深圳某牌商业 PoE；官网 WA +54 9 11 6306 5885；1 推）：进口中国同类 ✔ 但阿根廷无先例 → 留 C（储备）', []),
    'SC-2843': ('keep_C', '秘鲁 Top Security Peru（topsecurityperu.com；商业 PoE 主要 Utepo；官网 WA；1 推）：CCTV 店 + 秘鲁无先例 → 留 C（储备）', []),
    'SC-2861': ('keep_C', '坦桑尼亚 Hasnet ICT（hasnetict.com / hasnet.co.tz；像 hisource 的商业 PoE；1 推）：无先例 + 零回应 → 留 C（储备）', []),
    'SC-2875': ('keep_C', '巴西 Supri Nordeste（suprinordeste.com.br；商业 PoE 好几个牌子）：CCTV 店（非专业整线分销）→ 留 C（储备）', []),
    'SC-2970': ('keep_C', '孟加拉 Rasatech（rasatechbd.com；买的磊通的一些设备，很多供应商）：多供应商采购 + 非点名国 → 留 C（储备）', []),
    'SC-2916': ('keep_C', '约旦 CSE（cse.jo / csejo.com；MC / 商业 FS 周边；17 推 0 回）：零回应 + 非点名国 → 留 C（储备）', []),
    'SC-2960': ('keep_C', '格鲁吉亚 Telecom Specialties（telecomspecialties.com；「带着牌子卖 MC / SFP / 工业 FS，主要是卖别人的产品」；17 推 0 回）：自有牌证据含糊 → 留 C（储备；同国 Protech 已候选）', []),
    'SC-2801': ('keep_C', '菲律宾 Kital（kital.com.ph；商业 PoE；1 推）：无品牌证据 + 非点名国 → 留 C', []),
    'SC-2866': ('keep_C', 'Kabel（kabel.sk；表内「斯里兰卡」实为 .sk 斯洛伐克 → 国别待核；商业 PoE；4 推 0 回）：若核实为斯洛伐克 = 欧洲 → 下轮复看；现无中国品牌证据 → 留 C', []),
    'SC-2963': ('keep_C', '乌克兰 Elvis（elvis.com.ua；商业 PoE 卖很多牌子；17 推）：乌克兰 = 守界（非永久 pass）→ 留 C', []),
    'SC-2851': ('keep_C', '白俄罗斯 TCM（tcm.by；Internet provider；WA 加不上）：ISP 终端 → 留 C', []),
    'SC-2984': ('keep_C', '马来西亚 ASWAra（um.edu.my；在学校工作，用商业级 24 / 48 口 L2 / L3 管理，在意 VLAN，偶用 SFP）：学校终端个人 → 留 C', []),
    'SC-2865': ('keep_C', '哥伦比亚 IT-Cloud（it-cloud.com.co / itcloud.com.co；Bypass 模块；官网 WA）：Bypass 非 Saga 线 → 留 C', []),
    'SC-2904': ('keep_C', '南非 Firsttech（firsttech.co.za；电话未尝试；邮件中有详细联系信息）：无产品信息 → 留 C', []),
    'SC-2911': ('keep_C', 'Bright Solutions（brightsolutions.ae；表内沙特，域名阿联酋 → 国别待核；take catalog）：无产品信息 → 留 C', []),
    'SC-2905': ('keep_C', '越南 KTD（ktd.vn；备注空）：无信息 → 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 32 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 1101–1155 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：「用户判定不行」52 / 55（按 U115 全部过筛），其中退信 22、台湾 / 韩国同行与品牌商 12、俄罗斯 6、孟加拉 5、澳大利亚 5、国别错位 3（kabel.sk / antena.md / brightsolutions.ae）、平台邮箱 1。口径同桶 ⑥ 首批 + 「贴牌 / 自有品牌 = OEM 对象」线。候选 6 = Neousys（TW，品牌商）/ SBJ Link → Konten（TW，刷自己 logo）/ Trimatrik（BD，ONV 带标卖）/ Akatel（RU，想从中国直购，换址 alarmex.ru）/ PIIR（RU，中国货分销）/ LS Networks（ZA，工业 PoE + MC，Simon「单独跟进」）；永久 pass 2 = info@avito.ru（平台公共邮箱）/ GMD Telecom KR（唯一域死 + 退信）。留 C：退信待巡检（DEONET KR · Vedinfo IN · Daara KR · Head KR 等通了即转候选）、域 dead 无退信记录、本职线 dayjob_fit、品牌站并入（SNR → NAG）、分销储备、乌克兰守界、学校 / ISP 终端。「用户判定不行」/「stop」flag 均非客户明确拒绝，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批32_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
