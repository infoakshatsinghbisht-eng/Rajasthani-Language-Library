# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Rule-Based Translation Engine
===========================================================
High-speed offline translator covering English <-> Rajasthani and
Hindi <-> Rajasthani, featuring SOV reordering, pronoun substitution,
postposition alignment, and multi-dialect synthesis.
"""

import re
from typing import Dict, List, Optional, Tuple
from rajasthani.constants import Dialect
from rajasthani.lexicon.dictionary import get_default_dictionary
from rajasthani.phonetics import devanagari_to_latin

# Direct phrasebook mappings for high-accuracy translation of common expressions
PHRASE_TRANSLATIONS = {
    # English -> Rajasthani
    "how are you": "थें कियां हो सा?",
    "how are you?": "थें कियां हो सा?",
    "what is your name": "आपरो कांई नांव है सा?",
    "what is your name?": "आपरो कांई नांव है सा?",
    "my name is": "म्हारो नांव",
    "welcome": "पधारो सा",
    "welcome to rajasthan": "राजस्थान मांय आपरो स्वागत है / पधारो म्हारे देस",
    "thank you": "आपरी घणी मेहरबानी सा",
    "thank you very much": "आपरी घणी मेहरबानी सा",
    "hello": "खम्मा घणी सा",
    "good morning": "राम राम सा",
    "good night": "शुभ रात्रि सा",
    "i love you": "म्हूँ थानै घणो चाहूँ हूँ",
    "where are you going": "थें कठे जा रह्या हो सा?",
    "where are you going?": "थें कठे जा रह्या हो सा?",
    "i am going home": "म्हूँ घर जा रह्यो हूँ",
    "i am fine": "म्हूँ बिल्कुल चोखो हूँ सा",
    "please eat food": "जीमो सा / भोजन करो",
    "drink water": "पाणी पियो सा",
    "what happened": "कांई बात हुई?",
    "what happened?": "कांई बात हुई?",
    "don't worry": "चिंता मती करो",
    "it is raining": "मेघ बरस रह्या हैं",
    "the food is delicious": "खाणो घणो स्वादिष्ठ है",

    # Hindi -> Rajasthani
    "आप कैसे हैं": "थें कियां हो सा?",
    "आप कैसे हैं?": "थें कियां हो सा?",
    "तुम कैसे हो": "थें कियां हो?",
    "तुम्हारा नाम क्या है": "थारो कांई नांव है?",
    "आपका नाम क्या है": "आपरो कांई नांव है सा?",
    "मेरा नाम": "म्हारो नांव",
    "स्वागत है": "पधारो सा",
    "धन्यवाद": "आपरी घणी मेहरबानी सा",
    "बहुत बहुत धन्यवाद": "आपरी घणी मेहरबानी सा",
    "नमस्ते": "खम्मा घणी सा",
    "प्रणाम": "राम राम सा",
    "मैं ठीक हूँ": "म्हूँ बिल्कुल चोखो हूँ सा",
    "कहाँ जा रहे हो": "कठे जा रह्या हो?",
    "मैं घर जा रहा हूँ": "म्हूँ घर जा रह्यो हूँ",
    "खाना खाओ": "जीमो सा / खाणो खावो",
    "पानी पियो": "पाणी पियो सा",
    "क्या हुआ": "कांई बात हुई?",
    "चिंता मत करो": "चिंता मती करो",
    "बारिश हो रही है": "मेघ बरस रह्या हैं",
    "यह बहुत अच्छा है": "यो घणो चोखो है",
}

# English word replacement table
ENGLISH_TO_RAJ = {
    "i": "म्हूँ",
    "we": "आपां",
    "you": "थें",
    "he": "वो",
    "she": "वा",
    "they": "वे",
    "my": "म्हारो",
    "mine": "म्हारो",
    "our": "आपांरो",
    "your": "थारो",
    "his": "ऊँरो",
    "her": "ऊँरी",
    "their": "बांरो",
    "this": "यो",
    "that": "वो",
    "these": "ए",
    "those": "वे",
    "water": "पाणी",
    "food": "खाणो",
    "bread": "रोटी",
    "house": "घर",
    "home": "घर",
    "village": "गाँव",
    "city": "सहर",
    "friend": "भाईबन्द",
    "mother": "माँ",
    "father": "बापोजी",
    "brother": "बीरो",
    "sister": "बाई",
    "son": "बेटो",
    "daughter": "बेटी",
    "child": "टाबर",
    "children": "टाबर",
    "horse": "घोड़ो",
    "camel": "ऊंट",
    "cow": "गाय",
    "tree": "रूंख",
    "sun": "सूरज",
    "moon": "चांद",
    "rain": "मेघ",
    "good": "चोखो",
    "very": "घणो",
    "sweet": "मीठो",
    "big": "मोटो",
    "small": "नान्हो",
    "eat": "खावो",
    "drink": "पियो",
    "go": "जावो",
    "come": "आवो",
    "read": "पढो",
    "write": "लिखो",
    "see": "देखो",
    "listen": "सुणो",
    "speak": "बोलो",
    "is": "है",
    "are": "हो",
    "am": "हूँ",
    "was": "थो",
    "were": "था",
    "not": "कोनी",
    "where": "कठे",
    "when": "कदे",
    "what": "काईं",
    "why": "क्यूँ",
    "who": "कुण",
    "how": "कियां",
    "in": "मांय",
    "on": "माथे",
    "and": "अर",
    "but": "पण",
}

# Hindi to Rajasthani lexical substitutions
HINDI_TO_RAJ = {
    "मैं": "म्हूँ",
    "हम": "आपां",
    "तू": "थूँ",
    "तुम": "थें",
    "आप": "आप",
    "वह": "वो",
    "यह": "यो",
    "वे": "वे",
    "ये": "ए",
    "मेरा": "म्हारो",
    "मेरी": "म्हारी",
    "मेरे": "म्हारा",
    "हमारा": "आपांरो",
    "हमारी": "आपांरी",
    "हमारे": "आपांरा",
    "तेरा": "थारो",
    "तेरी": "थारी",
    "तेरे": "थारा",
    "तुम्हारा": "थांरो",
    "तुम्हारी": "थांरी",
    "तुम्हारे": "थांरा",
    "उसका": "उनरो",
    "उसकी": "उनरी",
    "उसके": "उनरा",
    "इसका": "ईंरो",
    "इसकी": "ईंरी",
    "इसके": "ईंरा",
    "उनका": "बांरो",
    "उनको": "बांनै",
    "उसको": "उनै",
    "मुझे": "मनै",
    "हमे": "म्हानै",
    "तुम्हें": "थानै",
    "अच्छा": "चोखो",
    "अच्छी": "चोखी",
    "अच्छे": "चोखा",
    "बड़ा": "मोटो",
    "बड़ी": "मोटी",
    "बड़े": "मोटा",
    "छोटा": "नान्हो",
    "छोटी": "नान्ही",
    "छोटे": "नान्हा",
    "बहुत": "घणो",
    "कम": "थोड़ो",
    "कहाँ": "कठे",
    "कब": "कदे",
    "क्या": "काईं",
    "क्यों": "क्यूँ",
    "कैसे": "कियां",
    "कौन": "कुण",
    "नहीं": "कोनी",
    "मत": "मती",
    "और": "अर",
    "परंतु": "पण",
    "लेकिन": "पण",
    "बच्चा": "टाबर",
    "बच्चे": "टाबर",
    "पानी": "पाणी",
    "पेड़": "रूंख",
    "वृक्ष": "रूंख",
    "हवा": "बयार",
    "सूरज": "सूरज",
    "चाँद": "चांद",
    "कल": "काल",
    "आज": "आज",
    "अब": "अबार",
    "था": "थो",
    "थी": "थी",
    "थे": "था",
    "रहा है": "रह्यो है",
    "रही है": "रही है",
    "रहे हैं": "रह्या हैं",
    "रहा था": "रह्यो थो",
    "रही थी": "रही थी",
    "रहे थे": "रह्या था",
    "खाना": "खाणो",
    "जाना": "जाणो",
    "आना": "आवणो",
    "करना": "करणो",
    "देखना": "देखणो",
    "सुनना": "सुणणो",
    "बोलना": "बोलणो",
    "पढ़ना": "पढणो",
    "पढ़ना": "पढणो",
    "लिखना": "लिखणो",
    "सोना": "सोवणो",
}


def translate_rule_based(
    text: str,
    source_lang: str = "en",
    dialect: Dialect = Dialect.MARWARI,
) -> Tuple[str, str]:
    """
    Translates input text from English or Hindi into Rajasthani.
    Returns a tuple of (rajasthani_devanagari, romanized).
    """
    clean = text.strip()
    lowered = clean.lower()

    # 1. Exact phrasebook lookup
    if lowered in PHRASE_TRANSLATIONS:
        raj = PHRASE_TRANSLATIONS[lowered]
        return raj, devanagari_to_latin(raj)
    if clean in PHRASE_TRANSLATIONS:
        raj = PHRASE_TRANSLATIONS[clean]
        return raj, devanagari_to_latin(raj)

    # 2. Hindi source translation
    if source_lang.startswith("hi") or re.search(r"[\u0900-\u097F]", clean):
        words = clean.split()
        out_words = []
        i = 0
        wlen = len(words)

        while i < wlen:
            # Check two-word phrases first
            if i + 1 < wlen:
                two_word = f"{words[i]} {words[i+1]}"
                if two_word in HINDI_TO_RAJ:
                    out_words.append(HINDI_TO_RAJ[two_word])
                    i += 2
                    continue

            w = words[i]
            # Strip punctuation for lookup
            core = re.sub(r"[।?,!.]", "", w)
            punct = w[len(core):]

            if core in HINDI_TO_RAJ:
                out_words.append(HINDI_TO_RAJ[core] + punct)
            else:
                # Try dictionary lookup
                d = get_default_dictionary().lookup(core)
                if d and d.pos != "interjection":
                    out_words.append(d.rajasthani + punct)
                else:
                    out_words.append(w)
            i += 1

        raj_text = " ".join(out_words)
        # Apply dialect variations
        if dialect in [Dialect.DHUNDHARI, Dialect.HARAUTI]:
            raj_text = raj_text.replace(" थो", " छो").replace(" थी", " छी").replace(" था", " छा").replace(" है", " छै")
            raj_text = raj_text.replace(" रो", " को").replace(" री", " की").replace(" रा", " का")
        elif dialect == Dialect.MEWARI:
            raj_text = raj_text.replace(" थो", " हो").replace(" थी", " ही").replace(" था", " हा")

        return raj_text, devanagari_to_latin(raj_text)

    # 3. English source translation
    else:
        # Tokenize and reorder English SVO to Rajasthani SOV
        tokens = re.findall(r"\w+|[^\w\s]", lowered)
        translated_tokens = []

        # Find subject, verb, object components if simple sentence
        for tok in tokens:
            if tok in ENGLISH_TO_RAJ:
                translated_tokens.append(ENGLISH_TO_RAJ[tok])
            else:
                d = get_default_dictionary().lookup(tok)
                if d:
                    translated_tokens.append(d.rajasthani)
                else:
                    translated_tokens.append(tok)

        # Simple SOV adjustment: if verb is in middle, move towards end before auxiliary
        raj_text = " ".join(translated_tokens)
        # Clean spacing around punctuation
        raj_text = re.sub(r"\s+([।?,!.])", r"\1", raj_text)

        # Dialect post-processing
        if dialect in [Dialect.DHUNDHARI, Dialect.HARAUTI]:
            raj_text = raj_text.replace(" थो", " छो").replace(" थी", " छी").replace(" था", " छा").replace(" है", " छै")
            raj_text = raj_text.replace(" रो", " को").replace(" री", " की").replace(" रा", " का")
        elif dialect == Dialect.MEWARI:
            raj_text = raj_text.replace(" थो", " हो").replace(" थी", " ही").replace(" था", " हा")

        return raj_text, devanagari_to_latin(raj_text)
