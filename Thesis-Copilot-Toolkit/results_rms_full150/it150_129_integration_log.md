# Integration Log: it150_129
Started: 2026-04-15T00:56:04.329561+00:00
Description: Bulk normalized run it150_129 dataset=synthetic_alpha graph=gaussian miss=[0.2] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2957e-01 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=1.6337e-01 | t=0.0046s
    tikhonov | MR=0.2 | seed=0 | MAE=3.4277e-01 | t=0.0064s
    tv | MR=0.2 | seed=0 | MAE=1.2933e-01 | t=0.1834s
    trss | MR=0.2 | seed=0 | MAE=9.5990e-02 | t=0.0183s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.2492e-01 | t=0.0074s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.5306e-01 | t=0.7629s
    mean | MR=0.2 | seed=1 | MAE=1.2838e-01 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=1.7359e-01 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=3.4241e-01 | t=0.0059s
    tv | MR=0.2 | seed=1 | MAE=1.2827e-01 | t=0.1809s
    trss | MR=0.2 | seed=1 | MAE=9.7029e-02 | t=0.0166s

Completed: 2026-04-15T00:56:04.330372+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.