#!/usr/bin/env python3
"""Kompiliert ZsRAG für die Veröffentlichung.

Bei jedem Lauf:
  1. Version hochzählen (version.txt): Version 1.0 -> 1.01 -> 1.02 ... (nach 1.99 folgt 2.0)
  2. Version und Datum des Kompilierens in index.html eintragen
  3. Artifact-Datei erzeugen (index.html ohne eigenes Dokumentgerüst)

Aufruf:  python3 build.py [Zieldatei]     (Standard: dist/zsrag.html)
         python3 build.py --no-bump ...   (Version nicht erhöhen, nur Datum setzen)
"""
import datetime, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
VERSION_FILE = os.path.join(ROOT, "version.txt")
INDEX = os.path.join(ROOT, "index.html")


def next_version(v):
    major, minor = v.split(".")
    n = int(minor) + 1
    if n > 99:
        return "%d.0" % (int(major) + 1)
    return "%s.%02d" % (major, n)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    bump = "--no-bump" not in sys.argv
    out = args[0] if args else os.path.join(ROOT, "dist", "zsrag.html")

    if os.path.exists(VERSION_FILE):
        version = open(VERSION_FILE).read().strip()
        if bump:
            version = next_version(version)
    else:
        version = "1.0"   # erste Version
    open(VERSION_FILE, "w").write(version + "\n")

    today = datetime.date.today().strftime("%d.%m.%Y")
    html = open(INDEX, encoding="utf-8").read()
    html = re.sub(r'(<span class="ver" id="appVersion">)[^<]*(</span>)', r"\g<1>Version " + version + r"\g<2>", html)
    html = re.sub(r'(<span id="buildDate">)[^<]*(</span>)', r"\g<1>" + today + r"\g<2>", html)
    open(INDEX, "w", encoding="utf-8").write(html)

    # Artifact-Fassung: Doctype, html/head/body-Tags sowie charset/viewport entfernen
    drop = re.compile(r'^(<!doctype|<html|</html>|<head>|</head>|<body>|</body>)|meta charset|name="viewport"', re.I)
    lines = [l for l in html.splitlines(True) if not drop.search(l)]
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w", encoding="utf-8").write("".join(lines))
    print("ZsRAG Version %s · %s -> %s" % (version, today, out))


if __name__ == "__main__":
    main()
