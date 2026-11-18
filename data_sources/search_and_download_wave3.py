# -*- coding: utf-8 -*-
"""
Search Archive.org for additional Rajasthani literature, folklore, vats, and grammar.
Check file manifests and download full texts.
"""

import urllib.request
import urllib.parse
import json
import ssl
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl._create_unverified_context()

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_texts")
os.makedirs(RAW_DIR, exist_ok=True)

queries = [
    'title:("rajasthani bhasha")',
    'title:("rajasthani lok")',
    'title:("marwari")',
    'title:("dingal")',
    'title:("veer satsai")',
    'title:("dhola maru")',
    'title:("tessitori") AND rajasthani',
    'title:("rajasthani nibandh")'
]

items = {}
for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl=identifier,title,creator,year,mediatype,description&rows=15&page=1&output=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            docs = data.get('response', {}).get('docs', [])
            for d in docs:
                if d.get('mediatype') == 'texts':
                    items[d['identifier']] = d
    except Exception as e:
        print(f"Query error for {q}: {e}")

print(f"Total discovered text items: {len(items)}")

# Check metadata files for each to find _djvu.txt
downloaded_count = 0
for ident, meta in list(items.items())[:25]:
    try:
        files_url = f"https://archive.org/metadata/{ident}/files"
        req = urllib.request.Request(files_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            fdata = json.loads(resp.read().decode('utf-8'))
            files = fdata.get('result', [])
            txt_file = None
            for f in files:
                fname = f.get('name', '')
                if fname.endswith('_djvu.txt'):
                    txt_file = fname
                    break
            if not txt_file:
                for f in files:
                    fname = f.get('name', '')
                    if fname.endswith('.txt') and not fname.endswith('_meta.txt'):
                        txt_file = fname
                        break
            
            if txt_file:
                print(f"Found text file for {ident}: {txt_file} (title: {meta.get('title')})")
                out_path = os.path.join(RAW_DIR, f"{ident}_{txt_file}")
                if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
                    print(f"  -> Already exists: {os.path.basename(out_path)}")
                    continue
                
                dl_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(txt_file)}"
                req_dl = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req_dl, context=ctx, timeout=30) as dl_resp:
                    content = dl_resp.read()
                    if len(content) > 1000:
                        with open(out_path, "wb") as out_f:
                            out_f.write(content)
                        print(f"  -> Downloaded: {os.path.basename(out_path)} ({len(content)} bytes)")
                        downloaded_count += 1
                        if downloaded_count >= 5:
                            break
    except Exception as e:
        print(f"Error inspecting/downloading {ident}: {e}")

print(f"Wave 3 downloads finished. Downloaded: {downloaded_count}")
