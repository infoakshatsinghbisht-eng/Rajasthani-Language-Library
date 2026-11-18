# -*- coding: utf-8 -*-
"""Unit tests for sentence formation rules and modal constructions in Rajasthani."""

import unittest
import rajasthani


class TestSentenceFormation(unittest.TestCase):
    def setUp(self):
        self.engine = rajasthani.SyntaxEngine(dialect=rajasthani.Dialect.MARWARI)

    def test_inceptive_construction(self):
        clause = rajasthani.inceptive_clause("टाबर", "रोव", gender=rajasthani.Gender.MASCULINE)
        self.assertEqual(clause, "टाबर रोवण लाग्यो।")

        clause_f = rajasthani.inceptive_clause("छोरी", "रोव", gender=rajasthani.Gender.FEMININE)
        self.assertEqual(clause_f, "छोरी रोवण लागी।")

    def test_obligative_construction(self):
        clause = rajasthani.obligative_clause("मनै", "जाणो")
        self.assertEqual(clause, "मनै जाणो पड़ेला।")

        clause_moral = rajasthani.obligative_clause("आपांनै", "सच बोलणो", moral=True)
        self.assertEqual(clause_moral, "आपांनै सच बोलणो चाहीजै।")

    def test_presumptive_construction(self):
        clause = rajasthani.presumptive_clause("वो", "पढ़", aspect="imperfective", gender=rajasthani.Gender.MASCULINE)
        self.assertEqual(clause, "वो पढ़तो होसी।")

    def test_deliberative_and_hortative(self):
        q = rajasthani.deliberative_question("म्हूँ", "कर")
        self.assertEqual(q, "म्हूँ के करूँ?")

        hort = rajasthani.hortative_proposal("चाल")
        self.assertEqual(hort, "चालो, चालां!")

    def test_medio_passive_inability(self):
        clause = rajasthani.medio_passive_inability("म्हासूं", "चालणो")
        self.assertEqual(clause, "म्हासूं चलिजै कोनी।")

    def test_dialect_conversion(self):
        sent_mwr = "वो गयो थो"
        sent_dhd = self.engine.convert_dialect(sent_mwr, rajasthani.Dialect.MARWARI, rajasthani.Dialect.DHUNDHARI)
        self.assertEqual(sent_dhd, "वो गयो छो")

    def test_hindi_to_rajasthani_conversion(self):
        h_sent = "मैं पानी पी रहा था"
        r_sent = rajasthani.hindi_to_rajasthani(h_sent, dialect=rajasthani.Dialect.MARWARI)
        self.assertEqual(r_sent, "म्हूँ पाणी पी रह्यो थो")

    def test_syntax_rules_explanation(self):
        rules = rajasthani.explain_syntax_rules()
        self.assertIn("canonical_word_order", rules)
        self.assertIn("split_ergativity", rules)
        self.assertIn("clusivity", rules)
        self.assertIn("dialect_contrast_matrix", rules)


if __name__ == "__main__":
    unittest.main()
