# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Universal World Language Pivot Bridge
==================================================================
Bridges non-English/non-Hindi world languages (Spanish, French, German,
Russian, Japanese, Mandarin, Arabic, Bengali, Tamil, etc.) into Rajasthani
using semantic pivot mappings.
"""

from typing import Dict, Optional, Tuple
from rajasthani.translator.rule_based import translate_rule_based
from rajasthani.constants import Dialect

# World language common phrase pivot mappings -> English
WORLD_PIVOTS: Dict[str, str] = {
    # Spanish
    "hola": "hello",
    "buenos días": "good morning",
    "cómo estás": "how are you",
    "cómo estás?": "how are you?",
    "gracias": "thank you",
    "muchas gracias": "thank you very much",
    "de nada": "welcome",
    "te amo": "i love you",
    "adiós": "goodbye",
    "dónde vas": "where are you going",
    "agua": "water",
    "comida": "food",

    # French
    "bonjour": "hello",
    "comment allez-vous": "how are you",
    "comment vas-tu": "how are you",
    "merci": "thank you",
    "merci beaucoup": "thank you very much",
    "je t'aime": "i love you",
    "eau": "water",
    "pain": "bread",

    # German
    "hallo": "hello",
    "guten morgen": "good morning",
    "wie geht es dir": "how are you",
    "danke": "thank you",
    "danke schön": "thank you very much",
    "ich liebe dich": "i love you",
    "wasser": "water",
    "brot": "bread",

    # Russian
    "здравствуйте": "hello",
    "привет": "hello",
    "как дела": "how are you",
    "спасибо": "thank you",
    "большое спасибо": "thank you very much",
    "я люблю тебя": "i love you",
    "вода": "water",

    # Japanese
    "こんにちは": "hello",
    "おはようございます": "good morning",
    "ありがとう": "thank you",
    "ありがとうございます": "thank you very much",
    "お元気ですか": "how are you",
    "愛してる": "i love you",
    "水": "water",

    # Mandarin
    "你好": "hello",
    "早上好": "good morning",
    "谢谢": "thank you",
    "非常感谢": "thank you very much",
    "你好吗": "how are you",
    "我爱你": "i love you",
    "水": "water",

    # Arabic
    "مرحبا": "hello",
    "السلام عليكم": "hello",
    "كيف حالك": "how are you",
    "شكرا": "thank you",
    "شكرا جزيلا": "thank you very much",
    "أحبك": "i love you",
    "ماء": "water",

    # Bengali
    "নমস্কার": "hello",
    "কেমন আছেন": "how are you",
    "ধন্যবাদ": "thank you",
    "জল": "water",
    "আমি তোমাকে ভালোবাসি": "i love you",

    # Tamil
    "வணக்கம்": "hello",
    "எப்படி இருக்கிறீர்கள்": "how are you",
    "நன்றி": "thank you",
    "தண்ணீர்": "water",
}


def pivot_translate(text: str, dialect: Dialect = Dialect.MARWARI) -> Optional[Tuple[str, str]]:
    """
    Attempts to translate a world language phrase by pivoting through English.
    """
    clean = text.strip().lower()
    if clean in WORLD_PIVOTS:
        en_pivot = WORLD_PIVOTS[clean]
        return translate_rule_based(en_pivot, source_lang="en", dialect=dialect)
    return None
