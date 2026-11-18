# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

WORDS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "rajasthani", "lexicon", "data", "words.json")
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip() for w in words}

batch_extra = [
    ("कंत", "kant", "beloved husband, lord or master in classical poetry", "पति / स्वामी / प्रियतम", "noun", "m", "literature", "mwr", "कंत विदेस गयो मारू झूरै।"),
    ("गोरी", "gori", "radiant fair maiden, beautiful heroine of folk tales", "सुंदरी / गोरी / नायिका", "noun", "f", "literature", "mwr", "गोरी मुख सूं घूंघट खोल्यो।"),
    ("मारू", "maaru", "Princess Maru of Poogal, immortal romantic heroine of Thar", "मारू (ढोला की नायिका)", "noun", "f", "literature", "mwr", "मारू सांढणी री बाट जोवै।"),
    ("ढोला", "dhola", "Prince Dhola of Narwar, romantic hero of Rajasthani lore", "ढोला (प्रेमाख्यान का नायक)", "noun", "m", "literature", "mwr", "ढोला मारू कनै पूग्यो।"),
    ("सुहाग", "suhaag", "auspicious state of marital happiness and husband longevity", "सुहाग / सौभाग्य", "noun", "m", "culture", "mwr", "सुहाग री रक्षा खातर व्रत कियो।"),
    ("सिंदूर", "sindoor", "auspicious vermilion powder filled in hair parting", "सिंदूर", "noun", "m", "culture", "mwr", "मांग में सिंदूर पूर्यो।"),
    ("चूड़लो", "choodlo", "sacred ivory and lac bridal bangle set", "चूड़ा (हाथीदांत व लाख की चूड़ियां)", "noun", "m", "ornaments", "mwr", "हाथ में हाथीदांत रो चूड़लो पहर्यो।"),
    ("कागद", "kaagad", "written letter, love epistle or scroll sent with courier", "पत्र / चिट्ठी / पाती", "noun", "m", "literature", "mwr", "कागद लिख कर सांढणी वाळे ने दियो।"),
    ("धावड़ियो", "dhaavadiyo", "swift runner, royal post courier or highway traveler", "धावक / हरकारा / दूत", "noun", "m", "history", "mwr", "धावड़ियो समाचार ले कर आयो।"),
    ("कसूमळ", "kasoomal", "deep auspicious vermillion crimson color of joy and romance", "कसूमी / गहरा लाल रंग", "adjective", "m", "descriptors", "mwr", "कसूमळ रंग रो साफा बांध्यो।"),
    ("पीळो", "peelo", "radiant yellow hue of mustard blossoms and spring", "पीला रंग", "adjective", "m", "descriptors", "mwr", "पीळा रोहिड़े रा फूल।"),
    ("हरियो", "hariyo", "lush green color of fields after monsoon rains", "हरा रंग", "adjective", "m", "descriptors", "mwr", "हरिया खेत मन मोह लेवै।"),
    ("धोळो", "dholo", "pure pristine white color of milk and desert salt", "श्वेत / सफेद", "adjective", "m", "descriptors", "mwr", "धोळो संगमरमर चमकै।"),
    ("काळो", "kaalo", "deep obsidian black color of rainclouds", "काला रंग", "adjective", "m", "descriptors", "mwr", "काळा मेघ आभै में छाय गया।"),
    ("रातो", "raato", "fiery passionate ruby-red color of bridal attire", "लाल रंग", "adjective", "m", "descriptors", "mwr", "राती चुनड़ी ओढ़ कर लाडी आई।"),
    ("जामण", "jaaman", "biological mother who bore the child; venerated birth-giver", "जन्मदात्री मां", "noun", "f", "kinship", "mwr", "जामण जायो भाई सूं मोटो कोई नीं।"),
    ("जणणी", "janani", "revered mother / motherland", "माता / जननी", "noun", "f", "kinship", "mwr", "जणणी जण तो ऐड़ा जण, के दाता के सूर।"),
    ("बाबोसा", "baabosa", "reverent affectionate address for father", "पिताजी (बाबोसा)", "noun", "m", "kinship", "mwr", "बाबोसा रो हुकम मान्यो।"),
    ("जीजोसा", "jeejosa", "elder sister husband (brother-in-law)", "जीजाजी", "noun", "m", "kinship", "mwr", "जीजोसा ब्याव में आया।"),
    ("बाइसा", "baaisa", "affectionate noble address for daughter or princess", "पुत्री / बहन / बाईसा", "noun", "f", "kinship", "mwr", "बाइसा घणी लाडली है।"),
    ("भाभीसा", "bhaabhisa", "elder brother wife treated like mother", "भाभीजी", "noun", "f", "kinship", "mwr", "भाभीसा थाळी परोसी।"),
    ("काकोसा", "kaakosa", "paternal uncle (father younger brother)", "चाचाजी", "noun", "m", "kinship", "mwr", "काकोसा खेत संभाळ्यो।"),
    ("फूफोसा", "phoophosa", "father sister husband (paternal uncle)", "फूफाजी", "noun", "m", "kinship", "mwr", "फूफोसा नै साफा पहरायो।"),
    ("मासोसा", "maasosa", "mother sister husband (maternal uncle)", "मौसाजी", "noun", "m", "kinship", "mwr", "मासोसा गांव सूं आया।"),
    ("नानोसा", "naanosa", "maternal grandfather", "नानाजी", "noun", "m", "kinship", "mwr", "नानोसा दोहिते नै लाड कियो।"),
    ("नानीसा", "naanisa", "maternal grandmother", "नानीजी", "noun", "f", "kinship", "mwr", "नानीसा कथा सुणाई।"),
    ("मामीसा", "maamisa", "maternal uncle wife", "मामीजी", "noun", "f", "kinship", "mwr", "मामीसा मायरो सजायो।"),
    ("मामोसा", "maamosa", "maternal uncle (brother of mother)", "मामाजी", "noun", "m", "kinship", "mwr", "मामोसा भात भर्यो।"),
    ("समधीसा", "samdhisa", "child in-law father", "समधीजी", "noun", "m", "kinship", "mwr", "समधीसा सामेला में मिल्या।"),
    ("समधणसा", "samdhansa", "child in-law mother", "समधिन जी", "noun", "f", "kinship", "mwr", "समधणसा ने आदर दियो।"),
    ("पगल्यो", "pagalyo", "auspicious first footprint stamp of newborn or bride entering home", "पगल्या (कुंकुम पद-चिह्न)", "noun", "m", "rituals", "mwr", "लक्ष्मी ज्यूं लाडी रा पगल्यो पड़्या।"),
    ("घूघरी", "ghooghari", "boiled spiced wheat or gram distributed upon childbirth or Teej", "घूघरी (मांगलिक प्रसाद)", "noun", "f", "food", "mwr", "पुत्र जन्म माथे घूघरी बांटी।"),
    ("ढूंढ", "dhoondh", "first Holi ceremonial celebration and blessing for newborn infant", "ढूंढ (प्रथम होली उत्सव)", "noun", "f", "rituals", "mwr", "बालक री ढूंढ पूजी।"),
    ("बिंदोळी", "bindoli", "pre-wedding festive horse-riding procession honoring bride or groom across town", "बिंदोली (वर/वधू की सवारी)", "noun", "f", "rituals", "mwr", "गाजे-बाजे सूं वर री बिंदोळी निकळी।"),
    ("बान-बैठणो", "baan-baithano", "commencing ceremonial turmeric application and pre-wedding seclusion", "बान बैठना (हल्दी रस्म आरंभ)", "noun", "m", "rituals", "mwr", "शुभ मुहूर्त में बान बैठ्यो।"),
    ("चाक-पूजणो", "chaak-poojano", "worship of potter wheel to obtain auspicious earthen pots for marriage", "चाक पूजन (कुम्हार के चाक की पूजा)", "noun", "m", "rituals", "mwr", "स्त्रियां मंगल गावत चाक पूजण गईं।"),
    ("रातीजगो", "raatijago_vigil", "all-night community prayer and singing vigil by village women", "रातीजगा (रात भर मंगल गायन)", "noun", "m", "rituals", "mwr", "ब्याव री पहली रात नै रातीजगो होयो।"),
    ("निकासी", "nikaasi_procession", "departure of the groom riding mare from his home towards bride village", "निकासी (दूल्हे की रवानगी)", "noun", "f", "rituals", "mwr", "घोड़ी माथे बैठ कर दूल्हे री निकासी हुई।"),
    ("बरियात", "bariyaat", "wedding guest party accompanying the groom", "बारात (बरियात)", "noun", "f", "rituals", "mwr", "बरियात गांव रै कांकड़ पूगी।"),
    ("पहरावणी", "pahraavni", "traditional gifting of garments and turbans to departed wedding guests", "पहरावनी (विदाई पर वस्त्र उपहार)", "noun", "f", "rituals", "mwr", "समधियों ने पहरावणी दीनी।"),
    ("रंग-बरी", "rang-bari", "presentation of bridal trousseau and ornaments by groom family to bride", "रंग-बरी (वधू पक्ष को शृंगार भेंट)", "noun", "f", "rituals", "mwr", "रंग-बरी में सोने रा गहणा आया।"),
    ("सीख-मनवार", "seekh-manvaar", "farewell hospitality and blessings", "सीख-मनुहार", "noun", "f", "rituals", "mwr", "सीख-मनवार सूं विदा कियो।"),
    ("कुंकुम-पत्री", "kunkum-patri", "traditional sacred wedding invitation inscribed with saffron and vermilion", "कुंकुम-पत्रिका (विवाह निमंत्रण पत्र)", "noun", "f", "rituals", "mwr", "गणेश जी नै पहली कुंकुम-पत्री भेजी।"),
    ("छाब", "chhaab", "large round woven bamboo platter basket carrying bridal gifts", "छाब (विवाह की डलिया / उपहार टोकरा)", "noun", "f", "rituals", "mwr", "मायरे री छाब सजाई।"),
    ("भाटी", "bhati", "rulers of Jaisalmer descending from Lunar dynasty", "भाटी (जैसलमेर का यदुवंशी राजवंश)", "noun", "m", "history", "mwr", "भाटी शासकां जैसलमेर दुर्ग बणायो।"),
    ("राठौड़", "rathore", "illustrious Suryavanshi Rajput clan ruling Marwar, Bikaner, and Kishangarh", "राठौड़ (मारवाड़ का राजवंश)", "noun", "m", "history", "mwr", "राठौड़ां रो शौर्य विख्यात है।"),
    ("सीसोदिया", "sisodia", "illustrious solar clan of Mewar sovereigns ruling from Chittor and Udaipur", "सिसोदिया (मेवाड़ का सूर्यवंशी राजवंश)", "noun", "m", "history", "mwi", "सिसोदिया महाराणावां स्वतंत्रता री रक्षा करी।"),
    ("कछवाहा", "kachhwaha", "solar dynasty ruling Dhundhar (Amer and Jaipur)", "कछवाहा (आमेर-जयपुर का राजवंश)", "noun", "m", "history", "dhd", "कछवाहा राजावां जयपुर बसायो।"),
    ("हाड़ा", "haada", "valiant Chauhan branch ruling Hadoti (Bundi and Kota)", "हाड़ा (हाड़ौती का चौहान वंश)", "noun", "m", "history", "hrt", "हाड़ा वीरां री तलवार प्रसिद्ध है।"),
    ("झाला", "jhaala", "noble Rajput clan known for heroic sacrifice at Haldighati (Jhala Manna)", "झाला (त्यागी व वीर राजवंश)", "noun", "m", "history", "mwi", "झाला मन्ना महाराणा प्रताप रो मुकुट पहर कर लड़्या।"),
    ("खींवसर दुर्ग", "kheemsar durg", "historic sand-fort fortress in Nagaur desert", "खींवसर दुर्ग", "noun", "m", "architecture", "mwr", "रेत रै टीलां रै बीच खींवसर दुर्ग चमकै।")
]

count = 0
for r, rom, eng, hin, pos, gen, cat, dia, ex in batch_extra:
    if r not in existing:
        words.append({
            "rajasthani": r,
            "roman": rom,
            "english": eng,
            "hindi": hin,
            "pos": pos,
            "gender": gen,
            "category": cat,
            "dialect": dia,
            "example": ex
        })
        existing.add(r)
        count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Successfully added {count} extra words. Grand total vocabulary now: {len(words)}")
