# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Noun Morphology & Declension
=========================================================
Handles noun inflection, gender alternation, pluralization, oblique cases,
and expressive diminutive/augmentative suffixes (-लियो, -ड़ो, -ड़ी).
"""

from typing import Dict, List, Optional, Tuple
from rajasthani.constants import Gender, GrammaticalNumber, Case

# Common irregular noun plurals in Rajasthani
IRREGULAR_PLURALS: Dict[str, str] = {
    "माणस": "माणस",
    "लोग": "लोग",
    "भाटा": "भाटा",
    "पाणी": "पाणी",
    "घी": "घी",
    "दूध": "दूध",
}


def pluralize(noun: str, gender: Gender = Gender.MASCULINE) -> str:
    """
    Returns the direct plural form of a Rajasthani noun.
    Rules:
    - Masc ending in -ओ (-o) -> changes to -आ (-aa): घोड़ो -> घोड़ा, कमरो -> कमरा, बेटो -> बेटा
    - Masc ending in consonant -> stays unchanged in direct plural: घर -> घर, हाथ -> हाथ
    - Fem ending in -ई (-ee) -> changes to -इयां / -याँ: छोरी -> छोरियां, घोड़ी -> घोड़ियाँ
    - Fem ending in consonant -> adds -ां / -एं: आँख -> आंखां, बात -> बातां
    """
    if noun in IRREGULAR_PLURALS:
        return IRREGULAR_PLURALS[noun]

    clean = noun.strip()
    if not clean:
        return ""

    if gender == Gender.MASCULINE:
        if clean.endswith("ो"):
            return clean[:-1] + "ा"
        elif clean.endswith("ौ"):
            return clean[:-1] + "ा"
        return clean
    else:  # FEMININE
        if clean.endswith("ी"):
            return clean[:-1] + "ियां"
        elif clean.endswith("ा"):
            return clean + "एं"
        else:
            return clean + "ां"


def to_oblique(noun: str, gender: Gender = Gender.MASCULINE, number: GrammaticalNumber = GrammaticalNumber.SINGULAR) -> str:
    """
    Forms the oblique base of a noun prior to attaching postpositions.
    Rules:
    - Masc Sg in -ओ -> changes to -आ: घोड़ो -> घोड़ा (घोड़ा नै, घोड़ा माथे)
    - Masc Plural oblique -> adds -ां: घोड़ा -> घोड़ों / घोड़ां (घोड़ां नै)
    - Consonant noun oblique plural -> adds -ां: घर -> घरां (घरां मांय), हाथ -> हाथां (हाथां सूं)
    - Fem Sg in -ई -> stays in -ई: घोड़ी -> घोड़ी (घोड़ी नै)
    - Fem Plural oblique -> adds -ां: छोरियां -> छोरियां (छोरियां नै)
    """
    clean = noun.strip()
    if not clean:
        return ""

    if number == GrammaticalNumber.SINGULAR:
        if gender == Gender.MASCULINE:
            if clean.endswith("ो") or clean.endswith("ौ"):
                return clean[:-1] + "ा"
            return clean
        else:
            return clean
    else:  # PLURAL
        if clean.endswith("ा"):
            return clean[:-1] + "ां"
        elif clean.endswith("ियां"):
            return clean
        elif clean.endswith("ी"):
            return clean[:-1] + "ियां"
        else:
            return clean + "ां"


def decline_noun(noun: str, gender: Gender = Gender.MASCULINE, number: GrammaticalNumber = GrammaticalNumber.SINGULAR) -> Dict[str, str]:
    """
    Produces complete case paradigm for a noun.
    """
    obl = to_oblique(noun, gender, number)
    direct = noun if number == GrammaticalNumber.SINGULAR else pluralize(noun, gender)

    return {
        "direct": direct,
        "oblique": obl,
        "ergative": f"{obl} नै",
        "dative": f"{obl} नै",
        "ablative": f"{obl} सूं",
        "genitive_m": f"{obl} रो",
        "genitive_f": f"{obl} री",
        "genitive_pl": f"{obl} रा",
        "locative_in": f"{obl} मांय",
        "locative_on": f"{obl} माथे",
        "vocative": f"हे {obl}!",
    }


def to_feminine(masc_noun: str) -> str:
    """
    Derives feminine noun form from masculine noun.
    Examples:
        घोड़ो -> घोड़ी
        छोरो -> छोरी
        ऊंट -> ऊंटणी
        शेर -> शेरणी
    """
    clean = masc_noun.strip()
    if clean.endswith("ो") or clean.endswith("ौ"):
        return clean[:-1] + "ी"
    if clean.endswith("ा"):
        return clean[:-1] + "ी"
    return clean + "णी"


def to_masculine(fem_noun: str) -> str:
    """
    Derives masculine noun form from feminine noun.
    Examples:
        घोड़ी -> घोड़ो
        छोरी -> छोरो
        ऊंटणी -> ऊंट
    """
    clean = fem_noun.strip()
    if clean.endswith("णी"):
        return clean[:-2]
    if clean.endswith("ी"):
        return clean[:-1] + "ो"
    return clean


def make_diminutive(noun: str) -> str:
    """
    Derives Rajasthani expressive diminutive form using -लियो / -ड़ी / -कियो.
    Examples:
        टाबर -> टाबरियो
        खाट -> खाटली
        ढोल -> ढोलकियो
        बात -> बातड़ी
    """
    clean = noun.strip()
    if clean.endswith("ी"):
        return clean + "ड़ी"
    if clean.endswith("ो"):
        return clean[:-1] + "लियो"
    return clean + "ियो"
