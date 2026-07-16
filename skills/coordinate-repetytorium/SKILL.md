---
name: coordinate-repetytorium
description: Coordinate work in dejvid673-prog/repetytorium by protecting the approved direction, classifying owner requests, checking authority, priorities, conflicts, phase gates and dependencies, preparing bounded tasks, tracking evidence and repairing state drift. Use for project-management commands, resumes, phase transitions, agent assignments, external GitHub candidates or plan changes.
---

# Koordynowanie Repetytorium

## 1. Tryb i dopuszczenie

Ustal `mode: validation | live`. W `live` potwierdź status A00 i `activation_scope`. Brak dopuszczenia dla żądanej klasy oznacza STOP.

## 2. Minimalny kontekst

Przeczytaj `PROJECT_CONTEXT.yaml`, `docs/CURRENT_STATE.md`, decyzje, wpis A00, nowe wejście i ostatni powiązany rekord. Pozostałe pliki ładuj według wpływu. Stosuj `OPERATING_PROTOCOL.md`.

## 3. Kontrola wejścia

1. Ustal cel i relację do wcześniejszego polecenia.
2. Oddziel fakty od wniosków.
3. Sklasyfikuj wejście.
4. Nadaj P0–P3.
5. Wskaż chronione decyzje i granice władzy.
6. Przy zmianie zakresu lub zastrzeżonej decyzji przejdź do `DECISION_REQUIRED`.

## 4. Kontrola gotowości

Sprawdź jednocześnie:

- committed work package i wymaganą bramę;
- aktualność wejść oraz ich odciski;
- dopuszczenie wykonawcy i recenzentów;
- rozdzielenie obowiązków;
- WIP agenta;
- kolizje `conflict_keys`, ścieżek i gałęzi;
- środowisko;
- kryteria, testy i plan odzyskania.

Niespełnienie warunku oznacza `BLOCKED` z właścicielem i dowodem odblokowania.

## 5. Wybór działania

Wybierz dokładnie jedno: `answer_only`, `prepare_task`, `update_state`, `block`, `request_owner_decision`, `cancel`, `repair_state` albo `no_action`.

Nie wykonuj zadania specjalistycznego za brakującego agenta.

## 6. Atomowy zapis

Przed mutacją przygotuj pełny zestaw dotkniętych kart, pakietów, gałęzi, bram i stanu. Każda zmiana zwiększa rewizję. Częściowy lub sprzeczny zapis tworzy `STATE_DIVERGENCE` i blokuje dalszą pracę zależną.

Cykl zmieniający stan zapisuje rekord zgodny z `schemas/a00-control-record.schema.json`.

## 7. Wznowienie i nowe polecenie

Nie ufaj staremu `READY`. Ponownie sprawdź kontekst, wejścia, agentów, bramy, konflikty i środowisko. Nowe polecenie nie usuwa cicho aktywnej pracy; zapisz, czy ją zastępuje, rozszerza, repriorytetyzuje czy tylko pyta o stan.

## 8. Zamknięcie

Zamknij cykl dopiero po spójnym stanie, dowodach, jawnych testach niewykonanych, znanym właścicielu blokady i jednoznacznym następnym kroku.

## Ograniczenia validation

Dozwolone są syntetyczne testy i raport audytu. Zabronione są rzeczywiste przydziały, zmiany rejestrów operacyjnych, gałęzie, PR, decyzje właściciela, scalanie, publikacja i wdrożenie.

## Kandydat GitHub

Stosuj `docs/GITHUB_SOURCE_INTAKE.md`: inspekcja statyczna, przypięty commit, licencja, minimalne uprawnienia, testy, niezależny audyt i plan wycofania.
