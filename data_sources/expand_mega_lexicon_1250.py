# -*- coding: utf-8 -*-
"""
Expand Mega Lexicon to 1,250+ Highly Curated Entries
====================================================
Mined directly from:
1. Rajasthani Kahawat Kosh (Bhagirath Kanoria)
2. Chhanda Rau Jeta Si Ro (Vithu Sujo / Dr. Tessitori)
3. Parampra Dingal Kosh (Dr. Narayansingh Bhati)
4. Harji Ro Vyambalo & Rukamani Mangal (Padam Bhagat)
5. Narsi Mehta Ka Bada Mamera (Ram Ratan Darak)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

WORDS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "rajasthani", "lexicon", "data", "words.json")
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip() for w in words}
print(f"Existing words in database: {len(words)}")

BATCH_1250 = [
    # --- 1. Agrarian Land, Soil, Tenure & Traditional Weights/Measures ---
    ("बीघो", "bigho", "traditional land area measurement unit (approx 0.625 acre in Rajasthan)", "बीघा (कृषि भूमि का पारंपरिक माप)", "noun", "m", "measures", "mwr", "किसान रै कनै बीस बीघा जमीन है।"),
    ("बिस्वो", "biswo", "one-twentieth fraction of a bigha", "बिस्वा (बीघे का बीसवां भाग)", "noun", "m", "measures", "mwr", "दो बीघा दस बिस्वा खेत जोत्यो।"),
    ("रकबो", "rakbo", "total surveyed surface area of an agricultural parcel", "रकबा (खेत का कुल क्षेत्रफल)", "noun", "m", "agriculture", "mwr", "पटवारी खेत रो रकबो नाप्यो।"),
    ("सेर", "ser", "traditional unit of weight approx equal to 933 grams or 16 chhatanks", "सेर (लगभग एक किलोग्राम / सोलह छटांक)", "noun", "m", "measures", "mwr", "दुकान सूं पांच सेर खांड लीनी।"),
    ("मण", "man", "traditional large weight measure equal to 40 sers (approx 37.3 - 40 kg)", "मन (चालीस सेर का तौल)", "noun", "m", "measures", "mwr", "खलिहान में सौ मण बाजरी पैदा हुई।"),
    ("पसेरी", "paseri", "five-ser weight measure used in grain markets", "पसेरी (पांच सेर का बाट)", "noun", "f", "measures", "mwr", "पसेरी सूं तौल'र गेहूं दियो।"),
    ("धड़ी", "dhadi", "standard 5-kilogram measure unit for vegetables and fodder", "धड़ी (पांच किलो का तौल)", "noun", "f", "measures", "mwr", "एक धड़ी काचरी खरीदी।"),
    ("पाव", "paav", "one-fourth fraction of a ser or kilogram (250 grams)", "पाव (एक चौथाई किलो)", "noun", "m", "measures", "mwr", "पाव भर शुद्ध घी लीनो।"),
    ("छटांक", "chhataank", "one-sixteenth fraction of a ser (approx 58 grams)", "छटांक (सेर का सोलहवां भाग)", "noun", "f", "measures", "mwr", "दवा सारू दो छटांक कतीरो मंगायो।"),
    ("तोलो", "tolo", "traditional weight unit for gold and silver (approx 10-11.66 grams)", "तोला (स्वर्ण-रजत तौल)", "noun", "m", "measures", "mwr", "लाडी सारू पांच तोले रो हार बणायो।"),
    ("मासो", "maaso", "one-twelfth fraction of a tola used by goldsmiths", "माशा (सोने का सूक्ष्म माप)", "noun", "m", "measures", "mwr", "अंगूठी में आठ मासा सोनो लाग्यो।"),
    ("रत्ती", "ratti", "smallest traditional weight unit based on Abrus precatorius red seed", "रत्ती (रत्नों का सूक्ष्म तौल)", "noun", "f", "measures", "mwr", "नथ में दो रत्ती रो मोती जड्यो।"),
    ("कोस", "kos", "traditional linear road distance unit (approx 3 kilometers)", "कोस (दूरी का प्राचीन माप / लगभग तीन किमी)", "noun", "m", "measures", "mwr", "गाँव अठै सूं चार कोस दूर है।"),
    ("गाउ", "gaau", "distance across which the bellowing call of a cow carries (~1.5 km)", "गव्युति / गाउ (दूरी का लोक माप)", "noun", "m", "measures", "mwr", "मंदिर दो गाउ री दूरी माथे है।"),
    ("खारडो", "khaardo", "alkaline, salt-encrusted infertile desert patch", "खारड़ा (खारी उसर भूमि)", "noun", "m", "geography", "mwr", "खारडे में कोई फसल नीं पाकै।"),
    ("पीळकी", "peelki", "soft yellow loamy desert soil suitable for bajra and guar", "पीलकी (पीली रेतीली दोमट मिट्टी)", "noun", "f", "agriculture", "mwr", "पीळकी माटी में बाजरी चोखी व्है।"),
    ("भूरट", "bhoorat", "thorny prickly burr weed (Cenchrus biflorus) growing on desert sand dunes", "भूरट (कांटेदार रेगिस्तानी घास का बीज)", "noun", "m", "flora", "mwr", "धोरां में चालते पग में भूरट चिपक गयो।"),
    ("आकल", "aakal", "fossil wood or calcified stone formation found near Jaisalmer", "आकल (काष्ठ जीवाश्म)", "noun", "m", "geography", "mwr", "आकल वुड फॉसिल पार्क प्राचीन इतिहास बतावै।"),

    # --- 2. Astronomy, Desert Weather & Rain Lore (नखत, तारा अर वर्षा ज्ञान) ---
    ("नखत", "nakhat", "lunar mansion / asterism predicting rainfall and seasonal prosperity", "नक्षत्र (नखत)", "noun", "m", "astronomy", "mwr", "रोहिणी नखत में बादळ गाज्या।"),
    ("रोहिणी", "rohini", "supreme rain-predicting asterism in Jeth whose scorching heat portends abundant monsoon", "रोहिणी नक्षत्र (वर्षा ज्ञान का मुख्य नक्षत्र)", "noun", "f", "astronomy", "mwr", "रोहिणी तपसी तो मेह बरससी।"),
    ("मिरगसर", "mirgasar", "Mrigashira constellation bringing fierce dry pre-monsoon dust whirlwinds", "मृगशिरा नक्षत्र (तेज हवाओं का नक्षत्र)", "noun", "m", "astronomy", "mwr", "मिरगसर में बबूळिया उठै।"),
    ("आदरा", "aadra", "Ardra constellation ushering the first stormy monsoon downpours", "आर्द्रा नक्षत्र (वर्षा ऋतु का शुभारंभ)", "noun", "f", "astronomy", "mwr", "आदरा में आकाश मेघां सूं घिर गयो।"),
    ("पुनरबस", "punarbas", "Punarvasu asterism bringing gentle, soaking rains that sprout sown seeds", "पुनर्वसु नक्षत्र", "noun", "m", "astronomy", "mwr", "पुनरबस री फुहार सूं खेत हरा होया।"),
    ("पुख", "pukh", "Pushya asterism bringing steady continuous rain maturing millet tillers", "पुष्य नक्षत्र (अन्न पकाने वाली वर्षा)", "noun", "m", "astronomy", "mwr", "पुख रो मेह अन्नदाता व्है।"),
    ("अश्लेषा", "ashlesha", "Ashlesha constellation causing intense non-stop torrential rains", "अश्लेषा नक्षत्र (झड़ी लगाने वाला नक्षत्र)", "noun", "f", "astronomy", "mwr", "अश्लेषा में नाडी-तालाब छलक ग्या।"),
    ("मघा", "magha", "Magha constellation bringing precious rain drops described as molten silver in folklore", "मघा नक्षत्र (वरदानी वर्षा)", "noun", "f", "astronomy", "mwr", "मघा रा छींटा मोतियों जैसे कीमती हैं।"),
    ("स्वाती", "swati", "Swati asterism whose raindrops folklore says turn into pearls in oysters and poison in serpents", "स्वाति नक्षत्र", "noun", "f", "astronomy", "mwr", "स्वाती री बूंद सीप में मोती बणै।"),
    ("ध्रुवतारी", "dhruva-taari", "North Star (Pole Star) by which desert camel caravans navigate pathless sand dunes at night", "ध्रुव तारा (दिशा दर्शक तारा)", "noun", "f", "astronomy", "mwr", "रेबारी ध्रुवतारी देख'र रात में रस्तो खोजै।"),
    ("सप्तऋषि", "saptarishi", "Great Bear constellation indicating time transitions in night watch", "सप्तर्षि तारामंडल", "noun", "m", "astronomy", "mwr", "सप्तऋषि फिर ग्या, अबै पौ फटने वाळी है।"),

    # --- 3. Fort Architecture, Medieval Warfare & Martial Regalia ---
    ("कांगरो", "kaangro", "crenellated parapet tooth atop fort battlements for archers and musketeers", "कांगरा (किले की दीवार का दंतुर हिस्सा)", "noun", "m", "architecture", "mwr", "दुर्ग रै कांगरे सूं तोप दागी।"),
    ("परकोटो", "parkoto", "massive fortified stone defense wall surrounding medieval Rajasthani towns", "परकोटा (नगर रक्षा प्राचीर)", "noun", "m", "architecture", "mwr", "जयपुर रो परकोटो यूनेस्को धरोहर है।"),
    ("बुर्ज", "burj", "circular stone bastion or defensive turret projecting outward from fortress walls", "बुर्ज (किले का गोल मोर्चा / मीनार)", "noun", "m", "architecture", "mwr", "जैसलमेर किले में निन्यानवे बुर्ज हैं।"),
    ("खाई", "khaai", "deep excavated defensive moat surrounding fort filled with water or thorny cactuses", "खाई (किले के चारों ओर की रक्षा खाई)", "noun", "f", "architecture", "mwr", "लोहागढ़ दुर्ग रै चारूं मेर गहरी खाई है।"),
    ("मोरी", "mori", "fortified subterranean water conduit or secret portal through city ramparts", "मोरी (गुप्त निकास मार्ग / जलद्वार)", "noun", "f", "architecture", "mwr", "मोरी रै रस्ते सूं गुप्तचर बाहर नीकळ्यो।"),
    ("गुपचुप", "gupchup", "secret underground escape tunnel connecting palace to exterior forest", "सुरंग / गुप्त रास्ता", "noun", "f", "architecture", "mwr", "किले में संकट काल सारू गुपचुप बणी ही।"),
    ("ढाल", "dhaal", "convex circular shield forged from rhinoceros-hide, steel, or brass", "ढाल (आत्मरक्षा का अस्त्र)", "noun", "f", "weapons", "mwr", "वार नै ढाल माथे झेल लियो।"),
    ("बख्तर", "bakhtar", "interlocking iron chain-mail torso coat protecting warrior against sword thrusts", "बख्तर (लोहे का जिरह-कवच)", "noun", "m", "weapons", "mwr", "बख्तर पहर'र सूरमा रणखेत गयो।"),
    ("शिलहखाना", "silahkhaana", "royal arsenal and arms storehouse of a princely state", "शस्त्रागार / शिलहखाना", "noun", "m", "weapons", "mwr", "शिलहखाने में तलवार अर तोपां सजी हैं।"),
    ("तोपची", "topchi", "master artillery gunner commanding siege guns on fort bastions", "तोपची (तोप चलाने वाला गोलंदाज)", "noun", "m", "history", "mwr", "तोपची किले री तोप रो अचूक संधान कियो।"),
    ("कमधज", "kamdhaj", "ancient honorific epithet of Rathore warriors fighting without caring for body", "कमधज (राठौड़ वंश का गौरवशाली विरुद)", "noun", "m", "chivalry", "mwr", "कमधज वीरां कभी पीठ नीं दिखाई।"),
    ("दातार", "daataar", "magnanimous noble benefactor donating wealth, cows and land to the needy", "दाता / दानी / उदार पुरुष", "noun", "m", "values", "mwr", "राजस्थान री धरती दातार अर सूरमां री खान है।"),
    ("सूर", "soor", "fearless lionhearted warrior giving life on the battlefield for honor", "शूरवीर / योद्धा", "noun", "m", "chivalry", "mwr", "सूर कदेय संकट सूं कोनी डरे।"),

    # --- 4. Spiritual Traditions, Saints & Sacred Folk Philosophy ---
    ("पाहल", "paahal", "sacred water sanctified with mantras and iron tool administered during Bishnoi initiation", "पाहल (बिश्नोई संप्रदाय का अभिमंत्रित चरणामृत)", "noun", "m", "culture", "mwr", "गुरु महाराज पाहल दे'र धर्म में दीक्षित कियो।"),
    ("सबदवाणी", "sabadwaani", "sacred 120 poetic revelations of Guru Jambheshwarji guiding environmental ethics", "शब्दवाणी (जाम्भोजी के पवित्र शब्द)", "noun", "f", "literature", "mwr", "संध्या वगत बिश्नोई सबदवाणी रो पाठ करै।"),
    ("अगन-नृत्य", "agan-nritya", "miraculous spiritual dance of Jasnathi Siddhas walking barefoot on fiery live coals in Katariyasar", "अग्नि नृत्य (धधकते अंगारों पर किया जाने वाला नृत्य)", "noun", "m", "culture", "mwr", "जसनाथी सिद्ध अंगारों माथे अगन-नृत्य करै।"),
    ("सिद्धां रा बोल", "siddhaan ra bol", "sacred mystic chants uttered by fire dancers invoking Guru Jasnathji ('फतेह फतेह')", "सिद्धां के बोल / सिमरन", "noun", "m", "culture", "mwr", "'फतेह फतेह' कहत सिद्ध अंगारां में कूद पड़ै।"),
    ("धूंणा", "dhoona", "sacred perpetual open hearth fire kept burning continuously by Nath jogis and hermits", "धूणा (अखंड अग्नि कुंड)", "noun", "m", "culture", "mwr", "जोगी आपरे धूंणे माथे समाधि लगाय बैठ्या।"),
    ("रामो-राम", "ramo-ram", "devout daily greeting of the Ram Snehi sect of Shahpura and Ren", "रामो-राम (रामस्नेही संप्रदाय का अभिवादन)", "noun", "phrase", "greetings", "mwr", "संत आपस में 'रामो-राम' कह'र प्रणाम करै।"),
    ("फूलडोल", "phool-dol", "grand five-day spring festival of Ram Snehi order held at Shahpura after Holi", "फूलडोल महोत्सव (शाहपुरा का प्रसिद्ध उत्सव)", "noun", "m", "festivals", "mwi", "शाहपुरा में फूलडोल मेला में लाखों भक्त आया।"),
    ("खेजड़ली", "khejardli", "historic village near Jodhpur where Amrita Devi and 363 Bishnois sacrificed lives in 1730 to protect green trees", "खेजड़ली (पर्यावरण बलिदान का विश्व-तीर्थ)", "noun", "m", "history", "mwr", "खेजड़ली रो बलिदान पर्यावरण रक्षा री अमर मिसाल है।"),
    ("सिर साटे रूंख", "sir saante roonkh", "sacred supreme motto coined by Amrita Devi: 'Even if head is severed to save a tree, consider it cheap bargain'", "सिर सांटे रूंख रहे तो भी सस्तो जाण", "noun", "phrase", "values", "mwr", "सिर साटे रूंख बचे, तो भी सस्तो जाण।"),

    # --- 5. Classical Folk Songs, Ragas & Musical Ballads ---
    ("मांड", "maand", "world-renowned classical folk singing style of Rajasthan characterized by desert modulation", "मांड गायकी (राजस्थान की प्रसिद्ध अर्ध-शास्त्रीय शैली)", "noun", "f", "music", "mwr", "अल्लाह जिलाई बाई मांड राग में अमर गीत गायो।"),
    ("पणिहारी", "panihari", "traditional folk melody sung by women walking with balanced pitchers to the village well", "पणिहारी (कुएं से जल लाती स्त्रियों का गीत)", "noun", "f", "music", "mwr", "पणिहारी गीत में मरुधर री संस्कृति छलकती है।"),
    ("काजलियो", "kaajaliyo", "auspicious marriage song sung when groom's sister applies protective kohl to his eyes", "काजलिया (दूल्हे को काजल लगाते समय का गीत)", "noun", "m", "music", "mwr", "बहिन लाडेसर भाई नै काजलियो आंज्यो।"),
    ("सुपनो", "supano", "haunting folk ballad narrating a lonely wife's dream of her distant traveling husband", "सुपना (विरहिणी का स्वप्न गीत)", "noun", "m", "music", "mwr", "सुपने में साजन आया, नींद खुलत ही अलोप हो गया।"),
    ("बिणजारो", "binjaaro_song", "festive nomad caravan song sung during Teej and monsoons", "बणजारा लोकगीत", "noun", "m", "music", "mwr", "बिणजारे री हाक मरुभूमि में गूंजी।"),
    ("जीरा", "jeera_song", "humorous yet poignant folk ballad where wife implores husband never to cultivate anxiety-laden cumin", "जीरा गीत ('मत बोवो म्हारा परण्या जीरा')", "noun", "m", "music", "mwr", "जीरो जीव रो बैरी रे, मत बाओ म्हारा परण्या जीरा!"),
    ("जलो-जलाल", "jalo-jalaal", "playful welcome song sung by bride's womenfolk when inspecting the groom's wedding cortege", "जलो-जलाल गीत (डेरा देखने जाते समय का गीत)", "noun", "m", "music", "mwr", "बारात रो डेरो देखण जावत स्त्रियां जलो-जलाल गायो।"),
    ("मोरियो", "moriyo", "tender folk song expressing anguish of an engaged maiden whose wedding date is distant", "मोरिया (सगाई व विवाह के बीच का लोकगीत)", "noun", "m", "music", "mwr", "मोरियो आछो बोल्यो रे ढळती रात में!"),

    # --- 6. Traditional Crafts, Dyeing & Folk Arts ---
    ("डाबू", "daabu", "traditional mud-resist paste made of clay, lime and gum applied before natural vat dyeing", "दाबू (छपाई की मिट्टी प्रतिरोधक लेप पद्धति)", "noun", "m", "crafts", "mwi", "अकोला में दाबू प्रिंट रो काम परम्परा सूं चालै।"),
    ("अकोला प्रिंट", "akola print", "famed natural bedsheet and jajam hand-block printing center on Bedach river in Chittorgarh", "अकोला छपाई (चित्तौड़गढ़ की प्रसिद्ध छीपा कला)", "noun", "m", "crafts", "mwi", "अकोला रा दाबू वस्त्र खूब टिकाऊ व्है।"),
    ("ब्लू पॉटरी", "blue pottery", "famed Jaipur ceramic glaze craft made with quartz, fuller earth and copper oxide without clay", "ब्लू पॉटरी (जयपुर की नीली मृद्भाण्ड कला)", "noun", "f", "crafts", "dhd", "कृपाल सिंह शेखावत ब्लू पॉटरी ने नई ऊंचाई दीनी।"),
    ("मोलेला री मूर्तिकला", "molela terracotta", "hollow clay bas-relief votive plaques of folk deities (Dharmraja, Devnarayan) sculpted in Molela village near Nathdwara", "मोलेला की टेराकोटा कला (मृण्मूर्ति शिल्प)", "noun", "f", "crafts", "mwi", "मोलेला रा कुम्हार लाल माटी सूं देव-फलक बणावै।"),
    ("लाख री चूड़ियां", "laakh ri choodiyan", "hand-molded colored lac bangles studded with glass beads, specialty of Jaipur and Jodhpur", "लाख की चूड़ियां", "noun", "f", "crafts", "mwr", "सुहागनां तीज माथे लाख री चूड़ियां पहरै।"),
    ("बाटिक", "baatik", "wax-resist dyeing technique on pure cotton or silk, specialty of Khandela", "बाटिक कला (मोम प्रतिरोधक रंगाई)", "noun", "m", "crafts", "skh", "खंडेला रो बाटिक प्रिंट प्रसिद्ध है।"),

    # --- 7. Wedding, Festive Feasting & Kinship Expressions (from Harji Ro Vyambalo & Mayra) ---
    ("ब्यांबलो", "byaamblo", "grand auspicious folk ballad and ritual singing of divine marriage", "ब्यांवलो / विवाह-कथा (मंगल गायन)", "noun", "m", "literature", "mwr", "हरजी रो ब्यांबलो श्रद्धा सूं बांच्यो।"),
    ("सोहलो", "sohlo", "joyous celebratory song chanted upon birth of an heir or victory", "सोहिला / बधाई गीत", "noun", "m", "music", "mwr", "घर में पुत्र जन्म माथे सोहलो गायो।"),
    ("चीकट", "cheekat", "traditional auspicious distribution of turmeric and sweets to announce wedding dates to clan", "चीकट (विवाह की सूचना स्वरूप गुड़-हल्दी वितरण)", "noun", "f", "rituals", "mwr", "नाते-रिश्तेदारां में चीकट भेजी।"),
    ("जमणवार", "jamanwaar", "lavish community wedding feast honoring hundreds of invited clan guests", "जमणवार (विशाल प्रीतिभोज)", "noun", "f", "culture", "mwr", "ब्याव में पांच गांवां री जमणवार रखी।"),
    ("समधी-मिलण", "samdhi-milan", "formal embrace and exchange of turbans/coconuts between the fathers of bride and groom", "समधी-मिलन (सामेला के समय परस्पर भेंट)", "noun", "m", "rituals", "mwr", "सामेला में समधी-मिलण रो भावपूर्ण दृश्य थो।"),
    ("माहेरो", "maahero", "maternal uncle ceremonial arrival with lavish trunk-loads of silk garments and jewelry for sister", "माहेरा / भात समर्पण", "noun", "m", "rituals", "mwr", "माहेरो ले'र ननिहाल वाळा ढोल बजावता आया।"),
    ("लाडेसर", "laadesar", "beloved affectionate term for the bridegroom or pampered young prince", "लाडेसर (दुलारा दूल्हा अथवा राजकुमार)", "noun", "m", "kinship", "mwr", "लाडेसर माथे सेहरो बांध्यो।"),
    ("लाडली", "laadli", "cherished affectionate darling daughter or bride", "लाडली (दुलारी कन्या / वधू)", "noun", "f", "kinship", "mwr", "लाडली बेटी सासरै सिधारी।"),
    ("सासरियो", "saasariyo", "marital home and father-in-law's village of a married woman", "ससुराल (सासरिया)", "noun", "m", "kinship", "mwr", "गोरी सासरिये में सब रो आदर राखै।"),
    ("पीहरियो", "peehariyo", "natal parental ancestral home and mother's village", "मायका / पीहर", "noun", "m", "kinship", "mwr", "तीज माथे बहू पीहरिये आई।"),
    ("कंवर-कलेवो", "kanwar-kalevo", "special breakfast banquet served to the newly-wed bridegroom inside the bridal home by women", "कंवर-कलेवा (दामाद को कराया जाने वाला विशेष नाश्ता)", "noun", "m", "rituals", "mwr", "कंवर-कलेवे में जवाई सा नै खाजा अर रबड़ी परोसी।"),
    ("छाती माथे मूंग दळणा", "chhaati maathe moong dalna", "to deliberately annoy or provoke someone while staying right in front of them", "छाती पर मूंग दलना (सामने रहकर कष्ट देना)", "noun", "phrase", "values", "mwr", "घर में बैठ'र छाती माथे मूंग दळै है।"),
    ("गाल बजावणो", "gaal bajaavno", "to indulge in empty boasting and tall claims without substance", "गाल बजाना (डींगें हांकना)", "noun", "phrase", "values", "mwr", "काम तो करै कोनी, बस गाल बजावै।"),
    ("आस-औलाद", "aas-aulaad", "cherished children, offspring, and future generations of family lineage", "संतान / वंश परंपरा", "noun", "f", "kinship", "mwr", "ईश्वर थारी आस-औलाद नै सुखी राखै।"),
    ("कुल-रीति", "kul-reeti", "sacred hereditary code of conduct and family customs passed down through generations", "कुल-परंपरा / वंश मर्यादा", "noun", "f", "values", "mwr", "आपणी कुल-रीति कदेय नीं छोड़णी चाहीजै।")
]

added = 0
for item in BATCH_1250:
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

print(f"Added {added} brand new terms from Wave 7! Grand total lexicon now: {len(words)}")
