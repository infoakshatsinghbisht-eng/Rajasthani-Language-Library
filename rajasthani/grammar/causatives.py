# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Causative Verb Derivation
======================================================
Derives primary (transitive/causative) and secondary (double causative)
verbs using the traditional suffixes -आवणो and -वावणो.
"""

from typing import Dict, Tuple
from rajasthani.grammar.verbs import extract_root

# Irregular causative root mappings
CAUSATIVE_OVERRIDES: Dict[str, Tuple[str, str]] = {
    "खाणो": ("खवावणो", "खवड़वावणो"),
    "पीवणो": ("पिलावणो", "पिलवावणो"),
    "सोवणो": ("सुवावणो", "सुववावणो"),
    "रोवणो": ("रुवावणो", "रुववावणो"),
    "धोवणो": ("धुवावणो", "धुववावणो"),
    "देणो": ("दिवावणो", "दिलवावणो"),
    "लेणो": ("लिवावणो", "लिलवावणो"),
}


def make_causative(verb: str, degree: int = 1) -> str:
    """
    Derives causative verb form.
    degree 1: Primary causative (-आवणो / -ावणो) -> e.g. करणो -> करावणो
    degree 2: Secondary causative (-वावणो) -> e.g. करणो -> करवावणो
    """
    infinitive = verb if verb.endswith("णो") else verb + "णो"
    if infinitive in CAUSATIVE_OVERRIDES:
        prim, sec = CAUSATIVE_OVERRIDES[infinitive]
        return prim if degree == 1 else sec

    root = extract_root(infinitive)
    # Shorten long vowels in stem: ई -> इ, ऊ -> उ, ए/ओ -> अ/उ
    short_root = root.replace("ी", "ि").replace("ू", "ु").replace("ो", "ु").replace("े", "ि")

    if degree == 1:
        # Primary causative: root + आवणो
        if short_root.endswith("ा"):
            return f"{short_root[:-1]}ावणो"
        return f"{short_root}ावणो"
    else:
        # Secondary causative: root + वावणो
        return f"{short_root}वावणो"
