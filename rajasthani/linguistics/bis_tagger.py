# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Bureau of Indian Standards (BIS) POS Tagger
========================================================================
Tags Rajasthani tokens with standard Indian Languages Part-of-Speech
Tagset (ILPOST / BIS Standard) codes:
N_NN (Noun), PR_PRP (Personal Pronoun), V_VM (Main Verb), V_VAUX (Auxiliary),
JJ (Adjective), RB (Adverb), PSP (Postposition), CC (Conjunction).
"""

from typing import List, Tuple
from rajasthani.lexicon.dictionary import get_default_dictionary
from rajasthani.phonetics import tokenize

# Common closed-class tags
CLOSED_CLASS_TAGS = {
    # Postpositions (PSP)
    "नै": "PSP", "सूं": "PSP", "स्यूं": "PSP", "रो": "PSP", "री": "PSP", "रा": "PSP",
    "को": "PSP", "की": "PSP", "का": "PSP", "मांय": "PSP", "माथे": "PSP", "कनै": "PSP",
    # Pronouns (PR_PRP)
    "म्हूँ": "PR_PRP", "म्हें": "PR_PRP", "आपां": "PR_PRP", "थूँ": "PR_PRP", "थें": "PR_PRP",
    "आप": "PR_PRP", "ओ": "PR_PRP", "वो": "PR_PRP", "वे": "PR_PRP", "मनै": "PR_PRP",
    # Interrogatives (PR_PRQ)
    "कुण": "PR_PRQ", "काईं": "PR_PRQ", "कठे": "PR_PRQ", "कदे": "PR_PRQ", "कियां": "PR_PRQ",
    # Auxiliaries (V_VAUX)
    "है": "V_VAUX", "हूँ": "V_VAUX", "हो": "V_VAUX", "हां": "V_VAUX", "हैं": "V_VAUX",
    "छै": "V_VAUX", "छू": "V_VAUX", "छो": "V_VAUX", "छा": "V_VAUX",
    "थो": "V_VAUX", "थी": "V_VAUX", "था": "V_VAUX",
    # Particles (RP_INJ / RP_HON)
    "सा": "RP_HON", "जी": "RP_HON", "हुकुम": "RP_HON",
    # Negation (NEG)
    "कोनी": "NEG", "नी": "NEG", "ना": "NEG", "मती": "NEG",
    # Conjunctions (CC_CCD)
    "अर": "CC_CCD", "पण": "CC_CCD",
}


def tag_sentence(text: str) -> List[Tuple[str, str]]:
    """
    Tokenizes and tags a Rajasthani sentence with BIS POS tags.
    """
    tokens = tokenize(text)
    tagged = []
    d = get_default_dictionary()

    for tok in tokens:
        if tok in CLOSED_CLASS_TAGS:
            tagged.append((tok, CLOSED_CLASS_TAGS[tok]))
            continue

        if tok in ["।", "?", "!", ",", "."]:
            tagged.append((tok, "RD_PUNC"))
            continue

        # Look up in dictionary with exact=True
        w = d.lookup(tok, exact=True)
        if w:
            if w.pos == "noun":
                tagged.append((tok, "N_NN"))
            elif w.pos == "verb":
                tagged.append((tok, "V_VM"))
            elif w.pos == "adjective":
                tagged.append((tok, "JJ"))
            elif w.pos == "adverb":
                tagged.append((tok, "RB"))
            elif w.pos == "interjection":
                tagged.append((tok, "RP_INJ"))
            else:
                tagged.append((tok, "N_NN"))
        else:
            # Heuristic verb check
            if tok.endswith("णो") or tok.endswith("वै") or tok.endswith("सी") or tok.endswith("यो"):
                tagged.append((tok, "V_VM"))
            else:
                tagged.append((tok, "N_NN"))

    return tagged
