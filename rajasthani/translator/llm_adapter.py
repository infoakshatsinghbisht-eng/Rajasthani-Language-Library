# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Neural LLM Translation Adapter
============================================================
Optional Neural AI adapter enabling zero-shot and few-shot translation
from any language in the world into Rajasthani using Google Gemini or OpenAI.
"""

import os
from typing import Optional, Tuple
from rajasthani.phonetics import devanagari_to_latin


class LLMTranslationAdapter:
    """
    Adapter for invoking neural LLMs when API keys are available in environment.
    """

    def __init__(self):
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        self.openai_key = os.getenv("OPENAI_API_KEY")

    def is_available(self) -> bool:
        """Returns True if any supported LLM API key is present."""
        return bool(self.gemini_key or self.openai_key)

    def translate_with_llm(self, text: str, source_lang: str = "auto", dialect: str = "mwr") -> Optional[Tuple[str, str]]:
        """
        Invokes LLM API if available; otherwise returns None to permit graceful fallback.
        """
        # When no API key is provided, gracefully falls back to offline engine
        if not self.is_available():
            return None

        # Implementation hooks for google.genai or openai SDKs
        try:
            if self.gemini_key:
                from google import genai
                client = genai.Client(api_key=self.gemini_key)
                prompt = (
                    f"Translate the following text into Rajasthani (dialect: {dialect}). "
                    f"Return ONLY the authentic Rajasthani Devanagari translation.\n"
                    f"Text: {text}"
                )
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                res_text = response.text.strip()
                return res_text, devanagari_to_latin(res_text)
        except Exception:
            return None

        return None
