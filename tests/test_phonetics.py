# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani phonetics and transliteration."""

import unittest
import rajasthani


class TestPhonetics(unittest.TestCase):
    def test_normalize_devanagari(self):
        text = "राजस्थानी \u200c भाषा"
        norm = rajasthani.normalize_devanagari(text)
        self.assertEqual(norm, "राजस्थानी भाषा")

    def test_detect_script(self):
        self.assertEqual(rajasthani.detect_script("खम्मा घणी"), rajasthani.Script.DEVANAGARI)
        self.assertEqual(rajasthani.detect_script("Khamma Ghani"), rajasthani.Script.LATIN)

    def test_devanagari_to_latin(self):
        lat = rajasthani.devanagari_to_latin("राजस्थानी")
        self.assertTrue(lat.startswith("raaj"))
        lat2 = rajasthani.devanagari_to_latin("चोखो")
        self.assertIn("chokho", lat2.lower())

    def test_latin_to_devanagari(self):
        dev = rajasthani.latin_to_devanagari("khamma ghani")
        self.assertEqual(dev, "खम्मा घणी")
        dev2 = rajasthani.latin_to_devanagari("padharo mhare des")
        self.assertEqual(dev2, "पधारो म्हारे देस")

    def test_tokenize(self):
        tokens = rajasthani.tokenize("पधारो म्हारे देस!")
        self.assertIn("पधारो", tokens)
        self.assertIn("देस", tokens)
        self.assertIn("!", tokens)

    def test_syllables(self):
        syls = rajasthani.syllables("राजस्थानी")
        self.assertTrue(len(syls) >= 3)


if __name__ == "__main__":
    unittest.main()
