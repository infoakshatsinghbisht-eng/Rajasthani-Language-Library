# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROVERBS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "proverbs.json")
IDIOMS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "idioms.json")

# 1. Enrich Proverbs
with open(PROVERBS_PATH, "r", encoding="utf-8") as f:
    proverbs = json.load(f)

existing_proverbs = {p["rajasthani"].strip() for p in proverbs}

new_proverbs = [
    {
        "rajasthani": "ऊंट किस करवट बैठै, राम ही जाणै।",
        "roman": "Oont kis karvat baithai, Ram hi jaanai.",
        "hindi": "ऊंट किस करवट बैठेगा, यह केवल ईश्वर जानता है (परिणाम अनिश्चित है)।",
        "english": "Only God knows which way the camel will kneel (uncertainty of unpredictable outcomes).",
        "cultural_context": "Desert proverb highlighting the uncertain turn of events in politics, weather, or commerce."
    },
    {
        "rajasthani": "बाजरी रो सोगरो अर काचरी रो साग, मिल जावै तो राजा रो भाग।",
        "roman": "Baajri ro sogro ar kaachari ro saag, mil jaavai to raja ro bhaag.",
        "hindi": "बाजरे की गर्म रोटी और काचरी की सब्जी मिल जाए तो राजा जैसा भाग्य है।",
        "english": "Hot bajra bread with wild kachari curry is fortune fit for an emperor.",
        "cultural_context": "Celebration of simple, wholesome desert cuisine bringing supreme happiness and health."
    },
    {
        "rajasthani": "धोरी रै माथै सींग, अर रजपूत रै माथै पाग।",
        "roman": "Dhori rai maathai seemg, ar Rajpoot rai maathai paag.",
        "hindi": "बैल के सिर पर सींग और राजपूत के सिर पर पगड़ी ही उसकी शोभा व मर्यादा है।",
        "english": "Just as horns adorn the bull, the turban defines the honor and integrity of a Rajput.",
        "cultural_context": "Emphasizes that identity, dignity, and headgear cannot be compromised."
    },
    {
        "rajasthani": "आप मुआं बिना सुरग नीं दीखै।",
        "roman": "Aap muaan bina surag neen deekhai.",
        "hindi": "स्वयं के मरे बिना स्वर्ग नहीं दिखता (खुद कर्म किए बिना फल या अनुभव नहीं मिलता)।",
        "english": "One cannot see heaven without dying oneself (success requires direct personal exertion).",
        "cultural_context": "Exhortation to personal responsibility, self-reliance, and active courage."
    },
    {
        "rajasthani": "पूत रा पग पालणै में ही दीखै।",
        "roman": "Poot ra pag paalanai mein hi deekhai.",
        "hindi": "पुत्र के लक्षण पालने में ही दिखाई दे जाते हैं (होनहार बिरवान के होत चीकने पात)।",
        "english": "A child's future character is evident right from the rocking cradle.",
        "cultural_context": "Reflects belief in early virtue, lineage training, and natural genius."
    },
    {
        "rajasthani": "जैसी संगत, वैसी रंगत।",
        "roman": "Jaisi sangat, vaisi rangat.",
        "hindi": "जैसी संगति होगी, वैसा ही प्रभाव और चरित्र बनेगा।",
        "english": "As the companionship, so the character and influence.",
        "cultural_context": "Moral guidance advising youth to seek noble companions."
    },
    {
        "rajasthani": "डूबते नै तिनके रो सहारो घणो।",
        "roman": "Doobte nai tinke ro sahaaro ghano.",
        "hindi": "डूबते हुए को तिनके का सहारा भी बहुत होता है।",
        "english": "To a drowning soul, even a straw of hope is immense salvation.",
        "cultural_context": "Compassion in extreme desert hardship and drought relief."
    },
    {
        "rajasthani": "हाथ कंगन नै आरसी क्या? पढ़े-लिखे नै फारसी क्या?",
        "roman": "Haath kangan nai aarsi kya? Padhe-likhe nai Faarsi kya?",
        "hindi": "प्रत्यक्ष को प्रमाण की आवश्यकता नहीं होती।",
        "english": "What need is there of a mirror to see bangles on one's own wrist? (The obvious needs no proof).",
        "cultural_context": "Alludes to the 'arsi' thumb-ring mirror ornament worn by Rajasthani women."
    },
    {
        "rajasthani": "घर रो भेदी लंका ढावै।",
        "roman": "Ghar ro bhedi Lanka dhaavai.",
        "hindi": "घर का भेदिया ही विनाश का कारण बनता है।",
        "english": "The insider traitor destroys the citadel.",
        "cultural_context": "Traditional caution against domestic betrayal and disunity."
    },
    {
        "rajasthani": "धीरज धरम मित्र अरु नारी, आपद काल परखिये चारी।",
        "roman": "Dheeraj dharam mitra aru naari, aapad kaal parakhiye chaari.",
        "hindi": "धैर्य, धर्म, मित्र और पत्नी की परीक्षा विपत्ति के समय ही होती है।",
        "english": "Fortitude, righteousness, friends, and spouse are truly tested in moments of adversity.",
        "cultural_context": "Centuries-old ethical benchmark cherished across Rajasthani joint families."
    }
]

p_added = 0
for np in new_proverbs:
    if np["rajasthani"].strip() not in existing_proverbs:
        proverbs.append(np)
        existing_proverbs.add(np["rajasthani"].strip())
        p_added += 1

with open(PROVERBS_PATH, "w", encoding="utf-8") as f:
    json.dump(proverbs, f, ensure_ascii=False, indent=2)

print(f"Added {p_added} new proverbs! Total proverbs: {len(proverbs)}")

# 2. Enrich Idioms
with open(IDIOMS_PATH, "r", encoding="utf-8") as f:
    idioms = json.load(f)

existing_idioms = {i["rajasthani"].strip() for i in idioms}

new_idioms = [
    {
        "rajasthani": "हाथ पीले करणा",
        "roman": "haath peele karna",
        "hindi": "कन्या का विवाह करना",
        "english": "to marry off a daughter (referencing auspicious turmeric ceremony)",
        "cultural_context": "Associated with the pre-wedding 'baan' and turmeric paste rites for the bride.",
        "example": "बाबोसा लाडली बेटी रा हाथ पीले कियो।"
    },
    {
        "rajasthani": "घोड़े बेच'र सोवणो",
        "roman": "ghode bech'r sovno",
        "hindi": "निश्चिंत होकर गहरी नींद सोना",
        "english": "to sleep soundly and carefree without anxiety",
        "cultural_context": "Alludes to a merchant or traveler sleeping soundly once their horses are settled.",
        "example": "परीक्षा समाप्त होवण पछै बालक घोड़े बेच'र सोयो।"
    },
    {
        "rajasthani": "घी के दीवे जळावणा",
        "roman": "ghee ke deeve jalaavna",
        "english": "to celebrate an occasion with supreme joy and gratitude",
        "hindi": "अत्यधिक खुशी मनाना / घी के दीपक जलाना",
        "cultural_context": "Signifies prosperity and sacred fulfillment of prayers with pure ghee offerings.",
        "example": "पुत्र री विजय री खबर सुण'र मां घी के दीवे जळाया।"
    },
    {
        "rajasthani": "दांत खट्टे करणा",
        "roman": "daant khatte karna",
        "english": "to inflict decisive defeat and humiliation on enemy forces",
        "hindi": "दुश्मन को बुरी तरह परास्त करना",
        "cultural_context": "Martial idiom common in Rajasthani hero epics and bardic chronicles.",
        "example": "हल्दीघाटी में वीरां मुगलां रा दांत खट्टे कियो।"
    },
    {
        "rajasthani": "गुड़ रो गोबर करणो",
        "roman": "gud ro gobar karno",
        "hindi": "बने-बनाए काम को नष्ट या विकृत कर देना",
        "english": "to ruin an otherwise sweet, harmonious or successful matter",
        "cultural_context": "Folk expression condemning reckless blunder.",
        "example": "क्रोध में आ'र उण सगळी बात रो गुड़ रो गोबर कर दियो।"
    },
    {
        "rajasthani": "आंख्यां रो तारो व्हैणो",
        "roman": "aankhyaan ro taaro hvaino",
        "english": "to be the beloved apple of someone's eye",
        "hindi": "अत्यंत प्रिय होना",
        "cultural_context": "Maternal affectionate idiom.",
        "example": "छोटो टाबर दादी री आंख्यां रो तारो है।"
    },
    {
        "rajasthani": "थाळी रो बैंगन व्हैणो",
        "roman": "thaali ro baingan hvaino",
        "english": "to be an unprincipled opportunist constantly rolling with the tide",
        "hindi": "बिना पेंदी का लोटा / अवसरवादी व्यक्ति",
        "cultural_context": "Critique of individuals lacking steadfast clan allegiance or moral spine.",
        "example": "उण रो कोई भरोसा कोनी, वो तो थाळी रो बैंगन है।"
    },
    {
        "rajasthani": "पेट में चूहा कूदणा",
        "roman": "pet mein chooha koodna",
        "english": "to experience intense, gnawing hunger",
        "hindi": "तीव्र भूख लगना",
        "cultural_context": "Common colloquial Rajasthani domestic phrase.",
        "example": "दिन भर रो भूखों म्हारे पेट में चूहा कूदै है।"
    },
    {
        "rajasthani": "चाक माथे माटी चढ़णी",
        "roman": "chaak maathe maati chadhni",
        "english": "to initiate life transformation, education, or formative training under master",
        "hindi": "जीवन का गढ़न व संस्कार आरंभ होना",
        "cultural_context": "Metaphor drawn from potter's chalk wheel giving shape to raw clay.",
        "example": "गुरु कनै जा'र शिष्य री माटी चाक माथे चढ़ी।"
    },
    {
        "rajasthani": "अंगूठो देखावणो",
        "roman": "angutho dekhaavno",
        "english": "to refuse point-blank at the crucial moment",
        "hindi": "ऐन वक्त पर साफ इनकार कर देना",
        "cultural_context": "Colloquial idiom denoting refusal of promised assistance.",
        "example": "मदद करण रो कह'र अंत में अंगूठो देखाय दियो।"
    }
]

i_added = 0
for ni in new_idioms:
    if ni["rajasthani"].strip() not in existing_idioms:
        idioms.append(ni)
        existing_idioms.add(ni["rajasthani"].strip())
        i_added += 1

with open(IDIOMS_PATH, "w", encoding="utf-8") as f:
    json.dump(idioms, f, ensure_ascii=False, indent=2)

print(f"Added {i_added} new idioms! Total idioms: {len(idioms)}")
