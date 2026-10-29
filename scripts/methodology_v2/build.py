#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《方法论全集》增补版生成器（T29-U133，2026-10-29，Simon：「方法论_全集_2026-10-27 这个能不能优化 就是加一些其他的 这个是方法论：针对如何工作 分析的」）。

做法：以初版 docs/方法论_全集_2026-10-27.md 的正文为底（原件不改），按锚点**只加不删**地插入 additions/*.md，
      个别过期数字加「2026-10-29 更新」注，输出 docs/方法论_全集_<date>.md + 自包含 .html。
用法：python3 scripts/methodology_v2/build.py [--date YYYY-MM-DD]
additions/ 文件：
  10_thinking.md   → 插在「## A. 信息怎么进来」之前（新章 Ⅰ 思维方法 M1–M14）
  20_A7.md         → 插在 B 章之前（A7）
  30_B5-B8.md      → 插在 C 章之前
  40_C8-C13.md     → 插在 D 章之前
  50_D4-D5.md      → 插在 E 章之前
  60_E6-E10.md     → 插在 F 章之前
  70_F_G_appendix.md → 用 @@F_ROWS / @@G_NOTE / @@MAP_ROWS / @@START_ITEMS / @@FOOTER 分段，各插各处
HTML 引擎复用 scripts/saga_intro/build.py（CSS + 降级转换器；装了 python-markdown 时优先用它）。
"""
import datetime
import html
import importlib.util
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
ADD = HERE / 'additions'
DOCS = ROOT / 'docs'
BASE = DOCS / '方法论_全集_2026-10-27.md'
TITLE = 'Saga / Planet 仓库 · 方法论全集（所有能形成方法论的做法，一处汇编）· 2026-10-29 增补版'


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


def read(name):
    return (ADD / name).read_text(encoding='utf-8')


def insert_before(s, anchor, text):
    assert s.count(anchor) == 1, (anchor, s.count(anchor))
    return s.replace(anchor, text.rstrip('\n') + '\n\n' + anchor)


def insert_after_line(s, anchor_line, text):
    lines = s.split('\n')
    idx = [i for i, l in enumerate(lines) if l == anchor_line]
    assert len(idx) == 1, (anchor_line, len(idx))
    lines.insert(idx[0] + 1, text.rstrip('\n'))
    return '\n'.join(lines)


def annotate(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new)


def toc(md):
    return '\n'.join(f'- {m.group(1).strip()}' for m in re.finditer(r'^## (.+)$', md, flags=re.M))


def build_md(date_str):
    utc, cst = now()
    head = git_head()
    base = BASE.read_text(encoding='utf-8')
    # 1. 去掉初版头部（到第一条 --- 为止），正文从「## 0.」开始
    body = base[base.index('## 0. 先看这个'):]
    # 2. 分段文件
    seg = {}
    cur = None
    for line in read('70_F_G_appendix.md').split('\n'):
        if line.startswith('@@'):
            cur = line[2:].strip()
            seg[cur] = []
        elif cur:
            seg[cur].append(line)
    seg = {k: '\n'.join(v).strip('\n') for k, v in seg.items()}
    # 3. 过期数字加注（只加注，不改原句）
    body = annotate(body, '沙箱会被重置（迄今 16 次）', '沙箱会被重置（迄今 16 次；2026-10-29 更新：24 次）')
    body = annotate(body, "末行应为 `{'A': 90, 'B': 1139, 'C': 3419}`", "末行应为 `{'A': 90, 'B': 1139, 'C': 3419}`（2026-10-29 更新：`{'A': 169, 'B': 1225, 'C': 3253}`，A/B 新标准 + C 捞出后）")
    body = annotate(body, '**快照已跑尽，不要再提议**。', '**快照已跑尽，不要再提议**（2026-10-29 更新：仅指老 A/B；新进群的 ~1,100 户由 `customer-watch` 顺手补抓，见 §C11）。')
    body = annotate(body, '### C5 · 公司底数（官方登记深挖）—— 当前主线（第 82 批试点 → 83–91 批九轮，2026-10-27 05:43Z 起）',
                    '### C5 · 公司底数（官方登记深挖）—— 当前主线（第 82 批试点 → 83–91 批九轮，2026-10-27 05:43Z 起；2026-10-29 更新：已到第 136 批 / 1,487 行，主线转为长期客户群，底数改为「新入库即查 + A 季度复核」，B 只对 B1 做）')
    body = annotate(body, '每轮一条编号条目（现在到 108）', '每轮一条编号条目（现在到 108；2026-10-29 更新：169）')
    body = annotate(body, 'Q-01…65 全部已关 |', 'Q-01…65 全部已关（2026-10-29 更新：编号到 Q-77；Q-77 长期客户群分层待裁定、默认执行） |')
    body = annotate(body, '**总纲一句话**：*信息进来（A）→ 组织成客户体系（B）→ 一户一户加厚 / 挖底（C）→ 按规则对外（D）→ 每一步可追溯、可恢复（E）。*',
                    '**总纲一句话**：*信息进来（A）→ 组织成客户体系（B）→ 一户一户加厚 / 挖底（C）→ 按规则对外（D）→ 每一步可追溯、可恢复（E）。*\n\n**2026-10-29 增补**：A–E 每一步之前都先过 **§Ⅰ 的 14 条思维方法**（怎么复述任务、分级证据、把判断做成规则、机器与人分层、可逆优先、二次验证、缺口盘点、幂等、预算、批处理、怎么读一个客户 / 一封邮件 / 一个官网 / 一个登记页、怎么判「做完了」、被纠偏怎么办）。')
    # 4. 插入新章节
    body = insert_before(body, '## A. 信息怎么进来（读取与入库）', read('10_thinking.md'))
    body = insert_before(body, '---\n\n## B. 信息怎么组织（客户体系）', read('20_A7.md'))
    body = insert_before(body, '---\n\n## C. 信息怎么变厚（加厚与挖掘）', read('30_B5-B8.md'))
    body = insert_before(body, '---\n\n## D. 信息怎么用（对外动作规则）', read('40_C8-C13.md'))
    body = insert_before(body, '---\n\n## E. 怎么不翻车（治理、记录、恢复）', read('50_D4-D5.md'))
    body = insert_before(body, '---\n\n## F. 时间线（每种方法什么时候诞生、被谁的哪句话触发）', read('60_E6-E10.md'))
    body = insert_after_line(body, '| 2026-10-27 T29-U74 | 本文 | 方法论全集 MD + HTML |', seg['F_ROWS'])
    body = insert_after_line(body, '## G. 预案：外部仓库里的客户怎么挖（任务 2，待 Simon 发链接后执行）', '\n' + seg['G_NOTE'])
    map_last = [l for l in body.split('\n') if l.startswith('| 理解类 |')]
    assert len(map_last) == 1
    body = insert_after_line(body, map_last[0], seg['MAP_ROWS'])
    body = insert_after_line(body, '10. 回复：搞定 / 没搞定 + 你要做啥 / 不用做啥。', seg['START_ITEMS'])
    body = annotate(body, '*— 完（2026-10-27 10:34Z 起草，10:4xZ 入库）—*', seg['FOOTER'])
    body = annotate(body, '## 附录 · 给另一个 Agent 的开工十条', '## 附录 · 给另一个 Agent 的开工十四条（初版十条 + 2026-10-29 增补四条）')
    # 5. 头部
    header = [
        f'# {TITLE}',
        '',
        f'> **本版生成**：{utc.strftime("%Y-%m-%d %H:%M:%S")} UTC（北京 {cst.strftime("%Y-%m-%d %H:%M")}），HEAD `{head}`。',
        '> **底本**：2026-10-27 10:34Z 初版 `docs/方法论_全集_2026-10-27.md`（HEAD `d9d20f297`，T29-U74，**原件保留不改**）。本版在其上**只加不删**：新增 **§Ⅰ 怎么分析、怎么决定（思维方法 M1–M14）**；新增方法 **A7 / B5–B8 / C8–C13 / D4–D5 / E6–E10**（共 20 法）；F 时间线续到 10-29；G 预案标记为已执行并指向 A7；文件地图、开工条目补齐；初版正文原样保留，过期数字处加「2026-10-29 更新」注。',
        '> 每一法仍写「**它解决什么 → 怎么做 → 踩过的坑 → 文件在哪 → 诞生时间**」。细则在专项文档里的只给主干 + 链接。',
        '> **三本分工**：本文 = **方法**（怎么工作、怎么分析）；`docs/Saga全景信息包_给其他Agent_2026-10-29.md` = **事实**（Saga 是谁 / 卖什么 / 价 / 客户数字）；`docs/方法论_V2_像素级SOP_2026-10-29.md` = **命令**（本文的操作附录，照抄命令用）。',
        f'> 同名 HTML：`docs/方法论_全集_{date_str}.html`。生成器 `scripts/methodology_v2/build.py`（初版正文 + `additions/*.md`；改 additions 重跑，不手改本文件）。',
        '',
        '## 目录',
        '',
        toc(body),
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
    md_path = DOCS / f'方法论_全集_{date_str}.md'
    html_path = DOCS / f'方法论_全集_{date_str}.html'
    md_path.write_text(md, encoding='utf-8')
    html_path.write_text(build_html(md, date_str, eng), encoding='utf-8')
    n_methods = len(re.findall(r'^### (?:M\d+|[A-G]\d+) · ', md, flags=re.M))
    n_tbl_md = len(re.findall(r'^\|---', md, flags=re.M))
    n_tbl_html = html_path.read_text(encoding='utf-8').count('<table')
    base_len = len(BASE.read_text(encoding='utf-8'))
    print(md_path, len(md), 'chars', md.count('\n'), 'lines', 'methods', n_methods, 'base', base_len)
    print(html_path, html_path.stat().st_size, 'bytes', 'tables md/html', n_tbl_md, n_tbl_html)


if __name__ == '__main__':
    main()
