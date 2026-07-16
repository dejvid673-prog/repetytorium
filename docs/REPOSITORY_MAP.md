# Mapa repozytorium

Status: struktura 0.2

```text
repetytorium/
├── README.md
├── PROJECT_INSTRUCTIONS.md
├── PROJECT_PROFILE.yaml
├── AGENTS.md
├── docs/
│   ├── PROJECT_CONSTITUTION.md
│   ├── MASTER_PLAN.md
│   ├── CURRENT_STATE.md
│   ├── ROADMAP.md
│   ├── GLOSSARY.md
│   ├── AGENT_SYSTEM.md
│   └── decisions/
├── registries/
├── agents/
├── skills/
├── workflows/
├── reports/
├── research/
├── knowledge/
├── articles/
├── assets/
├── design/
├── schemas/
├── module/
├── analytics/
├── community/
└── tests/
```

## Lokalizacja odpowiedzialności

- plan i zasady: root oraz `docs/`;
- kanoniczne wykazy: `registries/`;
- role: `agents/`;
- procedury wielokrotnego użytku: `skills/`;
- przekazania: `workflows/`;
- dowody pracy: `reports/`;
- surowe badania: `research/`;
- model pojęć i twierdzeń: `knowledge/`;
- treści: `articles/`;
- grafiki i licencje: `assets/`;
- makiety i komponenty: `design/`;
- kontrakty danych: `schemas/`;
- kod PrestaShop: `module/`;
- pomiar użycia: `analytics/`;
- materiały współpracy czytelników: `community/`.

Surowych badań nie nadpisuje się. Trwałe decyzje wymagają ADR. Pusty katalog powstaje dopiero z instrukcją albo rzeczywistym artefaktem.
