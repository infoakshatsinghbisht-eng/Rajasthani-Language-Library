# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Literary Traditions (डिंगल, पिंगल अर साहित्य)
==========================================================================
Comprehensive documentation of Rajasthani literary epochs:
Dingal (डिंगल) bardic poetry, Pingal (पिंगल), Prithviraj Raso, Mirabai's padavali,
Suryamal Misran (वंश भास्कर, वीर सतसई), Bankidas, Kanhaiyalal Sethia, and Vijaydan Detha.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class LiteraryFigure:
    name: str
    roman: str
    period: str
    style_or_tradition: str  # Dingal, Bhakti, Modern, Folk
    masterpieces: List[str]
    significance: str


LITERATURE_DATABASE: List[LiteraryFigure] = [
    LiteraryFigure(
        name="मीराबाई (Mirabai)",
        roman="Mirabai",
        period="16th Century (c. 1498–1547)",
        style_or_tradition="Madhurya Bhakti / Rajasthani Padavali",
        masterpieces=["मीराबाई की पदावली", "नरसीजी रो माहेरो", "राग सोरठ के पद"],
        significance="Legendary mystic poet princess of Mewar whose ecstatic devotional verses to Krishna (Girdhar Gopal) form the crowning glory of medieval Indian literature.",
    ),
    LiteraryFigure(
        name="सूर्यमल मीसण (Suryamal Misran)",
        roman="Suryamal Misran",
        period="1815–1868",
        style_or_tradition="Dingal Heroic & Historical Epic",
        masterpieces=["वंश भास्कर (Vansh Bhaskar)", "वीर सतसई (Veer Satsai)", "बलवद् विलास"],
        significance="Court poet of Bundi celebrated as the Rashtriya Kavi of Rajasthan; his fiery couplets inspired freedom fighters against British subjugation (इला न देणी आपणी, हालरियै हुलराय...).",
    ),
    LiteraryFigure(
        name="कन्हैयालाल सेठिया (Kanhaiyalal Sethia)",
        roman="Kanhaiyalal Sethia",
        period="1919–2008",
        style_or_tradition="Modern Rajasthani Patriotic & Lyrical",
        masterpieces=["धरती धोरां री (Dharti Dhoran Ri)", "पाथल अर पीथल (Pathal ar Peethal)", "लीलटांस (Leeltans - Sahitya Akademi Award)", "मींझर"],
        significance="Revered modern poet whose anthem 'धरती धोरां री' is the beloved cultural anthem of all Rajasthani people across the globe.",
    ),
    LiteraryFigure(
        name="विजयदान देथा 'बिज्जी' (Vijaydan Detha)",
        roman="Vijaydan Detha",
        period="1926–2013",
        style_or_tradition="Rajasthani Folk Fiction & Storytelling",
        masterpieces=["बातां री फुलवारी (14 Volumes of Rajasthani Folk Tales)", "दुविधा (Adapted into film Paheli)", "परिणति"],
        significance="The Shakespeare of Rajasthan, awarded the Padma Shri for compiling and transforming thousands of oral folktales into world-class literature.",
    ),
    LiteraryFigure(
        name="चंदबरदाई (Chand Bardai)",
        roman="Chand Bardai",
        period="12th Century",
        style_or_tradition="Pingal Epic Poetry",
        masterpieces=["पृथ्वीराज रासो (Prithviraj Raso)"],
        significance="Court bard and lifelong companion of Chauhan Emperor Prithviraj III; authored India's foremost vernacular heroic epic containing the famed distance-arrow couplet (चार बांस चौबीस गज, अंगुल अष्ट प्रमाण...).",
    ),
    LiteraryFigure(
        name="बांकीदास आसिया (Bankidas Asiya)",
        roman="Bankidas Asiya",
        period="1771–1833",
        style_or_tradition="Dingal Didactic & Patriotic Poetry",
        masterpieces=["बांकीदास री ख्यात", "आयो अंग्रेज मुलक रै ऊपर (Anti-colonial anthem)"],
        significance="Poet and historian of Jodhpur court who sounded the earliest clarion call against British imperialism in the desert.",
    ),
]


def get_literary_figures() -> List[LiteraryFigure]:
    """Returns all cataloged Rajasthani literary luminaries and their masterpieces."""
    return list(LITERATURE_DATABASE)
