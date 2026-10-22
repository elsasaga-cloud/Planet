#!/usr/bin/env python3
"""把 git 提交历史渲染成 docs/requirements/变更日志.md（宪法条款：所有变更带时间戳可追溯）。

用法：python3 scripts/changelog.py            # 全量重建
     python3 scripts/changelog.py --since 2026-10-01
只读 git log，不改任何其它文件；每行 = 提交时间(UTC) | 短哈希 | 作者 | 标题 | 改动文件数。
"""
import subprocess, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/requirements/变更日志.md'

def main():
    since = None
    if '--since' in sys.argv:
        since = sys.argv[sys.argv.index('--since') + 1]
    cmd = ['git', '-C', str(ROOT), 'log', '--date=iso-strict', '--pretty=format:%H%x09%ad%x09%an%x09%s', '--shortstat']
    if since:
        cmd.append(f'--since={since}')
    raw = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    rows, cur = [], None
    for line in raw.splitlines():
        if '\t' in line and len(line.split('\t')) == 4:
            if cur: rows.append(cur)
            h, d, a, s = line.split('\t')
            dt = datetime.datetime.fromisoformat(d).astimezone(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
            cur = {'h': h[:9], 'd': dt, 'a': a, 's': s.replace('|', '\\|'), 'files': ''}
        elif line.strip().startswith(tuple('0123456789')) and 'file' in line and cur:
            cur['files'] = line.strip().split(' file')[0]
    if cur: rows.append(cur)
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    lines = ['# 变更日志（由 `scripts/changelog.py` 从 git log 生成）', '',
             f'> 生成：{now}；共 {len(rows)} 次提交；时间为提交时间（UTC）。对话原文见 `对话全记录.md`，需求状态见 `用户要求总账.md`。', '',
             '| 时间（UTC） | 提交 | 作者 | 标题 | 改动文件数 |', '|---|---|---|---|---|']
    for r in rows:
        lines.append(f"| {r['d']} | `{r['h']}` | {r['a']} | {r['s']} | {r['files']} |")
    OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {OUT.relative_to(ROOT)} rows={len(rows)}')

if __name__ == '__main__':
    main()
