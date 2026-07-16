# Audyt użyteczności A00 0.4

- Audyt: A00-UTILITY-2026-07-16
- Kontekst: 0.3
- Decyzja właściciela: OWNER-0001
- Automatyczna walidacja: GitHub Actions 29502504632 — SUCCESS
- Testy zachowania: 15/15 PASS
- Wynik: `pass_conditional`

## Ocena

Wersja 0.3 była bezpieczna, ale mogła stać się zbyt opisowa i kosztowna przy długim projekcie. Wersja 0.4 usuwa to ryzyko.

## Dodane mechanizmy

- minimalny kontekst obowiązkowy i ładowanie reszty według wpływu;
- wersjonowany rekord każdego cyklu zmieniającego stan;
- priorytety P0–P3;
- rozdzielenie committed i forecast;
- domyślnie jedno ACTIVE na wykonawcę;
- blokowanie równoległych `conflict_keys`;
- zachowanie poprzedniego stanu po zmianie polecenia;
- zakaz zastępowania niedostępnego specjalisty;
- ponowna walidacja starego READY;
- atomowa aktualizacja kart, pakietów, gałęzi, bram i stanu;
- blokada `STATE_DIVERGENCE`;
- rewizje stanu i odciski wejść;
- zachowanie częściowych wyników przy anulowaniu.

## Testy graniczne

A00 poprawnie zablokował konflikt gałęzi, przekroczony WIP, brak specjalisty, stare READY, częściową aktualizację stanu i instrukcję wstrzykniętą do materiału. Przy P0/B4 zatrzymał dotkniętą pracę bez samodzielnego przejmowania naprawy.

## Zakres dopuszczenia

Obowiązuje zakres z OWNER-0001 oraz `registries/agents.yaml`. A00 nie może scalać fundamentu do `main`, publikować, wdrażać, zmieniać zakresu ani wykonywać pracy specjalistycznej.

## Pozostałe ograniczenia

1. Workflow pozostaje deklaratywny, co jest właściwe na obecnym etapie.
2. Ocena A01/A02 nie była wykonana jako dwie niezależne sesje modeli.
3. Po zamknięciu bootstrapu A01 i A02 wymagają osobnego dopuszczenia do zwykłych audytów agentów.
4. Zmiana kontraktu A00 albo jego władzy wymaga ponownego audytu.

## Wniosek

A00 nie znajduje się już na granicy praktycznej użyteczności. Jest wystarczająco precyzyjny do prowadzenia Fazy 0C i dalszego planowania, przy zachowaniu warunkowego oraz ograniczonego zakresu.
