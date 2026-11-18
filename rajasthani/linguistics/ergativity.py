# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Ergativity & Agreement Validator
=============================================================
Validates split-ergative alignment in Rajasthani sentences:
In past perfective transitive sentences, the agent takes ergative marking (नै / म्हैं / तैं)
and the verb agrees with the patient / direct object in gender and number.
"""

from typing import Dict, List, Tuple
from rajasthani.grammar.syntax import TRANSITIVE_VERBS


def is_ergative_sentence(sentence: str) -> bool:
    """
    Checks if a sentence exhibits Rajasthani ergative construction.
    Criteria:
    - Subject has 'नै' or ergative pronoun 'म्हैं', 'तैं', 'उण'
    - Followed by transitive verb in past tense
    """
    words = sentence.strip().split()
    if not words:
        return False

    has_erg_subject = any(w in ["म्हैं", "तैं", "उण", "बां"] or w.endswith("नै") for w in words[:3])
    has_past_verb = any(
        w.endswith("यो") or w.endswith("या") or w.endswith("ई") or w in ["खायो", "खाई", "कर्यो", "दीधी", "लियो"]
        for w in words[-3:]
    )

    return has_erg_subject and has_past_verb
