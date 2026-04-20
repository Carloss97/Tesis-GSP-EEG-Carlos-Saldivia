"""Classify NO-GO runs for provisional inclusion in comparisons.

Policy implemented:
- Accept a NO-GO run "provisionally" if:
  - `stats_exists` is True in `results/no_go_analysis.csv` AND
  - the referenced `stats_path` CSV contains at least one finite numeric `mae_median` value.
- Otherwise, mark as "requires_rerun" (rejected for comparison).

Outputs (written to results/):
- no_go_accepted_provisional.csv  -- accepted rows (tag,dataset,stats_path)
- no_go_rejected_provisional.csv  -- rejected rows (full original columns + reason)

Usage (run in conda env `eegrasp`):
  conda activate eegrasp
  python Thesis-Copilot-Toolkit/scripts/classify_no_go_for_comparison.py

"""
import argparse
import csv
import math
import os
import sys
from pathlib import Path

import pandas as pd
import re
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
NO_GO_ANALYSIS = RESULTS / "no_go_analysis.csv"


def has_valid_mae(stats_path: Path) -> bool:
    try:
        if not stats_path.exists():
            return False
        df = pd.read_csv(stats_path)
        # common column name
        col = None
        for candidate in ("mae_median", "mae_median", "mae_mean"):
            if candidate in df.columns:
                col = candidate
                break
        if col is None:
            return False
        vals = df[col].values
        for v in vals:
            try:
                if pd.notna(v) and not math.isinf(float(v)):
                    return True
            except Exception:
                continue
        return False
    except Exception:
        return False


def _inspect_stats_file(path: Path):
    """Return (has_valid, method_count) for a stats CSV path."""
    try:
        if not path.exists():
            return False, 0
        df = pd.read_csv(path)
        col = None
        for candidate in ("mae_median", "mae_mean"):
            if candidate in df.columns:
                col = candidate
                break
        if col is None:
            return False, 0
        # count unique methods if available
        method_count = 0
        if 'method' in df.columns:
            try:
                method_count = int(df['method'].nunique())
            except Exception:
                method_count = len(df.index)
        else:
            method_count = len(df.index)
        # check at least one finite value
        for v in df[col].values:
            try:
                if pd.notna(v) and not math.isinf(float(v)):
                    return True, int(method_count)
            except Exception:
                continue
        return False, int(method_count)
    except Exception:
        return False, 0


def find_best_stats_candidate(tag: str, dataset: str) -> Optional[Path]:
    """Search results for a plausible stats CSV for (tag,dataset).

    Preference order:
    1. files containing the `itNN` token from tag
    2. files containing dataset substring
    3. any _stats.csv with valid mae, prefer higher method_count
    Avoid `confirm_000` files unless no other candidate.
    """
    # gather candidates
    candidates = list(RESULTS.rglob("*_stats.csv"))
    if not candidates:
        return None

    it_match = re.search(r"(it\d{1,4})", tag or "", re.IGNORECASE)
    it_token = it_match.group(1) if it_match else None

    scored = []
    for p in candidates:
        name = p.name.lower()
        contains_it = it_token and (it_token.lower() in name)
        contains_dataset = dataset and (dataset.lower() in name.lower())
        # avoid confirm_000 if possible
        is_confirm000 = 'confirm_000' in name
        has_valid, mcount = _inspect_stats_file(p)
        if not has_valid:
            continue
        score = (0 if is_confirm000 else 1, 1 if contains_it else 0, 1 if contains_dataset else 0, mcount)
        scored.append((score, p))

    if not scored:
        return None
    # pick best by score (higher is better)
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1]


def main():
    if not NO_GO_ANALYSIS.exists():
        print(f"ERROR: {NO_GO_ANALYSIS} not found", file=sys.stderr)
        sys.exit(2)

    df = pd.read_csv(NO_GO_ANALYSIS, dtype=str).fillna("")

    accepted = []
    rejected = []

    for _, row in df.iterrows():
        tag = row.get("tag", "")
        dataset = row.get("dataset", "")
        stats_exists = row.get("stats_exists", "False").strip().lower() in ("1", "true", "yes")
        stats_path = row.get("stats_path", "")

        reason = None
        chosen_path = None
        tried = []
        # try given stats_path first
        if stats_exists and stats_path:
            stats_p = Path(stats_path)
            # If given absolute path, use it; otherwise resolve relative to RESULTS
            if not stats_p.is_absolute():
                stats_p = RESULTS / stats_path
            tried.append(stats_p)
            if has_valid_mae(stats_p):
                chosen_path = stats_p

        # If chosen_path came from the provided stats_path but has only one method,
        # try the same aggressive fallback to find any multi-method stats file.
        if chosen_path is not None:
            try:
                hv_chosen, mc_chosen = _inspect_stats_file(Path(chosen_path))
            except Exception:
                hv_chosen, mc_chosen = False, 0
            if hv_chosen and mc_chosen <= 1:
                alt_best = None
                alt_mc = 0
                for p in RESULTS.rglob("*_stats.csv"):
                    ok, mcount = _inspect_stats_file(p)
                    if not ok:
                        continue
                    if mcount > alt_mc and 'confirm_000' not in p.name.lower():
                        alt_best = p
                        alt_mc = mcount
                if alt_best is None:
                    for p in RESULTS.rglob("*_stats.csv"):
                        ok, mcount = _inspect_stats_file(p)
                        if not ok:
                            continue
                        if mcount > alt_mc:
                            alt_best = p
                            alt_mc = mcount
                if alt_best is not None:
                    tried.append(alt_best)
                    chosen_path = alt_best

        # fallback: search for better stats candidate in results
        if chosen_path is None:
            cand = find_best_stats_candidate(tag, dataset)
            if cand is not None:
                tried.append(cand)
                hv, mc = _inspect_stats_file(cand)
                if hv:
                    chosen_path = cand
                # If the chosen candidate has only one method, try an aggressive fallback:
                # prefer any _stats.csv in RESULTS with method_count > 1 (avoid confirm_000 when possible)
                if mc <= 1:
                    alt_best = None
                    alt_mc = 0
                    for p in RESULTS.rglob("*_stats.csv"):
                        ok, mcount = _inspect_stats_file(p)
                        if not ok:
                            continue
                        if mcount > alt_mc and 'confirm_000' not in p.name.lower():
                            alt_best = p
                            alt_mc = mcount
                    # if nothing found (non-confirm), allow confirm_000 as last resort
                    if alt_best is None:
                        for p in RESULTS.rglob("*_stats.csv"):
                            ok, mcount = _inspect_stats_file(p)
                            if not ok:
                                continue
                            if mcount > alt_mc:
                                alt_best = p
                                alt_mc = mcount
                    if alt_best is not None:
                        tried.append(alt_best)
                        chosen_path = alt_best

        if chosen_path is not None:
            accepted.append({"tag": tag, "dataset": dataset, "stats_path": str(chosen_path)})
        else:
            if not stats_exists:
                reason = "stats_missing"
            else:
                reason = "stats_no_valid_mae"
            rej = {**row}
            rej["reject_reason"] = reason
            rej["tried_stats_candidates"] = ";".join([str(p) for p in tried if p])
            rejected.append(rej)

    # write outputs
    accepted_path = RESULTS / "no_go_accepted_provisional.csv"
    rejected_path = RESULTS / "no_go_rejected_provisional.csv"

    with accepted_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["tag", "dataset", "stats_path"])
        w.writeheader()
        for r in accepted:
            w.writerow(r)

    # preserve original columns and add reject_reason + tried_stats_candidates
    with rejected_path.open("w", newline="", encoding="utf-8") as f:
        cols = list(df.columns) + ["reject_reason", "tried_stats_candidates"]
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rejected:
            # r already contains original row fields (as strings) + reject_reason and tried_stats_candidates
            # ensure all keys present
            out = {k: r.get(k, "") for k in cols}
            w.writerow(out)

    print(f"Provisional classification done. Accepted: {len(accepted)}. Rejected: {len(rejected)}")
    print(f"Files: {accepted_path}, {rejected_path}")


if __name__ == "__main__":
    main()
