# -*- coding: utf-8 -*-
"""第 132 批（T29-U118f，2026-10-29）—— **C 池三闸 · 闸 2 第九批**：闸 1 第 34 批（桶 ⑥ 收口段 第 1211–1257 户）候选 3 户查底数（MX / PK / IN 各 1）。
路径：MX → cosmos.com.mx + comxport（RFC / S.A. de C.V. / 地址）+ LinkedIn（规模 / 成立）；PK → rocketreach / zoominfo（法人名 / 地址 / CEO / 规模；SECP 登记号未取）；IN → zaubacorp / instafinancials（CIN / 实收 / 注册地址 / MCA 邮箱）+ indiamart（业务 / 营业额 / IEC）。
每户 1 查、depth 1。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 132
F = '2026-10-29'
IN = '— 印度常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 / 微型 预付 100%）+ FOB 深圳 / DAP 买方清关（进口认证要求由买方核，Saga 仅 CE / RoHS / FCC / REACH / UKCA）；周二 / 周四 11–13 IST'
OT = '— 其他区常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 / 微型 预付 100%）+ FOB 深圳 / DAP 买方清关；周二 / 周四 当地 10–12'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 墨西哥 ----------------
row('SC-3130', 'other', 'TVC en Línea.com, S.A. de C.V.（tvc.mx；**RFC TVC060802NE4；Camino al Mirador No. 5216, Col. Del Paseo Residencial 6to Sector, 64920 Monterrey, N.L.（comxport / cosmos）；LinkedIn：电子安防解决方案批发商（mayorista），2000 年创立，201–500 人，总部 Av. Lázaro Cárdenas 2611 Monterrey + 墨西哥城 Azcapotzalco 分部；进出口 批发 电信（comxport）；Tel 0133 1202 1777**）；表内：Utepo / 大华 CCTV 大分销，官网 WA +52 81 1799 1777', 'MX',
    'MX · 1 次检索：comxport（RFC / 法人名 / 地址 / 进出口）+ cosmos.com.mx（业务 / 地址）+ LinkedIn（2000 / 201–500 人 / 两地）；2026-10-29', 'https://www.comxport.com/co/tvc_en_lineacom_sa_de_cv-mexico-350701.php',
    'TVC060802NE4（RFC）', '营业中（LinkedIn / 目录 2025）', '2000（RFC 序列 2006-08-02）', 'S.A. de C.V.', '电子安防 / CCTV 批发分销（蒙特雷 + 墨西哥城）', 'Camino al Mirador No. 5216, Col. Del Paseo Residencial, 64920 Monterrey, Nuevo León', '大型（201–500 人；两地）',
    ['（具名 KP 未取；soporte@ 为支持信箱 → 需 ventas / compras）'],
    '**墨西哥 · CCTV 大分销 20%（长线）：WA + 换采购地址一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 分销价 + MOQ 1 + 付费样机；Utepo 不点名；西语稿可）' + OT + '**',
    '分销 20%；P 池候选 ★（大分销 ✔ 中国品牌进口 ✔ 对位 ✔ 坐实 ✔ 墨西哥先例 SYSCOM ✔）；坐实（RFC）。')

# ---------------- 巴基斯坦 ----------------
row('SC-3149', 'other', 'Starcom Technologies (Pvt) Limited — Star Communication Services（starcom.com.pk / starcom.net.pk；**Suite 401-A, Panorama Centre II, Raja Ghazanfar Ali Rd, Saddar, Karachi 75460；2004 创立；22–32 人；营收 $5.3M（zoominfo / rocketreach）；CEO Asghar Ali；+92 21 3566 1550；电信 + 数据网络项目实施（电话系统 → 宽带互联网络）；拉合尔销售 Farooq Shah（General Sales Manager）**）；SECP 登记号未取；表内：从 Raisecom 买一些产品；2026-02-26 真人回「请用公司域名邮箱发」；ali@ + 手机 +92 300 202 1141', 'PK',
    'PK · 1 次检索：rocketreach（法人名 / 地址 / 2004 / 人数 / 营收）+ zoominfo（CEO / 电话）；SECP 未取；2026-10-29', 'https://rocketreach.co/starcom-technologies-pvt-limited-profile_b5c15b82f42e0895',
    '未取（SECP 登记号未查；法人名目录坐实）', '营业中（目录 2025）', '2004', '(Pvt) Limited', '电信 / 数据网络系统集成（卡拉奇 + 拉合尔）', 'Suite 401-A, Panorama Centre II, Saddar, Karachi, Sindh 75460', '小型（22–32 人；$5.3M）',
    ['Asghar Ali — CEO', 'Farooq Shah — General Sales Manager（Lahore）'],
    '**巴基斯坦 · 集成 25% + 预付 100%：用 sagatele.com 域名邮箱回 ali@ 一页纸一次（STC-228GP / STC-2224GP / STC-4424GCPM + STI-288GPM 工业线 + MOQ 1 + 付费样机；Raisecom 不点名）' + OT + '**',
    '集成 25%；P 池候选 ○（真人回 ✔ 进口中国同类 ✔ 对位 ✔ 决策人具名 ✔；巴基斯坦非点名国 → 预付 100%）；部分坐实（SECP 未取）。')

# ---------------- 印度 ----------------
row('SC-3198', 'in', 'Techroutes Network Private Limited（techroutes.com；**CIN U72200RJ2003PTC018583（现）/ 原 U72900HR2003PTC035992（自 Jaipur 迁 Haryana 再迁）；注册号 35992；2003-09-11 成立；ROC Delhi；授权 / 实收 ₹2 Cr；Sun Tower, 2nd Floor, Main M.G. Road, Sukhrali, Gurgaon 122001；MCA 邮箱 acct@techroutes.com；ISO 9001；自有产品线 路由器 / 交换机 / VoIP / VPN / 宽带，经分销商 / SI / VAR 销售（indiamart：营业额 ₹5–25 Cr，IEC 在册，GST 06…2ZI）**）；表内：商业 FS + 工业 FS switch；dinesh.rastogi@ / kdeepak@；手机 93000 69633；Simon 标 Spam', 'IN',
    'IN · 1 次检索：zaubacorp（CIN / 地址 / MCA 邮箱）+ instafinancials（成立 / 实收 / 前 CIN）+ indiamart（业务 / 营业额 / IEC）；2026-10-29', 'https://www.instafinancials.com/company/techroutes-network-private-limited-U72200RJ2003PTC018583',
    'U72200RJ2003PTC018583（CIN；原 U72900HR2003PTC035992）', 'Active（MCA 2026-07）', '2003-09-11', 'Private Limited', '自有品牌网络设备（路由 / 交换 / VoIP）+ 分销网络（古尔冈）', 'Sun Tower, 2nd Floor, Main M.G. Road, Sukhrali, Gurgaon, Haryana 122001', '中型（实收 ₹2 Cr；营业额 ₹5–25 Cr；IEC）',
    ['Dinesh Rastogi — 表内具名 KP（职务未取）', 'K. Deepak — 表内具名 KP（职务未取）'],
    '**印度 · 自有品牌 OEM 30%：点名 Dinesh Rastogi 一页纸一次（STC-228GP $33 / STC-2224GP $86 / STC-4424GCPM $165 + STI-288GPM 工业线 中性包装 + 贴 Techroutes 牌 + MOQ 1 + 付费样机）' + IN + '**',
    'OEM 30%；P 池候选 ★（自有品牌经分销销售 ✔ 印度点名国 ✔ 对位 ✔ 决策人具名 ✔ 坐实 ✔；Simon 曾标 Spam → 可否决）；坐实（CIN）。')

print('b132_c done')
