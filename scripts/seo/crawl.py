import sys, json, re, subprocess, collections
from bs4 import BeautifulSoup
urls=[u.strip() for u in open(sys.argv[1]) if u.strip()]
rows=[]
for u in urls:
    r=subprocess.run(["curl","-sS","-L","-m","30","-A","Mozilla/5.0","-w","\n%{http_code} %{time_total} %{size_download}",u],capture_output=True,text=True)
    body,_,meta=r.stdout.rpartition("\n"); code,tt,size=meta.split()
    s=BeautifulSoup(body,"lxml")
    g=lambda sel,a=None:(s.select_one(sel).get(a) if a else s.select_one(sel).get_text(" ",strip=True)) if s.select_one(sel) else None
    title=g("title"); md=g('meta[name=description]',"content"); can=g('link[rel=canonical]',"href")
    robots=g('meta[name=robots]',"content")
    h1=[h.get_text(" ",strip=True) for h in s.find_all("h1")]
    text=s.get_text(" ",strip=True); words=len(text.split())
    imgs=s.find_all("img"); noalt=sum(1 for i in imgs if not (i.get("alt") or "").strip())
    types=[]
    for sc in s.find_all("script",type="application/ld+json"):
        try:
            d=json.loads(sc.string or "")
            for n in (d.get("@graph",[d]) if isinstance(d,dict) else d):
                t=n.get("@type"); types+= t if isinstance(t,list) else [t]
        except Exception: types.append("INVALID")
    host=re.sub(r"https?://([^/]+).*",r"\1","https://septicbeacon.com")
    ilinks=len([a for a in s.find_all("a",href=True) if a["href"].startswith("/") or "septicbeacon.com" in a["href"]])
    rows.append(dict(url=u,code=code,time=float(tt),kb=int(size)//1024,title=title,tl=len(title or ""),md=md,ml=len(md or ""),canon=can,robots=robots,h1=h1,h2=len(s.find_all("h2")),words=words,imgs=len(imgs),noalt=noalt,schema=sorted(set(x for x in types if x)),ilinks=ilinks,og=bool(s.select_one('meta[property="og:title"]'))))
json.dump(rows,open(sys.argv[2],"w"),indent=1)
