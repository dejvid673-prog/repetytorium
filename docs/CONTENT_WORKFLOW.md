# Workflow treści

Status: projekt 0.1

## Statusy

1. `NEW_RESEARCH` — nowe badanie.
2. `RESEARCH_ANALYSIS` — analiza materiału.
3. `ARTICLE_PLAN` — przygotowany podział na artykuły.
4. `DRAFTING` — redagowanie.
5. `FACT_CHECK` — kontrola faktów, źródeł i bezpieczeństwa.
6. `CORRECTIONS_REQUIRED` — poprawki wymagane.
7. `VISUAL_PREPARATION` — przygotowanie zasobów wizualnych.
8. `TECHNICAL_PREVIEW` — podgląd w warstwie publikacyjnej.
9. `HUMAN_APPROVAL` — oczekiwanie na decyzję właściciela.
10. `SCHEDULED` — publikacja zaplanowana.
11. `PUBLISHED` — opublikowano.
12. `REVIEW_REQUIRED` — potrzebna ponowna weryfikacja.
13. `ARCHIVED` — materiał wycofany, historia zachowana.

## Etapy

### 1. Przyjęcie badania

Koordynator:

- nadaje identyfikator;
- sprawdza kompletność;
- rejestruje pochodzenie i datę;
- blokuje przetwarzanie, jeśli brakuje kluczowych plików.

### 2. Analiza

Analityk:

- czyta całość;
- tworzy mapę pojęć;
- rozpoznaje duplikaty i luki;
- dzieli materiał na planowane artykuły;
- przypisuje źródła i twierdzenia;
- przygotowuje konspekty.

### 3. Redakcja

Redaktor:

- pracuje wyłącznie na zatwierdzonym pakiecie;
- używa właściwego szablonu artykułu;
- rozdziela fakty, hipotezy i ostrzeżenia;
- przygotowuje metadane, linki i briefy grafik.

### 4. Weryfikacja

Weryfikator:

- porównuje artykuł z badaniem;
- sprawdza źródła, jednostki i logikę;
- oznacza sprzeczności;
- blokuje niebezpieczne lub nieudokumentowane zalecenia;
- przekazuje precyzyjną listę poprawek.

### 5. Warstwa wizualna

Grafik:

- przygotowuje elementy zgodne z systemem wizualnym;
- zapisuje źródło i licencję;
- optymalizuje format;
- dostarcza tekst alternatywny.

### 6. Podgląd techniczny

Integrator:

- waliduje pakiet;
- importuje wersję roboczą;
- buduje podgląd;
- sprawdza linki, grafiki i relacje;
- nie zmienia samodzielnie znaczenia treści.

### 7. Zatwierdzenie

Właściciel podejmuje decyzję:

- zatwierdzić;
- zwrócić do poprawy;
- odłożyć;
- odrzucić;
- opublikować później.

### 8. Publikacja i utrzymanie

Po publikacji zapisuje się identyfikator, URL, wersję, datę i wynik kontroli. Monitoring wykrywa materiały nieaktualne, błędne linki, zmienione produkty i wymagane przeglądy.

## Zasada cofania

Każdy etap może zwrócić materiał do wskazanego wcześniejszego etapu z raportem problemów. Nie wolno poprawiać problemu w ukryciu poza zakresem roli.
