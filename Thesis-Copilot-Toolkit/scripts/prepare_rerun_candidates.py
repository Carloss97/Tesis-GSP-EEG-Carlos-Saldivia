#!/usr/bin/env python3
"""Prepare rerun candidates to reach a target sample size per combo.

Writes: results/analysis/batches/rerun_candidates_target{N}.csv

Usage: python scripts/prepare_rerun_candidates.py --target 200
"""
from pathlib import Path
import argparse
import pandas as pd
import math


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, default=200, help="Target samples per combo (default: 200)")
    parser.add_argument("--min-current", type=int, default=1, help="Include combos with current n below this (default: 1)")
    args = parser.parse_args()

    ROOT = Path(__file__).resolve().parents[1]
    batches = ROOT / "results" / "analysis" / "batches"

    stats_csv = batches / "best_method_by_combo_stats.csv"
    consolidated = batches / "consolidated_all_batches.csv"

    if stats_csv.exists():
        stats = pd.read_csv(stats_csv)
    else:
        stats = pd.DataFrame()

    # ensure numeric best_n
    if "best_n" in stats.columns:
        stats["best_n"] = pd.to_numeric(stats["best_n"], errors="coerce")

    # fallback to consolidated to compute current n per combo+method
    if consolidated.exists():
        cons = pd.read_csv(consolidated)
        cons["missing_ratio"] = pd.to_numeric(cons.get("missing_ratio"), errors="coerce")
    else:
        cons = pd.DataFrame()

    rows = []
    # iterate over stats rows if available
    if not stats.empty:
        for _, r in stats.iterrows():
            graph = r.get("graph")
            dataset = r.get("dataset")
            mr = r.get("missing_ratio")
            best = r.get("best_method")
            n_current = r.get("best_n")
            if pd.isna(n_current):
                # fallback to consolidated count
                if not cons.empty:
                    sel = cons[(cons["dataset"] == dataset) & (cons["graph"] == graph)]
                    try:
                        sel = sel[pd.to_numeric(sel["missing_ratio"], errors="coerce") == float(mr)]
                    except Exception:
                        sel = sel[sel["missing_ratio"] == mr]
                    n_current = int((sel[sel["method"] == best].shape[0]))
                else:
                    n_current = 0
            else:
                try:
                    n_current = int(n_current)
                except Exception:
                    n_current = 0

            additional = max(0, args.target - n_current)
            if n_current < args.min_current or additional > 0:
                rows.append({
                    "dataset": dataset,
                    "graph": graph,
                    "missing_ratio": mr,
                    "best_method": best,
                    "n_current": n_current,
                    "target_n": args.target,
                    "additional_needed": additional,
                })

    else:
        # no stats; compute summary counts per combo+method from consolidated
        if cons.empty:
            raise FileNotFoundError("No stats or consolidated CSV found to prepare rerun candidates.")
        grp = cons.groupby(["dataset", "graph", "missing_ratio", "method"])
        for (dataset, graph, mr, method), g in grp:
            n_current = int(len(g))
            additional = max(0, args.target - n_current)
            if n_current < args.min_current or additional > 0:
                rows.append({
                    "dataset": dataset,
                    "graph": graph,
                    "missing_ratio": mr,
                    "best_method": method,
                    "n_current": n_current,
                    "target_n": args.target,
                    "additional_needed": additional,
                })

    out = pd.DataFrame(rows)
    out_path = batches / f"rerun_candidates_target{args.target}.csv"
    out.to_csv(out_path, index=False)

    total_add = int(out["additional_needed"].sum()) if not out.empty else 0
    print(f"Wrote rerun candidates: {out_path} (rows: {len(out)}, total_additional_runs: {total_add})")


if __name__ == "__main__":
    main()
