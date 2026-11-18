# -*- coding: utf-8 -*-
"""Rajasthani Grammar Subpackage."""

from rajasthani.grammar.nouns import (
    pluralize,
    to_oblique,
    decline_noun,
    to_feminine,
    to_masculine,
    make_diminutive,
)
from rajasthani.grammar.pronouns import (
    PRONOUN_TABLE,
    get_pronoun,
    get_possessive,
    get_interrogative,
    get_relative,
)
from rajasthani.grammar.verbs import (
    extract_root,
    conjugate,
    conjugate_to_be,
    imperative,
    conjunctive_participle,
    passive_verb,
)
from rajasthani.grammar.causatives import make_causative
from rajasthani.grammar.postpositions import attach_case, get_marker, POSTPOSITIONS, SPATIAL_POSTPOSITIONS
from rajasthani.grammar.adjectives import agree_adjective, comparative, superlative
from rajasthani.grammar.adverbs import get_adverb, ADVERBS_CATALOG
from rajasthani.grammar.honorifics import add_honorific_sa, honorific_greeting
from rajasthani.grammar.negation import negate_sentence, prohibitive
from rajasthani.grammar.obligative import obligative_clause
from rajasthani.grammar.presumptive import presumptive_clause
from rajasthani.grammar.inceptive import inceptive_clause
from rajasthani.grammar.deliberative import deliberative_question, hortative_proposal
from rajasthani.grammar.voice import passive_form, medio_passive_inability
from rajasthani.grammar.syntax import (
    SyntaxEngine,
    hindi_to_rajasthani,
    explain_syntax_rules,
    build_compound_verb,
    build_complex_sentence,
    generate_causative,
    build_imperative,
    convert_clusivity,
    transform_voice,
    build_counterfactual_conditional,
    build_optative,
    build_vat_narrative,
    build_echo_word,
    intensify_adjective,
    convert_reported_speech,
    build_rhetorical_question,
    elevate_politeness,
    build_dubitative_sentence,
    connect_discourse,
    apply_ergative_construction,
)

__all__ = [
    "pluralize",
    "to_oblique",
    "decline_noun",
    "to_feminine",
    "to_masculine",
    "make_diminutive",
    "PRONOUN_TABLE",
    "get_pronoun",
    "get_possessive",
    "get_interrogative",
    "get_relative",
    "extract_root",
    "conjugate",
    "conjugate_to_be",
    "imperative",
    "conjunctive_participle",
    "passive_verb",
    "make_causative",
    "attach_case",
    "get_marker",
    "POSTPOSITIONS",
    "SPATIAL_POSTPOSITIONS",
    "agree_adjective",
    "comparative",
    "superlative",
    "get_adverb",
    "ADVERBS_CATALOG",
    "add_honorific_sa",
    "honorific_greeting",
    "negate_sentence",
    "prohibitive",
    "obligative_clause",
    "presumptive_clause",
    "inceptive_clause",
    "deliberative_question",
    "hortative_proposal",
    "passive_form",
    "medio_passive_inability",
    "SyntaxEngine",
    "hindi_to_rajasthani",
    "explain_syntax_rules",
    "build_compound_verb",
    "build_complex_sentence",
    "generate_causative",
    "build_imperative",
    "convert_clusivity",
    "transform_voice",
    "build_counterfactual_conditional",
    "build_optative",
    "build_vat_narrative",
    "build_echo_word",
    "intensify_adjective",
    "convert_reported_speech",
    "build_rhetorical_question",
    "elevate_politeness",
    "build_dubitative_sentence",
    "connect_discourse",
    "apply_ergative_construction",
]
