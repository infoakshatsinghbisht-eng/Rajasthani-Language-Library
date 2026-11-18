# Rajasthani (राजस्थानी) Language Library for Python

A standard-library-style computational linguistics toolkit, translator, and grammar engine for the **Rajasthani language** (`ISO 639-3: raj / mwr`).

## Features

1. **Universal Translation Engine (`rajasthani.translate`, `rajasthani.hindi_to_rajasthani`)**:
   - Translate from English, Hindi, and world languages into Rajasthani.
   - Dialect support: Marwari (`mwr`), Mewari (`mew`), Dhundhari (`dhd`), Harauti (`hoj`), Shekhawati (`swv`).
2. **Morphological Verb Conjugator (`rajasthani.conjugate`)**:
   - Conjugates verbs across tenses (Present, Past, Future, Continuous, Presumptive, Imperative).
   - Ergative past alignment with transitive verbs (`राम नै रोटी खाई`).
3. **Lexicon & Proverbs (`rajasthani.lookup`, `rajasthani.search`)**:
   - 273+ cataloged and verified words, authentic idioms, proverbs (कहावतें), and riddles (पहेलियाँ).
4. **Kinship & Social Relationships (`rajasthani.resolve_kinship`)**:
   - Comprehensive resolution of family, affinal, sibling, and friends terminology.
5. **Traditional Ornaments & Rituals (`rajasthani.culture`)**:
   - Dedicated modules for lifecycle rituals (जन्म, मुंडन, ब्याव, माहेरो) and head-to-toe ornaments.
6. **Numbers & Numerals (`rajasthani.num_to_words`)**:
   - Full integer to word conversion (0 to 100,000,000+), Devanagari numerals (०-९), ordinals, and fractions.
7. **Digitized Primary Corpus**:
   - Over 9.5 MB of scanned foundational texts downloaded and parsed in `data_sources/raw_texts/`.
8. **Interactive Web UI & CLI**:
   - Built-in web server and command-line interface.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
import rajasthani

# 1. Translation
result = rajasthani.translate("How are you?")
print(result.text)       # थें कियां हो सा?
print(result.romanized)  # then kiyan ho sa?

# 2. Hindi Sentence Converter
print(rajasthani.hindi_to_rajasthani("मैं पानी पी रहा था"))  # म्हूँ पाणी पी रह्यो थो

# 3. Verb Conjugation
print(rajasthani.conjugate("खाणो", tense="past", gender="masculine"))  # खायो

# 4. Numbers to Words
print(rajasthani.num_to_words(42))  # बयालीस
print(rajasthani.to_devanagari_numerals(42))  # ४२

# 5. Kinship Resolution
term = rajasthani.resolve_kinship("मामो")
print(term.english, "|", term.honorific)  # maternal uncle | मामोजी सा

friend = rajasthani.resolve_kinship("भाईलो")
print(friend.hindi)  # मित्र / जिगरी दोस्त / यार

# 6. Ornaments & Rituals
ornament = rajasthani.lookup("शीशफूल")
print(ornament.english)  # traditional floral forehead ornament

ritual = rajasthani.lookup("माहेरो")
print(ritual.english)    # maternal uncle's wedding gift tradition
```

## CLI Usage

```bash
# Translation
rajasthani translate "How are you?"
rajasthani translate "Welcome" --dialect dhd

# Verb Conjugation
rajasthani conjugate खाणो --tense past --gender feminine

# Number conversion
rajasthani num 105

# Dictionary
rajasthani dict चोखो

# Kinship resolution
rajasthani kinship मामो

# Launch Local Web UI
rajasthani web --port 8000
```

## Running Tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## License

MIT License.
