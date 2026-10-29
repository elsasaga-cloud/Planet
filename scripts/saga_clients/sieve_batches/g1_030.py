#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 30 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 991–1045 户（按综合分序，SC-2124 … SC-2322）。

构成：退信户 17（俄 / 越 / 印尼 / 巴 / 肯 / 沙，域名多正常 → 待巡检；仅 OK Computers PK 单域 no_mx）、乌克兰 6（守界）、「品类不符」VC / DWDM / CWDM / 跳线 / CCTV 约 30 户（俄罗斯 DWDM 集群 5 户用信泰 / 瑞斯康达 = 本职线）、WA 加不上 8、HK 同行 OT Systems（Simon 判不再跟进）。
  · 口径同桶 ⑥ 首批。本批无一户同时满足「可达 + 分销 / 集成 + 中国品牌 / 具体需求」：Gain ID 问工业 488 / 288GW（对位 STI-488DGGPM / STI-288GPM）但邮件 + WA 双退 → 待巡检，巡检通了再转候选；Asterisk KZ（ONV / 商业 PoE / 工业 FS 多品牌）退信 → 待巡检；ITBiz UA「全系列引入」→ 乌克兰守界；G-TECH MU 单台 Hirschmann RS20 替代询问 17 推 0 回 → 储备。
  · 候选 0；永久 pass 1 = OK Computers PK（okcomputers.com.pk 唯一域 no_mx + 退信 = 退信且域名全死，闸 0 刚性 G0-2）。
  · 其余留 C：退信待巡检（Microthings ID · Asterisk KZ · Gain ID · Indast RU · IP-Rec RU · KPS VN · Osbez RU 备用域 osbez.ru · RTK-Teh RU · SMCom VN · Sunico ID（DCN）· Sytek VN · Netlink PK 官网手机 · True-Tech KE · Vital PK · Terrabyt SA）；乌克兰守界（Import-Telecom 15 推 · Exe · Infosvyaz · Lanmarket · Svaltera · ITBiz）；本职线 dayjob_fit（MWA VC · 3kom DWDM · Cairo Comm SFP / MC / VC 要短交期 · dwdm-sfp.ru · Fiber Solutions PE · Fibronics · MK-F · N3com · Optic-Lines · RT Evolução FPV VC · Octopuss CL · Daccess IN VC 价格表 · Eagle Chemicals EG · Broadcast-StorageTV PE · OT Systems HK 同行 · SageIT MX WDM / OTN · Synergates MA 4V 光端机 · Linkstore OTDR · Net São Jose VC）；线缆 / 周边 / CCTV（YBR · ARG CO · Dynacom EC · Prisa PE · TWM BR · KCS ZA · Catvision OLT · CCL Opto · Gispa（表内突尼斯，域名土耳其语 güvenlik → 国别待核，若为土耳其则下轮复看）· LTE PK · MT Sys · Nomus 路由 · Ofigens）；G-TECH MU 储备。
  · 「stop」flag 来自 STOP_WORDS 文本命中 / Simon 备注，均非客户明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_030.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批30_2026-10-29.md）
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

BATCH = 'G1-30'
DATE = '2026-10-29'
CODES = ["SC-2124", "SC-2125", "SC-2138", "SC-2159", "SC-2162", "SC-2172", "SC-2174", "SC-2175", "SC-2179", "SC-2180", "SC-2181", "SC-2184", "SC-2186", "SC-2188", "SC-2190", "SC-2192", "SC-2193", "SC-2194", "SC-2195", "SC-2196", "SC-2197", "SC-2199", "SC-2200", "SC-2206", "SC-2214", "SC-2221", "SC-2222", "SC-2224", "SC-2229", "SC-2233", "SC-2234", "SC-2245", "SC-2247", "SC-2248", "SC-2250", "SC-2254", "SC-2257", "SC-2269", "SC-2278", "SC-2279", "SC-2281", "SC-2283", "SC-2284", "SC-2285", "SC-2286", "SC-2287", "SC-2289", "SC-2290", "SC-2291", "SC-2292", "SC-2303", "SC-2305", "SC-2306", "SC-2314", "SC-2322"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass（闸 0 刚性补判）----
    'SC-2125': ('pass_final', '巴基斯坦 OK Computers（okcomputers.com.pk 唯一域 no_mx；退信「发不过去」；有 Utepo 的）：退信 + 全部域名死 = 闸 0 刚性 G0-2 → 永久 pass（无任何可达路径）', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-2184': ('keep_C', '印尼 Gain（gain.co.id 域正常；邮件退信 + WA +62 822-9888-8916 发不过去；问工业 488 / 288GW = STI-488DGGPM / STI-288GPM 对位）：真需求 ✔ 但双路不可达 → 留 C 待巡检（巡检取到新地址即转候选）', []),
    'SC-2175': ('keep_C', '哈萨克斯坦 Asterisk（asterisk.kz 域正常；表内俄罗斯 → 国别待核；退信；很多品牌，有 ONV 的商业 PoE / 工业 FS）：进口中国同类 ✔ 但退信 + 无换址 → 留 C 待巡检（通了再转候选）', []),
    'SC-2303': ('keep_C', '毛里求斯 G-TECH Limited（gtechlimited.com；问 1 台 Hirschmann RS20-1700MMM2SDAEHH07；17 推 0 回）：单台替代询问 + 非点名国 + 零回应 → 留 C（储备）', []),
    'SC-2314': ('keep_C', '乌克兰 ITBiz（itbiz.ua / itbiz.com.ua；「全系列引入」）：乌克兰 = 守界（非永久 pass）→ 留 C（局势变化后优先复看）', []),
    'SC-2224': ('keep_C', '乌克兰 Import-Telecom（import-telecom.com；SFP / MC / Switch / CWDM，Planet 的一些产品；15 推 0 回）：乌克兰 = 守界 → 留 C', []),
    'SC-2247': ('keep_C', '乌克兰 Exe（exe.ua；CWDM / SFP / Network）：乌克兰 = 守界 → 留 C', []),
    'SC-2248': ('keep_C', '乌克兰 Infosvyaz（infosvyaz.net.ua；PON 为主）：乌克兰 = 守界 → 留 C', []),
    'SC-2250': ('keep_C', '乌克兰 Lanmarket（lanmarket.ua；有 Utepo 的 / DWDM；2 推）：乌克兰 = 守界 → 留 C', []),
    'SC-2257': ('keep_C', '乌克兰 Svaltera（svaltera.ua / sv-altera.com）：乌克兰 = 守界 → 留 C', []),
    'SC-2254': ('keep_C', '香港 OT Systems（ot-systems.com；自有品牌光路 / 光端机产品线接近；Simon 备注「不再跟进」；6 推 0 回）：同行制造商 → 留 C + dayjob_fit（无客户明确拒绝，不作 pass）', ['dayjob_fit']),
    'SC-2281': ('keep_C', 'Gispa Güvenlik（gispaguvenlik.com；表内「突尼斯」，域名土耳其语 → 国别待核，疑土耳其；主要 CCTV）：若核实为土耳其 = 四主区 → 下轮复看；现无交换机证据 → 留 C', []),
    'SC-2124': ('keep_C', '印尼 Microthings（microthings.id 域正常；退信；有一些工业交换机；1 推）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2186': ('keep_C', '俄罗斯 Indast（indast.ru 域正常；退信；switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2188': ('keep_C', '俄罗斯 IP-Rec（ip-rec.ru 域正常；退信；CCTV + 商业 PoE）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2190': ('keep_C', '越南 KPS（kps.com.vn 域正常；退信；工业 FS / MC / VC / SFP / 机架）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2195': ('keep_C', '俄罗斯 Osbez（osbez-cctv.ru 退信；osbez.ru 正常；MC / SFP / PoE / 同轴 / VC 周边）：备用域在 → 留 C 待巡检（换 osbez.ru 再试）', []),
    'SC-2197': ('keep_C', '俄罗斯 RTK-Teh（rtk-teh.ru 域正常；退信；MC / SFP / 工业 FS，有几个固定合作商）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2199': ('keep_C', '越南 SMCom（smcom.vn 域正常；退信；switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2200': ('keep_C', '印尼 Sunico Data（sunicodata.com 域正常；退信；基本都是 DCN 的）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2233': ('keep_C', '越南 Sytek（sytek.vn 域正常；退信；switch / WDM）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2285': ('keep_C', '巴基斯坦 Netlink（netlink.com.pk 域正常；退信；MC / switch 周边；官网手机 +92 321 9232025）：退信但官网有手机 → 留 C 待巡检', []),
    'SC-2291': ('keep_C', '肯尼亚 True-Tech（true-tech.co.ke 域正常；退信；丰润达 / Comfast 商业 PoE；1 推）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2292': ('keep_C', '巴基斯坦 Vital Group（vitalgroup.com.pk 域正常；退信；CCTV / FS / 大华很多 / 工业 PoE；1 推）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2322': ('keep_C', '沙特 Terrabyt（terrabyt.com 域正常；退信；Dahua）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2138': ('keep_C', '印尼 PT Marsat Windu Andika（mwa.co.id；VC；WA 加不上；1 推）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2159': ('keep_C', '印尼 3kom（3kom.co.id；DWDM network）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2162': ('keep_C', '埃及 Cairo Comm. Systems（ccs.com.eg；SFP / MC / VC 都了解，希望交期短；网站 CCTV 为主；1 推）：本职线为主（MC 可带 STC-110XGE）→ 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2179': ('keep_C', '俄罗斯 dwdm-sfp.ru（DWDM，用的信泰的）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2180': ('keep_C', '秘鲁 Fiber Solutions（fibersolutions.com.pe；MC / SFP（Vivotek）/ 无源周边，电信产品分销）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2181': ('keep_C', '俄罗斯 Fibronics（fibronics.ru；无源 WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2192': ('keep_C', '俄罗斯 MK-F（mk-f.ru；DWDM，瑞斯康达的）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2193': ('keep_C', '俄罗斯 N3com（n3com.ru；DWDM，用瑞斯康达的产品）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2194': ('keep_C', '俄罗斯 Optic-Lines（optic-lines.ru；DWDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2196': ('keep_C', '巴西 RT Evolução（rtevolucao.com.br；FPV drone VC）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2206': ('keep_C', '智利 Octopuss LTDA（octopuss.cl；VC / MC；WA 加不上；1 推）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2214': ('keep_C', '印度 Daccess Security Systems（daccess.co.in；import camera，要 VC 照片 + 价格表；WA 加不上）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2222': ('keep_C', '埃及 Eagle Chemicals（eagle-chemicals.com；HDMI extender / MC / VC，网站类目杂乱）：本职线 + 主业不符 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2245': ('keep_C', '秘鲁 Broadcast-StorageTV（broadcast-storagetv.com；非压缩 HDMI MC，视频音频为主；WA 加不上）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2289': ('keep_C', '墨西哥 SageIT（sageit.com.mx；WDM / OTN）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2290': ('keep_C', '摩洛哥 Synergates（synergates.ma；4V 高清光端机，2023 国际站看了很多家）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2305': ('keep_C', '智利 Linkstore（linkstore.cl；OTDR；WA 加不上）：本职线 / 仪表 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2306': ('keep_C', '巴西 Net São Jose（netsaojose.com.br；VC，wants to buy in Brazil；WA 加不上）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 30 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 991–1045 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：退信 17（域名多正常 → 待巡检）、乌克兰 6（守界）、「品类不符」VC / DWDM / CWDM / 跳线 / CCTV 约 30（俄罗斯 DWDM 集群 = 本职线）、WA 加不上 8、HK 同行 1。口径同桶 ⑥ 首批。候选 0（Gain ID 问工业 488 / 288GW 但邮件 + WA 双退 → 待巡检通了再转；Asterisk KZ 退信待巡检；ITBiz UA 全系列引入 → 守界）；永久 pass 1 = OK Computers（PK，唯一域 no_mx + 退信）。留 C：退信待巡检、乌克兰守界、本职线 dayjob_fit、线缆 / 周边 / CCTV、Gispa 国别待核（疑土耳其 → 下轮复看）、G-TECH MU 储备。「stop」flag / Simon 备注均非客户明确拒绝，不作 pass 依据。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批30_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
