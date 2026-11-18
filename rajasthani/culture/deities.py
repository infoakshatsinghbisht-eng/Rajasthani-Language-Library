# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Folk Deities & Lok Devtas (लोक देवता अर देवियां)
=============================================================================
Documentation of Rajasthan's venerated folk deities: The Panch Peer
(Ramdevji, Pabuji, Gogaji, Mehaji, Harbhuji), Veer Tejaji, Karni Mata,
Khatushyamji, Shrinathji, Jeen Mata, and Tanot Mata.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class FolkDeity:
    name: str
    roman: str
    type: str  # lok_devta, lok_devi, vaishnava_swaroop
    main_shrine: str
    symbol_or_vehicle: str
    legend: str
    fair_or_festival: str


DEITIES_DATABASE: List[FolkDeity] = [
    FolkDeity(
        name="बाबा रामदेवजी (Baba Ramdevji)",
        roman="Baba Ramdevji",
        type="lok_devta",
        main_shrine="रामदेवरा (रुणेचा, Jaisalmer)",
        symbol_or_vehicle="नीला घोड़ा अर पगलिया (Footprints)",
        legend="14th-century Tanwar Rajput prince and avatar of Krishna who fought caste discrimination and founded the egalitarian Kamadiya panth.",
        fair_or_festival="भादवा मेला (Bhadrapad Shukla Dwitiya to Ekadashi)",
    ),
    FolkDeity(
        name="पाबूजी राठौड़ (Pabuji Rathore)",
        roman="Pabuji Rathore",
        type="lok_devta",
        main_shrine="कोलू मंड (Phalodi / Jodhpur)",
        symbol_or_vehicle="केसर कालमी घोड़ी (Black mare) अर भाला",
        legend="Revered as protector of cattle and camels, incarnation of Lakshmana who sacrificed his wedding to protect cows.",
        fair_or_festival="चैत्र अमावस्या मेला",
    ),
    FolkDeity(
        name="गोगाजी (Gogaji / Jaharveer)",
        roman="Gogaji",
        type="lok_devta",
        main_shrine="गोगामेड़ी (Hanumangarh) अर ददरेवा (Churu)",
        symbol_or_vehicle="नीली घोड़ी अर सर्प (Snake deity)",
        legend="Chauhan warrior prince and supreme protector against serpent bites and poisonous hazards, revered by Hindus and Muslims alike.",
        fair_or_festival="गोगा नवमी (Bhadrapad Krishna Navami)",
    ),
    FolkDeity(
        name="वीर तेजाजी (Veer Tejaji)",
        roman="Tejaji",
        type="lok_devta",
        main_shrine="परबतसर (Nagaur) अर खरनाल (Nagaur)",
        symbol_or_vehicle="लीलण घोड़ी अर जीभ पर सर्प दंश",
        legend="Noble Jat warrior who honored his word given to a venomous serpent and gave his life defending Lachha Gujari's cattle.",
        fair_or_festival="तेजा दशमी (Bhadrapad Shukla Dashami) - Massive Cattle Fair",
    ),
    FolkDeity(
        name="करणी माता (Karni Mata)",
        roman="Karni Mata",
        type="lok_devi",
        main_shrine="देशनोक (Bikaner)",
        symbol_or_vehicle="सफेद चील अर काबा (Sacred white rats)",
        legend="15th-century Charan mystic and kuldevi of Bikaner rulers who laid the foundation stone of Mehrangarh and Bikaner forts.",
        fair_or_festival="नवरात्र मेला (Chaitra and Ashwin)",
    ),
    FolkDeity(
        name="खाटूश्यामजी (Khatushyamji)",
        roman="Khatushyamji",
        type="vaishnava_swaroop",
        main_shrine="खाटू धाम (Sikar)",
        symbol_or_vehicle="नीले घोड़े के सवार / शीश के दानी",
        legend="Barbarika, grandson of Bhima, who sacrificed his head before the Mahabharata war upon Krishna's request.",
        fair_or_festival="फाल्गुन लक्खी मेला (Phalgun Shukla Dashami to Dwadashi)",
    ),
    FolkDeity(
        name="श्रीनाथजी (Shrinathji)",
        roman="Shrinathji",
        type="vaishnava_swaroop",
        main_shrine="नाथद्वारा (Rajsamand)",
        symbol_or_vehicle="गोवर्धन पर्वत उठाए हुए बालकृष्ण",
        legend="Central deity of the Pushtimarg Vaishnava tradition brought from Govardhan to Mewar under Maharana Raj Singh.",
        fair_or_festival="अन्नकूट महोत्सव (Kartik Shukla Pratipada)",
    ),
    FolkDeity(
        name="तणोट माता (Tanot Mata)",
        roman="Tanot Mata",
        type="lok_devi",
        main_shrine="तणोट (Jaisalmer Indo-Pak Border)",
        symbol_or_vehicle="हिंगलाज माता का स्वरूप",
        legend="Miraculous goddess protecting Indian soldiers during the 1965 and 1971 wars where falling enemy artillery shells failed to explode.",
        fair_or_festival="नवरात्र मेला (Ashwin and Chaitra)",
    ),
]


def get_folk_deities() -> List[FolkDeity]:
    """Returns all cataloged Rajasthani folk deities."""
    return list(DEITIES_DATABASE)
