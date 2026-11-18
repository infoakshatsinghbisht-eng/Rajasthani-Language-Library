# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Inceptive Aspect Engine
====================================================
Synthetic inceptive aspect marking beginning of action using
infinitive (-ण) + लागणो auxiliary (लाग्यो / लागी / लाग्या).
Examples: 'पाणी बरसण लाग्यो', 'टाबर रोवण लागी', 'लोग हँसण लाग्या'.
"""

from typing import Dict
from rajasthani.constants import Gender, GrammaticalNumber


def inceptive_clause(subject: str, verb_root: str, gender: Gender = Gender.MASCULINE, plural: bool = False) -> str:
    """
    Constructs an inceptive aspect sentence.
    """
    aux = "लागी" if gender == Gender.FEMININE else ("लाग्या" if plural else "लाग्यो")
    return f"{subject} {verb_root}ण {aux}।"
