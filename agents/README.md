# Agenci projektu

Status: plan 0.1 — definicje wykonawcze nie zostały jeszcze utworzone.

## Agent 0 — koordynator

Rejestruje zadania, kontroluje kompletność, statusy, kolejność etapów, raporty błędów i bramy zatwierdzenia. Nie tworzy samodzielnie treści ani nie publikuje.

## Agent 1 — analityk badań i architekt wiedzy

Czyta badanie, buduje mapę tematów, rozpoznaje luki i duplikaty, dzieli materiał na artykuły, przypisuje źródła i przygotowuje konspekty.

## Agent 2 — redaktor merytoryczny i internetowy

Przekształca zatwierdzone pakiety w czytelne artykuły. Nie dopisuje brakujących faktów. Przygotowuje metadane, linki i briefy dla grafik.

## Agent 3 — integrator PrestaShop

Waliduje pakiet publikacyjny, przygotowuje podgląd, integruje treść z modułem i wykonuje zatwierdzoną publikację. Nie zmienia znaczenia materiału.

## Agent 4 — projektant i programista interfejsu

Buduje system komponentów, strony kategorii, artykułu, wyszukiwarki i nawigacji. Nie jest uruchamiany dla każdej publikacji, jeżeli istniejące komponenty są wystarczające.

## Agent 5 — grafik interfejsu i treści

Tworzy lub dobiera legalne grafiki, ikony i miniatury. Prowadzi informacje o licencji i pochodzeniu. Współpracuje z redaktorem i projektantem interfejsu.

## Kontrola merytoryczna

Sprawdza zgodność ze źródłami, jednostki, bezpieczeństwo, sprzeczności i zakres pewności. Początkowo może być workflow kontrolnym; później osobnym agentem.

## Kontrola publikacyjna

Sprawdza kompletność, linki, grafiki, SEO, responsywność, dostępność i zgodność podglądu. Początkowo może być workflow kontrolnym; później osobnym agentem.

## Wymagania przyszłej definicji agenta

Każdy agent musi otrzymać:

- cel;
- zakres;
- zakazy;
- format wejściowy;
- format wyjściowy;
- dostępne narzędzia i skille;
- kroki działania;
- obsługę braków i błędów;
- kryteria akceptacji;
- testy;
- format raportu;
- zasady eskalacji do człowieka.

Nie należy tworzyć agenta, jeśli zadanie jest jednorazowe albo nie ma stabilnego kontraktu wejścia i wyjścia.
