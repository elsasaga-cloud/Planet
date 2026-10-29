#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 12 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 1–55 户（按综合分序，SC-018 … SC-299）= 桶 ⑥ 1,257 开闸。

构成：亚太 / 俄语区 / 南亚 / 拉美 / 非洲 / 中东冷名单：台湾 · 韩国 · 日本同行与巨头、平台询盘（品类多为 Saga 不供：注入器 / I/O 模块 / EoC / 无人机 / DCI）、俄罗斯 CCTV / 工业分销群发 15–20 次未回复户。
  · 口径补充（桶 ⑥）：四主区外 → 默认留 C；「已进口中国 / 台湾同类品牌」且国别属 Simon 点名的俄罗斯 / 印度 / 韩国（或已有同区入池先例 ZA / UZ）→ 闸 2（低优先，俄语区收款待定）；「自有品牌 = OEM 品牌商」（目标顺位第一）不限国别 → 闸 2 低优先。
  · 候选 6 = DASAN Networks KR（三旺长期客户，上市网络设备商 → oem_target）/ COP Security TW（自有品牌 CCTV，PoE / 工业机外购 ONV → oem_target，低优先）/ comonyx RU（自有 Onyx CCTV 品牌 + ONV PoE 配件）/ inline.uz UZ（在售与公司同口型 2 光 8 工业机）/ MiRO ZA（多牌分销 + Edimax，同 Duxbury 先例）/ nag.kz KZ（NAG / SNR 自有品牌，从国内买 CWDM / Switch / SFP / MC）→ 闸 2 查底数。
  · 永久 pass 1：SC-180 tm.by（白俄罗斯综合网上商城：工具 / 家电 / 建材，非网络渠道、非买家、零互动 = 纯无关）。
  · 其余留 C：台湾 / 韩国 / 日本 / 香港同行与 ODM 巨头（ATW · AAEON · HawkeyeTech · IEI · Senao · Sera · Sercomm · Sunrich · HT Networks · Macnica · Hewtech · Delta）/ 运营商（Imagine BN · Rostelecom RU · HTI LY）/ 上市工程集团（Afcon）/ 军工守界（Enercon）/ Q-33（REPOTEC）/ 平台询盘品类不供但有互动（注入器 · I/O 模块 · EoC · 无人机 · DCI · 收发器）/ 本职线（模拟光端机板卡 · SFP 电口模块 · 光路彩页 → dayjob_fit）/ 俄罗斯群发 15–20 次 0 回且无进口证据（alstec · binfora · cameran · comfortsb · es-guard · fastwel · mavink）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_012.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批12_2026-10-29.md）
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

BATCH = 'G1-12'
DATE = '2026-10-29'
CODES = ["SC-018", "SC-039", "SC-050", "SC-053", "SC-054", "SC-067", "SC-069", "SC-075", "SC-081", "SC-095", "SC-096", "SC-100", "SC-101", "SC-102", "SC-108", "SC-110", "SC-111", "SC-113", "SC-149", "SC-150", "SC-163", "SC-170", "SC-171", "SC-172", "SC-173", "SC-174", "SC-176", "SC-177", "SC-178", "SC-179", "SC-180", "SC-184", "SC-185", "SC-197", "SC-199", "SC-205", "SC-206", "SC-208", "SC-209", "SC-248", "SC-267", "SC-270", "SC-275", "SC-279", "SC-281", "SC-282", "SC-283", "SC-286", "SC-287", "SC-289", "SC-291", "SC-295", "SC-297", "SC-298", "SC-299"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-180': ('pass_final', '白俄罗斯 TM.by（tm.by；明斯克综合网上商城：工具 / 家电 / 卫浴 / 建材，非网络渠道、非买家）零互动、无询盘 → 纯无关行业非买家，永久 pass', []),
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-185': ('candidate', '韩国 DASAN Networks（dasannetworks.com；上市网络设备集团；表内「三旺的长期合作客户」「质量高」= 长期进口中国工业交换机；KP Richard / jrcho@）：Simon 点名韩国 + 进口中国同类品牌 + 对位 ✔，群发 22 次 0 回 → 闸 2 查底数（DART）+ 找产品采购 KP；低优先，可否决', ['oem_target']),
    'SC-283': ('candidate', '俄罗斯 Comonyx / CCTV Onyx（comonyx.com / cctvonyx.ru；自有 Onyx CCTV 品牌 + 「有 ONV 的 PoE 配件」= 自有品牌 + 进口中国 PoE）：Simon 点名俄罗斯 + 自有品牌 + 对位 ✔，群发 20 次 0 回 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['oem_target']),
    'SC-295': ('candidate', '乌兹别克斯坦 Inline（inline.uz；表内「工业 FS / SFP / 光猫，好几个牌子，有公司的 2 光 8、nufiber 的」= 在售与公司同口型工业机）：进口中国同类 ✔ 对位 ✔ + 同区先例 SETKO 成单，群发 19 次 0 回 → 闸 2 查底数；低优先', []),
    'SC-298': ('candidate', '南非 MiRO（miro.co.za；表内「很多有名的牌子，有 Edimax 的；商业 PoE / FS / 工业 FS / 周边设备；分销商」= 多牌分销 + 进口台湾同类）：同区先例 Duxbury ★ + 对位 ✔，群发 8 次 0 回 → 闸 2 查底数；低优先', []),
    'SC-299': ('candidate', '哈萨克斯坦 NAG（nag.kz；NAG / SNR 集团自有品牌，表内「从国内买 CWDM 模块 / Switch / SFP / MC 等」= 自有品牌 + 从中国直采）：自有品牌 ✔ 进口中国同类 ✔ 对位 ✔，群发 16 次 0 回 → 闸 2 查底数；俄语区收款待定，低优先', ['oem_target', 'dayjob_fit']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-018': ('keep_C', '新加坡（待核）Fastcabling（fastcabling.com；深圳厂商海外品牌站）：同行；群发 5 次 0 回 → 留 C', []),
    'SC-053': ('keep_C', '韩国 BARO AI（baroai.com；自建站询盘「核心交换机 MSN3420-CB2FC Spectrum-2」= 品牌指定 DC 交换机）：AI 终端自用、品牌指定；未触达 → 留 C（DC 对位，CENTEC 敲门砖可择机）', []),
    'SC-067': ('keep_C', '俄罗斯 Eltex CM（eltexcm.ru；Элтекс 官方经销商，表内「switch 没办法突破」）：专营俄产 Eltex（国产替代导向）→ 留 C', []),
    'SC-069': ('keep_C', '文莱 Imagine Sdn. Bhd.（imagine.com.bn；电信运营商；「工业交换机 / 于总推荐」）：运营商 + 推荐线索；未触达 → 留 C（运营商不作永久 pass）', []),
    'SC-081': ('keep_C', '台湾 REPOTEC（repotec.com；MC / FS / 工业小壳 / SFP；表内「不跟了，他们那在面谈了」= SmartByte 原厂直接客户）：留 C' + Q33, []),
    'SC-096': ('keep_C', '新加坡 Rapsodo（rapsodo.com；运动表现分析设备厂商；展会问工业交换机 L2 / 光口速率，疑代朋友问）：非渠道但有互动（非零）→ 留 C（不主动碰）', []),
    'SC-150': ('keep_C', '香港 Sunrich / ST Lab（sunrichtech.com.hk；网卡 / 扩展坞 OEM/ODM 厂商；表内「2.5G switch」）：同行 + 2.5G 口径待 SB-263；群发 8 次 0 回 → 留 C', []),
    'SC-163': ('keep_C', '沙特 SAFEEN Subsea（safeensubsea.com；AD Ports 合资海洋工程；询盘「2V1D 模拟板子 RS422」= 模拟视频光端机板卡）：本职线 + 终端；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-170': ('keep_C', '塞内加尔 SynchubsHVSS（synchubs.net；询盘「1G 电口模块」= SFP 电口模块，Saga 不供）：本职线 + 区域外；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-172': ('candidate', '台湾 COP Security（cop-security.com；1992 起自有品牌 CCTV，表内「工业交换机 ONV 的」= 配套 PoE / 工业机外购中国品牌）：自有品牌 = OEM 对象 ✔ 进口中国同类 ✔ 对位 ✔；2 次 0 回 → 闸 2 查底数（twincn）；四主区外，低优先', ['oem_target']),
    'SC-173': ('keep_C', '马达加斯加 HABIBO Group（habibo.mg；食品集团；自建站询盘「2 个品牌的交换机」）：终端自用 + 区域外，但有询盘互动 → 留 C（不作永久 pass）', []),
    'SC-206': ('keep_C', '以色列 Enercon Technologies（enercon.co.il；军用电源 / 加固网络设备制造商 MIL-STD）：军工 = 守界（INH），群发 16 次 0 回 → 留 C（不主动碰；守界不等于刚性 pass）', []),
    'SC-208': ('keep_C', '澳大利亚 Fire Security Products（firesecurityproducts.com 域 no_mx；Carrier 旗下 IFS 集团自有线；仅 zendesk 客服邮箱）：巨头体系 + 域无 MX；群发 21 次 0 回 → 留 C 待巡检', []),
    'SC-209': ('keep_C', '澳大利亚（表内）HT Networks（htnetglobal.com；ISO9001 / OEM/ODM / 云管理平台 + 「深圳有办事处」）：中国厂商海外站 = 同行；群发 14 次 0 回 → 留 C', []),
    'SC-248': ('keep_C', '俄罗斯 Ростелеком Rostelecom（rt.ru；国家电信运营商 B2O 邮箱）：巨头运营商（难但非永久 pass）；未触达 → 留 C', []),
    'SC-270': ('keep_C', '马来西亚 Pernec Integrated Network Systems（pernec.com.my；IT 集成商，展会拿了光路彩页）：本职线互动 + 四主区外；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-289': ('keep_C', '俄罗斯 Fastwel（fastwel.ru；俄产工业计算机 / 工业 FS M12 自有品牌厂商）：同行 + M12 Saga 不供；群发 17 次 0 回 → 留 C', []),
    'SC-291': ('keep_C', '马来西亚 FGSS（fgss.asia；展会「需要报价单」）：有互动但四主区外、无进口证据；未触达 → 留 C（储备）', []),
    'SC-297': ('keep_C', '俄罗斯 Mavink / Aisprom（mavink.com 域 no_mx；aisprom.ru 正常；工业 FS）：群发 17 次 0 回、无进口证据 → 留 C 待巡检', []),
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
    L = [f'# C 池 · 闸 1 · 第 12 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 1–55 户（{len(V)} 户；桶 ⑥ 1,257 开闸）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：桶 ⑥ = 四主区外企业邮箱户，按综合分序。口径补充：四主区外默认留 C，只有「已进口中国 / 台湾同类品牌或自有品牌」且属 Simon 点名的俄罗斯 / 印度 / 韩国（或有同区入池先例 ZA / UZ）才进闸 2（低优先，俄语区收款待定）。候选 6 = DASAN Networks KR（三旺长期客户）/ COP Security TW（自有品牌 CCTV 外购 ONV）/ Comonyx RU（自有 Onyx 品牌 + ONV PoE）/ Inline UZ（在售同口型 2 光 8）/ MiRO ZA（多牌分销 + Edimax）/ NAG KZ（SNR 自有品牌，从国内直采）；永久 pass 1 = tm.by（白俄罗斯综合商城，非买家零互动）。留 C：台 / 韩 / 日 / 港同行与 ODM 巨头、运营商、上市工程集团、军工守界、Q-33（REPOTEC）、平台询盘品类不供但有互动、本职线（dayjob_fit）、俄罗斯群发 15–20 次 0 回无进口证据。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批12_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
