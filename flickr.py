"""Albumy z Flickra dla strony Obóz i galerii na stronie głównej.

python flickr.py   pobiera listę albumów i zapisuje ją w data/flickr.json

Wymaga własnego klucza API Flickra (darmowy, https://www.flickr.com/services/apps/create/)
w zmiennej środowiskowej FLICKR_API_KEY. Zapisany plik jest częścią repozytorium,
więc zwykły build (python freeze.py) nie potrzebuje ani klucza, ani internetu.
"""
import json
import os
import random
import re
import sys
from concurrent.futures import ThreadPoolExecutor
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


SAMPLE = 10  # tyle losowych zdjęć z albumu zapisujemy (do losowania okładki)
VERSION = 2  # zmiana wymusza ponowne pobranie zdjęć (v2: większe rozmiary)
EXTRAS = "url_q,url_z,url_c"  # kwadrat 150 px, 640 px, 800 px (dłuższy bok)


def _best(photo):
    """Największy dostępny rozmiar (do 800 px); url_q (150 px) to ostateczność."""
    return photo.get("url_c") or photo.get("url_z") or photo.get("url_q") or ""


def _sample_photos(key, user_id, album_id):
    data = _call(key, "flickr.photosets.getPhotos", photoset_id=album_id, user_id=user_id,
                 per_page=500, extras=EXTRAS, media="photos")
    urls = [u for u in (_best(p) for p in data["photoset"]["photo"]) if u]
    return random.sample(urls, min(SAMPLE, len(urls)))


def refresh(key):
    with open(ROOT / "data" / "site.yml", encoding="utf-8") as f:
        site = yaml.safe_load(f)
    profile_url = site["flickr"]["uzytkownik_url"]
    user = _call(key, "flickr.urls.lookupUser", url=profile_url)["user"]
    sets = _call(key, "flickr.photosets.getList", user_id=user["id"],
                 per_page=500, primary_photo_extras=EXTRAS)["photosets"]["photoset"]
    old = {a["id"]: a for a in load()}
    albums = []
    for s in sets:
        primary = s.get("primary_photo_extras") or {}
        albums.append({
            "id": s["id"],
            "tytul": s["title"]["_content"],
            "url": f"{profile_url.rstrip('/')}/albums/{s['id']}",
            "okladka": _best(primary),
            "v": VERSION,
            "zdjec": int(s.get("photos", 0)),
            "data": int(s.get("date_create", 0)),
        })
    albums.sort(key=lambda a: a["data"], reverse=True)

    # Losowe zdjęcia pobieramy tylko dla albumów, które mogą trafić na stronę:
    # z grup w sekcji zdjęć oraz kilku najnowszych. Reszta zostaje z okładką.
    needed = {a["id"] for g in site["zdjecia"] for a in filter_albums(albums, g.get("slowa"), g.get("wyklucz"))}
    needed |= {a["id"] for a in sorted(albums, key=lambda a: (_year(a), a["data"]), reverse=True)[:10]}
    todo = []
    for a in albums:
        prev = old.get(a["id"])
        if prev and prev.get("v") == VERSION and prev.get("zdjecia") and prev.get("zdjec") == a["zdjec"]:
            a["zdjecia"] = prev["zdjecia"]
        elif a["id"] in needed:
            todo.append(a)
    print(f"Albumów: {len(albums)}, do pobrania zdjęć: {len(todo)}")

    def fetch(a):
        a["zdjecia"] = _sample_photos(key, user["id"], a["id"])

    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(fetch, todo))

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
    found = [dict(a, rok=_year(a) or "", nazwa=re.sub(r"^\s*\d{4}(\s*[-–/]\s*|\s+)", "", a["tytul"]).strip()) for a in found]
    return sorted(found, key=lambda a: (a["rok"] or 0, a["data"]), reverse=True)


if __name__ == "__main__":
    key = os.environ.get("FLICKR_API_KEY")
    if not key:
        sys.exit("Ustaw zmienną FLICKR_API_KEY (klucz API z flickr.com/services/apps/create).")
    result = refresh(key)
    print(f"Zapisano {len(result)} albumów do {CACHE}")
