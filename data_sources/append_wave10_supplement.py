# -*- coding: utf-8 -*-
"""Append Wave 10 supplementary vocabulary to words.json."""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip(): w for w in words}

items = [
    ("उमराव", "umraav", "hereditary noble of the highest royal rank in Mewar/Marwar", "सर्वोच्च सामंत अथवा उमराव", "noun", "masculine", "history", "general", "उमराव दरबार मांय राजाजी रै दाबै-जीवणै बैठता।"),
    ("बक्शी", "bakhshi", "paymaster and military administrator of the royal forces", "सैन्य प्रशासक अथवा बख्शी", "noun", "masculine", "history", "general", "बक्शी जी सैनिकां रो वेतन चुकायो।"),
    ("कोतवाल", "kotwaal", "chief police officer and warden of a fortified city", "नगर रक्षक अथवा कोतवाल", "noun", "masculine", "history", "general", "कोतवाल रात नै नगर मांय गश्त लगावै।"),
    ("फौजदार", "phaujdaar", "military garrison commander of a fortress or district", "दुर्ग का सैन्य अधिकारी", "noun", "masculine", "history", "general", "फौजदार किले री सुरक्षा रो जिम्मो लियो।"),
    ("हरकारो", "harkaaro", "royal courier or post runner delivering state dispatches", "डाकिया अथवा संदेशवाहक", "noun", "masculine", "history", "marwari", "हरकारो राजाजी रो गुप्त फरमान लेय आयो।"),
    ("दरोगा", "daroga", "superintendent of royal karkhanas or departments", "विभागाध्यक्ष अथवा दरोगा", "noun", "masculine", "history", "general", "दरोगा तोपखाने री व्यवस्था जांची।"),
    ("खजांची", "khajaanchi", "custodian of the royal treasury and jewels", "कोषाध्यक्ष", "noun", "masculine", "history", "general", "खजांची तिजोरी रो हिसाब पेश कर्यो।"),
    ("चोबदार", "chobdaar", "royal herald carrying gold/silver staff announcing royal entry", "छड़ीदार अथवा चोबदार", "noun", "masculine", "history", "general", "चोबदार महाराज रै आगमन री घोषणा करी।"),
    ("खवास", "khawaas", "trusted personal royal aide or court attendant", "विश्वस्त सेवक अथवा खवास", "noun", "masculine", "history", "marwari", "खवास हुकम रो चंवर डुलायो।"),
    ("रूमाल", "roomaal", "embroidered cotton or silk kerchief", "रूमाल", "noun", "masculine", "attire", "general", "जेब मांय बंधेज रो रूमाल राख्यो।"),
    ("दुपट्टो", "dupatto", "light fine cotton scarf or mantle", "दुपट्टा", "noun", "masculine", "attire", "general", "गले मांय गुलाबी दुपट्टो सोभै।"),
    ("लोई", "loi", "soft fine woolen desert shawl", "ऊन की शाल अथवा लोई", "noun", "feminine", "attire", "marwari", "सियाळै मांय बीकानेरी लोई ओढ़ी।"),
    ("खेस", "khes", "heavy textured jacquard hand-woven cotton blanket of Jalore", "मोटा सूती चादर अथवा खेस", "noun", "masculine", "attire", "general", "जालोर रो खेस देसावर मांय मशहूर है।"),
    ("रजाई", "rajaai", "feather-light hand-quilted cotton quilt of Jaipur", "जयपुरी रजाई", "noun", "feminine", "household", "general", "जयपुर री पाव भर री रजाई घणी न्यान देवे।"),
    ("गद्दो", "gaddo", "cotton-stuffed soft floor mattress", "बिछौना अथवा गद्दा", "noun", "masculine", "household", "general", "बैठक मांय नरम गद्दो बिछायो।"),
    ("तकियो", "takiyo", "bolster pillow supporting royal guests (Gaotakiya)", "गोल तकिया अथवा गावतकिया", "noun", "masculine", "household", "general", "दीवान पर तकियो लगाय बैठ्या।"),
    ("गालीचो", "gaaleecho", "hand-knotted woolen pile carpet of Jaipur and Bikaner", "हाथ से बना कालीन अथवा गलीचा", "noun", "masculine", "crafts", "general", "महल मांय ईरानी डिजाइन रो गालीचो बिछ्यो।"),
    ("थाळी", "thaali", "broad rimmed silver or brass dining platter", "कांस्य अथवा पीतल की थाली", "noun", "feminine", "household", "marwari", "थाळी मांय चूरमो-बाटी परोसी।"),
    ("लोटो", "loto", "traditional round brass water vessel", "पीतल का लोटा", "noun", "masculine", "household", "general", "तांबे रै लोटे मांय पाणी भरयो।"),
    ("कटोरी", "katori", "small brass or silver curry bowl", "कटोरी", "noun", "feminine", "household", "general", "कटोरी मांय दही परोसी।"),
    ("चमचो", "chamcho", "spoon for serving ghee or lentils", "चम्मच", "noun", "masculine", "household", "general", "चमचे सूं घी नाख्यो।"),
    ("तपेली", "tapeli", "deep flat-bottomed boiling vessel", "पतीली अथवा तपेली", "noun", "feminine", "household", "general", "तपेली मांय दूध उफन्यो।"),
    ("भगोणी", "bhagoni", "wide cooking cauldron", "भगोना", "noun", "feminine", "household", "general", "भगोणी मांय खीर बणाई।"),
    ("कड़छी", "kadachhi", "long-handled ladle for stirring stews", "कड़छी अथवा चमचा", "noun", "feminine", "tools", "general", "कड़छी सूं दाल हिलाई।"),
    ("परात", "paraat", "large wide brass basin for kneading millet flour", "आटा गूंथने की परात", "noun", "feminine", "household", "general", "परात मांय बाजरी रो आटो लगायो।"),
    ("गागर", "gaagar", "polished spherical brass water pitcher", "पीतल की गागर", "noun", "feminine", "household", "general", "सिर पर गागर धर'र पणिहारी चालै।"),
    ("कलश", "kalash", "sacred copper or brass pot crowned with coconut and mango leaves", "मांगलिक कलश", "noun", "masculine", "rituals", "general", "गृह प्रवेश पर कलश स्थापित कर्यो।"),
    ("झारी", "jhaari", "spouted water flagon used in royal courts and temples", "टोंटीदार पात्र अथवा झारी", "noun", "feminine", "household", "general", "झारी सूं हाथ धुलाया।"),
    ("संदूक", "sandook", "heavy brass-bound teak chest holding dowry and family jewels", "बड़ा बक्सा अथवा संदूक", "noun", "masculine", "household", "general", "संदूक मांय सोने रा आभूषण सम्भाळ्या।"),
    ("पिटारो", "pitaaro", "woven cane or leather chest storing wedding garments", "कपड़े रखने का पिटारा", "noun", "masculine", "household", "general", "लाड़ी रो पिटारो सासरै पुग्यो।"),
    ("हल्दी", "haldhi", "golden medicinal turmeric rhizome auspicious in all rituals", "हल्दी", "noun", "feminine", "food", "general", "विवाह मांय पीठी मांय हल्दी घोळी।"),
    ("धनिया", "dhaniya", "fragrant whole and ground coriander seeds", "धनिया मसाला", "noun", "masculine", "food", "general", "सब्जी मांय पिसेड़ो धनिया नाख्यो।"),
    ("राई", "raai", "tiny pungent black mustard seeds for tempering dishes", "राई मसाला", "noun", "feminine", "food", "general", "घी मांय राई रो छौंक लगायो।"),
    ("मेथी", "methi", "golden bitter fenugreek seeds used in pickles and curries", "दाना मेथी", "noun", "feminine", "food", "general", "पापड़-मेथी री तरकारी घणी सवादी बणै।"),
    ("कलौंजी", "kalaunji", "black aromatic nigella onion seeds seasoning pickles", "कलौंजी", "noun", "feminine", "food", "general", "अचार मांय कलौंजी नाखी।"),
    ("सौंफ", "saunph", "sweet green aromatic fennel seeds offered after meals", "मीठी सौंफ", "noun", "feminine", "food", "general", "जीमण पछै मिश्री साथै सौंफ मनवारी।"),
    ("तेजपात", "tejpaat", "fragrant bay leaves enhancing royal stews", "तेजपत्ता", "noun", "masculine", "food", "general", "पुलाव मांय तेजपात नाख्यो।"),
    ("दालचीनी", "daalcheeni", "sweet aromatic rolled cinnamon bark", "दालचीनी", "noun", "feminine", "food", "general", "मसालेदार चाय मांय दालचीनी कूट'र नाखी।"),
    ("जायफल", "jaayaphal", "fragrant whole nutmeg grated into royal sweets and lapsi", "जायफल", "noun", "masculine", "food", "general", "लापसी मांय जायफल रो चूर्ण मिलायो।"),
    ("जावित्री", "jaavitri", "lacy mace aril imparting sublime fragrance to royal dishes", "जावित्री", "noun", "feminine", "food", "general", "जावित्री री महक पकवान मांय समागी।"),
    ("काली मिरच", "kaali mirach", "black peppercorns prized in ancient trade", "काली मिर्च", "noun", "feminine", "food", "general", "काढ़ै मांय काली मिरच नाखी।"),
    ("सेंधा लूण", "sendha loon", "pure pink rock salt favored during sacred fasts", "सेंधा नमक", "noun", "masculine", "food", "general", "व्रत मांय सेंधा लूण खाईजै।"),
    ("सूंठ", "soonth", "sun-dried ginger powder warming body in desert winter", "सूखा अदरक अथवा सोंठ", "noun", "feminine", "food", "general", "सर्दियां मांय सूंठ रा लाडू बणाय खवाया।"),
    ("पिस्ता", "pista", "green pistachio nut slivers garnishing ghevars and kheer", "पिस्ता मेवा", "noun", "masculine", "food", "general", "घेवर माथै पिस्ता री कतरन सजाई।"),
    ("बादाम", "baadaam", "rich almond nuts pounded into festive winter halwa", "बादाम", "noun", "masculine", "food", "general", "सवेरै दूध साथै बादाम लीधा।"),
    ("काजू", "kaajoo", "rich cashew nuts roasted in pure cow ghee", "काजू", "noun", "masculine", "food", "general", "काजू रो हलवो बणायो।"),
    ("किशमिश", "kishmish", "golden sun-dried raisins folded into sweet lapsi", "किशमिश", "noun", "feminine", "food", "general", "खीर मांय किशमिश नाखी।"),
    ("दाख", "daakh", "sweet dried green grape or currant", "दाख अथवा मुनक्का", "noun", "feminine", "food", "marwari", "वैदजी दाख खाबा री सलाह दीनी।"),
    ("टीलो", "teelo", "prominent hillock or isolated ridge", "रेत का टीला अथवा टीबड़ा", "noun", "masculine", "geography", "marwari", "टीले माथै सूं सूर्योदय देख्यो।"),
    ("घाटी", "ghaati", "narrow mountain pass between Aravalli crags (Naal)", "पहाड़ी दर्रा अथवा घाटी", "noun", "feminine", "geography", "general", "हल्दीघाटी रो युद्ध इतिहास मांय अमर है।"),
    ("दर्रो", "darro", "defensive pass cut through rugged hills", "दर्रा अथवा नाल", "noun", "masculine", "geography", "general", "पहाड़ रो संकरो दर्रो पार कर्यो।"),
    ("गुफा", "gupha", "subterranean cavern sheltering meditating hermits", "पहाड़ी कंदरा अथवा गुफा", "noun", "feminine", "geography", "general", "गुफा मांय योगी तपस्या करै हा।"),
    ("खड", "khad", "deep ravine or cleft carved by seasonal torrents", "गहरी खाई अथवा खड्ड", "noun", "masculine", "geography", "general", "पहाड़ रै किनारे गहरी खड ही।"),
    ("झरनो", "jharno", "crystal waterfall leaping down rocky cliffs during monsoons", "प्राकृतिक जल प्रपात", "noun", "masculine", "nature", "general", "मेनाल रो झरनो वर्षा ऋतु मांय घणो सोहणो दीसै।"),
    ("सरोवर", "sarovar", "sacred lake fringed by marble ghats (like Pushkar Lake)", "पवित्र झील अथवा सरोवर", "noun", "masculine", "water", "general", "पुष्कर सरोवर मांय कार्तिक पूनम नै स्नान कर्यो।"),
    ("पोखर", "pokhar", "village natural water pond sustaining desert birds and herds", "छोटा तालाब अथवा पोखर", "noun", "masculine", "water", "general", "पोखर रै तीरे पशु पाणी पीवै।"),
    ("झील", "jheel", "placid lake mirroring palaces and blue skies (e.g. Pichola)", "प्राकृतिक अथवा कृत्रिम झील", "noun", "feminine", "water", "general", "पिछोला झील मांय जलमहल री परछाईं दीसै।"),
    ("नदी", "nadi", "flowing river (like Chambal, Banas, Luni)", "नदी अथवा सरिता", "noun", "feminine", "water", "general", "लूणी नदी थार मांय बह्वै।"),
    ("तळाव", "talaav", "community reservoir secured by stone dam and ghats", "तालाब", "noun", "masculine", "water", "marwari", "तळाव री पाळ पर पीपल री छांव है।"),
    ("कुंड", "kund", "masonry water pool built inside fort courtyards", "पत्थर का पक्का जल कुंड", "noun", "masculine", "water", "general", "किले रै कुंड मांय वर्षा रो पाणी संचित रह्वै।"),
    ("नेकी", "neki", "goodness, benevolence, virtuous moral conduct", "सत्कर्म अथवा भलाई", "noun", "feminine", "values", "general", "नेकी कर दरिया मांय डाल।"),
    ("भलाई", "bhalaai", "altruistic benevolence, well-being of all beings", "परोपकार अथवा हित", "noun", "feminine", "values", "general", "दूसरां री भलाई करण सूं मन शांत रह्वै।"),
    ("दया", "daya", "compassion, tender mercy toward all suffering souls", "करुणा अथवा दया", "noun", "feminine", "values", "general", "जीव-जंतुवां पर दया राखो।"),
    ("कृपा", "kripa", "divine grace, unearned benevolence", "ईश्वर की कृपा", "noun", "feminine", "values", "general", "भगवान री कृपा सूं सारो काम सिद्ध होयो।"),
    ("करुणा", "karuna", "deep spiritual sympathy, loving kindness", "करुणा", "noun", "feminine", "values", "general", "संत रै हिये मांय प्राणी मात्र तांई करुणा ही।"),
    ("शांति", "shaanti", "inner tranquility, harmony, absence of conflict", "शांति अथवा अमन", "noun", "feminine", "values", "general", "घर मांय शांति अर प्रेम रहणो चाहीजै।"),
    ("संतोष", "santosh", "contentment, serene satisfaction with simple livelihood", "तृप्ति अथवा संतोष", "noun", "masculine", "values", "general", "संतोष धन सबसूं मोटो धन है।"),
    ("हिम्मत", "himmat", "intrepid fortitude facing desert storms and adversity", "साहस अथवा हिम्मत", "noun", "feminine", "values", "general", "संकट मांय हिम्मत नीं हारणी चाहीजै।"),
    ("उत्साह", "utsaah", "surging zeal, fervent energy embarking on noble tasks", "जोश अथवा उमंग", "noun", "masculine", "emotions", "general", "नया काम मांय भरपूर उत्साह दिखायो।"),
    ("आनंद", "aanand", "supreme spiritual bliss, untainted joy", "परम सुख अथवा आनंद", "noun", "masculine", "emotions", "general", "सत्संग सुण'र मन मांय आनंद छा गयो।"),
    ("मौज", "mauj", "carefree rejoicing, delight, exuberant good cheer", "मौज अथवा उल्लास", "noun", "feminine", "emotions", "marwari", "सावण मांय मरुधर रै लोगां री मौज रह्वै।"),
    ("मस्ती", "masti", "intoxication of devotional ecstasy or festive merriment", "उल्लास अथवा मस्ती", "noun", "feminine", "emotions", "general", "होळी रै रंग मांय सब मस्ती मांय झूम्है।"),
    ("उल्लास", "ullaas", "festive jubilant rejoicing filling communities", "उल्लास अथवा हर्ष", "noun", "masculine", "emotions", "general", "त्यौहार पर चारूं मेर उल्लास छायो।"),
    ("बहादुरी", "bahaaduri", "gallantry, valorous bravery in protecting weak", "शूरवीरता", "noun", "feminine", "chivalry", "general", "सैनिक री बहादुरी पर सरकार पदक दियो।"),
    ("समर्पण", "samarpan", "wholehearted selfless dedication to motherland or duty", "त्याग अथवा निष्ठा", "noun", "masculine", "values", "general", "मातृभूमि तांई पूरो जीवन समर्पण कर्यो।"),
    ("ईमानदारी", "eemaandaari", "scrupulous upright honesty in trade and word", "सत्यनिष्ठा अथवा ईमानदारी", "noun", "feminine", "values", "general", "व्यापार मांय ईमानदारी सबसूं बडी पूंजी है।"),
    ("सद्भाव", "sadbhaav", "communal fraternity, goodwill, mutual benevolence", "सद्भावना अथवा भाईचारा", "noun", "masculine", "social", "general", "सारे समाजां मांय आपसी सद्भाव बण्यो रह्यो।"),
    ("विद्वता", "vidwata", "erudite scholarly mastery over classical scriptures", "ज्ञान अथवा पांडित्य", "noun", "feminine", "education", "general", "पंडितजी री विद्वता रो सब आदर करता।"),
    ("सत्कार", "satkaar", "reverent hospitality shown to elders and wandering ascetics", "आदर-सत्कार", "noun", "masculine", "culture", "general", "दरवाजे आयै साधु रो भावपूर्ण सत्कार कर्यो।"),
    ("प्रणाम", "pranaam", "reverent bowing down touching feet in filial piety", "चरण स्पर्श अथवा नमस्कार", "noun", "masculine", "greetings", "general", "माता-पिता नै झुक'र प्रणाम कर्यो।"),
    ("आशीर्वाद", "aasheervaad", "blessing bestowed with divine love by elders", "शुभ आशीष", "noun", "masculine", "values", "general", "दादीजी रो आशीर्वाद सदां साथ रह्वै।"),
    ("सुकून", "sukoon", "peace of soul, restfulness after wandering dunes", "शांति अथवा चैन", "noun", "masculine", "emotions", "general", "घर आवतै ही मन नै सुकून मिल्यो।"),
    ("हर्ष", "harsh", "gladness, delight, radiant smiling joy", "हर्ष अथवा खुशी", "noun", "masculine", "emotions", "general", "शुभ समाचार सुण'र हर्ष फैल्यो।"),
    ("परमार्थ", "parmaarth", "selfless spiritual welfare of fellow beings", "परोपकार अथवा परमार्थ", "noun", "masculine", "values", "general", "परमार्थ खातर जीवन बिताना ही सार्थकता है।"),
    ("कर्तव्य", "kartavya", "moral allegiance, solemn bounden duty", "कर्तव्य", "noun", "masculine", "values", "general", "देश री रक्षा आपणो पैलो कर्तव्य है।"),
    ("प्रतिष्ठा", "pratishtha", "unblemished social stature, honor, dignity", "मान-सम्मान अथवा साख", "noun", "feminine", "values", "general", "कुल री प्रतिष्ठा माथै कोई दाग नीं लागण दियो।"),
    ("साख", "saakh", "credibility, commercial trust, high repute", "साख अथवा विश्वास", "noun", "feminine", "commerce", "marwari", "बाजार मांय व्यापारी री साख सबसूं बडी पूंजी है।"),
    ("वचन", "vachan", "sacred spoken pledge, inviolable word of honor", "प्रतिज्ञा अथवा वचन", "noun", "masculine", "values", "general", "रजपूत आपरा वचन पूरा करबा तांई सीस कटा देवे।"),
    ("निभा", "nibha", "steadfast fulfillment of pledge or relationship", "निभाना अथवा पालन", "noun", "masculine", "values", "general", "संकट मांय मित्र रो साथ निभायो।"),
    ("सुयश", "suyash", "flourishing renown won through righteousness", "उत्तम यश", "noun", "masculine", "values", "general", "सत्कर्म सूं सारै देस मांय सुयश फैल्यो।"),
    ("अमरता", "amarta", "enduring immortality in collective folk memory", "अमरत्व", "noun", "feminine", "values", "general", "त्याग सूं ही अमरता री प्राप्ति होवै।"),
    ("सहानुभूति", "sahaanubhooti", "gentle empathy sharing another sorrow", "हमदर्दी अथवा संवेदना", "noun", "feminine", "emotions", "general", "दुखी जन साथै सच्ची सहानुभूति जताई।"),
    ("उदारता", "udaarta", "broad-minded magnanimity, nobility of soul", "उदारता अथवा बड़प्पन", "noun", "feminine", "values", "general", "राजाजी री उदारता री चर्चा सब करता।"),
    ("धीरता", "dheerata", "stoic composure in tempestuous crisis", "धैर्य अथवा गंभीरता", "noun", "feminine", "values", "general", "विपत्ति मांय धीरता सूं निर्णय लीधो।"),
    ("वीरता", "veerta", "fearless martial heroism and chivalric valour", "शूरवीरता", "noun", "feminine", "chivalry", "general", "राजस्थान री धरती वीरता री पावन भूमि है।"),
    ("स्वाभिमान", "swaabhimaan", "unyielding self-respect, independent noble pride", "आत्मसम्मान", "noun", "masculine", "values", "general", "स्वाभिमान सूं जीणो ही सांचो जीवन है।"),
    ("सत्यनिष्ठा", "satyanishtha", "unfaltering integrity anchored in pure truth", "सत्य के प्रति निष्ठा", "noun", "feminine", "values", "general", "सत्यनिष्ठा सूं काम करण वाळो कदैई नीं डिगै।"),
    ("मातृभूमि", "maatribhoomi", "hallowed soil of the motherland", "मातृभूमि", "noun", "feminine", "values", "general", "मातृभूमि री रक्षा खातर वीरां प्राण न्योछावर कर्यो।"),
    ("पुण्यभूमि", "punyabhoomi", "sacred realm sanctified by saints and deities", "पवित्र तीर्थ भूमि", "noun", "feminine", "culture", "general", "राजस्थान वीरां अर संतां री पुण्यभूमि है।"),
    ("कर्मभूमि", "karmabhoomi", "sphere of action, duty, and noble endeavour", "कार्यक्षेत्र अथवा कर्मभूमि", "noun", "feminine", "values", "general", "मरुधरा ही म्हारै जीवन री कर्मभूमि है।")
]

added = 0
for r, rom, eng, hin, pos, g, cat, dia, ex in items:
    if r not in existing:
        words.append({
            "rajasthani": r,
            "roman": rom,
            "english": eng,
            "hindi": hin,
            "pos": pos,
            "gender": g,
            "category": cat,
            "dialect": dia,
            "example": ex
        })
        existing[r] = True
        added += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Added {added} words. Final total words: {len(words)}")
