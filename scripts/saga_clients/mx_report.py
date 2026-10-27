#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T29-U64 · 第 82 批 · 邮箱域体检总览：mx_check_<date>.json → docs/邮箱域体检_<date>.md

内容：① 总体分布（托管商 / 状态）② 死域名 / 无 MX 的 A/B 户（地址作废 + 降级候选）③ 企业网关户（冷邮件最难到）
④ 主要国家的托管商结构（决定群发策略）⑤ 按托管类型的发信守则。只读 JSON，不改档案。
"""
import datetime as dt
import glob
import json
import os
from collections import Counter, defaultdict

from common import DATA, ROOT

fs = sorted(glob.glob(os.path.join(DATA, 'mx_check_*.json')))
MX = json.load(open(fs[-1], encoding='utf-8'))
DATE = MX['_meta']['checked']
DOM = MX['domains']
HH = MX['households']
ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
ents = ents if isinstance(ents, list) else list(ents.values())
E = {e['code']: e for e in ents}
DIMS = json.load(open(os.path.join(DATA, 'dims.json'), encoding='utf-8')) if os.path.exists(os.path.join(DATA, 'dims.json')) else {}

GATEWAYS = ('Proofpoint', 'Mimecast', 'Barracuda', 'MessageLabs', 'Trend Micro', 'Sophos', 'Cisco', 'FortiMail', 'Hornetsecurity')


def family(cls, status):
    if status in ('nxdomain', 'dead', 'null_mx'):
        return '域名已死'
    if status == 'no_mx':
        return '无 MX'
    if status.startswith('error'):
        return '查询超时'
    if cls == 'Microsoft 365':
        return 'Microsoft 365'
    if cls == 'Google Workspace':
        return 'Google Workspace'
    if any(k in cls for k in GATEWAYS):
        return '企业网关'
    if cls in ('Zoho Mail', 'Yandex 360', 'Mail.ru（VK WorkMail）', 'Fastmail', 'Proton Mail', 'iCloud+ 自定义域'):
        return '中小企业云邮箱'
    if cls.startswith('自建'):
        return '自建服务器'
    if cls.startswith('中国邮箱'):
        return '中国邮箱'
    return '主机商邮箱'


def heat(code):
    v = DIMS.get(code) or {}
    h = v.get('heat')
    return h.get('score') if isinstance(h, dict) else (h or 0)


def main():
    fam_dom = Counter()
    fam_hh = Counter()
    hh_fam = {}
    for code, ds in HH.items():
        fams = [family(DOM[d]['cls'], DOM[d]['status']) for d in ds if d in DOM]
        for f in set(fams):
            fam_hh[f] += 1
        # 户的主类型 = 第一个活域名的类型
        live = [f for f in fams if f not in ('域名已死', '无 MX', '查询超时')]
        hh_fam[code] = live[0] if live else (fams[0] if fams else '')
    for d, r in DOM.items():
        fam_dom[family(r['cls'], r['status'])] += 1
    cls_cnt = Counter(r['cls'] for r in DOM.values() if r['cls'])

    L = [f'# 邮箱域体检 {DATE}（第 82 批 · T29-U64，自动生成，勿手改）', '',
         f"生成：{dt.datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')}。来源：`scripts/saga_clients/mx_check.py` 对 A/B 全部 {len(HH)} 户、{len(DOM)} 个域名（含邮箱地址所在域）做 DNS MX / A 查询；"
         '同域名 MX 再反解 PTR 区分「真自建」和「托管在主机商」。**没有做 SMTP 探测**（沙箱不放行，也不该对客户服务器做），所以「域活着」≠「这个地址活着」，退信仍以实际发送为准。',
         '', '## 一、这能干什么', '',
         '- **发信策略按托管商分**：Microsoft 365 户（最大一类）对陌生群发最严、像素被 Safe Links 预取 → 这些户的「打开」数据不可信，只走 1:1；Google Workspace 户像素偏高；企业网关户冷邮件基本到不了，靠回原线程 / LinkedIn。',
         '- **清地址**：域名已不存在 / 无 MX 的地址直接作废，省得再退信；户若没有别的域名或渠道 → 降级候选（见 §三）。',
         '- **看对方 IT 成色**：自建邮件服务器 = 有自己的 IT（技术人读信）；主机商附带邮箱 = 老板自己收（短、直接）。',
         '', '## 二、总体分布', '',
         '| 托管类型（户口径，按第一个活域名） | A/B 户 | 域名数 |', '|---|---|---|']
    for f, n in sorted(fam_dom.items(), key=lambda kv: -kv[1]):
        L.append(f'| {f} | {sum(1 for c in hh_fam if hh_fam[c] == f)} | {n} |')
    L += ['', '细分（域名口径，前 25）：', '']
    L.append('| 托管商 | 域名数 |')
    L.append('|---|---|')
    for c, n in cls_cnt.most_common(25):
        L.append(f'| {c} | {n} |')

    # §三 dead
    L += ['', '## 三、地址作废 / 降级候选（域名已死或无 MX）', '',
          '| 户 | 公司 | 级 | 国家 | 域名 | 状态 | 受影响地址 | 其他活域 | 热度 |', '|---|---|---|---|---|---|---|---|---|']
    rows = []
    for code, ds in HH.items():
        e = E.get(code) or {}
        bad = [(d, DOM[d]['status']) for d in ds if d in DOM and DOM[d]['status'] in ('nxdomain', 'dead', 'no_mx', 'null_mx')]
        if not bad:
            continue
        live = [d for d in ds if d in DOM and DOM[d]['status'] == 'ok']
        for d, st in bad:
            ems = [x for x in (e.get('emails') or []) if x.lower().endswith('@' + d)]
            rows.append((0 if st in ('nxdomain', 'dead') else 1, -heat(code), code, (e.get('name') or '')[:28], e.get('grade', ''), e.get('country', ''), d,
                         {'nxdomain': '域名不存在', 'dead': '无 MX 无 A', 'no_mx': '无 MX（A 兜底）', 'null_mx': 'Null MX'}[st], '、'.join(ems) or '—', '、'.join(live) or '—', heat(code)))
    rows.sort()
    for r in rows:
        L.append('| ' + ' | '.join(str(x) for x in r[2:]) + ' |')
    L += ['', f'共 {len(rows)} 条（{sum(1 for r in rows if r[0] == 0)} 条域名已死，{sum(1 for r in rows if r[0] == 1)} 条无 MX）。'
          '「无 MX」的域理论上还能靠 A 记录收信，但多数主流 MTA 会直接退 → 当作废处理，除非对方来信证明能收。「其他活域」有值的户不降级，只换地址。']

    # §四 gateways
    L += ['', '## 四、企业网关户（冷邮件最难到，像素失效）', '', '| 户 | 公司 | 级 | 国家 | 网关 | 热度 | 下一步 |', '|---|---|---|---|---|---|---|']
    gw = []
    for code, ds in HH.items():
        for d in ds:
            r = DOM.get(d) or {}
            if any(k in r.get('cls', '') for k in GATEWAYS):
                e = E.get(code) or {}
                rs_p = os.path.join(DATA, 'research', f'{code}.json')
                nm = ''
                if os.path.exists(rs_p):
                    nm = str((((json.load(open(rs_p, encoding='utf-8')).get('mail_review') or {}).get('next_move') or {}).get('when', '')))[:16]
                gw.append((-heat(code), code, (e.get('name') or '')[:28], e.get('grade', ''), e.get('country', ''), r['cls'], heat(code), nm))
                break
    gw.sort()
    for g in gw:
        L.append('| ' + ' | '.join(str(x) for x in g[1:]) + ' |')
    L += ['', f'共 {len(gw)} 户。这些户的群发基本白发：Proofpoint / Mimecast / Barracuda 会重写链接、隔离附件，像素一律不触发 → 「未打开」不等于没看。对策：回原线程（如果有）、LinkedIn、或让对方先来一封（展会 / 表单）。']

    # §五 by country
    L += ['', '## 五、主要国家的托管结构（决定该国群发怎么发）', '', '| 国家 | A/B 户 | M365 | Google | 主机商 | 自建 | 网关 | 中小云 | 死 / 无 MX |', '|---|---|---|---|---|---|---|---|---|']
    byc = defaultdict(Counter)
    for code, f in hh_fam.items():
        e = E.get(code) or {}
        byc[(e.get('country') or '?', (e.get('iso') or '').upper())][f] += 1
    for (cn, iso), c in sorted(byc.items(), key=lambda kv: -sum(kv[1].values()))[:18]:
        tot = sum(c.values())
        L.append(f"| {cn}（{iso}） | {tot} | {c['Microsoft 365']} | {c['Google Workspace']} | {c['主机商邮箱']} | {c['自建服务器']} | {c['企业网关']} | {c['中小企业云邮箱']} | {c['域名已死'] + c['无 MX']} |")
    L += ['', '读法：M365 占比高的国家（英 / 德 / 澳 / 美）群发的「打开率」天然失真，别拿它比土耳其 / 俄罗斯（主机商邮箱为主、像素好使）；'
          '俄罗斯 / 乌兹别克斯坦 / 哈萨克斯坦的 Yandex / Mail.ru 户投递正常但付款汇路要先问。']

    # §六 rules
    L += ['', '## 六、按托管类型的发信守则（已写进各户档案「第 82 批」一节）', '',
          '| 托管类型 | 投递 | 像素可信度 | 怎么发 |', '|---|---|---|---|',
          '| Microsoft 365 | 陌生群发多落「其他 / 垃圾」 | 低（Safe Links 预取 → 可能虚高或 0） | 只 1:1；首封纯文本、≤1 链接、无附件；有旧线程就回旧线程 |',
          '| Google Workspace | 最稳（同生态） | 偏高（图片代理预抓） | 可群发；三箱别同日打同一域；别把 open 当读过 |',
          '| 企业网关（Proofpoint / Mimecast / Barracuda / Hornetsecurity …） | 最差 | 失效 | 不开新线程；回原线程 / LinkedIn / 等对方来信 |',
          '| 主机商附带邮箱（IONOS / OVH / Hostinger / cPanel / 各国主机商） | 好，几乎不丢 | 可用 | 老板自己收：短、一行型号 + 价格 + 一个问题 |',
          '| 自建服务器 | 好，可能灰名单延迟 | 可用 | 技术人读：参数先于价格 |',
          '| 俄语区云邮箱（Yandex / Mail.ru） | 正常 | 可用 | 先问付款银行 / 币种，再报价 |',
          '| 无 MX / 域名已死 | 退信 | — | 地址作废；换域或换渠道；无渠道 → 降级候选 |',
          '', '复查：`python3 scripts/saga_clients/mx_check.py --only-missing`（补新域）或不带参数全量重查（约 1 分钟），再 `python3 mx_report.py` 刷新本页；季度一次够用。']
    out = os.path.join(ROOT, 'docs', f'邮箱域体检_{DATE}.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(out, 'rows', len(rows), 'gateways', len(gw))


if __name__ == '__main__':
    main()
