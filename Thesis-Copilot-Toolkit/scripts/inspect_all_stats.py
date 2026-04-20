import pandas as pd
import math
from pathlib import Path

R = Path(__file__).resolve().parents[1] / "results"
files = list(R.rglob("*_stats.csv"))
print("FOUND", len(files))
print("name,has_valid,method_count")
for f in files:
    try:
        df = pd.read_csv(f)
        col = None
        for c in ("mae_median", "mae_mean"):
            if c in df.columns:
                col = c
                break
        if col is None:
            hv = False
            mc = 0
        else:
            mc = int(df['method'].nunique()) if 'method' in df.columns else len(df.index)
            hv = False
            for v in df[col].values:
                try:
                    if pd.notna(v) and not math.isinf(float(v)):
                        hv = True
                        break
                except Exception:
                    pass
        print(f.name, hv, mc)
    except Exception as e:
        print(f.name, 'ERR', e)