# Instrukcje dla agentów i narzędzi

Ten plik obowiązuje w całym repozytorium. Instrukcja lokalna umieszczona głębiej może doprecyzować pracę w swoim katalogu, ale nie może bez wyraźnej decyzji architektonicznej unieważnić zasad bezpieczeństwa, źródeł i odpowiedzialności określonych tutaj.

## 1. Cel repozytorium

Repozytorium służy wyłącznie do budowy i utrzymania Repetytorium Staw Expert: systemu wiedzy o stawach, oczkach wodnych, wodzie i rybach oraz jego integracji z PrestaShop 9.

Nie należy umieszczać tutaj niezależnych modułów sklepowych, ogólnych automatyzacji 7DEJV OS, prywatnych danych klientów ani materiałów niezwiązanych z repetytorium.

## 2. Kolejność orientacji

Przed rozpoczęciem pracy agent ma:

1. przeczytać `README.md`;
2. przeczytać ten plik;
3. przeczytać dokumentację wskazaną dla danego katalogu;
4. sprawdzić `docs/decisions/`;
5. przeszukać repozytorium pod kątem istniejącego rozwiązania;
6. sprawdzić aktualny stan Git, gałąź i otwarte zmiany;
7. dopiero potem zaproponować lub wykonać zmianę.

Nie wolno zakładać istnienia pliku, agenta, skilla, schematu, funkcji lub testu bez sprawdzenia.

## 3. Źródło prawdy

- Badania źródłowe: `research/`.
- Ustrukturyzowana wiedza i taksonomia: docelowo `knowledge/`.
- Artykuły: `articles/`.
- Grafiki i ich licencje: `assets/`.
- Definicje agentów: `agents/`.
- Workflow: docelowo `workflows/`.
- Schematy danych: `schemas/`.
- Moduł PrestaShop: docelowo `module/`.
- Decyzje projektowe: `docs/decisions/`.

Nie wolno traktować treści opublikowanej w PrestaShop jako nowszej od repozytorium bez udokumentowanej synchronizacji zwrotnej.

## 4. Granice odpowiedzialności

Agent wykonuje tylko zadania należące do jego roli. W szczególności:

- analityk badań nie publikuje artykułów;
- redaktor nie tworzy brakujących faktów;
- grafik nie zatwierdza twierdzeń merytorycznych;
- integrator PrestaShop nie zmienia znaczenia treści;
- projektant interfejsu nie zmienia modelu wiedzy bez decyzji;
- żaden agent nie publikuje materiału wymagającego zatwierdzenia właściciela.

## 5. Źródła i prawdziwość

Każde twierdzenie techniczne, chemiczne, biologiczne lub dotyczące zdrowia ryb musi być możliwe do powiązania ze źródłem albo jasno oznaczone jako hipoteza.

Priorytet źródeł:

1. akty prawne, normy i dokumenty urzędowe;
2. publikacje naukowe i akademickie;
3. karty SDS, dane CLP i dokumentacja producenta;
4. oficjalna dokumentacja techniczna;
5. wiarygodne źródła branżowe;
6. fora i blogi wyłącznie pomocniczo.

Nie wolno:

- wymyślać źródeł, wyników badań ani cytatów;
- przedstawiać korelacji jako przyczyny;
- podawać dawkowania bez danych wejściowych i oceny ryzyka;
- diagnozować choroby ryb wyłącznie na podstawie jednego objawu;
- ukrywać sprzeczności pomiędzy źródłami.

## 6. Bezpieczeństwo treści

Materiały dotyczące chemii, jakości wody, leczenia i zdrowia ryb wymagają obowiązkowej kontroli merytorycznej przed publikacją.

Należy uwzględniać między innymi:

- gatunki i wielkość ryb;
- objętość oraz typ zbiornika;
- temperaturę i natlenienie;
- pH, KH, GH, amoniak/amonię, azotyny i inne istotne parametry;
- filtrację biologiczną;
- rośliny i bezkręgowce;
- interakcje substancji;
- wpływ na środowisko;
- prawo i wymagane oznakowanie.

## 7. Powiązania ze sklepem

Treść merytoryczna ma pierwszeństwo przed sprzedażą. Produkt można powiązać tylko wtedy, gdy istnieje udokumentowane uzasadnienie zastosowania.

Agent może zaproponować powiązanie produktu, ale nie może automatycznie zatwierdzić go do publikacji. Repetytorium ma pozostać wiarygodne również wtedy, gdy sklep nie posiada odpowiedniego produktu.

## 8. Grafiki i prawa

Każda grafika musi mieć ustalone pochodzenie, licencję i zakres dozwolonego użycia. Nie wolno kopiować przypadkowych grafik z internetu.

Preferowane są:

- materiały własne;
- materiały z udokumentowaną licencją komercyjną;
- materiały producenta z udokumentowanym prawem użycia;
- ilustracje przygotowane specjalnie dla projektu.

Emoji nie są docelowym systemem ikon interfejsu.

## 9. PrestaShop

Domyślna platforma: PrestaShop 9.

Zasady:

- nie modyfikować core;
- preferować oddzielny moduł, hooki, kontrolery i usługi Symfony;
- stosować oddzielne tabele dla wiedzy i relacji;
- zabezpieczać Back Office uprawnieniami i tokenami;
- uwzględniać CSRF, XSS, SQL injection, walidację i minimalne uprawnienia;
- zmiany treści i modułu muszą być możliwe do wycofania;
- nie publikować bez podglądu i kontroli.

## 10. Git i zakres zmian

- Pracować na osobnej gałęzi.
- Wprowadzać minimalny zakres potrzebny do zadania.
- Nie wykonywać szerokiego refaktoru bez uzasadnienia.
- Nie usuwać materiału źródłowego bez decyzji i ścieżki odzyskania.
- Nie nadpisywać cudzych zmian.
- Aktualizować dokumentację, jeśli zmiana wpływa na architekturę lub workflow.
- Trwałe decyzje zapisywać jako ADR w `docs/decisions/`.

## 11. Testy i raport

Agent ma odróżniać:

- analizę;
- przygotowany kod;
- zmianę zapisaną w repozytorium;
- test statyczny;
- test automatyczny;
- test integracyjny;
- wdrożenie;
- publikację produkcyjną.

Raport zadania musi zawierać:

- zmienione pliki;
- wykonane testy i ich wyniki;
- testy niewykonane wraz z powodem;
- błędy, ryzyka i ograniczenia;
- stan kryteriów akceptacji;
- następny krok.

## 12. Zakaz sekretów i danych klientów

Nie wolno zapisywać w repozytorium:

- haseł;
- tokenów;
- kluczy API;
- danych klientów;
- danych zamówień;
- produkcyjnych plików konfiguracyjnych z sekretami;
- prywatnych danych kontaktowych bez uzasadnionej potrzeby i ochrony.
