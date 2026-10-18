#!/usr/bin/env python3
"""DataForSEO yardımcısı: maliyet korumalı. Kimlik bilgileri yalnızca ortam değişkenlerinden okunur, asla yazdırılmaz.
Kullanım: from dfs import call; call('dataforseo_labs/google/ranked_keywords/live', [{...}], est=0.02, out='x.json')
"""
import os, json, base64, urllib.request, urllib.error, pathlib, sys
CAP = float(os.environ.get('DFS_CAP', '1.35'))   # toplam harcama tavanı (USD)
LEDGER = pathlib.Path(os.environ.get('DFS_LEDGER', 'dfs_ledger.json'))

def _auth():
    t = base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()
    return {'Authorization': 'Basic ' + t, 'Content-Type': 'application/json'}

def spent():
    return sum(e['cost'] for e in json.loads(LEDGER.read_text())) if LEDGER.exists() else 0.0

def call(path, payload, est, out=None):
    if spent() + est > CAP:
        sys.exit(f"STOP: harcama tavanı ({spent():.4f}+{est} > {CAP})")
    req = urllib.request.Request('https://api.dataforseo.com/v3/' + path, data=json.dumps(payload).encode(), headers=_auth())
    try:
        d = json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        d = {'status_code': e.code, 'status_message': e.read()[:200].decode(), 'cost': 0}
    led = json.loads(LEDGER.read_text()) if LEDGER.exists() else []
    led.append({'path': path, 'cost': d.get('cost', 0), 'status': d.get('status_code'), 'msg': d.get('status_message')})
    LEDGER.write_text(json.dumps(led, indent=1))
    if out: pathlib.Path(out).write_text(json.dumps(d))
    t = (d.get('tasks') or [{}])[0]
    print(f"{path}: http/api {d.get('status_code')} task {t.get('status_code')} {t.get('status_message')} cost={d.get('cost')} total={spent():.4f}")
    return d
