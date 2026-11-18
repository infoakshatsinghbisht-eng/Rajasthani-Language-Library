# -*- coding: utf-8 -*-
"""
Download Wave 6 Texts from Internet Archive
===========================================
Monumental Additions:
1. in.ernet.dli.2015.345971 - Rajasthani Sabad Kos Part-2-2 (Sitaram Lalas) (~6.04 MB)
2. in.ernet.dli.2015.348143 - Rajasthani Shabdkosh Vol-IV (Dr. Sitaram Lalas) (~8.67 MB)
3. in.ernet.dli.2015.539046 - Dingal Me Veer Ras (Motilal Menariya) (~622 KB)
4. in.ernet.dli.2015.345924 - Prakrit Aur Apbransh Ka Dingal Sahitya Par Prabhav (Dr. Govardhan Sharma) (~1.63 MB)
5. in.ernet.dli.2015.347988 - Rajasthani Sahitya Kosh Chad Saster (Dr. Narayansingh Bhati) (~1.12 MB)
6. in.ernet.dli.2015.444415 - Marwari Vyapari (Giriraj Shankar Sharma) (~1.23 MB)
"""

import os
import json
import urllib.request
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
        "id": "in.ernet.dli.2015.345971",
        "file": "2015.345971.Rajasthani-Sabad_djvu.txt",
        "target": "in.ernet.dli.2015.345971_sitaram_lalas_rajasthani_sabad_kos_vol2.txt",
        "title": "Rajasthani Sabad Kos (Part 2-2)",
        "author": "Sitaram Lalas",
        "year": "1967",
        "genre": "Lexicography / Etymology / Comprehensive Dictionary",
        "language": "Rajasthani / Marwari / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.348143",
        "file": "2015.348143.Rajasthani-Shabdkoshvol-iv_djvu.txt",
        "target": "in.ernet.dli.2015.348143_sitaram_lalas_rajasthani_shabdkosh_vol4.txt",
        "title": "Rajasthani Shabdkosh (Vol IV)",
        "author": "Dr. Sitaram Lalas",
        "year": "1978",
        "genre": "Lexicography / Comprehensive Dictionary & Etymology",
        "language": "Rajasthani / Dingal / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.539046",
        "file": "2015.539046.Dingal-Me_djvu.txt",
        "target": "in.ernet.dli.2015.539046_dingal_me_veer_ras.txt",
        "title": "Dingal Me Veer Ras",
        "author": "Motilal Menariya",
        "year": "1958",
        "genre": "Heroic Poetry & Critical Analysis",
        "language": "Dingal / Rajasthani / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.345924",
        "file": "2015.345924.Prakrit-Aur_djvu.txt",
        "target": "in.ernet.dli.2015.345924_prakrit_apbransh_dingal_prabhav.txt",
        "title": "Prakrit Aur Apbransh Ka Dingal Sahitya Par Prabhav",
        "author": "Dr. Govardhan Sharma",
        "year": "1965",
        "genre": "Linguistic Evolution & Philology",
        "language": "Apabhramsha / Dingal / Rajasthani"
    },
    {
        "id": "in.ernet.dli.2015.347988",
        "file": "2015.347988.Rajasthani-Sahitya_djvu.txt",
        "target": "in.ernet.dli.2015.347988_rajasthani_sahitya_kosh_chand.txt",
        "title": "Rajasthani Sahitya Kosh (Chhand Shastra)",
        "author": "Dr. Narayansingh Bhati",
        "year": "1972",
        "genre": "Prosody, Metrics & Chhand Treatise",
        "language": "Dingal / Rajasthani"
    },
    {
        "id": "in.ernet.dli.2015.444415",
        "file": "2015.444415.Marwari-Vyapari_djvu.txt",
        "target": "in.ernet.dli.2015.444415_marwari_vyapari.txt",
        "title": "Marwari Vyapari",
        "author": "Giriraj Shankar Sharma",
        "year": "1963",
        "genre": "Socio-economic History & Trade Terminology",
        "language": "Marwari / Rajasthani / Hindi"
    }
]

print(f"Starting Wave 6 download of {len(ITEMS)} texts...")

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

for item in ITEMS:
    target_path = os.path.join(RAW_TEXTS_DIR, item["target"])
    if os.path.exists(target_path) and os.path.getsize(target_path) > 10000:
        print(f"Already exists: {item['target']} ({os.path.getsize(target_path)} bytes)")
    else:
        url = f"https://archive.org/download/{item['id']}/{item['file']}"
        print(f"Downloading {item['title']} from {url}...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, context=ctx, timeout=120) as resp, open(target_path, "wb") as out:
                content = resp.read()
                out.write(content)
            print(f"Downloaded successfully: {item['target']} ({len(content)} bytes)")
        except Exception as e:
            print(f"Failed to download {item['id']}: {e}")
            continue

    # Register in catalog if not present
    existing_entry = next((c for c in catalog if c.get("filename") == item["target"]), None)
    if not existing_entry:
        file_size = os.path.getsize(target_path) if os.path.exists(target_path) else 0
        catalog.append({
            "filename": item["target"],
            "title": item["title"],
            "author": item["author"],
            "year": item["year"],
            "genre": item["genre"],
            "language": item["language"],
            "source": f"Internet Archive ({item['id']})",
            "size_bytes": file_size
        })

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Wave 6 download and catalog update complete. Total catalog entries: {len(catalog)}")
