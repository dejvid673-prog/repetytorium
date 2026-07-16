# Architektura projektu

Status: koncepcja 0.2

## Warstwy

1. badania źródłowe;
2. pakiety dowodowe;
3. model wiedzy i taksonomia;
4. artykuły i metadane;
5. zasoby wizualne oraz prawa;
6. system projektowy;
7. moduł PrestaShop;
8. wyszukiwarka i SEO;
9. analityka;
10. kontrola i utrzymanie.

Zmiana prezentacji nie wymaga przepisywania faktów. Zmiana wiedzy nie wymaga przebudowy komponentów.

## Procesy

### Platforma

Model danych, UX, prototypy, moduł, wyszukiwarka, dostępność, bezpieczeństwo i analityka.

### Treść

Przyjęcie badania, badania specjalistyczne, taksonomia, plan artykułów, redakcja, audyt, grafiki, podgląd, zatwierdzenie, publikacja i utrzymanie.

### Współpraca

Zgłoszenie e-mail, moderacja, zgoda, weryfikacja, korekta albo przyszły przypadek czytelnika.

## PrestaShop

Własny moduł roboczo `stawexpertknowledge`:

- własne tabele;
- artykuły, kategorie, tagi, gatunki, źródła i relacje treści;
- osobne statusy widoczności i weryfikacji;
- wersjonowanie i korekty;
- Back Office;
- import, podgląd i rollback;
- publiczne strony Front Office;
- SEO i wyszukiwarka;
- model przyszłych przypadków, domyślnie wyłączony.

Brak relacji produktowych i brak zmian core.

## Bramy

- Context Gate;
- walidacja schematów;
- audyt dowodów;
- audyt bezpieczeństwa;
- audyt praw do grafik;
- podgląd techniczny;
- QA techniczne, dostępności i SEO;
- zgoda właściciela na publikację.
