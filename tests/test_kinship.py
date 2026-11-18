# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani kinship resolution."""

import unittest
import rajasthani


class TestKinship(unittest.TestCase):
    def test_paternal_kinship(self):
        k = rajasthani.resolve_kinship("father")
        self.assertIsNotNone(k)
        self.assertEqual(k.rajasthani, "बापोजी")

        k_uncle = rajasthani.resolve_kinship("काको")
        self.assertIsNotNone(k_uncle)
        self.assertEqual(k_uncle.relation_key, "father_younger_brother")

    def test_maternal_kinship(self):
        k_mamo = rajasthani.resolve_kinship("मामो")
        self.assertIsNotNone(k_mamo)
        self.assertEqual(k_mamo.english, "maternal uncle")

    def test_affinal_kinship(self):
        k_byai = rajasthani.resolve_kinship("ब्याई")
        self.assertIsNotNone(k_byai)
        self.assertEqual(k_byai.hindi, "समधी")

        k_salo = rajasthani.resolve_kinship("साळो")
        self.assertIsNotNone(k_salo)
        self.assertEqual(k_salo.relation_key, "wife_brother")

    def test_list_by_category(self):
        paternal = rajasthani.list_by_category("paternal")
        self.assertTrue(len(paternal) >= 5)


if __name__ == "__main__":
    unittest.main()
