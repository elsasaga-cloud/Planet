#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 24 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 661–715 户（按综合分序，SC-1403 … SC-1495）。

构成：WDM / CWDM / bypass 本职线户（约 20 户：港 / 韩 / 澳 / 以 / 新 / 日）、印度 0 触达、俄罗斯 0 触达与退信户、越南推 8 次 0 回户、拉美推 1 次 0 回户、澳大利亚国防 / 马来西亚超市终端。
  · 口径同桶 ⑥ 首批（本职线 → 留 C + dayjob_fit；退信无品牌证据 → 留 C；自有品牌 + 进口中国同类 → 闸 2）。
  · 候选 2 = Triflex Info IN（从国内买 MC / PoE switch，点名印度）/ DSSL RU（TRASSIR 自有品牌安防大厂，很多朱姐客户的型号 → oem_target）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：本职线 WDM / CWDM / bypass / 光开关（Ausoptic · Canare · Comworth · Conetcn · Coweaver · eWave · Fiber-Mart · HJH 华为中兴 · Mediatech · MGAnet · Neon no_mx · PacketLight 同行 · Testmation · Titan ICT · Traxcomm · Upcom · Wayoptics · Zenya · Adcomtec · Bouz · Citraweb · Echola）/ 退信户（Xeronvision SG ONV · Cantonkcam RU · Dotcom-sys SA Planet → 无换址证据先留）/ 印度（ULEPL · Vays DC · WIS · NetSys WA 已加未回 16 推 → 回信即候选）/ 越南推 8 次 0 回（Datacom Quoc Te nufiber · GNSVN · Oritech · vncc）/ 拉美（Comred PE 直接要 PI 比价 · Comtelec EC AOA MC）/ 斯里兰卡 Rovidu Elink / 乌克兰守界（IC-Line）/ 澳大利亚国防 AMWC（守界军工）/ 马来西亚 Mydin（超市终端 no_mx）/ 俄罗斯 0 触达（akon nxdomain 待巡检 · b2b-services · Compel 元器件巨头 · Dart · Energoprime）/ 蒙古 Cybercom / 以色列 / 阿联酋 CCTV 方案商（CMPS · Shamrad · Fyber · Vostok VC）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_024.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批24_2026-10-29.md）
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

BATCH = 'G1-24'
DATE = '2026-10-29'
CODES = ["SC-1403", "SC-1404", "SC-1406", "SC-1407", "SC-1408", "SC-1409", "SC-1216", "SC-1420", "SC-1421", "SC-1424", "SC-1425", "SC-1429", "SC-1430", "SC-1431", "SC-1432", "SC-1433", "SC-1435", "SC-1436", "SC-1437", "SC-1439", "SC-1441", "SC-1442", "SC-1447", "SC-1448", "SC-1449", "SC-1451", "SC-1452", "SC-1455", "SC-1456", "SC-1457", "SC-1458", "SC-1459", "SC-1460", "SC-1465", "SC-1259", "SC-1269", "SC-1466", "SC-1467", "SC-1472", "SC-1473", "SC-1474", "SC-1478", "SC-1479", "SC-1480", "SC-1481", "SC-1482", "SC-1483", "SC-1484", "SC-1485", "SC-1486", "SC-1487", "SC-1488", "SC-1492", "SC-1494", "SC-1495"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1403': ('candidate', '印度 Triflex Info（triflexinfo.com；从国内买 MC / PoE switch）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1492': ('candidate', '俄罗斯 DSSL（dssl.ru；TRASSIR 自有品牌安防大厂，表内「很多朱姐客户的型号，很多牌子的」）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['oem_target']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1409': ('keep_C', '新加坡 Xeronvision（xeronvision.com；退信，域正常；CCTV 有 ONV 的 MC / switch）：退信 + 非点名国 + 无换址线索 → 留 C（待巡检）', []),
    'SC-1425': ('keep_C', '俄罗斯 Cantonkcam（cantonkcam.ru；退信，域正常；CCTV 商业 PoE）：退信 + 无品牌证据；群发 17 次 0 回 → 留 C（待巡检）', []),
    'SC-1433': ('keep_C', '沙特 Dotcom Systems（dotcom-sys.com；退信，域正常；基本都是 Planet 的）：Planet 渠道 ✔ 但退信 + 非点名国；群发 7 次 0 回 → 留 C（待巡检）', []),
    'SC-1451': ('keep_C', '以色列 PacketLight（packetlight.com；WDM 设备厂商）：本职线同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1466': ('keep_C', '澳大利亚 AMWC（defence.gov.au；国防部门，Optimal 的客户；WA 加不上）：军工 = 守界（INH）→ 留 C（不主动碰）', []),
    'SC-1472': ('keep_C', '马来西亚 Mydin Mohamed Holdings（mydin.com.my 域 no_mx；mydin.com 正常；连锁超市，搞 CCTV 自用，似乎想要 CCTV 配件）：终端 + 主域无 MX → 留 C', []),
    'SC-1473': ('keep_C', '印度 NetSys Network / Indian Network Co（idnetsys.com；网络交换机好多是牌子的 + SFP；Murari@ 具名；WA 已加未回）：WA 在 ✔ 具名 ✔ 但群发 16 次 0 回 + 无中国品牌证据 → 留 C（回信即候选）', []),
    'SC-1479': ('keep_C', '俄罗斯 akon.com.ru（域 nxdomain；「发送失败」）：死域名 → 留 C 待巡检', []),
    'SC-1484': ('keep_C', '俄罗斯 Compel（compel.ru；元器件分销巨头）：巨头体系 → 留 C', []),
    'SC-1485': ('keep_C', '秘鲁 Comred（comred.pe；SFP 模块 Cisco；「直接让做 PI，应该是在比价格，后续无回复」）：比价客 + 拉美非点名国 → 留 C', []),
    'SC-1486': ('keep_C', '厄瓜多尔 Comtelec（comtelec.com；从 AOA 买 MC）：进口中国同类 ✔ 但拉美非点名国；推 1 次 0 回 → 留 C（储备）', []),
    'SC-1259': ('keep_C', '越南 Datacom Quốc Tế（datacomquocte.com；VC / MC / SFP，很多都是 nufiber（深圳）的）：进口中国同类 ✔ 但四主区外非点名国；群发 8 次 0 回 → 留 C（储备）+ dayjob_fit', ['dayjob_fit']),
    'SC-1442': ('keep_C', '乌克兰 IC-Line（ic-line.ua；switch / MC / SFP）：乌克兰 = 守界（难，非永久 pass）；群发 14 次 0 回 → 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 24 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 661–715 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：WDM / CWDM / bypass 本职线户约 20 户、印度 0 触达、俄罗斯 0 触达与退信户、越南推 8 次 0 回、拉美推 1 次 0 回、澳大利亚国防 / 马来西亚超市终端。口径同桶 ⑥ 首批。候选 2 = Triflex Info（IN，从国内买 MC / PoE）/ DSSL（RU TRASSIR 自有品牌，朱姐客户型号）；永久 pass 0。留 C：本职线 dayjob_fit、退信无换址线索、印度无品牌证据（NetSys WA 在 → 回信即候选）、越南 / 拉美储备、乌克兰守界、军工守界（AMWC）、超市终端、俄罗斯巨头与死域名。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批24_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
