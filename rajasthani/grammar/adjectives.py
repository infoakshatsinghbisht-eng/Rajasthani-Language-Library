# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Adjective Agreement & Comparison
=============================================================
Handles declinable vs indeclinable adjectives, gender/number agreement
(चोखो/चोखी/चोखा), comparative ('सूं चोखो') and superlative ('सगळां सूं चोखो').
"""

from typing import Dict, Optional
from rajasthani.constants import Gender, GrammaticalNumber


def agree_adjective(adjective: str, gender: Gender = Gender.MASCULINE, number: GrammaticalNumber = GrammaticalNumber.SINGULAR) -> str:
    """
    Inflects marked Rajasthani adjectives ending in -ओ (-o).
    Examples:
        चोखो (good) -> चोखो (m sg), चोखी (f sg/pl), चोखा (m pl)
        मीठो (sweet) -> मीठो, मीठी, मीठा
        धोळो (white) -> धोळो, धोळी, धोळा
        काळो (black) -> काळो, काळी, काळा
        मोटो (big) -> मोटो, मोटी, मोटा
        नान्हो (small) -> नान्हो, नान्ही, नान्हा
    Unmarked adjectives ending in consonants (लाल, साफ, सुंदर, भारी) remain indeclinable.
    """
    clean = adjective.strip()
    if clean.endswith("ो") or clean.endswith("ौ"):
        stem = clean[:-1]
        if gender == Gender.FEMININE:
            return f"{stem}ी"
        elif number == GrammaticalNumber.PLURAL:
            return f"{stem}ा"
        return clean
    return clean


def comparative(adjective: str, standard: str) -> str:
    """
    Constructs comparative construction ('more than X'):
    Example:
        >>> comparative("चोखो", "राम")
        'राम सूं चोखो'
    """
    return f"{standard} सूं {adjective}"


def superlative(adjective: str) -> str:
    """
    Constructs superlative construction ('best of all'):
    Example:
        >>> superlative("चोखो")
        'सगळां सूं चोखो'
    """
    return f"सगळां सूं {adjective}"
