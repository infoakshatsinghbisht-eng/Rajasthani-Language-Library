# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Speech Synthesis & Pronunciation Guide
===================================================================
Provides phonetic pronunciation rules, SSML generation, accent modulations,
and text-to-speech mapping tailored to Rajasthani phonology.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from rajasthani.phonetics import devanagari_to_latin, normalize_devanagari


@dataclass
class VoiceConfig:
    speed: float = 1.0        # Speech rate (0.5 to 1.5)
    pitch: float = 1.0        # Pitch multiplier
    dialect_accent: str = "mwr"  # mwr, mew, dhd
    honorific_pause: bool = True  # Pause after 'सा' or 'हुकुम'


class RajasthaniVoiceSynthesizer:
    """
    Synthesizes phonetic instructions and SSML for Rajasthani speech.
    """

    def __init__(self, config: Optional[VoiceConfig] = None):
        self.config = config or VoiceConfig()

    def generate_ssml(self, text: str) -> str:
        """
        Converts Rajasthani text into Speech Synthesis Markup Language (SSML)
        with authentic phrasing pauses around honorifics (सा, हुकुम).
        """
        clean = normalize_devanagari(text)

        # Insert slight prosodic pause after traditional honorifics
        if self.config.honorific_pause:
            clean = clean.replace(" सा", ' सा <break time="200ms"/>')
            clean = clean.replace(" हुकुम", ' हुकुम <break time="250ms"/>')

        rate_str = f"{int(self.config.speed * 100)}%"
        pitch_str = f"{int((self.config.pitch - 1.0) * 50)}%"

        ssml = (
            f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="hi-IN">\n'
            f'  <prosody rate="{rate_str}" pitch="{pitch_str}">\n'
            f"    {clean}\n"
            f"  </prosody>\n"
            f"</speak>"
        )
        return ssml

    def get_pronunciation_guide(self, word: str) -> Dict[str, str]:
        """
        Generates phonetic breakdown and IPA-like guidance for a Rajasthani word.
        """
        clean = normalize_devanagari(word)
        latin = devanagari_to_latin(clean)

        notes = []
        if "ळ" in clean:
            notes.append("ळ is a voiced retroflex lateral flap [ɭ], pronounced with tongue curled against the palate.")
        if "सा" in clean:
            notes.append("सा is the royal honorific particle pronounced softly with courteous inflection.")
        if "घणो" in clean or "घणी" in clean:
            notes.append("घ is a voiced aspirated velar stop [ɡʱ].")

        return {
            "devanagari": clean,
            "phonetic_roman": latin,
            "notes": " ".join(notes) if notes else "Standard Devanagari pronunciation with open vowels.",
        }
