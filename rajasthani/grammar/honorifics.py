# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Honorifics & Politeness Markers
============================================================
The royal and polite etiquette system in Rajasthani culture:
- सा (Sa) - Respectful clitic attached to names, titles, and greetings (राम राम सा, हुकुम सा, बाईसा)
- जी (Ji) - Polite particle (बापोजी, काकीजी)
- हुकुम (Hukum) - Deferential response indicating humble submission to authority
- खम्मा घणी (Khamma Ghani) - Royal salutation
"""

from typing import Dict, List


def add_honorific_sa(phrase: str) -> str:
    """
    Appends the traditional Rajasthani honorific particle 'सा' (Sa) appropriately.
    Examples:
        राम राम -> राम राम सा
        हाँ -> हाँ सा
        हुकुम -> हुकुम सा
    """
    clean = phrase.strip()
    if clean.endswith("सा"):
        return clean
    return f"{clean} सा"


def honorific_greeting(greeting: str = "ram_ram") -> str:
    """
    Returns polite Rajasthani greeting.
    """
    greetings = {
        "khamma_ghani": "खम्मा घणी सा",
        "ram_ram": "राम राम सा",
        "jai_mata_ji": "जय माता जी री सा",
        "jai_jinendra": "जय जिनेन्द्र सा",
        "hukum": "हुकुम सा",
    }
    return greetings.get(greeting, "राम राम सा")
