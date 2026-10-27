#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T29-U64 · 第 82 批 渲染块：邮箱域体检（MX）+ 假日避让（按该户 next_move.when 算窗口）+ 公司底数（官方登记）+ 官网标价样本。

render.py 调用 fmt_batch82(ent, research) → markdown 字符串（无数据返回 ''）。
输入（都缺省可跳过）：
  data/saga_clients/mx_check_<date>.json           mx_check.py
  data/saga_clients/holidays_2026-11_2027-03.json  holidays_cal.py
  data/saga_clients/registry/*.json                registry_store.py
  data/saga_clients/price_samples_<date>.json      （一次性抽取，见 对话全记录 T29-U64）
"""
import datetime as dt
import glob
import json
import os
import re

from common import DATA

BATCH_DATE = '2026-10-27'
TODAY = dt.date.today()


def _latest(pattern):
    fs = sorted(glob.glob(os.path.join(DATA, pattern)))
    return fs[-1] if fs else None


def _load(path):
    return json.load(open(path, encoding='utf-8')) if path and os.path.exists(path) else {}


MX = _load(_latest('mx_check_*.json'))
HOL = _load(os.path.join(DATA, 'holidays_2026-11_2027-03.json'))
PRICES = _load(_latest('price_samples_*.json'))
REG = {}
for _p in sorted(glob.glob(os.path.join(DATA, 'registry', '*.json'))):
    _d = _load(_p)
    for _c, _r in (_d.get('rows') or {}).items():
        REG[_c] = _r

MX_DATE = (MX.get('_meta') or {}).get('checked', BATCH_DATE)
MX_DOM = MX.get('domains') or {}
HOL_C = HOL.get('countries') or {}
PR_C = PRICES.get('codes') or {}

GATEWAYS = ('Proofpoint', 'Mimecast', 'Barracuda', 'MessageLabs', 'Trend Micro', 'Sophos', 'Cisco', 'FortiMail', 'Hornetsecurity')
RU_CLOUD = ('Yandex', 'Mail.ru', '俄罗斯主机商')


def _mx_implication(cls, status):
    """按邮件托管类型给一句「怎么发」——这是体检的用处，不是罗列 DNS。"""
    if status == 'nxdomain':
        return '域名已不存在（NXDOMAIN）：这个域的所有地址都退信；公司可能换了域名或关门 → 先核再发，核不到就降级'
    if status == 'dead':
        return '域名无 MX 也无 A 记录：收不了信也打不开网站 → 地址作废，降级候选'
    if status == 'no_mx':
        return '无 MX 记录：收信只能靠 A 记录兜底，多数邮件服务器不接 → 这个域的地址大概率退信，先走该户别的渠道（WhatsApp / 平台 / 别的域）'
    if status.startswith('error'):
        return 'DNS 查询超时：下次 mx_check.py 重查'
    if not cls:
        return ''
    if cls == 'Microsoft 365':
        return 'M365 对陌生发件人最严：Gmail 发过去的群发多半落「其他 / 垃圾」，Safe Links 会预取像素 → 「打开」数不可信；这户只走 1:1、首封纯文本、≤1 个链接、不带附件'
    if cls == 'Google Workspace':
        return 'Gmail → Gmail 同生态投递最稳；但 Gmail 图片代理会预抓像素 → 「已打开」偏高，别把 open 当成读过；三个发信箱别同一天给这个域发'
    if any(k in cls for k in GATEWAYS):
        return f'企业级邮件网关（{cls}）：链接重写 + 附件沙箱 → 像素失效、附件常被隔离，冷邮件到达率最低；这户靠回原线程 / LinkedIn / 对方来信，不靠新开线程群发'
    if any(k in cls for k in RU_CLOUD):
        return f'俄语区云邮箱（{cls}）：Gmail 投递正常，但制裁环境下美元汇路和 PayPal 常走不通 → 报价前先问付款银行 / 币种，T/T 以外别承诺'
    if cls in ('Zoho Mail', 'Fastmail', 'Proton Mail', 'iCloud+ 自定义域', 'Kakao / Daum 企业邮箱', 'ecount ERP 邮箱（韩国）', '韩国主机商 / Naver Works'):
        return f'中小企业云邮箱（{cls}）：过滤中等、像素一般可用；这类公司邮箱通常老板或销售本人收，信要短、带型号和一口价'
    if cls.startswith('自建'):
        return '自建邮件服务器：有自己的 IT（可能灰名单 → 首封延迟几小时才进箱），像素可用；读信的是技术人，参数先于价格'
    if cls.startswith('同域名 MX → 托管在') or any(k in cls for k in ('主机商', 'cPanel', 'IONOS', 'OVH', 'Hostinger', 'GoDaddy', 'Rackspace', 'MailChannels', 'SpamExperts', 'Etisalat', 'Yahoo', 'AWS')):
        who = cls.replace('其他主机商邮箱（', '').rstrip('）') if cls.startswith('其他主机商邮箱') else cls
        return f'主机商附带邮箱（{who}）：过滤弱、几乎不丢信，但常是老板自己收、没人代读 → 短、直接、一行型号 + 价格 + 一个问题'
    if 'Dooray' in cls or '韩国' in cls:
        return f'{cls}：韩国企业协作套件邮箱，过滤中等；韩国客户习惯先看公司介绍页再回 → 首封附 sagatele.com 一个链接即可'
    if cls.startswith('中国邮箱'):
        return f'{cls}：注册方在国内（或用国内邮箱的海外华人）→ 直接中文沟通，走国内规则（《计划》：国内单子只走私账）'
    return cls


def fmt_mx(ent):
    code = ent['code']
    doms = [d.lower() for d in (ent.get('domains') or []) if d]
    for em in (ent.get('emails') or []):
        if '@' in em:
            doms.append(em.split('@')[-1].lower())
    doms = [d for d in dict.fromkeys(doms) if d in MX_DOM]
    if not doms:
        return []
    L = [f'**邮箱域体检（DNS MX / A，{MX_DATE} 查）：**', '']
    emails = ent.get('emails') or []
    dead = set()
    for d in doms:
        r = MX_DOM.get(d)
        if not r:
            continue
        mx = '、'.join(h for _, h in r.get('mx') or [])
        st = r.get('status', '')
        cls = r.get('cls', '')
        if st in ('nxdomain', 'dead', 'no_mx', 'null_mx'):
            dead.add(d)
        head = f'- `{d}` → ' + (cls if cls else {'nxdomain': '域名不存在', 'dead': '无 MX 无 A', 'no_mx': '无 MX（只有 A 记录 ' + '/'.join(r.get('a') or []) + '）', 'null_mx': 'Null MX（明确不收信）'}.get(st, st))
        if mx:
            head += f'（MX：{mx}）'
        imp = _mx_implication(cls, st)
        L.append(head + (f'。{imp}' if imp else ''))
    bad = [e for e in emails if e.split('@')[-1].lower() in dead]
    if bad:
        L.append(f'- ⚠ 手里这些地址所在的域已收不了信：{"、".join(f"`{e}`" for e in bad)} → 作废，别再发；该户若无其他域名 / 渠道，列入降级候选')
    if len(doms) > 1 and dead and len(dead) < len(doms):
        live = [d for d in doms if d not in dead]
        L.append(f'- 其他域名仍活：{"、".join(f"`{d}`" for d in live)} → 只用这些域的地址')
    L.append('')
    return L


# ---------- 假日避让 ----------
def _window(when):
    """next_move.when → (start, end, 描述)；不动 → None。"""
    w = str(when or '')
    if not w or w.startswith('不动') or '不单独发' in w or '不主动' in w:
        return None
    if '现在' in w or '立即' in w or '本周' in w:
        return TODAY, TODAY + dt.timedelta(days=14), '现在 → 两周内'
    m = re.search(r'(\d{4})-(\d{2})(?:-(\d{2}))?', w)
    if m:
        y, mo = int(m.group(1)), int(m.group(2))
        s = dt.date(y, mo, 1)
        e = (dt.date(y + (mo == 12), mo % 12 + 1, 1) - dt.timedelta(days=1))
        if s < TODAY:
            s = TODAY
        if e < TODAY:
            return TODAY, TODAY + dt.timedelta(days=14), f'{w[:16]}（已过期 → 按两周内）'
        return s, e, f'{y}-{mo:02d}'
    if '2027-Q1' in w or '2027' in w:
        return dt.date(2027, 1, 1), dt.date(2027, 3, 31), '2027-Q1'
    return TODAY, TODAY + dt.timedelta(days=30), '群发 / 待排期 → 未来 30 天'


def fmt_holidays(ent, research):
    iso = (ent.get('iso') or '').upper()
    hc = HOL_C.get(iso)
    if not hc:
        return []
    nm = ((research or {}).get('mail_review') or {}).get('next_move') or {}
    win = _window(nm.get('when'))
    if not win:
        return [f'**假日避让：** 下一步为「{str(nm.get("when", ""))[:20] or "未排"}」，不排发信，略。', '']
    s, e, label = win
    legal = [(d, n) for d, n in hc.get('legal') or [] if s <= dt.date.fromisoformat(d) <= e]
    prac = [(ps, pe, lab, kind) for ps, pe, lab, kind in hc.get('practice') or []
            if dt.date.fromisoformat(ps) <= e and dt.date.fromisoformat(pe) >= s]
    L = [f'**假日避让（{hc.get("country", iso)} · 按下一步「{label}」窗口 {s.isoformat()}→{e.isoformat()}）：**', '']
    if legal:
        L.append('- 法定假日：' + '；'.join(f'{d[5:]} {n}' for d, n in legal) + ' —— 假日前一个工作日下午、当天、长假后第一个上午都别发')
    else:
        L.append('- 窗口内无该国法定假日')
    for ps, pe, lab, kind in prac:
        L.append(f'- 【{kind}】{ps[5:]}→{pe[5:]}：{lab}' if ps != pe else f'- 【{kind}】{ps[5:]}：{lab}')
    L.append('')
    return L


# ---------- 公司底数 ----------
def fmt_registry(ent):
    r = REG.get(ent['code'])
    if not r:
        return []
    L = [f'**公司底数（{r.get("source", "官方登记")}，{r.get("fetched", BATCH_DATE)} 查；{r.get("url", "")}）：**', '']
    L.append(f'- 法定名 / 登记号：{r.get("name", "")} · {r.get("number", "")} · 状态 **{r.get("status", "")}** · 成立 {r.get("incorporated", "")} · {r.get("company_type", "")}')
    if r.get('sic'):
        L.append('- 行业码（SIC）：' + '；'.join(r['sic']))
    if r.get('address'):
        L.append(f'- 注册地址：{r["address"]}')
    if r.get('size_band'):
        L.append(f'- 规模档：{r["size_band"]}')
    if r.get('accounts'):
        L.append(f'- 账目：{r["accounts"]}' + (f'；{r["accounts_due"]}' if r.get('accounts_due') else ''))
    for o in r.get('officers') or []:
        L.append(f'- 高管：{o}')
    if r.get('charges'):
        L.append(f'- 抵押 / 担保：{r["charges"]}')
    if r.get('prev_names'):
        L.append('- 曾用名：' + '；'.join(r['prev_names']))
    if r.get('lines'):
        L.append('- **这意味着什么：**')
        for x in r['lines']:
            L.append(f'  - {x}')
    if r.get('notes'):
        L.append(f'- 备注：{r["notes"]}')
    L.append('')
    return L


# ---------- 官网标价样本 ----------
def fmt_prices(ent):
    p = PR_C.get(ent['code'])
    if not p:
        return []
    L = [f'**官网标价样本（快照 {str(p.get("fetched_at", ""))[:10]}，同句含 switch / PoE 且带币种数字；用来估他们的零售档位，不是我们的报价依据）：**', '']
    for r in p.get('rows') or []:
        L.append(f'- {r["price"]} ← 「{r["text"][:150]}」（{r["url"]}）')
    L.append('')
    return L


def fmt_batch82(ent, research):
    if ent.get('grade') not in ('A', 'B'):
        return ''
    parts = []
    parts += fmt_mx(ent)
    parts += fmt_holidays(ent, research)
    parts += fmt_registry(ent)
    parts += fmt_prices(ent)
    if not parts:
        return ''
    head = [f'## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（{BATCH_DATE}）', '',
            '> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。', '']
    return '\n'.join(head + parts)
