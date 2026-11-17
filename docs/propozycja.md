# Nowa strona Błękitnej XIV – propozycja

Dokument roboczy z ustaleniami. Pierwotna wersja powstała przed makietami; poniżej mapa strony jest zaktualizowana do tego, co zostało zbudowane (wersja pokazowa pod blekitna14.org/demo).

## Po co zmieniamy stronę

Obecna strona jest zbudowana na starych technologiach, każda podstrona to osobna kopia tego samego kodu, a zakładka z aktualnościami nie jest prowadzona. Budujemy ją od nowa, prościej.

Strona jest dla: harcerzy, rodziców, byłych harcerzy, rodziców dzieci, które chcą dołączyć, i wszystkich, którzy chcą się dowiedzieć, kim jesteśmy.

## Zasady

- **Na bieżąco – w mediach społecznościowych.** Facebook i Instagram pokazują, co dzieje się teraz. Strona nie ma aktualności; to stała „wizytówka”, którą aktualizujemy raz na ok. 3 miesiące.
- **Mało tekstu, dużo zdjęć.** Bez rozdziałów o misji i metodzie harcerskiej – nikogo nie przekonają.
- **Kontakt łatwy do znalezienia.** Rodzic szukający numeru do drużynowego swojego dziecka ma go znaleźć w kilka sekund.
- **Miejsce na Błękitny Grom.** Projekt ma pasować do dużego wydarzenia, ale samego Gromu jeszcze nie projektujemy.

## Mapa strony

| Podstrona | Co zawiera |
|---|---|
| **Start** (logo w menu) | Zdjęcie na cały ekran, „Kim jesteśmy?”, drużyny na ścieżce wieku (zdjęcia i telefony), „Jak zacząć?”, Obóz i zimowisko, ostatnie wpisy z Facebooka, galeria (2 najnowsze i 2 losowe albumy z Flickra), kontakt do szczepowego. |
| **Drużyny** | Osobny, duży fragment dla każdej drużyny i kręgu Kłuszyn: zdjęcie, logo, opis, zbiórki, **imię, telefon i e-mail drużynowego/drużynowej**, linki do mediów społecznościowych. Szybkie przechodzenie między drużynami u góry. |
| **Obóz** | Obóz letni i zimowisko: termin, miejsce, cena, komendant, informacje dla rodziców, zapisy. Poniżej albumy z Flickra (obozy, zimowiska, Żółkiewszczada, rajdy wiosenne). |
| **Archiwum** | Własna podstrona: wstęp, prośba o stare zdjęcia i zbiory (zdjęcia, Błękitny czas, jednodniówki, książki i śpiewniki) z linkami ze starego archiwum. |
| **Kontakt** | Najczęstsze pytania (FAQ), a pod nimi kontakt do szczepowego i adres. |
| **Przekaż 1,5%** | Numer KRS, kwota i cel szczegółowy krok po kroku. |
| **Błękitny Grom** *(później)* | Zarezerwowane miejsce, osobny wygląd w tej samej konstrukcji strony. |

Menu: **Drużyny · Obóz · Archiwum · Kontakt · Przekaż 1,5%**, plus ikony Facebooka, Instagrama i Flickra. Logo prowadzi na Start. Na dole każdej strony: Zobacz drużyny, FAQ, Przekaż 1,5%.

**Rezygnujemy z:** Aktualności, osobnych podstron Historia / 100-lecie, strony „10 powodów”.

**Kontakt:** szczepowy na Start i w Kontakcie, drużynowi na stronie Drużyny. Numery telefonów są jawne.

## Technologia (po ludzku)

- Strona napisana w Pythonie (Flask), zamieniana na zwykłe pliki, które hostujemy za darmo na GitHub Pages, pod tym samym adresem blekitna14.org. Nie potrzeba serwera ani opłat.
- Dane do aktualizacji (drużyny, drużynowi, telefony, terminy obozów, FAQ, linki archiwum) siedzą w jednym pliku.
- Albumy ze zdjęciami pobieramy z Flickra (publiczne dane, klucz API tylko lokalnie, nie na stronie). Zmiana numeru telefonu to edycja jednej linijki, a nie przepisywanie strony.
- Aktualizuje ktoś, kto programuje – rzadko, więc nie potrzebujemy panelu administracyjnego.
- Usuwamy z kodu klucze i hasła, które dziś leżą w repozytorium.

## Wygląd

Wybrany kierunek „D”: jasne tło, granat i błękit z logo, zaokrąglone kształty, drużyny jako zaokrąglone sześciokąty na ścieżce wieku. Zarchiwizowane makiety A–E są w `docs/makiety/`.

## Kolejne kroki

1. Uzupełnienie treści przez szczep (współdzielony dokument z tabelami).
2. Przegląd wersji pokazowej, poprawki.
3. Publikacja pod blekitna14.org po akceptacji; stara strona i archiwum zostają dostępne pod swoimi adresami.

## Czego potrzebujemy od szczepu

- Dni, godziny i miejsca zbiórek drużyn.
- Dane kontaktowe szczepowego i drużynowych (imię, telefon, e-mail).
- Terminy, miejsca i ceny obozu i zimowiska, link do zapisów.
- Zdjęcie na główną i zdjęcia do obozu.
- Czy numery telefonów mogą być jawne (zakładamy, że tak).
