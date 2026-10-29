#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 47 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 661–715 户（按综合分序，SC-3132 … SC-3278；综合分 −69 → −100，桶底）。

构成：仅网址 / 平台链接无邮箱 24（nxdomain 8）、退信 12（其中无任何备用路径 5 → 闸 0 刚性②）、「无联系方式」名单 8（原表有微信 ID / 阿里后台 / 领英 / 谷歌链接者留 C；完全无迹可寻 2 → 闸 0 刚性①）、守界（乌克兰 2、伊朗 2、叙利亚 1）5、巨头 4（Ingram Micro、Telecom Egypt、ООО НАГ、Alhamrani）、中国大陆 2。
  · 口径：闸 0 刚性① = 无邮箱 / 电话 / WA / 域名 / 平台链接且原表无 @ / 7 位以上数字 / URL / 微信 / 领英；刚性② = 退信且无电话 / 域名 / 平台备用。Simon 「Spam / 不跟进」标记一律不是 pass 依据。
  · 候选 0。永久 pass 6 = SC-3145（gmail 退信无备用）/ SC-3179 Sinag-Tel CO（gmail 退信 + 域 nxdomain）/ SC-3227 3D Video（aol 退信无备用）/ SC-3258（hotmail 退信无备用）/ SC-3248 North American Cable Equipment（ISC 2011 仅公司名，CATV 发射机）/ SC-3276 PT Integra Global Solusi（富通天下名单仅公司名，无任何路径）。
  · 留意：XTCOM VN（光网视 / 大华，退信但域名在 → 找到邮箱即转候选）、Creative Security Systems IN（IndiaMART 页，新桥 PoE）、Forbatt ZA（谷歌链接；南非自有品牌分销 → oem_target 备查）、ООО НАГ RU（SNR 品牌巨头分销）、Jackee Chong MY（加了 Simon 微信，找 MC 供应商 = 本职线）。

用法：python3 sieve_batches/g1_047.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批47_2026-10-29.md）
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

BATCH = 'G1-47'
DATE = '2026-10-29'
CODES = ["SC-3132", "SC-3134", "SC-3137", "SC-3139", "SC-3140", "SC-3141", "SC-3142", "SC-3144", "SC-3145", "SC-3148", "SC-3409", "SC-3151", "SC-3156", "SC-3167", "SC-3170", "SC-3173", "SC-3179", "SC-3180", "SC-3181", "SC-3182", "SC-3184", "SC-3185", "SC-3187", "SC-3188", "SC-3189", "SC-3203", "SC-3205", "SC-3207", "SC-3208", "SC-3225", "SC-3227", "SC-3229", "SC-3232", "SC-3234", "SC-3235", "SC-3237", "SC-3240", "SC-3244", "SC-3245", "SC-3248", "SC-3249", "SC-3250", "SC-3255", "SC-3256", "SC-3257", "SC-3258", "SC-3410", "SC-3411", "SC-3263", "SC-3264", "SC-3267", "SC-3412", "SC-3413", "SC-3276", "SC-3278"]

OVERRIDE = {
    'SC-3145': ('pass_final', 'feruz929250@gmail.com（表内俄罗斯，备注乌兹别克斯坦；2017 年国际站「光猫」；退信 bounce=1；无电话 / 域名 / 平台）：退信且无电话 / 域名 / 平台备用路径 = 闸 0 刚性② → 永久 pass', []),
    'SC-3179': ('pass_final', '哥伦比亚 Sinag-Tel（sinagtelservices@gmail.com 退信；sinag-tel.co nxdomain；无电话；商业 PoE）：退信且无电话 / 域名 / 平台备用路径 = 闸 0 刚性② → 永久 pass（域名亦死，非备用路径）', []),
    'SC-3227': ('pass_final', '3D Video System（Adanie；adanielipvideo@aol.com 退信；国别未填；无电话 / 域名 / 平台；MC）：退信且无电话 / 域名 / 平台备用路径 = 闸 0 刚性② → 永久 pass', []),
    'SC-3258': ('pass_final', '美国 Irene Bess（feerykusky1@hotmail.com 退信；2022 年看了很多串口工业品；无电话 / 域名 / 平台）：退信且无电话 / 域名 / 平台备用路径 = 闸 0 刚性② → 永久 pass', []),
    'SC-3248': ('pass_final', '美国 North American Cable Equipment Inc（ISC 2011 展会名单；interested in CATV optical transmitters；原表无邮箱 / 电话 / 网址 / 微信 / 领英，无任何可寻路径）：闸 0 刚性①（无邮箱无 WA 无任何迹）+ 2011 陈旧 + CATV 发射机非 Saga 线 → 永久 pass', []),
    'SC-3276': ('pass_final', '印度尼西亚 PT Integra Global Solusi（富通天下名单；「从 VOLKTEK 买很多」；原表无邮箱 / 电话 / 网址 / 微信 / 领英，无任何可寻路径）：闸 0 刚性① → 永久 pass（如 Simon 想救回可按编号否决）', []),
    'SC-3205': ('keep_C', '越南 XTCOM Technology（xtcom.vn no_mx；xtcomtechnology@gmail.com 退信 ×2；工业交换机 + 商业 PoE 主要是大华、光网视的 ✔；有大华和很多外壳；「销售平台」）：越南先例 + 中国品牌 ✔ 但邮箱退信；域名存活 = 非刚性 → 留 C 待巡检（官网 / FB 找到邮箱即转候选）', []),
    'SC-3412': ('keep_C', '印度 Creative Security Systems, Ludhiana（IndiaMART 商品页 network-switch；「新桥商业 PoE」✔；谷歌来源；无邮箱 / 电话）：印度先例 + 中国品牌 ✔ 但仅平台链接 → 留 C 待巡检（IndiaMART 页取到邮箱即转候选）', []),
    'SC-3413': ('keep_C', '南非 Forbatt（谷歌搜索链接；商业 PoE；南非安防分销商，自有品牌 Forbatt 迹象 → oem_target 备查；无邮箱 / 电话）：南非先例 ✔ 自有品牌 ✔ 但路径未建 → 留 C 待巡检（找到邮箱即转候选）', ['oem_target']),
    'SC-3411': ('keep_C', 'Enable-IT（谷歌搜索链接 enableit；国别未填 → 美国；商业 PoE / PoE 配件；美国 EoC / PoE 延长品牌商）：品牌同行 → 留 C 同行观察', []),
    'SC-3410': ('keep_C', '韩国 Optowiz（LinkedIn 公司页；富通天下；SFP；无邮箱 / 电话）：光模块本职线 + 仅平台链接 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-3409': ('keep_C', '中国大陆（made-in-china 店铺链接；Smartbyte 同行表）：中国大陆同行 / 供应链域名（非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-3237': ('keep_C', '中国大陆 Longse（longse.com；商业 PoE；「很多在卖他们的」）：中国大陆同行 / 供应链域名（非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-3240': ('keep_C', '中国大陆 RAS CCTV（rascctv.com；广州一家的商业 PoE；「有人用他们的」）：中国大陆同行 / 供应链域名（非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-3134': ('keep_C', '格鲁吉亚 Lagi CCTV（lagicctv.ge 正常；gmail；网站 Skype 按钮；主要 CCTV，用台湾 Geovision 的；16 推 0 回）：CCTV 店 + 格鲁吉亚无先例 + 零回应 → 留 C', []),
    'SC-3137': ('keep_C', '菲律宾 MJ Auto-ID（mj-autoid.com 正常；网站有 CCTV 类项目；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3142': ('keep_C', '印度 SEC Communications（seccom.org 正常；Converging Conferencing Solutions；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；会议系统非 Saga 主线', []),
    'SC-3167': ('keep_C', '巴拿马 Ring Ring Energy（ringringenergy.com 正常；主要无源设备；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3180': ('keep_C', '沙特 Ansaries Security System（ansaries.com 正常；fiber HDMI & VGA + Video distributor；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；HDMI / VC 本职线', ['dayjob_fit']),
    'SC-3184': ('keep_C', '沙特 Kouja Trading（kjsecurity.com null_mx；CCTV & Satellite，need fiber optics sometimes；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3185': ('keep_C', '沙特 Last Vision（lastvision-sa.com 正常；「14 building, 320 cameras」项目；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；项目终端', []),
    'SC-3188': ('keep_C', 'Zener Electronics UAE（zeneradh.com 正常；表内沙特，实为阿联酋 → 国别待核；CCTV Solutions；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-3229': ('keep_C', '印度 Ezone Security Solutions（ezonesecurity.com 正常；1–4V data / audio price；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检；VC 本职线', ['dayjob_fit']),
    'SC-3232': ('keep_C', '沙特 Alhamrani Universal Company（universal.com.sa 正常；take catalog；原邮箱退信但域名存活）：沙特大集团 → 留 C 巨头 / 待巡检（非刚性）', []),
    'SC-3139': ('keep_C', '俄罗斯 安防公司（xn--80adgenjmx1d.xn--80adxhks nxdomain；很多摄像头；无邮箱）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3140': ('keep_C', '印度 Cochin Aircraft Maintenance Co（cochinamco.com nxdomain；无需求记录）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）；航空维修终端', []),
    'SC-3141': ('keep_C', '印度 Prash Trading Pvt. Ltd.（prashtrading.com nxdomain；无需求记录）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3148': ('keep_C', '马耳他 DSS Datanet Security Systems（dss.com.mt nxdomain；Calvin Marais；video converter information）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）；VC 本职线', ['dayjob_fit']),
    'SC-3170': ('keep_C', '沙特 / 沙迦 JEEYAR（jeeyarme.com nxdomain；knows MC and VC，lives in 沙迦）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）；MC / VC 本职线', ['dayjob_fit']),
    'SC-3182': ('keep_C', '卡塔尔 First Choice Cont. & Trad.（firstchoice-qa.com nxdomain；System integrator，just give price list for VC）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）；VC 本职线', ['dayjob_fit']),
    'SC-3189': ('keep_C', '沙特 Scientechic（ae-.com / scientechic.ae 均 nxdomain；need price list for CCTV）：域名 nxdomain + 无邮箱 / 电话 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3255': ('keep_C', 'Ingram Micro（ingrammicro.com；表内菲律宾；Kevin Mychal Ong，yahoo，邮件发送失败；2016 年「2.5G network switch」）：全球分销巨头 → 留 C 巨头（2.5G 口径待 SB-263）', []),
    'SC-3249': ('keep_C', '埃及 Telecom Egypt（te.eg；Dr. Amr Mohamed Refaat，gmail ×2，领英电话；主动问 DWDM / general information）：巨头运营商 + DWDM 本职线 → 留 C 巨头 + dayjob_fit', ['dayjob_fit']),
    'SC-3256': ('keep_C', '俄罗斯 ООО НАГ（NAG，原表仅 yandex 搜索链接；「switch / 线缆等分销商」「网站在维修」；富通天下）：俄罗斯最大网络设备分销之一，自有品牌 SNR → 留 C 巨头（oem_target 备查；路径未建）', ['oem_target']),
    'SC-3156': ('keep_C', '乌克兰 XMEye（xmeye.com.ua 正常；gmail；商业 PoE）：守界乌克兰（不 pass，不主动发）→ 留 C', []),
    'SC-3244': ('keep_C', '乌克兰 Vago（vago.ua 正常；MC / SFP / 无源；无邮箱）：守界乌克兰（不 pass，不主动发）→ 留 C', []),
    'SC-3187': ('keep_C', '伊朗 Tolue Co.（tolue.ir / rfid.ir 正常；VC for projects in Iran；无邮箱）：伊朗守界（不 pass，不主动发）→ 留 C；VC 本职线', ['dayjob_fit']),
    'SC-3264': ('keep_C', '伊朗 erdush_alireza@yahoo.com（VC price list）：伊朗守界（不 pass，不主动发）→ 留 C；VC 本职线', ['dayjob_fit']),
    'SC-3181': ('keep_C', '叙利亚 Cham Tech（cham-sy.com 正常；need IP cameras；无邮箱）：叙利亚守界 → 留 C', []),
    'SC-3235': ('keep_C', '哥伦比亚 SyG Sertesegur（Sergio Rangel；gmail 退信；电话 +57 315 510 7634 在 = 备用路径；4MP VC 需要高像素）：非刚性 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3250': ('keep_C', '阿尔及利亚 SEZGINE（Lameche Badreddine；gmail 退信 ×2；微信 / WhatsApp +213 44 28 1090 在）：非刚性 → 留 C（WA 路径）', []),
    'SC-3263': ('keep_C', '加拿大 ahmed.parvez79@gmail.com（退信；电话 908 475 7911 在但 WA 加不上；4 光 8 电工业 / 8 电口工业）：电话 = 备用路径，非刚性 → 留 C 待巡检', []),
    'SC-3278': ('keep_C', '沙特 Wisetech Co.（Eng. Ihab Doghmosh；hotmail 退信；电话 +966 532 709 392 在；VC）：非刚性 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3132': ('keep_C', '巴基斯坦 Teczium（Usama Hamid；原表「VX: usama_1991」= 微信 ID；2026-07 阿里询盘「EO Converter」；Simon 标不相关）：微信 + 阿里后台路径在 → 留 C 不主动（品类不符）', []),
    'SC-3144': ('keep_C', '沙特 Al Fisht Elect（Wamiq Wasi；2023-06 阿里询盘「2×2 bypass 50 个」；「没有联系方式，问客户要了没给」；后续不看消息）：阿里后台路径在 + bypass 本职线 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-3245': ('keep_C', '马来西亚 Jackee Chong（Malaysia fair；会中文；加了 Simon 微信 ✔；主要做 Passive，在找 MC / 工业 MC 供应商，在意价格；去了光博会）：微信路径 ✔ 但需求为 MC = 本职线 → 留 C + dayjob_fit（本职线优先）', ['dayjob_fit']),
    'SC-3257': ('keep_C', '印度 Suraj Ravindran（仅电话 8129183067；「对工业 2 光 4 电感兴趣，想大量买」；Simon 备注 Spam）：电话路径在；Simon 标记非 pass 依据 → 留 C 不主动', []),
    'SC-3267': ('keep_C', '阿联酋 Change Networks（change-networks.com 正常；digitalcndxb@gmail.com；FB 电话 +971 58 569 3600；COMMANDO 分销商；Simon 标 Spam / 不跟）：分销商 ✔ 但印度品牌代理 + 阿联酋无先例 + Simon 不跟 → 留 C 不主动', []),
    'SC-3151': ('keep_C', '安哥拉 Eugénio Hossi（gmail；WA +244 927 145 309 还没尝试加；工业自动化 Ethernet / 工业管理，「有需求会说」）：个人 + 无先例 → 留 C 储备', []),
    'SC-3173': ('keep_C', '突尼斯 Nasreddine Ghorri（gmail；「有兴趣合作」）：个人 + 无公司 → 留 C', []),
    'SC-3203': ('keep_C', '斯里兰卡 Jteem Solutions（jteemsolutions.com 正常；Nimantha，gmail；MC / 无源器件；3 推 0 回）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3207': ('keep_C', '埃及 Link2000（Hussein El Sayed，yahoo；price list for all；WA 加不上）：零信息 → 留 C', []),
    'SC-3208': ('keep_C', '阿尔及利亚 Mokhtar Belkhiati（gmail；会用到 MC OAM）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3225': ('keep_C', '俄罗斯 kdidkovsky@gmail.com（无需求记录）：零信息 → 留 C', []),
    'SC-3234': ('keep_C', '巴西 Omni do Brasil（omnidobrasil.com.br 正常；Pedro Alexandre Gomes，terra.com.br；Buy VC from US（fail）；WA 加不上）：巴西先例在 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 47 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 661–715 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：仅网址 / 平台链接 24、退信 12、无联系方式 8、守界 5、巨头 4、中国大陆 2。候选 0。永久 pass 6 = 退信无备用 4（SC-3145 / 3179 / 3227 / 3258）+ 仅公司名无任何路径 2（SC-3248 / 3276，闸 0 刚性①）。', '',
         '> 值得留意的留 C：XTCOM VN（找到邮箱即转候选）、Creative Security Systems IN（IndiaMART）、Forbatt ZA（oem_target 备查）、ООО НАГ / Merlion 级巨头、Jackee Chong MY（微信，MC 本职线）、Suraj Ravindran IN（「想大量买工业 2 光 4 电」但 Simon 标 Spam → 留 C 不主动）、8 户 nxdomain 待巡检。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批47_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
