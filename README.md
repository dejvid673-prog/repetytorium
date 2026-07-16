# Repetytorium Staw Expert

Repozytorium jest źródłem prawdy dla projektu **Repetytorium Staw Expert** — internetowego kompendium wiedzy o stawach, oczkach wodnych, wodzie i rybach, które docelowo będzie bezpośrednio połączone ze sklepem Staw Expert działającym na PrestaShop 9.

## Cel projektu

Repetytorium ma pomóc klientowi:

- odnaleźć problem na podstawie objawów;
- poznać prawdopodobne przyczyny;
- ustalić, jakie obserwacje i pomiary wykonać;
- znaleźć bezpieczne sposoby postępowania;
- przejść do powiązanych artykułów;
- zobaczyć właściwe produkty sklepu, jeżeli ich zastosowanie jest merytorycznie uzasadnione;
- rozpoznać sytuacje wymagające pomocy specjalisty.

To nie ma być zwykły blog. Docelowo powstaje uporządkowany system wiedzy, redakcji, weryfikacji i publikacji.

## Aktualny stan

**Etap: fundament organizacyjny — wersja 0.1.**

Repozytorium nie zawiera jeszcze gotowego modułu PrestaShop, działających agentów ani automatycznej publikacji. Obecna dokumentacja definiuje kierunek projektu, odpowiedzialności, strukturę danych i zasady dalszej pracy.

## Od czego zacząć

1. [AGENTS.md](AGENTS.md) — obowiązkowe zasady dla wszystkich agentów i narzędzi.
2. [Karta projektu](docs/PROJECT_CHARTER.md) — cel, zakres i granice.
3. [Architektura](docs/ARCHITECTURE.md) — warstwy systemu i odpowiedzialności.
4. [Workflow treści](docs/CONTENT_WORKFLOW.md) — droga od badania do publikacji.
5. [Model wiedzy](docs/CONTENT_MODEL.md) — obiekty, relacje i typy artykułów.
6. [Role agentów](agents/README.md) — planowany podział pracy.
7. [Mapa repozytorium](docs/REPOSITORY_MAP.md) — gdzie szukać poszczególnych materiałów.
8. [Decyzje architektoniczne](docs/decisions/README.md) — trwałe decyzje i ich uzasadnienia.

## Główna zasada

GitHub przechowuje źródłową wersję badań, artykułów, metadanych, grafik, instrukcji, agentów, testów i decyzji. PrestaShop jest warstwą publikacji i prezentacji, a nie jedynym magazynem wiedzy.

## Proces w skrócie

```text
badanie -> analiza -> podział na artykuły -> redakcja
-> weryfikacja merytoryczna -> grafiki -> podgląd PrestaShop
-> kontrola techniczna -> zatwierdzenie właściciela -> publikacja
-> monitoring aktualności
```

Publikacja nie może być automatyczna bez wcześniejszego zatwierdzenia, dopóki proces nie zostanie zweryfikowany na odpowiednio dużej próbie materiałów.

## Najbliższy etap

Następny etap powinien ustalić:

- pierwszą taksonomię tematów;
- typy i szablony artykułów;
- format pakietu badawczego;
- kontrakty wejścia i wyjścia agentów;
- zakres pilotażu;
- wymagania modułu PrestaShop 9.

## Status dokumentów

Dokumenty oznaczone jako „projekt” lub „wersja 0.1” nie są jeszcze ostatecznymi wymaganiami wdrożeniowymi. Każda trwała decyzja powinna zostać zapisana w `docs/decisions/`.
