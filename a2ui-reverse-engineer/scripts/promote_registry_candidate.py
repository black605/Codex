#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone
from a2ui_compiler_common import PREREQUISITE_GATES, clone, example_ir, load_json, write_json
from compile_contract_bundle import compile_bundle
from validate_registry_candidate import validate


def promote(candidate, approval):
    errors = validate(candidate)
    gates = {item.get("gateId"): item.get("status") for item in candidate.get("gateResults", [])}
    for gate in ("RuntimeGate", "VisualGate"):
        if gates.get(gate) != "passed":
            errors.append(f"promotion gate not passed: {gate}")
    if not approval.get("reviewer") or not approval.get("approvedAt") or approval.get("sourceHash") != candidate.get("sourceHash"):
        errors.append("approval must contain reviewer, approvedAt and matching sourceHash")
    if errors:
        raise ValueError("; ".join(errors))
    result = clone(candidate)
    result["status"] = "active"
    result["promotion"] = {"reviewer": approval["reviewer"], "approvedAt": approval["approvedAt"], "sourceHash": approval["sourceHash"], "policy": "new-file-only"}
    for component in result.get("components", []):
        component["status"] = "active"
    return result


def main():
    parser = argparse.ArgumentParser(description="Promote a validated registry candidate into a new active registry document")
    parser.add_argument("candidate", nargs="?")
    parser.add_argument("approval", nargs="?")
    parser.add_argument("output", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        candidate = compile_bundle(example_ir())["registry-candidate.json"]
        approval = {"reviewer": "self-test", "approvedAt": datetime.now(timezone.utc).isoformat(), "sourceHash": candidate["sourceHash"]}
        result = promote(candidate, approval)
        assert result["status"] == "active" and result["promotion"]["policy"] == "new-file-only"
        print("PASS: registry promotion self-test")
        return
    if not args.candidate or not args.approval or not args.output:
        parser.error("candidate, approval and output are required")
    candidate_path = str(args.candidate)
    output_path = str(args.output)
    if candidate_path == output_path:
        raise SystemExit("ERROR: in-place registry promotion is forbidden")
    write_json(output_path, promote(load_json(candidate_path), load_json(args.approval)))
    print(f"PASS: promoted registry written to new file {output_path}")


if __name__ == "__main__":
    main()
