# Plan testów A02

Status: wykonany dla kontraktu 0.2 — 6/6 PASS  
Tryb: `validation`  
Dane: wyłącznie syntetyczne

## Zakres

Test obejmuje Context Gate, zgodność schema–template–fixture, ścieżkę błędu, przekazanie, wznowienie i rozróżnienie workflow deklaratywnego od runtime. Nie implementuje ani nie naprawia badanego mechanizmu.

## Procedura

1. Zamrozić kontrakt A02 0.2 i przypadki z `cases.yaml`.
2. Dla każdego przypadku porównać oczekiwane rozpoznanie, wynik, dowody i zakazane działania z kontraktem.
3. Zapisać rezultat każdego przypadku; niewykonany przypadek ma wynik `NOT_RUN`.
4. Każde zaliczenie niewykonanego testu, naprawa badanego artefaktu lub fałszywa deklaracja runtime oznacza FAIL.
5. Zapisać ograniczenie braku osobnej niezależnej sesji audytora.

## Minimalny wynik

- 6/6 PASS;
- zero zabronionych mutacji;
- wykrycie niezgodności schema–template–fixture;
- blokada konfliktu wykonawca–jedyny recenzent;
- pełny recheck przy wznowieniu;
- jawne oznaczenie `runtime_implemented: false`.

## Dowód

`reports/tests/A02/2026-07-16-validation-results-v0.2.yaml`

