# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Command-Line Interface (CLI)
=========================================================
CLI tool for translation, morphological conjugation, dictionary lookup,
number conversion, kinship resolution, and local web app server.
"""

import sys
import argparse
import rajasthani


def main():
    parser = argparse.ArgumentParser(
        prog="rajasthani",
        description="Rajasthani (राजस्थानी) Language Standard Library CLI",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 1. Translate
    trans_p = subparsers.add_parser("translate", help="Translate text into Rajasthani")
    trans_p.add_argument("text", help="Source text to translate")
    trans_p.add_argument("--source", "-s", default="auto", help="Source language (en, hi, etc.)")
    trans_p.add_argument("--dialect", "-d", default="mwr", help="Target dialect (mwr, mew, dhd, hoj, swv)")

    # 2. Conjugate
    conj_p = subparsers.add_parser("conjugate", help="Conjugate a Rajasthani verb")
    conj_p.add_argument("verb", help="Verb infinitive (e.g. खाणो, जाणो, करणो)")
    conj_p.add_argument("--tense", "-t", default="present", help="Tense (present, past, future, continuous, presumptive, imperative)")
    conj_p.add_argument("--person", "-p", default="third", choices=["first", "second", "third"])
    conj_p.add_argument("--gender", "-g", default="masculine", choices=["masculine", "feminine"])
    conj_p.add_argument("--number", "-n", default="singular", choices=["singular", "plural"])
    conj_p.add_argument("--dialect", "-d", default="mwr")

    # 3. Numbers
    num_p = subparsers.add_parser("num", help="Convert numbers to Rajasthani words")
    num_p.add_argument("value", type=int, help="Integer to convert (e.g. 42)")

    # 4. Dictionary Lookup
    dict_p = subparsers.add_parser("dict", help="Search the Rajasthani dictionary")
    dict_p.add_argument("query", help="Word to search")

    # 5. Kinship
    kin_p = subparsers.add_parser("kinship", help="Resolve Rajasthani kinship relationships")
    kin_p.add_argument("relation", help="Kinship relation (e.g. uncle, mama, father, byai)")

    # 6. Culture
    cul_p = subparsers.add_parser("culture", help="Explore Rajasthani cultural heritage")
    cul_p.add_argument("category", choices=["architecture", "attire", "music", "cuisine", "deities", "places", "literature"])

    # 7. Proverb
    subparsers.add_parser("proverb", help="Display a traditional Rajasthani proverb (कहावत)")

    # 8. Riddle
    subparsers.add_parser("riddle", help="Display a traditional Rajasthani riddle (पहेली)")

    # 9. Web Server
    web_p = subparsers.add_parser("web", help="Launch interactive web server")
    web_p.add_argument("--port", "-p", type=int, default=8000, help="Port to run on")
    web_p.add_argument("--host", default="127.0.0.1", help="Host interface")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Dispatch commands
    if args.command == "translate":
        res = rajasthani.translate(args.text, source_lang=args.source, dialect=args.dialect)
        print(f"\n🐫 राजस्थानी : {res.text}")
        print(f"🔤 Romanized : {res.romanized}")
        print(f"📌 Method    : {res.method} (Dialect: {res.dialect})\n")

    elif args.command == "conjugate":
        tense = getattr(rajasthani.Tense, args.tense.upper(), rajasthani.Tense.PRESENT)
        person = getattr(rajasthani.Person, args.person.upper(), rajasthani.Person.THIRD)
        gender = getattr(rajasthani.Gender, args.gender.upper(), rajasthani.Gender.MASCULINE)
        number = getattr(rajasthani.GrammaticalNumber, args.number.upper(), rajasthani.GrammaticalNumber.SINGULAR)
        res = rajasthani.conjugate(
            args.verb, tense=tense, person=person, gender=gender, number=number, dialect=args.dialect
        )
        print(f"\n⚙️  Conjugated Form: {res}\n")

    elif args.command == "num":
        words = rajasthani.num_to_words(args.value)
        digits = rajasthani.to_devanagari_numerals(args.value)
        ord_m = rajasthani.ordinal(args.value, "m")
        print(f"\n🔢 Number   : {args.value}")
        print(f"📖 Words    : {words}")
        print(f"🪔 Digits   : {digits}")
        print(f"🏅 Ordinal  : {ord_m}\n")

    elif args.command == "dict":
        w = rajasthani.lookup(args.query)
        if w:
            print(f"\n📖 शब्द      : {w.rajasthani} ({w.roman}) [{w.pos}]")
            print(f"🇮🇳 हिन्दी     : {w.hindi}")
            print(f"🇬🇧 English   : {w.english}")
            if w.example:
                print(f"💬 उदाहरण   : {w.example}")
            print()
        else:
            matches = rajasthani.search(args.query, limit=5)
            if matches:
                print(f"\nFound {len(matches)} matches:")
                for m in matches:
                    print(f"• {m.rajasthani} ({m.roman}): {m.hindi} / {m.english}")
                print()
            else:
                print("\n❌ कोई शब्द कोनी मिल्यो (No words found).\n")

    elif args.command == "kinship":
        term = rajasthani.resolve_kinship(args.relation)
        if term:
            print(f"\n👥 नाता-गोता : {term.rajasthani} ({term.roman})")
            print(f"👑 आदरसूचक   : {term.honorific}")
            print(f"🇮🇳 सम्बन्ध   : {term.hindi}")
            print(f"🇬🇧 English   : {term.english}")
            print(f"💡 परंपरा    : {term.cultural_notes}\n")
        else:
            print("\n❌ Kinship term not resolved.\n")

    elif args.command == "culture":
        if args.category == "architecture":
            for el in rajasthani.get_architecture_elements():
                print(f"🏰 {el.name}: {el.description}")
        elif args.category == "cuisine":
            for d in rajasthani.get_cuisine_dishes():
                print(f"🍛 {d.name}: {d.description}")
        elif args.category == "music":
            for ins in rajasthani.get_instruments():
                print(f"🎶 {ins.name}: {ins.description}")
        elif args.category == "deities":
            for deity in rajasthani.get_folk_deities():
                print(f"🙏 {deity.name}: {deity.legend}")
        elif args.category == "places":
            for pl in rajasthani.get_heritage_places():
                print(f"📍 {pl.name}: {pl.description}")
        elif args.category == "literature":
            for lit in rajasthani.get_literary_figures():
                print(f"📜 {lit.name} ({lit.period}): {lit.significance}")

    elif args.command == "proverb":
        p = rajasthani.get_default_dictionary().random_proverb()
        if p:
            print(f"\n📜 कहावत     : {p['rajasthani']}")
            print(f"🔤 उच्चारण   : {p['roman']}")
            print(f"🇮🇳 अर्थ      : {p['hindi']}")
            print(f"🇬🇧 Meaning   : {p['english']}")
            print(f"💡 संदर्भ     : {p['cultural_context']}\n")

    elif args.command == "riddle":
        r = rajasthani.get_default_dictionary().random_riddle()
        if r:
            print(f"\n❓ पहेली (आडी) : {r['riddle']}")
            print(f"💡 संकेत       : {r['hindi_hint']}")
            print(f"✅ उत्तर       : {r['answer']} ({r['answer_english']})\n")

    elif args.command == "web":
        rajasthani.run_server(port=args.port, host=args.host)


if __name__ == "__main__":
    main()
