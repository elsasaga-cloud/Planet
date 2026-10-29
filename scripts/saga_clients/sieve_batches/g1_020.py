#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 20 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 441–495 户（按综合分序，SC-1024 … SC-1164）。

构成：台湾工业网络厂与贴牌商（群发 8–19 次 0 回）、俄罗斯 WDM / DCI 户（本职线）、乌克兰 5 户（守界）、拉美推 1 次 0 回户、韩 / 日 / 马 / 伊朗 / 非洲零星、2 个无域名邮箱（电商平台 / 比价站）。
  · 口径同桶 ⑥ 首批 + 补充（自有品牌 / 贴牌 = OEM 品牌商不限国别 → 闸 2 低优先；纯平台 / 比价站非买家零互动 → 永久 pass）。
  · 候选 5 = Xentino TW（ONV 换标 = 贴牌自有品牌）/ XP Networks TW（ONV 换标 = 贴牌自有品牌）/ Teltex BR（摄像头厂要 PoE 配套，发过价格表 → oem_target）/ Aditya Group IN（Utepo，点名印度）/ SYSCOM MX（拉美大安防分销，Hasivo 工业 FS，长线）→ 闸 2 查底数。
  · 永久 pass 2：SC-1082 information@corp.auction.co.kr（韩国电商平台 Auction 公司邮箱，非买家、零互动）、SC-1110 sales@pricecheck.co.za（南非比价站，非买家、零互动）。
  · 其余留 C：台湾同行 / 巨头（ORing · Accton · WNC · Shidatech · Netzin · Yoda · Atrie · CNJT · Formerica · Hobbes）/ 台湾进口中国牌但非贴牌（Dawnray 宇航）/ 韩日巨头与分销（LS Cable · Hytec Inter · Servants · Optowiz）/ 俄罗斯本职线 WDM / DCI（advc · hdwdm no_mx · prointech · rotek · T8）/ 俄罗斯 TPZ（自研外壳疑似同行）/ 乌克兰守界（Alfa-Metronik ORing · Insolutions · Tiacom · Dimiks 中科德能）/ 拉美推 1 次 0 回储备（Corporation IT EC · Laumayer EC 宇航 · Inroi · FlexDSL · PS Data · WEG 巨头）/ 非洲与中东互动户（ATCS 科特迪瓦 展会满意 · Icronum 坦桑 MC 10 个 WA 未回 · Helptech 伊拉克 ONV）/ 伊朗洪瑞现供（Rash System · Rundeman → Q-33，非点名国 + 制裁）/ 政府终端（菲律宾 DICT）/ 太阳能终端（Flo Energy）/ 国别未填待核（gdss-dz nxdomain · kodicam · oreind.is hasivo）/ 本职线 dayjob_fit。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_020.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批20_2026-10-29.md）
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

BATCH = 'G1-20'
DATE = '2026-10-29'
CODES = ["SC-1024", "SC-1029", "SC-1032", "SC-1035", "SC-1038", "SC-1040", "SC-1042", "SC-1043", "SC-1044", "SC-1056", "SC-1057", "SC-1059", "SC-1071", "SC-1078", "SC-1079", "SC-1082", "SC-1083", "SC-1084", "SC-1085", "SC-1090", "SC-1092", "SC-1096", "SC-1102", "SC-1106", "SC-1108", "SC-1109", "SC-1110", "SC-1112", "SC-1117", "SC-1118", "SC-1123", "SC-1124", "SC-1130", "SC-1131", "SC-1134", "SC-1135", "SC-261", "SC-1138", "SC-1140", "SC-1142", "SC-1147", "SC-1149", "SC-1150", "SC-1151", "SC-1152", "SC-1153", "SC-1154", "SC-1155", "SC-1156", "SC-1157", "SC-1159", "SC-1161", "SC-1162", "SC-1163", "SC-1164"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-1082': ('pass_final', '韩国 information@corp.auction.co.kr（电商平台 Auction / Gmarket 公司邮箱，无域名、无网站对应；表内「redlion 的 switch」= 平台商品抓取）非买家、零互动 → 纯无关非买家，永久 pass', []),
    'SC-1110': ('pass_final', '南非 sales@pricecheck.co.za（比价网站 PriceCheck，无域名对应；表内「有 Utepo 的」= 站内商品抓取）非买家；群发 5 次 0 回 → 纯无关非买家，永久 pass', []),
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1029': ('candidate', '台湾 Xentino（xentino.com；工业 FS / SFP，表内「用的 ONV 的，就换了个标」= 贴牌自有品牌）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔；群发 8 次 0 回 → 闸 2 查底数（twincn）；四主区外，低优先', ['oem_target']),
    'SC-1038': ('candidate', '巴西 Teltex（teltex.com.br；做摄像头的，要用到 PoE，价格表已发）：自有品牌摄像头 = OEM 对象 ✔ 对位 ✔ 有互动 ✔；推 1 次 0 回 → 闸 2 查底数（cnpj.biz）；拉美非点名国，低优先', ['oem_target']),
    'SC-1042': ('candidate', '印度 Aditya Group（adityagroup.com；Utepo）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1117': ('candidate', '墨西哥 SYSCOM（syscom.mx；拉美大型安防 / 网络分销，Hasivo 的工业 FS）：进口中国同类 ✔ 对位 ✔ 大分销主体；推 1 次 0 回 → 闸 2 查底数（D&B）；拉美非点名国，长线低优先', []),
    'SC-1134': ('candidate', '台湾 XP Networks（xp-networks.com；工业 FS / MC / SFP 产品线很相似，表内「用的 ONV 的，就换了个标」= 贴牌自有品牌）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔；群发 17 次 0 回 → 闸 2 查底数（twincn）；四主区外，低优先', ['oem_target']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1024': ('keep_C', '台湾 ORing（oringnet.com；工业网络厂商）：台湾同行；群发 8 次 0 回 → 留 C', []),
    'SC-1032': ('keep_C', '科特迪瓦 ATCS（atcs-ci.com；做项目的，展会着重看了 2 光 8 傻瓜式、满意拍照、说展后详谈；WA 加不上）：真互动 ✔ 但非点名国 + 群发 15 次 0 回 → 留 C（储备；回信即候选）', []),
    'SC-1035': ('keep_C', '韩国 LS Cable & System（lscns.com；线缆巨头；KP JeongSang Oh）：巨头体系；群发 37 次 0 回 → 留 C', []),
    'SC-1040': ('keep_C', '台湾 Accton（accton.com；网络 ODM 巨头，Marvell 方案核心交换机）：同行巨头；群发 18 次 0 回 → 留 C', []),
    'SC-1059': ('keep_C', '台湾 Dawnray（dawnraytech.com.tw；DAC / AOC / 跳线无源为主 + 宇航的工业 FS 很多）：进口中国同类 ✔ 但非贴牌 + 四主区外非点名国；群发 19 次 0 回 → 留 C（储备）', []),
    'SC-1079': ('keep_C', '坦桑尼亚 Icronum（icronum.com；「MC 10 个」小量询盘；WA 已加未回）：小量 + 非点名国；群发 15 次 0 回 → 留 C', []),
    'SC-1090': ('keep_C', '厄瓜多尔 Laumayer（laumayer.com；宇航的工业 FS + D-Link SFP）：进口中国同类 ✔ 但拉美非点名国；推 1 次 0 回 → 留 C（储备）', []),
    'SC-1124': ('keep_C', '俄罗斯 TPZ（tpz.ru；bypass / MC / switch，「跟过，自己的外壳比较独特」）：自研外壳疑似同行 + bypass Saga 不供 → 留 C（闸 2 轮空；若查实为贴牌可升）', []),
    'SC-1130': ('keep_C', '巴西 WEG（weg.net；电机 / 自动化巨头）：巨头体系；推 1 次 0 回 → 留 C', []),
    'SC-1131': ('keep_C', '台湾 WNC 启碁（wnc.com.tw；ODM 巨头，2.5G switch 大口）：同行巨头 + 2.5G 口径待定；群发 18 次 0 回 → 留 C', []),
    'SC-261': ('keep_C', '乌克兰 Dimiks（dimiks.com / dimiks.ua；中科德能工业 FS + 光路 OEO + 外购 10G 收发器）：进口中国同类 ✔ 但乌克兰 = 守界（难，非永久 pass）；群发 23 次 0 回 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1138': ('keep_C', '菲律宾 DICT（dict.gov.ph；政府信息通信部，L3 DC 交换机；WA 加不上）：政府终端 + 非点名国 → 留 C', []),
    'SC-1140': ('keep_C', '新加坡 Flo Energy（floenergy.sg；太阳能公司，要 LinkedIn 发 case study）：终端 + 非对位主业；群发 7 次 0 回 → 留 C', []),
    'SC-1153': ('keep_C', 'gdss-dz.com（国别未填，域 nxdomain 无退信；工业级交换机）：死域名 + 国别未填 → 留 C 待巡检', []),
    'SC-1156': ('keep_C', '日本 Hytec Inter（hytec.co.jp；工业网络分销，工业 FS / PoE 比较多的牌子）：分销主体但无中国品牌证据 + 非点名国；群发 12 次 0 回 → 留 C（储备）', []),
    'SC-1161': ('keep_C', 'oreind.is（国别未填，.is 域；switch 等有 hasivo 的）：进口中国同类 ✔ 但国别未核 → 留 C 待核', []),
    'SC-1162': ('keep_C', '伊朗 Rash System（rashsystem.com；卖很多鸿瑞的产品 = 洪瑞现供）：非点名国 + 制裁风险；推 1 次 0 回 → 留 C' + Q33, []),
    'SC-1163': ('keep_C', '伊朗 Rundeman（rundeman.com；全线洪瑞，小杂货铺；网站有 WA）：非点名国 + 制裁风险 + 小店 → 留 C' + Q33, []),
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
    L = [f'# C 池 · 闸 1 · 第 20 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 441–495 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：台湾工业网络厂与贴牌商、俄罗斯 WDM / DCI 本职线户、乌克兰 5 户守界、拉美推 1 次 0 回户、韩 / 日 / 马 / 伊朗 / 非洲零星、2 个无域名平台邮箱。口径同桶 ⑥ 首批 + 补充（贴牌 = OEM 品牌商不限国别 → 闸 2；纯平台 / 比价站非买家零互动 → 永久 pass）。候选 5 = Xentino / XP Networks（TW，ONV 换标贴牌）/ Teltex（BR 摄像头厂，发过价格表）/ Aditya Group（IN，Utepo）/ SYSCOM（MX 大分销，Hasivo）；永久 pass 2 = auction.co.kr 平台邮箱 / pricecheck.co.za 比价站。留 C：台湾同行与巨头、韩日巨头与分销、俄罗斯本职线、乌克兰守界、拉美储备、非洲 / 中东互动户（ATCS 展会满意）、伊朗洪瑞现供（Q-33）、政府 / 太阳能终端、国别未填待核、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批20_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
