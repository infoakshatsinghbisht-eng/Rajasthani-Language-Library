# -*- coding: utf-8 -*-
"""
Download Wave 4: Foundational Rajasthani Literature, Story & Poetry Collections
=============================================================================
1. Veer Satsai - Mahakavi Suryamal Misran (in.ernet.dli.2015.380463)
2. Rajasthani Vat Sahitya - Dr. Poonam Daiya (in.ernet.dli.2015.308096)
3. Rajasthani Kahani Sangrah [Jaagati Jot] - Ramesh Dayal (in.ernet.dli.2015.444365)
4. Rajasthani Nibandh Sangrah - Manohar Sharma (in.ernet.dli.2015.444198)
5. Duvidha Aur Anya Kahaniya - Vijaydan Detha (cFZz_duvidha...)
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

TARGETS = [
    {
        "id": "RAJ-BOK-016",
        "archive_id": "in.ernet.dli.2015.380463",
        "title": "Veer Satsai",
        "author": "Mahakavi Suryamal Misran",
        "year": 1857,
        "category": "Classical Heroic Dingal Poetry"
    },
    {
        "id": "RAJ-BOK-017",
        "archive_id": "in.ernet.dli.2015.308096",
        "title": "Rajasthani Vat Sahitya",
        "author": "Dr. Poonam Daiya",
        "year": 1965,
        "category": "Historical Vats & Folk Chronicles"
    },
    {
        "id": "RAJ-BOK-018",
        "archive_id": "in.ernet.dli.2015.444365",
        "title": "Rajasthani Kahani Sangrah [Jaagati Jot]",
        "author": "Ramesh Dayal",
        "year": 1974,
        "category": "Modern Rajasthani Short Stories"
    },
    {
        "id": "RAJ-BOK-019",
        "archive_id": "in.ernet.dli.2015.444198",
        "title": "Rajasthani Nibandh",
        "author": "Manohar Sharma",
        "year": 1970,
        "category": "Essays & Literary Criticism"
    },
]

print("=== Starting Wave 4 Literary & Folklore Downloads ===")
downloaded = []

for target in TARGETS:
    ident = target["archive_id"]
    try:
        files_url = f"https://archive.org/metadata/{ident}/files"
        req = urllib.request.Request(files_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
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
                local_name = f"{ident}_{txt_file}"
                out_path = os.path.join(RAW_DIR, local_name)
                target["local_name"] = local_name
                target["file_name"] = txt_file

                if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
                    print(f"Already exists: {local_name} ({os.path.getsize(out_path)} bytes)")
                    target["size_kb"] = round(os.path.getsize(out_path) / 1024, 1)
                    downloaded.append(target)
                    continue

                dl_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(txt_file)}"
                print(f"Downloading {target['title']} from {dl_url}...")
                req_dl = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req_dl, context=ctx, timeout=60) as dl_resp:
                    content = dl_resp.read()
                    if len(content) > 1000:
                        with open(out_path, "wb") as out_f:
                            out_f.write(content)
                        print(f"Successfully saved: {local_name} ({len(content)} bytes)")
                        target["size_kb"] = round(len(content) / 1024, 1)
                        downloaded.append(target)
            else:
                print(f"No text transcript found for {ident}")
    except Exception as e:
        print(f"Failed processing {ident}: {e}")

# Update corpus catalog
cat_path = os.path.join(os.path.dirname(__file__), "corpus_catalog.json")
with open(cat_path, "r", encoding="utf-8") as f:
    cat = json.load(f)

existing_ids = {c["id"] for c in cat}
for d in downloaded:
    if d["id"] not in existing_ids:
        cat.append(d)

with open(cat_path, "w", encoding="utf-8") as f:
    json.dump(cat, f, ensure_ascii=False, indent=2)

print(f"\nCorpus catalog updated! Total cataloged texts: {len(cat)}")
