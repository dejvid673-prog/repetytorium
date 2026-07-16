# System agentów

## Zasada

Wąska specjalizacja ogranicza błędy tylko przy jednoznacznych kontraktach. Agent nie jest osobą posiadającą pełną władzę nad obszarem; jest kontrolowanym wykonawcą. Istnienie kontraktu oznacza rolę planowaną, nie aktywną.

## Project Context Gate

Przed zadaniem agent raportuje:

- identyfikator i wersję kontekstu;
- aktualną fazę;
- przeczytane decyzje;
- własny zakres;
- oczekiwane wejścia;
- planowane wyjścia;
- pliki, które zamierza zmienić;
- kryteria akceptacji;
- konflikty lub braki.

Brak któregokolwiek elementu zatrzymuje pracę. Context Gate nie zastępuje audytu roli ani testu gotowości zadania.

## Dopuszczenie agenta

Każdy agent przechodzi procedurę z `docs/AGENT_AUDIT_PLAN.md`. Audyt obejmuje konstrukcję kontraktu, nakładanie kompetencji, dostępność narzędzi, cztery testy zachowania oraz wymagane audyty krzyżowe. Status kanoniczny znajduje się w `registries/agents.yaml`.

Agent z `audit_pending`, `changes_required`, `suspended` albo `retired` nie wykonuje zadań. `pass_conditional` zezwala wyłącznie na klasy zadań wymienione w raporcie.

## Hierarchia instrukcji

1. Konstytucja projektu.
2. Zaakceptowane decyzje właściciela i ADR.
3. Plan główny oraz stan projektu.
4. Nadrzędna instrukcja projektu.
5. Root `AGENTS.md`.
6. Kontrakt konkretnego agenta.
7. Instrukcja lokalnego katalogu.
8. Prompt zadaniowy.

Niższa warstwa nie może unieważnić wyższej.

## Komunikacja

- Właściciel komunikuje się z A00.
- A00 przygotowuje zadania dla wykonawców.
- Wykonawcy raportują do A00.
- Spór pomiędzy agentami rozstrzyga A00 albo przekazuje właścicielowi.
- Agent nie zmienia wyniku innego agenta poza formalnym etapem korekty.

## Przekazanie pracy

Każde przekazanie zawiera:

- ID zadania;
- wersję wejścia;
- status;
- autora;
- wymagane wyjście;
- zaakceptowane i odrzucone elementy;
- nierozwiązane problemy;
- kryteria kontroli.

## Zmiana agentów

Nowego agenta tworzy się, gdy:

- istnieje powtarzalna odpowiedzialność;
- wejście i wyjście są stabilne;
- oddzielenie zmniejsza konflikt interesów;
- istnieją kryteria testowe.

Agent wymaga wpisu w rejestrze, kontraktu, przykładów i testów. Usunięcie lub połączenie agenta wymaga analizy wpływu.
