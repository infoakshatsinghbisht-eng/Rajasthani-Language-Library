# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Lexicon & Dictionary Engine
========================================================
Comprehensive multi-directional dictionary interface for Rajasthani,
indexing words, parts of speech, categories, colloquial phrases,
proverbs (कहावतें), and riddles (पहेलियाँ).
"""

import os
import json
import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from rajasthani.phonetics import normalize_devanagari


@dataclass
class Word:
    rajasthani: str
    roman: str
    english: str
    hindi: str
    pos: str
    category: str = "general"
    dialect: str = "general"
    example: str = ""
    synonyms: List[str] = field(default_factory=list)


class Dictionary:
    """
    Main dictionary interface for the Rajasthani language.
    """

    def __init__(self, data_dir: Optional[str] = None):
        if data_dir is None:
            data_dir = os.path.join(os.path.dirname(__file__), "data")
        self.data_dir = data_dir

        self.words: List[Word] = []
        self._raj_index: Dict[str, Word] = {}
        self._roman_index: Dict[str, Word] = {}
        self._english_index: Dict[str, List[Word]] = {}
        self._hindi_index: Dict[str, List[Word]] = {}

        self.phrases: List[Dict[str, str]] = []
        self.proverbs: List[Dict[str, str]] = []
        self.riddles: List[Dict[str, str]] = []

        self._load_data()

    def _load_data(self):
        """Loads words, phrases, proverbs, and riddles from JSON datasets."""
        # 1. Words
        words_path = os.path.join(self.data_dir, "words.json")
        if os.path.exists(words_path):
            with open(words_path, "r", encoding="utf-8") as f:
                raw_words = json.load(f)
                for item in raw_words:
                    w = Word(
                        rajasthani=item.get("rajasthani", ""),
                        roman=item.get("roman", ""),
                        english=item.get("english", ""),
                        hindi=item.get("hindi", ""),
                        pos=item.get("pos", "noun"),
                        category=item.get("category", "general"),
                        dialect=item.get("dialect", "general"),
                        example=item.get("example", ""),
                        synonyms=item.get("synonyms", []),
                    )
                    self.words.append(w)
                    norm_raj = normalize_devanagari(w.rajasthani)
                    self._raj_index[norm_raj] = w
                    self._roman_index[w.roman.lower()] = w

                    # Index English terms
                    for en in w.english.lower().split("/"):
                        en_clean = en.strip()
                        self._english_index.setdefault(en_clean, []).append(w)

                    # Index Hindi terms
                    for hi in w.hindi.split("/"):
                        hi_clean = hi.strip()
                        self._hindi_index.setdefault(hi_clean, []).append(w)

        # 2. Phrases
        phrases_path = os.path.join(self.data_dir, "phrases.json")
        if os.path.exists(phrases_path):
            with open(phrases_path, "r", encoding="utf-8") as f:
                self.phrases = json.load(f)

        # 3. Proverbs
        proverbs_path = os.path.join(self.data_dir, "proverbs.json")
        if os.path.exists(proverbs_path):
            with open(proverbs_path, "r", encoding="utf-8") as f:
                self.proverbs = json.load(f)

        # 4. Riddles
        riddles_path = os.path.join(self.data_dir, "riddles.json")
        if os.path.exists(riddles_path):
            with open(riddles_path, "r", encoding="utf-8") as f:
                self.riddles = json.load(f)

    def lookup(self, word: str, exact: bool = False) -> Optional[Word]:
        """
        Looks up a word by exact Devanagari, romanized form, Hindi, or English lemma.
        If exact is True, disables fuzzy substring fallback.
        """
        clean = word.strip()
        norm = normalize_devanagari(clean)
        if norm in self._raj_index:
            return self._raj_index[norm]

        lowered = clean.lower()
        if lowered in self._roman_index:
            return self._roman_index[lowered]

        if lowered in self._english_index and self._english_index[lowered]:
            return self._english_index[lowered][0]

        if clean in self._hindi_index and self._hindi_index[clean]:
            return self._hindi_index[clean][0]

        if exact:
            return None

        # Fuzzy substring match
        for w in self.words:
            if clean in w.rajasthani or lowered in w.roman.lower() or lowered in w.english.lower() or clean in w.hindi:
                return w

        return None

    def search(self, query: str, limit: int = 20) -> List[Word]:
        """
        Fuzzy multi-field search across Rajasthani, Roman, English, and Hindi.
        """
        clean = query.strip().lower()
        results = []
        for w in self.words:
            if (
                clean in w.rajasthani
                or clean in w.roman.lower()
                or clean in w.english.lower()
                or clean in w.hindi
                or any(clean in syn.lower() for syn in w.synonyms)
            ):
                results.append(w)
                if len(results) >= limit:
                    break
        return results

    def get_by_category(self, category: str) -> List[Word]:
        """Returns words belonging to a specific cultural or semantic category."""
        cat = category.strip().lower()
        return [w for w in self.words if w.category.lower() == cat]

    def get_all_words(self) -> List[Word]:
        """Returns all cataloged words in the dictionary."""
        return list(self.words)

    def get_by_pos(self, pos: str) -> List[Word]:
        """Returns words belonging to a grammatical Part of Speech."""
        p = pos.strip().lower()
        return [w for w in self.words if w.pos.lower() == p]

    def get_phrases(self, category: Optional[str] = None) -> List[Dict[str, str]]:
        """Returns conversational phrases, optionally filtered by category."""
        if category:
            cat = category.strip().lower()
            return [p for p in self.phrases if p.get("category", "").lower() == cat]
        return list(self.phrases)

    def get_proverbs(self) -> List[Dict[str, str]]:
        """Returns all traditional Rajasthani proverbs (कहावतें)."""
        return list(self.proverbs)

    def get_riddles(self) -> List[Dict[str, str]]:
        """Returns traditional Rajasthani riddles (पहेलियाँ)."""
        return list(self.riddles)

    def random_word(self) -> Optional[Word]:
        """Returns a random word from the lexicon."""
        return random.choice(self.words) if self.words else None

    def random_proverb(self) -> Optional[Dict[str, str]]:
        """Returns a random Rajasthani proverb."""
        return random.choice(self.proverbs) if self.proverbs else None

    def random_riddle(self) -> Optional[Dict[str, str]]:
        """Returns a random Rajasthani riddle."""
        return random.choice(self.riddles) if self.riddles else None


# Module-level default singleton
_DEFAULT_DICT: Optional[Dictionary] = None


def get_default_dictionary() -> Dictionary:
    """Returns the singleton instance of the Rajasthani dictionary."""
    global _DEFAULT_DICT
    if _DEFAULT_DICT is None:
        _DEFAULT_DICT = Dictionary()
    return _DEFAULT_DICT


def lookup(word: str) -> Optional[Word]:
    """Convenience function: look up a word in the default dictionary."""
    return get_default_dictionary().lookup(word)


def search(query: str, limit: int = 20) -> List[Word]:
    """Convenience function: search words in the default dictionary."""
    return get_default_dictionary().search(query, limit)
