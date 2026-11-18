# -*- coding: utf-8 -*-
"""
Enrichment of Family, Kinship, Marriage & Friendship Lexicon
============================================================
"""

import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"] for w in words}

NEW_WORDS = [
    # --- Family & Kinship ---
    {
        "rajasthani": "कुटुंब",
        "roman": "kutumb",
        "english": "extended family / joint household / clan",
        "hindi": "परिवार / कुटुंब",
        "pos": "noun",
        "category": "family",
        "dialect": "general",
        "example": "सगळो कुटुंब ब्याव मांय भेळो होयो।"
    },
    {
        "rajasthani": "परवार",
        "roman": "parwaar",
        "english": "family / household",
        "hindi": "परिवार",
        "pos": "noun",
        "category": "family",
        "dialect": "general",
        "example": "म्हारो परवार जोधपुर मांय रहै है।"
    },
    {
        "rajasthani": "नाता-गोता",
        "roman": "naata-gota",
        "english": "kinship relations / relatives / kith and kin",
        "hindi": "रिश्ते-नाते / सगे-संबंधी",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "नाता-गोता मांय सब सूं प्रेम राखणो चाहीजै।"
    },
    {
        "rajasthani": "भाईबन्द",
        "roman": "bhaaiband",
        "english": "kinsmen / brethren / brotherhood",
        "hindi": "भाई-बंधु / स्वजन",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "मुसीबत मांय भाईबन्द ही काम आवै।"
    },
    {
        "rajasthani": "परदादो",
        "roman": "pardaado",
        "english": "paternal great-grandfather",
        "hindi": "परदादा",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "परदादोजी री हवेली घणी पुरानी है।"
    },
    {
        "rajasthani": "परदादी",
        "roman": "pardaadi",
        "english": "paternal great-grandmother",
        "hindi": "परदादी",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "परदादीजी अमृतवाणी सुणावती।"
    },
    {
        "rajasthani": "भत्रीजो",
        "roman": "bhatreejo",
        "english": "brother's son (nephew)",
        "hindi": "भतीजा",
        "pos": "noun",
        "category": "kinship",
        "dialect": "mwr",
        "example": "भत्रीजो परीक्षा मांय अव्वल आयो।"
    },
    {
        "rajasthani": "भत्रीजी",
        "roman": "bhatreeji",
        "english": "brother's daughter (niece)",
        "hindi": "भतीजी",
        "pos": "noun",
        "category": "kinship",
        "dialect": "mwr",
        "example": "भत्रीजी नै सुंदर खिलौणो दियो।"
    },
    {
        "rajasthani": "भाणजो",
        "roman": "bhaanjo",
        "english": "sister's son (maternal nephew)",
        "hindi": "भांजा",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "मामो भाणजे नै घणो प्यार करै।"
    },
    {
        "rajasthani": "भाणजी",
        "roman": "bhaanji",
        "english": "sister's daughter (maternal niece)",
        "hindi": "भांजी",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "भाणजी ब्याव मांय आई।"
    },
    {
        "rajasthani": "चचेरो भाई",
        "roman": "chachero bhai",
        "english": "paternal uncle's son (cousin brother)",
        "hindi": "चचेरा भाई",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "म्हारो चचेरो भाई जयपुर पढ़ै है।"
    },
    {
        "rajasthani": "ममेरो भाई",
        "roman": "mamero bhai",
        "english": "maternal uncle's son (cousin brother)",
        "hindi": "ममेरा भाई",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "ममेरो भाई भात मांय आयो।"
    },
    {
        "rajasthani": "पोतो",
        "roman": "poto",
        "english": "son's son (paternal grandson)",
        "hindi": "पोता",
        "pos": "noun",
        "category": "kinship",
        "dialect": "mwr",
        "example": "दादोजी पोते नै अंगुली पकड़'र घुमावै।"
    },
    {
        "rajasthani": "पोती",
        "roman": "poti",
        "english": "son's daughter (paternal granddaughter)",
        "hindi": "पोती",
        "pos": "noun",
        "category": "kinship",
        "dialect": "mwr",
        "example": "पोती दादीजी सूं कहानी सुणै।"
    },
    {
        "rajasthani": "दोहितो",
        "roman": "dohito",
        "english": "daughter's son (maternal grandson)",
        "hindi": "दोहिता / नाती",
        "pos": "noun",
        "category": "kinship",
        "dialect": "mwr",
        "example": "नानाजी दोहिते नै लाड लडावै।"
    },
    {
        "rajasthani": "दोहिती",
        "roman": "dohiti",
        "english": "daughter's daughter (maternal granddaughter)",
        "hindi": "दोहिती / नातिन",
        "pos": "noun",
        "category": "kinship",
        "dialect": "mwr",
        "example": "दोहिती ननिहाल आई।"
    },

    # --- Marriage & In-Laws ---
    {
        "rajasthani": "ब्याव",
        "roman": "byaav",
        "english": "marriage / wedding ceremony / matrimony",
        "hindi": "विवाह / शादी / ब्याह",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "गाँव मांय आज मोटो ब्याव है।"
    },
    {
        "rajasthani": "सगाई",
        "roman": "sagaai",
        "english": "betrothal / engagement ceremony",
        "hindi": "सगाई / मंगनी",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "बन्ना अर बन्नी री सगाई हुई।"
    },
    {
        "rajasthani": "सावा",
        "roman": "saawa",
        "english": "auspicious wedding date / astronomical muhurat",
        "hindi": "विवाह का शुभ मुहूर्त / सावा",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "अखा तीज रो अबूझ सावा होवै।"
    },
    {
        "rajasthani": "पीहर",
        "roman": "peehar",
        "english": "maternal / parental home of a married woman",
        "hindi": "मायका / पीहर",
        "pos": "noun",
        "category": "family",
        "dialect": "general",
        "example": "तीज माथे बींदणी पीहर आई।"
    },
    {
        "rajasthani": "सासरों",
        "roman": "saasron",
        "english": "in-laws' home / husband's ancestral home",
        "hindi": "ससुराल",
        "pos": "noun",
        "category": "family",
        "dialect": "general",
        "example": "बींदणी सासरै मांय सबका आदर कर्यो।"
    },
    {
        "rajasthani": "ननिहाल",
        "roman": "nanihaal",
        "english": "maternal grandparents' home / village",
        "hindi": "ननिहाल",
        "pos": "noun",
        "category": "family",
        "dialect": "general",
        "example": "उनाळै री छुट्टी मांय टाबर ननिहाल गया।"
    },
    {
        "rajasthani": "ससरो",
        "roman": "sasro",
        "english": "father-in-law",
        "hindi": "ससुर",
        "pos": "noun",
        "category": "marriage",
        "dialect": "mwr",
        "example": "ससरोजी सा पाहुणे रो स्वागत कर्यो।"
    },
    {
        "rajasthani": "सासू",
        "roman": "saasu",
        "english": "mother-in-law",
        "hindi": "सास",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "सासूजी बींदणी नै आशीष दियो।"
    },
    {
        "rajasthani": "जेठ",
        "roman": "jeth",
        "english": "husband's elder brother",
        "hindi": "जेठ",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "जेठजी सा घर रा मुखिया हैं।"
    },
    {
        "rajasthani": "जेठाणी",
        "roman": "jethaani",
        "english": "husband's elder brother's wife",
        "hindi": "जेठानी",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "जेठाणीसा रसोई सम्भाळै हैं।"
    },
    {
        "rajasthani": "देवर",
        "roman": "devar",
        "english": "husband's younger brother",
        "hindi": "देवर",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "देवर भाभी सूं हंसी-मजाक करै।"
    },
    {
        "rajasthani": "देवराणी",
        "roman": "devraani",
        "english": "husband's younger brother's wife",
        "hindi": "देवरानी",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "देवराणी-जेठाणी प्रेम सूं रहवै हैं।"
    },
    {
        "rajasthani": "नणद",
        "roman": "nanad",
        "english": "husband's sister",
        "hindi": "ननद",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "नणद बाई ब्याव मांय नेग लियो।"
    },
    {
        "rajasthani": "नणदोई",
        "roman": "nandoi",
        "english": "husband's sister's husband",
        "hindi": "नंदोई",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "नणदोई सा बारात मांय शामिल होया।"
    },
    {
        "rajasthani": "साढू",
        "roman": "saadhoo",
        "english": "wife's sister's husband (co-brother-in-law)",
        "hindi": "साढ़ू भाई",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "दो साढू भाई आपस मांय मिल्या।"
    },
    {
        "rajasthani": "सलहज",
        "roman": "salhaj",
        "english": "wife's brother's wife",
        "hindi": "सलहज / साले की पत्नी",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "सलहज ब्याव मांय गीत गायो।"
    },
    {
        "rajasthani": "मुकलावो",
        "roman": "muklaavo",
        "english": "consummation journey of newlywed bride to husband's home (Gauna)",
        "hindi": "गौना / मुकलावा",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "मुकलावे माथे बींदणी नै पीहर सूं विदा करी।"
    },
    {
        "rajasthani": "बारात",
        "roman": "baaraat",
        "english": "wedding procession of the bridegroom",
        "hindi": "बारात",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "बारात ढोल-नगाड़ों रै सागे आई।"
    },
    {
        "rajasthani": "बराती",
        "roman": "baraati",
        "english": "wedding procession attendee / guest",
        "hindi": "बाराती / जनेती",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "बरात्यां नै सामेला मांय जीमायो।"
    },
    {
        "rajasthani": "मांडवो",
        "roman": "maandavo",
        "english": "decorated wedding pavilion or canopy",
        "hindi": "विवाह मंडप",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "मांडवे मांय फेरा होया।"
    },
    {
        "rajasthani": "हथलेवो",
        "roman": "hathlevo",
        "english": "ritual joining of bride's and groom's palms during wedding",
        "hindi": "हथलेवा / पाणिग्रहण",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "पंडितजी हथलेवो जुड़वायो।"
    },
    {
        "rajasthani": "तोरण",
        "roman": "toran",
        "english": "wooden auspicious archway mounted at bridal entrance",
        "hindi": "तोरण",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "बींद घोड़ी माथे बैठ'र तोरण मार्यो।"
    },
    {
        "rajasthani": "कामण",
        "roman": "kaaman",
        "english": "protective auspicious wedding folk songs sung to shield groom from evil eye",
        "hindi": "कामण गीत",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "लुगायां बन्ना नै कामण गा'र बधावै।"
    },
    {
        "rajasthani": "दायजो",
        "roman": "daayjo",
        "english": "bridal gifts given by parents upon daughter's departure",
        "hindi": "दहेज / दायजा / स्त्रीधन",
        "pos": "noun",
        "category": "marriage",
        "dialect": "general",
        "example": "बेटी नै दायजे मांय शगुन रा गहणा दिया।"
    },

    # --- Friends & Social Relationships ---
    {
        "rajasthani": "भाईलो",
        "roman": "bhaailo",
        "english": "close friend / intimate pal / bosom buddy (male)",
        "hindi": "मित्र / जिगरी दोस्त / यार",
        "pos": "noun",
        "category": "friends",
        "dialect": "mwr",
        "example": "म्हारो भाईलो म्हारै सागे खेलतो थो।"
    },
    {
        "rajasthani": "सहेली",
        "roman": "saheli",
        "english": "female friend / confidante",
        "hindi": "सहेली / सखी",
        "pos": "noun",
        "category": "friends",
        "dialect": "general",
        "example": "सहेलियां तीज माथे झूला झूलै।"
    },
    {
        "rajasthani": "गोयण",
        "roman": "goyan",
        "english": "close female childhood companion or female confidante",
        "hindi": "सहेली / सखी (गोयण)",
        "pos": "noun",
        "category": "friends",
        "dialect": "mwr",
        "example": "बाई आपरी गोयण सूं मन री बात कही।"
    },
    {
        "rajasthani": "बेली",
        "roman": "beli",
        "english": "companion / partner / faithful friend",
        "hindi": "मित्र / साथी / हमसफ़र",
        "pos": "noun",
        "category": "friends",
        "dialect": "general",
        "example": "ईं संसार मांय साचो बेली भगवान है।"
    },
    {
        "rajasthani": "संगी",
        "roman": "sangi",
        "english": "companion / comrade / associate",
        "hindi": "संगी / साथी",
        "pos": "noun",
        "category": "friends",
        "dialect": "general",
        "example": "सुख-दुःख रो संगी।"
    },
    {
        "rajasthani": "पड़ोसी",
        "roman": "padosi",
        "english": "neighbor (male)",
        "hindi": "पड़ोसी",
        "pos": "noun",
        "category": "social",
        "dialect": "general",
        "example": "चोखो पड़ोसी भगवान री देन होवै।"
    },
    {
        "rajasthani": "पड़ोसन",
        "roman": "padosan",
        "english": "neighbor (female)",
        "hindi": "पड़ोसिन",
        "pos": "noun",
        "category": "social",
        "dialect": "general",
        "example": "पड़ोसन चूल्हे वास्ते आँच लेवण आई।"
    },
    {
        "rajasthani": "गौंंत्यार",
        "roman": "gauntyaar",
        "english": "fellow villager / person belonging to the same native village",
        "hindi": "गाँव का निवासी / सहग्रामवासी",
        "pos": "noun",
        "category": "social",
        "dialect": "general",
        "example": "परदेस मांय गौंंत्यार मिल्यो तो घणो हरख होयो।"
    },
    {
        "rajasthani": "सयाणो",
        "roman": "sayaano",
        "english": "village elder / wise mature person / arbitrator",
        "hindi": "सयाना / बुजुर्ग / समझदार व्यक्ति",
        "pos": "noun",
        "category": "social",
        "dialect": "general",
        "example": "गाँव रा सयाणा झगड़ो सुलझा दियो।"
    },
    {
        "rajasthani": "चौधरी",
        "roman": "chaudhary",
        "english": "village headman / community leader",
        "hindi": "मुखिया / चौधरी",
        "pos": "noun",
        "category": "social",
        "dialect": "general",
        "example": "चौधरी साहब पंचायत मांय न्याय कर्यो।"
    },
    {
        "rajasthani": "सागो",
        "roman": "saago",
        "english": "blood relation / genuine relative / close affine",
        "hindi": "सगा / संबंधी",
        "pos": "noun",
        "category": "kinship",
        "dialect": "general",
        "example": "ओ म्हारो सागो भाई है।"
    },
]

added = 0
for item in NEW_WORDS:
    if item["rajasthani"] not in existing:
        words.append(item)
        existing.add(item["rajasthani"])
        added += 1

print(f"Added {added} new words related to family, friends, and marriage.")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Total vocabulary size: {len(words)} entries.")
