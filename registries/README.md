# Rejestry

Rejestry są kanonicznymi wykazami elementów projektu. Przed utworzeniem agenta, skilla, workflow, schematu, typu artykułu albo komponentu należy sprawdzić właściwy rejestr.

Każdy wpis posiada co najmniej ID, nazwę, ścieżkę, wersję i status. Rejestr aktualizuje się w tym samym zadaniu co element.

## Rejestry startowe

- `agents.yaml` — role, kontrakty i statusy audytów;
- `branches.yaml` — gałęzie, zależności, blokady i PR-y;
- `phase-gates.yaml` — warunki przejścia między fazami.

Status zmienia się tylko razem z dowodem. Deklaracja agenta nie zastępuje decyzji A00 ani raportu bramy.
