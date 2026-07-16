# Zarządzanie zależnościami i blokadami

Status: plan obowiązujący  
Właściciel rejestru: A00

## Zasada

Zadanie jest gotowe do pracy dopiero wtedy, gdy posiada kompletne wejścia, dopuszczonego agenta, otwartą bramę, gotowe środowisko i brak nierozwiązanej zależności krytycznej.

## Rodzaje zależności

| Kod | Rodzaj | Przykład |
|---|---|---|
| `CTX` | kontekst i decyzje | zatwierdzona konstytucja oraz aktualna wersja profilu |
| `AGENT` | dopuszczenie wykonawcy | audyt agenta i test przekazania |
| `DATA` | dane lub schemat | artykuł wymaga zatwierdzonego modelu twierdzeń |
| `CONTENT` | próbka treści | makieta artykułu wymaga rzeczywistej treści pilotażowej |
| `DESIGN` | projekt interfejsu | Front Office wymaga zaakceptowanych komponentów |
| `ENV` | środowisko | moduł wymaga powtarzalnego PrestaShop 9 i bazy testowej |
| `CODE` | implementacja | importer wymaga encji, migracji i walidatora |
| `AUDIT` | niezależna kontrola | treść o zdrowiu ryb wymaga A40 i A41 |
| `OWNER` | decyzja właściciela | publikacja, zmiana zakresu albo start produkcyjny |
| `LEGAL` | prawo, licencja lub zgoda | użycie zdjęcia wymaga rejestru praw |

## Reguła gotowości

Zadanie otrzymuje `READY`, gdy jednocześnie:

1. wszystkie wymagane bramy mają status `OPEN` albo `PASSED`;
2. wszystkie elementy `depends_on` mają status `ACCEPTED` lub `MERGED`;
3. wymagane środowisko ma status `READY`;
4. wykonawca ma ważne dopuszczenie do tej klasy zadania;
5. wejścia mają wersję i walidację;
6. audytorzy nie są tym samym wykonawcą;
7. istnieje kryterium zakończenia i dowód możliwy do sprawdzenia.

## Klasy blokad

| Poziom | Znaczenie | Działanie |
|---|---|---|
| `B0` | informacja, nie zatrzymuje pracy | zapisać w raporcie |
| `B1` | blokuje jedno zadanie | A00 wyznacza właściciela usunięcia |
| `B2` | blokuje tor albo etap | wstrzymać zależne gałęzie |
| `B3` | blokuje fazę lub zagraża zakresowi/danym | decyzja właściciela i możliwy ADR |
| `B4` | ryzyko produkcyjne, bezpieczeństwa lub utraty danych | natychmiast zatrzymać dotknięte prace |

## Procedura blokady

1. Agent nie obchodzi brakującej zależności.
2. Zgłasza kod, poziom, dowód i wpływ do A00.
3. A00 aktualizuje `registries/branches.yaml` oraz, gdy dotyczy, `registries/phase-gates.yaml`.
4. A00 wskazuje zadanie odblokowujące, właściciela i warunek ponownej kontroli.
5. Zależne gałęzie pozostają `BLOCKED`; mogą wykonywać tylko pracę wyraźnie niezależną.
6. Po dostarczeniu brakującego wyniku przeprowadza się ponowny test gotowości.

## Niedozwolone pozorne odblokowanie

Nie uznaje się za spełnienie zależności:

- ustnej deklaracji bez pliku lub raportu;
- niezatwierdzonej makiety użytej jako specyfikacja;
- danych przykładowych przedstawionych jako finalny schemat;
- lokalnego środowiska bez instrukcji odtworzenia;
- wyniku agenta bez audytu wymaganego dla ryzyka;
- kodu działającego tylko na nieudokumentowanej konfiguracji;
- źródła bez możliwości identyfikacji;
- grafiki bez informacji o prawach.

## Raportowanie

Każda blokada zawiera:

- `blocker_id`;
- rodzaj zależności;
- poziom B0–B4;
- zadanie i gałęzie dotknięte;
- właściciela usunięcia;
- wymagany rezultat;
- datę ostatniego sprawdzenia;
- dowód odblokowania;
- decyzję A00.
