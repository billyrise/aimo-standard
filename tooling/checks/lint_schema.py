import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas" / "jsonschema"

def main():
    errors = []
    for p in sorted(SCHEMAS.glob("*.json")):
        try:
            schema = json.loads(p.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
        except Exception as e:
            errors.append(f"{p.name}: {e}")

    if errors:
        print("schema lint failed:\n" + "\n".join(errors), file=sys.stderr)
        sys.exit(1)

    print("schema lint OK")
    sys.exit(0)

if __name__ == "__main__":
    main()
