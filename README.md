# Repetytorium Staw Expert

Kompletne źródło prawdy dla publicznej biblioteki wiedzy o przydomowych oczkach wodnych, hobbystycznych stawach, jakości wody i rybach słodkowodnych. Biblioteka będzie dodatkiem do sklepu Staw Expert na PrestaShop 9, ale nie reklamuje ani nie rekomenduje produktów.

## Aktualny stan

**Faza 0 — Ład projektu. Wersja kontekstu 0.2.**

Plan zależności, gałęzi i bram jest przygotowany. Wszystkie 27 kontraktów agentów oczekuje na audyt; żaden agent nie ma jeszcze statusu `active`. Nie ma działającego modułu, gotowych artykułów ani wdrożenia.

## Obowiązkowy start

1. [Nadrzędna instrukcja](PROJECT_INSTRUCTIONS.md)
2. [Konstytucja](docs/PROJECT_CONSTITUTION.md)
3. [Plan główny](docs/MASTER_PLAN.md)
4. [Wykonawczy plan faz i zależności](docs/PHASE_EXECUTION_PLAN.md)
5. [Aktualny stan](docs/CURRENT_STATE.md)
6. [Strategia gałęzi](docs/BRANCHING_STRATEGY.md)
7. [Plan audytu agentów](docs/AGENT_AUDIT_PLAN.md)
8. [Instrukcje agentów](AGENTS.md)
9. [System agentów](docs/AGENT_SYSTEM.md)
10. [Rejestr agentów](registries/agents.yaml), [gałęzi](registries/branches.yaml) i [bram](registries/phase-gates.yaml)
11. [Decyzje](docs/decisions/README.md)

## Model zarządzania

Właściciel kieruje polecenia do A00 — Kierownika Projektu. A00 kontroluje zakres, plan i zależności, a następnie przekazuje zadania wyspecjalizowanym agentom. Każdy agent ma osobny kontrakt w `agents/<id>/AGENT.md`.

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
