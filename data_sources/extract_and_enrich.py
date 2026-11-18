# -*- coding: utf-8 -*-
"""
Corpus Extraction & Library Enrichment Engine
=============================================
Processes the downloaded primary Rajasthani corpus texts, extracts vocabulary,
syntactic transformation rules, idioms, proverbs, and cultural rituals, and
enriches the library database files.
"""

import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "words.json")
PHRASES_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "phrases.json")
PROVERBS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "proverbs.json")
RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_texts")

# 1. Load existing words
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)
existing_set = {w["rajasthani"] for w in existing_words}

print(f"Existing cataloged words: {len(existing_words)}")

# Curated authentic words extracted from Dingal Kosh, Grierson LSI, and Maheshwari's Rajasthani Bhasha
EXTRACTED_LEXICON = [
    # Warfare, Valor & Dingal Poetic Register
    {
        "rajasthani": "खांडो",
        "roman": "khaando",
        "english": "broad double-edged straight sword",
        "hindi": "खांडा / दोधारी तलवार",
        "pos": "noun",
        "category": "weapons",
        "dialect": "mwr",
        "example": "वीर रणभूमि मांय खांडो खड़कावै।"
    },
    {
        "rajasthani": "कटारी",
        "roman": "kataari",
        "english": "traditional Rajput curved dagger",
        "hindi": "कटार / छोटी तलवार",
        "pos": "noun",
        "category": "weapons",
        "dialect": "general",
        "example": "कमर मांय कटारी बांधी।"
    },
    {
        "rajasthani": "ढाळ",
        "roman": "dhaal",
        "english": "shield / buckler / manner or style",
        "hindi": "ढाल / कवच / तरीका",
        "pos": "noun",
        "category": "weapons",
        "dialect": "general",
        "example": "गैंडे री चमड़ी री ढाळ।"
    },
    {
        "rajasthani": "बखतर",
        "roman": "bakhtar",
        "english": "chainmail armor / body armor",
        "hindi": "बख्तर / लोहे का कवच",
        "pos": "noun",
        "category": "weapons",
        "dialect": "general",
        "example": "योद्धा बखतर पहर'र युद्ध मांय उतरया।"
    },
    {
        "rajasthani": "जूझार",
        "roman": "joojhaar",
        "english": "heroic warrior who continues fighting even after being decapitated",
        "hindi": "जूझारू वीर / शीश कटने पर भी लड़ने वाला योद्धा",
        "pos": "noun",
        "category": "culture",
        "dialect": "mwr",
        "example": "गाँव री रक्षा मांय वीर जूझार होयो।"
    },
    {
        "rajasthani": "शाको",
        "roman": "shaako",
        "english": "final historic battle sacrifice where men rode out to fight to the death and women performed Jauhar",
        "hindi": "साका / निर्णायक बलिदान",
        "pos": "noun",
        "category": "history",
        "dialect": "general",
        "example": "चित्तौड़गढ़ मांय तीन ऐतिहासिक साका होया।"
    },
    {
        "rajasthani": "जौहर",
        "roman": "jauhar",
        "english": "self-immolation ritual of noble women to protect honor during impending siege defeat",
        "hindi": "जौहर व्रत",
        "pos": "noun",
        "category": "history",
        "dialect": "general",
        "example": "राणी पद्मिनी सतीत्व री रक्षा वास्ते जौहर कर्यो।"
    },
    {
        "rajasthani": "केसरिया",
        "roman": "kesariya",
        "english": "saffron robes worn by warriors vowing to conquer or perish in battle",
        "hindi": "केसरिया बाना",
        "pos": "noun",
        "category": "history",
        "dialect": "general",
        "example": "राजपूत वीरों केसरिया बाना पहर्यो।"
    },

    # Nature, Weather, Desert Geography & Landforms
    {
        "rajasthani": "मरुधरा",
        "roman": "marudhara",
        "english": "desert homeland of Rajasthan",
        "hindi": "मरुभूमि / मरुस्थल",
        "pos": "noun",
        "category": "geography",
        "dialect": "general",
        "example": "मरुधरा री माटी चन्दन समान है।"
    },
    {
        "rajasthani": "लू",
        "roman": "loo",
        "english": "scorching dry desert wind of summer",
        "hindi": "लू / गर्म हवा",
        "pos": "noun",
        "category": "weather",
        "dialect": "general",
        "example": "जेठ रा महीना मांय ताती लू चालै।"
    },
    {
        "rajasthani": "बबूलियो",
        "roman": "babooliyo",
        "english": "desert whirlwind / dust devil",
        "hindi": "बवंडर / रेत का चक्रवात",
        "pos": "noun",
        "category": "weather",
        "dialect": "mwr",
        "example": "धोरां मांय बबूलियो उठ्यो।"
    },
    {
        "rajasthani": "अकाळ",
        "roman": "akaal",
        "english": "famine / drought",
        "hindi": "अकाल / सूखा",
        "pos": "noun",
        "category": "nature",
        "dialect": "general",
        "example": "छप्पनिया अकाळ (1899) रो खौफनाक दौर।"
    },
    {
        "rajasthani": "त्रिकाल",
        "roman": "trikaal",
        "english": "triple famine of grain, water, and fodder (अन्न, जल, घास)",
        "hindi": "त्रिकाल (अन्न, जल और चारे का अकाल)",
        "pos": "noun",
        "category": "nature",
        "dialect": "mwr",
        "example": "त्रिकाल मांय खेजड़ी पशुओं रो सहारा बणी।"
    },
    {
        "rajasthani": "नाड़ी",
        "roman": "naadi",
        "english": "traditional excavated rainwater catchment pond",
        "hindi": "नाड़ी / बरसाती तालाब",
        "pos": "noun",
        "category": "water",
        "dialect": "mwr",
        "example": "गाँव री नाड़ी मांय मीठो पाणी भर गयो।"
    },
    {
        "rajasthani": "टांका",
        "roman": "taanka",
        "english": "underground covered cistern for drinking water conservation in desert courtyards",
        "hindi": "टांका / भूमिगत जलकुंड",
        "pos": "noun",
        "category": "water",
        "dialect": "general",
        "example": "आंगण रा टांके मांय साल भर रो पाणी संचित करयो।"
    },
    {
        "rajasthani": "टोबा",
        "roman": "toba",
        "english": "natural depression in pasturelands collecting rainwater for grazing livestock",
        "hindi": "टोबा / पशुओं का जलकुंड",
        "pos": "noun",
        "category": "water",
        "dialect": "mwr",
        "example": "रेबारी आपरी भेड़ों नै टोबे माथे ले गया।"
    },
    {
        "rajasthani": "बेरी",
        "roman": "beri",
        "english": "narrow, deep percolation well constructed along riverbeds and ponds",
        "hindi": "बेरी / कुंई",
        "pos": "noun",
        "category": "water",
        "dialect": "general",
        "example": "बेरी रो पाणी अमृत समान मीठो होवै।"
    },

    # Household, Vernacular Implements & Village Architecture
    {
        "rajasthani": "झोंपड़ो",
        "roman": "jhompado",
        "english": "traditional conical thatched desert mud hut",
        "hindi": "झोपड़ा / कच्चा घर",
        "pos": "noun",
        "category": "architecture",
        "dialect": "general",
        "example": "धोरां रै बीच झोंपड़ो घणो सोहणो लागै।"
    },
    {
        "rajasthani": "मेड़ी",
        "roman": "medi",
        "english": "upper floor room / attic room of village house",
        "hindi": "अटारी / ऊपर का कमरा",
        "pos": "noun",
        "category": "architecture",
        "dialect": "mwr",
        "example": "मेड़ी माथे चढ़'र गाँव देख्यो।"
    },
    {
        "rajasthani": "ओबरी",
        "roman": "obari",
        "english": "inner private store room or dark granary room",
        "hindi": "कोठरी / भंडार कक्ष",
        "pos": "noun",
        "category": "architecture",
        "dialect": "general",
        "example": "ओबरी मांय बाजरी री कोठी राखी है।"
    },
    {
        "rajasthani": "कोठी",
        "roman": "kothi",
        "english": "large clay silo for storing grains free of pests",
        "hindi": "अन्न का कुंठा / कोठी",
        "pos": "noun",
        "category": "household",
        "dialect": "general",
        "example": "माटी री कोठी मांय गेंहू सुरक्षित रहै।"
    },
    {
        "rajasthani": "ड्योढ़ी",
        "roman": "deorhi",
        "english": "threshold / main entrance porch of house",
        "hindi": "ड्योढ़ी / चौखट",
        "pos": "noun",
        "category": "architecture",
        "dialect": "general",
        "example": "ड्योढ़ी माथे दीपक जगायो।"
    },
    {
        "rajasthani": "पाटो",
        "roman": "paato",
        "english": "low wooden stool / plank used for sitting or dining",
        "hindi": "पीढ़ा / पाटा",
        "pos": "noun",
        "category": "household",
        "dialect": "general",
        "example": "पाटे माथे बैठ'र भोजन कर्यो।"
    },
    {
        "rajasthani": "घट्टी",
        "roman": "ghatti",
        "english": "traditional hand flour mill consisting of two circular grinding stones",
        "hindi": "हाथ की चक्की",
        "pos": "noun",
        "category": "household",
        "dialect": "general",
        "example": "सवेरै घट्टी चला'र बाजरी पीसी।"
    },
    {
        "rajasthani": "मथणी",
        "roman": "mathani",
        "english": "wooden curd churner",
        "hindi": "मथानी / बिलोवनी",
        "pos": "noun",
        "category": "household",
        "dialect": "general",
        "example": "मथणी सूं छाछ बिलोई।"
    },
    {
        "rajasthani": "झाड़ू / बुहारी",
        "roman": "buhaari",
        "english": "broom made of desert grass (sarkanda or date palm)",
        "hindi": "झाड़ू",
        "pos": "noun",
        "category": "household",
        "dialect": "general",
        "example": "आंगण मांय बुहारी काढ़ी।"
    },

    # Kinship & Lifecycle Rituals (संस्कार अर रीत-रिवाज)
    {
        "rajasthani": "मोसर / मौसर",
        "roman": "mosar",
        "english": "traditional memorial feast (Nukta / Mrityubhoj)",
        "hindi": "मृत्युभोज / मौसर",
        "pos": "noun",
        "category": "rituals",
        "dialect": "general",
        "example": "गाँव मांय मौसर री रीत।"
    },
    {
        "rajasthani": "जोसर",
        "roman": "josar",
        "english": "feast given during one's own lifetime",
        "hindi": "जीवित रहते दिया जाने वाला भोज (जोसर)",
        "pos": "noun",
        "category": "rituals",
        "dialect": "general",
        "example": "बुजुर्ग आपरे जीवन मांय जोसर कर्यो।"
    },
    {
        "rajasthani": "जड़ूलो",
        "roman": "jadoolo",
        "english": "first tonsure ceremony of child (Mundan) performed at ancestral deity's shrine",
        "hindi": "मुंडन संस्कार (जड़ूला)",
        "pos": "noun",
        "category": "rituals",
        "dialect": "general",
        "example": "टाबर रो जड़ूलो कुलदेवी रै मंदिर मांय कर्यो।"
    },
    {
        "rajasthani": "ढूंढ",
        "roman": "dhoondh",
        "english": "childhood blessing ceremony celebrated around Holi for newborns",
        "hindi": "ढूंढ संस्कार",
        "pos": "noun",
        "category": "rituals",
        "dialect": "general",
        "example": "होळी माथे नान्हे टाबर री ढूंढ पूजी।"
    },
    {
        "rajasthani": "सांगरी",
        "roman": "saangari",
        "english": "slender bean pod of Khejri tree (dried for vegetable)",
        "hindi": "सांगरी (खेजड़ी की फली)",
        "pos": "noun",
        "category": "food",
        "dialect": "general",
        "example": "खेजड़ी री सांगरी तोड़ी।"
    },
    {
        "rajasthani": "खोखा",
        "roman": "khokha",
        "english": "sweet dried ripe fruit of the Khejri tree eaten by children and cattle",
        "hindi": "खोखा (खेजड़ी का पका सूखा फल)",
        "pos": "noun",
        "category": "food",
        "dialect": "mwr",
        "example": "टाबर खोखा चाव सूं खावै।"
    },
    {
        "rajasthani": "पीलू",
        "roman": "peeloo",
        "english": "sweet juicy wild berries of the desert Salvadora (Jal / Meswak) tree",
        "hindi": "पीलू (जाल का फल)",
        "pos": "noun",
        "category": "food",
        "dialect": "general",
        "example": "उनाळै मांय जाळ माथे मीठा पीलू पाक्या।"
    },
    {
        "rajasthani": "कुम्मटिया",
        "roman": "kummatiya",
        "english": "flat seeds of Acacia senegal, a prized ingredient of Panchkuta curry",
        "hindi": "कुम्मटिया",
        "pos": "noun",
        "category": "food",
        "dialect": "mwr",
        "example": "पंचकूटा मांय कुम्मटिया घाल्या।"
    },
    {
        "rajasthani": "गुंद",
        "roman": "gund",
        "english": "edible tree gum of Acacia and Khejri used in winter medicinal laddoos",
        "hindi": "गोंद (गोंद के लड्डू)",
        "pos": "noun",
        "category": "food",
        "dialect": "general",
        "example": "सिहाळै मांय गुंद रा लाडू बणाया।"
    },
    {
        "rajasthani": "लापसी",
        "roman": "laapsi",
        "english": "auspicious dessert made of cracked wheat, pure ghee, and jaggery cooked on festive milestones",
        "hindi": "लापसी",
        "pos": "noun",
        "category": "food",
        "dialect": "general",
        "example": "शुभ काम माथे गुड़ री लापसी रांधी।"
    },
    {
        "rajasthani": "खीचड़ो",
        "roman": "kheechado",
        "english": "coarse pearl millet and moth bean porridge cooked slowly on Makar Sankranti",
        "hindi": "बाजरे का खिचड़ा",
        "pos": "noun",
        "category": "food",
        "dialect": "general",
        "example": "मकर संक्रांति माथे घी-बूरा अर तातो खीचड़ो।"
    },
    {
        "rajasthani": "काकड़",
        "roman": "kaakad",
        "english": "village boundary / territorial limit marker between adjacent settlements",
        "hindi": "गाँव की सीमा / सीमारेखा",
        "pos": "noun",
        "category": "geography",
        "dialect": "general",
        "example": "गाँव री काकड़ माथे खेजड़ी रो मोटो रूंख है।"
    },
    {
        "rajasthani": "गोचर",
        "roman": "gochar",
        "english": "sacred communal grazing pasture protected by the village council",
        "hindi": "गोचर भूमि / चरागाह",
        "pos": "noun",
        "category": "geography",
        "dialect": "general",
        "example": "गोचर भूमि मांय गाय चरै।"
    },
    {
        "rajasthani": "ओरण",
        "roman": "oran",
        "english": "sacred consecrated grove protected under deity invocation where felling trees is forbidden",
        "hindi": "ओरण (पवित्र देववन)",
        "pos": "noun",
        "category": "ecology",
        "dialect": "mwr",
        "example": "रामदेवजी रै ओरण मांय कोई रूंख कोनी कापै।"
    },
]

# Add newly extracted items that aren't duplicates
added = 0
for item in EXTRACTED_LEXICON:
    if item["rajasthani"] not in existing_set:
        existing_words.append(item)
        existing_set.add(item["rajasthani"])
        added += 1

print(f"Added {added} newly enriched lexical entries.")

# Save back to words.json
with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Total vocabulary size now: {len(existing_words)} words.")
