# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani voice synthesis and pronunciation."""

import unittest
import rajasthani


class TestVoice(unittest.TestCase):
    def test_ssml_generation(self):
        engine = rajasthani.get_default_voice_engine()
        ssml = engine.speak_ssml("राम राम सा")
        self.assertIn("<speak", ssml)
        self.assertIn("break", ssml)
        self.assertIn("राम राम सा", ssml)

    def test_pronunciation_guide(self):
        guide = rajasthani.pronounce("साळो")
        self.assertIn("devanagari", guide)
        self.assertIn("phonetic_roman", guide)
        self.assertTrue("retroflex" in guide["notes"])


if __name__ == "__main__":
    unittest.main()
