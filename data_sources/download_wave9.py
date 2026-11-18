# -*- coding: utf-8 -*-
"""
Download Wave 9: Seven Historical Masterpieces & Lexicons
=========================================================
1. in.ernet.dli.2015.345984 - Rajasthani Sabad Kos Part 2-1 (Dr. Sitaram Lalas) (~7.18 MB)
2. in.ernet.dli.2015.347791 - Parmpara Rajasthani Baat-sangrah (Dr. Narayansingh Bhati) (~1.08 MB)
3. in.ernet.dli.2015.307534 - Rajasthani Lokotsav (Gindaram Varma) (~268 KB)
4. in.ernet.dli.2015.538962 - Rajasthani Gadhya-Sahitya Udbhava Aur Vikas (Dr. Shivswaroop Sharma) (~924 KB)
5. in.ernet.dli.2015.445998 - Rajasthani Gadh Vikas Aur Prakash Bhag 1 (Dr. Narendra Bhanawat) (~1.19 MB)
6. in.ernet.dli.2015.550743 - Rajasthani Padh Sangrah (Komal Kothari) (~256 KB)
7. in.ernet.dli.2015.547214 - Hadi Shatak (Kavi Nathusingh Mahiyariya) (~146 KB)
"""

import os
import json
import urllib.request
import urllib.parse
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl._create_unverified_context()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_TEXTS_DIR = os.path.join(BASE_DIR, "data_sources", "raw_texts")
CATALOG_PATH = os.path.join(BASE_DIR, "data_sources", "corpus_catalog.json")

os.makedirs(RAW_TEXTS_DIR, exist_ok=True)

ITEMS = [
    {
        "id": "in.ernet.dli.2015.345984",
        "file": "2015.345984.Rajasthani-Sabad_djvu.txt",
        "target": "in.ernet.dli.2015.345984_sitaram_lalas_rajasthani_sabad_kos_vol2_pt1.txt",
        "title": "Rajasthani Sabad Kos Part-2-1",
        "author": "Dr. Sitaram Lalas",
        "year": "1967",
        "genre": "Authoritative Monumental Lexicon",
        "language": "Rajasthani / Marwari / Dingal"
    },
    {
        "id": "in.ernet.dli.2015.347791",
        "file": "2015.347791.Parmpara-Rajasthani_djvu.txt",
        "target": "in.ernet.dli.2015.347791_parmpara_rajasthani_baat_sangrah.txt",
        "title": "Parmpara Rajasthani Baat-Sangrah",
        "author": "Dr. Narayansingh Bhati",
        "year": "1961",
        "genre": "Traditional Vat Prose & Folk Narratives",
        "language": "Old Rajasthani / Marwari"
    },
    {
        "id": "in.ernet.dli.2015.307534",
        "file": "2015.307534.Rajasthani-Lokotsav_djvu.txt",
        "target": "in.ernet.dli.2015.307534_rajasthani_lokotsav_gindaram_varma.txt",
        "title": "Rajasthani Lokotsav",
        "author": "Gindaram Varma",
        "year": "1963",
        "genre": "Folk Festivals, Rituals & Cultural Customs",
        "language": "Rajasthani / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.538962",
        "file": "2015.538962.Rajasthani--_djvu.txt",
        "target": "in.ernet.dli.2015.538962_rajasthani_gadhya_sahitya_udbhava_vikas.txt",
        "title": "Rajasthani Gadhya-Sahitya Udbhava Aur Vikas",
        "author": "Dr. Shivswaroop Sharma",
        "year": "1972",
        "genre": "Evolution of Rajasthani Prose & Syntax",
        "language": "Rajasthani / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.445998",
        "file": "2015.445998.Rajasthani-Gadh_djvu.txt",
        "target": "in.ernet.dli.2015.445998_rajasthani_gadh_vikas_aur_prakash_pt1.txt",
        "title": "Rajasthani Gadh Vikas Aur Prakash Bhag 1",
        "author": "Dr. Narendra Bhanawat",
        "year": "1969",
        "genre": "Anthology of Literary Prose & Khayats",
        "language": "Rajasthani / Marwari"
    },
    {
        "id": "in.ernet.dli.2015.550743",
        "file": "2015.550743.Rajasthani-Padh_djvu.txt",
        "target": "in.ernet.dli.2015.550743_rajasthani_padh_sangrah_komal_kothari.txt",
        "title": "Rajasthani Padh Sangrah",
        "author": "Komal Kothari",
        "year": "1965",
        "genre": "Traditional Verse, Ballads & Folk Songs",
        "language": "Rajasthani"
    },
    {
        "id": "in.ernet.dli.2015.547214",
        "file": "2015.547214.Hadi-Shatak_djvu.txt",
        "target": "in.ernet.dli.2015.547214_hadi_shatak_nathusingh_mahiyariya.txt",
        "title": "Hadi Shatak",
        "author": "Kavi Nathusingh Mahiyariya",
        "year": "1946",
        "genre": "Heroic Veer-Ras Dingal Poetry",
        "language": "Dingal / Rajasthani"
    }
]

print(f"Starting Wave 9 download of {len(ITEMS)} texts...")

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

for item in ITEMS:
    target_path = os.path.join(RAW_TEXTS_DIR, item["target"])
    if os.path.exists(target_path) and os.path.getsize(target_path) > 10000:
        print(f"Already exists: {item['target']} ({os.path.getsize(target_path)} bytes)")
    else:
        encoded_file = urllib.parse.quote(item["file"])
        url = f"https://archive.org/download/{item['id']}/{encoded_file}"
        print(f"Downloading {item['title']} from {url}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=60) as resp, open(target_path, "wb") as out:
                content = resp.read()
                out.write(content)
            print(f"Successfully downloaded {item['target']} ({len(content)} bytes)")
        except Exception as e:
            print(f"Failed to download {item['target']}: {e}")
            continue

    # Register in catalog
    existing_entry = next((x for x in catalog if x.get("id") == item["id"] or x.get("filename") == item["target"] or x.get("local_name") == item["target"]), None)
    if not existing_entry and os.path.exists(target_path):
        size_bytes = os.path.getsize(target_path)
        catalog_entry = {
            "id": item["id"],
            "title": item["title"],
            "author": item["author"],
            "year": item["year"],
            "language": item["language"],
            "genre": item["genre"],
            "category": item["genre"],
            "filename": item["target"],
            "local_name": item["target"],
            "size_bytes": size_bytes,
            "status": "digitized",
            "source": "Internet Archive (DLI)"
        }
        catalog.append(catalog_entry)
        print(f"Registered {item['title']} in catalog.")

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print("Wave 9 download and catalog registration complete!")
