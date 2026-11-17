"""Buduje statyczną stronę.

python freeze.py          pełna strona do build/ (docelowo pod blekitna14.org/)
python freeze.py --demo   wersja pokazowa do build-demo/ (pod blekitna14.org/demo/,
                          z blokadą indeksowania; bez starych podstron i CNAME)
"""
import shutil
import sys
from pathlib import Path

from flask_frozen import Freezer

from app import app

ROOT = Path(__file__).parent
DEMO = "--demo" in sys.argv

# Stare podstrony, które muszą nadal działać pod swoimi adresami (tylko pełna strona).
KEEP = ["grom"]  # archiwum/ to teraz podstrona z app.py (ten sam adres)
EXTRA = ["CNAME", ".nojekyll", "favicon.ico"]

if DEMO:
    out = ROOT / "build-demo"
    app.config["FREEZER_BASE_URL"] = "https://blekitna14.org/demo/"
    app.config["NOINDEX"] = True
else:
    out = ROOT / "build"

app.config["FREEZER_DESTINATION"] = str(out)
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True

if __name__ == "__main__":
    Freezer(app).freeze()
    if not DEMO:
        for name in KEEP:
            if (ROOT / name).exists():
                shutil.copytree(ROOT / name, out / name, dirs_exist_ok=True)
        for name in EXTRA:
            if (ROOT / name).exists():
                shutil.copy(ROOT / name, out / name)
    print(f"Gotowe: {out.name}/")
