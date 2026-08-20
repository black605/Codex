#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from a2ui_compiler_common import example_ir, load_json, write_json
from compile_guardrails import compile_document
from normalize_a2ui_tokens import normalize


TYPE_MAP = {"string": "string", "number": "number", "boolean": "boolean", "array": "unknown[]", "object": "Record<string, unknown>"}


def prop_schema(props):
    properties = {}
    required = []
    for name, spec in props.items():
        properties[name] = {"type": spec.get("type", "string")}
        if spec.get("required"):
            required.append(name)
    return {"type": "object", "additionalProperties": False, "properties": properties, "required": required}


def compile_bundle(document):
    normalized, errors = normalize(document)
    if errors:
        raise ValueError("; ".join(errors))
    schemas = {}
    registry = []
    type_blocks = []
    tokens = []
    for component in normalized.get("components", []):
        key = f'{component["componentId"]}:{component["variant"]}'
        schema = prop_schema(component.get("props", {}))
        schemas[key] = schema
        interface = "".join(part.capitalize() for part in component["componentId"].split("-")) + "Props"
        fields = [f'  {name}{"" if spec.get("required") else "?"}: {TYPE_MAP.get(spec.get("type"), "unknown")};' for name, spec in component.get("props", {}).items()]
        type_blocks.append(f'export interface {interface} {{\n' + "\n".join(fields) + "\n}")
        registry.append({"componentId": component["componentId"], "variant": component["variant"], "version": component["version"], "implementation": component["implementation"], "propsSchemaRef": f"schemas.json#/{key}", "toolSchemaRef": f"tool-schemas.json#/{key}", "status": "compiled", "sourceHash": normalized["sourceHash"]})
        tokens.extend(component.get("tokens", []))
    return {
        "types.ts": "\n\n".join(type_blocks) + "\n",
        "schemas.json": schemas,
        "tool-schemas.json": schemas,
        "tokens.json": {"schemaVersion": "1.0.0", "tokens": tokens},
        "guardrails.json": compile_document(normalized),
        "registry-candidate.json": {"schemaVersion": "1.0.0", "runId": normalized["runId"], "projectId": normalized["projectId"], "sourceHash": normalized["sourceHash"], "status": "compiled", "components": registry, "gateResults": normalized.get("gateResults", [])},
    }


def write_bundle(output, bundle):
    target = Path(output)
    target.mkdir(parents=True, exist_ok=True)
    for name, value in bundle.items():
        path = target / name
        if isinstance(value, str):
            path.write_text(value, encoding="utf-8")
        else:
            write_json(path, value)


def main():
    parser = argparse.ArgumentParser(description="Compile Canonical A2UI IR into an equivalent contract bundle")
    parser.add_argument("input", nargs="?")
    parser.add_argument("output", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        bundle = compile_bundle(example_ir())
        assert bundle["schemas.json"] == bundle["tool-schemas.json"]
        assert bundle["registry-candidate.json"]["status"] == "compiled"
        print("PASS: contract bundle compiler self-test")
        return
    if not args.input or not args.output:
        parser.error("input and output are required")
    write_bundle(args.output, compile_bundle(load_json(args.input)))
    print(f"PASS: contract bundle written to {args.output}")


if __name__ == "__main__":
    main()
