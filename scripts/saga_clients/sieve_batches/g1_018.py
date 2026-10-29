#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 18 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 331–385 户（按综合分序，SC-806 … SC-898）。

构成：俄罗斯 0 触达工业 / CCTV 分销与网店（约 30 户）、越南 0 触达（约 18 户）、乌兹别克 3 户、印尼 / 印度 / 日本零星。
  · 口径同桶 ⑥ 首批 + 补充：名牌专营（单一台湾 / 欧美牌子）留 C；分销 / 集成主体 + 中国品牌证据 → 闸 2 低优先；洪瑞现供 → 候选 + Q-33 口径。
  · 候选 7 = EFO / Infiber RU（大电子分销，「很多中国合作商」）/ Mirtelcom RU（丰润达工业 PoE）/ Mistercom RU（朱姐客户产品 + 多牌，WA 在站）/ Nout.kz KZ（ONV 好几个工业 FS 型号）/ Novicam RU（自有品牌 CCTV → oem_target）/ Pixietech UZ（洪瑞的 → Q-33）/ Plexonics IN（百通 + 买很多国内的 PoE，点名印度）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：俄罗斯名牌专营（icp-das.ru ICP DAS · iie.ai Edimax · itnext.by Moxa · linkas 知名牌）/ 俄罗斯大分销无中国品牌证据（IPC2U · NNZ · Lanset · Insat · ic54）/ 巨头与大平台（Marvel · NIX）/ 中资分支（Jotrin）/ 死域名待巡检（it-volga no_mx · multech dead · thietbiquang no_mx）/ 俄罗斯 CCTV 小店与品牌不明（idom25 · infoteh AVT-lan · krosstel · msv77 · nposkss · orgtelecom · pimnara · novimax · n-l.ooo）/ 越南 0 触达储备（Mai Phuong 多国内牌 · Maptech 中科兰奥 · Netsystem BTON · Phuc Binh 发过目录报价 · Hoang Van ORing 等）/ 乌兹别克 oppr.uz Utepo（小）/ 印尼 MJG 集成商（问过 SFP 兼容）/ 日本 LINEEYE（2004 国际站问 PoE 分离器 = 不供）/ 本职线 dayjob_fit（VC · 光猫 · OLT）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_018.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批18_2026-10-29.md）
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

BATCH = 'G1-18'
DATE = '2026-10-29'
CODES = ["SC-806", "SC-807", "SC-808", "SC-810", "SC-812", "SC-814", "SC-815", "SC-816", "SC-817", "SC-818", "SC-820", "SC-823", "SC-824", "SC-825", "SC-826", "SC-828", "SC-829", "SC-832", "SC-836", "SC-839", "SC-842", "SC-844", "SC-846", "SC-848", "SC-850", "SC-851", "SC-852", "SC-853", "SC-854", "SC-859", "SC-860", "SC-861", "SC-862", "SC-865", "SC-866", "SC-869", "SC-873", "SC-874", "SC-876", "SC-879", "SC-880", "SC-881", "SC-882", "SC-883", "SC-884", "SC-885", "SC-886", "SC-888", "SC-889", "SC-891", "SC-893", "SC-894", "SC-896", "SC-897", "SC-898"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-817': ('candidate', '俄罗斯 EFO / Infiber（infiber.ru 域 no_mx，efo.ru 正常；MC / FS / 光猫，表内「很多中国合作商」）：进口中国同类 ✔ 对位 ✔ 大电子分销主体；未触达 → 闸 2 查底数（rusprofile）+ 换 efo.ru 地址；俄语区收款待定，低优先', []),
    'SC-859': ('candidate', '俄罗斯 Mirtelcom（mirtelcom.ru；丰润达的工业 PoE）：进口中国同类 ✔ 对位 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-860': ('candidate', '俄罗斯 Mistercom（mistercom.ru；工商业 FS 好几家牌子，有朱姐客户的；网站有 WA 按钮）：进口中国同类 ✔ 对位 ✔ WA 路径 ✔；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-883': ('candidate', '哈萨克斯坦 Nout.kz（nout.kz，表内国别俄罗斯、域 .kz；ONV 的好几个工业 FS 型号，比较多的品牌）：进口中国同类 ✔ 对位 ✔ 俄语区先例（NAG KZ）；未触达 → 闸 2 查底数（statsnet）+ 国别核（RU → KZ 待证据）；收款待定，低优先', []),
    'SC-884': ('candidate', '俄罗斯 Novicam（novicam.ru；自有品牌 CCTV，商业 PoE / 配件主要挂 PV-Link 牌）：自有品牌 = OEM 对象 ✔ 对位 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['oem_target']),
    'SC-897': ('candidate', '乌兹别克斯坦 Pixietech（pixietech.uz；洪瑞的 = 洪瑞现供）：进口中国同类 ✔ 对位 ✔ 同区先例 SETKO 成单；未触达 → 闸 2 查底数；低优先' + Q33, []),
    'SC-898': ('candidate', '印度 Plexonics（plexonics.com；百通 + 「买很多国内的 PoE」）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-808': ('keep_C', '越南 Thiết bị quang / Hợp Nhất（thietbiquang.com.vn 域 no_mx；hopnhatgroup.com 正常；工业 FS / MC / SFP / VC，在和 G-net 合作）：进口中国同类 ✔ 但四主区外非点名国 + 主域无 MX → 留 C（储备，待巡检）+ dayjob_fit', ['dayjob_fit']),
    'SC-814': ('keep_C', '俄罗斯 icp-das.ru（ICP DAS 俄区专营站：MC / 工业 FS / 光猫）：台湾名牌专营 → 留 C', []),
    'SC-816': ('keep_C', '俄罗斯 iie.ai（基本都是 Edimax 的工业 FS）：台湾名牌专营 + 零互动 → 留 C（储备）', []),
    'SC-824': ('keep_C', '俄罗斯 IPC2U（ipc2u.ru；大型工业电子分销：工业 FS / 串口 / 工业 MC / 电源）：分销主体但无中国品牌证据 + 零互动 → 留 C（闸 2 可补；储备）', []),
    'SC-826': ('keep_C', '俄罗斯 it-volga.ru（域 no_mx，无退信；商业 PoE 配件卖好几家的）：死域名无退信 → 留 C 待巡检', []),
    'SC-828': ('keep_C', '白俄罗斯 ITNext（itnext.by，表内国别俄罗斯；工业 MC / switch Moxa 的）：Moxa 专营 + 四主区外 → 留 C', []),
    'SC-832': ('keep_C', '俄罗斯 jotrin.ru（域 no_mx）/ jotrin.com（深圳元器件分销 Jotrin 俄区站）：中资分支 → 留 C', []),
    'SC-844': ('keep_C', '日本 LINEEYE（lineeye.co.jp；协议分析仪厂商；2004 国际站询「千兆 15.4W 5V PoE splitter 60 个」）：分离器 Saga 不供 + WA 加失败 → 留 C', []),
    'SC-852': ('keep_C', '越南 Mai Phuong（maiphuong.vn / maiphuonggroup.com；很多国内的牌子，商业 PoE）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-853': ('keep_C', '越南 Maptech（maptechvn.com；中科 / 兰奥的）：进口中国同类 ✔ 但四主区外非点名国 → 留 C（储备）', []),
    'SC-854': ('keep_C', '俄罗斯 Marvel Distribution（marvel.ru；IT 分销巨头）：巨头体系 → 留 C', []),
    'SC-861': ('keep_C', '印尼 MJG（mjg.co.id；系统集成商，问过「别人的 SFP 可以用在我们的 FS 上吗」）：有互动但四主区外非点名国 → 留 C（储备）', []),
    'SC-866': ('keep_C', '越南 Multech（multech.com.vn 域 dead，无退信；大口 FS / OLT / SFP）：死域名无退信 → 留 C 待巡检', []),
    'SC-876': ('keep_C', '越南 Netsystem（netsystemvn.com / netsystem.vn；思科 / 瞻博为主 + BTON 的 VC + 工业 MC）：名牌为主 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-880': ('keep_C', '俄罗斯 NIX（nix.ru；大型电脑 / 电子电商，CCTV 为主）：大平台；推 1 次 0 回 → 留 C', []),
    'SC-882': ('keep_C', '俄罗斯 NNZ（nnz-ipc.ru / nnz.ru；工业 PC 分销，工业 FS / MC 很多牌子）：分销主体但无中国品牌证据 → 留 C（储备）', []),
    'SC-891': ('keep_C', '乌兹别克斯坦 oppr.uz（Utepo 的）：进口中国同类 ✔ 但规模不明 + 零互动 → 留 C（储备）', []),
    'SC-894': ('keep_C', '越南 Phúc Bình（phucbinh.com.vn；收发器 / 交换机；曾「发目录 & 报价」）：有互动但四主区外非点名国 → 留 C（储备；回信即候选）', []),
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
    L = [f'# C 池 · 闸 1 · 第 18 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 331–385 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：俄罗斯 0 触达工业 / CCTV 分销与网店约 30 户、越南 0 触达约 18 户、乌兹别克 3 户、印尼 / 印度 / 日本零星。口径同桶 ⑥ 首批 + 补充：名牌专营留 C；分销 / 集成主体 + 中国品牌证据 → 闸 2 低优先；洪瑞现供 → 候选 + Q-33。候选 7 = EFO / Infiber（RU 大分销「很多中国合作商」）/ Mirtelcom（RU，丰润达）/ Mistercom（RU，朱姐客户产品 + WA）/ Nout.kz（KZ，ONV）/ Novicam（RU 自有品牌 CCTV）/ Pixietech（UZ，洪瑞现供 Q-33）/ Plexonics（IN，买很多国内 PoE）；永久 pass 0。留 C：名牌专营、大分销无中国品牌证据、巨头与大平台、中资分支、死域名待巡检、CCTV 小店与品牌不明、越南 / 乌兹别克 / 印尼储备、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批18_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
