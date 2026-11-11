#!/usr/bin/env python3
"""Generate the JoyHome UK static pages.

Shared header / footer live here; each page's body is a function below.
Run from the repo root:  python3 _build/build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://uxcircles.github.io/joyhomeuk/"
OFFICIAL = "https://joyhomeuk.com/"
CSS_V = 3
JS_V = 2

PHONE = "+44 7511 817812"
TEL = "+447511817812"
WA = "447511817812"
EMAIL = "joyhomeuk@gmail.com"
FB = "https://www.facebook.com/JoyhomeUK"
PRS_NO = "PRS029811"
AREAS = ["North London", "Milton Keynes", "St Albans", "Hertfordshire", "Surrey", "Luton",
         "Northampton", "Birmingham", "Nottingham", "Leeds", "Warrington"]

LANG = "zh"  # en.py switches this to "en"

UI = {
    "zh": dict(skip="跳到主要內容", concept='網站改版概念設計，並非 <a href="{o}" target="_blank" rel="noopener">JoyHome UK 官方網站</a>。',
               home="JoyHome UK 主頁", menu="主選單", wa_ask="WhatsApp 查詢", open_menu="開啟選單", close_menu="關閉選單",
               about="2015 年成立的英國物業顧問。以廣東話為香港及海外客戶處理英國買樓、租屋、物業管理及裝修。",
               f_svc="服務", f_acc="認證", f_contact="聯絡", ukala="UKALA 會員", cmp="客戶款項保障 CMP", cmh="客戶款項處理指引",
               prs="PRS 編號", hours="星期一至五 9:00–17:00（英國時間）", official="官方網站", by="改版概念設計",
               quick="快速聯絡", call="致電", mail="電郵", crumbs="頁面位置", crumb_home="主頁", book="預約諮詢", wa_us="WhatsApp 我們",
               faq="常見問題", faq_more="問題不在這裡？直接問我們", form="填寫查詢表",
               cta_h="想先聽聽專業意見？", cta_p="告訴我們你的地區、預算和時間表，顧問會以廣東話回覆，替你判斷下一步應該怎樣走。",
               lang_label="English", lang_short="EN", lang_code="en"),
    "en": dict(skip="Skip to main content", concept='Concept redesign. Not the <a href="{o}" target="_blank" rel="noopener">official JoyHome UK website</a>.',
               home="JoyHome UK home", menu="Main menu", wa_ask="WhatsApp us", open_menu="Open menu", close_menu="Close menu",
               about="UK property consultants since 2015, helping families from Hong Kong and overseas buy, rent, let and renovate homes in England.",
               f_svc="Services", f_acc="Accreditation", f_contact="Contact", ukala="UKALA member", cmp="Client Money Protection", cmh="Client money handling guide",
               prs="PRS number", hours="Mon–Fri 9:00–17:00 (UK time)", official="Official website", by="Concept redesign by",
               quick="Quick contact", call="Call", mail="Email", crumbs="Breadcrumb", crumb_home="Home", book="Book a consultation", wa_us="WhatsApp us",
               faq="FAQ", faq_more="Can't find your question? Ask us", form="Send an enquiry",
               cta_h="Want a professional opinion first?", cta_p="Tell us the area, budget and timeline. A consultant will reply in English or Cantonese and suggest your next step.",
               lang_label="繁體中文", lang_short="中", lang_code="zh-Hant-HK"),
}


def T(key):
    return UI[LANG][key]


NAV = [
    ("services.html", "服務及收費"),
    ("buy.html", "英國買樓"),
    ("rent.html", "英國租屋"),
    ("management.html", "物業管理"),
    ("renovation.html", "英國裝修"),
    ("contact.html", "聯絡我們"),
]
NAV_EN = [
    ("services.html", "Services & fees"),
    ("buy.html", "Buying"),
    ("rent.html", "Renting"),
    ("management.html", "Lettings"),
    ("renovation.html", "Renovation"),
    ("contact.html", "Contact"),
]


def nav_items():
    return NAV if LANG == "zh" else NAV_EN

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
  <symbol id="i-alert" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 8v4.5M12 16h.01"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M5 4h3.5l1.8 4.5-2.3 1.4a11 11 0 0 0 6.1 6.1l1.4-2.3L20 15.5V19a1.5 1.5 0 0 1-1.6 1.5A16.5 16.5 0 0 1 3.5 5.6 1.5 1.5 0 0 1 5 4Z"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path d="M12 2.2A9.7 9.7 0 0 0 3.6 16.8L2.3 21.7l5-1.3A9.7 9.7 0 1 0 12 2.2Zm0 17.7a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1 1 12 19.9Zm4.4-6c-.2-.1-1.4-.7-1.7-.8-.2-.1-.4-.1-.5.1l-.8 1c-.1.2-.3.2-.5.1a6.6 6.6 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.5-.4h-.5a.9.9 0 0 0-.6.3 2.7 2.7 0 0 0-.8 2c0 1.2.9 2.3 1 2.5.1.2 1.7 2.6 4.1 3.7 1.5.7 2.1.7 2.9.6.5-.1 1.4-.6 1.6-1.1.2-.6.2-1 .1-1.1l-.4-.3Z"/></symbol>
  <symbol id="i-ext" viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></symbol>
  <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6L12 3Z"/><path d="m8.8 12 2.2 2.2 4.2-4.4"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
  <symbol id="i-home" viewBox="0 0 24 24"><path d="M3.5 11 12 4l8.5 7"/><path d="M5.5 9.5V20h13V9.5"/><path d="M10 20v-5.5h4V20"/></symbol>
  <symbol id="i-key" viewBox="0 0 24 24"><circle cx="8" cy="15" r="4"/><path d="m10.8 12.2 8.7-8.7M16.5 6.5l2.5 2.5M14 9l2 2"/></symbol>
  <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
  <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4V5Z"/><path d="M8 9.5h8M8 12.5h5"/></symbol>
  <symbol id="i-pound" viewBox="0 0 24 24"><path d="M16.5 6.5A3.8 3.8 0 0 0 9 7.5V19M6 19h12M6.5 12.5h7"/></symbol>
  <symbol id="i-tool" viewBox="0 0 24 24"><path d="M14.5 6.5a4 4 0 0 0 5 5L12 19a2.1 2.1 0 0 1-3-3l7.5-7.5"/><path d="M14.5 6.5 17 4l3 3-2.5 2.5"/></symbol>
  <symbol id="i-doc" viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6V3Z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></symbol>
  <symbol id="i-eye" viewBox="0 0 24 24"><path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18.5 14a6.5 6.5 0 0 1 3 6"/></symbol>
  <symbol id="i-trend" viewBox="0 0 24 24"><path d="m3 17 6-6 4 4 8-8"/><path d="M15 7h6v6"/></symbol>
  <symbol id="i-fb" viewBox="0 0 24 24"><path d="M14 8.5V6.8c0-.8.2-1.3 1.4-1.3H17V2.6A21 21 0 0 0 14.6 2.5C12.2 2.5 10.6 4 10.6 6.6v1.9H8v3.2h2.6V21.5H14v-9.8h2.6l.4-3.2H14Z"/></symbol>
</svg>"""

MARK = """<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="#1F4670"/><path d="M12.5 10.5v15a4 4 0 0 1-4 4" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><path d="M20.5 12.5v9M28.5 12.5v9M20.5 17h8" fill="none" stroke="#BDAF8E" stroke-width="2" stroke-linecap="round"/><circle cx="12.5" cy="6.6" r="1.6" fill="#BDAF8E"/></svg>"""


def icon(name, cls="icon"):
    fill = " icon-fill" if name in ("wa", "fb") else ""
    return f'<svg class="{cls}{fill}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def ext():
    return icon("ext")


def header(active, slug):
    alt = ("en/" if LANG == "zh" else "../") + slug
    items = "\n".join(
        f'          <li><a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in nav_items())
    return f"""  <a class="skip" href="#main">{T("skip")}</a>
  {SPRITE}
  <div class="concept-bar" role="note">
    <div class="wrap concept-inner">
      <p><span class="concept-tag">Concept</span><span class="concept-long">{T("concept").format(o=OFFICIAL)}</span></p>
      <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener">Designed by <strong>UX CIRCLES</strong> {ext()}</a>
    </div>
  </div>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="index.html" aria-label="{T("home")}">
        {MARK}
        <span class="brand-word"><span class="brand-name">JoyHome UK</span><span class="brand-tag">Bring Home the Joy</span></span>
      </a>
      <nav class="nav" id="site-nav" aria-label="{T("menu")}" data-nav>
        <ul class="nav-list">
{items}
        </ul>
        <div class="nav-extra">
          <a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}{T("wa_ask")}</a>
          <a class="btn btn-ghost" href="tel:{TEL}">{icon("phone")}{PHONE}</a>
        </div>
      </nav>
      <div class="header-cta">
        <a class="lang" href="{alt}" lang="{T("lang_code")}" hreflang="{T("lang_code")}" aria-label="{T("lang_label")}">{T("lang_short")}</a>
        <a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}WhatsApp</a>
        <button class="burger" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{T("open_menu")}" data-open="{T("open_menu")}" data-close="{T("close_menu")}"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>"""


def footer():
    areas = " · ".join(AREAS)
    links = "\n".join(f'          <li><a href="{h}">{l}</a></li>' for h, l in nav_items()[:5])
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <a class="brand" href="index.html" aria-label="{T("home")}">
            {MARK}
            <span class="brand-word"><span class="brand-name">JoyHome UK</span><span class="brand-tag">Bring Home the Joy</span></span>
          </a>
          <p>{T("about")}</p>
          <div class="social"><a href="{FB}" target="_blank" rel="noopener" aria-label="JoyHome UK Facebook">{icon("fb")}</a><a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon("wa")}</a></div>
        </div>
        <div>
          <h4>{T("f_svc")}</h4>
          <ul>
{links}
          </ul>
        </div>
        <div>
          <h4>{T("f_acc")}</h4>
          <ul>
            <li><a href="https://www.joyhomeuk.com/wp-content/uploads/2020/07/UKALA.pdf" target="_blank" rel="noopener">{T("ukala")}</a></li>
            <li><a href="https://www.joyhomeuk.com/wp-content/uploads/2020/07/CMP.pdf" target="_blank" rel="noopener">{T("cmp")}</a></li>
            <li><a href="https://www.joyhomeuk.com/wp-content/uploads/2020/07/UKALA-Client-Money-Handling.pdf" target="_blank" rel="noopener">{T("cmh")}</a></li>
            <li>{T("prs")} {PRS_NO}</li>
          </ul>
        </div>
        <div>
          <h4>{T("f_contact")}</h4>
          <ul>
            <li><a href="tel:{TEL}">{PHONE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{T("hours")}</li>
          </ul>
          <p class="footer-areas">{areas}</p>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© <span data-year>2026</span> JoyHome UK. All rights reserved.</p>
        <p>{T("official")} <a href="{OFFICIAL}" target="_blank" rel="noopener">joyhomeuk.com {ext()}</a> · {T("by")} <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener">UX CIRCLES {ext()}</a></p>
      </div>
    </div>
  </footer>

  <nav class="action-bar" aria-label="{T("quick")}">
    <a class="is-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}WhatsApp</a>
    <a href="tel:{TEL}">{icon("phone")}{T("call")}</a>
    <a href="mailto:{EMAIL}">{icon("mail")}{T("mail")}</a>
  </nav>"""


def page(slug, title, desc, body, active=None, preload=None):
    path = "" if slug == "index.html" else slug.replace(".html", "")
    zh_url, en_url = BASE + path, BASE + "en/" + path
    url = zh_url if LANG == "zh" else en_url
    pre = f'\n  <link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ""
    html = f"""<!doctype html>
<html lang="{"zh-Hant-HK" if LANG == "zh" else "en-GB"}" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#F7F4EE">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="zh-Hant" href="{zh_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="JoyHome UK">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}assets/img/hero.webp">{pre}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css?v={CSS_V}">
  <script>document.documentElement.classList.replace('no-js','js')</script>
</head>
<body>
{header(slug if active is None else active, slug)}

  <main id="main">
{body}
  </main>

{footer()}
  <script src="assets/js/main.js?v={JS_V}" defer></script>
</body>
</html>
"""
    out = ROOT / slug
    if LANG == "en":
        html = re.sub(r'(?<![/\w.])assets/', '../assets/', html)
        out = ROOT / "en" / slug
        out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


def crumbs(label):
    return f"""<nav class="crumbs" aria-label="{T("crumbs")}"><ol><li><a href="index.html">{T("crumb_home")}</a></li><li aria-current="page">{label}</li></ol></nav>"""


def page_hero(label, eyebrow, h1, lead, img=None, alt="", ctas=True):
    btns = f"""
          <div class="btn-row">
            <a class="btn btn-primary" href="contact.html">{T("book")}</a>
            <a class="btn btn-ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}{T("wa_us")}</a>
          </div>""" if ctas else ""
    media = f"""
        <div class="page-hero-media"><img src="{img}" alt="{alt}" width="1024" height="768"></div>""" if img else ""
    return f"""    <section class="page-hero">
      <div class="wrap">
        {crumbs(label)}
        <div class="page-hero-grid{'' if img else ' no-media'}">
          <div>
            <p class="eyebrow">{eyebrow}</p>
            <h1>{h1}</h1>
            <p class="lead">{lead}</p>{btns}
          </div>{media}
        </div>
      </div>
    </section>"""


def faq(items):
    out = []
    for q, a in items:
        out.append(f"""          <details>
            <summary>{q}</summary>
            <div class="faq-a"><p>{a}</p></div>
          </details>""")
    return '        <div class="faq">\n' + "\n".join(out) + "\n        </div>"


def faq_section(title, lead, items, bg=""):
    return f"""    <section class="section{bg}" id="faq">
      <div class="wrap faq-wrap">
        <div class="head">
          <p class="eyebrow">{T("faq")}</p>
          <h2>{title}</h2>
          <p class="lead">{lead}</p>
          <a class="link-arrow" href="contact.html">{T("faq_more")}</a>
        </div>
{faq(items)}
      </div>
    </section>"""


def cta_band(h=None, p=None):
    h, p = h or T("cta_h"), p or T("cta_p")
    return f"""    <section class="section tight">
      <div class="wrap">
        <div class="cta-band reveal">
          <div>
            <h2>{h}</h2>
            <p>{p}</p>
            <p class="contact-lines">{T("hours")} · {EMAIL}</p>
          </div>
          <div class="btn-row">
            <a class="btn btn-gold" href="contact.html">{T("form")}</a>
            <a class="btn btn-ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}WhatsApp</a>
          </div>
        </div>
      </div>
    </section>"""


def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in items) + "</ul>"


# ------------------------------------------------------------------ pages

TYPES = [
    ("house-detached", "獨立屋", "Detached House", ["私隱度最高", "預算最高"],
     "獨自一棟，不與其他物業相連。空間感十足，通常有前後大花園及獨立車位。大型的又稱豪宅（Mansion）。"),
    ("house-semi", "半獨立屋", "Semi-detached House", ["最受家庭歡迎"],
     "一面牆與鄰屋相連，左右各一戶。私隱度高，多數有前後花園及車位，預算僅次於獨立屋，出租需求亦最穩定。"),
    ("house-terrace", "排屋", "Terraced House", ["性價比高"],
     "一整排房屋相連，牆身之間沒有空隙。居住空間較獨立屋少，與鄰居關係較緊密；舊式排屋要留意滲水和結構老化。"),
    ("house-bungalow", "單層平房", "Bungalow", ["適合長者"],
     "只有一層、沒有樓梯的房屋，適合三代同堂或有長者的家庭，土地面積通常較大。"),
    ("house-maisonette", "分層單位", "Maisonette", ["獨立入口"],
     "通常是一棟兩層的房屋分成上下兩個單位，各自有獨立入口，價錢介乎公寓和排屋之間。"),
    ("house-flat", "公寓", "Apartment / Flat / Studio", ["入場門檻低"],
     "與香港常見的大廈單位相似。新式公寓有電梯、大堂及會所；舊式可能只有數層、沒有電梯。多為 Leasehold，要留意地租及管理費。"),
]


def build_index():
    trust = "".join(f"<li>{icon('shield')}{t}</li>" for t in
                    [f"PRS 註冊 {PRS_NO}", "UKALA 會員", "客戶款項保障 CMP"])
    areas = "".join(f"<li>{a}</li>" for a in AREAS)
    diffs = [
        ("更適切的樓盤選擇", "先了解家庭成員、校網、通勤和預算，才開始搜盤，不會把你推向代理手上最想賣的單位。"),
        ("提升物業的未來價值", "每個單位都提供正反分析：街道、Leasehold 年期、維修狀況、轉售及出租潛力，一併寫清楚。"),
        ("協助你降低成本", "代你出價議價，並轉介可靠的測量師、按揭經紀和律師；議價成功才按差價收取 10%。"),
        ("分擔找樓的壓力", "人在香港也可以：視像睇樓、相片分析、跟進律師與按揭進度，直到你拿到鎖匙。"),
    ]
    diff_html = "\n".join(f"""          <article class="diff reveal"><h3>{h}</h3><p>{p}</p></article>""" for h, p in diffs)

    svcs = [
        ("buy.html", "house-detached.webp", "Buying", "英國買樓", "一手樓花或二手樓，由搜盤、睇樓、議價到成交收樓，全程跟進。"),
        ("rent.html", "rent.webp", "Renting", "英國租屋", "未到埗先找好落腳點：搜盤、代睇、Reference check 及簽約。"),
        ("management.html", "manage.webp", "Lettings", "物業管理", "姊妹公司 JHPM 代業主放租、收租、維修及年度安全證書。"),
        ("renovation.html", "reno-kitchen.webp", "Renovation", "英國裝修", "JoyHome Builder 處理廚房、浴室、全屋翻新及擴建。"),
    ]
    svc_html = "\n".join(f"""          <a class="svc reveal" href="{h}">
            <div class="svc-img"><img src="assets/img/{img}" alt="" loading="lazy" width="800" height="600"></div>
            <div class="svc-body"><span class="svc-kicker">{k}</span><h3>{t}</h3><p>{p}</p><span class="link-arrow">了解更多</span></div>
          </a>""" for h, img, k, t, p in svcs)

    types_html = "\n".join(f"""          <article class="type reveal">
            <div class="type-img"><img src="assets/img/{img}.webp" alt="{zh}（{en}）外觀" loading="lazy" width="800" height="600"><div class="type-meter">{''.join(f'<span>{t}</span>' for t in tags)}</div></div>
            <div class="type-body"><h3>{zh}</h3><span class="type-en">{en}</span><p>{p}</p></div>
          </article>""" for img, zh, en, tags, p in TYPES)

    partners = [("p-getground", "GetGround"), ("p-mkblinds", "MK Blinds"), ("p-giraffe", "Giraffe Square"),
                ("p-liangchapu", "良茶坊"), ("p-seelight", "SEE light")]
    partner_html = "".join(f'<li><img src="assets/img/{f}.webp" alt="{n}" loading="lazy"></li>' for f, n in partners)

    faqs = [
        ("英國地產代理那麼多，我應該如何選擇？",
         "先選定幾個心儀的城市，因為每間代理只服務特定地區。無論租或買，整個流程都涉及法律和稅務，最重要是選擇在英國正式註冊、有良好信譽、熟悉當地社區的代理或顧問。英語不太流利或未去過英國的話，找能說廣東話的顧問會溝通得更清楚。"),
        ("可以像香港一樣，打電話就隨時約睇樓嗎？",
         "不可以。英國是業主主導的市場，一般只能約指定日子和時段睇樓，有時更會限時開放。業主亦會挑選買家，不一定價高者得。所以由熟悉流程的顧問替你跟進，才不會錯過時機和重要資訊。"),
        ("人在香港，怎樣避免「隔山買牛」中伏？",
         "網上相片往往比實際好看。交易前要核實代理身份、看清樓盤資料和條款，最好由熟悉該區的顧問親身睇樓，了解社區配套、校網、交通和治安。我們會以視像及相片分析，把優點和要留意的地方一併告訴你。"),
        ("聽說英國業主回覆很慢，常常錯過機會？",
         "英國的節奏比香港慢，需要多一點耐性。但好盤往往同時有幾位買家出價，代理必須緊貼市場、熟悉流程，才能在對的時間替你出價，避免錯過筍盤。"),
        ("為子女升學移居，應該先租後買，還是直接買？",
         "沒有絕對答案，視乎每個家庭的背景、預算和計劃。想找學校，就先鎖定心儀的校網，再搜尋附近的好盤。如果完全未去過英國，我們一般建議先租後買，住一段時間、熟悉生活後再決定。"),
    ]

    body = f"""    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">英國物業顧問 · 自 2015 年</p>
          <h1>在英國買樓租屋<br>有人在當地<br><em>替你睇清楚</em></h1>
          <p class="lead">JoyHome 是扎根英國多年、正式註冊的物業顧問，不是剛到埗的新移民。由搜盤、睇樓、議價到收樓，我們以廣東話全程跟進，香港及海外客戶都適用。</p>
          <div class="btn-row">
            <a class="btn btn-primary" href="contact.html">預約諮詢</a>
            <a class="btn btn-ghost" href="services.html">查看服務收費</a>
          </div>
          <ul class="trust">{trust}</ul>
        </div>
        <div class="hero-media">
          <div class="hero-photo"><img src="assets/img/hero.webp" alt="英國傳統紅磚維多利亞式排屋街景" width="1024" height="619" fetchpriority="high"></div>
          <div class="badge-years" aria-hidden="true"><b>10+</b><span>年經驗</span></div>
          <aside class="report-card" aria-label="睇樓分析示例">
            <div class="rc-top"><span class="rc-label">睇樓分析</span><span class="rc-sample">示例</span></div>
            <strong>MK5 · 三房半獨立屋</strong>
            <ul>
              <li class="pro">{icon('check')}Outstanding 小學步行 8 分鐘</li>
              <li class="pro">{icon('check')}Freehold，有私家車位</li>
              <li class="con">{icon('alert')}後園外牆有滲水痕跡，建議 Survey</li>
            </ul>
          </aside>
        </div>
      </div>
    </section>

    <div class="areas">
      <div class="wrap areas-inner">
        <span class="areas-label">服務地區</span>
        <ul class="areas-list">{areas}</ul>
      </div>
    </div>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">我們的不同之處</p>
          <h2>不只是幫你找樓<br>而是站在你這一邊</h2>
          <p class="lead">英國的地產代理代表的是賣家。JoyHome 代表的是你：一個在英國生活多年、熟悉社區的顧問。</p>
        </div>
        <div class="diff-grid">
{diff_html}
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap split">
        <div class="split-media reveal"><img src="assets/img/house-semi.webp" alt="英國新式半獨立屋" loading="lazy" width="800" height="600"></div>
        <div>
          <p class="eyebrow">關於 JoyHome</p>
          <h2>你的一站式英國房地產顧問</h2>
          <p>移居前後要處理的事情繁多：既要照顧家人需要，又要配合預算，還要與時間表賽跑。單靠網上搜尋，資訊很多，卻沒有人替你判斷。</p>
          <p>我們的團隊曾在英國不同城鎮居住、讀書和工作，熟悉各區的生活配套。多年來與當地發展商、服務供應商及地產代理保持緊密聯繫，並對接有信譽的律師、按揭及稅務夥伴。</p>
          <div class="facts">
            <div><b>2015</b><span>年成立</span></div>
            <div><b>11</b><span>個服務地區</span></div>
            <div><b>粵 / 英</b><span>雙語溝通</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">服務範圍</p>
          <h2>由落腳、置業到打理物業</h2>
        </div>
        <div class="svc-grid">
{svc_html}
        </div>
      </div>
    </section>

    <section class="section bg-navy">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">服務流程</p>
          <h2>三步 找到理想的安樂窩</h2>
        </div>
        <ol class="steps">
          <li class="reveal"><h3>搜尋及諮詢</h3><p class="step-sub">了解心儀地區、位置及物業種類</p><p>先聽你的需要：家庭成員、校網、通勤、預算和時間表，再為你篩選合適的地區和樓盤。</p></li>
          <li class="reveal"><h3>預約睇盤及分析</h3><p class="step-sub">縮窄範圍，鎖定目標物業</p><p>聯絡代理安排睇樓，提供視像及相片，並就每個單位寫下正反分析，讓你在香港也能作決定。</p></li>
          <li class="reveal"><h3>談判及跟進成交</h3><p class="step-sub">制定策略，成功入住</p><p>代你出價議價，協調測量師、按揭經紀及律師，緊貼整個買賣或租賃流程，直到收樓。</p></li>
        </ol>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap">
        <div class="head center">
          <p class="eyebrow">收費清楚</p>
          <h2>開始前就知道要付多少</h2>
          <p class="lead" style="margin:0 auto">所有收費另加 VAT。睇樓、代辦等其他服務請參閱完整收費表。</p>
        </div>
        <div class="price-strip">
          <div class="price reveal"><span class="price-label">諮詢註冊費</span><div class="price-amt">£100<small>+ VAT</small></div><p class="price-note">買樓或租樓諮詢，提供英國物業及生活資訊，推薦合適樓盤。</p></div>
          <div class="price reveal"><span class="price-label">成功租樓</span><div class="price-amt">£880<small>+ VAT</small></div><p class="price-note">Offer accepted 時先付 £180。Hertfordshire 以外地區 £880 起。</p></div>
          <div class="price is-feature reveal"><span class="price-label">成功買樓</span><div class="price-amt"><span class="from">由</span>£1,880<small>+ VAT</small></div><p class="price-note">海外客戶 £2,880 起。買價協定時先付 £880，餘額成交後才收。</p></div>
        </div>
        <p style="text-align:center;margin-top:28px"><a class="link-arrow" href="services.html">查看完整服務及收費</a></p>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">英國房地產知多少</p>
          <h2>六種常見的英國房屋</h2>
          <p class="lead">英國人重視家庭生活和居住空間。先認識不同房屋類型的特點，才知道哪一種最適合你的家庭和預算。</p>
        </div>
        <div class="types">
{types_html}
        </div>
      </div>
    </section>

{faq_section("關於英國物業顧問服務", "第一次在英國租樓或買樓，以下是客人最常問的問題。", faqs, " bg-cream")}

    <section class="section tight">
      <div class="wrap">
        <div class="head center">
          <p class="eyebrow">合作伙伴及認證</p>
          <h2>守法正規 客戶款項受保障</h2>
        </div>
        <div class="accred" style="margin-bottom:48px">
          <a href="https://www.joyhomeuk.com/wp-content/uploads/2020/07/UKALA.pdf" target="_blank" rel="noopener"><img src="assets/img/ukala.webp" alt="UKALA" loading="lazy"><div><b>UKALA 會員</b><span>UK Association of Letting Agents</span></div></a>
          <a href="https://www.joyhomeuk.com/wp-content/uploads/2020/07/CMP.pdf" target="_blank" rel="noopener"><span class="ci" style="width:44px;height:44px;border-radius:12px;background:var(--gold-soft);color:var(--navy);display:grid;place-items:center">{icon('shield')}</span><div><b>客戶款項保障</b><span>Client Money Protection</span></div></a>
          <a href="https://www.theprs.co.uk/" target="_blank" rel="noopener"><img src="assets/img/prs.webp" alt="Property Redress Scheme" loading="lazy"><div><b>{PRS_NO}</b><span>Property Redress Scheme</span></div></a>
        </div>
        <ul class="logos">{partner_html}</ul>
      </div>
    </section>

{cta_band()}"""
    page("index.html",
         "JoyHome UK · 英國物業顧問｜英國買樓、租屋、物業管理",
         "JoyHome UK 自 2015 年起為香港及海外客戶提供英國買樓、租屋、物業管理及裝修服務。正式註冊，PRS029811，UKALA 會員。",
         body, active="", preload="assets/img/hero.webp")


def build_services():
    extras = ["代收物業 Inspection", "到埗前代購物資及必需品", "代購及組裝傢俬", "家居清潔", "機場接送",
              "代收鎖匙 Key collection", "Check-in 及 Inventory check", "代收包裹 / 等候送貨"]
    body = f"""{page_hero("服務及收費", "服務及收費", "收費透明<br>成功才收大部分費用", "所有價錢以英鎊計算，另加 VAT。買樓及租樓服務大部分費用在成功後才收取；測量師、按揭經紀及律師費用由客人自行支付。")}

    <div class="subnav"><div class="wrap"><ul>
      <li><a href="#consult">諮詢</a></li><li><a href="#rent">租樓</a></li><li><a href="#buy">買樓</a></li><li><a href="#viewing">代睇樓</a></li><li><a href="#extras">外加代辦</a></li>
    </ul></div></div>

    <section class="section">
      <div class="wrap">
        <article class="fee-card reveal" id="consult">
          <div>
            <span class="tag">第一步</span>
            <h2>買樓 / 租樓諮詢</h2>
            <p class="lead">先登記成為會員，顧問會了解你的需要並開始搜盤。代睇樓服務亦須先註冊。</p>
            {checklist(["提供英國物業購買及生活資訊", "專業搜尋及推薦合適樓盤"])}
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>註冊費</th><td>£100<small>+ VAT</small></td></tr>
            </tbody></table>
          </div>
        </article>

        <article class="fee-card reveal" id="rent">
          <div>
            <span class="tag">英國租樓</span>
            <h2>成功租樓</h2>
            <p class="lead">由搜盤、代睇、出 offer 到簽約入住，一個定額收費。</p>
            <a class="link-arrow" href="rent.html">了解租樓流程</a>
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>Hertfordshire 及鄰近地區</th><td>£880<small>+ VAT</small></td></tr>
              <tr><th>Hertfordshire 以外地區</th><td>£880 起<small>+ VAT</small></td></tr>
            </tbody></table>
            <p class="fee-foot">Offer accepted 時先付 £180，餘額於成功租樓後收取。</p>
          </div>
        </article>

        <article class="fee-card reveal" id="buy">
          <div>
            <span class="tag">英國買樓</span>
            <h2>成功買樓</h2>
            {checklist(["每個單位深入的正反專業分析", "協助出價、議價及成交", "推薦測量師、按揭經紀及律師", "安排 Home Buyer Survey 並分析報告", "與按揭經紀及律師溝通，處理文件", "收取物業"])}
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>本地客戶</th><td>£1,880<small>+ VAT</small></td></tr>
              <tr><th>海外客戶 · 成交價 £600K 以下</th><td>£2,880<small>+ VAT</small></td></tr>
              <tr><th>海外客戶 · 成交價 £600K 或以上</th><td>£3,880<small>+ VAT</small></td></tr>
              <tr><th>議價成功獎金</th><td>10%<small>成功議價差價</small></td></tr>
            </tbody></table>
            <p class="fee-foot">買價協定時先付 £880，餘額在物業成功交易時才收取。測量師、按揭經紀及律師費用由客人自行負責。</p>
          </div>
        </article>

        <article class="fee-card reveal" id="viewing">
          <div>
            <span class="tag">人不在英國？</span>
            <h2>代客睇樓</h2>
            <p class="lead">買樓或租樓都適用。我們聯絡地產代理安排睇樓，並以視像及相片為你分析。</p>
            <p class="note">必須先註冊成為會員才能使用此服務。</p>
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>Milton Keynes、Luton</th><td>£60<small>每個單位 + VAT</small></td></tr>
              <tr><th>North London、Bedfordshire、Buckinghamshire、Hertfordshire 一帶</th><td>£80 起<small>每個單位 + VAT</small></td></tr>
              <tr><th>其他地區</th><td>另議<small>來回每英里 +£1</small></td></tr>
            </tbody></table>
          </div>
        </article>

        <article class="fee-card reveal" id="extras">
          <div>
            <span class="tag">到埗前後</span>
            <h2>外加代辦服務</h2>
            <p class="lead">未到英國，也可以先把家準備好。</p>
            <table class="fee-table"><tbody><tr><th>每項服務</th><td>£30 起<small>+ VAT</small></td></tr></tbody></table>
          </div>
          <div>
            <ul class="chips">{''.join(f'<li>{e}</li>' for e in extras)}</ul>
            <p class="note">詳細價錢視乎地區及工作量，歡迎向我們查詢。</p>
          </div>
        </article>
      </div>
    </section>

{cta_band("不確定需要哪一項服務？", "WhatsApp 我們你的情況，顧問會建議最合適、最省錢的組合。")}"""
    page("services.html", "服務及收費 · JoyHome UK", "JoyHome UK 英國買樓、租樓、代睇樓及代辦服務收費。註冊費 £100，成功租樓 £880，成功買樓由 £1,880 起（另加 VAT）。", body)


CITIES = [
    ("city-london", "倫敦", "London", "首都區房價全國最高，北倫敦校網及交通配套成熟。"),
    ("city-stalbans", "聖奧爾本斯", "St Albans", "歷史古城，直達倫敦約 20 分鐘，名校林立。"),
    ("city-birmingham", "伯明翰", "Birmingham", "英國第二大城市，樓價相宜，租金回報穩定。"),
    ("city-nottingham", "諾丁漢", "Nottingham", "大學城，學生及專業人士租務需求強勁。"),
    ("city-leeds", "列斯", "Leeds", "北部金融中心，新式公寓選擇多。"),
    ("city-warrington", "沃靈頓", "Warrington", "位處曼徹斯特與利物浦之間，性價比高。"),
]


def build_buy():
    cities = "\n".join(f"""          <a class="city reveal" href="contact.html">
            <img src="assets/img/{img}.webp" alt="{zh}（{en}）" loading="lazy" width="900" height="675">
            <div class="city-body"><span>{en}</span><b>{zh}</b><p>{p}</p></div>
          </a>""" for img, zh, en, p in CITIES)
    mk_list = [("MK8 Pembroke Lane", "三房獨立屋", "£500,000"), ("MK5 Shenley Brook End", "三房排屋", "£390,000"),
               ("MK4 Tattenhoe Park", "四房半獨立屋", "£460,000"), ("MK10 Oakgrove", "五房獨立屋", "£660,000"),
               ("MK10 Middleton", "兩房排屋", "£300,000"), ("MK5 Loughton", "四房獨立屋", "£700,000")]
    mk_rows = "".join(f"<tr><td>{a}</td><td>{t}</td><td class=\"num\">{p}</td></tr>" for a, t, p in mk_list)

    faqs = [
        ("我持 BNO 簽證移英，買樓要付非居民附加印花稅嗎？",
         "非居民附加稅（額外 2%）是按居住日數判斷，而不是看簽證或護照：如果在交易前 12 個月內，在英國居住少於 183 日，一般須繳付。剛到埗便買樓的家庭特別要留意，部分情況可在其後申請退回。實際情況請向律師確認。"),
        ("Freehold 和 Leasehold 有甚麼分別？",
         "Freehold（永久業權）即擁有土地及其上建築物的絕對所有權。Leasehold（租賃業權）是租用土地，年期通常 99 至 999 年，每年要付地租、服務費及大廈保險。Leasehold 價錢較低，但升值空間較有限，年期越短越難轉售及承造按揭，購買前必須查清剩餘年期。"),
        ("除了印花稅，還有甚麼買樓雜費？",
         "常見包括：律師費（Legal fee）約 £1,000–2,000；驗樓（Survey）約 £600–850；Homebuyer Report 約 £400–650，舊屋建議一定要做；另外還有按揭申請費、搬運及保險等。以上只供參考，視乎律師行、地區及樓價而定。"),
        ("香港或海外有物業，在英國要交甚麼稅？",
         "成為英國稅務居民後，稅務是全球性的。出售海外物業可能要申報資本增值稅（Capital Gains Tax）；出租物業的租金收入可能要繳入息稅。我們會轉介熟悉港人情況的會計師，買樓前最好先做稅務規劃。"),
        ("Youtuber 常說 Milton Keynes 的 MK4、5、8、10 最好，是真的嗎？",
         "這幾區整體確實受歡迎，但不能一概而論，區內也有不宜居住的街道。最常見的陷阱就是只看網上相片便成交，結果貨不對辦、遲遲租不出。一定要有人親身睇樓。"),
    ]

    body = f"""{page_hero("英國買樓", "英國買樓", "英國買樓<br>流程、費用、稅務一次看清", "同一筆預算，在英國可以住得寬敞得多。但按揭、印花稅、Leasehold 等規則與香港很不同。JoyHome 由選區到收樓全程跟進，替你避開陷阱。", "assets/img/buy.webp", "英國新建獨立屋社區")}

    <div class="subnav"><div class="wrap"><ul>
      <li><a href="#areas">熱門地區</a></li><li><a href="#process">買樓流程</a></li><li><a href="#tax">印花稅</a></li><li><a href="#mk">Milton Keynes</a></li><li><a href="#faq">常見問題</a></li>
    </ul></div></div>

    <section class="section" id="areas">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">熱門地區</p>
          <h2>你想在哪裡安家？</h2>
          <p class="lead">倫敦以外，伯明翰、Milton Keynes、列斯等城市都有不少高性價比的選擇。告訴我們你的考慮，我們為你比較各區的校網、交通、治安和樓價。</p>
        </div>
        <div class="cities">
          <a class="city is-wide reveal" href="#mk">
            <img src="assets/img/city-mk.webp" srcset="assets/img/city-mk.webp 900w, assets/img/city-mk-1600.webp 1600w" sizes="(max-width: 520px) 100vw, 50vw" alt="Milton Keynes 火車站" loading="lazy" width="900" height="600">
            <div class="city-body"><span>Milton Keynes</span><b>米爾頓凱恩斯</b><p>港人熱門落腳地。直通火車到倫敦 Euston 約 35 分鐘，綠化及校網俱佳。</p></div>
          </a>
{cities}
        </div>
      </div>
    </section>

    <section class="section bg-cream" id="process">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">買樓流程</p>
          <h2>一手樓花與二手樓 步驟不一樣</h2>
        </div>
        <div class="tabs" role="tablist" aria-label="買樓類型">
          <button role="tab" id="tab-resale" aria-controls="panel-resale" aria-selected="true">二手樓</button>
          <button role="tab" id="tab-new" aria-controls="panel-new" aria-selected="false" tabindex="-1">一手樓 / 樓花</button>
        </div>
        <div class="grid-2">
          <div>
            <div role="tabpanel" id="panel-resale" aria-labelledby="tab-resale">
              <ol class="timeline">
                <li><h3>申請 Agreement in Principle</h3><p>如需按揭，先向銀行或按揭經紀取得原則上批核，證明購買能力，議價時更有說服力。</p></li>
                <li><h3>搜盤及睇樓</h3><p>人不在英國，由顧問代你睇樓，仔細拍照拍片並分析周邊環境。</p></li>
                <li><h3>出價及 Memorandum of Sale</h3><p>雙方同意價格後簽署銷售備忘錄，列明成交價及物業細節。</p></li>
                <li><h3>驗樓及按揭審批<span class="when">約 2–3 個月</span></h3><p>安排測量師檢查室內外、車庫及花園結構，有需要再與業主商討維修或議價。銀行按估值及還款能力審批貸款。</p></li>
                <li><h3>交換合約及成交</h3><p>律師草擬合約，交換合約時付約 10% 訂金；完成所有文件後付清餘款及印花稅，取鎖匙入住。</p></li>
              </ol>
            </div>
            <div role="tabpanel" id="panel-new" aria-labelledby="tab-new" hidden>
              <ol class="timeline">
                <li><h3>Reservation Agreement</h3><p>選定單位後簽署初步買賣協議並付留位費，由數百至數千英鎊不等，視乎發展商。</p></li>
                <li><h3>委託律師、交換合約</h3><p>簽訂正式買賣合約，一般付樓價約 10% 作首期訂金。</p></li>
                <li><h3>申請按揭<span class="when">交樓前約 6 個月</span></h3><p>需要按揭的話，顧問為你轉介按揭經紀，選取穩健合適的方案。</p></li>
                <li><h3>驗樓（Snagging）</h3><p>交樓前委託驗樓師到場檢查，列出需要發展商修補的細節。</p></li>
                <li><h3>完成交易、取鎖匙</h3><p>付清餘款、印花稅及相關費用，正式收樓入住。</p></li>
              </ol>
            </div>
          </div>
          <div>
            <div class="card">
              <div class="card-icon">{icon('users')}</div>
              <h3>JoyHome 在每一步做甚麼？</h3>
              {checklist(["為每個單位寫正反分析", "代你出價、議價，爭取最好條件", "推薦測量師、按揭經紀、律師", "分析 Homebuyer Report，指出要跟進的問題", "與律師及按揭經紀溝通，處理文件", "代你收取物業"])}
              <p style="margin-top:18px"><a class="link-arrow" href="services.html#buy">買樓服務收費</a></p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="tax">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">英國買樓稅務</p>
          <h2>印花稅（Stamp Duty Land Tax）</h2>
          <p class="lead">印花稅按樓價分段計算，首次置業、第二個物業及非居民的稅率各有不同。以下為英格蘭住宅物業稅率。</p>
        </div>
        <div class="grid-2">
          <div class="table-scroll">
            <table class="data-table">
              <thead><tr><th>樓價部分</th><th class="num">一般稅率</th><th class="num">額外物業</th></tr></thead>
              <tbody>
                <tr><td>£125,000 或以下</td><td class="num">0%</td><td class="num">5%</td></tr>
                <tr><td>£125,001 – £250,000</td><td class="num">2%</td><td class="num">7%</td></tr>
                <tr><td>£250,001 – £925,000</td><td class="num">5%</td><td class="num">10%</td></tr>
                <tr><td>£925,001 – £1.5M</td><td class="num">10%</td><td class="num">15%</td></tr>
                <tr><td>£1.5M 以上</td><td class="num">12%</td><td class="num">17%</td></tr>
              </tbody>
            </table>
            <p class="note">資料參考 2025 年 4 月起生效的稅率，只供參考，請以 <a href="https://www.gov.uk/stamp-duty-land-tax/residential-property-rates" target="_blank" rel="noopener">GOV.UK</a> 最新公布為準。</p>
          </div>
          <div style="display:grid;gap:16px;align-content:start">
            <div class="callout"><p><b>首次置業</b>：樓價 £300,000 以下部分免稅，£300,001–£500,000 部分 5%。樓價超過 £500,000 則按一般稅率計算。</p></div>
            <div class="callout"><p><b>非居民附加稅</b>：交易前 12 個月內在英國居住少於 183 日，各級稅率再加 2%。</p></div>
            <div class="callout"><p><b>市政稅（Council Tax）</b>：按物業所屬 Band 及地區每年繳付，由居住者負責。</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-cream" id="mk">
      <div class="wrap">
        <div class="split">
          <div>
            <p class="eyebrow">地區焦點</p>
            <h2>Milton Keynes：港人熱門落腳地</h2>
            <p>位於倫敦以北的 Buckinghamshire，人口近 30 萬，2022 年正式升格為城市。城市規劃完善，公園湖泊處處，有多間 Ofsted 評為 Outstanding 及 Good 的學校。</p>
            <p>西面的 MK4（Tattenhoe、Shenley Brook End、Emerson Valley）、MK5（Shenley Church End、Loughton）、MK8（Whitehouse）及東面的 MK10 都有優質校網；東面更貼近 M1 高速公路。三房半獨立屋最受歡迎，亦最容易出租。</p>
            <div class="facts">
              <div><b>35 分鐘</b><span>直達倫敦 Euston</span></div>
              <div><b>4–5.1%</b><span>參考租金回報</span></div>
              <div><b>£300K 起</b><span>三房半獨立屋</span></div>
            </div>
          </div>
          <div>
            <div class="table-scroll">
              <table class="data-table">
                <thead><tr><th>地區</th><th>類型</th><th class="num">參考價</th></tr></thead>
                <tbody>{mk_rows}</tbody>
              </table>
            </div>
            <p class="note">過往樓盤推介，只作價錢參考，並非現時放盤。</p>
          </div>
        </div>
      </div>
    </section>

{faq_section("有關英國買樓", "印花稅、業權、雜費，每次都有人問。", faqs)}

{cta_band("準備在英國置業？", "先約一次諮詢，我們按你的預算和家庭需要，比較幾個最合適的地區。")}"""
    page("buy.html", "英國買樓 · 流程、印花稅及熱門地區｜JoyHome UK",
         "英國買樓流程、印花稅、Freehold 與 Leasehold、Milton Keynes 等熱門地區介紹。JoyHome UK 由搜盤到收樓全程跟進。", body)


def build_rent():
    docs = [("護照 / BRP / eVisa", "身份證明"), ("Right to Rent", "證明你有權在英國租屋，例如 BNO 簽證批核"),
            ("工作證明", "部分業主不接受自僱或兼職人士"), ("銀行證明", "有業主會要求英國銀行戶口"), ("信貸報告", "Reference check 時查核")]
    doc_html = "\n".join(f"""          <div class="card reveal"><div class="card-icon">{icon('doc')}</div><h3>{a}</h3><p>{b}</p></div>""" for a, b in docs)
    faqs = [
        ("英國租樓網站那麼多，哪些比較可靠？",
         "Rightmove、Zoopla、OpenRent、SpareRoom 都是常用的租屋網站。可以先選心儀的城市和地區，比較租金，再看社區配套、校網、治安和交通。人在香港的話，JoyHome 可以替你全程跟進及分析。"),
        ("我有兩隻貓和一隻大狗，是不是很難租屋？",
         "部分業主不接受寵物，或會要求較高租金。我們明白寵物是家人，會積極替你找寵物友善的租盤。有寵物的話，建議到埗前預留 3 至 4 個月時間準備。"),
        ("租屋要準備多少錢？",
         "主要包括按金、首期租金及顧問費（如需要）。年租少於 £50,000 的話，按金上限為 5 星期租金，留屋訂金（Holding deposit）上限為 1 星期租金。另外每月要付水電煤、網絡及市政稅（Council Tax）。英格蘭租務法例於 2026 年有重大改動，預繳租金等規定與以往不同，我們會按最新法例為你解釋。"),
        ("獨立屋、排屋、公寓，哪種性價比最高？",
         "排屋較矮較舊，要留意防盜、滲水和設備老化，所以租金相對較低；新式公寓較新淨，治安和結構問題較少。最終要按地區、預算、校網和交通一併考慮。"),
    ]
    body = f"""{page_hero("英國租屋", "英國租屋", "未到埗<br>先找好落腳的家", "優質租盤放出不久便有人出價，3 至 4 星期內完成租約。建議到埗前預留 2 至 3 個月。JoyHome 替你搜盤、代睇、準備文件，跟進到簽約入住。", "assets/img/rent.webp", "倫敦街景")}

    <section class="section">
      <div class="wrap">
        <div class="grid-2" style="align-items:start;gap:clamp(32px,6vw,80px)">
          <div>
            <p class="eyebrow">租屋流程</p>
            <h2>英國租屋 比香港多幾個步驟</h2>
            <p class="lead">業主會對租客做 Reference check，確保你有能力交租。剛到埗未有穩定收入的話，要預早準備證明文件。</p>
            <p><a class="link-arrow" href="services.html#rent">租樓服務收費：成功租樓 £880 + VAT</a></p>
          </div>
          <ol class="timeline">
            <li class="reveal"><h3>搜盤及代睇</h3><p>按你的城市、校網、預算篩選租盤；人不在英國，由顧問代睇並以視像分析。</p></li>
            <li class="reveal"><h3>出價及留屋訂金</h3><p>確認租盤後付 Holding deposit（最多 1 星期租金）。</p></li>
            <li class="reveal"><h3>Reference check<span class="when">約 2–3 星期</span></h3><p>業主核實身份、Right to Rent、收入及信貸紀錄。</p></li>
            <li class="reveal"><h3>簽約、付按金</h3><p>簽署租約（Tenancy Agreement），按金存入政府認可的按金保障計劃。</p></li>
            <li class="reveal"><h3>Inventory check 及收樓</h3><p>逐項記錄屋內設備及狀況，日後退租取回按金時用得著。</p></li>
          </ol>
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Reference check</p>
          <h2>租屋需要準備的文件</h2>
        </div>
        <div class="grid-3" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">
{doc_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split reverse">
        <div class="split-media reveal"><img src="assets/img/rent-london.webp" alt="倫敦西敏寺及大笨鐘" loading="lazy" width="768" height="516"></div>
        <div>
          <p class="eyebrow">倫敦及其他地區</p>
          <h2>倫敦租屋 或者其他城市？</h2>
          <p>倫敦租金全國最高，但工作和學校選擇最多；倫敦以外的城市租金一般較相宜，空間更大。我們熟悉 North London、Hertfordshire、Milton Keynes、Luton 等地區，其他城市亦可安排。</p>
          <p>先租後買，是很多家庭的選擇：住一段時間、熟悉社區後，再決定在哪裡置業。</p>
          <a class="btn btn-primary" href="contact.html">告訴我們你的租屋需要</a>
        </div>
      </div>
    </section>

{faq_section("關於英國租屋", "寵物、預算、房屋類型，租屋前最常見的疑問。", faqs, " bg-cream")}

{cta_band("想在到埗前把家準備好？", "我們也提供到埗前代購物資、代收鎖匙、機場接送等代辦服務，£30 起。")}"""
    page("rent.html", "英國租屋 · 流程、文件及費用｜JoyHome UK",
         "英國租屋流程、Reference check 所需文件、按金及費用。JoyHome UK 替你搜盤代睇，跟進到簽約入住。", body)


def build_management():
    let_steps = [("估價", "按地點、物業狀況及市場需求，提供合理的預計租金。"),
                 ("專業相片及文案", "拍攝專業角度照片，撰寫準確吸引的物業描述。"),
                 ("刊登廣告", "於 JoyHome Facebook 專頁及主要租屋網站放盤。"),
                 ("安排睇樓", "帶有興趣的租客睇樓，篩選合適人選。"),
                 ("信貸評估", "透過認可機構為租客做信譽評估。"),
                 ("收首月租金及簽約", "收取首月租金及按金，簽署合法有效的租約。")]
    manage = ["租約開始前安排煤氣及電力安全證書，並每年更新煤氣安全證書",
              "起租前做物業狀況檢查，製作圖文報告，作為退還按金的依據",
              "每月收取租金", "處理租客問題及維修要求，並與業主溝通",
              "經業主同意後，安排可靠的工程師維修", "以相片及簽名記錄所有發出的鎖匙",
              "租約期間保管鎖匙及所有物業文件", "定期檢查物業（一般每 6 個月），及早發現問題",
              "按業主要求發出各項法定通知，例如加租、續約或終止租約"]
    faqs = [
        ("委託 JHPM 需要甚麼手續？", "我們會發給你一份物業管理合約，列明物業地址、描述、預估租金，以及各項收費和服務條款。你填寫個人資料及收租銀行資料，簽署交回後，我們便可開始服務。"),
        ("JHPM 會定期檢查物業嗎？", "會。我們通常每 6 個月檢查一次物業，並把結果匯報給業主。"),
        ("我住在海外，可以委託你們嗎？", "可以。JHPM 自成立以來已協助很多海外業主。我們已登記 Non-Resident Landlord Scheme，方便海外業主登記成為非居民業主。"),
    ]
    body = f"""{page_hero("物業管理", "英國物業管理 · JHPM", "人在海外<br>英國物業照樣打理妥當", "JoyHome Property Management（JHPM）是我們的姊妹公司，2021 年 1 月成立，為 UKALA 及 PRS 註冊成員。我們替在英國投資的業主放租、收租及管理物業。", "assets/img/manage.webp", "英國半獨立屋外觀")}

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">服務一</p>
          <h2>快速找到優質租客</h2>
        </div>
        <div class="grid-3">
{chr(10).join(f'          <div class="card reveal"><h3>{i + 1:02d}　{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(let_steps))}
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap split">
        <div>
          <p class="eyebrow">服務二</p>
          <h2>一站式租務管理</h2>
          <p class="lead">由起租前的安全證書，到租約期間的維修和法定通知，全部替你處理。</p>
        </div>
        <div>{checklist(manage)}</div>
      </div>
    </section>

    <section class="section bg-navy">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">為甚麼選擇 JHPM</p>
          <h2>業主可以放心交託的三個原因</h2>
        </div>
        <div class="grid-3">
          <div class="card reveal"><div class="card-icon">{icon('shield')}</div><h3>可靠</h3><p>UKALA 及 PRS 註冊成員，操作及財務受 UKALA 長期監管。設獨立客戶戶口（Client Account）收付租金，並通過客戶款項保障（CMP）認證。</p></div>
          <div class="card reveal"><div class="card-icon">{icon('eye')}</div><h3>透明</h3><p>由放盤到成功簽約，全程向業主匯報進度；物業有維修問題，第一時間通知並跟進。</p></div>
          <div class="card reveal"><div class="card-icon">{icon('chat')}</div><h3>溝通快</h3><p>WhatsApp、電郵、電話都找得到人，中文或英文溝通都可以，不會出現找不到管理公司的情況。</p></div>
        </div>
      </div>
    </section>

{faq_section("關於物業管理", "業主委託前最常問的問題。", faqs)}

{cta_band("有物業想放租？", "告訴我們物業地址和類型，我們先為你估算租金及管理費用。")}"""
    page("management.html", "英國物業管理 · JHPM｜JoyHome UK",
         "JoyHome Property Management：UKALA 及 PRS 註冊成員，為海外業主放租、收租、維修及處理安全證書，設客戶款項保障。", body)


def build_renovation():
    trades = [
        ("木工", ["地板鋪設：Laminate、LVT、SPC", "特色牆、大門", "雙層玻璃 UPVC 窗", "地腳線 / 天花線", "入牆傢俬、樓梯", "閣樓及車庫 Conversion", "溫室擴建"]),
        ("水喉及暖氣", ["暖板安裝", "熱水爐（Boiler）安裝", "淋浴間安裝", "排水渠安裝", "衛浴設備安裝"]),
        ("泥水", ["螺柱牆 / 石膏牆重建", "拆牆", "開放式廚房改造", "恢復時代特色天花線"]),
        ("電工", ["遷移主電箱", "電暖板、燈具、吊燈", "全屋重新佈線", "智能家居系統", "煙霧及保安系統"]),
        ("室內裝飾", ["牆壁及天花油漆", "貼牆紙", "特色牆油漆"]),
        ("瓦工", ["廚房及浴室瓷磚", "地台及牆身瓷磚"]),
    ]
    trade_html = "\n".join(f"""          <div class="card reveal"><h3>{t}</h3><ul>{''.join(f'<li>{i}</li>' for i in items)}</ul></div>""" for t, items in trades)
    body = f"""{page_hero("英國裝修", "JoyHome Builder", "把英國的屋<br>裝修成你的家", "JoyHome Builder 是 JoyHome Service Ltd 旗下的裝修團隊，提供浴室、廚房、全屋翻新、擴建及溫室工程。本地英國師傅加上香港背景的項目經理，溝通無障礙。", "assets/img/reno-kitchen.webp", "裝修完成的開放式廚房")}

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">裝修示例</p>
          <h2>真實完成的工程</h2>
        </div>
        <div class="gallery">
          <figure><img src="assets/img/reno-kitchen-1800.webp" alt="全屋裝修後的廚房" loading="lazy"><figcaption>全屋裝修</figcaption></figure>
          <figure><img src="assets/img/reno-bath.webp" alt="翻新後的浴室" loading="lazy"><figcaption>浴室</figcaption></figure>
          <figure><img src="assets/img/reno-conservatory.webp" alt="溫室及新鋪地板" loading="lazy"><figcaption>溫室 / 地板</figcaption></figure>
          <figure><img src="assets/img/reno-bath2.webp" alt="浴室洗手盆及櫃" loading="lazy"><figcaption>浴室</figcaption></figure>
          <figure><img src="assets/img/reno-before.webp" alt="拆牆工程進行中" loading="lazy"><figcaption>拆牆工程</figcaption></figure>
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">為甚麼選擇 JoyHome Builder</p>
          <h2>品質、預算、溝通 一併照顧</h2>
        </div>
        <div class="grid-3">
          <div class="card reveal"><div class="card-icon">{icon('home')}</div><h3>質量</h3><p>以最高標準施工，提升物業的舒適度和價值。</p></div>
          <div class="card reveal"><div class="card-icon">{icon('users')}</div><h3>一對一項目經理</h3><p>由計劃到完工都有專人跟進，替你控制裝修費用。</p></div>
          <div class="card reveal"><div class="card-icon">{icon('pound')}</div><h3>材料採購</h3><p>材料合作夥伴提供合理實惠的價錢，有效降低成本。</p></div>
          <div class="card reveal"><div class="card-icon">{icon('chat')}</div><h3>多元化團隊</h3><p>本地英國及香港背景的團隊，明白你的生活習慣和要求。</p></div>
          <div class="card reveal"><div class="card-icon">{icon('tool')}</div><h3>全面</h3><p>由全屋裝修到花園，涵蓋你想要的所有風格。</p></div>
          <div class="card reveal"><div class="card-icon">{icon('trend')}</div><h3>提升價值</h3><p>廚房、浴室及擴建工程，是提升轉售及租金價值最有效的方法。</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">服務範圍</p>
          <h2>各類工種 一個團隊完成</h2>
          <p class="lead">浴室由更換潔具到全濕區（Wet room）、廚房由小空間到開放式設計、房屋擴建由加建房間到溫室，都可以處理。</p>
        </div>
        <div class="trades">
{trade_html}
        </div>
      </div>
    </section>

{cta_band("有裝修計劃？", "傳幾張現場相片和你的想法給我們，先替你估算範圍和預算。")}"""
    page("renovation.html", "英國裝修 · JoyHome Builder｜JoyHome UK",
         "JoyHome Builder 提供英國浴室、廚房、全屋翻新、擴建及溫室工程，一對一項目經理，香港背景團隊。", body)


def build_contact():
    services = ["買樓", "租屋", "代睇樓", "物業管理", "裝修", "其他"]
    picks = "".join(f'<label><input type="checkbox" name="service" value="{s}"><span>{s}</span></label>' for s in services)
    body = f"""{page_hero("聯絡我們", "聯絡我們", "告訴我們你的計劃", "WhatsApp 最快。也可以填寫下面的表格，系統會把你的資料整理好，直接以 WhatsApp 或電郵傳送給我們。", ctas=False)}

    <section class="section" style="padding-top:clamp(40px,5vw,64px)">
      <div class="wrap contact-grid">
        <div>
          <ul class="contact-list">
            <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener"><span class="ci wa">{icon('wa')}</span><span><small>WhatsApp（最快回覆）</small><b>{PHONE}</b></span></a></li>
            <li><a href="tel:{TEL}"><span class="ci">{icon('phone')}</span><span><small>電話</small><b>{PHONE}</b></span></a></li>
            <li><a href="mailto:{EMAIL}"><span class="ci">{icon('mail')}</span><span><small>電郵</small><b>{EMAIL}</b></span></a></li>
            <li><a href="{FB}" target="_blank" rel="noopener"><span class="ci">{icon('fb')}</span><span><small>Facebook</small><b>JoyhomeUK</b></span></a></li>
          </ul>
          <h3>辦公時間</h3>
          <table class="hours"><tbody>
            <tr><td>星期一至五</td><td>9:00 – 17:00（英國時間）</td></tr>
            <tr><td>星期六、日及公眾假期</td><td>休息</td></tr>
          </tbody></table>
          <p class="note">香港夏令時間比英國快 7 小時，冬令時間快 8 小時。</p>
        </div>

        <form class="form" action="mailto:{EMAIL}" method="post" enctype="text/plain" data-enquiry data-wa="{WA}" data-mail="{EMAIL}">
          <h2 style="font-size:26px">查詢表</h2>
          <fieldset class="field">
            <legend>我想查詢</legend>
            <div class="pick">{picks}</div>
          </fieldset>
          <div class="field-row">
            <div class="field"><label for="f-area">地區<span class="opt">選填</span></label><input id="f-area" name="area" placeholder="例如 Milton Keynes"></div>
            <div class="field"><label for="f-when">預計時間<span class="opt">選填</span></label>
              <select id="f-when" name="when"><option value="">請選擇</option><option>一個月內</option><option>1–3 個月</option><option>3–6 個月</option><option>6 個月以上</option><option>未決定</option></select></div>
          </div>
          <div class="field"><label for="f-budget">預算<span class="opt">選填</span></label><input id="f-budget" name="budget" placeholder="例如 月租 £1,500 / 樓價 £400K"></div>
          <div class="field-row">
            <div class="field"><label for="f-name">名字</label><input id="f-name" name="name" required autocomplete="name"></div>
            <div class="field"><label for="f-reply">電郵或電話</label><input id="f-reply" name="reply" required autocomplete="email" placeholder="方便我們回覆你"></div>
          </div>
          <div class="field"><label for="f-msg">查詢事項</label><textarea id="f-msg" name="message" placeholder="家庭成員、校網、寵物、到埗日期等，越詳細越好"></textarea></div>
          <div class="form-actions">
            <button class="btn btn-wa" type="submit" value="wa">{icon('wa')}用 WhatsApp 傳送</button>
            <button class="btn btn-ghost" type="submit" value="email">{icon('mail')}用電郵傳送</button>
          </div>
          <p class="form-hint">按下後會開啟 WhatsApp 或電郵程式，訊息已預先填好，確認後再傳送即可。</p>
        </form>
      </div>
    </section>"""
    page("contact.html", "聯絡我們 · JoyHome UK", "WhatsApp、電話或電郵聯絡 JoyHome UK。辦公時間星期一至五 9:00–17:00（英國時間）。", body)


if __name__ == "__main__":
    build_index()
    build_services()
    build_buy()
    build_rent()
    build_management()
    build_renovation()
    build_contact()
    import en  # noqa: E402  English pages live in _build/en.py
    en.build_all()
