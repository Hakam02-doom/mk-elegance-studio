import json,sys
a=json.load(open(sys.argv[1]))
t=max(a,key=lambda x:len(x['text']))['text']
i=t.find('"')
dec=json.JSONDecoder()
v,_=dec.raw_decode(t[i:])
if isinstance(v,str):
    open(sys.argv[2],'w').write(v); print('str',len(v))
else:
    json.dump(v,open(sys.argv[2],'w')); print('obj',type(v))
