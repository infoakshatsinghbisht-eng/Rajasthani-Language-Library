# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Folk Music, Instruments & Dances (संगीत अर नृत्य)
==============================================================================
Comprehensive documentation of Rajasthani folk musical heritage:
Instruments (Ravanahatha, Kamaicha, Khartal, Morchang, Algoza, Chang),
Dances (Ghoomar, Kalbelia, Bhavai, Chari, Gair, Kachhi Ghodi), and hereditary
troubadour castes (Langa, Manganiyar, Dholi, Mirasi, Bhopa).
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class FolkInstrument:
    name: str
    roman: str
    category: str  # bowed, plucked, wind, percussion, idiophone
    description: str
    played_by: str
    cultural_context: str


@dataclass
class FolkDance:
    name: str
    roman: str
    performers: str  # women, men, both
    description: str
    instruments_used: List[str]
    unesco_status: bool


INSTRUMENTS_DATABASE: List[FolkInstrument] = [
    FolkInstrument(
        name="रावणहत्थो (Ravanahatha)",
        roman="Ravanahatha",
        category="bowed_string",
        description="Ancient bowed stringed instrument made of split coconut shell covered with goat hide, long bamboo shaft, and horsehair bow with ghungroos.",
        played_by="भोपा (Bhopa priests of Pabuji)",
        cultural_context="Used during nocturnal performances of Pabuji ki Phad epic narration across desert villages.",
    ),
    FolkInstrument(
        name="कमायचो (Kamaicha)",
        roman="Kamaicha",
        category="bowed_string",
        description="Spherical hollowed mango-wood body covered with goat skin, featuring 17 strings played with a curved wooden horsehair bow.",
        played_by="मांगणियार (Manganiyar masters)",
        cultural_context="Quintessential sonic soul of the Thar desert, producing deep resonant microtonal slides.",
    ),
    FolkInstrument(
        name="खड़ताल (Khartal)",
        roman="Khartal",
        category="idiophone_percussion",
        description="Pairs of hardwood clappers (sheesham) held in hands and clicked with lightning-fast rhythmic virtuosity.",
        played_by="मांगणियार अर लंगा गायक",
        cultural_context="Rhythmic companion to the Kamaicha and Dholak, creating intricate polyrhythms.",
    ),
    FolkInstrument(
        name="अळगोजो (Algoza)",
        roman="Algoza",
        category="wind",
        description="Twin beak flutes blown simultaneously using circular breathing, one maintaining continuous drone while the other plays melodic variations.",
        played_by="चरवाहा (Shepherds and Meena/Gurjar musicians)",
        cultural_context="Echoes across pasturelands and desert plains during folk gatherings.",
    ),
    FolkInstrument(
        name="मोरचंग (Morchang)",
        roman="Morchang",
        category="idiophone_mouth_harp",
        description="Small metal horseshoe-shaped harp placed between teeth, with vibrating tongue modulated by mouth cavity resonance.",
        played_by="लोक गायक अर वादक",
        cultural_context="Provides hypnotic rhythm and harmonic sound effects in folk ensembles.",
    ),
    FolkInstrument(
        name="चंग (Chang)",
        roman="Chang",
        category="percussion_frame_drum",
        description="Large circular single-headed wooden frame drum played with hands and sticks during the spring festival of Holi.",
        played_by="शेखावाटी अर मारवाड़ रा ग्रामीण",
        cultural_context="Soul of Holi festivities when Dhamal and Faag songs are sung all night.",
    ),
]

DANCES_DATABASE: List[FolkDance] = [
    FolkDance(
        name="घूमर (Ghoomar)",
        roman="Ghoomar",
        performers="women",
        description="Graceful royal folk dance featuring circular swirling movements (ghoomna) where the vibrant Ghagra blossoms like a flower.",
        instruments_used=["ढोलक", "नगाड़ा", "शहनाई"],
        unesco_status=False,
    ),
    FolkDance(
        name="कालबेलिया (Kalbelia)",
        roman="Kalbelia",
        performers="women (accompanied by male musicians)",
        description="Sensuous, acrobatic serpentine folk dance mimicking snake movements, performed in shimmering black embroidered skirts.",
        instruments_used=["पूँगी / बीन", "डफली", "खंजरी", "ढोलक"],
        unesco_status=True,  # Inscribed on UNESCO Intangible Cultural Heritage List (2010)
    ),
    FolkDance(
        name="भवाई (Bhavai)",
        roman="Bhavai",
        performers="women",
        description="Spectacular equilibrium balancing dance where dancer balances 7 to 9 brass pitchers on her head while dancing atop swords or glass shards.",
        instruments_used=["झांझ", "सारंगी", "ढोलक"],
        unesco_status=False,
    ),
    FolkDance(
        name="चरी नृत्य (Chari Dance)",
        roman="Chari",
        performers="women",
        description="Graceful Kishangarh dance balancing brass pots lit with flaming cotton seeds soaked in oil on head.",
        instruments_used=["ढोल", "बांकिया", "थाली"],
        unesco_status=False,
    ),
    FolkDance(
        name="गैर नृत्य (Gair Dance)",
        roman="Gair",
        performers="men",
        description="Energetic circular martial folk dance of Mewar and Barmer performed with wooden batons (khanda) striking in rhythm.",
        instruments_used=["मांदल", "ढोल", "बांकिया"],
        unesco_status=False,
    ),
    FolkDance(
        name="कच्छी घोड़ी (Kachhi Ghodi)",
        roman="Kachhi Ghodi",
        performers="men",
        description="Theatrical mock banditry and cavalry battle dance performed wearing dummy horses made of bamboo frames and vibrant cloth.",
        instruments_used=["ढोल", "ताशा", "बांकिया"],
        unesco_status=False,
    ),
]


def get_instruments() -> List[FolkInstrument]:
    """Returns all traditional Rajasthani musical instruments."""
    return list(INSTRUMENTS_DATABASE)


def get_dances() -> List[FolkDance]:
    """Returns all cataloged traditional Rajasthani folk dances."""
    return list(DANCES_DATABASE)
