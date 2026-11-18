# -*- coding: utf-8 -*-
"""
Expand Mega Lexicon to 750+ / 800+ Verified Words
=================================================
Injects curated lexical domains across:
1. Occupations & Crafts (दस्तकारी अर पेशा)
2. Body Parts & Anatomy (शरीर रा अंग)
3. Household Tools & Utensils (घर-गृहस्थी रा बरतन अर सामान)
4. Domestic Architecture (घर-मकान रा भाग)
5. Flora, Fauna & Birds (रूख, चिड़कली अर पंछी)
6. Tastes, Sensations & Colors (स्वाद, रंग अर अहसास)
7. Time, Measurements & Units (बखत, नाप अर तोल)
8. Fasts, Festivals & Vows (बरत, त्योहार अर नेम)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_keys = {w["rajasthani"] for w in existing_words}
print(f"Existing words in database: {len(existing_words)}")

MEGA_ENTRIES = [
    # =========================================================================
    # 1. TRADITIONAL OCCUPATIONS & ARTISAN GUILDS (पेशा अर दस्तकारी)
    # =========================================================================
    ("कुम्हार / कुंभार", "kumhaar / kumbhaar", "traditional village potter molding earthen pots on chalk wheel", "कुम्हार / प्रजापति", "noun", "m", "crafts", "general", "कुम्हार चाक माथे सुंदर मटकियां बणावै।"),
    ("लुहार", "luhaar", "blacksmith forging iron agricultural tools, sickles, and horseshoes", "लोहार", "noun", "m", "crafts", "general", "लुहार भट्टी मांय दांती अर कुल्हाड़ी गढ़ै।"),
    ("सोनी / सुनार", "soni / sunaar", "goldsmith crafting kundan, meenakari, and traditional ornaments", "सुनार / स्वर्णकार", "noun", "m", "crafts", "general", "सोनी जी रखड़ी माथे बारीक नक्काशी कीधी।"),
    ("खाती", "khaati", "traditional carpenter fabricating wooden ploughs, doors, and chariots", "बढ़ई / सुथार / खाती", "noun", "m", "crafts", "general", "खाती सा शीशम री लाकड़ी सूं किवाड़ बणायो।"),
    ("रंगरेज / नीलगर", "rangrej / neelgar", "traditional textile dyer mastering tie-dye, bandhej, and indigo vats", "रंगरेज (कपड़ा रंगने वाला)", "noun", "m", "crafts", "general", "रंगरेज चुनड़ी नै चटक पीळे रंग मांय रंगी।"),
    ("छिंपा", "chhimpa", "traditional hand block printer printing Sanganeri and Bagru textiles", "छीपा (ठप्पा छपाई कारीगर)", "noun", "m", "crafts", "general", "छिंपा काष्ठ रे ठप्पों सूं चादर माथे फूल मांड्या।"),
    ("तेली", "teli", "traditional oil-presser operating the bullock-drawn kolhu", "तेली (कोल्हू चलाने वाला)", "noun", "m", "crafts", "general", "तेली तिल अर सरसों रो तेल काढ़ै।"),
    ("नाई / सैन", "naai / sain", "traditional barber who also acts as matchmaker and ceremonial messenger", "नाई / हज्जाम / सैन", "noun", "m", "culture", "general", "नाई जी ब्याव रो लगन ले'र समधी रे घर गया।"),
    ("गाडोलिया लुहार", "gaadoliya luhaar", "nomadic cart-dwelling blacksmith artisans descending from Chittorgarh warriors", "गाडोलिया लोहार (घुमंतू लोहार)", "noun", "m", "culture", "general", "गाडोलिया लुहार बैलगाड़ी मांय आपरो संसार बसाय राखै।"),
    ("भोपा / भोपी", "bhopa / bhopi", "traditional folk priest and bard singing narrative ballad scrolls (Phad)", "भोपा-भोपी (फड़ वाचक)", "noun", "m", "culture", "general", "भोपाजी रावणहत्था री तान माथे पाबूजी री कथा सुणावै।"),
    ("भाट", "bhaat", "traditional family genealogist recording clan pedigrees on scrolls (पोथी)", "भाट (वंशावली लेखक)", "noun", "m", "culture", "general", "भाट जी बही-खाते मांय पूर्वजां रो इतिहास बांच्यो।"),
    ("बणजारा", "banjaara", "traditional nomadic desert trader transporting salt, grain, and cattle across caravan routes", "बंजारा (व्यापारी घुमंतू समुदाय)", "noun", "m", "culture", "general", "बणजारां रो काफिलो सांभर झील सूं लूण ले'र नीकळ्यो।"),

    # =========================================================================
    # 2. BODY PARTS & ANATOMY (शरीर रा अंग)
    # =========================================================================
    ("माथो", "maatho", "head, crown of head, forehead", "सिर / माथा", "noun", "m", "body", "general", "माथे माथे केसरिया साफा सज्यो है।"),
    ("आंख्यां / आंख", "aankhyaan / aankh", "eyes, vision, sight", "आँखें / नयन", "noun", "f", "body", "general", "मृगनयनी री आंख्यां मांय काजळ सोहै।"),
    ("कान", "kaan", "ear, hearing organ", "कान", "noun", "m", "body", "general", "कान मांय सोने री मुरकी पहरी।"),
    ("नाक", "naak", "nose, facial feature, symbol of dignity", "नाक", "noun", "f", "body", "general", "नाक मांय मोती जड़ी नथ झूलै।"),
    ("मूंह / मुखड़ो", "moonh / mukhado", "mouth, face, countenance", "मुंह / चेहरा", "noun", "m", "body", "general", "चांद जैसो मुखड़ो घूंघट मांय दीखै।"),
    ("होंठ / ओठ", "honth / oth", "lips", "होंठ / अधर", "noun", "m", "body", "general", "होंठ माथे मीठी मुस्कान खिली।"),
    ("दांत", "daant", "teeth", "दांत", "noun", "m", "body", "general", "दांत दाड़म रे बीज ज्यूं चमकै।"),
    ("जीभ", "jeebh", "tongue, speech organ", "जीभ / रसना", "noun", "f", "body", "general", "जीभ सूं सदा मीठे बोल बोलणा चाहिजै।"),
    ("खांदो", "khaando", "shoulder", "कंधा", "noun", "m", "body", "general", "खांदे माथे हळ उठा'र किसान चल्यो।"),
    ("छाती", "chhaati", "chest, bosom, bravery", "छाती / सीना", "noun", "f", "body", "general", "शूरवीर री छाती मांय भय कोनी व्है।"),
    ("पेट", "pet", "stomach, belly", "पेट", "noun", "m", "body", "general", "सोगरो खाण सूं पेट भर ग्यो।"),
    ("कमर", "kamar", "waist, loin", "कमर", "noun", "f", "body", "general", "कमर मांय चांदी रो कंदोरो रुणझुण बाजै।"),
    ("गोडो", "godo", "knee joint", "घुटना", "noun", "m", "body", "general", "लाम्बी दौड़ सूं गोडां मांय दरद हुयो।"),
    ("पग / पाँव", "pag / paanw", "foot, step, pace", "पैर / पाँव", "noun", "m", "body", "general", "पगां मांय चांदी री पाजेब पहरी।"),
    ("एड़ी", "edi", "heel of the foot", "एड़ी", "noun", "f", "body", "general", "एड़ी मांय महंदी रो रातो रंग लाग्यो।"),
    ("अंगूठो", "angutho", "thumb, big toe", "अंगूठा", "noun", "m", "body", "general", "अंगूठे मांय अरसी री मूंदड़ी पहरी।"),
    ("नूंह", "noonh", "finger-nail / toe-nail", "नाखून", "noun", "m", "body", "general", "नूंह साफ राखणा जरूरी हैं।"),
    ("हाड / हड्डी", "haad / haddi", "bone, skeleton, physical strength", "हड्डी", "noun", "m", "body", "general", "मेहनती मिनख रा हाड मजबूत व्है।"),
    ("चामड़ी", "chaamadi", "skin, hide", "त्वचा / चमड़ी", "noun", "f", "body", "general", "धूप मांय चामड़ी सांवळी पड़गी।"),

    # =========================================================================
    # 3. HOUSEHOLD TOOLS & UTENSILS (घर-गृहस्थी रा बरतन अर औजार)
    # =========================================================================
    ("दीवलो / दीवो", "deewalo / deewo", "small earthen clay oil lamp with cotton wick", "दीपक / दीया", "noun", "m", "household", "general", "संझा पड्यां देहरी माथे दीवलो बाळ्यो।"),
    ("बाती", "baati", "twisted cotton wick for oil lamp", "दीये की बत्ती", "noun", "f", "household", "general", "रुई री बाती तेल मांय भिगोई।"),
    ("हंडिया", "handiya", "small earthen cooking pot for simmering lentils and curries", "हांडी / छोटी मटकी", "noun", "f", "household", "general", "माटी री हंडिया मांय दाल स्वादिष्ट बणै।"),
    ("कटोरी", "katori", "small metal dining bowl", "कटोरी", "noun", "f", "household", "general", "कटोरी मांय देसी घी परोस द्यो।"),
    ("चमचो", "chamcho", "metal dining spoon or ladle", "चम्मच", "noun", "m", "household", "general", "चमचे सूं खीर खाई।"),
    ("चकला", "chakla", "circular wooden or marble rolling board for flatbreads", "चकला (रोटी बेलने का)", "noun", "m", "household", "general", "चकले माथे रोटी बेली।"),
    ("बेलन", "belan", "wooden rolling pin", "बेलन", "noun", "m", "household", "general", "बेलन सूं पूरियां बेली।"),
    ("चिमटो", "chimto", "iron tongs for flipping breads and tending embers", "चिमटा", "noun", "m", "household", "general", "चिमटे सूं चूल्हे री रोटी पलटी।"),
    ("संडासी", "sandaasi", "pincer tongs for grasping boiling hot pots", "सँड़सी (पतीला पकड़ने की)", "noun", "f", "household", "general", "संडासी सूं गरम तपीली उतारी।"),
    ("ओखळी", "okhali", "heavy stone or wooden mortar for pounding grain and spices", "ओखली / मूसली का पात्र", "noun", "f", "household", "general", "ओखळी मांय धान कूटीजै।"),
    ("मूसळ", "moosal", "heavy wooden pestle with iron collar for pounding", "मूसल", "noun", "m", "household", "general", "मूसळ सूं बाजरो कूूट्यो।"),
    ("सिल-बट्टो", "sil-batto", "flat granite grinding slab and hand pestle for spices", "सिल-बट्टा (मसाला पीसने का)", "noun", "m", "household", "general", "सिल-बट्टे माथे लहसण री चटनी पीसी।"),
    ("जांतो / घट्टी", "jaanto / ghattee", "traditional hand-turned stone rotary quern for grinding whole grains", "घट्टी / हाथ की चक्की", "noun", "m", "household", "general", "परभाते दादीजी जांतो चला'र आटो पीसती।"),

    # =========================================================================
    # 4. DOMESTIC ARCHITECTURE & HABITAT (घर-मकान रा भाग)
    # =========================================================================
    ("किवाड़", "kiwaad", "heavy carved wooden door leaf / shutter", "किवाड़ / दरवाजा", "noun", "m", "household", "general", "रात्यूं हवेली रा किवाड़ बंद कर्योड़ा हा।"),
    ("ताळो", "taalo", "iron padlock for securing gates and coffers", "ताला", "noun", "m", "household", "general", "ओबरे रे दरवाजे माथे ताळो लगायो।"),
    ("कूंजी", "koonji", "iron or brass key", "चाबी / कुंजी", "noun", "f", "household", "general", "तिजोरी री कूंजी सासूजी रे सटके मांय है।"),
    ("छज्जो", "chhajjo", "projecting stone cornice shielding balcony from sun and rain", "छज्जा", "noun", "m", "household", "general", "छज्जे माथे कबूतर बैठ्या हैं।"),
    ("जीणो", "jeeno", "flight of stone stairs leading to terrace or upper attic", "सीढ़ी / जीना", "noun", "m", "household", "general", "जीणे माथे चढ़'र छत माथे पूग्या।"),
    ("चारदीवारी / कोट", "chaardeewaari / kot", "perimeter defensive stone rampart enclosing residence", "चारदीवारी / प्राचीर", "noun", "f", "household", "general", "हवेली री चारदीवारी घणी ऊंची है।"),

    # =========================================================================
    # 5. DOMESTIC & WILD BIRDS (पंछी अर चिड़कली)
    # =========================================================================
    ("कागलो", "kaaglo", "black desert crow whistling portents of guest arrivals", "कौआ", "noun", "m", "animals", "general", "मुंडेर माथे कागलो बोलै, मेहमान आवैला।"),
    ("पारेवो / कबूतर", "paarewo / kabootar", "rock pigeon nesting in haveli niches and ramparts", "कबूतर / पारेवा", "noun", "m", "animals", "general", "पारेवो दाणा चुगबा आंगण मांय आयो।"),
    ("तोतो / सूओ", "toto / sooo", "green parakeet celebrated in Rajasthani romance ballads", "तोता / सुआ", "noun", "m", "animals", "general", "पींजरै मांय तोतो राम-राम बोलै।"),
    ("चिड़कली", "chidakali", "house sparrow chirping in thatched courtyards", "गौरैया / चिड़िया", "noun", "f", "animals", "general", "चिड़कली आंगण मांय फुदकै।"),
    ("मोर", "mor", "Indian peafowl, regal national bird dancing at monsoon onset", "मोर (मयूर)", "noun", "m", "animals", "general", "सावण आयां मोर पंख पसार'र नाचै।"),
    ("ढेल", "dhel", "female peahen companion to peafowl", "मोरनी", "noun", "f", "animals", "general", "मोर रे साथे ढेल बैठी है।"),
    ("बगलो", "baglo", "snowy white cattle egret resting near village ponds", "बगुला", "noun", "m", "animals", "general", "तालाब रे कोर माथे बगलो ध्यान लगायो।"),
    ("चील", "cheel", "black kite circling high across desert thermals", "चील", "noun", "f", "animals", "general", "आकास मांय चील मंडरा रह्यी है।"),
    ("बाज", "baaj", "falcon / hawk prized in historic courtly hunting falconry", "बाज पक्षी", "noun", "m", "animals", "general", "राजाजी हाथ माथे बाज बिठायो।"),
    ("उल्लू / घूघू", "ulloo / ghooghoo", "desert eagle owl hooting in abandoned ruins and desert forts", "उल्लू पक्षी", "noun", "m", "animals", "general", "रात्यूं खंडहर मांय घूघू बोल्यो।"),

    # =========================================================================
    # 6. TASTES, COLORS & SENSATIONS (स्वाद, रंग अर अहसास)
    # =========================================================================
    ("खाटो", "khaato", "sour, acidic, tart, fermented (e.g. curd or buttermilk)", "खट्टा", "adjective", "m", "descriptors", "general", "छाछ घणी खाटी है।"),
    ("कड़वो", "kadwo", "bitter (e.g. neem leaves or wild melon)", "कड़वा", "adjective", "m", "descriptors", "general", "नीम रो पत्तो कड़वो व्है पण गुणकारी है।"),
    ("फीको", "pheeko", "bland, unsalted, lacking sweetness or seasoning", "फीका / बेस्वाद", "adjective", "m", "descriptors", "general", "चाय मांय खांड कोनी, फीकी है।"),
    ("सांवळो", "saanwalo", "dusky dark-complexioned, affectionate complexion of Krishna", "सांवला रंग", "adjective", "m", "descriptors", "general", "भगवान कृष्ण रो रूप सांवळो सलोणो है।"),
    ("गोरो", "goro", "fair, radiant complexion", "गोरा रंग", "adjective", "m", "descriptors", "general", "गोरा बदन माथे पीळी पोसाक सोहै।"),
    ("सिंदूरियो", "sindooriyo", "bright vermilion orange-red color associated with marital rites", "सिंदूरी रंग", "adjective", "m", "descriptors", "general", "सिंदूरियो साफा ब्याव मांय पहर्यो।"),
    ("गुलाबी", "gulaabi", "rose pink, emblematic color of Jaipur sandstone", "गुलाबी रंग", "adjective", "m", "descriptors", "general", "जयपुर नै गुलाबी नगरी कह्यीजै।"),
    ("बादामी", "baadaami", "almond fawn-yellow shade of Jaisalmer yellow limestone", "बादामी रंग", "adjective", "m", "descriptors", "general", "जैसलमेर रा किला बादामी पत्थरां सूं बण्या हैं।"),
    ("घाम / धूप", "ghaam / dhoop", "blazing desert sunshine / sultry ambient heat", "धूप / घाम", "noun", "m", "weather", "general", "दुपहरी मांय तेज घाम तप रह्यो है।"),
    ("पाळो", "paalo", "severe biting frost freezing winter crops", "पाला पड़ना / पाला", "noun", "m", "weather", "general", "पोह महीने मांय पाळो पड़बा सूं फसल नै बचावणो पड़ै।"),

    # =========================================================================
    # 7. TIME, UNITS & TRADITIONAL MEASUREMENTS (नाप, तोल अर बखत)
    # =========================================================================
    ("पहर", "pahar", "traditional 3-hour chronological watch of day or night", "पहर (तीन घंटे का समय)", "noun", "m", "time", "general", "चार पहर दिन अर चार पहर रात व्है।"),
    ("घड़ी", "ghadi", "traditional temporal unit equal to 24 solar minutes", "घड़ी (२४ मिनट का समय)", "noun", "f", "time", "general", "दो घड़ी विश्राम करो सा।"),
    ("वेला / बखत", "vela / bakhat", "time, opportune hour, season, moment", "समय / वेला / वक्त", "noun", "f", "time", "general", "संझा री वेला घर वळो सा।"),
    ("तोलो", "tolo", "traditional standard mass unit (~10 to 11.66 grams) for gold and silver", "तोला (सोने का भार)", "noun", "m", "descriptors", "general", "पांच तोले रो बाजूबंद बणायो।"),
    ("सेर", "ser", "historic mass unit (~0.93 kg) preceding modern kilogram", "सेर (लगभग १ किलो)", "noun", "m", "descriptors", "general", "दो सेर देसी घी ल्याया।"),
    ("मण", "man", "traditional weight unit equal to 40 seers (~37.3 to 40 kg)", "मन (चालीस सेर / लगभग ४० किलो)", "noun", "m", "descriptors", "general", "दस मण बाजरो खळे मांय भरयो।"),
    ("बीघो", "beegho", "traditional agricultural land unit (~0.625 acre / 1618 sq m)", "बीघा (जमीन की माप)", "noun", "m", "descriptors", "general", "म्हारै कनै बीस बीघा जमीन है।"),
    ("गज", "gaj", "linear yard measure (~3 feet / 0.914 meters) used for textiles and masonry", "गज (लंबाई की माप)", "noun", "m", "descriptors", "general", "दस गज मलमल रो थान खरीदयो।"),

    # =========================================================================
    # 8. SOCIAL FASTS, VOWS & HOLY FESTIVALS (बरत अर त्योहार)
    # =========================================================================
    ("करवा चौथ", "karwa chauth", "autumn fast observed by married women praying for husband's long life", "करवा चौथ का व्रत", "noun", "m", "rituals", "general", "करवा चौथ माथे चांद नै अर्घ्य दे'र व्रत खोल्यो।"),
    ("अहोई अष्टमी", "ahoi ashtami", "maternal autumn fast observing penance for health and longevity of sons", "अहोई अष्टमी का व्रत", "noun", "f", "rituals", "general", "अहोई अष्टमी माथे मां स्याऊ माता री पूजा कीधी।"),
    ("गोवर्धन पूजा", "govardhan pooja", "post-Diwali worship of cow dung effigy of sacred Govardhan hill and Annakut", "गोवर्धन पूजा / अन्नकूट", "noun", "f", "rituals", "general", "दीपावली रे दूजे दिन गोवर्धन पूजा हुवै।"),
    ("धुलंडी", "dhulandi", "color-splashing spring carnival day following Holika dahan", "धुलंडी (होली के अगले दिन रंगों का पर्व)", "noun", "f", "rituals", "general", "धुलंडी माथे गुलाल उड़ाई अर ढोल बजायो।"),
    ("दशा माता", "dasha maata", "spring festival where women venerate Peepal tree and tie tenfold thread for household prosperity", "दशा माता का व्रत", "noun", "f", "rituals", "general", "चैत वदी दशमी माथे दशा माता रो डोरो बांध्यो।"),
    ("यम द्वितीया / भाई दूज", "bhaai dooj", "festival honoring sacred sibling bonding where sisters apply auspicious tilak to brothers", "भाई दूज", "noun", "f", "rituals", "general", "भाई दूज माथे बहनां भाया नै भोजन जिमावै।"),
]

added_count = 0
for item in MEGA_ENTRIES:
    if len(item) == 9:
        raj, rom, eng, hin, pos, g, cat, dial, ex = item
    else:
        raj, rom, eng, hin, pos, cat, dial, ex = item
        g = None
    
    if raj not in existing_keys:
        existing_words.append({
            "rajasthani": raj,
            "roman": rom,
            "english": eng,
            "hindi": hin,
            "pos": pos,
            "gender": g,
            "category": cat,
            "dialect": dial,
            "example": ex
        })
        existing_keys.add(raj)
        added_count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} new entries to words.json!")
print(f"Total vocabulary words in library now: {len(existing_words)}")
