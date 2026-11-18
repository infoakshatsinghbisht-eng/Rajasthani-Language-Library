# -*- coding: utf-8 -*-
"""
Download Wave 8: Six Foundational Literary & Historical Masterpieces
===================================================================
1. in.ernet.dli.2015.444215 - Rohidai Ra Phool (Dr. Manohar Sharma) (~308 KB)
2. in.ernet.dli.2015.444217 - Rajasthan Ke Kavi (Rawat Saraswat) (~334 KB)
3. in.ernet.dli.2015.308999 - Rajasthani Sahitya Ka Adi Kal (Dr. Narayansingh Bhati) (~818 KB)
4. in.ernet.dli.2015.309837 - Rajasthani Bhag-1 (Swami Narottamdas) (~361 KB)
5. in.ernet.dli.2015.443715 - Sadayvts Veer Prabandh (Dr. Manjulal) (~414 KB)
6. in.ernet.dli.2015.442001 - Rajasthan Ke Aitihasik Granthon Ka Sarvekshana (Dr. Narayansingh Bhati) (~1.12 MB)
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
        "id": "in.ernet.dli.2015.444215",
        "file": "2015.444215.Rohidai-Ra_djvu.txt",
        "target": "in.ernet.dli.2015.444215_rohidai_ra_phool_manohar_sharma.txt",
        "title": "Rohidai Ra Phool",
        "author": "Dr. Manohar Sharma",
        "year": "1964",
        "genre": "Modern Rajasthani Prose & Essays",
        "language": "Rajasthani / Marwari"
    },
    {
        "id": "in.ernet.dli.2015.444217",
        "file": "2015.444217.Rajasthan-Ke_djvu.txt",
        "target": "in.ernet.dli.2015.444217_rajasthan_ke_kavi_rawat_saraswat.txt",
        "title": "Rajasthan Ke Kavi",
        "author": "Rawat Saraswat",
        "year": "1962",
        "genre": "Poetic Biographies & Dingal Verse",
        "language": "Rajasthani / Hindi"
    },
    {
        "id": "in.ernet.dli.2015.308999",
        "file": "2015.308999.Rajasthani-Sahitya_djvu.txt",
        "target": "in.ernet.dli.2015.308999_rajasthani_sahitya_adi_kal.txt",
        "title": "Rajasthani Sahitya Ka Adi Kal",
        "author": "Dr. Narayansingh Bhati",
        "year": "1960",
        "genre": "Early Medieval Literature & Philology",
        "language": "Dingal / Rajasthani"
    },
    {
        "id": "in.ernet.dli.2015.309837",
        "file": "2015.309837.Rajasthani-Bhag-1_djvu.txt",
        "target": "in.ernet.dli.2015.309837_rajasthani_bhag1_narottamdas_swami.txt",
        "title": "Rajasthani (Bhag 1)",
        "author": "Swami Narottamdas",
        "year": "1951",
        "genre": "Linguistic Reader & Grammatical Selections",
        "language": "Rajasthani / Marwari"
    },
    {
        "id": "in.ernet.dli.2015.443715",
        "file": "2015.443715.Sadayvts-Veer_djvu.txt",
        "target": "in.ernet.dli.2015.443715_sadayvts_veer_prabandh.txt",
        "title": "Sadayvts Veer Prabandh",
        "author": "Dr. Manjulal Majmudar",
        "year": "1959",
        "genre": "Heroic Medieval Romance & Ballads",
        "language": "Old Rajasthani / Dingal"
    },
    {
        "id": "in.ernet.dli.2015.442001",
        "file": "2015.442001.Rajasthan-Ke_djvu.txt",
        "target": "in.ernet.dli.2015.442001_rajasthan_ke_aitihasik_granth_sarvekshan.txt",
        "title": "Rajasthan Ke Aitihasik Granthon Ka Sarvekshana",
        "author": "Dr. Narayansingh Bhati",
        "year": "1971",
        "genre": "Historical Survey of Khayats & Vats",
        "language": "Rajasthani / Hindi"
    }
]

print(f"Starting Wave 8 download of {len(ITEMS)} texts...")

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
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, context=ctx, timeout=120) as resp, open(target_path, "wb") as out:
                content = resp.read()
                out.write(content)
            print(f"Downloaded successfully: {item['target']} ({len(content)} bytes)")
        except Exception as e:
            print(f"Failed to download {item['id']}: {e}")
            continue

    # Register in catalog if not present
    existing_entry = next((c for c in catalog if c.get("local_name") == item["target"] or c.get("filename") == item["target"]), None)
    if not existing_entry:
        file_size = os.path.getsize(target_path) if os.path.exists(target_path) else 0
        new_id = f"RAJ-BOK-{len(catalog) + 1:03d}"
        catalog.append({
            "id": new_id,
            "filename": item["target"],
            "local_name": item["target"],
            "title": item["title"],
            "author": item["author"],
            "year": item["year"],
            "genre": item["genre"],
            "category": item["genre"],
            "language": item["language"],
            "source": f"Internet Archive ({item['id']})",
            "size_bytes": file_size
        })

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Wave 8 download and catalog update complete. Total catalog entries: {len(catalog)}")
