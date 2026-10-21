#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saga Clients · 第 3 步：把 entities.json 渲染成 `Saga Clients/A|B|C/<编号>-<公司>-<国家>.md`（结构同 profile/）+ 索引。

绝不手改 MD：改规则 → 改 build.py / research JSON / 人工定级.csv → 重跑 build.py + render.py。
"""
import csv
import datetime as dt
import glob
import json
import os
import re
import shutil
from collections import Counter, defaultdict

from common import DATA, OUT_DIR, ROOT, slug

TODAY = dt.date.today().isoformat()
PRICE_CSV = os.path.join(ROOT, 'data', '价格主表.csv')

# 兴趣 → Saga 主推（型号, 场景说明）
P1_RULES = [
    (r'48', 'STC-448DGGPM', '48 口 PoE 走量款'),
    (r'24.{0,3}(poe|PoE|POE)|4光24|2光24|24口|24电|24 ?PoE', 'STC-424DGGPM-280W', '24 口 PoE L2+ 走量款'),
    (r'10G|10g|万兆|2\.5G|2\.5g', 'STC-424XGGPM-280W', '24 口 PoE + 4×10G 上联'),
    (r'L3|三层|3层|核心|core|汇聚|数据中心|DC|堆叠|stack', 'STC-448XGGM(L3)', 'L3 48 口 + 4×10G（Hohunet/CENTEC 线）'),
    (r'16.{0,3}(poe|PoE|POE)|16电|16口|2光16|16 ?PoE', 'STI-21616GP', '工业 16 PoE + 2 SFP'),
    (r'工业.{0,6}(PoE|POE|poe)|导轨|DIN|din', 'STI-288DGGPM', '工业 L2+ 8 PoE + 2×2.5G SFP'),
    (r'1光4|4电|5电口|5口|4口|4 ?PoE|4PoE', 'STI-144GP', '工业 4 PoE + 1 SFP 小壳'),
    (r'2光8|1光8|8.{0,3}(poe|PoE|POE)|8电|8口|8 ?PoE|商业PoE|商业POE|商业poe', 'STC-28DGGPM', '8 口 PoE + 2 SFP L2+'),
    (r'工业FS|工业交换机|工业|industrial|Industrial', 'STI-288DGGPM', '工业 L2+ 8 PoE + 2×2.5G SFP'),
    (r'MC|media converter|光纤收发器|收发器', 'STI-110GE', '工业迷你 1 光 1 电（MC 位）'),
    (r'SFP|光模块|DAC|AOC|模块', None, 'SFP/DAC：Saga 三份价格表无光模块 → 按需询 SmartByte/HRUI'),
    (r'VC|光端机|AHD|HDMI|视频|video', None, 'VC/光端机：Saga 不做（可只推交换机）'),
    (r'DWDM|OTDR|相干|QSFP|200G|400G', None, 'DWDM/OTDR：Saga 不做'),
    (r'PoE|POE|poe|switch|Switch|交换机|FS', 'STC-424DGGPM-280W', '24 口 PoE L2+ 走量款'),
]
BRANDS = ['ONV', 'Utepo', 'Upeto', 'Ewind', '洪瑞', 'HRUI', '中科德能', 'E-link', 'Elink', 'E-Link', 'BDCOM', 'PLANET', 'Planet', 'planet', 'Cisco',
          'Redlion', 'redlion', 'Red Lion', 'Moxa', 'MOXA', 'Antaira', 'Hikvision', 'Dahua', 'TP-Link', 'Mikrotik', 'MikroTik', 'Ubiquiti', 'Netgear',
          'Trendnet', 'Kontron', '迈威', 'Maiwe', '丰润达', '磊通', 'GXCOM', 'Gxcom', 'Witek', 'Diva', 'Longse', 'N-net', 'OTS', 'UniPoE', '优力普',
          'Oring', 'ORing', 'Korenix', 'Westermo', 'Hirschmann', 'Phoenix', 'Advantech', 'Lantech', 'Comnet', 'ComNet', 'Perle', 'Transition',
          'Allied Telesis', 'D-Link', 'Zyxel', 'Tenda', 'Ruijie', 'H3C', 'Huawei', 'Uotek', 'Mlis', 'CTCU', 'Aruba', 'HPE', 'Dell', 'Juniper',
          'Extreme', 'Ubiquiti', 'Cambium', 'G-net', 'Gnet', 'Hioso', 'Fiberhome', 'ZTE', 'Raisecom', 'Televes', 'Dptek', 'DPTEK', 'Smartbyte',
          'SmartByte', 'Realtek', 'Marvell', '海思', 'Hisilicon', '华为', '海康', '大华', 'Axis', 'Bosch', 'Hanwha', 'Uniview', 'UNV', 'Milesight',
          'Teltonika', 'Robustel', 'InHand', 'Siemens', 'Weidmuller', 'Weidmüller', 'Belden', 'EtherWAN', 'Black Box', 'StarTech', 'TRENDnet',
          'Zebra', 'Supermicro', 'FS.com', 'FS', 'Ubiquiti', '武汉迈威', 'Kyland', '东土', 'Ruggedcom', 'Scalance']
TYPE_RULES = [
    (r'自己的logo|自己的品牌|自己的标|自己的牌子|自己的型号|自有品牌|OEM|ODM|贴牌|own brand|private label|刷了自己', '品牌商/贴牌需求（OEM/ODM）'),
    (r'分销|distributor|Distributor|销售平台|有人卖他们|有人在卖|经销|reseller|wholesale|批发|trader|trading|贸易|Trading', '分销商/经销商'),
    (r'集成|integrator|工程|项目|project|Project|solution|Solution|engineering|Engineering|安装|installer|方案', '系统集成/工程商'),
    (r'CCTV|安防|security|Security|监控|camera|摄像头|guvenlik|güvenlik|seguridad|segurança|sicurezza', '安防集成/经销'),
    (r'电信|telecom|Telecom|ISP|运营商|wisp|WISP|network operator', '电信/ISP/网络运营'),
    (r'自动化|automation|Automation|控制|PLC|IoT|物联网|工业控制', '工业自动化/IoT 方案商'),
    (r'电商|shop|Shop|store|Store|e-?commerce|online', '电商/网店'),
    (r'制造|manufactur|Manufactur|厂商|工厂|factory', '制造商（可能是同行或 OEM 客户）'),
]


def load_prices():
    by = {}
    if not os.path.exists(PRICE_CSV):
        return by
    for r in csv.DictReader(open(PRICE_CSV, encoding='utf-8-sig')):
        k = r['Saga对应型号'].strip()
        if k and k not in by:
            by[k] = r
    return by


PRICES = load_prices()


def price_line(model, tier):
    r = PRICES.get(model)
    if not r:
        return '价格待核（价格主表无此型号）'
    col = {20: 'USD@+20%', 25: 'USD@+25%', 30: 'USD@+30%'}[tier]
    return (f"${r[col]} USD EXW（{tier}% 档，SmartByte {r['SmartByte型号']} {r['CNY未税']} CNY × {1 + tier / 100:.2f} ÷ {r['汇率']}，"
            f"汇率快照 {r['汇率日期']}，15 天有效，报价前核价）")


def infer_type(ent):
    txt = ' '.join(ent['interests'] + ent['remarks'] + ent['names'] + ent['froms'] + ent.get('positions', []))
    if ent.get('research', {}).get('type'):
        return ent['research']['type']
    for pat, t in TYPE_RULES:
        if re.search(pat, txt):
            return t
    return '经销/集成（类型待核）'


def infer_tier(ent, typ):
    if '品牌' in typ or 'OEM' in typ:
        return 30
    if '分销' in typ or '经销' in typ or '电商' in typ:
        return 20
    return 25


def infer_p1(ent):
    txt = ' '.join(ent['interests'] + ent['remarks'])
    for pat, model, why in P1_RULES:
        if re.search(pat, txt):
            return model, why
    return 'STC-424DGGPM-280W', '无明确兴趣记录：按 Saga 走量款起手'


def brands_seen(ent):
    txt = ' '.join(ent['interests'] + ent['remarks'])
    out = []
    for b in BRANDS:
        if b in txt and b not in out:
            out.append(b)
    # 去同义
    norm = []
    seen = set()
    for b in out:
        k = b.lower().replace('-', '').replace(' ', '')
        k = {'upeto': 'utepo', 'elink': 'elink', 'redlion': 'redlion', 'hrui': '洪瑞', 'dptek': 'dptek', 'smartbyte': 'smartbyte', 'mikrotik': 'mikrotik',
             'oring': 'oring', 'comnet': 'comnet', 'weidmüller': 'weidmuller', 'trendnet': 'trendnet', 'gxcom': 'gxcom', 'gnet': 'gnet', 'planet': 'planet'}.get(k, k)
        if k not in seen:
            seen.add(k)
            norm.append(b)
    return norm


def stars(grade):
    return {'A': '★★★', 'B': '★★', 'C': '—'}[grade]


def md_escape(s):
    return (s or '').replace('|', '\\|').replace('\n', '<br>')


def fmt_sources(ent):
    lines = ['| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |', '|---|---|---|---|---|---|---|---|---|---|']
    for s in ent['sources']:
        lines.append('| ' + ' | '.join(md_escape(x) for x in [
            f"{s['file'].replace('Clients/', '')}#{s['sheet']}:{s['row']}", s['no'], s['company'], s['country'] or s.get('category', ''), s['person'],
            s['from'], s['interest'], ' '.join(x for x in [s['contact'], s['mobile'], s['website']] if x), ' '.join(x for x in [s['remark'], s['extra'], s['position']] if x),
            str(s['followups']) + ' 条' if s['followups'] else '—']) + ' |')
    return '\n'.join(lines)


def fmt_followups(ent, limit=400):
    fus = ent['followups']
    if not fus:
        return '（无跟进表记录）'
    lines = [f'合并自 {len({(f["file"], f["no"]) for f in fus})} 张跟进表，共 {len(fus)} 条（原值照录，日期已按年份递推补全）：', '',
             '| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |', '|---|---|---|---|---|---|---|']
    for f in fus[:limit]:
        lines.append('| ' + ' | '.join(md_escape(x) for x in [f['date_iso'] or '?', f['date'], f['content'], f['reply'], f['platform'], f['note'],
                                                            f"{os.path.basename(f['file'])}#{f['no']}"]) + ' |')
    if len(fus) > limit:
        lines.append(f'| … | | 其余 {len(fus) - limit} 条见 data/saga_clients/entities.json | | | | |')
    return '\n'.join(lines)


def fmt_contacts(ent):
    out = []
    bounce = ent['flags'].get('bounce')
    for e in ent['emails']:
        corp = e.split('@')[1] in {d for d in ent['domains']} or e in ent['corp_emails']
        st = '企业邮箱' if e in ent['corp_emails'] else '免费邮箱'
        if bounce:
            st += '；用户备注含「发不过去」——发送前核对是哪一个地址'
        out.append(f'- 邮箱：`{e}`〔{st}；来源：用户表原值〕')
    for ph in ent['phones']:
        wa = 'WhatsApp 已加' if ent['flags'].get('wa_added') or ent['wa_in_fu'] else ('WhatsApp 加不上' if ent['flags'].get('wa_failed') else '电话/WhatsApp 状态未记')
        out.append(f'- 电话：`+{ph}`〔{wa}；原值见来源表〕')
    for p in ent['persons']:
        out.append(f'- 联系人（原值）：{p}')
    for p in ent.get('positions', []):
        out.append(f'- 职位（原值）：{p}')
    for d in ent['domains']:
        out.append(f'- 网站/域名：{d}')
    for u in ent['platform_links'][:5]:
        out.append(f'- 平台链接：{u}')
    if not out:
        out.append('- （无任何联系方式：仅公司名/备注）')
    out.append('- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。')
    return '\n'.join(out)


def fmt_research(ent):
    rs = ent.get('research')
    if not rs:
        return ('- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），'
                '写入 `data/saga_clients/research/' + ent['code'] + '.json` 后由渲染器并入本节。')
    lines = [f"- **状态：已调研（{rs.get('researched_at', '')}）**　网站状态：{rs.get('website_status', '未记')}",
             f"- **是谁**：{rs.get('summary', '')}"]
    if rs.get('type'):
        lines.append(f"- **类型**：{rs['type']}")
    if rs.get('size'):
        lines.append(f"- **规模**：{rs['size']}")
    if rs.get('brands_seen'):
        lines.append(f"- **在卖/在用品牌**：{', '.join(rs['brands_seen'])}")
    for ev in rs.get('evidence', []):
        lines.append(f"- **【{ev.get('kind', '网页')}】{ev.get('claim', '')}**")
        if ev.get('quote'):
            lines.append(f"  > {ev['quote']}")
        lines.append(f"  > 来源：{ev.get('url', '')}（抓取 {ev.get('date', '')}）")
    for kp in rs.get('kp', []):
        lines.append(f"- **KP**：{kp.get('name', '')}（{kp.get('role', '')}）{kp.get('email', '')} {kp.get('phone', '')}〔{kp.get('source', '')}〕")
    if rs.get('grade_override'):
        lines.append(f"- **调研后定级**：{rs['grade_override']}（原自动 {ent['grade_auto']}）——{rs.get('override_reason', '')}")
    if rs.get('notes'):
        lines.append(f"- 备注：{rs['notes']}")
    return '\n'.join(lines)


def followup_plan(ent, grade, p1, tier):
    if grade == 'C':
        return ('> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。\n'
                f'> 不跟进理由：{ent["c_sub"] or "综合分低"}。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `{ent["code"]},B,理由` 后重跑即可。')
    model = p1 or 'STC-424DGGPM-280W'
    deal = ent['flags'].get('deal') or ent['deal_in_fu']
    if deal:
        step1 = f'**第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（{model}）；只问一个问题：当前在采购的主力型号与月量。'
    elif ent['reply_sub']:
        step1 = f'**第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + {model} 一条规格链接；只问一个问题。'
    else:
        step1 = f'**第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 {model} 一条规格链接；只问一个问题。'
    if grade == 'A':
        cadence = '节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。'
    else:
        cadence = '节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。'
    return '\n'.join([
        f'> 每次只推进一个台阶、只问一个问题；全程只推 P1（{model}），备选型不进首触。',
        '',
        f'- {step1}',
        f'- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。',
        f'- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；{tier}% 档报价。',
        f'- {cadence}',
        '- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。',
    ])


def render_one(ent):
    g = ent['grade']
    code = ent['code']
    typ = infer_type(ent)
    tier = infer_tier(ent, typ)
    p1, p1_why = infer_p1(ent)
    brands = brands_seen(ent)
    deal = bool(ent['flags'].get('deal') or ent['deal_in_fu'])
    rel = []
    if deal:
        rel.append('成交/下单过')
    if ent['reply_sub']:
        rel.append(f'实质回复 {ent["reply_sub"]} 次')
    if ent['reply_neg']:
        rel.append(f'回复暂无需求 {ent["reply_neg"]} 次')
    if ent['flags'].get('wa_added') or ent['wa_in_fu']:
        rel.append('WhatsApp 已加')
    if ent['fu_count']:
        rel.append(f'推送 {ent["fu_count"]} 次（{ent["fu_first"] or "?"} → {ent["fu_last"] or "?"}）')
    if not rel:
        rel.append('名单内·无互动记录')
    tags_short = '、'.join(ent['tags'])
    ai_txt = ''
    for a in ent['ai_evals']:
        parts = []
        if a.get('claude') and a['claude'].get('grade'):
            parts.append(f"Claude {a['claude']['pct']}% {a['claude']['grade']}")
        if a.get('ai') and a['ai'].get('grade'):
            parts.append(f"AI {a['ai']['pct']}% {a['ai']['grade']}")
        if parts:
            ai_txt = '；'.join(parts)
            break
    website = ent['domains'][0] if ent['domains'] else ''
    p1_price = price_line(p1, tier) if p1 else '—'
    last_reply = ''
    for f in reversed(ent['followups']):
        if f['reply'] and f['reply_kind'] in ('substantive', 'negative', 'other'):
            last_reply = f"{f['date_iso'] or f['date']}：{f['reply']}"
            break
    first_q = {
        'A': 'Which switch model are you buying most often right now, and roughly how many units a month?',
        'B': 'Are PoE / industrial switches something you still source today, or has that line been dropped?',
        'C': '—（C 级不发首触）',
    }[g]
    unknown = []
    if not ent['persons']:
        unknown.append('采购/产品负责人姓名（表内只有公司级邮箱）')
    if not website:
        unknown.append('公司网站（表内无域名，无法核实是否仍在运营）')
    if not ent['interests']:
        unknown.append('具体需求型号（表内兴趣列为空）')
    if not ent.get('research'):
        unknown.append('网页调研未做（公司规模/业务/在卖品牌待核）')
    if not unknown:
        unknown.append('年走量与现供应商')
    yaml_tags = json.dumps(ent['tags'], ensure_ascii=False)
    lines = []
    lines.append(f'# {ent["name"]}')
    lines.append('')
    lines.append(f'> **评级 {g}**　|　{ent["country"]}　|　档案编号 `{code}`　|　优先级 {stars(g)}　|　状态：{ent["status"]}')
    lines.append('>')
    lines.append(f'> **类型**：{typ}（推断）　|　**历史关系**：{"；".join(rel)}　|　**所在清单**：{tags_short}　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）')
    lines.append('')
    lines.append('```yaml structured_profile')
    lines.append(f'code: {code}')
    lines.append(f'rating: {g}')
    lines.append(f'rating_auto: {ent["grade_auto"]}')
    if ent.get('manual'):
        lines.append(f'rating_manual: {ent["manual"].get("等级", "")}  # {ent["manual"].get("理由", "")}')
    lines.append(f'score: {ent["score"]}')
    lines.append(f'country: {ent["country"]}')
    lines.append(f'region: {ent["region"]}')
    lines.append(f'website: {website or "none"}')
    lines.append(f'type: {typ}')
    lines.append(f'tier_tags: {yaml_tags}')
    lines.append(f'deal: {"yes" if deal else "no"}')
    lines.append(f'replies: {ent["reply_sub"]}')
    lines.append(f'followups: {ent["fu_count"]}')
    lines.append(f'first_contact: {ent["fu_first"] or "unknown"}')
    lines.append(f'last_contact: {ent["fu_last"] or "unknown"}')
    lines.append(f'p1: {p1 or "none"}')
    lines.append(f'price_tier: {tier}%')
    lines.append(f'research: {"done" if ent.get("research") else "pending"}')
    lines.append(f'sources: {len(ent["sources"])}')
    lines.append(f'updated: {TODAY}')
    lines.append('```')
    lines.append('')
    lines.append('## SALES BRIEF（压缩模型）')
    lines.append('')
    who = f'{ent["country"]}的{typ}'
    if ent['interests']:
        who += '；兴趣/在卖：' + '；'.join(ent['interests'])[:160].replace('\n', ' ')
    if brands:
        who += f'；提到的品牌：{", ".join(brands)}'
    lines.append(f'- **是谁**：{who}')
    lines.append(f'- **为什么是 {g} 级**：' + '；'.join(ent['reasons']) + (f'；C 级细分：{ent["c_sub"]}' if g == 'C' and ent['c_sub'] else ''))
    hist = '；'.join(rel)
    if last_reply:
        hist += f'；最近一次客户回复：{last_reply}'
    lines.append(f'- **历史互动**：{hist}')
    if g != 'C':
        lines.append(f'- **P1（下一步唯一主推）**：{p1 or "—"} — {p1_why}；{p1_price}')
        lines.append(f'- **第一问（只问一个）**：{first_q}')
    else:
        lines.append(f'- **P1**：不推（C 级）；若对方主动来询，起手 {p1 or "STC-424DGGPM-280W"}（{p1_why}）')
    lines.append(f'- **最大未知**：{"；".join(unknown)}')
    nxt = {'A': '按下文「跟进建议」第 1 次执行；回复后更新 research JSON 并重渲染', 'B': '放入慢跟队列（4–6 周一次）；有回复即重评', 'C': '不跟进；仅归档防重复开发'}[g]
    lines.append(f'- **下一步**：{nxt}')
    lines.append('')
    lines.append('## 基本事实（事实/推断/假设分层）')
    lines.append('')
    lines.append('| 项 | 内容 | 层级 |')
    lines.append('|---|---|---|')
    lines.append(f'| 名称 | {md_escape(ent["name"])}{"（取自域名，公司全名待核）" if ent["name_src"] == "domain" else ""} | {"事实（用户表）" if ent["name_src"] == "company" else "推断"} |')
    if len(ent['names']) > 1:
        lines.append(f'| 其他名称写法 | {md_escape(" / ".join(ent["names"][1:]))} | 事实（用户表） |')
    lines.append(f'| 国家 | {ent["country"]}{"（另见：" + "、".join(ent["other_countries"]) + "）" if ent["other_countries"] else ""} | 事实（用户表）|')
    lines.append(f'| 网站/域名 | {md_escape(" / ".join(ent["domains"]) or "—")} | 事实（用户表 URL/邮箱域名） |')
    lines.append(f'| 类型 | {typ} | 推断（据兴趣/备注关键词） |')
    lines.append(f'| 联系人 | {md_escape(" / ".join(ent["persons"]) or "—")} | 事实（用户表） |')
    lines.append(f'| 来源（From） | {md_escape(" / ".join(ent["froms"]) or "—")} | 事实（用户表） |')
    lines.append(f'| 兴趣（Interested in） | {md_escape(" / ".join(ent["interests"]) or "—")} | 事实（用户表） |')
    lines.append(f'| 用户备注（Remark） | {md_escape(" / ".join(ent["remarks"]) or "—")} | 事实（用户表） |')
    if ent['categories']:
        lines.append(f'| 用户分档（Category） | {md_escape(" / ".join(sorted(set(ent["categories"]))))} | 事实（用户表） |')
    if ai_txt:
        lines.append(f'| 用户 AI 评估 | {ai_txt} | 事实（用户表 AI评估结果/CALUDE评估结果列） |')
    lines.append(f'| 所在清单 | {md_escape(tags_short)} | 事实（文件路径） |')
    lines.append(f'| 在卖/在用品牌（备注所见） | {", ".join(brands) or "—"} | 事实（用户备注）/ 推断 |')
    lines.append('')
    if ent['ai_evals']:
        lines.append('### 用户 AI / Claude 评估原文')
        lines.append('')
        for a in ent['ai_evals']:
            for k in ('claude', 'ai'):
                if a.get(k) and a[k].get('text'):
                    lines.append(f'- **{"Claude" if k == "claude" else "AI"}**（{os.path.basename(a["file"])}）：')
                    for ln in a[k]['text'].split('\n'):
                        lines.append(f'  > {ln}')
        lines.append('')
    lines.append('## 客户调研（网页核实 · 引文 + URL + 日期）')
    lines.append('')
    lines.append(fmt_research(ent))
    lines.append('')
    lines.append('## 在卖/在用品牌 → Saga 对位')
    lines.append('')
    if brands:
        lines.append('| 备注所见品牌 | 含义 | Saga 切入 |')
        lines.append('|---|---|---|')
        for b in brands:
            bl = b.lower()
            if bl in ('洪瑞', 'hrui'):
                meaning, cut = '洪瑞 = HRUI（Saga 的 Realtek 辅线供应商）', '同源货：Saga STC Realtek 线（见 data/hrui_STC对照表.csv）可直接对型号报价'
            elif bl in ('smartbyte', 'dptek'):
                meaning, cut = 'Saga 主供应商 / 深圳同行品牌', '对方已接受深圳 Marvell 方案：直接谈贴牌与价格'
            elif bl in ('onv', 'utepo', 'upeto', 'ewind', '中科德能', 'e-link', 'elink', '丰润达', '磊通', 'gxcom', 'witek', 'g-net', 'gnet', 'uotek', 'n-net', 'ots', 'unipoe', '优力普', '迈威', 'maiwe', '武汉迈威', 'kyland', '东土', 'ctcu', 'hioso', 'raisecom', 'bdcom', 'mlis', 'diva', 'longse'):
                meaning, cut = '深圳/国内白牌或品牌供应商', '对方已在买中国货：以 Marvell 芯片 + L2+ 功能 + 交期为差异点做第二货源'
            elif bl in ('planet', 'moxa', 'oring', 'korenix', 'lantech', 'etherwan', 'advantech', 'antaira', 'comnet', 'perle', 'transition', 'westermo', 'hirschmann', 'phoenix', 'redlion', 'red lion', 'siemens', 'weidmuller', 'weidmüller', 'belden', 'ruggedcom', 'scalance', 'black box', 'startech', 'trendnet', 'allied telesis', 'd-link', 'zyxel', 'netgear', 'tp-link', 'tenda', 'mikrotik', 'ubiquiti', 'cambium', 'teltonika', 'robustel', 'inhand', 'milesight', 'fs.com', 'fs', 'televes'):
                meaning, cut = '台系/欧美/品牌工业或商用网络品牌', '按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌）'
            elif bl in ('cisco', 'aruba', 'hpe', 'dell', 'juniper', 'extreme', 'huawei', 'h3c', 'ruijie', 'zte', 'fiberhome', '华为'):
                meaning, cut = '企业级大牌（Cisco/HPE/华为类）', 'Saga 只能接接入层/工业层，不对标核心；问清是否有白牌接入层需求'
            elif bl in ('hikvision', 'dahua', 'uniview', 'unv', 'axis', 'bosch', 'hanwha', '海康', '大华'):
                meaning, cut = '安防摄像头品牌', '对方是安防集成/经销：主推 PoE 交换机配套（看门狗、长距、bt 口）'
            else:
                meaning, cut = '品牌/芯片提及', '按场景对位'
            lines.append(f'| {b} | {meaning} | {cut} |')
    else:
        lines.append('（备注未提及具体品牌）')
    lines.append('')
    lines.append('## 历史跟进记录（原表照录）')
    lines.append('')
    lines.append(fmt_followups(ent))
    lines.append('')
    lines.append('## 联系方式（已有 · 原值照录）')
    lines.append('')
    lines.append(fmt_contacts(ent))
    lines.append('')
    lines.append('## 来源与归并（不漏 · 原始行定位）')
    lines.append('')
    if len(ent['sources']) > 1:
        lines.append(f'本客户由 **{len(ent["sources"])} 行**原始记录归并而成；归并键：{", ".join("`" + k + "`" for k in ent.get("merge_keys", [])) or "（同一文件内同 No.）"}。')
    else:
        lines.append('本客户只有 1 行原始记录。')
    if ent.get('code_aliases'):
        lines.append(f'曾用编号：{", ".join(ent["code_aliases"])}')
    lines.append('')
    lines.append(fmt_sources(ent))
    lines.append('')
    if g != 'C':
        lines.append('## 产品决策（Saga · 单一决策口径）')
        lines.append('')
        lines.append('| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |')
        lines.append('|---|---|---|---|---|')
        lines.append(f'| **P1** | {p1 or "—"} | {p1_why} | {p1_price} | 据用户表兴趣/备注推断；档位 {tier}%（{typ}） |')
        alts = [('STC-28DGGPM', '8 口 PoE + 2 SFP L2+ 小接入'), ('STI-288DGGPM', '工业 L2+ 8 PoE + 2×2.5G SFP'), ('STC-424XGGPM-280W', '24 PoE + 4×10G 上联')]
        n = 2
        for m, sc in alts:
            if m != p1:
                lines.append(f'| 备选{n} | {m} | {sc} | {price_line(m, tier)} | P1 之后的台阶，不进首触 |')
                n += 1
        lines.append('')
        lines.append('- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。')
        lines.append('')
    lines.append('## 跟进建议')
    lines.append('')
    lines.append(followup_plan(ent, g, p1, tier))
    lines.append('')
    lines.append('## 触达与风险红线')
    lines.append('')
    lines.append('1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。')
    lines.append('2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。')
    lines.append('3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。')
    lines.append('4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。')
    lines.append('5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。')
    lines.append('')
    lines.append('## 变更日志')
    lines.append('')
    lines.append(f'- {TODAY}：建档（PR-02-19 · 从 `Clients/` {len(ent["sources"])} 行原始记录归并；自动评级 {ent["grade_auto"]}，分数 {ent["score"]}）' + (f'；人工/调研定级 → {g}' if g != ent['grade_auto'] else ''))
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append(f'*建档日期：{TODAY}　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*')
    return '\n'.join(lines) + '\n'


def main():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    for g in 'ABC':
        d = os.path.join(OUT_DIR, g)
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)
    index = defaultdict(list)
    for e in ents:
        fn = f"{e['code']}-{slug(e['name'])}-{slug(e['country'], 12)}.md"
        path = os.path.join(OUT_DIR, e['grade'], fn)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(render_one(e))
        index[e['grade']].append((e, fn))
    write_readme(ents, index)
    print({g: len(v) for g, v in index.items()})


def write_readme(ents, index):
    n = len(ents)
    byg = Counter(e['grade'] for e in ents)
    byreg = Counter((e['grade'], e['region']) for e in ents)
    regions = ['北美', '欧洲', '土耳其', '中东', '亚太', '俄语区', '南亚', '拉美', '非洲', '乌克兰', '中国大陆', '未知']
    L = []
    L.append('# Saga Clients — Saga 历史客户全量档案（A / B / C）')
    L.append('')
    L.append(f'> 生成：{TODAY}　|　来源：`Clients/`（Simon 上传到 main 的 137 个文件：6,246 行线索 + 20,819 条跟进记录）　|　归并后 **{n} 个客户**：A {byg["A"]} / B {byg["B"]} / C {byg["C"]}')
    L.append('>')
    L.append('> 流水线：`scripts/saga_clients/extract.py`（逐表逐行抽取）→ `build.py`（归并重复 + 规则分级 + 人工定级/调研覆盖）→ `render.py`（本目录）。**MD 不手改**：改 `data/saga_clients/人工定级.csv` 或 `research/<编号>.json` 后重跑。')
    L.append('')
    L.append('## 等级定义（用户口径 → 执行口径）')
    L.append('')
    L.append('| 等级 | 用户定义 | 执行口径（build.py） |')
    L.append('|---|---|---|')
    L.append('| **A** | 值得长期跟进 / OK 的 | 分数 ≥ 60 **且**有互动证据（成交 / 实质回复 / 询盘 / 展会面谈 / S 重点名单）；台系品牌商、巨头、守界区域、品类不符封顶 B 或 C |')
    L.append('| **B** | 一般的，慢慢跟进 | 分数 25–59；或有实质回复但分数低（托底 B）；或 A 候选但无互动证据（封顶 B） |')
    L.append('| **C** | 垃圾 / 基本或压根不值得跟进 | 分数 < 25；或硬规则：用户已归「不行及不太相关」、无联系方式、中国大陆、乌克兰（守界）、巨头/品牌厂商/运营商、备注「不再跟进/Spam」 |')
    L.append('')
    L.append('分数 = 用户信号（成单 +50、实质回复 +22/+30、S 名单 +25、已回复名单 +18、WhatsApp +15、询盘 +12、ISAF 面谈 +12、1类 +15、AI/Claude A +15…）'
             '− 负面（不行 −60、不再跟进 −40、发不过去 −25、巨头 −45、聋名单 −10/−16/−22…）+ 契合（自有品牌 +12、交换机主线 +8、品类不符 −15）'
             '+ 通道（企业邮箱 +10、有网站 +5、无联系方式 −40）+ 区域（北美/欧洲/土耳其 +8 … 南亚/非洲 −6、中国大陆 −40、乌克兰 −20）+ 时效。每个档案的「为什么是 X 级」逐项列出。')
    L.append('')
    L.append('## 分布')
    L.append('')
    L.append('| 区域 | A | B | C | 合计 |')
    L.append('|---|---|---|---|---|')
    for r in regions:
        a, b, c = byreg[('A', r)], byreg[('B', r)], byreg[('C', r)]
        if a + b + c:
            L.append(f'| {r} | {a} | {b} | {c} | {a + b + c} |')
    L.append(f'| **合计** | {byg["A"]} | {byg["B"]} | {byg["C"]} | {n} |')
    L.append('')
    st = Counter(e['status'].split('·')[0].split(' ')[0] for e in ents)
    L.append('状态分布：' + '；'.join(f'{k} {v}' for k, v in st.most_common()))
    L.append('')
    csub = Counter(e['c_sub'] for e in ents if e['grade'] == 'C')
    L.append('C 级细分：' + '；'.join(f'{k} {v}' for k, v in csub.most_common()))
    L.append('')
    L.append('## 配套文件')
    L.append('')
    L.append('- `data/saga_clients/客户主表.csv` — 一行一个客户（编号 / 等级 / 分数 / 联系方式 / 来源定位 / 评级依据）')
    L.append('- `data/saga_clients/重复客户归并记录.md` — 多来源客户与归并键、正负名单冲突')
    L.append('- `data/saga_clients/rows_raw.jsonl` / `followups.jsonl` / `extract_report.json` — 原始逐行抽取与逐文件行数（不漏复核）')
    L.append('- `data/saga_clients/research/` — 调研 JSON（引文 + URL + 日期；含 grade_override）')
    L.append('- `data/saga_clients/人工定级.csv` — 人工覆盖（列：键或编号, 等级, 理由）')
    L.append('- `Clients/` — 原件（只读，不改名不改内容）')
    L.append('')
    L.append('## 索引')
    L.append('')
    for g in 'ABC':
        L.append(f'### {g} 级（{len(index[g])}）— `Saga Clients/{g}/`')
        L.append('')
        if g == 'A':
            L.append('| 编号 | 公司 | 国家 | 类型 | 状态 | 分数 | 调研 | 档案 |')
            L.append('|---|---|---|---|---|---|---|---|')
            for e, fn in sorted(index[g], key=lambda x: x[0]['code']):
                L.append(f"| {e['code']} | {md_escape(e['name'])} | {e['country']} | {infer_type(e)} | {e['status']} | {e['score']} | {'已' if e.get('research') else '待'} | [{fn}]({g}/{fn.replace(' ', '%20')}) |")
        else:
            L.append(f'全部 {len(index[g])} 个档案见 `Saga Clients/{g}/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。')
            with open(os.path.join(OUT_DIR, g, '_索引.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {g} 级索引（{len(index[g])}）\n\n| 编号 | 公司 | 国家 | 状态 | 分数 | C级细分 | 档案 |\n|---|---|---|---|---|---|---|\n')
                for e, fn in sorted(index[g], key=lambda x: x[0]['code']):
                    f.write(f"| {e['code']} | {md_escape(e['name'])} | {e['country']} | {e['status']} | {e['score']} | {e['c_sub']} | [{fn}]({fn.replace(' ', '%20')}) |\n")
        L.append('')
    with open(os.path.join(OUT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
