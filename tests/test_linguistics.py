# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani linguistics, dialectology, and POS tagging."""

import unittest
import rajasthani


class TestLinguistics(unittest.TestCase):
    def test_dialectology(self):
        mwr = rajasthani.get_dialect_features("Marwari")
        self.assertIsNotNone(mwr)
        self.assertIn("Jodhpur", mwr["region"])

        dhd = rajasthani.get_dialect_features("Dhundhari")
        self.assertIsNotNone(dhd)
        self.assertIn("छै", dhd["present_copula"])

    def test_reduplication_and_echo(self):
        self.assertEqual(rajasthani.echo_word("रोटी"), "रोटी-सोटी")
        self.assertEqual(rajasthani.echo_word("पाणी"), "पाणी-धाणी")
        self.assertEqual(rajasthani.intensive_reduplication("हळू"), "हळू-हळू")

    def test_ergativity_detection(self):
        self.assertTrue(rajasthani.is_ergative_sentence("राम नै रोटी खाई"))
        self.assertTrue(rajasthani.is_ergative_sentence("म्हैं आंबा खायो"))
        self.assertFalse(rajasthani.is_ergative_sentence("राम घर जावै है"))

    def test_bis_tagger(self):
        tags = rajasthani.tag_sentence("राम रोटी खायो।")
        self.assertTrue(len(tags) >= 3)
        tag_dict = dict(tags)
        self.assertEqual(tag_dict.get("राम"), "N_NN")
        self.assertEqual(tag_dict.get("रोटी"), "N_NN")


if __name__ == "__main__":
    unittest.main()
