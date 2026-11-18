# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Traditional Architecture (वास्तु अर भवन-निर्माण)
=============================================================================
Detailed catalog of iconic Rajasthani vernacular architectural elements:
Havelis, Jharokhas, Stepwells (Baoris), Cenotaphs (Chhatris), Fort Gates (Pols),
and indigenous building traditions.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ArchitectureElement:
    name: str
    roman: str
    category: str
    description: str
    architectural_features: str
    famous_examples: List[str]


ARCHITECTURE_DATABASE: List[ArchitectureElement] = [
    ArchitectureElement(
        name="हवेली (Haveli)",
        roman="Haveli",
        category="mansions",
        description="Elaborate private mansions built by wealthy merchants and nobles with internal open courtyards and ornate frescoes.",
        architectural_features="Double courtyards (mardana and zenana), exquisite fresco murals, sandstone carved facade.",
        famous_examples=["पटवों की हवेली (Jaisalmer)", "नथमल की हवेली (Jaisalmer)", "बड़ा बाग हवेलियां (Shekhawati)", "बागोर की हवेली (Udaipur)"],
    ),
    ArchitectureElement(
        name="झरोखो (Jharokha)",
        roman="Jharokha",
        category="balcony",
        description="Projecting stone balcony resting on carved brackets with fine stone lattice screens (jali).",
        architectural_features="Allows natural cooling air currents (venturi effect) and discrete viewing of streets.",
        famous_examples=["हवामहल (Jaipur - 953 Jharokhas)", "मेहरानगढ़ झरोखे (Jodhpur)", "पटवा हवेली झरोखे (Jaisalmer)"],
    ),
    ArchitectureElement(
        name="छतरी (Chhatri)",
        roman="Chhatri",
        category="cenotaph",
        description="Elevated, dome-shaped pavilions used as memorials for departed kings, warriors, and saints.",
        architectural_features="Ornate pillars, vaulted ceiling with lotus finial, carved friezes of folk epics.",
        famous_examples=["चौरासी खंभों की छतरी (Bundi)", "मूसी महारानी की छतरी (Alwar)", "बड़ा बाग छतरियां (Jaisalmer)", "जसवंत थड़ा (Jodhpur)"],
    ),
    ArchitectureElement(
        name="बावड़ी (Baori / Stepwell)",
        roman="Baori",
        category="water_architecture",
        description="Deep subterranean stepped wells engineered for desert rainwater harvesting with cool shaded sanctuaries.",
        architectural_features="Geometrical descending flights of stairs, subterranean multi-tiered pillared pavilions.",
        famous_examples=["चाँद बावड़ी (Abhaneri, Dausa)", "रानी जी की बावड़ी (Bundi)", "पन्ना मीणा का कुंड (Amer, Jaipur)"],
    ),
    ArchitectureElement(
        name="पोळ (Pol / Gateway)",
        roman="Pol",
        category="fortifications",
        description="Monumental fortified gateway leading into desert citadels and royal precincts.",
        architectural_features="Spiked heavy wooden doors against war elephants, bent-axis defensive turns, guard bastions.",
        famous_examples=["जयपोल अर फतहपोल (Mehrangarh, Jodhpur)", "हाथी पोल (City Palace, Udaipur)", "सूरज पोल (Amer Fort)"],
    ),
    ArchitectureElement(
        name="मांडणो (Mandana)",
        roman="Mandana",
        category="folk_art_architecture",
        description="Sacred geometric designs and symbols painted on mud floors and walls with chalk and brick powder.",
        architectural_features="Triangles, peacocks, swastikas, flowers painted during festivals to welcome fortune.",
        famous_examples=["Traditional homes across Meena and rural households in Sawai Madhopur, Bundi, and Tonk"],
    ),
    ArchitectureElement(
        name="तिबारी (Tibari)",
        roman="Tibari",
        category="verandah",
        description="Three-arched pillared verandah overlooking the inner courtyard.",
        architectural_features="Cusped arches, fluted pillars, cool evening seating space for joint family assemblies.",
        famous_examples=["Interior courtyards across Havelis of Shekhawati and Bikaner"],
    ),
]


def get_architecture_elements() -> List[ArchitectureElement]:
    """Returns all cataloged traditional Rajasthani architectural elements."""
    return list(ARCHITECTURE_DATABASE)


def lookup_architecture(name: str) -> Optional[ArchitectureElement]:
    """Looks up architectural element by Hindi or English name."""
    clean = name.strip().lower()
    for el in ARCHITECTURE_DATABASE:
        if clean in el.name.lower() or clean in el.roman.lower():
            return el
    return None
