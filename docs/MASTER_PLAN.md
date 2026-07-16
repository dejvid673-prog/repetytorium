# Plan główny

Status: obowiązujący plan bazowy 0.2  
Zasada: cały znany zakres jest ujęty w planie; realizacja przebiega według zależności.

## Faza 0 — Ład projektu

Cel: repozytorium samo wyjaśnia cel, plan, decyzje i role.

Artefakty:

- instrukcja nadrzędna;
- konstytucja;
- profil projektu;
- mapa repozytorium;
- system ADR;
- system agentów;
- rejestry;
- mechanizm zmiany planu;
- aktualny stan projektu.

Kryteria zakończenia:

- brak sprzeczności w dokumentach nadrzędnych;
- każdy agent ma osobny kontrakt;
- każdy agent przechodzi Context Gate;
- właściciel zatwierdza plan bazowy.

## Faza 1 — Architektura wiedzy

Cel: ustalić, co przechowujemy i jak elementy są powiązane.

Zakres:

- taksonomia oczek, stawów, wody, techniki, roślin i ryb;
- lista grup gatunków;
- terminologia i synonimy;
- typy artykułów;
- model twierdzeń i źródeł;
- statusy widoczności, redakcji i weryfikacji;
- model korekt;
- model przyszłych przypadków czytelników;
- format pakietu badawczego.

Kryteria zakończenia:

- schematy przechodzą walidację;
- przykładowe dane reprezentują kilka różnych tematów;
- nie ma relacji produktowych;
- wysokie ryzyko jest oznaczane maszynowo.

## Faza 2 — Fabryka badań i treści

Cel: przeprowadzić materiał od badania do zatwierdzonego artykułu.

Zakres:

- przyjmowanie badań;
- analiza i katalogowanie;
- badania specjalistyczne;
- planowanie artykułów;
- redakcja;
- prezentacja treści;
- audyt źródeł;
- audyt bezpieczeństwa;
- korekty;
- raporty.

Kryteria zakończenia:

- jeden pakiet badawczy przechodzi pełen workflow;
- każde przekazanie ma poprawny kontrakt;
- błędy są cofane do właściwego etapu;
- status „zweryfikowany” zawiera dowody.

## Faza 3 — System projektowy i UX

Cel: zaprojektować dopracowane, spokojne i nowoczesne repetytorium.

Zakres:

- architektura informacji;
- ścieżki: przeglądanie, problem, gatunek, nauka;
- system kolorów, typografii i odstępów;
- komponenty;
- responsywne makiety HTML;
- strony główna, kategoria, wyniki, artykuł, gatunek, korekty i współtworzenie;
- WCAG 2.2 AA;
- testy z rzeczywistą treścią.

Kryteria zakończenia:

- zatwierdzone makiety desktop i mobile;
- interfejs nie przypomina dokumentu Word ani strony dziecięcej;
- nie używa emoji jako ikon;
- komponenty są udokumentowane;
- najważniejsze widoki przechodzą audyt dostępności.

## Faza 4 — Architektura i fundament modułu PrestaShop

Cel: stworzyć bezpieczną podstawę techniczną bez publikowania produkcyjnego.

Zakres:

- specyfikacja modułu;
- własne tabele;
- encje i migracje;
- role i uprawnienia;
- Back Office;
- import i walidacja;
- wersjonowanie;
- historia i wycofanie;
- publiczne trasy Front Office;
- wielojęzyczna gotowość techniczna przy polskiej treści startowej.

Kryteria zakończenia:

- instalacja i odinstalowanie w środowisku testowym;
- migracje są odwracalne albo bezpiecznie obsługiwane;
- brak modyfikacji core;
- testy bezpieczeństwa i uprawnień;
- brak utraty danych przy aktualizacji.

## Faza 5 — Wyszukiwarka i odkrywanie treści

Cel: użytkownik znajduje treść po języku potocznym.

Zakres:

- pełnotekstowe wyszukiwanie;
- synonimy, literówki i nazwy naukowe;
- filtry;
- breadcrumbs;
- powiązane artykuły;
- wyniki bez dopasowania;
- rejestr luk wiedzy;
- SEO techniczne i dane strukturalne.

Kryteria zakończenia:

- zestaw testowych zapytań ma oczekiwane wyniki;
- brak wyniku jest rejestrowany;
- adresy i canonical są stabilne;
- sitemap oraz dane strukturalne przechodzą testy.

## Faza 6 — Budowa biblioteki startowej

Cel: uruchomić serwis z szeroką, spójną i dopracowaną zawartością, bez pustych działów.

Zakres priorytetowy:

- podstawy wody i jej parametrów;
- glony i klarowność;
- filtracja i napowietrzanie;
- sezonowość;
- ryby popularne;
- problemy zdrowotne i środowiskowe;
- budowa i utrzymanie;
- pierwsze profile gatunków.

Kryteria zakończenia:

- każda widoczna kategoria ma wartościową treść;
- każdy artykuł ma źródła i status;
- materiały wysokiego ryzyka mają niezależną kontrolę;
- grafiki mają rejestr praw;
- zatwierdzona wersja znajduje się w repozytorium.

## Faza 7 — Analityka, kontakt i korekty

Cel: uczyć się z zachowania użytkowników i zgłoszeń.

Zakres:

- katalog zdarzeń;
- zarządzanie zgodami;
- centralny logiczny magazyn analityczny;
- pseudonimizacja i retencja;
- wyszukiwania bez wyników;
- ocena przydatności;
- obsługa e-maili i zdjęć poza stroną;
- dziennik korekt;
- podziękowania za zgodą.

Kryteria zakończenia:

- każde zdarzenie ma cel i właściciela;
- dane kontaktowe są oddzielone od analityki;
- istnieje procedura usunięcia;
- korekta przechodzi ponowną kontrolę;
- publiczny komunikat nie ujawnia danych bez zgody.

## Faza 8 — Testy przed uruchomieniem

Zakres:

- funkcjonalność;
- bezpieczeństwo;
- dostępność;
- responsywność;
- wydajność;
- SEO;
- migracje;
- import;
- wersjonowanie;
- przywracanie;
- błędne dane;
- linki i grafiki;
- test redakcyjny;
- test produkcyjnego rollbacku.

Kryterium: brak otwartych błędów krytycznych i wysokich; znane ograniczenia zaakceptowane przez właściciela.

## Faza 9 — Uruchomienie

- kopia zapasowa;
- kontrola wersji;
- wdrożenie;
- smoke test;
- indeksowanie;
- monitoring;
- raport powdrożeniowy;
- gotowy rollback.

Publikację zatwierdza właściciel.

## Faza 10 — Utrzymanie i współpraca

- monitoring aktualności;
- przeglądy źródeł;
- poprawki czytelników;
- nowe artykuły;
- analiza luk;
- aktualizacja agentów i skilli przez kontrolę zmian;
- rozwijanie biblioteki gatunków;
- audyty okresowe.

## Faza 11 — Moderowana biblioteka przypadków

Model danych projektujemy wcześniej, ale funkcję włączamy dopiero po osobnej decyzji.

Zakres przyszły:

- zgłoszenie e-mailem;
- zgoda;
- anonimizacja;
- redakcja;
- weryfikacja;
- publikacja przypadku;
- powiązania z artykułami.

Publiczne forum nie jest częścią zatwierdzonego zakresu.
