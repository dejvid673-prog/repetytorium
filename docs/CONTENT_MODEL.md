# Model wiedzy i treści

Status: projekt 0.1

## Podstawowe obiekty

- problem;
- objaw;
- możliwa przyczyna;
- parametr wody;
- pomiar lub obserwacja;
- działanie;
- zagrożenie;
- organizm;
- gatunek;
- choroba;
- typ zbiornika;
- urządzenie lub metoda;
- artykuł;
- produkt;
- źródło.

## Przykładowe relacje

- objaw **może wskazywać na** problem;
- problem **może wynikać z** przyczyny;
- przyczynę **można sprawdzić przez** pomiar;
- działanie **dotyczy** problemu;
- działanie **ma ograniczenie**;
- artykuł **wyjaśnia** obiekt wiedzy;
- artykuł **jest powiązany z** innym artykułem;
- produkt **może wspierać** działanie;
- twierdzenie **jest poparte przez** źródło.

Relacje muszą dopuszczać niepewność. Jeden objaw nie oznacza automatycznie jednej diagnozy.

## Typy artykułów

1. Problem.
2. Objaw ryb.
3. Choroba.
4. Parametr wody.
5. Gatunek ryby.
6. Poradnik.
7. Procedura sezonowa.
8. Budowa i technika.
9. Substancja lub metoda.
10. Porównanie rozwiązań.

Każdy typ otrzyma osobny szablon i wymagane pola.

## Minimalne metadane artykułu

- trwały identyfikator;
- wersja;
- status;
- typ;
- tytuł;
- slug;
- streszczenie;
- kategoria;
- grupa odbiorców;
- główne pytanie użytkownika;
- treść;
- źródła;
- twierdzenia wymagające kontroli;
- ostrzeżenia;
- powiązane artykuły;
- proponowane produkty;
- grafiki i teksty alternatywne;
- data utworzenia;
- data ostatniej weryfikacji;
- planowana data kolejnego przeglądu;
- historia zatwierdzeń.

## Ważne rozróżnienie

Artykuł jest prezentacją wybranego fragmentu wiedzy. Model problemów, objawów, przyczyn i pomiarów powinien być przechowywany niezależnie, aby w przyszłości umożliwić wyszukiwarkę problemową oraz kreator diagnostyczny.
