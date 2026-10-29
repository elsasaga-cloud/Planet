#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 25 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 716–770 户（按综合分序，SC-1496 … SC-1564）。

构成：俄罗斯 0 触达冷名单（约 33 户，多数备注空白）、越南 0 触达（约 10 户）、哈萨克 / 乌兹别克 / 白俄零星、WhatsApp 加不上的摩尔多瓦 / 南非 / 阿尔及利亚询价户、退信户 2、以色列军工级户。
  · 口径同桶 ⑥ 首批（俄语区：分销 / 集成 + 中国品牌证据 → 闸 2 低优先、收款待定；备注空白 / 名牌 / 周边 → 留 C；本职线 → dayjob_fit）。
  · 候选 4 = Manggis（.kz 域、表内俄罗斯 → 国别待核哈萨克；ONV + 海康为主）/ PLController RU（基本就是朱姐客户的牌子 = 中国工业交换机进口分销）/ Chiisa ZA（问过 4 光 8 工业大壳 = 真需求，WA 加不上）/ Nivetti Systems IN（印度自有品牌网络设备商 → oem_target）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：俄罗斯备注空白 / 名牌 / 周边 / 本土品牌（Interlogic .top 域 · i-sensor · icmicro 元器件 · idelectro · konnect-market · lambda-tdk · ledpremium · Morion WDM · msk.ru no_mx 华为思科 · mytel.pro 名牌 WDM · networktelecom · Sozvezdie 军工 = 守界 · on-com · onelec · PacketLight-Russia 域 dead · pairui · Powervideo 本土品牌 · redutsb · rs-catalog · scanstore · siptrade nsgate no_mx · skomplekt 周边 · sktech · smdx · teldis · ucord SFP · vikiwat · wehopower 电源 · west-l · zenonline）/ 越南（Fortel Ad-net · green-ias · Huviron 多牌 · iot-master · Jonjul · mangthanhcong · MCTT 三旺 JHA · namthanhcong NHM · thuviencokhi 三旺）/ 白俄 sfp.by 光模块 / 乌兹别克 Fortpro · Softcomtrade 布线 / 印尼 Rajanetwork CWDM · Javis 退信 丰润达 / 厄瓜多尔 Hentel Witek / 菲律宾 XBS 多牌 / 摩尔多瓦 DAAC（欧洲边缘大集成商，WA 加不上，无中国品牌证据 → 储备）/ 阿尔及利亚 Neobil 5 电口 / 退信 GIT Holding RU Utepo（无换址线索待巡检）/ 国别未填 Optronicsplus（MC 机架）/ 以色列 SDK Systems（军工级 FS，守界）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_025.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批25_2026-10-29.md）
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

BATCH = 'G1-25'
DATE = '2026-10-29'
CODES = ["SC-1496", "SC-1497", "SC-1498", "SC-1499", "SC-1500", "SC-1501", "SC-1502", "SC-1503", "SC-1506", "SC-1507", "SC-1508", "SC-1509", "SC-1510", "SC-1511", "SC-1513", "SC-1514", "SC-1515", "SC-1516", "SC-1517", "SC-1518", "SC-1519", "SC-1520", "SC-1521", "SC-1522", "SC-1523", "SC-1524", "SC-1525", "SC-1526", "SC-1527", "SC-1528", "SC-1529", "SC-1530", "SC-1531", "SC-1534", "SC-1535", "SC-1536", "SC-1537", "SC-1538", "SC-1540", "SC-1541", "SC-1542", "SC-1543", "SC-1544", "SC-1545", "SC-1547", "SC-1548", "SC-1549", "SC-1550", "SC-1551", "SC-1552", "SC-1553", "SC-1559", "SC-1561", "SC-1562", "SC-1564"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1513': ('candidate', 'Manggis（manggis.kz；表内国别「俄罗斯」、.kz 域 → 疑哈萨克，待核；主要是 ONV 和海康威视的产品）：进口中国同类 ✔ 对位 ✔ 哈萨克有先例；未触达 → 闸 2 查底数（statsnet / adata）并核国别；俄语区收款待定，低优先', []),
    'SC-1527': ('candidate', '俄罗斯 PLController（plcontroller.ru；「基本就是朱姐客户的牌子」= 中国工业交换机多牌进口分销）：进口中国同类 ✔ 对位 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-1552': ('candidate', '南非 Chiisa Groups（chiisa.com；问过「4 光 8 工业大壳」= 具体型号需求；WA 加不上）：真需求 ✔ 对位 ✔（STI-488DGGPM 同口型）南非有先例；→ 闸 2 查底数（D&B）+ 邮件路径；低优先', []),
    'SC-1521': ('candidate', '印度 Nivetti Systems（nivettisystems.com / .in；印度自有品牌网络设备商）：自有品牌 = OEM 对象 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', ['oem_target']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1506': ('keep_C', '俄罗斯 Interlogic（interlogic.top；从国内买一些 networking 设备）：.top 域主体不明 + 无品牌证据 + 零互动 → 留 C（储备）', []),
    'SC-1522': ('keep_C', '俄罗斯 Sozvezdie（oao-sozvezdie.ru；国防电子康采恩）：军工 = 守界 + 制裁风险 → 留 C（不主动碰）', []),
    'SC-1525': ('keep_C', '俄罗斯 PacketLight-Russia / Teleser（packetlight-russia.ru 域 dead；teleser.ru 正常；WDM DCI / SD-WAN）：本职线 + 主域死 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-1536': ('keep_C', '俄罗斯 Siptrade（siptrade.ru 域 no_mx；卖的基本都是 nsgate 的）：本土品牌专营 + 无 MX → 留 C 待巡检', []),
    'SC-1515': ('keep_C', '越南 MCTT（mctt.vn / mctt.com.vn；三旺 / JHA 产品比较多 + 串口 / 元器件）：进口中国同类 ✔ 但四主区外非点名国 + 零互动 → 留 C（储备）', []),
    'SC-1551': ('keep_C', '摩尔多瓦 DAAC System Integrator S.R.L.（daac-system.md；WEM / MC / 视频会议 / 监控 / 网安大集成商；WA 加不上）：欧洲边缘 + 无中国品牌证据 + 零互动 → 留 C（储备；回信即候选）', []),
    'SC-1553': ('keep_C', '阿尔及利亚 Neobil Computer Tech（neobil.com；问过 5 电口；WA 加不上）：微型需求 + 非点名国 → 留 C', []),
    'SC-1559': ('keep_C', '俄罗斯 GIT Holding（git-holding.ru；退信，域正常；工业 FS Utepo 的）：进口中国同类 ✔ 但退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-1561': ('keep_C', '印尼 Javis（javis.co.id；退信，域正常；买丰润达的商业 PoE）：进口中国同类 ✔ 但退信 + 四主区外非点名国 → 留 C 待巡检', []),
    'SC-1562': ('keep_C', 'Optronicsplus（optronicsplus.net；表内国别未填；MC / 14 槽机架 / 周边配件非常多）：国别待核 + 周边为主 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1564': ('keep_C', '以色列 SDK Systems（sdksys.com；军工级工业 FS，从 2 个印度厂商买；「big」flag）：军工 = 守界（INH）→ 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 25 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 716–770 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：俄罗斯 0 触达约 33 户（多数备注空白）、越南 0 触达约 10 户、哈萨克 / 乌兹别克 / 白俄零星、WA 加不上的询价户 3、退信户 2、以色列军工级户。口径同桶 ⑥ 首批。候选 4 = Manggis（.kz 国别待核，ONV + 海康）/ PLController（RU，朱姐客户的牌子）/ Chiisa（ZA，问过 4 光 8 工业大壳）/ Nivetti Systems（IN 自有品牌）；永久 pass 0。留 C：俄罗斯备注空白 / 名牌 / 周边 / 本土品牌 / 军工守界、越南储备、退信无换址线索、摩尔多瓦 DAAC 储备、本职线 dayjob_fit、国别未填。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批25_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
