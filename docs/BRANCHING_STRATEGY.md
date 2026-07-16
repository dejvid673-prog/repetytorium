# Strategia gałęzi

Status: plan obowiązujący od zatwierdzenia Fazy 0  
Właściciel procesu: A00 — Kierownik Projektu

## Cel

Gałęzie mają umożliwiać pracę równoległą bez rozpoczynania zadań, dla których nie istnieją jeszcze wymagane dane, kontrakty albo środowisko. Samo utworzenie agenta lub wpisanie zadania do planu nie oznacza zgody na rozpoczęcie pracy.

## Typy gałęzi

| Typ | Wzorzec | Przeznaczenie | Docelowy PR |
|---|---|---|---|
| stabilna | `main` | wyłącznie zatwierdzone podstawy, wydania i dokumentacja zgodna ze stanem faktycznym | nie dotyczy |
| integracyjna fazy | `phase/<nr>-<nazwa>` | wspólna integracja rezultatów jednej fazy albo niezależnego toru fazy | do `main` |
| zadaniowa agenta | `agent/<faza>-<id>-<zadanie>` | jedno ograniczone zadanie jednego agenta | do właściwej gałęzi `phase/*` |
| naprawcza | `fix/<faza>-<opis>` | błąd wykryty przed wdrożeniem | do aktywnej gałęzi fazy |
| pilna produkcyjna | `hotfix/<opis>` | krytyczna poprawka po uruchomieniu | do `main`, następnie synchronizacja z aktywnymi fazami |
| wydaniowa | `release/<wersja>` | stabilizacja zatwierdzonego wdrożenia, gdy będzie potrzebna | do `main` |

Bieżąca gałąź `agent/repository-foundation` jest historycznym wyjątkiem utworzonym przed przyjęciem tej konwencji.

## Zasady bez wyjątków

1. Nie wykonuje się bezpośrednich zmian na `main`.
2. Jedna gałąź zadaniowa obejmuje jedno zadanie, jednego właściciela i jedno jawne wyjście.
3. Każda gałąź posiada wpis w `registries/branches.yaml` i manifest według `templates/BRANCH_MANIFEST.yaml`.
4. Gałąź zadaniowa powstaje dopiero po uzyskaniu statusu `READY`.
5. Draft PR powstaje na początku pracy, a nie po jej zakończeniu.
6. Zmiany agenta trafiają do gałęzi integracyjnej fazy; dopiero zatwierdzona faza trafia do `main`.
7. Nie łączy się PR bez raportu wykonania, testów właściwych dla ryzyka i wymaganych audytów.
8. Scalanie do `main` wymaga zamkniętej bramy fazowej oraz decyzji właściciela tam, gdzie plan jej wymaga.
9. Preferowaną metodą włączenia PR fazy do `main` jest squash, aby historia główna pozostała czytelna.
10. Sekrety, dane klientów i pliki środowiskowe z poufnymi wartościami nigdy nie trafiają do gałęzi.

## Cykl życia gałęzi

| Status | Znaczenie |
|---|---|
| `PLANNED` | zadanie opisane, ale zależności nie zostały jeszcze sprawdzone |
| `BLOCKED` | co najmniej jedna zależność, brama, zgoda lub część środowiska nie jest gotowa |
| `READY` | można utworzyć gałąź; wejścia i środowisko są dostępne |
| `ACTIVE` | trwa dozwolona praca |
| `REVIEW` | wynik jest kompletny i oczekuje na audyty lub decyzję |
| `CHANGES_REQUIRED` | audyt wykazał konieczne poprawki |
| `ACCEPTED` | wynik spełnia kryteria i może zostać scalony |
| `MERGED` | wynik jest w gałęzi docelowej |
| `CANCELLED` | zadanie świadomie wycofano z zachowaniem przyczyny |

Przejście `BLOCKED -> READY` zapisuje A00 po ponownym sprawdzeniu rejestru zależności. Agent wykonawczy nie zmienia tego statusu samodzielnie.

## Gałęzie integracyjne i równoległość

Po zamknięciu Bramy G0 mogą równolegle rozpocząć się dwa niezależne tory:

- `phase/01-knowledge-foundation` — model wiedzy, taksonomie, statusy, źródła i pakiety;
- `phase/01t-technical-environment` — powtarzalne środowisko PrestaShop 9, testy, CI i zasady techniczne.

Kolejne tory są otwierane tylko na podstawie `docs/PHASE_EXECUTION_PLAN.md` oraz `registries/phase-gates.yaml`.

## Gałęzie zależne

Zagnieżdżone lub „stackowane” PR-y są wyjątkiem. Stosuje się je wyłącznie, gdy:

- czekanie zablokowałoby istotną niezależną pracę;
- zależność ma stabilny kontrakt;
- manifest podaje dokładną gałąź bazową;
- A00 zatwierdził ryzyko ponownego bazowania.

Preferowany model to najpierw scalić wymagany kontrakt do gałęzi fazy, a dopiero potem otworzyć zależną gałąź zadaniową.

## Kontrola przed utworzeniem gałęzi

A00 potwierdza:

- zgodność zadania z zakresem i aktywną fazą;
- wynik audytu agenta co najmniej `PASS_CONDITIONAL`;
- dostępność kompletnych wejść;
- spełnienie wszystkich `depends_on`;
- gotowość wymaganego środowiska;
- brak konfliktu z inną aktywną gałęzią;
- kryteria akceptacji i wymaganych recenzentów;
- plan testów oraz wycofania, jeżeli zmiana może wpływać na dane lub wdrożenie.

Brak jednej odpowiedzi powoduje status `BLOCKED`.
