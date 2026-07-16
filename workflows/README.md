# Workflow

Katalog przechowuje wykonywalne i opisowe procesy przekazywania pracy pomiędzy agentami.

Każdy workflow określa:

- wyzwalacz;
- wejście;
- kolejne role;
- bramy jakości;
- obsługę błędów;
- statusy;
- wymagane zatwierdzenia;
- wyjście;
- możliwość wznowienia i wycofania.

## Pierwszy workflow

`project-control.yaml` steruje przyjęciem polecenia, analizą wpływu, decyzją, blokadą, wznowieniem, wykonaniem, audytem i zamknięciem. Nie aktywuje sam agentów ani faz.
