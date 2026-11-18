# -*- coding: utf-8 -*-
"""
Enrich Folklore Wave 8 from 'Rajasthani Kahawat Kosh' (Bhagirath Kanoria)
========================================================================
Adds 12 traditional proverbs and 10 authentic idioms to exceed 50+ each.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROVERBS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "proverbs.json")
IDIOMS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "idioms.json")

# 1. Proverbs
with open(PROVERBS_PATH, "r", encoding="utf-8") as f:
    proverbs = json.load(f)

existing_p = {p["rajasthani"].strip() for p in proverbs}

NEW_PROVERBS = [
    {
        "rajasthani": "अकल बड़ी के भैंस?",
        "roman": "Akal badi ke bhains?",
        "hindi": "शारीरिक बल की अपेक्षा बुद्धि अधिक श्रेष्ठ होती है।",
        "english": "Is intellect greater or physical brawn? (Wisdom triumphs over brute strength).",
        "cultural_context": "Classic witty proverb teaching value of foresight over muscular force."
    },
    {
        "rajasthani": "आंधे रै आगै रोवै, आपणा दीदा खोवै।",
        "roman": "Aandhai rai aagai rovai, aapna deeda khovai.",
        "hindi": "अंधे के आगे रोना, अपने ही नैन खोना (अपात्र के समक्ष दुःख प्रकट करना व्यर्थ है)।",
        "english": "Crying before a blind man only ruins one's own eyes (never waste sorrow on the unfeeling).",
        "cultural_context": "Advises prudence in sharing vulnerability only with compassionate people."
    },
    {
        "rajasthani": "नाच न आवै आंगण टेडो।",
        "roman": "Naach na aavai aangan tedo.",
        "hindi": "अपनी अयोग्यता का दोष दूसरों अथवा साधनों पर मढ़ना।",
        "english": "One who cannot dance blames the uneven courtyard floor.",
        "cultural_context": "Satirical proverb rebuking poor craftspeople who blame their tools."
    },
    {
        "rajasthani": "बोयो पेड़ बबूल रो, तो आंबा कित सूं होय?",
        "roman": "Boyo ped babool ro, to aamba kit soon hoy?",
        "hindi": "बबूल का पेड़ बोने पर मीठे आम की प्राप्ति नहीं हो सकती (कर्म अनुसार फल मिलता है)।",
        "english": "If you plant acacia thorns, how can you expect sweet mangoes?",
        "cultural_context": "Ethical warning on the universal law of karma."
    },
    {
        "rajasthani": "चोर री दाढ़ी में तिनको।",
        "roman": "Chor ri daadhi mein tinko.",
        "hindi": "अपराधी अपने आचरण से स्वयं को उजागर कर देता है।",
        "english": "The guilty mind betrays itself through subconscious anxiety.",
        "cultural_context": "Village panchayat psychological adage."
    },
    {
        "rajasthani": "एक हाथ सूं ताळी नीं बाजै।",
        "roman": "Ek haath soon taali neen baajai.",
        "hindi": "विवाद या समझौते में दोनों पक्षों का योगदान होता है।",
        "english": "One hand cannot clap alone (disputes require two parties).",
        "cultural_context": "Arbitration proverb cited by village panchas in reconciliation."
    },
    {
        "rajasthani": "जैसो देस वैसो भेस।",
        "roman": "Jaiso des vaiso bhes.",
        "hindi": "स्थान और परिस्थिति के अनुकूल आचरण करना चाहिये।",
        "english": "When in Rome, do as the Romans do.",
        "cultural_context": "Practical desert nomad guidance across caravans."
    },
    {
        "rajasthani": "कागद री नाव नदी पार नीं उतरै।",
        "roman": "Kaagad ri naav nadi paar neen utrai.",
        "hindi": "झूठ और दिखावे का सहारा अधिक समय तक नहीं टिकता।",
        "english": "A paper boat cannot cross a turbulent river (untruth cannot sustain life).",
        "cultural_context": "Moral lesson on honesty and durability."
    },
    {
        "rajasthani": "गादड़ री मौत आवै तो शहर कानी भाजै।",
        "roman": "Gaadar ri maut aavai to shahar kaani bhaajai.",
        "hindi": "विनाश काले विपरीत बुद्धि (संकट काल में व्यक्ति अनुचित निर्णय लेता है)।",
        "english": "When destruction approaches the jackal, it flees toward the hunter's town.",
        "cultural_context": "Observations on recklessness preceding downfall."
    },
    {
        "rajasthani": "भूखे भजन न होय गोपाला।",
        "roman": "Bhookhe bhajan na hoy gopaala.",
        "hindi": "खाली पेट ईश्वर की भक्ति भी संभव नहीं होती (मूलभूत आवश्यकताएं अनिवार्य हैं)।",
        "english": "An empty stomach cannot sing devotional psalms (sustenance is the foundation of life).",
        "cultural_context": "Pragmatic balance between spiritual yearning and earthly survival."
    },
    {
        "rajasthani": "पानी पी'र जात नीं पूछणी।",
        "roman": "Paani pee'r jaat neen poochhni.",
        "hindi": "काम पूरा होने के बाद साधन या संबंध पर व्यर्थ संदेह नहीं करना चाहिये।",
        "english": "Never ask the caste after having drunk the water (embrace generosity without prejudice).",
        "cultural_context": "Folk critique of rigid caste orthodoxy in arid hospitality."
    },
    {
        "rajasthani": "लोभ पाप रो मूल है।",
        "roman": "Lobh paap ro mool hai.",
        "hindi": "लालच ही समस्त पापों और कष्टों की जड़ है।",
        "english": "Greed is the root of all ruin and sin.",
        "cultural_context": "Traditional moral bedrock taught to children in merchant households."
    }
]

added_p = 0
for np in NEW_PROVERBS:
    if np["rajasthani"].strip() not in existing_p:
        proverbs.append(np)
        existing_p.add(np["rajasthani"].strip())
        added_p += 1

with open(PROVERBS_PATH, "w", encoding="utf-8") as f:
    json.dump(proverbs, f, ensure_ascii=False, indent=2)

print(f"Added {added_p} proverbs. Total proverbs now: {len(proverbs)}")

# 2. Idioms
with open(IDIOMS_PATH, "r", encoding="utf-8") as f:
    idioms = json.load(f)

existing_i = {i["rajasthani"].strip() for i in idioms}

NEW_IDIOMS = [
    {
        "rajasthani": "आंख्यां में धूळ झोंकणी",
        "roman": "aankhyaan mein dhool jhonkani",
        "hindi": "धोखा देना / भ्रमित करना",
        "english": "to throw dust in someone's eyes; to deceive slyly",
        "cultural_context": "Common desert expression drawing imagery from dust storms.",
        "example": "शत्रु आंख्यां में धूळ झोंक'र भाग नीकळ्यो।"
    },
    {
        "rajasthani": "पग जमावणा",
        "roman": "pag jamaavna",
        "hindi": "स्थिति को सुदृढ़ बनाना / प्रभुत्व स्थापित करना",
        "english": "to plant feet firmly; to establish strong standing",
        "cultural_context": "Commercial and political idiom of Marwari merchants settling new mandis.",
        "example": "व्यापार में सेठ जी आपरा पग जमाया।"
    },
    {
        "rajasthani": "बात रो बतंगड़ बणावणो",
        "roman": "baat ro batangad banaavno",
        "hindi": "राई का पहाड़ बनाना / छोटी बात को तूल देना",
        "english": "to blow a tiny matter completely out of proportion",
        "cultural_context": "Domestic critique of needless squabbling.",
        "example": "छोटी सी बात रो बतंगड़ बणाय दियो।"
    },
    {
        "rajasthani": "जी जलणो",
        "roman": "jee jalno",
        "hindi": "ईर्ष्या अथवा अत्यधिक दुःख होना",
        "english": "to burn with deep anguish or envy",
        "cultural_context": "Emotional description of deep heartache.",
        "example": "दूसरे री तरक्की देख'र दुर्जन रो जी जलै।"
    },
    {
        "rajasthani": "पसीना रो मोल चुकावणो",
        "roman": "paseena ro mol chukaavno",
        "hindi": "कठिन परिश्रम का उचित प्रतिफल देना",
        "english": "to honor the worth of hard labor and sweat",
        "cultural_context": "Ethical guidance for employers and landlords in Rajasthan.",
        "example": "मजदूर रै पसीने रो पूरो मोल चुकायो।"
    },
    {
        "rajasthani": "कलेजे ठंडक पड़णी",
        "roman": "kaleje thandak padni",
        "hindi": "परम शांति व संतोष का अनुभव होना",
        "english": "to experience soothing peace and fulfillment in heart",
        "cultural_context": "Signifies joy of reunited kin or resolved crisis in desert heat.",
        "example": "बेटे ने सकुशल देख'र मां रै कलेजे ठंडक पड़ी।"
    },
    {
        "rajasthani": "नाक कटवावणी",
        "roman": "naak katwaavni",
        "hindi": "प्रतिष्ठा नष्ट करना / कुल को लज्जित करना",
        "english": "to bring public disgrace upon family dignity",
        "cultural_context": "Strict social commentary on maintaining honor.",
        "example": "गलत काम कर'र खानदान री नाक कटवाई।"
    },
    {
        "rajasthani": "हथेली माथे सरसूं उगावणी",
        "roman": "hatheli maathe sarsoon ugaavni",
        "hindi": "असंभव कार्य को तुरंत करने का दावा करना",
        "english": "to claim to sprout mustard on one's palm (attempting the impossible)",
        "cultural_context": "Folk adage rebuking unrealistic promises.",
        "example": "एक दिन में हवेली बणावणो तो हथेली माथे सरसूं उगावण ज्यूं है।"
    },
    {
        "rajasthani": "पाणी-पाणी व्हैणो",
        "roman": "paani-paani hvaino",
        "hindi": "अत्यधिक लज्जित होना",
        "english": "to drown in intense embarrassment and shame",
        "cultural_context": "Common colloquial expression.",
        "example": "चोरी पकड़ी जात ही वो पाणी-पाणी होय गयो।"
    },
    {
        "rajasthani": "सिर माथे चढ़णा",
        "roman": "sir maathe chadhna",
        "hindi": "अत्यधिक लाड़-प्यार से बिगड़ जाना",
        "english": "to become spoiled through excess indulgence",
        "cultural_context": "Domestic parenting observation in joint households.",
        "example": "अति लाड सूं बालक सिर माथे चढ़ गयो।"
    }
]

added_i = 0
for ni in NEW_IDIOMS:
    if ni["rajasthani"].strip() not in existing_i:
        idioms.append(ni)
        existing_i.add(ni["rajasthani"].strip())
        added_i += 1

with open(IDIOMS_PATH, "w", encoding="utf-8") as f:
    json.dump(idioms, f, ensure_ascii=False, indent=2)

print(f"Added {added_i} idioms. Total idioms now: {len(idioms)}")
