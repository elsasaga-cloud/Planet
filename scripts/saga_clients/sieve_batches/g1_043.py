#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 43 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 441–495 户（按综合分序，SC-2504 … SC-2616；综合分 −23 → −29）。

构成：群发冷名单 / 陈旧免费邮箱个人 36（本职线 VC / AHD / MC / SFP / 光猫 / DWDM / HDMI 延长 17；WA 加不上 9）、中国大陆同行域名 6（仅网址）、「无联系方式」但路径在 5（阿里后台 / 微信 / 平台链接）、仅电话 2、退信 1。
  · 口径同第 36–42 批。候选 1 = 越南 Tùng Lâm Technology Technical Co., Ltd.（2026-03 阿里询盘「分销商寻求合作」，原表有名片 + 两个手机号；越南先例 ✔ 公司名 ✔ 分销意向 ✔ 路径 ✔）。
  · 永久 pass 1 = SC-2525 肯尼亚 nixonbsongs@yahoo.com（退信 + 无电话 / 无域名 / 无平台 = 闸 0 刚性②）。
  · 留意：CNM International FR（Bosch 分销商，「想分销我们的 VC / MC」= 本职线强线索）、Artyom Hong KZ（300 个华为兼容 10G SFP+ = 本职线有量）、Aureola QA（415 个 HDMI extender）、SC-3329 = RS Components 英国商品页（巨头 + Q-33）、中国大陆 6 户按例留 C（smilenet-switch.com nxdomain 待巡检）。

用法：python3 sieve_batches/g1_043.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批43_2026-10-29.md）
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

BATCH = 'G1-43'
DATE = '2026-10-29'
CODES = ["SC-2504", "SC-2506", "SC-2507", "SC-2511", "SC-2512", "SC-2518", "SC-2465", "SC-2520", "SC-2521", "SC-2522", "SC-2523", "SC-2525", "SC-2526", "SC-2527", "SC-2528", "SC-2530", "SC-3329", "SC-2531", "SC-2534", "SC-2536", "SC-2538", "SC-2540", "SC-2544", "SC-2545", "SC-2549", "SC-2550", "SC-2554", "SC-2558", "SC-2559", "SC-2560", "SC-2563", "SC-2565", "SC-2566", "SC-2567", "SC-2570", "SC-2571", "SC-2572", "SC-2574", "SC-2576", "SC-2581", "SC-2582", "SC-2584", "SC-2589", "SC-2590", "SC-2591", "SC-3353", "SC-2595", "SC-2596", "SC-2602", "SC-2605", "SC-2607", "SC-2610", "SC-2546", "SC-2614", "SC-2616"]

OVERRIDE = {
    'SC-2504': ('candidate', '越南 Tùng Lâm Technology Technical Co., Ltd.（Tùng Lâm；2026-03-19 阿里巴巴询盘「分销商寻求合作」✔；原表「2019 年使用国际站，名片如右图，Phone: 0969 396 686 / 0858 344 388」= 路径在；表内无邮箱）：越南先例 ✔ 公司名 ✔ 分销意向（新鲜）✔ 电话 / 阿里后台可达 ✔ → 闸 2 查底数（MST）+ 阿里后台要邮箱，坐实后一页纸', []),
    'SC-2525': ('pass_final', '肯尼亚 Nixon Songio（nixonbsongs@yahoo.com；阿里询盘「千兆 2 光 4 工业小壳 PoE」；退信 bounce=1；无电话 / 无域名 / 无平台账号 / 无微信）：退信且无任何备用路径 = 闸 0 刚性② → 永久 pass', []),
    'SC-3329': ('keep_C', '英国 RS Components 商品页（sg.rs-online.com/web/p/network-switches/2727671；Smartbyte 同行经销商表）：巨头分销 + SmartByte 渠道（Q-33）→ 留 C 巨头（不 pass，不主动）', []),
    'SC-3353': ('keep_C', '台湾 ILU Co., Ltd.（ilucoltd.en.taiwantrade.com 平台页；「基本都是海思的」；谷歌来源；无邮箱 / 电话）：海思方案同行 / ODM 型 + 仅平台链接 → 留 C 待巡检', []),
    'SC-2616': ('keep_C', 'Zaid（国别未填；微信联系，11 推 0 回；问了 2 光 4 MC 外购板子）：微信路径在 + MC 板卡本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2566': ('keep_C', '中国大陆 connlight.com（域正常；无邮箱）：中国大陆同行 / 供应链域名（仅网址，非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-2570': ('keep_C', '中国大陆 flyingfiber.com（域正常；无邮箱）：中国大陆同行 / 供应链域名（仅网址，非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-2571': ('keep_C', '中国大陆 gpsenke.com（域正常；无邮箱）：中国大陆同行 / 供应链域名（仅网址，非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-2572': ('keep_C', '中国大陆 hdoverip.com（no_mx；无邮箱）：中国大陆同行 / 供应链域名（仅网址，非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-2584': ('keep_C', '中国大陆 smilenet-switch.com（nxdomain；无邮箱）：中国大陆同行 / 供应链域名（仅网址，非出口客户）→ 不入池、不 pass → 留 C（同行观察）；域死 → 待巡检（下次仍死即 pass）', []),
    'SC-2591': ('keep_C', '中国大陆 yunvo.cn（域正常；无邮箱）：中国大陆同行 / 供应链域名（仅网址，非出口客户）→ 不入池、不 pass → 留 C（同行观察）', []),
    'SC-2521': ('keep_C', '法国 CNM International（Franck Belchi Technical；contact-cnmi@wanadoo.fr；Bosch Distributor；「want to distribute our VC, MC」；WA 加不上）：欧洲分销商 ✔ 但需求为 VC / MC = 本职线 → 留 C + dayjob_fit（本职线优先联系；问到交换机即转候选）', ['dayjob_fit']),
    'SC-2512': ('keep_C', '哈萨克斯坦 Artyom Hong（kriganec@gmail.com；「300 个 10G SFP+ 1270/1330nm 10km 兼容华为」）：光模块本职线有量 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2520': ('keep_C', '卡塔尔 Aureola Technology（Geetesh Purbia；仅电话；「415 个 HDMI extender」；14 推 0 回）：HDMI 延长本职线有量 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2522': ('keep_C', '巴西 IP Associados（Ismael M. Santos Consultant，hotmail；只要 IP 视频监控 / IP camera over MC；WA 加不上）：IP 视频 + MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2545': ('keep_C', '印度 JAYANI TECHNOLOGIES LLP（仅电话；外贸邦「1V1D」；16 推 0 回）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2558': ('keep_C', '孟加拉 Friends Defence Systems（Syed Zalil Ahmed CEO，gmail；2022 年询盘 DWDM 设备）：DWDM 本职线 + 国防类守界 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2595': ('keep_C', '马来西亚 Synergy M5 Sdn Bhd（Alex Low，gmail；AHD over fiber；WA 可加）：AHD 光传本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2614': ('keep_C', '印度 Eco Smart Solutions（ecosmartsolutions.co.in 正常；Som Sharma，gmail；光猫 5 个）：光猫本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2465': ('keep_C', '俄罗斯 CCTV-IT（cctv-it.ru 正常；Politiko Evgeny，mail.ru；CCTV price；8 推 0 回）：CCTV 店 → 留 C', []),
    'SC-2546': ('keep_C', '俄罗斯 Krepkiy Oreshek（Dmitriy Viktorovich，mail.ru；安保公司，问 BNC 同时传视频与电；8 推 0 回）：EoC 非 Saga 线 → 留 C', []),
    'SC-2534': ('keep_C', '阿根廷 SPORT NETWORK（Gustavo López，yahoo.com.ar；光端机）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2544': ('keep_C', '美国 Automated Security（Dave Anderson，alarmitpueblo@msn.com；VC；WA 加不上）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2554': ('keep_C', '拉脱维亚 Vadim Adamovich（gmail；2Ch / 4Ch AHD；13 年阿里）：AHD 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2559': ('keep_C', '摩洛哥 Satcam（Tarik Anssir，gmail；4 路 AHD / 4V 高清 1 对；嫌价格高）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2602': ('keep_C', '韩国 Hongchung（Chang-ho Park，hanmail；2V1D 模拟视频光端机）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2607': ('keep_C', 'm_feyzi@yahoo.com（表内德国，0912 疑伊朗手机 → 国别待核；多功能光端机）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2526': ('keep_C', '印度尼西亚 onisseo4@gmail.com（Bidi 60KM 小外电；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2550': ('keep_C', '阿根廷 Marcos Piovi（gmail；Bidi 60KM MC；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2563': ('keep_C', '印度 buddhv0@gmail.com（Bidi 千兆小外电 60 公里）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2590': ('keep_C', '津巴布韦 Walter Nyawungwa（gmail；「600 个 15km / 30km / 60km 的」；17 年阿里）：MC 本职线有量 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2610': ('keep_C', '坦桑尼亚 Shabani（ramasalum224@gmail.com；百兆内电 MC；WA 加不上；3 推）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2530': ('keep_C', 'Sudesh Verma（gmail；国别未填 → 疑印度；单模单纤，也在找 8K 加串口；18 年国际站）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2567': ('keep_C', '乌干达 Allan Doi（gmail；百兆双纤小外电，「buy it locally」，后续不回复）：MC 本职线 + 已本地采购 → 留 C', []),
    'SC-2581': ('keep_C', '印度 Saharsha Enterprises（Kishore，hotmail；GPS over fiber，提供不了；2 推）：品类不符 → 留 C', []),
    'SC-2589': ('keep_C', '埃及 Mahmoud（utc20092010@yahoo.com；「问能成为分销商吗？」）：分销意向 ✔ 但 yahoo 无公司 + 埃及无先例 → 留 C 储备（坐实公司后看）', []),
    'SC-2528': ('keep_C', '孟加拉 Syed Abu Jafar CEO（seljafar@gmail.com；工业品；8 推 0 回）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2531': ('keep_C', '印度 Abeer Electronics（Manish Sharma，rediffmail；cctv information，发照片 / 公司简介；WA 加不上）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2538': ('keep_C', '土耳其 Biltek（Kaan Kokarcali，gmail；cameras；WA 加不上 ×2；9 推 0 回）：摄像机需求 + 免费邮箱 + 零回应 → 留 C（土耳其，来询再看）', []),
    'SC-2596': ('keep_C', '阿联酋 Mustafa Alnatour（abu.yaanaal@gmail.com；2018 年国际站 Distributor / Wholesaler；无需求记录）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2506': ('keep_C', '西班牙 Antonio Nieto（anieto7@hotmail.com；TA510-GE；18 年注册没别的信息）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2507': ('keep_C', '美国 atoguem@hotmail.com（Camera）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2511': ('keep_C', '印度尼西亚 kmjkt01@gmail.com（4 光 8 工业大壳；陈旧）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2518': ('keep_C', '俄罗斯 Bahaa Hamzah（ug204856@gmail.com；PoE MC；新注册没别的信息）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2523': ('keep_C', 'Daniel Oprica Manager（daniel.omanoffice@gmail.com；国别未填 → 疑阿曼；无需求记录）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2527': ('keep_C', 'Poly KOLTER（polykolter@gmail.com；国别未填；无需求记录）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2536': ('keep_C', '危地马拉 Jaime Rios（aleriosgomerano@hotmail.com；21 年注册没啥信息）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2540': ('keep_C', '墨西哥 Daniela Arcos（live.com；Cisco items）：品牌指定 → 留 C', []),
    'SC-2549': ('keep_C', '菲律宾 jossuedacdac3@gmail.com（4 光 8 工业大壳；WA 加不上）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2560': ('keep_C', '巴西 Anderson Silva（gmail；2017 年「百兆 1 光 2 板子 100 个」）：百兆板卡 Saga 不供 → 留 C', []),
    'SC-2565': ('keep_C', '墨西哥 Agustin Vidal（compu_cinkar@hotmail.com；8 口工业交换机；陈旧）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2574': ('keep_C', '墨西哥 Julian Doni Rojas Perez（hotmail；千兆工业 2 光 8 傻瓜式；陈旧）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2576': ('keep_C', '阿尔及利亚 Zobeidi（khmisti39@gmail.com；product and price）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2582': ('keep_C', '多米尼克 Sandy Perez（gmail；2 光 4 电 MC 外购那一款；陈旧）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2605': ('keep_C', '沙特 Layan Najd（layannajd@yahoo.com；general information）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 43 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 441–495 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：免费邮箱个人 36、中国大陆同行域名 6、无联系方式但路径在 5、仅电话 2、退信 1。候选 1 = 越南 Tùng Lâm Technology（分销商寻求合作 2026-03 + 名片电话）。永久 pass 1 = SC-2525（退信无备用路径，闸 0 刚性②）。', '',
         '> 值得留意的留 C：CNM International FR（Bosch 分销商要分销 VC / MC → 本职线）、Artyom Hong KZ（300 个 10G SFP+）、Aureola QA（415 个 HDMI extender）、Mahmoud EG（「能成为分销商吗」，yahoo 无公司）、SC-3329 RS Components 商品页（巨头 / Q-33）、SC-3353 台湾 ILU（海思方案，平台链接）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批43_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
