# System agentów

## Zasada

Wąska specjalizacja ogranicza błędy tylko przy jednoznacznych kontraktach. Agent jest kontrolowanym wykonawcą. Istnienie kontraktu oznacza rolę planowaną, nie aktywną.

## Project Context Gate

Przed zadaniem agent raportuje:

- identyfikator i wersję kontekstu;
- aktualną fazę;
- przeczytane decyzje;
- własny zakres i zakres dopuszczenia;
- oczekiwane wejścia oraz planowane wyjścia;
- pliki, które zamierza zmienić;
- kryteria akceptacji;
- konflikty lub braki.

Brak elementu zatrzymuje pracę. Context Gate nie zastępuje audytu roli ani testu gotowości zadania.

## Dopuszczenie agenta

Status kanoniczny znajduje się w `registries/agents.yaml`. Agent z `audit_pending`, `changes_required`, `suspended` albo `retired` nie wykonuje pracy projektowej. `pass_conditional` zezwala wyłącznie na klasy zadań zapisane w raporcie i rejestrze.

### Wyjątek startowy

Przed aktywacją A00 obowiązuje wyłącznie `docs/BOOTSTRAP_GOVERNANCE.md`. Właściciel może nadać A01 lub A02 ograniczone `pass_conditional` dla `bootstrap_audit`. Nie jest to praca wykonawcza ani pełna aktywacja.

Po dopuszczeniu A00 wyjątek wygasa. A00 nie zatwierdza własnego kontraktu ani ról, które mają kontrolować jego władzę. Pełne dopuszczenie podstawowych ról kontrolnych wymaga decyzji właściciela lub wskazanego audytu krzyżowego.

## Hierarchia instrukcji

1. Instrukcje systemowe środowiska wykonawczego.
2. Jawne decyzje właściciela i zaakceptowane ADR.
3. `docs/PROJECT_CONSTITUTION.md`.
4. `PROJECT_INSTRUCTIONS.md`.
5. `PROJECT_CONTEXT.yaml` i rejestry kanoniczne.
6. Plan główny oraz bieżący stan.
7. Root `AGENTS.md`.
8. Kontrakt agenta i jego zakres dopuszczenia.
9. Instrukcja lokalnego katalogu.
10. Karta zadania i prompt.

Niższa warstwa nie unieważnia wyższej. Kolejność czytania może być inna niż hierarchia rozstrzygania konfliktu.

## Komunikacja

- przed aktywacją A00 właściciel steruje wyłącznie bootstrapem;
- po aktywacji właściciel komunikuje się z A00;
- A00 przygotowuje zadania dla dopuszczonych wykonawców;
- wykonawcy raportują do A00;
- agent nie zmienia wyniku innego agenta poza formalnym etapem korekty;
- spór dotyczący zakresu lub władzy A00 rozstrzyga właściciel.

## Przekazanie pracy

Każde przekazanie zawiera ID zadania, wersję wejścia, status, autora, wymagane wyjście, zaakceptowane i odrzucone elementy, problemy oraz kryteria kontroli.

## Zmiana agentów

Nowego agenta tworzy się, gdy istnieje powtarzalna odpowiedzialność, stabilne wejście i wyjście, rozdzielenie zmniejsza konflikt interesów oraz istnieją kryteria testowe. Agent wymaga wpisu w rejestrze, kontraktu, testów i raportu dopuszczenia.
