# Integration Log: scr_00272
Started: 2026-04-16T15:06:02.140426+00:00
Description: Screening scr_00272 ds=movielens_graph_signal graph=gaussian miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0036s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=8.3830e-02 | t=0.0126s
    tv | MR=3ch | seed=0 | MAE=2.3379e-02 | t=0.4806s
    trss | MR=3ch | seed=0 | MAE=2.9534e-02 | t=0.2299s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.5735e-01 | t=0.0210s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4725e-01 | t=16.7183s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0080s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0055s
    tikhonov | MR=3ch | seed=1 | MAE=8.6108e-02 | t=0.0123s
    tv | MR=3ch | seed=1 | MAE=2.1801e-02 | t=0.8482s
    trss | MR=3ch | seed=1 | MAE=3.0503e-02 | t=0.4865s

Completed: 2026-04-16T15:06:02.141303+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.