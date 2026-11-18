# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Postpositions & Case Markers
==========================================================
System of postpositions governing nominal and pronominal oblique arguments
across Rajasthani dialects (रो/री/रा, को/की/का, नै, सूं, मांय, माथे, कने).
"""

from typing import Dict, Optional
from rajasthani.constants import Case, Dialect

# Primary postposition database
POSTPOSITIONS = {
    Case.ERGATIVE: {
        "mwr": "नै", "mew": "नै", "dhd": "नै", "hoj": "नै",
        "description": "Ergative past-tense subject marker (राम नै)",
    },
    Case.ACCUSATIVE_DATIVE: {
        "mwr": "नै", "mew": "नै", "dhd": "नै", "hoj": "नै",
        "description": "Accusative / Dative object marker (मनै / राम नै)",
    },
    Case.INSTRUMENTAL_ABLATIVE: {
        "mwr": "सूं", "mew": "सूं", "dhd": "सूं", "hoj": "सूं",
        "description": "Instrumental / Ablative marker (हाथ सूं, गाँव सूं)",
    },
    Case.GENITIVE: {
        "mwr": "रो / री / रा", "mew": "रो / री / रा", "dhd": "को / की / का", "hoj": "को / की / का",
        "description": "Genitive possessive marker (agreeing with head noun in gender/number)",
    },
    Case.LOCATIVE: {
        "mwr": "मांय / माथे", "mew": "मांय / माथे", "dhd": "महि / ऊपर", "hoj": "महि / माथे",
        "description": "In / On locative marker (घर मांय, घोड़ा माथे)",
    },
}

SPATIAL_POSTPOSITIONS = {
    "near": {"rajasthani": "कनै / पासै", "roman": "kanai / paasai", "english": "near / next to"},
    "inside": {"rajasthani": "मांय / मांयने", "roman": "maayn / maayne", "english": "inside"},
    "outside": {"rajasthani": "बारै", "roman": "baarai", "english": "outside"},
    "above": {"rajasthani": "माथे / ऊपर", "roman": "maathe / oopar", "english": "on / upon / above"},
    "below": {"rajasthani": "नीचै / हेठै", "roman": "neechai / hethai", "english": "under / below"},
    "front": {"rajasthani": "आगै / सामै", "roman": "aagai / saamai", "english": "in front of"},
    "behind": {"rajasthani": "पाछै", "roman": "paachhai", "english": "behind"},
    "with": {"rajasthani": "सागे / लारै", "roman": "saage / laarai", "english": "with / along with"},
}


def get_marker(case: Case, dialect: Dialect = Dialect.MARWARI) -> str:
    """Retrieves the appropriate case marker for a given case and dialect."""
    entry = POSTPOSITIONS.get(case, {})
    dial_key = dialect.value if hasattr(dialect, "value") else str(dialect)
    return entry.get(dial_key, entry.get("mwr", ""))


def attach_case(noun: str, case: Case, dialect: Dialect = Dialect.MARWARI) -> str:
    """Attaches the postposition to an oblique noun."""
    marker = get_marker(case, dialect)
    return f"{noun} {marker}".strip()
