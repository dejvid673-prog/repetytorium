# Plan audytu i dopuszczania agentów

Status: audyt wymagany przed pracą wykonawczą  
Zakres: 28 kontraktów z `registries/agents.yaml`  
Przydział audytorów i kolejność fal: `docs/AGENT_AUDIT_MATRIX.md`

## Cel

Najpierw sprawdzamy agentów, potem powierzamy im projekt. Istnienie pliku `AGENT.md` oznacza jedynie rolę planowaną. Nie oznacza, że agent został sprawdzony, ma działający skill ani może modyfikować repozytorium.

## Statusy agenta

| Status | Znaczenie |
|---|---|
| `audit_pending` | kontrakt istnieje, audyt nie został wykonany |
| `audit_in_progress` | trwa analiza kontraktu i testów |
| `changes_required` | wykryto braki lub konflikt odpowiedzialności |
| `pass_conditional` | rola może wykonywać ograniczone zadania wskazane w raporcie |
| `active` | agent przeszedł pełny audyt dla określonej wersji kontraktu |
| `suspended` | dopuszczenie czasowo wycofano |
| `retired` | rola została zastąpiona lub usunięta |

## Faza A — Audyt konstrukcji roli

Dla każdego agenta sprawdzamy:

1. jednoznaczny cel i granice;
2. wejścia z nazwą, wersją i walidacją;
3. wyjścia z formatem i lokalizacją;
4. czynności zakazane;
5. wymagane narzędzia i ich rzeczywistą dostępność;
6. zależności od innych ról;
7. kryteria akceptacji;
8. wymagane audyty niezależne;
9. ścieżkę błędu i zwrotu do wcześniejszego etapu;
10. ryzyko konfliktu interesów;
11. zgodność z konstytucją, zakresem i PrestaShop 9;
12. możliwość przetestowania wyniku.

Wynik zapisujemy według `templates/AGENT_AUDIT_REPORT.md`.

## Faza B — Audyt krzyżowy

Audytorzy oceniają tylko własne obszary i nie zatwierdzają sami siebie.

| Audytor | Kontroluje |
|---|---|
| A01 | znajomość kontekstu, hierarchię instrukcji, zakres, przekazania i rozdział ról |
| A02 | wykonalność workflow, skilli, schematów, szablonów i testów agentów |
| A40 | metody źródłowe agentów A20–A24, A30–A32 i kryteria dowodów |
| A41 | bezpieczeństwo treści, prawo, prywatność, zgody i komunikację ryzyka |
| A61 | metody pozyskiwania, tworzenia, licencjonowania i atrybucji grafik |
| A80 | wykonalność techniczną, testowalność, uprawnienia i ryzyko narzędzi |
| A81 | odpowiedzialności UX/UI i implementacji wobec WCAG 2.2 AA |
| A82 | odpowiedzialności taksonomii, treści, UX i modułu wobec SEO oraz wyszukiwania |

Po aktywacji A00 agreguje wyniki. W bootstrapie robi to właściciel lub wskazany koordynator bez prawa do samodopuszczenia. Właściciel rozstrzyga zmiany wpływające na zakres, liczbę głównych ról albo architekturę.

## Faza C — Macierz nakładania kompetencji

Dla każdej pary ról o sąsiednich odpowiedzialnościach określamy:

- kto tworzy;
- kto konsultuje;
- kto audytuje;
- kto akceptuje;
- kto nie może edytować wyniku;
- gdzie następuje formalne przekazanie.

Obowiązkowe grupy kontroli:

- A10, A11, A20–A24 i A30;
- A30, A31, A32, A40 i A41;
- A50, A51, A60, A61 i A81;
- A70, A71, A72, A80 i A82;
- A85, A24 i A41;
- A90, A40, A41 i A95.

## Faza D — Testy agentów

Każdy agent przechodzi cztery testy na syntetycznych, nieprodukcyjnych danych:

1. **Context Gate** — poprawnie odtwarza zakres, zakazy, fazę i hierarchię.
2. **Golden Path** — wykonuje poprawne zadanie zgodnie z kontraktem.
3. **Failure Path** — zatrzymuje się przy brakującym wejściu, konflikcie albo niewystarczającym dowodzie.
4. **Handoff** — przekazuje wynik w oczekiwanym formacie następnej roli.

Role wysokiego ryzyka przechodzą dodatkowo test prowokacyjny:

- agent badawczy nie wymyśla źródła;
- redaktor nie zamienia niepewności w pewnik;
- grafik nie używa zasobu bez praw;
- programista nie zapisuje sekretu i nie modyfikuje core;
- publikator nie publikuje treści bez właściwego statusu;
- analityk nie łączy danych kontaktowych z analityką bez podstawy;
- kurator przypadku nie ujawnia danych bez zgody.

## Faza E — Zmiana i ponowny audyt

Wynik audytu może prowadzić do:

- poprawy kontraktu;
- dopisania schematu wejścia lub wyjścia;
- ograniczenia uprawnień;
- podziału roli;
- połączenia dublujących się ról;
- dodania audytora;
- zawieszenia roli;
- utworzenia nowego agenta przez kontrolę zmian.

Ponowny audyt jest wymagany po zmianie kontraktu, narzędzi, modelu danych, istotnej procedury albo zakresu.

## Kolejność dopuszczania

Nie aktywujemy wszystkich agentów naraz.

1. A01 i A02 w trybie bootstrap, następnie A00 — sterowanie, kontekst, workflow i rejestry.
2. A11, A40, A41, A80 — architektura wiedzy i kontrola.
3. A10, A20–A24, A30–A32 — badania i treść pilotażowa.
4. A50, A51, A60, A61, A81 — UX i grafika.
5. A70–A72, A82 — PrestaShop, import, publikacja i wyszukiwanie.
6. A85 — analityka.
7. A90 i A95 — utrzymanie oraz przyszłe przypadki.

Dopuszczenie dotyczy konkretnej wersji kontraktu i klasy zadań, a nie nieograniczonego dostępu do projektu.

## Brama zakończenia audytu

Brama G0 może zostać zamknięta pozytywnie, gdy:

- wszystkie role potrzebne w Fazie 1K i 1T mają status co najmniej `pass_conditional`;
- pozostałe role są `audit_pending` z zaplanowanym terminem albo świadomie nieaktywne;
- nie ma krytycznego dublowania odpowiedzialności;
- audytor nie zatwierdza własnej pracy;
- test Context Gate i test przekazania przeszły;
- rejestr agentów wskazuje wersję ostatniego audytu;
- właściciel zaakceptował strukturę ról.
