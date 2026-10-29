#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A / B 判定工作台 HTML（T29-U126，2026-10-29）—— 给 Simon 一个能点的页面：选口径 → 看名单 → 勾例外 → 导出裁定。

输入：data/saga_clients/AB新标准_模拟_2026-10-29.csv（ab_standard_sim.py 产物，1,229 行）
     data/saga_clients/entities.json（补 situation 一句话 / 域名 / 邮件绑定头）
     Saga Clients/A|B/**/*.md（档案文件名 → GitHub 链接）
输出：docs/AB判定_工作台_2026-10-29.html（单文件，离线可开，数据内嵌；裁定存浏览器 localStorage，导出为文本 / CSV）
用法：python3 scripts/saga_clients/ab_judge_html.py
"""
import csv
import glob
import html
import json
import os
import re
import subprocess
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
SIM = os.path.join(DATA, 'AB新标准_模拟_2026-10-29.csv')
OUT = os.path.join(ROOT, 'docs', 'AB判定_工作台_2026-10-29.html')
GH = 'https://github.com/elsasaga-cloud/Planet/blob/arena/3f35b9b3-planet/'


def md_links():
    m = {}
    for p in glob.glob(os.path.join(ROOT, 'Saga Clients', '*', '**', '*.md'), recursive=True):
        fn = os.path.basename(p)
        mm = re.match(r'^(S[ABC]-\d+)-', fn)
        if mm and not fn.startswith('_'):
            rel = os.path.relpath(p, ROOT)
            m[mm.group(1)] = GH + '/'.join(urllib.parse.quote(x) for x in rel.split(os.sep))
    return m


def main():
    now = subprocess.check_output(['date', '-u', '+%Y-%m-%d %H:%MZ']).decode().strip()
    ents = {e['code']: e for e in json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))}
    links = md_links()
    rows = []
    for r in csv.DictReader(open(SIM, encoding='utf-8-sig')):
        e = ents[r['编号']]
        mr = (e.get('research') or {}).get('mail_review') or {}
        sit = re.sub(r'\s+', ' ', (mr.get('situation') or '')).strip()
        rows.append({
            'c': r['编号'], 'n': r['公司'], 'k': r['国家'], 'g': r['区域组'], 'cur': r['现等级'],
            's': r['建议-严'], 'w': r['建议-宽'], 'kc': r['建议-宽留冷'],
            'hs': r['命中-严'], 'hw': r['命中-宽'], 'hk': r['命中-宽留冷'],
            'deal': r['成单'], 'smp': r['样品'], 'pi': r['PI'], 'rep': r['真回次数'], 'op': r['打开'], 'wa': r['WA'], 'fair': r['展会'],
            'bind': r['绑定'], 'fit': r['对位'], 'own': r['自有品牌'], 'reg': r['登记'], 'emp': r['体量(人)'], 'last': r['最近往来'],
            'st': r['表内状态'], 'flag': r['红旗'], 'pool': r['现池位'], 'conc': r['预演结论'],
            'dom': ((e.get('domains') or [''])[0]) or '', 'sit': sit[:260] + ('…' if len(sit) > 260 else ''),
            'url': links.get(r['编号'], ''),
        })
    data_json = json.dumps(rows, ensure_ascii=False).replace('</', '<\\/')
    n_a = sum(1 for x in rows if x['cur'] == 'A')
    n_b = len(rows) - n_a
    page = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A / B 判定工作台 · 2026-10-29</title>
<style>
  :root{--ink:#1d2430;--mute:#6b7380;--line:#e3e6ea;--bg:#f7f8f9;--acc:#0b5fa5;--warn:#9a5b00;--ok:#1b7f3b;--bad:#a12a2a;--a:#1b7f3b;--b:#0b5fa5;--c:#8a8f98}
  *{box-sizing:border-box}
  body{margin:0;font-family:-apple-system,"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",Helvetica,Arial,sans-serif;color:var(--ink);background:#fff;line-height:1.55;font-size:14px}
  header{background:var(--ink);color:#fff;padding:22px 32px}
  header h1{margin:0 0 4px;font-size:22px;font-weight:600}
  header p{margin:0;color:#c7ccd4;font-size:13px}
  main{max-width:1500px;margin:0 auto;padding:18px 24px 60px}
  .steps{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:0 0 16px}
  .step{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:12px 14px}
  .step b{display:block;font-size:15px;margin-bottom:4px}
  .step small{color:var(--mute)}
  .profiles{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 4px}
  .prof{border:2px solid var(--line);border-radius:8px;padding:8px 14px;cursor:pointer;background:#fff;min-width:200px;text-align:left}
  .prof.on{border-color:var(--acc);background:#eef5fc}
  .prof b{display:block;font-size:15px}
  .prof span{color:var(--mute);font-size:12.5px}
  .cards{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0}
  .card{border:1px solid var(--line);border-radius:8px;padding:8px 14px;min-width:120px;background:#fff}
  .card .v{font-size:22px;font-weight:600}
  .card .l{color:var(--mute);font-size:12px}
  .bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:10px 0;padding:10px;background:var(--bg);border:1px solid var(--line);border-radius:8px}
  .bar select,.bar input{padding:5px 8px;border:1px solid var(--line);border-radius:6px;font-size:13px;background:#fff}
  .bar input[type=text]{min-width:220px}
  .bar label{font-size:12.5px;color:var(--mute)}
  .chip{display:inline-block;padding:2px 8px;border-radius:10px;font-size:12px;border:1px solid var(--line);background:#fff;cursor:pointer;user-select:none}
  .chip.on{background:var(--acc);color:#fff;border-color:var(--acc)}
  table{border-collapse:collapse;width:100%;font-size:12.8px}
  th,td{border:1px solid var(--line);padding:5px 7px;vertical-align:top;text-align:left}
  th{background:var(--bg);font-weight:600;position:sticky;top:0;z-index:2;cursor:pointer;white-space:nowrap}
  td.ev{white-space:nowrap}
  .g{display:inline-block;min-width:20px;text-align:center;border-radius:4px;padding:0 5px;font-weight:600;color:#fff}
  .gA{background:var(--a)}.gB{background:var(--b)}.gC{background:var(--c)}
  .up{color:var(--ok);font-weight:600}.down{color:var(--bad);font-weight:600}.same{color:var(--mute)}
  .dec button{border:1px solid var(--line);background:#fff;border-radius:5px;padding:2px 7px;margin:0 2px 2px 0;cursor:pointer;font-size:12px}
  .dec button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
  tr.decided td{background:#fffbe6}
  .sit{color:#3b4350;font-size:12.2px;max-width:420px}
  .mute{color:var(--mute)}
  .muted-row td{opacity:.75}
  .exp{margin-top:18px;border:1px solid var(--line);border-radius:8px;padding:12px 14px;background:var(--bg)}
  textarea{width:100%;min-height:110px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;border:1px solid var(--line);border-radius:6px;padding:8px}
  .btn{display:inline-block;border:1px solid var(--acc);color:#fff;background:var(--acc);border-radius:6px;padding:6px 14px;cursor:pointer;font-size:13px;margin-right:8px}
  .btn.sec{background:#fff;color:var(--acc)}
  details{margin:14px 0}
  summary{cursor:pointer;color:var(--acc)}
  .legend table{font-size:12.5px;width:auto}
  a{color:var(--acc);text-decoration:none}
  .cnt{font-size:12.5px;color:var(--mute);margin:6px 0}
  .hide{display:none}
</style>
</head>
<body>
<header>
  <h1>A / B 判定工作台 · 2026-10-29</h1>
  <p>Saga A 90 + B 1,139 = 1,229 户逐户证据 + 三档口径建议。生成 __NOW__ · 数据 `data/saga_clients/AB新标准_模拟_2026-10-29.csv` · 规则说明 `docs/AB判定_新标准_讨论稿_2026-10-29.md`。离线单文件；你的裁定存在本浏览器里，关了再开还在。</p>
</header>
<main>
  <div class="steps">
    <div class="step"><b>第 1 步 · 选口径</b>点下面三个按钮之一，表里「建议」列和上面数字跟着变。<br><small>懒人版：只回我一句「口径=宽留冷」就完事，名单按口径整批执行。</small></div>
    <div class="step"><b>第 2 步 · 看名单、勾例外</b>默认只显示「要变的」（升 / 降）。不同意哪户，点行尾 <b>A / B / C / 不动</b>。每行有公司档案链接（GitHub）和一句话情况。<br><small>不点 = 同意建议。</small></div>
    <div class="step"><b>第 3 步 · 导出给我</b>拉到最底「导出裁定」→ 复制文本粘到聊天里（或下载 CSV）。我按它改等级、重渲染、更新 P 池标签。<br><small>等级改动都可回滚。</small></div>
  </div>

  <div class="profiles" id="profiles"></div>
  <div class="cards" id="cards"></div>

  <div class="bar">
    <label>变化</label>
    <span class="chip on" data-f="chg" data-v="变">只看要变的</span>
    <span class="chip" data-f="chg" data-v="升">升</span>
    <span class="chip" data-f="chg" data-v="降">降</span>
    <span class="chip" data-f="chg" data-v="不变">不变</span>
    <span class="chip" data-f="chg" data-v="全部">全部</span>
    <label style="margin-left:10px">现等级</label>
    <select id="fCur"><option value="">全部</option><option>A</option><option>B</option></select>
    <label>区域</label>
    <select id="fGrp"><option value="">全部</option></select>
    <label>现池位</label>
    <select id="fPool"><option value="">全部</option></select>
    <label>证据</label>
    <select id="fEv"><option value="">全部</option><option value="deal">有成单 / 样品 / PI</option><option value="rep">真回 ≥1</option><option value="rep3">真回 ≥3</option><option value="wa">WA 已加</option><option value="own">自有品牌</option><option value="cold">0 真回 无 WA</option></select>
    <input type="text" id="fQ" placeholder="搜 编号 / 公司 / 国家 / 域名 / 情况">
    <span class="chip" id="fDec">只看已裁定</span>
    <span class="chip" id="reset">清空筛选</span>
  </div>
  <div class="cnt" id="cnt"></div>
  <div style="overflow:auto;max-height:78vh;border:1px solid var(--line)">
  <table id="tbl">
    <thead><tr>
      <th data-k="c">编号</th><th data-k="n">公司</th><th data-k="k">国家 / 区域</th><th data-k="cur">现</th><th data-k="prop">建议</th><th data-k="chg">变化</th>
      <th>证据（成单·样品·PI | 真回·打开·WA·展会 | 自牌·登记·体量 | 最近）</th><th data-k="hit">命中规则</th><th data-k="pool">现池位</th><th data-k="st">表内状态 / 红旗</th><th>一句话情况</th><th>你的裁定</th>
    </tr></thead>
    <tbody id="body"></tbody>
  </table>
  </div>

  <div class="exp">
    <b>导出裁定</b>（口径 + 你点过的例外；没点的一律按口径）
    <div style="margin:8px 0"><span class="btn" id="copy">复制文本</span><span class="btn sec" id="dl">下载 CSV</span><span class="btn sec" id="clear">清空我所有裁定</span> <span class="mute" id="decCnt"></span></div>
    <textarea id="out" readonly></textarea>
  </div>

  <details class="legend"><summary>规则说明（点开）</summary>
    <table>
      <tr><th>A（核心关系：你亲自跟 · 季度复核 · P 池 ★ 核心）</th><th>严</th><th>宽 / 宽留冷</th></tr>
      <tr><td>A1 复购（成单 ≥2）或 邮件绑定 ≥ 中度</td><td>✔</td><td>✔</td></tr>
      <tr><td>A2 成单 / 付样 / PI ≥1 + 真人往来（真回 ≥1 或 WA 或 展会面谈）</td><td>要近 24 个月有往来</td><td>不限时间</td></tr>
      <tr><td>A3 真人往来 + 对位 + 四主区 / 波兰 + （登记坐实 或 自有品牌）</td><td>真回 ≥2 + 坐实 + 体量 ≥10 人</td><td>真回 ≥1 / WA / 展会即可</td></tr>
      <tr><td>A4 Simon 点名（S 重点 / 状态含「（Simon）」）</td><td>✔</td><td>✔</td></tr>
      <tr><td>A5 自有品牌 + 对位 + 任一真人往来（OEM 品牌商，任何区域）</td><td>—</td><td>✔</td></tr>
      <tr><td>A6 真人真回 ≥3（扣否定回复）+ 对位，任何区域</td><td>—</td><td>✔</td></tr>
      <tr><th>B（培育：发送包 + 两月巡检）</th><th></th><th></th></tr>
      <tr><td>B1 成单 / 样品 / PI 但 gg / 凉 · B2 真回 ≥1 / WA / 有打开 ≥2（宽含展会）+ 对位 · B3 自有品牌 + 对位 · B4 四主区 / 波兰 + 对位 + 坐实 · B5（宽）四主区 / 波兰 + 对位的冷户 · B6（宽留冷）对位的冷户任何区域都留 B</td><td colspan="2"></td></tr>
      <tr><th>C（储备）</th><td colspan="2">其余：不对位 / 守界（乌克兰 · 伊朗 · 叙利亚）；登记注销且非点名最高 B；gg 一律不计 A</td></tr>
    </table>
    <p class="mute">「真回」= 用户表 / S·A 箱 reply_sub 与 mail_review.facts「来」向真人来信取大者；「对位」字段漏标时有成单 / 样品 / PI / 真回 ≥3 视同对位；A 档未标 off 视同对位。</p>
  </details>
</main>
<script>
const DATA = __DATA__;
const PROFILES = [
  {id:'s', name:'严', desc:'只认钱和绑定（A 52 / B 573 / C 604）'},
  {id:'w', name:'宽', desc:'+ 自有品牌有往来、真回 ≥3 任何区域（A 170 / B 572 / C 487）'},
  {id:'kc', name:'宽留冷 ★ 建议', desc:'宽 + 对位冷户留 B 走发送包（A 170 / B 847 / C 212）'}
];
const HIT = {s:'hs', w:'hw', kc:'hk'};
const LS_P = 'ab_judge_profile_20261029', LS_D = 'ab_judge_dec_20261029';
let profile = localStorage.getItem(LS_P) || 'kc';
let dec = JSON.parse(localStorage.getItem(LS_D) || '{}');
let F = {chg:'变', cur:'', grp:'', pool:'', ev:'', q:'', onlyDec:false, sortK:'', sortD:1};

function chgOf(r){ const p = r[profile]; if (p === r.cur) return '不变'; return ((r.cur==='B'&&p==='A')||(r.cur==='C')) ? '升' : '降'; }
function el(id){ return document.getElementById(id); }
function esc(s){ return String(s==null?'':s).replace(/[&<>"]/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

function renderProfiles(){
  el('profiles').innerHTML = PROFILES.map(p=>`<button class="prof ${p.id===profile?'on':''}" data-p="${p.id}"><b>${p.name}</b><span>${p.desc}</span></button>`).join('');
  document.querySelectorAll('.prof').forEach(b=>b.onclick=()=>{profile=b.dataset.p; localStorage.setItem(LS_P, profile); renderAll();});
}
function finalOf(r){ const d = dec[r.c]; if (!d) return r[profile]; if (d === '不动') return r.cur; return d; }
function renderCards(){
  const cnt = {A:0,B:0,C:0}, cur = {A:0,B:0}; let up=0, down=0, nd=0;
  DATA.forEach(r=>{ cnt[finalOf(r)]++; cur[r.cur]++; const c = chgOf(r); if (c==='升') up++; else if (c==='降') down++; if (dec[r.c]) nd++; });
  el('cards').innerHTML = [
    ['现状', `A ${cur.A} / B ${cur.B}`],
    ['所选口径后', `<span class="g gA">A</span> ${cnt.A} &nbsp; <span class="g gB">B</span> ${cnt.B} &nbsp; <span class="g gC">C</span> ${cnt.C}`],
    ['升', `<span class="up">${up}</span>`], ['降', `<span class="down">${down}</span>`], ['你已裁定', nd]
  ].map(([l,v])=>`<div class="card"><div class="v">${v}</div><div class="l">${l}</div></div>`).join('');
}
function passes(r){
  const c = chgOf(r);
  if (F.chg === '变' && c === '不变') return false;
  if ((F.chg === '升' || F.chg === '降' || F.chg === '不变') && c !== F.chg) return false;
  if (F.cur && r.cur !== F.cur) return false;
  if (F.grp && r.g !== F.grp) return false;
  if (F.pool && (r.pool||'—') !== F.pool) return false;
  if (F.ev) {
    const rep = +r.rep || 0;
    if (F.ev==='deal' && !(r.deal||r.smp||r.pi)) return false;
    if (F.ev==='rep' && rep < 1) return false;
    if (F.ev==='rep3' && rep < 3) return false;
    if (F.ev==='wa' && !r.wa) return false;
    if (F.ev==='own' && !r.own) return false;
    if (F.ev==='cold' && (rep > 0 || r.wa)) return false;
  }
  if (F.onlyDec && !dec[r.c]) return false;
  if (F.q) { const q = F.q.toLowerCase(); if (!(r.c+' '+r.n+' '+r.k+' '+r.dom+' '+r.sit+' '+r.st).toLowerCase().includes(q)) return false; }
  return true;
}
function sortRows(rows){
  if (!F.sortK) { const o = {'降':0,'升':1,'不变':2}; return rows.sort((a,b)=> (o[chgOf(a)]-o[chgOf(b)]) || a.cur.localeCompare(b.cur) || a.c.localeCompare(b.c)); }
  const k = F.sortK;
  const val = r => k==='prop' ? r[profile] : k==='chg' ? chgOf(r) : k==='hit' ? r[HIT[profile]] : (r[k]||'');
  return rows.sort((a,b)=> (val(a)>val(b)?1:val(a)<val(b)?-1:0) * F.sortD);
}
function renderTable(){
  const rows = sortRows(DATA.filter(passes));
  el('cnt').textContent = `显示 ${rows.length} / ${DATA.length} 户（口径：${PROFILES.find(p=>p.id===profile).name}）`;
  const out = [];
  for (const r of rows) {
    const p = r[profile], c = chgOf(r), d = dec[r.c] || '';
    const ev = `${r.deal||'—'}·${r.smp||'—'}·${r.pi||'—'} | ${r.rep}·${r.op}·${r.wa||'—'}·${r.fair||'—'} | ${r.own||'—'}·${r.reg||'—'}·${r.emp||'—'} | ${r.last||'—'}`;
    const name = r.url ? `<a href="${r.url}" target="_blank" rel="noopener">${esc(r.n)}</a>` : esc(r.n);
    out.push(`<tr class="${d?'decided':''} ${c==='不变'?'muted-row':''}" data-c="${r.c}">
      <td><b>${r.c}</b></td><td>${name}${r.dom?`<br><span class="mute">${esc(r.dom)}</span>`:''}</td><td>${esc(r.k)}<br><span class="mute">${esc(r.g)}</span></td>
      <td><span class="g g${r.cur}">${r.cur}</span></td><td><span class="g g${p}">${p}</span>${d?` → <span class="g g${finalOf(r)}">${finalOf(r)}</span>`:''}</td>
      <td class="${c==='升'?'up':c==='降'?'down':'same'}">${c}</td>
      <td class="ev">${esc(ev)}<br><span class="mute">绑定：${esc(r.bind)} · 对位：${esc(r.fit)}</span></td>
      <td>${esc(r[HIT[profile]])}</td><td>${esc(r.pool||'—')}</td><td>${esc(r.st)}${r.flag?`<br><span class="down">${esc(r.flag)}</span>`:''}</td>
      <td class="sit">${esc(r.sit)||'<span class="mute">—</span>'}</td>
      <td class="dec">${['A','B','C','不动'].map(x=>`<button data-c="${r.c}" data-d="${x}" class="${d===x?'on':''}">${x}</button>`).join('')}</td>
    </tr>`);
  }
  el('body').innerHTML = out.join('');
  document.querySelectorAll('.dec button').forEach(b=>b.onclick=()=>{
    const c=b.dataset.c, v=b.dataset.d;
    if (dec[c]===v) delete dec[c]; else dec[c]=v;
    localStorage.setItem(LS_D, JSON.stringify(dec)); renderCards(); renderTable(); renderOut();
  });
}
function renderOut(){
  const lines = [`口径=${PROFILES.find(p=>p.id===profile).name.replace(' ★ 建议','')}`];
  const keys = Object.keys(dec).sort();
  keys.forEach(c=>{ const r = DATA.find(x=>x.c===c); lines.push(`${c}=${dec[c]}（现 ${r.cur}，建议 ${r[profile]}；${r.n.slice(0,24)}）`); });
  if (!keys.length) lines.push('（没有例外：全部按口径执行）');
  el('out').value = lines.join('\n');
  el('decCnt').textContent = `例外 ${keys.length} 户`;
}
function renderAll(){ renderProfiles(); renderCards(); renderTable(); renderOut(); }

// filters
document.querySelectorAll('.chip[data-f=chg]').forEach(ch=>ch.onclick=()=>{ document.querySelectorAll('.chip[data-f=chg]').forEach(x=>x.classList.remove('on')); ch.classList.add('on'); F.chg = ch.dataset.v; renderTable(); });
[...new Set(DATA.map(r=>r.g))].forEach(g=>{ const o=document.createElement('option'); o.textContent=g; el('fGrp').appendChild(o); });
[...new Set(DATA.map(r=>r.pool||'—'))].sort().forEach(g=>{ const o=document.createElement('option'); o.textContent=g; el('fPool').appendChild(o); });
el('fCur').onchange = e=>{F.cur=e.target.value; renderTable();};
el('fGrp').onchange = e=>{F.grp=e.target.value; renderTable();};
el('fPool').onchange = e=>{F.pool=e.target.value; renderTable();};
el('fEv').onchange = e=>{F.ev=e.target.value; renderTable();};
el('fQ').oninput = e=>{F.q=e.target.value.trim(); renderTable();};
el('fDec').onclick = ()=>{F.onlyDec=!F.onlyDec; el('fDec').classList.toggle('on', F.onlyDec); renderTable();};
el('reset').onclick = ()=>{ F={chg:'变',cur:'',grp:'',pool:'',ev:'',q:'',onlyDec:false,sortK:'',sortD:1}; el('fCur').value=''; el('fGrp').value=''; el('fPool').value=''; el('fEv').value=''; el('fQ').value=''; el('fDec').classList.remove('on'); document.querySelectorAll('.chip[data-f=chg]').forEach(x=>x.classList.toggle('on', x.dataset.v==='变')); renderTable(); };
document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{ const k=th.dataset.k; if (F.sortK===k) F.sortD=-F.sortD; else {F.sortK=k; F.sortD=1;} renderTable(); });
el('copy').onclick = ()=>{ const t = el('out'); t.select(); try { navigator.clipboard.writeText(t.value); } catch(e) { document.execCommand('copy'); } el('copy').textContent='已复制 ✔'; setTimeout(()=>el('copy').textContent='复制文本', 1500); };
el('dl').onclick = ()=>{
  const prof = PROFILES.find(p=>p.id===profile).name.replace(' ★ 建议','');
  const head = ['编号','公司','国家','现等级','口径','建议','裁定','最终'];
  const lines = [head.join(',')].concat(DATA.map(r=>[r.c, '"'+r.n.replace(/"/g,'""')+'"', r.k, r.cur, prof, r[profile], dec[r.c]||'', finalOf(r)].join(',')));
  const blob = new Blob(['\ufeff'+lines.join('\n')], {type:'text/csv;charset=utf-8'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'AB裁定_'+prof+'_2026-10-29.csv'; a.click();
};
el('clear').onclick = ()=>{ if (confirm('清空你在本页点过的全部裁定？')) { dec={}; localStorage.setItem(LS_D,'{}'); renderAll(); } };
renderAll();
</script>
</body>
</html>
'''
    page = page.replace('__NOW__', now).replace('__DATA__', data_json)
    open(OUT, 'w', encoding='utf-8').write(page)
    print(os.path.relpath(OUT, ROOT), len(rows), 'A', n_a, 'B', n_b, 'links', sum(1 for r in rows if r['url']), f'{os.path.getsize(OUT)/1024:.0f} KB')


if __name__ == '__main__':
    main()
