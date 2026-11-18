# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Traditional Ornaments & Jewelry (आभूषण अर गहणा)
=============================================================================
Comprehensive catalog of authentic Rajasthani jewelry spanning head-to-toe:
Head, Forehead, Ear, Nose, Neck, Upper Arm, Wrist, Finger, Waist, and Foot
for both women and men, featuring historical alloys, gems, and cultural significance.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Ornament:
    name: str
    roman: str
    body_part: str  # head, ear, nose, neck, arm, wrist, finger, waist, foot
    metal: str      # gold, silver, ivory, brass, kundan, meenakari
    description: str
    cultural_context: str


ORNAMENTS_DATABASE: List[Ornament] = [
    # =========================================================================
    # 1. HEAD & FOREHEAD ORNAMENTS (सिर अर माथा रा आभूषण)
    # =========================================================================
    Ornament(
        name="रखड़ी / बोरलो (Rakhdi / Borla)",
        roman="Rakhdi / Borla",
        body_part="head",
        metal="gold / kundan / rubies",
        description="Spherical bell-shaped forehead ornament positioned precisely at the central parting of hair (मांग).",
        cultural_context="Quintessential emblem of marital status (सुहाग चिन्ह) worn by married women across Marwar and Mewar.",
    ),
    Ornament(
        name="शीशफूल (Sheeshphool)",
        roman="Sheeshphool",
        body_part="head",
        metal="gold / kundan / pearls",
        description="Floral round medallions fastened to the hair on either side of the Rakhdi linked by delicate pearl chains.",
        cultural_context="Adorns the crown of bridal and festive styling in royal processions.",
    ),
    Ornament(
        name="मेमंद (Memand)",
        roman="Memand",
        body_part="head",
        metal="gold / silver",
        description="Arched forehead band tied across the brow adorned with dangling golden beads, celebrated in folk songs.",
        cultural_context="Immortalized in the iconic Marwari folk song 'म्हारो मेमंद ल्यायो सा'.",
    ),
    Ornament(
        name="टीकी / टिकली (Tikli)",
        roman="Tikli",
        body_part="head",
        metal="gold foil / glass / lac",
        description="Glittering decorative forehead dot placed between eyebrows below the parting ornament.",
        cultural_context="Daily auspicious ornament worn by women across all rural communities.",
    ),
    Ornament(
        name="दामिनी / तावित (Damini / Taavit)",
        roman="Damini / Taavit",
        body_part="head",
        metal="gold / pearls",
        description="Elaborate head ornament with side chains that contour the temples and crown.",
        cultural_context="Worn during grand wedding ceremonies and seasonal royal durbars.",
    ),
    Ornament(
        name="सांकळी (Sankali)",
        roman="Sankali",
        body_part="head",
        metal="silver / gold",
        description="Interconnected flexible chain draped over the braid or hairline.",
        cultural_context="Secures the odhani firmly over the hair in desert winds.",
    ),

    # =========================================================================
    # 2. EAR ORNAMENTS (कान रा आभूषण)
    # =========================================================================
    Ornament(
        name="झुमका / झुमरी (Jhumka / Jhumri)",
        roman="Jhumka / Jhumri",
        body_part="ear",
        metal="gold / silver / meenakari",
        description="Hanging bell-shaped earrings with tiny golden fringing beads that sway gracefully with movement.",
        cultural_context="Universal favorite across classical and folk traditions.",
    ),
    Ornament(
        name="कर्णफूल (Karanphool)",
        roman="Karanphool",
        body_part="ear",
        metal="gold / uncut diamonds",
        description="Large flower-shaped ear stud covering the entire earlobe, often paired with supporting Jhela chains.",
        cultural_context="Heirloom jewelry passed down from mother-in-law to incoming bride.",
    ),
    Ornament(
        name="ओगण्या (Oganiya)",
        roman="Oganiya",
        body_part="ear",
        metal="solid gold / silver",
        description="Distinctive curved clip ornament worn on the upper cartilage of the ear.",
        cultural_context="Traditional rural ornament popular among Marwari and Shekhawati communities.",
    ),
    Ornament(
        name="सुरलिया (Surliya)",
        roman="Surliya",
        body_part="ear",
        metal="gold / silver",
        description="Crescent-shaped or cylindrical ear ornament suspended from the middle ear cartilage.",
        cultural_context="Ancient design documented in medieval Rajasthani miniature paintings.",
    ),
    Ornament(
        name="पीपलपत्ता (Peepalpata)",
        roman="Peepalpata",
        body_part="ear",
        metal="gold / silver",
        description="Earrings shaped like delicate trembling Peepal tree leaves.",
        cultural_context="Symbolizes nature veneration and ecological roots.",
    ),
    Ornament(
        name="टोटी (Toti)",
        roman="Toti",
        body_part="ear",
        metal="gold / red stones",
        description="Circular convex button-like ear ornament tightly gripping the lower lobe.",
        cultural_context="Favored by rural pastoral women in Dhundhar and Harauti.",
    ),
    Ornament(
        name="झेला (Jhela)",
        roman="Jhela",
        body_part="ear",
        metal="gold / pearl strand",
        description="Support chains that connect heavy earrings to the hair to alleviate earlobe strain.",
        cultural_context="Dual purpose of distributing weight and adding decorative shimmer to the hair.",
    ),
    Ornament(
        name="मुरकी (Murki)",
        roman="Murki",
        body_part="ear",
        metal="solid gold",
        description="Small smooth circular hoop earring worn exclusively by Rajasthani men in both ears.",
        cultural_context="Male mark of rustic nobility, valor, and pastoral pride.",
    ),

    # =========================================================================
    # 3. NOSE ORNAMENTS (नाक रा आभूषण)
    # =========================================================================
    Ornament(
        name="नथ (Nath)",
        roman="Nath",
        body_part="nose",
        metal="gold / pearls / kundan",
        description="Large ornate nose ring looped through the left nostril and supported by a fine gold chain hitched to the hair.",
        cultural_context="Supreme jewel of Rajasthani bridal attire and temple festivities.",
    ),
    Ornament(
        name="बेसरी (Besar)",
        roman="Besar",
        body_part="nose",
        metal="gold / pearl drop / emerald",
        description="Crescent-shaped pendant nose ornament immortalized in the Kishangarh school of painting.",
        cultural_context="Identified internationally with 'Bani Thani' - the Indian Mona Lisa.",
    ),
    Ornament(
        name="लोंग (Long)",
        roman="Long",
        body_part="nose",
        metal="gold / diamond / clove shape",
        description="Small clove-shaped stud worn in the nostril for daily wear.",
        cultural_context="Celebrated in popular folklore: 'म्हारो लोंग गवायो सा'.",
    ),
    Ornament(
        name="कांटा (Kanta)",
        roman="Kanta",
        body_part="nose",
        metal="gold / silver / ruby",
        description="Delicate single-gem nose pin fastened with a screw back.",
        cultural_context="Commonly gifted to young girls upon their first ear-and-nose piercing.",
    ),
    Ornament(
        name="चुन्नी / फीणी (Chunni / Phini)",
        roman="Chunni / Phini",
        body_part="nose",
        metal="gold / diamond",
        description="Tiny sparkling single-stone nose stud reflecting light like a dewdrop.",
        cultural_context="Subtle everyday nose ornament favored in urban and rural Rajasthan.",
    ),

    # =========================================================================
    # 4. NECK ORNAMENTS (गळा रा आभूषण अर हार)
    # =========================================================================
    Ornament(
        name="आड़ (Aad)",
        roman="Aad",
        body_part="neck",
        metal="gold / kundan / meenakari / pearls",
        description="Broad, rectangular rigid choker collar featuring heavy kundan stones with hanging clusters of pearls.",
        cultural_context="The sovereign bridal choker of Rajput nobility across Rajasthan.",
    ),
    Ornament(
        name="तिमणियो (Timaniyo)",
        roman="Timaniyo",
        body_part="neck",
        metal="gold / uncut diamonds",
        description="Tiered rectangular gold choker with three distinct gemstone registers and pearl fringes.",
        cultural_context="Celebrated in Rajasthani bridal songs as an indispensable wedding gift.",
    ),
    Ornament(
        name="चंपाकली (Champaakali)",
        roman="Champaakali",
        body_part="neck",
        metal="solid gold",
        description="Necklace composed of numerous linked golden buds shaped like fragrant Champa (jasmine) florets.",
        cultural_context="Mastery of goldsmithing popular across Jaipur and Mewar.",
    ),
    Ornament(
        name="मांदळियो (Maandaliyo)",
        roman="Maandaliyo",
        body_part="neck",
        metal="silver / gold",
        description="Cylindrical hollow amulet strung on sacred black thread carrying inscribed deity mantras.",
        cultural_context="Worn for spiritual protection against the evil eye and negative energies.",
    ),
    Ornament(
        name="हंसली (Hansali)",
        roman="Hansali",
        body_part="neck",
        metal="solid cast silver",
        description="Rigid crescent-shaped torque collar encircling the collarbones.",
        cultural_context="Iconic heavy traditional silver jewelry worn by pastoral and village women.",
    ),
    Ornament(
        name="कंठी (Kanthi)",
        roman="Kanthi",
        body_part="neck",
        metal="gold / agate / tulsi beads",
        description="Close-fitting beaded neckband worn by both women and devotional men.",
        cultural_context="Common in Vaishnav and folk bhakti devotional sects.",
    ),
    Ornament(
        name="गलपट्टा (Galpatta)",
        roman="Galpatta",
        body_part="neck",
        metal="gold / velvet backing / kundan",
        description="Velvet-backed flexible choker embedded with uncut stones worn tight against the throat.",
        cultural_context="Royal court attire providing regal posture.",
    ),
    Ornament(
        name="मोहनमाला / चंदनहार (Mohanmala / Chandanhar)",
        roman="Mohanmala / Chandanhar",
        body_part="neck",
        metal="gold / pearls",
        description="Long cascading multi-layered necklace falling gracefully below the chest.",
        cultural_context="Worn during festivals, durbar receptions, and state banquets.",
    ),
    Ornament(
        name="तुलसी (Tulsi)",
        roman="Tulsi",
        body_part="neck",
        metal="gold / sacred wood",
        description="Necklace consisting of tiny golden beads interspersed with sacred basil wood.",
        cultural_context="Symbol of purity, domestic piety, and auspicious blessings.",
    ),

    # =========================================================================
    # 5. ARMS, WRISTS & FINGER ORNAMENTS (बाजू, हाथ अर आंगळी रा आभूषण)
    # =========================================================================
    Ornament(
        name="बाजूबंद (Baazooband)",
        roman="Baazooband",
        body_part="arm",
        metal="gold / meenakari / red silk tassels",
        description="Upper armlet worn above the elbow fastened securely with braided silk cords and gold tassels (लूम).",
        cultural_context="Heroic and bridal ornament celebrating beauty and martial prestige.",
    ),
    Ornament(
        name="टड्डा / अणत (Tadda / Anat)",
        roman="Tadda / Anat",
        body_part="arm",
        metal="solid silver / gold",
        description="Heavy solid torque armlet with carved mythological serpent or floral terminals.",
        cultural_context="Worn tight on the bicep by agricultural and pastoral communities.",
    ),
    Ornament(
        name="हाथीदांत रो चूड़ो (Ivory Chooda)",
        roman="Haathidaant ro Choodo",
        body_part="arm",
        metal="ivory / acrylic / gold trim",
        description="Concentric sequence of white bangles graduated in diameter, worn from wrist all the way up to upper arm.",
        cultural_context="Inviolable emblem of marital bliss gifted exclusively by the maternal uncle (मामो).",
    ),
    Ornament(
        name="गोखरू (Gokhroo)",
        roman="Gokhroo",
        body_part="wrist",
        metal="solid gold / silver",
        description="Heavy solid bangle with jagged pyramidal serrations designed like cocklebur burrs.",
        cultural_context="Flanks the ivory chooda to protect it from slipping.",
    ),
    Ornament(
        name="बंगड़ी (Bangadi)",
        roman="Bangadi",
        body_part="wrist",
        metal="solid gold / lac filling",
        description="Thick circular gold bangle with round embossed pearls or beads along its circumference.",
        cultural_context="Traditional heirloom bangle worn by married women.",
    ),
    Ornament(
        name="पाटला (Patla)",
        roman="Patla",
        body_part="wrist",
        metal="gold / flat engraved band",
        description="Wide flat bangle with floral filigree work worn in pairs.",
        cultural_context="Standard piece of formal Rajasthani jewelry.",
    ),
    Ornament(
        name="नौगरी (Naugari)",
        roman="Naugari",
        body_part="wrist",
        metal="pearls / gold beads",
        description="Delicate wristlet formed by nine parallel strands of fine pearls and gold separators.",
        cultural_context="Favored by royal women of Jaipur and Jodhpur.",
    ),
    Ornament(
        name="पूंछी (Poonchi)",
        roman="Poonchi",
        body_part="wrist",
        metal="fabric band / gold beads",
        description="Band of woven red fabric mounted with multiple rows of small hollow golden spheres.",
        cultural_context="Rustic bridal jewelry of Shekhawati and Dhundhar.",
    ),
    Ornament(
        name="हथफूल (Hathphool)",
        roman="Hathphool",
        body_part="wrist",
        metal="gold / kundan / pearl web",
        description="Spiderweb-like ornament connecting a wrist bracelet to rings on all five fingers across the back of the hand.",
        cultural_context="Dramatically accentuates the graceful hand gestures of bridal rituals and dances.",
    ),
    Ornament(
        name="अरसी (Arsi)",
        roman="Arsi",
        body_part="finger",
        metal="gold / inset round mirror",
        description="Thumb ring set with a small convex mirror framed by gems.",
        cultural_context="Historically allowed the shy veiled bride to discreetly glance at her groom's face through her veil.",
    ),
    Ornament(
        name="बीटी / मूंदड़ी (Biti / Moondari)",
        roman="Biti / Moondari",
        body_part="finger",
        metal="gold / silver / gemstones",
        description="Engraved finger ring set with navratna or clan seals.",
        cultural_context="Universal ring worn on fingers.",
    ),

    # =========================================================================
    # 6. WAIST ORNAMENTS (कमर रा आभूषण)
    # =========================================================================
    Ornament(
        name="कंदोरो / तगड़ी (Kandoro / Tagadi)",
        roman="Kandoro / Tagadi",
        body_part="waist",
        metal="solid silver / gold",
        description="Multi-strand flexible silver belt draped loosely over the hips with tiny jingling bells (घूंघरू).",
        cultural_context="Accentuates waist movement during Ghoomar and Chari dances.",
    ),
    Ornament(
        name="करधनी (Kardhani)",
        roman="Kardhani",
        body_part="waist",
        metal="silver",
        description="Wide interlocking mesh silver belt fitted securely around the upper edge of the Ghagra.",
        cultural_context="Holds the voluminous folds of the heavy skirt in place.",
    ),
    Ornament(
        name="सटका (Satka)",
        roman="Satka",
        body_part="waist",
        metal="silver with key bunch / cowries",
        description="Ornate silver bunch of keys and trinkets tucked into the waist fold of the skirt hanging to the side.",
        cultural_context="Signifies household management and authority of the senior daughter-in-law.",
    ),
    Ornament(
        name="कणकती (Kanakti)",
        roman="Kanakti",
        body_part="waist",
        metal="gold / silver chain",
        description="Delicate single or double silver chain wrapped around the waist.",
        cultural_context="Subtle everyday waist jewelry worn by young women.",
    ),

    # =========================================================================
    # 7. FEET & ANKLE ORNAMENTS (पगां रा आभूषण)
    # (Note: Gold is traditionally never worn on feet out of respect for Lakshmi)
    # =========================================================================
    Ornament(
        name="पायल / झांझर (Paayal / Jhaanjhar)",
        roman="Paayal / Jhaanjhar",
        body_part="foot",
        metal="pure silver",
        description="Musical silver chain anklet adorned with hundreds of tiny resonant ghungroos.",
        cultural_context="Creates rhythmic melody across sandstone courtyards with every step.",
    ),
    Ornament(
        name="आंवळा (Aanwala)",
        roman="Aanwala",
        body_part="foot",
        metal="solid cast silver",
        description="Heavy solid ribbed silver ring anklet worn above the foot joint.",
        cultural_context="Iconic heavy traditional foot jewelry of western Rajasthan.",
    ),
    Ornament(
        name="नेवरी (Nevari)",
        roman="Nevari",
        body_part="foot",
        metal="flexible silver",
        description="Curved hollow silver anklet worn above the payal, producing gentle tinkling tones.",
        cultural_context="Aesthetic pairing with Aanwala in Marwari high fashion.",
    ),
    Ornament(
        name="रमझोल (Ramjhol)",
        roman="Ramjhol",
        body_part="foot",
        metal="silver with broad band of bells",
        description="Broad leather or fabric band covered with dozens of silver bells tied around ankles by folk dancers.",
        cultural_context="Produces powerful resonant rhythmic punctuation in Ghoomar and Kalbelia dances.",
    ),
    Ornament(
        name="तोड़ा (Toda)",
        roman="Toda",
        body_part="foot",
        metal="solid silver rod",
        description="Very heavy thick silver rod forged into an anklet with decorative ball ends.",
        cultural_context="Worn by rural matriarchs as a store of family wealth and security.",
    ),
    Ornament(
        name="लंगर (Langar)",
        roman="Langar",
        body_part="foot",
        metal="silver thick links",
        description="Heavy chain-link anklet resting heavily over the top of the foot.",
        cultural_context="Rustic style common in Mewar and Harauti.",
    ),
    Ornament(
        name="बिछिया (Bichhiya)",
        roman="Bichhiya",
        body_part="foot",
        metal="pure silver",
        description="Engraved silver toe rings worn on the second toe of both feet.",
        cultural_context="Sacred emblem of married woman (सुहाग चिन्ह); stimulates acupressure nerves associated with reproductive health.",
    ),
    Ornament(
        name="फोलरी (Pholari)",
        roman="Pholari",
        body_part="foot",
        metal="silver flower design",
        description="Toe ring shaped like a blooming flower worn on third or fourth toe.",
        cultural_context="Decorative bridal foot adornment.",
    ),
    Ornament(
        name="चुटकी (Chutki)",
        roman="Chutki",
        body_part="foot",
        metal="silver spiral wire",
        description="Coiled silver wire toe ring worn on little toes.",
        cultural_context="Daily foot adornment for village women.",
    ),
    Ornament(
        name="हीरनासैन (Hirnamain)",
        roman="Hirnamain",
        body_part="foot",
        metal="silver",
        description="Smooth curved tubular silver anklet worn by tribal and nomadic communities (Bhil, Garasia).",
        cultural_context="Traditional adornment reflecting ancient tribal metallurgic skills.",
    ),
]


def get_all_ornaments() -> List[Ornament]:
    """Returns all cataloged traditional Rajasthani ornaments."""
    return list(ORNAMENTS_DATABASE)


def get_ornaments_by_body_part(body_part: str) -> List[Ornament]:
    """Filters ornaments by body part (head, ear, nose, neck, arm, wrist, finger, waist, foot)."""
    return [o for o in ORNAMENTS_DATABASE if o.body_part == body_part]
