#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[1]
SCHEDULE_BAK = ROOT / "experiments" / "schedules" / "it01-it50_schedule.json.bak.json"
OUT_A = ROOT / "experiments" / "schedules" / "it01-it50_schedule_phaseA_real_varied.json"
OUT_B = ROOT / "experiments" / "schedules" / "it01-it50_schedule_phaseB_real_mne_sample.json"


MAPPING: Dict[str, str] = {
    "synthetic_alpha": "physionet_real",
    "synthetic_beta": "bci_iv2a_real_s1",
    "synthetic_broad": "iv100hz_mat",
    "synthetic_8ch": "bci_iv2a_real_s2",
    "synthetic_16ch": "iv100hz_mat",
    "synthetic_32ch": "physionet_real",
}


def _map_phase_a(ds: str) -> str:
    if ds in MAPPING:
        return MAPPING[ds]
    if isinstance(ds, str) and ds.startswith("synthetic_"):
        return MAPPING.get(ds, "physionet_real")
    return ds


def main() -> int:
    if not SCHEDULE_BAK.exists():
        print(f"Schedule bak not found: {SCHEDULE_BAK}")
        return 2

    sched = json.loads(SCHEDULE_BAK.read_text(encoding="utf-8"))
    iterations = sched.get("iterations", [])

    phase_a_iters = []
    phase_b_iters = []
    for it in iterations:
        it_a = dict(it)
        it_b = dict(it)

        ds_list = it.get("datasets", [])
        it_a["datasets"] = [_map_phase_a(d) for d in ds_list] or ["physionet_real"]
        it_b["datasets"] = ["mne_sample"]

        phase_a_iters.append(it_a)
        phase_b_iters.append(it_b)

    out_a = dict(sched)
    out_b = dict(sched)
    out_a["generated"] = datetime.now(timezone.utc).isoformat()
    out_b["generated"] = datetime.now(timezone.utc).isoformat()
    out_a["note"] = "Phase A: varied real dataset mapping (auto-generated)"
    out_b["note"] = "Phase B: control using mne_sample only (auto-generated)"
    out_a["iterations"] = phase_a_iters
    out_b["iterations"] = phase_b_iters

    OUT_A.write_text(json.dumps(out_a, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_B.write_text(json.dumps(out_b, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Wrote Phase A schedule: {OUT_A}")
    print(f"Wrote Phase B schedule: {OUT_B}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
