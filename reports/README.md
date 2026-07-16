# Raporty

Raporty agentów i audytów trafiają do katalogów powiązanych z zadaniami albo wydaniami. Raport nie zastępuje zmian w dokumentacji nadrzędnej.

Minimalna zawartość:

- ID zadania;
- agent;
- wersja kontekstu;
- zakres;
- wejścia;
- zmienione pliki;
- testy;
- wyniki;
- niewykonane testy;
- ryzyka;
- kryteria akceptacji;
- następny krok.

## Ustalone lokalizacje

- audyty agentów: `reports/agent-audits/<agent-id>/<audit-id>.md`;
- raporty bram: `reports/phase-gates/<gate-id>/<date>.md`;
- raporty zadań: `reports/tasks/<task-id>.md`;
- raporty wydań: `reports/releases/<version>.md`.

Wzorce znajdują się w `templates/AGENT_AUDIT_REPORT.md` i `templates/PHASE_GATE_REPORT.md`.
