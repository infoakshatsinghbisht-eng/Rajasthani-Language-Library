# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani lexicon and dictionary."""

import unittest
import rajasthani


class TestLexicon(unittest.TestCase):
    def setUp(self):
        self.d = rajasthani.get_default_dictionary()

    def test_lookup_exact(self):
        w = self.d.lookup("खम्मा घणी")
        self.assertIsNotNone(w)
        self.assertEqual(w.rajasthani, "खम्मा घणी")

    def test_lookup_roman(self):
        w = self.d.lookup("chokho")
        self.assertIsNotNone(w)
        self.assertEqual(w.rajasthani, "चोखो")

    def test_lookup_english(self):
        w = self.d.lookup("camel")
        self.assertIsNotNone(w)
        self.assertEqual(w.rajasthani, "ऊंट")

    def test_lookup_hindi(self):
        w = self.d.lookup("पानी")
        self.assertIsNotNone(w)
        self.assertEqual(w.rajasthani, "पाणी")

    def test_search(self):
        res = self.d.search("रोटी")
        self.assertTrue(len(res) > 0)

    def test_phrases(self):
        phrases = self.d.get_phrases()
        self.assertTrue(len(phrases) >= 20)

    def test_proverbs(self):
        proverbs = self.d.get_proverbs()
        self.assertTrue(len(proverbs) >= 20)

    def test_riddles(self):
        riddles = self.d.get_riddles()
        self.assertTrue(len(riddles) >= 25)

    def test_word_count(self):
        words = self.d.get_all_words()
        self.assertTrue(len(words) >= 1500)

    def test_morphology_paradigms(self):
        p_noun = rajasthani.generate_noun_paradigm("घोड़ो")
        self.assertIn("singular", p_noun)
        self.assertIn("plural", p_noun)
        self.assertEqual(p_noun["singular"]["ergative"], "घोड़ा नै")

        p_verb = rajasthani.generate_verb_paradigm("खाणो")
        self.assertIn("present", p_verb)
        self.assertIn("past", p_verb)


if __name__ == "__main__":
    unittest.main()
