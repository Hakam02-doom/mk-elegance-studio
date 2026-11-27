import sys,re,html
s=open(sys.argv[1]).read()
s=re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',s,flags=re.S)
m=re.search(r'<main.*?</main>',s,flags=re.S); s=m.group(0) if m else s
t=re.sub(r'<(h[1-6])[^>]*>','\n## ',s); t=re.sub(r'<[^>]+>','\n',t); t=html.unescape(t)
out=[];
for l in t.split('\n'):
    l=' '.join(l.split())
    if l and (not out or out[-1]!=l): out.append(l)
print('\n'.join(out)[:int(sys.argv[2])])
