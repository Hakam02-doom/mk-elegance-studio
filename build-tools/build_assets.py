"""Replace Morgana image files in place with MK Elegance imagery (same filename, same pixel size).
usage: venv/bin/python -I build_assets.py SITE_ASSETS_DIR BACKUP_DIR FONTS_DIR"""
import os, re, sys, shutil, base64, io
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

A, BK, FD = sys.argv[1:4]
MK = os.path.join(A, 'mk')
os.makedirs(BK, exist_ok=True)

GOLD = (176, 138, 82); IVORY = (248, 244, 238); ESP = (43, 30, 20); PARCH = (238, 231, 218); INK = (14, 11, 9)

def mk(name):
    im = Image.open(os.path.join(MK, name + '-1920.webp'))
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA'); bg = Image.new('RGBA', im.size, (*IVORY, 255)); bg.alpha_composite(im); im = bg
    return im.convert('RGB')

def contain(src, size, pad=.1):
    w, h = size
    out = Image.new('RGB', size, IVORY)
    s = min(w * (1 - 2 * pad) / src.width, h * (1 - 2 * pad) / src.height)
    im = src.resize((round(src.width * s), round(src.height * s)), Image.LANCZOS)
    out.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
    return out

def is_product(name):
    return name.startswith(('bushbalm', 'swissmed'))

def font(kind, size):
    return ImageFont.truetype(os.path.join(FD, kind + '.ttf'), size)

# prefix of original asset filename -> MK photo (and optional focal point y 0..1)
PHOTO = {
    # hero slideshow
    'AdobeStock_-2': ('studio-treatment-room', .45), 'AdobeStock_-3': ('facial-massage', .4),
    'AdobeStock_170324582': ('facial-treatment', .4), 'AdobeStock_170324596': ('brows-shaped', .35),
    'AdobeStock_551996209': ('facial-neck-massage', .4), 'img_2x_28379042': ('facial-serum', .5),
    # home sections
    'AdobeStock_170324556': ('facial-treatment', .4), 'AdobeStock_215650556': ('facial-massage', .4),
    'AdobeStock_528423480': ('studio-lounge', .55), 'Untitled-1': ('sqt-products', .5),
    'img6': ('waxing', .5), 'img7': ('brow-tint', .4), 'img8': ('facial-serum', .5), 'img9': ('facial-massage', .4),
    # instagram + newsletter
    'AdobeStock_170324431': ('studio-mirror', .5), 'AdobeStock_260941220': ('studio-lounge', .5),
    'AdobeStock_308411579': ('brows-shaped', .4), 'AdobeStock_406167622': ('facial-neck-massage', .4),
    'AdobeStock_468971730': ('sqt-products', .5), 'newsletter-1': ('studio-treatment-room', .5),
    'AdobeStock_99968874': ('studio-treatment-room', .5),   # welcome popup: photo framed into the left panel
    # about
    'AdobeStock_170324597': ('studio-treatment-room', .45), 'AdobeStock_170324435': ('facial-massage', .4),
    # About 'Inside the Studio' cards: Mital / Client Lounge / Hallway / Treatment Room
    'AdobeStock_502318435': ('facial-neck-massage', .4), 'AdobeStock_468971730_2x_4365d5ee': ('studio-lounge', .55),
    'AdobeStock_308411579_2x_6ff909a7': ('studio-mirror', .5), 'AdobeStock_468969160': ('studio-treatment-room', .45),
    # faq
    'f1': ('facial-treatment', .4), 'f2': ('facial-massage', .4),
    # product page ingredient icons
    'icon01': ('facial-serum', .5), 'icon02': ('sqt-products', .5), 'icon03': ('facial-massage', .4), 'icon04': ('facial-neck-massage', .4),
    # services: unique main / hover per card (no photo repeats across the 13 services)
    'shop-11.png': ('brows-shaped', .3), 'shop-11.1': ('studio-mirror', .5),                       # Eyebrow Threading
    'shop-8.png': ('brow-tint', .4), 'shop-8.1': ('swissmed-eye-lip-serum', .5),                   # Brow Tint
    'shop-9.png': ('facial-treatment', .4), 'shop-9.1': ('swissmed-zero-face-cleanser', .5),       # First-Time Full Face
    'shop-5.png': ('facial-massage', .4), 'shop-5.1': ('swissmed-intense-youth-face-serum', .5),   # Hydra Plump Ritual
    'shop-7.png': ('facial-temple', .3), 'shop-7.1': ('studio-lounge-video-poster', .5),           # Tinted Elegance Brow Duo
    'shop-10.png': ('facial-serum', .35), 'shop-10.1': ('swissmed-bio-lift-cells-cream', .5),      # Customised Facial
    'shop-3.png': ('waxing', .5), 'shop-3.1': ('bushbalm-vajacial-brightening', .5),               # Bikini Wax
    'shop-4.png': ('facial-neck-massage', .4), 'shop-4.1': ('swissmed-collagen-marine-mask', .5),  # Back Facial
    'shop-13.png': ('bushbalm-nude-duo', .5), 'shop-13.1': ('bushbalm-vajacial-hydrating', .5),    # Brazilian Renewal
    'shop-6.png': ('studio-treatment-room', .5), 'shop-6.1': ('bushbalm-bermuda-oil-pro', .5),     # Upper Lip Threading
    'cos10.png': ('bushbalm-watermelon-sugar-duo', .5), 'shop-2.1': ('bushbalm-watermelon-sugar-oil-pro', .5),  # Underarm Wax
    'shop-14.png': ('swissmed-bio-lift-peel', .5), 'shop-14.1': ('studio-lounge', .55),           # Express Glow Facial
    'cos14.png': ('sqt-products', .5), 'shop-1.1': ('bushbalm-vanilla-coconut-duo', .5),          # Hand Facial · Student
}
HERO = {'AdobeStock_-2', 'AdobeStock_-3', 'AdobeStock_170324582', 'AdobeStock_170324596', 'AdobeStock_551996209', 'img_2x_28379042'}

def hero_fade(im):
    w, h = im.size
    im = im.convert('RGBA')
    grad = Image.new('L', (w, 1))
    for x in range(w):
        t = x / w
        a = 240 if t < .3 else max(0, int(240 * (1 - (t - .3) / .35)))
        grad.putpixel((x, 0), a)
    ov = Image.new('RGBA', (w, h), (*IVORY, 255)); ov.putalpha(grad.resize((w, h)))
    im.alpha_composite(ov)
    return im.convert('RGB')

BOTTOM_FADE = {'AdobeStock_528423480', 'Untitled-1'}

def bottom_fade(im):
    w, h = im.size
    im = im.convert('RGBA')
    grad = Image.new('L', (1, h))
    for y in range(h):
        t = y / h
        grad.putpixel((0, y), 0 if t < .35 else min(235, int(235 * (t - .35) / .4)))
    ov = Image.new('RGBA', (w, h), (*IVORY, 255)); ov.putalpha(grad.resize((w, h)))
    im.alpha_composite(ov)
    return im.convert('RGB')

TINT = {'Screenshot_6': GOLD, 'Untitled-2': IVORY}
REVIEW_PHOTO = {'t1': ('brows-shaped', .3), 't2': ('waxing', .5), 't3': ('facial-massage', .35), 't4': ('studio-lounge', .5)}
AVATAR = {'t1': 'K', 't2': 'M', 't3': 'N', 't4': 'E'}
BANNER = {'Minimal_Beauty': ('studio-treatment-room', 'MK Elegance', 'Up to 20% off your first visit', 'BOOK NOW'),
          'Group_182976': ('facial-massage', 'A Welcome Ritual', 'Up to 20% off your first visit', '')}

def match(fname, table):
    base = fname
    for k in sorted(table, key=len, reverse=True):
        if k.endswith('.png'):
            if re.match(re.escape(k[:-4]) + r'(_w\d+)?(_h\d+)?-[0-9a-f]{6}\.png$', base): return k
        elif base.startswith(k) and (len(base) == len(k) or not base[len(k)].isdigit()):
            return k
    return None

def cover(src, size, fy=.5):
    w, h = size
    s = max(w / src.width, h / src.height)
    im = src.resize((max(w, round(src.width * s)), max(h, round(src.height * s))), Image.LANCZOS)
    x = (im.width - w) // 2
    y = int((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))

def save(im, path, orig):
    if path.lower().endswith('.png'):
        im.save(path, 'PNG', optimize=True)
    elif path.lower().endswith('.webp'):
        im.save(path, 'WEBP', quality=85)
    else:
        im.convert('RGB').save(path, 'JPEG', quality=86, optimize=True, progressive=True)

def avatar(size, letter):
    w, h = size
    im = Image.new('RGB', size, PARCH)
    d = ImageDraw.Draw(im)
    f = font('cormorant-garamond-latin-500', int(h * .55))
    d.text((w / 2, h / 2), letter, font=f, fill=GOLD, anchor='mm')
    return im

def banner(size, photo, title, sub, cta):
    w, h = size
    im = cover(mk(photo), size, .45).convert('RGBA')
    ov = Image.new('RGBA', size, (*ESP, 0))
    g = Image.linear_gradient('L').rotate(90).resize(size)
    ov.putalpha(ImageOps.invert(g).point(lambda v: int(v * .78)))
    im.alpha_composite(ov)
    d = ImageDraw.Draw(im)
    pad = int(w * .07)
    tf = font('cormorant-garamond-latin-500', int(h * .13))
    sf = font('montserrat-latin-500', int(h * .045))
    y = int(h * .52)
    d.text((pad, y), title, font=tf, fill=IVORY, anchor='ls')
    d.text((pad, y + int(h * .09)), sub.upper(), font=sf, fill=(234, 217, 190), anchor='ls')
    if cta:
        bx, by = pad, y + int(h * .16)
        bw, bh = int(w * .26), int(h * .1)
        d.rectangle((bx, by, bx + bw, by + bh), fill=GOLD)
        d.text((bx + bw / 2, by + bh / 2), cta, font=sf, fill=IVORY, anchor='mm')
    return im.convert('RGB')

def tint(img, color):
    g = ImageOps.grayscale(img.convert('RGB'))
    lo = tuple(int(c * .82) for c in color)
    hi = tuple(min(255, int(c + (255 - c) * .25)) for c in color)
    return ImageOps.colorize(g, lo, hi)

count = 0
for fname in sorted(os.listdir(A)):
    path = os.path.join(A, fname)
    if not os.path.isfile(path): continue
    if not re.search(r'\.(png|jpe?g|webp)$', fname, re.I): continue
    bk = os.path.join(BK, fname)
    if not os.path.exists(bk): shutil.copy2(path, bk)
    try:
        orig = Image.open(bk)
    except Exception:
        continue
    size = orig.size
    out = None
    k = match(fname, PHOTO)
    if k:
        name, fy = PHOTO[k]
        out = contain(mk(name), size) if is_product(name) else cover(mk(name), size, fy)
        if k == 'AdobeStock_99968874':
            w_, h_ = size; panel = int(w_ * .44)
            out = Image.new('RGB', size, IVORY)
            out.paste(cover(mk(name), (panel, h_), .5), (0, 0))
        if k in BOTTOM_FADE:
            out = bottom_fade(out)
        if k in HERO and size[0] > size[1]:
            out = hero_fade(out)
    elif (k := match(fname, TINT)):
        out = tint(orig, TINT[k])
    elif re.match(r't\d_[0-9a-f]{8}-', fname):
        out = cover(Image.open(os.path.join(MK, 'icon.png')).convert('RGB'), size, .5)
    elif (k := match(fname, AVATAR)) and re.match(r't\d', fname):
        # home testimonials: photo of the service each Google review is about
        name, fy = REVIEW_PHOTO.get(k, ('studio-treatment-room', .5))
        out = cover(mk(name), size, fy)
    elif (k := match(fname, BANNER)):
        out = banner(size, *BANNER[k])
    if out is not None:
        save(out, path, orig); count += 1
print('replaced', count, 'images')

# logos: svg wrappers around MK png
logo = Image.open(os.path.join(MK, 'mk-logo-trimmed.png')).convert('RGBA')
buf = io.BytesIO(); logo.save(buf, 'PNG'); b64 = base64.b64encode(buf.getvalue()).decode()
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
       f'viewBox="0 0 {logo.width} {logo.height}" width="{logo.width}" height="{logo.height}">'
       f'<image width="{logo.width}" height="{logo.height}" href="data:image/png;base64,{b64}"/></svg>')
n = 0
for fname in os.listdir(A):
    if re.match(r'(morgana_1|footer_logo)', fname) and fname.endswith('.svg'):
        open(os.path.join(A, fname), 'w').write(svg); n += 1
print('logos', n)
