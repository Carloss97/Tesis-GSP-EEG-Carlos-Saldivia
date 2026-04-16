# Integration Log: scr_00176
Started: 2026-04-16T14:16:53.487525+00:00
Description: Screening scr_00176 ds=movielens_graph_signal graph=kalofolias miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0031s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0050s
    tikhonov | MR=2ch | seed=0 | MAE=2.0577e-01 | t=0.0086s
    tv | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.5362s
    trss | MR=2ch | seed=0 | MAE=2.6235e-02 | t=0.1355s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.0246e-01 | t=0.0218s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.7799e-01 | t=29.3397s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0031s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0043s
    tikhonov | MR=2ch | seed=1 | MAE=2.0094e-01 | t=0.0152s
    tv | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.4895s
    trss | MR=2ch | seed=1 | MAE=3.2565e-02 | t=0.1202s

Completed: 2026-04-16T14:16:53.488589+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.