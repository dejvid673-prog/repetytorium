# Macierz audytu agentów

Status: plan wykonania Etapów 0.4–0.7  
Zasada: audytor nie zatwierdza własnego kontraktu ani własnego wyniku.

## Fale audytu

| Fala | Role | Cel |
|---|---|---|
| W0 | A00, A01 | bezpieczne sterowanie projektem i kontrola kontekstu |
| W1 | A11, A40, A41, A80 | fundament wiedzy, dowodów, bezpieczeństwa i wykonalności |
| W2 | A10, A20–A24, A30–A32 | pełny łańcuch badań i redakcji |
| W3 | A50, A51, A60, A61, A81 | UX, makiety, grafika i dostępność |
| W4 | A70–A72, A82 | PrestaShop, import, publikacja, SEO i wyszukiwanie |
| W5 | A85 | analityka, prywatność i retencja |
| W6 | A90, A95 | utrzymanie, korekty i przyszłe przypadki |

Następna fala nie wymaga zakończenia wszystkich przyszłych fal. Wymaga jednak aktywnych ról kontrolnych i kontraktów, z których korzysta.

## Przydział audytów

| Agent | Obszar | Audyt konstrukcji | Audyty krzyżowe | Decyzja dopuszczenia |
|---|---|---|---|---|
| A00 | kierowanie projektem | A01 | A80; właściciel | właściciel |
| A01 | kontekst i ład | A00 | A80; właściciel | właściciel |
| A10 | przyjęcie badań | A01 | A40, A41 | A00 |
| A11 | taksonomia i wiedza | A01 | A40, A82 | A00 |
| A20 | chemia wody | A01 | A40, A41 | A00 |
| A21 | ekologia i technika | A01 | A40, A41 | A00 |
| A22 | gatunki ryb | A01 | A40, A41 | A00 |
| A23 | zdrowie ryb | A01 | A40, A41 | A00 |
| A24 | prawo i regulacje | A01 | A40, A41 | A00 |
| A30 | portfel artykułów | A01 | A40, A82 | A00 |
| A31 | redakcja treści | A01 | A40, A41, A82 | A00 |
| A32 | prezentacja treści | A01 | A40, A81, A82 | A00 |
| A40 | dowody i źródła | A01 | A41, A80; właściciel przy sporze | A00 |
| A41 | bezpieczeństwo i zgodność | A01 | A24, A80; właściciel przy sporze | A00 |
| A50 | informacja i UX | A01 | A81, A82 | A00 |
| A51 | makiety i UI | A01 | A50, A81, A80 | A00 |
| A60 | zasoby wizualne | A01 | A61, A81 | A00 |
| A61 | prawa grafik | A01 | A24, A80; właściciel przy sporze | A00 |
| A70 | architektura PrestaShop | A01 | A80, A41, A82 | A00 |
| A71 | implementacja PrestaShop | A01 | A70, A80, A41 | A00 |
| A72 | import i publikacja | A01 | A70, A80, A41, A82 | A00 |
| A80 | techniczne QA | A01 | A70; właściciel przy sporze | A00 |
| A81 | dostępność | A01 | A50, A80; właściciel przy sporze | A00 |
| A82 | SEO i wyszukiwarka | A01 | A11, A50, A80 | A00 |
| A85 | analityka | A01 | A24, A41, A80 | A00 |
| A90 | aktualność i korekty | A01 | A40, A41, A82 | A00 |
| A95 | przypadki czytelników | A01 | A24, A41, A90 | A00 |

„Audyt konstrukcji” sprawdza kontrakt i granice roli. „Audyty krzyżowe” sprawdzają wymagania domenowe. Konsultacja nie daje konsultantowi prawa do cichej edycji kontraktu.

## Kolejność w każdej fali

1. A00 tworzy kartę audytu i zamraża wersję kontraktu.
2. Audytor konstrukcji analizuje kompletność i konflikty.
3. Audytorzy krzyżowi sprawdzają ryzyka swoich obszarów.
4. Agent przechodzi Context Gate, Golden Path, Failure Path i Handoff.
5. Ustalenia trafiają do jednego raportu.
6. Kontrakt jest poprawiany na osobnej gałęzi, jeśli to konieczne.
7. Audytorzy sprawdzają poprawki.
8. A00 albo właściciel nadaje status i zakres dopuszczenia.
9. Rejestr agentów otrzymuje datę, raport i wersję audytu.

## Obowiązkowe pary graniczne

Szczególnie dokładnie testujemy przekazania:

- A10 → A20–A24;
- A20–A24 → A30;
- A30 → A31 → A32;
- A32 → A40/A41;
- A11/A30 → A50;
- A50 → A51 ↔ A60;
- A51 → A70/A71;
- A31/A32 → A72;
- A70 → A71 → A80;
- A72 → A82/A80;
- A90 → A40/A41;
- A95 → A90/A41.

## Kryterium zakończenia fali

Fala jest zakończona, gdy wszystkie role potrzebne następnemu etapowi mają ważny raport, nie ma otwartego ustalenia krytycznego, test Handoff przeszedł, a rejestr wskazuje dokładny zakres dopuszczenia.
