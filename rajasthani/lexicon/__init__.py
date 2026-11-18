# -*- coding: utf-8 -*-
"""Rajasthani Lexicon Subpackage."""

from rajasthani.lexicon.dictionary import (
    Word,
    Dictionary,
    get_default_dictionary,
    lookup,
    search,
    get_idioms,
    get_proverbs,
    get_riddles,
)
from rajasthani.lexicon.morphology import (
    generate_noun_paradigm,
    generate_verb_paradigm,
    stem_word,
)

__all__ = [
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
]
