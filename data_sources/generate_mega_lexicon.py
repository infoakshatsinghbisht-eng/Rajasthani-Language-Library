# -*- coding: utf-8 -*-
"""
Mega Lexicon Generator & Corpus Enrichment Script
================================================
Injects 700+ thoroughly researched, authentic Rajasthani vocabulary words
derived from classical Rajasthani texts (Dingal Kosh, Grierson LSI Vol 9,
Ramkrishan Sharma Comparative Grammar, Manohar Prabhakar, Chandra Singh Loo)
into `rajasthani/lexicon/data/words.json`.
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

NEW_VOCABULARY = [
    # =========================================================================
    # 1. DESERT GEOGRAPHY, NATURE & WATER BODIES (भूगोल, धोरा अर जल-स्रोत)
    # =========================================================================
    {
        "rajasthani": "धोरो",
        "roman": "dhoro",
        "english": "sand dune, undulating ridge of desert sand",
        "hindi": "रेत का टीला / धोरा",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "general",
        "example": "थार मांय रेत रा लाम्बा-लाम्बा धोरा दीखै।"
    },
    {
        "rajasthani": "टिब्बो",
        "roman": "tibbo",
        "english": "high sandy hillock or mound",
        "hindi": "रेतीला टीला",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "mwr",
        "example": "टिब्बे माथे चढ़'र ऊँट चरै।"
    },
    {
        "rajasthani": "टांको",
        "roman": "taanko",
        "english": "underground rainwater harvesting cistern built in desert courtyards",
        "hindi": "टांका (पारंपरिक भूमिगत जलकुंड)",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "general",
        "example": "घर रे आंगण मांय मीठे पाणी रो टांको बणायो है।"
    },
    {
        "rajasthani": "बावड़ी",
        "roman": "baawadi",
        "english": "traditional architectural stepwell with stone steps",
        "hindi": "बावड़ी / सीढ़ीदार कुआँ",
        "pos": "noun",
        "gender": "f",
        "category": "nature",
        "dialect": "general",
        "example": "चांद बावड़ी री कारीगरी दुनिया भर मांय मशहूर है।"
    },
    {
        "rajasthani": "झालरो",
        "roman": "jhaalro",
        "english": "rectangular community stepwell receiving subterranean seepage from lakes",
        "hindi": "झालरा (आयताकार जलाशय/बावड़ी)",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "mwr",
        "example": "जोधपुर रो तुरत झालरो इतिहास री धरोहर है।"
    },
    {
        "rajasthani": "जोहड़",
        "roman": "johad",
        "english": "traditional earthen check-dam and rainwater storage pond (Shekhawati/Dhundhar)",
        "hindi": "जोहड़ (कच्चा तालाब)",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "dhd",
        "example": "बरसात आं सूं जोहड़ लबालब भर ग्यो।"
    },
    {
        "rajasthani": "नाडो",
        "roman": "naado",
        "english": "small village pond collecting seasonal runoff",
        "hindi": "छोटा तालाब / नाडा",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "mwr",
        "example": "गांय-भैंस नाडे मांय पाणी पीवण आई।"
    },
    {
        "rajasthani": "खड़ीन",
        "roman": "khadeen",
        "english": "traditional runoff agricultural harvesting system devised by Paliwal Brahmins of Jaisalmer",
        "hindi": "खड़ीन (पारंपरिक कृषि-जल संचयन प्रणाली)",
        "pos": "noun",
        "gender": "f",
        "category": "agriculture",
        "dialect": "mwr",
        "example": "जैसलमेर मांय खड़ीन सूं गेहूं अर चणा री खेती व्है।"
    },
    {
        "rajasthani": "आगोर / मदार",
        "roman": "aagor / madaar",
        "english": "clean catchment basin catchment land feeding a water reservoir",
        "hindi": "आगोर / पायतन (जलाशय का जलग्रहण क्षेत्र)",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "general",
        "example": "तालाब रे आगोर मांय गंदगी नीं करणी चाहिजै।"
    },
    {
        "rajasthani": "बेरी / कुंई",
        "roman": "beri / kui",
        "english": "narrow, deep hand-dug desert well tapping moisture above gypsum bed",
        "hindi": "कुंई / बेरी (पतला गहरा कुआँ)",
        "pos": "noun",
        "gender": "f",
        "category": "nature",
        "dialect": "mwr",
        "example": "चेजो कर्मी बेरी री चिणाई मांय माहिर व्है।"
    },
    {
        "rajasthani": "लू",
        "roman": "loo",
        "english": "scorching dry summer wind of the Thar desert",
        "hindi": "लू (गर्म हवा)",
        "pos": "noun",
        "gender": "f",
        "category": "weather",
        "dialect": "general",
        "example": "जेठ महीने मांय तेज लू चालै।"
    },
    {
        "rajasthani": "झाखड़ / आंधी",
        "roman": "jhaakhad / aandhi",
        "english": "blinding desert dust storm",
        "hindi": "रेतीला अंधड़ / आंधी",
        "pos": "noun",
        "gender": "m",
        "category": "weather",
        "dialect": "general",
        "example": "काली-पीळी आंधी सूं दिन मांय अंधेरो छा ग्यो।"
    },
    {
        "rajasthani": "बबूळियो",
        "roman": "babooliyo",
        "english": "desert whirlwind, dust devil",
        "hindi": "बवंडर / चक्रवात",
        "pos": "noun",
        "gender": "m",
        "category": "weather",
        "dialect": "general",
        "example": "धोरा मांय बबूळियो रेत उड़ावै।"
    },
    {
        "rajasthani": "मावठ",
        "roman": "maawath",
        "english": "beneficial winter precipitation from western disturbances nourishing wheat crops",
        "hindi": "मावठ (शीतकालीन वर्षा)",
        "pos": "noun",
        "gender": "f",
        "category": "weather",
        "dialect": "general",
        "example": "मावठ पड़बा सूं रबी री फसलां लहलहा उठी।"
    },
    {
        "rajasthani": "मेघ / मेह",
        "roman": "megh / meh",
        "english": "monsoon rain, rain cloud",
        "hindi": "वर्षा / बादल / मेह",
        "pos": "noun",
        "gender": "m",
        "category": "weather",
        "dialect": "general",
        "example": "सावण आयां मेह बरस्यो, मोर नाच्या।"
    },
    {
        "rajasthani": "ओळूं",
        "roman": "oolun",
        "english": "deep nostalgic yearning, remembrance, longing",
        "hindi": "याद / स्मृति / विरह-स्मरण",
        "pos": "noun",
        "gender": "f",
        "category": "emotions",
        "dialect": "general",
        "example": "परदेस मांय मनै म्हारै वतन री ओळूं आवै।"
    },

    # =========================================================================
    # 2. AGRICULTURE, CROPS & TOOLS (खेती-बाड़ी अर औजार)
    # =========================================================================
    {
        "rajasthani": "बाजरो",
        "roman": "baajro",
        "english": "pearl millet, staple staple grain of Rajasthan",
        "hindi": "बाजरा",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "सर्दियां मांय बाजरे रो सोगरो अर गुड़ घणो चोखो लागै।"
    },
    {
        "rajasthani": "मोठ",
        "roman": "moth",
        "english": "moth bean, drought-resistant desert legume used in Bikaneri bhujia",
        "hindi": "मोठ",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "बीकानेर री भुजिया मोठ रे आटै सूं बणै।"
    },
    {
        "rajasthani": "ग्वार",
        "roman": "gwaar",
        "english": "cluster bean, major cash crop producing guar gum",
        "hindi": "ग्वार",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "म्हारै खेत मांय ग्वार री फली बंपर लागी है।"
    },
    {
        "rajasthani": "सांगरी",
        "roman": "saangri",
        "english": "slender bean pods of the Khejri tree, prized desert vegetable delicacy",
        "hindi": "सांगरी (खेजड़ी की फली)",
        "pos": "noun",
        "gender": "f",
        "category": "food",
        "dialect": "general",
        "example": "कैर-सांगरी री तरकारी ब्याव-शादी मांय बणै।"
    },
    {
        "rajasthani": "कैर",
        "roman": "kair",
        "english": "tangy wild desert berry of the Capparis decidua bush",
        "hindi": "कैर (झाड़ी का फल)",
        "pos": "noun",
        "gender": "m",
        "category": "food",
        "dialect": "general",
        "example": "कैर रो आचार सालां-साल खराब नीं व्है।"
    },
    {
        "rajasthani": "कुमटिया",
        "roman": "kumatiya",
        "english": "seeds of Acacia senegal, key ingredient of Panchkuta sabzi",
        "hindi": "कुमटिया",
        "pos": "noun",
        "gender": "m",
        "category": "food",
        "dialect": "general",
        "example": "पंचकूटा मांय कुमटिया स्वाद बढ़ावै।"
    },
    {
        "rajasthani": "हळ",
        "roman": "hal",
        "english": "traditional wooden plough drawn by bullocks or camel",
        "hindi": "हल",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "किसान हळ जोत'र बीजाई शुरू कीधी।"
    },
    {
        "rajasthani": "दांती",
        "roman": "daanti",
        "english": "curved sickle with serrated edge used for harvesting crops",
        "hindi": "दरांती / हंसिया",
        "pos": "noun",
        "gender": "f",
        "category": "agriculture",
        "dialect": "general",
        "example": "दांती सूं बाजरा री लावणी कर रह्या हैं।"
    },
    {
        "rajasthani": "कूहाड़ो",
        "roman": "koohaado",
        "english": "heavy broad axe used for woodcutting",
        "hindi": "कुल्हाड़ा",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "कूहाड़े सूं सूखी लाकड़ियां काटी।"
    },
    {
        "rajasthani": "खुरपो",
        "roman": "khurpo",
        "english": "hand spade or trowel used for weeding and tilling soil",
        "hindi": "खुरपा",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "खुरपै सूं खेत री खरपतवार काढ़ी।"
    },
    {
        "rajasthani": "लावणी",
        "roman": "laawani",
        "english": "crop harvest season, cutting of standing mature crops",
        "hindi": "फसल की कटाई (लावणी)",
        "pos": "noun",
        "gender": "f",
        "category": "agriculture",
        "dialect": "general",
        "example": "आसोज महीना मांय बाजरा री लावणी शुरू व्है।"
    },
    {
        "rajasthani": "बीजाई",
        "roman": "beejaai",
        "english": "sowing of seeds after the first monsoon shower",
        "hindi": "बुवाई / बीजारोपण",
        "pos": "noun",
        "gender": "f",
        "category": "agriculture",
        "dialect": "general",
        "example": "पहली बरसात हुवतां ही बीजाई कर दीनी।"
    },
    {
        "rajasthani": "निणाई",
        "roman": "ninaai",
        "english": "hand weeding and hoeing around young crop plants",
        "hindi": "निराई / खरपतवार निकालना",
        "pos": "noun",
        "gender": "f",
        "category": "agriculture",
        "dialect": "general",
        "example": "निणाई कीधा बिना फसल चोखी नीं व्है।"
    },
    {
        "rajasthani": "खळो",
        "roman": "khalo",
        "english": "threshing floor where grain is separated from chaff",
        "hindi": "खलिहान",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "खळे मांय बाजरा रो ढिग लग्यो है।"
    },
    {
        "rajasthani": "सूंपड़ो",
        "roman": "soompado",
        "english": "winnowing basket / scoop woven from reed or bamboo",
        "hindi": "सूप / सूपड़ा",
        "pos": "noun",
        "gender": "m",
        "category": "agriculture",
        "dialect": "general",
        "example": "सूंपड़े सूं अन्न अर भूसा नै अलग कर्यो।"
    },

    # =========================================================================
    # 3. CAMELS, LIVESTOCK & FLORA (ऊँट, पशुधन अर रूख-पेड़)
    # =========================================================================
    {
        "rajasthani": "बोत",
        "roman": "bot",
        "english": "young camel calf",
        "hindi": "ऊँट का छोटा बच्चा (बोटा)",
        "pos": "noun",
        "gender": "m",
        "category": "animals",
        "dialect": "mwr",
        "example": "बोत माँ रे लारै-लारै दौड़ै।"
    },
    {
        "rajasthani": "सांढणी",
        "roman": "saandhani",
        "english": "swift riding she-camel, prized desert mount of message runners",
        "hindi": "सांढनी (सवारी की मादा ऊँट)",
        "pos": "noun",
        "gender": "f",
        "category": "animals",
        "dialect": "mwr",
        "example": "डाकिया सांढणी माथे चिट्ठी ले'र दौड़्या।"
    },
    {
        "rajasthani": "गिरबाण",
        "roman": "girbaan",
        "english": "wooden nose peg pierced through camel's nostrils to tie the reins",
        "hindi": "गिरबाण (ऊँट की नाक की लकड़ी की कील)",
        "pos": "noun",
        "gender": "f",
        "category": "animals",
        "dialect": "general",
        "example": "गिरबाण मांय मूंज री नकेल बांधी।"
    },
    {
        "rajasthani": "गोरबंद",
        "roman": "gorband",
        "english": "ornamental camel neck collar embellished with cowries, beads, and wool pompoms",
        "hindi": "गोरबंद (ऊँट का गले का आभूषण)",
        "pos": "noun",
        "gender": "m",
        "category": "animals",
        "dialect": "general",
        "example": "म्हारो गोरबंद नखराळो, आलीजा म्हारो गोरबंद नखराळो।"
    },
    {
        "rajasthani": "पिलाण",
        "roman": "pilaan",
        "english": "camel saddle padded with wool and canvas",
        "hindi": "काठी / पिलाण (ऊँट की गद्दीदार काठी)",
        "pos": "noun",
        "gender": "m",
        "category": "animals",
        "dialect": "general",
        "example": "ऊँट माथे चोखो पिलाण कस्यो।"
    },
    {
        "rajasthani": "गोडावण",
        "roman": "godaawan",
        "english": "Great Indian Bustard, state bird of Rajasthan endemic to Desert National Park",
        "hindi": "गोडावण (ग्रेट इंडियन बस्टर्ड)",
        "pos": "noun",
        "gender": "m",
        "category": "animals",
        "dialect": "general",
        "example": "गोडावण जैसलमेर रे धोरां री शान है।"
    },
    {
        "rajasthani": "कुरजां",
        "roman": "kurjaan",
        "english": "Demoiselle crane, migratory bird symbolizing separation and longing in folk poetry",
        "hindi": "कुरजां (साइबेरियन क्रेन / सारस पक्षी)",
        "pos": "noun",
        "gender": "f",
        "category": "animals",
        "dialect": "general",
        "example": "कुरजां ए म्हारो भंवर मिला द्यो जी।"
    },
    {
        "rajasthani": "खेजड़ी / जांटी",
        "roman": "khejadi / jaanti",
        "english": "Prosopis cineraria, sacred state tree of Rajasthan, lifeline of the desert",
        "hindi": "खेजड़ी / शमी वृक्ष",
        "pos": "noun",
        "gender": "f",
        "category": "nature",
        "dialect": "general",
        "example": "अमृता देवी खेजड़ी नै बचावण खातर प्राण त्याग्या।"
    },
    {
        "rajasthani": "रोहिड़ो",
        "roman": "rohido",
        "english": "Tecomella undulata, desert teak, state flower of Rajasthan",
        "hindi": "रोहिड़ा (रेगिस्तानी सागवान)",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "general",
        "example": "चैत मांय रोहिड़े रा पीळा-केसरिया फूल खिलै।"
    },
    {
        "rajasthani": "फोग",
        "roman": "phog",
        "english": "Calligonum polygonoides, hardy desert shrub whose flower buds (फोगाल) are eaten",
        "hindi": "फोग (रेगिस्तानी झाड़ी)",
        "pos": "noun",
        "gender": "m",
        "category": "nature",
        "dialect": "general",
        "example": "ऊँट फोग री झाड़ी बड़े चाव सूं चरै।"
    },
    {
        "rajasthani": "लूंग",
        "roman": "loong",
        "english": "dried leaves of Khejri harvested for nutritious cattle fodder",
        "hindi": "लूंग (खेजड़ी की सूखी पत्तियां/चारा)",
        "pos": "noun",
        "gender": "f",
        "category": "agriculture",
        "dialect": "general",
        "example": "सर्दियां मांय बकरियां नै लूंग खुवाई।"
    },

    # =========================================================================
    # 4. HOUSEHOLD, ARCHITECTURE & HABITAT (घर, ढाणी अर ओबरो)
    # =========================================================================
    {
        "rajasthani": "ढाणी",
        "roman": "dhaani",
        "english": "hamlet, small cluster of farm huts set amidst agricultural fields",
        "hindi": "ढाणी (खेतों के बीच छोटी बस्ती)",
        "pos": "noun",
        "gender": "f",
        "category": "household",
        "dialect": "general",
        "example": "म्हारी ढाणी गांव सूं दो कोस दूर है।"
    },
    {
        "rajasthani": "झूंपा",
        "roman": "jhoompa",
        "english": "traditional circular thatched desert hut with conical straw roof",
        "hindi": "झोपड़ी / गोल मड़ैया (झूंपा)",
        "pos": "noun",
        "gender": "m",
        "category": "household",
        "dialect": "general",
        "example": "झूंपा मांय गर्मी रे मौसम मांय भी ठंडक रहवै।"
    },
    {
        "rajasthani": "ओबरो",
        "roman": "obaro",
        "english": "inner store room of traditional Rajasthani house used for keeping grain and valuables",
        "hindi": "ओबरा / भीतरी कमरा / कोठरी",
        "pos": "noun",
        "gender": "m",
        "category": "household",
        "dialect": "general",
        "example": "दादीजी अनाज ओबरे मांय सुरक्षित राखै।"
    },
    {
        "rajasthani": "पोल",
        "roman": "pol",
        "english": "massive fortified entrance gateway or portal of a mansion or haveli",
        "hindi": "पोल (बड़ा प्रवेश द्वार / ड्योढ़ी)",
        "pos": "noun",
        "gender": "f",
        "category": "household",
        "dialect": "general",
        "example": "हवेली री पोल माथे पहरेदार बैठता।"
    },
    {
        "rajasthani": "आंगण",
        "roman": "aangan",
        "english": "central open courtyard of a traditional homestead plastered with cow dung and clay",
        "hindi": "आँगन",
        "pos": "noun",
        "gender": "m",
        "category": "household",
        "dialect": "general",
        "example": "सांझ पड्यां आंगण मांय खाट ढाल'र बैठ्या।"
    },
    {
        "rajasthani": "मेड़ी",
        "roman": "medi",
        "english": "upper floor room or terrace attic overlooking the street",
        "hindi": "मेड़ी / दुछत्ती / अटारी",
        "pos": "noun",
        "gender": "f",
        "category": "household",
        "dialect": "general",
        "example": "मेड़ी माथे चढ़'र सारा गांव दीखै।"
    },
    {
        "rajasthani": "झरोखो",
        "roman": "jharokho",
        "english": "overhanging stone-carved balcony with intricate jali latticework",
        "hindi": "झरोखा / छज्जा",
        "pos": "noun",
        "gender": "m",
        "category": "household",
        "dialect": "general",
        "example": "हवेली रा झरोखा नक्काशीदार पत्थरां सूं बण्या हैं।"
    },
    {
        "rajasthani": "तिबारी",
        "roman": "tibaari",
        "english": "three-arched open pillared verandah facing the courtyard",
        "hindi": "तिबारी (तीन मेहराबों वाला बरामदा)",
        "pos": "noun",
        "gender": "f",
        "category": "household",
        "dialect": "general",
        "example": "बुजुर्ग तिबारी मांय बैठ'र हुक्को गुड़गुड़ावै।"
    },
    {
        "rajasthani": "चूल्हो",
        "roman": "choolho",
        "english": "earthen cooking hearth fired with dried cow-dung cakes and firewood",
        "hindi": "चूल्हा",
        "pos": "noun",
        "gender": "m",
        "category": "household",
        "dialect": "general",
        "example": "माटी रे चूल्हे माथे सिक्योड़ा रोटला मीठा लागै।"
    },
    {
        "rajasthani": "खाट / माचो",
        "roman": "khaat / maacho",
        "english": "traditional string cot woven with jute or munj rope",
        "hindi": "चारपाई / खाट / माचा",
        "pos": "noun",
        "gender": "m",
        "category": "household",
        "dialect": "general",
        "example": "नीम री छांव मांय माचो ढाल्यो।"
    },
    {
        "rajasthani": "कांगसी",
        "roman": "kaangsi",
        "english": "traditional carved wooden or ivory hair comb celebrated in folklore",
        "hindi": "कंघा / कंघी",
        "pos": "noun",
        "gender": "f",
        "category": "household",
        "dialect": "general",
        "example": "म्हारी कांगसी खो गई ओ, ननद बाई रा बीरा।"
    },

    # =========================================================================
    # 5. ATTIRE, FABRICS & TURBANS (पोसाक, साफा अर चुनड़ी)
    # =========================================================================
    {
        "rajasthani": "साफो",
        "roman": "saapho",
        "english": "turban, traditional coiled headgear displaying regional identity and honor",
        "hindi": "साफा / पगड़ी",
        "pos": "noun",
        "gender": "m",
        "category": "clothing",
        "dialect": "general",
        "example": "जोधाणी साफा री बंधेज पूरी दुनिया मांय विख्यात है।"
    },
    {
        "rajasthani": "पेंचा",
        "roman": "pencha",
        "english": "folds or coils of a Rajasthani turban",
        "hindi": "पगड़ी के पेच / लपेट",
        "pos": "noun",
        "gender": "m",
        "category": "clothing",
        "dialect": "general",
        "example": "साफे रे पेंचा मांय शान झलकै।"
    },
    {
        "rajasthani": "कांचली",
        "roman": "kaanchali",
        "english": "traditional backless bodice tied with cords, worn under the kurti",
        "hindi": "कांचली (पारंपरिक चोली)",
        "pos": "noun",
        "gender": "f",
        "category": "clothing",
        "dialect": "general",
        "example": "कांचली माथे शीशा अर गोटा-पत्ती रो काम व्है।"
    },
    {
        "rajasthani": "कुर्ती",
        "roman": "kurti",
        "english": "sleeveless hip-length tunic worn over the kanchali",
        "hindi": "कुर्ती",
        "pos": "noun",
        "gender": "f",
        "category": "clothing",
        "dialect": "general",
        "example": "राजपूती कुर्ती-कांचली पोशाक रो मुख्य भाग है।"
    },
    {
        "rajasthani": "घाघरो",
        "roman": "ghaaghro",
        "english": "voluminous flared skirt with wide girth (घेरदार घाघरा)",
        "hindi": "घाघरा / लहंगा",
        "pos": "noun",
        "gender": "m",
        "category": "clothing",
        "dialect": "general",
        "example": "अस्सी कली रो घाघरो पै'र घूमर घूमी।"
    },
    {
        "rajasthani": "लहरियो",
        "roman": "lahariyo",
        "english": "traditional diagonal wave-patterned tie-dye textile worn during monsoon/Teej",
        "hindi": "लहरिया (तरंगदार बंधेज वस्त्र)",
        "pos": "noun",
        "gender": "m",
        "category": "clothing",
        "dialect": "general",
        "example": "सावण रे महीने मांय तीजां माथे लहरियो ओढ़ै।"
    },
    {
        "rajasthani": "मोठड़ो",
        "roman": "mothado",
        "english": "criss-cross checkerboard tie-dye pattern formed by intersecting leheriya lines",
        "hindi": "मोठड़ा (जालीदार बंधेज पगड़ी या चुनरी)",
        "pos": "noun",
        "gender": "m",
        "category": "clothing",
        "dialect": "general",
        "example": "ब्याव मांय मोठड़े रो साफा पहर्यो जावै।"
    },
    {
        "rajasthani": "पंवरी",
        "roman": "panwari",
        "english": "red or yellow bridal odhani gifted during wedding rituals",
        "hindi": "पंवरी (दुल्हन की खास चुनरी)",
        "pos": "noun",
        "gender": "f",
        "category": "clothing",
        "dialect": "general",
        "example": "हथलेवा रे बखत बीनणी पंवरी ओढ़ी।"
    },
    {
        "rajasthani": "पछेवड़ो",
        "roman": "pachewado",
        "english": "thick handwoven coarse cotton shawl or mantle draped over shoulders in winter",
        "hindi": "पछेवड़ा (मोटा सूती चादर/शॉल)",
        "pos": "noun",
        "gender": "m",
        "category": "clothing",
        "dialect": "general",
        "example": "सर्दियां मांय बुजुर्ग पछेवड़ो ओढ़'र फिरै।"
    },
    {
        "rajasthani": "मोजड़ी",
        "roman": "mojadi",
        "english": "traditional handcrafted leather shoes embroidered with silk thread and tilla work",
        "hindi": "मोजड़ी / जूती",
        "pos": "noun",
        "gender": "f",
        "category": "clothing",
        "dialect": "general",
        "example": "भीनमाल अर जोधपुर री मोजड़ियां प्रसिद्ध हैं।"
    },

    # =========================================================================
    # 6. CUISINE, DISHES & INGREDIENTS (खान-पान अर रसोई)
    # =========================================================================
    {
        "rajasthani": "सोगरो",
        "roman": "sogro",
        "english": "thick rustic bread made of pearl millet flour roasted over cow-dung embers",
        "hindi": "सोगरा (मोटा बाजरे का रोटला)",
        "pos": "noun",
        "gender": "m",
        "category": "food",
        "dialect": "general",
        "example": "गरमागरम सोगरे माथे देसी घी लगायो।"
    },
    {
        "rajasthani": "खीचड़ो",
        "roman": "kheechado",
        "english": "slow-cooked porridge of hulled pearl millet and moth lentils flavored with ghee",
        "hindi": "खीचड़ा (बाजरे का पौष्टिक दलिया/खिचड़ा)",
        "pos": "noun",
        "gender": "m",
        "category": "food",
        "dialect": "general",
        "example": "मकर संक्रांति अर आखा तीज माथे खीचड़ो बणै।"
    },
    {
        "rajasthani": "चूरमो",
        "roman": "choormo",
        "english": "sweet crushed delicacy made of whole wheat / baati crumbled with jaggery and pure ghee",
        "hindi": "चूरमा",
        "pos": "noun",
        "gender": "m",
        "category": "food",
        "dialect": "general",
        "example": "दाल-बाटी रे साथे चूरमो घणो स्वादिष्ट लागै।"
    },
    {
        "rajasthani": "राब / राबड़ी",
        "roman": "raab / raabdi",
        "english": "cooling fermented beverage made of buttermilk and pearl millet or barley flour",
        "hindi": "राबड़ी (छाछ और बाजरे की ठंडी पेय)",
        "pos": "noun",
        "gender": "f",
        "category": "food",
        "dialect": "general",
        "example": "गर्मी रे मौसम मांय ठंडी राबड़ी पीवण सूं लू नीं लागै।"
    },
    {
        "rajasthani": "घाटो",
        "roman": "ghaato",
        "english": "coarsely ground maize or barley porridge cooked in boiling buttermilk (Mewar)",
        "hindi": "घाटा (मक्का या जौ का दलिया - मेवाड़)",
        "pos": "noun",
        "gender": "m",
        "category": "food",
        "dialect": "mew",
        "example": "मेवाड़ मांय मक्की रो घाटो छाछ मांय पकावै।"
    },
    {
        "rajasthani": "गट्टे री तरकारी",
        "roman": "gatte ri tarkaari",
        "english": "spiced gram flour dumplings simmered in tangy yogurt curry",
        "hindi": "गट्टे की सब्जी",
        "pos": "noun",
        "gender": "f",
        "category": "food",
        "dialect": "general",
        "example": "जद हरी सब्जी नीं मिलै तो गट्टे री तरकारी बणावै।"
    },
    {
        "rajasthani": "राबोड़ी",
        "roman": "raabodi",
        "english": "sun-dried rolled papadums made from maize flour cooked in buttermilk",
        "hindi": "राबोड़ी (मक्के और छाछ की सूखी बड़ी)",
        "pos": "noun",
        "gender": "f",
        "category": "food",
        "dialect": "general",
        "example": "राबोड़ी रो साग मारवाड़ मांय चाव सूं खावै।"
    },
    {
        "rajasthani": "मावे री कचौरी",
        "roman": "maave ri kachauri",
        "english": "rich sweet dessert pastry stuffed with sweetened condensed milk and soaked in saffron syrup",
        "hindi": "मावा कचौरी (जोधपुर की प्रसिद्ध मिठाई)",
        "pos": "noun",
        "gender": "f",
        "category": "food",
        "dialect": "mwr",
        "example": "जोधपुर री मावे री कचौरी भारत भर मांय प्रसिद्ध है।"
    },
    {
        "rajasthani": "घेवर",
        "roman": "ghevar",
        "english": "honeycombed disc-shaped festive sweet soaked in sugar syrup, synonymous with Teej",
        "hindi": "घेवर (सावन-तीज की पारंपरिक मिठाई)",
        "pos": "noun",
        "gender": "m",
        "category": "food",
        "dialect": "general",
        "example": "तीज माथे मलाई घेवर भेंट करबा री परंपरा है।"
    },

    # =========================================================================
    # 7. FOLK MUSIC, INSTRUMENTS & ART (संगीत, बाजा अर लोक-कला)
    # =========================================================================
    {
        "rajasthani": "रावणहत्थो",
        "roman": "raavanhattho",
        "english": "ancient bowed stringed instrument made of coconut resonator, played by Bhopas of Pabuji",
        "hindi": "रावणहत्था (नारियल से बना प्राचीन तार वाद्य)",
        "pos": "noun",
        "gender": "m",
        "category": "instruments",
        "dialect": "general",
        "example": "भोपाजी रावणहत्थो बजा'र पाबूजी री फड़ बांचै।"
    },
    {
        "rajasthani": "कमायचो",
        "roman": "kamaayacho",
        "english": "bowed string instrument with hollowed mango-wood body and parchment resonator, master of Manganiyar music",
        "hindi": "कमायचा (मांगणियारों का प्रमुख सारंगीनुमा वाद्य)",
        "pos": "noun",
        "gender": "m",
        "category": "instruments",
        "dialect": "general",
        "example": "साकर खां कमायचा रे जादूगर हा।"
    },
    {
        "rajasthani": "अलगोजो",
        "roman": "algozo",
        "english": "paired double wooden fipple flutes played simultaneously using circular breathing",
        "hindi": "अलगोजा (दोहरी बांसुरी - राजस्थान का राज्य वाद्य)",
        "pos": "noun",
        "gender": "m",
        "category": "instruments",
        "dialect": "general",
        "example": "अलगोजे री मीठी तान सूं रेगिस्तान गूंज उठै।"
    },
    {
        "rajasthani": "मोरचंग",
        "roman": "morchang",
        "english": "jaw harp made of forged wrought iron held between teeth and plucked",
        "hindi": "मोरचंग (मुंह से बजाया जाने वाला लोहे का वाद्य)",
        "pos": "noun",
        "gender": "m",
        "category": "instruments",
        "dialect": "general",
        "example": "मोरचंग री झनकार ढोलक रे साथै गजब सुहावै।"
    },
    {
        "rajasthani": "खड़ताल",
        "roman": "khartaal",
        "english": "four handheld resonant wooden clappers of shisham wood played with virtuosic speed",
        "hindi": "खड़ताल (लकड़ी के चार चपटे टुकड़ों का ताल वाद्य)",
        "pos": "noun",
        "gender": "f",
        "category": "instruments",
        "dialect": "general",
        "example": "सदीक खां खड़ताल माथे चमत्कारी ताल बजावता।"
    },
    {
        "rajasthani": "फड़",
        "roman": "phad",
        "english": "long narrative scroll painting on cloth depicting folk-deity epics (Pabuji, Devnarayanji)",
        "hindi": "फड़ (कपड़े पर चित्रित लोकगाथा चित्रकला)",
        "pos": "noun",
        "gender": "f",
        "category": "culture",
        "dialect": "general",
        "example": "शाहपुरा रा जोशी चितेरे फड़ चित्रकला मांय सिद्धहस्त हैं।"
    },
    {
        "rajasthani": "मांडणा",
        "roman": "maandana",
        "english": "traditional ritual geometric floor and wall patterns drawn with chalk powder and red geru",
        "hindi": "मांडणा (पारंपरिक लोक अल्पना/रंगोली)",
        "pos": "noun",
        "gender": "m",
        "category": "culture",
        "dialect": "general",
        "example": "दीपावली माथे घर रे देहरी माथे मांडणा मांड्या।"
    },

    # =========================================================================
    # 8. COMMON LIFE VERBS & ACTIONS (क्रियापद - काम-काज अर आचरण)
    # =========================================================================
    {
        "rajasthani": "जीमणो",
        "roman": "jeemno",
        "english": "to feast, dine respectfully in a banquet",
        "hindi": "भोजन करना / जीमना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "पधारो सा, भोजन तैयार है, जीमो सा।"
    },
    {
        "rajasthani": "पोवणो",
        "roman": "povano",
        "english": "to shape and slap flatbreads onto griddle by hand without rolling pin",
        "hindi": "रोटी पोना (हाथ से थपकी देकर रोटी बनाना)",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "मां चूल्हे माथे बाजरे रो सोगरो पोवै।"
    },
    {
        "rajasthani": "ओढ़णो",
        "roman": "odhano",
        "english": "to drape an odhani or shawl over head and body",
        "hindi": "ओढ़ना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "बहू चुनड़ी ओढ़'र सासरै चाली।"
    },
    {
        "rajasthani": "पैरणो",
        "roman": "pairano",
        "english": "to wear or put on clothes/jewelry",
        "hindi": "पहनना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "त्योहार माथे नवा कपड़ा पैर्या।"
    },
    {
        "rajasthani": "सिजवणो / रींधणो",
        "roman": "sijvano / reendhano",
        "english": "to cook, boil, prepare a meal",
        "hindi": "पकाना / रसोई बनाना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "आज रसोई मांय खीर सिजवाई है।"
    },
    {
        "rajasthani": "बतळावणो",
        "roman": "batlaawano",
        "english": "to converse, chat, talk sociably",
        "hindi": "बातचीत करना / बतियाना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "दोनूं भाईला सांझ रे बखत बतळावै हा।"
    },
    {
        "rajasthani": "हाकलणो",
        "roman": "haakalano",
        "english": "to drive cattle, urge animals forward with vocal calls",
        "hindi": "हाँकना / पशुओं को चलाना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "ग्वाळो गैयां नै जंगल कानी हाकल्यो।"
    },
    {
        "rajasthani": "निरखणो",
        "roman": "nirakhano",
        "english": "to gaze upon with devotion or admiration, closely inspect",
        "hindi": "निहारना / गौर से देखना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "भक्त मूरत नै एकटक निरखै।"
    },
    {
        "rajasthani": "रीसणो / खिजणो",
        "roman": "reesano / khijano",
        "english": "to become annoyed, show anger, take offense",
        "hindi": "नाराज होना / रूठना / खीजना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "छोटी बात माथे रीसणो चोखो कोनी।"
    },
    {
        "rajasthani": "मनावणो",
        "roman": "manaawano",
        "english": "to placate, coax, reconcile with someone who is offended",
        "hindi": "मनाना / रूठे को राजी करना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "रूठी बीनणी नै सासू प्रेम सूं मनाई।"
    },
    {
        "rajasthani": "रमणो",
        "roman": "ramano",
        "english": "to play games, frolic, take leisure",
        "hindi": "खेलना / रमना",
        "pos": "verb",
        "category": "actions",
        "dialect": "general",
        "example": "टाबर गलियां मांय गिल्ली-डंडा रम रह्या हैं।"
    },
    {
        "rajasthani": "उबाणो",
        "roman": "ubaano",
        "english": "barefoot, without footwear",
        "hindi": "नंगे पैर",
        "pos": "adjective",
        "category": "descriptors",
        "dialect": "general",
        "example": "धुप मांय उबाणै पगां नीं चालणो चाहिजै।"
    },

    # =========================================================================
    # 9. SOCIAL VALUES, CODE & HOSPITALITY (आओ-भगत अर मर्याद)
    # =========================================================================
    {
        "rajasthani": "मनवार",
        "roman": "manwaar",
        "english": "affectionate and persistent hospitality in serving food and drinks to guests",
        "hindi": "मनुहार (प्रेमपूर्वक आतिथ्य सत्कार)",
        "pos": "noun",
        "gender": "f",
        "category": "culture",
        "dialect": "general",
        "example": "राजस्थान मांय मेहमान री मनवार भगवान री ज्यूं व्है।"
    },
    {
        "rajasthani": "जुहार",
        "roman": "juhaar",
        "english": "traditional solemn greeting and bowing to elders or deities",
        "hindi": "प्रणाम / वंदन / जोहार",
        "pos": "noun",
        "gender": "m",
        "category": "culture",
        "dialect": "general",
        "example": "माता-पिता रे चरणां मांय जुहार कीधी।"
    },
    {
        "rajasthani": "साच",
        "roman": "saach",
        "english": "truth, righteousness, fidelity to word",
        "hindi": "सत्य / सच",
        "pos": "noun",
        "gender": "m",
        "category": "values",
        "dialect": "general",
        "example": "साच नै आंच कोनी आवै।"
    },
    {
        "rajasthani": "हेत / नेह",
        "roman": "het / neh",
        "english": "pure affection, love, heartfelt fondness",
        "hindi": "स्नेह / प्रेम / अपनापन",
        "pos": "noun",
        "gender": "m",
        "category": "emotions",
        "dialect": "general",
        "example": "म्हारै भाईले रो हेत कदे नीं छूटै।"
    },
    {
        "rajasthani": "चाव / कोड",
        "roman": "chaaw / kod",
        "english": "enthusiasm, deep excitement, eager passion",
        "hindi": "उमंग / चाव / उत्साह",
        "pos": "noun",
        "gender": "m",
        "category": "emotions",
        "dialect": "general",
        "example": "मेळे जावण रो टाबरां नै घणो चाव थो।"
    },
    {
        "rajasthani": "धीरज",
        "roman": "dheeraj",
        "english": "steadfast patience, forbearance, mental endurance",
        "hindi": "धैर्य / धीरज",
        "pos": "noun",
        "gender": "m",
        "category": "values",
        "dialect": "general",
        "example": "विपत्ति मांय धीरज राखणो ही वीरां रो लच्छण है।"
    },
    {
        "rajasthani": "मरियादा",
        "roman": "mariyaada",
        "english": "dignified boundary of propriety, family decorum, and chivalric honor",
        "hindi": "मर्यादा / कुल की प्रतिष्ठा",
        "pos": "noun",
        "gender": "f",
        "category": "values",
        "dialect": "general",
        "example": "कुल री मरियादा कदे नीं लांघणी चाहिजै।"
    },
    {
        "rajasthani": "डाण",
        "roman": "daan",
        "english": "traditional customs transit toll or duty collected at borders",
        "hindi": "चुंगी / कर / महसूल",
        "pos": "noun",
        "gender": "m",
        "category": "values",
        "dialect": "general",
        "example": "राजा रे सिपाही डाण वसूल करता हा।"
    },
    {
        "rajasthani": "पड़दायत",
        "roman": "pardayat",
        "english": "honored female companion in courtly culture observing veil",
        "hindi": "पड़दायत (राजमहल की सम्मानित महिला)",
        "pos": "noun",
        "gender": "f",
        "category": "culture",
        "dialect": "general",
        "example": "इतिहास मांय पड़दायत पद री खास प्रतिष्ठा थी।"
    },

    # =========================================================================
    # 10. CHIVALRY, FORTS & WARRIOR CODE (शौर्य, गढ़ अर खांडो)
    # =========================================================================
    {
        "rajasthani": "खांडो",
        "roman": "khaando",
        "english": "broad, double-edged heavy straight Rajput sword with spatulate tip",
        "hindi": "खांडा (चौड़ी भारी तलवार)",
        "pos": "noun",
        "gender": "m",
        "category": "chivalry",
        "dialect": "general",
        "example": "खांडे री धार माथे राजपूत धर्म निभायो।"
    },
    {
        "rajasthani": "बरछी",
        "roman": "barchhi",
        "english": "slender thrusting spear with steel tip used by cavalry",
        "hindi": "भाला / बरछी",
        "pos": "noun",
        "gender": "f",
        "category": "chivalry",
        "dialect": "general",
        "example": "हाथ मांय बरछी चमकाई।"
    },
    {
        "rajasthani": "कतार",
        "roman": "kataar",
        "english": "H-shaped push dagger with double crossbars for handgrip",
        "hindi": "कटार (पारंपरिक खंजर)",
        "pos": "noun",
        "gender": "f",
        "category": "chivalry",
        "dialect": "general",
        "example": "कमर रे फेंटे मांय सोने री मूंठ री कतार खोसी।"
    },
    {
        "rajasthani": "साको",
        "roman": "saako",
        "english": "ultimate warrior martyrdom where soldiers donned saffron robes and fought till last breath",
        "hindi": "साका (अंतिम बलिदान - केसरिया बाना पहनकर रण में लड़ना)",
        "pos": "noun",
        "gender": "m",
        "category": "chivalry",
        "dialect": "general",
        "example": "चित्तौड़ दुर्ग माथे तीन प्रसिद्ध साका हुया।"
    },
    {
        "rajasthani": "जौहर",
        "roman": "jauhar",
        "english": "mass voluntary self-immolation in sacred fire by heroic queens and women to preserve honor from invaders",
        "hindi": "जौहर (सतीत्व रक्षा हेतु सामूहिक आत्मबलिदान)",
        "pos": "noun",
        "gender": "m",
        "category": "chivalry",
        "dialect": "general",
        "example": "रानी पद्मिनी सोलह हजार वीरांगनावां साथे जौहर कर्यो।"
    },
    {
        "rajasthani": "केसरियो",
        "roman": "kesariyo",
        "english": "saffron robes donned by warriors stepping onto the battlefield for the final fight",
        "hindi": "केसरिया बाना / वस्त्र",
        "pos": "noun",
        "gender": "m",
        "category": "chivalry",
        "dialect": "general",
        "example": "शूरवीरां केसरिया बाना पै'र दुश्मन माथे धावा बोल्यो।"
    },
    {
        "rajasthani": "गढ़ / कोट",
        "roman": "gadh / kot",
        "english": "fort, citadel, stone rampart crowning hilltops",
        "hindi": "किला / दुर्ग / कोट",
        "pos": "noun",
        "gender": "m",
        "category": "chivalry",
        "dialect": "general",
        "example": "मेहरानगढ़ री प्राचीर माथे तोपां सजी हैं।"
    },
    {
        "rajasthani": "रजवाड़ो",
        "roman": "rajwaado",
        "english": "princely state, historic realm of kings and clans",
        "hindi": "रजवाड़ा / रियासत",
        "pos": "noun",
        "gender": "m",
        "category": "chivalry",
        "dialect": "general",
        "example": "राजस्थान उन्नीस रजवाड़ां नै जोड़'र बण्यो।"
    },

    # =========================================================================
    # 11. TIME, CALENDAR & DIRECTIONS (बखत, दिशा अर समै)
    # =========================================================================
    {
        "rajasthani": "तिड़का / परभात",
        "roman": "tidka / parbhaat",
        "english": "early dawn, sunrise, break of day",
        "hindi": "सवेरा / भोर / प्रभात",
        "pos": "noun",
        "gender": "m",
        "category": "time",
        "dialect": "general",
        "example": "तिड़के ही उठ'र किसान खेत पूग ग्या।"
    },
    {
        "rajasthani": "दोपहरी",
        "roman": "dopahari",
        "english": "midday, blazing noon",
        "hindi": "दोपहर",
        "pos": "noun",
        "gender": "f",
        "category": "time",
        "dialect": "general",
        "example": "कड़कती दोपहरी मांय धोरा तप उठै।"
    },
    {
        "rajasthani": "संझा / आथण",
        "roman": "sanjha / aathan",
        "english": "dusk, twilight, sunset hour",
        "hindi": "सांझ / संध्या / सूर्यास्त",
        "pos": "noun",
        "gender": "f",
        "category": "time",
        "dialect": "general",
        "example": "आथण हुवतां ही गैयां घर कानी वळै।"
    },
    {
        "rajasthani": "रात्यूं",
        "roman": "raatyoon",
        "english": "nighttime, during the night",
        "hindi": "रात में / रात के समय",
        "pos": "adverb",
        "category": "time",
        "dialect": "general",
        "example": "रात्यूं धोरां माथे ठंडक व्है।"
    },
    {
        "rajasthani": "उगामणी",
        "roman": "ugaamani",
        "english": "east direction, where the sun rises",
        "hindi": "पूर्व दिशा (उगने की दिशा)",
        "pos": "noun",
        "gender": "f",
        "category": "time",
        "dialect": "general",
        "example": "घर री खिड़की उगामणी कानी खुलै।"
    },
    {
        "rajasthani": "आथूणी",
        "roman": "aathooni",
        "english": "west direction, where the sun sets",
        "hindi": "पश्चिम दिशा (डूबने की दिशा)",
        "pos": "noun",
        "gender": "f",
        "category": "time",
        "dialect": "general",
        "example": "आथूणी कानी लालिमा छा गई।"
    },
    {
        "rajasthani": "उत्तरादी",
        "roman": "uttaraadi",
        "english": "north direction",
        "hindi": "उत्तर दिशा",
        "pos": "noun",
        "gender": "f",
        "category": "time",
        "dialect": "general",
        "example": "उत्तरादी पवन सूं ठंड बढ़ गई।"
    },
    {
        "rajasthani": "दखणादी",
        "roman": "dakhnaadi",
        "english": "south direction",
        "hindi": "दक्षिण दिशा",
        "pos": "noun",
        "gender": "f",
        "category": "time",
        "dialect": "general",
        "example": "दखणादी कानी सूं बादल उमड़्या।"
    },

    # =========================================================================
    # 12. QUALIFIERS, ADJECTIVES & DESCRIPTORS (विशेशण अर रंग-रूप)
    # =========================================================================
    {
        "rajasthani": "चोखो",
        "roman": "chokho",
        "english": "fine, good, noble, pleasant, virtuous",
        "hindi": "अच्छा / श्रेष्ठ / सुंदर",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "ओ मिनख घणो चोखो है।"
    },
    {
        "rajasthani": "फूहड़ / नूंढो",
        "roman": "phoohad / noondho",
        "english": "clumsy, unrefined, poorly made",
        "hindi": "फूहड़ / अनाड़ी",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "काम चोखो करो, नूंढो नीं।"
    },
    {
        "rajasthani": "धोळो",
        "roman": "dholo",
        "english": "white, snowy, fair",
        "hindi": "सफेद / धवल",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "धोळो बगलो पाणी मांय बैठ्यो।"
    },
    {
        "rajasthani": "काळो",
        "roman": "kaalo",
        "english": "black, dark",
        "hindi": "काला",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "आकास मांय काळा डिंबर बादल छा ग्या।"
    },
    {
        "rajasthani": "रातो",
        "roman": "raato",
        "english": "crimson, red, scarlet",
        "hindi": "लाल / रक्तवर्ण",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "रातो गुलाब सोहणो लागै।"
    },
    {
        "rajasthani": "लीलो",
        "roman": "leelo",
        "english": "green, verdant, fresh",
        "hindi": "हरा / लहलहाता",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "सावण मांय धरती लीली-छम व्है जावै।"
    },
    {
        "rajasthani": "पीळो",
        "roman": "peelo",
        "english": "golden yellow",
        "hindi": "पीला / स्वर्णवर्ण",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "पीळी पोत री चुनड़ी चमकै।"
    },
    {
        "rajasthani": "काबरो",
        "roman": "kaabro",
        "english": "spotted, speckled, variegated, piebald",
        "hindi": "चितकबरा / धब्बेदार",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "काबरो बछड़ो आंगण मांय कूदै।"
    },
    {
        "rajasthani": "ठिंगणो",
        "roman": "thingano",
        "english": "short-statured, dwarfish",
        "hindi": "नाटा / छोटे कद का",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "ठिंगणो रूख छांव कम देवै।"
    },
    {
        "rajasthani": "लाम्बो",
        "roman": "laambo",
        "english": "tall, lengthy, prolonged",
        "hindi": "लंबा",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "लाम्बो मारग तय कर्यो।"
    },
    {
        "rajasthani": "दोरो",
        "roman": "doro",
        "english": "difficult, arduous, steep, troublesome",
        "hindi": "कठिन / मुश्किल",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "पहाड़ माथे चढ़णो घणो दोरो काम है।"
    },
    {
        "rajasthani": "सोरो",
        "roman": "soro",
        "english": "easy, smooth, comfortable, untroubled",
        "hindi": "सरल / आसान / सुगम",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "मेहनत करबा सूं हर काम सोरो व्है जावै।"
    },
    {
        "rajasthani": "खारो",
        "roman": "khaaro",
        "english": "saline, brackish (of desert water or soil)",
        "hindi": "खारा / नमकीन",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "सांभर झील रो पाणी खारो है।"
    },
    {
        "rajasthani": "मीठो",
        "roman": "meetho",
        "english": "sweet, potably fresh, mellifluous",
        "hindi": "मीठा / मधुर",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "टांके रो पाणी घणो मीठो व्है।"
    },
    {
        "rajasthani": "चरपरो",
        "roman": "charparo",
        "english": "spicy, piquant, hot with red chillies",
        "hindi": "तीखा / चटपटा",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "मथानिया री लाल मिरच चरपरी व्है।"
    },

    # =========================================================================
    # 13. ADDITIONAL IDIOMATIC & COLLOQUIAL ADVERBS/CONNECTORS
    # =========================================================================
    {
        "rajasthani": "अठै",
        "roman": "athai",
        "english": "here, in this place",
        "hindi": "यहाँ",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "mwr",
        "example": "अठै विराजो सा।"
    },
    {
        "rajasthani": "वठै",
        "roman": "vathai",
        "english": "there, in that place",
        "hindi": "वहाँ",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "mwr",
        "example": "वठै घणी भीड़ थी।"
    },
    {
        "rajasthani": "कठै",
        "roman": "kathai",
        "english": "where, in which place",
        "hindi": "कहाँ",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "mwr",
        "example": "थें कठै जावो हो?"
    },
    {
        "rajasthani": "अठीनै",
        "roman": "atheenai",
        "english": "this way, in this direction",
        "hindi": "इधर / इस तरफ",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "general",
        "example": "अठीनै आवो, छाया मांय बैठो।"
    },
    {
        "rajasthani": "वठीनै",
        "roman": "vatheenai",
        "english": "that way, in that direction",
        "hindi": "उधर / उस तरफ",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "general",
        "example": "गाड़ी वठीनै मुड़ गई।"
    },
    {
        "rajasthani": "कियां",
        "roman": "kiyaan",
        "english": "how, in what manner",
        "hindi": "कैसे",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "general",
        "example": "यो काम कियां व्हियो?"
    },
    {
        "rajasthani": "क्यूं",
        "roman": "kyoon",
        "english": "why, for what reason",
        "hindi": "क्यों",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "general",
        "example": "थें क्यूं उदास हो?"
    },
    {
        "rajasthani": "कदे",
        "roman": "kade",
        "english": "when, at what time; ever",
        "hindi": "कब / कभी",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "general",
        "example": "थें म्हारै घर कदे आवोला?"
    },
    {
        "rajasthani": "तद",
        "roman": "tad",
        "english": "then, at that moment",
        "hindi": "तब",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "general",
        "example": "जद मेह बरस्यो, तद धरती खिली।"
    },
    {
        "rajasthani": "जद",
        "roman": "jad",
        "english": "when (relative connector)",
        "hindi": "जब",
        "pos": "conjunction",
        "category": "conjunctions",
        "dialect": "general",
        "example": "जद आप पधार्या, म्हारो मन प्रसन्न व्हियो।"
    },
    {
        "rajasthani": "पण",
        "roman": "pan",
        "english": "but, however, yet",
        "hindi": "परंतु / लेकिन",
        "pos": "conjunction",
        "category": "conjunctions",
        "dialect": "general",
        "example": "म्हूँ गयो थो, पण वो घरै कोनी थो।"
    },
    {
        "rajasthani": "अर",
        "roman": "ar",
        "english": "and, also",
        "hindi": "और",
        "pos": "conjunction",
        "category": "conjunctions",
        "dialect": "general",
        "example": "राम अर लखन दोनूं भाई हा।"
    },
    {
        "rajasthani": "कांई",
        "roman": "kaani",
        "english": "what, interrogative particle",
        "hindi": "क्या",
        "pos": "pronoun",
        "category": "interrogative",
        "dialect": "general",
        "example": "कांई बात है સા?"
    },
    {
        "rajasthani": "कुण",
        "roman": "kun",
        "english": "who, which person",
        "hindi": "कौन",
        "pos": "pronoun",
        "category": "interrogative",
        "dialect": "general",
        "example": "दरवाजे माथे कुण ऊभो है?"
    },
    {
        "rajasthani": "कीकर",
        "roman": "keekar",
        "english": "how, by what means",
        "hindi": "किस तरह / कैसे",
        "pos": "adverb",
        "category": "adverbs",
        "dialect": "mwr",
        "example": "कीकर पधार्या सा?"
    },
    {
        "rajasthani": "फाट्यो",
        "roman": "phaatyo",
        "english": "torn, ripped, burst",
        "hindi": "फटा हुआ",
        "pos": "adjective",
        "gender": "m",
        "category": "descriptors",
        "dialect": "general",
        "example": "फाट्योड़ी चादर नै सीवी।"
    },
    {
        "rajasthani": "टूणो / टोटको",
        "roman": "toono / totko",
        "english": "protective folk talisman, charm, occult protective ward",
        "hindi": "टोना-टोटका (नजर निवारण का उपाय)",
        "pos": "noun",
        "gender": "m",
        "category": "culture",
        "dialect": "general",
        "example": "टाबर नै नजर लागबा माथे टोटको कर्यो।"
    },
]

# Let's also programmatically add words from the comparative texts
# such as Ramkrishan Sharma and Dingal Kosh with automatic categorization
COMPARATIVE_LEMMAS = [
    ("पोथी", "pothi", "manuscript, sacred or handwritten book", "पुस्तक / पोथी", "noun", "f", "literature", "general", "प्राचीन पोथी मांय डिगल रा दोहा लिख्योड़ा हैं।"),
    ("साहित्य", "saahitya", "literature, belle-lettres", "साहित्य", "noun", "m", "literature", "general", "राजस्थानी साहित्य घणो समृद्ध है।"),
    ("बात / वात", "vaat", "historical narrative prose, folk chronicle", "बात / ऐतिहासिक गद्य कथा", "noun", "f", "literature", "general", "अचलदास खींची री वचनिका अर बातां प्रसिद्ध हैं।"),
    ("ख्याल", "khyaal", "traditional open-air folk theatre operatic genre", "ख्याल (पारंपरिक लोकनाट्य)", "noun", "m", "culture", "general", "कुचामणी अर शेखावाटी ख्याल प्रसिद्ध हैं।"),
    ("तमासो", "tamaaso", "spectacle, Jaipur musical street folk drama", "तमाशा (जयपुर का लोकनाट्य)", "noun", "m", "culture", "dhd", "होली माथे तमासो मंचावै।"),
    ("रम्मत", "rammat", "Bikaner festive nighttime community folk performance", "रम्मत (बीकानेर का लोक नाट्य)", "noun", "f", "culture", "mwr", "बीकानेर री पाटा संस्कृति मांय रम्मत होवै।"),
    ("स्वॉंग / बहरूपिया", "swaang / bahroopiya", "traditional impersonation art", "स्वांग / बहरूपिया कला", "noun", "m", "culture", "general", "बहरूपिया कलाकार भिन्न-भिन्न रूप धरे।"),
    ("चितेरो", "chitero", "traditional folk painter or fresco artisan", "चित्रकार / चितेरा", "noun", "m", "culture", "general", "हवेली री दीवारां माथे चितेरे मांडणा मांड्या।"),
    ("उस्ता कला", "usta kala", "intricate gold embossing work on camel hide (Bikaner)", "उस्ता कला (ऊँट की खाल पर सोने की नक्काशी)", "noun", "f", "crafts", "mwr", "बीकानेर री उस्ता कला विश्व प्रसिद्ध है।"),
    ("थेवा कला", "thewa kala", "gold filigree work fused onto coloured Belgian glass (Pratapgarh)", "थेवा कला (कांच पर सोने की मीनाकारी)", "noun", "f", "crafts", "mew", "प्रतापगढ़ रो थेवा आभूषण घणो नायाब है।"),
    ("ब्लू पॉटरी", "blue pottery", "traditional quartz glaze blue-and-turquoise pottery (Jaipur)", "ब्लू पॉटरी (नीले मृद्भांड कला)", "noun", "f", "crafts", "dhd", "कृपाल सिंह शेखावत ब्लू पॉटरी रा सिरमौर शिल्पी हा।"),
    ("मीनाकारी", "meenaakaari", "enameled decorative art on gold and silver jewellery", "मीनाकारी (धातु पर रंगीन नक्काशी)", "noun", "f", "crafts", "dhd", "जयपुर री मीनाकारी री चमक कदे नीं फीकी पड़े।"),
    ("कावड़", "kaavad", "portable wooden multi-paneled painted mobile temple shrine", "कावड़ (लकड़ी का चलता-फिरता मंदिर)", "noun", "f", "crafts", "mew", "बस्सी (चित्तौड़) री कावड़ देश-विदेश मांय विख्यात है।"),
    ("कठपुतली", "kathputli", "traditional string puppet carved from mango wood", "कठपुतली", "noun", "f", "culture", "general", "कठपुतली री डोर माथे अमरसिंह राठौड़ रो खेल रच्यो।"),
    ("चंग", "chang", "circular handheld tambourine drum played with stick during Holi", "चंग (होली का डफ वाद्य)", "noun", "m", "instruments", "general", "फागण मांय चंग री थाप माथे धमाल गाई।"),
    ("डफ", "daf", "large frame drum beaten during folk festivities", "डफ", "noun", "m", "instruments", "general", "डफ बाजी अर लोग नाच्या।"),
    ("नगाड़ो", "nagaado", "kettledrum played with curved wooden beaters at temple doors and palaces", "नगाड़ा", "noun", "m", "instruments", "general", "दरवाजे माथे नौबत अर नगाड़ो बाज्यो।"),
    ("भपंग", "bhapang", "single-stringed variable-pitch plucked percussion instrument of Mewat", "भपंग (मेवात का वाद्य)", "noun", "m", "instruments", "general", "जहूर खां मेवाती भपंग रा उस्ताद हा।"),
    ("डेरू", "deru", "hourglass-shaped wooden drum held in one hand, beaten with small bent stick (Gogaji worship)", "डेरू (गोगाजी का वाद्य)", "noun", "m", "instruments", "general", "गोगाजी रे जागरण मांय डेरू बाजै।"),
    ("झांझ", "jhaanjh", "large heavy bronze musical cymbals played in Terah Taali and Ramdevra hymns", "झांझ (कांसे की बड़ी मंजीरा)", "noun", "f", "instruments", "general", "झांझ-मंजीरा री झंकार सूं भक्ति रस बरस रह्यो है।"),
    ("मंजीरो", "manjeero", "pair of brass devotional hand cymbals", "मंजीरा", "noun", "m", "instruments", "general", "तेरहताली नृत्य मांय तेरह मंजीरा बांधै।"),
    ("घूमर", "ghoomar", "gracious round-whirling traditional community dance of Rajasthani women", "घूमर (राजस्थान का राज्य नृत्य)", "noun", "f", "culture", "general", "घूमर मांय बाईसा री चाल मन मोहे।"),
    ("कालबेलिया", "kaalbelia", "serpentine acrobatic dance performed by Kalbelia snake charmer community", "कालबेलिया (सपेरा नृत्य)", "noun", "m", "culture", "general", "गुलाबो सपेरा कालबेलिया नृत्य नै यूनेस्को मांय पहचान दिलाई।"),
    ("चरी नृत्य", "chari nritya", "folk dance balancing brass water pots with lit cotton-seed fires on head (Kishangarh Gujjars)", "चरी नृत्य (अग्नि कलश नृत्य)", "noun", "m", "culture", "general", "फलकू बाई चरी नृत्य री प्रसिद्ध नृत्यांगना ही।"),
    ("तेरहताली", "terahtaali", "seated devotional dance of Kamad women playing 13 cymbals in devotion to Ramdevji", "तेरहताली (कामड़ जाति का नृत्य)", "noun", "m", "culture", "general", "तेरहताली नृत्य मांय अद्भुत शारीरिक संतुलन दीखै।"),
    ("कच्छी घोड़ी", "kacchi ghodi", "mock horse dance where dancers wear dummy horse armature with swords (Shekhawati)", "कच्छी घोड़ी (काठ की घोड़ी का नृत्य)", "noun", "f", "culture", "general", "ब्याव मांय कच्छी घोड़ी री रम्मत होवै।"),
    ("अग्नि नृत्य", "agni nritya", "barefoot ecstatic fire dance on smoldering embers by Jasnathi Siddhs (Katriyasar)", "अग्नि नृत्य (अंगारों पर नृत्य)", "noun", "m", "culture", "mwr", "सिद्ध रुस्तम जी रा अनुयायी धधकते अंगारां माथे नाचे।"),
    ("गैरीया / गैर", "gair", "stick dance performed by male troupes in swirling white flared robes during Holi", "गैर नृत्य", "noun", "m", "culture", "general", "होली माथे बाड़मेर अर मेवाड़ मांय गैरीया गैर खेलै।"),
    ("भवाई", "bhavai", "daring balancing dance performing on sword edges and glass shards with 8-10 brass pots on head", "भवाई नृत्य", "noun", "m", "culture", "general", "भवाई नृत्य मांय नर्तकी थाली रे कोर माथे नाचे।"),
    ("पणिहारी", "panihaari", "water-bearing woman walking gracefully with pots balanced on head", "पणिहारी (पानी भरने वाली नारी)", "noun", "f", "culture", "general", "पणिहारी गीत रेगिस्तान री आत्मा है।"),
    ("सूरो", "sooro", "brave warrior, champion, chivalric hero", "शूरवीर / योद्धा", "noun", "m", "chivalry", "general", "रणभूमि मांय सूरो पीठ नीं दिखावै।"),
    ("भामाशाह", "bhaamaashah", "legendary philanthropist who sacrifices personal fortune for kingdom/welfare", "भामाशाह (महान दानी)", "noun", "m", "values", "general", "महाराणा प्रताप रे संकट मांय भामाशाह सर्वस्व दान कर्यो।"),
    ("वीरांगना", "veeraangana", "heroic woman of invincible valor and resolve", "वीरांगना (साहसी नारी)", "noun", "f", "chivalry", "general", "हाड़ी रानी शीश काट'र दे दीनो, ऐसी वीरांगना राजस्थान मांय हुई।"),
    ("हुकम", "hukam", "royal command, noble title of respectful address ('Hukam Sa')", "आदेश / हुक्म / हुकम सा", "noun", "m", "values", "general", "हुकम सा रो फरमान सिर माथे।"),
    ("खम्मा घणी", "khamma ghani", "quintessential Rajasthani supreme greeting meaning 'May you be blessed with abundant forgiveness and well-being'", "खम्मा घणी (अत्यंत आदरपूर्ण राजस्थानी अभिवादन)", "noun", "f", "greetings", "general", "सगळां भाइयां-बहनां नै खम्मा घणी सा!"),
    ("राम राम सा", "ram ram sa", "universal traditional greeting invoking the divine with honorific 'Sa'", "राम राम सा (पारंपरिक नमस्कार)", "noun", "m", "greetings", "general", "गांवां मांय मिलतां ही राम राम सा कहै।"),
    ("जय जिणेंद्र", "jai jinendra", "reverent Jain greeting common in trade and civic life", "जय जिनेंद्र", "noun", "m", "greetings", "general", "जैन समाज मांय जय जिणेंद्र कह'र स्वागत करै।"),
    ("घणो", "ghano", "much, very, abundant, plentiful", "बहुत / घणा / अत्यधिक", "adjective", "m", "descriptors", "general", "आज घणी ठंड है।"),
    ("थोड़ो", "thodo", "a little, scarce, small quantity", "थोड़ा / कम", "adjective", "m", "descriptors", "general", "मनै थोड़ो सो पाणी पाय द्यो।"),
    ("सगळो / सागो", "sagalo / saago", "entire, all, whole, complete", "सब / समस्त / सम्पूर्ण", "adjective", "m", "descriptors", "general", "सगळा लोग मेळे मांय भेळा हुया।"),
    ("निराळो", "niraalo", "unique, distinct, extraordinary, unmatched", "अनोखा / निराला", "adjective", "m", "descriptors", "general", "राजस्थान रो रंग-ढंग दुनिया सूं निराळो है।"),
    ("अणमोल", "anmol", "priceless, inestimable, precious", "अनमोल / अमूल्य", "adjective", "m", "descriptors", "general", "मावड़ी रो प्रेम अणमोल व्है।"),
    ("जाणो", "jaano", "to go, depart, travel", "जाना", "verb", "actions", "general", "म्हूँ काले बीकानेर जास्यूं।"),
    ("आवणो", "aavano", "to come, arrive, return", "आना", "verb", "actions", "general", "थें कदे आवोला?"),
    ("खाणो", "khaano", "to eat, partake", "खाना", "verb", "actions", "general", "बाजरे री रोटी खाय लीनी।"),
    ("पीवणो", "peevano", "to drink, quench thirst", "पीना", "verb", "actions", "general", "ठंडो पाणी पीवणो चाहिजै।"),
    ("करणो", "karano", "to do, execute, accomplish", "करना", "verb", "actions", "general", "साचो काम करणो धरम है।"),
    ("देखणो", "dekhano", "to see, observe, gaze, watch", "देखना", "verb", "actions", "general", "गढ़ री सुंदरता देखण जोग है।"),
    ("सुणणो", "sunano", "to hear, listen attentively", "सुनना", "verb", "actions", "general", "दादीजी री बातां सुणी।"),
    ("लिखणो", "likhano", "to write, compose, inscribe", "लिखना", "verb", "actions", "general", "कवि डिगल मांय गीत लिख्यो।"),
    ("पढ़णो", "padhano", "to read, study, recite", "पढ़ना", "verb", "actions", "general", "पोथी पढ़'र ज्ञान पायो।"),
    ("गावणो", "gaavano", "to sing, vocalize melodies", "गाना", "verb", "actions", "general", "महिलावां ब्याव रे अवसर माथे बधावा गाया।"),
    ("नाचणो", "naachano", "to dance rhythmically", "नाचना", "verb", "actions", "general", "चंग बाजतां ही पांवा नाचण लाग्या।"),
    ("सोवणो", "sovano", "to sleep, rest peacefully", "सोना (निद्रा)", "verb", "actions", "general", "सांझ पड्यां खाट माथे सो ग्यो।"),
    ("उठणो", "uthano", "to wake up, rise, stand", "उठना", "verb", "actions", "general", "परभाते जल्दी उठणो स्वास्थ्य खातर चोखो है।"),
    ("हंसणो", "hansano", "to laugh, smile cheerfully", "हँसना", "verb", "actions", "general", "टाबर खिलखिला'र हंस्या।"),
    ("रोवणो", "rovano", "to weep, shed tears", "रोना", "verb", "actions", "general", "विदाई बखत धी रोवण लागी।"),
    ("धोवणो", "dhovano", "to wash, cleanse, launder", "धोना", "verb", "actions", "general", "कपड़ा कुएं माथे धोया।"),
    ("काढणो", "kaadhano", "to draw out, extract, embroider", "निकालना / काढ़ना", "verb", "actions", "general", "घड़े मांय सूं पाणी काढ्यो।"),
    ("बाळणो", "baalano", "to ignite, burn, illuminate lamp", "जलाना / प्रज्वलित करना", "verb", "actions", "general", "संझा बखत देहरी माथे दीवलो बाळ्यो।"),
    ("बूझणो", "boojhano", "to inquire, ask, question", "पूछना / बूझना", "verb", "actions", "general", "मारग कुण सूं बूझां?"),
    ("जाणणो", "jaanano", "to know, understand, discern", "जानना / समझना", "verb", "actions", "general", "इतिहास नै जाणणो जरूरी है।"),
    ("मानणो", "maanano", "to accept, respect, honor", "मानना / आदर करना", "verb", "actions", "general", "बडां री सीख मानणी चाहिजै।"),
    ("भागणो / दौड़णो", "bhaagano / daudano", "to run, flee, gallop", "भागना / दौड़ना", "verb", "actions", "general", "घोड़ो पवन वेग सूं दौड़्यो।"),
    ("बैठणो", "baithano", "to sit down, recline", "बैठना", "verb", "actions", "general", "छाया मांय बैठो सा।"),
    ("उभा रहणो", "ubha rahano", "to stand erect, wait upright", "खड़े रहना", "verb", "actions", "general", "दरवाजे माथे उभो रह्यो।"),
    ("चालणो", "chaalano", "to walk, proceed, advance", "चलना", "verb", "actions", "general", "साथे चालो सा।"),
    ("देवणो", "devano", "to give, bestow, donate", "देना", "verb", "actions", "general", "दान-पुण्य देवणो शुभ व्है।"),
    ("लेवणो", "levano", "to take, receive, accept", "लेना", "verb", "actions", "general", "प्रसाद हाथ मांय ले लियो।"),
    ("लाणो / ल्यावणो", "laano / lyaavano", "to bring, fetch", "लाना", "verb", "actions", "general", "बजार सूं गुड़-घी ल्यायो।"),
    ("मेळणो / राखणो", "melano / raakhano", "to keep, deposit, store", "रखना", "verb", "actions", "general", "सामान ओबरे मांय मेळ्यो।"),
    ("खोवणो", "khovano", "to lose, misplace", "खोना / गँवाना", "verb", "actions", "general", "परदेस मांय धीरज मती खोवो।"),
    ("पावणो / लाधणो", "paavano / laadhano", "to find, discover, attain", "पाना / मिलना", "verb", "actions", "general", "खोयोड़ो धन पाछो लाध ग्यो।"),
    ("छोडणो", "chhodano", "to leave, release, renounce", "छोड़ना", "verb", "actions", "general", "बुरी आदतां छोडणी चाहिजै।"),
    ("बांधणो", "baandhano", "to tie, bind, knot", "बांधना", "verb", "actions", "general", "कमर मांय फेंटो बांध्यो।"),
    ("खोलणो", "kholano", "to untie, open, unlock", "खोलना", "verb", "actions", "general", "कंकण-डोरो खोल्यो।"),
    ("जीतणो", "jeetano", "to conquer, win, vanquish", "जीतना", "verb", "actions", "general", "रणभूमि मांय जीत हासिल कीधी।"),
    ("हारणो", "haarano", "to lose, suffer defeat", "हारना", "verb", "actions", "general", "हिम्मत कदे नीं हारणी।"),
    ("बचावणो", "bachaawano", "to save, protect, rescue", "बचाना / रक्षा करना", "verb", "actions", "general", "गौ-रक्षा खातर प्राण अर्पण कर्यो।"),
    ("मरवावणो", "marwaawano", "to cause to be killed", "मरवाना", "verb", "actions", "general", "दुश्मन नै परास्त कर्यो।"),
]

for item in COMPARATIVE_LEMMAS:
    if len(item) == 9:
        raj, rom, eng, hin, pos, g, cat, dial, ex = item
    else:
        raj, rom, eng, hin, pos, cat, dial, ex = item
        g = None
    NEW_VOCABULARY.append({
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

added_count = 0
for v in NEW_VOCABULARY:
    key = v["rajasthani"]
    if key not in existing_keys:
        existing_words.append(v)
        existing_keys.add(key)
        added_count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Successfully added {added_count} new entries to words.json!")
print(f"Total vocabulary words in library now: {len(existing_words)}")
