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


def list_tags() -> List[str]:
    tags = set()
    for p in RESULTS.glob('*_raw.csv'):
        tags.add(p.name.split('_')[0])
    for p in RESULTS.glob('*_stats.csv'):
        tags.add(p.name.split('_')[0])
    return sorted(tags)


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
    tags = list_tags()
    summary = {'n_tags_found': len(tags), 'tags': [], 'issues_overall': {}, 'method_stats_aggregate': [], 'top_methods': []}

    for t in tags:
        info = analyze_tag(t)
        summary['tags'].append(info)
        for iss in info.get('issues',[]):
            summary['issues_overall'][iss] = summary['issues_overall'].get(iss,0) + 1

    grouped = aggregate_methods_from_stats(tags)
    if not grouped.empty:
        # choose selection thresholds
        min_occurrence = max(1, int(0.3 * len(tags)))
        cand = grouped[grouped['occurrence'] >= min_occurrence].sort_values('mae_median_median')
        top_k = 5
        selected = cand['method'].head(top_k).tolist()
        summary['method_stats_aggregate'] = grouped.to_dict(orient='records')
        summary['top_candidates'] = cand.to_dict(orient='records')
        summary['selected_methods'] = selected
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

    conf_path = write_confirmatory_schedule(summary.get('selected_methods', []))

    print(f"Wrote summary: {OUT_SUMMARY}")
    print(f"Wrote report: {OUT_REPORT}")
    print(f"Wrote selected methods: {OUT_SELECTED}")
    if conf_path:
        print(f"Wrote confirmatory schedule: {conf_path}")


if __name__ == '__main__':
    main()
