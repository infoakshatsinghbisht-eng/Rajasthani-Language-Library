# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Heritage Attire & Textiles (पहनावो अर वेशभूषा)
=============================================================================
Comprehensive catalog of Rajasthani traditional clothing, headgear (Pagri/Safa),
tie-dye prints (Bandhej, Leheriya, Mothra), jewelry, and festive garments.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class AttireItem:
    name: str
    roman: str
    wearer: str  # men, women, unisex
    description: str
    regional_varieties: List[str]
    cultural_significance: str


ATTIRE_DATABASE: List[AttireItem] = [
    AttireItem(
        name="साफो / पगड़ी (Safa / Pagri)",
        roman="Safa / Pagri",
        wearer="men",
        description="The quintessential Rajasthani turban measuring 9 to 18 meters wrapped in specialized knots reflecting lineage and caste.",
        regional_varieties=["जोधाणी साफो (Jodhpur)", "मेवाड़ी पाग (Udaipur)", "जयपुरिया पंचरंगी साफो (Jaipur)", "बीकानेरी पैंचा (Bikaner)"],
        cultural_significance="Supreme symbol of self-respect, honor (आण), and hospitality; never placed on the ground.",
    ),
    AttireItem(
        name="घूघरो / घाघरा (Ghagra / Chaniya)",
        roman="Ghagra",
        wearer="women",
        description="Full, flared pleated ankle-length skirt stitched with up to 80-100 vertical panels (कली) for expansive twirls in Ghoomar.",
        regional_varieties=["अस्सी कली रो घाघरो", "कालबेलिया काला घाघरा", "बजरंग घाघरा"],
        cultural_significance="Vibrant colors reflecting joyful celebration against desert monotone backgrounds.",
    ),
    AttireItem(
        name="ओढ़णी / चुनड़ी (Odhni / Chunari)",
        roman="Odhni",
        wearer="women",
        description="Graceful 2.5 meter translucent veil draped over head and shoulder, often tucked in waistband.",
        regional_varieties=["लहरिया (Monsoon zigzag pattern)", "पोमचा (Yellow/pink maternity wrap)", "मोठड़ा (Crossed bandhani)", "धनक"],
        cultural_significance="Signifies modesty, marital blessing, and festive radiance; central theme of folk poetry.",
    ),
    AttireItem(
        name="कांचळी (Kanchli)",
        roman="Kanchli",
        wearer="women",
        description="Inner fitted bodice tied at the back with colorful cords and adorned with mirror work, beads, and golden tassels.",
        regional_varieties=["मारवाड़ी कांचळी", "शेखावाटी गोटा-पत्ती कांचळी"],
        cultural_significance="Functional and cool desert topwear worn under the Kurti.",
    ),
    AttireItem(
        name="अंगरखो (Angrakho)",
        roman="Angrakho",
        wearer="men",
        description="Traditional side-fastening cotton robe fastened with fabric ties over the chest.",
        regional_varieties=["कमरी अंगरखा (short)", "जामा अंगरखा (long flared)"],
        cultural_significance="Historical warrior and court garment offering ease of sword movements and desert thermal comfort.",
    ),
    AttireItem(
        name="मोजड़ी / जूतियां (Mojari / Jutti)",
        roman="Mojari",
        wearer="unisex",
        description="Handcrafted leather footwear with upturned curled toes, stitched with silk and metallic zardozi embroidery.",
        regional_varieties=["जोधपुरी मोजड़ी", "भीनमाल री जूतियां", "जयपुरिया कसीदा मोजड़ी"],
        cultural_significance="Durable footwear designed to withstand desert sand with soft leather soles.",
    ),
]


def get_attire_items() -> List[AttireItem]:
    """Returns all cataloged traditional Rajasthani attire items."""
    return list(ATTIRE_DATABASE)
