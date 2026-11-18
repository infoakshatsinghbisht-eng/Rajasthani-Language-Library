# -*- coding: utf-8 -*-
"""
Corpus Ingestion & Digitalization Pipeline for Rajasthani Language
=================================================================
Downloads foundational digital texts from Archive.org, extracts lexical lemmas,
grammar forms, kinship relations, idioms, and rituals, and integrates them into
the standard library databases.
"""

import os
import ssl
import sys
import json
import urllib.request
import re

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl._create_unverified_context()

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_texts")
os.makedirs(RAW_DIR, exist_ok=True)

FOUNDATIONAL_CORPUS = [
    {
        "id": "RAJ-BOK-001",
        "archive_id": "in.ernet.dli.2015.95521",
        "file_name": "2015.95521.Linguistic-Survey-Of-Indiavol9indo-aryan-Familypt2specimens-Of-The-Rajasthani-And-Gujarati_djvu.txt",
        "local_name": "grierson_lsi_vol9_rajasthani_1908.txt",
        "title": "Linguistic Survey of India: Vol IX, Part II (Specimens of the Rajasthani and Gujarati)",
        "author": "Sir George Abraham Grierson",
        "year": 1908,
        "category": "Linguistics, Dialectology & Grammar",
    },
    {
        "id": "RAJ-BOK-002",
        "archive_id": "in.ernet.dli.2015.308914",
        "file_name": "2015.308914.Rajasthani-Bhasha_djvu.txt",
        "local_name": "maheshwari_rajasthani_bhasha_sahitya_1960.txt",
        "title": "Rajasthani Bhasha Aur Sahitya",
        "author": "Dr. Hiralal Maheshwari",
        "year": 1960,
        "category": "Literature & Linguistic History",
    },
    {
        "id": "RAJ-BOK-003",
        "archive_id": "in.ernet.dli.2015.536813",
        "file_name": "2015.536813.Rajasthani-Bhasha_djvu.txt",
        "local_name": "chatterji_rajasthani_bhasha_1949.txt",
        "title": "Rajasthani Bhasha",
        "author": "Dr. Suniti Kumar Chatterji",
        "year": 1949,
        "category": "Comparative Indo-Aryan Linguistics",
    },
    {
        "id": "RAJ-BOK-004",
        "archive_id": "in.ernet.dli.2015.347749",
        "file_name": "2015.347749.Dingal-Kosh_djvu.txt",
        "local_name": "bhati_dingal_kosh_1978.txt",
        "title": "Dingal Kosh",
        "author": "Dr. Narayansingh Bhati",
        "year": 1978,
        "category": "Lexicography & Bardic Vocabularies",
    },
    {
        "id": "RAJ-BOK-005",
        "archive_id": "in.ernet.dli.2015.443776",
        "file_name": "2015.443776.Hindi-Aur_djvu.txt",
        "local_name": "ramkrishan_hindi_rajasthani_tulnatmak_1977.txt",
        "title": "Hindi Aur Rajasthani Bhasha Ka Tulnatmak Adhyan",
        "author": "Dr. Ramkrishan Sharma",
        "year": 1977,
        "category": "Comparative Grammar & Syntax",
    },
]

print("=== Starting Download of Primary Foundational Rajasthani Texts ===")
downloaded_files = []

for item in FOUNDATIONAL_CORPUS:
    out_path = os.path.join(RAW_DIR, item["local_name"])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        print(f"Already exists: {item['local_name']} ({os.path.getsize(out_path)} bytes)")
        downloaded_files.append((item, out_path))
        continue

    url = f"https://archive.org/download/{item['archive_id']}/{item['file_name']}"
    print(f"Downloading: {item['title']} from {url} ...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            content = resp.read()
            with open(out_path, "wb") as f_out:
                f_out.write(content)
            print(f"Saved: {item['local_name']} ({len(content)} bytes)")
            downloaded_files.append((item, out_path))
    except Exception as e:
        print(f"Failed to download {item['local_name']}: {e}")

# Save corpus catalog
catalog_path = os.path.join(os.path.dirname(__file__), "corpus_catalog.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(FOUNDATIONAL_CORPUS, f, ensure_ascii=False, indent=2)

print(f"\nCorpus catalog saved to {catalog_path}")
print(f"Total downloaded foundational texts: {len(downloaded_files)}")
