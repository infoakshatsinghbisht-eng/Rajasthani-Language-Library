# -*- coding: utf-8 -*-
"""
Rajasthani (राजस्थानी) Language Standard Library for Python
==========================================================

A comprehensive, production-grade computational linguistics toolkit, NLP engine,
and cultural repository for the Rajasthani language (राजस्थानी भाषा).

Key Capabilities:
-----------------
1. Universal Translation Engine (World Languages -> Rajasthani)
2. Morphological Verb Conjugation & Syntax Engine (SOV, Split Ergativity)
3. Rich Lexicon, Proverbs (कहावतें), and Riddles (आडी / पहेलियाँ)
4. Comprehensive Kinship Resolution (नाता-गोता)
5. Numbers & Ordinals Converter (0 - 100,000,000+)
6. Cultural & Heritage Encyclopedia (Architecture, Music, Deities, Attire, Cuisine)
7. Phonetics & Bidirectional Romanization Engine
8. Interactive Web UI & Command Line Interface

Quick Start:
------------
>>> import rajasthani
>>> rajasthani.translate("How are you?")
<TranslationResult text='थें कियां हो सा?' romanized='then kiyan ho sa?' method='rule_based'>
>>> rajasthani.conjugate("खाणो", tense="past", gender="masculine")
'खायो'
>>> rajasthani.num_to_words(42)
'बयालीस'
>>> rajasthani.lookup("चोखो")
Word(rajasthani='चोखो', roman='chokho', english='good / fine / pleasant', hindi='अच्छा / बढ़िया', pos='adjective', category='descriptors')
"""

__version__ = "1.0.0"
__author__ = "Akshat Singh Bisht"
__email__ = "infoakshatsinghbisht@gmail.com"
__maintainer__ = "Akshat Singh Bisht"
__website__ = "https://akshatsinghbisht.com/"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2026 Akshat Singh Bisht"

# Constants & Enums
from rajasthani.constants import (
    ISO_639_1,
    ISO_639_2,
    ISO_639_3,
    ISO_639_NAME,
    NATIVE_NAME,
    DEVANAGARI_NAME,
    HISTORICAL_SCRIPT,
    Dialect,
    Script,
    PartOfSpeech,
    Gender,
    GrammaticalNumber,
    Person,
    Tense,
    Case,
    RAJASTHANI_MONTHS,
    SEASONS,
    DAYS_OF_WEEK,
    GREETINGS,
    POSTPOSITIONS_BY_DIALECT,
)

# Phonetics & Script Conversion
from rajasthani.phonetics import (
    normalize_devanagari,
    detect_script,
    devanagari_to_latin,
    latin_to_devanagari,
    tokenize,
    syllables,
)

# Numbers & Numerals
from rajasthani.numbers import (
    num_to_words,
    words_to_num,
    to_devanagari_numerals,
    from_devanagari_numerals,
    ordinal,
    fraction,
    DEV_DIGITS,
    RAJASTHANI_NUMBERS,
    FRACTIONS,
)

# Grammar & Morphology
from rajasthani.grammar import (
    pluralize,
    to_oblique,
    decline_noun,
    to_feminine,
    to_masculine,
    make_diminutive,
    PRONOUN_TABLE,
    get_pronoun,
    get_possessive,
    get_interrogative,
    get_relative,
    extract_root,
    conjugate,
    conjugate_to_be,
    imperative,
    conjunctive_participle,
    passive_verb,
    make_causative,
    attach_case,
    get_marker,
    POSTPOSITIONS,
    SPATIAL_POSTPOSITIONS,
    agree_adjective,
    comparative,
    superlative,
    get_adverb,
    ADVERBS_CATALOG,
    add_honorific_sa,
    honorific_greeting,
    negate_sentence,
    prohibitive,
    obligative_clause,
    presumptive_clause,
    inceptive_clause,
    deliberative_question,
    hortative_proposal,
    passive_form,
    medio_passive_inability,
    SyntaxEngine,
    hindi_to_rajasthani,
    explain_syntax_rules,
    build_compound_verb,
    build_complex_sentence,
)

# Lexicon & Dictionary
from rajasthani.lexicon import (
    Word,
    Dictionary,
    get_default_dictionary,
    lookup,
    search,
    get_idioms,
    get_proverbs,
    get_riddles,
    generate_noun_paradigm,
    generate_verb_paradigm,
    stem_word,
)

# Kinship System
from rajasthani.kinship import (
    KinshipTerm,
    resolve_kinship,
    get_all_kinship_terms,
    list_by_category,
    KINSHIP_DATABASE,
)

# Translation Engine
from rajasthani.translator import (
    TranslationResult,
    TranslationEngine,
    get_default_engine,
    translate,
    translate_rule_based,
    pivot_translate,
)

# Cultural Heritage
from rajasthani.culture import (
    ArchitectureElement,
    get_architecture_elements,
    lookup_architecture,
    ARCHITECTURE_DATABASE,
    AttireItem,
    get_attire_items,
    ATTIRE_DATABASE,
    FolkInstrument,
    FolkDance,
    get_instruments,
    get_dances,
    INSTRUMENTS_DATABASE,
    DANCES_DATABASE,
    Dish,
    get_cuisine_dishes,
    CUISINE_DATABASE,
    FolkDeity,
    get_folk_deities,
    DEITIES_DATABASE,
    HeritagePlace,
    get_heritage_places,
    PLACES_DATABASE,
    LiteraryFigure,
    get_literary_figures,
    LITERATURE_DATABASE,
    CulturalRitual,
    get_all_rituals,
    get_rituals_by_category,
    RITUALS_DATABASE,
    Ornament,
    get_all_ornaments,
    get_ornaments_by_body_part,
    ORNAMENTS_DATABASE,
)

# Voice & Pronunciation
from rajasthani.voice import (
    VoiceEngine,
    get_default_voice_engine,
    pronounce,
    RajasthaniVoiceSynthesizer,
    VoiceConfig,
)

# Linguistics
from rajasthani.linguistics import (
    get_dialect_features,
    list_all_dialects,
    DIALECT_COMPARISONS,
    echo_word,
    intensive_reduplication,
    is_ergative_sentence,
    tag_sentence,
)

# Web & CLI
from rajasthani.web import run_server
from rajasthani.cli import main as cli_main

__all__ = [
    # Metadata
    "__version__",
    "__author__",
    "__email__",
    "__maintainer__",
    "__website__",
    "__license__",
    # Constants
    "ISO_639_1",
    "ISO_639_2",
    "ISO_639_3",
    "ISO_639_NAME",
    "NATIVE_NAME",
    "DEVANAGARI_NAME",
    "HISTORICAL_SCRIPT",
    "Dialect",
    "Script",
    "PartOfSpeech",
    "Gender",
    "GrammaticalNumber",
    "Person",
    "Tense",
    "Case",
    "RAJASTHANI_MONTHS",
    "SEASONS",
    "DAYS_OF_WEEK",
    "GREETINGS",
    "POSTPOSITIONS_BY_DIALECT",
    # Phonetics
    "normalize_devanagari",
    "detect_script",
    "devanagari_to_latin",
    "latin_to_devanagari",
    "tokenize",
    "syllables",
    # Numbers
    "num_to_words",
    "words_to_num",
    "to_devanagari_numerals",
    "from_devanagari_numerals",
    "ordinal",
    "fraction",
    "DEV_DIGITS",
    "RAJASTHANI_NUMBERS",
    "FRACTIONS",
    # Grammar
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
    # Lexicon
    "Word",
    "Dictionary",
    "get_default_dictionary",
    "lookup",
    "search",
    "get_idioms",
    "get_proverbs",
    "get_riddles",
    "generate_noun_paradigm",
    "generate_verb_paradigm",
    "stem_word",
    # Kinship
    "KinshipTerm",
    "resolve_kinship",
    "get_all_kinship_terms",
    "list_by_category",
    "KINSHIP_DATABASE",
    # Translator
    "TranslationResult",
    "TranslationEngine",
    "get_default_engine",
    "translate",
    "translate_rule_based",
    "pivot_translate",
    # Culture
    "ArchitectureElement",
    "get_architecture_elements",
    "lookup_architecture",
    "ARCHITECTURE_DATABASE",
    "AttireItem",
    "get_attire_items",
    "ATTIRE_DATABASE",
    "FolkInstrument",
    "FolkDance",
    "get_instruments",
    "get_dances",
    "INSTRUMENTS_DATABASE",
    "DANCES_DATABASE",
    "Dish",
    "get_cuisine_dishes",
    "CUISINE_DATABASE",
    "FolkDeity",
    "get_folk_deities",
    "DEITIES_DATABASE",
    "HeritagePlace",
    "get_heritage_places",
    "PLACES_DATABASE",
    "LiteraryFigure",
    "get_literary_figures",
    "LITERATURE_DATABASE",
    "CulturalRitual",
    "get_all_rituals",
    "get_rituals_by_category",
    "RITUALS_DATABASE",
    "Ornament",
    "get_all_ornaments",
    "get_ornaments_by_body_part",
    "ORNAMENTS_DATABASE",
    # Voice
    "VoiceEngine",
    "get_default_voice_engine",
    "pronounce",
    "RajasthaniVoiceSynthesizer",
    "VoiceConfig",
    # Linguistics
    "get_dialect_features",
    "list_all_dialects",
    "DIALECT_COMPARISONS",
    "echo_word",
    "intensive_reduplication",
    "is_ergative_sentence",
    "tag_sentence",
    # Web & CLI
    "run_server",
    "cli_main",
]
