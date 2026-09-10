from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = ROOT / "expected.json"
DEFAULT_RESULT = ROOT / "result.json"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", nargs="?", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    actual = json.loads(args.result.read_text(encoding="utf-8"))

    errors: list[str] = []
    data_path = ROOT / "data" / "norris.csv"
    data_sha256 = hashlib.sha256(data_path.read_bytes()).hexdigest()
    if data_sha256 != expected["data_sha256"]:
        errors.append(
            f"data sha256: expected {expected['data_sha256']}, got {data_sha256}"
        )
    if actual.get("n") != expected["n"]:
        errors.append(f"n: expected {expected['n']}, got {actual.get('n')}")

    for key in ("intercept", "slope", "residual_standard_deviation", "r_squared"):
        value = actual.get(key)
        if not isinstance(value, (int, float)):
            errors.append(f"{key}: missing or non-numeric")
            continue
        tolerance = expected["tolerances"][key]
        if not math.isclose(value, expected[key], rel_tol=0.0, abs_tol=tolerance):
            errors.append(
                f"{key}: expected {expected[key]:.15g} ± {tolerance:g}, got {value:.15g}"
            )

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: NIST Norris certified values matched.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
