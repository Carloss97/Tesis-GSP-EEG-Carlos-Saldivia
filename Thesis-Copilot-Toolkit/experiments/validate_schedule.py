#!/usr/bin/env python3
"""Validate canonical schedule against produced results and generate
a minimal rerun schedule for missing non-baseline methods.

Outputs:
 - experiments/schedules/it01-it50_missing_nonbaseline_rerun_schedule.json
 - results/validate_schedule_summary.json
 - results/validate_schedule_report.md
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Set, Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SCHED_DIR = ROOT / "experiments" / "schedules"
FINAL_SCHEDULE = SCHED_DIR / "it01-it50_schedule_final.json"
MISSING_RERUN_SCHEDULE = SCHED_DIR / "it01-it50_missing_nonbaseline_rerun_schedule.json"
OUT_SUMMARY = RESULTS / "validate_schedule_summary.json"
OUT_REPORT = RESULTS / "validate_schedule_report.md"

# Keep same baseline list as postprocess
BASELINE_METHODS = ["linear", "ica", "spherical_spline", "rbfi_tps"]


def load_final_schedule() -> Dict[str, Any]:
    if not FINAL_SCHEDULE.exists():
        raise FileNotFoundError(f"Final schedule not found: {FINAL_SCHEDULE}")
    return json.loads(FINAL_SCHEDULE.read_text(encoding='utf-8'))


def collect_run_metadata_index() -> List[Dict[str, Any]]:
    """Scan RESULTS for run metadata and associated stats; return list of runs.

    Each run dict contains: meta_path, requested_datasets, stats_methods (set), stats_path
    """
    runs = []
    for p in RESULTS.glob('*_run_metadata.json'):
        try:
            mm = json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            mm = {}
        requested = mm.get('requested_datasets') or mm.get('datasets') or []
        stats_p = p.with_name(p.name.replace('_run_metadata.json', '_stats.csv'))
        methods: Set[str] = set()
        if stats_p.exists():
            try:
                df = pd.read_csv(stats_p)
                if 'method' in df.columns:
                    methods = set(df['method'].dropna().astype(str).unique().tolist())
            except Exception:
                methods = set()
        runs.append({'meta_path': str(p.name), 'requested_datasets': requested, 'stats_path': str(stats_p.name), 'methods': methods})
    return runs


def methods_present_for_iteration(it: Dict[str, Any], runs_index: List[Dict[str, Any]]) -> Set[str]:
    """Return union of methods present in stats files which match the iteration's datasets.

    Matching heuristic: run.requested_datasets intersects iteration.datasets.
    Also include direct stats file named {tag}_stats.csv when present.
    """
    present: Set[str] = set()
    it_datasets = set(it.get('datasets', []))
    # direct stats by tag
    direct_stats = RESULTS / f"{it.get('tag')}_stats.csv"
    if direct_stats.exists():
        try:
            df = pd.read_csv(direct_stats)
            if 'method' in df.columns:
                present.update(df['method'].dropna().astype(str).unique().tolist())
        except Exception:
            pass

    for r in runs_index:
        rd = set(r.get('requested_datasets') or [])
        if not rd:
            continue
        if it_datasets & rd:
            present.update(r.get('methods') or set())
    return present


def build_missing_rerun_schedule(final_sched: Dict[str, Any], runs_index: List[Dict[str, Any]]) -> Dict[str, Any]:
    missing_iterations = []
    summary = {'n_iterations': 0, 'n_missing_iters': 0, 'missing_by_iter': {}}
    for it in final_sched.get('iterations', []):
        summary['n_iterations'] += 1
        scheduled_methods = it.get('methods', [])
        non_baselines = [m for m in scheduled_methods if m not in BASELINE_METHODS]
        present = methods_present_for_iteration(it, runs_index)
        missing = [m for m in non_baselines if m not in present]
        if missing:
            summary['n_missing_iters'] += 1
            summary['missing_by_iter'][it.get('tag')] = missing
            # create a minimal rerun entry
            rerun_it = {
                'key': f"{it.get('key')}_rerun_missing_nonbaseline",
                'tag': f"{it.get('tag')}_missing_nonbaseline_rerun",
                'description': f"Rerun to produce missing non-baseline methods: {', '.join(missing)}",
                'fase': 'rerun',
                'objective': 'Produce stats rows for missing non-baseline methods required by confirmatory selection',
                'datasets': it.get('datasets', []),
                'mode': 'pilot',
                'missing_list': it.get('missing_list', [0.1])[:1],
                'seeds': [0],
                'graph_specs': (it.get('graph_specs') or [])[:1],
                'lambdas': (it.get('lambdas') or [])[:1] or [0.05],
                'snr_levels': (it.get('snr_levels') or [])[:1] or [20.0],
                'methods': missing,
            }
            missing_iterations.append(rerun_it)
    sched = {'generated_by': 'validate_schedule.py', 'reason': 'missing_nonbaseline_methods', 'iterations': missing_iterations}
    return sched, summary


def write_outputs(sched: Dict[str, Any], summary: Dict[str, Any]):
    # write schedule
    SCHED_DIR.mkdir(parents=True, exist_ok=True)
    MISSING_RERUN_SCHEDULE.write_text(json.dumps(sched, ensure_ascii=False, indent=2), encoding='utf-8')
    # write summary
    OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    # write human report
    lines = []
    lines.append('# Validate Schedule Report')
    lines.append('')
    lines.append(f"Generated: {pd.Timestamp.now().isoformat()}")
    lines.append('')
    lines.append(f"- Iterations inspected: {summary.get('n_iterations')}")
    lines.append(f"- Iterations with missing non-baseline methods: {summary.get('n_missing_iters')}")
    lines.append('')
    lines.append('## Missing by iteration')
    if summary.get('missing_by_iter'):
        for k, v in sorted(summary['missing_by_iter'].items()):
            lines.append(f"- {k}: {', '.join(v)}")
    else:
        lines.append('- None')
    OUT_REPORT.write_text('\n'.join(lines), encoding='utf-8')


def main():
    try:
        final = load_final_schedule()
    except FileNotFoundError as e:
        print(str(e))
        return

    runs_index = collect_run_metadata_index()
    rerun_sched, summary = build_missing_rerun_schedule(final, runs_index)
    write_outputs(rerun_sched, summary)
    print(f"Wrote missing rerun schedule: {MISSING_RERUN_SCHEDULE}")
    print(f"Wrote summary: {OUT_SUMMARY}")


if __name__ == '__main__':
    main()
