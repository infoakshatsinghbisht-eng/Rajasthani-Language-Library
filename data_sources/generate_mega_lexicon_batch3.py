# -*- coding: utf-8 -*-
"""
Expand Mega Lexicon Batch 3
===========================
Adds spices, cash crops, grasses, musical terms, folk song genres,
and ceremonial items.
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

BATCH_3 = [
    # Cash Crops, Spices & Herbs
    ("गूंद", "goond", "edible Acacia gum resin fried in pure ghee for nutritious winter laddus", "गोंद (पेड़ का खाने योग्य गोंद)", "noun", "m", "food", "general", "सर्दियां मांय गूंद रा लाडू बणावै।"),
    ("इसबगोल", "isabgol", "psyllium husk, major medicinal desert cash crop of Jalore and Barmer", "ईसबगोल", "noun", "m", "agriculture", "general", "जालोर मांय इसबगोल री बंपर पैदावार हुवै।"),
    ("पान मेथी", "paan methi", "fragrant dried fenugreek leaves of Nagaur with geographic indication", "नागौरी कसूरी मेथी", "noun", "f", "agriculture", "general", "नागौरी पान मेथी री महक दूर-दूर तक जावै।"),
    ("जीरो", "jeero", "cumin seeds, vital aromatic desert spice crop", "जीरा", "noun", "m", "agriculture", "general", "जीरे री खेती सूं किसान खुशहाल हुया।"),
    ("धणीयो", "dhaniyo", "coriander seeds produced in massive quantities in Hadoti / Ramganj Mandi", "धनिया", "noun", "m", "agriculture", "hoj", "रामगंज मंडी एशिया री सबसे बड़ी धणीया री मंडी है।"),
    ("राई", "raai", "small pungent black mustard seeds used for tempering curries and pickles", "राई / सरसों", "noun", "f", "agriculture", "general", "राई रो तड़को दाल मांय खुशबू भर देवै।"),
    ("मूंज", "moonj", "Saccharum munja, wild desert reed woven into durable ropes and cot webbing", "मूंज (मजबूत घास)", "noun", "f", "nature", "general", "मूंज री रस्सी सूं खाट बुणी।"),
    ("कांस", "kaans", "tall wild perennial grass bearing feathery white plumes along riverbeds", "कांस घास", "noun", "m", "nature", "general", "बरसात बाद नदी किनारे कांस खिल उठ्यो।"),
    ("धूब", "dhoob", "Cynodon dactylon, sacred green lawn grass indispensable in Ganesha worship", "दूर्वा / दूब घास", "noun", "f", "rituals", "general", "गणेशजी नै हरी धूब चढ़ाई।"),
    ("धतूरो", "dhaturo", "Datura stramonium, thorny desert plant bearing white bell flowers sacred to Shiva", "धतूरा", "noun", "m", "rituals", "general", "महाशिवरात्रि माथे धतूरो अर्पित कर्यो।"),

    # Musical & Folk Song Genres
    ("नौबत", "naubat", "massive ceremonial kettledrum mounted on palace gateway arches to mark royal hours", "नौबत (राजद्वार का बड़ा वाद्य)", "noun", "f", "instruments", "general", "किला री पोल माथे नौबत बाजी।"),
    ("शहनाई", "shehnaai", "double-reed auspicious oboe played at royal ceremonies and wedding thresholds", "शहनाई", "noun", "f", "instruments", "general", "तोरण रे बखत शहनाई री मीठी धुन गूंजी।"),
    ("धमाल", "dhamaal", "exuberant celebratory spring folk song genre sung to Chang beats during Holi", "धमाल (होली का लोकगीत)", "noun", "f", "music", "general", "फागण मांय चंग री थाप माथे धमाल गाई।"),
    ("बधावा", "badhaawa", "auspicious celebratory welcome hymn sung by women at births and weddings", "बधावा गीत (मांगलिक बधाई गीत)", "noun", "m", "music", "general", "शुभ अवसर माथे महिलावां बधावा गाया।"),
    ("काजळियो", "kaajaliyo", "traditional wedding folk song sung when applying ceremonial kohl to groom's eyes", "काजलिया गीत", "noun", "m", "music", "general", "भाभी जी देवर नै काजळियो आंज्यो।"),
    ("हिंडोळो", "hindolo", "joyous monsoon swing song sung by women during Hariyali Teej", "हिंडोला (सावन का झूला गीत)", "noun", "m", "music", "general", "सावण मांय नीम री डाल माथे हिंडोळो घाल्यो।"),

    # Ceremonial & Social Exchange
    ("पाहुणो / पावणो", "paahuno / paawano", "honored guest, particularly newly wedded son-in-law visiting in-laws", "मेहमान / दामाद (पाहुणा)", "noun", "m", "culture", "general", "पाहुणा रे आगमन माथे घी-गुड़ री मनवार कीधी।"),
    ("न्योतो", "nyoto", "formal wedding or community banquet invitation", "न्यौता / निमंत्रण पत्र", "noun", "m", "culture", "general", "पूरे गांव नै जीमण रो न्योतो दियो।"),
    ("नेग", "neg", "traditional customary honorarium or token cash gift bestowed on relatives/artisans during rituals", "नेग (पारंपरिक दस्तूरी उपहार)", "noun", "m", "rituals", "general", "ब्याव मांय ननद अर भाभी नै नेग दियो।"),
    ("अक्षत", "akshat", "unbroken consecrated raw rice grains used in auspicious tilak and temple pujas", "अक्षत (पूजा के साबुत चावल)", "noun", "m", "rituals", "general", "माथे माथे रोली अर अक्षत रो टीको लगायो।"),
    ("कुंकुम / रोली", "kunkum / roli", "sacred bright vermilion powder applied on forehead and threshold", "रोली / कुमकुम", "noun", "f", "rituals", "general", "कुंकुम सूं देहरी माथे स्वास्तिक मांड्यो।"),
    ("आरती", "aarti", "ceremonial circular wafting of lighted camphor/ghee lamp accompanied by hymns", "आरती", "noun", "f", "rituals", "general", "मंदिर मांय संझा री आरती हुयी।"),
    ("हवन / होम", "hawan / hom", "sacred fire sacrifice offering oblations of ghee, barley, and herbs into agni", "हवन / होम", "noun", "m", "rituals", "general", "गृह-प्रवेश रे अवसर माथे हवन करवायो।"),
    ("मौली", "mauli", "sanctified red and yellow cotton thread tied around wrist as divine shield", "मौली / कलावा / रक्षा-सूत्र", "noun", "f", "rituals", "general", "पंडित जी हाथ मांय रक्षा-सूत्र मौली बांधी।"),
    ("धूप", "dhoop", "aromatic fragrant guggul and frankincense resin burnt on live desert embers", "धूप / सुगंधित लोबान", "noun", "f", "rituals", "general", "सवेरै घर मांय गूगल री धूप खेई।"),
    ("कपूर", "kapoor", "purifying white aromatic camphor crystals lit during deity aarti", "कपूर", "noun", "m", "rituals", "general", "कपूर री लौ सूं आरती कीधी।"),
]

added_count = 0
for item in BATCH_3:
    raj, rom, eng, hin, pos, g, cat, dial, ex = item
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

print(f"Batch 3 added {added_count} words! Total vocabulary now: {len(existing_words)}")
