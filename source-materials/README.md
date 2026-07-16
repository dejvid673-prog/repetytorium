# Materiały źródłowe właściciela

To jest katalog publicznego repozytorium. Właściciel może tu dodawać wyłącznie instrukcje, dokumentację, przykłady i pliki pomocnicze, które wolno publicznie przechowywać. Materiały są wejściem do projektu, lecz nie zmieniają automatycznie konstytucji, zakresu ani planu.

## Planowane grupy

- `owner-instructions/` — nowe ustalenia i instrukcje właściciela;
- `brand/` — logo, kolory, typografia i przykłady estetyki;
- `prestashop/` — bezpieczna dokumentacja środowiska i integracji;
- `domain/` — własne materiały o oczkach, stawach, wodzie i rybach;
- `examples/` — przykłady dobrych i złych stron lub artykułów;
- `customer-questions/` — zanonimizowane wzorce pytań, bez danych klientów.

Katalogi mogą powstać razem z pierwszym rzeczywistym materiałem.

## Nazewnictwo

Preferowany format:

```text
YYYY-MM-DD__temat__vNN.ext
```

Do pliku warto dołączyć informację:

- skąd pochodzi;
- kto go przygotował;
- kiedy;
- czy zastępuje wcześniejszy materiał;
- do czego ma zostać użyty;
- czy zawiera treści wymagające zgody lub atrybucji.

## Obowiązkowy preflight

Przed uploadem należy zastosować `workflows/source-material-intake.yaml` i metadane zgodne ze schematem `schemas/source-material-intake.schema.json`. Plik zawierający dane osobowe, sekrety albo materiał bez prawa redystrybucji nie może trafić nawet tymczasowo do historii Git.

## Kontrola wejścia

A00:

1. rejestruje materiał;
2. sprawdza duplikaty i konflikt z decyzjami;
3. klasyfikuje wpływ;
4. wskazuje właściwą fazę oraz agenta;
5. prosi o decyzję, jeżeli materiał zmienia zakres;
6. zachowuje historię.

## Zakazy

Nie dodawać:

- haseł, tokenów i kluczy;
- eksportów danych klientów;
- danych zamówień;
- prywatnych wiadomości bez anonimizacji;
- zdjęć bez informacji o prawach i zgodzie;
- cudzych materiałów bez podstawy prawnej.

Raporty głębokich badań przeznaczone do przetwarzania trafiają do `research/inbox/`, zgodnie z `research/README.md`.
