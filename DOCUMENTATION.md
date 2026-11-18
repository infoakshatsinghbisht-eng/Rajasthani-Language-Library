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

## 2. Sentence Formation & Conversion Rules

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
   - Split ergative alignment. The Subject must take the Ergative marker `नै` (or pronominal forms `म्हैं` for I, `तैं` for thou, `उण` for that/he).
   - The verb agrees with the **Direct Object** in gender and number:
     - `राम नै पोथी पढ़ी।` *(Ram read the book - 'पढ़ी' is feminine agreeing with 'पोथी'.)*
     - `राम नै आंबा खायो।` *(Ram ate the mango - 'खायो' is masculine singular.)*
     - `म्हैं लाडू खाया।` *(I ate laddoos - 'खाया' is masculine plural.)*

### Rule 3: Pronoun Clusivity (आपां vs. म्हें)
Rajasthani maintains the classical Indo-Aryan distinction between:
- **Inclusive 1st Person Plural (`आपां`)**: Speaker + Listener included (`आपां चालां` - let us all go together).
- **Exclusive 1st Person Plural (`म्हें`)**: Speaker + Companions, excluding listener (`म्हें जावांगा` - we are going, not you).

### Rule 4: Bidirectional Sentence Conversion (`rajasthani.hindi_to_rajasthani`)
- Direct morphological and syntactic mapping from standard Hindi to Rajasthani dialects:
  - `मैं पानी पी रहा था` $\rightarrow$ `म्हूँ पाणी पी रह्यो थो` (Marwari)
  - `मैं पानी पी रहा था` $\rightarrow$ `म्हूँ पाणी पी रह्यो छो` (Dhundhari)
  - `मैं पानी पी रहा था` $\rightarrow$ `म्हूँ पाणी पी रह्यो हो` (Mewari)

---

## 3. Digitized Primary Corpus Sources
Downloaded full-text transcripts stored in `data_sources/raw_texts/` (over 9.5 MB primary text data):
1. `grierson_lsi_vol9_rajasthani_1908.txt` (1.03 MB): *LSI Vol. IX Part II: Rajasthani & Gujarati*, Sir George Grierson.
2. `maheshwari_rajasthani_bhasha_sahitya_1960.txt` (2.15 MB): *Rajasthani Bhasha Aur Sahitya*, Dr. Hiralal Maheshwari.
3. `chatterji_rajasthani_bhasha_1949.txt` (107 KB): *Rajasthani Bhasha*, Dr. Suniti Kumar Chatterji.
4. `bhati_dingal_kosh_1978.txt` (788 KB): *Dingal Kosh*, Dr. Narayansingh Bhati.
5. `ramkrishan_hindi_rajasthani_tulnatmak_1977.txt` (780 KB): *Hindi Aur Rajasthani Bhasha Ka Tulnatmak Adhyan*, Dr. Ramkrishan Sharma.
6. `saraswat_dingal_geet_1960.txt` (445 KB): *Dingal Geet*, Rawat Saraswat.
7. `bhati_dingal_geet_sahitya_1961.txt` (1.41 MB): *Dingal Geet Sahitya*, Dr. Narayansingh Bhati.
8. `chandra_singh_loo_1955.txt` (78 KB): *Loo (Rajasthani Bhasha Ka Ritu Kavya)*, Chandra Singh.
9. `menariya_rajasthani_rooprekha_1953.txt` (254 KB): *Rajasthani Bhasha Ki Rooprekha*, Purushottam Menariya.
10. `bhati_rajasthani_madhyakal_1954.txt` (1.77 MB): *Rajasthani Sahitya Ka Madhyakal*, Dr. Narayansingh Bhati.
11. `prabhakar_sahitya_sanskriti_1968.txt` (698 KB): *Rajasthani Sahitya Aur Sanskriti*, Manohar Prabhakar.

---

## 4. Lifecycle Rituals & Ornaments
- **Lifecycle Rituals (`rajasthani.get_all_rituals`)**:
  - `कुआँ पूजन / जलवा (Jalwa Pujan)`: Water reverence following childbirth.
  - `जड़ूलो (Jadoolo)`: Tonsure / Mundan at ancestral Kuldevi shrine.
  - `ढूंढ (Dhoondh)`: Newborn blessing festival at Holi.
  - `माहेरो / भात (Mayera / Bhaat)`: Maternal uncle wedding presentation.
  - `बान बैठना (Baan Baithna)`: Auspicious ubtan bath.
  - `बिंदौरी (Bindori)`: Village procession for bride and groom.
  - `सामेला (Samela)`: Reception of groom's party by bride's father.
  - `तोरण मारना (Toran Marna)`: Striking the sacred gateway arch.
  - `फेरा / हथलेवा (Phera / Hathleva)`: Agni circumambulation.
- **Traditional Ornaments (`rajasthani.get_all_ornaments`)**:
  - `रखड़ी / बोरलो`: Forehead bell ornament.
  - `शीशफूल`: Floral crown medallions.
  - `नथ`: Nose ring with pearl chain.
  - `तिमणियो`: Three-tiered royal choker.
  - `हंसली`: Solid silver neck torque.
  - `बाजूबंद`: Upper armlet with meenakari.
  - `हाथीदांत रो चूड़ो`: Bridal ivory chooda.
  - `कंदोरो / तगड़ी`: Jingling silver waistbelt.
  - `आंवळा / नेवरी`: Heavy solid silver anklets.
  - `बिछिया`: Toe rings (silver only).

---

## 5. API Reference Summary
- `rajasthani.translate(text, source_lang="auto", dialect="mwr")`
- `rajasthani.hindi_to_rajasthani(sentence, dialect="mwr")`
- `rajasthani.conjugate(verb, tense="present", person="third", gender="masculine")`
- `rajasthani.lookup(word)` / `rajasthani.search(query)`
- `rajasthani.num_to_words(n)` / `rajasthani.to_devanagari_numerals(n)`
- `rajasthani.resolve_kinship(relation_query)`
- `rajasthani.get_all_rituals()` / `rajasthani.get_rituals_by_category(category)`
- `rajasthani.get_all_ornaments()` / `rajasthani.get_ornaments_by_body_part(part)`
- `rajasthani.get_architecture_elements()`, `rajasthani.get_instruments()`, `rajasthani.get_cuisine_dishes()`, `rajasthani.get_folk_deities()`, `rajasthani.get_heritage_places()`
- `rajasthani.run_server(port=8000)`
