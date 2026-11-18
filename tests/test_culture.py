# -*- coding: utf-8 -*-
"""Unit tests for Rajasthani cultural heritage encyclopedia."""

import unittest
import rajasthani


class TestCulture(unittest.TestCase):
    def test_architecture(self):
        arch = rajasthani.get_architecture_elements()
        self.assertTrue(len(arch) >= 5)
        names = [a.name for a in arch]
        self.assertTrue(any("हवेली" in n for n in names))
        self.assertTrue(any("झरोखो" in n for n in names))

    def test_attire(self):
        att = rajasthani.get_attire_items()
        self.assertTrue(len(att) >= 4)
        names = [a.name for a in att]
        self.assertTrue(any("साफो" in n for n in names))

    def test_music_and_dances(self):
        instruments = rajasthani.get_instruments()
        self.assertTrue(len(instruments) >= 4)
        dances = rajasthani.get_dances()
        self.assertTrue(len(dances) >= 4)
        dance_names = [d.name for d in dances]
        self.assertTrue(any("घूमर" in n for n in dance_names))
        self.assertTrue(any("कालबेलिया" in n for n in dance_names))

    def test_cuisine(self):
        dishes = rajasthani.get_cuisine_dishes()
        self.assertTrue(len(dishes) >= 5)
        dish_names = [d.name for d in dishes]
        self.assertTrue(any("दाल बाटी" in n for n in dish_names))
        self.assertTrue(any("केर सांगरी" in n for n in dish_names))

    def test_folk_deities(self):
        deities = rajasthani.get_folk_deities()
        self.assertTrue(len(deities) >= 5)
        d_names = [d.name for d in deities]
        self.assertTrue(any("रामदेवजी" in n for n in d_names))
        self.assertTrue(any("पाबूजी" in n for n in d_names))

    def test_places(self):
        places = rajasthani.get_heritage_places()
        self.assertTrue(len(places) >= 5)
        p_names = [p.name for p in places]
        self.assertTrue(any("मेहरानगढ़" in n for n in p_names))
        self.assertTrue(any("चित्तौड़गढ़" in n for n in p_names))

    def test_literature(self):
        lit = rajasthani.get_literary_figures()
        self.assertTrue(len(lit) >= 4)
        l_names = [l.name for l in lit]
        self.assertTrue(any("मीराबाई" in n for n in l_names))
        self.assertTrue(any("कन्हैयालाल सेठिया" in n for n in l_names))

    def test_rituals(self):
        rituals = rajasthani.get_all_rituals()
        self.assertTrue(len(rituals) >= 20)
        r_names = [r.name for r in rituals]
        self.assertTrue(any("माहेरो" in n for n in r_names))
        self.assertTrue(any("जड़ूलो" in n for n in r_names))
        self.assertTrue(any("गणगौर" in n for n in r_names))

        wed_rituals = rajasthani.get_rituals_by_category("wedding")
        self.assertTrue(len(wed_rituals) >= 10)

    def test_ornaments(self):
        ornaments = rajasthani.get_all_ornaments()
        self.assertTrue(len(ornaments) >= 25)
        o_names = [o.name for o in ornaments]
        self.assertTrue(any("रखड़ी" in n for n in o_names))
        self.assertTrue(any("तिमणियो" in n for n in o_names))
        self.assertTrue(any("शीशफूल" in n for n in o_names))
        self.assertTrue(any("आड़" in n for n in o_names))
        self.assertTrue(any("मुरकी" in n for n in o_names))

        foot_ornaments = rajasthani.get_ornaments_by_body_part("foot")
        self.assertTrue(len(foot_ornaments) >= 5)


if __name__ == "__main__":
    unittest.main()
