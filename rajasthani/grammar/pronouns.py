# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Pronoun Paradigm & Clusivity Engine
================================================================
Comprehensive pronoun tables for 1st, 2nd, 3rd persons, demonstratives,
interrogatives, relatives, and Rajasthani's distinctive inclusive vs.
exclusive 1st person plural (आपां vs. म्हें).
"""

from typing import Dict, List, Optional
from rajasthani.constants import Person, GrammaticalNumber, Case

PRONOUN_TABLE: Dict[str, Dict[str, str]] = {
    # 1st Person Singular: "म्हूँ" (I)
    "1sg": {
        "direct": "म्हूँ",
        "roman": "mhoon",
        "oblique": "म्हा",
        "ergative": "म्हैं",
        "dative": "मनै / म्हारै",
        "ablative": "म्हासूं",
        "genitive_m": "म्हारो",
        "genitive_f": "म्हारी",
        "genitive_pl": "म्हारा",
        "locative": "म्हा मांय",
        "hindi": "मैं",
        "english": "I",
    },
    # 1st Person Plural Exclusive: "म्हें" (We - excluding the addressee)
    "1pl_excl": {
        "direct": "म्हें",
        "roman": "mhen",
        "oblique": "म्हां",
        "ergative": "म्हां",
        "dative": "म्हानै",
        "ablative": "म्हांसूं",
        "genitive_m": "म्हांरो",
        "genitive_f": "म्हांरी",
        "genitive_pl": "म्हांरा",
        "locative": "म्हां मांय",
        "hindi": "हम (तुमको छोड़कर)",
        "english": "we (exclusive)",
    },
    # 1st Person Plural Inclusive: "आपां" (We - including the addressee)
    "1pl_incl": {
        "direct": "आपां",
        "roman": "aapan",
        "oblique": "आपां",
        "ergative": "आपां",
        "dative": "आपांनै",
        "ablative": "आपांसूं",
        "genitive_m": "आपांरो",
        "genitive_f": "आपांरी",
        "genitive_pl": "आपांरा",
        "locative": "आपां मांय",
        "hindi": "हम सब (आप और हम)",
        "english": "we (inclusive)",
    },
    # 2nd Person Singular Informal: "थूँ" (Thou / You sg)
    "2sg": {
        "direct": "थूँ",
        "roman": "thoon",
        "oblique": "था",
        "ergative": "तैं",
        "dative": "तनै / थनै",
        "ablative": "थासूं",
        "genitive_m": "थारो",
        "genitive_f": "थारी",
        "genitive_pl": "थारा",
        "locative": "था मांय",
        "hindi": "तू",
        "english": "you (singular/intimate)",
    },
    # 2nd Person Plural Familiar: "थें" (You pl)
    "2pl": {
        "direct": "थें",
        "roman": "then",
        "oblique": "थां",
        "ergative": "थां",
        "dative": "थानै",
        "ablative": "थांसूं",
        "genitive_m": "थांरो",
        "genitive_f": "थांरी",
        "genitive_pl": "थांरा",
        "locative": "थां मांय",
        "hindi": "तुम / आप लोग",
        "english": "you (plural/familiar)",
    },
    # 2nd Person Polite / Honorific: "आप" (You polite)
    "2_hon": {
        "direct": "आप",
        "roman": "aap",
        "oblique": "आप",
        "ergative": "आप",
        "dative": "आपनै",
        "ablative": "आपसूं",
        "genitive_m": "आपरो",
        "genitive_f": "आपरी",
        "genitive_pl": "आपरा",
        "locative": "आप मांय",
        "hindi": "आप",
        "english": "you (honorific/polite)",
    },
    # 3rd Person Proximal Singular: "ओ / यो" (This / He / She here)
    "3sg_prox": {
        "direct": "ओ",
        "roman": "o / yo",
        "oblique": "ईं",
        "ergative": "ईं",
        "dative": "ईंनै",
        "ablative": "ईंसूं",
        "genitive_m": "ईंरो",
        "genitive_f": "ईंरी",
        "genitive_pl": "ईंरा",
        "locative": "ईं मांय",
        "hindi": "यह",
        "english": "this / he / she (proximal)",
    },
    # 3rd Person Distal Singular: "वो" (That / He / She there)
    "3sg_dist": {
        "direct": "वो",
        "roman": "vo",
        "oblique": "ऊँ",
        "ergative": "ऊँ",
        "dative": "उनै / ऊँनै",
        "ablative": "ऊँसूं",
        "genitive_m": "ऊँरो / उनरो",
        "genitive_f": "ऊँरी / उनरी",
        "genitive_pl": "ऊँरा / उनरा",
        "locative": "ऊँ मांय",
        "hindi": "वह",
        "english": "that / he / she (distal)",
    },
    # 3rd Person Plural: "वे / बा" (They / Those)
    "3pl": {
        "direct": "वे",
        "roman": "ve / ba",
        "oblique": "उनां / बां",
        "ergative": "उनां / बां",
        "dative": "उनांनै / बांनै",
        "ablative": "उनांसूं / बांसूं",
        "genitive_m": "उनांरो / बांरो",
        "genitive_f": "उनांरी / बांरी",
        "genitive_pl": "उनांरा / बांरा",
        "locative": "उनां मांय",
        "hindi": "वे / वो लोग",
        "english": "they / those",
    },
}

# Interrogative Pronouns
INTERROGATIVES: Dict[str, Dict[str, str]] = {
    "who": {"rajasthani": "कुण", "roman": "kun", "hindi": "कौन", "oblique": "किण"},
    "what": {"rajasthani": "काईं", "roman": "kaain", "hindi": "क्या", "oblique": "काईं"},
    "which": {"rajasthani": "कियो / की", "roman": "kiyo / kee", "hindi": "कौन सा", "oblique": "किण"},
    "whose": {"rajasthani": "किणरो", "roman": "kinro", "hindi": "किसका", "oblique": "किण"},
    "whom": {"rajasthani": "किणनै", "roman": "kinnai", "hindi": "किसे / किसको", "oblique": "किण"},
    "where": {"rajasthani": "कठे", "roman": "kathe", "hindi": "कहाँ", "oblique": "कठे"},
    "when": {"rajasthani": "कदे / कदी", "roman": "kade / kadee", "hindi": "कब", "oblique": "कदे"},
    "why": {"rajasthani": "क्यूँ", "roman": "kyun", "hindi": "क्यों", "oblique": "क्यूँ"},
    "how": {"rajasthani": "कियां / कीकर", "roman": "kiyan / keekar", "hindi": "कैसे", "oblique": "कियां"},
    "how_much": {"rajasthani": "कित्तो", "roman": "kitto", "hindi": "कितना", "oblique": "कित्ता"},
}

# Relative & Correlative Pronouns
RELATIVES: Dict[str, Dict[str, str]] = {
    "who_rel": {"rajasthani": "जको / जो", "roman": "jako / jo", "hindi": "जो", "correlative": "वो / तको"},
    "which_rel": {"rajasthani": "जियो", "roman": "jiyo", "hindi": "जो", "correlative": "तियो"},
    "where_rel": {"rajasthani": "जठे", "roman": "jathe", "hindi": "जहाँ", "correlative": "तठे / वठे"},
    "when_rel": {"rajasthani": "जदे", "roman": "jade", "hindi": "जब", "correlative": "तदे"},
    "how_rel": {"rajasthani": "जियां", "roman": "jiyan", "hindi": "जैसे", "correlative": "तियां / वियां"},
    "as_much_as": {"rajasthani": "जित्तो", "roman": "jitto", "hindi": "जितना", "correlative": "तित्तो"},
}


def get_pronoun(code: str) -> Optional[Dict[str, str]]:
    """Retrieves full case forms for a personal pronoun code (e.g. '1sg', '1pl_incl', '2sg')."""
    return PRONOUN_TABLE.get(code)


def get_possessive(code: str, gender: str = "m", plural: bool = False) -> str:
    """
    Returns the possessive adjective (e.g. 'म्हारो', 'म्हारी', 'म्हारा', 'थारो', 'थारी').
    """
    p = PRONOUN_TABLE.get(code)
    if not p:
        return ""
    if plural:
        return p.get("genitive_pl", p.get("genitive_m", ""))
    if gender.lower().startswith("f"):
        return p.get("genitive_f", "")
    return p.get("genitive_m", "")


def get_interrogative(key: str) -> Optional[Dict[str, str]]:
    """Retrieves Rajasthani interrogative pronoun (काईं, कुण, कठे, कदे, कियां, etc.)."""
    return INTERROGATIVES.get(key)


def get_relative(key: str) -> Optional[Dict[str, str]]:
    """Retrieves Rajasthani relative/correlative pronoun pair (जको-तको, जठे-वठे, जदे-तदे, etc.)."""
    return RELATIVES.get(key)
