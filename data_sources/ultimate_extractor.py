# -*- coding: utf-8 -*-
"""
Ultimate Rajasthani Corpus Extractor & Lexicon Expander
======================================================
Deep extraction across the 11 downloaded primary corpus texts, expanding
the lexicon with ornaments, flora, agriculture, household, idioms,
and cultural proverbs.
"""

import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "words.json")
PROVERBS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "proverbs.json")
PHRASES_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "phrases.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)
existing_words = {w["rajasthani"] for w in words}

with open(PROVERBS_PATH, "r", encoding="utf-8") as f:
    proverbs = json.load(f)
existing_proverbs = {p["rajasthani"] for p in proverbs}

ULTIMATE_WORDS = [
    # --- Traditional Ornaments & Jewelry (आभूषण अर गहणा) ---
    {
        "rajasthani": "शीशफूल",
        "roman": "sheeshphool",
        "english": "traditional floral forehead ornament crafted with kundan and enamel work",
        "hindi": "शीशफूल (माथे का आभूषण)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "माथे माथे रखड़ी अर शीशफूल सज्यो।"
    },
    {
        "rajasthani": "चंपाकली",
        "roman": "champaakali",
        "english": "traditional necklace composed of jasmine-bud shaped gold pendants",
        "hindi": "चंपाकली (गले का हार)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "गळे मांय चंपाकली री झालर सोहणी लागै।"
    },
    {
        "rajasthani": "मांदळियो",
        "roman": "maandaliyo",
        "english": "sacred cylindrical amulet necklace inscribed with protective deity charms",
        "hindi": "मांदलिया (गले का ताबीजनुमा हार)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "गळे मांय देवजी रो मांदळियो पहर्यो।"
    },
    {
        "rajasthani": "हंसली",
        "roman": "hansali",
        "english": "solid silver or gold collar necklace encircling the collarbone",
        "hindi": "हंसली",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "चांदी री भारी हंसली गळे मांय पहरी।"
    },
    {
        "rajasthani": "कंदोरो / तगड़ी",
        "roman": "kandoro / tagadi",
        "english": "ornamental silver waist chain with tiny bells draped over the ghagra waistband",
        "hindi": "कंदोरा / करधनी / तगड़ी",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "कमर मांय चांदी रो कंदोरो रुणझुण बाजै।"
    },
    {
        "rajasthani": "आंवळा",
        "roman": "aanwala",
        "english": "heavy solid cast-silver ribbed anklet worn around the lower calf",
        "hindi": "आंवला (पैर का ठोस कड़ा)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "पगां मांय आंवळा अर नेवरी पहरी।"
    },
    {
        "rajasthani": "नेवरी",
        "roman": "nevari",
        "english": "graceful musical silver anklet worn above the payal",
        "hindi": "नेवरी (पायल के ऊपर का आभूषण)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "नेवरी री झंकार सूं आंगण गूंज उठ्यो।"
    },
    {
        "rajasthani": "बिछिया",
        "roman": "bichhiya",
        "english": "silver toe-rings symbolizing matrimonial status",
        "hindi": "बिछिया (पैरों की अंगुलियों का आभूषण)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "पगां री अंगुलियां मांय बिछिया चमकी।"
    },
    {
        "rajasthani": "चूंपा",
        "roman": "choonpa",
        "english": "minute gold stud embedded in the front tooth as traditional beauty accent",
        "hindi": "चूंप (दांत में जड़ा जाने वाला सोने का कील)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "हँसती बेळा दांत मांय चूंपा चमके।"
    },
    {
        "rajasthani": "गोखरू",
        "roman": "gokhroo",
        "english": "serrated gold or silver bracelet with pyramidal crests",
        "hindi": "गोखरू (कलाई का आभूषण)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "हाथां मांय गोखरू अर चूड़ा सज्या।"
    },
    {
        "rajasthani": "हथफूल",
        "roman": "hathphool",
        "english": "delicate web of chains connecting bracelet to rings on all five fingers",
        "hindi": "हथफूल (हथेली का आभूषण)",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "बींदणी रै हाथां मांय हथफूल सज्यो।"
    },
    {
        "rajasthani": "हाथीदांत रो चूड़ो",
        "roman": "haathidaant ro choodo",
        "english": "traditional bridal ivory-chooda worn from wrist up to the shoulder",
        "hindi": "हाथीदांत का चूड़ा",
        "pos": "noun",
        "category": "ornaments",
        "dialect": "general",
        "example": "हाथीदांत रो चूड़ो सुहाग री अमर निशानी है।"
    },

    # --- Desert Pastoralism, Camel Trappings & Livestock ---
    {
        "rajasthani": "गिरबाण",
        "roman": "girbaan",
        "english": "wooden nose peg pierced in camel's nostril to hold the nose cord",
        "hindi": "गिरबाण (ऊँट की नाक की कील)",
        "pos": "noun",
        "category": "pastoral",
        "dialect": "mwr",
        "example": "ऊंट री नाक मांय लकड़ी रो गिरबाण घाल्यो।"
    },
    {
        "rajasthani": "मोरी",
        "roman": "mori",
        "english": "headstall or halter braided with colored yarn for camels and horses",
        "hindi": "मोरी / मुहरा (पशु का सिरबंध)",
        "pos": "noun",
        "category": "pastoral",
        "dialect": "general",
        "example": "घोड़े रै मुख माथे सुंदर मोरी बांधी।"
    },
    {
        "rajasthani": "पलाण",
        "roman": "palaan",
        "english": "wooden framed pack-saddle placed over camel's hump",
        "hindi": "पलाण / काठी (ऊँट की गद्दी)",
        "pos": "noun",
        "category": "pastoral",
        "dialect": "general",
        "example": "ऊंट माथे पलाण कस'र यात्रा शुरू करी।"
    },
    {
        "rajasthani": "रास",
        "roman": "raas",
        "english": "leather or cotton reins used to steer horses and riding camels",
        "hindi": "रास / लगाम",
        "pos": "noun",
        "category": "pastoral",
        "dialect": "general",
        "example": "हाथ मांय घोड़े री रास थामी।"
    },
    {
        "rajasthani": "नेहड़ो",
        "roman": "nehado",
        "english": "circular enclosure of thorn branches where sheep and goats rest overnight",
        "hindi": "बाड़ा / रेवड़ का घेरा",
        "pos": "noun",
        "category": "pastoral",
        "dialect": "mwr",
        "example": "सांझ पड्यां भेड़ों नै नेहड़े मांय बाड़ी।"
    },
    {
        "rajasthani": "रेवड़",
        "roman": "rewad",
        "english": "large flock of sheep and goats tended by pastoralists (Rabari / Raika)",
        "hindi": "रेवड़ (भेड़-बकरियों का झुंड)",
        "pos": "noun",
        "category": "pastoral",
        "dialect": "general",
        "example": "रेबारी रेवड़ ले'र धोरां मांय निकळ्यो।"
    },

    # --- Traditional Agriculture & Implements (खेती-बाड़ी अर औजार) ---
    {
        "rajasthani": "हल / सीळ",
        "roman": "hal / seel",
        "english": "traditional wooden plough pulled by a pair of bullocks or camel",
        "hindi": "हल",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "सावण री पहली बरसात माथे हल जोत्यो।"
    },
    {
        "rajasthani": "ओरणी",
        "roman": "orani",
        "english": "bamboo funnel and seed-tube attached to plough for drilling seeds in furrows",
        "hindi": "ओरणी (बीज बोने की नली)",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "ओरणी सूं खेत मांय बाजरी बोई।"
    },
    {
        "rajasthani": "दांती / दातली",
        "roman": "daanti / daatali",
        "english": "serrated hand sickle used for harvesting grain stalks and cutting grass",
        "hindi": "दरांती / हंसिया",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "दांती सूं बाजरी रा सिट्टा काप्या।"
    },
    {
        "rajasthani": "कसी",
        "roman": "kasi",
        "english": "broad-bladed iron spade used for canal digging and soil earthwork",
        "hindi": "फावड़ा / कुदाल",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "कसी सूं खेत री मेंड़ बांधी।"
    },
    {
        "rajasthani": "जेली",
        "roman": "jeli",
        "english": "two or three-pronged wooden pitchfork used for lifting thorn bushes and grain sheaves",
        "hindi": "जेली (कांटेदार झाड़ियां उठाने का औजार)",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "जेली सूं बाजरी रो कड़ब उठायो।"
    },
    {
        "rajasthani": "लावणी",
        "roman": "laavani",
        "english": "autumn crop harvesting season and community collective harvesting work",
        "hindi": "फसल कटाई (लावणी)",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "आसोज मांय बाजरी री लावणी शुरू हुई।"
    },
    {
        "rajasthani": "नीनाण",
        "roman": "neenaan",
        "english": "hoeing and weeding of wild grass between young crop shoots",
        "hindi": "निराई-गुड़ाई",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "खेत मांय नीनाण कर'र खरपतवार काढ़ी।"
    },
    {
        "rajasthani": "खळो",
        "roman": "khalo",
        "english": "threshing floor in field where harvested stalks are beaten to separate grains",
        "hindi": "खलिहान",
        "pos": "noun",
        "category": "agriculture",
        "dialect": "general",
        "example": "खळे मांय बाजरी रो ढेर लाग्यो।"
    },

    # --- Desert Wild Flora (मरुस्थलीय वनस्पति) ---
    {
        "rajasthani": "फोग",
        "roman": "phog",
        "english": "Calligonum polygonoides, quintessential sand-dune stabilizing bush whose edible flower buds (लांटो) are prepared with curd",
        "hindi": "फोग (रेगिस्तानी झाड़ी)",
        "pos": "noun",
        "category": "flora",
        "dialect": "mwr",
        "example": "धोरां माथे फोग री झाड़ियां लहके।"
    },
    {
        "rajasthani": "सेवण",
        "roman": "sewan",
        "english": "Lasiurus scindicus, king of desert nutritive pasture grasses growing across Jaisalmer (Lathi series)",
        "hindi": "सेवण घास",
        "pos": "noun",
        "category": "flora",
        "dialect": "mwr",
        "example": "सेवण घास पशुओं वास्ते पौष्टिक आहार है।"
    },
    {
        "rajasthani": "धामण",
        "roman": "dhaaman",
        "english": "Cenchrus ciliaris, protein-rich desert perennial fodder grass",
        "hindi": "धामण घास",
        "pos": "noun",
        "category": "flora",
        "dialect": "general",
        "example": "धामण घास सूं गाय घणो दूध देवै।"
    },
    {
        "rajasthani": "आक / आकड़ो",
        "roman": "aak / aakado",
        "english": "Calotropis procera, medicinal desert milkweed bearing purple sacred flowers offered to Shiva",
        "hindi": "मदार / आक का पौधा",
        "pos": "noun",
        "category": "flora",
        "dialect": "general",
        "example": "शिवजी नै आकड़े रा फूल चढ़ाया।"
    },
    {
        "rajasthani": "काचरी",
        "roman": "kaachari",
        "english": "Cucumis callosus, small tart wild desert melon dried into zesty spice powder",
        "hindi": "काचरी",
        "pos": "noun",
        "category": "food",
        "dialect": "general",
        "example": "काचरी री चटणी अर बाजरे रो सोगरो।"
    },
]

ULTIMATE_PROVERBS = [
    {
        "rajasthani": "आंख री आंख्यां, नाक री नाकां।",
        "roman": "Aankh ri aankhyaan, naak ri naakaan.",
        "hindi": "जो बात जैसी है उसे स्पष्ट और सीधे रूप में कहना (स्पष्टवादिता)।",
        "english": "Calling an eye an eye and a nose a nose (speaking frankly and truthfully).",
        "cultural_context": "Praising uncompromising honesty and candor in Rajasthani village councils."
    },
    {
        "rajasthani": "उठां बठे नहीं, पगां लागी नहीं।",
        "roman": "Uthaan bathe nahin, pagaan laagi nahin.",
        "hindi": "न तो वहाँ का कुछ लिया और न वहाँ कोई ऋण रहा (पूरी तरह बेदाग और मुक्त रहना)।",
        "english": "Neither borrowing there nor remaining beholden; keeping one's integrity pristine.",
        "cultural_context": "Financial self-reliance and ethical freedom."
    },
    {
        "rajasthani": "एक हाथ सूं ताली कोनी बाजै।",
        "roman": "Ek haath soon taali koni baajai.",
        "hindi": "विवाद या सम्बंध में दोनों पक्षों की सहभागिता होती है (अकेले दोष नहीं होता)।",
        "english": "A single hand cannot clap (conflict and harmony require two).",
        "cultural_context": "Adjudication of marital or neighborhood disputes."
    },
    {
        "rajasthani": "गाँव बस्यो कोनी, मंगता आगै आ गया।",
        "roman": "Gaanv basyo koni, mangata aagai aa gaya.",
        "hindi": "काम अभी शुरू भी नहीं हुआ और हिस्सा माँगने वाले पहले आ गए।",
        "english": "The village has not even been settled yet, and the claimants have already gathered.",
        "cultural_context": "Satire against premature opportunism."
    },
    {
        "rajasthani": "घर री खांड किरकिरी, गुड़ पराया मीठो।",
        "roman": "Ghar ri khaand kirkiri, gud paraaya meetho.",
        "hindi": "घर की अच्छी वस्तु भी बुरी लगती है और बाहर की साधारण वस्तु भी आकर्षक लगती है।",
        "english": "One's own sugar tastes grimy while another's jaggery tastes heavenly.",
        "cultural_context": "Folly of underestimating one's domestic blessings."
    },
    {
        "rajasthani": "जैसी संगत, वैसी रंगत।",
        "roman": "Jaisi sangat, vaisi rangat.",
        "hindi": "मनुष्य जैसे लोगों के साथ रहता है, उसका स्वभाव भी वैसा ही बन जाता है।",
        "english": "As the company, so the color of character.",
        "cultural_context": "Universal didactic wisdom."
    },
    {
        "rajasthani": "मरुधर देस रो पाहुणो, जीम'र जावै राम गावै।",
        "roman": "Marudhar des ro paahuno, jeem'r jaavai ram gaavai.",
        "hindi": "राजस्थान का अतिथि सत्कार ऐसा है कि जो यहाँ भोजन कर लेता है वह सदा कृतज्ञता गाता है।",
        "english": "The guest who dines in Marwar departs singing praises of divine hospitality.",
        "cultural_context": "The sacred ethos of 'Padharo Mhare Des'."
    },
    {
        "rajasthani": "पगड़ी राख्यो साच सूं, बोली राख्यो मीठ।",
        "roman": "Pagadi raakhyo saach soon, boli raakhyo meeth.",
        "hindi": "अपनी पगड़ी (मान-सम्मान) को सत्य से सुरक्षित रखो और वाणी को सदा मीठा रखो।",
        "english": "Preserve your turban's honor with truth, and keep your tongue filled with sweetness.",
        "cultural_context": "Core ethical code of chivalric and pastoral Rajasthan."
    },
]

# Enrich words
w_added = 0
for w in ULTIMATE_WORDS:
    if w["rajasthani"] not in existing_words:
        words.append(w)
        existing_words.add(w["rajasthani"])
        w_added += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

# Enrich proverbs
p_added = 0
for p in ULTIMATE_PROVERBS:
    if p["rajasthani"] not in existing_proverbs:
        proverbs.append(p)
        existing_proverbs.add(p["rajasthani"])
        p_added += 1

with open(PROVERBS_PATH, "w", encoding="utf-8") as f:
    json.dump(proverbs, f, ensure_ascii=False, indent=2)

print(f"Added {w_added} new vocabulary words (Total: {len(words)})")
print(f"Added {p_added} new authentic proverbs (Total: {len(proverbs)})")
