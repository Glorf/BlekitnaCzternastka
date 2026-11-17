# Strona BŁ XIV

Nowa strona (Flask + Frozen-Flask, gałąź `redesign`) i stara strona (statyczny HTML w katalogu głównym, serwowana z `master`) żyją w tym repozytorium obok siebie, dopóki nie przełączymy domeny.

## Nowa strona

```
pip install -r requirements.txt
python app.py                  # podgląd na http://127.0.0.1:5000
python freeze.py               # pełna statyczna strona do build/
python freeze.py --demo        # wersja pokazowa (prefiks /demo/, noindex) do build-demo/
python assemble_site.py        # po freeze --demo: składa _site/ (stara strona + demo/)
python deploy_demo.py          # ręczna publikacja demo bez GitHub Actions (--push wysyła)
python -m unittest discover tests
```

- **Treści:** `data/site.yml` (drużyny, drużynowi, kontakty, FAQ, archiwum, obozy, 1,5%). Szablony w `templates/`, style, skrypty i zdjęcia w `static/`.
- **Albumy z Flickra** (strona Obóz i galeria na głównej): `FLICKR_API_KEY=... python flickr.py` zapisuje `data/flickr.json`. Klucz jest tylko na Twoim komputerze, w pliku lądują wyłącznie publiczne dane o albumach.
- **Teksty do uzupełniania przez szczep:** współdzielony dokument (zob. wątek w historii zmian); po uzupełnieniu przepisujemy je do `data/site.yml`.
- Dane oznaczone w `site.yml` jako „do uzupełnienia” (terminy i ceny obozów, imię szczepowego, godziny zbiórek, FAQ) są przykładami.
- Zarchiwizowane makiety A–E: `docs/makiety/`. Ustalenia z szczepowym: `docs/propozycja.md`.

## Automatyczna publikacja

Workflow `.github/workflows/pages.yml` publikuje stronę na GitHub Pages: przy każdym pushu do `master`, co poniedziałek rano i na żądanie (Actions → Publikacja strony → Run workflow). Buduje demo, uruchamia testy i wysyła stronę: starą w katalogu głównym i nową pod `/demo/`.

Jednorazowa konfiguracja w repozytorium na GitHubie:

1. **Settings → Pages → Build and deployment → Source: GitHub Actions** (zamiast „Deploy from a branch”). Domena `blekitna14.org` zostaje w ustawieniach.
2. Opcjonalnie, żeby albumy z Flickra odświeżały się same: **Settings → Secrets and variables → Actions → New repository secret** o nazwie `FLICKR_API_KEY`. Bez niego używany jest `data/flickr.json` z repozytorium.

Po zatwierdzeniu nowej strony zamiast `--demo` budujemy `python freeze.py` i wysyłamy jej `build/` w katalogu głównym.

## Konwencje (stara strona)

- [wszystkie pliki (łącznie z tymi z .gitignore)](https://www.dropbox.com/sh/o7kwo1bq0cc7mqs/AACFT5Hs7CRNJkGPTB9off_Sa?dl=0)
- używamy-kebab-case
- tła definiujemy w css/custom.css i wrzucamy do css/img
- jak zmieniasz stronę główną, to pamiętaj, żeby zmienić menu ;)
- komentujemy główne divy i cmmity :)
