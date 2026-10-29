#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 40 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 276–330 户（按综合分序，SC-2044 … SC-2232；综合分 −4 → −10，低分段）。

构成：群发冷名单（免费邮箱，多数无公司域名）38（WA 加不上 10、2007–2013 年陈旧 9）、展会 / WA 接触 6（Norman Tan SG、Dinesh Wagh AE、Abdulrahman SA、Nguyen VN、Nadhimentera MY、Shinho IN）、阿里巴巴 / 自建站个人 8、阿里询盘无联系方式 1（Smart Marine TR，阿里后台可回 → 非闸 0）、机构 2（Ooredoo TN 巨头、Fiji National University 学校）。
  · 口径同第 36–39 批；本批免费邮箱个人为主，仅两家印度公司域名 + 点名中国品牌 / 真实回复 → 候选。
  · 候选 2 = 印度 Round Robin Tech（分销商，「有需求会说」= 真回；Pradeep Patel Regional 具名）/ 印度 Hanutech Solution（switch / MC / CCTV，丰润达的商业 PoE）。永久 pass 0。
  · 留意：Norman Tan SG（几个工业交换机型号，常在 WA 沟通，16 推 0 回，无公司）、Nguyen VN（要了中文价格册，商业品需求大，无公司）、Systec Control MX（8V1D 100 对 = 本职线有量）、Smart Marine TR（Elink 注入器，无直接联系方式）。

用法：python3 sieve_batches/g1_040.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批40_2026-10-29.md）
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

BATCH = 'G1-40'
DATE = '2026-10-29'
CODES = ["SC-2044", "SC-2045", "SC-2049", "SC-2051", "SC-2052", "SC-2057", "SC-2060", "SC-2073", "SC-2074", "SC-2075", "SC-2076", "SC-2080", "SC-2082", "SC-2086", "SC-2087", "SC-2093", "SC-2103", "SC-2108", "SC-2126", "SC-2128", "SC-2129", "SC-2134", "SC-2137", "SC-2141", "SC-2142", "SC-2144", "SC-2145", "SC-2146", "SC-2147", "SC-2149", "SC-2150", "SC-2151", "SC-2152", "SC-2153", "SC-2154", "SC-2156", "SC-2170", "SC-2177", "SC-2183", "SC-2189", "SC-2201", "SC-2202", "SC-2203", "SC-2204", "SC-2205", "SC-2208", "SC-2209", "SC-2210", "SC-2212", "SC-2216", "SC-2217", "SC-2220", "SC-2225", "SC-2231", "SC-2232"]

OVERRIDE = {
    'SC-2154': ('candidate', '印度 Round Robin Tech（roundrobintech.com 正常；Pradeep Patel Regional 具名，gmail；「分销商，有需求会说」= 真实回复 ✔；另有 Bakhtavar Usmani）：印度先例 ✔ 分销对位 ✔ 真回 ✔ 公司坐实路径 ✔ → 闸 2 查底数（MCA 镜像）后一页纸（STC-028GP / STC-2224GP 价格锚）', []),
    'SC-2208': ('candidate', '印度 Hanutech Solution（hanutechsolution.com 正常；gmail + 公司邮箱；switch / MC / CCTV 等；丰润达的商业 PoE ✔）：点名中国品牌 ✔ 印度先例 ✔ 对位 ✔ 可达 ✔ → 闸 2 查底数（MCA 镜像）后一页纸', []),
    'SC-2152': ('keep_C', '突尼斯 Ooredoo（ooredoo.tn；员工 gmail；要 catalog）：巨头运营商 → 留 C 巨头（不 pass）', []),
    'SC-2205': ('keep_C', '斐济 Fiji National University（gmail；WA 加不上）：学校终端 → 留 C', []),
    'SC-2183': ('keep_C', '希腊 Gadgetmou（gadgetmou.com 正常；gmail；主要 CCTV 类，销售平台好多供应商）：平台型 → 留 C', []),
    'SC-2141': ('keep_C', '土耳其 Smart Marine（Kurman；阿里巴巴询盘「Elink PoE Injector」；无邮箱 / 电话）：阿里后台可回 = 路径存在（非闸 0）+ 注入器 Saga 不供 → 留 C 待巡检', []),
    'SC-2151': ('keep_C', '新加坡 Norman Tan（gmail；几个工业交换机型号；「常在 WA 上沟通」；16 推 0 回）：WA 可达 ✔ 工业对位 ✔ 但无公司 + 零回应 → 留 C 储备（WA 一页纸一次后看）', []),
    'SC-2210': ('keep_C', '越南 Nguyen（nguyendinhhuanhd@gmail.com；要了价格册 / 中文报价，「商业品需求大」）：需求 ✔ 但无公司 / 无域名 → 留 C 储备（来询即报，坐实公司后转候选）', []),
    'SC-2204': ('keep_C', '阿联酋 Dinesh Wagh（CEO；仅电话；PoE switch；16 推 0 回）：无公司 + 零回应 → 留 C', []),
    'SC-2201': ('keep_C', '沙特 Abdulrahman（仅电话；Switch；16 推 0 回）：无公司 + 零回应 → 留 C', []),
    'SC-2052': ('keep_C', '马来西亚 Nadhimentera Engineering（Shamsul Kamal director；gmail；做 CCTV / IP，着重问 SFP 多模 + 1×9 模块）：光模块本职线 + 马来西亚无先例 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2217': ('keep_C', '印度 Shinho India（shinhoindia.com no_mx；A.V. Venkat，gmail；问台式 EDFA，名片 PON / OTDR 类）：PON / OTDR / EDFA 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2209': ('keep_C', 'msp1145@gmail.com（国别未填；bypass (PoE / no PoE)、工业 PoE 4 / 8 口；16 推 0 回）：个人 + bypass 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2080': ('keep_C', '巴基斯坦 Industrial Process Solutions（industrialprocesssolutions.com 正常；MD Rafi Distributor，gmail；2013 年询盘 CTCU 设备）：分销商 ✔ 但 2013 陈旧 + 需求不对位 → 留 C 储备', []),
    'SC-2128': ('keep_C', '巴基斯坦 Combine Networks（combinenetworks.net 正常；Hamid Jalal CEO，gmail / Skype；8ch HD information）：CCTV 视频 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2137': ('keep_C', '印度 KB Infotech（litecrop.com no_mx；Kulbhushan Rana，gmail，微信 KbRana84；无需求记录）：零信息 → 留 C', []),
    'SC-2145': ('keep_C', '印度 Fiber India（fiberindia.in 正常；gmail；optical 相关）：光纤本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2144': ('keep_C', '孟加拉 Dahua BD（dahuabd.com 正常；gmail；主要分销大华）：大华分销 + 孟加拉无先例 → 留 C 储备', []),
    'SC-2146': ('keep_C', '埃及 Hiteknofal（hiteknofal.com 正常；Mohamed Karam，gmail；转发过我方帖子 ✔）：社媒互动 ✔ 但无需求 + 埃及无先例 → 留 C 储备', []),
    'SC-2189': ('keep_C', '泰国 KBK Solution（kbksolution.com nxdomain；gmail；SW33026FM；「是个买手」）：买手 + 域死 → 留 C', []),
    'SC-2231': ('keep_C', '韩国 SPICT（spict.co.kr 正常；naver；WDM，用 packet light 的）：WDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2108': ('keep_C', '菲律宾 SGTECH（Stephen Gala，yahoo；4V CVI Distributor / Wholesaler，12 年阿里）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2134': ('keep_C', '亚美尼亚 IDS CJSC（Lyon Khoukaz，gmail ×2；VC 1V1E 小尺寸；1 推）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2232': ('keep_C', '墨西哥 Systec Control（gmail；2023 年「8V1D 100 对」）：视频光端机 100 对 = 本职线有量 → 留 C + dayjob_fit（墨西哥先例在，本职线优先）', ['dayjob_fit']),
    'SC-2220': ('keep_C', '危地马拉 Covima（Georges Hanna，hotmail；2007 年「8V 1080P」）：VC 本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2203': ('keep_C', '柬埔寨 CamTV（Savay Keo，yahoo；2009 年「16 路 3G-SDI」；WA 加不上）：SDI 本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2212': ('keep_C', '马里 / 法国 BONZI TELECOM（Tiecoro Traore，hotmail；2018 年光模块 + 很多杂乱产品）：光模块本职线 + 杂 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2216': ('keep_C', '津巴布韦 Pito Investments（Timothy Nunu，gmail；RFQ「RS232 单模光猫」；WA 加不上）：光猫本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2057': ('keep_C', '沙特 Topnet（Abdullatheef，hotmail；Gigabit MC with MM SFP；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2051': ('keep_C', '澳大利亚 Misal Technologies（Manfred Mayboehm，bigpond；MC，网站不太相关；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2142': ('keep_C', '印度尼西亚 CV. Heksa Utama Karya（Wisnu Baroto，yahoo；MC / passive components；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2150': ('keep_C', '加拿大 Milo Constantino（telus.net；问了光缆检测和 MC；14 推 0 回）：光缆检测 / MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2044': ('keep_C', '沙特 Hamrabi Trading（yahoo；take catalog, interested in China；WA 加不上）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2045': ('keep_C', '孟加拉 IT services / Majed & Co.（yahoo / gmail；要 PoE 管理）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2049': ('keep_C', '印度 MARZ SYSTEMS INDIA（gmail；模块 / Ethernet Converter / switch；2 推 0 回）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2060': ('keep_C', '印度 WTI（Anba，gmail；fiber switch 1 RJ45 + 6 SC）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2082': ('keep_C', '马来西亚 NN MAJU Enterprise（Wan Shahrizan，gmail；4 光 4 电 PoE managed；陈旧）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2126': ('keep_C', '以色列 Quasar（Eyal Shmueli QA manager，gmail；2007 年国际站；WA 加不上；查不到信息）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2129': ('keep_C', '科特迪瓦 CONNEXUS SARL（gmail；2021 年 RFQ 24 口商业 PoE；WA 加不上）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2170': ('keep_C', '沙特 Seven Bridges Security Systems（Mohammad Riyaz，gmail；2 个 1 光 4 SFP 小壳；WA 加不上；8 推 0 回）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2202': ('keep_C', 'CV. MORA ABADI TECHNIK（国别未填 → 疑印尼；Paian Sitompul，gmail；21 年国际站）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2086': ('keep_C', '美国 Alan Elman（aol；报了工业 2 光 8 电）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2087': ('keep_C', '美国 Mehrdad Alimard（yahoo；4 光 8 电工业网管及 SFP 模块）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2103': ('keep_C', '美国 Jay Anast（yahoo；2010 年「2+4 全网千兆 PoE」）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2093': ('keep_C', '英国 Gautam Rathod（hotmail；2020 年「千兆 PoE 延长器 1 分 4」）：延长器非 Saga 线 → 留 C', []),
    'SC-2177': ('keep_C', '波兰 Dariusz Rusiecki（gmail；2013 年「1 光 8 10G 光，2.5G 网」；WA 加不上）：个人 + 2.5G 口径待 SB-263 → 留 C', []),
    'SC-2147': ('keep_C', '巴基斯坦 Hedayat Ali（gmail；问过 2 光 8 管理，嫌贵）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2149': ('keep_C', '菲律宾 Oren Maturan（gmail；还想要收发器；19 年阿里，类目不太相关）：收发器本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2153': ('keep_C', '南非 Ronald Msimango（gmail；用 PoE 比较多，问了 DIN PoE）：南非先例在但个人无公司 → 留 C 储备（坐实公司后看）', []),
    'SC-2225': ('keep_C', '澳大利亚 Jawn Looi（hotmail；2013 年 PoE injector 相关）：注入器 Saga 不供 → 留 C', []),
    'SC-2073': ('keep_C', '阿尔及利亚 Riad（自建站「光开关」；gmail）：光开关本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2074': ('keep_C', '印度 rstmastboy@gmail.com（RFQ「无人机」）：品类不符 → 留 C', []),
    'SC-2075': ('keep_C', '沙特 Shajahan Azeez（gmail；2013 年「4P1E」询盘）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2076': ('keep_C', '布基纳法索 Souleymane Kabore（RFQ「Solar Power System」）：品类不符 → 留 C', []),
    'SC-2156': ('keep_C', '喀麦隆 Josue Tele Youbi（询盘「千兆内电单纤」；gmail）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
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
    L = [f'# C 池 · 闸 1 · 第 40 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 276–330 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：群发冷名单（免费邮箱）38、展会 / WA 接触 6、阿里巴巴 / 自建站个人 8、阿里询盘无联系方式 1、机构 2。候选 2 = 印度 Round Robin Tech（分销商真回 + 决策人具名）+ 印度 Hanutech Solution（丰润达渠道 + 公司域名）。', '',
         '> 值得留意的留 C：Norman Tan SG（WA 常聊，工业型号，无公司）、Nguyen VN（中文价格册，需求大，无公司）、Industrial Process Solutions PK（分销商，2013 陈旧）、Systec Control MX（8V1D 100 对 → 本职线）、Hiteknofal EG / Tac-Tic 同类（转发过帖子）、Smart Marine TR（阿里后台可回，非闸 0）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批40_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
