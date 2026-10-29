#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 19 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 386–440 户（按综合分序，SC-899 … SC-1022）。

构成：俄罗斯 / 白俄罗斯 0 触达 CCTV 与工业网店 / 分销（约 40 户）、越南 0 触达（约 9 户）、哈萨克 / 乌兹别克 / 马来西亚 / 南非 / 尼日利亚 / 台湾零星。
  · 口径同桶 ⑥ 首批 + 补充（网店留 C；名牌专营留 C；分销 / 批发主体 + 中国品牌证据 → 闸 2 低优先；自有品牌不限国别）。
  · 候选 6 = QP Optom RU（批发，全线 itoonertech 的 FS）/ Smartec RU（自有品牌 CCTV，工业 FS 国内外壳 → oem_target）/ Spektr Video RU（工商业 FS 有 Utepo）/ TrueView IN（自有品牌 CCTV + 商业 PoE，有人卖他们的设备 → oem_target）/ Utepo.by BY（Utepo 白俄罗斯专营 = 进口中国同类）/ Moon.kz KZ（ONV 很多产品）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：俄罗斯同行（TFortis 自研高 IP 工业机）/ 俄产品牌转售（point-it Gigalink · uralvision）/ 大分销无中国品牌证据（Satro-Paladin · telecom-sales 平台）/ 巨头（TVEL / Rosatom 域匹配存疑）/ 死域名待巡检（r-control nxdomain 朱姐客户牌 · relion-ex no_mx · wizolution no_mx）/ 网店（videomir.pro ONV · zipstore · xbitspb）/ CCTV 小店与无品牌证据（约 25 户）/ 越南储备（Vu Hoang 多国内牌 · Vien Thong Xanh 光网视 · Soeco · Sieu Thi Mang）/ 马来西亚 NetEon（展位放了三旺交换机 + ORing，非点名国储备）/ 尼日利亚 NetPro（洪瑞现供 → Q-33，非点名国）/ 乌兹别克 ELT 19 推 0 回 / 台湾 Liverage 光模块 dayjob_fit / 本职线 dayjob_fit（VC · 光猫 · PON）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_019.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批19_2026-10-29.md）
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

BATCH = 'G1-19'
DATE = '2026-10-29'
CODES = ["SC-899", "SC-900", "SC-904", "SC-906", "SC-909", "SC-910", "SC-912", "SC-915", "SC-919", "SC-923", "SC-926", "SC-927", "SC-930", "SC-931", "SC-932", "SC-933", "SC-939", "SC-940", "SC-941", "SC-943", "SC-945", "SC-946", "SC-948", "SC-949", "SC-950", "SC-954", "SC-955", "SC-962", "SC-963", "SC-964", "SC-967", "SC-969", "SC-971", "SC-972", "SC-976", "SC-977", "SC-981", "SC-983", "SC-984", "SC-985", "SC-986", "SC-987", "SC-988", "SC-989", "SC-992", "SC-993", "SC-995", "SC-997", "SC-999", "SC-1005", "SC-1011", "SC-1015", "SC-1018", "SC-1020", "SC-1022"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-912': ('candidate', '俄罗斯 QP Optom（qpoptom.ru；批发，全线用 itoonertech 的 FS，IPC 为主 / CCTV 领域）：进口中国同类 ✔ 对位 ✔ 批发主体 Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-941': ('candidate', '俄罗斯 Smartec（smartec-cctv.ru；自有品牌 CCTV，工业 FS 国内的外壳 = 中国代工）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['oem_target']),
    'SC-946': ('candidate', '俄罗斯 Spektr Video（spektrvideo.ru；工商业 FS 有 Utepo 的）：进口中国同类 ✔ 对位 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-969': ('candidate', '印度 TrueView（trueview.co.in；自有品牌 CCTV + 商业 PoE「同行的」，有人卖他们的设备）：自有品牌 = OEM 对象 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', ['oem_target']),
    'SC-977': ('candidate', '白俄罗斯 Utepo.by（表内国别俄罗斯、域 .by；Utepo 白俄罗斯专营，工业 FS）：进口中国同类 ✔ 对位 ✔ 俄语区先例；未触达 → 闸 2 查底数 + 国别核（RU → BY 待证据）；RU + BY 收款待定，低优先', []),
    'SC-1020': ('candidate', '哈萨克斯坦 Moon.kz（moon.kz；ONV 很多产品）：进口中国同类 ✔ 对位 ✔ 俄语区先例（NAG KZ）；群发 18 次 0 回 → 闸 2 查底数（statsnet）；收款待定，低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-900': ('keep_C', '俄罗斯 Point IT（point-it.ru；Gigalink 的 switch / PoE）：俄产品牌转售 + 零互动 → 留 C', []),
    'SC-915': ('keep_C', '俄罗斯 R-Control（r-control.ru 域 nxdomain，无退信；有朱姐客户的牌子 + 本土牌，工业 FS / VC / PoE 配件）：进口中国同类 ✔ 但死域名 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-919': ('keep_C', '俄罗斯 relion-ex.ru（域 no_mx；spectron-ops.ru 正常；switch）：主域无 MX 无退信 → 留 C 待巡检', []),
    'SC-927': ('keep_C', '俄罗斯 Satro-Paladin（satro-paladin.com；大型安防分销 / 销售平台，商业 PoE / 工业 FS）：分销主体但无中国品牌证据 + 零互动 → 留 C（储备，闸 2 可补）', []),
    'SC-962': ('keep_C', '俄罗斯 telecom-sales.ru（销售平台，商业 PoE / 工业 FS）：平台 + 无品牌证据；推 1 次 0 回 → 留 C', []),
    'SC-963': ('keep_C', '俄罗斯 TFortis / Fort-Telecom（tfortis.ru / fort-telecom.ru；自研高 IP 等级工业交换机厂商，比较专业；多个具名邮箱）：俄产同行 → 留 C', []),
    'SC-971': ('keep_C', '俄罗斯 tvel.ru（TVEL / Rosatom 核燃料公司域；表内「自己的 PVC 膜 logo，主要是大口 FS」= 域匹配存疑）：巨头 + 匹配存疑 → 留 C 待核', []),
    'SC-972': ('keep_C', '俄罗斯 ubnt.su（Ubiquiti 转售站）：名牌专营 → 留 C', []),
    'SC-976': ('keep_C', '俄罗斯 Uralvision（uralvision.com；工商业 FS 基本是卖上边几家公司的产品）：俄区转售 + 零互动 → 留 C', []),
    'SC-983': ('keep_C', '俄罗斯 Videomir.pro（很多品牌的、有 ONV 的，CCTV 为主很多配件）：进口中国同类 ✔ 但网店 + 零互动 → 留 C（储备）', []),
    'SC-995': ('keep_C', '俄罗斯 wizolution.ru（域 no_mx，无退信；PoE 配件 / 工业 FS）：死域名无退信 → 留 C 待巡检', []),
    'SC-985': ('keep_C', '越南 Viễn Thông Xanh（vienthongxanh.vn；商业 PoE 主要是光网视 ONV 的）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-989': ('keep_C', '越南 Vũ Hoàng Telecom（vuhoangtelecom.vn；MC / SFP / switch 好几个国内牌子）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-1005': ('keep_C', '马来西亚 NetEon (M) Sdn Bhd（neteon.com.my；参展商 7163，展位上放了三旺的交换机 + ORing bypass 工业 FS；手机在表）：进口中国同类 ✔ 有展会互动 ✔ 但四主区外非点名国 → 留 C（储备；若点名东南亚可升候选）', []),
    'SC-1018': ('keep_C', '台湾 Liverage（liverage.com.tw；光模块 / AOC / DOC 厂商）：光模块同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1022': ('keep_C', '尼日利亚 NetPro ICT（netproict.com；洪瑞的商业 PoE = 洪瑞现供）：进口中国同类 ✔ 但非点名国；群发 4 次 0 回 → 留 C（储备）' + Q33, []),
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
    L = [f'# C 池 · 闸 1 · 第 19 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 386–440 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：俄罗斯 / 白俄罗斯 0 触达 CCTV 与工业网店 / 分销约 40 户、越南 0 触达约 9 户、哈萨克 / 乌兹别克 / 马来西亚 / 南非 / 尼日利亚 / 台湾零星。口径同桶 ⑥ 首批 + 补充（网店 / 名牌专营留 C；分销 / 批发主体 + 中国品牌证据 → 闸 2 低优先；自有品牌不限国别）。候选 6 = QP Optom（RU 批发，itoonertech）/ Smartec（RU 自有品牌 CCTV）/ Spektr Video（RU，Utepo）/ TrueView（IN 自有品牌 CCTV）/ Utepo.by（BY）/ Moon.kz（KZ，ONV）；永久 pass 0。留 C：俄产同行（TFortis）、俄产品牌转售、大分销无中国品牌证据、巨头匹配存疑（tvel.ru）、死域名待巡检、网店、CCTV 小店、越南 / 马来西亚（NetEon 展位三旺）/ 尼日利亚（NetPro 洪瑞 Q-33）储备、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批19_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
