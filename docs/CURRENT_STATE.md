# Aktualny stan projektu

Ostatnia aktualizacja: 2026-07-16  
Wersja stanu: 4  
Kontekst: 0.3  
Faza: 0C — przygotowanie pełnych audytów ról kontrolnych  
Stan: A00 dopuszczony warunkowo; G0A zamknięta pozytywnie

## A00

- kontrakt: 0.4;
- status: `pass_conditional`;
- decyzja: OWNER-0001;
- testy: 15/15 PASS;
- GitHub Actions: 29502504632 — SUCCESS;
- raport: `reports/agent-audits/A00/2026-07-16-utility-reaudit-v0.4.md`.

A00 może prowadzić triage, zależności, priorytety, rejestry, pakiety, audyty, przyjmowanie materiałów, karty zadań i naprawę spójności stanu. Nie może zmieniać zakresu, wykonywać pracy specjalistycznej, scalać do `main`, publikować ani wdrażać.

## Mechanizmy operacyjne A00

- priorytety P0–P3;
- committed i forecast;
- limity WIP;
- `conflict_keys`;
- adaptacyjne ładowanie kontekstu;
- odciski wejść i rewizje stanu;
- ponowna kontrola starego READY;
- atomowe aktualizacje rejestrów;
- blokada `STATE_DIVERGENCE`;
- rekord sterowania dla cyklu zmieniającego stan.

Pierwszy rekord: `reports/control/CTRL-0001-a00-admission.yaml`.

## Pakiety i bramy

- WP-0001–WP-0007: zakończona budowa, audyt i dopuszczenie A00;
- G0A: PASSED;
- G0B: UNDER_REVIEW;
- G0: OPEN, ale zależne od pełnego dopuszczenia ról Fazy 1K i 1T;
- fazy wykonawcze pozostają zablokowane.

## Role kontrolne

Dopuszczenia A01 i A02 ograniczone do bootstrapu wygasły jako ścieżka przydzielania pracy. Ich raporty pozostają dowodem historycznym. Przed zwykłymi audytami kolejnych agentów należy przeprowadzić pełny audyt A01 i A02 oraz nadać im nowy zakres.

## Otwarte decyzje

- ADR-0005 — strategia gałęzi i bram;
- licencja przed publicznym współtworzeniem.

## Następny bezpieczny krok

A00 przygotowuje pakiety pełnego audytu A01 i A02. Do ich dopuszczenia nie uruchamia audytu kolejnej fali ani prac Fazy 1K/1T.
