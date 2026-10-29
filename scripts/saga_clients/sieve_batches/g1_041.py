#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 41 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 331–385 户（按综合分序，SC-2235 … SC-2363；综合分 −10 → −16）。

构成：展会微信接触（土耳其，Ady / Evelyn 加了微信，表内「无联系方式」）8、群发冷名单免费邮箱 30（WA 加不上 11）、仅电话 7、守界（伊朗 4、叙利亚 1、乌克兰 1）6、本职线 VC / SDI / MC / DWDM 个人 ~15（与上重叠）、退信无备用地址 1。
  · 口径：桶 ⑦ 展会微信规则 —— 有公司名 + 土耳其 + 产品问 → 候选；无公司名 → 留 C 储备，由 Ady / Evelyn 微信追问公司名，报出即转候选（SC-3322「郑州供应商要去土耳其建厂，找新供应商」+ SC-3323「工业 2 光 8 PoE 要规格书价格」优先追问）。
  · 候选 1 = 土耳其 NAZEMCO（Osama；Ady 微信；要商业级 PoE 交换机）。永久 pass 1 = SC-2351 法国 aymeric-suchet@live.fr（退信 + 无备用地址 / 无电话 / 无域名 = 闸 0 刚性②；需求亦为无人机光纤桶）。
  · 留意：拉赫曼 Vatankhah（天地伟业员工，替伊朗客户找 PoE → 伊朗终端守界）、SC-3324（2.5G 家用 → 消费级）、worldcns KR（31 推 0 回，Simon 曾说多跟进）。

用法：python3 sieve_batches/g1_041.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批41_2026-10-29.md）
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

BATCH = 'G1-41'
DATE = '2026-10-29'
CODES = ["SC-2235", "SC-2237", "SC-2239", "SC-2243", "SC-2251", "SC-2252", "SC-2253", "SC-2261", "SC-2265", "SC-2266", "SC-2268", "SC-2271", "SC-2272", "SC-2273", "SC-2276", "SC-2277", "SC-2288", "SC-2293", "SC-2294", "SC-3322", "SC-3323", "SC-3324", "SC-2295", "SC-2297", "SC-2298", "SC-2300", "SC-2304", "SC-2309", "SC-2310", "SC-2313", "SC-2315", "SC-2318", "SC-2320", "SC-2321", "SC-2323", "SC-2325", "SC-2326", "SC-2327", "SC-2238", "SC-2329", "SC-2340", "SC-2343", "SC-2345", "SC-2347", "SC-2348", "SC-2349", "SC-2350", "SC-2351", "SC-2353", "SC-2354", "SC-2355", "SC-2358", "SC-2360", "SC-2362", "SC-2363"]

OVERRIDE = {
    'SC-2271': ('candidate', '土耳其 NAZEMCO（Osama；Ady 加了微信；要商业级 PoE 交换机 ✔）：公司名 ✔ 土耳其四主区 ✔ 对位产品问 ✔ 微信可达 ✔ → 闸 2 查底数（vknsorgula / 官网）后微信一页纸（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 锚）', []),
    'SC-2351': ('pass_final', '法国 aymeric-suchet@live.fr（阿里巴巴 RFQ「无人机光纤桶 10KM」；退信 bounce=1；无备用邮箱 / 无电话 / 无域名 / 无平台账号）：退信且无任何备用路径 = 闸 0 刚性② → 永久 pass（需求亦为无人机 = 品类不符）', []),
    'SC-2265': ('keep_C', '土耳其 Enes Talha Karaaslan（Evelyn 加了 WeChat；要工业级交换机报价单）：土耳其展会微信接触（四主区 ✔ 产品问 ✔ 微信可达 ✔）但无公司名 → 留 C 储备；Ady / Evelyn 微信追问公司名 + 一页纸，报出公司即转候选', []),
    'SC-2266': ('keep_C', '土耳其 Gokhan（Ady 加了微信；要 Catalog 和价格表，多口交换机）：土耳其展会微信接触（四主区 ✔ 产品问 ✔ 微信可达 ✔）但无公司名 → 留 C 储备；Ady / Evelyn 微信追问公司名 + 一页纸，报出公司即转候选', []),
    'SC-2273': ('keep_C', '土耳其 Sedat（Ady 加了微信；5 / 8 口工业级不带 PoE 和管理交换机 + IO 模块，用作工业自动化，要电子 catalog）：土耳其展会微信接触（四主区 ✔ 产品问 ✔ 微信可达 ✔）但无公司名 → 留 C 储备；Ady / Evelyn 微信追问公司名 + 一页纸，报出公司即转候选（STI-054GP / STI-154GP 对位，优先）', []),
    'SC-3322': ('keep_C', '土耳其（未具名；Evelyn 加了微信；外国人中文很好；「有工业级供应商在郑州，供应商打算在土耳其开工厂，所以要找新的供应商」= 真实换供应商意向 ✔）：土耳其展会微信接触（四主区 ✔ 产品问 ✔ 微信可达 ✔）但无公司名 → 留 C 储备；Ady / Evelyn 微信追问公司名 + 一页纸，报出公司即转候选（意向最强，优先追问公司名 + 现用型号）', []),
    'SC-3323': ('keep_C', '土耳其（未具名；Evelyn 加了 WeChat；主要要工业级 2 光 8 带 PoE 不带网管，要规格书和价格 = 具体型号问 ✔）：土耳其展会微信接触（四主区 ✔ 产品问 ✔ 微信可达 ✔）但无公司名 → 留 C 储备；Ady / Evelyn 微信追问公司名 + 一页纸，报出公司即转候选（STI-288GPM $78.9 对位，优先）', []),
    'SC-3324': ('keep_C', '土耳其（未具名；Evelyn 加微信；「2.5G 交换机，家用的」）：消费级 + 2.5G 口径待 SB-263 → 留 C（微信在，不主动）', []),
    'SC-2294': ('keep_C', '土耳其 拉赫曼 Vatankhah（Ady 加了微信；会中文，在天地伟业工作；要给他的伊朗客户（在迪拜有合同）找商业级 PoE 交换机）：天地伟业员工 = 非渠道 + 终端伊朗守界 → 留 C（微信在，不主动）', []),
    'SC-2237': ('keep_C', '乌克兰 Anton Dudnyk（阿里询盘「无人机」；仅电话）：守界乌克兰 + 品类不符 → 留 C', []),
    'SC-2239': ('keep_C', '伊朗 Bast-agir Security Company（bastagir.ir 正常；hotmail；隔壁摊位客户代理商，想了解 VC；WA 加不上）：伊朗守界 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2321': ('keep_C', '伊朗 Telecom Borna（telecomborna.ir 正常；Parisa Hesari，gmail；4 路视频 + 4 路电话 + 1 路反向数据）：伊朗守界 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2326': ('keep_C', '伊朗 Vista Cable（vistacable.com 正常；Reza，gmail；FTTH 跳线等无源产品）：伊朗守界 + 无源非 Saga 线 → 留 C', []),
    'SC-2288': ('keep_C', 'Reza Habibzadeh（表内荷兰，0911 伊朗手机 → 国别待核；gmail；百兆 MC 内电；WA 加不上）：百兆 MC 本职线 + 疑伊朗 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2243': ('keep_C', '叙利亚 Security Station（se-st.com no_mx；Eng Cheyath Abbar GM，hotmail；1 / 2 / 4 / 8ch，4V+4D+1E；WA 加不上）：叙利亚守界 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2238': ('keep_C', '俄罗斯 Arso（grabbel@mail.ru；监控工程经销商；8 推 0 回）：经销商 ✔ 俄罗斯点名区 ✔ 但无公司域名 / 无品牌证据 + 零回应 → 留 C 储备（一页纸一次后看）', []),
    'SC-2251': ('keep_C', '俄罗斯 Megatronicka / OOO Eltrade（megatronicka.com 正常；mail.ru；Сергей，去过中国留学；无需求记录）：零需求 → 留 C', []),
    'SC-2295': ('keep_C', '俄罗斯 Yevgeniy Tikhonov（7017620435@mail.ru；2018 年「1 光 2 电商业 PoE 千兆 100 个」；目标价太低没法谈）：个人 + 价格不合 → 留 C', []),
    'SC-2340': ('keep_C', '俄罗斯 oao-bgp@bk.ru（fiber switch；WA 加不上；7 推 0 回；「该公司也联系了其他人」）：无公司域名 + 零回应 → 留 C', []),
    'SC-2310': ('keep_C', '哈萨克斯坦 Adil Djumadullaev（mail.ru；2015 年「2 光 8 管理 PoE 工业级」，看了 ONV 的）：哈萨克先例在但个人无公司 + 陈旧 → 留 C 储备', []),
    'SC-2235': ('keep_C', '智利 VTA / Videoanalítica（vta.cl 正常，videoanalitica.cl 死；Ivan Barria，gmail；说是谈光端机合作，网站 VC 为主；19 推 0 回）：VC 本职线 + 零回应 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2252': ('keep_C', '韩国 Motionsys（daum；Park Seong Joong；3 对 3G SDI 带数据；9 推 0 回）：SDI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2272': ('keep_C', '法国 PGM Optical-Fiber（Jacques Knafo，gmail；HDMI 接线盒 / SDI 需求较大；18 推 0 回）：SDI 本职线有量 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2297': ('keep_C', '沙特 Al Manar Hitech（gmail；fiber to RJ45，TA210-FE/S20）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2300': ('keep_C', '秘鲁 Comercial Melboch SAC（hotmail；1v1a；WA 加不上）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2325': ('keep_C', '加拿大 Virjeem（gmail；之前买别人的 analog 被坑）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2327': ('keep_C', '巴西 Isaac Ramos（gmail；2015 年「1080P 2V1D 1 对」，有兴趣买）：VC 本职线 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2329': ('keep_C', '尼日利亚 Degorv Systems Services（Lateef Shoola；仅电话；公司专门搞 VC，后期说不需要了；16 推）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2347': ('keep_C', '阿联酋 Raj（仅电话；MC；16 推 0 回）：MC 本职线 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2348': ('keep_C', '印度 TVH（Subash，gmail；MROTEK media converter；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2349': ('keep_C', '赞比亚 Washington Zeddy（仅电话，+254 肯尼亚号 → 国别待核；即时对话「DWDM」）：DWDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2350': ('keep_C', '印度 Adarsh Electronics India（Rajesh Lohia，yahoo.co.in；OM210 视频光端机；WA 加不上）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2353': ('keep_C', '印度 Chashmita Engineers Pvt. Ltd（YS Bisht，gmail；1V / 1V1D projects；WA 加不上）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2362': ('keep_C', '阿联酋 Fast Vision Security（M.H. Tahir Managing Director；fastvis@eim.ae；need video to VGA converter；加不上）：视频转换本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2343': ('keep_C', '印度 Arrob（Ramesh Babu B，gmail；拿了册子换了名片没交谈；名片主要是跳线）：跳线非 Saga 线 → 留 C', []),
    'SC-2293': ('keep_C', '韩国 Worldcns（worldcns.kr no_mx；hanmail；网站主要 CCTV；31 推 0 回；Simon「可以尝试多跟进一下」）：CCTV 店 + 31 推零回应 → 留 C 储备（换稿一次后看）', []),
    'SC-2320': ('keep_C', '孟加拉 Success Computers BD（successcomputersbd.com 域死；Ismail Hossain；仅电话；工业 PoE 2 光 4 电；16 推 0 回）：域死但电话路径在 → 留 C 待巡检（下次仍死且电话不通即 pass）', []),
    'SC-2355': ('keep_C', 'Martin Brunell / Epoint Innovate（国别未填；gmail；BNC 转网 / CCTV PoE solution；拍了我们展位图；Founder；16 推 0 回）：EoC 非 Saga 线 + 无公司域名 → 留 C', []),
    'SC-2304': ('keep_C', '印度 Haflinger Technologies（Amol Patil Director；live / hotmail；2017 年「5 电口 PoE」；WA 加不上；10 推 0 回）：无公司域名 + 零回应 → 留 C', []),
    'SC-2358': ('keep_C', '墨西哥 Xporta（xporta.com.mx no_mx；hotmail；2020 年国际站；「网站是一个中间商的感觉」）：中间商 + 零互动 → 留 C', []),
    'SC-2360': ('keep_C', '多米尼加 Ariel Jesurun Hernandez（仅电话；千兆 PoE / MC，发了很多 RFQ；16 推 0 回）：个人 RFQ 户 → 留 C', []),
    'SC-2363': ('keep_C', '墨西哥 Josephine Napoleon（仅电话；「2 光 4 电百兆板子 50 个」；16 推 0 回）：百兆板卡 Saga 不供 → 留 C', []),
    'SC-2268': ('keep_C', '埃塞俄比亚 Haleb Trading plc（gmail；Cisco 设备）：品牌指定 + 无先例 → 留 C', []),
    'SC-2276': ('keep_C', '孟加拉 Venus Trade International（MD. Asgar Ali Lal Proprietor；gmail ×2；「说的没听懂」）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2277': ('keep_C', '乌干达 Xcom（Tonny Obwin，gmail；「最后决定从当地买」）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2298': ('keep_C', '泰国 Cleanworld Management（gmail；2020 年国际站；网站没搜出来）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2309': ('keep_C', '特立尼达 Virtual Surver（Caleb Hamilton，hotmail；「all」；WA 加不上）：疑可疑线索 → 留 C（不主动发）', []),
    'SC-2313': ('keep_C', '美国 Danar Supriyadi（gmail；16 年国际站，经常登录，会买周边产品）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2318': ('keep_C', '美国 Hmh Mchh（gmail；22 年新注册；1 个）：群发冷名单免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2315': ('keep_C', '菲律宾 Mark Anthony Vicente（gmail；商业 PoE 2 / 8 千兆，看过 E-wind 和磊通的）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2323': ('keep_C', '菲律宾 towercoph@gmail.com（刚注册；也在找商业级 FS）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2253': ('keep_C', '越南 Ngoc Duy Nguyen（gmail；工业 FS；1 推 0 回）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2261': ('keep_C', '缅甸 Yehtun（gmail；2 光 8 管理）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2354': ('keep_C', '阿根廷 Claudio Devincenti（gmail；2013 年「工业千兆 4 光 8」；1 推）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2345': ('keep_C', '意大利 Fabrizio Blasio（阿里巴巴询盘「升压 5 口」；无邮箱 / 电话）：阿里后台可回 = 路径存在（非闸 0）+ 升压 Saga 不供 → 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 41 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 331–385 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：土耳其展会微信接触 8、群发冷名单免费邮箱 30、仅电话 7、守界 6、退信 1。候选 1 = 土耳其 NAZEMCO（公司名 + 微信 + 商业 PoE 问价）。永久 pass 1 = SC-2351（退信无备用地址，闸 0 刚性②）。', '',
         '> 值得留意的留 C：土耳其微信无名户 7（SC-2265 / 2266 / 2273 / 3322 / 3323 优先追问公司名，报出即转候选；SC-2294 伊朗终端守界；SC-3324 消费级 2.5G）、Arso RU（监控工程经销商，8 推 0 回）、worldcns KR（31 推 0 回）、Success Computers BD（域死仅电话待巡检）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批41_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
