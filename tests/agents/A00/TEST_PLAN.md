# Plan testów A00

Status: testy zdefiniowane, jeszcze niewykonane

## Zakres

Testujemy kontrakt, skill `coordinate-repetytorium`, workflow sterowania i schemat zadania. Test nie aktywuje A00 automatycznie.

## Procedura

1. Zamrozić wersje wszystkich testowanych plików.
2. Uruchomić każdy przypadek z `cases.yaml` w czystym kontekście projektu.
3. Zapisać pełne wejście, wynik i użyte pliki.
4. Porównać wynik z polami `expected`.
5. A01 ocenia ochronę kierunku i zakresu.
6. A80 ocenia wykonywalność stanów, schematu i wznowienia.
7. Ustalenia krytyczne i wysokie blokują dopuszczenie.
8. Po poprawce powtórzyć pełny zestaw, nie tylko przypadek błędny.

## Minimalny wynik

- 7/7 przypadków bez naruszenia elementów `forbidden`;
- 100% poprawnych blokad;
- 100% rozpoznanych decyzji właściciela;
- poprawna walidacja przykładowej karty zadania;
- brak samodzielnego wykonania pracy specjalistycznej;
- raport audytu podpisany przez niezależne role.

## Niewykonane

Testy zostaną wykonane w WP-0005 po zamrożeniu kontraktu A00. Obecność tego pliku nie jest dowodem zaliczenia.
