# -*- coding: utf-8 -*-
"""
Download Wave 7: Supreme Historical & Bardic Masterpieces
=========================================================
1. in.ernet.dli.2015.400763 - Rajasthani Kahawat Kosh (Bhagirath Kanoria) (~1.83 MB)
2. lzcw_rukamani-mangal-harji-ro-vyambalo - Rukamani Mangal Harji Ro Vyambalo (Padam Bhagat) (~1.00 MB)
3. dwht-bardic-and-historical-survey - Chhanda Rau Jeta Si Ro (Vithu Sujo / L.P. Tessitori) (~232 KB)
4. in.ernet.dli.2015.306886 - Parampra Dingal Kosh (Dr. Narayansingh Bhati) (~848 KB)
5. narsi-mehta-ka-bada-mamera - Narsi Mehta Ka Bada Mamera (Ram Ratan Darak) (~294 KB)
6. tbqa-veli-krisana-rukamani-ri - Veli Krisana Rukamani Ri (L.P. Tessitori 1919) (~390 KB)
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
        "id": "in.ernet.dli.2015.400763",
        "file": "2015.400763.Rajasthani-Kahawat_djvu.txt",
        "target": "in.ernet.dli.2015.400763_rajasthani_kahawat_kosh.txt",
        "title": "Rajasthani Kahawat Kosh",
        "author": "Bhagirath Kanoria",
        "year": "1965",
        "genre": "Proverbs, Paremiology & Folk Wisdom",
        "language": "Rajasthani / Marwari / Hindi"
    },
    {
        "id": "lzcw_rukamani-mangal-harji-ro-vyambalo-by-padam-bhagat-translated-by-satyanaraya",
        "file": "Rukamani Mangal Harji Ro Vyambalo By Padam Bhagat Translated by Satyanarayan Swami Rajasthani Hindi Translation Lucknow 1977 - Bhuvan Vani Trust_djvu.txt",
        "target": "padam_bhagat_rukamani_mangal_harji_ro_vyambalo_1977.txt",
        "title": "Rukamani Mangal & Harji Ro Vyambalo",
        "author": "Padam Bhagat / Satyanarayan Swami",
        "year": "1977",
        "genre": "Devotional Folk Ballad & Wedding Songs",
        "language": "Rajasthani / Marwari"
    },
    {
        "id": "dwht-bardic-and-historical-survey-of-rajputana-chanda-r",
        "file": "Bardic And Historical Survey Of Rajputana Chanda Rau Jeta Si Ro By Vithu Sujo L P Tessitori Dingal History Calcutta 1920 - Asiatic Society_djvu.txt",
        "target": "tessitori_vithu_sujo_chanda_rau_jeta_si_ro_1920.txt",
        "title": "Chhanda Rau Jeta Si Ro (Vithu Sujo)",
        "author": "Vithu Sujo / Dr. Luigi Pio Tessitori",
        "year": "1920",
        "genre": "Heroic Dingal Chronicle & Bardic History",
        "language": "Dingal / Rajasthani"
    },
    {
        "id": "in.ernet.dli.2015.306886",
        "file": "2015.306886.Parampra-Dingal_djvu.txt",
        "target": "in.ernet.dli.2015.306886_parampra_dingal_kosh.txt",
        "title": "Parampra Dingal Kosh",
        "author": "Dr. Narayansingh Bhati",
        "year": "1968",
        "genre": "Lexicography & Dingal Vocabulary",
        "language": "Dingal / Rajasthani"
    },
    {
        "id": "narsi-mehta-ka-bada-mamera-ram-ratan-darak-maheshwari-marwari",
        "file": "Narsi Mehta Ka Bada Mamera - Ram Ratan Darak Maheshwari Marwari_djvu.txt",
        "target": "narsi_mehta_ka_bada_mamera_marwari.txt",
        "title": "Narsi Mehta Ka Bada Mamera (Mayro)",
        "author": "Ram Ratan Darak Maheshwari",
        "year": "1952",
        "genre": "Folk Ballad & Mayra Traditions",
        "language": "Marwari / Rajasthani"
    },
    {
        "id": "tbqa-veli-krisana-rukamani-ri-part-1-dingala-text-by-ra",
        "file": "Veli Krisana Rukamani Ri Part 1 Dingala Text By Rathora Raja Prithi Raja L P Tessitori Rajasthani Poetry Calcutta 1919 - Asiatic Society_djvu.txt",
        "target": "tessitori_veli_krisana_rukamani_ri_asiatic_1919.txt",
        "title": "Veli Krisana Rukamani Ri (Asiatic Society Edition)",
        "author": "Rathore Raja Prithviraj / Dr. L.P. Tessitori",
        "year": "1919",
        "genre": "Classical Dingal Poetry (Tessitori Critical Edition)",
        "language": "Dingal / Rajasthani"
    }
]

print(f"Starting Wave 7 download of {len(ITEMS)} texts...")

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

print(f"Wave 7 download and catalog update complete. Total catalog entries: {len(catalog)}")
