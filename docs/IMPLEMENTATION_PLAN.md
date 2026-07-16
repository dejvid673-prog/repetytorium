# Konkretny plan realizacji projektu

Status: plan wykonawczy 0.1 do zatwierdzenia  
Właściciel sterowania: A00 po dopuszczeniu  
Rejestr zadań: `registries/work-packages.yaml`

## Zasada wykonania

Plan określa kolejność rezultatów, a nie tylko listę pomysłów. Każdy etap ma wejście, wyjście, zależność, wykonawcę, audytora i bramę. Nowa informacja może doprecyzować plan, ale nie zmienia głównego kierunku bez analizy wpływu i decyzji właściciela.

## Faza 0A — Uruchomienie koordynatora A00

To jest pierwszy wykonywany obszar. Pozostałe role nie są aktywowane przed powstaniem mechanizmu sterowania.

### Etapy

1. **0A.1 Kontrakt A00**
   - zdefiniować misję, uprawnienia, zakazy i granice;
   - wskazać dokładne wejścia i wyjścia;
   - oddzielić koordynowanie od wykonywania pracy specjalistycznej;
   - zapisać warunki zatrzymania i eskalacji.
   - Wyjście: `agents/A00-project-manager/AGENT.md`.

2. **0A.2 Model zadania**
   - przygotować schemat zadania, identyfikatory, statusy i kryteria akceptacji;
   - wymagać zależności, środowiska, wykonawcy i audytora;
   - wymagać dowodów testów.
   - Wyjście: `schemas/project-task.schema.json` i `templates/TASK_BRIEF.yaml`.

3. **0A.3 Skill koordynacyjny**
   - zapisać krótką, wykonywalną procedurę ochrony planu;
   - odsyłać do dokumentów źródłowych zamiast je dublować;
   - nie instalować skilla poza tym repozytorium.
   - Wyjście: `skills/coordinate-repetytorium/SKILL.md`.

4. **0A.4 Workflow sterowania**
   - obsłużyć wejście polecenia, analizę wpływu, blokady, przydział, audyt, korektę i zamknięcie;
   - zapewnić możliwość wznowienia po blokadzie.
   - Wyjście: `workflows/project-control.yaml`.

5. **0A.5 Testy A00**
   - polecenie zgodne z planem;
   - polecenie zmieniające zakres;
   - nowy materiał właściciela;
   - kandydat z zewnętrznego repozytorium;
   - brak środowiska;
   - deklaracja ukończenia bez dowodów.
   - Wyjście: `tests/agents/A00/cases.yaml`.

6. **0A.6 Audyt A00**
   - A01: zgodność z kontekstem i planem;
   - A80: wykonalność procedur, formatów i narzędzi;
   - właściciel: granice decyzyjne.
   - Wyjście: raport w `reports/agent-audits/A00/`.

7. **0A.7 Dopuszczenie warunkowe**
   - A00 może kierować tylko klasami zadań wskazanymi w raporcie;
   - nie może sam zatwierdzić zmiany zakresu ani własnego audytu.

**Brama G0A:** A00 ma ważny raport, przechodzi testy i otrzymuje co najmniej `pass_conditional`.

## Faza 0B — Narzędzia sterowania i materiały właściciela

1. Utworzyć miejsce na instrukcje właściciela: `source-materials/`.
2. Ustalić nazewnictwo, metadane, wersjonowanie i zakaz danych klientów.
3. Każdy nowy materiał skierować do A00.
4. A00 klasyfikuje materiał jako:
   - potwierdzenie istniejącego planu;
   - doprecyzowanie;
   - kandydat na zmianę;
   - materiał referencyjny;
   - odrzucony lub wymagający wyjaśnienia.
5. Nie nadpisywać konstytucji ani ADR samym dodaniem pliku.
6. Zbudować raport stanu, rejestr pakietów pracy i rejestr decyzji.

**Brama G0B:** nowe materiały mają kontrolowaną ścieżkę wejścia i nie mogą cicho zmienić planu.

## Faza 0C — Audyt systemu agentów

1. Audyt falami według `docs/AGENT_AUDIT_MATRIX.md`.
2. Najpierw role kontrolne A01, A11, A40, A41 i A80.
3. Następnie agenci badań i treści.
4. Później UX, grafika, PrestaShop, SEO i analityka.
5. Dla każdej roli:
   - kontrakt;
   - schema wejścia i wyjścia;
   - skill, jeśli potrzebny;
   - workflow przekazania;
   - testy;
   - audyty krzyżowe;
   - decyzja o dopuszczeniu.
6. Łączyć lub dzielić role tylko po analizie konfliktów.

**Brama G0:** role potrzebne dla 1K i 1T są dopuszczone, a właściciel zatwierdza kierunek.

## Faza 1K — Architektura wiedzy

1. Słownik terminów polskich, potocznych i naukowych.
2. Taksonomia tematów, problemów, gatunków i parametrów.
3. Typy artykułów i wymagane sekcje.
4. Model twierdzeń, źródeł, pewności, sprzeczności i ryzyka.
5. Statusy widoczności, redakcji, weryfikacji i aktualności.
6. Korekty, podziękowania, historia zmian i zgody.
7. Pakiet badawczy i publikacyjny.
8. Fixture dla chemii, gatunku, problemu zdrowotnego i techniki.
9. Walidacja oraz audyty A40, A41 i A82.

**Brama G1K:** schematy są walidowalne i pokrywają rzeczywiste przypadki bez reklam produktów.

## Faza 1T — Środowisko techniczne

1. Przypiąć wspierane wersje PrestaShop 9, PHP, bazy i narzędzi.
2. Zbudować odtwarzalne DEV bez sekretów.
3. Zbudować automatyczne TEST z syntetycznymi danymi.
4. Ustalić standardy kodu, konfiguracji i logowania.
5. Uruchomić CI: lint, analiza statyczna, testy, walidacja schematów i kontrola sekretów.
6. Przygotować backup, restore, migracje i rollback.
7. Zlecić A80 niezależne odtworzenie.

**Brama G1T:** ENV-DEV i ENV-TEST są powtarzalne.

## Faza 2 — Pilotażowa fabryka badań i treści

1. Przyjąć jeden reprezentatywny raport głębokiego badania.
2. Zachować oryginał bez zmian.
3. Wyodrębnić twierdzenia, źródła, luki i ryzyko.
4. Rozdzielić zagadnienia do właściwych badaczy.
5. Podzielić materiał na portfel artykułów.
6. Zredagować treść oraz warstwę prezentacyjną.
7. Wykonać audyty dowodów i bezpieczeństwa.
8. Cofnąć błędy do właściwego etapu.
9. Zbudować co najmniej trzy różne pakiety publikacyjne.
10. Udokumentować pełne przekazanie.

**Brama G2:** pilotaż jest odtwarzalny, a status weryfikacji ma dowody.

## Faza 3 — UX, makiety i system wizualny

1. Zbudować architekturę informacji na zatwierdzonej taksonomii.
2. Zaprojektować ścieżki: problem, temat, gatunek i nauka.
3. Przygotować wireframes bez dekoracji.
4. Ustalić kierunek wizualny, tokeny i komponenty.
5. Zaprojektować ikony i miniatury bez emoji.
6. Wykonać responsywne makiety HTML na prawdziwej treści pilotażowej.
7. Sprawdzić prawa do grafik.
8. Przeprowadzić audyt WCAG 2.2 AA.
9. Zebrać decyzje właściciela i poprawić makiety.

**Brama G3:** właściciel zatwierdza reprezentatywne widoki desktop i mobile.

## Faza 4 — Rdzeń modułu PrestaShop

1. Zatwierdzić ADR architektury modułu.
2. Zaimplementować własne tabele, encje i indeksy.
3. Zaimplementować migracje, instalację i odinstalowanie.
4. Zbudować role, uprawnienia i Back Office.
5. Zbudować walidowany, idempotentny importer.
6. Zbudować wersjonowanie, historię i wycofanie.
7. Przygotować publiczne trasy bez modyfikacji core.
8. Wykonać testy bezpieczeństwa, migracji i utraty danych.

**Brama G4:** rdzeń jest bezpieczny, aktualizowalny i nie dubluje danych.

## Faza 5 — Front Office, wyszukiwanie i SEO

1. Zaimplementować zaakceptowane komponenty.
2. Renderować artykuły, gatunki, statusy i korekty.
3. Wdrożyć wyszukiwanie, synonimy, literówki i nazwy naukowe.
4. Dodać filtry, breadcrumbs, powiązania i obsługę braku wyniku.
5. Wdrożyć stabilne URL, canonical, sitemap i dane strukturalne.
6. Przeprowadzić audyty techniczne, dostępności i SEO.

**Brama G5:** użytkownik znajduje właściwe treści językiem potocznym.

## Faza 6 — Biblioteka startowa

1. Zatwierdzić macierz pokrycia tematów.
2. Produkować treści w kontrolowanych partiach.
3. Tworzyć lub pozyskiwać grafiki z rejestrem praw.
4. Audytować materiały wysokiego ryzyka.
5. Importować do STAGE i wykonywać podgląd.
6. Usuwać puste działy, niespójności i błędne linki.
7. Zamrozić kandydatkę biblioteki.

**Brama G6:** każda widoczna kategoria zawiera wartościową, zweryfikowaną treść.

## Faza 7 — Kontakt, korekty i analityka

1. Zdefiniować katalog zdarzeń, cele i retencję.
2. Rozdzielić dane kontaktowe od analityki.
3. Wdrożyć zgody, pseudonimizację i usunięcie danych.
4. Ustalić obsługę e-maili, zdjęć, uwag i pytań.
5. Wdrożyć korektę, ponowną weryfikację i komunikat z datą.
6. Publikować podziękowanie z nazwiskiem wyłącznie po zgodzie.

**Brama G7:** kontakt i pomiar nie naruszają prywatności.

## Faza 8 — Kwalifikacja wydania

1. Funkcjonalność i regresja.
2. Bezpieczeństwo, prywatność i uprawnienia.
3. WCAG, mobile, desktop i przeglądarki.
4. SEO, wyszukiwarka, linki i grafiki.
5. Wydajność i błędne dane.
6. Migracje, import, backup, restore i rollback.
7. Audyt treści i jawności AI.
8. UAT właściciela.

**Brama G8:** brak błędów krytycznych i wysokich; rollback jest udowodniony.

## Faza 9 — Uruchomienie

1. Zamrozić wersję i zakres.
2. Wykonać kopię zapasową.
3. Wdrożyć na produkcję.
4. Wykonać smoke test.
5. Sprawdzić indeksowanie i monitoring.
6. Podjąć decyzję kontynuować albo wycofać.
7. Zapisać raport powdrożeniowy.

## Faza 10 — Utrzymanie

Cyklicznie sprawdzać aktualność, źródła, korekty, luki wyszukiwania, agentów, skille, workflow, moduł i bezpieczeństwo. Każda zmiana przechodzi tę samą kontrolę zależności co budowa początkowa.

## Faza 11 — Przypadki czytelników

Funkcja pozostaje zablokowana do osobnego ADR. Jej model minimalny można przewidzieć wcześniej, ale nie budujemy forum ani bezpośredniego uploadu zdjęć.

## Materiały, które właściciel może dostarczyć

Najbardziej pomocne będą:

- instrukcje i ograniczenia biznesowe;
- informacje o istniejącym sklepie i środowisku PrestaShop;
- zasady marki, logo, kolory i przykłady estetyki;
- przykłady pytań klientów;
- raporty głębokich badań;
- przykłady artykułów uznanych za dobre lub złe;
- wymagania dotyczące hostingu i wdrażania;
- informacje o używanych już narzędziach.

Materiały trafiają do `source-materials/`. Dodanie materiału nie oznacza automatycznej zmiany planu.
