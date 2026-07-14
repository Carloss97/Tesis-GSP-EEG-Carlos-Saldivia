#!/usr/bin/env python3
"""
Normalize a schedule JSON by replacing synthetic_* dataset tokens
with real dataset keys (default: mne_sample). When run with
`--inplace` a backup file `<name>.bak.json` is created.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict


DEFAULT_REAL = "mne_sample"
SYN_PREFIX = "synthetic_"


def load_schedule(path: Path) -> Dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_schedule(obj: Dict, path: Path) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_schedule(obj: Dict, mapping: Dict[str, str] | None = None, default: str = DEFAULT_REAL) -> int:
    mapping = mapping or {}
    replaced = 0
    for it in obj.get("iterations", []):
        ds_list = it.get("datasets", [])
        new_ds = []
        for d in ds_list:
            if isinstance(d, str) and d.startswith(SYN_PREFIX):
                new = mapping.get(d, default)
                if new != d:
                    replaced += 1
                new_ds.append(new)
            else:
                new_ds.append(d)
        it["datasets"] = new_ds
    return replaced


def parse_map_entries(entries: list[str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for e in entries or []:
        if ":" in e:
            k, v = e.split(":", 1)
            out[k] = v
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Normalize schedule datasets to real dataset keys")
    p.add_argument("--schedule", type=Path, required=True, help="Path to schedule JSON")
    p.add_argument("--inplace", action="store_true", help="Modify schedule file in-place (creates .bak.json)")
    p.add_argument("--backup", action="store_true", default=True, help="Create a .bak.json backup when --inplace is used")
    p.add_argument("--map", nargs="*", help="Optional mappings like synthetic_alpha:mne_sample")
    args = p.parse_args()

    schedule_path = args.schedule
    if not schedule_path.exists():
        print(f"Schedule not found: {schedule_path}")
        return 2

    sched = load_schedule(schedule_path)
    mapping = parse_map_entries(args.map) if args.map else {}
    replaced = normalize_schedule(sched, mapping=mapping, default=DEFAULT_REAL)

    if args.inplace:
        if args.backup:
            bak = schedule_path.parent / (schedule_path.name + ".bak.json")
            bak.write_text(schedule_path.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"Backup written: {bak}")
        save_schedule(sched, schedule_path)
        print(f"Wrote (in-place): {schedule_path} — replacements made: {replaced}")
    else:
        out = schedule_path.parent / (schedule_path.stem + "_real" + schedule_path.suffix)
        save_schedule(sched, out)
        print(f"Wrote: {out} — replacements made: {replaced}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
