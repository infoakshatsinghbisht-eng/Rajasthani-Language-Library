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

### Rule 7: Past Counterfactual Conditionals (हेतुहेतुमद्भाव)
Constructs unfulfilled historical or hypothetical past conditions:
- `जे मेह बरसतो, तो अकाल नीं पड़तो।` *(If it had rained, there would have been no famine).*
Use `rajasthani.build_counterfactual_conditional(condition_clause, consequence_clause)`.

### Rule 8: Imperative Directives & Politeness Registers
Four distinct social honorific tiers:
- `intimate` (तूं): `तूं लिख` / negative: `तूं मती लिख`
- `familiar` (तूं/थे): `तूं लिखो`
- `polite` (थे): `थे लिखो` / `थे बांचो`
- `honorific` (आप / हुकम): `आप विराजो सा` / `आप आरोगो सा` / `आप पधारो सा`
Use `rajasthani.build_imperative(verb, politeness_level, negative)`.

### Rule 9: Benedictions, Wishes & Optatives (आशीर्वचन)
Constructs auspicious blessings and desires:
- `भगवान थारो भलो करै!` *(May God bless you!)*
Use `rajasthani.build_optative(subject, verb_phrase, blessing=True)`.

### Rule 10: Classical Vat Narrative Story Builder (वात री बनावट)
Generates historical story discourse opening, body, and moral closure:
- `"एक समै री बात है। मरुधर देस मांय एक शूरवीर रजपूत रह्वै थो। तद उण धर्म री रक्षा खातर सीस कटाय दियो। कथा पूरी भई, आनंद मंगल भयो।"`
Use `rajasthani.build_vat_narrative(protagonist, setting, deed)`.

### Rule 11: Synthetic Passive Voice (`-ईजै` / `-इजै`)
Transforms active sentences into passive or impersonal voice:
- `राम पोथी बांचै है` $\rightarrow$ `राम सूं पोथी बंचीजै है`
- `म्हैं काम कियो` $\rightarrow$ `म्हारै सूं काम करीज्यो`
Use `rajasthani.transform_voice(sentence, target_voice="passive")`.

### Rule 12: Reduplicated Echo Words (अनुकरणवाचक शब्द)
Forms natural conversational echo formations:
- `रोटी` $\rightarrow$ `रोटी-ओटी`, `पाणी` $\rightarrow$ `पाणी-धाणी`, `चाय` $\rightarrow$ `चाय-वाय`
Use `rajasthani.build_echo_word(word)`.

### Rule 13: Absolute Expressive Superlatives (सघन विशेषण)
Expresses absolute qualities in classic folklore style:
- `धोळो` $\rightarrow$ `धोळो-धम्मक` *(dazzling snow-white)*
- `काळो` $\rightarrow$ `काळो-भम्मक` *(pitch obsidian-black)*
- `मीठो` $\rightarrow$ `मीठो-मध` *(honey sweet)*
- `रातो` $\rightarrow$ `रातो-पीळो` *(crimson-red / enraged)*
Use `rajasthani.intensify_adjective(adjective)`.

### Rule 14: Reported Speech in Vat Discourse (अप्रत्यक्ष कथन)
Transforms direct speech into indirect narrative reported speech:
- `राजा कह्यो कै वो काल जासी।`
Use `rajasthani.convert_reported_speech(speaker, direct_quote)`.

### Rule 15: Rhetorical Tag Questions (कथनोपकथन)
Appends authentic Rajasthani tag question particles:
- `थे चालो हो, नीं?` / `थे चालो हो कांईं?`
Use `rajasthani.build_rhetorical_question(statement, tag_type="neen"/"kani"/"ke")`.

### Rule 11: Absolute Expressive Superlatives (परम प्रकर्ष विशेषण)
Produces authentic reduplicated intensifying superlatives:
- `धोळो` $\rightarrow$ `धोळो-धम्मक` (dazzling milk-white)
- `काळो` $\rightarrow$ `काळो-भम्मक` (pitch-black)
- `पीळो` $\rightarrow$ `पीळो-पटक` (vibrant yellow)
- `रातो` $\rightarrow$ `रातो-चोळ` (deep vermilion blood-red)
- `मीठो` $\rightarrow$ `मीठो-मध` (honey-sweet)
- `खारो` $\rightarrow$ `खारो-खट` (briny saline)
- `कड़वो` $\rightarrow$ `कड़वो-झैर` (poisonous bitter)
Use `rajasthani.intensify_adjective(adjective)`.

### Rule 12: Reduplicated Echo Words (अनुकरणात्मक प्रतिध्वनि शब्द)
Derives traditional echo-reduplication where onset consonants shift to vowel/o- or dh-:
- `रोटी` $\rightarrow$ `रोटी-ओटी`
- `पाणी` $\rightarrow$ `पाणी-धाणी`
- `चाय` $\rightarrow$ `चाय-वाय`
Use `rajasthani.build_echo_word(word)`.

### Rule 13: Vat Narrative Reported Speech (आख्यानात्मक परोक्ष कथन)
Transforms direct speech into indirect narrative discourse as found in classical Vats:
- Direct: `राजा कह्यो, "म्हूँ काल जावूं।"`
- Reported: `राजा कह्यो कै वो काल जासी।`
Use `rajasthani.convert_reported_speech(speaker, direct_quote)`.

### Rule 14: Rhetorical Question Tags (अनुप्रश्नात्मक पद)
Appends colloquial Rajasthani pragmatic tag particles:
- Tag `neen`: `थे चालो हो, नीं?`
- Tag `kani`: `थे चालो हो कांईं?`
- Tag `ke`: `थे चालो हो के?`
Use `rajasthani.build_rhetorical_question(statement, tag_type)`.

### Rule 15: Royal Politeness & Deferential Register Elevation
Elevates basic sentences into royal / courtly Rajasthani address:
- Replaces basic verbs with royal verbs: `खावो/जीमो` $\rightarrow$ `आरोगो सा`, `बैठो` $\rightarrow$ `विराजो सा`, `आवो` $\rightarrow$ `पधारो सा`, `जावो` $\rightarrow$ `सिधावो सा`, `बोलो` $\rightarrow$ `फरमावो सा`, `सोवो` $\rightarrow$ `पोढो सा`.
- Injects honorific particles `सा` and `हुकम`.
Use `rajasthani.elevate_politeness(sentence, tier="royal")`.

### Rule 16: Dubitative & Speculative Mood (संदेहवाचक वाक्य)
Constructs authentic speculative sentences using Rajasthani modal markers:
- `शायद काल मेह बरसैला।`
- `कदाच वो काल आवै।`
- `हो सकै वो बात सांची होवै।`
- `जाणै इन्द्रदेव प्रसन्न होया होवै।`
Use `rajasthani.build_dubitative_sentence(proposition, mood_marker)`.

### Rule 17: Vat Narrative Discourse Connectives (कथा संयोजक)
Connects clauses into Vat prose discourse using classical connectives:
- Sequential: `तदन्तर` (`Clause 1। तदन्तर Clause 2।`)
- Consequential: `इण वास्तै` (`Clause 1, इण वास्तै Clause 2।`)
- Adversative: `पण` (`Clause 1, पण Clause 2।`)
- Simultaneous: `ज्यूं ही ... त्यूं ही` (`ज्यूं ही Clause 1, त्यूं ही Clause 2।`)
Use `rajasthani.connect_discourse(clauses, relation)`.

### Rule 18: Ergative Past Transitive Construction & Alignment
Generates complete split-ergative clauses in past transitive contexts:
- Assigns ergative postposition `नै` or oblique pronoun (`म्हैं`, `तैं`, `उण`, `ईं`).
- Ensures the verb strictly agrees with the Direct Object in gender and number.
Use `rajasthani.apply_ergative_construction(subject, direct_object, verb, obj_gender, obj_number)`.

### Rule 19: Adverbial Manner Correlatives (रीतिवाचक सापेक्ष वाक्य)
Constructs correlative clauses of manner using classical `जियां... तियां`:
- Formula: `जियां <manner>, तियां <result>।`
- Example: `जियां कह्यो, तियां कर्यो।`
Use `rajasthani.build_manner_correlative(manner_clause, result_clause)`.

### Rule 20: Habitual & Frequentative Aspect (अभ्यासवाचक पक्ष)
Constructs habitual aspectual sentences using infinitive stems combined with `-वा लाग्यो`:
- Example: `वो रोज सवेरै पोथी बांचवा लाग्यो।`
Use `rajasthani.build_habitual_aspect(subject, verb, object_noun, frequency)`.

### Rule 21: Interrogative Question Transformations (प्रश्नात्मक वाक्य रूपांतरण)
Transforms declarative sentences into polar (yes/no) or content (wh-) interrogatives:
- Polar: `कांईं राम पोथी पढ़ै है?`
- Content When: `राम कद जासी?`
- Content Who: `कूण काल जासी?`
- Content Where: `राम कठे जासी?`
Use `rajasthani.transform_interrogative(sentence, question_type, target_element)`.

### Rule 22: Protective Negative Optatives (अपशकुन निवारक आशीर्वाद)
Constructs protective benedictions warding off calamity:
- Example: `भगवान थारो रो बुरो नीं करै!`
Use `rajasthani.build_negative_optative(target, calamity)`.

### Rule 23: Compound Postposition Synthesis (संयुक्त परसर्ग)
Synthesizes complex compound postpositions attached to oblique stems:
- `रै सागै` (along with: `राम रै सागै`)
- `रै कारणै` (because of: `बरसात रै कारणै`)
- `रै बिना` (without: `पाणी रै बिना`)
- `रै खातर` (for the sake of: `मातृभूमि रै खातर`)
- `रै बद्लै` (instead of: `गेहूँ रै बद्लै`)
Use `rajasthani.attach_compound_postposition(noun, postposition)`.

---

## 3. Digitized Primary Corpus Sources (56 Files, ~64.02 MB, 53 Cataloged Works)
All full-text transcripts are indexed in `data_sources/corpus_catalog.json` and stored in `data_sources/raw_texts/`:
1. `in.ernet.dli.2015.348143_sitaram_lalas_rajasthani_shabdkosh_vol4.txt` (8.67 MB): *Rajasthani Shabdkosh (Vol IV)*, Dr. Sitaram Lalas.
2. `in.ernet.dli.2015.345984_sitaram_lalas_rajasthani_sabad_kos_vol2_pt1.txt` (7.18 MB): *Rajasthani Sabad Kos (Part 2-1)*, Dr. Sitaram Lalas.
3. `in.ernet.dli.2015.345971_sitaram_lalas_rajasthani_sabad_kos_vol2.txt` (6.05 MB): *Rajasthani Sabad Kos (Part 2-2)*, Dr. Sitaram Lalas.
4. `in.ernet.dli.2015.348199_2015.348199.Dhola-Maru_djvu.txt` (2.16 MB): *Dhola Maru Ra Dhoha*, Dr. Bhagwati Lal Rajpurohit.
5. `maheshwari_rajasthani_bhasha_sahitya_1960.txt` (2.15 MB): *Rajasthani Bhasha Aur Sahitya*, Dr. Hiralal Maheshwari.
6. `in.ernet.dli.2015.464090_detha_dictionary_rajasthani_proverbs.txt` (2.01 MB): *A Dictionary Of Rajasthani Proverbs*, Bijaydan Detha "Biji".
7. `in.ernet.dli.2015.400763_rajasthani_kahawat_kosh.txt` (1.83 MB): *Rajasthani Kahawat Kosh*, Bhagirath Kanoria.
8. `bhati_rajasthani_madhyakal_1954.txt` (1.77 MB): *Rajasthani Sahitya Ka Madhyakal*, Dr. Narayansingh Bhati.
9. `in.ernet.dli.2015.314052_2015.314052.Kanhadade-Prabandha_djvu.txt` (1.75 MB): *Kanhadade Prabandha (Vol 1)*, Kavi Padmanabha.
10. `in.ernet.dli.2015.443912_2015.443912.Rajasthani-Lok_djvu.txt` (1.69 MB): *Rajasthani Lok Sahitya Ki Saidhanti Vivechna*, Sohandan Charan.
11. `in.ernet.dli.2015.345924_prakrit_apbransh_dingal_prabhav.txt` (1.63 MB): *Prakrit Aur Apbransh Ka Dingal Sahitya Par Prabhav*, Dr. Govardhan Sharma.
12. `bhati_dingal_geet_sahitya_1961.txt` (1.41 MB): *Dingal Geet Sahitya*, Dr. Narayansingh Bhati.
13. `in.ernet.dli.2015.321330_2015.321330.Rajasthani-Bhasha_djvu.txt` (1.35 MB): *Rajasthani Bhasha Aur Sahitya*, Dr. Narayansingh Bhati.
14. `in.ernet.dli.2015.444415_marwari_vyapari.txt` (1.23 MB): *Marwari Vyapari*, Giriraj Shankar Sharma.
15. `in.ernet.dli.2015.445998_rajasthani_gadh_vikas_aur_prakash_pt1.txt` (1.19 MB): *Rajasthani Gadh Vikas Aur Prakash Bhag 1*, Dr. Narendra Bhanawat.
16. `in.ernet.dli.2015.545356_2015.545356.Krisan-Rukmani-Ri-Veli_djvu.txt` (1.15 MB): *Veli Krisan Rukmani Ri*, Rathore Prithviraj / Swami Narottamdas.
17. `in.ernet.dli.2015.347988_rajasthani_sahitya_kosh_chand.txt` (1.13 MB): *Rajasthani Sahitya Kosh (Chhand Shastra)*, Dr. Narayansingh Bhati.
18. `in.ernet.dli.2015.442001_rajasthan_ke_aitihasik_granth_sarvekshan.txt` (1.12 MB): *Rajasthan Ke Aitihasik Granthon Ka Sarvekshana*, Dr. Narayansingh Bhati.
19. `in.ernet.dli.2015.347791_parmpara_rajasthani_baat_sangrah.txt` (1.08 MB): *Parmpara Rajasthani Baat-Sangrah*, Dr. Narayansingh Bhati.
20. `in.ernet.dli.2015.309699_rajasthani_vratkathae_purohit.txt` (1.04 MB): *Rajasthani Vratkathae*, Mohanlal Purohit.
21. `grierson_lsi_vol9_rajasthani_1908.txt` (1.03 MB): *LSI Vol. IX Part II: Rajasthani & Gujarati*, Sir George Grierson.
22. `in.ernet.dli.2015.380463_...txt` (1.01 MB): *Veer Satsai*, Mahakavi Suryamal Misran.
23. `padam_bhagat_rukamani_mangal_harji_ro_vyambalo_1977.txt` (1.00 MB): *Rukamani Mangal & Harji Ro Vyambalo*, Padam Bhagat.
24. `in.ernet.dli.2015.538962_rajasthani_gadhya_sahitya_udbhava_vikas.txt` (924 KB): *Rajasthani Gadhya-Sahitya Udbhava Aur Vikas*, Dr. Shivswaroop Sharma.
25. `in.ernet.dli.2015.306886_parampra_dingal_kosh.txt` (848 KB): *Parampra Dingal Kosh*, Dr. Narayansingh Bhati.
26. `in.ernet.dli.2015.308999_rajasthani_sahitya_adi_kal.txt` (818 KB): *Rajasthani Sahitya Ka Adi Kal*, Dr. Narayansingh Bhati.
27. `bhati_dingal_kosh_1978.txt` (788 KB): *Dingal Kosh*, Dr. Narayansingh Bhati.
28. `ramkrishan_hindi_rajasthani_tulnatmak_1977.txt` (780 KB): *Hindi Aur Rajasthani Bhasha Ka Tulnatmak Adhyan*.
29. `in.ernet.dli.2015.308096_...txt` (776 KB): *Rajasthani Vat Sahitya*, Dr. Poonam Daiya.
30. `prabhakar_sahitya_sanskriti_1968.txt` (699 KB): *Rajasthani Sahitya Aur Sanskriti*, Manohar Prabhakar.
31. `in.ernet.dli.2015.539046_dingal_me_veer_ras.txt` (622 KB): *Dingal Me Veer Ras*, Motilal Menariya.
32. `in.ernet.dli.2015.443973_rajasthani_sanskrati_ra_chitram_mehar.txt` (590 KB): *Rajasthani Sanskrati Ra Chitram*, Jahur Khan Mehar.
33. `in.ernet.dli.2015.442115_...txt` (577 KB): *Rajasthani Bhasha, Sahitya, Sanskriti*, Dr. Ramprasad Dadhich.
34. `in.ernet.dli.2015.444852_dalpat_vilas_rawat_saraswat.txt` (544 KB): *Dalpat Vilas*, Rawat Saraswat.
35. `in.ernet.dli.2015.443965_...txt` (539 KB): *Rajasthani Lok Sahitya Adhyan Ke Aayam*, Dr. Ramprasad Dadhich.
36. `in.ernet.dli.2015.442351_parampra_mataji_ri_vachnika.txt` (477 KB): *Parampra - Mataji Ri Vachnika*, Jaychandra Jati.
37. `saraswat_dingal_geet_1960.txt` (446 KB): *Dingal Geet*, Rawat Saraswat.
38. `in.ernet.dli.2015.443715_sadayvts_veer_prabandh.txt` (414 KB): *Sadayvts Veer Prabandh*, Dr. Manjulal Majmudar.
39. `in.ernet.dli.2015.444198_...txt` (395 KB): *Rajasthani Nibandh*, Manohar Sharma.
40. `tessitori_veli_krisana_rukamani_ri_asiatic_1919.txt` (390 KB): *Veli Krisana Rukamani Ri (Asiatic Society Edition)*, Dr. L.P. Tessitori.
41. `in.ernet.dli.2015.444365_...txt` (363 KB): *Rajasthani Kahani Sangrah (Jaagati Jot)*, Ramesh Dayal.
42. `in.ernet.dli.2015.309837_rajasthani_bhag1_narottamdas_swami.txt` (361 KB): *Rajasthani (Bhag 1)*, Swami Narottamdas.
43. `in.ernet.dli.2015.444217_rajasthan_ke_kavi_rawat_saraswat.txt` (334 KB): *Rajasthan Ke Kavi*, Rawat Saraswat.
44. `in.ernet.dli.2015.401029_rajasthani_bheel_geet_pt2_sharma.txt` (331 KB): *Rajasthani Bheel Geet (Part 2)*, Giridhar Sharma.
45. `in.ernet.dli.2015.444215_rohidai_ra_phool_manohar_sharma.txt` (308 KB): *Rohidai Ra Phool*, Dr. Manohar Sharma.
46. `narsi_mehta_ka_bada_mamera_marwari.txt` (294 KB): *Narsi Mehta Ka Bada Mamera*, Ram Ratan Darak.
47. `in.ernet.dli.2015.307534_rajasthani_lokotsav_gindaram_varma.txt` (268 KB): *Rajasthani Lokotsav*, Gindaram Varma.
48. `in.ernet.dli.2015.550743_rajasthani_padh_sangrah_komal_kothari.txt` (256 KB): *Rajasthani Padh Sangrah*, Komal Kothari.
49. `menariya_rajasthani_rooprekha_1953.txt` (254 KB): *Rajasthani Bhasha Ki Rooprekha*, Purushottam Menariya.
50. `tessitori_vithu_sujo_chanda_rau_jeta_si_ro_1920.txt` (232 KB): *Chhanda Rau Jeta Si Ro*, Vithu Sujo / Dr. L.P. Tessitori.
51. `in.ernet.dli.2015.547214_hadi_shatak_nathusingh_mahiyariya.txt` (146 KB): *Hadi Shatak*, Kavi Nathusingh Mahiyariya.
52. `chatterji_rajasthani_bhasha_1949.txt` (108 KB): *Rajasthani Bhasha*, Dr. Suniti Kumar Chatterji.
53. `chandra_singh_loo_1955.txt` (78 KB): *Loo (Ritu Kavya)*, Chandra Singh Birbhadur.
*(Total corpus: 56 files, 64.02 MB / 67,127,827 bytes across 53 cataloged works).*

---

## 4. Lexicon, Folklore & Cultural Heritage
- **Lexicon**: **1,813+ fully verified lemmas** with Devanagari, IAST romanization, detailed English meaning, Hindi gloss, grammatical POS, gender, dialect, and illustrative example sentences across 55+ domains.
- **Idioms (मुहावरा)**: **60 authentic idioms** with cultural contexts.
- **Proverbs (कहावत / औखाणा)**: **60 traditional proverbs** with translations and contexts.
- **Riddles (आड़ी / बुझावळ)**: **25 traditional riddles** with solutions and cultural metaphors.
- **Lifecycle Rituals (36 items)**: Birth, childhood, marriage, seasonal fasts, and memorial rites (`मायरो/भात`, `सामेलो`, `तोरण मारणो`, `बान बैठणो`, `रातीजगो`, `हथलेवो`, `कंकण-डोरा खोलणो`, `सीख/विदाई`, `मुकलावो`).
- **Traditional Ornaments (53 items)**: Head to toe (`रखड़ी`, `बोरलो`, `शीशफूल`, `मेमंद`, `नथ`, `बेसरी`, `आड़`, `तिमणियो`, `चंपाकली`, `हंसली`, `बाजूबंद`, `हाथीदांत रो चूड़ो`, `गोखरू`, `अरसी`, `कंदोरो`, `आंवळा`, `नेवरी`, `रमझोल`, `बिछिया`).
- **Extended Kinship (58 relations)**: Patrilineal, matrilineal, affinal, sworn, and ceremonial roles.
- **Traditional Ornaments (53 items)**: Head to toe (`रखड़ी`, `बोरलो`, `शीशफूल`, `मेमंद`, `नथ`, `बेसरी`, `आड़`, `तिमणियो`, `चंपाकली`, `हंसली`, `बाजूबंद`, `हाथीदांत रो चूड़ो`, `गोखरू`, `अरसी`, `कंदोरो`, `आंवळा`, `नेवरी`, `रमझोल`, `बिछिया`).
- **Extended Kinship (58 relations)**: Patrilineal, matrilineal, affinal, sworn, and ceremonial roles.

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
- `GET /api/dictionary?q=...` - Full-text lexicon search (1,204+ words)
- `GET /api/numbers?val=...` - Number to Devanagari words & digits
- `GET /api/rituals?category=...` - Traditional lifecycle rituals (36 entries)
- `GET /api/ornaments?part=...` - Traditional jewelry (53 entries)
- `GET /api/syntax` - Structured syntax, split-ergativity, causatives, and dialect rules
- `GET /api/corpus` - Catalog of 40 digitized historical texts (48.72 MB)
- `GET /api/idioms` - Authentic idioms and sayings (52 entries)
- `GET /api/folklore` - Folk proverbs and riddles (62 entries)

---

## 6. Python API Reference
```python
import rajasthani

# 1. Dictionary & Lexicon (1,204+ words)
w = rajasthani.lookup("सांग")
print(w.english)  # "traditional Rajput iron lance or javelin wielded on horseback"

# 2. Syntax & Sentence Construction
s = rajasthani.hindi_to_rajasthani("मैं पानी पी रहा था", dialect=rajasthani.Dialect.MARWARI)
# -> "म्हूँ पाणी पी रह्यो थो"

# 3. Compound Verbs
cv = rajasthani.build_compound_verb("खाणो", vector_verb="लेणो", tense=rajasthani.Tense.PAST)
# -> "खाय लियो"

# 4. Complex Correlatives & Counterfactuals
sent = rajasthani.build_complex_sentence("मेह बरस्यो", "फसल चोखी व्हैला", connector_type="conditional")
# -> "जे मेह बरस्यो, तो फसल चोखी व्हैला।"

cf = rajasthani.build_counterfactual_conditional("मेह बरसतो", "अकाल नीं पड़तो")
# -> "जे मेह बरसतो, तो अकाल नीं पड़तो।"

# 5. Echo Words & Expressive Superlatives
echo = rajasthani.build_echo_word("रोटी")  # "रोटी-ओटी"
intl = rajasthani.intensify_adjective("धोळो")  # "धोळो-धम्मक"

# 6. Reported Speech & Rhetorical Questions
rep = rajasthani.convert_reported_speech("राजा", "म्हूँ काल जावूं")  # "राजा कह्यो कै वो काल जासी।"
rq = rajasthani.build_rhetorical_question("थे चालो हो", tag_type="neen")  # "थे चालो हो, नीं?"

# 7. Causatives & Imperatives
caus1 = rajasthani.generate_causative("करणो", level=1)  # "करावणो"
imp_royal = rajasthani.build_imperative("बैठणो", politeness_level="honorific")  # "आप विराजो सा"

# 8. Optatives & Folk Vat Narrative
blessing = rajasthani.build_optative("भगवान", "थारो भलो करै")  # "भगवान थारो भलो करै!"
vat = rajasthani.build_vat_narrative("राव जेतासी", "बीकानेर दुर्ग", "शत्रु दल नै परास्त कियो")

# 9. Clusivity & Passive Voice
incl = rajasthani.convert_clusivity("हम चालेंगे", inclusive=True)  # "आपां चालेंगे"
pass_sent = rajasthani.transform_voice("राम पोथी बांचै है")         # "राम रै हाथूं पोथी बंचीजै है।"
```
