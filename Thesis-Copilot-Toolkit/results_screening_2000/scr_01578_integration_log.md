# Integration Log: scr_01578
Started: 2026-04-16T09:07:41.353424+00:00
Description: Screening scr_01578 ds=iv100hz_mat graph=kalofolias miss=1ch mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=5.7277e-02 | t=0.0072s
    tv | MR=0.2 | seed=0 | MAE=1.6781e-02 | t=0.1774s
    trss | MR=0.2 | seed=0 | MAE=6.7736e-03 | t=0.0205s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.8058e-02 | t=0.0155s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1605e-01 | t=2.8414s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=1 | MAE=5.6917e-02 | t=0.0080s
    tv | MR=0.2 | seed=1 | MAE=1.6499e-02 | t=0.1896s
    trss | MR=0.2 | seed=1 | MAE=6.7643e-03 | t=0.0198s

Completed: 2026-04-16T09:07:41.354168+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.