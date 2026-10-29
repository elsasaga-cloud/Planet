#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-R10 · 官网快照打回候选复核（Saga 63 户）· T29-U134「搞吧」2026-10-29 16:2xZ。

来源：customer-watch 手动 Run ALL（15:11Z 起，机器人提交 0ba86b78d：快照 1,112 份；运行器已自跑 lt_snapshot_thicken）→
      data/长期客户群_快照打回候选_2026-10-29.csv 66 户（Saga 63 / Planet 3），规则 = 两次不同日期快照失败且无成功。
复核方法（方法论 M6 / D-03）：每户全部域名 dnspython 查 MX / A / NS，异常域 5 秒后第二次查询；
  结果：71 域里 69 域 DNS 正常（快照失败 = 反爬 / 超时 / 屏蔽境外，非死域）→ 不打回；
  fybera.com NoNameservers（同 LT-R09）、hisvisionhatay.com NXDOMAIN（SB-294 副域，主域 + WA 在）；
  停放页 7 户逐户看快照正文：SA-004 STRATO 占位 / SB-294 挂牌 / SB-389 HugeDomains / SB-522 HugeDomains（同户 guilera.com 在）/
  SB-636 主机商占位 / SB-729 抓到施工页（主站在）/ SB-815 误判（正常商店页）。
  A 级 3 户（SA-004 / SB-389 / SB-451）用新增 verdict「留A」：不动等级，只记证据与日志。
幂等：lt_review_lib.run + 本文件末尾 website_status 修正（只改占位 / 过期值）。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lt_review_lib import run, RESEARCH  # noqa: E402

BATCH = 'LT-R10'
V = {
 "SA-004": [
  "留A",
  "boecek.de 官网两次快照（10-21 / 10-29）为 STRATO「Domain reserved」占位页，但 DNS 2026-10-29 16:2xZ MX smtpin.rzone.de（STRATO 邮箱）/ A / NS 正常 → 域名未死、邮箱路径未断；邮件 15 封 0 打开仍是老问题 → A 不动（Simon 表内「样品购买 + 型号问价」），发信前核地址 / 问 Simon 有无别的联系方式",
  [
   [
    "DNS 2026-10-29 16:2xZ：boecek.de MX smtpin.rzone.de.；A 217.160.0.167；NS docks02.rzone.de. / shades02.rzone.de.",
    ""
   ]
  ]
 ],
 "SB-014": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 intecseg.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：intecseg.com MX mx.serviciodecorreo.es.；A 23.236.62.147；NS dns13.servidoresdns.net. / dns14.servidoresdns.net.",
    ""
   ]
  ]
 ],
 "SB-024": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 erstech.hu MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：erstech.hu MX posta3.mediacenter.hu. / posta2.mediacenter.hu.；A 92.43.203.178；NS ns2.mediacenter.hu. / ns3.mc-int-dns.org.",
    ""
   ]
  ]
 ],
 "SB-027": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：超时），但 DNS 2026-10-29 16:2xZ 复查 voipdistri.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：voipdistri.com MX mx08.mxgate.org. / mx07.mxgate.org.；A 185.226.241.8；NS ns2.q-ns.de. / ns1.q-ns.de.",
    ""
   ]
  ]
 ],
 "SB-081": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 dabos.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：dabos.com MX dabos-com.mail.protection.outlook.com.；A 104.18.16.101 / 104.18.17.101；NS nitin.ns.cloudflare.com. / amber.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-090": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 adlerss.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：adlerss.com MX adlerss-com.mail.protection.outlook.com.；A 104.21.81.52 / 172.67.138.217；NS beth.ns.cloudflare.com. / noah.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-1012": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：超时），但 DNS 2026-10-29 16:2xZ 复查 bitstreamcore.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：bitstreamcore.com MX mail.h-email.net.；A 104.247.81.99；NS ns1.parkingcrew.net. / ns2.parkingcrew.net.",
    ""
   ]
  ]
 ],
 "SB-1034": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 gogss.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：gogss.com MX aspmx.l.google.com. / alt2.aspmx.l.google.com.；A 104.21.60.147 / 172.67.197.200；NS laila.ns.cloudflare.com. / gabriel.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-1051": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 klemsan.com.tr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：klemsan.com.tr MX klemsan-com-tr.mail.protection.outlook.com.；A 104.26.9.177 / 172.67.71.65；NS lex.ns.cloudflare.com. / tara.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-1055": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 marcomweb.it MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：marcomweb.it MX alt3.aspmx.l.google.com. / alt4.aspmx.l.google.com.；A 104.21.43.15 / 172.67.215.215；NS kia.ns.cloudflare.com. / kip.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-1064": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：连接不可达（屏蔽境外 / 仅 CDN）），但 DNS 2026-10-29 16:2xZ 复查 portdepo.ru MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：portdepo.ru MX mx2.timeweb.ru. / mx1.timeweb.ru.；A 185.114.245.110；NS ns4.timeweb.org. / ns1.timeweb.ru.",
    ""
   ]
  ]
 ],
 "SB-1075": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 silmarelectronics.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：silmarelectronics.com MX mx2-us1.ppe-hosted.com. / mx1-us1.ppe-hosted.com.；A 172.67.73.9 / 104.26.11.165；NS keenan.ns.cloudflare.com. / brenna.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-1087": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 tehnoelectric.ro MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：tehnoelectric.ro MX mail.tehnoelectric.ro.；A 172.67.204.213 / 104.21.77.55；NS rafe.ns.cloudflare.com. / chuck.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-1098": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 zintronic.pl MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：zintronic.pl MX aspmx2.googlemail.com. / aspmx3.googlemail.com.；A 104.26.6.126 / 172.67.69.70；NS toby.ns.cloudflare.com. / peaches.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-146": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 exsys.it MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：exsys.it MX mx.exsys.it.；A 89.46.104.30；NS dns3.arubadns.net. / dns.technorail.com.",
    ""
   ]
  ]
 ],
 "SB-165": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：超时），但 DNS 2026-10-29 16:2xZ 复查 yminc.ca MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：yminc.ca MX mail2.stitches.ca. / mail.stitches.ca.；A 207.35.187.90；NS toroondcnszs04.srvr.bell.ca. / toroon63nszp04.srvr.bell.ca.",
    ""
   ]
  ]
 ],
 "SB-187": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 pelikanbilgisayar.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：pelikanbilgisayar.com MX pmg.arslanbilgisayar.com.tr.；A 104.21.49.59 / 172.67.159.56；NS ken.ns.cloudflare.com. / beth.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-195": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 bkgrupe.lt MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：bkgrupe.lt MX bkgrupe-lt.mail.protection.outlook.com.；A 104.26.6.52 / 172.67.69.36；NS asa.ns.cloudflare.com. / sergi.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-225": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：连接不可达（屏蔽境外 / 仅 CDN）），但 DNS 2026-10-29 16:2xZ 复查 shnrise.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：shnrise.com MX mail.shnrise.com.；A 45.84.189.66；NS ns32.guzelhosting.com. / ns31.guzelhosting.com.",
    ""
   ]
  ]
 ],
 "SB-234": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 benzotronic.it MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：benzotronic.it MX mx.vm202.interferenza.net.；A 104.21.3.148 / 172.67.130.213；NS olga.ns.cloudflare.com. / bowen.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-268": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 bulutlarbilisim.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：bulutlarbilisim.com MX bulutlarbilisim-com.mail.protection.outlook.com.；A 15.197.148.33 / 3.33.130.190；NS ns56.domaincontrol.com. / ns55.domaincontrol.com.",
    ""
   ]
  ]
 ],
 "SB-273": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 eretekne.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：eretekne.com MX mx.uzmanposta.com.；A 104.19.157.83 / 104.19.156.83；NS ns1.myideasoft.com. / ns2.myideasoft.com.",
    ""
   ]
  ]
 ],
 "SB-294": [
  "留B",
  "vivabilgisayar.com 快照为「Premium Parking Page」（挂牌）、hisvisionhatay.com DNS NXDOMAIN（2026-10-29 两次查询）；但 vivabilgisayar.com MX 仍指 Google（info@ 可能仍收信）+ WhatsApp 已加（90 544 64 91 142）+ 表内 hotmail → 路径 = WhatsApp / hotmail / info@（MX 在）→ 留 B；两站不再当官网用",
  [
   [
    "DNS 2026-10-29 16:2xZ：hisvisionhatay.com MX NXDOMAIN；A NXDOMAIN；NS NXDOMAIN",
    ""
   ],
   [
    "DNS 2026-10-29 16:2xZ：vivabilgisayar.com MX aspmx3.googlemail.com. / alt1.aspmx.l.google.com.；A 85.159.66.93；NS ns2.natrohost.com. / ns1.natrohost.com.",
    ""
   ]
  ]
 ],
 "SB-307": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 saxco.com.my MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：saxco.com.my MX smtp.google.com.；A 104.21.18.103 / 172.67.181.148；NS hazel.ns.cloudflare.com. / woz.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-321": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 bwsystems.de MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：bwsystems.de MX mx01.ionos.de. / mx00.ionos.de.；A 217.160.0.214；NS ns1042.ui-dns.de. / ns1042.ui-dns.org.",
    ""
   ]
  ]
 ],
 "SB-346": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 atz.com.sg MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：atz.com.sg MX mail.atz.com.sg.；A 104.21.72.91 / 172.67.179.117；NS melinda.ns.cloudflare.com. / mitch.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-352": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 fiberdyne.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：fiberdyne.com MX fiberdyne-com.mail.protection.outlook.com.；A 209.17.116.160；NS ns2-04.azure-dns.net. / ns3-04.azure-dns.org.",
    ""
   ]
  ]
 ],
 "SB-354": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 fiberopticlink.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：fiberopticlink.com MX fiberopticlink-com.mail.protection.outlook.com.；A 104.19.154.92；NS ns1.bluehost.com. / ns2.bluehost.com.",
    ""
   ]
  ]
 ],
 "SB-386": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 dvs.co.uk MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：dvs.co.uk MX eu-smtp-inbound-1.mimecast.com. / eu-smtp-inbound-2.mimecast.com.；A 104.18.5.120 / 104.18.4.120；NS troy.ns.cloudflare.com. / dell.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-389": [
  "留A",
  "hiperonline.com 快照为 HugeDomains「for sale」页，DNS 2026-10-29 MX NoAnswer / A = NameBright 停放 IP → eskisehir@hiperonline.com 邮件路径已断；公司在营（BTK 授权 ISP，官网 hiperonline.com.tr）+ ISAF 名片 + WhatsApp 已加 → A 不动，路径 = WhatsApp / .com.tr 域；.com 地址不再发",
  [
   [
    "DNS 2026-10-29 16:2xZ：hiperonline.com MX NoAnswer；A 54.243.117.197 / 13.223.25.84；NS nsg1.namebrightdns.com. / nsg2.namebrightdns.com.",
    ""
   ]
  ]
 ],
 "SB-396": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 morekamer.ru MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：morekamer.ru MX mx.yandex.net.；A 141.8.192.192；NS ns3.sprinthost.net. / ns4.sprinthost.net.",
    ""
   ]
  ]
 ],
 "SB-400": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 safanetworks.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：safanetworks.com MX mx.stackmail.com.；A 172.67.182.6 / 104.21.59.177；NS arya.ns.cloudflare.com. / sterling.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-451": [
  "留A",
  "e-saudi.net 快照两次 http_error，但 DNS 2026-10-29 MX Google / A 209.17.116.163 正常 → 站点反爬 / 非死域，邮箱路径在 → A 不动",
  [
   [
    "DNS 2026-10-29 16:2xZ：e-saudi.net MX aspmx2.googlemail.com. / alt2.aspmx.l.google.com.；A 209.17.116.163；NS ns37.worldnic.com. / ns38.worldnic.com.",
    ""
   ]
  ]
 ],
 "SB-460": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：连接不可达（屏蔽境外 / 仅 CDN）），但 DNS 2026-10-29 16:2xZ 复查 4g-gmbh.de MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：4g-gmbh.de MX mx01.ionos.de. / mx00.ionos.de.；A NoAnswer；NS ns1117.ui-dns.biz. / ns1071.ui-dns.com.",
    ""
   ]
  ]
 ],
 "SB-487": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：超时），但 DNS 2026-10-29 16:2xZ 复查 npotelecom.ru MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：npotelecom.ru MX mail.npotelecom.ru.；A 81.177.6.164；NS ns4.jino.ru. / ns1.jino.ru.",
    ""
   ]
  ]
 ],
 "SB-509": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 ione.kr、ionetech.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：ione.kr MX kr1-aspmx2.worksmobile.com. / kr1-aspmx1.worksmobile.com.；A 119.200.199.118；NS ns1.ssandom.com. / ns2.ssandom.com.",
    ""
   ],
   [
    "DNS 2026-10-29 16:2xZ：ionetech.com MX mail.ionetech.com.；A 114.108.129.120；NS ns.hostment.com. / ns2.hostment.com.",
    ""
   ]
  ]
 ],
 "SB-522": [
  "留B",
  "adilec.com 快照为 HugeDomains「for sale」、DNS MX NoAnswer / A = NameBright 停放 IP → info@adilec.com 已断；同户 guilera.com DNS 正常（MX Hornetsecurity，A 217.76.132.72）且 Elsa 2025-02-10 曾 1:1 去信 guilera@guilera.com → 留 B，路径 = guilera.com 两地址；adilec.com 不再发",
  [
   [
    "DNS 2026-10-29 16:2xZ：adilec.com MX NoAnswer；A 13.223.25.84 / 54.243.117.197；NS nsg2.namebrightdns.com. / nsg1.namebrightdns.com.",
    ""
   ],
   [
    "DNS 2026-10-29 16:2xZ：guilera.com MX mx01.hornetsecurity.com. / mx02.hornetsecurity.com.；A 217.76.132.72；NS dns1.editorialamc.com. / dns2.editorialamc.com.",
    ""
   ]
  ]
 ],
 "SB-525": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 atlantis-land.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：atlantis-land.com MX mx.zoho.eu. / mx3.zoho.eu.；A 172.67.132.115 / 104.21.4.210；NS weston.ns.cloudflare.com. / gail.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-537": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：连接不可达（屏蔽境外 / 仅 CDN）），但 DNS 2026-10-29 16:2xZ 复查 htvision.ru MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：htvision.ru MX mail.htvision.ru.；A 217.107.219.186；NS ns3.jino.ru. / ns1.jino.ru.",
    ""
   ]
  ]
 ],
 "SB-551": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 sanspot.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：sanspot.com MX sanspot-com.mail.protection.outlook.com.；A 104.26.11.44 / 104.26.10.44；NS nadia.ns.cloudflare.com. / bruce.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-558": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 uniformatic.fr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：uniformatic.fr MX uniformatic-fr.mail.protection.outlook.com.；A NoAnswer；NS ns5.safebrands.tech. / ns1.safebrands.fr.",
    ""
   ]
  ]
 ],
 "SB-564": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 voiptech.co.mz MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：voiptech.co.mz MX mail.voiptech.co.mz.；A 50.87.0.105；NS ns2.rhostbh.com. / ns1.rhostbh.com.",
    ""
   ]
  ]
 ],
 "SB-575": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 marbim.com.tr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：marbim.com.tr MX mail.marbim.com.tr.；A 89.252.182.2；NS ns32.guzelhosting.com. / ns31.guzelhosting.com.",
    ""
   ]
  ]
 ],
 "SB-636": [
  "留B",
  "marzetek.com 快照两次为主机商「coming soon」占位页（VE Host）；但 DNS 2026-10-29 MX mail.marzetek.com / A 102.208.231.50 正常 → procurement@ 路径技术上仍在；A 邮箱 17 封 0 回属冷户（B2 不因冷降级），需求 4+24 / 4+48 10G 对位 → 留 B（群发层）；电话 +27 61 836 5820 未试，可逆",
  [
   [
    "DNS 2026-10-29 16:2xZ：marzetek.com MX mail.marzetek.com.；A 102.208.231.50；NS dns2.webway.host. / dns1.webway.host.",
    ""
   ]
  ]
 ],
 "SB-691": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 vitel.com.tr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：vitel.com.tr MX vitel-com-tr.mail.protection.outlook.com.；A 172.67.160.116 / 104.21.42.90；NS leonidas.ns.cloudflare.com. / nicole.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-724": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 comms-express.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：comms-express.com MX d235690.a.ess.uk.barracudanetworks.com. / d235690.b.ess.uk.barracudanetworks.com.；A 104.20.24.54 / 172.66.162.129；NS kayleigh.ns.cloudflare.com. / vick.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-729": [
  "留B",
  "快照抓的是 secure-x.my「Portal Page Under Construction」；主站 heitech.com.my DNS 正常（MX Trend Micro 托管 / A 202.171.42.202）→ 上市集成商 HeiTech Padu 在营，rizaki@heitech.com.my 路径在 → 留 B；website 以 heitech.com.my 为准",
  [
   [
    "DNS 2026-10-29 16:2xZ：heitech.com.my MX fa98d20c-cc19-4f3b-885b-d6804a8d1346.in.tmes-sg.trendmicro.c；A 202.171.42.202；NS i1dns.i-sentrix.com. / i2dns.i-sentrix.net.",
    ""
   ],
   [
    "DNS 2026-10-29 16:2xZ：secure-x.my MX fa98d20c-cc19-4f3b-885b-d6804a8d1346.in.tmes-sg.trendmicro.c；A 202.171.33.164；NS i2dns.i-sentrix.net. / i1dns.i-sentrix.com.",
    ""
   ]
  ]
 ],
 "SB-730": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 it2ss.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：it2ss.com MX mail.it2ss.com.；A 50.116.95.52；NS hgns2.hostgator.com. / hgns1.hostgator.com.",
    ""
   ]
  ]
 ],
 "SB-740": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 bcp-uk.com、britaniccablingproduction.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：bcp-uk.com MX bcpuk-com0i.mail.protection.outlook.com.；A 185.151.30.173；NS ns1.stackdns.com. / ns3.stackdns.com.",
    ""
   ],
   [
    "DNS 2026-10-29 16:2xZ：britaniccablingproduction.com MX mx.stackmail.com.；A 185.151.30.173；NS ns4.stackdns.com. / ns2.stackdns.com.",
    ""
   ]
  ]
 ],
 "SB-772": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 mencom.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：mencom.com MX mencom-com.mail.protection.outlook.com.；A 104.26.11.50 / 104.26.10.50；NS noor.ns.cloudflare.com. / clint.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-781": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 silvernet.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：silvernet.com MX silvernet-com.mail.protection.outlook.com.；A 185.151.30.172；NS ns2.bdm.microsoftonline.com. / ns4.bdm.microsoftonline.com.",
    ""
   ]
  ]
 ],
 "SB-797": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：连接不可达（屏蔽境外 / 仅 CDN）），但 DNS 2026-10-29 16:2xZ 复查 excelengineeringsg.net MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：excelengineeringsg.net MX alt1.aspmx.l.google.com. / alt2.aspmx.l.google.com.；A NoAnswer；NS ns-cloud-a1.googledomains.com. / ns-cloud-a3.googledomains.com.",
    ""
   ]
  ]
 ],
 "SB-815": [
  "留B",
  "快照判 parked_or_empty 为误判：首页标题「Lendoux Specialized Store」+ 完整描述（数据中心 / 电信 / 安防 / 工业仪表多品牌商店）；DNS 正常（MX mail.lendoux.com / A 51.79.87.52）→ 在营，留 B",
  [
   [
    "DNS 2026-10-29 16:2xZ：lendoux.com MX mail.lendoux.com.；A 51.79.87.52；NS ns2.gcdn.services. / ns1.gcorelabs.net.",
    ""
   ]
  ]
 ],
 "SB-838": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：超时），但 DNS 2026-10-29 16:2xZ 复查 gmidatabox.fr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：gmidatabox.fr MX mx1.mail.ovh.net.；A 51.210.178.3；NS dns12.ovh.net. / ns12.ovh.net.",
    ""
   ]
  ]
 ],
 "SB-844": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 oemarket.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：oemarket.com MX mx02.mailcluster.com.au. / mx01.mailcluster.com.au.；A 101.0.113.110；NS ns4.digitalpacific.com. / ns3.digitalpacific.com.",
    ""
   ]
  ]
 ],
 "SB-895": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：超时），但 DNS 2026-10-29 16:2xZ 复查 vilcom.ru MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：vilcom.ru MX mail.vilcom.ru.；A 81.177.135.38；NS ns3-l2.nic.ru. / ns4-cloud.nic.ru.",
    ""
   ]
  ]
 ],
 "SB-944": [
  "留B",
  "fybera.com DNS 2026-10-29 16:2xZ 仍 NoNameservers（与 14:48Z LT-R09 一致，委派仍坏）；LT-R09 已据搜索摘要判在营（自有品牌 Fybera 光纤无源 / 媒转，sales@fybera.com）→ 维持留 B，下次巡检（12-28）再查委派；邮箱路径待观察",
  [
   [
    "DNS 2026-10-29 16:2xZ：fybera.com MX NoNameservers；A NoNameservers；NS NoNameservers",
    ""
   ]
  ]
 ],
 "SB-948": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 krysma.com.au MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：krysma.com.au MX smtp.krysma.com.au.；A 172.67.196.166 / 104.21.68.155；NS duke.ns.cloudflare.com. / gail.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-962": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：连接不可达（屏蔽境外 / 仅 CDN）），但 DNS 2026-10-29 16:2xZ 复查 triplenet.co.kr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：triplenet.co.kr MX mail.triplenet.co.kr.；A 133.186.144.129；NS ns4.cypack.com. / ns3.cypack.com.",
    ""
   ]
  ]
 ],
 "SB-966": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：连接不可达（屏蔽境外 / 仅 CDN）），但 DNS 2026-10-29 16:2xZ 复查 view-tel.co.kr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：view-tel.co.kr MX mx01.mailplug.com.；A NoAnswer；NS ns2.cafe24.co.kr. / ns1.cafe24.co.kr.",
    ""
   ]
  ]
 ],
 "SB-968": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 zenithtek.co.kr MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：zenithtek.co.kr MX mailapp.hiworks.co.kr.；A 104.21.7.156 / 172.67.130.85；NS miles.ns.cloudflare.com. / jasmine.ns.cloudflare.com.",
    ""
   ]
  ]
 ],
 "SB-972": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：超时），但 DNS 2026-10-29 16:2xZ 复查 electrologicservices.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：electrologicservices.com MX aspmx3.googlemail.com. / alt1.aspmx.l.google.com.；A 62.38.149.50；NS ns52.domaincontrol.com. / ns51.domaincontrol.com.",
    ""
   ]
  ]
 ],
 "SB-993": [
  "留B",
  "官网快照两次失败（2026-10-21 / 2026-10-29：HTTP 错误（4xx/5xx，多为反爬 / 屏蔽境外抓取）），但 DNS 2026-10-29 16:2xZ 复查 abigo4u.com MX/A/NS 正常 → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据（可逆：两次独立 DNS 死才复核）",
  [
   [
    "DNS 2026-10-29 16:2xZ：abigo4u.com MX NoAnswer；A 136.144.212.108；NS ns2.dn-s.nl. / ns3.dn-s.nl.",
    ""
   ]
  ]
 ]
}

# 快照停放 / 误判户的 website_status 修正（thicken 只替换占位，不覆盖「在线」等旧值；这里按复核结论改写，幂等）
WS = {
 'SA-004': '官网停放（boecek.de = STRATO「Domain reserved」占位页，2026-10-21 / 10-29 两次；域名与邮箱 MX 仍在）',
 'SB-294': '两域失效（vivabilgisayar.com 挂牌停放、hisvisionhatay.com NXDOMAIN，2026-10-29；MX 仍指 Google；路径 = WhatsApp）',
 'SB-389': 'hiperonline.com 已挂牌出售（HugeDomains，2026-10-29；MX 无）；公司在营官网 hiperonline.com.tr',
 'SB-522': 'adilec.com 已挂牌出售（HugeDomains，2026-10-29；MX 无）；同户 guilera.com 在（MX Hornetsecurity）',
 'SB-636': '官网为主机商占位页（marzetek.com「coming soon」，2026-10-21 / 10-29）；域名与 MX 在',
 'SB-729': '在线（主站 heitech.com.my；secure-x.my 为施工页，2026-10-29）',
 'SB-815': '在线（lendoux.com「Lendoux Specialized Store」；快照 parked 判定为误判，2026-10-29）',
}


def fix_ws():
    n = 0
    for code, ws in WS.items():
        p = os.path.join(RESEARCH, code + '.json')
        j = json.load(open(p, encoding='utf-8'))
        if j.get('website_status') == ws:
            continue
        j.setdefault('website_status_prev', j.get('website_status'))
        j['website_status'] = ws
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        n += 1
    print('website_status fixed', n)


if __name__ == '__main__':
    run(BATCH, V)
    fix_ws()
