# Macierz audytu agentów

Status: plan wykonania Fazy 0C  
Zasada: audytor nie zatwierdza własnego kontraktu ani własnego wyniku.

## Bootstrap

Przed aktywacją A00 stosuje się `docs/BOOTSTRAP_GOVERNANCE.md`.

| Badany element | Audyt kontekstu | Audyt wykonalności | Decyzja |
|---|---|---|---|
| A01 | właściciel / przegląd statyczny | A02 po ograniczonym dopuszczeniu | właściciel |
| A02 | A01 po ograniczonym dopuszczeniu | właściciel / przegląd statyczny | właściciel |
| A00, skill, workflow, schema i testy | A01 | A02 | właściciel |

A80 nie audytuje A00. Pozostaje niezależnym technicznym QA środowiska i modułu.

## Fale audytu

| Fala | Role | Cel |
|---|---|---|
| W0 | A01, A02, A00 | bezpieczne sterowanie, kontekst i wykonywalny workflow |
| W1 | A11, A40, A41, A80 | wiedza, dowody, bezpieczeństwo i techniczne QA |
| W2 | A10, A20–A24, A30–A32 | badania i redakcja |
| W3 | A50, A51, A60, A61, A81 | UX, makiety, grafika i dostępność |
| W4 | A70–A72, A82 | PrestaShop, publikacja, SEO i wyszukiwanie |
| W5 | A85 | analityka i prywatność |
| W6 | A90, A95 | utrzymanie, korekty i przyszłe przypadki |

## Przydział audytów

| Agent | Audyt konstrukcji | Audyty krzyżowe | Decyzja dopuszczenia |
|---|---|---|---|
| A00 | A01 | A02; właściciel | właściciel |
| A01 | właściciel | A02 | właściciel |
| A02 | A01 | właściciel | właściciel |
| A10 | A01 | A40, A41 | A00 |
| A11 | A01 | A40, A82 | właściciel dla pierwszego dopuszczenia |
| A20–A23 | A01 | A40, A41 | A00 |
| A24 | A01 | A40, A41 | A00 |
| A30–A32 | A01 | A40, A41, A82 według ryzyka | A00 |
| A40 | A01 | A41, A02 | właściciel dla pierwszego dopuszczenia |
| A41 | A01 | A24, A02 | właściciel dla pierwszego dopuszczenia |
| A50–A51 | A01 | A81, A82, A02 | A00 |
| A60 | A01 | A61, A81 | A00 |
| A61 | A01 | A24, A02 | właściciel dla pierwszego dopuszczenia |
| A70–A72 | A01 | A80, A41, A82 | A00 |
| A80 | A01 | A70, A02 | właściciel dla pierwszego dopuszczenia |
| A81 | A01 | A50, A80 | właściciel dla pierwszego dopuszczenia |
| A82 | A01 | A11, A50, A80 | właściciel dla pierwszego dopuszczenia |
| A85 | A01 | A24, A41, A80 | A00 |
| A90 | A01 | A40, A41, A82 | A00 |
| A95 | A01 | A24, A41, A90 | A00 |

## Kolejność w fali

1. A00 tworzy kartę audytu; w bootstrapie robi to właściciel.
2. Zamraża się wersję kontraktu.
3. Audytor konstrukcji analizuje kompletność i konflikty.
4. Audytorzy krzyżowi oceniają własne obszary.
5. Agent przechodzi Context Gate, Golden Path, Failure Path i Handoff.
6. Jeden raport rozdziela wyniki automatyczne, oceny i ograniczenia.
7. Poprawki wykonuje autor na osobnym zadaniu.
8. Audytorzy sprawdzają poprawki.
9. Uprawniony decydent nadaje status i dokładny zakres.
10. Rejestr otrzymuje datę, raport oraz wersję audytu.

## Kryterium zakończenia

Fala jest zakończona, gdy potrzebne role mają ważny raport, nie ma otwartego ustalenia krytycznego, Handoff przeszedł, a rejestr wskazuje dokładny zakres dopuszczenia.
