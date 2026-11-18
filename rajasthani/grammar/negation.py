# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Negation & Prohibitive Modality
============================================================
Handles negative copula, verbal negation (कोनी, नी, ना),
prohibitive imperative (मती - e.g. 'मती जा!'), and dialectal variants (कोन्या).
"""

from typing import Optional
from rajasthani.constants import Dialect


def negate_sentence(sentence: str, dialect: Dialect = Dialect.MARWARI) -> str:
    """
    Applies standard Rajasthani verbal negation.
    In Marwari, 'कोनी' or 'नी' is inserted before the finite verb or auxiliary.
    """
    words = sentence.strip().split()
    if not words:
        return ""

    neg_marker = "कोन्या" if dialect in [Dialect.DHUNDHARI, Dialect.SHEKHAWATI] else "कोनी"

    # If sentence ends with copula 'है' / 'छै', replace with 'कोनी' or prepend
    if words[-1] in ["है", "छै", "सै"]:
        return " ".join(words[:-1]) + f" {neg_marker}"

    # Default: insert before final verb
    if len(words) >= 2:
        return " ".join(words[:-1]) + f" {neg_marker} " + words[-1]
    return f"{neg_marker} {sentence}"


def prohibitive(verb: str) -> str:
    """
    Constructs prohibitive imperative command ('Do not do X!').
    Uses the iconic Rajasthani prohibitive particle 'मती' (mati).
    Examples:
        >>> prohibitive("जा")
        'मती जा!'
        >>> prohibitive("बोल")
        'मती बोल!'
        >>> prohibitive("खावो")
        'मती खावो!'
    """
    return f"मती {verb.strip()}!"
