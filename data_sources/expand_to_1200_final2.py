# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

WORDS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "rajasthani", "lexicon", "data", "words.json")
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip() for w in words}

EXTRA_TERMS = [
    ("राउ", "raau", "ancient sovereign royal title of Rathore kings of Bikaner and Marwar", "राव (राजा / शासक)", "noun", "m", "history", "mwr", "राउ जेतासी बाबर रै बेटे कामरान नै हराया।"),
    ("खंग", "khang", "heavy curved battle-sword of medieval knights", "खड़्ग / तलवार", "noun", "m", "weapons", "mwr", "हाथ में खंग ले'र वीर लड्यो।"),
    ("दल", "dal", "military army battalion or marching host", "सेना / कटक / लश्कर", "noun", "m", "history", "mwr", "किले रै कांकड़ दल आयो।"),
    ("कटक", "katak", "grand royal military encampment", "सैन्य छावनी / कटक", "noun", "m", "history", "mwr", "नदी किनारे कटक ठहऱ्यो।"),
    ("अर", "ar", "and / conjunction joining phrases in traditional literature", "और / तथा", "conjunction", None, "conjunctions", "mwr", "राम अर लखमण दोई भाई।"),
    ("पण", "pan", "but / however / yet", "किंतु / परंतु / लेकिन", "conjunction", None, "conjunctions", "mwr", "म्हैं गयो पण वो नीं मिल्यो।"),
    ("जदपि", "jadapi", "even though / although", "यद्यपि / हालांकि", "conjunction", None, "conjunctions", "mwr", "जदपि कष्ट भारी थो, पण धीरज नीं छोड़्यो।"),
    ("तदपि", "tadapi", "nevertheless / even then", "तथापि / फिर भी", "conjunction", None, "conjunctions", "mwr", "तदपि वो सच बोल्यो।"),
    ("कांई", "kaani", "what / interrogative particle", "क्या (प्रश्नवाचक)", "pronoun", None, "interrogative", "mwr", "थारो नांव कांई है?"),
    ("किणी", "kini", "anyone / someone / oblique indefinite pronoun", "किसी / कोई", "pronoun", None, "pronouns", "mwr", "किणी नै दुःख मती देवो।"),
    ("जिणी", "jini", "the one who / relative pronoun oblique", "जिसने / जिसे", "pronoun", None, "pronouns", "mwr", "जिणी सत्य कह्यो, वो तर ग्यो।"),
    ("तिणी", "tini", "that one / correlative pronoun oblique", "उसने / उसे", "pronoun", None, "pronouns", "mwr", "तिणी काम पूरो कियो।"),
    ("अठै", "athai", "here / at this place", "यहाँ / इस स्थान पर", "adverb", None, "adverbs", "mwr", "अठै विराजो सा।"),
    ("वठै", "vathai", "there / at that distant place", "वहाँ / उस स्थान पर", "adverb", None, "adverbs", "mwr", "वठै घणो मेलो भरै।"),
    ("जठै", "jathai", "where / relative spatial adverb", "जहाँ", "adverb", None, "adverbs", "mwr", "जठै साच है, वठै विजय है।"),
    ("कतै", "katai", "somewhere / anywhere", "कहीं", "adverb", None, "adverbs", "mwr", "कतै पाणी नीं दीखै।"),
    ("कितै", "kitai", "where? / interrogative place adverb", "कहाँ? / किधर?", "adverb", None, "interrogative", "mwr", "थे कितै चाल्या?"),
    ("इब", "ib", "now / currently (in modern time)", "अब / इस समय", "adverb", None, "time", "mwr", "इब घर चालो।"),
    ("तद", "tad", "then / at that historic moment", "तब / उस समय", "adverb", None, "time", "mwr", "तद राजा हुकम दियो।"),
    ("कद", "kad", "when? / interrogative temporal adverb", "कब?", "adverb", None, "interrogative", "mwr", "मेह कद बरससी?"),
    ("जद", "jad", "when / relative temporal adverb", "जब", "adverb", None, "time", "mwr", "जद सूरज ऊगै, तद उजाळो व्है।"),
    ("इम", "im", "thus / in this manner", "इस प्रकार / ऐसे", "adverb", None, "descriptors", "mwr", "इम विचार'र वो चाल पड़्यो।"),
    ("जिम", "jim", "as / like / relative manner adverb", "जैसे / जिस तरह", "adverb", None, "descriptors", "mwr", "जिम कह्यो, तिम कियो।"),
    ("तिम", "tim", "so / in that same manner", "तैसे / उस तरह", "adverb", None, "descriptors", "mwr", "तिम ही फल मिल्यो।"),
    ("किशोरी", "kishori", "young maiden or princess in court poetry", "किशोरी / सुकुमारी", "noun", "f", "literature", "mwr", "किशोरी सखियां सागै उपवन में आई।"),
    ("नवलखी", "navlakhi", "priceless, worth nine hundred thousand gold mohurs", "नौलखा / अमूल्य", "adjective", "f", "descriptors", "mwr", "गळे में नवलखी हार चमकै।"),
    ("कमळ", "kamal", "sacred pink lotus blossoming in desert temple ponds", "कमल / पद्म", "noun", "m", "flora", "mwr", "सरोवर में कमळ खिल्यो।"),
    ("अंब", "amb", "mango fruit or maternal mother in Dingal verse", "आम / माता", "noun", "m", "flora", "mwr", "मीठा अंब वृक्ष सूं टपकै।"),
    ("भंवर", "bhanwar_bee", "black bumblebee humming over forest blooms", "भौंरा / भ्रमर", "noun", "m", "fauna", "mwr", "कमल माथे भंवर मंडरायो।"),
    ("कोयल", "koyal", "sweet-voiced cuckoo singing in mango groves in spring", "कोयल (मधुर कंठ)", "noun", "f", "fauna", "mwr", "आम री डाली माथे कोयल कूकै।"),
    ("हंस", "hans", "pure white royal swan separating milk from water in proverbs", "हंस (नीर-क्षीर विवेकी पक्षी)", "noun", "m", "fauna", "mwr", "हंस मोती चुगै।"),
    ("नाग", "naag", "sacred cobra serpent worshipped on Goga Navami and Nag Panchami", "नाग देवता / सर्प", "noun", "m", "fauna", "mwr", "गोगाजी नाग देवता रा स्वामी हैं।"),
    ("गौ", "gau", "sacred cow, mother of pasture and agricultural wealth", "गौ माता", "noun", "f", "fauna", "mwr", "गौ सेवा सूं मोटो पुन व्है।"),
    ("अश्व", "ashwa", "noble war horse bred in Malani or Marwar", "अश्व / घोड़ा", "noun", "m", "animals", "mwr", "मालाणी अश्व री चाल विश्व विख्यात है।"),
    ("गजराज", "gajraaj", "mighty royal elephant mounted in royal processions", "गजराज / ऐरावत", "noun", "m", "animals", "mwr", "किले सूं गजराज री सवारी निकळी।"),
    ("केसरी", "kesari", "valiant roaring lion / courageous heroic king", "सिंह / केसरी", "noun", "m", "animals", "mwr", "रणखेत में केसरी ज्यूं लड्यो।"),
    ("नाहर", "naahar", "tiger or desert leopard stalking through Aravali ravines", "बाघ / नाहर", "noun", "m", "animals", "mwr", "अरावली री खोह में नाहर गरज्यो।"),
    ("बरछी", "barchhi", "slender throwing dart or short battle spear", "बरछी (लघु भाला)", "noun", "f", "weapons", "mwr", "बरछी सूं शत्रु रो वार रोक्यो।"),
    ("तीर-कमाण", "teer-kamaan", "traditional bamboo bow and barbed iron arrow of Bhil archers", "धनुष-बाण (तीर-कमान)", "noun", "m", "weapons", "mwr", "भील योद्धा तीर-कमाण में निपुण हा।"),
    ("तोप", "top", "heavy siege cannon mounted atop fort bastions (e.g. Jaivana)", "तोप (आग्नेयास्त्र)", "noun", "f", "weapons", "mwr", "जयगढ़ री जयबाण तोप एशिया री सबसूं बड़ी तोप है।"),
    ("गोलो", "golo", "heavy cast-iron cannonball fired against enemy ramparts", "तोप का गोला", "noun", "m", "weapons", "mwr", "तोप सूं लोहे रो गोलो छूट्यो।"),
    ("बारूद", "baarood", "black gunpowder manufactured in fort magazines", "बारूद", "noun", "f", "weapons", "mwr", "किले में बारूद सुरक्षित मेल्यो।"),
    ("मोर्चा", "morcha", "defensive military entrenchment or battlement outpost", "मोर्चा (युद्ध की चौकी)", "noun", "m", "history", "mwr", "सूरमां मोर्चे माथे डट गया।"),
    ("पराक्रम", "paraakram", "heroic prowess, bravery, and martial valor", "पराक्रम / शौर्य", "noun", "m", "values", "mwr", "महाराणा प्रताप रो पराक्रम युग-युग तक याद रहसी।")
]

added = 0
for item in EXTRA_TERMS:
    r, rom, eng, hin, pos, gen, cat, dia, ex = item
    key = r.strip()
    if key not in existing:
        words.append({
            "rajasthani": r,
            "roman": rom,
            "english": eng,
            "hindi": hin,
            "pos": pos,
            "gender": gen,
            "category": cat,
            "dialect": dia,
            "example": ex
        })
        existing.add(key)
        added += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Added {added} extra terms! Grand total lexicon now: {len(words)}")
