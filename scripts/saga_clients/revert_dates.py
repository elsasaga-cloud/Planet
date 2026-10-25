#!/usr/bin/env python3
"""render.py 之后跑：把「只改了日期行」的 Saga Clients/*.md 还原（git checkout），只留真正有内容变化的文件。

render.py 每次都会重写 4 处日期：`updated: YYYY-MM-DD`、`- YYYY-MM-DD：建档（…`、`*建档日期：YYYY-MM-DD …*`、
复核行 `- **YYYY-MM-DD**（14 天 / 30 天）`，以及总览/索引页的 `> 生成：YYYY-MM-DD`。
这些变化没有信息量，还原后 commit 只含实质改动。
用法：cd repo && python3 scripts/saga_clients/revert_dates.py   （原 /tmp/elsa/revert.py，第 74 批(q) 2026-10-25 入库，沙箱重置不再丢）
"""
import re
import subprocess
import sys

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE_ONLY = [
    re.compile(r'^updated: \d{4}-\d{2}-\d{2}\s*$'),
    re.compile(r'^- \d{4}-\d{2}-\d{2}：建档（'),
    re.compile(r'^\*建档日期：\d{4}-\d{2}-\d{2}'),
    re.compile(r'^- \*\*\d{4}-\d{2}-\d{2}\*\*（(14|30) 天）'),
    re.compile(r'^> 生成：\d{4}-\d{2}-\d{2}'),
    re.compile(r'^> \*\*生成\*\*：\d{4}-\d{2}-\d{2}'),
]


def changed_files():
    out = subprocess.check_output(['git', 'status', '--porcelain', '--', 'Saga Clients'], cwd=ROOT, text=True)
    files = []
    for line in out.splitlines():
        st, path = line[:2], line[3:]
        if st.strip() == 'M' or st == ' M' or st == 'M ':
            if path.startswith('"') and path.endswith('"'):
                path = bytes(path[1:-1], 'utf-8').decode('unicode_escape').encode('latin-1').decode('utf-8')
            files.append(path)
    return files


def date_only(path):
    diff = subprocess.run(['git', 'diff', '-U0', '--', path], cwd=ROOT, text=True, capture_output=True).stdout
    for line in diff.splitlines():
        if line.startswith('+++') or line.startswith('---'):
            continue
        if line.startswith('+') or line.startswith('-'):
            body = line[1:]
            if not any(p.match(body) for p in DATE_ONLY):
                return False
    return True


def main():
    files = changed_files()
    reverted = kept = 0
    batch = []
    for f in files:
        if date_only(f):
            batch.append(f)
            reverted += 1
        else:
            kept += 1
    for i in range(0, len(batch), 200):
        subprocess.run(['git', 'checkout', '--'] + batch[i:i + 200], cwd=ROOT, check=True)
    print(f'modified MDs {len(files)}, reverted date-only {reverted}, kept {kept}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
