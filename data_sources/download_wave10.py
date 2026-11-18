# -*- coding: utf-8 -*-
"""
Download Wave 10: Seven Rare Folklore & Classical Prose Masterpieces
===================================================================
1. in.ernet.dli.2015.464090 - A Dictionary Of Rajasthani Proverbs (Bijaydan Detha "Biji") (~2.01 MB)
2. in.ernet.dli.2015.309699 - Rajasthani Vratkathae (Mohanlal Purohit) (~1.04 MB)
3. in.ernet.dli.2015.443973 - Rajasthani Sanskrati Ra Chitram (Jahur Khan Mehar) (~590 KB)
4. in.ernet.dli.2015.444852 - Dalpat Vilas (Rawat Saraswat) (~544 KB)
5. in.ernet.dli.2015.514940 - Rajasthani Vachnikaye (Dr. Aalam Shaha Ravan) (~495 KB)
6. in.ernet.dli.2015.442351 - Parampra - Mataji Ri Vachnika (Jaychandra Jati) (~477 KB)
7. in.ernet.dli.2015.401029 - Rajasthani Bheel Geet Bhag-2 (Giridhar Sharma) (~331 KB)
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
        "id": "in.ernet.dli.2015.464090",
        "file": "2015.464090.A-Dictionary_djvu.txt",
        "target": "in.ernet.dli.2015.464090_detha_dictionary_rajasthani_proverbs.txt",
        "title": "A Dictionary Of Rajasthani Proverbs",
        "author": "Bijaydan Detha (Biji)",
        "year": "1976",
        "genre": "Authoritative Monumental Dictionary of Proverbs & Idioms",
        "language": "Rajasthani / Marwari / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.309699",
        "file": "2015.309699.Rajasthani-Vratkathae_djvu.txt",
        "target": "in.ernet.dli.2015.309699_rajasthani_vratkathae_purohit.txt",
        "title": "Rajasthani Vratkathae",
        "author": "Mohanlal Purohit",
        "year": "1960",
        "genre": "Traditional Religious Vows, Fasts & Sacred Folk Stories",
        "language": "Rajasthani / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.443973",
        "file": "2015.443973.Rajasthani-Sanskrati_djvu.txt",
        "target": "in.ernet.dli.2015.443973_rajasthani_sanskrati_ra_chitram_mehar.txt",
        "title": "Rajasthani Sanskrati Ra Chitram",
        "author": "Jahur Khan Mehar",
        "year": "1981",
        "genre": "Vibrant Portrayals of Rajasthani Culture & Desert Heritage",
        "language": "Rajasthani"
    },
    {
        "id": "in.ernet.dli.2015.444852",
        "file": "2015.444852.Dalpat-Vilas_djvu.txt",
        "target": "in.ernet.dli.2015.444852_dalpat_vilas_rawat_saraswat.txt",
        "title": "Dalpat Vilas",
        "author": "Rawat Saraswat (Ed.)",
        "year": "1960",
        "genre": "16th-Century Historical Bikaner Court Prose & Khyat",
        "language": "Old Rajasthani / Marwari"
    },
    {
        "id": "in.ernet.dli.2015.514940",
        "file": "2015.514940.Rajasthani-Vachnikaye_djvu.txt",
        "target": "in.ernet.dli.2015.514940_rajasthani_vachnikaye_ravan.txt",
        "title": "Rajasthani Vachnikaye",
        "author": "Dr. Aalam Shaha Ravan",
        "year": "1979",
        "genre": "Philological Anthology of Martial Rhymed Prose (Vachnika)",
        "language": "Dingal / Rajasthani"
    },
    {
        "id": "in.ernet.dli.2015.442351",
        "file": "2015.442351.Parampra-Mataji-Ri_djvu.txt",
        "target": "in.ernet.dli.2015.442351_parampra_mataji_ri_vachnika.txt",
        "title": "Parampra: Mataji Ri Vachnika",
        "author": "Jaychandra Jati",
        "year": "1964",
        "genre": "Devotional & Historical Vachnika Prose",
        "language": "Old Rajasthani / Dingal"
    },
    {
        "id": "in.ernet.dli.2015.401029",
        "file": "2015.401029.Rajasthani-Bheel_djvu.txt",
        "target": "in.ernet.dli.2015.401029_rajasthani_bheel_geet_pt2_sharma.txt",
        "title": "Rajasthani Bheel Geet (Part 2)",
        "author": "Giridhar Sharma",
        "year": "1956",
        "genre": "Tribal Folk Ballads, Songs & Southern Dialect Lore",
        "language": "Bhilodi / Wagdi / Rajasthani"
    }
]

print(f"Starting Wave 10 download of {len(ITEMS)} texts...", flush=True)

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

for item in ITEMS:
    target_path = os.path.join(RAW_TEXTS_DIR, item["target"])
    if os.path.exists(target_path) and os.path.getsize(target_path) > 10000:
        print(f"Already exists: {item['target']} ({os.path.getsize(target_path)} bytes)", flush=True)
    else:
        encoded_file = urllib.parse.quote(item["file"])
        url = f"https://archive.org/download/{item['id']}/{encoded_file}"
        print(f"Downloading {item['title']} from {url}...", flush=True)
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=60) as resp, open(target_path, "wb") as out:
                content = resp.read()
                out.write(content)
            print(f"Successfully downloaded {item['target']} ({len(content)} bytes)", flush=True)
        except Exception as e:
            print(f"Failed to download {item['target']}: {e}", flush=True)
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
        print(f"Registered {item['title']} in catalog.", flush=True)

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print("Wave 10 download and catalog registration complete!", flush=True)
