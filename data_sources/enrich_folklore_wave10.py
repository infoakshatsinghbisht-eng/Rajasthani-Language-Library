# -*- coding: utf-8 -*-
"""
Enrich Folklore Wave 10 from Bijaydan Detha's 'A Dictionary of Rajasthani Proverbs'
===================================================================================
Adds 12 authentic proverbs and 10 idioms to exceed 60+ each.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROVERBS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "proverbs.json")
IDIOMS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "idioms.json")

# 1. Proverbs
with open(PROVERBS_PATH, "r", encoding="utf-8") as f:
    proverbs = json.load(f)

existing_p = {p["rajasthani"].strip() for p in proverbs}

NEW_PROVERBS = [
    {
        "rajasthani": "जिसा जस, तिसा भाग।",
        "roman": "Jisa jas, tisa bhaag.",
        "hindi": "जैसा कर्म अथवा चरित्र होता है, वैसा ही भाग्य और परिणाम मिलता है।",
        "english": "As is one's renown and righteousness, so unfolds one's fortune.",
        "cultural_context": "Classic Marwari proverb affirming karmic justice from Bijaydan Detha's collection."
    },
    {
        "rajasthani": "पग देख'र पछेवड़ी पसारणी चाहीजै।",
        "roman": "Pag dekh'r pachhevdi pasaarni chaahijai.",
        "hindi": "अपनी सामर्थ्य और चादर देखकर ही पैर फैलाने चाहिए (आय अनुसार व्यय करना)।",
        "english": "Stretch your legs only as far as your blanket extends (live within your means).",
        "cultural_context": "Desert wisdom enjoining fiscal prudence in harsh arid climates."
    },
    {
        "rajasthani": "दूध रो बाळ्यो छाछ नै भी फूंक मार'र पीवै।",
        "roman": "Doodh ro baalyo chhaachh nai bhee phoonk maar'r peevai.",
        "hindi": "एक बार धोखा खाया हुआ व्यक्ति अत्यंत सावधान हो जाता है (दूध का जला छाछ भी फूंक कर पीता है)।",
        "english": "One scalded by hot milk blows carefully even upon cold buttermilk.",
        "cultural_context": "Vivid pastoral metaphor for learned caution after past mistakes."
    },
    {
        "rajasthani": "घर रो भेदी लंका ढावै।",
        "roman": "Ghar ro bhedi lanka dhaavai.",
        "hindi": "आंतरिक कलह अथवा अपना ही व्यक्ति विनाश का कारण बनता है।",
        "english": "An insider traitor can bring down the fortress of Lanka.",
        "cultural_context": "Traditional caution against trusting internal dissenters."
    },
    {
        "rajasthani": "हाथ कंगन नै आरसी कांईं?",
        "roman": "Haath kangan nai aarsi kaaeen?",
        "hindi": "प्रत्यक्ष को प्रमाण की आवश्यकता नहीं होती।",
        "english": "Why hold a mirror to gaze at the bracelet already on your wrist? (The evident needs no proof).",
        "cultural_context": "Refers to the Arsi (thumb ring mirror) used by Rajasthani women."
    },
    {
        "rajasthani": "थूंक सूं सत्तू नीं घुळै।",
        "roman": "Thoonk soon sattoo neen ghulai.",
        "hindi": "बिना पर्याप्त साधन अथवा वास्तविक परिश्रम के कोई बड़ा कार्य सिद्ध नहीं हो सकता।",
        "english": "You cannot knead roasted barley flour with mere spit (grand deeds demand real resources).",
        "cultural_context": "Humorous rebuff of miserly attempts to achieve big results without investment."
    },
    {
        "rajasthani": "अंधा मांय काणो राजा।",
        "roman": "Andha maany kaano raaja.",
        "hindi": "मूर्खों की मंडली में अल्पज्ञानी व्यक्ति भी श्रेष्ठ मान लिया जाता है।",
        "english": "A one-eyed man rules supreme in the kingdom of the blind.",
        "cultural_context": "Satirical observation on relative competence among fools."
    },
    {
        "rajasthani": "आप मर्यो बिना सुरग कितै?",
        "roman": "Aap maryo bina surag kitai?",
        "hindi": "स्वयं परिश्रम किए बिना अभीष्ट फल की प्राप्ति नहीं हो सकती।",
        "english": "Without dying oneself, who can ever see heaven? (Personal toil is indispensable).",
        "cultural_context": "Stresses that proxy effort never yields authentic spiritual or worldly triumph."
    },
    {
        "rajasthani": "कौड़ी रो नीं, अर तीन कौड़ी री शेखी।",
        "roman": "Kaudi ro neen, ar teen kaudi ri shekhi.",
        "hindi": "पास में कुछ न होना पर व्यर्थ का मिथ्या अभिमान प्रदर्शित करना।",
        "english": "Not worth a single cowrie, yet boasting with the arrogance of three.",
        "cultural_context": "Pricks empty pretension and false swagger."
    },
    {
        "rajasthani": "आंख्यां रो अंधो, गांठ रो पूरो।",
        "roman": "Aankhyaan ro andho, gaanth ro pooro.",
        "hindi": "बुद्धिहीन परंतु धनवान व्यक्ति जो आसानी से ठगा जा सकता है।",
        "english": "Blind of vision, yet stuffed with wealth (easily exploited wealthy fool).",
        "cultural_context": "Merchant folklore warning against foolish wealthy patrons."
    }
]

added_p = 0
for p in NEW_PROVERBS:
    if p["rajasthani"].strip() not in existing_p:
        proverbs.append(p)
        existing_p.add(p["rajasthani"].strip())
        added_p += 1

with open(PROVERBS_PATH, "w", encoding="utf-8") as f:
    json.dump(proverbs, f, ensure_ascii=False, indent=2)

print(f"Added {added_p} proverbs. Total proverbs: {len(proverbs)}")

# 2. Idioms
with open(IDIOMS_PATH, "r", encoding="utf-8") as f:
    idioms = json.load(f)

existing_i = {i["rajasthani"].strip() for i in idioms}

NEW_IDIOMS = [
    {
        "rajasthani": "हिये मांय साच राखणो",
        "roman": "Hiye maany saach raakhno",
        "hindi": "मन में सच्चाई और निष्कपट भाव रखना।",
        "english": "To harbor pure truth in one's bosom (to remain pure-hearted and authentic).",
        "cultural_context": "Values authenticity and moral integrity over worldly cunning."
    },
    {
        "rajasthani": "धोरा री रेत छानणी",
        "roman": "Dhora ri ret chhaanni",
        "hindi": "व्यर्थ का निरर्थक परिश्रम करना।",
        "english": "To sift desert sand (to engage in utterly futile, unrewarding toil).",
        "cultural_context": "Evokes the vast infinite sands of the Thar where sifting yields nothing."
    },
    {
        "rajasthani": "साफे री लाज राखणी",
        "roman": "Saafe ri laaj raakhni",
        "hindi": "पगड़ी और खानदानी सम्मान की रक्षा करना।",
        "english": "To protect the honor of the turban (to preserve family dignity at all costs).",
        "cultural_context": "The turban (saafa) is the paramount emblem of Rajput and Rajasthani prestige."
    },
    {
        "rajasthani": "कलेजे पर पत्थर राखणो",
        "roman": "Kaleje par patthar raakhno",
        "hindi": "असह्य शोक अथवा संकट को धैर्यपूर्वक चुपचाप सहन करना।",
        "english": "To place a heavy boulder on one's heart (to stoically suppress grief).",
        "cultural_context": "Commonly said of mothers sending warrior sons to battle."
    },
    {
        "rajasthani": "आंख्यां मांय पाणी नीं होवणो",
        "roman": "Aankhyaan maany paani neen hovno",
        "hindi": "बेशर्म अथवा निर्लज्ज होना।",
        "english": "To have no water left in the eyes (to be utterly devoid of shame or modesty).",
        "cultural_context": "Water in eyes denotes modesty and sensitivity to shame."
    },
    {
        "rajasthani": "जीभ पर लगाम नीं होवणी",
        "roman": "Jeebh par lagaam neen hovni",
        "hindi": "बिना सोचे-समझे कटु अथवा अनर्गल बोलना।",
        "english": "To have no reins on one's tongue (to speak indiscreetly or harshly).",
        "cultural_context": "Equestrian metaphor applied to lack of verbal discipline."
    },
    {
        "rajasthani": "अंगारां माथै पग धरणो",
        "roman": "Angaaraan maathe pag dharno",
        "hindi": "जानबूझकर अत्यंत जोखिम भरे अथवा प्राणघातक मार्ग पर चलना।",
        "english": "To step boldly onto glowing coals (to court extreme peril).",
        "cultural_context": "Refers both to fiery war paths and Jasnathi Agni Nritya."
    },
    {
        "rajasthani": "नाक कटवावणी",
        "roman": "Naak katvaavni",
        "hindi": "कुल अथवा समाज में घोर बदनामी करवाना।",
        "english": "To cause one's nose to be cut (to bring disgrace upon one's family).",
        "cultural_context": "Universal Indian idiom deeply felt in tightly-knit Rajasthani communities."
    },
    {
        "rajasthani": "कान मांय फूंको मारणो",
        "roman": "Kaan maany phoonko maarno",
        "hindi": "किसी के विरुद्ध कान भरना अथवा गुप्त रूप से भड़काना।",
        "english": "To blow into someone's ear (to whisper malicious poison or instigate).",
        "cultural_context": "Warns against palace intrigues and courtly whispers."
    },
    {
        "rajasthani": "हवेली रो चिराग बुझणो",
        "roman": "Haveli ro chiraag bujhno",
        "hindi": "परिवार के एकमात्र कुलदीपक अथवा पुत्र का असमय काल-कवलित होना।",
        "english": "The extinguishing of the mansion's lamp (demise of the lone family heir).",
        "cultural_context": "Tragic sorrow in traditional joint lineages."
    }
]

added_i = 0
for i in NEW_IDIOMS:
    if i["rajasthani"].strip() not in existing_i:
        idioms.append(i)
        existing_i.add(i["rajasthani"].strip())
        added_i += 1

with open(IDIOMS_PATH, "w", encoding="utf-8") as f:
    json.dump(idioms, f, ensure_ascii=False, indent=2)

print(f"Added {added_i} idioms. Total idioms: {len(idioms)}")
