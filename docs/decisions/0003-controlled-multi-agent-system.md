# ADR-0003: Kontrolowany system wielu agentów

Status: accepted  
Data: 2026-07-16

## Decyzja

Projekt wykorzystuje większą liczbę wąsko wyspecjalizowanych agentów. Wszystkie polecenia właściciela przechodzą przez Kierownika Projektu A00. Każdy agent posiada osobny kontrakt i obowiązkowy Context Gate.

## Konsekwencje

- zmniejsza się konflikt odpowiedzialności;
- rośnie liczba przekazań, dlatego wymagane są schematy i raporty;
- agent nie rozszerza samodzielnie planu;
- nowe role można dodawać kontrolowaną zmianą bez renumerowania istniejących.
