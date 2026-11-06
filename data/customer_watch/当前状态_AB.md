# A/B 级客户 · 动态监控 · 当前状态（T29-U19）

> 失败分类（最近一次状态）：HTTP 503 ×518；HTTP 403 ×73；ConnectTimeout: HTTPSConnectionPool ×37；ConnectionError: HTTPSConnectionPool ×31；HTTP 404 ×30；SSLError: HTTPSConnectionPool ×24；ReadTimeout: HTTPSConnectionPool ×11；RuntimeError: channelId not found ×9；YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_ ×4；HTTP 500 ×3。403 = 站点反爬（运行器 IP 被拦，人工看）；YouTube 404 = YouTube 对数据中心 IP 的拦截（设仓库 secret YT_API_KEY 后走官方 API）；其它 404 = 页面不存在；SSL/连接/DNS 错误 = 站点本身问题，连续多轮失败再从清单摘掉。

> 本轮 2026-11-06T09:32:27Z。客户 1392 家 / 源 3995 个。清单 `scripts/web_watch/targets_auto.json`（discover.py 离线生成：首页 / sitemap / 新闻栏目 / YouTube / GitHub / Telegram / VK + 运行时自动发现的 feed）。变化见 `变化日志_AB.md`；每客户文本快照在 `snapshots/<客户码>/`。「最近变化」= 任一源最近一次内容变化的时间（首轮 = 基线时间）；「人工看」= 有登录墙的社媒，链接在 targets_auto.json 的 manual 字段。

| 客户 | 级 | 源数 | 本轮可达/失败 | 最近变化 | 最近变化摘要 | 人工看 |
|---|---|---|---|---|---|---|
| SA-002 simrex.com | A | 2 | 2/0 | 2026-11-01T09:25:59Z | 2026-11-01 intel_news_en：新增 1 条：Sun, 16 Jul 2023 07 The Best Drones for Under $100 - MakeUseOf |  |
| SA-003 Eyescan security Systems | A | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook、Instagram、LinkedIn |
| SA-004 Boecek Sec | A | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SA-005 Taurus Vision | A | 2 | 2/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SA-009 coptek.com.tr | A | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 31 条：2021-01-11T14:01:38 www.coptek.com.tr；2021-01-11T14:01:38 index.html；2021 |  |
| SA-010 NEXTU EZ-NET | A | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Instagram |
| SA-011 CXR | A | 7 | 7/0 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Instagram、LinkedIn、X/Twitter、Facebook |
| SA-012 widen.co.th | A | 1 | 0/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SA-014 impulsecctv.com | A | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+13 −13 行 | LinkedIn、X/Twitter |
| SA-015 megnet.co.uk | A | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+37 −28 行 | LinkedIn、X/Twitter |
| SA-020 bitstream.pl | A | 7 | 6/1 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：新增 1 条：Thu, 20 Dec 2018 08 ♪ Depeche Mode - A Pain That I'm Used To [Bitstr | Facebook、LinkedIn、X/Twitter |
| SA-021 optiviewusa.com | A | 2 | 1/1 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：更新 1 条：Space42 and IEC Telecom target up to 30% more capacity from （Wed, 04 |  |
| SA-023 fcnet.pl | A | 3 | 2/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SA-025 Avenger Security（getsecurity | A | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+1 −0 行 | X/Twitter、Facebook、Instagram |
| SA-026 hardenednetworks.com | A | 4 | 4/0 | 2026-11-04T09:30:29Z | 2026-11-04 intel_news_en：新增 1 条：Fri, 27 Feb 2026 20 The State of the Union Meets the State of Cybers |  |
| SA-027 Al Salami Trading L.L.C | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SA-028 entasource.co.th | A | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 12 条：2021-10-11T14:12:37 network；2020-06-17T14:44:46 4k-over-fiber； hd-over-fi | Facebook |
| SA-029 gtwave.co.kr | A | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+2 −1 行 |  |
| SA-030 snexus.com.tr | A | 7 | 7/0 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Instagram、LinkedIn、Facebook |
| SA-031 Truong Son Solutions | A | 4 | 4/0 | 2026-11-02T09:40:28Z | 2026-11-02 home：内容变化：+6 −0 行 | Facebook、LinkedIn |
| SA-033 bluewarrior.com | A | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SA-034 rfog.pl | A | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2019-07-21T16:32:53 produkt,1101,mini-nadajnik-swiatlowodowy-catv-rf1t15 | Facebook |
| SA-035 td-fe.com | A | 5 | 2/3 | 2026-11-01T09:25:59Z | 2026-11-01 sitemap：新增 2 条：2022-09-04T06:00:01 td-fe.com；2022-09-04T06:00:01 enclosed |  |
| SA-036 svn-video.ru | A | 9 | 9/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+6 −6 行 |  |
| SA-039 mt-link.com | A | 4 | 4/0 | 2026-11-04T09:30:29Z | 2026-10-31 youtube：新增 1 条：2026-10-30T06:06:52 MT-Link’s 1000m armored cable ensures durable, moistur | Facebook、Instagram、X/Twitter、WhatsApp |
| SA-042 antronix.com | A | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 sitemap：新增 3 条：2026-11-05T00:09:49 2ghztaps_lp-install；2026-11-05T00:13:17 mvra；2026-11-0 |  |
| SA-043 direktronik.se | A | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+550 −1 行 |  |
| SA-045 energyplusystems.cl | A | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+19 −2 行 | WhatsApp、WhatsApp、WhatsApp |
| SA-047 sge.com.tr | A | 6 | 5/1 | 2026-10-31T08:34:28Z | 2026-10-24 news_2：内容变化：+5 −5 行 | Facebook、X/Twitter、LinkedIn |
| SA-048 ekhalas.com | A | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+62 −71 行 |  |
| SA-049 iotsistem.com | A | 6 | 6/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook、Instagram、X/Twitter |
| SA-050 impakt.com.pl | A | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 intel_news_pl：新增 3 条：Mon, 18 Apr 2022 07 Stowarzyszenie Impakt pomaga młodym w realizacji | Facebook、LinkedIn |
| SA-051 Tecpro Solutions | A | 7 | 7/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook、Instagram、LinkedIn |
| SA-053 infrateq.id | A | 3 | 3/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SA-054 softnetworks.net | A | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SA-055 NOVA Group Engineering Proje | A | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+83 −81 行 |  |
| SA-058 alphanetcom.com | A | 3 | 3/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SA-059 data-connect.com | A | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2018-01-09T15:47:06 Employment.htm；2018-01-09T15:46:33 Hot_Products.htm； |  |
| SA-060 gofiberx.com | A | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：新增 2 条：Wed, 07 Jul 2021 07 Converge FiberX offers exclusive deals at Shopee |  |
| SA-061 RYMTECH EAS | A | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SA-063 Areca Embedded Systems Pvt L | A | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-27 home：内容变化：+0 −13 行 |  |
| SA-064 optat.ru | A | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 intel_news_ru：更新 1 条：В Нижегородской области аннулированы декларации на рыбную пр（Tue, 27 |  |
| SA-066 ccs-msk.ru | A | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+3 −3 行 |  |
| SA-067 Latmedia Group, LLC | A | 6 | 6/0 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、Instagram |
| SA-068 Pt.ras otomasi indonesia | A | 3 | 3/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SA-070 Top Italia | A | 3 | 2/1 | 2026-11-05T09:39:48Z | 2026-11-05 intel_news_it：新增 5 条：Fri, 11 Mar 2022 10 ING Direct Top Italia Arancio Dis - www.altrocon |  |
| SA-071 surlink-tech.com | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SA-072 trans audio video group | A | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_it：新增 2 条：Mon, 25 May 2026 07 VIDEOCLIP ITALIA AWARDS 2026: il Piemonte protag |  |
| SA-074 Elite Team Security Ltd | A | 6 | 6/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SA-076 Telemobil | A | 3 | 2/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SA-082 ISIMKO GmbH,Guhrower Straße | A | 5 | 5/0 | 2026-11-01T09:25:59Z | 2026-11-01 intel_news_de：新增 1 条：Fri, 18 Jan 2019 08 Hackerangriff auf SeeCampus Niederlausitz. Syste |  |
| SA-085 HCS | A | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-010 americanfibertek.com | A | 5 | 5/0 | 2026-11-01T09:25:59Z | 2026-11-01 intel_news_en：新增 1 条：Fri, 01 May 2020 07 May 2020 Industry News - ASIS International |  |
| SB-018 Smart-Protect | A | 4 | 4/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-022 Desk Technologies | A | 7 | 7/0 | 2026-11-01T09:25:59Z | 2026-11-01 news_1：内容变化：+3 −3 行 | Instagram、Facebook、X/Twitter、LinkedIn |
| SB-027 VoIPDistri | A | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-031 OM Telecom S.R.L. | A | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：新增 1 条：Sun, 25 Aug 2024 07 SAMSUNG A04. A045F. CHARGING PROBLEM FIX - YouTu |  |
| SB-038 tricomp.com.pl | A | 3 | 2/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SB-040 4Demand Co | A | 5 | 1/4 | 2026-11-04T09:30:29Z | 2026-11-04 feed_auto：恢复可达（上轮 HTTP 503） | WhatsApp |
| SB-043 Euro Technology | A | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+1 −2 行 | Facebook、Instagram、LinkedIn、WhatsApp |
| SB-047 topica.mn | A | 5 | 2/3 | 2026-11-04T09:30:29Z | 2026-11-04 intel_news_en：新增 12 条：Wed, 29 Jul 2020 07 How EdTech in Southeast Asia Transforms Learnin | Facebook |
| SB-053 onnettechnologies.com | A | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-055 DIOS ULTRA HD VIDEO SECURITY | A | 4 | 0/4 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | X/Twitter、Instagram |
| SB-056 Net Work Business Solutions | A | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-057 Rfcom | A | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-059 avanca.com.sg | A | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-063 Avesta | A | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SB-071 nkstech.net | A | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-074 Bilge SECURITY SYSTEMS | A | 6 | 6/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-077 Liveye | A | 10 | 10/0 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_de：新增 1 条：Thu, 11 Dec 2025 08 Risikofaktor Baustelle: Sabotage und Spionage au | Instagram、Facebook、LinkedIn |
| SB-079 cansisteknoloji.com | A | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-085 DIGI Group | A | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −0 行 |  |
| SB-093 konakguvenlik.com.tr | A | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、Instagram |
| SB-1026 epygi.com | A | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 1 条：Fri, 30 Oct 2026 12 October 2026 Newsletter | Facebook、LinkedIn、X/Twitter |
| SB-103 Grundig | A | 7 | 5/2 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn |
| SB-1031 findcontrols.com | A | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+77 −35 行 | Instagram、X/Twitter |
| SB-104 STS Italia S.r.l. | A | 3 | 1/2 | 2026-11-03T09:43:52Z | 2026-11-03 intel_news_it：恢复可达（上轮 HTTP 503） |  |
| SB-109 ite.net.pk | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-110 itkati.com | A | 2 | 0/2 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SB-1102 vienthonggiatot.com | A | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 369 条：2020-08-10T09:07:16 siemens-cable.html；2020-08-10T09:07:16 cap-ket-noi-h |  |
| SB-111 nivoxtech.com | A | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1114 Fikes Media | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-1115 Milliseconds Evolution Limit | A | 2 | 1/1 | 2026-11-02T09:40:28Z | 2026-10-23 首轮基线 |  |
| SB-1116 Litech (Pvt) Ltd | A | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+12 −4 行 | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-1122 comtinu.ru | A | 6 | 4/2 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SB-1134 conexionderedes.com | A | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：更新 7 条：conexionderedes.com（2026-11-05T09:45:32 → 2026-11-06T09:39:21）；tienda（2026 | WhatsApp |
| SB-1135 raisecom.su | A | 3 | 0/3 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SB-1136 fiberoptics4sale.com | A | 4 | 3/1 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SB-1138 devray.in | A | 3 | 2/1 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SB-119 wirestar.net | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-29 home：内容变化：+130 −1 行 |  |
| SB-122 Tera Technologies and Engine | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-24 首轮基线 |  |
| SB-129 Addon Technology Ltd | A | 1 | 1/0 | 2026-10-26T07:56:19Z | 2026-10-23 首轮基线 |  |
| SB-130 Bonmag International | A | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-131 DE secure | A | 5 | 3/2 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+1 −1 行 | LinkedIn |
| SB-132 F.A.S.T | A | 6 | 4/2 | 2026-10-31T08:34:28Z | 2026-10-29 news_1：内容变化：+78 −1 行 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-134 Kassaba Systems | A | 4 | 1/3 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： 8lbpdn-4-4-komplekt-za-videonablyudenie-longse； dvoina-vanshna-wifi-kam |  |
| SB-137 ORAL GUVENLIK | A | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-140 ag-bilgisayar.com | A | 4 | 2/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook |
| SB-143 broadstar.com | A | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 | Facebook、LinkedIn |
| SB-144 bsdnetworks.com | A | 3 | 2/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-149 klasnet.com.tr | A | 4 | 2/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-151 optiwatch monitoring solutio | A | 4 | 0/4 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、X/Twitter |
| SB-153 sinerjik | A | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-24 首轮基线 |  |
| SB-160 linx-com.com | A | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+11 −11 行 | X/Twitter、Facebook、LinkedIn |
| SB-163 skeo.ru | A | 8 | 2/6 | 2026-11-01T09:25:59Z | 2026-11-01 news_2：内容变化：+1 −1 行 | Facebook、X/Twitter |
| SB-164 unea-x.com | A | 4 | 2/2 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+2 −4 行 |  |
| SB-167 ONSIS ELEKTRONIK | A | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 2 条：Fri, 06 Nov 2026 08 Imagine Earth Pre-Cracked — Multilingual；Thu, 05 Nov | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-169 agsplus.in | A | 2 | 0/2 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SB-173 inaxsys.com | A | 3 | 2/1 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+3 −1 行 |  |
| SB-175 mbtc.com.sa | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-185 Zeytek | A | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 19 条：2021-04-01T20:17:50 Zeytek_Katalog.pdf；2021-03-21T13:59:57 Zeytek_Premium |  |
| SB-189 vintronsmartvision.com | A | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 46 条： 3-0mp-ip-h-265-new-outdoor-big-camera； 1-8-port； 1-4-port-180m-distance- | Facebook、LinkedIn、Instagram |
| SB-193 Dema Vertriebs GmbH | A | 4 | 2/2 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+93 −22 行 |  |
| SB-201 Elsi | A | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-31 news_1：内容变化：+0 −2 行 | Facebook、LinkedIn、WhatsApp |
| SB-225 CESS Govalik | A | 3 | 0/3 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SB-226 HANCHANG Infotech CO.,LTD | A | 3 | 1/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-243 hfcl.com | A | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T07:30:49 AI Racks Need Up to 36x More Fiber. Can Data Centers K | LinkedIn、Instagram、Facebook、X/Twitter |
| SB-246 isnetworks.pl | A | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook |
| SB-248 nellyssecurity.com | A | 4 | 3/1 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+1186 −1 行 | X/Twitter、Facebook、Instagram |
| SB-255 switchtek | A | 4 | 3/1 | 2026-10-31T08:34:28Z | 2026-10-28 news_1：内容变化：+1161 −1 行 |  |
| SB-256 tvprzemyslowa.pl | A | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 |  |
| SB-267 bio-cognitive.com | A | 4 | 3/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-274 fiberix.com.tr | A | 3 | 1/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-315 stc-vietnam.com | A | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： stc-vietnam.com； gioi-thieu.html； danh-sach-san-pham.html； bang-gia.htm |  |
| SB-326 PROXEET LIMITED | A | 4 | 3/1 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | X/Twitter、Facebook、Instagram、LinkedIn |
| SB-331 retelem-dz.com | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-342 Sure Transport | A | 4 | 3/1 | 2026-11-05T09:39:48Z | 2026-11-05 intel_careers：内容变化：+0 −32 行 |  |
| SB-343 Zekko Tech Private Limited | A | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 104 条：2018-07-30T20:27:42 www.zekko.co.in；2018-07-30T20:27:42 index.html；2018- |  |
| SB-359 larch-networks.com | A | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook |
| SB-360 longtek | A | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook |
| SB-367 thuyluc.com | A | 4 | 2/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-388 fhguvenlik.com | A | 4 | 2/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-389 hiperonline.com | A | 4 | 1/3 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-392 makrosisas.com.tr | A | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 483 条：2026-11-06 wv-s66700-z3ln；2026-11-06 wv-s66700-z3l；2026-11-06 wv-s66700- |  |
| SB-447 automationsystem.in | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-24 首轮基线 | LinkedIn、Facebook、Instagram |
| SB-451 e-saudi.net | A | 1 | 0/1 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-461 EMOS | A | 5 | 3/2 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+2 −2 行 | Facebook |
| SB-474 casecomms.com | A | 6 | 6/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-485 n-itus.com | A | 3 | 0/3 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-487 npotelecom.ru | A | 3 | 0/3 | 2026-11-03T09:43:52Z | 2026-10-23 首轮基线 |  |
| SB-529 dmsimfg.com | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-29 home：内容变化：+30 −1 行 |  |
| SB-542 lanopia.de | A | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 35 条： audio-to-fiber-converter； 12g-3g-sdi-video-sfp； usb-to-fiber-converter；  |  |
| SB-599 symanitron.ru | A | 4 | 2/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-630 CORE IT SOLUTIONS | A | 4 | 3/1 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook |
| SB-641 apolloinfoways.in | A | 2 | 1/1 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+0 −1 行 |  |
| SB-692 Anda Telecom | A | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SB-696 aironix.co.il | A | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+0 −32 行 |  |
| SB-767 itmsystems.co.uk | A | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-24 首轮基线 | Facebook |
| SB-787 tccomm.com | A | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 400 条： BECOL； Serial-Over-T1-E1-Multiplexer； TDM-over-IP-Jumboswitch； Fiber； N | LinkedIn |
| SB-826 versitron.com | A | 6 | 5/1 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter、LinkedIn |
| SB-831 actelis.com | A | 9 | 7/2 | 2026-11-02T09:40:28Z | 2026-11-02 news_2：内容变化：+1 −1 行 | Facebook、X/Twitter、LinkedIn |
| SB-869 futurist.com.pk | A | 2 | 0/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-905 TELTRONIX ／ BRITICOM | A | 3 | 1/2 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-910 etictelecom.com | A | 5 | 3/2 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+14 −15 行 |  |
| SB-924 Intracom Middle East FZ-LLC | A | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+331 −1 行 | LinkedIn、X/Twitter、Facebook |
| SB-949 ksm.com.au | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-29 home：内容变化：+2 −1 行 |  |
| SB-970 EION Inc | A | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-982 mcss.co.kr | A | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 491 条： index； 18； intro； notice； 22； system； 46； ito… | Instagram、Facebook |
| SB-984 olsontech.com | A | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SB-988 Infinity Hardware | A | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+209 −1 行 |  |
| SC-002 Intelligent | A | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-097 Three Lines Company | A | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 28 条：2026-09-02T11:08:41 electronics-diagnostic-and-repair-workshops；2026-09-0 | LinkedIn |
| SC-1056 cloudinfotech.co.in | A | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-1200 futurepointt.com | A | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-1371 mywatchdog.in | A | 2 | 1/1 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+0 −1 行 |  |
| SC-1399 team5tech.com | A | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-1623 shopfiber.co.za | A | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+78 −86 行 |  |
| SC-1657 San Telequip Pvt. Ltd. | A | 7 | 6/1 | 2026-11-04T09:30:29Z | 2026-11-04 news_2：内容变化：+5 −1 行 | LinkedIn |
| SC-1771 telexcell.com | A | 2 | 1/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-190 Crontr Technology | A | 3 | 1/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+38 −38 行 |  |
| SC-1904 optimal.com.ph | A | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-1942 satvision-cctv.ru | A | 8 | 6/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SC-2513 microtech.net.pk | A | 3 | 2/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-2802 Euro Security Solutions Ltd | A | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2904 firsttech.co.za | A | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+96 −1 行 |  |
| SC-371 Visiotech | A | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 687 条： hiwatch-hikvision-40； cámaras-domo-85； cámaras-compactas； anviz； hiwatc |  |
| SC-584 nambasoftware.com.br | A | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SA-013 alfa.com.tw | B | 2 | 2/0 | 2026-11-02T09:40:28Z | 2026-11-02 home：内容变化：+94 −82 行 | X/Twitter、LinkedIn |
| SA-017 parallaxdigital.co.uk | B | 8 | 8/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+8 −8 行 | Facebook、X/Twitter、LinkedIn、Instagram |
| SA-018 Sewell | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：更新 1 条：Philadelphia developer wins bid for South Jersey site, plans（Wed, 28 | Facebook、Instagram、X/Twitter |
| SA-019 allnet.de | B | 3 | 3/0 | 2026-11-02T09:40:28Z | 2026-11-02 home：内容变化：+0 −1 行 |  |
| SA-022 Addon Computer Products | B | 6 | 6/0 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn |
| SA-024 Cable Distribution Services | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 intel_news_en：新增 1 条：Wed, 22 Jul 2026 07 #e4mExclusive: TRAI moves to reclaim role in TV  | Facebook、LinkedIn |
| SA-037 aeconnect.co.in | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T02:30:15 Happy Dhanteras | Facebook、Instagram、X/Twitter、LinkedIn |
| SA-038 dncsolutions.co.in | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SA-040 success-network.co.th | B | 4 | 0/4 | 2026-10-31T08:34:28Z | 2026-10-31 feed_auto：恢复可达（上轮 HTTP 403） | Facebook |
| SA-041 lightoptics.pl | B | 6 | 6/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+7 −2 行 | Facebook、LinkedIn |
| SA-044 dymec.com | B | 6 | 6/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、LinkedIn |
| SA-046 ipcampower.com | B | 3 | 3/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SA-052 bsn-system.com | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SA-056 B&S electronics | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 821 条：2020-03-07T09:04:12 tcctv-1205-4c；2020-03-13T09:18:59 tcctv-1210-9c；2020 |  |
| SA-057 Born SPb LLC | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+20 −20 行 |  |
| SA-062 ipns-uae.com | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SA-065 smbit.co.il | B | 6 | 6/0 | 2026-10-29T15:11:51Z | 2026-10-29 news_2：内容变化：+1 −1 行 | Facebook、LinkedIn |
| SA-069 bptehno.ru | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-10-23 首轮基线 |  |
| SA-073 vicomsecurity.com | B | 3 | 2/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、Instagram |
| SA-075 Falke security | B | 7 | 7/0 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter |
| SA-081 4power.it | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+30 −29 行 | Facebook、Instagram、LinkedIn |
| SA-083 kyma.it | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+4 −1 行 |  |
| SA-084 Eds protection technology | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 486 条：2021-03-16 eds-elektronik-31-yasinda；2021-08-09 en54-sertifikalı-eds-kon | Facebook、X/Twitter、Instagram、LinkedIn |
| SA-087 norelcosafecam.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −0 行 |  |
| SA-088 ute.de | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： 16-port-dvi-video-splitter-vopex-dvis-16-von-nti.html； 16-port-kvm-over |  |
| SA-089 lancomat.cz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+166 −166 行 | LinkedIn |
| SB-004 fhn-na.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-005 rovez.sk | B | 4 | 4/0 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+2 −2 行 |  |
| SB-008 Abdulaziz Al Jowasem | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-009 sicurmax.com | B | 4 | 4/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-011 greentechme.net | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 intel_news_en：新增 1 条：Mon, 27 Jan 2025 16 Dior And Lewis Hamilton B44 Blade Gradient Green |  |
| SB-012 xcam.cz | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-013 synchcom.com.pk | B | 4 | 4/0 | 2026-11-03T09:43:52Z | 2026-10-23 首轮基线 |  |
| SB-014 ITS, S.L.-S.B.T. | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-015 suministros-industriales.es | B | 6 | 6/0 | 2026-11-03T09:43:52Z | 2026-11-03 feed_auto：新增 1 条：Mon, 02 Nov 2026 09 Actuadores eléctricos: 5 errores habituales al elegi | WhatsApp |
| SB-016 Richard Jackson | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-017 Securitytec | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 478 条： www.securitytec.co.uk；2022-05-13T21:00:54 our-products.html；2022-05-01T | Facebook、X/Twitter |
| SB-019 aetektec.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −1 行 | LinkedIn |
| SB-021 LOOP TELECOM | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：新增 2 条：Thu, 05 Nov 2026 11 APAC Opto Electronics Inc. (4908.TWO) Seasonal r | LinkedIn |
| SB-023 itk.co.th | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： 400g-aec-cable.html； tconnect-400gbps-transceiver.html； tconnect-40gbps |  |
| SB-024 ERSTECH | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-23 首轮基线 |  |
| SB-025 SIPe | B | 6 | 6/0 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+2 −0 行 | Instagram、LinkedIn |
| SB-026 Safe-tech CCTV systems Swede | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-028 fibotelecom.ru | B | 4 | 4/0 | 2026-10-27T08:02:45Z | 2026-10-27 news_2：内容变化：+6 −6 行 |  |
| SB-029 ETRADINGKOREA Co., Ltd | B | 3 | 3/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-030 Medias-Com'S | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-28 sitemap：新增 10 条： medias-coms.ch； entreprise.html； ecrans-digitaux.html； enseignes.html； a |  |
| SB-032 PIOLINK | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 25 条：2023-02-02T09:14:30 Web-Application-Firewall.php；2023-02-02T09:14:30 Comp | LinkedIn、Facebook |
| SB-033 Marvel ITCS Bahrain | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+3 −0 行 | LinkedIn、Facebook、Instagram、Facebook |
| SB-034 TJ Computer | B | 1 | 0/1 | - |  |  |
| SB-035 Thimphu Techpark | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 intel_news_en：新增 1 条：Tue, 22 Jun 2021 07 What are the entrepreneurship programmes and ini |  |
| SB-036 inthouse.eu | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、Instagram |
| SB-037 pulsar.kz | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 366 条： videokamera-s-ik-podsvetkoy-ds-tcg406-e； zkteco-terminal-raspoznavaniya |  |
| SB-039 zelax.ru | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 547 条：2021-10-27T16:35:26 order-delivery；2018-11-02T15:02:17 routers-switches； |  |
| SB-041 Telcam Fire&securoty Ltd | B | 4 | 4/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | X/Twitter、Facebook、LinkedIn、WhatsApp |
| SB-042 regalsecurity.co.za | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+78 −3 行 |  |
| SB-044 Win-Tech Alliance Ltd | B | 2 | 2/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-045 advancedigital.co.in | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：新增 6 条：Thu, 05 Nov 2026 14 StormGeo Partners with China Classification Soci |  |
| SB-046 domoticalia.es | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+36 −36 行 |  |
| SB-048 Almaks Security SystemsGospo | B | 6 | 2/4 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 | Instagram、Facebook、LinkedIn |
| SB-049 MULTILINK (PVT) LTD | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-050 PT. ANUGERAH | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp |
| SB-051 Prestige Satellites Communic | B | 3 | 3/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-052 excellent data communication | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-054 testronix.ph | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、Instagram、LinkedIn |
| SB-058 SABMARtv | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-060 bargas.ru | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+2 −2 行 |  |
| SB-061 megatelindustries.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 166 条：2026-10-27T12:07:18 gico.html；2026-10-27T12:07:18 dst1fico.html；2026-10- |  |
| SB-062 Aarya ITES Pvt. Ltd. | B | 4 | 4/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-064 amitytechnologies.co.in | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、LinkedIn |
| SB-065 ayk.com.pk | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、LinkedIn |
| SB-066 comtec.com.vn | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+71 −66 行 |  |
| SB-067 crec.com.ph | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 148 条：2025-08-06 citicore-solar-capacity-accelerates-to-13gw-early-next-year；2 |  |
| SB-068 ict-integrators.com | B | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+69 −226 行 | Facebook |
| SB-069 mutexsystemsltd.com | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | WhatsApp、LinkedIn、Facebook、X/Twitter、Instagram |
| SB-070 neowine | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+16 −15 行 |  |
| SB-072 technosys.co.in | B | 4 | 3/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-073 ANB rimex | B | 7 | 7/0 | 2026-11-02T09:40:28Z | 2026-11-02 sitemap：新增 1 条：2026-11-02 noel-2026 | Facebook、LinkedIn |
| SB-075 Gmka | B | 4 | 4/0 | 2026-11-01T09:25:59Z | 2026-10-29 home：内容变化：+72 −1 行 |  |
| SB-076 IST surveillance | B | 2 | 2/0 | 2026-11-01T09:25:59Z | 2026-11-01 sitemap：新增 1 条： lander |  |
| SB-078 Sitis Sarl | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-080 cyber-tec.net | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-081 dabos.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-082 voltechelektronik.com | B | 1 | 0/1 | - |  |  |
| SB-083 MERIT LILIN ENT. CO., LTD. | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： tw； support； worldwide； solution； case-studies； blog； ndaa； where-to-bu | LinkedIn |
| SB-084 AD-NET TECHNOLOGY CO., LTD. | B | 5 | 5/0 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter、LinkedIn |
| SB-086 TAILYN | B | 5 | 5/0 | 2026-11-05T09:39:48Z | 2026-11-05 intel_news_en：新增 1 条：Tue, 03 Nov 2026 00 Tainet Communication System Corp. (4905.TWO) Sea |  |
| SB-087 ASSMANN ASIA | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-088 EDIMAX | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 intel_news_en：新增 2 条：Thu, 05 Nov 2026 09 EDIMAX Technology Co., Ltd. (3047.TW) Seasonal r |  |
| SB-089 Winsonic Electronics Co., Lt | B | 2 | 2/0 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-090 adlerss.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-091 fingerprint-access-control.c | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+149 −1 行 |  |
| SB-092 spacetronik.pl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+63 −4 行 |  |
| SB-094 maxcomcorp.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-095 mtechnology.it | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 131 条： speciali-e-per-applicazioni-industriali-ip-camera-light-hunt-megapixel- |  |
| SB-096 ovisscctv.com | B | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+169 −1 行 |  |
| SB-097 lansan.com.tr | B | 4 | 4/0 | 2026-11-03T09:43:52Z | 2026-11-03 news_1：内容变化：+31 −15 行 | Instagram、X/Twitter、Facebook |
| SB-098 nexxtsolutions.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-099 rocstor.com | B | 3 | 0/3 | 2026-11-02T09:40:28Z | 2026-10-25 feed_auto：恢复可达（上轮 HTTP 403） | Facebook、X/Twitter、LinkedIn、Facebook |
| SB-100 telkolink.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2015-03-30T11:00:21 1040G.pdf；2014-12-03T11:16:14 10G-SFP.pdf；2013-12-04 | LinkedIn、Instagram、X/Twitter、Facebook |
| SB-1000 alphaelettronica.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-11-06 spine.html；2026-11-06 prese.html；2026-11-06 spine-vaschetta-d |  |
| SB-1001 altelix.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1002 amplicon.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −0 行 | LinkedIn、X/Twitter、Instagram |
| SB-1003 aplusnet.de | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+456 −2 行 |  |
| SB-1004 arpeo.pl | B | 5 | 5/0 | 2026-11-01T09:25:59Z | 2026-10-29 feed_auto：新增 2 条：Thu, 29 Oct 2026 09 Jak dobrać dławnicę kablową? Najważniejsze parametry |  |
| SB-1005 asit.it | B | 4 | 4/0 | 2026-10-24T04:35:40Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SB-1006 audio.com.tr | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、Instagram |
| SB-1007 avnordic.se | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+1 −0 行 | Facebook、LinkedIn |
| SB-1008 avstek.fi | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook |
| SB-1009 batna24.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 |  |
| SB-101 AVICAM Ltd. | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook |
| SB-1010 bayiden.com.tr | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-11-06 philips-3dtv37860ix-37-inc-2-adet-tv-led-bar；2026-11-06 samsu | Facebook、Instagram、X/Twitter |
| SB-1011 binarteknik.se | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+10 −10 行 | Instagram、LinkedIn |
| SB-1012 bitstreamcore.com | B | 1 | 0/1 | - |  |  |
| SB-1013 bizsyscon.com | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter、LinkedIn |
| SB-1014 bluenote.ro | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-24 home：内容变化：+3 −266 行 |  |
| SB-1015 br-network-shop.de | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+502 −223 行 |  |
| SB-1016 cae-groupe.com | B | 6 | 3/3 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+108 −9 行 | Facebook、LinkedIn |
| SB-1017 cellco.com.pl | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-1018 coeldistribution.it | B | 5 | 5/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+23 −46 行 | LinkedIn、Facebook |
| SB-1019 connectixcablingsystems.com | B | 2 | 1/1 | 2026-11-03T09:43:52Z | 2026-11-03 intel_news_en：新增 1 条：Thu, 07 Mar 2013 08 Microsoft VHDX format: Understanding benefits, c |  |
| SB-102 Denso Electronics Ltd | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1020 cratsol.ae | B | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+202 −1 行 |  |
| SB-1021 cyberbajt.pl | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+18 −18 行 |  |
| SB-1022 danbit.dk | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+5 −5 行 | Instagram、LinkedIn |
| SB-1023 dipol.pt | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+183 −1 行 | Facebook |
| SB-1024 dowtechnologies.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-05-21 12volt-closeouts；2026-08-31 12volt；2026-08-31 custom-integrat |  |
| SB-1025 elfon.com.pl | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook |
| SB-1027 everbesthk.com | B | 4 | 4/0 | 2026-11-03T09:43:52Z | 2026-10-29 news_2：内容变化：+2 −4 行 |  |
| SB-1028 fibersavvy.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | X/Twitter、Facebook、Instagram、LinkedIn |
| SB-1029 fibersystem.com | B | 6 | 4/2 | 2026-11-03T09:43:52Z | 2026-11-03 intel_news_sv：恢复可达（上轮 HTTP 503） | Facebook、LinkedIn |
| SB-1030 fibertronics.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+143 −1 行 | Facebook、LinkedIn |
| SB-1032 foppex.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+200 −1 行 |  |
| SB-1033 garmasl.com | B | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 youtube：新增 1 条：2026-10-29T11:19:48 ATMI AQUA XL: boya de nivel omnidireccional para aguas | Facebook、LinkedIn |
| SB-1034 gogss.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1035 gponnetwork.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1036 grinsrl.it | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1037 hightrade-international.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-1038 icecom.is | B | 2 | 1/1 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+1 −1 行 |  |
| SB-1039 ico.de | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+4 −4 行 |  |
| SB-1040 icpdas.ro | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1041 intshop.pl | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1042 iotkomponenty.sk | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1043 ipcamerawebwinkel.nl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+23 −0 行 | Facebook、Instagram |
| SB-1044 ipcctv.ch | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2008-07-23T23:01:11 km8100mdw.pdf；2008-07-23T23:01:15 km8100mxw.pdf；2008 | Facebook |
| SB-1045 itm-components.co.uk | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_2：内容变化：+153 −1 行 | LinkedIn |
| SB-1046 ivolta.pl | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+29 −31 行 | Facebook、LinkedIn |
| SB-1047 kamsys.pl | B | 6 | 4/2 | 2026-11-01T09:25:59Z | 2026-10-27 news_2：内容变化：+3 −0 行 | Facebook |
| SB-1048 kargor.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1049 kdelectronics.ie | B | 2 | 2/0 | 2026-11-01T09:25:59Z | 2026-11-01 home：内容变化：+321 −1 行 | Instagram、LinkedIn |
| SB-105 cenova.com.tr | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 | Instagram、Facebook、X/Twitter |
| SB-1050 keydence.com | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp |
| SB-1051 klemsan.com.tr | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1052 lan.hu | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： lan.hu；2022-11-08T13:45:02 termekek-177；2026-11-06T10:11:27 kabelcsupas | Facebook、Instagram、LinkedIn |
| SB-1053 lichtleiterkabel.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1054 luxritesecurity.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-10-12T14:01:00 contact；2024-01-16T16:21:00 careers；2026-05-06T15:16 | Facebook、Instagram、LinkedIn |
| SB-1055 marcomweb.it | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1056 mikrodev.com | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Facebook |
| SB-1057 mondoplast.ro | B | 3 | 1/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+181 −146 行 | Facebook |
| SB-1058 multiproject.com.pl | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+42 −42 行 |  |
| SB-1059 neteon.net | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 97 条：2026-06-12T15:59:40 search；2026-06-12T15:59:40 moxa；2026-06-12T15:59:41 c | LinkedIn |
| SB-106 citicalls.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+244 −0 行 | Facebook |
| SB-1060 norteh.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1062 −1 行 |  |
| SB-1061 obserwuj.pl | B | 3 | 1/2 | 2026-11-05T09:39:48Z | 2026-11-05 sitemap：新增 820 条： www.obserwuj.pl； lista-kategorii.html； lista-producentow.html； blog.htm | Instagram |
| SB-1062 odoo.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 2 条：2026-11-05T19:40:27 Webinaire - Odoo 20 – Découvrez les nouvelles innovati | X/Twitter、LinkedIn、Instagram、Facebook |
| SB-1063 pc-industriali.it | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-1064 portdepo.ru | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-10-24 首轮基线 |  |
| SB-1065 poznan.pl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+99 −9 行 | Facebook、Instagram |
| SB-1066 pramoninisrysys.lt | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 sitemap：新增 66 条： ranks_badges； rating； users； info； all； terms； livechat； slides… |  |
| SB-1067 raytelsecurity.com | B | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+2 −2 行 | LinkedIn、Facebook |
| SB-1068 rbline.pl | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+774 −75 行 |  |
| SB-1069 reweb.it | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn |
| SB-107 glm.ge | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook |
| SB-1070 safeguard.se | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、Instagram |
| SB-1071 scada-hmi.it | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+14 −14 行 | Facebook |
| SB-1072 securame.com | B | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+27 −7 行 |  |
| SB-1073 sensoguard.com | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Facebook、X/Twitter |
| SB-1074 setik.biz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-03-31 407-video-surveillance；2025-03-31 407-videosurveillance；2025- |  |
| SB-1075 silmarelectronics.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1076 simplifinetworks.com | B | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 806 条：2026-10-15T11:19:09 ruijie-reyee-rg-cs83-12gt4xs-p-12-port-1ge-rj45-laye | Facebook、X/Twitter、LinkedIn |
| SB-1077 soft-tronik.ru | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+2 −2 行 |  |
| SB-1078 solimedia.net | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+14 −14 行 | Facebook、X/Twitter、LinkedIn |
| SB-1079 spesaelettrica.it | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-108 gwsecurityusa.com | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、Instagram、X/Twitter |
| SB-1080 sphinxcomputer.de | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-09-02T13:40:47 rma.php；2025-09-02T13:40:47 ueber.php；2025-09-02T13: |  |
| SB-1082 standardaudio.se | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-29 home：内容变化：+376 −3 行 |  |
| SB-1083 systemfabricworks.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1084 targoncavilla.com | B | 4 | 4/0 | 2026-11-03T09:43:52Z | 2026-10-24 首轮基线 | Facebook、Facebook |
| SB-1085 tayama.pl | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-1086 teamtelecom.ro | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、LinkedIn |
| SB-1087 tehnoelectric.ro | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1088 tipteh.com | B | 6 | 1/5 | 2026-11-01T09:25:59Z | 2026-10-31 feed_auto：新增 1 条：Fri, 30 Oct 2026 06 Turck MARGEE Programmable Block I/O Modules | Facebook、LinkedIn |
| SB-1089 tpnet.com.br | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1090 tramaweb.com.br | B | 5 | 5/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+37 −37 行 | Facebook、Instagram、LinkedIn、X/Twitter |
| SB-1091 triotronik.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+438 −238 行 |  |
| SB-1092 unifibre.it | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+78 −3 行 | Facebook、LinkedIn |
| SB-1093 vercoma.nl | B | 5 | 3/2 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+1 −1 行 | Facebook、LinkedIn |
| SB-1094 videobits.co.uk | B | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+4 −1 行 |  |
| SB-1095 vidom.pl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+191 −1 行 | Facebook、Instagram |
| SB-1096 westpennwire.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、X/Twitter |
| SB-1097 yatun.cz | B | 5 | 1/4 | 2026-11-01T09:25:59Z | 2026-10-28 home：内容变化：+5 −5 行 | LinkedIn、Instagram、Facebook |
| SB-1098 zintronic.pl | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1099 zxtech.co | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Instagram |
| SB-1100 IT Broadcast & Cyber Securit | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-1103 ara.com.bd | B | 1 | 0/1 | - |  |  |
| SB-1104 Agility Elektrotekniks Pvt L | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-1105 Suraj Katte | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-1108 Sunmars Enterprises | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-1110 amineachoura21@gmail.com | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-1117 Switchcom Distribution (Pty) | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn、WhatsApp、X/Twitter |
| SB-1118 Education HMO / CSPE（educati | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SB-1119 noktaelektronik.net | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-112 opax.com | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+396 −95 行 |  |
| SB-1121 technetix.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SB-1123 connectec.uk | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+3 −3 行 | Facebook、X/Twitter、LinkedIn |
| SB-1124 fonex.pl | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+187 −6 行 |  |
| SB-1125 globall.ca | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook、LinkedIn |
| SB-1126 klinger.fi | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 feed_auto：新增 1 条：Wed, 04 Nov 2026 09 Avoin työpaikka: Tekninen myyjä anturitiimiin, hakua | LinkedIn |
| SB-1127 linhawstore.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 900 条： confirmation； return； info； quick_order_confirm； quick_order_review； qu |  |
| SB-1128 losan.cz | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-1129 redcorp.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+0 −1 行 | Facebook、X/Twitter、LinkedIn |
| SB-113 regionprof.ru | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-1130 cnstech.gr | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 305 条：2025-10-17T12:31:08 ?page=10；2025-10-17T12:31:08 ?page=168；2025-10-17T12 | Facebook、Instagram、LinkedIn、X/Twitter |
| SB-1131 marugged.com | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | X/Twitter、Facebook、LinkedIn、Instagram |
| SB-1132 nedic.aleksandar@gmail.com | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-1133 netram.de | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-1137 Infotec Comercio de Equipame | B | 2 | 0/2 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SB-1139 arnoldomohr@gmail.com | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-114 swift.net.pk | B | 2 | 0/2 | - |  |  |
| SB-116 Pyramid Enterprises | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-117 Softline Technology | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-118 genrov.com | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-24 首轮基线 |  |
| SB-120 Pronet Connectivity (Pvt) Lt | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、Instagram |
| SB-121 STORM ICT | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-123 tdtorus.ru | B | 4 | 0/4 | 2026-11-01T09:25:59Z | 2026-11-01 sitemap：新增 819 条：2026-05-07 ibpdlakotla；2026-04-30 ibpdlaofisa；2026-04-30 ibpdlazagorodno |  |
| SB-124 telconet.net | B | 3 | 0/3 | 2026-10-24T07:26:33Z | 2026-10-24 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SB-126 cablewindow.com | B | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 420 条： seguridad-en-vehiculos-monitores-de-vehiculo-monitor-camara-marcha-atra | Facebook、LinkedIn |
| SB-127 izux.es | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+0 −10 行 | Facebook、X/Twitter、LinkedIn、WhatsApp |
| SB-128 orbitadigital.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+269 −290 行 | WhatsApp、Facebook、X/Twitter |
| SB-133 Gigalight Pte ltd | B | 4 | 4/0 | 2026-11-02T09:40:28Z | 2026-11-02 feed_auto：新增 1 条：Mon, 02 Nov 2026 02 2026 Year End Promotion: Five devices. Five strength |  |
| SB-135 LABOR | B | 2 | 2/0 | 2026-10-26T07:56:19Z | 2026-10-24 首轮基线 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-136 Metalog International DMCC | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter |
| SB-138 Volktek | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+5 −5 行 | Facebook、LinkedIn、Instagram |
| SB-139 acusenseteknoloji.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp |
| SB-141 agilenetworks.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook |
| SB-142 airpo.co.id | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-145 digicomm.de | B | 4 | 4/0 | 2026-11-03T09:43:52Z | 2026-11-03 news_2：内容变化：+5 −5 行 |  |
| SB-146 exsys.it | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-147 genieproducts.co.uk | B | 5 | 4/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-148 isrcorp.co.il | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-150 nexxus.cc | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-152 pulsar.pl | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+3 −3 行 | Facebook、LinkedIn、Facebook |
| SB-154 wire.tech | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-156 cyberteam.pl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2016-08-22 25_skyeter18；2016-08-22 27_skyeter13；2016-04-18 28_kabel-h100 | Facebook、X/Twitter |
| SB-157 dci.jp | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-158 diatrend.com | B | 3 | 3/0 | 2026-11-02T09:40:28Z | 2026-11-02 home：内容变化：+6 −6 行 | Instagram、Facebook、LinkedIn、X/Twitter |
| SB-159 elmospa.com | B | 6 | 4/2 | 2026-11-03T09:43:52Z | 2026-10-31 youtube：更新 1 条：EL.MO. Fire Evolution ／ Una nuova era per la sicurezza antin（2026-10-28T09 | Facebook、LinkedIn |
| SB-161 mahanet-jp.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-162 optigo.net | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+3 −3 行 | LinkedIn |
| SB-165 yminc.ca | B | 1 | 0/1 | - |  |  |
| SB-166 Crown Security Solutions | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-168 WIMEX TECHNOLOGIES | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-170 balter.de | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | X/Twitter、Instagram |
| SB-172 consteel-electronics.com | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+12 −12 行 |  |
| SB-174 karerguvenlik.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+14 −14 行 |  |
| SB-176 oksa.co.uk | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-07-15T07:51:17 products；2026-07-14T10:38:50 cart；2026-07-14T10:48:2 | LinkedIn、X/Twitter |
| SB-177 sklep-ecsystem.pl | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+265 −0 行 |  |
| SB-178 wisp.pl | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： k213,monitoring-rejestratory-sieciowe-nvr.html； k265,monitoring-urzadze |  |
| SB-179 CRISPY CREPES | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-180 FOLINE | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Instagram |
| SB-182 NETBOWL PTY LTD | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-184 Vernetzen Pty Ltd | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-187 pelikanbilgisayar.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-188 saf-slk.de | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+3 −0 行 |  |
| SB-190 A Hamson Middle East FZE | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、X/Twitter |
| SB-191 Astkom | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-194 SRI ANNAI BUSINESS ASSOCIATE | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-195 bkgrupe.lt | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-196 extradigital.eu | B | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-10-23T09:00:00 tempered-glass-screen-protectors；2024-11-18T09:00:00 |  |
| SB-197 intellisystem.it | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-198 katalita.lt | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-11-06T05:42:02 mimosa-backhaul-integrated-radio-with-modular-antenn |  |
| SB-199 korekonect.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-10-23 首轮基线 |  |
| SB-200 sysnetcenter.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+9 −9 行 |  |
| SB-202 Engineering Group Contractor | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter、LinkedIn、Instagram、WhatsApp |
| SB-203 PT. Suryatama | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-205 barox.de | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T07:40:01 Integrating DW Spectrum IPVMS into barox Switch Manage | LinkedIn |
| SB-206 brainboxes.com | B | 6 | 6/0 | 2026-11-04T09:30:29Z | 2026-11-04 feed_auto：新增 1 条：Tue, 03 Nov 2026 16 Visit Brainboxes at AEMS! | LinkedIn、X/Twitter |
| SB-207 ccontrols.de | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 28 条：2024-05-16T15:05:18 odm.htm；2024-05-16T15:05:17 about.htm；2024-05-16T15:0 | LinkedIn、LinkedIn |
| SB-208 delock.com | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+33 −29 行 | Facebook |
| SB-209 denwaip.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 sitemap：新增 8 条：2026-10-27 blog.html；2026-10-27 tono.html；2026-10-27 pulso.html；2026-10-29 |  |
| SB-210 deonet.co.kr | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-211 een.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −1 行 | LinkedIn、Facebook、X/Twitter、Instagram |
| SB-212 fti-optronic.com | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-10-24 首轮基线 |  |
| SB-213 kti.de | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Instagram、LinkedIn |
| SB-214 level1.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： level1_en；2022-07-25T05:45:34 vga-cables；2022-07-25T05:45:34 smartphone |  |
| SB-215 lindy.co.uk | B | 2 | 2/0 | 2026-10-27T08:02:45Z | 2026-10-27 home：内容变化：+54 −54 行 |  |
| SB-216 ltsecurityinc.com.au | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+131 −24 行 |  |
| SB-217 microsens.com | B | 5 | 5/0 | 2026-10-27T08:02:45Z | 2026-10-27 news_2：内容变化：+3 −4 行 | LinkedIn、LinkedIn |
| SB-218 nag.ru | B | 8 | 6/2 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+61 −13 行 |  |
| SB-219 sieraelectronics.com | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-220 sun-flowers.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-221 tyconsystems.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+3 −1 行 | LinkedIn、Facebook、X/Twitter、Instagram |
| SB-223 2mtechnology.net | B | 3 | 3/0 | 2026-11-01T09:25:59Z | 2026-11-01 home：内容变化：+258 −1 行 | Facebook、LinkedIn、LinkedIn、X/Twitter |
| SB-224 Arsenal TV | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-227 NKF wireless internet and se | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-228 Negoh-Op | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-229 TESCOM COMPANY LIMITED | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-230 adin.it | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+282 −1 行 | Facebook、LinkedIn |
| SB-231 advance.technology | B | 5 | 4/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-232 aixontec.com | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+2 −2 行 | Facebook、Instagram、LinkedIn |
| SB-233 avycon.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+3 −3 行 |  |
| SB-234 benzotronic.it | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-235 bositaly.it | B | 6 | 6/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Facebook |
| SB-236 congtyminhphuoc.vn | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 420 条：2024-11-13T01:28:51 kadita；2024-11-13T01:28:51 cap-mang-1；2024-11-13T01: |  |
| SB-237 dalessandris.it | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+41 −22 行 |  |
| SB-238 digimax.it | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-09-17T00:06:23 14D-12D05NNL；2025-09-17T00:06:23 14D-12D05NNL；2025-0 |  |
| SB-239 empicstar.com | B | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+401 −91 行 |  |
| SB-240 frogfish.de | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 |  |
| SB-241 gluszek.tomasz@gmail.com | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-242 grothe.de | B | 6 | 3/3 | 2026-11-01T09:25:59Z | 2026-10-29 news_1：内容变化：+0 −25 行 | Facebook、Instagram |
| SB-244 innowatt.it | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+3 −3 行 | Facebook、Instagram、LinkedIn |
| SB-245 iotech-italia.net | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-247 jpg.lt | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 637 条： sma-male-uzspaudziama-jungtis-rg174-kabeliui； industrinis-4glte-marsrut | Facebook |
| SB-249 netbergtw.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-250 pf-electronic.pl | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-251 pixcom.ae | B | 7 | 6/1 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、Instagram、LinkedIn、X/Twitter、Facebook |
| SB-252 platinumcctv.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 220 条：2026-11-05 tvi-analog-turret-camera.html；2026-11-05 hd-tvi-ptac344-camer | X/Twitter、Instagram |
| SB-253 provision-isr.com | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+456 −104 行 |  |
| SB-254 sicurtecnicanapoli.it | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+196 −1 行 |  |
| SB-257 voxplus.it | B | 7 | 5/2 | 2026-11-05T09:39:48Z | 2026-11-05 news_2：内容变化：+6 −3 行 | LinkedIn |
| SB-258 Arfanet | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-259 Dourte | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+117 −1 行 |  |
| SB-260 HK GmbH | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook |
| SB-261 RecTec servis, s.r.o. | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-262 Software Effect Enterprises, | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-263 TECside BV | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 112 条：2026-10-26 radio1-2022-studio-vrt；2026-10-26 villa-sporza；2026-10-26 vil | Facebook、Instagram、LinkedIn |
| SB-264 TIER1 DATA SYSTEMS LIMITED | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-265 Vdeotronic AG | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、LinkedIn、X/Twitter |
| SB-266 axilogi.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+41 −39 行 | Facebook、X/Twitter、Instagram |
| SB-268 bulutlarbilisim.com | B | 1 | 0/1 | 2026-10-27T08:02:45Z | 2026-10-24 首轮基线 |  |
| SB-269 contradata.it | B | 4 | 2/2 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+3 −3 行 |  |
| SB-270 damixsat.pl | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+547 −25 行 | Facebook |
| SB-271 dodicelettronica.it | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+8 −8 行 | Facebook、Instagram、LinkedIn |
| SB-272 electronikhouse.it | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+39 −39 行 | Facebook |
| SB-273 eretekne.com | B | 1 | 0/1 | 2026-10-28T08:44:48Z | 2026-10-23 首轮基线 |  |
| SB-275 gelecekbt.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+675 −88 行 | WhatsApp、Facebook、Instagram、X/Twitter、LinkedIn |
| SB-276 hanelektronik.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+35 −35 行 | Facebook、Instagram、X/Twitter |
| SB-277 instantbyte.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+166 −13 行 | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-278 lanmus.com | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-31 youtube：新增 1 条：2026-10-30T12:19:44 Lanmus | WhatsApp、Facebook、Instagram、LinkedIn、X/Twitter |
| SB-279 marlexconexion.com | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-280 metcom.com.tr | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-281 multiGuide GmbH | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-282 nfsteknoloji.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 413 条： nfs； p-iris-lens.html； 13-mp-ahd-ir-bullet-kamera.html； samsung-wisenet | Facebook、X/Twitter、LinkedIn |
| SB-283 oncuguvenlik.com.tr | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-03-31 yeni-urunler；2026-04-06 urunlerimiz；2026-04-01 ip-kameralar；2 |  |
| SB-284 provowire.com | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+306 −1 行 |  |
| SB-285 rfteknoloji.com.tr | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-286 rimaelektronik.com | B | 2 | 2/0 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+43 −42 行 | X/Twitter、LinkedIn |
| SB-287 sea-srl.it | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+55 −54 行 |  |
| SB-288 secomp-international.com | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-289 sisav.it | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+8 −8 行 | LinkedIn、LinkedIn |
| SB-290 solpakutec.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-291 technosources.ca | B | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+2 −243 行 |  |
| SB-292 teslanetworks.be | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-293 virtualprotective.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-294 viva bilgisayar | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-295 wicomsolutions.it | B | 7 | 5/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook |
| SB-296 BHS Telecom 视频比较多一些 | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-297 Chisinau, Ion Creanga 66, Ch | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-298 VNS technologies | B | 6 | 5/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | X/Twitter、Facebook、LinkedIn、LinkedIn、Facebook |
| SB-299 ayezeegroup.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、WhatsApp |
| SB-301 ebatek.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −1 行 | Facebook、Instagram、LinkedIn |
| SB-302 turkuaz | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-303 watchnetinc.com | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、LinkedIn、Instagram |
| SB-304 AADONA COMMUNICATION Pvt. Lt | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-305 Bits&Byte CONSULTING PVT LTD | B | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 3 条： privacy-policy； terms-conditions； aup | WhatsApp、LinkedIn、Instagram、Facebook |
| SB-307 Saxco Marketing Sdn Bhd | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-308 alconlink.com | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 210 条：2026-07-04T06:31:52 253；2026-07-04T06:31:52 219；2026-07-04T06:31:52 95；2 | Facebook、X/Twitter、Instagram |
| SB-309 alternetivo.cz | B | 5 | 3/2 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+59 −4 行 | Facebook、LinkedIn、X/Twitter |
| SB-310 arcanlibya.com | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-311 dipolnet.cz | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+136 −0 行 | Facebook |
| SB-312 fibercomtelecoms.com | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-313 intellcom.net | B | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-12-01 Circuit-Breakers；2025-12-01 %E1%83%93%E1%83%98%E1%83%A4%E1%83 |  |
| SB-314 rspotsolutions.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 23 条： blog； our-blog-1； feed； technoclear-fiber-optics-data-center-certificati | Facebook、Facebook、Facebook、Facebook、Facebook |
| SB-316 swl.co.nz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+14 −14 行 |  |
| SB-317 techfors.cz | B | 4 | 2/2 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+5 −6 行 | Facebook |
| SB-318 verdelon.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-319 viewtech.co.nz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 | Facebook、LinkedIn |
| SB-320 353311@mail.ru | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-321 BWsystems | B | 1 | 0/1 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-322 Blackbear TechHive | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-324 Elhem Trading Co., Sal | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、Instagram |
| SB-327 Techno Tower | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-10-24 首轮基线 |  |
| SB-328 advice.co.il | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+4 −5 行 | Facebook、Instagram、LinkedIn |
| SB-329 cansol.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-330 omninet.com.vn | B | 2 | 2/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook |
| SB-332 simplelogin.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、X/Twitter、X/Twitter |
| SB-333 yli.ro | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+13 −13 行 |  |
| SB-336 INTERCOAX CO.,LTD | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-337 Kimberley telecommunications | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-338 MAX protect | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+135 −135 行 | Facebook、Instagram |
| SB-339 OMEGATEC SARL | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-340 ROCKBIOS Limited | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-344 amer.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook |
| SB-345 andcorp.com.au | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+162 −1 行 |  |
| SB-346 atz.com.sg | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-347 avcomm.us | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： inc.avcomm.us； help-1； faq； feed； feed； feed； feed； feed… |  |
| SB-348 cloudtronics.com.au | B | 3 | 3/0 | 2026-10-29T15:11:51Z | 2026-10-29 feed_auto：恢复可达（上轮 HTTP 502） |  |
| SB-349 dualcomm.com | B | 5 | 4/1 | 2026-11-01T09:25:59Z | 2026-10-28 home：内容变化：+1 −1 行 | X/Twitter |
| SB-350 edge-networks.us | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、X/Twitter |
| SB-351 enetusa.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-352 fiberdyne.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-353 fiberopticcableshop.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-354 fiberopticlink.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-355 gaotek.com | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 feed_auto：新增 1 条：Sat, 24 Oct 2026 06 hello world |  |
| SB-356 infinicoreinc.com | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-357 infonet-tech.com | B | 5 | 4/1 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+1 −0 行 | X/Twitter、LinkedIn、Facebook |
| SB-358 kyolis.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-361 luckyjoint.com.sg | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp、Facebook、LinkedIn、X/Twitter、Instagram |
| SB-362 maintechconnect.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+33 −6 行 |  |
| SB-363 meridian-tech.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-364 nitrotelmanufacturing.com | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-365 robofiber.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-366 th-it.com | B | 3 | 2/1 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+1 −1 行 | WhatsApp、Facebook、WhatsApp |
| SB-368 welotec.com | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+16 −18 行 | LinkedIn、Facebook、Instagram、Instagram |
| SB-369 wieland-electric.com | B | 6 | 4/2 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+62 −3 行 | LinkedIn |
| SB-370 wildix.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 1 条：Thu, 05 Nov 2026 18 Beyond Telephony: How Challenger Business Communicat |  |
| SB-371 wirewerks.com | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、LinkedIn |
| SB-372 很多UK公司在卖他们的产品 | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 113 条： amg-help-digitise-cardiffs-traffic-monitoring-cctv-network； borough-of- | LinkedIn |
| SB-374 3s.com.tr | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、Instagram |
| SB-376 Leamratech | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） |  |
| SB-377 PROVES | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-378 Pal Wintec | B | 4 | 3/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、Instagram |
| SB-379 TRK solution Ltd | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-380 Yellowbox Co Pty Ltd | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 82 条： liberty-brisbane； liberty-melbourne； lseg-gdynia； match-group-london； pe | LinkedIn、Instagram |
| SB-381 accessofranco.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook |
| SB-383 autechcontrol.com.au | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook |
| SB-384 canacctv.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+0 −6 行 |  |
| SB-385 dtsdigitalcctv.co.uk | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2020-03-30 proddetail.asp?prod=DCS-4701E；2020-03-30 proddetail.asp?prod= |  |
| SB-386 dvs.co.uk | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-387 fatwiredist.ca | B | 1 | 1/0 | 2026-10-29T08:41:09Z | 2026-10-29 home：内容变化：+6 −6 行 |  |
| SB-390 hunters-wholesalers.co.uk | B | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-10-23 首轮基线 |  |
| SB-391 inscapedata.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 382 条：2016-06-30T00:43:15 about.htm；2016-03-25T22:32:45 InscapeDataLineCard041 | LinkedIn |
| SB-393 mapleye.com | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、Instagram、X/Twitter |
| SB-394 maxtel.bg | B | 8 | 6/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、X/Twitter |
| SB-395 mercku.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+177 −1 行 |  |
| SB-396 morekamer.ru | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-397 netiks.rs | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+72 −21 行 |  |
| SB-398 osd.com.au | B | 5 | 5/0 | 2026-11-05T09:39:48Z | 2026-11-05 feed_auto：新增 4 条：Thu, 22 Apr 2021 05 Newsletter April 2021；Wed, 31 Mar 2021 05 Newsletter |  |
| SB-399 petawise.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 125 条：2020-12-08T08:16:31 ipc314sr-dvpf2836；2020-12-08T08:16:31 ipc314sr-dvpf3 | Facebook、LinkedIn、Instagram、LinkedIn |
| SB-400 safanetworks.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-401 securasound.co.uk | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-28 news_1：内容变化：+1 −1 行 |  |
| SB-402 sfpturkey.com.tr | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-403 surveillance-video.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SB-404 teamac-arabia.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-405 tinycontrol.pl | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 218 条： accessories_boards_rj12-splitter-3xi2c1w-4x1w； accessories_boards_relay |  |
| SB-406 volokno.kz | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+888 −1 行 | Facebook、Instagram、WhatsApp |
| SB-407 winnerintertech.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+3 −3 行 |  |
| SB-408 xblue.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-409 xlrsecurity.com | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+11 −11 行 | LinkedIn、Instagram、Facebook |
| SB-410 4sltd.com.tr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-411 Floter | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Instagram、Facebook、LinkedIn |
| SB-412 InterConnectivity Computer S | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-413 LTE ELEKTRONIK | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 sitemap：新增 1 条： ohs-policy | Instagram、LinkedIn |
| SB-414 Rolins | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-415 a2s.pl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+4 −4 行 |  |
| SB-416 abcv.pl | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1372 −7 行 |  |
| SB-417 alidex.it | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-418 atel.com.pl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： www.atel.com.pl； ofirmie.php； partnerzy_handlowi.php； rekomendacje.php； |  |
| SB-419 avproglobal.com | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-31 news_1：内容变化：+6 −6 行 |  |
| SB-420 cdr.pl | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： k976,access-pointy-routery-systemy-bezprzewodowe-hotspot-ubiquiti-unifi | Facebook、Instagram |
| SB-421 distribolutions.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SB-422 efb-elektronik.com.tr | B | 5 | 4/1 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Facebook |
| SB-423 es-france.com | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+2 −2 行 |  |
| SB-424 golmar.es | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 2 条：2026-11-06T07:05:42 Sixty5 Touch. Connecting the present to open the futur | LinkedIn、X/Twitter、Instagram |
| SB-425 gsginternational.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 147 条：2019-02-19T17:23:13 arh_smartcamera.pdf；2019-02-27T08:59:25 infosheet_th | LinkedIn、Facebook、Instagram |
| SB-426 helmholz.de | B | 7 | 5/2 | 2026-11-01T09:25:59Z | 2026-10-31 news_2：内容变化：+1 −1 行 | Facebook、LinkedIn |
| SB-427 longlinenetwork.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+10 −10 行 | Facebook、X/Twitter、LinkedIn、Instagram、WhatsApp |
| SB-428 media-konwertery.pl | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+110 −107 行 | Facebook、X/Twitter |
| SB-429 murrelektronik.de | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Instagram、Facebook |
| SB-430 pro-tek.pro | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： company-news；2023-10-11 HiWatch_sale1.html；2023-08-24 forum2023.html；20 |  |
| SB-431 protekna.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-432 qubix.it | B | 4 | 4/0 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+214 −1 行 |  |
| SB-433 rister.com | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-434 s-connect.es | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+6 −7 行 |  |
| SB-435 saucontech.com | B | 4 | 3/1 | 2026-11-04T09:30:29Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、X/Twitter |
| SB-436 steplockaccess.se | B | 1 | 1/0 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+1 −131 行 |  |
| SB-437 tpole.it | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+642 −1 行 | LinkedIn |
| SB-438 CTCU | B | 5 | 4/1 | 2026-11-01T09:25:59Z | 2026-10-29 news_2：内容变化：+2 −4 行 | Facebook、X/Twitter、LinkedIn |
| SB-439 Exxell Vision | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Instagram、Facebook |
| SB-440 JMP | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-441 Metal Union | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-442 Optima Soft | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 818 条：2026-04-24T09:50:52 tr；2026-04-24T09:50:52 en；2026-04-24T09:50:52 fr；202 | Instagram、LinkedIn、WhatsApp |
| SB-443 Spring Network | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-444 Tritonsystems spol. s r.o. | B | 3 | 2/1 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-445 aicom.pl | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-11-06 kable-i-przewody-kable-swiatlowodowe-polaczeniowe-patch-cordy |  |
| SB-446 amatek.su | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2015-09-01 nachalo_prodaz；2015-10-30 amatek_sfitex；2016-02-05 registrato |  |
| SB-448 bettinivideo.com | B | 6 | 4/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-449 bvsecurity.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 |  |
| SB-450 comtech.net.pk | B | 5 | 4/1 | 2026-11-01T09:25:59Z | 2026-10-27 feed_auto：恢复可达（上轮 HTTP 403） | Facebook、Instagram、LinkedIn |
| SB-452 espuk.com | B | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 818 条：2026-11-06 RC228BW；2026-11-06 RC228TB；2026-11-06 RC228TW；2026-11-06 HC42 | Facebook、X/Twitter、LinkedIn |
| SB-453 gmtcontrol.com | B | 5 | 4/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、Instagram |
| SB-454 leoptics.pl | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-455 maxlink.cz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： product； product； product； product； product； product； product； product… |  |
| SB-456 pancakumala.co.id | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-457 pavotek.com.tr | B | 2 | 2/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Instagram、X/Twitter |
| SB-458 satsdigital.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+600 −1 行 |  |
| SB-459 ssdcam.ru | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+8 −8 行 |  |
| SB-460 4G-GmbH | B | 1 | 0/1 | - |  |  |
| SB-462 Eter biometric technologies  | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T07:00:17 No Apps. No Cables. Just Seamless Sharing. | Facebook、Instagram、LinkedIn |
| SB-464 HAMDAZTECH TECHNOLOGIES INC  | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp、LinkedIn、WhatsApp |
| SB-465 Koza | B | 3 | 2/1 | 2026-11-05T09:39:48Z | 2026-11-05 sitemap：新增 820 条：2017-07-04T16:22:40 1-amper-adaptor；2017-07-25T14:24:29 bft-moovi-30-oto |  |
| SB-466 MicroFast Technologies | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-467 NORTEL | B | 1 | 1/0 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 | Facebook、Instagram、X/Twitter |
| SB-468 Ninh Thanh Production and Tr | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter |
| SB-470 asm.cz | B | 3 | 1/2 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+177 −2 行 |  |
| SB-471 austec.net | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-472 bma-networks.com | B | 7 | 5/2 | 2026-11-05T09:39:48Z | 2026-11-05 news_2：内容变化：+105 −1 行 | Instagram、LinkedIn |
| SB-475 cctvdepo.com | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 | WhatsApp、Facebook、Instagram、X/Twitter、LinkedIn |
| SB-477 eminnovate.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-478 eurocamguvenlik.com.tr | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 552 条：2026-11-06 urun.php?id=689；2026-11-06 urun.php?id=688；2026-11-06 urun.ph |  |
| SB-479 ezy.hr | B | 3 | 1/2 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+0 −2 行 |  |
| SB-480 hanyotele.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-481 itegra.lt | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、Instagram |
| SB-482 keme-tec.com | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 | Facebook |
| SB-483 melbyefiber.com | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Facebook |
| SB-484 mosonetworks.com | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+185 −1 行 |  |
| SB-486 ngapl.in | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+0 −1 行 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-488 octogate.de | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Instagram、X/Twitter |
| SB-489 portel.com.tr | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、Instagram、LinkedIn |
| SB-490 radioteknoloji.com.tr | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 243 条：2026-07-08T11:16:06 ilgaz-belediye-bakanmz-sayn-mehmet-ztrk-irketimizde- | WhatsApp |
| SB-491 raskpreke.lt | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-492 sistel-networking.it | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） |  |
| SB-493 syserso.com | B | 6 | 4/2 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn |
| SB-494 teleone.com.tr | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-495 topnetdistribution.com | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SB-497 Cong Ty TNHH CONG NGHE QUANG | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-498 DTI Tecnologia Ltda | B | 1 | 0/1 | - |  |  |
| SB-499 b.medvedev11@mail.ru | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-500 cetsingapore.com | B | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+145 −1 行 |  |
| SB-501 diteksurgeprotection.com | B | 6 | 5/1 | 2026-11-03T09:43:52Z | 2026-10-31 home：内容变化：+1 −1 行 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-502 elimopt.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-503 elprotech.com | B | 6 | 6/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn |
| SB-504 eltech.com.au | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+0 −5 行 | Facebook、Instagram、LinkedIn |
| SB-505 eso.co.th | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+3 −3 行 | Facebook、Instagram |
| SB-506 fibertek-ap.com | B | 2 | 1/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 303 条：2024-09-23T11:46:54 ethernet-network-ethernet-cable-unshielded-category- |  |
| SB-507 fibreoptic.com.au | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-508 gotinc.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-509 ionetech.com | B | 1 | 0/1 | 2026-11-06T09:32:27Z | 2026-10-23 首轮基线 |  |
| SB-511 rivershop.co.kr | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-08-22T11:36:30 rivershop.co.kr；2025-08-20T15:16:15 company.html；202 | Instagram、Facebook |
| SB-512 solustecnologia.com | B | 3 | 0/3 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、Instagram、WhatsApp |
| SB-513 starlink.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-514 257.cz | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-515 3tel.com.sg | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 155 条：2021-05-19T12:41:10 acm-k3r；2021-05-19T12:41:47 acm-y280-5bolts；2021-05- | Facebook |
| SB-518 Info Systems Lahore | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-519 Kyber Electronics | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-520 abctech.cz | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+55 −55 行 | Facebook |
| SB-521 aceonline.co.uk | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2024-04-17 ace-44cm-zone-1-elliptical-dish-17-p.asp；2026-05-13 blake-ada | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-522 adilec.com | B | 2 | 1/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-523 aristel.com.au | B | 4 | 3/1 | 2026-10-29T08:41:09Z | 2026-10-29 home：内容变化：+0 −2 行 |  |
| SB-524 armadi-rack.it | B | 2 | 1/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-02-18 149-quadri-elettrici；2026-09-14 120-telai-subracks；2025-10-23 |  |
| SB-525 atlantis-land.com | B | 1 | 0/1 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-526 automationstore.it | B | 1 | 0/1 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+2 −505 行 |  |
| SB-527 avalan.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+3 −3 行 | Facebook、LinkedIn、X/Twitter、Instagram |
| SB-528 commfront.com | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook |
| SB-530 dss-kuwait.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Instagram |
| SB-531 dynamode.co.uk | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-532 eclipsecctv.com | B | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：更新 18 条：ESG-NVR16 16 Camera Network Video Recorder（Wed, 4 Nov 2026 00: → Fri, 6 | Facebook、X/Twitter、Instagram |
| SB-533 eks-engel.de | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、Instagram、LinkedIn |
| SB-534 elfcams.com | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 | WhatsApp、WhatsApp |
| SB-535 escadtrade.cz | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-536 highlink.co.kr | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-537 htvision.ru | B | 1 | 0/1 | 2026-11-03T09:43:52Z | 2026-10-23 首轮基线 |  |
| SB-538 infinitecables.com | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-31 home：内容变化：+3 −3 行 | Facebook、X/Twitter、Instagram |
| SB-539 ipcomm.de | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 767 条： sheet.html； sheet.html； sheet.html； sheet.html； sheet.html； sheet.html； |  |
| SB-540 jdktech.com.au | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-541 kbcnetworks.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+4 −4 行 | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-543 luetze.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+12 −3 行 | LinkedIn |
| SB-544 makonetworks.com | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+219 −1 行 | X/Twitter、Facebook、LinkedIn |
| SB-545 mreit.co.kr | B | 1 | 1/0 | 2026-10-25T07:41:18Z | 2026-10-23 首轮基线 |  |
| SB-546 ness.com.au | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2024-11-07 home-security；2023-08-20 self-contained；2023-08-20 premium-se |  |
| SB-547 netinet.pl | B | 6 | 4/2 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+16 −15 行 | LinkedIn、LinkedIn |
| SB-548 netsys-direct.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-549 poewit.com | B | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+149 −1 行 |  |
| SB-550 reichelt.com | B | 2 | 2/0 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+0 −1 行 | Facebook |
| SB-551 sanspot.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-552 securevision.com.sg | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 168 条：2026-07-02 cctv-cable-upgrade；2026-07-02 cctv-pdpa-compliance；2026-07-02 | WhatsApp |
| SB-553 sequrinet.us | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-554 sysnettelematica.it | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-24 首轮基线 |  |
| SB-555 tacel.ca | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 107 条： 2070lx-controller； xn-its-controller； xn-1-controller； xn-2-controller； | LinkedIn |
| SB-556 ubf.de | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-557 ubitron.co.kr | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+11 −11 行 |  |
| SB-558 uniformatic.fr | B | 1 | 0/1 | - |  |  |
| SB-559 vipausa.com | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 HTTP 500） | LinkedIn、X/Twitter |
| SB-560 womaster.eu | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-09-09 download_51_186.htm；2025-09-09 download_51_187.htm；2025-09-09 |  |
| SB-561 zoomlinenetwork.com | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-11-04 feed_auto：新增 2 条：Wed, 04 Nov 2026 05 5 Structured Cabling Installation Mistakes That Cost | Facebook、Instagram、LinkedIn、X/Twitter |
| SB-562 ALT VISION | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-564 Latitude | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-565 Marmaris Bilişim | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-566 PCG Bilgisayar LTD.STI. | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、LinkedIn、Instagram |
| SB-567 TGM Global Pte Ltd | B | 1 | 1/0 | 2026-10-27T08:02:45Z | 2026-10-23 首轮基线 |  |
| SB-569 cablematic.com | B | 3 | 1/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1948 −1 行 |  |
| SB-570 certech.com.au | B | 1 | 1/0 | 2026-10-26T07:56:19Z | 2026-10-26 home：内容变化：+5 −5 行 | LinkedIn |
| SB-571 energus.eu | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-572 fourline.com.tr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-573 integranetwork.es | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-574 lanberg.pl | B | 6 | 4/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、LinkedIn |
| SB-575 marbim.com.tr | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-576 matrix.es | B | 6 | 4/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-577 metaworldcomputers.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+151 −1 行 |  |
| SB-578 niaar.net | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、WhatsApp |
| SB-579 nnc.net.vn | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-581 sheildify.com | B | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-03 news_1：内容变化：+465 −1 行 |  |
| SB-582 smartintercom.eu | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+2 −2 行 |  |
| SB-584 vanphatdat.vn | B | 2 | 0/2 | - |  | Facebook |
| SB-585 vidos.pl | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook |
| SB-586 Matrix vision systems | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-588 WAN networking technology | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-24 youtube：恢复可达（上轮 HTTP 500） | Facebook、X/Twitter |
| SB-589 bydemes.com | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+24 −24 行 |  |
| SB-590 carritech.com | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 6 条：Mon, 02 Nov 2026 13 Alarm Hygiene: Why Nobody Trusts the Alarm List and  | LinkedIn、Facebook |
| SB-591 elementuengenharia.com.br | B | 5 | 5/0 | 2026-10-28T08:44:48Z | 2026-10-28 youtube：新增 1 条：2026-10-27T19:00:13 INSTALAÇÃO DE POSTES DE ILUMINAÇÃO AUTÔNOMA E CONVENCI | Instagram、Facebook、LinkedIn |
| SB-592 fotech.com.tr | B | 2 | 2/0 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+85 −6 行 |  |
| SB-593 ibdglobal.com | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+5 −0 行 |  |
| SB-594 kmsoltec.com | B | 6 | 3/3 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-05T11:30:06 NUC 16 Pro Ultra X9: RAM saldata, ma più veloce per l’ | Facebook、Instagram、LinkedIn |
| SB-595 mpcl.in | B | 5 | 5/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+2 −16 行 | LinkedIn |
| SB-596 optokon.pl | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 178 条：2020-08-04T11:31:37 panele.pdf；2021-02-09T19:05:21 52-sprzegacz-optyczny |  |
| SB-597 plus-nn.ru | B | 1 | 0/1 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-598 solway.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-600 t1nexus.com | B | 3 | 3/0 | 2026-10-26T07:56:19Z | 2026-10-26 home：内容变化：+5 −9 行 | LinkedIn |
| SB-601 visus.pt | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-602 ANIL | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+104 −1 行 | Instagram、LinkedIn、LinkedIn |
| SB-604 Burns Precision Ag | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+0 −1 行 |  |
| SB-605 Elkov Elektro | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1215 −16 行 |  |
| SB-606 HME Solutions | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-607 JTOPTICS | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+154 −2 行 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-608 Marlen Sadybekov | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-609 ablelink.co.th | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： f-pca-fcfc5-3-dx； f-pca-fclc5-3-dx； f-pca-lclc5-3-dx； f-pca-fcsc5-3-dx； |  |
| SB-611 avanis.de | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-29 news_2：内容变化：+1 −1 行 | Instagram、LinkedIn |
| SB-612 clouditnetwork.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter |
| SB-613 cozzmic.com | B | 5 | 4/1 | 2026-11-01T09:25:59Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter、LinkedIn |
| SB-614 focomm-cabling.com | B | 4 | 1/3 | 2026-10-31T08:34:28Z | 2026-10-31 feed_auto：恢复可达（上轮 HTTP 403） | Facebook、Facebook |
| SB-615 handsonsecurity.co.za | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-616 intant.kz | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+604 −0 行 |  |
| SB-617 ipc2u.com | B | 5 | 5/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、LinkedIn |
| SB-618 jeatech.com.au | B | 4 | 4/0 | 2026-10-27T08:02:45Z | 2026-10-27 news_2：内容变化：+153 −2 行 |  |
| SB-619 jmdv.ru | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-620 karma-group.ru | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-621 lanshack.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： QuickTreX-PRO-System-Pre-Terminated-Fiber-Optic-Assemblies-C534； QuickT |  |
| SB-622 market-telecom.kz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： market-telecom.kz；2026-06-06 products；2026-07-29 about_shop；2026-06-06  | Instagram |
| SB-623 smol-electro.ru | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 87 条：2020-10-16T15:26:57 magistral-70-premium-4-linzy；2020-10-21T14:15:01 svet |  |
| SB-624 ubwh.com.au | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+19 −15 行 |  |
| SB-625 virtware.pt | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-626 visiondynamics.de | B | 1 | 1/0 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-627 zonagsm.su | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2021-10-30T10:59:26 ax-2411y-napravlennaya-vneshnyaya-antenna-wi-fi；2021 |  |
| SB-628 BRIGHTNET SERVICES SDN BHD | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp、Facebook、Instagram |
| SB-629 C-TECH | B | 4 | 4/0 | 2026-10-28T08:44:48Z | 2026-10-28 feed_auto：恢复可达（上轮 HTTP 509） | LinkedIn、Facebook |
| SB-631 Gigaxysafe Technologies Ltd | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+36 −4 行 |  |
| SB-632 Grypen Technologies Private  | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-633 Hoang Long Import-Export and | B | 1 | 1/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+92 −3 行 | Facebook、Instagram |
| SB-634 Hoang Thien An Technology Tr | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+3 −3 行 | Facebook、Facebook |
| SB-635 LMD Hitech India (P) Ltd. | B | 1 | 0/1 | - |  |  |
| SB-636 MARZETEK (Pty) Ltd | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-637 NaSys Inc | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-638 OPATOV 之前联系过的客户 | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+4 −12 行 |  |
| SB-640 Technoverse Business Solutio | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2025-09-08T11:36:52 TECHNOVERSE BUSINESS SOLUTIONS | WhatsApp、Instagram、Facebook、X/Twitter、LinkedIn |
| SB-643 arbybilgisayar.com.tr | B | 3 | 3/0 | 2026-10-26T07:56:19Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Instagram、X/Twitter、Facebook |
| SB-644 art2soft.eu | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、Instagram、LinkedIn |
| SB-645 arthaberlesme.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SB-646 artsistem.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： poe-guc-butcesi； kablo-mesafesi-100m-ustu； ups-va-yedekleme-suresi； rai | Facebook、Instagram、LinkedIn、WhatsApp |
| SB-647 arttelekom.com.tr | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 12 条： guvenlik-kamera-sistemleri； apartman-konusma-sistemleri； hirsiz-alarm-si | Facebook、LinkedIn |
| SB-648 atelekom.com.tr | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+20 −20 行 | Instagram、Instagram、Instagram、Facebook、Instagram |
| SB-649 basarimuhendislik.com | B | 6 | 6/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn、Instagram、Facebook |
| SB-650 beastteknoloji.com | B | 3 | 2/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、Instagram |
| SB-651 biges.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 794 条： VG-8C1E-NVR-I； BLW-H5104-D1； GFE-SWR-LMP； BLW-506CP-R； DG75PLUS； DHI-DS |  |
| SB-652 comxus.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+424 −251 行 | Facebook、Instagram、LinkedIn |
| SB-654 davantel.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 221 条：Fri, 06 Nov 2026 09 Kyland obtiene una nueva certificación IEC 62443-4 |  |
| SB-655 digisol.com | B | 6 | 6/0 | 2026-11-02T09:40:28Z | 2026-11-02 news_2：内容变化：+4 −0 行 | LinkedIn、Facebook、Instagram、X/Twitter、WhatsApp |
| SB-656 dijitalbina.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-657 egesanteknoloji.com.tr | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+1 −1 行 | WhatsApp |
| SB-658 ekingen.com.tr | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn、WhatsApp、Facebook |
| SB-659 entpa.com.tr | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 | Facebook |
| SB-660 fonet.com.tr | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-662 hssl.us | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+2180 −1 行 |  |
| SB-663 hstn.co.th | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T01:53:21 JJSATs รับติดตั้งระบบอะไรบ้าง? | Facebook |
| SB-664 jm.pl | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 816 条： uklady-scalone-i-mikrokontrolery-dla-urzadzen-z-wyswietlaczem； uklady-s | Facebook、LinkedIn |
| SB-665 marsateknoloji.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、Instagram、WhatsApp、Facebook |
| SB-666 mavialarm.com.tr | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、Instagram、LinkedIn、X/Twitter |
| SB-667 mgt.bayern | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook |
| SB-669 mnsbilisim.com | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 HTTP 500） | Facebook、Instagram、LinkedIn |
| SB-670 monkas.com.tr | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+40 −40 行 |  |
| SB-672 netshieldsa.com | B | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：恢复可达（上轮 HTTP 500） |  |
| SB-673 nodactechnology.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-08-07 Personal%20Data%20Processing%20Policy.pdf；2025-10-03 brands?l | Facebook、Instagram、Facebook、LinkedIn、X/Twitter |
| SB-674 noxel.pl | B | 6 | 6/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+2 −3 行 | Facebook |
| SB-675 pandacomdirekt.de | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 188 条：2019-12-17T20:22:45 herstelleruebergreifende-orchestrierung.html；2019-12 |  |
| SB-676 pctedarik.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 2 条：2026-11-05T17:00:40 Minik Kedi, Dev Ekrandaki Futbolcuların Peşinde；2026-1 |  |
| SB-677 perkotek.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 815 条：2021-06-16T09:12:42 ariza-bildirimi；2021-06-16T09:12:42 teknik-destek-ta | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-678 qntmnet.com | B | 4 | 4/0 | 2026-11-04T09:30:29Z | 2026-11-04 youtube：新增 1 条：2026-11-04T07:30:15 A campus network is tested when everyone comes online  | LinkedIn、X/Twitter、Instagram、Facebook |
| SB-679 saratota.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+5 −5 行 | Facebook、X/Twitter、X/Twitter、Instagram |
| SB-680 schrack.cz | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −0 行 | Facebook、Instagram、LinkedIn |
| SB-681 serrackkabin.com.tr | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 115 条： 07U-Acik-Tip-Duvar-Kabinet--Moduler； 09U-Acik-Tip-Duvar-Kabinet--Module | Instagram、Facebook、LinkedIn |
| SB-682 serverblink.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+311 −1 行 |  |
| SB-683 spectra.de | B | 6 | 4/2 | 2026-11-05T09:39:48Z | 2026-11-05 news_2：内容变化：+12 −6 行 |  |
| SB-684 technics-india.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 95 条： rugged-pc-robust-pc.pdf； Rugged_ASP-1.pdf； Rugged_Monitor.pdf； Rugged_Se |  |
| SB-685 techsouq.com | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-686 teknoktadestek.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 591 条：2026-06-15 category&path=69_78_85；2026-06-15 category&path=69_93_95；2026 | WhatsApp、Instagram、X/Twitter、Facebook |
| SB-687 telkotim.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 420 条：2021-11-11T18:43:29 dahili-tight-buffer-fiber-optik-kablolar；2021-11-11T |  |
| SB-688 teslakom.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-689 tiscontrol.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2022-05-05 air_venera_switch.html?cid=20；2022-05-05 air_venera_dimmer.ht |  |
| SB-690 troyykontrol.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 | Facebook、X/Twitter |
| SB-691 vitel.com.tr | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-693 Bin Hilal Group | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-694 Le Reveil | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-695 Leandro Roisenberg FI | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+35 −41 行 |  |
| SB-697 alliedasia.com.sg | B | 3 | 3/0 | 2026-11-03T09:43:52Z | 2026-11-03 feed_auto：恢复可达（上轮 HTTP 522） |  |
| SB-698 cbo-it.de | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-699 ccdact.com.au | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+1 −3 行 | Facebook、Instagram、LinkedIn |
| SB-700 cctvcamara.pt | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+56 −1 行 |  |
| SB-702 ctsystem.com | B | 6 | 1/5 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | LinkedIn |
| SB-703 engitel.com.mx | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-704 ethical-ltd.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-705 eware.com.hk | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、LinkedIn、WhatsApp |
| SB-706 eworldme.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1766 −1 行 |  |
| SB-707 goetz-automation.de | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-708 hyconext.com | B | 2 | 2/0 | 2026-11-01T09:25:59Z | 2026-11-01 news_1：内容变化：+8 −8 行 | Facebook、LinkedIn |
| SB-709 ic-intracom.bg | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： apsc59123cdl60-1-25g-cwdm-sfp-оптичен-модул-по-две-влакна-1590-nm-lc-60 |  |
| SB-710 ktinet.com.tw | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-711 madalix.co.il | B | 4 | 4/0 | 2026-10-29T08:41:09Z | 2026-10-29 news_1：内容变化：+33 −1 行 |  |
| SB-712 maplesystems.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+261 −0 行 |  |
| SB-713 netronicsnetworks.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-714 netsecurity.com.au | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+8 −8 行 |  |
| SB-715 netsys.com.tw | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook |
| SB-716 radioparts.com.au | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1031 −1 行 |  |
| SB-717 skyware.com.hk | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-718 teksarf.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+4 −4 行 |  |
| SB-719 trioms.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-721 woodcomm.ie | B | 5 | 5/0 | 2026-10-29T15:11:51Z | 2026-10-29 news_2：内容变化：+3 −3 行 | Facebook、LinkedIn |
| SB-722 Aptvel global technologies | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | X/Twitter、LinkedIn |
| SB-723 BİLGEN ELEKTRONİK | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-724 Comms Express Ltd | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-726 Elettronica E Sicurezza | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： connettori-ballun.1.16.288.sp.uw； contatti-magnetici.1.16.289.sp.uw； ta |  |
| SB-728 Fast-Track Systems & Service | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-729 Heitech Padu Berhad | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-730 ITSS Inc/ | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-732 Maxitulin | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T04:30:33 AI-Powered Real-Time Truck & Visitor Monitoring by Max |  |
| SB-733 Preciso Technology SDN BHD | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-29 home：内容变化：+224 −1 行 |  |
| SB-734 SIGMA RECTRIX SYSTEMS (M) SD | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 31 条： jobs-30； internship-31； jobs-30； feed； feed； feed； nak-tahu-1-ap-boleh-c |  |
| SB-736 Sun Energy Enterprise Sdn Bh | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-738 Ugur Simsek Netmax | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-739 arcdyn.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 778 条： arcdyn.com；2026-09-28T18:04:31 ip-cameras.html；2026-09-03T14:26:47 nvr. |  |
| SB-740 britaniccablingproduction.co | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-741 canarycom.com | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-742 cctvroom.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-743 cleerlinefiber.com | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+2 −2 行 |  |
| SB-744 commandonetworks.com | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+30 −3 行 | X/Twitter、Facebook、Instagram、LinkedIn |
| SB-745 comtrol.co.uk | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-746 cybron.com.my | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter |
| SB-747 digitclik.it | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-748 dnaelektro.cz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −63 行 |  |
| SB-749 ecin.ca | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 194 条：2026-07-30 celestica；2026-06-23 contact-us；2026-07-31 cookie-policy；2026 |  |
| SB-750 enableit.com | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_2：内容变化：+118 −1 行 |  |
| SB-751 engeniustech.com | B | 5 | 5/0 | 2026-11-03T09:43:52Z | 2026-11-03 youtube：新增 1 条：2026-11-02T20:57:24 Webinar: Beyond Wi-Fi - Complete Connectivity for Resi |  |
| SB-752 enika.cz | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 | LinkedIn、Facebook |
| SB-753 eu.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-754 fastercable.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-755 fibresales.com.au | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-756 fluxlight.com | B | 2 | 1/1 | 2026-10-25T07:41:18Z | 2026-10-25 home：内容变化：+49 −217 行 | LinkedIn、Facebook、X/Twitter |
| SB-757 flyteccomputers.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp |
| SB-758 fossfibreoptics.com | B | 5 | 3/2 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+195 −2 行 |  |
| SB-759 futurereadysolutions.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+2 −2 行 | Facebook、X/Twitter、LinkedIn |
| SB-760 galaxysecurity.com | B | 2 | 2/0 | 2026-10-28T08:44:48Z | 2026-10-28 home：内容变化：+8 −0 行 |  |
| SB-761 getscw.com | B | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-05T17:20:06 PTZ Camera Auto Tracking: Better Parking Lot Evidence | LinkedIn |
| SB-762 groundcontrol.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-05T12:46:22 RockBLOCK APNT: Iridium PNT Positioning and Timing for | X/Twitter、LinkedIn、Facebook |
| SB-763 idome.uk | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+17 −17 行 |  |
| SB-764 ifotec.com | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-765 inv-technology.com | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 228 条：2020-10-09T14:26:03 33-accessories；2020-10-09T14:26:03 34-access-control | Facebook |
| SB-766 invidtech.com | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、LinkedIn |
| SB-768 kbvdatacom.rs | B | 5 | 0/5 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-769 konturm.ru | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 550 条： tech.php?id=ods； tech.php?id=im； tech.php?id=nap； tech.php?id=rv； tech. | Instagram |
| SB-770 lanode.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 home：内容变化：+9 −9 行 |  |
| SB-771 lanprosa.com | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+36 −36 行 | Facebook、Instagram、LinkedIn、WhatsApp、Facebook |
| SB-772 mencom.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-773 microseven.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SB-774 netwerkproducten.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-775 patton.com | B | 6 | 1/5 | 2026-11-05T09:39:48Z | 2026-11-05 sitemap：新增 214 条：2021-05-04T20:56:46 www.patton.com；2021-05-04T20:56:53 contact-us.asp；20 | X/Twitter、LinkedIn、Facebook |
| SB-776 prolink2u.com | B | 3 | 3/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、Instagram、LinkedIn |
| SB-777 proplex.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 20 条：2023-03-06 proplex-ethernet-cables-adopted-by-new-markets；2021-06-04 bbc- |  |
| SB-778 pyramid.lt | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1406 −1 行 |  |
| SB-779 shop4power.nl | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-780 signamax.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-781 silvernet.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-782 simpleuk.com | B | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2020-09-16 cfp-100g；2019-11-12 cisco-memory；2019-12-20 compact-flash；201 | Facebook、X/Twitter |
| SB-783 sitech-bitdriver.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 212 条： t43.htm； t44.htm； t45.htm； t46.htm； t47.htm； t48.htm； t49.htm； t50.htm… |  |
| SB-784 sklep-bcs.pl | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+20 −19 行 | Facebook |
| SB-785 smartsystems.jo | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： network-nf-801b-tester-rj11-rj45-lan-wire-tracker-fault-locator-and-cab | Facebook、Instagram |
| SB-788 tss-e.com | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-789 visarcctv.com | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-27 home：内容变化：+76 −2 行 | Facebook、LinkedIn |
| SB-790 vulsanx.com | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-791 wachendorff-prozesstechnik.d | B | 6 | 4/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-792 weltronproducts.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-793 worldstarsecuritycameras.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 1 条：Fri, 06 Nov 2026 02 Access Control vs Traditional Keys for Business |  |
| SB-794 wut.de | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-795 yachtgurus.us | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-796 Destek Elektronik Tic. Ltd. | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 750 条： gecis-kontrol； sesli-uyari-sistemi； maskesiz-kisi-algilama-kameralari；  |  |
| SB-797 Excel Engineering (SG) Pte L | B | 1 | 0/1 | - |  |  |
| SB-798 Getec | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-800 acelink.com.tw | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 HTTP 500） | Facebook、LinkedIn |
| SB-801 aurcore.net | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 1 条：2026-03-06T17:28:15 meet-the-aurcore-team-at-ofc-2026-west-hall-5151 | LinkedIn、X/Twitter、Instagram、Facebook |
| SB-802 baldota.co.in | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、Instagram、LinkedIn、X/Twitter |
| SB-803 bestpc.bg | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+79 −81 行 |  |
| SB-804 bm-switch.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-805 cctvspot.co.uk | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −1 行 | Facebook、X/Twitter |
| SB-806 datageneral.co | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-807 datastream.by | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+810 −1 行 |  |
| SB-808 deponet.com.tr | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Instagram |
| SB-809 econnet.it | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： telecamere-ip-professionali.1.22.258.sp.uw； lpr-license-plate-recogniti |  |
| SB-810 enssecurity.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+469 −1 行 |  |
| SB-811 esoft.fi | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+114 −68 行 |  |
| SB-812 ethernetdirect-jp.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 7 条：2017-09-04T02:24:42 www.ethernetdirect-tw.com；2017-09-04T02:24:42 index.ht | Facebook |
| SB-813 ifocusshop.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+53 −1 行 |  |
| SB-814 istream.by | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 808 条： nerezerviruemye-bloki-pitaniya； rezerviruemye-bloki-pitaniya； akkumulya | Facebook、X/Twitter |
| SB-815 lendoux.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+38 −39 行 |  |
| SB-816 lorwen.it | B | 2 | 2/0 | 2026-10-25T07:41:18Z | 2026-10-25 home：内容变化：+0 −1 行 |  |
| SB-817 masstracktech.com | B | 2 | 1/1 | 2026-11-04T09:30:29Z | 2026-10-23 首轮基线 | Facebook |
| SB-819 nabludenie.by | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Instagram |
| SB-820 prismwifi.com | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Instagram、Facebook、LinkedIn、X/Twitter |
| SB-822 solidcable.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 714 条： Types.aspx?shelfBoardNo=2005； Types.aspx?shelfBoardNo=2006； Types.aspx? |  |
| SB-823 synchronet.net | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+77 −5 行 | Facebook、LinkedIn |
| SB-824 synchsoft.com.pk | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-10-23 首轮基线 |  |
| SB-825 t-automation.by | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+76 −6 行 | Facebook、Instagram |
| SB-827 GOIP Global Services Pvt Ltd | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | Facebook、Instagram、LinkedIn |
| SB-828 LMP Lux Media Plan | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-829 Optimus | B | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-10-23 首轮基线 |  |
| SB-832 alidex.es | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+1 −1 行 |  |
| SB-833 comtime-com.de | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-834 eneo-security.com | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-835 fiberopticsupply.com | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-23 首轮基线 |  |
| SB-836 fiberworks.no | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 21 条：06.11.2026 09.16.36 QSFP28, 100G/40G SRBD, 2x50 Gbps, 150m；02.11.2026 1 |  |
| SB-837 giga-link.ru | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-838 gmidatabox.fr | B | 1 | 0/1 | - |  |  |
| SB-839 ilucoltd.com | B | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 169 条： %e9%82%84%e5%9b%9e%e6%b2%bb%e5%85%b7； %e8%b3%87%e8%a8%8a%e8%a8%ad%e5%82 |  |
| SB-840 inline-info.com | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+0 −10 行 |  |
| SB-841 kohen.ca | B | 1 | 1/0 | 2026-10-24T04:35:40Z | 2026-10-24 home：内容变化：+3 −1 行 |  |
| SB-842 kzn-gps.ru | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-11-03 smart-watch；2026-11-03 fitness；2026-11-03 materinskie-platy；2 |  |
| SB-843 mir-sb.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+4 −4 行 |  |
| SB-844 oemarket.com | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-846 qualicam.de | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 433 条： funk-pgm-modul-868-mhz-qc-md20.html； funk-fernbedienung-868-mhz-qc-rc11 | Instagram、Facebook、WhatsApp |
| SB-847 rollan.ca | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-848 setilend.ru | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1452 −41 行 | WhatsApp |
| SB-849 ssd.ru | B | 7 | 7/0 | 2026-11-05T09:39:48Z | 2026-11-05 telegram：内容变化：+1 −1 行 |  |
| SB-850 symway.com | B | 1 | 0/1 | - |  |  |
| SB-851 tayle.ru | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+126 −9 行 |  |
| SB-852 Alam Jaya Management | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-853 JM Fiber Optics Inc | B | 4 | 3/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-854 NetCat SYSTEMS GmbH | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-856 Omond-Tong Consultancy Ltd | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-857 airpro.in | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-858 areskom.com.tr | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） |  |
| SB-859 baburtech.com | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+786 −1 行 | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-860 basithamitech.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-861 bimel.com.tr | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T06:47:30 Beek BT-LT600S Dokunmatik Ekranlı Çok Fonksiyonlu Ağ K | LinkedIn、X/Twitter、Facebook |
| SB-862 cebecigrup.com | B | 4 | 4/0 | 2026-10-24T04:35:40Z | 2026-10-24 news_1：内容变化：+1 −0 行 | Facebook、X/Twitter、Instagram |
| SB-863 cmd-sec.ru | B | 7 | 7/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+7 −7 行 |  |
| SB-864 dacelsolutions.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-05T14:00:08 PLC Nedir? Makinede Kararı Hangi Cihaz Verir? | Facebook、X/Twitter、Instagram、LinkedIn |
| SB-865 dbjcontrad@hotmail.com | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-866 egemenelektronik.com | B | 2 | 2/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 HTTP 500） | WhatsApp、Facebook、LinkedIn、X/Twitter、Instagram |
| SB-867 erete.com.tr | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 289 条：2017-10-31 60；2017-10-31 55；2017-10-31 54；2017-10-31 53；2017-10-31 59；20 | Facebook、LinkedIn、X/Twitter |
| SB-868 fiberden.com | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+107 −106 行 | Instagram、LinkedIn |
| SB-870 hunter-cctv.ru | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 555 条：2026-10-31 f-f-perehodnik-bochka；2026-10-31 rca-shteker-pod-vint；2026-10 |  |
| SB-871 intenet.com.tr | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、X/Twitter、Instagram |
| SB-873 istccorp.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-874 keno-cctv.ru | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+532 −1 行 |  |
| SB-875 lemaxguvenlik.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 255 条： 194； 197； 253； 325； 321； 322； 323； 142… |  |
| SB-876 lilin.vn | B | 1 | 1/0 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-877 ltv-cctv.ru | B | 7 | 7/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+104 −17 行 |  |
| SB-878 magnusgulf.com | B | 6 | 6/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter、LinkedIn、Instagram |
| SB-879 mfd.com.tr | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter、LinkedIn、Instagram、Instagram |
| SB-881 nexlar.com | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、X/Twitter |
| SB-882 pctelecom.co.th | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-883 phuongdung.com | B | 2 | 0/2 | 2026-11-04T09:30:29Z | 2026-11-04 sitemap：新增 773 条：2026-11-04T16:51:04 siemens；2026-11-04T16:51:04 bo-luu-dien；2026-11-04T1 |  |
| SB-884 polyvision.ru | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2017-07-10T14:54:27 1881-obnovlenie-programmnogo-obespecheniya-cms；2018- |  |
| SB-885 riverplus.com | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 youtube：新增 2 条：2026-11-05T04:41:45 Milesight UR32S ／ เชื่อมต่ออินเทอร์เน็ตผ่าน 4G โดยไม่ต | Facebook |
| SB-886 sarmatt.ru | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter |
| SB-887 stasanet.rs | B | 4 | 3/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 819 条： ja-110z-b-modul-za-spajanje-petlje； ja-110z-c-modul-za-spajanje-petlje； | Facebook、Instagram、LinkedIn |
| SB-888 stordis.com | B | 5 | 0/5 | 2026-11-03T09:43:52Z | 2026-10-28 home：内容变化：+227 −3 行 |  |
| SB-889 teamon.com.tr | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+2 −2 行 | Facebook、X/Twitter、Instagram |
| SB-890 technopc.com.tr | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 515 条： endustriyel-arac-pc-serisi； endustriyel-monitor-serisi； digital-signage | Facebook、Instagram、LinkedIn |
| SB-891 techpoint-gmbh.de | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、Facebook、WhatsApp |
| SB-893 trassir.ru | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 420 条：2025-03-10T12:38:05 trassir.ru；2025-03-10T12:38:05 products；2025-03-10T1 |  |
| SB-894 video-svp.ru | B | 3 | 3/0 | 2026-11-03T09:43:52Z | 2026-10-23 首轮基线 |  |
| SB-895 vilcom.ru | B | 1 | 0/1 | - |  |  |
| SB-896 wafulamusine@gmail.com | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-898 xvi.ru | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-899 摄像头公司 | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-10-23 首轮基线 |  |
| SB-900 Eleandro | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-901 Hersnet Ltd | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-904 Nuthill | B | 1 | 1/0 | 2026-10-29T08:41:09Z | 2026-10-23 首轮基线 |  |
| SB-906 avizio.pl | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-907 besd.nl | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | LinkedIn |
| SB-908 ctservicestore.it | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+59 −59 行 | WhatsApp |
| SB-909 daejinnetworks.com | B | 3 | 3/0 | 2026-10-24T04:35:40Z | 2026-10-24 home：内容变化：+1 −1 行 |  |
| SB-911 itmarket.co.il | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+108 −1 行 |  |
| SB-913 lanpro.com | B | 3 | 2/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 370 条： products_list.asp?id=30； products_list.asp?id=33； products_list.asp?id= | Facebook、X/Twitter、Instagram |
| SB-914 mro-tek.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 22 条：2026-09-07 ecat-01l；2026-09-07 maple；2026-09-07 maple-1c-o；2026-09-07 map | LinkedIn |
| SB-915 radwin.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 |  |
| SB-916 skipod.lk | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、LinkedIn |
| SB-917 torqsys.com | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-918 Alston Systems | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、Instagram |
| SB-919 Bismon Co.,Ltd | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-11-06 x764；2026-11-06 x763；2026-11-06 x757；2026-11-06 x756；2026-11- |  |
| SB-920 Blue Skill Ltd | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | WhatsApp、WhatsApp |
| SB-922 Fiberbase | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-923 HYESUNG TECHWIN | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-925 MIRAE SIGNAL CO.,LTD | B | 2 | 2/0 | 2026-10-28T08:44:48Z | 2026-10-28 home：内容变化：+79 −10 行 |  |
| SB-926 Osool Coummunications | B | 5 | 4/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、Instagram |
| SB-927 RARMX ENGINEERING SA DE CV | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-928 SEVEN Stars | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter |
| SB-929 SOLTECH | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+17 −18 行 |  |
| SB-930 Socra Spa. | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+3 −3 行 | Facebook、Instagram |
| SB-931 Wave1 Pty Ltd | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+2 −2 行 |  |
| SB-932 acceed.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： cpu-embedded-celeron-pentium； cpu-embedded-celeron-pentium； ram； ram； r |  |
| SB-933 airlive.com | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 455 条：2024-12-18 SMB；2021-02-24 Others---topology-top-introduce；2023-05-11 Air |  |
| SB-934 alibisecurity.com | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_2：内容变化：+0 −4 行 | Facebook、LinkedIn |
| SB-935 alshuaibelectronics.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、X/Twitter、LinkedIn |
| SB-936 altronics.com.au | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-937 anewtech.net | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 840 条：2026-03-30T09:36:01 wi-fi-24ghz5ghz-industrial-iot-wireless-io-modules；2 | LinkedIn、Facebook |
| SB-938 c4line.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | LinkedIn、X/Twitter |
| SB-939 cleverkey.ru | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+4 −4 行 |  |
| SB-940 cominet.co.kr | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+15 −15 行 |  |
| SB-941 comptek.kz | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-942 dmtrade.pl | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+307 −1 行 |  |
| SB-943 dorani.com.au | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-944 fybera.com | B | 1 | 0/1 | - |  |  |
| SB-945 grep.sg | B | 4 | 2/2 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+2 −2 行 |  |
| SB-946 intrising.com.tw | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 87 条：2023-06-15T21:34:42 location_existed_prp_topology；2023-06-17T18:10:02 odm |  |
| SB-947 ison-tech.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 123 条：2021-03-01 home；2021-03-01 company；2021-03-01 core_value；2021-03-01 qual |  |
| SB-948 krysma.com.au | B | 1 | 0/1 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-950 line-net | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-951 montavue.com | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+5 −5 行 | Facebook、Instagram、LinkedIn |
| SB-952 mse.com.tw | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-953 nemon.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-954 netstar.in | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-10-23 首轮基线 |  |
| SB-955 omctech.com | B | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 home：内容变化：+290 −1 行 |  |
| SB-956 psaproducts.com.au | B | 5 | 5/0 | 2026-10-29T08:41:09Z | 2026-10-29 youtube：更新 1 条：PSA Centrii 4G Solar PT Camera - Video Manual Guide（2026-08-25T01:17:36 →  | Facebook、Instagram、LinkedIn |
| SB-957 servo-tech.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Instagram |
| SB-958 sieuthivienthong.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+436 −2 行 | Facebook、X/Twitter |
| SB-959 silarius.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+612 −2 行 |  |
| SB-960 steren.com.mx | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+194 −111 行 |  |
| SB-961 top-fa.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+4 −4 行 |  |
| SB-962 triplenet.co.kr | B | 1 | 0/1 | - |  |  |
| SB-963 unitelco.co.kr | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-964 uplinker.ru | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： mediakonverter_mc_wdm100a_mini； mediakonverter_mc_wdm100b_mini； blok_pi |  |
| SB-965 vidcom.uz | B | 2 | 2/0 | 2026-10-27T08:02:45Z | 2026-10-23 首轮基线 |  |
| SB-966 view-tel.co.kr | B | 1 | 0/1 | - |  |  |
| SB-967 ynminc.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 |  |
| SB-968 zenithtek.co.kr | B | 1 | 0/1 | 2026-10-24T04:35:40Z | 2026-10-24 首轮基线 |  |
| SB-971 IPS | B | 4 | 4/0 | 2026-10-24T07:26:33Z | 2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过）） | Facebook、LinkedIn |
| SB-972 KN Electrologic Services Ltd | B | 1 | 0/1 | - |  |  |
| SB-973 Multi Technology System | B | 2 | 1/1 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+103 −85 行 |  |
| SB-974 b-plus.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −1 行 | LinkedIn、Instagram、Facebook |
| SB-975 cctv-global.co.uk | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 |  |
| SB-976 dauren.boltaev@mail.ru | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SB-977 eltrox.cz | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+217 −1 行 |  |
| SB-978 eurobyte.co.za | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-979 iOneresources | B | 5 | 5/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook |
| SB-980 ipvoiceshop.nl | B | 2 | 2/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-981 l-com.com | B | 1 | 1/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-983 nltinc.com | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、LinkedIn |
| SB-985 qnv.com | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-986 testsol.ru | B | 3 | 3/0 | 2026-10-27T08:02:45Z | 2026-10-23 首轮基线 |  |
| SB-987 throughput.co.za | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-990 Precision | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：更新 35 条：precisionsolutions.com.br（2026-11-05 → 2026-11-06）；produtos（2026-11-05 →  | WhatsApp、WhatsApp、LinkedIn、Instagram、WhatsApp |
| SB-991 Tubal | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-23 首轮基线 | X/Twitter、LinkedIn |
| SB-992 Wave electronics Ltd | B | 4 | 4/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 |  |
| SB-993 abigo4u.com | B | 1 | 0/1 | 2026-10-27T08:02:45Z | 2026-10-27 home：内容变化：+12 −12 行 |  |
| SB-994 accuratetechnologies.com | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-11-04 youtube：新增 1 条：2026-11-03T18:44:08 Turbo Speed Measurement Demo | LinkedIn、Facebook、Instagram |
| SB-995 acixme.com | B | 6 | 6/0 | 2026-10-31T08:34:28Z | 2026-10-31 news_2：内容变化：+2 −2 行 | WhatsApp、LinkedIn、WhatsApp |
| SB-996 adj.it | B | 3 | 3/0 | 2026-10-23T04:20:51Z | 2026-10-23 首轮基线 | Facebook、Instagram、LinkedIn |
| SB-997 agmultivision.it | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+1 −1 行 | LinkedIn、Facebook、X/Twitter、Instagram |
| SB-998 akistechnologies.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 23 条：2022-08-30T11:18+00 make-customers-fall-in-love-with-you；2022-08-30T11:51 | Facebook、LinkedIn、X/Twitter |
| SB-999 algosolutions.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+3 −3 行 | LinkedIn |
| SC-001 sslcom.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-007 bornelectronics.com | B | 1 | 1/0 | 2026-11-04T09:30:29Z | 2026-11-01 首轮基线 |  |
| SC-012 LDZ Apsardze | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-04 home：内容变化：+82 −3 行 |  |
| SC-023 Central Gospel School | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-039 atwtechnology.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-10-31 首轮基线 |  |
| SC-1009 arasvarel.com | B | 2 | 2/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+4 −0 行 | Instagram、LinkedIn |
| SC-1013 gemaxxnetwork.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-1014 gtlan.com | B | 2 | 2/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1029 xentino.com | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、X/Twitter、LinkedIn、WhatsApp、Instagram |
| SC-1033 Bausch Datacom | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+7 −7 行 | LinkedIn |
| SC-1038 TELTEX | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-1042 adityagroup.com | B | 3 | 3/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+16 −3 行 |  |
| SC-1045 alfabase.co.th | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook |
| SC-1053 casmarglobal.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+222 −1 行 |  |
| SC-1117 syscom.mx | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+20 −22 行 | Facebook |
| SC-1134 xp-networks.com | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-114 Siklu Communication | B | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+8 −8 行 | LinkedIn、Facebook、X/Twitter |
| SC-1167 vmo broadband pvt ltd | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-1168 vuetec.de | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-1173 JEVASO S.L. DPTO. ELECTRONIC | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1176 PT Omni Cakrawala Komunikasi | B | 3 | 1/2 | 2026-11-05T09:39:48Z | 2026-10-31 首轮基线 |  |
| SC-1177 Projexon | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-31 首轮基线 |  |
| SC-1181 agendaage.hu | B | 1 | 1/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+30 −6 行 |  |
| SC-1191 cngsystem.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1194 eldi.no | B | 3 | 0/3 | 2026-11-05T09:39:48Z | 2026-11-05 feed_auto：新增 1 条：Mon, 02 Nov 2026 12 PH301 Bærbart Flowmeter | LinkedIn、Facebook |
| SC-1203 lapistechnologies.in | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、Instagram、LinkedIn |
| SC-1215 router.lv | B | 1 | 1/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+3 −1 行 |  |
| SC-1220 starelec.fi | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-08-12 palautusoikeus；2026-05-07 oppaat；2026-05-06 rekry；2026-04-14  |  |
| SC-1230 wantec.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 | Facebook |
| SC-1248 avensiauae.com | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | WhatsApp、Facebook、LinkedIn |
| SC-1251 bolid.ru | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+122 −10 行 |  |
| SC-1280 plcsystems.ru | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+300 −124 行 |  |
| SC-1283 reditron.co.za | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、LinkedIn |
| SC-1297 winncom.com | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1309 Elftech Co.,Ltd. | B | 3 | 1/2 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+2 −7 行 |  |
| SC-1332 dbg.co.za | B | 3 | 1/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+325 −8 行 |  |
| SC-1335 discomp.cz | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+441 −1 行 |  |
| SC-1339 econtroldevices.com | B | 5 | 5/0 | 2026-11-04T09:30:29Z | 2026-11-04 youtube：新增 1 条：2026-11-04T09:20:30 How Do Thermal Pads Help Manage Heat in Electronics? 🌡 | WhatsApp、Facebook、X/Twitter、LinkedIn |
| SC-1344 excellmedia.net | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 | Facebook、X/Twitter、LinkedIn、Instagram |
| SC-1352 globusinfocom.com | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 59 条：Mon, 18 Nov 2024 19 How IR Illuminators Enhance the Effectiveness of Yo | LinkedIn、Facebook、X/Twitter |
| SC-1365 masibus.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1366 mayenetsolutions.com | B | 1 | 0/1 | - |  |  |
| SC-1379 parks.com.br | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 3 条：2026-11-05T20:28:31 Uma Única Fibra Pode Transmitir 800 Gigabits? #shorts； | Instagram、Facebook、LinkedIn、WhatsApp |
| SC-1393 setko.uz | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+7 −7 行 | Instagram、Facebook |
| SC-1403 triflexinfo.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1443 infinique.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1446 lojacctv.com | B | 7 | 5/2 | 2026-11-03T09:43:52Z | 2026-10-29 首轮基线 | Facebook、Instagram、LinkedIn |
| SC-1450 nodexon.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 106 条：2021-10-17T09:22:47 nodexon-catalogue.pdf；2021-10-16T14:35:09 wifi6-broc |  |
| SC-1469 Defense MICE Institude | B | 3 | 0/3 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+1 −1 行 |  |
| SC-1491 distri-x.nl | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-1492 dssl.ru | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+8 −8 行 |  |
| SC-1493 duxbury.co.za | B | 5 | 5/0 | 2026-11-03T09:43:52Z | 2026-11-03 feed_auto：新增 1 条：Mon, 02 Nov 2026 10 The next network bottleneck is hiding in the uplink | LinkedIn、X/Twitter、Facebook、Instagram |
| SC-1521 nivettisystems.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 | X/Twitter、LinkedIn、LinkedIn |
| SC-1583 cartagocomex.com | B | 1 | 0/1 | 2026-11-04T09:30:29Z | 2026-10-29 首轮基线 |  |
| SC-1586 chuyendoiquang.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+10 −10 行 |  |
| SC-1605 mangcongnghiep.vn | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-1606 mangvienthong.com.vn | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-161 logilink.eu | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-1613 origo-networks.ru | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-1629 sominetworks.com | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | LinkedIn、Facebook |
| SC-1638 thuananvn.com.vn | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+2 −2 行 | Facebook、Facebook、Facebook、Facebook |
| SC-1644 vienthonghoangthach.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SC-1670 metsuki.com.vn | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1675 tekmodul.de | B | 7 | 5/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 |  |
| SC-1689 abovenet.com.br | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 feed_auto：恢复可达（上轮 HTTP 500） | LinkedIn、Instagram、Facebook |
| SC-1691 alfacomp.net | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-05T14:38:45 Como usar Modbus Read e Modbus Write nos CLPs Haiwell  | Instagram、Facebook、LinkedIn、WhatsApp |
| SC-1706 itvsecurity.com | B | 4 | 2/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 |  |
| SC-1713 oak-integrator.lv | B | 6 | 4/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 | Facebook、LinkedIn |
| SC-1714 omniray.ch | B | 7 | 5/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： railway-computer； panel-pc-tablets-display； moxa； prodvx； beijer-electr | LinkedIn、Facebook |
| SC-1715 onsite.pk | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-10-31 首轮基线 |  |
| SC-172 cop-security.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 420 条：2019-04-17T03:44:24 product.php?lang=en&tb=3&cid=264；2019-04-17T03:44:24 | Facebook、X/Twitter、LinkedIn |
| SC-1734 Joohitha Power Systems Pvt L | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-1793 axisindia.in | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-12-31 about-us；2026-05-27 brand-story；2026-05-15 code-of-conduct；20 | LinkedIn、LinkedIn、LinkedIn、LinkedIn、LinkedIn |
| SC-1795 bbcpl.in | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 | X/Twitter、Facebook、Instagram、LinkedIn |
| SC-1797 cohesiveglobal.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-09-18 smart-lock-sl30.php；2026-09-18 smart-lock-sl50.php；2026-09-18 | LinkedIn、X/Twitter、Facebook、Instagram |
| SC-1803 habari.co.tz | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-10-29 首轮基线 | WhatsApp、Instagram、Facebook、LinkedIn、X/Twitter |
| SC-1804 indraheera.com | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 279 条： sfp-transceiver-sf15tg100； sfp-transceiver-sf15tg40； sfp-transceiver-sf | Facebook、X/Twitter、LinkedIn |
| SC-1807 Mootek（mootek.in） | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1812 ns-t.ru | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-1841 cnca.com.ar | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-185 dasannetworks.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 273 条： sub02_01_02.php?mode=view&idx=72&cat_no=3； sub02_01_02.php?mode=view&id |  |
| SC-1855 kirac bilisim | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Instagram、LinkedIn |
| SC-1867 vienthonghanoi.vn | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+16 −16 行 |  |
| SC-1871 Bay datacom solutions pvt lt | B | 3 | 0/3 | - |  |  |
| SC-1881 Tss security systems | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1883 anfatech.com.vn | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 174 条：2025-02-21T00:00:11 lien-he；2023-07-09T14:35:57 test-table-press；2022-11 | Facebook、Facebook |
| SC-1900 konectsoluciones.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 386 条： camara-ip-seguridad-tiandy-exteriores-tipo-tubo-de-2mp-color-maker-con- | WhatsApp |
| SC-1916 vigilworld.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-1935 leunig.de | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+12 −5 行 |  |
| SC-1965 entegronnetwork.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、X/Twitter、LinkedIn、Instagram |
| SC-1979 switchquang.com.vn | B | 1 | 0/1 | - |  |  |
| SC-1983 vietlongtelecom.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1 −1 行 |  |
| SC-2012 VEMAX TECHNOLOGY SDN.BHD | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-11-01 home：内容变化：+0 −1 行 |  |
| SC-2021 distributor | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 | X/Twitter、Instagram、LinkedIn |
| SC-2052 Nadhimentera Engineering | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-2066 ethoswitch.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-2078 zebeye.com | B | 3 | 3/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+0 −8 行 |  |
| SC-2106 Optimal Cable Services | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 youtube：新增 1 条：2026-11-04T14:00:34 Fujikura 100R Mass Fusion Splicer: Episode 5 ／ Intelli | LinkedIn、Facebook、X/Twitter、Instagram |
| SC-2111 ami-com.ru | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+23 −20 行 |  |
| SC-2154 roundrobintech.com | B | 1 | 1/0 | 2026-11-01T09:25:59Z | 2026-11-01 home：内容变化：+18 −11 行 |  |
| SC-2208 hanutechsolution.com | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、Instagram、LinkedIn、X/Twitter、WhatsApp |
| SC-2217 Shinhoinia | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-10-31 首轮基线 |  |
| SC-2219 comelitgroup.com | B | 7 | 5/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 | Facebook、LinkedIn、Instagram |
| SC-2255 poetexas.com | B | 6 | 5/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 |  |
| SC-2256 redfox.srl | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2258 townet.it | B | 5 | 4/1 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、LinkedIn |
| SC-2262 1st-embedded.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+20 −20 行 | LinkedIn |
| SC-2372 eurosatscotland.co.uk | B | 3 | 2/1 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 | Facebook、Instagram、LinkedIn |
| SC-2383 3grouterstore.co.uk | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+782 −8 行 |  |
| SC-2402 sisegusa.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： combo4-1-ds-7104hghi-m1-t-2-ds-2ce16d0t-lpfs-2-ds-2ce76d0t-lpfs-4-ds-1h |  |
| SC-2418 streakwave.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-08-06 promotions；2026-07-28 ubiquiti-enterprise；2026-07-28 memory-s | LinkedIn、Facebook、X/Twitter、X/Twitter |
| SC-2429 epcom.net | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、Instagram、LinkedIn |
| SC-2452 a-secur.com | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2481 Okisan | B | 6 | 6/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、X/Twitter、LinkedIn、Instagram |
| SC-2488 fiber24.net | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2510 getfort.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+3 −0 行 |  |
| SC-2516 novuscctv.com | B | 7 | 1/6 | 2026-11-05T09:39:48Z | 2026-11-05 news_2：内容变化：+76 −75 行 |  |
| SC-2542 gridconnect.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+95 −3 行 | LinkedIn、X/Twitter |
| SC-257 Al Rajhi Telecommunication ( | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Instagram、Facebook、X/Twitter、LinkedIn |
| SC-2587 tactio.net | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2598 digital-watchdog.com | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+418 −1 行 | Facebook、X/Twitter、LinkedIn、Instagram |
| SC-2606 logicbus.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 50 条：Fri, 6 Nov 2026 00: 6069-410-026；Fri, 6 Nov 2026 00: 6069-410-120；Fri,  |  |
| SC-2608 mayflex.com | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2609 partizanstore.eu | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 | Facebook、Instagram |
| SC-2637 ORIENT TELECOMS | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-31 首轮基线 |  |
| SC-2657 lynnelec.com | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | LinkedIn |
| SC-2684 hirtv.net | B | 1 | 0/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-2695 everfocus.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 3 条：2026-11-05T22:18:37 Scaling real-time edge AI: University of Alabama crowd | Facebook、LinkedIn、LinkedIn |
| SC-2718 mercasat.es | B | 3 | 1/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+43 −43 行 |  |
| SC-2725 todotelecom.com | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+283 −10 行 |  |
| SC-274 alcadon.no | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 21 条：06.11.2026 10:53:53 Strømkabel C20 – C21, Sort, 3m；09.10.2026 09:46:12  |  |
| SC-276 assmann.pl | B | 4 | 4/0 | 2026-11-04T09:30:29Z | 2026-11-04 youtube：新增 1 条：2026-11-04T06:26:47 DIGITUS CAT 6A compact keystone module ／ shielded ／ to | LinkedIn、Facebook、Instagram |
| SC-2760 tempelgroup.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2776 karel.com.tr | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： www.karel.com.tr；2024-01-24T11:33Z ve-ev-alarm-sistemleri；2024-01-24T10 | Instagram、X/Twitter、Facebook、LinkedIn |
| SC-2813 siospa.it | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-2823 ST SPACE TECHNOLOGY | B | 3 | 1/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 |  |
| SC-283 comonyx.com | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+64 −4 行 |  |
| SC-2834 Dipol | B | 5 | 3/2 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+638 −1 行 | Facebook |
| SC-2839 neousys-tech.com | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-284 dcbnet.com | B | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-10-29 首轮基线 |  |
| SC-2846 DEONET | B | 1 | 0/1 | - |  |  |
| SC-2857 Tropical Computers Cairns | B | 2 | 0/2 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-2885 LS Networks (Pty) Ltd | B | 4 | 3/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 | Facebook、Instagram、LinkedIn |
| SC-2891 trimatrikbd.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 801 条：2025-07-23 hundure-rac-520；2025-07-23 ahuja-dxa-2502-amplifiers-dual-cha |  |
| SC-291 fgss.asia | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-292 fiberinstrumentsales.com | B | 1 | 0/1 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+1 −56 行 |  |
| SC-2941 digitx.it | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、LinkedIn、X/Twitter |
| SC-2943 extralink24.com | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+6 −10 行 |  |
| SC-295 inline.uz | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+5 −5 行 | Facebook、Instagram |
| SC-2954 videcon.co.uk | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+0 −1 行 | LinkedIn、Facebook、Instagram |
| SC-2955 Continental Towers Guaatemal | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-2957 conexpro.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 648 条： product； product； product； product； product； product； product； product… |  |
| SC-2969 metrikingdom.com | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-2976 blake-uk.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： www.blake-uk.com；2026-11-06T07:06:10 6x125-18g-1828-x32-x12mm-cranked-a |  |
| SC-298 miro.co.za | B | 1 | 0/1 | 2026-11-03T09:43:52Z | 2026-11-03 home：内容变化：+319 −5 行 |  |
| SC-299 nag.kz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+194 −62 行 |  |
| SC-2993 cablesnmore.com | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2023-02-10 audio-video；2016-03-10 adaptersconverters；2016-03-10 usb-adap |  |
| SC-3007 ks-itsolutions.com | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-302 osnovo.ru | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+4 −4 行 |  |
| SC-3023 nettrans.pl | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 |  |
| SC-3026 说是有需求会说的，问了catalog | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-305 prosoft.ru | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+5 −12 行 | Facebook、X/Twitter、Facebook、X/Twitter、Facebook |
| SC-311 videoglaz.ru | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-3130 tvc.mx | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+13 −0 行 | Facebook、LinkedIn、WhatsApp |
| SC-3133 federalcable.net | B | 1 | 1/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+2 −2 行 |  |
| SC-3135 sphinxcomputer.fr | B | 4 | 2/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-09-02T13:03:13 dse.php；2025-09-02T13:03:13 cookie.php；2025-09-02T13 |  |
| SC-3149 starcom.com.pk | B | 4 | 3/1 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 |  |
| SC-3198 techroutes.com | B | 2 | 2/0 | 2026-11-03T09:43:52Z | 2026-11-03 feed_auto：新增 1 条：Mon, 02 Nov 2026 10 AG3100-16O |  |
| SC-3203 jteemsolutions.com | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-3204 koc.com.cn | B | 1 | 1/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+1 −1 行 |  |
| SC-323 comptek.ru | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+19 −19 行 |  |
| SC-324 enercore.co.in | B | 1 | 1/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-3249 te.eg | B | 1 | 1/0 | 2026-11-04T09:30:29Z | 2026-11-04 home：内容变化：+0 −3 行 |  |
| SC-3302 niveoprofessional.com | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | LinkedIn |
| SC-331 industrialcomms.com | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-343 optilinknetwork.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+23 −7 行 | Facebook、LinkedIn、Instagram |
| SC-345 pine-networks.com | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | LinkedIn |
| SC-364 EasyWind GmbH | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-368 Itmax system sdn bhd | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-31 首轮基线 |  |
| SC-380 iptime.com | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 feed_auto：新增 13 条：Fri, 06 Nov 2026 08 [ipTIME 카메라] 홈캠 AI 감지는 유료인가요? 구독해야 하나요?；Fri, 06 Nov |  |
| SC-382 securitywarehouse.co.za | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+2 −2 行 | Facebook、LinkedIn |
| SC-387 DGTAS | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+0 −2 行 |  |
| SC-397 alloy.com.au | B | 2 | 2/0 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 | Facebook、X/Twitter、Instagram、LinkedIn |
| SC-413 hifocuscctv.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 2 条：2026-11-06T05:30:34 Shagun Ka Hisaab, Hi-Focus CCTV Ke Saath! 💸😂 ／ Diwali  | WhatsApp、Facebook、Instagram、LinkedIn |
| SC-427 tbkvision.com | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-432 CabNet Systems(M) Sdn. Bhd | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-31 首轮基线 |  |
| SC-439 IRnow Sdn Bhd | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-31 首轮基线 |  |
| SC-455 ags-electronics.com | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | LinkedIn、Facebook、X/Twitter、Instagram |
| SC-463 atronic.co.in | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | LinkedIn |
| SC-465 avtech.com.tw | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-468 bkeesti.ee | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-485 fxc.jp | B | 4 | 4/0 | 2026-11-04T09:30:29Z | 2026-11-04 news_1：内容变化：+588 −1 行 | Facebook |
| SC-490 hattelandtechnology.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2025-11-26 jh-17tap-std_accessory_118；2025-11-26 p006997-1_accessory_475 | Facebook、LinkedIn |
| SC-491 hisharp.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 263 条：2026-07-28 news.php?act=view&id=149；2026-07-08 news.php?act=view&id=148； | Facebook |
| SC-493 idisglobal.com | B | 5 | 5/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | X/Twitter、Facebook、LinkedIn |
| SC-503 lutze.com | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+12 −3 行 | LinkedIn |
| SC-509 nextik.co.in | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、Instagram、LinkedIn、X/Twitter |
| SC-562 balticnetworks.com | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+1503 −7 行 | Facebook、LinkedIn、X/Twitter |
| SC-568 efb-elektronik.de | B | 2 | 2/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+314 −1 行 |  |
| SC-571 gsl.com.tr | B | 5 | 4/1 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+25 −25 行 | LinkedIn、Instagram、Facebook、X/Twitter |
| SC-575 kst-bg.com | B | 5 | 3/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 | Facebook |
| SC-577 leap-networks.ae | B | 4 | 4/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 |  |
| SC-619 hdcabling.co.za | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+175 −120 行 |  |
| SC-622 iacontrol.co.za | B | 2 | 1/1 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 |  |
| SC-623 industrialnets.ru | B | 4 | 4/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+4 −4 行 |  |
| SC-625 ipmatika.ru | B | 7 | 7/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-05T11:04:37 Новинки от Fanvil — Wi-Fi-SIP-телефоны W626W, новые ин |  |
| SC-634 newtechindustries.com | B | 1 | 1/0 | 2026-11-06T09:32:27Z | 2026-11-06 home：内容变化：+44 −44 行 |  |
| SC-644 scoop.co.za | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-656 100mega.cz | B | 5 | 3/2 | 2026-11-05T09:39:48Z | 2026-11-05 news_1：内容变化：+147 −2 行 |  |
| SC-665 Civitas systems Srl | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-31 首轮基线 |  |
| SC-670 Lansale LLC (Russia) | B | 3 | 0/3 | - |  |  |
| SC-671 Leader Optec | B | 5 | 4/1 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 | LinkedIn、Facebook、Instagram |
| SC-672 Ministry of interior RAK pol | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-676 Puncak Niaga Holdings | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-678 QVIS | B | 3 | 3/0 | 2026-10-31T08:34:28Z | 2026-10-29 首轮基线 | Facebook、LinkedIn |
| SC-679 SPECTRUM | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-680 SUREN Smart Electrical | B | 1 | 0/1 | 2026-11-01T09:25:59Z | 2026-11-01 首轮基线 |  |
| SC-683 VOYGAR SYSTEMS GmbH | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_1：内容变化：+1 −1 行 | Facebook、LinkedIn |
| SC-700 amc-systeme.de | B | 3 | 3/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条： digital-io-steuerkarten.html； messgeraete-karten.html； motorsteuer-und- |  |
| SC-704 annicom.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 | LinkedIn |
| SC-708 armosystems.ru | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+24 −33 行 |  |
| SC-714 avant.by | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T09:40:31 Как организовать доступ на одну дверь без сложной сист | Facebook、Instagram、LinkedIn |
| SC-722 bic-video.ru | B | 6 | 6/0 | 2026-11-06T09:32:27Z | 2026-11-06 telegram：内容变化：+22 −23 行 |  |
| SC-729 brownbear.ru | B | 5 | 5/0 | 2026-11-06T09:32:27Z | 2026-11-06 news_2：内容变化：+2 −3 行 |  |
| SC-770 elmark.com.pl | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-06T08:00:31 Falownik czy serwonapęd? Sterowanie prędkością serwa E | LinkedIn、Facebook |
| SC-782 exara.ru | B | 1 | 0/1 | 2026-11-04T09:30:29Z | 2026-10-29 首轮基线 |  |
| SC-783 expressalarm.cz | B | 4 | 0/4 | 2026-11-05T09:39:48Z | 2026-11-05 sitemap：新增 745 条：2026-03-03 12-internal34；2025-05-23 2n-produktove-skoleni-internal；2025- |  |
| SC-817 infiber.ru | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-838 koscomcable.com | B | 1 | 0/1 | 2026-10-31T08:34:28Z | 2026-10-31 首轮基线 |  |
| SC-855 mastdigital.co.uk | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-884 novicam.ru | B | 8 | 8/0 | 2026-11-06T09:32:27Z | 2026-11-06 youtube：新增 1 条：2026-11-05T15:00:33 Бесконтактная кнопка выхода Novicam B70SLW BLACK! Подн |  |
| SC-897 pixietech.uz | B | 2 | 2/0 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：更新 9 条：ru（2026-11-05T08:02:22 → 2026-11-06T10:00:21）；switches（2026-11-05T08:02:22 |  |
| SC-898 plexonics.com | B | 1 | 1/0 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-908 prumysloveswitche.cz | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 |  |
| SC-925 sarcitalia.it | B | 3 | 1/2 | 2026-11-01T09:25:59Z | 2026-10-29 首轮基线 |  |
| SC-935 semaphore-systems.co.uk | B | 1 | 0/1 | 2026-10-29T15:11:51Z | 2026-10-29 首轮基线 |  |
| SC-956 systerra.de | B | 6 | 4/2 | 2026-11-06T09:32:27Z | 2026-11-06 sitemap：新增 820 条：2026-11-05 SRS-3201-BLUBOXX.html；2026-11-05 SRS-4401-SERIAL.html；2026-11 |  |
| SC-969 trueview.co.in | B | 4 | 4/0 | 2026-11-05T09:39:48Z | 2026-11-05 home：内容变化：+438 −1 行 | X/Twitter、Facebook、Instagram、LinkedIn |
