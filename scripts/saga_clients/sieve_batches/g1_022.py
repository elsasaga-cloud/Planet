#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 22 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 551–605 户（按综合分序，SC-1275 … SC-1340）。

构成：印度 0 触达冷名单（约 20 户，多在售丰润达 / Atop）、南非 / 马来西亚 / 泰国 / 韩国 / 台湾零星、俄罗斯 17–18 推 0 回、尼日利亚 / 孟加拉 / 巴基斯坦 / 中东 DWDM 询盘户（本职线）。
  · 口径同桶 ⑥ 首批 + 补充（分销 / 批发 / 集成主体 + 中国 / 台湾品牌证据且属俄 / 印 / 韩或同区先例 → 闸 2 低优先；网店 / 终端 / 运营商留 C；纯无关非买家零互动 → 永久 pass）。
  · 候选 5 = ASI IN（在卖丰润达的工业 FS）/ eControl Devices IN（Atop 的工业 FS）/ Reditron ZA（大安防分销，Utepo + 帧田）/ DBG ZA（工业 FS / MC / 串口分销商，显示锐捷）/ PLC Systems RU（Korenix 分销商）→ 闸 2 查底数。
  · 永久 pass 1：SC-1302 Aboughaly Motors（埃及汽车授权经销商，网站与网络产品无关，非买家、零互动 = 纯无关）。
  · 其余留 C：印度网店 / 终端（ehoome 丰润达 · APM Kingstrack 车辆追踪 · Biolink 像国内外壳 + WA · Camone no_mx · Avyukta no_mx · Consistent · Discreet · Easytech · Datasol · Dynalog · DC Infotech · Avihs）/ 印度运营商（ACT Corp 买国内交换机模块 = 巨头 ISP）/ 巴基斯坦 Ahmer（丰润达，非点名国）/ 南非死域名待巡检（Amptek dead · AGE）/ 孟加拉（Workstation · Datatech · Asiabiz dead）/ 俄罗斯（Optel · parts2b OM330 光模块）/ 韩国名牌专营（Yoisys Moxa · MTMnet 平台 · Unionelecom）/ 台湾同行（Optoway 光模块 · Rapidmax · Sintrones 车载 PC · SK.net 产品线接近 · Top-Unum 电源）/ 马来西亚 / 泰国（Prismabytes 全 Soltech · Multitrade Advantech · Switch2com nxdomain · Thai MMI Korenix）/ 中东名牌（Techzone D-Link · TB Distr · Shams ONV）/ 乌克兰守界（Willows RFQ）/ 尼日利亚 Fiberone（ISP，Simon 加了 Larry 微信 → 回信即候选）/ 本职线 dayjob_fit（DWDM · 相干模块 · EoSDH · WDM DCI）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_022.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批22_2026-10-29.md）
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

BATCH = 'G1-22'
DATE = '2026-10-29'
CODES = ["SC-1275", "SC-1276", "SC-1278", "SC-1279", "SC-1280", "SC-1281", "SC-1282", "SC-1283", "SC-1284", "SC-1285", "SC-1286", "SC-1287", "SC-1288", "SC-1289", "SC-1290", "SC-1291", "SC-1292", "SC-1293", "SC-1294", "SC-1295", "SC-1296", "SC-1298", "SC-1299", "SC-1300", "SC-1301", "SC-1302", "SC-1305", "SC-1306", "SC-1309", "SC-1310", "SC-1314", "SC-1315", "SC-1316", "SC-1317", "SC-1318", "SC-1319", "SC-1320", "SC-1321", "SC-1322", "SC-1323", "SC-1324", "SC-1325", "SC-1326", "SC-1327", "SC-1328", "SC-1329", "SC-1330", "SC-1331", "SC-1332", "SC-1334", "SC-1336", "SC-1337", "SC-1338", "SC-1339", "SC-1340"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-1302': ('pass_final', '埃及 Aboughaly Motors Authorized Distributor（aboughalymotors.com；汽车授权经销商，表内「网站看不出来啥东西，不太相关」）非网络买家、零互动 → 纯无关非买家，永久 pass', []),
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1280': ('candidate', '俄罗斯 PLC Systems（plcsystems.ru；工业 FS，Korenix 的分销商；lantan.pro 域 nxdomain）：进口台湾同类 ✔ 对位 ✔ 分销主体 Simon 点名俄罗斯；群发 18 次 0 回 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-1283': ('candidate', '南非 Reditron（reditron.co.za；大型安防分销，Utepo + 帧田 + CCTV）：进口中国同类 ✔ 对位 ✔ 分销主体 + 同区先例 Duxbury / MiRO；群发 8 次 0 回 → 闸 2 查底数（CIPC 镜像）；低优先', []),
    'SC-1322': ('candidate', '印度 ASI（asi.ind.in；在卖丰润达的工业 FS）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1332': ('candidate', '南非 DBG（dbg.co.za；工业 FS / MC / SFP / VC / 串口分销商，显示了国内锐捷的牌子）：进口中国同类 ✔ 对位 ✔ 分销主体 + 同区先例；未触达 → 闸 2 查底数（CIPC 镜像）；低优先', ['dayjob_fit']),
    'SC-1339': ('candidate', '印度 eControl Devices（econtroldevices.com；Atop 的工业 FS）：进口台湾同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1281': ('keep_C', '马来西亚 Prismabytes（prismabytes.com；产品线很接近但都是 Soltech 的）：进口中国同类 ✔ 但四主区外非点名国 + 零互动 → 留 C（储备）', []),
    'SC-1288': ('keep_C', '台湾 SK.net（sk.net.tw；产品线很接近）：台湾同类品牌商（疑同行）+ 零互动 → 留 C', []),
    'SC-1299': ('keep_C', '韩国 Yoisys（yoisys.com；在用 Moxa 的很多产品）：Moxa 专营 + 零互动 → 留 C', []),
    'SC-1309': ('keep_C', '韩国 Elftech（elftech.co.kr；展会问 3800 系列、相干模块、200G QSFP-DD 价格 / Tunable；网站有 WDM 设备）：本职线互动 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1310': ('keep_C', '尼日利亚 Fiberone Broadband（fob.ng；宽带 ISP，3 人展会、Simon 加了 Larry 微信、交换机 / WDM 都看了）：运营商 + 非点名国，但微信在 → 留 C（回信即候选）+ dayjob_fit', ['dayjob_fit']),
    'SC-1316': ('keep_C', '印度 ACT Corp（actcorp.in；大型 ISP，买国内的交换机 / 模块）：巨头运营商（难但非永久 pass）→ 留 C', []),
    'SC-1318': ('keep_C', '巴基斯坦 Ahmer Enterprises（ahmerenterprises.com；买丰润达的商业 PoE）：进口中国同类 ✔ 但非点名国 + 零互动 → 留 C（储备）', []),
    'SC-1319': ('keep_C', '南非 Amptek（amptek.co.za 域 dead，无退信；卖本土 Scoop 的牌子）：死域名 → 留 C 待巡检', []),
    'SC-1320': ('keep_C', '印度 APM Kingstrack（apmkingstrack.com；车辆追踪公司，丰润达的商业 PoE）：终端自用 → 留 C', []),
    'SC-1323': ('keep_C', '孟加拉 Asiabiz（asiabizbd.com 域 dead，无退信；CCTV 为主）：死域名 → 留 C 待巡检', []),
    'SC-1325': ('keep_C', '印度 Avyukta Shop（avyuktashop.com 域 no_mx；商业 switch 网店）：网店 + 死域名 → 留 C 待巡检', []),
    'SC-1326': ('keep_C', '印度 Biolink（biolinkindia.com；商业 PoE「看着像是国内的外壳」；网站有 WA）：进口证据不确定 + 零互动 → 留 C（储备，WA 可试）', []),
    'SC-1328': ('keep_C', '印度 Camone（camone.in 域 no_mx；bioroles.com 正常；CCTV + 国内商业 PoE，邮箱来自 facebook）：主域无 MX → 留 C 待巡检', []),
    'SC-1340': ('keep_C', '印度 ehoome.in（买丰润达的商业 PoE；智能家居网店）：网店 + 零互动 → 留 C（储备）', []),
    'SC-1289': ('keep_C', '马来西亚 Switch2com（switch2com.com 域 nxdomain；s2com.com.my 正常；都有、价格不高）：主域死 + 非点名国 → 留 C 待巡检', []),
    'SC-1296': ('keep_C', '乌克兰 Willows Holding（阿里 RFQ「无人机光纤」）：乌克兰 = 守界 + 品类不供 → 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 22 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 551–605 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：印度 0 触达约 20 户（多在售丰润达 / Atop）、南非 / 马 / 泰 / 韩 / 台零星、俄罗斯 17–18 推 0 回、尼日利亚 / 孟加拉 / 巴基斯坦 / 中东 DWDM 询盘户。口径同桶 ⑥ 首批 + 补充（网店 / 终端 / 运营商留 C；纯无关非买家零互动 → 永久 pass）。候选 5 = ASI / eControl Devices（IN，丰润达 / Atop 工业 FS）、Reditron / DBG（ZA 分销，Utepo 帧田 / 锐捷）、PLC Systems（RU，Korenix 分销）；永久 pass 1 = Aboughaly Motors（埃及汽车经销商）。留 C：印度网店 / 终端 / 巨头 ISP、巴基斯坦 / 孟加拉储备、死域名待巡检、俄罗斯光模块、韩国名牌专营与平台、台湾同行、马 / 泰储备、中东名牌、乌克兰守界、Fiberone（微信在）、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批22_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
