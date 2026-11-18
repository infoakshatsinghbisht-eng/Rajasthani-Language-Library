# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Numbers & Numerals Converter
=========================================================
Converts numbers to Rajasthani words (0-100+), parses Rajasthani number words
to integers, handles Devanagari digits (०-९), ordinals, and cultural fractions.
"""

from typing import Dict, List, Optional

# Devanagari numerals map
DEV_DIGITS = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९"]
ARABIC_TO_DEV = {str(i): DEV_DIGITS[i] for i in range(10)}
DEV_TO_ARABIC = {DEV_DIGITS[i]: str(i) for i in range(10)}

# Rajasthani cardinal numbers (0-100)
RAJASTHANI_NUMBERS: Dict[int, str] = {
    0: "मींडो",
    1: "एक",
    2: "दो",
    3: "तीन",
    4: "चार",
    5: "पाँच",
    6: "छह",
    7: "सात",
    8: "आठ",
    9: "नौ",
    10: "दस",
    11: "ग्यारा",
    12: "बारा",
    13: "तेरा",
    14: "चौदा",
    15: "पंद्रा",
    16: "सोळा",
    17: "सत्रा",
    18: "अठारा",
    19: "उणीस",
    20: "बीस",
    21: "इक्कीस",
    22: "बाईस",
    23: "तेईस",
    24: "चौबीस",
    25: "पच्चीस",
    26: "छब्बीस",
    27: "सत्ताईस",
    28: "अट्ठाईस",
    29: "उणतीस",
    30: "तीस",
    31: "इकतीस",
    32: "बत्तीस",
    33: "तैंतीस",
    34: "चौंतीस",
    35: "पैंतीस",
    36: "छत्तीस",
    37: "सैंतीस",
    38: "अड़तीस",
    39: "उनचालीस",
    40: "चालीस",
    41: "इकतालीस",
    42: "बयालीस",
    43: "तैंतालीस",
    44: "चौंतालीस",
    45: "पैंतालीस",
    46: "छियालीस",
    47: "सैंतालीस",
    48: "अड़तालीस",
    49: "उनचास",
    50: "पचास",
    51: "इक्यावन",
    52: "बावन",
    53: "तिरपन",
    54: "चौवन",
    55: "पचपन",
    56: "छप्पन",
    57: "सत्तावन",
    58: "अट्ठावन",
    59: "उनसठ",
    60: "साठ",
    61: "इकसठ",
    62: "बासठ",
    63: "तिरसठ",
    64: "चौंसठ",
    65: "पैंसठ",
    66: "छियासठ",
    67: "सड़सठ",
    68: "अड़सठ",
    69: "उनहत्तर",
    70: "सत्तर",
    71: "इकहत्तर",
    72: "बहत्तर",
    73: "तिहत्तर",
    74: "चौहत्तर",
    75: "पचहत्तर",
    76: "छिहत्तर",
    77: "सतहत्तर",
    78: "अठहत्तर",
    79: "उनासी",
    80: "अस्सी",
    81: "इक्यासी",
    82: "बयासी",
    83: "तिरासी",
    84: "चौरासी",
    85: "पचासी",
    86: "छियासी",
    87: "सतासी",
    88: "अठासी",
    89: "नवासी",
    90: "नब्बे",
    91: "इक्यानवे",
    92: "बानवे",
    93: "तिरानवे",
    94: "चौरानवे",
    95: "पचानवे",
    96: "छियानवे",
    97: "सत्तानवे",
    98: "अट्ठानवे",
    99: "निन्यानवे",
    100: "सो",
}

# Reverse lookup for parsing
WORDS_TO_NUM: Dict[str, int] = {v: k for k, v in RAJASTHANI_NUMBERS.items()}
# Add common phonetic and dialectal variants
WORDS_TO_NUM.update({
    "शून्य": 0, "सुन्न": 0, "छै": 6, "ग्यारै": 11, "बारै": 12, "तेरै": 13,
    "चौदै": 14, "पंदरै": 15, "सोळै": 16, "सत्रै": 17, "अठारै": 18,
    "सैकड़ो": 100, "सौ": 100,
})

# Ordinals (क्रमसूचक संख्या)
ORDINALS_MASCULINE = {
    1: "पहलो",
    2: "दूजो",
    3: "तीजो",
    4: "चौथो",
    5: "पाँचवो",
    6: "छठ्ठो",
    7: "सातवो",
    8: "आठवो",
    9: "नौवो",
    10: "दसवां",
}

ORDINALS_FEMININE = {
    1: "पहली",
    2: "दूजी",
    3: "तीजी",
    4: "चौथी",
    5: "पाँचवी",
    6: "छठ्ठी",
    7: "सातवी",
    8: "आठवी",
    9: "नौवी",
    10: "दसवीं",
}

# Traditional fractions (भिन्न अर माप)
FRACTIONS = {
    "quarter": {"rajasthani": "पाव", "value": 0.25, "english": "one quarter (1/4)"},
    "half": {"rajasthani": "आधो", "value": 0.5, "english": "half (1/2)"},
    "three_quarters": {"rajasthani": "पौण", "value": 0.75, "english": "three quarters (3/4)"},
    "one_and_quarter": {"rajasthani": "सवा", "value": 1.25, "english": "one and a quarter (1 1/4)"},
    "one_and_half": {"rajasthani": "डेढ़", "value": 1.5, "english": "one and a half (1 1/2)"},
    "two_and_half": {"rajasthani": "अढाई", "value": 2.5, "english": "two and a half (2 1/2)"},
    "plus_half": {"rajasthani": "साढ़े", "value": 0.5, "english": "plus half (used from 3.5 onwards)"},
}


def num_to_words(n: int) -> str:
    """
    Converts an integer to Rajasthani words (supports 0 to 99,99,99,999).
    Example:
        >>> num_to_words(42)
        'बयालीस'
        >>> num_to_words(105)
        'एक सो पाँच'
    """
    if n < 0:
        return "माइनस " + num_to_words(-n)

    if n in RAJASTHANI_NUMBERS:
        return RAJASTHANI_NUMBERS[n]

    if n < 1000:
        hundreds = n // 100
        rem = n % 100
        h_str = f"{RAJASTHANI_NUMBERS[hundreds]} सो"
        if rem == 0:
            return h_str
        return f"{h_str} {num_to_words(rem)}"

    if n < 100000:
        thousands = n // 1000
        rem = n % 1000
        t_str = f"{num_to_words(thousands)} हजार"
        if rem == 0:
            return t_str
        return f"{t_str} {num_to_words(rem)}"

    if n < 10000000:
        lakhs = n // 100000
        rem = n % 100000
        l_str = f"{num_to_words(lakhs)} लाख"
        if rem == 0:
            return l_str
        return f"{l_str} {num_to_words(rem)}"

    crores = n // 10000000
    rem = n % 10000000
    c_str = f"{num_to_words(crores)} करोड़"
    if rem == 0:
        return c_str
    return f"{c_str} {num_to_words(rem)}"


def words_to_num(text: str) -> Optional[int]:
    """
    Parses a Rajasthani number word back to an integer.
    Example:
        >>> words_to_num('बयालीस')
        42
    """
    clean = text.strip()
    if clean in WORDS_TO_NUM:
        return WORDS_TO_NUM[clean]

    # Handle compounds like 'एक सो पाँच'
    parts = clean.split()
    total = 0
    current = 0

    for word in parts:
        if word in ["हजार"]:
            total += (current or 1) * 1000
            current = 0
        elif word in ["लाख"]:
            total += (current or 1) * 100000
            current = 0
        elif word in ["करोड़"]:
            total += (current or 1) * 10000000
            current = 0
        elif word in ["सो", "सौ", "सैकड़ो"]:
            current = (current or 1) * 100
        elif word in WORDS_TO_NUM:
            current += WORDS_TO_NUM[word]
        else:
            return None

    return total + current


def to_devanagari_numerals(n: int) -> str:
    """
    Converts integer or string of digits to Devanagari numerals (०-९).
    Example:
        >>> to_devanagari_numerals(2026)
        '२०२६'
    """
    s = str(n)
    return "".join(ARABIC_TO_DEV.get(c, c) for c in s)


def from_devanagari_numerals(dev_str: str) -> int:
    """
    Converts a string of Devanagari numerals (०-९) to an integer.
    Example:
        >>> from_devanagari_numerals('२०२६')
        2026
    """
    arabic_str = "".join(DEV_TO_ARABIC.get(c, c) for c in dev_str)
    return int(arabic_str)


def ordinal(n: int, gender: str = "m") -> str:
    """
    Returns ordinal string for number n.
    Example:
        >>> ordinal(1, 'm')
        'पहलो'
        >>> ordinal(2, 'f')
        'दूजी'
    """
    table = ORDINALS_FEMININE if gender.lower().startswith("f") else ORDINALS_MASCULINE
    if n in table:
        return table[n]
    base = num_to_words(n)
    return f"{base}वीं" if gender.lower().startswith("f") else f"{base}वां"


def fraction(key: str) -> Optional[Dict[str, any]]:
    """Retrieves Rajasthani fractional term data."""
    return FRACTIONS.get(key)
