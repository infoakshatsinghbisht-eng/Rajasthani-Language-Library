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
Downloaded full-text transcripts stored in `data_sources/raw_texts/` (over 13.3 MB primary text data across 16 foundational texts):
1. `grierson_lsi_vol9_rajasthani_1908.txt` (1.03 MB): *LSI Vol. IX Part II: Rajasthani & Gujarati*, Sir George Grierson.
2. `maheshwari_rajasthani_bhasha_sahitya_1960.txt` (2.15 MB): *Rajasthani Bhasha Aur Sahitya*, Dr. Hiralal Maheshwari.
3. `chatterji_rajasthani_bhasha_1949.txt` (107 KB): *Rajasthani Bhasha*, Dr. Suniti Kumar Chatterji.
4. `bhati_dingal_kosh_1978.txt` (788 KB): *Dingal Kosh*, Dr. Narayansingh Bhati.
5. `ramkrishan_hindi_rajasthani_tulnatmak_1977.txt` (780 KB): *Hindi Aur Rajasthani Bhasha Ka Tulnatmak Adhyan*, Dr. Ramkrishan Sharma.
6. `saraswat_dingal_geet_1960.txt` (445 KB): *Dingal Geet*, Rawat Saraswat.
7. `bhati_dingal_geet_sahitya_1961.txt` (1.41 MB): *Dingal Geet Sahitya*, Dr. Narayansingh Bhati.
8. `chandra_singh_loo_1955.txt` (78 KB): *Loo (Rajasthani Bhasha Ka Ritu Kavya)*, Chandra Singh Birbhadur.
9. `menariya_rajasthani_rooprekha_1953.txt` (254 KB): *Rajasthani Bhasha Ki Rooprekha*, Purushottam Menariya.
10. `bhati_rajasthani_madhyakal_1954.txt` (1.77 MB): *Rajasthani Sahitya Ka Madhyakal*, Dr. Narayansingh Bhati.
11. `prabhakar_sahitya_sanskriti_1968.txt` (699 KB): *Rajasthani Sahitya Aur Sanskriti*, Manohar Prabhakar.
12. `in.ernet.dli.2015.321330_2015.321330.Rajasthani-Bhasha_djvu.txt` (1.35 MB): *Rajasthani Bhasha Aur Sahitya*, Dr. Narayansingh Bhati.
13. `in.ernet.dli.2015.442115_2015.442115.Rajasthani-Bhasha_djvu.txt` (564 KB): *Rajasthani Bhasha, Sahitya, Sanskriti*, Dr. Ramprasad Dadhich (1986).
14. `in.ernet.dli.2015.308914_2015.308914.Rajasthani-Bhasha_djvu.txt` (2.11 MB): *Rajasthani Bhasha Aur Sahitya (Vol II)*.
15. `in.ernet.dli.2015.325506_2015.325506.Loo-rajasthani_djvu.txt` (78 KB): *Loo Ritu Kavya Edition II*.
16. `in.ernet.dli.2015.348572_2015.348572.Rajasthani-Bhasha_djvu.txt` (254 KB): *Rajasthani Bhasha Manyta Ka Prasan*.

---

## 4. Traditional Lifecycle Rituals & Cultural Encyclopedia
- **Pregnancy & Natal Rites (8 categories)**:
  - सीमंतोन्नयन / अग्यारणी / आठवां (Agharni / Aathwan - 8th month pregnancy ceremony)
  - सांथी रो मांडणो (Swastika & protective neem leaves threshold ritual)
  - छठी पूजन (Vidhata / Bemata destiny inscription on 6th night)
  - नामकरण संस्कार (Astrological constellation naming rite)
  - कुआँ पूजन / जलवा पूजन (Post-partum water goddess veneration)
  - जड़ूलो (Kuldevi temple tonsure/mundan)
  - ढूंढ़ (First Holi protective rite by Mama)
  - कर्णवेध (Acupressure ear-piercing for gold murki/bali)
- **Wedding Ceremonies (14 categories)**:
  - सगाई / रोक (Betrothal), टीका / दस्तूर (Chivalric engagement), लगन पत्रिका (Astrological letter)
  - चाक पूजना (Potter's wheel ceremony), बान बैठना अर पीठी (Haldi ubtan purification)
  - माहेरो / भात (Maternal uncle financial and chunari offering), रातीजोगा (Matriarch night vigil)
  - बिंदौरी / बन्दोली (Horseback procession), सामेला (Barat reception), तोरण मारना (Heroic archway strike)
  - हथलेवा (Sacred hand joining), फेरा अर सप्तपदी (Seven circumambulations), सीख अर विदाई (Bridal farewell)
  - कंकण-डोरा खोलना अर जुआ-जुई (Post-wedding bonding games), पगफेरा / मुकलावा (First homecoming)
- **Seasonal Folk Observances**:
  - गणगौर (Isar-Gauri worship), तीज (Hariyali & Kajli Teej), शीतला अष्टमी (Basoda / cold food feast)
  - आखा तीज (Agricultural new year & Khichda), बछ बारस (Cow-calf veneration), गोगा नवमी, तेजा दशमी, रामदेवरा यात्रा.
- **Traditional Ornaments & Jewelry (40+ items)**:
  - Head/Forehead: रखड़ी / बोरलो, शीशफूल, मेमंद, टीकी, दामिनी / तावित, सांकळी.
  - Ears: झुमका, कर्णफूल, ओगण्या, सुरलिया, पीपलपत्ता, टोटी, झेला, मुरकी (men's earring).
  - Nose: नथ, बेसरी (Bani Thani style), लोंग, कांटा, चुन्नी / फीणी.
  - Neck: आड़ (Rajputi square choker), तिमणियो, चंपाकली, मांदळियो, हंसली, कंठी, गलपट्टा, मोहनमाला / चंदनहार, तुलसी.
  - Arms & Wrists: बाजूबंद, टड्डा / अणत, हाथीदांत रो चूड़ो, गोखरू, बंगड़ी, पाटला, नौगरी, पूंछी, हथफूल.
  - Fingers: अरसी (thumb mirror ring!), बीटी / मूंदड़ी, छल्ला.
  - Waist: कंदोरो / तगड़ी, करधनी, सटका, कणकती.
  - Feet & Ankles (pure silver): पायल / झांझर, आंवळा, नेवरी, रमझोल, तोड़ा, लंगर, बिछिया, फोलरी, चुटकी, हीरनासैन.

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
- `GET /api/dictionary?q=...` - Full-text lexicon search
- `GET /api/numbers?val=...` - Number to Devanagari words & digits
- `GET /api/rituals?category=...` - Traditional lifecycle rituals
- `GET /api/ornaments?part=...` - Traditional head-to-toe jewelry
- `GET /api/syntax` - Structured syntax, split-ergativity, and dialect rules
- `GET /api/corpus` - Catalog of 16 digitized historical texts
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
