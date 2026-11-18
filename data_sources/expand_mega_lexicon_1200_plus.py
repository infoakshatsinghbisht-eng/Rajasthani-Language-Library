# -*- coding: utf-8 -*-
"""
Expand Mega Lexicon to 1,200+ Verified Words
============================================
From Dingal Poetics, Traditional Flora/Fauna, Household Utensils,
and Folk Descriptors.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

WORDS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "rajasthani", "lexicon", "data", "words.json")
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip() for w in words}
print(f"Existing words in database: {len(words)}")

BATCH_1200 = [
    # --- 1. Classical Dingal Prosody & Metrics (डिंगल छंद अर काव्यशास्त्र) ---
    ("दूहो", "dooho", "classic rhymed couplet of Dingal and Rajasthani poetry (13 and 11 matras)", "दोहा (डिंगल का प्रमुख छंद)", "noun", "m", "literature", "mwr", "ढोला-मारू रा दूहा मरुधर में गूंजै।"),
    ("सोरठो", "sortho", "inverted couplet with 11 and 13 matras, poignant and melodious", "सोरठा (दोहे का उल्टा छंद)", "noun", "m", "literature", "mwr", "कवि सोरठे में विरह रो वर्णन कियो।"),
    ("छप्पय", "chhappay", "six-line composite heroic stanza combining Rola and Ullala meters", "छप्पय (छह पंक्तियों का वीर छंद)", "noun", "m", "literature", "mwr", "चारण कवि छप्पय छंद में वीरता बखानी।"),
    ("कुंडलिया", "kundaliya", "compound cyclical verse beginning and ending with the same opening word", "कुंडलिया (गिरधर कविराय का छंद)", "noun", "m", "literature", "mwr", "कुंडलिया में नीति री शिक्षा है।"),
    ("कवित्त", "kavitt", "classic 31-syllable narrative verse form celebrating bravery and nature", "कवित्त / घनाक्षरी", "noun", "m", "literature", "mwr", "सेनापति वर्षा ऋतु रो कवित्त रच्यो।"),
    ("डिंगल गीत", "dingal geet", "heroic rhythmic song composed in strict Dingal alliterative rules", "डिंगल गीत (वीर रसात्मक गीत)", "noun", "m", "literature", "mwr", "युद्ध मैदान में डिंगल गीत गायो।"),
    ("वेणसगाई", "vensagaai", "sacred initial-letter alliteration constraint mandatory in Dingal poetry", "वैणसगाई (डिंगल का अनिवार्य अलंकार / आदि-अनुप्रास)", "noun", "f", "literature", "mwr", "वेणसगाई बिना डिंगल गीत नीं बणै।"),
    ("झूलणा", "jhoolna", "swaying devotional rhythm meter popularized by Sant Dadu Dayal and Mirabai", "झूलना छंद", "noun", "m", "literature", "mwr", "कृष्ण स्तुति में झूलणा गायो।"),
    ("सांखळी", "saankhli", "interlinking chain meter where last syllable of a line opens the next", "सांखली छंद (श्रृंखला छंद)", "noun", "f", "literature", "mwr", "कवि सांखळी छंद में भाव गूंथ्यो।"),

    # --- 2. Traditional Household Utensils & Kitchen Artifacts ---
    ("कलश", "kalash", "sacred ceremonial bronze water pitcher topped with coconut and mango leaves", "कलश / मंगल घट", "noun", "m", "household", "mwr", "प्रवेश द्वार माथे मंगल कलश स्थापित कियो।"),
    ("ताम्बियो", "taambiyo", "heavy pure copper water pot used for healthy morning hydration", "तांबिया (तांबे का लोटा)", "noun", "m", "household", "mwr", "ताम्बिये रो पाणी स्वास्थ्य सारू गुणकारी है।"),
    ("कटोरी / वाटी", "katori / vaati", "small rounded metal bowl for serving dal, rabri, or ghee", "कटोरी / वाटी", "noun", "f", "household", "mwr", "कटोरी में दाल परोसी।"),
    ("थाळी", "thaali", "large broad brass or bronze platter for complete meal feast", "थाली / थाट", "noun", "f", "household", "mwr", "कांसा री थाळी में जीमण जीम्यो।"),
    ("लोटो", "loto", "spherical drinking vessel with small pouring neck", "लोटा", "noun", "m", "household", "mwr", "लोटे सूं पाणी पायो।"),
    ("डोई", "doi", "large wooden stirring ladle for mixing lentils, kadhi and rabri", "डोई (काष्ठ चमचा)", "noun", "f", "household", "mwr", "डोई सूं कढ़ी हिलाई।"),
    ("कड़छी", "kadachhi", "deep iron or brass soup spoon with long handle", "करछुल / कड़छी", "noun", "f", "household", "mwr", "कड़छी सूं दाल काढ़ी।"),
    ("सरोतो", "saroto", "ornate steel nutcracker used for slicing betel nuts (supari)", "सरोता (सुपारी काटने का औजार)", "noun", "m", "household", "mwr", "सरोते सूं कसैली काटी।"),
    ("चिमटो", "chimto", "iron fire-tongs for flipping hot rotis on baking griddle", "चिमटा", "noun", "m", "household", "mwr", "चिमटे सूं सोगरो पल्ट्यो।"),
    ("सांसी", "saansi", "iron pincers for lifting hot heavy cooking pots from chulha", "संडासी (बर्तन पकड़ने का औजार)", "noun", "f", "household", "mwr", "सांसी सूं पतीला चूल्हे सूं उतार्यो।"),
    ("फूंकणी", "phoonkani", "hollow brass or iron tube used to blow air and rekindle hearth embers", "फूंकनी (चूल्हे में फूंक मारने की नली)", "noun", "f", "household", "mwr", "फूंकणी सूं फूंक मार'र आग जलाई।"),
    ("देगची", "degchi", "wide-bottomed cooking pot for boiling rice or preparing curries", "देगची / पतीला", "noun", "f", "household", "mwr", "देगची में खीचड़ो सीझै है।"),
    ("बटलोई", "batloi", "heavy brass cauldron with narrowed mouth retaining steam", "बटलोई (पीतल का विशेष पकाने का पात्र)", "noun", "f", "household", "mwr", "बटलोई में भात बणायो।"),
    ("तवी", "tawi", "concave iron or earthenware baking plate for rotis", "तवा / तवी", "noun", "f", "household", "mwr", "तवी माथे गरम-गरम रोटी फूलै।"),

    # --- 3. Desert Flora, Herbs & Natural Ecology ---
    ("कीकर", "keekar", "thorny acacia tree (Acacia nilotica) providing nutritious livestock pods", "कीकर / देशी बबूल", "noun", "m", "flora", "mwr", "कीकर री दातुन दांत मजबूत करै।"),
    ("जाल", "jaal", "dense evergreen shade tree of Thar (Salvadora oleifera) bearing sweet pilu berries", "जाल (मरुस्थल का छायादार वृक्ष)", "noun", "m", "flora", "mwr", "जाल रै नीचे चरवाहा विश्राम करै।"),
    ("पीलू", "peelu", "sweet juicy red and yellow berries harvested from Jaal trees in summer", "पीलू (जाल वृक्ष का फल)", "noun", "m", "flora", "mwr", "जेठ में टाबर मीठा पीलू तोड़ै।"),
    ("ढाक / पलाश", "dhaak / palaash", "Flame of the Forest tree bursting into fiery scarlet flowers in spring", "पलाश / ढाक (टेसू के फूल)", "noun", "m", "flora", "mwr", "फागण में ढाक रा लाल फूल खिलै।"),
    ("महुआ", "mahua", "sacred flowering tree of southern Rajasthan whose sweet blossoms feed communities", "महुआ (आदिवासी अंचलों का कल्पवृक्ष)", "noun", "m", "flora", "mwr", "महुए रा फूल टपकै।"),
    ("अमलतास", "amaltaas", "golden shower tree dripping radiant yellow blossom clusters in summer", "अमलतास (पीले फूलों वाला वृक्ष)", "noun", "m", "flora", "mwr", "अमलतास री छटा मनमोहक है।"),
    ("गूगल", "googal", "fragrant medicinal desert resin harvested from Commiphora mukul shrub", "गुग्गुल (सुगंधित व औषधीय धूप)", "noun", "m", "flora", "mwr", "संध्या वगत गूगल रो धूप दियो।"),
    ("सतावर", "sataavar", "medicinal climbing asparagus herb strengthening vitality", "शतावरी / सतावर", "noun", "f", "flora", "mwr", "सतावर री जड़ ताकत देवै।"),
    ("अश्वगंधा", "ashwagandha", "winter-cherry rejuvenating herb cultivated extensively in Jhalawar and Nagaur", "अश्वगंधा (आयुर्वेदिक रसायन)", "noun", "f", "flora", "mwr", "नागौर री अश्वगंधा देशभर में प्रसिद्ध है।"),

    # --- 4. Birds & Desert Wildlife (पंछी अर मरुधरा रा जीव) ---
    ("तीतर", "teetar", "grey francolin partridge calling at dawn from thorny scrub", "तीतर (रेगिस्तानी पक्षी)", "noun", "m", "fauna", "mwr", "सवेरे रोही में तीतर री बोली सुणीजै।"),
    ("बटेर", "bater", "quail foraging for grass seeds in dry fields", "बटेर (छोटा शिकारी पक्षी)", "noun", "f", "fauna", "mwr", "बटेर खेत में फड़फड़ाई।"),
    ("हरियल", "hariyal", "yellow-footed green pigeon that rarely touches ground in folklore", "हरियल (हरा कबूतर)", "noun", "m", "fauna", "mwr", "हरियल पीपल री डाली माथे बैठ्यो।"),
    ("काबर", "kaabar", "common myna bird chattering on cattle backs", "काबर / मैना", "noun", "f", "fauna", "mwr", "काबर गाय री पीठ माथे बैठी।"),
    ("हुदहुद", "hudhud", "common hoopoe bird boasting a magnificent crown crest", "हुदहुद (कलगीदार पक्षी)", "noun", "m", "fauna", "mwr", "हुदहुद माटी में कीड़ा खोजै।"),
    ("चील", "cheel", "black kite soaring high on desert thermals", "चील / शिकरा", "noun", "f", "fauna", "mwr", "चील आभै में चक्कर काटै।"),

    # --- 5. Human Attributes, Personality Traits & Descriptors ---
    ("हेताळू", "hetaaloo", "overflowing with deep unconditional love, warm and affectionate", "स्नेही / प्रेमपूर्ण / दयालु", "adjective", "m", "descriptors", "mwr", "म्हारी दादी घणी हेताळू है।"),
    ("हठीलो", "hatheelo", "steadfastly determined, uncompromisingly stubborn in righteousness", "हठी / दृढ़निश्चयी", "adjective", "m", "descriptors", "mwr", "हठीलो हम्मीर शरणागत री रक्षा करी।"),
    ("भोळो", "bholo", "innocent, simple-hearted, pure without deceit or malice", "सीधा-साधा / निष्कपट", "adjective", "m", "descriptors", "mwr", "भोळो किसान सब माथे विश्वास कर लेवै।"),
    ("ढीठ", "dheet", "bold, audacious, unperturbed by admonition", "ढीठ / निडर", "adjective", "m", "descriptors", "mwr", "ढीठ बालक बात नीं मानै।"),
    ("सुरस", "suras", "melodious, harmonious, sweetly resonant", "मधुर / सुरीला / रसीला", "adjective", "m", "descriptors", "mwr", "सुरस कंठ सूं मीरां भजन गायो।"),
    ("अलबेलो", "albelo", "jaunty, charmingly unique, playful and spirited", "अलबेला / रंगीला / बांका", "adjective", "m", "descriptors", "mwr", "अलबेलो राजस्थान रंग-रंगीलो है।"),
    ("मस्तानो", "mastaano", "joyfully carefree, spirited and ecstatic", "मस्ताना / आनंदमग्न", "adjective", "m", "descriptors", "mwr", "फकीर मस्तानो चालै।"),
    ("गंभीर", "gambheer", "profound, dignified, thoughtful and calm in temperament", "गंभीर / धीर-प्रशांत", "adjective", "m", "descriptors", "mwr", "राजा गंभीर विचार कियो।"),
    ("खोटो", "khoto", "counterfeit, flawed, insincere, lacking integrity", "खोटा / नकली / दुर्गुणी", "adjective", "m", "descriptors", "mwr", "खोटो सिक्को बाजार में नीं चालै।"),
    ("साचो", "saacho", "genuine, truthful, authentic, steadfast in honesty", "सच्चा / प्रामाणिक", "adjective", "m", "descriptors", "mwr", "साचो मित्र विपत्ति में सागै ऊभो रैवै।"),

    # --- 6. Seasons & Agricultural Harvest Eras ---
    ("सांवणी", "saamvani", "kharif monsoon crop cycle sown in Asadh and reaped in Asoj (bajra, guar, moth)", "खरीफ / सांवणी फसल", "noun", "f", "agriculture", "mwr", "सांवणी फसल चोखी हुई।"),
    ("उनाळू", "unaaloo", "rabi winter-spring crop cycle harvested in Chaitra (wheat, gram, mustard)", "रबी / उनाळू फसल", "noun", "f", "agriculture", "mwr", "उनाळू में गहूं री लावणी हुई।"),
    ("काती", "kaati", "holy month of Kartika marked by lamp lighting, Pushkar bath, and Dipawali", "कार्तिक मास (काती)", "noun", "m", "time", "mwr", "काती में पुष्कर में स्नान कियो।"),
    ("अगहन", "agahan", "month of Margashirsha bringing early winter chill and weddings", "मार्गशीर्ष मास (अगहन)", "noun", "m", "time", "mwr", "अगहन में ब्याव रा सावा आया।"),
    ("पूस", "poos", "mid-winter month of Pausha freezing water in desert shallow pans", "पौष मास (पूस की ठंड)", "noun", "m", "time", "mwr", "पूस में पालो पड़्यो।"),
    ("माघ", "maagh", "late winter month celebrated for Vasant Panchami and holy river baths", "माघ मास", "noun", "m", "time", "mwr", "माघ में सूर्य उत्तरायण व्है।"),
    ("चेत", "chet", "spring month of Chaitra opening the traditional Hindu New Year and Gangaur", "चैत्र मास (नया वर्ष व गणगौर)", "noun", "m", "time", "mwr", "चेत सुदी एकम नै नव संवत्सर शुरू व्है।"),
    ("बैसाख", "baisaakh", "warm month of Vaishakha celebrated for Akshaya Tritiya (Akha Teej)", "वैशाख मास", "noun", "m", "time", "mwr", "बैसाख में आखातीज आई।"),
    ("जेठ", "jeth_month", "fierce mid-summer month of Jyeshtha bringing highest temperatures and Rohini rains", "ज्येष्ठ मास (जेठ की दुपहरी)", "noun", "m", "time", "mwr", "जेठ री दुपहरै धोरां माथे लू तपैकै।")
]

added = 0
for item in BATCH_1200:
    r, rom, eng, hin, pos, gen, cat, dia, ex = item
    key = r.strip()
    if key not in existing:
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
        existing.add(key)
        added += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Added {added} brand new terms from Wave 7 Batch 2! Grand total lexicon now: {len(words)}")
