# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Verb Conjugation & Aspect Engine
=============================================================
Conjugates regular and irregular Rajasthani verbs across tenses
(Present, Past, Future, Continuous, Habitual, Imperative, Presumptive),
persons (1st, 2nd, 3rd), genders, and major dialectal variations
(Marwari, Mewari, Dhundhari).
"""

from typing import Dict, List, Optional, Tuple
from rajasthani.constants import Tense, Person, Gender, GrammaticalNumber, Dialect

# Irregular verb past stems
IRREGULAR_PAST: Dict[str, Dict[str, str]] = {
    "जाणो": {"m_sg": "गयो", "f_sg": "गई", "m_pl": "गया", "f_pl": "गई"},
    "आवणो": {"m_sg": "आयो", "f_sg": "आई", "m_pl": "आया", "f_pl": "आई"},
    "करणो": {"m_sg": "कर्यो", "f_sg": "करी", "m_pl": "कर्या", "f_pl": "करी"},
    "लेवणो": {"m_sg": "लियो", "f_sg": "ली", "m_pl": "लिया", "f_pl": "ली"},
    "देवणो": {"m_sg": "दियो", "f_sg": "दी", "m_pl": "दिया", "f_pl": "दी"},
    "होणो": {"m_sg": "ह्वै गयो", "f_sg": "ह्वै गई", "m_pl": "ह्वै गया", "f_pl": "ह्वै गई"},
    "पीवणो": {"m_sg": "पीयौ", "f_sg": "पीई", "m_pl": "पीया", "f_pl": "पीई"},
    "खाणो": {"m_sg": "खायो", "f_sg": "खाई", "m_pl": "खाया", "f_pl": "खाई"},
}


def extract_root(infinitive: str) -> str:
    """
    Extracts the root stem from a Rajasthani verb infinitive ending in -णो, -णू, or -ना.
    Examples:
        खाणो -> खा
        जाणो -> जा
        करणो -> कर
        बोलणो -> बोल
        लिखणो -> लिख
        सुणणो -> सुण
    """
    clean = infinitive.strip()
    for suffix in ["णो", "णू", "ना", "नूं"]:
        if clean.endswith(suffix):
            return clean[:-len(suffix)]
    return clean


def conjugate_to_be(
    tense: Tense = Tense.PRESENT,
    person: Person = Person.THIRD,
    number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
    gender: Gender = Gender.MASCULINE,
    dialect: Dialect = Dialect.MARWARI,
) -> str:
    """
    Conjugates the Rajasthani copula / existential auxiliary ('to be').
    Supports Marwari (है/थो), Mewari (है/हो), and Dhundhari (छै/छो).
    """
    if tense == Tense.PRESENT:
        if dialect in [Dialect.DHUNDHARI, Dialect.HARAUTI]:
            if person == Person.FIRST:
                return "छू" if number == GrammaticalNumber.SINGULAR else "छां"
            elif person == Person.SECOND:
                return "छै" if number == GrammaticalNumber.SINGULAR else "छो"
            else:
                return "छै" if number == GrammaticalNumber.SINGULAR else "छैं"
        else:  # Marwari / Mewari / Standard
            if person == Person.FIRST:
                return "हूँ" if number == GrammaticalNumber.SINGULAR else "हां"
            elif person == Person.SECOND:
                return "है" if number == GrammaticalNumber.SINGULAR else "हो"
            else:
                return "है" if number == GrammaticalNumber.SINGULAR else "हैं"

    elif tense == Tense.PAST:
        if dialect == Dialect.MEWARI:
            if gender == Gender.FEMININE:
                return "ही"
            return "हो" if number == GrammaticalNumber.SINGULAR else "हा"
        elif dialect in [Dialect.DHUNDHARI, Dialect.HARAUTI]:
            if gender == Gender.FEMININE:
                return "छी"
            return "छो" if number == GrammaticalNumber.SINGULAR else "छा"
        else:  # Marwari / Standard
            if gender == Gender.FEMININE:
                return "थी"
            return "थो" if number == GrammaticalNumber.SINGULAR else "था"

    elif tense == Tense.FUTURE:
        if person == Person.FIRST:
            return "होऊँला" if number == GrammaticalNumber.SINGULAR else "होवांला"
        elif person == Person.SECOND:
            return "होवेला" if number == GrammaticalNumber.SINGULAR else "होवोला"
        else:
            return "होसी" if number == GrammaticalNumber.SINGULAR else "होवेला"

    return "है"


def conjugate(
    verb: str,
    tense: Tense = Tense.PRESENT,
    person: Person = Person.THIRD,
    number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
    gender: Gender = Gender.MASCULINE,
    dialect: Dialect = Dialect.MARWARI,
) -> str:
    """
    Main conjugation engine for Rajasthani verbs.
    Supports Present, Past, Future, Continuous, Habitual, and Imperative.
    """
    infinitive = verb if (verb.endswith("णो") or verb.endswith("णू")) else verb + "णो"
    root = extract_root(infinitive)

    # 1. Present Habitual / Indicative
    if tense == Tense.PRESENT:
        copula = conjugate_to_be(Tense.PRESENT, person, number, gender, dialect)
        if person == Person.FIRST:
            ending = "ऊँ" if number == GrammaticalNumber.SINGULAR else "आं"
            return f"{root}{ending} {copula}".strip()
        elif person == Person.SECOND:
            if number == GrammaticalNumber.SINGULAR:
                return f"{root}वै {copula}".strip()
            else:
                return f"{root}वो {copula}".strip()
        else:  # THIRD
            return f"{root}वै {copula}".strip()

    # 2. Past (Perfective)
    elif tense == Tense.PAST:
        if infinitive in IRREGULAR_PAST:
            forms = IRREGULAR_PAST[infinitive]
            if gender == Gender.FEMININE:
                return forms["f_sg"] if number == GrammaticalNumber.SINGULAR else forms["f_pl"]
            else:
                return forms["m_sg"] if number == GrammaticalNumber.SINGULAR else forms["m_pl"]
        else:
            # Regular past formation: root + -यो / -ी / -या
            if gender == Gender.FEMININE:
                if root and (root[-1] in "ािीुूेैोौ" or "\u0904" <= root[-1] <= "\u0914"):
                    return f"{root}ई"
                else:
                    return f"{root}ी"
            else:
                return f"{root}यो" if number == GrammaticalNumber.SINGULAR else f"{root}या"

    # 3. Future
    elif tense == Tense.FUTURE:
        if dialect in [Dialect.DHUNDHARI, Dialect.HARAUTI]:
            # Dhundhari uses -गो / -गी / -गा
            if person == Person.FIRST:
                suffix = "ऊँगो" if gender == Gender.MASCULINE else "ऊँगी"
                return f"{root}{suffix}"
            else:
                suffix = "गो" if gender == Gender.MASCULINE else "गी"
                return f"{root}वै{suffix}"
        else:
            # Marwari / Western uses -सी or -वेला
            if person == Person.FIRST:
                return f"{root}स्यूं" if number == GrammaticalNumber.SINGULAR else f"{root}स्यां"
            elif person == Person.SECOND:
                return f"{root}वेला" if number == GrammaticalNumber.SINGULAR else f"{root}वोला"
            else:
                return f"{root}सी" if number == GrammaticalNumber.SINGULAR else f"{root}सी"

    # 4. Continuous (रहा है)
    elif tense == Tense.CONTINUOUS:
        copula = conjugate_to_be(Tense.PRESENT, person, number, gender, dialect)
        aspect = "रही" if gender == Gender.FEMININE else ("रह्यो" if number == GrammaticalNumber.SINGULAR else "रह्या")
        return f"{root} {aspect} {copula}".strip()

    # 5. Past Continuous (रहा था)
    elif tense == Tense.PAST_CONTINUOUS:
        copula = conjugate_to_be(Tense.PAST, person, number, gender, dialect)
        aspect = "रही" if gender == Gender.FEMININE else ("रह्यो" if number == GrammaticalNumber.SINGULAR else "रह्या")
        return f"{root} {aspect} {copula}".strip()

    # 6. Imperative
    elif tense == Tense.IMPERATIVE:
        return imperative(verb, person, honorific=True)

    # 7. Subjunctive / Presumptive
    elif tense == Tense.PRESUMPTIVE:
        participle = f"{root}तो" if gender == Gender.MASCULINE else f"{root}ती"
        return f"{participle} होसी"

    return f"{root}वै"


IRREGULAR_IMPERATIVE = {
    "आवणो": "आज्यो",
    "जाणो": "जाइज्यो",
    "खाणो": "खाज्यो",
    "करणो": "करज्यो",
    "लेवणो": "लीज्यो",
    "देवणो": "दीज्यो",
}


def imperative(verb: str, person: Person = Person.SECOND, honorific: bool = True) -> str:
    """
    Forms Rajasthani imperative commands.
    Respectful/polite future imperative uses the celebrated suffix -ज्यो / -इज्यो!
    Examples:
        खाणो -> खाज्यो (Polite) / खावो (Familiar) / खा (Intimate)
        जाणो -> जाइज्यो / जावो / जा
        आवणो -> आज्यो / आवो / आ
        करणो -> करज्यो / करो / कर
    """
    infinitive = verb if (verb.endswith("णो") or verb.endswith("णू")) else verb + "णो"
    if honorific and infinitive in IRREGULAR_IMPERATIVE:
        return IRREGULAR_IMPERATIVE[infinitive]

    root = extract_root(infinitive)
    if honorific:
        # Polite respectful: -ज्यो / -इज्यो
        if root.endswith("ा") or root.endswith("ी") or root.endswith("े"):
            return f"{root}ज्यो"
        return f"{root}इज्यो"
    else:
        # Familiar
        return f"{root}वो"


def conjunctive_participle(verb: str) -> str:
    """
    Forms the conjunctive participle (having done / खाकर / जाकर).
    In Rajasthani: root + -'र / -ने (e.g. खा'र, जा'र, कर'र, खायने, जायने).
    """
    root = extract_root(verb)
    return f"{root}'र"


def passive_verb(verb: str) -> str:
    """
    Forms synthetic passive verb in Rajasthani ending in -इजणो / -इजै.
    Examples:
        करणो -> करीजै (is done)
        खाणो -> खाइजै (is eaten)
        बोलणो -> बोलिजै (is said)
        देखणो -> देखिजै (is seen)
    """
    root = extract_root(verb)
    return f"{root}इजै"
