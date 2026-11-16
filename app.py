"""Strona Błękitnej XIV: Flask + Jinja2, zamrażana do statycznego HTML (freeze.py).

Cała treść do aktualizowania (drużyny, kontakty, obozy) jest w data/site.yml.
"""
import re
from pathlib import Path

import yaml
from flask import Flask, render_template

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


@app.route("/")
def start():
    return render_template("start.html", page="start")


@app.route("/druzyny/")
def druzyny():
    return render_template("druzyny.html", page="druzyny")


@app.route("/oboz/")
def oboz():
    return render_template("oboz.html", page="oboz")


if __name__ == "__main__":
    app.run(debug=True)
