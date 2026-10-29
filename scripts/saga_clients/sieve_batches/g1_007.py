#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 07 批（2026-10-29）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 276–385 户（按编号序，SC-2244 … SC-285）。

这一段的主体是 Simon 早年标「用户判定不行 / 不相关」的欧美经销商名单 —— 但表内备注恰恰写着「在卖 Utepo / 洪瑞 / ONV / Witek / hasivo / 3onedata / Atop / Planet 的」，
= 现成的中国白牌进口商（目标顺位第 2），按 U117 口径 必须重判：
  · 候选 = 已在卖中国同类品牌（进口经验）或 自有品牌 / 分销主体，且在四主区 / 欧洲 / 波兰 → 进闸 2 查底数；Simon 曾判不行的一律在理由里注明「可否决」。
    洪瑞（HRUI）现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线），理由注明。
  · 永久 pass 仅 2：SC-235 Bravour（充电家具品牌，纯无关 + 零互动）、SC-2620 ata98.es（域名 NXDOMAIN + 邮件 fail + 无电话 = G0-2 同款，闸 0 因状态字段漏判）。
  · 其余留 C：巨头 / 守界 / 同行 / 终端 / 平台 / 光端机-WDM 类（dayjob_fit）/ 死域名待巡检。

用法：python3 sieve_batches/g1_007.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批07_2026-10-29.md）
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

BATCH = 'G1-07'
DATE = '2026-10-29'
CODES = ["SC-2244", "SC-2255", "SC-2256", "SC-2258", "SC-2260", "SC-2262", "SC-227", "SC-2282", "SC-233", "SC-2339", "SC-234", "SC-235", "SC-2357", "SC-236", "SC-237", "SC-238", "SC-2383", "SC-239", "SC-2393", "SC-2395", "SC-2397", "SC-2402", "SC-241", "SC-2418", "SC-2425", "SC-2429", "SC-243", "SC-2445", "SC-245", "SC-246", "SC-2469", "SC-247", "SC-2488", "SC-249", "SC-250", "SC-251", "SC-2515", "SC-2517", "SC-252", "SC-2535", "SC-254", "SC-2542", "SC-2543", "SC-2548", "SC-2573", "SC-2593", "SC-2597", "SC-2599", "SC-2600", "SC-2601", "SC-2603", "SC-2604", "SC-2606", "SC-2608", "SC-2609", "SC-2611", "SC-2612", "SC-2617", "SC-2618", "SC-2619", "SC-2620", "SC-2622", "SC-2625", "SC-2626", "SC-2630", "SC-2633", "SC-2634", "SC-264", "SC-2642", "SC-2657", "SC-2662", "SC-2663", "SC-2668", "SC-268", "SC-2699", "SC-2701", "SC-2706", "SC-2707", "SC-271", "SC-2711", "SC-2718", "SC-2719", "SC-272", "SC-2720", "SC-2721", "SC-2722", "SC-2723", "SC-2725", "SC-2726", "SC-2728", "SC-273", "SC-274", "SC-2743", "SC-2754", "SC-2757", "SC-276", "SC-2760", "SC-2767", "SC-277", "SC-2780", "SC-2782", "SC-2786", "SC-2802", "SC-2809", "SC-2813", "SC-2820", "SC-2832", "SC-2834", "SC-284", "SC-285"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-235': ('pass_final', '英国 Bravour®（充电柜 / 充电车 / 讲台等空间与充电家具品牌；站内 switch / PoE 词仅为充电方案配件）表内无兴趣记录、零互动 → 纯无关行业，永久 pass', []),
    'SC-2620': ('pass_final', '西班牙 ata98.com：域名 NXDOMAIN + 邮件 fail + 无电话 / 无 WA / 零互动 = G0-2 同款（闸 0 因状态字段「用户判定不行」漏判）→ 永久 pass', []),
    # ---- 候选 → 闸 2（进口经验 / 自有品牌 / 分销主体）----
    'SC-2255': ('candidate', '美国 PoE Texas（poetexas.com；在亚马逊上卖 Utepo 商业 PoE）：美国主区 + 已进口中国同类品牌 + 对位 ✔；8 推 0 回 → 闸 2 查底数' + VETO, []),
    'SC-2256': ('candidate', '意大利 Redfox S.r.l.（工商业 PoE 用 Utepo 的）：欧洲 + 已进口中国同类品牌 + 对位 ✔；14 推 0 回 → 闸 2 查底数' + VETO, []),
    'SC-2258': ('candidate', '意大利 Townet（用 hasivo 的，安防 + 工业 FS）：欧洲 + 已进口中国同类品牌 + 对位 ✔；9 推 0 回 → 闸 2 查底数' + VETO, []),
    'SC-2260': ('candidate', '意大利 videosorveglianza.it（商业 PoE：ONV / 洪瑞 / Witek 等多个国内牌子）：欧洲 + 多品牌进口经验 + 对位 ✔；14 推 0 回 → 闸 2 查底数' + Q33 + VETO, []),
    'SC-2262': ('candidate', '德国 1st-embedded / supersrv.de（ISON 的，少量工业电口）：德国主区 + 已进口中国工业品牌；3 推 0 回 → 闸 2 查底数，低优先' + VETO, []),
    'SC-2383': ('candidate', '英国 3G Router Store（商业 PoE 主要是洪瑞的）：英国主区 + 已进口同供应链产品 + 对位 ✔；18 推 0 回 → 闸 2 查底数' + Q33 + VETO, []),
    'SC-2402': ('candidate', '美国 Siseg USA（Utepo 的商业 PoE）：美国主区 + 已进口中国同类品牌 + 对位 ✔；19 推 0 回 → 闸 2 查底数' + VETO, []),
    'SC-2418': ('candidate', '加拿大 / 美国 Streakwave（卖很多牌子：商业 PoE / 工业 FS / SFP；北美无线 + 网络大分销）：北美主区 + 分销主体 + 对位 ✔；1 推 0 回 → 闸 2 查底数（体量偏大）' + VETO, ['dayjob_fit']),
    'SC-2429': ('candidate', '美国 Epcom（El Paso；Syscom 美方；约 100 人；PLANET 商用 + 工业两线备货、Wi-Tek 在用；研究档对位 STC-424DGGM）：美国主区 + 分销主体 + 对位 ✔；8 推 0 回 → 闸 2 查底数' + VETO, []),
    'SC-2488': ('candidate', '德国 fiber24.net（光路 / Planet 的 / 工业 FS 很多牌子）：德国主区 + 多品牌分销 + 对位 ✔；8 推 0 回 → 闸 2 查底数' + VETO, ['dayjob_fit']),
    'SC-2542': ('candidate', '美国 Grid Connect, Inc.（Naperville IL；Atop 的；表内完整地址 + 直线电话）：美国主区 + 工业网络分销主体（Atop 等）+ 对位 ✔；互动过 → 闸 2 查底数' + VETO, []),
    'SC-2597': ('candidate', '美国 cctv.supplies / cctv.nyc（商业 PoE 主要是洪瑞的）：美国主区 + 已进口同供应链产品 + 对位 ✔；20 推 0 回 → 闸 2 查底数' + Q33 + VETO, []),
    'SC-2606': ('candidate', '美国 Logicbus（Atop / 三旺 3onedata 工业 FS 电口）：美国主区 + 已进口中国工业品牌 + 对位 ✔；20 推 0 回 → 闸 2 查底数' + VETO, []),
    'SC-2608': ('candidate', '英国 Mayflex（Sonepar 旗下大型布线 / 安防 / 网络分销，自有品牌 Excel Networking；商业 PoE）：英国主区 + 分销 + 自有品牌 ✔；19 推 0 回 → 闸 2 查底数（体量偏大）' + VETO, ['oem_target']),
    'SC-2609': ('candidate', 'Partizan Store（partizanstore.eu，国别未填；商业 PoE 主要是洪瑞的）：欧洲 + 已进口同供应链产品；17 推 0 回 → 闸 2 先定国别再查底数，低优先' + Q33 + VETO, []),
    'SC-2619': ('candidate', '美国 Alantek USA（布线品牌 Alantek 美国站；工业 FS / PoE / MC 周边）：美国主区 + 自有品牌线（推定贴牌）→ 闸 2 查底数核自有品牌，低优先' + VETO, ['oem_target', 'dayjob_fit']),
    'SC-2622': ('candidate', '美国 cctvvideo.com（VC / SFP / 工业 FS，有 e-link 的）：美国主区 + 已进口中国品牌 e-link；→ 闸 2 查底数，低优先' + VETO, ['dayjob_fit']),
    'SC-2633': ('candidate', '西班牙 Sisecam（工业 FS；Axis 及其他牌子的分销商；邮件 fail）：欧洲 + 分销主体 + 对位 ✔ → 闸 2 查底数 + 找新地址' + VETO, []),
    'SC-2657': ('candidate', '美国 Lynn Electronics（MC / switch / SFP，从 VOLKTEK 买 MC）：美国主区 + 进口经验（台湾 Volktek）+ 自有品牌连接产品 → 闸 2 查底数；11 推 0 回' + VETO, ['dayjob_fit']),
    'SC-2718': ('candidate', '西班牙 Mercasat（商业 PoE 好几种外壳、好多家国内的牌子）：欧洲 + 多品牌进口经验 + 对位 ✔ → 闸 2 查底数，低优先' + VETO, []),
    'SC-2725': ('candidate', '西班牙 Todotelecom（商业 PoE 为主、好多种外壳、销售平台；网站有 WA 按钮）：欧洲 + 多品牌进口经验 + 对位 ✔ → 闸 2 查底数，低优先' + VETO, []),
    'SC-2728': ('candidate', '英国 Blue Helix（主要卖 AMG / Comnet 工业以太网）：英国主区 + 工业网络分销主体 + 对位 ✔；19 推 0 回 → 闸 2 查底数' + VETO, []),
    'SC-274': ('candidate', '挪威 Alcadon（北欧布线 / 网络分销集团，很多 Planet 产品，CWDM）：欧洲 + 分销主体 + 对位 ✔；10 推 0 回 → 闸 2 查底数（体量偏大）', ['dayjob_fit']),
    'SC-276': ('candidate', '波兰 Assmann（ASSMANN / DIGITUS 品牌集团波兰公司；表内「很大的一个公司，由国内较多合作商」）：波兰次主区 + 自有品牌 DIGITUS（贴牌中国）→ 闸 2 查底数（宜同时核德国总部口径）', ['oem_target']),
    'SC-2760': ('candidate', '西班牙 Tempel Group（Moxa 分销；工业电子分销集团）：欧洲 + 工业网络分销主体 + 对位 ✔ → 闸 2 查底数' + VETO, []),
    'SC-2802': ('candidate', '英国 Euro Security Solutions Ltd（展会：很在意 AC/DC 输入、问 VC 用法、要 full info、想拿样；邮件退信）：英国主区 + 样品意向 + 对位 ✔ → 闸 2 查底数 + 找新地址，低优先' + VETO, ['dayjob_fit']),
    'SC-2809': ('candidate', '英国 Ogar Technology（商业 PoE 看着像 ONV 的；退信）：英国主区 + 疑似进口中国品牌 + 对位 ✔；17 推 0 回 → 闸 2 查底数 + 找新地址，低优先' + VETO, []),
    'SC-2832': ('candidate', '加拿大 SA Store / Smart Access（商业 PoE 国内的外壳、CCTV；退信）：北美主区 + 进口经验 + 对位 ✔ → 闸 2 查底数 + 找新地址，低优先' + VETO, []),
    'SC-2834': ('candidate', '波兰 Dipol（大型安防 / 光纤 / 网络分销，自有品牌 Ultipower 等；IFSEC 参展；VC / MC / SFP / 工业 FS）：波兰次主区 + 分销 + 自有品牌 ✔ → 闸 2 查底数' + VETO, ['oem_target', 'dayjob_fit']),
    'SC-284': ('candidate', '美国 DCB（Data Comm for Business；有自己一套型号、产品多、「感觉还行」）：美国主区 + 自有品牌网络设备（推定部分贴牌）→ 闸 2 查底数；19 推 0 回', ['oem_target']),
    # ---- 需要专门说明的留 C ----
    'SC-2699': ('keep_C', '意大利 Rexel Italia（Gigamedia 为其自有品牌商业 PoE）→ Rexel = 全球电气分销巨头：自有品牌有既定采购体系，按 U117 不 pass；留 C（oem 线索备查）', ['oem_target']),
    'SC-2599': ('keep_C', '丹麦 EET Group（北欧 IT 分销巨头；Planet 设备很多、CWDM / SFP）→ 巨头不 pass；留 C', ['dayjob_fit']),
    'SC-2612': ('keep_C', '英国 Veracity（自研 PoE 延长 / 交换产品品牌商）→ 同行 / 自有设计；留 C', []),
    'SC-2611': ('keep_C', '美国 Valiant Communications（多国办事处、自有产品线广）→ 厂商 / 同行；留 C', []),
    'SC-2630': ('keep_C', '土耳其 kep.tr（洪瑞的商业 PoE；域名已 dead、无退信记录）→ 不满足 G0-2（无退信）；留 C，下次巡检官网 / 社媒也死即 pass', []),
    'SC-2720': ('keep_C', '英国 netbit.biz（商业 PoE；域名 dead、无退信记录）→ 不满足 G0-2；留 C，巡检后再定', []),
    'SC-2573': ('keep_C', '美国 ICC Networking（用 hinet 的；域名无 MX、2 个邮箱 fail）→ 邮件已死但官网未核；留 C，巡检后再定', []),
    'SC-2780': ('keep_C', '美国 Fiber Optic Xpress（域名 NXDOMAIN、WA 加不上、工具类询盘）→ 无退信记录不满足 G0-2；留 C，巡检后再定', []),
    'SC-2767': ('keep_C', '立陶宛 SOMI RT（MC；域名 NXDOMAIN、电话加不上）→ 与 SC-1629 Somi Networks 疑似同源，并线核对后再定；留 C', ['dayjob_fit']),
    'SC-2668': ('keep_C', 'A&M Corporación（表内美国；域名 NXDOMAIN、WA 加不上、要价极低）→ 无退信记录；留 C，巡检后再定', []),
    'SC-2786': ('keep_C', '美国 Staley, Inc.（TA210-FE/A2 ×500 pcs 询盘 = 光端机 / 收发器类型号；电话加不上）→ 品类 Saga 不供但数量大（本职可参考）；留 C', ['dayjob_fit']),
    'SC-2515': ('keep_C', '匈牙利 NBSZ（nbsz.gov.hu = 国家安全特勤局；模拟光端机；退信）→ 守界公共安全 + 光端机；留 C', ['dayjob_fit']),
    'SC-2517': ('keep_C', '美国 Rakers Automation（要 UL 证书；Simon 注「后边不用跟」）→ 无 UL 不对位，我方决定不跟；留 C', []),
    'SC-2535': ('keep_C', '加拿大 Aartech（TRENDnet 零售）→ 品牌零售无白牌进口证据；Simon 判不行；留 C', []),
    'SC-2397': ('keep_C', '拉脱维亚 drosibai.lv（PoE 配件销售平台）→ 平台型无 KP；Simon 判不行；留 C', []),
    'SC-238': ('keep_C', 'dustin.fi + dolphin.com.bd（表内误并两家：Dustin 北欧上市巨头 / Dolphin 孟加拉网店）→ 巨头 + 区域外；留 C（待拆分）', []),
    'SC-2723': ('keep_C', '德国 RTSB Group（铁路货运物流集团，「有可能需求 5 / 8 / 16 电口」）→ 终端用户自用；留 C（来询被动报价）', []),
    'SC-2813': ('keep_C', '意大利 SIO S.p.A.（展会：Ubiquiti 用户、要 Passive PoE 输入；名片 Enrico Butera；退信）→ Passive PoE 不供 + 退信；留 C', []),
    'SC-2820': ('keep_C', '德国 Technica Engineering（车载以太网测试设备厂商；一些 MC 和 switch；退信）→ 同行 / 车载守界；留 C', ['dayjob_fit']),
    'SC-2282': ('keep_C', '土耳其 isee.com.tr / asyatelekom（商业 PoE 好几种外壳）→ 疑似多家国内货但无品牌证据；2 推 0 回；留 C（土耳其主区，巡检有新信号再升候选）', []),
    'SC-2395': ('keep_C', '英国 CCTV Direct（CCTV 为主、很多外壳）→ 安防网店无明确进口品牌证据；19 推 0 回；留 C', ['dayjob_fit']),
    'SC-2662': ('keep_C', '土耳其 Tekmarshop（商业 PoE 好几个牌子）→ 网店、无明确品牌证据；留 C', []),
    'SC-249': ('keep_C', '克罗地亚 Sartura（嵌入式 Linux / OpenWrt 工程服务；Marvell 平台板）→ 软件工程服务不经销硬件，但与网络设备相关（样机 / 合作可能）；留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 07 批（{DATE}）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 276–385 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 这一段主体是 Simon 早年标「用户判定不行 / 不相关」的欧美经销商 —— 表内备注却写着「在卖 Utepo / 洪瑞 / ONV / Witek / hasivo / 3onedata / Atop / Planet 的」= 现成的中国白牌进口商（目标顺位第 2），按 U117 必须重判，所以候选偏多（30）。'
         '**每一户理由末尾都标了「可否决」，Simon 回编号即可。** 洪瑞现供客户（videosorveglianza / 3G Router Store / cctv.supplies / Partizan）按 Q-33 口径默认只推 SmartByte / Marvell 管理 + 工业线。'
         ' 永久 pass 2：Bravour（充电家具品牌）、ata98.es（域名 NXDOMAIN + 邮件 fail + 无电话，闸 0 漏判）。5 户「域名已死但无退信记录」留 C 等巡检。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批07_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
