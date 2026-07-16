# Instrukcje dla wszystkich agentów i narzędzi

Ten plik obowiązuje w całym repozytorium.

## Obowiązkowy kontekst

Przed pracą agent musi przeczytać:

1. `PROJECT_INSTRUCTIONS.md`;
2. `docs/PROJECT_CONSTITUTION.md`;
3. `docs/MASTER_PLAN.md` i `docs/PHASE_EXECUTION_PLAN.md`;
4. `docs/CURRENT_STATE.md`;
5. `docs/BRANCHING_STRATEGY.md` i `docs/DEPENDENCY_MANAGEMENT.md`;
6. ten plik;
7. właściwe ADR;
8. własny `agents/<id>/AGENT.md` i wpis w `registries/agents.yaml`;
9. instrukcje katalogów objętych zadaniem;
10. manifest gałęzi i prompt zadania od A00.

Następnie przechodzi Project Context Gate z `docs/AGENT_SYSTEM.md`. Sam kontrakt nie daje uprawnienia do działania. Agent musi mieć dopuszczenie zgodne z `docs/AGENT_AUDIT_PLAN.md`, a zadanie status `READY`. Bez obu warunków nie rozpoczyna pracy.

## Kierowanie pracą

Wszystkie polecenia właściciela przechodzą przez A00. Pozostali agenci:

- nie negocjują samodzielnie zakresu z właścicielem;
- nie zmieniają planu;
- nie przejmują innych ról;
- raportują wynik do A00;
- zatrzymują się przy konflikcie albo braku danych.

## Źródło prawdy

Wszystkie artefakty projektu tworzy się w tym repozytorium. Inne repozytoria wolno czytać referencyjnie. Przeniesienie wymaga kontroli duplikatu, licencji, aktualności, bezpieczeństwa i zależności.

## Zakres treści

Repetytorium dotyczy przydomowych oczek, stawów hobbystycznych, wody, ryb, roślin i techniki. Nie obejmuje hodowli produkcyjnej, reklam produktów, kalkulatorów, automatycznej diagnozy ani profilu użytkownika.

## Źródła i prawdziwość

Priorytet:

1. prawo, normy i urzędy;
2. publikacje naukowe;
3. SDS, CLP i dokumentacja producenta;
4. oficjalna dokumentacja techniczna;
5. wiarygodne źródła branżowe;
6. blogi i fora pomocniczo.

Nie wolno:

- wymyślać faktów, źródeł i cytatów;
- ukrywać sprzeczności;
- przedstawiać hipotezy jako faktu;
- diagnozować na podstawie jednego objawu;
- podawać niebezpiecznych zaleceń bez oceny warunków;
- podporządkowywać treści sprzedaży.

## Kontrola niezależna

Materiały wysokiego ryzyka przechodzą A40 i A41. Autor nie jest jedynym recenzentem. Weryfikacja redakcyjna nie jest tym samym co weryfikacja merytoryczna.

## Grafiki

Każdy zasób posiada pochodzenie, licencję, zakres użycia i tekst alternatywny. Wynik wyszukiwarki nie jest licencją. Emoji nie są systemem ikon.

## PrestaShop

- PrestaShop 9;
- bez zmian core;
- własny moduł i tabele;
- kontrola uprawnień, CSRF, XSS, SQL injection i walidacji;
- publiczne czytanie bez konta;
- widoczność niezależna od weryfikacji;
- historia i rollback;
- brak relacji produktowych.

## Git i zmiany

- gałąź utworzona zgodnie z `docs/BRANCHING_STRATEGY.md`;
- wpis w `registries/branches.yaml` i manifest gałęzi;
- sprawdzone zależności i bramy;
- minimalny zakres;
- brak nadpisywania cudzych zmian;
- decyzje architektoniczne jako ADR;
- zmiana planu przez wniosek analizowany przez A00;
- aktualizacja rejestrów i `CURRENT_STATE.md` po zmianie stanu.

## Raport

Raport zawiera wejścia, zmienione pliki, testy, wyniki, niewykonane testy, ryzyka, kryteria akceptacji i następny krok. Nie wolno deklarować testu, publikacji ani wdrożenia bez dowodu.

## Sekrety i dane

Nie zapisywać haseł, tokenów, kluczy API, danych klientów, zamówień ani prywatnych danych zgłaszających. Materiały e-mail i zdjęcia wymagają zgody, ochrony oraz anonimizacji przed publikacją.
