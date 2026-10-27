# -*- coding: utf-8 -*-
"""data/external_clients/*.json → External Clients/<repo>/A|B|C/<code>-<name>-<国家>.md + 各库 00-索引.md + 00-总索引.md
只从 JSON 渲染（INH 规则：render-from-JSON）。人工改级写 data/external_clients/overrides.json：{code: {grade, reason, date}}。"""
import json
import os
import re
import shutil
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
from common import DATA, ROOT

OUT = os.path.join(ROOT, 'External Clients')
REPOS = [
    ('edgecore.json', 'Edgecore', 'E', 'OEM / 贴牌 + 低价标品（Edgecore 渠道已习惯白牌/开放网络，拿价格与贴牌能力切）',
     'elsasaga-cloud/Edgecore（Edgecore where-to-buy SI/VAR 名录深挖；profile/A|B|C）'),
    ('mikrotik.json', 'mikrotik-info', 'M', 'SmartByte 商用管理型（Marvell）为主 + Saga STI 工业系列补位（MikroTik/Allied/工业品牌渠道，缺的是性价比管理型与工业 PoE）',
     'elsasaga-cloud/mikrotik-info（客户名单_反向信号_2026-09.csv 1,032 行，只取 A/B 747；profile/A|B）'),
    ('cctv.json', 'CCTV-PoE', 'C', 'HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）',
     'elsasaga-cloud/CCTV-PoE（03 清单 + profile/ + smartbyte/ + exhibition/；待导入）'),
]
GRADE_TXT = {'A': 'XA 长期跟进', 'B': 'XB 慢慢跟进', 'C': 'XC 暂不管'}


def safe(s, n=60):
    s = re.sub(r'[\\/:*?"<>|\n\r\t]+', ' ', s or '').strip()
    s = re.sub(r'\s+', ' ', s)
    return s[:n].rstrip(' .')


def esc(s):
    return (s or '').replace('|', '｜').replace('\n', ' ').strip()


def md_table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    for r in rows:
        r = list(r) + [''] * (len(header) - len(r))
        out.append('| ' + ' | '.join(esc(str(c)) for c in r[:len(header)]) + ' |')
    return '\n'.join(out)


def load_overrides():
    p = os.path.join(DATA, 'overrides.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def render_record(r, repo, product_line, src_desc, ov):
    g = r['grade']
    code = r['code']
    o = ov.get(code)
    grade_now = o['grade'] if o else g
    lines = []
    lines.append(f"# {code} · {r['name']} · {r['country_zh']}")
    lines.append('')
    if r.get('src_code'):
        src_txt = f"来源 {repo} `{r['src_code']}`（原评级 {r.get('src_grade', '')}" + (f"，阶段 {r['stage']}" if r.get('stage') else '') + '）'
    else:
        src_txt = f"来源 {repo} `{r['src_path']}`:{r.get('src_line', '')}" + (f"（其分级 {r['their_class']}类）" if r.get('their_class') else '')
    head = [f"**初判 {GRADE_TXT[grade_now]}**", src_txt, f"导入 2026-10-27", '研究状态：未研究（第 2 步待做）']
    if o:
        head.insert(1, f"人工改级 {o['date']}：{o['grade']}（{o['reason']}）")
    lines.append('> ' + ' ｜ '.join(head))
    lines.append('')
    lines.append('## 1. 初判与理由')
    lines.append(f"- 初判：**X{grade_now}** — {r['grade_reason']}")
    if o:
        lines.append(f"- 人工改级：X{o['grade']}（{o['date']}，{o['reason']}）；编号不变")
    lines.append('- 标记：' + ('、'.join(r['flags']) if r['flags'] else '无'))
    if r.get('saga_dup'):
        d = r['saga_dup']
        lines.append(f"- 与 Saga Clients 重叠：**{d['code']}**（Saga 评级 {d['grade']}，经域名 {d['via']}）→ 以 Saga 档为主；本条只保留来源库事实")
    else:
        lines.append('- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）')
    if r.get('repo_dup'):
        lines.append(f"- 库内重复：与来源库 `{r['repo_dup']}` 同域名，研究时合并判断")
    lines.append('- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）')
    lines.append('')
    lines.append('## 2. 基本事实（来源库口径，未经本库复核）')
    rows = [('公司', r['name']), ('国家 / 城市', r['country_zh'] + (f" / {r['city']}" if r.get('city') else '')), ('ISO', r['iso'] or '待核'),
            ('网站', r.get('website') or '—'), ('类型 / 角色', r.get('type') or '—')]
    if r.get('signals'):
        rows.append(('在卖品牌（反向信号）', r['signals']))
    if r.get('own_brand'):
        rows.append(('自有品牌', r['own_brand']))
    if r.get('entry_point'):
        rows.append(('切入点（来源库）', r['entry_point']))
    if r.get('src_biz_org') or r.get('src_business_model'):
        rows.append(('组织 / 模式（来源库推断）', ' / '.join(x for x in [r.get('src_biz_org'), r.get('src_business_model')] if x)))
    if r.get('src_segment'):
        rows.append(('细分（来源库）', r['src_segment']))
    if r.get('src_volume'):
        rows.append(('量级（来源库推断）', r['src_volume']))
    if r.get('src_needs'):
        rows.append(('需求标签（来源库）', '、'.join(map(str, r['src_needs']))))
    if r.get('src_risk'):
        rows.append(('风险标签（来源库）', '、'.join(map(str, r['src_risk']))))
    rows.append(('他们首推（仅参考，不照搬）', r.get('src_p1') or '—'))
    if r.get('src_priority') or r.get('src_status'):
        rows.append(('来源库优先级 / 状态', ' / '.join(x for x in [r.get('src_priority'), r.get('src_status')] if x)))
    if r.get('src_source'):
        rows.append(('来源库之来源', r['src_source']))
    if r.get('src_note'):
        rows.append(('来源库备注', r['src_note']))
    if r.get('src_rating_basis'):
        rows.append(('来源库评级依据', r['src_rating_basis']))
    if r.get('src_manual'):
        rows.append(('来源库人工定级', r['src_manual']))
    if r.get('their_class') or r.get('stars'):
        rows.append(('来源库分级 / 星级（仅参考）', ' / '.join(x for x in [(r.get('their_class') + '类') if r.get('their_class') else '', ('★' * r['stars']) if r.get('stars') else ''] if x)))
    if r.get('heading_path'):
        rows.append(('来源章节', ' > '.join(r['heading_path'][-3:])))
    if r.get('kv'):
        for k, v in list(r['kv'].items())[:40]:
            if k and v and k not in ('公司全称', '公司名', '国家'):
                rows.append((f'来源库字段·{k}', v))
    rows.append(('来源文件', f"`{r['src_path']}`" + (f" 第 {r['src_line']} 行" if r.get('src_line') else '') + f" @ {r.get('src_repo_ref', '')}" + (f"（更新 {r['src_updated']}）" if r.get('src_updated') else '')))
    if r.get('also'):
        rows.append(('同一家在来源库其他位置', '；'.join(f"`{a['src_path']}`:{a['src_line']}（{a.get('heading', '')[:40]}）" for a in r['also'][:12])))
    lines.append(md_table(['项', '内容'], rows))
    facts = [x for x in (r.get('facts') or []) if x and x[0] not in ('项', '内容')]
    if facts:
        lines.append('')
        lines.append('来源库「基本事实」表（原样）：')
        lines.append('')
        width = max(len(x) for x in facts)
        hdr = ['项', '内容', '层级'][:width] if width <= 3 else ['内容', '标签'] + [''] * (width - 2)
        lines.append(md_table(hdr if len(hdr) == width else [f'列{i+1}' for i in range(width)], facts))
    lines.append('')
    lines.append('## 3. 联系方式')
    if r['emails']:
        for e in r['emails']:
            lines.append(f"- 邮箱：{e['addr']}（{e['status']}）")
    else:
        lines.append('- 邮箱：无（表单或待挖）')
    if r.get('phones'):
        lines.append('- 电话：' + '；'.join(r['phones'][:4]) + '（内部用，不进外发材料）')
    if r.get('entry_contact'):
        lines.append(f"- 来源库入口字段：{r['entry_contact']}")
    ct = (r.get('contact_text') or '').strip()
    if ct:
        ct = '\n'.join(l for l in ct.split('\n') if 'R71 跟进核对' not in l and '不补造' not in l)
        lines.append('')
        lines.append('来源库「联系方式」段原文：')
        lines.append('')
        lines.extend('> ' + l for l in ct.split('\n'))
    lines.append('')
    lines.append('## 4. 关键人（KP）')
    kp = r.get('kp')
    if isinstance(kp, list) and kp:
        lines.append(md_table(['姓名', '角色', '联系方式', '状态/核实度', '来源', '性质'],
                              [(k['name'], k['role'], k['contact'], k['status'], k['source'], '猜测/待查' if k['guess'] else '实名') for k in kp]))
    elif (r.get('kp_text') or '').strip():
        lines.extend('> ' + l for l in r['kp_text'].strip().split('\n'))
    else:
        lines.append('- 无（待挖）')
    lines.append('')
    lines.append('## 5. 证据与来源 URL（来源库）')
    if r.get('evidence_urls'):
        lines.extend(f'- {u}' for u in r['evidence_urls'][:25])
    else:
        lines.append('- 无')
    et = (r.get('evidence_text') or '').strip()
    if et:
        lines.append('')
        lines.extend('> ' + l for l in et.split('\n')[:30])
    lines.append('')
    lines.append('## 6. 已知触达')
    t = r.get('touch')
    if t:
        lines.append(f"- Saga S 箱群发：「{t['主题']}」→ {t['邮箱']}，首次 {t['首次']}，最后 {t['最后']}，去信 {t['去信']}，来信 {t['来信']}"
                     f"（对账源 `data/gmail_s/2026-09_10群发名单_未入库.csv`；来信含自动回复，需人工看）")
    else:
        lines.append('- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱')
    if r.get('followups'):
        fu = [x for x in r['followups'] if x and x[0] not in ('#', '序', '日期') and any(c.strip() for c in x)]
        if fu:
            lines.append('- 来源库跟进记录：')
            lines.append('')
            w = max(len(x) for x in fu)
            lines.append(md_table([f'列{i+1}' for i in range(w)], fu))
    if r.get('r_notes'):
        lines.append('- 来源库核验 / 退信摘录：')
        for n in r['r_notes']:
            lines.append(f"  - {n['title']}")
            lines.extend(f'    - {esc(l)[:300]}' for l in n['lines'][:8])
    lines.append('')
    if r.get('raw'):
        lines.append('## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）')
        lines.append('')
        lines.extend('> ' + l for l in r['raw'].split('\n')[:60])
        for a in (r.get('also') or [])[:5]:
            if a.get('raw'):
                lines.append('>')
                lines.append(f"> ——另见 `{a['src_path']}`:{a['src_line']}：")
                lines.extend('> ' + l for l in a['raw'].split('\n')[:15])
        lines.append('')
    lines.append('## 7. 我方产品线提示')
    lines.append(f'- {product_line}')
    lines.append('- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`')
    lines.append('- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）')
    lines.append('')
    lines.append('## 8. 研究与跟进（第 2 步起填）')
    lines.append('- 研究状态：未研究')
    lines.append('- 研究结论 / 升降建议：—')
    lines.append('- 下一步：—')
    lines.append('')
    return '\n'.join(lines)


def main():
    ov = load_overrides()
    os.makedirs(OUT, exist_ok=True)
    summary = []
    for fn, repo, letter, product_line, src_desc in REPOS:
        p = os.path.join(DATA, fn)
        if not os.path.exists(p):
            summary.append((repo, None, src_desc, product_line))
            continue
        d = json.load(open(p, encoding='utf-8'))
        recs = [r for r in d['records'] if r['grade'] != 'DELETE']
        base = os.path.join(OUT, repo)
        for g in 'ABC':
            gd = os.path.join(base, g)
            if os.path.isdir(gd):
                shutil.rmtree(gd)
            os.makedirs(gd)
        idx_rows = []
        cnt = Counter()
        for r in recs:
            g = ov.get(r['code'], {}).get('grade', r['grade'])
            cnt[g] += 1
            fname = f"{r['code']}-{safe(r['name'])}-{safe(r['country_zh'], 12)}.md"
            rel = f"{g}/{fname}"
            with open(os.path.join(base, rel), 'w', encoding='utf-8') as f:
                f.write(render_record(r, repo, product_line, src_desc, ov))
            live = [e['addr'] for e in r['emails'] if e['status'] != '停用']
            idx_rows.append((f"[{r['code']}]({rel.replace(' ', '%20')})", r.get('src_code') or f"{r['src_path'].split('/')[-1][:18]}:{r.get('src_line', '')}", r['name'], r['country_zh'], (r.get('type') or '')[:28],
                             f"X{g}", r['grade_reason'][:40], live[0] if live else ('（停用）' + r['emails'][0]['addr'] if r['emails'] else '—'),
                             '是' if r.get('kp_named') else '—', r['saga_dup']['code'] if r.get('saga_dup') else '—',
                             (r['touch']['最后'] + ' 去' + r['touch']['去信'] + '/来' + r['touch']['来信']) if r.get('touch') else '—'))
        deleted = [r for r in d['records'] if r['grade'] == 'DELETE']
        idx = [f"# {repo} · External Clients 索引", '',
               f"- 来源：{src_desc}；快照 `{d['src']}`（分支 `{d['branch']}`）",
               f"- 导入 2026-10-27：{len(recs)} 户（XA {cnt['A']} / XB {cnt['B']} / XC {cnt['C']}）" + (f"；剔除大陆 {len(deleted)}" if deleted else ''),
               f"- 产品线：{product_line}",
               '- 编号：`X<等级>-' + letter + '<序号>`，导入时一次分配、永不重排；研究后升降 = 改等级 + 移文件夹，编号不动（可能出现 XA 编号躺在 B 文件夹，与 Saga Clients 同理）',
               '- 初判 = 机械规则（方案草案 §3）：主攻区（美加/欧/土）+ 渠道型买家 + 可用邮箱 → XA；对口但非主攻区 / 个人顾问 / 缺邮箱 / 风险国 → XB；与 Saga 重叠 / 原厂同行 / 超大集团 / 来源库 C → XC。第 2 步逐户研究后再定。',
               '- 已知触达 = S 箱 2026-09/10「24 Port PoE Managed Switch」群发名单对账（`data/gmail_s/2026-09_10群发名单_未入库.csv`）', '',
               md_table(['编号', '原编号', '公司', '国家', '类型', '初判', '理由（节选）', '首选邮箱', '实名KP', 'Saga重叠', 'S箱触达(最后/去/来)'], idx_rows), '']
        if len(idx_rows) > 800:
            hdr_lines = idx[:-2]
            links = []
            for g in 'ABC':
                sub = [row for row in idx_rows if row[5] == f'X{g}']
                fn_g = f'00-索引-X{g}.md'
                open(os.path.join(base, fn_g), 'w', encoding='utf-8').write('\n'.join(hdr_lines + [f'（本页只列 X{g}，{len(sub)} 户）', '', md_table(['编号', '原编号', '公司', '国家', '类型', '初判', '理由（节选）', '首选邮箱', '实名KP', 'Saga重叠', 'S箱触达(最后/去/来)'], sub), '']))
                links.append(f'- [{fn_g}]({fn_g})：X{g} {len(sub)} 户')
            idx = hdr_lines + ['', '索引按等级分页：'] + links + ['', '侧表：`data/external_clients/cctv_未导入条目.csv`（粗体/表格里不像公司的条目与理由）、`cctv_非客户段落.csv`、`cctv_剔除大陆.csv`', '']
        open(os.path.join(base, '00-索引.md'), 'w', encoding='utf-8').write('\n'.join(idx))
        summary.append((repo, cnt, src_desc, product_line, len(recs), len(deleted), d['src']))
        print(repo, dict(cnt), 'deleted', len(deleted))
    top = ['# External Clients · 总索引', '',
           '外部三仓（Edgecore / mikrotik-info / CCTV-PoE）客户全量进库。四步：① 全量导入（本页）→ ② 逐户深研定级 XA/XB/XC → ③ 跟进（与 S 箱群发对账）→ ④ 加厚/KP。方案：`docs/external_repos/External_Clients_方案草案_2026-10-27.md`；通读：`docs/external_repos/通读记录_2026-10-27.md`。',
           '', '## 数量', '', '| 库 | 导入 | XA | XB | XC | 剔除大陆 | 快照 | 索引 |', '|---|---|---|---|---|---|---|---|']
    for s in summary:
        if s[1] is None:
            top.append(f"| {s[0]} | 待导入 | — | — | — | — | — | — |")
        else:
            repo, cnt, src_desc, pl, n, dele, src = s
            top.append(f"| {repo} | {n} | {cnt['A']} | {cnt['B']} | {cnt['C']} | {dele} | `{src}` | [{repo}/00-索引.md]({repo}/00-索引.md) |")
    top += ['', '## 规则', '',
            '- 目录：每库独立 `A/ B/ C/`（三库目的与跟进策略不同，Simon 2026-10-27 定）。',
            '- 编号：`XA-E001`（Edgecore）/ `XA-M001`（mikrotik-info）/ `XA-C001`（CCTV-PoE）；X = 外部，第二字母 = 导入时初判等级，连字符后字母 = 来源库；一次分配永不重排。',
            '- 大陆公司一律不导入（Simon：直接删除）；外部库已删的存档不复活。',
            '- 与 Saga Clients 重叠（按域名，公共邮箱域除外）→ XC-重复，以 Saga 档为主，本条只存来源库事实。',
            '- 产品线：Edgecore → OEM/贴牌 + 低价；mikrotik-info → SmartByte 商用管理型（Marvell）+ STI 工业补位；CCTV-PoE → HRUI PoE + SmartByte PoE。三库与 Planet 一样都是冲着 Marvell 芯片产品去的。',
            '- 人工改级：`data/external_clients/overrides.json`（code → grade/reason/date）→ 重跑 `scripts/external_clients/render.py`；档案只从 JSON 渲染，不手改 MD。',
            '- 来源库的信稿 / 三步计划 / SWOT / 首推型号不照搬：只留事实、联系方式、KP、证据 URL、跟进与退信记录。', '']
    open(os.path.join(OUT, '00-总索引.md'), 'w', encoding='utf-8').write('\n'.join(top))


if __name__ == '__main__':
    main()
