"""Strona Błękitnej XIV: Flask + Jinja2, zamrażana do statycznego HTML (freeze.py).

Cała treść do aktualizowania (drużyny, kontakty, obozy) jest w data/site.yml.
"""
import random
import re
from pathlib import Path

import yaml
from flask import Flask, render_template

import flickr

ROOT = Path(__file__).parent

app = Flask(__name__)


def load_site():
    with open(ROOT / "data" / "site.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)


@app.template_filter("tel")
def tel_filter(phone):
    """'600 100 200' -> 'tel:600100200'"""
    return "tel:" + re.sub(r"[^\d+]", "", phone)


@app.context_processor
def inject_site():
    return {"site": load_site()}


def gallery_albums(site, newest=2, rand=2):
    """Albumy do galerii na stronie głównej: najnowsze plus losowe.

    Okładka to losowe zdjęcie z albumu (jeśli data/flickr.json je zawiera).
    Losowanie odbywa się przy każdym budowaniu strony."""
    albums = flickr.load()
    if not albums:
        return []
    for a in albums:
        a["rok"] = flickr._year(a) or ""
        a["nazwa"] = re.sub(r"^\s*\d{4}(\s*[-–/]\s*|\s+)", "", a["tytul"]).strip()
    dated = [a for a in albums if a["rok"]]
    latest = sorted(dated, key=lambda a: (a["rok"], a["data"]), reverse=True)[:newest]
    taken = {a["id"] for a in latest}
    pool = {}
    for g in site["zdjecia"]:
        for a in flickr.filter_albums(albums, g.get("slowa"), g.get("wyklucz")):
            if a["id"] not in taken:
                pool[a["id"]] = a
    picked = random.sample(list(pool.values()), min(rand, len(pool)))
    chosen = [dict(a) for a in latest + picked]
    for a in chosen:
        a["twarz"] = random.choice(a["zdjecia"]) if a.get("zdjecia") else a["okladka"]
    return chosen


@app.route("/")
def start():
    return render_template("start.html", page="start", galeria=gallery_albums(load_site()))


@app.route("/druzyny/")
def druzyny():
    return render_template("druzyny.html", page="druzyny")


@app.route("/oboz/")
def oboz():
    albums = flickr.load()
    site = load_site()
    for g in site["zdjecia"]:
        g["albumy"] = flickr.filter_albums(albums, g.get("slowa"), g.get("wyklucz"))
    return render_template("oboz.html", page="oboz", site=site)


@app.route("/kontakt/")
def kontakt():
    return render_template("kontakt.html", page="kontakt")


@app.route("/archiwum/")
def archiwum():
    return render_template("archiwum.html", page="archiwum")


@app.route("/procent/")
def procent():
    return render_template("procent.html", page="procent")


if __name__ == "__main__":
    app.run(debug=True)
