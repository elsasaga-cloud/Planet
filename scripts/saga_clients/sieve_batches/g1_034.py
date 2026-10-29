#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 34 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 1211–1257 户（按综合分序，SC-3129 … SC-3314）—— **桶 ⑥ 收口**。

构成：「用户判定不行 / 不相关」42 / 47 + 守界乌克兰 3 + 巨头 2（Datacom BR 同行制造、ATC 科威特）；退信 26、Simon 标「Spam / stop」14、印度 8、巴西 5、台湾 5、巴基斯坦 3、格鲁吉亚 3。
  · 口径同桶 ⑥ 首批 + 第 33 批收紧（退信 + no_mx 留 C 待巡检）。「Spam / stop」= 我方备注，非客户要求停发 → 不作 pass 依据。
  · 候选 3 = TVC MX（tvc.mx；Utepo / 大华大分销；官网 WA → 墨西哥先例 SYSCOM 已入池）/ Starcom PK（starcom.com.pk；从 Raisecom 采购；2026-02 真人回「请用公司域名邮箱发」= 真回 ✔；手机在表）/ Techroutes IN（techroutes.com；商业 + 工业 FS；两位具名 KP + 手机；Simon 标 Spam → 可否决）。
  · 永久 pass 0：premua.com（乌克兰；退信 + nxdomain）按「乌克兰一律守界不永久 pass」留 C。
  · 其余留 C：守界 NET’s / Premua / Ritm（乌克兰）、Avang（伊朗）；同行 / 品牌商 Datacom BR、LinkPro / MLinkSys / Tainet TW、Corecess KR（PON）；巨头终端 ATC KW（光端机 24 / 32 路问价 → dayjob）；
    Q-33 渠道冲突 x-pon.ru（卖 SmartByte 的 = 现有渠道客户 → 待裁不主动碰）；运营商 Cybernet PK；本职线 dayjob_fit 11（VC / 光端机 / bypass / fiber tap / 无源 / 光产品）；
    国别待核 ue-it.de（表内未填 → .de 德国主区，Peplink 分销，退信待巡检）；WAGO India（巨头子公司，从 Volktek 买工业交换机；wagoindia.com nxdomain 无退信 → 换 wago.com 域后转候选）；
    澳大利亚 Motherwell Automation（迈威工业 FS；双地址退信 + no_mx → 找新域名后转候选）。

用法：python3 sieve_batches/g1_034.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批34_2026-10-29.md）
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

BATCH = 'G1-34'
DATE = '2026-10-29'
CODES = ["SC-3129", "SC-3130", "SC-3136", "SC-3138", "SC-3103", "SC-3149", "SC-3150", "SC-3152", "SC-3153", "SC-3154", "SC-3155", "SC-3157", "SC-3159", "SC-3160", "SC-3161", "SC-3162", "SC-3163", "SC-3164", "SC-3165", "SC-3166", "SC-3177", "SC-3178", "SC-3186", "SC-3197", "SC-3198", "SC-3201", "SC-3202", "SC-3210", "SC-3213", "SC-3215", "SC-3216", "SC-3217", "SC-3222", "SC-3224", "SC-3226", "SC-3230", "SC-3231", "SC-3238", "SC-3239", "SC-3246", "SC-3252", "SC-3265", "SC-3269", "SC-3295", "SC-3298", "SC-3299", "SC-3314"]

Q33 = '；洪瑞 / SmartByte 现有渠道客户 → Q-33 口径待 Simon'
VETO = '；Simon 曾标 Spam / 不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2 ----
    'SC-3130': ('candidate', '墨西哥 TVC（tvc.mx；Utepo / 大华等 CCTV 大分销，「主要是 CCTV」；官网 WA 按钮 +52 81 1799 1777；1 推 0 回；soporte@ 为支持信箱）：大分销 + 中国品牌 ✔ 对位 ✔ 墨西哥先例 SYSCOM 已入池 ✔ → 闸 2 查底数（RFC / D&B）后换 ventas / compras 地址 + WA 一页纸' + VETO, []),
    'SC-3149': ('candidate', '巴基斯坦 Starcom（starcom.com.pk / starcom.net.pk；switch + 安防，从 Raisecom 买一些产品；OTN 方案商；2026-02-26 真人回「Please send us email from your company Email domain」= 真回 ✔；ali@ 具名 + 手机 +92 300 202 1141；info@ 曾退信）：决策人真回 ✔ 进口中国同类 ✔ 对位 ✔ → 闸 2 查底数（SECP 镜像）后用 sagatele.com 域名重发 + 预付 100%', []),
    'SC-3198': ('candidate', '印度 Techroutes（techroutes.com；商业 FS + 工业 FS switch；dinesh.rastogi@ / kdeepak@ 两位具名；手机 93000 69633「好像是没加」；Simon 标 Spam）：印度点名国 ✔ 对位 ✔ 决策人具名 ✔ 手机路径 ✔（§5 ≥4 条）→ 闸 2 查底数（MCA 镜像；核是否自有品牌 → oem_target）' + VETO, []),
    # ---- 守界 ----
    'SC-3202': ('keep_C', '乌克兰 NET’s（nets.com.ua 域正常；Modems；WA 加不上）：乌克兰 = 守界（非永久 pass）→ 留 C', []),
    'SC-3215': ('keep_C', '乌克兰 Premua（premua.com nxdomain；退信「发送失败」；MC / 工业 FS / PoE / SFP）：形式上满足 G0-2，但乌克兰一律守界不永久 pass（U117）→ 留 C 待巡检', []),
    'SC-3216': ('keep_C', '乌克兰 Ritm Industry（ritmindustry.com 域正常；退信；工业 FS 很多牌子）：乌克兰 = 守界 → 留 C', []),
    'SC-3210': ('keep_C', '伊朗 Avang（avang.ir 域正常；光路的 10G MC，有 FS 的图；stop）：伊朗 = 制裁 / 守界 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    # ---- 同行 / 品牌商 / 巨头 ----
    'SC-3103': ('keep_C', '巴西 Datacom（datacom.com.br / datacom.ind.br；巴西本土电信设备制造商，自研交换机 / OLT；FS / SFP 大口 / 10G；退信 caroline.souza@，selecao@ 为招聘信箱）：同行制造商 + 巨头 → 留 C（不 pass）', []),
    'SC-3164': ('keep_C', '台湾 LinkPro（linkpro.com.tw no_mx；两地址发送失败；工业 FS / MC / 大口 FS / PoE / SFP；stop）：台湾网络品牌 = 同行 + 退信 no_mx → 留 C 待巡检', []),
    'SC-3165': ('keep_C', '台湾 MLinkSys（mlinksys.com 域正常；MC / FS / PoE「外观看着一般」；stop）：台湾品牌 = 疑同行 → 留 C', []),
    'SC-3231': ('keep_C', '台湾 Tainet（tainet.net 域正常；MC / SFP / 16 槽机架；peter.lee@；stop）：台湾 MC 品牌制造商 = 同行 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3213': ('keep_C', '韩国 Corecess（corecess.com no_mx；退信；基本是 PON 产品）：PON 厂商 = 同行 / 非 Saga 线 + 退信 no_mx → 留 C 待巡检', []),
    'SC-3177': ('keep_C', '巴基斯坦 Cybernet（cyber.net.pk 域正常；退信；在 Cisco 帖子下评论 price）：运营商 / ISP → 留 C', []),
    'SC-3314': ('keep_C', '科威特 Advanced Technology Company KSC（atc.com.kw 域正常；退信 subu@；WA 加不上；「16V $850，want prices for 24ch / 32ch，buying from Shanghai」= 光端机多路问价）：巨头集团终端 + 本职线 → 留 C + dayjob_fit（来询被动报价）', ['dayjob_fit']),
    'SC-3222': ('keep_C', '印度 WAGO India（wagoindia.com nxdomain，无退信记录；anilkumar@ 具名；「从 Volktek 买工业交换机」= 台湾品牌 ✔；Simon 标 Spam）：德国巨头印度子公司 + 印度点名国 ✔ 但旧域已死 → 留 C 待巡检（换 wago.com 域找到地址即转候选，长线）' + VETO, []),
    'SC-3238': ('keep_C', '澳大利亚 Motherwell Automation（motherwell.net.au no_mx；两地址退信；「很多迈威的工业 FS，也有光路的」= 中国工业品牌 ✔；21 推 0 回；stop）：澳大利亚先例 ✔ 对位 ✔ 但不可达 → 留 C 待巡检（找新域名 / 地址后转候选）', []),
    # ---- Q-33 ----
    'SC-3201': ('keep_C', '俄罗斯 X-PON（x-pon.ru 域正常；「Dptek 的商业级、SmartByte 的」= 已在售 SmartByte 产品 = 原厂 / 现有渠道客户；stop）：Q-33 渠道冲突待裁，不主动碰 → 留 C' + Q33, []),
    # ---- 本职线 dayjob_fit ----
    'SC-3129': ('keep_C', '印度 Smartnet Networks（smartnetnetworks.net 域正常；退信 sales@；「方案解决商，质量感觉不错，工业 FS / Bypass 周边」）：印度点名国 ✔ 工业对位 ✔ + bypass 本职 → 留 C + dayjob_fit；退信待巡检（通了可转候选）', ['dayjob_fit']),
    'SC-3136': ('keep_C', '俄罗斯 Kamsan（kamsan.ru null_mx = 邮件已关；k.matveev@ 具名；VC）：本职线 VC + 邮件关闭无退信记录 → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    'SC-3152': ('keep_C', '格鲁吉亚 GSC（gsc.ge / gsc.com.ge 均正常；gassiev.d@ 具名；video converter；两手机都加不上）：本职线 VC → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3153': ('keep_C', 'MIS Group（misgroup.co.za；国别未填 → 南非；kersagan@ 具名；「need detailed info about VC，main biz CCTV」）：本职线 VC + 南非先例 → 留 C + dayjob_fit（交换机线可顺带一页纸）', ['dayjob_fit']),
    'SC-3154': ('keep_C', '新加坡 Starview International（starviewint.com / .net 均正常；Chan Hong Kek 具名；比较多无源产品 / PoE 配件 / MC；17 推 0 回；stop）：本职线无源 / MC + 零回应 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3157': ('keep_C', '秘鲁 GM Industries SAC（gm-industry.com no_mx；两地址都 fail；「光端机，想做代理」西语询盘）：本职线 光端机 + 退信 no_mx → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    'SC-3161': ('keep_C', '印度 Cube Telecom（cubetelecom.com / .net 均正常；退信 ×2；百通 + 光产品）：本职线 光产品 + 退信 → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    'SC-3163': ('keep_C', '台湾 Fibertronic（fibertronic.com 域正常；roy@ 具名；没有工业品、很多无源 / MC / HDMI / SDI；stop）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3178': ('keep_C', '印度 Mahalasa Enterprises（mahalasaent.com 域正常；退信 prakashv@；Bypass networking）：本职线 bypass + 退信 → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    'SC-3197': ('keep_C', '以色列 RBS Telecom（rbs-telecom.com 域正常；退信 info@，aviv@ 具名；fiber tap；分销商 catalog 很多牌子；微信已加国内分公司对接人）：分销 ✔ 但以色列非点名国 + fiber tap 本职线；微信路径在 → 留 C + dayjob_fit（本职线索；交换机线顺带）', ['dayjob_fit']),
    'SC-3217': ('keep_C', '马来西亚 Soul Communication（soulcommunication.com.my 域正常；退信 asrul@；VC 在用北京 HCSTCOM 家的）：本职线 VC + 退信 → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    'SC-3298': ('keep_C', '印度 Netro Networks（netronetworks.in 域正常；vipin.chauhan@ 具名；MC / SFP 无源，主要 SFP；Simon 标 Spam；stop）：本职线 SFP → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3299': ('keep_C', '巴基斯坦 RT Automation（rtautomation.pk nxdomain，无退信记录；MC / VC 周边无源，有 Versitron / 深圳 Beyond 的；stop）：本职线 + 域死无退信 → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    # ---- 退信但域名正常 → 留 C 待巡检 ----
    'SC-3138': ('keep_C', '菲律宾 Expose（expose.ph dead / pic-expose.ph 正常；退信 sales@expose.ph；Dahua；备注 fail）：备用域在 → 留 C 待巡检（换 pic-expose.ph 地址）', []),
    'SC-3155': ('keep_C', 'UE IT（ue-it.de 域正常；表内国别未填 → .de 德国主区 → 国别待核；退信 info@；Peplink 的）：德国主区 ✔ 但 Peplink = 路由 / SD-WAN 分销（交换机对位一般）+ 退信 → 留 C 待巡检（核实国别 + 找新地址后复看）', []),
    'SC-3159': ('keep_C', '智利 Acanto（acanto.io 域正常；退信 sales.cl@；「云 telecommunications」）：品类偏 + 退信 → 留 C 待巡检', []),
    'SC-3160': ('keep_C', '巴拿马 Alpha Telecom（alphatelecomsa.com nxdomain / alphatelecom.cc 正常；退信 info@alphatelecom.cc；无兴趣记录）：退信 + 无信息 → 留 C 待巡检', []),
    'SC-3166': ('keep_C', '巴西 Mundifibra（mundifibra.com.br 域正常；退信 orcamento@；「和之前客户 flexmedia 产线很相似」= 光纤产品线；官网 WA +55 11 98488-0868）：WA 路径在 → 留 C 待巡检（试加 WA 后复看）', []),
    'SC-3186': ('keep_C', '沙特 Tele Networks International（telenetworksintl.com 域正常；退信 prasanth@；voice / data）：退信 + 对位弱 → 留 C 待巡检', []),
    'SC-3224': ('keep_C', '格鲁吉亚 Innotech（innotech.ge 域正常；退信 info@ / sales@；CCTV 大华几个型号）：CCTV 店 + 退信 + 非点名国 → 留 C 待巡检', []),
    'SC-3226': ('keep_C', '格鲁吉亚 Optimum（optimum.ge 域正常；退信 info@；CCTV + Planet 几个型号 = 台湾品牌 ✔）：退信 + 非点名国 → 留 C 待巡检（通了复看）', []),
    'SC-3230': ('keep_C', '尼泊尔 Himhippo（himhippo.com 域正常；退信 info@；Telecom 项目商）：退信 + 非点名国 → 留 C 待巡检', []),
    'SC-3246': ('keep_C', '巴西 JM Tell（jmtell.com.br 域正常；退信 sac@；CCTV 相关）：退信 + CCTV 店 → 留 C 待巡检', []),
    'SC-3252': ('keep_C', '南非 Devtel（devtel.co.za 域正常；退信 info@；Fiber / CCTV 方案商）：南非先例 ✔ 但退信 + 无品牌证据 → 留 C 待巡检（通了复看）', []),
    'SC-3265': ('keep_C', '俄罗斯 Intecs（intecs.ru 域正常；退信 avi@；两座机加不上；问带报警抓拍的 camera）：CCTV 需求非 Saga 线 + 退信 → 留 C', []),
    'SC-3269': ('keep_C', '印度 iVision India（ivisionindia.co.in 域正常；退信；主要 CCTV + 少量商业 PoE；Simon 标 Spam；stop）：退信 + CCTV 店 → 留 C 待巡检' + VETO, []),
    'SC-3295': ('keep_C', '韩国 Linknzone（linknzone.com 域正常；退信 sales@；「network，信息很模糊」；stop）：退信 + 信息不足 → 留 C 待巡检', []),
    # ---- 其他留 C ----
    'SC-3150': ('keep_C', '俄罗斯 SAB（spektr-sab.ru nxdomain，无退信记录；chief@；贸易商卖摄像头 / 门禁；WA 加不上）：域死无退信 → 留 C 待巡检（下次巡检仍死即 pass）', []),
    'SC-3162': ('keep_C', '马来西亚 Cynics（cynics.com.my 域正常；info@ / sales@；工业 FS / PoE / CCTV 为主，有 Utepo 的 = 中国品牌 ✔；stop；0 推）：进口中国同类 ✔ 但马来西亚无先例 + 零互动 → 留 C（储备；一页纸一次后看）', []),
    'SC-3239': ('keep_C', '巴西 Portwell（portwell.com.br 域正常；flavio@ 具名；工业 FS / MC 机架式；官网 WA 按钮；Simon 标 Spam；stop）：对位 ✔ 但品牌未点名 + 巴西需全线专业分销先例 → 留 C（试加 WA 后复看）' + VETO, []),
}


def main():
    assert len(CODES) == 47 and len(set(CODES)) == 47
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
    L = [f'# C 池 · 闸 1 · 第 34 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 1211–1257 户（{len(V)} 户）—— 桶 ⑥ 收口', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：「用户判定不行」42 / 47 + 守界乌克兰 3 + 巨头 2（Datacom BR 同行制造、ATC 科威特）；退信 26、Simon 标「Spam / stop」14（我方备注，非客户要求停发 → 不作 pass 依据）。口径同桶 ⑥ 首批 + 第 33 批收紧（退信 + no_mx 留 C 待巡检）。'
         ' 候选 3 = TVC（MX，Utepo / 大华大分销，墨西哥先例 SYSCOM）/ Starcom（PK，Raisecom 采购 + 2026-02 真人回「请用公司域名邮箱发」）/ Techroutes（IN，两位具名 KP + 手机；Simon 标 Spam → 可否决）。'
         ' 永久 pass 0：Premua（乌克兰；退信 + nxdomain）按「乌克兰一律守界不永久 pass」留 C。值得巡检后转候选：WAGO India（Volktek 工业交换机；换 wago.com 域）、Motherwell Automation AU（迈威工业 FS；找新域名）、Smartnet IN、Optimum GE（Planet 型号）。'
         ' 国别待核：ue-it.de（表内未填 → 德国主区，Peplink 分销）、misgroup.co.za（→ 南非）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批34_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
