#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 04 批（2026-10-29）—— 「加过 WhatsApp」桶 392 户（尚未判定、flags.wa_added=1）。

这桶的特点：几乎全是展会 / 阿里 / 自建站来的个人号或小公司，只有表内一两行备注，**没有调研 JSON**（仅 2 户有）。
判定口径（方案 §3）：
  · 有 WhatsApp 路径 = 活着、能联系 → 不满足任何刚性 pass 条件 → **默认 keep_C**（理由按表内信息自动组句，逐户可查）。
  · 候选只给「有进口 / 成交 / SKD-OEM / 主区数量询盘」硬信号的 5 户（见 OVERRIDE）。
  · 标签：dayjob_fit（兴趣为光端机 / VC / HDMI / SDI / DWDM / SFP / 模块 / MC 等）、oem_target（自己的 logo / 刷丝印 / SKD）。
  · 「似乎拉黑」「Spam」「不跟了」按 U117 不刚性 → keep_C 并在理由里注明。

用法：python3 sieve_batches/g1_004.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批04_2026-10-29.md）
"""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G1-04'
DATE = '2026-10-29'

DJ_RE = re.compile(r'光端机|\bVC\b|HDMI|SDI|DWDM|\bWDM\b|OTN|SFP|模块|收发器|\bMC\b|光猫|OLP|光缆|CWDM|AHD|CVI|TVI|BNC|Bypass|OM4\d|TA\d{3}|光纤|GBIC|DVI|延长器|转光|V1D|V转|路视频|同轴', re.I)
OEM_RE = re.compile(r'自己的logo|自己的牌子|刷|贴牌|SKD|own logo|丝印|自己的型号|自己的标', re.I)

# 候选（硬信号）与少数需要专门说明的户
OVERRIDE = {
    'SC-683': ('candidate', '德国 VOYGAR SYSTEMS GmbH（Josef Klaus）：工业 1 光 4 电 **54 台**数量询盘；WA 发不过去但企业邮箱域正常 → 欧洲主区 + 对位 ✔ + 数量 → 闸 2 查底数', []),
    'SC-2481': ('candidate', '土耳其 Okisan（Gökhan，okisan.com）：已从深圳 HSGQ 进口（1V1D $30），用丰润达商业 PoE，要 catalog / relay converter → 土耳其主区 + 进口经验 + 对位 ✔；Simon 曾判不行 → 闸 2 查底数再定', ['oem_target']),
    'SC-1025': ('candidate', '印度 Pixelcube（Siran，WeChat siran-pixel）：问能否做 SKD、要全系列价目、想来公司看 → 印度次优区 + SKD/OEM 路径（30% 口径）→ 闸 2 查底数', ['oem_target']),
    'SC-2955': ('candidate', '危地马拉 Continental Towers（mip.com.gt）：「下过两次单买 2 光 3 电和收发器」= 复购户（表内 deal 词未被机器识别）；英语不好；Simon 曾判不行 → 闸 2 核成交记录再定', ['dayjob_fit']),
    'SC-2386': ('candidate', '印度 KHUSHI ENTERPRISES：「import from ONV, need price list, LG distributor」= 同行品牌现成进口商 → 印度次优区 + 进口经验 + 对位 ✔ → 闸 2 查底数', []),
    'SC-2768': ('keep_C', '美国 Hanway International：hanwaycorp.com NXDOMAIN、邮件 fail、「WA 似乎也不太行」、Skype 在 → 接近死但不满足刚性（有 WA/Skype 路径）；留 C，下次巡检若 WA 仍不通可 pass', []),
    'SC-3011': ('keep_C', '印度 gmail 个人（想合作 MC / PoE 8–10 口交换机）表记「似乎是拉黑了」→ 不确定，按 U117 不刚性；留 C', ['dayjob_fit']),
    'SC-3072': ('keep_C', '菲律宾 gmail 个人（千兆 2 光 8 电网管 PoE 工业）表记「似乎是拉黑了」→ 不确定；留 C', []),
    'SC-3297': ('keep_C', '埃及 ARCOSTEEL（钢结构公司，问网络延长器 HDMI）表记「似乎是拉黑了」→ 不确定 + 行业外；留 C', ['dayjob_fit']),
    'SC-3283': ('keep_C', '玻利维亚 SIS Tecnologia（光端机，西语）表记 Spam / fail → 不刚性；留 C', ['dayjob_fit']),
    'SC-3100': ('keep_C', '伊朗（表名「不跟了」，常问复杂型号）→ 我方决定 + 制裁口径；留 C', []),
    'SC-2637': ('keep_C', '马来西亚 Orient Telecoms：用 Adva DWDM、Raisecom 工业机，着重问 L2 管理交换机 → 对位但 Simon 判不行、区域次级；留 C；DWDM 本职可参考', ['dayjob_fit']),
    'SC-674': ('keep_C', '沙特 NTI Middle East：16 口 PoE + 2 SFP 10G 工业 ×18 台询盘，24 次跟进 0 回 → 数量真但无回应、区域次级；留 C（若再询直接报）', []),
    'SC-1174': ('keep_C', '莱索托税务局（政府终端，2 光 16 + 10G 上联）→ 守界公共部门；留 C', []),
    'SC-2011': ('keep_C', '新加坡 StarHub（运营商，SDI 光端机）→ 巨头运营商不 pass；留 C', ['dayjob_fit']),
    'SC-2592': ('keep_C', 'Belden Broadband（opterna，DWDM / 无源配件）→ 巨头；留 C', ['dayjob_fit']),
    'SC-2691': ('keep_C', 'Motorola Solutions 埃及（工业 FS）→ 巨头；留 C', []),
    'SC-2299': ('keep_C', '墨西哥 Comcast Group（DWDM 整套，有国内对接人）→ 需求为 DWDM（本职可参考）；WA 一号加不上；留 C', ['dayjob_fit']),
}

BUCKET_WHY = [
    ('守界：乌克兰', '乌克兰：Simon 明示不永久 pass，战时留 C'),
    ('中国大陆', '中国大陆规则（国内单只走私账）；留 C'),
    ('体量过大', '巨头 / 运营商 / 品牌厂商：按 U117 不 pass；留 C'),
    ('品类不符', '需求为光端机 / 视频 / 光模块类（Saga 不供，Simon 本职可参考）；留 C'),
    ('低价值区域', '区域外冷线索，但 WA 路径在 → 不刚性；留 C 储备'),
    ('群发冷名单', '冷名单无回应，WA 路径在 → 不刚性；留 C 储备'),
    ('陈旧线索', '陈旧线索无互动，WA 路径在 → 不刚性；留 C 储备'),
    ('无邮箱', '仅 WA / 电话路径，无邮箱 → 不刚性；留 C（来询被动报价）'),
    ('用户判定不行', 'Simon 曾判不行；WA 路径在、无刚性 pass 证据 → 留 C（不主动碰）'),
    ('综合分低', '综合分低（多为免费邮箱 / 个人），WA 路径在 → 留 C'),
    ('用户备注不再跟进', '表记不再跟进 / Spam（我方备注，非客户拒绝）→ 留 C'),
]


def compose(e):
    text = ' / '.join((e.get('remarks') or []) + (e.get('interests') or []))
    text = re.sub(r'\s+', ' ', text)
    interest = re.sub(r'\s+', ' ', '；'.join(dict.fromkeys(i.strip() for i in (e.get('interests') or []) if i.strip())))[:50]
    if not interest:
        m = re.sub(r'^[\d\s\-+()已加T M网站上的发不过去WA一直没看信息]+', '', text)
        interest = m[:50]
    sub = e.get('c_sub') or ''
    why = next((w for k, w in BUCKET_WHY if sub.startswith(k)), '无刚性 pass 证据；留 C')
    fu = e.get('fu_count') or 0
    bits = [f"{e.get('country') or '未填'}", 'WA 已加']
    if interest:
        bits.append(f'兴趣：{interest}')
    if fu:
        bits.append(f'跟进 {fu} 次无回复' if not (e.get('reply_sub') or 0) else f'跟进 {fu} 次')
    if (e.get('flags') or {}).get('bounce'):
        bits.append('邮件曾退信')
    tags = []
    if DJ_RE.search(text):
        tags.append('dayjob_fit')
    if OEM_RE.search(text):
        tags.append('oem_target')
    return '；'.join(bits) + ' → ' + why, tags


def main():
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    todo = [e for e in ents.values() if e.get('grade') == 'C' and (e.get('flags') or {}).get('wa_added')
            and not ((sv.get(e['code']) or {}).get('gate', 0) >= 1 and (sv.get(e['code']) or {}).get('batch') != BATCH)
            and not ((sv.get(e['code']) or {}).get('gate') == 0)]
    V = {}
    for e in todo:
        code = e['code']
        if code in OVERRIDE:
            V[code] = OVERRIDE[code]
        else:
            reason, tags = compose(e)
            V[code] = ('keep_C', reason, tags)
    for code in OVERRIDE:
        assert code in V, ('override not in todo', code)
    for code, (verdict, reason, tags) in V.items():
        cur = sv.get(code) or {}
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True, 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    tg = Counter(t for v in V.values() for t in v[2])
    L = [f'# C 池 · 闸 1 · 第 04 批（{DATE}）—— 「加过 WhatsApp」桶 {len(V)} 户', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 这桶几乎全是展会 / 阿里 / 自建站来的个人号或小公司，只有一两行备注、没有调研 JSON。有 WhatsApp 路径 = 活着能联系，不满足任何刚性 pass 条件，所以**一户都没 pass**，全部留 C（理由按表内信息逐户组句）；只有 5 户带硬信号（进口经验 / 复购 / SKD / 主区数量询盘）进闸 2。', '']
    for verdict, title in (('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批04_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
