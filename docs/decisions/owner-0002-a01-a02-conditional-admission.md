# OWNER-0002: Warunkowe dopuszczenie A01 i A02

Status: accepted  
Data: 2026-07-16  
Decydent: właściciel projektu  
Polecenie źródłowe: przeprowadzić pełny audyt i dopuszczenie A01 oraz A02 w draft PR #1

## Decyzja

Właściciel przyjmuje wyniki pełnych audytów kontraktów 0.2 i dopuszcza A01 oraz A02 warunkowo do zwykłych, ograniczonych audytów agentów i mechanizmów projektu.

Status `active` nie zostaje nadany. Testy wykonano na danych syntetycznych w jednej głównej sesji projektu, bez niezależnych sesji agentów krzyżowych. Ograniczenie jest jawne i nie może zostać pominięte w kolejnych raportach.

## A01 — dozwolony zakres

- `agent_context_and_governance_audit`;
- `task_context_gate_review`;
- `instruction_conflict_analysis`;
- `change_request_governance_review`;
- `state_consistency_governance_review`.

## A02 — dozwolony zakres

- `agent_workflow_and_test_audit`;
- `workflow_state_machine_audit`;
- `schema_template_fixture_audit`;
- `skill_permission_and_invocation_audit`;
- `validation_claim_audit`.

## Wspólne zakazy

A01 i A02 nie mogą:

- zatwierdzać własnych kontraktów, testów ani wyników;
- edytować badanego elementu w tej samej karcie audytu;
- wykonywać pracy domenowej lub zastępować innych audytorów;
- samodzielnie aktywować agentów albo zmieniać stan kanoniczny;
- scalać do `main`, publikować ani wdrażać.

## Warunki utrzymania dopuszczenia

- każde zadanie pochodzi od A00 i ma zamrożone wejścia, kryteria oraz rozdzielone role;
- ustalenie wysokie lub krytyczne zawiesza dopuszczenie w dotkniętym zakresie;
- zmiana kontraktu, zakresu, narzędzi lub modelu przekazania wymaga ponownego audytu;
- pierwszy zwykły audyt każdego agenta jest obserwowanym testem operacyjnym;
- przed statusem `active` wymagany jest niezależny audyt krzyżowy w osobnej sesji lub równoważnym, udokumentowanym środowisku.

## Dowody

- `reports/agent-audits/A01/2026-07-16-full-audit-v0.2.md`;
- `reports/agent-audits/A02/2026-07-16-full-audit-v0.2.md`;
- `reports/tests/A01/2026-07-16-validation-results-v0.2.yaml`;
- `reports/tests/A02/2026-07-16-validation-results-v0.2.yaml`.

