# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('data_sources/discovered_books.json', encoding='utf-8') as f:
    books = json.load(f)

texts = [b for b in books if b.get('mediatype') == 'texts']
print(f"Total text books found: {len(texts)}")
for i, b in enumerate(texts[:50], 1):
    title = b.get('title', 'Unknown Title')
    creator = b.get('creator', 'Unknown Author')
    year = b.get('year', 'N/A')
    ident = b.get('identifier', '')
    print(f"{i}. [{ident}] {title} - {creator} ({year})")
