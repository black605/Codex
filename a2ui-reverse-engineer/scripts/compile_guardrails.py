#!/usr/bin/env python3
import argparse
from a2ui_compiler_common import example_ir, load_json, write_json


def compile_component(component):
    rules = component.get("guardrails", {})
    selector = f'[data-component="{component["componentId"]}"][data-variant="{component["variant"]}"]'
    css = []
    runtime = {"componentId": component["componentId"], "variant": component["variant"], "checks": {}}
    if rules.get("prefixShrink") is False:
        css.append(f'{selector} [data-slot-role="prefix"]{{flex-shrink:0}}')
    if rules.get("actionShrink") is False:
        css.append(f'{selector} [data-slot-role="action"]{{flex-shrink:0}}')
    if rules.get("mainMinWidth") == 0:
        css.append(f'{selector} [data-slot-role="main"]{{min-width:0;flex:1}}')
    if isinstance(rules.get("titleMaxLines"), int):
        lines = rules["titleMaxLines"]
        css.append(f'{selector} [data-slot-role="title"]{{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:{lines};overflow:hidden}}')
        runtime["checks"]["titleMaxLines"] = lines
    if rules.get("minHeight"):
        css.append(f'{selector}{{min-height:{rules["minHeight"]}}}')
    if rules.get("overflowPolicy") in {"clip", "hidden"}:
        css.append(f'{selector}{{overflow:{rules["overflowPolicy"]}}}')
    if rules.get("emptySlotPolicy") == "collapse":
        css.append(f'{selector} [data-empty-policy="collapse"]:empty{{display:none}}')
    runtime["checks"]["emptySlotPolicy"] = rules.get("emptySlotPolicy", "preserve")
    return {"componentId": component["componentId"], "variant": component["variant"], "cssRules": css, "runtimeRules": runtime}


def compile_document(document):
    return {"schemaVersion": "1.0.0", "runId": document.get("runId"), "components": [compile_component(item) for item in document.get("components", [])]}


def main():
    parser = argparse.ArgumentParser(description="Compile A2UI guardrails")
    parser.add_argument("input", nargs="?")
    parser.add_argument("output", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = compile_document(example_ir())
        assert any("min-width:0;flex:1" in rule for rule in result["components"][0]["cssRules"])
        assert all("[data-slot]:empty" not in rule for rule in result["components"][0]["cssRules"])
        print("PASS: guardrail compiler self-test")
        return
    if not args.input or not args.output:
        parser.error("input and output are required")
    write_json(args.output, compile_document(load_json(args.input)))
    print(f"PASS: guardrails written to {args.output}")


if __name__ == "__main__":
    main()
