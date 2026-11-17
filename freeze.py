"""Buduje statyczną stronę do katalogu build/ (python freeze.py)."""
import shutil
from pathlib import Path

from flask_frozen import Freezer

from app import app

ROOT = Path(__file__).parent
app.config["FREEZER_DESTINATION"] = str(ROOT / "build")
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True

# Stare podstrony, które muszą nadal działać pod swoimi adresami.
KEEP = ["grom"]  # archiwum/ to teraz podstrona z app.py (ten sam adres)
EXTRA = ["CNAME", ".nojekyll", "favicon.ico"]

if __name__ == "__main__":
    Freezer(app).freeze()
    build = ROOT / "build"
    for name in KEEP:
        if (ROOT / name).exists():
            shutil.copytree(ROOT / name, build / name, dirs_exist_ok=True)
    for name in EXTRA:
        if (ROOT / name).exists():
            shutil.copy(ROOT / name, build / name)
    print("Gotowe: build/")
