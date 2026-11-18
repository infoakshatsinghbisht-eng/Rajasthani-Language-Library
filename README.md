# Rajasthani (राजस्थानी) Language Library for Python

A standard-library-style computational linguistics toolkit, translator, and grammar engine for the **Rajasthani language** (`ISO 639-3: raj / mwr`).

## Features

1. **Universal Translation Engine (`rajasthani.translate`, `rajasthani.hindi_to_rajasthani`)**:
   - Translate from English, Hindi, and world languages into Rajasthani.
   - Dialect support: Marwari (`mwr`), Mewari (`mew`), Dhundhari (`dhd`), Harauti (`hoj`), Shekhawati (`swv`).
2. **Morphological Verb Conjugator & Syntax Engine**:
   - Conjugates verbs across tenses (Present, Past, Future, Continuous, Presumptive, Imperative).
   - Compound verbs with aspectual vectors (`rajasthani.build_compound_verb` - `खाय लियो`, `दे दीनो`, `चाल पड़्यो`, `मार नांख्यो`).
   - Correlative complex clauses (`rajasthani.build_complex_sentence` - `जे... तो`, `जद... तद`, `जको... वो`, `जठै... वठै`, `जियां... तियां`).
   - Past counterfactual conditionals (`rajasthani.build_counterfactual_conditional` - `जे मेह बरसतो, तो अकाल नीं पड़तो`).
   - Benedictions and optative wishes (`rajasthani.build_optative` - `भगवान थारो भलो करै!`).
   - Classical folk vat narrative builder (`rajasthani.build_vat_narrative` - authentic story discourse).
   - Split ergativity past alignment with direct object agreement (`राम नै पोथी पढ़ी` vs `राम नै आंबा खायो`).
   - Causative morphology derivation (`rajasthani.generate_causative` - `करावणो`, `करवावणो`, `जिमावणो`, `जिमवावणो`).
   - Imperative directives across 4 politeness tiers (`rajasthani.build_imperative` - intimate, familiar, polite, honorific).
   - Pronoun clusivity conversion (`rajasthani.convert_clusivity` - `आपां` inclusive vs `म्हे` exclusive).
   - Synthetic passive voice transformation (`rajasthani.transform_voice` - `-ईजै` / `-इजै`).
3. **Mega Lexicon, Idioms & Folklore**:
   - **1,204+** cataloged and fully verified words with Devanagari, English, Hindi, POS, gender, dialect, and example sentences.
   - **42 authentic idioms** (मुहावरे) with cultural contexts.
   - **39 traditional proverbs** (कहावतें / औखाणा).
   - **11 folk riddles** (पहेलियाँ / आड़ी).
4. **Kinship & Clan Taxonomy (`rajasthani.resolve_kinship`)**:
   - 58 distinct relationships across patrilineal, matrilineal, affinal (`साढू`, `नणदोई`, `ब्याई`, `ब्याण`), sworn (`धरम-भाई`, `पगड़ी-बदल भाई`), and wedding companions (`कामोतर`, `ओळंदी`).
5. **Traditional Ornaments & Lifecycle Rituals (`rajasthani.culture`)**:
   - 36 lifecycle rituals (जन्म, मुंडन, ब्याव, माहेरो, रातीजोगा, तोरण, सीख, मुकलावो).
   - 53 traditional head-to-toe ornaments (`रखड़ी`, `बोरलो`, `शीशफूल`, `आड़`, `तिमणियो`, `गोखरू`, `आंवळा`, `रमझोल`, `बिछिया`).
6. **Numbers & Numerals (`rajasthani.num_to_words`)**:
   - Full integer to word conversion (0 to 100,000,000+), Devanagari numerals (०-९), ordinals, and fractions.
7. **Digitized Primary Corpus (37 Historical Files, ~45.52 MB)**:
   - Complete transcripts in `data_sources/raw_texts/` including *Rajasthani Shabdkosh* (Vols II & IV by Dr. Sitaram Lalas), *Rajasthani Kahawat Kosh* (Bhagirath Kanoria), *Dhola Maru Ra Dhoha*, *Kanhadade Prabandha*, *Chhanda Rau Jeta Si Ro* (Vithu Sujo / Tessitori), *Veli Krisan Rukmani Ri*, *Veer Satsai*, *Parampra Dingal Kosh*, *Harji Ro Vyambalo*, *Narsi Mehta Ka Bada Mamera*, and Grierson's *LSI*.
8. **Interactive Web UI & CLI**:
   - Built-in zero-dependency web server (`rajasthani web --port 8000`) with REST API and responsive 7-tab dashboard.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
import rajasthani

# 1. Translation & Conversion
print(rajasthani.translate("How are you?").text)  # थें कियां हो सा?
print(rajasthani.hindi_to_rajasthani("मैं पानी पी रहा था"))  # म्हूँ पाणी पी रह्यो थो

# 2. Causatives & Compound Verbs
print(rajasthani.generate_causative("करणो", level=1))  # करावणो
print(rajasthani.generate_causative("करणो", level=2))  # करवावणो
print(rajasthani.build_compound_verb("खाणो", vector_verb="लेणो", tense=rajasthani.Tense.PAST))  # खाय लियो

# 3. Correlative Sentences, Counterfactuals & Imperatives
print(rajasthani.build_complex_sentence("मेह बरस्यो", "फसल चोखी व्हैला", connector_type="conditional"))
# -> जे मेह बरस्यो, तो फसल चोखी व्हैला।
print(rajasthani.build_counterfactual_conditional("मेह बरसतो", "अकाल नीं पड़तो"))
# -> जे मेह बरसतो, तो अकाल नीं पड़तो।
print(rajasthani.build_imperative("बैठणो", politeness_level="honorific"))  # आप विराजो सा

# 4. Optatives & Folk Vat Prose
print(rajasthani.build_optative("भगवान", "थारो भलो करै"))  # भगवान थारो भलो करै!
print(rajasthani.build_vat_narrative("राव जेतासी", "बीकानेर दुर्ग", "शत्रु दल नै परास्त कियो"))

# 5. Clusivity & Passive Voice
print(rajasthani.convert_clusivity("हम सब साथ चलेंगे", inclusive=True))  # आपां सब साथ चलेंगे
print(rajasthani.transform_voice("राम पोथी बांचै है"))  # राम रै हाथूं पोथी बंचीजै है।

# 6. Lexicon & Folklore
word = rajasthani.lookup("सांग")
print(word.english)  # traditional Rajput iron lance or javelin wielded on horseback

# 7. Kinship & Culture
term = rajasthani.resolve_kinship("साढू")
print(term.english)  # husband of one's wife's sister (co-brother-in-law)
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
**84 unit tests pass in ~0.03s with 100% success rate.**

## License

MIT License.
