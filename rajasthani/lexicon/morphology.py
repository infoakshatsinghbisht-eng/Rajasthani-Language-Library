# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Morphology & Paradigm Generation
==============================================================
Generates inflectional paradigms for nouns, verbs, and adjectives;
provides morphological stemming and surface-form decomposition.
"""

from typing import Dict, List, Set, Tuple
from rajasthani.constants import Gender, GrammaticalNumber, Person, Tense, Dialect
from rajasthani.grammar.nouns import decline_noun, pluralize
from rajasthani.grammar.verbs import conjugate, extract_root


def generate_noun_paradigm(noun: str, gender: Gender = Gender.MASCULINE) -> Dict[str, Dict[str, str]]:
    """
    Generates the complete 2x8 case inflection paradigm for a noun (Singular & Plural).
    """
    return {
        "singular": decline_noun(noun, gender, GrammaticalNumber.SINGULAR),
        "plural": decline_noun(noun, gender, GrammaticalNumber.PLURAL),
    }


def generate_verb_paradigm(verb: str, dialect: Dialect = Dialect.MARWARI) -> Dict[str, Dict[str, str]]:
    """
    Generates a full tense/person matrix for a given verb.
    """
    tenses = [Tense.PRESENT, Tense.PAST, Tense.FUTURE, Tense.CONTINUOUS]
    paradigm = {}

    for t in tenses:
        t_key = t.value
        paradigm[t_key] = {
            "1sg_m": conjugate(verb, t, Person.FIRST, GrammaticalNumber.SINGULAR, Gender.MASCULINE, dialect),
            "1sg_f": conjugate(verb, t, Person.FIRST, GrammaticalNumber.SINGULAR, Gender.FEMININE, dialect),
            "1pl_m": conjugate(verb, t, Person.FIRST, GrammaticalNumber.PLURAL, Gender.MASCULINE, dialect),
            "2sg_m": conjugate(verb, t, Person.SECOND, GrammaticalNumber.SINGULAR, Gender.MASCULINE, dialect),
            "2pl_m": conjugate(verb, t, Person.SECOND, GrammaticalNumber.PLURAL, Gender.MASCULINE, dialect),
            "3sg_m": conjugate(verb, t, Person.THIRD, GrammaticalNumber.SINGULAR, Gender.MASCULINE, dialect),
            "3sg_f": conjugate(verb, t, Person.THIRD, GrammaticalNumber.SINGULAR, Gender.FEMININE, dialect),
            "3pl_m": conjugate(verb, t, Person.THIRD, GrammaticalNumber.PLURAL, Gender.MASCULINE, dialect),
        }
    return paradigm


def stem_word(word: str) -> str:
    """
    Rule-based morphological stemmer for Rajasthani words:
    Strips inflectional case endings (-सूं, -नै, -मांय), plural markers (-ां, -इयां),
    and common verbal suffixes (-वै, -सी, -यो, -ी).
    """
    clean = word.strip()

    # Strip attached postpositions
    for postp in ["सूं", "नै", "मांय", "माथे", "रो", "री", "रा"]:
        if clean.endswith(postp) and len(clean) > len(postp) + 1:
            clean = clean[:-len(postp)].strip()

    # Strip plural suffixes
    if clean.endswith("ियां") and len(clean) > 4:
        return clean[:-4] + "ी"
    if clean.endswith("ां") and len(clean) > 2:
        return clean[:-2]

    # Strip verbal suffixes
    for v_suf in ["वेला", "स्यूं", "स्यां", "सी", "वै", "यो", "या"]:
        if clean.endswith(v_suf) and len(clean) > len(v_suf) + 1:
            return clean[:-len(v_suf)]

    return clean
