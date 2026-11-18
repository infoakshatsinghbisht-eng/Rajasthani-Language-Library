# -*- coding: utf-8 -*-
"""
Enrich Folklore: Proverbs (कहावतां), Riddles (आड़ी / पहेली), and Phrases
========================================================================
Expands proverbs, riddles, and daily conversational phrases from
classical Rajasthani folklore collections.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROV_FILE = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "proverbs.json")
RIDD_FILE = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "riddles.json")
PHRA_FILE = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "phrases.json")

# --- 1. PROVERBS ---
with open(PROV_FILE, "r", encoding="utf-8") as f:
    proverbs = json.load(f)
prov_set = {p["rajasthani"] for p in proverbs}

MORE_PROVERBS = [
    {
        "rajasthani": "घर रो जोगी जोगणो, आन गांव रो सिद्ध।",
        "roman": "Ghar ro jogi jogano, aan gaanw ro siddh.",
        "hindi": "घर का विद्वान उपेक्षित रहता है, पर पराए गांव का साधारण व्यक्ति भी आदर पाता है। (घर की मुर्गी दाल बराबर)",
        "english": "A prophet is never honored in his own village.",
        "cultural_context": "Pastoral skepticism of local pretension vs external reverence."
    },
    {
        "rajasthani": "आंगण तेवड़ो ही पसारिये, जितनी लाम्बी सौर।",
        "roman": "Aangan tevado hi pasaariye, jitni laambi saur.",
        "hindi": "उतने ही पैर पसारने चाहिए जितनी लंबी चादर हो।",
        "english": "Cut your coat according to your cloth; live strictly within your financial means.",
        "cultural_context": "Core financial and domestic prudence in the thrift of desert life."
    },
    {
        "rajasthani": "अककल बड़ी के भैंस?",
        "roman": "Akkal badi ke bhains?",
        "hindi": "बुद्धि बड़ी होती है या शारीरिक बल?",
        "english": "Is intellect mightier than brute physical strength?",
        "cultural_context": "Classic folk riddle on wisdom triumphing over brute force."
    },
    {
        "rajasthani": "दुबळो दीखे पण दाव घणो।",
        "roman": "Dublo deekhe pan daav ghano.",
        "hindi": "दिखने में दुबला-पतला है पर चाल और ताकत में बहुत माहिर है।",
        "english": "Deceptively frail in appearance, but wielding formidable skill and cunning.",
        "cultural_context": "Warning against underestimating quiet or slender competitors."
    },
    {
        "rajasthani": "खाय'र पीटो, रोय'र डीटो।",
        "roman": "Khaay'r peeto, roy'r deeto.",
        "hindi": "पेट भरकर खाने से तृप्ति होती है, और दिल खोलकर रोने से मन का बोझ उतरता है।",
        "english": "A hearty meal satisfies the body, and honest tears release the sorrow of the soul.",
        "cultural_context": "Deep emotional and practical psychology in Marwari folk living."
    },
    {
        "rajasthani": "जेठ महीने लू चालै, भादवे मेह न्हाळै।",
        "roman": "Jeth maheene loo chaalai, bhaadve meh nhaalai.",
        "hindi": "यदि जेठ माह में प्रचंड लू चले, तो भाद्रपद में भरपूर वर्षा होती है।",
        "english": "Intense desert heat in May-June guarantees copious monsoon rains in August.",
        "cultural_context": "Traditional weather lore derived from centuries of desert farming observation."
    },
    {
        "rajasthani": "ऊँट री दाढ़ी मांय जीरो।",
        "roman": "Oont ri daadhi maany jeero.",
        "hindi": "ऊँट के मुंह में जीरा (अत्यंत अपर्याप्त मात्रा)।",
        "english": "A cumin seed in a camel's beard; a drop in the ocean.",
        "cultural_context": "Humorous desert expression for a hopelessly minuscule portion."
    },
    {
        "rajasthani": "धी खासी तो ब्याई लासी।",
        "roman": "Dhee khaasi to byaai laasi.",
        "hindi": "यदि कन्या खाएगी तो ससुराल वाले लाएंगे (बेटी और दामाद का स्वाभाविक संबंध)।",
        "english": "What is nurtured in the daughter will be cherished and provided by the in-laws.",
        "cultural_context": "Affectionate reflection on matrimonial hospitality."
    },
    {
        "rajasthani": "काग बोलै मुंडेर माथे, पाहुणा आवेला।",
        "roman": "Kaag bolai munder maathe, paahuna aavela.",
        "hindi": "छत की मुंडेर पर कौआ बोले तो घर में मेहमान आते हैं।",
        "english": "When a crow calls on the parapet, honored guests are on their way.",
        "cultural_context": "Universal folklore omen announcing joyful visitor arrivals."
    },
    {
        "rajasthani": "मारवाड़ मांय पाणी अर धी कदे नीं वेचीजै।",
        "roman": "Maarwaad maany paani ar dhee kade neen vecheejai.",
        "hindi": "मारवाड़ में पानी और बेटी को कभी बेचा नहीं जाता (परम सम्माननीय मर्यादा)।",
        "english": "In Marwar, sacred water and one's daughter are never bartered or sold.",
        "cultural_context": "The moral bedrock of Marwari chivalry, water hospitality, and familial honor."
    },
    {
        "rajasthani": "घणो मीठो हुवै तो खा जावै, घणो कड़वो हुवै तो थूक देवै।",
        "roman": "Ghano meetho huvai to khaa jaavai, ghano kadvo huvai to thook devai.",
        "hindi": "अति मीठा बनोगे तो लोग खा जाएंगे, अति कड़वे बनोगे तो लोग थूक देंगे।",
        "english": "If you are excessively submissive, people consume you; if excessively harsh, they cast you out.",
        "cultural_context": "Balanced pragmatism and firm self-respect in social life."
    },
    {
        "rajasthani": "जागे सो पावै, सोवे सो खोवै।",
        "roman": "Jaage so paavai, sove so khovai.",
        "hindi": "जो जागता है वह पाता है, जो सोता है वह खोता है।",
        "english": "The vigilant prosper, while the slumbering suffer loss.",
        "cultural_context": "Work ethic and alertness required for desert survival."
    }
]

for p in MORE_PROVERBS:
    if p["rajasthani"] not in prov_set:
        proverbs.append(p)
        prov_set.add(p["rajasthani"])

with open(PROV_FILE, "w", encoding="utf-8") as f:
    json.dump(proverbs, f, ensure_ascii=False, indent=2)

print(f"Total proverbs now: {len(proverbs)}")

# --- 2. RIDDLES ---
with open(RIDD_FILE, "r", encoding="utf-8") as f:
    riddles = json.load(f)
ridd_set = {r["riddle"] for r in riddles}

MORE_RIDDLES = [
    {
        "riddle": "हरी थी मन भरी थी, मोती जड़ी थी। राजाजी रे बाग मांय दुशाला ओढ़'र खड़ी थी।",
        "roman": "Hari thi man bhari thi, moti jadi thi. Raajaaji re baag maany dushaala odh'r khadi thi.",
        "hindi": "हरी थी, मन भरी थी, लाख मोतियों से जड़ी थी। राजाजी के बाग में दुशाला ओढ़े खड़ी थी।",
        "english": "I was green and full, studded with pearls. In the king's garden I stood draped in a shawl. What am I?",
        "answer_rajasthani": "भुट्टो / मक्की रो सिट्टो",
        "answer_hindi": "भुट्टा / मक्के की बाली",
        "answer_english": "Ear of Corn / Maize cob",
        "category": "agriculture"
    },
    {
        "riddle": "गोल मटोल मुखड़ो, भीतर भरी मिश्री। खावै राजा, खावै परजा, स्वाद लागै मीठो।",
        "roman": "Gol matol mukhado, bheetar bhari mishri. Khaavai raaja, khaavai parja, swaad laagai meetho.",
        "hindi": "गोल मटोल चेहरा, भीतर मीठा रस। राजा भी खाते हैं और प्रजा भी।",
        "english": "Round and plump, filled with sweet crystalline sugar inside, relished by kings and peasants alike. What am I?",
        "answer_rajasthani": "मतीलड़ी / मतीरो (कालींगड़ो)",
        "answer_hindi": "मतीरा / तरबूज",
        "answer_english": "Desert Watermelon (Mateera)",
        "category": "nature"
    },
    {
        "riddle": "एक थाल मोतियां सूं भरियो, सबके सिर माथे औंधो धरियो। चारों कानी थाल फिरै, मोती उस सूं एक न गिरै।",
        "roman": "Ek thaal motiyaan soon bhariyo, sabke sir maathe aundho dhariyo. Chaaron kaani thaal phirai, moti us soon ek na girai.",
        "hindi": "एक थाली मोतियों से भरी, सबके सिर पर उल्टी रखी है। थाली घूमती है पर एक भी मोती नीचे नहीं गिरता।",
        "english": "A platter laden with pearls, held upside down above everyone's head; the platter turns, yet not a pearl falls. What is it?",
        "answer_rajasthani": "तारों भरियो आकास",
        "answer_hindi": "तारों भरा आकाश / नभ",
        "answer_english": "The Starry Night Sky",
        "category": "nature"
    },
    {
        "riddle": "काठ री घोड़ी, लोहे री लगाम। जो बैठे, वो उतरे नहीं।",
        "roman": "Kaath ri ghodi, lohe ri lagaam. Jo baithe, vo utre nahin.",
        "hindi": "काठ की घोड़ी, लोहे की लगाम। जो बैठे, वह उतरे नहीं।",
        "english": "A mare of wood, reins of iron; whoever mounts never dismounts alive.",
        "answer_rajasthani": "बैकुंठ / अर्थी",
        "answer_hindi": "अर्थी / जनाजा",
        "answer_english": "Funeral bier",
        "category": "culture"
    },
    {
        "riddle": "सांप री ज्यूं लपेटां खावै, धोरां मांय सूं मारग काढ़ै।",
        "roman": "Saanp ri jyoon lapetaan khaavai, dhoraan maany soon maarag kaadhai.",
        "hindi": "सांप की तरह बलखाती है, धोरों के बीच से रास्ता बनाती है।",
        "english": "Winding like a serpent, carving a path through the rolling dunes. What is it?",
        "answer_rajasthani": "पगडंडी / रेगिस्तानी डगर",
        "answer_hindi": "पगडंडी / रास्ता",
        "answer_english": "Desert foot-track / bridle path",
        "category": "nature"
    },
    {
        "riddle": "दो भाई हैं, एक रंग एक रूप, पण जद चलै तो एक आगै अर एक पाछै।",
        "roman": "Do bhaai hain, ek rang ek roop, pan jad chalai to ek aagai ar ek paachhai.",
        "hindi": "दो भाई हैं, एक जैसे रंग-रूप के, लेकिन जब चलते हैं तो एक आगे और एक पीछे रहता है।",
        "english": "Two brothers of identical form and color; yet whenever they walk, one is ahead and one behind. What are they?",
        "answer_rajasthani": "पगां री मोजड़ियां / जूता",
        "answer_hindi": "जूते / मोजड़ी",
        "answer_english": "Pair of Mojaris / Shoes",
        "category": "clothing"
    }
]

for r in MORE_RIDDLES:
    if r["riddle"] not in ridd_set:
        riddles.append(r)
        ridd_set.add(r["riddle"])

with open(RIDD_FILE, "w", encoding="utf-8") as f:
    json.dump(riddles, f, ensure_ascii=False, indent=2)

print(f"Total riddles now: {len(riddles)}")

# --- 3. PHRASES ---
with open(PHRA_FILE, "r", encoding="utf-8") as f:
    phrases = json.load(f)
phra_set = {p["rajasthani"] for p in phrases}

MORE_PHRASES = [
    {
        "rajasthani": "जीमबा पधारो सा!",
        "roman": "Jeemba padhaaro sa!",
        "hindi": "भोजन करने पधारिए सा!",
        "english": "Please grace us and come feast!",
        "category": "hospitality",
        "dialect": "general"
    },
    {
        "rajasthani": "खम्मा घणी, हुकम सा!",
        "roman": "Khamma ghani, hukam sa!",
        "hindi": "अत्यंत आदरपूर्वक नमस्कार, महाराज/श्रीमान!",
        "english": "Abundant greetings, noble lord/sir!",
        "category": "greetings",
        "dialect": "general"
    },
    {
        "rajasthani": "थारो घणो-घणो आभार सा।",
        "roman": "Thaaro ghano-ghano aabhaar sa.",
        "hindi": "आपका बहुत-बहुत आभार सा।",
        "english": "Heartfelt and immense gratitude to you.",
        "category": "etiquette",
        "dialect": "general"
    },
    {
        "rajasthani": "आनंद मांय रहो सा।",
        "roman": "Aanand maany raho sa.",
        "hindi": "सदा आनंद में रहिए सा।",
        "english": "May you abide in perpetual bliss and joy.",
        "category": "blessings",
        "dialect": "general"
    },
    {
        "rajasthani": "पाणी पीवो सा, छाया मांय विराजो।",
        "roman": "Paani peevo sa, chhaaya maany viraajo.",
        "hindi": "पानी पीजिए सा, छाया में बैठिए।",
        "english": "Have some cool water, please take your seat in the cool shade.",
        "category": "hospitality",
        "dialect": "general"
    },
    {
        "rajasthani": "धीरज राखो, सगळो काम चोखो व्हैला।",
        "roman": "Dheeraj raakho, sagalo kaam chokho vhaila.",
        "hindi": "धैर्य रखिए, सब काम अच्छा होगा।",
        "english": "Keep patience, everything will turn out splendidly.",
        "category": "conversation",
        "dialect": "general"
    },
    {
        "rajasthani": "काले फेर म्हे भेळा व्हैस्यां।",
        "roman": "Kaale pher mhe bhela vhaisyaan.",
        "hindi": "कल फिर हम सब इकट्ठा मिलेंगे।",
        "english": "Tomorrow we shall all gather together again.",
        "category": "parting",
        "dialect": "general"
    }
]

for p in MORE_PHRASES:
    if p["rajasthani"] not in phra_set:
        phrases.append(p)
        phra_set.add(p["rajasthani"])

with open(PHRA_FILE, "w", encoding="utf-8") as f:
    json.dump(phrases, f, ensure_ascii=False, indent=2)

print(f"Total phrases now: {len(phrases)}")
