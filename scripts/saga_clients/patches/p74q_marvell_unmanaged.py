"""第 74 批(q) 2026-10-25：研究档 email_hook / one_question / draft_en.body 里把「Marvell-based」挂到非网管型号
（STI-050GE/080GE/280GE/054GP/144GP/154GP/244GP/288GP/110GE/21616GP、HRUI 线）上的措辞改正——规则 ㉛：
「Marvell」只给网管 L2/L2+/L3。网管款在同一句里的，改成「…units (managed versions on a Marvell platform)」。
幂等：再跑一次应 0 变更。json.dump 沿用各文件原缩进（库内 1 空格 1049 份 / 2 空格 409 份）。"""
import json, re, glob, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
R = [
 (r'(?<![\w-])Marvell-based (neutral-brand )?DIN-rail 5-GE, 8-GE \+ 2 SFP and 8-PoE \+ 2 SFP (?:managed )?(units|switches)', r'\1DIN-rail 5-GE, 8-GE + 2 SFP and 8-PoE + 2 SFP \2 (managed versions on a Marvell platform)'),
 (r'neutral-brand Marvell-based DIN-rail 5-GE, 8-GE \+ 2 SFP and 8-PoE \+ 2 SFP (?:managed )?(units|switches)', r'neutral-brand DIN-rail 5-GE, 8-GE + 2 SFP and 8-PoE + 2 SFP \1 (managed versions on a Marvell platform)'),
 (r'Marvell-based DIN-rail 5-GE and 8-GE \+ 2 SFP managed units', 'DIN-rail 5-GE and 8-GE + 2 SFP units (the managed 8-GE on a Marvell platform)'),
 (r'Marvell-based DIN-rail 4-PoE \+ 1 (GE|SFP) and 8-PoE \+ 2 SFP managed units', r'DIN-rail 4-PoE + 1 \1 and 8-PoE + 2 SFP units (the 8-PoE managed version on a Marvell platform)'),
 (r'Marvell-based DIN-rail 4-PoE( \+ 1 (?:GE|SFP))? and 8-PoE \+ 2 SFP units', r'DIN-rail 4-PoE\1 and 8-PoE + 2 SFP units (managed versions on a Marvell platform)'),
 (r'Marvell-based DIN-rail 4-PoE \+ 1 GE and 4-PoE \+ 2 SFP managed units', 'DIN-rail 4-PoE + 1 GE and 4-PoE + 2 SFP units (the managed one on a Marvell platform)'),
 (r'Marvell-based DIN-rail 5-port and 8-PoE \+ 4×10G industrial units', 'DIN-rail 5-port and 8-PoE + 4×10G industrial units (the latter L2+ managed on a Marvell platform)'),
 (r'Marvell-based DIN-rail 4-PoE \+ 1 GE, 5-GE and gigabit MC units', 'DIN-rail 4-PoE + 1 GE, 5-GE and gigabit MC units'),
 (r'Marvell-based DIN-rail 5/8-port gigabit( copper| \(and PoE\))? units', r'DIN-rail 5/8-port gigabit\1 units'),
 (r'Marvell-based 5/8-port DIN-rail units', '5/8-port DIN-rail units'),
 (r'Marvell-based DIN-rail 5/8-GE units', 'DIN-rail 5/8-GE units'),
 (r'Marvell-based DIN-rail 8-port copper gigabit \(and 8 \+ 2 SFP\) industrial units', 'DIN-rail 8-port copper gigabit (and 8 + 2 SFP) industrial units'),
 (r'DIN-rail Marvell-based 8-port gigabit \(and PoE\) industrial switches', 'DIN-rail 8-port gigabit (and PoE) industrial switches'),
 (r'Marvell-based DIN-rail 8-GE and 8-PoE \+ 2 SFP units', 'DIN-rail 8-GE and 8-PoE + 2 SFP units'),
 (r'Marvell-based DIN-rail 8-GE \+ 2 SFP and 8-PoE \+ 2 SFP units', 'DIN-rail 8-GE + 2 SFP and 8-PoE + 2 SFP units (managed versions on a Marvell platform)'),
 (r'Marvell-based DIN-rail 8-GE/8-PoE \+ 2 SFP units and gigabit MCs', 'DIN-rail 8-GE/8-PoE + 2 SFP units (managed versions on a Marvell platform) and gigabit MCs'),
 (r'Marvell-based DIN-rail 8-GE \+ 2 SFP \(and PoE\) switches and gigabit media converters', 'DIN-rail 8-GE + 2 SFP (and PoE) switches (managed versions on a Marvell platform) and gigabit media converters'),
 (r'Marvell-based DIN-rail 8-GE \+ 2 SFP managed and 8-PoE \+ 2 SFP models', 'DIN-rail 8-GE + 2 SFP managed (Marvell platform) and 8-PoE + 2 SFP models'),
 (r'Marvell-based DIN-rail 8-GE \+ 2 SFP and 24-GE \+ 4×10G switches', 'DIN-rail 8-GE + 2 SFP units and Marvell-based 24-GE + 4×10G managed switches'),
 (r'Marvell-based DIN-rail 8-port PoE\+ switches with 2 SFP \(−40~75 °C\) and the managed version', 'DIN-rail 8-port PoE+ switches with 2 SFP (−40~75 °C) and the managed version (Marvell platform)'),
 (r'Marvell-based DIN-rail 8-port PoE and gigabit industrial switches', 'DIN-rail 8-port PoE and gigabit industrial switches'),
 (r'Marvell-based DIN-rail 4-PoE \+ 1 and 5-port gigabit industrial units', 'DIN-rail 4-PoE + 1 and 5-port gigabit industrial units'),
 (r'Marvell-based DIN-rail 5-port gigabit and 4-PoE \+ 1 industrial units', 'DIN-rail 5-port gigabit and 4-PoE + 1 industrial units'),
 (r'Marvell-based 4-PoE \+ 1 industrial and 8-PoE \+ 2 SFP commercial units', '4-PoE + 1 industrial and 8-PoE + 2 SFP commercial units (the latter L2+ managed on a Marvell platform)'),
 (r'the Marvell-based 4-PoE \+ SFP DIN unit', 'the 4-PoE + SFP DIN unit'),
 (r'the Marvell-based equivalent I supply', 'the equivalent I supply'),
 (r'Marvell-based gigabit PoE DIN switch in 8\+2 SFP and 4\+1 formats', 'gigabit PoE DIN switch in 8+2 SFP and 4+1 formats (the 8+2 also as a Marvell-based managed version)'),
 (r'Marvell-based 5-port \(4 PoE\+\) industrial units', '5-port (4 PoE+) industrial units'),
 (r'\(Marvell-based, −40~75 °C, neutral packing\)', '(−40~75 °C, neutral packing)'),
 (r'a Marvell-based, neutral-packed STI 4-port PoE \+ 2×SFP unit', 'a neutral-packed STI 4-port PoE + 2×SFP unit'),
 (r'we build Marvell-based DIN/rack industrial 16-PoE \+ 2 SFP units', 'we build DIN/rack industrial 16-PoE + 2 SFP units'),
 (r'a Marvell-based 8-port Gigabit \+ 2 SFP industrial switch', 'an 8-port Gigabit + 2 SFP industrial switch'),
 (r'we build Marvell-based 5/8-port DIN-rail units', 'we build 5/8-port DIN-rail units'),
 (r'Marvell-based DIN-rail units under the Fibersystem label', 'DIN-rail units under the Fibersystem label'),
 (r'a Marvell-based neutral-brand DIN-rail 8-GE \+ 2 SFP line', 'a neutral-brand DIN-rail 8-GE + 2 SFP line (unmanaged, or managed on a Marvell platform)'),
 (r'Marvell/Realtek-based gigabit media converters and 8-GE \+ 2 SFP switches', 'gigabit media converters and 8-GE + 2 SFP switches'),
 (r'second source for Marvell/Realtek-based gigabit and PoE media converters', 'second source for gigabit and PoE media converters'),
 (r'we supply Marvell/Realtek-based industrial gigabit and PoE media converters', 'we supply industrial gigabit and PoE media converters'),
 (r'Marvell/Realtek DIN units \(2-SFP \+ 8-PoE, 1-SFP MC\)', 'DIN units (2-SFP + 8-PoE, 1-SFP MC)'),
 (r'second ODM source on a Marvell platform — industrial 8-PoE \+ 2 SFP, FE/gigabit PoE media converters, commercial 8-PoE \+ 2 SFP L2\+ —', 'second ODM source — industrial 8-PoE + 2 SFP, FE/gigabit PoE media converters, commercial 8-PoE + 2 SFP L2+ (Marvell platform) —'),
 (r'second source on a Marvell/Realtek platform \(', 'second source on our industrial platform ('),
]
UNMANAGED_IN_LIST = re.compile(r'(?<![\d/])5-GE|5/8-port|(?<![\d/])4-PoE|(?<![\d/])4/8-PoE|DIN-rail 8-PoE \+ 2 SFP,|8-GE \+ 2 SFP, 8-PoE \+ 2 SFP;')


def r13(t):
    def rep(m):
        inner = m.group(1)
        if UNMANAGED_IN_LIST.search(inner):
            return f'({inner}; managed versions on a Marvell platform)'
        return m.group(0)
    return re.sub(r'on a Marvell platform \(([^)]*)\)', rep, t)


def fix(t):
    if not isinstance(t, str) or 'Marvell' not in t:
        return t, False
    o = t
    for a, b in R:
        t = re.sub(a, b, t)
    t = r13(t)
    t = re.sub(r'\(managed versions on a Marvell platform\) \(([^)]*)\)', r'(\1; managed versions on a Marvell platform)', t)
    t = re.sub(r'\((the [^()]*?on a Marvell platform)\) \(([^)]*)\)', r'(\2; \1)', t)
    return t, t != o


def main():
    changed = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data/saga_clients/research/S[AB]-*.json'))):
        raw = open(f, encoding='utf-8').read()
        indent = len(raw.split('\n', 2)[1]) - len(raw.split('\n', 2)[1].lstrip(' ')) if '\n' in raw else 1
        d = json.loads(raw)
        mr = d.get('mail_review') or {}
        ch = []
        t, c = fix(d.get('email_hook'))
        if c:
            d['email_hook'] = t; ch.append('hook')
        nm = mr.get('next_move')
        if isinstance(nm, dict):
            t, c = fix(nm.get('one_question'))
            if c:
                nm['one_question'] = t; ch.append('oq')
        de = mr.get('draft_en')
        if isinstance(de, dict):
            t, c = fix(de.get('body'))
            if c:
                de['body'] = t; ch.append('body')
        if d.get('code') == 'SB-957':
            sf = d.get('saga_fit') or {}
            if sf.get('p1') == 'STI-280GE':
                sf['p1'] = 'STI-280GM'; ch.append('p1')
                rep = ('管理 STI-280GE（$50.5 @30%）', '管理 STI-280GM（$73.8 @30%；非管理 STI-280GE $50.5）')
                if isinstance(sf.get('why'), str):
                    sf['why'] = sf['why'].replace(*rep)
                if isinstance(mr.get('need'), str):
                    mr['need'] = mr['need'].replace(*rep)
                sn = mr.get('saga_now')
                if isinstance(sn, dict):
                    sn['p1'] = 'STI-280GM'
                    if isinstance(sn.get('why'), str):
                        sn['why'] = sn['why'].replace(*rep)
        if ch:
            changed[d['code']] = ch
            with open(f, 'w', encoding='utf-8') as fh:
                json.dump(d, fh, ensure_ascii=False, indent=indent or 1)
    print(len(changed), changed)


if __name__ == '__main__':
    main()
