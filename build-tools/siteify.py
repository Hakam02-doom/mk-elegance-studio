"""Turn the rebranded Morgana (Shopify) pages into a static studio website for MK Elegance.
Removes shop machinery (cart, login, search, wishlist, filters, variant pickers, fake social proof),
wires every link and CTA, and makes forms work without a backend.
usage: venv/bin/python -I siteify.py SITE_DIR"""
import os, re, sys, copy
from bs4 import BeautifulSoup, Comment

sys.path.insert(0, os.path.dirname(__file__))
from content import JANE, IG, FB

SITE = sys.argv[1]
MK = 'https://www.mkelegancestudio.ca'
EMAIL = 'care@mkelegancestudio.com'
PHONE = '+13653367271'
PHONE_TXT = '+1 (365) 336-7271'
GOOGLE = 'https://www.google.com/maps/search/?api=1&query=MK+Elegance+Studio+116+King+St+S+Waterloo'

# Pages not rebuilt yet point at the current official pages. Swap to local paths as they are built.
LINKS = {
    'Home': 'index.html', 'Services': 'services.html', 'Treatments': 'services.html',
    'About': 'about.html', 'About Mital': 'about.html', 'Blog': 'blog.html', 'FAQ': 'faq.html',
    'Contact': 'contact.html', 'Contact & Hours': 'contact.html',
    'Brows & Lashes': 'services.html', 'Hair Removal': 'services.html', 'Facials': f'{MK}/services/facials/',
    'Advanced Skin': f'{MK}/skin-treatments/',
    'Eyebrow Threading': f'{MK}/services/threading/', 'Threading': f'{MK}/services/threading/',
    'Full Face Threading': f'{MK}/services/threading/', 'Upper Lip Threading': f'{MK}/services/threading/',
    'Brow Tint': f'{MK}/services/brow-tint/', 'Tinted Elegance Brow Duo': f'{MK}/services/brow-tint/',
    'Brow Lamination': f'{MK}/services/brow-lamination/', 'Lash Lift & Tint': f'{MK}/services/lash-lift-and-tint/',
    'Face & Body Waxing': f'{MK}/services/waxing/', 'Waxing': f'{MK}/services/waxing/', 'Full Legs Wax': f'{MK}/services/waxing/',
    'Underarm Wax': f'{MK}/services/waxing/',
    'Brazilian Wax': f'{MK}/services/brazilian-wax/', 'Hollywood Wax': f'{MK}/services/brazilian-wax/',
    'Brazilian Renewal': f'{MK}/services/brazilian-wax/', 'Bikini Wax': f'{MK}/services/bikini-wax/',
    'Customised Facial': f'{MK}/services/customised-facial/', 'First-Time Full Face': f'{MK}/services/threading/',
    'Diego dalla Palma Rituals': f'{MK}/services/ddp-facial-rituals/', 'Hydra Plump Ritual': 'service.html',
    'NaturMed Facials': f'{MK}/services/naturmed-facials/', 'Express Glow Facial': f'{MK}/services/naturmed-facials/',
    'Body Facials': f'{MK}/services/back-facial/', 'Back Facial': f'{MK}/services/back-facial/',
    'Hand Facial': f'{MK}/services/hand-facial/', 'Hand Facial · Student': f'{MK}/students/',
    'Leg Facial': f'{MK}/services/leg-facial/', 'SQT Bio Microneedling': f'{MK}/services/sqt-bio-microneedling/',
    'Men’s Threading': f'{MK}/men/', 'Men': f'{MK}/men/', 'Skin Quiz': f'{MK}/skin-quiz/',
    'Skin Treatments': f'{MK}/skin-treatments/',
    'Privacy Policy': f'{MK}/privacy/', 'Terms of Service': f'{MK}/terms/', 'How Booking Works': f'{MK}/booking/',
    'Waterloo': f'{MK}/waterloo/', 'Kitchener': f'{MK}/kitchener/', 'Cambridge': f'{MK}/cambridge/',
    'Guelph': f'{MK}/guelph/', 'Elmira': f'{MK}/elmira/',
    'What to Expect From Your First Professional Facial': 'article.html',
    'Is a Lash Lift and Tint Right for You?': f'{MK}/blog/',
    'Eyebrow Tint vs Eyebrow Threading': f'{MK}/blog/eyebrow-tint-vs-eyebrow-threading/',
    'Brazilian Waxing in Waterloo: Prices and Preparation': f'{MK}/blog/brazilian-waxing-waterloo-preparation-guide/',
    'FB': FB, 'Facebook': FB, 'Fb': FB, 'IN': IG, 'Instagram': IG, 'In': IG,
}
REMOVE = [
    'cart-drawer', 'cart-notification', '.header__icon--cart', '.header__icon--account', 'details-modal.header__search',
    '.menu-drawer__account', 'quick-add-modal', 'ul.product-icons', '.card-wrapper product-form', '.card-wrapper form',
    '#shopify-section-suggested-products', '.list-payment', '.product__payment', 'shop-cart-sync',
    '.facets-container', 'facet-filters-form', '.social-proof-sales', 'variant-radios',
    'variant-selects', '.product-form__noscript-wrapper', 'product-form', '.product-form__input--quantity',
    'quantity-input', '.installment', 'dtx-wishlist', 'dtx-compare', 'product-recommendations', '.recent-view-container',
    '.recently-viewed', '[id*=judge_me]', '.jdgm-widget', '.sticky-bar-form', '.load-more', '.load-more_wrap',
    '.collection-load-more', '.comment-form', '.product__view-details', '.dt-sc-product__price-form',
]
DROP_JS = {'cart', 'cart-drawer', 'cart-notification', 'product-form', 'quick-add', 'predictive-search',
           'shipping', 'dt_wishlist', 'axios.min', 'handlebars.min', 'details-modal',
           'portable-wallets.en', 'pickup-availability'}

def js_stem(src):
    b = src.split('/')[-1].split('?')[0]
    return re.sub(r'(-[0-9a-f]{6})?\.js$', '', b)

def book_button(soup, label='Book on Jane App', cls='button button--primary'):
    a = soup.new_tag('a', href=JANE, target='_blank', rel='noopener', **{'class': cls})
    a.string = label
    return a

def frag(soup, html):
    return BeautifulSoup(html, 'html.parser')

def process(name):
    p = os.path.join(SITE, name)
    soup = BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser')

    # scripts that only served the store
    for s in soup.find_all('script', src=True):
        if js_stem(s['src']) in DROP_JS:
            s.decompose()
    for s in soup.find_all('script'):
        if s.decomposed: continue
        src_attr = s.get('data-source-attribution', '')
        body = s.string or ''
        if ('shopify' in src_attr or 'flashSoldBar' in body or 'recently_viewed' in body.lower()
                or 'event_observer' in body or 'sticky-bar-close' in body or 'DT_GrvP' in body):
            s.decompose()

    for l in soup.find_all('link', href=re.compile(r'accelerated-checkout|sticky-cart|pickup-availability|quick-add|cart-drawer|component-cart|component-totals|component-discounts|list-payment|predictive-search')):
        l.decompose()

    # hide-and-remove shop components
    for sel in REMOVE:
        for e in soup.select(sel):
            e.decompose()

    # header: Book Now in place of the cart/account icons
    icons = soup.select_one('.header__icons')
    if icons and not icons.select_one('.mk-book'):
        icons.append(book_button(soup, 'Book Now', 'button button--primary mk-book'))

    # social: MK is on Instagram and Facebook only
    for a in soup.select('a.list-social__link, .social-icons a, a[class*=social], .list-social a'):
        if a.decomposed: continue
        words = set(' '.join(a.get_text().split()).lower().split())
        if words & {'tw', 'twitter', 'youtube', 'yt'}:
            li = a.find_parent('li')
            (li or a).decompose()
        elif words & {'fb', 'facebook'}:
            a['href'] = FB; a['target'] = '_blank'; a['rel'] = 'noopener'
        elif words & {'in', 'instagram'}:
            a['href'] = IG; a['target'] = '_blank'; a['rel'] = 'noopener'
    # offer marquee -> current offers page
    for a in soup.select('.marquee-inner-wrapper a'):
        a['href'] = f'{MK}/offers/'; a['target'] = '_blank'; a['rel'] = 'noopener'

    # product cards: whole card -> service page (if built) or the matching live page
    for card in soup.select('.card-wrapper, .dt-sc-product, .product-sidebar-item'):
        h = card.select_one('.card__heading, .dt-sc-product__title, h3, h4')
        if not h: continue
        title = ' '.join(h.get_text().split())
        url = LINKS.get(title)
        if url:
            for a in card.find_all('a'):
                a['href'] = url
                if url.startswith('http'): a['target'] = '_blank'; a['rel'] = 'noopener'

    # generic links that went nowhere
    for a in soup.find_all('a'):
        t = ' '.join(a.get_text().split())
        href = a.get('href', '')
        if href in ('#', '', 'javascript:void(0);') or (href == 'service.html' and LINKS.get(t, 'service.html') != 'service.html'):
            if t in LINKS:
                a['href'] = LINKS[t]
                if LINKS[t].startswith('http'): a['target'] = '_blank'; a['rel'] = 'noopener'
        if t.lower().startswith('book') and 'janeapp' not in a.get('href', ''):
            a['href'] = JANE; a['target'] = '_blank'; a['rel'] = 'noopener'

    # newsletter modal: no mailing list exists -> welcome offer with Book / Instagram
    for form in soup.select('form.newsletter-form'):
        box = frag(soup, f'''<div class="mk-offer-ctas">
          <a class="button button--primary" href="{JANE}" target="_blank" rel="noopener">Book your first visit</a>
          <a class="button button--secondary" href="{IG}" target="_blank" rel="noopener">Follow @mkelegancestudio</a>
          <p class="mk-offer-note">Up to 20% off your first visit · mention the offer when you book.</p></div>''')
        form.replace_with(box)

    # contact-style forms: no backend -> compose an email to the studio
    for form in soup.select('form.isolate, form.contact-form, form#ContactForm, form[action*="contact#ContactForm"]'):
        form['action'] = f'mailto:{EMAIL}?subject=Website%20enquiry'
        form['method'] = 'post'; form['enctype'] = 'text/plain'
        for i in form.select('input[name="form_type"], input[name="utf8"]'):
            i.decompose()

    # search boxes in sidebars (blog) have no index to search
    for f in soup.select('form[role=search]'):
        w = f.find_parent(class_=re.compile('widget|sidebar|search')) or f
        w.decompose()

    # meta
    for m in soup.select('link[rel=canonical]'):
        m['href'] = MK + '/'
    for m in soup.find_all('meta', attrs={'property': re.compile('^og:')}):
        if m.get('property') == 'og:site_name': m['content'] = 'MK Elegance Studio'
        if m.get('property') == 'og:url': m['content'] = MK + '/'
    for m in soup.find_all('meta', attrs={'name': 'description'}):
        m['content'] = 'MK Elegance Studio — threading, waxing, brows & lashes and Diego dalla Palma facials in Uptown Waterloo. 116 King St S, Floor 1. Book on Jane App.'

    # ---- page specific ----
    if name == 'service.html':
        info = soup.select_one('.product__info-container')
        price = info.select_one('[id^=price-]') if info else None
        if price and not soup.select_one('.mk-service-book'):
            price.insert_after(frag(soup, f'''<div class="mk-service-book">
              <a class="mk-rating" href="{GOOGLE}" target="_blank" rel="noopener">★★★★★ <span>4.9 · 185 Google reviews</span></a>
              <dl class="mk-facts">
                <div><dt>Best for</dt><dd>Dehydrated, dull skin</dd></div>
                <div><dt>Line</dt><dd>Diego dalla Palma · HA Hero</dd></div>
                <div><dt>Duration</dt><dd>60 minutes</dd></div>
              </dl>
              <div class="mk-service-ctas">
                <a class="button button--primary" href="{JANE}" target="_blank" rel="noopener">Book on Jane App</a>
                <a class="button button--secondary" href="tel:{PHONE}">Call or text {PHONE_TXT}</a>
              </div></div>'''))
        for b in soup.find_all(string=re.compile(r'^\s*Write a review\s*$')):
            a = b.find_parent(['a', 'button'])
            if a:
                new = soup.new_tag('a', href=GOOGLE, target='_blank', rel='noopener', **{'class': a.get('class', [])})
                new.string = 'Read all reviews on Google'
                a.replace_with(new)
        for d in soup.select('.html-sections-product'):
            d.decompose()  # duplicated by the facts list above

    if name == 'services.html':
        for t in soup.find_all(string=re.compile(r"You're viewing|Showing \d")):
            if t.parent: t.parent.decompose()

    if name == 'article.html':
        for h in soup.find_all(['h2', 'h3', 'h4'], string=re.compile('Leave a Reply')):
            box = h.find_parent(class_=re.compile('comment|reply')) or h
            box.replace_with(frag(soup, f'''<div class="mk-article-cta">
              <h3>Ready for your first facial?</h3>
              <p>Book on Jane App 24/7, or call or text {PHONE_TXT}. First-time clients get up to 20% off.</p>
              <a class="button button--primary" href="{JANE}" target="_blank" rel="noopener">Book a facial</a></div>'''))

    if name == 'booking.html':
        main = soup.select_one('main')
        holder = main.select_one('.cart__warnings, .cart, cart-items, .page-width') if main else None
        block = frag(soup, f'''<div class="page-width mk-booking">
          <p class="mk-eyebrow">How booking works</p>
          <h2>Book your appointment</h2>
          <p>Every MK Elegance Studio service is booked on Jane App, 24/7 — open Mital’s page at Luna Aesthetics,
             choose your service and time, and you’ll get a confirmation email.</p>
          <div class="mk-service-ctas">
            <a class="button button--primary" href="{JANE}" target="_blank" rel="noopener">Book on Jane App</a>
            <a class="button button--secondary" href="tel:{PHONE}">Call or text {PHONE_TXT}</a>
          </div>
          <dl class="mk-facts">
            <div><dt>Hours</dt><dd>Mon–Fri 10–6:30 · Sat 10–6 · Sun closed</dd></div>
            <div><dt>Walk-ins</dt><dd>Welcome Mon–Sat when there’s a gap</dd></div>
            <div><dt>Where</dt><dd>116 King St S, Floor 1 — Luna Aesthetics door beside Pilot Coffee Roasters</dd></div>
            <div><dt>Offers</dt><dd>Up to 20% off your first visit · students 10% off every visit</dd></div>
          </dl></div>''')
        if holder:
            holder.replace_with(block)

    out = str(soup)
    # testimonials quote 5-star Google reviews; Morgana's demo showed 4 / 4.5 stars
    out = re.sub(r'class="(four|four-half|three|three-half)-star-rating"', 'class="five-star-rating"', out)
    # Morgana printed Liquid errors where image URLs should be -> 404s on every page
    out = re.sub(r'url\(\s*[\'"]?Liquid error[^)]*\)', 'none', out)
    out = re.sub(r',\s*Liquid error[^",]*', '', out)
    out = re.sub(r'(src|srcset|data-src|href)="Liquid error[^"]*"', r'\1=""', out)
    open(p, 'w', encoding='utf-8').write(out)
    print('siteified', name)

for f in sorted(os.listdir(SITE)):
    if f.endswith('.html'):
        process(f)
