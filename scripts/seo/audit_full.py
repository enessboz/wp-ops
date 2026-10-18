import json,re,glob,subprocess,sys,concurrent.futures as cf,collections
from bs4 import BeautifulSoup
SC='/home/user/agricidaniel/claude-seo/scripts'; PY=sys.executable
posts=json.load(open('posts_full.json')); P={x['link']:x for x in posts}
pages={x['link']:x for x in json.load(open('pages.json'))}
urls=list(P)+list(pages)
def fname(u): return 'html3/'+re.sub(r'/','_',u.replace('https://septicbeacon.com',''))+'.html'
def head(u):
    r=subprocess.run(['curl','-sSI','-m','20',u],capture_output=True,text=True).stdout
    m=re.search(r'(?im)^content-length:\s*(\d+)',r); return u,int(m.group(1)) if m else None
rows=[];imgs=set()
for u in urls:
    h=open(fname(u),errors='ignore').read(); s=BeautifulSoup(h,'lxml')
    art=s.select_one('article') or s
    title=s.title.get_text(strip=True) if s.title else ''
    md=(s.select_one('meta[name=description]') or {}).get('content','')
    text=art.get_text(' ',strip=True); words=len(text.split())
    hs=[int(x.name[1]) for x in art.find_all(re.compile('^h[1-6]$'))]
    skips=sum(1 for a,b in zip(hs,hs[1:]) if b-a>1)
    il=[a for a in art.find_all('a',href=True) if a['href'].startswith('/') or 'septicbeacon.com' in a['href']]
    el=[a for a in art.find_all('a',href=True) if a['href'].startswith('http') and 'septicbeacon' not in a['href']]
    im=art.find_all('img'); 
    for i in im:
        if i.get('src'): imgs.add(i['src'])
    sch=[]
    for sc in s.find_all('script',type='application/ld+json'):
        try:
            d=json.loads(sc.string or ''); 
            for n in (d.get('@graph',[d]) if isinstance(d,dict) else d):
                t=n.get('@type'); sch+= t if isinstance(t,list) else [t]
        except Exception: sch.append('INVALID')
    tm=json.loads(subprocess.run([PY,SC+'/metadata_template.py','--title',title,'--description',md,'--json'],capture_output=True,text=True).stdout)['pages'][0]
    cq=json.loads(subprocess.run([PY,SC+'/content_quality.py','--json','--threshold','0',fname(u)],capture_output=True,text=True).stdout)
    low=text.lower()
    meta=P[u]['meta'] if u in P else {}
    rows.append(dict(url=u,slug=u.rstrip('/').split('/')[-1],is_post=u in P,title=title,tl=len(title),md=md,ml=len(md),fk=meta.get('rank_math_focus_keyword',''),
      h1=len(art.find_all('h1')) or len(s.find_all('h1')),h2=len(art.find_all('h2')),skips=skips,words=words,il=len(il),el=len(el),
      ilpk=round(len(il)/max(words,1)*1000,1),imgs=len(im),noalt=sum(1 for i in im if not (i.get('alt') or '').strip()),nodim=sum(1 for i in im if not (i.get('width') and i.get('height'))),
      og=bool(s.select_one('meta[property="og:title"]')),tw=bool(s.select_one('meta[name="twitter:card"]')),schema=sorted(set(x for x in sch if x)),
      sources=('sources and further reading' in low or 'sources' in low and len(el)>=3),faq=('frequently asked' in low),
      byline=bool(re.search(r'written by|reviewed by|by sepic?tic',low)),date_vis=bool(re.search(r'updated|published',low)),
      mod=(P[u]['modified'][:10] if u in P else None),pub=(P[u]['date'][:10] if u in P else None),
      tmpl=tm['severity'],tflags=tm['flags'],cq=cq['overall_quality'],cqflags=cq['flags'],imgsrc=[i.get('src') for i in im if i.get('src')]))
with cf.ThreadPoolExecutor(8) as ex: sizes=dict(ex.map(head,sorted(imgs)))
for r in rows:
    r['imgbig']=[(u.split('/')[-1],sizes.get(u)) for u in r['imgsrc'] if (sizes.get(u) or 0)>200000]
    r['imgfmt']=collections.Counter(u.rsplit('.',1)[-1].lower() for u in r['imgsrc'])
    del r['imgsrc']
json.dump(rows,open('audit_full.json','w'),indent=1,default=dict)
print('done',len(rows),'images',len(imgs))
