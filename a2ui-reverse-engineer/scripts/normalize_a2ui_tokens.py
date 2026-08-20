#!/usr/bin/env python3
import argparse
from a2ui_compiler_common import TOKEN_RE, clone, css_variable, example_ir, load_json, snap_px, write_json


def normalize(document):
    result = clone(document)
    errors = []
    for component in result.get("components", []):
        for token in component.get("tokens", []):
            name = token.get("tokenName", "")
            if not TOKEN_RE.fullmatch(name):
                errors.append(f"invalid tokenName: {name}")
                continue
            category = token.get("category")
            policy = "spacing-4px" if category == "spacing" else "radius-4px" if category == "radius" else "none"
            token["snapPolicy"] = token.get("snapPolicy", policy)
            token["compiledValue"] = snap_px(token.get("rawValue")) if token["snapPolicy"] in {"spacing-4px", "radius-4px"} else token.get("rawValue")
            token["cssVariable"] = css_variable(name)
            token.setdefault("semanticRef", None)
    return result, errors


def main():
    parser = argparse.ArgumentParser(description="Normalize Canonical A2UI IR tokens")
    parser.add_argument("input", nargs="?")
    parser.add_argument("output", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result, errors = normalize(example_ir())
        assert not errors and result["components"][0]["tokens"][0]["compiledValue"] == "16px"
        print("PASS: token normalizer self-test")
        return
    if not args.input or not args.output:
        parser.error("input and output are required")
    result, errors = normalize(load_json(args.input))
    if errors:
        raise SystemExit("\n".join(errors))
    write_json(args.output, result)
    print(f"PASS: normalized tokens written to {args.output}")


if __name__ == "__main__":
    main()
