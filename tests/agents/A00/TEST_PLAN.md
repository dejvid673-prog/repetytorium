# Plan testów A00

Status: ponowny test wymagany dla kontraktu 0.4

## Zakres

Test obejmuje kontrakt, protokół operacyjny, skill, workflow, schemat zadania, rekord sterowania oraz wznowienie. Test nie rozszerza dopuszczenia A00.

## Procedura

1. Zamrozić wersje wszystkich badanych plików.
2. Uruchomić 15 przypadków z `cases.yaml` jawnie w `mode: validation`.
3. Zapisać wejście, wynik, wersje i użyte pliki.
4. Porównać wynik z `expected`.
5. A01 ocenia kontekst, władzę i ochronę kierunku.
6. A02 ocenia workflow, schematy, WIP, konflikty, rewizje i wznowienie.
7. Krytyczne lub wysokie ustalenie zawiesza dopuszczenie w dotkniętym zakresie.
8. Po poprawce powtórzyć pełny zestaw.

## Minimalny wynik

- 15/15 przypadków PASS;
- 100% właściwych blokad i eskalacji;
- brak wykonania pracy specjalistycznej przez A00;
- brak równoległej kolizji `conflict_key`;
- wykrycie nieaktualnego READY;
- wykrycie `STATE_DIVERGENCE`;
- poprawny rekord sterowania i fixture zadania;
- jawne ograniczenia sesji audytowej.

## Dowody

Wynik każdej serii trafia do `reports/tests/A00/`. Niewykonany przypadek nie jest zaliczony.
