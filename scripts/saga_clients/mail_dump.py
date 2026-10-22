#!/usr/bin/env python3
"""把某个客户在 S 邮箱里的全部往来按时间顺序倒出来，供「针对性复盘」时逐封阅读（只读，不改任何仓库文件）。

用法：python3 mail_dump.py SA-011 [--chars 700] [--out /tmp/elsa/SA-011.txt]
匹配规则与 gmail_digest.py 一致：实体域名 / 实体邮箱 / 邮箱别名.csv。
输出每封：序号 | 日期 | 方向 | 发件人 → 收件人 | 主题 | 附件名 | 正文前 N 字（去引用）。
"""
import json, sys, glob, csv, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / 'data/saga_clients'
FREE = {'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'live.com', 'aol.com', 'icloud.com', 'protonmail.com', 'mail.ru', 'yandex.ru', 'qq.com', '163.com', '126.com'}


def load_targets(code):
    ents = {e['code']: e for e in json.load(open(DATA / 'entities.json', encoding='utf-8'))}
    e = ents[code]
    doms = {d.lower() for d in (e.get('domains') or []) if d and d.lower() not in FREE}
    mails = {m.lower() for m in (e.get('emails') or []) + (e.get('corp_emails') or []) if m}
    p = DATA / '邮箱别名.csv'
    if p.exists():
        for r in csv.DictReader(open(p, encoding='utf-8-sig')):
            if r.get('编号', '').strip() == code:
                v = r.get('邮箱或域名', '').strip().lower()
                (mails if '@' in v else doms).add(v)
    return e, doms, mails


def hit(m, doms, mails):
    ppl = [m.get('from') or {}] + (m.get('to') or []) + (m.get('cc') or [])
    for p in ppl:
        a = (p.get('e') or '').lower()
        if not a:
            continue
        if a in mails or a.split('@')[-1] in doms:
            return True
    return False


def strip_quote(t):
    out = []
    for ln in (t or '').splitlines():
        s = ln.strip()
        if s.startswith('>'):
            break
        if re.match(r'^(On .+wrote:|From: |-----Original Message|Sent from my|在.+写道：)', s):
            break
        out.append(ln)
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip()


def main():
    code = sys.argv[1]
    chars = int(sys.argv[sys.argv.index('--chars') + 1]) if '--chars' in sys.argv else 700
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
    e, doms, mails = load_targets(code)
    rows = []
    for f in sorted(glob.glob(str(ROOT / 'data/gmail_*/messages/*/*.jsonl'))):
        acct = f.split('/data/')[1].split('/')[0]
        for line in open(f, encoding='utf-8'):
            m = json.loads(line)
            if hit(m, doms, mails):
                m['_acct'] = acct
                rows.append(m)
    rows.sort(key=lambda m: m.get('date') or '')
    L = [f"# {code} {e.get('name')} | domains={sorted(doms)} emails={sorted(mails)} | {len(rows)} msgs"]
    for i, m in enumerate(rows, 1):
        to = ', '.join((p.get('e') or '') for p in (m.get('to') or [])[:3])
        att = '; '.join(a.get('n', '') for a in (m.get('att') or []))
        L.append(f"\n--- [{i}] {m.get('date')} {m.get('dir').upper()}{' (bulk)' if m.get('bulk') else ''} k={m.get('k')} {m['_acct']}")
        L.append(f"{(m.get('from') or {}).get('e')} -> {to} | {m.get('subj')}" + (f" | ATT: {att}" if att else ''))
        L.append(strip_quote(m.get('text'))[:chars])
    txt = '\n'.join(L)
    if out:
        pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
        open(out, 'w', encoding='utf-8').write(txt)
        print(out, len(rows))
    else:
        print(txt)


if __name__ == '__main__':
    main()
