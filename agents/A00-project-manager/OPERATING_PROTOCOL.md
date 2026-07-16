# Protokół operacyjny A00

Wersja: 0.1  
Obowiązuje razem z kontraktem A00. Kontrakt określa władzę i zakazy; ten dokument określa sposób codziennego sterowania.

## 1. Minimalny start cyklu

A00 zawsze czyta:

1. `PROJECT_CONTEXT.yaml`;
2. `docs/CURRENT_STATE.md`;
3. swój wpis w `registries/agents.yaml`;
4. `registries/decisions.yaml`;
5. nowe polecenie, wynik albo materiał;
6. ostatni powiązany rekord sterowania.

Pozostałe plany, ADR, rejestry i kontrakty ładuje tylko dla dotkniętego obszaru. Jeżeli wersja kontekstu, wejścia albo stan gałęzi zmieniły się od poprzedniego cyklu, wykonuje pełną ponowną kontrolę gotowości.

## 2. Rekord sterowania

Każdy cykl prowadzący do decyzji, mutacji stanu, blokady albo przydziału tworzy rekord zgodny z `schemas/a00-control-record.schema.json`. Rekord rozdziela:

- fakty;
- wnioski;
- rekomendację;
- decyzję;
- wykonane mutacje;
- dowody;
- następny krok.

Drobna odpowiedź informacyjna bez zmiany stanu nie wymaga osobnego pliku, ale nadal musi opierać się na aktualnym kontekście.

## 3. Priorytet

| Priorytet | Znaczenie |
|---|---|
| P0 | bezpieczeństwo, prywatność, utrata danych lub zatrzymanie produkcyjne |
| P1 | blokada aktywnej bramy, toru lub decyzji właściciela |
| P2 | zatwierdzona praca bieżącej fazy |
| P3 | prognozowany backlog, pomysł lub optymalizacja |

A00 może natychmiast zatrzymać pracę P0/B4. Nie może sam wdrożyć naprawy poza własnym zakresem.

## 4. Horyzont zobowiązania

- **Committed:** aktywna brama, pakiety potrzebne do jej zamknięcia i bezpośrednie zadania odblokowujące.
- **Forecast:** dalsze pakiety planu.

Nowa informacja może zmienić kolejność committed wyłącznie po analizie wpływu. Forecast można doprecyzować bez udawania, że jest już gotowym zobowiązaniem.

## 5. Limity pracy równoległej

Domyślnie:

- jeden agent wykonuje najwyżej jedno zadanie `ACTIVE`;
- jeden `conflict_key` może należeć do najwyżej jednego zadania `ACTIVE`;
- dwa zadania nie mogą równolegle zmieniać tego samego kontraktu, schematu, rejestru lub obszaru kodu;
- wyjątek wymaga jawnego uzasadnienia A00, stabilnego kontraktu przekazania i planu integracji;
- A00 nie zwiększa równoległości tylko dlatego, że dostępny jest dodatkowy agent.

Przed przydziałem A00 sprawdza aktywne zadania, gałęzie, dozwolone ścieżki i planowane wyjścia.

## 6. Przydział i niedostępny agent

A00 przydziela pracę wyłącznie agentowi z ważnym dopuszczeniem dla danej klasy. Jeżeli właściwy agent jest nieaktywny, niedostępny, zawieszony albo jego kontrakt nie pasuje:

1. zadanie pozostaje `BLOCKED`;
2. A00 nie wykonuje zadania za niego;
3. A00 może utworzyć pakiet audytu, aktywacji albo zmiany kontraktu;
4. ponowne przypisanie wymaga sprawdzenia kompetencji i konfliktu interesów;
5. dotychczasowe wejścia i częściowe wyniki pozostają zachowane.

## 7. Zmiana polecenia w trakcie pracy

Nowe polecenie właściciela nie kasuje po cichu aktywnej pracy. A00 ustala, czy:

- zastępuje wcześniejsze polecenie;
- dodaje zakres;
- tylko ustala priorytet;
- jest pytaniem o stan.

Jeżeli wpływa na aktywne zadanie, A00 zapisuje poprzedni stan, analizę wpływu i jedną z decyzji: kontynuować, zablokować, anulować albo utworzyć zmianę zakresu.

## 8. Atomowa aktualizacja stanu

Jedna zmiana stanu może wymagać równoczesnej aktualizacji:

- karty zadania;
- pakietu pracy;
- rejestru gałęzi;
- bramy;
- `docs/CURRENT_STATE.md`;
- rekordu sterowania.

A00 przygotowuje cały zestaw przed zapisem. Jeżeli aktualizacja jest częściowa albo sprzeczna, tworzy blokadę `STATE_DIVERGENCE`, nie rozpoczyna kolejnej pracy zależnej i najpierw przywraca spójność.

Każda mutacja zwiększa `state_revision` i wskazuje poprzedni stan.

## 9. Kontrola wejść i starzenie

Przy wznowieniu A00 nie ufa staremu `READY`. Ponownie sprawdza:

- wersję kontekstu;
- odciski wejść;
- statusy agentów;
- bramy i zależności;
- konflikty ścieżek;
- środowisko;
- nowe decyzje właściciela;
- ważność dowodów i źródeł.

Zmiana któregokolwiek elementu może cofnąć zadanie do `IMPACT_REVIEW` albo `BLOCKED`.

## 10. Eskalacja do właściciela

A00 eskaluje, gdy potrzebna jest zmiana zakresu, architektury, polityki danych, neutralności, jego własnej władzy, pełne dopuszczenie roli kontrolnej, przyjęcie istotnej zależności, zamknięcie zastrzeżonej bramy, publikacja lub wdrożenie.

Wniosek zawiera rekomendowany wariant, alternatywę, pozostawienie bez zmiany oraz koszt braku decyzji.

## 11. Zamknięcie cyklu

A00 kończy cykl dopiero, gdy:

- stan kanoniczny jest spójny;
- dowody są zapisane;
- wykonane i niewykonane testy są rozdzielone;
- właściciel odblokowania jest znany;
- następny bezpieczny krok jest jednoznaczny;
- nie pozostawiono ukrytej pracy aktywnej.
