# -*- coding: utf-8 -*-
"""
Download Wave 5: Five Supreme Historical Masterpieces of Rajasthani Literature
=============================================================================
1. Dhola Maru Ra Dhoha - Dr. Bhagwati Lal (in.ernet.dli.2015.348199)
2. Veli Krisan Rukmani Ri - Rathore Prithviraj / Swami Narottamdas (in.ernet.dli.2015.545356)
3. Rajasthani Lok Sahitya Adhyan Ke Aayam - Dr. Ramprasad Dadhich (in.ernet.dli.2015.443965)
4. Rajasthani Lok Sahitya Ki Saidhanti Vivechna - Sohandan Charan (in.ernet.dli.2015.443912)
5. Kanhadade Prabandha Vol 1 - Kavi Padmanabha (in.ernet.dli.2015.314052)
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
        "id": "RAJ-BOK-020",
        "archive_id": "in.ernet.dli.2015.348199",
        "title": "Dhola Maru Ra Dhoha",
        "author": "Dr. Bhagwati Lal Rajpurohit",
        "year": 1960,
        "category": "Folk Ballad, Medieval Romance & Dohas"
    },
    {
        "id": "RAJ-BOK-021",
        "archive_id": "in.ernet.dli.2015.545356",
        "title": "Veli Krisan Rukmani Ri",
        "author": "Rathore Raja Prithviraj / Swami Narottamdas",
        "year": 1953,
        "category": "Classical Dingal Epic & Devotional Poetry"
    },
    {
        "id": "RAJ-BOK-022",
        "archive_id": "in.ernet.dli.2015.443965",
        "title": "Rajasthani Lok Sahitya Adhyan Ke Aayam",
        "author": "Dr. Ramprasad Dadhich",
        "year": 1984,
        "category": "Folklore, Ethnography & Folk Song Analysis"
    },
    {
        "id": "RAJ-BOK-023",
        "archive_id": "in.ernet.dli.2015.443912",
        "title": "Rajasthani Lok Sahitya Ki Saidhanti Vivechna",
        "author": "Sohandan Charan",
        "year": 1978,
        "category": "Theoretical Folk Poetics & Charani Traditions"
    },
    {
        "id": "RAJ-BOK-024",
        "archive_id": "in.ernet.dli.2015.314052",
        "title": "Kanhadade Prabandha Vol-1",
        "author": "Kavi Padmanabha / Prof. Kanti Lal Vyas",
        "year": 1953,
        "category": "Medieval Heroic Chronicle & Early Western Rajasthani"
    }
]

print("=== Starting Wave 5 Supreme Literary Downloads ===")
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
                print(f"No text file found for {ident}")
    except Exception as e:
        print(f"Failed processing {ident}: {e}")

# Update catalog
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
