# -*- coding: utf-8 -*-
"""
Ultimate Features Verification Suite
====================================
Tests compound verbs, complex sentences, idioms, extended kinship,
and digital corpus integrity for the Rajasthani language library.
"""

import unittest
import os
import json
import rajasthani


class TestUltimateFeatures(unittest.TestCase):
    def test_compound_verbs(self):
        # 1. Completive for self: खाय लियो
        cv1 = rajasthani.build_compound_verb("खाणो", vector_verb="लेणो", tense=rajasthani.Tense.PAST)
        self.assertEqual(cv1, "खाय लियो")

        # 2. Completive for others: दे दीनो
        cv2 = rajasthani.build_compound_verb("देवणो", vector_verb="देणो", tense=rajasthani.Tense.PAST)
        self.assertEqual(cv2, "दे दीनो")

        # 3. Sudden inception: चाल पड़्यो / चाल पड़यो
        cv3 = rajasthani.build_compound_verb("चालणो", vector_verb="पड़णो", tense=rajasthani.Tense.PAST)
        self.assertIn(cv3, ["चाल पड़यो", "चाल पड़्यो"])

        # 4. Feminine past agreement: खाय लीनी
        cv4 = rajasthani.build_compound_verb(
            "खाणो",
            vector_verb="लेणो",
            tense=rajasthani.Tense.PAST,
            gender=rajasthani.Gender.FEMININE,
        )
        self.assertEqual(cv4, "खाय लीनी")

    def test_complex_correlative_sentences(self):
        # Conditional: जे... तो
        sent_cond = rajasthani.build_complex_sentence("मेह बरस्यो", "फसल चोखी व्हैला", connector_type="conditional")
        self.assertEqual(sent_cond, "जे मेह बरस्यो, तो फसल चोखी व्हैला।")

        # Temporal: जद... तद
        sent_temp = rajasthani.build_complex_sentence("सूरज ऊग्यो", "अंधेरो मिट ग्यो", connector_type="temporal")
        self.assertEqual(sent_temp, "जद सूरज ऊग्यो, तद अंधेरो मिट ग्यो।")

        # Relative: जको... वो
        sent_rel = rajasthani.build_complex_sentence("मेहनत करै है", "सुखी रह्वै है", connector_type="relative")
        self.assertEqual(sent_rel, "जको मेहनत करै है, वो सुखी रह्वै है।")

    def test_idioms_catalog(self):
        idioms = rajasthani.get_idioms()
        self.assertTrue(len(idioms) >= 15)
        raj_phrases = [i["rajasthani"] for i in idioms]
        self.assertTrue(any("पगड़ी" in p for p in raj_phrases))
        self.assertTrue(any("खांडे री धार" in p for p in raj_phrases))
        self.assertTrue(any("केसरिया बाना" in p for p in raj_phrases))
        self.assertTrue(any("हाथ पीळा" in p for p in raj_phrases))

    def test_extended_kinship(self):
        sadhoo = rajasthani.resolve_kinship("साढू")
        self.assertIsNotNone(sadhoo)
        self.assertIn(sadhoo.relation_key, ["wife_sister_husband", "co_brother_in_law"])

        nandoi = rajasthani.resolve_kinship("नणदोई")
        self.assertIsNotNone(nandoi)
        self.assertEqual(nandoi.relation_key, "husband_sister_husband")

        bhaanjo = rajasthani.resolve_kinship("भाणजो")
        self.assertIsNotNone(bhaanjo)
        self.assertEqual(bhaanjo.relation_key, "sister_son")

        dharam_bhai = rajasthani.resolve_kinship("धरम-भाई")
        self.assertIsNotNone(dharam_bhai)
        self.assertEqual(dharam_bhai.relation_key, "sworn_brother")

    def test_corpus_catalog(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cat_file = os.path.join(base_dir, "data_sources", "corpus_catalog.json")
        self.assertTrue(os.path.exists(cat_file))
        with open(cat_file, "r", encoding="utf-8") as f:
            cat = json.load(f)
        self.assertTrue(len(cat) >= 15)
        titles = [c.get("title", "") for c in cat]
        self.assertTrue(any("Veer Satsai" in t for t in titles))
        self.assertTrue(any("Vat" in t for t in titles))

    def test_split_ergative_sentence_generation(self):
        engine = rajasthani.SyntaxEngine(dialect=rajasthani.Dialect.MARWARI)
        # Transitive past: verb agrees with feminine direct object 'पोथी' -> पढ़ी
        s1 = engine.build_sentence(
            subject="राम",
            verb="पढ़णो",
            direct_object="पोथी",
            tense=rajasthani.Tense.PAST,
            obj_gender=rajasthani.Gender.FEMININE,
        )
        self.assertIn("राम नै पोथी पढ़ी।", s1)

        # Transitive past: verb agrees with masculine direct object 'आंबा' -> खायो
        s2 = engine.build_sentence(
            subject="सीता",
            verb="खाणो",
            direct_object="आंबा",
            tense=rajasthani.Tense.PAST,
            obj_gender=rajasthani.Gender.MASCULINE,
        )
        self.assertIn("सीता नै आंबा खायो।", s2)


if __name__ == "__main__":
    unittest.main()
