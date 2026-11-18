# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Obligative Modality Engine
=======================================================
Deontic and compulsive obligation constructions:
- Dative subject + Infinitive (-णो) + पड़णो auxiliary (e.g. 'मनै जाणो पड़ेला' / 'उणनै काम करणो पड़े')
- Moral obligation with चाहीजै (e.g. 'आपांनै सच बोलणो चाहीजै')
"""

from typing import Dict


def obligative_clause(subject_dative: str, verb_infinitive: str, moral: bool = False) -> str:
    """
    Constructs an obligative clause in Rajasthani.
    Examples:
        >>> obligative_clause("मनै", "जाणो")
        'मनै जाणो पड़ेला।'
        >>> obligative_clause("आपांनै", "सच बोलणो", moral=True)
        'आपांनै सच बोलणो चाहीजै।'
    """
    if moral:
        return f"{subject_dative} {verb_infinitive} चाहीजै।"
    return f"{subject_dative} {verb_infinitive} पड़ेला।"
