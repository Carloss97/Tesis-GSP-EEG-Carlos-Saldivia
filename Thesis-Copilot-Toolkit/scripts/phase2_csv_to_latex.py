"""Convert phase2_iteration_stats.csv into a formatted LaTeX table.

Outputs: results/tablas_resumen/phase2_results_table.tex
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1] / "results" / "tablas_resumen"
IN_CSV = ROOT / "phase2_iteration_stats.csv"
OUT_TEX = ROOT / "phase2_results_table.tex"


def fmt(x):
    try:
        if pd.isna(x):
            return "-"
        if abs(x) < 1e-3 and x != 0:
            return f"{x:.2e}"
        return f"{x:.4f}"
    except Exception:
        return str(x)


def main():
    if not IN_CSV.exists():
        print(f"Input CSV not found: {IN_CSV}")
        return
    df = pd.read_csv(IN_CSV)
    # keep rows with numeric p_value
    df = df[df["n_iterations"].notna()]
    # replace infinite / missing p-values
    df["p_value"] = pd.to_numeric(df["p_value"], errors="coerce")
    df = df.sort_values(by=["p_value"], na_position="last")
    top = df.head(40)

    header = (
        "\\begin{table}[ht]\n\\centering\n\\small\n"
        "\\caption{Phase 2 pairwise comparisons (Wilcoxon, Cliff's delta, bootstrap 95\\% CI).}" 
        "\\label{tab:phase2_pairwise}\n"
        "\\begin{tabular}{l l r r r r r}\n\\hline\n"
        "Method A & Method B & n & p-value & Cliff's $\delta$ & Median diff & 95\\% CI \\\\ \n\\hline\n"
    )

    lines = [header]
    for _, r in top.iterrows():
        a = r.method_a
        b = r.method_b
        n = int(r.n_iterations) if pd.notna(r.n_iterations) else 0
        p = fmt(r.p_value)
        cliff = fmt(r.cliff_delta)
        med = fmt(r.median_diff)
        ci_lo = fmt(r.ci_lo)
        ci_hi = fmt(r.ci_hi)
        ci = f"[{ci_lo}, {ci_hi}]" if ci_lo != "-" and ci_hi != "-" else "-"
        lines.append(f"{a} & {b} & {n} & {p} & {cliff} & {med} & {ci} \\\\ \n")

    footer = "\\hline\n\\end{tabular}\n\\end{table}\n"
    lines.append(footer)

    OUT_TEX.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote LaTeX table to {OUT_TEX}")


if __name__ == '__main__':
    main()
