# Strona BŁ XIV

Nowa strona (Flask + Frozen-Flask, gałąź `redesign`) i stara strona (statyczny HTML w katalogu głównym, serwowana z `master`) żyją w tym repozytorium obok siebie, dopóki nie przełączymy domeny.

## Nowa strona

```
pip install -r requirements.txt
python app.py                  # podgląd na http://127.0.0.1:5000
python freeze.py               # pełna statyczna strona do build/
python freeze.py --demo        # wersja pokazowa (prefiks /demo/, noindex) do build-demo/
python deploy_demo.py          # przygotowuje commit z demo/ na master (--push wysyła)
python -m unittest discover tests
```

- **Treści:** `data/site.yml` (drużyny, drużynowi, kontakty, FAQ, archiwum, obozy, 1,5%). Szablony w `templates/`, style, skrypty i zdjęcia w `static/`.
- **Albumy z Flickra** (strona Obóz i galeria na głównej): `FLICKR_API_KEY=... python flickr.py` zapisuje `data/flickr.json`. Klucz jest tylko na Twoim komputerze, w pliku lądują wyłącznie publiczne dane o albumach.
- **Teksty do uzupełniania przez szczep:** współdzielony dokument (zob. wątek w historii zmian); po uzupełnieniu przepisujemy je do `data/site.yml`.
- Dane oznaczone w `site.yml` jako „do uzupełnienia” (terminy i ceny obozów, imię szczepowego, godziny zbiórek, FAQ) są przykładami.
- Zarchiwizowane makiety A–E: `docs/makiety/`. Ustalenia z szczepowym: `docs/propozycja.md`.

## Konwencje (stara strona)

- [wszystkie pliki (łącznie z tymi z .gitignore)](https://www.dropbox.com/sh/o7kwo1bq0cc7mqs/AACFT5Hs7CRNJkGPTB9off_Sa?dl=0)
- używamy-kebab-case
- tła definiujemy w css/custom.css i wrzucamy do css/img
- jak zmieniasz stronę główną, to pamiętaj, żeby zmienić menu ;)
- komentujemy główne divy i cmmity :)
