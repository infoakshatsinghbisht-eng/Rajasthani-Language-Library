# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Syntax Engine & Split Ergativity
==============================================================
Governs SOV (Subject-Object-Verb) sentence architecture, split ergativity
in past-tense transitive constructions, object-verb agreement, and
dialectal syntactic transformation.
"""

import re
from typing import Dict, List, Optional
from rajasthani.constants import Tense, Person, Gender, GrammaticalNumber, Dialect
from rajasthani.grammar.verbs import conjugate, extract_root
from rajasthani.grammar.pronouns import PRONOUN_TABLE

# Known transitive verbs in Rajasthani
TRANSITIVE_VERBS = {
    "खाणो", "पीवणो", "करणो", "लिखणो", "पढ़णो", "देखणो", "सुणणो",
    "लेवणो", "देवणो", "बणावणो", "काढणो", "गावणो", "धोवणो",
}


class SyntaxEngine:
    """
    Rajasthani syntax analysis and generation engine.
    """

    def __init__(self, dialect: Dialect = Dialect.MARWARI):
        self.dialect = dialect

    def build_sentence(
        self,
        subject: str,
        verb: str,
        direct_object: Optional[str] = None,
        tense: Tense = Tense.PRESENT,
        person: Person = Person.THIRD,
        gender: Gender = Gender.MASCULINE,
        number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
        obj_gender: Gender = Gender.MASCULINE,
        obj_number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
        negative: bool = False,
        honorific: bool = False,
    ) -> str:
        """
        Builds a grammatical Rajasthani sentence following strict SOV order
        and split-ergative agreement principles.
        """
        infinitive = verb if verb.endswith("णो") else verb + "णो"
        is_transitive = infinitive in TRANSITIVE_VERBS

        # 1. Past Tense with Transitive Verb -> Ergative Construction!
        if tense == Tense.PAST and is_transitive:
            # Subject takes ergative marking
            subj_clean = subject.strip()
            if subj_clean == "म्हूँ":
                subj_form = "म्हैं"
            elif subj_clean == "थूँ":
                subj_form = "तैं"
            elif subj_clean in ["ओ", "यो"]:
                subj_form = "ईं"
            elif subj_clean == "वो":
                subj_form = "उण"
            elif not subj_clean.endswith("नै"):
                subj_form = f"{subj_clean} नै"
            else:
                subj_form = subj_clean

            # Verb agrees with DIRECT OBJECT, not subject!
            verb_gender = obj_gender if direct_object else gender
            verb_number = obj_number if direct_object else number
            verb_form = conjugate(
                verb,
                tense=Tense.PAST,
                person=Person.THIRD,
                gender=verb_gender,
                number=verb_number,
                dialect=self.dialect,
            )

            parts = [subj_form]
            if direct_object:
                parts.append(direct_object)
            if negative:
                parts.append("कोनी")
            parts.append(verb_form)

        # 2. Intransitive or Non-Past Tense -> Nominative-Accusative Agreement
        else:
            verb_form = conjugate(
                verb,
                tense=tense,
                person=person,
                gender=gender,
                number=number,
                dialect=self.dialect,
            )
            parts = [subject]
            if direct_object:
                parts.append(direct_object)
            if negative:
                parts.append("कोनी")
            parts.append(verb_form)

        if honorific:
            parts.append("सा")

        return " ".join(parts).strip() + "।"

    def convert_dialect(self, sentence: str, source_dial: Dialect, target_dial: Dialect) -> str:
        """
        Converts grammatical markers in a sentence across dialects.
        Example: Marwari 'वो गयो थो' -> Dhundhari 'वो गयो छो'
        """
        if source_dial == target_dial:
            return sentence

        result = sentence

        # Past copula conversion
        if source_dial == Dialect.MARWARI and target_dial == Dialect.DHUNDHARI:
            result = result.replace(" थो", " छो").replace(" थी", " छी").replace(" था", " छा")
            result = result.replace(" रो", " को").replace(" री", " की").replace(" रा", " का")
            result = result.replace(" है", " छै")
        elif source_dial == Dialect.DHUNDHARI and target_dial == Dialect.MARWARI:
            result = result.replace(" छो", " थो").replace(" छी", " थी").replace(" छा", " था")
            result = result.replace(" को", " रो").replace(" की", " री").replace(" का", " रा")
            result = result.replace(" छै", " है")
        elif source_dial == Dialect.MARWARI and target_dial == Dialect.MEWARI:
            result = result.replace(" थो", " हो").replace(" थी", " ही").replace(" था", " हा")

        return result

    def hindi_to_rajasthani(self, hindi_sentence: str, dialect: Dialect = Dialect.MARWARI) -> str:
        """
        Syntactic & morphological rule-based sentence conversion from Hindi into Rajasthani.
        Handles pronouns, postpositions, auxiliaries, tenses, and dialect-specific endings.
        """
        text = hindi_sentence.strip()
        # Direct pronouns and lexical substitutions
        replacements = [
            ("रहा था", "रह्यो थो"),
            ("रही थी", "रही थी"),
            ("रहे थे", "रह्या था"),
            ("रहा है", "रह्यो है"),
            ("रही है", "रही है"),
            ("रहे हैं", "रह्या हैं"),
            ("मैं", "म्हूँ"),
            ("हम", "आपां"),
            ("तू", "थूँ"),
            ("तुम", "थें"),
            ("वह", "वो"),
            ("यह", "यो"),
            ("वे", "वे"),
            ("ये", "ए"),
            ("मेरा", "म्हारो"),
            ("मेरी", "म्हारी"),
            ("मेरे", "म्हारा"),
            ("हमारा", "आपांरो"),
            ("हमारी", "आपांरी"),
            ("हमारे", "आपांरा"),
            ("तेरा", "थारो"),
            ("तेरी", "थारी"),
            ("तेरे", "थारा"),
            ("तुम्हारा", "थांरो"),
            ("तुम्हारी", "थांरी"),
            ("तुम्हारे", "थांरा"),
            ("उसका", "उनरो"),
            ("उसकी", "उनरी"),
            ("उसके", "उनरा"),
            ("इसका", "ईंरो"),
            ("इसकी", "ईंरी"),
            ("इसके", "ईंरा"),
            ("मुझे", "मनै"),
            ("हमें", "म्हानै"),
            ("तुम्हें", "थानै"),
            ("उसको", "उनै"),
            ("इसको", "ईंनै"),
            ("क्या", "काईं"),
            ("कहाँ", "कठे"),
            ("कब", "कदे"),
            ("कैसे", "कियां"),
            ("क्यों", "क्यूँ"),
            ("कौन", "कुण"),
            ("नहीं", "कोनी"),
            ("मत", "मती"),
            ("और", "अर"),
            ("लेकिन", "पण"),
            ("परंतु", "पण"),
            ("बहुत", "घणो"),
            ("अच्छा", "चोखो"),
            ("अच्छी", "चोखी"),
            ("अच्छे", "चोखा"),
            ("पानी", "पाणी"),
            ("था", "थो"),
            ("थी", "थी"),
            ("थे", "था"),
        ]

        # Use non-whitespace boundary matching (?<!\S)word(?!\S)
        for src, target in replacements:
            pattern = r"(?<!\S)" + re.escape(src) + r"(?!\S)"
            text = re.sub(pattern, target, text)

        # Dialect post-processing
        if dialect in [Dialect.DHUNDHARI, Dialect.HARAUTI]:
            text = self.convert_dialect(text, Dialect.MARWARI, Dialect.DHUNDHARI)
        elif dialect == Dialect.MEWARI:
            text = self.convert_dialect(text, Dialect.MARWARI, Dialect.MEWARI)

        return text

    def build_compound_verb(
        self,
        main_verb: str,
        vector_verb: str = "लेणो",
        tense: Tense = Tense.PAST,
        gender: Gender = Gender.MASCULINE,
        number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
        dialect: Dialect = Dialect.MARWARI,
    ) -> str:
        """
        Constructs an authentic Rajasthani compound verb (संयुक्त क्रिया) with vector auxiliary.
        Examples:
          - खाणो + लेणो -> खाय लियो (completed action for self)
          - देवणो + देणो -> दे दीनो (completed action for another)
          - चालणो + पड़णो -> चाल पड़्यो (sudden inception)
          - बोलणो + उठणो -> बोल उठ्यो (spontaneous utterance)
          - करणो + नांखणो -> कर नांख्यो (decisive disposal)
        """
        root = extract_root(main_verb)
        # Conjunctive participle of main verb
        if root.endswith(("ा", "ो", "ी", "ू")):
            participle = root + "य"
        else:
            participle = root

        # Special stem adjustments
        if main_verb in ["खाणो", "खा"]:
            participle = "खाय"
        elif main_verb in ["पीवणो", "पी"]:
            participle = "पीय"
        elif main_verb in ["देवणो", "दे"]:
            participle = "दे"
        elif main_verb in ["लेवणो", "ले"]:
            participle = "ले"
        elif main_verb in ["करणो", "कर"]:
            participle = "कर"

        # Conjugate vector verb
        vector_conjugated = conjugate(
            vector_verb,
            tense=tense,
            person=Person.THIRD,
            gender=gender,
            number=number,
            dialect=dialect,
        )

        # Irregular past vector forms in Rajasthani literature
        if tense == Tense.PAST:
            if vector_verb in ["देणो", "देवणो"]:
                vector_conjugated = "दीनो" if gender == Gender.MASCULINE and number == GrammaticalNumber.SINGULAR else ("दीनी" if gender == Gender.FEMININE else "दीना")
            elif vector_verb in ["लेणो", "लेवणो"]:
                vector_conjugated = "लियो" if gender == Gender.MASCULINE and number == GrammaticalNumber.SINGULAR else ("लीनी" if gender == Gender.FEMININE else "लिया")

        return f"{participle} {vector_conjugated}"

    def build_complex_sentence(
        self,
        sub_clause: str,
        main_clause: str,
        connector_type: str = "conditional",
    ) -> str:
        """
        Builds complex Rajasthani sentences with correlative clause connectors
        characteristic of classical folk vats and modern literary stories.
        Supported connector_types:
          - 'conditional': जे... तो (If... then)
          - 'temporal': जद... तद (When... then)
          - 'relative': जको... वो (The one who... that one)
          - 'spatial': जठै... वठै (Where... there)
          - 'manner': जियां... तियां (As... so)
          - 'concessive': भले ही... पण (Even if... yet)
        """
        clean_sub = sub_clause.strip().rstrip("।").rstrip(",")
        clean_main = main_clause.strip().rstrip("।")

        connectors = {
            "conditional": ("जे", "तो"),
            "temporal": ("जद", "तद"),
            "relative": ("जको", "वो"),
            "spatial": ("जठै", "वठै"),
            "manner": ("जियां", "तियां"),
            "concessive": ("भले ही", "पण"),
        }

        prefix, bridge = connectors.get(connector_type.lower(), ("जे", "तो"))
        return f"{prefix} {clean_sub}, {bridge} {clean_main}।"

    def generate_causative(self, verb: str, level: int = 1) -> str:
        """
        Derives authentic Rajasthani causative verb forms (प्रेरणार्थक क्रियावां).
        Level 1 (Direct causative - प्रत्यक्ष प्रेरणार्थक): e.g. करणो -> करावणो
        Level 2 (Mediated causative - अप्रत्यक्ष प्रेरणार्थक): e.g. करणो -> करवावणो
        """
        CAUSATIVE_REGISTRY = {
            "करणो": ("करावणो", "करवावणो"),
            "लिखणो": ("लिखावणो", "लिखवावणो"),
            "पढ़णो": ("पढ़ावणो", "पढ़वावणो"),
            "खावणो": ("जिमावणो", "जिमवावणो"),
            "पीवणो": ("पिलावणो", "पिलवावणो"),
            "सोवणो": ("सुवावणो", "सुळवावणो"),
            "धोवणो": ("धुवावणो", "धुळवावणो"),
            "देखणो": ("दिखावणो", "दिखवावणो"),
            "सुणणो": ("सुणावणो", "सुणवावणो"),
            "नाचणो": ("नचावणो", "नचवावणो"),
            "हंसणो": ("हंसावणो", "हंसवावणो"),
            "रोवणो": ("रुवावणो", "रुळवावणो"),
            "बैठणो": ("बिठावणो", "बिठवावणो"),
            "उठणो": ("उठावणो", "उठवावणो"),
            "देणो": ("दिवावणो", "दिवरावणो"),
            "लेणो": ("लिवावणो", "लिवरावणो"),
            "चालणो": ("चलावणो", "चलवावणो"),
            "बोलणो": ("बुलावणो", "बुलवावणो"),
            "काढणो": ("कढावणो", "कढ़वावणो"),
            "बांचणो": ("बंचावणो", "बंचवावणो"),
        }

        v_clean = verb.strip()
        if not v_clean.endswith("णो") and not v_clean.endswith("नो"):
            v_clean = v_clean + "णो"

        if v_clean in CAUSATIVE_REGISTRY:
            idx = 0 if level == 1 else 1
            return CAUSATIVE_REGISTRY[v_clean][idx]

        root = extract_root(v_clean)
        if level == 1:
            return f"{root}ावणो"
        else:
            return f"{root}वावणो"

    def build_imperative(
        self,
        verb: str,
        politeness_level: str = "polite",
        negative: bool = False,
    ) -> str:
        """
        Generates authentic imperative directive sentences across 4 politeness tiers:
        - 'intimate': तूं + root (e.g., 'तूं लिख', neg: 'तूं मती लिख')
        - 'familiar': तूं + root-ओ (e.g., 'तूं लिखो', neg: 'तूं लिखो मती')
        - 'polite': थे + root-ओ / पधारो (e.g., 'थे लिखो', neg: 'थे लिखो मती')
        - 'honorific': आप + royal verb + सा (e.g., 'आप विराजो सा', 'आप आरोगो सा')
        """
        root = extract_root(verb)
        lvl = politeness_level.lower()

        if lvl == "intimate":
            if negative:
                return f"तूं मती {root}"
            return f"तूं {root}"
        elif lvl == "familiar":
            if negative:
                return f"तूं {root}ो मती"
            return f"तूं {root}ो"
        elif lvl == "honorific":
            royal_map = {
                "खाणो": "आरोगो",
                "खा": "आरोगो",
                "आवणो": "पधारो",
                "आ": "पधारो",
                "जाणो": "पधारो",
                "जा": "पधारो",
                "बैठणो": "विराजो",
                "बैठ": "विराजो",
                "बोलणो": "फरमावो",
                "कहणो": "फरमावो",
                "देखणो": "निहारो",
            }
            form = royal_map.get(verb.strip(), f"{root}ो")
            if negative:
                return f"आप {form} मती सा"
            return f"आप {form} सा"
        else:  # polite default (थे)
            if negative:
                return f"थे {root}ो मती"
            return f"थे {root}ो"

    def convert_clusivity(self, sentence: str, inclusive: bool = True) -> str:
        """
        Transforms 1st person plural statements between Inclusive ('आपां' = speaker + listener)
        and Exclusive ('म्हे' / 'म्हैं' = speaker + associates, excluding listener).
        """
        text = sentence.strip()

        def _replace_word(pattern: str, repl: str, s: str) -> str:
            return re.sub(rf"(?:(?<=^)|(?<=\s))({pattern})(?=\s|$|[।?,.!])", repl, s)

        if inclusive:
            # Replace exclusive or generic Hindi pronouns with inclusive आपां
            text = _replace_word("म्हे|म्हें|हम", "आपां", text)
            text = _replace_word("म्हारो|हमारा", "आपणो", text)
            text = _replace_word("म्हारी|हमारी", "आपणी", text)
            text = _replace_word("म्हारा|हमारे", "आपणा", text)
        else:
            # Replace inclusive with exclusive म्हें
            text = _replace_word("आपां|हम", "म्हे", text)
            text = _replace_word("आपणो|हमारा", "म्हारो", text)
            text = _replace_word("आपणी|हमारी", "म्हारी", text)
            text = _replace_word("आपणा|हमारे", "म्हारा", text)
        return text

    def transform_voice(self, sentence: str, target_voice: str = "passive") -> str:
        """
        Transforms active Rajasthani sentences into synthetic passive or impersonal voice
        (कर्मवाच्य अर भाववाच्य) utilizing -ईजै / -इजै suffixation.
        Examples:
          - 'राम पोथी बांचै है' -> 'राम सूं पोथी बंचीजै है'
          - 'म्हैं काम कियो' -> 'म्हारै सूं काम करीज्यो'
          - 'म्हे नीं चाल सकाँ' -> 'म्हारै सूं चालिजै कोनी'
        """
        s = sentence.strip().rstrip("।").strip()
        if target_voice.lower() == "passive":
            # Simple pronoun agent transformations
            agent_map = {
                "म्हूँ": "म्हारै सूं",
                "म्हैं": "म्हारै सूं",
                "थूँ": "थारै सूं",
                "तैं": "थारै सूं",
                "वो": "उण रै सूं",
                "उण": "उण रै सूं",
                "आपां": "आपां रै सूं",
            }
            for k, v in agent_map.items():
                if s.startswith(k + " "):
                    s = v + s[len(k):]
                    break
            else:
                words = s.split()
                if words and not words[0].endswith("सूं"):
                    words[0] = f"{words[0]} रै हाथूं"
                    s = " ".join(words)

            # Verb stem passivization
            if "बांचै" in s:
                s = s.replace("बांचै है", "बंचीजै है").replace("बांचै", "बंचीजै")
            elif "करै" in s:
                s = s.replace("करै है", "करीजै है").replace("करै", "करीजै")
            elif "लिखै" in s:
                s = s.replace("लिखै है", "लिखीजै है").replace("लिखै", "लिखीजै")
            elif "चाल" in s:
                s = s.replace("चाल सकाँ कोनी", "चालीजै कोनी").replace("चाल सकै कोनी", "चालीजै कोनी")
        return f"{s}।"

    def explain_syntax_rules(self) -> Dict[str, any]:
        """
        Returns structured documentation and grammatical rules of Rajasthani sentence construction,
        syntactic constraints, split ergativity, and dialectal variation.
        """
        return {
            "canonical_word_order": "SOV (Subject - Object - Verb)",
            "modifier_placement": {
                "adjectives": "Precede the noun they qualify and inflect for gender/number (e.g., 'धोळो घोड़ो' vs 'धोळी घोड़ी')",
                "adverbs": "Precede the verb (e.g., 'घणो सोहणो गावै')",
                "postpositions": "Follow the noun or pronoun in oblique case (e.g., 'घोड़े माथे', 'घर मांय')"
            },
            "split_ergativity": {
                "definition": "In past tense with transitive verbs, the subject takes ergative marking while the verb agrees with the direct object in gender and number.",
                "transitive_past_agreement": "Verb agrees with Direct Object: 'राम नै पोथी पढ़ी' (book is feminine -> पढ़ी), 'सीता नै आंबा खायो' (mango is masculine -> खायो).",
                "intransitive_past_agreement": "Verb agrees with Subject in nominative case: 'राम गयो', 'सीता गई'.",
                "ergative_pronoun_shifts": {
                    "म्हूँ (I)": "म्हैं",
                    "थूँ (You)": "तैं",
                    "यो / ओ (This)": "ईं",
                    "वो (That)": "उण",
                    "वे (They)": "उणां",
                    "आपां (We incl.)": "आपां"
                }
            },
            "clusivity": {
                "inclusive_plural": "आपां (includes speaker AND listener: 'we all together')",
                "exclusive_plural": "म्हें (includes speaker BUT EXCLUDES listener: 'we, not you')"
            },
            "dialect_contrast_matrix": {
                "genitive_marker": {
                    "marwari": "रो, री, रा",
                    "mewari": "रो, री, रा",
                    "dhundhari": "को, की, का",
                    "harauti": "को, की, का"
                },
                "present_copula": {
                    "marwari": "है / हैं",
                    "mewari": "है / हैं",
                    "dhundhari": "छै / छैं",
                    "harauti": "छै / छैं"
                },
                "past_copula": {
                    "marwari": "थो, थी, था",
                    "mewari": "हो, ही, हा",
                    "dhundhari": "छो, छी, छा",
                    "harauti": "छो, छी, छा"
                },
                "future_marker": {
                    "marwari": "-सी / -ला (जासी, खावैला)",
                    "mewari": "-वेगा / -ला",
                    "dhundhari": "-गो, -गी, -गा (जावैगो, करैगा)"
                },
                "infinitive_suffix": {
                    "marwari": "-णो / -वणो (करणो, आवणो)",
                    "mewari": "-णो / -वो",
                    "dhundhari": "-बो (करबो, जाबो)"
                }
            },
            "aspects_and_modalities": {
                "inceptive": "Oblique infinitive + लाग- ('टाबर रोवण लाग्यो' - the child began to cry)",
                "obligative": "Infinitive + पड़- / व्है ('मनै जाणो पड़सी' - I will have to go)",
                "medio_passive_inability": "Verb stem + -इजै + कोनी ('म्हारै सूं चालिजै कोनी' - I am unable to walk)"
            },
            "negation_system": {
                "general_negation": "कोनी (Marwari/Mewari) / कोन्या (Dhundhari) (e.g., 'म्हूँ कोनी जावूं')",
                "prohibitive_imperative": "मती (e.g., 'झूठ मती बोलो!')"
            },
            "causative_morphology": {
                "direct_causative": "Root + -ावणो (e.g., करणो -> करावणो, लिखणो -> लिखावणो, खावणो -> जिमावणो)",
                "mediated_causative": "Root + -वावणो (e.g., करणो -> करवावणो, लिखणो -> लिखवावणो, खावणो -> जिमवावणो)"
            },
            "vat_narrative_discourse": {
                "opening_formulas": ["एक समै री बात है", "इण भांत कहीजै", "वात यूं है कि"],
                "transition_particles": ["तद", "पछै", "इत्तै में", "ओ देख'र"],
                "reported_speech": ["इम बोल्या", "यूं कह्यो", "हुकम फरमायो"],
                "closing_formulas": ["कथा पूरी भई, आनंद मंगल भयो", "सगळा सुख सूं रहण लाग्या"]
            },
            "honorific_registers": {
                "intimate": "तूं + root (तूं लिख / मती लिख)",
                "familiar": "तूं + root-ओ (तूं लिखो)",
                "polite": "थे + root-ओ (थे लिखो)",
                "courtly_honorific": "आप + royal verb + सा (आप विराजो सा / आरोगो सा / पधारो सा)"
            }
        }


def generate_causative(verb: str, level: int = 1) -> str:
    """Convenience function: derives Rajasthani causative verb forms."""
    return SyntaxEngine().generate_causative(verb, level=level)


def build_imperative(verb: str, politeness_level: str = "polite", negative: bool = False) -> str:
    """Convenience function: builds directive imperative sentence in Rajasthani."""
    return SyntaxEngine().build_imperative(verb, politeness_level=politeness_level, negative=negative)


def convert_clusivity(sentence: str, inclusive: bool = True) -> str:
    """Convenience function: transforms between inclusive (आपां) and exclusive (म्हे) 1st plural."""
    return SyntaxEngine().convert_clusivity(sentence, inclusive=inclusive)


def transform_voice(sentence: str, target_voice: str = "passive") -> str:
    """Convenience function: converts active Rajasthani sentence into synthetic passive voice."""
    return SyntaxEngine().transform_voice(sentence, target_voice=target_voice)


def hindi_to_rajasthani(sentence: str, dialect: Dialect = Dialect.MARWARI) -> str:
    """Convenience function: converts Hindi sentence into Rajasthani."""
    return SyntaxEngine(dialect=dialect).hindi_to_rajasthani(sentence, dialect=dialect)


def build_compound_verb(
    main_verb: str,
    vector_verb: str = "लेणो",
    tense: Tense = Tense.PAST,
    gender: Gender = Gender.MASCULINE,
    number: GrammaticalNumber = GrammaticalNumber.SINGULAR,
    dialect: Dialect = Dialect.MARWARI,
) -> str:
    """Convenience function: constructs a Rajasthani compound verb."""
    return SyntaxEngine(dialect=dialect).build_compound_verb(
        main_verb, vector_verb, tense=tense, gender=gender, number=number, dialect=dialect
    )


def build_complex_sentence(
    sub_clause: str,
    main_clause: str,
    connector_type: str = "conditional",
) -> str:
    """Convenience function: constructs a Rajasthani correlative complex sentence."""
    return SyntaxEngine().build_complex_sentence(sub_clause, main_clause, connector_type=connector_type)


def explain_syntax_rules() -> Dict[str, any]:
    """Convenience function: returns dictionary of Rajasthani syntax, agreement and conversion rules."""
    return SyntaxEngine().explain_syntax_rules()
