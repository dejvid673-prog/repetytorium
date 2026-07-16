# Mapa repozytorium

Status: planowana struktura 0.1

```text
repetytorium/
├── README.md
├── AGENTS.md
├── docs/
│   ├── PROJECT_CHARTER.md
│   ├── ARCHITECTURE.md
│   ├── CONTENT_WORKFLOW.md
│   ├── CONTENT_MODEL.md
│   ├── REPOSITORY_MAP.md
│   └── decisions/
├── research/
│   ├── inbox/
│   ├── accepted/
│   ├── processing/
│   ├── completed/
│   └── rejected/
├── knowledge/
│   ├── topics/
│   ├── sources/
│   ├── terminology/
│   └── relationships/
├── articles/
│   ├── drafts/
│   ├── review/
│   ├── approved/
│   ├── published/
│   └── archived/
├── assets/
│   ├── icons/
│   ├── thumbnails/
│   ├── illustrations/
│   ├── photographs/
│   └── licenses/
├── agents/
├── workflows/
├── schemas/
├── module/
│   └── stawexpertknowledge/
└── tests/
```

## Zasady użycia

- Puste katalogi nie są tworzone wyłącznie „na zapas”; powstają z plikiem README albo pierwszym rzeczywistym artefaktem.
- Surowe badania pozostają niezmienione. Poprawki i materiały pochodne trafiają do kolejnych warstw.
- Artykuły nie przechowują binarnych grafik w swoich katalogach; odwołują się do kontrolowanych zasobów.
- Pliki schematów walidują dane przekazywane między etapami.
- Kod modułu nie może zawierać produkcyjnych sekretów.
- Trwałe zmiany architektoniczne wymagają ADR.
