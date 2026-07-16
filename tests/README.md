# Testy

Katalog obejmuje testy dokumentacji, schematów, agentów, workflow, modułu, interfejsu, dostępności, SEO, bezpieczeństwa i migracji.

Każdy test wskazuje środowisko, dane wejściowe, oczekiwany wynik i rzeczywisty wynik. Test niewykonany nie jest testem zaliczonym. Wynik manualny, automatyczny i deklaratywny muszą być rozróżnione.

## Testy agentów

- `tests/agents/A00/` — 15 scenariuszy sterowania projektem;
- `tests/agents/A01/` — 6 scenariuszy kontekstu, ładu i przekazania;
- `tests/agents/A02/` — 6 scenariuszy workflow, schematów, wznowienia i twierdzeń o runtime.

Plik `cases.yaml` definiuje oczekiwane zachowania, a `TEST_PLAN.md` procedurę i minimalny wynik. Rzeczywiste wyniki znajdują się w `reports/tests/<agent-id>/`.

