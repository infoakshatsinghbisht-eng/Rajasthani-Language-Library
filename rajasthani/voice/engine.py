# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Voice Engine
==========================================
Top-level voice synthesis controller.
"""

from typing import Dict, Optional
from rajasthani.voice.synthesizer import RajasthaniVoiceSynthesizer, VoiceConfig


class VoiceEngine:
    """
    Controller for speech synthesis and audio generation.
    """

    def __init__(self, config: Optional[VoiceConfig] = None):
        self.synthesizer = RajasthaniVoiceSynthesizer(config)

    def speak_ssml(self, text: str) -> str:
        """Returns ready-to-broadcast SSML."""
        return self.synthesizer.generate_ssml(text)

    def get_pronunciation(self, text: str) -> Dict[str, str]:
        """Returns phonetic guide and romanization."""
        return self.synthesizer.get_pronunciation_guide(text)


_DEFAULT_VOICE: Optional[VoiceEngine] = None


def get_default_voice_engine() -> VoiceEngine:
    global _DEFAULT_VOICE
    if _DEFAULT_VOICE is None:
        _DEFAULT_VOICE = VoiceEngine()
    return _DEFAULT_VOICE


def pronounce(text: str) -> Dict[str, str]:
    """Convenience helper to fetch pronunciation for Rajasthani text."""
    return get_default_voice_engine().get_pronunciation(text)
