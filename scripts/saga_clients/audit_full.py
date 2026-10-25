#!/usr/bin/env python3
"""全量审计（T29-U57，2026-10-25）：仓库 / 数据 / 信稿 / 文档 / 规矩 一次扫完。

在 scripts/saga_clients 下运行：python3 audit_full.py
产出：docs/requirements/全量审计_机检_<TODAY>.md + data/saga_clients/audit_full_<TODAY>.json
只读；不改任何档案。退出码 1 = 有硬问题。
"""
import csv
import glob
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
TODAY = date.today().isoformat()

hard, soft, info = [], [], []


def H(k, w, x=''):
    hard.append((k, w, str(x)))


def S(k, w, x=''):
    soft.append((k, w, str(x)))


def I(k, x):
    info.append((k, str(x)))


# ---------- 1. 实体 / 编号 / 目录 ----------
ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
codes = [e['code'] for e in ents]
dup = [c for c, n in Counter(codes).items() if n > 1]
if dup:
    H('实体', '编号重复', dup[:10])
grades = Counter(e['grade'] for e in ents)
I('实体', f"{len(ents)} 户 · 等级 {dict(grades)}")
for e in ents:
    if not e.get('name'):
        S('实体', '无名称', e['code'])
    if e['grade'] not in ('A', 'B', 'C'):
        H('实体', '等级非 A/B/C', f"{e['code']} {e['grade']}")
    if e['code'][1] != e['code'][1]:
        pass
E = {e['code']: e for e in ents}
reg = json.load(open(os.path.join(DATA, '编号登记.json'), encoding='utf-8'))
reg_codes = set(reg['keys'].values()) if isinstance(reg.get('keys'), dict) else set()
missing_reg = [c for c in codes if c not in reg_codes]
if missing_reg:
    S('编号', '实体编号不在登记表（可能是拆分/新号）', missing_reg[:10])
folder = Counter()
md_codes = {}
for g in 'ABC':
    for fn in os.listdir(os.path.join(ROOT, 'Saga Clients', g)):
        if fn.endswith('.md') and not fn.startswith('_'):
            folder[g] += 1
            md_codes[fn.split('-')[0] + '-' + fn.split('-')[1]] = g
for g in 'ABC':
    if folder[g] != grades[g]:
        H('目录', f'{g} 目录 MD 数 ≠ 等级数', f'{folder[g]} vs {grades[g]}')
for c, e in E.items():
    if md_codes.get(c) != e['grade']:
        H('目录', 'MD 所在目录与等级不符', f"{c} md={md_codes.get(c)} grade={e['grade']}")
for c in md_codes:
    if c not in E:
        H('目录', '孤儿 MD（无实体）', c)

# ---------- 2. 研究档 schema ----------
R = {}
for p in glob.glob(os.path.join(DATA, 'research', '*.json')):
    c = os.path.basename(p)[:-5]
    try:
        R[c] = json.load(open(p, encoding='utf-8'))
    except Exception as ex:  # noqa
        H('研究档', 'JSON 解析失败', f'{c}: {ex}')
I('研究档', f'{len(R)} 份')
WHEN_OK = re.compile(r'^(现在|立即|2026-1[12]|2027|不动|群发节奏|待 Simon|按 WA|按 Simon|跟 PI|被动|随 S[ABC]-|待新地址|不主动|不单独发|按群发|Elsa|待|随|第 \d+ 单|标书|季度|停止|—)')
DATE_RE = re.compile(r'^\d{4}-\d{2}(-\d{2})?')
drafts = {}
DIRS = Counter()
ACTIVE_WHEN = re.compile(r'^(现在|立即|2026-1[12]|2027)')
for c, d in R.items():
    if c not in E:
        H('研究档', '研究档无对应实体', c)
        continue
    g = E[c]['grade']
    mr = d.get('mail_review')
    if g in 'AB' and not mr:
        H('研究档', 'A/B 无 mail_review', c)
        continue
    if not mr:
        continue
    need_keys = ('binding', 'situation', 'need', 'breakpoint', 'saga_now', 'next_move', 'facts') if g in 'AB' else ('binding', 'next_move')
    for k in need_keys:
        if not mr.get(k) and not (k == 'saga_now' and str((mr.get('next_move') or {}).get('when', '')).startswith('不动')):
            H('研究档', f'mail_review 缺 {k}', c)
    cs = str(E[c].get('c_sub') or '')
    if ('退订' in cs or '拒绝' in cs) and mr.get('draft_en') and ACTIVE_WHEN.match(str((mr.get('next_move') or {}).get('when') or '')):
        H('研究档', '退订/拒绝户仍有活跃信稿', f'{c} c_sub={cs} when={(mr.get("next_move") or {}).get("when")}')
    sn = mr.get('saga_now') or {}
    tier = sn.get('tier')
    if tier not in (20, 25, 30, None):
        H('研究档', 'tier 非 20/25/30/None', f'{c} {tier!r}')
    nm = mr.get('next_move') or {}
    w = str(nm.get('when') or '')
    if g in 'AB' and not w:
        H('研究档', 'next_move.when 空', c)
    elif w and not WHEN_OK.match(w):
        S('研究档', 'when 词表外', f'{c} {w[:40]}')
    for f in mr.get('facts') or []:
        dt = str(f.get('date') or '')
        if not DATE_RE.match(dt):
            S('研究档', '事实日期格式', f'{c} {dt!r}')
        elif dt[:10] > TODAY:
            H('研究档', '事实日期在未来', f'{c} {dt}')
        DIRS[str(f.get('dir'))] += 1
        if not str(f.get('quote') or '').strip():
            S('研究档', '事实 quote 空', c)
    de = mr.get('draft_en')
    if de is not None:
        if not (isinstance(de, dict) and de.get('subject') and de.get('body')):
            H('研究档', 'draft_en 形状错', c)
        else:
            drafts[c] = de
    ao = str(mr.get('as_of') or '')
    if ao and ao > TODAY:
        H('研究档', 'as_of 在未来', f'{c} {ao}')
    go = d.get('grade_override')
    if go not in ('A', 'B', 'C', None, ''):
        H('研究档', 'grade_override 非法', f'{c} {go!r}')
I('信稿', f'{len(drafts)} 份（A/B/C 全部）')
I('研究档', f'事实 dir 取值分布 {dict(DIRS.most_common())}')

# ---------- 3. 信稿红线（全等级） ----------
PHONE = re.compile(r'(\+\d[\d\s\-()]{7,}\d)|(\b1[35]\d{9}\b)|(\b0\d{2,3}-\d{7,8}\b)')
BAD_PHRASES = [
    ('OEM Factory', 'Saga.md：「OEM Factory」已弃'),
    ('trading company', '不自称贸易商'),
    ('UL compliant', '不声称 UL'),
    ('UL-listed', '不声称 UL'),
    ('list price', '不写 list price'),
    ('EXW list', '不写 EXW list'),
    ('in stock', '不写 in stock'),
    ('free sample', '样品付费'),
    ('s.sagatelecom', '对外不写 s. 邮箱'),
    ('152371', '对外不写 152 手机'),
    ('NDAA-compliant', 'NDAA 不声称'),
    ('ERPS', '只写 ring redundancy'),
]
SIGN_RE = re.compile(r'\n(Best regards|Kind regards|Thank you)[,.]?\n(Simon|Alan|Elsa)\n', re.S)
for c, de in drafts.items():
    body = de['body']
    subj = de['subject']
    private = 'WhatsApp' in subj or '私信' in subj or '微信' in subj
    for ph, why in BAD_PHRASES:
        if ph.lower() in body.lower():
            # 允许：复述客户自己的原话/页面（「Your site lists …」「you asked for …」或引号内）
            i = body.lower().find(ph.lower())
            ctx = body[max(0, i - 120):i].lower()
            if ph == 'NDAA-compliant' and ('your site' in ctx or 'you asked' in ctx or 'your rfq' in ctx or 'you listed' in ctx):
                continue
            if ph == 'ERPS' and re.search(r'"[^"]*ERPS[^"]*"', body):
                continue
            H('信稿', f'红线短语「{ph}」', f'{c}：{why}')
    m = PHONE.search(body)
    if m and not private:
        H('信稿', '正文含电话号码', f'{c} {m.group(0)}')
    if re.search(r'[\u4e00-\u9fff]', body) and not private:
        H('信稿', '英文稿含中文', c)
    if not private:
        if '?' not in body:
            H('信稿', '无问句', c)
        sig = re.search(r'\n(Simon|Alan|Elsa)\n', body + '\n')
        if not sig:
            S('信稿', '署名不在 Simon/Alan/Elsa 之列或缺失', c)
        elif 'Saga Telecom' not in body[sig.start():]:
            S('信稿', '署名后无公司行', c)
        if sig:
            who = sig.group(1)
            chn = str(((R[c]['mail_review'].get('next_move') or {}).get('channel') or ''))
            want = 'Alan' if chn.startswith('A 邮箱') else 'Simon' if chn.startswith('S 邮箱') else 'Elsa' if chn.startswith(('Elsa', 'E 邮箱')) else None
            if want and who != want:
                H('信稿', '署名 ≠ 渠道邮箱人名（A 箱=Alan / S 箱=Simon / Elsa 箱=Elsa）', f'{c} 署名 {who} 渠道 {chn[:30]}')
        if re.search(r'valid(ity)?\s*(for\s*)?(\d+)[ -]day', body):
            for n in re.findall(r'valid(?:ity)?\s*(?:for\s*)?(\d+)[ -]day', body):
                if n != '15':
                    H('信稿', '有效期 ≠ 15 天', f'{c} {n}')
        for n in re.findall(r'(\d+)-day validity', body):
            if n != '15':
                H('信稿', '有效期 ≠ 15 天', f'{c} {n}')
    if E[c]['grade'] == 'C':
        nm = (R[c]['mail_review'].get('next_move') or {})
        if not str(nm.get('when') or '').startswith(('不动', '被动', '待', '现在', '2027', '2026', '不主动', '—')):
            S('信稿', 'C 级信稿 when 异常', f"{c} {nm.get('when')}")

# ---------- 4. 剔除名单 × 信稿渠道 ----------
excl = {}
p = os.path.join(DATA, '群发剔除名单_2026-10-24.csv')
for r in csv.DictReader(open(p, encoding='utf-8-sig')):
    excl[r['地址'].strip().lower()] = r
I('剔除名单', f'{len(excl)} 地址')
ACTIVE = re.compile(r'^(现在|立即|2026-1[12]|2027)')
for c, d in R.items():
    mr = d.get('mail_review') or {}
    nm = mr.get('next_move') or {}
    w = str(nm.get('when') or '')
    if not ACTIVE.match(w) or not mr.get('draft_en'):
        continue
    ch = str(nm.get('channel') or '').lower()
    hits = [a for a in excl if a in ch]
    for a in hits:
        cat = excl[a]['类别']
        if '拒绝' in cat or '移除' in cat or '婉拒' in cat or '退订' in cat:
            H('剔除', '信稿渠道地址在剔除名单（拒绝/移除/婉拒）且 when 活跃', f'{c} {a} [{cat}] when={w}')
        elif '退信' in cat:
            S('剔除', '信稿渠道地址曾退信', f'{c} {a} [{cat}]')

# 按客户编号：明确拒绝/移除 → 不得有活跃信稿；婉拒 → 只许 2027 一句
for addr, r in excl.items():
    c = r.get('客户编号', '').strip()
    if c not in R:
        continue
    mr = R[c].get('mail_review') or {}
    w = str((mr.get('next_move') or {}).get('when') or '')
    cat = r['类别']
    if not mr.get('draft_en'):
        continue
    if ('拒绝' in cat or '移除' in cat or '退订' in cat) and ACTIVE.match(w):
        H('剔除', '明确拒绝/移除户仍有活跃信稿', f'{c} {addr} [{cat}] when={w}')
    elif '婉拒' in cat and ACTIVE.match(w) and not w.startswith('2027'):
        H('剔除', '婉拒户信稿不在 2027', f'{c} {addr} [{cat}] when={w}')

# ---------- 5. MD ↔ JSON（主题在 MD 内） ----------
for c, de in drafts.items():
    g = E[c]['grade']
    fns = [f for f in os.listdir(os.path.join(ROOT, 'Saga Clients', g)) if f.startswith(c + '-')]
    if not fns:
        H('渲染', 'MD 缺失', c)
        continue
    md = open(os.path.join(ROOT, 'Saga Clients', g, fns[0]), encoding='utf-8').read()
    if de['subject'] not in md:
        H('渲染', 'MD 未含信稿主题（需重渲染）', c)

# ---------- 6. 文档：README 编号 / Q 清单 / 变更日志 / 对话全记录 ----------
readme = open(os.path.join(ROOT, 'README.md'), encoding='utf-8').read()
nums = [int(x) for x in re.findall(r'^(\d+)\. ', readme, re.M)]
seq = list(range(1, max(nums) + 1)) if nums else []
missing_items = sorted(set(seq) - set(nums))
dups = [n for n, k in Counter(nums).items() if k > 1]
I('README', f'条目 1..{max(nums) if nums else 0}；缺 {missing_items[:10]}；重 {dups[:10]}')
if dups:
    S('README', '条目编号重复', dups)
q = open(os.path.join(ROOT, 'docs', 'requirements', '待统一处理问题清单.md'), encoding='utf-8').read()
qn = sorted({int(x) for x in re.findall(r'\| Q-(\d+) \|', q)})
qmiss = sorted(set(range(1, max(qn) + 1)) - set(qn)) if qn else []
I('Q 清单', f'Q-01..Q-{max(qn):02d}；缺 {qmiss}')
open_q = []
for line in q.split('\n'):
    m = re.match(r'\| Q-(\d+) \|', line)
    if m and not re.search(r'已裁|已结案|结案|已关闭|已完成|已做|已执行|撤销|作废|已解决|不再|已落地', line):
        open_q.append(f'Q-{int(m.group(1)):02d}')
I('Q 清单', f'无明确结案词的条目 {len(open_q)}：{" ".join(open_q)}')
chg = open(os.path.join(ROOT, 'docs', 'requirements', '变更日志.md'), encoding='utf-8').read()
chg_rows = len(re.findall(r'^\| \d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC \| `[0-9a-f]{7,}`', chg, re.M))
ncommit = int(subprocess.check_output(['git', 'rev-list', '--count', 'HEAD'], cwd=ROOT).decode().strip())
I('变更日志', f'{chg_rows} 行 vs git 提交 {ncommit}（日志晚一次提交属正常）')
if ncommit - chg_rows > 3:
    S('变更日志', '落后 git 提交超过 3 次', f'{chg_rows} vs {ncommit}')
conv = open(os.path.join(ROOT, 'docs', 'requirements', '对话全记录.md'), encoding='utf-8').read()
heads = re.findall(r'^### (T\d+(?:-U\d+)?)[^\n]*?(\d{4}-\d{2}-\d{2} \d{2}:\d{2})', conv, re.M)
last = None
for h, ts in heads:
    if last and ts < last[1]:
        S('对话全记录', '用户轮次时间倒序', f'{h} {ts} < {last[0]} {last[1]}')
    last = (h, ts)
I('对话全记录', f'{len(heads)} 个带 Z 时间的用户轮次头；最后 {last}')

# ---------- 7. 价格表 ----------
pm = list(csv.DictReader(open(os.path.join(ROOT, 'data', '价格主表.csv'), encoding='utf-8-sig')))
fx = Counter(r.get('汇率') for r in pm)
I('价格主表', f'{len(pm)} 行；汇率 {dict(fx)}')
dupm = [m for m, n in Counter(r.get('Saga对应型号') for r in pm if r.get('Saga对应型号')).items() if n > 1]
if dupm:
    S('价格主表', 'Saga 型号重复行', dupm[:10])

# ---------- 8. 日历 ----------
for ym in ('2026-11', '2026-12'):
    cal = open(os.path.join(ROOT, 'docs', f'跟进日历_{ym}.md'), encoding='utf-8').read()
    sec = cal.split(f'## {ym}（', 1)[-1].split('\n## ', 1)[0]
    n_cal = len(re.findall(r'^\| S[ABC]-\d+', sec, re.M))
    n_json = sum(1 for c, d in R.items() if str(((d.get('mail_review') or {}).get('next_move') or {}).get('when') or '').startswith(ym) and E.get(c, {}).get('grade') in 'AB')
    I('日历', f'{ym}：表 {n_cal} 行 vs 研究档 A/B when 以 {ym} 开头 {n_json}')
    if abs(n_cal - n_json) > 5:
        S('日历', f'{ym} 行数与研究档偏差 >5', f'{n_cal} vs {n_json}')

# ---------- 9. 仓库卫生 ----------
st = subprocess.check_output(['git', 'status', '--short'], cwd=ROOT).decode()
I('git', f'未提交条目 {len([l for l in st.splitlines() if l.strip()])}')
for bad in ('gmail', '__pycache__'):
    if os.path.isdir(os.path.join(ROOT, bad)):
        S('仓库', f'根目录存在 {bad}/', '')
v0 = subprocess.check_output(['git', 'log', '--oneline', '--', 'docs/理解与方向_答卷_2026-10-22.html'], cwd=ROOT).decode().strip().splitlines()
I('V0', f'历史提交 {len(v0)} 次（应为 1）')
if len(v0) != 1:
    H('V0', 'V0 被改动过', v0)

# ---------- 输出 ----------
out = {'hard': hard, 'soft': soft, 'info': info, 'today': TODAY}
json.dump(out, open(os.path.join(DATA, f'audit_full_{TODAY}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
L = [f'# 全量审计 · {TODAY}', '', '> 生成：`scripts/saga_clients/audit_full.py`（只读）。硬问题 = 必须修；软项 = 眼核。', '']
L.append(f'## 概览\n\n- 硬问题 {len(hard)} / 软项 {len(soft)}\n')
L.append('## 基本数（info）\n')
for k, x in info:
    L.append(f'- **{k}**：{x}')
L.append('\n## 硬问题\n')
if not hard:
    L.append('- 无')
for k, w, x in hard:
    L.append(f'- [{k}] {w}：{x}')
L.append('\n## 软项\n')
if not soft:
    L.append('- 无')
by = defaultdict(list)
for k, w, x in soft:
    by[(k, w)].append(x)
for (k, w), xs in by.items():
    L.append(f'- [{k}] {w}（{len(xs)}）：{"；".join(xs[:12])}{" …" if len(xs) > 12 else ""}')
open(os.path.join(ROOT, 'docs', 'requirements', f'全量审计_机检_{TODAY}.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(f'hard {len(hard)} soft {len(soft)} | report docs/requirements/全量审计_机检_{TODAY}.md')
for k, w, x in hard[:60]:
    print('  HARD', k, w, x[:160])
sys.exit(1 if hard else 0)
