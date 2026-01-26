import json
import glob
from datetime import datetime, timezone

PLAN_FILES = [
    "curriculum/plans/lds_standard_works.json",
    "curriculum/plans/temple_prep.json",
    "curriculum/plans/motherhood.json",
    "curriculum/plans/fatherhood.json",
    "curriculum/plans/mission_prep.json",
]

OUT_FILE = "curriculum/v1.json"

VERSION = 4  # <-- bump this anytime you publish
DEFAULT_ID = "lds_standard_works"

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    curricula = []
    for path in PLAN_FILES:
        plan = load_json(path)
        # minimal validation
        for key in ("id", "name", "days"):
            if key not in plan:
                raise ValueError(f"{path} missing required key: {key}")
        curricula.append(plan)

    bundle = {
        "version": VERSION,
        "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "default_curriculum_id": DEFAULT_ID,
        "curricula": curricula,
    }

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)

    print(f"Wrote {OUT_FILE} with {len(curricula)} curricula.")

if __name__ == "__main__":
    main()
