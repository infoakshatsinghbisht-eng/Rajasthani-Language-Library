# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Voice & Medio-Passive Inability
============================================================
Handles synthetic passive in -इजणो / -इजै and the Rajasthani
medio-passive of physical or psychological inability:
'म्हासूं चलिजै कोनी' (I cannot walk).
"""

from typing import Dict
from rajasthani.grammar.verbs import extract_root


PASSIVE_OVERRIDES = {
    "चालणो": "चलिजै",
    "करणो": "करीजै",
    "खाणो": "खाइजै",
    "देखणो": "देखिजै",
    "बोलणो": "बोलिजै",
    "सुणणो": "सुणिजै",
}


def passive_form(verb: str) -> str:
    """
    Derives synthetic passive verb form in -इजै.
    Examples:
        करणो -> करीजै
        चालणो -> चलिजै
        खाणो -> खाइजै
        देखणो -> देखिजै
    """
    infinitive = verb if verb.endswith("णो") else verb + "णो"
    if infinitive in PASSIVE_OVERRIDES:
        return PASSIVE_OVERRIDES[infinitive]

    root = extract_root(infinitive)
    # Shorten stem vowel if needed
    if "ा" in root:
        root = root.replace("ा", "")
    return f"{root}इजै"


def medio_passive_inability(subject_ablative: str, verb: str) -> str:
    """
    Constructs medio-passive construction expressing inability:
    Examples:
        >>> medio_passive_inability("म्हासूं", "चालणो")
        'म्हासूं चलिजै कोनी।'
        >>> medio_passive_inability("उणसूं", "बोलणो")
        'उणसूं बोलिजै कोनी।'
    """
    pass_v = passive_form(verb)
    return f"{subject_ablative} {pass_v} कोनी।"
