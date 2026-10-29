#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 11 批（2026-10-29）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 606–660 户（按编号序，SC-878 … SC-998）= 桶 ⑤ 收尾。

构成：全部冷名单未触达 / 推过 1–4 次未回复的欧美 / 波兰光模块商 · 工业分销 · 安防网店 · 巨头。
  · 候选 4 = 已进口台湾工业品牌且对位强（prumysloveswitche.cz 研华「工业交换机」专卖 / sarcitalia Atop + USR IoT / semaphore-systems Advantech GB / systerra Moxa DE）→ 闸 2 查底数。
  · 永久 pass 2：SC-973 ul.com（UL 认证机构，非买家、零互动 = 纯无关）、SC-998 zenitled.com.tr（LED 照明制造商，非买家、零互动 = 纯无关）。
  · 其余留 C：巨头 / 同行（Niagara · OE Solutions · Optixcom · Schrack · Senetic · Provantage · TDK · Turck Banner · Verkada · Rhombus · WASKO）/ 本职线（CWDM SFP · 光模块 · VC → dayjob_fit）/ 仅卖欧美日名牌（Moxa · Weidmüller · LevelOne · TRENDnet · RocketLinx）/ 死域名无退信待巡检（pwrel.it · rbdatasys · redalert）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_011.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批11_2026-10-29.md）
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

BATCH = 'G1-11'
DATE = '2026-10-29'
CODES = ["SC-878", "SC-887", "SC-890", "SC-892", "SC-895", "SC-901", "SC-902", "SC-903", "SC-905", "SC-907", "SC-908", "SC-911", "SC-913", "SC-914", "SC-916", "SC-917", "SC-918", "SC-920", "SC-921", "SC-922", "SC-924", "SC-925", "SC-928", "SC-929", "SC-934", "SC-935", "SC-936", "SC-937", "SC-938", "SC-942", "SC-944", "SC-947", "SC-951", "SC-952", "SC-953", "SC-956", "SC-957", "SC-958", "SC-959", "SC-960", "SC-961", "SC-965", "SC-966", "SC-968", "SC-970", "SC-973", "SC-978", "SC-979", "SC-980", "SC-982", "SC-990", "SC-991", "SC-994", "SC-996", "SC-998"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-973': ('pass_final', '美国 ul.com（UL 认证 / 检测机构，非经销商、非买家）零互动 → 纯无关行业非买家，永久 pass', []),
    'SC-998': ('pass_final', '土耳其 Zenit LED（zenitled.com.tr；LED 照明制造商，非网络产品买家）零互动 → 纯无关行业非买家，永久 pass', []),
    # ---- 候选 → 闸 2 ----
    'SC-908': ('candidate', '捷克 Průmyslové switche / Bluecom（prumysloveswitche.cz / bluecom.cz；「工业交换机」专卖，基本都是研华的）：欧洲 + 已进口台湾工业品牌 + 对位极强；未触达 → 闸 2 查底数', []),
    'SC-925': ('candidate', '意大利 SARC Italia（sarcitalia.it；Atop + USR IoT）：欧洲 + 已进口台湾 / 中国工业品牌 + 对位 ✔；未触达 → 闸 2 查底数', []),
    'SC-935': ('candidate', '英国 Semaphore Systems（semaphore-systems.co.uk；Advantech）：四主区 + 已进口台湾工业品牌 + 对位 ✔；未触达 → 闸 2 查底数', []),
    'SC-956': ('candidate', '德国 Systerra（systerra.de；Moxa 分销）：四主区 + 工业网络分销主体 + 对位 ✔；未触达 → 闸 2 查底数（Moxa 不点名）', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-878': ('keep_C', '美国 Niagara Networks（niagaranetworks.com；高端 bypass / TAP 厂商）：同行制造商；未触达 → 留 C', []),
    'SC-887': ('keep_C', '希腊 NSYS（nsys.gr；CWDM SFP / Network）：光模块 = 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-890': ('keep_C', '美国 OE Solutions（oesolutions.com；SFP 制造商）：光模块同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-892': ('keep_C', '美国 Optixcom（opticaltransceiver.com；基本都是 SFP）：光模块同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-895': ('keep_C', '美国 / 德国 piezosystem jena（piezosystem.com；压电 / 光开关精密器件厂）：非网络买家；未触达 → 留 C（非刚性 pass）', []),
    'SC-902': ('keep_C', '美国 Precision OT（precisionot.com；CWDM SFP）：光模块 = 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-911': ('keep_C', '意大利 PWREL（pwrel.it；域名 dead、表内 fail 但无退信记录）：→ 留 C 待巡检', []),
    'SC-914': ('keep_C', '美国 QuestTel（questtel.com；VC 为主）：本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-917': ('keep_C', '美国 RB Datasys（rbdatasys.com；域名 NXDOMAIN 但无退信记录）：→ 留 C 待巡检', []),
    'SC-918': ('keep_C', '英国 Red Alert Data and Telecoms（域名 NXDOMAIN 但无退信记录；拿过 catalogue）：→ 留 C 待巡检', []),
    'SC-920': ('keep_C', '美国 Rhombus（rhombus.com；云摄像机厂商）：同行 / 自有供应链；未触达 → 留 C', []),
    'SC-928': ('keep_C', '奥地利 Schrack Technik（schrack.com；电气巨头，基本都是 LevelOne）：巨头采购体系；1 推 0 回 → 留 C', []),
    'SC-936': ('keep_C', '捷克 Senetic（senetic.cz；跨国 IT 电商，主要是 Planet 的）：大型电商采购体系；未触达 → 留 C', []),
    'SC-937': ('keep_C', '西班牙 Senetic（senetic.es；跨国 IT 电商）：大型电商采购体系；未触达 → 留 C', []),
    'SC-947': ('keep_C', '德国 Spree Fiber（spree-fiber.com；基本就是光模块）：光模块同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-953': ('keep_C', '瑞典 Swedish Telecom Opto（swedishtelecomopto.com；主要是 SFP）：光模块同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-958': ('keep_C', '意大利 TDK（tdk.com；电子元件巨头）：非经销买家；未触达 → 留 C', []),
    'SC-965': ('keep_C', '波兰 Tibtronix（tibtronix.eu；基本都是 SFP）：光模块同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-966': ('keep_C', '意大利 TLC Fabrik（tlcfabrik.com；CWDM SFP；域名 no_mx）：光模块 = 本职线；未触达 → 留 C + dayjob_fit 待巡检', ['dayjob_fit']),
    'SC-970': ('keep_C', '意大利 Turck Banner（turckbanner.it；传感器巨头意大利公司）：巨头采购体系；未触达 → 留 C', []),
    'SC-979': ('keep_C', '美国 Verkada（verkada.com；云安防巨头）：同行 / 自有供应链；未触达 → 留 C', []),
    'SC-982': ('keep_C', '保加利亚 Videomax AVS（videomaxavs.com；「产品线比较接近」）：欧洲 + 对位，但无进口 / 体量证据；1 推 0 回 → 留 C（出现信号再升候选）', []),
    'SC-990': ('keep_C', '波兰 WASKO S.A.（wasko.pl；大型 IT / 电信集成商）：巨头采购体系；未触达 → 留 C', []),
    'SC-991': ('keep_C', '罗马尼亚 Wavezon（wavezon.com；CWDM SFP）：光模块 = 本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-996': ('keep_C', '波兰 xBest（xbest.pl；知名品牌 + CWDM 线缆配件）：品类偏无源 / 本职线；4 推 0 回 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 11 批（{DATE}）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 606–660 户（{len(V)} 户；桶 ⑤ 收尾）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：全部冷名单未触达 / 推过 1–4 次未回复。候选 4 = 已进口台湾工业品牌且对位强（Průmyslové switche 研华 / SARC Italia Atop + USR / Semaphore Advantech / Systerra Moxa）；'
         '永久 pass 2 = ul.com（认证机构）、zenitled.com.tr（LED 厂）= 纯无关非买家零互动。留 C：巨头 / 同行（Niagara · OE Solutions · Optixcom · Schrack · Senetic · TDK · Turck Banner · Verkada · Rhombus · WASKO）、本职线（CWDM SFP · 光模块 · VC → dayjob_fit）、仅卖欧美日名牌、死域名无退信待巡检。「stop」flag = 文本命中，不作 pass 依据。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批11_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
