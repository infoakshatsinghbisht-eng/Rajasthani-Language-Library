# -*- coding: utf-8 -*-
"""
Rajasthani Language Library - Web Application Server
===================================================
Lightweight, zero-dependency built-in HTTP server providing an interactive
web UI and REST API for translation, verb conjugation, dictionary lookups,
number conversion, and cultural discovery.
"""

import os
import json
import urllib.parse
from http.server import SimpleHTTPRequestHandler, HTTPServer
import rajasthani

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")


class RajasthaniRequestHandler(SimpleHTTPRequestHandler):
    """
    HTTP handler serving static UI and REST endpoints for Rajasthani.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # REST API endpoints
        if path == "/api/translate":
            text = query.get("text", [""])[0]
            dialect = query.get("dialect", ["mwr"])[0]
            result = rajasthani.translate(text, dialect=dialect)
            self._send_json({
                "source_text": text,
                "rajasthani": result.text,
                "romanized": result.romanized,
                "dialect": result.dialect,
                "method": result.method,
            })
            return

        elif path == "/api/conjugate":
            verb = query.get("verb", ["खाणो"])[0]
            tense_str = query.get("tense", ["present"])[0]
            person_str = query.get("person", ["third"])[0]
            gender_str = query.get("gender", ["masculine"])[0]
            num_str = query.get("number", ["singular"])[0]
            dialect = query.get("dialect", ["mwr"])[0]

            tense = getattr(rajasthani.Tense, tense_str.upper(), rajasthani.Tense.PRESENT)
            person = getattr(rajasthani.Person, person_str.upper(), rajasthani.Person.THIRD)
            gender = getattr(rajasthani.Gender, gender_str.upper(), rajasthani.Gender.MASCULINE)
            number = getattr(rajasthani.GrammaticalNumber, num_str.upper(), rajasthani.GrammaticalNumber.SINGULAR)

            conjugated = rajasthani.conjugate(
                verb, tense=tense, person=person, gender=gender, number=number, dialect=dialect
            )
            self._send_json({"verb": verb, "conjugated": conjugated, "tense": tense_str})
            return

        elif path == "/api/dictionary":
            q = query.get("q", [""])[0]
            results = rajasthani.search(q, limit=15)
            data = [
                {
                    "rajasthani": w.rajasthani,
                    "roman": w.roman,
                    "english": w.english,
                    "hindi": w.hindi,
                    "pos": w.pos,
                    "category": w.category,
                    "example": w.example,
                }
                for w in results
            ]
            self._send_json({"results": data, "count": len(data)})
            return

        elif path == "/api/numbers":
            val_str = query.get("val", ["1"])[0]
            try:
                val = int(val_str)
                words = rajasthani.num_to_words(val)
                dev_digits = rajasthani.to_devanagari_numerals(val)
                ord_m = rajasthani.ordinal(val, "m")
                self._send_json({
                    "number": val,
                    "words": words,
                    "devanagari_numerals": dev_digits,
                    "ordinal": ord_m,
                })
            except ValueError:
                self._send_json({"error": "Invalid integer"})
            return

        elif path == "/api/rituals":
            cat = query.get("category", [""])[0]
            if cat:
                rituals = rajasthani.get_rituals_by_category(cat)
            else:
                rituals = rajasthani.get_all_rituals()
            data = [
                {
                    "name": r.name,
                    "roman": r.roman,
                    "category": r.category,
                    "description": r.description,
                    "customs_and_practices": r.customs_and_practices,
                    "cultural_significance": r.cultural_significance
                }
                for r in rituals
            ]
            self._send_json({"rituals": data, "count": len(data)})
            return

        elif path == "/api/ornaments":
            part = query.get("part", [""])[0]
            if part:
                ornaments = rajasthani.get_ornaments_by_body_part(part)
            else:
                ornaments = rajasthani.get_all_ornaments()
            data = [
                {
                    "name": o.name,
                    "roman": o.roman,
                    "body_part": o.body_part,
                    "metal": o.metal,
                    "description": o.description,
                    "cultural_context": o.cultural_context
                }
                for o in ornaments
            ]
            self._send_json({"ornaments": data, "count": len(data)})
            return

        elif path == "/api/syntax":
            rules = rajasthani.explain_syntax_rules()
            self._send_json(rules)
            return

        elif path == "/api/corpus":
            catalog_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data_sources", "corpus_catalog.json")
            if os.path.exists(catalog_path):
                with open(catalog_path, "r", encoding="utf-8") as f:
                    cat_data = json.load(f)
            else:
                cat_data = []
            self._send_json({"books": cat_data, "total_books": len(cat_data)})
            return

        # Default static file serving
        return super().do_GET()

    def _send_json(self, data: dict, status: int = 200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


def run_server(port: int = 8000, host: str = "127.0.0.1"):
    """Starts the built-in web server."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, RajasthaniRequestHandler)
    print(f"🐫 Rajasthani Language Library Server running at http://{host}:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
