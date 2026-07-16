# Nadrzędna instrukcja projektu

Wersja kontekstu: 0.2  
Projekt: Repetytorium Staw Expert  
Repozytorium: `dejvid673-prog/repetytorium`

## 1. Przeznaczenie

Repozytorium zawiera kompletny projekt publicznej biblioteki wiedzy o przydomowych oczkach wodnych, hobbystycznych stawach, jakości wody, rybach słodkowodnych i utrzymaniu zbiorników. Biblioteka będzie bezpośrednim dodatkiem do sklepu Staw Expert na PrestaShop 9, ale jej treść pozostaje neutralna i nie reklamuje produktów.

## 2. Model zarządzania

Właściciel kieruje wszystkie polecenia do Kierownika Projektu A00. A00:

1. ustala intencję i zakres;
2. porównuje polecenie z planem oraz decyzjami;
3. wykonuje analizę wpływu;
4. wybiera właściwych agentów;
5. określa kolejność i kryteria akceptacji;
6. zbiera raporty;
7. przedstawia właścicielowi wynik i decyzje.

Pozostali agenci nie rozszerzają samodzielnie zakresu i nie zmieniają planu głównego.

## 3. Obowiązkowe źródła kontekstu

Przed pracą każdy agent czyta:

1. `PROJECT_INSTRUCTIONS.md`;
2. `docs/PROJECT_CONSTITUTION.md`;
3. `docs/MASTER_PLAN.md`;
4. `docs/CURRENT_STATE.md`;
5. `AGENTS.md`;
6. zaakceptowane ADR dotyczące zadania;
7. własny plik `agents/<id>/AGENT.md`;
8. instrukcje katalogów objętych zadaniem;
9. prompt konkretnego zadania.

Konflikt zgłasza do A00. Agent nie wybiera samodzielnie wygodniejszej instrukcji.

## 4. Źródło prawdy i użycie innych repozytoriów

Można czytać inne repozytoria właściciela jako materiały referencyjne. Wszystkie artefakty należące do tego projektu — instrukcje, agenci, skille, workflow, schematy, badania, artykuły, grafiki, kod i raporty — tworzy się wyłącznie w tym repozytorium.

Przed przeniesieniem elementu z zewnątrz trzeba sprawdzić:

- czy podobny element już istnieje;
- aktualność;
- licencję i atrybucję;
- zgodność z konstytucją;
- zależności;
- ryzyko bezpieczeństwa;
- zakres wymaganych modyfikacji.

## 5. Zakres

W zakresie:

- przydomowe oczka wodne i hobbystyczne stawy;
- woda, glony, filtracja, napowietrzanie, rośliny i sezonowość;
- ryby polskich wód śródlądowych;
- ryby ozdobne utrzymywane w stawach;
- atrakcyjne gatunki będące przedmiotem zainteresowania pasjonatów;
- problemy, objawy, przyczyny, pomiary i ogólne sposoby postępowania;
- publiczne artykuły dostępne bez logowania;
- kontakt i przesyłanie zdjęć wyłącznie e-mailem;
- korekty czytelników;
- przyszła moderowana biblioteka przypadków;
- szeroka analityka z poszanowaniem prywatności.

Poza zakresem:

- przemysłowa i produkcyjna hodowla ryb;
- automatyczna diagnoza;
- tryb ratunkowy;
- profil zbiornika i dziennik pomiarów;
- kalkulatory repetytorium;
- reklamy, rekomendacje i powiązania produktowe;
- publiczne forum w pierwszych etapach;
- przesyłanie zdjęć przez stronę;
- niezwiązane funkcje sklepu.

## 6. Zasady treści

- Nie zmyślać faktów, źródeł, wyników ani cytatów.
- Rozdzielać fakty, dane producenta, praktykę branżową i hipotezy.
- Materiały o chemii i zdrowiu ryb wymagają niezależnej kontroli.
- Jeden objaw nie stanowi pewnej diagnozy.
- Pokazywać ograniczenia i brakujące dane.
- Artykuł może zawierać ostrzeżenie o konieczności konsultacji, ale system nie świadczy diagnozy.
- Źródła mają być możliwe do zweryfikowania.
- Treść nie może być podporządkowana sprzedaży.

## 7. AI i współpraca ludzi

Strona jawnie informuje o wykorzystaniu AI. Każdy artykuł posiada status redakcyjny i weryfikacyjny. Status „zweryfikowano merytorycznie” wymaga zapisania osoby, daty, zakresu i podstawy weryfikacji.

Czytelnicy mogą zgłaszać błędy, tematy, przypadki i zdjęcia e-mailem. Publikacja danych, nazwiska lub zdjęcia wymaga właściwej zgody. Materiały społecznościowe przechodzą moderację, anonimizację i kontrolę źródeł.

## 8. Zasady techniczne

- PrestaShop 9.
- Bez modyfikacji core.
- Własny moduł i własne tabele.
- Publiczne czytanie bez obowiązkowego logowania.
- Status widoczności niezależny od statusu weryfikacji.
- Historia zmian i możliwość wycofania.
- WCAG 2.2 AA.
- Responsywność i wydajność.
- Bez sekretów oraz danych klientów w Git.
- Import ma być walidowany, wersjonowany i idempotentny.

## 9. Plan i zmiany

Plan nie jest zmieniany nieformalnie. Nowa potrzeba trafia do A00, który klasyfikuje ją jako:

- wykonanie istniejącego planu;
- doprecyzowanie bez wpływu architektonicznego;
- wniosek o zmianę;
- nowy obszar poza zakresem.

Zmiana wpływająca na zakres, architekturę, bezpieczeństwo, dane albo agentów wymaga aktualizacji planu, rejestru i odpowiedniego ADR. Historia decyzji pozostaje zachowana.

## 10. Raportowanie

Każdy wykonawca raportuje:

- kontekst i zakres;
- użyte wejścia;
- zmienione pliki;
- wykonane oraz niewykonane testy;
- wyniki;
- wykryte konflikty;
- ryzyka i ograniczenia;
- status kryteriów akceptacji;
- proponowany następny krok.

Deklaracja ukończenia bez dowodów nie jest akceptowana.
