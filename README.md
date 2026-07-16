# Repetytorium Staw Expert

Kompletne źródło prawdy dla publicznej biblioteki wiedzy o przydomowych oczkach wodnych, hobbystycznych stawach, jakości wody i rybach słodkowodnych. Biblioteka będzie dodatkiem do sklepu Staw Expert na PrestaShop 9, ale nie reklamuje ani nie rekomenduje produktów.

## Aktualny stan

**Faza 0 — Ład projektu. Wersja kontekstu 0.3.**

A00 0.4 został warunkowo dopuszczony decyzją właściciela po 15 testach zachowania i pozytywnej walidacji GitHub Actions. G0A ma status PASSED. Następny krok to pełne dopuszczenie A01 i A02 do zwykłych audytów; pozostałe role oraz fazy wykonawcze są zablokowane.

## Obowiązkowy start

1. [Manifest kontekstu](PROJECT_CONTEXT.yaml)
2. [Nadrzędna instrukcja](PROJECT_INSTRUCTIONS.md)
3. [Konstytucja](docs/PROJECT_CONSTITUTION.md)
4. [Plan główny](docs/MASTER_PLAN.md)
5. [Konkretny plan realizacji](docs/IMPLEMENTATION_PLAN.md)
6. [Wykonawczy plan faz i zależności](docs/PHASE_EXECUTION_PLAN.md)
7. [Plan pierwszego agenta A00](docs/PHASE_00_COORDINATOR_PLAN.md)
8. [Aktualny stan](docs/CURRENT_STATE.md)
9. [Strategia gałęzi](docs/BRANCHING_STRATEGY.md)
10. [Plan audytu agentów](docs/AGENT_AUDIT_PLAN.md)
11. [Instrukcje agentów](AGENTS.md)
12. [System agentów](docs/AGENT_SYSTEM.md)
13. [Rejestry](registries/README.md)
14. [Pozyskiwanie z GitHuba](docs/GITHUB_SOURCE_INTAKE.md)
15. [Decyzje](docs/decisions/README.md)

## Model zarządzania

Właściciel kieruje polecenia do A00 — Koordynatora i Kierownika Projektu. Po pozytywnym audycie A00 będzie kontrolował zakres, plan i zależności, a następnie przekazywał zadania wyspecjalizowanym agentom. Każdy agent ma osobny kontrakt w `agents/<id>/AGENT.md`.

## Zakres

W projekcie:

- publiczne artykuły po polsku;
- oczka przydomowe i stawy hobbystyczne;
- woda, ekologia, technika, rośliny i sezonowość;
- ryby polskich wód, ryby ozdobne i gatunki interesujące pasjonatów;
- jawne źródła, statusy weryfikacji i historia korekt;
- kontakt oraz materiały czytelników przez e-mail;
- przyszła moderowana biblioteka przypadków;
- WCAG 2.2 AA;
- wyszukiwarka i analityka zgodna z prywatnością.

Poza projektem:

- reklamy i rekomendacje produktów;
- hodowla przemysłowa;
- automatyczna diagnoza i tryb ratunkowy;
- kalkulatory;
- profil zbiornika i dziennik pomiarów;
- forum w pierwszych etapach;
- wysyłanie zdjęć bezpośrednio przez stronę.

## Źródło prawdy

Wszystkie artefakty projektu powstają wyłącznie tutaj. Inne repozytoria mogą być czytane referencyjnie, lecz przeniesienie elementu wymaga audytu duplikatów, licencji, bezpieczeństwa i zgodności.

## Plan

Realizacja przebiega przez fazy, etapy i formalne bramy. Po G0 równolegle mogą ruszyć fundament wiedzy 1K i środowisko techniczne 1T; dalsze gałęzie pozostają zablokowane do spełnienia swoich zależności. Plan strategiczny: [MASTER_PLAN.md](docs/MASTER_PLAN.md). Plan wykonawczy: [PHASE_EXECUTION_PLAN.md](docs/PHASE_EXECUTION_PLAN.md).
