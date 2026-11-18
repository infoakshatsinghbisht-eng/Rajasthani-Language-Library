# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Phonetics & Orthography
====================================================
Devanagari normalization, Latin transliteration (bidirectional),
syllable segmentation, script detection, and phonetic transformations
characteristic of Rajasthani (e.g. ळ retroflex lateral, murmured sonorants).
"""

import re
import unicodedata
from typing import List, Tuple, Optional
from rajasthani.constants import Script

# Unicode Devanagari range: \u0900 to \u097F
DEVANAGARI_RANGE = (0x0900, 0x097F)

# Vowel / Matra mappings
DEVANAGARI_VOWELS = {
    "अ": "a", "आ": "aa", "इ": "i", "ई": "ee", "उ": "u", "ऊ": "oo",
    "ऋ": "ri", "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au", "अं": "am", "अः": "ah",
}

DEVANAGARI_MATRAS = {
    "ा": "aa", "ि": "i", "ी": "ee", "ु": "u", "ू": "oo",
    "ृ": "ri", "े": "e", "ै": "ai", "ो": "o", "ौ": "au",
    "ं": "n", "ँ": "n", "ः": "h", "्": "",
}

# Consonant mapping
DEVANAGARI_CONSONANTS = {
    "क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ng",
    "च": "ch", "छ": "chh", "ज": "j", "झ": "jh", "ञ": "ny",
    "ट": "t", "ठ": "th", "ड": "d", "ढ": "dh", "ण": "n",
    "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n",
    "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m",
    "य": "y", "र": "r", "ल": "l", "व": "v",
    "श": "sh", "ष": "sh", "स": "s", "ह": "h",
    # Specific Rajasthani retroflex consonants
    "ळ": "l",   # Retroflex lateral flap, common in Rajasthani (काळा, मेळो)
    "ड़": "d", "ढ़": "dh", "फ़": "f", "ज़": "z", "ख़": "kh", "ग़": "gh",
}

# Inverted mappings for Latin -> Devanagari
LATIN_TO_DEV_CONSONANTS = [
    ("chh", "छ"), ("kh", "ख"), ("gh", "घ"), ("ch", "च"),
    ("jh", "झ"), ("th", "थ"), ("dh", "ध"), ("ph", "फ"),
    ("bh", "भ"), ("sh", "श"), ("ng", "ङ"), ("ny", "ञ"),
    ("k", "क"), ("g", "ग"), ("j", "ज"), ("t", "त"),
    ("d", "द"), ("n", "न"), ("p", "प"), ("b", "ब"),
    ("m", "म"), ("y", "य"), ("r", "र"), ("l", "ल"),
    ("v", "व"), ("w", "व"), ("s", "स"), ("h", "ह"),
    ("z", "ज़"), ("f", "फ़"),
]

LATIN_TO_DEV_MATRAS = [
    ("aau", "ौ"), ("aa", "ा"), ("ee", "ी"), ("oo", "ू"),
    ("ai", "ै"), ("au", "ौ"), ("e", "े"), ("o", "ो"),
    ("i", "ि"), ("u", "ु"), ("a", ""),
]

LATIN_TO_DEV_INITIAL_VOWELS = [
    ("aau", "औ"), ("aa", "आ"), ("ee", "ई"), ("oo", "ऊ"),
    ("ai", "ऐ"), ("au", "औ"), ("e", "ए"), ("o", "ओ"),
    ("i", "इ"), ("u", "उ"), ("a", "अ"),
]


def normalize_devanagari(text: str) -> str:
    """
    Normalizes Rajasthani Devanagari text:
    - Unicode NFC normalization
    - Strips unwanted zero-width spaces/joiners
    - Normalizes nuktas and candid anunasika/anusvara
    """
    if not text:
        return ""
    text = unicodedata.normalize("NFC", text)
    # Remove ZWJ / ZWNJ when stray
    text = text.replace("\u200c", "").replace("\u200b", "")
    # Normalize danda and double danda
    text = text.replace("।", "।").replace("॥", "॥")
    # Collapse multiple whitespace
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def detect_script(text: str) -> Script:
    """
    Detects whether text is in Devanagari or Latin script.
    """
    dev_count = 0
    lat_count = 0
    for char in text:
        cp = ord(char)
        if DEVANAGARI_RANGE[0] <= cp <= DEVANAGARI_RANGE[1]:
            dev_count += 1
        elif (65 <= cp <= 90) or (97 <= cp <= 122):
            lat_count += 1

    if dev_count >= lat_count and dev_count > 0:
        return Script.DEVANAGARI
    elif lat_count > 0:
        return Script.LATIN
    return Script.DEVANAGARI


def devanagari_to_latin(text: str) -> str:
    """
    Converts Rajasthani Devanagari text to readable, phonetic Latin romanization.
    Properly handles halant, implicit 'a', aspirated conjuncts, and retroflex ळ.
    """
    text = normalize_devanagari(text)
    output = []
    i = 0
    n = len(text)

    while i < n:
        c = text[i]

        # Check full vowels
        if c in DEVANAGARI_VOWELS:
            output.append(DEVANAGARI_VOWELS[c])
            i += 1
            continue

        # Check consonants
        if c in DEVANAGARI_CONSONANTS:
            base_lat = DEVANAGARI_CONSONANTS[c]
            # Check next character for matra or halant
            if i + 1 < n:
                nxt = text[i + 1]
                if nxt == "्":  # Halant: no implicit vowel
                    output.append(base_lat)
                    i += 2
                    continue
                elif nxt in DEVANAGARI_MATRAS:
                    output.append(base_lat + DEVANAGARI_MATRAS[nxt])
                    i += 2
                    continue
                else:
                    # Next is another consonant or space: implicit 'a'
                    # Word-final 'a' is suppressed in standard pronunciation if ending
                    if i + 1 == n or text[i + 1].isspace() or text[i + 1] in "।,.-!?":
                        # In Rajasthani, final 'o', 'a' are pronounced, but pure inherent 'a' at end is soft
                        output.append(base_lat)
                    else:
                        output.append(base_lat + "a")
                    i += 1
                    continue
            else:
                # Last character of word
                output.append(base_lat)
                i += 1
                continue

        # Check standalone matra or punctuation
        if c in DEVANAGARI_MATRAS:
            output.append(DEVANAGARI_MATRAS[c])
        else:
            output.append(c)
        i += 1

    result = "".join(output)
    # Clean up duplicate spaces or awkward double vowels
    result = re.sub(r"\s+", " ", result)
    return result.strip()


def latin_to_devanagari(text: str) -> str:
    """
    Converts Romanized Rajasthani text back to Devanagari.
    Handles common Rajasthani phrases like 'khamma ghani' -> 'खम्मा घणी'.
    """
    if not text:
        return ""

    # Known common phrase shortcuts
    phrase_map = {
        "khamma ghani": "खम्मा घणी",
        "ghani khamma": "घणी खम्मा",
        "ram ram sa": "राम राम सा",
        "padharo mhare des": "पधारो म्हारे देस",
        "mharo": "म्हारो",
        "mhari": "म्हारी",
        "mhara": "म्हारा",
        "tharo": "थारो",
        "thari": "थारी",
        "thara": "थारा",
        "hukum": "हुकुम",
        "banna": "बन्ना",
        "baisa": "बाईसा",
        "koni": "कोनी",
        "chhai": "छै",
        "kai": "काईं",
        "kothe": "कठे",
        "kade": "कदे",
    }
    lowered = text.strip().lower()
    if lowered in phrase_map:
        return phrase_map[lowered]

    # Token-by-token phonetic transliteration
    words = text.split()
    dev_words = []
    for word in words:
        clean = word.lower()
        if clean in phrase_map:
            dev_words.append(phrase_map[clean])
            continue

        res = []
        i = 0
        wlen = len(clean)
        is_start = True

        while i < wlen:
            matched = False
            # If word start, check initial vowels
            if is_start:
                for lat_v, dev_v in LATIN_TO_DEV_INITIAL_VOWELS:
                    if clean.startswith(lat_v, i):
                        res.append(dev_v)
                        i += len(lat_v)
                        is_start = False
                        matched = True
                        break
                if matched:
                    continue

            # Check consonants
            for lat_c, dev_c in LATIN_TO_DEV_CONSONANTS:
                if clean.startswith(lat_c, i):
                    res.append(dev_c)
                    i += len(lat_c)
                    is_start = False
                    matched = True

                    # Check trailing vowel matra
                    matra_matched = False
                    for lat_m, dev_m in LATIN_TO_DEV_MATRAS:
                        if clean.startswith(lat_m, i):
                            res.append(dev_m)
                            i += len(lat_m)
                            matra_matched = True
                            break
                    if not matra_matched and i < wlen and clean[i].isalpha():
                        # Consonant cluster -> add halant
                        res.append("्")
                    break

            if not matched:
                res.append(clean[i])
                i += 1
                is_start = False

        dev_words.append("".join(res))

    return " ".join(dev_words)


def tokenize(text: str) -> List[str]:
    """
    Tokenizes Rajasthani text into lexical tokens, separating
    punctuation while keeping compounds or clitics intact.
    """
    text = normalize_devanagari(text)
    # Match words (including devanagari letters, matras, halant, and hyphen) or punctuation
    tokens = re.findall(r"[\u0900-\u097F\w\-]+|[^\s\w]", text)
    return [t for t in tokens if t.strip()]


def syllables(word: str) -> List[str]:
    """
    Splits a Rajasthani Devanagari word into phonetic syllables.
    Example: 'राजस्थानी' -> ['रा', 'ज', 'स्था', 'नी']
    """
    word = normalize_devanagari(word)
    pattern = r"(?:[क-हळ](?:्[क-हळ])*(?:[ा-ौ]|ं|ँ|ः)?)|(?:[अ-औ](?:ं|ँ|ः)?)"
    matches = re.findall(pattern, word)
    return matches if matches else [word]
