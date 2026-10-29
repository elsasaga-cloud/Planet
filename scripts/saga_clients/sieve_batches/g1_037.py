#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 37 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 111–165 户（按综合分序，SC-1208 … SC-1606）。

构成：群发冷名单（免费邮箱 + 公司网址）24（越南 10、俄语区 7）、阿里巴巴 RFQ / RTS 个人 23（无人机 / 光模块 / 光开关 / SDI 等品类不符 12）、展会接触 2（Elid MY、Defense MICE KR）、仅网址 3。
  · 口径同桶 ⑦ 首批 + 桶 ⑥ 规则「分销 / 零售商 + 点名中国品牌 + 先例国（越南 / 哈萨克）→ 候选」（免费邮箱不减分，可达即可）。
  · 候选 4 = 越南 Chuyển Đổi Quang / Holink（VC 为主 + 工业 FS / 商业 PoE 很多国内牌子，有业务微信）/ Mạng Công Nghiệp（工业交换机，三旺的）/ Mạng Viễn Thông（PoE / FS / MC / VC + 工业交换机，中科德能的）/ 哈萨克 LS Service（表内俄罗斯，.kz → 国别待核；商业 PoE 主要 hisource）。永久 pass 0。
  · 留意：Falcon Eye RU（俄罗斯 CCTV 品牌站，无邮箱 → oem_target 备查）、Elid Sdn Bhd MY（门禁品牌商，BD 具名）、Defense MICE KR（国防展会机构 = 守界，Simon 曾说多跟进）、digicom.com.bd（表内印尼实为孟加拉）。

用法：python3 sieve_batches/g1_037.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批37_2026-10-29.md）
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

BATCH = 'G1-37'
DATE = '2026-10-29'
CODES = ["SC-1208", "SC-1221", "SC-1223", "SC-1231", "SC-1241", "SC-1252", "SC-1257", "SC-1258", "SC-1272", "SC-1277", "SC-1303", "SC-1304", "SC-1307", "SC-1333", "SC-1405", "SC-1411", "SC-1413", "SC-1416", "SC-1418", "SC-1419", "SC-1422", "SC-1426", "SC-1434", "SC-1438", "SC-1440", "SC-1444", "SC-1453", "SC-1454", "SC-1461", "SC-1462", "SC-1463", "SC-1469", "SC-1470", "SC-1489", "SC-1546", "SC-1565", "SC-1566", "SC-1567", "SC-1577", "SC-1579", "SC-1580", "SC-1582", "SC-1586", "SC-1589", "SC-1590", "SC-1591", "SC-1592", "SC-1593", "SC-1594", "SC-1597", "SC-1602", "SC-1603", "SC-1604", "SC-1605", "SC-1606"]

OVERRIDE = {
    'SC-1586': ('candidate', '越南 Chuyển Đổi Quang / Holink Tech / Viễn Thông Thiên Tân（chuyendoiquang.com / holinktech.com / vienthongthientan.com 均正常；VC 为主很多国内牌子低价 + MC G-net + 工业 FS / 商业 PoE；「有他们业务微信」；gmail）：点名中国品牌 ✔ 越南先例 ✔ 对位 ✔ 微信可达 ✔ → 闸 2 查底数（MST：yellowpages.vn）后微信 / 邮件一页纸；VC 本职线并行', ['dayjob_fit']),
    'SC-1605': ('candidate', '越南 Mạng Công Nghiệp（mangcongnghiep.vn no_mx；联系 tantien2tech@gmail.com；工业交换机，三旺的 ✔）：点名中国工业品牌 ✔ 越南先例 ✔ 工业对位 ✔ gmail 可达 ✔ → 闸 2 查底数（MST）后一页纸（STI-280GE $46.6 / STI-288GPM $78.9）', []),
    'SC-1606': ('candidate', '越南 Mạng Viễn Thông（mangvienthong.com.vn 正常；联系 inbox.thanhcong@gmail.com；PoE / FS / MC / VC + 工业交换机，有中科德能的 ✔）：点名中国品牌 ✔ 越南先例 ✔ 对位 ✔ 可达 ✔ → 闸 2 查底数（MST）后一页纸', ['dayjob_fit']),
    'SC-1602': ('candidate', 'LS Service（lsservice.kz 正常；表内「俄罗斯」，.kz = 哈萨克斯坦 → 国别待核；ls-servicom@yandex.ru；商业 PoE 主要是 hisource 的 ✔）：点名中国品牌 ✔ 哈萨克先例 ✔ 对位 ✔ 可达 ✔ → 闸 2 查底数（statsnet / adata）后一页纸；收款路径待 Simon', []),
    'SC-1469': ('keep_C', '韩国 Defense MICE Institute（kdmi.kr；T.H. Lee Director；naver；只要了名片；45 推 0 回；Simon「可以尝试多跟进」）：国防展会机构 = 守界（军工）+ 零回应 → 留 C（不 pass）', []),
    'SC-1241': ('keep_C', '伊朗 Jaefar Sayedi（询盘「OXC」；仅电话）：伊朗守界 + 光交叉本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1592': ('keep_C', '俄罗斯 Falcon Eye（falconeye.su 域正常；商业 PoE；无邮箱）：俄罗斯 CCTV 品牌站（疑自有品牌 → oem_target 备查）+ 无路径 → 留 C 待巡检（找到邮箱即转候选；收款待定）', ['oem_target']),
    'SC-1470': ('keep_C', '马来西亚 Elid Sdn Bhd（展会；做 Security，也拿了旁边展位册子；Chee Karlson BD；gmail）：马来西亚门禁品牌商（疑自有品牌 → oem_target 备查）+ 决策人具名 ✔ 但免费邮箱 + 马来西亚无先例 → 留 C 储备（一页纸一次后看）', ['oem_target']),
    'SC-1438': ('keep_C', '韩国 Fiberworld（fiberworld.co.kr；naver；MC / FS 更多 cable 连接器；「似乎是个平台」）：平台型 + 本职线 → 留 C', ['dayjob_fit']),
    'SC-1454': ('keep_C', '泰国 Sysinfo（sysinfo.co.th；gmail；工业 FS 等有名牌子；「销售平台」）：平台型 → 留 C', []),
    'SC-1546': ('keep_C', '越南 VVA（vva.com.vn 正常；Tran Quang Dung Managing Director 具名；gmail；工业级交换机；1 推 0 回）：越南先例 ✔ 对位 ✔ 决策人 ✔ 但无品牌证据 + 零回应 → 留 C 储备（一页纸一次后看，有回应即转候选）', []),
    'SC-1567': ('keep_C', '越南 3A / Vua Phụ Kiện（3a.com.vn；gmail；很多国内牌子商业 PoE）：配件网店型 → 留 C', []),
    'SC-1589': ('keep_C', '越南 Điện Máy Trường Doanh（dienmaytruongdoanh.vn no_mx；gmail；MC / SFP / switch 好几个国内牌子）：电器杂货店 → 留 C', []),
    'SC-1580': ('keep_C', '越南 Anh Khôi Telecom（anhkhoi.com.vn no_mx；gmail；switch「很多外壳」）：零互动 + 无品牌证据 → 留 C 储备', []),
    'SC-1597': ('keep_C', '越南 Hshop（hshop.vn；gmail；工业交换机）：电子元件网店 → 留 C', []),
    'SC-1603': ('keep_C', '越南 Lưu Gia Telecom（luugiatelecom.vn nxdomain；gmail ×2；switch）：域死但 gmail 路径在 → 留 C 待巡检', []),
    'SC-1604': ('keep_C', '越南 Maitel（maitel.vn；gmail；switch，有海思的）：零互动 → 留 C 储备', []),
    'SC-1489': ('keep_C', 'Digicom（digicom.com.bd no_mx；表内「印度尼西亚」，.bd = 孟加拉 → 国别待核；yahoo；CCTV + 商业 PoE；Simon「可以多跟进一下」；1 推）：CCTV 店 + 非点名国 → 留 C 储备（换稿一次后看）', []),
    'SC-1565': ('keep_C', '危地马拉 Teletechnonet（teletechnonet.com；gmail；Ethernet switch；4 推 0 回）：零回应 + 无先例 → 留 C', []),
    'SC-1453': ('keep_C', 'Somvangoa（somvangoa.com；hotmail；电话 +856 = 老挝 ↔ 表内泰国 → 国别待核；MC / 工业 MC / 工业 FS「Link 牌子」看着国内外壳）：零互动 + 国别存疑 → 留 C 储备', []),
    'SC-1405': ('keep_C', '韩国 us101.co.kr（nate.com；switch；17 推 0 回）：零回应 → 留 C', []),
    'SC-1579': ('keep_C', '俄罗斯 Alfavision（alfavision.su MX 正常但网站打不开；商业 PoE；无邮箱）：无路径 → 留 C 待巡检', []),
    'SC-1582': ('keep_C', '俄罗斯 BP Kuban（bp-kuban.ru；yandex / gmail；商业 PoE）：零互动 → 留 C 储备', []),
    'SC-1590': ('keep_C', '俄罗斯 DV Network（dvnetwork.ru DNS 超时；mail.ru；Bton 的 MC / VC / FS）：本职线 + 零互动 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1591': ('keep_C', '俄罗斯 Elecom37（elecom37.ru；mail.ru；商业 PoE）：零互动 → 留 C 储备', []),
    'SC-1593': ('keep_C', '意大利 Giuseppe Guastella（giuseppeguastella.it；gmail；无需求记录）：个体电子店 → 留 C', []),
    'SC-1426': ('keep_C', '台湾 CJ Eco（cjeco.com.tw no_mx；yahoo.com.tw；VC / HDMI，像 Nufiber 外壳）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1252': ('keep_C', 'Boss Security Worldwide（bosssecurityworldwide.com 域正常；国别未填；Wi-Tek；无邮箱）：无路径 + 国别未知 → 留 C 待巡检', []),
    'SC-1304': ('keep_C', '美国 Al-Omnia（omnia.com no_mx；hotmail；interested in network extender）：延长器非 Saga 线 → 留 C', []),
    'SC-1577': ('keep_C', '美国 R&H computer group（「Mr. Router Hansome」gmail；TA714-FE/SXX switch；WA 加不上）：疑可疑线索 + 型号非 Saga → 留 C', []),
    'SC-1221': ('keep_C', '澳大利亚 stefan@outlook.com（RTS 订单「1 个 10G 收发器」）：阿里巴巴 RTS 小额订单个人买家（付过钱）→ 不 pass、不入池 → 留 C（来询被动报价）；收发器本职线', ['dayjob_fit']),
    'SC-1231': ('keep_C', '澳大利亚 zarkosaveski@gmail.com（RTS 订单「光路 10G MC」）：阿里巴巴 RTS 小额订单个人买家（付过钱）→ 不 pass、不入池 → 留 C（来询被动报价）', []),
    'SC-1258': ('keep_C', '英国 danielb@gmail.com（RTS 订单「1 个 IO 模块」）：阿里巴巴 RTS 小额订单个人买家（付过钱）→ 不 pass、不入池 → 留 C（来询被动报价）', []),
    'SC-1303': ('keep_C', '孟加拉 Abdul Lotif（RTS 订单「外购的 2 光 4 电板子」；仅电话）：阿里巴巴 RTS 小额订单个人买家（付过钱）→ 不 pass、不入池 → 留 C（来询被动报价）', []),
    'SC-1257': ('keep_C', '波兰 daniel.kowalsky93@gmail.com（RFQ「无人机模块」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1272': ('keep_C', '美国 kradhikrish@gmail.com（RFQ「无人机模块」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1418': ('keep_C', '美国 adonaymurcia74@gmail.com（RFQ「无人机」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1440': ('keep_C', '波兰 gbconelove@gmail.com（RFQ「无人机」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1461': ('keep_C', '捷克 webkochmar@gmail.com（RFQ「无人机」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1462': ('keep_C', '法国 wisey1337@gmail.com（RFQ「无人机光纤」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1594': ('keep_C', '韩国 gkgkgk0610@gmail.com（RFQ「无人机模块」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-1277': ('keep_C', '捷克 netcorp.cz@gmail.com（RFQ「100G 40KM / 80KM 模块」；Martin Kolar）：光模块本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1444': ('keep_C', '芬兰 jukka.lampikoski@gmail.com（RFQ「CWDM」）：CWDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1463': ('keep_C', '波兰 wroblewski88@gmail.com（RFQ「48×48 矩阵光开关」）：光开关本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1422': ('keep_C', '波兰 bartixxx1@gmail.com（RFQ「3G SDI 不带数据」）：SDI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1413': ('keep_C', '意大利 Club Magic Audiovision（RFQ「8 路模拟视频」；Domenico Marconi；gmail）：视频光传本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1419': ('keep_C', '匈牙利 arpadeusz@gmail.com（RFQ「升压 5 口」）：升压 PoE Saga 不供 → 留 C', []),
    'SC-1208': ('keep_C', '阿联酋 muhammad.sameer.wk@gmail.com（自建站询盘「DH-PFS4210-8GT-DP」大华型号指定；沙特号码）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1223': ('keep_C', '加蓬 tech-cam vision retailer（2019 年 RFQ「全千兆 1+2+24 口 PoE」；gmail）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1307': ('keep_C', '科特迪瓦 Bkg service（RFQ「Router」；gmail）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1333': ('keep_C', '乌干达 dbm techs company Ltd（RFQ「Teltonika TSW200」品牌指定；gmail）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1411': ('keep_C', '南苏丹（未具名；自建站询盘「5 电口」；仅电话）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1416': ('keep_C', '几内亚 New tech informatic（即时对话「Cisco 模块」；gmail）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1434': ('keep_C', '印度尼西亚 eddy.setiady@gmail.com（自建站询盘「5 口交换机带 PoE」；手机）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1566': ('keep_C', '乌兹别克斯坦 1414captiva@gmail.com（RFQ「2+8 千兆商业 PoE」；Eshmurodov Isomiddin）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）（乌兹别克先例在，但个人 RFQ）', []),
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
    L = [f'# C 池 · 闸 1 · 第 37 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 111–165 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：群发冷名单（免费邮箱 + 公司网址）24、阿里巴巴 RFQ / RTS 个人 23（品类不符 12）、展会接触 2、仅网址 3。候选 4 = 越南 3 家专业店 / 分销（Chuyển Đổi Quang / Holink、Mạng Công Nghiệp、Mạng Viễn Thông；均点名中国品牌 + 越南先例）+ 哈萨克 LS Service（hisource；国别待核）。', '',
         '> 值得留意的留 C：Falcon Eye RU（CCTV 品牌站，无邮箱）、Elid Sdn Bhd MY（门禁品牌商）、Defense MICE Institute KR（守界，45 推 0 回）、VVA VN（Managing Director 具名，工业交换机）、digicom.com.bd（国别待核）、somvangoa（+856 老挝号 ↔ 表内泰国）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批37_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
