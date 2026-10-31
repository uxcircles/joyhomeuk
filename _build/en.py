"""English pages. Shares header, footer and helpers with build.py; output goes to /en/."""
import build as b
from build import (icon, page, page_hero, faq_section, cta_band, checklist,
                   AREAS, PRS_NO, WA, TEL, PHONE, EMAIL, FB)

TYPES_EN = [
    ("house-detached", "Detached house", ["Most privacy", "Highest budget"],
     "Stands on its own with no shared walls. Plenty of space, usually front and back gardens and a driveway. The largest are called mansions."),
    ("house-semi", "Semi-detached house", ["Family favourite"],
     "Shares one wall with the house next door. Private, usually with gardens and parking, second only to detached on price and the easiest to let."),
    ("house-terrace", "Terraced house", ["Good value"],
     "Part of a row of joined houses. Less space than a detached home and closer neighbours. In older terraces, check for damp and ageing structure."),
    ("house-bungalow", "Bungalow", ["Step-free living"],
     "A single-storey home with no stairs. Suits families living with grandparents, and plots are often generous."),
    ("house-maisonette", "Maisonette", ["Own front door"],
     "Usually a two-storey building split into an upper and a lower home, each with its own entrance. Priced between a flat and a terrace."),
    ("house-flat", "Apartment / flat / studio", ["Lowest entry price"],
     "Like a Hong Kong apartment. New blocks have lifts, a lobby and amenities; older ones may have a few floors and no lift. Mostly leasehold, so check ground rent and service charges."),
]

CITIES_EN = [
    ("city-london", "London", "The highest prices in the UK. North London has established schools and transport."),
    ("city-stalbans", "St Albans", "Historic cathedral city about 20 minutes from London, with strong schools."),
    ("city-birmingham", "Birmingham", "The UK's second city. Affordable prices and steady rental yields."),
    ("city-nottingham", "Nottingham", "University city with strong demand from students and professionals."),
    ("city-leeds", "Leeds", "Financial hub of the North with plenty of new-build flats."),
    ("city-warrington", "Warrington", "Between Manchester and Liverpool, with good value for money."),
]


def build_index():
    trust = "".join(f"<li>{icon('shield')}{t}</li>" for t in
                    [f"PRS registered {PRS_NO}", "UKALA member", "Client Money Protection"])
    areas = "".join(f"<li>{a}</li>" for a in AREAS)
    diffs = [
        ("Homes that actually fit", "We start with your family, schools, commute and budget before we search, rather than pushing whatever an agent most wants to sell."),
        ("Better long-term value", "Every property comes with pros and cons in writing: the street, lease length, condition, resale and rental potential."),
        ("Lower costs", "We make offers and negotiate for you and introduce trusted surveyors, brokers and solicitors. Our negotiation fee is 10% of what we save you."),
        ("Less stress", "You can be in Hong Kong: video viewings, photo reports and updates on your solicitor and mortgage until you have the keys."),
    ]
    diff_html = "\n".join(f'          <article class="diff reveal"><h3>{h}</h3><p>{p}</p></article>' for h, p in diffs)
    svcs = [
        ("buy.html", "house-detached.webp", "Buying", "Buying in the UK", "New builds or resale homes, from search and viewings to negotiation and completion."),
        ("rent.html", "rent.webp", "Renting", "Renting in the UK", "Line up a home before you land: search, viewings, referencing and tenancy."),
        ("management.html", "manage.webp", "Lettings", "Property management", "Our sister company JHPM lets, collects rent, handles repairs and safety certificates."),
        ("renovation.html", "reno-kitchen.webp", "Renovation", "Renovation", "JoyHome Builder handles kitchens, bathrooms, full refurbishments and extensions."),
    ]
    svc_html = "\n".join(f"""          <a class="svc reveal" href="{h}">
            <div class="svc-img"><img src="assets/img/{img}" alt="" loading="lazy" width="800" height="600"></div>
            <div class="svc-body"><span class="svc-kicker">{k}</span><h3>{t}</h3><p>{p}</p><span class="link-arrow">Learn more</span></div>
          </a>""" for h, img, k, t, p in svcs)
    types_html = "\n".join(f"""          <article class="type reveal">
            <div class="type-img"><img src="assets/img/{img}.webp" alt="{name}" loading="lazy" width="800" height="600"><div class="type-meter">{''.join(f'<span>{t}</span>' for t in tags)}</div></div>
            <div class="type-body"><h3>{name}</h3><p>{p}</p></div>
          </article>""" for img, name, tags, p in TYPES_EN)
    partners = [("p-getground", "GetGround"), ("p-mkblinds", "MK Blinds"), ("p-giraffe", "Giraffe Square"),
                ("p-liangchapu", "Liang Cha Pu"), ("p-seelight", "SEE light")]
    partner_html = "".join(f'<li><img src="assets/img/{f}.webp" alt="{n}" loading="lazy"></li>' for f, n in partners)
    faqs = [
        ("There are so many UK estate agents. How do I choose?",
         "Start by shortlisting a few towns, because each agent only covers certain areas. Renting or buying involves legal and tax steps, so choose a UK-registered agent or consultant with a good reputation who knows the local community. If English is not your first language, a Cantonese-speaking consultant makes everything clearer."),
        ("Can I just call and view a property any time, like in Hong Kong?",
         "No. The UK market is led by sellers and landlords. Viewings are booked for set days and slots, sometimes only for a short window, and sellers may choose a buyer on more than price. Someone who knows the process makes sure you don't miss your chance."),
        ("I'm in Hong Kong. How do I avoid buying sight unseen?",
         "Online photos often flatter. Before committing, check who the agent is, read the details and terms carefully, and have someone who knows the area visit in person to judge the neighbourhood, schools, transport and safety. We report back on video and in writing, good points and concerns alike."),
        ("I hear UK sellers reply slowly and good homes get away.",
         "The UK moves more slowly than Hong Kong, so patience helps. But good homes often get several offers at once, so your agent has to follow the market closely and know the process to make your offer at the right moment."),
        ("We're moving for our children's education. Should we rent first or buy?",
         "There is no single answer; it depends on your background, budget and plans. For schools, pick the catchment first and then search nearby. If you have never lived in the UK, we usually suggest renting first and buying once you know the area."),
    ]
    body = f"""    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">UK property consultants · since 2015</p>
          <h1>Your UK home<br><em>checked in person</em><br>before you commit</h1>
          <p class="lead">JoyHome is a registered UK property consultancy that has been here for years. We handle the search, viewings, negotiation and handover in English or Cantonese, for clients in the UK, Hong Kong and overseas.</p>
          <div class="btn-row">
            <a class="btn btn-primary" href="contact.html">Book a consultation</a>
            <a class="btn btn-ghost" href="services.html">See our fees</a>
          </div>
          <ul class="trust">{trust}</ul>
        </div>
        <div class="hero-media">
          <div class="hero-photo"><img src="assets/img/hero.webp" alt="A street of red-brick Victorian terraced houses" width="1024" height="619" fetchpriority="high"></div>
          <div class="badge-years" aria-hidden="true"><b>10+</b><span>years</span></div>
          <aside class="report-card" aria-label="Sample viewing report">
            <div class="rc-top"><span class="rc-label">Viewing report</span><span class="rc-sample">Sample</span></div>
            <strong>MK5 · 3-bed semi</strong>
            <ul>
              <li class="pro">{icon('check')}8-minute walk to an Outstanding primary</li>
              <li class="pro">{icon('check')}Freehold with off-street parking</li>
              <li class="con">{icon('alert')}Damp marks on the rear wall: get a survey</li>
            </ul>
          </aside>
        </div>
      </div>
    </section>

    <div class="areas">
      <div class="wrap areas-inner">
        <span class="areas-label">AREAS WE COVER</span>
        <ul class="areas-list">{areas}</ul>
      </div>
    </div>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">What makes us different</p>
          <h2>Not just finding a home<br>but being on your side</h2>
          <p class="lead">UK estate agents work for the seller. JoyHome works for you: a consultant who has lived here for years and knows the neighbourhoods.</p>
        </div>
        <div class="diff-grid">
{diff_html}
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap split">
        <div class="split-media reveal"><img src="assets/img/house-semi.webp" alt="A new-build semi-detached house" loading="lazy" width="800" height="600"></div>
        <div>
          <p class="eyebrow">About JoyHome</p>
          <h2>Your one-stop UK property consultant</h2>
          <p>Moving country means juggling a lot: your family's needs, your budget and a tight timeline. Searching online gives you plenty of listings but nobody to tell you which ones are right.</p>
          <p>Our team has lived, studied and worked in towns across the UK. We have long-standing links with developers, service providers and agents, and work with trusted solicitors, mortgage brokers and tax advisers.</p>
          <div class="facts">
            <div><b>2015</b><span>founded</span></div>
            <div><b>11</b><span>areas covered</span></div>
            <div><b>EN / 粵</b><span>bilingual team</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Services</p>
          <h2>From first rental to buying and letting</h2>
        </div>
        <div class="svc-grid">
{svc_html}
        </div>
      </div>
    </section>

    <section class="section bg-navy">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">How it works</p>
          <h2>Three steps to the right home</h2>
        </div>
        <ol class="steps">
          <li class="reveal"><h3>Search and advice</h3><p class="step-sub">Areas, locations and property types</p><p>We listen first: who is moving, schools, commute, budget and timing. Then we shortlist the right areas and homes.</p></li>
          <li class="reveal"><h3>Viewings and analysis</h3><p class="step-sub">Narrow it down to the one</p><p>We book viewings with agents, send video and photos, and write up the pros and cons of every property so you can decide from abroad.</p></li>
          <li class="reveal"><h3>Negotiation to completion</h3><p class="step-sub">A plan that gets you moved in</p><p>We make offers and negotiate, coordinate surveyors, brokers and solicitors, and follow the purchase or tenancy until you have the keys.</p></li>
        </ol>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap">
        <div class="head center">
          <p class="eyebrow">Clear fees</p>
          <h2>Know what you'll pay before you start</h2>
          <p class="lead" style="margin:0 auto">All fees are plus VAT. See the full list for viewings and other services.</p>
        </div>
        <div class="price-strip">
          <div class="price reveal"><span class="price-label">Registration</span><div class="price-amt">£100<small>+ VAT</small></div><p class="price-note">Advice on buying or renting, UK property and living information, and suitable homes.</p></div>
          <div class="price reveal"><span class="price-label">Successful rental</span><div class="price-amt">£880<small>+ VAT</small></div><p class="price-note">£180 due when your offer is accepted. From £880 outside Hertfordshire.</p></div>
          <div class="price is-feature reveal"><span class="price-label">Successful purchase</span><div class="price-amt"><span class="from">from</span>£1,880<small>+ VAT</small></div><p class="price-note">Overseas clients from £2,880. £880 on agreed price, the rest only on completion.</p></div>
        </div>
        <p style="text-align:center;margin-top:28px"><a class="link-arrow" href="services.html">See all services and fees</a></p>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">UK homes explained</p>
          <h2>Six common types of UK home</h2>
          <p class="lead">British homes put space and family life first. Knowing how each type works helps you pick the one that suits your family and budget.</p>
        </div>
        <div class="types">
{types_html}
        </div>
      </div>
    </section>

{faq_section("About our consultancy service", "The questions people ask most before renting or buying in the UK for the first time.", faqs, " bg-cream")}

    <section class="section tight">
      <div class="wrap">
        <div class="head center">
          <p class="eyebrow">Partners and accreditation</p>
          <h2>Regulated with client money protected</h2>
        </div>
        <div class="accred" style="margin-bottom:48px">
          <a href="https://www.joyhomeuk.com/wp-content/uploads/2020/07/UKALA.pdf" target="_blank" rel="noopener"><img src="assets/img/ukala.webp" alt="UKALA" loading="lazy"><div><b>UKALA member</b><span>UK Association of Letting Agents</span></div></a>
          <a href="https://www.joyhomeuk.com/wp-content/uploads/2020/07/CMP.pdf" target="_blank" rel="noopener"><span class="ci" style="width:44px;height:44px;border-radius:12px;background:var(--gold-soft);color:var(--navy);display:grid;place-items:center">{icon('shield')}</span><div><b>Client Money Protection</b><span>Certificate (PDF)</span></div></a>
          <a href="https://www.theprs.co.uk/" target="_blank" rel="noopener"><img src="assets/img/prs.webp" alt="Property Redress Scheme" loading="lazy"><div><b>{PRS_NO}</b><span>Property Redress Scheme</span></div></a>
        </div>
        <ul class="logos">{partner_html}</ul>
      </div>
    </section>

{cta_band()}"""
    page("index.html", "JoyHome UK · UK property consultants for buying, renting and lettings",
         "JoyHome UK has helped clients from Hong Kong and overseas buy, rent, let and renovate UK homes since 2015. Registered, PRS029811, UKALA member.",
         body, active="", preload="assets/img/hero.webp")


def build_services():
    extras = ["Property inspections", "Shopping for essentials before you arrive", "Furniture buying and assembly", "Home cleaning",
              "Airport pick-up", "Key collection", "Check-in and inventory check", "Waiting in for deliveries"]
    body = f"""{page_hero("Services & fees", "Services & fees", "Clear fees<br>with most paid only on success", "All prices are in pounds plus VAT. Most of the buying and renting fee is charged only once you succeed. Surveyor, mortgage broker and solicitor fees are paid by the client.")}

    <div class="subnav"><div class="wrap"><ul>
      <li><a href="#consult">Advice</a></li><li><a href="#rent">Renting</a></li><li><a href="#buy">Buying</a></li><li><a href="#viewing">Viewings</a></li><li><a href="#extras">Extras</a></li>
    </ul></div></div>

    <section class="section">
      <div class="wrap">
        <article class="fee-card reveal" id="consult">
          <div>
            <span class="tag">Step one</span>
            <h2>Buying or renting advice</h2>
            <p class="lead">Register as a member and a consultant will learn what you need and start searching. Registration is also required for our viewing service.</p>
            {checklist(["Advice on buying UK property and living in the UK", "Professional search and recommended homes"])}
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>Registration fee</th><td>£100<small>+ VAT</small></td></tr>
            </tbody></table>
          </div>
        </article>

        <article class="fee-card reveal" id="rent">
          <div>
            <span class="tag">Renting</span>
            <h2>Successful rental</h2>
            <p class="lead">One fixed fee from search and viewings to offer, signing and move-in.</p>
            <a class="link-arrow" href="rent.html">How renting works</a>
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>Hertfordshire and nearby</th><td>£880<small>+ VAT</small></td></tr>
              <tr><th>Outside Hertfordshire</th><td>from £880<small>+ VAT</small></td></tr>
            </tbody></table>
            <p class="fee-foot">£180 is due when your offer is accepted; the balance once the tenancy is secured.</p>
          </div>
        </article>

        <article class="fee-card reveal" id="buy">
          <div>
            <span class="tag">Buying</span>
            <h2>Successful purchase</h2>
            {checklist(["In-depth pros and cons of every property", "Offers, negotiation and help to complete", "Recommended surveyors, mortgage brokers and solicitors", "Home Buyer Survey arranged and explained", "Liaising with your broker and solicitor on paperwork", "Collecting the property for you"])}
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>UK-based clients</th><td>£1,880<small>+ VAT</small></td></tr>
              <tr><th>Overseas clients · price under £600K</th><td>£2,880<small>+ VAT</small></td></tr>
              <tr><th>Overseas clients · price £600K or more</th><td>£3,880<small>+ VAT</small></td></tr>
              <tr><th>Negotiation fee</th><td>10%<small>of the amount saved</small></td></tr>
            </tbody></table>
            <p class="fee-foot">£880 is due when the price is agreed; the balance only on completion. Surveyor, broker and solicitor fees are paid by the client.</p>
          </div>
        </article>

        <article class="fee-card reveal" id="viewing">
          <div>
            <span class="tag">Not in the UK yet?</span>
            <h2>Viewings on your behalf</h2>
            <p class="lead">For buying or renting. We book the viewing with the agent and report back on video and in photos.</p>
            <p class="note">Available to registered members only.</p>
          </div>
          <div>
            <table class="fee-table"><tbody>
              <tr><th>Milton Keynes, Luton</th><td>£60<small>per property + VAT</small></td></tr>
              <tr><th>North London, Bedfordshire, Buckinghamshire, Hertfordshire</th><td>from £80<small>per property + VAT</small></td></tr>
              <tr><th>Other areas</th><td>On request<small>+£1 per mile return</small></td></tr>
            </tbody></table>
          </div>
        </article>

        <article class="fee-card reveal" id="extras">
          <div>
            <span class="tag">Before and after you arrive</span>
            <h2>Extra services</h2>
            <p class="lead">Get your home ready before you land.</p>
            <table class="fee-table"><tbody><tr><th>Per service</th><td>from £30<small>+ VAT</small></td></tr></tbody></table>
          </div>
          <div>
            <ul class="chips">{''.join(f'<li>{e}</li>' for e in extras)}</ul>
            <p class="note">Prices depend on area and workload. Ask us for a quote.</p>
          </div>
        </article>
      </div>
    </section>

{cta_band("Not sure which service you need?", "WhatsApp us your situation and a consultant will suggest the simplest, most cost-effective option.")}"""
    page("services.html", "Services & fees · JoyHome UK",
         "JoyHome UK fees for buying, renting, viewings and extra services. Registration £100, successful rental £880, purchase from £1,880 (plus VAT).", body)


def build_buy():
    cities = "\n".join(f"""          <a class="city reveal" href="contact.html">
            <img src="assets/img/{img}.webp" alt="{name}" loading="lazy" width="900" height="675">
            <div class="city-body"><b>{name}</b><p>{p}</p></div>
          </a>""" for img, name, p in CITIES_EN)
    mk = [("MK8 Pembroke Lane", "3-bed detached", "£500,000"), ("MK5 Shenley Brook End", "3-bed terrace", "£390,000"),
          ("MK4 Tattenhoe Park", "4-bed semi", "£460,000"), ("MK10 Oakgrove", "5-bed detached", "£660,000"),
          ("MK10 Middleton", "2-bed terrace", "£300,000"), ("MK5 Loughton", "4-bed detached", "£700,000")]
    mk_rows = "".join(f'<tr><td>{a}</td><td>{t}</td><td class="num">{p}</td></tr>' for a, t, p in mk)
    faqs = [
        ("I moved on a BN(O) visa. Do I pay the non-resident stamp duty surcharge?",
         "The extra 2% depends on how long you have been in the UK, not on your visa or passport. If you spent fewer than 183 days in the UK in the 12 months before buying, it usually applies. Families who buy soon after arriving should watch for this; in some cases it can be reclaimed later. Confirm your situation with your solicitor."),
        ("What's the difference between freehold and leasehold?",
         "Freehold means you own the building and the land outright. Leasehold means you own the home for a fixed term, often 99 to 999 years, and pay ground rent, service charges and building insurance. Leasehold homes cost less but usually grow less in value, and short leases are harder to sell or mortgage, so always check the remaining term."),
        ("Apart from stamp duty, what other costs are there?",
         "Typical costs include solicitor fees of about £1,000–2,000, a survey at about £600–850 and a Homebuyer Report at about £400–650 (strongly advised for older homes), plus mortgage fees, removals and insurance. These are guides only and vary by firm, area and price."),
        ("I own property in Hong Kong. What UK tax applies?",
         "Once you are UK tax resident, the UK taxes worldwide income and gains. Selling overseas property may mean Capital Gains Tax, and rent from a let property may be subject to Income Tax. We can introduce accountants who know Hong Kong clients; it's best to plan before you buy."),
        ("YouTubers say MK4, 5, 8 and 10 are the best parts of Milton Keynes. True?",
         "Those areas are popular overall, but every area has streets you would avoid. The most common mistake is buying from online photos alone, then finding the home doesn't match and won't let. Someone needs to see it in person."),
    ]
    body = f"""{page_hero("Buying", "Buying in the UK", "Buying in the UK<br>process, costs and tax made clear", "The same budget buys far more space in the UK. But mortgages, stamp duty and leaseholds work very differently from Hong Kong. JoyHome guides you from choosing an area to collecting the keys.", "assets/img/buy.webp", "A new-build housing development")}

    <div class="subnav"><div class="wrap"><ul>
      <li><a href="#areas">Areas</a></li><li><a href="#process">Process</a></li><li><a href="#tax">Stamp duty</a></li><li><a href="#mk">Milton Keynes</a></li><li><a href="#faq">FAQ</a></li>
    </ul></div></div>

    <section class="section" id="areas">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Popular areas</p>
          <h2>Where would you like to live?</h2>
          <p class="lead">Beyond London, Birmingham, Milton Keynes and Leeds all offer good value. Tell us what matters and we'll compare schools, transport, safety and prices for you.</p>
        </div>
        <div class="cities">
          <a class="city is-wide reveal" href="#mk">
            <img src="assets/img/city-mk.webp" srcset="assets/img/city-mk.webp 900w, assets/img/city-mk-1600.webp 1600w" sizes="(max-width: 520px) 100vw, 50vw" alt="Milton Keynes railway station" loading="lazy" width="900" height="600">
            <div class="city-body"><b>Milton Keynes</b><p>A favourite with Hong Kong families. 35 minutes direct to London Euston, with green space and good schools.</p></div>
          </a>
{cities}
        </div>
      </div>
    </section>

    <section class="section bg-cream" id="process">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">How buying works</p>
          <h2>New builds and resale homes follow different steps</h2>
        </div>
        <div class="tabs" role="tablist" aria-label="Type of purchase">
          <button role="tab" id="tab-resale" aria-controls="panel-resale" aria-selected="true">Resale</button>
          <button role="tab" id="tab-new" aria-controls="panel-new" aria-selected="false" tabindex="-1">New build / off-plan</button>
        </div>
        <div class="grid-2">
          <div>
            <div role="tabpanel" id="panel-resale" aria-labelledby="tab-resale">
              <ol class="timeline">
                <li><h3>Get an Agreement in Principle</h3><p>If you need a mortgage, get one from a lender or broker first. It shows sellers you're serious and strengthens your offer.</p></li>
                <li><h3>Search and view</h3><p>If you're abroad, a consultant views for you, films and photographs it, and reports on the surroundings.</p></li>
                <li><h3>Offer and Memorandum of Sale</h3><p>Once a price is agreed, the memorandum records the price and the property details.</p></li>
                <li><h3>Survey and mortgage approval<span class="when">about 2–3 months</span></h3><p>A surveyor checks the inside, outside, garage and garden; issues can be raised with the seller or used to renegotiate. The lender approves based on valuation and affordability.</p></li>
                <li><h3>Exchange and completion</h3><p>Solicitors draft the contract and you pay about 10% on exchange. Once everything is in place you pay the balance and stamp duty and collect the keys.</p></li>
              </ol>
            </div>
            <div role="tabpanel" id="panel-new" aria-labelledby="tab-new" hidden>
              <ol class="timeline">
                <li><h3>Reservation agreement</h3><p>Choose a plot and pay a reservation fee, from a few hundred to a few thousand pounds depending on the developer.</p></li>
                <li><h3>Instruct a solicitor and exchange</h3><p>Sign the contract and usually pay about 10% of the price as a deposit.</p></li>
                <li><h3>Mortgage<span class="when">about 6 months before handover</span></h3><p>If you need a mortgage, we introduce a broker to find a suitable product.</p></li>
                <li><h3>Snagging inspection</h3><p>An inspector checks the home before handover and lists anything the developer must fix.</p></li>
                <li><h3>Completion and keys</h3><p>Pay the balance, stamp duty and fees, and move in.</p></li>
              </ol>
            </div>
          </div>
          <div>
            <div class="card">
              <div class="card-icon">{icon('users')}</div>
              <h3>What JoyHome does at each step</h3>
              {checklist(["Writes up the pros and cons of each property", "Makes offers and negotiates the best terms", "Recommends surveyors, brokers and solicitors", "Explains your Homebuyer Report and what to follow up", "Liaises with your solicitor and broker", "Collects the property for you"])}
              <p style="margin-top:18px"><a class="link-arrow" href="services.html#buy">Buying fees</a></p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="tax">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Tax when buying</p>
          <h2>Stamp Duty Land Tax</h2>
          <p class="lead">Stamp duty is charged in bands of the price. First-time buyers, additional homes and non-residents pay different rates. These are the rates for homes in England.</p>
        </div>
        <div class="grid-2">
          <div class="table-scroll">
            <table class="data-table">
              <thead><tr><th>Portion of the price</th><th class="num">Standard</th><th class="num">Additional home</th></tr></thead>
              <tbody>
                <tr><td>Up to £125,000</td><td class="num">0%</td><td class="num">5%</td></tr>
                <tr><td>£125,001 – £250,000</td><td class="num">2%</td><td class="num">7%</td></tr>
                <tr><td>£250,001 – £925,000</td><td class="num">5%</td><td class="num">10%</td></tr>
                <tr><td>£925,001 – £1.5M</td><td class="num">10%</td><td class="num">15%</td></tr>
                <tr><td>Over £1.5M</td><td class="num">12%</td><td class="num">17%</td></tr>
              </tbody>
            </table>
            <p class="note">Rates in force from April 2025, for guidance only. Check the latest on <a href="https://www.gov.uk/stamp-duty-land-tax/residential-property-rates" target="_blank" rel="noopener">GOV.UK</a>.</p>
          </div>
          <div style="display:grid;gap:16px;align-content:start">
            <div class="callout"><p><b>First-time buyers</b>: nothing on the first £300,000 and 5% on £300,001–£500,000. Above £500,000, standard rates apply.</p></div>
            <div class="callout"><p><b>Non-resident surcharge</b>: an extra 2% on every band if you spent fewer than 183 days in the UK in the 12 months before buying.</p></div>
            <div class="callout"><p><b>Council Tax</b>: paid yearly by whoever lives in the home, based on the property's band and area.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-cream" id="mk">
      <div class="wrap">
        <div class="split">
          <div>
            <p class="eyebrow">Area focus</p>
            <h2>Milton Keynes for Hong Kong families</h2>
            <p>North of London in Buckinghamshire, with nearly 300,000 people, Milton Keynes became a city in 2022. It is well planned, full of parks and lakes, and has many schools rated Outstanding or Good by Ofsted.</p>
            <p>MK4 (Tattenhoe, Shenley Brook End, Emerson Valley), MK5 (Shenley Church End, Loughton) and MK8 (Whitehouse) in the west and MK10 in the east all have strong school catchments; the east is closer to the M1. Three-bed semis are the most popular and the easiest to let.</p>
            <div class="facts">
              <div><b>35 min</b><span>direct to Euston</span></div>
              <div><b>4–5.1%</b><span>indicative yield</span></div>
              <div><b>from £300K</b><span>3-bed semi</span></div>
            </div>
          </div>
          <div>
            <div class="table-scroll">
              <table class="data-table">
                <thead><tr><th>Area</th><th>Type</th><th class="num">Guide price</th></tr></thead>
                <tbody>{mk_rows}</tbody>
              </table>
            </div>
            <p class="note">Past recommendations shown as a price guide, not current listings.</p>
          </div>
        </div>
      </div>
    </section>

{faq_section("About buying in the UK", "Stamp duty, tenure and extra costs come up every time.", faqs)}

{cta_band("Ready to buy in the UK?", "Book a consultation and we'll compare the areas that best fit your budget and family.")}"""
    page("buy.html", "Buying in the UK · process, stamp duty and areas | JoyHome UK",
         "How buying a home in the UK works, stamp duty, freehold and leasehold, and popular areas such as Milton Keynes. JoyHome UK supports you from search to keys.", body)


def build_rent():
    docs = [("Passport / BRP / eVisa", "Proof of identity"), ("Right to Rent", "Proof you can rent in the UK, such as BN(O) visa approval"),
            ("Proof of work", "Some landlords don't accept self-employed or part-time tenants"), ("Bank statements", "Some landlords ask for a UK bank account"),
            ("Credit report", "Checked during referencing")]
    doc_html = "\n".join(f'          <div class="card reveal"><div class="card-icon">{icon("doc")}</div><h3>{a}</h3><p>{c}</p></div>' for a, c in docs)
    faqs = [
        ("Which UK rental websites can I trust?",
         "Rightmove, Zoopla, OpenRent and SpareRoom are the most used. Pick your town and area, compare rents, then look at amenities, schools, safety and transport. If you're in Hong Kong, JoyHome can handle the whole process for you."),
        ("We have two cats and a big dog. Will renting be hard?",
         "Some landlords don't accept pets or ask for higher rent. Pets are family, so we actively look for pet-friendly homes. With pets, allow 3 to 4 months before you arrive."),
        ("How much money do I need to rent?",
         "Mainly the deposit, the first month's rent and any consultancy fee. For rents under £50,000 a year, the deposit is capped at 5 weeks' rent and a holding deposit at 1 week's rent. You'll also pay utilities, broadband and Council Tax. Renting law in England changed significantly in 2026, including rules on rent in advance, and we'll explain the current position."),
        ("Detached, terraced or flat: which is best value?",
         "Terraces are often older and lower, so watch for security, damp and ageing fittings, which is why rents are lower. Newer flats tend to have fewer security and structural issues. In the end it's about area, budget, schools and transport together."),
    ]
    body = f"""{page_hero("Renting", "Renting in the UK", "Find your first home<br>before you land", "Good rentals get offers soon after listing and tenancies complete within 3 to 4 weeks. Allow 2 to 3 months before you arrive. JoyHome searches, views, prepares your documents and follows through to move-in.", "assets/img/rent.webp", "A London street")}

    <section class="section">
      <div class="wrap">
        <div class="grid-2" style="align-items:start;gap:clamp(32px,6vw,80px)">
          <div>
            <p class="eyebrow">How renting works</p>
            <h2>A few more steps than in Hong Kong</h2>
            <p class="lead">Landlords reference tenants to check they can pay the rent. If you don't have a UK income yet, prepare your documents early.</p>
            <p><a class="link-arrow" href="services.html#rent">Rental fee: £880 + VAT on success</a></p>
          </div>
          <ol class="timeline">
            <li class="reveal"><h3>Search and viewings</h3><p>We shortlist by town, schools and budget. If you're abroad, a consultant views for you and reports on video.</p></li>
            <li class="reveal"><h3>Offer and holding deposit</h3><p>Once you choose a home, you pay a holding deposit of up to 1 week's rent.</p></li>
            <li class="reveal"><h3>Referencing<span class="when">about 2–3 weeks</span></h3><p>The landlord checks your identity, Right to Rent, income and credit history.</p></li>
            <li class="reveal"><h3>Tenancy and deposit</h3><p>You sign the tenancy agreement and the deposit is protected in a government-approved scheme.</p></li>
            <li class="reveal"><h3>Inventory and move-in</h3><p>Every item and its condition is recorded, which matters when you get your deposit back.</p></li>
          </ol>
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Referencing</p>
          <h2>Documents you'll need</h2>
        </div>
        <div class="grid-3" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">
{doc_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split reverse">
        <div class="split-media reveal"><img src="assets/img/rent-london.webp" alt="Westminster and Big Ben" loading="lazy" width="768" height="516"></div>
        <div>
          <p class="eyebrow">London and beyond</p>
          <h2>London or another city?</h2>
          <p>London has the highest rents but the most jobs and schools. Rents elsewhere are generally lower and homes are bigger. We know North London, Hertfordshire, Milton Keynes and Luton well, and can help in other cities too.</p>
          <p>Many families rent first, get to know an area, and then decide where to buy.</p>
          <a class="btn btn-primary" href="contact.html">Tell us what you need</a>
        </div>
      </div>
    </section>

{faq_section("About renting in the UK", "Pets, budgets and property types: the questions people ask before renting.", faqs, " bg-cream")}

{cta_band("Want your home ready before you arrive?", "We can also shop for essentials, collect keys and pick you up from the airport, from £30.")}"""
    page("rent.html", "Renting in the UK · process, documents and costs | JoyHome UK",
         "How renting a home in the UK works, referencing documents, deposits and costs. JoyHome UK searches and views for you through to move-in.", body)


def build_management():
    let_steps = [("Valuation", "A realistic rent based on location, condition and local demand."),
                 ("Photos and description", "Professional photos and an accurate, appealing description."),
                 ("Advertising", "Listed on the JoyHome Facebook page and the main property portals."),
                 ("Viewings", "We show the property to interested tenants and screen applicants."),
                 ("Credit checks", "Tenant referencing through an approved agency."),
                 ("First rent and tenancy", "We collect the first month's rent and deposit and sign a compliant tenancy agreement.")]
    manage = ["Gas and electrical safety certificates before the tenancy, with the gas certificate renewed yearly",
              "A photo and written inventory before move-in, used when the deposit is returned",
              "Monthly rent collection", "Handling tenant queries and repairs and keeping you informed",
              "Reliable contractors for repairs, with your approval", "A signed photo record of every key issued",
              "Holding keys and all property documents during the tenancy", "Regular inspections, usually every 6 months",
              "Serving legal notices for rent increases, renewals or ending a tenancy"]
    steps_html = "\n".join(f'          <div class="card reveal"><h3>{i + 1:02d}　{a}</h3><p>{c}</p></div>' for i, (a, c) in enumerate(let_steps))
    faqs = [
        ("How do I appoint JHPM?", "We send you a management agreement covering the address, description, expected rent, our fees and terms. You add your details and the bank account for rent, sign it and send it back, and we can start."),
        ("Does JHPM inspect the property?", "Yes. We usually inspect every 6 months and send you a report."),
        ("I live overseas. Can you manage my property?", "Yes. JHPM has helped many overseas landlords and is registered with the Non-Resident Landlord Scheme, which makes it easier for you to register as a non-resident landlord."),
    ]
    body = f"""{page_hero("Lettings", "Property management · JHPM", "Your UK property looked after<br>wherever you live", "JoyHome Property Management (JHPM) is our sister company, founded in January 2021 and a member of UKALA and the PRS. We let, collect rent and manage homes for landlords investing in the UK.", "assets/img/manage.webp", "A semi-detached house")}

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Service one</p>
          <h2>Finding good tenants fast</h2>
        </div>
        <div class="grid-3">
{steps_html}
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Service two</p>
          <h2>Full tenancy management</h2>
          <p class="lead">From safety certificates before the tenancy to repairs and legal notices during it, we handle it all.</p>
        </div>
        <div>{checklist(manage)}</div>
      </div>
    </section>

    <section class="section bg-navy">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Why JHPM</p>
          <h2>Three reasons landlords trust us</h2>
        </div>
        <div class="grid-3">
          <div class="card reveal"><div class="card-icon">{icon('shield')}</div><h3>Reliable</h3><p>A member of UKALA and the PRS, regulated by UKALA. Rent goes through a separate client account, covered by Client Money Protection.</p></div>
          <div class="card reveal"><div class="card-icon">{icon('eye')}</div><h3>Transparent</h3><p>We update you from listing to signing, and tell you straight away about any maintenance issue.</p></div>
          <div class="card reveal"><div class="card-icon">{icon('chat')}</div><h3>Easy to reach</h3><p>WhatsApp, email or phone, in English or Chinese. No chasing an agent who never picks up.</p></div>
        </div>
      </div>
    </section>

{faq_section("About property management", "What landlords ask before appointing us.", faqs)}

{cta_band("Have a property to let?", "Tell us the address and type and we'll estimate the rent and our fees.")}"""
    page("management.html", "Property management · JHPM | JoyHome UK",
         "JoyHome Property Management: UKALA and PRS member letting and managing homes for overseas landlords, with Client Money Protection.", body)


def build_renovation():
    trades = [
        ("Carpentry", ["Laminate, LVT and SPC flooring", "Feature walls and doors", "Double-glazed uPVC windows", "Skirting and coving", "Fitted furniture and stairs", "Loft and garage conversions", "Conservatories"]),
        ("Plumbing and heating", ["Radiators", "Boilers", "Showers", "Drainage", "Bathroom fittings"]),
        ("Plastering", ["Stud and plaster walls", "Wall removal", "Open-plan kitchens", "Period coving restored"]),
        ("Electrics", ["Consumer unit moves", "Electric radiators and lighting", "Full rewiring", "Smart home systems", "Smoke and security alarms"]),
        ("Decorating", ["Walls and ceilings", "Wallpapering", "Feature walls"]),
        ("Tiling", ["Kitchen and bathroom tiles", "Floor and wall tiling"]),
    ]
    trade_html = "\n".join(f'          <div class="card reveal"><h3>{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for t, items in trades)
    body = f"""{page_hero("Renovation", "JoyHome Builder", "Turn a UK house<br>into your home", "JoyHome Builder is the renovation team of JoyHome Service Ltd: bathrooms, kitchens, full refurbishments, extensions and conservatories. Local trades with a Hong Kong-background project manager, so nothing gets lost in translation.", "assets/img/reno-kitchen.webp", "A finished open-plan kitchen")}

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Our work</p>
          <h2>Real finished projects</h2>
        </div>
        <div class="gallery">
          <figure><img src="assets/img/reno-kitchen-1800.webp" alt="Kitchen after a full renovation" loading="lazy"><figcaption>Full renovation</figcaption></figure>
          <figure><img src="assets/img/reno-bath.webp" alt="Refitted bathroom" loading="lazy"><figcaption>Bathroom</figcaption></figure>
          <figure><img src="assets/img/reno-conservatory.webp" alt="Conservatory with new flooring" loading="lazy"><figcaption>Conservatory</figcaption></figure>
          <figure><img src="assets/img/reno-bath2.webp" alt="Bathroom basin and vanity unit" loading="lazy"><figcaption>Bathroom</figcaption></figure>
          <figure><img src="assets/img/reno-before.webp" alt="Wall removal in progress" loading="lazy"><figcaption>Wall removal</figcaption></figure>
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">Why JoyHome Builder</p>
          <h2>Quality and budget with clear communication</h2>
        </div>
        <div class="grid-3">
          <div class="card reveal"><div class="card-icon">{icon('home')}</div><h3>Quality</h3><p>Finished to a high standard that adds comfort and value.</p></div>
          <div class="card reveal"><div class="card-icon">{icon('users')}</div><h3>A dedicated project manager</h3><p>One person from plan to handover, keeping costs under control.</p></div>
          <div class="card reveal"><div class="card-icon">{icon('pound')}</div><h3>Materials at trade prices</h3><p>Our suppliers offer fair prices that keep your budget down.</p></div>
          <div class="card reveal"><div class="card-icon">{icon('chat')}</div><h3>A mixed team</h3><p>Local British trades and Hong Kong-background staff who understand how you live.</p></div>
          <div class="card reveal"><div class="card-icon">{icon('tool')}</div><h3>Full range</h3><p>From whole-house refurbishments to the garden, in any style.</p></div>
          <div class="card reveal"><div class="card-icon">{icon('trend')}</div><h3>Adds value</h3><p>Kitchens, bathrooms and extensions are the surest way to raise resale and rental value.</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head">
          <p class="eyebrow">What we do</p>
          <h2>Every trade in one team</h2>
          <p class="lead">Bathrooms from new suites to wet rooms, kitchens from compact to open-plan, extensions from extra rooms to conservatories.</p>
        </div>
        <div class="trades">
{trade_html}
        </div>
      </div>
    </section>

{cta_band("Planning a renovation?", "Send us a few photos and your ideas and we'll estimate the scope and budget.")}"""
    page("renovation.html", "Renovation · JoyHome Builder | JoyHome UK",
         "JoyHome Builder renovates UK homes: bathrooms, kitchens, full refurbishments, extensions and conservatories, with a dedicated project manager.", body)


def build_contact():
    services = ["Buying", "Renting", "Viewings", "Lettings", "Renovation", "Other"]
    picks = "".join(f'<label><input type="checkbox" name="service" value="{s}"><span>{s}</span></label>' for s in services)
    body = f"""{page_hero("Contact", "Contact", "Tell us your plans", "WhatsApp is fastest. Or fill in the form below and we'll turn it into a ready-to-send WhatsApp message or email.", ctas=False)}

    <section class="section" style="padding-top:clamp(40px,5vw,64px)">
      <div class="wrap contact-grid">
        <div>
          <ul class="contact-list">
            <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener"><span class="ci wa">{icon('wa')}</span><span><small>WhatsApp (fastest)</small><b>{PHONE}</b></span></a></li>
            <li><a href="tel:{TEL}"><span class="ci">{icon('phone')}</span><span><small>Phone</small><b>{PHONE}</b></span></a></li>
            <li><a href="mailto:{EMAIL}"><span class="ci">{icon('mail')}</span><span><small>Email</small><b>{EMAIL}</b></span></a></li>
            <li><a href="{FB}" target="_blank" rel="noopener"><span class="ci">{icon('fb')}</span><span><small>Facebook</small><b>JoyhomeUK</b></span></a></li>
          </ul>
          <h3>Office hours</h3>
          <table class="hours"><tbody>
            <tr><td>Monday to Friday</td><td>9:00 – 17:00 (UK time)</td></tr>
            <tr><td>Weekends and bank holidays</td><td>Closed</td></tr>
          </tbody></table>
          <p class="note">Hong Kong is 7 hours ahead of the UK in summer and 8 hours ahead in winter.</p>
        </div>

        <form class="form" action="mailto:{EMAIL}" method="post" enctype="text/plain" data-enquiry data-wa="{WA}" data-mail="{EMAIL}">
          <h2 style="font-size:26px">Enquiry form</h2>
          <fieldset class="field">
            <legend>I'm interested in</legend>
            <div class="pick">{picks}</div>
          </fieldset>
          <div class="field-row">
            <div class="field"><label for="f-area">Area<span class="opt">optional</span></label><input id="f-area" name="area" placeholder="e.g. Milton Keynes"></div>
            <div class="field"><label for="f-when">Timing<span class="opt">optional</span></label>
              <select id="f-when" name="when"><option value="">Choose</option><option>Within a month</option><option>1–3 months</option><option>3–6 months</option><option>6+ months</option><option>Not sure yet</option></select></div>
          </div>
          <div class="field"><label for="f-budget">Budget<span class="opt">optional</span></label><input id="f-budget" name="budget" placeholder="e.g. £1,500 a month / £400K"></div>
          <div class="field-row">
            <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div>
            <div class="field"><label for="f-reply">Email or phone</label><input id="f-reply" name="reply" required autocomplete="email" placeholder="So we can reply"></div>
          </div>
          <div class="field"><label for="f-msg">Your question</label><textarea id="f-msg" name="message" placeholder="Family members, schools, pets, arrival date: the more detail the better"></textarea></div>
          <div class="form-actions">
            <button class="btn btn-wa" type="submit" value="wa">{icon('wa')}Send by WhatsApp</button>
            <button class="btn btn-ghost" type="submit" value="email">{icon('mail')}Send by email</button>
          </div>
          <p class="form-hint">This opens WhatsApp or your email app with the message filled in. Check it, then press send.</p>
        </form>
      </div>
    </section>"""
    page("contact.html", "Contact · JoyHome UK", "Contact JoyHome UK by WhatsApp, phone or email. Office hours Monday to Friday 9:00–17:00 UK time.", body)


def build_all():
    b.LANG = "en"
    try:
        for f in (build_index, build_services, build_buy, build_rent, build_management, build_renovation, build_contact):
            f()
    finally:
        b.LANG = "zh"
