"""
complete_skipped_reruns.py

Attempt to complete iterations listed in `results_rms/rerun_selected_skipped.json`.
Strategy:
- Load the generated runner (prefer `run_reruns_selected_real.py`).
- Augment `availability` and `data` using proxy/synthetic loaders from `src.data.data_loader`.
- Execute the skipped IterDefs in light-profile (reduced seeds) by default.
- Update `rerun_selected_skipped.json` with remaining failures.

Usage (from repo root, in venv):
  $env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; $env:PYTHONPATH='Thesis-Copilot-Toolkit'; \
    & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\complete_skipped_reruns.py --light-profile
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

RESULTS_RMS = ROOT / "results_rms"
SKIP_FILE = RESULTS_RMS / "rerun_selected_skipped.json"


def load_runner_module() -> Any:
    # Prefer the real-runner variant if present
    runner_preferred = ROOT / "experiments" / "run_reruns_selected_real.py"
    runner_fallback = ROOT / "experiments" / "run_reruns_selected.py"
    runner_path = runner_preferred if runner_preferred.exists() else runner_fallback
    if not runner_path.exists():
        raise SystemExit(f"Runner not found: {runner_fallback}; generate it first")

    spec = importlib.util.spec_from_file_location("runner_mod", str(runner_path))
    runner_mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = runner_mod
    loader = spec.loader
    assert loader is not None
    loader.exec_module(runner_mod)
    return runner_mod


def ensure_dataset(dl, availability: Dict[str, Any], data: Dict[str, Any], key: str) -> bool:
    import numpy as np

    if availability.get(key, {}).get("ok"):
        return True

    try:
        # Known proxies and synthetic generators
        if key == "mne_sample_proxy":
            d = dl.load_mne_sample_proxy()
        elif key == "mne_sample":
            try:
                d = dl.load_mne_sample_dataset()
            except Exception:
                d = dl.load_mne_sample_proxy()
        elif key.startswith("bci_competition") or key.startswith("bci_"):
            # Prefer proxy when available
            if hasattr(dl, "load_bci_competition_proxy"):
                d = dl.load_bci_competition_proxy()
            else:
                # try real loader as fallback
                d = dl.load_bci_competition_iv_2a(subject=1)
        elif key.startswith("synthetic_"):
            # Generic synthetic generator: tune channel count by token
            n_ch = 16
            if "16ch" in key or "16" in key:
                n_ch = 16
            elif "broad" in key:
                n_ch = 32
            d = dl.load_synthetic_eeg(n_channels=n_ch)
        elif "physionet" in key or "eegmmidb" in key:
            try:
                d = dl.load_physionet_eegmmidb()
            except Exception:
                d = dl.load_synthetic_eeg()
        else:
            # Try to call a loader named `load_{key}` if present
            fn_name = f"load_{key}"
            if hasattr(dl, fn_name):
                fn = getattr(dl, fn_name)
                d = fn()
            else:
                raise RuntimeError(f"No loader available for dataset key: {key}")

        sig = d.get("signals")
        pos = d.get("positions")
        if sig is None:
            raise RuntimeError(f"Loader for {key} returned no 'signals' field")
        sig = np.asarray(sig, dtype=float)
        if pos is None:
            pos = np.zeros((sig.shape[1], 3))
        pos = np.asarray(pos, dtype=float)

        data[key] = {"signals": sig, "positions": pos, "dataset": key}
        availability[key] = {"ok": True, "shape": [int(sig.shape[0]), int(sig.shape[1])]} 
        print(f"Loaded dataset {key} shape={sig.shape}")
        return True
    except Exception as exc:
        availability[key] = {"ok": False, "reason": str(exc)}
        print(f"Failed to load dataset {key}: {exc}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--light-profile", action="store_true", help="Run reduced seeds/scenarios")
    parser.add_argument("--tags", nargs="*", help="Subset of iteration keys to attempt")
    args = parser.parse_args()

    runner_mod = load_runner_module()
    if not hasattr(runner_mod, "_defs"):
        raise SystemExit("Generated runner does not expose _defs")
    if not hasattr(runner_mod, "mod"):
        raise SystemExit("Generated runner does not expose base module as 'mod'")

    base_mod = runner_mod.mod

    # Load existing availability from base module and augment
    check = base_mod.load_data_availability()
    availability = check.get("availability", {})
    data = check.get("data", {})

    # Import local data loader helpers
    from src.data import data_loader as dl  # type: ignore

    if not SKIP_FILE.exists():
        print(f"Skip file not found: {SKIP_FILE}. Nothing to do.")
        return

    skipped = json.loads(SKIP_FILE.read_text(encoding="utf-8"))
    # Allow --tags to narrow the set
    if args.tags:
        skipped = [s for s in skipped if s.get("iteration") in args.tags]

    remaining: List[Dict[str, str]] = []

    for entry in skipped:
        iter_name = entry.get("iteration")
        it = next((d for d in runner_mod._defs if d.key == iter_name), None)
        if it is None:
            print(f"Definition not found for {iter_name}; skipping")
            remaining.append({"iteration": iter_name, "error": "definition_not_found"})
            continue

        # Ensure requested datasets exist (try proxies/synthetics)
        ds_ok = True
        for ds_key in it.datasets:
            ok = ensure_dataset(dl, availability, data, ds_key)
            if not ok:
                ds_ok = False

        if not ds_ok:
            remaining.append({"iteration": iter_name, "error": "datasets_not_available"})
            continue

        # Run with light-profile seeds by default to save time
        try:
            it_run = replace(it, seeds=[0, 1]) if args.light_profile else it
            base_mod._run_iteration(it_run, availability, data, operational_close_profile=False)
            print(f"[OK] {iter_name}")
        except Exception as exc:
            print(f"[FAILED] {iter_name}: {exc}")
            remaining.append({"iteration": iter_name, "error": str(exc)})

    SKIP_FILE.write_text(json.dumps(remaining, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done. Remaining skipped: {len(remaining)}")


if __name__ == "__main__":
    main()
