# Nowa strona Błękitnej XIV – propozycja

Dokument roboczy do omówienia z szczepowym/hufcowym. Nic jeszcze nie jest zbudowane – to ustalenia, które chcemy zatwierdzić przed pracą nad makietami.

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
| **Start** | Zdjęcie, 2–3 zdania o nas, przyciski do Drużyn i Obozu, **kontakt do szczepowego** (imię, telefon, e-mail, adres: ul. Bukowska 16, Poznań), linki do Facebooka, Instagrama i Flickra, 1% podatku. |
| **Drużyny** (dawniej „Dołącz do nas”) | Na górze krótko o szczepie i jego historii (kilka zdań), potem karta każdej drużyny osobno: wiek, kiedy i gdzie zbiórki, krótki opis, **imię, telefon i e-mail drużynowego**. Szybkie przechodzenie między drużynami; na dole miejsce na linki do dłuższych opracowań o szczepie i historii (dodamy później, jeśli szczepowy zechce). |
| **Obóz** | Obóz letni i zimowisko: terminy, miejsce, cena, informacje dla rodziców, zdjęcia, zapisy. Tylko te dwa duże wydarzenia. |
| **Archiwum** | W wersji 1.0 tylko link do istniejącego archiwum: <https://blekitna14.org/archiwum/index.html> (ta strona zostaje bez zmian). |
| **Błękitny Grom** *(później)* | Zarezerwowane miejsce, osobny wygląd w tej samej konstrukcji strony. |

Menu: **Start · Drużyny · Obóz · Archiwum**, plus ikony Facebooka, Instagrama i Flickra.

**Rezygnujemy z:** Aktualności, osobnych podstron O nas / Kontakt / Historia / 100-lecie, strony „10 powodów”.

**Kontakt:** szczepowy na stronie Start, drużynowi na kartach drużyn. Numery telefonów są jawne.

## Technologia (po ludzku)

- Strona napisana w Pythonie (Flask), zamieniana na zwykłe pliki, które hostujemy za darmo na GitHub Pages, pod tym samym adresem blekitna14.org. Nie potrzeba serwera ani opłat.
- Dane do aktualizacji (drużyny, drużynowi, telefony, terminy obozów) siedzą w jednym pliku. Zmiana numeru telefonu to edycja jednej linijki, a nie przepisywanie strony.
- Aktualizuje ktoś, kto programuje – rzadko, więc nie potrzebujemy panelu administracyjnego.
- Usuwamy z kodu klucze i hasła, które dziś leżą w repozytorium.

## Wygląd

Kolory i układ ustalimy na makietach, nie w tabelkach. Punkt wyjścia: obecny błękit marki (`#0BB5FF`), granat (`#293040`) i kremowe tło (`#FFFAF0`), maksymalnie jeden kolor dodatkowy. Strona ma być oparta na zdjęciach, wygodna na telefonie i czytelna.

## Kolejne kroki

1. Zatwierdzenie tego dokumentu przez szczepowego.
2. 2–3 makiety strony głównej do wyboru.
3. Budowa Start, Drużyny, Obóz.
4. Podgląd na gałęzi `redesign`, akceptacja, publikacja.

## Czego potrzebujemy od szczepu

- Lista drużyn: nazwy, przedziały wiekowe, dni i miejsca zbiórek.
- Dane kontaktowe szczepowego i drużynowych (imię, telefon, e-mail).
- Terminy, miejsca i ceny obozu i zimowiska, link do zapisów.
- Zdjęcie na główną i zdjęcia do obozu.
- Czy numery telefonów mogą być jawne (zakładamy, że tak).
