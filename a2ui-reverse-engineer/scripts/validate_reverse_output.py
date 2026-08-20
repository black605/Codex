#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

TOKEN_RE = re.compile(r"^component\.a2-[a-z0-9-]+\.[a-z0-9-]+\.[a-z0-9-]+\.[a-z0-9-]+$")
BASE_RE = re.compile(r"^a2-[a-z0-9]+(?:-[a-z0-9]+)*$")
SLOT_RE = re.compile(r"^slot-[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_slot(slot, parent_level, seen, errors, path):
    level = slot.get("level")
    slot_id = slot.get("slotId", "")
    if not SLOT_RE.fullmatch(slot_id):
        errors.append(f"{path}.slotId is invalid: {slot_id}")
    if slot_id in seen:
        errors.append(f"duplicate slotId: {slot_id}")
    seen.add(slot_id)
    if level not in (1, 2, 3):
        errors.append(f"{path}.level must be 1, 2 or 3")
    if parent_level is not None and level != parent_level + 1:
        errors.append(f"{path} skips slot hierarchy")
    children = slot.get("children", [])
    if level == 3 and children:
        errors.append(f"{path} level-3 slot cannot have children")
    if slot.get("min", 0) > slot.get("max", 0):
        errors.append(f"{path} min exceeds max")
    for index, child in enumerate(children):
        validate_slot(child, level, seen, errors, f"{path}.children[{index}]")


def main():
    parser = argparse.ArgumentParser(description="Validate an A2UI reverse-engineering output package")
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    document = json.loads(args.input.read_text(encoding="utf-8"))
    errors = []
    required = ["runId", "projectId", "sourceRef", "sourceHash", "status", "observationsRef", "sheetA", "sheetB", "gateResults", "issues"]
    for key in required:
        if key not in document:
            errors.append(f"missing top-level field: {key}")
    if not re.fullmatch(r"[a-fA-F0-9]{64}", document.get("sourceHash", "")):
        errors.append("sourceHash must be a SHA-256 hex digest")
    seen_slots = set()
    for index, component in enumerate(document.get("sheetA", [])):
        for field in ("componentId", "baseClass"):
            if not BASE_RE.fullmatch(component.get(field, "")):
                errors.append(f"sheetA[{index}].{field} must use the a2- base convention")
        if not component.get("sourceObservationIds"):
            errors.append(f"sheetA[{index}] has no sourceObservationIds")
        for slot_index, slot in enumerate(component.get("slots", [])):
            validate_slot(slot, None, seen_slots, errors, f"sheetA[{index}].slots[{slot_index}]")
    for index, token in enumerate(document.get("sheetB", [])):
        if not TOKEN_RE.fullmatch(token.get("tokenName", "")):
            errors.append(f"sheetB[{index}].tokenName is not five-segment A2UI naming")
        if not token.get("sourceObservationIds"):
            errors.append(f"sheetB[{index}] has no sourceObservationIds")
        confidence = token.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"sheetB[{index}].confidence must be between 0 and 1")
    prerequisite_gates = {"ReverseSchemaGate", "SlotGate", "TokenGate", "RegistryGate"}
    if document.get("renderSpec") and any(gate.get("status") != "passed" for gate in document.get("gateResults", []) if gate.get("gateId") in prerequisite_gates):
        errors.append("renderSpec exists before all prerequisite gates passed")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {args.input} contains {len(document.get('sheetA', []))} components and {len(document.get('sheetB', []))} tokens")


if __name__ == "__main__":
    main()
