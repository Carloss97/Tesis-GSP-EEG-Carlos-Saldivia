#!/usr/bin/env python3
"""Postprocess experiment results: sanitize, detect errors/anomalies, aggregate stats,
select best methods and produce a confirmatory schedule limited to top methods.

Writes into `Thesis-Copilot-Toolkit/results/`:
 - postprocess_summary.json
 - postprocess_report.md
 - selected_best_methods.json

And produces schedule: `experiments/schedules/it01-it50_confirmatory_top_methods.json`
"""
from __future__ import annotations
import json
import math
import os
from pathlib import Path
from typing import Dict, List, Any

import numpy as np
import pandas as pd

try:
    from scipy.stats import mannwhitneyu
    SCIPY_AVAILABLE = True
except Exception:
    SCIPY_AVAILABLE = False

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SCHED_DIR = ROOT / "experiments" / "schedules"
FINAL_SCHEDULE = SCHED_DIR / "it01-it50_schedule_final.json"
CONF_SCHEDULE = SCHED_DIR / "it01-it50_confirmatory_top_methods.json"

OUT_SUMMARY = RESULTS / "postprocess_summary.json"
OUT_REPORT = RESULTS / "postprocess_report.md"
OUT_SELECTED = RESULTS / "selected_best_methods.json"
OUT_SELECTED_DETAILED = RESULTS / "selected_best_methods_detailed.json"

# Configuration: baseline group and selection thresholds
BASELINE_METHODS = ["linear", "ica", "spherical_spline", "rbfi_tps"]
MIN_OCCURRENCE_FRACTION = 0.05  # lowered further to be more inclusive
MIN_SELECTED_NONBASELINE = 3
MAX_SELECTED = 6


def list_tags() -> List[str]:
    tags = set()
    for p in RESULTS.glob('*_raw.csv'):
        tags.add(p.name.split('_')[0])
    for p in RESULTS.glob('*_stats.csv'):
        tags.add(p.name.split('_')[0])
    return sorted(tags)


def schedule_tags() -> List[str]:
    """Return the ordered list of tags declared in the FINAL_SCHEDULE file.

    If the schedule file is missing or malformed, returns an empty list.
    """
    if not FINAL_SCHEDULE.exists():
        return []
    try:
        sched = json.loads(FINAL_SCHEDULE.read_text(encoding='utf-8'))
        return [it.get('tag') for it in sched.get('iterations', []) if it.get('tag')]
    except Exception:
        return []


def safe_read_csv(p: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(p)
    except Exception:
        return pd.DataFrame()


def analyze_tag(tag: str) -> Dict[str, Any]:
    raw_p = RESULTS / f"{tag}_raw.csv"
    stats_p = RESULTS / f"{tag}_stats.csv"
    meta_p = RESULTS / f"{tag}_run_metadata.json"

    out: Dict[str, Any] = {"tag": tag, "has_raw": raw_p.exists(), "has_stats": stats_p.exists(), "issues": []}

    if raw_p.exists():
        df = safe_read_csv(raw_p)
        out["n_rows"] = int(len(df))
        if df.empty:
            out["issues"].append("empty_raw")
        else:
            # methods present
            methods = sorted(df['method'].unique().tolist()) if 'method' in df.columns else []
            out["n_methods"] = int(len(methods))
            out["methods"] = methods
            # error analysis
            if 'error' in df.columns:
                err_rows = df[df['error'].notna() & (df['error'].astype(str).str.strip() != "")]
                out["errors_count"] = int(len(err_rows))
                out["errors_sample"] = err_rows['error'].astype(str).drop_duplicates().head(5).tolist()
                if int(len(err_rows)) > 0:
                    out["issues"].append("has_errors")
            # method-level stats
            if 'mae' in df.columns and 'method' in df.columns:
                g = df.groupby('method')['mae'].agg(['count','median','mean','std']).reset_index()
                out["method_stats"] = g.rename(columns={'count':'n'}).to_dict(orient='records')
                # detect collapsed outputs (all medians equal)
                try:
                    medians = g['median'].dropna().values
                    if len(medians) > 1 and np.nanstd(medians) < 1e-12:
                        out["issues"].append("collapsed_mae_across_methods")
                except Exception:
                    pass
                # detect outliers
                all_mae = df['mae'].dropna().values
                if len(all_mae) > 0:
                    mu = float(np.mean(all_mae))
                    sigma = float(np.std(all_mae))
                    out["mae_mean"] = mu
                    out["mae_std"] = sigma
                    # flagged if any mae > mu + 6*sigma
                    if sigma > 0 and (all_mae > (mu + 6 * sigma)).any():
                        out["issues"].append("extreme_mae_outliers")
            # time stats
            if 'time_sec' in df.columns:
                out["time_max_sec"] = float(df['time_sec'].max())
                out["time_mean_sec"] = float(df['time_sec'].mean())
                if out["time_max_sec"] > 600:
                    out["issues"].append("very_slow_runs")
    else:
        out["issues"].append("missing_raw")

    if stats_p.exists():
        s = safe_read_csv(stats_p)
        if s.empty:
            out.setdefault('issues',[]).append('empty_stats')
        else:
            out['stats_methods'] = int(s['method'].nunique()) if 'method' in s.columns else 0
    else:
        out.setdefault('issues',[]).append('missing_stats')

    if meta_p.exists():
        try:
            mm = json.loads(meta_p.read_text(encoding='utf-8'))
            out['meta'] = {k: mm.get(k) for k in ['requested_datasets','blocked_requested_datasets','normalization'] if mm.get(k) is not None}
            if mm.get('blocked_requested_datasets'):
                out.setdefault('issues',[]).append('blocked_datasets')
        except Exception:
            out.setdefault('issues',[]).append('bad_metadata')
    return out


def aggregate_methods_from_stats(tags: List[str]) -> pd.DataFrame:
    rows = []
    for tag in tags:
        p = RESULTS / f"{tag}_stats.csv"
        if not p.exists():
            continue
        try:
            df = pd.read_csv(p)
            df['tag'] = tag
            rows.append(df)
        except Exception:
            continue
    if not rows:
        return pd.DataFrame()
    allstats = pd.concat(rows, ignore_index=True)
    # Expect columns: method, mae_mean, mae_std, mae_median, time_mean_sec
    grouped = (
        allstats.groupby('method', as_index=False)
        .agg(
            occurrence=('tag', 'nunique'),
            mae_median_median=('mae_median', 'median'),
            mae_mean_mean=('mae_mean', 'mean'),
            mae_mean_std=('mae_mean','std'),
            n_stats_total=('mae_median','count'),
        )
        .sort_values('mae_median_median')
    )
    return grouped


def pairwise_tests_for_top_methods(raw_tags: List[str], top_methods: List[str]) -> List[Dict[str,Any]]:
    # build big raw df
    rows = []
    for tag in raw_tags:
        p = RESULTS / f"{tag}_raw.csv"
        if not p.exists():
            continue
        try:
            df = pd.read_csv(p)
            rows.append(df[['method','mae']])
        except Exception:
            continue
    if not rows:
        return []
    combined = pd.concat(rows, ignore_index=True)
    results = []
    for i in range(len(top_methods)):
        for j in range(i+1, len(top_methods)):
            a = top_methods[i]
            b = top_methods[j]
            a_vals = combined[combined['method']==a]['mae'].dropna().values
            b_vals = combined[combined['method']==b]['mae'].dropna().values
            if len(a_vals) < 3 or len(b_vals) < 3:
                results.append({'a':a,'b':b,'n_a':len(a_vals),'n_b':len(b_vals),'u':None,'p':None,'note':'insufficient_samples'})
                continue
            if SCIPY_AVAILABLE:
                try:
                    u, p = mannwhitneyu(a_vals, b_vals, alternative='two-sided')
                except Exception:
                    u, p = None, None
            else:
                u, p = None, None
            results.append({'a':a,'b':b,'n_a':len(a_vals),'n_b':len(b_vals),'u':u,'p':p})
    return results


def write_confirmatory_schedule(selected: List[str]):
    if not FINAL_SCHEDULE.exists():
        print(f"Final schedule not found: {FINAL_SCHEDULE}; skipping confirmatory schedule creation.")
        return None
    sched = json.loads(FINAL_SCHEDULE.read_text(encoding='utf-8'))
    for it in sched.get('iterations', []):
        it['methods'] = selected
    CONF_SCHEDULE.write_text(json.dumps(sched, ensure_ascii=False, indent=2), encoding='utf-8')
    return str(CONF_SCHEDULE)


def main():
    # Prefer tags declared in the final schedule to avoid using historical/aggregated-only
    # artifacts when selecting candidate methods.
    # Prefer tags declared in the final schedule, but also append any rerun tags
    # (prefixes `rr` and `rerun_`) that may hold newly-executed candidate methods.
    sched_tags = schedule_tags()
    all_tags = list_tags()
    if sched_tags:
        # preserve order: schedule tags first, then reruns not already present
        rerun_tags = [t for t in all_tags if t.startswith("rr") or t.startswith("rerun_")]
        tags = list(dict.fromkeys(sched_tags + [t for t in rerun_tags if t not in sched_tags]))
        schedule_used = True
    else:
        tags = all_tags
        schedule_used = False

    summary = {
        'n_tags_found': len(tags),
        'tags': [],
        'issues_overall': {},
        'method_stats_aggregate': [],
        'top_methods': [],
        'schedule_used': schedule_used,
        'schedule_tags_count': len(sched_tags) if sched_tags else 0,
    }

    for t in tags:
        info = analyze_tag(t)
        summary['tags'].append(info)
        for iss in info.get('issues',[]):
            summary['issues_overall'][iss] = summary['issues_overall'].get(iss,0) + 1

    grouped = aggregate_methods_from_stats(tags)
    if not grouped.empty:
        # Rank methods by median-of-medians MAE across available stats.
        # Do NOT exclude low-occurrence methods here — we prefer to select
        # top non-baseline methods even if they appear in few tags (they may
        # come from focused reruns). Occurrence is still reported.
        cand = grouped.sort_values('mae_median_median')

        # Ensure we prefer non-baseline methods and guarantee at least
        # MIN_SELECTED_NONBASELINE non-baselines when available.
        TOP_REQUIRED = MIN_SELECTED_NONBASELINE
        final_selected: List[str] = []

        # 1) collect non-baseline candidates from the ranked pool
        ranked_methods = cand['method'].tolist()
        for m in ranked_methods:
            if m in BASELINE_METHODS:
                continue
            if m not in final_selected:
                final_selected.append(m)
            if len(final_selected) >= TOP_REQUIRED:
                break

        # 2) if not enough non-baselines found, extend search to the full grouped ranking
        if len(final_selected) < TOP_REQUIRED:
            full_ranked = grouped.sort_values('mae_median_median')['method'].tolist()
            for m in full_ranked:
                if m in final_selected or m in BASELINE_METHODS:
                    continue
                final_selected.append(m)
                if len(final_selected) >= TOP_REQUIRED:
                    break

        # 3) if still insufficient, reluctantly include baseline methods (mark this)
        selection_note = None
        if len(final_selected) < TOP_REQUIRED:
            for m in ranked_methods:
                if m in final_selected:
                    continue
                final_selected.append(m)
                if len(final_selected) >= TOP_REQUIRED:
                    break
            selection_note = 'forced_include_baselines_due_to_no_nonbaseline_candidates'

        # Trim to MAX_SELECTED overall
        final_selected = final_selected[:MAX_SELECTED]

        summary['method_stats_aggregate'] = grouped.to_dict(orient='records')
        summary['top_candidates'] = cand.to_dict(orient='records')
        summary['selected_methods'] = final_selected
        if selection_note:
            summary['selection_note'] = selection_note
    else:
        summary['method_stats_aggregate'] = []
        summary['top_candidates'] = []
        summary['selected_methods'] = []

    # pairwise tests
    if summary.get('selected_methods'):
        pair = pairwise_tests_for_top_methods(tags, summary['selected_methods'])
    else:
        pair = []

    # write outputs
    OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

    # human report
    md = []
    md.append(f"# Postprocess Report\n\nGenerated: {pd.Timestamp.now().isoformat()}\n")
    md.append(f"- Tags found: {len(tags)}\n")
    md.append("## Overall issues summary\n")
    for k,v in sorted(summary['issues_overall'].items(), key=lambda kv: -kv[1]):
        md.append(f"- {k}: {v}\n")
    md.append('\n## Selected methods (candidates)\n')
    for m in summary.get('selected_methods',[]):
        md.append(f"- {m}\n")
    # add selection note if baselines were excluded or a fallback occurred
    if summary.get('selection_note'):
        note = summary.get('selection_note')
        if note == 'baselines_excluded_from_selection':
            md.append(f"- Note: baseline methods ({', '.join(BASELINE_METHODS)}) were excluded from the final candidate list.\n")
        elif note == 'no_nonbaseline_candidates_found':
            md.append(f"- Note: no non-baseline candidate methods were found in the aggregated stats; the selected-methods list is empty.\n")
        else:
            md.append(f"- Note: selection status: {note}\n")
    md.append('\n## Pairwise tests (selected methods)\n')
    if pair:
        for r in pair:
            md.append(f"- {r['a']} vs {r['b']}: n_a={r['n_a']}, n_b={r['n_b']}, u={r.get('u')}, p={r.get('p')}\n")
    else:
        md.append("- No pairwise tests computed (insufficient data or no selection).\n")

    # Anomalies per tag
    md.append('\n## Notable anomalies by tag\n')
    for tinfo in summary['tags']:
        issues = tinfo.get('issues', [])
        if issues:
            md.append(f"- {tinfo['tag']}: {', '.join(issues)}\n")

    OUT_REPORT.write_text('\n'.join(md), encoding='utf-8')

    OUT_SELECTED.write_text(json.dumps(summary.get('selected_methods', []), ensure_ascii=False, indent=2), encoding='utf-8')
    # Also write a detailed selection artifact for auditing (includes notes and top candidates)
    OUT_SELECTED_DETAILED.write_text(json.dumps({
        "methods": summary.get('selected_methods', []),
        "note": summary.get('selection_note'),
        "top_candidates": summary.get('top_candidates', []),
    }, ensure_ascii=False, indent=2), encoding='utf-8')

    conf_path = write_confirmatory_schedule(summary.get('selected_methods', []))

    print(f"Wrote summary: {OUT_SUMMARY}")
    print(f"Wrote report: {OUT_REPORT}")
    print(f"Wrote selected methods: {OUT_SELECTED}")
    if conf_path:
        print(f"Wrote confirmatory schedule: {conf_path}")


if __name__ == '__main__':
    main()
