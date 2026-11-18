# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani grammar, verb conjugation, and syntax engine."""

import unittest
import rajasthani


class TestGrammar(unittest.TestCase):
    def test_noun_pluralization(self):
        # Masculine -ओ -> -आ
        self.assertEqual(rajasthani.pluralize("घोड़ो", rajasthani.Gender.MASCULINE), "घोड़ा")
        self.assertEqual(rajasthani.pluralize("बेटो", rajasthani.Gender.MASCULINE), "बेटा")
        # Feminine -ई -> -ियां
        self.assertEqual(rajasthani.pluralize("घोड़ी", rajasthani.Gender.FEMININE), "घोड़ियां")
        self.assertEqual(rajasthani.pluralize("छोरी", rajasthani.Gender.FEMININE), "छोरियां")

    def test_noun_oblique(self):
        self.assertEqual(rajasthani.to_oblique("घोड़ो", rajasthani.Gender.MASCULINE), "घोड़ा")
        decline = rajasthani.decline_noun("घोड़ो")
        self.assertEqual(decline["ergative"], "घोड़ा नै")
        self.assertEqual(decline["ablative"], "घोड़ा सूं")
        self.assertEqual(decline["genitive_m"], "घोड़ा रो")

    def test_gender_conversion(self):
        self.assertEqual(rajasthani.to_feminine("घोड़ो"), "घोड़ी")
        self.assertEqual(rajasthani.to_feminine("छोरो"), "छोरी")
        self.assertEqual(rajasthani.to_masculine("घोड़ी"), "घोड़ो")

    def test_pronouns_and_clusivity(self):
        # 1st person singular
        p1sg = rajasthani.get_pronoun("1sg")
        self.assertEqual(p1sg["direct"], "म्हूँ")
        self.assertEqual(p1sg["genitive_m"], "म्हारो")
        # 1st person inclusive vs exclusive!
        p1_incl = rajasthani.get_pronoun("1pl_incl")
        p1_excl = rajasthani.get_pronoun("1pl_excl")
        self.assertEqual(p1_incl["direct"], "आपां")
        self.assertEqual(p1_excl["direct"], "म्हें")

    def test_verb_conjugation_present(self):
        # खाणो present
        conj_1sg = rajasthani.conjugate("खाणो", tense=rajasthani.Tense.PRESENT, person=rajasthani.Person.FIRST)
        self.assertIn("खाऊँ", conj_1sg)
        conj_3sg = rajasthani.conjugate("खाणो", tense=rajasthani.Tense.PRESENT, person=rajasthani.Person.THIRD)
        self.assertEqual(conj_3sg, "खावै है")

    def test_verb_conjugation_past(self):
        # खाणो past
        self.assertEqual(rajasthani.conjugate("खाणो", tense=rajasthani.Tense.PAST, gender=rajasthani.Gender.MASCULINE), "खायो")
        self.assertEqual(rajasthani.conjugate("खाणो", tense=rajasthani.Tense.PAST, gender=rajasthani.Gender.FEMININE), "खाई")
        # Irregular जाणो
        self.assertEqual(rajasthani.conjugate("जाणो", tense=rajasthani.Tense.PAST, gender=rajasthani.Gender.MASCULINE), "गयो")
        self.assertEqual(rajasthani.conjugate("जाणो", tense=rajasthani.Tense.PAST, gender=rajasthani.Gender.FEMININE), "गई")

    def test_verb_imperative(self):
        self.assertEqual(rajasthani.imperative("खाणो", honorific=True), "खाज्यो")
        self.assertEqual(rajasthani.imperative("आवणो", honorific=True), "आज्यो")

    def test_causatives(self):
        self.assertEqual(rajasthani.make_causative("करणो", degree=1), "करावणो")
        self.assertEqual(rajasthani.make_causative("करणो", degree=2), "करवावणो")

    def test_negation_and_prohibitive(self):
        neg = rajasthani.negate_sentence("राम खावै है")
        self.assertIn("कोनी", neg)
        prohib = rajasthani.prohibitive("जा")
        self.assertEqual(prohib, "मती जा!")

    def test_syntax_engine_and_ergativity(self):
        engine = rajasthani.SyntaxEngine(dialect=rajasthani.Dialect.MARWARI)
        # Present: nominative
        sent_pres = engine.build_sentence("राम", "खाणो", direct_object="रोटी", tense=rajasthani.Tense.PRESENT)
        self.assertEqual(sent_pres, "राम रोटी खावै है।")
        # Past: ergative with transitive verb!
        sent_past = engine.build_sentence(
            "राम", "खाणो", direct_object="रोटी",
            tense=rajasthani.Tense.PAST,
            obj_gender=rajasthani.Gender.FEMININE
        )
        self.assertEqual(sent_past, "राम नै रोटी खाई।")


if __name__ == "__main__":
    unittest.main()
