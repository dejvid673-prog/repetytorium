# Aktualny stan projektu

Ostatnia aktualizacja: 2026-07-16  
Wersja stanu: 6  
Kontekst: 0.3  
Faza: 0C — zewnętrzne poszukiwanie przed dalszą budową agentów  
Stan: A00, A01 i A02 mają ograniczone `pass_conditional`; Codex poboczny działa wyłącznie odczytowo

## A00

- kontrakt: 0.4;
- status: `pass_conditional`;
- decyzja: OWNER-0001;
- testy: 15/15 PASS;
- raport: `reports/agent-audits/A00/2026-07-16-utility-reaudit-v0.4.md`.

A00 koordynuje poszukiwania, porządkuje surowe wyniki, usuwa duplikaty i stosuje procedurę przyjęcia zewnętrznego komponentu. Nie może uznać kandydata za przyjętego bez wymaganych dowodów, audytu i decyzji.

## A01 i A02

- kontrakty: 0.2;
- status: `pass_conditional`;
- decyzja: OWNER-0002;
- testy A01: 6/6 PASS;
- testy A02: 6/6 PASS;
- ograniczenie: testy syntetyczne wykonano w jednej głównej sesji, bez niezależnych sesji krzyżowych.

A01 audytuje kontekst, ład i zakres. A02 audytuje workflow, skille, schematy i testy. Żaden z nich nie jest zatwierdzonym twórcą schematów WP-0011.

## Codex poboczny — tryb read-only

Decyzja OWNER-0003 ustanawia Codexa jako pomocniczego wykonawcę poszukiwań GitHub:

- może czytać to repozytorium i publiczny GitHub;
- nie może zmieniać plików, gałęzi, commitów, PR, issue ani rejestrów;
- dostarcza użytkownikowi surowe dane i dowody;
- A00 wykonuje integrację wyników z projektem;
- backlog: `docs/CODEX_READ_ONLY_RESEARCH_BACKLOG.md`.

Poszukiwanie jest wymagane przed istotnym tworzeniem lub przebudową własnego agenta, skilla, workflow albo mechanizmu agentowego. Nie dotyczy każdej drobnej czynności.

## Pakiety i bramy

- WP-0001–WP-0007: `COMPLETED`;
- WP-0010: `COMPLETED`;
- WP-0011: `BLOCKED` — oczekuje na DISC-001 i ustalenie właściwego wykonawcy;
- WP-0012: `BLOCKED`;
- G0A: `PASSED`;
- G0B: `UNDER_REVIEW`;
- G0: `OPEN`;
- fazy wykonawcze pozostają zablokowane.

## Otwarte decyzje i ograniczenia

- ADR-0005 — strategia gałęzi i bram;
- licencja przed publicznym współtworzeniem;
- A01/A02 wymagają niezależnego audytu krzyżowego przed statusem `active`;
- workflow A00 pozostaje deklaratywny (`runtime_implemented: false`);
- zewnętrzne rozwiązania nie eliminują audytu licencji, bezpieczeństwa, integracji i rollbacku.

## Następny bezpieczny krok

Uruchomić `DISC-001 — Protokoły handoff, checkpoint i resume` w pobocznym Codexie z dostępem wyłącznie do odczytu. Po dostarczeniu surowych kandydatów A00 przeprowadzi deduplikację, ocenę i ponowny test gotowości WP-0011.

