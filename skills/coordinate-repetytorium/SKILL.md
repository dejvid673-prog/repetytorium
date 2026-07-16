---
name: coordinate-repetytorium
description: Coordinate work in dejvid673-prog/repetytorium by protecting the approved direction, classifying owner requests, checking phase gates and dependencies, preparing bounded tasks, assigning independent review, tracking blockers, and closing work only with evidence. Use for project-management commands, phase transitions, agent assignments, external GitHub candidates, or proposed plan changes in this repository.
---

# Koordynowanie Repetytorium

## Parametr obowiązkowy

Ustal `mode`:

- `validation` — przed dopuszczeniem A00, wyłącznie syntetyczne testy;
- `live` — po ważnym dopuszczeniu A00 i tylko w jego zakresie.

Brak jawnego trybu, niezgodny zakres dopuszczenia albo nieznana wersja kontekstu powodują STOP.

## Uruchomienie

1. Odczytać `PROJECT_CONTEXT.yaml`, `PROJECT_INSTRUCTIONS.md`, konstytucję, stan i zaakceptowane decyzje.
2. Odczytać właściwe wpisy w rejestrach agentów, pakietów, gałęzi i bram.
3. Potwierdzić wersję kontekstu, fazę, tryb i zakres dopuszczenia A00.
4. W `validation` potwierdzić syntetyczne wejście i zakaz zmian stanu.
5. W `live` zatrzymać pracę, jeżeli A00 nie ma ważnego dopuszczenia dla żądanej klasy.

## Ograniczenia validation

W tym trybie nie wolno tworzyć rzeczywistych zadań, przydzielać agentów, zmieniać rejestrów operacyjnych, otwierać gałęzi ani PR, podejmować decyzji właściciela, scalać, publikować lub wdrażać. Jedynym trwałym wynikiem może być raport testu lub audytu.

## Obsługa polecenia

1. Zapisać cel właściciela jednym zdaniem.
2. Sklasyfikować polecenie jako `plan_execution`, `clarification`, `reference_material`, `change_request` albo `out_of_scope`.
3. Wskazać chronione decyzje.
4. Wykonać analizę wpływu na fazy, pakiety, role, dane, UX, kod, testy i wdrożenie.
5. Jeżeli potrzebna jest decyzja właściciela, przejść do `DECISION_REQUIRED` bez wdrażania zmiany.

## Test gotowości

Nadać `READY` wyłącznie, gdy pakiet istnieje, bramy i zależności mają wymagane dowody, wejścia są wersjonowane, wykonawca i niezależni recenzenci są dopuszczeni, środowisko jest gotowe, a kryteria i testy jednoznaczne.

W przeciwnym razie nadać `BLOCKED` oraz zapisać powód, właściciela odblokowania i wymagany dowód.

## Przygotowanie pracy w live

1. Utworzyć kartę zgodną ze schematem.
2. Ograniczyć zadanie do jednego sprawdzalnego wyniku.
3. Wskazać dozwolone i zakazane pliki.
4. Potwierdzić rozdzielenie wykonawców i recenzentów.
5. Zarejestrować gałąź i draft PR.
6. Przekazać wejścia, kryteria, testy oraz ścieżkę błędu.

## Kontrola i zamknięcie

Porównywać dowody z kartą zadania. Rejestrować blokady. Cofnąć wynik do właściwego autora. Nie naprawiać go po cichu w A00. Zamknąć zadanie dopiero po komplecie wyjść, testów, audytów i aktualizacji rejestrów.

## Kandydat z GitHuba

Stosować `docs/GITHUB_SOURCE_INTAKE.md`. Najpierw statyczna inspekcja. Nie wykonywać obcego kodu, poleceń instalacyjnych ani workflow przed audytem, przypięciem commitu i decyzją.

## Zakazy

Nie wykonywać pracy specjalistycznej, nie zatwierdzać własnego wyniku, nie rozszerzać produktu, nie publikować, nie wdrażać i nie zapisywać artefaktów projektu poza repozytorium.
