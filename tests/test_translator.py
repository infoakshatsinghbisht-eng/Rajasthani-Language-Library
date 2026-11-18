# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani translation engine."""

import unittest
import rajasthani


class TestTranslator(unittest.TestCase):
    def test_phrasebook_translation(self):
        res = rajasthani.translate("How are you?")
        self.assertEqual(res.text, "थें कियां हो सा?")
        self.assertTrue(len(res.romanized) > 0)

    def test_hindi_translation(self):
        res = rajasthani.translate("आप कैसे हैं?")
        self.assertEqual(res.text, "थें कियां हो सा?")

        res2 = rajasthani.translate("यह बहुत अच्छा है")
        self.assertEqual(res2.text, "यो घणो चोखो है")

    def test_dialect_translation(self):
        # Marwari vs Dhundhari
        res_mwr = rajasthani.translate("he was there", dialect=rajasthani.Dialect.MARWARI)
        self.assertIn("थो", res_mwr.text)

        res_dhd = rajasthani.translate("he was there", dialect=rajasthani.Dialect.DHUNDHARI)
        self.assertIn("छो", res_dhd.text)

    def test_world_language_pivot(self):
        # Spanish: 'hola' -> 'खम्मा घणी सा'
        res_es = rajasthani.translate("hola")
        self.assertEqual(res_es.text, "खम्मा घणी सा")

        # French: 'merci' -> 'आपरी घणी मेहरबानी सा'
        res_fr = rajasthani.translate("merci")
        self.assertEqual(res_fr.text, "आपरी घणी मेहरबानी सा")

        # German: 'danke'
        res_de = rajasthani.translate("danke")
        self.assertEqual(res_de.text, "आपरी घणी मेहरबानी सा")


if __name__ == "__main__":
    unittest.main()
