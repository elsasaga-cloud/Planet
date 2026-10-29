#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成《方法论 V2 · 像素级 SOP（剧本集）》MD + HTML（T29-U133，2026-10-29，Simon：「让其他 agent 像素级 一步一步对照着搞」）。

用法：python3 scripts/sop_v2/build.py [--date YYYY-MM-DD]
- 正文：scripts/sop_v2/parts/s1_core.md … s4_tables_diag.md（手写，按文件名顺序拼接）
- 头部：标题 / UTC + 北京时间戳 / git HEAD / 目录（`## ` 标题自动生成）/ 剧本索引（`### Rnn ·` 自动生成）
- 输出：docs/方法论_V2_像素级SOP_<date>.md / .html（HTML 自包含：内联 <style>，无外链、无脚本）
- HTML 引擎复用 scripts/saga_intro/build.py 的 CSS / 降级转换器（python-markdown 可用时优先）。
- V1（docs/方法论_全集_2026-10-27.md）永不改动；本生成器只产新日期文件。
"""
import datetime
import html
import importlib.util
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PARTS = ROOT / 'scripts' / 'sop_v2' / 'parts'
DOCS = ROOT / 'docs'
TITLE = '方法论 V2 · 像素级 SOP（剧本集）—— 给其他 Agent 一步一步对照着做'


def _engine():
    spec = importlib.util.spec_from_file_location('saga_intro_build', ROOT / 'scripts' / 'saga_intro' / 'build.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def now():
    utc = datetime.datetime.now(datetime.timezone.utc)
    return utc, utc + datetime.timedelta(hours=8)


def git_head():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT).decode().strip()
    except Exception:
        return '未知'


def toc(md):
    return '\n'.join(f'- {m.group(1).strip()}' for m in re.finditer(r'^## (.+)$', md, flags=re.M))


def runbook_index(md):
    rows = []
    for m in re.finditer(r'^### (R\d\d) · (.+)$', md, flags=re.M):
        rows.append(f'| {m.group(1)} | {m.group(2).strip()} |')
    for m in re.finditer(r'^### (D-\d\d) · (.+)$', md, flags=re.M):
        rows.append(f'| {m.group(1)} | {m.group(2).strip()} |')
    return '\n'.join(['| 编号 | 剧本 / 判定表 |', '|---|---|'] + rows)


def build_md(date_str):
    utc, cst = now()
    head = git_head()
    parts = [open(PARTS / n, encoding='utf-8').read() for n in sorted(p.name for p in PARTS.glob('s*.md'))]
    body = '\n'.join(parts)
    header = [
        f'# {TITLE}',
        '',
        f'> **生成时间戳**：{utc.strftime("%Y-%m-%d %H:%M:%S")} UTC（北京时间 {cst.strftime("%Y-%m-%d %H:%M")}）｜仓库 `elsasaga-cloud/Planet` 分支 `arena/3f35b9b3-planet` @ `{head}`｜生成器 `scripts/sop_v2/build.py`（正文在 `scripts/sop_v2/parts/`，改 parts 重跑，不手改本文件）',
        '>',
        '> **这是什么**：V1 `docs/方法论_全集_2026-10-27.md` 的操作版升级——V1 讲「为什么、怎么来的」，本书只讲「现在手怎么动」：每轮固定 **S-00 开工 → 选剧本 → S-99 收工**，25 个剧本（R01–R25）每个都是 编号步骤 + 可复制命令 + ✅ 预期输出 + ❓ 判定表 + 🔁 失败处理 + 📒 台账 + 🏁 完成标准，外加 判定表汇编 / 诊断树 / 禁区 / 质量门。命令与预期数字均为 2026-10-29 在仓库实跑所得。',
        '>',
        '> **读者**：接手本仓库的任何 Agent（包括能力一般的）。前提：先读 `docs/Saga全景信息包_给其他Agent_2026-10-29.md` 知道 Saga 是谁，再用本书干活。本书不含进价 / 邮箱等敏感事实，但整体仍属内部文档。',
        '',
        '## 目录',
        '',
        toc(body),
        '',
        '### 剧本 / 判定表索引',
        '',
        runbook_index(body),
        '',
        '---',
        '',
    ]
    return '\n'.join(header) + body


def build_html(md, date_str, eng):
    try:
        import markdown  # type: ignore
        body = markdown.markdown(md, extensions=['tables', 'fenced_code', 'sane_lists'])
    except Exception:
        body = eng.md_to_html_fallback(md)
    utc, cst = now()
    return (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
        f'<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{html.escape(TITLE)} · {date_str}</title>\n'
        f'<style>{eng.CSS}</style>\n</head>\n<body>\n'
        f'<p class="meta">生成 {utc.strftime("%Y-%m-%d %H:%M:%S")} UTC · 北京时间 {cst.strftime("%Y-%m-%d %H:%M")} · 自包含 HTML（无外链、无脚本）· MD 同名同目录</p>\n'
        + body + '\n</body>\n</html>\n'
    )


def main():
    date_str = None
    if '--date' in sys.argv:
        date_str = sys.argv[sys.argv.index('--date') + 1]
    utc, _ = now()
    date_str = date_str or utc.strftime('%Y-%m-%d')
    eng = _engine()
    md = build_md(date_str)
    md_path = DOCS / f'方法论_V2_像素级SOP_{date_str}.md'
    html_path = DOCS / f'方法论_V2_像素级SOP_{date_str}.html'
    md_path.write_text(md, encoding='utf-8')
    html_path.write_text(build_html(md, date_str, eng), encoding='utf-8')
    n_r = len(re.findall(r'^### R\d\d · ', md, flags=re.M))
    n_d = len(re.findall(r'^### D-\d\d · ', md, flags=re.M))
    n_tbl_md = len(re.findall(r'^\|---', md, flags=re.M))
    n_tbl_html = html_path.read_text(encoding='utf-8').count('<table')
    print(md_path, len(md), 'chars', md.count('\n'), 'lines', 'runbooks', n_r, 'tables-D', n_d)
    print(html_path, html_path.stat().st_size, 'bytes', 'tables md/html', n_tbl_md, n_tbl_html)


if __name__ == '__main__':
    main()
