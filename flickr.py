"""Albumy z Flickra dla strony Obóz.

python flickr.py   pobiera listę albumów i zapisuje ją w data/flickr.json

Wymaga własnego klucza API Flickra (darmowy, https://www.flickr.com/services/apps/create/)
w zmiennej środowiskowej FLICKR_API_KEY. Zapisany plik jest częścią repozytorium,
więc zwykły build (python freeze.py) nie potrzebuje ani klucza, ani internetu.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CACHE = ROOT / "data" / "flickr.json"
API = "https://api.flickr.com/services/rest/"


def _call(key, method, **params):
    params.update(method=method, api_key=key, format="json", nojsoncallback=1)
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        data = json.load(r)
    if data.get("stat") != "ok":
        raise RuntimeError(f"Flickr {method}: {data.get('message')}")
    return data


def refresh(key):
    with open(ROOT / "data" / "site.yml", encoding="utf-8") as f:
        profile_url = yaml.safe_load(f)["flickr"]["uzytkownik_url"]
    user = _call(key, "flickr.urls.lookupUser", url=profile_url)["user"]
    sets = _call(key, "flickr.photosets.getList", user_id=user["id"],
                 per_page=500, primary_photo_extras="url_q")["photosets"]["photoset"]
    albums = []
    for s in sets:
        primary = s.get("primary_photo_extras") or {}
        albums.append({
            "id": s["id"],
            "tytul": s["title"]["_content"],
            "url": f"{profile_url.rstrip('/')}/albums/{s['id']}",
            "okladka": primary.get("url_q", ""),
            "zdjec": int(s.get("photos", 0)),
            "data": int(s.get("date_create", 0)),
        })
    albums.sort(key=lambda a: a["data"], reverse=True)
    CACHE.write_text(json.dumps(albums, ensure_ascii=False, indent=1), encoding="utf-8")
    return albums


def load():
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8-sig"))
    return []


def _year(album):
    m = re.match(r"\s*(\d{4})", album["tytul"])
    return int(m.group(1)) if m else 0


def filter_albums(albums, words, exclude=None):
    """Albumy z którymś ze słów w tytule (bez względu na wielkość liter),
    bez tych ze słowami wykluczonymi. Najnowsze (wg roku w tytule) pierwsze."""
    words = [w.lower() for w in words or []]
    exclude = [w.lower() for w in exclude or []]
    found = [a for a in albums
             if any(w in a["tytul"].lower() for w in words)
             and not any(w in a["tytul"].lower() for w in exclude)]
    return sorted(found, key=lambda a: (_year(a), a["data"]), reverse=True)


if __name__ == "__main__":
    key = os.environ.get("FLICKR_API_KEY")
    if not key:
        sys.exit("Ustaw zmienną FLICKR_API_KEY (klucz API z flickr.com/services/apps/create).")
    result = refresh(key)
    print(f"Zapisano {len(result)} albumów do {CACHE}")
