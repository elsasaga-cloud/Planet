#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 38 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 166–220 户（按综合分序，SC-1610 … SC-1889）。

构成：群发冷名单（免费邮箱 + 公司网址）27（越南 14、俄语区 7、韩国 1、其他 5）、仅网址无邮箱 6、阿里巴巴 RFQ / RTS / 自建站个人 17（无人机 3、升压 / 注入器 4、光模块 / WDM / DAC 6）、展会接触 5（ZAFCO KR、Omri IL、Saleh OM、Ansar AE、Myanmar Padauk）。
  · 口径同第 36–37 批：分销 / 专业店 + 点名中国 / 台湾品牌 + 先例国（越南 / 印度 / 俄罗斯）→ 候选；自有品牌线索 → oem_target。
  · 候选 5 = 俄罗斯 ORIGO Networks（「自己的白色外壳，有人在卖他们的」「比较重要」= 自有品牌，无邮箱 → 闸 2 先找路径）/ 越南 Thuận An（工业交换机，optone 的）/ 越南 Viễn Thông Hoàng Thạch（switch，有 utepo 的）/ 印度 San Telequip Pvt. Ltd.（Profibus 连接器商，主动问 5 / 8 电口价格）/ 印度 Axis India（在用 Leonton 工业 FS，Sales Engineer 具名）。永久 pass 0。
  · 留意：Sức Sống Số VN（有洪瑞的 → Q-33 口径待 Simon）、ZAFCO KR（问 KC，26 推 0 回）、smr-egs.by（表内爱沙尼亚实为白俄罗斯）、Saleh（表内马来西亚，+968 阿曼号）、叙利亚 Saad（守界）。

用法：python3 sieve_batches/g1_038.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批38_2026-10-29.md）
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

BATCH = 'G1-38'
DATE = '2026-10-29'
CODES = ["SC-1610", "SC-1611", "SC-1613", "SC-1614", "SC-1615", "SC-1617", "SC-1620", "SC-1621", "SC-1624", "SC-1625", "SC-1627", "SC-1628", "SC-1634", "SC-1636", "SC-1638", "SC-1639", "SC-1640", "SC-1642", "SC-1643", "SC-1644", "SC-1645", "SC-1647", "SC-1648", "SC-1657", "SC-1658", "SC-1664", "SC-1668", "SC-1673", "SC-1678", "SC-1687", "SC-1696", "SC-1707", "SC-1708", "SC-1716", "SC-1720", "SC-1742", "SC-1743", "SC-1750", "SC-1756", "SC-1758", "SC-1776", "SC-1784", "SC-1785", "SC-1791", "SC-1793", "SC-1824", "SC-1827", "SC-1829", "SC-1832", "SC-1836", "SC-1847", "SC-1849", "SC-1863", "SC-1875", "SC-1889"]

OVERRIDE = {
    'SC-1613': ('candidate', '俄罗斯 ORIGO Networks（origo-networks.ru 正常；Simon：「自己的白色外壳，有人在卖他们的」「比较重要」；无邮箱 / 无电话）：自有品牌交换机商 = OEM 对象 ✔ 俄罗斯点名区 ✔ 对位 ✔ Simon 标重要 ✔ → 闸 2 查底数（rusprofile / checko）+ 官网找 sales 路径；无路径则回 C 待巡检；收款 / 物流待 Simon', ['oem_target']),
    'SC-1638': ('candidate', '越南 Thuận An（thuananvn.com.vn no_mx；thuanan.sales1@gmail.com；工业交换机，optone 的 ✔）：点名中国工业品牌 ✔ 越南先例 ✔ 工业对位 ✔ gmail 可达 ✔ → 闸 2 查底数（MST）后一页纸（STI-280GE / STI-288GPM）', []),
    'SC-1644': ('candidate', '越南 Viễn Thông Hoàng Thạch（vienthonghoangthach.com 正常；gmail；switch，有 utepo 的 ✔）：点名中国品牌 ✔ 越南先例 ✔ 对位 ✔ 可达 ✔ → 闸 2 查底数（MST）后一页纸', []),
    'SC-1657': ('candidate', '印度 San Telequip Pvt. Ltd.（santelequip.com 正常；Chetan Kamdi，gmail；Profibus Connectors 商，主动问了 5 / 8 电口的价格 ✔）：印度先例 ✔ 工业自动化渠道对位 ✔ 主动问价 ✔ 公司坐实路径 ✔ → 闸 2 查底数（MCA 镜像 zaubacorp / tofler）后报 STI-054GP / STC-028GP', []),
    'SC-1793': ('candidate', '印度 Axis India（axisindia.in 正常；Lavesh Savale Sales Engineer，gmail；2022-12 问了 website；在用 Leonton 工业 FS ✔）：印度先例 ✔ 台湾工业品牌在用 ✔ 工业对位 ✔ 主动接触 ✔ → 闸 2 查底数（MCA 镜像）后一页纸（STI 系列对标 Leonton）', []),
    'SC-1634': ('keep_C', '越南 Sức Sống Số（sucsongso.vn no_mx；gmail；switch，有洪瑞的）：洪瑞渠道客户 → Q-33 口径待 Simon（越南先例在，口径放开即转候选）→ 留 C', []),
    'SC-1621': ('keep_C', '叙利亚 Saad（自建站询盘「MINI 收发器 100 个」；hotmail）：叙利亚守界 + 收发器本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1824': ('keep_C', '乌克兰 Serhii Dichenko（RFQ「无人机」；gmail）：守界乌克兰 + 品类不符 → 留 C', []),
    'SC-1658': ('keep_C', '韩国 ZAFCO（YJ Hong Representative；hanmail；PoE switch 问 KC 认证；26 推 0 回）：决策人具名 ✔ 但 KC 门槛 + 26 推零回应 → 留 C 储备（KC 买方自理口径一页纸一次后看）', []),
    'SC-1611': ('keep_C', '越南 Noyafa / Newlink（noyafa.vn / newlink.com.vn 均 no_mx；gmail ×2；工业 MC、MC SFP 好几个国内牌子，Gnet 的）：光收发 / MC 为主 = 本职线 → 留 C + dayjob_fit（越南先例在，问到交换机即转候选）', ['dayjob_fit']),
    'SC-1639': ('keep_C', '越南 Tuấn Linh（tuanlinh.net.vn 正常；gmail；工业 MC，optone 的）：MC 为主 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1642': ('keep_C', '越南 Ulcab（ulcab.com.vn 正常；gmail ×2；工业 MC，upcom 的）：线缆商 + MC → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1645': ('keep_C', '越南 Viễn Thông Quang Thắng（vienthongquangthang.com no_mx；gmail；MC / VC 主要是 BTON 的）：MC / VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1640': ('keep_C', '越南 Tường Vui（tuongvui.vn 正常；gmail；switch，海康威视的）：海康 CCTV 店 → 留 C 储备', []),
    'SC-1610': ('keep_C', '越南 Nhất Tín（nhattin.vn 正常；maytinhnhattin@gmail.com；switch）：电脑店 + 零互动 → 留 C', []),
    'SC-1614': ('keep_C', '越南 PDC（pdcvn.com 正常；gmail；switch）：零互动 + 无品牌证据 → 留 C 储备', []),
    'SC-1615': ('keep_C', '越南 Penguin Fiber（penguin-fiber.com 正常；工业 FS / PoE 等；「似乎是一个销售平台 / 有国内的外壳」；hunter 没找到邮箱）：平台型 + 无路径 → 留 C 待巡检', []),
    'SC-1617': ('keep_C', '越南 PI Vietnam / Smarttech（pivietnam.com.vn no_mx；gmail；工业交换机 PoE 配件）：零互动 + 无品牌证据 → 留 C 储备', []),
    'SC-1647': ('keep_C', '越南 XLL Tech（xlltech.com no_mx；hotmail；商业 PoE 店铺形式卖得杂；有 YouTube 频道）：杂货店 → 留 C', []),
    'SC-1620': ('keep_C', '俄罗斯 Roxton MSK（roxton-msk.ru no_mx，网站打不开；商业 PoE；无邮箱）：无路径 → 留 C 待巡检（下次仍死即 pass）', []),
    'SC-1624': ('keep_C', '俄罗斯 Sibir Elektra（sibir-elektra.ru no_mx；mail.ru ×2；switch）：零互动 → 留 C 储备', []),
    'SC-1636': ('keep_C', '俄罗斯 TD Unic（tdunic.ru 正常；mail.ru；主要是 CCTV 商业 PoE）：CCTV 店 → 留 C 储备', []),
    'SC-1643': ('keep_C', '俄罗斯 Video PV（videopv.ru no_mx；gmail；商业 PoE / PoE 配件卖好几家的）：多品牌但未点名 + 零互动 → 留 C 储备（一页纸一次后看）', []),
    'SC-1827': ('keep_C', '俄罗斯 Maxim Neretin（gmail；2015 年国际站；2 光 8 电 10G 光 mikrotik 的）：个人 + 品牌指定 → 留 C', []),
    'SC-1832': ('keep_C', '俄罗斯 OOO Date-Perm（bk.ru；2019 年「333 个 PoE injector 15.4W」）：注入器 Saga 不供 → 留 C', []),
    'SC-1628': ('keep_C', 'SMR EGS（smr-egs.by 正常；表内「爱沙尼亚」，.by = 白俄罗斯 → 国别待核；mail.ru；networking）：零互动 + 无产品证据 → 留 C 储备', []),
    'SC-1625': ('keep_C', '马耳他 Simark Supplies（simarksupplies.com 正常；很多产品 / 周边；「销售平台」；无邮箱）：平台型 + 无路径 → 留 C 待巡检', []),
    'SC-1708': ('keep_C', '波兰 Marjol（marjol.eu 正常；WDM；无邮箱）：WDM 本职线 + 无路径 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-1696': ('keep_C', '保加利亚 Eurostroy RN（eurostroy-rn.com no_mx；abv.bg；CWDM 接线）：CWDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1829': ('keep_C', '保加利亚 Green power BG Ltd.（gmail；2011 年询盘「15 对 2 路开关量走光」）：开关量光传 = 本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1668': ('keep_C', '瑞士 internetfabrik（Juerg Rietmann，gmail；2014 年「SFP 千兆小外电」；WA 加不上；vymaps 仅黄页）：SFP 本职线 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1687': ('keep_C', '以色列 Teleric（Khaliq Rehman，yahoo；2016 年「100 个千兆 SFP 小外电」，也看了洪瑞商业交换机）：SFP 本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1849': ('keep_C', '韩国 Fiberland（fiberland.co.kr；naver；很多产品都有，销售平台）：平台型 → 留 C', []),
    'SC-1791': ('keep_C', '孟加拉 Appro（appro.com.bd 正常；gmail；丰润达的商业 PoE，应是 Elink 分公司；1 推）：点名中国品牌 ✔ 但孟加拉无先例 → 留 C 储备（一页纸一次后看）', []),
    'SC-1889': ('keep_C', '尼日利亚 Crosstech（crosstech.com.ng 正常；gmail；FS / MC 主要是 CCTV）：CCTV 店 + 无先例 → 留 C', []),
    'SC-1784': ('keep_C', '缅甸 Myanmar Padauk Engineering（myanmarpadauk.com 正常；Wai Yan Htet 采购；仅电话；MC 千兆 SC 双纤 20 公里小外电；15 推 0 回）：MC 本职线 + 缅甸无先例 + 零回应 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1743': ('keep_C', '津巴布韦 Annie Palatoni（gmail；无需求记录；8 推 0 回）：零信息 → 留 C', []),
    'SC-1750': ('keep_C', '土耳其 Gokhan CAKIR（hotmail；15 年国际站；2 推 0 回）：个人 + 无公司 → 留 C（土耳其个人，来询再看）', []),
    'SC-1785': ('keep_C', '以色列 Omri（仅电话；问 8+1 / 8+2 / 8+2+1 商业级价格）：问价 ✔ 但无公司 / 无邮箱 → 留 C（WA 一页纸一次后看）', []),
    'SC-1863': ('keep_C', 'Saleh AL-Marjabi（software engineer；gmail；表内「马来西亚」，+968 = 阿曼 → 国别待核；懂 WDM，同事问 2 光 4 PoE，拍了 2 光 4 管理小壳，看了 SFP）：展会个人 + 无公司 → 留 C 储备 + dayjob_fit', ['dayjob_fit']),
    'SC-1847': ('keep_C', '阿联酋 Ansar Abbas（yahoo ×2；问了商业 PoE 合作 + 无源产品；「长期不看信息」；5 推）：个人 + 无公司 → 留 C', []),
    'SC-1875': ('keep_C', '津巴布韦 Prosper Motsi（仅电话；「5 米 10G DAC」；19 推 0 回）：DAC 本职线 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1707': ('keep_C', '以色列 lirang@gmail.com（RTS 订单「升压 5 口」）：阿里巴巴 RTS 小额订单个人买家（付过钱）→ 不 pass、不入池 → 留 C（来询被动报价）；升压 Saga 不供', []),
    'SC-1756': ('keep_C', '越南 le.nhat@gmail.com（RTS 订单「1 个 IO 模块」）：阿里巴巴 RTS 小额订单个人买家（付过钱）→ 不 pass、不入池 → 留 C（来询被动报价）', []),
    'SC-1648': ('keep_C', '以色列 yaircohen162@gmail.com（RFQ「无人机模块」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1758': ('keep_C', '白俄罗斯 lobazhevich.ip@gmail.com（RFQ「无人机模块」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1627': ('keep_C', '以色列 slmanabojrad@gmail.com（RFQ「5 口延长器」）：延长器非 Saga 线 → 留 C', []),
    'SC-1664': ('keep_C', '哥伦比亚 comria@gmail.com（即时对话「2 光 4 升压及配件」）：升压 Saga 不供 → 留 C', []),
    'SC-1776': ('keep_C', '乌干达 Anthony Okonye（询盘「升压 5 口」；仅电话）：升压 Saga 不供 → 留 C', []),
    'SC-1673': ('keep_C', '巴拉圭 robertwiki1@hotmail.com（RFQ「10G 100KM bidi 模块」）：光模块本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1678': ('keep_C', '危地马拉 wag31molina@gmail.com（自建站询盘「8 台 2 光 10 电」）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1716': ('keep_C', '澳大利亚 pedro.visualeffects@gmail.com（自建站询盘「2 台 WS-C3650-48FQ-E」思科型号；墨西哥号码）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1720': ('keep_C', '阿联酋 shams7790@gmail.com（RFQ「安防箱」）：品类不符 → 留 C', []),
    'SC-1742': ('keep_C', '贝宁 a3hinter2000@gmail.com（RFQ「4 口千兆商业 PoE」）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1836': ('keep_C', '印度尼西亚 abieb.mep@gmail.com（RFQ「DS-3E0326P-E/M」海康型号指定）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
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
    L = [f'# C 池 · 闸 1 · 第 38 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 166–220 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：群发冷名单（免费邮箱 + 公司网址）27、仅网址 6、阿里巴巴 RFQ / RTS / 自建站个人 17、展会接触 5。候选 5 = 俄罗斯 ORIGO Networks（自有品牌，先找路径）+ 越南 Thuận An / Hoàng Thạch（点名中国品牌 + 越南先例）+ 印度 San Telequip / Axis India（主动问价 / 在用台湾工业品牌）。', '',
         '> 值得留意的留 C：Sức Sống Số VN（有洪瑞的 → Q-33）、ZAFCO KR（KC + 26 推 0 回）、Noyafa / Tuấn Linh / Ulcab VN（工业 MC = 本职线）、videopv.ru（多品牌 PoE 配件店）、Myanmar Padauk（采购具名，仅电话，15 推 0 回）、国别待核 smr-egs.by / Saleh（+968）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批38_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
