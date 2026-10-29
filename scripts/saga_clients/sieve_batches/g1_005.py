#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 05 批（2026-10-29）—— 桶 ⑤「企业邮箱 · 四主区+波兰」前 165 户（按编号序，SC-008 … SC-1491）。

桶 ⑤ 共 660 户（有企业邮箱、北美 / 欧洲 / 土耳其 / 波兰），其中 115 户有调研 JSON。本批口径（方案 §3 + §5）：
  · 永久 pass 仅：纯无关行业 + 无任何互动（金属建筑 / MIDI 软件 / 租约网站 / 比价平台 / 招标门户 / SaaS / 支付软件 / 个人无购买 RFQ）。
    付过钱的个人零售买家（Shopify / RTS 订单）不 pass —— 成单是准入信号，哪怕只买过 1 台。
  · 候选：对位 ✔ + 主区 / 欧洲 + 硬信号（已在卖 ONV / Utepo / 宇航 / credfiber / 洪瑞 / Planet 等中国同类品牌 = 进口经验；或分销商主体）。冷户进池仍要过 §5 ≥4 条。
  · 其余留 C：守界 / 巨头 / 同行 / 厂商 / 公共部门 / 终端用户 / 品类不符（光端机 / WDM / bypass / 无源 → dayjob_fit）/ Q-33 渠道冲突（不主动碰）。
  · 「WDM / CWDM / bypass / 光开关」整段（SC-1041…SC-1136）是一份光通信厂商名单，几乎全为同行 / 厂商 → 留 C + dayjob_fit。

用法：python3 sieve_batches/g1_005.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批05_2026-10-29.md）
"""
import os
import re
import sys
import json
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G1-05'
DATE = '2026-10-29'
CODES = ["SC-008", "SC-014", "SC-015", "SC-016", "SC-017", "SC-022", "SC-025", "SC-026", "SC-027", "SC-030", "SC-031", "SC-033", "SC-034", "SC-035", "SC-036", "SC-037", "SC-042", "SC-045", "SC-052", "SC-057", "SC-058", "SC-059", "SC-060", "SC-061", "SC-062", "SC-063", "SC-064", "SC-065", "SC-066", "SC-068", "SC-070", "SC-071", "SC-072", "SC-074", "SC-077", "SC-078", "SC-087", "SC-090", "SC-091", "SC-092", "SC-099", "SC-1004", "SC-1006", "SC-1009", "SC-1010", "SC-1013", "SC-1014", "SC-1023", "SC-1031", "SC-1033", "SC-104", "SC-1041", "SC-1046", "SC-1047", "SC-1048", "SC-1049", "SC-105", "SC-1050", "SC-1051", "SC-1052", "SC-1054", "SC-1055", "SC-1058", "SC-1060", "SC-1061", "SC-1062", "SC-1063", "SC-1064", "SC-1065", "SC-1067", "SC-1068", "SC-1069", "SC-1070", "SC-1072", "SC-1073", "SC-1074", "SC-1075", "SC-1076", "SC-1077", "SC-1080", "SC-1086", "SC-1089", "SC-1091", "SC-1093", "SC-1094", "SC-1095", "SC-1097", "SC-1098", "SC-1099", "SC-1100", "SC-1101", "SC-1103", "SC-1104", "SC-1105", "SC-1107", "SC-1111", "SC-1113", "SC-1114", "SC-1115", "SC-1119", "SC-112", "SC-1120", "SC-1121", "SC-1122", "SC-1125", "SC-1126", "SC-1127", "SC-1128", "SC-1132", "SC-1133", "SC-1136", "SC-1141", "SC-115", "SC-1158", "SC-116", "SC-1160", "SC-1166", "SC-1168", "SC-117", "SC-118", "SC-1181", "SC-1184", "SC-1189", "SC-119", "SC-1192", "SC-1194", "SC-120", "SC-121", "SC-1215", "SC-122", "SC-1220", "SC-1226", "SC-123", "SC-1230", "SC-1237", "SC-124", "SC-125", "SC-126", "SC-1268", "SC-127", "SC-128", "SC-129", "SC-1297", "SC-130", "SC-131", "SC-132", "SC-133", "SC-1335", "SC-134", "SC-1347", "SC-135", "SC-136", "SC-137", "SC-1395", "SC-1397", "SC-1414", "SC-1427", "SC-144", "SC-1443", "SC-1450", "SC-146", "SC-1468", "SC-148", "SC-1490", "SC-1491"]

DJ_RE = re.compile(r'光端机|\bVC\b|HDMI|SDI|DWDM|\bWDM\b|CWDM|OTN|SFP|模块|收发器|\bMC\b|光猫|OLP|光缆|AHD|CVI|TVI|BNC|Bypass|光开关|光纤|GBIC|DVI|延长器|转光|V1D|同轴|CCTV|无源|PON|光保护|跳线|optical converter|fiber', re.I)
OEM_RE = re.compile(r'自己的logo|自己的牌子|刷了|刷他们|贴牌|SKD|own logo|丝印', re.I)

OVERRIDE = {
    # ---- 永久 pass：纯无关行业 + 无互动（刚性）----
    'SC-015': ('pass_final', '瑞士 Schnetzler Metallbau AG（金属 / 玻璃建筑施工）2015 年阿里 RFQ「10G 交换机」一次、gmx 免费邮箱、此后零互动 → 纯无关行业，永久 pass', []),
    'SC-022': ('pass_final', '英国 Canonbury / mcelroy.co.uk（在线租约文书服务站）2014 年 RFQ「5 口 PoE」一次、电话加不上、零互动 → 纯无关行业，永久 pass', []),
    'SC-025': ('pass_final', '德国 Bome Software（MIDI 音乐软硬件）2014 年 RFQ「5 电口板子」（板级，Saga 不供）、电话加不上、零互动 → 纯无关行业，永久 pass', []),
    'SC-030': ('pass_final', '加拿大 Visionar Window Systems（窗户五金制造商）单次 RFQ「2 光 10 电」自用、零互动 → 纯无关行业，永久 pass', []),
    'SC-058': ('pass_final', '意大利 FBK SRL（医疗 AI 招标软件）RFQ「100G 80/100KM 光模块」（Saga 不供）、零互动 → 纯无关行业 + 品类外，永久 pass', []),
    'SC-061': ('pass_final', '丹麦 gill.dk（个人摄影 / 铁路照片网站）个人 RFQ「2+16 Passive PoE」（Saga 无此款）、未购买、WA 加不上 → 个人无购买，永久 pass', []),
    'SC-070': ('pass_final', '德国 INLOCON（招标商机信息门户，非集成商、不经销硬件）7 次跟进零回复 → 纯无关行业，永久 pass', []),
    'SC-099': ('pass_final', '土耳其 Akakçe（比价平台；联系仅 destek@ 客服 / ik@ 人事）2 次跟进零回复 → 非销售方、纯无关，永久 pass', []),
    'SC-1268': ('pass_final', '捷克 heureka.cz 个人地址（Heureka = 比价平台，非销售方）、零互动 → 纯无关行业，永久 pass', []),
    'SC-125': ('pass_final', '英国 FloLIVE（蜂窝 IoT 连接 SaaS 平台，不采购以太网交换机）1 次跟进零回复 → 纯无关行业，永久 pass', []),
    'SC-129': ('pass_final', '德国 INOTEC（inotec.digital 文档 / 调研 / 运维软件公司，不经销硬件）7 次跟进零回复 → 纯无关行业，永久 pass', []),
    'SC-130': ('pass_final', 'Linktree（「Link in bio」SaaS 平台；表内国别爱沙尼亚为域名误判）5 次跟进零回复 → 纯无关行业，永久 pass', []),
    'SC-135': ('pass_final', '瑞典 PacketFront Software（网络编排 / OSS 纯软件）1 次跟进零回复 → 纯无关行业，永久 pass', []),
    'SC-137': ('pass_final', '捷克 Switchio（支付编排平台，「switch」为支付路由语义）4 次跟进零回复 → 纯无关行业，永久 pass', []),
    # ---- 候选 → 闸 2 ----
    'SC-1009': ('candidate', '土耳其 Aras Varel / Varel Alarm（工商业 FS，在卖 Utepo）：土耳其主区 + 已进口中国同类品牌 + 对位 ✔；arasvarel.com 无 MX 但 varelalarm.com 正常 → 闸 2 查底数 + 换地址', []),
    'SC-1010': ('candidate', '英国 Crony Trading Ltd（商业 PoE，用的洪瑞的；网站品类杂）：英国主区 + 已进口同款供应链产品 + 对位 ✔；曾退信但域名正常 → 闸 2 查底数（Companies House）再定', []),
    'SC-1013': ('candidate', '德国 Gemaxx Network（ONV 工业 FS）：德国主区 + 已进口中国同类品牌 + 对位 ✔；曾退信但域名正常 → 闸 2 查底数 + 找新地址', []),
    'SC-1014': ('candidate', '西班牙 GTLAN（工业 FS，GXcom + 宇航；有工业 10G 5 口产品页）：欧洲 + 已进口中国同类品牌 + 对位 ✔；曾退信但域名正常 → 闸 2 查底数', []),
    'SC-1033': ('candidate', '比利时 Bausch Datacom（网络产品分销：二层光纤交换机、SFP）：欧洲 + 分销商主体 + 对位 ✔，冷户（未推送过）→ 闸 2 查底数，入池需 §5 ≥4 条', []),
    'SC-1181': ('candidate', '匈牙利 Agenda Age（SFP / MC / 工业 FS，在用深圳 credfiber 的）：欧洲 + 已进口中国同类品牌 + 对位 ✔；15 次跟进无回复（冷）→ 闸 2 查底数', ['dayjob_fit']),
    'SC-1194': ('candidate', '挪威 Eldi（宇航的工业 FS / SFP，产品较少）：欧洲 + 已进口中国同类品牌 + 对位 ✔；15 次跟进无回复（冷）→ 闸 2 查底数', []),
    'SC-1215': ('candidate', '拉脱维亚 router.lv（switch 等，有少量 Utepo）：欧洲 + 已进口中国同类品牌 + 对位 ✔；15 次跟进无回复（冷，小国）→ 闸 2 查底数，低优先', []),
    'SC-1220': ('candidate', '芬兰 Starelec（Networking，有 ONV 的 switch）：欧洲 + 已进口中国同类品牌 + 对位 ✔；15 次跟进无回复（冷）→ 闸 2 查底数', []),
    'SC-1230': ('candidate', '美国 Wantec（周边产品 + 宇航的工业 FS）：美国主区 + 已进口中国同类品牌 + 对位 ✔；18 次跟进无回复（冷）→ 闸 2 查底数', []),
    'SC-1297': ('candidate', '美国 Winncom Technologies（「实力不错的分销商」，无线 / 网络分销）：美国主区 + 分销商主体 + 对位 ✔；体量偏大、10 次跟进无回复 → 闸 2 查底数，看是否有白牌 / 工业线入口', []),
    'SC-1335': ('candidate', '捷克 Discomp（光纤设备 / CWDM / SFP，有部分 Planet 的）：欧洲 + Planet 渠道（对位 ✔）+ 分销主体；冷户 → 闸 2 查底数（与 Planet 仓并线核对）', ['dayjob_fit']),
    'SC-1443': ('candidate', '加拿大 Infinique（几乎都是 ONV 的、刷了他们的 logo = 现成 OEM 买家）：北美主区 + 进口经验 + 自有品牌 OEM（30% 口径）；曾退信但域名正常、16 次跟进无回复 → 闸 2 查底数 + 找新地址', ['oem_target']),
    'SC-1450': ('candidate', '美国 Nodexon / Microlink（长飞、中科的工业 FS，商业 L3 核心，光配件多）：美国主区 + 已进口中国同类品牌 + 对位 ✔；曾退信但两域名正常 → 闸 2 查底数', ['dayjob_fit']),
    # ---- 需要专门说明的留 C ----
    'SC-105': ('keep_C', '加拿大「Moonversion」（营地主任 RFQ 2,300 个收发器，不合常理；官网 unreachable、WA 加不上）→ 疑似无效线索但不满足刚性（有邮箱域曾存在）；留 C，下次巡检仍死即 pass', ['dayjob_fit']),
    'SC-077': ('keep_C', '英国 Charter Controls（已备货 SmartByte 工业非管理机 = 原厂 / 英国进口商客户）→ Q-33 渠道冲突待裁，不主动碰；留 C', []),
    'SC-078': ('keep_C', '英国 Innon（与 Charter Controls 同属 SmartByte 英国经销渠道）→ Q-33 待裁，不主动碰；留 C', []),
    'SC-146': ('keep_C', '英国 Electric Bray（在售 Smartbyte 5 口工业机）→ Q-33 待裁，不主动碰；留 C', []),
    'SC-148': ('keep_C', '波兰 napad.pl / ipox.pl（SmartByte 经销名单内）→ Q-33 待裁，不主动碰；留 C', []),
    'SC-052': ('keep_C', '德国 Axellence GmbH（芯片 / IP 代理，含 CENTEC）→ 芯片层面不经销整机；留 C（CENTEC 线索可参考，不推销）', []),
    'SC-1023': ('keep_C', '英国 Optifab（MC / 工业 MC / SFP / DAC / 无源；Catherine Caldwell）：optifab.com null MX（邮件已关）但官网未核 → 不刚性；留 C（下次巡检官网也死即 pass）', ['dayjob_fit']),
    'SC-1166': ('keep_C', '法国 Techtel（进口商，问过几次无源产品，加了 Skype）→ 有进口经验但需求为无源（Saga 不供）；留 C，若问交换机再接', ['dayjob_fit']),
    'SC-1189': ('keep_C', 'bicar.by（.by 白俄罗斯域，表内国别爱沙尼亚）工业 FS，15 次无回复 → RU/BY 收款路径未定 + 冷；留 C', []),
    'SC-1192': ('keep_C', '爱沙尼亚 Datasys（销售平台，「似乎是国内的供应商」）→ 主体不明；留 C', []),
    'SC-1226': ('keep_C', 'Texim Europe（工业 FS，「像同行的」；国别未填）→ 疑似同行 / 元器件分销；留 C', []),
    'SC-1491': ('keep_C', '荷兰 Distri-X（问工业 PoE 带 NAT = L3 功能，Saga 工业线无；表内标不再跟进 / Spam 为我方备注）→ 不刚性；留 C', []),
    'SC-1158': ('keep_C', '德国 LANCOM Systems（自有品牌交换机厂商，17 次群发无回复）→ 同行 / 厂商；留 C', []),
    'SC-136': ('keep_C', '瑞士 Selectron Systems（轨道车载 EN50155 唯一场景；表内「有回复」待核）→ 守界轨道；留 C', []),
}

SUB_WHY = [
    (r'渠道冲突|Q-33', 'Q-33 渠道冲突（SmartByte 经销名单）待裁，不主动碰；留 C'),
    (r'守界', '守界行业（军工 / 轨道 / 公共部门 / 关键基础设施）：不做但不 pass；留 C'),
    (r'体量过大|巨头|集团', '巨头 / 集团 / 大型分销：按 U117 不 pass；留 C'),
    (r'同行|厂商|自研', '同行 / 自有品牌厂商，非渠道客户；留 C'),
    (r'运营商', '运营商 / ISP：非渠道客户；留 C'),
    (r'中国厂商', '中国厂商海外办事处（采购在国内总部）；留 C'),
    (r'个人买家', '个人零售买家（付过钱）：不 pass；留 C（来询被动报价）'),
    (r'终端用户', '终端用户自用（有购买或询盘）：不 pass；留 C（来询被动报价）'),
    (r'品类不符', '需求 / 主业为 Saga 不供品类（光端机 / WDM / bypass / 无源 / 板级 / 软件 / 服务）；留 C'),
    (r'发不过去', '曾退信但域名仍解析 → 不满足 G0-2；留 C（下次巡检找新地址）'),
    (r'综合分低', '光通信 / WDM / bypass 厂商名单内冷户（多为同行），未推送、零互动；留 C'),
    (r'群发冷名单', '群发冷名单无回应，企业邮箱域正常 → 不刚性；留 C 储备'),
    (r'陈旧线索', '陈旧线索无互动，企业邮箱域正常 → 不刚性；留 C 储备'),
    (r'用户备注不再跟进', '表记不再跟进 / Spam（我方备注，非客户拒绝）→ 留 C'),
]


def compose(e, research):
    text = ' / '.join((e.get('interests') or []) + (e.get('remarks') or []))
    if research:
        text += ' / ' + (research.get('summary') or '') + ' / ' + (research.get('type') or '')
    text = re.sub(r'\s+', ' ', text)
    interest = re.sub(r'\s+', ' ', '；'.join(dict.fromkeys(i.strip() for i in (e.get('interests') or []) if i.strip())))[:50]
    if not interest:
        interest = re.sub(r'\s+', ' ', ' / '.join(e.get('remarks') or []))[:50]
    sub = e.get('c_sub') or ''
    why = next((w for k, w in SUB_WHY if re.search(k, sub)), '无刚性 pass 证据；留 C')
    fu = e.get('fu_count') or 0
    bits = [f"{e.get('country') or '未填'}", f'表分 {sub[:18]}' if sub else '']
    if interest:
        bits.append(f'兴趣：{interest}')
    if fu:
        bits.append(f'跟进 {fu} 次无回复' if not (e.get('reply_sub') or 0) else f'跟进 {fu} 次')
    if research:
        t = re.sub(r'\s+', ' ', research.get('type') or research.get('summary') or '')[:60]
        if t:
            bits.append(f'研：{t}')
    if (e.get('flags') or {}).get('bounce'):
        bits.append('邮件曾退信')
    tags = []
    if DJ_RE.search(text):
        tags.append('dayjob_fit')
    if OEM_RE.search(text):
        tags.append('oem_target')
    return '；'.join(b for b in bits if b) + ' → ' + why, tags


def main():
    assert len(CODES) == 165 and len(set(CODES)) == 165
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
    L = [f'# C 池 · 闸 1 · 第 05 批（{DATE}）—— 桶 ⑤「企业邮箱 · 四主区+波兰」前 {len(V)} 户', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 桶 ⑤ 共 660 户（企业邮箱 + 北美 / 欧洲 / 土耳其 / 波兰），115 户有调研 JSON；本批按编号序取前 165 户（SC-008 … SC-1491）。'
         '永久 pass 只给「纯无关行业 + 零互动」（金属建筑、MIDI 软件、租约网站、比价平台、招标门户、SaaS / 支付 / 编排软件、个人无购买 RFQ）；'
         '付过钱的个人零售买家一律留 C。候选 = 对位 ✔ + 主区 / 欧洲 + 硬信号（已在卖 ONV / Utepo / 宇航 / credfiber / 洪瑞 / Planet 等中国同类品牌，或分销商主体）。'
         'SC-1041…SC-1136 一段是光通信 / WDM / bypass 厂商名单，几乎全为同行 → 留 C + dayjob_fit。Q-33 渠道冲突 4 户（Charter Controls / Innon / Electric Bray / napad.pl）留 C 不碰。', '',
         '> **Simon 可按编号否决**：pass 的 14 户若有任何一户想留，回一句编号即可恢复为留 C。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批05_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
