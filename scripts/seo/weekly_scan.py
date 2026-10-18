#!/usr/bin/env python3
"""Haftalık canlı site taraması: sitemap URL'leri için durum, title/meta uzunluğu, H1, canonical, noindex, iç link sayısı.
Kullanım: python3 scripts/seo/weekly_scan.py > rapor.md   (bağımlılık: beautifulsoup4 lxml; curl proxy üzerinden çalışır)"""
import re, subprocess, sys, collections, concurrent.futures as cf
from bs4 import BeautifulSoup
BASE = "https://septicbeacon.com"
def curl(u, head=False):
    a = ["curl", "-s", "-m", "30", "-A", "Mozilla/5.0", "-w", "\n%{http_code}"]
    r = subprocess.run(a + [u], capture_output=True, text=True).stdout
    body, _, code = r.rpartition("\n"); return code.strip(), body
def locs(u): return re.findall(r"<loc>([^<]+)</loc>", curl(u)[1])
idx = locs(BASE + "/sitemap_index.xml"); urls = []
for s in idx: urls += locs(s)
urls = sorted(set(urls))
def scan(u):
    c, h = curl(u); s = BeautifulSoup(h, "lxml")
    t = s.title.get_text(strip=True) if s.title else ""
    d = (s.select_one("meta[name=description]") or {}).get("content", "")
    can = (s.select_one("link[rel=canonical]") or {}).get("href", "")
    rb = (s.select_one("meta[name=robots]") or {}).get("content", "")
    art = s.select_one("article") or s
    il = {a["href"].split("#")[0].rstrip("/") for a in art.find_all("a", href=True) if a["href"].startswith("/") or BASE in a["href"]}
    return dict(url=u, code=c, tl=len(t), ml=len(d), h1=len(s.find_all("h1")), canon=can.rstrip("/") == u.rstrip("/"), noindex="noindex" in rb, il=il)
with cf.ThreadPoolExecutor(6) as ex: rows = list(ex.map(scan, urls))
inb = collections.Counter()
for r in rows:
    for l in r["il"]:
        l = l if l.startswith("http") else BASE + l
        if l.rstrip("/") != r["url"].rstrip("/"): inb[l.rstrip("/")] += 1
sl = lambda r: r["url"].replace(BASE, "")
print(f"# Haftalık tarama\n\nSitemap URL: {len(urls)} ({', '.join(i.rsplit('/',1)[-1] for i in idx)})\n")
print("- durum ≠ 200:", [(sl(r), r["code"]) for r in rows if r["code"] != "200"])
print("- title >65:", [(sl(r), r["tl"]) for r in rows if r["tl"] > 65])
print("- meta >160 veya <70:", [(sl(r), r["ml"]) for r in rows if r["ml"] > 160 or r["ml"] < 70])
print("- H1 ≠ 1:", [(sl(r), r["h1"]) for r in rows if r["h1"] != 1])
print("- canonical kendisi değil:", [sl(r) for r in rows if not r["canon"]])
print("- noindex:", [sl(r) for r in rows if r["noindex"]])
low = sorted((inb[r["url"].rstrip("/")], sl(r)) for r in rows if "/category/" not in r["url"] and r["url"].rstrip("/") != BASE)
print("- en az gelen iç link (ilk 5):", low[:5])
