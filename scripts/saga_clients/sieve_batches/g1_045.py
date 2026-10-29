#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 45 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 551–605 户（按综合分序，SC-2773 … SC-2915；综合分 −39 → −52；本批起进入「用户判定不行 / 仅网址无邮箱」密集段）。

构成：仅公司网址无邮箱（Simon 二筛「判定不行 / 不相关」）27、本职线 VC / HDMI / MC / DWDM 个人 16、守界乌克兰 6、印度 CCTV 经销 4、Simon 标记不跟 1、中国大陆 1。
  · 口径：仅网址户 = 路径未建（非闸 0，域名即 URL）→ 默认留 C 待巡检；凡「四主区 / 欧洲 / 先例国 + 在卖中国品牌或自有品牌」→ 标注「找到邮箱即转候选」；自有品牌迹象 → oem_target 备查。
  · 候选 1 = 土耳其 Karel（karel.com.tr；Simon 备注「用的丰润达的」= 已在采购中国 OEM PoE 交换机；Karel 为土耳其本土通信设备品牌厂 → OEM 品牌商 = 首选对象；无邮箱 → 闸 2 先坐实 + 找采购路径；Simon 原判「不行」可否决）。永久 pass 0。
  · 留意：overcam.ru / viethansecurity.com（在卖国内外壳 / 国内牌子，找到邮箱即转候选）、evi-networks.dk / upvel.com（自有品牌迹象 oem_target 备查）、dvicomm.com（美国方案商）、Dacom IL（CEO 具名问 4 / 8 口 PoE，16 推 0 回）、sasantron MY（展会 director 要 price list）。

用法：python3 sieve_batches/g1_045.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批45_2026-10-29.md）
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

BATCH = 'G1-45'
DATE = '2026-10-29'
CODES = ["SC-2773", "SC-2774", "SC-2775", "SC-2776", "SC-2777", "SC-2778", "SC-2779", "SC-2784", "SC-2785", "SC-2787", "SC-2789", "SC-2794", "SC-2795", "SC-2796", "SC-2797", "SC-2798", "SC-2799", "SC-2808", "SC-2810", "SC-2811", "SC-2812", "SC-2818", "SC-2822", "SC-2824", "SC-2825", "SC-2826", "SC-2828", "SC-2830", "SC-2831", "SC-2837", "SC-2838", "SC-2844", "SC-2845", "SC-2848", "SC-2849", "SC-2852", "SC-2853", "SC-2856", "SC-2859", "SC-2862", "SC-2868", "SC-2869", "SC-2871", "SC-2873", "SC-2874", "SC-2876", "SC-2882", "SC-2887", "SC-2888", "SC-2890", "SC-2898", "SC-2902", "SC-2903", "SC-2906", "SC-2915"]

OVERRIDE = {
    'SC-2776': ('candidate', '土耳其 Karel（karel.com.tr 正常；Simon 二筛备注「用的丰润达的」✔ = 已采购中国 OEM 商业 PoE 交换机；Karel = 土耳其本土通信 / 网络设备品牌厂 → OEM 品牌商首选对象；无邮箱）：土耳其四主区 ✔ 自有品牌 + 中国 OEM 在用 ✔ 对位 ✔ 公司可坐实 ✔ → 闸 2 查底数（官网 / MERSİS 镜像）+ 找采购 / OEM 路径（LinkedIn 仅 James）；Simon 原判「不行」→ 可按编号否决', ['oem_target']),
    'SC-2868': ('keep_C', '俄罗斯 Overcam（overcam.ru 正常；商业 PoE，「有国内的外壳」✔；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（俄罗斯点名区 + 在卖中国外壳 → 找到邮箱即转候选；收款待定）', []),
    'SC-2876': ('keep_C', '越南 Việt Hàn Security（viethansecurity.com 正常；MC / SFP / switch 等好几个国内牌子 ✔；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（越南先例 + 中国品牌 → 找到邮箱即转候选）', []),
    'SC-2862': ('keep_C', '俄罗斯 IC-Line（ic-line.ru 正常；MC / Switch / SFP；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（俄罗斯点名区 → 找到邮箱后看）', []),
    'SC-2773': ('keep_C', '意大利 CNIT Consult（cnitconsult.com 正常；商业 PoE；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（欧洲 → 找到邮箱后看）', []),
    'SC-2859': ('keep_C', '美国 DVI Comm（dvicomm.com 正常；telecom networking，「方案商」；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（美国四主区方案商 → 找到邮箱后看）', []),
    'SC-2869': ('keep_C', '法国 PNE（pne.fr 正常；networking，产品线稍杂；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2778': ('keep_C', '美国 Wave Electronics（wave-electronics.com MX 正常但网站打不开；大口 3 层 switch；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（AV 分销，三层大口非 Saga 主线）', []),
    'SC-2871': ('keep_C', '印度尼西亚 Sentralindo（sentralindo.co.id 正常；工业 FS optilinknetwork 的，「分销别人的牌子」；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（印尼无先例，储备）', []),
    'SC-2873': ('keep_C', '俄罗斯 Smartfiber（smartfiber.ru 正常；很多公司之前的产品外壳，网站似乎不更新；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2828': ('keep_C', '泰国 Infitel（infitel.co.th 正常；大口 FS；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2824': ('keep_C', '韩国 Dayou Plus（dayouplus.co.kr 正常；商业机架 / 大口 FS，没啥工业级；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2856': ('keep_C', '印度尼西亚 PT Kejora Gemilang Internusa（kejora.net 正常；ISP；MC / Managed；无邮箱）：ISP 终端 + 无路径 → 留 C 待巡检', []),
    'SC-2874': ('keep_C', '印度尼西亚 Sufi（sufi.co.id 正常；FTTH / 数据中心，没显示明确产品；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检', []),
    'SC-2915': ('keep_C', '沙特 AHB Industrial（ahb-industrial.com nxdomain；fiber tools and testers；无邮箱）：域死 + 无路径 + 品类不符 → 留 C 待巡检（下次仍死即 pass）', []),
    'SC-2837': ('keep_C', '丹麦 EVI Networks（evi-networks.dk 正常；MC 配件 / SFP 等，「有人卖他们的」= 自有品牌迹象；无邮箱）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（欧洲自有品牌 → oem_target 备查；MC / SFP 为本职线）', ['oem_target', 'dayjob_fit']),
    'SC-2902': ('keep_C', 'UPVEL（upvel.com 正常；国别未填；工商业 switch 比较专业；自有品牌网络设备商）：仅公司网址、无邮箱 / 电话 = 路径未建（域名即 URL，非闸 0）→ 留 C 待巡检（自有品牌 → oem_target 备查；国别待核）', ['oem_target']),
    'SC-2898': ('keep_C', 'Control4（control4.com；国别未填 → 美国；智能家居品牌巨头，switch 商业级，「有人卖他们的」）：品牌巨头 → 留 C 巨头', []),
    'SC-2826': ('keep_C', '韩国 Emerson Korea（emerson.kr no_mx；工业 FS；无邮箱）：跨国巨头 → 留 C 巨头', []),
    'SC-2777': ('keep_C', '美国 Santec（santec.com 正常；Optical switch；无邮箱）：光学测试 / 光开关厂商 = 同行 / 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2838': ('keep_C', '美国 Integra Optics（integraoptics.com 正常；SFP / DAC；无邮箱）：光模块品牌商 = 本职线同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2774': ('keep_C', '意大利 / 波兰 Dipol（dipolnet.com 正常；「销售平台，好多个供应商」；无邮箱）：大型分销平台 → 留 C 平台 / 巨头', []),
    'SC-2825': ('keep_C', '台湾 DIYTrade（diytrade.com 正常；B2B 平台；switch 周边）：平台 → 留 C', []),
    'SC-2796': ('keep_C', '乌克兰 Nikolaj Konstantinov（阿里询盘「无人机模块」；无邮箱 / 电话）：守界乌克兰（不 pass，不主动发）→ 留 C；品类不符', []),
    'SC-2818': ('keep_C', '乌克兰 securandvideosys@gmail.com（2 光 2 电小壳）：守界乌克兰（不 pass，不主动发）→ 留 C', []),
    'SC-2845': ('keep_C', '乌克兰 Buycisco（Maxim Kalashnik，gmail；阿里 RFQ「100G 光模块」）：守界乌克兰（不 pass，不主动发）→ 留 C；光模块本职线', ['dayjob_fit']),
    'SC-2887': ('keep_C', '乌克兰 Alexander Dobrydniev（gmail；百兆 SC 单纤 1×9 模块）：守界乌克兰（不 pass，不主动发）→ 留 C；光模块本职线', ['dayjob_fit']),
    'SC-2906': ('keep_C', '乌克兰 Oleg（oleg@mail.ru；fiber lan card）：守界乌克兰（不 pass，不主动发）→ 留 C', []),
    'SC-2849': ('keep_C', '叙利亚 Khaldoon Alwa（hotmail；4ch video converter；WA 加不上）：叙利亚守界 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2903': ('keep_C', '中国大陆 Annie Wang（annietg007@gmail.com；阿里 RFQ「80KM 100G DWDM 模块」）：中国大陆非出口客户 + DWDM 本职线 → 留 C', ['dayjob_fit']),
    'SC-2794': ('keep_C', 'Dacom Advanced Systems Ltd（dacomltd.com 正常；Aviad Shalom CEO，dacom3000@gmail.com；国别未填 → 疑以色列；问了商业 PoE 4 / 8 口 + 上联光 / 电、24V / 48V PoE；介绍 2 光 10 电反馈不多；16 推 0 回）：CEO 具名 + 具体问 ✔ 但 16 推零回应 + 非点名区 → 留 C 储备（换稿一次后看）', []),
    'SC-2831': ('keep_C', '马来西亚 Sasantron（Piratheepan director；yahoo；展会：对 PoE 有兴趣，工商业都要，要 price list / catalog，也去了宇航和旁边展位；+65 号 WA 加不上；1 推）：意向 ✔ 决策人 ✔ 但无域名 + 马来西亚无先例 + Simon 判不行 → 留 C 储备（一页纸一次后看）', []),
    'SC-2844': ('keep_C', '菲律宾 Abet Parungao / LNP farm（gmail；直播进来，询盘了很多不相关产品；Simon 标记不再跟进）：Simon 备注非闸 0 依据 + 非渠道 → 留 C 不主动', []),
    'SC-2779': ('keep_C', '印度 Emerald Green Corporation（Moiz Murad Ali，gmail；buy camera from SZ，interest in VC；WA 加不上）：CCTV 经销 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2784': ('keep_C', '印度 Sanjay Telecom（Sanjay Shah，hotmail；dealers in CCTV & Security products；WA 加不上）：CCTV 经销 → 留 C', []),
    'SC-2785': ('keep_C', '印度 Spy Vision（Ravi Dave，gmail；home security，推过光端机；WA 加不上）：家用安防 → 留 C', []),
    'SC-2787': ('keep_C', '印度 Universal Technologies（M. Surendra，gmail ×2；CCTV / IP Cam / Access control；WA 加不上）：CCTV 经销 → 留 C', []),
    'SC-2795': ('keep_C', '印度 Jignesh Prajapati（仅电话；VC (AHD Analog)；16 推 0 回）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2797': ('keep_C', '印度 P Srinivas（仅电话；VC 要价格；15 推 0 回）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2798': ('keep_C', '印度 Rahul Juneja（仅电话；HDMI 转网，一对买样测试；16 推 0 回）：HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2799': ('keep_C', '印度 Valmik Divase（仅电话；2V1D 模拟视频光端机；16 推 0 回）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2808': ('keep_C', '印度 kanuj304648@gmail.com（Bidi 千兆小外电 60 公里 / HDMI-DVI 转光）：MC / HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2811': ('keep_C', '印度 Satish Kumar（s76344196@gmail.com；Bidi 千兆小外电 / HDMI-DVI 转光）：MC / HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2775': ('keep_C', '俄罗斯 Darlene Moses（fatskayv@hotmail.com；2022 年光猫，问公司规模；WA 加不上）：光猫本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2789': ('keep_C', '埃及 Redaabdelmoez（engredasmart@gmail.com；HDMI extender）：HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2810': ('keep_C', '埃及 Omar Naur（omnd2009@hotmail.com；VC）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2812': ('keep_C', '孟加拉 MD Saidul（saidulbr@gmail.com；10 对光猫，RMB）：光猫本职线 + RMB 待 Simon → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2822': ('keep_C', '巴基斯坦 Muhammad Hammad（阿里询盘「DWDM」；无邮箱 / 电话）：阿里后台可回 + DWDM 本职线 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2830': ('keep_C', '澳大利亚 Mark Andrew Cowan（gmail；HDMI extender 2 对 PW-DT209 只要接收机；WA 加不上）：HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2848': ('keep_C', '菲律宾 Lee Jane Abadiano（crymton@gmail.com；Skype；Cat5e/6 VGA KVM Extender 300m）：KVM 延长本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2852': ('keep_C', '斐济 Atish Nand（tsh.netcracker@live.com；AHD / CVI / TVI；WA 可加但一直不看）：AHD 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2853': ('keep_C', '缅甸 Vicheka Nouv（gmail；HDMI 转光）：HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2882': ('keep_C', '巴西 Flavio Ferreira（gmail；HDMI extender）：HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2888': ('keep_C', 'Peter Gazda / NST CCTV（nstcctv@gmail.com；国别未填；buying VC from OB Technology）：VC 本职线 + 同行在供 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2890': ('keep_C', 'rusadze@gmail.com（国别未填 → 疑格鲁吉亚；问级联光端机，发了级联规格书）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 45 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 551–605 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：仅网址无邮箱 27、本职线个人 16、守界乌克兰 6、印度 CCTV 经销 4、Simon 标记不跟 1、中国大陆 1。候选 1 = 土耳其 Karel（用丰润达 OEM → 品牌商对象，闸 2 先找路径）。永久 pass 0。', '',
         '> 值得留意的留 C：overcam.ru / viethansecurity.com / ic-line.ru（找到邮箱即转候选）、evi-networks.dk / upvel.com（oem_target 备查）、dvicomm.com US（方案商待巡检）、Dacom Advanced Systems（CEO 问 PoE，零回应）、sasantron MY（展会意向，无域名）、Karel 原为 Simon「判定不行」→ 已改候选可否决。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批45_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
