"""Normalize graph method names in a schedule JSON.

Replaces legacy aliases 'knn_gaussian' -> 'knng' and 'vknn_gaussian' -> 'vknng'
in the main schedule and any batch JSONs under the batch directory.

Usage:
  python experiments/normalize_schedule_methods.py --schedule experiments/schedules/it_exhaustive_from_registry.json --batch-dir experiments/schedules/batches
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def normalize_iteration(it: dict) -> bool:
    changed = False
    gs = it.get("graph_specs", [])
    new_gs = []
    for g in gs:
        if isinstance(g, list) and len(g) == 2 and isinstance(g[0], str):
            m = g[0]
            if m == "knn_gaussian":
                new_gs.append(["knng", g[1]])
                changed = True
                continue
            if m == "vknn_gaussian":
                new_gs.append(["vknng", g[1]])
                changed = True
                continue
            if m == "kaliofolias":
                new_gs.append(["kalofolias", g[1]])
                changed = True
                continue
        new_gs.append(g)
    if changed:
        it["graph_specs"] = new_gs
    # Normalize textual description hints that may contain legacy aliases
    desc = it.get("description", "")
    if isinstance(desc, str) and desc:
        new_desc = desc.replace("graph=knn_gaussian", "graph=knng") \
                        .replace("graph=vknn_gaussian", "graph=vknng") \
                        .replace("graph=kaliofolias", "graph=kalofolias")
        if new_desc != desc:
            it["description"] = new_desc
            changed = True
    return changed


def normalize_file(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    its = data.get("iterations", [])
    n_changed = 0
    for it in its:
        if normalize_iteration(it):
            n_changed += 1
    if n_changed > 0:
        bak = path.with_suffix(path.suffix + ".bak")
        bak.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return n_changed


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--schedule", type=Path, required=True)
    p.add_argument("--batch-dir", type=Path, default=Path("experiments") / "schedules" / "batches")
    args = p.parse_args()

    print("Normalizing schedule:", args.schedule)
    n = normalize_file(args.schedule)
    print(f"Updated {n} iterations in {args.schedule}")

    if args.batch_dir.exists():
        for f in sorted(args.batch_dir.glob("*.json")):
            m = normalize_file(f)
            if m:
                print(f"Updated {m} iterations in batch {f}")


if __name__ == "__main__":
    main()
