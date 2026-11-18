# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Constants and Enums
=================================================
Linguistic constants, ISO identifiers, dialects, and grammatical enumerations
for Rajasthani (राजस्थानी भाषा).
"""

from enum import Enum
from typing import Dict, List, Tuple

# ISO Identifiers
ISO_639_1 = "hi"         # Historically cataloged under Hindi macrolanguage cluster in ISO 639-1
ISO_639_2 = "raj"
ISO_639_3 = "raj"        # Macro-language code for Rajasthani
ISO_639_NAME = "Rajasthani"
NATIVE_NAME = "राजस्थानी"
DEVANAGARI_NAME = "राजस्थानी"
SCRIPT_NAME = "Devanagari"
HISTORICAL_SCRIPT = "Mahajani / Muria (महाजनी / मुरिया)"

# Dialect Sub-codes (ISO 639-3)
class Dialect(str, Enum):
    MARWARI = "mwr"       # Western Rajasthan (Jodhpur, Jaisalmer, Bikaner, Nagaur, Barmer)
    MEWARI = "mew"        # South-Central (Udaipur, Rajsamand, Chittorgarh, Bhilwara)
    DHUNDHARI = "dhd"     # East-Central / Jaipuri (Jaipur, Dausa, Tonk)
    HARAUTI = "hoj"       # South-Eastern (Kota, Bundi, Baran, Jhalawar)
    SHEKHAWATI = "swv"    # North-Central (Sikar, Jhunjhunu, Churu)
    BAGRI = "bgq"         # North-Western (Sri Ganganagar, Hanumangarh, Sirsa border)
    MEWATI = "wtm"        # North-Eastern (Alwar, Bharatpur)
    WAGDI = "wbr"         # Southern / Tribal (Dungarpur, Banswara)
    STANDARD = "mwr"      # Standard / Marwari serves as the classical literary norm

    @classmethod
    def get_display_name(cls, dialect: "Dialect") -> str:
        names = {
            cls.MARWARI: "मारवाड़ी (Marwari)",
            cls.MEWARI: "मेवाड़ी (Mewari)",
            cls.DHUNDHARI: "ढूंढाड़ी (Dhundhari / Jaipuri)",
            cls.HARAUTI: "हाड़ौती (Harauti)",
            cls.SHEKHAWATI: "शेखावाटी (Shekhawati)",
            cls.BAGRI: "बागड़ी (Bagri)",
            cls.MEWATI: "मेवाती (Mewati)",
            cls.WAGDI: "वागड़ी (Wagdi)",
        }
        return names.get(dialect, dialect.value)


class Script(str, Enum):
    DEVANAGARI = "Devanagari"
    LATIN = "Latin"
    MAHAJANI = "Mahajani"


class PartOfSpeech(str, Enum):
    NOUN = "noun"
    PRONOUN = "pronoun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    POSTPOSITION = "postposition"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"
    PARTICLE = "particle"
    NUMERAL = "numeral"
    AUXILIARY = "auxiliary"


class Gender(str, Enum):
    MASCULINE = "masculine"
    FEMININE = "feminine"
    NEUTER = "neuter"  # Trace archaisms in Dingal / Western dialects


class GrammaticalNumber(str, Enum):
    SINGULAR = "singular"
    PLURAL = "plural"


class Person(str, Enum):
    FIRST = "first"       # म्हूँ / म्हें / आपां
    SECOND = "second"     # थूँ / थें / आप
    THIRD = "third"       # ओ / वो / या / बा


class Tense(str, Enum):
    PRESENT = "present"
    PAST = "past"
    FUTURE = "future"
    CONTINUOUS = "continuous"
    PAST_CONTINUOUS = "past_continuous"
    HABITUAL_PAST = "habitual_past"
    PRESUMPTIVE = "presumptive"
    IMPERATIVE = "imperative"
    SUBJUNCTIVE = "subjunctive"
    OBLIGATIVE = "obligative"
    PERFECT = "perfect"


class Case(str, Enum):
    DIRECT = "direct"
    OBLIQUE = "oblique"
    ERGATIVE = "ergative"               # नै (ने)
    ACCUSATIVE_DATIVE = "dative"        # नै (ने)
    INSTRUMENTAL_ABLATIVE = "ablative"  # सूं / स्यूं
    GENITIVE = "genitive"               # रो / री / रा (Marwari) or को / की / का (Dhundhari)
    LOCATIVE = "locative"               # मांय / मांयने / माथे / पे
    VOCATIVE = "vocative"               # ए / ओ / रे / हे


# Traditional Rajasthani Months (विक्रम संवत देसी महीना)
RAJASTHANI_MONTHS: List[Dict[str, str]] = [
    {"rajasthani": "चैत", "roman": "Chait", "hindi": "चैत्र", "season": "बसंत (Spring)"},
    {"rajasthani": "बैसाख", "roman": "Baisakh", "hindi": "वैशाख", "season": "बसंत / उनाळो"},
    {"rajasthani": "जेठ", "roman": "Jeth", "hindi": "ज्येष्ठ", "season": "उनाळो (Summer)"},
    {"rajasthani": "असाढ़", "roman": "Asadh", "hindi": "आषाढ़", "season": "उनाळो / चौमासो"},
    {"rajasthani": "सावण", "roman": "Saawan", "hindi": "श्रावण", "season": "चौमासो (Monsoon)"},
    {"rajasthani": "भादवो", "roman": "Bhadvo", "hindi": "भाद्रपद", "season": "चौमासो (Monsoon)"},
    {"rajasthani": "आसोज", "roman": "Aasoj", "hindi": "आश्विन", "season": "शरद (Autumn)"},
    {"rajasthani": "काती", "roman": "Kaati", "hindi": "कार्तिक", "season": "शरद (Autumn)"},
    {"rajasthani": "मंगसर", "roman": "Mangsar", "hindi": "मार्गशीर्ष", "season": "हेमंत"},
    {"rajasthani": "पोह", "roman": "Poh", "hindi": "पौष", "season": "सिहाळो (Winter)"},
    {"rajasthani": "माह", "roman": "Maah", "hindi": "माघ", "season": "सिहाळो (Winter)"},
    {"rajasthani": "फागण", "roman": "Faagan", "hindi": "फाल्गुन", "season": "फागण / बसंत"},
]

# Rajasthani Ritus / Seasons (ऋतु / मौसम)
SEASONS: Dict[str, Dict[str, str]] = {
    "unalo": {"rajasthani": "उनाळो", "roman": "Unalo", "english": "Summer", "hindi": "गर्मी"},
    "choumaso": {"rajasthani": "चौमासो", "roman": "Choumaso", "english": "Monsoon / Rainy Season", "hindi": "वर्षा ऋतु"},
    "sihalo": {"rajasthani": "सिहाळो", "roman": "Sihalo", "english": "Winter", "hindi": "सर्दी / शीत ऋतु"},
    "basant": {"rajasthani": "बसंत", "roman": "Basant", "english": "Spring", "hindi": "वसंत ऋतु"},
}

# Days of the Week (वार)
DAYS_OF_WEEK: List[Dict[str, str]] = [
    {"rajasthani": "आदितवार / एतवार", "roman": "Aaditwar / Aitwar", "english": "Sunday", "hindi": "रविवार"},
    {"rajasthani": "सोमवार", "roman": "Somwar", "english": "Monday", "hindi": "सोमवार"},
    {"rajasthani": "मंगळवार", "roman": "Mangalwar", "english": "Tuesday", "hindi": "मंगलवार"},
    {"rajasthani": "बुधवार", "roman": "Budhwar", "english": "Wednesday", "hindi": "बुधवार"},
    {"rajasthani": "बृहस्पतिवार / बीरवार", "roman": "Brihaspatiwar / Beerwar", "english": "Thursday", "hindi": "गुरुवार"},
    {"rajasthani": "सुकवार / भ्रगुवार", "roman": "Sukwar / Bhraguwar", "english": "Friday", "hindi": "शुक्रवार"},
    {"rajasthani": "सनीवार / थवार", "roman": "Saniwar / Thawar", "english": "Saturday", "hindi": "शनिवार"},
]

# Common Cultural Greetings (प्रणाम अर आदर-सत्कार)
GREETINGS: List[Dict[str, str]] = [
    {
        "phrase": "खम्मा घणी",
        "response": "घणी खम्मा",
        "roman": "Khamma Ghani",
        "english": "Royal greeting: Much forgiveness and prosperity / May you be blessed with longevity and joy",
        "hindi": "सादर प्रणाम / बहुत-बहुत नमस्कार",
    },
    {
        "phrase": "राम राम सा",
        "response": "राम राम सा",
        "roman": "Ram Ram Sa",
        "english": "Respectful Universal Greeting",
        "hindi": "राम राम जी / सादर प्रणाम",
    },
    {
        "phrase": "जय माता जी री",
        "response": "जय माता जी री सा",
        "roman": "Jai Mata Ji Ri",
        "english": "Invocation of Mother Goddess (Rajput / traditional invocation)",
        "hindi": "माता जी की जय",
    },
    {
        "phrase": "जय जिनेन्द्र",
        "response": "जय जिनेन्द्र सा",
        "roman": "Jai Jinendra",
        "english": "Victory to the Jinas (Jain community greeting across Marwar/Mewar)",
        "hindi": "जय जिनेन्द्र",
    },
    {
        "phrase": "हुकुम",
        "response": "हुकुम सा",
        "roman": "Hukum",
        "english": "Your royal command / At your service (highest honorific)",
        "hindi": "आज्ञा / आपका हुक्म",
    },
    {
        "phrase": "पधारो म्हारे देस",
        "response": "घणी मेहरबानी सा",
        "roman": "Padharo Mhare Des",
        "english": "Welcome to our land (celebrated hospitality motto)",
        "hindi": "हमारे देश में आपका स्वागत है",
    },
]

# Postposition Markers across major dialects
POSTPOSITIONS_BY_DIALECT: Dict[str, Dict[str, str]] = {
    "mwr": {  # Marwari
        "genitive_m_sg": "रो",
        "genitive_f_sg": "री",
        "genitive_m_pl": "रा",
        "genitive_f_pl": "री",
        "ergative": "नै",
        "dative": "नै",
        "ablative": "सूं",
        "locative_in": "मांय",
        "locative_on": "माथे",
        "copula_present": "है",
        "copula_past_m": "थो",
        "copula_past_f": "थी",
        "copula_past_pl": "था",
        "future_suffix": "-सी / -ला",
    },
    "mew": {  # Mewari
        "genitive_m_sg": "रो",
        "genitive_f_sg": "री",
        "genitive_m_pl": "रा",
        "genitive_f_pl": "री",
        "ergative": "नै",
        "dative": "नै",
        "ablative": "सूं",
        "locative_in": "मांय",
        "locative_on": "माथे",
        "copula_present": "है",
        "copula_past_m": "हो",
        "copula_past_f": "ही",
        "copula_past_pl": "हा",
        "future_suffix": "-सी",
    },
    "dhd": {  # Dhundhari (Jaipuri)
        "genitive_m_sg": "को",
        "genitive_f_sg": "की",
        "genitive_m_pl": "का",
        "genitive_f_pl": "की",
        "ergative": "नै",
        "dative": "नै",
        "ablative": "सूं",
        "locative_in": "महि / मांय",
        "locative_on": "ऊपर",
        "copula_present": "छै",
        "copula_past_m": "छो",
        "copula_past_f": "छी",
        "copula_past_pl": "छा",
        "future_suffix": "-गो",
    },
    "hoj": {  # Harauti
        "genitive_m_sg": "को",
        "genitive_f_sg": "की",
        "genitive_m_pl": "का",
        "genitive_f_pl": "की",
        "ergative": "नै",
        "dative": "नै",
        "ablative": "सूं",
        "locative_in": "महि",
        "locative_on": "माथे",
        "copula_present": "छै",
        "copula_past_m": "छो",
        "copula_past_f": "छी",
        "copula_past_pl": "छा",
        "future_suffix": "-गो",
    },
    "swv": {  # Shekhawati
        "genitive_m_sg": "को",
        "genitive_f_sg": "की",
        "genitive_m_pl": "का",
        "genitive_f_pl": "की",
        "ergative": "नै",
        "dative": "नै",
        "ablative": "सूं",
        "locative_in": "मांय",
        "locative_on": "माथे",
        "copula_present": "सै",
        "copula_past_m": "थो",
        "copula_past_f": "थी",
        "copula_past_pl": "था",
        "future_suffix": "-सी / -गो",
    },
}
