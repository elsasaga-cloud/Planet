#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 16 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 221–275 户（按综合分序，SC-593 … SC-698）。

构成：俄罗斯群发 12–18 次 0 回户与 0 触达户、南非 15–17 推 0 回户、越南 / 菲律宾 / 中东零星、台湾光开关厂、俄区平台询盘（数量信号）。
  · 口径同桶 ⑥ 首批：四主区外默认留 C；「已进口中国 / 台湾同类品牌」+ 俄 / 印 / 韩（或同区先例 ZA / UZ）→ 闸 2 低优先；自有品牌 = OEM 品牌商不限国别 → 闸 2 低优先；数量询盘 + 对位 → 闸 2。
  · 候选 5 = IA Control ZA（与台湾 Korenix 合作）/ Industrial Nets RU（与深圳 Comark + N-Net 合作）/ Ipmatika RU（Wi-Tek + TG-NET 工业 FS）/ Scoop Distribution ZA（Cudy + 多牌中型分销）/ Lansale RU（「150 pcs 千兆 1 光 2 PoE」数量询盘）→ 闸 2 查底数。
  · 永久 pass 2：SC-697 alichecker.info、SC-698 aliradar.com（速卖通比价 / 追踪工具站，非买家、零互动 = 纯无关）。
  · 其余留 C：俄罗斯无品牌证据或仅光模块（adventa · altcam · future-tech Gigalight 模块 · gs-p · nagtech · nk-group · nvc-it · roxton · rus-telcom · telecamera · zscom · 5sgroup · aladis）/ 死域名待巡检（1-security no_mx · abn.ru dead · invisystems nxdomain 600 只注入器）/ 南非小零售（hdcabling · phendula · redstrut ONV · skynatics ONV）/ 乌克兰守界（setevoe Utepo）/ 中资分支（ZKTeco RU）/ 同行（CASwell · NADDOD · Silicom · Kennine · Wanshing）/ 越南 · 菲律宾 · 中东 · 拉美 储备（Simbacorp BTON · Teltrends Volktek · Coulomb 帧田 · Smartix Soltech 带标）/ 名牌专营（Pride System D-Link · METS Allied Telesis）/ 本职线 dayjob_fit（VC · WDM · DCI · 400G 相干）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_016.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批16_2026-10-29.md）
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

BATCH = 'G1-16'
DATE = '2026-10-29'
CODES = ["SC-593", "SC-595", "SC-596", "SC-597", "SC-602", "SC-605", "SC-607", "SC-608", "SC-609", "SC-610", "SC-611", "SC-616", "SC-618", "SC-619", "SC-621", "SC-622", "SC-623", "SC-625", "SC-627", "SC-630", "SC-632", "SC-633", "SC-635", "SC-636", "SC-637", "SC-638", "SC-640", "SC-642", "SC-643", "SC-644", "SC-646", "SC-647", "SC-648", "SC-650", "SC-653", "SC-654", "SC-1000", "SC-1001", "SC-655", "SC-657", "SC-660", "SC-664", "SC-666", "SC-668", "SC-669", "SC-670", "SC-673", "SC-675", "SC-677", "SC-684", "SC-688", "SC-690", "SC-692", "SC-697", "SC-698"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-697': ('pass_final', '俄罗斯 alichecker.info（速卖通卖家 / 价格检查工具站；表内「商业 PoE 很多家的外壳，有 Hiseeu」= 站内商品抓取，非经销商、非买家）零互动 → 纯无关非买家，永久 pass', []),
    'SC-698': ('pass_final', '俄罗斯 aliradar.com（速卖通比价 / 追踪浏览器插件站；表内「ONV 的工业 FS」= 站内商品抓取，非经销商、非买家）零互动 → 纯无关非买家，永久 pass', []),
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-622': ('candidate', '南非 IA Control（iacontrol.co.za；工业 MC / FS，表内「在和台湾 Korenix 合作」）：进口台湾同类 ✔ 对位 ✔ + 同区先例 Duxbury / MiRO；群发 15 次 0 回 → 闸 2 查底数（CIPC 镜像）；低优先', []),
    'SC-623': ('candidate', '俄罗斯 Industrial Nets（industrialnets.ru / i-nets.ru；工业 FS 带串口，表内「和深圳 Comark 合作，还有 N-Net」）：进口中国同类 ✔ 对位 ✔ Simon 点名俄罗斯；群发 17 次 0 回 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-625': ('candidate', '俄罗斯 Ipmatika（ipmatika.ru / ipmatika.com；表内「用了 Wi-Tek 和 TG-NET 的工业 FS，工商业 FS 基本是 Wi-Tek 的」）：进口中国同类 ✔ 对位 ✔ 俄罗斯分销；群发 17 次 0 回 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-644': ('candidate', '南非 Scoop Distribution（scoop.co.za；无线 / 网络中型分销，表内「商业 PoE Cudy 的，也有一些有名的牌子」）：进口中国同类 ✔ 对位 ✔ 中型分销 + 同区先例；群发 15 次 0 回 → 闸 2 查底数（CIPC 镜像）；低优先', []),
    'SC-670': ('candidate', '俄罗斯 Lansale LLC（lansale.ru；国际站询盘「150 pcs 千兆 1 光 2 PoE」= 数量信号）：数量 ✔ 对位 ✔（小口工业 / 商用 PoE，STI-154GP 近口型）Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-595': ('keep_C', '沙特 Smartix ME（smartix-me.com；全线卖 Soltech 产品、带标卖）：进口中国同类 ✔ 但四主区外非点名国；群发 19 次 0 回 → 留 C（储备）', []),
    'SC-609': ('keep_C', '台湾 CASwell（cas-well.com；网络设备 ODM，高速 switch / SD-WAN）：台湾同行 → 留 C', []),
    'SC-610': ('keep_C', '哥伦比亚 Coulomb Tecnología（coulombtecnologia.com；帧田的商业 PoE）：进口中国同类 ✔ 但拉美非点名国；群发 6 次 0 回 → 留 C（储备）', []),
    'SC-616': ('keep_C', '俄罗斯 Future-Tech（future-tech.ru；买 Tibtronix / Gigalight 的 SFP 模块 + MC）：光模块 = 本职线；群发 17 次 0 回 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-621': ('keep_C', '澳大利亚 Hyperscalers（hyperscalers.com；服务器 / OCP 集成，DC 对位）：四主区外非点名国 + 零互动 → 留 C（CENTEC 敲门砖可择机）', []),
    'SC-632': ('keep_C', '新加坡 NADDOD（naddod.com；中国光模块 / 交换机品牌海外站）：同行 → 留 C', []),
    'SC-640': ('keep_C', '南非 Redstrut（redstrut.co.za；ONV 的 MC + 商业 FS，似乎没有工业 FS）：进口中国同类 ✔ 但小零售；群发 15 次 0 回 → 留 C（储备）', []),
    'SC-646': ('keep_C', '乌克兰 Setevoe（setevoe.com.ua；PoE Switch 有 Utepo 的 / CWDM SFP）：进口中国同类 ✔ 但乌克兰 = 守界（难，非永久 pass）→ 留 C', []),
    'SC-647': ('keep_C', '以色列 Silicom（silicom-usa.com；bypass 网卡 / 设备厂商）：同行 + bypass Saga 不供 → 留 C', []),
    'SC-648': ('keep_C', '南非 Skynatics（skynatics.com；商业 PoE 有 ONV 的）：进口中国同类 ✔ 但小零售；群发 15 次 0 回 → 留 C（储备）', []),
    'SC-650': ('keep_C', '俄罗斯 Telecamera.ru（CCTV 电商；VC 4V1D 似停产 / 商业 PoE 配件卖好几家的）：无具体中国品牌证据 + 本职线 VC；群发 18 次 0 回 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1000': ('keep_C', 'ZKTeco（zkteco.com，表内国别俄罗斯 = 俄区分支；中国安防巨头）：中资分支 → 留 C', []),
    'SC-655': ('keep_C', '俄罗斯 1-security.ru（域 no_mx，无退信；SFP / MC / PoE / FS）：死域名无退信 → 留 C 待巡检', []),
    'SC-666': ('keep_C', '越南 Dat Xanh Group（datxanh.vn；房地产集团，收发器 / 交换机自用）：终端 + 四主区外 → 留 C', []),
    'SC-669': ('keep_C', '俄罗斯 LLC Kompleksnye Systemy Virtualuza（invisystems.com 域 nxdomain；2019 国际站询盘「PoE injector 挂墙式 600 个」）：注入器 Saga 不供 + 死域名无退信 → 留 C 待巡检', []),
    'SC-673': ('keep_C', '沙特 METS – Mohammad Abdulla Eissa Trade（mets-ksa.com；Allied Telesis 品牌交换机）：名牌专营 + WA 加失败 → 留 C', []),
    'SC-675': ('keep_C', '摩尔多瓦 PRIDE SYSTEM SRL（pride.md；分销 / 批发，2011 国际站询 D-Link PoE 管理型）：名牌专营 + 零互动 → 留 C（储备）', []),
    'SC-684': ('keep_C', '俄罗斯 abn.ru（域 dead，无退信；工业 FS / MC / SFP）：死域名无退信 → 留 C 待巡检', []),
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
    L = [f'# C 池 · 闸 1 · 第 16 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 221–275 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：俄罗斯群发 12–18 次 0 回与 0 触达户、南非 15–17 推 0 回户、越 / 菲 / 中东零星、台湾光开关厂、俄区平台数量询盘。口径同桶 ⑥ 首批。候选 5 = IA Control（ZA，Korenix）/ Industrial Nets（RU，Comark + N-Net）/ Ipmatika（RU，Wi-Tek + TG-NET）/ Scoop（ZA 中型分销，Cudy）/ Lansale（RU，150 台数量询盘）；永久 pass 2 = alichecker.info / aliradar.com（速卖通比价工具站，非买家零互动）。留 C：俄罗斯无品牌证据或仅光模块、死域名待巡检、南非小零售、乌克兰守界、中资分支、同行、东南亚 / 中东 / 拉美储备、名牌专营、本职线 dayjob_fit。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批16_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
