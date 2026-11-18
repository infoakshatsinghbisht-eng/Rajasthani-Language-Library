# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Historic Forts & Heritage Landmarks (दुर्ग अर तीर्थ)
==================================================================================
Comprehensive documentation of Rajasthan's UNESCO World Heritage Hill Forts,
desert palaces, desert national parks, and sacred pilgrimage centers.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class HeritagePlace:
    name: str
    roman: str
    city_district: str
    category: str  # unesco_fort, palace, temple, lake, natural
    description: str
    historical_details: str


PLACES_DATABASE: List[HeritagePlace] = [
    HeritagePlace(
        name="मेहरानगढ़ दुर्ग (Mehrangarh Fort)",
        roman="Mehrangarh Fort",
        city_district="जोधपुर (Jodhpur)",
        category="fort",
        description="Imposing 15th-century citadel perched atop a 400-foot perpendicular sandstone cliff commanding the Sun City of Jodhpur.",
        historical_details="Built by Rao Jodha in 1459; houses the Moti Mahal, Phool Mahal, Sheesh Mahal, and Chamunda Mata temple.",
    ),
    HeritagePlace(
        name="चित्तौड़गढ़ दुर्ग (Chittorgarh Fort)",
        roman="Chittorgarh Fort",
        city_district="चित्तौड़गढ़ (Chittorgarh)",
        category="unesco_fort",
        description="Largest fort complex in India spanning 700 acres atop a 590-foot hill, supreme symbol of Rajput valor, sacrifice, and Jauhar.",
        historical_details="UNESCO World Heritage site; features the 9-story Vijay Stambh (Tower of Victory), Kirti Stambh, and Padmini Palace.",
    ),
    HeritagePlace(
        name="कुंभलगढ़ दुर्ग (Kumbhalgarh Fort)",
        roman="Kumbhalgarh Fort",
        city_district="राजसमंद (Rajsamand)",
        category="unesco_fort",
        description="Mewar bastion nestled in the Aravalli hills featuring the second-longest continuous defensive wall in the world (36 kilometers).",
        historical_details="Built by Maharana Kumbha in the 15th century; birthplace of Maharana Pratap; houses the Badal Mahal palace.",
    ),
    HeritagePlace(
        name="सोनार किला / जैसलमेर दुर्ग (Jaisalmer Golden Fort)",
        roman="Jaisalmer Golden Fort",
        city_district="जैसलमेर (Jaisalmer)",
        category="unesco_fort",
        description="Living golden-yellow sandstone fort rising directly from the Thar sand dunes like a desert mirage.",
        historical_details="Built in 1156 by Rawal Jaisal; home to a thriving civilian community, 7 historic Jain temples, and Laxminath shrine.",
    ),
    HeritagePlace(
        name="आमेर दुर्ग (Amer Fort)",
        roman="Amer Fort",
        city_district="जयपुर (Jaipur)",
        category="unesco_fort",
        description="Magnificent hilltop palace-fortress blending Rajput and Mughal architecture overlooking Maota Lake.",
        historical_details="Constructed by Raja Man Singh I; world-renowned for its Sheesh Mahal (Mirror Palace) reflecting single candle flames.",
    ),
    HeritagePlace(
        name="जूनागढ़ दुर्ग (Junagarh Fort)",
        roman="Junagarh Fort",
        city_district="बीकानेर (Bikaner)",
        category="fort",
        description="Unconquered desert plains fortress constructed with brilliant red sandstone and Italian marble.",
        historical_details="Built by Raja Rai Singh between 1589 and 1594; features Anup Mahal, Karan Mahal, and Badal Mahal.",
    ),
    HeritagePlace(
        name="पुष्कर तीर्थ (Pushkar Sacred Lake)",
        roman="Pushkar",
        city_district="अजमेर (Ajmer)",
        category="temple",
        description="One of the holiest pilgrimage lakes surrounded by 52 bathing ghats and the world's most prominent shrine dedicated to Lord Brahma.",
        historical_details="Annual Kartik Purnima fair attracts pilgrims, sadhus, and the world's largest gathering of colorfully decorated camels.",
    ),
    HeritagePlace(
        name="हवामहल (Hawa Mahal)",
        roman="Hawa Mahal",
        city_district="जयपुर (Jaipur)",
        category="palace",
        description="Five-story pink and red sandstone 'Palace of Winds' shaped like Lord Krishna's crown with 953 micro-carved casements (jharokhas).",
        historical_details="Built by Maharaja Sawai Pratap Singh in 1799; engineered to channel refreshing mountain winds across royal zenana chambers.",
    ),
]


def get_heritage_places() -> List[HeritagePlace]:
    """Returns all cataloged historic landmarks and UNESCO sites."""
    return list(PLACES_DATABASE)
