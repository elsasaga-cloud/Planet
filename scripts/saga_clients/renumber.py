#!/usr/bin/env python3
"""编号重排（T29-U58，2026-10-25，Simon：「重构ABC的客户排序 从001 002依次排序 不要跳数」）。

规则：
- 新编号 = 当前等级字母 + 连号：A → SA-001…，B → SB-001…，C → SC-001…；同级内按旧编号顺序（旧前缀 SA<SB<SC，再按旧号数）排，不跳号。
- 旧登记簿里已不对应任何实体的「死号」（归并掉的别名 / 失效键）改写成 `旧X-nnn`（如 旧C-1713），避免与新号撞车；登记簿里的死键删除。
- 全库改写：研究档 / 实体 / 登记簿 / 各 CSV / 邮箱索引 client 标签 / 监控目标与快照目录 / 文档 / 脚本里的编号；
  不改：V0 答卷（冻结）、对话全记录（逐字留档）、变更日志（git 生成）。
- 产出映射表 data/saga_clients/编号映射_2026-10-25.csv（旧 → 新），供查历史记录。

用法（仓库根目录）：python3 scripts/saga_clients/renumber.py            # 执行
随后：cd scripts/saga_clients && python3 build.py && python3 render.py ；再 python3 scripts/saga_clients/renumber.py --restore-dates
"""
import csv
import glob
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
os.chdir(ROOT)
DATA = 'data/saga_clients'
TODAY = '2026-10-25'
MAP_CSV = f'{DATA}/编号映射_{TODAY}.csv'
SNAP_OLD_MD = '/tmp/renumber_old_md.json'
CODE_RE = re.compile(r'(?<![A-Za-z0-9_])S([ABC])-(\d{3,4})(?![A-Za-z0-9])')
TEXT_EXT = ('.md', '.json', '.jsonl', '.csv', '.py', '.html', '.yml', '.yaml', '.txt', '.js', '.css', '.xml', '.svg', '.tsv')
NEVER = {
    'docs/理解与方向_答卷_2026-10-22.html',      # V0 冻结
    'docs/requirements/对话全记录.md',          # 逐字留档
    'docs/requirements/变更日志.md',            # git 生成
}
DATE_ONLY = [
    re.compile(r'^updated: \d{4}-\d{2}-\d{2}\s*$'),
    re.compile(r'^- \d{4}-\d{2}-\d{2}：建档（'),
    re.compile(r'^\*建档日期：\d{4}-\d{2}-\d{2}'),
    re.compile(r'^- \*\*\d{4}-\d{2}-\d{2}\*\*（(14|30) 天）'),
    re.compile(r'^> 生成：\d{4}-\d{2}-\d{2}'),
    re.compile(r'^> \*\*生成\*\*：\d{4}-\d{2}-\d{2}'),
]


def tracked_files():
    return [f for f in subprocess.check_output(['git', 'ls-files', '-z'], text=True).split('\0') if f]


def read_text(path):
    b = open(path, 'rb').read()
    bom = b.startswith(b'\xef\xbb\xbf')
    return b[3:].decode('utf-8') if bom else b.decode('utf-8'), bom


def write_text(path, s, bom):
    with open(path, 'wb') as f:
        if bom:
            f.write(b'\xef\xbb\xbf')
        f.write(s.encode('utf-8'))


def build_mapping():
    ents = json.load(open(f'{DATA}/entities.json', encoding='utf-8'))
    order = {'A': 0, 'B': 1, 'C': 2}
    mapping = {}
    for g in 'ABC':
        rows = [e for e in ents if e['grade'] == g]
        rows.sort(key=lambda e: (order[e['code'][1]], int(e['code'][3:])))
        for i, e in enumerate(rows, 1):
            mapping[e['code']] = f'S{g}-{i:03d}'
    live = set(mapping)
    # 死号：登记簿值 / 别名 / 人工归并 B 列 / 全库出现过的编号样式 token，但不是现存实体
    dead = set()
    reg = json.load(open(f'{DATA}/编号登记.json', encoding='utf-8'))
    dead |= {c for c in reg['keys'].values() if c not in live}
    for e in ents:
        for a in (e.get('code_aliases') or []) + (e.get('split_from') or []):
            if a not in live:
                dead.add(a)
    for f in tracked_files():
        if f in NEVER or not f.endswith(TEXT_EXT) or f.startswith(('Saga Clients/', 'data/customer_watch/snapshots/', 'data/saga_clients/site_snapshots/', 'data/gmail_e/text/')):
            continue
        if not f.startswith(('docs/', 'scripts/', 'data/saga_clients/', 'data/customer_watch/', 'data/pi_orders/', 'README.md', 'AGENT-CONSTITUTION.md')):
            continue
        s, _ = read_text(f)
        for m in CODE_RE.finditer(s):
            if m.group(0) not in live:
                dead.add(m.group(0))
    dead_map = {c: '旧' + c[1:] for c in dead}
    return ents, mapping, dead_map


def make_mapper(mapping, dead_map):
    def fn(s):
        def rep(m):
            c = m.group(0)
            return mapping.get(c) or dead_map.get(c) or c
        return CODE_RE.sub(rep, s)
    return fn


def rename_paths(mapper):
    """文件/目录名里的编号：两段式改名避免撞车（旧 SA-005 → 新 SA-003 而旧 SA-003 还在）。"""
    paths = set()
    for f in tracked_files():
        if f.startswith('Saga Clients/'):
            continue
        parts = f.split('/')
        for i in range(1, len(parts) + 1):
            p = '/'.join(parts[:i])
            if CODE_RE.search(parts[i - 1]):
                paths.add(p)
                break
    paths = sorted(paths)
    tmp = {}
    for p in paths:
        d, b = os.path.split(p)
        t = os.path.join(d, '__renum__' + b)
        os.rename(p, t)
        tmp[t] = os.path.join(d, mapper(b))
    for t, final in tmp.items():
        if os.path.exists(final):
            raise SystemExit(f'改名撞车：{final}')
        os.rename(t, final)
    return len(paths)


def blanket_files():
    out = []
    for f in tracked_files():
        if f in NEVER or not f.endswith(TEXT_EXT):
            continue
        if f.startswith('Saga Clients/'):
            continue
        if f.startswith(('data/customer_watch/snapshots/', 'data/saga_clients/site_snapshots/', 'data/gmail_e/text/',
                         'data/gmail_a/messages/', 'data/gmail_s/messages/')) or '/attachments/' in f:
            continue
        if f.endswith('threads.json') and f.startswith('data/gmail_'):
            continue
        if f == f'{DATA}/编号登记.json':
            continue
        if f.startswith(('docs/', 'scripts/', 'data/saga_clients/', 'data/customer_watch/', 'data/github_watch/', 'data/pi_orders/', 'data/gmail_e/',
                         'data/gmail_a/', 'data/gmail_s/', 'data/web_recrawl_2026-10-22/', 'data/gmail_elsa_来询未回清单_2026-10.csv', 'data/gmail_已触达清单.csv',
                         'README.md', 'AGENT-CONSTITUTION.md')):
            out.append(f)
    return out


def snapshot_md(mapping=None, dead_map=None):
    """把当前全部客户 MD 按编号存快照（/tmp），供 render 后 --restore-dates 比对；不带映射时 = 原编号。"""
    old_md = {}
    for g in 'ABC':
        for dp, _dns, fns in os.walk(f'Saga Clients/{g}'):
            for fn in fns:
                m = re.match(r'(S[ABC]-\d+)-', fn)
                if m and fn.endswith('.md'):
                    old_md[m.group(1)] = open(os.path.join(dp, fn), encoding='utf-8').read()
    mapping = mapping or {c: c for c in old_md}
    json.dump({'mapping': mapping, 'dead': dead_map or {}, 'old_md': old_md}, open(SNAP_OLD_MD, 'w', encoding='utf-8'), ensure_ascii=False)
    return old_md


def main():
    if '--restore-dates' in sys.argv:
        return restore_dates()
    if '--snapshot-md' in sys.argv:
        # 目录结构调整 / 纯重渲染前用：python3 renumber.py --snapshot-md → render.py → renumber.py --restore-dates
        print(f'MD 快照 {len(snapshot_md())} 份 → {SNAP_OLD_MD}')
        return
    ents, mapping, dead_map = build_mapping()
    mapper = make_mapper(mapping, dead_map)
    print(f'实体 {len(ents)}；映射 {len(mapping)}；死号 {len(dead_map)}')
    # 0. 映射表
    with open(MAP_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['旧编号', '新编号', '等级', '名称', '国家'])
        for e in sorted(ents, key=lambda e: mapping[e['code']]):
            w.writerow([e['code'], mapping[e['code']], e['grade'], e['name'], e['country']])
        for c, n in sorted(dead_map.items()):
            w.writerow([c, n, '—', '（死号：已归并/失效，仅改写以免与新号混淆）', ''])
    # 1. 旧 MD 快照（保留 updated 日期用）：按旧编号 → 内容
    snapshot_md(mapping, dead_map)
    # 2. 登记簿：值映射、死键删除、next 重置
    reg = json.load(open(f'{DATA}/编号登记.json', encoding='utf-8'))
    keys = {}
    dropped = 0
    for k, v in reg['keys'].items():
        if v in mapping:
            keys[k] = mapping[v]
        else:
            dropped += 1
    nxt = {g: 1 + sum(1 for e in ents if e['grade'] == g) for g in 'ABC'}
    json.dump({'next': nxt, 'keys': keys}, open(f'{DATA}/编号登记.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'登记簿：键 {len(keys)}，删除死键 {dropped}，next {nxt}')
    # 3. 整文件改写
    nfile = nhit = 0
    for f in blanket_files():
        s, bom = read_text(f)
        t = mapper(s)
        if t != s:
            nhit += len(CODE_RE.findall(s))
            write_text(f, t, bom)
            nfile += 1
    print(f'整文件改写：{nfile} 个文件')
    # 4. 字段级改写
    #   4a. 邮箱索引：只改 "client": [...]
    seg = re.compile(r'"client":\s*\[[^\]]*\]')
    n = 0
    for f in glob.glob('data/gmail_[as]/messages/*/*.jsonl') + glob.glob('data/gmail_[as]/threads.json'):
        s, bom = read_text(f)
        t = seg.sub(lambda m: mapper(m.group(0)), s)
        if t != s:
            write_text(f, t, bom)
            n += 1
    print(f'邮箱索引 client 标签：{n} 个文件')
    #   4b. 官网快照：只改开头 "code"
    n = 0
    for f in glob.glob(f'{DATA}/site_snapshots/*.json'):
        s, bom = read_text(f)
        t = re.sub(r'^\{"code":"(S[ABC]-\d+)"', lambda m: '{"code":"' + mapper(m.group(1)) + '"', s)
        if t != s:
            write_text(f, t, bom)
            n += 1
    print(f'官网快照 code 字段：{n} 个文件')
    #   4c. 监控快照：只改首行标题
    n = 0
    for f in glob.glob('data/customer_watch/snapshots/*/*'):
        if os.path.isdir(f):
            continue
        s, bom = read_text(f)
        if s.startswith('# '):
            head, _, rest = s.partition('\n')
            h2 = mapper(head)
            if h2 != head:
                write_text(f, h2 + '\n' + rest if _ else h2, bom)
                n += 1
    print(f'监控快照首行：{n} 个文件')
    #   4d. Elsa 箱正文 JSON：只改 note 字段
    n = 0
    for f in glob.glob('data/gmail_e/text/*.json'):
        raw = open(f, encoding='utf-8').read()
        d = json.loads(raw)
        if isinstance(d.get('note'), str) and CODE_RE.search(d['note']):
            d['note'] = mapper(d['note'])
            out = json.dumps(d, ensure_ascii=False, indent=1)
            if raw.endswith('\n'):
                out += '\n'
            open(f, 'w', encoding='utf-8').write(out)
            n += 1
    print(f'Elsa 箱 note 字段：{n} 个文件')
    # 5. 路径改名
    print(f'路径改名：{rename_paths(mapper)} 个')
    print('下一步：cd scripts/saga_clients && python3 build.py && python3 render.py ; cd ../.. && python3 scripts/saga_clients/renumber.py --restore-dates')


def restore_dates():
    """render 后：新 MD 与「旧 MD 经映射」除日期行外一致 → 把日期行换回旧值（编号重排不算内容变化）。"""
    snap = json.load(open(SNAP_OLD_MD, encoding='utf-8'))
    mapping, dead_map, old_md = snap['mapping'], snap['dead'], snap['old_md']
    mapper = make_mapper(mapping, dead_map)
    new_path = {}
    for g in 'ABC':
        for dp, _dns, fns in os.walk(f'Saga Clients/{g}'):
            for fn in fns:
                m = re.match(r'(S[ABC]-\d+)-', fn)
                if m and fn.endswith('.md'):
                    new_path[m.group(1)] = os.path.join(dp, fn)
    kept = restored = differ = 0
    for old, content in old_md.items():
        new = mapping.get(old)
        if not new or new not in new_path:
            differ += 1
            continue
        a = mapper(content).split('\n')
        b = open(new_path[new], encoding='utf-8').read().split('\n')
        if len(a) != len(b):
            differ += 1
            continue
        ok = True
        out = []
        for la, lb in zip(a, b):
            if la == lb:
                out.append(lb)
            elif any(p.match(la) for p in DATE_ONLY) and any(p.match(lb) for p in DATE_ONLY):
                out.append(la)
            else:
                ok = False
                break
        if ok:
            if out != b:
                open(new_path[new], 'w', encoding='utf-8').write('\n'.join(out))
                restored += 1
            else:
                kept += 1
        else:
            differ += 1
    print(f'日期还原：{restored}；无需改：{kept}；内容确有差异：{differ}')


if __name__ == '__main__':
    main()
