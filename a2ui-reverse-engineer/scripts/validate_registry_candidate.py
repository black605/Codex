#!/usr/bin/env python3
import argparse
from a2ui_compiler_common import BASE_RE, PREREQUISITE_GATES, example_ir, load_json
from compile_contract_bundle import compile_bundle


def validate(candidate):
    errors = []
    seen = set()
    if candidate.get("status") not in {"compiled", "runtime-validated", "visual-validated"}:
        errors.append("registry candidate status is not promotable")
    for component in candidate.get("components", []):
        key = (component.get("componentId"), component.get("variant"))
        if key in seen:
            errors.append(f"duplicate component variant: {key}")
        seen.add(key)
        if not BASE_RE.fullmatch(str(component.get("componentId", ""))):
            errors.append(f"invalid componentId: {component.get('componentId')}")
        if not str(component.get("implementation", {}).get("react", "")).startswith("registry://"):
            errors.append(f"unresolved implementation: {key}")
        for ref in (component.get("propsSchemaRef"), component.get("toolSchemaRef")):
            if not ref or "#" not in ref:
                errors.append(f"invalid schema reference for {key}: {ref}")
    gates = {item.get("gateId"): item.get("status") for item in candidate.get("gateResults", [])}
    for gate in PREREQUISITE_GATES - {"RuntimeGate", "VisualGate"}:
        if gates.get(gate) != "passed":
            errors.append(f"prerequisite gate not passed: {gate}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate an A2UI staging registry candidate")
    parser.add_argument("input", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        candidate = compile_bundle(example_ir())["registry-candidate.json"]
        assert not validate(candidate)
        candidate["components"].append(dict(candidate["components"][0]))
        assert any("duplicate" in item for item in validate(candidate))
        print("PASS: registry candidate validator self-test")
        return
    if not args.input:
        parser.error("input is required")
    errors = validate(load_json(args.input))
    if errors:
        raise SystemExit("\n".join(f"ERROR: {item}" for item in errors))
    print(f"PASS: {args.input} is a valid staging registry candidate")


if __name__ == "__main__":
    main()
