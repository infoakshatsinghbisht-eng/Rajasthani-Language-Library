# -*- coding: utf-8 -*-
import json
import os

cat_file = "data_sources/corpus_catalog.json"
with open(cat_file, "r", encoding="utf-8") as f:
    cat = json.load(f)

existing_ids = {c["id"] for c in cat}
existing_files = {c.get("local_name") for c in cat}

new_entries = [
    {
        "id": "RAJ-BOK-014",
        "archive_id": "in.ernet.dli.2015.321330",
        "file_name": "2015.321330.Rajasthani-Bhasha_djvu.txt",
        "local_name": "in.ernet.dli.2015.321330_2015.321330.Rajasthani-Bhasha_djvu.txt",
        "title": "Rajasthani Bhasha Aur Sahitya",
        "author": "Dr. Narayansingh Bhati / Dr. Hiralal Maheshwari",
        "year": 1960,
        "category": "Literature, Poetics & History",
        "size_kb": 1349.2
    },
    {
        "id": "RAJ-BOK-015",
        "archive_id": "in.ernet.dli.2015.442115",
        "file_name": "2015.442115.Rajasthani-Bhasha_djvu.txt",
        "local_name": "in.ernet.dli.2015.442115_2015.442115.Rajasthani-Bhasha_djvu.txt",
        "title": "Rajasthani Bhasha, Sahitya, Sanskriti",
        "author": "Dr. Ramprasad Dadhich",
        "year": 1986,
        "category": "Language, Cultural Traditions & Literary Critique",
        "size_kb": 564.4
    }
]

for entry in new_entries:
    if entry["id"] not in existing_ids and entry["local_name"] not in existing_files:
        cat.append(entry)

with open(cat_file, "w", encoding="utf-8") as f:
    json.dump(cat, f, ensure_ascii=False, indent=2)

print(f"Catalog updated! Total cataloged books: {len(cat)}")
