# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Adverbs & Spatial-Temporal Deictics
================================================================
Comprehensive catalog of Rajasthani manner, time, place, degree,
and frequentative adverbs.
"""

from typing import Dict, List, Optional

ADVERBS_CATALOG = {
    # Spatial / Place
    "here": {"rajasthani": "अठे", "roman": "athe", "hindi": "यहाँ", "type": "place"},
    "there": {"rajasthani": "वठे", "roman": "vathe", "hindi": "वहाँ", "type": "place"},
    "where": {"rajasthani": "कठे", "roman": "kathe", "hindi": "कहाँ", "type": "place"},
    "everywhere": {"rajasthani": "सगळी जगा", "roman": "saglee jaga", "hindi": "सब जगह", "type": "place"},
    "far": {"rajasthani": "आघै / दूर", "roman": "aaghai / door", "hindi": "दूर", "type": "place"},
    "near": {"rajasthani": "नेड़े / कनै", "roman": "nerai / kanai", "hindi": "पास", "type": "place"},

    # Temporal / Time
    "now": {"rajasthani": "अबार / इब", "roman": "abaar / ib", "hindi": "अब / अभी", "type": "time"},
    "then": {"rajasthani": "तद / जद", "roman": "tad / jad", "hindi": "तब", "type": "time"},
    "today": {"rajasthani": "आज", "roman": "aaj", "hindi": "आज", "type": "time"},
    "yesterday": {"rajasthani": "काल", "roman": "kaal", "hindi": "कल (बीता हुआ)", "type": "time"},
    "tomorrow": {"rajasthani": "काल", "roman": "kaal", "hindi": "कल (आने वाला)", "type": "time"},
    "day_after": {"rajasthani": "परसों", "roman": "parson", "hindi": "परसों", "type": "time"},
    "always": {"rajasthani": "हमेसा / नित", "roman": "hamesa / nit", "hindi": "हमेशा / प्रतिदिन", "type": "time"},
    "sometimes": {"rajasthani": "कदे-कदे", "roman": "kade-kade", "hindi": "कभी-कभी", "type": "time"},
    "never": {"rajasthani": "कदेई कोनी", "roman": "kadei koni", "hindi": "कभी नहीं", "type": "time"},
    "early": {"rajasthani": "सवेरै / बेगो", "roman": "saverai / bego", "hindi": "जल्दी / सुबह", "type": "time"},
    "late": {"rajasthani": "मोड़ो", "roman": "modo", "hindi": "देर से", "type": "time"},

    # Manner
    "slowly": {"rajasthani": "हळूहळू / धीमे", "roman": "halu-halu / dheeme", "hindi": "धीरे-धीरे", "type": "manner"},
    "quickly": {"rajasthani": "बेगो-बेगो / झटपट", "roman": "bego-bego / jhatpat", "hindi": "जल्दी-जल्दी", "type": "manner"},
    "well": {"rajasthani": "चोखी ढाळ / चोखी तरियां", "roman": "chokhi dhaal", "hindi": "अच्छी तरह", "type": "manner"},
    "how": {"rajasthani": "कियां / कीकर", "roman": "kiyan / keekar", "hindi": "कैसे", "type": "manner"},
    "like_this": {"rajasthani": "इयां / इसी तरियां", "roman": "iyan", "hindi": "ऐसे", "type": "manner"},

    # Degree / Quantity
    "very": {"rajasthani": "घणो / घणी / बहुत", "roman": "ghano", "hindi": "बहुत", "type": "degree"},
    "little": {"rajasthani": "थोड़ो / तनिक", "roman": "thodo", "hindi": "थोड़ा", "type": "degree"},
    "more": {"rajasthani": "ज्यादा / बत्ती", "roman": "jyada / battee", "hindi": "ज्यादा / अधिक", "type": "degree"},
    "all": {"rajasthani": "सगळो / सब", "roman": "saglo", "hindi": "सब / सम्पूर्ण", "type": "degree"},
}


def get_adverb(key: str) -> Optional[Dict[str, str]]:
    """Retrieves Rajasthani adverb metadata."""
    return ADVERBS_CATALOG.get(key)
