# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl._create_unverified_context()

queries = [
    'title:(rajasthani) OR description:(rajasthani language)',
    'title:(marwari) AND (grammar OR language OR sahitya OR dictionary)',
    'title:(dingal) OR description:(dingal rajasthani)',
    'title:("rajasthani bhasha") OR title:("rajasthani sahitya")',
    'tessitori AND (bardic OR rajasthani OR marwari)',
    'grierson AND rajasthani',
    'title:(dhola maru) OR title:("rajasthani vat")',
    'title:("rajasthani lok")',
]

all_items = {}

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl=identifier,title,creator,year,mediatype,description&rows=40&page=1&output=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            docs = data.get('response', {}).get('docs', [])
            print(f"Query '{q}' returned {len(docs)} documents.")
            for d in docs:
                all_items[d['identifier']] = d
    except Exception as e:
        print(f"Error querying '{q}': {e}")

print(f"Total unique identifiers discovered: {len(all_items)}")

with open("data_sources/discovered_books.json", "w", encoding="utf-8") as f:
    json.dump(list(all_items.values()), f, ensure_ascii=False, indent=2)
