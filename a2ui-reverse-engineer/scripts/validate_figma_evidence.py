#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

HASH_RE = re.compile(r"^[a-fA-F0-9]{64}$")
NODE_RE = re.compile(r"^[0-9]+[:-][0-9]+$")
REQUIRED_ARTIFACTS = ("designContext", "screenshot", "variables", "codeConnect", "assets")


def validate(document):
    errors = []
    if document.get("schemaVersion") != "1.0.0":
        errors.append("schemaVersion must be 1.0.0")
    if not document.get("runId"):
        errors.append("runId is required")
    source = document.get("source", {})
    if not str(source.get("url", "")).startswith(("https://figma.com/design/", "https://www.figma.com/design/")):
        errors.append("source.url must be a Figma design URL")
    if not source.get("fileKey"):
        errors.append("source.fileKey is required")
    if not NODE_RE.fullmatch(str(source.get("nodeId", ""))):
        errors.append("source.nodeId must be an explicit numeric node id")
    if source.get("tool") != "figma-mcp":
        errors.append("source.tool must be figma-mcp")
    artifacts = document.get("artifacts", {})
    for name in REQUIRED_ARTIFACTS:
        artifact = artifacts.get(name)
        if not isinstance(artifact, dict):
            errors.append(f"artifacts.{name} is required")
            continue
        if not artifact.get("artifactRef"):
            errors.append(f"artifacts.{name}.artifactRef is required")
        if not HASH_RE.fullmatch(str(artifact.get("sha256", ""))):
            errors.append(f"artifacts.{name}.sha256 must be a SHA-256 digest")
        if artifact.get("status") not in {"captured", "persisted", "missing", "needs-review"}:
            errors.append(f"artifacts.{name}.status is invalid")
        if artifact.get("temporarySource") and artifact.get("status") == "persisted":
            errors.append(f"artifacts.{name} cannot be both temporary and persisted")
    gate = document.get("gate", {})
    if gate.get("gateId") != "FigmaSourceGate":
        errors.append("gate.gateId must be FigmaSourceGate")
    if gate.get("status") == "passed":
        unresolved = [name for name in REQUIRED_ARTIFACTS if artifacts.get(name, {}).get("status") not in {"captured", "persisted"}]
        if unresolved:
            errors.append(f"FigmaSourceGate cannot pass with unresolved artifacts: {', '.join(unresolved)}")
        if gate.get("issues"):
            errors.append("FigmaSourceGate cannot pass while issues are present")
    return errors


def self_test():
    digest = "a" * 64
    artifact = {"artifactRef": "figma/example.json", "sha256": digest, "status": "persisted"}
    example = {
        "schemaVersion": "1.0.0",
        "runId": "figma-self-test",
        "source": {"url": "https://www.figma.com/design/file/example?node-id=1-2", "fileKey": "file", "nodeId": "1:2", "capturedAt": "2026-08-17T00:00:00Z", "tool": "figma-mcp"},
        "artifacts": {name: dict(artifact) for name in REQUIRED_ARTIFACTS},
        "gate": {"gateId": "FigmaSourceGate", "status": "passed", "checks": ["self-test"], "issues": []},
    }
    errors = validate(example)
    if errors:
        raise AssertionError("; ".join(errors))
    print("PASS: Figma evidence validator self-test")


def main():
    parser = argparse.ArgumentParser(description="Validate an A2UI Figma evidence package")
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.input:
        parser.error("input is required unless --self-test is used")
    document = json.loads(args.input.read_text(encoding="utf-8"))
    errors = validate(document)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {args.input} is a valid Figma evidence package")


if __name__ == "__main__":
    main()
