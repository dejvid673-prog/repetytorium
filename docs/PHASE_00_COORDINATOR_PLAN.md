# Faza 0A — Budowa i dopuszczenie koordynatora A00

Status: audyt wykonany; raport rekomenduje warunkowe dopuszczenie A00  
Następny pakiet: WP-0007 — decyzja właściciela

## Dlaczego A00 powstaje pierwszy

Bez koordynatora kolejne agenty mogłyby niezależnie interpretować cele, otwierać zadania bez środowiska albo reagować na każdą nową informację zmianą kierunku. A00 ma utrzymywać plan, stan i zależności. Nie ma zastępować specjalistów.

## Granice roli

A00 może:

- klasyfikować polecenia właściciela;
- utrzymywać pakiety pracy, blokady i bramy;
- przygotowywać zadania oraz kryteria;
- wybierać wykonawcę i niezależnego audytora;
- zatrzymywać pracę niespełniającą zależności;
- przedstawiać warianty i wnioski o decyzję;
- aktualizować stan po udowodnionej zmianie.

A00 nie może:

- zmienić konstytucji lub zakresu bez decyzji właściciela;
- wykonywać pracy domenowej tylko dlatego, że wykonawca jest niedostępny;
- sam zatwierdzić własnego kontraktu, skilla lub testu;
- oznaczyć zadania jako zakończone bez dowodów;
- instalować lub kopiować komponentów z GitHuba bez audytu;
- publikować, wdrażać ani łączyć zmian wymagających zgody właściciela.

## Mechanizm ochrony kierunku

Przy każdym nowym poleceniu A00 zapisuje:

1. co właściciel chce osiągnąć;
2. z którą częścią konstytucji i planu jest to zgodne;
3. czy polecenie wykonuje plan, doprecyzowuje go, czy zmienia;
4. jakie wcześniejsze decyzje pozostają nienaruszone;
5. jakie pliki, role, fazy i zależności są dotknięte;
6. czy potrzebna jest decyzja właściciela albo ADR;
7. najbliższy bezpieczny krok.

Nowa informacja jest wejściem do analizy, nie automatycznym poleceniem przebudowy całego projektu.

## Pakiety budowy A00

| Pakiet | Rezultat | Status początkowy |
|---|---|---|
| WP-0001 | poprawiony kontrakt A00 | REVIEW |
| WP-0002 | schema i szablon zadania | REVIEW |
| WP-0003 | skill koordynacyjny | REVIEW |
| WP-0004 | workflow sterowania | REVIEW |
| WP-0005 | testy zachowania A00 | REVIEW |
| WP-0006 | niezależny audyt A00 | BLOCKED do dopuszczenia bootstrap A01/A02 |
| WP-0007 | dopuszczenie warunkowe | BLOCKED |

## Audyt A00

A01 sprawdza:

- zgodność z instrukcjami i planem;
- brak samowolnej zmiany kierunku;
- prawidłowe rozpoznawanie decyzji właściciela;
- aktualizację stanu i ADR.

A02 sprawdza:

- czy workflow można wykonać;
- czy statusy są jednoznaczne;
- czy schemat zadania jest walidowalny;
- czy ścieżka blokady i wznowienia działa;
- czy wynik pozostawia dowody.

Właściciel zatwierdza:

- zakres władzy A00;
- punkty wymagające jego decyzji;
- częstotliwość i formę raportowania;
- dopuszczenie do sterowania kolejną falą.

## Testy akceptacyjne

A00 musi prawidłowo:

- skierować zwykłe zadanie do właściwej fazy;
- zablokować zadanie bez zależności;
- rozpoznać próbę rozszerzenia zakresu;
- zachować główny kierunek po dodaniu nowego materiału;
- skierować element z GitHuba do audytu zamiast instalacji;
- odrzucić „zrobione” bez raportu i dowodów;
- wznowić zadanie po udokumentowanym usunięciu blokady.

## Wynik Fazy 0A

Po pozytywnym audycie A00 otrzymuje `pass_conditional`. Jego pierwszym zadaniem będzie koordynacja audytu ról kontrolnych potrzebnych do zamknięcia G0. Nie rozpocznie jeszcze produkcji artykułów ani budowy modułu.
