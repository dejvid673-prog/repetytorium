# Procedura startowa audytu

Status: obowiązująca w Fazie 0 do aktywacji A00  
Właściciel decyzji: właściciel projektu  
Zakres: wyłącznie audyt kontraktów, skilli, workflow, schematów i testów na danych syntetycznych

## Cel

Procedura usuwa zależność kołową, w której A00 nie może działać przed audytem, a audytorzy nie mogą otrzymać zadania od nieaktywnego A00. Nie daje żadnemu agentowi prawa do pracy wykonawczej, publikacji, wdrożenia ani zmiany zakresu.

## Tryb bootstrap

1. Właściciel albo działający w jego imieniu główny koordynator rozmowy tworzy ograniczoną kartę audytu.
2. Kontrakt audytora przechodzi statyczną kontrolę celu, granic, wejść, wyjść, zakazów i konfliktów interesów.
3. Audytor może otrzymać status `pass_conditional` wyłącznie dla klasy `bootstrap_audit`.
4. W tym trybie wolno czytać repozytorium, używać danych syntetycznych, uruchamiać walidatory i zapisywać raporty audytu na aktywnej gałęzi.
5. Nie wolno zlecać pracy innym agentom, zmieniać treści domenowych, projektować UI, implementować modułu, publikować, scalać ani wdrażać.
6. A01 kontroluje kontekst i ład. A02 kontroluje workflow, schematy, skille oraz testowalność.
7. A00 może zostać dopuszczony dopiero po zgodnych raportach A01 i A02 oraz decyzji właściciela.
8. Po aktywacji A00 wyjątek bootstrap wygasa. Kolejne audyty przechodzą zwykły workflow.

## Niezależność

- badany agent nie zatwierdza własnego kontraktu;
- twórca poprawki nie jest jedynym źródłem decyzji o zaliczeniu;
- raport oddziela wynik walidacji automatycznej od oceny właściciela;
- ograniczenie narzędzi lub brak niezależnej sesji audytora są jawnie zapisane;
- role kontrolne A01, A02, A40, A41, A61, A80, A81 i A82 wymagają decyzji właściciela albo audytu krzyżowego przed pełną aktywacją.

## Tryb walidacyjny A00

Przed dopuszczeniem A00 wolno uruchomić jego skill tylko z jawnym parametrem `mode: validation`. Tryb:

- działa na syntetycznym wejściu;
- nie tworzy rzeczywistych zadań, gałęzi, PR, decyzji ani przydziałów;
- nie zmienia rejestrów poza zapisaniem wyniku testu;
- nie uruchamia innych agentów;
- kończy się raportem PASS, BLOCK albo CHANGES_REQUIRED.

## Wygaśnięcie

Procedura przestaje być ścieżką przydzielania zadań po uzyskaniu przez A00 statusu co najmniej `pass_conditional`. Dopuszczenia A01 i A02 ograniczone do `bootstrap_audit` nie przechodzą automatycznie na zwykłe audyty agentów. Wymagają osobnego rozszerzenia zakresu. Dokument pozostaje jako zapis sposobu uruchomienia systemu.
