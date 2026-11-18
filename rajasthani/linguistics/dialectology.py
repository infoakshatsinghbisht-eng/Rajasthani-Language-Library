# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Dialectology & Comparative Phonology
==================================================================
Comparative matrix and transformational rules across the major dialects
of Rajasthani: Marwari, Mewari, Dhundhari, Harauti, Shekhawati, and Bagri.
"""

from typing import Dict, List, Optional
from rajasthani.constants import Dialect

DIALECT_COMPARISONS: Dict[str, Dict[str, str]] = {
    "Marwari (Western)": {
        "region": "Jodhpur, Jaisalmer, Bikaner, Nagaur, Barmer",
        "genitive_marker": "रो / री / रा (mharo, tharo)",
        "present_copula": "है / हैं (hai / hain)",
        "past_copula": "थो / थी / था (tho / thee / tha)",
        "future_suffix": "-सी / -वेला (khaasi / jaavela)",
        "infinitive": "-णो / -णू (khaano, jaano)",
        "hallmark": "Rich Dingal heritage, retroflex lateral ळ, split ergativity with नै",
    },
    "Dhundhari / Jaipuri (East-Central)": {
        "region": "Jaipur, Dausa, Tonk",
        "genitive_marker": "को / की / का (mhako, thako)",
        "present_copula": "छै / छैं (chhai / chhain)",
        "past_copula": "छो / छी / छा (chho / chhee / chha)",
        "future_suffix": "-गो / -गी / -गा (khaaigo / jaaigo)",
        "infinitive": "-बो / -णो (khaarbo, karbo)",
        "hallmark": "Pervasive use of 'छै' copula and '-गो' future endings",
    },
    "Mewari (South-Central)": {
        "region": "Udaipur, Rajsamand, Chittorgarh, Bhilwara",
        "genitive_marker": "रो / री / रा (mharo, tharo)",
        "present_copula": "है / हैं (hai)",
        "past_copula": "हो / ही / हा (ho / hee / ha)",
        "future_suffix": "-सी (khaasi, jaasi)",
        "infinitive": "-णो / -वू (khaano, karano)",
        "hallmark": "Past copula in 'हो/ही/हा' and deep historical association with Maharana Pratap",
    },
    "Harauti (South-Eastern)": {
        "region": "Kota, Bundi, Baran, Jhalawar",
        "genitive_marker": "को / की / का",
        "present_copula": "छै / छैं",
        "past_copula": "छो / छी / छा",
        "future_suffix": "-गो / -गा",
        "infinitive": "-बो / -णो",
        "hallmark": "Close affinity to Dhundhari with distinct tonal intonations",
    },
    "Shekhawati (North-Central)": {
        "region": "Sikar, Jhunjhunu, Churu",
        "genitive_marker": "को / की / का",
        "present_copula": "सै / सैं (sai / sain)",
        "past_copula": "थो / थी / था",
        "future_suffix": "-सी / -गो",
        "infinitive": "-णो",
        "hallmark": "Copula in 'सै' and negative 'कोन्या'",
    },
}


def get_dialect_features(dialect_name: str) -> Optional[Dict[str, str]]:
    """Returns linguistic features of a dialect."""
    for name, features in DIALECT_COMPARISONS.items():
        if dialect_name.lower() in name.lower():
            return features
    return None


def list_all_dialects() -> Dict[str, Dict[str, str]]:
    """Returns the comparative dialectology matrix."""
    return dict(DIALECT_COMPARISONS)
