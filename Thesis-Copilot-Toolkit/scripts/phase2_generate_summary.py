"""Generate human-readable summary from phase2_iteration_stats.csv
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1] / "results" / "tablas_resumen"
IN_CSV = ROOT / "phase2_iteration_stats.csv"
OUT_TXT = Path(__file__).resolve().parents[1] / ".agent_work" / "PHASE2_SUMMARY.txt"
OUT_TXT.parent.mkdir(parents=True, exist_ok=True)


def interpret_row(r):
    a = r.method_a
    b = r.method_b
    p = r.p_value
    n = int(r.n_iterations) if pd.notna(r.n_iterations) else 0
    med = r.median_diff
    cliff = r.cliff_delta
    if pd.isna(p):
        return None
    if p < 0.001:
        sig = "p<0.001"
    else:
        sig = f"p={p:.3g}"
    if pd.isna(med):
        direction = "(no median available)"
    else:
        if med < 0:
            direction = f"{a} BETTER than {b} by {abs(med):.4f} (lower MAE)"
        elif med > 0:
            direction = f"{a} WORSE than {b} by {med:.4f} (higher MAE)"
        else:
            direction = f"no median difference"
    return f"{a} vs {b}: n={n}, {sig}, Cliff's delta={cliff:.3f}, {direction}"


def main():
    if not IN_CSV.exists():
        print("phase2 CSV not found")
        return
    df = pd.read_csv(IN_CSV)
    df = df[df["n_iterations"] >= 30]
    df = df[df["p_value"].notna()]
    df = df.sort_values(by="p_value")
    lines = ["Phase 2 summary: pairwise comparisons\n"]
    for _, r in df.iterrows():
        try:
            s = interpret_row(r)
        except Exception:
            s = None
        if s:
            lines.append(s + "\n")
    OUT_TXT.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote summary to {OUT_TXT}")


if __name__ == '__main__':
    main()
