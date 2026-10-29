#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 08 批（2026-10-29）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 386–495 户（按编号序，SC-2870 … SC-552）。

构成：「用户判定不行」欧美安防 / 网络经销商（表内多标退信 bounce，域名仍正常）+ 「综合分低 · 名单内未触达」的光开关 / WDM / DCI 厂商冷名单（多为同行或本职线）+ 群发冷名单。
  · 候选 18 = 已在卖中国白牌（洪瑞 / 3onedata / 3C Link / ONV / Wi-Tek / Utepo）或 自有品牌（Extralink / Cables N More 自有 logo 型号 / Niveo / Lütze）或 主区分销主体（digitx / Sphinx / Videcon / Blake UK / Industrial Comms / Hatteland / Pine Networks）或 成单（EasyWind RTS 4 台）→ 闸 2 查底数；Simon 曾判不行的注明「可否决」。
  · 永久 pass 1：SC-3200 twenga.es（比价平台，非买家、零互动 = 纯无关）。
  · 其余留 C：巨头 / 同行（光开关 · 光模块 · 测试仪器厂商）/ 本职线（WDM · DCI · 光端机 → dayjob_fit）/ 平台 / 个人 / 死域名无退信待巡检。
  · 「stop」flag 来自 STOP_WORDS 文本命中（含我方「Spam」备注），不是明确要求停发 → 不作 pass 依据（已沿用 G1-04 口径）。

用法：python3 sieve_batches/g1_008.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批08_2026-10-29.md）
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

BATCH = 'G1-08'
DATE = '2026-10-29'
CODES = ["SC-2870", "SC-2872", "SC-2889", "SC-2892", "SC-2893", "SC-2894", "SC-2895", "SC-2919", "SC-2923", "SC-2924", "SC-2930", "SC-2934", "SC-2939", "SC-294", "SC-2940", "SC-2941", "SC-2943", "SC-2944", "SC-2945", "SC-2946", "SC-2947", "SC-2948", "SC-2949", "SC-2950", "SC-2954", "SC-2956", "SC-2962", "SC-2976", "SC-2993", "SC-301", "SC-3020", "SC-3023", "SC-3024", "SC-303", "SC-3036", "SC-3049", "SC-3051", "SC-3052", "SC-3057", "SC-3058", "SC-3061", "SC-3062", "SC-308", "SC-3086", "SC-3092", "SC-3131", "SC-3133", "SC-3135", "SC-316", "SC-3169", "SC-317", "SC-3171", "SC-318", "SC-319", "SC-3190", "SC-3191", "SC-3192", "SC-3193", "SC-3195", "SC-3196", "SC-3199", "SC-320", "SC-3200", "SC-3209", "SC-321", "SC-322", "SC-3236", "SC-3241", "SC-325", "SC-3266", "SC-327", "SC-3270", "SC-328", "SC-330", "SC-3302", "SC-3305", "SC-331", "SC-334", "SC-338", "SC-339", "SC-340", "SC-342", "SC-344", "SC-345", "SC-348", "SC-349", "SC-351", "SC-352", "SC-355", "SC-357", "SC-358", "SC-363", "SC-364", "SC-366", "SC-370", "SC-378", "SC-383", "SC-388", "SC-402", "SC-410", "SC-418", "SC-457", "SC-466", "SC-468", "SC-490", "SC-503", "SC-515", "SC-518", "SC-532", "SC-552"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-3200': ('pass_final', '西班牙 twenga.es（Twenga 比价 / 购物搜索平台，非经销商、非买家；表内仅「很多牌子的」）零互动 → 纯无关行业非买家，永久 pass', []),
    # ---- 候选 → 闸 2 ----
    'SC-2870': ('candidate', '葡萄牙 PT Refurb（ptrefurb.pt；洪瑞的商业 PoE）：欧洲 + 已进口同供应链产品 + 对位 ✔；17 推 0 回 → 闸 2 查底数，低优先' + Q33 + VETO, []),
    'SC-2872': ('candidate', '丹麦 Sevecu（sevecu.com；商业 PoE：大华 / 光网视 ONV / 洪瑞）：欧洲 + 多品牌进口经验 + 对位 ✔；17 推 0 回 → 闸 2 查底数' + Q33 + VETO, []),
    'SC-2941': ('candidate', '意大利 Digitx（digitx.it；研究档：博洛尼亚工业电子 B2B 电商 2012 起，卖 Moxa / PLANET / 3onedata / Teltonika / Mean Well 给自动化客户；bypass / 工业电源 / 工业 FS）：欧洲 + 已进口中国工业品牌 + 对位 ✔；退信 → 闸 2 查底数 + 找新地址' + VETO, []),
    'SC-2943': ('candidate', '波兰 Extralink（extralink24.com / .eu；自有品牌 Extralink：国内外壳 switch / PoE 配件 / PON，「有人在卖他们的」= 品牌已铺渠道）：波兰次主区 + 自有品牌贴牌 ✔ → 闸 2 查底数（OEM 对象）；退信 → 找新地址' + VETO, ['oem_target']),
    'SC-2993': ('candidate', '美国 Cables N More / TL Networx（cablesnmore.com / tlnetworx.com；宇航的工业 FS、MC 好几个外壳、SFP，**自己的 logo 和型号**）：美国主区 + 自有品牌贴牌 ✔ + 已进口中国品牌 ✔；17 推 0 回 + 退信 → 闸 2 查底数 + 找新地址' + VETO, ['oem_target', 'dayjob_fit']),
    'SC-3023': ('candidate', '波兰 Nettrans（nettrans.pl；工业 FS：国内 3C Link / ONV 的）：波兰次主区 + 已进口中国同类品牌 + 对位 ✔；退信 → 闸 2 查底数 + 找新地址' + VETO, []),
    'SC-3057': ('candidate', 'kamery-hikvision.sk（表内国别「斯洛文尼亚」应为斯洛伐克 .sk，闸 2 核；Wi-Tek 的）：欧洲 + 已进口中国同类品牌；退信 → 闸 2 查底数 + 定国别，低优先' + VETO, []),
    'SC-3135': ('candidate', '法国 Sphinx（sphinxcomputer.fr / sphinxconnect.fr；工业 FS 好几个牌子 = 法国工业网络分销商）：欧洲 + 分销主体 + 对位 ✔ → 闸 2 查底数（stop flag 为文本命中，非要求停发）' + VETO, []),
    'SC-2954': ('candidate', '英国 Videcon（videcon.co.uk；CCTV 分销为主、有商业 PoE；疑有自有品牌线，闸 2 核）：英国主区 + 分销主体 + 对位 ✔；退信 → 闸 2 查底数 + 找新地址，低优先' + VETO, []),
    'SC-2976': ('candidate', '英国 Blake UK（blake-uk.com；CCTV / networking / fiber 销售平台 = 英国天线 / 安防大分销）：英国主区 + 分销主体 + 对位 ✔ → 闸 2 查底数，低优先' + VETO, []),
    'SC-3266': ('candidate', '西班牙 Calytel（calytel.com；很多国内的产品、CCTV 为主、「卖下边公司的」）：欧洲 + 多品牌进口经验 + 对位 ✔ → 闸 2 查底数，低优先（stop flag 为文本命中）' + VETO, []),
    'SC-3302': ('candidate', '荷兰 Niveo Professional（niveoprofessional.com；自有品牌 Niveo：商业 PoE / 10G / MC / 机架 / SFP / 大口 FS 全线贴牌）：欧洲 + 自有品牌 ✔ + 对位 ✔；15 推 0 回 + 退信 → 闸 2 查底数 + 找新地址（OEM 对象）' + VETO, ['oem_target', 'dayjob_fit']),
    'SC-331': ('candidate', '英国 Industrial Comms（industrialcomms.com；bypass / 工业 FS 基本是研华的 = 工业网络分销）：英国主区 + 分销主体 + 对位 ✔；名单内未触达 → 闸 2 查底数，低优先', []),
    'SC-345': ('candidate', '法国 Pine Networks（pine-networks.com；Edgecore 的 = 开放网络 / 数据中心白盒渠道）：欧洲 + DC 对位（CENTEC 敲门砖）+ 分销主体；名单内未触达 → 闸 2 查底数，低优先', []),
    'SC-364': ('candidate', '德国 EasyWind GmbH（easywind.org；阿里巴巴 RTS 成单：4 台 1 光 4 电小壳非 PoE）：德国主区 + 成单 ✔ + 对位 ✔ ≥2 条；WA 加不上 → 闸 2 查底数 + 回访', []),
    'SC-468': ('candidate', '爱沙尼亚 BK Eesti（bkeesti.ee；CCTV 为主，有 Utepo 的）：欧洲 + 已进口中国同类品牌 + 对位 ✔；15 推 0 回 → 闸 2 查底数，低优先', []),
    'SC-490': ('candidate', '挪威 Hatteland Technology（hattelandtechnology.com；工业 FS：有用 ONV 的 + Moxa，「分销有名牌子的」= 北欧工业电子分销集团）：欧洲 + 分销主体 + 已进口中国品牌 + 对位 ✔；15 推 0 回 → 闸 2 查底数', []),
    'SC-503': ('candidate', '美国 Lütze Inc.（lutze.com；工业 FS 自己的 PVC 膜和编号 = 自有品牌贴牌；德系工业集团美国公司，表内「体量过大」）：美国主区 + 自有品牌 ✔ + 对位 ✔；11 推 0 回 → 闸 2 查底数（OEM 对象；体量偏大非巨头）', ['oem_target']),
    # ---- 需要专门说明的留 C ----
    'SC-2889': ('keep_C', '美国 QCT / Quanta Cloud Technology（大口 switch；退信）→ ODM 巨头 / 同行；留 C', []),
    'SC-2893': ('keep_C', '法国 Areva T&D（已并入 GE Grid；电话加不上、areva-td.com 无 MX）→ 巨头 + 法人变更；留 C', []),
    'SC-2894': ('keep_C', '法国 DATA FIBRE（域名 NXDOMAIN、电话加不上；记录称实为 HK 公司）→ 无退信记录不满足 G0-2；留 C，巡检后再定', []),
    'SC-2895': ('keep_C', '法国 Monitoring Company（域名 NXDOMAIN、电话加不上；要全线价格表）→ 无退信记录不满足 G0-2；留 C，巡检后再定', []),
    'SC-2924': ('keep_C', '土耳其 GIS Güvenlik（光端机 / 收发器；域名 NXDOMAIN、电话加不上）→ 本职线 + 未满足 G0-2；留 C，巡检后再定', ['dayjob_fit']),
    'SC-2946': ('keep_C', '美国 Mobotrex（交通 ITS 分销，工业 FS 卖 Comtrol 的；退信）→ 美系品牌渠道、无中国白牌进口证据；留 C（巡检有新信号再升）', []),
    'SC-2947': ('keep_C', '意大利 Net-Store（Digitus 产品很多、MC / SFP / 大口商业 FS；退信）→ 德系品牌零售、无白牌进口证据；留 C', ['dayjob_fit']),
    'SC-3020': ('keep_C', '英国 Comnet Europe / acre（37 推 0 回；Mark Roberts）→ 同行厂商；留 C', ['dayjob_fit']),
    'SC-3049': ('keep_C', '挪威 Alloptix（2021 新司，基本无源产品；域名 NXDOMAIN 无退信）→ 不满足 G0-2；留 C，巡检后再定', []),
    'SC-3131': ('keep_C', '美国 Watersnet（switch；「Spam」为我方备注、18 推 0 回）→ 非明确要求停发；留 C', []),
    'SC-3133': ('keep_C', '美国 Federal Cable（全线 Signamax 的）→ 美系品牌渠道、无白牌进口证据；留 C', []),
    'SC-3190': ('keep_C', '美国 Data Interfaces（很多知名供应商的销售平台）→ 平台型无 KP；留 C', []),
    'SC-3191': ('keep_C', '美国 DiCon Fiberoptics（光开关厂商；台湾办事处）→ 同行 / 本职线；留 C', ['dayjob_fit']),
    'SC-3236': ('keep_C', '美国 calebbeene.com（个人站、视频相关；2022 国际站；退信）→ 个人非买家但非刚性；留 C', []),
    'SC-317': ('keep_C', '土耳其 ATP Tech（Edge Data Center Deployment；名单内未触达）→ DC 相关但零证据；留 C（巡检有信号即升候选，CENTEC 线）', []),
    'SC-327': ('keep_C', '土耳其 Eva ICT（Edge Data Center Deployment；名单内未触达）→ 同上；留 C', []),
    'SC-321': ('keep_C', '土耳其 CCS Güvenlik（switch 有洪瑞的；域名无 MX + 退信）→ 邮件已死但未核官网；留 C，巡检后再定' + Q33, []),
    'SC-340': ('keep_C', '波兰 Nexitel（工业 FS、相关产品较多；退信、8 推 0 回）→ 无品牌 / 进口证据；留 C（找到新地址再议）', []),
    'SC-383': ('keep_C', '加拿大 ysesq.com（2 光 8 PoE 管理 12–48V 询盘；WA 加不上）→ 单次询盘、无实体证据；留 C', []),
    'SC-515': ('keep_C', '美国 Perle（同行厂商）+ dcscom.net（卖 Perle 的加拿大经销）→ 同行 / 其渠道；留 C', ['dayjob_fit']),
    'SC-518': ('keep_C', '美国 ProLabs（光模块 / DAC / AOC 品牌商；Will Kilmartin）→ 同行 / 本职线；留 C', ['dayjob_fit']),
    'SC-552': ('keep_C', '土耳其 LANDE（机柜制造商；MC）→ 机柜厂非交换机渠道；留 C', []),
    'SC-370': ('keep_C', '美国 Micro Trends（2008 年 8 / 16 / 24 口 PoE 询盘；电话加不上）→ 陈年单次询盘；留 C', []),
}


def main():
    assert len(CODES) == 110 and len(set(CODES)) == 110
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
    L = [f'# C 池 · 闸 1 · 第 08 批（{DATE}）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 386–495 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：「用户判定不行」欧美经销商（多标退信但域名正常）+ 光开关 / WDM / DCI 厂商冷名单（同行或本职线）+ 群发冷名单。候选 18 = 在卖中国白牌（洪瑞 / 3onedata / 3C Link / ONV / Wi-Tek / Utepo）、自有品牌（Extralink / Cables N More / Niveo / Lütze → oem_target）、主区分销主体（digitx / Sphinx / Videcon / Blake UK / Industrial Comms / Hatteland / Pine Networks）、成单（EasyWind RTS 4 台）；'
         '**曾判不行的理由末尾标「可否决」。** 永久 pass 1：twenga.es 比价平台。「stop」flag = 文本命中（含我方「Spam」备注），不作 pass 依据。多户「域名 NXDOMAIN 但无退信记录」留 C 等巡检。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批08_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
