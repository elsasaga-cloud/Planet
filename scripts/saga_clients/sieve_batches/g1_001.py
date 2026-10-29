#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 01 批（2026-10-29）—— 「研究后定级 C」44 户 + 成单 / 样品 37 户 = 81 户（全部已有调研 JSON 或用户表成交记录，不需新网查）。

判定口径：docs/C池三闸筛选_方案_2026-10-29.md §3。
  pass_final 只给硬证据（清算 / 无名无联系路径 / 拉黑 / 纯无关行业且无采购迹象）；
  keep_C = 没判死（守界 / 巨头 / 伊朗制裁 / 区域外 / 终端用户 / 产品外 …），全部保留；
  candidate = 对位 ✔ 且（主区 or 成单 / 样品 / 回信 / 自有品牌）→ 闸 2 公司底数。
标签 dayjob_fit = 光端机 / DWDM / 光模块 为主（Simon 本职公司用得上，按 U117 不 pass）。

用法：python3 sieve_batches/g1_001.py        （幂等；写 data/saga_clients/sieve.json + docs/requirements/C池闸1_批01_2026-10-29.md）
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G1-01'
DATE = '2026-10-29'
DJ = ['dayjob_fit']

# code: (verdict, reason, tags)
V = {
    # ---- 研究后定级 C（44）----
    'SC-001': ('keep_C', '以色列战术通信方案商（SILVUS / Microhard 代理，印军案例）→ 军用守界；历史仅买 240W 电源；活着、回过 3 次信，留档不推进', []),
    'SC-002': ('keep_C', '港资中资同行（自称有 PoE 交换机工厂，+86 手机），沙特只是网点；同行不开发但不判死', []),
    'SC-004': ('keep_C', 'Murrelektronik 美国（集团 3,200 人，自有 PoE 交换机，要 UL/MIL）→ 巨头品牌厂；工程师回过 1 次技术问题；再来询按 B', []),
    'SC-005': ('keep_C', 'ACT / Intronics（TKH 集团，€18 亿）布线品牌，需求以无源为主「少量 switch」；回过 1 次 → 可被动报价，不主动', []),
    'SC-006': ('keep_C', '葡萄牙 B2B 运营商 Ar Telecom（Aire Networks 集团），RFQ 为 400G DWDM / 高速交换机 → 超出 Saga；DWDM 本职可参考', DJ),
    'SC-011': ('keep_C', '俄「主权互联网」DPI 集成商 АО ДЦОА（制裁敏感），历史从 GLsun 买光设备；成单户但不主动碰', DJ),
    'SC-012': ('keep_C', '拉脱维亚国铁安保子公司（国有 + 铁路守界），对工业管理交换机有兴趣、6 推 0 回、WA 加不上；留档', []),
    'SC-013': ('keep_C', '伊朗，2024 多轮问价（2 光 4 管理 / L2 2 光 8 / mini 工业），目标价太低；制裁口径不主动发；WA 已加 → 保留', []),
    'SC-019': ('keep_C', '伊朗伊斯法罕 CCTV 分销（Tiandy），WA 多次要价目；域名 NXDOMAIN 但 WA 在 → 制裁口径留 C', []),
    'SC-020': ('pass_final', '意大利商业登记：3MEDIALAB S.R.L. IN LIQUIDAZIONE（清算中，2025 员工 0，2023 营收 €60.8k）；历史定制 VC 一次性 → 主体消失', []),
    'SC-021': ('keep_C', '伊朗大不里士 IT 工程公司 NetPardaz（11–50 人，数据中心 / 安防 / 企业网），ISAF 拿彩页未交谈；制裁口径留 C', []),
    'SC-023': ('keep_C', '加纳学校终端（2 台 UniFi 同款 + 工业管理价目，主动来询，WA 已加）→ 非渠道，被动报价即可', []),
    'SC-028': ('keep_C', '西班牙公立中学 IT 老师阿里 RFQ 10G 光模块（学校自购，公共部门）→ 非渠道；光模块本职可参考', DJ),
    'SC-029': ('keep_C', '荷兰 Simac IDS（学生出勤云软件 + RFID 门禁，17 人，2026-03 售予 TimeEdit）；展会要 5 口工业小机 → 行业外但有采购迹象，未判死', []),
    'SC-032': ('keep_C', '利比亚（.ly + 218，ISAF 误记土耳其），WA 已加、最要商业 PoE；区域外但活着，若其土耳其有法人可重开', []),
    'SC-040': ('keep_C', '南非服务器 / 数据中心设备商 Compuspare：要 100G+ 交换机与 Alcatel 兼容 SFP 大批量、嫌贵；规格外；光模块本职可参考', DJ),
    'SC-044': ('keep_C', '尼泊尔税务部门（政府终端，gmail）要工业品价目，一次 thanks → 守界公共部门；留档不推进', []),
    'SC-049': ('keep_C', '巴勒斯坦 .ps（ISAF 误记土耳其）PoE 交换机 info@；区域外 + 物流收款风险；未触达 → 留档', []),
    'SC-051': ('keep_C', '利比亚 alhossan.ly（ISAF 误记土耳其），Ady 加了 WA、要商业 PoE；区域外但有 WA 路径 → 对方主动询价可被动报', []),
    'SC-056': ('keep_C', '主体不明：btmelectronics.com 名录归巴基斯坦消费电子站，联系人仅 gmail + WA；未交谈 → 不刚性，留 C', []),
    'SC-073': ('keep_C', '伊朗网店 ittelecom.ir（SFP 134 / PoE 58 / switch 14，自有 logo，产品线与 Saga 高度相似）→ 制裁口径留 C；若口径放开是对位户', DJ),
    'SC-083': ('keep_C', 'AddSecure（1,000+ 人，€200M，PE 控股）集团采购；展会看过 2 光 8 管理、15 推 0 回 → 巨头不 pass，留档', []),
    'SC-086': ('keep_C', 'InHand 映翰通美国站（中国大陆厂商办事处，自有工业交换机）→ 同行 / 大陆主体，不开发不判死', []),
    'SC-089': ('pass_final', 'newworldpolo.com = 伊斯坦布尔男装品牌电商站，希腊联系人为服装经销商（Yahoo 邮箱）；ISAF「没说什么、看了一眼」无任何 IT 采购迹象 → 纯无关行业', []),
    'SC-097': ('keep_C', '沙特「愿景 2030」军民服务本地化公司（AS9110 航空维修），要堆叠交换机 + 光模块 MC「其实需要其他品牌」→ 军工守界；活着', DJ),
    'SC-107': ('keep_C', 'AECL 加拿大原子能（联邦皇家公司），阿里 RFQ 为 5 口 PoE 交换机 PCB 板级件 → 守界 + 产品外；WA 已加 → 留档', []),
    'SC-109': ('keep_C', '荷兰 Solid Optics：独立式 WDM / EDFA / 光开关供应商（同行型）；Saga 无采购关系，但 DWDM 正是本职可用 → 标 dayjob', DJ),
    'SC-114': ('keep_C', 'Siklu（2024 并入 Ceragon 上市公司）毫米波设备厂，仅 marketing@，问过 10G 工业 MC 未成 → 巨头 / 厂商，不 pass', DJ),
    'SC-152': ('keep_C', '多米尼加安防批发分销（Provision-ISR / Hanwha / ZKTeco 授权，11–50 人；表误记美国），19 推 0 回、WA 已加 → 区域外真分销商，若开拓拉美可回 B', []),
    'SC-160': ('keep_C', '表内伊朗（联系人库尔德名，可能伊拉克库区），询工商业 PoE、看过官网；官网维护中页 → 核国别前留 C', []),
    'SC-167': ('keep_C', 'Westermo 奥地利 / 德语区办事处（瑞典工业网络厂商）→ 厂商办事处非渠道；8 推 0 回；不判死', []),
    'SC-169': ('keep_C', '伊斯坦布尔安防弱电集成商 Hafya（+90 212），ISAF 3 人来要防水机 / 4 光 8 电 PoE 网管规格「做军队项目」→ 军用守界 + 无 IP67；公司本身对位，留 C', []),
    'SC-189': ('keep_C', '克罗地亚 solarstore.hr（太阳能零售）Director 阿里 RFQ 100 pcs 1×2 锁存光开关（Saga 不供）；WA 已加 → 产品外，留档', []),
    'SC-192': ('keep_C', '美国 Garland Technology（TAP / Bypass / 分流器厂商），关注高速模块卡 SFP / DAC → 同行型厂商；光模块本职可参考', DJ),
    'SC-195': ('keep_C', '伊朗电信设备公司 Parman（WDM + 交换机），展会问工业 / 高速交换机、拍 DWDM 柜 → 制裁口径留 C；DWDM 本职可参考', DJ),
    'SC-200': ('keep_C', 'stc 巴林企业业务（运营商），联系人 gmail、无需求描述、电话疑录错 → 巨头运营商不 pass；留档', []),
    'SC-201': ('keep_C', 'Batelco 巴林国家运营商，联系人 gmail，2023 回「let me check / 有用」后无互动 → 巨头运营商不 pass；留档', []),
    'SC-204': ('keep_C', 'DCN 神州数码网络（中国厂商，欧洲分支 dcneurope.eu），历史与其印尼分支成一单工业 FS → 同行厂商不开发；成单户留档', []),
    'SC-240': ('keep_C', '波兰 Kępno 个体摄影工作室（NIP 6191857535，兼热泵），问过 24 口 FS / CCTV VC 报价、WA 已加 → 行业外但有采购迹象，未判死', []),
    'SC-244': ('keep_C', '土耳其 irtibatmerkezi.com 为公益组织信息平台（Moodle），询盘人 Mehmet Bora 身份无法确认；「问的很多产品较相关」、WA 已加 → 主体不明留 C', []),
    'SC-253': ('keep_C', 'Versa Technology（AETEK 美国伙伴）—— Simon T03 规则：Versa = C 不再回访；规则性留 C，不是永久 pass', []),
    'SC-255': ('keep_C', '伊朗个人（yahoo / gmail，+98 915），2024 要价目、问无关产品 → 制裁口径 + 个人；WA 已加留档', []),
    'SC-256': ('keep_C', '巴基斯坦 Spearhead Group：国防 / 执法供应商为主业（军队训练与供应），问过 4/8 口工业 PoE → 军用守界；活着', []),
    'SC-257': ('candidate', '沙特利雅得系统集成 / 数据中心业务 Al Rajhi Telecom：2024-10-22 DC Division Manager 回群发索样 STI-154GP（Simon 答 $36 非免费）→ 具名 KP + 对位 + 样品意向；区域次优 → 闸 2 查底数', []),
    # ---- 成单 / 样品（37）----
    'SC-1148': ('keep_C', '巴拉圭电视台 Canal Once（终端），要 HDMI/DVI 网络延长器样品（Saga 不供）、WA 已加 → 产品外；视频传输本职可参考', DJ),
    'SC-1173': ('candidate', '西班牙 JEVASO S.L. 电子部门：成单户（alberto@abbolli.com，「是个技术」）；欧洲主区 + 成单 → 闸 2 查底数、找采购 KP', []),
    'SC-1238': ('keep_C', '沙特 ESCC：买过 1V1D 样品、要价目、WA 已加 → 光端机类（本职可参考）；Saga 对位弱，留 C', DJ),
    'SC-1242': ('pass_final', '匈牙利 Off BEAT Bt（HD-SDI 光端机分销，成单户）表记「拉黑了」—— 关系已断死（闸 0 因成单转闸 1，人判同 G0-3）', DJ),
    'SC-1393': ('candidate', '乌兹别克斯坦 setko.uz：2018/19 买过洪瑞 PoE 交换机（CCTV 类）；成单 + 对位 ✔；退信但域名 MX 正常 → 闸 2 查底数 + 找新地址', []),
    'SC-1476': ('keep_C', '印尼 WIDEATEK：以前在中国买过收发器、问过光模块；域名 NXDOMAIN、仅电话 → 光模块本职可参考；留 C', DJ),
    'SC-1493': ('candidate', '南非 Duxbury Networking（知名分销商）：要过 8 光 8 管理 PoE 样品、「也卖很多商业 PoE」、常用邮件沟通；16 推 0 回 → 分销体量 + 对位 ✔ → 闸 2', []),
    'SC-1662': ('keep_C', '斯威士兰 gmail 阿里询盘：升压 5 口 2 台样品测试（Saga 无升压 PoE）→ 产品外 + 免费邮箱；活着，留 C', []),
    'SC-1835': ('keep_C', '伊拉克 Zenyar（台湾采购办）买 1V1D 样品、WA 已加；zenyar.net NXDOMAIN → 光端机类本职可参考；留 C', DJ),
    'SC-2058': ('keep_C', '越南 VSL：买过迈威 MC；9 推 0 回 → 成单户、产品为 MC（Saga 仅 STC-110XGE）；留 C', DJ),
    'SC-2066': ('candidate', '美国 ethoswitch.com：买过台湾 KONTEN 工业 FS「质量不错」；退信但域名 MX 正常 → 北美主区 + 成单 + 对位 ✔ → 闸 2 找新 KP', []),
    'SC-2105': ('keep_C', '沙特 Mekshaf：Melody 时期买 4V1D 样品（4ch $200 / 8ch $400），gmail、WA 加不上 → 光端机类本职可参考；留 C', DJ),
    'SC-2106': ('candidate', '澳大利亚 Optimal Cable Services（现属 AFL）：2007 年起合作、买过 MC / CWDM、「偶尔有反应」、23 次跟进 → 长期成单户 + 体量；产品偏光传输 → 闸 2 核现状并标 dayjob', DJ),
    'SC-2107': ('keep_C', '越南 QT System Solutions（EOC 历史成单额较高，Owner），表记「似乎是拉黑了」不确定 → 成单户不判死；Simon 若确认被拉黑则 pass', []),
    'SC-2116': ('keep_C', '美国 hotmail 个人问 sample policy、WA 加不上；无公司主体 → 无价值但活着，留 C', []),
    'SC-2249': ('keep_C', '印度 Jupiter Systems：成单（各种光产品），无邮箱、域名正常 → 光产品本职可参考；留 C', DJ),
    'SC-2344': ('keep_C', '新加坡 DenseLight 半导体：2011 年自用买 2 台收发器，联系人退信（域名正常）→ 终端一次性；留 C', DJ),
    'SC-2361': ('keep_C', '肯尼亚 Electro Research：2010 年买过一次跳线、后无反应 → 一次性小单；留 C', []),
    'SC-2368': ('candidate', '巴拉圭 Radio ZP30：HDMI + USB over SM fiber 光端机「多次下单」→ 复购户；产品属本职线（dayjob），P 池是否收 dayjob 户待 Q-70 → 先入候选', DJ),
    'SC-2387': ('keep_C', '巴林 Microcomms：买过两次光端机 SC 口；域名 NXDOMAIN、无 WA → 成单户（光端机）；留 C 待新联系路径', DJ),
    'SC-2482': ('keep_C', 'PCCW 香港（运营商巨头）：买过一台 OM4205 后退信、无其他联系人 → 巨头不 pass；留档', DJ),
    'SC-2552': ('keep_C', '印度 Radius Infratel：成单 ONU PCB 等（Saga 不供 GPON）；无邮箱 → 产品外；留 C', []),
    'SC-2580': ('keep_C', '印度 gmail 个人要高清 4V1D 样品、WA 已加 → 光端机类；留 C', DJ),
    'SC-259': ('candidate', '土耳其 Sami Çeuik（ISAF）：用光网视交换机、政府项目、问 500 台 2 光 8 PoE 网管价、最后一天买了 1 台 2 光 10 电 PoE 样机 $100、Evelyn 加了微信 → 土耳其主区 + 成单 + 对位 ✔；表内无邮箱 → 闸 2 先查公司', []),
    'SC-2680': ('pass_final', '菲律宾「Ronaldo Cutterman」：1 对 AHD 1V1D 一次性成交，无邮箱 / 电话 / WA / 公司 → 无任何联系路径（G0-1 口径，闸 0 因成单转闸 1 后人判）', []),
    'SC-2709': ('keep_C', '印尼 delameta.com：成单户、官网有 CCTV 项目；退信但域名正常 → 留 C 待新地址', []),
    'SC-2896': ('keep_C', '哈萨克 Carat-Prognoz：2012 买 1 对 2V1D2A、「需求不大」、Spam 注 → 一次性成单；留 C', DJ),
    'SC-296': ('candidate', '韩国 lsipro@hanmail.net：3G / HD-SDI 光端机「多次下单」→ 复购户（韩国为次优区）；产品属本职线 → 候选 + dayjob，待 Q-70', DJ),
    'SC-3070': ('keep_C', '法国 ISP IMS Networks / e-teleport：要 CWDM & DWDM 价格与样品，WA 加不上；Simon 判定不行 → 留 C；DWDM 本职可参考', DJ),
    'SC-3206': ('keep_C', '尼日利亚 Worldwide Net（表名误作 AXIS）：2011 年来过公司、买过一次收发器；域名 NXDOMAIN、「可加」WA 号在 → 留 C', DJ),
    'SC-3212': ('keep_C', '特立尼达 BVR Technologies（yahoo）：要 VC 样品、WA 加不上 → 光端机类；留 C', DJ),
    'SC-3408': ('pass_final', '印度（未具名）：买过飞宇跳线一单，无公司名 / 邮箱 / 电话 / WA → 无任何联系路径（G0-1 口径，闸 0 因成单转闸 1 后人判）', []),
    'SC-371': ('candidate', '西班牙 Visiotech（大型安防分销商，自有品牌 Safire，产品中见中科德能）：成单记录 + OEM 交换机合作邮件、31 次跟进 → 欧洲主区 + 自有品牌 + 分销体量 → 闸 2', []),
    'SC-385': ('keep_C', '印度 Computer Point：成单 HDMI units（Saga 不供）→ 产品外；留 C', []),
    'SC-661': ('keep_C', '叙利亚 ALAMAN：买过一次样品（1V1D）、自有品牌、后无反应；两域 NXDOMAIN、WA 加不上 → 制裁 / 区域外；留 C', DJ),
    'SC-667': ('candidate', '克罗地亚 H1 Telekom：成样品单（SFP / 收发器）、「常回复」、17 次跟进 → 欧洲 + 样品 + 回信；产品偏光模块 → 候选 + dayjob，闸 2 核', DJ),
    'SC-678': ('candidate', '英国 QVIS（安防品牌，在华有摄像机工厂）：问过 fiber optics 想买样品、「有需要会直接联系」；从未邮件触达 → 英国主区 + 品牌商 → 闸 2 查底数再定', []),
}


def main():
    assert len(V) == 81, len(V)
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    for code, (verdict, reason, tags) in V.items():
        assert code in ents and ents[code].get('grade') == 'C', code
        assert verdict in ('pass_final', 'keep_C', 'candidate'), (code, verdict)
        assert len(reason) >= 12, code
        cur = sv.get(code) or {}
        if cur.get('gate', 0) >= 1 and cur.get('batch') != BATCH:
            continue  # 更高闸 / 别的批已判，不覆盖
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True, 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    # 批报告
    from collections import Counter
    c = Counter(v[0] for v in V.values())
    L = [f'# C 池 · 闸 1 · 第 01 批（{DATE}）—— 研究后定 C 44 + 成单 / 样品 37 = 81 户', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标 dayjob_fit {sum(1 for v in V.values() if v[2])} 户。', '',
         '> **Simon 看法**：任何一户一句话可改。pass_final 只给了硬证据（清算 / 无名无联系路径 / 拉黑 / 纯无关行业无采购迹象）。', '']
    for verdict, title in (('pass_final', '永久 pass'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批01_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
