# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl._create_unverified_context()

test_ids = [
    "in.ernet.dli.2015.95521",
    "in.ernet.dli.2015.308914",
    "in.ernet.dli.2015.536813",
    "in.ernet.dli.2015.347749",
    "in.ernet.dli.2015.443776",
]

for ident in test_ids:
    url = f"https://archive.org/metadata/{ident}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            files = data.get('files', [])
            txt_files = [f['name'] for f in files if f['name'].endswith('_djvu.txt') or f['name'].endswith('.txt')]
            print(f"[{ident}] Title: {data.get('metadata', {}).get('title')} | Txt files: {txt_files}")
    except Exception as e:
        print(f"[{ident}] Error: {e}")
