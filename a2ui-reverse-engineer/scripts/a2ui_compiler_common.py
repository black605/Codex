import copy
import json
import re
from pathlib import Path

TOKEN_RE = re.compile(r"^component\.a2-[a-z0-9-]+\.[a-z0-9-]+\.[a-z0-9-]+\.[a-z0-9-]+$")
BASE_RE = re.compile(r"^a2-[a-z0-9]+(?:-[a-z0-9]+)*$")
PX_RE = re.compile(r"^(-?\d+(?:\.\d+)?)px$")
PREREQUISITE_GATES = {
    "ReverseSchemaGate", "SlotGate", "TokenNormalizationGate", "GuardrailGate",
    "ContractEquivalenceGate", "RegistryCandidateGate", "RuntimeGate", "VisualGate",
}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def css_variable(token_name):
    return "--" + token_name.replace(".", "-")


def snap_px(value, step=4):
    match = PX_RE.fullmatch(str(value).strip())
    if not match:
        return value
    snapped = float(round(float(match.group(1)) / step) * step)
    return f"{int(snapped) if snapped.is_integer() else snapped}px"


def example_ir():
    return {
        "schemaVersion": "1.0.0", "runId": "self-test", "projectId": "test", "sourceHash": "a" * 64,
        "components": [{
            "componentId": "a2-card", "baseClass": "a2-card", "version": "1.0.0", "variant": "info",
            "source": {"sourceObservationIds": ["obs-1"], "confidence": 0.99, "status": "approved"},
            "slots": [{"slotId": "slot-card", "level": 1, "min": 1, "max": 1, "accepts": ["component"], "emptyPolicy": "preserve", "children": []}],
            "props": {"title": {"type": "string", "required": True}},
            "tokens": [{"tokenName": "component.a2-card.info.container.padding-inline", "category": "spacing", "rawValue": "15.3px", "sourceObservationIds": ["obs-1"], "confidence": 0.9, "status": "approved"}],
            "guardrails": {"prefixShrink": False, "mainMinWidth": 0, "titleMaxLines": 2, "minHeight": "120px", "emptySlotPolicy": "collapse", "overflowPolicy": "clip"},
            "actions": [], "implementation": {"react": "registry://a2-card/info"}, "status": "visual-validated"
        }],
        "gateResults": [{"gateId": gate, "status": "passed", "issues": []} for gate in sorted(PREREQUISITE_GATES)]
    }


def clone(value):
    return copy.deepcopy(value)
