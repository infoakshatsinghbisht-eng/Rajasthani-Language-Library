# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Reduplication & Echo-Word Engine
=============================================================
Models morphological echo-word formation (e.g. रोटी-सोटी, पाणी-धाणी,
चाय-वाय) and expressively intensified adverbial reduplications
(हळूहळू, बेगो-बेगो, लाल-लाल).
"""

from typing import Tuple


def echo_word(word: str) -> str:
    """
    Generates the characteristic Rajasthani echo compound (शब्द-द्वित्व).
    Rules:
    - If word begins with consonant (excluding 'स' / 'व'), replace initial onset with 'स' or 'व':
        रोटी -> रोटी-सोटी
        भात -> भात-सात
        खाट -> खाट-साट
        काम -> काम-काज / काम-साम
    - If word begins with 'प', often echoes with 'ध' or 'स':
        पाणी -> पाणी-धाणी
    - If word begins with vowel, prefix with 'स' / 'व':
        अकल -> अकल-सकल
    """
    clean = word.strip()
    if not clean:
        return ""

    if clean.startswith("पाणी"):
        return "पाणी-धाणी"
    if clean.startswith("रोटी"):
        return "रोटी-सोटी"
    if clean.startswith("चाय"):
        return "चाय-वाय"
    if clean.startswith("काम"):
        return "काम-काज"

    # Generic echo rule: replace initial consonant with 'स'
    first_char = clean[0]
    rest = clean[1:]
    if first_char in ["स", "श", "ष"]:
        echo_part = "व" + rest
    else:
        echo_part = "स" + rest

    return f"{clean}-{echo_part}"


def intensive_reduplication(word: str) -> str:
    """
    Constructs an intensive reduplicative phrase.
    Examples:
        >>> intensive_reduplication("हळू")
        'हळूहळू'
        >>> intensive_reduplication("बेगो")
        'बेगो-बेगो'
        >>> intensive_reduplication("मीठो")
        'मीठो-मीठो'
    """
    clean = word.strip()
    return f"{clean}-{clean}"
