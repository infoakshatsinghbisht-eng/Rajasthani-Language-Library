# -*- coding: utf-8 -*-
"""Comprehensive translation benchmark tests for Rajasthani."""

import unittest
import rajasthani


class TestTranslationBenchmark(unittest.TestCase):
    BENCHMARK_CASES = [
        # Greetings & Welcoming
        ("Hello", "खम्मा घणी सा"),
        ("How are you?", "थें कियां हो सा?"),
        ("What is your name?", "आपरो कांई नांव है सा?"),
        ("Welcome", "पधारो सा"),
        ("Thank you very much", "आपरी घणी मेहरबानी सा"),
        ("Good morning", "राम राम सा"),
        ("I love you", "म्हूँ थानै घणो चाहूँ हूँ"),
        ("Where are you going?", "थें कठे जा रह्या हो सा?"),
        ("I am going home", "म्हूँ घर जा रह्यो हूँ"),
        ("I am fine", "म्हूँ बिल्कुल चोखो हूँ सा"),
        ("Please eat food", "जीमो सा / भोजन करो"),
        ("Drink water", "पाणी पियो सा"),
        ("What happened?", "कांई बात हुई?"),
        ("Don't worry", "चिंता मती करो"),
        ("It is raining", "मेघ बरस रह्या हैं"),
        # Hindi inputs
        ("आप कैसे हैं?", "थें कियां हो सा?"),
        ("तुम्हारा नाम क्या है", "थारो कांई नांव है?"),
        ("स्वागत है", "पधारो सा"),
        ("धन्यवाद", "आपरी घणी मेहरबानी सा"),
        ("मैं ठीक हूँ", "म्हूँ बिल्कुल चोखो हूँ सा"),
        ("कहाँ जा रहे हो", "कठे जा रह्या हो?"),
        ("मैं घर जा रहा हूँ", "म्हूँ घर जा रह्यो हूँ"),
        ("खाना खाओ", "जीमो सा / खाणो खावो"),
        ("पानी पियो", "पाणी पियो सा"),
        ("यह बहुत अच्छा है", "यो घणो चोखो है"),
        # World languages (via Pivot)
        ("hola", "खम्मा घणी सा"),
        ("bonjour", "खम्मा घणी सा"),
        ("merci", "आपरी घणी मेहरबानी सा"),
        ("danke", "आपरी घणी मेहरबानी सा"),
    ]

    def test_benchmark_suite(self):
        passed = 0
        for src, expected in self.BENCHMARK_CASES:
            res = rajasthani.translate(src)
            self.assertEqual(res.text, expected, f"Failed translating '{src}'")
            passed += 1
        self.assertEqual(passed, len(self.BENCHMARK_CASES))


if __name__ == "__main__":
    unittest.main()
