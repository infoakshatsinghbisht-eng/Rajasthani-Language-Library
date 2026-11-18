# -*- coding: utf-8 -*-
"""
Wave 2 Ingestion: Download 10 more premier Rajasthani literary, folklore & grammar texts
======================================================================================
"""

import os
import ssl
import sys
import json
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl._create_unverified_context()

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_texts")
os.makedirs(RAW_DIR, exist_ok=True)

with open(os.path.join(os.path.dirname(__file__), "discovered_books.json"), "r", encoding="utf-8") as f:
    discovered = json.load(f)

# Priority identifiers for literature, folklore, proverbs, and dictionaries
TARGET_BOOKS = [
    {
        "id": "RAJ-BOK-006",
        "archive_id": "in.ernet.dli.2015.347797",
        "file_name": "2015.347797.Dingal-Geet_djvu.txt",
        "local_name": "saraswat_dingal_geet_1960.txt",
        "title": "Dingal Geet",
        "author": "Rawat Saraswat",
        "year": 1960,
        "category": "Bardic Poetry & Folk Ballads",
    },
    {
        "id": "RAJ-BOK-007",
        "archive_id": "in.ernet.dli.2015.401053",
        "file_name": "2015.401053.Dingal-Geet_djvu.txt",
        "local_name": "bhati_dingal_geet_sahitya_1961.txt",
        "title": "Dingal Geet Sahitya",
        "author": "Dr. Narayansingh Bhati",
        "year": 1961,
        "category": "Classical Dingal Poetics",
    },
    {
        "id": "RAJ-BOK-008",
        "archive_id": "in.ernet.dli.2015.325506",
        "file_name": "2015.325506.Loo-rajasthani_djvu.txt",
        "local_name": "chandra_singh_loo_1955.txt",
        "title": "Loo (Rajasthani Bhasha Ka Ritu Kavya)",
        "author": "Chandra Singh Birbhadur",
        "year": 1955,
        "category": "Modern Rajasthani Poetry & Seasons",
    },
    {
        "id": "RAJ-BOK-009",
        "archive_id": "in.ernet.dli.2015.348572",
        "file_name": "2015.348572.Rajasthani-Bhasha_djvu.txt",
        "local_name": "menariya_rajasthani_rooprekha_1953.txt",
        "title": "Rajasthani Bhasha Ki Rooprekha Aur Manyta Ka Prasan",
        "author": "Purushottam Menariya",
        "year": 1953,
        "category": "Grammar, Dialects & Morphology",
    },
    {
        "id": "RAJ-BOK-010",
        "archive_id": "in.ernet.dli.2015.445241",
        "file_name": "2015.445241.Rajasthani-Sahitya-sangrah_djvu.txt",
        "local_name": "jinvijay_rajasthani_sahitya_sangrah_vol2_1962.txt",
        "title": "Rajasthani Sahitya-Sangrah Bhag-II",
        "author": "Muni Jinvijay",
        "year": 1962,
        "category": "Medieval Rajasthani Literature & Epics",
    },
    {
        "id": "RAJ-BOK-011",
        "archive_id": "in.ernet.dli.2015.347874",
        "file_name": "2015.347874.Rajasthani-sahitya-sagrah_djvu.txt",
        "local_name": "jinvijay_rajasthani_sahitya_sangrah_vol3_1966.txt",
        "title": "Rajasthani Sahitya-Sangrah Bhag-III",
        "author": "Muni Jinvijay",
        "year": 1966,
        "category": "Historical Vats & Charani Literature",
    },
    {
        "id": "RAJ-BOK-012",
        "archive_id": "in.ernet.dli.2015.309510",
        "file_name": "2015.309510.Rajasthani-Sahitya_djvu.txt",
        "local_name": "bhati_rajasthani_madhyakal_1954.txt",
        "title": "Rajasthani Sahitya Ka Madhyakal",
        "author": "Dr. Narayansingh Bhati",
        "year": 1954,
        "category": "Medieval Rajasthani Literary History",
    },
    {
        "id": "RAJ-BOK-013",
        "archive_id": "in.ernet.dli.2015.321591",
        "file_name": "2015.321591.Rajasthani-Sahitya_djvu.txt",
        "local_name": "prabhakar_sahitya_sanskriti_1968.txt",
        "title": "Rajasthani Sahitya Aur Sanskriti",
        "author": "Manohar Prabhakar",
        "year": 1968,
        "category": "Folk Culture, Rituals & Beliefs",
    },
]

print("=== Downloading Wave 2 Foundational Digital Texts ===")
downloaded = []

for b in TARGET_BOOKS:
    out_file = os.path.join(RAW_DIR, b["local_name"])
    if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
        print(f"Already exists: {b['local_name']} ({os.path.getsize(out_file)} bytes)")
        downloaded.append(b)
        continue

    url = f"https://archive.org/download/{b['archive_id']}/{b['file_name']}"
    print(f"Fetching: {b['title']} -> {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            data = resp.read()
            with open(out_file, "wb") as f_out:
                f_out.write(data)
            print(f"Saved: {b['local_name']} ({len(data)} bytes)")
            downloaded.append(b)
    except Exception as e:
        print(f"Download failed for {b['local_name']}: {e}")

# Append to catalog
catalog_path = os.path.join(os.path.dirname(__file__), "corpus_catalog.json")
with open(catalog_path, "r", encoding="utf-8") as f:
    cat = json.load(f)

cat_ids = {c["id"] for c in cat}
for b in downloaded:
    if b["id"] not in cat_ids:
        cat.append(b)

with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(cat, f, ensure_ascii=False, indent=2)

print(f"\nCorpus catalog updated! Total registered books: {len(cat)}")
