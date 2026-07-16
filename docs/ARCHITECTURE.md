# Architektura projektu

Status: koncepcja 0.1

## Zasada podziału warstw

Projekt rozdziela:

1. **źródła i badania** — surowy materiał dowodowy;
2. **model wiedzy** — pojęcia, relacje i taksonomia;
3. **treść redakcyjną** — artykuły oraz ich metadane;
4. **zasoby wizualne** — grafiki, ikony i licencje;
5. **publikację** — moduł i interfejs PrestaShop;
6. **kontrolę** — walidację, testy, zatwierdzenie i monitoring.

Zmiana wyglądu nie powinna wymagać przepisywania artykułów. Zmiana artykułu nie powinna wymagać przebudowy modułu.

## Dwa procesy

### A. Budowa platformy

Obejmuje model danych, moduł PrestaShop, komponenty interfejsu, wyszukiwarkę, nawigację, wydajność i dostępność.

### B. Produkcja treści

Obejmuje przyjęcie badania, analizę, podział, redakcję, weryfikację, grafiki, podgląd, zatwierdzenie, publikację i późniejsze aktualizacje.

Agent budujący interfejs nie powinien być uruchamiany dla każdego artykułu. Artykuły korzystają ze stabilnych komponentów.

## Planowane komponenty

- repozytorium GitHub jako źródło prawdy;
- koordynator workflow;
- agenci wyspecjalizowani;
- schematy walidujące pakiety danych;
- własny moduł PrestaShop 9;
- panel Back Office z podglądem i kontrolą publikacji;
- Front Office z kategoriami, wyszukiwarką i artykułami;
- system monitorowania aktualności.

## Przepływ

```text
research/
  -> analiza i mapa tematów
  -> articles/drafts/
  -> kontrola merytoryczna
  -> articles/review/
  -> grafiki i metadane
  -> podgląd PrestaShop
  -> zatwierdzenie właściciela
  -> articles/published/
  -> monitoring aktualności
```

## PrestaShop 9

Rekomendowany jest własny moduł roboczo nazwany `stawexpertknowledge`.

Planowany zakres modułu:

- własne tabele danych;
- encje artykułów, kategorii, tagów i relacji;
- wielojęzyczność;
- statusy wersji;
- import ustrukturyzowanych pakietów;
- podgląd przed publikacją;
- strony Front Office;
- SEO i dane strukturalne;
- relacje z produktami;
- historia zmian.

Nazwa, model danych i zakres modułu nie są jeszcze zatwierdzone jako specyfikacja wykonawcza.

## Bramy bezpieczeństwa

Automatyzacja nie może ominąć:

- kontroli źródeł;
- kontroli merytorycznej dla chemii i zdrowia ryb;
- kontroli praw do grafik;
- kontroli technicznej podglądu;
- zatwierdzenia właściciela przed publikacją produkcyjną.
