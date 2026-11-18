# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Lifecycle Rituals & Cultural Rites (संस्कार अर रीत-रिवाज)
========================================================================================
Comprehensive catalog of authentic traditional Rajasthani rituals:
1. Pregnancy & Natal Rites (सीमंत, छठी, नामकरण, जलवा, जड़ूलो, ढूंढ, कर्णवेध)
2. Wedding Ceremonies (सगाई, टीका, लगन, चाक, पीठी, माहेरो, रातीजोगा, बिंदौरी, सामेला, तोरण, हथलेवा, फेरा, विदाई, कंकण-डोरा, पगफेरा)
3. Seasonal Folk & Deific Observances (गणगौर, तीज, बासोड़ा, आखा तीज, बछ बारस, गोगा नवमी, तेजा दशमी, रामदेवरा)
4. Memorial Observances (तीया, मोसर, पगड़ी रसम)
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CulturalRitual:
    name: str
    roman: str
    category: str  # birth_childhood, wedding, festival_ritual, memorial
    description: str
    customs_and_practices: str
    cultural_significance: str


RITUALS_DATABASE: List[CulturalRitual] = [
    # =========================================================================
    # 1. PREGNANCY, NATAL & CHILDHOOD RITUALS (गर्भ, जन्म अर बाल संस्कार)
    # =========================================================================
    CulturalRitual(
        name="सीमंतोन्नयन / अग्यारणी / आठवां (Agharni / Aathwan)",
        roman="Agharni / Aathwan",
        category="birth_childhood",
        description="Auspicious celebration during the seventh or eighth month of first pregnancy praying for safe delivery and mother-child well-being.",
        customs_and_practices="Maternal parents bring green bangles, silk odhani, dry fruits, and sweets; seven fortunate women fill the expectant mother's lap (गोद भराई).",
        cultural_significance="Psychological reassurance and familial blessing celebrating the inception of motherhood in joint families.",
    ),
    CulturalRitual(
        name="सांथी रो मांडणो (Santhi Ro Mandano)",
        roman="Santhi Ro Mandano",
        category="birth_childhood",
        description="Drawing of auspicious protective Swastika (सांथी) and deity symbols at the threshold of the confinement room immediately following childbirth.",
        customs_and_practices="Elder women use red vermilion and cow dung to mark the doorway, hanging protective neem leaves to ward off infections and negative energies.",
        cultural_significance="Traditional eco-sanitary barrier and spiritual invocation for maternal and infant protection.",
    ),
    CulturalRitual(
        name="छठी पूजन (Chhathi Pujan)",
        roman="Chhathi Pujan",
        category="birth_childhood",
        description="Sacred observance on the sixth night following birth when Goddess Vidhata (विधाता/बेमाता) is believed to inscribe the infant's lifelong destiny.",
        customs_and_practices="A clean white cloth, paper, pen, kajal, and oil lamp are placed on a wooden stool near the infant; family keeps night-long vigil singing devotional hymns.",
        cultural_significance="Reverence for divine destiny, cosmic providence, and protection from infant mortality.",
    ),
    CulturalRitual(
        name="नामकरण संस्कार (Namkaran Sanskar)",
        roman="Namkaran Sanskar",
        category="birth_childhood",
        description="Formal naming rite conducted on the 10th or 12th day under the astrological constellation determined by the family pandit.",
        customs_and_practices="Havan is performed; father or paternal aunt whispers the chosen name into the child's right ear using a betel leaf, followed by distributing jaggery or lapsi.",
        cultural_significance="Bestowal of cultural identity, cosmic alignment, and integration into the ancestral clan.",
    ),
    CulturalRitual(
        name="कुआँ पूजन / जलवा पूजन (Kuan Pujan / Jalwa)",
        roman="Kuan Pujan / Jalwa",
        category="birth_childhood",
        description="Pivotal post-natal purification ceremony marking the end of the post-partum seclusion period and thanksgiving to the water deity.",
        customs_and_practices="Mother is adorned in yellow 'Peela' odhani, walks to the village well or stepwell carrying an ornate brass pot crowned with coconut, singing Badhai songs.",
        cultural_significance="Veneration of water (वरुण देव) as the sacred fountain of life in the arid desert realm.",
    ),
    CulturalRitual(
        name="जड़ूलो (Jadoolo - Tonsure / Mundan)",
        roman="Jadoolo",
        category="birth_childhood",
        description="First tonsure of child's hair solemnized exclusively at the ancestral temple shrine of the clan deity (Kuldevi/Kuldevta).",
        customs_and_practices="Child's natal hair is cleanly shaved, cooling paste of curd and turmeric is applied, and sweet churma/lapsi prasad is offered to the deity.",
        cultural_significance="Ritual shedding of prenatal impurities and securing the everlasting protective shield of the clan deities.",
    ),
    CulturalRitual(
        name="ढूंढ (Dhoondh)",
        roman="Dhoondh",
        category="birth_childhood",
        description="Festive social rite during the spring festival of Holi for children born during the preceding year.",
        customs_and_practices="Maternal uncle sends lavish gifts of traditional clothes, sweets, and silver ornaments; neighborhood women gather to sing humorous and blessing folk songs.",
        cultural_significance="Reinforces the indelible affection and reciprocal gift-giving duty of the maternal uncle (मामो) towards the child.",
    ),
    CulturalRitual(
        name="कर्णवेध (Karnavedha - Ear Piercing)",
        roman="Karnavedha",
        category="birth_childhood",
        description="Traditional ear-lobe piercing ceremony performed on boys and girls around 3-5 years of age.",
        customs_and_practices="Sunar (goldsmith) pierces ears with gold wire or needle; boys are fitted with gold Murkis while girls receive Balis/Jhumkis, followed by feeding sweet halwa.",
        cultural_significance="Acupressure benefits recognized in Ayurveda promoting mental agility and eyesight.",
    ),

    # =========================================================================
    # 2. WEDDING & MATRIMONIAL CUSTOMS (ब्याव-शादी रा रीत-रिवाज)
    # =========================================================================
    CulturalRitual(
        name="सगाई / रोक (Sagai / Roka)",
        roman="Sagai / Roka",
        category="wedding",
        description="Formal betrothal sealing the matrimonial alliance between the two families.",
        customs_and_practices="Bride's family visits the groom's residence, offers coconut (श्रीफल), silver rupee, and sweets; tilak is applied to the groom's forehead.",
        cultural_significance="Public solemnization of contract between two lineages, uniting two extended communities.",
    ),
    CulturalRitual(
        name="टीका / दस्तूर (Teeka / Dastoor)",
        roman="Teeka / Dastoor",
        category="wedding",
        description="Grand aristocratic engagement ceremony involving exchange of customary gifts, sword, jewels, and lineage crests.",
        customs_and_practices="Groom receives royal sword, mare, gold chains, and ceremonial robes from the bride's father in presence of community elders.",
        cultural_significance="Display of chivalric heritage, mutual prestige, and reciprocal respect between clans.",
    ),
    CulturalRitual(
        name="लगन पत्रिका (Lagan Patrika)",
        roman="Lagan Patrika",
        category="wedding",
        description="Formal handwritten wedding invitation letter prepared by the royal astrologer with auspicious dates, planetary positions, and exact mahurat.",
        customs_and_practices="Rolled parchment tinted with turmeric and vermilion is carried by the family priest or barber to the groom's house and read aloud before assembled kin.",
        cultural_significance="Sacred astrological sanction ensuring cosmic harmony for the marital union.",
    ),
    CulturalRitual(
        name="चाक पूजना (Chak Poojna)",
        roman="Chak Poojna",
        category="wedding",
        description="Pre-wedding ritual where married women visit the village potter's home to venerate the potter's wheel (प्रजापति चाक).",
        customs_and_practices="Women dance in procession carrying a decorated pot; raw clay cooking vessels and ceremonial kalash for the wedding are purchased and blessed.",
        cultural_significance="Honoring the artisan community and invoking the blessings of Lord Brahma/Prajapati for familial fertility.",
    ),
    CulturalRitual(
        name="बान बैठना अर पीठी (Baan Baithna / Peethi)",
        roman="Baan Baithna / Peethi",
        category="wedding",
        description="Ritual purification and beautification regimen lasting 3 to 7 days before the wedding ceremony.",
        customs_and_practices="Fragrant ubtan paste of turmeric, mustard oil, barley flour, and sandalwood is massaged onto bride/groom by seven auspicious married women.",
        cultural_significance="Enhances bridal radiance while providing natural antiseptic shielding against desert dust.",
    ),
    CulturalRitual(
        name="माहेरो / भात (Mayera / Bhaat)",
        roman="Mayera / Bhaat",
        category="wedding",
        description="The emotional centerpiece of Rajasthani weddings where maternal uncles bear gifts, wedding finances, and jewels.",
        customs_and_practices="Mama and Mami are greeted at the village boundary with aarti and singing; mama drapes the ceremonial Chunari over his sister and showers gold/silver upon the newlyweds.",
        cultural_significance="Immortalized through the legendary narrative of Narsi Mehta ('नरसीजी रो माहेरो'), demonstrating unconditional maternal love.",
    ),
    CulturalRitual(
        name="रातीजोगा (Raatijoga)",
        roman="Raatijoga",
        category="wedding",
        description="Night-long musical vigil held on the eve of the wedding honoring 33 crore deities, ancestors (पितर), and clan deities.",
        customs_and_practices="Matriarchs sing unbroken cycle of traditional hymns through the night without sleep, concluding with the dawn song 'कुकड़ू' (rooster's call).",
        cultural_significance="Invoking universal divine blessings and ensuring cosmic safety before the departure of the wedding party.",
    ),
    CulturalRitual(
        name="बिंदौरी / बन्दोली (Bindori)",
        roman="Bindori",
        category="wedding",
        description="Joyous royal procession where bride or groom is paraded across village streets in royal finery accompanied by brass bands.",
        customs_and_practices="Groom rides a caparisoned mare (घोड़ी) holding a sword; relatives invite the groom into their courtyards, feed sweets, and offer cash gifts.",
        cultural_significance="Expressing community celebration, communal pride, and collective affection before departure.",
    ),
    CulturalRitual(
        name="सामेला / धूली-अर्घ (Samela / Dhuli-Argh)",
        roman="Samela / Dhuli-Argh",
        category="wedding",
        description="Ceremonial reception of the groom's procession (बारात) by the bride's father and elders at the threshold of the wedding destination.",
        customs_and_practices="The two fathers-in-law (ब्याई) embrace three times, sprinkle rose water, exchange saffron turbans and shawls, and bestow cash honoraria (मिलावा).",
        cultural_significance="Public solemnization of mutual alliance and equality between two families.",
    ),
    CulturalRitual(
        name="तोरण मारना (Toran Marna)",
        roman="Toran Marna",
        category="wedding",
        description="Heroic archway custom where the groom, mounted on his horse, strikes the decorative wooden Toran hung above the portal with his sword.",
        customs_and_practices="Bride's mother performs aarti with lit camphor, gently teasingly pulls the groom's nose (नाक खींचना) in affectionate challenge.",
        cultural_significance="Relic of chivalric epochs symbolizing groom demonstrating fitness and martial courage to win his bride.",
    ),
    CulturalRitual(
        name="हथलेवा (Hathleva)",
        roman="Hathleva",
        category="wedding",
        description="Sacred joining of hands where the groom's right palm is placed over the bride's palm with betel leaf, coin, and turmeric paste.",
        customs_and_practices="Hands are bound together with a sacred red-and-yellow thread (मौली) as priests chant Vedic mantras uniting their destinies.",
        cultural_significance="Symbolizes lifelong companionship, shared duty, and mutual physical and spiritual union.",
    ),
    CulturalRitual(
        name="फेरा अर सप्तपदी (Phera and Saptapadi)",
        roman="Phera and Saptapadi",
        category="wedding",
        description="Seven sacred circumambulations around the holy agni fire solemnizing the marital bond.",
        customs_and_practices="Groom leads the first four pheres emphasizing dharma, artha, and kama; bride leads the final three emphasizing spiritual release and household dominance.",
        cultural_significance="Inviolable covenant before Agni Devta establishing eternal marriage.",
    ),
    CulturalRitual(
        name="गाठजोड़ो (Gathjodo)",
        roman="Gathjodo",
        category="wedding",
        description="Tying of the groom's shoulder mantle (दुपट्टा) to the corner of the bride's odhani by the groom's sister.",
        customs_and_practices="Knotted fabric holds coins, turmeric root, and rice grains, ensuring they remain inseparable throughout rituals.",
        cultural_significance="Symbolizes the metaphysical cord binding their life paths.",
    ),
    CulturalRitual(
        name="सीख अर विदाई (Seekh and Vidai)",
        roman="Seekh and Vidai",
        category="wedding",
        description="Emotional farewell ceremony where the bride takes leave of her childhood parental home.",
        customs_and_practices="Bride tosses fistfuls of raw puffed rice over her head into her mother's apron, wishing eternal prosperity upon her maternal home.",
        cultural_significance="Poignant transition acknowledging her enduring gratitude to her parents.",
    ),
    CulturalRitual(
        name="गृह प्रवेश अर कंकण-डोरा खोलना (Griha Pravesh and Kankan Dora)",
        roman="Griha Pravesh and Kankan Dora",
        category="wedding",
        description="Welcoming the new bride into the groom's ancestral home followed by playful community bonding games.",
        customs_and_practices="Bride overturns a pot filled with grain at the threshold with her right foot; newlyweds untie each other's sacred wedding wristlets (कंकण-डोरा).",
        cultural_significance="Invoking Goddess Lakshmi's entrance into the home and fostering intimacy between bride and groom.",
    ),
    CulturalRitual(
        name="जुआ-जुई (Jua-Jui)",
        roman="Jua-Jui",
        category="wedding",
        description="Playful traditional post-wedding parlor game played in the presence of the joint family.",
        customs_and_practices="A gold ring is immersed in a large brass platter filled with milk, water, and vermilion; bride and groom race to retrieve it.",
        cultural_significance="Ice-breaking humor and affectionate entertainment cementing family affection.",
    ),
    CulturalRitual(
        name="पगफेरा / मुकलावा (Pagphera / Muklawa)",
        roman="Pagphera / Muklawa",
        category="wedding",
        description="First homecoming return of the newlywed bride to her parental home shortly after the wedding.",
        customs_and_practices="Bride's brother comes to fetch her; after staying a few weeks, she permanently relocates to her husband's home.",
        cultural_significance="Gentle psychosocial adjustment for the young bride transitioning into married life.",
    ),

    # =========================================================================
    # 3. SEASONAL, FESTIVAL & DEIFIC RITUALS (ऋतु, त्योहार अर लोक-देवता)
    # =========================================================================
    CulturalRitual(
        name="गणगौर पूजन (Gangaur Pujan)",
        roman="Gangaur Pujan",
        category="festival_ritual",
        description="The ultimate spring festival of Rajasthan celebrating Goddess Gauri (Parvati) and Lord Isar (Shiva).",
        customs_and_practices="Women fast, mold clay idols of Isar and Gauri, sing delicate Gangaur songs, carry lit clay pots (घुड़लो) on their heads, and take out grand palanquin processions.",
        cultural_significance="Celebrates conjugal love, marital longevity (सुहाग), and the blooming beauty of spring.",
    ),
    CulturalRitual(
        name="तीज पूजन (Teej Pujan - Hariyali & Kajli Teej)",
        roman="Teej Pujan",
        category="festival_ritual",
        description="Monsoon festival welcoming rainfall, green vegetation, and the reunion of Shiva and Parvati.",
        customs_and_practices="Women dress in Leheriya odhanis, apply intricate henna, swing on tree-hung decorated swings (झूला), and relish Ghevar.",
        cultural_significance="Rejoicing the transformation of the arid landscape into lush fertility.",
    ),
    CulturalRitual(
        name="शीतला अष्टमी / बासोड़ा (Sheetla Ashtami / Basoda)",
        roman="Sheetla Ashtami / Basoda",
        category="festival_ritual",
        description="Spring worship of Goddess Sheetla on the eighth day after Holi, where no domestic cooking fires are lit.",
        customs_and_practices="Families consume cold, stale food (बासी खाना - राबड़ी, पूरी, लापसी) cooked the preceding evening, offering curd and cold water to the Goddess.",
        cultural_significance="Ayurvedic transition marking the onset of summer, promoting digestive cooling and disease prevention.",
    ),
    CulturalRitual(
        name="आखा तीज (Akshaya Tritiya)",
        roman="Akshaya Tritiya",
        category="festival_ritual",
        description="Unblemished auspicious day marking the traditional agricultural new year and founding anniversary of cities (Bikaner, Udaipur).",
        customs_and_practices="Farmers perform symbolic ploughing of fields (हळ जोतना); families feast on whole millet Khichda and sweet Imarti while flying paper kites.",
        cultural_significance="Praying for plentiful monsoon rains and bumper crop yield.",
    ),
    CulturalRitual(
        name="बछ बारस (Bachh Baras - Gau-Vatsa Dwadashi)",
        roman="Bachh Baras",
        category="festival_ritual",
        description="Reverential autumn celebration honoring mothers, cows, and nursing calves.",
        customs_and_practices="Mothers fast for the prosperity of sons; cows with calves are anointed with sandalwood paste and fed sprouted moth beans; knife-cut food and cow milk are avoided.",
        cultural_significance="Expressing profound pastoral gratitude for bovine companionship.",
    ),
    CulturalRitual(
        name="गोगा नवमी (Goga Navami)",
        roman="Goga Navami",
        category="festival_ritual",
        description="Festival devoted to folk deity Goga Ji Maharaj (Jaharveer) as protector against snake venom and pastoral dangers.",
        customs_and_practices="Devotees visit Goga Medi shrines, carry blue banners (निशान), sing heroic sagas accompanied by Deru drums, and offer milk and kheer.",
        cultural_significance="Deep-rooted agrarian faith overcoming desert hazards.",
    ),
    CulturalRitual(
        name="तेजा दशमी (Teja Dashami)",
        roman="Teja Dashami",
        category="festival_ritual",
        description="Folk commemoration honoring Veer Tejaji who laid down his life protecting cows from bandits and honoring his sacred word to a serpent.",
        customs_and_practices="Large livestock and cattle fairs are held across Parbatsar and Marwar; sacred protective threads (तांती) are tied around wrists.",
        cultural_significance="Celebration of supreme pastoral self-sacrifice, truthfulness, and cattle protection.",
    ),
    CulturalRitual(
        name="रामदेवरा री पैदल यात्रा अर जमा (Ramdevra Yatra and Jama)",
        roman="Ramdevra Yatra and Jama",
        category="festival_ritual",
        description="Mass annual pilgrimage to the samadhi shrine of Baba Ramdevji at Runicha (Pokhran), who preached caste-free human equality.",
        customs_and_practices="Lakhs of pilgrims walk hundreds of miles waving red-and-white striped flags (ध्वजा); Kamad singers hold night-long mystic assemblies (जमा जागरण).",
        cultural_significance="Social synthesis, communal harmony, and abolition of caste divisions in devotional folk spirituality.",
    ),

    # =========================================================================
    # 4. MEMORIAL & PASSING RITES (अंतिम संस्कार अर सामाजिक मर्याद)
    # =========================================================================
    CulturalRitual(
        name="तीया री बैठक (Tiya Ri Baithak)",
        roman="Tiya Ri Baithak",
        category="memorial",
        description="Solemn communal condolence assembly held on the third day following a bereavement.",
        customs_and_practices="Community members gather silently in white attire on white cotton sheets (जाजम) to offer condolences to the grieving family.",
        cultural_significance="Community solidarity absorbing grief and reassuring the bereaved family.",
    ),
    CulturalRitual(
        name="मोसर / गंगा-प्रसादी (Mosar / Ganga Prasadi)",
        roman="Mosar / Ganga Prasadi",
        category="memorial",
        description="Post-cremation memorial rite and communion feast held on the 12th or 13th day.",
        customs_and_practices="Ancestral rituals (पिंडदान) are performed, Ganga water is consecrated, and meals of lapsi and puri are offered to community elders and relatives.",
        cultural_significance="Assisting the soul's transition to peace while affirming family continuity.",
    ),
    CulturalRitual(
        name="पगड़ी रसम (Pagdi Rasam)",
        roman="Pagdi Rasam",
        category="memorial",
        description="Sacred ceremony of investiture and succession of family responsibility following the demise of the household patriarch.",
        customs_and_practices="Maternal relatives and in-laws bring a new turban; it is solemnly wound onto the eldest son's head in front of the village panchayat.",
        cultural_significance="Generational continuity ensuring the mantle of family honor, duty, and clan leadership is preserved unbroken.",
    ),
]


def get_all_rituals() -> List[CulturalRitual]:
    """Returns all cataloged traditional Rajasthani lifecycle rituals."""
    return list(RITUALS_DATABASE)


def get_rituals_by_category(category: str) -> List[CulturalRitual]:
    """Filters rituals by category (birth_childhood, wedding, festival_ritual, memorial)."""
    return [r for r in RITUALS_DATABASE if r.category == category]
