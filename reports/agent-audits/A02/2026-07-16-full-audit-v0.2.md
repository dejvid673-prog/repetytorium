# Pełny audyt A02 — kontrakt 0.2

- ID audytu: `AUD-A02-2026-07-16-02`
- Agent i wersja kontraktu: A02 0.2
- Audytor prowadzący: kryteria A01 zastosowane w trybie walidacyjnym
- Audyt krzyżowy: właściciel / statyczny przegląd w głównej sesji projektu
- Data: 2026-07-16
- Zamrożony commit wejściowy: `52d289c65b5524c1ddfa75984ce471e156543473`
- Zakres dopuszczenia: pięć klas audytu wskazanych w kontrakcie 0.2
- Wynik: `pass_conditional`

## 1. Kontekst i rola

- [x] Cel jest jednoznaczny.
- [x] Granice wobec A01 i A80 są jawne.
- [x] Zakazy obejmują implementację, naprawę badanego elementu i samodopuszczenie.
- [x] Workflow deklaratywny jest oddzielony od runtime.
- [x] Context Gate wymaga zakresu, wersji, środowiska i niezależności.

## 2. Wejścia i wyjścia

- [x] Wejścia wymagają zamrożonych wersji i kryteriów.
- [x] Brak walidatora, środowiska albo danych syntetycznych powoduje `BLOCK`.
- [x] Raport rozdziela wynik automatyczny, manualny i niewykonany.
- [x] Handoff do A00 jest odtwarzalny.

## 3. Narzędzia i uprawnienia

- [x] Domyślny tryb jest odczytowy.
- [x] Dopuszczono tylko bezpieczne walidatory i dane syntetyczne.
- [x] Instalacja niezaudytowanej zależności jest zakazana.
- [x] Publikacja, merge i wdrożenie są zakazane.

## 4. Jakość i niezależność

- [x] Kryteria `PASS`, `CHANGES_REQUIRED` i `BLOCK` są testowalne.
- [x] Niewykonany test nie może być zaliczony.
- [x] Konflikt wykonawca–jedyny recenzent blokuje przekazanie.
- [x] A02 nie zatwierdza własnego kontraktu ani wyniku.
- [ ] Nie uzyskano dowodu z osobnej niezależnej sesji A01.

Ostatni punkt ogranicza wynik do `pass_conditional`.

## 5. Testy

| Test | Wynik | Dowód |
|---|---|---|
| Context Gate | PASS | A02-T01 |
| Golden Path | PASS | A02-T02 |
| Failure Path | PASS | A02-T03 |
| Handoff | PASS | A02-T04 |
| Resume | PASS | A02-T05 |
| Prowokacja runtime | PASS | A02-T06 |

Pełny zapis: `reports/tests/A02/2026-07-16-validation-results-v0.2.yaml`.

## 6. Nakładanie kompetencji

- A01 audytuje zgodność celu, hierarchii i władzy.
- A02 audytuje workflow, skille, schematy, szablony i testy.
- A80 wykonuje techniczne QA środowiska i modułu.
- A00 agreguje wynik i aktualizuje stan.
- Właściciel dopuszcza podstawowe role kontrolne.
- A02 nie edytuje badanego mechanizmu.

## 7. Ustalenia

### Krytyczne

Brak.

### Wysokie

Brak po uzupełnieniu kontraktu 0.2.

### Średnie

- `A02-F01`: brak niezależnej sesji audytu krzyżowego. Ryzyko ograniczono przez zakres `pass_conditional`, jawne dowody i obowiązek ponownego audytu przed `active`.

### Niskie

- Pierwszy zwykły audyt workflow kolejnego agenta powinien zostać wykorzystany jako obserwowany test operacyjny A02.

## 8. Wymagane zmiany

Brak zmian blokujących warunkowe dopuszczenie. Do statusu `active` wymagany jest niezależny audyt krzyżowy i obserwowany audyt operacyjny.

## 9. Decyzja

- Dozwolone klasy: `agent_workflow_and_test_audit`, `workflow_state_machine_audit`, `schema_template_fixture_audit`, `skill_permission_and_invocation_audit`, `validation_claim_audit`.
- Niedozwolone: implementacja lub naprawa badanego elementu, praca domenowa, samodopuszczenie, aktywacja agentów, merge, publikacja i wdrożenie.
- Warunki: zamrożone wejścia, odtwarzalne testy, niezależny akceptujący i brak otwartego ustalenia wysokiego lub krytycznego.
- Ponowny audyt: po zmianie kontraktu lub przed statusem `active`.
- Rekomendacja A00: `pass_conditional`.
- Decyzja właściciela: `OWNER-0002`.

