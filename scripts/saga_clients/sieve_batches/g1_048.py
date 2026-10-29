#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 48 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 716–734 户（末批 19 户；按综合分序，SC-3279 … SC-3315；综合分 −100 → −131，全桶最底）。

构成：「无联系方式」名单 10（2011 年展会 / 海关数据 / 富通天下条目为主）、退信 3（无备用 2）、仅电话 1、免费邮箱 2、巨头 2（Merlion、Ethio Telecom）、守界乌克兰 1、域名死 2。
  · 口径同第 47 批：闸 0 刚性① = 无邮箱 / 电话 / WA / 域名 / 平台链接且原表无任何迹；刚性② = 退信且无备用路径。巨头 / 乌克兰 / Simon「Spam」一律不 pass。
  · 候选 0。永久 pass 6 = SC-3281 Rasyonel Güvenlik TR（ETW 2011 仅公司名）/ SC-3287 Him Hippo NP（仅公司名）/ SC-3417（ETW 2011 仅「VC, russian」）/ SC-3315 ICOT EG（ETW 2011 仅公司名）/ SC-3289 Secutech KE（yahoo 退信无备用）/ SC-3294（icloud 退信无备用）。
  · 留意：SC-3414 / SC-3415 = 同一家 INGENIERIA Y CONTRATOS S.A.S.（海关数据，两条重复 → 待并档）；SC-3279 Merlion = 俄罗斯 IT 分销巨头；SC-3292 Jos. Hansen & Soehne (Gulf) = 德资贸易行海湾公司（Intersec 2011）。
  · 本批结束 = 桶 ⑦ 734 户全部过闸，闸 1 全部 3,419 户过完。

用法：python3 sieve_batches/g1_048.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批48_2026-10-29.md）
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

BATCH = 'G1-48'
DATE = '2026-10-29'
CODES = ["SC-3279", "SC-3281", "SC-3282", "SC-3414", "SC-3415", "SC-3286", "SC-3287", "SC-3289", "SC-3290", "SC-3292", "SC-3294", "SC-3416", "SC-3301", "SC-3307", "SC-3308", "SC-3310", "SC-3311", "SC-3417", "SC-3315"]

OVERRIDE = {
    'SC-3281': ('pass_final', '土耳其 Rasyonel Güvenlik Sistemleri（ETW 2011 展会名单；fiber optic price list；原表无邮箱 / 电话 / 网址 / 微信 / 领英）：闸 0 刚性①（无邮箱 / 电话 / WA / 域名 / 平台链接，原表无任何可寻迹）→ 永久 pass（2011 陈旧 + 土耳其同名安防公司众多，无法坐实；如 Simon 想救回可按编号否决）', []),
    'SC-3287': ('pass_final', '尼泊尔 Him Hippo Company Pvt. Ltd.（「a bid of telecom Nepal」；原表无邮箱 / 电话 / 网址）：闸 0 刚性①（无邮箱 / 电话 / WA / 域名 / 平台链接，原表无任何可寻迹）→ 永久 pass', []),
    'SC-3417': ('pass_final', '哈萨克斯坦（未具名；ETW 2011；仅「VC, russian」；原表无公司名 / 邮箱 / 电话 / 网址）：闸 0 刚性①（无邮箱 / 电话 / WA / 域名 / 平台链接，原表无任何可寻迹）→ 永久 pass', []),
    'SC-3315': ('pass_final', '埃及 ICOT（ETW 2011；8ch VC；原表无邮箱 / 电话 / 网址）：闸 0 刚性①（无邮箱 / 电话 / WA / 域名 / 平台链接，原表无任何可寻迹）→ 永久 pass；VC 本职线亦无路径', []),
    'SC-3289': ('pass_final', '肯尼亚 Secutech Masters Limited（Andrew M. Ngigi / CEO；wanyabs@yahoo.com 退信；「VC buy from others at $15 less」；无电话 / 域名 / 平台）：退信且无电话 / 域名 / 平台备用路径 = 闸 0 刚性② → 永久 pass', []),
    'SC-3294': ('pass_final', '美国 Ami Cardenasespinoza（amicardenas12@icloud.com 退信；光猫；无电话 / 域名 / 平台）：退信且无电话 / 域名 / 平台备用路径 = 闸 0 刚性② → 永久 pass', []),
    'SC-3279': ('keep_C', '俄罗斯 ООО «МЕРЛИОН»（Merlion；「从 IP-COM 买，网站打不开」；富通天下；原表无邮箱 / 电话）：俄罗斯最大 IT 分销巨头之一 → 留 C 巨头（不 pass；路径未建，收款待定）', []),
    'SC-3311': ('keep_C', '埃塞俄比亚 Ethio Telecom（ethiotelecom.et 正常；Mebrahtu Marso，gmail；需要 OTDR）：巨头运营商 + OTDR 本职线 → 留 C 巨头 + dayjob_fit', ['dayjob_fit']),
    'SC-3308': ('keep_C', '乌克兰 IT-Web（MIC；TA510-FE；原表无联系方式）：守界乌克兰（不 pass，不主动发）→ 留 C', []),
    'SC-3414': ('keep_C', 'INGENIERIA Y CONTRATOS S.A.S.（海关数据；原表仅谷歌搜索链接；国别未填，S.A.S. 后缀指向哥伦比亚 → 国别待核）：海关数据有进口记录 = 路径可建 → 留 C 待巡检', []),
    'SC-3415': ('keep_C', 'INGENIERIA Y CONTRATOS S.A.S.（与 SC-3414 完全同一条海关数据，重复录入 → 待并档到 SC-3414）：随 SC-3414 留 C', []),
    'SC-3282': ('keep_C', '格鲁吉亚 Georgian International Company（Giorgi Varsimashvili；rambler.ru 退信；电话 +995 95 908 376 在但 WA 加不上；VC）：电话 = 备用路径，非刚性 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3286': ('keep_C', '沙特 Creative Computer Trading（Shafi；仅电话 +966 50 273 7825；Simon「暂时不跟进」）：电话路径在；Simon 标记非 pass 依据 → 留 C 不主动', []),
    'SC-3290': ('keep_C', '沙特 Advanced Broadband Electro（abb-electro.com dead；「12 pairs 8V1D」VC；表内标体量过大）：域名死 + 无邮箱 → 留 C 待巡检（下次仍死即 pass）+ dayjob_fit', ['dayjob_fit']),
    'SC-3301': ('keep_C', '法国 Artus Events（artusevents.com dead；Fleury Syrill，syrill@wanadoo.fr 未退信；SDI 多功能；官网视频类；Simon 不跟）：邮箱在 = 路径在；SDI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3292': ('keep_C', 'Jos. Hansen & Soehne (Gulf) LLC（Intersec 2011；原表仅「@emirates.net.ae」域名片段；catalogue；表内沙特，实为阿联酋 → 国别待核）：德资贸易行海湾公司，公司可坐实但路径未建 → 留 C 待巡检', []),
    'SC-3416': ('keep_C', '俄罗斯 iTrade Group（原表公司栏即 itrade-group.ru；ETW 2011；SFP；无邮箱 / 电话）：域名 = 路径可建；SFP 本职线 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-3307': ('keep_C', '印度 currentoptronics@gmail.com（SFP，「买后边的」= 深圳 OPWAY；Simon 标 Spam）：SFP 本职线；Simon 标记非 pass 依据 → 留 C 不主动 + dayjob_fit', ['dayjob_fit']),
    'SC-3310': ('keep_C', '埃塞俄比亚 Alador Nigus（领英来源 = 平台路径；catalogue；主要 networking / CCTV）：个人 + 无先例 → 留 C 储备', []),
}


def main():
    assert len(CODES) == 19 and len(set(CODES)) == 19
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
    L = [f'# C 池 · 闸 1 · 第 48 批（桶 ⑦ 收尾）（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 716–734 户（末批，19 户）（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：无联系方式 10、退信 3、仅电话 1、免费邮箱 2、巨头 2、守界 1、域名死 2（有重叠）。候选 0。永久 pass 6 = 仅公司名无任何路径 4（SC-3281 / 3287 / 3417 / 3315，闸 0 刚性①）+ 退信无备用 2（SC-3289 / 3294，刚性②）。', '',
         '> 桶 ⑦ 至此 734 户全部过闸；闸 1 共 48 批覆盖 C 池 3,419 户。SC-3414 / SC-3415 重复待并档；Merlion / Ethio Telecom 巨头留 C；Jos. Hansen (Gulf) 2011 名单留 C 待巡检。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批48_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
