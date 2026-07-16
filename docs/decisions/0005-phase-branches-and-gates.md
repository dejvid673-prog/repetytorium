# ADR-0005: Gałęzie integracyjne faz i formalne bramy

Status: proponowana do zatwierdzenia  
Data: 2026-07-16

## Kontekst

Projekt ma wiele wyspecjalizowanych ról i zależności. Niektóre prace mogą działać równolegle, lecz kod, UX i treść potrzebują wcześniej zatwierdzonych kontraktów albo środowisk. Jedna długa gałąź lub bezpośrednie PR-y wszystkich agentów do `main` utrudniłyby kontrolę zgodności.

## Decyzja

- `main` przyjmuje wyłącznie zatwierdzone rezultaty faz i wydania;
- każda faza lub niezależny tor ma gałąź `phase/*`;
- zadania agentów trafiają przez małe gałęzie do właściwej gałęzi fazy;
- rozpoczęcie zadania wymaga statusu `READY`;
- zakończenie fazy wymaga raportu bramy i wymaganych audytów;
- prace zależne pozostają `BLOCKED`, nawet jeśli wykonawca jest dostępny;
- Faza 1K i 1T mogą działać równolegle po G0;
- scalanie PR fazy do `main` wymaga decyzji A00 oraz właściciela w punktach wskazanych planem.

## Skutki

Korzyści:

- zależności są widoczne;
- można bezpiecznie równoleglić pracę;
- `main` pozostaje stabilny;
- audyty odbywają się przed integracją;
- łatwiej wskazać dokładny powód blokady.

Koszty:

- więcej rejestrów i PR-ów;
- konieczna regularna aktualizacja statusów;
- możliwe konflikty integracyjne na gałęziach faz;
- A00 musi aktywnie zarządzać kolejnością.

## Alternatywy odrzucone

- jedna długowieczna gałąź `develop` dla całego projektu;
- bezpośrednie gałęzie wszystkich agentów do `main`;
- uruchamianie faz wyłącznie według numeru bez testu zależności;
- aktywowanie wszystkich agentów przed audytem.
