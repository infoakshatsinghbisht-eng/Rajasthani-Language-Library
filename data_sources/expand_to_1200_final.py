# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

WORDS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "rajasthani", "lexicon", "data", "words.json")
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip() for w in words}

FINAL_BATCH = [
    # --- Spices & Traditional Culinary Items ---
    ("जीरो", "jeero", "fragrant cumin seeds, supreme cash-crop of Western Rajasthan", "जीरा", "noun", "m", "food", "mwr", "जीरे री खेती में घणी मेहनत है।"),
    ("धाणो", "dhaano", "aromatic coriander seeds used in curry powder", "धनिया (साबुत)", "noun", "m", "food", "mwr", "दाल में पिसे धाणे री खुशबू आई।"),
    ("मेथी", "methi", "fenugreek seeds, famous from Nagaur (Kasoori Methi)", "मेथी (नागौरी पान मेथी)", "noun", "f", "food", "mwr", "नागौरी मेथी री खुशबू देश भर में प्रसिद्ध है।"),
    ("अजवायन", "ajvaayan", "carom seeds used for stomach digestive health", "अजवायन", "noun", "f", "food", "mwr", "सोगरे में अजवायन नांखी।"),
    ("सोंठ", "sonth", "dried powdered ginger root used in winter tonics", "सोंठ (सूखी अदरक)", "noun", "f", "food", "mwr", "गोंद रा लाडू में सोंठ नांखी।"),
    ("राई", "raai", "small black mustard seeds popped in oil tadka", "राई / सरसों", "noun", "f", "food", "mwr", "सब्जी में राई रो छौंक लगायो।"),
    ("हळदी", "haldhi", "auspicious ground turmeric used in healing and wedding baan", "हल्दी", "noun", "f", "food", "mwr", "बान में हळदी रो लेप कियो।"),
    ("मावो", "maavo", "slowly reduced thickened whole milk solids for festive sweets", "मावा / खोया", "noun", "m", "food", "mwr", "मावे री कचौरी जोधपुर री शान है।"),
    ("मिश्री", "mishri", "crystallized raw rock sugar offered with saunf", "मिश्री (प्रसाद)", "noun", "f", "food", "mwr", "पावणा नै मिश्री-सौंफ री मनवार करी।"),
    ("पतासो", "pataaso", "porous aerated drop sugar candies distributed at temples", "बताशा (पतासा)", "noun", "m", "food", "mwr", "आरती पछै पतासा बांट्या।"),
    ("नुक्ती", "nukti", "tiny golden fried chickpea-flour droplet pearls soaked in syrup", "नुक्ती / मीठी बूंदी", "noun", "f", "food", "mwr", "ब्याव में नुक्ती-लापसी बणी।"),
    ("मखानो", "makhaano", "popped foxnut lotus seeds used in fasting feasts", "मखाना", "noun", "m", "food", "mwr", "खीर में मखाना नांख्यो।"),

    # --- Desert Grasses, Pasture Herbs & Trees ---
    ("सेवण", "sevan", "nutritious perennial desert pasture grass (Lasiurus scindicus) thriving on dry sand", "सेवण घास (थार की अमृत घास)", "noun", "f", "flora", "mwr", "सेवण घास खा'र गायां खूब दूध देवै।"),
    ("धामण", "dhaaman", "succulent desert grass (Cenchrus ciliaris) rich in protein for sheep and cows", "धामण घास", "noun", "f", "flora", "mwr", "धामण घास धोरां माथे उगै।"),
    ("करड़", "karad", "drought-hardy desert fodder grass grazed by camels", "करड़ घास", "noun", "f", "flora", "mwr", "करड़ घास पशुवां नै भावे।"),
    ("शीशम", "sheesham", "dense durable rosewood tree used by carpenters for doors and cartwheels", "शीशम (काष्ठ वृक्ष)", "noun", "m", "flora", "mwr", "शीशम री लकड़ी सूं किवाड़ बणायो।"),
    ("सिरस", "siras", "fragrant white-flowered shade tree (Albizia lebbeck)", "सिरस (छायादार वृक्ष)", "noun", "m", "flora", "mwr", "सिरस रै नीचे चौपाल लगी।"),
    ("नीम", "neem", "sacred medicinal neem tree purifying desert air and healing wounds", "नीम (औषधीय वृक्ष)", "noun", "m", "flora", "mwr", "नीम री छांव सुखदायी व्है।"),
    ("पीपल", "peepal", "sacred ficus tree revered as divine abode of ancestors", "पीपल (देववृक्ष)", "noun", "m", "flora", "mwr", "पीपल री परिक्रमा करी।"),
    ("बड़", "bad", "ancient spreading banyan tree with aerial roots (Vat Vriksha)", "बरगद / बड़ (वट वृक्ष)", "noun", "m", "flora", "mwr", "गाँव रै बीचां मोटो बड़ है।"),
    ("इमली", "imli", "tamarind tree bearing tart pod fruit used in chutneys", "इमली", "noun", "f", "flora", "mwr", "इमली री खटाई सूं तरकारी बणी।"),
    ("खजूर", "khajoor", "desert date palm thriving in arid oasis zones", "खजूर का पेड़", "noun", "m", "flora", "mwr", "जैसलमेर में खजूर रा बगोचा हैं।"),

    # --- Artisans, Guilds & Social Roles ---
    ("पटवो", "patwo", "traditional artisan braiding colorful silk threads for royal jewelry and amulets", "पटवा (रेशमी धागा पिरोने वाला)", "noun", "m", "crafts", "mwr", "पटवों री हवेली जैसलमेर में दर्शनीय है।"),
    ("मोची", "mochi", "traditional leather artisan hand-crafting durable Jodhpuri and Jaipuri mojris", "मोची (जूती बनाने वाला)", "noun", "m", "crafts", "mwr", "मोची बारीक कशीदे वाळी मोजड़ी घढ़ी।"),
    ("धोबी", "dhobi", "traditional village washerman cleansing garments at river ghats", "धोबी", "noun", "m", "crafts", "mwr", "धोबी घाट माथे वस्त्र धोवै।"),
    ("बलाई", "balaai", "traditional rural weaver weaving coarse cotton reza and durries", "बलाई (बुनकर समुदाय)", "noun", "m", "crafts", "mwr", "बलाई खादी रो थान बुण्यो।"),

    # --- Kinship Honorifics & Affectionate Nuances ---
    ("मायड़", "maayad", "sacred affectionate poetic word for Mother / Motherland", "मायड़ (मां / मातृभूमि)", "noun", "f", "kinship", "mwr", "मायड़ भाषा राजस्थानी री जय होवे!"),
    ("बापजी", "baapji", "venerated royal patriarch address for king, saint or revered grandfather", "बापजी (महाराजा अथवा पूज्य पिता)", "noun", "m", "kinship", "mwr", "बापजी दरबार में पधार्या।"),
    ("बाईजी", "baaiji", "revered title for princess, aunt, or respected elder woman", "बाईजी (पूज्य बुआजी अथवा राजकुमारी)", "noun", "f", "kinship", "mwr", "बाईजी मंदिर में दर्शन कियो।"),
    ("भंवर", "bhanwar", "chivalric title for a young Rajput nobleman or beloved husband in folk songs", "भंवर (राजकुमार / साजन)", "noun", "m", "culture", "mwr", "केसरिया भंवर म्हारो देस पधारो!"),
    ("कंवर", "kanwar", "princely title of the son or heir of a Thakur or ruler", "कुंवर (राजकुमार)", "noun", "m", "culture", "mwr", "कुंवर सा शिकार सूं पाछा आया।"),
    ("बींद", "beend", "the bridegroom on his wedding day adorned in royal attire", "दूल्हा (बींद)", "noun", "m", "kinship", "mwr", "बींद घोड़ी माथे सज्यो।"),
    ("बींदणी", "beendani", "the newly-wed bride arriving at her marital home", "दुल्हन (बींदणी)", "noun", "f", "kinship", "mwr", "बींदणी रै पगल्यो रो स्वागत कियो।"),
    ("अन्नदाता", "anndaata", "sovereign master and provider of sustenance", "अन्नदाता (महाराज / स्वामी)", "noun", "m", "honorifics", "mwr", "अन्नदाता री जय होवे।"),
    ("हुकम", "hukam", "sovereign command; royal form of respectful compliance ('as you command')", "हुकम (आज्ञा / श्रीमान)", "noun", "m", "honorifics", "mwr", "हुकम, आपरो आदेश सिर माथे।")
]

added = 0
for item in FINAL_BATCH:
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

print(f"Added {added} final batch words! Grand total lexicon now: {len(words)}")
