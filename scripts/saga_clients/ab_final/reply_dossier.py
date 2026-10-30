#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AB-FINAL-01 · 回信档案（T29-U136 2026-10-30，Simon：A 级 = 成单客户 + 有过回信沟通的客户 为主力，再加极贴合产品线者）。

每户一份「回信档案」：三箱真人来信（A = Alan Takeout 全量 / S = Simon Takeout 全量 / E = Elsa 连接器 index_replied）
  + Simon 表内「客户回复」日志（A Replied 09.04 / S 09.08 / WhatsApp 跟进表等，经 build.py followups）
  + 成单来源（PI 包 20 户 Simon 标签；备注「成单客户 / 成样品单 / 买了…样」正则命中，需人工甄别）。
逐封分类：auto（自动回复 / 退信 / 工单确认 / 休假）/ neg（明确婉拒：not interested / no need / not our market / have supplier / unsubscribe …）
          / pos（问价 / 要资料 / 要样 / MOQ / 交期 / 认证 / 项目数量 / 约会 / OEM-SDK …）/ thin（只致谢 / 转内部 / 一句话无实质）。
户级结论 reply_class：R+（有 pos，且最后一句非硬性婉拒）/ R±（有 pos，但最后一句硬性婉拒或谈崩）/ R0（只有 thin）/ R-（只有 neg）/ auto / none。
输出：data/saga_clients/回信档案_2026-10-30.json + .csv（不改研究档）。幂等。
"""
import csv
import glob
import json
import os
import re
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-30'
OUT_JSON = os.path.join(SD, f'回信档案_{DATE}.json')
OUT_CSV = os.path.join(SD, f'回信档案_{DATE}.csv')

AUTO_FROM = re.compile(r'mailer-daemon|postmaster|noreply|no-reply|donotreply|do-not-reply|notification|bounce|autoreply|auto-reply|helpdesk|support@|ticket', re.I)
AUTO_SUBJ = re.compile(r'automatic reply|auto.?reply|autoreply|out of office|out-of-office|abwesenheit|abwesend|undeliver|delivery status|delivery failure|failure notice|mail delivery|returned mail|^read:|^lu :|gelesen|leído|otomatik yanıt|automatische antwort|réponse automatique|risposta automatica|respuesta automática|fuori sede|absence|vacation|urlaub|tatil|^accepted:|accepté|invitation|thank you for contacting|thank you for your email|your request has been|request has been logged|ticket|case #|confirmation:', re.I)
NEWSLETTER = re.compile(r'view (?:this email )?online|view online version|webversion|newsletter|unsubscribe here|manage (?:your )?(?:subscription|preferences)|privacy policy|verify the email address|your account|password|webinar|promo|sale ends|%\s*off|shop now|order confirmation|invoice #|your order has', re.I)
TICKET = re.compile(r'case number|ticket|your request|has been (?:logged|created|received)|we have received your|acknowledg|support request|will be in touch|concerns your recent', re.I)
STRONG = re.compile(r"price|quot|cost|how much|moq|minimum (?:order|quantity)|sample|data ?sheet|spec|lead ?time|delivery|certif|meeting|zoom|teams|invoice|proforma|\bpi\b|order|project|\d+\s*(?:pcs|units|pieces|sets|pc)\b|oem|odm|sdk|interested|interesting|send (?:me|us)|share|catalog|price ?list|availability|in stock|payment|t/?t\b|paypal|xtransfer|ddp|exw|fob|cif|brochure|more (?:info|information|details)|technical|manual|drawing|voltage|managed|cli|snmp|chip|requirement|looking for|do you have|can you|could you|would like", re.I)
AUTO_TEXT = re.compile(r'(?:this is an automatic|this is an automated|automated response|automatic reply|i am (?:currently )?out of (?:the )?office|i will be out of|currently out of office|away from (?:the )?office|on (?:annual |vacation |holiday |maternity |sick )?leave|siamo chiusi|we are closed|ich bin (?:bis|vom|ab)|we have received your (?:email|message|inquiry|enquiry) and|your message has been received|thank you for reaching out to us regarding|thank you for contacting us|we will get back to you|återkommer till dig|grazie per averci contattato|reacted via gmail|please make a selection|acknowledgement mail|has been created with id|no longer works|no longer with|is no longer employed|left the company|not a valid|mailbox is full|has left)', re.I)
NEG_HARD = re.compile(r"no,? but thank|no thank|not interested|no interest|not of interest|nothing of interest|unsubscribe|remove (?:me|us|our|my)|take (?:me|us) off|do not (?:contact|send|email|mail)|don'?t (?:contact|send|email|mail)|stop (?:sending|emailing|mailing)|not looking|please delete|not require|no (?:need|requirement|demand)|don'?t need|not need|not our (?:market|business|product|line|focus|area)|not (?:relevant|applicable|suitable) for us|we (?:only|just) (?:buy|use|sell|deal|work)|have our (?:own )?(?:solution|supplier|products|partner)|already have (?:a |our )?(?:supplier|partner|solution|vendor)|will have to pass|pass on your|we are not (?:a |an )?(?:interested|distributor|buyer|looking)|nicht interessiert|kein (?:interesse|bedarf)|no nos interesa|pas intéress|ilgilenmiyoruz|не интересу|не актуально|cease|spam", re.I)
NEG_SOFT = re.compile(r"too (?:expensive|high)|price is (?:really |too )?high|lost to|went with|chose another|budget|not (?:at (?:the|this) moment|now|currently|right now|this year)|maybe (?:later|in the future)|in the future|later on|keep (?:you|it) in mind|for future", re.I)
POS = re.compile(r"price|quot|cost|how much|moq|minimum (?:order|quantity)|data ?sheet|spec|sample|catalog|pricelist|price list|interested|interesting|send (?:me|us)|share|lead ?time|delivery|availability|in stock|certif|ce |fcc|rohs|meeting|call|zoom|teams|invoice|proforma|\bpi\b|order|project|\d+\s*(?:pcs|units|pieces|sets)|offer|oem|odm|sdk|firmware|cli|snmp|vlan|poe|sfp|10g|2\.5g|voltage|\bdc\b|power supply|managed|unmanaged|uplink|fiber|fibre|warranty|payment|t/?t|paypal|xtransfer|ddp|exw|fob|cif|shipping|freight|website|company (?:profile|info)|brochure|more (?:info|information|details)|detail|technical|manual|drawing|dimension|din|rack|chip|marvell|realtek|broadcom|centec|sonic|l2|l3|layer|switch", re.I)

READ_WORDS = {'read', 'opened', '已读', '看了', 'seen'}
# Simon 表内「客户回复」栏的再分类（build.py 的 reply_kind 把 Simon 自己的动作也算了）
TBL_NOT = re.compile(r'^\s*(?:\d{3,4}[:：]?\s*)?e?mail\s*发了|^\s*发了|贺卡|没看|对勾|拉黑|CC了|回复没啥内容|一直是一个勾|^\s*[—-]*\s*$', re.I)
TBL_NEG = re.compile(r'暂时没需求|暂时无需求|没需求|没有需求|不需要|no need|不用跟|买了别家|有自己的|已经有了|有了$|不做|NO BIZ|做不了|不太相关|嫌价格高|太贵|^贵$|要便宜|国内的|有统一的|在和.*合作|not now|not at this time|slow business|自己的型号|只用|only use|not interested|后续不用|不感兴趣|有需求会说|有需求时会说|稍后谈|later', re.I)
TBL_THIN = re.compile(r'^\s*(?:thanks?(?: for (?:the )?info(?:rmation)?)?|thank you|ok|okay|hi|hello|useful|有用|will check|let me check|checking|noted|yes|看了|read|点了一个赞|回复了一个表情|表情|interesting|interested|有兴趣|问我是谁|问了一个不相关的(?:东西|产品)?|问了一个别的东西|会看|收到|good|great|nice|fine|wr r u from)\s*[.!。！]*\s*$', re.I)
TBL_POS = re.compile(r'price|价格|报价|报了|catalog|目录|价格册|sample|样品|样机|测样|spec|规格|datasheet|\bds\b|info|资料|moq|quantity|数量|项目|project|型号|model|问了|要|需要|need|certif|证书|距离|poe|port|\d+\s*口|光|管理|managed|l2|l3|10g|2\.5g|sfp|oem|odm|需求|下单|order|invoice|website|profile|company|联系方式|wechat|微信|whatsapp|skype|meeting|visit|来中国|展会|bis|en50155|cli|https|multicast|stack|chip|芯片|router|pon|100g|电源|power', re.I)


# Simon 备注/兴趣栏里记录的对方动作（展会当面 / WhatsApp 聊的内容）：有明确「对方问/要/谈」动词才算实质沟通
NOTE_POS = re.compile(r'问了|要了|问价|问价格|要价格|要报价|要资料|要目录|要价格册|想测样|要样|想拿样|想下单|要下单|想买|谈了|聊了|见面|面谈|当面|展会上(?:问|说|要|谈)|WhatsApp.{0,6}(?:问|聊|谈)|主动(?:联系|问|找)|发来(?:询盘|需求|规格)|给了(?:需求|规格|数量)|报了(?:数量|需求)|需要\d+|要\d+\s*(?:台|个|套|pcs)')
NOTE_NEG = re.compile(r'没需求|没有需求|不需要|不感兴趣|不做了|拉黑|不行|不相关|已经有了|有自己的|买了别家|不回|不理')


def classify_note(text):
    t = str(text or '')
    if not t.strip():
        return ''
    if NOTE_NEG.search(t) and not NOTE_POS.search(t):
        return 'neg'
    if NOTE_POS.search(t):
        return 'pos'
    return ''


OFFLINE = re.compile(r'\bAHD\b|HDMI|\bDVR\b|\bNVR\b|camera|摄像|光猫|\bONU\b|GPON|EPON|\bOLT\b|光端机|\bSDI\b|视频光端|\bVC\b|KVM|对讲|门禁|报警|cable\b|线缆|跳线|patch cord|机柜|rack\b|UPS|电池|solar|太阳能', re.I)


def year_of(date_str):
    m = re.search(r'(20\d\d)', str(date_str or ''))
    return int(m.group(1)) if m else None


def classify_tbl(reply, content='', date=''):
    r = str(reply or '').strip()
    if not r or TBL_NOT.search(r):
        return 'not'
    y = year_of(date)
    if y and y < 2022:
        return 'not'  # Saga 之前年代（本职公司时期）的互动，不计 Saga 回信
    if OFFLINE.search(r + ' ' + str(content or '')) and not re.search(r'switch|交换机|poe|sfp|\bmc\b|光纤收发|转换器|converter|工业|industrial', r + ' ' + str(content or ''), re.I):
        return 'not'  # 问的是 Saga 产品线外的东西
    if TBL_NEG.search(r):
        return 'neg'
    if TBL_THIN.match(r):
        return 'thin'
    if TBL_POS.search(r):
        return 'pos'
    return 'thin' if len(r) < 6 else 'weak'


def classify_msg(subj, text, frm_e='', frm_n=''):
    s = subj or ''
    t = (text or '').strip()
    if AUTO_FROM.search(frm_e) or AUTO_FROM.search(frm_n) or AUTO_SUBJ.search(s) or AUTO_TEXT.search(t[:500]):
        return 'auto'
    body = t[:1200]
    if NEWSLETTER.search(body) or TICKET.search(body[:400]):
        return 'auto'
    if NEG_HARD.search(body):
        return 'neg'
    if STRONG.search(body) and len(body) >= 8:
        return 'pos'
    if POS.search(body) and len(body) >= 25:
        return 'weak'
    return 'thin'


def own_text(m):
    text = m.get('text') or ''
    qa = m.get('quote_at')
    own = text[:qa] if isinstance(qa, int) and qa > 0 else text
    own = re.sub(r'(?m)^>.*$', '', own)
    own = re.split(r'\n(?:On .{5,80}wrote:|From: |Von: |De : |-----Original Message-----|Am .{5,60}schrieb|Le .{5,60}a écrit)', own)[0]
    return re.sub(r'\s+', ' ', own).strip()


def main():
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    tbl = {r['档案编号']: r for r in csv.DictReader(open(os.path.join(SD, '客户主表.csv'), encoding='utf-8-sig'))}
    by_email, by_dom = {}, {}
    for e in ents.values():
        for m in e.get('emails') or []:
            by_email.setdefault(m.lower(), e['code'])
        for d in e.get('domains') or []:
            d = re.sub(r'（.*', '', d).lower().strip()
            if d:
                by_dom.setdefault(d, e['code'])
    free = {'gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'live.com', 'icloud.com', 'mail.ru', 'yandex.ru', 'protonmail.com'}
    msgs = defaultdict(list)
    # A / S Takeout 全量
    for box in ['gmail_a', 'gmail_s']:
        for f in sorted(glob.glob(os.path.join(ROOT, 'data', box, 'messages', '*', '*.jsonl'))):
            for line in open(f, encoding='utf-8'):
                m = json.loads(line)
                if m.get('dir') != 'in' or not m.get('client'):
                    continue
                fr = m.get('from') or {}
                own = own_text(m)
                cls = classify_msg(m.get('subj'), own, (fr.get('e') or '').lower(), fr.get('n') or '')
                if m.get('bulk') and not re.match(r'^\s*(re|aw|sv|fw|fwd|tr|wg|odp|回复|答复|轉寄|转发)\s*:', m.get('subj') or '', re.I):
                    cls = 'auto'
                if cls != 'auto' and NEG_SOFT.search(own[:1200]) and cls != 'neg':
                    soft = True
                else:
                    soft = False
                for c in m['client']:
                    if c in ents:
                        msgs[c].append({'box': box[-1].upper(), 'k': m['k'], 'date': m['date'][:10], 'from': (fr.get('e') or '').lower(), 'subj': (m.get('subj') or '')[:100], 'cls': cls, 'soft_neg': soft, 'bulk': bool(m.get('bulk')), 'excerpt': own[:300], 'att': [a.get('n') for a in (m.get('att') or [])][:3]})
    # E 连接器 index_replied
    texts = {f[:-5]: f for f in os.listdir(os.path.join(ROOT, 'data', 'gmail_e', 'text'))}
    for line in open(os.path.join(ROOT, 'data', 'gmail_e', 'index_replied.jsonl'), encoding='utf-8'):
        m = json.loads(line)
        fr = m['from']
        em = re.search(r'<([^>]+)>', fr)
        em = (em.group(1) if em else fr).lower().strip()
        if 'sagatelecom' in em or 'mailer-daemon' in em or 'postmaster' in em:
            continue
        code = by_email.get(em)
        if not code:
            dom = em.split('@')[-1]
            if dom not in free:
                code = by_dom.get(dom)
        if not code:
            continue
        t = ''
        if m['id'] in texts:
            j = json.load(open(os.path.join(ROOT, 'data', 'gmail_e', 'text', texts[m['id']]), encoding='utf-8'))
            t = re.sub(r'\s+', ' ', (j.get('text') or '')).strip()
            t = re.split(r'(?:On .{5,80}wrote:|From: |-----Original Message-----)', t)[0]
        dm = re.search(r'(\d{1,2}) (\w{3}) (\d{4})', m['date'])
        mon = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        d_iso = f"{dm.group(3)}-{mon.get(dm.group(2), '01')}-{int(dm.group(1)):02d}" if dm else m['date'][:10]
        cls = classify_msg(m['subject'], t, em, '')
        msgs[code].append({'box': 'E', 'k': m['id'], 'date': d_iso, 'from': em, 'subj': m['subject'][:100], 'cls': cls, 'soft_neg': bool(NEG_SOFT.search(t[:1200])), 'bulk': False, 'excerpt': t[:300], 'att': []})
    out = {}
    codes = set(msgs) | {c for c, e in ents.items() if e.get('reply_sub') or e.get('reply_neg') or e.get('pi') or tbl[c]['成交'] == '是' or tbl[c].get('备注提及成交(非Saga)') == '是'
                         or classify_note(' '.join([str(x) for x in (e.get('interests') or [])] + [str(x) for x in (e.get('remarks') or [])]))}
    for c in sorted(codes):
        e = ents[c]
        L = sorted(msgs.get(c, []), key=lambda r: r['date'])
        human = [r for r in L if r['cls'] != 'auto']
        fu = []
        for f in e.get('followups') or []:
            if f.get('reply'):
                k = classify_tbl(f.get('reply'), f.get('content'), f.get('date'))
                if k == 'not':
                    continue
                fu.append({'date': f.get('date', ''), 'content': str(f.get('content', ''))[:40], 'reply': str(f.get('reply', ''))[:80], 'kind': k})
        # Simon 备注/兴趣（展会当面 / WhatsApp 聊过的内容）
        note_txt = ' ； '.join([str(x) for x in (e.get('interests') or [])] + [str(x) for x in (e.get('remarks') or [])])
        nk = classify_note(note_txt)
        yrs = [str(y) for y in (e.get('years') or []) if str(y).isdigit()]
        ny = max(yrs) if yrs else ''
        if nk and not (ny and int(ny) < 2022) and not (OFFLINE.search(note_txt) and not re.search(r'switch|交换机|poe|sfp|\bmc\b|光纤收发|转换器|converter|工业|industrial|2\.5G|10G', note_txt, re.I)):
            fu.append({'date': ny, 'content': 'Simon 备注/兴趣栏', 'reply': note_txt[:80], 'kind': nk})
        signals = [r['cls'] for r in human] + [f['kind'] for f in fu]
        last = human[-1]['cls'] if human else (signals[-1] if signals else '')
        if 'pos' in signals:
            rc = 'R±' if last == 'neg' else 'R+'
        elif 'weak' in signals:
            rc = 'R±' if last == 'neg' else 'Rw'
        elif 'neg' in signals:
            rc = 'R-'
        elif signals:
            rc = 'R0'
        elif L:
            rc = 'auto'
        else:
            rc = 'none'
        out[c] = {'code': c, 'name': e.get('name'), 'country': e.get('country'), 'grade_now': e.get('grade'), 'pi': (e.get('pi') or {}).get('simon', '') if e.get('pi') else '', 'deal_flag': tbl[c]['成交'] == '是',
                  'n_in_human': len(human), 'n_in_auto': len(L) - len(human), 'n_pos': signals.count('pos'), 'n_neg': signals.count('neg'), 'n_tbl_reply': len(fu),
                  'first': human[0]['date'] if human else '', 'last': human[-1]['date'] if human else '', 'last_cls': last, 'soft_neg': any(r.get('soft_neg') for r in human), 'reply_class': rc,
                  'boxes': ''.join(sorted({r['box'] for r in human})), 'msgs': L, 'tbl_replies': fu}
    json.dump(out, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    with open(OUT_CSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['编号', '公司', '国家', '现等级', 'PI标签', '成交标记', '真人来信', '自动回复', 'pos', 'neg', '表内回复', '首次', '最近', '最后一句', '软婉拒', '回信结论', '邮箱', '最近三句'])
        for c, o in out.items():
            hm = [r for r in o['msgs'] if r['cls'] != 'auto'][-3:]
            w.writerow([c, o['name'], o['country'], o['grade_now'], o['pi'], '是' if o['deal_flag'] else '', o['n_in_human'], o['n_in_auto'], o['n_pos'], o['n_neg'], o['n_tbl_reply'], o['first'], o['last'], o['last_cls'], '是' if o['soft_neg'] else '', o['reply_class'], o['boxes'],
                        ' ‖ '.join(f"[{r['box']} {r['date']} {r['cls']}] {r['excerpt'][:160]}" for r in hm)])
    from collections import Counter
    print('households', len(out), Counter(o['reply_class'] for o in out.values()))
    print('by grade', Counter((o['grade_now'], o['reply_class']) for o in out.values()))


if __name__ == '__main__':
    main()
