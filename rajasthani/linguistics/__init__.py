# -*- coding: utf-8 -*-
"""Rajasthani Linguistics Subpackage."""

from rajasthani.linguistics.dialectology import (
    get_dialect_features,
    list_all_dialects,
    DIALECT_COMPARISONS,
)
from rajasthani.linguistics.reduplication import (
    echo_word,
    intensive_reduplication,
)
from rajasthani.linguistics.ergativity import (
    is_ergative_sentence,
)
from rajasthani.linguistics.bis_tagger import (
    tag_sentence,
)

__all__ = [
    "get_dialect_features",
    "list_all_dialects",
    "DIALECT_COMPARISONS",
    "echo_word",
    "intensive_reduplication",
    "is_ergative_sentence",
    "tag_sentence",
]
