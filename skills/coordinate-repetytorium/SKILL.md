---
name: coordinate-repetytorium
description: Coordinate work in dejvid673-prog/repetytorium by protecting the approved direction, classifying owner requests, checking phase gates and dependencies, preparing bounded tasks, assigning independent review, tracking blockers, and closing work only with evidence. Use for every project-management command, phase transition, agent assignment, external GitHub candidate, or proposed plan change in this repository.
---

# Koordynowanie Repetytorium

## Uruchomienie

1. Przeczytać `PROJECT_INSTRUCTIONS.md`, konstytucję, `docs/IMPLEMENTATION_PLAN.md`, `docs/CURRENT_STATE.md` i właściwe ADR.
2. Odczytać `registries/work-packages.yaml`, `registries/branches.yaml` i `registries/phase-gates.yaml`.
3. Potwierdzić wersję kontekstu, fazę i zakres dopuszczenia A00.
4. Zatrzymać pracę, jeżeli A00 nie ma ważnego audytu dla żądanej klasy zadania.

## Obsługa polecenia

1. Zapisać cel właściciela jednym zdaniem.
2. Sklasyfikować polecenie:
   - wykonanie planu;
   - doprecyzowanie;
   - materiał referencyjny;
   - wniosek o zmianę;
   - poza zakresem.
3. Wskazać niezmienne decyzje, których polecenie nie uchyla.
4. Wykonać analizę wpływu na fazy, pakiety, agentów, dane, UX, kod, testy i wdrożenie.
5. Jeżeli polecenie zmienia zakres lub architekturę, przygotować decyzję dla właściciela. Nie wdrażać zmiany przed akceptacją.

## Test gotowości

Nadać zadaniu `READY` wyłącznie, gdy:

- pakiet pracy istnieje;
- wymagana brama jest otwarta;
- wszystkie zależności mają dowody;
- wejścia są kompletne i wersjonowane;
- wykonawca ma właściwe dopuszczenie;
- audytor jest niezależny;
- środowisko jest gotowe;
- wynik i kryteria akceptacji są jednoznaczne;
- istnieje plan testów i odzyskania, jeśli jest potrzebny.

W przeciwnym razie nadać `BLOCKED`, zapisać powód, właściciela odblokowania i wymagany dowód.

## Przygotowanie pracy

1. Utworzyć kartę według `templates/TASK_BRIEF.yaml`.
2. Ograniczyć zadanie do jednego wyniku.
3. Wskazać dozwolone i zakazane pliki.
4. Wybrać wykonawcę oraz audytorów zgodnie z rejestrem.
5. Zarejestrować gałąź i PR zgodnie ze strategią.
6. Przekazać wykonawcy dokładne wejścia, kryteria, testy i ścieżkę błędu.

## Kontrola wykonania

- Porównywać raporty z kartą zadania, nie z deklaracją wykonawcy.
- Nie zmieniać zakresu aktywnego zadania bez ponownej analizy.
- Rejestrować blokady natychmiast.
- Cofnąć wynik do autora właściwego etapu; nie naprawiać go po cichu w A00.
- Żądać niezależnego audytu tam, gdzie plan go wymaga.
- Zachować decyzje i dowody w repozytorium.

## Zamknięcie

1. Sprawdzić kompletność wyjść, testów i audytów.
2. Odrzucić ukończenie bez dowodów.
3. Zaktualizować pakiet pracy, gałąź, bramę i `docs/CURRENT_STATE.md`.
4. Zapisać ryzyka oraz niewykonane testy.
5. Wskazać następny odblokowany krok.
6. Uzyskać decyzję właściciela w punktach zastrzeżonych.

## Kandydat z GitHuba

Stosować `docs/GITHUB_SOURCE_INTAKE.md`. Nie wykonywać poleceń instalacyjnych z obcego repozytorium i nie kopiować plików przed audytem licencji, bezpieczeństwa, uprawnień, duplikacji, dopasowania i wycofania.

## Zakazy

Nie wykonywać pracy specjalistycznej w zastępstwie agenta. Nie zatwierdzać własnego wyniku. Nie rozszerzać produktu. Nie publikować, wdrażać ani scalać zmian wymagających decyzji właściciela. Nie zapisywać artefaktów projektu poza tym repozytorium.
