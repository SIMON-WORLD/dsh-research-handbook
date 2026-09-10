from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "norris.csv"
OUTPUT = ROOT / "result.json"

def load_data(path: Path) -> list[tuple[float, float]]:
    rows: list[tuple[float, float]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["y", "x"]:
            raise ValueError(f"unexpected columns: {reader.fieldnames}")
        for row in reader:
            rows.append((float(row["x"]), float(row["y"])))
    return rows

def fit_ols(rows: list[tuple[float, float]]) -> dict[str, float | int]:
    n = len(rows)
    if n < 3:
        raise ValueError("need at least 3 observations")
    xs = [x for x, _ in rows]
    ys = [y for _, y in rows]
    mean_x = math.fsum(xs) / n
    mean_y = math.fsum(ys) / n
    sxx = math.fsum((x - mean_x) ** 2 for x in xs)
    sxy = math.fsum((x - mean_x) * (y - mean_y) for x, y in rows)
    if sxx == 0:
        raise ValueError("predictor has zero variance")
    slope = sxy / sxx
    intercept = mean_y - slope * mean_x
    residuals = [y - (intercept + slope * x) for x, y in rows]
    sse = math.fsum(r * r for r in residuals)
    sst = math.fsum((y - mean_y) ** 2 for y in ys)
    residual_sd = math.sqrt(sse / (n - 2))
    r_squared = 1.0 - sse / sst
    return {
        "n": n,
        "intercept": intercept,
        "slope": slope,
        "residual_standard_deviation": residual_sd,
        "r_squared": r_squared,
    }

def main() -> None:
    result = fit_ols(load_data(DATA))
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(OUTPUT)

if __name__ == "__main__":
    main()
