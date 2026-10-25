"""第 75 批：规则 ㉕「任何数不得高于 2026-06 列表价」——2.5G-SFP 工业 DGG 家族（及 STC-448DGGM / STI-21616DGGPM）
档位价高于 Saga 列表价的，研究档里的钩子句 / 信稿 / need / why 文本统一封顶到列表价。
只动 A/B；解释性文字（「档位 139.9–151.6 超上限」「PDF 上限」「封顶」）不动。
用法：python3 p75_pdf_cap.py [--apply]
"""
import glob, json, re, sys

ROOT = __file__.split('/scripts/')[0]
APPLY = '--apply' in sys.argv
ents = {e['code']: e for e in json.load(open(f'{ROOT}/data/saga_clients/entities.json', encoding='utf-8'))}

# number → [(model, cap)] 候选；多候选时按窗口里最近出现的型号名判定
CANDS = {
    '139.9': [('STI-288DGGPM', '137.5'), ('STI-244DGGPM', '121.0')],
    '145.7': [('STI-288DGGPM', '137.5'), ('STC-424DGGPM-280W', None)],   # None = 不封（24 口 30% 档合规）
    '151.6': [('STI-288DGGPM', '137.5')],
    '157.8': [('STI-288DGGPM-2BT', '154.0')],
    '164.4': [('STI-288DGGPM-2BT', '154.0')],
    '171.0': [('STI-288DGGPM-2BT', '154.0')],
    '125.6': [('STI-280DGGM', '121.0')],
    '130.8': [('STI-280DGGM', '121.0')],
    '136.0': [('STI-280DGGM', '121.0')],
    '129.1': [('STI-244DGGPM', '121.0')],
    '134.5': [('STI-244DGGPM', '121.0'), ('STC-424DGGPM-280W', None)],
    '147.1': [('STI-244DGGPM-2BT', '143.0'), ('STI-488DGGPM', None)],
    '153.2': [('STI-244DGGPM-2BT', '143.0'), ('STI-488DGGPM', '148.5')],
    '159.3': [('STI-244DGGPM-2BT', '143.0'), ('STI-488DGGPM', '148.5')],
    '118.4': [('STI-240DGGM', '110.0')], '123.3': [('STI-240DGGM', '110.0')], '128.3': [('STI-240DGGM', '110.0')],
    '171.9': [('STI-488DGGPM-2BT', '165.0'), ('STI-488XGGPM', None)], '178.8': [('STI-488DGGPM-2BT', '165.0'), ('STI-488XGGPM', None)],
    '153.2': [('STI-244DGGPM-2BT', '143.0'), ('STI-488DGGPM', '148.5')],
    '138.3': [('STI-480DGGM', '132.0')], '143.8': [('STI-480DGGM', '132.0')],
    '250.4': [('STI-21616DGGPM', '242.0')], '260.4': [('STI-21616DGGPM', '242.0')],
    '236.8': [('STC-448DGGM', '220.0')], '246.6': [('STC-448DGGM', '220.0')], '256.5': [('STC-448DGGM', '220.0')],
    '321.4': [('STC-448DGGPM', '308.0')], '334.2': [('STC-448DGGPM', '308.0')],
    '224.2': [('STC-424DGGPM-440W', '220.0')], '233.2': [('STC-424DGGPM-440W', '220.0')],
}
SKIP_CTX = re.compile(r'超上限|超）|超;|PDF 上限|封顶|档位 1|列表价 \$|第 7\d 批\(\w\)?[^）]*由|→ \$|改为|原 hook|误用')
# 无型号名时的描述词（钩子句 / 信稿）：8 口 PoE + 2 SFP 管理型 → STI-288DGGPM；24 口 → STC-424DGGPM
DESC_288 = re.compile(r'(8[-× x]*(port |PoE|GbE)|8 x Gigabit PoE|8-port PoE\+ managed|8 PoE|DIN)', re.I)
DESC_424 = re.compile(r'24[-× x]*(port|PoE|x Gigabit)|280 W|280W', re.I)


def nearest(window, names):
    best = None
    for n in names:
        i = window.rfind(n)
        if i >= 0 and (best is None or i > best[1]):
            best = (n, i)
    return best[0] if best else None


def decide(num, window):
    cands = CANDS[num]
    names = [c[0] for c in cands]
    hit = nearest(window, names)
    if hit:
        return dict(cands)[hit], hit
    if len(cands) == 1:
        return cands[0][1], cands[0][0]
    # 无型号名：按描述词
    if num in ('145.7', '134.5'):
        tail = window[-140:]
        if DESC_424.search(tail) and not DESC_288.search(tail[-60:]):
            return None, 'STC-424DGGPM-280W(desc)'
        if DESC_288.search(tail):
            return dict(cands)[names[0]], names[0] + '(desc)'
        return 'AMBIG', None
    if num == '139.9':
        tail = window[-90:]
        if re.search(r'4[-× x]*(port|PoE|GbE|x Gigabit)', tail) and not DESC_288.search(tail):
            return '121.0', 'STI-244DGGPM(desc)'
        return '137.5', 'STI-288DGGPM(desc-default)'
    return 'AMBIG', None


changes = []
for f in sorted(glob.glob(f'{ROOT}/data/saga_clients/research/S[AB]-*.json')):
    code = f.rsplit('/', 1)[1][:-5]
    if ents.get(code, {}).get('grade') not in ('A', 'B'):
        continue
    raw = open(f, encoding='utf-8').read()
    s = raw
    touched = []
    for lst, rep, model in (('139.9/145.7/151.6', '137.5（列表价封顶）', 'STI-288DGGPM'), ('157.8/164.4/171.0', '154.0（列表价封顶）', 'STI-288DGGPM-2BT'),
                            ('125.6/130.8/136.0', '121.0（列表价封顶）', 'STI-280DGGM'), ('139.9–151.6 USD', '137.5 USD（列表价封顶）', 'STI-288DGGPM')):
        if lst in s and not SKIP_CTX.search(s[max(0, s.find(lst) - 90):s.find(lst)]):
            s = s.replace(lst, rep); touched.append((lst, rep, model, 'slash-list'))
    for num in CANDS:
        n_comma = num.replace('.', ',')
        pat = re.compile(r'(?<![0-9.,])(' + re.escape(num) + r')(?![0-9])|(?<![0-9.,])(' + re.escape(n_comma) + r')(?=\s?USD)')
        pos = 0
        out = []
        last = 0
        for m in pat.finditer(s):
            window = s[max(0, m.start() - 220):m.start()]
            after = s[m.end():m.end() + 30]
            if SKIP_CTX.search(window[-90:] + after):
                continue
            if window.endswith('/') or after.startswith('/') or window.endswith('–') or after.startswith('–') or after.startswith('-'):
                continue
            # 只动带货币语境的数（$ 前缀 / USD 后缀 / 「，$」）
            if not (window.endswith('$') or window.endswith('$ ') or re.match(r'\s?USD|\s?EXW| USD', after) or m.group(2)):
                continue
            cap, model = decide(num, window)
            if model and '(' not in model and model not in window and model not in s:
                cap = 'AMBIG'   # 单候选但全文无该型号名 → 不猜
            if cap == 'AMBIG':
                changes.append((code, num, 'AMBIG', window[-80:].replace('\n', ' ')))
                continue
            if cap is None:
                continue
            rep = cap if m.group(1) else cap.replace('.', ',')
            out.append(s[last:m.start()]); out.append(rep); last = m.end()
            touched.append((num, cap, model, window[-70:].replace('\n', ' ') + '|' + after[:20].replace('\n', ' ')))
        if out:
            out.append(s[last:]); s = ''.join(out)
    if touched:
        d = json.loads(s)
        if APPLY:
            # 在 saga_now.price 里留一句
            mr = d.get('mail_review') or {}
            sn = mr.get('saga_now')
            models = sorted({t[2].split('(')[0] for t in touched})
            note = '（㉕ 封顶：' + ' / '.join(models) + ' 档位价高于 2026-06 列表价，文本按列表价改；第 75 批 2026-10-25）'
            if isinstance(sn, dict):
                sn['price'] = (sn.get('price') or '') + note
            ind = len(raw.split('\n', 2)[1]) - len(raw.split('\n', 2)[1].lstrip(' ')) or 1
            json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=ind)
        for t in touched:
            changes.append((code,) + t)

for c in changes:
    print(c)
print('files', len({c[0] for c in changes}), 'changes', len(changes), 'APPLY' if APPLY else 'DRY')
