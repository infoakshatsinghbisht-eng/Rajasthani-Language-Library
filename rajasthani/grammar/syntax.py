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
            }
        }


def hindi_to_rajasthani(sentence: str, dialect: Dialect = Dialect.MARWARI) -> str:
    """Convenience function: converts Hindi sentence into Rajasthani."""
    return SyntaxEngine(dialect=dialect).hindi_to_rajasthani(sentence, dialect=dialect)


def explain_syntax_rules() -> Dict[str, any]:
    """Convenience function: returns dictionary of Rajasthani syntax, agreement and conversion rules."""
    return SyntaxEngine().explain_syntax_rules()
