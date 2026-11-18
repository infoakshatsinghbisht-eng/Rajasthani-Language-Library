# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Cuisine & Culinary Heritage (खाण-पीण अर रसोई)
==========================================================================
Comprehensive catalog of royal and pastoral delicacies: Dal Baati Churma,
Ker Sangri, Gatte ki Sabzi, Ghevar, Bajre ki Roti, Rabdi, and signature sweets.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Dish:
    name: str
    roman: str
    course: str  # main_course, side_dish, dessert, beverage, bread
    description: str
    ingredients: List[str]
    origin_region: str
    cultural_context: str


CUISINE_DATABASE: List[Dish] = [
    Dish(
        name="दाल बाटी चूरमो (Dal Baati Churma)",
        roman="Dal Baati Churma",
        course="main_course",
        description="The sovereign culinary triad of Rajasthan: spiced five-lentil Panchmel Dal, wood-baked whole-wheat dough balls soaked in pure desi ghee, and sweet crumbled churma.",
        ingredients=["गेंहू का आटा", "देसी घी", "पंचमेल दाल (चना, मूंग, उड़द, मसूर, तुवर)", "गुड़ या बूरा"],
        origin_region="Mewar & statewide",
        cultural_context="Born out of medieval warfare when Rajput soldiers buried dough balls in sand under the sun before battle.",
    ),
    Dish(
        name="केर सांगरी (Ker Sangri)",
        roman="Ker Sangri",
        course="side_dish",
        description="Piquant dry desert vegetable curry prepared from tart wild caper berries (ker) and slender desert tree beans (sangri) tossed with red chillies and raisins.",
        ingredients=["केर", "सांगरी", "साबुत लाल मिर्च", "अमचूर", "राई", "तेल"],
        origin_region="Marwar (Thar Desert)",
        cultural_context="Drought-resistant lifeline wild flora preserved for years, celebrated in royal feasts and desert travels.",
    ),
    Dish(
        name="गट्टे री सब्जी (Gatte ki Sabzi)",
        roman="Gatte ki Sabzi",
        course="main_course",
        description="Steamed and fried chickpea-flour (besan) cylindric dumplings simmered in rich spiced yoghurt gravy.",
        ingredients=["बेसन", "दही", "हींग", "धनिया", "लाल मिर्च पाउडर"],
        origin_region="Statewide",
        cultural_context="Invented as a lush curry substitute during arid seasons when fresh leafy greens were unavailable.",
    ),
    Dish(
        name="घेवर (Ghevar)",
        roman="Ghevar",
        course="dessert",
        description="Perforated disc-shaped honeycomb sweet pastry made of deep-fried batter, soaked in saffron syrup, topped with rabri and pistachios.",
        ingredients=["मैदा", "घी", "दूध", "केसर", "चाशनी", "मावा/रबड़ी"],
        origin_region="Jaipur & statewide",
        cultural_context="Indispensable festive treat prepared specially for Hariyali Teej and Raksha Bandhan.",
    ),
    Dish(
        name="बाजरे रो सोगरो (Bajre ki Roti / Sogro)",
        roman="Bajre ki Roti",
        course="bread",
        description="Thick rustic unleavened flatbread hand-patted from pearl millet flour and roasted over cow-dung or firewood embers.",
        ingredients=["बाजरे का आटा", "पानी", "नमक", "देसी घी"],
        origin_region="Marwar & Shekhawati",
        cultural_context="Winter staple providing sustained endurance and thermal warmth in the desert cold.",
    ),
    Dish(
        name="मिर्ची बड़ो (Mirchi Bada)",
        roman="Mirchi Bada",
        course="snack",
        description="Large mildly spicy green Bhavnagri chilli stuffed with spiced mashed potato mixture, dipped in gram flour batter and crisp fried.",
        ingredients=["बड़ी हरी मिर्च", "आलू मसाला", "बेसन", "हींग"],
        origin_region="Jodhpur",
        cultural_context="Legendary breakfast street food of Jodhpur enjoyed with sweet tamarind chutney.",
    ),
    Dish(
        name="प्याज़ री कचौरी (Pyaaz ki Kachori)",
        roman="Pyaaz ki Kachori",
        course="snack",
        description="Flaky deep-fried puff pastry stuffed with caramelized onions and aromatic crushed whole spices.",
        ingredients=["मैदा", "प्याज़", "सौंफ", "धनिया बीज", "गरम मसाला"],
        origin_region="Jaipur & Jodhpur",
        cultural_context="Celebrated morning tea accompaniment across Rajasthan.",
    ),
    Dish(
        name="राबड़ी (Rabdi)",
        roman="Rabdi",
        course="beverage",
        description="Fermented probiotic cooling beverage prepared by simmering millet flour in sour buttermilk, left overnight in earthen pots.",
        ingredients=["बाजरा या मक्की का आटा", "खट्टी छाछ", "भुना जीरा", "सेंधा नमक"],
        origin_region="Rural desert homesteads",
        cultural_context="Natural shield against summer heatwaves (लू) in western Rajasthan.",
    ),
]


def get_cuisine_dishes() -> List[Dish]:
    """Returns all cataloged traditional Rajasthani dishes."""
    return list(CUISINE_DATABASE)
