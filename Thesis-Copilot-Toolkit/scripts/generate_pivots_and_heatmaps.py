#!/usr/bin/env python3
"""
Generate pivot tables and heatmaps (mean MAE) for:
- method x graph
- method x dataset
- method x missing_ratio

Saves CSV pivot tables in `results/analysis/batches/` and PNG heatmaps
in `results/analysis/batches/figures/`.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import sys


def load_csv(path: Path):
    if not path.exists():
        print(f"Missing file: {path}", file=sys.stderr)
        return None
    return pd.read_csv(path)


def make_pivot(df: pd.DataFrame, index: str, columns: str, value: str = "mean_mae"):
    if df is None:
        return None
    for col in (index, columns, value):
        if col not in df.columns:
            print(f"Column {col} not found in dataframe", file=sys.stderr)
            return None
    df[value] = pd.to_numeric(df[value], errors="coerce")
    pivot = df.pivot_table(index=index, columns=columns, values=value, aggfunc="mean")
    # order rows by mean (best -> worst)
    try:
        pivot = pivot.reindex(pivot.mean(axis=1).sort_values().index)
    except Exception:
        pass
    return pivot


def save_pivot_and_heatmap(pivot: pd.DataFrame, out_csv: Path, out_png: Path, title: str):
    pivot.to_csv(out_csv)
    arr = pivot.values
    if np.isnan(arr).all():
        print(f"All NaN in pivot {out_csv}; skipping heatmap")
        return
    vmin = np.nanpercentile(arr, 1)
    vmax = np.nanpercentile(arr, 99)
    plt.figure(figsize=(max(10, pivot.shape[1] * 0.6), max(6, pivot.shape[0] * 0.3)))
    sns.set(font_scale=0.8)
    cmap = "viridis"
    sns.heatmap(pivot, cmap=cmap, linewidths=0.5, linecolor="gray", vmin=vmin, vmax=vmax, cbar_kws={"label": "mean MAE"})
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_png, dpi=200)
    plt.close()
    print(f"Wrote heatmap {out_png}")


def parse_combo_csv(path: Path):
    if not path.exists():
        return None
    df = pd.read_csv(path)
    if 'combo' not in df.columns:
        return df
    parts = df['combo'].astype(str).str.split('|', n=3, expand=True)
    if parts.shape[1] >= 4:
        df = df.copy()
        df['method'] = parts[0].str.strip()
        df['graph'] = parts[1].str.strip()
        df['dataset'] = parts[2].str.strip()
        df['missing_ratio'] = parts[3].str.strip()
    return df


def main():
    parser = argparse.ArgumentParser(description="Generate pivot CSVs and heatmaps from batch global CSVs")
    parser.add_argument("--batches-dir", default=None, help="Path to results/analysis/batches")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    root = script_path.parent.parent
    default_batches = root / "results" / "analysis" / "batches"
    batches_dir = Path(args.batches_dir) if args.batches_dir else default_batches
    if not batches_dir.exists():
        print(f"Batches dir not found: {batches_dir}", file=sys.stderr)
        sys.exit(1)

    fig_dir = batches_dir / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "method_graph": batches_dir / "global_by_method_graph.csv",
        "dataset": batches_dir / "global_by_dataset.csv",
        "missing": batches_dir / "global_by_missing_ratio.csv",
        "overall": batches_dir / "overall_method_ranking.csv",
    }

    df_mg = load_csv(files["method_graph"])
    df_ds = load_csv(files["dataset"])
    df_miss = load_csv(files["missing"])
    df_overall = load_csv(files["overall"])
    # Fallback: if dataset/missing CSVs don't contain per-method rows, parse global_by_combo.csv
    combo_file = batches_dir / "global_by_combo.csv"
    combo_df = None
    if ((df_ds is None or 'method' not in df_ds.columns) or
        (df_miss is None or 'method' not in df_miss.columns)) and combo_file.exists():
        combo_df = parse_combo_csv(combo_file)
        if combo_df is not None:
            # coerce missing_ratio to numeric when available
            if 'missing_ratio' in combo_df.columns:
                combo_df['missing_ratio'] = pd.to_numeric(combo_df['missing_ratio'], errors='coerce')
            if df_ds is None or 'method' not in df_ds.columns:
                df_ds = combo_df
            if df_miss is None or 'method' not in df_miss.columns:
                df_miss = combo_df

    # 1) method x graph
    pivot_mg = make_pivot(df_mg, index="method", columns="graph", value="mean_mae")
    if pivot_mg is not None:
        out_csv = batches_dir / "pivot_method_by_graph_mean_mae.csv"
        out_png = fig_dir / "heatmap_method_graph_mean_mae.png"
        save_pivot_and_heatmap(pivot_mg, out_csv, out_png, "Mean MAE: method × graph")
        print(f"Wrote {out_csv}")

    # 2) method x dataset
    pivot_md = make_pivot(df_ds, index="method", columns="dataset", value="mean_mae")
    if pivot_md is not None:
        out_csv = batches_dir / "pivot_method_by_dataset_mean_mae.csv"
        out_png = fig_dir / "heatmap_method_dataset_mean_mae.png"
        save_pivot_and_heatmap(pivot_md, out_csv, out_png, "Mean MAE: method × dataset")
        print(f"Wrote {out_csv}")

    # 3) method x missing_ratio (try common names)
    if df_miss is not None:
        miss_col = None
        if "missing_ratio" in df_miss.columns:
            miss_col = "missing_ratio"
        elif "missing" in df_miss.columns:
            miss_col = "missing"
        if miss_col:
            pivot_mm = make_pivot(df_miss, index="method", columns=miss_col, value="mean_mae")
            if pivot_mm is not None:
                out_csv = batches_dir / "pivot_method_by_missing_ratio_mean_mae.csv"
                out_png = fig_dir / "heatmap_method_missing_ratio_mean_mae.png"
                save_pivot_and_heatmap(pivot_mm, out_csv, out_png, "Mean MAE: method × missing_ratio")
                print(f"Wrote {out_csv}")
        else:
            print("No missing_ratio column found in global_by_missing_ratio.csv or combo fallback")

    # 4) top20 summary from overall
    if df_overall is not None:
        try:
            df_overall["mean"] = pd.to_numeric(df_overall["mean"], errors="coerce")
            top = df_overall.sort_values("mean").head(20)
            top.to_csv(batches_dir / "top20_methods_by_mean_mae.csv", index=False)
            print("Wrote top20_methods_by_mean_mae.csv")
        except Exception as e:
            print("Error writing top20: ", e, file=sys.stderr)

    print("Done.")


if __name__ == "__main__":
    main()
