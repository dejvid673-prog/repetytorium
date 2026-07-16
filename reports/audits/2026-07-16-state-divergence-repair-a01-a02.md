# Naprawa STATE_DIVERGENCE przed dopuszczeniem A01 i A02

Data: 2026-07-16  
Zakres: draft PR #1, gałąź `agent/repository-foundation`  
Wynik: naprawiono w atomowym zestawie dopuszczenia A01/A02

## Wykryte rozbieżności

1. Kontrakt A00 miał wersję 0.4, a `registries/agents.yaml` wskazywał 0.3.
2. `docs/CURRENT_STATE.md` i opis PR wskazywały zakończenie WP-0001–WP-0007, ale WP-0001–WP-0005 miały status `REVIEW`.
3. `registries/decisions.yaml` był kanonicznym rejestrem bez `state_revision`, mimo że opis PR deklarował rewizjonowanie wszystkich źródeł kanonicznych.
4. A01 miał status planowany w kontrakcie, lecz rejestr zachowywał wygasłe `pass_conditional` bootstrap.

## Naprawa

- zsynchronizowano wersję A00 do 0.4;
- ustawiono WP-0001–WP-0007 na `COMPLETED` zgodnie z dowodami G0A i OWNER-0001;
- dodano rewizję rejestru decyzji;
- zastąpiono wygasły zakres bootstrap kontraktami A01/A02 0.2 i nową decyzją OWNER-0002;
- wzmocniono walidator o kontrole wersji, zakresów dopuszczenia, testów, raportów i zamkniętych pakietów.

## Ograniczenia

Naprawa nie zamyka G0B ani G0, nie aktywuje następnej fali agentów i nie zmienia statusu draft PR #1.

