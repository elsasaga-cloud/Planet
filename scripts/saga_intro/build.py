#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成《Saga 全景信息包（给其他 Agent）》MD + HTML。

用法：python3 scripts/saga_intro/build.py [--date YYYY-MM-DD]
- 叙述部分：scripts/saga_intro/parts/p1_*.md … p4_*.md（手写，按顺序拼接）
- 自动表：data/价格主表.csv（SmartByte/Marvell 线 135 行）、data/价格主表_HRUI.csv（洪瑞 55 行）
- 输出：docs/Saga全景信息包_给其他Agent_<date>.md / .html（HTML 自包含，只有内联 <style>，无外链无脚本）
"""
import csv, html, re, subprocess, sys, datetime, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
PARTS = ROOT / 'scripts' / 'saga_intro' / 'parts'
DOCS = ROOT / 'docs'

TITLE = 'Saga Telecom 全景信息包（给其他 Agent 的参考手册）'


def now():
    utc = datetime.datetime.now(datetime.timezone.utc)
    cst = utc + datetime.timedelta(hours=8)
    return utc, cst


def git_head():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT).decode().strip()
    except Exception:
        return '未知'


def cell(s, n=None):
    s = (s or '').replace('\n', ' ').replace('|', '／').strip()
    s = re.sub(r'\s+', ' ', s)
    if n and len(s) > n:
        s = s[:n - 1] + '…'
    return s


def marvell_tables():
    rows = list(csv.DictReader(open(ROOT / 'data' / '价格主表.csv', encoding='utf-8-sig')))
    groups = collections.OrderedDict()
    for r in rows:
        groups.setdefault(r['系列/节'].strip(), []).append(r)
    out = []
    out.append(f'#### 5.3.1 SmartByte / Marvell 线（`data/价格主表.csv`，{len(rows)} 行，CNY 为 SmartByte 未税价，汇率 {rows[0]["汇率"]} @ {rows[0]["汇率日期"]}）\n')
    na = []
    for g, rs in groups.items():
        out.append(f'**{cell(g)}**（{len(rs)} 款）\n')
        out.append('| Saga 型号 | SmartByte 型号 | 规格摘要 | CNY | USD +20% | USD +25% | USD +30% | Saga 列表价 USD | 备注 |')
        out.append('|---|---|---|---|---|---|---|---|---|')
        for r in rs:
            saga = r['Saga对应型号'].strip()
            if saga.startswith('（Saga 暂无对应'):
                saga = '—（沿用 LT-）'
                na.append(r['SmartByte型号'])
            note = cell(r.get('Saga档位/备注') or r.get('对照说明') or '', 60)
            out.append(f"| {cell(saga)} | {cell(r['SmartByte型号'])} | {cell(r['规格摘要'], 110)} | {cell(r['CNY未税'])} | {cell(r['USD@+20%'])} | {cell(r['USD@+25%'])} | {cell(r['USD@+30%'])} | {cell(r.get('Saga列表价USD'))} | {note} |")
        out.append('')
    out.append(f'- **Saga 暂无对应型号（{len(na)} 款，只能写 SmartByte LT- 型号并注明「Saga 暂无对应型号，沿用 SmartByte 型号 LT-xxx」）**：' + '、'.join(na) + '\n')
    return '\n'.join(out)


def hrui_table():
    rows = list(csv.DictReader(open(ROOT / 'data' / '价格主表_HRUI.csv', encoding='utf-8-sig')))
    out = []
    out.append(f'#### 5.3.2 HRUI 洪瑞 / Realtek 线（`data/价格主表_HRUI.csv`，{len(rows)} 行，CNY 不含税含运费，来源《洪瑞报价-天龙2026930.xls》，汇率 {rows[0]["汇率"]} @ {rows[0]["汇率日期"]}）\n')
    out.append('> 用法：只在客户自己说 Realtek / 低价 / 功能简单时给；报价按本表（2026-09-30 新进价）重算，不要用 Drive 2026 Q3 老美元表（39 款隐含加价 <20%，Q-47）。ZX- 为洪瑞报价单中性型号；「Saga 对应型号」空 = 尚未对照（Q-42）。\n')
    out.append('| ZX 型号 | Saga 对应型号 | 品名 | 规格摘要 | CNY 成本 | USD +20% | USD +25% | USD +30% | 最近采购价 RMB / 日期 |')
    out.append('|---|---|---|---|---|---|---|---|---|')
    for r in rows:
        buy = cell(r.get('最近采购价RMB'))
        if buy:
            buy += ' / ' + cell(r.get('采购日期'))
        out.append(f"| {cell(r['ZX型号'])} | {cell(r.get('Saga对应型号'))} | {cell(r.get('品名'), 40)} | {cell(r.get('规格摘要'), 100)} | {cell(r.get('CNY不含税含运费'))} | {cell(r.get('USD@+20%'))} | {cell(r.get('USD@+25%'))} | {cell(r.get('USD@+30%'))} | {buy} |")
    out.append('')
    return '\n'.join(out)


def toc(md):
    lines = []
    for m in re.finditer(r'^## (.+)$', md, flags=re.M):
        t = m.group(1).strip()
        lines.append(f'- {t}')
    return '\n'.join(lines)


def build_md(date_str):
    utc, cst = now()
    head = git_head()
    parts = [open(PARTS / n, encoding='utf-8').read() for n in sorted(p.name for p in PARTS.glob('p*.md'))]
    body = parts[0] + '\n' + marvell_tables() + '\n' + hrui_table() + '\n'.join(parts[1:])
    header = [
        f'# {TITLE}',
        '',
        f'> **生成时间戳**：{utc.strftime("%Y-%m-%d %H:%M:%S")} UTC（北京时间 {cst.strftime("%Y-%m-%d %H:%M")}）｜仓库 `elsasaga-cloud/Planet` 分支 `arena/3f35b9b3-planet` @ `{head}`｜生成器 `scripts/saga_intro/build.py`',
        '>',
        '> **一句话**：Saga Telecom = Simon 一个人用三个名字经营的、以 Marvell（SmartByte）接入层交换机为核心、CENTEC（Hohunet）为汇聚/核心层、Realtek（HRUI）补位的中国出口 SOHO 品牌；只做海外、只做长期关系、不打价格战、不做云管/轨交/IP67/消费级；四主区土耳其 / 美国 / 英国 / 德国 + 波兰；对外口径「An Engineering & Supply-Chain-First Telecom Partner — Built to Last, Continuous Supply, Evolving Together」。',
        '>',
        '> **性质**：内部参考（含进价 / 毛利 / 邮箱 / 成单明细），不得整段外发。数据截至 2026-10-29（长期客户群 2,045 = A 170 / B 1,875；价格表 SmartByte 2026-09 / 洪瑞 2026-09-30；汇率 6.69 @ 2026-10-17）。',
        '',
        '## 目录',
        '',
        toc(body),
        '',
        '---',
        '',
    ]
    return '\n'.join(header) + body


CSS = """
body{font-family:-apple-system,"Segoe UI","PingFang SC","Microsoft YaHei","Noto Sans CJK SC",Helvetica,Arial,sans-serif;font-size:14px;line-height:1.6;color:#1f2328;max-width:1280px;margin:0 auto;padding:24px 32px;background:#fff}
h1{font-size:26px;border-bottom:2px solid #d0d7de;padding-bottom:8px;margin-top:0}
h2{font-size:20px;border-bottom:1px solid #d8dee4;padding-bottom:6px;margin-top:40px;background:#f6f8fa;padding:8px 10px;border-left:5px solid #0969da}
h3{font-size:16px;margin-top:28px;color:#0a3069}
h4{font-size:14px;margin-top:20px;color:#24292f}
table{border-collapse:collapse;width:100%;margin:10px 0 18px;font-size:12.5px;display:block;overflow-x:auto}
th,td{border:1px solid #d0d7de;padding:5px 8px;vertical-align:top;text-align:left}
th{background:#eef2f6;font-weight:600;white-space:nowrap}
tr:nth-child(even) td{background:#fafbfc}
code{background:#f3f4f6;padding:1px 4px;border-radius:3px;font-size:12px;font-family:SFMono-Regular,Consolas,"Liberation Mono",Menlo,monospace}
pre{background:#f6f8fa;padding:10px 12px;border-radius:6px;overflow-x:auto;font-size:12px;border:1px solid #d8dee4}
pre code{background:none;padding:0}
blockquote{border-left:4px solid #0969da;background:#f0f6ff;margin:12px 0;padding:8px 14px;color:#24292f}
a{color:#0969da;text-decoration:none}
hr{border:0;border-top:1px solid #d0d7de;margin:28px 0}
ul,ol{padding-left:24px}
li{margin:2px 0}
strong{color:#0a0a0a}
.meta{color:#57606a;font-size:12px}
"""


def md_to_html_fallback(md):
    """极简转换（无 markdown 库时）：标题 / 段落 / 列表 / 表格 / 代码块 / 粗体 / 行内代码 / 链接。"""
    out = []
    lines = md.split('\n')
    i = 0
    in_ul = False
    in_pre = False
    in_bq = False

    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'<(https?://[^>]+)>', r'<a href="\1">\1</a>', s)
        s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', s)
        return s

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append('</ul>')
            in_ul = False

    def close_bq():
        nonlocal in_bq
        if in_bq:
            out.append('</blockquote>')
            in_bq = False

    while i < len(lines):
        ln = lines[i]
        if ln.startswith('```'):
            close_ul(); close_bq()
            if not in_pre:
                out.append('<pre><code>'); in_pre = True
            else:
                out.append('</code></pre>'); in_pre = False
            i += 1; continue
        if in_pre:
            out.append(html.escape(ln)); i += 1; continue
        if ln.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:\-|]+\|\s*$', lines[i + 1]):
            close_ul(); close_bq()
            hdr = [c.strip() for c in ln.strip().strip('|').split('|')]
            out.append('<table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in hdr) + '</tr></thead><tbody>')
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('</tbody></table>')
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            close_ul(); close_bq()
            lvl = len(m.group(1))
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>')
            i += 1; continue
        if ln.strip() == '---':
            close_ul(); close_bq(); out.append('<hr>'); i += 1; continue
        if ln.startswith('>'):
            close_ul()
            if not in_bq:
                out.append('<blockquote>'); in_bq = True
            t = ln[1:].strip()
            out.append(f'<p>{inline(t)}</p>' if t else '')
            i += 1; continue
        m = re.match(r'^\s*[-*]\s+(.*)$', ln)
        if m:
            close_bq()
            if not in_ul:
                out.append('<ul>'); in_ul = True
            out.append(f'<li>{inline(m.group(1))}</li>')
            i += 1; continue
        m = re.match(r'^\s*(\d+)\.\s+(.*)$', ln)
        if m:
            close_bq()
            if not in_ul:
                out.append('<ul>'); in_ul = True
            out.append(f'<li>{m.group(1)}. {inline(m.group(2))}</li>')
            i += 1; continue
        if ln.strip() == '':
            close_ul(); close_bq(); i += 1; continue
        close_ul(); close_bq()
        out.append(f'<p>{inline(ln)}</p>')
        i += 1
    close_ul(); close_bq()
    return '\n'.join(out)


def build_html(md, date_str):
    try:
        import markdown  # type: ignore
        body = markdown.markdown(md, extensions=['tables', 'fenced_code', 'sane_lists'])
    except Exception:
        body = md_to_html_fallback(md)
    utc, cst = now()
    return (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
        f'<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{html.escape(TITLE)} · {date_str}</title>\n'
        f'<style>{CSS}</style>\n</head>\n<body>\n'
        f'<p class="meta">生成 {utc.strftime("%Y-%m-%d %H:%M:%S")} UTC · 北京时间 {cst.strftime("%Y-%m-%d %H:%M")} · 自包含 HTML（无外链、无脚本）· MD 同名同目录</p>\n'
        + body + '\n</body>\n</html>\n'
    )


def main():
    date_str = None
    if '--date' in sys.argv:
        date_str = sys.argv[sys.argv.index('--date') + 1]
    utc, cst = now()
    date_str = date_str or utc.strftime('%Y-%m-%d')
    md = build_md(date_str)
    md_path = DOCS / f'Saga全景信息包_给其他Agent_{date_str}.md'
    html_path = DOCS / f'Saga全景信息包_给其他Agent_{date_str}.html'
    md_path.write_text(md, encoding='utf-8')
    html_path.write_text(build_html(md, date_str), encoding='utf-8')
    print(md_path, len(md), 'chars', md.count('\n'), 'lines')
    print(html_path, html_path.stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
