#!/usr/bin/env python3
"""Dependency-free structural validation for the Repetytorium foundation."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        fail(f"missing file: {path}")
        return ""
    return p.read_text(encoding="utf-8")


required_files = [
    "PROJECT_CONTEXT.yaml",
    "PROJECT_INSTRUCTIONS.md",
    "docs/BOOTSTRAP_GOVERNANCE.md",
    "agents/A00-project-manager/OPERATING_PROTOCOL.md",
    "schemas/a00-control-record.schema.json",
    "templates/A00_CONTROL_RECORD.yaml",
    "docs/decisions/owner-0001-a00-conditional-admission.md",
    "docs/decisions/owner-0002-a01-a02-conditional-admission.md",
    "docs/decisions/owner-0003-read-only-codex-discovery.md",
    "docs/CODEX_READ_ONLY_RESEARCH_BACKLOG.md",
    "agents/A01-context-governance-auditor/AGENT.md",
    "agents/A02-workflow-schema-auditor/AGENT.md",
    "tests/agents/A01/cases.yaml",
    "tests/agents/A02/cases.yaml",
    "reports/agent-audits/A01/2026-07-16-full-audit-v0.2.md",
    "reports/agent-audits/A02/2026-07-16-full-audit-v0.2.md",
    "reports/tests/A01/2026-07-16-validation-results-v0.2.yaml",
    "reports/tests/A02/2026-07-16-validation-results-v0.2.yaml",
    "reports/control/CTRL-0002-a01-a02-admission.yaml",
    "reports/control/CTRL-0003-read-only-codex-discovery.yaml",
    "registries/agents.yaml",
    "registries/work-packages.yaml",
    "registries/phase-gates.yaml",
    "registries/decisions.yaml",
    "schemas/project-task.schema.json",
    "schemas/source-material-intake.schema.json",
    "workflows/project-control.yaml",
    "workflows/source-material-intake.yaml",
]
for item in required_files:
    read(item)

for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

for registry in [
    "registries/agents.yaml",
    "registries/work-packages.yaml",
    "registries/phase-gates.yaml",
    "registries/branches.yaml",
    "registries/decisions.yaml",
]:
    if not re.search(r"^state_revision: [0-9]+$", read(registry), re.MULTILINE):
        fail(f"registry missing state_revision: {registry}")

for path in list(ROOT.rglob("*.yaml")) + list(ROOT.rglob("*.yml")):
    text = path.read_text(encoding="utf-8")
    if "\t" in text:
        fail(f"tab character in YAML {path.relative_to(ROOT)}")
    if "\r" in text:
        warnings.append(f"CRLF in YAML {path.relative_to(ROOT)}")

agents_text = read("registries/agents.yaml")
agent_blocks = re.split(r"\n  - id: ", agents_text)[1:]
agents: dict[str, str] = {}
statuses: dict[str, str] = {}
for block in agent_blocks:
    match_id = re.match(r"(A\d{2})", block)
    phase = re.search(r'\n    phases: "([^"]+)"', block)
    status = re.search(r"\n    status: ([a-z_]+)", block)
    if not match_id or not phase or not status:
        fail("malformed agent registry block")
        continue
    agent_id = match_id.group(1)
    if agent_id in agents:
        fail(f"duplicate agent: {agent_id}")
    agents[agent_id] = phase.group(1)
    statuses[agent_id] = status.group(1)

if len(agents) != 28:
    fail(f"expected 28 agents, found {len(agents)}")


def phase_allowed(spec: str, phase: str) -> bool:
    if spec == "all":
        return True
    phase_match = re.match(r"(\d+)", phase)
    phase_number = int(phase_match.group(1)) if phase_match else None
    for raw in (part.strip() for part in spec.split(",")):
        if raw == phase:
            return True
        if raw.endswith("+") and raw[:-1].isdigit() and phase_number is not None:
            if phase_number >= int(raw[:-1]):
                return True
        range_match = re.fullmatch(r"(\d+)-(\d+)", raw)
        if range_match and phase_number is not None:
            lo, hi = map(int, range_match.groups())
            if lo <= phase_number <= hi:
                return True
    return False


wp_text = read("registries/work-packages.yaml")
wp_blocks = re.split(r'\n  - id: "', wp_text)[1:]
work_packages: dict[str, dict[str, str]] = {}
for block in wp_blocks:
    wp_id_match = re.match(r'(WP-\d+)"', block)
    phase = re.search(r'\n    phase: "([^"]+)"', block)
    owner = re.search(r'\n    owner_agent: "([^"]+)"', block)
    status = re.search(r'\n    status: "([^"]+)"', block)
    if not wp_id_match or not phase or not owner or not status:
        fail("malformed work package block")
        continue
    wp_id = wp_id_match.group(1)
    if wp_id in work_packages:
        fail(f"duplicate work package: {wp_id}")
    work_packages[wp_id] = {
        "phase": phase.group(1),
        "owner": owner.group(1),
        "status": status.group(1),
    }

gate_text = read("registries/phase-gates.yaml")
gates = set(re.findall(r"\n  - id: (G[A-Z0-9_]+)", gate_text))
special_dependencies = {"OWNER_LAUNCH_APPROVAL", "OWNER_CASE_LIBRARY_DECISION", "G2_CONTENT_SAMPLE"}
for wp_id, data in work_packages.items():
    owner = data["owner"]
    if owner != "OWNER" and owner not in agents:
        fail(f"{wp_id} has unknown owner {owner}")
    if owner in agents and not phase_allowed(agents[owner], data["phase"]):
        fail(f"{wp_id} phase {data['phase']} outside {owner} scope {agents[owner]}")

for dependency in re.findall(r'"(WP-\d+|G[A-Z0-9_]+|OWNER_[A-Z0-9_]+)"', wp_text):
    if dependency.startswith("WP-") and dependency not in work_packages:
        fail(f"unknown work package dependency: {dependency}")
    if dependency.startswith("G") and dependency not in gates and dependency not in special_dependencies:
        fail(f"unknown gate dependency: {dependency}")

workflow = read("workflows/project-control.yaml")
state_section = workflow.split("states:", 1)[1].split("transitions:", 1)[0] if "states:" in workflow else ""
states = set(re.findall(r"^  - ([A-Z_]+)$", state_section, re.MULTILINE))
for field, state in re.findall(r"^    (from|to): ([A-Z_]+)$", workflow, re.MULTILINE):
    if state not in states:
        fail(f"workflow transition uses unknown state {state} in {field}")
if "CANCELLED" not in states or "to: CANCELLED" not in workflow:
    fail("workflow has no usable cancellation path")
if "runtime_implemented: false" not in workflow:
    fail("declarative workflow must disclose missing runtime")

cases = read("tests/agents/A00/cases.yaml")
case_count = len(re.findall(r'^  - id: "A00-T[0-9]+"$', cases, re.MULTILINE))
if case_count != 15:
    fail(f"expected 15 A00 test cases, found {case_count}")
if "READY_IF_" in cases:
    fail("A00 tests use non-canonical conditional statuses")
if 'mode: "validation"' not in cases:
    fail("A00 tests do not declare validation mode")

for agent_id, expected_count in [("A01", 6), ("A02", 6)]:
    audit_cases = read(f"tests/agents/{agent_id}/cases.yaml")
    case_count = len(re.findall(rf'^  - id: "{agent_id}-T[0-9]+"$', audit_cases, re.MULTILINE))
    if case_count != expected_count:
        fail(f"expected {expected_count} {agent_id} test cases, found {case_count}")
    if 'mode: "validation"' not in audit_cases:
        fail(f"{agent_id} tests do not declare validation mode")

skill_policy = read("skills/coordinate-repetytorium/agents/openai.yaml")
if "allow_implicit_invocation: false" not in skill_policy:
    fail("A00 skill implicit invocation must remain disabled before admission")

schema = json.loads(read("schemas/project-task.schema.json") or "{}")
required = set(schema.get("required", []))
template = read("templates/TASK_BRIEF.yaml")
template_keys = set(re.findall(r"^([a-z_]+):", template, re.MULTILINE))
missing_template_keys = sorted(required - template_keys)
if missing_template_keys:
    fail(f"task template missing schema keys: {missing_template_keys}")

control_schema = json.loads(read("schemas/a00-control-record.schema.json") or "{}")
control_required = set(control_schema.get("required", []))
control_template = read("templates/A00_CONTROL_RECORD.yaml")
control_template_keys = set(re.findall(r"^([a-z_]+):", control_template, re.MULTILINE))
missing_control_keys = sorted(control_required - control_template_keys)
if missing_control_keys:
    fail(f"A00 control template missing schema keys: {missing_control_keys}")

for invariant in ["one active task per conflict_key", "state mutations are revisioned and atomic", "missing specialist never expands A00 role"]:
    if invariant not in workflow:
        fail(f"A00 workflow missing invariant: {invariant}")

source_template = read("templates/SOURCE_MATERIAL_INTAKE.yaml")
for expected in [
    "public_repository_acknowledged: true",
    "contains_personal_data: false",
    "contains_secrets: false",
]:
    if expected not in source_template:
        fail(f"source intake template missing safety invariant: {expected}")

context = read("PROJECT_CONTEXT.yaml")
for expected in [
    'version: "0.3"',
    'A00: "pass_conditional"',
    'A01: "pass_conditional"',
    'A02: "pass_conditional"',
    'assurance_roles_decision: "OWNER-0002"',
    'bootstrap_status: "closed_after_A00_admission"',
    'decision: "OWNER-0003"',
    'codex_repository_access: "read_only"',
    'codex_mutations_allowed: false',
]:
    if expected not in context:
        fail(f"context manifest missing {expected}")

for expected in [
    'contract_version: "0.4"',
    'contract_version: "0.2"',
    'agent_context_and_governance_audit',
    'agent_workflow_and_test_audit',
    'admission_decision: "OWNER-0002"',
]:
    if expected not in agents_text:
        fail(f"agent registry missing admission invariant: {expected}")

for wp_id in ["WP-0001", "WP-0002", "WP-0003", "WP-0004", "WP-0005", "WP-0006", "WP-0007", "WP-0010"]:
    if work_packages.get(wp_id, {}).get("status") != "COMPLETED":
        fail(f"{wp_id} must be COMPLETED after A01/A02 admission")
if work_packages.get("WP-0011", {}).get("status") != "BLOCKED":
    fail("WP-0011 must remain BLOCKED until DISC-001 and executor assignment are complete")

decisions = read("registries/decisions.yaml")
for decision_id in ["OWNER-0002", "OWNER-0003"]:
    if f'id: "{decision_id}"' not in decisions:
        fail(f"decision registry missing {decision_id}")

current_state = read("docs/CURRENT_STATE.md")
for expected in ["Wersja stanu: 6", "Codex poboczny", "WP-0011: `BLOCKED`", "DISC-001"]:
    if expected not in current_state:
        fail(f"current state missing {expected}")

research_backlog = read("docs/CODEX_READ_ONLY_RESEARCH_BACKLOG.md")
for expected in [
    "tryb tylko do odczytu",
    "Codex nie może:",
    "DISC-001",
    "DISC-005",
    "DISC-012",
    "nie wykonano żadnej zmiany w repozytorium",
]:
    if expected not in research_backlog:
        fail(f"Codex research backlog missing invariant: {expected}")
if len(re.findall(r"^### DISC-[0-9]{3} ", research_backlog, re.MULTILINE)) != 15:
    fail("Codex research backlog must define 15 primary DISC tasks")

print(f"agents={len(agents)} work_packages={len(work_packages)} gates={len(gates)}")
for warning in warnings:
    print(f"WARNING: {warning}")
for error in errors:
    print(f"ERROR: {error}")
if errors:
    print(f"VALIDATION FAILED: {len(errors)} error(s)")
    sys.exit(1)
print("VALIDATION PASSED")
