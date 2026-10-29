#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 46 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 606–660 户（按综合分序，SC-2917 … SC-3114；综合分 −52 → −67；「用户判定不行 / 仅网址」密集段）。

构成：仅公司网址无邮箱 37（其中伊朗守界 7、巨头 / 品牌厂 6、域死 nxdomain 6）、免费邮箱个人 / 公司 12、Simon 标记不跟 2、退信无备用 1、无联系方式但路径在 1、政府 1。
  · 口径同第 45 批（仅网址 = 路径未建 → 留 C 待巡检；点名区 + 中国品牌 / 自有品牌 → 「找到邮箱即转候选」）。
  · 候选 2 = 俄罗斯 ConexPro（conexpro.com；Simon 备注「基本是全线帧田的」= 自有品牌全线 OEM 自中国 → oem_target；无邮箱，闸 2 先找路径；Simon 原判「不行」可否决）/ 葡萄牙 Metri Kingdom（metrikingdom.com；Saleha Kanwal；+351 电话；问 2 SFP + 2 RJ45 交换机；欧洲 + 对位 + 可达 + 可坐实）。
  · 永久 pass 1 = SC-3089 英国 Gvaman Consultancy（gmail 退信；无电话 / 域名 / 平台；交谈内容亦无记录 = 闸 0 刚性②）。
  · 留意：avpsecured.com IN（国内外壳，找到邮箱即转候选）、Khởi Nguyên VN（洪瑞 / 光网视 → Q-33）、Net Plus BR（2007 年合作过 MC = 老客户，本职线）、Intelec CR（商业 PoE 多外壳，WA 按钮）、Algérie Télécom 员工（想自己开公司找厂家，意愿强）。

用法：python3 sieve_batches/g1_046.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批46_2026-10-29.md）
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

BATCH = 'G1-46'
DATE = '2026-10-29'
CODES = ["SC-2917", "SC-2918", "SC-2920", "SC-1616", "SC-2925", "SC-2926", "SC-2927", "SC-2929", "SC-2932", "SC-2936", "SC-2938", "SC-2957", "SC-2958", "SC-2959", "SC-2961", "SC-2967", "SC-2969", "SC-2973", "SC-2974", "SC-2977", "SC-2978", "SC-2979", "SC-2981", "SC-2987", "SC-3000", "SC-3005", "SC-3010", "SC-3022", "SC-3026", "SC-2982", "SC-3029", "SC-3034", "SC-3035", "SC-3037", "SC-3042", "SC-3044", "SC-3045", "SC-3046", "SC-3047", "SC-3054", "SC-3066", "SC-3067", "SC-3069", "SC-3087", "SC-3089", "SC-3090", "SC-3091", "SC-3096", "SC-3098", "SC-3099", "SC-3105", "SC-3110", "SC-3111", "SC-3113", "SC-3114"]

OVERRIDE = {
    'SC-2957': ('candidate', '俄罗斯 ConexPro（conexpro.com 正常；Simon 二筛备注「基本是全线帧田的」✔ = 自有品牌、全线自中国 OEM；无邮箱）：俄罗斯点名区 ✔ 自有品牌 OEM 对象 ✔ 对位 ✔ 公司可坐实 ✔ → 闸 2 查底数（rusprofile / checko）+ 官网找采购路径；收款 / 物流待 Simon；Simon 原判「不行」→ 可按编号否决', ['oem_target']),
    'SC-2969': ('candidate', '葡萄牙 Metri Kingdom（metrikingdom.com 正常；Saleha Kanwal；+351 920 236 978；问「2 SFP + 2 RJ45 交换机」✔；无邮箱）：欧洲 ✔ 对位产品问 ✔ 电话 / WA 可达 ✔ 公司可坐实 ✔ → 闸 2 查底数（葡萄牙 NIF：racius / einforma 镜像）后 WA / 邮件一页纸（STC-228GP $33 锚）；微型则 △ 预付', []),
    'SC-3089': ('pass_final', '英国 Gvaman Consultancy Services（Brij Mishra Sales Head；brijmishra07@gmail.com 退信 bounce=1；无电话 / 无域名 / 无平台账号；「交谈内容无记录」）：退信且无任何备用路径 + 零内容 = 闸 0 刚性② → 永久 pass', []),
    'SC-2925': ('keep_C', '印度 AVP Secured（avpsecured.com 正常；商业 PoE，「看着像国内的外壳」✔；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（印度先例 + 中国外壳 → 找到邮箱即转候选）', []),
    'SC-3113': ('keep_C', '巴西 Net Plus（netplus.com.br 正常；「2007 年与我们合作过 / 来访过，MC 业务」；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（巴西先例 + 老客户；MC = 本职线优先重连）', ['dayjob_fit']),
    'SC-3000': ('keep_C', '墨西哥 Fibremex（fibremex.com 正常；无需求记录；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（墨西哥先例在，找到邮箱后看）', []),
    'SC-3047': ('keep_C', '罗马尼亚 AC-CSS（ac-css.ro 正常；CCTV price list；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（欧洲 CCTV 商，找到邮箱后看）', []),
    'SC-2959': ('keep_C', '俄罗斯 Satel TVK（sateltvk.ru 正常；「从 raisecom 买一些产品」；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（俄罗斯点名区，找到邮箱后看）', []),
    'SC-2961': ('keep_C', '俄罗斯 Vostok Electra（vostok-electra.ru 正常；无需求记录；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3091': ('keep_C', '俄罗斯 Secvior（secvior.ru 正常；just take the catalogue；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3087': ('keep_C', '俄罗斯 Data Group（datasystems.ru no_mx；无需求记录；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2929': ('keep_C', '俄罗斯 Netside（netside.ru 正常；SFP；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；SFP 本职线', ['dayjob_fit']),
    'SC-3099': ('keep_C', '俄罗斯 ООО Выпуск（ra-trent.ru no_mx；8V 视频光端机；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；VC 本职线', ['dayjob_fit']),
    'SC-2918': ('keep_C', '韩国 LS Simple（lssimple.co.kr no_mx；fiber optics / networking；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2926': ('keep_C', '印度尼西亚 CGS（cgs.co.id 正常；从 OPTONE 买模块；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；光模块本职线', ['dayjob_fit']),
    'SC-2927': ('keep_C', 'Evasion（evasion.com.tn 正常；表内「坦桑尼亚」，.tn = 突尼斯 → 国别待核；商业 PoE；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2958': ('keep_C', '加拿大 NLNTS（nlnts.tech 正常；SFP 模块；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；SFP 本职线', ['dayjob_fit']),
    'SC-2967': ('keep_C', '厄瓜多尔 Cablemodem（cablemodem.com.ec 正常；Alicia Lliguicota；MC / passive；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；MC 本职线（厄瓜多尔先例在）', ['dayjob_fit']),
    'SC-2977': ('keep_C', 'EM Comunitel（emcomunitel.com 正常；国别未填；无需求记录）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2978': ('keep_C', 'Función Digital（funciondigital.com 正常；国别未填；安防的）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2987': ('keep_C', '委内瑞拉 Techtrol Sistemas Electrónicos（techtrol.com.ve 正常；Video Servers / Video encoder；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；视频编码本职线', ['dayjob_fit']),
    'SC-3022': ('keep_C', '瑞士 MH Fiberoptics（mh-fiberoptics.com no_mx；MC / WDM / 跳线；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；MC / WDM 本职线', ['dayjob_fit']),
    'SC-3034': ('keep_C', '沙特 7 Stars（sevenstarstech.com 正常；take catalog；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3035': ('keep_C', '巴林 Almufeed Information Technology（almufeed.com 正常；catalogue；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3042': ('keep_C', '沙特 Manakh Shebah Al-Jazeerah（msj.com.sa 正常；历史报价 24ch video $1180/pair、1V1D $90/pair、MC $20；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；VC / MC 本职线', ['dayjob_fit']),
    'SC-3044': ('keep_C', '黎巴嫩 Safe Home（safehometechno.com 正常；need prices for 1ch / 2ch / 4ch and fiber；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；VC 本职线', ['dayjob_fit']),
    'SC-3045': ('keep_C', 'Star Max（starmaxuae.com no_mx；表内沙特，域名 UAE → 国别待核；4V1D；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；VC 本职线', ['dayjob_fit']),
    'SC-3037': ('keep_C', '沙特 BlueRays Technology LLC（blueraystechnology.com nxdomain；catalogue）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3090': ('keep_C', '俄罗斯 MPO RVM Yantsev（mporom.ru nxdomain；无需求记录）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-2917': ('keep_C', 'Ekinops（ekinops.com 正常；表内澳大利亚，总部法国；光传输设备巨头；「光派产品」）：巨头 + 本职线同行 → 留 C 巨头', ['dayjob_fit']),
    'SC-2932': ('keep_C', 'Proxim Wireless（proxim.com 正常；表内印度，美国品牌；主要无线 AP，可能需要 PoE）：无线品牌厂 → 留 C 巨头 / 品牌（OEM 可能性低）', []),
    'SC-2936': ('keep_C', '沙特 Det-Tronics（det-tronics.com 正常；火气探测品牌，Carrier 旗下；8-port ethernet switch）：跨国巨头子公司 → 留 C 巨头', []),
    'SC-2979': ('keep_C', 'GE Grid Solutions（gegridsolutions.com no_mx；Ethernet Optical，「功能比较复杂」）：GE 巨头 → 留 C 巨头', []),
    'SC-2981': ('keep_C', 'VIAVI Solutions（viavisolutions.com 正常；光开关）：测试仪表巨头 + 本职线 → 留 C 巨头', ['dayjob_fit']),
    'SC-3029': ('keep_C', '南非 Phalaborwa Mining Company（riotinto.com；Rio Tinto 矿业巨头终端；video to wireless）：巨头终端 → 留 C 巨头', []),
    'SC-2974': ('keep_C', 'Angustos（angustos.com 正常；国别未填；Simon「同行」）：同行 → 留 C 同行观察', []),
    'SC-2938': ('keep_C', '伊朗 Narfoamkar Company（narfoamkar.com 正常；switch for IP camera；无邮箱）：伊朗守界（不 pass，不主动发）→ 留 C', []),
    'SC-3046': ('keep_C', '伊朗 Tehran Nikava Co（nikava.biz 正常；无需求记录；无邮箱）：伊朗守界（不 pass，不主动发）→ 留 C', []),
    'SC-3054': ('keep_C', '伊朗 HARG Co（hargco.com nxdomain；4 people；telecom MC）：伊朗守界（不 pass，不主动发）→ 留 C；域死', []),
    'SC-3066': ('keep_C', '伊朗 VAFCO（vafco.ir 正常；SDH / PDH / Wireless，在和 WRI 合作；与 SC-3067 vafcorp.com 同一户）：伊朗守界（不 pass，不主动发）→ 留 C；SDH 本职线', ['dayjob_fit']),
    'SC-3067': ('keep_C', '伊朗 VAF Corp（vafcorp.com nxdomain；与 SC-3066 vafco.ir 同一户 → 待并档）：伊朗守界（不 pass，不主动发）→ 留 C', []),
    'SC-3069': ('keep_C', '伊朗 Yas Communication（yascommunication.com nxdomain；无需求记录）：伊朗守界（不 pass，不主动发）→ 留 C；域死', []),
    'SC-3111': ('keep_C', 'Government of Sharjah（Bijee Phillip；bijee@eim.ae；表内沙特，实为阿联酋沙迦政府；need price for 4V1D / 8V / 1V）：政府终端 + VC 本职线 → 留 C 守界', ['dayjob_fit']),
    'SC-2982': ('keep_C', '越南 Viễn Thông Khởi Nguyên（vienthongkhoinguyen.com nxdomain；gmail；商业 PoE 主要是洪瑞、光网视的 ✔；10 推 0 回）：洪瑞渠道 → Q-33 口径待 Simon（越南先例 + 中国品牌，口径放开即转候选）→ 留 C', []),
    'SC-1616': ('keep_C', '越南 Phụ Kiện Điện Tử（phukiendientu.vn / .com 均 no_mx；gmail；switch）：电子配件网店 → 留 C', []),
    'SC-3005': ('keep_C', '哥斯达黎加 Intelec（intelec.co.cr 正常；商业 PoE 为主，好多种外壳 ✔；「销售平台」；网站 WA 按钮 +506 8468 3532）：中国外壳 ✔ WA 可达 ✔ 但哥斯达黎加无先例 + 平台型 → 留 C 储备（WA 一页纸一次后看）', []),
    'SC-3098': ('keep_C', '马来西亚 Startech IT Sdn Bhd（startechit.com.my 域死；Kangson Wang；gmail；WA / 微信按钮 +60 167 728 962；MC / VC 产品来自多家，周边产品）：MC / VC 本职线 + 域死 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2973': ('keep_C', '吉尔吉斯斯坦 SJT Service Ltd.（Kayrat Sharshenbaev；kostaneda@inbox.ru；Skype；48V 收发器 / 协转）：收发器本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3114': ('keep_C', '阿尔及利亚 Abdelmadjid Damis（Algérie Télécom 员工，algerietelecom.dz；damis_maj@yahoo.fr；WA +213 661 682 908 可加；「想自己开公司找厂家，意愿比较强」）：个人创业意向 ✔ 但无公司 + 阿尔及利亚无先例 → 留 C 储备（成立公司后再看）', []),
    'SC-3026': ('keep_C', '喀麦隆 Norbert Ndongo（gmail；「有需求会说」，问了 catalog；WA 还没尝试加）：个人 + 无先例 → 留 C', []),
    'SC-3105': ('keep_C', 'Gladness Bokamoso Lekgoa（lbgladness@gmail.com；国别未填 → 疑南非 / 博茨瓦纳；「有兴趣在南非搞一个 office」）：个人意向 + 无公司 → 留 C', []),
    'SC-3110': ('keep_C', '孟加拉 Bari（2020-12 询盘「HDMI 1 网 1 USB」；表内无联系方式但 11 推 = 路径在）：HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2920': ('keep_C', '肯尼亚 Tony（rbltny@gmail.com；VC general）：VC 本职线 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3010': ('keep_C', '印度 Rk（mdakhtar943.phusro@gmail.com；2 光 4 PoE 大壳；1 推；Simon 标记不再跟进 / Spam）：Simon 备注非闸 0 依据 → 留 C 不主动', []),
    'SC-3096': ('keep_C', '巴西 Eliane Ramos（bol.com.br；2010 年注册；网站搜出来不相关；Simon 标记不再跟进）：Simon 备注非闸 0 依据 → 留 C 不主动', []),
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
    L = [f'# C 池 · 闸 1 · 第 46 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 606–660 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：仅网址 37（伊朗 7、巨头 6、域死 6）、免费邮箱 12、Simon 不跟 2、退信 1、路径在 1、政府 1。候选 2 = 俄罗斯 ConexPro（自有品牌，帧田 OEM）+ 葡萄牙 Metri Kingdom（欧洲 + 产品问 + 电话）。永久 pass 1 = SC-3089（退信无备用路径）。', '',
         '> 值得留意的留 C：avpsecured.com IN（找到邮箱即转候选）、Khởi Nguyên VN（洪瑞 Q-33）、Net Plus BR（2007 老客户 MC）、Intelec CR（WA 按钮）、Abdelmadjid Damis DZ（想开公司找厂家）、6 户 nxdomain 待巡检「下次仍死即 pass」、ConexPro 原为 Simon「判定不行」→ 已改候选可否决。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批46_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
