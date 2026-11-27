"""Apply MK Elegance branding + copy to the pristine Morgana mirror.
usage: python3 -I rebrand.py PRISTINE_DIR SITE_DIR ORIG_ASSETS_DIR"""
import os, re, sys, html, shutil
sys.path.insert(0, os.path.dirname(__file__))
from content import TEXT, SUBSTR, PRODUCTS, ORIG_PRICES, ORIG_BADGE, COLLECTION_ONLY, JANE, IG, FB

PR, SITE, OA = sys.argv[1:4]
ASSETS = os.path.join(SITE, 'assets')

COLOR_SUBS = [
    (r'--color-base-text:\s*0, 0, 0;', '--color-base-text: 43, 30, 20;'),
    (r'--color-base-accent-1:\s*0, 0, 0;', '--color-base-accent-1: 43, 30, 20;'),
    (r'--gradient-base-accent-1:\s*#000000;', '--gradient-base-accent-1: #2b1e14;'),
    (r'241, 239, 225', '248, 244, 238'),
    (r'187, 181, 131', '176, 138, 82'),
    (r'22, 22, 22', '43, 30, 20'),
    (r'(?i)#bbb583', '#b08a52'), (r'(?i)#f1efe1', '#f8f4ee'), (r'(?i)#e2dfce', '#eee7da'),
    (r'(?i)#161616', '#2b1e14'), (r'(?i)#313131', '#2b1e14'), (r'(?i)#231f20', '#0e0b09'),
    (r"'Marcellus', serif", "'Cormorant Garamond', serif"),
    (r"'Lexend Deca', sans-serif", "'Montserrat', sans-serif"),
    (r"'Mr De Haviland', cursive", "'Cormorant Garamond', serif"),
    (r'--font-heading-weight:\s*400', '--font-heading-weight: 500'),
    (r'--font-body-weight:\s*300', '--font-body-weight: 400'),
    (r'--font-additional-heading-style:\s*normal', '--font-additional-heading-style: italic'),
    (r'font-family:\s*Outfit', 'font-family: Montserrat'),
    (r'text-transform:\s*capitalize', 'text-transform:none'),
]
FONT_FACE = """@font-face{font-family:'Cormorant Garamond';src:url(assets/mk/cormorant-garamond-latin.woff2) format('woff2');font-weight:300 700;font-style:normal;font-display:swap}
@font-face{font-family:'Cormorant Garamond';src:url(assets/mk/cormorant-garamond-italic-latin.woff2) format('woff2');font-weight:300 700;font-style:italic;font-display:swap}
@font-face{font-family:'Montserrat';src:url(assets/mk/montserrat-latin.woff2) format('woff2');font-weight:100 900;font-style:normal;font-display:swap}"""

def norm(s):
    return ' '.join(html.unescape(s).split())

TOK = re.compile(r'(<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->|<[^>]+>)', re.S | re.I)
NAMES = sorted(PRODUCTS, key=len, reverse=True)

def esc(s):
    return html.escape(s, quote=False)

def rewrite_attr_names(tag):
    # product names inside alt/title/aria-label attributes
    def sub(m):
        v = html.unescape(m.group(3))
        for n in NAMES:
            if n in v:
                v = v.replace(n, PRODUCTS[n][0])
        return f'{m.group(1)}={m.group(2)}{html.escape(v)}{m.group(2)}'
    return re.sub(r'\b(alt|title|aria-label|placeholder)=(["\'])(.*?)\2', sub, tag)

def process_page(src, name):
    h = open(src, encoding='utf-8').read()
    for a, b in COLOR_SUBS:
        h = re.sub(a, b, h)
    h = re.sub(r"@import url\('https://fonts\.googleapis\.com[^']*'\);", '', h)
    h = h.replace('</head>', f'<style>{FONT_FACE}</style>\n</head>', 1)
    # favicon
    h = re.sub(r'(<link rel="icon"[^>]*href=")[^"]*(")', r'\1assets/mk/icon.png\2', h)
    if 'rel="icon"' not in h:
        h = h.replace('</head>', '<link rel="icon" type="image/png" href="assets/mk/icon.png">\n</head>', 1)

    toks = TOK.split(h)
    current = None
    last_a = None
    out = []
    for t in toks:
        if not t:
            continue
        if t.startswith('<'):
            low = t[:8].lower()
            if low.startswith('<script') or low.startswith('<style') or t.startswith('<!--'):
                out.append(t); continue
            m = re.search(r'\balt=(["\'])(.*?)\1', t)
            if m:
                v = html.unescape(m.group(2))
                if v in PRODUCTS: current = v
            t = rewrite_attr_names(t)
            if re.match(r'<a\b', t, re.I):
                last_a = len(out)
            out.append(t); continue
        # text token
        n = norm(t)
        if not n:
            out.append(t); continue
        lead = t[:len(t) - len(t.lstrip())]; trail = t[len(t.rstrip()):]
        new = None
        if n in PRODUCTS:
            current = n
            new = PRODUCTS[n][0]
        elif current in ORIG_PRICES and n in ORIG_PRICES[current]:
            op, oc = ORIG_PRICES[current]
            _, np_, nc, _ = PRODUCTS[current]
            new = np_ if n == op else (nc or np_)
        elif name == 'services.html' and n in COLLECTION_ONLY:
            new = COLLECTION_ONLY[n]
        elif n in TEXT:
            new = TEXT[n]
        if new is None and current in ORIG_BADGE and ORIG_BADGE[current] in n and re.fullmatch(r'(OFF\s*)?\d+%(\s*OFF)?', n):
            new = n.replace(ORIG_BADGE[current], PRODUCTS[current][3])
        if new is None:
            s = n; changed = False
            for a, b in SUBSTR:
                if a in s:
                    s = s.replace(a, b); changed = True
            for pn in NAMES:
                if pn in s:
                    s = s.replace(pn, PRODUCTS[pn][0]); changed = True
            if changed: new = s
        if new is not None:
            out.append(lead + esc(new) + trail)
            if new.lower().startswith('book') and last_a is not None and len(out) - last_a <= 6:
                out[last_a] = re.sub(r'href=(["\'])[^"\']*\1', f'href="{JANE}" target="_blank" rel="noopener"', out[last_a], count=1)
        else:
            out.append(t)
    h = ''.join(out)

    # social links
    h = re.sub(r'href="https?://(?:www\.)?(?:twitter|x)\.com[^"]*"', f'href="{IG}"', h)
    h = re.sub(r'href="https?://(?:www\.)?youtube\.com[^"]*"', f'href="{IG}"', h)
    h = re.sub(r'href="https?://(?:www\.)?instagram\.com[^"]*"', f'href="{IG}"', h)
    h = re.sub(r'href="https?://(?:www\.)?facebook\.com[^"]*"', f'href="{FB}"', h)
    # checkout -> Jane
    h = re.sub(r'(<button[^>]*name="checkout")', r'\1 onclick="window.open(\'' + JANE + r'\');return false;"', h)
    # contact map -> studio address
    h = re.sub(r'src="https://maps\.google\.co\.in/[^"]*output=embed"', 'src="https://maps.google.com/maps?q=116+King+St+S,+Waterloo,+ON+N2J+1P5&z=16&output=embed" title="MK Elegance Studio, 116 King St S, Waterloo" loading="lazy"', h, flags=re.S)
    # page <title>
    h = re.sub(r'<title>\s*([^<]*?)\s*</title>', lambda m: '<title>' + esc(TEXT.get(norm(m.group(1)), norm(m.group(1)).replace('dt-morgana', 'MK Elegance Studio'))) + '</title>', h, count=1)
    if name == 'index.html':
        h = re.sub(r'<title>[^<]*</title>', '<title>Threading, Waxing &amp; Facials, Waterloo | MK Elegance Studio</title>', h, count=1)
    h = h.replace('dt-morgana', 'MK Elegance Studio')
    return h

# CSS assets: restore from backup, then recolour
os.makedirs(os.path.join(OA, 'css'), exist_ok=True)
for f in os.listdir(ASSETS):
    if not f.endswith('.css') or f == 'mk-brand.css':
        continue
    p = os.path.join(ASSETS, f); b = os.path.join(OA, 'css', f)
    if not os.path.exists(b): shutil.copy2(p, b)
    css = open(b, encoding='utf-8', errors='replace').read()
    for a, c in COLOR_SUBS:
        css = re.sub(a, c, css)
    open(p, 'w', encoding='utf-8').write(css)

for f in sorted(os.listdir(PR)):
    if f.endswith('.html'):
        open(os.path.join(SITE, f), 'w', encoding='utf-8').write(process_page(os.path.join(PR, f), f))
        print('built', f)
