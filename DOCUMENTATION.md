# Rajasthani (राजस्थानी) Language Library - Documentation & Reference Manual

## 1. Linguistic Overview & Classification
- **Macro-language ISO 639-3**: `raj`
- **Dialect ISO codes**:
  - Marwari (Western Rajasthan - Jodhpur, Bikaner, Jaisalmer): `mwr`
  - Mewari (South-Central - Udaipur, Chittorgarh): `mew`
  - Dhundhari / Jaipuri (East-Central - Jaipur, Dausa): `dhd`
  - Harauti (South-Eastern - Kota, Bundi): `hoj`
  - Shekhawati (North-Central - Sikar, Jhunjhunu, Churu): `swv`
  - Bagri (North-Western): `bgq`
  - Wagdi (Southern): `wbr`
  - Mewati (North-Eastern): `wtm`

---

## 2. Sentence Formation, Syntax & Conversion Engine

### Rule 1: Canonical Constituent Word Order (SOV)
Rajasthani adheres strictly to Subject - Object - Verb word order:
$$\text{Subject} + (\text{Time/Location}) + \text{Indirect Object} + \text{Direct Object} + \text{Verb} + \text{Auxiliary}$$

*Example*:
`म्हूँ (S) सवेरै (Time) घर मांय (Loc) पोथी (O) पढ़ूँ हूँ (V).`
*(I read a book at home in the morning.)*

### Rule 2: Split Ergativity in Past Tense (भूतकालिक सकर्मक क्रिया तालमेल)
1. **Present, Continuous & Future Tenses**:
   - Nominative alignment. The verb agrees with the Subject:
     - `राम पोथी पढ़ै है।` *(Ram reads the book.)*
     - `सीता पोथी पढ़ै है।` *(Sita reads the book.)*
2. **Past Tense (with Transitive Verbs)**:
   - Split ergative alignment. The Subject takes the Ergative marker `नै` (or pronominal forms `म्हैं` for I, `तैं` for thou, `उण` for that/he).
   - The verb agrees with the **Direct Object** in gender and number:
     - `राम नै पोथी पढ़ी।` *(Ram read the book - 'पढ़ी' is feminine agreeing with 'पोथी'.)*
     - `राम नै आंबा खायो।` *(Ram ate the mango - 'खायो' is masculine singular.)*
     - `म्हैं लाडू खाया।` *(I ate laddoos - 'खाया' is masculine plural.)*

### Rule 3: Pronoun Clusivity (आपां vs. म्हें)
Rajasthani maintains the classical Indo-Aryan distinction between:
- **Inclusive 1st Person Plural (`आपां`)**: Speaker + Listener included (`आपां चालां` - let us all go together).
- **Exclusive 1st Person Plural (`म्हें`)**: Speaker + Companions, excluding listener (`म्हें जावांगा` - we are going, not you).
Use `rajasthani.convert_clusivity(sentence, inclusive=True/False)`.

### Rule 4: Causative Alternations (प्रेरणार्थक क्रियावां)
Rajasthani features two systematic tiers of morphological causativization:
- **Level 1 (Direct Causative - प्रत्यक्ष प्रेरणार्थक)**: `करणो` $\rightarrow$ `करावणो`, `लिखणो` $\rightarrow$ `लिखावणो`, `खावणो` $\rightarrow$ `जिमावणो`.
- **Level 2 (Mediated Causative - अप्रत्यक्ष प्रेरणार्थक)**: `करणो` $\rightarrow$ `करवावणो`, `लिखणो` $\rightarrow$ `लिखवावणो`, `खावणो` $\rightarrow$ `जिमवावणो`.
Use `rajasthani.generate_causative(verb, level=1/2)`.

### Rule 5: Compound Verbs & Aspectual Vectors (संयुक्त क्रियावां)
Vector auxiliaries attach to conjunctive participle stems to mark aspect and orientation:
- `लेणो` (Self-benefactive): `खाय लियो`, `बांच लियो`
- `देणो` (Outward action): `दे दीनो`, `बताय दीनो`
- `पड़णो` (Sudden/involuntary action): `चाल पड़्यो`, `हंस पड़्यो`
- `नांखणो` (Complete disposal / violent telicity): `मार नांख्यो`, `फैंक नांख्यो`
Use `rajasthani.build_compound_verb(main_verb, vector_verb, tense, gender, number)`.

### Rule 6: Correlative Complex Sentences (मिश्र अर संयुक्त वाक्य)
Constructs authentic folk vat and literary correlatives:
- `conditional`: `जे... तो` (*जे मेह बरस्यो, तो फसल चोखी व्हैला।*)
- `temporal`: `जद... तद` (*जद सूरज ऊग्यो, तद अंधेरो मिट ग्यो।*)
- `relative`: `जको... वो` (*जको मेहनत करै है, वो सुखी रह्वै है।*)
- `spatial`: `जठै... वठै` (*जठै धर्मी राजा, वठै आनंद।*)
- `manner`: `जियां... तियां` (*जियां कह्यो, तियां कियो।*)
- `concessive`: `भले ही... पण` (*भले ही आंधी आवै, पण कदम नीं रुकसी।*)
Use `rajasthani.build_complex_sentence(sub_clause, main_clause, connector_type)`.

### Rule 7: Imperative Directives & Politeness Registers
Four distinct social honorific tiers:
- `intimate` (तूं): `तूं लिख` / negative: `तूं मती लिख`
- `familiar` (तूं/थे): `तूं लिखो`
- `polite` (थे): `थे लिखो` / `थे बांचो`
- `honorific` (आप / हुकम): `आप विराजो सा` / `आप आरोगो सा` / `आप पधारो सा`
Use `rajasthani.build_imperative(verb, politeness_level, negative)`.

### Rule 8: Synthetic Passive Voice (`-ईजै` / `-इजै`)
Transforms active sentences into passive or impersonal voice:
- `राम पोथी बांचै है` $\rightarrow$ `राम सूं पोथी बंचीजै है`
- `म्हैं काम कियो` $\rightarrow$ `म्हारै सूं काम करीज्यो`
Use `rajasthani.transform_voice(sentence, target_voice="passive")`.

---

## 3. Digitized Primary Corpus Sources (31 Texts, 41+ MB)
All full-text transcripts are indexed in `data_sources/corpus_catalog.json` and stored in `data_sources/raw_texts/`:
1. `in.ernet.dli.2015.348143_sitaram_lalas_rajasthani_shabdkosh_vol4.txt` (8.67 MB): *Rajasthani Shabdkosh (Vol IV)*, Dr. Sitaram Lalas.
2. `in.ernet.dli.2015.345971_sitaram_lalas_rajasthani_sabad_kos_vol2.txt` (6.05 MB): *Rajasthani Sabad Kos (Part 2-2)*, Sitaram Lalas.
3. `maheshwari_rajasthani_bhasha_sahitya_1960.txt` (2.15 MB): *Rajasthani Bhasha Aur Sahitya*, Dr. Hiralal Maheshwari.
4. `in.ernet.dli.2015.348199_2015.348199.Dhola-Maru_djvu.txt` (2.16 MB): *Dhola Maru Ra Dhoha*, Dr. Bhagwati Lal Rajpurohit.
5. `in.ernet.dli.2015.314052_2015.314052.Kanhadade-Prabandha_djvu.txt` (1.75 MB): *Kanhadade Prabandha (Vol 1)*, Kavi Padmanabha.
6. `bhati_rajasthani_madhyakal_1954.txt` (1.77 MB): *Rajasthani Sahitya Ka Madhyakal*, Dr. Narayansingh Bhati.
7. `in.ernet.dli.2015.443912_2015.443912.Rajasthani-Lok_djvu.txt` (1.69 MB): *Rajasthani Lok Sahitya Ki Saidhanti Vivechna*, Sohandan Charan.
8. `in.ernet.dli.2015.345924_prakrit_apbransh_dingal_prabhav.txt` (1.63 MB): *Prakrit Aur Apbransh Ka Dingal Sahitya Par Prabhav*, Dr. Govardhan Sharma.
9. `bhati_dingal_geet_sahitya_1961.txt` (1.41 MB): *Dingal Geet Sahitya*, Dr. Narayansingh Bhati.
10. `in.ernet.dli.2015.321330_2015.321330.Rajasthani-Bhasha_djvu.txt` (1.35 MB): *Rajasthani Bhasha Aur Sahitya*, Dr. Narayansingh Bhati.
11. `in.ernet.dli.2015.444415_marwari_vyapari.txt` (1.23 MB): *Marwari Vyapari*, Giriraj Shankar Sharma.
12. `in.ernet.dli.2015.545356_2015.545356.Krisan-Rukmani-Ri-Veli_djvu.txt` (1.15 MB): *Veli Krisan Rukmani Ri*, Rathore Prithviraj / Swami Narottamdas.
13. `in.ernet.dli.2015.347988_rajasthani_sahitya_kosh_chand.txt` (1.13 MB): *Rajasthani Sahitya Kosh (Chhand Shastra)*, Dr. Narayansingh Bhati.
14. `grierson_lsi_vol9_rajasthani_1908.txt` (1.03 MB): *LSI Vol. IX Part II: Rajasthani & Gujarati*, Sir George Grierson.
15. `in.ernet.dli.2015.380463_...txt` (1.01 MB): *Veer Satsai*, Mahakavi Suryamal Misran.
16. `bhati_dingal_kosh_1978.txt` (788 KB): *Dingal Kosh*, Dr. Narayansingh Bhati.
17. `ramkrishan_hindi_rajasthani_tulnatmak_1977.txt` (780 KB): *Hindi Aur Rajasthani Bhasha Ka Tulnatmak Adhyan*.
18. `in.ernet.dli.2015.308096_...txt` (776 KB): *Rajasthani Vat Sahitya*, Dr. Poonam Daiya.
19. `prabhakar_sahitya_sanskriti_1968.txt` (699 KB): *Rajasthani Sahitya Aur Sanskriti*, Manohar Prabhakar.
20. `in.ernet.dli.2015.539046_dingal_me_veer_ras.txt` (622 KB): *Dingal Me Veer Ras*, Motilal Menariya.
21. `in.ernet.dli.2015.442115_...txt` (577 KB): *Rajasthani Bhasha, Sahitya, Sanskriti*, Dr. Ramprasad Dadhich.
22. `in.ernet.dli.2015.443965_...txt` (539 KB): *Rajasthani Lok Sahitya Adhyan Ke Aayam*, Dr. Ramprasad Dadhich.
23. `saraswat_dingal_geet_1960.txt` (446 KB): *Dingal Geet*, Rawat Saraswat.
24. `in.ernet.dli.2015.444198_...txt` (395 KB): *Rajasthani Nibandh*, Manohar Sharma.
25. `in.ernet.dli.2015.444365_...txt` (363 KB): *Rajasthani Kahani Sangrah (Jaagati Jot)*, Ramesh Dayal.
26. `menariya_rajasthani_rooprekha_1953.txt` (254 KB): *Rajasthani Bhasha Ki Rooprekha*, Purushottam Menariya.
27. `chatterji_rajasthani_bhasha_1949.txt` (108 KB): *Rajasthani Bhasha*, Dr. Suniti Kumar Chatterji.
28. `chandra_singh_loo_1955.txt` (78 KB): *Loo (Ritu Kavya)*, Chandra Singh Birbhadur.
*(And additional historical texts bringing the total corpus to 31 texts and 41.14 MB!)*

---

## 4. Lexicon, Folklore & Cultural Heritage
- **Lexicon**: **1,027+ fully verified lemmas** with Devanagari, IAST romanization, detailed English meaning, Hindi gloss, grammatical POS, gender, dialect, and illustrative example sentences across 20+ domains.
- **Idioms (मुहावरा)**: **42 authentic idioms** (`पगड़ी राखणी`, `खांडे री धार माथे चालणो`, `हाथ पीले करणा`, `घोड़े बेच'र सोवणो`, `घी के दीवे जळावणा`, `दांत खट्टे करणा`, `सांढणी री चाल चलणो`, `हवेली रो दीवलो`).
- **Proverbs (कहावत / औखाणा)**: **39 traditional proverbs** (`साच नै आँच कोनी`, `गादड़ रो सींग नीं व्है`, `ऊंट किस करवट बैठै`, `धोरी रै माथै सींग, अर रजपूत रै माथै पाग`, `आप मुआं बिना सुरग नीं दीखै`).
- **Riddles (आड़ी / बुझावळ)**: **11 traditional riddles** with solutions and cultural metaphors.
- **Lifecycle Rituals (36 items)**: Birth, childhood, marriage, seasonal fasts, and memorial rites (`मायरो/भात`, `सामेलो`, `तोरण मारणो`, `बान बैठणो`, `रातीजगो`, `हथलेवो`, `कंकण-डोरा खोलणो`, `सीख/विदाई`, `मुकलावो`).
- **Traditional Ornaments (53 items)**: Head to toe (`रखड़ी`, `बोरलो`, `शीशफूल`, `मेमंद`, `नथ`, `बेसरी`, `आड़`, `तिमणियो`, `चंपाकली`, `हंसली`, `बाजूबंद`, `हाथीदांत रो चूड़ो`, `गोखरू`, `अरसी`, `कंदोरो`, `आंवळा`, `नेवरी`, `रमझोल`, `बिछिया`).
- **Extended Kinship (58 relations)**: Patrilineal, matrilineal, affinal (`साढू`, `नणदोई`, `ब्याई`, `ब्याण`), clan (`गोत-भाई`), sworn (`धरम-भाई`, `पगड़ी-बदल भाई`), and wedding companions (`कामोतर`, `ओळंदी`).

---

## 5. Web UI & REST API Endpoints
Run the built-in HTTP server:
```bash
rajasthani web --port 8000
```
Or programmatically:
```python
import rajasthani
rajasthani.run_server(port=8000)
```
Interactive Endpoints:
- `GET /api/translate?text=...&dialect=...` - Universal translator
- `GET /api/conjugate?verb=...&tense=...` - Morphological verb conjugator
- `GET /api/dictionary?q=...` - Full-text lexicon search (1,027+ words)
- `GET /api/numbers?val=...` - Number to Devanagari words & digits
- `GET /api/rituals?category=...` - Traditional lifecycle rituals (36 entries)
- `GET /api/ornaments?part=...` - Traditional jewelry (53 entries)
- `GET /api/syntax` - Structured syntax, split-ergativity, causatives, and dialect rules
- `GET /api/corpus` - Catalog of 31 digitized historical texts (41.14 MB)
- `GET /api/idioms` - Authentic idioms and sayings (42 entries)
- `GET /api/folklore` - Folk proverbs and riddles (50 entries)

---

## 6. Python API Reference
```python
import rajasthani

# 1. Dictionary & Lexicon (1,027+ words)
w = rajasthani.lookup("सांग")
print(w.english)  # "traditional Rajput iron lance or javelin wielded on horseback"

# 2. Syntax & Sentence Construction
s = rajasthani.hindi_to_rajasthani("मैं पानी पी रहा था", dialect=rajasthani.Dialect.MARWARI)
# -> "म्हूँ पाणी पी रह्यो थो"

# 3. Compound Verbs
cv = rajasthani.build_compound_verb("खाणो", vector_verb="लेणो", tense=rajasthani.Tense.PAST)
# -> "खाय लियो"

# 4. Complex Correlatives
sent = rajasthani.build_complex_sentence("मेह बरस्यो", "फसल चोखी व्हैला", connector_type="conditional")
# -> "जे मेह बरस्यो, तो फसल चोखी व्हैला।"

# 5. Causatives
caus1 = rajasthani.generate_causative("करणो", level=1)  # "करावणो"
caus2 = rajasthani.generate_causative("करणो", level=2)  # "करवावणो"

# 6. Imperatives & Honorific Registers
imp_intimate = rajasthani.build_imperative("लिखणो", politeness_level="intimate")  # "तूं लिख"
imp_royal = rajasthani.build_imperative("बैठणो", politeness_level="honorific")     # "आप विराजो सा"

# 7. Clusivity
incl = rajasthani.convert_clusivity("हम चालेंगे", inclusive=True)   # "आपां चालेंगे"
excl = rajasthani.convert_clusivity("आपां चालेंगे", inclusive=False)  # "म्हे चालेंगे"

# 8. Synthetic Passive Voice
pass_sent = rajasthani.transform_voice("राम पोथी बांचै है")  # "राम रै हाथूं पोथी बंचीजै है।"

# 9. Kinship & Culture
kin = rajasthani.resolve_kinship("साढू")
rituals = rajasthani.get_all_rituals()
ornaments = rajasthani.get_all_ornaments()
```
