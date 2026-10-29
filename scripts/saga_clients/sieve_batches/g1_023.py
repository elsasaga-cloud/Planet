#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 23 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 606–660 户（按综合分序，SC-1342 … SC-1402）。

构成：印度 0 触达冷名单（约 30 户）、孟加拉 / 巴基斯坦 / 尼日利亚 / 摩洛哥 / 肯尼亚 / 喀麦隆 / 马尔代夫零星、俄罗斯 / 越南光模块户、巴西 2 户、南非 4 户、突尼斯 / 亚美尼亚 / 印尼各 1。
  · 口径同桶 ⑥ 首批 + 补充（印度：分销 / 集成 / 自有品牌主体 + 中国 / 台湾品牌证据 → 闸 2 低优先；「想拿样」= 真意向 → 闸 2；仅有名牌 / 无品牌证据 / 网店 / 终端留 C）。
  · 候选 6 = Excell Media IN（从 Volktek 买 2 光 8 管理）/ Globus Infocom IN（自有品牌 AV / 安防，Ashish@ 具名 → oem_target）/ Masibus IN（工业仪表自有品牌，三旺 + IO 比较专业 → oem_target）/ Mayenet IN（要商业级全千兆、想拿样 = 真意向）/ Mywatchdog IN（AOA · 洪瑞 · 丰润达都有 → Q-33）/ Parks BR（巴西自有品牌电信设备，WDM switch 用桂林的 → oem_target）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：印度无品牌证据 / 名牌 / 终端 / 网店（Eurotech AV · Futuregate 名牌 · Golf Automation · Immunity · Kothari · Modii · Multybyte · Panabyte · SA Electro · Securus · SISL · Telenet · Tenet · Theta · Fortune IT 新桥 · Javi Cisco + 少量国内 · Pyrotech ONV 商用 · Team5 10Gtek 光模块 · Smartlink BTON 站挂）/ 突尼斯 Faze（21 台 2 光 8 管理但要 MPLS = 不供，非点名国 → 储备）/ 巴西 FiberX（华为 DWDM）/ 南非（RJ Connect Moxa · Gensix · iDevices · Primus 线缆）/ 亚美尼亚 Medisar Utepo / 印尼 Sejahtera Mandiri Utepo 类目 / 俄罗斯 · 越南光模块（kdds · netstore · orbiss · hcomvn · one.com.vn · optomind）/ 孟加拉 · 巴基斯坦 · 尼日利亚 · 摩洛哥 · 肯尼亚 · 喀麦隆 · 马尔代夫 0 触达 / 死域名待巡检（khenterprise no_mx · servo.ng nxdomain · mayenetsolutions nxdomain 已换 mayenet.com）/ 国别存疑（onlinecamerashop.nl 表内尼泊尔、.nl 域）/ 本职线 dayjob_fit（DWDM · WDM · 光模块）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_023.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批23_2026-10-29.md）
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

BATCH = 'G1-23'
DATE = '2026-10-29'
CODES = ["SC-1342", "SC-1343", "SC-1344", "SC-1345", "SC-1346", "SC-1348", "SC-1349", "SC-1350", "SC-1351", "SC-1352", "SC-1353", "SC-1354", "SC-1355", "SC-1356", "SC-1357", "SC-1359", "SC-1360", "SC-1361", "SC-1362", "SC-1363", "SC-1364", "SC-1365", "SC-1366", "SC-1367", "SC-1368", "SC-1369", "SC-1370", "SC-1371", "SC-1372", "SC-1373", "SC-1374", "SC-1375", "SC-1376", "SC-1377", "SC-1378", "SC-1379", "SC-1380", "SC-1381", "SC-1382", "SC-1383", "SC-1385", "SC-1386", "SC-1387", "SC-1388", "SC-1389", "SC-1390", "SC-1391", "SC-1392", "SC-1394", "SC-1396", "SC-1398", "SC-1399", "SC-1400", "SC-1401", "SC-1402"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1344': ('candidate', '印度 Excell Media（excellmedia.net；从 Volktek 买 2 光 8 管理）：进口台湾同类 ✔ 对位 ✔（STC-228GP 同口型）Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1352': ('candidate', '印度 Globus Infocom（globusinfocom.com；自有品牌 AV / 安防，工业 FS；Ashish@ 具名在表）：自有品牌 = OEM 对象 ✔ 对位 ✔ 具名 KP ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', ['oem_target']),
    'SC-1365': ('candidate', '印度 Masibus（masibus.com；工业仪表 / 控制自有品牌，三旺 + IO「比较专业」；邮件中有详细联系信息）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔；未触达 → 闸 2 查底数（zaubacorp）；低优先', ['oem_target']),
    'SC-1366': ('candidate', '印度 Mayenet Solutions（mayenetsolutions.com 域 nxdomain；mayenet.com 正常；「不太要工业级，要商业级全千兆不要混合速率，想拿样」）：真意向 + 样品 ✔ 对位 ✔（STC-2224GP 全千兆）Simon 点名印度 → 闸 2 查底数 + 换 mayenet.com 地址；低优先', []),
    'SC-1371': ('candidate', '印度 Mywatchdog（mywatchdog.in；工业交换机页 AOA / 洪瑞 / 丰润达都有 = 多牌进口 + 洪瑞现供）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先' + Q33, []),
    'SC-1379': ('candidate', '巴西 Parks（parks.com.br；巴西自有品牌电信设备商，WDM switch 用的桂林的 = 中国代工；电话在表）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔ + 本职线 WDM；未触达 → 闸 2 查底数（cnpj.biz）；拉美非点名国，低优先', ['oem_target', 'dayjob_fit']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1346': ('keep_C', '突尼斯 Faze（faze.tn；「21 个 2 光 8 PoE 管理，需支持 MPLS」）：数量 ✔ 但 MPLS Saga 不供 + 非点名国 + 零推送 → 留 C（储备；回信即候选）', []),
    'SC-1349': ('keep_C', '印度 Fortune IT（fortune-it.com；新桥的商业 PoE）：进口中国同类 ✔ 但主体规模不明 + 零互动 → 留 C（储备）', []),
    'SC-1359': ('keep_C', '印度 Javi Systems（javisystems.com；Cisco 产品 + 从国内买一些 switch）：名牌为主 + 零互动 → 留 C（储备）', []),
    'SC-1361': ('keep_C', '孟加拉 KH Enterprise（khenterprise.com.bd 域 no_mx，无退信；CCTV 为主）：死域名 → 留 C 待巡检', []),
    'SC-1367': ('keep_C', '亚美尼亚 Medisar（medisar.am；有 Utepo 的）：进口中国同类 ✔ 但非点名国；推 1 次 0 回 → 留 C（储备）', []),
    'SC-1374': ('keep_C', 'onlinecamerashop.nl（表内国别尼泊尔、.nl 域 = 疑荷兰网店；SFP / VC / FS 周边）：国别存疑 + 网店 → 留 C 待核 + dayjob_fit', ['dayjob_fit']),
    'SC-1382': ('keep_C', '印度 Pyrotech（pyrotechindia.com；工业控制盘厂，在卖 ONV 的商业 PoE）：进口中国同类 ✔ 但主业非网络 + 零互动 → 留 C（储备）', []),
    'SC-1383': ('keep_C', '南非 RJ Connect（rjconnect.co.za；工业通讯，主要是 Moxa 的）：Moxa 专营 + 零互动 → 留 C', []),
    'SC-1390': ('keep_C', '印尼 Sejahtera Mandiri（sejahteramandiri.com；有单独的 Utepo 类目）：进口中国同类 ✔ 但四主区外非点名国；推 1 次 0 回 → 留 C（储备）', []),
    'SC-1391': ('keep_C', '尼日利亚 Servo（servo.ng 域 nxdomain；servodirect.com 正常；CCTV 为主）：主域死 → 留 C 待巡检', []),
    'SC-1396': ('keep_C', '印度 Smartlink（smartlink.co.in；BTON；网站打不开、邮箱 OK）：站挂无退信 → 留 C 待巡检', []),
    'SC-1399': ('keep_C', '印度 Team5 Tech（team5tech.com；从 10Gtek 买东西 = 光模块 / DAC）：本职线进口 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 23 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 606–660 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：印度 0 触达约 30 户、南亚 / 非洲零星、俄罗斯 / 越南光模块户、巴西 2 户、南非 4 户。口径同桶 ⑥ 首批 + 补充（印度：分销 / 集成 / 自有品牌主体 + 中国 / 台湾品牌证据 → 闸 2 低优先；「想拿样」= 真意向 → 闸 2）。候选 6 = Excell Media（IN，Volktek 2 光 8）/ Globus Infocom（IN 自有品牌）/ Masibus（IN 自有品牌 + 三旺）/ Mayenet（IN 想拿样）/ Mywatchdog（IN 多牌 + 洪瑞 Q-33）/ Parks（BR 自有品牌，桂林 WDM）；永久 pass 0。留 C：印度无品牌证据 / 名牌 / 终端 / 网店、突尼斯 Faze（21 台但要 MPLS）、南非 Moxa 专营等、俄 / 越光模块、南亚 / 非洲 0 触达、死域名待巡检、国别存疑（onlinecamerashop.nl）、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批23_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
