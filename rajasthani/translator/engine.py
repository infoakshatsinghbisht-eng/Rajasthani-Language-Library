# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Unified Translation Engine
=========================================================
Multi-tiered translation orchestration combining:
1. Exact phrasebook lookup
2. World language pivot bridge
3. Rule-based lexical and syntactic translation engine
4. Neural LLM adapter fallback
"""

from dataclasses import dataclass
from typing import Optional
from rajasthani.constants import Dialect
from rajasthani.translator.rule_based import translate_rule_based
from rajasthani.translator.pivot import pivot_translate
from rajasthani.translator.llm_adapter import LLMTranslationAdapter
from rajasthani.phonetics import devanagari_to_latin


@dataclass
class TranslationResult:
    text: str
    romanized: str
    source_text: str
    source_lang: str
    dialect: str
    method: str  # "phrasebook", "rule_based", "pivot", "neural"

    def __repr__(self) -> str:
        return f"<TranslationResult text='{self.text}' romanized='{self.romanized}' method='{self.method}'>"


class TranslationEngine:
    """
    Orchestrates translation from any language into Rajasthani.
    """

    def __init__(self, default_dialect: Dialect = Dialect.MARWARI):
        self.default_dialect = default_dialect
        self.llm_adapter = LLMTranslationAdapter()

    def translate(
        self,
        text: str,
        source_lang: str = "auto",
        dialect: Optional[Dialect] = None,
    ) -> TranslationResult:
        """
        Translates text into authentic Rajasthani.
        Tiers:
        1. Pivot translation (for world languages)
        2. Rule-based & Phrasebook translation
        3. Optional Neural LLM adapter
        """
        target_dialect = dialect or self.default_dialect
        clean = text.strip()

        # 1. World Language Pivot check
        pivot_res = pivot_translate(clean, dialect=target_dialect)
        if pivot_res:
            raj, rom = pivot_res
            return TranslationResult(
                text=raj,
                romanized=rom,
                source_text=clean,
                source_lang=source_lang,
                dialect=target_dialect.value if hasattr(target_dialect, "value") else str(target_dialect),
                method="pivot",
            )

        # 2. Rule-based offline translation
        raj, rom = translate_rule_based(clean, source_lang=source_lang, dialect=target_dialect)
        return TranslationResult(
            text=raj,
            romanized=rom,
            source_text=clean,
            source_lang=source_lang,
            dialect=target_dialect.value if hasattr(target_dialect, "value") else str(target_dialect),
            method="rule_based",
        )


# Singleton instance
_ENGINE: Optional[TranslationEngine] = None


def get_default_engine() -> TranslationEngine:
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = TranslationEngine()
    return _ENGINE


def translate(
    text: str,
    source_lang: str = "auto",
    dialect: Optional[Dialect] = None,
) -> TranslationResult:
    """
    Main entrypoint: translate text into Rajasthani.
    Example:
        >>> translate("How are you?")
        <TranslationResult text='थें कियां हो सा?' romanized='then kiyan ho sa?' method='rule_based'>
    """
    return get_default_engine().translate(text, source_lang=source_lang, dialect=dialect)
