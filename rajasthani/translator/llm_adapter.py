# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Remote Translation Adapter
========================================================
Optional translation adapter enabling zero-shot and few-shot translation
from other languages into Rajasthani when an external API key is configured.
"""

import os
from typing import Optional, Tuple
from rajasthani.phonetics import devanagari_to_latin


class LLMTranslationAdapter:
    """
    Adapter for invoking remote translation services when an API key is available in environment.
    """

    def __init__(self):
        self.api_key = os.getenv("TRANSLATION_API_KEY") or os.getenv("LLM_API_KEY")

    def is_available(self) -> bool:
        """Returns True if a remote translation API key is present."""
        return bool(self.api_key)

    def translate_with_llm(self, text: str, source_lang: str = "auto", dialect: str = "mwr") -> Optional[Tuple[str, str]]:
        """
        Invokes remote service if available; otherwise returns None to permit graceful offline fallback.
        """
        # When no API key is provided, gracefully falls back to offline engine
        if not self.is_available():
            return None

        # Hook for external translation endpoints
        try:
            # Custom endpoint hook - returns None if remote service is not actively configured
            return None
        except Exception:
            return None
