#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 21 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 496–550 户（按综合分序，SC-1026 … SC-1274）。

构成：拉美 0 触达（约 12 户）、南亚 / 尼泊尔 / 斯里兰卡 / 巴基斯坦推 1–3 次 0 回户、埃及推 1 次 0 回户、澳大利亚平台商、韩国展商与分销、俄罗斯 17–18 推 0 回户、乌克兰 2 户 RFQ（守界）、中东零星、1 个平台邮箱。
  · 口径同桶 ⑥ 首批 + 补充（明确「不买中国的东西」= 婉拒 → 永久 pass；电商平台客服邮箱 = 非买家 → 永久 pass；想分销 / 想换供应商 = 真意向 → 闸 2）。
  · 候选 5 = Bolid RU（俄产安防大厂自有品牌，从 Elink 买 MC → oem_target）/ SDT KR（「想分销，认证是个麻烦事儿」= 真意向，KC 待议）/ CNG System KR（CENTEC Switch 意向，退信 → 换 dialogic.co.kr 地址）/ Lapis Technologies IN（Alcon 商业 PoE，点名印度）/ Avensia UAE（「想换供应商」，WA 已加未回）→ 闸 2 查底数。
  · 永久 pass 2：SC-1214 raredist.com（埃及分销，电话里「说不买中国的东西」= 明确婉拒）、SC-1270 hotro@tiki.vn（越南电商平台 Tiki 客服邮箱，非买家、零互动）。
  · 其余留 C：拉美储备（Flexport BR Atop + 常总的 · Airway PA 4 光 8 电 6 台 · Altus BR 自动化厂 · Directlink · Secoch · MPI ORing · Alastor · Unicorsa · Netsun · SAS Comm）/ 南亚储备（Microzone LK ONV · Techgates LK hasivo · Firstlink NP nclink · Tayabally PK 鸿瑞 → Q-33 · Terralink · NCS · Abhinawan · Sritech Red Lion · K15）/ 埃及推 1 次 0 回（EMIC · ESI · Peta）/ 澳大利亚平台（4Cabling · CPL · MSY · CSD 台湾牌分销 · EQL Planet · Ion）/ 韩国（Handreamnet 同行展商 · Fiberpia 平台 no_mx）/ 俄罗斯（2TEST 测试仪分销 · Emilink PON）/ 乌克兰守界 RFQ（bigmir 1V1D · co.site 无人机光纤）/ 中东（Al Mamaas 名牌 · Al Nabaa ONV · DNS BH GXCOM · Fiberway SA Planet · 伊朗 Baradinn / Easyertebat）/ 台湾 MITS（基本都是 ONV，非贴牌）/ 退信 + 域无 MX（netlink.tw 待巡检）/ 本职线 dayjob_fit。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_021.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批21_2026-10-29.md）
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

BATCH = 'G1-21'
DATE = '2026-10-29'
CODES = ["SC-1026", "SC-1172", "SC-1180", "SC-1182", "SC-1183", "SC-1186", "SC-1191", "SC-1193", "SC-1195", "SC-1196", "SC-1198", "SC-1199", "SC-1201", "SC-1202", "SC-1203", "SC-1206", "SC-1207", "SC-1209", "SC-1210", "SC-1211", "SC-1212", "SC-1214", "SC-1217", "SC-1218", "SC-1219", "SC-1222", "SC-1224", "SC-1225", "SC-1227", "SC-1233", "SC-1234", "SC-1239", "SC-1243", "SC-1246", "SC-1247", "SC-1248", "SC-1249", "SC-1250", "SC-1251", "SC-1253", "SC-1254", "SC-1255", "SC-1256", "SC-1260", "SC-1261", "SC-1262", "SC-1263", "SC-1264", "SC-1265", "SC-1266", "SC-1267", "SC-1270", "SC-1271", "SC-1273", "SC-1274"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-1214': ('pass_final', '埃及 Rare Dist（raredist.com；搞分销的，Planet MC / FS 都有；电话 +20 1030 800500 后备注「说不买中国的东西」= 明确婉拒中国货）；推 1 次 0 回 → 明确婉拒，永久 pass', []),
    'SC-1270': ('pass_final', '越南 hotro@tiki.vn（电商平台 Tiki 客服邮箱，无域名对应；表内「switch」= 平台商品抓取）非买家、零互动 → 纯无关非买家，永久 pass', []),
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1191': ('candidate', '韩国 CNG System（cngsystem.com 退信；dialogic.co.kr 正常；表内「CENTEC Switch」）：CENTEC 敲门砖 ✔ Simon 点名韩国；退信 ≠ 死 → 闸 2 查底数（bizno）+ 换 dialogic.co.kr 地址；低优先', []),
    'SC-1203': ('candidate', '印度 Lapis Technologies（lapistechnologies.in；商业 PoE Alcon 的）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1243': ('candidate', '韩国 SDT Inc（sdt.inc；表内「想分销，认证是个麻烦事儿」；电话在表未加）：真意向 ✔ Simon 点名韩国 ✔ 对位 ✔；KC 认证 Saga 无（只能走无需 KC 的工业 / B2B 场景）→ 闸 2 查底数（bizno）；低优先', []),
    'SC-1248': ('candidate', '阿联酋 Avensia UAE（avensiauae.com；表内「想换供应商」；WA 已加未回；avensiasuae.com 域 nxdomain）：真意向 ✔ 对位 ✔ WA 路径 ✔；推 1 次 0 回 → 闸 2 查底数（D&B）；四主区外，低优先', []),
    'SC-1251': ('candidate', '俄罗斯 Bolid（bolid.ru；俄产安防大厂自有品牌，表内「从 Elink 买 MC」）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔ Simon 点名俄罗斯；群发 17 次 0 回 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['oem_target']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1172': ('keep_C', '韩国 Handreamnet（handreamnet.com；交换机厂商，参展商；KP Pedro Joung）：韩国同行；群发 17 次 0 回 → 留 C', []),
    'SC-1182': ('keep_C', '巴拿马 Airway（airway.com；「4 光 8 电管理 6 个」小量询盘）：小量 + 拉美非点名国 + 零推送 → 留 C（储备；回信即候选）', []),
    'SC-1186': ('keep_C', '巴西 Altus（altus.com.br；PLC / 自动化厂商，工业 FS）：自动化厂商无进口证据 + 拉美非点名国 → 留 C', []),
    'SC-1199': ('keep_C', '巴西 Flexport（flexport.com.br；工业 FS Atop 的 + 常总的）：进口中国 / 台湾同类 ✔ 但拉美非点名国 + 零互动 → 留 C（储备；若点名巴西可升候选）', []),
    'SC-1210': ('keep_C', '台湾 Netlink（netlink.tw 域 no_mx；info / sales 均退信；看着像中科德能外壳）：退信 + 域无 MX → 留 C 待巡检（若确认无其他联系方式可转永久 pass）', []),
    'SC-1222': ('keep_C', '巴基斯坦 Tayabally（tayabally.com.pk；鸿瑞的 MC / 商业 FS / 工业 FS + Fierbit VC）：洪瑞现供 + 非点名国；推 1 次 0 回 → 留 C + dayjob_fit' + Q33, ['dayjob_fit']),
    'SC-1233': ('keep_C', '俄罗斯 2TEST（2test.ru；测试测量仪器分销，工业 FS / MC / SFP / 电源）：分销主体但无中国品牌证据；群发 18 次 0 回 → 留 C', []),
    'SC-1250': ('keep_C', '乌克兰 bigmir.net（阿里 RFQ「1V1D BIDI RS485」）：乌克兰 = 守界 + 本职线品类 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1254': ('keep_C', '乌克兰 co.site（阿里 RFQ「无人机光纤」）：乌克兰 = 守界 + 品类不供 → 留 C', []),
    'SC-1256': ('keep_C', '澳大利亚 CSD（csd.com.au；很多有名牌子 / 台湾牌子分销商）：进口台湾同类 ✔ 但四主区外非点名国 + 零互动 → 留 C（储备）', []),
    'SC-1266': ('keep_C', '韩国 Fiberpia（fiberpia.co.kr 域 no_mx；fiberpia.com 正常；CWDM SFP / MC / switch 销售平台）：平台 + 主域无 MX → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-1273': ('keep_C', '台湾 MITS Component（mitscomponent.com；基本都是 ONV 的）：进口中国同类 ✔ 但非贴牌转售 + 四主区外非点名国 → 留 C（储备）', []),
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
    L = [f'# C 池 · 闸 1 · 第 21 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 496–550 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：拉美 0 触达约 12 户、南亚 / 埃及推 1–3 次 0 回户、澳大利亚平台商、韩国展商与分销、俄罗斯 17–18 推 0 回户、乌克兰 RFQ 2 户守界、中东零星、1 个平台邮箱。口径同桶 ⑥ 首批 + 补充（「不买中国的东西」= 婉拒 → 永久 pass；平台客服邮箱 → 永久 pass；想分销 / 想换供应商 = 真意向 → 闸 2）。候选 5 = Bolid（RU 自有品牌，Elink MC）/ SDT（KR 想分销）/ CNG System（KR CENTEC 意向，退信换址）/ Lapis（IN，Alcon）/ Avensia（UAE 想换供应商）；永久 pass 2 = raredist.com（明确不买中国货）/ hotro@tiki.vn（平台客服）。留 C：拉美 / 南亚 / 埃及储备、澳大利亚平台、韩国同行与平台、俄罗斯无品牌证据、乌克兰守界、中东名牌与 ONV 小户、台湾 ONV 转售、退信 + 域无 MX 待巡检、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批21_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
