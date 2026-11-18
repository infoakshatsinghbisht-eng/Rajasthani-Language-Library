# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip(): w for w in words}

more = [
    ("सोहणो", "sohano", "handsome, charming, aesthetically pleasant", "सुंदर अथवा मनोहर", "adjective", "masculine", "descriptors", "marwari", "यो महल घणो सोहणो बण्यो है।"),
    ("लाडलो", "laadlo", "cherished, deeply pampered child", "प्यारा अथवा दुलारा", "noun", "masculine", "family", "marwari", "माय रो लाडलो बेटा आंगणै खेलै।"),
    ("दुलारो", "dulaaro", "beloved, adored darling", "दुलारा अथवा प्रिय", "adjective", "masculine", "descriptors", "general", "दुलारो बालक किलकारी मारै।"),
    ("मनभावण", "manbhaavan", "alluring, delightful, pleasing to the heart", "मनभावन अथवा प्रिय", "adjective", "masculine", "descriptors", "general", "सावण रो महीनो घणो मनभावण लागै।"),
    ("रसीलो", "raseelo", "succulent, juicy, flavorful", "रसीला अथवा सरस", "adjective", "masculine", "descriptors", "general", "थार रो मतीरो घणो रसीलो होवै।"),
    ("चटकीलो", "chatkeelo", "vivid, strikingly vibrant in hue", "चमकीला अथवा चटख रंग का", "adjective", "masculine", "descriptors", "general", "साफे रो लाल रंग घणो चटकीलो है।"),
    ("हसमुख", "hasmukh", "cheerful, smiling, good-humoured", "हंसमुख अथवा प्रसन्नचित्त", "adjective", "masculine", "descriptors", "general", "हसमुख स्वभाव सूं सब राजी रह्वै।"),
    ("सलोनो", "salono", "graceful, beautifully fashioned", "सुंदर अथवा सलोना", "adjective", "masculine", "descriptors", "general", "सलोनो रूप देख सब मोहित होया।"),
    ("गुणी", "guni", "virtuous, talented master of arts", "गुणवान अथवा कला प्रवीण", "adjective", "masculine", "descriptors", "general", "गुणी पुरुष रो सब आदर करै।"),
    ("विद्वान", "vidvaan", "profound scholar learned in scriptures", "विद्वान अथवा पंडित", "noun", "masculine", "education", "general", "विद्वान पुरुष सभा मांय शास्त्रार्थ कर्यो।"),
    ("धीरो", "dheero", "unflurried, calm, composed", "धैर्यवान अथवा शांत", "adjective", "masculine", "descriptors", "marwari", "संकट मांय धीरो रहणो जरूरी है।"),
    ("गंभीरो", "gambheero", "stately, solemn and reflective", "गंभीर", "adjective", "masculine", "descriptors", "marwari", "राजाजी रो स्वभाव घणो गंभीरो थो।"),
    ("सरलो", "sarlo", "guileless, simple, straightforward", "सरल अथवा सीधा", "adjective", "masculine", "descriptors", "marwari", "सरलो मानख छल नीं समझै।"),
    ("साधुता", "saadhuta", "saintliness, moral integrity", "सज्जनता अथवा साधुता", "noun", "feminine", "values", "general", "साधुता ही मानख रो सांचो गहणो है।"),
    ("नेह", "neh", "warm unconditional tender affection", "स्नेह अथवा प्रेम", "noun", "masculine", "emotions", "marwari", "माय रो बालकां सूं सांचो नेह होवै।"),
    ("प्रीति", "preeti", "loving fellowship and goodwill", "प्रेम अथवा सद्भाव", "noun", "feminine", "emotions", "general", "आपसी प्रीति सूं संसार सुखमय बणै।"),
    ("लाड", "laad", "indulgent affection, tender pampering", "स्नेह अथवा दुलार", "noun", "masculine", "emotions", "general", "दादीजी पोते नै घणो लाड कर्यो।"),
    ("अनुराग", "anuraag", "devotional surrender, profound love", "भक्ति अथवा अनुराग", "noun", "masculine", "emotions", "general", "ईश्वर रै चरणां मांय अनुराग राख्यो।"),
    ("उमंगियो", "umangiyo", "thrilled with surging inner ecstasy", "उत्साहित अथवा उमंग से भरा", "adjective", "masculine", "emotions", "marwari", "जीत री खबर सुण सारो नगर उमंगियो।"),
    ("हियाव", "hiyaav", "inner courage of heart, daring resolve", "साहस अथवा कलेजा", "noun", "masculine", "values", "marwari", "मुश्किल समै मांय हियाव राख्यो।")
]

added = 0
for item in more:
    if item[0] not in existing:
        words.append({
            "rajasthani": item[0],
            "roman": item[1],
            "english": item[2],
            "hindi": item[3],
            "pos": item[4],
            "gender": item[5],
            "category": item[6],
            "dialect": item[7],
            "example": item[8]
        })
        existing[item[0]] = True
        added += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Added {added} words. Final total words: {len(words)}")
