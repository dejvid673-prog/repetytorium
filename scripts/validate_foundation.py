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
    phase_match = re.match(r"(\\d+)", phase)
    phase_number = int(phase_match.group(1)) if phase_match else None
    for raw in (part.strip() for part in spec.split(",")):
        if raw == phase:
            return True
        if raw.endswith("+") and raw[:-1].isdigit() and phase_number is not None:
            if phase_number >= int(raw[:-1]):
                return True
        range_match = re.fullmatch(r"(\\d+)-(\\d+)", raw)
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
if "READY_IF_" in cases:
    fail("A00 tests use non-canonical conditional statuses")
if 'mode: "validation"' not in cases:
    fail("A00 tests do not declare validation mode")

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

source_template = read("templates/SOURCE_MATERIAL_INTAKE.yaml")
for expected in [
    "public_repository_acknowledged: true",
    "contains_personal_data: false",
    "contains_secrets: false",
]:
    if expected not in source_template:
        fail(f"source intake template missing safety invariant: {expected}")

context = read("PROJECT_CONTEXT.yaml")
for expected in ['version: "0.3"', 'A00: "audit_pending"']:
    if expected not in context:
        fail(f"context manifest missing {expected}")

print(f"agents={len(agents)} work_packages={len(work_packages)} gates={len(gates)}")
for warning in warnings:
    print(f"WARNING: {warning}")
for error in errors:
    print(f"ERROR: {error}")
if errors:
    print(f"VALIDATION FAILED: {len(errors)} error(s)")
    sys.exit(1)
print("VALIDATION PASSED")
