# Rajasthani (राजस्थानी) Language Library for Python

A standard-library-style computational linguistics toolkit, translator, and grammar engine for the **Rajasthani language** (`ISO 639-3: raj / mwr`).

## Features

1. **Universal Translation Engine (`rajasthani.translate`, `rajasthani.hindi_to_rajasthani`)**:
   - Translate from English, Hindi, and world languages into Rajasthani.
   - Dialect support: Marwari (`mwr`), Mewari (`mew`), Dhundhari (`dhd`), Harauti (`hoj`), Shekhawati (`swv`).
2. **Morphological Verb Conjugator & Syntax Engine (`rajasthani.conjugate`, `rajasthani.build_compound_verb`, `rajasthani.build_complex_sentence`)**:
   - Conjugates verbs across tenses (Present, Past, Future, Continuous, Presumptive, Imperative).
   - Compound verbs with aspectual vectors (`खाय लियो`, `दे दीनो`, `चाल पड़्यो`, `बोल उठ्यो`).
   - Correlative complex clauses (`जे... तो`, `जद... तद`, `जको... वो`, `जठै... वठै`, `जियां... तियां`).
   - Split ergativity past alignment with direct object agreement (`राम नै पोथी पढ़ी` vs `राम नै आंबा खायो`).
3. **Lexicon, Idioms & Folklore (`rajasthani.lookup`, `rajasthani.get_idioms`, `rajasthani.get_proverbs`, `rajasthani.get_riddles`)**:
   - 450+ cataloged and verified words, 20+ authentic idioms (मुहावरे), 30 proverbs (कहावतें), and 11 riddles (पहेलियाँ).
4. **Kinship & Social Relationships (`rajasthani.resolve_kinship`)**:
   - Comprehensive resolution of paternal, maternal, affinal (साढू, नणदोई), sibling, sworn (धरम-भाई), and friends terminology.
5. **Traditional Ornaments & Rituals (`rajasthani.culture`)**:
   - Dedicated modules for 32+ lifecycle rituals (जन्म, मुंडन, ब्याव, माहेरो, रातीजोगा) and 40+ head-to-toe ornaments (रखड़ी, शीशफूल, आड़, तिमणियो, गोखरू, आंवळा, रमझोल).
6. **Numbers & Numerals (`rajasthani.num_to_words`)**:
   - Full integer to word conversion (0 to 100,000,000+), Devanagari numerals (०-९), ordinals, and fractions.
7. **Digitized Primary Corpus (20 Historical Texts, ~16 MB)**:
   - Scanned foundational texts downloaded and parsed in `data_sources/raw_texts/` including *Veer Satsai*, *Dingal Kosh*, *Rajasthani Vat Sahitya*, *Loo*, *Jaagati Jot*, and Grierson's *LSI*.
8. **Interactive Web UI & CLI**:
   - Built-in zero-dependency web server and command-line interface.

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
