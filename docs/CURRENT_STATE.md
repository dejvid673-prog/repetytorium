# Aktualny stan projektu

Ostatnia aktualizacja: 2026-07-16  
Wersja stanu: 5  
Kontekst: 0.3  
Faza: 0C — role kontrolne dopuszczone warunkowo  
Stan: A00, A01 i A02 mają ograniczone `pass_conditional`; G0A zamknięta pozytywnie

## A00

- kontrakt: 0.4;
- status: `pass_conditional`;
- decyzja: OWNER-0001;
- testy: 15/15 PASS;
- raport: `reports/agent-audits/A00/2026-07-16-utility-reaudit-v0.4.md`.

A00 może prowadzić triage, zależności, priorytety, rejestry, pakiety, audyty, przyjmowanie materiałów, karty zadań i naprawę spójności stanu. Nie może zmieniać zakresu, wykonywać pracy specjalistycznej, scalać do `main`, publikować ani wdrażać.

## A01 i A02

- kontrakty: 0.2;
- status: `pass_conditional`;
- decyzja: OWNER-0002;
- testy A01: 6/6 PASS;
- testy A02: 6/6 PASS;
- zakres: wyłącznie klasy audytu jawnie wpisane w kontraktach i rejestrze;
- ograniczenie: testy syntetyczne wykonano w jednej głównej sesji, bez niezależnych sesji krzyżowych.

A01 może audytować kontekst, ład, hierarchię instrukcji, Context Gate i spójność stanu. A02 może audytować workflow, skille, schematy, szablony, fixture i twierdzenia o walidacji. Żaden z nich nie może naprawiać badanego elementu w tym samym zadaniu ani samodzielnie aktywować agentów.

## Naprawa spójności

Przed dopuszczeniem naprawiono `STATE_DIVERGENCE`:

- wersję A00 w rejestrze zsynchronizowano do 0.4;
- WP-0001–WP-0007 mają spójny status `COMPLETED`;
- kanoniczny rejestr decyzji otrzymał `state_revision`;
- wygasły zakres bootstrap A01/A02 zastąpiono decyzją OWNER-0002.

Dowód: `reports/audits/2026-07-16-state-divergence-repair-a01-a02.md`.

## Pakiety i bramy

- WP-0001–WP-0007: `COMPLETED`;
- WP-0010: `COMPLETED` — pełny audyt A01/A02;
- WP-0011: `READY` — schematy przekazań agentów;
- G0A: `PASSED`;
- G0B: `UNDER_REVIEW`;
- G0: `OPEN`;
- fazy wykonawcze pozostają zablokowane.

## Otwarte decyzje i ograniczenia

- ADR-0005 — strategia gałęzi i bram;
- licencja przed publicznym współtworzeniem;
- A01/A02 wymagają niezależnego audytu krzyżowego przed statusem `active`;
- workflow A00 pozostaje deklaratywny (`runtime_implemented: false`).

## Następny bezpieczny krok

Rozpocząć WP-0011: przygotować walidowalne schematy przekazań agentów. Nie uruchamiać jeszcze produkcji treści, implementacji modułu ani Fazy 1K/1T.

