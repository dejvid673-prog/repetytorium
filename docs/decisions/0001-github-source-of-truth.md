# ADR-0001: GitHub jako źródło prawdy

Status: accepted  
Data: 2026-07-16

## Kontekst

Projekt obejmuje badania, wiedzę, artykuły, grafiki, agentów, workflow, kod PrestaShop oraz historię decyzji. Przechowywanie tych elementów wyłącznie w sklepie lub w rozproszonych katalogach utrudni kontrolę wersji, audyt i automatyzację.

## Decyzja

Repozytorium `dejvid673-prog/repetytorium` jest głównym źródłem prawdy dla całego projektu Repetytorium Staw Expert.

PrestaShop jest docelową warstwą publikacji i prezentacji. Zmiany wykonane bezpośrednio w PrestaShop muszą zostać zsynchronizowane z repozytorium, zanim zostaną uznane za trwałe.

## Konsekwencje

- decyzje i zmiany mają historię;
- agenci otrzymują jedno miejsce orientacji;
- materiały muszą mieć ustalone formaty;
- potrzebny będzie proces synchronizacji i wykrywania rozbieżności;
- sekretów i danych klientów nie wolno zapisywać w repozytorium.
