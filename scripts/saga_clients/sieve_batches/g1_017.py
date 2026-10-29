#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 17 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 276–330 户（按综合分序，SC-699 … SC-805）。

构成：俄罗斯 0 触达 CCTV / 工业网店与分销（约 35 户）、越南 0 触达冷名单（约 15 户）、乌兹别克 / 印尼 / 新加坡零星。
  · 口径同桶 ⑥ 首批 + 补充：纯网店（.shop / 商城）即使在售中国品牌也留 C 储备；分销 / 集成主体 + 中国 / 台湾品牌证据 → 闸 2 低优先；白俄罗斯并入俄语区先例（RU + BY 收款待 Simon）。
  · 候选 6 = Angtel RU（工业 FS 自有系列编号、有人在卖他们的 = 自有品牌）/ ARMO Systems RU（大安防分销，用 Utepo）/ Avant BY（工商业 FS 好几家牌子，有宇航等国内的）/ BIC Video RU（朱姐客户产品 + 多牌「可以查一下」）/ Brown Bear RU（工业 FS / MC Planet 的）/ Exara RU（在找 switch / WDM / MPLS / PTN，会中文常驻杭州，Simon 当天发了目录册待老板审核 = 真互动）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：俄罗斯 CCTV 小店「主要是 CCTV 有一些商业 PoE」（all-bez · bas-ip · bast · bic-inform · donvision · cctvdom · domofonn · av808 · bnt-video · devicepro · anteycentr）/ 俄罗斯无品牌证据（angareyon · aofortis · apm · aveon · bbrc · conel · dekker · euromobile · evisb · anlan 线缆）/ 网店（c-tt.shop Wi-Tek · great-store 丰润达 no_mx · esocctv ESVI）/ 巨头与大平台（ETM · ChipDip）/ 国别存疑待核（cctvcamerapros.com 疑美国 · e-server.com.ua 疑乌克兰）/ bztel（Simon 曾跟进 WDM → 回信即候选）/ 越南 0 触达储备（Bingcomm ONV · congnghevienthong 三旺 Upcom · GOC · CPT · Cotel 等）/ 印尼 Aswindra DCN / 本职线 dayjob_fit（模拟光端机 · WDM · VC）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_017.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批17_2026-10-29.md）
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

BATCH = 'G1-17'
DATE = '2026-10-29'
CODES = ["SC-699", "SC-701", "SC-702", "SC-703", "SC-705", "SC-706", "SC-707", "SC-708", "SC-711", "SC-713", "SC-714", "SC-715", "SC-717", "SC-718", "SC-719", "SC-720", "SC-721", "SC-722", "SC-724", "SC-725", "SC-726", "SC-727", "SC-729", "SC-730", "SC-731", "SC-738", "SC-739", "SC-740", "SC-743", "SC-746", "SC-747", "SC-749", "SC-750", "SC-757", "SC-758", "SC-761", "SC-762", "SC-763", "SC-765", "SC-772", "SC-776", "SC-777", "SC-778", "SC-781", "SC-782", "SC-784", "SC-785", "SC-791", "SC-792", "SC-795", "SC-796", "SC-799", "SC-801", "SC-802", "SC-805"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-702': ('candidate', '俄罗斯 Angtel（angtel.ru；工业 FS 有自己的系列编号、有人在卖他们的 = 自有品牌）：自有品牌 = OEM 对象 ✔ 对位 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['oem_target']),
    'SC-708': ('candidate', '俄罗斯 ARMO Systems（armosystems.ru / armo.ru；大型安防分销，表内「用的 Utepo 的，工业 FS / SFP / PoE 配件」）：进口中国同类 ✔ 对位 ✔ 分销主体；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-714': ('candidate', '白俄罗斯 Avant（avant.by；表内国别俄罗斯，域 .by；工商业 FS 好几家牌子，有宇航等国内的）：进口中国同类 ✔ 对位 ✔ 俄语区先例；未触达 → 闸 2 查底数 + 国别核（RU → BY 待证据）；RU + BY 收款待定，低优先', []),
    'SC-722': ('candidate', '俄罗斯 BIC Video（bic-video.ru；工业 FS / SFP / MC 朱姐客户的 + HDMI / SDI / AHD，很多牌子「可以查一下」）：进口中国同类 ✔ 对位 ✔；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['dayjob_fit']),
    'SC-729': ('candidate', '俄罗斯 Brown Bear（brownbear.ru；工业 FS / MC Planet 的）：进口台湾同类 ✔ 对位 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-782': ('candidate', '俄罗斯 Exara（exara.ru；在找 switch / WDM / MPLS / PTN，会中文、常驻杭州，Simon 邮件当天发了目录册让老板审核；+86 手机在表）：真互动 ✔ 对位 ✔（switch 线）+ 本职线（WDM / PTN）；→ 闸 2 查底数（rusprofile）+ 微信 / 电话跟进；俄语区收款待定', ['dayjob_fit']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-717': ('keep_C', '新加坡 Barrier Master（barriermaster.com；自建站询盘「4V / 8V 模拟光端机」）：本职线品类 + 终端；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-730': ('keep_C', '俄罗斯 BZTel（bztel.ru；WDM / Switch；表内「无沟通记录，Simon 之前跟进过」）：曾跟进无回 + 本职线 → 留 C + dayjob_fit（回信即候选）', ['dayjob_fit']),
    'SC-731': ('keep_C', '俄罗斯 c-tt.shop / c-tt.ru（工业 FS Wi-Tek）：进口中国同类 ✔ 但纯网店 + 零互动 → 留 C（储备）', []),
    'SC-738': ('keep_C', 'cctvcamerapros.com（表内国别俄罗斯；.com 域、疑为美国 CCTV Camera Pros，待核）：安防为主 + 国别存疑 → 留 C 待核（若坐实美国可重过桶 ⑤ 口径）', []),
    'SC-740': ('keep_C', '俄罗斯 ChipDip（chipdip.ru；大型元器件 / 电子电商）：大平台 → 留 C', []),
    'SC-765': ('keep_C', 'e-server.com.ua（表内国别俄罗斯；.ua 域、疑为乌克兰，待核）：MC / switch 很多牌子 + 国别存疑（乌克兰 = 守界）→ 留 C 待核', []),
    'SC-776': ('keep_C', '俄罗斯 ESO CCTV（esocctv.ru；商业 PoE 主要是 ESVI 牌子，没查到）：品牌来源不明 + 零互动 → 留 C', []),
    'SC-777': ('keep_C', '俄罗斯 ETM（etm.ru；全国电气分销巨头，工业 MC / FS 很多牌子）：巨头体系 → 留 C', []),
    'SC-796': ('keep_C', '俄罗斯 great-store.ru（域 no_mx，无退信；丰润达的商业 PoE）：进口中国同类 ✔ 但网店 + 死域名 → 留 C 待巡检', []),
    'SC-711': ('keep_C', '印尼 Aswindra（aswindra.co.id；基本都是 DCN 的）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-724': ('keep_C', '越南 Bingcomm（bingcomm.com；ONV 的 FS / 工业 FS + Yeastar）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-747': ('keep_C', '越南 Công nghệ Viễn thông / HPTT（congnghevienthong.com / hptt.vn；工业 FS / 串口 / VC / MC，三旺 · Upcom 等较多牌子）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）+ dayjob_fit', ['dayjob_fit']),
    'SC-805': ('keep_C', '印尼 Hessatech（hessatech.com；普通光端机，说需要 PoE injector）：本职线 + 注入器 Saga 不供 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 17 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 276–330 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：俄罗斯 0 触达 CCTV / 工业网店与分销约 35 户、越南 0 触达约 15 户、乌兹别克 / 印尼 / 新加坡零星。口径同桶 ⑥ 首批 + 补充：纯网店即使在售中国品牌也留 C；分销 / 集成主体 + 中国 / 台湾品牌证据 → 闸 2 低优先；白俄罗斯并入俄语区先例。候选 6 = Angtel（RU 自有系列）/ ARMO Systems（RU 大安防分销，Utepo）/ Avant（BY，宇航等）/ BIC Video（RU，朱姐客户产品）/ Brown Bear（RU，Planet）/ Exara（RU，Simon 发过目录册的真互动）；永久 pass 0。留 C：俄罗斯 CCTV 小店与无品牌证据户、网店、巨头与大平台、国别存疑待核（cctvcamerapros.com · e-server.com.ua）、bztel 曾跟进、越南 / 印尼储备、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批17_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
