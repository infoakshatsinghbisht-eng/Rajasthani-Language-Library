# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani numbers converter."""

import unittest
import rajasthani


class TestNumbers(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(rajasthani.num_to_words(0), "मींडो")
        self.assertEqual(rajasthani.num_to_words(1), "एक")
        self.assertEqual(rajasthani.num_to_words(10), "दस")
        self.assertEqual(rajasthani.num_to_words(16), "सोळा")
        self.assertEqual(rajasthani.num_to_words(42), "बयालीस")
        self.assertEqual(rajasthani.num_to_words(100), "सो")

    def test_large_numbers(self):
        self.assertEqual(rajasthani.num_to_words(105), "एक सो पाँच")
        self.assertEqual(rajasthani.num_to_words(1000), "एक हजार")
        self.assertEqual(rajasthani.num_to_words(100000), "एक लाख")

    def test_words_to_num(self):
        self.assertEqual(rajasthani.words_to_num("बयालीस"), 42)
        self.assertEqual(rajasthani.words_to_num("एक सो पाँच"), 105)

    def test_devanagari_numerals(self):
        self.assertEqual(rajasthani.to_devanagari_numerals(2026), "२०२६")
        self.assertEqual(rajasthani.from_devanagari_numerals("२०२६"), 2026)

    def test_ordinals(self):
        self.assertEqual(rajasthani.ordinal(1, "m"), "पहलो")
        self.assertEqual(rajasthani.ordinal(1, "f"), "पहली")
        self.assertEqual(rajasthani.ordinal(2, "m"), "दूजो")
        self.assertEqual(rajasthani.ordinal(3, "f"), "तीजी")

    def test_fractions(self):
        q = rajasthani.fraction("quarter")
        self.assertIsNotNone(q)
        self.assertEqual(q["rajasthani"], "पाव")
        self.assertEqual(rajasthani.fraction("half")["rajasthani"], "आधो")


if __name__ == "__main__":
    unittest.main()
