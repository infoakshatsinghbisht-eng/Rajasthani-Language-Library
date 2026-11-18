# -*- coding: utf-8 -*-
"""Rajasthani Lexicon Subpackage."""

from rajasthani.lexicon.dictionary import (
    Word,
    Dictionary,
    get_default_dictionary,
    lookup,
    search,
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
    "generate_noun_paradigm",
    "generate_verb_paradigm",
    "stem_word",
]
