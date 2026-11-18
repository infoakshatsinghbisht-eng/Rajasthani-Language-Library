# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani constants and enums."""

import unittest
import rajasthani


class TestConstants(unittest.TestCase):
    def test_iso_identifiers(self):
        self.assertEqual(rajasthani.ISO_639_3, "raj")
        self.assertEqual(rajasthani.NATIVE_NAME, "राजस्थानी")
        self.assertEqual(rajasthani.ISO_639_NAME, "Rajasthani")

    def test_dialects(self):
        self.assertEqual(rajasthani.Dialect.MARWARI.value, "mwr")
        self.assertEqual(rajasthani.Dialect.MEWARI.value, "mew")
        self.assertEqual(rajasthani.Dialect.DHUNDHARI.value, "dhd")
        self.assertEqual(rajasthani.Dialect.HARAUTI.value, "hoj")
        self.assertEqual(rajasthani.Dialect.SHEKHAWATI.value, "swv")

    def test_calendar_and_seasons(self):
        self.assertEqual(len(rajasthani.RAJASTHANI_MONTHS), 12)
        self.assertEqual(rajasthani.RAJASTHANI_MONTHS[0]["rajasthani"], "चैत")
        self.assertIn("unalo", rajasthani.SEASONS)
        self.assertEqual(rajasthani.SEASONS["unalo"]["rajasthani"], "उनाळो")
        self.assertEqual(len(rajasthani.DAYS_OF_WEEK), 7)

    def test_greetings(self):
        phrases = [g["phrase"] for g in rajasthani.GREETINGS]
        self.assertIn("खम्मा घणी", phrases)
        self.assertIn("राम राम सा", phrases)
        self.assertIn("पधारो म्हारे देस", phrases)


if __name__ == "__main__":
    unittest.main()
