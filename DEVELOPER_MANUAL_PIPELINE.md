# Developer Manual: Corpus Ingestion, Extraction & Pipeline

This manual outlines the pipeline for expanding the Rajasthani Language Library with primary texts, automated corpus downloading, and database synchronization.

## 1. Directory Structure

```
Rajasthan Language Library/
├── data_sources/
│   ├── corpus_catalog.json           # Catalog of foundational scanned/digitized texts
│   ├── discovered_books.json         # Archive.org search results metadata (221 books)
│   ├── ingest_corpus.py              # Automated download script for text transcripts
│   ├── extract_and_enrich.py         # Parsing, lemma extraction, and dictionary updater
│   └── raw_texts/                    # Stored full-text corpus files (~4.87 MB raw)
│       ├── grierson_lsi_vol9_rajasthani_1908.txt
│       ├── maheshwari_rajasthani_bhasha_sahitya_1960.txt
│       ├── chatterji_rajasthani_bhasha_1949.txt
│       ├── bhati_dingal_kosh_1978.txt
│       └── ramkrishan_hindi_rajasthani_tulnatmak_1977.txt
```

## 2. Ingestion Commands

```bash
# Search and discover books on Archive.org
python data_sources/search_archive.py

# Download full-text transcripts
python data_sources/ingest_corpus.py

# Extract vocabulary, idioms, and rituals into the dictionary
python data_sources/extract_and_enrich.py

# Run verification test suite
python -m unittest discover -s tests -p "test_*.py"
```
