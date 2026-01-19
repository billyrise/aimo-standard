import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = ROOT / "schemas" / "jsonschema"

def load_schema(name: str) -> dict:
    p = SCHEMAS_DIR / name
    return json.loads(p.read_text(encoding="utf-8"))

def make_resolver():
    store = {
        "aimo-standard.schema.json": load_schema("aimo-standard.schema.json"),
        "aimo-dictionary.schema.json": load_schema("aimo-dictionary.schema.json"),
        "aimo-ev.schema.json": load_schema("aimo-ev.schema.json"),
    }
    # Allow relative $ref like "aimo-dictionary.schema.json"
    return RefResolver.from_schema(store["aimo-standard.schema.json"], store=store)

def validate_json(payload: dict) -> None:
    schema = load_schema("aimo-standard.schema.json")
    resolver = make_resolver()
    validator = Draft202012Validator(schema, resolver=resolver)
    errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
    if errors:
        msgs = []
        for e in errors[:50]:
            path = ".".join([str(x) for x in e.path]) if e.path else "<root>"
            msgs.append(f"{path}: {e.message}")
        raise ValueError("Schema validation failed:\n" + "\n".join(msgs))

def main():
    if len(sys.argv) != 2:
        print("Usage: python validator/src/validate.py <path-to-root-json>", file=sys.stderr)
        sys.exit(2)

    p = Path(sys.argv[1])
    payload = json.loads(p.read_text(encoding="utf-8"))
    try:
        validate_json(payload)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    print("OK")
    sys.exit(0)

if __name__ == "__main__":
    main()
