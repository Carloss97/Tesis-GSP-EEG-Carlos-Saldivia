#!/usr/bin/env python3
"""Merge Phase A and Phase B it01-it50 schedules into a canonical final schedule.

Writes: experiments/schedules/it01-it50_schedule_final.json
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
SCHED_DIR = ROOT / "experiments" / "schedules"
OUT = SCHED_DIR / "it01-it50_schedule_final.json"
A = SCHED_DIR / "it01-it50_schedule_phaseA_real_varied.json"
B = SCHED_DIR / "it01-it50_schedule_phaseB_real_mne_sample.json"
FALLBACK = SCHED_DIR / "it01-it50_schedule.json"


def load(path: Path):
    if not path.exists():
        return {"generated": None, "iterations": []}
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    a = load(A)
    b = load(B)
    fb = load(FALLBACK)

    # Build map preferring Phase A, then Phase B, then fallback
    merged = {}
    for it in fb.get("iterations", []):
        key = it.get("key")
        if key:
            merged[key] = it
    for it in b.get("iterations", []):
        key = it.get("key")
        if key:
            merged[key] = it
    for it in a.get("iterations", []):
        key = it.get("key")
        if key:
            merged[key] = it

    # Ensure ordering it01..it50 when possible
    keys_sorted = sorted(merged.keys(), key=lambda s: int(s.replace("it", "")) if s.startswith("it") and s.replace("it", "").isdigit() else s)
    iterations = [merged[k] for k in keys_sorted]

    out = {"generated": datetime.utcnow().isoformat() + "Z", "iterations": iterations}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote final schedule: {OUT}")


if __name__ == '__main__':
    main()
