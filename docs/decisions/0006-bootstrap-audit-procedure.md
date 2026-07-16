# ADR-0006: Ograniczony bootstrap audytu agentów

Status: accepted  
Data: 2026-07-16

## Kontekst

Wszystkie role, w tym A00, A01 i A80, otrzymały początkowo status `audit_pending`. Jednocześnie system zabraniał agentowi z takim statusem wykonywania audytu. Powstała zależność kołowa uniemożliwiająca rozpoczęcie WP-0006.

A80 jest technicznym audytorem PrestaShop i nie powinien rozszerzać swojej roli na audyt skilli oraz workflow zarządczych.

## Decyzja

- w Fazie 0 obowiązuje ograniczona procedura z `docs/BOOTSTRAP_GOVERNANCE.md`;
- A01 może działać warunkowo wyłącznie jako audytor kontekstu;
- powstaje A02 — Audytor Workflow, Skilli i Schematów;
- A02 zastępuje A80 w audycie mechanizmów A00;
- właściciel podejmuje końcową decyzję o dopuszczeniu A00;
- A80 zachowuje odpowiedzialność za techniczne QA środowiska i modułu;
- tryb bootstrap nie daje prawa do pracy wykonawczej ani publikacji.

## Konsekwencje

System może rozpocząć kontrolowany audyt bez pozornego aktywowania wszystkich agentów. Zakres audytorów pozostaje wąski, a wyjątek wygasa po dopuszczeniu A00.
