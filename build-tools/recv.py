import http.server,os,re,sys
OUT=sys.argv[1]
class H(http.server.BaseHTTPRequestHandler):
    def _c(self):
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Headers','*')
        self.send_header('Access-Control-Allow-Private-Network','true')
    def do_OPTIONS(self):
        self.send_response(204);self._c();self.end_headers()
    def do_GET(self):
        self.send_response(200);self.send_header('Content-Type','text/html');self.end_headers()
        self.wfile.write(b'''<html><body>receiver<pre id=l></pre><script>
window.addEventListener('message',async e=>{const r=await fetch('/'+e.data.name,{method:'POST',body:e.data.body});document.getElementById('l').textContent+=e.data.name+' '+r.status+'\\n';e.source.postMessage({ok:e.data.name},'*')});
</script></body></html>''')
    def do_POST(self):
        n=int(self.headers['Content-Length']);d=self.rfile.read(n)
        name=re.sub(r'[^\w.-]','_',self.path.strip('/')) or 'page'
        open(os.path.join(OUT,name),'wb').write(d)
        self.send_response(200);self._c();self.end_headers();self.wfile.write(b'ok')
http.server.HTTPServer(('127.0.0.1',8765),H).serve_forever()
