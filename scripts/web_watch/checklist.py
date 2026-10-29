#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P 池两月一次人工巡检 · 可勾选清单生成器（T29-U123，2026-10-29）。

从最新 `data/saga_clients/P池_巡检表_*.csv` 生成 `docs/P池_巡检清单_<巡检日>.md`：按区域组 → 档位排序，每户一行，
把「巡检项」长串拆成 6 个可勾选格（官网 / 社媒 / 新闻·展会 / 招聘 / GitHub / MX），并预填自动监控层已覆盖的源数
（`scripts/web_watch/targets_auto.json` layer P）与上次 GitHub 核查结果（`data/saga_clients/github_presence.json`）。
清单只是工作底稿：勾完后结论回写到巡检表「上次巡检 / 备注」，有动静的户按 §0 规则动作；A/B 并池后重跑一次即可。

用法：python3 scripts/web_watch/checklist.py [--csv 路径] [--date 2026-12-28] [--out 路径]
"""
import argparse
import collections
import csv
import glob
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
GROUP_ORDER = ['四主区 + 波兰', '欧洲其他', '俄语区', '印度 / 南亚', '东亚 / 东南亚 / 大洋洲', '中东 / 非洲', '拉美', '其他']
STAR_ORDER = {'★★': 0, '★': 1, '○': 2, '☆': 3, '△': 4}

FAIRS = {
    '四主区 + 波兰': 'SPS（纽伦堡，通常 11 月）/ embedded world（纽伦堡，通常 3 月）/ Hannover Messe（通常 4 月）/ ISC West（拉斯维加斯，通常 3–4 月）/ Automate（北美，通常 5–6 月）/ IFSEC（伦敦，通常 5 月）/ ISAF（伊斯坦布尔，通常 10 月）/ WIN EURASIA（伊斯坦布尔，通常 6 月）/ Automaticon & Securex（波兰）',
    '欧洲其他': 'ISE（巴塞罗那，通常 1–2 月）/ MWC（巴塞罗那，通常 3 月）/ SPS Italia（帕尔马，通常 5 月）/ Sicurezza（米兰，隔年 11 月）/ Elmia Automation（瑞典）/ Expoprotection（巴黎）',
    '俄语区': 'Securika（莫斯科，通常 4 月）/ ЭкспоЭлектроника（莫斯科，通常 4 月）/ Сviaz（莫斯科，通常 6 月）/ KazBuild & Securika Kazakhstan',
    '印度 / 南亚': 'Convergence India（新德里，通常 1–3 月）/ IFSEC India（通常 12 月）/ Automation Expo（孟买，通常 8 月）/ ELECRAMA（隔年 2 月）',
    '东亚 / 东南亚 / 大洋洲': 'Secutech（台北，通常 4–5 月）/ COMPUTEX（台北，通常 5–6 月）/ Security Essen 亚洲版 / CommunicAsia（新加坡，通常 5–6 月）/ Vietnam ETE / Security Expo（澳洲）',
    '中东 / 非洲': 'Intersec（迪拜，通常 1 月）/ GITEX（迪拜，通常 10 月）/ Securex South Africa（通常 5–6 月）/ Cairo ICT（通常 11 月）',
    '拉美': 'Expo Seguridad México（通常 4 月）/ ISC Brasil（圣保罗，通常 3–4 月）/ Futurecom（巴西，通常 10 月）/ Expo Seguridad Chile',
    '其他': '按国家临时查',
}


def latest_csv():
    fs = sorted(glob.glob(os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_*.csv')))
    return fs[-1] if fs else None


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', default=None)
    ap.add_argument('--date', default=None, help='巡检日（默认取巡检表「下次巡检」众数）')
    ap.add_argument('--out', default=None)
    a = ap.parse_args(argv)
    path = a.csv or latest_csv()
    with open(path, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    date = a.date or collections.Counter(r['下次巡检'] for r in rows).most_common(1)[0][0]
    out = a.out or os.path.join(ROOT, 'docs', f'P池_巡检清单_{date}.md')
    # 自动层
    auto = {}
    tp = os.path.join(HERE, 'targets_auto.json')
    if os.path.exists(tp):
        for c in json.load(open(tp, encoding='utf-8'))['customers']:
            kinds = collections.Counter(s['kind'] for s in c.get('sources') or [])
            auto[c['code']] = '+'.join(f'{k}{n}' for k, n in sorted(kinds.items())) or '—'
    gh = {}
    gp = os.path.join(ROOT, 'data', 'saga_clients', 'github_presence.json')
    if os.path.exists(gp):
        for code, g in json.load(open(gp, encoding='utf-8')).items():
            gh[code] = f'有 {len(g["accounts"])} 账号' if g.get('accounts') else '上次无'
    now = subprocess.check_output(['date', '-u', '+%Y-%m-%d %H:%MZ']).decode().strip()
    groups = collections.defaultdict(list)
    for r in rows:
        groups[r['区域组']].append(r)
    n_formal = sum(1 for r in rows if r['入池'] == '正式')
    lines = [f'# P 池人工巡检清单 · {date}（生成 {now}，来源 `{os.path.relpath(path, ROOT)}`，{len(rows)} 户 = 正式 {n_formal} / 观察 {len(rows) - n_formal}）', '',
             '> 两月一次（U117 ⑦）。自动层（`data/customer_watch/当前状态_P.md` / `变化日志_P.md`，每日 02:23Z）先看：有「变化」的户优先勾；其余按本清单逐户 ≈3 分钟。勾完把结论写回巡检表「上次巡检 / 备注」，本文件可重生成（`python3 scripts/web_watch/checklist.py`）。',
             '', '## 0. 怎么勾 / 勾完怎么办', '',
             '| 格 | 看什么 | 去哪看（免费） | 算「有动静」的例子 |', '|---|---|---|---|',
             '| 官网 | 改版 / 新品类 / 新品牌 / 停更 / 跳转 | 自动层快照 diff；`fetch_page` 首页 + 产品页 | 上了新交换机线、换了代理品牌、页面写「acquired by」 |',
             '| 社媒 | LinkedIn / FB / IG 近 2 个月有没有发帖 | `web_search`「公司名 LinkedIn」/ FB 公共页 | 新项目案例、新展会、人事（采购 / 销售总监到任） |',
             '| 新闻·展会 | 新闻稿 / 展会参展商名录 | `web_search`「公司名 2026」/ 展会官网 exhibitor list（区域展会见各组表头） | 参展 = 首触最佳时机（「见到你们在 X 展」） |',
             '| 招聘 | 官网 careers / LinkedIn jobs | `web_search`「公司名 jobs」 | 招网络工程师 / 采购 = 在扩张 |',
             '| GitHub | 账号 / 仓库是否提到网络设备 | `data/saga_clients/github_presence.json`（上次结果预填）；`web_search`「域名 github」 | 新仓库涉及 SONiC / 交换机自动化 → CENTEC 线 |',
             '| MX | 域名 / 邮箱是否还活 | `scripts/saga_clients/mx_check.py --mx`（先 `pip install dnspython`） | NXDOMAIN / 无 MX → 找备用路径 |',
             '', '**勾完的动作**：有动静 → 英文一句话问候 + 对位新品（一个问题，签名 `Saga Telecom - sagatele.com`，按 T29-U28 口径，不报价不推单）；官网 / 品牌变更 → 更新档案并重核对位；'
             '域名死 / MX 失效 → 找备用路径，两轮找不到 → 正式降观察、观察退回原档；观察档两轮（4 个月）无动静且无回信 → 退回原档（写进 sieve，不是 pass）；`q33_hold` 只巡检不主动发；`civil_only` 只谈民用；`ru_payment` 先问收款再谈货。', '']
    for grp in GROUP_ORDER:
        rs = groups.get(grp)
        if not rs:
            continue
        rs.sort(key=lambda r: (STAR_ORDER.get(r['档位'], 9), r['编号']))
        lines += [f'## {grp}（{len(rs)} 户）', '', f'> 本组展会：{FAIRS.get(grp, "")}', '',
                  '| 编号 | 档 | 公司 | 国家 | 域名 / 链接 | 自动源 | 官网 | 社媒 | 新闻·展会 | 招聘 | GitHub | MX | 标签 | 结论 / 动作 |',
                  '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        for r in rs:
            lines.append(f"| {r['编号']} | {r['档位']} | {r['公司'][:40].replace('|', '｜')} | {r['国家']} | {r['域名 / 平台链接'][:48].replace('|', '｜')} | {auto.get(r['编号'], '—')} | ☐ | ☐ | ☐ | ☐ | ☐ {gh.get(r['编号'], '')} | ☐ | {r['标签']} |  |")
        lines.append('')
    open(out, 'w', encoding='utf-8').write('\n'.join(lines))
    print(out, len(rows), {g: len(groups[g]) for g in GROUP_ORDER if groups.get(g)})


if __name__ == '__main__':
    main()
