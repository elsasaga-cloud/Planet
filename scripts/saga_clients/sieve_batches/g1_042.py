#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 42 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 386–440 户（按综合分序，SC-2364 … SC-2502；综合分 −16 → −23，桶尾低分段）。

构成：群发冷名单免费邮箱个人 30（WA 加不上 8；本职线 VC / MC / SFP / 光开关 / DWDM / OTN 14）、阿里询盘「无联系方式」（后台可回）8、守界（乌克兰 6、伊朗 4）10、土耳其展会微信无名户 2、仅电话 2、退信 2（均有备用路径 → 非刚性）。
  · 口径同第 36–41 批。本批无一户同时满足「公司名 / 域名 + 先例国或四主区 + 对位产品 + 可达」四条 → 候选 0；两条退信（SC-2419 域名存活、SC-2436 有电话）均非闸 0 刚性 → 永久 pass 0。
  · 留意：Visioncop VN（很多国内牌子商业 PoE，gmail 退信但 visioncop.com 存活 → 官网找到邮箱即转候选）、GRUPO EBX PE（工业 1 光 1 SFP 24 台，仅阿里后台）、omnet78 IN（1 光 4 工业小壳 MOQ / 价格册 / 交期，无公司）、Anvar（+993 土库曼，SNR SFP 量大 = 本职线）、Fibercom PK（「和珊姐对接了」= 内部分工，非 pass 依据）。

用法：python3 sieve_batches/g1_042.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批42_2026-10-29.md）
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

BATCH = 'G1-42'
DATE = '2026-10-29'
CODES = ["SC-2364", "SC-2369", "SC-2371", "SC-2375", "SC-2377", "SC-2378", "SC-2380", "SC-2381", "SC-2382", "SC-2390", "SC-2391", "SC-2394", "SC-2400", "SC-2404", "SC-2406", "SC-2407", "SC-2408", "SC-2411", "SC-2412", "SC-2414", "SC-2415", "SC-2417", "SC-2419", "SC-2420", "SC-2422", "SC-2424", "SC-2426", "SC-2427", "SC-2430", "SC-2435", "SC-2436", "SC-2439", "SC-3325", "SC-2444", "SC-2447", "SC-2450", "SC-2451", "SC-2453", "SC-2456", "SC-2457", "SC-2459", "SC-2460", "SC-2461", "SC-2462", "SC-2466", "SC-2467", "SC-2468", "SC-2472", "SC-2473", "SC-3326", "SC-2487", "SC-2491", "SC-2492", "SC-2498", "SC-2502"]

OVERRIDE = {
    'SC-2419': ('keep_C', '越南 Visioncop（visioncop.com 正常；visioncop.it@gmail.com 退信；很多国内的牌子商业 PoE ✔）：越南先例 ✔ 中国品牌 ✔ 对位 ✔ 但唯一邮箱退信 → 留 C 待巡检（官网找到邮箱即转候选；域名存活 = 非刚性）', []),
    'SC-2420': ('keep_C', '秘鲁 GRUPO EBX E.I.R.L（Carlos Chavez E.；阿里询盘「工业千兆 1 光 1 SFP 24 台」✔；无邮箱 / 电话）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检（来询即报）（有量，阿里后台回一页纸 + 要邮箱，坐实后转候选）', []),
    'SC-2439': ('keep_C', '印度 omnet78@gmail.com（1 光 4 工业小壳 MOQ / 价格册 / 交期等 ✔；4 推 0 回）：具体采购问 ✔ 但无公司 / 域名 + 零回应 → 留 C 储备（坐实公司后转候选）', []),
    'SC-2426': ('keep_C', 'Anvar（az.anvar@mail.ru；表内俄罗斯，+993 = 土库曼斯坦 → 国别待核；SFP 模块 SNR 牌子的，量比较大；18 推 0 回；WA 加不上 ×2）：SFP 本职线有量 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2444': ('keep_C', '巴基斯坦 Fibercom（Jalal Hamid；仅电话；MC / SFP 模块；10 推；备注「和珊姐对接了，不跟了」= 内部分工，非 pass 依据）：MC / SFP 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2450': ('keep_C', '土耳其 Serkan（Ady 加了微信；Alisa 客户；最主要看了 bypass）：土耳其展会微信接触（四主区 ✔ 微信可达 ✔）但无公司名 → 留 C 储备；Ady 微信追问公司名，报出即转候选；bypass 本职线', ['dayjob_fit']),
    'SC-2451': ('keep_C', '土耳其 Smali（Ady 加了微信；要 catalog 和公司 Profile）：土耳其展会微信接触（四主区 ✔ 微信可达 ✔）但无公司名 → 留 C 储备；Ady 微信追问公司名，报出即转候选', []),
    'SC-2411': ('keep_C', '吉尔吉斯斯坦 Zeenbek Sakeev（阿里巴巴广告询盘「新桥商业 PoE」；无邮箱 / 电话）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检（来询即报）', []),
    'SC-2447': ('keep_C', '台湾 Kai Turn Enterprise Co Ltd（Sheila Tsai；阿里询盘「3 个 IM-WS080GE」）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检（来询即报）', []),
    'SC-2462': ('keep_C', '印度尼西亚 PT Matahari Padang（Reza Wahid；阿里询盘「无人机模块」）：品类不符 + 仅阿里后台 → 留 C', []),
    'SC-3325': ('keep_C', '印度尼西亚（未具名；之前问过 MC，后续没回复；1 推）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检（来询即报）；MC 本职线', ['dayjob_fit']),
    'SC-3326': ('keep_C', '澳大利亚（未具名；阿里即时对话「I/O 模块」）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检（来询即报）', []),
    'SC-2502': ('keep_C', '伊朗 Khalid Faqeeh（阿里即时对话；无需求记录；无邮箱 / 电话）：伊朗守界（不 pass，不主动发）→ 留 C（仅阿里后台）', []),
    'SC-2378': ('keep_C', '乌克兰 Sergey / pulsar.kyiv@gmail.com（Shopify 询盘「无人机模块」）：守界乌克兰（不 pass，不主动发）→ 留 C；品类不符', []),
    'SC-2382': ('keep_C', '乌克兰 Vitaliy Grishchenko（RFQ「无人机模块」）：守界乌克兰（不 pass，不主动发）→ 留 C；品类不符', []),
    'SC-2407': ('keep_C', '乌克兰 Panasonic / Koziievskyi Maksym（gmail；「0 光 8 管理 PoE」）：守界乌克兰（不 pass，不主动发）→ 留 C', []),
    'SC-2412': ('keep_C', '乌克兰 Julia Chizh（mail.ru；询盘「升压 5 口」）：守界乌克兰（不 pass，不主动发）→ 留 C；升压 Saga 不供', []),
    'SC-2415': ('keep_C', '乌克兰 Maxim Guzhva（询盘「无人机」）：守界乌克兰（不 pass，不主动发）→ 留 C；品类不符', []),
    'SC-2436': ('keep_C', '伊朗 Eghlim Sabaye Shargh（lezdco@gmail.com 退信；电话 +98 915 在 = 备用路径，非刚性；8V 多功能）：伊朗守界（不 pass，不主动发）→ 留 C；VC 本职线', ['dayjob_fit']),
    'SC-2453': ('keep_C', '伊朗 aliirezazare@gmail.com（陈旧；1 光 4 FS 百兆 PoE 双纤 SC）：伊朗守界（不 pass，不主动发）→ 留 C', []),
    'SC-2369': ('keep_C', '沙特 Technology Leaders（MD Aslam，gmail；1V1D analog；WA 加不上）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2371': ('keep_C', '沙特 MalikM Ali（coreipro76@gmail.com；2023 年「2V1E」，也看了 ONV 的 MC）：VC / MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2375': ('keep_C', 'Faris（nurufi98@yahoo.com；国别未填；FS / MC）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2377': ('keep_C', '俄罗斯 P-Brand（p-brand.ru 正常；bk.ru；VC / 网络 / 光，像平台，很多牌子 N-Net）：平台型 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2380': ('keep_C', '科威特 Tamer Seleim（gmail；光猫；7 推 0 回）：光猫本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2381': ('keep_C', '英国 Usman Khan（uk8893740@gmail.com；多功能 VC；巴基斯坦号加不上 → 国别待核）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2404': ('keep_C', '越南 Tran Khien（gmail；千兆单纤 20KM 收发器 PCB board；1 推）：收发器板卡本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2406': ('keep_C', '埃塞俄比亚 Mulualem Ataliy（仅电话；Fiber Array 16 CH）：光纤阵列本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2427': ('keep_C', '孟加拉 Hadayet Ullah CEO（beingnbuy@gmail.com；10G 10KM 单模双纤模块）：光模块本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2430': ('keep_C', '印度 Himanshu Negi（gmail；2017 年 RFQ「2×2 光开关」）：光开关本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2435': ('keep_C', '印度尼西亚 lavenlavendos7@gmail.com（Bidi 60KM MC）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2457': ('keep_C', '智利 Diego Nicolas（gmail；询盘「DWDM」；WA 加不上）：DWDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2467': ('keep_C', '菲律宾 Freedie Valmeo（fcmvelectronics@yahoo.com；其实需要 TVI 1080P 16ch 3 对）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2472': ('keep_C', '印度尼西亚 rp5488536@gmail.com（Bidi 60KM 小外电）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2498': ('keep_C', '塞内加尔 Babacar Thiam（gmail；RFQ「华为 OTN」）：OTN 本职线 + 品牌指定 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2364': ('keep_C', '菲律宾 Liz Yumang（analiza.rwmy@gmail.com；16 槽机架；新注册没别的信息）：机架 Saga 不供 → 留 C', []),
    'SC-2390': ('keep_C', '乌干达 Warm services（Walubo，gmail；4 光 8 电工业；WA 加不上）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2391': ('keep_C', '摩洛哥 Beg-tech（Omar Begdouri，gmail；「中间商」；8 推 0 回）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2394': ('keep_C', '委内瑞拉 Amin Aboud（gmail；2018 年「60 个工业 90W PoE injector 分销」，看了好几家）：注入器 / 90W Saga 不供 → 留 C', []),
    'SC-2400': ('keep_C', '智利 Felipe Andres（piper.andres@gmail.com；2021 年「5 电口 PoE 工业级 70 个」）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）（有量但无公司，坐实后看）', []),
    'SC-2408': ('keep_C', '韩国 SPDC Inc.（Seung-Hyun Son，yahoo；wireless router）：品类不符 → 留 C', []),
    'SC-2414': ('keep_C', '澳大利亚 Ganzorig Erdenechimeg（ganaa725@gmail.com；无需求记录）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2417': ('keep_C', '韩国 Chang-Su Park（pcs0713@gmail.com；15 年国际站；无需求记录）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2422': ('keep_C', '菲律宾 Raked Store PH（Ariel Cervantes，gmail；TA726-FE；WA 加不上）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2424': ('keep_C', '印度 Ashu Ent（gmail；商业 PoE / PoE 配件，后边有 3 个合作公司；2 推 0 回）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C（坐实公司后看）', []),
    'SC-2456': ('keep_C', '沙特 MD Alhassan（mohammed-ah89@hotmail.com；工业千兆 1 光 4 电；最近活动 switch / CCTV）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2459': ('keep_C', '卡塔尔 Muhammed Shafi（shafi.gasco@gmail.com；2 光 8 带管理商业级；没别的信息）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2460': ('keep_C', '沙特 Sohaib Hadir（gmail；2 光 8 工业 PoE；21 年注册）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2461': ('keep_C', '巴西 Vescri Eletro（Cristiano De Jesus，yahoo.com.br；TA510-GE；Ribeirão Pires SP）：巴西先例在但个人免费邮箱 + 陈旧 → 留 C 储备', []),
    'SC-2466': ('keep_C', '印度尼西亚 Anita Heo（f_friend2005@hotmail.com；锐捷 / 海康威视产品）：品牌指定 → 留 C', []),
    'SC-2468': ('keep_C', '缅甸 Golden Wave Group（Aung，gmail ×2；无需求记录）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2473': ('keep_C', '印度尼西亚 Syukron Makmun（gmail；「10 个 Distributor / Wholesaler」）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2487': ('keep_C', '津巴布韦 Canlink（canlink.co.zw 正常；Tanyaradzwa Jimu，gmail；要 catalog；问 AP / CCTV / NVR）：品类杂 + 无先例 → 留 C', []),
    'SC-2491': ('keep_C', '印度 Govind Kumar（gmail ×2；2 光 8 傻瓜式；WA 加不上）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2492': ('keep_C', '阿尔及利亚 Hamza Kihel（gmail；2 光 4 管理小壳；WA 加不上；1 推）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
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
    L = [f'# C 池 · 闸 1 · 第 42 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 386–440 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：群发冷名单免费邮箱个人 30、阿里询盘后台可回 8、守界 10、土耳其微信无名户 2、仅电话 2、退信（有备用路径）2。候选 0、永久 pass 0 —— 桶尾低分段，全部留 C。', '',
         '> 值得留意的留 C：Visioncop VN（域名存活，找到邮箱即转候选）、GRUPO EBX PE（24 台工业 SFP 问，阿里后台）、omnet78 IN（MOQ / 价格册 / 交期问，无公司）、Serkan / Smali TR（Ady 微信，追问公司名）、Anvar TM（SNR SFP 量大 → 本职线）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批42_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
