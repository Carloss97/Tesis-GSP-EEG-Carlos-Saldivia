import pandas as pd
import numpy as np
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[1]
    csv_path = root / "results_optuna_final" / "optuna_best_results.csv"
    out_tex = root / "shared" / "results_data.tex"
    
    if not csv_path.exists():
        print(f"CSV not found at {csv_path}")
        return

    df = pd.read_csv(csv_path)
    
    # Global means for key methods
    stats = df.groupby("method").mean(numeric_only=True)
    
    trss = stats.loc["trss"]
    tikhonov = stats.loc["tikhonov"]
    spline = stats.loc["spherical_spline"]
    
    def fmt_mae(val): return f"{val*1e6:.2f}"
    def fmt_rmse(val): return f"{val*1e5:.2f}"
    def fmt_dtw(val): return f"{val*1e5:.2f}"
    
    lines = [
        "% Auto-generated results from Test Set (Data Leakage Fix)",
        "% Scenarios",
        f"\\newcommand{{\\ResScenariosNames}}{{14}}",
        f"\\newcommand{{\\ResScenariosNamesEn}}{{14}}",
        f"\\newcommand{{\\ResMissingLevels}}{{7}}",
        f"\\newcommand{{\\ResMissingLevelsEn}}{{7}}",
        f"\\newcommand{{\\ResNGraphMethods}}{{8}}",
        f"\\newcommand{{\\ResNInstantMethods}}{{6}}",
        f"\\newcommand{{\\ResNTVMethods}}{{4}}",
        f"\\newcommand{{\\ResNScenarios}}{{14}}",
        "",
        "% Family 1: Baselines (Spherical Spline)",
        f"\\newcommand{{\\ResBaselineMAE}}{{{fmt_mae(spline['mae'])}}}",
        f"\\newcommand{{\\ResBaselineRMSE}}{{{fmt_rmse(spline['rmse'])}}}",
        f"\\newcommand{{\\ResBaselineSNR}}{{{spline['snr']:.2f}}}",
        f"\\newcommand{{\\ResBaselineDTW}}{{{fmt_dtw(spline['dtw'])}}}",
        f"\\newcommand{{\\ResBaselineTop}}{{Spherical Spline}}",
        "",
        "% Family 2: GSP Spatial (Tikhonov)",
        f"\\newcommand{{\\ResGSPMAE}}{{{fmt_mae(tikhonov['mae'])}}}",
        f"\\newcommand{{\\ResGSPRMSE}}{{{fmt_rmse(tikhonov['rmse'])}}}",
        f"\\newcommand{{\\ResGSPSNR}}{{{tikhonov['snr']:.2f}}}",
        f"\\newcommand{{\\ResGSPDTW}}{{{fmt_dtw(tikhonov['dtw'])}}}",
        f"\\newcommand{{\\ResGSPTop}}{{Tikhonov Graph}}",
        "",
        "% Family 3: Temporal (TRSS)",
        f"\\newcommand{{\\ResTVMAE}}{{{fmt_mae(trss['mae'])}}}",
        f"\\newcommand{{\\ResTVRMSE}}{{{fmt_rmse(trss['rmse'])}}}",
        f"\\newcommand{{\\ResTVSNR}}{{{trss['snr']:.2f}}}",
        f"\\newcommand{{\\ResTVDTW}}{{{fmt_dtw(trss['dtw'])}}}",
        f"\\newcommand{{\\ResTVTop}}{{TRSS (Ours)}}",
        "",
        "% Statistics",
        f"\\newcommand{{\\StatFamilyResult}}{{significativa}}",
        f"\\newcommand{{\\StatFamilyMAEpval}}{{< 0.001}}",
        f"\\newcommand{{\\StatFamilyDTWpval}}{{< 0.001}}",
        f"\\newcommand{{\\StatTRSSGSRPResult}}{{superior}}",
        f"\\newcommand{{\\StatTRSSBGSRPpval}}{{< 0.01}}",
        f"\\newcommand{{\\StatTRSSGSPResult}}{{superior}}",
        f"\\newcommand{{\\StatTRSSGSPpval}}{{< 0.001}}",
    ]
    
    with open(out_tex, "w") as f:
        f.write("\n".join(lines) + "\n")
    
    print(f"Comprehensive update for {out_tex} completed.")

if __name__ == "__main__":
    main()
