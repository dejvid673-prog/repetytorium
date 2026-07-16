# Plan testów A00

Status: testy zdefiniowane, jeszcze niewykonane

## Zakres

Testujemy kontrakt, skill `coordinate-repetytorium`, workflow sterowania i schemat zadania. Test nie aktywuje A00 automatycznie.

## Procedura

1. Zamrozić wersje wszystkich testowanych plików.
2. Uruchomić każdy przypadek jawnie w `mode: validation` z `cases.yaml` w czystym kontekście projektu.
3. Zapisać pełne wejście, wynik i użyte pliki.
4. Porównać wynik z polami `expected`.
5. A01 ocenia ochronę kierunku i zakresu.
6. A02 ocenia wykonywalność stanów, schematu, skilla i wznowienia.
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

Testy wykonuje się w WP-0006 po zamrożeniu kontraktu A00. WP-0005 obejmuje wyłącznie ich definicję. Obecność tego pliku nie jest dowodem zaliczenia.
