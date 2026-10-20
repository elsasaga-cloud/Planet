#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render.py — 由主表 CSV + batch/*.json 渲染 profile/A|B|C/<编号>-<公司>-<国家>.md（v2 骨架）。
不要手改档案；改 JSON 后重跑。A 类全骨架；B/C 精简骨架（同节名、少段落）。
用法：python scripts/render.py [PA-001 ...]
"""
import datetime, json, os, re, shutil, sys
from common import read_csv, load_batches, load_prices, price_line, PROFILE_DIR, ROOT

TODAY = datetime.date.today().isoformat()
STRUCT_VER = "v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）"

RED_LINES = """**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**：PLANET 本身与其关联公司只是信号源；对 PLANET 渠道不贬低 PLANET，只谈「第二货源 / 贴牌 / 功能定制」。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据；Saga 商用线 **无 802.3bt**，不要对标 PLANET 的 bt/UPoE 型号。
4. 不承诺 UL、EN50155、IP67、云管理——Saga 没有。
5. 样机先送测，再谈价格；大集团先问清采购层级。

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。"""


def safe_name(s):
    return re.sub(r'[\\/:*?"<>|]+', " ", s).strip()


def gather(code):
    """从所有批次收集该编号客户的 JSON 记录（按加载顺序合并，不覆盖已有键，列表追加）。"""
    merged = {}
    for path, b in load_batches():
        for c in b.get("customers", []):
            if c.get("_code") == code:
                for k, v in c.items():
                    if k not in merged:
                        merged[k] = v
                    elif isinstance(v, list) and isinstance(merged[k], list):
                        merged[k] = merged[k] + [x for x in v if x not in merged[k]]
                merged.setdefault("_batches", []).append(os.path.basename(path))
    return merged


def email_template(row, c, p1, price_str):
    name = (c.get("contacts") or [{}])[0].get("name") or ""
    # 占位联系人（「—（销售）」等）不是人名：问候语退回 there，避免把占位符抄进邮件
    first = name.split()[0] if name and not name.startswith("—") else "there"
    t = row["类型"]
    company = row["公司名"]
    country = row["国家"]
    q = c.get("first_question") or "Which PoE switch model do you sell most often today, and roughly how many units a year?"
    hook = c.get("hook") or f"You carry PLANET PoE switches in {country}, so your customers already accept Taiwan-grade pricing and lead times."
    if "分销" in t or "电商" in t:
        body = f"""Hi {first},

{hook}

We build Marvell-based L2+ PoE switches (ERPS <20 ms ring, IGMP snooping, 802.1Q/QinQ, PoE watchdog, CLI/SNMP) that fit the same slot as the PLANET GS-4210/GS-5220 class at a lower landed cost, and we can ship under your own label with neutral packaging. The unit I would start with for your line is {p1} at {price_str}.

One question: {q}

If useful, I can send one unit to your office for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)"""
    elif "集成" in t or "方案" in t or "安防" in t or "自动化" in t:
        body = f"""Hi {first},

{hook}

We supply Marvell-based managed PoE switches (L2+/L3, ERPS ring <20 ms, PoE watchdog that power-cycles a hung camera or AP, full CLI/SNMP/MIB) that drop in where a PLANET GS-4210/IGS-5225 class unit would sit, and we can customise the web UI or firmware features for a project. The unit I would start with for your sites is {p1} at {price_str}.

One question: {q}

If it helps, I can ship one unit for a 30-day test on a live site. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)"""
    else:
        body = f"""Hi {first},

{hook}

We build Marvell-based managed PoE and industrial switches (L2+/L3, ERPS <20 ms, PoE watchdog, CLI/SNMP) and ship under the customer's own label with neutral packaging and 3-year warranty on the industrial line. The unit I would start with is {p1} at {price_str}.

One question: {q}

Happy to send one unit for a 30-day test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)"""
    subj = c.get("subject") or f"Second-source PoE switch for your {('PLANET line' if ('分销' in t or '电商' in t) else 'PoE projects')}"
    return subj, body


def render_one(row, by_saga, by_sb):
    code = row["档案编号"]
    grade = row["评级"]
    c = gather(code)
    p1 = row["首推Saga型号"] or c.get("p1", "")
    tier = float(c.get("tier") or (0.20 if ("分销" in row["类型"] or "电商" in row["类型"]) else 0.25))
    price_str, prow = price_line(p1, tier, by_saga, by_sb) if p1 else ("（未定 P1）", None)
    contacts = c.get("contacts") or []
    evidence = c.get("evidence") or []
    L = []
    L.append(f"# {row['公司名']}\n")
    L.append(f"> **评级 {grade}**　|　{row['国家']} · {row['城市'] or '—'}　|　档案编号 `{code}`　|　优先级 {row['优先级'] or '—'}　|　状态：{row['状态']}")
    L.append(f">")
    L.append(f"> **类型**：{row['类型']}　|　**PLANET 关联**：{row['信号（在卖什么品牌）']}　|　结构版本：{STRUCT_VER}")
    if row.get("Mikrotik仓库对照编号"):
        L.append(f">")
        L.append(f"> ⚠️ **Mikrotik 仓库已有档案 {row['Mikrotik仓库对照编号']}**：本档只补 PLANET 侧证据；联系策略以先建档案为准，勿重复首触。")
    L.append("")
    L.append("```yaml structured_profile")
    L.append(f"code: {code}\nrating: {grade}\ncountry: {row['国家']}\ntype: {row['类型']}\nplanet_models: {json.dumps(c.get('planet_models', []), ensure_ascii=False)}\n"
             f"p1: {p1}\nprice_tier: {int(tier*100)}%\nstage: {row['状态']}\nmikrotik_ref: {row.get('Mikrotik仓库对照编号','') or 'none'}\nupdated: {TODAY}")
    L.append("```\n")
    # SALES BRIEF
    L.append("## SALES BRIEF（压缩模型）\n")
    L.append(f"- **是谁**：{c.get('who') or row['类型'] + '；' + row['信号（在卖什么品牌）']}")
    L.append(f"- **为什么值得跟**：{row['评级依据']}")
    L.append(f"- **P1（首触唯一主推）**：{p1 or '待定'} — {c.get('p1_reason','按其在卖的 PLANET 型号对位')}；{price_str}")
    L.append(f"- **第一问（只问一个）**：{c.get('first_question','Which PoE switch model do you sell most often today, and roughly how many units a year?')}")
    L.append(f"- **最大未知**：{c.get('biggest_unknown','采购决策人与年用量未确认；现用 PLANET 型号的毛利与断货痛点未确认')}")
    L.append(f"- **下一步**：{c.get('next_step','未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档')}\n")
    # 基本事实
    L.append("## 基本事实（事实/推断/假设分层）\n")
    L.append("| 项 | 内容 | 层级 |\n|---|---|---|")
    L.append(f"| 名称 | {row['公司名']} | 事实（网页自述） |")
    L.append(f"| 国家/城市 | {row['国家']} / {row['城市'] or '待补证'} | 事实 |")
    L.append(f"| 网站 | {row['网站']} | 事实 |")
    L.append(f"| 类型 | {row['类型']} | {'事实（厂商/官网口径）' if evidence else '推断'} |")
    L.append(f"| PLANET 关联 | {row['信号（在卖什么品牌）']} | 事实（见下节证据） |")
    L.append(f"| 自有品牌 | {row['是否自有品牌']} | {'事实' if row['是否自有品牌'] in ('是','否') else '待补证'} |")
    for k, v in (c.get("facts") or {}).items():
        L.append(f"| {k} | {v} | {'【推断】' if '推断' in str(v) else '事实/自述'} |")
    L.append("")
    # PLANET 关联证据
    L.append("## PLANET 关联证据（原文 + URL + 抓取日期）\n")
    if evidence:
        for e in evidence:
            L.append(f"- **【{e.get('level','来源')}】{e.get('claim','')}**")
            if e.get("quote"):
                L.append(f"  > {e['quote']}")
            L.append(f"  > 来源：{e.get('url','')}（抓取 {e.get('date', TODAY)}）")
    else:
        L.append("- 待补证")
    L.append("")
    # 在卖 PLANET 型号 → Saga 对位
    L.append("## 在卖/在用 PLANET 型号 → Saga 对位\n")
    pm = c.get("planet_models") or []
    if pm:
        L.append("| PLANET 型号（证据所见） | Saga 对位 | 说明 |\n|---|---|---|")
        for m in pm:
            mp = c.get("model_map", {}).get(m, {})
            L.append(f"| {m} | {mp.get('saga', p1 or '—')} | {mp.get('note','同口数/同上联近似对位，非功能等价')} |")
    else:
        L.append("- 证据页未列具体型号（只到品牌级）；首触后再问。")
    L.append("")
    # 需求与场景
    L.append("## 需求与场景（推断标签）\n")
    L.append(f"- {c.get('needs','PoE 接入供电（安防/AP）；' + ('工业/宽温 DIN；' if '工业' in row['类型'] or 'IGS' in ' '.join(pm) else '') + '万兆上行')}（【推断】依据在卖品类）\n")
    # 联系方式
    L.append("## 联系方式（已有/猜测分标）\n")
    if contacts:
        for k in contacts:
            L.append(f"- **{k.get('name') or '（未具名）'}**{('（' + k['role'] + '）') if k.get('role') else ''}："
                     f"{k.get('email','') or '—'}{(' / ' + k['phone']) if k.get('phone') else ''} 〔{k.get('status','公开')}；源：{k.get('source','')}〕")
    else:
        L.append(f"- 入口：{row['入口/联系方式'] or '待补证'}")
    L.append(f"- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：{c.get('mx','未查')}。\n")
    # KP 表（A 类）
    if grade == "A":
        L.append("## 关键人（KP）与触达通道\n")
        L.append("| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |\n|---|---|---|---|---|")
        for k in contacts or [{}]:
            L.append(f"| {k.get('name','—')} | {k.get('role','—')} | {k.get('email','') or '—'}{(' / ' + k['phone']) if k.get('phone') else ''} | {k.get('status','公开')} | {k.get('source','')} |")
        L.append("")
    # 跟进步骤
    steps = c.get("steps") or []
    L.append("## 跟进步骤（最多 3 次 · 成功/退出标准）\n")
    L.append(f"> 每次只推进一个台阶、只问一个问题；全程只推 P1（{p1}），备选型不进邮件。\n")
    if steps:
        for i, s in enumerate(steps, 1):
            L.append(f"### 第 {i} 次跟进 · {s.get('title','')}\n")
            L.append(f"- **推什么**：{s.get('push', p1)}")
            L.append(f"- **切入点**：{s.get('angle','')}")
            L.append(f"- **要问的问题**：{s.get('question','')}")
            L.append(f"- **随附/动作**：{s.get('action','')}\n")
    else:
        L.append(f"### 第 1 次跟进 · 第二货源/贴牌试探\n\n- **推什么**：{p1}\n- **切入点**：{row['切入点']}\n- **要问的问题**：{c.get('first_question','Which PoE switch model do you sell most often today, and roughly how many units a year?')}\n- **随附/动作**：无附件；规格页链接一条\n")
        L.append(f"### 第 2 次跟进 · 样机\n\n- **推什么**：{p1}（1 台）\n- **切入点**：30 天并行测试，不要求承诺\n- **要问的问题**：Which site/customer would you test it on?\n- **随附/动作**：L2+ 特性表 1 页（ERPS/QinQ/IGMP/PoE watchdog）\n")
        L.append(f"### 第 3 次跟进 · 贴牌与批量\n\n- **推什么**：{p1} + 贴牌方案\n- **切入点**：中性包装、客户型号、固件 UI 定制\n- **要问的问题**：What MOQ and label format would make sense for a first run?\n- **随附/动作**：贴牌流程 1 页；报价前核价\n")
    # 产品决策
    L.append("## 产品决策（Saga · 单一决策口径）\n")
    L.append("| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |\n|---|---|---|---|---|")
    L.append(f"| **P1（首触唯一）** | {p1 or '待定'} | 主场景 | {price_str} | {c.get('p1_reason','按其在卖的 PLANET 型号对位')}；档位 {int(tier*100)}%：{c.get('tier_reason', '分销/电商走量' if tier==0.20 else ('集成/项目型' if tier==0.25 else 'OEM/定制或小批量技术型'))} |")
    for i, alt in enumerate(c.get("alts") or [], 2):
        ps, _ = price_line(alt.get("model",""), tier, by_saga, by_sb)
        L.append(f"| 备选{i} | {alt.get('model','')} | {alt.get('scene','升级/延展')} | {ps} | {alt.get('reason','P1 过后的台阶，不进首触邮件')} |")
    if prow is not None and prow["Saga对应型号"].startswith("（"):
        L.append(f"\n- ⚠️ **型号口径**：Saga 暂无对应型号，本档沿用 SmartByte 型号 **{prow['SmartByte型号']}**（用户规则 PR-01-05）。")
    L.append(f"\n- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率（`docs/rules/报价与型号规则.md`）；Saga 商用线无 802.3bt、无 LCD、无云管理——不对标 PLANET 的 UPoE/LCD/NMS 型号。\n")
    # SWOT / 红线 / Qualification / Unknowns
    sw = c.get("swot") or {}
    L.append("## SWOT\n")
    L.append(f"- **S**：{sw.get('S','已在卖台系 PoE 交换机，接受亚洲供货与价位；Saga 可贴牌+功能定制')}")
    L.append(f"- **W**：{sw.get('W','Saga 为贸易商、官网弱、无 UL/bt；需以样机与规格说话')}")
    L.append(f"- **O**：{sw.get('O','PLANET 断货/涨价/型号停产时的第二货源；自有品牌贴牌')}")
    L.append(f"- **T**：{sw.get('T','对 PLANET 忠诚度高；深圳同行低价竞争')}\n")
    L.append("## 触达与风险红线\n")
    L.append(RED_LINES)
    if c.get("boundary"):
        L.append(f"\n**本户特别红线**：{c['boundary']}")
    L.append("")
    L.append("## Qualification 清单\n")
    L.append("| 门槛 | 状态 |\n|---|---|")
    L.append(f"| 需求面成立（在卖/在用 PoE 交换机） | {'✅' if evidence else '❓'} |")
    L.append(f"| 决策人识别 | {'✅' if any(k.get('name') for k in contacts) else '❓ 未具名'} |")
    L.append(f"| 触达通道 | {'✅ 有公开邮箱' if any(k.get('email') for k in contacts) or '@' in row['入口/联系方式'] else '❓ 仅表单/电话'} |")
    L.append("| 现用交换品牌 | ✅ PLANET（证据所见） |")
    L.append("| 采购量/预算 | ❓ 未确认 |")
    L.append(f"| 商业资格结论 | **{c.get('qual','技术上合格 / 商业上未合格（待首触信号）')}** |\n")
    L.append("## Unknowns（待问清单 · 首触后逐项消除）\n")
    for u in c.get("unknowns") or ["年用量与最常出的 PLANET 型号", "是否接受贴牌/第二货源", "采购决策人与付款口径", "对 bt/LCD/云管理等 Saga 缺口的依赖程度"]:
        L.append(f"- [ ] {u}")
    L.append("")
    # 首触邮件
    mref = row.get("Mikrotik仓库对照编号", "") or ""
    via_mikrotik = "首触以 Mikrotik 仓库为准" in (row.get("备注", "") or "")
    if grade in ("A", "B") and via_mikrotik:
        # 并档户：首触由 Mikrotik 仓库发，本仓不生成可发送邮件，避免同一客户被两仓各发一封
        L.append("## 首触邮件：本仓不发（Mikrotik 同户并档）\n")
        L.append(f"> 本户 = Mikrotik 仓库 **{mref}**，按《客户分级与去重规则》§4 与 T06 裁决，首触只发一次、以 Mikrotik 仓库为准。本档只提供 PLANET 侧证据与对位（P1 {p1}，{price_str}）。Mikrotik 侧首触有回复且涉及 PLANET 线时，再据本档补一封对位邮件；届时话术另写，不用通用样板。\n")
    elif grade in ("A", "B"):
        subj, body = email_template(row, c, p1, price_str.split("（")[0].strip() + " (price snapshot 2026-10-17, valid 15 days)")
        L.append("## 首触邮件（英文样板 · 可直接发送）\n")
        if mref:
            L.append(f"> ⚠ Mikrotik 同户 **{mref}**：首触只发一次。发出前先核对 Mikrotik 仓库该行状态（已触达/退信/回复），避免两仓各发一封。\n")
        L.append(f"**主题**：{subj}\n")
        L.append("```text\n" + body + "\n```\n")
        L.append("> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标；③ 落款换成你自己的名字与公司；④ **一次只问一个问题**；⑤ 货币 USD 并带快照日期；⑥ 分销商勿贬低 PLANET，只谈第二货源/贴牌。\n")
    # 跟进记录 / 复核
    L.append("## 跟进记录\n")
    L.append("| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |\n|---|---|---|---|---|---|---|\n|  |  |  |  |  |  |  |\n")
    L.append("> 首次触达前留空；用户在仓库外发出邮件后告诉我日期与渠道，我来更新本档并重评 stage。\n")
    L.append("## 下次复核\n")
    L.append("- 首触发出后 **14 天**无回复 → 复核是否降频；有任何回复 → 当即重评 stage 与评级。")
    L.append("- 报价纪律：价格为 USD EXW 快照（汇率 2026-10-17），过窗先核价再报价。\n")
    L.append("---\n")
    L.append(f"*建档日期：{row['入库日期']}　|　入库批次：{row['入库批次']}　|　原始证据：{', '.join('batch/'+b for b in c.get('_batches', []))}　|　渲染：scripts/render.py {TODAY}*")
    return "\n".join(L) + "\n"


def main():
    only = set(sys.argv[1:])
    rows = read_csv()
    by_saga, by_sb = load_prices()
    # 清理旧文件（同编号可能换目录/改名）
    existing = {}
    for g in "ABC":
        d = os.path.join(PROFILE_DIR, g)
        os.makedirs(d, exist_ok=True)
        for fn in os.listdir(d):
            m = re.match(r"^(P[ABC]-\d{3})-", fn)
            if m:
                existing.setdefault(m.group(1), []).append(os.path.join(d, fn))
    n = 0
    for r in rows:
        code = r["档案编号"]
        if only and code not in only:
            continue
        if r["状态"].startswith("并入"):
            continue
        grade = (r.get("人工定级") or r["评级"]).strip()[:1]
        fn = f"{code}-{safe_name(r['公司名'])}-{r['国家']}.md"
        path = os.path.join(PROFILE_DIR, grade, fn)
        for old in existing.get(code, []):
            if os.path.abspath(old) != os.path.abspath(path) and os.path.exists(old):
                os.remove(old)
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_one(r, by_saga, by_sb))
        n += 1
    # 索引
    idx = ["# 客户档案索引（自动生成）\n", f"更新：{TODAY}\n", "| 编号 | 公司 | 国家 | 类型 | 评级 | 状态 | PLANET 关联 |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["状态"].startswith("并入"):
            continue
        g = (r.get("人工定级") or r["评级"]).strip()[:1]
        fn = f"{r['档案编号']}-{safe_name(r['公司名'])}-{r['国家']}.md"
        idx.append(f"| [{r['档案编号']}]({g}/{fn}) | {r['公司名']} | {r['国家']} | {r['类型']} | {r['评级']} | {r['状态']} | {r['信号（在卖什么品牌）'][:60]} |")
    with open(os.path.join(PROFILE_DIR, "00-索引.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(idx) + "\n")
    print(f"rendered {n} profiles")


if __name__ == "__main__":
    main()
