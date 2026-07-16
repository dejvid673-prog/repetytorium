# Audyt bootstrap A02

- Agent: A02 — Audytor Workflow, Skilli i Schematów
- Kontrakt: 0.1
- Data: 2026-07-16
- Tryb: bootstrap
- Wynik: `pass_conditional`
- Dozwolona klasa: `bootstrap_audit`

## Zakres kontroli

Sprawdzono cel, rozdzielenie od A80, wejścia, wyjścia, zakazy, ścieżki błędu i kryteria dowodów. A02 może oceniać workflow, skille, schematy i testy A00. Nie może naprawiać badanego elementu w zadaniu audytowym, sterować agentami ani wykonywać technicznego QA PrestaShop.

## Ustalenia

- krytyczne: brak;
- wysokie: brak;
- średnie: przed pełną aktywacją potrzebny osobny Handoff z A01 oraz test wykrycia konfliktu wykonawca–recenzent;
- ograniczenie: przegląd wykonano w głównej sesji projektu, nie w osobnej sesji niezależnego agenta.

## Decyzja

Warunkowe dopuszczenie obejmuje wyłącznie `bootstrap_audit`. Wygasa po zmianie kontraktu albo zakończeniu bootstrapu.
