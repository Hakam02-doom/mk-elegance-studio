"""Mirror captured Morgana pages into a static local site.
usage: python3 -I mirror.py RAW_PAGES_DIR OUT_DIR
Downloads public CDN assets, rewrites URLs, strips Shopify tracking."""
import os, re, sys, hashlib, urllib.request, urllib.parse, concurrent.futures as cf

RAW, OUT = sys.argv[1], sys.argv[2]
ASSETS = os.path.join(OUT, 'assets')
os.makedirs(ASSETS, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0'}

PAGES = {
    'index.html': 'index.html',
    'collections_all.html': 'services.html',
    'products_vitamin-c-glow-cream.html': 'service.html',
    'pages_about-us.html': 'about.html',
    'pages_contact.html': 'contact.html',
    'pages_faq.html': 'faq.html',
    'blogs_news.html': 'blog.html',
    'blogs_news_blog-10.html': 'article.html',
    'cart.html': 'booking.html',
}
LINKMAP = {
    '/': 'index.html', '/collections/all': 'services.html', '/collections': 'services.html',
    '/pages/about-us': 'about.html', '/pages/contact': 'contact.html', '/pages/faq': 'faq.html',
    '/blogs/news': 'blog.html', '/cart': 'booking.html',
}

ASSET_RE = re.compile(r'''((?:https?:)?//(?:dt-morgana\.myshopify\.com|cdn\.shopify\.com|cdnjs\.cloudflare\.com|unpkg\.com|fonts\.shopifycdn\.com)/[^"'\s)<>,\\]+)''')
cache = {}

def local_name(url):
    u = urllib.parse.urlsplit(url if url.startswith('http') else 'https:' + url)
    path = u.path
    base = os.path.basename(path) or 'file'
    # keep image size params distinct
    q = urllib.parse.parse_qs(u.query)
    stem, ext = os.path.splitext(base)
    tag = ''
    if 'width' in q: tag += '_w' + q['width'][0]
    if 'height' in q: tag += '_h' + q['height'][0]
    if 'crop' in q: tag += '_c' + q['crop'][0]
    m = re.search(r'_(\d+x\d*|x\d+)$', stem)
    h = hashlib.md5(path.encode()).hexdigest()[:6]
    return f'{stem}{tag}-{h}{ext}'

def fetch(url):
    full = url if url.startswith('http') else 'https:' + url
    full = full.replace('&amp;', '&')
    name = local_name(full)
    dest = os.path.join(ASSETS, name)
    if not os.path.exists(dest):
        try:
            req = urllib.request.Request(full, headers=UA)
            data = urllib.request.urlopen(req, timeout=30).read()
        except Exception as e:
            print('FAIL', full, e); return None
        if name.endswith('.css'):
            data = rewrite_css(data.decode('utf-8', 'replace'), full).encode()
        open(dest, 'wb').write(data)
    return name

def rewrite_css(css, base):
    def sub(m):
        raw = m.group(1).strip('\'"')
        if raw.startswith('data:') or raw.startswith('#'): return m.group(0)
        absu = urllib.parse.urljoin(base, raw)
        n = fetch(absu)
        return f'url({n})' if n else m.group(0)
    return re.sub(r'url\(([^)]+)\)', sub, css)

DROP_SCRIPT_PAT = re.compile(r'monorail|web-pixels|webPixelsManager|trekkie|shop-js|preloads\.js|load_feature|origin_trials|standard-actions|countries\.js|shopify-features|ShopifyAnalytics|shopify_common|captcha|boomerang|perf-kit|privacy-banner|consent-tracking|__st=|shop_events_listener|checkout-web', re.I)

def clean(html):
    html = re.sub(r'<script\b[^>]*>.*?</script>', lambda m: '' if DROP_SCRIPT_PAT.search(m.group(0)) else m.group(0), html, flags=re.S)
    html = re.sub(r'<link[^>]+(?:dns-prefetch|preconnect|modulepreload)[^>]*>', '', html)
    html = re.sub(r'<link[^>]+rel="preload"[^>]*as="script"[^>]*>', '', html)
    html = re.sub(r'<div id="shopify-section-cookie-banner".*?</div>\s*</div>\s*</div>', '', html, flags=re.S)
    html = re.sub(r'<shop-cart-sync.*?</shop-cart-sync>', '', html, flags=re.S)
    html = html.replace('(password: buddha)', '')
    return html

def rewrite_links(html):
    def sub(m):
        attr, q, href = m.group(1), m.group(2), m.group(3)
        p = href.split('?')[0].split('#')[0]
        frag = '#' + href.split('#')[1] if '#' in href else ''
        if p in LINKMAP: return f'{attr}={q}{LINKMAP[p]}{frag}{q}'
        if p.startswith('/products/'): return f'{attr}={q}service.html{q}'
        if p.startswith('/collections/'): return f'{attr}={q}services.html{q}'
        if p.startswith('/blogs/news/'): return f'{attr}={q}article.html{q}'
        if p.startswith('/pages/'): return f'{attr}={q}about.html{q}'
        if p.startswith('/account') or p.startswith('/search') or p.startswith('/cart/'): return f'{attr}={q}#{q}'
        return m.group(0)
    html = re.sub(r'(href|action)=(["\'])(/(?!/)[^"\']*)\2', sub, html)
    return html

def process(html):
    html = clean(html)
    urls = set(ASSET_RE.findall(html))
    urls = {u for u in urls if not re.search(r'/(checkouts|services|cart|account)/', u)}
    with cf.ThreadPoolExecutor(16) as ex:
        names = dict(zip(urls, ex.map(fetch, urls)))
    for u in sorted(urls, key=len, reverse=True):
        if names[u]: html = html.replace(u, 'assets/' + names[u])
    html = rewrite_links(html)
    # root-relative shopify cdn paths
    html = re.sub(r'(["\'(])/cdn/', r'\1https://dt-morgana.myshopify.com/cdn/', html)
    return html

for src, dst in PAGES.items():
    p = os.path.join(RAW, src)
    if not os.path.exists(p): continue
    out = process(open(p, encoding='utf-8').read())
    # second pass for root-relative cdn urls introduced above
    out = process(out)
    out = out.replace('</head>', '<link rel="stylesheet" href="assets/mk-brand.css">\n</head>', 1)
    open(os.path.join(OUT, dst), 'w', encoding='utf-8').write(out)
    print('wrote', dst, len(out))
