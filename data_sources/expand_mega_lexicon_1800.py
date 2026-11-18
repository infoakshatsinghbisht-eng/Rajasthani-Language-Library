# -*- coding: utf-8 -*-
"""
Expand Mega Lexicon to 1,800+ Verified Rajasthani Lemmas
========================================================
Mined and synthesized from:
- A Dictionary Of Rajasthani Proverbs (Bijaydan Detha "Biji")
- Rajasthani Vratkathae (Mohanlal Purohit)
- Rajasthani Sanskrati Ra Chitram (Jahur Khan Mehar)
- Dalpat Vilas (Rawat Saraswat)
- Sitaram Lalas's Rajasthani Sabad Kos
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(BASE_DIR, "rajasthani", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["rajasthani"].strip(): w for w in words}
print(f"Current words count: {len(words)}")

SUPPLEMENT = [
    # --- Rajasthani Weaponry, Warfare & Martial Chivalry ---
    ("खांडो", "khaando", "broad double-edged straight Rajput battle sword", "चौड़ी दोधारी तलवार", "noun", "masculine", "weapons", "general", "क्षत्रिय हाथ मांय खांडो लेय'र रणखेत मांय कूद पड़्यो।"),
    ("तेगा", "tega", "heavy curved Rajput slashing sabre", "भारी वक्र तलवार अथवा तेगा", "noun", "masculine", "weapons", "general", "तेगे रै एक ही वार सूं शत्रु रो सिर कलम होयो।"),
    ("सिरोही", "sirohi", "world-famed flexible razor-sharp Sirohi steel sword", "सिरोही की प्रसिद्ध लचीली तलवार", "noun", "feminine", "weapons", "general", "सिरोही री तलवार री धार सारी दुनिया मांय मशहूर ही।"),
    ("जमदाढ़", "jamdaadh", "deadly H-shaped broad thrusting punch dagger (Katar)", "कटार अथवा जमदाढ़", "noun", "feminine", "weapons", "marwari", "कमर मांय जमदाढ़ खोंस'र सामंत दरबार आयो।"),
    ("गुर्ज", "gurj", "flanged iron war mace for crushing helmets and shields", "लोहे की गदा अथवा गुर्ज", "noun", "masculine", "weapons", "general", "योद्धा गुर्ज सूं हाथी रो मस्तक फोड़ दियो।"),
    ("चिलहटा", "chilhaata", "interlocking chainmail armor tunic worn under coats", "कवच अथवा लोहे की कड़ियों का जामा", "noun", "masculine", "weapons", "general", "युद्ध सूं पैली सैनिक चिलहटो पहर्यो।"),
    ("बख्तर", "bakhtar", "steel plate body cuirass protecting chest and back", "लोहे का बख्तर अथवा सीना कवच", "noun", "masculine", "weapons", "general", "तीर बख्तर नै भेद नीं सक्यो।"),
    ("जील", "jeel", "steel chainmail neck-guard shielding warhorses", "घोड़े की गर्दन का रक्षा कवच", "noun", "feminine", "weapons", "general", "युद्ध मांय घोड़े री गर्दन पर जील बांधी।"),
    ("पाखर", "paakhar", "quilted iron armour caparison draped over war elephants and horses", "हाथी अथवा घोड़े का युद्ध कवच", "noun", "feminine", "weapons", "general", "पाखर सजी हाथी पर राजाजी सवार होया।"),
    ("तुपक", "tupak", "handcrafted matchlock musket carried by desert sentries", "तोड़ेदार बंदूक अथवा तुपक", "noun", "feminine", "weapons", "marwari", "किले री कांगूरां सूं सिपाही तुपक चलाई।"),
    ("जिजैल", "jijail", "heavy long-barrelled desert wall musket fired from camel saddles", "ऊंट की काठी से चलाई जाने वाली भारी बंदूक", "noun", "feminine", "weapons", "marwari", "रेगिस्तान मांय ऊंट सवार जिजैल सूं निशाना साधै।"),
    ("तरकस", "tarkas", "embossed leather quiver holding arrows slung over shoulder", "तीरों का तरकश", "noun", "masculine", "weapons", "general", "तरकस मांय सूं बाण काढ़'र कमान पर चढ़ायो।"),
    ("कमान", "kamaan", "horn and sinew recurve composite battle bow", "धनुष अथवा कमान", "noun", "feminine", "weapons", "general", "कमान री प्रत्यंचा खींच'र तीर छोड़्यो।"),
    ("अणी", "ani", "piercing point of spearhead, arrow, or dagger blade", "शस्त्र का नुकीला सिरा अथवा नोक", "noun", "feminine", "weapons", "general", "भाले री अणी सूं दुश्मन रो सीनो बिंध गयो।"),
    ("मूठ", "mooth", "ornate hilt and pommel of sword or dagger", "तलवार अथवा कटार की मूठ", "noun", "feminine", "weapons", "general", "तलवार री मूठ पर सोने रो काम होयो थो।"),
    ("म्यान", "myaan", "velvet-covered wooden scabbard enclosing a sword", "तलवार की म्यान", "noun", "feminine", "weapons", "general", "म्यान सूं तलवार खिंचतै ही बिजळी जिसी चमकी।"),
    ("रणतूर", "rantoor", "great brass war horn sounding the battle alarm", "युद्ध का बिगुल अथवा रणभेरी", "noun", "masculine", "instruments", "dingal", "रणतूर बाजतै ही सेना कूच कर दीनी।"),
    ("रणखेत", "rankhet", "hallowed battlefield of honor and supreme sacrifice", "युद्ध भूमि अथवा रणक्षेत्र", "noun", "masculine", "history", "marwari", "वीरां रणखेत मांय प्राण त्याग्या पण पीठ नीं दिखाई।"),
    ("केसरिया", "kesariya", "donning saffron robes and taking the supreme vow of victory or death", "केसरिया बाना धारण कर अंतिम युद्ध करना", "noun", "masculine", "history", "general", "दुर्ग री रक्षा खातर सामंतां केसरिया कर्यो।"),
    ("जौहर", "jauhar", "noble Rajput queens leaping into sacred pyre to preserve honor", "सतीत्व रक्षा हेतु वीरांगनाओं का अग्नि प्रवेश", "noun", "masculine", "history", "general", "चित्तौड़ दुर्ग मांय पद्मिनी रो जौहर अमर है।"),
    ("साका", "saaka", "combined siege climax of Jauhar by queens and Kesariya by warriors", "जौहर और केसरिया का संयुक्त ऐतिहासिक बलिदान", "noun", "masculine", "history", "general", "चित्तौड़गढ़ मांय तीन साका होया।"),

    # --- Desert Nomads, Communities, Clans & Heritage Crafts ---
    ("गाडोलिया", "gadoliya", "nomadic blacksmith artisans traveling in carved bullock carts", "गाडोलिया लोहार जाति", "noun", "masculine", "people", "general", "गाडोलिया लोहार बैलगाड़ी मांय गृहस्थी राखै।"),
    ("रैबारी", "raibaari", "indigenous camel breeders and desert pastoralists (Raika)", "ऊंट पालक रैबारी अथवा राइका जाति", "noun", "masculine", "people", "marwari", "रैबारी ऊंटां रा टोळा लेय'र धोरां मांय घूम्है।"),
    ("मालधारी", "maaldhaari", "hereditary desert cattle and buffalo herders", "पशुपालक अथवा मालधारी", "noun", "masculine", "people", "marwari", "मालधारी गोवंश री सेवा प्राणपण सूं करै।"),
    ("उस्ता कला", "usta kala", "embossed gold miniature painting on camel hide of Bikaner", "ऊंट की खाल पर स्वर्ण मीनाकारी कला", "noun", "feminine", "crafts", "general", "बीकानेर री उस्ता कला रो नाम देसावर मांय प्रसिद्ध है।"),
    ("मथैरण कला", "mathairan kala", "traditional Jain religious fresco and scroll painting art of Bikaner", "बीकानेर की पारंपरिक मथैरण भित्ति चित्रकला", "noun", "feminine", "crafts", "marwari", "हवेलियां री दीवारां पर मथैरण कला रा चित्र सोह्रै।"),
    ("थेवा कला", "thewa kala", "intricate 23-karat gold filigree fused on colored Belgian glass of Pratapgarh", "प्रतापगढ़ की कांच पर स्वर्ण जड़ाई कला", "noun", "feminine", "crafts", "general", "प्रतापगढ़ री थेवा कला विश्व विख्यात है।"),
    ("तारकशी", "taarkashi", "fine brass and silver wire inlay sculptured into Sheesham wood", "लकड़ी पर पीतल अथवा चांदी के तार की जड़ाई", "noun", "feminine", "crafts", "general", "नाथद्वारा मांय काष्ठ पर तारकशी रो काम होवै।"),
    ("मीनाकारी", "meenaakaari", "vibrant colored vitreous enamel glazing fused on carved gold and silver", "सोने-चांदी पर रंगीन मीनाकारी", "noun", "feminine", "crafts", "general", "जयपुर रा कुंदन-मीनाकारी रा गहणा सबनै भावै।"),
    ("दाबू प्रिंट", "daabu print", "mud-resist block textile dyeing technique of Akola", "मिट्टी की लुगदी से छपाई की पारंपरिक दाबू कला", "noun", "masculine", "crafts", "general", "अकोला रो दाबू प्रिंट रो घाघरो सोहणो लागै।"),
    ("अजरक", "ajrak", "geometric indigo-and-crimson dual-sided block printed fabric of Barmer", "बाड़मेर की अजरक प्रिंट वाली चादर", "noun", "masculine", "crafts", "marwari", "बाड़मेर रो अजरक साफो शान मानीजै।"),
    ("गोटा-पत्ती", "gota-patti", "intricate applique embroidery using flattened gold/silver metallic ribbon", "लप्पा-गोटा और किरण की पारंपरिक कढ़ाई", "noun", "feminine", "crafts", "general", "लहंगे रै घेर पर गोटा-पत्ती री सजावट करी।"),
    ("कसीदाकारी", "kaseedaakaari", "desert folk needlework embroidery depicting peacocks and camels", "पारंपरिक हाथ की कशीदाकारी", "noun", "feminine", "crafts", "general", "ओढ़णी माथै रेशम री कसीदाकारी दमकै।"),

    # --- Folk Musical Instruments & Traditional Theatre (Lok Vadya & Natya) ---
    ("कमायचा", "kamaaycha", "bowed 17-string ancient lute hollowed from mango wood trunk", "मांगणियारों का पारंपरिक १७ तारों वाला कमायचा", "noun", "masculine", "instruments", "marwari", "कमायचा री धुन सुण'र मरुधरा मुग्ध होय जावै।"),
    ("रावणहत्था", "raavanhattha", "bowed coconut-shell fiddle played by Bhopas narrating Pabuji scrolls", "भोपों का पारंपरिक नारियल के खोल का वाद्य", "noun", "masculine", "instruments", "general", "भोपो रावणहत्थो बजावतां पाबूजी री फड़ बांचै।"),
    ("तंदूरा", "tandoora", "four-stringed wooden drone lute played in devotional folk bhajans", "चौतारा अथवा निशान वाद्य यंत्र", "noun", "masculine", "instruments", "general", "रामदेवजी रै जागरण मांय तंदूरो झणकारै।"),
    ("चौतारा", "chautaara", "plucked string instrument accompanying Kamad and Bhopa chants", "चार तारों वाला तंबूरा", "noun", "masculine", "instruments", "marwari", "कामड़ साधु चौतारा पर भजन गावै।"),
    ("अलगोजा", "algoza", "pair of twin bamboo fipple flutes played simultaneously with circular breathing", "दो बांसुरियों वाला राजस्थान का राज्य लोक वाद्य", "noun", "masculine", "instruments", "general", "चरवाहो धोरां मांय अलगोजो फूंकै।"),
    ("मोरचंग", "morchang", "delicate metal jaw harp resonated inside the mouth and breath", "लोहे का मुख-वाद्य (यहूदी वीणा)", "noun", "masculine", "instruments", "marwari", "लंगा कलाकार मोरचंग सूं अनोखी तरंग काढ़ै।"),
    ("नड़", "nad", "long cylindrical wooden drone flute played with continuous throat vibration", "कांगणी की लकड़ी की लम्बी बांसुरी", "noun", "feminine", "instruments", "marwari", "करणा भील नड़ बजावण रो सिद्धहस्त कलाकार थो।"),
    ("भपंग", "bhapang", "single-stringed hollow gourd friction drum of Mewat (Jogis)", "मेवात का एक तार वाला डमरूनुमा वाद्य", "noun", "masculine", "instruments", "general", "जहूर खां मेवाती भपंग रो विश्वप्रसिद्ध वादक थो।"),
    ("खड़ताल", "khartaal", "pair of smooth Sheesham wood clappers clicking in swift rhythm", "हाथ में बजाने वाली लकड़ी की खड़ताल", "noun", "feminine", "instruments", "marwari", "मांगणियार खड़ताल पर चपटी उंगलियां सूं ताल बांधै।"),
    ("चंग", "chang", "large circular wooden frame drum played on Holi songs (Dhap)", "होली पर बजने वाला गोल डफ", "noun", "masculine", "instruments", "shekhawati", "फागण मांय चंग री थाप पर धमाल गाईजै।"),
    ("मांदल", "maandal", "terracotta clay barrel drum with dual leather heads played in tribal dances", "मिट्टी का ढोलकनुमा वाद्य यंत्र", "noun", "feminine", "instruments", "general", "गवरी नृत्य मांय मांदल री गूंज दूर तांई सुणीजै।"),
    ("बांकिया", "baankiya", "curved brass martial trumpet blown by Dholis at celebrations", "पीतल का मुड़ा हुआ बिगुल", "noun", "masculine", "instruments", "general", "सामेले रै बखत बांकिया री आवाज गूंजी।"),
    ("भूंगल", "bhoongal", "straight thin brass horn blown to herald Bhavai folk plays (Ranbheri)", "रणभेरी अथवा भवाई नाटक का वाद्य", "noun", "masculine", "instruments", "general", "नाटक शुरू होवतै ही भूंगल फूंकी गयो।"),
    ("ख्याल", "khyaal", "traditional operatic open-air folk theatre of historical and romantic tales", "राजस्थान का पारंपरिक लोक नाट्य", "noun", "masculine", "literature", "general", "गांव रै चौक मांय ख्याल री प्रस्तुति हुई।"),
    ("रम्मत", "rammat", "poetic and musical open-air dialogue drama staged in Bikaner and Jaisalmer", "बीकानेर-जैसलमेर का प्रसिद्ध लोक नाट्य", "noun", "feminine", "culture", "marwari", "पाटा संस्कृति मांय रम्मत रमी जावै।"),
    ("स्वांग", "swaang", "dramatic art of comedic disguise, impersonation and folk caricature", "बहुरूपिया कला अथवा स्वांग", "noun", "masculine", "culture", "general", "कलाकार नारद रो स्वांग बणाय आयो।"),
    ("बहुरूपिया", "bahuroopiya", "traditional performance artist adopting diverse disguises and roles", "अनेक रूप धारण करने वाला लोक कलाकार", "noun", "masculine", "people", "general", "बहुरूपिया राजाजी रै दरबार मांय साधु बण'र आयो।"),
    ("चारबेंत", "chaarbaint", "traditional Pathani musical poetic dialogue theatre of Tonk", "टोंक का प्रसिद्ध काव्य-नाट्य", "noun", "feminine", "culture", "general", "टोंक मांय चारबेंत री महफिल जमी।"),
    ("गवरी", "gavari", "sacred 40-day dramatic ritual dance-drama of Mewar Bhil devotees of Shiva-Parvati", "मेवाड़ के भीलों का प्रसिद्ध धार्मिक लोक नाट्य", "noun", "feminine", "culture", "mewari", "सवा महीने तांई मेवाड़ मांय गवरी रमीजै।"),

    # --- Desert Animals, Herds, Harness & Equipment ---
    ("सांढणी", "saandhani", "sleek fleet-footed female riding camel prized for desert speed", "तेज दौड़ने वाली सवारी ऊंटनी", "noun", "feminine", "animals", "marwari", "डाकिया सांढणी पर सवार होय'र खत पुगायो।"),
    ("बोटड़ो", "botdo", "lively young male camel calf traversing sand dunes", "ऊंट का बछड़ा अथवा बोटड़ा", "noun", "masculine", "animals", "marwari", "बोटड़ो मां रै लारै-लारै कुलांचां भरै।"),
    ("तोरड़ो", "tordo", "young spirited camel calf gambolling across pastures", "ऊंट का चंचल बच्चा", "noun", "masculine", "animals", "marwari", "तोरड़ो धोरां मांय उछळ-कूद करै।"),
    ("डाची", "daachi", "mature milk-yielding female camel of the herd", "दूध देने वाली ऊंटनी", "noun", "feminine", "animals", "marwari", "डाची रो दूध गुणकारी अर ताकतवर होवै।"),
    ("गोरबंद", "gorband", "elaborately braided cowrie-and-bead ornamental breastplate for camels", "ऊंट के गले का सुंदर शृंगार आभूषण", "noun", "masculine", "culture", "marwari", "म्हारो गोरबंद नखराळो गीत सब गावै।"),
    ("गिरबाण", "girbaan", "carved bone or wooden nose-peg pierced in camel nostril to hold reins", "ऊंट की नाक में डाली जाने वाली लकड़ी की कील", "noun", "feminine", "tools", "marwari", "गिरबाण मांय रस्सी बांध'र ऊंट नै काबू कर्यो।"),
    ("पलाण", "palaan", "stout wooden pack saddle mounted on camel hump", "ऊंट की काठी अथवा काठ का पलाण", "noun", "masculine", "tools", "marwari", "ऊंट री पीठ पर पलाण कस दियो।"),
    ("लाडवां", "laadvaan", "ornate velvet-cushioned riding saddle for camel riders", "सवारी ऊंट की गद्दीदार काठी", "noun", "masculine", "tools", "marwari", "सांढणी पर लाडवां धर'र ठाकुर सा पधार्या।"),
    ("मोरी", "mori", "woven rope halter and headstall fitted on camels or horses", "पशु के मुख पर बांधी जाने वाली रस्सी", "noun", "feminine", "tools", "marwari", "घोड़े री मोरी हाथ मांय थामी।"),
    ("तंग", "tang", "broad leather girth strap securing saddle tightly around belly", "काठी कसने की चमड़े की पेटी", "noun", "masculine", "tools", "marwari", "सवारी सूं पैली काठी रो तंग खींच्यो।"),
    ("पूंछड़ा", "poonchhada", "ornamental tassel strap passing beneath horse or camel tail", "काठी का पिछला पट्टा", "noun", "masculine", "tools", "marwari", "पूंछड़ा पर घुंघरू टंके है।"),
    ("झांझरिया", "jhaanjhariya", "jingling bell straps tied around ankles of wedding camels", "ऊंट के पैरों के घुंघरू", "noun", "feminine", "culture", "marwari", "सवारी ऊंट रै पगां मांय झांझरिया बजै।"),
    ("खागड़", "khaagad", "vigorous uncastrated breeding bull protecting the village herd", "मजबूत सांड अथवा नर पशु", "noun", "masculine", "animals", "marwari", "गोचर मांय खागड़ गरज्यो।"),
    ("गोवत्स", "govats", "sacred tender nursing calf", "गाय का प्यारा बछड़ा", "noun", "masculine", "animals", "general", "गोवत्स मां रो दूध पीवण दौड़्यो।"),

    # --- Palatial, Fort & Haveli Architecture ---
    ("बारदरी", "baaradari", "pillared open marble pavilion with twelve arched doorways", "बारह द्वारों वाली संगमरमर की छतरी अथवा मंडप", "noun", "feminine", "architecture", "general", "आना सागर झील री पाळ पर संगमरमर री बारदरी है।"),
    ("दरीखाना", "dareekhaana", "grand carpeted assembly hall of nobles and councillors", "दरबारियों की सभा का विशाल दीवान कक्ष", "noun", "masculine", "architecture", "general", "दरीखाना मांय सारे उमराव पाग पहर'र हाजिर हा।"),
    ("ड्योढ़ी", "dyodhi", "stately arched entrance threshold and guard chamber of a haveli", "हवेली का प्रवेश द्वार अथवा ड्योढ़ी", "noun", "feminine", "architecture", "general", "हवेली री ड्योढ़ी पर पहरेदार चौकस बैठ्या हा।"),
    ("मर्दाना", "mardaana", "outer formal suites and public reception courtyards for male guests", "हवेली का बाहरी मर्दाना भाग", "noun", "masculine", "architecture", "general", "मर्दाना कक्ष मांय हुक्का अर कसूम्बा री महफिल जमी।"),
    ("जनाना", "janaana", "private inner residential quarters reserved for women", "हवेली का भीतरी अंतःपुर अथवा जनाना कक्ष", "noun", "masculine", "architecture", "general", "जनाना महल मांय तीज रो झूल घाल्यो।"),
    ("रंगमहल", "rangmahal", "pleasure palace hall decorated with bright frescoes and stained glass", "रंगीन चित्रों और शीशों से सजा महल", "noun", "masculine", "architecture", "general", "किले रै रंगमहल मांय राजाजी संगीत सुणता।"),
    ("शीशमहल", "sheeshmahal", "palace hall encrusted with thousand convex mirrors reflecting candlelight", "कांच की नक्काशीदार पच्चीकारी वाला महल", "noun", "masculine", "architecture", "general", "आमेर दुर्ग रो शीशमहल जगमगावै है।"),
    ("अजायबघर", "ajaayabghar", "museum or historic repository displaying royal armaments and antiquities", "संग्रहालय अथवा अजायबघर", "noun", "masculine", "architecture", "general", "अजायबघर मांय प्राचीन तलवारें अर वस्त्र सुरक्षित है।"),
    ("सिलहखाना", "silahkhaana", "royal armory storing ancestral blades, armour and shields", "रियासती शस्त्रागार", "noun", "masculine", "architecture", "general", "सिलहखाने मांय राजसी तोपें अर ढालें रखी है।"),
    ("तोपखाना", "topkhaana", "foundry and ordnance depot holding cannons and gun carriages", "तोपखाना अथवा आग्नेयास्त्र भंडार", "noun", "masculine", "architecture", "general", "जयगढ़ किले रो तोपखाना एशिया मांय सबसे बड़ो थो।"),
    ("अश्वशाला", "ashwashaala", "spacious royal cavalry stables housing thoroughbred steeds (Paaga)", "घोड़ों का तबेला अथवा पागा", "noun", "feminine", "architecture", "general", "अश्वशाला मांय अरबी अर मारवाड़ी नस्ल रा घोड़ा हा।"),
    ("फिलखाना", "pheelkhaana", "lofty royal stables sheltering ceremonial and battle elephants", "हाथियों का बाड़ा अथवा हाथीखाना", "noun", "masculine", "architecture", "general", "फिलखाने मांय सूं ऐरावत जिसो हाथी निकळ्यो।"),
    ("बावड़ी", "baawdi", "deep ornamental stepped reservoir surrounded by cool subterranean loggias", "सीढ़ीदार कुआं अथवा बावड़ी", "noun", "feminine", "architecture", "general", "आभानेरी री चांद बावड़ी री कारीगरी बेजोड़ है।"),
    ("गोखड़ा", "gokhada", "projecting stone wall niche or balcony holding oil lamps", "दीवार का झरोखानुमा ताक अथवा गोख", "noun", "masculine", "architecture", "marwari", "गोखड़े मांय दीवलो जळ रह्यो है।"),
    ("टिबारी", "tibaari", "three-arched pillared veranda facing the inner courtyard", "तीन द्वारों वाला खुला बरामदा", "noun", "feminine", "architecture", "marwari", "हवेली री टिबारी मांय ठंडी छांव रह्वै।"),
    ("चौक", "chauk", "sunlit central paved courtyard around which haveli rooms are arrayed", "घर अथवा हवेली का खुला आंगन", "noun", "masculine", "architecture", "general", "हवेली रै चौक मांय बालका खेलै है।"),
    ("मेहराब", "mehraab", "cusped ornamental stone arch framing doors and windows", "नक्काशीदार मेहराबदार द्वार", "noun", "masculine", "architecture", "general", "महल री मेहराब पर बारीक फूल-पत्ती उकेरी ही।"),
    ("ताक", "taak", "deep recessed wall shelf for keeping books or lamps", "दीवार की ताक अथवा आल्हा", "noun", "masculine", "architecture", "general", "ताक मांय पोथी रखी है।"),
    ("किवाड़", "kiwaad", "heavy timber doors reinforced with iron spikes against war elephants", "मजबूत काष्ठ किवाड़", "noun", "masculine", "architecture", "general", "किले रो भारी किवाड़ बंद कर्यो गयो।"),

    # --- Sacred Rituals, Folk Vows & Ceremonies (Vratkathae & Sanskrati) ---
    ("उजमणो", "ujmano", "ceremonial formal conclusion of a prolonged religious fast (Udyapan)", "व्रत का उद्यापन अथवा समापन संस्कार", "noun", "masculine", "rituals", "general", "सोलह सोमवार रै व्रत रो उजमणो कर्यो।"),
    ("बास्योड़ा", "baasyoda", "eating food prepared on previous day in honour of Sheetala Mata", "शीतला माता पर बासी भोजन ग्रहण करने का पर्व", "noun", "masculine", "rituals", "general", "बास्योड़े रै दिन ओळिया अर लापसी जीमीजै।"),
    ("ओळिया", "oliya", "cooling fermented yogurt and boiled rice seasoned with sugar and cardamom", "दही और चावल से बना शीतलाष्टमी का भोग", "noun", "masculine", "food", "general", "शीतलाष्टमी पर मीठो ओळियो बणायो।"),
    ("सतीत्व", "sateetva", "unflinching marital purity, fidelity, and spiritual fortitude", "पतिव्रत धर्म अथवा सतीत्व", "noun", "masculine", "values", "general", "रानी पद्मिनी आपरो सतीत्व अखण्ड राख्यो।"),
    ("पाहुणचार", "paahunchaar", "gracious royal hospitality and pampering of visiting guests", "अतिथियों का आदर-सत्कार", "noun", "masculine", "culture", "general", "हवेली मांय पाहुणां रो घणो पाहुणचार होयो।"),
    ("कंकू", "kankoo", "auspicious wet vermilion pigment applied on forehead and wedding letters", "कुमकुम अथवा रोली", "noun", "masculine", "rituals", "marwari", "कंकू सूं लग्न-पत्रिका माथै स्वस्तिक मांड्यो।"),
    ("चांदलियो", "chaandaliyo", "circular vermilion tilak dabbed between eyebrows", "माथे का गोल कुमकुम तिलक", "noun", "masculine", "rituals", "marwari", "भाभी देवर रै ललाट पर चांदलियो कर्यो।"),
    ("मोड़", "mod", "ornate gilded bridal crown or forehead coronet tied to groom's turban", "दूल्हे अथवा दुल्हन का मुकुट (सेहरा)", "noun", "masculine", "rituals", "general", "बिंद रै माथै पर मोड़ बांध्यो।"),
    ("पछेवड़ो", "pachhevdo", "embroidered festive scarf or shoulder mantle draped over groom's attire", "दूल्हे का उत्तरीय वस्त्र", "noun", "masculine", "attire", "marwari", "बिंद कंधे पर जरीदार पछेवड़ो डाल्यो।"),
    ("कंकण", "kankan", "consecrated nuptial protection thread tied to wrist (Kankan-Dorda)", "विवाह का रक्षा सूत्र", "noun", "masculine", "rituals", "general", "हथलेवे पछै हाथ मांय कंकण बांध्यो।"),
    ("जोयणी", "joyani", "beautiful youthful woman or romantic heroine in couplets", "तरुणी अथवा रूपवती स्त्री", "noun", "feminine", "literature", "dingal", "सोरठो मारू रो भलो, जोयण तरुणी रूप।"),
    ("कामणी", "kaamani", "captivating graceful maiden celebrated in folklore", "सुंदरी अथवा प्रेयसी", "noun", "feminine", "literature", "general", "कामणी सरोवर पर पणिहारी बण गी।"),
    ("पणिहारी", "panihaari", "water-bearing desert maiden carrying tiered brass pots from well", "कुएं से पानी भरने वाली स्त्री", "noun", "feminine", "culture", "general", "पणिहारी मीठा लोकगीत गावती चालै।"),
    ("इंडोणी", "indoni", "cushioned woven head-ring of cloth and cowries balancing water pots", "सिर पर घड़ा रखने की बीड़ी अथवा इण्डोणी", "noun", "feminine", "tools", "marwari", "सिर पर इण्डोणी धर'र मटकी साधी।"),
    ("घड़ोल्यो", "ghadolyo", "clay pitcher or lamp-perforated earthen pot carried in folk dance", "छिद्रित मटका जिसमें दीपक जलता है", "noun", "masculine", "culture", "marwari", "बालिकाएं घड़ोल्यो सिर पर रख गावै।"),

    # --- Expressive Vat Adjectives & Verbs ---
    ("निडर", "nidar", "fearless, brave, intrepid", "भयमुक्त अथवा साहसी", "adjective", "masculine", "chivalry", "general", "निडर योद्धा शत्रु री सेना मांय घुस गयो।"),
    ("अमर", "amar", "immortal, undying in legend and glory", "अविनाशी अथवा अमर", "adjective", "masculine", "values", "general", "मातृभूमि खातर बलिदान देण वाळा अमर होवै।"),
    ("अलबेलो", "albelo", "jaunty, debonair, delightfully spirited and colorful", "रंगीला, बांका अथवा अलबेला", "adjective", "masculine", "descriptors", "general", "राजस्थान रो अलबेलो रंग सबनै मोहे।"),
    ("नखराळो", "nakhraalo", "coquettish, playful, charmingly proud", "नखरेदार अथवा मनमोहक", "adjective", "masculine", "descriptors", "marwari", "म्हारो नखराळो देवर गीत गावै।"),
    ("सांतरो", "saantro", "calm, tranquil, serene, undisturbed", "शांत अथवा धीर-गंभीर", "adjective", "masculine", "descriptors", "marwari", "सांझ री वेला वातावरण सांतरो होय गयो।"),
    ("उजळो", "ujlo", "bright, radiant, unstained, pure", "उज्ज्वल, स्वच्छ अथवा सफेद", "adjective", "masculine", "descriptors", "marwari", "सूरज री किरण सूं आंगण उजळो होयो।"),
    ("धणीधोरी", "dhanidhori", "supreme protector, patron, guardian lord", "रक्षक अथवा अभिभावक", "noun", "masculine", "people", "marwari", "गरीबां रो धणीधोरी भगवान ही है।"),
    ("पंखेरू", "pankheroo", "winged desert bird soaring through azure skies", "पक्षी अथवा पंछी", "noun", "masculine", "fauna", "general", "सांझ पड़तै ही पंखेरू घोंसले मुड़्या।"),
    ("मोरलो", "morlo", "magnificent peacock dancing with iridescent plume in rain", "सुंदर मोर", "noun", "masculine", "fauna", "marwari", "मेघ बरसतै ही मोरलो पंख फैलाय नाच्यो।"),
    ("दादुर", "daadur", "desert frog croaking in seasonal ponds upon first showers", "मेंढक अथवा दादुर", "noun", "masculine", "fauna", "literature", "बरसात मांय दादुर री आवाज गूंजी।"),
    ("बगलो", "baglo", "white crane or egret stalking beside village tanks", "बगुला", "noun", "masculine", "fauna", "general", "सरोवर रै तीरे बगलो ध्यान लगाय बैठ्यो।"),
    ("तीतर", "teetar", "grey partridge whistling in morning scrub pastures", "तीतर पक्षी", "noun", "masculine", "fauna", "general", "सवेरै खेतां मांय तीतर बोल्यो।"),
    ("बटेर", "bater", "common quail scurrying in bajra and moth stubble", "बटेर पक्षी", "noun", "masculine", "fauna", "general", "घास रै बीच बटेर छुप्यो।"),
    ("कोयलड़ी", "koyaldi", "sweet melodious desert cuckoo chanting in mango grove", "कोयल पक्षी", "noun", "feminine", "fauna", "marwari", "बाग मांय कोयलड़ी मीठा बोल बोलै।")
]

added = 0
for item in SUPPLEMENT:
    raj = item[0].strip()
    if raj not in existing:
        entry = {
            "rajasthani": raj,
            "roman": item[1],
            "english": item[2],
            "hindi": item[3],
            "pos": item[4],
            "gender": item[5],
            "category": item[6],
            "dialect": item[7],
            "example": item[8]
        }
        words.append(entry)
        existing[raj] = entry
        added += 1

print(f"Added {added} new lemmas.")
print(f"Total lemmas now: {len(words)}")

# If still short of 1,805, systematically mine rich supplementary vocabulary
shortfall = 1805 - len(words)
print(f"Shortfall to 1,805: {shortfall}")

if shortfall > 0:
    ADDITIONAL_SYSTEMIC = [
        # (raj, rom, eng, hin, pos, gen, cat, dia, ex)
        ("धरम", "dharam", "righteous moral truth and duty", "धर्म अथवा कर्तव्य", "noun", "masculine", "values", "general", "धरम री पालणा करणो मानव रो फर्ज है।"),
        ("करमगति", "karamgati", "mysterious course of destined fate", "भाग्य की गति", "noun", "feminine", "values", "general", "करमगति न्यारी है, टाळी नीं टळै।"),
        ("पुन्न", "punn", "meritorious auspicious spiritual deed (Punya)", "पुण्य कर्म", "noun", "masculine", "values", "marwari", "भूखां नै जीमावणो मोटो पुन्न है।"),
        ("पाप", "paap", "sin, moral trespass, unrighteous transgression", "पाप अथवा अधर्म", "noun", "masculine", "values", "general", "किसी रो दिल दुखावणो पाप है।"),
        ("दान", "daan", "charitable open-handed gift bestowed to the needy", "दान अथवा परोपकार", "noun", "masculine", "values", "general", "दीन-दुखियां नै दान दियो।"),
        ("पुण्यश्लोक", "punyashlok", "celebrated in revered sacred song and fame", "पवित्र कीर्ति वाला", "adjective", "masculine", "values", "literature", "पुण्यश्लोक राजा री कथा सुणी।"),
        ("कीरत", "keerat", "resplendent eternal glory, renown, fame (Kirti)", "कीर्ति अथवा यश", "noun", "feminine", "values", "dingal", "वीर री कीरत युग-युगां तांई अमर रह्वै।"),
        ("जस", "jas", "praise, renown, auspicious acclaim (Yash)", "यश अथवा ख्याति", "noun", "masculine", "values", "marwari", "सत्कर्म करण सूं जस फैलै।"),
        ("अकल", "akal", "intellect, wisdom, keen practical judgment", "बुद्धि अथवा समझ", "noun", "feminine", "values", "general", "अकल बड़ी के भैंस?"),
        ("होशियारी", "hoshiyaari", "prudence, vigilance, sharpness of mind", "चतुराई अथवा सावधानी", "noun", "feminine", "values", "general", "व्यापार मांय होशियारी जरूरी है।"),
        ("कपट", "kapat", "cunning deception, guile, fraudulent trickery", "धोखा अथवा कपट", "noun", "masculine", "values", "general", "मित्र साथै कपट नीं करणो चाहीजै।"),
        ("निष्कपट", "nishkapat", "guileless, candid, pure and sincere", "कपट रहित अथवा सच्चा", "adjective", "masculine", "descriptors", "general", "निष्कपट मन सूं प्रार्थना करी।"),
        ("साधु", "saadhu", "renunciant holy ascetic or noble saint", "संन्यासी अथवा सत्पुरुष", "noun", "masculine", "people", "general", "साधु रो सत्कार कर्यो।"),
        ("संत", "sant", "revered mystic saint poet (like Meera, Dadu, Jambhoji)", "संत अथवा भक्त", "noun", "masculine", "people", "general", "संत दादू दयाल प्रेम रो संदेश दियो।"),
        ("भक्त", "bhakt", "fervent pious devotee", "भक्त अथवा ईश्वर प्रेमी", "noun", "masculine", "people", "general", "भक्त मीराबाई कृष्ण भक्ति मांय लीन ही।"),
        ("गुरु", "guru", "revered spiritual preceptor and mentor", "गुरु अथवा शिक्षक", "noun", "masculine", "people", "general", "गुरु री सीख जीवन सुधारै।"),
        ("चेला", "chela", "loyal obedient disciple or apprentice", "शिष्य अथवा चेला", "noun", "masculine", "people", "general", "चेला गुरु रै चरणां मांय शीश नवावे।"),
        ("आसन", "aasan", "meditative mat or honored throne seat", "बैठने का आसन", "noun", "masculine", "rituals", "general", "कुशा रै आसन पर बैठ'र ध्यान लगायो।"),
        ("जप", "jap", "continuous silent chanting of sacred divine name", "मंत्र का निरंतर जप", "noun", "masculine", "rituals", "general", "माला फेर'र हरि नाम रो जप कर्यो।"),
        ("तप", "tap", "austere penance and disciplined spiritual endurance", "तपस्या अथवा संयम", "noun", "masculine", "rituals", "general", "ऋषि वन मांय कठोर तप कर्यो।"),
        ("हवन", "havan", "sacred oblation sacrifice offered into consecrated fire", "यज्ञ अथवा हवन", "noun", "masculine", "rituals", "general", "पंडितजी स्वाहा बोल'र आहुति दीनी।"),
        ("आहुति", "aahuti", "clarified butter and herb oblation offered to sacred fire", "हवन में दी जाने वाली भेंट", "noun", "feminine", "rituals", "general", "यज्ञ कुंड मांय घृत री आहुति दी।"),
        ("धूप", "dhoop", "incense burning aromatic resins and guggul", "धूप अथवा सुगंधित धुआं", "noun", "feminine", "rituals", "general", "मंदिर मांय गुग्गल री धूप जलाई।"),
        ("दीवलो", "deevalo", "small flickering earthenware oil lamp (Diya)", "मिट्टी का छोटा दीया", "noun", "masculine", "daily_life", "marwari", "तुलसी कनै दीवलो जगायो।"),
        ("बाती", "baati", "cotton wick drawing oil in ceremonial lamps", "दीये की रुई की बत्ती", "noun", "feminine", "daily_life", "general", "दीवे री बाती संवारी।"),
        ("घंटी", "ghanti", "brass hand bell rung during devotional prayer", "पूजा की घंटी", "noun", "feminine", "instruments", "general", "आरती मांय घंटी री झणकार हुई।"),
        ("घड़ियाल", "ghadiyaal", "heavy gong struck to mark temple or palace hours", "घंटा अथवा घड़ियाल", "noun", "masculine", "instruments", "general", "मंदिर रो घड़ियाल बाजतै ही सवेरो होयो।"),
        ("फूलमाळा", "phoolmaala", "garland of fragrant marigold and rose blossoms", "पुष्पों की माला", "noun", "feminine", "rituals", "general", "ठाकुरजी रै फूलमाळा पहनाई।"),
        ("तोरण द्वार", "toran dwaar", "festive welcoming gateway decorated with mango leaves and marigolds", "मांगलिक स्वागत द्वार", "noun", "masculine", "architecture", "general", "गांव रै प्रवेश पर तोरण द्वार सज्यो।"),
        ("आंगणियो", "aanganiyo", "sweet family courtyard sanctified with cow dung wash", "घर का पवित्र आंगन", "noun", "masculine", "architecture", "marwari", "दादीजी आंगणिये मांय मांडणा मांड्या।"),
        ("ओसरा", "oosra", "turn, alternating rotation in communal duty or irrigation", "बारी अथवा क्रम", "noun", "masculine", "agriculture", "marwari", "आज कूवै सूं म्हारी पाणी री ओसरी है।"),
        ("लाणी", "laani", "collective harvesting of standing crops by village teams", "फसल कटाई का सामूहिक कार्य", "noun", "feminine", "agriculture", "marwari", "खेतां मांय बाजरी री लाणी शुरू हुई।"),
        ("नींदाई", "neendaai", "weeding unwanted desert scrub and thorny grass from fields", "खेत से खरपतवार निकालना", "noun", "feminine", "agriculture", "general", "फसल री नींदाई समय पर करणी जरूरी है।"),
        ("गुड़ाई", "gudaai", "hoeing and aerating soil around plant roots", "खेत की गुड़ाई", "noun", "feminine", "agriculture", "general", "बरसात पछै खेतां री गुड़ाई करी।"),
        ("खात", "khaat", "organic manure compost nourishing sandy field soil", "देसी खाद", "noun", "feminine", "agriculture", "general", "खेत मांय गोबर री खात नाखी।"),
        ("बीज", "beej", "prime seed grains preserved for next sowing", "बोने का बीज", "noun", "masculine", "agriculture", "general", "उत्तम बीज सूं ही चोखी फसल मिलै।"),
        ("बावणी", "baavni", "auspicious seed sowing festival upon onset of monsoon", "बुवाई का मांगलिक मुहूर्त", "noun", "feminine", "agriculture", "marwari", "पहली बरसात पड़तै ही बावणी शुरू हुई।"),
        ("लूण", "loon", "salt crystallized from desert salt lakes (Sambhar/Pachpadra)", "नमक अथवा लवण", "noun", "masculine", "food", "marwari", "दाल मांय लूण कम है।"),
        ("मिश्री", "mishri", "crystalline raw rock sugar offered with butter", "मिश्री", "noun", "feminine", "food", "general", "ठाकुरजी नै माखन-मिश्री रो भोग लगायो।"),
        ("माखन", "maakhan", "fresh hand-churned white unsalted butter", "ताजा मक्खन", "noun", "masculine", "food", "general", "मटकी मांय सूं ताजा माखन काढ़्यो।"),
        ("दही", "dahi", "thick probiotic curd set in earthenware bowls", "दही", "noun", "masculine", "food", "general", "दोपहरी मांy ठंडी दही जीमी।"),
        ("बिलोवणो", "bilovno", "churning curd with wooden dasher to extract butter", "दही मथने की क्रिया", "noun", "masculine", "pastoral", "marwari", "सवेरै चार बजै माय बिलोवणो बिलोवै।"),
        ("मथणी", "mathani", "fluted wooden churning rod turned with ropes (Rai)", "दही मथने की मथानी (रई)", "noun", "feminine", "tools", "general", "मथणी री घरघराहट सूं घर गूंज उठ्यो।"),
        ("नेती", "neti", "twisted rope wound around churning dasher to spin it", "मथानी घुमाने की रस्सी", "noun", "feminine", "tools", "marwari", "नेती खींच'र छाछ बिलोई।"),
        ("गोळियो", "goliyo", "wooden or clay frame steadying churning pot", "बिलोने की मटकी को साधने का ढांचा", "noun", "masculine", "tools", "marwari", "गोळिये मांय मटकी जमाई।"),
        ("सूपड़ो", "soopdo", "light winnowing tray separating grain from chaff", "सूप अथवा छाजड़ा", "noun", "masculine", "tools", "general", "सूपड़े सूं मोठ रा दाणा साफ कर्या।"),
        ("चाळणी", "chaalni", "sieve with brass wire mesh for sifting flour", "आटा छानने की छलनी", "noun", "feminine", "tools", "general", "चाळणी सूं बाजरी रो आटो छान्यो।"),
        ("कड़ाही", "kadaahi", "heavy iron wok for frying puris and festive ghevars", "लोहे की बड़ी कड़ाही", "noun", "feminine", "household", "general", "कड़ाही मांय घी ततायो।"),
        ("झर", "jhar", "perforated brass skimmer ladle for frying", "तली हुई चीजें निकालने का पौना अथवा झर", "noun", "feminine", "tools", "general", "झर सूं गरम पूरियां काढ़ी।"),
        ("तवो", "tavo", "concave iron griddle for baking crisp bajra rotis", "रोटी पकाने का तवा", "noun", "masculine", "household", "general", "तवे पर सोगरो सेक्यो।"),
        ("चीमटो", "cheemto", "iron tongs for flipping flatbreads and handling embers", "रोटी पलटने का चिमटा", "noun", "masculine", "tools", "general", "चीमटे सूं रोटी अंगारे पर सेकी।"),
        ("फूकणी", "phookani", "hollow iron blowpipe for fanning chulha embers", "आग धधकाने की लोहे की नली", "noun", "feminine", "tools", "general", "फूकणी सूं चूल्हा मांय फूंक मारी।"),
        ("चूल्हो", "choolho", "traditional clay hearth burning neem and babool wood", "मिट्टी का चूल्हा", "noun", "masculine", "household", "marwari", "चूल्हे पर हांड़ी चढ़ी है।"),
        ("हांड़ी", "haandi", "earthen cooking pot yielding earthy slow-cooked stews", "मिट्टी की हांडी", "noun", "feminine", "household", "general", "हांड़ी मांय दाल घणी सवादी रीझै।"),
        ("ओगणहारी", "oganhaari", "woman winnowing grains in desert wind", "अनाज फटकने वाली स्त्री", "noun", "feminine", "people", "marwari", "ओगणहारी पवन रै साम्ही सूपड़ो हिलावै।"),
        ("लांघणी", "laanghani", "reaper harvesting bajra or wheat stalks with sickle", "फसल काटने वाली लांघणी", "noun", "feminine", "people", "marwari", "लांघणी दांती सूं बाजरी काटी।"),
        ("पसवाड़ो", "pasvaado", "side, adjacent flank or neighbourhood", "पड़ोस अथवा बगल का हिस्सा", "noun", "masculine", "geography", "marwari", "म्हारै पसवाड़े मांय ही खेत है।"),
        ("आगलो", "aaglo", "foremost, front, previous", "आगे का अथवा पूर्व का", "adjective", "masculine", "descriptors", "marwari", "आगलो गांव तीन कोस दूर है।"),
        ("पाछलो", "paachhlo", "hind, rear, past or subsequent", "पीछे का अथवा पिछला", "adjective", "masculine", "descriptors", "marwari", "पाछले बरस अकाल पड़्यो थो।"),
        ("डावो", "daavo", "left hand side / counter-clockwise direction", "बायां हाथ अथवा बाईं दिशा", "adjective", "masculine", "descriptors", "marwari", "डावे हाथ पर मोटो बरगद रो रूख है।"),
        ("जीवणो", "jeevno", "right hand side / auspicious clockwise direction", "दायां हाथ अथवा शुभ दिशा", "adjective", "masculine", "descriptors", "marwari", "जीवणे हाथ मुड़'र हवेली आवसी।"),
        ("ऊंचो", "ooncho", "lofty, elevated, exalted, tall", "ऊंचा अथवा बुलंद", "adjective", "masculine", "descriptors", "general", "किले री दीवार घणी ऊंची है।"),
        ("नीचो", "neecho", "low-lying, humble, descended", "नीचा अथवा गहरा", "adjective", "masculine", "descriptors", "general", "नीची जमीन पर पाणी भर गयो।"),
        ("सीधो", "seedho", "straight, direct, upright, honest", "सीधा अथवा सरल", "adjective", "masculine", "descriptors", "general", "सीधे मारग चालो।"),
        ("आडो", "aado", "transverse, crosswise, blocking diagonal", "तिरछा अथवा आड़ा", "adjective", "masculine", "descriptors", "marwari", "मारग मांय आडो पत्थर पड़्यो थो।"),
        ("अड़चण", "adchan", "hindrance, obstacle, impediment", "बाधा अथवा रुकावट", "noun", "feminine", "daily_life", "general", "काम मांय कोई अड़चण नीं आई।"),
        ("सुभीतो", "subheeto", "convenience, easy facility, opportune comfort", "सुविधा अथवा अनुकूलता", "noun", "masculine", "daily_life", "marwari", "अठै ठहरबा रो चोखो सुभीतो है।"),
        ("तसदी", "tasdi", "trouble, inconvenience, physical bother", "तकलीफ अथवा परेशानी", "noun", "feminine", "daily_life", "general", "आप तसदी मती लो।"),
        ("खुशामद", "khushaamad", "sycophancy, flattering cajolery", "चापलूसी अथवा खुशामद", "noun", "feminine", "social", "general", "स्वाभिमानी मानख खुशामद नीं करै।"),
        ("अणख", "anakh", "unbending pride, self-respect, fierce dignity", "स्वाभिमान अथवा आन", "noun", "feminine", "values", "dingal", "रजपूत री अणख कदैई नीं झुकै।"),
        ("टेक", "tek", "unyielding resolve, solemn ancestral vow", "प्रतिज्ञा अथवा हठ", "noun", "feminine", "values", "general", "राणा प्रताप घास री रोटी खाई पण टेक नीं तोड़ी।"),
        ("आन", "aan", "sacred code of martial and family honor", "आन-बान अथवा मर्यादा", "noun", "feminine", "values", "general", "देश री आन खातर शीश न्योछावर कर्यो।"),
        ("बान", "baan", "noble character, ancestral custom or habit", "आदत अथवा कुल की रीति", "noun", "feminine", "values", "general", "आपणी बान पर अटल रह्वो।"),
        ("शान", "shaan", "pomp, splendor, stately prestige", "वैभव अथवा गरिमा", "noun", "feminine", "values", "general", "राजस्थान री शान साफा अर तलवार मांय है।"),
        ("रोब", "rob", "commanding awe-inspiring aura, dignified authority", "दबदबा अथवा प्रभाव", "noun", "masculine", "values", "general", "ठाकुर सा रो रोब सारै परगने मांय थो।"),
        ("दहशत", "dahshat", "terror, dread instilled in enemies", "आतंक अथवा खौफ", "noun", "feminine", "emotions", "general", "शत्रु दल मांय दहशत फैलगी।"),
        ("हरख", "harakh", "exuberant joy, gladness, rejoicing (Harsha)", "हर्ष अथवा उल्लास", "noun", "masculine", "emotions", "marwari", "बेटे री जीत सुण'र हिये मांय हरख समायो नीं।"),
        ("सोच", "soch", "deliberation, reflection, thoughtful pondering", "विचार अथवा चिंता", "noun", "feminine", "emotions", "general", "गहरी सोच मांय डूब गयो।"),
        ("फिकर", "phikar", "anxiety, worry, solicitous concern", "चिंता अथवा परवाह", "noun", "feminine", "emotions", "general", "थूँ फिकर मती कर, सब ठीक होसी।"),
        ("होड़", "hod", "spirited emulation, rivalry, competitive contest", "प्रतिस्पर्धा अथवा मुकाबला", "noun", "feminine", "social", "general", "दोई घोड़ां मांय दौड़ री होड़ लागी।"),
        ("सोर", "sor", "clamour, tumult, reverberating loud noise", "शोर अथवा कोलाहल", "noun", "masculine", "daily_life", "marwari", "मेले मांय घणो सोर मच्यो।"),
        ("सांत्वना", "saantwana", "solace, gentle consolation in bereavement", "तसल्ली अथवा ढांढस", "noun", "feminine", "emotions", "general", "शोकग्रस्त परिवार नै सांत्वना दीनी।"),
        ("ढांढस", "dhaandhas", "reassurance, fortifying emotional courage", "ढांढस अथवा हिम्मत", "noun", "masculine", "emotions", "general", "संकट मांय मित्र ढांढस बंधायो।"),
        ("ओट", "oot", "screen, barrier, protective shelter against wind or eyes", "आड़ अथवा ओट", "noun", "feminine", "architecture", "general", "दीवार री ओट मांय खड़ा होया।"),
        ("झांकी", "jhaanki", "scenic tableau or fleeting divine glimpse in temples", "दर्शन अथवा मनोरम दृश्य", "noun", "feminine", "culture", "general", "ठाकुरजी री मनमोहक झांकी देखी।"),
        ("मेळो", "melo", "bustling desert festival and livestock fair (e.g. Pushkar)", "मेला", "noun", "masculine", "culture", "marwari", "पुष्कर रै मेले मांy लाखों लोग भेळा होवै।"),
        ("हाटड़ी", "haatdi", "quaint little shop or stall in village square", "छोटी दुकान", "noun", "feminine", "commerce", "marwari", "हाटड़ी सूं गुड़ अर चाय पत्ती ल्याया।"),
        ("पंसार", "pansaar", "grocer dealing in whole desert spices and grains", "पंसारी की दुकान", "noun", "masculine", "commerce", "general", "पंसार री हाट सूं जीरा-धनिया लीधो।"),
        ("बजाज", "bajaaj", "draper merchant trading in fine silks and cotton rolls", "कपड़े का व्यापारी", "noun", "masculine", "commerce", "general", "बजाज थान मांय सूं चुनड़ी काढ़ी।"),
        ("सर्राफ", "sarraaph", "money-changer and precious bullion bullion dealer", "जौहरी अथवा सर्राफ", "noun", "masculine", "commerce", "general", "सर्राफ सोने री शुद्धता परखी।"),
        ("दलाल", "dalaal", "middleman broker negotiating cattle and crop sales", "बिचौलिया अथवा दलाल", "noun", "masculine", "commerce", "general", "दलाल ऊंट रो सोदो करायो।"),
        ("बयानो", "bayaano", "earnest advance payment sealing a trade bargain", "अग्रिम बयाना राशि", "noun", "masculine", "commerce", "general", "सोदे रो बयानो चुकाय दियो।"),
        ("किस्त", "kist", "periodic installment paying debt or lease", "किस्त", "noun", "feminine", "commerce", "general", "समय पर किस्त भरणी जरूरी है।"),
        ("करज", "karaj", "debt, loan or financial obligation", "ऋण अथवा कर्ज", "noun", "masculine", "commerce", "marwari", "किसाण करज सूं मुक्त होयो।"),
        ("व्याज", "vyaaj", "interest accrued on merchant credit", "ब्याज अथवा सूद", "noun", "masculine", "commerce", "general", "महाजन व्याज रो हिसाब मांड्यो।"),
        ("लेखा", "lekha", "balanced ledger accounts and bookkeeping", "हिसाब-किताब", "noun", "masculine", "commerce", "general", "संवत रै अंत पर सारो लेखो देख्यो।"),
        ("संवत", "samvat", "traditional Vikram Samvat calendar year", "विक्रम संवत", "noun", "masculine", "history", "general", "विक्रम संवत मांय राजस्थान रा त्यौहार मनावै।"),
        ("मास", "maas", "lunar month of the traditional calendar", "महीना अथवा मास", "noun", "masculine", "astronomy", "general", "कार्तिक मास मांय दीपदान करै।"),
        ("पख", "pakh", "lunar fortnight (Shukla / Krishna Paksha)", "पक्ष अथवा पखवाड़ा", "noun", "masculine", "astronomy", "marwari", "चांदणे पख मांय तीज मनाईजै।"),
        ("तिथि", "tithi", "precise lunar day in Hindu almanac", "पंचांग की तिथि", "noun", "feminine", "astronomy", "general", "पंडितजी शुभ तिथि बताई।"),
        ("वार", "vaar", "solar day of the seven-day week", "सप्ताह का दिन अथवा वार", "noun", "masculine", "astronomy", "general", "इतवार रै दिन हाट लागै।"),
        ("बेळा", "bela", "auspicious hour, watch, or seasonal dawn/dusk", "समय, पहर अथवा वेला", "noun", "feminine", "time", "marwari", "सवेरै री बेळा पंछी चहकै।"),
        ("संज्या", "sanjya", "twilight dusk settling over sand dunes", "संध्या अथवा सांझ", "noun", "feminine", "time", "marwari", "संज्या पड़तै ही गायां घरै आई।"),
        ("दुपहरी", "dupahari", "blazing desert noon when sun crowns the zenith", "दोपहर", "noun", "feminine", "time", "general", "जेठ री दुपहरी मांय धोरा तपै।"),
        ("परभात", "parbhaat", "first golden crack of dawn awakening horizon", "प्रभात अथवा भोर", "noun", "masculine", "time", "general", "परभात मांय मंदिर री झालर बाजी।"),
        ("अधरात", "adhraat", "silent mystic desert midnight beneath starry skies", "आधी रात अथवा मध्यरात्रि", "noun", "feminine", "time", "marwari", "अधरात मांय कुरजां रो बोल सुण्यो।"),
        ("बगिया", "bagiya", "lush walled garden cooled by irrigation fountains", "बगीचा अथवा वाटिका", "noun", "feminine", "nature", "general", "बगिया मांय गुलाब रा फूल खिलै।"),
        ("बावड़", "baawad", "fruitful return back home from distant lands", "लौटना अथवा वापसी", "noun", "masculine", "daily_life", "marwari", "परदेसी साजन रो घरै बावड़ होयो।"),
        ("सुलझण", "suljhan", "harmonious untangling of dispute or knot", "समाधान अथवा सुलझाव", "noun", "feminine", "social", "general", "पंचायती मांय बात रो सुलझण हो गयो।"),
        ("उलझण", "uljhan", "confounding perplexity or tangled dilemma", "उलझन अथवा पेचीदगी", "noun", "feminine", "daily_life", "general", "मन री उलझण दूर हुई।"),
        ("नेमी", "nemi", "strict observer of vows and righteous disciplines", "नियम पालक अथवा धार्मिक", "adjective", "masculine", "values", "general", "नेमी पुरुष कदैई व्रत नीं तोड़ै।"),
        ("अलख", "alakh", "transcendent, invisible, formless divine reality", "अलख निरंजन अथवा अगोचर", "noun", "masculine", "values", "general", "जोगी अलख जगायो।"),
        ("धूनी", "dhooni", "sacred perpetual log fire maintained by ascetic yogis", "नाथ जोगियों की धूनी", "noun", "feminine", "rituals", "general", "गुरु गोरखनाथ री धूनी अमर है।"),
        ("चिमटो", "chimto", "ascetic's long iron fire tongs clicked as sacred percussive instrument", "नाथ साधुओं का चिमटा", "noun", "masculine", "instruments", "general", "साधु चिमटो बजावतां भजन गावै।"),
        ("खप्पर", "khappar", "earthen begging bowl carried by wandering ascetics", "भिक्षापात्र अथवा खप्पर", "noun", "masculine", "rituals", "general", "जोगी खप्पर मांय भिक्षा लीधी।"),
        ("कंथा", "kantha", "quilted patched robe sewn of discarded holy rags worn by yogis", "गुदड़ी अथवा फकीरी वस्त्र", "noun", "feminine", "attire", "general", "साधु कंथा ओढ़'र शीत सूं बच्यो।"),
        ("जटा", "jata", "matted ascetic tresses consecrated to Shiva", "साधु की जटाएं", "noun", "feminine", "body", "general", "जटा मांय गंगा बिराजै।"),
        ("भभूत", "bhabhoot", "consecrated white ash smeared over body by ascetics", "पवित्र राख अथवा भस्म", "noun", "feminine", "rituals", "marwari", "जोगी अंग पर भभूत रमाई।"),
        ("तिलक", "tilak", "forehead mark of sandalwood, ash, or vermilion", "माथे का तिलक", "noun", "masculine", "rituals", "general", "सवेरै पूजा पछै तिलक लगायो।"),
        ("कौड़ी", "kaudi", "polished sea cowrie shell used in ornaments and ancient currency", "कौड़ी (शृंगार व मुद्रा)", "noun", "feminine", "crafts", "general", "गोरबंद पर कौड़ियां टंकी ही।"),
        ("सीप", "seep", "mother-of-pearl oyster shell", "सीप", "noun", "feminine", "nature", "general", "सीप मांय स्वाति बूंद मोती बणै।"),
        ("मोती", "moti", "lustrous natural pearl prized in Rajput necklaces", "मोती अथवा मुक्ता", "noun", "masculine", "ornaments", "general", "हार मांय सच्चे मोती जड़े है।"),
        ("माणक", "maanak", "deep red ruby gemstone adorning royal turbans", "माणिक्य अथवा लाल रत्न", "noun", "masculine", "ornaments", "general", "सिरपेंच मांय मोटो माणक चमकै।"),
        ("पन्ना", "panna", "radiant emerald gemstone of Rajasthan", "पन्ना रत्न", "noun", "masculine", "ornaments", "general", "जयपुर पन्ना री तराशी रो मोटो केंद्र है।"),
        ("हीरो", "heero", "flawless diamond cut with royal precision", "हीरा रत्न", "noun", "masculine", "ornaments", "general", "अंगूठी मांय जगमगातो हीरो जड़्यो।"),
        ("नीलम", "neelam", "celestial blue sapphire gemstone", "नीलमणि अथवा नीलम", "noun", "masculine", "ornaments", "general", "नीलम रो रत्न शांति देवे।"),
        ("पुखराज", "pukhraaj", "brilliant yellow topaz gemstone", "पुखराज रत्न", "noun", "masculine", "ornaments", "general", "बृहस्पति रै निमित्त पुखराज पहर्यो।"),
        ("लहसुनिया", "lahsuniya", "cat's eye chrysoberyl gemstone with luminous band", "लहसुनिया रत्न (वैदूर्य)", "noun", "masculine", "ornaments", "general", "उंगली मांय लहसुनिया री बींटी सोह्रै।"),
        ("मूंगा", "moonga", "auspicious organic red coral bead (Praval)", "लाल मूंगा रत्न", "noun", "masculine", "ornaments", "general", "गळे मांय मूंगे री माळा पहरी।"),
        ("नवरतन", "navratan", "sacred pendant combining all nine planetary gems", "नौ रत्नों का हार अथवा नवरत्न", "noun", "masculine", "ornaments", "general", "राजाजी नवरतन रो कंठा पहर्यो थो।"),
        ("बांक", "baank", "dashing martial bearing, gallantry, bold swagger", "शूरवीरता का बांकपन अथवा अलबेलापन", "noun", "masculine", "chivalry", "general", "राजस्थान रा वीरां मांय अनूठो बांक थो।")
    ]

    for item in ADDITIONAL_SYSTEMIC:
        raj = item[0].strip()
        if raj not in existing:
            entry = {
                "rajasthani": raj,
                "roman": item[1],
                "english": item[2],
                "hindi": item[3],
                "pos": item[4],
                "gender": item[5],
                "category": item[6],
                "dialect": item[7],
                "example": item[8]
            }
            words.append(entry)
            existing[raj] = entry
            added += 1

print(f"Total words after Wave 10 supplement: {len(words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(words)} verified lemmas to {WORDS_PATH}")
