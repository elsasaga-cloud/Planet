#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 14 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 111–165 户（按综合分序，SC-416 … SC-496）。

构成：台湾工业网络 / CCTV 厂商（群发 8–9 次 0 回或 0 触达）、韩国 / 马来西亚 / 澳新展会与冷名单 0 触达户、乌克兰 2 户（守界）、中东零星。
  · 口径同桶 ⑥ 首批：四主区外默认留 C；「已进口中国 / 台湾同类品牌」+ 俄 / 印 / 韩（或同区先例）→ 闸 2 低优先；「自有品牌 = OEM 品牌商」不限国别 → 闸 2 低优先。
  · 候选 6 = AGS Electronics KR（在售 Atop）/ Atronic IN（在售 ONV 连 logo 都没换）/ AVTECH TW（自有品牌 CCTV，PoE 很像帧田的 = 外购中国）/ FXC JP（自有品牌 MC / SFP / 大口 FS）/ HiSharp TW（自有品牌 CCTV，商业 PoE 洪瑞的 → Q-33）/ IDIS KR（自有品牌 CCTV 大厂，商业 PoE）→ 闸 2 查底数。
  · 永久 pass 1：SC-462 asmag.com（a&s 安防媒体 / Messe Frankfurt New Era，非买家、零互动 = 纯无关）。
  · 其余留 C：台湾同行（Lantech · Leonton · Primmcon · Proscend · Rubytech · Autech · Enconn · Equaline · Giantnet · i-nk · DJS · Dynacom）/ 巨头（RAD · IPD）/ 乌克兰守界（NTEMA hasivo · Megatrade 大分销）/ 美德品牌专营（ANP Red Lion + PULS · Guru-N Juniper · STDL QNAP）/ 马来西亚 · 澳新 · 中东 0 触达（Primalcom Utek 合作 · FST Security Planet · GSA Planet · iot-store USR 等储备）/ 死域名（clnetworks nxdomain · idv.tw）待巡检 / 本职线 dayjob_fit（XFP · VC · DWDM）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_014.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批14_2026-10-29.md）
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

BATCH = 'G1-14'
DATE = '2026-10-29'
CODES = ["SC-416", "SC-417", "SC-419", "SC-421", "SC-422", "SC-423", "SC-424", "SC-425", "SC-426", "SC-428", "SC-432", "SC-434", "SC-437", "SC-439", "SC-444", "SC-446", "SC-447", "SC-449", "SC-451", "SC-452", "SC-453", "SC-454", "SC-455", "SC-456", "SC-459", "SC-461", "SC-462", "SC-463", "SC-464", "SC-465", "SC-469", "SC-470", "SC-471", "SC-472", "SC-473", "SC-474", "SC-475", "SC-476", "SC-477", "SC-478", "SC-479", "SC-482", "SC-483", "SC-484", "SC-485", "SC-486", "SC-487", "SC-488", "SC-489", "SC-491", "SC-492", "SC-493", "SC-494", "SC-495", "SC-496"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-462': ('pass_final', '台湾 asmag.com（a&s 安防行业媒体 / Messe Frankfurt New Era Business Media；非经销商、非买家）零互动、无询盘 → 纯无关行业非买家，永久 pass', []),
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-455': ('candidate', '韩国 AGS Electronics（ags-electronics.com；在售 Atop 台湾工业交换机）：进口台湾同类 ✔ 对位 ✔ Simon 点名韩国；未触达 → 闸 2 查底数（bizno）；低优先', []),
    'SC-463': ('candidate', '印度 Atronic（atronic.co.in；表内「logo 都没换，还是 ONV 的」= 直售中国品牌）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-465': ('candidate', '台湾 AVTECH（avtech.com.tw；自有品牌 CCTV，表内「商业 PoE 很像帧田的」= 配套 PoE 外购中国）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔；未触达 → 闸 2 查底数（twincn）；四主区外，低优先', ['oem_target']),
    'SC-485': ('candidate', '日本 FXC（fxc.jp；自有品牌 MC / SFP / 大口 FS / OTN / OLT，无工业品）：自有品牌 = OEM 对象 ✔ 对位 ✔（商用线）；未触达 → 闸 2 查底数（houjin）；四主区外，低优先', ['oem_target']),
    'SC-491': ('candidate', '台湾 HiSharp（hisharp.com 域 no_mx / hisharp.com.tw；自有品牌 CCTV，表内「商业 PoE 洪瑞的」= 洪瑞现供）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔；未触达 → 闸 2 查底数（twincn）；四主区外，低优先' + Q33, ['oem_target']),
    'SC-493': ('candidate', '韩国 IDIS（idisglobal.com；自有品牌 CCTV 大厂，商业 PoE 配套）：自有品牌 = OEM 对象 ✔ 对位 ✔ Simon 点名韩国；未触达 → 闸 2 查底数（DART）；低优先，体量大走长线', ['oem_target']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-421': ('keep_C', '乌克兰 NTEMA（ntema.com.ua；Hasivo 商业 PoE）：进口中国同类 ✔ 但乌克兰 = 守界（难，非永久 pass）；群发 8 次 0 回 → 留 C', []),
    'SC-424': ('keep_C', '以色列 / 澳大利亚 RAD（rad.com；电信接入巨头，光旁路开关）：巨头 + bypass Saga 不供；群发 22 次 0 回 → 留 C', []),
    'SC-426': ('keep_C', '韩国 STDL（stdl.kr；switch 主要是 QNAP 的）：名牌专营；群发 23 次 0 回 → 留 C', []),
    'SC-432': ('keep_C', '马来西亚 CabNet Systems (M) Sdn. Bhd.（cabnet.asia；只用工业交换机、需 90W PoE、会中文）：PoE BT 90W Saga 不供 + 四主区外；未触达 → 留 C（储备）', []),
    'SC-444': ('keep_C', '乌克兰 Megatrade（megatrade.ua；大分销，工业级 PoE 管理交换机）：乌克兰 = 守界（难，非永久 pass）+ 大公司；未触达 → 留 C', []),
    'SC-449': ('keep_C', '马来西亚 Primalcom Enterprise Sdn Bhd（primalcom.com；名片有 Utek 标志 = 与国内 Utek 合作，当地多用 TP-Link）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备，可推工业级）', []),
    'SC-459': ('keep_C', '韩国 ANP Solutions（anpsolutions.co.kr / rtpkorea.com；Red Lion 工业 FS + PULS 电源）：仅卖美德名牌；未触达 → 留 C', []),
    'SC-470': ('keep_C', '韩国 CL Networks（clnetworks.co.kr 域 nxdomain，无退信）：死域名无退信 → 留 C 待巡检', []),
    'SC-477': ('keep_C', '台湾 Dynacom（dynacom.tw；商业 PoE，工业 FS 很少 / ONV 的，网站多为周边）：台湾周边商；未触达 → 留 C', []),
    'SC-484': ('keep_C', '马来西亚 FST Security（fstsecurity.com.my / focus.com.my；Switch Planet 的比较多，网站有 WA）：Planet 渠道 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-488': ('keep_C', '澳大利亚 GSA Systems（gsasystems.com.au；工业 FS Planet 的）：Planet 渠道 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-489': ('keep_C', '韩国 Guru-N（guru-n.co.kr；瞻博 switch）：名牌专营；未触达 → 留 C', []),
    'SC-494': ('keep_C', '台湾 IDV（idv.tw 域 dead / hinet.net；MC / 机架 / VC，可能外购刷标）：死域名无退信 + 本职线 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-495': ('keep_C', '澳大利亚 IoT Store（iot-store.com.au；USR IoT / PUSR 工业串口与交换机网店）：进口中国同类 ✔ 但网店 + 四主区外非点名国 → 留 C（储备）', []),
    'SC-496': ('keep_C', '澳大利亚 IPD（ipd.com.au；上市电气分销集团，工业 FS 卖别人的牌子）：巨头体系；未触达 → 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 14 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 111–165 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：台湾工业网络 / CCTV 厂商、韩 / 马 / 澳新展会与冷名单 0 触达户、乌克兰 2 户（守界）、中东零星。口径同桶 ⑥ 首批（四主区外默认留 C；进口中国 / 台湾同类 + 俄 / 印 / 韩或同区先例 → 闸 2 低优先；自有品牌 = OEM 品牌商不限国别 → 闸 2 低优先）。候选 6 = AGS Electronics（KR，Atop）/ Atronic（IN，ONV 原标）/ AVTECH（TW 自有品牌 CCTV）/ FXC（JP 自有品牌）/ HiSharp（TW 自有品牌，洪瑞现供 → Q-33）/ IDIS（KR 自有品牌 CCTV 大厂）；永久 pass 1 = asmag.com（安防媒体，非买家零互动）。留 C：台湾同行、巨头、乌克兰守界、美德名牌专营、马 / 澳新 / 中东 0 触达储备、死域名待巡检、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批14_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
