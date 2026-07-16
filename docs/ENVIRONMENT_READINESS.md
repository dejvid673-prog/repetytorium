# Gotowość środowisk

Status: plan techniczny; realizacja po Bramie G0

## Środowiska

| Kod | Środowisko | Przeznaczenie | Dane |
|---|---|---|---|
| `DOCS` | dokumentacyjne | schematy, kontrakty, artykuły i audyty | wyłącznie dane projektowe |
| `DEV` | developerskie | lokalna budowa modułu i integracja | syntetyczne fixture |
| `TEST` | automatycznych testów | CI, migracje, walidacja i regresja | dane syntetyczne odtwarzalne |
| `STAGE` | przedprodukcyjne | UAT, pełny import i test wdrożenia | zanonimizowane albo syntetyczne |
| `PROD` | produkcyjne | publiczna biblioteka | minimalny zatwierdzony zakres danych |

## Tory gotowości

Tor wiedzy może rozpocząć się po G0 w środowisku `DOCS`. Nie czeka na PrestaShop.

Tor techniczny może rozpocząć przygotowanie `DEV` i `TEST` po G0, ale implementacja modelu danych czeka na zatwierdzone schematy Fazy 1.

UX może rozpocząć architekturę informacji po zatwierdzeniu taksonomii, a makiety treściowe dopiero po dostępności reprezentatywnego pakietu pilotażowego.

## Brama ENV-DEV

Środowisko developerskie ma status `READY`, gdy:

- wersje PHP, PrestaShop 9, bazy danych, Node i narzędzi są przypięte;
- istnieje instrukcja uruchomienia od czystego systemu;
- konfiguracja przykładowa nie zawiera sekretów;
- instalacja jest powtarzalna;
- istnieją syntetyczne dane startowe;
- moduł można zainstalować i odinstalować;
- logi nie ujawniają danych wrażliwych;
- A80 odtworzył instrukcję niezależnie.

## Brama ENV-TEST

- CI uruchamia walidatory, testy i analizę statyczną;
- baza testowa jest tworzona automatycznie;
- migracje można przetestować w obie strony albo bezpiecznie odtworzyć;
- fixture są wersjonowane;
- wynik testu jest zapisywany;
- błąd blokuje łączenie wymagających kodu PR-ów.

## Brama ENV-STAGE

- konfiguracja jest możliwie zgodna z produkcją;
- dane nie naruszają prywatności;
- istnieją backup, restore i rollback;
- import pełnego pakietu jest testowalny;
- dostęp jest ograniczony;
- monitoring i smoke test są gotowe;
- właściciel zna różnice między STAGE i PROD.

## Zakazy

- żadnych danych klientów sklepu w repozytorium;
- żadnych sekretów w plikach, fixture, logach i przykładach;
- żadnego uznania „działa u mnie” za dowód gotowości;
- żadnego wdrożenia z DEV bez przejścia przez TEST i STAGE;
- żadnych nieudokumentowanych ręcznych poprawek środowiska.
